---
document_id: PUBLICATION-PROFILE-STANDARD-V1
title: "Publication Profile Standard (PF2-007)"
version: "1.0"
status: "APPROVED"
created: "2026-06-30"
created_by: "PF2-007 — Proposal Publishing Engine"
approved_by: "PF2-007"
approved_date: "2026-06-30"
category: "Standard"
scope: "Defines the three publication profiles produced by the Proposal Publishing Engine: CLIENT, INTERNAL REVIEW, and TRACEABILITY. Specifies which content is included, excluded, and transformed in each profile."
---

# Publication Profile Standard

**Version:** 1.0  
**Date:** 2026-06-30  
**Status:** APPROVED

---

## 1. Purpose

A Publication Profile is a set of rules that governs which content appears in a specific output document and how it is presented. The Proposal Publishing Engine (PPE) implements three profiles. Each profile targets a distinct audience with distinct needs.

**The PPE may:**
- Remove internal metadata and governance markers
- Convert HTML comment markers to visible callout boxes
- Add review-aid structure (completeness matrices, traceability panels)
- Apply whitespace, pagination, and navigation improvements

**The PPE must not:**
- Rewrite, summarise, or paraphrase any governed knowledge asset content
- Invent, supplement, or extend proposal content
- Remove content that the client needs to evaluate the proposal
- Alter the substance of any assumption, methodology, or commercial statement

---

## 2. Section Status Classification

All sections are classified before profile rendering:

| Status | Definition |
|---|---|
| `RENDERED` | Section has substantive content from KB assets (paragraphs, tables, lists) |
| `PLACEHOLDER` | Section has a `<!-- PLACEHOLDER: ... -->` comment — human commercial or client-specific input required |
| `AI_DRAFT` | Section has an `<!-- AI-DRAFT REQUIRED: ... -->` comment — AI generation plus human review required before use |
| `TEMPLATE` | Cover Page / Transmittal and Table of Contents — handled by PPE directly |
| `EMPTY` | No content segments |

**Classification priority:** PLACEHOLDER comment overrides any body content. A section with "Fields to complete" paragraphs AND a PLACEHOLDER comment is `PLACEHOLDER`, not `RENDERED`.

---

## 3. Profile 1 — CLIENT

### 3.1 Audience

Client / prospective customer. This is the document submitted as part of a tender response.

### 3.2 Objective

A clean, professional proposal. No internal metadata, governance notes, asset IDs, assembly markers, or internal review instructions visible.

### 3.3 Section Inclusion Rules

| Section Status | Included in CLIENT |
|---|---|
| RENDERED | Yes |
| PLACEHOLDER | No — omitted entirely (no notice) |
| AI_DRAFT | No — omitted entirely (no notice) |
| TEMPLATE | Cover page and TOC handled by PPE; not duplicated |
| EMPTY | No |

### 3.4 Content Stripping Rules

The following content is stripped from all RENDERED sections:

**Stripped paragraph patterns:**
- KB asset header lines: `Capability Statement | ... Oracle Business Unit`
- KB asset header lines: `Methodology Statement | ... Oracle Business Unit`
- KB asset header lines: `Assumption Pack | ...` / `Assumption Schedule | ...`
- Document ID lines: `Document ID: W#S#-NNN`
- Governance tag lines: `**Scope:** ...` / `**Governance:** ...` / `**Usage:** ...`
- Pack classification lines: `*Standalone pack` / `*Mandatory attachment`
- Assumption count lines: `*N assumptions/exclusions`
- Governance reference lines: `Governed under ASSUMPTION_GOVERNANCE`
- AI sentinel paragraph: `_[AI-generated content to be inserted here...]_`

**Stripped inline patterns:**
- BU update references: `(Updated ...)` or `*(Updated ...)*`

**Stripped blockquotes:**
- Blockquotes whose first line matches: ACTION REQUIRED / AI-DRAFT REQUIRED / AI DRAFT REQUIRED / HUMAN REVIEW REQUIRED / GOVERNANCE FLAGS

**Stripped HTML comments:** All — CLIENT document contains no HTML comments.

### 3.5 Document Structure

1. Cover page — APPSolve brand; proposal title; client name; metadata table
2. Table of Contents — Word auto-TOC field (updates on open)
3. Body — RENDERED sections with page break before each numbered section
4. Headers: APPSolve (Pty) Ltd (left) | solution description — COMMERCIAL IN CONFIDENCE (right)
5. Footers: APPSolve (Pty) Ltd | Tender ID | Page N of M

### 3.6 Classification

**COMMERCIAL IN CONFIDENCE.** Do not distribute outside APPSolve and the client organisation.

---

## 4. Profile 2 — INTERNAL REVIEW

### 4.1 Audience

APPSolve BU Lead and Account Manager. Internal working document for proposal review and completion tracking.

### 4.2 Objective

Complete view of all sections with action-required callouts for incomplete sections. Enables the reviewer to identify exactly what work remains before the proposal can be submitted to the client.

### 4.3 Section Inclusion Rules

| Section Status | Included in INTERNAL |
|---|---|
| RENDERED | Yes — with governance notes and action callouts |
| PLACEHOLDER | Yes — as omitted-section notice: "PLACEHOLDER — human action required" |
| AI_DRAFT | Yes — as omitted-section notice: "AI-DRAFT REQUIRED — generate and review" |
| TEMPLATE | Cover page/TOC skipped; summary panel and completeness matrix at front |
| EMPTY | Yes — as "— No content" notice |

### 4.4 Content Handling

**Kept (transformed):**
- `<!-- PLACEHOLDER: ... -->` comments → red action callout: **Action Required: ...**
- `<!-- AI-DRAFT REQUIRED: ... -->` comments → yellow callout: **AI-Draft Required: ...**
- `<!-- GOV: ... -->` and `<!-- SI-RULE: ... -->` → small italic governance note: ⚙ Governance: ...
- All blockquotes including internal review blockquotes

**Removed:**
- Raw HTML comments for `<!-- GOVERNANCE -->` and `<!-- META: -->` markers (pure metadata)

**Section heading badges:**
- RENDERED → `✓` suffix
- PLACEHOLDER → `⚠` suffix
- AI_DRAFT → `✏` suffix
- EMPTY → `—` suffix

### 4.5 Document Structure

1. Summary panel — section counts table (RENDERED/PLACEHOLDER/AI_DRAFT/TOTAL) with colour coding
2. Internal Use Only callout box
3. Section Completeness Matrix — 40-row table with section number, name, status, and action required
4. Body — all numbered sections with status badges and appropriate notices
5. Headers: APPSolve INTERNAL REVIEW (left) | Tender ID — INTERNAL USE ONLY (right)
6. Footers: APPSolve (Pty) Ltd | Tender ID | Page N of M

### 4.6 Classification

**INTERNAL USE ONLY.** Do not distribute outside APPSolve. Complete all PLACEHOLDER and AI-DRAFT sections before generating the CLIENT profile.

---

## 5. Profile 3 — TRACEABILITY

### 5.1 Audience

APPSolve governance auditors, Quality Assurance, and post-submission review.

### 5.2 Objective

Full audit record of the proposal: how each section was assembled, which Knowledge Base assets contributed, which manifest decisions were made, and what governance constraints applied.

### 5.3 Section Inclusion Rules

| Section Status | Included in TRACEABILITY |
|---|---|
| RENDERED | Yes — with traceability panel and clean content |
| PLACEHOLDER | Yes — with traceability panel and status notice |
| AI_DRAFT | Yes — with traceability panel and status notice |
| TEMPLATE | Cover page/TOC skipped; manifest overview on title page |
| EMPTY | Yes — with traceability panel and status notice |

### 5.4 Traceability Panel

Before each section's content, a 2-column table is rendered:

| Field | Source |
|---|---|
| Section ID | `sec.mid` from manifest mapping (e.g. S-03) |
| Section Name | Section heading text |
| Status | Classification result (RENDERED/PLACEHOLDER/AI_DRAFT/EMPTY) |
| Assembly Method | `assembly_method` from Section Manifest |
| Mandatory Class | `rationale` from Section Manifest |
| Source Assets | `source_assets` list from Section Manifest |
| Placeholders | `placeholders` list (if present) |
| Governance | `governance_constraints` (first 2, if present) |
| SI Rules | `si_rules_applied` (if present) |
| Human Input | `human_input_required` + `human_input_notes` |

Panel colour: light green background (HEX E8F3E8) with forest green border (HEX 2E8B57).

### 5.5 Content Handling

- RENDERED sections: CLIENT filter applied (internal metadata stripped; clean content shown beside panel)
- PLACEHOLDER/AI_DRAFT/EMPTY: grey status notice; no content beyond the panel

### 5.6 Document Structure

1. Title page — "Proposal Traceability Record" with tender ID, date, platform version
2. Manifest metadata table — manifest ID, platform, engagement type, section counts, validation status
3. Active governance flags callout (from manifest)
4. Body — all sections with traceability panels
5. Headers: TRACEABILITY RECORD — APPSolve INTERNAL (left) | Tender ID — GOVERNANCE DOCUMENT (right)
6. Footers: APPSolve (Pty) Ltd | Tender ID | Page N of M

### 5.7 Classification

**INTERNAL GOVERNANCE DOCUMENT.** Retain as part of the tender submission audit record for 7 years.

---

## 6. Review Report

The Review Report is not a Publication Profile in the same sense — it is a quality assurance output that assesses the proposal against 10 criteria. It is generated alongside the three profiles.

### 6.1 Ten Quality Criteria

| # | Criterion | Description |
|---|---|---|
| 1 | Executive Summary | Completeness and quality of the executive summary |
| 2 | Customer Focus | Evidence of RFP-specific understanding and tailoring |
| 3 | Proposal Flow | Logical sequence, completeness of structure |
| 4 | Commercial Positioning | Pricing completeness, commercial terms, value positioning |
| 5 | Differentiation | Competitive differentiation articulated |
| 6 | Client References | Reference quality, sector relevance, compliance |
| 7 | Readability | Typography, structure, professional presentation |
| 8 | Technical Completeness | Capability depth, assumption coverage, methodology |
| 9 | Missing Customer Info | Customer-specific gaps (plan, team, RFP response) |
| 10 | Recommendations | Action plan quality, owner assignment, priority |

### 6.2 Scoring

Each criterion scored 1–5. Colour coding:
- Red: ≤ 2 — significant gap; submission risk
- Amber: 3 — acceptable with action; monitor
- Green: ≥ 4 — strong; maintain

Overall readiness = sum / 50 × 100 (percentage).

### 6.3 Action Plan Classification

Actions are classified P0–P3:
- **P0 — URGENT:** Submission blocker with external deadline (e.g. B-BBEE expiry)
- **P1:** Submission blocker — must be resolved before submission
- **P2:** Quality risk — important but not a hard blocker
- **P3:** Nice to have — improve proposal quality if time allows

---

## 7. Colour Palette

| Use | Hex | RGB | Description |
|---|---|---|---|
| Navy (primary) | 00467F | 0,70,127 | Headings, table headers, brand |
| Blue (accent) | 0070C0 | 0,112,192 | Subheadings, cover subtitle |
| Grey | 595959 | 89,89,89 | Body text, labels |
| Light grey | ABABAB | 171,171,171 | Meta text, footers |
| White | FFFFFF | 255,255,255 | Table header text |
| Orange | E07000 | 224,112,0 | Inline field references |
| PLACEHOLDER bg | FFE8E8 | — | Red tint — missing sections |
| AI-DRAFT bg | FFF5D0 | — | Yellow tint — AI required |
| HUMAN REVIEW bg | E8F0FF | — | Blue tint — human review |
| GOVERNANCE bg | F0F4F0 | — | Green tint — governance note |
| TRACEABILITY bg | E8F3E8 | — | Light green — traceability panel |
| RENDERED bg | D4EDDA | — | Green tint — status OK |
| PLACEHOLDER status | F8D7DA | — | Red tint — status at risk |
| AI-DRAFT status | FFF3CD | — | Yellow tint — action needed |

---

*Document ID: PUBLICATION-PROFILE-STANDARD-V1 | Platform L5.9 | PF2-007 | 2026-06-30*
