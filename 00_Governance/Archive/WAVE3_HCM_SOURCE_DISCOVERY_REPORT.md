---
title: "Wave 3 Oracle HCM — Source Discovery Report"
version: "1.0"
created: "2026-06-12"
created_by: "Claude (AI — Wave 3 source discovery)"
status: "BU Lead Decisions CLOSED 2026-06-12 — Extraction Authorised"
purpose: "Source inventory and proposed extraction plan for Oracle HCM capability statements. Read before any Wave 3 extraction begins."
---

# Wave 3 Oracle HCM — Source Discovery Report

**Date:** 2026-06-12 | **Owner:** Hein Blignaut | **Phase:** Wave 3 Initiation  
**Status:** Source discovery complete — BU lead decisions required before extraction begins  
**KB destination:** `06_Capabilities/Oracle/Oracle_HCM/`

---

## 1. Executive Summary

Nine Oracle HCM source documents were identified in the Customers corpus. The SAA HCM RFP Response (June 2025) is the richest primary source: 1,270 paragraphs covering 24 confirmed HCM modules. The CCBA Oracle HCM RFP V2.0 (May 2025) is a close second with 598 paragraphs. The Hollywood Bets Accepted Proposal V5.0 (April 2023) is the strongest implementation proof document — it is the only ACCEPTED HCM proposal in the corpus and covers a go-live of July 2025 with 7,000 users.

Nine capability statements are proposed for Wave 3. Six HIST registrations are required before extraction begins (HIST-006, HIST-007, and four new entries). Four governance decisions are required from the BU lead.

**No extraction has been performed. This report is for planning and BU lead approval only.**

---

## 2. Source Document Inventory

### 2.1 Primary Sources — Full HCM Proposals

| HIST ID | Document | Date | Client | Location | Paragraphs | Status |
|---|---|---|---|---|---|---|
| **HIST-006** | APPSolve_SAA_RFP.docx | June 2025 | South African Airways | `Parties/Customers/South African Airways/HCM/1.Working/` | 1,270 | **Not yet registered in DOCUMENT_REGISTER** |
| **HIST-007** | APPSolve_HollywoodBets_Oracle Implementation 3rd part_V5.0.docx | April 2023 | Hollywood Bets | `Parties/Customers/Hollywood Bets/RFP/HCM and Payroll Implementation/Accepted proposal/` | 375 | **Not yet registered** |
| **HIST-014** *(new)* | APPSolve_CCBA_HCM_Solution_V2.0.docx | May 2025 | CCBA | `Parties/Customers/CCBA/Oracle HCM RFP/0. Submitted/` | 598 | **Not yet registered** |
| **HIST-015** *(new)* | APPSolve Afrocentric - HCM Proposal V4.0.docx | 2023 | Afrocentric Health | `Parties/Customers/Afrocentric Health/RFP/HCM 2023/` | 368 | **Not yet registered** |

### 2.2 Secondary Sources — Client Reference and Supplementary

| HIST ID | Document | Date | Location | Notes |
|---|---|---|---|---|
| **HIST-008** | RedPath Mining_APPSolve_RFI Reply Detail.docx | March 2026 | `Parties/Customers/RedPath Mining/Working/` | Already used in Wave 2 (W2S1-001, W2S1-005). Contains HCM client list and OIC confirmation. |
| **HIST-016** *(new)* | APPSolve_SABS_RFP_Response.docx (SABS ETS — Oracle Fusion) | Dec 2025 | `Parties/Customers/SABS/RFP/ETS - Oracle Fusion/` | 77 paragraphs — primarily reference client tables. Source for confirmed HCM reference clients (Mr Price, Hollywood Bets, KPMG Taleo). Confirms HCM scope per client. |
| **HIST-017** *(new)* | APPSolve_SAA_Additional Information.docx | June 2025 | `Parties/Customers/South African Airways/HCM/1.Working/Support Clarification/` | SAA clarification response — may contain payroll integration and architecture detail. Register as supplementary to HIST-006. |

### 2.3 Supporting Reference Documents (Not Extractable — Governance Compliance Docs)

| Document | Location | Purpose |
|---|---|---|
| SAA Tender Document (RFP GSM009:25) | `Parties/Customers/South African Airways/HCM/0.Submitted/Tender Documents/` | Client RFP — confirms SAA HCM requirements scope (not extractable; client's document) |
| RFP-BRS-HCM solution V7.1 (CCBA) | `Parties/Customers/CCBA/Oracle HCM RFP/4. Supporting Documentation/` | Client BRS — confirms CCBA HCM module requirements (not extractable; client's document) |
| Reference letters in SAA submission | `Parties/Customers/South African Airways/HCM/0.Submitted/Returnable Documents and References/` | Adcock Ingram (2023), Mr Price (2024), Oracle (2024) reference letters. Potential source for `04_References/Oracle/`. |

### 2.4 Sources Considered but Not Selected as Primary

| Document | Reason not selected |
|---|---|
| Agileum HCM Consultants v1.0 (2019) | Consultant placement document — no HCM capability content |
| CellC HCM 2020 | Appears to be older RFP response — superseded by SAA, CCBA (2025) |
| Barloworld HCM Implementation | Only questionnaire in corpus — no APPSolve response document |
| Dark Fibre Africa / Maziv Group HCM | Quotes and license pricing only — no proposal content; also, DFA is excluded (governance rule) |
| APPS Associates HCM Support | Support/staffing engagement — not an implementation capability source |

---

## 3. Module Coverage by Source

The following table maps each confirmed HCM module to its source documents, rated by extraction quality (H=High/primary, M=Medium/supporting, L=Low/mention only):

| HCM Module | HIST-006 (SAA) | HIST-007 (HB) | HIST-014 (CCBA) | HIST-015 (Afro) | Confirmed Implementation |
|---|---|---|---|---|---|
| **Global HR / Core HCM** | H | H | H | H | HB (go-live Jul 2025), Mr Price (SABS ETS) |
| **Absence Management** | H | H | M | H | HB Phase 1 (confirmed) |
| **Benefits** | H | — | M | — | SAA proposal only |
| **Journeys / Employee Self-Service** | H | — | M | M | SAA proposal only |
| **Workforce Directory / Modelling** | H | — | M | — | SAA proposal only |
| **Recruiting Cloud** | H | H | H | H | HB Phase 3 (confirmed) |
| **Recruiting Booster** | — | — | H | — | CCBA proposal only |
| **Talent Management (Talent Review + Career Dev)** | H | H | H | H | HB Phase 2 (confirmed) |
| **Goal Management** | H | H | H | H | HB Phase 4 (confirmed) |
| **Performance Management** | H | H | H | H | HB Phase 4 (confirmed) |
| **Succession Planning** | H | H | M | H | HB post-Phase 4 (in progress as at July 2025) |
| **Learning Cloud (OLM)** | H | H | H | H | HB Phase 4 (Learning module), Mr Price (Learning only — see note) |
| **Workforce Compensation** | H | — | H | H | SAA + CCBA proposals |
| **Time and Labor** | H | — | — | H | SAA proposal; SABS ETS (Mr Price T&L) |
| **Workforce Scheduling** | H | — | — | — | SAA proposal only |
| **Help Desk / HR Service Center** | H | H (Annexure) | H | H | HB Annexure 2 (confirmed in scope) |
| **HCM Analytics (OTBI + TDE)** | H | — | H | — | SAA + CCBA proposals |
| **Strategic Workforce Planning (EPM)** | — | — | H | — | CCBA proposal only; recommend separate assessment |
| **HCM Communicate Cloud** | — | — | H | — | CCBA proposal only |
| **Payroll Interface (OIC / HCM Extracts)** | H | H | H | — | OIC: HB (3rd party payroll); SAP Payroll: SAA narrative |
| **Work Life** | H | — | — | — | SAA proposal only |

**Important note on Mr Price:** Per ORACLE_FACT_BASELINE Section 19, Mr Price scope is **Oracle HCM Learning Cloud only** — not full HCM. Do not describe Mr Price as a full HCM reference. Approved wording: "Oracle HCM Learning Cloud."

---

## 4. Proposed Wave 3 Capability Statements — Priority Order

The following nine capability statements are proposed in extraction priority order. Priority is based on: (1) tender frequency / breadth of demand, (2) source corpus quality, (3) confirmed implementation evidence.

### Priority 1 — W3S1-001: Oracle HCM Core — Global HR and Employee Lifecycle

**Proposed document ID:** W3S1-001-ORA-HCM-Core  
**KB destination:** `06_Capabilities/Oracle/Oracle_HCM/`  
**Primary source:** HIST-006 (SAA Section 2 and Section 3)  
**Supporting sources:** HIST-007 (HB Phase 1), HIST-014 (CCBA), HIST-015 (Afrocentric Phase 1)  
**Confirmed implementation proof:** Hollywood Bets (go-live July 2025, 7,000 users); Mr Price Group (SABS ETS)  
**Proposed scope:** Global HR foundation, employee lifecycle (hire to retire), organisational structures, position management, absence management, self-service, journeys, workforce directory and modelling, work life solutions, AI-based skills management  
**Rationale:** Foundational HCM statement required for every Oracle HCM tender. Broadest source coverage in corpus. Hollywood Bets provides the strongest implementation evidence.  
**Governance note:** Module list is broad — BU lead to confirm which modules have been implemented vs proposed only (see Section 6, Flag F-W3-001).

---

### Priority 2 — W3S1-002: Oracle Talent Management Suite

**Proposed document ID:** W3S1-002-ORA-HCM-TalentMgmt  
**KB destination:** `06_Capabilities/Oracle/Oracle_HCM/`  
**Primary source:** HIST-007 (Hollywood Bets V5.0 — ACCEPTED, Phases 2, 4, post-Phase 4)  
**Supporting sources:** HIST-006 (SAA Section 3), HIST-015 (Afrocentric Phases 7–9)  
**Confirmed implementation proof:** Hollywood Bets — Talent Management (Phase 2: Talent Review, Career Development, Talent Review); Performance and Goal Management (Phase 4)  
**Proposed scope:** Talent review, career development, succession planning, goal management, performance management, employee development plans, high-potential identification  
**Rationale:** Hollywood Bets is the only ACCEPTED proposal in the corpus — maximum extraction confidence. Talent Management is a high-value, frequently-tendered Oracle HCM module set.  
**Governance note:** Succession Planning was post-Phase 4 — verify with BU lead whether this was implemented at Hollywood Bets go-live (July 2025) or remains in progress.

---

### Priority 3 — W3S1-003: Oracle Recruiting Cloud

**Proposed document ID:** W3S1-003-ORA-HCM-Recruiting  
**KB destination:** `06_Capabilities/Oracle/Oracle_HCM/`  
**Primary source:** HIST-006 (SAA Section 2 and 3), HIST-014 (CCBA — includes Recruiting Booster)  
**Supporting sources:** HIST-007 (HB Phase 3 — Recruitment), HIST-015 (Afrocentric Phase 2)  
**Confirmed implementation proof:** Hollywood Bets Phase 3 (confirmed in scope per ORACLE_FACT_BASELINE)  
**Proposed scope:** AI-driven talent acquisition, job requisition management, branded career sites, multi-channel posting, CRM-style talent pools, interview management, AI candidate matching, onboarding integration  
**Rationale:** High-demand capability for HR tenders. Four-source coverage. CCBA source adds Recruiting Booster content not in SAA document.  
**Governance note:** Recruiting Booster is an add-on module — BU lead to confirm if this has been included in any client scope before claiming it as a standard delivery item.

---

### Priority 4 — W3S1-004: Oracle Learning Cloud

**Proposed document ID:** W3S1-004-ORA-HCM-Learning  
**KB destination:** `06_Capabilities/Oracle/Oracle_HCM/`  
**Primary source:** HIST-006 (SAA Section 2 and 3), HIST-014 (CCBA)  
**Supporting sources:** HIST-007 (HB Phase 4 — Learning), HIST-015 (Afrocentric Phase 3)  
**Confirmed implementation proof:** Hollywood Bets (Learning in Phase 4 scope); Mr Price (Oracle HCM Learning Cloud — Learning-only implementation, SABS ETS confirmed)  
**Proposed scope:** AI-driven personalised learning paths, compliance training and certification management, blended learning (ILT/self-paced/video), gamification, social learning, integration with external content providers (LinkedIn Learning, Coursera), learning analytics  
**Rationale:** High tender frequency; Mr Price provides an additional reference specifically for Learning Cloud. Two strong narrative sources (SAA and CCBA).  
**Governance note:** Mr Price scope is Learning Cloud only — separate from full HCM implementations. Do not conflate in client reference tables.

---

### Priority 5 — W3S1-005: Oracle Workforce Compensation

**Proposed document ID:** W3S1-005-ORA-HCM-Compensation  
**KB destination:** `06_Capabilities/Oracle/Oracle_HCM/`  
**Primary source:** HIST-006 (SAA Section 2 and 3 — Compensation Management section)  
**Supporting sources:** HIST-014 (CCBA), HIST-015 (Afrocentric Phase 5)  
**Confirmed implementation proof:** SAA and CCBA proposals (no confirmed go-live implementation of Compensation as standalone module — HB proposal did not include this module)  
**Proposed scope:** Merit plan management, bonus and incentive plans, salary review cycles, compensation budgeting, workforce compensation analytics, equity management, market-rate benchmarking  
**Rationale:** Strong source content in both SAA and CCBA documents. Compensation is a core HR tender requirement.  
**Governance note:** No confirmed client go-live for this module as standalone. Frame as APPSolve configuration and enablement capability — not "we have implemented X at Y." Flag assumption in draft.

---

### Priority 6 — W3S1-006: Oracle HCM Analytics and Workforce Insights

**Proposed document ID:** W3S1-006-ORA-HCM-Analytics  
**KB destination:** `06_Capabilities/Oracle/Oracle_HCM/`  
**Primary source:** HIST-006 (SAA Section 3 — HCM Analytics, OTBI, TDE sections)  
**Supporting sources:** HIST-014 (CCBA — HCM Analytics and Strategic Workforce Planning)  
**Confirmed implementation proof:** SAA and CCBA proposals (OTBI and TDE confirmed as SAA modules per ORACLE_FACT_BASELINE Section 4.1)  
**Proposed scope:** OTBI (Oracle Transactional Business Intelligence), TDE (Transactional Data Extracts), prebuilt HCM dashboards, workforce composition KPIs, diversity and inclusion analytics, attrition analysis, predictive workforce trends, self-service reporting, mobile-optimised dashboards  
**Rationale:** Analytics is a tender differentiator. OTBI and TDE are technically distinct and worth explaining separately from EPM/Strategic Workforce Planning.  
**Governance note:** Strategic Workforce Planning (Oracle EPM module referenced in CCBA) is a separate licensed product — do not conflate with HCM Analytics. Treat EPM as a future Wave 3 scope item, not part of this statement.

---

### Priority 7 — W3S1-007: Oracle Workforce Management (Time, Absence and Scheduling)

**Proposed document ID:** W3S1-007-ORA-HCM-WorkforceMgmt  
**KB destination:** `06_Capabilities/Oracle/Oracle_HCM/`  
**Primary source:** HIST-006 (SAA — Time and Labor, Workforce Scheduling, Absence sections)  
**Supporting sources:** HIST-015 (Afrocentric Phase 4 — Time and Labor)  
**Confirmed implementation proof:** SAA proposal; SABS ETS (Mr Price — Time and Labour confirmed as their product area)  
**Proposed scope:** Time and labor capture (multiple input methods), shift scheduling, demand-based workforce scheduling, labor compliance and union rule enforcement, absence management (integrates with Time and Labor), real-time labor cost analytics, integration with Oracle Payroll and Project Costing  
**Rationale:** Workforce management is frequently scoped in large enterprise HCM tenders. SAA provides the best source content.  
**Governance note:** Mr Price is confirmed as an Oracle Fusion HCM + Time and Labour client (SABS ETS + RedPath Mining RFI). Approved for reference subject to BU lead pre-tender check on contact availability.

---

### Priority 8 — W3S1-008: Oracle Help Desk and HR Service Centre

**Proposed document ID:** W3S1-008-ORA-HCM-HelpDesk  
**KB destination:** `06_Capabilities/Oracle/Oracle_HCM/`  
**Primary source:** HIST-007 (Hollywood Bets Annexure 2 — HR Help Desk), HIST-006 (SAA Section 2 and 3 — Help Desk)  
**Supporting sources:** HIST-014 (CCBA), HIST-015 (Afrocentric Phase 6)  
**Confirmed implementation proof:** Hollywood Bets (Help Desk in confirmed scope per ORACLE_FACT_BASELINE Section 19)  
**Proposed scope:** HR case management, self-service employee portal, AI-driven case routing, virtual assistant for HR queries, multi-channel support (email, chatbot, web), SLA management, role-based access, knowledge base for HR policies, integration with Oracle Fusion HCM  
**Rationale:** Help Desk is increasingly required in enterprise HCM tenders as a service layer over Oracle. Hollywood Bets provides the only ACCEPTED-proposal proof for this module.  
**Governance note:** The HB Annexure 2 specifically covers HR Help Desk — extract from this section, not from the main proposal body which covers implementation approach only.

---

### Priority 9 — W3S1-009: Oracle HCM Payroll Interface and Integration

**Proposed document ID:** W3S1-009-ORA-HCM-PayrollInterface  
**KB destination:** `06_Capabilities/Oracle/Oracle_HCM/`  
**Primary source:** HIST-006 (SAA — payroll section including SAP Payroll narrative)  
**Supporting sources:** HIST-007 (HB — 3rd party payroll via OIC), ORACLE_FACT_BASELINE Sections 7 and 12  
**Confirmed implementation proof:** "APPSolve has implemented an Integration between Oracle HCM and SAP Payroll many times" (ORACLE_FACT_BASELINE Section 14 — approved phrase); Hollywood Bets (3rd party payroll via OIC — confirmed in scope)  
**Proposed scope:** Oracle HCM Payroll Interface (PI) configuration, OIC-based integration to third-party payroll systems (SAP Payroll, PaySpace, others), HCM Extracts as alternative payroll export method, standard integration patterns, payroll data validation and reconciliation  
**Rationale:** Payroll integration is a near-universal requirement in HCM tenders and a proven APPSolve strength. The confirmed SAP Payroll integration claim is a key differentiator.  
**Governance note:** Do not imply Oracle Payroll Cloud native as the default — APPSolve's standard model is integration to a third-party payroll system. DFA exception (Oracle Payroll Cloud native) must not appear in general capability statements. See ORACLE_FACT_BASELINE Section 12.

---

## 5. HIST Registration Plan

The following HIST entries must be registered in DOCUMENT_REGISTER.csv before extraction begins. HIST-006 and HIST-007 were planned in ORACLE_FACT_BASELINE Section 18. HIST-014 through HIST-017 are new.

| HIST ID | Title | Date | Path |
|---|---|---|---|
| HIST-006 | SAA HCM RFP Response (APPSolve_SAA_RFP.docx) | June 2025 | `Parties/Customers/South African Airways/HCM/1.Working/APPSolve_SAA_RFP.docx` |
| HIST-007 | Hollywood Bets Oracle HCM Accepted Proposal V5.0 | April 2023 | `Parties/Customers/Hollywood Bets/RFP/HCM and Payroll Implementation/Accepted proposal/APPSolve_HollywoodBets_Oracle Implementation 3rd part_V5.0.docx` |
| HIST-014 | CCBA Oracle HCM Solution V2.0 | May 2025 | `Parties/Customers/CCBA/Oracle HCM RFP/0. Submitted/APPSolve_CCBA_HCM_Solution_V2.0.docx` |
| HIST-015 | Afrocentric Health HCM Proposal V4.0 | 2023 | `Parties/Customers/Afrocentric Health/RFP/HCM 2023/APPSolve Afrocentric - HCM Proposal V4.0.docx` |
| HIST-016 | SABS ETS Oracle Fusion RFP Response | Dec 2025 | `Parties/Customers/SABS/RFP/ETS - Oracle Fusion/APPSolve_SABS_RFP_Response.docx` |
| HIST-017 | SAA HCM Additional Information (Clarification) | June 2025 | `Parties/Customers/South African Airways/HCM/1.Working/Support Clarification/APPSolve_SAA_Additional Information.docx` |

---

## 6. Governance Flags — BU Lead Decisions Required Before Extraction

### Flag F-W3-001: Module Scope Boundary — Implemented vs Proposed

**Issue:** Several HCM modules in the SAA and CCBA source documents describe Oracle product capabilities rather than APPSolve implementation experience. The SAA and CCBA proposals are **submitted** tenders — their outcomes (won/lost/pending) are not recorded in the corpus.

**Required decision:** Confirm whether APPSolve has **implemented** each module below as a live client delivery, or only proposed it. This determines whether the capability statement says "APPSolve has implemented" vs "APPSolve has successfully proposed and scoped."

Modules requiring BU lead confirmation:
- Benefits Management
- Journeys / Employee Self-Service
- Workforce Scheduling
- Workforce Directory / Modelling
- Work Life
- Workforce Compensation (as standalone, not bundled with Core HCM)
- HCM Communicate Cloud

**Confirmed implementations (no BU decision needed):**
- Global HR / Core HCM — Hollywood Bets (go-live July 2025)
- Talent Management (Talent Review, Career Dev) — Hollywood Bets Phase 2
- Goal and Performance Management — Hollywood Bets Phase 4
- Recruiting — Hollywood Bets Phase 3
- Learning — Hollywood Bets Phase 4; Mr Price (Learning Cloud only)
- Absence Management — Hollywood Bets Phase 1
- Help Desk — Hollywood Bets (in confirmed scope)
- SAP Payroll Integration via OIC — confirmed by ORACLE_FACT_BASELINE approved phrase

---

### Flag F-W3-002: Hollywood Bets Go-Live Reference Availability

**Issue:** ORACLE_FACT_BASELINE Section 19 confirms Hollywood Bets go-live July 2025, 7,000 users, 7 modules. This is the strongest HCM reference in the corpus. However, reference availability has not been confirmed.

**Required decision:** Confirm whether the Hollywood Bets account manager has confirmed HB as a referenceable client for Oracle HCM capability statements. If yes, this unlocks the highest-confidence source for Priority 1–4 statements. If no, the statements must rely on SAA/CCBA proposals without a confirmed go-live reference.

---

### Flag F-W3-003: SAA HCM Tender Outcome

**Issue:** The SAA HCM RFP (GSM009:25, June 2025) is the richest source document. Its outcome (won/lost/pending) is not recorded in the corpus. APPSolve submitted to SAA — SAA is NOT an approved reference client.

**Required decision:**
1. What is the outcome of the SAA HCM submission? (Won / Lost / Pending / No award)
2. May SAA be described as a current or prospective client in any KB content? (Governance default: No — unless BU lead approves.)
3. The SAA source may be used as a corpus reference to extract **APPSolve methodology and approach** content — but SAA may not be named as a client in approved KB capability statements without BU lead approval.

---

### Flag F-W3-004: CCBA Proposal Status and Client Naming

**Issue:** The CCBA Oracle HCM RFP V2.0 (May 2025) is a full proposal submission. CCBA outcome is not recorded in the corpus.

**Required decision:** May CCBA be used as a named project reference in any Wave 3 KB content? If not, the document is still extractable as an APPSolve methodology and approach source — CCBA is simply not cited by name in the approved output.

---

### Flag F-W3-005: Reference Letters in SAA Submission Folder

**Issue:** The SAA HCM submission folder (`0.Submitted/Returnable Documents and References/`) contains the following reference letters:
- `Reference 2023 Adcock Ingram Letter.pdf`
- `Reference 2024 Mr Price.pdf`
- `Reference 2024 Oracle Letter.pdf`

These letters may be usable for `04_References/Oracle/` registration.

**Required decision:** Confirm if these letters are approved for registration in the KB Reference library. Note: the Adcock Ingram reference and Oracle reference letter are high priority per CURRENT_STATE.md standing actions.

---

## 7. Risk Register — Wave 3 HCM

| Risk ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-W3-001 | Hollywood Bets reference not available — HB account manager has not confirmed reference access | Medium | High | Frame HCM Core, Talent, Recruiting capability without naming specific clients; rely on generic "enterprise clients" framing until BU lead confirms |
| R-W3-002 | SAA HCM modules are proposed only — SAA tender was not won, reducing the evidentiary weight of SAA-specific configuration claims | Medium | Medium | Frame SAA-sourced module content as "APPSolve has scoped and proposed" or "APPSolve's standard approach includes" — not "APPSolve has implemented" |
| R-W3-003 | CCBA source contains Oracle product marketing language — risk of extracting Oracle claims as APPSolve delivery claims | Medium | High | Systematic framing discipline required: never "Oracle delivers X"; always "APPSolve configures and implements X within Oracle Fusion HCM" |
| R-W3-004 | Mr Price scope overstated — corpus materials reference Mr Price as an HCM client; actual scope is Learning Cloud only | Medium | Medium | Use only the corrected scope per ORACLE_FACT_BASELINE Section 19: "Oracle HCM Learning Cloud" — do not imply full HCM |
| R-W3-005 | Module count claims — SAA and CCBA documents list many modules; unsupported total-module counts must not appear in KB content | Low | High | Do not state "APPSolve implements all 24 HCM modules" — list only modules with confirmed source backing |
| R-W3-006 | BEE Level 3 certificate expiry (2026-07-31) — any Wave 3 tender submitted after July 2026 must use the renewed certificate | High (date-driven) | High | Pre-tender check on each draft: confirm BEE certificate is current before submission |

---

## 8. Pre-Extraction Checklist

Before the first Wave 3 extraction draft is created:

| Check | Status |
|---|---|
| HIST-006 through HIST-017 registered in DOCUMENT_REGISTER.csv | ❌ Pending |
| BU lead decision on F-W3-001 (module scope boundary) | ✅ CLOSED — APPSolve has implemented all Oracle HCM modules |
| BU lead decision on F-W3-002 (Hollywood Bets reference availability) | ✅ CLOSED — Hollywood Bets confirmed and referenceable |
| BU lead decision on F-W3-003 (SAA outcome and naming) | ✅ CLOSED — SAA not awarded; use as capability evidence only; do not name as reference |
| BU lead decision on F-W3-004 (CCBA naming) | ✅ CLOSED — CCBA source-only; must never be named in approved KB content |
| BU lead decision on F-W3-005 (reference letters) | ✅ CLOSED — All letters in Tender Pack and Reference folders may be registered |
| ORACLE_FACT_BASELINE reviewed — all Wave 3 facts must be checked against it before extraction | ✅ Ready |
| KB destination folder confirmed: `06_Capabilities/Oracle/Oracle_HCM/` | ✅ Exists and empty |
| Approved Content folder confirmed: `07_Approved_Content/Approved/Oracle/` | ✅ Exists |
| Candidate Content folder for drafts: `07_Approved_Content/Candidate_Content/Oracle/` | ✅ Exists |

---

## 9. Recommended Extraction Sequence

Once BU lead decisions are received:

1. **W3S1-001** (HCM Core) — extract from HIST-007 (HB) + HIST-006 (SAA) as primary narrative
2. **W3S1-003** (Recruiting) — extract from HIST-006 + HIST-014 (CCBA)
3. **W3S1-004** (Learning) — extract from HIST-006 + HIST-007 + HIST-014
4. **W3S1-002** (Talent Management) — extract from HIST-007 (Phase 2 + Phase 4) + HIST-006
5. **W3S1-008** (Help Desk) — extract from HIST-007 (Annexure 2) + HIST-006
6. **W3S1-009** (Payroll Interface) — extract from HIST-006 (SAA payroll section) + ORACLE_FACT_BASELINE Section 12
7. **W3S1-005** (Compensation) — extract from HIST-006 + HIST-014 + HIST-015
8. **W3S1-006** (Analytics) — extract from HIST-006 + HIST-014
9. **W3S1-007** (Workforce Management) — extract from HIST-006 + HIST-015

---

## 10. Governance Notes — Permanent Rules for Wave 3 Extraction

The following rules apply to all Wave 3 Oracle HCM content and override any source document wording:

1. **Never reference DFA** in any Wave 3 content (governance rule — permanent).
2. **Oracle Level 1 Partner** — use this exact phrase; never "Gold Partner" or "Gold Level."
3. **"50+ Senior Consultants"** — use this; never "110 senior consultants" or "100+ consultants."
4. **"Over 23 years of experience"** — use this; never "22 years."
5. **BEE Level 3** — current cert (RS-19451, expires 2026-07-31). Never cite Level 2 (expired).
6. **APPSolve delivery framing** — every capability claim must be framed as APPSolve implementing, configuring, or enabling — not Oracle providing. Never "Oracle Fusion HCM does X" — always "APPSolve implements X using Oracle Fusion HCM."
7. **Client references** — only clients confirmed in ORACLE_FACT_BASELINE Section 11 may be cited. No unsupported client references. No client naming without BU lead approval.
8. **OIC as standard** — per ORACLE_FACT_BASELINE Section 7, OIC is mandatory in every Fusion HCM implementation. Note OIC as the standard integration layer in all HCM content.
9. **Mr Price = Learning Cloud only** — do not describe Mr Price as a full HCM client.
10. **No unsupported module counts** — do not state total module counts without listing the specific modules.

---

*Wave 3 Source Discovery Report prepared 2026-06-12 by Claude (AI) — source inventory only; no capability content extracted.*  
*BU lead decisions required before extraction begins. All extraction subject to ORACLE_FACT_BASELINE authority.*
