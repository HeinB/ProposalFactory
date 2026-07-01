---
document_id: PLENNEGY-ASSEMBLY-TEST
title: "Plennegy Proposal — Assembly Engine Test"
version: "1.0"
created: "2026-06-16"
created_by: "WP12 — Proposal Assembly Engine"
status: "Active"
---

# Plennegy Proposal — Assembly Engine Test

**Purpose:** Applies the WP12 Proposal Assembly Engine to the Plennegy Oracle HCM Full Suite tender (Track A). Produces the corrected assembly specification, identifies submission blockers, and documents known gaps.

**Source documents:** PLENNEGY_COVERAGE_REPORT.md; PLENNEGY_READINESS_SCORECARD.md; PLENNEGY_QUESTION_MATRIX.md; V3 draft (PLENNEGY_DRAFT_RESPONSE.docx)
**Rules engine applied:** ASSEMBLY_RULES_ENGINE.md v1.0
**BOM applied:** TENDER_BOM_LIBRARY.md BOM 1 (Oracle HCM Full Suite)

---

## 1. Engagement Parameters

| Parameter | Value |
|---|---|
| Client | Plennegy Pty Ltd |
| Client sector | Agribusiness / Agricultural Holdings |
| Tender track | Track A — Oracle HCM Full Suite |
| Modules in scope | Core HR, Absence Management, Journeys, AI Skills, Recruiting Cloud, Learning Cloud, Talent Management, Workforce Compensation, Payroll Interface (OIC ↔ PaySpace) |
| Payroll parallel run | INCLUDED by default (HCM-CUT-005) — unless Plennegy provides written waiver |
| Modules NOT in scope | HR Help Desk, Oracle Analytics (primary scope) |
| Modules with known KB gap | Recruiting Booster (4/10 — no KB asset), Touch Points (2/10 — no KB asset) |
| Integration count | Minimum 1 (OIC ↔ PaySpace); additional integrations TBC per PLENNEGY_QUESTION_MATRIX.md |
| Implementation model | Phased go-live recommended (Wave 1: Core HR + Absence + Journeys + AI Skills + Payroll; Wave 2: Recruiting + Learning + Talent + Compensation) |
| Payroll cycle | TBC — confirm from Plennegy (OAR-C04) |
| AMS in scope | TBC — flag in proposal |

---

## 2. Capability Asset Manifest

Assets selected by applying ASSEMBLY_RULES_ENGINE.md Rules A1–A6 to Plennegy scope.

### 2A — Mandatory Corporate Block

| Asset | Name | Usage in Proposal |
|---|---|---|
| W1S1-001 | Company Overview | Company Profile section |
| W1S1-007 | Delivery Model | Delivery Model section |
| W1S1-008 | Geographic Presence | Company Profile section |
| W1S1-009 | Key Differentiators | Executive Summary and Company Profile |

### 2B — Oracle HCM Capability Assets

| Asset | Name | Section | Gov Restriction |
|---|---|---|---|
| W1S1-003 | Oracle Partnership Statement | Oracle Partnership | Level 1 only — no Gold claim |
| W2S1-005 | Oracle Implementation Methodology | Methodology chapter | D-W5-003/004/005/006 checks |
| W3S1-001 | HCM Core — Global HR | Solution: Core HR | HB AM required for named reference |
| W3S1-007 | Oracle Workforce Management | Solution: Absence Management | HB AM required for named reference |
| W4-HCM-002 | Oracle Journeys | Solution: Journeys | HB AM required |
| W4-AI-002 | Oracle AI Skills | Solution: AI Skills | Do not conflate with ODA or Oracle Grow |
| W3S1-003 | Recruiting Cloud | Solution: Recruiting | DFA Taleo internal only; HB AM required |
| W3S1-004 | Learning Cloud | Solution: Learning | Mr Price = Learning scope only (C-W3-002) |
| W3S1-002 | Talent Management | Solution: Talent | Redpath Rule 21.5; HB AM required |
| W3S1-005 | Workforce Compensation | Solution: Compensation | **G-001: Tier 2 only for Agribusiness — no named reference client; Mining = only sector with evidence** |
| W3S1-009 | Payroll Interface & Integration | Solution: Payroll Interface | **Strip Section 13.2 (PT-W9-008)**. Parallel run included (HCM-CUT-005). |
| W4-INT-001 | OIC Integration Accelerators | Solution: Integrations | **Scan and remove HIST-018 billing amounts** |

### 2C — Assets NOT Included

| Asset | Reason |
|---|---|
| W3S1-006 (HCM Analytics) | Not stated as primary scope — omit unless analytics is a specified Plennegy requirement |
| W3S1-008 (HR Help Desk) | Help Desk not in Plennegy scope |
| W4-ERP-001/002/003 (ERP modules) | Not in Plennegy scope |
| W2S1-002 (EBS) | Not in scope |
| W1S2-xxx (Acumatica) | Not in scope |
| W1S3-xxx (BeBanking) | Not in scope |

### 2D — KB Gaps (No Asset Available)

| Module / Feature | Coverage Score | Action |
|---|---|---|
| Oracle Recruiting Booster | 4/10 | No KB asset — describe at a high level using Oracle product documentation; flag as "Tier 3 — external source"; do NOT represent as APPSolve delivery evidence |
| Oracle Touch Points | 2/10 | No KB asset — same approach as Recruiting Booster; flag as gap |

---

## 3. Assumption Pack Selection

| Pack | Status | Action |
|---|---|---|
| HCM_BASE_ASSUMPTIONS_V1.md | **Approved** | INCLUDE as Appendix A — mandatory |
| OIC_ASSUMPTIONS_V1.md | **Approved** | INCLUDE as Appendix B — OIC integrations in scope |
| HCM Recruiting | Draft (7 BU items pending) | Reference with note: "Subject to BU Lead final approval — addendum may be issued prior to contract" |
| HCM Learning | Draft (5 BU items pending) | Same note |
| HCM Talent | Draft (4 BU items pending) | Same note |
| HCM Compensation | Draft (5 BU items pending) | Same note |
| AMS_ASSUMPTIONS_V1.md | **Approved** | INCLUDE only if post-implementation support is in scope |

---

## 4. Reference Selection

Apply ASSEMBLY_RULES_ENGINE.md Rules C1–C3.

| Ref | Client | Section Use | Status | Decision |
|---|---|---|---|---|
| REF-ORA-007 | Oracle Corporation SA | Partnership endorsement | Active — safe | **INCLUDE** — always |
| Hollywood Bets | Not registered | Full HCM suite; OIC; Recruiting; Absence | AM approval required | **CONDITIONAL** — use only if OAR-C01 resolved. Until then: "a major financial services and gaming company" in text |
| REF-ORA-006 | Mr Price Group | Learning Cloud section only | Active — scope restricted | **INCLUDE** in Learning section only (C-W3-002). Must NOT be used to imply broader HCM evidence |
| Agribusiness reference | None available | Sector match | No agribusiness reference in KB | **GAP** — flag in proposal; consider generic "agriculture/FMCG sector experience" if factually supportable |
| DFA | — | Any section | Permanently suppressed (Rule 21.4) | **EXCLUDE** |
| Redpath | — | Any section | Not referenceable until go-live | **EXCLUDE** (Rule 21.5) |
| CCBA | — | Any section | Permanently suppressed | **EXCLUDE** |
| KPMG | — | Any section | AM-W4E3-001 ACTIVE — blocked | **EXCLUDE** |

**Reference coverage outcome:** 2 confirmed references (Oracle endorsement + Mr Price Learning). Hollywood Bets = conditional on OAR-C01. No agribusiness sector reference available. Reference section score will remain sub-optimal (~40%) until Hollywood Bets signed letter is obtained.

---

## 5. Compliance Documents

| Document | Status at 2026-06-16 | Action |
|---|---|---|
| COMP-001 B-BBEE Level 3 | ACTIVE — expires **2026-07-31** | **FLAG** — check at submission: if submitted after 2026-07-31, certificate will be expired. Renewal is OAR-A01. |
| COMP-002 Tax Clearance PIN | ACTIVE — valid 2027-02-23 | Include |
| COMP-004 CIPC Registration Pack | Active | Include (COR14.3 + Disclosure + Cor39 + Beneficiary) |
| COMP-006 Bank Confirmation Letter | Must be < 3 months old | Refresh if older than 3 months from submission date |
| COMP-007 PI Insurance | Active | Include |
| COMP-008 PL Insurance | OBTAINED 2026-06-15 | Include — confirm exact policy document filename from broker |
| COMP-009 COIDA | Active | Include |
| COMP-011 Directors' Resolution | RENEWED 2026-06-15 — valid to June 2027 | Include |
| Public sector compliance (VAT/CSD/EE) | Not required | Plennegy is private sector |

---

## 6. Project Plan Template Selection

**Recommended:** Template 1 — Oracle HCM Full Suite (42 weeks) with phased go-live adaptation (Pattern 2).

**Recommended phasing for Plennegy:**
- **Wave 1 (Weeks 1–26):** Mobilize + SDD (all modules) → Prototype Wave 1 → Go-Live Wave 1
  - Wave 1 modules: Core HR, Absence Management, Journeys, AI Skills, Payroll Interface (OIC)
  - Wave 1 rationale: Foundational HR record-of-truth + payroll interface early go-live reduces parallel run period
- **Wave 2 (Weeks 20–42):** Prototype Wave 2 → Go-Live Wave 2
  - Wave 2 modules: Recruiting Cloud, Learning Cloud, Talent Management, Workforce Compensation
  - Wave 2 rationale: Talent suite modules can follow initial HR stabilisation

**Alternative (if client requires single go-live):** Template 1 (42 weeks, single go-live) — all modules simultaneously. Higher risk; requires stronger client steering committee commitment.

**Go-live date:** TBC — pending Plennegy project commencement confirmation (OAR-C04).

---

## 7. Team Category Recommendations

Based on CONSULTANT_INDEX.csv skill categories. BU Lead to select specific consultants; CVs from APPTime.

| Role | Category | Notes |
|---|---|---|
| Programme Manager | CON-XBU (Programme Manager category) | Large scope warrants Programme Manager above PM |
| Project Manager | CON-XBU or CON-ORA (PM-qualified) | Day-to-day delivery management |
| HCM Principal Consultant (Lead) | CON-ORA (HCM Principal) | Leads Core HR, Absence, Journeys |
| HCM Senior Consultant — Recruiting | CON-ORA (Recruiting specialist) | Confirm Recruiting Cloud certifications |
| HCM Senior Consultant — Learning | CON-ORA (Learning specialist) | Confirm Learning Cloud certifications |
| HCM Senior Consultant — Talent | CON-ORA (Talent specialist) | Confirm Performance/Succession modules |
| HCM Consultant — Compensation | CON-ORA (Compensation specialist) | Tier 2 coverage — confirm Compensation experience |
| OIC Integration Consultant | CON-ORA (OIC-tagged) | OIC ↔ PaySpace integration build + additional integrations |
| Data Migration Consultant | CON-ORA (Data/Migration-tagged) | HCM data migration lead |

**ADR-001 reminder:** Do NOT write CV text from KB records. Use CONSULTANT_INDEX.csv for skill matching only. Obtain CVs from APPTime.

---

## 8. Commercial Placeholders

All pricing fields must remain as placeholders until Commercial Director completes the commercial model.

| Section | Placeholder Text |
|---|---|
| Implementation Commercials | `[COMMERCIAL INPUT REQUIRED — BU Lead and Commercial Director to complete. Based on Estimation Input Model (ESTIMATION_INPUT_MODEL.md) completed for Plennegy engagement.]` |
| Post-Implementation AMS (if in scope) | `[AMS COMMERCIAL INPUT REQUIRED — retainer or allocated hours model to be confirmed. CRs billed T&M per AMS_ASSUMPTIONS_V1.md.]` |
| Payroll Parallel Run | Note: Parallel payroll run for minimum 1 pay cycle is included in scope as a standard deliverable (HCM-CUT-005). |
| Recruiting Booster / Touch Points | Note: "APPSolve is aware of the Recruiting Booster and Touch Points modules. Detailed delivery approach to be confirmed during Scope and Design phase. These modules are not reflected in the core implementation estimate above." |

---

## 9. Governance Violations in V3 — Required Corrections Before Submission

The following violations were identified in the V3 PLENNEGY_DRAFT_RESPONSE.docx and must be corrected before submission.

| Code | Violation Found in V3 | Required Correction | Rule |
|---|---|---|---|
| GOV-V3-001 | "110+ Senior Consultants" headcount claim | Change to "more than 50 Senior Consultants" | CROSS-1 |
| GOV-V3-002 | Nigeria, Uganda, Ghana listed as service countries | Remove — not in approved geographic list | W1S1-008 restriction |
| GOV-V3-003 | Bangladesh, Qatar listed as international markets | Remove — not in approved list | W1S1-008 restriction |
| GOV-V3-004 | Year count discrepancy (e.g., "22 years" or "19 years") | Correct: founded 2002; "more than 24 years" as of 2026; Hein's career "since 1996" | CROSS-1 |
| GOV-V3-005 | Award claims with unverified success story URLs | Omit unverified URLs (Tiger Brands, USAID, UT Grain) until BU confirms | D-W5-006 |
| GOV-V3-006 | Oracle Gold Partner reference | Change to "Oracle Partner Network" — Gold status expired 2021 | W1S1-003 restriction |

**Note:** Verify W3S1-009 Section 13.2 is NOT present in the submitted version (PT-W9-008). If it is, strip before submission.
**Note:** Verify W4-INT-001 does not contain HIST-018 billing amounts in the submitted version.

---

## 10. Missing Information (Required Before Submission)

| Item | Source | Who Provides | OAR Reference |
|---|---|---|---|
| Plennegy employee count, legal entity count, payroll cycle count | Client | Bid Manager to confirm from RFP or client meeting | OAR-C04 |
| Plennegy go-live date / desired cutover | Client | Bid Manager | OAR-C04 |
| OIC integration list and complexity | Client | Technical Lead to confirm during SDD | (new item) |
| Hollywood Bets AM approval | BU Lead / AM | Account Manager to request | OAR-C01 |
| Costing / commercial section content | Commercial Director | BU Lead to initiate Estimation Input Model completion | OAR-C02 |
| Word TOC (after all sections confirmed) | DOCX generation | Bid Manager | OAR-C03 |
| Oracle awards wording verification | BU Lead | BU Lead to confirm | OAR-C05 |
| Plennegy-specific company research (sector, size, parent group) | Internet / client | Bid Manager | N/A |

---

## 11. Submission Blockers

Items that MUST be resolved before the Plennegy proposal can be submitted:

| Priority | Blocker | Owner | Status |
|---|---|---|---|
| CRITICAL | OAR-C01 — AM approval for Hollywood Bets naming | Oracle BU Lead / AM | Open |
| CRITICAL | OAR-C02 — Costing section missing from draft | Commercial Director + BU Lead | Open |
| CRITICAL | OAR-C03 — Word TOC not generated | Bid Manager | Open — generate after sections confirmed |
| HIGH | GOV-V3-001 to GOV-V3-006 corrections | Bid Manager / KB | Must correct in V3 |
| HIGH | OAR-A01 — B-BBEE certificate valid at submission date | Finance Director | Certificate expires 2026-07-31 |
| MEDIUM | OAR-C04 — Client parameters (LE count, payroll, go-live date) | Bid Manager | Required for project plan and estimation |
| MEDIUM | OAR-C05 — Awards wording BU verification | Oracle HCM BU Lead | Required before submitting company profile |

**Items that are NOT blocking proposal assembly (but reduce quality):**
- No agribusiness sector reference (gap — accept lower reference score)
- HCM module assumption packs are Draft (flag with note in appendix)
- Recruiting Booster / Touch Points have no KB assets (flag in proposal)

---

## 12. Plennegy Readiness Summary

| Dimension | Score (from PLENNEGY_READINESS_SCORECARD.md) | Post-Engine Correction |
|---|---|---|
| HCM Core / Absence / Journeys / AI Skills | 10/10 | Maintained — fully covered by KB assets |
| Recruiting Cloud | 10/10 | Maintained — W3S1-003 covers this |
| Learning Cloud | 10/10 | Maintained — W3S1-004 + Mr Price reference |
| Talent Management | 10/10 | Maintained — W3S1-002 covers this |
| Workforce Compensation | 7/10 (Tier 2 only) | Maintained at Tier 2 — G-001 applies; no Agribusiness reference |
| Payroll Interface | 8/10 | Improves to ~9/10 after Section 13.2 stripped and HCM-CUT-005 parallel run confirmed |
| Recruiting Booster | 4/10 | Maintained — no KB asset; describe using Oracle documentation |
| Touch Points | 2/10 | Maintained — no KB asset; mention at high level only |
| Company Profile | 3/10 | **Improves to ~9/10 after GOV-V3-001–006 corrections applied** |
| Reference Coverage | 28/60 (47%) | Improves to ~35/60 (~58%) with Mr Price (Learning) confirmed; to ~48/60 (~80%) if Hollywood Bets AM approved |

**Estimated overall score post-engine correction (without HB):** ~72–76/100
**Estimated overall score post-engine correction (with HB):** ~84–88/100

---

*PLENNEGY_ASSEMBLY_TEST v1.0 | WP12 — Proposal Assembly Engine | 2026-06-16*
*Companion: TENDER_BOM_LIBRARY.md | ASSEMBLY_RULES_ENGINE.md | PLENNEGY_READINESS_SCORECARD.md*
