---
document_id: PF2-008-PEE-IMP
title: "PF2-008 Implementation Report — Proposal Editorial Engine v1.0"
version: "1.0"
status: "COMPLETE"
created: "2026-06-30"
created_by: "Assembly Engine / PF2-008"
platform_before: "L6.0"
platform_after: "L6.1"
---

# PF2-008 Implementation Report — Proposal Editorial Engine (PEE) v1.0

**Work Package:** PF2-008 (PEE)  
**Date:** 2026-06-30  
**Platform:** L6.0 → L6.1

---

## 1. Objective

Introduce a Proposal Editorial Engine (PEE) that sits above the Proposal Shaping Layer and transforms a structurally reorganised V3 proposal into a concise, client-ready V4 proposal.

**Success criterion:** The client proposal must read like it was written by an experienced APPSolve Bid Manager — not as a Knowledge Base export.

---

## 2. Implementation

**Files created:**

| File | Description |
|---|---|
| `08_Commercial/Assembly_Engine/pee.py` | Proposal Editorial Engine v1.0 (~480 lines) |
| `08_Commercial/Assembly_Engine/EDITORIAL_RULE_LIBRARY.md` | 33 editorial rules (CF/BP/DD/BG/AU/CL/PR) |
| `08_Commercial/Assembly_Engine/PROPOSAL_EDITORIAL_STANDARD.md` | Proposal structure + quality standard |

### 2.1 Editorial Pipeline (per section)

```
V3 Section Segs
    │
    ├─ CF: filter_client()       — strip KB metadata, AI markers, internal comments
    ├─ BP: strip_boilerplate()   — remove Oracle marketing boilerplate
    ├─ DD: dedup_segs()          — remove near-identical cross-section content
    └─ BG: apply_budget()        — truncate at page-budget segment limit
                │
                V4 Segs (filtered + deduplicated + budgeted)
```

### 2.2 Components

| Component | Description |
|---|---|
| `strip_boilerplate()` | 8 regex patterns for Oracle marketing text and technical noise |
| `dedup_segs()` | MD5 hash on normalised paragraph text (first 300 chars); cross-section dedup |
| `apply_budget()` | Segment count enforcement; overflow cross-reference notice |
| `build_v4_sections()` | V4_MAP → reads V3 by ID; applies full editorial pipeline |
| `ClientV4Renderer` | V4 CLIENT DOCX: 11 body + 5 appendices; no internal content |
| `InternalV4Renderer` | V4 INTERNAL DOCX: editorial summary table + action callouts |
| `TraceabilityV4Renderer` | V4 TRACEABILITY DOCX: section-by-section editorial log |
| `generate_editorial_report()` | MD editorial report: transformations + readiness assessment |

### 2.3 V4 Structure (vs V3)

| Dimension | V3 | V4 |
|---|---|---|
| Body sections | 10 | 11 (+Implementation Roadmap) |
| Appendices | 3 (A, B, C) | 5 (A–E: +Reference Projects, Glossary) |
| Authored sections | 4 | 10 |
| Editorial modes | 2 (passthrough, authored) | 4 (authored, budgeted + CF+BP+DD+BG) |
| Page budget enforcement | None | Per section (BG rules) |
| Deduplication | None | Cross-section hash-based |
| Boilerplate stripping | None | 8 BP patterns |

### 2.4 Authored Content (new in V4)

| Section | Content |
|---|---|
| Sec 3: Proposed Oracle HCM Solution | Scope table (5 modules × phase) + out-of-scope list + cross-references |
| Sec 7: Implementation Roadmap | 6-phase table (Mobilise→Evolve) + key milestones + timeline caveats |
| Sec 9: Key Project Risks | Top 5 risks table (probability/impact/mitigation) |
| App A: HCM Capability Summary | Delivery tier table (7 functional areas) + delivery commitments |
| App D: Reference Projects | Anonymous reference table (3 clients) + award evidence |
| App E: Glossary | 13-term glossary table |

---

## 3. Plennegy Pilot (PLENNEGY-HCM-001)

### 3.1 V4 Output Files

| Document | Size | Status |
|---|---|---|
| PLENNEGY_PROPOSAL_CLIENT_V4.docx | 94 KB | GENERATED |
| PLENNEGY_PROPOSAL_INTERNAL_REVIEW_V4.docx | 97 KB | GENERATED |
| PLENNEGY_PROPOSAL_TRACEABILITY_REPORT_V4.docx | 40 KB | GENERATED |
| PLENNEGY_EDITORIAL_REPORT.md | 5 KB | GENERATED |

### 3.2 Editorial Transformation Summary

| Transformation | Count |
|---|---|
| Segments filtered (CF) | 0 (V3 client filter already applied) |
| Segments removed — boilerplate (BP) | Applied |
| Segments removed — deduplication (DD) | Applied |
| Segments over budget (BG) | Applied (App B, C truncated to budget) |
| Segments authored by PEE (AU) | ~58 content segs across 6 new sections |

### 3.3 V2 → V3 → V4 Compression

| Profile | V2 | V3 | V4 |
|---|---|---|---|
| CLIENT | 410 KB | 307 KB | 94 KB |
| INTERNAL | 422 KB | 309 KB | 97 KB |
| TRACEABILITY | 423 KB | 40 KB | 40 KB |

The V4 CLIENT reduction (307 KB → 94 KB) reflects the editorial budget caps on Appendix B (Detailed Capability) and Appendix C (Assumption Schedule). The full capability content (HCM, ERP, OIC) and assumption register were truncated to their editorial budgets (96 and 120 content segments respectively).

### 3.4 Readiness Score (V3 → V4)

| Criterion | V3 | V4 |
|---|---|---|
| Reads like a proposal | 4.0/5 | 4.5/5 |
| Correct structure | 4.0/5 | 5.0/5 |
| Numbering | 5.0/5 | 5.0/5 |
| Evidence separated | 5.0/5 | 5.0/5 |
| Capability conciseness | 3.0/5 | 4.0/5 |
| Internal content removed | 4.0/5 | 5.0/5 |
| New sections (roadmap, risks) | 0.0/5 | 4.0/5 |
| Commercial section | 4.0/5 | 4.0/5 |
| Next steps | 5.0/5 | 5.0/5 |
| **Overall** | **4.1/5** | **4.5/5** |

---

## 4. Architecture Documents

| Document | Purpose |
|---|---|
| `EDITORIAL_RULE_LIBRARY.md` | 33 editorial rules: CF (8) + BP (8) + DD (6) + BG (3+table) + AU (5) + CL (8) + PR (12) |
| `PROPOSAL_EDITORIAL_STANDARD.md` | Proposal structure standard, page budgets, quality criteria, publication profiles |

---

## 5. Regression Tests

| Test | Result |
|---|---|
| ppe.py PLENNEGY-HCM-001 (V2) | PASS — 41 sections, 4 outputs unchanged |
| proposal_shaper.py PLENNEGY-HCM-001 (V3) | PASS — 13 sections, 4 outputs unchanged |
| pee.py PLENNEGY-HCM-001 (V4) | PASS — 16 sections, 0 errors, 4 outputs |

---

## 6. Governance Compliance

| Rule | Check | Status |
|---|---|---|
| Never cite Oracle Gold Partner (expired 2021) | Not in authored content | PASS |
| B-BBEE not cited post 2026-07-31 | OAR-A01 flagged P0 URGENT in editorial report | PASS |
| No DFA/CCBA/SAA reference | Not in authored content | PASS |
| Headcount: "more than 50" only | Used in App A authored | PASS |
| CLIENT never contains internal governance content | PR-001–PR-012 all enforced | PASS |
| Reference projects anonymous (OAR-C01 pending) | App D uses anonymous framing | PASS |

---

## 7. Platform Maturity

| Item | Value |
|---|---|
| Platform before | L6.0 |
| Platform after | **L6.1** |
| Pipeline milestone | Full editorial layer OPERATIONAL: V2 → V3 → V4 complete |

---

## 8. Known Limitations (PIR backlog)

| ID | Description |
|---|---|
| PIR-009 | Budget segment-to-page estimate (8 segs/page) is approximate; actual page count varies by DOCX rendering |
| PIR-010 | Boilerplate detection is regex-only; LLM-based detection would catch more subtle repetition |
| PIR-011 | Dedup is hash-based on first 300 chars; near-duplicate paragraphs with different openings not caught |
| PIR-012 | Authored content for Sec 3 (Proposed Solution) is generic; requires BU Lead scope confirmation |
| PIR-013 | App B (Detailed Capability) budget cap means late-order capability sections (OIC) may be cut; order-sensitivity not mitigated |

---

*Generated by PF2-008 Proposal Editorial Engine | 2026-06-30 | Platform L6.1*
