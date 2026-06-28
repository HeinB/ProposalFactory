# Extraction Plan — Priority Template Sources
**Date:** 2026-06-08
**Status:** Planning only — no files copied, no content authored, no source files modified
**Based on:** `MASTER_TEMPLATE_REGISTER.md` discovery findings
**Governed by:** `AI_CONTEXT.md` — no invented content, no unverified claims

---

## How to Use This Plan

This document defines what to extract, from where, to where, and how. It does not authorise extraction to begin. Each extraction requires:

1. The source document to be **read in full** by a named reviewer
2. Client-specific content to be **identified and marked** for removal
3. The extracted text to be **edited** to remove client names, specific pricing, and outdated claims
4. A named person to **approve** the extracted content before it enters any KB folder
5. The DOCUMENT_REGISTER.csv row for the source to be updated with `approved_for_reuse = Yes`

**Three readiness ratings are used throughout:**
- `DIRECT` — content can be used with minor date/name updates only (verified factual, current)
- `MODERNISE` — content is structurally sound but needs updating (outdated tech references, old company stats, expired certifications)
- `STRUCTURE ONLY` — the document provides a framework to write against; the actual text is too client-specific or outdated to reuse verbatim

---

## Source 1: MTN 2014 Volume 2 — Oracle EBS DBA Managed Services

**Source documents:**
```
Parties/Customers/MTN/RFP/Archive/ZZ Archive/RFP 20140718 close 20140801/
  Old Tender/MTN Tender/APPSolve Tender - Volume 2/
    APPSolve Executive Summary.docx
    APPSolve Proposal 2.1 - Technical Solution Introduction.docx
    APPSolve Proposal 2.2 - Services.docx
    APPSolve Proposal 2.3  - Performance Standards.docx
    APPSolve Proposal 2.4 - Governance and Change.doc
    APPSolve Proposal 2.5 - Transition.docx
    APPSolve Proposal 2.6 - Exit.doc
```
**Date:** August 2014 | **BU:** Oracle | **Outcome:** Won (MTN awarded)

**Important context:** Sections 2.2, 2.3, 2.5 are structured as formal compliance matrices in MTN's prescribed format — APPSolve's responses are embedded within client-defined tables. The IP is in APPSolve's written responses, not the matrix structure itself. Sections 2.4 and 2.6 are `.doc` format and require reading directly.

---

### Extraction 1.A — Oracle DBA Managed Services Executive Summary

| Field | Value |
|---|---|
| Source file | `APPSolve Executive Summary.docx` |
| Section | Full document |
| Content type | Executive Summary |
| Business unit | Oracle |
| Service area | Oracle DBA / Managed Services |
| Readiness | `MODERNISE` |
| Target folder | `09_Executive_Summaries/Oracle/` (once created) |
| Target filename | `EXE-ORA-DBA-Managed-Services-Draft.md` |

**What to extract:** The entire Executive Summary document. This is a standalone 1–2 page document summarising APPSolve's Oracle DBA managed services proposition for a large enterprise client.

**What to remove before use:**
- All MTN-specific references (client name, contract reference RFP-SA/I/09/2012)
- 2014 company statistics (staff numbers, years of experience)
- Specific pricing references

**What to update:**
- Company size (2014 → 2026 figures)
- Oracle partner certifications (Gold → confirm current status)
- Product version references (EBS 12.1.x → current supported versions)

**Review notes:** The executive summary was written for a won engagement — the positioning and value proposition were validated by a real client decision. High confidence in structural quality.

---

### Extraction 1.B — Oracle DBA Technical Solution (Methodology)

| Field | Value |
|---|---|
| Source file | `APPSolve Proposal 2.1 - Technical Solution Introduction.docx` |
| Sections | Supplier's Technical Solution → Architectural, Strategy, System Architecture, Support & Professional Services, Services Model, Data Protection |
| Content type | Methodology |
| Business unit | Oracle |
| Service area | Oracle DBA / Infrastructure |
| Readiness | `MODERNISE` |
| Target folder | `08_Methodologies/Oracle/DBA_Support/` |
| Target filename | `METH-ORA-DBA-Technical-Solution-Draft.md` |

**What to extract:**
- Architectural approach to DBA managed services
- Strategy section (operational philosophy)
- System Architecture, Integration and Management approach
- Support & Professional Services model description
- Services Model (how service is structured and delivered)
- Data Protection Techniques

**What to skip (client/MTN-specific):**
- The "MTN Database Scenario" section (client environment description)
- ITAB section (MTN-specific governance body)
- Migration section (specific to MTN's migration context)
- Pre-requisites section (MTN infrastructure specifics)

**What to update:**
- On-premises DBA architecture → add cloud/OCI context
- Virtualisation references (2014 technology landscape)
- Security / compliance references → add POPIA, ISO 27001 context

**Review notes:** The technical solution is 12 years old. The principles (access control, architecture, support model, data protection) are enduring; the technology specifics (specific Oracle versions, virtualisation platforms) need modernising. Do not treat as current without review.

---

### Extraction 1.C — Oracle SLA / Support Model Framework

| Field | Value |
|---|---|
| Source file | `APPSolve Proposal 2.3 - Performance Standards.docx` |
| Sections | Service Level Performance (Measurement, Failure to Perform), Definitions |
| Content type | Support Model |
| Business unit | Oracle |
| Service area | Oracle EBS / DBA Managed Services |
| Readiness | `STRUCTURE ONLY` |
| Target folder | `08_Methodologies/Oracle/Support_Model/` |
| Target filename | `METH-ORA-SLA-Framework-Draft.md` |

**What to extract (structure only):**
- SLA measurement and monitoring approach
- Service Level Default definition and response obligations
- Root cause analysis obligation
- Preventive measure obligations

**What to skip entirely:**
- All liquidated damages clauses and amounts (MTN-specific, commercially sensitive)
- All MTN-defined measurement periods
- The compliance matrix format itself

**What to write fresh based on this structure:**
- APPSolve's standard SLA tiers (response times by severity)
- Standard measurement and reporting cadence
- Standard remediation obligations

**Review notes:** Sections 2.2 (Services) and 2.3 (Performance Standards) are written in MTN's compliance matrix format. Do not extract the matrix — extract the concepts and write a clean APPSolve-owned version of each obligation.

---

### Extraction 1.D — Governance and Change Model

| Field | Value |
|---|---|
| Source file | `APPSolve Proposal 2.4 - Governance and Change.doc` |
| Sections | Full document (must read first — `.doc` format, headings not yet extracted) |
| Content type | Governance Model |
| Business unit | Oracle |
| Service area | Oracle EBS / DBA Managed Services |
| Readiness | `MODERNISE` (assumed — confirm on reading) |
| Target folder | `08_Methodologies/Oracle/Governance/` |
| Target filename | `METH-ORA-Governance-Draft.md` |

**What to extract (expected based on document title):**
- Governance structure (steering committees, project boards, RACI)
- Change management procedure
- Escalation framework

**Review action required:** This is a `.doc` file. It must be opened and read before extraction can be planned in detail. Open and document its section structure before proceeding.

---

### Extraction 1.E — Transition Methodology

| Field | Value |
|---|---|
| Source file | `APPSolve Proposal 2.5 - Transition.docx` |
| Sections | Transition section → General, Transition Plan and Handover, Failure to Perform |
| Content type | Methodology (Transition) |
| Business unit | Oracle |
| Service area | Oracle EBS / DBA Managed Services |
| Readiness | `STRUCTURE ONLY` |
| Target folder | `08_Methodologies/Oracle/Transition/` |
| Target filename | `METH-ORA-Transition-Framework-Draft.md` |

**What to extract (process structure only):**
- Definition of transition activities (transfer of service responsibility)
- Transition Plan and Handover process
- Acceptance criteria concept
- "Ready to commence" confirmation criteria

**What to skip entirely:**
- All liquidated damages and legal obligations (MTN-specific)
- Specific timelines (MTN-defined)

**Review notes:** The transition document is heavily formatted in MTN's legal style. The process concept (plan, handover, acceptance) is reusable; the legal wrapping is not.

---

### Extraction 1.F — Exit Procedure

| Field | Value |
|---|---|
| Source file | `APPSolve Proposal 2.6 - Exit.doc` |
| Sections | Full document (must read first — `.doc` format) |
| Content type | Standard Response (Exit) |
| Business unit | Oracle |
| Service area | Oracle EBS / DBA Managed Services |
| Readiness | `STRUCTURE ONLY` (assumed) |
| Target folder | `07_Approved_Content/Oracle/Standard_Responses/` |
| Target filename | `STD-ORA-Exit-Procedure-Draft.md` |

**Review action required:** `.doc` file — open and read before planning extraction.

---

## Source 2: Oracle Fusion Template (Primary Template)

**Source document:**
```
Parties/Customers/0. Proposal Templates/Oracle Fusion/Oracle Fusion Template.docx
```
**Date:** September 2024 | **BU:** Oracle | **Format:** Editable DOCX master template

**Confirmed structure:** Executive Summary · Scope · Oracle Fusion Information (Overview + component table) · Response criteria · Company profile (Who is APPSolve · Contacts · Company History · Products and Services · Benefits) · Assumptions · Conclusion

---

### Extraction 2.A — Oracle Fusion / Cloud Capability Statement

| Field | Value |
|---|---|
| Source file | `Oracle Fusion Template.docx` |
| Sections | "Oracle Fusion Information" → Oracle Fusion Overview + component table |
| Content type | Capability Statement |
| Business unit | Oracle |
| Service area | Oracle Cloud / Fusion |
| Readiness | `MODERNISE` |
| Target folder | `06_Capabilities/Oracle/Oracle_Cloud/` |
| Target filename | `CAP-ORA-Cloud-Fusion-Overview-Draft.md` |

**What to extract:**
- Oracle Fusion platform description (7 key features: modular architecture, cloud-native, integration, advanced analytics, user experience, global capabilities, security)
- Core component table (Financials, HCM, SCM, CRM, Governance/Risk/Compliance)

**What to update:**
- Verify all product feature claims are current for Oracle Fusion 2025/2026
- Add APPSolve-specific delivery credentials (confirmed won deals, not invented)
- Add Oracle partner status (confirmed)

**Review notes:** The product description reads as accurate for current Oracle Fusion. The table of core components is a strong starting point for a capability statement. Avoid presenting Oracle's product description as APPSolve's own capability — layer in APPSolve's experience claims separately.

---

### Extraction 2.B — APPSolve Company Profile (Reusable Across BUs)

| Field | Value |
|---|---|
| Source file | `Oracle Fusion Template.docx` |
| Sections | "Company profile" → Who is APPSolve · Company History · Products and Services · Benefits of Working with APPSolve |
| Content type | Capability Statement (Corporate) |
| Business unit | Cross-BU |
| Service area | Corporate |
| Readiness | `MODERNISE` |
| Target folder | `06_Capabilities/Corporate/` or `07_Approved_Content/Cross_BU/` |
| Target filename | `CAP-CORP-Company-Profile-Draft.md` |

**What to extract:**
- "Who is APPSolve?" opening paragraph
- Company History narrative (founded 2002, sub-Saharan expansion, award history)
- Products and Services list (Professional Advisory, Projects, Customer Development, Managed Services, Business Development, Functional Services, Technical Services)
- "Benefits of Working with APPSolve" (trusted partner focus, senior resources, flexible billing, customer retention narrative)

**What to update:**
- "22 years" → "24 years" (as of 2026)
- "110 Senior Consultants" → verify current headcount
- Awards (Oracle Innovation Sustainability 2015/2016, SaaS Partner of the Year 2016/2019) → confirm most recent awards
- Contact details for Hein, Andre, Jeanette → verify current roles and correct any changes
- Sub-Saharan and international markets → update with current active geographies

**Review notes:** This is the same company profile section appearing in all three primary templates (Oracle Fusion, Oracle EBS, Acumatica). One clean version should be authored and cross-referenced into all proposals — do not maintain three separate versions. The "Hein established APPSolve in 2002" biographical note contains personal information; confirm it is approved for tender use.

**Used in:** Oracle Fusion Template, Oracle EBS Template, Acumatica Sept 2025 Template, HyDac V5.1 — consolidate into one approved master.

---

## Source 3: Acumatica Proposal Template — September 2025

**Source document:**
```
Parties/Customers/0. Proposal Templates/Acumatica/
  APPSolve Acumatica - CUSTOMER - Proposal Template Sept2025 BH.docx
```
**Date:** September 2025 | **BU:** Acumatica | **Deployed for:** HearX Group (active engagement)

**Confirmed structure:** Executive Summary · Scope · Acumatica Information (12 module sections including Host-to-Host Banking) · Company profile · Project And Implementation Methodology → Overview of Phases · High-Level Project Plan & Costing (License + Implementation) · Assumptions (11 categories) · Conclusion

---

### Extraction 3.A — Acumatica Module Capability Descriptions

| Field | Value |
|---|---|
| Source file | `APPSolve Acumatica - CUSTOMER - Proposal Template Sept2025 BH.docx` |
| Sections | "Acumatica Information" → all 12 module subsections |
| Content type | Capability Statement |
| Business unit | Acumatica |
| Service area | Acumatica ERP — modules |
| Readiness | `DIRECT` |
| Target folder | `06_Capabilities/Acumatica/` |
| Target filename | `CAP-ACU-Module-Library-Draft.md` |

**Module sections to extract individually:**
| Module | Target sub-file |
|---|---|
| Acumatica Overview | `CAP-ACU-Platform-Overview.md` |
| Distribution Edition | `CAP-ACU-Distribution.md` |
| Financials | `CAP-ACU-Financials.md` |
| Monitoring and Automation | `CAP-ACU-Monitoring-Automation.md` |
| Inventory Control | `CAP-ACU-Inventory.md` |
| Order Management | `CAP-ACU-Order-Management.md` |
| Multifactor Authentication | `CAP-ACU-Security-MFA.md` |
| AI Insights and Anomaly Detection | `CAP-ACU-AI-Insights.md` |
| Shopify Commerce Connector | `CAP-ACU-Shopify-Connector.md` |
| Deferred Revenue | `CAP-ACU-Deferred-Revenue.md` |
| Fixed Assets | `CAP-ACU-Fixed-Assets.md` |
| Host-to-Host Banking | → Extract to BeBanking capability folder (see 3.F) |

**Review notes:** These descriptions are Acumatica product marketing content adapted for APPSolve's proposals. They are factually accurate for the current product version but should be verified against current Acumatica release notes for any deprecated features. The "Host-to-Host Banking" module section is the BeBanking integration section — route to BeBanking capability folder.

---

### Extraction 3.B — Acumatica Manufacturing Capabilities (from HyDac V5.1)

*Cross-reference: HyDac V5.1 (Source 7) adds manufacturing-specific modules not in the Sept 2025 template. Both should be read and merged.*

| Additional modules (HyDac only) | Target |
|---|---|
| Prime Manufacturing Edition overview | `CAP-ACU-Manufacturing-Edition.md` |
| Manufacturing Foundation | `CAP-ACU-Manufacturing-Foundation.md` |
| Discrete Manufacturing | `CAP-ACU-Discrete-Manufacturing.md` |
| MRP | `CAP-ACU-MRP.md` |
| Estimating | `CAP-ACU-Estimating.md` |
| Engineering Change Control | `CAP-ACU-ECC.md` |
| CRM | `CAP-ACU-CRM.md` |

---

### Extraction 3.C — Acumatica Implementation Methodology

| Field | Value |
|---|---|
| Source file | `APPSolve Acumatica - CUSTOMER - Proposal Template Sept2025 BH.docx` |
| Sections | "Project And Implementation Methodology" → "Overview of Phases" |
| Content type | Methodology |
| Business unit | Acumatica |
| Service area | Acumatica ERP Implementation |
| Readiness | `MODERNISE` |
| Target folder | `08_Methodologies/Acumatica/` |
| Target filename | `METH-ACU-Implementation-Methodology-Draft.md` |

**What to extract:**
- Overview of delivery phases
- Phase objectives and sequencing

**What to supplement from other sources:**
- Mpact BeBanking proposal Section: "Project and Implementation Methodology Summary" + "Project Management Approach" + "Implementation Methodology" subsections (Issue Management, Change Control) — these provide the detail that may be missing from the template's Overview section
- CLH ERP Project Plan Template (XLSX, Feb 2026) — provides the actual task breakdown within each phase

**Review notes:** The methodology section in the Sept 2025 template may be a brief overview only. Cross-reference with Mpact (Source 6) for the detailed process content. The CLH project plan gives the task-level structure.

---

### Extraction 3.D — Acumatica Pricing and Costing Assumptions

| Field | Value |
|---|---|
| Source file | `APPSolve Acumatica - CUSTOMER - Proposal Template Sept2025 BH.docx` |
| Sections | "High-Level Project Plan & Costing" structure · "Assumptions" (all 11 subsections) |
| Content type | Pricing Assumptions |
| Business unit | Acumatica |
| Service area | Acumatica ERP |
| Readiness | `MODERNISE` |
| Target folder | `13_Quote_Generator/Assumptions_Exclusions/` |
| Target filename | `ASSUM-ACU-Implementation-Standard.md` |

**Assumption categories to extract (generic ones only):**
- General IT Assumptions
- Project Management Assumptions
- Human Assumptions
- The Costing Notes
- The Costing Assumptions

**Skip (client-specific to HearX):**
- US Tax Assumption (US-specific)
- Group Structure Assumptions (HearX 6-entity structure)
- Order to Cash Assumptions (HearX-specific order types)
- Warehouse Management Assumptions (HearX-specific)
- Shopify Commerce Connector assumptions

**Review notes:** The 11 assumption categories show the full scope of what APPSolve typically needs to clarify before pricing an Acumatica implementation. Even the HearX-specific ones provide a template of what questions to ask for other clients — they can be retained as question prompts even if the specific answers are removed.

---

## Source 4: Oracle EBS Template (Primary Template)

**Source document:**
```
Parties/Customers/0. Proposal Templates/Oracle EBS/Oracle EBS Template.docx
```
**Date:** Unknown (pre-dates Sept 2024 Fusion template — same structure, EBS variant) | **BU:** Oracle

**Confirmed structure:** Executive Summary · Scope · Oracle EBS Information → Oracle EBS Overview · Response criteria · Company profile (identical to Fusion template) · Assumptions · Conclusion

---

### Extraction 4.A — Oracle EBS Capability Statement

| Field | Value |
|---|---|
| Source file | `Oracle EBS Template.docx` |
| Sections | "Oracle EBS Information" → Oracle EBS Overview |
| Content type | Capability Statement |
| Business unit | Oracle |
| Service area | Oracle EBS |
| Readiness | `MODERNISE` |
| Target folder | `06_Capabilities/Oracle/Oracle_EBS/` |
| Target filename | `CAP-ORA-EBS-Overview-Draft.md` |

**What to extract:**
- Oracle EBS platform overview and module descriptions
- APPSolve's EBS delivery focus areas (as described in the template)

**What to update:**
- EBS version references — verify current supported versions (R12.2.x)
- Confirm EBS product lifecycle positioning (EBS Premier Support, Sustaining Support timeline)
- Add APPSolve EBS project history highlights (module coverage confirmed by references)

**Review notes:** Compare with Oracle Fusion template — the Company profile section is identical. Use the single merged version from Extraction 2.B. Extract EBS-specific product content only from this source.

---

### Extraction 4.B — Oracle EBS Executive Summary Shell

| Field | Value |
|---|---|
| Source file | `Oracle EBS Template.docx` |
| Sections | "Executive Summary" (placeholder structure) |
| Content type | Executive Summary |
| Business unit | Oracle |
| Service area | Oracle EBS |
| Readiness | `STRUCTURE ONLY` |
| Target folder | `09_Executive_Summaries/Oracle/` |
| Target filename | `EXE-ORA-EBS-Shell.md` |

**Note:** The Executive Summary in the Oracle EBS template is likely a placeholder or generic shell. The MTN 2014 Executive Summary (Extraction 1.A) provides richer content for an EBS-specific executive summary. Use EBS Template for structure, MTN 2014 for content.

---

## Source 5: SITA BeBanking Proposal — Host-to-Host (v1 06)

**Source document:**
```
Parties/Customers/Sita/RFP/H2H/APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx
```
**Date:** Unknown (v1 06 = 6th revision, government engagement) | **BU:** BeBanking | **Client:** SITA (SA Government ICT Agency)

**Confirmed structure:** Executive Summary (6 subsections) · Proposed Engagement · Cost Proposal and Assumptions (Option 1 + Option 2) · Conclusion · Appendices (Product Module Summary · Host to Host Process Flow · Proposal Acceptance)

---

### Extraction 5.A — BeBanking Support Model ("Hybrid Support Model")

| Field | Value |
|---|---|
| Source file | `APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx` |
| Sections | Executive Summary → "Our Hybrid Support Model" |
| Content type | Support Model |
| Business unit | BeBanking |
| Service area | BeBanking Managed Support |
| Readiness | `MODERNISE` |
| Target folder | `08_Methodologies/BeBanking/` |
| Target filename | `METH-BB-Hybrid-Support-Model-Draft.md` |

**What to extract:** APPSolve's BeBanking hybrid support model description — what "hybrid" means in the BeBanking context (likely on-site + remote combination).

---

### Extraction 5.B — BeBanking Capability Statement (Executive Summary)

| Field | Value |
|---|---|
| Source file | `APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx` |
| Sections | Executive Summary → "Our team of technical expertise and track record" + "Service Delivery Management Team" + "Continuous Improvement Model" + "Flexible and Predictable Costing Model" |
| Content type | Capability Statement |
| Business unit | BeBanking |
| Service area | BeBanking H2H / Managed Services |
| Readiness | `MODERNISE` |
| Target folder | `06_Capabilities/BeBanking/` |
| Target filename | `CAP-BB-Service-Delivery-Capability-Draft.md` |

**What to extract:** All four Executive Summary subsections describing APPSolve's delivery capability in the BeBanking context.

**What to remove:** All SITA-specific references, any pricing or commercial figures.

---

### Extraction 5.C — BeBanking Proposed Engagement / Implementation Scope

| Field | Value |
|---|---|
| Source file | `APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx` |
| Sections | "Proposed Engagement" |
| Content type | Methodology |
| Business unit | BeBanking |
| Service area | BeBanking H2H Implementation |
| Readiness | `MODERNISE` |
| Target folder | `08_Methodologies/BeBanking/` |
| Target filename | `METH-BB-H2H-Engagement-Approach-Draft.md` |

**What to extract:** Description of how APPSolve engages for a Host-to-Host BeBanking implementation — scope, phases, deliverables.

---

### Extraction 5.D — BeBanking Product Module Summary (Appendix)

| Field | Value |
|---|---|
| Source file | `APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx` |
| Sections | Appendices → "Product Module Summary" |
| Content type | Capability Statement |
| Business unit | BeBanking |
| Service area | BeBanking Platform |
| Readiness | `MODERNISE` |
| Target folder | `06_Capabilities/BeBanking/` |
| Target filename | `CAP-BB-Product-Module-Summary-Draft.md` |

**What to extract:** BeBanking module/feature catalog — list of what the product does.

---

### Extraction 5.E — Host-to-Host Process Flow (Appendix)

| Field | Value |
|---|---|
| Source file | `APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx` |
| Sections | Appendices → "Host to Host Process Flow" |
| Content type | Methodology |
| Business unit | BeBanking |
| Service area | BeBanking H2H |
| Readiness | `MODERNISE` |
| Target folder | `08_Methodologies/BeBanking/` |
| Target filename | `METH-BB-H2H-Process-Flow-Draft.md` |

**What to extract:** The Host-to-Host process flow diagram or description. This is potentially a diagram — if so, it cannot be extracted as text and must be re-created as a Markdown table or Mermaid diagram.

**Review notes:** If this is an embedded diagram (Visio, PowerPoint shape, or image), note the source location and assign a human to re-draw it in KB format. Do not leave it as an embedded image in an extracted document.

---

### Extraction 5.F — BeBanking Pricing Options (Structure Only)

| Field | Value |
|---|---|
| Source file | `APPSolve SITA Host-to-Host BEBanking Proposal v1 06.docx` |
| Sections | "Cost Proposal and Assumptions" → Option 1 and Option 2 |
| Content type | Pricing Assumptions |
| Business unit | BeBanking |
| Service area | BeBanking |
| Readiness | `STRUCTURE ONLY` |
| Target folder | `13_Quote_Generator/Assumptions_Exclusions/` |
| Target filename | `ASSUM-BB-Pricing-Options-Structure.md` |

**What to extract:** The two pricing model types (Service Option vs Software Option) — the concept and what each covers, not the specific figures. This reveals APPSolve's commercial flexibility in positioning BeBanking.

---

## Source 6: Mpact BeBanking Scoping and Implementation Proposal (2019)

**Source document:**
```
Parties/Customers/Mpact/RFP/BeBanking/
  APPSolve Mpact BeBanking Scoping and Implementation Proposal v1 11122019.docx
  APPSolve Mpact BeBanking Scoping Project Plan v1 11122019.mpp
```
**Date:** December 2019 | **BU:** BeBanking | **Most important:** Full three-part package (proposal + cost estimate + project plan)

**Confirmed structure:** Executive Summary · Profile of APPSolve · References · Proposed Engagement (Scoping Phase + Implementation Phase with BeBanking Cloud Service) · Professional Services (Methodology Summary + PM Approach + Implementation Methodology) · High Level Project Plan · Costs and Assumptions

---

### Extraction 6.A — BeBanking Implementation Methodology (Core)

| Field | Value |
|---|---|
| Source file | `APPSolve Mpact BeBanking Scoping and Implementation Proposal v1 11122019.docx` |
| Sections | "Professional Services" → "Project and Implementation Methodology Summary" + "Project Management Approach" + "Implementation Methodology" (all three subsections) |
| Content type | Methodology |
| Business unit | BeBanking |
| Service area | BeBanking Implementation |
| Readiness | `MODERNISE` |
| Target folder | `08_Methodologies/BeBanking/` |
| Target filename | `METH-BB-Implementation-Methodology-Draft.md` |

**What to extract:**
- **Project and Implementation Methodology Summary** — the framing description of how APPSolve delivers BeBanking
- **Project Management Approach** — PM framework applied to BeBanking engagements
- **Implementation Methodology** → three subsections:
  - Project Infrastructure (team structure, tools, environment)
  - Issue Management Process (how issues are logged, escalated, resolved)
  - Change Control Process (how scope changes are managed)

**This is the most important BeBanking methodology extraction in the entire corpus.** All three subsections are APPSolve's own structured methodology, not client-prescribed format. The content is 7 years old and BeBanking Cloud has evolved (the "Trolley Vendor Solution" is probably deprecated), but the PM and issue/change management frameworks are enduring.

**What to update:**
- BeBanking Cloud Service description → verify current platform version
- Remove "Trolley Vendor Solution (E-Wallet)" references (likely a deprecated feature)
- Update project infrastructure tools if specific tools are named

---

### Extraction 6.B — BeBanking Delivery Phases

| Field | Value |
|---|---|
| Source file | `APPSolve Mpact BeBanking Scoping and Implementation Proposal v1 11122019.docx` |
| Sections | "Proposed Engagement" → Scoping Phase (Conceive and Design) + Implementation Phase (Validate, Transition and Realisation) |
| Content type | Methodology |
| Business unit | BeBanking |
| Service area | BeBanking Implementation |
| Readiness | `MODERNISE` |
| Target folder | `08_Methodologies/BeBanking/` |
| Target filename | `METH-BB-Delivery-Phases-Draft.md` |

**What to extract:** Phase descriptions including objectives and activities for each named phase. Phase naming (Conceive, Design, Validate, Transition, Realisation) matches industry-standard implementation methodology language.

---

### Extraction 6.C — BeBanking Executive Summary Pattern

| Field | Value |
|---|---|
| Source file | `APPSolve Mpact BeBanking Scoping and Implementation Proposal v1 11122019.docx` |
| Sections | "Executive Summary" |
| Content type | Executive Summary |
| Business unit | BeBanking |
| Service area | BeBanking |
| Readiness | `MODERNISE` |
| Target folder | `09_Executive_Summaries/BeBanking/` |
| Target filename | `EXE-BB-Scoping-Implementation-Draft.md` |

**What to remove:** All Mpact-specific references (company name, project scope details).

---

### Extraction 6.D — APPSolve Company Profile (BeBanking Version)

| Field | Value |
|---|---|
| Source file | `APPSolve Mpact BeBanking Scoping and Implementation Proposal v1 11122019.docx` |
| Sections | "PROFILE OF APPSolve" → Credentials + Company History + Benefits |
| Content type | Capability Statement (Corporate) |
| Business unit | Cross-BU |
| Service area | Corporate |
| Readiness | `MODERNISE` |
| Target folder | → Merge with Extraction 2.B (single corporate profile) |

**Note:** Compare with Oracle template version (Extraction 2.B). This version may contain different BeBanking-specific credential language. Merge the best elements into the single corporate profile document.

---

### Extraction 6.E — BeBanking Pricing Assumptions

| Field | Value |
|---|---|
| Source file | `APPSolve Mpact BeBanking Scoping and Implementation Proposal v1 11122019.docx` |
| Sections | "Costs and Assumptions" → General Assumptions + PM Assumptions + Human Assumptions + Costing Assumptions |
| Content type | Pricing Assumptions |
| Business unit | BeBanking |
| Service area | BeBanking |
| Readiness | `MODERNISE` |
| Target folder | `13_Quote_Generator/Assumptions_Exclusions/` |
| Target filename | `ASSUM-BB-Implementation-Standard.md` |

---

### Extraction 6.F — BeBanking Project Plan Structure (from .mpp)

| Field | Value |
|---|---|
| Source file | `APPSolve Mpact BeBanking Scoping Project Plan v1 11122019.mpp` |
| Sections | Full project plan |
| Content type | Project Plan |
| Business unit | BeBanking |
| Service area | BeBanking Implementation |
| Readiness | `STRUCTURE ONLY` |
| Target folder | `08_Methodologies/BeBanking/` or `13_Quote_Generator/` |
| Target filename | `PLAN-BB-Implementation-Phases-Draft.md` |

**Action:** Open in Microsoft Project. Export the WBS (task names, phases, durations) to CSV or copy task names into a structured Markdown table. Do not copy dates (project-specific). The phase and task structure is what is reusable.

---

## Source 7: HyDac Combined Acumatica + BeBanking Proposal — V5.1

**Source document:**
```
Parties/Customers/HyDac/RFP/Acumatica Implementation/1. Working/
  APPSolve_HyDac_Proposal_20241211_V5.1 Template BeBanking.docx
```
**Date:** December 2024 | **BU:** Acumatica + BeBanking | **Status:** V5.1 — extensively iterated

**Confirmed structure:** Executive Summary · Scope · Acumatica Information (15 modules including Manufacturing) · BeBanking – Host 2 Host Banking · Company profile · Project And Implementation Methodology → Overview of Phases · High-Level Project Plan & Costing · Assumptions · Conclusion

---

### Extraction 7.A — BeBanking Host-to-Host Section (Standalone)

| Field | Value |
|---|---|
| Source file | `APPSolve_HyDac_Proposal_20241211_V5.1 Template BeBanking.docx` |
| Sections | "BeBanking – Host 2 Host Banking" (full section) |
| Content type | Capability Statement |
| Business unit | BeBanking |
| Service area | BeBanking H2H |
| Readiness | `DIRECT` |
| Target folder | `06_Capabilities/BeBanking/` |
| Target filename | `CAP-BB-H2H-Capability-Statement-Draft.md` |

**What to extract:** The complete BeBanking H2H section — this is designed as a standalone insert within a combined proposal, making it the most ready-to-reuse BeBanking capability block in the corpus. Dated December 2024 — recent enough to be factually current.

**What to remove:** HyDac-specific references (company name, any client context).

**Review notes:** V5.1 implies this section has been refined over at least 5 iterations. High confidence in quality. Verify BeBanking product claims are still current before approving.

---

### Extraction 7.B — Acumatica Manufacturing Capability (additional modules)

| Field | Value |
|---|---|
| Source file | `APPSolve_HyDac_Proposal_20241211_V5.1 Template BeBanking.docx` |
| Sections | "Acumatica Information" → Manufacturing Foundation, Discrete Manufacturing, MRP, Estimating, Engineering Change Control sections |
| Content type | Capability Statement |
| Business unit | Acumatica |
| Service area | Acumatica Manufacturing |
| Readiness | `DIRECT` |
| Target folder | `06_Capabilities/Acumatica/Manufacturing/` |
| Target filename | See Extraction 3.B target files |

**Note:** Merge with Distribution/Financials modules from Source 3 (Acumatica Sept 2025) to build a complete Acumatica module library.

---

### Extraction 7.C — Combined Acumatica + BeBanking Executive Summary Pattern

| Field | Value |
|---|---|
| Source file | `APPSolve_HyDac_Proposal_20241211_V5.1 Template BeBanking.docx` |
| Sections | "Executive Summary" |
| Content type | Executive Summary |
| Business unit | Acumatica + BeBanking |
| Service area | Combined ERP + Banking Integration |
| Readiness | `MODERNISE` |
| Target folder | `09_Executive_Summaries/Acumatica/` |
| Target filename | `EXE-ACU-BB-Combined-Draft.md` |

**Review notes:** This is the only executive summary in the corpus for a combined Acumatica+BeBanking engagement. Highly valuable for clients who need both products. Remove HyDac references.

---

## Consolidated Extraction Map

### By KB Destination Folder

| Target Folder | Extractions | Primary Source |
|---|---|---|
| `06_Capabilities/Oracle/Oracle_Cloud/` | Oracle Fusion overview + component table | Source 2 |
| `06_Capabilities/Oracle/Oracle_EBS/` | Oracle EBS overview | Source 4 |
| `06_Capabilities/Corporate/` | Company profile (master) | Source 2 (merge 3, 6) |
| `06_Capabilities/Acumatica/` | Module library (15 modules) | Sources 3 + 7 |
| `06_Capabilities/Acumatica/Manufacturing/` | Manufacturing-specific modules | Source 7 |
| `06_Capabilities/BeBanking/` | H2H capability, service delivery, module summary | Sources 5 + 7 |
| `08_Methodologies/Oracle/DBA_Support/` | Technical solution, support model | Source 1 |
| `08_Methodologies/Oracle/Support_Model/` | SLA framework structure | Source 1 |
| `08_Methodologies/Oracle/Governance/` | Governance and change model | Source 1 |
| `08_Methodologies/Oracle/Transition/` | Transition methodology | Source 1 |
| `08_Methodologies/Acumatica/` | Implementation methodology + phases | Sources 3 + 6 |
| `08_Methodologies/BeBanking/` | Full BeBanking methodology (6 components) | Sources 5 + 6 |
| `09_Executive_Summaries/Oracle/` | Oracle DBA/EBS/Fusion exec summaries | Sources 1 + 2 + 4 |
| `09_Executive_Summaries/Acumatica/` | Acumatica and combined exec summaries | Sources 3 + 7 |
| `09_Executive_Summaries/BeBanking/` | BeBanking exec summaries | Sources 5 + 6 |
| `13_Quote_Generator/Assumptions_Exclusions/` | Pricing assumptions (3 BUs) | Sources 3 + 5 + 6 |

### By Readiness Rating

**DIRECT — Extract and use with minor name/date updates only (5 extractions):**
- Acumatica module capability descriptions × 12 modules (Source 3)
- Acumatica manufacturing modules × 5 (Source 7)
- BeBanking H2H capability statement (Source 7)
- Company profile (Oracle Fusion template, with date updates)

**MODERNISE — Extract and update before use (12 extractions):**
- Oracle DBA Executive Summary (Source 1)
- Oracle DBA Technical Solution (Source 1)
- Governance and Change Model (Source 1)
- Oracle Fusion capability overview (Source 2)
- Acumatica implementation methodology (Source 3)
- Acumatica pricing assumptions (Source 3)
- BeBanking Support Model (Source 5)
- BeBanking capability statement (Source 5)
- BeBanking engagement approach (Source 5)
- BeBanking product module summary (Source 5)
- BeBanking implementation methodology (Source 6)
- BeBanking delivery phases (Source 6)

**STRUCTURE ONLY — Use as framework; write fresh content against this structure (6 extractions):**
- Oracle SLA framework (Source 1 — extract concepts, write clean version)
- Transition methodology (Source 1 — extract process, remove legal terms)
- Exit procedure (Source 1 — read first, then assess)
- Oracle EBS executive summary shell (Source 4 — MTN 2014 provides better content)
- BeBanking H2H process flow (Source 5 — diagram must be re-created)
- BeBanking pricing options (Source 5 — concept only, not figures)

---

## Execution Sequence

The extractions above should be executed in this order to maximise early value:

**Wave 1 — Foundation content (Cross-BU, immediately reusable)**
1. Company Profile master (Extraction 2.B) — used in every tender, highest frequency
2. Acumatica module capability library (Extraction 3.A + 3.B) — DIRECT, fastest to complete
3. BeBanking H2H capability statement (Extraction 7.A) — DIRECT, fills critical gap

**Wave 2 — Methodology content (Oracle, high tender impact)**
4. Oracle DBA Executive Summary (Extraction 1.A)
5. Oracle DBA Technical Solution (Extraction 1.B)
6. Oracle Fusion capability overview (Extraction 2.A)
7. Oracle EBS capability overview (Extraction 4.A)

**Wave 3 — Methodology content (BeBanking, fills largest gap)**
8. BeBanking implementation methodology (Extraction 6.A) — highest BeBanking priority
9. BeBanking delivery phases (Extraction 6.B)
10. BeBanking capability (Extraction 5.B + 5.C + 5.D)

**Wave 4 — Methodology content (Oracle governance + support model)**
11. Governance and Change (Extraction 1.D) — requires reading .doc first
12. SLA framework (Extraction 1.C) — structure only, write fresh
13. Acumatica methodology (Extraction 3.C)

**Wave 5 — Pricing and assumptions (Quote Generator)**
14. Acumatica pricing assumptions (Extraction 3.D)
15. BeBanking pricing options (Extraction 5.F + 6.E)

---

## Review and Approval Workflow

Before any extracted content enters a KB folder with `approved_for_reuse = Yes`:

1. **Reviewer reads source** — confirms section content matches plan description
2. **Client references removed** — no client names, contract values, specific dates
3. **Outdated claims flagged** — technology versions, staff numbers, award history
4. **Factual claims verified** — certifications, partner status, team size confirmed current
5. **BU lead approval** — named person signs off per BU (Oracle, Acumatica, BeBanking)
6. **Register updated** — `approved_for_reuse = Yes`, `content_reviewed_by`, `content_reviewed_date`

Content in KB folders without this approval workflow must be marked `DRAFT — NOT APPROVED FOR TENDER USE` in the file header.

---

*Source files remain at their original paths. No files moved or modified.*
*This plan does not authorise extraction — it authorises planning for extraction.*
*Begin with Wave 1 after document register rows are added for all 7 sources.*
