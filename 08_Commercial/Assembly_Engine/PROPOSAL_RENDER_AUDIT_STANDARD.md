---
document_id: PROPOSAL-RENDER-AUDIT-STANDARD-V1
title: "Proposal Render Audit Standard"
version: "1.0"
status: "APPROVED"
created: "2026-06-29"
created_by: "PF2-004 — Markdown Proposal Renderer"
approved_by: "PF2-004"
approved_date: "2026-06-29"
approved_for_reuse: true
category: "Standard / Audit"
scope: "Defines the schema and requirements for the Proposal Render Audit file produced by the Proposal Renderer for every rendered tender."
---

# Proposal Render Audit Standard

**Work Package:** PF2-004  
**Date:** 2026-06-29  
**Version:** 1.0  
**Status:** APPROVED

---

## 1. Purpose

Every proposal rendered by the Proposal Renderer must be accompanied by a **Render Audit** file. The audit provides complete per-section traceability from the Section Manifest through to the rendered output, enabling any reviewer to:

- Verify that every included section was populated from a governed source
- Identify sections requiring human completion before submission
- Confirm that governance constraints were applied
- Trace every rendered asset back to its source file

The audit file is a governance document — it must be retained alongside the submitted proposal.

---

## 2. Audit File Naming and Location

| Field | Value |
|---|---|
| Filename | `PROPOSAL_RENDER_AUDIT_[tender_id].md` |
| Location | `08_Commercial/Proposals/[tender_id]/` |
| Produced by | `proposal_renderer.py` automatically on every render run |

---

## 3. Audit File Schema

### 3.1 Frontmatter

```yaml
---
document_id: RENDER-AUDIT-[tender_id]-V1
title: "Proposal Render Audit — [tender_id]"
version: "1.0"
status: "COMPLETE"
rendered_at: "[ISO 8601 timestamp]"
renderer_version: "[n.n]"
manifest_id: "[manifest_id from PSAE]"
---
```

### 3.2 Section 1 — Render Summary

Aggregate counts for the render run:

| Metric | Description |
|---|---|
| Sections in manifest | Total 82-section universe |
| Assembly sequence length | Sections included in render sequence |
| RENDERED | Sections populated from governed assets or templates |
| PLACEHOLDER | Sections awaiting human content |
| AI-DRAFT | Sections requiring AI-assisted drafting with human review |
| NOT_FOUND | Sections where referenced assets were not in AssetIndex |
| SKIPPED | Sections excluded from assembly sequence |

### 3.3 Section 2 — Governance Flags

All `governance_flags` from the Section Manifest, listed verbatim. These are the same flags displayed in the rendered proposal header.

### 3.4 Section 3 — Section Audit Trail

A table with one row per section (all 82 sections, plus SKIPPED entries for excluded sections):

| Column | Description |
|---|---|
| Section | Section ID (S-01 to S-76, A-01 to A-06) |
| Name | Section name |
| Status | `include_status` from manifest |
| Render Status | `RENDERED` / `PLACEHOLDER` / `AI-DRAFT` / `NOT_FOUND` / `SKIPPED` |
| Method | `assembly_method` from manifest |
| Assets Found | Filename(s) of source assets successfully loaded |
| Assets Missing | Asset ID(s) not found in AssetIndex |
| Notes | Render engine notes for this section |

### 3.5 Section 4 — Governance Constraint Detail

For each section with non-empty `governance_constraints`, lists all constraints verbatim. Enables targeted review of sections carrying governance obligations.

### 3.6 Section 5 — Asset Not Found Register

Lists all sections where at least one referenced asset was not found in the AssetIndex:

| Column | Description |
|---|---|
| Section | Section ID |
| Asset ID | The asset ID not found |
| Impact | How the missing asset affected the render (e.g. `PLACEHOLDER rendered`) |

An empty register confirms all referenced assets were resolved.

### 3.7 Section 6 — Human Action Register

Lists all sections with `render_status` in `{PLACEHOLDER, AI-DRAFT, NOT_FOUND}`. These are the sections requiring human completion before the proposal may be submitted:

| Column | Description |
|---|---|
| Section | Section ID |
| Name | Section name |
| Render Status | The status requiring action |
| Action Required | Engine note describing what is needed |

---

## 4. AuditEntry Schema

The `AuditEntry` data class produced by the renderer for each section:

| Field | Type | Description |
|---|---|---|
| `section_id` | str | Section identifier (S-01, A-01, etc.) |
| `section_name` | str | Human-readable section name |
| `include_status` | str | From manifest: MANDATORY / OPTIONAL_SELECTED / EXCLUDED / DEFAULT_EXCLUDED |
| `render_status` | str | RENDERED / PLACEHOLDER / AI-DRAFT / NOT_FOUND / SKIPPED |
| `assembly_method` | str | From manifest: DIRECT / MERGE / EXTRACT / TEMPLATE / AI-GENERATE / PLACEHOLDER |
| `source_files` | List[str] | Absolute paths of governed .md files loaded |
| `assets_found` | List[str] | Asset IDs successfully resolved in AssetIndex |
| `assets_not_found` | List[str] | Asset IDs not in AssetIndex |
| `governance_constraints` | List[str] | Governance constraints from manifest |
| `si_rules_applied` | List[str] | SI rule IDs applied to this section |
| `notes` | str | Renderer notes explaining the render decision |

---

## 5. Traceability Chain

The audit file enables full reconstruction of any section's render decision:

```
Section Manifest (PSAE output)
    ↓ include_status / source_assets / assembly_method
Render decision
    ↓ AssetIndex lookup
Source file(s) loaded / missing
    ↓ strip_frontmatter + demote_headings
Body content inserted into proposal
    ↓
render_status recorded in AuditEntry
    ↓
Audit trail table row
```

For any MANDATORY section with `render_status: NOT_FOUND`, the audit provides the asset_id(s) that need to be added to `07_Approved_Content/Approved/` to resolve the gap.

---

## 6. Audit Retention Requirements

| Requirement | Description |
|---|---|
| Retain with submission | The audit file must accompany or be filed with the submitted proposal |
| Traceability reference | Reviewers must be able to produce the audit on demand for any submitted proposal |
| Governance review | BU Lead or AM must review Section 6 (Human Action Register) before submission |
| Version alignment | The audit file must match the submitted PROPOSAL_RENDERED_*.md (same `rendered_at` timestamp) |

---

## 7. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-29 | PF2-004 | Initial standard |

---

*PROPOSAL_RENDER_AUDIT_STANDARD.md v1.0 | PF2-004 — Markdown Proposal Renderer | 2026-06-29*
