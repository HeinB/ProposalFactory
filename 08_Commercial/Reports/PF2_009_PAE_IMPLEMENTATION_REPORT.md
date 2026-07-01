---
document_id: PF2-009-IMPL-REPORT
title: PF2-009 Proposal Authoring Engine — Implementation Report
work_package: PF2-009 (PAE v1.0)
engine: proposal_authoring_engine.py
status: COMPLETE
date: "2026-06-30"
platform_before: L6.1
platform_after: L6.2
---

# PF2-009 — Proposal Authoring Engine Implementation Report

## Summary

The Proposal Authoring Engine (PAE) is the final publishing step of the APPSolve Proposal Factory. Unlike all prior engines (which reorganise, filter, and annotate Knowledge Base content), the PAE **authors** client proposals from scratch — treating KB assets as source evidence rather than proposal sections.

PAE produces two completely different outputs from the same V2 rendered source:

| Output | File | Size | Description |
|---|---|---|---|
| Client Proposal | `CLIENT_PROPOSAL_[Tender].docx` | 61 KB (Plennegy) | 25–40 pages; executive narrative; no internal content |
| Internal Review Pack | `INTERNAL_REVIEW_PACK_[Tender].docx` | 431 KB (Plennegy) | Complete internal document: all V2 content + traceability |

---

## New Permanent Platform Rule — GOV-PAE-001

This work package encodes a permanent, governed platform rule:

> **Oracle Fusion Cloud proposals must use "Oracle's Modern Best Practices" and "Oracle Success Navigator" as the primary delivery methodology. Oracle Unified Method (OUM) is prohibited.**

OUM is only permitted for Oracle E-Business Suite (EBS) legacy engagements. Fusion Cloud proposals must never state "Our methodology is based on OUM."

This rule is hard-coded in `proposal_authoring_engine.py`. The authored methodology section uses correct Oracle Modern Best Practices language exclusively.

---

## Architecture

```
PROPOSAL_RENDERED_[Tender].md (V2)
          │
          ▼
proposal_authoring_engine.py (PAE)
          │
    ┌─────┴──────┐
    │            │
    ▼            ▼
CLIENT_PROPOSAL  INTERNAL_REVIEW_PACK
(11+2 sections,  (Action Register +
authored         Part 1: Published +
narrative)       Part 2: KB content)
```

PAE imports from `docx_renderer.py`, `proposal_shaper.py`, and `pee.py`. The prior engines (shaper, pee) remain the traceability-oriented pipeline; PAE is the client-publishing pipeline.

---

## PAE Authored Sections

| # | Section | Content Source | Target Length |
|---|---|---|---|
| 1 | Executive Summary | PLACEHOLDER — BU Lead | 2 pages |
| 2 | Understanding of Requirements | PLACEHOLDER — AM | 2 pages |
| 3 | The Solution We Propose | PAE authored — scope table | 1–2 pages |
| 4 | Why APPSolve | PAE authored — credential narrative | 2–3 pages |
| 5 | How We Deliver | PAE authored — Oracle Modern Best Practices | 3–4 pages |
| 6 | What We Deliver for You | PAE authored — HCM capability summary | 4–6 pages |
| 7 | Project Governance | PAE authored — governance table | 2 pages |
| 8 | Your Implementation Roadmap | PAE authored — phase timeline | 2 pages |
| 9 | Key Assumptions | PAE authored — category summary | 2 pages |
| 10 | Commercial | PAE authored — inputs required | 1 page |
| 11 | Your Next Steps | PAE authored — client actions ONLY | 1 page |
| A | Assumption Schedule | KB assets — extracted | ≤15 pages |
| B | Reference Summary | PLACEHOLDER — AM approval | ≤3 pages |

**Plennegy result:** Authored=9, Pending=2 (Exec Summary + Understanding)

---

## Authoring Improvements Over Prior Engines

| Dimension | Prior Engines (PEE/Shaper) | PAE |
|---|---|---|
| Content source | Filtered/budgeted KB text | Original authored narrative |
| Methodology | OUM inherited from KB assets | Oracle Modern Best Practices (PAE-authored) |
| Section length | Budget-capped KB excerpts | Targeted narrative (business story) |
| Source evidence | Stripped/filtered | Moved to Internal Review Pack |
| Client language | Technical, KB-native | "You" and "your" — client perspective |
| Internal actions | Shown as callouts | Consolidated in Action Register (Internal only) |

---

## Architecture Documents Delivered

| Document | ID | Purpose |
|---|---|---|
| `PROPOSAL_AUTHORING_STANDARD.md` | TD-020 | GOV-PAE-001 + quality gates |
| `CLIENT_PROPOSAL_STANDARD.md` | TD-021 | Client proposal section standard |
| `INTERNAL_REVIEW_PACK_STANDARD.md` | TD-022 | Internal review pack standard |

---

## Regression Results

| Engine | Status | Notes |
|---|---|---|
| `proposal_renderer.py` | 6/6 PASS | RENDERED=21 PH=18 AI=3 NOT_FOUND=0 |
| `pee.py` (PEE) | 6/6 PASS | V4: 16 secs CLIENT=94KB INTERNAL=97KB |
| `proposal_authoring_engine.py` (PAE) | NEW | CLIENT=61KB INTERNAL=431KB |

**Total regression violations: 0**

---

## Plennegy-HCM-001 Outputs

| File | Size | Description |
|---|---|---|
| `CLIENT_PROPOSAL_PLENNEGY.docx` | 61 KB | Client-ready proposal — 9 authored sections |
| `INTERNAL_REVIEW_PACK_PLENNEGY.docx` | 431 KB | Full internal document — 41 V2 sections |

---

## Open Actions (from Internal Action Register)

| Priority | Action | Owner |
|---|---|---|
| P0 URGENT | Renew B-BBEE certificate (due 2026-07-31) | Finance Director |
| P1 | Author Executive Summary with Plennegy win themes | BU Lead |
| P1 | Author Understanding of Requirements from client brief | Account Manager |
| P1 | Confirm scope: modules, entities, headcount, payroll provider (OAR-C04) | Account Manager |
| P1 | Issue Commercial Proposal (OAR-C02) | Commercial Director |
| P2 | Approve Hollywood Bets reference (OAR-C01) | Account Manager |

---

## Platform Maturity

| Before | After |
|---|---|
| L6.1 | **L6.2** |

Platform L6.2: Proposal Authoring Engine operational. Two complete Plennegy outputs: CLIENT_PROPOSAL (authored) and INTERNAL_REVIEW_PACK (traceability). GOV-PAE-001 (Oracle methodology rule) encoded as permanent governed rule.
