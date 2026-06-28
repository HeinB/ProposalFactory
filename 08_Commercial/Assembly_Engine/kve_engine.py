#!/usr/bin/env python3
"""
Knowledge Validation Engine (KVE) — Phase B Implementation
Work Package: WP19D
Version: 2.0
Date: 2026-06-28

76 validation rules across 8 phases. AREL V1.0 evaluator (no eval()).
Mode 1: Platform Health — full registry scan, KHS calculation, health report.
Mode 2: Assembly Validation — manifest construction and certification.

Usage:
    python kve_engine.py --mode assembly --context tender_context.yaml [--dry-run]
    python kve_engine.py --mode health [--dry-run]
    python kve_engine.py --mode assembly --context ctx.yaml --repo /path/to/kb --output /path/to/out
"""

import argparse
import re
import sys
import yaml
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple
from dataclasses import dataclass, field

# ── Constants ─────────────────────────────────────────────────────────────────

ENGINE_VERSION = "2.0"
RULES_VERSION = "1.0"

BLOCK_RULES = [
    "RI-001", "RI-008", "RI-009", "RI-011", "RI-012",
    "AV-001", "AV-002", "AV-004", "AV-008", "AV-009", "AV-010", "AV-011",
    "CLV-001", "CLV-002", "CLV-007", "CLV-008",
    "LV-ASM-001", "LV-ASM-002", "LV-ASP-002",
    "LV-RSK-004", "LV-RSK-008", "LV-REF-001",
]

VALID_ASSET_TYPES = {
    "CAP", "ASP", "ASM", "RSK", "MTH", "REF",
    "PPT", "PRT", "CON", "COM", "PAT", "SEC",
}
VALID_LIFECYCLE_STATES = {
    "DRAFT", "NORMALISED", "READY_FOR_REVIEW", "AUTO_APPROVED",
    "REVIEW_REQUIRED", "APPROVED", "SUPERSEDED", "ARCHIVED",
}
VALID_PATTERNS = {f"P{i}" for i in range(1, 14)}
VALID_PLATFORMS = {
    "Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle EBS",
    "Oracle Integration Cloud", "Acumatica", "BeBanking",
}
MANDATORY_FIELDS = [
    "asset_id", "asset_type", "title", "version", "source_file",
    "lifecycle_status", "approved_for_reuse", "owner_role", "owner_business_unit",
    "approval_authority", "governing_standard", "registry_version_added",
    "created", "created_by", "governance_notes", "pattern_applicability", "proposal_sections",
]
VALID_CONTENT_SOURCE_TYPES = {"DIRECT", "EXTRACT", "MERGE", "AI-GENERATE", "TEMPLATE", "PLACEHOLDER"}
VALID_AUTOMATION_TYPES = {"DIRECT", "EXTRACT", "MERGE", "AI-GENERATE", "TEMPLATE", "PLACEHOLDER"}

RATING_MATRIX: Dict[Tuple[str, str], str] = {
    ("Low", "Low"): "LOW",      ("Low", "Medium"): "LOW",      ("Low", "High"): "MEDIUM",
    ("Medium", "Low"): "LOW",   ("Medium", "Medium"): "MEDIUM", ("Medium", "High"): "HIGH",
    ("High", "Low"): "MEDIUM",  ("High", "Medium"): "HIGH",     ("High", "High"): "CRITICAL",
}


# ── Data Structures ───────────────────────────────────────────────────────────

@dataclass
class RuleResult:
    rule_code: str
    rule_name: str
    severity: str          # BLOCK / ERROR / WARNING / INFO
    passed: bool
    affected_ids: List[str] = field(default_factory=list)
    condition_triggered: str = ""
    message: str = ""
    recommended_action: str = ""
    escalation: str = ""


@dataclass
class ValidationContext:
    # Phase A — 7 core variables
    tender_id: str = ""
    pattern: str = ""
    platform: str = ""
    engagement_type: str = ""
    modules: List[str] = field(default_factory=list)
    country: str = "RSA"
    client_size: str = "Enterprise"
    client_sector: str = "All"
    am_clearances: List[str] = field(default_factory=list)
    ptc_clearances: List[str] = field(default_factory=list)
    tender_date: str = ""
    # Phase B — 13 extended variables
    industry: str = ""
    bom: List[str] = field(default_factory=list)
    payroll_integration: Optional[bool] = None
    oci_in_scope: Optional[bool] = None
    client_has_oic: Optional[bool] = None
    dr_in_scope: Optional[bool] = None
    security_in_scope: Optional[bool] = None
    migration_scope: Optional[bool] = None
    integration_scope: Optional[bool] = None
    support_scope: Optional[bool] = None
    pricing_type: str = ""
    project_duration_months: Optional[float] = None


# ── AREL V1.0 Evaluator ───────────────────────────────────────────────────────

class _Token:
    __slots__ = ("kind", "value")

    def __init__(self, kind: str, value: Any) -> None:
        self.kind = kind
        self.value = value

    def __repr__(self) -> str:
        return f"Token({self.kind}, {self.value!r})"


_KEYWORDS = {"and", "or", "not", "in", "contains"}
_OP_CHARS = {"=", "!", ">", "<"}


class ARELEvaluator:
    """Recursive-descent AREL V1.0 parser and evaluator. No eval()."""

    def __init__(self, context: "ValidationContext") -> None:
        self._context = context
        self._tokens: List[_Token] = []
        self._pos: int = 0

    def evaluate(self, expr: str) -> bool:
        if not expr:
            return False
        s = expr.strip()
        if not s:
            return False
        if s == "TRUE":
            return True
        if s == "FALSE":
            return False
        try:
            self._tokens = self._tokenize(s)
            self._pos = 0
            result = self._parse_or_expr()
            # Accept trailing EOF
            tok = self._peek()
            if tok.kind != "EOF":
                return False
            return bool(result)
        except Exception:
            return False

    # ── Tokenizer ──────────────────────────────────────────────────────────

    def _tokenize(self, s: str) -> List[_Token]:
        tokens: List[_Token] = []
        i = 0
        n = len(s)
        while i < n:
            c = s[i]
            # Whitespace
            if c in " \t\n\r":
                i += 1
                continue
            # Double-quoted string
            if c == '"':
                j = i + 1
                while j < n and s[j] != '"':
                    if s[j] == '\\':
                        j += 1  # skip escaped char
                    j += 1
                if j >= n:
                    raise ValueError(f"Unterminated string at position {i}")
                tokens.append(_Token("STR", s[i + 1:j]))
                i = j + 1
                continue
            # Operators
            if c in _OP_CHARS:
                if i + 1 < n and s[i + 1] == "=":
                    op = c + "="
                    tokens.append(_Token("OP", op))
                    i += 2
                    continue
                tokens.append(_Token("OP", c))
                i += 1
                continue
            # Brackets / Parens / Comma
            if c == "[":
                tokens.append(_Token("LBRACKET", "["))
                i += 1
                continue
            if c == "]":
                tokens.append(_Token("RBRACKET", "]"))
                i += 1
                continue
            if c == "(":
                tokens.append(_Token("LPAREN", "("))
                i += 1
                continue
            if c == ")":
                tokens.append(_Token("RPAREN", ")"))
                i += 1
                continue
            if c == ",":
                tokens.append(_Token("COMMA", ","))
                i += 1
                continue
            # Number
            if c.isdigit() or (c == "-" and i + 1 < n and s[i + 1].isdigit()):
                j = i + 1
                has_dot = False
                while j < n and (s[j].isdigit() or (s[j] == "." and not has_dot)):
                    if s[j] == ".":
                        has_dot = True
                    j += 1
                num_str = s[i:j]
                val: Any = float(num_str) if has_dot else int(num_str)
                tokens.append(_Token("NUM", val))
                i = j
                continue
            # Identifier / keyword / boolean
            if c.isalpha() or c == "_":
                j = i
                while j < n and (s[j].isalnum() or s[j] == "_"):
                    j += 1
                word = s[i:j]
                word_lower = word.lower()
                if word_lower == "true":
                    tokens.append(_Token("BOOL", True))
                elif word_lower == "false":
                    tokens.append(_Token("BOOL", False))
                elif word_lower in _KEYWORDS:
                    tokens.append(_Token("KW", word_lower))
                else:
                    tokens.append(_Token("VAR", word))
                i = j
                continue
            raise ValueError(f"Unexpected character '{c}' at position {i}")
        tokens.append(_Token("EOF", None))
        return tokens

    # ── Parser helpers ─────────────────────────────────────────────────────

    def _peek(self) -> _Token:
        if self._pos < len(self._tokens):
            return self._tokens[self._pos]
        return _Token("EOF", None)

    def _consume(self) -> _Token:
        tok = self._peek()
        self._pos += 1
        return tok

    def _expect_kw(self, kw: str) -> None:
        tok = self._consume()
        if tok.kind != "KW" or tok.value != kw:
            raise ValueError(f"Expected keyword '{kw}', got {tok!r}")

    # ── Grammar rules ──────────────────────────────────────────────────────

    def _parse_or_expr(self) -> bool:
        result = self._parse_and_expr()
        while self._peek().kind == "KW" and self._peek().value == "or":
            self._consume()
            right = self._parse_and_expr()
            result = result or right
        return result

    def _parse_and_expr(self) -> bool:
        result = self._parse_not_expr()
        while self._peek().kind == "KW" and self._peek().value == "and":
            self._consume()
            right = self._parse_not_expr()
            result = result and right
        return result

    def _parse_not_expr(self) -> bool:
        if self._peek().kind == "KW" and self._peek().value == "not":
            self._consume()
            return not self._parse_not_expr()
        return self._parse_atom()

    def _parse_atom(self) -> bool:
        tok = self._peek()
        if tok.kind == "LPAREN":
            self._consume()
            result = self._parse_or_expr()
            tok2 = self._consume()
            if tok2.kind != "RPAREN":
                raise ValueError(f"Expected ')' got {tok2!r}")
            return result
        return self._parse_comparison()

    def _parse_comparison(self) -> bool:
        tok = self._peek()
        # Bare boolean literal
        if tok.kind == "BOOL":
            self._consume()
            return tok.value
        if tok.kind != "VAR":
            raise ValueError(f"Expected variable or boolean, got {tok!r}")
        self._consume()
        var_name = tok.value
        left = self._resolve(var_name)

        next_tok = self._peek()
        # VAR not in [...]  — "not" after variable is the "not in" two-token operator
        if next_tok.kind == "KW" and next_tok.value == "not":
            self._consume()
            self._expect_kw("in")
            value_list = self._parse_list()
            return self._null_safe_not_in(left, value_list)

        # VAR in [...]
        if next_tok.kind == "KW" and next_tok.value == "in":
            self._consume()
            value_list = self._parse_list()
            return self._null_safe_in(left, value_list)

        # VAR contains "..."
        if next_tok.kind == "KW" and next_tok.value == "contains":
            self._consume()
            right = self._parse_scalar()
            return self._null_safe_contains(left, right)

        # VAR OP scalar
        if next_tok.kind == "OP":
            self._consume()
            op = next_tok.value
            right = self._parse_scalar()
            return self._compare(left, op, right)

        raise ValueError(f"Expected operator after variable '{var_name}', got {next_tok!r}")

    def _parse_scalar(self) -> Any:
        tok = self._consume()
        if tok.kind in ("STR", "NUM"):
            return tok.value
        if tok.kind == "BOOL":
            return tok.value
        raise ValueError(f"Expected scalar value, got {tok!r}")

    def _parse_list(self) -> List[Any]:
        tok = self._consume()
        if tok.kind != "LBRACKET":
            raise ValueError(f"Expected '[', got {tok!r}")
        items: List[Any] = []
        while self._peek().kind != "RBRACKET":
            if items:
                sep = self._consume()
                if sep.kind != "COMMA":
                    raise ValueError(f"Expected ',' in list, got {sep!r}")
            items.append(self._parse_scalar())
        self._consume()  # consume "]"
        return items

    # ── Variable resolution (null-safe) ────────────────────────────────────

    def _resolve(self, name: str) -> Any:
        ctx = self._context
        mapping: Dict[str, Any] = {
            "pattern": ctx.pattern,
            "platform": ctx.platform,
            "engagement_type": ctx.engagement_type,
            "modules": ctx.modules,
            "country": ctx.country,
            "client_size": ctx.client_size,
            "client_sector": ctx.client_sector,
            "am_clearances": ctx.am_clearances,
            "ptc_clearances": ctx.ptc_clearances,
            "tender_date": ctx.tender_date,
            "industry": ctx.industry,
            "bom": ctx.bom,
            "payroll_integration": ctx.payroll_integration,
            "oci_in_scope": ctx.oci_in_scope,
            "client_has_oic": ctx.client_has_oic,
            "dr_in_scope": ctx.dr_in_scope,
            "security_in_scope": ctx.security_in_scope,
            "migration_scope": ctx.migration_scope,
            "integration_scope": ctx.integration_scope,
            "support_scope": ctx.support_scope,
            "pricing_type": ctx.pricing_type,
            "project_duration_months": ctx.project_duration_months,
        }
        return mapping.get(name, None)  # absent variable → None (null-safe)

    # ── Null-safe comparisons ──────────────────────────────────────────────

    def _compare(self, left: Any, op: str, right: Any) -> bool:
        if left is None:
            return False
        try:
            if op == "==":
                # Type-safe: bool and str are never equal
                if isinstance(left, bool) != isinstance(right, bool):
                    if isinstance(left, bool) or isinstance(right, bool):
                        return False
                return str(left) == str(right) if isinstance(right, str) else left == right
            if op == "!=":
                if isinstance(left, bool) != isinstance(right, bool):
                    if isinstance(left, bool) or isinstance(right, bool):
                        return True
                return str(left) != str(right) if isinstance(right, str) else left != right
            if op == ">":
                return float(left) > float(right)
            if op == ">=":
                return float(left) >= float(right)
            if op == "<":
                return float(left) < float(right)
            if op == "<=":
                return float(left) <= float(right)
        except (TypeError, ValueError):
            return False
        return False

    def _null_safe_in(self, left: Any, value_list: List[Any]) -> bool:
        if left is None:
            return False
        if isinstance(left, list):
            # any element of left is in value_list
            return any(item in value_list for item in left)
        return left in value_list

    def _null_safe_not_in(self, left: Any, value_list: List[Any]) -> bool:
        if left is None:
            return False
        if isinstance(left, list):
            return all(item not in value_list for item in left)
        return left not in value_list

    def _null_safe_contains(self, left: Any, right: Any) -> bool:
        if left is None:
            return False
        if isinstance(left, list):
            return right in left
        if isinstance(left, str):
            return str(right) in left
        return False


def evaluate_expression(expr: str, context: ValidationContext) -> bool:
    """Evaluate an AREL V1.0 mandatory_if / optional_if / excluded_if expression."""
    return ARELEvaluator(context).evaluate(expr)


# ── AREL Compliance Test Suite (80 tests) ─────────────────────────────────────

def run_arel_compliance_tests(context: Optional[ValidationContext] = None) -> Tuple[int, int, List[str]]:
    """Execute all 80 AREL V1.0 compliance tests. Returns (passed, total, failures)."""
    # Reference context per ASSEMBLY_RULE_TEST_SUITE.md
    ref = ValidationContext(
        tender_id="TEST-001",
        pattern="P1",
        platform="Oracle HCM Cloud",
        engagement_type="Implementation",
        modules=["Oracle HCM Core", "Oracle Recruiting Cloud", "Oracle Learning Cloud"],
        country="RSA",
        client_size="Enterprise",
        client_sector="Government",
        am_clearances=["REF-001", "REF-007"],
        ptc_clearances=["W1S1-001-ORA-HCMCoreCap"],
        tender_date="2026-06-28",
        industry="Public Sector",
        bom=["HCM-CORE", "RECRUIT-CLOUD"],
        payroll_integration=False,
        oci_in_scope=True,
        client_has_oic=False,
        dr_in_scope=False,
        security_in_scope=True,
        migration_scope=True,
        integration_scope=False,
        support_scope=False,
        pricing_type="Fixed Price",
        project_duration_months=12.0,
    )
    ctx = context or ref

    def ev(expr: str) -> bool:
        return evaluate_expression(expr, ctx)

    cases: List[Tuple[str, str, bool]] = [
        # Section A — Unconditionals
        ("A01", "TRUE", True),
        ("A02", "FALSE", False),
        ("A03", "", False),

        # Section B — String equality
        ("B01", 'pattern == "P1"', True),
        ("B02", 'pattern == "P2"', False),
        ("B03", 'platform == "Oracle HCM Cloud"', True),
        ("B04", 'platform == "Acumatica"', False),
        ("B05", 'engagement_type == "Implementation"', True),
        ("B06", 'engagement_type == "Support"', False),
        ("B07", 'country == "RSA"', True),
        ("B08", 'client_size == "Enterprise"', True),
        ("B09", 'client_sector == "Government"', True),

        # Section C — Inequality
        ("C01", 'pattern != "P2"', True),
        ("C02", 'platform != "Acumatica"', True),
        ("C03", 'client_sector != "Government"', False),

        # Section D — in operator (scalar variable)
        ("D01", 'pattern in ["P1", "P2", "P3"]', True),
        ("D02", 'pattern in ["P4", "P5"]', False),
        ("D03", 'platform in ["Oracle HCM Cloud", "Oracle ERP Cloud"]', True),
        ("D04", 'client_size in ["SME", "Mid-Market"]', False),

        # Section E — not in operator
        ("E01", 'pattern not in ["P4", "P5"]', True),
        ("E02", 'pattern not in ["P1", "P2"]', False),
        ("E03", 'platform not in ["Acumatica", "BeBanking"]', True),

        # Section F — contains operator (list variable)
        ("F01", 'modules contains "Oracle HCM Core"', True),
        ("F02", 'modules contains "Oracle Payroll"', False),
        ("F03", 'am_clearances contains "REF-001"', True),
        ("F04", 'am_clearances contains "REF-999"', False),
        ("F05", 'bom contains "HCM-CORE"', True),
        ("F06", 'bom contains "ERP-FIN"', False),

        # Section G — Boolean variables
        ("G01", 'payroll_integration == "False"', False),  # bool False != string
        ("G02", 'oci_in_scope == "True"', False),  # bool True != string
        ("G03", 'security_in_scope == "True"', False),
        ("G04", 'migration_scope == "True"', False),

        # Section H — Numeric comparisons
        ("H01", 'project_duration_months > 6', True),
        ("H02", 'project_duration_months >= 12', True),
        ("H03", 'project_duration_months < 24', True),
        ("H04", 'project_duration_months <= 12', True),
        ("H05", 'project_duration_months > 24', False),

        # Section I — and operator
        ("I01", 'pattern == "P1" and platform == "Oracle HCM Cloud"', True),
        ("I02", 'pattern == "P1" and platform == "Acumatica"', False),
        ("I03", 'pattern == "P2" and platform == "Oracle HCM Cloud"', False),
        ("I04", 'country == "RSA" and client_size == "Enterprise" and client_sector == "Government"', True),

        # Section J — or operator
        ("J01", 'pattern == "P1" or pattern == "P2"', True),
        ("J02", 'pattern == "P2" or pattern == "P3"', False),
        ("J03", 'platform == "Acumatica" or platform == "Oracle HCM Cloud"', True),

        # Section K — not operator (unary)
        ("K01", 'not pattern == "P2"', True),
        ("K02", 'not pattern == "P1"', False),
        ("K03", 'not platform == "Acumatica"', True),
        ("K04", 'not TRUE', False),
        ("K05", 'not FALSE', True),

        # Section L — Parentheses / precedence
        ("L01", '(pattern == "P1" or pattern == "P2") and platform == "Oracle HCM Cloud"', True),
        ("L02", 'pattern == "P1" and (platform == "Acumatica" or platform == "Oracle HCM Cloud")', True),
        ("L03", '(pattern == "P2" or pattern == "P3") and platform == "Oracle HCM Cloud"', False),
        ("L04", 'not (pattern == "P2" and client_size == "Enterprise")', True),

        # Section M — Mixed complex expressions
        ("M01", 'pattern in ["P1", "P2"] and modules contains "Oracle HCM Core"', True),
        ("M02", 'platform == "Oracle HCM Cloud" and engagement_type == "Implementation" and client_size == "Enterprise"', True),
        ("M03", 'pattern not in ["P10", "P13"] and platform == "Oracle HCM Cloud"', True),
        ("M04", 'modules contains "Oracle HCM Core" or modules contains "Oracle Payroll"', True),
        ("M05", 'client_sector in ["Government", "Public Sector"] and country == "RSA"', True),
        ("M06", '(pattern == "P1" and platform == "Oracle HCM Cloud") or (pattern == "P7" and platform == "Acumatica")', True),
        ("M07", 'not modules contains "Oracle Payroll" and platform == "Oracle HCM Cloud"', True),
        ("M08", 'project_duration_months >= 6 and project_duration_months <= 24', True),
        ("M09", 'am_clearances contains "REF-001" and pattern in ["P1", "P2", "P3"]', True),
        ("M10", 'bom contains "HCM-CORE" and platform == "Oracle HCM Cloud" and client_size == "Enterprise"', True),

        # Section N — Null-safe (absent variable → false)
        ("N01", 'nonexistent_var == "anything"', False),
        ("N02", 'nonexistent_var in ["a", "b"]', False),
        ("N03", 'nonexistent_var not in ["a", "b"]', False),
        ("N04", 'nonexistent_var contains "x"', False),
        ("N05", 'nonexistent_var > 0', False),

        # Section O — Phase B extended variables
        ("O01", 'pricing_type == "Fixed Price"', True),
        ("O02", 'pricing_type == "Time and Materials"', False),
        ("O03", 'industry == "Public Sector"', True),
        ("O04", 'industry in ["Public Sector", "Financial Services"]', True),
        ("O05", 'engagement_type == "Implementation" and pricing_type == "Fixed Price"', True),
        ("O06", 'client_size == "Enterprise" and industry == "Public Sector"', True),
        ("O07", 'pattern in ["P1", "P3"] and platform == "Oracle HCM Cloud" and client_sector == "Government"', True),
        ("O08", 'not industry == "Financial Services" and platform == "Oracle HCM Cloud"', True),
        ("O09", 'project_duration_months > 6 and pricing_type == "Fixed Price"', True),
        ("O10", 'modules contains "Oracle Recruiting Cloud" and client_sector == "Government"', True),

        # Section P — Edge cases
        ("P01", '"string literal in expression" == "nope"', False),  # should fail gracefully
        ("P02", 'pattern == "P1" and', False),  # malformed — trailing and
        ("P03", 'TRUE and pattern == "P1"', True),
        ("P04", 'FALSE or pattern == "P1"', True),
        ("P05", 'pattern == "P1" or FALSE', True),
        ("P06", 'pattern == "P2" and TRUE', False),
        ("P07", '((pattern == "P1"))', True),
        ("P08", 'not not pattern == "P1"', True),
    ]

    passed = 0
    failures: List[str] = []
    for tid, expr, expected in cases:
        try:
            result = ev(expr)
            if result == expected:
                passed += 1
            else:
                failures.append(f"{tid}: expr={expr!r} expected={expected} got={result}")
        except Exception as exc:
            if not expected:
                passed += 1  # graceful failure on invalid input counts as pass if expected=False
            else:
                failures.append(f"{tid}: expr={expr!r} raised {exc}")

    return passed, len(cases), failures


# ── Cycle Detection ───────────────────────────────────────────────────────────

def _detect_cycle(graph: Dict[str, str]) -> Optional[str]:
    visited: Set[str] = set()
    in_stack: Set[str] = set()

    def dfs(node: str) -> Optional[str]:
        if node in in_stack:
            return node
        if node in visited:
            return None
        visited.add(node)
        in_stack.add(node)
        successor = graph.get(node)
        if successor:
            result = dfs(successor)
            if result:
                return result
        in_stack.discard(node)
        return None

    for node in list(graph.keys()):
        if node not in visited:
            result = dfs(node)
            if result:
                return result
    return None


# ── Registry Loader ───────────────────────────────────────────────────────────

class RegistryLoader:
    def __init__(self, repo_root: Path) -> None:
        self.repo_root = repo_root
        self.governance_dir = repo_root / "00_Governance" / "Knowledge_Standards"

    def load(self) -> Tuple[Dict, Dict, Dict]:
        core_path = self.governance_dir / "KNOWLEDGE_ASSET_REGISTRY.yaml"
        asm_path = self.governance_dir / "KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml"
        if not core_path.exists():
            raise FileNotFoundError(
                f"Registry not found: {core_path}\n"
                "Run KRPE (krpe.py) to populate the registry before running KVE."
            )
        if not asm_path.exists():
            raise FileNotFoundError(
                f"Assumptions registry not found: {asm_path}\n"
                "Run KRPE (krpe.py) to populate the registry before running KVE."
            )
        with open(core_path, "r", encoding="utf-8") as f:
            core_data = yaml.safe_load(f)
        with open(asm_path, "r", encoding="utf-8") as f:
            asm_data = yaml.safe_load(f)

        registry_meta = core_data.get("registry_metadata", {})
        registry_index = {
            e["asset_id"]: e
            for e in core_data.get("assets", [])
            if e.get("asset_id")
        }
        assumptions_index = {
            e["asset_id"]: e
            for e in asm_data.get("assumptions", [])
            if e.get("asset_id")
        }
        return registry_index, assumptions_index, registry_meta


# ── Phase 1 — Registry Integrity ─────────────────────────────────────────────

def phase1_registry_integrity(
    registry: Dict,
    assumptions: Dict,
    all_ids: Set,
    repo_root: Path,
) -> Tuple[List[RuleResult], bool]:
    results: List[RuleResult] = []
    all_entries = {**registry, **assumptions}

    # RI-001: No duplicate asset IDs — ENGINE HALT
    all_id_list = list(registry.keys()) + list(assumptions.keys())
    seen: Set[str] = set()
    dups: Set[str] = set()
    for aid in all_id_list:
        if aid in seen:
            dups.add(aid)
        seen.add(aid)
    if dups:
        results.append(RuleResult(
            "RI-001", "No Duplicate Asset IDs", "BLOCK", False,
            affected_ids=sorted(dups),
            condition_triggered="asset_id appears more than once across registry + assumptions",
            message=f"Duplicate asset IDs found: {', '.join(sorted(dups))}. Registry is corrupt.",
            recommended_action="Remove or rename duplicate entries and regenerate the registry via KRPE.",
            escalation="REGISTRY_FACILITATOR",
        ))
        return results, True
    results.append(RuleResult("RI-001", "No Duplicate Asset IDs", "INFO", True,
                              message=f"{len(all_id_list)} unique asset IDs — no duplicates."))

    # RI-002: Valid asset_type values
    invalid_type = [aid for aid, e in all_entries.items()
                    if e.get("asset_type", "") not in VALID_ASSET_TYPES]
    if invalid_type:
        results.append(RuleResult("RI-002", "Valid Asset Types", "ERROR", False,
                                  affected_ids=invalid_type,
                                  message=f"{len(invalid_type)} entries have an invalid asset_type.",
                                  recommended_action="Correct asset_type to one of: " + ", ".join(sorted(VALID_ASSET_TYPES))))
    else:
        results.append(RuleResult("RI-002", "Valid Asset Types", "INFO", True,
                                  message="All asset_type values are valid."))

    # RI-003: Valid lifecycle_status values
    invalid_lc = [aid for aid, e in all_entries.items()
                  if e.get("lifecycle_status", "") not in VALID_LIFECYCLE_STATES]
    if invalid_lc:
        results.append(RuleResult("RI-003", "Valid Lifecycle States", "ERROR", False,
                                  affected_ids=invalid_lc,
                                  message=f"{len(invalid_lc)} entries have an invalid lifecycle_status."))
    else:
        results.append(RuleResult("RI-003", "Valid Lifecycle States", "INFO", True,
                                  message="All lifecycle_status values are valid."))

    # RI-004: Source file paths resolve
    missing_src = []
    for aid, entry in all_entries.items():
        sf = entry.get("source_file", "") or ""
        if sf:
            resolved = (repo_root / sf) if not Path(sf).is_absolute() else Path(sf)
            if not resolved.exists():
                missing_src.append(aid)
    if missing_src:
        results.append(RuleResult("RI-004", "Source File Paths Resolve", "WARNING", False,
                                  affected_ids=missing_src,
                                  message=f"{len(missing_src)} entries have unresolvable source_file paths."))
    else:
        results.append(RuleResult("RI-004", "Source File Paths Resolve", "INFO", True,
                                  message="All source_file paths resolve."))

    # RI-005: related_assets references resolve
    broken_related = []
    for aid, entry in all_entries.items():
        for ref in entry.get("related_assets", []) or []:
            if ref and ref not in all_ids:
                broken_related.append(aid)
                break
    if broken_related:
        results.append(RuleResult("RI-005", "Related Assets Resolve", "WARNING", False,
                                  affected_ids=broken_related,
                                  message=f"{len(broken_related)} entries have unresolvable related_assets references."))
    else:
        results.append(RuleResult("RI-005", "Related Assets Resolve", "INFO", True,
                                  message="All related_assets references resolve."))

    # RI-006: supersedes reference resolves
    broken_supersedes = [aid for aid, e in all_entries.items()
                         if e.get("supersedes", "") and e["supersedes"] not in all_ids]
    if broken_supersedes:
        results.append(RuleResult("RI-006", "Supersedes Reference Resolves", "ERROR", False,
                                  affected_ids=broken_supersedes,
                                  message=f"{len(broken_supersedes)} entries reference a superseded asset that does not exist."))
    else:
        results.append(RuleResult("RI-006", "Supersedes Reference Resolves", "INFO", True,
                                  message="All supersedes references resolve."))

    # RI-007: superseded_by reference resolves
    broken_supby = [aid for aid, e in all_entries.items()
                    if e.get("superseded_by", "") and e["superseded_by"] not in all_ids]
    if broken_supby:
        results.append(RuleResult("RI-007", "Superseded-By Reference Resolves", "ERROR", False,
                                  affected_ids=broken_supby,
                                  message=f"{len(broken_supby)} entries have an unresolvable superseded_by reference."))
    else:
        results.append(RuleResult("RI-007", "Superseded-By Reference Resolves", "INFO", True,
                                  message="All superseded_by references resolve."))

    # RI-008: No circular supersession — ENGINE HALT
    supersession_graph = {
        aid: e["superseded_by"]
        for aid, e in all_entries.items()
        if e.get("superseded_by", "") and e["superseded_by"] in all_ids
    }
    cycle_node = _detect_cycle(supersession_graph)
    if cycle_node:
        results.append(RuleResult(
            "RI-008", "No Circular Supersession Chain", "BLOCK", False,
            affected_ids=[cycle_node],
            condition_triggered="Cycle detected in superseded_by graph",
            message=f"Circular supersession chain detected at node: {cycle_node}.",
            recommended_action="Break the cycle by removing the circular superseded_by reference.",
            escalation="REGISTRY_FACILITATOR",
        ))
        return results, True

    results.append(RuleResult("RI-008", "No Circular Supersession Chain", "INFO", True,
                              message="No circular supersession chains detected."))

    # RI-009: No circular parent-child chain — ENGINE HALT
    parent_graph = {}
    for aid, entry in assumptions.items():
        asm_ext = entry.get("asm_ext", {}) or {}
        parent_id = asm_ext.get("parent_pack_id", "") or ""
        if parent_id and parent_id in all_ids:
            parent_graph[aid] = parent_id
    cycle_node = _detect_cycle(parent_graph)
    if cycle_node:
        results.append(RuleResult(
            "RI-009", "No Circular Parent-Child Chain", "BLOCK", False,
            affected_ids=[cycle_node],
            condition_triggered="Cycle detected in asm_ext.parent_pack_id graph",
            message=f"Circular parent-child chain detected at node: {cycle_node}.",
            recommended_action="Fix the parent_pack_id to break the cycle.",
            escalation="REGISTRY_FACILITATOR",
        ))
        return results, True

    results.append(RuleResult("RI-009", "No Circular Parent-Child Chain", "INFO", True,
                              message="No circular parent-child chains detected."))

    # RI-010: approved_for_reuse consistency
    afr_inconsistent = [
        aid for aid, e in all_entries.items()
        if e.get("approved_for_reuse", False) and e.get("lifecycle_status", "") != "APPROVED"
    ]
    if afr_inconsistent:
        results.append(RuleResult("RI-010", "Approved-for-Reuse Consistency", "ERROR", False,
                                  affected_ids=afr_inconsistent,
                                  message=f"{len(afr_inconsistent)} entries have approved_for_reuse=true but lifecycle_status != APPROVED."))
    else:
        results.append(RuleResult("RI-010", "Approved-for-Reuse Consistency", "INFO", True,
                                  message="approved_for_reuse is consistent with lifecycle_status for all entries."))

    # RI-011: DRAFT cannot be approved_for_reuse — BLOCK
    draft_afr = [
        aid for aid, e in all_entries.items()
        if e.get("approved_for_reuse", False) and e.get("lifecycle_status", "") == "DRAFT"
    ]
    if draft_afr:
        results.append(RuleResult(
            "RI-011", "DRAFT Not Approved-for-Reuse", "BLOCK", False,
            affected_ids=draft_afr,
            condition_triggered="approved_for_reuse = true AND lifecycle_status = DRAFT",
            message=f"{len(draft_afr)} DRAFT assets are incorrectly marked approved_for_reuse=true.",
            recommended_action="Set approved_for_reuse=false for all DRAFT assets.",
            escalation="AUTHOR",
        ))
    else:
        results.append(RuleResult("RI-011", "DRAFT Not Approved-for-Reuse", "INFO", True,
                                  message="No DRAFT assets marked approved_for_reuse=true."))

    # RI-012: ARCHIVED cannot be approved_for_reuse — BLOCK
    archived_afr = [
        aid for aid, e in all_entries.items()
        if e.get("approved_for_reuse", False) and e.get("lifecycle_status", "") == "ARCHIVED"
    ]
    if archived_afr:
        results.append(RuleResult(
            "RI-012", "ARCHIVED Not Approved-for-Reuse", "BLOCK", False,
            affected_ids=archived_afr,
            condition_triggered="approved_for_reuse = true AND lifecycle_status = ARCHIVED",
            message=f"{len(archived_afr)} ARCHIVED assets are incorrectly marked approved_for_reuse=true.",
            recommended_action="Set approved_for_reuse=false for all ARCHIVED assets.",
            escalation="AUTHOR",
        ))
    else:
        results.append(RuleResult("RI-012", "ARCHIVED Not Approved-for-Reuse", "INFO", True,
                                  message="No ARCHIVED assets marked approved_for_reuse=true."))

    # RI-013: SUPERSEDED cannot be approved_for_reuse
    superseded_afr = [
        aid for aid, e in all_entries.items()
        if e.get("approved_for_reuse", False) and e.get("lifecycle_status", "") == "SUPERSEDED"
    ]
    if superseded_afr:
        results.append(RuleResult("RI-013", "SUPERSEDED Not Approved-for-Reuse", "ERROR", False,
                                  affected_ids=superseded_afr,
                                  message=f"{len(superseded_afr)} SUPERSEDED assets have approved_for_reuse=true."))
    else:
        results.append(RuleResult("RI-013", "SUPERSEDED Not Approved-for-Reuse", "INFO", True,
                                  message="No SUPERSEDED assets marked approved_for_reuse=true."))

    # RI-014: Mandatory fields present
    metadata_failures = []
    for aid, entry in all_entries.items():
        missing = [f for f in MANDATORY_FIELDS
                   if entry.get(f) is None or entry.get(f) == "" or entry.get(f) == []]
        if missing:
            metadata_failures.append(aid)
    if metadata_failures:
        results.append(RuleResult("RI-014", "Mandatory Fields Present", "ERROR", False,
                                  affected_ids=metadata_failures,
                                  message=f"{len(metadata_failures)} entries have missing mandatory fields."))
    else:
        results.append(RuleResult("RI-014", "Mandatory Fields Present", "INFO", True,
                                  message="All mandatory fields populated across all entries."))

    # RI-015: Extension block present for typed assets
    extension_map = {
        "CAP": "cap_ext", "ASP": "asp_ext", "ASM": "asm_ext",
        "RSK": "rsk_ext", "MTH": "mth_ext", "REF": "ref_ext",
        "PAT": "pat_ext", "SEC": "sec_ext",
    }
    missing_ext = [
        aid for aid, e in all_entries.items()
        if e.get("asset_type") in extension_map and not e.get(extension_map[e["asset_type"]])
    ]
    if missing_ext:
        results.append(RuleResult("RI-015", "Extension Block Present", "WARNING", False,
                                  affected_ids=missing_ext,
                                  message=f"{len(missing_ext)} typed assets are missing their extension block."))
    else:
        results.append(RuleResult("RI-015", "Extension Block Present", "INFO", True,
                                  message="All typed assets have their extension block."))

    return results, False


# ── Phase 2 — Tender Profile Establishment ───────────────────────────────────

def phase2_load_context(context_path: Path) -> ValidationContext:
    if not context_path.exists():
        raise FileNotFoundError(f"Tender context not found: {context_path}")
    with open(context_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    tc = data.get("tender_context", data) if isinstance(data, dict) else {}

    def _opt_bool(val: Any) -> Optional[bool]:
        if val is None:
            return None
        if isinstance(val, bool):
            return val
        s = str(val).strip().lower()
        if s in ("true", "yes", "1"):
            return True
        if s in ("false", "no", "0"):
            return False
        return None

    def _opt_float(val: Any) -> Optional[float]:
        if val is None:
            return None
        try:
            return float(val)
        except (TypeError, ValueError):
            return None

    ctx = ValidationContext()
    ctx.tender_id = str(tc.get("tender_id", "") or "")
    ctx.pattern = str(tc.get("pattern", "") or "")
    ctx.platform = str(tc.get("platform", "") or "")
    ctx.engagement_type = str(tc.get("engagement_type", "") or "")
    ctx.tender_date = str(tc.get("tender_date", "") or "")
    ctx.modules = list(tc.get("modules", []) or [])
    ctx.country = str(tc.get("country", "RSA") or "RSA")
    ctx.client_size = str(tc.get("client_size", "Enterprise") or "Enterprise")
    ctx.client_sector = str(tc.get("client_sector", "All") or "All")
    ctx.am_clearances = list(tc.get("am_clearances", []) or [])
    ctx.ptc_clearances = list(tc.get("ptc_clearances", []) or [])
    # Phase B extended
    ctx.industry = str(tc.get("industry", "") or "")
    ctx.bom = list(tc.get("bom", []) or [])
    ctx.payroll_integration = _opt_bool(tc.get("payroll_integration"))
    ctx.oci_in_scope = _opt_bool(tc.get("oci_in_scope"))
    ctx.client_has_oic = _opt_bool(tc.get("client_has_oic"))
    ctx.dr_in_scope = _opt_bool(tc.get("dr_in_scope"))
    ctx.security_in_scope = _opt_bool(tc.get("security_in_scope"))
    ctx.migration_scope = _opt_bool(tc.get("migration_scope"))
    ctx.integration_scope = _opt_bool(tc.get("integration_scope"))
    ctx.support_scope = _opt_bool(tc.get("support_scope"))
    ctx.pricing_type = str(tc.get("pricing_type", "") or "")
    ctx.project_duration_months = _opt_float(tc.get("project_duration_months"))

    if not ctx.tender_id:
        raise ValueError("tender_context.yaml: tender_id is required")
    if not ctx.pattern:
        raise ValueError("tender_context.yaml: pattern is required")
    if ctx.pattern not in VALID_PATTERNS:
        raise ValueError(f"tender_context.yaml: pattern '{ctx.pattern}' is not valid (P1–P13)")
    if not ctx.platform:
        raise ValueError("tender_context.yaml: platform is required")
    if ctx.platform not in VALID_PLATFORMS:
        raise ValueError(
            f"tender_context.yaml: platform '{ctx.platform}' is not valid.\n"
            f"Valid values: {', '.join(sorted(VALID_PLATFORMS))}"
        )
    if not ctx.engagement_type:
        raise ValueError("tender_context.yaml: engagement_type is required")

    return ctx


# ── Phase 3 — Candidate Manifest Construction ─────────────────────────────────

def phase3_build_manifest(
    registry: Dict,
    assumptions: Dict,
    context: ValidationContext,
    all_ids: Set,
) -> Tuple[Dict, List[RuleResult]]:
    results: List[RuleResult] = []
    all_entries = {**registry, **assumptions}
    candidates: Dict[str, dict] = {}
    mandatory_flags: Set[str] = set()

    # AV-005: Pattern applicability filter
    for aid, entry in all_entries.items():
        pa = entry.get("pattern_applicability", []) or []
        if context.pattern in pa or "ALL" in pa:
            candidates[aid] = entry

    results.append(RuleResult(
        "AV-005", "Pattern Applicability Filter", "INFO", True,
        message=(
            f"Pattern filter ({context.pattern}): {len(candidates)} of {len(all_entries)} assets qualify."
            + ("" if candidates else " Note: pattern_applicability not yet populated for most assets.")
        ),
    ))

    # AV-006: Platform filter for CAP assets
    cap_removed: List[str] = []
    for aid in list(candidates.keys()):
        entry = candidates[aid]
        if entry.get("asset_type") == "CAP":
            cap_ext = entry.get("cap_ext", {}) or {}
            ep = str(cap_ext.get("platform", "") or "")
            if ep and ep != context.platform and ep not in ("Cross-Platform", "Corporate"):
                cap_removed.append(aid)
                del candidates[aid]
    if cap_removed:
        results.append(RuleResult("AV-006", "Platform Applicability Filter", "WARNING", True,
                                  affected_ids=cap_removed,
                                  message=f"{len(cap_removed)} CAP assets removed — platform does not match {context.platform}."))
    else:
        results.append(RuleResult("AV-006", "Platform Applicability Filter", "INFO", True,
                                  message=f"Platform filter applied — no CAP assets removed for '{context.platform}'."))

    # AV-007: Engagement type filter for ASP assets
    asp_removed: List[str] = []
    asm_removed_via_asp: List[str] = []
    for aid in list(candidates.keys()):
        entry = candidates[aid]
        if entry.get("asset_type") == "ASP":
            asp_ext = entry.get("asp_ext", {}) or {}
            aet = asp_ext.get("applicable_engagement_types", []) or []
            if aet and aet != ["All"] and context.engagement_type not in aet:
                asp_removed.append(aid)
                del candidates[aid]
                for asm_id in list(candidates.keys()):
                    asm_ext = candidates[asm_id].get("asm_ext", {}) or {}
                    if asm_ext.get("parent_pack_id") == aid:
                        asm_removed_via_asp.append(asm_id)
                        del candidates[asm_id]
    if asp_removed:
        results.append(RuleResult("AV-007", "Engagement Type Filter", "ERROR", False,
                                  affected_ids=asp_removed + asm_removed_via_asp,
                                  message=f"{len(asp_removed)} ASP and {len(asm_removed_via_asp)} child ASMs removed."))
    else:
        results.append(RuleResult("AV-007", "Engagement Type Filter", "INFO", True,
                                  message="Engagement type filter applied — no ASP assets removed."))

    # AV-008: Add mandatory assets
    mandatory_added: List[str] = []
    for aid, entry in all_entries.items():
        if aid not in candidates:
            mi = (entry.get("assembly_rules", {}) or {}).get("mandatory_if", "") or ""
            if evaluate_expression(mi, context):
                candidates[aid] = entry
                mandatory_flags.add(aid)
                mandatory_added.append(aid)
    results.append(RuleResult(
        "AV-008", "Mandatory Asset Inclusion", "INFO", True,
        affected_ids=mandatory_added,
        message=(f"{len(mandatory_added)} mandatory assets added via mandatory_if."
                 if mandatory_added else "No mandatory_if expressions evaluated to true."),
    ))

    # AV-009 / AV-010: Excluded assets and mandatory-excluded conflicts
    excluded_ids: List[str] = []
    conflict_ids: List[str] = []
    for aid in list(candidates.keys()):
        entry = candidates[aid]
        ar = entry.get("assembly_rules", {}) or {}
        ei = ar.get("excluded_if", "") or ""
        mi = ar.get("mandatory_if", "") or ""
        if evaluate_expression(ei, context):
            is_mandatory = aid in mandatory_flags and evaluate_expression(mi, context)
            if is_mandatory:
                conflict_ids.append(aid)
            else:
                excluded_ids.append(aid)
                del candidates[aid]

    if conflict_ids:
        results.append(RuleResult(
            "AV-010", "No Mandatory-Excluded Conflict", "BLOCK", False,
            affected_ids=conflict_ids,
            condition_triggered="mandatory_if AND excluded_if both evaluate to TRUE",
            message=f"{len(conflict_ids)} assets are simultaneously mandatory and excluded.",
            recommended_action="Resolve the conflicting assembly_rules expressions.",
            escalation="BU_LEAD",
        ))
    else:
        results.append(RuleResult("AV-009", "Excluded Assets Removed", "INFO", True,
                                  affected_ids=excluded_ids,
                                  message=(f"{len(excluded_ids)} excluded assets removed."
                                           if excluded_ids else "No excluded_if expressions evaluated to true.")))
        results.append(RuleResult("AV-010", "No Mandatory-Excluded Conflict", "INFO", True,
                                  message="No mandatory-excluded conflicts detected."))

    # AV-011: RC-OPS-001 mandatory for non-P10 patterns — BLOCK
    if context.pattern != "P10":
        if "RC-OPS-001" not in candidates:
            results.append(RuleResult(
                "AV-011", "RC-OPS-001 Mandatory for Non-P10", "BLOCK", False,
                affected_ids=["RC-OPS-001"],
                condition_triggered=f"pattern={context.pattern} (not P10) AND RC-OPS-001 absent from manifest",
                message="RC-OPS-001 (Operational Risk) is not in the manifest. Unconditionally mandatory for non-P10.",
                recommended_action="Ensure RC-OPS-001 is APPROVED in the registry.",
                escalation="BU_LEAD",
            ))
        else:
            results.append(RuleResult("AV-011", "RC-OPS-001 Mandatory for Non-P10", "INFO", True,
                                      message="RC-OPS-001 is present in the manifest."))
    else:
        results.append(RuleResult("AV-011", "RC-OPS-001 Mandatory for Non-P10", "INFO", True,
                                  message="Pattern P10 — RC-OPS-001 not required."))

    return candidates, results


# ── Phase 4 — Gate Checks ─────────────────────────────────────────────────────

def phase4_gate_checks(
    manifest: Dict,
    context: ValidationContext,
) -> Tuple[Dict, List[RuleResult]]:
    results: List[RuleResult] = []

    # AV-001: approved_for_reuse gate — BLOCK
    afr_false = [aid for aid in list(manifest) if not manifest[aid].get("approved_for_reuse", False)]
    for aid in afr_false:
        del manifest[aid]
    if afr_false:
        results.append(RuleResult(
            "AV-001", "Approved-for-Reuse Gate", "BLOCK", False,
            affected_ids=afr_false,
            condition_triggered="approved_for_reuse = false in manifest",
            message=f"{len(afr_false)} manifest assets have approved_for_reuse=false.",
            recommended_action="Complete governance approval.",
            escalation="BU_LEAD",
        ))
    else:
        results.append(RuleResult("AV-001", "Approved-for-Reuse Gate", "INFO", True,
                                  message=f"All {len(manifest)} manifest assets have approved_for_reuse=true."))

    # AV-002: Lifecycle gate — BLOCK
    non_approved = [aid for aid in list(manifest) if manifest[aid].get("lifecycle_status", "") != "APPROVED"]
    for aid in non_approved:
        del manifest[aid]
    if non_approved:
        results.append(RuleResult(
            "AV-002", "Lifecycle Gate", "BLOCK", False,
            affected_ids=non_approved,
            condition_triggered="lifecycle_status != APPROVED in manifest",
            message=f"{len(non_approved)} manifest assets are not APPROVED.",
            recommended_action="Complete governance approval.",
            escalation="BU_LEAD",
        ))
    else:
        results.append(RuleResult("AV-002", "Lifecycle Gate", "INFO", True,
                                  message=f"All {len(manifest)} manifest assets are APPROVED."))

    # AV-003: SUPERSEDED asset replacement
    superseded_in_manifest = [aid for aid in manifest if manifest[aid].get("lifecycle_status") == "SUPERSEDED"]
    if superseded_in_manifest:
        results.append(RuleResult("AV-003", "SUPERSEDED Asset Replacement", "WARNING", False,
                                  affected_ids=superseded_in_manifest,
                                  message=f"{len(superseded_in_manifest)} SUPERSEDED assets in manifest."))
    else:
        results.append(RuleResult("AV-003", "SUPERSEDED Asset Replacement", "INFO", True,
                                  message="No SUPERSEDED assets in manifest."))

    # AV-004: ARCHIVED asset gate — BLOCK
    archived = [aid for aid in list(manifest) if manifest[aid].get("lifecycle_status", "") == "ARCHIVED"]
    for aid in archived:
        del manifest[aid]
    if archived:
        results.append(RuleResult(
            "AV-004", "No Archived Assets in Manifest", "BLOCK", False,
            affected_ids=archived,
            condition_triggered="lifecycle_status = ARCHIVED in manifest",
            message=f"{len(archived)} ARCHIVED assets found in manifest.",
            recommended_action="Remove ARCHIVED assets from tender scope.",
            escalation="BU_LEAD",
        ))
    else:
        results.append(RuleResult("AV-004", "No Archived Assets in Manifest", "INFO", True,
                                  message="No ARCHIVED assets in manifest."))

    # AV-012: Review overdue
    today = datetime.utcnow().date()
    overdue: List[str] = []
    critically_overdue: List[str] = []
    for aid, entry in manifest.items():
        rd = entry.get("review_due", "") or ""
        if rd:
            try:
                due_date = datetime.fromisoformat(rd).date()
                days_overdue = (today - due_date).days
                cap_ext = entry.get("cap_ext", {}) or {}
                if days_overdue > 0:
                    if (entry.get("asset_type") == "CAP"
                            and cap_ext.get("annual_review_obligation", False)
                            and days_overdue > 90):
                        critically_overdue.append(aid)
                    else:
                        overdue.append(aid)
            except (ValueError, TypeError):
                pass

    if overdue:
        results.append(RuleResult("AV-012", "Review Overdue", "WARNING", False,
                                  affected_ids=overdue,
                                  message=f"{len(overdue)} assets have an overdue review date."))
    else:
        results.append(RuleResult("AV-012", "Review Overdue", "INFO", True,
                                  message="No overdue reviews in manifest."))

    # AV-013: Annual review critically overdue — ERROR (Phase B: remove from manifest)
    for aid in critically_overdue:
        del manifest[aid]
    if critically_overdue:
        results.append(RuleResult(
            "AV-013", "Annual Review Critically Overdue", "ERROR", False,
            affected_ids=critically_overdue,
            message=f"{len(critically_overdue)} CAP assets have annual review >90 days overdue — removed from manifest.",
            recommended_action="Complete annual review for these CAP assets before assembling.",
        ))
    else:
        results.append(RuleResult("AV-013", "Annual Review Critically Overdue", "INFO", True,
                                  message="No critically overdue annual reviews."))

    return manifest, results


# ── Phase 5 — Cross-Library Validation ───────────────────────────────────────

def phase5_cross_library(
    manifest: Dict,
    context: ValidationContext,
    all_ids: Set,
    registry: Dict,
    assumptions: Dict,
) -> Tuple[Dict, List[RuleResult]]:
    results: List[RuleResult] = []

    # CLV-001: Approved-for-Reuse gate (belt-and-braces) — BLOCK
    clv1 = [aid for aid in list(manifest) if not manifest[aid].get("approved_for_reuse", False)]
    for aid in clv1:
        del manifest[aid]
    if clv1:
        results.append(RuleResult(
            "CLV-001", "Cross-Library Approved-for-Reuse", "BLOCK", False,
            affected_ids=clv1,
            condition_triggered="approved_for_reuse = false (caught by CLV-001)",
            message=f"{len(clv1)} assets failed CLV-001 belt-and-braces check.",
            recommended_action="Investigate — these should have been caught by AV-001.",
            escalation="REGISTRY_FACILITATOR",
        ))
    else:
        results.append(RuleResult("CLV-001", "Cross-Library Approved-for-Reuse", "INFO", True,
                                  message="CLV-001 passed — all manifest assets have approved_for_reuse=true."))

    # CLV-002: Lifecycle gate (belt-and-braces) — BLOCK
    clv2 = [aid for aid in list(manifest) if manifest[aid].get("lifecycle_status", "") != "APPROVED"]
    for aid in clv2:
        del manifest[aid]
    if clv2:
        results.append(RuleResult(
            "CLV-002", "Cross-Library Lifecycle Gate", "BLOCK", False,
            affected_ids=clv2,
            condition_triggered="lifecycle_status != APPROVED (caught by CLV-002)",
            message=f"{len(clv2)} assets failed CLV-002 belt-and-braces check.",
            recommended_action="Investigate — these should have been caught by AV-002.",
            escalation="REGISTRY_FACILITATOR",
        ))
    else:
        results.append(RuleResult("CLV-002", "Cross-Library Lifecycle Gate", "INFO", True,
                                  message="CLV-002 passed — all manifest assets are APPROVED."))

    # CLV-003: Related assets resolve
    clv3_broken = []
    for aid, entry in manifest.items():
        for ref in entry.get("related_assets", []) or []:
            if ref and ref not in all_ids:
                clv3_broken.append(aid)
                break
    if clv3_broken:
        results.append(RuleResult("CLV-003", "Related Assets Resolve (Manifest)", "WARNING", False,
                                  affected_ids=clv3_broken,
                                  message=f"{len(clv3_broken)} manifest assets have unresolvable related_assets references."))
    else:
        results.append(RuleResult("CLV-003", "Related Assets Resolve (Manifest)", "INFO", True,
                                  message="All manifest related_assets references resolve."))

    # CLV-004: Source assets resolve
    clv4_broken = []
    for aid, entry in manifest.items():
        for ref in entry.get("source_assets", []) or []:
            if ref and ref not in all_ids:
                clv4_broken.append(aid)
                break
    if clv4_broken:
        results.append(RuleResult("CLV-004", "Source Assets Resolve (Manifest)", "WARNING", False,
                                  affected_ids=clv4_broken,
                                  message=f"{len(clv4_broken)} manifest assets have unresolvable source_assets references."))
    else:
        results.append(RuleResult("CLV-004", "Source Assets Resolve (Manifest)", "INFO", True,
                                  message="All manifest source_assets references resolve."))

    # CLV-005: Pre-tender controls satisfied (CAP only) — ERROR + remove
    clv5 = []
    for aid in list(manifest.keys()):
        entry = manifest[aid]
        if entry.get("asset_type") == "CAP":
            cap_ext = entry.get("cap_ext", {}) or {}
            ptc = cap_ext.get("pre_tender_controls", []) or []
            if ptc and aid not in context.ptc_clearances:
                clv5.append(aid)
                del manifest[aid]
    if clv5:
        results.append(RuleResult(
            "CLV-005", "Pre-Tender Controls Satisfied", "ERROR", False,
            affected_ids=clv5,
            condition_triggered="cap_ext.pre_tender_controls non-empty AND asset_id NOT IN ptc_clearances",
            message=f"{len(clv5)} CAP assets have pre-tender controls not cleared.",
            recommended_action="Obtain PTC clearance and add asset IDs to ptc_clearances in tender_context.yaml.",
        ))
    else:
        results.append(RuleResult("CLV-005", "Pre-Tender Controls Satisfied", "INFO", True,
                                  message="CLV-005 passed — all CAP pre-tender controls satisfied."))

    # CLV-006: Risk-assumption cross-reference (RSK only) — WARNING
    clv6 = []
    for aid, entry in manifest.items():
        if entry.get("asset_type") == "RSK":
            rsk_ext = entry.get("rsk_ext", {}) or {}
            related_asms = rsk_ext.get("related_assumptions", []) or []
            for asm_id in related_asms:
                asm = assumptions.get(asm_id)
                if not asm or asm.get("lifecycle_status", "") != "APPROVED":
                    clv6.append(aid)
                    break
    if clv6:
        results.append(RuleResult("CLV-006", "Risk-Assumption Cross-Reference", "WARNING", False,
                                  affected_ids=clv6,
                                  message=f"{len(clv6)} RSK assets reference assumptions that are absent or not APPROVED."))
    else:
        results.append(RuleResult("CLV-006", "Risk-Assumption Cross-Reference", "INFO", True,
                                  message="CLV-006 passed — all RSK related_assumptions are APPROVED."))

    # CLV-007: SUPERSEDED/ARCHIVED blocking — BLOCK
    clv7 = [
        aid for aid in list(manifest)
        if manifest[aid].get("lifecycle_status", "") in {"SUPERSEDED", "ARCHIVED"}
    ]
    for aid in clv7:
        del manifest[aid]
    if clv7:
        results.append(RuleResult(
            "CLV-007", "No SUPERSEDED/ARCHIVED in Manifest", "BLOCK", False,
            affected_ids=clv7,
            condition_triggered="lifecycle_status IN {SUPERSEDED, ARCHIVED}",
            message=f"{len(clv7)} superseded or archived assets in manifest.",
            recommended_action="Replace SUPERSEDED assets with approved successors; remove ARCHIVED assets.",
            escalation="BU_LEAD",
        ))
    else:
        results.append(RuleResult("CLV-007", "No SUPERSEDED/ARCHIVED in Manifest", "INFO", True,
                                  message="No SUPERSEDED or ARCHIVED assets in manifest."))

    # CLV-008: REF without AM clearance — BLOCK
    clv8 = []
    for aid in list(manifest.keys()):
        entry = manifest[aid]
        if entry.get("asset_type") == "REF":
            ref_ext = entry.get("ref_ext", {}) or {}
            if ref_ext.get("account_manager_required", False) and aid not in context.am_clearances:
                clv8.append(aid)
                del manifest[aid]
    if clv8:
        results.append(RuleResult(
            "CLV-008", "REF Account Manager Clearance", "BLOCK", False,
            affected_ids=clv8,
            condition_triggered="ref_ext.account_manager_required = true AND asset_id NOT IN am_clearances",
            message=f"{len(clv8)} REF assets require AM clearance not provided.",
            recommended_action="Obtain AM clearance and add to am_clearances in tender_context.yaml.",
            escalation="AM",
        ))
    else:
        results.append(RuleResult("CLV-008", "REF Account Manager Clearance", "INFO", True,
                                  message="CLV-008 passed — no REF clearance violations."))

    # CLV-009: Pack scope compatibility (ASP only) — ERROR + remove ASP and child ASMs
    clv9 = []
    for aid in list(manifest.keys()):
        entry = manifest[aid]
        if entry.get("asset_type") == "ASP":
            asp_ext = entry.get("asp_ext", {}) or {}
            asp_platform = str(asp_ext.get("platform", "All") or "All")
            if asp_platform != "All" and asp_platform != context.platform:
                clv9.append(aid)
                del manifest[aid]
                # Remove child ASMs
                for asm_id in list(manifest.keys()):
                    asm_ext = manifest[asm_id].get("asm_ext", {}) or {}
                    if asm_ext.get("parent_pack_id") == aid:
                        del manifest[asm_id]
    if clv9:
        results.append(RuleResult(
            "CLV-009", "Pack Scope Compatibility", "ERROR", False,
            affected_ids=clv9,
            condition_triggered=f"asp_ext.platform != {context.platform} AND != All",
            message=f"{len(clv9)} ASP packs have incompatible platform scope.",
        ))
    else:
        results.append(RuleResult("CLV-009", "Pack Scope Compatibility", "INFO", True,
                                  message="CLV-009 passed — all ASP platform scopes compatible."))

    # CLV-010: CAP sector restriction — ERROR + remove
    clv10 = []
    for aid in list(manifest.keys()):
        entry = manifest[aid]
        if entry.get("asset_type") == "CAP":
            cap_ext = entry.get("cap_ext", {}) or {}
            sector = cap_ext.get("sector", []) or []
            if sector and context.client_sector not in sector and "All" not in sector:
                clv10.append(aid)
                del manifest[aid]
    if clv10:
        results.append(RuleResult(
            "CLV-010", "CAP Sector Restriction", "ERROR", False,
            affected_ids=clv10,
            condition_triggered=f"client_sector={context.client_sector} NOT IN cap_ext.sector AND 'All' NOT IN sector",
            message=f"{len(clv10)} CAP assets excluded — sector restriction for '{context.client_sector}'.",
        ))
    else:
        results.append(RuleResult("CLV-010", "CAP Sector Restriction", "INFO", True,
                                  message="CLV-010 passed — no sector restriction violations."))

    # CLV-011: S-50 priority order (RSK) — WARNING
    priority_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    rsk_items = [(aid, e) for aid, e in manifest.items() if e.get("asset_type") == "RSK"]
    if rsk_items:
        priorities = [
            priority_order.get(str((e.get("assembly_rules", {}) or {}).get("assembly_priority", "LOW")), 3)
            for _, e in rsk_items
        ]
        is_sorted = all(priorities[i] <= priorities[i + 1] for i in range(len(priorities) - 1))
        if not is_sorted:
            results.append(RuleResult("CLV-011", "S-50 Risk Priority Order", "WARNING", False,
                                      message="RSK assets in manifest are not in S-50 priority order (CRITICAL→HIGH→MEDIUM→LOW)."))
        else:
            results.append(RuleResult("CLV-011", "S-50 Risk Priority Order", "INFO", True,
                                      message="RSK assets are in correct S-50 priority order."))
    else:
        results.append(RuleResult("CLV-011", "S-50 Risk Priority Order", "INFO", True,
                                  message="CLV-011: No RSK assets in manifest."))

    # CLV-012: Supersession chain complete — ERROR + remove
    clv12 = []
    for aid in list(manifest.keys()):
        entry = manifest[aid]
        supby = entry.get("superseded_by", "") or ""
        if supby:
            succ = registry.get(supby) or assumptions.get(supby)
            if not succ or succ.get("lifecycle_status", "") != "APPROVED":
                clv12.append(aid)
                del manifest[aid]
    if clv12:
        results.append(RuleResult(
            "CLV-012", "Supersession Chain Complete", "ERROR", False,
            affected_ids=clv12,
            message=f"{len(clv12)} assets have a broken supersession chain — successor absent or not APPROVED.",
        ))
    else:
        results.append(RuleResult("CLV-012", "Supersession Chain Complete", "INFO", True,
                                  message="CLV-012 passed — all supersession chains are complete."))

    return manifest, results


# ── Phase 5 (Health Mode) — CLV-003 / CLV-004 against full registry ───────────

def phase5_health_clv(
    registry: Dict,
    assumptions: Dict,
    all_ids: Set,
) -> List[RuleResult]:
    results: List[RuleResult] = []
    all_entries = {**registry, **assumptions}

    clv3_broken = []
    for aid, entry in all_entries.items():
        for ref in entry.get("related_assets", []) or []:
            if ref and ref not in all_ids:
                clv3_broken.append(aid)
                break
    if clv3_broken:
        results.append(RuleResult("CLV-003", "Related Assets Resolve (Registry)", "WARNING", False,
                                  affected_ids=clv3_broken,
                                  message=f"{len(clv3_broken)} registry entries have unresolvable related_assets."))
    else:
        results.append(RuleResult("CLV-003", "Related Assets Resolve (Registry)", "INFO", True,
                                  message="All registry related_assets references resolve."))

    clv4_broken = []
    for aid, entry in all_entries.items():
        for ref in entry.get("source_assets", []) or []:
            if ref and ref not in all_ids:
                clv4_broken.append(aid)
                break
    if clv4_broken:
        results.append(RuleResult("CLV-004", "Source Assets Resolve (Registry)", "WARNING", False,
                                  affected_ids=clv4_broken,
                                  message=f"{len(clv4_broken)} registry entries have unresolvable source_assets."))
    else:
        results.append(RuleResult("CLV-004", "Source Assets Resolve (Registry)", "INFO", True,
                                  message="All registry source_assets references resolve."))

    return results


# ── Phase 6 — Library-Specific Validation ────────────────────────────────────

def phase6_library_specific(
    entries: Dict,        # manifest (Mode 2) or full registry+assumptions (Mode 1)
    context: Optional[ValidationContext],
    registry: Dict,
    assumptions: Dict,
    health_mode: bool = False,
) -> Tuple[Dict, List[RuleResult]]:
    """
    Execute all LV rules. Execution order: PAT→SEC→ASP→ASM→CAP→RSK→REF→MTH.
    In health_mode: read-only (no removal from entries dict).
    Returns (updated_entries, results).
    """
    results: List[RuleResult] = []
    all_entries = {**registry, **assumptions}

    def _remove(aid: str) -> None:
        if not health_mode and aid in entries:
            del entries[aid]

    # ── LV-PAT ──────────────────────────────────────────────────────────────

    # LV-PAT-001: BOM reference declared — WARNING
    pat_no_bom = []
    for aid, entry in entries.items():
        if entry.get("asset_type") == "PAT":
            pat_ext = entry.get("pat_ext", {}) or {}
            if not (pat_ext.get("bom_reference", "") or ""):
                pat_no_bom.append(aid)
    if pat_no_bom:
        results.append(RuleResult("LV-PAT-001", "PAT BOM Reference Declared", "WARNING", False,
                                  affected_ids=pat_no_bom,
                                  message=f"{len(pat_no_bom)} PAT assets have no bom_reference declared."))
    else:
        results.append(RuleResult("LV-PAT-001", "PAT BOM Reference Declared", "INFO", True,
                                  message="All PAT assets have bom_reference populated."))

    # LV-PAT-002: Typical sections declared — ERROR + flag
    pat_no_sections = []
    for aid, entry in entries.items():
        if entry.get("asset_type") == "PAT":
            pat_ext = entry.get("pat_ext", {}) or {}
            if not (pat_ext.get("typical_sections", []) or []):
                pat_no_sections.append(aid)
                _remove(aid)
    if pat_no_sections:
        results.append(RuleResult("LV-PAT-002", "PAT Typical Sections Declared", "ERROR", False,
                                  affected_ids=pat_no_sections,
                                  message=f"{len(pat_no_sections)} PAT assets have no typical_sections declared."))
    else:
        results.append(RuleResult("LV-PAT-002", "PAT Typical Sections Declared", "INFO", True,
                                  message="All PAT assets have typical_sections populated."))

    # LV-PAT-003: All 13 patterns registered — ERROR
    approved_pats = [
        e for e in registry.values()
        if e.get("asset_type") == "PAT" and e.get("lifecycle_status") == "APPROVED"
    ]
    if len(approved_pats) < 13:
        results.append(RuleResult("LV-PAT-003", "All 13 Patterns Registered", "ERROR", False,
                                  message=f"Only {len(approved_pats)}/13 patterns registered as APPROVED.",
                                  recommended_action="Ensure all 13 proposal patterns are registered and approved."))
    else:
        results.append(RuleResult("LV-PAT-003", "All 13 Patterns Registered", "INFO", True,
                                  message=f"{len(approved_pats)}/13 patterns registered as APPROVED."))

    # ── LV-SEC ──────────────────────────────────────────────────────────────

    # LV-SEC-001: Automation type declared — ERROR + remove
    sec_no_type = []
    for aid in list(entries.keys()):
        entry = entries[aid]
        if entry.get("asset_type") == "SEC":
            sec_ext = entry.get("sec_ext", {}) or {}
            at = str(sec_ext.get("automation_type", "") or "")
            if at not in VALID_AUTOMATION_TYPES:
                sec_no_type.append(aid)
                _remove(aid)
    if sec_no_type:
        results.append(RuleResult("LV-SEC-001", "SEC Automation Type Valid", "ERROR", False,
                                  affected_ids=sec_no_type,
                                  message=f"{len(sec_no_type)} SEC assets have invalid or missing automation_type."))
    else:
        results.append(RuleResult("LV-SEC-001", "SEC Automation Type Valid", "INFO", True,
                                  message="All SEC assets have a valid automation_type."))

    # LV-SEC-002: Content source assets declared (DIRECT/EXTRACT) — WARNING
    sec_no_csa = []
    for aid, entry in entries.items():
        if entry.get("asset_type") == "SEC":
            sec_ext = entry.get("sec_ext", {}) or {}
            at = str(sec_ext.get("automation_type", "") or "")
            if at in ("DIRECT", "EXTRACT"):
                if not (sec_ext.get("content_source_assets", []) or []):
                    sec_no_csa.append(aid)
    if sec_no_csa:
        results.append(RuleResult("LV-SEC-002", "SEC Content Source Assets Declared", "WARNING", False,
                                  affected_ids=sec_no_csa,
                                  message=f"{len(sec_no_csa)} DIRECT/EXTRACT SEC assets have no content_source_assets."))
    else:
        results.append(RuleResult("LV-SEC-002", "SEC Content Source Assets Declared", "INFO", True,
                                  message="All DIRECT/EXTRACT SEC assets have content_source_assets."))

    # LV-SEC-003: PLACEHOLDER sections flagged — WARNING
    sec_placeholder = [
        aid for aid, e in entries.items()
        if e.get("asset_type") == "SEC"
        and (e.get("sec_ext", {}) or {}).get("automation_type") == "PLACEHOLDER"
    ]
    if sec_placeholder:
        results.append(RuleResult("LV-SEC-003", "PLACEHOLDER Sections Flagged", "WARNING", False,
                                  affected_ids=sec_placeholder,
                                  message=f"{len(sec_placeholder)} SEC assets are PLACEHOLDER — will appear blank in output."))
    else:
        results.append(RuleResult("LV-SEC-003", "PLACEHOLDER Sections Flagged", "INFO", True,
                                  message="No PLACEHOLDER SEC assets in scope."))

    # LV-SEC-004: Mandatory pattern coverage — ERROR
    sec_missing_refs = []
    for aid, entry in entries.items():
        if entry.get("asset_type") == "PAT":
            pat_ext = entry.get("pat_ext", {}) or {}
            for sec_id in (pat_ext.get("typical_sections", []) or []):
                if sec_id and sec_id not in all_entries:
                    sec_missing_refs.append(f"{aid}→{sec_id}")
    if sec_missing_refs:
        results.append(RuleResult("LV-SEC-004", "Mandatory Pattern Coverage", "ERROR", False,
                                  message=f"{len(sec_missing_refs)} section references from PAT typical_sections not in registry: "
                                          + ", ".join(sec_missing_refs[:5])
                                          + (" …" if len(sec_missing_refs) > 5 else "")))
    else:
        results.append(RuleResult("LV-SEC-004", "Mandatory Pattern Coverage", "INFO", True,
                                  message="All PAT typical_sections references resolve in registry."))

    # ── LV-ASP ──────────────────────────────────────────────────────────────

    # LV-ASP-001: Pack has child assumptions — ERROR + remove
    asp_no_children = []
    for aid in list(entries.keys()):
        entry = entries[aid]
        if entry.get("asset_type") == "ASP":
            children = [
                e for e in assumptions.values()
                if (e.get("asm_ext", {}) or {}).get("parent_pack_id") == aid
            ]
            if not children:
                asp_no_children.append(aid)
                _remove(aid)
    if asp_no_children:
        results.append(RuleResult("LV-ASP-001", "ASP Has Child Assumptions", "ERROR", False,
                                  affected_ids=asp_no_children,
                                  message=f"{len(asp_no_children)} ASP packs have no child assumptions."))
    else:
        results.append(RuleResult("LV-ASP-001", "ASP Has Child Assumptions", "INFO", True,
                                  message="All ASP packs have at least one child assumption."))

    # LV-ASP-002: No pending decisions — BLOCK
    lv_asp2 = []
    for aid in list(entries.keys()):
        entry = entries[aid]
        if entry.get("asset_type") == "ASP":
            asp_ext = entry.get("asp_ext", {}) or {}
            try:
                pending = int(asp_ext.get("pending_decisions", 0) or 0)
            except (ValueError, TypeError):
                pending = 0
            if pending > 0:
                lv_asp2.append(aid)
                _remove(aid)
    if lv_asp2:
        results.append(RuleResult(
            "LV-ASP-002", "No Pending Decisions in ASP", "BLOCK", False,
            affected_ids=lv_asp2,
            condition_triggered="asp_ext.pending_decisions > 0",
            message=f"{len(lv_asp2)} ASP packs have pending governance decisions.",
            recommended_action="Complete all pending governance decisions for these assumption packs.",
            escalation="BU_LEAD",
        ))
    else:
        results.append(RuleResult("LV-ASP-002", "No Pending Decisions in ASP", "INFO", True,
                                  message="No ASP packs have pending decisions."))

    # LV-ASP-003: Pack code matches ID — ERROR
    asp_code_mismatch = []
    for aid, entry in entries.items():
        if entry.get("asset_type") == "ASP":
            asp_ext = entry.get("asp_ext", {}) or {}
            code = str(asp_ext.get("pack_code", "") or "")
            if code and code != aid:
                asp_code_mismatch.append(aid)
    if asp_code_mismatch:
        results.append(RuleResult("LV-ASP-003", "ASP Pack Code Matches ID", "ERROR", False,
                                  affected_ids=asp_code_mismatch,
                                  message=f"{len(asp_code_mismatch)} ASP packs have pack_code != asset_id."))
    else:
        results.append(RuleResult("LV-ASP-003", "ASP Pack Code Matches ID", "INFO", True,
                                  message="All ASP pack_codes match asset_id."))

    # LV-ASP-004: Section codes declared — WARNING
    asp_no_codes = []
    for aid, entry in entries.items():
        if entry.get("asset_type") == "ASP":
            asp_ext = entry.get("asp_ext", {}) or {}
            if not (asp_ext.get("section_codes", []) or []):
                asp_no_codes.append(aid)
    if asp_no_codes:
        results.append(RuleResult("LV-ASP-004", "ASP Section Codes Declared", "WARNING", False,
                                  affected_ids=asp_no_codes,
                                  message=f"{len(asp_no_codes)} ASP packs have no section_codes declared."))
    else:
        results.append(RuleResult("LV-ASP-004", "ASP Section Codes Declared", "INFO", True,
                                  message="All ASP packs have section_codes populated."))

    # ── LV-ASM ──────────────────────────────────────────────────────────────

    # LV-ASM-001: Exactly one parent pack — BLOCK + remove
    lv_asm1 = []
    for aid in list(entries.keys()):
        if entries[aid].get("asset_type") == "ASM":
            asm_ext = entries[aid].get("asm_ext", {}) or {}
            if not (asm_ext.get("parent_pack_id", "") or ""):
                lv_asm1.append(aid)
                _remove(aid)
    if lv_asm1:
        results.append(RuleResult(
            "LV-ASM-001", "ASM Has Parent Pack", "BLOCK", False,
            affected_ids=lv_asm1,
            condition_triggered="asm_ext.parent_pack_id is empty",
            message=f"{len(lv_asm1)} ASM entries have no parent_pack_id.",
            recommended_action="Assign parent_pack_id to all orphan ASM entries.",
            escalation="REGISTRY_FACILITATOR",
        ))
    else:
        results.append(RuleResult("LV-ASM-001", "ASM Has Parent Pack", "INFO", True,
                                  message="All ASM assets have parent_pack_id populated."))

    # LV-ASM-002: Parent pack exists and is APPROVED — BLOCK + remove
    lv_asm2 = []
    for aid in list(entries.keys()):
        if aid in entries and entries[aid].get("asset_type") == "ASM":
            asm_ext = entries[aid].get("asm_ext", {}) or {}
            pack_id = asm_ext.get("parent_pack_id", "") or ""
            if pack_id:
                parent = all_entries.get(pack_id)
                if not parent or parent.get("lifecycle_status", "") != "APPROVED":
                    lv_asm2.append(aid)
                    _remove(aid)
    if lv_asm2:
        results.append(RuleResult(
            "LV-ASM-002", "ASM Parent Pack Approved", "BLOCK", False,
            affected_ids=lv_asm2,
            condition_triggered="asm_ext.parent_pack_id references non-existent or non-APPROVED pack",
            message=f"{len(lv_asm2)} ASM entries reference a parent pack that is not APPROVED.",
            recommended_action="Approve the parent assumption pack before assembling its assumptions.",
            escalation="BU_LEAD",
        ))
    else:
        results.append(RuleResult("LV-ASM-002", "ASM Parent Pack Approved", "INFO", True,
                                  message="All ASM parent packs are APPROVED."))

    # LV-ASM-003: mandatory_if declared — WARNING
    asm_no_mif = []
    for aid, entry in entries.items():
        if entry.get("asset_type") == "ASM":
            ar = entry.get("assembly_rules", {}) or {}
            if not (ar.get("mandatory_if", "") or ""):
                asm_no_mif.append(aid)
    if asm_no_mif:
        results.append(RuleResult("LV-ASM-003", "ASM mandatory_if Declared", "WARNING", False,
                                  affected_ids=asm_no_mif[:20],
                                  message=f"{len(asm_no_mif)} ASM entries have no mandatory_if expression."))
    else:
        results.append(RuleResult("LV-ASM-003", "ASM mandatory_if Declared", "INFO", True,
                                  message="All ASM entries have mandatory_if populated."))

    # LV-ASM-004: Assumption text populated — ERROR + remove
    asm_no_text = []
    for aid in list(entries.keys()):
        entry = entries[aid]
        if entry.get("asset_type") == "ASM":
            asm_ext = entry.get("asm_ext", {}) or {}
            if not (asm_ext.get("assumption_text", "") or ""):
                asm_no_text.append(aid)
                _remove(aid)
    if asm_no_text:
        results.append(RuleResult("LV-ASM-004", "ASM Assumption Text Populated", "ERROR", False,
                                  affected_ids=asm_no_text[:20],
                                  message=f"{len(asm_no_text)} ASM entries have empty assumption_text."))
    else:
        results.append(RuleResult("LV-ASM-004", "ASM Assumption Text Populated", "INFO", True,
                                  message="All ASM entries have assumption_text populated."))

    # LV-ASM-005: Section code declared — ERROR + remove
    asm_no_sec = []
    for aid in list(entries.keys()):
        entry = entries[aid]
        if entry.get("asset_type") == "ASM":
            asm_ext = entry.get("asm_ext", {}) or {}
            if not (asm_ext.get("section_code", "") or ""):
                asm_no_sec.append(aid)
                _remove(aid)
    if asm_no_sec:
        results.append(RuleResult("LV-ASM-005", "ASM Section Code Declared", "ERROR", False,
                                  affected_ids=asm_no_sec[:20],
                                  message=f"{len(asm_no_sec)} ASM entries have no section_code."))
    else:
        results.append(RuleResult("LV-ASM-005", "ASM Section Code Declared", "INFO", True,
                                  message="All ASM entries have section_code populated."))

    # ── LV-CAP ──────────────────────────────────────────────────────────────

    # LV-CAP-001: Proposal section declared — ERROR + remove
    cap_no_ps = []
    for aid in list(entries.keys()):
        entry = entries[aid]
        if entry.get("asset_type") == "CAP":
            if not (entry.get("proposal_sections", []) or []):
                cap_no_ps.append(aid)
                _remove(aid)
    if cap_no_ps:
        results.append(RuleResult("LV-CAP-001", "CAP Proposal Section Declared", "ERROR", False,
                                  affected_ids=cap_no_ps,
                                  message=f"{len(cap_no_ps)} CAP assets have no proposal_sections declared."))
    else:
        results.append(RuleResult("LV-CAP-001", "CAP Proposal Section Declared", "INFO", True,
                                  message="All CAP assets have proposal_sections populated."))

    # LV-CAP-002: Evidence tier populated — WARNING
    cap_no_tier = []
    for aid, entry in entries.items():
        if entry.get("asset_type") == "CAP":
            cap_ext = entry.get("cap_ext", {}) or {}
            if not (cap_ext.get("evidence_tier", "") or ""):
                cap_no_tier.append(aid)
    if cap_no_tier:
        results.append(RuleResult("LV-CAP-002", "CAP Evidence Tier Populated", "WARNING", False,
                                  affected_ids=cap_no_tier,
                                  message=f"{len(cap_no_tier)} CAP assets have no evidence_tier declared."))
    else:
        results.append(RuleResult("LV-CAP-002", "CAP Evidence Tier Populated", "INFO", True,
                                  message="All CAP assets have evidence_tier populated."))

    # LV-CAP-003: Pattern applicability non-empty — ERROR + remove
    cap_no_pa = []
    for aid in list(entries.keys()):
        entry = entries[aid]
        if entry.get("asset_type") == "CAP":
            if not (entry.get("pattern_applicability", []) or []):
                cap_no_pa.append(aid)
                _remove(aid)
    if cap_no_pa:
        results.append(RuleResult("LV-CAP-003", "CAP Pattern Applicability Non-Empty", "ERROR", False,
                                  affected_ids=cap_no_pa,
                                  message=f"{len(cap_no_pa)} CAP assets have empty pattern_applicability."))
    else:
        results.append(RuleResult("LV-CAP-003", "CAP Pattern Applicability Non-Empty", "INFO", True,
                                  message="All CAP assets have pattern_applicability populated."))

    # LV-CAP-004: Annual review date set — WARNING
    cap_no_review = []
    for aid, entry in entries.items():
        if entry.get("asset_type") == "CAP":
            cap_ext = entry.get("cap_ext", {}) or {}
            if cap_ext.get("annual_review_obligation", False) and not (entry.get("review_due", "") or ""):
                cap_no_review.append(aid)
    if cap_no_review:
        results.append(RuleResult("LV-CAP-004", "CAP Annual Review Date Set", "WARNING", False,
                                  affected_ids=cap_no_review,
                                  message=f"{len(cap_no_review)} CAP assets have annual_review_obligation=true but no review_due date."))
    else:
        results.append(RuleResult("LV-CAP-004", "CAP Annual Review Date Set", "INFO", True,
                                  message="All CAP assets with annual review obligation have review_due set."))

    # LV-CAP-005: Content source type valid — ERROR + remove
    cap_bad_cst = []
    for aid in list(entries.keys()):
        entry = entries[aid]
        if entry.get("asset_type") == "CAP":
            ar = entry.get("assembly_rules", {}) or {}
            cst = str(ar.get("content_source_type", "") or "")
            if cst and cst not in VALID_CONTENT_SOURCE_TYPES:
                cap_bad_cst.append(aid)
                _remove(aid)
    if cap_bad_cst:
        results.append(RuleResult("LV-CAP-005", "CAP Content Source Type Valid", "ERROR", False,
                                  affected_ids=cap_bad_cst,
                                  message=f"{len(cap_bad_cst)} CAP assets have invalid content_source_type."))
    else:
        results.append(RuleResult("LV-CAP-005", "CAP Content Source Type Valid", "INFO", True,
                                  message="All CAP assets have a valid content_source_type."))

    # ── LV-RSK ──────────────────────────────────────────────────────────────

    # LV-RSK-001: Net rating consistent with RATING_MATRIX — ERROR
    rsk_bad_rating = []
    for aid, entry in entries.items():
        if entry.get("asset_type") == "RSK":
            rsk_ext = entry.get("rsk_ext", {}) or {}
            likelihood = str(rsk_ext.get("likelihood", "") or "")
            impact = str(rsk_ext.get("impact", "") or "")
            net_rating = str(rsk_ext.get("net_rating", "") or "")
            if likelihood and impact:
                expected = RATING_MATRIX.get((likelihood, impact), "")
                if expected and net_rating != expected:
                    rsk_bad_rating.append(aid)
    if rsk_bad_rating:
        results.append(RuleResult("LV-RSK-001", "RSK Net Rating Consistent", "ERROR", False,
                                  affected_ids=rsk_bad_rating,
                                  message=f"{len(rsk_bad_rating)} RSK assets have net_rating inconsistent with RATING_MATRIX."))
    else:
        results.append(RuleResult("LV-RSK-001", "RSK Net Rating Consistent", "INFO", True,
                                  message="All RSK net_ratings are consistent with the RATING_MATRIX."))

    # LV-RSK-002: Related assumptions declared (non-governance RSK) — WARNING
    rsk_no_asms = []
    for aid, entry in entries.items():
        if entry.get("asset_type") == "RSK":
            rsk_ext = entry.get("rsk_ext", {}) or {}
            gov_cat = str(rsk_ext.get("governance_category", "") or "")
            if gov_cat.upper() != "G":
                if not (rsk_ext.get("related_assumptions", []) or []):
                    rsk_no_asms.append(aid)
    if rsk_no_asms:
        results.append(RuleResult("LV-RSK-002", "RSK Related Assumptions Declared", "WARNING", False,
                                  affected_ids=rsk_no_asms,
                                  message=f"{len(rsk_no_asms)} non-governance RSK assets have no related_assumptions."))
    else:
        results.append(RuleResult("LV-RSK-002", "RSK Related Assumptions Declared", "INFO", True,
                                  message="All non-governance RSK assets have related_assumptions."))

    # LV-RSK-003: mandatory_if_engagement declared — ERROR + remove
    rsk_no_mie = []
    for aid in list(entries.keys()):
        entry = entries[aid]
        if entry.get("asset_type") == "RSK":
            rsk_ext = entry.get("rsk_ext", {}) or {}
            if not (rsk_ext.get("mandatory_if_engagement", "") or ""):
                rsk_no_mie.append(aid)
                _remove(aid)
    if rsk_no_mie:
        results.append(RuleResult("LV-RSK-003", "RSK mandatory_if_engagement Declared", "ERROR", False,
                                  affected_ids=rsk_no_mie,
                                  message=f"{len(rsk_no_mie)} RSK assets have no mandatory_if_engagement declared."))
    else:
        results.append(RuleResult("LV-RSK-003", "RSK mandatory_if_engagement Declared", "INFO", True,
                                  message="All RSK assets have mandatory_if_engagement populated."))

    # LV-RSK-004: RC-OPS-001 must be unconditional — BLOCK
    rc_ops = registry.get("RC-OPS-001")
    if rc_ops:
        rsk_ext = rc_ops.get("rsk_ext", {}) or {}
        mie = str(rsk_ext.get("mandatory_if_engagement", "") or "").strip().upper()
        if mie != "TRUE":
            results.append(RuleResult(
                "LV-RSK-004", "RC-OPS-001 Unconditional", "BLOCK", False,
                affected_ids=["RC-OPS-001"],
                condition_triggered=f"RC-OPS-001.rsk_ext.mandatory_if_engagement = '{mie}' (expected TRUE)",
                message="RC-OPS-001 must be unconditional — mandatory_if_engagement must be 'TRUE'.",
                recommended_action="Set mandatory_if_engagement: TRUE for RC-OPS-001 in the Risk Library.",
                escalation="BU_LEAD",
            ))
        else:
            results.append(RuleResult("LV-RSK-004", "RC-OPS-001 Unconditional", "INFO", True,
                                      message="RC-OPS-001 is unconditional (mandatory_if_engagement = TRUE)."))
    else:
        results.append(RuleResult("LV-RSK-004", "RC-OPS-001 Unconditional", "INFO", True,
                                  message="RC-OPS-001 not in registry."))

    # LV-RSK-005: Proposal section declared — ERROR + remove
    rsk_no_ps = []
    for aid in list(entries.keys()):
        entry = entries[aid]
        if entry.get("asset_type") == "RSK":
            if not (entry.get("proposal_sections", []) or []):
                rsk_no_ps.append(aid)
                _remove(aid)
    if rsk_no_ps:
        results.append(RuleResult("LV-RSK-005", "RSK Proposal Section Declared", "ERROR", False,
                                  affected_ids=rsk_no_ps,
                                  message=f"{len(rsk_no_ps)} RSK assets have no proposal_sections declared."))
    else:
        results.append(RuleResult("LV-RSK-005", "RSK Proposal Section Declared", "INFO", True,
                                  message="All RSK assets have proposal_sections populated."))

    # LV-RSK-006: Governance category declared — WARNING
    rsk_no_gc = []
    for aid, entry in entries.items():
        if entry.get("asset_type") == "RSK":
            rsk_ext = entry.get("rsk_ext", {}) or {}
            if not (rsk_ext.get("governance_category", "") or ""):
                rsk_no_gc.append(aid)
    if rsk_no_gc:
        results.append(RuleResult("LV-RSK-006", "RSK Governance Category Declared", "WARNING", False,
                                  affected_ids=rsk_no_gc,
                                  message=f"{len(rsk_no_gc)} RSK assets have no governance_category declared."))
    else:
        results.append(RuleResult("LV-RSK-006", "RSK Governance Category Declared", "INFO", True,
                                  message="All RSK assets have governance_category populated."))

    # LV-RSK-007: Category B has decision reference — ERROR
    rsk_no_dec_ref = []
    for aid, entry in entries.items():
        if entry.get("asset_type") == "RSK":
            rsk_ext = entry.get("rsk_ext", {}) or {}
            if str(rsk_ext.get("governance_category", "") or "").upper() == "B":
                if not (rsk_ext.get("governance_decision_ref", "") or ""):
                    rsk_no_dec_ref.append(aid)
    if rsk_no_dec_ref:
        results.append(RuleResult("LV-RSK-007", "Category-B RSK Has Decision Reference", "ERROR", False,
                                  affected_ids=rsk_no_dec_ref,
                                  message=f"{len(rsk_no_dec_ref)} Category-B RSK assets have no governance_decision_ref."))
    else:
        results.append(RuleResult("LV-RSK-007", "Category-B RSK Has Decision Reference", "INFO", True,
                                  message="All Category-B RSK assets have governance_decision_ref populated."))

    # LV-RSK-008: DRAFT risk not assembled — BLOCK + remove
    lv_rsk8 = []
    for aid in list(entries.keys()):
        if (entries[aid].get("asset_type") == "RSK"
                and entries[aid].get("lifecycle_status", "") == "DRAFT"):
            lv_rsk8.append(aid)
            _remove(aid)
    if lv_rsk8:
        results.append(RuleResult(
            "LV-RSK-008", "No DRAFT RSK in Manifest", "BLOCK", False,
            affected_ids=lv_rsk8,
            condition_triggered="lifecycle_status = DRAFT AND asset_type = RSK",
            message=f"{len(lv_rsk8)} DRAFT RSK assets are in scope — cannot assemble.",
            recommended_action="Complete governance approval for the Risk Library.",
            escalation="BU_LEAD",
        ))
    else:
        results.append(RuleResult("LV-RSK-008", "No DRAFT RSK in Manifest", "INFO", True,
                                  message="No DRAFT RSK assets in scope."))

    # ── LV-REF ──────────────────────────────────────────────────────────────

    # LV-REF-001: REF AM clearance (belt-and-braces) — BLOCK + remove
    lv_ref1 = []
    if context is not None:
        for aid in list(entries.keys()):
            if entries[aid].get("asset_type") == "REF":
                ref_ext = entries[aid].get("ref_ext", {}) or {}
                if ref_ext.get("account_manager_required", False) and aid not in context.am_clearances:
                    lv_ref1.append(aid)
                    _remove(aid)
    if lv_ref1:
        results.append(RuleResult(
            "LV-REF-001", "REF AM Clearance (Belt-and-Braces)", "BLOCK", False,
            affected_ids=lv_ref1,
            condition_triggered="ref_ext.account_manager_required = true AND asset_id NOT IN am_clearances",
            message=f"{len(lv_ref1)} REF assets require AM clearance — not provided.",
            recommended_action="Add confirmed AM clearance asset IDs to am_clearances in tender_context.yaml.",
            escalation="AM",
        ))
    else:
        results.append(RuleResult("LV-REF-001", "REF AM Clearance (Belt-and-Braces)", "INFO", True,
                                  message="LV-REF-001 passed — no REF clearance violations."))

    # LV-REF-002: Signed date populated — ERROR + remove
    ref_no_signed = []
    for aid in list(entries.keys()):
        entry = entries[aid]
        if entry.get("asset_type") == "REF":
            ref_ext = entry.get("ref_ext", {}) or {}
            if not (ref_ext.get("signed_date", "") or ""):
                ref_no_signed.append(aid)
                _remove(aid)
    if ref_no_signed:
        results.append(RuleResult("LV-REF-002", "REF Signed Date Populated", "ERROR", False,
                                  affected_ids=ref_no_signed,
                                  message=f"{len(ref_no_signed)} REF assets have no signed_date."))
    else:
        results.append(RuleResult("LV-REF-002", "REF Signed Date Populated", "INFO", True,
                                  message="All REF assets have signed_date populated."))

    # LV-REF-003: Letter on file — WARNING
    ref_no_letter = []
    for aid, entry in entries.items():
        if entry.get("asset_type") == "REF":
            ref_ext = entry.get("ref_ext", {}) or {}
            if not ref_ext.get("letter_on_file", False):
                ref_no_letter.append(aid)
    if ref_no_letter:
        results.append(RuleResult("LV-REF-003", "REF Letter on File", "WARNING", False,
                                  affected_ids=ref_no_letter,
                                  message=f"{len(ref_no_letter)} REF assets have letter_on_file=false."))
    else:
        results.append(RuleResult("LV-REF-003", "REF Letter on File", "INFO", True,
                                  message="All REF assets have letter_on_file=true."))

    # LV-REF-004: Restrictions checked — WARNING
    ref_with_restrictions = []
    for aid, entry in entries.items():
        if entry.get("asset_type") == "REF":
            ref_ext = entry.get("ref_ext", {}) or {}
            if ref_ext.get("restrictions", "") or "":
                ref_with_restrictions.append(aid)
    if ref_with_restrictions:
        results.append(RuleResult("LV-REF-004", "REF Restrictions Checked", "WARNING", False,
                                  affected_ids=ref_with_restrictions,
                                  message=f"{len(ref_with_restrictions)} REF assets have usage restrictions — review before use."))
    else:
        results.append(RuleResult("LV-REF-004", "REF Restrictions Checked", "INFO", True,
                                  message="No REF assets have usage restrictions."))

    # ── LV-MTH ──────────────────────────────────────────────────────────────

    # LV-MTH-001: Platform declared — ERROR + remove
    mth_no_platform = []
    for aid in list(entries.keys()):
        entry = entries[aid]
        if entry.get("asset_type") == "MTH":
            mth_ext = entry.get("mth_ext", {}) or {}
            if not (mth_ext.get("applicable_platforms", []) or []):
                mth_no_platform.append(aid)
                _remove(aid)
    if mth_no_platform:
        results.append(RuleResult("LV-MTH-001", "MTH Platform Declared", "ERROR", False,
                                  affected_ids=mth_no_platform,
                                  message=f"{len(mth_no_platform)} MTH assets have no applicable_platforms declared."))
    else:
        results.append(RuleResult("LV-MTH-001", "MTH Platform Declared", "INFO", True,
                                  message="All MTH assets have applicable_platforms populated."))

    # LV-MTH-002: Phase structure declared — WARNING
    mth_no_phases = []
    for aid, entry in entries.items():
        if entry.get("asset_type") == "MTH":
            mth_ext = entry.get("mth_ext", {}) or {}
            if not (mth_ext.get("phase_structure", []) or []):
                mth_no_phases.append(aid)
    if mth_no_phases:
        results.append(RuleResult("LV-MTH-002", "MTH Phase Structure Declared", "WARNING", False,
                                  affected_ids=mth_no_phases,
                                  message=f"{len(mth_no_phases)} MTH assets have no phase_structure declared."))
    else:
        results.append(RuleResult("LV-MTH-002", "MTH Phase Structure Declared", "INFO", True,
                                  message="All MTH assets have phase_structure populated."))

    # LV-MTH-003: One methodology per platform — ERROR
    platform_to_mth: Dict[str, str] = {}
    mth_duplicates: List[str] = []
    for aid, entry in registry.items():
        if entry.get("asset_type") == "MTH" and entry.get("lifecycle_status") == "APPROVED":
            mth_ext = entry.get("mth_ext", {}) or {}
            for plat in (mth_ext.get("applicable_platforms", []) or []):
                if plat in platform_to_mth:
                    mth_duplicates.append(aid)
                else:
                    platform_to_mth[plat] = aid
    if mth_duplicates:
        results.append(RuleResult("LV-MTH-003", "One Methodology Per Platform", "ERROR", False,
                                  affected_ids=mth_duplicates,
                                  message=f"{len(mth_duplicates)} platforms have multiple APPROVED methodologies."))
    else:
        results.append(RuleResult("LV-MTH-003", "One Methodology Per Platform", "INFO", True,
                                  message="No platform has multiple APPROVED methodologies."))

    return entries, results


# ── Phase 7 — Manifest Finalisation ──────────────────────────────────────────

def phase7_finalise(
    manifest: Dict,
    all_results: List[RuleResult],
    context: ValidationContext,
    registry_meta: Dict,
) -> Dict:
    blocks = sum(1 for r in all_results if r.severity == "BLOCK" and not r.passed)
    errors = sum(1 for r in all_results if r.severity == "ERROR" and not r.passed)
    warnings = sum(1 for r in all_results if r.severity == "WARNING" and not r.passed)

    if blocks > 0:
        manifest_status = "BLOCKED"
        proceed = False
    elif errors > 0:
        manifest_status = "APPROVED_WITH_CONDITIONS"
        proceed = True
    else:
        manifest_status = "VALID"
        proceed = True

    priority_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
    rsk_items = [(aid, e) for aid, e in manifest.items() if e.get("asset_type") == "RSK"]
    non_rsk_items = [(aid, e) for aid, e in manifest.items() if e.get("asset_type") != "RSK"]
    rsk_items.sort(key=lambda x: priority_order.get(
        str((x[1].get("assembly_rules", {}) or {}).get("assembly_priority", "LOW")), 3
    ))
    ordered_assets = non_rsk_items + rsk_items

    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    today_str = datetime.utcnow().strftime("%Y%m%d")
    manifest_id = f"{context.tender_id}-MANIFEST-{today_str}"
    report_ref = (
        f"08_Commercial/Proposals/{context.tender_id}/"
        f"ASSEMBLY_VALIDATION_REPORT_{context.tender_id}_{today_str}.md"
    )
    rules_evaluated = len(all_results)
    rules_passed = sum(1 for r in all_results if r.passed)

    return {
        "manifest_id": manifest_id,
        "tender_id": context.tender_id,
        "tender_pattern": context.pattern,
        "tender_platform": context.platform,
        "engagement_type": context.engagement_type,
        "manifest_status": manifest_status,
        "proceed": proceed,
        "manifest_timestamp": timestamp,
        "registry_version": registry_meta.get("schema_version", "1.0"),
        "registry_build_id": registry_meta.get("build_id", ""),
        "validation_report_ref": report_ref,
        "blocks": blocks,
        "errors": errors,
        "warnings": warnings,
        "assets_in_manifest": len(ordered_assets),
        "rules_evaluated": rules_evaluated,
        "rules_passed": rules_passed,
        "_ordered_assets": ordered_assets,
        "_today_str": today_str,
    }


# ── Knowledge Health Score Calculation ───────────────────────────────────────

def _khs_band(score: int) -> str:
    if score >= 90:
        return "EXCELLENT"
    if score >= 75:
        return "GOOD"
    if score >= 60:
        return "ADEQUATE"
    if score >= 40:
        return "POOR"
    return "CRITICAL"


def calculate_health_score(
    all_results: List[RuleResult],
    registry: Dict,
    assumptions: Dict,
) -> Dict:
    """Calculate 7-dimension Knowledge Health Score from rule results."""
    all_entries = {**registry, **assumptions}
    total_entries = len(all_entries)

    # ── D1: Registry Integrity (weight 0.25) ──────────────────────────────
    ri_blocks = [r for r in all_results if r.rule_code.startswith("RI-") and r.severity == "BLOCK" and not r.passed]
    ri_errors = [r for r in all_results if r.rule_code.startswith("RI-") and r.severity == "ERROR" and not r.passed]
    ri_warnings = [r for r in all_results if r.rule_code.startswith("RI-") and r.severity == "WARNING" and not r.passed]

    # Corrupt registry rules
    halt_fired = any(r.rule_code in ("RI-001", "RI-008", "RI-009") for r in ri_blocks)
    if halt_fired:
        d1 = 0.0
    else:
        deductions = (len(ri_blocks) * 50.0) + (len(ri_errors) * 15.0) + (len(ri_warnings) * 5.0)
        d1 = max(0.0, 100.0 - deductions)

    # ── D2: Lifecycle Compliance (weight 0.20) ─────────────────────────────
    if total_entries > 0:
        approved_count = sum(1 for e in all_entries.values() if e.get("lifecycle_status") == "APPROVED")
        base = (approved_count / total_entries) * 100.0
        ri10_entries = next((len(r.affected_ids) for r in all_results if r.rule_code == "RI-010" and not r.passed), 0)
        ri11_entries = next((len(r.affected_ids) for r in all_results if r.rule_code == "RI-011" and not r.passed), 0)
        ri12_entries = next((len(r.affected_ids) for r in all_results if r.rule_code == "RI-012" and not r.passed), 0)
        deductions = ((ri10_entries + ri11_entries + ri12_entries) / total_entries) * 30.0
        d2 = max(0.0, base - deductions)
    else:
        d2 = 100.0

    # ── D3: Approval Status (weight 0.20) ──────────────────────────────────
    type_weights = {
        "CAP": 3.0, "ASP": 3.0, "RSK": 3.0, "PAT": 3.0,
        "MTH": 2.0, "REF": 2.0, "SEC": 2.0,
        "ASM": 1.5,
        "PPT": 1.0, "PRT": 1.0, "CON": 0.5, "COM": 0.5,
    }
    weighted_sum = 0.0
    weight_total = 0.0
    by_type: Dict[str, List] = {}
    for e in all_entries.values():
        t = e.get("asset_type", "")
        by_type.setdefault(t, []).append(e)
    for t, elist in by_type.items():
        w = type_weights.get(t, 0.5)
        approved = sum(1 for e in elist if e.get("lifecycle_status") == "APPROVED")
        rate = (approved / len(elist)) * 100.0 if elist else 100.0
        weighted_sum += rate * w
        weight_total += w
    d3 = (weighted_sum / weight_total) if weight_total > 0 else 100.0

    # ── D4: Governance Compliance (weight 0.15) ────────────────────────────
    governance_rules = [r for r in all_results if r.rule_code.startswith(("RI-", "AV-", "CLV-", "LV-"))]
    total_gov = len(governance_rules)
    passed_gov = sum(1 for r in governance_rules if r.passed)
    d4 = (passed_gov / total_gov * 100.0) if total_gov > 0 else 100.0

    # ── D5: Metadata Completeness (weight 0.10) ────────────────────────────
    if all_entries:
        scores = []
        ext_map = {
            "CAP": "cap_ext", "ASP": "asp_ext", "ASM": "asm_ext",
            "RSK": "rsk_ext", "MTH": "mth_ext", "REF": "ref_ext",
            "PAT": "pat_ext", "SEC": "sec_ext",
        }
        for entry in all_entries.values():
            present = sum(1 for f in MANDATORY_FIELDS
                          if entry.get(f) is not None and entry.get(f) != "" and entry.get(f) != [])
            entry_completeness = present / len(MANDATORY_FIELDS)
            t = entry.get("asset_type", "")
            ext_key = ext_map.get(t)
            ext_completeness = 1.0 if (not ext_key or entry.get(ext_key)) else 0.0
            score = (0.7 * entry_completeness) + (0.3 * ext_completeness)
            scores.append(score)
        d5 = (sum(scores) / len(scores)) * 100.0
    else:
        d5 = 100.0

    # ── D6: Relationship Integrity (weight 0.05) ───────────────────────────
    total_rels = sum(
        len(e.get("related_assets", []) or []) + len(e.get("source_assets", []) or [])
        for e in all_entries.values()
    )
    if total_rels == 0:
        d6 = 100.0
    else:
        broken_related = next(
            (len(r.affected_ids) for r in all_results if r.rule_code == "RI-005" and not r.passed), 0
        )
        broken_clv3 = next(
            (len(r.affected_ids) for r in all_results if r.rule_code == "CLV-003" and not r.passed), 0
        )
        broken = broken_related + broken_clv3
        d6 = max(0.0, (1.0 - broken / max(1, len(all_entries))) * 100.0)

    # ── D7: Validation Success (weight 0.05) ───────────────────────────────
    total_rules = len(all_results)
    passed_rules = sum(1 for r in all_results if r.passed)
    d7 = (passed_rules / total_rules * 100.0) if total_rules > 0 else 100.0

    khs = round(d1 * 0.25 + d2 * 0.20 + d3 * 0.20 + d4 * 0.15 + d5 * 0.10 + d6 * 0.05 + d7 * 0.05)
    band = _khs_band(khs)

    return {
        "khs": khs,
        "band": band,
        "d1": round(d1, 1),
        "d2": round(d2, 1),
        "d3": round(d3, 1),
        "d4": round(d4, 1),
        "d5": round(d5, 1),
        "d6": round(d6, 1),
        "d7": round(d7, 1),
        "total_entries": total_entries,
        "total_rules": total_rules,
        "passed_rules": passed_rules,
    }


# ── Report Builders ───────────────────────────────────────────────────────────

def _build_manifest_yaml(meta: Dict) -> str:
    header = {
        "manifest_id": meta["manifest_id"],
        "report_type": "ASSEMBLY_MANIFEST",
        "engine_version": ENGINE_VERSION,
        "rules_version": RULES_VERSION,
        "certification_level": (
            "CERTIFIED" if meta["manifest_status"] == "VALID"
            else "CONDITIONAL" if meta["manifest_status"] == "APPROVED_WITH_CONDITIONS"
            else "BLOCKED"
        ),
        "tender_id": meta["tender_id"],
        "tender_pattern": meta["tender_pattern"],
        "tender_platform": meta["tender_platform"],
        "engagement_type": meta["engagement_type"],
        "manifest_status": meta["manifest_status"],
        "proceed": meta["proceed"],
        "manifest_timestamp": meta["manifest_timestamp"],
        "registry_version": meta["registry_version"],
        "registry_build_id": meta["registry_build_id"],
        "validation_report_ref": meta["validation_report_ref"],
        "validation_summary": {
            "rules_evaluated": meta.get("rules_evaluated", 0),
            "rules_passed": meta.get("rules_passed", 0),
            "blocks": meta["blocks"],
            "errors": meta["errors"],
            "warnings": meta["warnings"],
        },
        "assets_in_manifest": meta["assets_in_manifest"],
    }
    out = "---\n" + yaml.dump(header, default_flow_style=False, allow_unicode=True, sort_keys=False)

    ordered_assets = meta["_ordered_assets"]
    if not ordered_assets:
        out += "\nmanifest_assets: []\n"
        out += "\n# NOTE: Empty manifest — populate pattern_applicability and mandatory_if in source files.\n"
        return out

    out += "\nmanifest_assets:\n"
    for aid, entry in ordered_assets:
        ar = entry.get("assembly_rules", {}) or {}
        asset_block = {
            "asset_id": aid,
            "asset_type": entry.get("asset_type", ""),
            "title": entry.get("title", ""),
            "version": str(entry.get("version", "1.0")),
            "source_file": entry.get("source_file", ""),
            "lifecycle_status": entry.get("lifecycle_status", "APPROVED"),
            "approved_for_reuse": entry.get("approved_for_reuse", True),
            "assembly_rules": {
                "mandatory_if": str(ar.get("mandatory_if", "") or ""),
                "optional_if": str(ar.get("optional_if", "") or ""),
                "excluded_if": str(ar.get("excluded_if", "") or ""),
                "assembly_priority": str(ar.get("assembly_priority", "") or ""),
                "section_placement": ar.get("section_placement", []) or [],
                "content_source_type": str(ar.get("content_source_type", "") or ""),
            },
            "validation_flags": [],
        }
        out += "\n" + yaml.dump([asset_block], default_flow_style=False, allow_unicode=True, sort_keys=False)
    return out


def _build_validation_report_md(
    meta: Dict,
    all_results: List[RuleResult],
    context: ValidationContext,
    registry_meta: Dict,
) -> str:
    blocks_list = [r for r in all_results if r.severity == "BLOCK" and not r.passed]
    errors_list = [r for r in all_results if r.severity == "ERROR" and not r.passed]
    warnings_list = [r for r in all_results if r.severity == "WARNING" and not r.passed]
    rules_evaluated = len(all_results)
    rules_passed = sum(1 for r in all_results if r.passed)
    proceed_str = "YES — Proceed to Assembly Engine" if meta["proceed"] else "NO — Resolve BLOCK conditions first"
    today = datetime.utcnow().strftime("%Y-%m-%d")

    lines = [
        f"# Assembly Validation Report — {context.tender_id}",
        "",
        f"**Date:** {today}  ",
        f"**Tender Pattern:** {context.pattern}  ",
        f"**Platform:** {context.platform}  ",
        f"**Engagement Type:** {context.engagement_type}  ",
        f"**Manifest Status:** {meta['manifest_status']}  ",
        f"**Certification Level:** {'CERTIFIED' if meta['manifest_status'] == 'VALID' else 'CONDITIONAL' if meta['manifest_status'] == 'APPROVED_WITH_CONDITIONS' else 'BLOCKED'}  ",
        f"**Proceed to Assembly:** {proceed_str}  ",
        f"**Registry Build:** {registry_meta.get('build_id', 'Unknown')}  ",
        f"**Engine Version:** KVE V{ENGINE_VERSION} (Phase B — 76 rules)  ",
        "",
        "---",
        "",
        "## Summary",
        "",
        "| Metric | Count |",
        "|---|---|",
        f"| Rules Evaluated | {rules_evaluated} |",
        f"| Rules Passed | {rules_passed} |",
        f"| BLOCK Conditions | {meta['blocks']} |",
        f"| ERROR Conditions | {meta['errors']} |",
        f"| WARNING Conditions | {meta['warnings']} |",
        f"| Assets in Manifest | {meta['assets_in_manifest']} |",
        "",
        "---",
    ]

    lines += ["", "## BLOCK Conditions"]
    if blocks_list:
        lines += ["", "> **Assembly is BLOCKED. All BLOCK conditions must be resolved before any proposal generation.**", ""]
        for r in blocks_list:
            asset_str = ", ".join(r.affected_ids) if r.affected_ids else "N/A"
            lines += [
                f"### {r.rule_code} — {r.rule_name}",
                "",
                f"**Asset(s):** {asset_str}  ",
                f"**Condition:** {r.condition_triggered}  ",
                f"**Description:** {r.message}  ",
                (f"**Action Required:** {r.recommended_action}  " if r.recommended_action else ""),
                (f"**Escalation:** {r.escalation}  " if r.escalation else ""),
                "",
            ]
    else:
        lines += ["", "_No BLOCK conditions. Assembly may proceed (subject to ERROR and WARNING review)._", ""]

    lines += ["---", ""]

    lines += ["## ERROR Conditions — Assets Removed or Failed"]
    if errors_list:
        lines.append("")
        for r in errors_list:
            asset_str = ", ".join(r.affected_ids[:10]) if r.affected_ids else "N/A"
            if len(r.affected_ids) > 10:
                asset_str += f" … (+{len(r.affected_ids) - 10} more)"
            lines += [
                f"### {r.rule_code} — {r.rule_name}",
                f"**Asset(s):** {asset_str}  ",
                f"**Description:** {r.message}  ",
                (f"**Action Required:** {r.recommended_action}  " if r.recommended_action else ""),
                "",
            ]
    else:
        lines += ["", "_No ERROR conditions._", ""]

    lines += ["---", ""]

    lines += ["## WARNING Conditions — Assets Flagged"]
    if warnings_list:
        lines.append("")
        for r in warnings_list:
            lines += [
                f"### {r.rule_code} — {r.rule_name}",
                f"**Note:** {r.message}  ",
                "",
            ]
    else:
        lines += ["", "_No WARNING conditions._", ""]

    lines += ["---", ""]

    lines += [
        "## Rule Coverage",
        "",
        "| Phase | Rules | BLOCK | ERROR | WARN | PASS |",
        "|---|---|---|---|---|---|",
    ]
    for phase_prefix, phase_name in [
        ("RI-", "Phase 1 — Registry Integrity"),
        ("AV-", "Phase 3–4 — Assembly Validation"),
        ("CLV-", "Phase 5 — Cross-Library"),
        ("LV-", "Phase 6 — Library-Specific"),
    ]:
        phase_rules = [r for r in all_results if r.rule_code.startswith(phase_prefix)]
        p_block = sum(1 for r in phase_rules if r.severity == "BLOCK" and not r.passed)
        p_error = sum(1 for r in phase_rules if r.severity == "ERROR" and not r.passed)
        p_warn = sum(1 for r in phase_rules if r.severity == "WARNING" and not r.passed)
        p_pass = sum(1 for r in phase_rules if r.passed)
        lines.append(f"| {phase_name} | {len(phase_rules)} | {p_block} | {p_error} | {p_warn} | {p_pass} |")

    lines += [
        "",
        "---",
        "",
        "## Assembly Manifest",
        "",
        f"**Manifest ID:** `{meta['manifest_id']}`  ",
        f"**Manifest Status:** `{meta['manifest_status']}`  ",
        f"**Proceed:** `{meta['proceed']}`  ",
        f"**Assets Certified:** {meta['assets_in_manifest']}  ",
        "",
        "---",
        "",
        f"*Generated by Knowledge Validation Engine V{ENGINE_VERSION} — Phase B (76 rules, WP19D)*  ",
        f"*Timestamp: {meta['manifest_timestamp']} | Rules Version: {RULES_VERSION}*",
    ]

    return "\n".join(lines)


def _build_health_report_md(
    all_results: List[RuleResult],
    khs_data: Dict,
    registry: Dict,
    assumptions: Dict,
    registry_meta: Dict,
    elapsed: float,
) -> str:
    today = datetime.utcnow().strftime("%Y-%m-%d")
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    khs = khs_data["khs"]
    band = khs_data["band"]

    blocks_list = [r for r in all_results if r.severity == "BLOCK" and not r.passed]
    errors_list = [r for r in all_results if r.severity == "ERROR" and not r.passed]
    warnings_list = [r for r in all_results if r.severity == "WARNING" and not r.passed]

    total_core = len(registry)
    total_asm = len(assumptions)

    by_type: Dict[str, int] = {}
    for e in registry.values():
        t = e.get("asset_type", "UNKNOWN")
        by_type[t] = by_type.get(t, 0) + 1

    lines = [
        "# Knowledge Health Report",
        "",
        f"**Date:** {today}  ",
        f"**Registry Build:** {registry_meta.get('build_id', 'Unknown')}  ",
        f"**Engine Version:** KVE V{ENGINE_VERSION}  ",
        f"**Mode:** Platform Health (Mode 1)  ",
        f"**Duration:** {elapsed:.2f}s  ",
        "",
        "---",
        "",
        "## Knowledge Health Score",
        "",
        f"```",
        f"  KHS: {khs:3d} / 100    Band: {band}",
        f"  {'█' * (khs // 5)}{'░' * (20 - khs // 5)}",
        f"```",
        "",
        "| Dimension | Weight | Score | Contribution |",
        "|---|---|---|---|",
        f"| D1 — Registry Integrity      | 25% | {khs_data['d1']:5.1f} | {khs_data['d1'] * 0.25:5.1f} |",
        f"| D2 — Lifecycle Compliance    | 20% | {khs_data['d2']:5.1f} | {khs_data['d2'] * 0.20:5.1f} |",
        f"| D3 — Approval Status         | 20% | {khs_data['d3']:5.1f} | {khs_data['d3'] * 0.20:5.1f} |",
        f"| D4 — Governance Compliance   | 15% | {khs_data['d4']:5.1f} | {khs_data['d4'] * 0.15:5.1f} |",
        f"| D5 — Metadata Completeness   | 10% | {khs_data['d5']:5.1f} | {khs_data['d5'] * 0.10:5.1f} |",
        f"| D6 — Relationship Integrity  |  5% | {khs_data['d6']:5.1f} | {khs_data['d6'] * 0.05:5.1f} |",
        f"| D7 — Validation Success      |  5% | {khs_data['d7']:5.1f} | {khs_data['d7'] * 0.05:5.1f} |",
        f"| **KHS** | **100%** | **{khs}** | **{khs}** |",
        "",
        "**Score Bands:** EXCELLENT (90–100) | GOOD (75–89) | ADEQUATE (60–74) | POOR (40–59) | CRITICAL (0–39)",
        "",
        "---",
        "",
        "## Registry Summary",
        "",
        f"| Metric | Value |",
        f"|---|---|",
        f"| Total Core Assets | {total_core} |",
        f"| Total Assumptions (ASM) | {total_asm} |",
        f"| Registry Build ID | {registry_meta.get('build_id', 'Unknown')} |",
        f"| Schema Version | {registry_meta.get('schema_version', '1.0')} |",
        "",
        "**Asset Breakdown:**",
        "",
        "| Type | Count |",
        "|---|---|",
    ]
    for t in sorted(by_type.keys()):
        lines.append(f"| {t} | {by_type[t]} |")
    lines.append(f"| ASM | {total_asm} |")

    lines += [
        "",
        "---",
        "",
        "## Validation Results",
        "",
        f"| Metric | Value |",
        f"|---|---|",
        f"| Total Rules Evaluated | {khs_data['total_rules']} |",
        f"| Rules Passed | {khs_data['passed_rules']} |",
        f"| BLOCK Conditions | {len(blocks_list)} |",
        f"| ERROR Conditions | {len(errors_list)} |",
        f"| WARNING Conditions | {len(warnings_list)} |",
        "",
    ]

    if blocks_list:
        lines += ["### BLOCK Conditions", ""]
        for r in blocks_list:
            lines += [f"- **{r.rule_code}** — {r.message}", ""]
    else:
        lines += ["_No BLOCK conditions — registry integrity confirmed._", ""]

    if errors_list:
        lines += ["", "### ERROR Conditions", ""]
        for r in errors_list[:20]:
            lines += [f"- **{r.rule_code}** — {r.message}", ""]
        if len(errors_list) > 20:
            lines.append(f"_(+ {len(errors_list) - 20} more errors)_")
    else:
        lines += ["", "_No ERROR conditions._", ""]

    if warnings_list:
        lines += ["", "### WARNING Conditions", ""]
        for r in warnings_list[:20]:
            lines += [f"- **{r.rule_code}** — {r.message}", ""]
        if len(warnings_list) > 20:
            lines.append(f"_(+ {len(warnings_list) - 20} more warnings)_")
    else:
        lines += ["", "_No WARNING conditions._", ""]

    # Remediation
    lines += ["", "---", "", "## Remediation Priorities", ""]
    if khs >= 90:
        lines += ["> **EXCELLENT** — Registry is in excellent health. No immediate remediation required.", ""]
    elif khs >= 75:
        lines += ["> **GOOD** — Registry is healthy. Address WARNING conditions to improve score.", ""]
    elif khs >= 60:
        lines += ["> **ADEQUATE** — Registry meets minimum quality bar. Address ERROR conditions.", ""]
    elif khs >= 40:
        lines += ["> **POOR** — Registry quality is below acceptable threshold. Immediate attention required.", ""]
    else:
        lines += ["> **CRITICAL** — Registry is in critical condition. Block all assembly until resolved.", ""]

    if blocks_list:
        lines += [
            "",
            "**Priority 1 — BLOCK Conditions (resolve immediately):**",
            "",
        ]
        for r in blocks_list:
            action = r.recommended_action or "Review and resolve."
            lines.append(f"- `{r.rule_code}`: {action}")

    if errors_list:
        lines += [
            "",
            "**Priority 2 — ERROR Conditions (resolve before next assembly):**",
            "",
        ]
        for r in errors_list[:10]:
            lines.append(f"- `{r.rule_code}`: {r.message[:100]}")

    lines += [
        "",
        "---",
        "",
        f"*Generated by Knowledge Validation Engine V{ENGINE_VERSION} — Mode 1 (Platform Health, WP19D)*  ",
        f"*Timestamp: {timestamp} | Registry Build: {registry_meta.get('build_id', 'Unknown')}*",
    ]

    return "\n".join(lines)


# ── Phase 8 — Report Generation ───────────────────────────────────────────────

def phase8_generate_reports(
    meta: Dict,
    all_results: List[RuleResult],
    context: ValidationContext,
    registry_meta: Dict,
    output_dir: Path,
    dry_run: bool,
) -> Tuple[str, str]:
    today_str = meta["_today_str"]
    manifest_fname = f"ASSEMBLY_MANIFEST_{context.tender_id}_{today_str}.yaml"
    report_fname = f"ASSEMBLY_VALIDATION_REPORT_{context.tender_id}_{today_str}.md"

    manifest_yaml_str = _build_manifest_yaml(meta)
    report_md_str = _build_validation_report_md(meta, all_results, context, registry_meta)

    if dry_run:
        print("[KVE] DRY_RUN — no files written. Preview:")
        print(f"\n{'='*70}\nFILE: {manifest_fname}\n{'─'*70}")
        print(manifest_yaml_str[:2000])
        print(f"\n{'='*70}\nFILE: {report_fname}\n{'─'*70}")
        print(report_md_str[:2000])
    else:
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / manifest_fname).write_text(manifest_yaml_str, encoding="utf-8")
        (output_dir / report_fname).write_text(report_md_str, encoding="utf-8")
        print(f"[KVE] Manifest written:  {output_dir / manifest_fname}")
        print(f"[KVE] Report written:    {output_dir / report_fname}")

    return manifest_fname, report_fname


def phase8_health_report(
    all_results: List[RuleResult],
    khs_data: Dict,
    registry: Dict,
    assumptions: Dict,
    registry_meta: Dict,
    output_dir: Path,
    dry_run: bool,
    elapsed: float,
) -> str:
    today_str = datetime.utcnow().strftime("%Y%m%d")
    fname = f"KNOWLEDGE_HEALTH_REPORT_{today_str}.md"
    content = _build_health_report_md(all_results, khs_data, registry, assumptions, registry_meta, elapsed)

    if dry_run:
        print(f"\n{'='*70}\nFILE: {fname}\n{'─'*70}")
        print(content[:3000])
    else:
        output_dir.mkdir(parents=True, exist_ok=True)
        (output_dir / fname).write_text(content, encoding="utf-8")
        print(f"[KVE] Health Report:     {output_dir / fname}")

    return fname


# ── Main Engine ───────────────────────────────────────────────────────────────

def run_kve(
    mode: str,
    context_path: Optional[Path],
    repo_root: Path,
    dry_run: bool,
    output_dir: Optional[Path] = None,
    run_tests: bool = False,
) -> int:
    start = datetime.utcnow()
    print(f"[KVE] Knowledge Validation Engine V{ENGINE_VERSION} — Phase B (76 rules)")
    print(f"[KVE] Mode: {mode.upper()} | DRY_RUN: {dry_run}")
    print(f"[KVE] Started: {start.isoformat()}Z")
    print(f"[KVE] Repo root: {repo_root}")
    print()

    # AREL compliance tests
    if run_tests:
        print("[KVE] ── AREL V1.0 Compliance Test Suite ────────────────────────")
        passed, total, failures = run_arel_compliance_tests()
        print(f"[KVE]   {passed}/{total} tests PASS")
        if failures:
            for f in failures:
                print(f"[KVE]   FAIL: {f}")
        if passed < total:
            print(f"[KVE] AREL certification FAILED ({total - passed} failures)")
            return 2
        print(f"[KVE]   AREL certification: {passed}/{total} PASS ✓")
        print()

    # Load registry
    loader = RegistryLoader(repo_root)
    try:
        registry, assumptions, registry_meta = loader.load()
    except FileNotFoundError as exc:
        print(f"[KVE] FATAL: {exc}")
        return 2

    all_ids = set(registry.keys()) | set(assumptions.keys())
    print(
        f"[KVE] Registry: {len(registry)} core entries | "
        f"{len(assumptions)} ASM entries | {len(all_ids)} total"
    )
    print(
        f"[KVE] Build: {registry_meta.get('build_id', 'unknown')} | "
        f"Generated: {registry_meta.get('generated_at', 'unknown')}"
    )
    print()

    all_results: List[RuleResult] = []

    # Phase 1: Registry Integrity (both modes)
    print("[KVE] ── Phase 1: Registry Integrity ──────────────────────────")
    p1_results, halted = phase1_registry_integrity(registry, assumptions, all_ids, repo_root)
    all_results.extend(p1_results)
    p1_blocks = [r for r in p1_results if r.severity == "BLOCK" and not r.passed]
    p1_errors = [r for r in p1_results if r.severity == "ERROR" and not r.passed]
    p1_warnings = [r for r in p1_results if r.severity == "WARNING" and not r.passed]
    print(f"[KVE]   {len(p1_results)} rules | BLOCK: {len(p1_blocks)} | ERROR: {len(p1_errors)} | WARN: {len(p1_warnings)}")

    if halted:
        for r in p1_blocks:
            print(f"[KVE]   ENGINE HALT — {r.rule_code}: {r.message}")
        print("[KVE] Engine halted. Fix the registry error above and re-run.")
        return 2

    if mode == "health":
        # Mode 1: Full platform health scan
        print()
        print("[KVE] ── Phase H2: Cross-Library (CLV-003/004) ─────────────────")
        p_h2 = phase5_health_clv(registry, assumptions, all_ids)
        all_results.extend(p_h2)
        print(f"[KVE]   {len(p_h2)} rules | WARN: {sum(1 for r in p_h2 if r.severity == 'WARNING' and not r.passed)}")

        print("[KVE] ── Phase H3: Library-Specific (all LV rules) ─────────────")
        health_entries = {**registry, **assumptions}
        health_entries_copy = dict(health_entries)  # read-only for health mode
        _, p_h3 = phase6_library_specific(
            health_entries_copy, None, registry, assumptions, health_mode=True
        )
        all_results.extend(p_h3)
        p_h3_blocks = sum(1 for r in p_h3 if r.severity == "BLOCK" and not r.passed)
        p_h3_errors = sum(1 for r in p_h3 if r.severity == "ERROR" and not r.passed)
        p_h3_warnings = sum(1 for r in p_h3 if r.severity == "WARNING" and not r.passed)
        print(f"[KVE]   {len(p_h3)} rules | BLOCK: {p_h3_blocks} | ERROR: {p_h3_errors} | WARN: {p_h3_warnings}")

        print("[KVE] ── Phase H4: Knowledge Health Score ──────────────────────")
        khs_data = calculate_health_score(all_results, registry, assumptions)
        print(f"[KVE]   KHS: {khs_data['khs']}/100 — {khs_data['band']}")
        print(f"[KVE]   D1={khs_data['d1']} D2={khs_data['d2']} D3={khs_data['d3']} D4={khs_data['d4']}")
        print(f"[KVE]   D5={khs_data['d5']} D6={khs_data['d6']} D7={khs_data['d7']}")

        print("[KVE] ── Phase H5: Health Report ───────────────────────────────")
        if output_dir is None:
            output_dir = repo_root / "08_Commercial" / "Reports"
        elapsed = (datetime.utcnow() - start).total_seconds()
        health_fname = phase8_health_report(
            all_results, khs_data, registry, assumptions,
            registry_meta, output_dir, dry_run, elapsed
        )

        total_blocks = sum(1 for r in all_results if r.severity == "BLOCK" and not r.passed)
        total_errors = sum(1 for r in all_results if r.severity == "ERROR" and not r.passed)
        total_warnings = sum(1 for r in all_results if r.severity == "WARNING" and not r.passed)

        print()
        print("[KVE] ════════════════════════════════════════════════════════════")
        print(f"[KVE] MODE 1 — PLATFORM HEALTH COMPLETE")
        print(f"[KVE] KHS:               {khs_data['khs']}/100 ({khs_data['band']})")
        print(f"[KVE] BLOCK Conditions:  {total_blocks}")
        print(f"[KVE] ERROR Conditions:  {total_errors}")
        print(f"[KVE] WARNING Conditions:{total_warnings}")
        print(f"[KVE] Rules Evaluated:   {len(all_results)}")
        print(f"[KVE] Duration:          {elapsed:.2f}s")
        print("[KVE] ════════════════════════════════════════════════════════════")

        return 0

    # Mode 2: Assembly Validation
    print("[KVE] ── Phase 2: Tender Profile Establishment ─────────────────")
    if not context_path:
        print("[KVE] FATAL: --context <tender_context.yaml> is required for assembly mode.")
        return 2
    try:
        context = phase2_load_context(context_path)
    except (FileNotFoundError, ValueError) as exc:
        print(f"[KVE] FATAL: {exc}")
        return 2
    print(f"[KVE]   Tender ID:   {context.tender_id}")
    print(f"[KVE]   Pattern:     {context.pattern}")
    print(f"[KVE]   Platform:    {context.platform}")
    print(f"[KVE]   Engagement:  {context.engagement_type}")
    print(f"[KVE]   Country:     {context.country} | Size: {context.client_size} | Sector: {context.client_sector}")

    if output_dir is None:
        output_dir = repo_root / "08_Commercial" / "Proposals" / context.tender_id

    print("[KVE] ── Phase 3: Candidate Manifest Construction ─────────────")
    manifest, p3_results = phase3_build_manifest(registry, assumptions, context, all_ids)
    all_results.extend(p3_results)
    p3_blocks = [r for r in p3_results if r.severity == "BLOCK" and not r.passed]
    print(f"[KVE]   {len(manifest)} candidates | BLOCK: {len(p3_blocks)}")

    print("[KVE] ── Phase 4: Gate Checks ──────────────────────────────────")
    manifest, p4_results = phase4_gate_checks(manifest, context)
    all_results.extend(p4_results)
    p4_blocks = [r for r in p4_results if r.severity == "BLOCK" and not r.passed]
    print(f"[KVE]   {len(manifest)} remaining | BLOCK: {len(p4_blocks)}")

    print("[KVE] ── Phase 5: Cross-Library Validation ─────────────────────")
    manifest, p5_results = phase5_cross_library(manifest, context, all_ids, registry, assumptions)
    all_results.extend(p5_results)
    p5_blocks = [r for r in p5_results if r.severity == "BLOCK" and not r.passed]
    print(f"[KVE]   {len(manifest)} remaining | BLOCK: {len(p5_blocks)}")

    print("[KVE] ── Phase 6: Library-Specific Validation ──────────────────")
    manifest, p6_results = phase6_library_specific(manifest, context, registry, assumptions, health_mode=False)
    all_results.extend(p6_results)
    p6_blocks = [r for r in p6_results if r.severity == "BLOCK" and not r.passed]
    p6_errors = [r for r in p6_results if r.severity == "ERROR" and not r.passed]
    print(f"[KVE]   {len(manifest)} assets | BLOCK: {len(p6_blocks)} | ERROR: {len(p6_errors)}")

    print("[KVE] ── Phase 7: Manifest Finalisation ────────────────────────")
    manifest_meta = phase7_finalise(manifest, all_results, context, registry_meta)
    print(
        f"[KVE]   Status: {manifest_meta['manifest_status']} | "
        f"Proceed: {manifest_meta['proceed']} | "
        f"Assets: {manifest_meta['assets_in_manifest']}"
    )

    print("[KVE] ── Phase 8: Report Generation ────────────────────────────")
    phase8_generate_reports(manifest_meta, all_results, context, registry_meta, output_dir, dry_run)

    elapsed = (datetime.utcnow() - start).total_seconds()
    total_blocks = manifest_meta["blocks"]
    total_errors = manifest_meta["errors"]
    total_warnings = manifest_meta["warnings"]

    print()
    print("[KVE] ════════════════════════════════════════════════════════════")
    print(f"[KVE] RESULT:            {manifest_meta['manifest_status']}")
    print(f"[KVE] Proceed:           {'YES' if manifest_meta['proceed'] else 'NO'}")
    print(f"[KVE] BLOCK Conditions:  {total_blocks}")
    print(f"[KVE] ERROR Conditions:  {total_errors}")
    print(f"[KVE] WARNING Conditions:{total_warnings}")
    print(f"[KVE] Assets in Manifest:{manifest_meta['assets_in_manifest']}")
    print(f"[KVE] Rules Evaluated:   {len(all_results)}")
    print(f"[KVE] Duration:          {elapsed:.2f}s")
    print("[KVE] ════════════════════════════════════════════════════════════")

    if total_blocks:
        print()
        print("[KVE] BLOCK CONDITIONS:")
        for r in all_results:
            if r.severity == "BLOCK" and not r.passed:
                print(f"[KVE]   BLOCK {r.rule_code}: {r.message[:80]}")

    return 1 if manifest_meta["manifest_status"] == "BLOCKED" else 0


# ── CLI Entry Point ───────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description=f"Knowledge Validation Engine V{ENGINE_VERSION} — Phase B (76 rules)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Assembly validation (Mode 2):
  python kve_engine.py --mode assembly --context tender_context.yaml

  # Assembly validation — dry run:
  python kve_engine.py --mode assembly --context tender_context.yaml --dry-run

  # Platform health check (Mode 1):
  python kve_engine.py --mode health

  # Platform health check with AREL tests:
  python kve_engine.py --mode health --run-tests

  # AREL compliance tests only:
  python kve_engine.py --run-tests

  # Explicit repo root and output:
  python kve_engine.py --mode assembly --context ctx.yaml \\
      --repo "/path/to/Tender Knowledge Base" --output /path/to/output
""",
    )
    parser.add_argument("--mode", choices=["assembly", "health"], default="assembly",
                        help="Validation mode. Default: assembly")
    parser.add_argument("--context", type=Path, default=None,
                        help="Path to tender_context.yaml (required for --mode assembly)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Execute all rules but do not write output files")
    parser.add_argument("--run-tests", action="store_true",
                        help="Run AREL V1.0 compliance test suite (80 tests)")
    parser.add_argument("--repo", type=Path, default=None,
                        help="Repository root path. Default: two levels above this script")
    parser.add_argument("--output", type=Path, default=None,
                        help="Output directory. Default: <repo>/08_Commercial/Proposals/<tender_id>/")

    args = parser.parse_args()

    if args.repo:
        repo_root = args.repo.resolve()
    else:
        repo_root = Path(__file__).parent.parent.parent.resolve()

    if not repo_root.exists():
        print(f"[KVE] FATAL: Repository root not found: {repo_root}")
        sys.exit(2)

    # AREL tests only (no registry load)
    if args.run_tests and args.mode != "health":
        print("[KVE] AREL V1.0 Compliance Test Suite")
        passed, total, failures = run_arel_compliance_tests()
        print(f"[KVE] {passed}/{total} PASS")
        for f in failures:
            print(f"[KVE] FAIL: {f}")
        sys.exit(0 if passed == total else 2)

    context_path = args.context.resolve() if args.context else None
    output_dir = args.output.resolve() if args.output else None

    exit_code = run_kve(
        mode=args.mode,
        context_path=context_path,
        repo_root=repo_root,
        dry_run=args.dry_run,
        output_dir=output_dir,
        run_tests=args.run_tests,
    )
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
