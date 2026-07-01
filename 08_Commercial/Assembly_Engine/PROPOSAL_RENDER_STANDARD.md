---
document_id: PROPOSAL-RENDER-STANDARD-V1
title: "Proposal Render Standard"
version: "1.0"
status: "APPROVED"
created: "2026-06-29"
created_by: "PF2-004 — Markdown Proposal Renderer"
approved_by: "PF2-004"
approved_date: "2026-06-29"
approved_for_reuse: true
category: "Standard / Rendering"
scope: "Defines the format rules, heading conventions, frontmatter handling, placeholder syntax, and rendering requirements for all proposals produced by the Proposal Renderer."
---

# Proposal Render Standard

**Work Package:** PF2-004  
**Date:** 2026-06-29  
**Version:** 1.0  
**Status:** APPROVED

---

## 1. Purpose

This standard defines the rules that the Proposal Renderer (proposal_renderer.py) must follow when assembling a governed proposal from a Section Manifest and approved source assets. It is the authoritative reference for output format consistency.

---

## 2. Input Requirements

| Input | Source | Requirement |
|---|---|---|
| Section Manifest | PSAE output | `validation_status: PASS`; `manifest_id` present |
| Source assets | `07_Approved_Content/Approved/` | `lifecycle_status: APPROVED`; `approved_for_reuse: Yes` |
| Tender context | Manifest metadata | `tender_id`, `platform`, `engagement_type` |

**The renderer must not:**
- Access the Knowledge Asset Registry directly
- Bypass PSAE (manifests must pre-exist from PSAE output)
- Read assets from `Candidate_Content/` or `Review_Required/`
- Generate proposal content using AI (AI markers flag where human drafting is needed)

---

## 3. Output Files

| File | Location | Description |
|---|---|---|
| `PROPOSAL_RENDERED_[tender_id].md` | `08_Commercial/Proposals/[tender_id]/` | Complete assembled proposal |
| `PROPOSAL_RENDER_AUDIT_[tender_id].md` | `08_Commercial/Proposals/[tender_id]/` | Per-section render audit |

---

## 4. Frontmatter Stripping

All approved `.md` assets contain YAML frontmatter and administrative content that must be stripped before the asset body is included in the proposal.

### 4.1 Leading stripping sequence (applied in order)

1. Remove the YAML frontmatter block: everything from the first `---` to the closing `---` (inclusive)
2. Remove blank lines
3. Remove approval banner lines starting with `>` (e.g. `> **Approved for tender reuse**`)
4. Remove horizontal dividers (`---`)
5. Remove further blank lines

The first non-blank, non-quote, non-divider line after these passes is the first line of the renderable body.

### 4.2 Trailing internal section stripping

The following markers signal the start of internal-only content. When detected, all content from the marker (or from the preceding `---` divider) to the end of the file is stripped:

| Marker (startswith / contains) | Description |
|---|---|
| `**Pre-tender ...` (startswith) | Pre-tender checklist or confirmation section |
| `**Review notes:` (startswith) | KB extraction review notes |
| `**File location:` (startswith) | Internal asset path reference |
| `## Approval Record` (startswith) | Asset governance approval record |
| `Internal — Not for Tender Use` (contains) | Section explicitly flagged internal |
| `Extraction Documentation (Internal` (contains) | KB extraction documentation |

---

## 5. Heading Convention

### 5.1 Document-level headings

| Level | Usage | Example |
|---|---|---|
| `#` | Cover page only (S-01) | `# Cover Page / Transmittal` |
| `##` | Proposal sections (numbered) | `## 1. Company Overview` |
| `##` | Appendix sections | `## Appendix A — Complete Assumption Schedule` |

### 5.2 Asset body heading demotion

All ATX headings in source asset bodies are demoted by 2 levels before inclusion:

| Source heading | Rendered heading |
|---|---|
| `# Heading` | `### Heading` |
| `## Sub-heading` | `#### Sub-heading` |
| `### Sub-sub-heading` | `##### Sub-sub-heading` |
| `#### Detail` | `###### Detail` |

This ensures body content sits at heading level 3+ under the section's level-2 heading, maintaining consistent document hierarchy.

### 5.3 Section numbering

Sections are numbered sequentially from 1 in assembly order, excluding:
- S-01 (Cover Page — no sequence number)
- S-02 (Table of Contents — no sequence number)
- Appendix sections (A-01 to A-06 — use label format)

Sequence numbers are not the section's `assembly_order` field from the manifest; they reflect the proposal position within the rendered document.

---

## 6. Placeholder Syntax

Placeholders mark fields requiring human completion before submission.

### 6.1 Inline placeholders

Used in TEMPLATE sections:

```
`{{field_name}}`
```

Examples:
- `{{tender_title}}`
- `{{client_name}}`
- `{{submission_date}}`
- `{{rfp_reference}}`

### 6.2 Section-level placeholders (PLACEHOLDER method)

```markdown
<!-- PLACEHOLDER: Section Name -->
<!-- [instruction or note] -->

> **Action Required:** [instruction]

**Fields to complete:**
- `{{field_1}}`
- `{{field_2}}`
```

### 6.3 AI-draft markers (AI-GENERATE method)

```markdown
<!-- AI-DRAFT REQUIRED: Section Name -->
<!-- Instruction: [tailoring instruction] -->

> **AI-Draft Required:** This section requires AI-assisted drafting with mandatory human review.
>
> *[instruction]*

_[AI-generated content to be inserted here — must be reviewed and approved before submission]_
```

### 6.4 Not Found markers

When a referenced asset is not in the Asset Index:

```markdown
<!-- NOT_FOUND: asset_id -->

> **Content Not Found:** Governed asset `asset_id` not located in the Asset Index.
> Add to `07_Approved_Content/Approved/` before submission.
```

---

## 7. Governance Formatting

### 7.1 Document-level flags

All `governance_flags` and `validation_warnings` from the Section Manifest appear as a prominent callout block immediately before the Cover Page:

```markdown
---

> **GOVERNANCE FLAGS — Review before submission:**
> - [flag 1]
> - [flag 2]
> - WARNING: [warning]

---
```

### 7.2 Section-level constraints

Per-section `governance_constraints` and `si_rules_applied` are emitted as HTML comments after the section heading. They do not appear in rendered Markdown output:

```markdown
<!-- GOVERNANCE -->
<!-- GOV: [constraint text] -->
<!-- SI-RULE: [rule ID] -->
```

### 7.3 Human review callouts

When `human_input_required: true` for a RENDERED section (not already a PLACEHOLDER or AI-DRAFT):

```markdown
> **Human Review Required:** [human_input_notes text]
```

---

## 8. Table of Contents

The TOC is generated after the first rendering pass from all included sections in assembly order:

- Format: unordered Markdown list (`-`)
- Main sections: `- {seq}. {Section Name}`
- Appendix sections: indented `  - Appendix {Label} — {Section Name}`
- Sections S-01 and S-02 not listed in TOC
- TOC replaces the `__TOC_PLACEHOLDER__` marker in the document after the first pass

---

## 9. Document Footer

Every rendered proposal ends with:

```markdown
---

<!-- RENDER SUMMARY -->
<!-- Rendered: [ISO timestamp] | Renderer v[version] -->
<!-- RENDERED=[n] | PLACEHOLDER=[n] | AI-DRAFT=[n] | NOT_FOUND=[n] | SKIPPED=[n] -->

*End of document — assembled by APPSolve Proposal Factory v1.0*
```

---

## 10. Render Status Enum

| Status | Meaning |
|---|---|
| `RENDERED` | Content populated from a governed source asset or template |
| `PLACEHOLDER` | Human input required; content not yet available |
| `AI-DRAFT` | AI-assisted draft required; mandatory human review before submission |
| `NOT_FOUND` | Referenced asset not found in AssetIndex; treat as PLACEHOLDER |
| `SKIPPED` | Section excluded from assembly sequence; not rendered |

---

## 11. Validation Requirements

Before a rendered proposal may be submitted:

| Check | Requirement |
|---|---|
| Zero NOT_FOUND in submitted sections | All MANDATORY source assets must be present in index |
| All PLACEHOLDER sections completed | Reviewer must provide content for every PLACEHOLDER |
| All AI-DRAFT sections reviewed | AI-generated content reviewed and approved by AM/BU Lead |
| Governance flags acknowledged | BU Lead or AM sign-off on all `governance_flags` |
| Human input sections signed off | All `human_input_required: true` sections verified |
| PROPOSAL_RENDER_AUDIT retained | Audit file must be retained alongside submission |

---

## 12. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-29 | PF2-004 | Initial standard |

---

*PROPOSAL_RENDER_STANDARD.md v1.0 | PF2-004 — Markdown Proposal Renderer | 2026-06-29*
