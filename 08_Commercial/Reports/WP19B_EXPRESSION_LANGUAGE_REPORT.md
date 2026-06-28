---
document_id: WP19B-EXPRESSION-LANGUAGE-REPORT-V1
title: "WP19B — Assembly Rule Expression Language (AREL) Specification — Completion Report"
version: "1.0"
status: "COMPLETE"
created: "2026-06-28"
created_by: "WP19B — Assembly Rule Expression Language Specification"
approved_by: "Architecture — WP19B"
approved_date: "2026-06-28"
approved_for_reuse: true
category: "Assembly Engine / Governance"
scope: "Completion report for WP19B — documents objective, deliverables produced, design decisions, known gaps, and next steps. Platform maturity advances from L4.1 to L4.2."
---

# WP19B — Assembly Rule Expression Language (AREL) Specification

## Completion Report

**Work Package:** WP19B  
**Date:** 2026-06-28  
**Status:** COMPLETE  
**Platform Maturity:** L4.1 → **L4.2**

---

## 1. Objective

Design, standardise, and freeze the Assembly Rules Expression Language (AREL) used by the Knowledge Platform. AREL governs all `mandatory_if`, `optional_if`, and `excluded_if` expressions in the Knowledge Asset Registry.

**Scope constraints (strictly observed):**
- Language specification only — no rule population, no registry modification, no evaluator implementation.
- Do not redesign KVE architecture.
- Do not introduce new registry metadata.
- Do not modify KRPE or kve_engine.py.

---

## 2. Deliverables Produced

| # | Document | Path | Status |
|---|---|---|---|
| 1 | `ASSEMBLY_RULE_EXPRESSION_LANGUAGE.md` | `08_Commercial/Assembly_Engine/` | FROZEN |
| 2 | `ASSEMBLY_RULE_VALIDATION_STANDARD.md` | `08_Commercial/Assembly_Engine/` | FROZEN |
| 3 | `ASSEMBLY_RULE_TEST_SUITE.md` | `08_Commercial/Assembly_Engine/` | FROZEN |
| 4 | `WP19B_EXPRESSION_LANGUAGE_REPORT.md` (this document) | `08_Commercial/Reports/` | COMPLETE |
| 5 | `HANDOVER.md` | root | UPDATED |
| 6 | `AI_CONTEXT.md` | root | UPDATED |
| 7 | `memory/project_context.md` | `memory/` | UPDATED |
| 8 | `memory/MEMORY.md` | `memory/` | UPDATED |

---

## 3. Design Decisions

### D-001 — Grammar not Python eval

**Decision:** AREL is a formal domain-specific language with a BNF grammar specification, not an alias for Python syntax evaluated via `eval()`.

**Rationale:** The Phase A `evaluate_expression()` function uses Python `eval()` with `__builtins__: {}`. This is unsafe (timing attacks, accidental injection), non-deterministic across Python versions, and requires rule authors to know Python. The KVE Phase B evaluator must replace this with a sandboxed AREL parser.

**Impact:** Existing expressions that happen to be Python-valid but AREL-invalid (e.g. `platform IN ['x']` with single quotes, `engagement_type = 'AMS'` with `=`) must be corrected during rule population.

### D-002 — Null → false for all operators

**Decision:** Any comparison involving a context variable that is absent or null evaluates to `false`, regardless of the operator — including `!=` and `not in`.

**Rationale:** Safe failure principle. A rule that cannot be evaluated should never accidentally enable a mandatory asset or silently disable an exclusion. `!=` returning `true` for null would create phantom matches.

**Impact:** Rule authors must not rely on `!=` to mean "this variable has a known value that is different" — they should use explicit `in` membership tests against the expected value set.

### D-003 — Canonical platform vocabulary

**Decision:** The canonical `platform` context variable has 6 values: "Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle EBS", "Oracle Integration Cloud", "Acumatica", "BeBanking".

**Rationale:** kve_engine.py Phase A has only 4 VALID_PLATFORMS ("Oracle HCM Cloud", "Oracle Fusion ERP", "Acumatica", "BeBanking") — missing EBS and OIC as distinct values, and using "Oracle Fusion ERP" instead of "Oracle ERP Cloud". KRPE's product-specific platform taxonomy (WP19A.1) is the correct source of truth. The kve_engine.py VALID_PLATFORMS constant must be updated in Phase B.

**Impact:** `kve_engine.py` VALID_PLATFORMS must be updated in Phase B. Tender contexts for EBS tenders need `platform: "Oracle EBS"`, not a legacy value.

### D-004 — `contains` operator for list variables

**Decision:** `list_variable contains "value"` tests whether a list-typed variable contains a scalar value. This is distinct from `"value" in list_literal` (scalar in literal list).

**Rationale:** The two use cases are cognitively distinct: checking if a tender module is in scope (`modules contains "Oracle Recruiting Cloud"`) vs. checking if a scalar is one of a fixed enumeration (`platform in ["Oracle HCM Cloud", "Oracle ERP Cloud"]`). Using `contains` for the first and `in` for the second makes rules more readable and prevents the need for Python-style set operations.

### D-005 — Double-quotes only, lowercase keywords

**Decision:** All string literals use double quotes. Logical and membership keywords (`and`, `or`, `not`, `in`, `not in`, `contains`) are lowercase.

**Rationale:** Eliminates ambiguity. Single-quoted strings and uppercase keywords (`AND`, `OR`, `IN`) are forbidden and flagged as ARVAL syntax errors. This makes expressions uniform and parser implementation simpler.

### D-006 — `TRUE` / `FALSE` uppercase shorthands retained

**Decision:** `TRUE` and `FALSE` (uppercase, no quotes) are reserved unconditional shorthands, compatible with existing registry entries (e.g., `mandatory_if_engagement: "TRUE"` for RC-OPS-001).

**Rationale:** Backward compatibility. Existing RSK entries already use `"TRUE"` as a string field value. AREL treats `TRUE` as the unconditional include and `FALSE` as the unconditional exclude; the evaluator recognizes these before parsing.

### D-007 — Variable vocabulary extensible but grammar frozen

**Decision:** Adding new context variables (§6.2 entries) is a V1.x backward-compatible change. Grammar constructs (operators, syntax rules) require a V2.0 change with ADR.

**Rationale:** Context variables will expand as TIL matures and richer tender profiles are produced. Grammar constructs should remain stable to protect the evaluator investment. This two-tier versioning allows vocabulary growth without breaking changes.

---

## 4. Context Variable Vocabulary — Summary

### Core (implemented in Phase A — 7 variables):
`pattern`, `platform`, `engagement_type`, `modules`, `country`, `client_size`, `client_sector`

### Extended (available for Phase B rule population — 13 variables):
`industry`, `bom`, `payroll_integration`, `oci_in_scope`, `client_has_oic`, `dr_in_scope`, `security_in_scope`, `migration_scope`, `integration_scope`, `support_scope`, `pricing_type`, `project_duration_months`

**Total vocabulary: 20 context variables** (7 core + 13 extended)

---

## 5. AREL Validation Standard — Summary

30 ARVAL rules defined across three tiers:
- **Tier 1 — Syntax (ARVAL-001 to ARVAL-010):** Parse grammar compliance; forbidden patterns
- **Tier 2 — Semantic (ARVAL-011 to ARVAL-020):** Variable vocabulary; type compatibility
- **Tier 3 — Contextual (ARVAL-021 to ARVAL-030):** Logical constraints; mandatory_if/excluded_if coherence

Validation runs:
1. During KRPE registry population (pre-write check)
2. During KVE Phase 1 pre-flight (lightweight syntax check)
3. Standalone AREL validator tool (rule author self-service)

---

## 6. Test Suite — Summary

80 test cases across 12 sections:
- Section A: Empty and unconditional forms (5 cases)
- Section B: Simple equality (12 cases)
- Section C: Inequality (6 cases)
- Section D: Numeric comparison (8 cases)
- Section E: Membership `in` and `not in` (12 cases)
- Section F: `contains` operator (10 cases)
- Section G: Boolean variables (8 cases)
- Section H: Logical operators `and`, `or`, `not` (15 cases)
- Section I: Operator precedence (8 cases)
- Section J: Null/undefined variables (8 cases)
- Section K: Complex real-world expressions (12 cases)
- Section L: Edge cases (11 cases)

Compliance threshold: 80/80 (100%) required for AREL V1.0 Compliant certification.

---

## 7. Known Gaps and Deferred Items

| Gap | Description | When to Address |
|---|---|---|
| G-WP19B-001 | `kve_engine.py` VALID_PLATFORMS constant uses "Oracle Fusion ERP" — must be updated to canonical vocabulary | KVE Phase B |
| G-WP19B-002 | `evaluate_expression()` uses Python `eval()` — must be replaced with sandboxed AREL parser | KVE Phase B |
| G-WP19B-003 | Extended context variables (13) not yet populated by TIL Block G — `tender_context.yaml` schema extension needed | TIL Phase B |
| G-WP19B-004 | AREL validator tool not yet implemented — rule authors rely on manual review for now | Before large-scale rule population |
| G-WP19B-005 | `optional_if` field semantics not yet implemented in KVE (ARVAL-028 notes this) — Phase A ignores it | KVE Phase B |
| G-WP19B-006 | Existing schema example expressions (KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md §4) use Python syntax — must be updated to AREL when rules are populated | Assembly rules population work package |

---

## 8. Pre-Conditions for Rule Population

Before large-scale rule population (mandatory_if / optional_if / excluded_if for 49 CAPs + 13 ASPs) begins:

| Pre-Condition | Status |
|---|---|
| AREL grammar frozen (V1.0) | COMPLETE (WP19B) |
| AREL validation standard defined (30 rules) | COMPLETE (WP19B) |
| AREL test suite defined (80 cases) | COMPLETE (WP19B) |
| AREL evaluator implemented and passing test suite | PENDING — KVE Phase B |
| AREL validator tool available for rule authors | PENDING — before population |
| WP18B-EXT.2 completed (Risk Library approved — resolves AV-011 BLOCK) | PENDING — BU Lead action ~2h |

Rule population **must not start** until both the evaluator is certified AREL V1.0 Compliant and the AREL validator tool is available. Writing rules into the registry that cannot be evaluated will produce silent false-negatives in KVE (current `eval()` fallback returns `false` on parse error).

---

## 9. Platform Maturity Update

| Dimension | Before WP19B | After WP19B |
|---|---|---|
| Registry | L4.1 (1,198 entries clean) | L4.1 (unchanged) |
| Expression Language | Undefined — ad-hoc Python eval | **L4.2 — AREL V1.0 FROZEN** |
| KVE Phase A | Operational (22 BLOCK rules) | Operational (unchanged) |
| KVE Phase B | Pending | Pending (unblocked by WP19B) |
| Rule Population | Blocked (no language spec) | **Unblocked — pending evaluator implementation** |

**Platform maturity: L4.2**

---

## 10. Recommended Next Steps

Priority order:

1. **WP18B-EXT.2** (BU Lead, ~2h 10min human action) — Risk Library governance session. Approves RC-OPS-001 and resolves the AV-011 BLOCK that prevents any non-P10 proposal from proceeding to assembly. This is the highest-priority action for enabling real proposal generation.

2. **KVE Phase B** — Implement the full 76-rule set, replace `eval()` with an AREL-compliant evaluator, run 80-case test suite to certify compliance, implement Health Score.

3. **AREL Validator Tool** — Implement standalone expression validator (ARVAL-001 to ARVAL-030) as a command-line tool. Required before rule population begins.

4. **TIL Block G Extension** — Extend `tender_context.yaml` schema to include the 13 extended variables. Required for Phase B expressions that reference `industry`, `bom`, `payroll_integration`, etc.

5. **Assembly Rules Population** — Populate `mandatory_if`, `optional_if`, `excluded_if` for all 49 CAPs + 13 ASPs. Requires items 2, 3, and 4 to be complete.

---

## 11. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-28 | WP19B | Initial completion report — 4 deliverables; 7 design decisions; 20 context variables; 30 validation rules; 80 test cases; 6 known gaps |
