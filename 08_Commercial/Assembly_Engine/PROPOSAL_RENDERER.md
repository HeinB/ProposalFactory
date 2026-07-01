---
document_id: PROPOSAL-RENDERER-V1
title: "Proposal Renderer — Architecture and Operation"
version: "1.0"
status: "APPROVED"
created: "2026-06-29"
created_by: "PF2-004 — Markdown Proposal Renderer"
approved_by: "PF2-004"
approved_date: "2026-06-29"
approved_for_reuse: true
category: "Architecture / Engine Documentation"
scope: "Documents the design, inputs, outputs, processing logic, and governance of the Markdown Proposal Renderer (proposal_renderer.py)."
---

# Proposal Renderer — Architecture and Operation

**Work Package:** PF2-004  
**Date:** 2026-06-29  
**Version:** 1.0  
**Status:** APPROVED

---

## 1. Purpose

The Proposal Renderer is the final assembly engine in the APPSolve Proposal Factory. It consumes the certified Proposal Section Manifest produced by the Proposal Section Assembly Engine (PSAE) and the governed source assets approved in `07_Approved_Content/Approved/`, and produces:

1. A complete, ordered **Markdown proposal document** (`PROPOSAL_RENDERED_[tender_id].md`)
2. A full **render audit report** (`PROPOSAL_RENDER_AUDIT_[tender_id].md`) with per-section traceability

The renderer performs **no AI-authored content generation**. All text in the rendered proposal is sourced from:
- Governed approved assets (KB-approved .md files)
- Structured templates (cover page, TOC)
- Placeholder markers (for human completion)
- AI-draft markers (signalling that AI-assisted drafting is needed, with mandatory human review)

---

## 2. Position in the Proposal Factory

```
Tender Context
    ↓
KRPE (Registry Population)
    ↓
KVE (Validation Engine)
    ↓
ARE (Assembly Rule Engine)     ← asset selection
    ↓
PSAE (Section Assembly Engine) ← section orchestration
    ↓
RSE (Risk Selection Engine)
    ↓
[Proposal Renderer]            ← THIS ENGINE
    ↓
PROPOSAL_RENDERED_[tender].md
PROPOSAL_RENDER_AUDIT_[tender].md
```

**Inputs consumed:**
- `08_Commercial/Proposals/[tender_id]/PROPOSAL_SECTION_MANIFEST_[tender_id].yaml` (from PSAE)
- `07_Approved_Content/Approved/**/*.md` (governed source assets)
- No direct access to the Knowledge Asset Registry

**Outputs produced:**
- `08_Commercial/Proposals/[tender_id]/PROPOSAL_RENDERED_[tender_id].md`
- `08_Commercial/Proposals/[tender_id]/PROPOSAL_RENDER_AUDIT_[tender_id].md`

---

## 3. Engine Components

### 3.1 AssetIndex

Scans `07_Approved_Content/Approved/` on startup and builds a lookup dictionary:

```
{asset_id: absolute_file_path}
```

Indexes both **canonical IDs** (full file stem, e.g. `W1S1-001-CORP-CompanyOverview`) and **short prefix IDs** (e.g. `W1S1-001`) extracted by the rule: *take all hyphen-separated segments up to and including the first all-digit segment*.

This dual-indexing ensures that manifests using either ID form resolve correctly to the governed asset file.

### 3.2 Content Pipeline

For each source `.md` file read from the Asset Index:

1. **Strip YAML frontmatter** — remove the leading `--- ... ---` block
2. **Strip approval banners** — remove `> **Approved...**` lines and following `---` dividers
3. **Strip internal trailing sections** — remove sections marked with known internal markers (pre-tender checks, review notes, approval records, extraction documentation)
4. **Demote headings** — promote all ATX headings down by 2 levels (`#` → `###`, `##` → `####`, etc.) so body content sits correctly under the section's `##` heading

### 3.3 Section Renderer

Dispatches each section to a rendering function based on `assembly_method`:

| Assembly Method | Rendering Action |
|---|---|
| `DIRECT` | Load primary source asset; strip and demote; insert body |
| `MERGE` | Load all source assets in order; strip and demote each; concatenate |
| `EXTRACT` | Load primary source asset; insert full body + audit note (sub-section extraction not automated) |
| `TEMPLATE` | Generate structured template with `{{placeholder}}` markers |
| `AI-GENERATE` | Insert `<!-- AI-DRAFT REQUIRED -->` comment + human action callout |
| `PLACEHOLDER` | Insert `<!-- PLACEHOLDER -->` comment + human action callout |

Sections with `include_status` not in `{MANDATORY, OPTIONAL_SELECTED}` are skipped (not rendered).

### 3.4 TOC Generator

After all sections are processed, builds a Markdown bullet list TOC from the ordered section names. Sections S-01 and S-02 are excluded from the TOC. Appendix sections are indented under main sections.

### 3.5 Audit Reporter

Produces a structured Markdown audit file with:
- Render summary counts (RENDERED / PLACEHOLDER / AI-DRAFT / NOT_FOUND / SKIPPED)
- Governance flags from the manifest
- Per-section audit table (82 rows)
- Governance constraint detail by section
- Asset Not Found register
- Human Action register (all sections requiring completion)

---

## 4. Document Structure

The rendered proposal follows this structure:

```
<!-- metadata comments -->
<!-- governance flags (prominent callout) -->

# Cover Page / Transmittal        (S-01, TEMPLATE)

## Table of Contents               (S-02, auto-generated)

## 1. [Section Name]               (first included section after TOC)
### [sub-heading from asset]
#### [sub-sub-heading]
...

## N. [Section Name]               (last main section)

## Appendix A — [Name]             (A-01)
## Appendix B — [Name]             (A-02)
...

<!-- render summary footer -->
```

### Heading Levels

| Context | Level | Example |
|---|---|---|
| Cover page | `#` | `# Cover Page / Transmittal` |
| Proposal section heading | `##` | `## 1. Company Overview` |
| Appendix heading | `##` | `## Appendix A — Complete Assumption Schedule` |
| Asset body top-level | `###` | `### APPSolve Company Overview` |
| Asset body sub-section | `####` | `#### Our Approach` |
| Asset body sub-sub-section | `#####` | `##### Detail` |

---

## 5. Governance Enforcement

### 5.1 Governance Flags

All `governance_flags` from the Section Manifest are displayed as a prominent callout block immediately after the document metadata header, before the cover page. This ensures flags are never buried.

### 5.2 Section-Level Governance

Each section's `governance_constraints` and `si_rules_applied` are emitted as HTML comments inline with the section content. They are invisible in rendered Markdown output but preserved in the raw source for audit.

### 5.3 Internal Content Stripping

The following patterns are detected and stripped from asset body content before inclusion in the proposal:

| Pattern | Description |
|---|---|
| `(Internal — Not for Tender Use)` | Section explicitly marked internal |
| `**Pre-tender ...` | Pre-tender checklist or confirmation |
| `**Review notes:` | Extraction review notes |
| `## Approval Record` | Asset approval record |
| `**File location:` | Internal file reference |
| `Extraction Documentation (Internal` | KB extraction documentation |

When a stripping marker is found, the renderer also removes any preceding `---` divider that separated the internal section.

---

## 6. Known Gaps and Limitations

| Gap | Description | Priority |
|---|---|---|
| ASP assumption pack content | `OIC-ASSUMPTIONS-V1`, `AMS-ASSUMPTIONS-V1` not yet materialised as .md files; sections render as NOT_FOUND | High |
| EXTRACT sub-section automation | EXTRACT method inserts full asset body; sub-section tagging and extraction not yet automated | Medium |
| S-37 RAID / Risk Register | Risk selections from RSE not yet fed into renderer for Risk Register generation | Medium |
| Word/PDF export | Renderer produces Markdown only; Word/PDF conversion not implemented | Low |
| Dynamic TOC anchors | TOC bullet list does not generate clickable Markdown anchor links | Low |

---

## 7. CLI Usage

```bash
# Render a specific tender
python3 proposal_renderer.py --tender ARM-IT045

# Run full regression (ARM-IT045 full + 5 smoke tests)
python3 proposal_renderer.py --regression

# Render all regression tenders
python3 proposal_renderer.py --all

# Use a custom content root
python3 proposal_renderer.py --tender ARM-IT045 --content-root /path/to/Approved
```

---

## 8. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-29 | PF2-004 | Initial architecture document |

---

*PROPOSAL_RENDERER.md v1.0 | PF2-004 — Markdown Proposal Renderer | 2026-06-29*
