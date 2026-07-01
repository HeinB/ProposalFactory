---
document_id: PF2-009-RPT
title: PF2-009 Proposal Narrative Engine (PNE) — Implementation Report
engine: proposal_narrative_engine.py v1.0
platform_before: L6.3
platform_after: L6.4
date: "2026-06-30"
status: COMPLETE
---

# PF2-009 — Proposal Narrative Engine Implementation Report

## Summary

PNE (Proposal Narrative Authoring Engine) v1.0 is COMPLETE. The engine transforms V2 rendered Markdown into a concise, authored, customer-facing proposal narrative using a business-outcome framework. Three DOCX outputs are produced; all regression tests pass.

---

## Problem Statement

The Proposal Factory pipeline (KRPE → KVE → ARE → RSE → PSAE → Renderer → PPE) produces V2 rendered Markdown that faithfully exports Knowledge Base content. When rendered verbatim, this produces:

| KB Section | Verbatim Size |
|---|---|
| Oracle Fusion HCM Capability | ≈69 pages |
| Implementation Methodology | ≈18 pages |
| Project Governance | ≈18 pages |
| Key Assumptions (Body) | ≈62 pages |
| Company sections (7) | ≈10 pages |
| **Total (major sections)** | **≈177 pages of source content** |

This is not a client proposal. It is a knowledge asset export. PPPE (PF2-010) applies page budgets but truncates rather than replaces — it cannot transform 69 pages of capability detail into 6 pages of proposal narrative.

PNE solves this by authoring all major sections from scratch. KB content is source evidence; the proposal is authored narrative.

---

## Engine Architecture

### Input
- `PROPOSAL_RENDERED_[TENDER_ID].md` — V2 rendered Markdown from the upstream pipeline
- Parsed via `parse_md()` + `group_v2()` (imported from proposal_shaper.py)

### Authored Content Functions

| Section | Function | KB Sources Used | Output Size |
|---|---|---|---|
| 1. Executive Summary | `_authored_exec_summary()` | None — PENDING | PENDING |
| 2. Understanding Plennegy's Requirements | `_authored_understanding()` | None — PENDING | PENDING |
| 3. Proposed Oracle HCM Solution | `_authored_hcm_solution()` | HCM Capability, OIC, Learning, Talent | ≈6 pages |
| 4. Why APPSolve | `_authored_why_appsolve()` | 7 company sections | ≈3 pages |
| 5. How We Deliver | `_authored_how_we_deliver()` | Implementation Methodology | ≈4 pages |
| 6. Project Governance | `_authored_project_governance()` | Project Governance | ≈2 pages |
| 7. Implementation Roadmap | `_authored_roadmap()` | Project Plan / Timeline | ≈2 pages |
| 8. Key Commercial Assumptions | `_authored_key_assumptions()` | Key Assumptions | ≈2 pages |
| 9. Key Delivery Risks and Mitigations | `_authored_key_risks()` | Risk Register | ≈2 pages |
| 10. Commercial Position | `_authored_commercial()` | Commercials / Pricing | ≈1 page |
| 11. Your Next Steps | `_authored_next_steps()` | None — client actions | ≈1 page |

### Output Renderers

| Output | Renderer | Purpose |
|---|---|---|
| `CLIENT_PROPOSAL_[TENDER]_VNEXT.docx` | `render_client()` | Authored narrative, 11 sections, PENDING boxes for incomplete |
| `INTERNAL_REVIEW_PACK_[TENDER]_VNEXT.docx` | `render_internal()` | Action Register + Part 1 (authored) + Part 2 (all 41 V2 KB sections) |
| `TRACEABILITY_REPORT_[TENDER]_VNEXT.docx` | `render_traceability()` | Authoring summary + section trace + compression table |

---

## Plennegy Run Results

```
[PNE] Tender: PLENNEGY-HCM-001
[PNE] V2: 41 secs | RENDERED=20 PH=18 AI=3
[PNE] Sections: 11 | Authored=9 Pending=2
[PNE CLIENT]      CLIENT_PROPOSAL_PLENNEGY_VNEXT.docx  (45 KB)  Authored=9 Pending=2
[PNE INTERNAL]    INTERNAL_REVIEW_PACK_PLENNEGY_VNEXT.docx  (429 KB)  V2 secs=41
[PNE TRACE]       TRACEABILITY_REPORT_PLENNEGY_VNEXT.docx  (39 KB)
[PNE] Complete — 3 outputs in .../08_Commercial/Proposals/PLENNEGY-HCM-001
```

---

## Content Compression Achieved (Plennegy)

| KB Section | Source Segs | Approx Pages | PNE Section | PNE Pages | Compression |
|---|---|---|---|---|---|
| Oracle Fusion HCM Capability | 555 | 69 | Sec 3 (partial) | 6 | 11× |
| Oracle Fusion ERP Capability | 165 | 21 | Not published | — | ∞ |
| Oracle OIC / Integration | 71 | 9 | Sec 3 (partial) | — | Combined |
| Implementation Methodology | 140 | 18 | Sec 5 | 4 | 4.5× |
| Project Governance | 140 | 18 | Sec 6 | 2 | 9× |
| Key Assumptions (Body) | 497 | 62 | Sec 8 | 2 | 31× |
| Company sections (7) | 76 | 10 | Sec 4 | 3 | 3.3× |
| **Total (major)** | **1,644** | **≈207** | **Authored** | **≈23** | **≈9×** |

---

## Governance Compliance

| Rule | Status | Notes |
|---|---|---|
| **GOV-PAE-001** (OUM prohibited) | COMPLIANT | All authored sections use "Oracle's Modern Best Practices" / "Oracle Success Navigator" — OUM does not appear in client output |
| Internal IDs prohibited | COMPLIANT | No ASM, CAP, ADR, TD, WP IDs in client output |
| No draft markers | COMPLIANT | PENDING shown as grey boxes in client; full callouts in internal |
| No full assumption packs | COMPLIANT | Sec 8 = 5-row commercial table; full packs in Part 2 (internal only) |
| No AI Draft exposed | COMPLIANT | Client sees PENDING box; internal sees Action Required callout |
| Headcount: "more than 50 Senior Consultants" | COMPLIANT | Used in Why APPSolve section |
| Oracle Level 1 Partner (not Gold) | COMPLIANT | Used in Why APPSolve section |
| B-BBEE warning | PRESENT | Action Register: OAR-A01 — renewal due 2026-07-31 URGENT |

---

## Regression Tests (6/6 PASS)

| # | Test | Result |
|---|---|---|
| R1 | PNE imports without error | PASS |
| R2 | `_build_sections()` returns 11 sections | PASS |
| R3 | `_authored_how_we_deliver()` contains zero OUM occurrences | PASS |
| R4 | `_authored_hcm_solution()` contains zero OUM occurrences | PASS |
| R5 | `_authored_key_assumptions()` contains no ID patterns | PASS |
| R6 | `run_pne()` produces 3 DOCX files | PASS |

---

## Deliverables

| File | Location | Status |
|---|---|---|
| `proposal_narrative_engine.py` v1.0 | `08_Commercial/Assembly_Engine/` | COMPLETE |
| `PROPOSAL_NARRATIVE_AUTHORING_STANDARD.md` (TD-026) | `08_Commercial/Assembly_Engine/` | COMPLETE |
| `CLIENT_PROPOSAL_PLENNEGY_VNEXT.docx` | `08_Commercial/Proposals/PLENNEGY-HCM-001/` | COMPLETE |
| `INTERNAL_REVIEW_PACK_PLENNEGY_VNEXT.docx` | `08_Commercial/Proposals/PLENNEGY-HCM-001/` | COMPLETE |
| `TRACEABILITY_REPORT_PLENNEGY_VNEXT.docx` | `08_Commercial/Proposals/PLENNEGY-HCM-001/` | COMPLETE |

---

## Known Constraints

1. **Sections 1 and 2 remain PENDING** — Executive Summary and Understanding of Requirements require BU Lead + Account Manager input with Plennegy-specific context. PNE will render PENDING boxes until these are authored.
2. **Oracle Fusion ERP Capability not published** — HCM is the primary scope; ERP retained in Internal Review Pack Part 2 as source material.
3. **No binding commercial pricing** — Commercial Position (Sec 10) contains framework only; formal Commercial Proposal issued separately by Commercial Director.

---

## Platform Status

- **Platform maturity:** L6.4 (from L6.3)
- **Cumulative engines:** KRPE v2.0 + KVE v2.0 + ARE v1.0 + RSE v1.0 + PSAE v1.0 + Renderer v1.0 + PPE v1.0 + Shaper v1.0 + PEE v1.0 + PAE v1.0 + PPPE v1.0 + **PNE v1.0**
- **New artefacts:** TD-026
