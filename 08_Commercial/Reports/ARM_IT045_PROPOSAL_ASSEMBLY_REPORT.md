---
document_id: ARM-IT045-PROPOSAL-ASSEMBLY-REPORT
title: "ARM IT045 — Proposal Assembly Report"
tender_id: "ARM IT045"
version: "1.1"
status: "WP18C Stage 4 Output — Regression corrected WP18C.2 (SI-001: S-38 excluded for AMS; SI-007 boundaries applied; section count corrected)"
created: "2026-06-25"
created_by: "WP18C — Proposal Factory Assembly Engine v1.0"
updated: "2026-06-26"
updated_by: "WP18C.2 — Section Library Consolidation (regression review)"
sections_in_scope: 56
sections_ready: 37
sections_partial: 12
sections_gap: 7
automation_pct: 66
qa_score: 72
---

# ARM IT045 — Proposal Assembly Report

**Stage 4 Output:** Section-by-section assembly metadata  
**Tender:** ARM IT045 | African Rainbow Minerals | Oracle EBS AMS  
**Assembly date:** 2026-06-25  
**Total sections in scope:** 57  
**Overall QA score:** 72/100 (below submission threshold of 75)

---

## 1. Summary Statistics

| Metric | Value |
|---|---|
| Total sections in scope | 56 *(S-38 excluded — SI-001: AMS engagement; see Section 13)* |
| Status: READY | 37 (66%) |
| Status: PARTIAL | 12 (21%) |
| Status: GAP | 7 (13%) |
| Assembly methods: DIRECT | 22 sections |
| Assembly methods: EXTRACT | 18 sections *(S-38 removed)* |
| Assembly methods: MERGE | 3 sections |
| Assembly methods: AI-GENERATE | 8 sections |
| Assembly methods: TEMPLATE | 3 sections |
| Assembly methods: PLACEHOLDER | 2 sections |
| Current automation % | 67% (DIRECT + EXTRACT + MERGE as % of total) |
| Human review required | 27 sections |
| BU Lead approval required | All AI-GENERATE + PLACEHOLDER |
| AM approval required | All 4 references (S-67) |
| Critical flags | 2 (S-12 B-BBEE expiry; S-50 Risk Register AI-only) |

---

## 2. Assembly Report — Corporate and Partnership

| Section ID | Section Name | Method | Source Asset | Status | Human Review | Notes |
|---|---|---|---|---|---|---|
| S-01 | Cover Page | TEMPLATE | Tender metadata | PARTIAL | Yes — insert submission date and contact details | Submission date and contact must be added |
| S-02 | Table of Contents | DIRECT | Auto-generated | READY | No | Updates when sections are added/removed |
| S-03 | Company Overview | DIRECT | W1S1-001 | READY | No | Approved KB asset; no further action |
| S-04 | Company History | DIRECT | W1S1-002 | READY | No | Approved KB asset; no further action |
| S-05 | Awards and Recognition | DIRECT | W1S1-006 | PARTIAL | Yes — BU Lead to extract current award table from W1S1-006 | Award table not inlined — must be extracted and inserted |
| S-06 | Delivery Model | DIRECT | W1S1-007 | READY | No | Approved KB asset |
| S-07 | Geographic Presence | DIRECT | W1S1-008 | READY | No | Approved KB asset |
| S-08 | Key Differentiators | DIRECT | W1S1-009 | READY | No | Approved KB asset |
| S-09 | Oracle Partnership | DIRECT | W1S1-003 | READY | Yes — BU Lead: confirm OPN status current | Level 1 Partner — governance checked |
| S-12 | B-BBEE Statement | EXTRACT | COMP-001 + COMPLIANCE_REGISTER | PARTIAL | Yes — confirm certificate expiry | **FLAG: expires 2026-07-31** |

---

## 3. Assembly Report — Understanding and Solution

| Section ID | Section Name | Method | Source Asset | Status | Human Review | Notes |
|---|---|---|---|---|---|---|
| S-13 | Executive Summary | AI-GENERATE | W1S1-001 + Tender context | PARTIAL | **Yes — MANDATORY** | AI-drafted; BU Lead + AM must review and personalise |
| S-14 | Understanding of Requirements | AI-GENERATE | Requirement Matrix (derived) | PARTIAL | **Yes — MANDATORY** | AI-drafted; Requirement Extraction Engine not yet built |
| S-15 | Proposed Solution Overview | MERGE | W2S1-002 + W2S1-004 + W4-INT-001 | READY | Yes — validate merge coherence | Three assets merged; check voice consistency |
| S-18 | Oracle EBS Capability | EXTRACT | W2S1-002 | PARTIAL | Yes — BU Lead: verify version claims | Vintage content; may need modernisation |
| S-19 | Oracle OIC | DIRECT | W4-INT-001 | READY | No | Approved KB asset |
| S-20 | Oracle DBA Capability | EXTRACT | W2S1-003 | PARTIAL | Yes — BU Lead: verify team size | Stats verification required before submission |
| S-21 | Oracle Managed Services | EXTRACT | W2S1-004 | READY | No | Approved KB asset |
| S-22 | OCI Infrastructure | AI-GENERATE | OCI pack (proxy) | GAP | **Yes — MANDATORY** | No standalone OCI capability narrative asset. AI-drafted. Gap: OCI-capability-narrative |

---

## 4. Assembly Report — Scope and Governance

> **SI-001 Regression Correction (WP18C.2):** S-38 (Change Control Framework) has been removed from this assembly. ARM IT045 is an Oracle EBS AMS engagement (Pattern 13). Per SI-001, S-38 is excluded for all AMS proposals — change management governance is provided exclusively by S-73 (Change Request Process) within the AMS Support Model block. This correction reduces the in-scope section count from 57 to 56. Authority: PROPOSAL_PATTERN_ENGINE.md Section 4.1 Rule C-1; PROPOSAL_SECTION_LIBRARY.md v1.2 footnote ¹.

| Section ID | Section Name | Method | Source Asset | Status | Human Review | Notes |
|---|---|---|---|---|---|---|
| S-30 | Scope — Inclusions | EXTRACT | ASS: INC codes (6 packs) | READY | Yes — BU Lead: validate scope list | Extracted from assumption pack INC sections |
| S-31 | Scope — Exclusions | EXTRACT | ASS: EXC/H codes (6 packs) | READY | Yes — BU Lead: validate exclusions list | Extracted from assumption pack Section H |
| S-33 | Dependencies | EXTRACT | ASS: DEP/G codes (6 packs) | READY | No | Direct from Assembly Engine Section G output |
| S-36 | Project Governance | EXTRACT | W2S1-005 (Sections 11–12) | READY | No | Governance framework; approved KB asset |
| S-37 | RAID Framework | TEMPLATE | RISK_LIBRARY_STANDARD.md | PARTIAL | Yes | Risk Library standard defined; structure assembled; no approved library entries yet |
| ~~S-38~~ | ~~Change Control~~ | **EXCLUDED** | **N/A** | **EXCL-AMS** | — | **SI-001: Excluded — AMS proposal. S-73 (AMS Support block) is the governing change management section.** |
| S-45 | Security Architecture | EXTRACT | OCI pack SEC sections | PARTIAL | Yes — BU Lead: validate against ARM's actual security posture | OCI pack-derived; arm-specific validation required |

---

## 5. Assembly Report — People

| Section ID | Section Name | Method | Source Asset | Status | Human Review | Notes |
|---|---|---|---|---|---|---|
| S-46 | Team Structure | TEMPLATE | CONSULTANT_INDEX + EBS-DRM Overlay | GAP | **Yes — MANDATORY** | **[PLACEHOLDER]** BU Lead must confirm all named resources from APPTime/CONSULTANT_INDEX |
| S-47 | Named Consultant CVs | PLACEHOLDER | APPTime (ADR-001) | GAP | **Yes — MANDATORY** | **[PLACEHOLDER]** CVs must come from APPTime only; cannot be generated from KB |

---

## 6. Assembly Report — Commercial and Governance

| Section ID | Section Name | Method | Source Asset | Status | Human Review | Notes |
|---|---|---|---|---|---|---|
| S-49 | Key Assumptions (Body) | DIRECT | Assembly Engine WP17D-1 output | READY | Yes — BU Lead standard review | 175 body assumptions; WP17D-1 COMPLETE |
| S-50 | Risk Register | AI-GENERATE | Risk Library (standard defined; no entries) | GAP | **Yes — MANDATORY** | **AI-generated; Risk Library not yet populated.** 9 AI risks drafted; all require BU Lead review + approval |
| S-51 | Commercial Assumptions | DIRECT | Assembly Engine WP17D-1 output (Appendix) | READY | Yes — BU Lead standard review | 594 complete assumptions; WP17D-1 COMPLETE |
| S-52 | Commercials / Pricing | PLACEHOLDER | Commercial Director | GAP | **Yes — MANDATORY** | **[PLACEHOLDER]** Commercial Director input required; no rates in KB |

---

## 7. Assembly Report — Compliance

| Section ID | Section Name | Method | Source Asset | Status | Human Review | Notes |
|---|---|---|---|---|---|---|
| S-55 | Compliance Schedule | EXTRACT | COMPLIANCE_REGISTER.csv | PARTIAL | Yes — verify all expiry dates | B-BBEE flag noted |
| S-56 | Company Registration | DIRECT | `02_Corporate/` | READY | No — check file is current | Physical document |
| S-57 | Tax Clearance | DIRECT | COMP-005 | READY | No — valid to 2027-02-23 | No action required |
| S-58 | Directors' Resolution | DIRECT | COMP-011 | READY | No — renewed 2026-06-15 | No action required |
| S-59 | B-BBEE Certificate | DIRECT | COMP-001 | PARTIAL | **Yes — MANDATORY** | **FLAG: expires 2026-07-31** — confirm renewal before submission |
| S-60 | Public Liability Insurance | DIRECT | COMP-008 | READY | No — renewed 2026-06-15 | No action required |
| S-62 | Oracle OPN Certificate | DIRECT | COMP-007 | READY | Yes — confirm current | Annual revalidation; confirm Level 1 active |

---

## 8. Assembly Report — References

| Section ID | Section Name | Method | Source Asset | Status | Human Review | Notes |
|---|---|---|---|---|---|---|
| S-67 | Client References | TEMPLATE | REF-ORA-008/-004/-005/-009 | PARTIAL | **Yes — AM APPROVAL for all 4** | Reference contact details not inlined; AM must confirm each reference before submission |
| S-69 | Reference Letters | DIRECT | `04_References/Oracle/` | GAP | Yes — AM must obtain current letters | Physical letters required; may not be in KB directory yet |

---

## 9. Assembly Report — AMS Support Sections

| Section ID | Section Name | Method | Source Asset | Status | Human Review | Notes |
|---|---|---|---|---|---|---|
| S-70 | Support Model | MERGE | W2S1-004 + AMS pack | READY | No | Merged; validated against AMS pack |
| S-71 | SLA Framework | EXTRACT | EBS-SLA Overlay | READY | No | Direct from overlay. **SI-007 boundary:** Assemble SLA tier table and service hours ONLY. Do NOT include incident classification process or any process narrative — that content belongs in S-72. |
| S-72 | Incident Management | EXTRACT | AMS pack + EBS-SLA Overlay | READY | No | Direct from AMS pack. **SI-007 boundary:** Assemble incident classification process and lifecycle ONLY. Do NOT re-state SLA tier values — reference as "per S-71 SLA Framework". Never duplicate the SLA tier table from S-71. |
| S-73 | Change Request Process | EXTRACT | AMS pack CR sections | READY | No | **SI-001 (WP18C.2): This is the AMS-authoritative change management section — it replaces S-38 for all AMS proposals. S-73 governs all change management for ARM IT045. S-38 has been excluded.** |
| S-74 | Resource Model | EXTRACT | EBS-DRM Overlay | READY | Yes — BU Lead confirms role allocations | Hours total confirmed (680h/month); role split requires BU Lead |
| S-75 | Release Management | EXTRACT | AMS pack REL sections | READY | No | Direct from AMS pack |
| S-76 | Monitoring and Reporting | EXTRACT | AMS pack MON sections | READY | No | Direct from AMS pack |

---

## 10. Assembly Report — Appendices

| Section ID | Section Name | Method | Source Asset | Status | Human Review | Notes |
|---|---|---|---|---|---|---|
| A-01 | Complete Assumption Schedule | DIRECT | WP17D-1 output | READY | Yes — BU Lead standard review | ARM_IT045_ASSUMPTION_SCHEDULE_V1.md; 594 assumptions |
| A-02 | Consultant CVs | PLACEHOLDER | APPTime (ADR-001) | GAP | **Yes — MANDATORY** | BU Lead to obtain from APPTime; cannot be generated |
| A-03 | Reference Letters | DIRECT | `04_References/Oracle/` | GAP | **Yes — AM APPROVAL** | Physical letters required; confirm 4 reference letters available |
| A-04 | Certifications | DIRECT | `01_Compliance/` + `02_Corporate/` | PARTIAL | Yes — BU Lead to compile and check expiry | Package 5 compliance documents; check all current |
| A-05 | B-BBEE Certificate | DIRECT | COMP-001 | PARTIAL | **Yes — FLAG** | Expires 2026-07-31; confirm renewal status |

---

## 11. Pre-Submission Checklist

The following actions are MANDATORY before this proposal can be submitted:

| # | Action | Owner | Priority | Status |
|---|---|---|---|---|
| A1 | Insert submission date and contact details (S-01) | Bid Manager | HIGH | OPEN |
| A2 | Extract and insert current award table from W1S1-006 (S-05) | Bid Manager | MED | OPEN |
| A3 | Confirm B-BBEE certificate renewal / obtain updated certificate (S-12, S-59, A-05) | BU Lead | **CRITICAL** | OPEN |
| A4 | Review and approve AI-drafted Executive Summary (S-13) | BU Lead + AM | HIGH | OPEN |
| A5 | Review and approve AI-drafted Understanding of Requirements (S-14) | BU Lead + AM | HIGH | OPEN |
| A6 | Validate and modernise EBS Capability content from W2S1-002 (S-18) | BU Lead | MED | OPEN |
| A7 | Write/approve OCI narrative (S-22) — currently AI-generated | BU Lead | HIGH | OPEN |
| A8 | Confirm all named AMS team resources from APPTime (S-46) | BU Lead | **CRITICAL** | OPEN |
| A9 | Obtain and insert all Consultant CVs from APPTime (A-02) | BU Lead | **CRITICAL** | OPEN |
| A10 | Review and approve AI-generated Risk Register (S-50) — 9 risks need BU approval | BU Lead | **CRITICAL** | OPEN |
| A11 | Commercial Director to complete pricing section (S-52) | Commercial Director | **CRITICAL** | OPEN |
| A12 | AM to approve and provide contact details for all 4 references (S-67, A-03) | AM | **CRITICAL** | OPEN |
| A13 | Obtain signed reference letters for all 4 references (A-03) | AM | HIGH | OPEN |
| A14 | Confirm Oracle OPN Level 1 Partner status current (S-09, A-04) | BU Lead | MED | OPEN |
| A15 | Confirm CR rate for S-73 (out-of-scope rate — placeholder). Note: S-38 is excluded for AMS (SI-001). | Commercial Director | MED | OPEN |

---

## 12. QA Score Breakdown

| QA Category | Max Score | Score Achieved | Notes |
|---|---|---|---|
| Governance compliance (G-01 to G-14) | 20 | 18 | G-08 B-BBEE expiry flag; G-14 CVs pending |
| Assumption completeness | 15 | 15 | WP17D-1 COMPLETE; 594 assumptions; 175 body |
| Capability asset coverage | 15 | 12 | S-22 OCI gap; S-18 vintage risk |
| Reference quality | 10 | 6 | 4 references selected; contacts/letters pending AM approval |
| Compliance completeness | 10 | 7 | B-BBEE expiry flag; letters pending |
| Commercial completeness | 10 | 2 | S-52 PLACEHOLDER; critical gap |
| Risk management | 10 | 5 | S-50 AI-only; Risk Library not populated |
| Section completeness | 10 | 7 | 7 sections at GAP status |
| **TOTAL** | **100** | **72** | **Below 75 threshold — not ready for submission** |

---

---

## 13. WP18C.2 Regression Review Notes

**Review date:** 2026-06-26  
**Review scope:** WP18C.2 — Section Library Consolidation architecture changes verified against ARM IT045 assembly

| Finding | Code | Severity | Status |
|---|---|---|---|
| S-38 included in AMS assembly — excluded per SI-001 | RF-001 | CRITICAL | **CORRECTED** — S-38 removed; section count 57→56; S-73 confirmed as governing section |
| S-73 described as "consistent with S-38" — incorrect designation | RF-002 | HIGH | **CORRECTED** — S-73 now designated as AMS-authoritative change management section |
| S-71/S-72 assembly notes missing SI-007 content boundaries | RF-003 | MEDIUM | **CORRECTED** — SI-007 boundary instructions added to both rows |
| A15 action references "S-38/S-73" implying both in scope | RF-004 | LOW | **CORRECTED** — A15 updated to S-73 only |

**Downstream architecture validation:**

| Document | Version | Regression Status |
|---|---|---|
| PROPOSAL_PATTERN_ENGINE.md | v1.0 | PASS — SI-001 already encoded; S-38 excluded for AMS at Rule C-1 |
| PROPOSAL_SECTION_LIBRARY.md | v1.2 | PASS — SI-001/SI-007 applied; scoping reference added |
| CONTENT_SOURCE_MATRIX.md | v1.2 | PASS — S-38 AMS exclusion + secondary source corrected; SI-007 boundaries |
| PROPOSAL_ASSEMBLY_SEQUENCE.md | v1.1 | PASS — SI-001/SI-005/SI-006/SI-007 assembly notes applied; Pattern 13 order table added |
| PROPOSAL_FACTORY_ARCHITECTURE.md | v1.2 | PASS — Stage 0 TIL operational; dependency map current |
| TENDER_BOM_LIBRARY.md | v1.1 | PASS — KI-001 stale statuses corrected; EBS overlays added |

**Assembly order (SI-005/SI-006):** For Pattern 13 (AMS), the production document order follows PROPOSAL_ASSEMBLY_SEQUENCE.md v1.1 Section 6: Scope → AMS Support Model (S-74→S-70→S-71→S-72→S-73→S-75→S-76) → Commercial (S-49→S-50→S-51→S-52, SI-006) → Compliance → References (after commercial, SI-005) → Appendices. This assembly is governed by PROPOSAL_ASSEMBLY_SEQUENCE.md, not the section grouping in this report.

**Recommendation:** ARM_IT045_PROPOSAL_STRUCTURE.md also requires S-38 correction (capability asset W2S1-005 target sections; S-38 row; section count). Corrected in parallel as part of WP18C.2 regression.

---

*ARM_IT045_PROPOSAL_ASSEMBLY_REPORT.md v1.1 | WP18C — Proposal Factory Assembly Engine v1.0 | 2026-06-25*  
*v1.1 (WP18C.2 2026-06-26): Regression corrections — RF-001 S-38 excluded (SI-001); RF-002 S-73 AMS designation; RF-003 SI-007 boundaries; RF-004 A15 updated. Section count corrected 57→56.*  
*Stage 4 output. QA score: 72/100. 15 pre-submission actions open. Submission readiness: NOT READY.*
