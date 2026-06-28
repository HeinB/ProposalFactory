---
document_id: ARM-IT045-ASSUMPTION-SCHEDULE
title: "ARM IT045 — Complete Assumption Schedule"
version: "1.0"
status: "Approved — Client Ready"
generated: "2026-06-24"
generated_by: "WP17D-1 — Inline Text Assembly Engine"
pattern: "EBS AMS Full Stack"
tender_id: "ARM IT045"
client: "African Rainbow Minerals"
category: "Assembly Engine Output"
packs_loaded: 6
raw_assumptions: 600
suppressions: 6
net_assumptions: 594
---

# ARM IT045 — Complete Assumption Schedule

---
AFRICAN RAINBOW MINERALS — ASSUMPTION SCHEDULE  
Version: 1.0  
Date: 2026-06-24  
Tender Reference: ARM IT045  
Engagement: Oracle EBS Application Managed Services — EBS AMS Full Stack  
Assembled: APPSolve Assembly Engine v1.1 — WP17D-1  
---

> This Assumption Schedule forms part of APPSolve's proposal and defines the assumptions under which the proposed scope, price, and timeline have been calculated. These assumptions represent the basis on which APPSolve has planned its approach and resources.
>
> Where any of these assumptions prove to be incorrect or where the client's requirements deviate from these assumptions, APPSolve reserves the right to raise a change request to address any resultant impact on scope, cost, or timeline.
>
> Client non-objection to this schedule within 10 business days of proposal submission constitutes acknowledgement of these assumptions for commercial purposes.

---

## Engagement Context

| Field | Value |
|---|---|
| Client | African Rainbow Minerals |
| Tender Reference | ARM IT045 |
| Engagement Type | Oracle EBS Application Managed Services |
| Products in Scope | Oracle EBS Financials + PPM + OCI (managed) + OIC Integrations + AMS |
| Solution Pattern | EBS AMS Full Stack |
| Packs Loaded | 6 (ERP, OCI, OIC, AMS, EBS-SLA Overlay, EBS-DRM Overlay) |
| Total Assumptions (Net) | 594 |
| Proposal Version | 1.0 |
| Valid From | 2026-06-24 |
| Valid To | 2026-08-23 (60 days) |

---

## Suppression Log

The following assumptions were suppressed per active suppression rules and do not appear in this schedule:

| Suppressed ID | Rule | Replacement |
|---|---|---|
| AMS-INC-004 | S1 — Replaced by dedicated resource model | EBS-DRM-013 |
| AMS-SLA-001 | S2 — Superseded by EBS-SLA overlay | EBS-SLA-002 |
| AMS-SLA-005 | S3 — Superseded by EBS-DRM framework | EBS-DRM-001 |
| AMS-PRI-001 | S2 — Superseded by EBS-SLA overlay | EBS-SLA-004, EBS-SLA-011 |
| AMS-PRI-002 | S2 — Superseded by EBS-SLA overlay | EBS-SLA-005 to EBS-SLA-009 |
| AMS-PRI-003 | S2 — Superseded by EBS-SLA overlay | EBS-SLA-012 |

---

## Section A — General and Engagement Assumptions

*This section establishes the overall scope, engagement model, and commercial framework governing this proposal.*

1. APPSolve's scope in Oracle Fusion ERP engagements covers: configuration design (Chart of Accounts, ledger structure, module setup); system configuration (applying the agreed design in Oracle ERP); data migration (FBDI load of agreed data objects); integration setup (where in scope — governed by OIC pack); testing support (CRP1, CRP2, UAT support); training delivery (TTT); cutover execution; and hypercare. APPSolve does not manage, administer, or operate the client's business processes post-go-live. *(Ref: ERP-GEN-001)*

2. APPSolve's Oracle ERP implementations follow the Oracle Unified Method (OUM): Mobilize → Scope and Design → Prototype → Validate → Deploy → Evolve. The Customer Success Navigator (CSN) accelerates delivery within OUM. Each phase has defined deliverables and client approval gates. *(Ref: ERP-GEN-002)*

3. Modules in scope are confirmed by the Oracle BOM signed at the time of SOW execution. Modules not in the signed BOM are excluded from scope. Where the client adds a module after SOW execution, the additional module is assessed and priced as a Change Request. *(Ref: ERP-GEN-003)*

4. Oracle Fusion ERP is delivered as a SaaS platform by Oracle. APPSolve configures the platform; Oracle operates it. The client receives one Production environment and at least one non-production (test) environment under the standard Oracle SaaS subscription. APPSolve does not procure, manage, or operate Oracle ERP infrastructure. *(Ref: ERP-GEN-004)*

5. Oracle Fusion ERP implementations are configuration-based. APPSolve uses Oracle-delivered configuration tools (Setup and Maintenance, BPM Worklist, Application Composer). Custom code development — Oracle APEX extensions, Oracle PaaS customisations, Groovy scripts beyond standard Oracle ERP configuration — is assessed as a separately scoped item. *(Ref: ERP-GEN-005)*

6. Oracle Fusion ERP receives quarterly updates from Oracle as part of the SaaS subscription. Oracle manages the update schedule. APPSolve provides implementation services; ongoing update management and regression testing post-go-live are the client's responsibility unless an APPSolve AMS agreement covers this. *(Ref: ERP-GEN-006)*

7. The Chart of Accounts (COA) design is the most critical early Scope and Design decision in an Oracle ERP Financials implementation. All downstream configuration — ledger setup, cross-validation rules, financial reporting, cost centre hierarchy, budget structure — depends on an approved COA. Delays to COA sign-off cascade to all dependent configuration streams. COA design must be signed off by the client before ledger configuration commences. *(Ref: ERP-GEN-007)*

8. The client's legal entity structure (company code, legal entity names, business unit structure) must be confirmed and stable before legal entity configuration commences. Changes to the legal entity structure after legal entity configuration is complete may require significant rework. APPSolve flags legal entity design changes as a project risk with scope impact. *(Ref: ERP-GEN-008)*

9. APPSolve's OCI engagement scope is limited to the workloads and environments explicitly named in the Statement of Work. Any workload not named in the SOW is out of scope. If the client identifies additional workloads during delivery that require OCI hosting, these will be treated as a Change Request. *(Ref: OCI-GEN-001)*

10. APPSolve is engaged to design, configure, and deliver OCI infrastructure. APPSolve is not engaged as the client's ongoing cloud operations team unless an explicit AMS or Managed OCI Services SOW is in place. Operational responsibility for OCI tenancy post-handover transfers to the client or the client's designated cloud operations team. *(Ref: OCI-GEN-002)*

11. The client holds the Oracle Cloud (OCI) tenancy agreement directly with Oracle. APPSolve does not enter into OCI tenancy agreements on behalf of clients. The client is responsible for all OCI subscription costs, support tiers, and contractual obligations with Oracle. Where a client requires assistance activating and configuring a new OCI tenancy before engagement work begins, this is treated as a billable pre-engagement activity and must be explicitly included in the SOW. OCI tenancy activation assistance is not assumed as a standard included service. *(Ref: OCI-GEN-003)*

12. OCI region selection is assumed to be Oracle's South Africa (Johannesburg) region as the primary region, unless the client specifies otherwise in writing. Multi-region deployments (e.g., primary South Africa with a secondary DR region) require explicit SOW definition and are not assumed by default. *(Ref: OCI-GEN-004)*

13. APPSolve assumes a single OCI tenancy for the engagement. If the client requires multiple tenancies (e.g., separate tenancies for subsidiaries, business units, or geographic entities), each additional tenancy is a separate scoped item and may require additional effort. *(Ref: OCI-GEN-005)*

14. APPSolve assumes the client will provide named technical contacts with authority to approve OCI architecture decisions, network configuration changes, and security policies. Without authorised client technical contacts, APPSolve cannot progress infrastructure delivery. Delayed approval of OCI architecture decisions is treated as a client-side delay per the CR framework. *(Ref: OCI-GEN-006)*

15. APPSolve delivers OCI engagements using Oracle's documented Well-Architected Framework principles as the baseline. Deviations from Oracle's recommended architecture require client approval and are documented as risk-accepted variances in the project record. *(Ref: OCI-GEN-007)*

16. Oracle SaaS products (Fusion HCM Cloud, Fusion ERP Cloud, Oracle CX Cloud) are hosted by Oracle on Oracle-managed infrastructure. APPSolve does not configure, access, or manage Oracle SaaS infrastructure. Any OCI work in a SaaS engagement is limited to integration middleware (OIC), custom extensions (APEX), or connected on-premise/hybrid systems. *(Ref: OCI-GEN-008)*

17. OCI infrastructure costs (compute, storage, database licensing, network egress, managed services) are the client's financial responsibility. APPSolve does not absorb, share, or guarantee OCI infrastructure costs. All OCI costs are billed by Oracle directly to the client's OCI tenancy. *(Ref: OCI-CST-001)*

18. APPSolve provides indicative OCI infrastructure cost estimates for budgeting purposes only. These estimates are based on Oracle's published price list at the time of proposal preparation and reflect the workload specifications provided. Indicative OCI cost estimates are not contractual commitments. Actual OCI infrastructure costs will vary based on: actual resource consumption, Oracle pricing changes, workload growth, additional environments, and usage outside normal business hours. OCI infrastructure costs are billed by Oracle directly to the client's OCI tenancy. APPSolve's engagement fees cover design, implementation, and professional delivery services only — they do not include OCI subscription or consumption costs. *(Ref: OCI-CST-002)*

19. OCI cost optimisation recommendations are provided as part of the standard delivery (right-sizing, scheduling non-production environments, Reserved Instance recommendations). Implementation of cost optimisation actions post-delivery is the client's operational responsibility unless covered by a Managed OCI Services AMS SOW. *(Ref: OCI-CST-003)*

20. Reserved Instances (Universal Credits / Annual Flex) for OCI cost reduction require client commitment for 1-year or 3-year periods. APPSolve may recommend Reserved Instance commitments but does not make these commitments on behalf of the client. Reserved Instance purchasing is the client's commercial decision with Oracle. *(Ref: OCI-CST-004)*

21. Non-production OCI environments (Development, Test, UAT) can be scheduled to shut down outside business hours to reduce OCI costs. Auto-shutdown scheduling is configured if explicitly requested. The client defines the non-production uptime schedule. Auto-shutdown is not enabled by default. *(Ref: OCI-CST-005)*

22. OCI network egress costs (data transfer from OCI to internet or on-premise) can be significant for high-volume data integrations. APPSolve highlights egress cost risk in the architecture design review where applicable. Actual egress costs are based on Oracle's pricing and are the client's responsibility. *(Ref: OCI-CST-006)*

23. FinOps (cloud financial operations) maturity implementation — tagging governance, showback/chargeback models, unit cost economics — is not included in the standard OCI delivery. FinOps advisory is a separate optional engagement and is not assumed by default. *(Ref: OCI-CST-007)*

24. OCI Cost Analysis and Budgets dashboards are configured as part of the standard Landing Zone. The client's finance team is responsible for OCI budget management and cost anomaly investigation post-handover. Cost anomaly alerts are configured in OCI Budgets to notify the client's designated contacts. *(Ref: OCI-CST-008)*

---

## Section B — Project Execution Assumptions

*This section covers integration, data migration, testing, training, cutover, and hypercare assumptions applicable across all solution components.*

25. All ERP integrations to third-party systems are governed by `OIC_ASSUMPTIONS_V1.md`. This section defines ERP-specific integration scope boundaries and Oracle-native integration points that do not require OIC. *(Ref: ERP-INT-001)*

26. Oracle Fusion ERP to Oracle Fusion HCM (where both modules are in scope in the same project): the ERP-HCM integration uses Oracle-native REST APIs and Oracle-delivered integration patterns. This is not a separately scoped OIC integration; it is included in the combined HCM + ERP implementation scope. *(Ref: ERP-INT-002)*

27. Within Oracle Fusion ERP, inter-module integration (for example: AP to GL subledger accounting posting; Procurement to AP invoice matching; PPM cost to GL) uses Oracle-native subledger accounting and integration architecture. These are not separately scoped OIC integrations. *(Ref: ERP-INT-003)*

28. Bank connectivity — EFT payment file generation and bank statement import — is facilitated via BeBanking H2H (where BeBanking is in scope) or via direct bank file format integration where BeBanking is not in scope. Each payment format (different bank or different payment type) constitutes one OIC integration (see OIC_ASSUMPTIONS_V1.md OIC-SCP-002). *(Ref: ERP-INT-004)*

29. SARS eFiling integration is not an APPSolve standard ERP capability and is excluded from scope unless specifically contracted as a custom integration engagement. Oracle Fusion ERP does not have a native integration to the SARS eFiling portal. Automated submission of VAT201, PAYE EMP201, or provisional tax returns to SARS is the client's tax team's responsibility using their preferred submission method (manual eFiling, tax software, or separately contracted integration). Tax reporting data extracts — OTBI-based VAT reports or GL tax reports to support the client's manual eFiling process — may be included in scope where explicitly listed in the proposal. *(Ref: ERP-INT-005)*

30. Data migration follows Oracle's File-Based Data Import (FBDI) framework for all standard Oracle ERP data objects. APPSolve provides FBDI templates for each data object in scope; the client populates these templates with data extracted from the source system. APPSolve loads and validates the data in Oracle ERP. *(Ref: ERP-DAT-001)*

31. Standard migrated data objects for Oracle Fusion ERP (subject to BOM and scope confirmation): Chart of Accounts value sets and code combinations; suppliers (AP); customers (AR); open AP invoices and payment schedules; open AR invoices and receipt applications; fixed asset register (opening balance); projects and project budgets (PPM); open purchase orders (Procurement). *(Ref: ERP-DAT-002)*

32. Historical transaction data is not migrated. Opening balances are migrated as at the agreed cut-over date. This means: historical GL journals (prior periods) are not in Oracle ERP; historical paid AP invoices are not in Oracle ERP; historical closed AR invoices are not in Oracle ERP. The client's legacy system is the system of record for historical data. *(Ref: ERP-DAT-003)*

33. Data extraction from the source (legacy) system is the client's responsibility. APPSolve provides the FBDI templates and format specifications. The client's IT team or legacy system administrator extracts data from the legacy system and populates the FBDI templates. APPSolve is available for template guidance but does not extract data from legacy systems. *(Ref: ERP-DAT-004)*

34. Data quality and cleansing is the client's responsibility before data is provided to APPSolve. Data provided to APPSolve must be: de-duplicated (no duplicate supplier or customer records); complete (all mandatory fields populated); accurate (values match the business reality); and correctly coded (GL codes, cost centres, and project codes aligned to the agreed COA). APPSolve validates that data loads correctly into Oracle ERP; it does not validate the business accuracy of source data. *(Ref: ERP-DAT-005)*

35. Two migration cycles are standard: (1) Mock Migration 1 — executed in the non-production environment to test the FBDI load process, identify data issues, and allow the client to correct data; (2) Mock Migration 2 — a repeat mock run after data corrections, validating that all issues from Mock 1 are resolved; (3) Final Migration — executed in the production environment at go-live. A total of two mock cycles plus one final production migration is the APPSolve base scope. Additional migration cycles beyond two mocks require a change control approval and are priced per additional cycle. *(Ref: ERP-DAT-006)*

36. Tax registration data — VAT registration numbers, income tax reference numbers, customs registration numbers, and PAYE reference numbers — is configured in Oracle ERP as part of the legal entity and tax setup. The client provides all tax registration information before legal entity and tax configuration commences. *(Ref: ERP-DAT-007)*

37. Oracle Fusion ERP testing follows the OUM testing framework and aligns to HCM Base testing assumptions (HCM-TST-001 through HCM-TST-004 where applicable). Three testing cycles: CRP1 — Design Validation; CRP2 — End-to-End Validation; UAT — User Acceptance Testing. *(Ref: ERP-TST-001)*

38. CRP1 (Design Validation): APPSolve demonstrates the configured system against the agreed Scope and Design document. The client's functional team (finance leads, procurement leads, PPM leads) validates that the configured process matches the design. CRP1 is a structured design review — not a user acceptance test. *(Ref: ERP-TST-002)*

39. CRP2 (End-to-End Validation): complete end-to-end process testing across all configured ERP modules. For example: purchase requisition → PO approval → goods receipt → AP invoice → payment → GL posting → bank reconciliation. The client's functional team executes end-to-end scenarios with test data. APPSolve resolves configuration defects identified during CRP2. *(Ref: ERP-TST-003)*

40. UAT (User Acceptance Testing): the client's user community (finance users, procurement users, project managers) validates the system against their business requirements. APPSolve supports UAT but does not execute it. UAT sign-off is the client's responsibility and a mandatory prerequisite for production cutover. *(Ref: ERP-TST-004)*

41. Test data provision for all testing cycles is the client's responsibility. Test data must reflect realistic transaction values, include both standard and exception scenarios, and cover all modules in scope. APPSolve does not source, create, or transform test data. *(Ref: ERP-TST-005)*

42. Defect management follows the same classification as OIC testing (build defects resolved by APPSolve; data/process/design defects resolved by client). A formal defect log is maintained throughout all testing phases. *(Ref: ERP-TST-006)*

43. Two testing cycles are standard for each OIC integration engagement: (1) **System Integration Testing (SIT)** — executed by APPSolve against all endpoints; validates technical connectivity, data format, transformation logic, error handling, and integration flow behaviour; (2) **User Acceptance Testing (UAT)** — executed by the client's functional team with APPSolve support; validates that the integration meets business requirements and end-to-end business processes work as expected. *(Ref: OIC-TST-001)*

44. The client provides all test data required for SIT and UAT before testing commences. Test data must be realistic (representative of actual production transactions) and must cover positive scenarios (successful transactions), negative scenarios (invalid data, missing mandatory fields), and edge cases (extreme values, boundary conditions) as agreed in the test plan. APPSolve does not source, create, or validate test data on the client's behalf. *(Ref: OIC-TST-002)*

45. APPSolve executes SIT and produces SIT test results for each integration. UAT is executed by the client's designated UAT testers. APPSolve provides UAT support: attending UAT sessions, investigating defects raised during UAT, and resolving build defects (defects caused by APPSolve's implementation). APPSolve does not execute UAT on behalf of the client. *(Ref: OIC-TST-003)*

46. APPSolve classifies defects raised during testing as follows: (a) **Build defects** — caused by APPSolve's implementation (incorrect transformation logic, incorrect OIC configuration, error handling failures) — resolved by APPSolve at no additional charge; (b) **Data defects** — caused by incorrect or incomplete test data provided by the client — the client's responsibility to resolve; (c) **Mapping defects** — caused by incorrect business mapping decisions (which may require a Mapping Specification amendment) — assessed as a mapping change; (d) **Vendor defects** — caused by the third-party endpoint (API errors, incorrect API documentation, unstable sandbox) — the vendor's and client's responsibility to resolve. *(Ref: OIC-TST-004)*

47. The client signs off SIT completion before UAT commences, and signs off UAT completion before production cutover proceeds. APPSolve does not proceed to the next test phase or to cutover without written client sign-off on the completion of the preceding phase. Sign-off may be provided by email from the client's designated project sponsor or project manager. *(Ref: OIC-TST-005)*

48. The client is responsible for coordinating third-party vendor participation in integration testing where the integration connects to a non-Oracle system. If a third-party vendor is not available during the agreed SIT testing window, SIT for that integration is deferred. APPSolve is not responsible for delays caused by third-party vendor unavailability during testing. *(Ref: OIC-TST-006)*

49. APPSolve delivers train-the-trainer (TTT) training for Oracle Fusion ERP across the user populations agreed in the training plan. Default TTT populations (subject to BOM): GL and Financial Reporting users, AP Invoice Processors, AR Billing users, Cash Management users, Procurement Requisitioners and Buyers, PPM Project Managers (per modules in scope). *(Ref: ERP-TRN-001)*

50. End-user training delivery is the client's responsibility. APPSolve provides TTT training and delivers configured-system training guides and quick reference cards; the client's trained trainers deliver end-user training to the broader employee population. APPSolve does not train individual end users. *(Ref: ERP-TRN-002)*

51. Training materials are based on the client's configured Oracle ERP system. APPSolve does not use generic Oracle product training materials as the primary training deliverable. Training materials reference the client's specific COA, workflows, data, and transaction types. *(Ref: ERP-TRN-003)*

52. Oracle University formal training (Oracle certification courses, Oracle product training) is the client's commercial arrangement with Oracle. APPSolve's training scope covers the configured system — not Oracle product certification or generic Oracle Fusion overview training. *(Ref: ERP-TRN-004)*

53. One production cutover event is included. The cutover approach (big-bang cutover of all modules on one date, or phased module go-live) is confirmed in the Scope and Design phase and documented in the cutover plan. APPSolve recommends big-bang cutover for Oracle ERP where the modules are highly interdependent (GL, AP, AR in the same ledger must typically go live together). *(Ref: ERP-CUT-001)*

54. APPSolve produces a cutover runbook covering: pre-cutover steps (legacy system transaction freeze, final FBDI data extract, data validation, non-production mock run completion); cutover day steps (FBDI production load execution, opening balance verification, connectivity testing, integration activation); and go-live confirmation criteria (trial balance agrees, AP supplier list loaded, AR customer list loaded, open transaction count reconciled). *(Ref: ERP-CUT-002)*

55. Legacy system transaction freeze: the client implements a freeze on new transaction entry in the legacy system for the period required to extract final migration data and complete the FBDI load. The freeze duration is determined by the data volume and migration complexity. The client manages the internal communication and business impact of the freeze period. *(Ref: ERP-CUT-003)*

56. Go-live decision is made by the client's ERP project sponsor based on APPSolve's technical go/no-go assessment. APPSolve provides a written go/no-go recommendation; the final go-live decision rests with the client's project sponsor. *(Ref: ERP-CUT-004)*

57. ERP parallel running is excluded by default. Parallel running — simultaneously operating the legacy ERP and Oracle Fusion ERP for a period after go-live, with transaction reconciliation between both systems — is not included in the base scope. A short controlled validation period (typically five to ten business days, limited to trial balance and opening balance verification only, not full operational parallel close) may be included where this is explicitly stated in the proposal scope section. Full parallel financial close cycles — completing a full month-end close in both legacy and Oracle ERP simultaneously — are excluded unless separately scoped and priced. The commercial and resource implications of any parallel activity must be agreed before the SOW is executed. *(Ref: ERP-CUT-005)*

58. One production cutover event is included per integration. The cutover event covers: APPSolve promoting the integration from the non-production OIC environment to the production OIC environment; executing the cutover runbook; performing initial production connectivity tests; and confirming the integration is live in production. *(Ref: OIC-CUT-001)*

59. APPSolve produces a cutover runbook for each integration covering: pre-cutover steps; production credential configuration; production environment promotion; initial connectivity test; go-live confirmation check; and rollback steps. The cutover runbook is reviewed and approved by the client's project manager before production cutover commences. *(Ref: OIC-CUT-002)*

60. Multiple production cutover rehearsals (integration dress rehearsals) are not included in standard scope. Where the client requires production rehearsal runs — deploying to a production-like environment before the actual go-live — each rehearsal is assessed as a scope addition. APPSolve recommends rehearsals where the integration is business-critical or where the go-live window is time-constrained. *(Ref: OIC-CUT-003)*

61. Production cutover requires the client's written go-ahead (go/no-go decision) from the designated project sponsor. APPSolve does not deploy to production without receiving the client's explicit go-live authorisation. The client's project manager or sponsor provides go-live authorisation in writing (email is acceptable) before APPSolve commences production deployment. *(Ref: OIC-CUT-004)*

62. End-to-end data reconciliation between source and target systems at cutover — verifying that every record processed during the initial production run was correctly received and processed by the target system — is the client's operational responsibility. APPSolve provides integration-level validation (confirming OIC processed the expected number of messages without errors). Business-level reconciliation (confirming that business records in the target system match the source) is the client's team's responsibility. *(Ref: OIC-CUT-005)*

63. ERP hypercare aligns to the APPSolve standard: four (4) weeks duration; business hours (08:00–17:00 SAST Monday–Friday); defect resolution and system stabilisation only. HCM Base assumptions HCM-HYP-001, HCM-HYP-002, and HCM-HYP-003 apply equally to Oracle Fusion ERP engagements. *(Ref: ERP-HYP-001)*

64. Where Oracle ERP and Oracle HCM and/or OIC integrations are delivered in the same project, hypercare is a single concurrent four-week period covering all modules and integrations. HCM Base HCM-HYP-001 and OIC pack OIC-SUP-002 apply. *(Ref: ERP-HYP-002)*

65. Enhancements and scope additions during hypercare are excluded. This includes: adding new GL accounts or COA segments post-go-live, adding new approval workflows, adding new OTBI reports beyond the agreed scope, and adding new modules not in the original BOM. These are assessed as Change Requests or new project work. *(Ref: ERP-HYP-003)*

66. Period-end close support during hypercare: APPSolve provides hypercare support during the first month-end close after go-live. If the hypercare period ends before the first month-end close, APPSolve will extend hypercare to cover the first month-end close at the standard daily hypercare rate. This ensures the client has APPSolve support during the most operationally critical post-go-live event. *(Ref: ERP-HYP-004)*

---

## Section C — Functional Application Assumptions

*This section covers all application-layer configuration, customisation, and integration assumptions grouped by product.*

### C.1 Oracle E-Business Suite Functional Assumptions

*This section covers all Oracle EBS functional module configuration assumptions including Financials, Procurement, PPM, Reporting, and Workflow.*

67. APPSolve configures one primary ledger per legal entity. A primary ledger holds the main accounting records in the functional currency. Secondary ledgers — including reporting currency ledgers, IFRS vs local GAAP adjustment ledgers, and any additional statutory or management accounting ledgers — are excluded from base scope unless explicitly listed in the proposal and SOW. Where secondary ledgers are required, their design, configuration, and testing effort is separately assessed and priced. *(Ref: ERP-GL-001)*

68. The client is responsible for defining the Chart of Accounts structure: the segment names, segment lengths, value set definitions, and the complete list of code combination values for each segment. APPSolve configures the COA in Oracle ERP based on the client-approved COA design. APPSolve facilitates COA design workshops; it does not design the client's COA from scratch. *(Ref: ERP-GL-002)*

69. The default Chart of Accounts structure includes up to six (6) segments: Company/Entity, Department, Account (Natural Account), Cost Centre, Project, and one additional segment confirmed in the Scope and Design phase. Additional segments beyond six require assessment and may affect reporting and cross-validation rule complexity. The client confirms the final segment structure before COA configuration commences. *(Ref: ERP-GL-003)*

70. The client provides the financial calendar — accounting year-end month, period type (monthly, 12 periods per year is the standard), and the financial year start date — before ledger configuration commences. APPSolve configures the Oracle accounting calendar per the client's confirmed specifications. *(Ref: ERP-GL-004)*

71. The functional currency (the currency in which each legal entity conducts its primary business and keeps its books of account) is confirmed per legal entity before ledger configuration commences. For South African operations, the functional currency is ZAR. Where a legal entity operates in a foreign currency, the functional currency, presentation currency, and currency conversion method are confirmed in the Scope and Design phase. *(Ref: ERP-GL-005)*

72. Intercompany accounting is excluded from base GL scope unless explicitly listed in the proposal. Basic balancing segment design — configuring the primary balancing segment so that Oracle ERP automatically balances intercompany entries — may be included as part of the standard COA and ledger configuration. Full intercompany accounting scope (intercompany accounting rules, intercompany invoicing, intercompany reconciliation workflows, multi-lateral netting, and consolidation eliminations) requires a separately scoped and priced engagement. *(Ref: ERP-GL-006)*

73. APPSolve configures one (1) standard journal approval workflow per Oracle ERP instance. The journal approval workflow routes manual journal entries through an approval chain before posting. Additional journal approval workflows (for example, separate workflows per business unit, per journal category, or per ledger) constitute a Change Request. *(Ref: ERP-GL-007)*

74. Financial reporting: APPSolve configures Financial Reporting Studio (FRS) reports covering the client's agreed standard financial statement pack (Income Statement, Balance Sheet, Trial Balance, and Cash Flow Statement where required). The number of FRS reports agreed is documented in the Scope and Design deliverables. Additional financial reports beyond the agreed scope are Change Requests. *(Ref: ERP-GL-008)*

75. Supplier master data is migrated from the client's source system as part of the data migration scope. The client provides all supplier master data — including legal name, registration number, tax registration number, bank account details, payment terms, and address — in APPSolve's FBDI supplier template. APPSolve loads and validates the supplier data in Oracle ERP. *(Ref: ERP-AP-001)*

76. Manual invoice entry is the default AP invoice processing approach. Automated invoice capture — OCR-based invoice imaging, intelligent document processing, e-invoicing via supplier networks (Ariba Network, Tungsten/OB10, or equivalent) — is excluded from base scope. Where the client requires automated invoice capture, this is assessed as a scope addition. *(Ref: ERP-AP-002)*

77. Three-way match (PO / Goods Receipt Note / Invoice) is the APPSolve default for purchase-order-based supplier invoices where Oracle Procurement and Oracle Receiving are both in scope. Three-way match validates that the invoice quantity and amount match both the approved PO and the confirmed goods receipt before the invoice is approved for payment. Two-way match (PO / Invoice only, without a goods receipt) may be used only where Oracle Receiving is not in the BOM scope, or where the client explicitly confirms that their purchasing process does not use goods receipt confirmation. The matching approach is confirmed in the Scope and Design phase and documented in the AP configuration design. *(Ref: ERP-AP-003)*

78. Non-PO invoices (invoices without a corresponding purchase order — typically for services, utilities, rent, and overhead costs) are entered via Oracle AP's direct invoice entry workflow. The non-PO invoice approval routing is designed in the Scope and Design phase. One standard non-PO invoice approval workflow is included. *(Ref: ERP-AP-004)*

79. Payment processing: APPSolve configures Oracle AP for EFT (electronic funds transfer) payments to South African bank accounts using the standard South African EFT payment format. The specific bank payment format file specification is confirmed with the client's bank before AP payment configuration commences. Where BeBanking is in scope, payment file generation and bank submission are facilitated via the BeBanking H2H integration (see OIC pack). *(Ref: ERP-AP-005)*

80. Payment terms (standard supplier payment terms — 30 days, 60 days, net immediate, etc.) are configured in Oracle AP based on the list of payment terms provided by the client. APPSolve configures all payment terms provided by the client; it does not define the client's payment terms policy. *(Ref: ERP-AP-006)*

81. Oracle Supplier Portal — enabling suppliers to submit invoices electronically, view PO status, and update their own profile — is excluded from base scope. The Supplier Portal requires Oracle Supplier Portal Cloud Service (separately licensed) and an integration setup. Where Supplier Portal is required, it is assessed and priced as a scope addition. *(Ref: ERP-AP-007)*

82. Customer master data is migrated from the client's source system as part of the data migration scope. The client provides customer data — legal name, account number, address, payment terms, credit limit, and tax details — in APPSolve's FBDI customer template. *(Ref: ERP-AR-001)*

83. Oracle AR transaction types (invoice, credit memo, debit memo) and transaction sources are configured per the client's billing processes confirmed in the Scope and Design phase. APPSolve configures the transaction type library; the client confirms which transaction types are required. *(Ref: ERP-AR-002)*

84. Auto-invoicing — importing invoice transactions from another Oracle module (Oracle Fusion PPM, Oracle Order Management, or another source system) — is included in standard AR scope where the source system is an Oracle module in the same implementation. Auto-invoicing from a non-Oracle source requires an OIC integration (see OIC pack). *(Ref: ERP-AR-003)*

85. Cash application: Oracle AR is configured with standard auto-cash rules for EFT receipts — matching receipts to open invoices by invoice number or customer account. Complex cash application scenarios (foreign currency receipts, partial payments with deduction management, lockbox processing for high-volume B2C receipts) are assessed per complexity. *(Ref: ERP-AR-004)*

86. Oracle AR Collections Management — automated dunning letter generation, collection strategy assignment, and aged debt reporting — is an Oracle-delivered platform feature. APPSolve configures the collections framework (dunning letter templates, collection strategies) as part of the standard AR implementation. The client's credit control team manages collections activity post-go-live. *(Ref: ERP-AR-005)*

87. APPSolve configures Oracle FA asset categories (the grouping structure that defines default depreciation rules for each asset type), depreciation methods, useful life assignments, and the asset book structure. The client provides the complete list of asset categories with their depreciation rules before FA configuration commences. *(Ref: ERP-FA-001)*

88. Fixed asset migration standard is opening balance only as at the go-live date. The opening balance migration includes: asset description, asset cost (original cost), net book value (NBV) at go-live, accumulated depreciation at go-live, and remaining useful life. Detailed historical asset transactions — period-by-period depreciation run history, historical revaluation journals, historical impairment entries, and asset additions/disposals prior to go-live — are not migrated. The client's legacy asset system is retained as the system of record for historical fixed asset data. The client is required to provide the current, reconciled asset register (including cost, accumulated depreciation, and NBV per asset) before migration commences. Migration cannot proceed without a client-approved asset register. *(Ref: ERP-FA-002)*

89. Oracle FA is configured to run periodic (monthly) depreciation as a batch process. The client's finance team runs the depreciation process in Oracle after period-end close. APPSolve configures the depreciation process; the client's finance team operates it post-go-live. *(Ref: ERP-FA-003)*

90. Capital expenditure approval (the workflow for approving a capital purchase before the asset is created in Oracle FA) is configured as one standard capex approval workflow. The approval routing is based on the client's confirmed authority matrix. *(Ref: ERP-FA-004)*

91. A tax asset book (tracking assets for tax depreciation purposes separately from the accounting asset book) is assessed per engagement. Where South African tax depreciation allowances (Section 11/12 SITA, accelerated depreciation, SBC allowances) require separate tracking from accounting depreciation, a tax book is added to the design. *(Ref: ERP-FA-005)*

92. Oracle Cash Management is configured for bank reconciliation. APPSolve configures bank accounts in Oracle CM, defines reconciliation rules, and enables the bank statement import capability. Manual bank reconciliation (bank officer manually reconciles bank statement to Oracle cash entries) and automated reconciliation (via electronic bank statement import) are both supported. *(Ref: ERP-CM-001)*

93. Bank statement import format is confirmed with the client's bank. Oracle CM supports ISO 20022 camt.053 and SWIFT MT940 as standard formats for electronic bank statement import. Where the bank uses a proprietary format not supported by Oracle natively, a format conversion is assessed. Where BeBanking is in scope, MT940 inbound via the BeBanking integration is the standard mechanism (see OIC pack). *(Ref: ERP-CM-002)*

94. Cash positioning and cash forecasting capabilities are Oracle-delivered platform features within Oracle CM. APPSolve enables and configures cash positioning as part of the standard CM implementation. The accuracy of cash forecasts depends on the completeness of Oracle AP payment schedules and AR expected receipt data. *(Ref: ERP-CM-003)*

95. Where BeBanking H2H bank connectivity is in scope (B86481 + BeBanking BOM), the MT940 bank statement inbound integration from BeBanking to Oracle CM is configured as part of the BeBanking OIC integration scope (OIC pack OIC-SCP-001). The Oracle CM bank account and reconciliation rules are configured as part of the ERP Financials scope. *(Ref: ERP-CM-004)*

96. Oracle Procurement modules in scope are confirmed by the BOM. Standard Procurement scope includes Self-Service Procurement (purchase requisitioning), Oracle Purchasing (PO management, approval, receiving), and where licensed, Oracle Sourcing (RFQ, RFP, auction management) and Oracle Procurement Contracts. *(Ref: ERP-PRO-001)*

97. The requisition-to-PO procurement flow is the core Procurement process. APPSolve configures: purchase requisition entry and approval; automatic PO creation from approved requisitions; PO acknowledgement; goods receipt (Oracle Receiving); and three-way match linkage to Oracle AP. The flow design is agreed in the Scope and Design phase. *(Ref: ERP-PRO-002)*

98. Procurement approval hierarchy: APPSolve configures one approval hierarchy for purchase requisitions and one for purchase orders, using Oracle Approval Management Engine (AME). The default is position-based approval (routing based on the requester's position in the organisation hierarchy). Employee-supervisor based approval is an alternative. The approval authority matrix (who can approve, up to what amount) is provided by the client before workflow configuration commences. *(Ref: ERP-PRO-003)*

99. Oracle Procurement catalogue management: APPSolve configures hosted item catalogues in Oracle Self-Service Procurement where the client wishes to restrict requisitions to approved items at pre-agreed prices. The client provides item catalogue data (item descriptions, unit prices, supplier links) in the required template. Punchout catalogues (integration to a supplier-hosted catalogue) require a separately scoped OIC integration. *(Ref: ERP-PRO-004)*

100. Oracle Procurement Contracts (where in scope): APPSolve configures contract templates, standard contract terms, and the contract authoring workflow. The client provides the legal content for contract templates (standard terms and conditions, deviation approval rules). APPSolve configures the Oracle contract framework; the client's legal team is responsible for the contract content. *(Ref: ERP-PRO-005)*

101. Oracle Receiving (GRN processing) is included in standard Procurement scope for PO-based purchasing. Receiving records the physical delivery of goods against a purchase order and triggers the three-way match process in Oracle AP. The goods receipt workflow (who records receipts, on what device, in what location) is confirmed in the Scope and Design phase. *(Ref: ERP-PRO-006)*

102. Oracle Spend Analytics and Procurement reporting use Oracle OTBI's Procurement subject areas. APPSolve configures procurement-specific OTBI reporting security and delivers the agreed set of standard procurement reports. Advanced spend analysis requiring Oracle Procurement Analytics Cloud (OAX) is separately licensed and assessed. *(Ref: ERP-PRO-007)*

103. Oracle Fusion PPM modules in scope are confirmed by the BOM. Standard PPM scope includes Project Costing (B86483) — project creation and maintenance, cost collection, project reporting. Where Oracle Project Billing is in scope, billing events and revenue recognition are added. *(Ref: ERP-PPM-001)*

104. Project types and project templates are designed in the Scope and Design phase. The client provides the project classification structure (project types, project statuses, project categories) and the template for each project type before PPM configuration commences. APPSolve configures the Oracle PPM project type library based on the client's confirmed structure. *(Ref: ERP-PPM-002)*

105. Project costing: cost transactions are collected against projects using Oracle's standard cost collection mechanisms — labour costs (via Oracle Time and Labour or manual timecard entry), non-labour costs (via Oracle AP invoice line distribution to a project), and expense costs (where Oracle Expenses is in scope). The costing design is confirmed in the Scope and Design phase. *(Ref: ERP-PPM-003)*

106. Project budgeting: Oracle PPM supports project-level budgets and forecasts. APPSolve configures the budget type structure and budget approval workflow as agreed in Scope and Design. The client provides project budget templates before budget configuration commences. *(Ref: ERP-PPM-004)*

107. Oracle Project Billing (where in scope): billing methods supported by Oracle PPM include time-and-material billing, fixed-price milestones, and cost-plus billing. The billing method per project type is confirmed in the Scope and Design phase. The client confirms the billing events, billing cycles, and revenue recognition rules before billing configuration commences. *(Ref: ERP-PPM-005)*

108. Integration between Oracle PPM and Oracle Financials (GL and AP) is Oracle-native — project cost transactions post automatically to the General Ledger via Oracle's subledger accounting engine. This is not a separately scoped OIC integration. APPSolve configures the subledger accounting (SLA) rules that govern how project costs hit the GL. *(Ref: ERP-PPM-006)*

109. Project reporting via OTBI: APPSolve configures PPM OTBI reporting security and delivers agreed project performance reports. Advanced project portfolio analytics and dashboard capabilities requiring Oracle Analytics Cloud are separately licensed and excluded from PPM base scope. *(Ref: ERP-PPM-007)*

110. Oracle Transaction Business Intelligence (OTBI) is the standard embedded reporting tool for Oracle Fusion ERP. APPSolve configures OTBI reporting security (subject area access, data security filters) and delivers the agreed custom OTBI reports as part of the implementation. The number of custom OTBI reports included in scope is confirmed in the Scope and Design phase. *(Ref: ERP-REP-001)*

111. Oracle Financial Reporting Studio (FRS) — the tool for designing formatted financial statements — is included in Oracle Fusion ERP. APPSolve configures FRS reports for the agreed standard financial statement pack. The number of FRS reports in scope is confirmed in the Scope and Design phase. *(Ref: ERP-REP-002)*

112. Oracle Smart View (Excel add-in enabling financial data queries directly from Excel against Oracle ERP) is an Oracle-delivered feature included in the ERP subscription. APPSolve enables Smart View and provides awareness training to finance users. The client's finance team is responsible for building their own Smart View-based Excel models; APPSolve does not build client Excel reporting models. *(Ref: ERP-REP-003)*

113. Oracle Analytics Cloud (OAX/FAW — Fusion Analytics Warehouse) is a separately licensed Oracle product and is not included in the standard Oracle Fusion ERP subscription. OTBI, FRS, and Smart View are included in the ERP licence. Where the client requires OAX analytics, it is a separately licensed and separately scoped item. *(Ref: ERP-REP-004)*

114. SARS VAT return reporting: Oracle ERP captures the VAT transaction data required to prepare the VAT201 return. APPSolve configures OTBI VAT reports that the client's tax team uses to extract VAT data. Oracle Fusion ERP does not submit VAT returns to SARS eFiling. The eFiling submission is the client's tax team's responsibility. *(Ref: ERP-REP-005)*

115. All Oracle Fusion ERP approval workflows are configured using the Oracle Approval Management Engine (AME). APPSolve configures AME approval rules per the workflow design agreed in the Scope and Design phase. The client provides the complete authority matrix — defining who can approve what transaction type at what monetary amount — before workflow configuration commences. *(Ref: ERP-WFL-001)*

116. Standard approval workflows included in base ERP scope (subject to module BOM): (a) Manual journal approval (GL); (b) Non-PO supplier invoice approval (AP); (c) Purchase requisition approval (Procurement); (d) Purchase order approval (Procurement); (e) Capex approval (Fixed Assets — where FA is in scope); (f) Project budget approval (PPM — where PPM is in scope). Each workflow listed constitutes one APPSolve configuration item. *(Ref: ERP-WFL-002)*

117. One approval hierarchy is configured per workflow type. Multiple parallel approval hierarchies per workflow (for example, a different PO approval chain for each business unit or department) constitute a Change Request and are assessed per the number of additional hierarchies required. *(Ref: ERP-WFL-003)*

118. Oracle Fusion ERP approval notification emails use Oracle's standard BPM Worklist notification framework. Notifications are delivered via Oracle's workflow notification engine. Custom HTML-branded email templates are excluded from base scope. HCM Base assumption HCM-WFL-004 applies where HCM and ERP are in the same project. *(Ref: ERP-WFL-004)*

119. Delegation rules — allowing a user to delegate their approval authority to another user during absence — are an Oracle ERP platform feature. APPSolve enables delegation capability as part of the standard workflow configuration. Users manage their own delegation rules post-go-live via the Oracle ERP self-service interface. *(Ref: ERP-WFL-005)*

120. Approval limits (the monetary amount thresholds that determine which approver handles which transaction value) are configured per the client's authority matrix. The client provides the complete, approved authority matrix before workflow configuration commences. Changes to approval limits after workflow configuration is complete are low-effort configuration changes and do not constitute a Change Request unless they require structural workflow redesign. *(Ref: ERP-WFL-006)*

### C.3 Oracle Integration Cloud (OIC) Assumptions

*This section covers OIC integration platform assumptions, interface design, endpoint management, and middleware configuration.*

121. APPSolve's scope in Oracle Integration Cloud engagements covers: integration design (technical architecture, connection design, data flow design); integration build (OIC connection configuration, integration flow development, data transformation mapping, error handling); integration testing (SIT execution, UAT support); integration cutover (production deployment, cutover runbook); and hypercare (post-go-live stabilisation). APPSolve does not manage, configure, or support the endpoint systems on either side of the integration. *(Ref: OIC-SCP-001)*

122. One integration is defined as one directional data flow between one source system and one target system. An integration that sends data from System A to System B is one integration. An integration that returns data from System B to System A is a second, separate integration — two integrations must therefore be scoped, estimated, and priced where a bidirectional flow is required. This definition is the basis for APPSolve's integration count and estimate. Where the client uses the word "integration" to mean a business process spanning multiple flows, each directional flow within that process is counted and priced separately. *(Ref: OIC-SCP-002)*

123. The number of integrations in scope for an engagement is agreed and documented in an Integration Inventory during the Scope and Design phase. The Integration Inventory lists every integration by: integration ID, source system, target system, integration type (real-time/batch/file-based), trigger mechanism, frequency, and data payload summary. The signed Integration Inventory is the authoritative scope document for OIC work. *(Ref: OIC-SCP-003)*

124. The client is responsible for holding a valid Oracle Integration Cloud Enterprise (B91110) or Standard (B85207) subscription before integration development commences. APPSolve does not procure, manage, or renew Oracle OIC licences on the client's behalf. The client's Oracle OIC environment must be provisioned and accessible before the build phase commences. *(Ref: OIC-SCP-004)*

125. APPSolve assumes one (1) Production OIC environment and one (1) standard non-production OIC environment, where these are included in the customer's Oracle OIC licence. APPSolve does not provide, procure, or license Oracle OIC environments. The client confirms that both environments are provisioned and accessible before the build phase commences. Additional OIC environments beyond the standard customer subscription require the client to licence them separately from Oracle. *(Ref: OIC-SCP-005)*

126. Integrations not listed in the agreed Integration Inventory at the time of SOW execution constitute a scope addition. Each additional integration requires a formal Change Request that re-prices the additional design, build, test, and cutover effort. The Integration Inventory may be updated by mutual agreement during the Scope and Design phase; changes after Scope and Design closure are subject to the Change Request process. *(Ref: OIC-SCP-006)*

127. Where APPSolve has published OIC accelerators for a specific integration pattern (as documented in W4-INT-001 and OIC_IMPLEMENTATION_PATTERNS.md), the estimate for that integration reflects the accelerator's reuse benefit. The accelerator reduces but does not eliminate design, configuration, and testing effort. The specific effort reduction associated with each accelerator is confirmed in the project estimate. *(Ref: OIC-SCP-007)*

128. APPSolve implements Oracle-to-Oracle integrations (Oracle HCM ↔ Oracle ERP; Oracle HCM ↔ Oracle OCI; Oracle Fusion ↔ Oracle Analytics Cloud) using Oracle's native integration capabilities where available. Native Oracle-to-Oracle connectivity may use Oracle-delivered OTBI extracts, Oracle Integration Cloud, or Oracle-native REST APIs. The preferred mechanism is confirmed during the Scope and Design phase. *(Ref: OIC-SCP-008)*

129. The default integration architecture for APPSolve OIC implementations is point-to-point: one source system sends data directly to one target system via OIC. Point-to-point is preferred for its simplicity, maintainability, and lower design risk compared to hub-and-spoke or enterprise service bus (ESB) patterns. APPSolve does not implement ESB architectures or message broker replacements under a standard OIC engagement. *(Ref: OIC-DES-001)*

130. Orchestration integrations — flows where OIC coordinates data between three or more systems in a single integration transaction — are not included in the standard point-to-point scope. Where the client's business process requires multi-step orchestration, APPSolve assesses the orchestration design as a separately scoped item. Orchestration integrations typically carry higher design and testing complexity and are priced accordingly. *(Ref: OIC-DES-002)*

131. Standard Oracle-delivered adapters are the default mechanism for all OIC connections. APPSolve uses Oracle's published adapter catalogue (Oracle Fusion Applications adapter, REST adapter, SOAP adapter, File adapter, FTP adapter, Database adapter, and available pre-built connectors). Where no Oracle-delivered adapter exists for a target system, APPSolve uses the Oracle REST or SOAP adapter with the vendor's published API. Custom adapter development is excluded. *(Ref: OIC-DES-003)*

132. APPSolve produces an Integration Inventory and a Technical Design Document (TDD) for each integration in scope. The TDD covers: connection design, trigger mechanism and frequency, payload structure, data transformation logic, error handling approach, and retry strategy. The client reviews and approves the TDD before build commences. Changes to an approved TDD after build commencement constitute a Change Request. *(Ref: OIC-DES-004)*

133. Where a third-party system does not support a REST or SOAP API for integration, SFTP file-based integration is the standard fallback mechanism, subject to the customer's IT security approval of the SFTP connectivity approach. File-based integrations use the Oracle FTP Adapter. The client confirms the SFTP server host, port, directory path, file format, and file naming convention before file-based integration design commences. Where the client's system supports neither API nor SFTP, or where the client's security policy does not permit SFTP-based integration, the integration approach requires assessment before it can be included in scope. *(Ref: OIC-DES-005)*

134. REST API integration is preferred over SOAP where both protocols are available from the vendor. Where SOAP is the only available protocol, APPSolve implements the SOAP integration using Oracle's SOAP adapter. Protocol selection is documented in the Integration Inventory and TDD. *(Ref: OIC-DES-006)*

135. Where an applicable OIC accelerator exists in APPSolve's integration pattern library (W4-INT-001), the accelerator is used as the starting point for integration design. Accelerator applicability is assessed per integration during the estimation phase — no automatic effort discount is applied. Where an accelerator is confirmed applicable, the actual effort reduction is documented explicitly in the project estimate. Accelerator reuse does not eliminate design, testing, or cutover effort; it reduces the build component of effort for the specific integration flow covered by the accelerator. *(Ref: OIC-DES-007)*

136. Error handling is included in every integration's design. Standard error handling covers: field-level validation errors (payload does not match schema), connection errors (target system unavailable), transformation errors (data type mismatches), and business validation errors (business rule violation at the target system). Error handling design follows APPSolve's standard error pattern library (OIC_IMPLEMENTATION_PATTERNS.md Section 4). *(Ref: OIC-DES-008)*

137. Retry logic is included in every integration design where technically appropriate. Standard retry configuration: 3 retry attempts with exponential backoff. Custom retry rules (different retry counts, non-standard backoff intervals, or conditional retry based on error type) are assessed per complexity. Retry configuration is documented in the TDD. *(Ref: OIC-DES-009)*

138. All source and target system endpoints are technically available and accessible from Oracle OIC during SIT and UAT. If an endpoint is not available during the agreed testing window, SIT or UAT for that integration is deferred. Timeline impact arising from endpoint unavailability is the client's risk. *(Ref: OIC-END-001)*

139. The client provides all technical endpoint connection details — including: API base URL, authentication credentials (username/password, API key, OAuth client ID/secret), SSL certificate information, SFTP host/port/directory/credentials, and any endpoint-specific connection parameters — before the design phase commences. APPSolve cannot begin integration design without complete endpoint specifications. *(Ref: OIC-END-002)*

140. Where a third-party system is involved in the integration (for example, a payroll system, background check provider, banking platform, or HR portal), the third-party vendor is responsible for providing: API documentation, a sandbox environment for development and testing, technical support during integration testing, and timely response to integration queries. APPSolve facilitates the integration from the Oracle OIC side; it does not provide third-party vendor technical support. *(Ref: OIC-END-003)*

141. Where a third-party vendor does not provide a sandbox environment for development, APPSolve uses mock data and mocked endpoint responses during the development phase. The client acknowledges that mock-based development may not surface all integration issues until SIT against the real endpoint commences. Production credentials and the live endpoint must be available before SIT commences. *(Ref: OIC-END-004)*

142. If a third-party endpoint system is unavailable during agreed SIT or UAT testing windows due to vendor issues (planned maintenance, API downtime, API version changes, infrastructure problems), APPSolve cannot be held responsible for testing delays caused by vendor unavailability. The client is responsible for managing the vendor relationship and escalating endpoint availability issues to the vendor. *(Ref: OIC-END-005)*

143. Oracle Fusion HCM and Oracle Fusion ERP endpoints use Oracle's standard REST APIs published in Oracle's API documentation. APPSolve designs HCM/ERP integrations using Oracle-standard REST endpoints. Custom Oracle Fusion endpoints (custom-developed APEX APIs, bespoke PaaS extensions) require assessment and are not assumed to follow Oracle's standard API patterns. *(Ref: OIC-END-006)*

144. The client is responsible for procuring all SSL/TLS certificates required to establish secure HTTPS connectivity between Oracle OIC and endpoint systems. This includes: server certificates for client-managed SFTP servers; certificates required for mutual TLS (mTLS) integrations; any custom certificates required by the third-party vendor. Certificate procurement from certificate authorities (CAs), vendors, or internal PKI systems is the client's responsibility. *(Ref: OIC-CERT-001)*

145. All SSL/TLS certificates required for integration connectivity must be provided to APPSolve before SIT commences. Where certificates are not available at SIT commencement, SIT for the affected integrations is deferred until certificates are available. Timeline impact from delayed certificate availability is the client's risk. *(Ref: OIC-CERT-002)*

146. APPSolve installs and configures all provided certificates in Oracle OIC — including importing certificates into OIC's certificate management, configuring connections to use the correct certificate, and validating that certificate-secured connections are functional. Certificate installation in endpoint systems is the client's or vendor's responsibility. *(Ref: OIC-CERT-003)*

147. Oracle OIC's own platform certificate (the OIC platform's public HTTPS certificate) is an Oracle-managed certificate included in the Oracle OIC subscription. APPSolve does not procure or manage Oracle OIC's platform certificate. *(Ref: OIC-CERT-004)*

148. Post-go-live certificate lifecycle management — including certificate expiry monitoring, certificate renewal before expiry, and updating expired certificates in Oracle OIC — is the client's IT team's responsibility. APPSolve may assist with certificate renewal updates in OIC during a managed services or AMS engagement, but not under a standard implementation project. *(Ref: OIC-CERT-005)*

149. Business data mapping decisions — which source system field maps to which target system field, and what business rule governs the mapping — are the client's responsibility. The client's functional team or business analyst is the owner of business mapping decisions. APPSolve facilitates mapping workshops, documents the outcomes, and implements the approved mappings in OIC. *(Ref: OIC-MAP-001)*

150. APPSolve conducts data mapping workshops with the client's functional team during the Scope and Design phase. Workshop outputs: a complete Mapping Specification document listing every source field, target field, transformation rule, and default value for each integration. APPSolve produces the Mapping Specification; the client reviews and approves it. *(Ref: OIC-MAP-002)*

151. A signed Mapping Specification is a mandatory prerequisite before integration build commences. APPSolve will not commence building an integration whose mapping has not been approved by the client. Where mapping workshops are delayed, the integration build is deferred and the project timeline is extended accordingly. *(Ref: OIC-MAP-003)*

152. Data transformation logic — including lookups (translating a source code to a target code), calculations (deriving a target value from source values), conditional logic (different mapping rules for different record types), and string manipulations — is implemented by APPSolve in OIC based on the client-approved Mapping Specification. APPSolve does not make business transformation decisions independently. *(Ref: OIC-MAP-004)*

153. Code-set translations — where source and target systems use different code values for the same business concept (for example, source system uses department code "10" where the target system uses "DEPT-010") — are the client's responsibility to define. The client provides complete source-to-target code mapping tables before the mapping workshop for all applicable code sets (department codes, cost centre codes, employee status codes, pay type codes, location codes, and equivalent). APPSolve implements the translation in OIC based on the client-provided lookup table. *(Ref: OIC-MAP-005)*

154. Changes to an approved Mapping Specification after integration build has commenced constitute a Change Request. The impact of mapping changes on build, testing, and re-testing effort is assessed and agreed before changes are implemented. Minor mapping corrections (factual errors in the approved mapping) are distinguished from mapping scope changes (new fields, new transformation rules, new code sets) in the Change Request assessment. *(Ref: OIC-MAP-006)*

155. OIC integrations are designed for normal business transaction volumes as defined in the Integration Inventory. The client provides estimated transaction volumes — messages per hour (for real-time integrations), file sizes and record counts (for batch/file-based integrations), and peak volume periods — before the design phase. OIC design assumes these volumes will not be exceeded in production without prior notification and design review. *(Ref: OIC-PERF-001)*

156. Load testing and stress testing — including testing at projected peak volume, testing at multiples of expected volume to identify breaking points, and sustained-load testing — are excluded from standard OIC scope. Where the client requires load testing, this is assessed and priced as a scope addition. *(Ref: OIC-PERF-002)*

157. Performance tuning beyond standard Oracle OIC configuration is excluded from standard scope. APPSolve configures Oracle OIC using Oracle's recommended configuration practices. Bespoke performance tuning, custom Oracle OIC instance configuration, or infrastructure-level tuning of Oracle OIC resources are Oracle's responsibility for the managed OIC platform. *(Ref: OIC-PERF-003)*

158. Oracle OIC Enterprise (B91110) has published message volume limits and platform constraints (messages per hour, maximum payload size, maximum concurrent connections) as defined by Oracle's current product documentation. APPSolve designs integrations within these limits. The client is responsible for selecting an Oracle OIC licence tier (Standard vs Enterprise) that provides sufficient message capacity for their expected volumes. Licence tier selection is the client's commercial decision. *(Ref: OIC-PERF-004)*

159. Where the estimated transaction volumes provided by the client materially understate actual production volumes (for example, actual volumes exceed estimated volumes by more than 50%), the integration design may require review. APPSolve flags this risk during design if estimated volumes appear atypically low. The client is responsible for providing accurate volume estimates. *(Ref: OIC-PERF-005)*

160. Standard Oracle OIC monitoring capability is configured as part of every OIC implementation. This includes: Oracle OIC Activity Stream (real-time view of integration executions); Oracle OIC Error Management console (view and resubmit failed messages); Oracle OIC Dashboard (integration health summary); and Oracle OIC Alerts (notification of failed integrations). APPSolve configures these standard monitoring tools as part of the implementation. *(Ref: OIC-MON-001)*

161. APPSolve configures Oracle OIC error notification alerts to send email notifications when an integration fails. Error notification emails are sent to: (1) the customer's nominated integration support mailbox — configured at project outset and confirmed by the client during Scope and Design; and (2) APPSolve's integration support mailbox during the hypercare period only. After hypercare, APPSolve's mailbox is removed from the error notification configuration. Post-hypercare monitoring and error response is the customer's operational team's responsibility unless an APPSolve AMS agreement is in place. *(Ref: OIC-MON-002)*

162. Custom monitoring dashboards — external to the Oracle OIC native monitoring interface — are excluded from standard scope. This includes: custom BI dashboards showing integration volume or error trends; integration monitoring portals built on top of Oracle OIC data; or Grafana/Kibana-style operational monitoring dashboards. Where a client requires integration monitoring beyond OIC's native tools, this is assessed as a scope addition. *(Ref: OIC-MON-003)*

163. Third-party monitoring platform integration — connecting Oracle OIC monitoring data to Splunk, Dynatrace, New Relic, Datadog, IBM Instana, or any equivalent observability platform — is excluded from standard OIC scope. Where the client requires third-party observability platform integration, this is assessed as a separately scoped integration. *(Ref: OIC-MON-004)*

164. Post-go-live monitoring ownership is the client's IT operations team. After hypercare, the client's operations team monitors Oracle OIC error dashboards, responds to alert emails, investigates and resubmits failed messages, and escalates persistent integration failures to Oracle Support or APPSolve AMS (if under a managed services agreement). APPSolve does not actively monitor client OIC environments post-hypercare under a standard implementation contract. *(Ref: OIC-MON-005)*

---

## Section D — Oracle Cloud Infrastructure Assumptions

*This section covers all OCI infrastructure provisioning, networking, compute, storage, database, and operations assumptions.*

165. APPSolve deploys OCI environments using Oracle's Landing Zone framework as the baseline configuration. The standard Landing Zone includes: compartment structure, identity domains, basic IAM policies, default tagging framework, and budget alerts. Customisation beyond the standard Landing Zone baseline is scoped separately. *(Ref: OCI-LZ-001)*

166. The standard APPSolve OCI Landing Zone delivers three compartments as a minimum: Production, Non-Production (two environments: Dev/Test combined and UAT separate), and Shared Services. The two non-production environments (Dev/Test combined and UAT separate) are the standard delivery model. Engagements requiring three separate non-production environments (Dev, Test, UAT fully independent) are treated as an expanded scope item. Additional compartments for separate business units, subsidiary entities, or regulatory isolation are out of scope unless explicitly included in the SOW. *(Ref: OCI-LZ-002)*

167. Landing Zone deployment is assumed to be a greenfield deployment into a new OCI tenancy. If the client has an existing OCI tenancy with existing resources, a tenancy audit is required before Landing Zone deployment. The tenancy audit is a separate billable activity not included in standard Landing Zone effort. *(Ref: OCI-LZ-003)*

168. APPSolve delivers the Landing Zone configuration as infrastructure-as-code (Terraform via OCI Resource Manager). The client receives the IaC artefacts at project close. Ongoing maintenance of the IaC repository post-handover is the client's responsibility unless covered by an AMS SOW. *(Ref: OCI-LZ-004)*

169. The standard Landing Zone includes one set of default tagging policies covering: environment (Production/Non-Production), cost centre, project, and owner. Custom tagging taxonomies beyond this set are out of scope unless explicitly included. *(Ref: OCI-LZ-005)*

170. Budget alerts are configured at tenancy level and compartment level as part of the standard Landing Zone. Alert thresholds are set based on client-provided budget data. APPSolve does not define the client's OCI budget — the client provides the approved budget values before Landing Zone configuration begins. *(Ref: OCI-LZ-006)*

171. APPSolve's Landing Zone does not include multi-cloud federation (e.g., Azure Arc, AWS Control Tower integration). If the client requires OCI resources to be visible in a multi-cloud management plane, this is a separate scope item. *(Ref: OCI-LZ-007)*

172. The Landing Zone does not include automatic resource lifecycle management (auto-shutdown of non-production environments, automated right-sizing). These capabilities are available as optional add-on services and are scoped separately if required. *(Ref: OCI-LZ-008)*

173. APPSolve assumes OCI Resource Manager (ORM) as the Terraform execution environment. If the client requires a self-managed Terraform pipeline (e.g., GitLab CI/CD, GitHub Actions), pipeline integration is a separate scope item. *(Ref: OCI-LZ-009)*

174. Post-Landing Zone, APPSolve hands over a Landing Zone Runbook documenting compartment structure, IAM policies, tagging taxonomy, and operational procedures. The Runbook is a standard deliverable. Bespoke operational procedure manuals beyond the standard Runbook are out of scope. *(Ref: OCI-LZ-010)*

175. OCI Identity and Access Management (IAM) is configured using Oracle Identity Domains as the default. Legacy IDCS-based identity configuration is not used for new engagements. If the client has an existing IDCS configuration, migration to Identity Domains is a separate scoped item. *(Ref: OCI-IAM-001)*

176. APPSolve configures a standard set of IAM groups and policies covering: tenancy administrators, compartment administrators, network administrators, security administrators, database administrators, and read-only auditors. Custom groups beyond this standard set require explicit scoping. *(Ref: OCI-IAM-002)*

177. Federation with the client's corporate identity provider (e.g., Microsoft Entra ID / Azure AD, Okta, ADFS) is included in scope where explicitly stated in the SOW. Federation configuration requires the client's identity team to provide SAML metadata and federation approval. APPSolve cannot configure federation without client identity team participation. *(Ref: OCI-IAM-003)*

178. APPSolve assumes a single Identity Domain for the engagement. Multiple Identity Domains (e.g., separate domains for employees vs. contractors, or for separate business units) are out of scope unless explicitly included. Each additional Identity Domain may require separate Oracle licensing. *(Ref: OCI-IAM-004)*

179. Privileged Access Management (PAM) tooling integration (e.g., CyberArk, BeyondTrust, Delinea) with OCI IAM is not included in the standard engagement. PAM integration is a specialist security scope item requiring a separate SOW or sub-contract with a security specialist. *(Ref: OCI-IAM-005)*

180. Service accounts for APPSolve automation (Terraform, ORM, monitoring agents) are created with least-privilege policies. These service accounts are handed over to the client at project close. APPSolve does not retain access to client tenancies after project close unless covered by an AMS SOW. *(Ref: OCI-IAM-006)*

181. APPSolve assumes the client will designate at least one internal OCI tenancy administrator who holds credentials to the tenancy administrator group. This is a client responsibility. APPSolve will not be the sole administrator of a production tenancy. *(Ref: OCI-IAM-007)*

182. Multi-Factor Authentication (MFA) policy is enabled by default for all IAM users accessing the OCI Console. APPSolve configures MFA enforcement as a standard security baseline. Disabling MFA requires explicit written client approval and is documented as a risk-accepted variance. *(Ref: OCI-IAM-008)*

183. OCI IAM policy design uses the principle of least privilege. All policies are reviewed against Oracle's security baseline before handover. APPSolve does not configure open or wildcard policies (e.g., "Allow any-user to manage all-resources in tenancy") in production environments. *(Ref: OCI-IAM-009)*

184. Emergency Break-Glass access procedures are documented as part of the Landing Zone Runbook. The client's tenancy administrator team is responsible for Break-Glass procedure maintenance after handover. APPSolve does not hold Break-Glass credentials to client tenancies post-project. *(Ref: OCI-IAM-010)*

185. APPSolve designs and deploys Virtual Cloud Networks (VCNs) according to Oracle's networking best practices. The standard deployment includes one VCN per major environment (Production, Non-Production). Additional VCNs for specific workload isolation (e.g., DMZ, partner networks) are out of scope unless explicitly included. *(Ref: OCI-NET-001)*

186. VCN address space (CIDR) is assigned by the client's network team before OCI networking configuration begins. APPSolve does not allocate IP address ranges without client network team confirmation. CIDR conflicts with existing on-premise or cloud networks are a client responsibility to identify before design sign-off. *(Ref: OCI-NET-002)*

187. On-premise to OCI connectivity is implemented via IPSec VPN as the default for most client profiles. APPSolve recommends upgrading to FastConnect (dedicated circuit) when any of the following conditions apply: sustained bandwidth requirement exceeds 100 Mbps, the engagement has more than 100 concurrent users accessing OCI-hosted applications, the OIC or integration layer requires sub-second OCI-to-on-premise latency, or the DR design specifies an RTO of less than 2 hours. FastConnect requires a separate commercial engagement with a FastConnect partner and is separately priced in all cases. *(Ref: OCI-NET-003)*

188. IPSec VPN configuration requires the client's network team to provide VPN gateway IP addresses, pre-shared keys, and routing information. APPSolve cannot configure the OCI VPN without the corresponding on-premise VPN configuration being provided. VPN commissioning requires coordination windows that must be agreed in the project schedule. *(Ref: OCI-NET-004)*

189. The standard network design uses a Hub-and-Spoke topology with a dedicated network VCN (hub) connected to spoke VCNs via Local Peering Gateways or OCI Network Firewall. Flat single-VCN designs are available for simple or single-workload engagements at client request. *(Ref: OCI-NET-005)*

190. OCI Service Gateway is enabled by default to allow OCI resources to access Oracle Services (Object Storage, Autonomous Database) without traversing the public internet. Internet Gateway is enabled only where explicitly required (e.g., for public-facing application tiers). Private OCI deployments without public internet access are the default security posture. *(Ref: OCI-NET-006)*

191. DNS resolution for OCI resources uses OCI Private DNS zones for internal resolution. External DNS (public-facing) is managed by the client's DNS provider. APPSolve configures OCI Private DNS records as part of the engagement. External DNS record management is the client's responsibility. *(Ref: OCI-NET-007)*

192. Network Security Groups and Security Lists are configured at minimum to restrict traffic between tiers (web, application, database). Port-level firewall rules are defined in the network design document, which requires client approval before deployment. APPSolve does not open unrestricted ports in production environments. *(Ref: OCI-NET-008)*

193. OCI Network Firewall (where required) is an additional licensed OCI service. If the client requires deep packet inspection, IDS/IPS, or URL filtering beyond NSG/Security List capabilities, OCI Network Firewall must be included in the OCI subscription and is separately scoped. *(Ref: OCI-NET-009)*

194. Load Balancing is included where specified in the SOW (e.g., for EBS web tier HA, APEX public access). The standard configuration uses OCI's flexible load balancer. Application-specific load balancer tuning (session persistence, health check configurations) is included for the named application. Generic infrastructure load balancers not tied to a specific application are out of scope. *(Ref: OCI-NET-010)*

195. OCI Bastion Service is configured as the standard secure access mechanism for administrative access to OCI resources. Direct public IP access to compute instances is not provisioned in production environments. Access to production compute requires Bastion Session initiation. *(Ref: OCI-NET-011)*

196. Third-party network appliances (e.g., Palo Alto, Fortinet, Cisco ASA on OCI) are out of scope. APPSolve delivers OCI-native networking components only. If the client requires third-party network appliances on OCI, this is a specialist network scope item requiring a separate SOW. *(Ref: OCI-NET-012)*

197. Compute instance sizing (shape, OCPU count, memory) is based on the sizing requirements provided by the application team or derived from the client's existing on-premise workload specifications. APPSolve does not independently validate application performance requirements — sizing is based on client-provided or Oracle-recommended specifications for the specific application. *(Ref: OCI-CMP-001)*

198. The standard compute shape uses Oracle's Flexible shapes (VM.Standard.E4.Flex or VM.Standard3.Flex) unless a specific shape is required by the application (e.g., bare metal for high-performance databases, GPU shapes for analytics workloads). Shape selection is documented in the design and approved by the client before provisioning. *(Ref: OCI-CMP-002)*

199. APPSolve provisions compute instances with Oracle Linux as the default operating system unless the application requires a specific certified OS (e.g., RHEL for EBS, Windows Server for Windows-based applications). For EBS on OCI, the OS selection (Oracle Linux or RHEL) is confirmed at design sign-off in consultation with the client; both are valid EBS-certified platforms and the choice affects ongoing OS support costs and patching tooling. OS licensing for non-Oracle operating systems is the client's responsibility to procure. *(Ref: OCI-CMP-003)*

200. Operating system hardening is performed to Oracle's baseline OS hardening standards. Additional hardening requirements (CIS Benchmarks, STIG, NIST) are out of scope unless explicitly included. If advanced OS hardening is required, a separate specialist engagement is needed. *(Ref: OCI-CMP-004)*

201. APPSolve provisions compute instances using Terraform/ORM as the deployment mechanism. Manual console-based provisioning is not used for production environments. All compute configuration is codified in the IaC repository provided at project close. *(Ref: OCI-CMP-005)*

202. Auto-scaling of compute resources (instance pools, autoscaling configurations) is configured where explicitly required by the application design (e.g., for OIC compute nodes, APEX web tier scaling). Auto-scaling is not assumed by default for all compute workloads. *(Ref: OCI-CMP-006)*

203. Compute high availability within a single region uses Availability Domain or Fault Domain placement strategies as appropriate for the region and application. Multi-AD HA and Fault Domain placement are designed per application requirements and documented in the architecture design document. *(Ref: OCI-CMP-007)*

204. Compute instance backup (boot volume backups) is configured as part of the standard deployment for production instances. Backup frequency and retention period are agreed with the client before configuration. Non-production instance backups are optional and not assumed by default. *(Ref: OCI-CMP-008)*

205. OCI Object Storage is used for: database backups, application file exports, OCI audit log archiving, and static content hosting where applicable. Object Storage bucket structure, lifecycle policies, and access controls are defined in the storage design document and approved before provisioning. *(Ref: OCI-STO-001)*

206. Object Storage bucket access is private by default. Public buckets are not configured without explicit client approval. Pre-Authenticated Requests are used for controlled temporary external access. APPSolve does not configure permanent public read access to Object Storage buckets in production environments. *(Ref: OCI-STO-002)*

207. Block Volume storage sizing for compute instances is based on client-provided storage requirements. APPSolve does not independently validate application storage growth projections. Storage capacity planning is the client's responsibility; APPSolve provisions what is specified. Block Volume expansion is a straightforward operational action and does not require a Change Request. *(Ref: OCI-STO-003)*

208. Block Volume performance tier (Balanced, Higher Performance, Ultra High Performance) is selected based on application I/O requirements. For database workloads, Higher Performance or Ultra High Performance tiers may be required. Performance tier selection is documented and approved before provisioning. *(Ref: OCI-STO-004)*

209. File Storage Service (NFS) is included where the application requires shared file system access across multiple compute instances (e.g., EBS shared application tier, multi-node middleware). File Storage Service is not assumed by default — it is only provisioned where explicitly required by the application design. *(Ref: OCI-STO-005)*

210. Object Storage lifecycle policies are configured to transition objects from Standard to Infrequent Access or Archive tiers based on client-defined age thresholds. Default lifecycle policy: Standard for 30 days, Infrequent Access for 60 days, then Archive. Clients may override these thresholds in the storage design document. *(Ref: OCI-STO-006)*

211. APPSolve does not configure cross-region Object Storage replication as part of the standard engagement. Cross-region replication for DR Object Storage is included only where the DR design explicitly requires it and is separately scoped. *(Ref: OCI-STO-007)*

212. Storage encryption uses Oracle-managed keys by default. Customer-managed key integration with OCI Vault for Block Volumes and Object Storage is available as an optional capability and must be explicitly included in the SOW if required by the client's security policy. *(Ref: OCI-STO-008)*

213. Oracle Database on OCI is deployed as a Virtual Machine DB System for standard enterprise workloads unless a specific database service type is required (e.g., Exadata Cloud Service for high-performance EBS, Autonomous Database for analytics/reporting). The database service type is confirmed in the design and approved before provisioning. *(Ref: OCI-DB-001)*

214. Oracle Database licensing for OCI DB Systems defaults to Bring Your Own License (BYOL). BYOL assumes the client holds current Oracle Database software licences that are eligible for use on OCI under Oracle's cloud licensing policies. The pre-sales discovery process must confirm the client's Oracle Database licence position before finalising OCI DB pricing. Where a client confirms they hold no Oracle Database licences (or licences insufficient for the required edition), License Included pricing is used. Proposing BYOL without confirming the client's licence position is not permitted. *(Ref: OCI-DB-002)*

215. APPSolve deploys Oracle Database to the version certified for the application being deployed (e.g., EBS-certified DB version, SOA-certified DB version). Database version selection is confirmed before provisioning. Upgrading to a non-certified database version at client request is a risk-accepted variance requiring client sign-off. *(Ref: OCI-DB-003)*

216. Database High Availability for production Oracle VM DB Systems is implemented using Oracle Data Guard (primary + standby) as the standard default. Data Guard is included in all production VM DB System deployments unless the client provides written risk acceptance for single-instance production. Single-instance production deployments require explicit client sign-off acknowledging the absence of database HA and the implications for RTO/RPO. OCI cost estimates for production VM DB Systems must reflect the dual-node (primary + standby) sizing. Active Data Guard for read-scale-out scenarios is available where licensed and must be explicitly included in scope. *(Ref: OCI-DB-004)*

217. Database Automatic Backups are enabled for all Oracle DB Systems. Production database backup retention is set to 30 days. Non-production database backup retention is set to 7 days. Clients requiring longer production retention periods (e.g., 60 or 90 days for regulatory compliance) must specify this in the SOW; extended retention increases Object Storage costs. Database backups are stored in OCI Object Storage within the same region as the database. *(Ref: OCI-DB-005)*

218. Database Automatic Backups do not replace application-level data exports or logical backups. For EBS on OCI, application-level database exports (Data Pump) are configured separately as part of the EBS design and are not assumed as part of the OCI database configuration. *(Ref: OCI-DB-006)*

219. Oracle Database patching (OS patching, DB software patching) is the client's operational responsibility after handover. APPSolve configures an initial patching schedule and documents the patching runbook as a handover deliverable. Ongoing patch execution is not included in the project scope unless covered by an AMS SOW. *(Ref: OCI-DB-007)*

220. OCI infrastructure DBA activities — Oracle Database patching, RMAN backup and restore operations, Data Guard administration, storage expansion, and OCI DB System availability management — are within the OCI AMS pack scope. Application DBA activities — AWR analysis, SQL performance tuning, schema design, index optimisation, Data Pump export/import — are within the ERP or HCM AMS pack scope as applicable to the hosted application. Application-level DBA activities are not included in the OCI infrastructure scope regardless of whether the database is hosted on OCI. *(Ref: OCI-DB-008)*

221. Autonomous Database deployments are included where the solution specifically requires Autonomous Database services (e.g., Oracle Analytics Cloud data warehouse, APEX with ADB). The provisioning, network configuration, and access setup for Autonomous Database are included. ADB application-level schema design and query optimisation are not included. *(Ref: OCI-DB-009)*

222. Cross-region database replication (for DR purposes) is included only where the DR design explicitly requires it. Cross-region Data Guard configurations are a significant additional effort item and are separately scoped. Single-region database HA does not include cross-region replication. *(Ref: OCI-DB-010)*

223. Oracle GoldenGate on OCI (for real-time replication or migration) is a separate licensed service. If GoldenGate is required for migration or DR, it is explicitly scoped and licensed. GoldenGate is not assumed as part of the standard OCI database delivery. *(Ref: OCI-DB-011)*

224. Database performance benchmarking, stress testing, or capacity planning simulations are not included in the OCI scope. Performance testing of database workloads on OCI is a separate optional activity. The database infrastructure is provisioned to the specified sizing; actual performance validation is the client's responsibility or a separately scoped activity. *(Ref: OCI-DB-012)*

225. Oracle Integration Cloud (OIC) on OCI is provisioned as a managed Oracle PaaS instance. APPSolve provisions and configures the OIC instance; integration flows and adapters are in scope per the Integration pack assumptions, not this OCI pack. OCI network access to OIC (private endpoints, VCN peering) is within this pack's scope. *(Ref: OCI-MW-001)*

226. Oracle Application Express (APEX) on OCI is deployed using Oracle's managed APEX Application Development service unless the application design requires a self-managed APEX installation on a compute instance. The APEX service type (managed vs. self-managed) is confirmed in the design and approved before provisioning. *(Ref: OCI-MW-002)*

227. Oracle WebLogic Server on OCI (for EBS web/DMZ tier or custom JEE applications) is provisioned using the Oracle WebLogic for OCI Marketplace image as the baseline. WebLogic patching post-handover is the client's operational responsibility. *(Ref: OCI-MW-003)*

228. Oracle SOA Suite on OCI (where required for on-premise SOA lift-and-shift) is provisioned using the Oracle SOA for OCI Marketplace image. APPSolve does not re-architect SOA composites during an OCI lift-and-shift engagement. Application-level SOA changes are a separate scope item. *(Ref: OCI-MW-004)*

229. Oracle Analytics Cloud (OAC) on OCI is a managed Oracle PaaS service. OAC provisioning, VCN private access configuration, and initial setup are within scope where explicitly included. OAC content development (dashboards, datasets, analytics flows) is in scope per a separate Analytics or BI engagement, not this OCI pack. *(Ref: OCI-MW-005)*

230. APPSolve assumes Oracle Marketplace images as the deployment baseline for Oracle-branded middleware (WebLogic, SOA, self-managed APEX). Custom OS configuration or software installation outside Oracle Marketplace images requires additional effort and is separately scoped. *(Ref: OCI-MW-006)*

231. Middleware HA configuration (WebLogic cluster, SOA cluster) is included where required by the application design. The HA design is documented and approved before provisioning. Single-node non-HA middleware deployment is the default for non-production environments. *(Ref: OCI-MW-007)*

232. Third-party middleware (IBM MQ, Apache Kafka, MuleSoft, Tibco) on OCI compute is out of scope for the OCI pack. Third-party middleware installation and configuration on OCI requires a separate sub-engagement or sub-contract with the relevant technology specialist. *(Ref: OCI-MW-008)*

233. OCI integration scope covers network connectivity between OCI-hosted applications and external systems (on-premise, SaaS, partner systems). Application-level integration logic (adapters, mappings, flows) is in scope per the Integration pack (OIC/AMS assumptions), not this OCI pack. *(Ref: OCI-INT-001)*

234. OCI API Gateway is provisioned where the solution requires managed API exposure (e.g., APEX APIs, custom OCI Function endpoints). API content (routes, policies, authentication schemes) is configured as part of the API Gateway setup. API design and backend integration logic are not in scope for the OCI pack. *(Ref: OCI-INT-002)*

235. OCI Functions (serverless) is included where the solution design explicitly includes serverless components (e.g., event-driven triggers, lightweight data processing). OCI Function code development is not in scope for the OCI pack — function code is provided by the application team or Integration workstream. *(Ref: OCI-INT-003)*

236. Oracle Streaming Service (Kafka-compatible) is provisioned where the solution design requires event streaming. Topic configuration, partition sizing, and retention periods are defined in the integration design. Application-level message producers and consumers are not in scope for the OCI pack. *(Ref: OCI-INT-004)*

237. File-based integration via OCI (SFTP, AS2, EDI) uses OCI's B2B Service within OIC where applicable. Dedicated SFTP server configuration on OCI compute is an alternative for legacy file-based integrations. The approach is defined per integration point in the integration design document. *(Ref: OCI-INT-005)*

238. OCI Email Delivery service configuration (for application-generated emails from OCI-hosted applications) is included where required. APPSolve configures approved sender domains and suppression lists. The client is responsible for verifying email sender domain ownership via DNS records. *(Ref: OCI-INT-006)*

239. OCI Notifications and Events service configuration (for operational alerting and event-driven automation) is included as part of the monitoring setup (see OCI-MON). Application-level event subscriptions beyond operational monitoring are a separate scope item. *(Ref: OCI-INT-007)*

240. Third-party iPaaS tools (Boomi, Informatica, Talend) hosted on OCI compute are not configured as part of the OCI pack. Third-party iPaaS installation and configuration require a separate sub-engagement or sub-contract with the relevant tool specialist. *(Ref: OCI-INT-008)*

241. OCI backup scope covers: Block Volume Backups, Boot Volume Backups, and Oracle DB System Automatic Backups. Application-level backups (EBS database exports, application tier file backups) are in scope per the respective application pack, not this OCI pack. *(Ref: OCI-BKP-001)*

242. Block Volume and Boot Volume backups are configured using OCI's automatic backup policies. The standard APPSolve backup schedule is: daily incremental (30-day retention), weekly full (60-day retention). Clients may define alternative retention periods in the backup design document. *(Ref: OCI-BKP-002)*

243. Database backups use Oracle's automated RMAN-based backup to OCI Object Storage. Backup windows are configured during low-activity periods agreed with the client. The backup window is confirmed before configuration and documented in the operations runbook. *(Ref: OCI-BKP-003)*

244. Backup restore testing is performed once during the engagement (using a pre-production or staging environment) to validate backup integrity. Ongoing periodic restore testing post-handover is the client's operational responsibility. The restore procedure is documented in the operations runbook. *(Ref: OCI-BKP-004)*

245. Cross-region backup replication is not assumed by default. If the client's DR or data protection policy requires backups to be replicated to a secondary OCI region, this is explicitly included in the DR design and separately scoped (see OCI-DR). *(Ref: OCI-BKP-005)*

246. Third-party backup tools (Veeam, Commvault, Veritas) on OCI are out of scope. APPSolve delivers OCI-native backup services only. Integration of OCI workloads into a third-party backup environment is a separate specialist scope item. *(Ref: OCI-BKP-006)*

247. Backup alerting (failed backup notifications, missed backup schedule alerts) is configured as part of the monitoring setup. Alert delivery uses OCI Notifications to client-designated email addresses. PagerDuty or equivalent on-call alerting tool integration is not included unless explicitly specified. *(Ref: OCI-BKP-007)*

248. Archive-tier backup storage is used for long-term retention where backup data does not require rapid restore capability. Archive retrieval times (typically 1–4 hours for Oracle Archive tier) are documented in the backup runbook. Clients requiring sub-1-hour restore from archive must use Standard or Infrequent Access storage tiers. *(Ref: OCI-BKP-008)*

249. Disaster Recovery (DR) design and implementation is included only where explicitly stated in the SOW. DR is not assumed by default in any OCI engagement. An engagement without an explicit DR SOW item delivers single-region, single-availability-domain infrastructure only. *(Ref: OCI-DR-001)*

250. APPSolve's standard OCI DR approach is a Pilot Light DR configuration: critical infrastructure is provisioned in the DR region in a shut-down or minimal state and can be activated when disaster is declared. Pilot Light DR is always separately priced and is never assumed or included in the base OCI engagement. When DR is required, Pilot Light DR is presented as a named engagement option in the SOW with explicit pricing. Proposals must not include DR assumptions unless DR is explicitly included in the SOW. *(Ref: OCI-DR-002)*

251. Full Active-Active DR (warm standby or hot standby across two regions) is a premium DR configuration and is always separately priced. Active-Active DR typically doubles the OCI infrastructure cost and requires application-level HA support. APPSolve provides Active-Active DR design and implementation as a separately scoped engagement. *(Ref: OCI-DR-003)*

252. Recovery Time Objective (RTO) and Recovery Point Objective (RPO) targets are defined by the client and documented in the DR design before implementation. APPSolve designs the DR architecture to meet the stated RTO/RPO. APPSolve does not independently validate or guarantee RTO/RPO achievement — performance against RTO/RPO is validated in the DR test. *(Ref: OCI-DR-004)*

253. DR testing (DR failover test, DR failback test) is performed once during the engagement as a planned DR test. The DR test is conducted in a controlled window agreed with the client. Failed DR tests require remediation and re-testing; re-test effort is included for one remediation cycle. Multiple remediation cycles are a Change Request. *(Ref: OCI-DR-005)*

254. Database DR uses Oracle Data Guard cross-region standby as the standard database DR mechanism. Application tier DR uses OCI Full Stack DR Service or Pilot Light compute re-provisioning. The DR mechanism per tier is defined in the DR design document. *(Ref: OCI-DR-006)*

255. APPSolve does not deliver or test DR for third-party applications hosted on OCI unless those applications are within the project scope and the DR mechanism is OCI-native. Third-party application DR is out of scope. *(Ref: OCI-DR-007)*

256. DR runbook development is included as a standard deliverable for all DR-scoped engagements. The runbook covers: disaster declaration criteria, activation steps per tier, estimated recovery time, communication contacts, and failback procedure. Runbook maintenance after handover is the client's responsibility. *(Ref: OCI-DR-008)*

257. Network DR (routing failover, DNS failover, load balancer DR) is included as part of the DR design for DR-scoped engagements. DNS TTL reduction before planned DR tests is the client's DNS team responsibility. APPSolve documents the DNS changes required in the DR runbook. *(Ref: OCI-DR-009)*

258. OCI Full Stack DR Service is used where applicable to orchestrate DR failover for supported resource types. Manual DR runbooks are maintained for resource types not supported by Full Stack DR. The combination of automated and manual DR procedures is documented in the DR runbook. *(Ref: OCI-DR-010)*

259. OCI Monitoring (Metrics) is enabled for all provisioned OCI resources. Standard metrics dashboards are configured for: compute CPU/memory/disk utilisation, database performance metrics, network throughput, and Object Storage usage. Custom metrics dashboards beyond the standard set are out of scope. *(Ref: OCI-MON-001)*

260. OCI Logging (service logs, audit logs, custom application logs) is configured for all provisioned OCI services. Log ingestion into OCI Logging Analytics is included where the client has a Logging Analytics subscription. Without a Logging Analytics subscription, raw logs are available in OCI Logging only (90-day retention). *(Ref: OCI-MON-002)*

261. Alerting is configured for the following standard conditions: CPU sustained above 90% for 15 minutes, Memory sustained above 85% for 15 minutes, Disk above 80% used, Database availability below 100%, Backup job failure, and network anomaly. Alert thresholds are adjusted based on client-provided operational baselines. Notifications are delivered to client-designated email addresses. *(Ref: OCI-MON-003)*

262. Third-party monitoring tool integration (Splunk, Dynatrace, Datadog, New Relic) is not included in the standard OCI monitoring configuration. If the client requires OCI metrics and logs to flow to a third-party monitoring platform, this is an optional integration item that must be explicitly included in the SOW. *(Ref: OCI-MON-004)*

263. Application Performance Monitoring (APM) using OCI APM or third-party tools is not included in the standard OCI monitoring scope. APM requires agent installation on application servers and application-level instrumentation. If APM is required, it is a separate scope item. *(Ref: OCI-MON-005)*

264. OCI Operations Insights for database performance analysis is an optional monitoring enhancement. If included, it provides AWR data analysis, capacity planning, and SQL performance insights. Operations Insights is not assumed by default; it must be explicitly included. *(Ref: OCI-MON-006)*

265. A Monitoring Runbook is delivered at project close documenting: dashboard locations, alert configurations, alert response procedures, and escalation contacts. Runbook maintenance after handover is the client's responsibility. *(Ref: OCI-MON-007)*

266. Uptime monitoring and SLA reporting are not included in the standard OCI monitoring scope. If the client requires uptime SLA reports (e.g., 99.9% availability reporting), this is configured as part of an AMS Managed OCI Services SOW, not a project delivery engagement. *(Ref: OCI-MON-008)*

267. APPSolve delivers OCI infrastructure in a project mode. Operations begin at project close when the client's operational team takes responsibility. Operational readiness (team training, runbook review, first-month hypercare) is a standard project close activity. Post-hypercare ongoing operations are covered by an AMS SOW if required. *(Ref: OCI-OPS-001)*

268. OS Management Hub is enabled on Oracle Linux instances for centrally managed OS patching. APPSolve configures the initial patching groups and schedule. Patch approval and execution after project close is the client's operational responsibility unless covered by an AMS SOW. Under a Managed OCI Services AMS SOW, the standard APPSolve patching cadence is quarterly (OS patches and DB patch bundles applied in a quarterly maintenance window). Monthly patching cadence is available as a premium tier where the client's risk profile or regulatory obligations require more frequent patching cycles. Critical Security Patch Updates (CPU) issued by Oracle are applied within 30 days of Oracle release under all AMS tiers regardless of the standard cadence. *(Ref: OCI-OPS-002)*

269. Oracle Cloud Lift (OCI's free implementation assistance program) resources are not assumed to be available for any client engagement. APPSolve scopes and prices its OCI work independently of Oracle Cloud Lift availability. *(Ref: OCI-OPS-003)*

270. OCI Governance rules (Quotas, Budget Alerts, Compartment-level policies) are configured during delivery to prevent resource sprawl. Post-handover, quota management is the client's tenancy administrator responsibility. APPSolve documents the quota configuration in the operations runbook. *(Ref: OCI-OPS-004)*

271. Change management for OCI infrastructure post-handover follows the client's internal IT change management process. APPSolve does not manage the client's change advisory board process. Changes to OCI infrastructure during the project delivery phase follow APPSolve's project-mode change process per COMMERCIAL_GOVERNANCE.md. *(Ref: OCI-OPS-005)*

272. Scheduled maintenance windows for OCI patching, database patching, and planned changes are agreed with the client before the operational handover. Maintenance windows outside South Africa business hours may apply for production changes. Coordination with the client's IT operations team is required for all production maintenance activities. *(Ref: OCI-OPS-006)*

273. APPSolve provides operational handover training to the client's designated OCI administrator team. The standard training package covers: OCI Console navigation, key monitoring dashboards, backup verification, alert acknowledgement, and escalation procedures. Advanced OCI administrator training is a separate scope item. *(Ref: OCI-OPS-007)*

274. Incident management post-handover uses the client's incident management tooling (ServiceNow, Jira Service Desk, etc.). APPSolve does not provide an incident management platform. Under an AMS SOW, APPSolve integrates with the client's ITSM tool for AMS-managed incidents. *(Ref: OCI-OPS-008)*

275. OCI migration scope is explicitly defined in the Migration Plan document, which is a mandatory deliverable for any OCI migration engagement. The Migration Plan defines: migration approach (lift-and-shift, re-platform, re-architecture), migration sequence, rollback criteria, and acceptance criteria for each migrated workload. *(Ref: OCI-MIG-001)*

276. APPSolve supports the following OCI migration approaches: (a) Lift-and-Shift using OCI VM migration tools or manual replication; (b) Database migration using Oracle Zero Downtime Migration (ZDM); (c) Application re-platform using Oracle Marketplace images. Migration approach per workload is confirmed in the Migration Plan. *(Ref: OCI-MIG-002)*

277. Zero Downtime Migration (ZDM) is the preferred database migration tool for Oracle Database migrations to OCI. ZDM minimises downtime using online data transfer and redo log shipping. ZDM requires access to both source and target database environments. If ZDM is not viable (source DB version incompatibility, network restrictions), an alternative migration approach is documented and approved. *(Ref: OCI-MIG-003)*

278. Pre-migration workload assessment is a prerequisite for all OCI migrations. APPSolve performs a pre-migration assessment covering: source environment inventory, dependency mapping, network connectivity requirements, and cutover risk assessment. Assessment results are documented before migration execution begins. *(Ref: OCI-MIG-004)*

279. Migration cutover is a planned event with an agreed cutover window (typically a weekend). APPSolve provides APPSolve resources during the cutover window as specified in the project plan. Extended cutover windows (greater than 48 hours) require explicit resourcing agreement and may involve additional cost. *(Ref: OCI-MIG-005)*

280. Rollback capability is maintained during the migration cutover window. The rollback plan is documented in the Migration Plan. After the client signs the migration acceptance sign-off, rollback is no longer supported. Rollback after acceptance sign-off constitutes a new project activity. *(Ref: OCI-MIG-006)*

281. Source environment decommissioning is the client's responsibility. APPSolve does not decommission on-premise servers, SAN storage, or data centre infrastructure as part of an OCI migration engagement. APPSolve may provide a decommissioning checklist but does not execute decommissioning actions. *(Ref: OCI-MIG-007)*

282. Data migration for large volumes (greater than 10 TB) requires a data transfer strategy review. Options include: OCI FastConnect-based bulk transfer, Oracle Data Transfer Appliance (physical media), or direct internet transfer with compression. The data transfer strategy is confirmed in the Migration Plan based on available bandwidth and timeline. *(Ref: OCI-MIG-008)*

283. Parallel running of source and OCI target environments during migration testing is the recommended approach. Parallel run costs (double infrastructure, network, licensing) are the client's responsibility. The parallel run period is defined in the Migration Plan and ends at acceptance sign-off. *(Ref: OCI-MIG-009)*

284. Application compatibility validation (confirming the migrated application behaves identically on OCI as on-premise) is the client's and application vendor's responsibility. APPSolve ensures the OCI infrastructure meets the application's documented system requirements. Application-level functional testing is in scope per the application pack, not the OCI pack. *(Ref: OCI-MIG-010)*

285. Third-party application migration (non-Oracle applications co-resident with Oracle on on-premise infrastructure) is out of scope for the OCI pack. APPSolve migrates Oracle workloads defined in the SOW. Third-party applications sharing the same physical infrastructure require separate migration planning. *(Ref: OCI-MIG-011)*

286. Post-migration performance validation is included as a standard migration deliverable. APPSolve validates that the migrated workload on OCI meets the documented performance baseline established from the pre-migration assessment. A pre-migration performance baseline must be established and agreed before migration execution begins; without a baseline, post-migration performance validation cannot be performed. OCI infrastructure performance issues identified within 30 calendar days of client acceptance sign-off are treated as migration defects and remediated within the project scope. Performance issues identified after 30 days are treated as operational matters and handled under AMS or a new engagement. Application-level performance issues (slow queries, application code inefficiencies, integration bottlenecks) are excluded from the 30-day infrastructure performance warranty. *(Ref: OCI-MIG-012)*

287. APPSolve designs OCI infrastructure to Oracle's documented sizing guidelines for the applicable application (EBS on OCI Sizing Guide, OIC performance guidelines, etc.). APPSolve does not independently develop performance models for applications not covered by Oracle's documented sizing guidelines. *(Ref: OCI-PER-001)*

288. Performance testing (load testing, stress testing, soak testing) of OCI-hosted applications is not included in the standard OCI delivery. If performance testing is required, it is a separate scope item. Performance testing against production OCI environments requires advance coordination and a maintenance window. *(Ref: OCI-PER-002)*

289. OCI Compute auto-scaling (instance pools) is configured where the application design requires dynamic scaling. Auto-scaling triggers are defined based on CPU/memory metrics. Application-level validation that the application handles OCI auto-scaling correctly is the application team's responsibility. *(Ref: OCI-PER-003)*

290. Network bandwidth between OCI and on-premise environments is a significant performance variable. IPSec VPN bandwidth limitations may impact performance for high-volume OCI integrations. APPSolve documents network bandwidth requirements in the architecture design; if bandwidth is insufficient, FastConnect upgrade is recommended as a separate commercial item. *(Ref: OCI-PER-004)*

291. OCI Storage I/O performance (Block Volume IOPS) is provisioned based on application requirements specified before implementation. APPSolve does not conduct production I/O profiling of existing on-premise workloads unless a pre-migration assessment is explicitly included in the SOW. *(Ref: OCI-PER-005)*

292. Database performance on OCI VM DB Systems is subject to the compute shape selected and Block Volume I/O performance tier. APPSolve recommends the appropriate shape and I/O tier based on the sizing assessment. Sub-optimal performance caused by incorrect sizing information provided by the client is not a delivery defect. *(Ref: OCI-PER-006)*

293. APPSolve does not provide performance guarantees (SLA-backed response times, guaranteed throughput) for OCI infrastructure as part of a project delivery. Performance SLAs are a feature of AMS Managed OCI Services SOWs only. *(Ref: OCI-PER-007)*

294. Compute right-sizing recommendations are provided as part of the standard delivery and updated at the 30-day post-go-live review. Right-sizing actions post-review are the client's operational responsibility unless covered by an AMS SOW. *(Ref: OCI-PER-008)*

---

## Section E — Managed Application Services (AMS) Assumptions

*This section covers all managed services delivery assumptions including service scope, hours, change management, SLA framework, dedicated resource model, release management, and OCI support.*

295. APPSolve AMS scope is limited to the applications and modules explicitly listed in the AMS agreement. Support for an application or module not named in the AMS agreement is excluded. Adding a new application to an existing AMS agreement requires a scope change to the AMS contract. *(Ref: AMS-SCP-001)*

296. APPSolve provides Level 2 and Level 3 application and technical support only. Level 1 support — the first point of contact for users with questions or requests, service desk ticket creation, user communication, and first-line triage — remains the client's responsibility unless Level 1 support is explicitly contracted as an add-on service. *(Ref: AMS-SCP-002)*

297. Level 2 support covers: functional configuration questions and configuration adjustments within the existing system design; application error investigation and diagnosis; user access and security role assignment support where this has been delegated to APPSolve; data correction assistance for system-originated data issues; workflow configuration adjustments (approval routing changes that do not constitute structural redesign); and report adjustments within the existing report framework. *(Ref: AMS-SCP-003)*

298. Level 3 support covers: technical investigation of Oracle platform issues, Oracle SR (Service Request) management with Oracle Support, integration error investigation (OIC / BeBanking H2H), performance issue diagnosis, and complex configuration issues requiring senior Oracle or Acumatica certified expertise. *(Ref: AMS-SCP-004)*

299. Oracle Application Managed Services support is scoped to the Oracle applications configured and delivered during the implementation. APPSolve does not support Oracle applications not configured by APPSolve, or applications configured by other parties, without a separate scope assessment and onboarding engagement. *(Ref: AMS-SCP-005)*

300. BeBanking AMS support covers: OIC integration error investigation for BeBanking H2H flows; file format and payment file query handling; BeBanking connectivity issue escalation to BeBanking; and bank statement import troubleshooting. BeBanking AMS is only available where Carin Webb (sole BeBanking OIC resource) is available — see CONSULTANT_SKILL_MATRIX.md SPOF note. *(Ref: AMS-SCP-006)*

301. Acumatica AMS support covers: Acumatica configuration adjustments within the agreed application scope; Acumatica workflow and customisation support within the implemented framework; data correction support; Acumatica release advisory; and Acumatica user access management where contracted. *(Ref: AMS-SCP-007)*

302. Standard AMS support is provided during business hours: 08:00–17:00 SAST, Monday to Friday, excluding South African public holidays. Business-hours support is the default for all AMS agreements. Extended hours support (weekday evenings, Saturday, Sunday) and 24/7 support require a separate commercial agreement and are not included in the standard AMS agreement. *(Ref: AMS-HRS-001)*

303. AMS support is delivered remotely unless on-site support is explicitly contracted. On-site support incurs a separate on-site day rate plus travel expenses as applicable. Remote-first support is the APPSolve standard for all AMS engagements. *(Ref: AMS-HRS-002)*

304. There is no default monthly support hours allocation. The support model and allocation are governed by the specific AMS agreement. APPSolve offers both retainer-based engagements (fixed monthly fee for a defined support scope) and allocated-hour models (monthly hour bucket at a contracted rate). The model, allocation, and overage terms are defined in each AMS agreement. Where an allocated-hour model applies, hours not used in a given month do not roll over to the following month. *(Ref: AMS-HRS-003)*

305. Hours consumed against the monthly allocation are tracked and reported. APPSolve provides a monthly support activity report showing: incidents resolved; service requests completed; hours consumed; hours remaining; change requests raised; and open items carried to the following month. *(Ref: AMS-HRS-004)*

306. Where the monthly hours allocation is exhausted before month-end, APPSolve notifies the client immediately. Additional hours may be approved by the client at the applicable AMS hourly rate. APPSolve does not continue work beyond the monthly allocation without written client approval. *(Ref: AMS-HRS-005)*

307. Public holiday support: APPSolve does not provide AMS support on South African public holidays under the standard business hours agreement. Where the client requires support on public holidays, this is arranged separately and billed at the applicable out-of-hours rate. *(Ref: AMS-HRS-006)*

308. All AMS support requests must be logged via APPSolve's designated support channel — either the APPSolve support portal, a designated support email address, or the agreed ticketing mechanism specified in the AMS agreement. Requests made directly to individual consultants via WhatsApp, personal email, or phone are acknowledged but must be formally logged to be covered under the AMS agreement. *(Ref: AMS-CHN-001)*

309. Telephone support is available for P1 (Critical) incidents only — the client may call the APPSolve AMS hotline to report a P1 after logging the ticket. For P2, P3, and P4 requests, ticket-first is the required process; telephone follow-up is at APPSolve's discretion. *(Ref: AMS-CHN-002)*

310. A designated AMS contact at APPSolve (the AMS Account Manager or AMS Team Lead) is the client's primary escalation point for service delivery concerns, SLA disputes, and change request approvals. The AMS contact is named in the AMS agreement. Changes to the AMS contact are communicated to the client in writing. *(Ref: AMS-CHN-003)*

311. The client designates a primary AMS contact (typically the internal IT or ERP team lead) who is authorised to log support requests, approve change requests, and receive monthly reports. APPSolve only takes direction from the designated client AMS contact. Requests from other client employees may be acknowledged but require authorisation from the designated contact before work commences. *(Ref: AMS-CHN-004)*

312. An incident is an unplanned interruption or degradation of a supported application. Incidents are distinguished from service requests (planned configuration changes) and change requests (enhancements or new scope). The incident classification determines the priority level and SLA response target. *(Ref: AMS-INC-001)*

313. Incidents are classified by the client at the time of logging. APPSolve may reclassify an incident based on its assessment of business impact. Where APPSolve downgrades an incident from P1 to P2, the client is notified with the reason. Where the client disputes the reclassification, the AMS Account Manager resolves the classification within four (4) business hours. *(Ref: AMS-INC-002)*

314. Incident ownership: APPSolve owns the investigation and resolution of application configuration and integration defects. Incidents caused by client data entry errors, client business process errors, client IT infrastructure failures (network, hardware, browser), or Oracle SaaS platform outages are not APPSolve defects. APPSolve assists in the diagnosis of such incidents but the resolution responsibility lies with the relevant party. *(Ref: AMS-INC-003)*

315. Incident resolution: APPSolve provides resolution for application configuration incidents. For complex incidents requiring Oracle Support involvement (Oracle bug, Oracle platform issue, Oracle patch required), resolution timelines depend on Oracle's support processes and are outside APPSolve's control. APPSolve manages Oracle SR progress on the client's behalf and provides weekly status updates for open Oracle SRs. *(Ref: AMS-INC-005)*

316. A service request is a planned, pre-agreed configuration change or task that does not constitute a defect and does not represent new scope. Service requests are fulfilled within the monthly hours allocation. Examples: adding a new user and assigning roles; updating an existing approval limit in a workflow; adding a new GL account to an existing value set; updating a document sequence; configuring a new supplier payment term. *(Ref: AMS-SRQ-001)*

317. Service requests are prioritised within the monthly allocation based on business need, as agreed between the client's designated AMS contact and APPSolve's AMS Team Lead. APPSolve does not guarantee fulfilment of all service requests within a given month if the volume exceeds the monthly allocation. *(Ref: AMS-SRQ-002)*

318. Service requests that are assessed as requiring design work, testing, or stakeholder approval before implementation — even if small — are raised as change requests rather than service requests. The boundary between SR and CR is the need for a documented design and formal approval. *(Ref: AMS-SRQ-003)*

319. Standard service request catalogue: APPSolve maintains a list of standard service requests with pre-defined effort estimates. Requests on the standard catalogue are fulfilled within the allocated hours without further negotiation. Non-catalogue requests are assessed per complexity and agreed with the client before work commences. *(Ref: AMS-SRQ-004)*

320. Enhancements — adding new functionality, new configuration, new modules, new integrations, or new reports beyond the contracted application scope — are excluded from AMS. Enhancements are delivered as project work under a separate project SOW. *(Ref: AMS-ENH-001)*

321. Where the client requests an enhancement during an AMS support interaction, APPSolve identifies it as an enhancement, logs it, and advises the client that it requires a separate project engagement. APPSolve does not absorb enhancement work into the AMS hours without explicit commercial agreement. *(Ref: AMS-ENH-002)*

322. Enhancement identification: APPSolve's obligation is to tell the client when a request crosses the enhancement boundary. APPSolve is not responsible for the client's decision about whether to proceed with the enhancement or when to schedule it. *(Ref: AMS-ENH-003)*

323. Where a client-requested configuration change is ambiguous (could be interpreted as support or enhancement), APPSolve escalates to the AMS Account Manager and the client's designated AMS contact for classification before work commences. Agreed classifications are logged in the monthly report. *(Ref: AMS-ENH-004)*

324. A change request (CR) is a formally scoped and approved work item that constitutes new or changed scope beyond the standard service request catalogue. The standard CR threshold is 2 hours: changes estimated at more than 2 hours of effort require a formal written CR, an effort estimate, and written client approval before work commences. APPSolve may, at its discretion, absorb changes estimated below 2 hours into the monthly support hours without raising a formal CR. No entitlement to this discretionary treatment is created by previous practice — each case is assessed independently. The CR threshold defined in a specific AMS agreement takes precedence over this standard. *(Ref: AMS-CR-001)*

325. The change request process: (1) Client submits change request description via the support channel; (2) APPSolve assesses and produces a written effort estimate within five (5) business days; (3) Client approves the estimate in writing; (4) APPSolve schedules and delivers the change; (5) Client signs off delivery. No change request work commences without written client approval of the estimate. *(Ref: AMS-CR-002)*

326. Change requests are not subject to the incident SLA. CR delivery timelines are agreed at the time of CR approval based on complexity, resource availability, and the client's priority. APPSolve provides a delivery date at the time of CR approval. *(Ref: AMS-CR-003)*

327. Change requests that introduce risk to the live production system (for example, security role changes affecting multiple users, workflow restructuring, GL period-end configuration changes) are assessed by APPSolve for risk before implementation and require a testing confirmation from the client before production deployment. *(Ref: AMS-CR-004)*

328. A defect is a system behaviour that does not conform to the agreed configuration design documented during implementation. Defects in the configured system discovered post-go-live are covered under AMS incident management and are resolved within the monthly hours allocation (or as a priority incident depending on severity) at no additional charge. *(Ref: AMS-DEF-001)*

329. Defect vs enhancement vs configuration drift: APPSolve distinguishes between three types of post-go-live issues: - **Defect:** System does not behave per the agreed design — APPSolve resolves, no additional charge - **Enhancement:** Client requests new functionality not in the original design — separately priced project work - **Configuration drift:** Client or another party has changed the configuration since go-live, causing unexpected behaviour — APPSolve investigates; resolution effort may be billed as a service request. *(Ref: AMS-DEF-002)*

330. Defects introduced by Oracle's quarterly platform updates are managed as follows: APPSolve monitors Oracle's quarterly release notes for the client's supported applications; where a release update introduces a defect in the client's configuration, APPSolve resolves the defect within the standard SLA; the root cause (Oracle release) is documented in the monthly report. *(Ref: AMS-DEF-003)*

331. Configuration changes made by the client's internal team without APPSolve involvement may invalidate existing configuration and cause system issues. APPSolve is not responsible for defects caused by client-initiated configuration changes. Restoring the system from a client-caused configuration error is treated as a service request and billed against the monthly allocation. *(Ref: AMS-DEF-004)*

332. SLA clock starts when the ticket is logged in APPSolve's support system during business hours. Tickets logged outside business hours (evenings, weekends, public holidays) start the SLA clock at 08:00 SAST on the next business day, unless a 24/7 SLA has been contracted. *(Ref: AMS-SLA-002)*

333. SLA clock is paused in the following circumstances: - APPSolve is waiting for information from the client that is required to proceed with investigation or resolution - The incident is pending Oracle Support response (Oracle SR lodged; resolution outside APPSolve's control) - The client has not approved a required change to proceed with resolution - A scheduled maintenance window is in progress (agreed in advance). *(Ref: AMS-SLA-003)*

334. SLA reporting: APPSolve reports SLA performance in the monthly support report. The report shows: total tickets logged by priority; SLA compliance rate per priority; SLA breaches with root cause; Oracle SR status for open items; change request status. *(Ref: AMS-SLA-004)*

335. This SLA Assumptions Overlay applies to APPSolve AMS engagements where Oracle EBS (R11, R12.1, or R12.2) is the supported application, and where the client specifies service level commitments that differ from APPSolve's standard AMS SLA defined in AMS-SLA-001 and AMS-PRI-001 of the base AMS pack. This overlay is assembled alongside the base AMS pack; it does not replace the base pack in its entirety. *(Ref: EBS-SLA-001)*

336. For EBS AMS engagements using this overlay, the standard AMS response times in AMS-SLA-001 (P1=1 hour, P2=4 business hours, P3=1 business day, P4=3 business days) are superseded by the five-priority SLA tier defined in EBS-SLA-010 through EBS-SLA-014 of this overlay. The base AMS pack four-priority model does not apply where this overlay is assembled. *(Ref: EBS-SLA-002)*

337. SLA commitments in this overlay — including response times, resolution times, and 24/7 coverage obligations — apply only where they are explicitly included in the signed AMS agreement. No SLA commitment in this overlay is automatically included unless stated in the commercial agreement. The overlay defines the available SLA positions; the specific targets agreed with a given client are confirmed in the AMS SOW or AMS agreement schedule. *(Ref: EBS-SLA-003)*

338. EBS AMS engagements using this overlay adopt a five-priority severity classification (P1 through P5). All five tiers are active from the commencement date of the AMS agreement. The priority of a ticket is assigned by the client at the time of logging and may be reclassified by APPSolve per EBS-SLA-008. *(Ref: EBS-SLA-004)*

339. P1 Critical: the EBS application is completely unavailable to all users; payroll processing is blocked and a pay run is imminent or in progress; Oracle Financial period-end processing is blocked and a statutory reporting deadline is at risk; all OIC or BeBanking integrations have failed and payment runs, bank reconciliations, or inter-company transactions cannot proceed; or data integrity has been compromised and financial records are at risk. P1 requires immediate action and triggers the 24/7 on-call escalation regardless of the time of day or day of week. *(Ref: EBS-SLA-005)*

340. P2 Major: a significant function or module is impaired affecting a material user population; a critical business process (accounts payable run, payroll pre-close, inter-company reconciliation, bank payment authorisation) cannot be completed; a major OIC or BeBanking integration is failing but a manual workaround exists; or a single critical user (CFO, Payroll Manager, Finance Director) is completely locked out of a mission-critical function. P2 requires same-day resolution and, where it occurs outside business hours with 24/7 contracted, triggers the after-hours response procedure. *(Ref: EBS-SLA-006)*

341. P3 Normal: a non-critical function or a non-mission-critical process is impaired; a subset of users is affected with a practical workaround available; a report is producing incorrect results for non-period-end use; a workflow is not routing correctly for lower-value transactions; or a service request is required for a time-sensitive but non-emergency configuration change. P3 is resolved within business hours at the contracted response and resolution targets. *(Ref: EBS-SLA-007)*

342. P4 Minor: a low-impact cosmetic issue; a non-urgent configuration question that does not block a business process; a minor report formatting issue; an individual user access query; a non-urgent service request for which the client has no immediate deadline. P4 is planned and delivered within the standard resolution window. *(Ref: EBS-SLA-008)*

343. P5 Minimal: a general how-to question that does not require configuration change; a documentation request; an enquiry about EBS functionality; a request for explanation of an existing report result; a non-urgent product advisory question. P5 is addressed in the normal course of monthly support operations and does not carry an SLA response obligation beyond the P5 response target. *(Ref: EBS-SLA-009)*

344. APPSolve may reclassify a ticket from the client-assigned priority where the actual business impact assessed during initial investigation materially differs from the assigned priority. Reclassification in either direction (upgrade or downgrade) is communicated to the client's designated AMS contact at the time of reclassification with the reason recorded in the ticket. Where the client disputes a downgrade, the AMS Account Manager or SDM resolves the classification dispute within two (2) business hours. The SLA clock is not reset on reclassification; it runs from original ticket logging. *(Ref: EBS-SLA-010)*

345. Response time is the elapsed time from ticket logging to APPSolve's first substantive response — an acknowledgement of receipt, a request for information, an initial diagnosis, or the assignment of an engineer to the incident. Response time is not resolution time. The response time targets for EBS AMS engagements using this overlay are:

| Priority | Response Target |
|---|---|
| P1 — Critical | 15 minutes from ticket logging (24 hours a day, 7 days a week) — client-configurable; specific target confirmed in AMS agreement schedule |
| P2 — Major | 1 hour (within contracted support hours; or 24/7 where contracted) |
| P3 — Normal | 4 business hours |
| P4 — Minor | 8 business hours |
| P5 — Minimal | 3 business days |

*(Ref: EBS-SLA-011)*

346. The P1 15-minute response target applies regardless of the day, time, or public holiday status. Where P1 24/7 coverage is contracted, the APPSolve on-call resource must acknowledge the P1 incident within 15 minutes of the ticket being logged or the automated alert being triggered. Where 24/7 coverage is not contracted, APPSolve acknowledges P1 tickets logged outside business hours at the start of the next business day; the 15-minute target applies only within contracted support hours unless 24/7 is in the agreement. *(Ref: EBS-SLA-012)*

347. The P2 1-hour response target applies within contracted business hours. Where P2 24/7 response is included in the AMS agreement, the 1-hour target applies at all hours. P2 tickets logged outside business hours under a standard (business-hours) agreement start the SLA clock at 08:00 SAST on the next business day. *(Ref: EBS-SLA-013)*

348. Response time measurement: APPSolve's support system timestamps the first outbound communication from an APPSolve resource against the ticket. The timestamp of the client's ticket creation is the SLA start time. Where a ticket is created by automated monitoring (where monitoring is contracted), the SLA start time is the automated alert timestamp. *(Ref: EBS-SLA-014)*

349. SLA response performance is reported in the monthly support report per EBS-SLA-050. Where a response SLA is missed, the reason is documented in the report. Persistent P1 or P2 response SLA misses (two or more in any rolling 3-month period) trigger a service review meeting within five (5) business days. *(Ref: EBS-SLA-015)*

350. Resolution time commitments define the target elapsed time from ticket logging to confirmed resolution — meaning the application function is restored to the agreed operating state and the client has confirmed, or APPSolve has demonstrated, that the incident has been fully resolved. Resolution time is measured from initial ticket logging and includes any SLA clock pause periods per EBS-SLA-030 through EBS-SLA-034. *(Ref: EBS-SLA-016)*

351. Where resolution time SLAs are contracted, the resolution time targets for EBS AMS engagements are:

| Priority | Resolution Target |
|---|---|
| P1 — Critical | 2 hours (restore to operational status) |
| P2 — Major | 4 hours |
| P3 — Normal | 8 business hours |
| P4 — Minor | 16 business hours |
| P5 — Minimal | 5 business days |

*(Ref: EBS-SLA-017)*

352. Resolution time commitments apply only where explicitly included in the AMS agreement. Where the AMS agreement includes response time SLAs but not resolution time SLAs, APPSolve commits to response time only. Resolution effort is always prioritised in order of severity, but without contractual resolution time commitments, no SLA breach is recorded against resolution timing alone. *(Ref: EBS-SLA-018)*

353. P1 resolution is defined as: the application function that triggered the P1 is restored to operational status sufficient to unblock the affected business process. P1 resolution does not require root cause elimination — a validated workaround that restores operations constitutes resolution for P1 SLA purposes. Full root cause correction may be delivered in a subsequent P3 or CR under the agreed root cause timeline. *(Ref: EBS-SLA-019)*

354. Resolution extension: where a P1 or P2 incident cannot be resolved within the contracted resolution window — due to Oracle Support escalation, infrastructure root cause, or a factor outside APPSolve's direct control — APPSolve notifies the client's designated AMS contact and SDM (where applicable) at the expiry of the resolution window with an updated resolution estimate and the reason for the extension. Extension notification does not extinguish the SLA breach; it is recorded and reported. *(Ref: EBS-SLA-020)*

355. 24/7 P1 coverage is available as a contracted AMS add-on. Where 24/7 P1 coverage is included in the AMS agreement, APPSolve maintains an on-call resource for P1 EBS incidents at all hours, including evenings, weekends, and South African public holidays. 24/7 coverage does not apply to P2, P3, P4, or P5 under the standard 24/7 P1 model. *(Ref: EBS-SLA-021)*

356. Where 24/7 P1 and P2 coverage is contracted, APPSolve provides an on-call resource available for both P1 and P2 incidents at all hours. The P1 15-minute response and P2 1-hour response targets apply at all hours. Additional commercial terms (on-call premium, after-hours rate) are defined in the AMS agreement. *(Ref: EBS-SLA-022)*

357. The 24/7 on-call resource is an APPSolve AMS consultant with direct knowledge of the client's EBS configuration. The specific on-call roster is maintained by APPSolve's AMS Account Manager. The client receives the after-hours emergency contact number for direct on-call access. The emergency contact number is updated whenever the on-call roster changes. *(Ref: EBS-SLA-023)*

358. After-hours P1 activation procedure: (1) Client logs a P1 ticket in the support system AND (2) calls the emergency contact number. Logging alone without the call does not guarantee 15-minute activation outside business hours. Where automated monitoring is contracted, a P1 monitoring alert activates the on-call resource without client call. *(Ref: EBS-SLA-024)*

359. After-hours commercial model: APPSolve's confirmed 24/7 on-call commercial structure is a fixed monthly premium. After-hours on-call availability is included in the contracted 24/7 monthly fee. No separate per-callout charge applies — all after-hours callout work is covered within the fixed monthly premium. Where a specific engagement requires a different commercial structure, this must be agreed in writing in the AMS agreement as an exception to the fixed premium standard. *(Ref: EBS-SLA-025)*

360. 24/7 coverage for planned payroll runs: where a client payroll run is scheduled outside standard business hours (for example, overnight batch payroll processing), and the client has contracted 24/7 P1 coverage, APPSolve's on-call resource is available to respond to EBS or OIC failures that block the payroll batch. The client notifies APPSolve of payroll run schedules at the start of each month. *(Ref: EBS-SLA-026)*

361. 24/7 coverage exclusions: 24/7 coverage under this overlay covers P1 (and P2 if contracted) EBS application incidents only. It does not cover: Acumatica or BeBanking incidents (separate AMS agreements apply); client IT infrastructure incidents (client's IT team responsibility); Oracle SaaS platform incidents (Oracle responsibility); or enhancement or project work. *(Ref: EBS-SLA-027)*

362. After-hours escalation tree: for P1 incidents outside business hours, APPSolve follows the escalation tree documented in the AMS agreement. The standard escalation sequence is: (Level 1) on-call AMS consultant; (Level 2) AMS Account Manager or SDM (if applicable); (Level 3) APPSolve Oracle BU Lead or Technical Lead; (Level 4) APPSolve Managing Director. Each level is engaged if the previous level does not acknowledge within 30 minutes. *(Ref: EBS-SLA-028)*

363. Client escalation mirror: the client designates a corresponding after-hours escalation tree — including a named 24/7 contact for P1 declarations (typically the IT Manager or ERP Manager). Without a client 24/7 contact, APPSolve cannot engage the client for P1 resolution steps (access provision, environment decisions, test authorisation) outside business hours. The absence of a client 24/7 contact suspends the SLA clock for time spent awaiting client engagement per EBS-SLA-031. *(Ref: EBS-SLA-029)*

364. SLA clock start: the SLA clock starts at the timestamp of ticket creation in APPSolve's support system — either client-logged or auto-generated by monitoring (where contracted). For P1 incidents with 24/7 coverage, the clock runs continuously. For P2, P3, P4, and P5 under business-hours SLAs, the clock runs only during contracted support hours. *(Ref: EBS-SLA-030)*

365. SLA clock pause — client dependency: the SLA clock is paused when APPSolve is actively waiting for client action required to proceed with investigation or resolution. Pause conditions: client has not provided required information requested in writing; client has not granted requested system or environment access; client has not approved a required configuration change; client test environment is unavailable despite being required for resolution. The pause commences when APPSolve documents the dependency in the ticket and notifies the client. The clock resumes when the client fulfils the dependency. *(Ref: EBS-SLA-031)*

366. SLA clock pause — Oracle SR: the SLA clock is paused for the period during which an Oracle Support SR is the blocking dependency. Pause commences when APPSolve lodges the Oracle SR and notifies the client. The clock resumes when Oracle provides the required patch, fix, or resolution and APPSolve commences implementation. Oracle SR pause time is documented in the monthly report. *(Ref: EBS-SLA-032)*

367. SLA clock pause — maintenance window: the SLA clock is paused during agreed maintenance windows per EBS-SLA-040 through EBS-SLA-043. *(Ref: EBS-SLA-033)*

368. SLA clock pause — force majeure: the SLA clock is paused during force majeure events that prevent APPSolve from providing service. Force majeure events are communicated to the client in writing as soon as practicable. The pause does not apply to events that affect only the client's environment (network outage, power failure, hardware failure) as these are the client's IT team's responsibility. *(Ref: EBS-SLA-034)*

369. A Major Incident is a P1 incident that has not been resolved within the P1 resolution window, or a P1 incident affecting all users across all client sites simultaneously, or a P1 incident that has a confirmed regulatory, financial reporting, or payroll processing deadline impact. All Major Incidents trigger the Major Incident Management (MIM) process. *(Ref: EBS-SLA-035)*

370. MIM war room: APPSolve convenes a conference bridge or virtual war room within 30 minutes of P1 declaration. The client is invited immediately. The bridge remains open until the P1 is resolved. Attendance: APPSolve on-call consultant, APPSolve AMS Account Manager or SDM, client's designated AMS contact, and any technical specialists required. *(Ref: EBS-SLA-036)*

371. P1 status updates: APPSolve provides status updates to the client's designated AMS contact at 30-minute intervals for the duration of an active P1 incident. Updates include: current status, actions taken, next steps, estimated resolution time (where determinable), and whether Oracle Support has been engaged. *(Ref: EBS-SLA-037)*

372. Executive communication: for P1 incidents exceeding 2 hours without resolution (or immediately if payroll is blocked on a pay run date), APPSolve's AMS Account Manager or Oracle BU Lead notifies the client's CIO, CFO, or designated executive contact. Executive communication is in writing (email) with a verbal brief. Executive communication is maintained every 2 hours thereafter until resolution. *(Ref: EBS-SLA-038)*

373. Post-P1 debrief: within 5 business days of P1 resolution, APPSolve and the client conduct a post-incident review call (30 minutes) to review the incident timeline, validate the root cause, and agree on prevention measures. This debrief is separate from and precedes the formal RCA document. *(Ref: EBS-SLA-039)*

374. Standard maintenance window: the default EBS AMS maintenance window is Sunday 00:00–06:00 SAST. During this window, APPSolve may apply configuration changes, EBS patch applications (where DBA scope is contracted), or integration maintenance without SLA obligation. The maintenance window is agreed in the AMS agreement and may be adjusted by mutual written agreement. *(Ref: EBS-SLA-040)*

375. Advance notice for maintenance: APPSolve provides the client with a minimum of five (5) business days' advance notice for planned maintenance activities that require system downtime or application restart. The notice includes: maintenance scope, expected duration, expected impact on users, and the date/time of the maintenance window. *(Ref: EBS-SLA-041)*

376. Emergency maintenance: where a critical security patch, Oracle-required emergency configuration change, or P1 resolution requires immediate system changes outside the standard maintenance window, APPSolve notifies the client's designated AMS contact as soon as practicable before commencing. Emergency maintenance notification is by telephone followed immediately by written confirmation. *(Ref: EBS-SLA-042)*

377. Client-requested downtime: where the client requires planned downtime outside the standard maintenance window (for example, for an internal audit, a data migration, or a DR test), the client provides APPSolve with a minimum of 10 business days' advance notice. SLA is suspended during client-requested downtime where agreed in advance in writing. *(Ref: EBS-SLA-043)*

378. RCA for P1 incidents: APPSolve delivers a written RCA report to the client within five (5) business days of P1 resolution. The RCA report covers: incident timeline (detection to resolution); root cause analysis; contributing factors; immediate corrective actions taken; preventive measures recommended and agreed; and follow-on actions with owners and due dates. *(Ref: EBS-SLA-044)*

379. RCA for P2 incidents: APPSolve delivers a written RCA report for P2 incidents on request from the client. The report is delivered within ten (10) business days of the request. Not all P2 incidents require a formal RCA — the client designates which P2 incidents warrant a formal RCA at the time of ticket closure. *(Ref: EBS-SLA-045)*

380. RCA format: the RCA report uses the 5-Why or fishbone methodology. It documents the technical root cause, any contributing process or human factors, and the recommended preventive action. Where Oracle is the root cause (Oracle bug, Oracle infrastructure failure), the RCA documents the Oracle SR reference, the Oracle diagnosis, and the workaround applied pending Oracle's permanent fix. *(Ref: EBS-SLA-046)*

381. RCA follow-on actions: where an RCA identifies a configuration change, process change, or monitoring requirement as a preventive action, APPSolve provides an effort estimate for implementing the recommendation. The client decides whether to proceed. Preventive actions are tracked in the monthly report until closed. *(Ref: EBS-SLA-047)*

382. Service credits (negotiate per engagement): service credits are available as a negotiated commercial option in EBS AMS agreements and are not a standard inclusion. Where service credits are negotiated and included in the AMS agreement, and APPSolve fails to meet the contracted P1 response or resolution SLA in a given month, the client is entitled to a service credit calculated as a percentage of the applicable monthly AMS fee. The credit percentage, monthly cap, and SLA breach trigger conditions are defined through negotiation and confirmed in the AMS agreement. Service credits are the client's exclusive remedy for SLA failures and are applied to the following month's invoice. *(Ref: EBS-SLA-048)*

383. Service credit exclusions: service credits do not apply where an SLA miss is attributable to: client dependency pause per EBS-SLA-031; Oracle SR blocking per EBS-SLA-032; force majeure per EBS-SLA-034; a client-initiated change that caused the incident; or where the client did not activate the P1 emergency call procedure per EBS-SLA-024. Credits are applied only for SLA breaches within APPSolve's direct control. *(Ref: EBS-SLA-049)*

384. Service credit claim process: service credits are not applied automatically. The client submits a credit claim in writing (email to the AMS Account Manager or SDM) within 10 business days of the SLA breach. APPSolve reviews the claim against the support system data within 5 business days and confirms the credit or provides the reason for exclusion. Undisputed credits are applied to the next invoice. *(Ref: EBS-SLA-050)*

385. Response and resolution SLA commitments are contingent on the client fulfilling its obligations under the AMS agreement. Key client dependencies that, if unmet, suspend SLA obligations: (a) designated AMS contact available during business hours; (b) P1 24/7 contact available for after-hours P1 incidents where 24/7 is contracted; (c) system access provisioned for the APPSolve AMS team prior to engagement commencement; (d) test environment available for APPSolve testing where required for resolution; (e) client CSI access provided for Oracle SR management. *(Ref: EBS-SLA-051)*

386. Change approval timing: where an incident or service request resolution requires the client to approve a configuration change before APPSolve can implement it, the SLA clock is paused from the time APPSolve submits the change approval request to the time the client approves. For P1 and P2 incidents, APPSolve requires a response to configuration change approval requests within 30 minutes during P1 and within 2 hours during P2. Delay in approval beyond these times is documented as a client dependency pause. *(Ref: EBS-SLA-052)*

387. Monthly SLA report (EBS AMS): in addition to the standard AMS monthly report (AMS-REP-001), EBS AMS engagements using this overlay include the following SLA-specific content in the monthly report: (a) ticket count by priority tier (P1–P5); (b) response SLA compliance rate per priority; (c) resolution SLA compliance rate per priority (where resolution SLAs are contracted); (d) SLA pauses: total pause minutes per priority per ticket, with reason; (e) P1 incident log: each P1 with date, duration, root cause category, and resolution; (f) service credit position: credits earned and applied (where applicable). *(Ref: EBS-SLA-053)*

388. For EBS AMS engagements using this overlay, the base AMS pack assumption AMS-SLA-005 ("Named consultant excluded from standard AMS") is superseded. A Dedicated Resource Model engagement by definition includes named consultants with contracted minimum monthly hour commitments. The roles, minimum hours, and governance obligations for each named resource are defined in EBS-DRM-010 through EBS-DRM-029 of this overlay. *(Ref: EBS-DRM-001)*

389. This overlay assumes that the DRM contract structure specifies, at minimum: the role title for each named resource; the minimum monthly hours committed per role; the support hours window (business hours, 24/7 P1, or extended); and the commercial rate or blended monthly fee for the named resource team. Where any of these elements is absent from the contract, the standard base AMS pooled model applies to that element. *(Ref: EBS-DRM-002)*

390. Named resources under the DRM are APPSolve employees or contractors permanently engaged by APPSolve. The DRM does not constitute an employment relationship, labour broking arrangement, or secondment between APPSolve's resources and the client. APPSolve retains full employment, management, and HR authority over all named resources. *(Ref: EBS-DRM-003)*

391. The Service Delivery Manager (SDM) is the single point of accountability for the EBS AMS engagement. The SDM owns client relationship management, SLA performance, team coordination, escalation handling, and monthly and quarterly governance reporting. The SDM is the client's first point of escalation above the support consultant tier. *(Ref: EBS-DRM-004)*

392. SDM minimum monthly commitment: the SDM commits a minimum of 40 hours per month to the client under the DRM. These hours cover: weekly operational call preparation and facilitation; monthly SLA review preparation and facilitation; incident management oversight; resource coordination; monthly report compilation and delivery; and client stakeholder communication. Additional SDM hours are engaged at the contracted SDM hourly rate. The 40-hour figure is the ARM IT045 reference architecture; actual SDM minimum hours for each engagement are confirmed in the AMS agreement schedule. *(Ref: EBS-DRM-005)*

393. SDM availability: the SDM is available to the client during business hours (08:00–17:00 SAST, Monday–Friday, excluding South African public holidays). For P1 incidents where 24/7 coverage is contracted, the SDM is on the after-hours escalation tree per EBS-SLA-028 but is not necessarily the primary on-call responder — the SDM's after-hours role is coordination and executive communication where the on-call consultant cannot resolve the incident within 1 hour. *(Ref: EBS-DRM-006)*

394. SDM continuity: APPSolve does not change the named SDM without providing the client with a minimum of 30 days' advance written notice, except where the SDM is absent due to unplanned leave or termination. In these circumstances, APPSolve designates an Acting SDM within 2 business days and provides formal nomination within 10 business days. The acting appointment process is governed by EBS-DRM-040 through EBS-DRM-044. *(Ref: EBS-DRM-007)*

395. SDM onboarding: the incoming SDM completes a 30-day knowledge transfer with the outgoing SDM (where the outgoing SDM is available) before assuming full client-facing responsibility. The KT programme is governed by EBS-DRM-050 through EBS-DRM-055. Where an unplanned SDM change occurs and the 30-day KT is not possible, the Acting SDM assumes the role with the available briefing documentation and the KT obligation is fulfilled on a best-efforts basis over the first 30 days of the acting period. *(Ref: EBS-DRM-008)*

396. SDM skills requirement: the named SDM holds a minimum of 5 years' Oracle AMS or Oracle EBS project experience, with demonstrated client-facing delivery management experience. SDM selection is APPSolve's responsibility. Where the client requests a replacement SDM on grounds of service quality, APPSolve investigates the request within 5 business days and provides a remediation plan or a replacement nomination within 20 business days. *(Ref: EBS-DRM-009)*

397. The Named DBA / OCI Specialist is the dedicated database and infrastructure expert for the EBS AMS engagement. The DBA role covers: Oracle database administration for EBS (R11, R12.1, or R12.2); performance tuning; patch application (where patch management is in AMS scope); backup monitoring (advisory, not DR hosting); OCI infrastructure coordination (where EBS runs on OCI); and database-related incident resolution. *(Ref: EBS-DRM-010)*

398. DBA scope boundary: the DBA role is scoped to Oracle Database (versions in use for the EBS environment — typically 11g, 12c, 19c, or 21c) and OCI services that directly support the EBS workload (Compute, Block Storage, Networking as they relate to EBS database and application tiers). The DBA does not assume responsibility for: the client's OCI tenancy governance (BU-OCI-007 permanent constraint applies); cloud cost management; non-EBS workloads on OCI; or DR site operations where separately contracted. *(Ref: EBS-DRM-011)*

399. DBA minimum monthly hours: the DBA / OCI Specialist commits a minimum of 160 hours per month to the client under the DRM. These hours cover BAU DBA operations, proactive monitoring, incident resolution, and scheduled maintenance. Hours in excess of the minimum are engaged at the contracted DBA hourly rate. The 160-hour figure is the ARM IT045 reference architecture; actual minimum hours are defined per engagement in the AMS agreement schedule. *(Ref: EBS-DRM-012)*

400. EBS infrastructure scope clarification: Unlike Oracle Fusion SaaS, Oracle EBS is not delivered on Oracle's managed SaaS infrastructure. The client operates the EBS application tier (on-premises or on OCI). APPSolve's DBA / OCI Specialist has access to the database and application tier to perform database administration, patching, and performance management activities within the contracted DBA scope. The client retains ownership and administrator access to the OCI tenancy or on-premises environment. *(Ref: EBS-DRM-013)*

401. EBS patch management: where EBS patching is included in the DBA scope, APPSolve's DBA Specialist applies Oracle-recommended patches (one-off patches, PSUs, RUs, and interim patches) in accordance with the agreed maintenance window schedule (EBS-SLA-040 through EBS-SLA-043). Patch recommendations are reviewed and approved by the client before application. APPSolve does not apply patches that the client has explicitly declined. *(Ref: EBS-DRM-014)*

402. The DRM includes named Functional Lead resources for each EBS module group in scope. The standard EBS AMS DRM functional lead structure is: (a) HCM Functional Lead — responsible for Oracle EBS HR, Payroll, and Self-Service; (b) Finance Functional Lead — responsible for Oracle EBS General Ledger, Accounts Payable, Accounts Receivable, Fixed Assets, Cash Management, and iProcurement. Additional module leads (Supply Chain, Projects) are separately contracted. *(Ref: EBS-DRM-015)*

403. HCM Functional Lead minimum monthly hours: the HCM Functional Lead commits a minimum of 240 hours per month to the client under the DRM. These hours cover: HCM module incident resolution; functional configuration changes; user support; payroll processing support; reporting; integration support (EBS Payroll–PaySpace where contracted); and HCM process documentation maintenance. The 240-hour figure is the ARM IT045 reference architecture; actual minimum hours are defined per engagement in the AMS agreement schedule. *(Ref: EBS-DRM-016)*

404. Finance Functional Lead minimum monthly hours: the Finance Functional Lead commits a minimum of 160 hours per month to the client under the DRM. These hours cover: Finance module incident resolution; period-end support; month-end reconciliation support; functional configuration changes; chart of accounts maintenance; reporting; and bank interface management (where contracted). The 160-hour figure is the ARM IT045 reference architecture; actual minimum hours are defined per engagement in the AMS agreement schedule. *(Ref: EBS-DRM-017)*

405. Functional Lead scope boundary: Functional Leads are responsible for Oracle EBS functional configuration and support. They do not perform: custom development (RICE/CEMLI — separately scoped under CRs); report development (separately scoped); data migration (separately scoped); or upgrade activities (separately scoped). Where a functional issue requires technical investigation or custom code, the Functional Lead engages the Technical Specialist per EBS-DRM-020. *(Ref: EBS-DRM-018)*

406. Functional Lead module boundary: the HCM Functional Lead's scope is limited to EBS modules contracted in the AMS agreement. Where the client adds an EBS module after the AMS agreement commences, APPSolve and the client agree the additional module inclusion terms via Change Request before the Functional Lead assumes support responsibility for the new module. *(Ref: EBS-DRM-019)*

407. The Named Technical / OIC Specialist covers Oracle Integration Cloud (OIC) integration support, EBS technical layer support (Forms, Workflow, APIs, concurrent programs, customisation support advisory), and BeBanking integration support where BeBanking is within the AMS agreement scope. The Technical Specialist is the DRM resource for all integration-related incidents and service requests. *(Ref: EBS-DRM-020)*

408. Technical / OIC Specialist minimum monthly hours: the Technical / OIC Specialist commits a minimum of 80 hours per month to the client under the DRM. These hours cover: OIC integration monitoring and incident resolution; technical advisory for customisation issues; EBS Workflow issue resolution; API and concurrent program troubleshooting; and BeBanking integration support (where contracted). The 80-hour figure is the ARM IT045 reference architecture; actual minimum hours are defined per engagement in the AMS agreement schedule. *(Ref: EBS-DRM-021)*

409. OIC scope boundary: the Technical / OIC Specialist manages OIC integrations within the AMS agreement scope (those built and handed over as part of the implementation). New OIC integrations or material enhancements to existing OIC integrations are scoped and delivered as project work separately. The Technical Specialist provides post-implementation support, not new development, within the AMS hours commitment. *(Ref: EBS-DRM-022)*

410. BeBanking integration rule: where BeBanking is within the AMS agreement scope, the Technical Specialist supports the EBS-to-BeBanking and BeBanking-to-OIC integration at the Oracle EBS and OIC layers. BeBanking core banking platform issues are escalated to BeBanking's own support team. APPSolve does not assume responsibility for BeBanking application-layer incidents; these are the client's responsibility to log with BeBanking directly. *(Ref: EBS-DRM-023)*

411. Non-pooled allocation: under the DRM, each named resource's contracted minimum hours are ring-fenced exclusively for the client. These hours are not shared across APPSolve's AMS client pool. Hours not consumed within the month are not re-allocated to other APPSolve clients. The commercial consequence of unconsumed minimum hours is governed by EBS-DRM-030. *(Ref: EBS-DRM-024)*

412. Total team capacity: the standard EBS AMS DRM team minimum monthly capacity is 680 hours (SDM 40h + HCM Lead 240h + Finance Lead 160h + DBA+OCI 160h + OIC/Technical 80h). This total is the ARM IT045 reference architecture; actual totals are defined in the AMS agreement schedule and may differ per engagement. *(Ref: EBS-DRM-025)*

413. Above-minimum hours: where the client requires work beyond the contracted minimum hours in any role in any month, the additional hours are engaged at the contracted hourly rate for that role. APPSolve provides an estimate and the client approves prior to the additional work commencing, except for P1 incidents where APPSolve engages the required hours and reports usage immediately after stabilisation. *(Ref: EBS-DRM-026)*

414. Role substitution within team: where the client requires work that is within the DRM scope but falls between role boundaries, the SDM coordinates the most appropriate team member to handle it. Cross-role assistance does not change the minimum hour commitments of the individual roles; it is managed through team collaboration under the SDM. *(Ref: EBS-DRM-027)*

415. Client-side time requirements: the DRM model assumes that the client designates a named AMS Relationship Owner (functional owner of the EBS AMS engagement) who attends governance meetings, approves change requests, and coordinates client-side testing. The absence of a client Relationship Owner does not reduce APPSolve's obligations but may impact the speed of delivery for items requiring client approval. *(Ref: EBS-DRM-028)*

416. Minimum hours floor: the contracted minimum hours per role represent the floor of APPSolve's commitment, not the ceiling. APPSolve will not deliver fewer than the minimum hours to the client in any month, subject to EBS-DRM-035 through EBS-DRM-039 (leave and absence provisions). *(Ref: EBS-DRM-029)*

417. Monthly hours rollover: unused minimum hours in a given month roll over to the following month for the client's use. Unconsumed hours from month N are added to month N+1's available committed hours balance. Rollover hours that remain unconsumed at the end of month N+1 expire and are not further carried forward beyond one additional month. The rollover model is confirmed as the EBS AMS DRM commercial standard. *(Ref: EBS-DRM-030)*

418. Hours tracking system: APPSolve tracks all DRM hours by resource by ticket or activity in its project management and support system. Each time entry is categorised as: incident resolution, service request, proactive maintenance, governance, or knowledge management. The hours consumed against each category and each role are reported in the monthly DRM report per EBS-DRM-058. *(Ref: EBS-DRM-031)*

419. Hours transparency: the client has read access to APPSolve's hours tracking system (or a client-facing dashboard equivalent) to view hours consumed by role and by category in real time. APPSolve provides the access credentials within 10 business days of DRM commencement. Where real-time access is not technically feasible, APPSolve provides a weekly hours snapshot by email every Monday by 10:00 SAST. *(Ref: EBS-DRM-032)*

420. Hours dispute resolution: where the client disputes the hours recorded in the monthly report, the client raises the dispute in writing within 10 business days of receiving the monthly report. APPSolve reviews the disputed entries within 5 business days, provides the supporting ticket and time entry detail, and agrees or adjusts the hours. Adjusted hours are reflected in the following month's report. *(Ref: EBS-DRM-033)*

421. Leave planning notice: named DRM resources coordinate planned leave (annual leave, study leave, medical procedures with advance notice) with the SDM. The SDM notifies the client's AMS Relationship Owner of planned absences of 3 or more consecutive business days a minimum of 10 business days in advance. Notification includes: resource name, absence dates, and coverage arrangement. *(Ref: EBS-DRM-034)*

422. APPSolve illness absorption: APPSolve absorbs unplanned absence (illness, family responsibility leave) of up to 3 business days per named resource per calendar month without commercial impact on the client. Unplanned absence within this limit is covered by APPSolve's internal team on a best-efforts basis. The minimum monthly hours commitment is maintained within a reasonable tolerance of ±5% over the monthly period. *(Ref: EBS-DRM-035)*

423. Illness exceeding 3 days: where a named resource is absent due to illness for more than 3 consecutive business days, APPSolve activates its substitution procedure per EBS-DRM-040. The substitute resource is engaged within 2 business days of the named resource's 4th consecutive day of absence. The client is notified of the substitution. *(Ref: EBS-DRM-036)*

424. Leave and minimum hours: planned annual leave of a named resource in a given month reduces the named resource's available hours for that month below the minimum. Where the leave reduces the resource's available hours to below 80% of the monthly minimum, APPSolve provides a supplementary resource for the shortfall hours at no additional cost to the client. Where the shortfall is less than 20%, APPSolve manages the priority of work internally to deliver the highest-value items within the available hours. *(Ref: EBS-DRM-037)*

425. South African public holidays: South African public holidays are excluded from DRM business hours per AMS-HRS-001. Where a public holiday falls on a day where the client requires DRM coverage (for example, a payroll run scheduled on a public holiday), the client requests coverage a minimum of 5 business days in advance. Public holiday coverage is provided at the contracted overtime or public holiday rate. *(Ref: EBS-DRM-038)*

426. Permanent substitution (planned): APPSolve may permanently substitute a named DRM resource with a replacement of equivalent or higher grade where: (a) the named resource resigns or is terminated; (b) the named resource is promoted to a role that takes them out of AMS delivery; or (c) the named resource and APPSolve mutually agree a role change. APPSolve provides the client with a minimum of 30 days' advance written notice for planned permanent substitutions. *(Ref: EBS-DRM-039)*

427. Client approval right: the client has the right to meet with and assess a proposed permanent replacement before the replacement assumes the named role. The client assessment (competency discussion or practical assessment) is completed within 10 business days of APPSolve's nomination. Where the client objects to a proposed replacement on reasonable grounds related to skills or experience, APPSolve provides an alternative nomination within 10 business days. *(Ref: EBS-DRM-040)*

428. Equivalent grade definition: a replacement resource is considered equivalent grade if they hold: (a) the same or greater years of Oracle EBS experience in the relevant functional or technical domain; (b) the same or greater certifications or qualifications relevant to the role; and (c) demonstrated client-facing AMS experience. Equivalent grade is confirmed as role band equivalence — a replacement meets the standard if they occupy the same or higher role band in APPSolve's grade structure within the relevant EBS domain. *(Ref: EBS-DRM-041)*

429. Emergency substitution: where a named resource becomes unavailable with no advance notice (serious illness, incapacitation, immediate resignation), APPSolve appoints an Acting resource within 2 business days. The Acting resource may be of interim grade (not necessarily equivalent) for the period while APPSolve identifies and assesses a permanent replacement. The permanent replacement process per EBS-DRM-039 applies within 30 days of the emergency substitution. *(Ref: EBS-DRM-042)*

430. Substitution KT period: for planned permanent substitutions, the outgoing named resource and the incoming replacement resource conduct a 30-day knowledge transfer per EBS-DRM-050 through EBS-DRM-055, overlapping where possible. For emergency substitutions, KT is conducted on a best-efforts basis using available runbook documentation. *(Ref: EBS-DRM-043)*

431. Initial DRM onboarding period: for a new DRM engagement, the first 30 calendar days are designated as the knowledge transfer and onboarding period. During this period, the DRM team establishes: system access for all named resources; run books and environment documentation; escalation contacts on both sides; support system configuration; and familiarity with the client's EBS environment and business processes. *(Ref: EBS-DRM-044)*

432. Runbook creation obligation: as part of the initial DRM onboarding (or the DRM KT on a resource substitution), the relevant named resource creates and maintains a client-specific runbook for their domain. Runbook creation is a standard deliverable in all EBS AMS DRM engagements — not conditional on client request. The SDM maintains the master DRM runbook. Runbooks are stored in APPSolve's document management system and a copy is provided to the client on request. Runbooks are reviewed and updated quarterly. *(Ref: EBS-DRM-045)*

433. Runbook domains: minimum runbook coverage per role: (a) SDM: client contact list, escalation tree, SLA summary, governance calendar, change register, active OARs; (b) DBA/OCI Specialist: EBS database configuration, OCI environment diagram (where applicable), backup schedule, patch history, access credentials register (stored securely, not in the runbook body); (c) HCM Functional Lead: HCM module configuration, payroll calendar, integration summary (EBS–PaySpace), key reports; (d) Finance Functional Lead: Finance module configuration, period-end checklist, bank interface details, chart of accounts summary; (e) Technical/OIC Specialist: OIC integration inventory, BeBanking integration map (where applicable), technical customisation log. *(Ref: EBS-DRM-046)*

434. Client environment documentation: within 30 days of DRM commencement, APPSolve delivers an EBS Environment Summary document to the client. This document covers: EBS version and patch level; database version; OCI environment topology (where applicable); custom objects (RICE/CEMLI) inventory; OIC integration list; active interfaces; and known open issues. The client reviews and approves the document. It is maintained and updated quarterly. *(Ref: EBS-DRM-047)*

435. Offboarding KT: where the DRM agreement is terminated (for any reason), APPSolve provides a 30-day transition period from the date of termination notice, during which: (a) the DRM team continues to provide support at the contracted service level; (b) runbooks and documentation are updated to current state and handed to the client; (c) the SDM facilitates a transition briefing with the client's designated successor team or internal team; (d) APPSolve's system access is removed in a managed, agreed sequence to avoid disruption. *(Ref: EBS-DRM-048)*

436. Weekly operational call: the SDM facilitates a weekly operational stand-up (30 minutes, maximum) with the client's AMS Relationship Owner and relevant DRM team members. Agenda: open tickets status; upcoming planned work; resource availability for the week; any at-risk items. Minutes are recorded and distributed within 1 business day of the call. *(Ref: EBS-DRM-049)*

437. Monthly SLA review meeting: the SDM facilitates a monthly SLA review meeting (60 minutes) with the client's AMS Relationship Owner. Agenda: SLA performance for the month (by priority tier); hours consumed vs. minimum by role; incident analysis (top 5 by frequency or business impact); change request pipeline; open OARs; proactive recommendations. The monthly SLA report is circulated 2 business days before the monthly meeting. *(Ref: EBS-DRM-050)*

438. Quarterly service review: the SDM facilitates a quarterly business review (QBR, 90 minutes) with the client's AMS Relationship Owner and the client's senior stakeholder (CIO, IT Manager, or CFO as applicable). Agenda: quarterly SLA trends; service health assessment; strategic roadmap advisory; upcoming Oracle releases or patches relevant to the client's environment; contract performance review; renewal discussion (where approaching contract term). The QBR presentation is circulated 5 business days before the meeting. *(Ref: EBS-DRM-051)*

439. Meeting cancellation policy: where the client cancels a scheduled governance meeting, APPSolve offers a rescheduled meeting within 5 business days of the cancelled date. Where a meeting is cancelled by APPSolve, APPSolve reschedules within 2 business days and circulates any outstanding reports as a written update in lieu of the meeting. Persistent cancellation of governance meetings (3 or more in a rolling quarter by either party) is noted in the QBR as a governance risk. *(Ref: EBS-DRM-052)*

440. Meeting hours: SDM governance meeting hours (preparation, facilitation, follow-up) are charged against the SDM's minimum monthly hours. They do not constitute additional billable hours. Where DRM team members attend governance meetings, the attendance hours are charged against their respective role minimums. *(Ref: EBS-DRM-053)*

441. Monthly DRM report delivery: APPSolve delivers the Monthly DRM Report to the client's AMS Relationship Owner by the 5th business day of the following month. The report covers the calendar month of the preceding month. The SDM owns the report. *(Ref: EBS-DRM-054)*

442. Monthly DRM report content: (a) SLA performance (per priority tier, per EBS-SLA-053); (b) Hours consumed vs. minimum by role — actual hours, minimum, variance, and reason for material variance (>10%); (c) Ticket summary — count by priority by status (open, closed, in-progress); (d) Incident highlight — top 3 incidents by business impact with resolution summary; (e) Proactive maintenance completed; (f) Change requests — approved, in-progress, completed; (g) Open action items; (h) Next month's planned activities; (i) Resource availability and leave schedule for the coming month. *(Ref: EBS-DRM-055)*

443. Hours underspend notification: where any named resource's actual hours in a given month are tracking below 80% of the monthly minimum by the 20th of the month, the SDM notifies the client in writing and proposes activities (from the client's backlog or proactive work queue) to utilise the remaining committed hours. The client may direct the underspend hours or accept them as elapsed. *(Ref: EBS-DRM-056)*

444. Report format: the Monthly DRM Report is delivered in PDF format (or the client's preferred format as agreed at DRM commencement). The raw data supporting the report (ticket logs, time entries) is available to the client on request or via the self-service dashboard per EBS-DRM-032. *(Ref: EBS-DRM-057)*

445. Out-of-scope identification: where a client request falls outside the contracted DRM scope (as defined in the AMS agreement and this overlay), the SDM identifies the out-of-scope item within 1 business day of the request, notifies the client in writing, and provides a preliminary effort estimate for the out-of-scope work as a Change Request. *(Ref: EBS-DRM-058)*

446. CR commercials: out-of-scope work is delivered under a Change Request (CR) at the contracted change request rate per role. The CR is approved by the client's designated approver before APPSolve commences. The CR hours are in addition to the contracted minimum hours and are invoiced separately at the end of the month. *(Ref: EBS-DRM-059)*

447. Out-of-scope examples: items always treated as out of scope for EBS AMS DRM include: new EBS module implementations; major EBS upgrades; custom report development; new OIC integration builds; data migration; DR testing; licence procurement; payroll processing (client-executed, with APPSolve advisory only); RICE/CEMLI development; and third-party application support (unless explicitly included in the AMS agreement). *(Ref: EBS-DRM-060)*

448. Strategic advisory hours: where the DRM agreement includes a strategic advisory component (architecture review, EBS roadmap planning, upgrade assessment), the hours and scope of the strategic advisory service are defined in the AMS agreement. Strategic advisory hours are separate from the incident-and-service-request DRM minimum hours. *(Ref: EBS-DRM-061)*

449. System access provisioning: APPSolve requires the following access for DRM team members to deliver service: (a) Oracle EBS: named user accounts with relevant module access per role; (b) Oracle support portal (My Oracle Support): CSI customer support identifier access for SR management; (c) OCI Console: DBA+OCI Specialist requires OCI tenancy access at the resource level required for EBS database and infrastructure management; (d) APPSolve support system: configured as the client's support channel; (e) Client document management system (read access): for environment documentation and runbook storage. All access is provisioned by the client within 5 business days of DRM commencement. Failure to provision access delays the DRM commencement date by an equivalent period and the SLA clock does not begin until access is complete. *(Ref: EBS-DRM-062)*

450. Oracle Fusion HCM and ERP receive quarterly platform updates from Oracle (typically January, April, July, October). Oracle manages the update schedule; APPSolve does not control Oracle's release cadence. APPSolve provides Oracle quarterly release advisory as a standard AMS service item — reviewing Oracle release notes for the client's contracted modules and flagging changes with potential impact on the client's configured processes. The advisory is a review and notification service. Regression testing, UAT execution, and business process validation following each Oracle quarterly update are excluded from standard AMS unless specifically contracted as a separately priced service. The customer remains responsible for business testing of their own processes before and after each quarterly update. *(Ref: AMS-REL-001)*

451. Where an Oracle quarterly update introduces a change that affects the client's configured process or causes a regression, APPSolve investigates and resolves the regression as an AMS incident under the standard SLA. Oracle platform-caused regressions are investigated by APPSolve; where an Oracle bug is identified, APPSolve logs an Oracle SR and manages resolution. *(Ref: AMS-REL-002)*

452. Oracle quarterly update regression testing — systematically testing all configured processes in a non-production environment after each Oracle update before activating in production — is not included in standard AMS scope. Full regression testing is a separately contracted service. APPSolve recommends regression testing before each quarterly update for high-criticality environments (payroll, financial close, banking integrations). *(Ref: AMS-REL-003)*

453. Acumatica updates: Acumatica releases major version updates and maintenance builds. APPSolve provides Acumatica release advisory under Acumatica AMS — reviewing release notes and flagging customisation compatibility risks. Full Acumatica version upgrade execution is not included in standard AMS and requires a separate upgrade engagement. *(Ref: AMS-REL-004)*

454. BeBanking updates: BeBanking product updates and banking partner connectivity changes are managed by BeBanking. APPSolve monitors for BeBanking-initiated changes that may affect OIC integrations and provides advisory to the client. Format changes or connectivity changes initiated by BeBanking or the client's bank may require OIC integration updates — these are assessed and priced per the OIC pack assumptions. *(Ref: AMS-REL-005)*

455. Oracle Fusion HCM and ERP patches are applied by Oracle as part of the SaaS subscription. APPSolve does not apply Oracle SaaS patches; Oracle manages patching automatically as part of its platform management. APPSolve's role is to monitor for patch-related regressions and resolve them under the AMS SLA. *(Ref: AMS-PAT-001)*

456. Oracle EBS patching: where APPSolve provides AMS for Oracle EBS (on-premises or OCI-hosted), patch assessment, testing, and application are separately contracted. Oracle EBS patching is a technical DBA task and is not included in standard application AMS unless a DBA support component is explicitly in scope. *(Ref: AMS-PAT-002)*

457. Acumatica patching: Acumatica maintenance builds are applied by Acumatica or the client's Acumatica cloud host (Acumatica SaaS or partner-hosted). APPSolve monitors for Acumatica build compatibility with the client's customisations and advises accordingly. Where a build update breaks a client customisation, APPSolve investigates and resolves under AMS. *(Ref: AMS-PAT-003)*

458. Standard AMS includes mailbox monitoring during contracted support hours only — APPSolve monitors the support mailbox and responds to tickets logged during business hours. Proactive monitoring of Oracle OIC integration error consoles, automated alerting, infrastructure monitoring, and application performance monitoring are excluded from standard AMS unless specifically contracted as a monitoring add-on service. Where a monitoring add-on is contracted, APPSolve reviews the OIC error console at the agreed frequency, logs incidents for any failed integrations, and commences investigation within the SLA response time. 24/7 monitoring, automated alerting frameworks, and infrastructure-level monitoring require a separately scoped and priced monitoring engagement. *(Ref: AMS-MON-001)*

459. Proactive monitoring — automated alerting, SLA-based monitoring dashboards, infrastructure monitoring, and log aggregation — requires a separate monitoring tooling arrangement. APPSolve does not provide a proprietary monitoring platform; where the client requires proactive monitoring, APPSolve can configure Oracle OIC's built-in alerting and notification framework as a configuration activity within AMS. *(Ref: AMS-MON-002)*

460. Oracle Fusion HCM and ERP system health monitoring is Oracle's responsibility as the SaaS provider. Oracle operates the infrastructure, monitors availability, and manages platform incidents. The Oracle SaaS status page is the authoritative source for platform availability status. APPSolve does not duplicate Oracle's infrastructure monitoring. *(Ref: AMS-MON-003)*

461. BeBanking monitoring: APPSolve monitors OIC integration error logs for BeBanking H2H integrations where BeBanking AMS is contracted. BeBanking platform monitoring (the BeBanking H2H portal, bank connectivity status) is BeBanking's responsibility. *(Ref: AMS-MON-004)*

462. APPSolve provides a monthly support report to the client's designated AMS contact. The monthly report covers: support activity summary (tickets by priority and status); SLA compliance summary; hours consumed vs. monthly allocation; open incidents and service requests; change requests raised, approved, and in progress; Oracle SR status (where open); planned activities for the following month. *(Ref: AMS-REP-001)*

463. The monthly report is provided within five (5) business days of the end of each calendar month. The report is delivered via email to the client's designated AMS contact and any additional distribution recipients agreed in the AMS agreement. *(Ref: AMS-REP-002)*

464. Quarterly review meeting: APPSolve offers a quarterly AMS service review meeting (60–90 minutes, remote) to review AMS performance, discuss upcoming changes, review Oracle release impacts, and align on priorities. The quarterly review is offered as standard — whether it takes place is at the client's discretion. *(Ref: AMS-REP-003)*

465. Ad hoc reporting: APPSolve provides ad hoc AMS reports on request (for example, a summary of all CRs for the year to date for internal audit, or a support activity extract for a specific period). Ad hoc reports are reasonable requests fulfilled within the monthly hours allocation. *(Ref: AMS-REP-004)*

466. Oracle Cloud support for OCI is the client's direct relationship with Oracle. The client must hold an appropriate Oracle support subscription (Premier Support recommended for production workloads). APPSolve assists the client in raising Oracle support requests where required but is not a proxy for Oracle support. *(Ref: OCI-SUP-001)*

467. APPSolve's OCI project delivery support covers: configuration defects, deployment issues, and infrastructure design queries during the project delivery period. The project delivery support period ends at acceptance sign-off. Post-acceptance support is provided under a separate AMS or Managed OCI Services SOW. *(Ref: OCI-SUP-002)*

468. APPSolve's AMS OCI support scope covers the OCI infrastructure services explicitly named in the AMS SOW. OCI services not named in the AMS SOW are not covered by the AMS support agreement. Expansion of AMS OCI scope requires a SOW amendment. *(Ref: OCI-SUP-003)*

469. Critical OCI infrastructure incidents under an AMS SOW are escalated to Oracle support by APPSolve on the client's behalf where the root cause is an OCI platform issue. APPSolve cannot resolve Oracle platform outages — Oracle's support SLA governs resolution. APPSolve communicates Oracle's support status to the client. *(Ref: OCI-SUP-004)*

470. OCI tenancy administration support (user management, compartment changes, policy amendments) is included under an AMS SOW as a standard service request type. The volume of service requests covered per period is defined in the AMS SOW. *(Ref: OCI-SUP-005)*

471. Security incident response for OCI (Cloud Guard alert response, suspected breach, anomalous activity) under an AMS SOW follows APPSolve's incident response procedures. APPSolve does not provide a dedicated 24x7 SOC for OCI security monitoring. Security incident response outside business hours requires a separately scoped on-call retainer. *(Ref: OCI-SUP-006)*

472. OCI cost spike investigation (unexpected OCI bill increases) is included as a standard service request under a Managed OCI Services AMS SOW. APPSolve investigates root causes and recommends remediation. APPSolve cannot reverse or credit OCI charges — Oracle billing is the client's direct financial relationship. *(Ref: OCI-SUP-007)*

473. APPSolve's OCI support team holds current Oracle OCI certifications. The minimum OCI certification requirement for APPSolve OCI support is Oracle Cloud Infrastructure Architect Associate. Senior OCI support engineers hold OCI Architect Professional certification. Certification currency is validated at AMS renewal. *(Ref: OCI-SUP-008)*

474. Hypercare for OIC integrations aligns with APPSolve's HCM Base hypercare standard (HCM-HYP-001 through HCM-HYP-003): four (4) weeks' duration; business hours (08:00–17:00 SAST, Monday to Friday); defect resolution and stabilisation only; enhancements, new integrations, and scope additions excluded. *(Ref: OIC-SUP-001)*

475. OIC hypercare runs concurrently with the primary project's hypercare period. Where OIC is delivered as part of the same project as Oracle HCM or Oracle ERP, the single four-week hypercare period covers both the primary modules and the OIC integrations. The hypercare period commences on the go-live date of the last module or integration to go live in the project. Where OIC is delivered as a standalone project without a primary HCM or ERP module, hypercare commences on the date of the last integration go-live. OIC hypercare does not extend beyond the four-week default unless separately contracted. *(Ref: OIC-SUP-002)*

476. Integration enhancements during hypercare — including adding new fields to an existing integration, adding new integrations not in the agreed Integration Inventory, changing the integration's frequency or trigger mechanism, or adding new error handling behaviour — are excluded from hypercare scope. These are assessed as Change Requests or as new project work. *(Ref: OIC-SUP-003)*

477. Third-party vendor API changes — including vendor-initiated API version upgrades, vendor API deprecations, vendor authentication method changes, or vendor endpoint URL changes — that occur during or after hypercare are outside APPSolve's hypercare obligation. The client is responsible for: maintaining the vendor relationship; notifying APPSolve of impending vendor API changes; and engaging APPSolve to assess and implement required integration changes. Integration updates required as a result of vendor-initiated API changes are priced as Change Requests. *(Ref: OIC-SUP-004)*

---

## Section F — Security and Access Management Assumptions

*This section covers security configuration, access control, and compliance assumptions across all solution components.*

478. APPSolve designs and configures the Oracle Fusion ERP security model: job roles, data security policies, duty roles, and abstract roles. The security design is agreed in the Scope and Design phase. APPSolve uses Oracle-delivered roles as the starting point and creates custom roles only where Oracle-delivered roles do not meet the client's access requirements. *(Ref: ERP-SEC-001)*

479. The number of custom job roles is confirmed in the Scope and Design phase. Standard APPSolve ERP security designs use the following Oracle-delivered role archetypes: Financial Analyst, AP Invoice Supervisor, AR Billing Specialist, Cash Manager, Procurement Manager, Procurement Agent, and Project Manager. Custom roles are created for access patterns not covered by Oracle-delivered roles. *(Ref: ERP-SEC-002)*

480. Data security policies — row-level security restricting users to specific ledgers, business units, legal entities, or cost centres — are designed in the Scope and Design phase. Complex data security requirements (for example, a user who can view GL for one legal entity but AP for a different business unit) increase design and testing effort and are assessed per complexity. *(Ref: ERP-SEC-003)*

481. Segregation of Duties (SoD) awareness: APPSolve designs Oracle ERP roles following Oracle's recommended SoD guidelines. Formal SoD analysis — using Oracle Access Controls Governor (ACG), Fastpath, or equivalent specialist SoD tool — is excluded from base scope. Where a formal SoD audit is required (for example, by external auditors or internal audit), it is assessed as a separately scoped item using the appropriate tool. *(Ref: ERP-SEC-004)*

482. User provisioning post-go-live: creating new Oracle ERP users, assigning roles to users, and deactivating users who leave the organisation are the client's IT team's responsibility after go-live. APPSolve configures the user provisioning framework during implementation; ongoing user lifecycle management is operational, not implementation, work. *(Ref: ERP-SEC-005)*

483. Single Sign-On (SSO) is excluded from base ERP scope unless explicitly scoped and listed in the proposal. Oracle Fusion ERP supports SAML 2.0 SSO as an Oracle platform feature. Where the client uses Microsoft Azure AD / Entra ID and holds Oracle Fusion Cloud licensing that supports SAML 2.0 federation, SSO can be included in the implementation as a separately listed configuration activity — this must be explicitly named in the proposal scope section and priced accordingly. SSO configuration with other identity providers (Okta, Ping Identity, Google Workspace, ADFS) is assessed per client environment. In all cases, the client's IT security team must provide IdP federation metadata and co-ordinate certificate configuration before SSO configuration commences. *(Ref: ERP-SEC-006)*

484. OCI security configuration is delivered against Oracle's CIS OCI Foundations Benchmark (Level 1) as APPSolve's standard OCI security delivery baseline. Compliance with higher security standards (CIS Level 2, ISO 27001, PCI-DSS, SOC 2) requires explicit scoping and may require specialist security advisory services. Where a client operates in a regulated industry (South African financial services, government, healthcare), APPSolve will flag this at pre-sales and recommend an OCI Security Addendum discussion before proposal finalisation. Regulated-industry security requirements that exceed the CIS Level 1 baseline are out of scope for the standard OCI pack and must be separately scoped. *(Ref: OCI-SEC-001)*

485. OCI Cloud Guard is enabled and configured in the tenancy as part of the standard security baseline. Cloud Guard detects misconfigurations and threat indicators. Remediation of Cloud Guard findings post-handover is the client's operational responsibility. APPSolve configures Cloud Guard detector rules during the engagement and provides a Cloud Guard baseline report at project close. *(Ref: OCI-SEC-002)*

486. OCI Security Zones are applied to the Production compartment as a standard control. Security Zone policies enforce mandatory encryption, prevent public access to storage objects, and enforce other baseline controls. Any client request to disable Security Zone policies in production must be approved in writing by the client's CISO or equivalent and documented as a risk-accepted variance. *(Ref: OCI-SEC-003)*

487. Encryption at rest is enabled for all OCI resources using Oracle-managed encryption keys as the default. Customer-managed encryption keys (CMEK) via OCI Vault are available but require additional configuration and key management operational procedures. CMEK is not assumed by default — it must be explicitly included in the SOW if required by the client's security policy. *(Ref: OCI-SEC-004)*

488. Encryption in transit is enforced for all data moving between OCI services, between OCI and on-premise networks, and between OCI public internet endpoints and users. APPSolve configures TLS termination at load balancers and ensures all OCI service endpoints use HTTPS/TLS. Plaintext communication channels in production environments are not configured. *(Ref: OCI-SEC-005)*

489. OCI Audit logging is enabled for all tenancy-level and compartment-level events. Audit logs are retained per Oracle's default 90-day retention window. If the client requires longer audit log retention (e.g., 1 year for regulatory compliance), logs must be exported to OCI Object Storage and the client provides the retention policy. Extended retention is not assumed by default. *(Ref: OCI-SEC-006)*

490. Penetration testing of OCI infrastructure is not included in APPSolve's scope. If the client requires penetration testing, this is procured from a specialist security vendor and coordinated through Oracle's penetration testing notification process. APPSolve will provide architecture documentation to the pen test vendor on request. *(Ref: OCI-SEC-007)*

491. Vulnerability scanning of OCI compute instances is the client's operational responsibility after handover. APPSolve may recommend OCI's native vulnerability scanning service (OS Management Hub) and configure it if explicitly included in the SOW. Ongoing scan management and remediation are not included in the standard engagement. *(Ref: OCI-SEC-008)*

492. Data residency: APPSolve configures OCI workloads to reside exclusively within the contracted OCI region(s). Cross-region data replication for DR purposes (where included in scope) is explicitly defined in the DR design document. APPSolve does not configure cross-border data replication without explicit client approval. *(Ref: OCI-SEC-009)*

493. OCI Security Advisor is run during the engagement to validate the architecture against Oracle's security recommendations. The Security Advisor report is provided to the client as a handover deliverable. Any accepted findings not fully remediated are documented with the client's written acknowledgement. *(Ref: OCI-SEC-010)*

494. The client's IT team is responsible for all endpoint security configuration required to enable OIC connectivity. This includes, but is not limited to: firewall rules permitting outbound and inbound traffic on required ports; IP address whitelisting of Oracle OIC's published IP ranges at third-party endpoints; VPN configuration where required; network access control list (ACL) changes. APPSolve provides Oracle OIC's IP ranges and required port specifications; the client's IT team implements the network configuration. *(Ref: OIC-SEC-001)*

495. All firewall rule changes required to allow Oracle OIC traffic to reach source or target systems must be completed before SIT commences. Delays in firewall configuration directly delay SIT and extend the project timeline. Timeline impact from delayed firewall changes is the client's risk. *(Ref: OIC-SEC-002)*

496. Third-party endpoint IP whitelisting — where the third-party vendor must approve Oracle OIC's IP addresses before the connection is permitted — is the client's responsibility to coordinate with the vendor. APPSolve provides the Oracle OIC IP address ranges; the client manages the vendor approval process. *(Ref: OIC-SEC-003)*

497. APPSolve is responsible for OIC connection configuration within the Oracle OIC platform: configuring connection agents, setting authentication parameters, configuring connection properties, and testing connectivity from OIC to the endpoint. APPSolve is not responsible for network-layer security, infrastructure security, or endpoint system security configuration. *(Ref: OIC-SEC-004)*

498. The default authentication method for REST-based integrations is OAuth 2.0 (client credentials grant) where supported by the endpoint, or Basic Authentication where OAuth is not available. Alternative authentication methods (API key, JWT bearer token, custom token, certificate-based mutual TLS) are implemented where required by the endpoint. The authentication method is confirmed per endpoint in the Integration Inventory and TDD. *(Ref: OIC-SEC-005)*

499. Service accounts required for Oracle OIC to authenticate to source and target systems are provisioned by the client's IT team or system administrators. APPSolve specifies the required service account permissions for each integration. Service accounts must be created and credentials provided to APPSolve before the build phase commences. APPSolve does not create user accounts or modify access controls in the endpoint systems. *(Ref: OIC-SEC-006)*

---

## Section G — Client Responsibilities and Dependencies

*This section defines all obligations on the Client that are conditions of this engagement. APPSolve's pricing, timeline, and delivery commitments are contingent on the Client fulfilling these obligations.*

500. **Executive Sponsorship:** The client appoints an ERP project sponsor with authority to make business decisions affecting the ERP implementation: approving scope, resolving escalated design issues, authorising go-live, and driving internal change management. Without an empowered sponsor, design decisions stall. *(Ref: ERP-CUS-001)*

501. **Functional Team:** The client appoints functional leads for each module in scope (Finance Lead for GL/AP/AR/FA/CM; Procurement Lead for Procurement; PPM Lead for Projects). Functional leads are available for the full project duration, attend all workshops and CRP sessions, make business decisions in their domain, and provide sign-off at each milestone. *(Ref: ERP-CUS-002)*

502. **Chart of Accounts Design:** The COA structure — segments, value sets, and code combination values — is the client's most critical deliverable in the Scope and Design phase. The client's finance team provides the COA design (or APPSolve facilitates COA design workshops and the client approves the output) before COA configuration commences. COA delays cascade to all downstream configuration. *(Ref: ERP-CUS-003)*

503. **Data Provision:** The client extracts, cleanses, and provides all migration data in APPSolve's FBDI templates by the dates agreed in the project plan. Suppliers, customers, fixed assets, open payables, open receivables, open purchase orders, and projects — all data objects require client preparation. Late or incomplete data provision directly delays the go-live date. *(Ref: ERP-CUS-004)*

504. **Data Cleansing:** The client cleanses and validates source data before providing it to APPSolve. This includes: removing duplicate supplier or customer records; populating mandatory fields; correcting incorrect account codes; updating inactive or blocked records; and confirming bank account details. APPSolve does not cleanse source data. *(Ref: ERP-CUS-005)*

505. **Business Process Decisions:** The client's functional team makes all business process decisions required during the Scope and Design phase: which transaction types to use; how approval workflows should route; what payment terms to configure; which cost centres to include in the COA; how project billing works. APPSolve facilitates and documents; the client decides. *(Ref: ERP-CUS-006)*

506. **Authority Matrix:** The client provides the complete, approved authority matrix for all transaction types requiring approval — purchase requisitions, purchase orders, supplier invoices, journals, capex requests — before workflow configuration commences. The authority matrix must be authorised by the appropriate governance authority (CFO, CEO, or Finance Director). *(Ref: ERP-CUS-007)*

507. **Tax Configuration Information:** The client's tax team provides all tax configuration requirements: SA VAT registration number; applicable VAT rates and tax classifications (standard-rated, zero-rated, exempt, out-of-scope); withholding tax requirements; and any industry-specific tax treatment. APPSolve configures Oracle ERP tax based on this information; it does not provide tax advice. *(Ref: ERP-CUS-008)*

508. **Statutory Compliance Responsibility:** The client's finance and tax team is responsible for ensuring Oracle ERP configuration meets applicable statutory and regulatory requirements: Companies Act reporting, SARS VAT/PAYE requirements, IFRS or GAAP compliance, and any industry-specific regulations. APPSolve configures Oracle ERP based on requirements provided by the client; it does not provide tax, legal, or audit advice. *(Ref: ERP-CUS-009)*

509. **Testing Participation:** The client's functional team and user community participate in CRP1, CRP2, and UAT. The client provides test data, supplies UAT testers, executes UAT scenarios, logs defects, and provides written sign-off at each testing milestone. *(Ref: ERP-CUS-010)*

510. **Training Delivery:** The client is responsible for end-user training delivery, scheduling, communication, and adoption measurement. APPSolve trains the client's trainers (TTT); the client's trainers deliver to end users. The client provides training venue, equipment, and scheduling logistics. *(Ref: ERP-CUS-011)*

511. **Change Management:** Internal change management — communicating the ERP project to employees, managing transition from the legacy system, addressing adoption challenges, and measuring post-go-live adoption — is the client's leadership and HR responsibility. APPSolve provides implementation expertise; it does not run change management programmes. *(Ref: ERP-CUS-012)*

512. **Business Ownership:** The client appoints a designated business owner for each integration. The business owner is accountable for: defining and approving integration requirements; attending and contributing to mapping workshops; validating mapping decisions; reviewing and signing off the Mapping Specification and TDD; executing or overseeing UAT; and providing go-live sign-off. Without a designated business owner, integration requirements cannot be finalised. *(Ref: OIC-CUS-001)*

513. **Test Participation:** The client appoints UAT testers for each integration. UAT testers attend UAT sessions, execute test scenarios, record defect observations, and provide test sign-off. The client ensures UAT testers are available during the agreed UAT testing window. If UAT testers are unavailable during the agreed window, UAT is deferred and the timeline is extended. *(Ref: OIC-CUS-002)*

514. **Infrastructure Readiness:** The client ensures that all source and target systems are technically configured and accessible before SIT commences. For each integration endpoint, the client confirms: (a) the system is deployed and accessible in the relevant environment; (b) test data is available in the system; (c) technical credentials for OIC connectivity have been provisioned; (d) the system administrator is available to support connectivity testing. *(Ref: OIC-CUS-003)*

515. **Security Readiness:** The client's IT team completes all firewall rule changes, IP whitelisting configurations, network ACL updates, and VPN configurations required to allow Oracle OIC to reach source and target systems before SIT commences. APPSolve provides the required Oracle OIC IP ranges and port requirements. The client manages the IT change management process internally to ensure changes are implemented before the agreed SIT start date. *(Ref: OIC-CUS-004)*

516. **Certificates:** The client procures all SSL/TLS certificates required for integration connectivity and provides them to APPSolve before SIT commences. The client confirms that all provided certificates are valid (not expired), correctly configured (covering the correct domain names), and in the correct format for Oracle OIC import. Certificate expiry dates must extend beyond the project's planned go-live date. *(Ref: OIC-CUS-005)*

517. **Endpoint Availability:** The client ensures that all integration endpoints (source systems, target systems, and third-party vendor sandboxes) are available during agreed SIT and UAT testing windows. Where planned maintenance of endpoint systems is scheduled during testing windows, the client notifies APPSolve at least five (5) business days in advance. APPSolve adjusts the testing schedule where operationally feasible. *(Ref: OIC-CUS-006)*

518. **Vendor Coordination:** The client is responsible for the commercial and technical relationship with all third-party vendors whose systems are included in the integration scope. Client responsibilities include: obtaining API documentation from each vendor; requesting vendor sandbox access; escalating vendor responsiveness issues; managing vendor participation in SIT; and managing vendor API version change communications. APPSolve is not a party to the client–vendor commercial relationship and cannot compel vendors to provide access, documentation, or support. *(Ref: OIC-CUS-007)*

519. **Data Validation:** The client is responsible for validating the business accuracy of data flowing through integrations during UAT. APPSolve validates technical accuracy (data was transmitted correctly, in the correct format, to the correct endpoint). Business accuracy — confirming that the data in the target system is correctly classified, coded, and attributed according to the client's business rules — is the client's UAT team's responsibility. *(Ref: OIC-CUS-008)*

520. **Sign-Offs:** The client provides written sign-off at each of the following integration milestones: (a) Mapping Specification sign-off (prerequisite for build); (b) Technical Design Document sign-off (prerequisite for build); (c) SIT completion sign-off (prerequisite for UAT); (d) UAT completion sign-off (prerequisite for production cutover); (e) Go-live authorisation (prerequisite for production deployment). Sign-off by email from the client's designated project manager or sponsor is acceptable. *(Ref: OIC-CUS-009)*

521. **Service Accounts:** The client's IT team or system administrators provision all service accounts required for Oracle OIC to authenticate to source and target systems. APPSolve specifies the required service accounts, required permissions, and required credentials format for each integration. Service accounts must be created and credentials confirmed before the build phase commences. APPSolve does not create user accounts, modify access controls, or manage access provisioning in endpoint systems. *(Ref: OIC-CUS-010)*

522. **API Documentation:** The client obtains and provides complete API documentation from all third-party vendors before the integration design phase commences. API documentation must include: the vendor's API reference (endpoints, request/response schema, authentication requirements, error codes); the vendor's connectivity prerequisites; and the vendor's support contact for technical integration queries. Where a vendor requires the client to complete an onboarding or registration process before API access is granted, the client initiates and completes this process in advance. *(Ref: OIC-CUS-011)*

523. **OIC Licence and Environment:** The client ensures a valid Oracle OIC Enterprise or Standard subscription is active and that the OIC environment is provisioned, accessible, and at the correct release version before integration development commences. The client is responsible for Oracle licence renewal, Oracle OIC upgrade management, and Oracle OIC environment administration throughout the project and post-go-live. *(Ref: OIC-CUS-012)*

524. Oracle OIC Enterprise (B91110) licence must be active and the OIC environment provisioned and accessible before integration development commences. If OIC provisioning is delayed, integration development is deferred accordingly. *(Ref: OIC-DEP-001)*

525. All source and target system technical specifications must be available and agreed before the integration design phase is completed. Undefined or changing endpoint specifications after design sign-off delay build and constitute a mapping change. *(Ref: OIC-DEP-002)*

526. Where OIC integrations connect to Oracle Fusion HCM or Oracle Fusion ERP modules, those modules must be sufficiently configured in the non-production environment before SIT of dependent integrations commences. For example, an integration that sends employee data from HCM to a payroll system depends on the HCM Core module being configured and test data being available in HCM. *(Ref: OIC-DEP-003)*

527. Third-party vendor API availability and technical documentation are a dependency for all integrations connecting to non-Oracle systems. If a vendor does not provide API documentation or sandbox access before the design phase, the integration design cannot be completed. The client is responsible for managing this dependency. *(Ref: OIC-DEP-004)*

528. The Mapping Specification and Technical Design Document for each integration must be signed off before build commences. All mapping workshops, business mapping decisions, and code-set translation tables must be provided by the client before workshop outcomes can be finalised. *(Ref: OIC-DEP-005)*

529. Production credentials for all source and target systems must be available before production cutover. Where production credentials differ from non-production credentials (for example, different service accounts, different API endpoints, different certificates), the client provides production credentials at least five (5) business days before the scheduled cutover date. *(Ref: OIC-DEP-006)*

530. APPSolve configures Oracle OIC only. APPSolve does not configure, administer, support, or troubleshoot the source or target systems on either side of an integration. Any configuration changes, data corrections, or system administration actions required in source or target systems during the integration project are the responsibility of the respective system administrators. *(Ref: OIC-CON-001)*

531. Integration performance is subject to Oracle OIC's published platform constraints — including maximum message payload size, maximum messages per hour per integration, maximum concurrent integration executions, and API gateway rate limits. APPSolve designs integrations within these constraints. Performance issues caused by Oracle OIC platform limits are escalated to Oracle Support; APPSolve assists with the technical escalation but cannot override Oracle's platform constraints. *(Ref: OIC-CON-002)*

532. Oracle OIC integration capability depends on the existence of an Oracle-supported adapter or the availability of a standard REST/SOAP API at the endpoint. Where an endpoint system does not expose a REST or SOAP API, and where SFTP/file-based integration is not feasible, the integration cannot be implemented using Oracle OIC without custom adapter development. Custom adapter development is excluded from standard scope and requires assessment. *(Ref: OIC-CON-003)*

533. APPSolve cannot guarantee third-party vendor API uptime, API versioning stability, or vendor response times during the integration project. If a vendor's API is unstable, underdocumented, or subject to breaking changes during the project, APPSolve will document the impact and raise it as a project risk for the client to manage with the vendor. *(Ref: OIC-CON-004)*

534. OIC integration scope is bounded by the Integration Inventory agreed in the Scope and Design phase. Integrations added after the Integration Inventory is signed off require a formal Change Request that re-prices the design, build, test, and cutover effort for the new integration. *(Ref: OIC-CON-005)*

535. APPSolve classifies all OIC integrations using a three-tier complexity model for estimation. Every integration in the Integration Inventory is assigned a tier during Scope and Design; the tier is documented in the project estimate. - **Simple:** One source system, one target system. Standard Oracle adapter. Limited data transformation — direct field mapping with minimal lookups. No orchestration. Standard authentication (OAuth 2.0, Basic Auth). Small to medium payload. Well-documented vendor API with sandbox available. - **Standard:** One source system, one target system. Moderate data transformation — code-set lookups, conditional logic, data splitting or merging. Standard error handling and retry. One-to-one field mapping plus lookups. Typical payload. Reasonably documented vendor API. - **Complex:** Multi-step orchestration involving three or more systems, or multi-step processing within a single flow. Multiple business objects in a single integration. Complex transformations — calculations, aggregations, multi-level conditional branching. High-volume or near-real-time processing. Non-standard adapter. Custom or complex authentication — mTLS, JWT, custom token. No vendor sandbox available; production credentials only for testing. Integrations that do not clearly fit a single tier are assessed by the project lead and categorised with a documented rationale in the estimate. *(Ref: OIC-CON-006)*

536. **Business Process Ownership:** The client owns its business processes. AMS covers the application layer; the client's functional leads are responsible for deciding whether a business process change is needed, documenting the requirement, and approving the solution before APPSolve implements it. APPSolve does not redesign business processes under AMS. *(Ref: AMS-CUS-001)*

537. **User Support (Level 1):** The client's internal helpdesk or ERP team provides first-line support to end users — answering how-to questions, resetting passwords, explaining existing functionality, and triaging whether an issue is a user error or a system issue. This Level 1 responsibility belongs to the client unless explicitly contracted to APPSolve. *(Ref: AMS-CUS-002)*

538. **User Access Management:** Creating new user accounts, assigning Oracle ERP or Oracle HCM roles to users, and deactivating users who leave are the client's IT team's responsibility, unless APPSolve has been contracted to provide user access management as part of the AMS agreement. *(Ref: AMS-CUS-003)*

539. **Internal Change Management:** Communicating system changes to the client's user population, updating internal user guides and job aids, and managing internal business change resulting from configuration updates are the client's responsibility. *(Ref: AMS-CUS-004)*

540. **Change Request Approval:** All change requests must be approved in writing by the client's designated AMS contact (or a named delegate) before APPSolve commences work. Verbal approval is not sufficient. APPSolve does not proceed with a CR without written approval. *(Ref: AMS-CUS-005)*

541. **Test Sign-Off:** Where a change request, service request, or incident resolution requires testing before production deployment, the client's functional team performs and signs off the test. APPSolve deploys to production only after written client sign-off on the test outcome. *(Ref: AMS-CUS-006)*

542. **Information Provision:** The client provides accurate and complete information when logging support tickets — including error messages, screenshots, steps to reproduce, affected users, and business impact. Incomplete ticket information delays investigation. APPSolve is not responsible for SLA delays caused by insufficient information provided by the client. *(Ref: AMS-CUS-007)*

543. **Internal IT Responsibilities:** Network connectivity, hardware, browser compatibility, VPN access, printer configuration, and other IT infrastructure are the client's IT team's responsibility. APPSolve provides application support only; infrastructure support is not in AMS scope. *(Ref: AMS-CUS-008)*

544. **Oracle Support Access:** The client provides APPSolve with access to the client's Oracle Support account (Customer Support Identifier — CSI) to log Oracle SRs on the client's behalf. Without CSI access, APPSolve cannot manage Oracle SRs directly and the client must log SRs themselves. APPSolve can provide the SR description and evidence for the client to log. *(Ref: AMS-CUS-009)*

545. **AMS Onboarding Documentation:** At the start of an AMS engagement, the client provides APPSolve with access to: the implementation project documentation (Scope and Design documents, configuration workbooks, test sign-off records); current system access credentials for the AMS team; and an introduction to the client's internal ERP/IT team contacts. Where implementation was done by APPSolve, this documentation already exists. *(Ref: AMS-CUS-010)*

---

## Section H — Explicit Exclusions and Out-of-Scope Items

*The following items are explicitly excluded from the scope of this engagement. Any request to include excluded items will be treated as a change request and priced separately.*

546. **Oracle Fusion Global Payroll:** Native Oracle payroll processing (gross-to-net calculation, payslip generation, PAYE submission) is excluded. South African payroll is managed by a third-party payroll provider (PaySpace, Sage 300 People, VIP Premier, or equivalent) integrated via OIC. *(Ref: ERP-EXC-001)*

547. **Oracle Fusion Expenses:** Employee expense claim management (Oracle Fusion Expenses Cloud Service) is excluded from base ERP scope unless explicitly included in the Oracle BOM. Where Oracle Expenses is required, it is separately licensed and separately scoped. *(Ref: ERP-EXC-002)*

548. **SARS eFiling Integration:** SARS eFiling integration is not an APPSolve standard ERP capability and is excluded unless specifically scoped as a custom integration (see ERP-INT-005). Oracle Fusion ERP does not integrate natively with the SARS eFiling portal. VAT201, PAYE EMP201, and provisional tax return submission are the client's tax team's responsibility. Tax reporting data extracts from Oracle OTBI to support the client's eFiling process may be included where explicitly listed in the proposal. *(Ref: ERP-EXC-003)*

549. **Formal SoD Analysis and Remediation:** Systematic SoD conflict identification, user access risk reporting, and SoD remediation using Oracle Access Controls Governor, Fastpath, or equivalent is excluded from base scope. *(Ref: ERP-EXC-004)*

550. **Oracle Supplier Portal:** Supplier self-service for invoice submission, PO acknowledgement, and supplier profile management is excluded. Requires separate Oracle licence and separately scoped OIC integration. *(Ref: ERP-EXC-005)*

551. **Oracle Fusion Risk Management (Advanced Controls):** Oracle's risk management and financial reporting compliance product is separately licensed and excluded from base ERP scope. *(Ref: ERP-EXC-006)*

552. **Legacy System Decommissioning:** Shutdown, data archiving, and decommissioning of the client's legacy ERP system after Oracle go-live is the client's responsibility and is excluded from this engagement. *(Ref: ERP-EXC-007)*

553. **Parallel Running:** Simultaneous operation of the legacy ERP and Oracle Fusion ERP post-go-live is excluded from base scope. See ERP-CUT-005. *(Ref: ERP-EXC-008)*

554. **Business Process Redesign:** Designing new or fundamentally different business processes is excluded. APPSolve configures Oracle ERP to support the agreed future-state processes confirmed in Scope and Design. Business process redesign consulting is separate from ERP implementation. *(Ref: ERP-EXC-009)*

555. **Invoice OCR and Intelligent Document Capture:** Automated invoice image capture, OCR data extraction, and AI-powered invoice processing are excluded from base scope. Standard AP scope is manual invoice entry. *(Ref: ERP-EXC-010)*

556. **Oracle Revenue Management Cloud (IFRS 15 / ASC 606 Complex Scenarios):** Complex revenue recognition — multiple-element arrangements, variable consideration, licence vs service distinction, contract modification accounting — may require Oracle Revenue Management Cloud (separately licensed). Standard Oracle AR revenue recognition is included; IFRS 15 complex scenarios require assessment. *(Ref: ERP-EXC-011)*

557. **Audit Deliverables and CAAT Reports:** Producing audit deliverables, Computer Assisted Audit Techniques (CAAT) reports, or auditor-specific testing reports for external or internal auditors is excluded. Standard Oracle OTBI reports are available for audit support; bespoke audit deliverables are not in implementation scope. *(Ref: ERP-EXC-012)*

558. FastConnect (OCI dedicated circuit) provisioning requires coordination with a FastConnect partner (e.g., BCX, Liquid Telecom, Vox Telecom). APPSolve designs the FastConnect architecture and provides specifications to the FastConnect partner. Procurement, commercial agreements with the FastConnect partner, and physical circuit provisioning are the client's responsibility. FastConnect lead times are typically 6–12 weeks and must be planned accordingly. *(Ref: OCI-EXT-001)*

559. Third-party SaaS application integration with OCI-hosted Oracle applications is in scope for OCI network connectivity only (e.g., configuring outbound OCI network access to a third-party SaaS endpoint). Application-level integration logic (API calls, data mapping, authentication) is in scope per the Integration pack. APPSolve does not configure or support third-party SaaS applications directly. *(Ref: OCI-EXT-002)*

560. Oracle Cloud Marketplace ISV solutions (third-party software from the OCI Marketplace) deployed on OCI are provisioned by APPSolve using the Marketplace image. The ISV's support relationship is directly between the client and the ISV. APPSolve does not support, patch, or maintain ISV software post-handover. *(Ref: OCI-EXT-003)*

561. Content Delivery Network (CDN) integration (OCI's Akamai-powered CDN) for OCI-hosted applications is included where explicitly required by the application design (e.g., for APEX public applications requiring global content distribution). CDN configuration is a separate scope item and is not assumed by default. *(Ref: OCI-EXT-004)*

562. Oracle Cloud for Government region requirements are out of scope for the standard OCI pack. South African government clients with data sovereignty requirements mandating Government regions require a separate engagement design. OCI Government regions may have limited service availability compared to commercial regions. *(Ref: OCI-EXT-005)*

563. Third-party product-specific OCI infrastructure assumptions (for example, assumptions specific to BeBanking, Acumatica, or other products hosted on OCI) are not included in the standard OCI Infrastructure Assumption Pack. Product-specific OCI assumptions are maintained within the relevant product assumption packs where required. The OCI Infrastructure Assumption Pack governs the shared OCI infrastructure layer applicable to any supported workload. *(Ref: OCI-EXT-006)*

564. Export control and cross-border data compliance: OCI data residency is maintained within the contracted OCI region. Cross-border data transfer requirements (e.g., POPIA Section 72, financial sector cross-border restrictions) are the client's legal responsibility to identify. APPSolve configures OCI to maintain data within the specified region but is not the client's legal compliance advisor. *(Ref: OCI-EXT-007)*

565. Oracle Cloud Customer Connect resources are available to clients with active Oracle support subscriptions. APPSolve may reference Customer Connect knowledge base articles during engagements. Customer Connect does not replace Oracle's paid support for production issues. *(Ref: OCI-EXT-008)*

566. Independent Software Vendor software licence compliance on OCI is the client's responsibility. APPSolve provisions OCI infrastructure to the specifications required by the ISV's licensing documentation. Over-provisioning or under-provisioning that results in ISV licence non-compliance is not APPSolve's liability. *(Ref: OCI-EXT-009)*

567. EBS on OCI: Oracle's EBS on OCI program (EBS Cloud Manager, EBS lift-and-shift) requires an active Oracle E-Business Suite software support subscription. APPSolve assumes the client holds current EBS software support with Oracle. The ERP Assumption Pack and OCI Infrastructure Assumption Pack together provide sufficient assumption coverage for EBS on OCI engagements. A separate EBS-OCI Addendum assumption pack is not required at this time; if EBS-specific OCI assumptions beyond the current combined pack coverage are identified in a specific engagement, they will be documented as project-level assumption supplements in that engagement's SOW. *(Ref: OCI-EXT-010)*

568. **Data Cleansing:** Cleansing, de-duplicating, reformatting, or improving the quality of source system data before it passes through an OIC integration is excluded. Where poor source data quality causes integration failures, the root cause is the data quality issue in the source system, not the integration itself. The client is responsible for source data quality. *(Ref: OIC-EXC-001)*

569. **Source System Remediation:** Fixing configuration defects, data integrity issues, missing master data, or API defects in source systems that prevent the integration from functioning is excluded. APPSolve identifies and documents source system issues encountered during SIT; resolution is the source system owner's responsibility. *(Ref: OIC-EXC-002)*

570. **Third-Party Vendor Management:** Managing the commercial relationship, SLA, or performance of third-party vendors whose systems are integration endpoints is excluded. APPSolve provides technical integration expertise; the client owns the vendor relationship. *(Ref: OIC-EXC-003)*

571. **Infrastructure Procurement:** Procuring, provisioning, or managing any infrastructure components required by the integration — including servers, networks, cloud infrastructure beyond Oracle OIC, SFTP servers, load balancers, or API gateways — is excluded. Oracle OIC itself is managed by Oracle; the client is responsible for all other infrastructure. *(Ref: OIC-EXC-004)*

572. **Network Troubleshooting:** Diagnosing or resolving network connectivity issues between the client's infrastructure and third-party endpoints — including network latency, packet loss, DNS resolution failures, and routing issues — is excluded. Oracle OIC connects via the public internet or via Oracle's private network fabric; network troubleshooting at the client or vendor network layer is the respective IT team's responsibility. *(Ref: OIC-EXC-005)*

573. **Business Process Redesign:** Redesigning the business process that the integration supports — including changing workflow, changing approval hierarchies, redesigning data flows for business reasons, or re-engineering systems to accommodate integration — is excluded from OIC scope. *(Ref: OIC-EXC-006)*

574. **Change Management and User Adoption:** Change management activities associated with the business impact of integrations — including stakeholder communication about integrated system changes, training users on new process flows enabled by the integration, or user adoption measurement — are excluded. *(Ref: OIC-EXC-007)*

575. **Training Beyond Agreed Super-User Scope:** Training delivery beyond the agreed super-user or administrator training scope for Oracle OIC monitoring and operations is excluded. APPSolve delivers one round of admin/operational training covering OIC monitoring, error management, and basic troubleshooting. Broad end-user training on integrated business processes is excluded. *(Ref: OIC-EXC-008)*

576. **Managed Services and Post-Hypercare Ongoing Support:** Ongoing management of OIC integrations after hypercare — including monitoring, incident management, error resolution, and integration maintenance — is excluded from a standard implementation contract. Post-hypercare managed services are a separate commercial engagement (AMS). *(Ref: OIC-EXC-009)*

577. **24x7 Support:** Round-the-clock support for OIC integrations — including evening, overnight, weekend, and public holiday support — is excluded from both the implementation scope and the standard hypercare scope. Extended support hours during hypercare are separately priced. *(Ref: OIC-EXC-010)*

578. **EDI and AS2 Integrations:** Electronic Data Interchange (EDI) integrations (EDIFACT, X12, or equivalent) and AS2-protocol-based integrations are excluded from standard OIC scope. EDI and AS2 require specialist integration expertise and tooling beyond standard Oracle OIC configuration. Where EDI is required, APPSolve assesses the requirement separately. *(Ref: OIC-EXC-011)*

579. **Custom Proprietary Protocols:** Integration with systems that communicate only via custom proprietary protocols — protocols not supported by any Oracle OIC adapter, and not exposed as REST, SOAP, SFTP, or database connections — is excluded from standard scope. Assessment is required before such integrations can be scoped. *(Ref: OIC-EXC-012)*

580. **Message Broker and ESB Replacement Programmes:** Replacing an existing enterprise service bus (ESB) or message broker platform (IBM MQ, MuleSoft, Tibco, WSO2, BizTalk, or equivalent) with Oracle OIC is an enterprise integration architecture programme, not a standard implementation scope item. APPSolve can deliver individual point-to-point integrations that replace specific broker-managed flows; a full ESB migration programme requires separate scoping and architecture planning. *(Ref: OIC-EXC-013)*

581. **Load Testing and Performance Benchmarking:** Executing structured load tests, measuring OIC throughput at projected peak volumes, or formally benchmarking Oracle OIC against performance SLAs is excluded from standard scope. Load testing is a separately scoped and priced activity. *(Ref: OIC-EXC-014)*

582. **Custom Monitoring Dashboards:** Building custom monitoring dashboards, integration operations portals, or observability tooling beyond Oracle OIC's native monitoring console is excluded. Third-party monitoring platform integration (Splunk, Dynatrace, Datadog, New Relic, etc.) is excluded. *(Ref: OIC-EXC-015)*

583. **New Module Implementations:** Implementing Oracle Fusion modules, Acumatica modules, or BeBanking integrations not in the client's current production system is excluded from AMS. New module implementations are project work under a separate implementation SOW. *(Ref: AMS-EXC-001)*

584. **New Integration Development:** Developing new OIC integrations or new BeBanking integrations not currently in the client's production environment is excluded from AMS. See OIC pack for integration development assumptions. *(Ref: AMS-EXC-002)*

585. **New Data Migration:** Loading new data sets into Oracle ERP or HCM post-go-live (for example, migrating a newly acquired company's supplier master or adding historical transactions from a merged entity) is excluded from AMS and requires a separately scoped data migration engagement. *(Ref: AMS-EXC-003)*

586. **New Report Development:** Developing new OTBI reports, FRS reports, BI Publisher reports, or Acumatica reports not in the client's existing report library is excluded from AMS. New report development is a project item. Adjusting existing in-scope reports within the report scope defined in the AMS agreement is a service request. *(Ref: AMS-EXC-004)*

587. **Regulatory Compliance Advice:** APPSolve does not provide tax, legal, audit, or regulatory compliance advice under AMS. System configuration to implement compliance requirements must be driven by a client-provided requirement specification approved by the client's tax or legal team. *(Ref: AMS-EXC-005)*

588. **End-User Training:** Delivering training to the client's users on existing Oracle or Acumatica functionality is excluded from standard AMS. Training can be contracted as a separately invoiced training engagement. APPSolve can provide quick reference cards and job aids for simple how-to queries within the monthly support hours. *(Ref: AMS-EXC-006)*

589. **Infrastructure Support:** Network, hardware, browser, VPN, printer, and IT infrastructure are the client's responsibility. Oracle SaaS infrastructure is Oracle's responsibility. APPSolve's AMS scope is the application configuration layer only. *(Ref: AMS-EXC-007)*

590. **Acumatica Customisation Development:** Developing new Acumatica customisations (low-code extensions, workflow customisations, custom web services, custom report designer reports) is excluded from standard Acumatica AMS. New customisation development requires a separately scoped development engagement. *(Ref: AMS-EXC-008)*

591. **Major Version Upgrades:** Oracle EBS major version upgrades, Acumatica major version upgrades, and BeBanking platform version migrations are excluded from standard AMS. These are project-level activities requiring planning, testing, and delivery effort far exceeding the AMS monthly support model. *(Ref: AMS-EXC-009)*

592. **Oracle Licensing and Subscription Management:** APPSolve does not manage the client's Oracle licences, Oracle Cloud subscription changes, or Oracle product roadmap planning. These are the client's commercial relationship with Oracle. APPSolve advises on licensing implications of configuration decisions; it does not purchase, renew, or modify Oracle licences on the client's behalf. *(Ref: AMS-EXC-010)*

593. **Business Intelligence and Analytics Development:** Developing Oracle Analytics Cloud (OAX/FAW) dashboards, reports, and data models is excluded from AMS. OAX development is separately scoped project work. *(Ref: AMS-EXC-011)*

594. **Disaster Recovery Testing:** Planning, executing, or certifying disaster recovery tests for the client's Oracle ERP or HCM environment is excluded from AMS. Oracle SaaS DR is Oracle's responsibility; on-premises DR is the client's IT team's responsibility. *(Ref: AMS-EXC-012)*

---

*ARM_IT045_ASSUMPTION_SCHEDULE_V1.md | WP17D-1 | 2026-06-24*  
*594 net assumptions | 6 packs | EBS AMS Full Stack | ARM IT045*  
*Generated by APPSolve Assembly Engine — Inline Text Mode v1.1*