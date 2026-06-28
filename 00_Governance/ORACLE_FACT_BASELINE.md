---
created: "2026-06-10"
created_by: "Claude (AI — Wave 2 pre-extraction fact baseline)"
status: "Active — validated before extraction begins; do not override without confirmed source"
purpose: "Authoritative fact reference for all Oracle Wave 2 extraction tasks. Extractor must check this file before writing any Oracle capability claim."
---

# Oracle Fact Baseline
**Date:** 2026-06-10 | **Owner:** Hein Blignaut | **Scope:** All Oracle capability extraction in Wave 2

This file establishes the validated Oracle fact set before any extraction begins. No capability content may be extracted into a KB draft file if it contradicts a fact recorded here. Discrepancies between a source document and this baseline must be flagged to the BU lead — not resolved by the AI.

**How to use this file during extraction:**
1. Read this baseline before writing any Oracle claim.
2. For each claim you are about to write, locate the matching row in the relevant section below.
3. If the claim does not appear here, flag it as `[UNVERIFIED — requires BU lead confirmation]` in the draft.
4. Never extract from the Prohibited Wording section, regardless of what the source document says.

---

## 1. Oracle Partner Model and Partner Status

| Fact | Approved value | Source / Confirming authority |
|---|---|---|
| Oracle partner tier | **Oracle Level 1 Partner** | F3 — Hein Blignaut confirmation; EXPIRED_APPSolve_OPN_202108.pdf |
| Gold Partner status | **EXPIRED August 2021** — do not cite, do not imply | F3 — certification archive |
| Approved partner tier phrase | "Oracle Level 1 Partner" | W1S1-003 (approved) |
| Value-Added Reseller | Oracle Value-Added Reseller — authorised to sell and distribute Oracle licenses | W1S1-003 (approved) |
| Cloud Excellence Implementer | Approved — see annual revalidation note | W1S1-003 (approved); revalidate annually via OPN portal |
| Oracle Enterprise Linux Specialist | Approved — see annual revalidation note | W1S1-003 (approved); revalidate annually via OPN portal |
| Years as Oracle partner | "over two decades" (approved phrase) | W1S1-003 (approved) |

**Critical rule:** Never use "Gold Partner", "Gold Level", "Gold or higher", or any variation implying Gold tier. Gold Membership expired August 2021. The approved phrase is "Oracle Level 1 Partner."

---

## 2. Published Oracle Expertise Areas

Five areas confirmed through Hein Blignaut (F3) and published on OPN at time of W1S1-003 approval (2026-06-09):

| Expertise area | Approved description |
|---|---|
| Oracle Fusion Cloud Financials | Implementation expertise certified |
| Oracle Fusion Cloud HCM Core | Implementation expertise certified |
| Oracle Integration | Implementation expertise certified |
| Oracle E-Business Suite Migration to OCI | Migration expertise certified |
| Oracle Cloud Infrastructure Migration | Migration expertise certified |

---

## 3. Oracle Awards

Six awards confirmed. Source: W1S1-003 (approved by Hein Blignaut 2026-06-09).

| Award | Year | Region |
|---|---|---|
| Oracle Innovation Sustainability Award | 2015 | Global — for applications developed in Mozambique |
| Oracle Innovation Sustainability Award | 2016 | Global — repeat winner |
| Oracle SaaS Partner of the Year | 2016 | SADC Region |
| Oracle SaaS Partner of the Year — New Entrant | 2019 | SADC Region |
| Oracle Business Impact Award | 2024 | EMEA Region |
| Oracle Business Impact Award | 2024 | ECEMEA Region |

---

## 4. Oracle Fusion Capabilities — Confirmed Modules

Modules confirmed through one or more of: SABS Fusion ETS Response (Dec 2025), SAA HCM RFP Response Section 2 (June 2025), RedPath Mining RFI Reply (March 2026), Hollywood Bets Accepted Proposal V5.0 (April 2023).

### 4.1 Fusion HCM Modules

| Module | Confirmed in | Notes |
|---|---|---|
| Global HR | SAA Section 2; SABS ETS | Core HCM module |
| AI-Based Skills | SAA Section 2 | |
| Absence Management | SAA Section 2; Hollywood Bets Phase 1 | |
| Benefits | SAA Section 2 | |
| Journeys | SAA Section 2 | |
| Payroll Interface (3rd party integration) | SAA Section 2; Hollywood Bets; SABS ETS | Not Oracle Payroll Cloud native — integrates to PaySpace or SAP Payroll; exception: DFA uses Oracle Payroll Cloud native |
| Workforce Directory | SAA Section 2 | |
| Workforce Modelling | SAA Section 2 | |
| Work Life | SAA Section 2 | |
| OTBI (Oracle Transactional Business Intelligence) | SAA Section 2 | |
| TDE (Transactional Data Extracts) | SAA Section 2 | |
| Workforce Compensation | SAA Section 2 | |
| Recruiting | SAA Section 2; Hollywood Bets Phase 3 | |
| Talent Management | SAA Section 2; Hollywood Bets Phase 2 | |
| Goal Management | Hollywood Bets Phase 4 | |
| Performance Management | Hollywood Bets Phase 4 | |
| Talent Review | Hollywood Bets Phase 2 | |
| Career Development | Hollywood Bets Phase 2 | |
| Succession Planning | Hollywood Bets post-Phase 4 | |
| Help Desk | SAA Section 2 | |
| Learning Cloud | SAA Section 2 | |
| HCM Analytics | SAA Section 2 | |
| Time and Labor | SAA Section 2; SABS ETS (Mr Price) | |
| Workforce Scheduling | SAA Section 2 | |

### 4.2 Fusion Finance and Procurement Modules

| Module | Confirmed in | Notes |
|---|---|---|
| Oracle Fusion Finance | SABS ETS (Cape Union Mart, Investec); RedPath Mining RFI | |
| Oracle Fusion Procurement | SABS ETS (Cape Union Mart, Investec) | |

### 4.3 Project Portfolio Management (PPM)

| Module | Confirmed in | Notes |
|---|---|---|
| Oracle PPM | SABS ETS (DFA, KPMG) | |

---

## 5. Oracle EBS Capabilities — Confirmed

| EBS area | Confirmed clients | Source |
|---|---|---|
| Oracle EBS (general R12) | KPMG (SADC 6 countries), Assore, Adcock Ingram | SABS ETS |
| Oracle EBS R12.2 (specific version) | ARM (African Rainbow Minerals) | ORACLE_REFERENCE_GAP_REPORT.md — ARM reference letter |
| Oracle EBS Taleo | KPMG | SABS ETS |
| Oracle EBS multi-country deployment | KPMG (6 SADC countries) | SABS ETS |
| Oracle EBS Payroll | Confirmed as an option for SA payroll alongside PaySpace | SAA RFP Section payroll narrative |

---

## 6. Oracle Cloud Infrastructure (OCI)

| Fact | Approved value | Source |
|---|---|---|
| OCI security certifications | SOC 1 Type 2 + SOC 2 Type 2 Bridge Letters (June 2025) | SAA RFP supporting documents — OCI Bridge Letters submitted June 2025 |
| OCI compliance evidence | Bridge Letters available — must be attached to tenders requiring cloud security evidence | SAA RFP |
| Approved expertise phrase | "Oracle Cloud Infrastructure Migration" | W1S1-003 (published expertise area) |
| EBS Migration to OCI | Confirmed expertise | W1S1-003 (published expertise area) |

---

## 7. Oracle Integration Cloud (OIC) — Standard Integration Layer

| Fact | Approved value | Source |
|---|---|---|
| OIC usage | **Mandatory component in every Oracle Fusion implementation** | RedPath Mining RFI (confirmed OIC used in ALL Fusion implementations listed) |
| SAP Payroll integration via OIC | Confirmed — "APPSolve has implemented an Integration between Oracle HCM and SAP Payroll many times" | SAA RFP Section (payroll narrative) |
| Alternative integration method | HCM Extracts (for payroll exports where OIC is not in scope) | SAA RFP |
| OIC expertise area | "Oracle Integration" — published OPN expertise area | W1S1-003 |

**Rule for extraction:** Do not describe any Oracle Fusion implementation as complete without OIC. If a source document does not mention OIC, this does not mean OIC was absent — it is the standard. Note OIC as standard architecture in all Fusion capability content.

---

## 8. EBS-to-OCI Migration Capability

| Fact | Approved value | Source |
|---|---|---|
| EBS-to-OCI migration expertise | Confirmed — published OPN expertise area | W1S1-003 |
| Approved phrase | "Oracle E-Business Suite Migration to OCI" | W1S1-003 |
| Cloud migration expertise | "Oracle Cloud Infrastructure Migration" | W1S1-003 |

---

## 9. DBA Managed Services Capability

| Fact | Approved value | Source |
|---|---|---|
| DBA team claim | **"one of the largest locally-based Oracle Applications DBA teams in South Africa"** | F15 — Hein Blignaut confirmation; W1S1-007 (approved) |
| After-hours support | Confirmed | W1S1-009 (approved) |
| 24x7 monitoring | Confirmed | W1S1-009 (approved) |
| Hybrid support model | Confirmed — on-site / remote / hybrid | W1S1-009 (approved) |

---

## 10. Oracle Support Services

| Fact | Approved value | Source |
|---|---|---|
| Support model | Hybrid — on-site, remote, and combined delivery | W1S1-007 and W1S1-009 (approved) |
| Monitoring | 24x7 | W1S1-009 (approved) |
| After-hours support | Confirmed | W1S1-009 (approved) |
| SLA tiers | P1/P2/P3/P4 (framework available in HIST-002 and ATNS 2025 — not yet in approved KB content) | HIST-002; ATNS 2025 proposal — extract in Deliverable 4 |
| CIM 4-stage model | Continuous Improvement Model reference | W1S1-009 (approved) |

---

## 11. Oracle Reference Clients — Confirmed

Clients confirmed through two or more sources (SABS ETS, SAA RFP, RedPath Mining RFI) as live or completed Oracle implementations by APPSolve. Reference letters exist in the corpus for most (see ORACLE_REFERENCE_GAP_REPORT.md).

### Fusion Clients

| Client | Product | Scope | Confirmed in |
|---|---|---|---|
| Dark Fibre Africa (DFA) | Oracle Fusion (full suite incl. Oracle Payroll Cloud) | Full Oracle suite | SABS ETS; RedPath Mining RFI |
| Cape Union Mart | Oracle Fusion Finance + Procurement | ERP | SABS ETS; RedPath Mining RFI |
| Investec | Oracle Fusion Finance + Procurement | 3 countries: SA, US, UK | SABS ETS; RedPath Mining RFI |
| Mr Price Group | Oracle Fusion HCM + Time and Labour | HCM | SABS ETS (Mr Price); RedPath Mining RFI |
| Hollywood Bets | Oracle Fusion HCM (7 modules) + OIC + 3rd party payroll | HCM | Hollywood Bets proposal V5.0 (WON); RedPath Mining RFI |
| NALA Renewables | Oracle Fusion Finance (multi-country: Lithuania, Finland, Romania) | Finance — 8 countries | SABS ETS; RedPath Mining RFI |
| KPMG | Oracle Taleo | Talent | SABS ETS |

### EBS Clients

| Client | Product | Scope | Confirmed in |
|---|---|---|---|
| KPMG | Oracle EBS | SADC 6 countries | SABS ETS |
| Assore | Oracle EBS | ERP | SABS ETS; reference letter in corpus |
| Adcock Ingram | Oracle EBS | ERP | SABS ETS; reference letter in corpus |
| ARM (African Rainbow Minerals) | Oracle EBS R12.2 | ERP | Reference letter in corpus |

### PPM Clients

| Client | Product | Scope | Confirmed in |
|---|---|---|---|
| DFA | Oracle PPM | PPM | SABS ETS |
| KPMG | Oracle PPM | PPM | SABS ETS |

**Note on reference letters:** Reference letters are in corpus submission folders, not yet in `04_References/Oracle/`. See ORACLE_REFERENCE_GAP_REPORT.md for registration priority. Do not cite any client as a reference in a tender without first confirming the signed letter is available and the client contact is still active.

---

## 12. Payroll Integration Confirmed Facts

| Fact | Approved value | Source |
|---|---|---|
| SAP Payroll integration | "APPSolve has implemented an Integration between Oracle HCM and SAP Payroll many times" | SAA RFP payroll section |
| Standard integration method | HCM Extracts or OIC for payroll system integration | SAA RFP |
| PaySpace | Confirmed as an Oracle payroll integration partner | SAA RFP |
| Oracle EBS Payroll | Confirmed as an on-premise payroll option alongside PaySpace | SAA RFP |
| DFA exception | DFA uses Oracle Payroll Cloud native (not 3rd party) | SABS ETS |
| BeBanking/Acumatica payroll rule | Acumatica does not provide payroll in SA. BeBanking Payroll H2H is Oracle EBS and Oracle Fusion sources only | BU lead clarification 2026-06-10 (BQ5) |

---

## 13. Company Stats — Oracle-Related Claims

| Fact | Approved value | Notes |
|---|---|---|
| Founded | 2002 — "over 23 years" | CIPC 2002/008072/07 |
| Headcount | 50+ Senior Consultants | F2 — Hein Blignaut confirmation |
| BEE level | **Level 3** (RS-19451, issued August 2025, **expires 2026-07-31**) | SAA RFP BEE section; current cert |
| Prior BEE level | Level 2 (RS-17968, July 2024) — expired; do not cite | SAA RFP BEE section |
| DBA team | "one of the largest locally-based Oracle Applications DBA teams in South Africa" | F15 |
| Hein career start | 1996 at MTN — ~30 years as of 2026 | CV / corpus (F8) |

---

## 14. Approved Wording — Oracle-Specific Phrases

These phrases are approved for direct reuse (source: W1S1-003 approved 2026-06-09, W1S1-007 approved 2026-06-09, W1S1-009 approved 2026-06-09):

| Approved phrase | Approved in | Context |
|---|---|---|
| "Oracle Level 1 Partner" | W1S1-003 | Partnership tier; use wherever partner status is cited |
| "Oracle partner for over two decades" | W1S1-003 | Company tenure as Oracle partner |
| "one of the largest locally-based Oracle Applications DBA teams in South Africa" | W1S1-007 | DBA capability claim |
| "50+ Senior Consultants" | W1S1-001 | Company headcount |
| "over 23 years" | W1S1-002 | Company age (founded 2002) |
| "Oracle Value-Added Reseller — authorised to sell and distribute Oracle licenses" | W1S1-003 | Reseller status |
| "OIC used in all Oracle Fusion implementations" | RedPath Mining RFI (source document) | Standard integration claim — extract to KB in Deliverable 1 |
| "APPSolve has implemented an Integration between Oracle HCM and SAP Payroll many times" | SAA RFP (source document) | SAP payroll integration — extract to KB in Deliverable 1 |

---

## 15. Prohibited and Outdated Wording

**MANDATORY:** Do not extract, paraphrase, or include any of the following in KB content, regardless of what the source document says.

| Prohibited phrase or claim | Why prohibited | Correct value to use |
|---|---|---|
| "Oracle Gold Partner" | Gold Membership expired August 2021 | "Oracle Level 1 Partner" |
| "Gold Level" | Same — Gold expired | "Level 1 Partner" |
| "Gold or higher" | Same — Gold expired | Omit tier comparatives; cite Level 1 only |
| "110 Senior Consultants" | Outdated stat from old templates (RedPath Mining RFI, September 2024 template) | "50+ Senior Consultants" |
| "over 100 consultants" / "100+ consultants" | Same outdated stat | "50+ Senior Consultants" |
| "over 22 years" | Outdated; company founded 2002 → 24 years as of 2026 | "over 23 years" |
| "19 years' experience" for Hein Blignaut | Outdated; Hein started at MTN in 1996 = ~30 years as of 2026 | "~30 years" |
| "BEE Level 2" | Prior cert (RS-17968, July 2024) — expired | "BEE Level 3" (RS-19451, expires 2026-07-31) |
| Any stat from the RedPath Mining RFI company profile section | Contains multiple outdated stats (110 consultants, 22 years) — do not extract company profile from this source | Use approved W1S1 files for all company stats |

---

## 16. BEE Certificate — Critical Compliance Note

**Current certificate:** Level 3 (RS-19451, issued August 2025, **expires 2026-07-31**)

**Prior certificate:** Level 2 (RS-17968, July 2024) — expired

**Approved wording:** "APPSolve is currently BEE Level 3. Renewal of the next certificate is underway. Current certificate expires 2026-07-31."

**Prohibited wording:** "BEE Level 2", "Level 2 BEE", "B-BBEE Level 2", or any wording implying Level 2 is the current status.

**Governance note:** Older proposal sources (including ARM IT045 July 2025 and ATNS Feb 2025) contain BEE Level 2 references — these are stale and must not be extracted. BEE status belongs in compliance documents, not capability statements. Prefer to omit BEE from capability statements unless the tender specifically requires it.

**Action status (updated 2026-06-12):**
- `00_Governance/AI_CONTEXT.md` — **UPDATED 2026-06-12** (Level 3 added to facts table)
- `00_Governance/CHECKPOINT_WAVE1_2026-06-10.md` — pending (low priority; not in active use)
- Wave 1 approved files — searched 2026-06-12; no Level 2 references found in any approved KB file
- W2S1-002 candidate — no BEE content (correct; BEE not appropriate in capability statements)

**Renewal status:** Renewal process has started — confirmed by Hein Blignaut 2026-06-12. Hard deadline: 2026-07-31.

---

## 17. Implementation Methodology — Confirmed Framework

| Phase | Name | Key activities | Source |
|---|---|---|---|
| 0 | Mobilize | Charter, work plan, kick-off | Hollywood Bets V5.0; RedPath Mining RFI |
| 1 | Scoping | Confirm scope, align to Oracle Modern Best Practices, data assessment | RedPath Mining RFI |
| 2 | Prototype | Design workshops, CRP1/CRP2, change control | RedPath Mining RFI |
| 3 | Build | Configuration, integration build (OIC standard), data migration (Oracle FBDI sheets) | Hollywood Bets V5.0; RedPath Mining RFI |
| 4 | Deploy | Production build, data verification, testing, training, UAT | Hollywood Bets V5.0; RedPath Mining RFI |
| Post-go-live | Hyper-care | Full team ~3 months; critical care ~6 months; then steady state | Hollywood Bets V5.0 |

**Methodology basis:** Oracle UIM / OUM (Oracle Unified Methodology) — referenced in RedPath Mining RFI as "OUM-based".

---

## 18. Document Register Status — Oracle Sources

These source documents are confirmed but not yet registered in DOCUMENT_REGISTER.csv. Register before extraction begins.

| Planned HIST ID | Document | Date | Location |
|---|---|---|---|
| HIST-006 | SAA HCM RFP Response (APPSolve_SAA_RFP.docx) | June 2025 | `Parties/Customers/South African Airways/HCM/1.Working/APPSolve_SAA_RFP.docx` |
| HIST-007 | Hollywood Bets Accepted Proposal V5.0 | April 2023 | `Parties/Customers/Hollywood Bets/RFP/HCM and Payroll Implementation/Accepted proposal/APPSolve_HollywoodBets_Oracle Implementation 3rd part_V5.0.docx` |
| HIST-008 | RedPath Mining RFI Reply Detail | March 2026 | `Parties/Customers/RedPath Mining/Working/RedPath Mining_APPSolve_RFI Reply Detail.docx` |
| HIST-014 | CCBA Oracle HCM Solution V2.0 | May 2025 | `Parties/Customers/CCBA/Oracle HCM RFP/0. Submitted/APPSolve_CCBA_HCM_Solution_V2.0.docx` |
| HIST-015 | Afrocentric Health HCM Proposal V4.0 | 2023 | `Parties/Customers/Afrocentric Health/RFP/HCM 2023/APPSolve Afrocentric - HCM Proposal V4.0.docx` |
| HIST-016 | SABS ETS Oracle Fusion RFP Response | Dec 2025 | `Parties/Customers/SABS/RFP/ETS - Oracle Fusion/APPSolve_SABS_RFP_Response.docx` |
| HIST-017 | SAA HCM Additional Information (Clarification) | June 2025 | `Parties/Customers/South African Airways/HCM/1.Working/Support Clarification/APPSolve_SAA_Additional Information.docx` |
| HIST-009 | ATNS EBS Support 2025 Proposal V2 | May 2025 | `Parties/Customers/ATNS/RFP/EBS Support 2025/` |
| HIST-010 | Mpact Oracle ERP Implementation Proposal | August 2025 | `Parties/Customers/Mpact/RFP/ERP/2 Working/` |
| HIST-011 | BankServAfrica ERP Implementation Proposal V1 | August 2024 | `Parties/Customers/Bankserv/RFP/ERP/1 Working/` |
| HIST-012 | APPSolve MTN DBA RFP Response (RFX-1000004246) | 05 April 2026 | `Parties/Customers/MTN/RFP/2026 DBA MTN SA/Working/APPSolve_MTN_DBA_RFP_RFX-1000004246_v1.0.docx` |
| HIST-013 | APPSolve MTN 2014 DBA Executive Summary (HIST-002) | July 2014 | `Parties/Customers/MTN/RFP/Archive/ZZ Archive/RFP 20140718 close 20140801/Old Tender/MTN Tender/APPSolve Executive Summary.docx` |

---

## 19. Client Reference Corrections (2026-06-11)

These corrections were established from Mpact ERP Proposal reference cards (August 2025) — the most specific and recent client reference data found. These supersede the RedPath Mining RFI client list for the clients below.

| Client | Correction | Prior Assumption | Confirmed Data | Source |
|---|---|---|---|---|
| Cape Union Mart | **Modules corrected** | "Finance + SCM" (WRONG) | Oracle Fusion Financials + Oracle Fusion Procurement | Mpact references lines 557–583 |
| Nala Renewables | **Country count corrected** | "8 countries" (WRONG) | 4 countries: South Africa, Lithuania, Romania, Finland | Mpact references lines 472–498 |
| Mr Price Group | **Scope and role clarified — C-W3-002 CLOSED 2026-06-12; Oracle Opportunity Marketplace added OI-W2-002 CLOSED 2026-06-12** | "HCM" (implied full) | Oracle HCM Learning Cloud (implemented by APPSolve); Oracle Opportunity Marketplace (implemented by APPSolve — OI-W2-002 CLOSED 2026-06-12); broader Oracle HCM estate (ongoing support provided by APPSolve — not implemented by APPSolve). Cite Learning Cloud and Opportunity Marketplace as implementation references. Cite broader HCM as support reference only. Approved wording for Opportunity Marketplace: "APPSolve has experience implementing Oracle Opportunity Marketplace capabilities as part of broader Oracle Talent Management programmes." | Mpact references lines 528–554; C-W3-002 BU Lead decision; OI-W2-002 BU Lead decision |
| Dark Fibre Africa (DFA) | **HCM scope updated; Workforce Compensation added — OI-W5-003 CLOSED 2026-06-13; NOT referenceable — Rule 21.4** | Oracle HCM Core, Talent Management, Learning Cloud, Taleo Recruiting (prior) | Oracle HCM Core, Oracle Talent Management, Oracle Learning Cloud, Oracle Taleo Recruiting, **Oracle Workforce Compensation** — all implemented by APPSolve. NOT approved as a referenceable client. DFA confirms APPSolve implementation experience across Oracle HCM Core, Talent Management, Learning Cloud, Taleo Recruiting and Workforce Compensation. DFA is not currently approved as a referenceable client. Internal capability validation use only. Any future reference usage requires separate BU Lead approval. Rule 21.4 applies — DFA must never be named in tender-ready content. | Mpact references lines 617–643; BU Lead decision 2026-06-12; OI-W5-003 BU Lead decision 2026-06-13 (Workforce Compensation added) |
| Redpath Mining | **Active HCM implementation — NOT yet live; NOT referenceable — BU Lead 2026-06-12** | Not in HCM register | Oracle HCM Core, Absence Management, Recruitment and Onboarding, Compensation, Talent Management — active implementation in progress, not yet complete. Redpath Mining is an active Oracle HCM implementation programme covering Core HR, Absence Management, Recruitment and Onboarding, Compensation and Talent Management. The project is not yet complete and is not approved as a referenceable client. May be referenced as active implementation pipeline evidence only where governance permits pipeline references — must not be cited as completed implementation. | BU Lead decision 2026-06-12 |
| Investec | **Scope and go-live confirmed** | Finance + Procurement (3 countries) | Oracle Fusion Financials, Procurement, iExpenses — SA, UK, USA — Go-Live July 2024 — >1,000 users | Mpact references lines 500–526 |
| Hollywood Bets | **Go-live and scope confirmed; full module list confirmed by BU Lead OI-W1-001 CLOSED 2026-06-12** | HCM (in progress) | Oracle Fusion HCM Core, Absence Management, Recruiting, Talent Management, Performance Management, Career Development, Succession Planning, Help Desk — Go-Live July 2025 — 7,000 users — OIC integration to third-party payroll — biometric integration — SETA/WSP/ATR extract | Mpact references lines 589–614; HIST-007 BOM; OI-W1-001 BU Lead decision |

---

## 20. OIC Differentiator Claim

**Claim (August 2024):** "APPSolve is the only African partner which is certified on Oracle Integration cloud."

*Source: BankServAfrica ERP Proposal (August 2024) line 274*

**Qualification:** This claim was made by APPSolve in August 2024. Certification requires both certified consultants and published Oracle success stories. This is a strong differentiator if still current.

**Temporal risk:** HIGH — this claim is approximately 22 months old at the time of this baseline update (June 2026). Oracle partner certifications change. Do not use this claim without BU Lead confirmation that it is still accurate as at the date of any tender submission.

**Related published expertise (August 2024 — temporal risk same as above):**
- Service Expertise in Oracle Cloud Platform Integration
- Service Expertise in Human Resources
- Service Expertise in Financials

---

---

## 21. Wave 3 Oracle HCM — Standing Governance Rules (established 2026-06-12)

These rules were established during Wave 3 W3S1-001 extraction and apply to ALL subsequent Wave 3 Oracle HCM capability statements.

### 21.1 Industry Sector Claims — HCM (C-W3-001)

| Rule | Detail |
|---|---|
| **Approved HCM sectors (implementation evidence)** | Retail; Mining; Professional Services |
| **Aviation — PROHIBITED in HCM content** | SAA was not awarded. Do not cite aviation as an implemented Oracle HCM sector. SAA remains source material only (platform capability context). This prohibition applies until BU Lead confirms an aviation sector award and explicitly approves the addition. |
| **Healthcare** | May only be included where supported by confirmed implementation evidence. Not currently approved for Wave 3 HCM content. |
| **SAA usage rule** | SAA HCM RFP may be used as source material for platform capability descriptions (reframed, not cited). SAA must not be named as a client, reference, or implementation in any KB content. |

### 21.2 Implementation vs Support Distinction — Oracle HCM (C-W3-002)

This distinction must be maintained in all Wave 3 Oracle HCM content. Collapsing implementation and support into a single claim is a governance violation.

| Category | Current confirmed references | Approved wording |
|---|---|---|
| **Implementation references** | Hollywood Bets (8 modules — see Section 19); Mr Price Learning Cloud | "APPSolve implemented..." |
| **Support references** | Mr Price broader Oracle HCM estate (all modules beyond Learning Cloud) | "APPSolve provides ongoing support..." |

**Prohibited:** "APPSolve implemented Oracle HCM for Mr Price Group" — APPSolve implemented Learning Cloud and Opportunity Marketplace. Broader HCM modules at Mr Price are supported, not implemented, by APPSolve.

### 21.3 Oracle Opportunity Marketplace — Approved Implementation Evidence (OI-W2-002 CLOSED 2026-06-12)

Oracle Opportunity Marketplace is an approved implementation capability for all Wave 3 statements where internal mobility, career growth, talent marketplace, skills matching, or workforce mobility capabilities are referenced.

| Rule | Detail |
|---|---|
| **Implementation evidence** | Mr Price Group — Oracle Opportunity Marketplace implemented by APPSolve |
| **Approved wording** | "APPSolve has experience implementing Oracle Opportunity Marketplace capabilities as part of broader Oracle Talent Management programmes." |
| **Do not imply** | Universal deployment across all Oracle HCM clients |
| **Scope note** | Implementation of Opportunity Marketplace at Mr Price is confirmed as part of the broader Oracle HCM support and implementation engagement — not a standalone reference |
| **Applicable statements** | W3S1-002 (Talent Management), W3S1-006 (Analytics — workforce mobility context), W3S1-003 (Recruiting — internal candidate pipeline context) |

### 21.4 DFA — Implementation Evidence Only; Not Referenceable (BU Lead 2026-06-12)

Dark Fibre Africa (DFA) is confirmed as an APPSolve implementation client for Oracle HCM. DFA is NOT approved as a referenceable client and must never be named in tender responses, case studies, or capability statements.

| Rule | Detail |
|---|---|
| **HCM scope confirmed** | Oracle HCM Core, Oracle Talent Management, Oracle Learning Cloud, Oracle Taleo Recruiting |
| **Implemented by** | APPSolve |
| **Reference status** | NOT approved — internal implementation evidence only |
| **Permitted use** | Internal capability validation only; confirms APPSolve's breadth of Oracle HCM implementation experience |
| **Prohibited use** | Named in tender responses, case studies, testimonials, client reference lists, or reusable content |
| **Future reference** | Requires separate BU Lead approval before any public or tender citation |
| **Approved fact** | "DFA confirms APPSolve implementation experience across Oracle HCM Core, Talent Management, Learning Cloud, Taleo Recruiting and Workforce Compensation. DFA is not currently approved as a referenceable client." (Updated 2026-06-13 — OI-W5-003 CLOSED) |
| **Applies to** | W3S1-001 through W3S1-009 and all future Oracle HCM statements |

---

### 21.5 Redpath Mining — Active Implementation; Not Referenceable Until Go-Live and Approval (BU Lead 2026-06-12)

Redpath Mining is an active Oracle HCM implementation programme currently in progress. Redpath is NOT approved as a referenceable client and must not be cited as a completed implementation until go-live is confirmed and referenceability separately approved.

| Rule | Detail |
|---|---|
| **HCM scope** | Oracle HCM Core (Core HR), Absence Management, Recruitment and Onboarding, Compensation, Talent Management |
| **Status** | Active implementation — not yet complete, not yet live |
| **Reference status** | NOT approved — not referenceable until go-live confirmed and separate BU Lead approval granted |
| **Permitted use** | May be described as active implementation pipeline evidence only in contexts where governance explicitly permits pipeline references |
| **Prohibited use** | Named as completed implementation, reference client, case study, testimonial, or implementation example in any reusable tender content |
| **Future reference** | Requires: (1) go-live confirmation from delivery team; (2) separate BU Lead approval for referenceability |
| **Approved fact** | "Redpath Mining is an active Oracle HCM implementation programme covering Core HR, Absence Management, Recruitment and Onboarding, Compensation and Talent Management. The project is not yet complete and is not approved as a referenceable client." |
| **Applies to** | W3S1-001 through W3S1-009 and all future Oracle HCM statements |

---

*Prepared 2026-06-10 by Claude (AI) — fact compilation from confirmed sources.*
*Updated 2026-06-11 — Sections 19 and 20 added from Mpact and BankServAfrica proposals.*
*Updated 2026-06-11 — HIST-012 (MTN 2026 DBA RFP) and HIST-013 (MTN 2014 Exec Summary) registered in Section 18.*
*Updated 2026-06-12 — Section 19 Hollywood Bets row updated with confirmed full module scope (OI-W1-001 CLOSED). Section 19 Mr Price row updated with implementation/support distinction (C-W3-002 CLOSED) and Opportunity Marketplace added (OI-W2-002 CLOSED). Section 21 Wave 3 HCM standing governance rules added (C-W3-001, C-W3-002). Section 21.3 Oracle Opportunity Marketplace approved implementation evidence added (OI-W2-002 CLOSED).*
*Updated 2026-06-12 — Section 19 DFA row updated with confirmed HCM scope (Core, Talent, Learning, Taleo Recruiting); NOT referenceable status confirmed. Section 19 Redpath Mining row added (active implementation — Core HR, Absence, Recruiting & Onboarding, Compensation, Talent — not yet live, not referenceable). Section 21.4 (DFA governance rule) and 21.5 (Redpath governance rule) added. BU Lead decisions 2026-06-12.*
*Updated 2026-06-13 — Section 19 DFA row updated: Workforce Compensation added to confirmed DFA HCM implementation scope (OI-W5-003 CLOSED — BU Lead 2026-06-13). Section 21.4 approved fact updated to include Workforce Compensation. Rule 21.4 (DFA never named) unchanged.*
*No capability content extracted. All claims sourced. All approvals require Hein Blignaut sign-off.*
