---
created: "2026-06-10"
updated: "2026-06-10"
created_by: "Claude (AI — Wave 2 source discovery)"
updated_by: "Claude (AI — Wave 2 source update: Hollywood Bets, SAA, RedPath Mining added)"
status: "Active — planning document; no extraction work performed"
---

# Oracle Wave 2 Source Map
**Date:** 2026-06-10 (updated same day) | **Owner:** Hein Blignaut | **Purpose:** Catalogue and rank all source documents available for Oracle Wave 2 extraction

This document records the result of a systematic corpus scan for Oracle source material, updated with three BU-confirmed additional sources: Hollywood Bets, South African Airways, and RedPath Mining. No content has been extracted. All source files are read-only. All paths are relative to `APPSolve Company Docs/`.

---

## Discovery Method

Filesystem scan of `Parties/Customers/` covering:
- `0. Proposal Templates/Oracle Fusion/` and `0. Proposal Templates/Oracle EBS/`
- `MTN/RFP/Archive/` (registered HIST-002)
- `ATNS/RFP/EBS Support 2025/` (unregistered — discovered this session)
- `SABS/RFP/ETS - Oracle Fusion/` (unregistered — discovered this session)
- `Truworths/RFP/` (unregistered — discovered this session)
- Broader scan for Oracle-labelled proposals across all customer folders

Cross-referenced against `DOCUMENT_REGISTER.csv` and `EXTRACTION_LOG.csv`.

---

## Primary Sources (Registered in DOCUMENT_REGISTER.csv)

### Source 1 — TMPL-001: Oracle Fusion Proposal Template

| Field | Detail |
|---|---|
| **File** | `Oracle Fusion Template.docx` |
| **Full path** | `Parties/Customers/0. Proposal Templates/Oracle Fusion/Oracle Fusion Template.docx` |
| **Document type** | TMPL — Active proposal template |
| **File size** | 17 MB |
| **Date stamp** | August 2025 (most recent update) |
| **Oracle area covered** | Oracle Cloud (Fusion): ERP/Financials, HCM, SCM, CRM, GRC, Oracle Integration Cloud |
| **Quality score** | 4/5 |
| **Reuse suitability** | High — current master template, confirmed used in SABS 2025 and SANPARKS 2024 |
| **Known risks** | ⚠️ Contains company profile years (22) that need updating to current (24); partner award claims need verification against current OPN status; review all company stats before extraction |
| **Registration status** | Registered (TMPL-001) |
| **Recommended extraction priority** | **Priority 1** — Fusion gap is the most critical content gap in the repository |

**Notes:** This template is confirmed active as of 2025. Copies exist in both SABS and SANPARKS working folders, confirming it is still being deployed. The "Oracle Fusion Information" section contains the Fusion product capability table that is the target for extraction. The company profile section contains facts that need modernisation. No client-specific content in the Fusion capability section itself.

---

### Source 2 — TMPL-002: Oracle EBS Proposal Template

| Field | Detail |
|---|---|
| **File** | `Oracle EBS Template.docx` |
| **Full path** | `Parties/Customers/0. Proposal Templates/Oracle EBS/Oracle EBS Template.docx` |
| **Document type** | TMPL — Active proposal template |
| **File size** | 17 MB |
| **Date stamp** | August 2025 |
| **Oracle area covered** | Oracle EBS: R12 Financial Management, HRMS/Payroll, Supply Chain, Procurement, Projects, DBA Services |
| **Quality score** | 3/5 |
| **Reuse suitability** | High — current master EBS template, parallel structure to TMPL-001 |
| **Known risks** | ⚠️ Date unknown at registration (now confirmed Aug 2025 file stamp); company profile identical to TMPL-001 — same year and award update needed; EBS R12 version claims need confirming against active APPSolve delivery scope |
| **Registration status** | Registered (TMPL-002) |
| **Recommended extraction priority** | **Priority 2** — EBS is a significant active delivery area; extract immediately after Fusion |

**Notes:** TMPL-002 resides in a separate folder (`Oracle EBS/`) from TMPL-001 (`Oracle Fusion/`). Both are 17 MB, consistent with a shared template infrastructure. The "Oracle EBS Information" section is the extraction target. The company profile section is likely identical to TMPL-001 — verify before extracting to avoid duplication.

---

### Source 3 — HIST-002: MTN Oracle EBS DBA Managed Services — Volume 2 (Won 2014)

| Field | Detail |
|---|---|
| **Files** | `APPSolve Executive Summary.pdf`; `APPSolve Proposal 2.1 - Technical Solution Introduction.docx`; `APPSolve Proposal 2.2 - Services.docx`; `APPSolve Proposal 2.3 - Performance Standards.docx`; `APPSolve Proposal 2.4 - Governance and Change.doc`; `APPSolve Proposal 2.5 - Transition.docx`; `APPSolve Proposal 2.6 - Exit.doc`; `APPSolve Technical Solutions Document.docx` |
| **Full path** | `Parties/Customers/MTN/RFP/Archive/ZZ Archive/RFP 20140718 close 20140801/Old Tender/MTN Tender/APPSolve Tender - Volume 2/` |
| **Document type** | HIST — Won engagement |
| **File system dates** | 2012 (note: file system dates predate the 2014 RFP folder name — files were likely drafted from older templates; actual submission was 2014-08-01 per RFP folder) |
| **Oracle area covered** | Oracle EBS DBA Managed Services: technical solution, service catalogue, SLA/performance standards, governance model, transition methodology, exit methodology |
| **Quality score** | 3/5 |
| **Reuse suitability** | High for DBA methodology and SLA framework; requires modernisation — 2012/2014 vintage; company facts, partner tier, and technology references need updating |
| **Known risks** | ⚠️ 2012 file dates suggest template reuse from pre-2014 documents — all company statistics, technology versions, and personnel references must be verified and modernised before any reuse; MTN is a named client — remove all client-identifying language during extraction; SLA commitments are historically specific — generalise rather than reuse verbatim |
| **Registration status** | Registered (HIST-002) |
| **Recommended extraction priority** | **Priority 3** — Extract after Fusion and EBS templates; DBA Executive Summary is the most reusable section |

**Notes:** The Executive Summary (PDF, 413KB) is the highest-value extraction target within this set. Section 2.1 Technical Solution Introduction also has strong methodology content. The SLA framework (2.3) and Governance model (2.4) are valuable but require substantial modernisation. All 8 files are accessible and readable.

---

## BU-Confirmed Additional Sources (Confirmed by Hein Blignaut 2026-06-10)

These three sources were confirmed by the BU lead as high-value Oracle sources. All have been read and assessed in the source mapping session. Content was read for assessment only — no extraction performed.

---

### Confirmed Source D — Hollywood Bets: Oracle HCM + 3rd Party Payroll Implementation (WON 2023)

| Field | Detail |
|---|---|
| **Primary file** | `APPSolve_HollywoodBets_Oracle Implementation 3rd part_V5.0.docx` (Accepted proposal) |
| **Full path** | `Parties/Customers/Hollywood Bets/RFP/HCM and Payroll Implementation/Accepted proposal/` |
| **Secondary file** | `APPSolve_HollywoodBets_Oracle Implementation_Technical and Pricing_V6.0.docx` (Oracle EBS Payroll option) |
| **File dates** | V5.0: April 2023; V6.0: May 2022 |
| **Engagement status** | **WON** — signed MSA + NDA + Annexure 1 (Oracle HCM Implementation V4.1 signed) + Support SLA Annexure 4 v3 signed |
| **Oracle area covered** | Oracle Fusion HCM Cloud (Base, Recruiting, Talent, Goals, Performance, Talent Review, Career Development), Oracle Integration Cloud (OIC), Oracle EBS Payroll (alternative pricing option), 3rd party payroll integration |
| **Quality score** | 4/5 |
| **Reuse suitability** | **High** — WON engagement, accepted proposal, current HCM scope is a standard APPSolve Oracle HCM delivery pattern |
| **Known risks** | ⚠️ Payroll integration is 3rd party (not Oracle native) — scope must be understood; EBS Payroll V6.0 is an alternative not the accepted path; client-specific project schedule, team names and pricing must be removed |
| **Oracle products confirmed** | Oracle Fusion HCM (7 cloud modules), OIC, EBS Payroll (alternative) |
| **Recommended extraction use** | **HCM implementation methodology** and **3rd party payroll integration pattern** — valuable for Oracle HCM tenders; provides implementation phase structure, integration data-field list, and team role model |

**Key content in this source:**
- Phase-by-phase Oracle HCM implementation plan (Phase 0 Scoping → Phase 1 HCM Core → Phase 2 Talent → Phase 3 Recruiting → Phase 4 Goal/Performance → Succession)
- Complete 3rd party payroll integration data-field list (Locations, Positions, Jobs, Grades, Employee, Assignment, Salary, Leave, Expenses, Overtime, Bonus, Tax Info, Terminations → Payslips, IRP5, IT3A, Cost2Company)
- Implementation approach: Journey Prep → Journey Workshop → Solution Reflection → Technical Build → Integration Testing → Training and UAT → Data Management → Production Build → Support/Hyper-care
- Project Infrastructure: Risk, Issue, Change Control, Configuration Management

---

### Confirmed Source E — South African Airways: Oracle Fusion HCM RFP Response (Submitted June 2025)

| Field | Detail |
|---|---|
| **Primary file** | `APPSolve_SAA_RFP.docx` (working; 9.3MB — most complete version) |
| **Full path** | `Parties/Customers/South African Airways/HCM/1.Working/` |
| **Submitted file** | `APPSolve_SAA_RFP GSM009 25_Response.pdf` (submitted; 9.7MB) |
| **Reference** | RFP GSM009/25, submitted 30 June 2025 |
| **Engagement status** | Submitted — outcome unknown |
| **Oracle area covered** | Oracle Fusion HCM — **most comprehensive Oracle HCM capability description in the corpus**: Global HR, AI-Based Dynamic Skills, Absence Management, Benefits, Journeys, Payroll Interface (3rd party + EBS Payroll option + PaySpace), Workforce Directory, Workforce Modelling, Work Life Solutions, OTBI, TDE, Workforce Compensation, Recruiting Cloud, Talent Management, Help Desk, Learning Cloud, HCM Analytics, Time and Labor, Workforce Scheduling |
| **Additional sections** | Implementation Approach (Section 5, OUM-based methodology), Company Profile (Section 6), Evaluation Criteria responses (Section 3), Assumptions (Section 7) |
| **Quality score** | **5/5** — most current (June 2025), most detailed Oracle HCM capability document in the corpus; used as primary proposal document for a major SA RFP |
| **Reuse suitability** | **Very High** — this is the template-level Oracle HCM capability description that should feed into the Oracle Fusion Capability Statement extraction |
| **Known risks** | ⚠️ SAA-specific context in executive summary (SAP ECC 6 EHP 6.0 integration, SAA restructuring) must be stripped; pricing section must be excluded; headcount figure in company profile needs to be verified against approved value (SAA document may use outdated numbers) |
| **Oracle products confirmed** | Oracle Fusion HCM (full suite), OIC, Oracle EBS Payroll (option), PaySpace integration (option), OCI |
| **Recommended extraction use** | **Primary source for Oracle Fusion Capability Statement** — the "Oracle Fusion Information" section (Section 2) contains the complete capability matrix with Overview + 15+ HCM module descriptions, each with Overview / Benefits / Key Features / Capabilities table |

**Supplementary documents found in SAA submission folder:**
- `OCI SOC 1 Report Bridge Letter_June 2025` — Oracle's OCI SOC 1 compliance certification (current to June 2025) — confirms OCI security compliance documentation is available for tenders
- `OCI SOC 2 Report Bridge Letter_June 2025` — OCI SOC 2 compliance certification (current to June 2025)
- `Oracle_Scalability and Global Footprint.pdf` — Oracle-provided document on OCI/Fusion scale and global footprint; useful supporting document for cloud tenders
- `Gartner Market Intelligence Report.pdf` — Oracle positioned in Gartner analysis; useful market positioning reference

**References submitted with SAA tender:**
DFA, Adcock Ingram 2023, Mr Price 2024, Oracle Letter 2024, Tiger Brands, SAA Tiger Reference Letter SAP Integration

**Critical BEE finding from SAA submission folder:**
- `BEE Level 2 - APPSolve (Pty) Ltd RS-17968-0724-C58 20250716.pdf` — **Level 2 cert, July 2024 vintage** (used for HCM submission June 2025)
- `BBBEE Level 3 - APPSolve (Pty) Ltd RS-19451-0825-C3-20260731.pdf` — **Level 3 cert, August 2025 vintage, expires 2026-07-31** — the CURRENT certificate
- **Action required:** APPSolve's BEE level is currently **Level 3** (not Level 2). The Level 3 cert expires 2026-07-31. All future tenders must use the Level 3 cert and cite Level 3. Update AI_CONTEXT.md and CHECKPOINT to reflect Level 3.

---

### Confirmed Source F — RedPath Mining: Oracle Fusion Cloud ERP SI Evaluation (Active 2026)

| Field | Detail |
|---|---|
| **Primary file** | `RedPath Mining_APPSolve_RFI Reply Detail.docx` (7.2MB, March 2026) |
| **Full path** | `Parties/Customers/RedPath Mining/Working/` |
| **Submitted file** | `RedPath Mining_APPSolve_SI Evaluation Detail.pdf` (1.6MB, March 2026) |
| **Contract status** | **ACTIVE** — EY Subcontractor Agreement fully executed April 17, 2026; APPSolve is Oracle Fusion Cloud ERP SI sub-contractor to EY for Redpath Mining South Africa |
| **Oracle area covered** | Oracle Fusion Cloud ERP: Finance, HCM, SCM, Procurement, Projects/PPM; Oracle Integration Cloud (OIC); Oracle Cloud Infrastructure (OCI) |
| **Quality score** | **5/5** — active, signed engagement; March 2026; most current Oracle Fusion Cloud positioning document |
| **Reuse suitability** | **Very High** — the SI Evaluation response describes APPSolve's Oracle Fusion Cloud capability using current language; implementation methodology is described in detail; client list is confirmed; certifications are current |
| **Known risks** | ⚠️ Company profile in document uses OUTDATED FACTS — "110 Senior Consultants" and "over 22 years" and "19 years' experience" for Hein — ALL PROHIBITED; use approved values (50+, 23 years, ~30 years) instead; do not extract company profile text from this source |
| **Oracle products confirmed** | Oracle Fusion Cloud ERP (Finance, HCM, SCM, PPM), OIC, OCI, Oracle Fusion Payroll |
| **Recommended extraction use** | **Validation source for Oracle Fusion Capability Statement** — confirms capability coverage, implementation methodology, and confirmed client list; do NOT use company profile section |

**Key content confirmed in RedPath Mining RFI:**
- Confirmed Oracle Fusion Saas implementations: DFA (Finance, Procurement, Project, HCM, OIC), Cape Union Mart (Finance, SCM, Procurement, OIC), Hollywood Bets (HCM, OIC), Mr Price (HCM, OIC), Investec Bank (Finance, Procurement, OIC — 3 countries), Nala Renewables (Finance, Project — 8 countries)
- Mining sector Oracle clients: Assore, ARM (African Rainbow Minerals), Harmony
- OIC used in ALL Oracle Fusion implementations — confirmed standard practice
- Implementation methodology: Mobilize → Scoping → Prototype → Build → Deploy (OUM-based)
- Data migration: Oracle FBDI sheets and APIs; more4apps as optional tool
- Security: Role-based access; AOR (Area of Responsibility) for HCM; Oracle license compliance tool developed by APPSolve
- Reporting: OTBI and BI Publisher; Visual Builder Studio (VB Studio) for Redwood UI

**Consultant Certifications confirmed in RedPath Mining Consultant Certificates folder:**
| Consultant | Certification |
|---|---|
| Hein Blignaut | OCI Architect |
| Carin Webb | Oracle Cloud Infrastructure 2025 + App Integration Professional |
| Esna Pretorius | Oracle Accounting Hub Cloud + Oracle Fusion Cloud Financials Implementation Professional |
| Gavin Sadler | Oracle Fusion Cloud Financials Implementation Professional + Oracle Financials Cloud Payables Implementation |
| Ian de Koker | Oracle Global HR Cloud 2021 + Oracle Recruiting Cloud 2022 Implementation Professional |
| Jono | Oracle Cloud Platform App Integration 2022 Professional |
| Kiran | Oracle Receivables Cloud Implementation Certificate |
| Rahul Dave | Oracle Fusion Cloud Procurement Implementation + Oracle Fusion PPM Implementation Specialist |
| Michael | HCM Cloud Implementation |
| Sam | Oracle Cloud Infrastructure AI Foundations Associate |

**New Reference Letters confirmed in RedPath Mining References folder:**
- `Reference 202507 MTN Reference Letter.pdf` — **MTN July 2025 reference letter** — brand new, most recent MTN reference
- `Reference 2025 Stellenbosch University.pdf` — **Stellenbosch University 2025** — new reference letter not in ATNS/SABS submissions
- Plus standard set: NALA, Assore 2023, Investec 2023, Harmony 2024, Mr Price 2024

---

### Confirmed Source G — SABS Oracle Fusion ETS Response (December 2025) [Updated assessment]

The SABS ETS response was read in full. It is a **capability table** (not a full proposal) listing reference implementations for each Oracle module. Content is brief but confirms the full client/module matrix.

**Key content confirmed:**
- Finance/SCM references: Nala (Fusion multi-country), Cape Union Mart (Fusion Finance + Procurement), Investec (Fusion Finance + Procurement SA/US/UK), KPMG (EBS SADC 6 countries), Assore (EBS support), Adcock Ingram (EBS)
- HCM references: Mr Price (Fusion HCM + Time and Labour — stores rollout), Hollywood Bets (Fusion HCM full suite + 3rd party payroll), Investec (HCM + Payroll), KPMG (Taleo), Dark Fibre Africa (full Oracle suite)
- PPM references: Dark Fibre Africa, KPMG
- **Dark Fibre Africa (DFA)** is APPSolve's most comprehensive Oracle Fusion implementation — covers Finance, SCM, HCM, Learning, Goal/Performance, Taleo Recruiting, **Oracle Payroll Cloud** (native), OIC, EPM

| Field | Detail |
|---|---|
| **Quality score** | 2/5 (for content depth — reference table only, not a capability document) |
| **Recommended use** | Reference table validation only; confirms client implementations are current and accepted in formal tender submissions |

---

## Previously Discovered Sources (Unregistered)

These sources were discovered during the Wave 2 scan but are not registered in DOCUMENT_REGISTER.csv. They are noted here for planning purposes only. Do not extract from these sources without first adding them to the register and confirming with BU lead.

---

### Discovered Source A — ATNS Oracle EBS Support Proposal 2025

| Field | Detail |
|---|---|
| **File** | `ATNS_APPsolve Support Proposal V2.docx` |
| **Full path** | `Parties/Customers/ATNS/RFP/EBS Support 2025/1.Working/ATNS_APPsolve Support Proposal V2.docx` |
| **Submitted** | May 2025 — outcome unknown |
| **Oracle area covered** | Oracle EBS managed services/DBA support, SLA, governance |
| **Quality score** | 4/5 (estimated — recent, polished multi-version proposal) |
| **Reuse suitability** | Very high — most recent Oracle EBS support proposal in corpus; May 2025 submission reflects current positioning |
| **Known risks** | ATNS client-specific language must be removed; outcome unknown (may or may not be a won engagement) |
| **Registration status** | **Not registered** — not in DOCUMENT_REGISTER.csv |
| **Recommended action** | Register in DOCUMENT_REGISTER.csv as HIST-006 (or next available HIST ID); add to EXTRACTION_LOG.csv before extracting |

**Why this matters:** This is a 2025 Oracle EBS support proposal — more current than the MTN 2014 HIST-002 source. If confirmed as a submitted or won tender, this becomes the preferred source for Oracle EBS managed services and DBA support content, superseding HIST-002 for the methodology sections. It also includes the same reference letters used in the SABS Fusion submission (Assore, Harmony, Investec, Oracle, ARM, Adcock Ingram, NALA) confirming these letters are currently in active tender use.

---

### Discovered Source B — SABS Oracle Fusion ETS Response (Dec 2025)

| Field | Detail |
|---|---|
| **File** | `APPSolve_SABS_RFP_Response.docx` |
| **Full path** | `Parties/Customers/SABS/RFP/ETS - Oracle Fusion/APPSolve_SABS_RFP_Response.docx` |
| **Date** | December 2025 (file stamp) |
| **Oracle area covered** | Oracle Fusion (ERP/Cloud) — likely an ETS evaluation response |
| **File size** | 23 KB (small — likely a short ETS or capability questionnaire response, not a full proposal) |
| **Reuse suitability** | Low for bulk content; potentially useful for Oracle Fusion capability framing and recent positioning language |
| **Registration status** | Not registered |
| **Recommended action** | Read before any Fusion extraction to confirm what capability claims APPSolve made most recently; small file makes this a quick read |

---

### Discovered Source C — Truworths Oracle R12 Upgrade Proposals (2014)

| Field | Detail |
|---|---|
| **Files** | `Truworths Oracle R12 Scoping and Implementation Proposal v1 14022014.docx`; `v2 14022014.docx` |
| **Full path** | `Parties/Customers/Truworths/RFP/Upgrade/` |
| **Date** | February 2014 |
| **Oracle area covered** | Oracle EBS R12 upgrade/implementation methodology |
| **Reuse suitability** | Moderate — methodology content useful; heavily dated (2014); client-specific scope |
| **Registration status** | Not registered |
| **Recommended action** | Lower priority than ATNS 2025 for EBS methodology; consider registering as HIST-007 if Wave 2 EBS extraction needs additional methodology depth |

---

## Source Comparison Table (Updated)

| ID | Source | Type | Date | Area | Quality | Role in extraction |
|---|---|---|---|---|---|---|
| TMPL-001 | Oracle Fusion Template | Active template | Aug 2025 | Fusion/Cloud ERP + HCM + SCM | 4/5 | **Primary: Oracle Fusion Capability Statement** |
| Source E | SAA HCM RFP Response | Submitted tender | June 2025 | Oracle Fusion HCM (full suite) | **5/5** | **Primary: Oracle Fusion HCM detail** — "Oracle Fusion Information" section is a complete HCM capability matrix |
| Source F | RedPath Mining RFI Reply | Active engagement | March 2026 | Oracle Fusion Cloud full ERP + HCM | **5/5** | **Validation: confirm capability, methodology, and client list** — DO NOT extract company profile (outdated stats) |
| Source G | SABS ETS Response | ETS table | Dec 2025 | Fusion capability/reference table | 2/5 | **Reference validation only** — confirms current client/module matrix |
| TMPL-002 | Oracle EBS Template | Active template | Aug 2025 | EBS R12 | 3/5 | **Primary: Oracle EBS Capability Statement** |
| Source A | ATNS EBS Support 2025 | Submitted tender | May 2025 | EBS DBA Support | 4/5 | **Primary: Oracle EBS managed services/DBA sections** — more current than HIST-002 for EBS support |
| HIST-002 | MTN DBA Volume 2 | Won tender | 2014 | EBS DBA Managed Services | 3/5 | **Supplementary: DBA methodology depth** — use for SLA framework and governance model structure |
| Source D | Hollywood Bets proposal | Won tender | 2023 | Oracle HCM + OIC + payroll integration | 4/5 | **Oracle HCM implementation methodology** — phase structure, team roles, integration field list |
| Discovered C | Truworths R12 Upgrade | Historical | 2014 | EBS R12 implementation | 2/5 | Low priority — tertiary EBS methodology source |

---

## Pre-Extraction Actions Required (Updated)

| Action | Owner | Notes |
|---|---|---|
| **Update BEE Level to 3 in all governance docs** | AI (now) | Current cert: Level 3 (RS-19451, issued Aug 2025, expires 2026-07-31). Previous cert was Level 2. Update AI_CONTEXT.md and CHECKPOINT_WAVE1. |
| Register SAA HCM response in DOCUMENT_REGISTER.csv | AI (next extraction session) | Assign HIST-006 (or next available ID); add to EXTRACTION_LOG.csv |
| Register Hollywood Bets in DOCUMENT_REGISTER.csv | AI (next extraction session) | Assign HIST-007; add to EXTRACTION_LOG.csv |
| Register RedPath Mining RFI in DOCUMENT_REGISTER.csv | AI (next extraction session) | Assign HIST-008; note active 2026 engagement; add to EXTRACTION_LOG.csv |
| Register ATNS EBS Support 2025 in DOCUMENT_REGISTER.csv | AI (next extraction session) | Assign HIST-009; add to EXTRACTION_LOG.csv |
| Register MTN July 2025 and Stellenbosch 2025 reference letters | AI | New Oracle reference letters found in RedPath Mining folder; register in 04_References/Oracle/ |
| Confirm file system dates on HIST-002 | Hein Blignaut | 2012 file dates vs. 2014 RFP folder — affects modernisation effort estimate |
| Update AI_CONTEXT.md folder references | AI | `08_Methodologies/` → `05_Methodologies/`; remove `09_Executive_Summaries/` |

---

*Prepared 2026-06-10 by Claude (AI) — source discovery only. No content extracted. Source files are read-only.*
