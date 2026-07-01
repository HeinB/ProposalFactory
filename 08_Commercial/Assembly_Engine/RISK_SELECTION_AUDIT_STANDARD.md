---
document_id: RISK-SELECTION-AUDIT-STANDARD-V1
title: "Risk Selection Audit Standard — V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-29"
created_by: "PF2-001 — Proposal Factory Risk Selection Engine"
approved_by: "PF2-001"
approved_date: "2026-06-29"
approved_for_reuse: true
category: "Proposal Factory / Standards"
scope: "Defines the required structure, content, and traceability requirements for the RISK_SELECTION_AUDIT output produced by the RSE."
---

# Risk Selection Audit Standard — V1.0

**Purpose:** Defines what a valid RISK_SELECTION_AUDIT_[TenderID].md must contain.

---

## 1. Purpose of the Audit Document

The Risk Selection Audit provides complete traceability for every RSE selection decision. It must be sufficient to allow an independent reviewer to verify that:
1. The correct AREL expressions were evaluated
2. The normalization transformations were applied consistently
3. The tender context used is complete and accurate
4. Every risk received a classified outcome (no risks skipped)
5. Validation checks were applied and results recorded

---

## 2. Required Sections

| Section | Required | Description |
|---|---|---|
| Document frontmatter | Mandatory | YAML block with document_id, tender_id, engine, generated |
| Audit Summary | Mandatory | Count table by status |
| Tender Context Used | Mandatory | All RSEContext fields as evaluated (post-normalization) |
| Full Evaluation Trace | Mandatory | One row per risk: ID, status, normalized expressions, TRUE/FALSE results per condition, reason |
| Validation Violations | Mandatory | All V-001, V-002, V-003 results (PASS or FAIL) |
| AREL Normalization Applied | Mandatory | Documentation of all transformations applied |
| Generation metadata | Mandatory | Engine version, timestamp |

---

## 3. Evaluation Trace Requirements

The full evaluation trace table MUST include one row per risk (all 40 ERR entries):

| Column | Required | Description |
|---|---|---|
| Risk ID | Mandatory | Risk identifier |
| Status | Mandatory | Final classification |
| excl_if result | Mandatory | Normalized expression + TRUE/FALSE/—  |
| mand_if result | Mandatory | Normalized expression + TRUE/FALSE/— |
| opt_if result | Mandatory | Normalized expression + TRUE/FALSE/— |
| Reason | Mandatory | Human-readable selection reason |

For PATTERN_EXCLUDED and LIFECYCLE_EXCLUDED entries, expression columns show "—" (not evaluated).

---

## 4. Tender Context Documentation

All the following fields must be documented in the audit, showing the value as used for evaluation (post-normalization):

- tender_id, pattern, platform, engagement_type, modules, country (normalized)
- client_size, client_sector, payroll_integration, pricing_type, fixed_price (derived)
- integration_scope, security_in_scope, migration_scope, dr_in_scope
- integration_count, oax_in_scope, analytics_requirements_in_tender
- personal_data_in_scope, help_desk_in_scope, feature_licensing_confirmed
- delivery_model

Fields not provided (None) are documented as None — confirming null-safe evaluation applied.

---

## 5. Validation Check Requirements

The audit MUST document the results of all three validation checks:

| Check | Description | Required Action |
|---|---|---|
| V-001 | No duplicate risk IDs in selected set | FAIL → investigation required |
| V-002 | No risk is both mandatory_if=TRUE and excluded_if=TRUE | FAIL → ERR review required |
| V-003 | RC-OPS-001 not in DEFAULT_EXCLUDED | WARN → verify mandatory_if expression |

An audit with V-001 or V-002 FAIL must not be used to assemble a proposal risk section.

---

## 6. AREL Normalization Documentation

The audit MUST document all AREL transformations applied, including:
- Keyword case normalization (CONTAINS/AND/OR/NOT → lowercase)
- Equality operator normalization (standalone = → ==)
- Platform alias normalization ("OIC" → "Oracle Integration Cloud")
- Country normalization (RSA → ZA)
- List-aware contains behavior

---

## 7. Completeness Check

An audit is complete if:
- Total rows in evaluation trace = 40 (all ERR entries)
- Sum of MANDATORY + OPTIONAL_SELECTED + EXCLUDED + PATTERN_EXCLUDED + DEFAULT_EXCLUDED = 40
- All validation checks documented

---

## 8. Naming Convention

```
RISK_SELECTION_AUDIT_[TenderID].md
```

Where `[TenderID]` is the `tender_id` field from the context, with hyphens and spaces replaced by underscores.

Files are written to `08_Commercial/Reports/`.

---

## 9. Amendment History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-06-29 | Initial standard — PF2-001 |
