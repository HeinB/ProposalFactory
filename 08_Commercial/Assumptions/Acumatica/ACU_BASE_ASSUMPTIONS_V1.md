---
document_id: ACU-BASE-ASSUMPTIONS-V1
title: "APPSolve Acumatica Base Assumption Pack"
version: "1.0-Approved"
status: "Approved v1.0"
created: "2026-06-16"
created_by: "WP11I — Acumatica Base Assumption Pack"
approved_by: "Acumatica BU Lead"
approved_date: "2026-06-18"
approval_programme: "WP15C"
pack_code: ACU
section_range: "120–139"
assumption_count: 152
approved_for_reuse: true
lifecycle_status: APPROVED
applies_to:
  - Acumatica ERP implementations
  - Acumatica cloud SaaS deployments
  - Acumatica upgrades and migrations
  - Acumatica managed services (AMS)
  - Acumatica + PaySpace payroll integration
  - Acumatica + BeBanking integration
bu_lead_decisions_applied:
  - BU-ACU-001
  - BU-ACU-002
  - BU-ACU-003
  - BU-ACU-004
  - BU-ACU-005
  - BU-ACU-006
  - BU-ACU-007
  - BU-ACU-008
  - BU-ACU-009
  - BU-ACU-010
  - BU-ACU-011
  - BU-ACU-012
  - BU-ACU-014
  - BU-ACU-015
bu_lead_decisions_pending: []
---

# APPSolve Acumatica Base Assumption Pack

**Pack:** ACU | **Sections:** 120–139 | **Assumptions:** 152 | **Status:** Approved v1.0 | **Approved:** 2026-06-18 (WP15C) | **approved_for_reuse: Yes**

This pack defines the standard assumptions governing APPSolve's delivery of Acumatica ERP engagements. All assumptions in this pack apply to every Acumatica proposal and SOW as the base layer. Module-specific and integration-specific packs layer on top of this base. This pack is the Acumatica equivalent of the Oracle HCM Base pack — it is always loaded first for any Acumatica engagement.

**Scope:** Acumatica cloud SaaS implementations, upgrades, data migrations, and managed services. Applies to all Acumatica modules (Financials, Distribution, Manufacturing, CRM, Field Services, Project Accounting). Does NOT apply to Acumatica on-premises deployments (APPSolve does not deliver on-premises Acumatica).

**Assumption Principles:** Assume simplest reasonable cloud SaaS implementation. These assumptions protect APPSolve from scope creep in customisation, legacy data migration, payroll integration, multi-entity configuration, user training, and post-go-live support.

---

## Section 120 — ACU-GEN: General Engagement Scope

**ACU-GEN-001.** APPSolve's Acumatica engagement scope is limited to the modules, entities, and workstreams explicitly named in the Statement of Work. Any Acumatica module, business entity, or business process not named in the SOW is out of scope. If the client identifies additional scope during delivery, these items are treated as Change Requests.

**ACU-GEN-002.** APPSolve implements Acumatica as a cloud SaaS platform. APPSolve does not deploy, configure, or support Acumatica on-premises installations. Clients requiring on-premises deployment must engage a different implementation partner. Any request to modify this scope is a category error, not a Change Request.

**ACU-GEN-003.** Acumatica licences are procured by APPSolve as a Value-Added Reseller (VAR) or directly by the client. Unlike most ERP platforms, Acumatica's SaaS subscription is priced on a resource-consumption basis — not per named user or per concurrent user. The number of system users does not drive the licence cost; the allocated computing resource tier does. Unlimited users can be added to an Acumatica subscription without additional per-user licence fees; however, if resource consumption exceeds the subscribed tier, a tier upgrade is required. The appropriate resource tier is confirmed before implementation commences based on estimated transaction volumes and user activity levels. APPSolve cannot begin implementation configuration until the Acumatica licence is active in the client's tenant.

**ACU-GEN-004.** APPSolve assumes the client has identified and committed named business owners for each Acumatica module in scope. Business owners are accountable for: approving configuration decisions, providing master data, completing User Acceptance Testing, and attending training sessions. Without committed business owners, APPSolve cannot progress key project milestones.

**ACU-GEN-005.** APPSolve's Acumatica implementation uses Acumatica's standard out-of-the-box functionality as the starting point for all business process designs. Customisation is considered only after a documented business justification confirms that the standard functionality does not meet the business requirement. Customisation for convenience or aesthetic preference is not approved by default.

**ACU-GEN-006.** APPSolve assumes the client's business processes will be adapted to align with Acumatica's standard workflows where feasible. Business process re-engineering to force Acumatica to replicate legacy system behaviour is out of scope unless explicitly included. The engagement is an Acumatica implementation, not a legacy system replication project.

**ACU-GEN-007.** APPSolve delivers Acumatica implementations using a structured methodology (Mobilise → Scope & Design → Configure → Validate → Deploy → Evolve). The client's project sponsor and project manager are required to participate in all milestone reviews and project governance meetings. Missed milestone reviews delay the project timeline and are documented as client-side delays.

**ACU-GEN-008.** APPSolve assumes a single Acumatica tenant for the engagement unless multiple tenants are explicitly included in the SOW. Multiple tenants (e.g., separate production tenants for subsidiary entities with different Acumatica licence contracts) are a separately scoped and separately priced item.

**ACU-GEN-009.** APPSolve is an Acumatica Gold Partner. All proposals and submissions citing APPSolve's Acumatica partner credentials must state "Acumatica Gold Partner." APPSolve does not hold Acumatica Gold Certified status — proposals must not cite "Gold Certified." [BU-ACU-009: RESOLVED WP14G 2026-06-18]

**ACU-GEN-010.** APPSolve appoints a Lead Consultant or Solution Architect as the primary APPSolve delivery contact for all Acumatica implementations. A dedicated APPSolve Project Manager is included where 3 or more Acumatica modules are in scope, or where the implementation spans more than one client business unit. For single-module or dual-module implementations, the Lead Consultant manages APPSolve-side delivery activities and the client's Project Manager coordinates overall project governance. Where a dedicated APPSolve PM is required and not pre-included in the proposal, PM resource is added to the SOW as a separate line item. [BU-ACU-014: RESOLVED WP15C 2026-06-18 — PM included for 3+ modules or multi-BU scope]

---

## Section 121 — ACU-ENV: Environments

**ACU-ENV-001.** The standard Acumatica implementation includes two environments: one Production tenant and one non-Production tenant (used for configuration, testing, and training). Separate environments for Development, User Acceptance Testing (UAT), Training, and Performance Testing are not assumed by default and are separately scoped if required.

**ACU-ENV-002.** Acumatica's cloud environment provisioning is managed by Acumatica and its hosting partners. APPSolve does not control Acumatica environment provisioning timelines. Delays in environment availability caused by Acumatica or its hosting partners are not APPSolve's responsibility and are documented as third-party delays.

**ACU-ENV-003.** Environment configuration activities (module activation, base configuration, user setup) begin once the non-Production environment is available. APPSolve provides a confirmed environment readiness checklist before configuration begins.

**ACU-ENV-004.** All configuration work is performed in the non-Production environment first. Configuration is promoted to Production only after: client UAT sign-off, data migration validation, and go-live approval from the client's project sponsor. APPSolve does not configure Production environments directly without non-Production sign-off.

**ACU-ENV-005.** APPSolve assumes Acumatica will be accessed by client users through a standard web browser (Chrome or Edge recommended). Mobile app access for Acumatica is available through the Acumatica mobile app. APPSolve does not configure or support custom mobile applications built on top of Acumatica.

**ACU-ENV-006.** Performance testing of the Acumatica environment (load testing, stress testing) is not included in the standard implementation. If the client requires performance testing, it is a separately scoped activity. Acumatica's cloud infrastructure SLAs are governed by Acumatica's hosting agreements, not APPSolve's delivery scope.

---

## Section 122 — ACU-CFG: Configuration and Customisation

**ACU-CFG-001.** APPSolve configures Acumatica using Acumatica's standard Low-Code/No-Code customisation framework (Acumatica Customisation Project, screen customisations, generic inquiries, reports via Report Designer). Direct database modifications, SQL-level changes, and modifications to Acumatica's core application source code are never performed.

**ACU-CFG-002.** Custom development beyond the Acumatica Low-Code/No-Code framework (e.g., custom web service integrations, custom API endpoints, custom workflow extensions requiring C# development) is treated as a customisation scope item and priced separately. The volume and complexity of custom development items are confirmed before the SOW is signed.

**ACU-CFG-003.** Generic Inquiries (GIs) are used as the standard tool for custom data views, lookup screens, and reporting source queries. APPSolve delivers a set of GIs defined during Scope & Design. GIs outside the agreed set are a Change Request. The client's operational team will maintain GIs post-handover using Acumatica's GI builder.

**ACU-CFG-004.** Acumatica Push Notifications and Business Events are configured for defined automated workflow triggers identified during Scope & Design. Automations outside the agreed set are a Change Request. Complex multi-step automation requiring Acumatica Workflow Engine customisation is separately priced.

**ACU-CFG-005.** Report Designer is used for all standard Acumatica reports. APPSolve delivers a set of configured reports defined during Scope & Design. Custom reports outside the agreed set are a Change Request. SSRS, Power BI, or external BI tool integration is out of scope for the standard Acumatica implementation and requires a separate analytics engagement.

**ACU-CFG-006.** Acumatica screen customisation (adding or modifying fields, relabelling, reordering) is performed only where the business requirement cannot be met by standard configuration. Each screen customisation is individually scoped. The number of screen customisations is agreed and capped in the SOW — additional customisations are Change Requests.

**ACU-CFG-007.** Acumatica Dashboards are configured using standard Acumatica dashboard widgets connected to Generic Inquiries. APPSolve delivers a defined set of dashboards per role agreed during Scope & Design. Custom Power BI or third-party analytics dashboards embedded in Acumatica are out of scope for the standard implementation.

**ACU-CFG-008.** Configuration documentation (Acumatica Configuration Workbook) is delivered at project close. The Configuration Workbook captures: module activations, numbering sequences, approval workflows, configuration decisions, and custom GIs/reports/dashboards. The Configuration Workbook is a standard deliverable and is the client's operational reference for system maintenance.

**ACU-CFG-009.** Single Sign-On (SSO) integration between Acumatica and the client's identity provider (Microsoft Azure AD, Okta, Google Workspace, or similar) is not included in the standard implementation. SSO requires the client's IT administrator to configure the identity provider and exchange SAML metadata with Acumatica. APPSolve assists with Acumatica-side SSO configuration where explicitly included in the SOW and subject to the client's IT team providing the required identity provider configuration.

---

## Section 123 — ACU-DAT: Data Migration

**ACU-DAT-001.** Data migration scope is limited to the data entities explicitly named in the Data Migration Plan. The Data Migration Plan is a mandatory deliverable agreed before migration execution begins. Data entities not named in the Data Migration Plan are out of scope. Adding new entities after the Data Migration Plan is signed is a Change Request.

**ACU-DAT-002.** APPSolve provides Acumatica Import Scenarios and data migration templates for the agreed data entities. The client is responsible for extracting data from the legacy system, populating the migration templates, and delivering the populated templates to APPSolve by the agreed date. APPSolve does not extract data from the client's legacy system.

**ACU-DAT-003.** APPSolve performs data validation on the client-provided data: format validation, referential integrity checks, and business rule validation against Acumatica's data model. APPSolve does not cleanse, de-duplicate, or enrich the client's data. Data quality is the client's responsibility. Data quality issues identified during validation are returned to the client for correction.

**ACU-DAT-004.** The standard APPSolve data migration approach includes: one pilot migration (into the non-Production environment), one dress rehearsal migration (simulating the production migration sequence and timing), and one final migration (production go-live). Additional migration cycles are a Change Request.

**ACU-DAT-005.** Data migration covers opening balances as at the agreed cut-over date: GL opening trial balance, open AR invoices and receipts, open AP invoices and payments, open purchase orders, open sales orders, and current inventory on-hand quantities (where inventory is in scope). Historical transaction migration (prior-period journals, closed invoices, historical purchase or sales history) is not included by default and must be explicitly included as a separately scoped item. Historical transaction migration significantly increases migration effort and data quality risk. [BU-ACU-010: RESOLVED WP15C 2026-06-18 — opening balances and open items only by default]

**ACU-DAT-006.** Active master data is migrated by default. The definition of "active" is confirmed with the client during Scope & Design (e.g., customers active in the last 24 months; inventory items with positive stock on hand). Inactive, archived, or superseded master data is excluded from the migration unless explicitly included.

**ACU-DAT-007.** The client provides a formal sign-off on the migrated data in the non-Production environment before the final Production migration is executed. Sign-off confirms: data completeness, opening balance accuracy, and master data integrity. The final Production migration does not proceed without sign-off.

**ACU-DAT-008.** APPSolve provides a data migration runbook for the production go-live migration event, including estimated timings, rollback decision criteria, and sign-off checkpoints. The client's project sponsor participates in the go-live migration event and is available throughout the migration window.

**ACU-DAT-009.** Post-go-live data corrections (errors in migrated data identified after go-live) are the client's operational responsibility to assess and prioritise. APPSolve supports data correction activities during the post-go-live hypercare period within the agreed hypercare scope. Data corrections requiring a new migration run after go-live are a Change Request.

**ACU-DAT-010.** Document attachments from the legacy system (PDF invoices, scanned receipts, signed contracts, delivery notes, correspondence, and image files attached to legacy transactions or master records) are not migrated to Acumatica as part of the standard data migration. Acumatica's native file attachment capability allows new documents to be attached from go-live forward. Migration of legacy document attachments is a separately scoped, high-effort activity and must be explicitly included in the SOW if required.

**ACU-DAT-011.** Notes, inline comments, memo fields, and internal descriptions attached to individual transactions in the legacy system are not migrated to Acumatica. Only structured transactional data defined in APPSolve's data migration templates is migrated. Post-go-live, notes can be added to Acumatica records using Acumatica's standard notes and file attachment features.

**ACU-DAT-012.** Legacy system audit trail and transaction change history are not migrated to Acumatica. Acumatica maintains its own audit trail from go-live forward. For regulatory or audit continuity purposes, clients must retain access to the legacy system or archive the legacy audit data separately. APPSolve recommends clients confirm their data retention obligations with their auditors before decommissioning the legacy system.

---

## Section 124 — ACU-FIN: Financials

**ACU-FIN-001.** APPSolve configures Acumatica Financials (General Ledger, Accounts Payable, Accounts Receivable, Cash Management) as the core financial module for all Acumatica implementations. The Financials module is the mandatory base for all Acumatica implementations — it cannot be excluded.

**ACU-FIN-002.** The client designs the Chart of Accounts (CoA) before configuration begins. APPSolve configures the CoA in Acumatica according to the client's approved design. APPSolve may provide CoA design guidance but does not design the CoA on behalf of the client. CoA changes after design sign-off are a Change Request.

**ACU-FIN-003.** Acumatica Financial Periods (fiscal year, fiscal periods) are configured to the client's confirmed fiscal year structure. Period structure changes after configuration sign-off (e.g., switching from calendar to non-calendar year) are a significant Change Request requiring full reconfiguration.

**ACU-FIN-004.** Multi-currency is configured where the client operates in multiple currencies. The client confirms: functional currency per entity, currencies to be enabled, and foreign exchange rate source (manual entry or OER/Xignite feed). APPSolve configures the confirmed currencies and rate mechanism. Live FX rate feed integration with a third-party provider is separately scoped.

**ACU-FIN-005.** Bank account configuration requires the client to provide: bank name, account number, currency, and branch/sort code for each bank account before configuration begins. Bank reconciliation configuration is included for all configured bank accounts. Direct bank feed integration (automatic statement import from the bank) requires a bank-specific integration and is separately scoped.

**ACU-FIN-006.** Accounts Payable configuration includes: supplier master setup, payment terms, approval workflows for invoices and payments, and standard AP reports. AP automation (OCR invoice capture, automated invoice matching) is separately licensed and separately scoped. AP automation is not assumed by default.

**ACU-FIN-007.** Accounts Receivable configuration includes: customer master setup, payment terms, AR invoice templates, cash receipt application, and standard AR reports. Credit management, collections automation, and customer portal self-service are separately scoped if required.

**ACU-FIN-008.** Fixed Assets management in Acumatica (asset register, depreciation, disposal) is included where explicitly stated in the SOW. Asset register migration (historical asset data, accumulated depreciation) is a separately scoped data migration item. Impairment testing, revaluation, and IFRS 16 lease accounting are out of scope unless explicitly included.

**ACU-FIN-009.** Tax configuration for South Africa (VAT, WHT) is included as a standard configuration item. SARS eFiling integration is out of scope — tax submissions are prepared in Acumatica and filed by the client directly via SARS eFiling. International tax jurisdictions (non-SA VAT, US sales tax, EU VAT) require separate specialist configuration and are out of scope for the standard South African Acumatica implementation.

**ACU-FIN-010.** Period-end close procedures (month-end, year-end) are documented in the operations runbook. APPSolve facilitates the first month-end close post go-live as part of the standard hypercare period. The client's finance team is trained to execute subsequent period-end close procedures independently.

**ACU-FIN-011.** APPSolve configures Acumatica accounts receivable invoice templates to comply with South Africa's VAT Act requirements for a valid tax invoice, including all mandatory fields (supplier name, supplier VAT registration number, "Tax Invoice" heading, sequential invoice number, invoice date, description of supply, taxable amount, VAT amount, and total amount including VAT). Standard Acumatica invoice templates are used as the configuration baseline. Custom invoice template design beyond standard SARS compliance (branded layouts, non-standard field arrangements, or multi-page formats) is separately scoped.

---

## Section 125 — ACU-ORG: Organisation Structure

**ACU-ORG-001.** The number of Acumatica legal entities (companies/branches) configured is confirmed in the SOW before implementation begins. Each additional legal entity beyond the base scope is a separately scoped item with its own configuration effort estimate. The entity count directly affects implementation effort and licence requirements.

**ACU-ORG-002.** APPSolve assumes the client's legal entity structure is finalised before configuration begins. Adding or changing legal entities after the organisation structure is signed off is a Change Request. Legal entity changes during implementation are among the highest-impact Change Requests.

**ACU-ORG-003.** Inter-company transactions between Acumatica entities are configured where confirmed in the SOW. The volume and types of inter-company transactions (stock transfers, cost allocations, management fees, loans) are defined during Scope & Design. Complex inter-company netting and reconciliation workflows are separately scoped.

**ACU-ORG-004.** Branch accounting (sub-entity reporting within a single legal entity) is configured as part of the standard Financials configuration. The chart of accounts supports branch segmentation through Acumatica's subaccount structure. APPSolve configures the subaccount structure according to the client's approved design.

**ACU-ORG-005.** Acumatica's approval workflow engine is configured for the approval processes confirmed during Scope & Design. The standard scope covers: purchase requisition approval, purchase order approval, AP invoice approval, and expense claim approval. Additional approval processes are a Change Request. Complex multi-level, multi-condition approval trees are separately scoped.

**ACU-ORG-006.** Consolidated financial reporting across multiple Acumatica entities (consolidated profit and loss statement, consolidated balance sheet, group-level management accounts) requires consolidation ledger configuration and inter-company elimination rules. Consolidated reporting is not assumed by default for any multi-entity implementation and is always separately scoped. The number of entities, elimination rules, and reporting periods covered by consolidation are confirmed during Scope & Design and documented in the SOW. [BU-ACU-015: RESOLVED WP15C 2026-06-18 — consolidated reporting always separately scoped]

---

## Section 126 — ACU-INV: Inventory and Warehouse

**ACU-INV-001.** Inventory management configuration is included where the Acumatica Inventory module is in scope per the SOW. Inventory configuration covers: item class setup, warehouse/location structure, unit of measure definitions, lot/serial tracking (where applicable), and standard inventory valuation method (FIFO, average cost, or standard cost — confirmed during Scope & Design).

**ACU-INV-002.** Warehouse configuration covers the warehouses explicitly named in the SOW. Each additional warehouse not in the SOW is a Change Request. Multi-warehouse and multi-bin location structures are included where confirmed. Third-party warehouse management systems (WMS) integration is separately scoped.

**ACU-INV-003.** Inventory opening balances (quantity on hand and cost) are migrated as at the agreed cut-over date. APPSolve migrates the agreed inventory snapshot. Historic inventory transactions are not migrated. Inventory accuracy at cut-over is the client's responsibility — APPSolve validates the migration against the client-provided inventory count.

**ACU-INV-004.** Barcode and scanning integration for warehouse operations (using Acumatica's WMS functionality or third-party devices) is separately scoped. Standard Acumatica inventory management uses manual data entry or Acumatica's mobile warehouse app. Complex WMS integrations with conveyor systems, automated storage, or RFID are out of scope for the standard implementation.

**ACU-INV-005.** Replenishment and demand planning configuration in Acumatica (min/max, reorder points, demand forecasting) is included where explicitly stated in the SOW. Advanced supply chain planning (APS) and external demand forecasting tool integration are out of scope for the standard Acumatica implementation.

---

## Section 127 — ACU-PUR: Purchasing and Procurement

**ACU-PUR-001.** Purchase Requisition and Purchase Order management is configured as part of the standard Acumatica Financials or Distribution scope. Procurement workflow configuration (requisition creation, PO approval, goods receipt, three-way match) is included. Three-way match (PO + GRN + invoice) is the default matching standard.

**ACU-PUR-002.** Supplier master configuration is included. The client provides the confirmed supplier master data file before migration. APPSolve configures supplier payment terms, payment methods, bank details (for EFT payments), and tax categories. Supplier self-service portal configuration is out of scope unless explicitly included.

**ACU-PUR-003.** Contract management in Acumatica (blanket POs, supplier contracts, price agreements) is included where explicitly stated in the SOW. Complex contract lifecycle management (CLM) integration with a specialist CLM tool is out of scope.

**ACU-PUR-004.** E-procurement or supplier punchout integration (e.g., SAP Ariba, Coupa punchout) is out of scope for the standard implementation. APPSolve does not configure punchout catalogues. If the client requires e-procurement integration, this is a separately scoped integration item.

---

## Section 128 — ACU-PAY: PaySpace Payroll Integration

**ACU-PAY-001.** Payroll is not a native Acumatica module in South Africa. APPSolve integrates Acumatica with PaySpace as the standard South African payroll system. The integration method is confirmed at pre-sales based on the client's PaySpace licence tier and IT environment. Payroll processing, PAYE calculations, UIF/SDL deductions, and IRP5/EMP501 submissions are PaySpace's scope — not Acumatica's and not APPSolve's payroll scope. [BU-ACU-001: RESOLVED WP15C 2026-06-18 — integration method confirmed at pre-sales per client PaySpace licence tier]

**ACU-PAY-002.** The Acumatica-PaySpace integration scope covers: payroll journal postings from PaySpace to Acumatica GL (ensuring payroll costs are reflected in Acumatica's general ledger). The integration does not cover: individual employee pay slip data, leave balances, or HR management information in Acumatica. These remain in PaySpace.

**ACU-PAY-003.** APPSolve assumes the client is an active PaySpace subscriber with a confirmed PaySpace account before integration design begins. APPSolve does not procure, set up, or configure PaySpace. PaySpace configuration and payroll processing are PaySpace's (or the client's PaySpace implementation partner's) responsibility.

**ACU-PAY-004.** The Acumatica-PaySpace integration method is confirmed at pre-sales based on the client's PaySpace licence tier and IT environment. APPSolve recommends API integration where the client's PaySpace licence includes REST API access; file-based integration (automated or scheduled export/import) is used where API access is unavailable. The confirmed integration method is documented in the SOW before implementation begins. Available methods: (a) REST API integration — preferred where PaySpace API access is included in the client's licence; (b) automated file-based integration — scheduled export from PaySpace, scheduled import to Acumatica; (c) manual journal import using Acumatica's Import Scenarios — lowest-effort option for low-frequency payroll runs. The integration method is confirmed and locked before SOW sign-off. [BU-ACU-001: RESOLVED WP15C 2026-06-18 — method confirmed at pre-sales per client PaySpace licence tier; API preferred]

**ACU-PAY-005.** Payroll General Ledger mapping (PaySpace payroll codes mapped to Acumatica GL accounts, departments, and branches) requires input from both the client's payroll team (PaySpace pay component codes) and finance team (GL account structure). APPSolve cannot design the GL mapping without both inputs. Mapping sign-off is a mandatory milestone before integration configuration begins.

**ACU-PAY-006.** Integration testing for Acumatica-PaySpace requires a live PaySpace test environment with representative payroll data. The client's PaySpace administrator must provide test environment access and coordinate PaySpace-side testing activities. APPSolve cannot execute integration testing without PaySpace test environment access.

**ACU-PAY-007.** PaySpace is the system of record for all payroll data (employee records, earnings, deductions, tax calculations, leave). Acumatica is the system of record for financial accounting. The integration is one-directional for payroll: PaySpace → Acumatica GL. Acumatica does not send HR or payroll data to PaySpace.

**ACU-PAY-008.** APPSolve's standard Acumatica payroll integration target is PaySpace. Clients using alternative South African payroll systems (VIP Payroll, Sage Business Cloud Payroll, Sage Payroll 300, SimplePay, or other providers) are assessed for integration feasibility at pre-sales before SOW sign-off. Where API or file-based integration with a non-PaySpace system is technically feasible, payroll integration is delivered as a Custom Integration and is separately scoped and priced at custom integration rates. Where integration with the client's payroll system is not technically feasible, payroll integration is excluded from the Acumatica implementation scope. Non-PaySpace payroll integration is not governed by the ACU-PAY assumptions — it requires a separate integration design and assessment. [BU-ACU-011: RESOLVED WP15C 2026-06-18 — PaySpace is standard; non-PaySpace payroll assessed at pre-sales as custom integration]

---

## Section 129 — ACU-CRM: CRM and Customer Management

**ACU-CRM-001.** Acumatica CRM configuration is included where the CRM module is in scope per the SOW. CRM scope covers: Lead and Opportunity management, Customer/Contact master, Activity tracking, and Case management. Advanced CRM features (marketing campaign management, email marketing, customer portals) are separately scoped.

**ACU-CRM-002.** CRM data migration (leads, contacts, opportunities, historical activities) from a legacy CRM (Salesforce, HubSpot, Zoho, Microsoft Dynamics) requires a data extraction from the legacy system. The client extracts CRM data and provides it in the APPSolve-supplied migration template. APPSolve does not directly connect to or extract data from third-party CRM systems.

**ACU-CRM-003.** Acumatica CRM integration with Microsoft 365 (Outlook email synchronisation, calendar integration) is included where explicitly stated in the SOW. The client's Microsoft 365 tenant administrator must approve and configure the Microsoft 365 integration permissions. APPSolve cannot configure the Microsoft 365 integration without Microsoft 365 admin access.

**ACU-CRM-004.** Acumatica CRM does not include a customer-facing self-service portal as part of the standard implementation. If the client requires a customer portal (for case submission, invoice viewing, order status), this is a separately scoped Acumatica Portal configuration item.

---

## Section 130 — ACU-PRJ: Project Accounting

**ACU-PRJ-001.** Acumatica Project Accounting configuration is included where the Project Accounting module is in scope per the SOW. Project Accounting scope covers: project template setup, project budget configuration, time and expense entry, project billing, and project profitability reporting.

**ACU-PRJ-002.** APPSolve configures the project cost code structure, project tasks, and project budget categories based on the client's confirmed project management methodology. The client provides the project structure definition before configuration begins. Complex multi-level work breakdown structures (WBS) are supported by Acumatica's Project Accounting module and are configured per the agreed design.

**ACU-PRJ-003.** Time entry configuration for project time tracking (employee time against project tasks) is included where time-based billing is in scope. The client confirms the time entry approval workflow before configuration. Mobile time entry via the Acumatica mobile app is available as standard functionality.

**ACU-PRJ-004.** Project billing (time-and-materials billing, fixed-price milestone billing, cost-plus billing) is configured per the billing models confirmed during Scope & Design. APPSolve supports Acumatica's standard billing models. Custom billing logic outside Acumatica's standard billing types is separately scoped.

**ACU-PRJ-005.** Project Accounting integration with Acumatica Payroll (for labour cost allocation from PaySpace to projects) follows the same integration model as the standard ACU-PAY integration. The PaySpace-to-Acumatica GL journal must carry project coding for project cost allocation to work. Project costing from payroll requires confirmed GL mapping that includes the project dimension.

---

## Section 131 — ACU-MFG: Manufacturing

**ACU-MFG-001.** Acumatica Manufacturing configuration is included where the Manufacturing module is in scope per the SOW. The manufacturing scope is confirmed during Scope & Design and covers the manufacturing processes explicitly named. APPSolve implements Acumatica Manufacturing for discrete manufacturing (Bill of Materials, Production Orders, Shop Floor). Process manufacturing and repetitive manufacturing require separate assessment.

**ACU-MFG-002.** Bill of Materials (BOM) data migration requires the client to provide the complete BOM structure in the APPSolve-supplied template. BOM data is typically the most complex master data migration in a manufacturing implementation. Incomplete or inaccurate BOM data significantly impacts configuration progress. The client's engineering or production team must validate BOM data before migration.

**ACU-MFG-003.** Production order management (work order creation, shop floor scheduling, labour and material issue, production order costing) is configured per the client's confirmed production process. Shop floor data collection via barcode scanning or IoT integration is separately scoped.

**ACU-MFG-004.** Acumatica's Material Requirements Planning (MRP) is included where explicitly stated in the SOW. MRP configuration requires confirmed lead times, reorder quantities, and supplier data. APPSolve configures MRP parameters during Scope & Design. Advanced planning and scheduling (APS) tools that replace or supplement Acumatica MRP are out of scope.

**ACU-MFG-005.** Quality management (quality control holds, inspection orders, non-conformance reports) in Acumatica is included where explicitly stated in the SOW. Third-party quality management system (QMS) integration is separately scoped.

---

## Section 132 — ACU-INT: Integration

**ACU-INT-001.** Acumatica integrations with third-party systems are in scope only where explicitly named in the SOW. Every integration is individually scoped. The standard integration complexity tiers apply (aligned to AMS Pack definitions): Simple — standard Acumatica connector or straightforward API call with no transformation; Standard — custom API with field mapping, data transformation, or schedule logic; Complex — multi-step workflow, event-driven integration, complex transformation logic, or bi-directional real-time integration. Integration tier determines effort and pricing. Tier is confirmed during Scope & Design. [BU-ACU-002: RESOLVED WP15C 2026-06-18 — AMS Pack tier definitions adopted for Acumatica: Simple / Standard / Complex]

**ACU-INT-002.** Acumatica's native REST API is used for all real-time integrations. File-based integrations use Acumatica's Import Scenarios or scheduled file exchange. The integration method for each integration point is confirmed during Scope & Design. APPSolve does not use SOAP-based integration for new Acumatica integrations.

**ACU-INT-003.** BeBanking Host-to-Host banking integration with Acumatica is included where BeBanking is in scope per the SOW. The BeBanking-Acumatica integration is a separately scoped item — it is not included in the standard Acumatica Base pack. BeBanking integration scope, banking partners, and payment file formats are confirmed in the BeBanking scope definition.

**ACU-INT-004.** E-commerce platform integration (Shopify, WooCommerce, Magento) with Acumatica is separately scoped. APPSolve does not include e-commerce integration as a standard Acumatica implementation item. Standard Acumatica connectors exist for popular e-commerce platforms; however, each integration requires individual scoping due to the variation in product catalogue, order management, and fulfilment workflow complexity.

**ACU-INT-005.** Third-party logistics (3PL) integration with Acumatica is separately scoped. If the client uses a 3PL provider for fulfilment, the 3PL integration (stock receipt, dispatch notification, inventory sync) requires individual scoping and is not a standard Acumatica implementation item.

**ACU-INT-006.** Integration testing requires the third-party system's test environment to be available and stable. APPSolve cannot execute integration testing if the third-party test environment is unavailable. Third-party test environment unavailability is documented as a third-party delay. APPSolve adjusts the project schedule to accommodate third-party delays, and the client bears the cost of any schedule extension caused by third-party delays.

**ACU-INT-007.** Post-go-live monitoring of Acumatica integrations (API call health, file transfer completion, import/export success and failure notifications) is the client's operational responsibility unless explicitly included in an Acumatica AMS SOW. During implementation, APPSolve configures Acumatica's standard integration error notification mechanisms (email alerts, failed import notifications, Business Event triggers for integration failures). Proactive integration monitoring, automated alerting to APPSolve, and integration error log review as an operational activity are AMS scope items and are not included in the standard implementation.

**ACU-INT-008.** Where Oracle Integration Cloud (OIC) is available in the client's environment and proposed by APPSolve as the middleware layer for Acumatica integrations, the OIC Assumption Pack (OIC-ASSUMPTIONS-V1) governs the OIC components of the integration. The ACU-INT assumptions govern the Acumatica-side integration configuration. The decision to use OIC as Acumatica integration middleware is confirmed at pre-sales and documented in the SOW. Where OIC is not proposed, Acumatica's native REST API and Import Scenarios are used as per ACU-INT-002.

---

## Section 133 — ACU-REP: Reporting and Analytics

**ACU-REP-001.** All factory-delivered Acumatica reports for each module in scope are included in the standard implementation. "Standard reports" means the full Acumatica factory report library for the activated modules — APPSolve configures, activates, and sets permissions for these reports as part of module configuration. Custom reports developed using Acumatica Report Designer (i.e., net-new reports not part of the Acumatica factory library) are separately scoped. [BU-ACU-006: RESOLVED WP15C 2026-06-18 — standard = all factory Acumatica reports for modules in scope; no curated list required]

**ACU-REP-002.** Generic Inquiries (GIs) are APPSolve's primary tool for ad-hoc data views. APPSolve delivers a defined set of GIs during Scope & Design. The client's super-users are trained to create and modify GIs after go-live. APPSolve does not create unlimited GIs on demand during or after the implementation.

**ACU-REP-003.** Acumatica's built-in dashboards are configured using standard Acumatica widgets and GI sources. APPSolve configures role-based dashboards as defined during Scope & Design. The number of dashboards is agreed and documented in the SOW. Additional dashboards beyond the agreed set are a Change Request.

**ACU-REP-004.** External BI tool integration (Power BI, Tableau, QlikView, or any third-party analytics platform) with Acumatica data is not included in the standard implementation and is always separately scoped. If the client requires BI tool connectivity to Acumatica data, this is a separately scoped integration item delivered using Acumatica's OData feed or Direct SQL access (where Acumatica's database access policy permits). BI connector configuration is quoted as a distinct line item and is never assumed within standard implementation scope. [BU-ACU-003: RESOLVED WP15C 2026-06-18 — BI tool integration always separately scoped; never in standard scope]

**ACU-REP-005.** Compliance reports (SARS VAT returns, management accounts, regulatory filings) are based on Acumatica's standard financial data. APPSolve configures Acumatica to support the preparation of these reports. APPSolve does not prepare or submit regulatory filings on the client's behalf — submissions are the client's responsibility.

---

## Section 134 — ACU-TRN: Training

**ACU-TRN-001.** APPSolve provides end-user training for all Acumatica modules in scope. Training is delivered to the client's named super-users and key users, not to all end users. The client's super-users are responsible for training remaining end users after APPSolve's training engagement concludes. Training for more than the agreed number of users is a Change Request.

**ACU-TRN-002.** APPSolve's standard Acumatica training delivery format is virtual facilitated training (Microsoft Teams or Zoom). Virtual facilitated training is the default for all Acumatica training sessions unless the client requests on-site delivery. On-site training is available at additional cost — travel and accommodation costs are billed separately at actual cost. Self-paced training via Acumatica Open University is recommended as a pre-session supplement for key users. [BU-ACU-007: RESOLVED WP15C 2026-06-18 — virtual facilitated training is the standard; on-site at additional cost]

**ACU-TRN-003.** APPSolve provides training materials (process guides and quick-reference cards) for the modules in scope. Training materials are provided in English. Materials in other languages are not included. Branded training materials with the client's company logo and terminology are separately scoped.

**ACU-TRN-004.** Acumatica Open University (Acumatica's self-paced online learning platform) is available to all Acumatica licence holders at no additional cost. APPSolve recommends that key users complete relevant Acumatica Open University courses before APPSolve's facilitated training sessions. Pre-training completion of Open University courses is strongly recommended but not mandated.

**ACU-TRN-005.** Training is conducted in the non-Production environment using representative data loaded during UAT. Training is not conducted in the Production environment. If the non-Production environment is unavailable for training (due to configuration activity), the training schedule is adjusted with the client.

**ACU-TRN-006.** Organisational change management (stakeholder communication, executive sponsorship, end-user adoption planning, and resistance management) is the client's responsibility. APPSolve's training delivery and documentation support the client's change management programme but do not replace it. Where the implementation involves significant process changes or large user populations, APPSolve recommends the client engage specialist change management support. Change management consulting services from APPSolve are separately scoped if required.

---

## Section 135 — ACU-UAT: Testing

**ACU-UAT-001.** User Acceptance Testing (UAT) is the client's responsibility. APPSolve provides: a UAT test plan framework, UAT test scenarios aligned to the configured business processes, a UAT defect log, and UAT support during the testing window. APPSolve does not execute UAT on behalf of the client.

**ACU-UAT-002.** The UAT test scenarios are prepared based on the business processes confirmed during Scope & Design. The client's UAT team is responsible for executing the test scenarios, recording actual results, and logging defects. APPSolve resolves defects classified as configuration defects within the UAT window. Scope changes identified during UAT are Change Requests.

**ACU-UAT-003.** APPSolve assumes a single UAT cycle with one remediation pass. If UAT requires more than one remediation cycle (e.g., because of significant scope changes identified during UAT, or because defect volume is high), additional UAT cycles are a Change Request.

**ACU-UAT-004.** Regression testing after configuration changes or Acumatica updates is the client's responsibility during and after UAT. APPSolve provides guidance on test scenarios for regression testing but does not execute regression testing after the UAT cycle is complete.

**ACU-UAT-005.** UAT sign-off (written client approval that UAT is complete and the system is accepted for go-live) is a mandatory project milestone. Go-live does not proceed without UAT sign-off from the client's project sponsor. APPSolve may proceed to go-live preparation in parallel with UAT finalisation if the open defect list contains only minor non-blocking items agreed in writing with the client.

---

## Section 136 — ACU-CUT: Cutover and Go-Live

**ACU-CUT-001.** Go-live cutover is a planned event with an agreed cutover window. APPSolve provides an Acumatica Go-Live Runbook covering: cutover sequence, data migration execution, parallel run activities (where applicable), go-live sign-off checklist, and rollback criteria. The runbook is reviewed and approved by the client's project sponsor before the cutover window begins.

**ACU-CUT-002.** Parallel run (operating both the legacy system and Acumatica simultaneously for a period after go-live) is excluded by default from all Acumatica implementations. Parallel run is a high-effort activity that requires double data entry and reconciliation across both systems. If the client requires a parallel run, it must be explicitly included in the SOW with a defined duration, defined scope, and defined reconciliation responsibilities. Where parallel run is in scope, APPSolve assists with the first parallel run reconciliation cycle only — subsequent cycles are the client's operational responsibility. [BU-ACU-005: RESOLVED WP15C 2026-06-18 — parallel run excluded by default; included only where explicitly in SOW]

**ACU-CUT-003.** The legacy system is the client's system. APPSolve does not control the legacy system and cannot guarantee that the legacy system will be available for parallel run or data extraction during the cutover window. Delays caused by legacy system unavailability during cutover are client-side delays.

**ACU-CUT-004.** Go-live date changes requested by the client after the project schedule is baselined are Change Requests. A client-initiated go-live delay of more than four weeks may require a project scope review and cost impact assessment.

**ACU-CUT-005.** APPSolve provides four (4) weeks of hypercare support after Acumatica go-live. Four weeks is the standard hypercare period for all Acumatica implementations, consistent with the BeBanking Base Pack and Oracle implementation standards. Hypercare covers: answering user queries, resolving configuration defects identified post-go-live, and providing guidance on Acumatica operational procedures. Hypercare does not cover new configuration, new integrations, new modules, or scope changes — these are Change Requests. Hypercare period commences on the go-live date and ends 28 calendar days later. [BU-ACU-008: RESOLVED WP15C 2026-06-18 — 4-week hypercare standard; consistent with BeBanking and Oracle pack standards]

---

## Section 137 — ACU-SUP: Support and AMS

**ACU-SUP-001.** Acumatica support after the hypercare period is provided under a separate AMS (Application Managed Services) SOW. The standard Acumatica implementation ends at hypercare close. Post-hypercare operational support is not included in the implementation SOW.

**ACU-SUP-002.** Acumatica software updates and version upgrades are managed by Acumatica as part of the SaaS subscription. APPSolve does not control Acumatica's release schedule. Under an Acumatica AMS SOW, APPSolve assesses the impact of Acumatica updates, tests critical business processes in the non-Production environment, and coordinates the client's sign-off before the update is applied to Production.

**ACU-SUP-003.** Acumatica platform support (hosting, infrastructure, uptime) is Acumatica's responsibility under the SaaS subscription. APPSolve is not the escalation path for Acumatica platform outages. APPSolve assists the client in raising Acumatica support cases where the issue is confirmed to be a platform defect.

**ACU-SUP-004.** Under an Acumatica AMS SOW, APPSolve's scope covers the modules and integrations named in the AMS SOW. Modules or integrations not named in the AMS SOW are not covered. AMS scope expansion requires a SOW amendment.

**ACU-SUP-005.** Bug fixes vs. enhancement requests in an Acumatica AMS context follow the same definitions as the AMS Assumption Pack (ACU-AMS cross-reference). A configuration defect that reproduces consistently and causes a business process to fail is a bug. A request to change how a business process works, add new functionality, or improve the user experience is an enhancement — not a bug — and is a Change Request under AMS.

**ACU-SUP-006.** When Acumatica releases a new version, Acumatica Marketplace ISV products installed in the client's tenant may require compatibility updates from their respective ISV vendors. Under an Acumatica AMS SOW, APPSolve identifies known ISV compatibility issues as part of the version impact assessment and notifies the client. APPSolve cannot apply a Acumatica version update that breaks a confirmed ISV product until the ISV vendor releases a compatible version. Delays caused by ISV update timelines are outside APPSolve's control; the client should maintain active support agreements with any ISV vendors to ensure timely compatibility updates.

**ACU-SUP-007.** Under an Acumatica AMS SOW, APPSolve's version impact assessment and regression testing activities require access to the client's non-Production Acumatica environment. Continuity of the non-Production environment is the client's responsibility under their Acumatica SaaS subscription. If the non-Production environment is not maintained or is decommissioned after implementation go-live, APPSolve's ability to validate updates before applying them to the Production environment is materially impaired. Clients are strongly advised to retain their non-Production environment as part of their ongoing Acumatica subscription.

**ACU-SUP-008.** Under an Acumatica AMS SOW, the Acumatica version update process follows this sequence: (a) APPSolve applies the update to the non-Production environment; (b) APPSolve tests critical business processes in non-Production; (c) the client's nominated testers complete regression testing and provide written sign-off confirming the update does not break business-critical processes; (d) APPSolve applies the update to the Production environment. No Acumatica update is applied to Production without the client's written sign-off from step (c). Regression testing in step (c) is the client's operational responsibility.

---

## Section 138 — ACU-EXT: External Dependencies and Third-Party

**ACU-EXT-001.** Acumatica licence procurement is the client's commercial relationship with Acumatica (either directly or via APPSolve as VAR). Acumatica licence cost is not included in APPSolve's implementation fee. Licence delays caused by commercial negotiations between the client and Acumatica are the client's responsibility and are documented as client-side delays if they impact the project schedule.

**ACU-EXT-002.** Client IT infrastructure for Acumatica (internet connectivity, user hardware, browser compatibility) is the client's responsibility. Acumatica is a cloud SaaS application accessible via a web browser. APPSolve does not assess, upgrade, or support the client's internal IT infrastructure. Connectivity or hardware issues that prevent users from accessing Acumatica are resolved by the client's IT team.

**ACU-EXT-003.** APPSolve maintains a published ISV Support List confirming which Acumatica Marketplace add-on products APPSolve actively implements, configures, and supports. Proposals may include ISV products only where they appear on the ISV Support List. APPSolve may recommend ISV products from the Acumatica Marketplace where standard Acumatica functionality has gaps — but only where the ISV is on the Support List. Procurement, licensing, and ISV vendor support agreements are separately contracted between the client and the ISV vendor. APPSolve's ISV configuration assistance is separately scoped. ISV products not on the Support List are assessed at pre-sales; APPSolve reserves the right to decline ISV implementation for products outside its competency. The ISV Support List is maintained by the Acumatica BU Lead and updated as APPSolve's ISV capabilities expand. [BU-ACU-004: RESOLVED WP15C 2026-06-18 — APPSolve maintains a published ISV Support List; proposals limited to listed ISVs]

**ACU-EXT-004.** Acumatica's SLA (uptime guarantee, disaster recovery, data backup) is governed by Acumatica's SaaS subscription agreement between the client and Acumatica. APPSolve's implementation and AMS SOW does not duplicate or override Acumatica's SaaS SLA. Clients seeking infrastructure SLA guarantees beyond Acumatica's standard SaaS terms must negotiate these directly with Acumatica.

**ACU-EXT-005.** SARS eFiling, UIF URS submissions, and other regulatory filings from Acumatica data are the client's responsibility. APPSolve configures Acumatica to support the preparation of filing data. APPSolve is not a tax practitioner and does not submit regulatory filings on behalf of clients.

**ACU-EXT-006.** Shipping and logistics carrier integration (DHL, FedEx, local courier API) with Acumatica is separately scoped. Carrier integration for shipment booking, tracking, and cost calculation requires individual scoping and is not a standard Acumatica base implementation item.

**ACU-EXT-007.** Retail and Point of Sale (POS) integration with Acumatica (for retail clients selling through physical or online POS systems) is separately scoped. POS system integration complexity varies significantly by POS platform. APPSolve assesses POS integration requirements during pre-sales and scopes them separately from the base Acumatica implementation.

**ACU-EXT-008.** Document management system (DMS) integration with Acumatica (SharePoint, OneDrive, DocuWare) is separately scoped. Acumatica's native file management (attaching documents to Acumatica records) is included in the standard implementation. Advanced DMS integration with automated document routing, approval, and archiving is out of scope for the standard implementation.

**ACU-EXT-009.** Electronic Data Interchange (EDI) integration with customers or suppliers through Acumatica is separately scoped. EDI integration requires: EDI standards mapping (X12, EDIFACT), VAN or direct EDI connection, and trading partner testing. APPSolve does not assume EDI integration in the standard Acumatica base scope.

---

## Section 139 — ACU-SEC: Security and Access Control

**ACU-SEC-001.** APPSolve configures Acumatica's role-based access control framework (user roles, module-level access rights, screen-level permissions) based on the access role framework defined and confirmed during Scope & Design. APPSolve delivers a set of standard roles aligned to the business processes in scope. Additional roles beyond the agreed set are a Change Request. Post-go-live user provisioning, role assignment, and deprovisioning are the client's IT or systems administrator's responsibility.

**ACU-SEC-002.** In multi-entity Acumatica implementations, branch and company-level access restriction (configuring which users can view and transact against which entities and branches) is configured by APPSolve as part of the standard security setup, based on the access matrix confirmed and signed off during Scope & Design. Changes to the access matrix after security configuration sign-off are a Change Request.

**ACU-SEC-003.** All Acumatica proposals issued by APPSolve include the following mandatory data residency and POPIA disclosure: Acumatica's cloud SaaS platform hosts client data in Acumatica's infrastructure. Data residency location is determined by Acumatica's hosting arrangements and is not within APPSolve's control. All South African organisations processing personal or financial data in Acumatica SaaS are subject to the Protection of Personal Information Act (POPIA). Clients must confirm Acumatica's data residency options and data processing agreements directly with Acumatica before engagement commences. APPSolve will assist with pre-sales data residency discussions but cannot contractually guarantee South African data residency for Acumatica SaaS. This disclosure is mandatory in all Acumatica proposals regardless of the client's industry sector. [BU-ACU-012: RESOLVED WP15C 2026-06-18 — POPIA data residency disclosure mandatory in all Acumatica proposals]

---

## Customer Responsibilities

**ACU-CUS-001.** The client provides a dedicated Project Sponsor and Project Manager for the duration of the Acumatica implementation. The Project Sponsor attends all key milestone reviews and has authority to make project decisions. Absence of a Project Sponsor or Project Manager from critical milestones delays the project.

**ACU-CUS-002.** The client provides named super-users for each module in scope. Super-users participate in design workshops, UAT, training, and knowledge transfer. Super-users must be available for a minimum of 50% of their working time during the implementation. If super-users are not available at the agreed participation level, this is a client-side risk that impacts the project timeline.

**ACU-CUS-003.** The client completes all configuration decisions and design workshops within the agreed timeline. Decision delays that block configuration progress are documented as client-side delays. APPSolve adjusts the project schedule to reflect client-side delays, and the client bears the cost of any schedule extension caused by decision delays.

**ACU-CUS-004.** The client provides all master data and opening balance data in the APPSolve-supplied templates by the agreed data submission deadline. Late data submission delays data migration and UAT, which delays go-live. Data quality issues in client-provided data are the client's responsibility to resolve.

**ACU-CUS-005.** The client executes UAT using the APPSolve-provided test scenarios. The client logs defects in the agreed defect management tool. UAT sign-off is the client's formal acceptance that the system is ready for production. The client understands that UAT sign-off triggers the go-live preparation phase.

**ACU-CUS-006.** The client is responsible for training their end users after APPSolve's super-user training is complete. End-user training is a client operational activity. APPSolve provides training materials for this purpose. The go-live date is not delayed because of end-user training completion.

**ACU-CUS-007.** The client manages the decommissioning of their legacy system after Acumatica go-live. APPSolve does not decommission, archive, or maintain the client's legacy system. The timing of legacy system decommissioning is the client's decision.

**ACU-CUS-008.** The client holds a valid Acumatica licence for the production go-live date. APPSolve does not proceed to production go-live without written confirmation that the client's Acumatica production licence is active.

---

## Explicit Exclusions

**ACU-EXC-001.** On-premises Acumatica installation, hosting, or infrastructure management — APPSolve delivers Acumatica as a cloud SaaS implementation only.

**ACU-EXC-002.** Payroll processing, payroll calculations, PAYE/UIF/SDL management — these are PaySpace's scope. Acumatica is not a payroll system.

**ACU-EXC-003.** Tax advisory, tax return preparation, SARS submissions — the client's tax advisors.

**ACU-EXC-004.** End-user training beyond the agreed super-user training sessions — the client cascades training to end users.

**ACU-EXC-005.** Historical transaction data migration beyond the agreed opening balance snapshot — unless explicitly included.

**ACU-EXC-006.** Custom development outside Acumatica's Low-Code/No-Code framework without explicit SOW inclusion and separate pricing.

**ACU-EXC-007.** Third-party system integration not explicitly named in the SOW.

**ACU-EXC-008.** Acumatica platform outage resolution — Acumatica SaaS SLA governs; client engages Acumatica support directly.

**ACU-EXC-009.** Business process consulting beyond the Acumatica implementation scope — change management, org design, process mapping for processes not in Acumatica scope.

**ACU-EXC-010.** Acumatica licence negotiation, commercial terms with Acumatica, or software cost reduction advice.

---

## BU Lead Decision Register — All Decisions RESOLVED

All 14 BU Lead decisions are resolved. This pack is Approved v1.0 and available for use in client-facing proposals.

| Decision ID | Item | Resolution | Programme |
|---|---|---|---|
| ~~BU-ACU-001~~ | Acumatica-PaySpace integration method | **RESOLVED** — Method confirmed at pre-sales per client PaySpace licence tier; API preferred where licence permits | WP15C 2026-06-18 |
| ~~BU-ACU-002~~ | Integration tier definitions | **RESOLVED** — AMS Pack tiers adopted: Simple / Standard / Complex | WP15C 2026-06-18 |
| ~~BU-ACU-003~~ | BI connector configuration | **RESOLVED** — BI tool integration always separately scoped; never in standard scope | WP15C 2026-06-18 |
| ~~BU-ACU-004~~ | ISV Support List | **RESOLVED** — APPSolve maintains a published ISV Support List; proposals limited to listed ISVs | WP15C 2026-06-18 |
| ~~BU-ACU-005~~ | Parallel run default | **RESOLVED** — Parallel run excluded by default; included only where explicitly in SOW | WP15C 2026-06-18 |
| ~~BU-ACU-006~~ | Standard reports per module | **RESOLVED** — All factory Acumatica reports for modules in scope; no curated list required | WP15C 2026-06-18 |
| ~~BU-ACU-007~~ | Training delivery format | **RESOLVED** — Virtual facilitated training is the standard; on-site at additional cost | WP15C 2026-06-18 |
| ~~BU-ACU-008~~ | Hypercare duration | **RESOLVED** — 4-week hypercare standard; consistent with BeBanking and Oracle standards | WP15C 2026-06-18 |
| ~~BU-ACU-009~~ | Acumatica partner tier | **RESOLVED** — Acumatica Gold Partner confirmed; cite "Acumatica Gold Partner" only; never "Gold Certified" | WP14G 2026-06-18 |
| ~~BU-ACU-010~~ | Data migration default | **RESOLVED** — Opening balances and open items only by default; historical migration always separately scoped | WP15C 2026-06-18 |
| ~~BU-ACU-011~~ | Non-PaySpace payroll policy | **RESOLVED** — PaySpace is standard; non-PaySpace assessed at pre-sales as custom integration | WP15C 2026-06-18 |
| ~~BU-ACU-012~~ | POPIA data residency disclosure | **RESOLVED** — Mandatory POPIA data residency disclosure in all Acumatica proposals | WP15C 2026-06-18 |
| BU-ACU-013 | (Not created — Velixo partnership factual confirmation; not a governance decision) | N/A | — |
| ~~BU-ACU-014~~ | PM inclusion threshold | **RESOLVED** — Dedicated PM included for 3+ modules or multi-BU scope | WP15C 2026-06-18 |
| ~~BU-ACU-015~~ | Consolidated financial reporting | **RESOLVED** — Consolidated reporting always separately scoped | WP15C 2026-06-18 |

---

*Acumatica Base Assumption Pack v1.0-Approved | WP11I created | WP11I-A Remediation Applied | WP14G BU-ACU-009 Resolved | WP15C All 14 Decisions Resolved 2026-06-18*
*Status: Approved v1.0 | approved_for_reuse: Yes | 152 assumptions across Sections 120–139 | All 14 BU decisions resolved | Approved by Acumatica BU Lead 2026-06-18 | Programme: WP15C*
