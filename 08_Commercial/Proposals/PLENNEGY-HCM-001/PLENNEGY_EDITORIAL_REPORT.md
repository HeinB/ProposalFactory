---
document_id: PLENNEGY-V3-V4-EDITORIAL-V1
title: "Plennegy Proposal V3 → V4 Editorial Report"
version: "1.0"
status: "COMPLETE"
created: "2026-06-30"
created_by: "PF2-008 — Proposal Editorial Engine v1.0"
---

# Plennegy Proposal — V3 → V4 Editorial Report

**Tender:** PLENNEGY-HCM-001  
**Date:** 2026-06-30  
**Engine:** pee.py v1.0 (PF2-008 Proposal Editorial Engine)  
**Platform:** L6.0

---

## 1. Executive Summary

The Proposal Editorial Engine (PEE) applied five editorial transformations to the V3 structured proposal, producing V4 — a concise, customer-focused proposal ready for executive review and final commercial sign-off.

| Metric | V3 | V4 | Change |
|---|---|---|---|
| Body sections | 10 | 11 | +1 (Implementation Roadmap added) |
| Appendices | 3 (A,B,C) | 5 (A–E) | +2 (Reference Projects + Glossary) |
| Total content segments | 1398 | 322 | −1076 (76%) |
| Segments removed by engine | — | 1100 | Filter+Boilerplate+Dedup+Budget |
| Segments authored by PEE | — | 22 | New sections: Sec 3, 7, 9, App A, D, E |
| RENDERED sections | — | 4 | From V2 Knowledge Base |
| AUTHORED sections | — | 10 | By PEE editorial engine |
| Pending (human action) | — | 2 | See Action Register |

## 2. Editorial Transformations Applied

### 2.1 Content Filter

All V3 sections passed through `filter_client()` to remove: Knowledge Base metadata, document IDs, governance markers, AI sentinel paragraphs, and internal review notes. Total filtered: **21 segments**.

### 2.2 Boilerplate Strip

Oracle marketing boilerplate and overly technical passages detected by regex pattern matching. Total removed: **1 segments**.

### 2.3 Cross-Section Deduplication

Near-identical paragraphs detected across sections using MD5 hash on normalised text (first 300 chars). Duplicate instances removed from later sections. Total deduped: **12 segments**.

### 2.4 Page Budget Enforcement

Content segments per section capped at editorial budget. Over-budget sections truncated with cross-reference to appendix. Total truncated: **1066 segments**.

### 2.5 Authored Overlays

Six sections authored by PEE to replace placeholders or add new content: Proposed Oracle HCM Solution (Sec 3), Implementation Roadmap (Sec 7), Key Project Risks (Sec 9), HCM Capability Summary (App A), Reference Projects (App D), Glossary (App E). Total authored: **22 content segments**.

## 3. Section-by-Section Editorial Log

| V4 Section | Mode | V3 Segs | Budget | V4 Segs | Removed | Status |
|---|---|---|---|---|---|---|
| 1. Executive Summary | budgeted | — | 12 | 0 | — | AI_DRAFT |
| 2. Understanding Plennegy's Requirements | budgeted | — | 12 | 0 | — | AI_DRAFT |
| 3. Proposed Oracle HCM Solution | authored | — | 40 | 5 | — | AUTHORED |
| 4. Why APPSolve | budgeted | 72 | 24 | 25 | 48 | RENDERED |
| 5. Delivery Approach | budgeted | 144 | 40 | 41 | 104 | RENDERED |
| 6. Project Governance | budgeted | 6 | 24 | 6 | — | AUTHORED |
| 7. Implementation Roadmap | authored | — | 20 | 4 | — | AUTHORED |
| 8. Key Assumptions | budgeted | 5 | 24 | 5 | — | AUTHORED |
| 9. Key Project Risks and Mitigations | authored | — | 16 | 3 | — | AUTHORED |
| 10. Commercial Inputs | budgeted | 4 | 16 | 4 | — | AUTHORED |
| 11. Next Steps (Customer Actions) | budgeted | 3 | 12 | 3 | — | AUTHORED |
| Appendix A — Oracle HCM Capability Summary | authored | — | 20 | 4 | — | AUTHORED |
| Appendix B — Detailed Capability Catalogue | budgeted | 797 | 96 | 96 | 701 | RENDERED |
| Appendix C — Assumption Schedule | budgeted | 367 | 120 | 120 | 247 | RENDERED |
| Appendix D — Reference Projects | authored | — | 24 | 4 | — | AUTHORED |
| Appendix E — Glossary | authored | — | 16 | 2 | — | AUTHORED |

## 4. Readiness Assessment (V3 → V4)

| Criterion | V3 | V4 | Notes |
|---|---|---|---|
| Reads like a proposal | 4/5 | 4.5/5 | Authored sections improve narrative; KB sections still verbose |
| Structure | 4/5 | 5/5 | 11-section structure + 5 appendices — clean and evaluator-ready |
| Numbering | 5/5 | 5/5 | 1–11 body, A–E appendices |
| Evidence separated | 5/5 | 5/5 | Appendix B (capability), C (assumptions), D (references) |
| Capability conciseness | 3/5 | 4/5 | App A summary authored; App B still from KB but budgeted |
| Internal content removed | 4/5 | 5/5 | Client filter + boilerplate + dedup applied |
| New sections (roadmap, risks) | 0/5 | 4/5 | Authored roadmap + top-5 risks |
| Pending sections | 4/5 | 4/5 | Exec Summary + Understanding + Proposed Solution pending human |
| Commercial section | 4/5 | 4/5 | Authored; pricing still TBD (OAR-C02) |
| Next steps | 5/5 | 5/5 | Clear client action list with owners |
| **Overall** | **4.1/5** | **4.5/5** | **V4 ready for executive review before commercial sign-off** |

## 5. Remaining Human Actions (Critical Path)

| Priority | Action | Owner |
|---|---|---|
| **P0 URGENT** | Renew B-BBEE certificate before 2026-07-31 | Finance Director |
| P1 | Draft Executive Summary with Plennegy win themes | BU Lead |
| P1 | Draft Understanding of Requirements from RFP | Account Manager |
| P1 | Confirm scope (entities, headcount, go-live, payroll system) | AM (OAR-C04) |
| P1 | Provide commercial proposal and pricing | Commercial Director (OAR-C02) |
| P2 | Approve Hollywood Bets reference for this tender | AM (OAR-C01) |
| P2 | BU Lead review authored sections (Sec 3, 7, 9, App A, D) | BU Lead |
| P2 | Provide team structure and CVs | Delivery Manager |
| P3 | Verify all compliance document expiry dates | Operations |


*Generated by pee.py v1.0 (PF2-008) | 2026-06-30 15:11 | Platform L6.0*