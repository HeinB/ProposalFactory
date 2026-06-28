---
document_id: HCM-BASE-ASSUMPTIONS-V1
title: "Oracle Fusion HCM — Base Assumptions, Exclusions, and Customer Responsibilities"
version: "1.1"
status: "Approved"
created: "2026-06-15"
created_by: "WP11 — Commercial Assumptions Library"
last_updated: "2026-06-19"
last_updated_by: "WP16D — Oracle Journeys Post-Programme Enhancement"
approved_by: "BU Lead — Oracle Practice"
approved_date: "2026-06-15"
approved_for_reuse: true
lifecycle_status: APPROVED
category: "Commercial / Assumptions"
scope: "Oracle Fusion HCM Cloud — all core HCM implementations (Core HR, Absence, Benefits, Journeys, AI Skills, Payroll Interface, OTBI). Module-specific extensions loaded from Recruiting, Learning, Talent, Compensation, and OIC packs."
apply_with: "TENDER_ASSUMPTION_ASSEMBLY_RULES.md"
assumption_count: 115
bu_lead_decisions_applied:
  - "BU-WP11-001 CLOSED 2026-06-15: Parallel payroll run INCLUDED by default where payroll replacement is in scope — HCM-CUT-005 reversed; HCM-CUT-008 added"
  - "BU-WP11-002 CLOSED 2026-06-15: 1 Production + 1 Standard non-production environment — HCM-ENV-003 updated"
  - "BU-WP11-003 CLOSED 2026-06-15: 4-week hypercare is contractual default — HCM-HYP-001/002/003 updated"
  - "BU-WP11-004 CLOSED 2026-06-15: Job Management is default; Position Management excluded unless explicitly scoped — HCM-ORG-006 updated"
  - "BU-WP11-005 CLOSED 2026-06-15: 4 custom job roles included (Employee, Line Manager, Administrator, 1 additional) — HCM-SEC-002 updated"
  - "BU-WP11-006 CLOSED 2026-06-15: CRP1=Design Validation; CRP2=End-to-End Validation; standard is 2 CRP cycles — HCM-TST-003 updated"
  - "BU-WP11-007 CLOSED 2026-06-15: Default on-site = UAT support + Go-Live support only; all other activities remote — HCM-GEN-001/002 updated"
  - "BU-HCM-022 CLOSED 2026-06-19: Default Journey count = 3 (Onboarding + Internal Transfer/Promotion + Offboarding); additional Journeys separately scoped — HCM-JRN-001 added (WP16D)"
---

# Oracle Fusion HCM — Base Assumptions V1.0

**Scope:** This document governs all Oracle Fusion HCM Cloud implementations delivered by APPSolve. These assumptions form the contractual and commercial foundation of every HCM proposal, Statement of Work, and scope document. Module-specific assumption packs (Recruiting, Learning, Talent, Compensation, OIC) extend this base.

**Governance:** Governed under ASSUMPTION_GOVERNANCE.md. No assumption may be altered in a proposal without BU Lead approval and a registered change to this document or a project-level override recorded in the SOW.

**Usage:** Selected assumptions are assembled into proposals using TENDER_ASSUMPTION_ASSEMBLY_RULES.md. All HCM proposals include this base pack in full unless a specific item is explicitly excluded in the SOW.

---

## 1. Environment Assumptions

**HCM-ENV-001**  
This engagement covers Oracle Fusion HCM Cloud (SaaS). No on-premises Oracle HCM software is deployed or licensed under this proposal. All environments are Oracle-managed cloud tenants.

**HCM-ENV-002**  
The Oracle Cloud production environment will be provisioned by Oracle Corporation upon commercial agreement. Environment provisioning is Oracle's responsibility; APPSolve's implementation timeline commences from the date production and non-production environments are accessible to the project team.

**HCM-ENV-003** *(Updated — BU-WP11-002)*  
This proposal is scoped to one (1) Oracle Cloud production environment and one (1) standard Oracle non-production environment included in the client's SaaS subscription. No assumption is made about multiple non-production environments. If additional non-production environments are required (for example, dedicated UAT, training, or development tenants beyond the single standard tenant), these must be explicitly licensed by the client as part of the Oracle SaaS contract and are outside APPSolve's implementation scope.

**HCM-ENV-004**  
All Oracle Fusion HCM Cloud environments are subject to Oracle's standard quarterly update schedule. APPSolve will notify the client of upcoming updates and their potential impact during the implementation. The client acknowledges that Oracle quarterly updates may introduce changes to the user interface, delivered functionality, or configuration behaviour.

**HCM-ENV-005**  
Access to Oracle Cloud environments requires a supported, up-to-date web browser. APPSolve does not provide IT support for client-side browser configuration, VPN setup, or network proxy issues that prevent access to Oracle Cloud.

**HCM-ENV-006**  
The client is responsible for ensuring that all employees and project team members who require access to Oracle Cloud environments have the necessary internet connectivity. APPSolve is not responsible for performance degradation caused by the client's network infrastructure.

**HCM-ENV-007**  
Oracle's standard SaaS availability commitments (as defined in the Oracle SaaS Service Level Agreement) apply to all production environments. APPSolve is not responsible for Oracle platform downtime, maintenance windows, or service degradation.

**HCM-ENV-008**  
Any Oracle patch bundles, critical patch updates (CPUs), or mandatory platform changes applied by Oracle to the client's tenancy during the implementation are outside APPSolve's scope. APPSolve will assess the impact of such changes as part of the standard quarterly release management process; remediation effort is a change request.

---

## 2. Organisation Structure Assumptions

**HCM-ORG-001**  
The scope of Oracle HCM configuration is based on the number of legal entities, business units, locations, and legislative data groups confirmed during the Mobilize phase. Configuration effort estimates provided in this proposal are based on the entity and legislative scope documented at the time of submission. Scope changes require a formal Change Request.

**HCM-ORG-002**  
The client is responsible for confirming the final list of legal entities, business units, departments, locations, and job structures to be configured in Oracle HCM before the Scope and Design phase commences. Design decisions made on the basis of unconfirmed or subsequently revised organisational data may require re-work, which will be assessed as a Change Request.

**HCM-ORG-003**  
APPSolve will configure one Legislative Data Group (LDG) per country jurisdiction included in the agreed scope. Each additional LDG not identified in the scoping phase constitutes a scope change.

**HCM-ORG-004**  
APPSolve will apply Oracle's Modern Best Practice organisational design principles as the default configuration approach. Significant deviations from Oracle Modern Best Practice — including highly customised department hierarchies, non-standard grade structures, or atypical legal entity configurations — may require additional configuration effort and will be assessed as a Change Request.

**HCM-ORG-005**  
Organisational design decisions (including the structure of business units, department hierarchies, position vs job management approach, and grade ladder design) are the client's responsibility and must be finalised and signed off before configuration commences. APPSolve provides guidance and facilitation; final design authority rests with the client.

**HCM-ORG-006** *(Updated — BU-WP11-004)*  
APPSolve configures Oracle Job Management (job-based worker assignments) as the default. Oracle Position Management (hard or soft position control) is not included in base scope and is not the APPSolve standard. Where the client's HR operating model requires Position Management — for example, for headcount control, vacancy management, or compliance with position-based authorities — this must be explicitly identified and agreed in the Scope and Design phase and is priced and scoped as an addition. Position Management imposes significant additional configuration, testing, and data migration complexity.

**HCM-ORG-007**  
The client's HR organisation model (centralised vs decentralised HR) will be reflected in Oracle HCM through the configuration of Business Units, HR Organisations, and Security Profiles. The client is responsible for confirming which HR tasks are centralised (managed by a shared HR function) and which are distributed (managed by subsidiary or departmental HR teams) before security design commences.

**HCM-ORG-008**  
APPSolve will configure a single Worker Number assignment sequence per implementation unless multiple sequences are specifically agreed in scope. Multiple worker number sequences (for example, separate series by legal entity or employment type) are a scope addition requiring a Change Request.

---

## 3. Security Assumptions

**HCM-SEC-001**  
APPSolve will implement Oracle Fusion HCM role-based access control (RBAC) using Oracle's seeded duty roles and abstract roles as the baseline. Customisation of Oracle seeded duty roles is not included in base scope. All role requirements must be documented by the client before security configuration commences.

**HCM-SEC-002** *(Updated — BU-WP11-005)*  
APPSolve will configure a maximum of four (4) custom Oracle HCM job roles as part of base scope: (1) Employee self-service role, (2) Line Manager role, (3) HR Administrator role, and (4) one (1) additional custom role specific to the client's security requirements, as confirmed during the Scope and Design phase. Custom job roles beyond these four constitute a scope change requiring a Change Request and additional effort assessment.

**HCM-SEC-003**  
The client is responsible for defining and maintaining its user provisioning process (creation, modification, and deactivation of Oracle HCM user accounts). APPSolve configures the Oracle Identity Cloud Service (IDCS) / Oracle Cloud Infrastructure Identity and Access Management (OCI IAM) integration to the client's Identity Provider (IdP) if Single Sign-On (SSO) is in scope. SSO configuration is only included where explicitly stated in the SOW.

**HCM-SEC-004**  
Where Single Sign-On (SSO) is included in scope, the client is responsible for providing access to the Identity Provider (IdP) environment (Microsoft Azure AD, Okta, Active Directory Federation Services, or equivalent), the IdP technical contact, and all required integration metadata (SAML 2.0 metadata XML, entity IDs, callback URLs). APPSolve configures the Oracle-side of the SSO integration only.

**HCM-SEC-005**  
Data masking and data security in non-production environments is the client's responsibility. APPSolve recommends against loading production-grade personal data into non-production environments. The client is responsible for ensuring compliance with POPIA and applicable data protection legislation when populating test environments.

**HCM-SEC-006**  
Oracle Transparent Data Encryption (TDE) is included in the Oracle Fusion HCM Base Cloud Service licence and is enabled by default on Oracle-managed cloud environments. APPSolve does not configure TDE — it is an Oracle platform control. APPSolve will include reference to TDE in security documentation but is not responsible for its configuration or certification.

**HCM-SEC-007**  
The client is responsible for defining segregation of duties (SoD) requirements for Oracle HCM user roles. Where the client requires a formal SoD conflict matrix, this must be provided by the client or their internal audit function. APPSolve configures roles as directed but does not perform independent SoD audits.

**HCM-SEC-008**  
APPSolve configures Oracle HCM security for the agreed list of user populations (employees, managers, HR administrators, HR Business Partners, senior leadership, and system administrators) as confirmed in the Scope and Design phase. User populations not identified during design that require distinct security profiles constitute a scope change.

---

## 4. Workflow Assumptions

**HCM-WFL-001**  
APPSolve configures Oracle HCM approval workflows using Oracle's Business Process Management (BPM) framework. All workflow configurations in scope are based on Oracle's delivered approval patterns (management hierarchy, position hierarchy, or approval group) applied to the transactions agreed during the Scope and Design phase.

**HCM-WFL-002**  
The client is responsible for providing all approval hierarchies, approval rules, and notification requirements before workflow configuration commences. APPSolve will not design approval structures on behalf of the client. Approval structure changes after configuration has commenced are assessed as a Change Request.

**HCM-WFL-003**  
The number of distinct approval workflows included in base scope is limited to the transactions listed in the agreed Scope and Design documentation. Additional approval workflows not identified in scope constitute a Change Request.

**HCM-WFL-004**  
APPSolve configures email notifications using Oracle's standard notification framework. Custom-branded email templates (logo, HTML design, custom CSS) are not included in base scope. Standard Oracle email notification templates are the default delivery.

**HCM-WFL-005**  
Where Oracle Human Capital Management Cloud workflow routing depends on manager hierarchies, those hierarchies must exist and be accurate in Oracle HCM before workflow testing can be completed. The client is responsible for ensuring management structure data is loaded and validated before workflow UAT commences.

**HCM-WFL-006**  
Oracle HCM workflow delegation (out-of-office approval delegation) is a standard Oracle platform feature and is included in the delivered configuration. Configuration of permanent delegation hierarchies (where a specific role always delegates to another) requires a dedicated design decision from the client and may constitute a scope addition depending on complexity.

---

## 5. Data Migration Assumptions

**HCM-DAT-001**  
APPSolve provides Oracle FBDI-compliant data migration templates for all in-scope data entities. The client is responsible for extracting data from source systems, cleansing and normalising the data to the required format, and loading it into APPSolve's templates. APPSolve does not perform data extraction from client source systems unless explicitly included in the SOW as an additional service.

**HCM-DAT-002**  
Only active employee records are migrated to Oracle HCM as part of this engagement. Terminated employees, historical employment records, and contractor records not included in the active employee population are excluded from the data migration scope unless explicitly agreed.

**HCM-DAT-003**  
The client is responsible for the accuracy and completeness of all migrated data. APPSolve confirms that data has been loaded correctly into Oracle HCM and that the loaded records are visible and structurally valid. APPSolve does not take responsibility for the accuracy of source data, including personal details, employment dates, compensation records, or statutory information.

**HCM-DAT-004**  
APPSolve will conduct a maximum of three (3) data migration load cycles during the implementation (for example: Mock 1, Mock 2, and Production Go-Live). Additional load cycles beyond this number constitute a scope change. The production data load is the final load cycle.

**HCM-DAT-005**  
Historical learning completion records, historical performance review records, and historical payslip data are excluded from data migration scope unless explicitly agreed and scoped. Historical data take-on requires additional scoping, template design, and load effort, and is priced separately.

**HCM-DAT-006**  
The client is responsible for completing data reconciliation between the source system and Oracle HCM after each migration load cycle. APPSolve provides reconciliation controls and validation reports; the client's HR data team performs the reconciliation sign-off.

**HCM-DAT-007**  
All data provided by the client for migration must be in English or in the primary language of the Oracle HCM implementation. Where multi-language support is required, translated data values must be provided by the client in the required format before the migration load.

**HCM-DAT-008**  
The client accepts that data migration activities introduce risk during the cutover period. The client is responsible for maintaining a data freeze on the source system during the final production migration window to prevent data divergence. The client is responsible for defining and enforcing the data freeze period.

**HCM-DAT-009**  
Contractor, agency worker, and contingent worker records are excluded from the default Core HR data migration scope. If these worker types require Oracle HCM records (for example, to support self-service, absence, or workforce directory access), this must be agreed during the Scope and Design phase and scoped as an addition.

---

## 6. Reporting Assumptions

**HCM-RPT-001**  
APPSolve configures standard Oracle Transactional Business Intelligence (OTBI) reports and dashboards as part of this implementation. OTBI is the default reporting tool in Oracle Fusion HCM and is included in the HCM Base Cloud Service licence.

**HCM-RPT-002**  
The number of custom OTBI reports included in base scope is limited to the count agreed during the Scope and Design phase. Custom OTBI reports beyond the agreed count are a scope change requiring a Change Request.

**HCM-RPT-003**  
Oracle Analytics for Cloud (OAC/OAX) is a separately licensed Oracle product. Any OAC/OAX analytics requirements are outside the scope of this proposal unless explicitly included in the Bill of Materials and SOW.

**HCM-RPT-004**  
Oracle BI Publisher is available within Oracle Fusion HCM for structured document generation (payslips, offer letters, notice templates). APPSolve includes BI Publisher configuration for documents confirmed in the Scope and Design phase. Additional BI Publisher templates beyond those agreed in scope constitute a Change Request.

**HCM-RPT-005**  
All reports delivered by APPSolve are designed against the data model and configuration in place at the time of go-live. Changes to Oracle HCM configuration after report delivery that affect report output require report remediation, which is assessed as a Change Request.

**HCM-RPT-006**  
The client is responsible for the business requirements for all reports, including the definition of required fields, filters, grouping, sorting, and calculation logic. APPSolve translates agreed requirements into OTBI configuration but does not define reporting requirements on the client's behalf.

---

## 7. Testing Assumptions

**HCM-TST-001**  
User Acceptance Testing (UAT) is led and owned by the client. APPSolve facilitates UAT by providing a structured test execution environment, issue logging process, and test support resources during the agreed UAT period. APPSolve does not sign off UAT on behalf of the client.

**HCM-TST-002**  
The client is responsible for preparing UAT test scripts and scenarios aligned to their business processes. APPSolve provides configuration test scripts (CRP scripts) for the technical validation of Oracle HCM configuration; these are distinct from business UAT test scripts, which the client owns.

**HCM-TST-003** *(Updated — BU-WP11-006)*  
The implementation plan includes two Conference Room Pilot (CRP) cycles and one UAT cycle as the APPSolve standard: **CRP1 (Design Validation)** — first rapid build; facilitated demonstration; structured design feedback captured and resolved before CRP2; **CRP2 (End-to-End Validation)** — complete end-to-end scenario test of configured Oracle HCM; final configuration sign-off before UAT entry. Additional CRP cycles beyond CRP1 and CRP2 are not included in standard scope and require a Change Request. A second UAT cycle also constitutes a scope change.

**HCM-TST-004**  
The client is responsible for providing a sufficient number of business users for UAT participation. Delays in UAT caused by insufficient client user availability or late test script preparation are the client's responsibility and may impact the project timeline.

**HCM-TST-005**  
APPSolve will track and manage defects identified during CRP and UAT using the agreed defect management tool (for example, Excel tracker, Jira, ServiceNow, or equivalent — to be agreed during Mobilize). Configuration defects (errors in APPSolve's configuration of Oracle HCM) are remediated by APPSolve at no additional cost. Defects attributable to incorrect or incomplete client business requirements, client data quality issues, or Oracle platform behaviour are not APPSolve's responsibility to remediate within base scope.

**HCM-TST-006**  
System Integration Testing (SIT) for any in-scope OIC integrations requires test environments for all connected third-party systems to be available, accessible, and stable before SIT commences. Delays caused by third-party system unavailability or instability are the client's responsibility.

**HCM-TST-007**  
Performance and load testing of the Oracle HCM Cloud environment is Oracle's responsibility as the SaaS provider. APPSolve does not conduct infrastructure performance testing. Oracle's standard SaaS platform is expected to support the contracted user volumes.

**HCM-TST-008**  
APPSolve will conduct regression testing after each Oracle quarterly update during the active implementation period. Regression testing after go-live is included in the AMS scope, not the implementation scope. One UAT-to-go-live quarterly update cycle is included in base scope; additional quarterly cycles caused by delayed go-live are assessed as a Change Request.

---

## 8. Training Assumptions

**HCM-TRN-001**  
APPSolve delivers a train-the-trainer (TTT) training programme as the default training approach. The client is responsible for cascading knowledge to end users. APPSolve is not responsible for end-user training beyond the train-the-trainer group unless explicitly included in the SOW.

**HCM-TRN-002**  
All APPSolve training is delivered in English. Translation of training materials into other languages is the client's responsibility and is not included in base scope.

**HCM-TRN-003**  
APPSolve delivers training using APPSolve-prepared quick reference guides, process walkthrough documentation, and live demonstration in the configured Oracle HCM environment. High-fidelity interactive eLearning modules, narrated video training, or custom LMS content is not included in base scope.

**HCM-TRN-004**  
The client is responsible for ensuring that designated train-the-trainer participants attend all scheduled training sessions. Rescheduling or repeating training sessions caused by client unavailability may constitute a Change Request.

**HCM-TRN-005**  
Oracle University training courses (Oracle-branded instructor-led or virtual training) are not included in APPSolve's proposal. Oracle University training is available separately through Oracle and is the client's direct commercial relationship with Oracle Corporation.

**HCM-TRN-006**  
APPSolve recommends that Oracle HCM system administrators attend relevant Oracle Cloud Learning Subscriptions (formerly Oracle University) courses before go-live to ensure sustainable system administration capability. This is a client action and is not included in APPSolve's scope.

---

## 9. Cutover Assumptions

**HCM-CUT-001**  
The production go-live date will be confirmed during the Mobilize phase and agreed in the project plan. APPSolve will build a detailed cutover plan including a cutover checklist, task assignments, and contingency procedures. The cutover plan must be reviewed and approved by the client before the production migration commences.

**HCM-CUT-002**  
The production data migration window is assumed to be a weekend (Friday evening to Sunday evening, local time). Business-day production migrations that impact the client's operational HR processes during working hours require specific agreement and risk acceptance by the client.

**HCM-CUT-003**  
A data freeze on the client's source HR system(s) is required from the start of the production data migration window. The client is responsible for communicating and enforcing the data freeze with all subsidiaries, HR teams, and system administrators. Any transactions processed in the source system during the data freeze period will not be reflected in Oracle HCM without manual intervention after go-live.

**HCM-CUT-004**  
APPSolve will define a go/no-go decision point in the cutover plan. If the production migration cannot be completed within the agreed cutover window due to data quality failures, environment issues, or integration failures, APPSolve and the client will jointly assess whether to continue or roll back. The client retains the final go/no-go decision authority.

**HCM-CUT-005** *(Updated — BU-WP11-001)*  
Where Oracle HCM is replacing an existing payroll-connected HR system, a parallel payroll run period is included in base scope as a standard risk-mitigation control. The parallel run enables the client to reconcile payroll outputs from the legacy system and Oracle HCM concurrently before the legacy system is decommissioned. The duration of the parallel run, reconciliation approach, and parallel run exit criteria are agreed with the client during the Scope and Design phase and are documented in the cutover plan.

**HCM-CUT-008** *(New — BU-WP11-001)*  
The following conditions apply to the parallel payroll run (HCM-CUT-005): (a) the parallel run applies to payroll interface outputs from Oracle HCM to the third-party payroll provider only; (b) Oracle HCM is not used as a payroll calculation engine — payroll calculations remain the payroll provider's responsibility throughout; (c) the client's payroll team owns the reconciliation between parallel run payroll outputs; APPSolve provides the Oracle HCM configuration and interface support; (d) the parallel run is not applicable where Oracle HCM is not replacing a payroll-connected system.

**HCM-CUT-006**  
Legacy system decommissioning, data archival, or shutdown of the client's previous HR system(s) after go-live is the client's responsibility. APPSolve does not plan or execute legacy system decommissioning.

**HCM-CUT-007**  
Go-live readiness sign-off is required from both APPSolve and the client before the production migration commences. APPSolve will not proceed with production cutover without the client's written (or email) confirmation of readiness.

---

## 10. Hypercare Assumptions

**HCM-HYP-001** *(Updated — BU-WP11-003)*  
A four (4) week hypercare period is the contractual default and commences immediately after the production go-live date. Hypercare is not a guideline — it is a standard delivery obligation. During hypercare, a senior APPSolve team is available during South African business hours (08:00–17:00 SAST, Monday–Friday) to respond to and resolve production defects and stabilisation issues. Hypercare scope is limited to defect resolution and system stabilisation. Enhancements, new functionality, new scope, and change requests are explicitly excluded from hypercare. Hypercare resource allocation is defined in the SOW.

**HCM-HYP-002** *(Updated — BU-WP11-003)*  
During hypercare, APPSolve's response to production issues operates on the following priority classification, applicable during standard South African business hours (08:00–17:00 SAST, Monday–Friday):
- **P1 (Critical):** System unavailable or payroll/data integrity impacted — 2-hour response
- **P2 (High):** Major function unavailable, no workaround — 4-hour response
- **P3 (Medium):** Non-critical issue, workaround available — next business day response

These SLAs are contractual during hypercare. Extended-hours or weekend support during hypercare requires explicit agreement in the SOW and is priced as an additional service.

**HCM-HYP-003** *(Updated — BU-WP11-003)*  
Hypercare support covers defect resolution and stabilisation of functionality that was in the agreed implementation scope. The following are explicitly excluded from hypercare support and will not be resolved under hypercare SLAs: (a) enhancements — changes to delivered functionality beyond what was agreed; (b) new scope requests — functionality not in the original SOW; (c) Change Requests — items identified as out-of-scope during the implementation; (d) training and user adoption support beyond what is documented in the hypercare plan. All excluded items are assessed and quoted separately as Change Requests.

**HCM-HYP-004**  
The transition from hypercare to the client's steady-state support model (internal IT support or APPSolve AMS) is governed by a formal hypercare exit review. APPSolve will not transition out of hypercare without a documented handover and the client's acceptance.

**HCM-HYP-005**  
If the client requires hypercare beyond the minimum agreed period due to outstanding issues, extended hypercare is available as an additional service at APPSolve's standard rate card. Extended hypercare must be agreed in writing before the scheduled hypercare end date.

---

## 11. Change Management Assumptions

**HCM-CHG-001**  
Organisational Change Management (OCM) — including communication planning, stakeholder engagement, resistance management, and change readiness assessments — is not included in base scope. APPSolve strongly recommends the client appoints a dedicated internal Change Manager for any Oracle HCM implementation impacting more than 200 employees.

**HCM-CHG-002**  
APPSolve provides functional and technical support for the Oracle HCM implementation. Developing and executing a change management strategy, communication cascade, or employee engagement programme for the HCM go-live is the client's responsibility.

**HCM-CHG-003**  
Where the client elects not to appoint an internal Change Manager, APPSolve accepts no responsibility for user adoption challenges, resistance to the new system, or the business impact of low system engagement after go-live.

**HCM-CHG-004**  
APPSolve can provide optional Change Management consulting as a separately scoped and priced engagement. This must be explicitly included in the SOW if required.

---

## 12. Third-Party System Assumptions

**HCM-3PT-001**  
All third-party systems that require integration with Oracle HCM (including payroll systems, time and attendance systems, background check providers, job board platforms, and identity providers) must have documented, available, and accessible APIs or standard file exchange interfaces. Where a third-party vendor does not provide standard integration capability, APPSolve will assess the feasibility and cost of a custom integration during the Scope and Design phase.

**HCM-3PT-002**  
The client is responsible for all commercial and contractual engagement with third-party vendors whose systems integrate with Oracle HCM. This includes obtaining API credentials, ensuring integration licensing is in place, arranging access to vendor technical support, and negotiating vendor-side integration effort. APPSolve is not responsible for third-party vendor delays, cost overruns, or technical limitations.

**HCM-3PT-003**  
Third-party vendors must provide stable, accessible non-production (test) environments for all OIC integration testing activities. Delays caused by a third-party vendor's inability to provide a test environment, or instability of the vendor test environment, are outside APPSolve's control and may impact the project timeline.

**HCM-3PT-004**  
The number of third-party system integrations included in scope is as documented in the SOW. Each integration not listed in the SOW constitutes a scope change and requires a formal Change Request and impact assessment before APPSolve proceeds.

**HCM-3PT-005**  
Where a third-party system's API or file format changes after integration design has been completed, any remediation of the affected Oracle OIC integration is a Change Request.

**HCM-3PT-006**  
APPSolve is an Oracle integration partner. APPSolve is not a payroll service provider, payroll bureau, or payroll administrator. Where APPSolve configures a payroll interface or OIC payroll integration, the payroll calculation, tax computation, statutory filing, and payroll compliance remain the exclusive responsibility of the client and their designated payroll provider.

---

## 13. Customer Responsibilities

**HCM-CUS-001**  
The client appoints a dedicated Project Sponsor with sufficient authority to make scope decisions, approve Change Requests, escalate issues to executive level, and provide go/no-go decisions at key project milestones. The absence of an empowered Project Sponsor is a significant project risk and is the client's responsibility to address.

**HCM-CUS-002**  
The client appoints a dedicated HR Project Lead (or equivalent) who participates in the project team on a full-time or near-full-time basis throughout the implementation. The HR Project Lead is responsible for: facilitating access to subject matter experts; coordinating internal HR workshops; reviewing and approving design documents; leading UAT; and ensuring timely decisions on design questions raised by APPSolve.

**HCM-CUS-003**  
The client makes available appropriate functional subject matter experts (HR administrators, payroll administrators, IT representatives, and departmental HR leads) for workshops, design reviews, testing, and training activities as required by the project plan. Unavailability of required client resources at agreed project milestones may impact the project timeline.

**HCM-CUS-004**  
The client reviews and approves all APPSolve design documents, configuration workbooks, and test results within the agreed review turnaround period (standard: 5 business days unless otherwise agreed in the SOW). Delays in client review and approval that impact project milestones are the client's responsibility.

**HCM-CUS-005**  
The client performs all data extraction, cleansing, preparation, and loading of migration data into APPSolve-provided templates. The client assigns appropriate data stewards for each data entity (employee records, jobs and positions, grade structures, absence entitlements) to own data quality for each migration cycle.

**HCM-CUS-006**  
The client provides all business rules, policy documents, HR procedures, and process documentation required for Oracle HCM configuration. APPSolve configures Oracle HCM to the client's defined business rules. If business rules are undefined, incomplete, or contradictory, APPSolve will escalate to the client for resolution. Design decisions delayed by incomplete client business rules may impact the project timeline.

**HCM-CUS-007**  
The client is responsible for obtaining all internal approvals required for Oracle HCM go-live, including approvals from executive sponsors, IT governance bodies, POPIA/data protection officers, works councils (where applicable), and any other internal stakeholder whose approval is a prerequisite for production deployment.

**HCM-CUS-008**  
The client is responsible for all internal communication to employees, managers, and HR teams regarding the Oracle HCM implementation — including go-live announcements, system access instructions, training schedules, and post-go-live support contact details.

**HCM-CUS-009**  
The client ensures that all required Oracle user licences are procured and active before the implementation commences. APPSolve is not responsible for Oracle licence procurement, licence compliance, or licence overruns caused by the client deploying Oracle HCM to a larger user population than was contracted.

**HCM-CUS-010**  
Where after-hours access to the client's premises is required for implementation activities (for example, weekend cutover, hypercare on-call), the client provides such access to the relevant APPSolve consultants within agreed timelines.

---

## 14. General Assumptions

**HCM-GEN-001** *(Updated — BU-WP11-007)*  
This engagement is delivered on a remote-first basis (videoconference, Oracle Cloud access, screen-share, and collaboration tools). The default on-site activities included in base scope are: (1) **UAT support** — APPSolve facilitates on-site UAT sessions at the client's premises; (2) **Go-Live support** — APPSolve senior team is on-site during the production cutover and day-one go-live. All other project activities — including project kick-off, Scope and Design workshops, CRP1 and CRP2 demonstrations — are conducted remotely unless the client specifically requests on-site facilitation and this is agreed in the SOW. Additional on-site days beyond those in the SOW are chargeable at APPSolve's standard rate card.

**HCM-GEN-002** *(Updated — BU-WP11-007)*  
Travel, accommodation, and subsistence costs for APPSolve consultants attending on-site (UAT support and Go-Live support, and any additional on-site days agreed in the SOW) are for the client's account, in addition to consulting fees. APPSolve will agree a travel and expense approval process with the client before incurring any travel-related cost.

**HCM-GEN-003**  
All project communication, documentation, and deliverables are in English. Where the client requires documentation in another language, translation is the client's responsibility.

**HCM-GEN-004**  
APPSolve's standard implementation methodology is based on Oracle Unified Method (OUM) and the Oracle Customer Success Navigator. The six phases of the methodology are: Mobilize → Scope and Design → Prototype → Validate → Deploy → Evolve. The client accepts this methodology as the basis of the engagement.

**HCM-GEN-005**  
All APPSolve resources assigned to this engagement are confirmed at the time of project initiation. APPSolve will not substitute named resources without prior written notification to the client. Where substitution is unavoidable (for example, resignation, medical), APPSolve will provide a resource of equivalent or greater seniority and experience.

**HCM-GEN-006**  
This proposal covers Oracle Fusion HCM Cloud implementation only. Oracle subscription, licence, and hosting fees are payable directly by the client to Oracle Corporation and are not included in APPSolve's commercial proposal.

**HCM-GEN-007**  
The implementation timeline in this proposal is based on the scope documented at the time of submission and assumes timely client decision-making, resource availability, and data readiness. Material changes to any of these factors may require timeline revision, assessed as a formal Change Request.

**HCM-GEN-008**  
APPSolve will configure Oracle HCM to comply with applicable South African legislation (including the Basic Conditions of Employment Act, the Employment Equity Act, the POPIA, and relevant LRA requirements) as they apply to Oracle HCM configuration at the time of implementation. Changes to legislation after the design sign-off date that require configuration changes are assessed as a Change Request.

**HCM-GEN-009**  
Where this engagement spans multiple calendar years, APPSolve's standard rate card is subject to an annual escalation in line with the South African CPI, applied on 1 March each year, unless fixed rates are explicitly agreed in the SOW.

**HCM-GEN-010**  
APPSolve's maximum liability in relation to this engagement is limited to the total fees paid by the client to APPSolve under the relevant Statement of Work, as governed by APPSolve's standard Master Services Agreement.

**HCM-JRN-001** *(BU-HCM-022 — WP16D 2026-06-19)*  
Oracle Journeys are configured based on the business processes identified during design workshops. Unless otherwise stated in the Statement of Work, the standard Oracle HCM implementation includes configuration of up to three (3) Oracle Journeys using Oracle-delivered functionality and standard task types. The standard implementation assumes one onboarding Journey, one internal movement Journey (transfer or promotion), and one offboarding Journey. Additional Journeys, complex conditional logic, custom integrations, external system orchestration, advanced approvals, bespoke user experiences, or Journey redesign activities are separately scoped.

---

## 15. Explicit Exclusions

**HCM-EXC-001**  
**Oracle Fusion Global Payroll (native):** APPSolve does not implement Oracle Fusion Global Payroll as a payroll calculation engine in South Africa. APPSolve implements the Oracle HCM Payroll Interface to connect Oracle HCM to a third-party payroll provider via OIC. Native Oracle Fusion payroll processing, statutory payroll filing (PAYE, UIF, SDL), and payroll legislative updates are excluded from this engagement.

**HCM-EXC-002**  
**Organisational Change Management (OCM):** Formal change management planning, stakeholder mapping, communication cascades, resistance management, and change readiness programmes are excluded from base scope. OCM is available as a separately priced optional service.

**HCM-EXC-003**  
**Custom Software Development:** Bespoke code development, Oracle Application Framework (OAF) page personalisation, Oracle Fusion Application Composer extensions beyond standard low-code configuration, and Oracle VBCS application development are excluded from base scope. Any requirement for custom code is assessed and priced separately.

**HCM-EXC-004**  
**Hardware, Infrastructure, and Networking:** Oracle Fusion HCM Cloud is a SaaS solution hosted and managed by Oracle. No hardware procurement, server deployment, network infrastructure design, or data centre services are included in this engagement.

**HCM-EXC-005**  
**Oracle EPM (Enterprise Performance Management):** Oracle Fusion Workforce Planning, Oracle Planning and Budgeting Cloud, and Oracle Narrative Reporting are EPM products and are excluded from this proposal. Workforce budgeting and headcount planning beyond Oracle HCM's included analytics are not in scope.

**HCM-EXC-006**  
**Oracle University Training:** Oracle-branded training courses and Oracle Learning Subscriptions are not included in this proposal. Oracle University training is available directly from Oracle Corporation and is the client's direct commercial relationship.

**HCM-EXC-007**  
**Legacy System Support:** Continued support, maintenance, or enhancement of the client's legacy HR system(s) during or after the Oracle HCM implementation is excluded from this engagement.

**HCM-EXC-008**  
**Data Archival and Legacy System Decommissioning:** Archiving, purging, or decommissioning of data in the client's legacy HR system after Oracle HCM go-live is excluded from this engagement.

**HCM-EXC-009**  
**Third-Party Vendor Integration Effort:** APPSolve designs and configures the Oracle OIC side of agreed integrations. Third-party vendor-side integration development, vendor API changes, vendor project management, and vendor testing resources are excluded from this engagement.

**HCM-EXC-010**  
**POPIA Compliance Programme:** While APPSolve configures Oracle HCM in a manner consistent with POPIA principles (data minimisation, consent management where supported by Oracle), APPSolve does not provide legal advice on POPIA compliance, conduct POPIA risk assessments, or act as the client's Information Officer. The client retains sole responsibility for POPIA compliance.

**HCM-EXC-011**  
**End-User Helpdesk and Level 1 Support:** First-line user support for Oracle HCM end users (password resets, navigation assistance, basic user queries) is excluded from the implementation scope. The client's IT helpdesk is responsible for Level 1 support. APPSolve provides Level 2 and Level 3 configuration and functional support through the AMS service.

**HCM-EXC-012**  
**Report Development for Statutory Regulatory Submissions:** APPSolve does not prepare, validate, or submit statutory reports on behalf of the client (including EEA2/EEA4 Employment Equity reports, Workplace Skills Plans (WSP), Annual Training Reports (ATR), or PAYE/UIF/SDL reconciliations). APPSolve configures Oracle HCM to hold the data required for these reports; the extraction, validation, and submission of statutory reports to the relevant authority is the client's responsibility.

---

## BU Lead Decisions — Applied

All eight BU Lead decisions have been applied. No open items remain. This document is Approved.

| Decision ID | Decision | Assumptions Affected | Applied |
|---|---|---|---|
| BU-WP11-001 | Parallel payroll run INCLUDED by default where payroll replacement is in scope | HCM-CUT-005 reversed (Exclusion → Assumption); HCM-CUT-008 added | 2026-06-15 |
| BU-WP11-002 | 1 production + 1 standard non-production environment; no implication of multiple non-production tenants | HCM-ENV-003 updated | 2026-06-15 |
| BU-WP11-003 | 4-week hypercare is contractual default (not guideline); business hours; defect/stabilisation only; enhancements excluded | HCM-HYP-001/002/003 updated | 2026-06-15 |
| BU-WP11-004 | Job Management is APPSolve default; Position Management excluded unless explicitly scoped | HCM-ORG-006 updated | 2026-06-15 |
| BU-WP11-005 | 4 custom job roles included: Employee, Line Manager, HR Administrator, 1 additional | HCM-SEC-002 updated | 2026-06-15 |
| BU-WP11-006 | CRP1=Design Validation; CRP2=End-to-End Validation; 2 CRP cycles is APPSolve standard | HCM-TST-003 updated | 2026-06-15 |
| BU-WP11-007 | Default on-site = UAT support + Go-Live support only; all other activities remote-first | HCM-GEN-001/002 updated | 2026-06-15 |
| BU-HCM-022 | Default Journey count = 3 (Onboarding + Internal Transfer/Promotion + Offboarding); additional Journeys separately scoped | HCM-JRN-001 added | 2026-06-19 (WP16D) |

---

*HCM_BASE_ASSUMPTIONS_V1.1 | WP11 — Commercial Assumptions Library | 2026-06-15 | **APPROVED** — BU Lead Oracle Practice | WP16D post-programme enhancement: BU-HCM-022 applied 2026-06-19*  
*115 assumptions / exclusions / responsibilities across 15 sections*  
*Governed under: 08_Commercial/ASSUMPTION_GOVERNANCE.md*  
*Assembly rules: 08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md*
