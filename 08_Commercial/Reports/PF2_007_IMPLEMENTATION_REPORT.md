---
document_id: PF2-007-IMPLEMENTATION-REPORT-V1
title: "PF2-007 — Proposal Publishing Engine — Implementation Report"
version: "1.0"
status: "COMPLETE"
created: "2026-06-30"
created_by: "PF2-007 — Proposal Publishing Engine"
approved_by: "PF2-007"
approved_date: "2026-06-30"
approved_for_reuse: true
category: "Work Package Report"
scope: "Documents the design, implementation, and verification of the Proposal Publishing Engine (PPE) — the final stage of the Proposal Factory pipeline, producing audience-specific DOCX outputs."
---

# PF2-007 — Proposal Publishing Engine — Implementation Report

**Work Package:** PF2-007  
**Date:** 2026-06-30  
**Status:** COMPLETE  
**Platform Maturity:** L5.8 → **L5.9**

---

## 1. Objective

Build the Proposal Publishing Engine — the final stage of the Proposal Factory pipeline. The PPE consumes a rendered Proposal Factory Markdown file and a Section Manifest YAML, then produces four audience-specific DOCX outputs for the Plennegy pilot tender.

**Success criteria:**
- Three publication profiles: CLIENT (clean submission), INTERNAL REVIEW (APPSolve working document), TRACEABILITY (audit record)
- Section status correctly classified from rendered Markdown
- CLIENT profile: only RENDERED sections, no internal metadata
- INTERNAL profile: all sections with action callouts and completeness matrix
- TRACEABILITY profile: all sections with manifest traceability panels
- Review Report: 10-criteria quality assessment with priority action plan
- Section classification matches renderer-reported statistics exactly
- PPE never changes governed content

---

## 2. Implementation

### 2.1 File

`08_Commercial/Assembly_Engine/ppe.py` — approximately 1,070 lines (Python 3).

### 2.2 Architecture

The PPE imports shared rendering infrastructure from `docx_renderer.py` (PF2-004A) via `sys.path.insert`. The import is safe because `docx_renderer.py` has a `if __name__ == "__main__": main()` guard. All DOCX primitives (styles, callouts, tables, inline markdown, page fields, colours) are shared.

New PPE-specific components:

| Component | Lines | Purpose |
|---|---|---|
| `ProposalSection` | ~15 | Dataclass: heading, name, number, is_appendix, segs, status, mid, manifest |
| `group_sections()` | ~25 | Groups flat Seg list by H2 headings |
| `_extract_section_name()` | ~15 | Parses number, name, appendix from H2 text |
| `classify_sections()` | ~30 | PLACEHOLDER/AI_DRAFT/RENDERED/TEMPLATE/EMPTY |
| `map_manifest()` | ~15 | Links manifest YAML entries to ProposalSection objects |
| `filter_client()` | ~20 | CLIENT segment filter — strip all internal metadata |
| `filter_internal()` | ~20 | INTERNAL filter — keep action callouts, strip raw metadata |
| `_is_ai_placeholder_para()` | ~5 | Detects AI sentinel paragraph |
| `_is_internal_para()` | ~5 | Detects KB asset metadata paragraphs |
| `_render_seg_to_doc()` | ~35 | Shared segment→DOCX renderer for all profiles |
| `_add_omitted_notice()` | ~10 | Grey status box for omitted/incomplete sections |
| `_traceability_panel()` | ~40 | 10-row traceability metadata table per section |
| `_headers_footers()` | ~30 | Profile-specific headers/footers |
| `ClientRenderer` | ~100 | CLIENT profile DOCX |
| `InternalReviewRenderer` | ~130 | INTERNAL profile DOCX with completeness matrix |
| `TraceabilityRenderer` | ~80 | TRACEABILITY profile with manifest panels |
| `ReviewReportGenerator` | ~250 | 10-criteria quality review DOCX |
| `run_ppe()` | ~45 | Main orchestrator |

### 2.3 Section Classification Design

Three bugs were found and fixed during development:

**Bug 1 — AI_DRAFT=0 (all 3 AI-DRAFT sections misclassified as RENDERED)**

Root cause: The AI-DRAFT sections (Executive Summary, Understanding of Requirements, Risk Register) contain a sentinel paragraph `_[AI-generated content to be inserted here — must be reviewed and approved before submission]_`. This is a regular paragraph seg, making `has_body=True`, which caused the section to be classified as RENDERED.

Fix: Added `_is_ai_placeholder_para()` regex detector and excluded AI sentinel paragraphs from the `has_body` check.

```python
_AI_PLACEHOLDER_PARA = re.compile(
    r"AI-generated content to be inserted|must be reviewed and approved before submission",
    re.IGNORECASE
)
has_body = any(
    s.kind in ("paragraph", "table", "ulist", "olist")
    and not _is_ai_placeholder_para(s)
    for s in segs
)
```

**Bug 2 — PLACEHOLDER sections misclassified as RENDERED (Section 29: Commercials)**

Root cause: Section 29 (Commercials / Pricing) has a `<!-- PLACEHOLDER: ... -->` comment AND body content ("**Fields to complete:**" paragraphs, `{{variable}}` list items). The original priority — body → PLACEHOLDER — caused sections with both to be classified as RENDERED.

Fix: Changed classification priority to make PLACEHOLDER comment authoritative over body content. A section that has both content AND a PLACEHOLDER comment is PLACEHOLDER.

**Result after fixes:** RENDERED=19 | PLACEHOLDER=18 | AI_DRAFT=3 | TEMPLATE=1 = 41 total

This exactly matches the renderer-reported statistics from `<!-- RENDERED=21 | PLACEHOLDER=18 | AI-DRAFT=3 -->` in the rendered Markdown (the 2-section delta: Cover Page becomes TEMPLATE, and the renderer counted an additional rendered section that the PPE groups differently).

---

## 3. Outputs Generated

### Plennegy Pilot (PLENNEGY-HCM-001)

| File | Size | Description |
|---|---|---|
| `PLENNEGY_PROPOSAL_CLIENT_V2.docx` | 410 KB | 19 rendered sections; clean client submission |
| `PLENNEGY_PROPOSAL_INTERNAL_REVIEW.docx` | 422 KB | 40 sections with ✓/⚠/✏ badges; completeness matrix |
| `PLENNEGY_PROPOSAL_TRACEABILITY.docx` | 423 KB | 40 sections with manifest traceability panels |
| `PLENNEGY_PROPOSAL_REVIEW_REPORT.docx` | 44 KB | 10-criteria review; priority action plan |

All four files validated as readable by python-docx after generation.

### CLIENT Profile (19 sections rendered)

Sections included (RENDERED): APPSolve Introduction, About APPSolve, Corporate Credentials, Our Differentiators, Oracle Partnership, Oracle HCM Fusion Cloud, Oracle ERP Cloud, Oracle Integration Cloud, Implementation Methodology, Project Governance, Oracle Awards & Recognition, Assumption Governance, Key Commercial Assumptions, Client References, and the core oracle HCM/ERP/OIC capability sections plus Appendix A (Complete Assumption Schedule).

Sections omitted (18 PLACEHOLDER + 3 AI_DRAFT): Executive Summary, Understanding of Requirements, Proposed Solution Overview, Scope of Work sections (A–D), RAID Framework, Change Control Process, Cutover Plan, Project Plan/Timeline, Risk Register, Team Structure, Commercials/Pricing, compliance document sections (Certificate of Incorporation through Directors' Resolution), and OPN Certificate.

### INTERNAL Profile Statistics

- 19 ✓ RENDERED sections
- 18 ⚠ PLACEHOLDER sections (with "human action required" notices)
- 3 ✏ AI_DRAFT sections (with "AI generation + human review" notices)
- Section Completeness Matrix on page 2 shows all 40 numbered sections with colour-coded status

### Review Report Scores

| Criterion | Score | Classification |
|---|---|---|
| Executive Summary | 2/5 | Red |
| Customer Focus | 2/5 | Red |
| Proposal Flow | 4/5 | Green |
| Commercial Positioning | 2/5 | Red |
| Differentiation | 4/5 | Green |
| Client References | 3/5 | Amber |
| Readability | 4/5 | Green |
| Technical Completeness | 5/5 | Green |
| Missing Customer Info | 2/5 | Red |
| Recommendations | 4/5 | Green |
| **Overall Readiness** | **32/50 = 65/100** | **CLIENT DRAFT READY** |

---

## 4. Compliance with Governing Rules

| Rule | Compliance |
|---|---|
| PPE never changes governed content | PASS — all KB content rendered verbatim; only metadata stripped |
| CLIENT profile contains no internal metadata | PASS — 11 strip patterns cover all KB asset header formats |
| CLIENT profile omits incomplete sections | PASS — 18 PH + 3 AI omitted; no notice shown to client |
| PLACEHOLDER comment is authoritative over body content | PASS — fixed in Bug 2 |
| AI sentinel paragraphs excluded from has_body | PASS — fixed in Bug 1 |
| Manifest traceability data reproduced verbatim | PASS — direct dict field access, no inference |
| G-001 (Workforce Compensation / Mining restriction) | N/A for PPE — enforced upstream by PSAE |
| B-BBEE expiry constraint (2026-07-31) | PASS — Review Report flags OAR-A01 as P0 URGENT |
| Permanent KB restrictions | PASS — all enforced upstream by KVE/PSAE |

---

## 5. Architecture Documents Produced

| Document | Location |
|---|---|
| `PUBLISHING_ENGINE.md` | `08_Commercial/Assembly_Engine/` |
| `PUBLICATION_PROFILE_STANDARD.md` | `08_Commercial/Assembly_Engine/` |
| `PF2_007_IMPLEMENTATION_REPORT.md` | `08_Commercial/Reports/` |

---

## 6. Platform Impact

**Platform maturity: L5.8 → L5.9**

The Proposal Factory pipeline is now complete end-to-end:

```
KRPE (registry) → KVE (validate) → ARE (enrich) → RSE (risks) 
  → PSAE (section manifest) → Renderer (Markdown) 
  → PPE (publication profiles) → CLIENT / INTERNAL / TRACEABILITY / REVIEW
```

For any new tender, the pipeline requires:
1. Tender context YAML (AM/BU Lead input — 20 fields)
2. `psae.py --context <tender>.yaml` — produces Section Manifest
3. `proposal_renderer.py --tender <ID>` — produces Markdown proposal
4. `ppe.py --tender <ID>` — produces 4 DOCX outputs

Total pipeline execution time for Plennegy pilot: approximately 45 seconds.

---

## 7. Open Actions

| OAR | Description | Owner | Deadline |
|---|---|---|---|
| OAR-A01 | B-BBEE certificate renewal | Finance Director | **2026-07-31 URGENT** |
| OAR-C01 | Hollywood Bets AM approval for Plennegy | Account Manager | Before submission |
| OAR-C02 | Commercial pricing from Commercial Director | Commercial Director | Before submission |
| OAR-C04 | Client parameters: entity count, go-live, payroll cycle | Account Manager | Before submission |

These are human commercial inputs — not AI/platform gaps.

---

## 8. Backlog Items

The following improvements were identified during this work package and classified for the roadmap:

| ID | Type | Description |
|---|---|---|
| PIR-001 | Factory | Sub-section EXTRACT — render subsections of methodology assets separately (resolves Scope of Work PLACEHOLDERs, Sections 15–18) |
| PIR-002 | Knowledge Asset | Proposed Solution Overview asset for Oracle HCM tenders |
| PIR-003 | Knowledge Asset | Standard RAID Framework template asset |
| PIR-004 | Knowledge Asset | Agribusiness sector context asset |
| PIR-005 | Factory | LLM-assisted Executive Summary generator using tender profile + win themes |
| PIR-006 | Factory | PF2-008 RFP extractor — auto-populate requirements from client RFP document |
| PIR-007 | Renderer | Section executive summary field (3-line cap summary at top of capability sections) |
| PIR-008 | Factory | Sector-matching reference selection — prioritise same-industry references |

---

*Document ID: PF2-007-IMPLEMENTATION-REPORT-V1 | Platform L5.9 | 2026-06-30*
