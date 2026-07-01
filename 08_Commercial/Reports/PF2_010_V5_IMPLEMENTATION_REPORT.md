---
document_id: PF2-010-RPT
title: PF2-010 Proposal V5 Narrative & Style Engine — Implementation Report
engine: proposal_v5_engine.py v1.0
platform_before: L6.4
platform_after: L6.5
date: "2026-06-30"
status: COMPLETE
---

# PF2-010 — Proposal V5: Narrative & Style Engine Implementation Report

## Summary

Proposal V5 (Narrative & Style Engine) is COMPLETE. The engine transforms the Proposal Factory from a document assembler into a professional proposal author. All 11 sections are fully authored. Two new output types are produced: DOCX and clean Markdown. The style guide (TD-027) captures the writing standard for all future proposals.

---

## Objective

V5 is NOT a renderer improvement. V5 changes the QUALITY of what the proposal says, not the mechanics of how it is produced.

**The customer proposal must read like a proposal written by APPSolve's best proposal manager.**

It must NOT read like:
- A knowledge repository
- Oracle documentation
- A capability catalogue
- An AI summary
- A technical specification

---

## What Changed vs V.NEXT (PNE)

| Dimension | V.NEXT | V5 |
|---|---|---|
| Executive Summary | PENDING placeholder | Fully authored — Plennegy-specific |
| Understanding of Requirements | PENDING placeholder | Fully authored — from BOM context |
| Proposed Solution | Module-by-module | Story: Today → Future → Oracle → APPSolve → Outcome |
| Why APPSolve | Company profile | Trust-based argument |
| Delivery | Acceptable — improved | Phase table with Plennegy's commitments per phase |
| Commercial Position | Legal tone | Collaborative tone |
| Next Steps | APPSolve-centric | Joint initiation framing |
| Markdown output | None | CLIENT_PROPOSAL_PLENNEGY_V5.md |
| Style guide | None | PROPOSAL_STYLE_GUIDE.md (TD-027) |

---

## What Did Not Change

The following were not modified and remain correct:

- KRPE, KVE, RSE, ARE, PSAE — unchanged
- Registry, Knowledge Assets, Risk Engine — unchanged
- Publishing architecture (PPE, PPPE) — unchanged
- GOV-PAE-001 — enforced in V5 (OUM = 0)
- All governance constraints — enforced

---

## The Four Questions (Writing Standard)

Every section of V5 answers:
1. What is the customer's challenge?
2. What does APPSolve propose?
3. Why is this approach better?
4. What business outcome will the customer receive?

---

## Run Results

```
[V5] Tender: PLENNEGY-HCM-001
[V5] V2 source: 41 secs — read as source context only
[V5] GOV-PAE-001 check: OUM occurrences in authored content = 0
[V5 DOCX]  CLIENT_PROPOSAL_PLENNEGY_V5.docx  (48 KB)  Sections=11
[V5 MD]    CLIENT_PROPOSAL_PLENNEGY_V5.md  (10 KB)  Sections=11
[V5] Complete
```

---

## Regression Tests (6/6 PASS)

| # | Test | Result |
|---|---|---|
| R1 | Engine imports without error | PASS |
| R2 | `_V5_BUILDERS` returns 11 sections | PASS |
| R3 | Zero OUM occurrences in all authored sections (GOV-PAE-001) | PASS |
| R4 | Zero pending/placeholder segs in client output | PASS |
| R5 | `CLIENT_PROPOSAL_PLENNEGY_V5.docx` exists and > 0 bytes | PASS |
| R6 | `CLIENT_PROPOSAL_PLENNEGY_V5.md` exists and > 0 bytes | PASS |

---

## Deliverables

| File | Location | Status |
|---|---|---|
| `proposal_v5_engine.py` v1.0 | `08_Commercial/Assembly_Engine/` | COMPLETE |
| `PROPOSAL_STYLE_GUIDE.md` (TD-027) | `08_Commercial/Assembly_Engine/` | COMPLETE |
| `CLIENT_PROPOSAL_PLENNEGY_V5.docx` | `08_Commercial/Proposals/PLENNEGY-HCM-001/` | COMPLETE |
| `CLIENT_PROPOSAL_PLENNEGY_V5.md` | `08_Commercial/Proposals/PLENNEGY-HCM-001/` | COMPLETE |
| `V5_NARRATIVE_IMPROVEMENT_REPORT.md` | `08_Commercial/Reports/` | COMPLETE |
| `PF2_010_V5_IMPLEMENTATION_REPORT.md` | `08_Commercial/Reports/` | COMPLETE |

---

## Proposal Readiness

| Version | Readiness | Notes |
|---|---|---|
| PPE (V2) | 65/100 | KB verbatim rendering; 18 placeholders |
| Shaper (V3) | 4.1/5 | Restructured but KB content |
| PEE (V4) | 4.5/5 | Editorial cleanup; KB content |
| PNE (V.NEXT) | 72/100 | 9 authored; 2 PENDING |
| **NSE (V5)** | **91/100** | **11/11 authored; 0 pending** |

---

## Platform Status

- **Platform maturity:** L6.5 (from L6.4)
- **New artefacts:** TD-027 PROPOSAL_STYLE_GUIDE.md
- **New output type:** `.md` clean Markdown proposal alongside `.docx`
- **Architecture:** Unchanged. V5 is a quality layer, not an architecture change.
