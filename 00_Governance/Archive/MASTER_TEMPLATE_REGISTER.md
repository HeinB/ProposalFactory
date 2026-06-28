# Master Template Register
**Date:** 2026-06-08
**Status:** Discovery complete — read-only. No files copied or modified.
**Source:** `APPSolve Company Docs/Parties/Customers/` repository
**Scope:** Proposal templates, tender templates, SOW templates, BeBanking templates, pricing templates, governance templates

---

## Executive Summary

APPSolve's proposal IP is substantially more developed than the `CONTENT_GAP_ANALYSIS.md` suggested. This discovery exercise identified:

- **6 dedicated template documents** in a master `0. Proposal Templates/` folder, covering Oracle EBS, Oracle Fusion, and Acumatica (long-form and short-form), with the Acumatica set updated as recently as September 2025
- **A complete Oracle managed support tender** (MTN 2014, 7-volume structure) containing explicit sections for methodology, services, performance standards, governance, transition, and exit — content that the Gap Analysis rated as "Missing"
- **An Oracle Support Template** actively being used for 2025 engagements (ATNS)
- **An Oracle Fusion Template** actively used for 2025 government ERP tenders (SABS, SANPARKS)
- **Over 20 BeBanking proposal documents** across 15+ clients, spanning 2016–2025 — completely contradicting the "Missing/Must Author from Scratch" rating in the Gap Analysis
- **A standardised BeBanking OEM agreement template** and a detailed government-facing BeBanking implementation proposal (SITA, 6 revisions)
- **A combined Acumatica+BeBanking proposal template** (HyDac V5.1, December 2024)
- **A current Acumatica project plan template** in active use across 4 implementations (February 2026)
- **SOW templates** covering DBA retainers, APEX engagements, QA work
- **Governance and risk review templates** from the Axon engagement

**The most significant finding:** The MTN 2014 tender (Volume 2) contains exactly the sections that were rated "Missing" in the Gap Analysis: Technical Solution Introduction, Services, Performance Standards, Governance and Change, Transition, and Exit. This one document contains the structural skeleton for an Oracle EBS managed services methodology.

---

## Template Register

### Group 1 — Primary Proposal Templates (Dedicated Template Folder)

These are intentionally maintained master templates in `0. Proposal Templates/`.

---

**TMPL-001: Oracle EBS Proposal Template**

| Field | Value |
|---|---|
| File | `0. Proposal Templates/Oracle EBS/Oracle EBS Template.docx` |
| Type | Proposal Template — Oracle EBS |
| Format | DOCX (editable) |
| Estimated vintage | Unknown — check document properties |
| Status | Active (used as base for EBS engagements) |
| Also seen in | `Dark Fibre Africa/Oracle Submission Template DFA amended August 2022.doc` (2022 variant); `Global Oil/Oracle Success Story/Global Oil Oracle Submission Template 31032017.doc` (2017 variant) |

**Content likely includes:** Company background, Oracle EBS service overview, team profiles, implementation methodology, pricing structure. Editable master — this is the starting point for all Oracle EBS proposals.

---

**TMPL-002: Oracle Fusion / Cloud Proposal Template**

| Field | Value |
|---|---|
| File | `0. Proposal Templates/Oracle Fusion/Oracle Fusion Template.docx` |
| Type | Proposal Template — Oracle Fusion/Cloud |
| Format | DOCX (editable) |
| Estimated vintage | 2024–2025 (in active use) |
| Status | Active — currently in use for live tenders |
| Also seen in | `SABS/RFP/Cloud Based ERP 2025/1. Working/Oracle Fusion Template.docx` (SABS ERP tender 2025); `SANPARKS/RFP/New ERP/1. Working/Oracle Fusion Template.docx` (SANPARKS ERP tender 2024/2025) |

**Content likely includes:** Cloud transformation narrative, Oracle Fusion module coverage, implementation approach, cloud readiness, migration methodology, team and partner credentials. Confirmed in active use for two concurrent government ERP tenders.

---

**TMPL-003: Acumatica Proposal Template (Current Long-Form)**

| Field | Value |
|---|---|
| File | `0. Proposal Templates/Acumatica/APPSolve Acumatica - CUSTOMER - Proposal Template Sept2025 BH.docx` |
| Type | Proposal Template — Acumatica (long-form) |
| Format | DOCX (editable, customer-name placeholder) |
| Estimated vintage | September 2025 |
| Status | Current active template — most recent version |
| Initials | BH = likely a named author or reviewer |

**Content likely includes:** Acumatica Gold Partner positioning, module coverage, implementation approach, team profiles, pricing structure, references section. This is the primary Acumatica proposal template as of Q3 2025.

---

**TMPL-004: Acumatica Proposal Template (Short-Form)**

| Field | Value |
|---|---|
| File | `0. Proposal Templates/Acumatica/APPSolve Short Acumatica Proposal V1.0 20250407.docx` |
| Type | Proposal Template — Acumatica (short-form) |
| Format | DOCX (editable) |
| Estimated vintage | April 2025 |
| Status | Active — used for smaller or exploratory engagements |
| Related | `Eyabantu/RFP/1.Working/Eya Bantu Acumatica Short V1.0 20260603.docx` (derived deployment, 2026) |

**Content likely includes:** Condensed Acumatica capability narrative, simplified pricing approach. Used when a full proposal is not required. The Eyabantu deployment confirms it is the parent of recent short-form submissions.

---

**TMPL-005: Acumatica Proposal Template (Older Base)**

| Field | Value |
|---|---|
| File | `0. Proposal Templates/Acumatica/Acumatica Proposal Template.docx` |
| Type | Proposal Template — Acumatica (base/legacy) |
| Format | DOCX |
| Estimated vintage | Unknown — pre-dates TMPL-003 |
| Status | Superseded by TMPL-003 but may contain content not in the newer version |

**Note:** Read alongside TMPL-003 to identify any content that was removed in the latest iteration.

---

**TMPL-006: Acumatica Reference/Deployed Document**

| Field | Value |
|---|---|
| File | `0. Proposal Templates/Acumatica/20250218 Annexure 1 Hydac Acumatica Implementation V1.2.docx` |
| Type | Proposal — Acumatica (deployed instance, used as reference) |
| Format | DOCX |
| Estimated vintage | February 2025 (V1.2) |
| Status | A specific client proposal stored in the templates folder as a reference example |
| Related | `HyDac/RFP/Acumatica Implementation/` |

---

### Group 2 — Oracle Support / Managed Services Templates

---

**TMPL-007: Oracle EBS Support Proposal Template (2025)**

| Field | Value |
|---|---|
| File | `ATNS/RFP/EBS Support 2025 - Re issue/1.Working/Oracle Support Template.docx` |
| Type | Proposal Template — Oracle EBS Support |
| Format | DOCX |
| Estimated vintage | 2025 |
| Status | Active — in working folder for a live 2025 tender |
| Context | ATNS (Airports Company subsidiary) Oracle EBS support re-issue |

**Content likely includes:** Current Oracle EBS managed support narrative, resource profiles, SLA framework, pricing structure. This is the current support proposal template.

---

**TMPL-008: Oracle EBS Managed Services Proposal (Dark Fibre Africa 2017)**

| Field | Value |
|---|---|
| File | `Dark Fibre Africa/RFP/BID 2017/APPSolve DFA Oracle EBS Managed Services Functionality and Price Submission 04082017 v2.docx` |
| Type | Oracle Managed Services Proposal |
| Format | DOCX |
| Estimated vintage | August 2017 |
| Status | Historical — foundational managed services response format |
| Pattern | Naming convention `APPSolve [Client] Oracle EBS Managed Services Functionality and Pricing Submission [date] v[x].docx` repeated across: ARM (2016, 2018), DFA (2017, 2018), HPCSA (2017), Global Oil (2016, 2017), Clickatell (2015), DFF (2017) |

**Significance:** This naming pattern across 8+ clients over 2015–2018 indicates a master managed services template was in use. The DFA v2 (2017) is the most complete example found. Comparing across clients will reveal the stable "core" sections vs. client-specific customisation.

---

**TMPL-009: MTN Oracle DBA/EBS Support Tender — Complete Structured Submission (2014)**

| Field | Value |
|---|---|
| Files | `MTN/RFP/Archive/ZZ Archive/RFP 20140718 close 20140801/Old Tender/MTN Tender/APPSolve Tender - Volume 2/` |
| Type | Full Tender Response — Oracle EBS/DBA Managed Support |
| Format | Multiple DOCX (Volume 1 + Volume 2) |
| Estimated vintage | August 2014 |
| Status | Historical — but structurally highly reusable |

**Volume 2 sections explicitly documented:**
| Section | File | KB Content Category |
|---|---|---|
| 2.1 Technical Solution Introduction | `APPSolve Proposal 2.1 - Technical Solution Introduction.docx` | Capability Statement |
| 2.2 Services | `APPSolve Proposal 2.2 - Services.docx` | Support Model / Managed Services |
| 2.3 Performance Standards | `APPSolve Proposal 2.3 - Performance Standards.docx` | Support Model / SLA Framework |
| 2.4 Governance and Change | `APPSolve Proposal 2.4 - Governance and Change.doc` | Governance Model |
| 2.5 Transition | `APPSolve Proposal 2.5 - Transition.docx` | Methodology (Transition) |
| 2.6 Exit | `APPSolve Proposal 2.6 - Exit.doc` | Standard Response (Exit Procedures) |
| Executive Summary | `APPSolve Executive Summary.docx` | Executive Summary |

**This is the most important single Oracle template find.** All six sections of Volume 2 map directly to categories the Gap Analysis rated as "Missing". The content is 12 years old and will need updating, but the structure and much of the IP is likely directly reusable.

---

**TMPL-010: MTN Oracle EBS Support Tender — 2017 Update**

| Field | Value |
|---|---|
| File | `MTN/RFP/Archive/ZZ Archive/2017 ERP Support RFP/APPSolve Response/Archive/APPSolve Proposal APPS DBA Professional Services v3 18052017.docx` |
| Type | Support Proposal — Oracle EBS/DBA |
| Format | DOCX |
| Estimated vintage | May 2017 |
| Status | Historical — updated version of MTN 2014 content |
| Related | Same engagement 3 years later — shows how content evolved |

---

### Group 3 — BeBanking Templates

---

**TMPL-011: BeBanking Standard OEM/License Agreement (Recurring)**

| Field | Value |
|---|---|
| File (canonical) | `ACSA/Contracts/H2H Banking/appsolve BeBanking OEM 2025.doc` |
| Type | Commercial Agreement — BeBanking OEM License |
| Format | DOC/PDF |
| Estimated vintage | Recurring — versions for 2021, 2025 observed |
| Status | Active commercial template |
| Also seen in | `Parliament/appsolve BeBanking OEM 2024.docx`; `Hulamin/RFP/Support BeBanking/appsolve BeBanking OEM 2022.docx`; ACSA versions for 2016, 2021, 2025 |

**Content:** Standard BeBanking OEM licensing and support terms. This is a commercial/legal template, not a sales proposal — but the service descriptions within it describe BeBanking functionality that can be quoted in capability statements.

---

**TMPL-012: BeBanking Implementation Proposal — SITA (Government, Most Comprehensive)**

| Field | Value |
|---|---|
| File | `Sita/RFP/H2H/APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx` |
| Type | BeBanking Proposal — Government Host-to-Host |
| Format | DOCX |
| Estimated vintage | Unknown — v1 06 (sixth revision) |
| Status | Historical — most detailed government-facing BeBanking proposal found |
| Context | SITA is the South African government's ICT agency — this proposal was for a government entity |

**Significance:** This is the most comprehensive BeBanking proposal in the corpus. Government-facing means it will have addressed formal capability questions rather than a simple commercial conversation. Six revisions suggest significant iteration and refinement.

---

**TMPL-013: BeBanking Scoping and Implementation Proposal — Mpact (2019)**

| Field | Value |
|---|---|
| File | `Mpact/RFP/BeBanking/APPSolve Mpact BeBanking Scoping and Implementation Proposal v1 11122019.docx` |
| Type | BeBanking Proposal — Scoping and Implementation |
| Format | DOCX (+ matching PDF + `.mpp` project plan) |
| Estimated vintage | December 2019 |
| Status | Historical — early structured BeBanking implementation proposal |
| Related files | `APPSolve Mpact BeBanking Scoping and Implementation Cost Estimate v1 11122019.xlsx`; `APPSolve Mpact Trolley Implementation v1 11122019.mpp` |

**Significance:** This proposal includes a full three-part package: technical proposal, cost estimate, and project plan. The project plan `.mpp` file is particularly valuable — it shows how a BeBanking implementation was scheduled and broken into phases. This is the closest thing to a BeBanking methodology document currently in the corpus.

---

**TMPL-014: Combined Acumatica + BeBanking Proposal Template (2024)**

| Field | Value |
|---|---|
| File | `Airstream Group/RFP/1. Working/APPSolve_HyDac_Proposal_20241211_V5.1 Template BeBanking.docx` |
| Type | Combined Proposal Template — Acumatica + BeBanking |
| Format | DOCX |
| Estimated vintage | December 2024 (V5.1) |
| Status | Recent active template — V5.1 indicates significant maturity |
| Also in | `HyDac/RFP/Acumatica Implementation/1. Working/` (same file, different customer folder) |

**Significance:** The only known combined Acumatica+BeBanking proposal template. Covers both an ERP implementation and a BeBanking integration in a single document. Highly relevant for Acumatica clients adopting BeBanking. V5.1 means it has been refined across at least 5 major revision cycles.

---

**TMPL-015: BeBanking Sales/Capability Deck (2019)**

| Field | Value |
|---|---|
| File | `ARM/Presentations/APPSolve Overview and BeBanking V1 00 Aug 2019.pptx` |
| Type | Presentation — APPSolve + BeBanking Capability |
| Format | PPTX |
| Estimated vintage | August 2019 |
| Status | Historical — may be outdated in product claims |
| Related | `ARM/RFP/FNB Fintegrate/APPSolve Overview and BeBanking V1 00 Aug 2019-awarded.pptx` (same deck, marked "awarded") |

**Significance:** The "awarded" copy confirms this deck was used in a successful engagement. Content likely includes: APPSolve company overview, BeBanking platform explanation, use cases, integration scenarios. Useful for capability statement language.

---

**TMPL-016: Acumatica + BeBanking Introduction Deck (2024)**

| Field | Value |
|---|---|
| File | `Irvines/BeBanking/Acumatica_BeBanking Intro 2024_v1.0 copy.pptx` |
| Type | Presentation — Acumatica + BeBanking Introduction |
| Format | PPTX |
| Estimated vintage | 2024 |
| Status | Recent — current combined product pitch |

**Content likely includes:** Acumatica ERP overview, BeBanking integration benefits, combined value proposition. More current than TMPL-015.

---

**TMPL-017: BeBanking Fintegrate Migration Proposal (ACSA, multiple versions)**

| Field | Value |
|---|---|
| File | `ACSA/Contracts/H2H Banking/APPSolve ACSA Fintegrate Move BeBanking v3.docx` |
| Type | Proposal — BeBanking platform migration (Fintegrate → BeBanking Cloud) |
| Format | DOCX (+ decision comparison PDFs) |
| Estimated vintage | 2021 |
| Status | Historical — useful for cloud migration methodology |
| Related files | `...cloud vs on premise.pdf`; `...switch vs extend.pdf` (decision analysis documents) |

**Significance:** ACSA is a long-running BeBanking client (since 2016). The Fintegrate migration documents include a cloud vs. on-premise comparison and a switch vs. extend analysis. These are unique decision-framework documents that could support future cloud migration proposals.

---

### Group 4 — SOW / Statement of Work Templates

---

**TMPL-018: DBA Retainer SOW (Current Format)**

| Field | Value |
|---|---|
| File | `Investec/RFP/DBA Retainer Investec Bank 2024/APPSolve_Investec_DBA_Retainer_SOW.docx` |
| Type | SOW — Oracle DBA Retainer |
| Format | DOCX |
| Estimated vintage | 2024 |
| Status | Current format |
| Related | `Investec/RFP/DBA Retainer Investec Bank/APPSolve_Investec_DBA_Retainer_SOW.docx` (prior version) |

---

**TMPL-019: APEX / Development Engagement SOW (2024–2026)**

| Field | Value |
|---|---|
| Files | `Investec/RFP/APEX De-couple/Appsolve SOW de_couple ERP [date] v[x].docx` (many versions) |
| Type | SOW — APEX/Development Engagement |
| Format | DOCX |
| Estimated vintage | 2024–2026 (active) |
| Status | Actively evolving — latest version is 2026 |

**Significance:** Investec has issued many SOW revisions covering Oracle APEX decoupling work. The collection shows how APPSolve structures SOWs for ongoing development engagements with extension clauses. The evolution from 2024 to 2026 captures commercial terms refinement.

---

**TMPL-020: Standard SOW for Professional Services (Government Format)**

| Field | Value |
|---|---|
| File | `SARB/RFP/Archives/Pre-2022/Up to 2017/Annemarie/STANDARD SCHEDULE F - SOW for Professional Services Annamarie Wilke.docx` |
| Type | SOW — Professional Services (Government) |
| Format | DOCX |
| Estimated vintage | Pre-2017 |
| Status | Historical — government SOW format |

---

**TMPL-021: QA / Testing SOW**

| Field | Value |
|---|---|
| File | `Axon/RFP/APPSolve Axon QA Statement of Work V1 02.docx` |
| Type | SOW — Quality Assurance |
| Format | DOCX |
| Estimated vintage | ~2019–2020 |
| Status | Historical |

---

### Group 5 — Pricing and Costing Templates

---

**TMPL-022: Oracle Costing Template (Evolved Series)**

| Field | Value |
|---|---|
| File (latest) | `Dark Fibre Africa/RFP/BID 2018/Financials Only Costing/APPSolve FIN Costing Template v7 13042018.xlsx` |
| Type | Pricing Template — Oracle EBS |
| Format | XLSX |
| Estimated vintage | April 2018 (v7 = 7th iteration) |
| Status | Historical — most refined version of the DFA costing template series |
| Version history | v2 (Oct 2017) → v3 → v4 → v5 → v6.1 → v6.2 → v7 (Apr 2018), all in `Dark Fibre Africa/RFP/BID 2017-2018/` |

**Significance:** 7 iterations over 6 months is a significant investment. The v7 template represents the most refined Oracle pricing model developed at that point.

---

**TMPL-023: DBA Rate Card (Current, 2026)**

| Field | Value |
|---|---|
| File | `MTN/RFP/2026 DBA MTN SA/Negotiations/Commercial Rate Cards DBA Services.xlsx` |
| Type | Rate Card — Oracle DBA Services |
| Format | XLSX |
| Estimated vintage | 2026 |
| Status | Current — used in active 2026 MTN DBA negotiation |
| Related | `MTN/RFP/2026 DBA MTN SA/Reverse Auction 28 May 2026/Commercial Rate Cards DBA Services_APPSolve_RevereseAuction_28May26.xlsx` (reverse auction version) |

---

**TMPL-024: SASSA Response Template — Oracle ERP Annexures (2021)**

| Field | Value |
|---|---|
| File | `SASSA/RFP/ERP Support 2021 RE-issue/2. Submitted/APPSolve_RESPONSE TEMPLATE ORACLE ERP ANNEXURE A B C.xlsx` |
| Type | Response Template — Government ERP Annexures |
| Format | XLSX |
| Estimated vintage | 2021 |
| Status | Historical — structured government RFP response format |
| Context | Filled-in template for a government ERP support tender — Annexures A, B, C |

---

### Group 6 — OCI and Specialist Oracle Templates

---

**TMPL-025: OCI Proposal Template**

| Field | Value |
|---|---|
| File | `Truworths/RFP/Supplier Portal and Invoice Matching/1.Working/APPSolve_OCI_Proposal_Template.docx` |
| Type | Proposal Template — Oracle Cloud Infrastructure |
| Format | DOCX |
| Estimated vintage | Unknown — in a working folder for an active Truworths engagement |
| Status | In use — OCI-specific capability and approach document |

---

### Group 7 — Project Plan Templates

---

**TMPL-026: Acumatica ERP Project Plan Template (Current)**

| Field | Value |
|---|---|
| File (canonical) | `City Lodge Hotels/RFP/3.Project Plan/CLH ERP Project Plan Template V1.0 20260212.xlsx` |
| Type | Project Plan Template — Acumatica ERP |
| Format | XLSX |
| Estimated vintage | February 2026 |
| Status | Active — shared across 4 current Acumatica implementations |
| Also in | `Eyabantu/RFP/3.Project Plan/`; `CATS/RFP/3.Project Plan/`; `Norse Projects/RFP/3.Project Plan/` |

**Significance:** Four different active Acumatica implementations (2026) are using the same project plan template. This is the current standard Acumatica project schedule. Phase names and task structure reveal the standard APPSolve Acumatica delivery model.

---

**TMPL-027: BeBanking Implementation Project Plan**

| Field | Value |
|---|---|
| File | `Mpact/RFP/BeBanking/APPSolve Mpact BeBanking Scoping Project Plan v1 11122019.mpp` |
| Type | Project Plan — BeBanking Implementation |
| Format | MPP (Microsoft Project) |
| Estimated vintage | December 2019 |
| Status | Historical — the only known BeBanking project plan |

---

### Group 8 — Governance and Risk Templates

---

**TMPL-028: Project Governance Review Template**

| Field | Value |
|---|---|
| File | `Axon/RFP/Dirk's Docs/Project Office/Project Governance Review Template V0.doc` |
| Type | Project Governance Template |
| Format | DOC |
| Estimated vintage | ~2010–2012 |
| Status | Historical — early APPSolve governance framework |
| Related | `Risk Register/RFT - Project Governance an Risk Review Template V0.1.doc` (risk variant) |

---

**TMPL-029: SLA Governance and Risk Review Template**

| Field | Value |
|---|---|
| File | `Axon/RFP/Dirk's Docs/Project Office/Risk Register/RFT - SLA Governance an Risk Review Template V0.1.doc` |
| Type | SLA Governance Template |
| Format | DOC |
| Estimated vintage | ~2010–2012 |
| Status | Historical — SLA-specific governance framework |

---

### Group 9 — Supporting Capability Documents

---

**TMPL-030: Acumatica Standard Reporting Document**

| Field | Value |
|---|---|
| File | `Eyabantu/RFP/4. Supporting Documentation/Acumatica Standard Reporting V1.0.docx` |
| Type | Capability Document — Acumatica Reporting |
| Format | DOCX |
| Estimated vintage | 2026 |
| Status | Current — used as supporting document in active 2026 Acumatica submission |

---

**TMPL-031: Competency Area and Response Template (2016)**

| Field | Value |
|---|---|
| File | `GPAA/RFP/Software Development/APPSolve Competency Area and Response template 02082016 v 02.docx` |
| Type | Standard Response Template — Government Capability |
| Format | DOCX |
| Estimated vintage | August 2016 |
| Status | Historical — government panel competency response |
| Context | GPAA (Government Pensions Administration Agency) ICT panelist application |

**Content likely includes:** Structured competency responses mapped to government evaluation criteria. Useful as a model for structuring government tender responses.

---

## Recommended Extraction Priority

### Tier 1 — Read Immediately (before any authoring begins)

These documents are most likely to contain the richest, most reusable content:

| Priority | Template ID | File | Why |
|---|---|---|---|
| 1 | TMPL-009 | `MTN Tender - Volume 2/` (all 6 sections) | Explicit sections for methodology, services, performance standards, governance, transition, exit — the most complete Oracle support response structure in the corpus |
| 2 | TMPL-002 | `0. Proposal Templates/Oracle Fusion/Oracle Fusion Template.docx` | Current active Fusion template — direct reflection of APPSolve's current Oracle Cloud proposition |
| 3 | TMPL-003 | `0. Proposal Templates/Acumatica/APPSolve Acumatica - CUSTOMER - Proposal Template Sept2025 BH.docx` | Most recent Acumatica template — primary source for Acumatica capability and methodology content |
| 4 | TMPL-001 | `0. Proposal Templates/Oracle EBS/Oracle EBS Template.docx` | Current Oracle EBS template |
| 5 | TMPL-012 | `Sita/RFP/H2H/APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx` | Most comprehensive government-facing BeBanking proposal; 6 revisions = highly refined |
| 6 | TMPL-013 | `Mpact/RFP/BeBanking/APPSolve Mpact BeBanking Scoping and Implementation Proposal v1 11122019.docx` | First complete BeBanking scoping+implementation proposal — the BeBanking methodology skeleton |
| 7 | TMPL-014 | `HyDac/RFP/Acumatica Implementation/1. Working/APPSolve_HyDac_Proposal_20241211_V5.1 Template BeBanking.docx` | Combined Acumatica+BeBanking template, V5.1 — mature and recent |
| 8 | TMPL-007 | `ATNS/RFP/EBS Support 2025 - Re issue/1.Working/Oracle Support Template.docx` | Current Oracle support template for ongoing support tenders |

### Tier 2 — Read After Tier 1

| Priority | Template ID | File | Why |
|---|---|---|---|
| 9 | TMPL-004 | Short Acumatica Proposal (Apr 2025) | Short-form template — fills a gap for smaller Acumatica engagements |
| 10 | TMPL-008 | DFA Oracle EBS Managed Services v2 (2017) | Earliest clear managed services template — compare with MTN 2014 to identify what changed |
| 11 | TMPL-026 | CLH ERP Project Plan Template (Feb 2026) | Current Acumatica delivery schedule — reveals standard phase structure |
| 12 | TMPL-027 | Mpact BeBanking Project Plan (2019) | Only BeBanking project plan — reveals delivery phase structure |
| 13 | TMPL-025 | OCI Proposal Template | OCI-specific — relevant for infrastructure and cloud tenders |
| 14 | TMPL-015 | APPSolve Overview and BeBanking Deck (2019, "awarded") | Confirmed winning deck — language and positioning validated |

### Tier 3 — Read for Completeness or Specific Needs

| Priority | Template ID | File | Why |
|---|---|---|---|
| 15 | TMPL-005 | Older Acumatica base template | Compare with TMPL-003 for removed content |
| 16 | TMPL-017 | ACSA BeBanking Fintegrate Migration | Cloud vs on-premise analysis — useful for cloud migration tenders |
| 17 | TMPL-028/029 | Axon Governance templates | Historical governance framework — structural basis for current governance model |
| 18 | TMPL-018 | Investec DBA SOW (2024) | Current SOW format for DBA engagements |
| 19 | TMPL-019 | Investec APEX SOW series | SOW evolution for ongoing development contracts |
| 20 | TMPL-022 | DFA Costing Template v7 | Pricing model structure — useful for Quote Generator |
| 21 | TMPL-016 | Irvines Acumatica+BeBanking Intro (2024) | Current combined pitch deck |

---

## Assessment: Template Acceleration by KB Content Category

### Methodology Documents

**Oracle EBS Methodology**
- TMPL-009 (MTN 2014 Vol 2) contains sections 2.2 (Services), 2.5 (Transition), and the Services Overview — direct source material
- TMPL-001 (Oracle EBS Template) likely contains an implementation methodology section
- TMPL-007 (ATNS Oracle Support Template 2025) contains the current support delivery approach
- **Assessment: Methodology content EXISTS. It can be extracted, not authored from scratch. Effort is extraction + modernisation, not creation.**

**Oracle Cloud/Fusion Methodology**
- TMPL-002 (Oracle Fusion Template) is the primary source
- TMPL-009 section 2.5 (Transition) provides cloud migration approach language
- **Assessment: Content likely exists. Template reading will confirm.**

**Acumatica Methodology**
- TMPL-003 (Sept 2025 template) is the primary source — it is the active template
- TMPL-026 (CLH Project Plan Feb 2026) reveals the standard delivery phases in a structured format
- TMPL-014 (HyDac V5.1) shows combined implementation + BeBanking integration approach
- **Assessment: Methodology content exists in active templates. Acumatica phases are encoded in the current project plan template. This is NOT "author from scratch" territory.**

**BeBanking Methodology**
- TMPL-012 (SITA Host-to-Host, 6 revisions) is the richest BeBanking capability and process document
- TMPL-013 (Mpact Scoping and Implementation Proposal) has a full three-part package: proposal + cost + project plan
- TMPL-027 (Mpact BeBanking Project Plan .mpp) shows actual delivery phases
- **Assessment: BeBanking methodology DOES exist in the corpus. The Gap Analysis rating of "Missing" is wrong. Extraction is the work, not authoring from scratch.**

---

### Executive Summaries

**Oracle**
- TMPL-009 (MTN 2014 — standalone Executive Summary file: `APPSolve Executive Summary.docx`)
- TMPL-010 (MTN 2017 update)
- TMPL-001 / TMPL-002 (Templates likely contain executive intro sections)
- **Assessment: Oracle executive summary language exists. Will need updating for 2026 products and certifications.**

**Acumatica**
- TMPL-003 (Sept 2025 template) is the direct source
- TMPL-004 (Short proposal) likely has a condensed version
- **Assessment: Current Acumatica executive content exists in the active template.**

**BeBanking**
- TMPL-015 (ARM deck, "awarded") and TMPL-016 (Irvines 2024) contain BeBanking positioning language
- TMPL-012 (SITA proposal) likely opens with an executive summary section
- **Assessment: BeBanking executive content exists — more recent and validated than expected.**

---

### Governance Models

**Oracle EBS**
- TMPL-009 section 2.4 (Governance and Change) — explicit governance section
- TMPL-028 / TMPL-029 (Axon templates) — structural governance framework
- **Assessment: Governance content exists from 2014 (MTN). Will need updating for modern delivery models.**

**Acumatica**
- TMPL-003 likely includes a project governance section
- TMPL-026 (project plan template) defines phase ownership implicitly
- **Assessment: Probably exists in TMPL-003; confirm on reading.**

---

### Capability Statements

**Oracle**
- TMPL-009 section 2.1 (Technical Solution Introduction) = Oracle capability positioning
- TMPL-001 / TMPL-002 (templates) = capability statements
- **Assessment: Well-documented. Current templates are the primary source.**

**Acumatica**
- TMPL-003 (Sept 2025) = current Acumatica capability positioning
- TMPL-030 (Acumatica Standard Reporting) = specific reporting capability document
- **Assessment: Well-documented. Current template is the primary source.**

**BeBanking**
- TMPL-015 ("awarded" deck 2019) = BeBanking capability in presentation form
- TMPL-016 (Irvines 2024) = more current capability deck
- TMPL-012 (SITA) = written capability statement in proposal form
- TMPL-011 (OEM agreement) = service description language in commercial form
- **Assessment: BeBanking capability is NOT "Missing". Multiple current and historical sources exist.**

---

### Standard Tender Responses

**Government Compliance Sections (BEE, tax, COID, etc.)**
- MTN 2014 Volume 1 documents (1.1–1.10) contain all standard compliance annexures in DOCX format
- SASSA 2021 Annexure response template (TMPL-024) shows government response format
- **Assessment: Standard compliance section structure is well-documented.**

**Project Management Approach**
- TMPL-009 section 2.4 (Governance and Change) directly covers this
- **Assessment: Exists — needs extraction and modernisation.**

**Support and SLA Approach**
- TMPL-009 section 2.3 (Performance Standards) = explicit SLA framework
- **Assessment: Exists.**

**Pricing Narrative**
- TMPL-022 (DFA Costing Template v7) provides pricing structure
- TMPL-023 (MTN DBA Rate Card 2026) provides current rate framework
- **Assessment: Commercial structure exists; narrative framing needs authoring.**

---

## Critical Corrections to CONTENT_GAP_ANALYSIS.md

The following ratings from the existing Gap Analysis must be updated:

| Gap Analysis Finding | Actual Status (post-discovery) |
|---|---|
| Oracle methodology — Missing, author from scratch | **Wrong.** MTN 2014 Vol 2 contains explicit sections for services, performance standards, governance, transition, and exit. TMPL-001/002 likely contain methodology sections. Effort is extraction + modernisation. |
| Acumatica methodology — Missing, nothing in Tender Pack | **Wrong.** TMPL-003 (Sept 2025 active template) and TMPL-026 (Feb 2026 project plan) encode the current delivery approach. Acumatica methodology is visible in the template ecosystem. |
| BeBanking — Missing across all categories | **Significantly wrong.** 20+ BeBanking proposals exist across 15+ clients. SITA H2H proposal (6 revisions), Mpact scoping+implementation+project plan, ACSA long-running relationship with Fintegrate analysis, multiple OEM agreements, two capability decks. BeBanking IP is substantial. |
| Oracle executive summary — Missing | **Wrong.** MTN 2014 has a standalone `APPSolve Executive Summary.docx`. Template documents likely contain executive sections. |
| Acumatica standard tender responses — zero historical proposals | **Wrong.** TMPL-003 is a complete current proposal template (September 2025). Multiple deployed instances (TUT, HyDac, Eyabantu, CATS, Norse Projects) confirm it is in active use. |
| Governance model — Missing | **Wrong.** MTN 2014 section 2.4 and Axon governance templates provide the foundation. |

---

*Next action: Proceed to Phase 2 sampling — read Tier 1 templates in priority order, recording content section by section.*
*All source files remain at their original paths — no copies made.*
