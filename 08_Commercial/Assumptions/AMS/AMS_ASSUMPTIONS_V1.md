---
document_id: AMS-ASSUMPTIONS-V1
title: "APPSolve Application Managed Services — Assumptions, Exclusions, Dependencies, Constraints and Customer Responsibilities"
version: "1.0"
status: "Approved"
created: "2026-06-15"
created_by: "WP11E — AMS / Managed Services Assumptions Pack"
approved_by: "BU Lead — Oracle Practice (Cross-BU)"
approved_date: "2026-06-15"
approved_for_reuse: true
lifecycle_status: APPROVED
category: "Commercial / Assumptions"
scope: "All APPSolve Application Managed Services (AMS) agreements covering Oracle Fusion HCM, Oracle Fusion ERP, Oracle EBS, Oracle Integration Cloud (OIC), Acumatica ERP, and BeBanking H2H post-implementation support. This pack governs the commercial assumptions for all AMS proposals, Managed Services SOWs, and AMS renewal agreements."
apply_with: "TENDER_ASSUMPTION_ASSEMBLY_RULES.md"
parent_pack: "None — AMS is a Cross-BU standalone pack. Load alongside the relevant implementation pack(s) for the supported applications."
applies_to: "Oracle BU, Acumatica BU, BeBanking BU, Cross-BU"
assumption_count: 84
bu_lead_decisions_applied:
  - "BU-AMS-001 CLOSED: Standard response targets — P1: 1 hour; P2: 4 business hours; P3: 1 business day; P4: 3 business days. Uniform across Oracle, Acumatica, BeBanking. Response time is not resolution time. Applied to AMS-SLA-001, AMS-PRI-001."
  - "BU-AMS-002 CLOSED: Standard support hours confirmed as 08:00–17:00 SAST, Mon–Fri, excluding South African public holidays. Extended hours, weekend support, and 24x7 require separate commercial agreement. Applied to AMS-HRS-001."
  - "BU-AMS-003 CLOSED: No default included support hours. Support allocation governed by specific AMS agreement. Retainer-based and allocated-hour models both permitted. Applied to AMS-HRS-003."
  - "BU-AMS-004 CLOSED: CR threshold set at 2 hours. Changes estimated above 2 hours require a formal CR. APPSolve may absorb items at its discretion below threshold; no entitlement created by previous discretionary work. Applied to AMS-CR-001."
  - "BU-AMS-005 CLOSED: Oracle quarterly release assessment included in base AMS. Regression testing, UAT execution, and business process validation excluded unless specifically contracted. Customer responsible for business testing. Applied to AMS-REL-001."
  - "BU-AMS-006 CLOSED: Named consultant allocation not included. Support delivered by APPSolve support team on best-effort resource allocation basis. Dedicated named consultants require separate commercial agreement. Applied to AMS-SLA-005."
  - "BU-AMS-007 CLOSED: Proactive monitoring excluded unless specifically contracted. Standard AMS includes mailbox monitoring during support hours only. 24x7 monitoring, automated alerting, infrastructure monitoring, and application monitoring require separate scope. Applied to AMS-MON-001."
---

# APPSolve Application Managed Services — Assumptions V1.0

**Scope:** This document governs APPSolve's Application Managed Services (AMS) agreements. AMS provides post-implementation application support covering Level 2 and Level 3 application and technical support for Oracle Fusion HCM, Oracle Fusion ERP, Oracle EBS, Oracle Integration Cloud, Acumatica ERP, and BeBanking H2H. AMS does not include project delivery, new implementation, or new module deployment.

**What AMS is:** AMS is a post-go-live support retainer. The client's system is live and stable. APPSolve provides ongoing configuration support, break/fix resolution, user support escalation handling, Oracle release advisory, and periodic minor configuration changes within the contracted scope.

**What AMS is not:** AMS is not a project. It does not include new module implementations, new integration development, new data migrations, major functional redesigns, or new report development beyond the contracted scope. These are separately scoped and separately priced as project work.

**Governance:** Status: Approved — 2026-06-15. All BU-AMS-XXX items closed. Approved for use in external AMS proposals and SOWs. Governed under: 08_Commercial/ASSUMPTION_GOVERNANCE.md.

---

## 85. Support Scope

**AMS-SCP-001**  
APPSolve AMS scope is limited to the applications and modules explicitly listed in the AMS agreement. Support for an application or module not named in the AMS agreement is excluded. Adding a new application to an existing AMS agreement requires a scope change to the AMS contract.

**AMS-SCP-002**  
APPSolve provides Level 2 and Level 3 application and technical support only. Level 1 support — the first point of contact for users with questions or requests, service desk ticket creation, user communication, and first-line triage — remains the client's responsibility unless Level 1 support is explicitly contracted as an add-on service.

**AMS-SCP-003**  
Level 2 support covers: functional configuration questions and configuration adjustments within the existing system design; application error investigation and diagnosis; user access and security role assignment support where this has been delegated to APPSolve; data correction assistance for system-originated data issues; workflow configuration adjustments (approval routing changes that do not constitute structural redesign); and report adjustments within the existing report framework.

**AMS-SCP-004**  
Level 3 support covers: technical investigation of Oracle platform issues, Oracle SR (Service Request) management with Oracle Support, integration error investigation (OIC / BeBanking H2H), performance issue diagnosis, and complex configuration issues requiring senior Oracle or Acumatica certified expertise.

**AMS-SCP-005**  
Oracle Application Managed Services support is scoped to the Oracle applications configured and delivered during the implementation. APPSolve does not support Oracle applications not configured by APPSolve, or applications configured by other parties, without a separate scope assessment and onboarding engagement.

**AMS-SCP-006**  
BeBanking AMS support covers: OIC integration error investigation for BeBanking H2H flows; file format and payment file query handling; BeBanking connectivity issue escalation to BeBanking; and bank statement import troubleshooting. BeBanking AMS is only available where Carin Webb (sole BeBanking OIC resource) is available — see CONSULTANT_SKILL_MATRIX.md SPOF note.

**AMS-SCP-007**  
Acumatica AMS support covers: Acumatica configuration adjustments within the agreed application scope; Acumatica workflow and customisation support within the implemented framework; data correction support; Acumatica release advisory; and Acumatica user access management where contracted.

---

## 86. Support Hours

**AMS-HRS-001**  
Standard AMS support is provided during business hours: 08:00–17:00 SAST, Monday to Friday, excluding South African public holidays. Business-hours support is the default for all AMS agreements. Extended hours support (weekday evenings, Saturday, Sunday) and 24/7 support require a separate commercial agreement and are not included in the standard AMS agreement.

**AMS-HRS-002**  
AMS support is delivered remotely unless on-site support is explicitly contracted. On-site support incurs a separate on-site day rate plus travel expenses as applicable. Remote-first support is the APPSolve standard for all AMS engagements.

**AMS-HRS-003**  
There is no default monthly support hours allocation. The support model and allocation are governed by the specific AMS agreement. APPSolve offers both retainer-based engagements (fixed monthly fee for a defined support scope) and allocated-hour models (monthly hour bucket at a contracted rate). The model, allocation, and overage terms are defined in each AMS agreement. Where an allocated-hour model applies, hours not used in a given month do not roll over to the following month.

**AMS-HRS-004**  
Hours consumed against the monthly allocation are tracked and reported. APPSolve provides a monthly support activity report showing: incidents resolved; service requests completed; hours consumed; hours remaining; change requests raised; and open items carried to the following month.

**AMS-HRS-005**  
Where the monthly hours allocation is exhausted before month-end, APPSolve notifies the client immediately. Additional hours may be approved by the client at the applicable AMS hourly rate. APPSolve does not continue work beyond the monthly allocation without written client approval.

**AMS-HRS-006**  
Public holiday support: APPSolve does not provide AMS support on South African public holidays under the standard business hours agreement. Where the client requires support on public holidays, this is arranged separately and billed at the applicable out-of-hours rate.

---

## 87. Support Channels

**AMS-CHN-001**  
All AMS support requests must be logged via APPSolve's designated support channel — either the APPSolve support portal, a designated support email address, or the agreed ticketing mechanism specified in the AMS agreement. Requests made directly to individual consultants via WhatsApp, personal email, or phone are acknowledged but must be formally logged to be covered under the AMS agreement.

**AMS-CHN-002**  
Telephone support is available for P1 (Critical) incidents only — the client may call the APPSolve AMS hotline to report a P1 after logging the ticket. For P2, P3, and P4 requests, ticket-first is the required process; telephone follow-up is at APPSolve's discretion.

**AMS-CHN-003**  
A designated AMS contact at APPSolve (the AMS Account Manager or AMS Team Lead) is the client's primary escalation point for service delivery concerns, SLA disputes, and change request approvals. The AMS contact is named in the AMS agreement. Changes to the AMS contact are communicated to the client in writing.

**AMS-CHN-004**  
The client designates a primary AMS contact (typically the internal IT or ERP team lead) who is authorised to log support requests, approve change requests, and receive monthly reports. APPSolve only takes direction from the designated client AMS contact. Requests from other client employees may be acknowledged but require authorisation from the designated contact before work commences.

---

## 88. Incident Management

**AMS-INC-001**  
An incident is an unplanned interruption or degradation of a supported application. Incidents are distinguished from service requests (planned configuration changes) and change requests (enhancements or new scope). The incident classification determines the priority level and SLA response target.

**AMS-INC-002**  
Incidents are classified by the client at the time of logging. APPSolve may reclassify an incident based on its assessment of business impact. Where APPSolve downgrades an incident from P1 to P2, the client is notified with the reason. Where the client disputes the reclassification, the AMS Account Manager resolves the classification within four (4) business hours.

**AMS-INC-003**  
Incident ownership: APPSolve owns the investigation and resolution of application configuration and integration defects. Incidents caused by client data entry errors, client business process errors, client IT infrastructure failures (network, hardware, browser), or Oracle SaaS platform outages are not APPSolve defects. APPSolve assists in the diagnosis of such incidents but the resolution responsibility lies with the relevant party.

**AMS-INC-004**  
Oracle SaaS platform availability: Oracle Fusion HCM and ERP are delivered on Oracle's SaaS infrastructure. Oracle SaaS outages and Oracle-caused service degradation are outside APPSolve's control. APPSolve logs Oracle SRs, monitors Oracle's resolution progress, and communicates status to the client. SLA clock is paused during Oracle-caused outages.

**AMS-INC-005**  
Incident resolution: APPSolve provides resolution for application configuration incidents. For complex incidents requiring Oracle Support involvement (Oracle bug, Oracle platform issue, Oracle patch required), resolution timelines depend on Oracle's support processes and are outside APPSolve's control. APPSolve manages Oracle SR progress on the client's behalf and provides weekly status updates for open Oracle SRs.

---

## 89. Service Requests

**AMS-SRQ-001**  
A service request is a planned, pre-agreed configuration change or task that does not constitute a defect and does not represent new scope. Service requests are fulfilled within the monthly hours allocation. Examples: adding a new user and assigning roles; updating an existing approval limit in a workflow; adding a new GL account to an existing value set; updating a document sequence; configuring a new supplier payment term.

**AMS-SRQ-002**  
Service requests are prioritised within the monthly allocation based on business need, as agreed between the client's designated AMS contact and APPSolve's AMS Team Lead. APPSolve does not guarantee fulfilment of all service requests within a given month if the volume exceeds the monthly allocation.

**AMS-SRQ-003**  
Service requests that are assessed as requiring design work, testing, or stakeholder approval before implementation — even if small — are raised as change requests rather than service requests. The boundary between SR and CR is the need for a documented design and formal approval.

**AMS-SRQ-004**  
Standard service request catalogue: APPSolve maintains a list of standard service requests with pre-defined effort estimates. Requests on the standard catalogue are fulfilled within the allocated hours without further negotiation. Non-catalogue requests are assessed per complexity and agreed with the client before work commences.

---

## 90. Enhancements

**AMS-ENH-001**  
Enhancements — adding new functionality, new configuration, new modules, new integrations, or new reports beyond the contracted application scope — are excluded from AMS. Enhancements are delivered as project work under a separate project SOW.

**AMS-ENH-002**  
Where the client requests an enhancement during an AMS support interaction, APPSolve identifies it as an enhancement, logs it, and advises the client that it requires a separate project engagement. APPSolve does not absorb enhancement work into the AMS hours without explicit commercial agreement.

**AMS-ENH-003**  
Enhancement identification: APPSolve's obligation is to tell the client when a request crosses the enhancement boundary. APPSolve is not responsible for the client's decision about whether to proceed with the enhancement or when to schedule it.

**AMS-ENH-004**  
Where a client-requested configuration change is ambiguous (could be interpreted as support or enhancement), APPSolve escalates to the AMS Account Manager and the client's designated AMS contact for classification before work commences. Agreed classifications are logged in the monthly report.

---

## 91. Change Requests

**AMS-CR-001**  
A change request (CR) is a formally scoped and approved work item that constitutes new or changed scope beyond the standard service request catalogue. The standard CR threshold is 2 hours: changes estimated at more than 2 hours of effort require a formal written CR, an effort estimate, and written client approval before work commences. APPSolve may, at its discretion, absorb changes estimated below 2 hours into the monthly support hours without raising a formal CR. No entitlement to this discretionary treatment is created by previous practice — each case is assessed independently. The CR threshold defined in a specific AMS agreement takes precedence over this standard.

**AMS-CR-002**  
The change request process: (1) Client submits change request description via the support channel; (2) APPSolve assesses and produces a written effort estimate within five (5) business days; (3) Client approves the estimate in writing; (4) APPSolve schedules and delivers the change; (5) Client signs off delivery. No change request work commences without written client approval of the estimate.

**AMS-CR-003**  
Change requests are not subject to the incident SLA. CR delivery timelines are agreed at the time of CR approval based on complexity, resource availability, and the client's priority. APPSolve provides a delivery date at the time of CR approval.

**AMS-CR-004**  
Change requests that introduce risk to the live production system (for example, security role changes affecting multiple users, workflow restructuring, GL period-end configuration changes) are assessed by APPSolve for risk before implementation and require a testing confirmation from the client before production deployment.

---

## 92. Defect Management

**AMS-DEF-001**  
A defect is a system behaviour that does not conform to the agreed configuration design documented during implementation. Defects in the configured system discovered post-go-live are covered under AMS incident management and are resolved within the monthly hours allocation (or as a priority incident depending on severity) at no additional charge.

**AMS-DEF-002**  
Defect vs enhancement vs configuration drift: APPSolve distinguishes between three types of post-go-live issues:
- **Defect:** System does not behave per the agreed design — APPSolve resolves, no additional charge
- **Enhancement:** Client requests new functionality not in the original design — separately priced project work
- **Configuration drift:** Client or another party has changed the configuration since go-live, causing unexpected behaviour — APPSolve investigates; resolution effort may be billed as a service request

**AMS-DEF-003**  
Defects introduced by Oracle's quarterly platform updates are managed as follows: APPSolve monitors Oracle's quarterly release notes for the client's supported applications; where a release update introduces a defect in the client's configuration, APPSolve resolves the defect within the standard SLA; the root cause (Oracle release) is documented in the monthly report.

**AMS-DEF-004**  
Configuration changes made by the client's internal team without APPSolve involvement may invalidate existing configuration and cause system issues. APPSolve is not responsible for defects caused by client-initiated configuration changes. Restoring the system from a client-caused configuration error is treated as a service request and billed against the monthly allocation.

---

## 93. SLA Assumptions

**AMS-SLA-001**  
APPSolve's standard AMS SLA defines the following response time targets per priority level, applicable uniformly across Oracle, Acumatica, and BeBanking AMS agreements:

| Priority | Target Response Time |
|---|---|
| P1 — Critical | 1 hour (from ticket logging during contracted support hours) |
| P2 — Major | 4 business hours |
| P3 — Normal | 1 business day |
| P4 — Minor | 3 business days |

Response time is the time from ticket logging to APPSolve's first substantive response — acknowledgement, initial diagnosis, or a request for additional information required to commence investigation. Response time is not resolution time. Guaranteed resolution time requires a separately contracted resolution SLA.

**AMS-SLA-002**  
SLA clock starts when the ticket is logged in APPSolve's support system during business hours. Tickets logged outside business hours (evenings, weekends, public holidays) start the SLA clock at 08:00 SAST on the next business day, unless a 24/7 SLA has been contracted.

**AMS-SLA-003**  
SLA clock is paused in the following circumstances:
- APPSolve is waiting for information from the client that is required to proceed with investigation or resolution
- The incident is pending Oracle Support response (Oracle SR lodged; resolution outside APPSolve's control)
- The client has not approved a required change to proceed with resolution
- A scheduled maintenance window is in progress (agreed in advance)

**AMS-SLA-004**  
SLA reporting: APPSolve reports SLA performance in the monthly support report. The report shows: total tickets logged by priority; SLA compliance rate per priority; SLA breaches with root cause; Oracle SR status for open items; change request status.

**AMS-SLA-005**  
Named consultant allocation is not included in standard AMS. AMS support is delivered by the APPSolve support team on a best-effort resource allocation basis. While APPSolve endeavours to assign consultants with client-specific knowledge, no named consultant commitment is made under standard AMS. A dedicated named consultant arrangement — where a specific consultant is contractually committed to the client's AMS account — requires a separate commercial agreement at the applicable dedicated-resource rate.

---

## 94. Priority Definitions

**AMS-PRI-001**  
Standard APPSolve AMS priority classification and response time targets:

| Priority | Definition | Response Target |
|---|---|---|
| **P1 — Critical** | Complete system outage affecting all users; payroll processing blocked; financial period-end processing blocked; all integrations failed; data loss or corruption risk. System is unusable for core business functions. | **1 hour** |
| **P2 — Major** | Major functionality impaired affecting a significant user population or a critical business process; key financial transactions cannot be processed; major integration failure affecting payment runs or bank reconciliation. Workaround exists but is severely limiting. | **4 business hours** |
| **P3 — Normal** | Non-critical functionality impaired; a subset of users affected; workaround exists and is practical; non-urgent configuration question; report not working as expected. | **1 business day** |
| **P4 — Minor** | Minor cosmetic issue; general how-to question; non-urgent service request; documentation request; low-impact configuration query. | **3 business days** |

Response targets are uniform across Oracle, Acumatica, and BeBanking AMS. Response time is not resolution time (see AMS-SLA-001).

**AMS-PRI-002**  
Priority escalation: where a P3 or P4 issue has not been resolved within the expected timeframe and its business impact increases (for example, a P3 report error becomes P2 at month-end), the client may request a priority re-classification. APPSolve's AMS Account Manager reviews the re-classification request within four (4) business hours.

**AMS-PRI-003**  
P1 incidents: APPSolve commits to providing an initial response and diagnosis update within the contracted P1 response time. For P1 incidents occurring outside business hours under a standard (business hours) SLA, APPSolve will respond at the start of the next business day. Where a P1 outside-hours response is required, this must be contracted as a 24/7 SLA add-on.

---

## 95. Release Management

**AMS-REL-001**  
Oracle Fusion HCM and ERP receive quarterly platform updates from Oracle (typically January, April, July, October). Oracle manages the update schedule; APPSolve does not control Oracle's release cadence. APPSolve provides Oracle quarterly release advisory as a standard AMS service item — reviewing Oracle release notes for the client's contracted modules and flagging changes with potential impact on the client's configured processes. The advisory is a review and notification service. Regression testing, UAT execution, and business process validation following each Oracle quarterly update are excluded from standard AMS unless specifically contracted as a separately priced service. The customer remains responsible for business testing of their own processes before and after each quarterly update.

**AMS-REL-002**  
Where an Oracle quarterly update introduces a change that affects the client's configured process or causes a regression, APPSolve investigates and resolves the regression as an AMS incident under the standard SLA. Oracle platform-caused regressions are investigated by APPSolve; where an Oracle bug is identified, APPSolve logs an Oracle SR and manages resolution.

**AMS-REL-003**  
Oracle quarterly update regression testing — systematically testing all configured processes in a non-production environment after each Oracle update before activating in production — is not included in standard AMS scope. Full regression testing is a separately contracted service. APPSolve recommends regression testing before each quarterly update for high-criticality environments (payroll, financial close, banking integrations).

**AMS-REL-004**  
Acumatica updates: Acumatica releases major version updates and maintenance builds. APPSolve provides Acumatica release advisory under Acumatica AMS — reviewing release notes and flagging customisation compatibility risks. Full Acumatica version upgrade execution is not included in standard AMS and requires a separate upgrade engagement.

**AMS-REL-005**  
BeBanking updates: BeBanking product updates and banking partner connectivity changes are managed by BeBanking. APPSolve monitors for BeBanking-initiated changes that may affect OIC integrations and provides advisory to the client. Format changes or connectivity changes initiated by BeBanking or the client's bank may require OIC integration updates — these are assessed and priced per the OIC pack assumptions.

---

## 96. Patching

**AMS-PAT-001**  
Oracle Fusion HCM and ERP patches are applied by Oracle as part of the SaaS subscription. APPSolve does not apply Oracle SaaS patches; Oracle manages patching automatically as part of its platform management. APPSolve's role is to monitor for patch-related regressions and resolve them under the AMS SLA.

**AMS-PAT-002**  
Oracle EBS patching: where APPSolve provides AMS for Oracle EBS (on-premises or OCI-hosted), patch assessment, testing, and application are separately contracted. Oracle EBS patching is a technical DBA task and is not included in standard application AMS unless a DBA support component is explicitly in scope.

**AMS-PAT-003**  
Acumatica patching: Acumatica maintenance builds are applied by Acumatica or the client's Acumatica cloud host (Acumatica SaaS or partner-hosted). APPSolve monitors for Acumatica build compatibility with the client's customisations and advises accordingly. Where a build update breaks a client customisation, APPSolve investigates and resolves under AMS.

---

## 97. Monitoring

**AMS-MON-001**  
Standard AMS includes mailbox monitoring during contracted support hours only — APPSolve monitors the support mailbox and responds to tickets logged during business hours. Proactive monitoring of Oracle OIC integration error consoles, automated alerting, infrastructure monitoring, and application performance monitoring are excluded from standard AMS unless specifically contracted as a monitoring add-on service. Where a monitoring add-on is contracted, APPSolve reviews the OIC error console at the agreed frequency, logs incidents for any failed integrations, and commences investigation within the SLA response time. 24/7 monitoring, automated alerting frameworks, and infrastructure-level monitoring require a separately scoped and priced monitoring engagement.

**AMS-MON-002**  
Proactive monitoring — automated alerting, SLA-based monitoring dashboards, infrastructure monitoring, and log aggregation — requires a separate monitoring tooling arrangement. APPSolve does not provide a proprietary monitoring platform; where the client requires proactive monitoring, APPSolve can configure Oracle OIC's built-in alerting and notification framework as a configuration activity within AMS.

**AMS-MON-003**  
Oracle Fusion HCM and ERP system health monitoring is Oracle's responsibility as the SaaS provider. Oracle operates the infrastructure, monitors availability, and manages platform incidents. The Oracle SaaS status page is the authoritative source for platform availability status. APPSolve does not duplicate Oracle's infrastructure monitoring.

**AMS-MON-004**  
BeBanking monitoring: APPSolve monitors OIC integration error logs for BeBanking H2H integrations where BeBanking AMS is contracted. BeBanking platform monitoring (the BeBanking H2H portal, bank connectivity status) is BeBanking's responsibility.

---

## 98. Reporting

**AMS-REP-001**  
APPSolve provides a monthly support report to the client's designated AMS contact. The monthly report covers: support activity summary (tickets by priority and status); SLA compliance summary; hours consumed vs. monthly allocation; open incidents and service requests; change requests raised, approved, and in progress; Oracle SR status (where open); planned activities for the following month.

**AMS-REP-002**  
The monthly report is provided within five (5) business days of the end of each calendar month. The report is delivered via email to the client's designated AMS contact and any additional distribution recipients agreed in the AMS agreement.

**AMS-REP-003**  
Quarterly review meeting: APPSolve offers a quarterly AMS service review meeting (60–90 minutes, remote) to review AMS performance, discuss upcoming changes, review Oracle release impacts, and align on priorities. The quarterly review is offered as standard — whether it takes place is at the client's discretion.

**AMS-REP-004**  
Ad hoc reporting: APPSolve provides ad hoc AMS reports on request (for example, a summary of all CRs for the year to date for internal audit, or a support activity extract for a specific period). Ad hoc reports are reasonable requests fulfilled within the monthly hours allocation.

---

## 99. Customer Responsibilities

**AMS-CUS-001**  
**Business Process Ownership:** The client owns its business processes. AMS covers the application layer; the client's functional leads are responsible for deciding whether a business process change is needed, documenting the requirement, and approving the solution before APPSolve implements it. APPSolve does not redesign business processes under AMS.

**AMS-CUS-002**  
**User Support (Level 1):** The client's internal helpdesk or ERP team provides first-line support to end users — answering how-to questions, resetting passwords, explaining existing functionality, and triaging whether an issue is a user error or a system issue. This Level 1 responsibility belongs to the client unless explicitly contracted to APPSolve.

**AMS-CUS-003**  
**User Access Management:** Creating new user accounts, assigning Oracle ERP or Oracle HCM roles to users, and deactivating users who leave are the client's IT team's responsibility, unless APPSolve has been contracted to provide user access management as part of the AMS agreement.

**AMS-CUS-004**  
**Internal Change Management:** Communicating system changes to the client's user population, updating internal user guides and job aids, and managing internal business change resulting from configuration updates are the client's responsibility.

**AMS-CUS-005**  
**Change Request Approval:** All change requests must be approved in writing by the client's designated AMS contact (or a named delegate) before APPSolve commences work. Verbal approval is not sufficient. APPSolve does not proceed with a CR without written approval.

**AMS-CUS-006**  
**Test Sign-Off:** Where a change request, service request, or incident resolution requires testing before production deployment, the client's functional team performs and signs off the test. APPSolve deploys to production only after written client sign-off on the test outcome.

**AMS-CUS-007**  
**Information Provision:** The client provides accurate and complete information when logging support tickets — including error messages, screenshots, steps to reproduce, affected users, and business impact. Incomplete ticket information delays investigation. APPSolve is not responsible for SLA delays caused by insufficient information provided by the client.

**AMS-CUS-008**  
**Internal IT Responsibilities:** Network connectivity, hardware, browser compatibility, VPN access, printer configuration, and other IT infrastructure are the client's IT team's responsibility. APPSolve provides application support only; infrastructure support is not in AMS scope.

**AMS-CUS-009**  
**Oracle Support Access:** The client provides APPSolve with access to the client's Oracle Support account (Customer Support Identifier — CSI) to log Oracle SRs on the client's behalf. Without CSI access, APPSolve cannot manage Oracle SRs directly and the client must log SRs themselves. APPSolve can provide the SR description and evidence for the client to log.

**AMS-CUS-010**  
**AMS Onboarding Documentation:** At the start of an AMS engagement, the client provides APPSolve with access to: the implementation project documentation (Scope and Design documents, configuration workbooks, test sign-off records); current system access credentials for the AMS team; and an introduction to the client's internal ERP/IT team contacts. Where implementation was done by APPSolve, this documentation already exists.

---

## 100. Exclusions

**AMS-EXC-001**  
**New Module Implementations:** Implementing Oracle Fusion modules, Acumatica modules, or BeBanking integrations not in the client's current production system is excluded from AMS. New module implementations are project work under a separate implementation SOW.

**AMS-EXC-002**  
**New Integration Development:** Developing new OIC integrations or new BeBanking integrations not currently in the client's production environment is excluded from AMS. See OIC pack for integration development assumptions.

**AMS-EXC-003**  
**New Data Migration:** Loading new data sets into Oracle ERP or HCM post-go-live (for example, migrating a newly acquired company's supplier master or adding historical transactions from a merged entity) is excluded from AMS and requires a separately scoped data migration engagement.

**AMS-EXC-004**  
**New Report Development:** Developing new OTBI reports, FRS reports, BI Publisher reports, or Acumatica reports not in the client's existing report library is excluded from AMS. New report development is a project item. Adjusting existing in-scope reports within the report scope defined in the AMS agreement is a service request.

**AMS-EXC-005**  
**Regulatory Compliance Advice:** APPSolve does not provide tax, legal, audit, or regulatory compliance advice under AMS. System configuration to implement compliance requirements must be driven by a client-provided requirement specification approved by the client's tax or legal team.

**AMS-EXC-006**  
**End-User Training:** Delivering training to the client's users on existing Oracle or Acumatica functionality is excluded from standard AMS. Training can be contracted as a separately invoiced training engagement. APPSolve can provide quick reference cards and job aids for simple how-to queries within the monthly support hours.

**AMS-EXC-007**  
**Infrastructure Support:** Network, hardware, browser, VPN, printer, and IT infrastructure are the client's responsibility. Oracle SaaS infrastructure is Oracle's responsibility. APPSolve's AMS scope is the application configuration layer only.

**AMS-EXC-008**  
**Acumatica Customisation Development:** Developing new Acumatica customisations (low-code extensions, workflow customisations, custom web services, custom report designer reports) is excluded from standard Acumatica AMS. New customisation development requires a separately scoped development engagement.

**AMS-EXC-009**  
**Major Version Upgrades:** Oracle EBS major version upgrades, Acumatica major version upgrades, and BeBanking platform version migrations are excluded from standard AMS. These are project-level activities requiring planning, testing, and delivery effort far exceeding the AMS monthly support model.

**AMS-EXC-010**  
**Oracle Licensing and Subscription Management:** APPSolve does not manage the client's Oracle licences, Oracle Cloud subscription changes, or Oracle product roadmap planning. These are the client's commercial relationship with Oracle. APPSolve advises on licensing implications of configuration decisions; it does not purchase, renew, or modify Oracle licences on the client's behalf.

**AMS-EXC-011**  
**Business Intelligence and Analytics Development:** Developing Oracle Analytics Cloud (OAX/FAW) dashboards, reports, and data models is excluded from AMS. OAX development is separately scoped project work.

**AMS-EXC-012**  
**Disaster Recovery Testing:** Planning, executing, or certifying disaster recovery tests for the client's Oracle ERP or HCM environment is excluded from AMS. Oracle SaaS DR is Oracle's responsibility; on-premises DR is the client's IT team's responsibility.

---

## BU Lead Decisions Applied — All Items Closed

| Item ID | Decision | Assumptions Updated | Closed |
|---|---|---|---|
| BU-AMS-001 | P1: 1 hour; P2: 4 business hours; P3: 1 business day; P4: 3 business days. Uniform across Oracle, Acumatica, BeBanking. Response time ≠ resolution time. | AMS-SLA-001, AMS-PRI-001 | 2026-06-15 |
| BU-AMS-002 | 08:00–17:00 SAST Mon–Fri confirmed. Excluding SA public holidays. Extended hours, weekend, 24x7 require separate commercial agreement. | AMS-HRS-001 | 2026-06-15 |
| BU-AMS-003 | No default monthly hours. Retainer-based and allocated-hour models both permitted. Model and allocation defined per AMS agreement. | AMS-HRS-003 | 2026-06-15 |
| BU-AMS-004 | CR threshold = 2 hours. Above 2 hours requires formal CR. Below threshold APPSolve may absorb at discretion; no entitlement from prior practice. | AMS-CR-001 | 2026-06-15 |
| BU-AMS-005 | Oracle quarterly release advisory included in standard AMS. Regression testing, UAT execution, business process validation excluded unless contracted. Customer responsible for business testing. | AMS-REL-001 | 2026-06-15 |
| BU-AMS-006 | Named consultant not included. Support delivered by APPSolve support team on best-effort resource allocation. Dedicated named consultant requires separate commercial agreement. | AMS-SLA-005 | 2026-06-15 |
| BU-AMS-007 | Standard AMS = mailbox monitoring during support hours only. Proactive/automated/24x7/infrastructure monitoring excluded unless specifically contracted. | AMS-MON-001 | 2026-06-15 |

---

*AMS_ASSUMPTIONS_V1.0 | WP11E — AMS / Managed Services Assumptions Pack | Approved 2026-06-15 | BU Lead — Oracle Practice (Cross-BU)*  
*84 assumptions / exclusions / dependencies / constraints / responsibilities across Sections 85–100*  
*Cross-BU pack — applies to Oracle, Acumatica, and BeBanking AMS agreements | Governed under: 08_Commercial/ASSUMPTION_GOVERNANCE.md*
