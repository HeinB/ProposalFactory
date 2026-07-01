---
document_id: SECTION-TRACEABILITY-STANDARD-V1
title: "Section Traceability Standard"
version: "1.0"
status: "APPROVED"
created: "2026-06-29"
created_by: "PF2-003 — Proposal Section Assembly Engine"
approved_by: "PF2-003"
approved_date: "2026-06-29"
approved_for_reuse: true
category: "Standard / Traceability"
scope: "Defines the traceability requirements for the Proposal Section Assembly Engine: how every section inclusion/exclusion decision must be traced back to its source rule, source asset, and governance constraint."
---

# Section Traceability Standard

**Work Package:** PF2-003  
**Date:** 2026-06-29  
**Version:** 1.0  
**Status:** APPROVED

---

## 1. Purpose

Every section in a proposal must be explainable. The Proposal Factory must be able to answer, for any proposal section:

- **Why it exists** — which rule, asset, or mandatory class triggered inclusion
- **Why it does not exist** — which exclusion rule or pattern removed it
- **Which assets contributed** — traceability back to the Knowledge Asset Registry
- **Which governance rules applied** — which Section Integrity rules, ADR decisions, or GOV constraints were enforced

This standard defines how traceability is captured in the Section Manifest and reported in the Section Traceability Report.

---

## 2. Traceability Chain

```
Tender Context
    ↓
AREL Rule Evaluation (ARE engine)
    ↓
Asset Selection (MANDATORY / OPTIONAL_SELECTED / EXCLUDED / DEFAULT_EXCLUDED)
    ↓
Section Driver Evaluation (PSAE)
    ↓
Section Inclusion Decision (with rationale)
    ↓
Governance Constraint Application (SI rules, GOV rules, ADRs)
    ↓
Section Manifest Entry (source_assets, si_rules_applied, governance_constraints)
    ↓
Section Traceability Report
```

---

## 3. Traceability Fields

Every `SectionEntry` in the Section Manifest (see SECTION_MANIFEST_STANDARD.md) carries:

| Field | Traceability Purpose |
|---|---|
| `include_status` | Final decision |
| `rationale` | Plain-English explanation of the decision rule that triggered the status |
| `source_assets` | Registry asset IDs (CAP/ASP) that contribute content; empty if no registry asset drives the section |
| `si_rules_applied` | Identifies which Section Integrity rules (SI-001 to SI-007) constrain this section |
| `governance_constraints` | Active governance restrictions (GOV-010 Mining, ADR-001, OAR flags, named-entity rules) |
| `human_input_required` | Flags human review requirement; `human_input_notes` explains what is needed |

---

## 4. Rationale Format

The `rationale` string must follow one of these patterns:

| Decision | Rationale Pattern |
|---|---|
| M-ALL mandatory | `"M-ALL — mandatory in all proposals"` |
| M-FIXED mandatory | `"M-FIXED — mandatory in all fixed-price proposals"` |
| M-SA mandatory | `"M-SA — mandatory for South African entities"` |
| AMS excluded | `"EXCLUDED — AMS Pattern 13 excludes [section_id]"` or `"EXCLUDED — AMS Pattern 13 exclusion; SI-001 applies"` |
| AMS-only excluded | `"EXCLUDED — [section_id] applies to AMS engagements only"` |
| Platform conditional | `"COND-[TYPE] — platform=[value]; drivers: [asset_list]"` |
| Asset-driven mandatory | `"[COND-TYPE] — drivers: [asset_id_list]"` (mandatory_class driver assets MANDATORY) |
| Asset-driven optional | `"[COND-TYPE] — drivers: [asset_id_list]"` (driver assets OPTIONAL_SELECTED) |
| Default excluded | `"[COND-TYPE] — no driver assets selected"` |
| OPT not triggered | `"OPT — no condition triggered; not in scope"` |

---

## 5. Source Asset Traceability

For every included section, `source_assets` lists only assets with status `MANDATORY` or `OPTIONAL_SELECTED` in the AREL selection that contribute to that section via the `ASSET_TO_SECTIONS` mapping.

**Traceability guarantee:** Any asset listed in `source_assets` can be:
1. Located by `asset_id` in the Knowledge Asset Registry
2. Its AREL selection status verified in the ARE engine output
3. Its assembly rule (`mandatory_if` / `optional_if` / `excluded_if`) read from the registry

This creates a full chain: tender context → AREL evaluation → asset status → section inclusion.

---

## 6. Governance Constraint Traceability

The following governance constraints must be explicitly encoded in the manifest when they apply:

| Constraint | When Applied | Source |
|---|---|---|
| ADR-001: No CV from KB | S-47, S-48, A-02 always | `si_rules_applied: [ADR-001]` |
| GOV-010 / G-001 Mining | W3S1-005 / HCM-COMPENSATION | ARE AREL exclusion; reflected in asset not selected |
| B-BBEE expiry 2026-07-31 | S-59, S-12, A-05 | `governance_constraints` + `governance_flags` |
| SI-001: S-38 AMS exclusion | S-38 for AMS | `si_rules_applied: [SI-001]` on S-38, S-73 |
| SI-006: S-49 before S-52 | S-49, S-52 always | `si_rules_applied: [SI-006]` |
| SI-007: S-71/S-72 boundaries | S-71, S-72 for AMS | `si_rules_applied: [SI-001, SI-007]` |
| Named-entity restrictions | S-09, S-17, S-67, S-68 | `governance_constraints` notes |

---

## 7. Section Traceability Report

**File:** `08_Commercial/Reports/SECTION_TRACEABILITY_REPORT.md`  
**Generated by:** `proposal_section_engine.py --regression`

The report contains, for every scenario, a full table of all 82 sections with:
- Include status
- Rationale (the rule that decided)
- Source assets (what drove the content)
- SI rules applied

This enables any reviewer to reconstruct the assembly decision without running the engine.

---

## 8. Traceability Requirements for Production Use

Before any manifest is used to assemble a proposal for submission:

| Requirement | Check |
|---|---|
| `validation_status: PASS` | No VAL-001 to VAL-005 failures |
| All MANDATORY sections have source assets or are M-ALL template/compliance sections | Verify source_assets is non-empty or section is a template/compliance section |
| All PLACEHOLDER sections have placeholders list populated | Renderer must supply each placeholder before submission |
| `governance_flags` reviewed | BU Lead or AM must confirm B-BBEE, ADR-001, and other flags |
| Human-review sections signed off | All `human_input_required: true` sections reviewed by appropriate authority |

---

## 9. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-29 | PF2-003 | Initial standard |

---

*SECTION_TRACEABILITY_STANDARD.md v1.0 | PF2-003 — Proposal Section Assembly Engine | 2026-06-29*
