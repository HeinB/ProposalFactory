---
document_id: SECTION-MANIFEST-STANDARD-V1
title: "Section Manifest Standard"
version: "1.0"
status: "APPROVED"
created: "2026-06-29"
created_by: "PF2-003 — Proposal Section Assembly Engine"
approved_by: "PF2-003"
approved_date: "2026-06-29"
approved_for_reuse: true
category: "Standard / Schema Definition"
scope: "Defines the canonical schema for the Proposal Section Manifest YAML produced by the PSAE. Governs field names, types, enumerated values, and validation requirements."
---

# Section Manifest Standard

**Work Package:** PF2-003  
**Date:** 2026-06-29  
**Version:** 1.0  
**Status:** APPROVED

---

## 1. Purpose

This standard defines the schema for `PROPOSAL_SECTION_MANIFEST_[TENDER_ID].yaml` — the primary output of the Proposal Section Assembly Engine. Every downstream consumer (Proposal Renderer, QA checker, human reviewer) reads this manifest to understand the complete section assembly plan for a tender.

---

## 2. File Naming and Location

| Property | Value |
|---|---|
| Filename | `PROPOSAL_SECTION_MANIFEST_[TENDER_ID].yaml` |
| Location | `08_Commercial/Proposals/[TENDER_ID]/` |
| Encoding | UTF-8 |
| Format | YAML (PyYAML `dump` — block style) |
| Producer | `proposal_section_engine.py` v1.0+ |

---

## 3. Top-Level Schema

```yaml
manifest_id:    string          # Unique manifest ID: [TENDER_ID]-PSM-[YYYYMMDD-HHMMSS]
tender_id:      string          # Tender identifier (e.g., ARM-IT045)
tender_pattern: string          # Pattern number (e.g., "13")
platform:       string          # Platform name (canonical AREL value)
engagement_type: string         # "Implementation" | "AMS"
industry:       string          # Industry context (e.g., "Mining", "Banking")
generated_at:   ISO8601         # UTC timestamp of generation
engine_version: string          # PSAE version (e.g., "1.0")

summary:
  mandatory_sections:        int
  optional_sections:         int
  excluded_sections:         int
  default_excluded_sections: int
  total_sections:            int    # Always 82
  assembly_sequence_length:  int    # Count of included sections
  validation_status:         string # "PASS" | "FAIL"

assembly_sequence: [string, ...]  # Ordered list of included section IDs

validation_errors:   [string, ...]   # VAL-001 to VAL-005 failures
validation_warnings: [string, ...]   # Non-blocking warnings
governance_flags:    [string, ...]   # Governance reminders (B-BBEE, ADR-001, etc.)

sections:
  [section_id]: SectionEntry
  ...
```

---

## 4. SectionEntry Schema

```yaml
section_id:     string    # e.g., "S-16"
section_name:   string    # Human-readable name
include_status: enum      # See §5
rationale:      string    # Plain-English explanation of the inclusion decision
assembly_order: int       # 0 = not in sequence; 1..N = position in assembly_sequence
assembly_method: enum     # See §6
merge_strategy: string    # Instructions for MERGE method; "N/A" otherwise
source_assets:  [string]  # CAP/ASP asset IDs that contribute content (selected assets only)
placeholders:   [string]  # Named placeholders requiring human-supplied content
human_input_required: bool
human_input_notes: string # Specific instructions for the human reviewer/author
renderer_metadata:
  section_type:    string   # optional — "cover", "toc", etc.
  page_break_before: bool   # optional
  automation_pct:  int      # 0–100 current automation percentage
  ai_assisted:     bool     # optional
  gap:             string   # optional — gap description
governance_constraints: [string]   # Active governance rules for this section
si_rules_applied:       [string]   # SI-001, SI-005, SI-006, SI-007, ADR-001
```

---

## 5. `include_status` Enumerated Values

| Value | Meaning |
|---|---|
| `MANDATORY` | Section must appear in the proposal; sourced from a rule or M-ALL/M-FIXED designation |
| `OPTIONAL_SELECTED` | Section is in scope based on tender context; may be deselected by bid manager |
| `EXCLUDED` | Section is explicitly excluded by a governance rule (e.g., AMS exclusion, platform mismatch) |
| `DEFAULT_EXCLUDED` | Section has no rule triggering it; not applicable to this tender |

Only `MANDATORY` and `OPTIONAL_SELECTED` sections appear in `assembly_sequence`.

---

## 6. `assembly_method` Enumerated Values

| Value | Meaning |
|---|---|
| `DIRECT` | Content taken verbatim from a single source asset |
| `EXTRACT` | Specific sub-sections extracted from one or more source documents |
| `MERGE` | Multiple assets combined; primary asset first, secondary assets appended |
| `TEMPLATE` | Fill-in-the-blank template; placeholders must be populated |
| `AI-GENERATE` | Content requires AI generation with human review |
| `PLACEHOLDER` | Content not yet available or requires external input (e.g., pricing, CVs) |

---

## 7. `merge_strategy` Values (for MERGE method)

| Pattern | Value |
|---|---|
| Standard capability merge | `"Ordered concatenation; primary asset first; secondary assets appended by module selection order"` |
| Extract from sub-sections | `"Extract designated sub-sections from source documents"` |
| Non-MERGE sections | `"N/A"` |

---

## 8. Canonical Platform Values

These values must match AREL V1.0 platform variable vocabulary:

| Platform | Canonical Value |
|---|---|
| Oracle HCM Cloud | `"Oracle HCM Cloud"` |
| Oracle ERP Cloud | `"Oracle ERP Cloud"` |
| Oracle EBS | `"Oracle EBS"` |
| Oracle Integration Cloud | `"Oracle Integration Cloud"` |
| Acumatica | `"Acumatica"` |
| BeBanking | `"BeBanking"` |

---

## 9. Canonical Engagement Type Values

| Engagement Type | Canonical Value |
|---|---|
| Fixed-price implementation | `"Implementation"` |
| Application managed services | `"AMS"` |

---

## 10. Validation Rules

All manifests must satisfy:

| Rule | Check |
|---|---|
| VAL-001 | All M-ALL sections have `include_status: MANDATORY` (excluding AMS-excluded sections for AMS proposals) |
| VAL-002 | `assembly_sequence` contains no duplicate section IDs |
| VAL-003 (SI-006) | S-49 appears at a lower index than S-52 in `assembly_sequence` |
| VAL-004 (SI-007) | S-71 and S-72 both MANDATORY when `engagement_type: AMS` |
| VAL-005 | `total_sections == 82` (all sections represented in the `sections` block) |

---

## 11. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-29 | PF2-003 | Initial standard |

---

*SECTION_MANIFEST_STANDARD.md v1.0 | PF2-003 — Proposal Section Assembly Engine | 2026-06-29*
