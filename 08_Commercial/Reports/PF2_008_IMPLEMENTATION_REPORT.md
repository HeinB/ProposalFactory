---
document_id: PF2-008-IMP
title: "PF2-008 Implementation Report — Proposal Shaping Layer"
version: "1.0"
status: "COMPLETE"
created: "2026-06-30"
created_by: "Assembly Engine / PF2-008"
platform_before: "L5.9"
platform_after: "L6.0"
---

# PF2-008 Implementation Report — Proposal Shaping Layer

**Work Package:** PF2-008  
**Date:** 2026-06-30  
**Platform:** L5.9 → L6.0

---

## 1. Objective

Introduce a Proposal Shaping Layer that transforms the V2 rendered proposal (output of PPE, PF2-007)
into a concise, persuasive, client-ready V3 structured proposal.

The shaping layer does not redesign the platform — it reads V2 DOCX/MD output and applies editorial
transformation rules to produce V3 outputs for three audiences.

**Success criteria:** V3 must read like a proposal, not a knowledge base export.

---

## 2. Implementation

**File created:** `08_Commercial/Assembly_Engine/proposal_shaper.py` v1.0

| Metric | Value |
|---|---|
| Engine lines | ~570 |
| Modes implemented | 5 (passthrough, full, full_multi, authored, authored_with_excerpt) |
| Authored sections | 4 (Governance, Assumptions Summary, Commercial, Next Steps) |
| Output profiles | 3 DOCX + 1 MD report |
| Pilot: PLENNEGY-HCM-001 | 4 outputs, 0 errors |

### 2.1 Core Components

| Component | Description |
|---|---|
| `group_v2()` | Parse MD → group flat Seg list into V2Sec objects by H2 headings |
| `classify_v2()` | Assign RENDERED/PLACEHOLDER/AI_DRAFT/EMPTY to each V2 section |
| `filter_client()` | Strip internal metadata, markers, governance comments for CLIENT |
| `excerpt()` | Extract first N content segments from a section |
| `build_v3_sections()` | Apply V3_MAP definition to produce V3Sec list from V2 index |
| `ClientV3Renderer` | CLIENT DOCX: pending notices for gaps; authored + rendered for complete |
| `InternalWorkbookV3Renderer` | INTERNAL DOCX: action register, V3→V2 map, full content with callouts |
| `TraceabilityReportV3Renderer` | TRACEABILITY DOCX: section-by-section transformation log |
| `generate_review_report()` | MD report: structural comparison, readiness scores, remaining gaps |
| `run_shaper()` | Orchestrator: parse → build → render all 4 outputs |

### 2.2 V3 Section Mapping

| V3 Section | Mode | V2 Sources |
|---|---|---|
| 1. Executive Summary | passthrough | V2 AI-Draft section |
| 2. Understanding of Requirements | passthrough | V2 AI-Draft section |
| 3. Proposed Oracle HCM Solution | passthrough | V2 PLACEHOLDER |
| 4. Why APPSolve | full_multi | 7 V2 credential sections (Secs 1–7) |
| 5. Delivery Approach | full | V2 Implementation Methodology + scope notices |
| 6. Project Governance | authored | Governance table + RAID/Cutover placeholders |
| 7. Key Assumptions | authored_with_excerpt | Authored category summary (341 assumptions) |
| 8. Key Risks and Mitigations | passthrough | V2 AI-Draft Risk Register |
| 9. Commercial Inputs Required | authored | Commercial framework + pricing model table |
| 10. Next Steps | authored | 10-row priority action table with owners |
| Appendix A | full_multi | V2 HCM + ERP + OIC capability sections (full) |
| Appendix B | full | V2 Assumptions Register (full) |
| Appendix C | passthrough | V2 Client References |

### 2.3 Authored Content

| Section | Content |
|---|---|
| Governance | 4-layer governance table (Steering/PM/Workstream/CCB) + 3 paragraphs + RAID/Cutover placeholders |
| Assumptions Summary | 5-pack category table (341 total) + 6 key commercial assumptions + App B cross-reference |
| Commercial | Commercial framework intro + 5-item input checklist + 3-model comparison table + disclaimer |
| Next Steps | 10-priority action table (P0–P3) with owners and target dates |

---

## 3. Plennegy Pilot (PLENNEGY-HCM-001)

### 3.1 Output Files

| Document | Size | Status |
|---|---|---|
| PLENNEGY_PROPOSAL_CLIENT_V3.docx | 307 KB | GENERATED |
| PLENNEGY_PROPOSAL_INTERNAL_REVIEW_WORKBOOK_V3.docx | 309 KB | GENERATED |
| PLENNEGY_PROPOSAL_TRACEABILITY_REPORT_V3.docx | 40 KB | GENERATED |
| PLENNEGY_V2_TO_V3_REVIEW_REPORT.md | 5 KB | GENERATED |

### 3.2 V2 → V3 Structural Change

| Dimension | V2 | V3 |
|---|---|---|
| Body sections | 37 numbered | 10 numbered (1–10) |
| Appendices | 3 (A, D, E) | 3 (A, B, C) |
| Credential sections in body | 7 | 1 (consolidated) |
| Capability sections in body | 3 | 0 (moved to Appendix A) |
| Compliance sections in body | 7 | 0 (separate submission) |
| Authored sections | 0 | 4 |
| CLIENT V3 size vs CLIENT V2 | 410 KB | 307 KB (−25%) |

### 3.3 Section Status (V3 Body)

| Status | Count | Sections |
|---|---|---|
| RENDERED | 2 | Why APPSolve; Delivery Approach |
| AUTHORED | 4 | Governance; Assumptions; Commercial; Next Steps |
| AI_DRAFT | 3 | Executive Summary; Understanding; Risk Register |
| PLACEHOLDER | 1 | Proposed Oracle HCM Solution |

### 3.4 Readiness Score (V2 → V3)

| Criterion | V2 | V3 |
|---|---|---|
| Reads like a proposal | 3/5 | 4/5 |
| Structure | 2/5 | 4/5 |
| Numbering | 2/5 | 5/5 |
| Credential conciseness | 2/5 | 4/5 |
| Evidence separated | 1/5 | 5/5 |
| Pending visibility | 3/5 | 4/5 |
| Commercial section | 2/5 | 4/5 |
| Next steps clarity | 1/5 | 5/5 |
| **Overall** | **2.0/5** | **4.1/5** |

---

## 4. Regression Tests

| Test | Result |
|---|---|
| PPE (ppe.py) PLENNEGY-HCM-001 re-run | PASS — 41 sections, V2 unchanged |
| proposal_shaper.py PLENNEGY-HCM-001 | PASS — 0 errors, 4 outputs |
| CLIENT V3 / INTERNAL V3 / TRACEABILITY V3 | PASS — all saved |
| V2→V3 review report | PASS — generated |

---

## 5. Governance Compliance

| Rule | Check | Status |
|---|---|---|
| Never cite DFA/CCBA/SAA as client or reference | No such references in authored content | PASS |
| Never cite Oracle Gold Partner (expired 2021) | Not cited | PASS |
| B-BBEE not cited after 2026-07-31 | OAR-A01 flagged in authored Next Steps (P0 URGENT) | PASS |
| Never use headcount 100+ or 110+ | Not used | PASS |
| CLIENT profile strips KB metadata | filter_client() applied to all RENDERED sections | PASS |
| W2S1-005 (Methodology) only in Delivery Approach | PIR-001 Governance duplicate NOT reproduced in V3 | PASS |

---

## 6. Platform Maturity

| Item | Status |
|---|---|
| Platform before | L5.9 |
| Platform after | **L6.0** |
| Pipeline milestone | Proposal Factory complete + V3 Shaping Layer OPERATIONAL |

---

## 7. Remaining Items (PIR backlog — not blocking)

| ID | Description | Impact |
|---|---|---|
| PIR-001 | V2 Sec 21 (Governance) still duplicates Sec 19 in V2 RENDERED output | V3 AUTHORED governance replaces it — no client impact |
| PIR-006 | Sec 7 (Key Assumptions) in V3 uses authored summary only; full excerpt not applied | Low — App B cross-reference provided |
| PIR-007 | Assumption category counts (341) hard-coded to Plennegy BOM | Future: derive from registry dynamically |
| PIR-008 | Authored commercial section rates/model hard-coded | Future: derive from commercial YAML per tender |

---

*Generated by PF2-008 Proposal Shaping Layer | 2026-06-30 | Platform L6.0*
