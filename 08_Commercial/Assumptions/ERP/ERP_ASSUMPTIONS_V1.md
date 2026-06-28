---
document_id: ERP-ASSUMPTIONS-V1
title: "Oracle Fusion ERP — Assumptions, Exclusions, Dependencies, Constraints and Customer Responsibilities"
version: "1.0"
status: "Approved"
created: "2026-06-15"
created_by: "WP11D — Oracle ERP Assumptions Pack"
approved_by: "BU Lead — Oracle Practice"
approved_date: "2026-06-15"
approved_for_reuse: true
lifecycle_status: APPROVED
category: "Commercial / Assumptions"
scope: "Oracle Fusion Financials Cloud (B86481), Oracle Fusion Procurement Cloud (B86482), Oracle Fusion Project Portfolio Management Cloud (B86483). Extends HCM_BASE_ASSUMPTIONS_V1.md where ERP is delivered in the same project as Oracle HCM. Standalone for ERP-only engagements."
apply_with: "TENDER_ASSUMPTION_ASSEMBLY_RULES.md"
parent_pack: "None — ERP Base is a standalone track. Load alongside OIC pack for all ERP engagements with integrations. Load alongside HCM Base where ERP and HCM are in the same project."
oracle_part_numbers: "B86481 (Financials) | B86482 (Procurement) | B86483 (PPM)"
kb_reference: "W4-ERP-001-ORA-FusionFinance.md | W4-ERP-002-ORA-FusionProcurement.md | W4-ERP-003-ORA-PPM.md"
assumption_count: 123
bu_lead_decisions_applied:
  - "BU-ERP-001 CLOSED: Default = one primary ledger per LE. Secondary ledgers, reporting ledgers and additional local GAAP ledgers excluded unless explicitly scoped. (ERP-GL-001)"
  - "BU-ERP-002 CLOSED: Intercompany accounting excluded from base GL scope unless explicitly listed. Basic balancing segment design may be included; intercompany accounting/rules/invoicing/eliminations require separate scope. (ERP-GL-006)"
  - "BU-ERP-003 CLOSED: Default = three-way match where Procurement and Receiving in scope. Two-way match only where Receiving not in scope or client confirms process. (ERP-AP-003)"
  - "BU-ERP-004 CLOSED: Fixed asset migration standard = opening balance only (asset cost / NBV / accumulated depreciation). Current asset register required from customer. Historical transactions excluded. (ERP-FA-002)"
  - "BU-ERP-005 CLOSED: ERP parallel running excluded by default. Short controlled validation period may be included only where explicitly stated in the proposal. Full parallel financial close cycles excluded unless separately scoped. (ERP-CUT-005)"
  - "BU-ERP-006 CLOSED: SARS eFiling integration not an APPSolve standard ERP capability; excluded unless specifically scoped as custom integration. Tax reporting extracts via OTBI may be included where explicitly listed. (ERP-INT-005, ERP-EXC-003)"
  - "BU-ERP-007 CLOSED: Data migration standard = two mock migration cycles plus one final production migration. Additional cycles require change control. (ERP-DAT-006)"
  - "BU-ERP-008 CLOSED: SSO excluded by default unless explicitly scoped. If client has Azure AD/Entra ID and Oracle Fusion licensing, SSO can be included as separately listed configuration activity. (ERP-SEC-006)"
---

# Oracle Fusion ERP — Assumptions V1.0

**Scope:** This document governs Oracle Fusion ERP implementations delivered by APPSolve, covering Financials (GL, AP, AR, Fixed Assets, Cash Management), Procurement, and Project Portfolio Management (PPM). Modules in scope for a specific engagement are confirmed by the Oracle BOM. Not all sections of this document apply to every engagement — the applicable sections are determined by the BOM line items.

**Relationship to other packs:** For ERP engagements that include integrations, load this pack alongside `OIC_ASSUMPTIONS_V1.md`. For combined ERP + HCM engagements, load `HCM_BASE_ASSUMPTIONS_V1.md` alongside this pack. HCM Base hypercare and general delivery assumptions (on-site, travel, testing cycles) apply to ERP engagements equally.

**Governance:** Status: Approved — 2026-06-15 | BU Lead — Oracle Practice. Approved for use in all Oracle Fusion ERP estimates, SOWs, proposals, and tender responses.

---

## 66. General ERP Scope Assumptions

**ERP-GEN-001**  
APPSolve's scope in Oracle Fusion ERP engagements covers: configuration design (Chart of Accounts, ledger structure, module setup); system configuration (applying the agreed design in Oracle ERP); data migration (FBDI load of agreed data objects); integration setup (where in scope — governed by OIC pack); testing support (CRP1, CRP2, UAT support); training delivery (TTT); cutover execution; and hypercare. APPSolve does not manage, administer, or operate the client's business processes post-go-live.

**ERP-GEN-002**  
APPSolve's Oracle ERP implementations follow the Oracle Unified Method (OUM): Mobilize → Scope and Design → Prototype → Validate → Deploy → Evolve. The Customer Success Navigator (CSN) accelerates delivery within OUM. Each phase has defined deliverables and client approval gates.

**ERP-GEN-003**  
Modules in scope are confirmed by the Oracle BOM signed at the time of SOW execution. Modules not in the signed BOM are excluded from scope. Where the client adds a module after SOW execution, the additional module is assessed and priced as a Change Request.

**ERP-GEN-004**  
Oracle Fusion ERP is delivered as a SaaS platform by Oracle. APPSolve configures the platform; Oracle operates it. The client receives one Production environment and at least one non-production (test) environment under the standard Oracle SaaS subscription. APPSolve does not procure, manage, or operate Oracle ERP infrastructure.

**ERP-GEN-005**  
Oracle Fusion ERP implementations are configuration-based. APPSolve uses Oracle-delivered configuration tools (Setup and Maintenance, BPM Worklist, Application Composer). Custom code development — Oracle APEX extensions, Oracle PaaS customisations, Groovy scripts beyond standard Oracle ERP configuration — is assessed as a separately scoped item.

**ERP-GEN-006**  
Oracle Fusion ERP receives quarterly updates from Oracle as part of the SaaS subscription. Oracle manages the update schedule. APPSolve provides implementation services; ongoing update management and regression testing post-go-live are the client's responsibility unless an APPSolve AMS agreement covers this.

**ERP-GEN-007**  
The Chart of Accounts (COA) design is the most critical early Scope and Design decision in an Oracle ERP Financials implementation. All downstream configuration — ledger setup, cross-validation rules, financial reporting, cost centre hierarchy, budget structure — depends on an approved COA. Delays to COA sign-off cascade to all dependent configuration streams. COA design must be signed off by the client before ledger configuration commences.

**ERP-GEN-008**  
The client's legal entity structure (company code, legal entity names, business unit structure) must be confirmed and stable before legal entity configuration commences. Changes to the legal entity structure after legal entity configuration is complete may require significant rework. APPSolve flags legal entity design changes as a project risk with scope impact.

---

## 67. Oracle Fusion Financials — General Ledger

**ERP-GL-001**  
APPSolve configures one primary ledger per legal entity. A primary ledger holds the main accounting records in the functional currency. Secondary ledgers — including reporting currency ledgers, IFRS vs local GAAP adjustment ledgers, and any additional statutory or management accounting ledgers — are excluded from base scope unless explicitly listed in the proposal and SOW. Where secondary ledgers are required, their design, configuration, and testing effort is separately assessed and priced.

**ERP-GL-002**  
The client is responsible for defining the Chart of Accounts structure: the segment names, segment lengths, value set definitions, and the complete list of code combination values for each segment. APPSolve configures the COA in Oracle ERP based on the client-approved COA design. APPSolve facilitates COA design workshops; it does not design the client's COA from scratch.

**ERP-GL-003**  
The default Chart of Accounts structure includes up to six (6) segments: Company/Entity, Department, Account (Natural Account), Cost Centre, Project, and one additional segment confirmed in the Scope and Design phase. Additional segments beyond six require assessment and may affect reporting and cross-validation rule complexity. The client confirms the final segment structure before COA configuration commences.

**ERP-GL-004**  
The client provides the financial calendar — accounting year-end month, period type (monthly, 12 periods per year is the standard), and the financial year start date — before ledger configuration commences. APPSolve configures the Oracle accounting calendar per the client's confirmed specifications.

**ERP-GL-005**  
The functional currency (the currency in which each legal entity conducts its primary business and keeps its books of account) is confirmed per legal entity before ledger configuration commences. For South African operations, the functional currency is ZAR. Where a legal entity operates in a foreign currency, the functional currency, presentation currency, and currency conversion method are confirmed in the Scope and Design phase.

**ERP-GL-006**  
Intercompany accounting is excluded from base GL scope unless explicitly listed in the proposal. Basic balancing segment design — configuring the primary balancing segment so that Oracle ERP automatically balances intercompany entries — may be included as part of the standard COA and ledger configuration. Full intercompany accounting scope (intercompany accounting rules, intercompany invoicing, intercompany reconciliation workflows, multi-lateral netting, and consolidation eliminations) requires a separately scoped and priced engagement.

**ERP-GL-007**  
APPSolve configures one (1) standard journal approval workflow per Oracle ERP instance. The journal approval workflow routes manual journal entries through an approval chain before posting. Additional journal approval workflows (for example, separate workflows per business unit, per journal category, or per ledger) constitute a Change Request.

**ERP-GL-008**  
Financial reporting: APPSolve configures Financial Reporting Studio (FRS) reports covering the client's agreed standard financial statement pack (Income Statement, Balance Sheet, Trial Balance, and Cash Flow Statement where required). The number of FRS reports agreed is documented in the Scope and Design deliverables. Additional financial reports beyond the agreed scope are Change Requests.

---

## 68. Oracle Fusion Accounts Payable

**ERP-AP-001**  
Supplier master data is migrated from the client's source system as part of the data migration scope. The client provides all supplier master data — including legal name, registration number, tax registration number, bank account details, payment terms, and address — in APPSolve's FBDI supplier template. APPSolve loads and validates the supplier data in Oracle ERP.

**ERP-AP-002**  
Manual invoice entry is the default AP invoice processing approach. Automated invoice capture — OCR-based invoice imaging, intelligent document processing, e-invoicing via supplier networks (Ariba Network, Tungsten/OB10, or equivalent) — is excluded from base scope. Where the client requires automated invoice capture, this is assessed as a scope addition.

**ERP-AP-003**  
Three-way match (PO / Goods Receipt Note / Invoice) is the APPSolve default for purchase-order-based supplier invoices where Oracle Procurement and Oracle Receiving are both in scope. Three-way match validates that the invoice quantity and amount match both the approved PO and the confirmed goods receipt before the invoice is approved for payment. Two-way match (PO / Invoice only, without a goods receipt) may be used only where Oracle Receiving is not in the BOM scope, or where the client explicitly confirms that their purchasing process does not use goods receipt confirmation. The matching approach is confirmed in the Scope and Design phase and documented in the AP configuration design.

**ERP-AP-004**  
Non-PO invoices (invoices without a corresponding purchase order — typically for services, utilities, rent, and overhead costs) are entered via Oracle AP's direct invoice entry workflow. The non-PO invoice approval routing is designed in the Scope and Design phase. One standard non-PO invoice approval workflow is included.

**ERP-AP-005**  
Payment processing: APPSolve configures Oracle AP for EFT (electronic funds transfer) payments to South African bank accounts using the standard South African EFT payment format. The specific bank payment format file specification is confirmed with the client's bank before AP payment configuration commences. Where BeBanking is in scope, payment file generation and bank submission are facilitated via the BeBanking H2H integration (see OIC pack).

**ERP-AP-006**  
Payment terms (standard supplier payment terms — 30 days, 60 days, net immediate, etc.) are configured in Oracle AP based on the list of payment terms provided by the client. APPSolve configures all payment terms provided by the client; it does not define the client's payment terms policy.

**ERP-AP-007**  
Oracle Supplier Portal — enabling suppliers to submit invoices electronically, view PO status, and update their own profile — is excluded from base scope. The Supplier Portal requires Oracle Supplier Portal Cloud Service (separately licensed) and an integration setup. Where Supplier Portal is required, it is assessed and priced as a scope addition.

---

## 69. Oracle Fusion Accounts Receivable

**ERP-AR-001**  
Customer master data is migrated from the client's source system as part of the data migration scope. The client provides customer data — legal name, account number, address, payment terms, credit limit, and tax details — in APPSolve's FBDI customer template.

**ERP-AR-002**  
Oracle AR transaction types (invoice, credit memo, debit memo) and transaction sources are configured per the client's billing processes confirmed in the Scope and Design phase. APPSolve configures the transaction type library; the client confirms which transaction types are required.

**ERP-AR-003**  
Auto-invoicing — importing invoice transactions from another Oracle module (Oracle Fusion PPM, Oracle Order Management, or another source system) — is included in standard AR scope where the source system is an Oracle module in the same implementation. Auto-invoicing from a non-Oracle source requires an OIC integration (see OIC pack).

**ERP-AR-004**  
Cash application: Oracle AR is configured with standard auto-cash rules for EFT receipts — matching receipts to open invoices by invoice number or customer account. Complex cash application scenarios (foreign currency receipts, partial payments with deduction management, lockbox processing for high-volume B2C receipts) are assessed per complexity.

**ERP-AR-005**  
Oracle AR Collections Management — automated dunning letter generation, collection strategy assignment, and aged debt reporting — is an Oracle-delivered platform feature. APPSolve configures the collections framework (dunning letter templates, collection strategies) as part of the standard AR implementation. The client's credit control team manages collections activity post-go-live.

---

## 70. Oracle Fusion Fixed Assets

**ERP-FA-001**  
APPSolve configures Oracle FA asset categories (the grouping structure that defines default depreciation rules for each asset type), depreciation methods, useful life assignments, and the asset book structure. The client provides the complete list of asset categories with their depreciation rules before FA configuration commences.

**ERP-FA-002**  
Fixed asset migration standard is opening balance only as at the go-live date. The opening balance migration includes: asset description, asset cost (original cost), net book value (NBV) at go-live, accumulated depreciation at go-live, and remaining useful life. Detailed historical asset transactions — period-by-period depreciation run history, historical revaluation journals, historical impairment entries, and asset additions/disposals prior to go-live — are not migrated. The client's legacy asset system is retained as the system of record for historical fixed asset data. The client is required to provide the current, reconciled asset register (including cost, accumulated depreciation, and NBV per asset) before migration commences. Migration cannot proceed without a client-approved asset register.

**ERP-FA-003**  
Oracle FA is configured to run periodic (monthly) depreciation as a batch process. The client's finance team runs the depreciation process in Oracle after period-end close. APPSolve configures the depreciation process; the client's finance team operates it post-go-live.

**ERP-FA-004**  
Capital expenditure approval (the workflow for approving a capital purchase before the asset is created in Oracle FA) is configured as one standard capex approval workflow. The approval routing is based on the client's confirmed authority matrix.

**ERP-FA-005**  
A tax asset book (tracking assets for tax depreciation purposes separately from the accounting asset book) is assessed per engagement. Where South African tax depreciation allowances (Section 11/12 SITA, accelerated depreciation, SBC allowances) require separate tracking from accounting depreciation, a tax book is added to the design.

---

## 71. Oracle Fusion Cash Management

**ERP-CM-001**  
Oracle Cash Management is configured for bank reconciliation. APPSolve configures bank accounts in Oracle CM, defines reconciliation rules, and enables the bank statement import capability. Manual bank reconciliation (bank officer manually reconciles bank statement to Oracle cash entries) and automated reconciliation (via electronic bank statement import) are both supported.

**ERP-CM-002**  
Bank statement import format is confirmed with the client's bank. Oracle CM supports ISO 20022 camt.053 and SWIFT MT940 as standard formats for electronic bank statement import. Where the bank uses a proprietary format not supported by Oracle natively, a format conversion is assessed. Where BeBanking is in scope, MT940 inbound via the BeBanking integration is the standard mechanism (see OIC pack).

**ERP-CM-003**  
Cash positioning and cash forecasting capabilities are Oracle-delivered platform features within Oracle CM. APPSolve enables and configures cash positioning as part of the standard CM implementation. The accuracy of cash forecasts depends on the completeness of Oracle AP payment schedules and AR expected receipt data.

**ERP-CM-004**  
Where BeBanking H2H bank connectivity is in scope (B86481 + BeBanking BOM), the MT940 bank statement inbound integration from BeBanking to Oracle CM is configured as part of the BeBanking OIC integration scope (OIC pack OIC-SCP-001). The Oracle CM bank account and reconciliation rules are configured as part of the ERP Financials scope.

---

## 72. Oracle Fusion Procurement

**ERP-PRO-001**  
Oracle Procurement modules in scope are confirmed by the BOM. Standard Procurement scope includes Self-Service Procurement (purchase requisitioning), Oracle Purchasing (PO management, approval, receiving), and where licensed, Oracle Sourcing (RFQ, RFP, auction management) and Oracle Procurement Contracts.

**ERP-PRO-002**  
The requisition-to-PO procurement flow is the core Procurement process. APPSolve configures: purchase requisition entry and approval; automatic PO creation from approved requisitions; PO acknowledgement; goods receipt (Oracle Receiving); and three-way match linkage to Oracle AP. The flow design is agreed in the Scope and Design phase.

**ERP-PRO-003**  
Procurement approval hierarchy: APPSolve configures one approval hierarchy for purchase requisitions and one for purchase orders, using Oracle Approval Management Engine (AME). The default is position-based approval (routing based on the requester's position in the organisation hierarchy). Employee-supervisor based approval is an alternative. The approval authority matrix (who can approve, up to what amount) is provided by the client before workflow configuration commences.

**ERP-PRO-004**  
Oracle Procurement catalogue management: APPSolve configures hosted item catalogues in Oracle Self-Service Procurement where the client wishes to restrict requisitions to approved items at pre-agreed prices. The client provides item catalogue data (item descriptions, unit prices, supplier links) in the required template. Punchout catalogues (integration to a supplier-hosted catalogue) require a separately scoped OIC integration.

**ERP-PRO-005**  
Oracle Procurement Contracts (where in scope): APPSolve configures contract templates, standard contract terms, and the contract authoring workflow. The client provides the legal content for contract templates (standard terms and conditions, deviation approval rules). APPSolve configures the Oracle contract framework; the client's legal team is responsible for the contract content.

**ERP-PRO-006**  
Oracle Receiving (GRN processing) is included in standard Procurement scope for PO-based purchasing. Receiving records the physical delivery of goods against a purchase order and triggers the three-way match process in Oracle AP. The goods receipt workflow (who records receipts, on what device, in what location) is confirmed in the Scope and Design phase.

**ERP-PRO-007**  
Oracle Spend Analytics and Procurement reporting use Oracle OTBI's Procurement subject areas. APPSolve configures procurement-specific OTBI reporting security and delivers the agreed set of standard procurement reports. Advanced spend analysis requiring Oracle Procurement Analytics Cloud (OAX) is separately licensed and assessed.

---

## 73. Oracle Fusion Project Portfolio Management (PPM)

**ERP-PPM-001**  
Oracle Fusion PPM modules in scope are confirmed by the BOM. Standard PPM scope includes Project Costing (B86483) — project creation and maintenance, cost collection, project reporting. Where Oracle Project Billing is in scope, billing events and revenue recognition are added.

**ERP-PPM-002**  
Project types and project templates are designed in the Scope and Design phase. The client provides the project classification structure (project types, project statuses, project categories) and the template for each project type before PPM configuration commences. APPSolve configures the Oracle PPM project type library based on the client's confirmed structure.

**ERP-PPM-003**  
Project costing: cost transactions are collected against projects using Oracle's standard cost collection mechanisms — labour costs (via Oracle Time and Labour or manual timecard entry), non-labour costs (via Oracle AP invoice line distribution to a project), and expense costs (where Oracle Expenses is in scope). The costing design is confirmed in the Scope and Design phase.

**ERP-PPM-004**  
Project budgeting: Oracle PPM supports project-level budgets and forecasts. APPSolve configures the budget type structure and budget approval workflow as agreed in Scope and Design. The client provides project budget templates before budget configuration commences.

**ERP-PPM-005**  
Oracle Project Billing (where in scope): billing methods supported by Oracle PPM include time-and-material billing, fixed-price milestones, and cost-plus billing. The billing method per project type is confirmed in the Scope and Design phase. The client confirms the billing events, billing cycles, and revenue recognition rules before billing configuration commences.

**ERP-PPM-006**  
Integration between Oracle PPM and Oracle Financials (GL and AP) is Oracle-native — project cost transactions post automatically to the General Ledger via Oracle's subledger accounting engine. This is not a separately scoped OIC integration. APPSolve configures the subledger accounting (SLA) rules that govern how project costs hit the GL.

**ERP-PPM-007**  
Project reporting via OTBI: APPSolve configures PPM OTBI reporting security and delivers agreed project performance reports. Advanced project portfolio analytics and dashboard capabilities requiring Oracle Analytics Cloud are separately licensed and excluded from PPM base scope.

---

## 74. Reporting and Analytics

**ERP-REP-001**  
Oracle Transaction Business Intelligence (OTBI) is the standard embedded reporting tool for Oracle Fusion ERP. APPSolve configures OTBI reporting security (subject area access, data security filters) and delivers the agreed custom OTBI reports as part of the implementation. The number of custom OTBI reports included in scope is confirmed in the Scope and Design phase.

**ERP-REP-002**  
Oracle Financial Reporting Studio (FRS) — the tool for designing formatted financial statements — is included in Oracle Fusion ERP. APPSolve configures FRS reports for the agreed standard financial statement pack. The number of FRS reports in scope is confirmed in the Scope and Design phase.

**ERP-REP-003**  
Oracle Smart View (Excel add-in enabling financial data queries directly from Excel against Oracle ERP) is an Oracle-delivered feature included in the ERP subscription. APPSolve enables Smart View and provides awareness training to finance users. The client's finance team is responsible for building their own Smart View-based Excel models; APPSolve does not build client Excel reporting models.

**ERP-REP-004**  
Oracle Analytics Cloud (OAX/FAW — Fusion Analytics Warehouse) is a separately licensed Oracle product and is not included in the standard Oracle Fusion ERP subscription. OTBI, FRS, and Smart View are included in the ERP licence. Where the client requires OAX analytics, it is a separately licensed and separately scoped item.

**ERP-REP-005**  
SARS VAT return reporting: Oracle ERP captures the VAT transaction data required to prepare the VAT201 return. APPSolve configures OTBI VAT reports that the client's tax team uses to extract VAT data. Oracle Fusion ERP does not submit VAT returns to SARS eFiling. The eFiling submission is the client's tax team's responsibility.

---

## 75. Data Migration

**ERP-DAT-001**  
Data migration follows Oracle's File-Based Data Import (FBDI) framework for all standard Oracle ERP data objects. APPSolve provides FBDI templates for each data object in scope; the client populates these templates with data extracted from the source system. APPSolve loads and validates the data in Oracle ERP.

**ERP-DAT-002**  
Standard migrated data objects for Oracle Fusion ERP (subject to BOM and scope confirmation): Chart of Accounts value sets and code combinations; suppliers (AP); customers (AR); open AP invoices and payment schedules; open AR invoices and receipt applications; fixed asset register (opening balance); projects and project budgets (PPM); open purchase orders (Procurement).

**ERP-DAT-003**  
Historical transaction data is not migrated. Opening balances are migrated as at the agreed cut-over date. This means: historical GL journals (prior periods) are not in Oracle ERP; historical paid AP invoices are not in Oracle ERP; historical closed AR invoices are not in Oracle ERP. The client's legacy system is the system of record for historical data.

**ERP-DAT-004**  
Data extraction from the source (legacy) system is the client's responsibility. APPSolve provides the FBDI templates and format specifications. The client's IT team or legacy system administrator extracts data from the legacy system and populates the FBDI templates. APPSolve is available for template guidance but does not extract data from legacy systems.

**ERP-DAT-005**  
Data quality and cleansing is the client's responsibility before data is provided to APPSolve. Data provided to APPSolve must be: de-duplicated (no duplicate supplier or customer records); complete (all mandatory fields populated); accurate (values match the business reality); and correctly coded (GL codes, cost centres, and project codes aligned to the agreed COA). APPSolve validates that data loads correctly into Oracle ERP; it does not validate the business accuracy of source data.

**ERP-DAT-006**  
Two migration cycles are standard: (1) Mock Migration 1 — executed in the non-production environment to test the FBDI load process, identify data issues, and allow the client to correct data; (2) Mock Migration 2 — a repeat mock run after data corrections, validating that all issues from Mock 1 are resolved; (3) Final Migration — executed in the production environment at go-live. A total of two mock cycles plus one final production migration is the APPSolve base scope. Additional migration cycles beyond two mocks require a change control approval and are priced per additional cycle.

**ERP-DAT-007**  
Tax registration data — VAT registration numbers, income tax reference numbers, customs registration numbers, and PAYE reference numbers — is configured in Oracle ERP as part of the legal entity and tax setup. The client provides all tax registration information before legal entity and tax configuration commences.

---

## 76. Integration Assumptions (ERP-Specific)

**ERP-INT-001**  
All ERP integrations to third-party systems are governed by `OIC_ASSUMPTIONS_V1.md`. This section defines ERP-specific integration scope boundaries and Oracle-native integration points that do not require OIC.

**ERP-INT-002**  
Oracle Fusion ERP to Oracle Fusion HCM (where both modules are in scope in the same project): the ERP-HCM integration uses Oracle-native REST APIs and Oracle-delivered integration patterns. This is not a separately scoped OIC integration; it is included in the combined HCM + ERP implementation scope.

**ERP-INT-003**  
Within Oracle Fusion ERP, inter-module integration (for example: AP to GL subledger accounting posting; Procurement to AP invoice matching; PPM cost to GL) uses Oracle-native subledger accounting and integration architecture. These are not separately scoped OIC integrations.

**ERP-INT-004**  
Bank connectivity — EFT payment file generation and bank statement import — is facilitated via BeBanking H2H (where BeBanking is in scope) or via direct bank file format integration where BeBanking is not in scope. Each payment format (different bank or different payment type) constitutes one OIC integration (see OIC_ASSUMPTIONS_V1.md OIC-SCP-002).

**ERP-INT-005**  
SARS eFiling integration is not an APPSolve standard ERP capability and is excluded from scope unless specifically contracted as a custom integration engagement. Oracle Fusion ERP does not have a native integration to the SARS eFiling portal. Automated submission of VAT201, PAYE EMP201, or provisional tax returns to SARS is the client's tax team's responsibility using their preferred submission method (manual eFiling, tax software, or separately contracted integration). Tax reporting data extracts — OTBI-based VAT reports or GL tax reports to support the client's manual eFiling process — may be included in scope where explicitly listed in the proposal.

---

## 77. Security Assumptions

**ERP-SEC-001**  
APPSolve designs and configures the Oracle Fusion ERP security model: job roles, data security policies, duty roles, and abstract roles. The security design is agreed in the Scope and Design phase. APPSolve uses Oracle-delivered roles as the starting point and creates custom roles only where Oracle-delivered roles do not meet the client's access requirements.

**ERP-SEC-002**  
The number of custom job roles is confirmed in the Scope and Design phase. Standard APPSolve ERP security designs use the following Oracle-delivered role archetypes: Financial Analyst, AP Invoice Supervisor, AR Billing Specialist, Cash Manager, Procurement Manager, Procurement Agent, and Project Manager. Custom roles are created for access patterns not covered by Oracle-delivered roles.

**ERP-SEC-003**  
Data security policies — row-level security restricting users to specific ledgers, business units, legal entities, or cost centres — are designed in the Scope and Design phase. Complex data security requirements (for example, a user who can view GL for one legal entity but AP for a different business unit) increase design and testing effort and are assessed per complexity.

**ERP-SEC-004**  
Segregation of Duties (SoD) awareness: APPSolve designs Oracle ERP roles following Oracle's recommended SoD guidelines. Formal SoD analysis — using Oracle Access Controls Governor (ACG), Fastpath, or equivalent specialist SoD tool — is excluded from base scope. Where a formal SoD audit is required (for example, by external auditors or internal audit), it is assessed as a separately scoped item using the appropriate tool.

**ERP-SEC-005**  
User provisioning post-go-live: creating new Oracle ERP users, assigning roles to users, and deactivating users who leave the organisation are the client's IT team's responsibility after go-live. APPSolve configures the user provisioning framework during implementation; ongoing user lifecycle management is operational, not implementation, work.

**ERP-SEC-006**  
Single Sign-On (SSO) is excluded from base ERP scope unless explicitly scoped and listed in the proposal. Oracle Fusion ERP supports SAML 2.0 SSO as an Oracle platform feature. Where the client uses Microsoft Azure AD / Entra ID and holds Oracle Fusion Cloud licensing that supports SAML 2.0 federation, SSO can be included in the implementation as a separately listed configuration activity — this must be explicitly named in the proposal scope section and priced accordingly. SSO configuration with other identity providers (Okta, Ping Identity, Google Workspace, ADFS) is assessed per client environment. In all cases, the client's IT security team must provide IdP federation metadata and co-ordinate certificate configuration before SSO configuration commences.

---

## 78. Workflow and Approval Assumptions

**ERP-WFL-001**  
All Oracle Fusion ERP approval workflows are configured using the Oracle Approval Management Engine (AME). APPSolve configures AME approval rules per the workflow design agreed in the Scope and Design phase. The client provides the complete authority matrix — defining who can approve what transaction type at what monetary amount — before workflow configuration commences.

**ERP-WFL-002**  
Standard approval workflows included in base ERP scope (subject to module BOM): (a) Manual journal approval (GL); (b) Non-PO supplier invoice approval (AP); (c) Purchase requisition approval (Procurement); (d) Purchase order approval (Procurement); (e) Capex approval (Fixed Assets — where FA is in scope); (f) Project budget approval (PPM — where PPM is in scope). Each workflow listed constitutes one APPSolve configuration item.

**ERP-WFL-003**  
One approval hierarchy is configured per workflow type. Multiple parallel approval hierarchies per workflow (for example, a different PO approval chain for each business unit or department) constitute a Change Request and are assessed per the number of additional hierarchies required.

**ERP-WFL-004**  
Oracle Fusion ERP approval notification emails use Oracle's standard BPM Worklist notification framework. Notifications are delivered via Oracle's workflow notification engine. Custom HTML-branded email templates are excluded from base scope. HCM Base assumption HCM-WFL-004 applies where HCM and ERP are in the same project.

**ERP-WFL-005**  
Delegation rules — allowing a user to delegate their approval authority to another user during absence — are an Oracle ERP platform feature. APPSolve enables delegation capability as part of the standard workflow configuration. Users manage their own delegation rules post-go-live via the Oracle ERP self-service interface.

**ERP-WFL-006**  
Approval limits (the monetary amount thresholds that determine which approver handles which transaction value) are configured per the client's authority matrix. The client provides the complete, approved authority matrix before workflow configuration commences. Changes to approval limits after workflow configuration is complete are low-effort configuration changes and do not constitute a Change Request unless they require structural workflow redesign.

---

## 79. Testing Assumptions

**ERP-TST-001**  
Oracle Fusion ERP testing follows the OUM testing framework and aligns to HCM Base testing assumptions (HCM-TST-001 through HCM-TST-004 where applicable). Three testing cycles: CRP1 — Design Validation; CRP2 — End-to-End Validation; UAT — User Acceptance Testing.

**ERP-TST-002**  
CRP1 (Design Validation): APPSolve demonstrates the configured system against the agreed Scope and Design document. The client's functional team (finance leads, procurement leads, PPM leads) validates that the configured process matches the design. CRP1 is a structured design review — not a user acceptance test.

**ERP-TST-003**  
CRP2 (End-to-End Validation): complete end-to-end process testing across all configured ERP modules. For example: purchase requisition → PO approval → goods receipt → AP invoice → payment → GL posting → bank reconciliation. The client's functional team executes end-to-end scenarios with test data. APPSolve resolves configuration defects identified during CRP2.

**ERP-TST-004**  
UAT (User Acceptance Testing): the client's user community (finance users, procurement users, project managers) validates the system against their business requirements. APPSolve supports UAT but does not execute it. UAT sign-off is the client's responsibility and a mandatory prerequisite for production cutover.

**ERP-TST-005**  
Test data provision for all testing cycles is the client's responsibility. Test data must reflect realistic transaction values, include both standard and exception scenarios, and cover all modules in scope. APPSolve does not source, create, or transform test data.

**ERP-TST-006**  
Defect management follows the same classification as OIC testing (build defects resolved by APPSolve; data/process/design defects resolved by client). A formal defect log is maintained throughout all testing phases.

---

## 80. Training Assumptions

**ERP-TRN-001**  
APPSolve delivers train-the-trainer (TTT) training for Oracle Fusion ERP across the user populations agreed in the training plan. Default TTT populations (subject to BOM): GL and Financial Reporting users, AP Invoice Processors, AR Billing users, Cash Management users, Procurement Requisitioners and Buyers, PPM Project Managers (per modules in scope).

**ERP-TRN-002**  
End-user training delivery is the client's responsibility. APPSolve provides TTT training and delivers configured-system training guides and quick reference cards; the client's trained trainers deliver end-user training to the broader employee population. APPSolve does not train individual end users.

**ERP-TRN-003**  
Training materials are based on the client's configured Oracle ERP system. APPSolve does not use generic Oracle product training materials as the primary training deliverable. Training materials reference the client's specific COA, workflows, data, and transaction types.

**ERP-TRN-004**  
Oracle University formal training (Oracle certification courses, Oracle product training) is the client's commercial arrangement with Oracle. APPSolve's training scope covers the configured system — not Oracle product certification or generic Oracle Fusion overview training.

---

## 81. Cutover Assumptions

**ERP-CUT-001**  
One production cutover event is included. The cutover approach (big-bang cutover of all modules on one date, or phased module go-live) is confirmed in the Scope and Design phase and documented in the cutover plan. APPSolve recommends big-bang cutover for Oracle ERP where the modules are highly interdependent (GL, AP, AR in the same ledger must typically go live together).

**ERP-CUT-002**  
APPSolve produces a cutover runbook covering: pre-cutover steps (legacy system transaction freeze, final FBDI data extract, data validation, non-production mock run completion); cutover day steps (FBDI production load execution, opening balance verification, connectivity testing, integration activation); and go-live confirmation criteria (trial balance agrees, AP supplier list loaded, AR customer list loaded, open transaction count reconciled).

**ERP-CUT-003**  
Legacy system transaction freeze: the client implements a freeze on new transaction entry in the legacy system for the period required to extract final migration data and complete the FBDI load. The freeze duration is determined by the data volume and migration complexity. The client manages the internal communication and business impact of the freeze period.

**ERP-CUT-004**  
Go-live decision is made by the client's ERP project sponsor based on APPSolve's technical go/no-go assessment. APPSolve provides a written go/no-go recommendation; the final go-live decision rests with the client's project sponsor.

**ERP-CUT-005**  
ERP parallel running is excluded by default. Parallel running — simultaneously operating the legacy ERP and Oracle Fusion ERP for a period after go-live, with transaction reconciliation between both systems — is not included in the base scope. A short controlled validation period (typically five to ten business days, limited to trial balance and opening balance verification only, not full operational parallel close) may be included where this is explicitly stated in the proposal scope section. Full parallel financial close cycles — completing a full month-end close in both legacy and Oracle ERP simultaneously — are excluded unless separately scoped and priced. The commercial and resource implications of any parallel activity must be agreed before the SOW is executed.

---

## 82. Hypercare Assumptions

**ERP-HYP-001**  
ERP hypercare aligns to the APPSolve standard: four (4) weeks duration; business hours (08:00–17:00 SAST Monday–Friday); defect resolution and system stabilisation only. HCM Base assumptions HCM-HYP-001, HCM-HYP-002, and HCM-HYP-003 apply equally to Oracle Fusion ERP engagements.

**ERP-HYP-002**  
Where Oracle ERP and Oracle HCM and/or OIC integrations are delivered in the same project, hypercare is a single concurrent four-week period covering all modules and integrations. HCM Base HCM-HYP-001 and OIC pack OIC-SUP-002 apply.

**ERP-HYP-003**  
Enhancements and scope additions during hypercare are excluded. This includes: adding new GL accounts or COA segments post-go-live, adding new approval workflows, adding new OTBI reports beyond the agreed scope, and adding new modules not in the original BOM. These are assessed as Change Requests or new project work.

**ERP-HYP-004**  
Period-end close support during hypercare: APPSolve provides hypercare support during the first month-end close after go-live. If the hypercare period ends before the first month-end close, APPSolve will extend hypercare to cover the first month-end close at the standard daily hypercare rate. This ensures the client has APPSolve support during the most operationally critical post-go-live event.

---

## 83. Customer Responsibilities

**ERP-CUS-001**  
**Executive Sponsorship:** The client appoints an ERP project sponsor with authority to make business decisions affecting the ERP implementation: approving scope, resolving escalated design issues, authorising go-live, and driving internal change management. Without an empowered sponsor, design decisions stall.

**ERP-CUS-002**  
**Functional Team:** The client appoints functional leads for each module in scope (Finance Lead for GL/AP/AR/FA/CM; Procurement Lead for Procurement; PPM Lead for Projects). Functional leads are available for the full project duration, attend all workshops and CRP sessions, make business decisions in their domain, and provide sign-off at each milestone.

**ERP-CUS-003**  
**Chart of Accounts Design:** The COA structure — segments, value sets, and code combination values — is the client's most critical deliverable in the Scope and Design phase. The client's finance team provides the COA design (or APPSolve facilitates COA design workshops and the client approves the output) before COA configuration commences. COA delays cascade to all downstream configuration.

**ERP-CUS-004**  
**Data Provision:** The client extracts, cleanses, and provides all migration data in APPSolve's FBDI templates by the dates agreed in the project plan. Suppliers, customers, fixed assets, open payables, open receivables, open purchase orders, and projects — all data objects require client preparation. Late or incomplete data provision directly delays the go-live date.

**ERP-CUS-005**  
**Data Cleansing:** The client cleanses and validates source data before providing it to APPSolve. This includes: removing duplicate supplier or customer records; populating mandatory fields; correcting incorrect account codes; updating inactive or blocked records; and confirming bank account details. APPSolve does not cleanse source data.

**ERP-CUS-006**  
**Business Process Decisions:** The client's functional team makes all business process decisions required during the Scope and Design phase: which transaction types to use; how approval workflows should route; what payment terms to configure; which cost centres to include in the COA; how project billing works. APPSolve facilitates and documents; the client decides.

**ERP-CUS-007**  
**Authority Matrix:** The client provides the complete, approved authority matrix for all transaction types requiring approval — purchase requisitions, purchase orders, supplier invoices, journals, capex requests — before workflow configuration commences. The authority matrix must be authorised by the appropriate governance authority (CFO, CEO, or Finance Director).

**ERP-CUS-008**  
**Tax Configuration Information:** The client's tax team provides all tax configuration requirements: SA VAT registration number; applicable VAT rates and tax classifications (standard-rated, zero-rated, exempt, out-of-scope); withholding tax requirements; and any industry-specific tax treatment. APPSolve configures Oracle ERP tax based on this information; it does not provide tax advice.

**ERP-CUS-009**  
**Statutory Compliance Responsibility:** The client's finance and tax team is responsible for ensuring Oracle ERP configuration meets applicable statutory and regulatory requirements: Companies Act reporting, SARS VAT/PAYE requirements, IFRS or GAAP compliance, and any industry-specific regulations. APPSolve configures Oracle ERP based on requirements provided by the client; it does not provide tax, legal, or audit advice.

**ERP-CUS-010**  
**Testing Participation:** The client's functional team and user community participate in CRP1, CRP2, and UAT. The client provides test data, supplies UAT testers, executes UAT scenarios, logs defects, and provides written sign-off at each testing milestone.

**ERP-CUS-011**  
**Training Delivery:** The client is responsible for end-user training delivery, scheduling, communication, and adoption measurement. APPSolve trains the client's trainers (TTT); the client's trainers deliver to end users. The client provides training venue, equipment, and scheduling logistics.

**ERP-CUS-012**  
**Change Management:** Internal change management — communicating the ERP project to employees, managing transition from the legacy system, addressing adoption challenges, and measuring post-go-live adoption — is the client's leadership and HR responsibility. APPSolve provides implementation expertise; it does not run change management programmes.

---

## 84. Exclusions

**ERP-EXC-001**  
**Oracle Fusion Global Payroll:** Native Oracle payroll processing (gross-to-net calculation, payslip generation, PAYE submission) is excluded. South African payroll is managed by a third-party payroll provider (PaySpace, Sage 300 People, VIP Premier, or equivalent) integrated via OIC.

**ERP-EXC-002**  
**Oracle Fusion Expenses:** Employee expense claim management (Oracle Fusion Expenses Cloud Service) is excluded from base ERP scope unless explicitly included in the Oracle BOM. Where Oracle Expenses is required, it is separately licensed and separately scoped.

**ERP-EXC-003**  
**SARS eFiling Integration:** SARS eFiling integration is not an APPSolve standard ERP capability and is excluded unless specifically scoped as a custom integration (see ERP-INT-005). Oracle Fusion ERP does not integrate natively with the SARS eFiling portal. VAT201, PAYE EMP201, and provisional tax return submission are the client's tax team's responsibility. Tax reporting data extracts from Oracle OTBI to support the client's eFiling process may be included where explicitly listed in the proposal.

**ERP-EXC-004**  
**Formal SoD Analysis and Remediation:** Systematic SoD conflict identification, user access risk reporting, and SoD remediation using Oracle Access Controls Governor, Fastpath, or equivalent is excluded from base scope.

**ERP-EXC-005**  
**Oracle Supplier Portal:** Supplier self-service for invoice submission, PO acknowledgement, and supplier profile management is excluded. Requires separate Oracle licence and separately scoped OIC integration.

**ERP-EXC-006**  
**Oracle Fusion Risk Management (Advanced Controls):** Oracle's risk management and financial reporting compliance product is separately licensed and excluded from base ERP scope.

**ERP-EXC-007**  
**Legacy System Decommissioning:** Shutdown, data archiving, and decommissioning of the client's legacy ERP system after Oracle go-live is the client's responsibility and is excluded from this engagement.

**ERP-EXC-008**  
**Parallel Running:** Simultaneous operation of the legacy ERP and Oracle Fusion ERP post-go-live is excluded from base scope. See ERP-CUT-005.

**ERP-EXC-009**  
**Business Process Redesign:** Designing new or fundamentally different business processes is excluded. APPSolve configures Oracle ERP to support the agreed future-state processes confirmed in Scope and Design. Business process redesign consulting is separate from ERP implementation.

**ERP-EXC-010**  
**Invoice OCR and Intelligent Document Capture:** Automated invoice image capture, OCR data extraction, and AI-powered invoice processing are excluded from base scope. Standard AP scope is manual invoice entry.

**ERP-EXC-011**  
**Oracle Revenue Management Cloud (IFRS 15 / ASC 606 Complex Scenarios):** Complex revenue recognition — multiple-element arrangements, variable consideration, licence vs service distinction, contract modification accounting — may require Oracle Revenue Management Cloud (separately licensed). Standard Oracle AR revenue recognition is included; IFRS 15 complex scenarios require assessment.

**ERP-EXC-012**  
**Audit Deliverables and CAAT Reports:** Producing audit deliverables, Computer Assisted Audit Techniques (CAAT) reports, or auditor-specific testing reports for external or internal auditors is excluded. Standard Oracle OTBI reports are available for audit support; bespoke audit deliverables are not in implementation scope.

---

## BU Lead Decisions Applied — All Items Closed

| Decision ID | Assumption | Change Applied | Date |
|---|---|---|---|
| BU-ERP-001 | ERP-GL-001 | Secondary ledgers explicitly excluded from base scope unless named in proposal; separately assessed and priced | 2026-06-15 |
| BU-ERP-002 | ERP-GL-006 | Intercompany accounting excluded from base GL scope; basic balancing segment design may be included; full intercompany scope requires separate engagement | 2026-06-15 |
| BU-ERP-003 | ERP-AP-003 | Three-way match confirmed as APPSolve default; two-way match only where Receiving not in BOM or client confirms process | 2026-06-15 |
| BU-ERP-004 | ERP-FA-002 | Opening balance only confirmed as standard (asset cost / NBV / accumulated depreciation); current asset register required from customer before migration; historical transactions excluded | 2026-06-15 |
| BU-ERP-005 | ERP-CUT-005 | Parallel running excluded by default; short controlled validation period (5–10 days, trial balance only) may be included if explicitly stated in proposal; full parallel close cycles excluded unless separately scoped | 2026-06-15 |
| BU-ERP-006 | ERP-INT-005 / ERP-EXC-003 | SARS eFiling integration excluded unless specifically scoped as custom integration; tax reporting data extracts via OTBI may be included where explicitly listed | 2026-06-15 |
| BU-ERP-007 | ERP-DAT-006 | Two mock migrations plus one final production migration confirmed as standard base scope; additional cycles require change control | 2026-06-15 |
| BU-ERP-008 | ERP-SEC-006 | SSO excluded by default; Azure AD/Entra ID SSO may be included as separately listed configuration activity where explicitly scoped; other IdPs assessed per environment | 2026-06-15 |

---

*ERP_ASSUMPTIONS_V1.0 | WP11D-A — Oracle ERP Assumptions Approval | Approved 2026-06-15 | BU Lead — Oracle Practice*  
*123 assumptions / exclusions / dependencies / constraints / responsibilities across Sections 66–84*  
*Standalone pack — load alongside OIC pack for integrations; alongside HCM Base for combined projects | Governed under: 08_Commercial/ASSUMPTION_GOVERNANCE.md*
