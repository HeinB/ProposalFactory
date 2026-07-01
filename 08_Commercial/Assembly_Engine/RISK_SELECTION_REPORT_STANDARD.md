---
document_id: RISK-SELECTION-REPORT-STANDARD-V1
title: "Risk Selection Report Standard — V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-29"
created_by: "PF2-001 — Proposal Factory Risk Selection Engine"
approved_by: "PF2-001"
approved_date: "2026-06-29"
approved_for_reuse: true
category: "Proposal Factory / Standards"
scope: "Defines the required structure, content, and completeness criteria for the SELECTED_RISK_REGISTER output produced by the RSE."
---

# Risk Selection Report Standard — V1.0

**Purpose:** Defines what a valid SELECTED_RISK_REGISTER_[TenderID].md must contain.

---

## 1. Required Sections

| Section | Required | Description |
|---|---|---|
| Document frontmatter | Mandatory | YAML block with document_id, tender_id, pattern, platform, engine version |
| Summary table | Mandatory | Counts by status: MANDATORY, OPTIONAL_SELECTED, EXCLUDED, PATTERN_EXCLUDED, DEFAULT_EXCLUDED |
| Selected Risks | Mandatory | Full entry for each selected risk (MANDATORY + OPTIONAL_SELECTED) |
| Excluded Risks | Mandatory | Table of risks excluded by excluded_if=TRUE |
| Pattern-Excluded Risks | Mandatory | Table of risks not applicable to this pattern |
| Default-Excluded Risks | Mandatory | Table of risks with unresolved conditions |
| Generation metadata | Mandatory | Engine version, timestamp |

---

## 2. Selected Risk Entry Requirements

Each selected risk entry must include:

| Field | Required |
|---|---|
| Risk ID | Mandatory |
| Title | Mandatory |
| Category | Mandatory |
| Rating (CRITICAL / HIGH / MEDIUM / LOW) | Mandatory |
| Likelihood × Impact | Mandatory |
| Assembly priority | Mandatory |
| Selection status (MANDATORY / OPTIONAL_SELECTED) | Mandatory |
| Why selected (reason string with source expression) | Mandatory |
| Source rule (mandatory_if raw expression) | Mandatory |
| Owner | Mandatory |
| Proposal sections (Primary + Secondary) | Mandatory |
| Related assumptions (governed IDs only) | Mandatory |
| Applicable proposal patterns | Mandatory |
| Description summary (first sentence of risk description) | Mandatory |

---

## 3. Sort Order

Selected risks MUST appear in the following order:
1. Assembly priority: Critical → High → Standard → Low
2. Rating: CRITICAL → HIGH → MEDIUM → LOW
3. Risk ID: ascending alphabetical

MANDATORY risks appear before OPTIONAL_SELECTED risks within each priority group.

---

## 4. Completeness Criteria

A SELECTED_RISK_REGISTER is complete if:
- All 40 Enterprise Risk Register entries are accounted for (total = MANDATORY + OPTIONAL + EXCLUDED + PATTERN_EXCLUDED + DEFAULT_EXCLUDED)
- RC-OPS-001 appears in MANDATORY or EXCLUDED (never DEFAULT_EXCLUDED)
- No risk ID appears more than once across any status group
- No risk appears in both MANDATORY and EXCLUDED
- All related_assumption IDs are governed IDs (traceable to approved assumption packs)

---

## 5. Naming Convention

```
SELECTED_RISK_REGISTER_[TenderID].md
```

Where `[TenderID]` is the `tender_id` field from the context, with hyphens and spaces replaced by underscores.

Files are written to `08_Commercial/Reports/`.

---

## 6. Amendment History

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-06-29 | Initial standard — PF2-001 |
