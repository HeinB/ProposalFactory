---
document_id: NEXT-WORK-PACKAGE
title: Next Work Package Pointer
last_updated: "2026-07-01"
last_completed: PF2-010 (V5)
platform_maturity: L6.5
---

# Next Work Package

**Last completed:** PF2-010 — Proposal V5 Narrative & Style Engine v1.0 (2026-06-30)
**Platform maturity:** L6.5
**Session closed:** 2026-07-01

---

## ⚠ IMMEDIATE NEXT ACTION — HUMAN GATE

**The next step is human review, not AI engine work.**

1. **Open** `08_Commercial/Proposals/PLENNEGY-HCM-001/CLIENT_PROPOSAL_PLENNEGY_V5.docx`
2. **Read** the full proposal as a client would read it
3. **Assess:**
   - Does Section 1 (Executive Summary) reflect the real Plennegy engagement?
   - Does Section 2 (Understanding) capture what APPSolve knows about Plennegy?
   - Is the narrative tone right for the specific decision-maker receiving this?
   - Are there any factual errors based on knowledge the AM holds that is not in the KB?
4. **Edit** directly in Word if adjustments are needed
5. **Then** resolve commercial blockers (see Open Human Actions below)

Do not start the next AI work package until the human review is complete.

---

## Open Human Actions (Plennegy Blockers)

| ID | Action | Owner | Deadline | Status |
|---|---|---|---|---|
| OAR-A01 | Renew B-BBEE Level 3 certificate | Finance Director | **2026-07-31 URGENT** | OPEN |
| OAR-C01 | AM approval to name Hollywood Bets as reference in this tender | Account Manager | Before submission | OPEN |
| OAR-C02 | Commercial Director to issue formal Commercial Proposal once scope confirmed | Commercial Director | After OAR-C04 | OPEN |
| OAR-C04 | AM to confirm scope inputs from Plennegy: entities, headcount, modules, go-live date | Account Manager | Before OAR-C02 | OPEN |

---

## Completed Work Packages (Proposal Factory Phase 2)

| WP | Name | Status | Date |
|---|---|---|---|
| PF2-001 | Risk Selection Engine (rse.py v1.0) | COMPLETE | 2026-06-29 |
| PF2-002 | Assembly Rule Enrichment Engine (are.py v1.0) | COMPLETE | 2026-06-29 |
| PF2-003 | Proposal Section Assembly Engine (proposal_section_engine.py v1.0) | COMPLETE | 2026-06-29 |
| PF2-004 | Markdown Proposal Renderer (proposal_renderer.py v1.0) | COMPLETE | 2026-06-29 |
| PF2-004A | DOCX Renderer (docx_renderer.py v1.0) | COMPLETE | 2026-06-30 |
| PF2-005 | Assumption Library Materialisation | COMPLETE | 2026-06-30 |
| PF2-006 | Operational Validation: Plennegy BOM | COMPLETE | 2026-06-30 |
| PF2-007 | Proposal Publishing Engine (ppe.py v1.0) | COMPLETE | 2026-06-30 |
| PF2-008A | Proposal Shaping Layer (proposal_shaper.py v1.0) | COMPLETE | 2026-06-30 |
| PF2-008 | Proposal Editorial Engine (pee.py v1.0) | COMPLETE | 2026-06-30 |
| PF2-009 (PAE) | Proposal Authoring Engine (proposal_authoring_engine.py v1.0) | COMPLETE | 2026-06-30 |
| PF2-010 (PPPE) | Proposal Publishing Policy Engine (proposal_publishing_policy.py v1.0) | COMPLETE | 2026-06-30 |
| PF2-009 (PNE) | Proposal Narrative Engine (proposal_narrative_engine.py v1.0) | COMPLETE | 2026-06-30 |
| PF2-010 (V5) | Proposal V5 Narrative & Style Engine (proposal_v5_engine.py v1.0) | COMPLETE | 2026-06-30 |

---

## Governing Standards (Post-V5)

These standards apply to all future proposal engine work and human authoring:

| Standard | Document | Rule |
|---|---|---|
| **V5 Narrative Style** | `PROPOSAL_STYLE_GUIDE.md` (TD-027) | Every section answers: challenge / proposal / why / outcome. No knowledge dumps, no Oracle feature lists. |
| **OUM Prohibition** | GOV-PAE-001 (permanent) | Fusion Cloud proposals must use Oracle Modern Best Practices / Oracle Success Navigator. OUM is prohibited. |
| **No regression** | — | Future engines must not regress to V2 knowledge-dump output. V5 readiness (91/100) is the floor. |
| **Client proposal clean room** | — | No IDs, no governance artefacts, no draft markers, no KB content verbatim in client output. |

---

## Open Candidate Work Packages (AI)

| Priority | WP | Name | Notes |
|---|---|---|---|
| 1 | — | **Human Review Gate** | Review CLIENT_PROPOSAL_PLENNEGY_V5.docx before any further engine work |
| 2 | PIR-001 | Sub-section EXTRACT Renderer | Extract subsections by heading from methodology assets — resolves Scope of Work PLACEHOLDERs for future tenders |
| 3 | PF3-001 | Live Tender Context Extractor | Parse RFP/tender documents to auto-populate tender context YAML; enables Section 2 (Understanding) to be populated from client documents |
| 4 | KB-W5 | Wave 5 Knowledge Assets | Oracle Recruiting Booster; Oracle Touch Points; Agribusiness sector context; RAID Framework template; Proposed Solution Overview |
| 5 | PIR-005 | V5 Executive Summary Generator | Generate Plennegy-specific win-theme executive summary using tender profile + BOM + AM notes |

---

*Update this file at the start of each work package and on completion.*
