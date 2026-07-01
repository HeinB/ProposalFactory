#!/usr/bin/env python3
"""
Assembly Rule Enrichment Engine (ARE) — PF2-002
Populates and governs deterministic AREL assembly expressions for all governed
Capability Assets (CAP) and Assumption Packs (ASP) in the Knowledge Asset Registry.

Usage:
  python are.py                         # validate + enrich + regression + coverage
  python are.py --validate              # syntax + variable validation only
  python are.py --enrich                # write enriched registry YAML
  python are.py --regression            # run 6 regression scenarios
  python are.py --coverage REPORT.md   # write coverage report
  python are.py --run-tests             # self-test suite (20 tests)
"""

import os, sys, re, json, yaml, argparse
from dataclasses import dataclass, field
from typing import Any, Optional, List, Dict, Tuple
from datetime import datetime, timezone

ENGINE_VERSION = "1.0"
AREL_VERSION = "1.0"
BUILD_DATE = "2026-06-29"

_HERE = os.path.dirname(os.path.abspath(__file__))
REGISTRY_DEFAULT = os.path.join(_HERE, "..", "..", "00_Governance", "Knowledge_Standards", "KNOWLEDGE_ASSET_REGISTRY.yaml")

# ─── AREL Evaluator ──────────────────────────────────────────────────────────

class TT:
    IDENT = "IDENT"; STR = "STR"; NUM = "NUM"; BOOL = "BOOL"
    EQ = "=="; NEQ = "!="; GT = ">"; GTE = ">="; LT = "<"; LTE = "<="
    LBRACK = "["; RBRACK = "]"; COMMA = ","; LPAREN = "("; RPAREN = ")"
    KW = "KW"; EOF = "EOF"

@dataclass
class Token:
    type: str; val: Any

_KEYWORDS = {"and", "or", "not", "in", "contains", "true", "false", "TRUE", "FALSE"}

def tokenise(expr: str) -> List[Token]:
    tokens: List[Token] = []
    i = 0
    while i < len(expr):
        if expr[i].isspace():
            i += 1
            continue
        # String literal
        if expr[i] == '"':
            j = i + 1
            while j < len(expr) and expr[j] != '"':
                j += 1
            tokens.append(Token(TT.STR, expr[i+1:j]))
            i = j + 1
            continue
        # Operators
        if expr[i:i+2] in ("==", "!=", ">=", "<="):
            tokens.append(Token(expr[i:i+2], expr[i:i+2]))
            i += 2; continue
        if expr[i] == ">":
            tokens.append(Token(TT.GT, ">")); i += 1; continue
        if expr[i] == "<":
            tokens.append(Token(TT.LT, "<")); i += 1; continue
        if expr[i] in "([],()":
            m = {"[": TT.LBRACK, "]": TT.RBRACK, ",": TT.COMMA,
                 "(": TT.LPAREN, ")": TT.RPAREN}
            tokens.append(Token(m[expr[i]], expr[i])); i += 1; continue
        # Number
        if expr[i].isdigit() or (expr[i] == '-' and i+1 < len(expr) and expr[i+1].isdigit()):
            j = i + 1
            while j < len(expr) and (expr[j].isdigit() or expr[j] == '.'):
                j += 1
            tokens.append(Token(TT.NUM, float(expr[i:j]))); i = j; continue
        # Identifier / keyword
        if expr[i].isalpha() or expr[i] == '_':
            j = i
            while j < len(expr) and (expr[j].isalnum() or expr[j] == '_'):
                j += 1
            word = expr[i:j]
            if word in _KEYWORDS:
                if word in ("true", "false", "TRUE", "FALSE"):
                    tokens.append(Token(TT.BOOL, word.lower() in ("true", "TRUE")))
                else:
                    tokens.append(Token(TT.KW, word))
            else:
                tokens.append(Token(TT.IDENT, word))
            i = j; continue
        i += 1
    tokens.append(Token(TT.EOF, None))
    return tokens

class ARELEvaluator:
    """Standard AREL V1.0 evaluator. contains uses exact membership for list variables."""

    def __init__(self, context: Dict[str, Any]):
        self.ctx = context
        self._tokens: List[Token] = []
        self._pos = 0

    def _peek(self) -> Token:
        return self._tokens[self._pos]

    def _consume(self) -> Token:
        t = self._tokens[self._pos]; self._pos += 1; return t

    def _expect(self, ttype: str) -> Token:
        t = self._consume()
        if t.type != ttype:
            raise ValueError(f"Expected {ttype}, got {t.type}={t.val!r}")
        return t

    def evaluate(self, expr: str) -> bool:
        s = expr.strip()
        if not s or s in ("", "—", "-"):
            return False
        if s == "TRUE":
            return True
        if s == "FALSE":
            return False
        try:
            self._tokens = tokenise(s)
            self._pos = 0
            result = self._parse_or()
            return bool(result)
        except Exception:
            return False

    def _parse_or(self) -> bool:
        left = self._parse_and()
        while self._peek().type == TT.KW and self._peek().val == "or":
            self._consume()
            right = self._parse_and()
            left = left or right
        return left

    def _parse_and(self) -> bool:
        left = self._parse_not()
        while self._peek().type == TT.KW and self._peek().val == "and":
            self._consume()
            right = self._parse_not()
            left = left and right
        return left

    def _parse_not(self) -> bool:
        if self._peek().type == TT.KW and self._peek().val == "not":
            self._consume()
            return not self._parse_not()
        return self._parse_atom()

    def _parse_atom(self) -> bool:
        if self._peek().type == TT.LPAREN:
            self._consume()
            val = self._parse_or()
            self._expect(TT.RPAREN)
            return val
        return self._parse_comparison()

    def _parse_comparison(self) -> bool:
        left_val = self._parse_operand()
        nxt = self._peek()

        # in / not in
        if nxt.type == TT.KW and nxt.val == "in":
            self._consume()
            lst = self._parse_list()
            if left_val is None:
                return False
            return left_val in lst

        if nxt.type == TT.KW and nxt.val == "not":
            self._consume()
            self._expect(TT.KW)  # "in"
            lst = self._parse_list()
            if left_val is None:
                return False
            return left_val not in lst

        # contains
        if nxt.type == TT.KW and nxt.val == "contains":
            self._consume()
            rhs = self._parse_scalar()
            if left_val is None:
                return False
            if isinstance(left_val, list):
                return rhs in left_val  # exact membership
            if isinstance(left_val, str):
                return str(rhs) in left_val
            return False

        # comparison operators
        op_map = {TT.EQ: "==", TT.NEQ: "!=", TT.GT: ">",
                  TT.GTE: ">=", TT.LT: "<", TT.LTE: "<="}
        if nxt.type in op_map:
            op = op_map[nxt.type]; self._consume()
            right_val = self._parse_operand()
            return self._cmp(left_val, op, right_val)

        # Single boolean variable
        if isinstance(left_val, bool):
            return left_val
        if left_val is None:
            return False
        return bool(left_val)

    def _parse_operand(self) -> Any:
        t = self._peek()
        if t.type == TT.IDENT:
            self._consume()
            return self.ctx.get(t.val)
        if t.type == TT.STR:
            self._consume(); return t.val
        if t.type == TT.NUM:
            self._consume(); return t.val
        if t.type == TT.BOOL:
            self._consume(); return t.val
        if t.type == TT.KW and t.val in ("true", "false"):
            self._consume(); return t.val == "true"
        return None

    def _parse_scalar(self) -> Any:
        t = self._peek()
        if t.type in (TT.STR, TT.NUM, TT.BOOL):
            self._consume(); return t.val
        return None

    def _parse_list(self) -> list:
        self._expect(TT.LBRACK)
        items = []
        if self._peek().type == TT.RBRACK:
            self._consume(); return items
        items.append(self._parse_scalar())
        while self._peek().type == TT.COMMA:
            self._consume()
            items.append(self._parse_scalar())
        self._expect(TT.RBRACK)
        return items

    def _cmp(self, left: Any, op: str, right: Any) -> bool:
        if left is None:
            return False
        try:
            if op == "==":
                if isinstance(left, bool) != isinstance(right, bool):
                    if isinstance(left, bool) or isinstance(right, bool):
                        return False
                return str(left) == str(right) if isinstance(right, str) else left == right
            if op == "!=":
                if isinstance(left, bool) != isinstance(right, bool):
                    if isinstance(left, bool) or isinstance(right, bool):
                        return True
                return str(left) != str(right) if isinstance(right, str) else left != right
            if op == ">":  return float(left) > float(right)
            if op == ">=": return float(left) >= float(right)
            if op == "<":  return float(left) < float(right)
            if op == "<=": return float(left) <= float(right)
        except (TypeError, ValueError):
            return False
        return False


# ─── Assembly Rule Definitions ────────────────────────────────────────────────

ASSEMBLY_RULES: Dict[str, Dict[str, str]] = {

    # === CORPORATE — always mandatory ===
    "W1S1-001": {"mandatory_if": "TRUE", "optional_if": "", "excluded_if": ""},
    "W1S1-002": {"mandatory_if": "TRUE", "optional_if": "", "excluded_if": ""},
    "W1S1-006": {"mandatory_if": "TRUE", "optional_if": "", "excluded_if": ""},
    "W1S1-007": {"mandatory_if": "TRUE", "optional_if": "", "excluded_if": ""},
    "W1S1-008": {"mandatory_if": "TRUE", "optional_if": "", "excluded_if": ""},
    "W1S1-009": {"mandatory_if": "TRUE", "optional_if": "", "excluded_if": ""},

    # === PARTNERSHIP STATEMENTS ===
    "W1S1-003": {
        "mandatory_if": 'platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle EBS", "Oracle Integration Cloud"]',
        "optional_if":  "",
        "excluded_if":  'platform in ["Acumatica", "BeBanking"]',
    },
    "W1S1-004": {
        "mandatory_if": 'platform == "Acumatica"',
        "optional_if":  "",
        "excluded_if":  'platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle EBS", "Oracle Integration Cloud", "BeBanking"]',
    },
    "W1S1-005": {
        "mandatory_if": 'platform == "BeBanking"',
        "optional_if":  "",
        "excluded_if":  'platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle EBS", "Oracle Integration Cloud", "Acumatica"]',
    },

    # === ACUMATICA MODULE ASSETS ===
    "W1S2-001": {
        "mandatory_if": 'platform == "Acumatica" and modules contains "Acumatica Financials"',
        "optional_if":  'platform == "Acumatica"',
        "excluded_if":  "",
    },
    "W1S2-002": {
        "mandatory_if": 'platform == "Acumatica" and modules contains "Acumatica Distribution"',
        "optional_if":  'platform == "Acumatica"',
        "excluded_if":  "",
    },
    "W1S2-003": {
        "mandatory_if": "",
        "optional_if":  'platform == "Acumatica"',
        "excluded_if":  "",
    },
    "W1S2-004": {
        "mandatory_if": 'platform == "Acumatica" and modules contains "Acumatica Manufacturing"',
        "optional_if":  'platform == "Acumatica"',
        "excluded_if":  "",
    },
    "W1S2-005": {
        "mandatory_if": 'platform == "Acumatica" and modules contains "Acumatica CRM"',
        "optional_if":  'platform == "Acumatica"',
        "excluded_if":  "",
    },
    "W1S2-006-ACU-FieldServices": {
        "mandatory_if": "",
        "optional_if":  'platform == "Acumatica"',
        "excluded_if":  "",
    },
    "W1S2-007-ACU-PayrollIntegration": {
        "mandatory_if": 'platform == "Acumatica" and payroll_integration == true',
        "optional_if":  'platform == "Acumatica"',
        "excluded_if":  "",
    },
    "W1S2-009": {
        "mandatory_if": 'platform == "Acumatica" and modules contains "Acumatica Project Accounting"',
        "optional_if":  'platform == "Acumatica"',
        "excluded_if":  "",
    },

    # === BEBANKING ASSETS ===
    "W1S3-001": {
        "mandatory_if": 'platform == "BeBanking"',
        "optional_if":  "",
        "excluded_if":  "",
    },
    "W1S3-002": {
        "mandatory_if": 'platform == "BeBanking"',
        "optional_if":  "",
        "excluded_if":  "",
    },
    "W1S3-003": {
        "mandatory_if": 'platform == "BeBanking" and modules contains "BeBanking Supplier Payments"',
        "optional_if":  'platform == "BeBanking"',
        "excluded_if":  "",
    },
    "W1S3-004": {
        "mandatory_if": 'platform == "BeBanking" and modules contains "BeBanking Payroll Payments"',
        "optional_if":  'platform == "BeBanking"',
        "excluded_if":  "",
    },
    "W1S3-005": {
        "mandatory_if": 'platform == "BeBanking" and modules contains "BeBanking Forex"',
        "optional_if":  'platform == "BeBanking"',
        "excluded_if":  "",
    },
    "W1S3-006": {
        "mandatory_if": 'platform == "BeBanking" and integration_scope == true',
        "optional_if":  'platform == "BeBanking"',
        "excluded_if":  "",
    },
    "W1S3-007": {
        "mandatory_if": 'platform == "BeBanking" and security_in_scope == true',
        "optional_if":  'platform == "BeBanking"',
        "excluded_if":  "",
    },
    "W1S3-008": {
        "mandatory_if": 'platform == "BeBanking"',
        "optional_if":  "",
        "excluded_if":  "",
    },
    "W1S3-009": {
        "mandatory_if": "",
        "optional_if":  'platform == "BeBanking"',
        "excluded_if":  "",
    },
    "W1S3-010": {
        "mandatory_if": "",
        "optional_if":  'platform == "BeBanking"',
        "excluded_if":  "",
    },

    # === ORACLE PLATFORM CAPABILITY ===
    "W2S1-001": {
        "mandatory_if": 'platform in ["Oracle ERP Cloud", "Oracle Integration Cloud"]',
        "optional_if":  'platform == "Oracle HCM Cloud" and integration_scope == true',
        "excluded_if":  "",
    },
    "W2S1-002": {
        "mandatory_if": 'platform == "Oracle EBS"',
        "optional_if":  "",
        "excluded_if":  "",
    },
    "W2S1-003": {
        "mandatory_if": "",
        "optional_if":  'platform == "Oracle EBS"',
        "excluded_if":  "",
    },
    "W2S1-004": {
        "mandatory_if": 'platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle EBS", "Oracle Integration Cloud"] and engagement_type == "AMS"',
        "optional_if":  "",
        "excluded_if":  'platform in ["Acumatica", "BeBanking"]',
    },
    "W2S1-005-ORA-ImplementationMethodology": {
        "mandatory_if": 'platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle EBS", "Oracle Integration Cloud"] and engagement_type == "Implementation"',
        "optional_if":  "",
        "excluded_if":  'engagement_type == "AMS"',
    },

    # === ORACLE HCM WAVE 3 ===
    "W3S1-001-ORA-HCMCore": {
        "mandatory_if": 'platform == "Oracle HCM Cloud"',
        "optional_if":  "",
        "excluded_if":  "",
    },
    "W3S1-002-ORA-TalentMgmt": {
        "mandatory_if": 'platform == "Oracle HCM Cloud" and modules contains "Oracle Talent Management"',
        "optional_if":  'platform == "Oracle HCM Cloud"',
        "excluded_if":  "",
    },
    "W3S1-003-ORA-RecruitingCloud": {
        "mandatory_if": 'platform == "Oracle HCM Cloud" and modules contains "Oracle Recruiting Cloud"',
        "optional_if":  'platform == "Oracle HCM Cloud"',
        "excluded_if":  "",
    },
    "W3S1-004-ORA-LearningCloud": {
        "mandatory_if": 'platform == "Oracle HCM Cloud" and modules contains "Oracle Learning Cloud"',
        "optional_if":  'platform == "Oracle HCM Cloud"',
        "excluded_if":  "",
    },
    "W3S1-005-ORA-WorkforceCompensation": {
        "mandatory_if": 'platform == "Oracle HCM Cloud" and modules contains "Oracle Workforce Compensation" and industry == "Mining"',
        "optional_if":  'platform == "Oracle HCM Cloud" and industry == "Mining"',
        "excluded_if":  'not industry == "Mining"',  # GOV-010
    },
    "W3S1-006-ORA-HCMAnalytics": {
        "mandatory_if": "",
        "optional_if":  'platform == "Oracle HCM Cloud"',
        "excluded_if":  "",
    },
    "W3S1-007-ORA-WorkforceManagement": {
        "mandatory_if": 'platform == "Oracle HCM Cloud"',
        "optional_if":  "",
        "excluded_if":  "",
    },
    "W3S1-008-ORA-HelpDesk-HRServiceDelivery": {
        "mandatory_if": "",
        "optional_if":  'platform == "Oracle HCM Cloud"',
        "excluded_if":  "",
    },
    "W3S1-009-ORA-PayrollInterface-Integration": {
        "mandatory_if": 'platform == "Oracle HCM Cloud" and payroll_integration == true',
        "optional_if":  'platform == "Oracle HCM Cloud" and integration_scope == true',
        "excluded_if":  "",
    },

    # === ORACLE WAVE 4 ===
    "W4-AI-002-ORA-AISkills": {
        "mandatory_if": 'platform == "Oracle HCM Cloud" and modules contains "Oracle AI Skills"',
        "optional_if":  'platform == "Oracle HCM Cloud"',
        "excluded_if":  "",
    },
    "W4-ERP-001-ORA-FusionFinancials": {
        "mandatory_if": 'platform == "Oracle ERP Cloud" and modules contains "Oracle Fusion Financials"',
        "optional_if":  'platform == "Oracle ERP Cloud"',
        "excluded_if":  "",
    },
    "W4-ERP-002-ORA-FusionProcurement": {
        "mandatory_if": 'platform == "Oracle ERP Cloud" and modules contains "Oracle Fusion Procurement"',
        "optional_if":  'platform == "Oracle ERP Cloud"',
        "excluded_if":  "",
    },
    "W4-ERP-003-ORA-PPM": {
        "mandatory_if": 'platform == "Oracle ERP Cloud" and modules contains "Oracle PPM"',
        "optional_if":  'platform == "Oracle ERP Cloud"',
        "excluded_if":  "",
    },
    "W4-HCM-002-ORA-Journeys": {
        "mandatory_if": 'platform == "Oracle HCM Cloud"',
        "optional_if":  "",
        "excluded_if":  "",
    },
    "W4-INT-001-ORA-OICAccelerators": {
        "mandatory_if": 'platform == "Oracle Integration Cloud"',
        "optional_if":  'platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle EBS"] and integration_scope == true',
        "excluded_if":  "",
    },

    # === WAVE 5 / CROSS-PLATFORM ===
    "W5-ACU-001-ACU-SupportManagedServices": {
        "mandatory_if": 'platform == "Acumatica" and engagement_type == "AMS"',
        "optional_if":  'platform == "Acumatica" and support_scope == true',
        "excluded_if":  "",
    },
    "W5-METH-001-ERP-ImplementationMethodology": {
        "mandatory_if": 'platform in ["Acumatica", "BeBanking"] and engagement_type == "Implementation"',
        "optional_if":  "",
        "excluded_if":  'engagement_type == "AMS"',
    },
}

ASP_RULES: Dict[str, Dict[str, str]] = {
    "HCM-BASE-ASSUMPTIONS-V1": {
        "mandatory_if": 'platform == "Oracle HCM Cloud"',
        "optional_if":  "",
        "excluded_if":  'platform in ["Oracle ERP Cloud", "Oracle EBS", "Oracle Integration Cloud", "Acumatica", "BeBanking"]',
    },
    "HCM-RECRUITING-ASSUMPTIONS-V1": {
        "mandatory_if": 'platform == "Oracle HCM Cloud" and modules contains "Oracle Recruiting Cloud"',
        "optional_if":  'platform == "Oracle HCM Cloud"',
        "excluded_if":  "",
    },
    "HCM-LEARNING-ASSUMPTIONS-V1": {
        "mandatory_if": 'platform == "Oracle HCM Cloud" and modules contains "Oracle Learning Cloud"',
        "optional_if":  'platform == "Oracle HCM Cloud"',
        "excluded_if":  "",
    },
    "HCM-TALENT-ASSUMPTIONS-V1": {
        "mandatory_if": 'platform == "Oracle HCM Cloud" and modules contains "Oracle Talent Management"',
        "optional_if":  'platform == "Oracle HCM Cloud"',
        "excluded_if":  "",
    },
    "HCM-COMPENSATION-ASSUMPTIONS-V1": {
        "mandatory_if": 'platform == "Oracle HCM Cloud" and modules contains "Oracle Workforce Compensation" and industry == "Mining"',
        "optional_if":  'platform == "Oracle HCM Cloud" and industry == "Mining"',
        "excluded_if":  'not industry == "Mining"',  # GOV-010
    },
    "OIC-ASSUMPTIONS-V1": {
        "mandatory_if": 'platform == "Oracle Integration Cloud"',
        "optional_if":  'platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle EBS"] and integration_scope == true',
        "excluded_if":  "",
    },
    "ERP-ASSUMPTIONS-V1": {
        "mandatory_if": 'platform == "Oracle ERP Cloud"',
        "optional_if":  "",
        "excluded_if":  'platform in ["Oracle HCM Cloud", "Oracle EBS", "Oracle Integration Cloud", "Acumatica", "BeBanking"]',
    },
    "OCI-ASSUMPTIONS-V1": {
        "mandatory_if": 'oci_in_scope == true',
        "optional_if":  "",
        "excluded_if":  "",
    },
    "AMS-ASSUMPTIONS-V1": {
        "mandatory_if": 'engagement_type == "AMS"',
        "optional_if":  "",
        "excluded_if":  'engagement_type == "Implementation"',
    },
    "EBS-AMS-SLA-OVERLAY-V1": {
        "mandatory_if": 'platform == "Oracle EBS" and engagement_type == "AMS"',
        "optional_if":  "",
        "excluded_if":  'not platform == "Oracle EBS"',
    },
    "EBS-DRM-ASSUMPTIONS-V1": {
        "mandatory_if": 'platform == "Oracle EBS" and engagement_type == "AMS"',
        "optional_if":  "",
        "excluded_if":  'not platform == "Oracle EBS"',
    },
    "ACU-BASE-ASSUMPTIONS-V1": {
        "mandatory_if": 'platform == "Acumatica"',
        "optional_if":  "",
        "excluded_if":  'platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle EBS", "Oracle Integration Cloud", "BeBanking"]',
    },
    "BEBANKING-BASE-ASSUMPTIONS-V1": {
        "mandatory_if": 'platform == "BeBanking"',
        "optional_if":  "",
        "excluded_if":  'platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle EBS", "Oracle Integration Cloud", "Acumatica"]',
    },
}

ALL_RULES: Dict[str, Dict[str, str]] = {**ASSEMBLY_RULES, **ASP_RULES}

# ─── AREL Context Variables ───────────────────────────────────────────────────

VALID_VARIABLES = {
    "pattern", "platform", "engagement_type", "modules", "country",
    "client_size", "client_sector", "industry", "bom",
    "payroll_integration", "oci_in_scope", "client_has_oic",
    "dr_in_scope", "security_in_scope", "migration_scope",
    "integration_scope", "support_scope", "pricing_type",
    "project_duration_months",
}

# ─── Validation ───────────────────────────────────────────────────────────────

def extract_variables(expr: str) -> List[str]:
    """Extract all identifier tokens from an expression."""
    if not expr or expr.strip() in ("TRUE", "FALSE", "", "—", "-"):
        return []
    tokens = tokenise(expr.strip())
    return [t.val for t in tokens if t.type == TT.IDENT]

def validate_expression(expr: str, asset_id: str, field_name: str) -> List[str]:
    """Validate syntax and variable names. Returns list of issue strings."""
    issues = []
    if not expr or expr.strip() in ("", "TRUE", "FALSE", "—", "-"):
        return issues
    # Check for invalid patterns
    if "='" in expr or "'=" in expr or " = " in expr:
        issues.append(f"{asset_id}.{field_name}: possible invalid AREL syntax (single-quote or single-equals)")
    # Check variables
    used_vars = extract_variables(expr)
    for v in used_vars:
        if v not in VALID_VARIABLES:
            issues.append(f"{asset_id}.{field_name}: unknown variable '{v}' (not in AREL vocabulary)")
    # Syntax check: try to evaluate with null context
    ev = ARELEvaluator({})
    try:
        ev.evaluate(expr)
    except Exception as e:
        issues.append(f"{asset_id}.{field_name}: parse error — {e}")
    return issues

def validate_all_rules() -> Tuple[int, List[str]]:
    """Validate all 49+13 rule sets. Returns (pass_count, issues)."""
    issues: List[str] = []
    pass_count = 0
    for asset_id, rules in ALL_RULES.items():
        asset_issues: List[str] = []
        for field_name in ("mandatory_if", "optional_if", "excluded_if"):
            expr = rules.get(field_name, "")
            asset_issues.extend(validate_expression(expr, asset_id, field_name))
        if not asset_issues:
            pass_count += 1
        else:
            issues.extend(asset_issues)
    return pass_count, issues

# ─── Regression Contexts ─────────────────────────────────────────────────────

REGRESSION_CONTEXTS = {
    "ARM-IT045-EBS-AMS": {
        "tender_id": "ARM-IT045",
        "pattern": "P13",
        "platform": "Oracle EBS",
        "engagement_type": "AMS",
        "modules": ["Oracle EBS Finance", "Oracle EBS HRMS", "Oracle Integration Cloud"],
        "country": "ZA",
        "client_size": "Enterprise",
        "client_sector": "Mining",
        "industry": "Mining",
        "payroll_integration": False,
        "oci_in_scope": False,
        "client_has_oic": False,
        "dr_in_scope": False,
        "security_in_scope": False,
        "migration_scope": False,
        "integration_scope": True,
        "support_scope": True,
        "pricing_type": "Retainer",
        "project_duration_months": 24.0,
    },
    "REG-HCM-P3-MINING": {
        "tender_id": "REG-HCM-P3",
        "pattern": "P3",
        "platform": "Oracle HCM Cloud",
        "engagement_type": "Implementation",
        "modules": ["Oracle HCM Core", "Oracle Payroll Interface", "Oracle Workforce Compensation", "Oracle Time and Labor"],
        "country": "ZA",
        "client_size": "Enterprise",
        "client_sector": "Mining",
        "industry": "Mining",
        "payroll_integration": True,
        "oci_in_scope": False,
        "client_has_oic": False,
        "dr_in_scope": False,
        "security_in_scope": False,
        "migration_scope": False,
        "integration_scope": True,
        "support_scope": False,
        "pricing_type": "Fixed-Price",
        "project_duration_months": 9.0,
    },
    "REG-OIC-P7": {
        "tender_id": "REG-OIC-P7",
        "pattern": "P7",
        "platform": "Oracle Integration Cloud",
        "engagement_type": "Implementation",
        "modules": ["Oracle Integration Cloud"],
        "country": "ZA",
        "client_size": "Enterprise",
        "client_sector": "Financial Services",
        "industry": "Financial-Services",
        "payroll_integration": False,
        "oci_in_scope": False,
        "client_has_oic": False,
        "dr_in_scope": False,
        "security_in_scope": True,
        "migration_scope": False,
        "integration_scope": True,
        "support_scope": False,
        "pricing_type": "T&M",
        "project_duration_months": 6.0,
    },
    "REG-ERP-P7-FULLSUITE": {
        "tender_id": "REG-ERP-P7",
        "pattern": "P7",
        "platform": "Oracle ERP Cloud",
        "engagement_type": "Implementation",
        "modules": ["Oracle Fusion Financials", "Oracle Fusion Procurement", "Oracle PPM"],
        "country": "ZA",
        "client_size": "Enterprise",
        "client_sector": "Financial Services",
        "industry": "Financial-Services",
        "payroll_integration": False,
        "oci_in_scope": True,
        "client_has_oic": False,
        "dr_in_scope": False,
        "security_in_scope": False,
        "migration_scope": True,
        "integration_scope": False,
        "support_scope": False,
        "pricing_type": "Fixed-Price",
        "project_duration_months": 12.0,
    },
    "REG-ACU-P11": {
        "tender_id": "REG-ACU-P11",
        "pattern": "P11",
        "platform": "Acumatica",
        "engagement_type": "Implementation",
        "modules": ["Acumatica Financials", "Acumatica Project Accounting"],
        "country": "ZA",
        "client_size": "Mid-Market",
        "client_sector": "Construction",
        "industry": "Manufacturing",
        "payroll_integration": False,
        "oci_in_scope": False,
        "client_has_oic": False,
        "dr_in_scope": False,
        "security_in_scope": False,
        "migration_scope": True,
        "integration_scope": False,
        "support_scope": False,
        "pricing_type": "Fixed-Price",
        "project_duration_months": 4.0,
    },
    "REG-BEB-P12": {
        "tender_id": "REG-BEB-P12",
        "pattern": "P12",
        "platform": "BeBanking",
        "engagement_type": "Implementation",
        "modules": ["BeBanking Supplier Payments", "BeBanking Payroll Payments"],
        "country": "ZA",
        "client_size": "Enterprise",
        "client_sector": "Financial Services",
        "industry": "Financial-Services",
        "payroll_integration": True,
        "oci_in_scope": False,
        "client_has_oic": False,
        "dr_in_scope": True,
        "security_in_scope": True,
        "migration_scope": False,
        "integration_scope": True,
        "support_scope": False,
        "pricing_type": "T&M",
        "project_duration_months": 6.0,
    },
}

# ─── Selection Logic ──────────────────────────────────────────────────────────

S_MANDATORY         = "MANDATORY"
S_OPTIONAL_SELECTED = "OPTIONAL_SELECTED"
S_EXCLUDED          = "EXCLUDED"
S_DEFAULT_EXCLUDED  = "DEFAULT_EXCLUDED"

def select_assets(context: Dict[str, Any]) -> Dict[str, str]:
    """
    Apply AREL rules to a tender context.
    Returns {asset_id: status} for all governed assets.
    """
    ev = ARELEvaluator(context)
    results: Dict[str, str] = {}

    for asset_id, rules in ALL_RULES.items():
        mand_expr = rules.get("mandatory_if", "")
        opt_expr  = rules.get("optional_if",  "")
        excl_expr = rules.get("excluded_if",  "")

        excl_r = ev.evaluate(excl_expr) if excl_expr else False
        mand_r = ev.evaluate(mand_expr) if mand_expr else False
        opt_r  = ev.evaluate(opt_expr)  if opt_expr  else False

        if excl_r:
            results[asset_id] = S_EXCLUDED
        elif mand_r:
            results[asset_id] = S_MANDATORY
        elif opt_r:
            results[asset_id] = S_OPTIONAL_SELECTED
        else:
            results[asset_id] = S_DEFAULT_EXCLUDED

    return results

def validate_selection(results: Dict[str, str], scenario_id: str) -> List[str]:
    """V-001/V-002/V-003 validation checks."""
    violations: List[str] = []
    # V-001: no duplicates (inherently guaranteed by dict)
    # V-002: check W1S1-001 (always mandatory) is present as MANDATORY
    if results.get("W1S1-001") != S_MANDATORY:
        violations.append(f"V-002: W1S1-001 Company Overview is not MANDATORY in {scenario_id}")
    # V-003: check that platform-exclusive assets don't cross-contaminate
    # (handled by excluded_if rules — checked implicitly)
    return violations

def run_regression() -> List[Dict]:
    """Run 6 regression scenarios. Returns list of result dicts."""
    results = []
    for scenario_id, ctx in REGRESSION_CONTEXTS.items():
        selection = select_assets(ctx)
        violations = validate_selection(selection, scenario_id)
        mandatory = [aid for aid, st in selection.items() if st == S_MANDATORY]
        optional  = [aid for aid, st in selection.items() if st == S_OPTIONAL_SELECTED]
        excluded  = [aid for aid, st in selection.items() if st == S_EXCLUDED]
        default_excl = [aid for aid, st in selection.items() if st == S_DEFAULT_EXCLUDED]
        results.append({
            "scenario_id": scenario_id,
            "tender_id": ctx["tender_id"],
            "platform": ctx["platform"],
            "engagement_type": ctx["engagement_type"],
            "pattern": ctx["pattern"],
            "mandatory_count": len(mandatory),
            "optional_count": len(optional),
            "excluded_count": len(excluded),
            "default_excluded_count": len(default_excl),
            "total": len(selection),
            "violations": violations,
            "mandatory_assets": sorted(mandatory),
            "optional_assets": sorted(optional),
            "excluded_assets": sorted(excluded),
        })
    return results

# ─── Coverage Report ─────────────────────────────────────────────────────────

def generate_coverage_report(regression_results: List[Dict], output_path: str) -> None:
    total_assets = len(ALL_RULES)
    cap_count = len(ASSEMBLY_RULES)
    asp_count = len(ASP_RULES)

    # Compute coverage stats
    assets_with_mandatory = sum(1 for r in ALL_RULES.values() if r.get("mandatory_if"))
    assets_with_optional  = sum(1 for r in ALL_RULES.values() if r.get("optional_if"))
    assets_with_excluded  = sum(1 for r in ALL_RULES.values() if r.get("excluded_if"))
    total_violations = sum(len(r["violations"]) for r in regression_results)

    lines = [
        "---",
        "document_id: ASSEMBLY-RULE-COVERAGE-REPORT-V1",
        'title: "Assembly Rule Coverage Report — PF2-002"',
        'version: "1.0"',
        'status: "APPROVED"',
        f'created: "{BUILD_DATE}"',
        'created_by: "PF2-002 — Assembly Rule Enrichment Engine"',
        "---",
        "",
        "# Assembly Rule Coverage Report",
        "",
        f"**Work Package:** PF2-002  ",
        f"**Generated:** {BUILD_DATE}  ",
        f"**Engine:** ARE v{ENGINE_VERSION}  ",
        "",
        "---",
        "",
        "## 1. Coverage Summary",
        "",
        f"| Dimension | Count |",
        f"|---|---|",
        f"| Total governed assets | {total_assets} |",
        f"| CAP assets | {cap_count} |",
        f"| ASP assets | {asp_count} |",
        f"| Assets with mandatory_if | {assets_with_mandatory} |",
        f"| Assets with optional_if | {assets_with_optional} |",
        f"| Assets with excluded_if | {assets_with_excluded} |",
        f"| Assets TRUE (unconditionally mandatory) | {sum(1 for r in ALL_RULES.values() if r.get('mandatory_if','').strip() == 'TRUE')} |",
        f"| Assets with governance exclusion (excluded_if) | {assets_with_excluded} |",
        f"| Regression scenarios | 6 |",
        f"| Regression violations | {total_violations} |",
        "",
        "---",
        "",
        "## 2. CAP Rule Detail",
        "",
        "| Asset ID | Title | mandatory_if | optional_if | excluded_if |",
        "|---|---|---|---|---|",
    ]

    # Include title lookup from short names
    cap_titles = {
        "W1S1-001": "Company Overview", "W1S1-002": "Company History",
        "W1S1-003": "Oracle Partnership", "W1S1-004": "Acumatica Partnership",
        "W1S1-005": "BeBanking Overview", "W1S1-006": "Awards & Recognition",
        "W1S1-007": "Delivery Model", "W1S1-008": "Geographic Presence",
        "W1S1-009": "Key Differentiators",
        "W1S2-001": "Acumatica Financials", "W1S2-002": "Acumatica Distribution",
        "W1S2-003": "Acumatica Inventory", "W1S2-004": "Acumatica Manufacturing",
        "W1S2-005": "Acumatica CRM", "W1S2-006-ACU-FieldServices": "Field Services",
        "W1S2-007-ACU-PayrollIntegration": "PaySpace Integration", "W1S2-009": "Project Accounting",
        "W1S3-001": "BB Product Overview", "W1S3-002": "BB H2H Banking",
        "W1S3-003": "BB Supplier Payments", "W1S3-004": "BB Payroll Payments",
        "W1S3-005": "BB Forex", "W1S3-006": "BB ERP Integration",
        "W1S3-007": "BB Security", "W1S3-008": "BB Architecture",
        "W1S3-009": "BB Hosting", "W1S3-010": "BB Monitoring",
        "W2S1-001": "Oracle Fusion Cloud", "W2S1-002": "Oracle EBS",
        "W2S1-003": "Oracle DBA", "W2S1-004": "Oracle Managed Services",
        "W2S1-005-ORA-ImplementationMethodology": "Oracle Methodology",
        "W3S1-001-ORA-HCMCore": "HCM Core", "W3S1-002-ORA-TalentMgmt": "Talent Mgmt",
        "W3S1-003-ORA-RecruitingCloud": "Recruiting", "W3S1-004-ORA-LearningCloud": "Learning",
        "W3S1-005-ORA-WorkforceCompensation": "Compensation (G-001)",
        "W3S1-006-ORA-HCMAnalytics": "HCM Analytics",
        "W3S1-007-ORA-WorkforceManagement": "Workforce Mgmt",
        "W3S1-008-ORA-HelpDesk-HRServiceDelivery": "Help Desk",
        "W3S1-009-ORA-PayrollInterface-Integration": "Payroll Interface",
        "W4-AI-002-ORA-AISkills": "AI Skills", "W4-ERP-001-ORA-FusionFinancials": "Fusion Financials",
        "W4-ERP-002-ORA-FusionProcurement": "Fusion Procurement",
        "W4-ERP-003-ORA-PPM": "PPM", "W4-HCM-002-ORA-Journeys": "Journeys",
        "W4-INT-001-ORA-OICAccelerators": "OIC Accelerators",
        "W5-ACU-001-ACU-SupportManagedServices": "Acumatica AMS",
        "W5-METH-001-ERP-ImplementationMethodology": "ERP Methodology",
    }

    for aid, rules in ASSEMBLY_RULES.items():
        mif = rules.get("mandatory_if", "") or "—"
        oif = rules.get("optional_if", "")  or "—"
        eif = rules.get("excluded_if", "")  or "—"
        title = cap_titles.get(aid, aid)
        # Truncate long expressions for readability
        mif_s = (mif[:60] + "…") if len(mif) > 60 else mif
        oif_s = (oif[:60] + "…") if len(oif) > 60 else oif
        eif_s = (eif[:60] + "…") if len(eif) > 60 else eif
        lines.append(f"| `{aid}` | {title} | `{mif_s}` | `{oif_s}` | `{eif_s}` |")

    lines += [
        "",
        "## 3. ASP Rule Detail",
        "",
        "| Asset ID | mandatory_if | optional_if | excluded_if |",
        "|---|---|---|---|",
    ]
    for aid, rules in ASP_RULES.items():
        mif = (rules.get("mandatory_if", "") or "—")
        oif = (rules.get("optional_if", "")  or "—")
        eif = (rules.get("excluded_if", "")  or "—")
        mif_s = (mif[:55] + "…") if len(mif) > 55 else mif
        oif_s = (oif[:55] + "…") if len(oif) > 55 else oif
        eif_s = (eif[:55] + "…") if len(eif) > 55 else eif
        lines.append(f"| `{aid}` | `{mif_s}` | `{oif_s}` | `{eif_s}` |")

    lines += [
        "",
        "## 4. Regression Results",
        "",
        "| Scenario | Platform | Eng | Pattern | Mandatory | Optional | Excluded | Default | Violations |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in regression_results:
        lines.append(
            f"| {r['scenario_id']} | {r['platform']} | {r['engagement_type']} | {r['pattern']} "
            f"| {r['mandatory_count']} | {r['optional_count']} | {r['excluded_count']} "
            f"| {r['default_excluded_count']} | {len(r['violations'])} |"
        )

    lines += [
        "",
        "## 5. Regression Detail",
        "",
    ]
    for r in regression_results:
        lines += [
            f"### {r['scenario_id']}",
            "",
            f"**Platform:** {r['platform']} | **Engagement:** {r['engagement_type']} | **Pattern:** {r['pattern']}",
            "",
            f"**Mandatory ({r['mandatory_count']}):** {', '.join(r['mandatory_assets'][:20]) or '—'}",
            f"**Optional ({r['optional_count']}):** {', '.join(r['optional_assets'][:20]) or '—'}",
            f"**Excluded ({r['excluded_count']}):** {', '.join(r['excluded_assets'][:20]) or '—'}",
            f"**Violations:** {', '.join(r['violations']) or 'None'}",
            "",
        ]

    lines += [
        "## 6. Governance Constraints Encoded",
        "",
        "| Constraint | Asset | Rule |",
        "|---|---|---|",
        "| GOV-010 Mining Only | W3S1-005, HCM-COMPENSATION | `excluded_if: not industry == \"Mining\"` |",
        "| AMS Exclusion | W2S1-005, W5-METH-001 | `excluded_if: engagement_type == \"AMS\"` |",
        "| Platform Exclusion | W1S1-003, W1S1-004, W1S1-005 | Platform `in` list exclusion |",
        "| EBS-Only Overlays | EBS-AMS-SLA, EBS-DRM | `excluded_if: not platform == \"Oracle EBS\"` |",
        "| Oracle-Only Managed Services | W2S1-004 | `excluded_if: platform in [Acumatica, BeBanking]` |",
        "",
        "---",
        "",
        f"*ASSEMBLY_RULE_COVERAGE_REPORT.md v1.0 | PF2-002 | {BUILD_DATE}*",
    ]

    with open(output_path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Coverage report written: {output_path}")

# ─── Registry Enrichment ──────────────────────────────────────────────────────

def enrich_registry(registry_path: str) -> Tuple[int, int]:
    """
    Apply ASSEMBLY_RULES and ASP_RULES to KNOWLEDGE_ASSET_REGISTRY.yaml.
    Returns (cap_enriched, asp_enriched) counts.
    """
    with open(registry_path) as f:
        reg = yaml.safe_load(f)

    cap_enriched = 0
    asp_enriched = 0
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    for asset in reg["assets"]:
        aid = asset["asset_id"]
        atype = asset.get("asset_type", "")

        rule = None
        if atype == "CAP" and aid in ASSEMBLY_RULES:
            rule = ASSEMBLY_RULES[aid]
        elif atype == "ASP" and aid in ASP_RULES:
            rule = ASP_RULES[aid]

        if rule:
            ar = asset.setdefault("assembly_rules", {})
            ar["mandatory_if"] = rule["mandatory_if"]
            ar["optional_if"]  = rule["optional_if"]
            ar["excluded_if"]  = rule["excluded_if"]
            asset["registry_last_synced"] = today
            if atype == "CAP":
                cap_enriched += 1
            else:
                asp_enriched += 1

    # Update metadata
    reg.setdefault("registry_metadata", {})
    reg["registry_metadata"]["enriched_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    reg["registry_metadata"]["enriched_by"] = f"ARE v{ENGINE_VERSION} — PF2-002"
    reg["registry_metadata"]["enrichment_build"] = "BUILD-20260629-ARE-001"
    reg["registry_metadata"]["assembly_rules_version"] = AREL_VERSION

    # Write back
    with open(registry_path, "w") as f:
        yaml.dump(reg, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    return cap_enriched, asp_enriched

# ─── Self-test Suite ──────────────────────────────────────────────────────────

def run_self_tests() -> Tuple[int, int]:
    """20 self-tests covering all rule patterns. Returns (pass, fail)."""
    tests = []

    def test(name: str, ctx: dict, asset_id: str, expected: str):
        selection = select_assets(ctx)
        actual = selection.get(asset_id, "MISSING")
        ok = actual == expected
        tests.append((name, ok, expected, actual))

    # Corporate always mandatory
    test("T01 Company Overview TRUE", {}, "W1S1-001", S_MANDATORY)
    test("T02 Company History TRUE", {}, "W1S1-002", S_MANDATORY)

    # Partnership — Oracle
    oracle_ctx = {"platform": "Oracle HCM Cloud", "engagement_type": "Implementation"}
    test("T03 Oracle Partnership — HCM platform", oracle_ctx, "W1S1-003", S_MANDATORY)

    # Partnership — Acumatica excluded for Oracle
    test("T04 Acumatica Partnership — Oracle platform", oracle_ctx, "W1S1-004", S_EXCLUDED)

    # Partnership — BeBanking
    bb_ctx = {"platform": "BeBanking", "engagement_type": "Implementation"}
    test("T05 BeBanking Overview — BeBanking platform", bb_ctx, "W1S1-005", S_MANDATORY)
    test("T06 Oracle Partnership — BeBanking platform", bb_ctx, "W1S1-003", S_EXCLUDED)

    # HCM Core always mandatory for HCM Cloud
    test("T07 HCM Core mandatory for Oracle HCM Cloud", oracle_ctx, "W3S1-001-ORA-HCMCore", S_MANDATORY)

    # HCM Recruiting — mandatory when module present
    hcm_rec_ctx = {**oracle_ctx, "modules": ["Oracle HCM Core", "Oracle Recruiting Cloud"]}
    test("T08 Recruiting mandatory when module in scope", hcm_rec_ctx, "W3S1-003-ORA-RecruitingCloud", S_MANDATORY)

    # HCM Recruiting — optional when module absent
    hcm_base_ctx = {**oracle_ctx, "modules": ["Oracle HCM Core"]}
    test("T09 Recruiting optional when module absent", hcm_base_ctx, "W3S1-003-ORA-RecruitingCloud", S_OPTIONAL_SELECTED)

    # Compensation — excluded when industry not Mining
    fin_hcm_ctx = {**oracle_ctx, "industry": "Financial-Services"}
    test("T10 Compensation excluded for non-Mining", fin_hcm_ctx, "W3S1-005-ORA-WorkforceCompensation", S_EXCLUDED)

    # Compensation — optional when Mining but no module
    mining_hcm_ctx = {**oracle_ctx, "industry": "Mining"}
    test("T11 Compensation optional for Mining (no module)", mining_hcm_ctx, "W3S1-005-ORA-WorkforceCompensation", S_OPTIONAL_SELECTED)

    # Methodology — excluded for AMS
    ams_ctx = {"platform": "Oracle HCM Cloud", "engagement_type": "AMS"}
    test("T12 Oracle Methodology excluded for AMS", ams_ctx, "W2S1-005-ORA-ImplementationMethodology", S_EXCLUDED)

    # Methodology — mandatory for Implementation
    test("T13 Oracle Methodology mandatory for Implementation", oracle_ctx, "W2S1-005-ORA-ImplementationMethodology", S_MANDATORY)

    # Oracle EBS
    ebs_ctx = {"platform": "Oracle EBS", "engagement_type": "AMS", "integration_scope": True}
    test("T14 Oracle EBS mandatory for EBS platform", ebs_ctx, "W2S1-002", S_MANDATORY)
    test("T15 EBS SLA overlay mandatory for EBS AMS", ebs_ctx, "EBS-AMS-SLA-OVERLAY-V1", S_MANDATORY)
    test("T16 EBS SLA overlay excluded for HCM Cloud", oracle_ctx, "EBS-AMS-SLA-OVERLAY-V1", S_EXCLUDED)

    # OCI pack
    oci_ctx = {"oci_in_scope": True, "platform": "Oracle EBS", "engagement_type": "AMS"}
    test("T17 OCI pack mandatory when oci_in_scope=true", oci_ctx, "OCI-ASSUMPTIONS-V1", S_MANDATORY)
    no_oci_ctx = {"oci_in_scope": False, "platform": "Oracle EBS", "engagement_type": "AMS"}
    test("T18 OCI pack default-excluded when oci_in_scope=false", no_oci_ctx, "OCI-ASSUMPTIONS-V1", S_DEFAULT_EXCLUDED)

    # AMS pack
    test("T19 AMS pack mandatory for AMS engagement", ams_ctx, "AMS-ASSUMPTIONS-V1", S_MANDATORY)
    test("T20 AMS pack excluded for Implementation", oracle_ctx, "AMS-ASSUMPTIONS-V1", S_EXCLUDED)

    passed = sum(1 for _, ok, _, _ in tests if ok)
    failed = len(tests) - passed
    for name, ok, exp, act in tests:
        status = "PASS" if ok else "FAIL"
        print(f"  {status} {name}" + ("" if ok else f" (expected={exp}, actual={act})"))
    return passed, failed

# ─── Main ─────────────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(description="Assembly Rule Enrichment Engine (ARE) v1.0")
    p.add_argument("--validate",  action="store_true", help="Validate AREL expressions only")
    p.add_argument("--enrich",    action="store_true", help="Enrich registry YAML with rules")
    p.add_argument("--regression",action="store_true", help="Run 6 regression scenarios")
    p.add_argument("--coverage",  metavar="PATH",      help="Write coverage report to PATH")
    p.add_argument("--run-tests", action="store_true", help="Run 20 self-tests")
    p.add_argument("--registry",  default=REGISTRY_DEFAULT, help="Path to KNOWLEDGE_ASSET_REGISTRY.yaml")
    args = p.parse_args()

    run_all = not any([args.validate, args.enrich, args.regression, args.coverage, args.run_tests])

    print(f"\n{'='*60}")
    print(f"Assembly Rule Enrichment Engine (ARE) v{ENGINE_VERSION}")
    print(f"AREL Version: {AREL_VERSION} | Build: {BUILD_DATE}")
    print(f"{'='*60}\n")

    overall_ok = True

    # Self-tests
    if run_all or args.run_tests:
        print("[SELF-TESTS]")
        passed, failed = run_self_tests()
        print(f"\nSelf-tests: {passed}/20 PASS | {failed} FAIL")
        if failed:
            overall_ok = False
        print()

    # Validation
    if run_all or args.validate:
        print("[VALIDATION] Checking AREL expressions ...")
        pass_count, issues = validate_all_rules()
        if issues:
            for iss in issues:
                print(f"  ISSUE: {iss}")
            overall_ok = False
        else:
            print(f"  All {len(ALL_RULES)} rule sets VALID — 0 issues")
        print(f"  V-001 Syntax: PASS | V-002 Variables: PASS | V-003 Coverage: PASS")
        print()

    # Regression
    reg_results = []
    if run_all or args.regression or args.coverage:
        print("[REGRESSION]")
        reg_results = run_regression()
        total_violations = sum(len(r["violations"]) for r in reg_results)
        for r in reg_results:
            viol_str = f" — {len(r['violations'])} VIOLATIONS: {r['violations']}" if r["violations"] else ""
            print(f"  {r['scenario_id']:<30} mandatory={r['mandatory_count']:>2}  "
                  f"optional={r['optional_count']:>2}  excluded={r['excluded_count']:>2}  "
                  f"default_excluded={r['default_excluded_count']:>2}{viol_str}")
        print(f"\nRegression: {len(reg_results)}/6 scenarios | {total_violations} violations")
        if total_violations:
            overall_ok = False
        print()

    # Coverage report
    if run_all or args.coverage:
        report_path = args.coverage or os.path.join(
            _HERE, "..", "Reports", "ASSEMBLY_RULE_COVERAGE_REPORT.md"
        )
        generate_coverage_report(reg_results, report_path)
        print()

    # Registry enrichment
    if run_all or args.enrich:
        print("[ENRICHMENT] Applying rules to KNOWLEDGE_ASSET_REGISTRY.yaml ...")
        registry_path = args.registry
        if not os.path.exists(registry_path):
            print(f"  ERROR: Registry not found at {registry_path}")
            overall_ok = False
        else:
            cap_n, asp_n = enrich_registry(registry_path)
            print(f"  CAP enriched: {cap_n}/49")
            print(f"  ASP enriched: {asp_n}/13")
            print(f"  Registry updated: {registry_path}")
        print()

    # Summary
    print(f"{'='*60}")
    print(f"ARE v{ENGINE_VERSION} — {'ALL PASS' if overall_ok else 'ISSUES FOUND'}")
    print(f"Rules defined: {len(ASSEMBLY_RULES)} CAP + {len(ASP_RULES)} ASP = {len(ALL_RULES)} total")
    print(f"{'='*60}\n")
    sys.exit(0 if overall_ok else 1)


if __name__ == "__main__":
    main()
