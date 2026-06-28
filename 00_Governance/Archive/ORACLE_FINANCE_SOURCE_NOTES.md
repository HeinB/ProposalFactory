---
name: oracle-finance-source-notes
description: Source notes for Oracle Fusion Finance, ERP, Procurement, SCM coverage — Mpact and BankServAfrica proposals. Feeds W2S1-001 Sections 4–7.
metadata:
  type: project
  created: 2026-06-11
  created_by: AI (Claude Sonnet 4.6) — Wave 2 Session 1 (strengthening phase)
  feeds: W2S1-001-ORA-FusionCapability.md Sections 4, 5, 6, 7, 12
---

> These notes support the strengthening of Sections 4–7 in `W2S1-001-ORA-FusionCapability.md`.
> All prohibited wording identified below must not be extracted.
> All content marked **REUSABLE** has been extracted and applied to W2S1-001.

---

## Source 1: Mpact Oracle ERP Proposal

**Document name:** `Mpact_APPSolve Implementation Proposal of Oracle ERP.docx`
**File path:** `Parties/Customers/Mpact/RFP/ERP/2 Working/Mpact_APPSolve Implementation Proposal of Oracle ERP.docx`
**Date:** 14 August 2025
**Client / Tender context:** RFP-01 PLASTICS-2025 FMCG ERP — Mpact Plastics seeking to replace JDE World with Oracle Fusion Cloud. Full scope: ERP Financial Modules + SCM (Supply Chain, CX, Manufacturing) + EPM (Phase 2). Proposal not yet confirmed as won.
**Reference:** `/tmp/mpact_erp.txt` (989 lines)

---

### Oracle Products Covered

- Oracle Fusion Cloud ERP (Financial Modules)
- Oracle Fusion SCM (Supply Chain Modules)
- Oracle Fusion CX (Customer Experience Modules)
- Oracle Fusion EPM (Planning and Budgeting — Phase 2)
- BeBanking (Host-to-Host banking — APPSolve product)

---

### Finance / ERP Sections Found

**Scope confirmed (lines 50–54):**
- Customer Experience Modules
- Supply Chain Modules
- ERP Financial Modules
- EPM — Planning and Budgeting

**Module scope (per implementation commercials section):**
Oracle Fusion Modules Phase 1 (7 months) + EPM Phase 2 (9 months)

**Reports scoped (client-specific — do not reuse specific counts):**
- ERP Finance: 5 custom reports
- SCM Procurement: 3 custom reports
- SCM Order Management: 3 custom reports
- SCM Manufacturing: 2 custom reports
- CX CPQ: 2 custom reports

**Integration assumptions (client-specific — exclude from generic capability):**
- Hyperion integration
- Archivist (JDE data archiving tool)
- Payroll and HCM
- Standard Bank via BeBanking
- DWH: Qlik Sense data feeds from various Oracle Fusion modules

**Standard reports claim (REUSABLE):**
> "Oracle Fusion provides numerous standard reports that can be run as scheduled processes or OTBI reports. We have found that 95% of all customer reports requirements are met by the standard Oracle reports."
*Source: Mpact line 174*

---

### References Section — CRITICAL CORRECTIONS TO W2S1-001 CLIENT TABLE

The Mpact proposal references section (lines 470–643) contains the most detailed client reference cards found across all sources. All entries supersede prior assumptions from the RedPath Mining RFI client list.

| Client | Countries | Industry | Users | Implementation | Go-Live | Modules | Integrations | Reference Available |
|---|---|---|---|---|---|---|---|---|
| Nala Renewables | **South Africa, Lithuania, Romania, Finland** (4 countries) | Renewable Energy | 25 | 8 months | **April 2025** | Oracle Fusion Financials, Oracle Fusion ERP | Banking | **Yes** |
| Investec | **South Africa, United Kingdom, United States** (3 countries) | Banking | >1,000 | 13 months | **July 2024** | Oracle Fusion Financials, Oracle Fusion Procurement, iExpenses | Payroll, JDE GL, Banking, EBS HCM on-premise | **Yes** |
| Mr Price Group | South Africa | Retail | 2,300 | 18 months | **June 2023** | **Oracle HCM Learning Cloud** (NOT full HCM) | Oracle HCM ↔ 3rd party systems | **Yes** |
| Cape Union Mart | South Africa | Retail | 25 | 8 months | **February 2022** | **Oracle Fusion Financials, Oracle Fusion Procurement** (NOT SCM) | Bank Statement, Payment file, Trade Management, TM1 Reporting, Manufacturing | **Yes** |
| Hollywood Bets | South Africa | Online Gambling | **7,000** | **18 months** | **July 2025** | Oracle Fusion HCM, Oracle Fusion Help Desk, Oracle Fusion Recruiting Cloud, Oracle Fusion Talent Management | PaySpace and Moodle | **Yes** |
| Dark Fibre Africa (DFA) | South Africa | Telecom / Infrastructure | 20 | 14 months | **June 2019** | Oracle HCM Cloud, Learning Cloud, Goal & Performance, Taleo Recruiting, Oracle Payroll, **Oracle Financials Cloud**, **Oracle SCM Cloud**, Oracle Integration Cloud, **Oracle EPM** | All modules + Quickbase, BeBanking, Globill, Safety360, MSDynamics, EBS Payroll on-premises | **No — NOT available for reference** |

**Critical corrections this table drives in W2S1-001:**

1. **MATERIAL ERROR:** W2S1-001 Section 6 (SCM) cited Cape Union Mart as the sole SCM client. **Cape Union Mart is Financials + Procurement, NOT SCM.** Section 6 must be corrected.
2. **Nala country count wrong:** W2S1-001 Section 12 states "8 countries". Correct count is **4 countries** (SA, Lithuania, Romania, Finland).
3. **Mr Price scope narrower than assumed:** Mr Price implemented Oracle HCM Learning Cloud only — not "full HCM" as implied in prior notes.
4. **DFA is the only confirmed Oracle Fusion SCM client** — but DFA is NOT available for reference. Section 6 must be updated to reflect this.
5. **Hollywood Bets go-live confirmed:** July 2025, 7,000 users.
6. **Investec integrations** now detailed: Payroll, JDE GL, Banking, EBS HCM on-premise.

---

### Procurement Sections Found

None at module-description level — Mpact scope mentions "Supply Chain Modules" without module-level breakdown.

---

### SCM Sections Found

None at module-description level in Mpact proposal body. DFA is the only confirmed Fusion SCM reference client (from References section) but is not available for reference.

---

### Integration Sections Found

- BeBanking (Host-to-Host banking for ERP) — APPSolve proprietary product
- Qlik Sense DWH integration mentioned
- Archivist (JDE archival) — client-specific, do not extract

---

### Implementation Approach Notes

Mpact proposal uses the standard OUM-based implementation structure (Mobilize → Scoping → Prototype → Validate → Deploy → Evolve) — identical to BankServAfrica and PayInc proposals. This is standard APPSolve delivery methodology.

**Data Migration (REUSABLE — lines 218–222):**
> "APPSolve distinguishes data take-on between Master Data and Transactional Data. Master Data: APPSolve will provide take-on templates early in the project... For Prototype 1 and Prototype 2, we will test the loaded data, even if it is only a sample set. Transactional Data: APPSolve will also provide templates... We will conduct a requirements session to determine the scope, and agree on the inclusion of historical transactional data versus only open items, depending on the various modules and their dependencies."

**Support model (consistent with other sources):**
2 months hyper care → 12 months critical care → steady state. (Note: Hollywood Bets / BSA say 3 months hyper care. Range is 2–3 months depending on project.)

---

### Reusable Wording Candidates

| Candidate | Source Line | Use |
|---|---|---|
| "95% of all customer reports requirements are met by the standard Oracle reports" | 174 | Analytics / Reporting section |
| Data migration master/transactional distinction | 218–222 | Implementation approach (W2S1-005) |
| BeBanking description | 651–661 | BeBanking deliverable (separate) |

---

### Client-Specific Wording to Exclude

- All Mpact-specific references (JDE World replacement, Qlik Sense, Hyperion, Archivist, Standard Bank OneHub) — client context only
- Project commercials (costing, travel policy) — client-specific

---

### Prohibited Wording Found

| Prohibited | Location | Correct Replacement |
|---|---|---|
| "19 years' experience" (Hein) | Line 687 | ~30 years |
| "22 years" (company) | Line 712 | "over two decades" or "more than 23 years" |
| "Gold Level partnership" | Line 782 | "Level 1 Partner" |
| "110+ Senior Consultants" | Line 865 | 50+ |
| "APPSolve has the largest number of locally based Oracle Applications DBAs" | Line 788 | "one of the largest" |

---

## Source 2: BankServAfrica ERP Proposal

**Document name:** `BankServAfrica_APPSolve Implementation Proposal V1.docx`
**File path:** `Parties/Customers/Bankserv/RFP/ERP/1 Working/BankServAfrica_APPSolve Implementation Proposal V1.docx`
**Date:** 30 August 2024
**Client / Tender context:** RFP 08/2024 — Finance ERP System including Financial Planning and Analysis (FP&A) Tool. BankServAfrica (payment clearing infrastructure, South Africa) seeking full Oracle Fusion Finance ERP + EPM deployment. Submitted; outcome not confirmed in source.
**Reference:** `/tmp/bsa_erp.txt` (1395 lines)

---

### Oracle Products Covered

Phase 1: General Ledger, Tax, Accounts Payable, IDR (Intelligent Document Recognition), Expense Reports (Claims), Accounts Receivable, Cash Management, Fixed Assets, Purchasing, Inventory, Supplier Portal, OIC integration

Phase 2: Order Management, Project Costing and Billing, Time and Labour, Sourcing and Contracts, Maintenance

Phase 2 EPM: Planning and Budgeting, Costing and Profitability, ESG

---

### Finance / ERP Module Descriptions — PRIMARY SOURCED CONTENT

All sourced from BSA proposal lines 389–495 (Oracle Fusion ERP section). Content reproduced here for extraction reference.

**Oracle Fusion ERP Overview:**
> "Oracle Fusion Enterprise Resource Planning (ERP) is a core component of Oracle Fusion Applications, designed to manage and automate a wide range of financial and operational business processes. It is a comprehensive, cloud-based solution that integrates various modules to help organizations streamline operations, improve decision-making, and achieve greater financial control."

**ERP Benefits (sourced — REUSABLE):**
- Unified Platform: Combines financial, procurement, project management, and supply chain functions into a single, integrated system
- Cloud-Based: Reduces the need for on-premises infrastructure and enables access from anywhere, enhancing business continuity
- Real-Time Insights: Provides real-time data and analytics for faster decision-making
- Scalability: Adapts to business growth, small enterprise to large multinational
- Automation: Automates routine tasks and processes, reducing manual effort and errors
- Compliance: Helps organizations stay compliant with various regulatory requirements

**Financial Management module descriptions (sourced — REUSABLE):**

| Module | Sourced Description |
|---|---|
| General Ledger | Centralized accounting hub that supports complex financial structures, multi-entity accounting, and real-time financial reporting |
| Accounts Payable | Automates invoice processing, vendor payments, and compliance with global tax regulations |
| Accounts Receivable | Manages customer billing, collections, and cash application processes |
| Fixed Assets Management | Tracks and manages the lifecycle of fixed assets, including depreciation and asset transfers |
| Cash Management | Provides visibility into cash positions, cash forecasting, and bank reconciliation |

*Source: BSA ERP proposal lines 402–420*

**Analytics and Reporting (sourced — REUSABLE):**

| Capability | Sourced Description |
|---|---|
| Embedded Analytics | Real-time reporting and analytics embedded within the ERP modules, providing insights into financial performance, operational efficiency, and more |
| Financial Reporting Center | A centralized platform for generating, scheduling, and distributing financial reports |
| Dashboards and KPIs | Role-based dashboards with key performance indicators (KPIs) for monitoring business performance |

*Source: BSA ERP proposal lines 448–460*

**Project Contract Billing (sourced — REUSABLE):**

| Capability | Sourced Description |
|---|---|
| Contract Management | Create and manage complex contracts, including terms, conditions, and billing arrangements |
| Billing Rules | Set up flexible billing methods — fixed-price, time and materials, milestone-based billing |
| Revenue Recognition | Automatically recognize revenue in compliance with accounting standards |
| Invoice Processing | Automate invoice creation and processing based on contract terms and project progress |
| Customer Collaboration | Collaborate with customers through portals for contract approval, invoice tracking, and dispute resolution |

*Source: BSA ERP proposal lines 460–477*

**Project Financials (sourced — REUSABLE):**

| Capability | Sourced Description |
|---|---|
| Budgeting and Forecasting | Create detailed project budgets and forecasts for financial planning and management |
| Cost Management | Track and control project costs including labour, materials, and overhead |
| Capital Projects | Manage capital project expenditures and asset capitalization processes |
| Financial Reporting | Generate comprehensive financial reports including P&L, cash flow analysis, project profitability |
| Integration with General Ledger | Seamlessly integrate with Oracle Fusion GL for consistent and accurate reporting |

*Source: BSA ERP proposal lines 479–495*

**Project Management (sourced — REUSABLE):**

| Capability | Sourced Description |
|---|---|
| Project Planning | Define project scope, objectives, timelines, and resources |
| Task Management | Break down projects into tasks, assign responsibilities, track progress |
| Resource Management | Allocate and manage resources — personnel, equipment, materials |
| Collaboration | Integrated collaboration tools including document sharing and discussion forums |
| Project Monitoring and Control | Real-time dashboards and analytics for proactive management and risk mitigation |
| Issue and Risk Management | Identify and manage project risks and issues |

*Source: BSA ERP proposal lines 496–516*

---

### Procurement Sections Found — PRIMARY SOURCED CONTENT

**Oracle Fusion Procurement Overview (sourced — REUSABLE, lines 561–604):**
> "Oracle Fusion Procurement is a comprehensive suite of cloud-based applications designed to streamline and enhance the procurement process for organizations. It integrates various procurement activities, enabling businesses to manage their procurement needs efficiently."

**Procurement Benefits (sourced):**
- Cost Reduction: Centralising and streamlining procurement processes reduces costs and eliminates inefficiencies
- Improved Supplier Relationships: Enhanced collaboration tools foster better supplier relationships
- Increased Visibility: Real-time insights and analytics provide greater visibility into procurement activities
- Compliance and Risk Management: Manage compliance with contracts, policies, and regulations

**Procurement Capabilities (sourced — REUSABLE):**

| Capability | Sourced Description |
|---|---|
| Procurement Contracts | Manages the entire lifecycle of procurement contracts — creation, negotiation, approval, and management. Ensures compliance with organizational policies and legal requirements |
| Self-Service Procurement | Allows employees to request goods and services through a user-friendly, catalog-based interface. Reduces maverick spending by guiding employees towards approved suppliers |
| Sourcing | Facilitates strategic sourcing — supplier identification, bid collection, bid evaluation. Supports RFQs and reverse auctions |
| Supplier Qualification Management | Assesses and manages supplier risk and performance. Automates qualification to ensure only qualified suppliers participate |
| Supplier Portal | Platform for suppliers to manage profiles, view purchase orders, submit invoices, and track payments |
| Spend Analysis | Analyses procurement spending to identify cost-saving opportunities; insights into supplier performance, spend categories, and trends |
| Purchase Order Management | Manages creation, approval, and tracking of purchase orders. Ensures alignment with contracts and organizational policies |

*Source: BSA ERP proposal lines 570–604*

**Self-Service Procurement (sourced — REUSABLE, lines 717–805):**
Key capabilities: consumer-like shopping experience, guided buying toward approved suppliers, real-time budget checks via Oracle Financials integration, automated approval workflows, self-service receiving and returns, spend analysis reporting.

---

### SCM Sections Found — PRIMARY SOURCED CONTENT

**Oracle Fusion SCM / Supply Chain Execution (sourced — REUSABLE, lines 658–715):**

| Capability | Sourced Description |
|---|---|
| Inventory Management | Real-time visibility into inventory levels across multiple locations; supports multi-channel fulfilment, lot and serial tracking, inventory valuation |
| Order Management | Manages entire order-to-cash process — order capture through fulfilment and invoicing; supports drop shipping, backorders, split shipments |
| Logistics Management | Optimises transportation and logistics; transportation planning, execution, freight management; real-time shipment tracking |
| Warehouse Management | Manages receiving, storage, picking, packing, shipping; supports cross-docking, wave picking, task interleaving |
| Procurement | Automates procurement from requisitioning through PO creation, supplier management, invoice processing; strategic sourcing and contract management |
| Supply Chain Planning | Demand forecasting, supply planning, inventory optimisation; S&OP processes; scenario planning and what-if analysis |
| Global Trade Management | Import/export compliance, customs documentation, trade finance; international trade regulation compliance |
| Quality Management | Quality standards throughout supply chain — inspections, non-conformance management, corrective actions |
| Maintenance | Asset maintenance management — preventive, corrective, predictive maintenance strategies |

*Source: BSA ERP proposal lines 658–715*

**Order Management (sourced — REUSABLE, lines 605–657):**
Centralised order hub for multi-channel order management, order promising with global inventory visibility, configurable workflows, pricing and discount management, advanced analytics; seamless integration with Oracle Financials Cloud for invoicing and revenue recognition.

---

### Integration Sections Found

BSA OIC section is identical in content to the PayInc OIC description — both sourced from APPSolve's standard Oracle Fusion Information document. Key additions:
- "APPSolve is the only African partner which is certified on Oracle Integration cloud" (line 274)
  - **TEMPORAL RISK:** This claim was made in August 2024. It may not be accurate in 2026. Record as differentiator with temporal caveat.
- Process automation spanning multiple applications via OIC

---

### Reporting Section (sourced — REUSABLE, lines 930–932)

**Oracle Financials Cloud reporting tools:**
> "Oracle Financials Cloud provides predefined analyses, dashboards, and reports that help you meet financial and business intelligence requirements. The Financial Reporting Center is intended to be the primary user interface for financials end users to access all seven report types."

Report types: Financial Reporting Web Studio Reports, Account Groups and Sunburst, Smart View Reports, Oracle Transactional Business Intelligence Analyses, Oracle Transactional Business Intelligence Dashboards, Oracle Analytics Publisher Reports, and Business Intelligence Mobile Apps.

---

### Monitoring and Audit

**Monitoring tools (sourced — REUSABLE, lines 935–940):**
- Oracle Management Cloud: Monitors infrastructure, applications, and performance — managed by Oracle as part of SaaS
- System Monitoring Dashboards: Built-in dashboards with KPIs, transaction statuses, and processing times
- Audit and Compliance Reporting: Tracks user activities, approvals, and changes in system configurations
- Health Checks and Logs: System health, log files, background process monitoring

---

### High Availability / Disaster Recovery

**Oracle SaaS HA/DR (sourced — line 964):**
> "Oracle Fusion Cloud Service is designed and hosted on highly resilient and highly available infrastructure, including a failover datacentre region."

SLA: 99.9% uptime target. Service credit tiers: 10% (<99.9%), 15% (<99.5%), 25% (<99.0%), 100% (<95.0%).

Oracle Data Guard for Production and Failover DataCentre. Annual DR exercises conducted.

---

### Migration Ease Section

**Sourced APPSolve statement on Oracle Cloud migration (line 942):**
> "For data migration, whether involving master data or transactional data, Oracle offers multiple methods for importing and validating data. Our team of consultants has developed tailored templates to facilitate data import across various modules, ensuring a smooth transition and alignment with Oracle's standards."

---

### Customisation Section — Key Sourced Content

BSA lines 895–924 contain a comprehensive sourced description of Oracle Cloud SaaS configurability:

**Configuration:** Functional Setup Manager (FSM), Flexfields (Descriptive, Key, Extensible)
**Personalisation:** UI drag-and-drop personalisation, Role-based Access Control (RBAC)
**Extensions:** Oracle Visual Builder, Groovy Scripting, Page Composer
**Integration:** OIC with pre-built adapters + REST/SOAP APIs
**Reports:** BI Publisher for custom reports and layouts; OTBI for ad-hoc; Financial Reporting Studio for GL-level
**Workflows:** BPM Workflows for approval automation; Approval Management Extensions
**Security:** Custom security policies, role-based data access
**Custom Apps:** Oracle PaaS for SaaS for custom application development

---

### Eligibility / Certification Claims

**Published cloud expertise (BSA lines 271–274):**
- Service Expertise in Oracle Cloud Platform Integration
- Service Expertise in Human Resources
- Service Expertise in Financials
- "APPSolve is the only African partner which is certified on Oracle Integration cloud."
  - **Caveat:** August 2024 claim. Not independently verified. May be outdated by 2026.

**BBBEE noted:** BEE Level 2 certificate referenced in submission (line 231) — `RS-17968-0724-C58`. This is the OLD Level 2 certificate (expired). Current certificate is Level 3 (RS-19451, August 2025, expires 2026-07-31). This confirms the ORACLE_FACT_BASELINE.md BEE correction is critical.

---

### Source 3: BankServAfrica Oracle Fusion Information (Jordan)

**Document name:** `Oracle Fusion Information for BankServe RFP - Jordan.docx`
**File path:** `Parties/Customers/Bankserv/RFP/ERP/1 Working/Oracle Fusion Information for BankServe RFP - Jordan.docx`
**Date:** 2024 (exact date not in document)
**Notes:** This is a subsidiary document feeding into the BSA main proposal. Content is identical to the Oracle Fusion module sections of the BSA V1 proposal — same module descriptions for ERP, Procurement, SCM, OIC, EPM. No unique content beyond the BSA V1 source. Not treated as a separate source.

---

## Contradictions and Corrections Identified

| ID | Finding | Impact | Resolution |
|---|---|---|---|
| MC-001 | Cape Union Mart in W2S1-001 Section 6 (SCM) — WRONG. Cape Union Mart is Financials + Procurement, confirmed Mpact references. | MATERIAL ERROR — Section 6 SCM was built on false evidence | Correct W2S1-001: Remove Cape Union Mart from SCM; move to Financials and Procurement sections |
| MC-002 | Nala country count: W2S1-001 Section 12 says "8 countries". Correct is 4 (SA, Lithuania, Romania, Finland). RedPath Mining RFI said "8 countries" — likely refers to a different count or a different scope. | MATERIAL ERROR — Factual misstatement in client reference table | Correct W2S1-001 Section 12: Nala = 4 countries |
| MC-003 | Mr Price scope: W2S1-001 and prior notes implied full HCM. Correct is Oracle HCM Learning Cloud only | HIGH — Scope overstated | Correct Section 12 client table |
| MC-004 | DFA is the only confirmed Fusion SCM client but is NOT available for reference | HIGH — SCM section had no referenceable evidence; it now has evidence but not referenceable | Correct Section 6 narrative accordingly |
| MC-005 | BEE Level 2 found in BSA submission (old cert) vs. current Level 3 | CRITICAL (already known) | Already flagged in ORACLE_FACT_BASELINE.md |

---

## Reusable Wording — Summary for W2S1-001

| Section | What is Available | Source | Status |
|---|---|---|---|
| Section 4 — Financials | Full module descriptions (GL, AP, AR, Fixed Assets, Cash Management) + ERP Benefits list | BSA ERP lines 389–420 | APPLIED to W2S1-001 |
| Section 4 — Financials | Reporting Center description + 7 report types | BSA ERP lines 930–932 | APPLIED to W2S1-001 |
| Section 5 — Procurement | All 7 procurement capabilities with sourced descriptions | BSA ERP lines 561–604 | APPLIED to W2S1-001 |
| Section 6 — SCM | Full SCM module descriptions (9 capabilities) | BSA ERP lines 658–715 | APPLIED to W2S1-001; client evidence note updated |
| Section 7 — Projects | Project Financials + Project Management + Project Contract Billing | BSA ERP lines 460–516 | APPLIED to W2S1-001 |
| Section 9 — OIC | OIC capabilities (already in W2S1-001 from PayInc/RedPath) | BSA ERP lines 806–855 | Already covered |
| Client Table | Full reference card data per client | Mpact references lines 470–643 | APPLIED to W2S1-001 Section 12 |

---

## Risks and Caveats

| ID | Risk | Severity |
|---|---|---|
| R-001 | BSA module descriptions (ERP, Procurement, SCM) are written as standard Oracle product descriptions, not APPSolve-specific delivery evidence. They appear in the proposal as "here is what the Oracle product does" — not "here is what APPSolve delivered". They are APPSolve-authored and used in client proposals, making them reusable. However, they should not be presented as evidence of APPSolve-specific delivery capability for these modules without client reference support. | MEDIUM |
| R-002 | "Only African partner certified on OIC" (August 2024) — not independently verified; may be outdated | MEDIUM — treat as differentiator claim requiring BU Lead confirmation |
| R-003 | DFA full scope (Financials, SCM, EPM, HCM, OIC, all integrations) is impressive but DFA is explicitly NOT available for reference (confirmed Mpact proposal line 641–642) | HIGH — cannot cite DFA in competitive tenders |
| R-004 | Cape Union Mart confirmed as Financials + Procurement (not SCM). This removes the only SCM reference client. Section 6 SCM is now feature-description only with no referenceable client. | MEDIUM for W2S1-001; HIGH if tender has SCM-heavy requirements |
| R-005 | Nala Renewables confirmed go-live April 2025, contact provided. Renewable energy sector. 4 countries. Contact: Panashe Moyo +27 66 528 3776 panashe.moyo@nalarenewables.com — available for reference | POSITIVE — strengthens Finance + international rollout story |
| R-006 | Investec confirmed July 2024 go-live, >1000 users, 3 countries (SA/UK/USA), available for reference via Meagan Botha. Largest active Fusion Finance reference by user count | POSITIVE — use as flagship Finance reference |

---

*Notes created: 2026-06-11*
*Feeds: W2S1-001-ORA-FusionCapability.md*
*Next action: Apply corrections and sourced content to W2S1-001*
