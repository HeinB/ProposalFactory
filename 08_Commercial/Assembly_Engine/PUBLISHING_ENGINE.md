---
document_id: PUBLISHING-ENGINE-V1
title: "Proposal Publishing Engine — Architecture (PF2-007)"
version: "1.0"
status: "APPROVED"
created: "2026-06-30"
created_by: "PF2-007 — Proposal Publishing Engine"
approved_by: "PF2-007"
approved_date: "2026-06-30"
category: "Architecture Document"
scope: "Defines the architecture, publication profiles, section classification model, and rendering pipeline of the Proposal Publishing Engine (ppe.py)."
---

# Proposal Publishing Engine — Architecture

**Version:** 1.0  
**Date:** 2026-06-30  
**Status:** APPROVED  
**Platform Maturity:** L5.8 → **L5.9**

---

## 1. Purpose

The Proposal Publishing Engine (PPE) consumes a rendered Proposal Factory Markdown file and a Section Manifest YAML and produces audience-specific Microsoft Word (DOCX) outputs. It is the final stage of the Proposal Factory pipeline.

The PPE enforces a strict rule: **it never changes governed content.** It may remove internal metadata, convert comment markers to callouts, and apply publication profile rules. It must not rewrite technical content, invent proposal content, or alter approved knowledge assets.

---

## 2. Position in the Pipeline

```
Knowledge Registry (KRPE)
         │
         ▼
Knowledge Validation Engine (KVE)
         │
         ▼
Assembly Rule Enrichment Engine (ARE)
         │
         ▼
Risk Selection Engine (RSE)
         │
         ▼
Proposal Section Assembly Engine (PSAE) ──▶ Section Manifest YAML
         │
         ▼
Markdown Proposal Renderer ──▶ PROPOSAL_RENDERED_<ID>.md
         │
         ▼
Proposal Publishing Engine (PPE / ppe.py)
         │
         ├──▶ <ID>_PROPOSAL_CLIENT_V2.docx
         ├──▶ <ID>_PROPOSAL_INTERNAL_REVIEW.docx
         ├──▶ <ID>_PROPOSAL_TRACEABILITY.docx
         └──▶ <ID>_PROPOSAL_REVIEW_REPORT.docx
```

The PPE imports rendering primitives from `docx_renderer.py` (PF2-004A) and extends them with publication profile logic.

---

## 3. Inputs

| Input | Source | Required |
|---|---|---|
| `PROPOSAL_RENDERED_<ID>.md` | Markdown Renderer (PF2-004) | Yes |
| `PROPOSAL_SECTION_MANIFEST_<ID>.yaml` | PSAE (PF2-003) | Yes |
| Tender ID | CLI argument | Yes |

---

## 4. Outputs

| Output | Profile | Audience |
|---|---|---|
| `<PREFIX>_CLIENT_V2.docx` | CLIENT | Plennegy Group / external client |
| `<PREFIX>_INTERNAL_REVIEW.docx` | INTERNAL | APPSolve BU Lead + AM |
| `<PREFIX>_TRACEABILITY.docx` | TRACEABILITY | Governance audit record |
| `<PREFIX>_REVIEW_REPORT.docx` | REVIEW | APPSolve quality assurance |

---

## 5. Core Components

### 5.1 Markdown Parser (`parse_md`)

Imported from `docx_renderer.py`. Converts the 11,000+ line proposal Markdown into a flat list of `Seg` objects. Handles:
- HTML comments (single-line and block)
- Headings (H1–H5)
- Tables (pipe-delimited)
- Unordered and ordered lists
- Blockquotes (callout boxes)
- Paragraphs
- Horizontal rules

### 5.2 Section Grouper (`group_sections`)

Groups the flat `Seg` list into `ProposalSection` objects, one per H2 heading. Extracts:
- Section number ("12" from "12. Oracle Fusion HCM")
- Section name ("Oracle Fusion HCM")
- Appendix indicator ("A" from "Appendix A — Complete Assumption Schedule")

### 5.3 Section Classifier (`classify_sections`)

Classifies each section by examining its segment list:

| Status | Trigger | Priority |
|---|---|---|
| `TEMPLATE` | Section is "Table of Contents" or "Cover Page / Transmittal" | 1 (highest) |
| `PLACEHOLDER` | Any `<!-- PLACEHOLDER: ... -->` HTML comment present | 2 |
| `AI_DRAFT` | Any `<!-- AI-DRAFT REQUIRED: ... -->` HTML comment present | 3 |
| `RENDERED` | Has paragraph/table/ulist/olist that is not an AI sentinel | 4 |
| `EMPTY` | No content segments | 5 (lowest) |

**Critical rule:** PLACEHOLDER comment is authoritative. Sections with "Fields to complete" body text AND a PLACEHOLDER comment are classified as PLACEHOLDER (not RENDERED).

**AI sentinel detection:** The paragraph `_[AI-generated content to be inserted here — must be reviewed and approved before submission]_` is an internal marker. It is excluded from the `has_body` test so that AI-DRAFT sections are not misclassified as RENDERED.

### 5.4 Manifest Mapper (`map_manifest`)

Maps PSAE Section Manifest data onto each `ProposalSection` by matching section names (case-insensitive). Populates:
- `sec.mid` — manifest section ID (e.g. "S-03")
- `sec.manifest` — full manifest entry dict (assembly_method, source_assets, placeholders, governance_constraints, etc.)

### 5.5 Segment Filters

Three filter functions transform sections before rendering:

**`filter_client(segs)`** — strips:
- All HTML comments
- Internal marker blockquotes (ACTION REQUIRED, AI-DRAFT REQUIRED, HUMAN REVIEW REQUIRED, GOVERNANCE FLAGS)
- Internal paragraph metadata (KB asset headers, Document IDs, Scope/Governance/Usage tags, standalone pack markers)
- AI sentinel paragraphs
- Inline BU update references `(Updated...)`

**`filter_internal(segs)`** — keeps:
- PLACEHOLDER/AI-DRAFT comments (converted to action callouts)
- Governance notes (rendered as small italic notes)
- All blockquotes
- All content segments

**`filter_client` used for TRACEABILITY** — traceability profile shows clean content beside the manifest panel, using the same CLIENT filter to strip internal metadata.

---

## 6. Publication Profile Renderers

### 6.1 `ClientRenderer`

Produces the client-facing proposal. Algorithm:
1. Renders cover page with APPSolve branding, proposal title, Plennegy Group, metadata table
2. Adds auto-TOC field (Word updates on open)
3. Iterates sections:
   - TEMPLATE sections → skip (handled by cover/TOC)
   - PLACEHOLDER, AI_DRAFT, EMPTY → omit entirely (no notice shown to client)
   - RENDERED → render with CLIENT filter; page break before each numbered section
4. Adds headers (APPSolve brand) and footers (page numbers, COMMERCIAL IN CONFIDENCE)

**Plennegy pilot result:** 19 sections rendered | 18 PLACEHOLDER omitted | 3 AI_DRAFT omitted

### 6.2 `InternalReviewRenderer`

Produces the APPSolve internal review document. Algorithm:
1. Renders summary panel with section status counts (RENDERED/PLACEHOLDER/AI_DRAFT/TOTAL)
2. Renders Section Completeness Matrix — 40-row table with status badge and action required
3. Iterates all sections with status badge in heading (`✓`/`⚠`/`✏`/`—`):
   - PLACEHOLDER → grey notice box ("human action required")
   - AI_DRAFT → grey notice box ("AI generation + human review required")
   - RENDERED → content with INTERNAL filter (governance notes + action callouts preserved)
4. Adds INTERNAL USE ONLY headers and footers

### 6.3 `TraceabilityRenderer`

Produces the governance audit record. Algorithm:
1. Renders title page and manifest metadata table (manifest ID, platform, engagement type, section counts, validation status)
2. Shows active governance flags callout
3. Iterates all sections:
   - Each section preceded by traceability panel (2-column table: Section ID, Name, Status, Assembly Method, Mandatory Class, Source Assets, Placeholders, Governance Constraints, SI Rules, Human Input)
   - PLACEHOLDER/AI_DRAFT/EMPTY → grey notice box for content
   - RENDERED → CLIENT-filtered content
4. TRACEABILITY RECORD headers and footers

### 6.4 `ReviewReportGenerator`

Produces the quality review report. Sections:
1. Cover page with tender metadata
2. Executive Summary — proposal readiness assessment, overall score
3. Quality Scorecard — 10 criteria scored 1–5 (red ≤2 / amber 3 / green ≥4)
4. Detailed Criteria Assessment — per-criterion findings with recommendations
5. Priority Action Plan — owner-assigned actions, P0/P1/P2/P3 classification
6. Improvement Classification — human actions vs. factory improvements vs. KB gaps

---

## 7. Shared Rendering Infrastructure

All renderers import from `docx_renderer.py`:

| Import | Purpose |
|---|---|
| `Seg`, `parse_md` | Markdown parsing |
| `add_inline` | Inline markdown (bold, italic, code, links) to Word runs |
| `render_table` | Pipe-delimited markdown → Word table with navy headers |
| `render_callout` | Blockquote → coloured callout box |
| `render_ulist`, `render_olist` | Bulleted and numbered lists |
| `setup_styles` | APPSolve brand styles (Calibri; navy/blue headings) |
| `_page_break`, `_hr`, `_toc_field` | Document structure helpers |
| `_tab_stop`, `_page_field`, `_numpages_field` | Header/footer fields |
| `_cell_bg`, `_cell_borders` | Table cell formatting |
| `NAVY`, `BLUE`, `GREY`, `LGREY`, `WHITE`, `ORANGE` | Brand colours |
| `HEX_*` constants | Hex strings for callout box colours |
| `classify_comment` | HTML comment type classifier |
| `PROPOSALS_DIR` | Canonical proposals directory path |

---

## 8. Governance Rules

The PPE enforces the following constraints at all times:

1. **No content invention.** The PPE renders what the Knowledge Registry and PSAE have assembled. It does not draft, supplement, or alter any governed text.
2. **No governance bypass.** Sections under active governance constraints are rendered as-is; PPE does not remove or suppress governance markers in INTERNAL/TRACEABILITY profiles.
3. **CLIENT profile is clean.** No internal reference IDs, KB asset headers, Scope/Governance/Usage tags, or document IDs appear in the CLIENT output.
4. **Permanent KB restrictions.** The PPE does not render prohibited content (expired BEE status, prohibited client references, expired Oracle partnership claims). These are enforced upstream by KVE and PSAE — PPE trusts the assembly pipeline.
5. **Manifest integrity.** The traceability panel reproduces manifest data verbatim; it does not derive, infer, or interpolate assembly decisions.

---

## 9. CLI Usage

```bash
# Auto-locate by tender ID
python3 ppe.py --tender PLENNEGY-HCM-001

# Explicit paths
python3 ppe.py --md /path/to/proposal.md \
               --manifest /path/to/manifest.yaml \
               --out /path/to/output/
```

The `--tender` form locates the rendered MD and manifest from the canonical `Proposals/<TENDER_ID>/` directory structure.

---

## 10. File Locations

```
08_Commercial/Assembly_Engine/
  ppe.py                          — Proposal Publishing Engine v1.0
  docx_renderer.py                — Shared DOCX rendering infrastructure (PF2-004A)
  PUBLISHING_ENGINE.md            — This document
  PUBLICATION_PROFILE_STANDARD.md — Profile definitions and rules

08_Commercial/Proposals/<TENDER_ID>/
  PROPOSAL_RENDERED_<ID>.md       — Input: Markdown proposal (from PF2-004)
  PROPOSAL_SECTION_MANIFEST_<ID>.yaml — Input: Section manifest (from PF2-003)
  <PREFIX>_CLIENT_V2.docx         — Output: Client submission
  <PREFIX>_INTERNAL_REVIEW.docx   — Output: APPSolve review
  <PREFIX>_TRACEABILITY.docx      — Output: Audit record
  <PREFIX>_REVIEW_REPORT.docx     — Output: Quality review
```

---

## 11. Regression Safety

The PPE uses `parse_md` from `docx_renderer.py`. Any change to the Markdown parser must be regression-tested against both `docx_renderer.py` and `ppe.py` outputs. The PF2-007 Plennegy pilot output statistics serve as the regression baseline:

| Metric | Baseline (PLENNEGY-HCM-001) |
|---|---|
| Total H2 sections parsed | 41 |
| RENDERED | 19 |
| PLACEHOLDER | 18 |
| AI_DRAFT | 3 |
| TEMPLATE | 1 |
| CLIENT DOCX size | 410 KB |
| INTERNAL DOCX size | 422 KB |
| TRACEABILITY DOCX size | 423 KB |
| REVIEW REPORT size | 44 KB |

---

*Document ID: PUBLISHING-ENGINE-V1 | Platform L5.9 | PF2-007 | 2026-06-30*
