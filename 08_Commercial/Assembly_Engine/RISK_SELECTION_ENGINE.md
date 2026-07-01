---
document_id: RISK-SELECTION-ENGINE-V1
title: "Risk Selection Engine — Architecture v1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-29"
created_by: "PF2-001 — Proposal Factory Risk Selection Engine"
approved_by: "PF2-001"
approved_date: "2026-06-29"
approved_for_reuse: true
category: "Proposal Factory / Architecture"
scope: "Defines the architecture, selection logic, data flows, and governance of the Risk Selection Engine — the first Proposal Factory component that consumes the certified Knowledge Platform."
related_documents:
  - 08_Commercial/Assembly_Engine/kve_engine.py
  - 08_Commercial/Assembly_Engine/rse.py
  - 08_Commercial/Assembly_Engine/ASSEMBLY_RULE_EXPRESSION_LANGUAGE.md
  - 08_Commercial/Risk_Library/ENTERPRISE_RISK_REGISTER_V1.md
  - 08_Commercial/Risk_Library/RISK_PROPOSAL_MAPPING.md
  - 08_Commercial/Risk_Library/RISK_ASSUMPTION_CROSS_REFERENCE.md
  - 08_Commercial/Reports/KNOWLEDGE_REGISTRY_V1_CERTIFICATION.md
---

# Risk Selection Engine — Architecture v1.0

**Work Package:** PF2-001  
**Date:** 2026-06-29  
**Status:** APPROVED  
**Platform Maturity:** L5.1 → **L5.2**

---

## 1. Purpose

The Risk Selection Engine (RSE) is the first Proposal Factory component that consumes the certified Knowledge Platform. It selects proposal risks deterministically from the approved Enterprise Risk Library using a certified Assembly Manifest context.

**Input:** Certified tender context (from Assembly Manifest or standalone YAML)  
**Output:** Selected Proposal Risk Register + Risk Selection Audit  
**Selection:** 100% deterministic — driven by AREL V1.0 expressions. No AI judgement. No probabilistic ranking.

---

## 2. Position in Proposal Factory

```
Knowledge Platform (L5.1)
│
├── KNOWLEDGE_ASSET_REGISTRY_V1.yaml   (213 core assets)
├── kve_engine.py v2.0                 (76 rules — governance gateway)
└── ENTERPRISE_RISK_REGISTER_V1.md     (40 approved RSK assets)
           │
           ▼
    ┌─────────────────────────┐
    │  Risk Selection Engine  │  ◄── rse.py v1.0
    │  (RSE)                  │
    └─────────────────────────┘
           │
     ┌─────┴──────┐
     ▼            ▼
SELECTED_RISK_   RISK_SELECTION_
REGISTER_[T].md  AUDIT_[T].md
```

The RSE is the first Proposal Factory stage between the Knowledge Platform and the assembled proposal. It produces a deterministic risk section that feeds directly into the proposal writing pipeline.

---

## 3. Architecture

### 3.1 Components

| Component | Description |
|---|---|
| `rse.py` | Risk Selection Engine — Python 3 script |
| `RSEContext` | Dataclass: 20 KVE AREL variables + 14 RSE extension fields |
| `RSEARELEvaluator` | AREL V1.0 recursive-descent evaluator (RSE variant) |
| `normalize_arel()` | ERR expression normalizer |
| `parse_risk_register()` | Parses ENTERPRISE_RISK_REGISTER_V1.md |
| `select_risks()` | Core selection cascade |
| `validate_selections()` | Deterministic validation checks |
| Output generators | `generate_risk_register_md()` + `generate_audit_md()` |

### 3.2 Data Flow

```
ENTERPRISE_RISK_REGISTER_V1.md
         │
         ▼
  parse_risk_register()
         │
         ▼  40 RSKRecord objects
  ┌──────────────────────────────────────────────────────┐
  │  select_risks(risks, ctx)                            │
  │                                                      │
  │  For each RSKRecord:                                 │
  │    1. Lifecycle filter  → LIFECYCLE_EXCLUDED         │
  │    2. Pattern filter    → PATTERN_EXCLUDED           │
  │    3. normalize_arel()  → AREL V1.0 expression       │
  │    4. excluded_if eval  → EXCLUDED                   │
  │    5. mandatory_if eval → MANDATORY                  │
  │    6. optional_if eval  → OPTIONAL_SELECTED          │
  │    7. else              → DEFAULT_EXCLUDED           │
  └──────────────────────────────────────────────────────┘
         │
         ▼
  validate_selections()
         │
         ▼
  generate_risk_register_md() → SELECTED_RISK_REGISTER_[Tender].md
  generate_audit_md()         → RISK_SELECTION_AUDIT_[Tender].md
```

---

## 4. Selection Cascade

For each of the 40 approved RSK assets, the RSE applies the following cascade in strict order:

| Step | Test | Classification |
|---|---|---|
| 1 | lifecycle_status ≠ APPROVED | LIFECYCLE_EXCLUDED |
| 2 | tender pattern ∉ risk.proposal_patterns | PATTERN_EXCLUDED |
| 3 | excluded_if evaluates to TRUE | EXCLUDED |
| 4 | mandatory_if evaluates to TRUE | MANDATORY |
| 5 | optional_if evaluates to TRUE | OPTIONAL_SELECTED |
| 6 | (none of the above) | DEFAULT_EXCLUDED |

**SELECTED** = MANDATORY ∪ OPTIONAL_SELECTED  
**NOT SELECTED** = EXCLUDED ∪ PATTERN_EXCLUDED ∪ DEFAULT_EXCLUDED ∪ LIFECYCLE_EXCLUDED

The cascade is deterministic and irreversible: once a risk is classified at step N, steps N+1 onward are not evaluated. `excluded_if` always takes precedence over `mandatory_if`.

---

## 5. Context Model

### 5.1 RSEContext Fields

The RSEContext includes the 20 KVE AREL context variables plus 14 RSE extension fields:

**KVE AREL variables (20):**

| Field | Type | Description |
|---|---|---|
| `tender_id` | str | Tender identifier |
| `pattern` | str | Proposal pattern (P1–P13) |
| `platform` | str | Canonical platform name |
| `engagement_type` | str | "Implementation", "AMS", "DBA" |
| `modules` | List[str] | Modules in scope |
| `country` | str | ISO 3166-1 alpha-2 (e.g., "ZA") |
| `client_size` | str | "Enterprise", "Mid-Market" |
| `client_sector` | str | Industry sector |
| `am_clearances` | List[str] | AM governance clearances |
| `ptc_clearances` | List[str] | PTC clearances |
| `tender_date` | str | Tender date |
| `industry` | str | Industry vertical |
| `bom` | List[str] | Bill of materials |
| `payroll_integration` | Optional[bool] | Payroll integration in scope |
| `oci_in_scope` | Optional[bool] | OCI infrastructure in scope |
| `client_has_oic` | Optional[bool] | Client has OIC licence |
| `dr_in_scope` | Optional[bool] | Disaster recovery in scope |
| `security_in_scope` | Optional[bool] | Security workstream in scope |
| `migration_scope` | Optional[bool] | Data migration in scope |
| `integration_scope` | Optional[bool] | Integration workstream in scope |
| `support_scope` | Optional[bool] | Support in scope |
| `pricing_type` | str | "Fixed Price", "Time and Materials" |
| `project_duration_months` | Optional[float] | Duration in months |

**RSE extension fields (14):**

| Field | Type | Used by |
|---|---|---|
| `integration_count` | Optional[int] | RC-INT-002 |
| `third_party_api` | Optional[bool] | RC-INT-003 |
| `payroll_provider` | str | RC-INT-007 |
| `oax_in_scope` | Optional[bool] | RC-TECH-006, RC-TECH-007, RC-COMM-001 |
| `analytics_requirements_in_tender` | Optional[bool] | RC-TECH-006, RC-COMM-001 |
| `oda_in_scope` | Optional[bool] | RC-TECH-009 |
| `digital_channels` | Optional[bool] | RC-TECH-010 |
| `feature_licensing_confirmed` | Optional[bool] | RC-TECH-008 |
| `help_desk_in_scope` | Optional[bool] | RC-CLIENT-006, RC-COMM-002 |
| `personal_data_in_scope` | Optional[bool] | RC-COMP-001 |
| `integration_method_prescribed_in_tender` | Optional[bool] | RC-COMM-003 |
| `delivery_model` | str | RC-PROJ-002 |
| `phase_count` | Optional[int] | RC-PROJ-002 |
| `fixed_price` | Optional[bool] | RC-PROJ-004 (derived from pricing_type) |

**Note:** RSE extension fields default to `None` when not provided. AREL's null-safe evaluation returns `False` for any comparison involving `None`. This means risks whose selection conditions reference absent extension fields evaluate to DEFAULT_EXCLUDED. Provide an RSE extension YAML to unlock these risks.

### 5.2 Context Loading

The RSE context is loaded from a tender context YAML (`tender_context`) with an optional RSE extension YAML (`rse_extension`). Two normalizations are applied automatically:

1. **Country normalization:** `country: "RSA"` → `"ZA"` (ISO 3166-1 alpha-2; AREL expressions use "ZA")
2. **fixed_price derivation:** `fixed_price` is derived from `pricing_type` — `True` if `pricing_type` is "Fixed Price", "Fixed-Price", or "Fixed"

---

## 6. AREL Expression Normalization

The Enterprise Risk Register (ERR) was authored before AREL V1.0 was frozen, using a pre-standard expression syntax. The RSE normalizes all ERR expressions before evaluation:

| Transformation | Example Before | After |
|---|---|---|
| Keyword lowercase | `CONTAINS` | `contains` |
| Keyword lowercase | `AND`, `OR`, `NOT` | `and`, `or`, `not` |
| Equality operator | `engagement_type = "AMS"` | `engagement_type == "AMS"` |
| Platform alias | `platform contains "OIC"` | `platform contains "Oracle Integration Cloud"` |
| Preserves | `!=`, `>=`, `<=`, `==` | unchanged |

The standalone `=` → `==` substitution uses the regex `(?<![!<>=])=(?![=])` to avoid modifying `!=`, `>=`, `<=`, `==`.

---

## 7. RSE AREL Evaluator — List-Aware Contains

The RSE uses `RSEARELEvaluator`, a variant of the KVE `ARELEvaluator` with one behavioral difference:

**List-aware `contains`:** When the left operand is a list, `contains` checks whether the right operand is a substring of any list element (not exact membership).

| Evaluator | `modules contains "Oracle Learning"` (modules=["Oracle Learning Cloud"]) |
|---|---|
| KVE ARELEvaluator | `False` (exact membership: "Oracle Learning" not in list) |
| RSE RSEARELEvaluator | `True` (substring: "Oracle Learning" IS in "Oracle Learning Cloud") |

This is necessary because the ERR uses partial module names (e.g., "Oracle Learning") while context module lists use full canonical names (e.g., "Oracle Learning Cloud").

Both evaluators are AREL V1.0 compliant for non-list operands.

---

## 8. Validation Checks

After selection, the RSE runs deterministic validation checks:

| Check | Rule | Severity |
|---|---|---|
| V-001 | No duplicate risk IDs in selected set | FAIL |
| V-002 | No risk is both mandatory_if=TRUE and excluded_if=TRUE | FAIL |
| V-003 | RC-OPS-001 must not resolve to DEFAULT_EXCLUDED | WARN |

---

## 9. Output Documents

### 9.1 SELECTED_RISK_REGISTER_[TenderID].md

Contains:
- Selection summary (counts by status)
- Selected risks (MANDATORY first, then OPTIONAL_SELECTED), sorted by assembly_priority then rating
- Risk metadata: ID, title, category, rating, likelihood, impact, assembly priority, selection reason, source rule, owner, proposal sections, related assumptions, applicable patterns, description summary
- Excluded risks table
- Pattern-excluded risks table
- Default-excluded risks table (with unresolved conditions)

### 9.2 RISK_SELECTION_AUDIT_[TenderID].md

Contains:
- Audit summary (counts by status)
- Tender context used (all fields)
- Full evaluation trace: one row per risk, showing normalized expressions and TRUE/FALSE results for each of excluded_if, mandatory_if, optional_if
- Validation violations
- AREL normalization applied (documentation of transformations)

---

## 10. CLI

```
python3 rse.py <context.yaml> [--extension <ext.yaml>] [--register <path>]
               [--outdir <path>] [--dry-run] [--run-tests]
```

| Flag | Description |
|---|---|
| `context` | Tender context YAML (required) |
| `--extension` | RSE extension YAML (optional; adds RSE-specific fields) |
| `--register` | Path to ENTERPRISE_RISK_REGISTER_V1.md (auto-located by default) |
| `--outdir` | Output directory (defaults to 08_Commercial/Reports/) |
| `--dry-run` | Print results without writing files |
| `--run-tests` | Run 17-test self-test suite and exit |

---

## 11. RSE Extension YAML Format

```yaml
# rse_extension_[TenderID].yaml
rse_extension:
  integration_count: 4               # integer — number of integrations in scope
  third_party_api: true              # bool — third-party API in scope
  payroll_provider: "non-standard"   # str — "standard" or "non-standard"
  oax_in_scope: false                # bool — Oracle Analytics (OAX) in scope
  analytics_requirements_in_tender: true
  oda_in_scope: false
  digital_channels: false
  feature_licensing_confirmed: false  # false → RC-TECH-008 MANDATORY
  help_desk_in_scope: false
  personal_data_in_scope: true       # true → RC-COMP-001 MANDATORY for ZA
  integration_method_prescribed_in_tender: false
  delivery_model: "Phased"           # "Single" or "Phased"
  phase_count: 3
```

---

## 12. Known Data Quality Gaps

The following gaps in the Enterprise Risk Register were identified during RSE implementation. They affect which risks enter the DEFAULT_EXCLUDED category when RSE extension fields are absent.

| Gap | Risks Affected | Impact |
|---|---|---|
| `oax_in_scope` not in base context | RC-TECH-006, RC-TECH-007, RC-COMM-001 | DEFAULT_EXCLUDED when field absent |
| `feature_licensing_confirmed` not in base context | RC-TECH-008 | DEFAULT_EXCLUDED — should be MANDATORY for new Oracle implementations |
| `personal_data_in_scope` not in base context | RC-COMP-001 | DEFAULT_EXCLUDED — POPIA risk missed for HCM/OIC proposals without extension |
| `integration_count` not in base context | RC-INT-002 | DEFAULT_EXCLUDED — integration scope risk missed |
| ERR uses `= "AMS"` (single equals) | All 40 risks | Normalized by RSE at evaluation time |
| ERR uses `CONTAINS` (uppercase) | 20+ risks | Normalized by RSE at evaluation time |
| `payroll_integration == FALSE` exclusion | RC-INT-001, RC-INT-005 | Correctly EXCLUDED by exclusion logic |
| BeBanking pattern P12 missing from RC-OPS-001 | RC-OPS-001 | PATTERN_EXCLUDED for P12 proposals — possible ERR oversight |

**Resolution path:** Provide RSE extension YAML for full risk resolution. Data quality items to address in future ERR revision.

---

## 13. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-29 | PF2-001 | Initial architecture — RSE v1.0; 17/17 self-tests; 5 regression scenarios |
