---
document_id: ASSEMBLY-RULE-TEST-SUITE-V1
title: "Assembly Rule Expression Language — Test Suite V1.0"
version: "1.0"
status: "FROZEN"
created: "2026-06-28"
created_by: "WP19B — Assembly Rule Expression Language Specification"
approved_by: "Architecture — WP19B"
approved_date: "2026-06-28"
approved_for_reuse: true
category: "Assembly Engine / Expression Language"
scope: "Defines the canonical test suite for AREL evaluator implementations. Every test case specifies an expression, a context, and the expected boolean result. An evaluator implementation is compliant if and only if it produces the correct result for all 80 test cases without exceptions."
governing_standard: "ASSEMBLY_RULE_EXPRESSION_LANGUAGE.md V1.0"
related_documents:
  - ASSEMBLY_RULE_EXPRESSION_LANGUAGE.md
  - ASSEMBLY_RULE_VALIDATION_STANDARD.md
---

# Assembly Rule Expression Language — Test Suite V1.0

**Work Package:** WP19B  
**Status:** FROZEN  
**Total test cases:** 80  
**Required pass rate for compliance:** 80/80 (100%)

---

## 1. Purpose

This test suite defines the canonical compliance tests for any implementation of the AREL evaluator. An implementation is certified as AREL V1.0 compliant only when it passes all 80 test cases.

Test cases are grouped by construct. Each test specifies:
- **ID** — unique test identifier
- **Expression** — the AREL string to evaluate
- **Context** — the variable bindings (partial context; unlisted variables are absent/null)
- **Expected** — the boolean result the evaluator must return

---

## 2. Reference Context

The following full reference context is used unless a test overrides specific variables:

```yaml
pattern: "P1"
platform: "Oracle HCM Cloud"
engagement_type: "Implementation"
modules:
  - "Oracle HCM Core"
  - "Oracle Recruiting Cloud"
  - "Oracle Learning Cloud"
country: "ZA"
client_size: "Enterprise"
client_sector: "Government"
industry: "Mining"
bom:
  - "BOM-1"
  - "BOM-3"
payroll_integration: false
oci_in_scope: false
client_has_oic: false
dr_in_scope: false
security_in_scope: false
migration_scope: true
integration_scope: false
support_scope: false
pricing_type: "Fixed-Price"
project_duration_months: 18
```

Tests marked **[OVERRIDE]** specify which variables differ from this reference.

---

## 3. Section A — Empty and Unconditional Forms (TC-A-001 to TC-A-005)

| ID | Expression | Context | Expected | Notes |
|---|---|---|---|---|
| TC-A-001 | `""` | reference | `false` | Empty expression always false |
| TC-A-002 | `"   "` | reference | `false` | Whitespace-only always false |
| TC-A-003 | `TRUE` | reference | `true` | Unconditional include |
| TC-A-004 | `FALSE` | reference | `false` | Unconditional exclude |
| TC-A-005 | `true` | reference | `true` | Boolean literal true |

---

## 4. Section B — Simple Equality (TC-B-001 to TC-B-012)

| ID | Expression | Context Override | Expected | Notes |
|---|---|---|---|---|
| TC-B-001 | `platform == "Oracle HCM Cloud"` | — | `true` | Exact match |
| TC-B-002 | `platform == "Acumatica"` | — | `false` | No match |
| TC-B-003 | `platform == "oracle hcm cloud"` | — | `false` | Case-sensitive; lowercase fails |
| TC-B-004 | `engagement_type == "AMS"` | `engagement_type: "AMS"` | `true` | Match |
| TC-B-005 | `engagement_type == "AMS"` | — | `false` | Reference context has "Implementation" |
| TC-B-006 | `pattern == "P1"` | — | `true` | Exact match |
| TC-B-007 | `pattern == "P13"` | — | `false` | No match |
| TC-B-008 | `country == "ZA"` | — | `true` | Exact match |
| TC-B-009 | `country == "RSA"` | `country: "RSA"` | `true` | RSA as-given matches RSA literal |
| TC-B-010 | `client_size == "Enterprise"` | — | `true` | Match |
| TC-B-011 | `pricing_type == "Fixed-Price"` | — | `true` | Hyphenated string match |
| TC-B-012 | `pricing_type == "T&M"` | — | `false` | No match |

---

## 5. Section C — Inequality (TC-C-001 to TC-C-006)

| ID | Expression | Context Override | Expected | Notes |
|---|---|---|---|---|
| TC-C-001 | `platform != "BeBanking"` | — | `true` | Not equal — different platform |
| TC-C-002 | `platform != "Oracle HCM Cloud"` | — | `false` | Not equal — same value, returns false |
| TC-C-003 | `engagement_type != "AMS"` | — | `true` | Reference context is "Implementation" |
| TC-C-004 | `engagement_type != "AMS"` | `engagement_type: "AMS"` | `false` | Same value, not-equal is false |
| TC-C-005 | `country != "NG"` | — | `true` | Different country |
| TC-C-006 | `industry != "Other"` | `industry: null` | `false` | Null variable — any op returns false |

---

## 6. Section D — Numeric Comparison (TC-D-001 to TC-D-008)

| ID | Expression | Context Override | Expected | Notes |
|---|---|---|---|---|
| TC-D-001 | `project_duration_months > 12` | — | `true` | 18 > 12 |
| TC-D-002 | `project_duration_months > 18` | — | `false` | 18 > 18 is false |
| TC-D-003 | `project_duration_months >= 18` | — | `true` | 18 >= 18 |
| TC-D-004 | `project_duration_months < 24` | — | `true` | 18 < 24 |
| TC-D-005 | `project_duration_months <= 18` | — | `true` | 18 <= 18 |
| TC-D-006 | `project_duration_months < 12` | — | `false` | 18 < 12 is false |
| TC-D-007 | `project_duration_months > 12` | `project_duration_months: null` | `false` | Null → false |
| TC-D-008 | `project_duration_months >= 0` | — | `true` | 18 >= 0 |

---

## 7. Section E — Membership: `in` and `not in` (TC-E-001 to TC-E-012)

| ID | Expression | Context Override | Expected | Notes |
|---|---|---|---|---|
| TC-E-001 | `platform in ["Oracle HCM Cloud", "Oracle ERP Cloud"]` | — | `true` | Member |
| TC-E-002 | `platform in ["Acumatica", "BeBanking"]` | — | `false` | Not a member |
| TC-E-003 | `platform in ["Oracle HCM Cloud"]` | — | `true` | Single-element list, member |
| TC-E-004 | `platform in []` | — | `false` | Empty list — always false |
| TC-E-005 | `industry in ["Mining", "Manufacturing"]` | — | `true` | Mining is a member |
| TC-E-006 | `industry in ["Financial-Services", "Retail"]` | — | `false` | Mining not in list |
| TC-E-007 | `pattern in ["P1", "P2", "P3", "P7"]` | — | `true` | P1 is in list |
| TC-E-008 | `pattern in ["P4", "P5", "P6"]` | — | `false` | P1 not in list |
| TC-E-009 | `engagement_type not in ["AMS", "Managed Services"]` | — | `true` | "Implementation" not in list |
| TC-E-010 | `engagement_type not in ["AMS", "Managed Services"]` | `engagement_type: "AMS"` | `false` | "AMS" is in list, so not-in = false |
| TC-E-011 | `platform in ["Oracle HCM Cloud"]` | `platform: null` | `false` | Null → false |
| TC-E-012 | `country in ["ZA", "NG", "GH", "UG"]` | — | `true` | "ZA" is a member |

---

## 8. Section F — `contains` Operator (TC-F-001 to TC-F-010)

| ID | Expression | Context Override | Expected | Notes |
|---|---|---|---|---|
| TC-F-001 | `modules contains "Oracle Recruiting Cloud"` | — | `true` | In reference context modules list |
| TC-F-002 | `modules contains "Oracle Workforce Compensation"` | — | `false` | Not in reference context modules list |
| TC-F-003 | `modules contains "Oracle HCM Core"` | — | `true` | First element |
| TC-F-004 | `modules contains "Oracle Learning Cloud"` | — | `true` | Last element |
| TC-F-005 | `modules contains "oracle hcm core"` | — | `false` | Case-sensitive; lowercase fails |
| TC-F-006 | `bom contains "BOM-1"` | — | `true` | BOM-1 in reference bom list |
| TC-F-007 | `bom contains "BOM-6"` | — | `false` | BOM-6 not in reference bom list |
| TC-F-008 | `modules contains "Oracle Recruiting Cloud"` | `modules: null` | `false` | Null list → false |
| TC-F-009 | `modules contains "Oracle Recruiting Cloud"` | `modules: []` | `false` | Empty list → false |
| TC-F-010 | `bom contains "BOM-6"` | `bom: ["BOM-6", "BOM-1"]` | `true` | Custom bom context |

---

## 9. Section G — Boolean Variables (TC-G-001 to TC-G-008)

| ID | Expression | Context Override | Expected | Notes |
|---|---|---|---|---|
| TC-G-001 | `payroll_integration == true` | — | `false` | Reference context: false |
| TC-G-002 | `payroll_integration == true` | `payroll_integration: true` | `true` | True override |
| TC-G-003 | `payroll_integration == false` | — | `true` | False == false |
| TC-G-004 | `oci_in_scope == true` | — | `false` | Reference: false |
| TC-G-005 | `oci_in_scope == true` | `oci_in_scope: true` | `true` | Override |
| TC-G-006 | `migration_scope == true` | — | `true` | Reference: true |
| TC-G-007 | `client_has_oic == true` | `client_has_oic: true` | `true` | Override |
| TC-G-008 | `payroll_integration == true` | `payroll_integration: null` | `false` | Null → false |

---

## 10. Section H — Logical: `and`, `or`, `not` (TC-H-001 to TC-H-015)

| ID | Expression | Context Override | Expected | Notes |
|---|---|---|---|---|
| TC-H-001 | `platform == "Oracle HCM Cloud" and engagement_type == "Implementation"` | — | `true` | Both true |
| TC-H-002 | `platform == "Oracle HCM Cloud" and engagement_type == "AMS"` | — | `false` | Second is false |
| TC-H-003 | `platform == "Acumatica" and engagement_type == "Implementation"` | — | `false` | First is false |
| TC-H-004 | `platform == "Oracle HCM Cloud" or platform == "Oracle ERP Cloud"` | — | `true` | First is true |
| TC-H-005 | `platform == "Acumatica" or platform == "BeBanking"` | — | `false` | Both false |
| TC-H-006 | `not engagement_type == "AMS"` | — | `true` | Not false = true |
| TC-H-007 | `not engagement_type == "Implementation"` | — | `false` | Not true = false |
| TC-H-008 | `not (platform == "Acumatica" or platform == "BeBanking")` | — | `true` | Not (false or false) = true |
| TC-H-009 | `platform == "Oracle HCM Cloud" and engagement_type == "Implementation" and country == "ZA"` | — | `true` | All three true |
| TC-H-010 | `platform == "Oracle HCM Cloud" or platform == "Oracle ERP Cloud" or platform == "Oracle EBS"` | — | `true` | First true, short-circuit |
| TC-H-011 | `not not platform == "Oracle HCM Cloud"` | — | `true` | Double negation |
| TC-H-012 | `industry == "Mining" and modules contains "Oracle Workforce Compensation"` | — | `false` | Industry true; modules false |
| TC-H-013 | `industry == "Mining" and modules contains "Oracle Workforce Compensation"` | `modules: ["Oracle HCM Core", "Oracle Workforce Compensation"]` | `true` | Both true |
| TC-H-014 | `engagement_type == "AMS" or support_scope == true` | — | `false` | Both false |
| TC-H-015 | `engagement_type == "AMS" or support_scope == true` | `support_scope: true` | `true` | Second true |

---

## 11. Section I — Operator Precedence (TC-I-001 to TC-I-008)

| ID | Expression | Context Override | Expected | Notes |
|---|---|---|---|---|
| TC-I-001 | `platform == "Oracle HCM Cloud" or platform == "Oracle ERP Cloud" and engagement_type == "AMS"` | — | `true` | `and` binds tighter: `HCM` or `(ERP and AMS)` → `true or false` = `true` |
| TC-I-002 | `(platform == "Oracle HCM Cloud" or platform == "Oracle ERP Cloud") and engagement_type == "AMS"` | — | `false` | Parentheses change precedence: `(HCM or ERP) and AMS` → `true and false` = `false` |
| TC-I-003 | `not platform == "Acumatica" and engagement_type == "Implementation"` | — | `true` | `not` binds tightest: `(not Acumatica) and Implementation` → `true and true` |
| TC-I-004 | `not (platform == "Acumatica" and engagement_type == "Implementation")` | — | `true` | Parentheses: `not (false and true)` = `not false` = `true` |
| TC-I-005 | `platform == "Acumatica" or platform == "BeBanking" and engagement_type == "Implementation"` | — | `false` | `(Acumatica) or (BeBanking and Implementation)` → `false or false` = `false` |
| TC-I-006 | `not platform == "Oracle HCM Cloud" or engagement_type == "AMS"` | — | `false` | `(not HCM) or AMS` → `false or false` = `false` |
| TC-I-007 | `platform in ["Oracle HCM Cloud", "Oracle ERP Cloud"] and engagement_type == "Implementation"` | — | `true` | Comparison then and |
| TC-I-008 | `country == "ZA" and modules contains "Oracle Recruiting Cloud" or payroll_integration == true` | — | `true` | `(ZA and Recruiting) or payroll_integration` → `(true and true) or false` = `true` |

---

## 12. Section J — Null / Undefined Variables (TC-J-001 to TC-J-008)

| ID | Expression | Context Override | Expected | Notes |
|---|---|---|---|---|
| TC-J-001 | `industry == "Mining"` | `industry: null` | `false` | Null → false for == |
| TC-J-002 | `industry != "Mining"` | `industry: null` | `false` | Null → false for != |
| TC-J-003 | `industry in ["Mining", "Manufacturing"]` | `industry: null` | `false` | Null → false for in |
| TC-J-004 | `industry not in ["Other"]` | `industry: null` | `false` | Null → false for not in |
| TC-J-005 | `modules contains "Oracle Recruiting Cloud"` | `modules: null` | `false` | Null list → false for contains |
| TC-J-006 | `project_duration_months > 12` | `project_duration_months: null` | `false` | Null → false for > |
| TC-J-007 | `undefined_variable == "test"` | — | `false` | Variable not in context |
| TC-J-008 | `industry == "Mining" or undefined_variable == "test"` | `industry: "Mining"` | `true` | First clause true; null clause false; or = true |

---

## 13. Section K — Complex Real-World Expressions (TC-K-001 to TC-K-012)

These test cases reflect the actual assembly rules anticipated for Phase B rule population.

| ID | Expression | Context Override | Expected | Notes |
|---|---|---|---|---|
| TC-K-001 | `platform == "Oracle HCM Cloud" and engagement_type == "Implementation"` | — | `true` | W3S1-001 mandatory_if |
| TC-K-002 | `platform in ["Oracle HCM Cloud", "Oracle ERP Cloud"] and engagement_type == "Implementation"` | — | `true` | Methodology mandatory_if (W2S1-005) |
| TC-K-003 | `industry == "Mining" and modules contains "Oracle Workforce Compensation"` | `modules: ["Oracle Workforce Compensation"]` | `true` | W3S1-005 G-001 guard |
| TC-K-004 | `industry == "Mining" and modules contains "Oracle Workforce Compensation"` | `industry: "Financial-Services"` | `false` | G-001: non-Mining excluded |
| TC-K-005 | `engagement_type == "AMS"` | — | `false` | AMS sections excluded from Implementation |
| TC-K-006 | `engagement_type == "AMS"` | `engagement_type: "AMS"` | `true` | AMS trigger |
| TC-K-007 | `platform not in ["Acumatica", "BeBanking"] and pattern != "P10"` | — | `true` | RC-OPS-001 scope (non-P10, non-niche platform) |
| TC-K-008 | `platform not in ["Acumatica", "BeBanking"] and pattern != "P10"` | `pattern: "P10"` | `false` | P10 excluded |
| TC-K-009 | `modules contains "Oracle Recruiting Cloud" and engagement_type == "Implementation"` | — | `true` | W3S1-003 conditional |
| TC-K-010 | `payroll_integration == true and platform == "Oracle HCM Cloud"` | `payroll_integration: true` | `true` | W3S1-009 conditional |
| TC-K-011 | `oci_in_scope == true` | — | `false` | OCI assumption pack not triggered |
| TC-K-012 | `(platform == "Oracle HCM Cloud" or platform == "Oracle ERP Cloud") and engagement_type == "Implementation" and country == "ZA"` | — | `true` | ZA-specific Implementation asset |

---

## 14. Section L — Edge Cases (TC-L-001 to TC-L-011)

| ID | Expression | Context Override | Expected | Notes |
|---|---|---|---|---|
| TC-L-001 | `platform in []` | — | `false` | Empty list — always false |
| TC-L-002 | `platform in ["Oracle HCM Cloud"]` | — | `true` | Single-element list |
| TC-L-003 | `not TRUE` | — | `false` | `not` applied to `TRUE` constant |
| TC-L-004 | `not FALSE` | — | `true` | `not` applied to `FALSE` constant |
| TC-L-005 | `TRUE and engagement_type == "AMS"` | — | `false` | TRUE and false = false |
| TC-L-006 | `FALSE or engagement_type == "Implementation"` | — | `true` | FALSE or true = true |
| TC-L-007 | `modules contains "Oracle HCM Core"` | `modules: ["Oracle HCM Core"]` | `true` | Single-element list contains check |
| TC-L-008 | `project_duration_months >= 18 and project_duration_months <= 24` | — | `true` | 18 in [18,24] range |
| TC-L-009 | `project_duration_months >= 18 and project_duration_months <= 24` | `project_duration_months: 12` | `false` | 12 not in [18,24] range |
| TC-L-010 | `platform == "Oracle HCM Cloud"` | `platform: "Oracle HCM Cloud "` | `false` | Trailing space — exact match fails |
| TC-L-011 | `engagement_type not in ["AMS"]` | `engagement_type: "AMS"` | `false` | Single-item not-in |

---

## 15. Evaluator Compliance Certification

An AREL evaluator implementation is certified as **AREL V1.0 Compliant** when:

1. All 80 test cases produce the exact expected result (no exceptions permitted).
2. No test case raises an uncaught exception — all errors are handled as `false` return.
3. The evaluator processes each test case in under 100ms on standard hardware.
4. The evaluator does not use Python `eval()` or any equivalent dynamic code execution.

**Certification document format:** After running the full test suite, produce a compliance report with:
- Total cases: 80
- Passed: N/80
- Failed: list of failed IDs with actual vs. expected result
- Status: COMPLIANT (80/80) or NON-COMPLIANT (< 80/80)

---

## 16. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-28 | WP19B | Initial test suite — 80 test cases across 12 sections (A–L); reference context; compliance certification criteria |
