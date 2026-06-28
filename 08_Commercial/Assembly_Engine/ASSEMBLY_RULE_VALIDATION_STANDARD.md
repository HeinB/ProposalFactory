---
document_id: ASSEMBLY-RULE-VALIDATION-STANDARD-V1
title: "Assembly Rule Validation Standard — AREL Expression Validation V1.0"
version: "1.0"
status: "FROZEN"
created: "2026-06-28"
created_by: "WP19B — Assembly Rule Expression Language Specification"
approved_by: "Architecture — WP19B"
approved_date: "2026-06-28"
approved_for_reuse: true
category: "Assembly Engine / Expression Language"
scope: "Defines the complete validation ruleset for AREL expressions stored in the Knowledge Asset Registry — covering syntax validation, semantic validation, contextual constraints, and the severity model applied by the AREL validator during registry population and KVE pre-flight checks."
governing_standard: "ASSEMBLY_RULE_EXPRESSION_LANGUAGE.md V1.0"
related_documents:
  - ASSEMBLY_RULE_EXPRESSION_LANGUAGE.md
  - ASSEMBLY_RULE_TEST_SUITE.md
  - KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md
  - VALIDATION_RULE_EXECUTION_MODEL.md
---

# Assembly Rule Validation Standard — AREL Expression Validation V1.0

**Work Package:** WP19B  
**Status:** FROZEN  
**Governs:** Validation of all `mandatory_if`, `optional_if`, `excluded_if` expressions in the Knowledge Asset Registry.

---

## 1. Purpose

This standard defines the rules that govern whether an AREL expression stored in a registry entry is valid. It separates validation into three layers:

1. **Syntax validation** — does the expression parse against the AREL grammar?
2. **Semantic validation** — do the variables and type usages make sense?
3. **Contextual constraints** — are there logical errors (always-true, always-false, contradictions with other rules on the same asset)?

Validation is performed:
- **During registry population** (KRPE): before any expression is written to the registry YAML, it must pass at minimum ARVAL-001 to ARVAL-007.
- **During KVE pre-flight** (Phase 1, RI-014 extension): expressions are re-validated as part of the registry integrity check to catch expressions that were valid when written but became invalid after a vocabulary change.
- **In the AREL validator tool** (standalone): rule authors may run expressions through the validator before populating registry entries.

---

## 2. Validation Rule Table

### Tier 1 — Syntax Rules (ARVAL-001 to ARVAL-010)

Syntax rules check that the expression string is grammatically well-formed per ASSEMBLY_RULE_EXPRESSION_LANGUAGE.md §3.

| Rule ID | Severity | Check | Condition | Remediation |
|---|---|---|---|---|
| ARVAL-001 | ERROR | Parse against AREL grammar | Expression is not a valid AREL parse tree | Rewrite the expression per the AREL grammar |
| ARVAL-002 | ERROR | No single-quoted strings | Expression contains `'` | Replace `'...'` with `"..."` |
| ARVAL-003 | ERROR | No single-equals operator | Expression contains `=` not preceded or followed by `=`, `!`, `<`, `>` | Replace `=` with `==` |
| ARVAL-004 | ERROR | No Python-style operators | Expression contains `and` written as `&&`, `or` as `\|\|`, `not` as `!` (prefix) | Replace with AREL keywords |
| ARVAL-005 | ERROR | No function calls | Expression contains `(` immediately preceded by an identifier (e.g. `len(`, `str(`) | Remove function call; use direct variable comparisons |
| ARVAL-006 | ERROR | No index access | Expression contains `[` immediately preceded by an identifier (e.g. `modules[0]`) | Use `contains` operator instead |
| ARVAL-007 | ERROR | No method calls | Expression contains `.` used as a method accessor (e.g. `platform.startswith`) | Use supported operators only |
| ARVAL-008 | WARNING | Uppercase `IN` / `NOT IN` / `CONTAINS` | `IN`, `NOT IN`, or `CONTAINS` in uppercase | Replace with lowercase forms |
| ARVAL-009 | WARNING | Uppercase `AND` / `OR` / `NOT` | Logical keywords in uppercase | Replace with lowercase forms |
| ARVAL-010 | ERROR | Literal on left of comparison | `==`, `!=`, `>`, `>=`, `<`, `<=` has a string, number, or boolean literal on the left | Swap operands so variable is on the left |

### Tier 2 — Semantic Rules (ARVAL-011 to ARVAL-020)

Semantic rules check that the variables referenced exist in the AREL vocabulary and are used with types that match their declared type.

| Rule ID | Severity | Check | Condition | Remediation |
|---|---|---|---|---|
| ARVAL-011 | WARNING | Variable in AREL vocabulary | Expression references a variable name not in ASSEMBLY_RULE_EXPRESSION_LANGUAGE.md §6 | Correct the variable name or request vocabulary extension via ADR |
| ARVAL-012 | ERROR | Numeric operator on string variable | `>`, `>=`, `<`, `<=` applied to a string-typed variable | Use `==`, `!=`, `in`, or `not in` instead |
| ARVAL-013 | ERROR | Numeric operator on boolean variable | `>`, `>=`, `<`, `<=` applied to a boolean-typed variable | Use `== true` or `== false` instead |
| ARVAL-014 | ERROR | `==` / `!=` on list variable | `==` or `!=` applied to a list-typed variable (`modules`, `bom`) | Use `contains` or check individual values |
| ARVAL-015 | ERROR | `contains` on scalar variable | `contains` left operand is a scalar-typed variable | Use `in` for scalar membership testing |
| ARVAL-016 | ERROR | Mixed-type `in` list | List literal in `in` / `not in` expression contains elements of mixed types | Use a uniform-type list (all strings or all numbers) |
| ARVAL-017 | WARNING | Phase B variable in Phase A registry | Expression references an extended variable (§6.2) | Acceptable if expression is authored for Phase B rule population; flag for Phase B validation pass |
| ARVAL-018 | ERROR | String compared to boolean literal | `variable == true` where variable is a string-typed variable | Check `variable in ["true"]` is likely wrong; use correct variable |
| ARVAL-019 | ERROR | `TRUE` / `FALSE` in quoted form | Expression contains `"TRUE"` or `"FALSE"` (quoted) in a position where a boolean result is expected | Use `TRUE` or `FALSE` without quotes |
| ARVAL-020 | WARNING | `not in` on single-item list | `variable not in ["single_value"]` — equivalent to `variable != "single_value"` | Simplify to `variable != "single_value"` for clarity |

### Tier 3 — Contextual Constraints (ARVAL-021 to ARVAL-030)

Contextual rules check logical relationships between the three assembly rule fields on the same registry entry, and flag expressions that are logically degenerate.

| Rule ID | Severity | Check | Condition | Remediation |
|---|---|---|---|---|
| ARVAL-021 | WARNING | `mandatory_if` and `excluded_if` potential conflict | Both `mandatory_if` and `excluded_if` are non-empty and reference the same variables with conditions that could simultaneously be true | Review — KVE AV-010 will BLOCK if both evaluate to `true` at runtime; resolve conflict in expressions |
| ARVAL-022 | INFO | Redundant `excluded_if` when `mandatory_if = TRUE` | Asset has `mandatory_if: TRUE` and a non-empty `excluded_if` | Unconditionally mandatory assets should have `excluded_if: ""` |
| ARVAL-023 | WARNING | Tautological expression | Expression is always `true` regardless of context (e.g. `platform == platform`, `true == true`) | Simplify to `TRUE` if unconditional inclusion is intended |
| ARVAL-024 | WARNING | Contradiction expression | Expression is always `false` regardless of context (e.g. `platform == "Oracle HCM Cloud" and platform == "Acumatica"`) | Simplify to `FALSE` or remove |
| ARVAL-025 | WARNING | CAP with `mandatory_if` and `excluded_if` both empty | Both fields are `""` for a CAP asset | Confirm the asset is pattern-driven (pattern_applicability) only; if always-include, set `mandatory_if: TRUE` |
| ARVAL-026 | ERROR | ASM with empty `mandatory_if` | ASM asset has `mandatory_if: ""` — triggers LV-ASM-003 WARNING during KVE validation | Populate `mandatory_if` per LV-ASM-003 requirement |
| ARVAL-027 | WARNING | Asymmetric `mandatory_if` / `excluded_if` pair | `mandatory_if` references `platform == "Oracle HCM Cloud"` but `excluded_if` does not reference platform | Typically `excluded_if` should be the logical complement of `mandatory_if`; verify intent |
| ARVAL-028 | INFO | `optional_if` field non-empty | `optional_if` is populated — note this field is not currently evaluated by KVE Phase A | Valid for future use; no action required until Phase B optional selection rules are implemented |
| ARVAL-029 | WARNING | `excluded_if` is `TRUE` for non-ARCHIVED asset | Asset has `excluded_if: TRUE` but `lifecycle_status = APPROVED` and `approved_for_reuse = true` | If the asset should never be assembled, consider setting `approved_for_reuse: false` instead |
| ARVAL-030 | ERROR | `mandatory_if` is `TRUE` for DRAFT asset | Asset has `mandatory_if: TRUE` but `lifecycle_status = DRAFT` | DRAFT assets cannot be unconditionally mandatory; KVE AV-001 / AV-002 will BLOCK |

---

## 3. Validation Severity Model

| Severity | Effect on Registry Population | Effect on KVE Run |
|---|---|---|
| **ERROR** | Expression must not be written to registry; KRPE fails with error | KVE logs validation failure for the asset; expression treated as `""` (false) |
| **WARNING** | Expression may be written to registry with warning recorded | KVE logs warning; expression evaluated as authored; rule author must review |
| **INFO** | Expression is acceptable; informational note only | No KVE action |

---

## 4. Validation Procedure

### 4.1 During Registry Population (KRPE)

When KRPE generates a registry entry with assembly_rules populated:

```
FOR each asset entry being written:
  FOR each field IN [mandatory_if, optional_if, excluded_if]:
    expr = entry.assembly_rules[field]
    IF expr == "" OR expr == "TRUE" OR expr == "FALSE":
      PASS (no validation needed)
    ELSE:
      Run ARVAL-001 through ARVAL-010 (syntax rules)
      IF any ERROR → reject entry; log error; halt for this asset
      Run ARVAL-011 through ARVAL-020 (semantic rules)
      IF any ERROR → reject entry; log error; halt for this asset
      IF any WARNING → log warning; allow entry to proceed
      Run ARVAL-021 through ARVAL-030 (contextual rules)
      IF any ERROR → reject entry; log error; halt for this asset
      IF any WARNING → log warning; allow entry to proceed
```

### 4.2 During KVE Pre-Flight (Phase 1 Extension)

After RI-014 (mandatory fields), KVE runs a lightweight expression check:

```
FOR each asset in registry where assembly_rules has any non-empty expression:
  Run ARVAL-001 (parse check) on each expression
  IF ARVAL-001 fails → log WARNING; asset remains in registry but expressions are treated as ""
```

Full Tier 2 and Tier 3 checks are deferred to the KRPE population phase to avoid slowing KVE runtime.

### 4.3 Standalone AREL Validator

Rule authors should validate expressions before population. The validator tool accepts:
- A single expression string
- Optionally, a context YAML file for semantic type checking

Output: list of ARVAL rule results with severity and remediation advice.

---

## 5. Compliance Thresholds

For a registry to be considered **expression-clean**:

| Threshold | Requirement |
|---|---|
| Minimum | Zero ARVAL ERROR conditions across all entries |
| Target | Zero ARVAL ERROR + zero ARVAL WARNING conditions |
| Certified | Zero ERROR + zero WARNING + all INFO items reviewed and accepted |

These thresholds apply to entries where `mandatory_if`, `optional_if`, or `excluded_if` contains a non-empty, non-`TRUE`, non-`FALSE` expression. Entries with only `""`, `TRUE`, or `FALSE` are implicitly compliant.

---

## 6. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-28 | WP19B | Initial standard — 30 ARVAL rules across three tiers; severity model; validation procedure; compliance thresholds |
