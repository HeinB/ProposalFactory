#!/usr/bin/env python3
"""
rse.py — Risk Selection Engine v1.0
PF2-001 — Proposal Factory Risk Selection Engine
Knowledge Platform Version 1.0

Input:  Tender Context YAML (mandatory)
        RSE Extension YAML (optional — adds RSE-specific fields)
Reads:  ENTERPRISE_RISK_REGISTER_V1.md (auto-located relative to script)
Output: SELECTED_RISK_REGISTER_[TenderID].md
        RISK_SELECTION_AUDIT_[TenderID].md

Selection is 100% deterministic. No AI judgement. No probabilistic ranking.
All selections are driven by AREL V1.0 expressions (mandatory_if / optional_if /
excluded_if) from the approved Enterprise Risk Register.

Design notes:
  - List-aware contains: `modules contains "Oracle Learning"` matches any
    module whose name contains "Oracle Learning" as a substring.
  - Country normalization: "RSA" -> "ZA" (AREL expressions use ISO 3166-1 alpha-2).
  - Platform alias: "OIC" in expressions maps to "Oracle Integration Cloud".
  - ERR expression normalization: CONTAINS->contains, AND->and, OR->or,
    NOT->not, standalone = -> ==.
"""

import argparse
import os
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto
from typing import Any, Dict, List, Optional

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────

ENGINE_VERSION = "1.0"
AREL_VERSION = "1.0"
BUILD_DATE = "2026-06-29"

_HERE = os.path.dirname(os.path.abspath(__file__))
RISK_REGISTER_DEFAULT = os.path.join(_HERE, "..", "Risk_Library", "ENTERPRISE_RISK_REGISTER_V1.md")
OUTPUT_DIR_DEFAULT = os.path.join(_HERE, "..", "Reports")

PATTERN_NAMES: Dict[str, str] = {
    "P1": "HCM Full Suite Single",
    "P2": "HCM Full Suite Phased",
    "P3": "HCM + Payroll Integration",
    "P4": "Recruiting Standalone",
    "P5": "Learning Standalone",
    "P6": "OIC Standalone",
    "P7": "ERP Multi-Module",
    "P8": "ERP Single Module",
    "P9": "EBS Implementation",
    "P10": "DBA / Managed Services",
    "P11": "Acumatica",
    "P12": "BeBanking",
    "P13": "AMS",
}

PRIORITY_ORDER: Dict[str, int] = {"Critical": 0, "High": 1, "Standard": 2, "Low": 3}
RATING_ORDER: Dict[str, int] = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}

# ─────────────────────────────────────────────────────────────────────────────
# AREL V1.0 TOKENIZER
# ─────────────────────────────────────────────────────────────────────────────

class TT(Enum):
    STR = auto(); NUM = auto(); BOOL = auto(); KW = auto(); OP = auto()
    VAR = auto(); LBRACKET = auto(); RBRACKET = auto()
    LPAREN = auto(); RPAREN = auto(); COMMA = auto(); EOF = auto()


@dataclass
class Token:
    type: TT
    val: Any


def _tokenize(expr: str) -> List[Token]:
    tokens: List[Token] = []
    i = 0
    n = len(expr)
    while i < n:
        c = expr[i]
        if c in " \t\n":
            i += 1; continue
        if c == '"':
            j = i + 1
            while j < n and expr[j] != '"':
                j += 1
            tokens.append(Token(TT.STR, expr[i+1:j]))
            i = j + 1; continue
        if c == '[': tokens.append(Token(TT.LBRACKET, '[')); i += 1; continue
        if c == ']': tokens.append(Token(TT.RBRACKET, ']')); i += 1; continue
        if c == '(': tokens.append(Token(TT.LPAREN,   '(')); i += 1; continue
        if c == ')': tokens.append(Token(TT.RPAREN,   ')')); i += 1; continue
        if c == ',': tokens.append(Token(TT.COMMA,    ',')); i += 1; continue
        if i + 1 < n and expr[i:i+2] in ('==', '!=', '>=', '<='):
            tokens.append(Token(TT.OP, expr[i:i+2])); i += 2; continue
        if c in ('>', '<'):
            tokens.append(Token(TT.OP, c)); i += 1; continue
        if c.isdigit() or (c == '-' and i+1 < n and expr[i+1].isdigit()):
            j = i + 1
            while j < n and (expr[j].isdigit() or expr[j] == '.'):
                j += 1
            s = expr[i:j]
            tokens.append(Token(TT.NUM, float(s) if '.' in s else int(s)))
            i = j; continue
        if c.isalpha() or c == '_':
            j = i
            while j < n and (expr[j].isalnum() or expr[j] == '_'):
                j += 1
            word = expr[i:j]
            up = word.upper()
            if up == 'TRUE':
                tokens.append(Token(TT.BOOL, True))
            elif up == 'FALSE':
                tokens.append(Token(TT.BOOL, False))
            elif word in ('and', 'or', 'not', 'in', 'contains'):
                tokens.append(Token(TT.KW, word))
            else:
                tokens.append(Token(TT.VAR, word))
            i = j; continue
        i += 1  # skip unknown character
    tokens.append(Token(TT.EOF, None))
    return tokens


# ─────────────────────────────────────────────────────────────────────────────
# AREL V1.0 RECURSIVE-DESCENT EVALUATOR (RSE variant)
# ─────────────────────────────────────────────────────────────────────────────

class RSEARELEvaluator:
    """
    AREL V1.0 recursive-descent evaluator.

    RSE variant differences from KVE variant:
      - contains on list variables uses substring match on each element
        (so `modules contains "Oracle Learning"` matches "Oracle Learning Cloud")
      - Resolves variables via getattr(ctx, name, None) — works with RSEContext
        which includes RSE-specific extension fields beyond the 20 AREL variables.
    """

    def __init__(self, ctx: Any) -> None:
        self.ctx = ctx
        self._tokens: List[Token] = []
        self._pos: int = 0

    def evaluate(self, expr: str) -> bool:
        if not expr or not expr.strip():
            return False
        stripped = expr.strip()
        if stripped.upper() == 'TRUE':
            return True
        if stripped.upper() == 'FALSE':
            return False
        self._tokens = _tokenize(expr)
        self._pos = 0
        try:
            result = self._parse_or()
            return bool(result)
        except Exception:
            return False

    def _cur(self) -> Token:
        return self._tokens[self._pos] if self._pos < len(self._tokens) else Token(TT.EOF, None)

    def _consume(self) -> Token:
        tok = self._cur()
        self._pos += 1
        return tok

    def _expect(self, tt: TT) -> Token:
        tok = self._cur()
        if tok.type != tt:
            raise ValueError(f"Expected {tt}, got {tok}")
        return self._consume()

    def _expect_kw(self, kw: str) -> Token:
        tok = self._cur()
        if tok.type != TT.KW or tok.val != kw:
            raise ValueError(f"Expected keyword '{kw}', got {tok}")
        return self._consume()

    def _var(self, name: str) -> Any:
        return getattr(self.ctx, name, None)

    # Grammar: or → and { "or" and }
    def _parse_or(self) -> bool:
        left = self._parse_and()
        while self._cur().type == TT.KW and self._cur().val == 'or':
            self._consume()
            right = self._parse_and()
            left = left or right
        return left

    # Grammar: and → not { "and" not }
    def _parse_and(self) -> bool:
        left = self._parse_not()
        while self._cur().type == TT.KW and self._cur().val == 'and':
            self._consume()
            right = self._parse_not()
            left = left and right
        return left

    # Grammar: not → "not" not | atom
    def _parse_not(self) -> bool:
        if self._cur().type == TT.KW and self._cur().val == 'not':
            self._consume()
            return not self._parse_not()
        return self._parse_atom()

    # Grammar: atom → "(" or ")" | BOOL | comparison
    def _parse_atom(self) -> bool:
        tok = self._cur()
        if tok.type == TT.LPAREN:
            self._consume()
            val = self._parse_or()
            self._expect(TT.RPAREN)
            return val
        if tok.type == TT.BOOL:
            self._consume()
            return tok.val
        return self._parse_cmp()

    # Grammar: comparison → VAR OP scalar | VAR "in" list | VAR "not" "in" list
    #                      | VAR "contains" scalar | VAR (standalone bool)
    def _parse_cmp(self) -> bool:
        tok = self._expect(TT.VAR)
        left = self._var(tok.val)
        nxt = self._cur()

        if nxt.type == TT.KW and nxt.val == 'not':
            self._consume()
            self._expect_kw('in')
            rhs = self._parse_list()
            return False if left is None else left not in rhs

        if nxt.type == TT.KW and nxt.val == 'in':
            self._consume()
            rhs = self._parse_list()
            return False if left is None else left in rhs

        if nxt.type == TT.KW and nxt.val == 'contains':
            self._consume()
            rhs = self._parse_scalar()
            if left is None:
                return False
            # RSE: list-aware substring match
            if isinstance(left, list):
                return any(str(rhs) in str(el) for el in left)
            if isinstance(left, str):
                return str(rhs) in left
            return False

        if nxt.type == TT.OP:
            self._consume()
            rhs = self._parse_scalar()
            return self._cmp(left, nxt.val, rhs)

        # Standalone VAR — treat as boolean
        return bool(left) if left is not None else False

    def _cmp(self, left: Any, op: str, right: Any) -> bool:
        if left is None:
            return False
        try:
            if op == '==':
                # Type-safe: Python bool vs str/int never equal
                if isinstance(left, bool) != isinstance(right, bool):
                    if isinstance(left, bool) or isinstance(right, bool):
                        return False
                return str(left) == str(right) if isinstance(right, str) else left == right
            if op == '!=':
                if isinstance(left, bool) != isinstance(right, bool):
                    if isinstance(left, bool) or isinstance(right, bool):
                        return True
                return str(left) != str(right) if isinstance(right, str) else left != right
            if op == '>':  return float(left) > float(right)
            if op == '>=': return float(left) >= float(right)
            if op == '<':  return float(left) < float(right)
            if op == '<=': return float(left) <= float(right)
        except (TypeError, ValueError):
            return False
        return False

    def _parse_scalar(self) -> Any:
        tok = self._cur()
        if tok.type in (TT.STR, TT.NUM, TT.BOOL):
            self._consume()
            return tok.val
        if tok.type == TT.VAR:
            self._consume()
            return self._var(tok.val)
        raise ValueError(f"Expected scalar, got {tok}")

    def _parse_list(self) -> List[Any]:
        self._expect(TT.LBRACKET)
        items: List[Any] = []
        while self._cur().type != TT.RBRACKET:
            items.append(self._parse_scalar())
            if self._cur().type == TT.COMMA:
                self._consume()
        self._expect(TT.RBRACKET)
        return items


# ─────────────────────────────────────────────────────────────────────────────
# CONTEXT
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class RSEContext:
    # ── 20 KVE AREL context variables ──────────────────────────────────────
    tender_id:              str            = ""
    pattern:                str            = ""
    platform:               str            = ""
    engagement_type:        str            = ""
    modules:                List[str]      = field(default_factory=list)
    country:                str            = ""
    client_size:            str            = "Enterprise"
    client_sector:          str            = "All"
    am_clearances:          List[str]      = field(default_factory=list)
    ptc_clearances:         List[str]      = field(default_factory=list)
    tender_date:            str            = ""
    industry:               str            = ""
    bom:                    List[str]      = field(default_factory=list)
    payroll_integration:    Optional[bool] = None
    oci_in_scope:           Optional[bool] = None
    client_has_oic:         Optional[bool] = None
    dr_in_scope:            Optional[bool] = None
    security_in_scope:      Optional[bool] = None
    migration_scope:        Optional[bool] = None
    integration_scope:      Optional[bool] = None
    support_scope:          Optional[bool] = None
    pricing_type:           str            = ""
    project_duration_months: Optional[float] = None
    # ── RSE extension fields (AREL expressions in ERR use these) ──────────
    integration_count:                    Optional[int]  = None
    third_party_api:                      Optional[bool] = None
    payroll_provider:                     str            = ""
    oax_in_scope:                         Optional[bool] = None
    analytics_requirements_in_tender:     Optional[bool] = None
    oda_in_scope:                         Optional[bool] = None
    digital_channels:                     Optional[bool] = None
    feature_licensing_confirmed:          Optional[bool] = None
    help_desk_in_scope:                   Optional[bool] = None
    personal_data_in_scope:               Optional[bool] = None
    integration_method_prescribed_in_tender: Optional[bool] = None
    delivery_model:                       str            = ""
    phase_count:                          Optional[int]  = None
    fixed_price:                          Optional[bool] = None


def load_rse_context(context_path: str, extension_path: Optional[str] = None) -> RSEContext:
    with open(context_path, encoding="utf-8") as f:
        raw = yaml.safe_load(f)
    tc = raw.get("tender_context", raw)

    ctx = RSEContext(
        tender_id             = tc.get("tender_id", ""),
        pattern               = tc.get("pattern", ""),
        platform              = tc.get("platform", ""),
        engagement_type       = tc.get("engagement_type", ""),
        modules               = tc.get("modules", []),
        country               = tc.get("country", ""),
        client_size           = tc.get("client_size", "Enterprise"),
        client_sector         = tc.get("client_sector", "All"),
        am_clearances         = tc.get("am_clearances", []),
        ptc_clearances        = tc.get("ptc_clearances", []),
        tender_date           = tc.get("tender_date", ""),
        industry              = tc.get("industry", ""),
        bom                   = tc.get("bom", []),
        payroll_integration   = tc.get("payroll_integration"),
        oci_in_scope          = tc.get("oci_in_scope"),
        client_has_oic        = tc.get("client_has_oic"),
        dr_in_scope           = tc.get("dr_in_scope"),
        security_in_scope     = tc.get("security_in_scope"),
        migration_scope       = tc.get("migration_scope"),
        integration_scope     = tc.get("integration_scope"),
        support_scope         = tc.get("support_scope"),
        pricing_type          = tc.get("pricing_type", ""),
        project_duration_months = tc.get("project_duration_months"),
    )

    # Country normalization: RSA → ZA (ERR AREL expressions use ISO 3166-1 alpha-2)
    if ctx.country == "RSA":
        ctx.country = "ZA"

    # Derive fixed_price from pricing_type
    if ctx.pricing_type:
        ctx.fixed_price = ctx.pricing_type.strip().lower() in (
            "fixed price", "fixed-price", "fixed"
        )

    # RSE extension YAML (optional)
    if extension_path and os.path.exists(extension_path):
        with open(extension_path, encoding="utf-8") as f:
            ext = yaml.safe_load(f).get("rse_extension", {})
        ctx.integration_count                    = ext.get("integration_count")
        ctx.third_party_api                      = ext.get("third_party_api")
        ctx.payroll_provider                     = ext.get("payroll_provider", "")
        ctx.oax_in_scope                         = ext.get("oax_in_scope")
        ctx.analytics_requirements_in_tender     = ext.get("analytics_requirements_in_tender")
        ctx.oda_in_scope                         = ext.get("oda_in_scope")
        ctx.digital_channels                     = ext.get("digital_channels")
        ctx.feature_licensing_confirmed          = ext.get("feature_licensing_confirmed")
        ctx.help_desk_in_scope                   = ext.get("help_desk_in_scope")
        ctx.personal_data_in_scope               = ext.get("personal_data_in_scope")
        ctx.integration_method_prescribed_in_tender = ext.get("integration_method_prescribed_in_tender")
        ctx.delivery_model                       = ext.get("delivery_model", "")
        ctx.phase_count                          = ext.get("phase_count")

    return ctx


# ─────────────────────────────────────────────────────────────────────────────
# ENTERPRISE RISK REGISTER PARSER
# ─────────────────────────────────────────────────────────────────────────────

@dataclass
class RSKRecord:
    risk_id:             str
    title:               str
    category:            str
    rating:              str
    likelihood:          str
    impact:              str
    owner:               str
    lifecycle_status:    str
    proposal_patterns:   List[str]   # ["P1", "P2", ...]
    assembly_priority:   str
    mandatory_if_raw:    str
    optional_if_raw:     str
    excluded_if_raw:     str
    related_assumptions: List[str]
    proposal_sections:   str
    description_summary: str


def _table_val(lines: List[str], field_name: str) -> str:
    pat = re.compile(
        r"^\|\s*\*\*" + re.escape(field_name) + r"\*\*\s*\|\s*(.+?)\s*\|"
    )
    for line in lines:
        m = pat.match(line.strip())
        if m:
            return m.group(1).strip()
    return ""


def parse_risk_register(path: str) -> List[RSKRecord]:
    with open(path, encoding="utf-8") as f:
        content = f.read()

    records: List[RSKRecord] = []
    sections = re.split(r"\n(?=### RC-)", content)

    for sec in sections:
        if not sec.strip().startswith("### RC-"):
            continue
        m = re.match(r"### (RC-[A-Z]+-\d+)\s*[—-]+\s*(.+)", sec.strip())
        if not m:
            continue
        risk_id = m.group(1).strip()
        title   = m.group(2).strip()

        lines = sec.split("\n")

        def gf(name: str) -> str:
            return _table_val(lines, name)

        # Parse proposal patterns: "1, 2, 3" → ["P1", "P2", "P3"]
        pat_raw = gf("Proposal patterns")
        patterns: List[str] = []
        if pat_raw and pat_raw not in ("—", "-", ""):
            for p in re.split(r"[,\s]+", pat_raw):
                p = p.strip()
                if p.isdigit():
                    patterns.append(f"P{p}")

        # Related assumptions
        asm_raw = gf("Related assumptions")
        assumptions: List[str] = []
        if asm_raw and asm_raw not in ("—", "-", ""):
            assumptions = [a.strip() for a in asm_raw.split(",") if a.strip()]

        # Description summary: first sentence of Risk description paragraph
        desc_m = re.search(r"\*\*Risk description:\*\*\s*(.+?)(?:\n|$)", sec)
        summary = desc_m.group(1).strip() if desc_m else ""
        if summary and not summary.endswith("."):
            summary += "."

        def clean(val: str) -> str:
            return "" if val in ("—", "-") else val

        records.append(RSKRecord(
            risk_id             = risk_id,
            title               = title,
            category            = gf("Category"),
            rating              = gf("Rating"),
            likelihood          = gf("Likelihood"),
            impact              = gf("Impact"),
            owner               = gf("Owner"),
            lifecycle_status    = gf("Lifecycle status"),
            proposal_patterns   = patterns,
            assembly_priority   = gf("Assembly priority"),
            mandatory_if_raw    = clean(gf("Mandatory if")),
            optional_if_raw     = clean(gf("Optional if")),
            excluded_if_raw     = clean(gf("Excluded if")),
            related_assumptions = assumptions,
            proposal_sections   = gf("Proposal sections"),
            description_summary = summary,
        ))

    return records


# ─────────────────────────────────────────────────────────────────────────────
# AREL EXPRESSION NORMALIZATION
# ─────────────────────────────────────────────────────────────────────────────

def normalize_arel(expr: str) -> str:
    """
    Normalize ERR-format AREL expressions to strict AREL V1.0 syntax.

    Transformations:
      - CONTAINS → contains  (case normalization)
      - AND → and, OR → or, NOT → not
      - Standalone = → ==   (not part of !=, >=, <=, ==)
      - "OIC" → "Oracle Integration Cloud"  (platform alias)
    """
    if not expr or expr.strip() in ("", "—", "-"):
        return expr
    stripped = expr.strip()
    if stripped.upper() in ("TRUE", "FALSE"):
        return stripped.upper()

    # 1. Keyword case normalization (word-boundary safe)
    expr = re.sub(r"\bCONTAINS\b", "contains", expr)
    expr = re.sub(r"\bAND\b",      "and",      expr)
    expr = re.sub(r"\bOR\b",       "or",       expr)
    expr = re.sub(r"\bNOT\b",      "not",      expr)

    # 2. Standalone = → == (not part of !=, >=, <=, ==)
    expr = re.sub(r"(?<![!<>=])=(?![=])", "==", expr)

    # 3. Platform alias: "OIC" → "Oracle Integration Cloud"
    expr = expr.replace('"OIC"', '"Oracle Integration Cloud"')

    return expr.strip()


# ─────────────────────────────────────────────────────────────────────────────
# SELECTION
# ─────────────────────────────────────────────────────────────────────────────

S_MANDATORY          = "MANDATORY"
S_OPTIONAL_SELECTED  = "OPTIONAL_SELECTED"
S_EXCLUDED           = "EXCLUDED"
S_PATTERN_EXCLUDED   = "PATTERN_EXCLUDED"
S_DEFAULT_EXCLUDED   = "DEFAULT_EXCLUDED"
S_LIFECYCLE_EXCLUDED = "LIFECYCLE_EXCLUDED"

SELECTED = {S_MANDATORY, S_OPTIONAL_SELECTED}


@dataclass
class SelectionResult:
    risk:                 RSKRecord
    status:               str
    mandatory_if_norm:    str            = ""
    optional_if_norm:     str            = ""
    excluded_if_norm:     str            = ""
    mandatory_if_result:  Optional[bool] = None
    optional_if_result:   Optional[bool] = None
    excluded_if_result:   Optional[bool] = None
    selection_reason:     str            = ""


def _eval(ev: RSEARELEvaluator, expr: str) -> Optional[bool]:
    if not expr or expr.strip() in ("", "—", "-"):
        return None
    if expr.strip().upper() == "TRUE":
        return True
    if expr.strip().upper() == "FALSE":
        return False
    try:
        return ev.evaluate(expr)
    except Exception:
        return None


def select_risks(risks: List[RSKRecord], ctx: RSEContext) -> List[SelectionResult]:
    ev = RSEARELEvaluator(ctx)
    results: List[SelectionResult] = []

    for risk in risks:
        # ── Lifecycle filter ────────────────────────────────────────────────
        if risk.lifecycle_status.upper() != "APPROVED":
            results.append(SelectionResult(
                risk=risk, status=S_LIFECYCLE_EXCLUDED,
                selection_reason=f"lifecycle_status={risk.lifecycle_status!r}",
            ))
            continue

        # ── Pattern filter ──────────────────────────────────────────────────
        if ctx.pattern and risk.proposal_patterns:
            if ctx.pattern not in risk.proposal_patterns:
                results.append(SelectionResult(
                    risk=risk, status=S_PATTERN_EXCLUDED,
                    selection_reason=(
                        f"Pattern {ctx.pattern} not in applicable patterns "
                        f"{risk.proposal_patterns}"
                    ),
                ))
                continue

        # ── Normalize expressions ────────────────────────────────────────────
        mand_n = normalize_arel(risk.mandatory_if_raw)
        opt_n  = normalize_arel(risk.optional_if_raw)
        excl_n = normalize_arel(risk.excluded_if_raw)

        # ── Evaluate ─────────────────────────────────────────────────────────
        excl_r = _eval(ev, excl_n)
        mand_r = _eval(ev, mand_n)
        opt_r  = _eval(ev, opt_n)

        # ── Classify ─────────────────────────────────────────────────────────
        if excl_r is True:
            status = S_EXCLUDED
            reason = f"excluded_if → TRUE: {excl_n}"
        elif mand_r is True:
            status = S_MANDATORY
            reason = f"mandatory_if → TRUE: {mand_n}"
        elif opt_r is True:
            status = S_OPTIONAL_SELECTED
            reason = f"optional_if → TRUE: {opt_n}"
        else:
            status = S_DEFAULT_EXCLUDED
            reason = "No selection condition resolved to TRUE (conditions unresolvable or FALSE)"

        results.append(SelectionResult(
            risk=risk,
            status=status,
            mandatory_if_norm=mand_n,
            optional_if_norm=opt_n,
            excluded_if_norm=excl_n,
            mandatory_if_result=mand_r,
            optional_if_result=opt_r,
            excluded_if_result=excl_r,
            selection_reason=reason,
        ))

    return results


def validate_selections(results: List[SelectionResult]) -> List[str]:
    violations: List[str] = []
    selected = [r for r in results if r.status in SELECTED]

    # V-001: No duplicate risk IDs in selected set
    ids = [r.risk.risk_id for r in selected]
    if len(ids) != len(set(ids)):
        violations.append("V-001 FAIL: Duplicate risk IDs in selected set")

    # V-002: No contradictions (mandatory AND excluded both TRUE)
    for r in results:
        if r.excluded_if_result and r.mandatory_if_result:
            violations.append(
                f"V-002 FAIL: Contradiction — {r.risk.risk_id} is both "
                f"mandatory_if=TRUE and excluded_if=TRUE"
            )

    # V-003: RC-OPS-001 must be MANDATORY or EXCLUDED (never default-excluded
    #        unless engagement is DBA/BeBanking non-applicable)
    ops = next((r for r in results if r.risk.risk_id == "RC-OPS-001"), None)
    if ops and ops.status == S_DEFAULT_EXCLUDED:
        violations.append(
            "V-003 WARN: RC-OPS-001 (unconditional mandatory risk) resolved "
            "to DEFAULT_EXCLUDED — verify mandatory_if expression"
        )

    return violations


# ─────────────────────────────────────────────────────────────────────────────
# OUTPUT GENERATORS
# ─────────────────────────────────────────────────────────────────────────────

def _sort_key(r: SelectionResult) -> tuple:
    p = PRIORITY_ORDER.get(r.risk.assembly_priority, 9)
    g = RATING_ORDER.get(r.risk.rating.upper(), 9)
    return (p, g, r.risk.risk_id)


def generate_risk_register_md(
    results: List[SelectionResult],
    ctx: RSEContext,
    violations: List[str],
) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    selected  = sorted([r for r in results if r.status in SELECTED],    key=_sort_key)
    mandatory = [r for r in selected if r.status == S_MANDATORY]
    optional_s = [r for r in selected if r.status == S_OPTIONAL_SELECTED]
    excl      = [r for r in results  if r.status == S_EXCLUDED]
    pat_excl  = [r for r in results  if r.status == S_PATTERN_EXCLUDED]
    def_excl  = [r for r in results  if r.status == S_DEFAULT_EXCLUDED]

    lines = [
        f"---",
        f"document_id: SELECTED-RISK-REGISTER-{ctx.tender_id}",
        f"title: \"Selected Proposal Risk Register — {ctx.tender_id}\"",
        f"version: \"1.0\"",
        f"status: \"GENERATED\"",
        f"generated: \"{now}\"",
        f"engine: \"RSE v{ENGINE_VERSION} / AREL V{AREL_VERSION}\"",
        f"tender_id: \"{ctx.tender_id}\"",
        f"pattern: \"{ctx.pattern}\"",
        f"platform: \"{ctx.platform}\"",
        f"engagement_type: \"{ctx.engagement_type}\"",
        f"---",
        f"",
        f"# Selected Proposal Risk Register — {ctx.tender_id}",
        f"",
        f"**Generated:** {now}  ",
        f"**Engine:** Risk Selection Engine v{ENGINE_VERSION} | AREL V{AREL_VERSION}  ",
        f"**Tender:** {ctx.tender_id} | Pattern: {ctx.pattern} ({PATTERN_NAMES.get(ctx.pattern, 'Unknown')})  ",
        f"**Platform:** {ctx.platform} | Engagement: {ctx.engagement_type}  ",
        f"",
        f"---",
        f"",
        f"## Summary",
        f"",
        f"| Metric | Count |",
        f"|---|---|",
        f"| Risks evaluated | {len(results)} |",
        f"| **Selected (total)** | **{len(selected)}** |",
        f"| — Mandatory | {len(mandatory)} |",
        f"| — Optional (selected) | {len(optional_s)} |",
        f"| Excluded (excluded_if TRUE) | {len(excl)} |",
        f"| Pattern-excluded | {len(pat_excl)} |",
        f"| Default-excluded | {len(def_excl)} |",
        f"| Validation violations | {len(violations)} |",
        f"",
    ]

    if violations:
        lines += ["## Validation Violations", ""]
        for v in violations:
            lines.append(f"- {v}")
        lines.append("")

    lines += [
        "---",
        "",
        "## Selected Risks",
        "",
        "Sorted by assembly priority (Critical → High → Standard), then rating.",
        "",
    ]

    for r in selected:
        risk = r.risk
        badge = "**[MANDATORY]**" if r.status == S_MANDATORY else "**[OPTIONAL]**"
        lines += [
            f"### {risk.risk_id} — {risk.title} {badge} [{risk.rating}]",
            f"",
            f"| Field | Value |",
            f"|---|---|",
            f"| **Risk ID** | {risk.risk_id} |",
            f"| **Category** | {risk.category} |",
            f"| **Rating** | {risk.rating} |",
            f"| **Likelihood × Impact** | {risk.likelihood} × {risk.impact} |",
            f"| **Assembly priority** | {risk.assembly_priority} |",
            f"| **Selection status** | {r.status} |",
            f"| **Why selected** | {r.selection_reason} |",
            f"| **Source rule** | mandatory_if: `{risk.mandatory_if_raw}` |",
            f"| **Owner** | {risk.owner} |",
            f"| **Proposal sections** | {risk.proposal_sections} |",
            f"| **Related assumptions** | {', '.join(risk.related_assumptions) if risk.related_assumptions else '—'} |",
            f"| **Applicable patterns** | {', '.join(risk.proposal_patterns)} |",
            f"",
            f"> {risk.description_summary}",
            f"",
        ]

    lines += [
        "---",
        "",
        "## Excluded Risks (excluded_if TRUE)",
        "",
        "| Risk ID | Title | Rating | Excluded If |",
        "|---|---|---|---|",
    ]
    for r in sorted(excl, key=_sort_key):
        lines.append(
            f"| {r.risk.risk_id} | {r.risk.title} | {r.risk.rating} "
            f"| `{r.risk.excluded_if_raw}` |"
        )

    lines += [
        "",
        "---",
        "",
        "## Pattern-Excluded Risks",
        "",
        f"The following risks are not applicable to pattern {ctx.pattern} ({PATTERN_NAMES.get(ctx.pattern, '')}).",
        "",
        "| Risk ID | Title | Applicable Patterns |",
        "|---|---|---|",
    ]
    for r in sorted(pat_excl, key=lambda x: x.risk.risk_id):
        lines.append(
            f"| {r.risk.risk_id} | {r.risk.title} "
            f"| {', '.join(r.risk.proposal_patterns)} |"
        )

    lines += [
        "",
        "---",
        "",
        "## Default-Excluded Risks",
        "",
        "Risks that are pattern-applicable but where no AREL condition resolved to TRUE.",
        "These risks may become MANDATORY or OPTIONAL if additional RSE extension fields",
        "are provided (e.g., oax_in_scope, integration_count, personal_data_in_scope).",
        "",
        "| Risk ID | Title | Rating | Unresolved Conditions |",
        "|---|---|---|---|",
    ]
    for r in sorted(def_excl, key=_sort_key):
        conds = []
        if r.risk.mandatory_if_raw:
            conds.append(f"mandatory_if: `{r.risk.mandatory_if_raw}`")
        if r.risk.optional_if_raw:
            conds.append(f"optional_if: `{r.risk.optional_if_raw}`")
        cond_str = " | ".join(conds) if conds else "—"
        lines.append(
            f"| {r.risk.risk_id} | {r.risk.title} | {r.risk.rating} | {cond_str} |"
        )

    lines += ["", "---", "", f"*Generated by RSE v{ENGINE_VERSION} — {now}*", ""]
    return "\n".join(lines)


def generate_audit_md(
    results: List[SelectionResult],
    ctx: RSEContext,
    violations: List[str],
) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    selected = [r for r in results if r.status in SELECTED]

    def fmt_eval(expr: str, result: Optional[bool]) -> str:
        if not expr:
            return "—"
        r_str = "TRUE" if result is True else ("FALSE" if result is False else "?")
        return f"`{expr}` → {r_str}"

    lines = [
        f"---",
        f"document_id: RISK-SELECTION-AUDIT-{ctx.tender_id}",
        f"title: \"Risk Selection Audit — {ctx.tender_id}\"",
        f"version: \"1.0\"",
        f"status: \"GENERATED\"",
        f"generated: \"{now}\"",
        f"engine: \"RSE v{ENGINE_VERSION} / AREL V{AREL_VERSION}\"",
        f"---",
        f"",
        f"# Risk Selection Audit — {ctx.tender_id}",
        f"",
        f"**Generated:** {now}  ",
        f"**Engine:** RSE v{ENGINE_VERSION} | AREL V{AREL_VERSION}  ",
        f"**Tender:** {ctx.tender_id} | {ctx.pattern} | {ctx.platform} | {ctx.engagement_type}  ",
        f"",
        f"---",
        f"",
        f"## Audit Summary",
        f"",
        f"| Metric | Value |",
        f"|---|---|",
        f"| Risks evaluated | {len(results)} |",
        f"| MANDATORY | {sum(1 for r in results if r.status == S_MANDATORY)} |",
        f"| OPTIONAL_SELECTED | {sum(1 for r in results if r.status == S_OPTIONAL_SELECTED)} |",
        f"| EXCLUDED | {sum(1 for r in results if r.status == S_EXCLUDED)} |",
        f"| PATTERN_EXCLUDED | {sum(1 for r in results if r.status == S_PATTERN_EXCLUDED)} |",
        f"| DEFAULT_EXCLUDED | {sum(1 for r in results if r.status == S_DEFAULT_EXCLUDED)} |",
        f"| **Total selected** | **{len(selected)}** |",
        f"| Validation violations | {len(violations)} |",
        f"",
        f"---",
        f"",
        f"## Tender Context Used",
        f"",
        f"| Field | Value |",
        f"|---|---|",
        f"| tender_id | {ctx.tender_id} |",
        f"| pattern | {ctx.pattern} |",
        f"| platform | {ctx.platform} |",
        f"| engagement_type | {ctx.engagement_type} |",
        f"| modules | {', '.join(ctx.modules) if ctx.modules else '—'} |",
        f"| country | {ctx.country} |",
        f"| client_size | {ctx.client_size} |",
        f"| client_sector | {ctx.client_sector} |",
        f"| payroll_integration | {ctx.payroll_integration} |",
        f"| pricing_type | {ctx.pricing_type or '—'} |",
        f"| fixed_price | {ctx.fixed_price} |",
        f"| integration_scope | {ctx.integration_scope} |",
        f"| security_in_scope | {ctx.security_in_scope} |",
        f"| migration_scope | {ctx.migration_scope} |",
        f"| dr_in_scope | {ctx.dr_in_scope} |",
        f"| integration_count | {ctx.integration_count} |",
        f"| oax_in_scope | {ctx.oax_in_scope} |",
        f"| analytics_requirements_in_tender | {ctx.analytics_requirements_in_tender} |",
        f"| personal_data_in_scope | {ctx.personal_data_in_scope} |",
        f"| help_desk_in_scope | {ctx.help_desk_in_scope} |",
        f"| feature_licensing_confirmed | {ctx.feature_licensing_confirmed} |",
        f"| delivery_model | {ctx.delivery_model or '—'} |",
        f"",
        f"---",
        f"",
        f"## Full Evaluation Trace",
        f"",
        f"| Risk ID | Status | excl_if result | mand_if result | opt_if result | Reason |",
        f"|---|---|---|---|---|---|",
    ]

    for r in sorted(results, key=lambda x: x.risk.risk_id):
        if r.status in (S_PATTERN_EXCLUDED, S_LIFECYCLE_EXCLUDED):
            lines.append(
                f"| {r.risk.risk_id} | {r.status} | — | — | — | "
                f"{r.selection_reason} |"
            )
        else:
            excl_s = fmt_eval(r.excluded_if_norm, r.excluded_if_result)
            mand_s = fmt_eval(r.mandatory_if_norm, r.mandatory_if_result)
            opt_s  = fmt_eval(r.optional_if_norm,  r.optional_if_result)
            lines.append(
                f"| {r.risk.risk_id} | **{r.status}** | "
                f"{excl_s} | {mand_s} | {opt_s} | "
                f"{r.selection_reason[:80]} |"
            )

    if violations:
        lines += [
            "",
            "---",
            "",
            "## Validation Violations",
            "",
        ]
        for v in violations:
            lines.append(f"- {v}")

    lines += [
        "",
        "---",
        "",
        "## AREL Normalization Applied",
        "",
        "The following normalizations were applied to ERR expressions before evaluation:",
        "",
        "| Transformation | Rule |",
        "|---|---|",
        "| `CONTAINS` → `contains` | Keyword case normalization |",
        "| `AND` → `and`, `OR` → `or`, `NOT` → `not` | Keyword case normalization |",
        "| Standalone `=` → `==` | Equality operator normalization (preserves `!=`, `>=`, `<=`) |",
        "| `\"OIC\"` → `\"Oracle Integration Cloud\"` | Platform alias normalization |",
        "| `country: \"RSA\"` → `\"ZA\"` | Country ISO 3166-1 alpha-2 normalization |",
        "| List `contains` → substring per element | RSE list-aware contains |",
        "",
        f"*Generated by RSE v{ENGINE_VERSION} — {now}*",
        "",
    ]
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────────────────
# SELF-TESTS
# ─────────────────────────────────────────────────────────────────────────────

def run_self_tests() -> None:
    print("RSE Self-Test Suite")
    print("=" * 60)

    @dataclass
    class _Ctx:
        platform: str = "Oracle HCM Cloud"
        engagement_type: str = "Implementation"
        modules: List[str] = field(default_factory=lambda: [
            "Oracle HCM Core", "Oracle Learning Cloud", "Oracle Recruiting Cloud"
        ])
        country: str = "ZA"
        payroll_integration: Optional[bool] = False
        oax_in_scope: Optional[bool] = None
        integration_count: Optional[int] = None

    ctx = _Ctx()
    ev = RSEARELEvaluator(ctx)

    tests = [
        # (description, expression, expected)
        ("platform contains 'Oracle HCM'",
         'platform contains "Oracle HCM"', True),
        ("modules list-aware contains 'Oracle Learning'",
         'modules contains "Oracle Learning"', True),  # Learning Cloud contains Learning
        ("modules list-aware contains 'Oracle WFM' → False",
         'modules contains "Oracle WFM"', False),
        ("engagement_type == 'Implementation'",
         'engagement_type == "Implementation"', True),
        ("payroll_integration == FALSE (bool-safe)",
         'payroll_integration == FALSE', True),
        ("payroll_integration == TRUE → False",
         'payroll_integration == TRUE', False),
        ("not payroll_integration == TRUE",
         'not payroll_integration == TRUE', True),
        ("NULL var → False",
         'oax_in_scope == TRUE', False),
        ("NULL var for int comparison → False",
         'integration_count > 2', False),
        ("compound: platform contains Oracle HCM AND engagement Implementation",
         'platform contains "Oracle HCM" and engagement_type == "Implementation"', True),
        ("country == ZA",
         'country == "ZA"', True),
        ("country != ZA → False",
         'country != "ZA"', False),
        ("OIC alias: platform contains Oracle Integration Cloud",
         'platform contains "Oracle Integration Cloud"', False),  # HCM platform
        ("TRUE literal",
         'TRUE', True),
        ("not (payroll_integration == TRUE) via parentheses",
         'not (payroll_integration == TRUE)', True),
        ("platform == Acumatica → False",
         'platform == "Acumatica"', False),
        ("platform excluded check",
         'platform == "Acumatica" or platform == "BeBanking"', False),
    ]

    passed = 0
    for desc, expr, expected in tests:
        result = ev.evaluate(normalize_arel(expr))
        ok = result == expected
        status = "PASS" if ok else "FAIL"
        if ok:
            passed += 1
        print(f"  [{status}] {desc}")
        if not ok:
            print(f"         expr={expr!r}")
            print(f"         expected={expected}, got={result}")

    print(f"\nResult: {passed}/{len(tests)} PASS")
    if passed == len(tests):
        print("SELF-TEST: ALL PASS")
    else:
        print("SELF-TEST: FAILURES DETECTED")
        sys.exit(1)


# ─────────────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description=f"Risk Selection Engine v{ENGINE_VERSION} — PF2-001",
    )
    parser.add_argument("context", nargs="?", help="Tender context YAML path")
    parser.add_argument("--extension", help="RSE extension YAML (optional)")
    parser.add_argument(
        "--register", default=RISK_REGISTER_DEFAULT,
        help="Path to ENTERPRISE_RISK_REGISTER_V1.md",
    )
    parser.add_argument("--outdir", default=OUTPUT_DIR_DEFAULT, help="Output directory")
    parser.add_argument("--dry-run", action="store_true", help="Print results without writing files")
    parser.add_argument("--run-tests", action="store_true", help="Run self-test suite")
    args = parser.parse_args()

    if args.run_tests:
        run_self_tests()
        return

    if not args.context:
        parser.print_help()
        sys.exit(1)

    # ── Load ────────────────────────────────────────────────────────────────
    ctx   = load_rse_context(args.context, args.extension)
    risks = parse_risk_register(args.register)

    print(f"\nRisk Selection Engine v{ENGINE_VERSION}")
    print(f"  Tender:   {ctx.tender_id}")
    print(f"  Pattern:  {ctx.pattern} ({PATTERN_NAMES.get(ctx.pattern, 'Unknown')})")
    print(f"  Platform: {ctx.platform}")
    print(f"  Risks loaded: {len(risks)}")
    print()

    # ── Select ──────────────────────────────────────────────────────────────
    results    = select_risks(risks, ctx)
    violations = validate_selections(results)

    mandatory    = [r for r in results if r.status == S_MANDATORY]
    optional_sel = [r for r in results if r.status == S_OPTIONAL_SELECTED]
    excluded     = [r for r in results if r.status == S_EXCLUDED]
    pat_excl     = [r for r in results if r.status == S_PATTERN_EXCLUDED]
    def_excl     = [r for r in results if r.status == S_DEFAULT_EXCLUDED]
    selected_all = mandatory + optional_sel

    print("Selection Results:")
    print(f"  MANDATORY:         {len(mandatory)}")
    print(f"  OPTIONAL_SELECTED: {len(optional_sel)}")
    print(f"  EXCLUDED:          {len(excluded)}")
    print(f"  PATTERN_EXCLUDED:  {len(pat_excl)}")
    print(f"  DEFAULT_EXCLUDED:  {len(def_excl)}")
    print(f"  ─────────────────────────")
    print(f"  TOTAL SELECTED:    {len(selected_all)}")
    print(f"  Violations:        {len(violations)}")
    print()

    if mandatory:
        print("  Mandatory risks:")
        for r in sorted(mandatory, key=_sort_key):
            print(f"    [{r.risk.rating:<8}] {r.risk.risk_id} — {r.risk.title}")
    if optional_sel:
        print("  Optional selected:")
        for r in sorted(optional_sel, key=_sort_key):
            print(f"    [{r.risk.rating:<8}] {r.risk.risk_id} — {r.risk.title}")
    if violations:
        print("\n  Violations:")
        for v in violations:
            print(f"    !! {v}")

    # ── Generate outputs ────────────────────────────────────────────────────
    reg_md   = generate_risk_register_md(results, ctx, violations)
    audit_md = generate_audit_md(results, ctx, violations)

    slug     = re.sub(r"[^A-Za-z0-9_-]", "_", ctx.tender_id)
    reg_fn   = f"SELECTED_RISK_REGISTER_{slug}.md"
    audit_fn = f"RISK_SELECTION_AUDIT_{slug}.md"

    if not args.dry_run:
        os.makedirs(args.outdir, exist_ok=True)
        with open(os.path.join(args.outdir, reg_fn),   "w", encoding="utf-8") as f:
            f.write(reg_md)
        with open(os.path.join(args.outdir, audit_fn), "w", encoding="utf-8") as f:
            f.write(audit_md)
        print(f"\nOutputs written to: {args.outdir}")
        print(f"  {reg_fn}")
        print(f"  {audit_fn}")
    else:
        print("\n[DRY-RUN] Files not written.")
        print("\n── SELECTED RISK REGISTER (preview) ──")
        print(reg_md[:2000])


if __name__ == "__main__":
    main()
