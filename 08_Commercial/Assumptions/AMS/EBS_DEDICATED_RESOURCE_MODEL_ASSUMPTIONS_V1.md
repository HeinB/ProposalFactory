---
document_id: EBS-DRM-ASSUMPTIONS-V1
title: "APPSolve EBS AMS — Dedicated Resource Model Assumptions Overlay Pack"
version: "1.0"
status: "Approved v1.0 — all BU Lead decisions resolved; WP15F 2026-06-19"
created: "2026-06-18"
created_by: "WP15D — EBS AMS Remediation Programme"
promoted: "2026-06-19"
promoted_by: "WP15F — EBS AMS Overlay Promotion"
classification: "Overlay Pack — additive to AMS_ASSUMPTIONS_V1.md"
parent_pack: "AMS_ASSUMPTIONS_V1.md"
applies_to: "Oracle EBS AMS engagements where client specifies a named/dedicated resource team rather than a pooled support model"
override_assumptions: "AMS-SLA-005, AMS-HRS-001 (hours model only — not clock rules)"
assumption_count: 62
bu_lead_decisions_resolved:
  - "EBS-DRM-BU-001 RESOLVED WP15F 2026-06-19: Per-engagement model confirmed; ARM IT045 hours are reference architecture only; actual minimums defined in AMS agreement schedule"
  - "EBS-DRM-BU-002 RESOLVED WP15F 2026-06-19: Rollover model confirmed; unused minimum hours roll over to the following month"
  - "EBS-DRM-BU-003 RESOLVED WP15F 2026-06-19: 3-business-day illness absorption and 10-business-day leave notice confirmed as standard"
  - "EBS-DRM-BU-004 RESOLVED WP15F 2026-06-19: 30-day (calendar) substitution notice confirmed; equivalent grade = same or greater role band in relevant EBS domain"
  - "EBS-DRM-BU-005 RESOLVED WP15F 2026-06-19: 30-day KT period and runbook creation confirmed as standard in all DRM engagements"
approved_for_reuse: true
lifecycle_status: APPROVED
---

# APPSolve EBS AMS — Dedicated Resource Model Assumptions Overlay Pack

**Pack type:** Overlay — additive to `AMS_ASSUMPTIONS_V1.md`
**Applies to:** Oracle EBS AMS engagements where the client procures a named, dedicated support team rather than APPSolve's standard pooled AMS model
**Status:** Approved v1.0 — all 5 BU Lead decisions resolved (WP15F 2026-06-19); approved for use in EBS AMS tenders with dedicated named resource requirements

> **Overlay principle:** This pack SUPPLEMENTS the base AMS pack. Assumptions EBS-DRM-001 through EBS-DRM-062 are additive unless the assumption header explicitly states "[REPLACES: AMS-XXX-NNN]". Where a replacement is stated, the base AMS assumption is suppressed for the duration of the EBS AMS engagement. All non-replaced AMS base assumptions remain in force.
>
> **Dedicated Resource Model definition:** a contracted model in which the client pays for specified minimum monthly hours from named APPSolve consultants in defined roles. These hours are ring-fenced for the client — they are not shared with other APPSolve AMS clients. The DRM applies where the client's contract specifies named roles and minimum hour commitments per role.
>
> **Do not assemble this overlay for standard pooled AMS engagements.** The base AMS pack governs pooled support. This overlay is specific to EBS AMS engagements with named resource commitments.

---

## Overlay Section 1: Purpose, Scope, and Precedence

**EBS-DRM-001 [REPLACES: AMS-SLA-005]**
For EBS AMS engagements using this overlay, the base AMS pack assumption AMS-SLA-005 ("Named consultant excluded from standard AMS") is superseded. A Dedicated Resource Model engagement by definition includes named consultants with contracted minimum monthly hour commitments. The roles, minimum hours, and governance obligations for each named resource are defined in EBS-DRM-010 through EBS-DRM-029 of this overlay.

**EBS-DRM-002**
This overlay assumes that the DRM contract structure specifies, at minimum: the role title for each named resource; the minimum monthly hours committed per role; the support hours window (business hours, 24/7 P1, or extended); and the commercial rate or blended monthly fee for the named resource team. Where any of these elements is absent from the contract, the standard base AMS pooled model applies to that element.

**EBS-DRM-003**
Named resources under the DRM are APPSolve employees or contractors permanently engaged by APPSolve. The DRM does not constitute an employment relationship, labour broking arrangement, or secondment between APPSolve's resources and the client. APPSolve retains full employment, management, and HR authority over all named resources.

---

## Overlay Section 2: Service Delivery Manager (SDM) Role

**EBS-DRM-004**
The Service Delivery Manager (SDM) is the single point of accountability for the EBS AMS engagement. The SDM owns client relationship management, SLA performance, team coordination, escalation handling, and monthly and quarterly governance reporting. The SDM is the client's first point of escalation above the support consultant tier.

**EBS-DRM-005**
SDM minimum monthly commitment: the SDM commits a minimum of 40 hours per month to the client under the DRM. These hours cover: weekly operational call preparation and facilitation; monthly SLA review preparation and facilitation; incident management oversight; resource coordination; monthly report compilation and delivery; and client stakeholder communication. Additional SDM hours are engaged at the contracted SDM hourly rate. The 40-hour figure is the ARM IT045 reference architecture; actual SDM minimum hours for each engagement are confirmed in the AMS agreement schedule. (EBS-DRM-BU-001 RESOLVED — per-engagement model confirmed; WP15F 2026-06-19)

**EBS-DRM-006**
SDM availability: the SDM is available to the client during business hours (08:00–17:00 SAST, Monday–Friday, excluding South African public holidays). For P1 incidents where 24/7 coverage is contracted, the SDM is on the after-hours escalation tree per EBS-SLA-028 but is not necessarily the primary on-call responder — the SDM's after-hours role is coordination and executive communication where the on-call consultant cannot resolve the incident within 1 hour.

**EBS-DRM-007**
SDM continuity: APPSolve does not change the named SDM without providing the client with a minimum of 30 days' advance written notice, except where the SDM is absent due to unplanned leave or termination. In these circumstances, APPSolve designates an Acting SDM within 2 business days and provides formal nomination within 10 business days. The acting appointment process is governed by EBS-DRM-040 through EBS-DRM-044.

**EBS-DRM-008**
SDM onboarding: the incoming SDM completes a 30-day knowledge transfer with the outgoing SDM (where the outgoing SDM is available) before assuming full client-facing responsibility. The KT programme is governed by EBS-DRM-050 through EBS-DRM-055. Where an unplanned SDM change occurs and the 30-day KT is not possible, the Acting SDM assumes the role with the available briefing documentation and the KT obligation is fulfilled on a best-efforts basis over the first 30 days of the acting period.

**EBS-DRM-009**
SDM skills requirement: the named SDM holds a minimum of 5 years' Oracle AMS or Oracle EBS project experience, with demonstrated client-facing delivery management experience. SDM selection is APPSolve's responsibility. Where the client requests a replacement SDM on grounds of service quality, APPSolve investigates the request within 5 business days and provides a remediation plan or a replacement nomination within 20 business days.

---

## Overlay Section 3: Named DBA / OCI Specialist Role

**EBS-DRM-010**
The Named DBA / OCI Specialist is the dedicated database and infrastructure expert for the EBS AMS engagement. The DBA role covers: Oracle database administration for EBS (R11, R12.1, or R12.2); performance tuning; patch application (where patch management is in AMS scope); backup monitoring (advisory, not DR hosting); OCI infrastructure coordination (where EBS runs on OCI); and database-related incident resolution.

**EBS-DRM-011**
DBA scope boundary: the DBA role is scoped to Oracle Database (versions in use for the EBS environment — typically 11g, 12c, 19c, or 21c) and OCI services that directly support the EBS workload (Compute, Block Storage, Networking as they relate to EBS database and application tiers). The DBA does not assume responsibility for: the client's OCI tenancy governance (BU-OCI-007 permanent constraint applies); cloud cost management; non-EBS workloads on OCI; or DR site operations where separately contracted.

**EBS-DRM-012**
DBA minimum monthly hours: the DBA / OCI Specialist commits a minimum of 160 hours per month to the client under the DRM. These hours cover BAU DBA operations, proactive monitoring, incident resolution, and scheduled maintenance. Hours in excess of the minimum are engaged at the contracted DBA hourly rate. The 160-hour figure is the ARM IT045 reference architecture; actual minimum hours are defined per engagement in the AMS agreement schedule. (EBS-DRM-BU-001 RESOLVED; WP15F 2026-06-19)

**EBS-DRM-013**
EBS infrastructure scope clarification [SUPPLEMENTS: AMS-INC-004]: Unlike Oracle Fusion SaaS, Oracle EBS is not delivered on Oracle's managed SaaS infrastructure. The client operates the EBS application tier (on-premises or on OCI). APPSolve's DBA / OCI Specialist has access to the database and application tier to perform database administration, patching, and performance management activities within the contracted DBA scope. The client retains ownership and administrator access to the OCI tenancy or on-premises environment.

**EBS-DRM-014**
EBS patch management: where EBS patching is included in the DBA scope, APPSolve's DBA Specialist applies Oracle-recommended patches (one-off patches, PSUs, RUs, and interim patches) in accordance with the agreed maintenance window schedule (EBS-SLA-040 through EBS-SLA-043). Patch recommendations are reviewed and approved by the client before application. APPSolve does not apply patches that the client has explicitly declined.

---

## Overlay Section 4: Named Functional Leads

**EBS-DRM-015**
The DRM includes named Functional Lead resources for each EBS module group in scope. The standard EBS AMS DRM functional lead structure is: (a) HCM Functional Lead — responsible for Oracle EBS HR, Payroll, and Self-Service; (b) Finance Functional Lead — responsible for Oracle EBS General Ledger, Accounts Payable, Accounts Receivable, Fixed Assets, Cash Management, and iProcurement. Additional module leads (Supply Chain, Projects) are separately contracted.

**EBS-DRM-016**
HCM Functional Lead minimum monthly hours: the HCM Functional Lead commits a minimum of 240 hours per month to the client under the DRM. These hours cover: HCM module incident resolution; functional configuration changes; user support; payroll processing support; reporting; integration support (EBS Payroll–PaySpace where contracted); and HCM process documentation maintenance. The 240-hour figure is the ARM IT045 reference architecture; actual minimum hours are defined per engagement in the AMS agreement schedule. (EBS-DRM-BU-001 RESOLVED; WP15F 2026-06-19)

**EBS-DRM-017**
Finance Functional Lead minimum monthly hours: the Finance Functional Lead commits a minimum of 160 hours per month to the client under the DRM. These hours cover: Finance module incident resolution; period-end support; month-end reconciliation support; functional configuration changes; chart of accounts maintenance; reporting; and bank interface management (where contracted). The 160-hour figure is the ARM IT045 reference architecture; actual minimum hours are defined per engagement in the AMS agreement schedule. (EBS-DRM-BU-001 RESOLVED; WP15F 2026-06-19)

**EBS-DRM-018**
Functional Lead scope boundary: Functional Leads are responsible for Oracle EBS functional configuration and support. They do not perform: custom development (RICE/CEMLI — separately scoped under CRs); report development (separately scoped); data migration (separately scoped); or upgrade activities (separately scoped). Where a functional issue requires technical investigation or custom code, the Functional Lead engages the Technical Specialist per EBS-DRM-020.

**EBS-DRM-019**
Functional Lead module boundary: the HCM Functional Lead's scope is limited to EBS modules contracted in the AMS agreement. Where the client adds an EBS module after the AMS agreement commences, APPSolve and the client agree the additional module inclusion terms via Change Request before the Functional Lead assumes support responsibility for the new module.

---

## Overlay Section 5: Named Technical / OIC Specialist

**EBS-DRM-020**
The Named Technical / OIC Specialist covers Oracle Integration Cloud (OIC) integration support, EBS technical layer support (Forms, Workflow, APIs, concurrent programs, customisation support advisory), and BeBanking integration support where BeBanking is within the AMS agreement scope. The Technical Specialist is the DRM resource for all integration-related incidents and service requests.

**EBS-DRM-021**
Technical / OIC Specialist minimum monthly hours: the Technical / OIC Specialist commits a minimum of 80 hours per month to the client under the DRM. These hours cover: OIC integration monitoring and incident resolution; technical advisory for customisation issues; EBS Workflow issue resolution; API and concurrent program troubleshooting; and BeBanking integration support (where contracted). The 80-hour figure is the ARM IT045 reference architecture; actual minimum hours are defined per engagement in the AMS agreement schedule. (EBS-DRM-BU-001 RESOLVED; WP15F 2026-06-19)

**EBS-DRM-022**
OIC scope boundary: the Technical / OIC Specialist manages OIC integrations within the AMS agreement scope (those built and handed over as part of the implementation). New OIC integrations or material enhancements to existing OIC integrations are scoped and delivered as project work separately. The Technical Specialist provides post-implementation support, not new development, within the AMS hours commitment.

**EBS-DRM-023**
BeBanking integration rule: where BeBanking is within the AMS agreement scope, the Technical Specialist supports the EBS-to-BeBanking and BeBanking-to-OIC integration at the Oracle EBS and OIC layers. BeBanking core banking platform issues are escalated to BeBanking's own support team. APPSolve does not assume responsibility for BeBanking application-layer incidents; these are the client's responsibility to log with BeBanking directly.

---

## Overlay Section 6: Capacity Allocation Model

**EBS-DRM-024**
Non-pooled allocation: under the DRM, each named resource's contracted minimum hours are ring-fenced exclusively for the client. These hours are not shared across APPSolve's AMS client pool. Hours not consumed within the month are not re-allocated to other APPSolve clients. The commercial consequence of unconsumed minimum hours is governed by EBS-DRM-030.

**EBS-DRM-025**
Total team capacity: the standard EBS AMS DRM team minimum monthly capacity is 680 hours (SDM 40h + HCM Lead 240h + Finance Lead 160h + DBA+OCI 160h + OIC/Technical 80h). This total is the ARM IT045 reference architecture; actual totals are defined in the AMS agreement schedule and may differ per engagement. (EBS-DRM-BU-001 RESOLVED — per-engagement model confirmed; WP15F 2026-06-19)

**EBS-DRM-026**
Above-minimum hours: where the client requires work beyond the contracted minimum hours in any role in any month, the additional hours are engaged at the contracted hourly rate for that role. APPSolve provides an estimate and the client approves prior to the additional work commencing, except for P1 incidents where APPSolve engages the required hours and reports usage immediately after stabilisation.

**EBS-DRM-027**
Role substitution within team: where the client requires work that is within the DRM scope but falls between role boundaries, the SDM coordinates the most appropriate team member to handle it. Cross-role assistance does not change the minimum hour commitments of the individual roles; it is managed through team collaboration under the SDM.

**EBS-DRM-028**
Client-side time requirements: the DRM model assumes that the client designates a named AMS Relationship Owner (functional owner of the EBS AMS engagement) who attends governance meetings, approves change requests, and coordinates client-side testing. The absence of a client Relationship Owner does not reduce APPSolve's obligations but may impact the speed of delivery for items requiring client approval.

**EBS-DRM-029**
Minimum hours floor: the contracted minimum hours per role represent the floor of APPSolve's commitment, not the ceiling. APPSolve will not deliver fewer than the minimum hours to the client in any month, subject to EBS-DRM-035 through EBS-DRM-039 (leave and absence provisions).

---

## Overlay Section 7: Hours Consumption and Tracking

**EBS-DRM-030**
Monthly hours rollover: unused minimum hours in a given month roll over to the following month for the client's use. Unconsumed hours from month N are added to month N+1's available committed hours balance. Rollover hours that remain unconsumed at the end of month N+1 expire and are not further carried forward beyond one additional month. The rollover model is confirmed as the EBS AMS DRM commercial standard. (EBS-DRM-BU-002 RESOLVED — rollover model confirmed; WP15F 2026-06-19)

**EBS-DRM-031**
Hours tracking system: APPSolve tracks all DRM hours by resource by ticket or activity in its project management and support system. Each time entry is categorised as: incident resolution, service request, proactive maintenance, governance, or knowledge management. The hours consumed against each category and each role are reported in the monthly DRM report per EBS-DRM-058.

**EBS-DRM-032**
Hours transparency: the client has read access to APPSolve's hours tracking system (or a client-facing dashboard equivalent) to view hours consumed by role and by category in real time. APPSolve provides the access credentials within 10 business days of DRM commencement. Where real-time access is not technically feasible, APPSolve provides a weekly hours snapshot by email every Monday by 10:00 SAST.

**EBS-DRM-033**
Hours dispute resolution: where the client disputes the hours recorded in the monthly report, the client raises the dispute in writing within 10 business days of receiving the monthly report. APPSolve reviews the disputed entries within 5 business days, provides the supporting ticket and time entry detail, and agrees or adjusts the hours. Adjusted hours are reflected in the following month's report.

---

## Overlay Section 8: Leave and Absence Coverage

**EBS-DRM-034**
Leave planning notice: named DRM resources coordinate planned leave (annual leave, study leave, medical procedures with advance notice) with the SDM. The SDM notifies the client's AMS Relationship Owner of planned absences of 3 or more consecutive business days a minimum of 10 business days in advance. Notification includes: resource name, absence dates, and coverage arrangement. (EBS-DRM-BU-003 RESOLVED — 10-business-day leave notice confirmed as standard; WP15F 2026-06-19)

**EBS-DRM-035**
APPSolve illness absorption: APPSolve absorbs unplanned absence (illness, family responsibility leave) of up to 3 business days per named resource per calendar month without commercial impact on the client. Unplanned absence within this limit is covered by APPSolve's internal team on a best-efforts basis. The minimum monthly hours commitment is maintained within a reasonable tolerance of ±5% over the monthly period. (EBS-DRM-BU-003 RESOLVED — 3-business-day illness absorption limit confirmed as standard; WP15F 2026-06-19)

**EBS-DRM-036**
Illness exceeding 3 days: where a named resource is absent due to illness for more than 3 consecutive business days, APPSolve activates its substitution procedure per EBS-DRM-040. The substitute resource is engaged within 2 business days of the named resource's 4th consecutive day of absence. The client is notified of the substitution.

**EBS-DRM-037**
Leave and minimum hours: planned annual leave of a named resource in a given month reduces the named resource's available hours for that month below the minimum. Where the leave reduces the resource's available hours to below 80% of the monthly minimum, APPSolve provides a supplementary resource for the shortfall hours at no additional cost to the client. Where the shortfall is less than 20%, APPSolve manages the priority of work internally to deliver the highest-value items within the available hours.

**EBS-DRM-038**
South African public holidays: South African public holidays are excluded from DRM business hours per AMS-HRS-001. Where a public holiday falls on a day where the client requires DRM coverage (for example, a payroll run scheduled on a public holiday), the client requests coverage a minimum of 5 business days in advance. Public holiday coverage is provided at the contracted overtime or public holiday rate.

---

## Overlay Section 9: Resource Substitution

**EBS-DRM-039**
Permanent substitution (planned): APPSolve may permanently substitute a named DRM resource with a replacement of equivalent or higher grade where: (a) the named resource resigns or is terminated; (b) the named resource is promoted to a role that takes them out of AMS delivery; or (c) the named resource and APPSolve mutually agree a role change. APPSolve provides the client with a minimum of 30 days' advance written notice for planned permanent substitutions. (EBS-DRM-BU-004 RESOLVED — 30-day calendar notice confirmed; WP15F 2026-06-19)

**EBS-DRM-040**
Client approval right: the client has the right to meet with and assess a proposed permanent replacement before the replacement assumes the named role. The client assessment (competency discussion or practical assessment) is completed within 10 business days of APPSolve's nomination. Where the client objects to a proposed replacement on reasonable grounds related to skills or experience, APPSolve provides an alternative nomination within 10 business days.

**EBS-DRM-041**
Equivalent grade definition: a replacement resource is considered equivalent grade if they hold: (a) the same or greater years of Oracle EBS experience in the relevant functional or technical domain; (b) the same or greater certifications or qualifications relevant to the role; and (c) demonstrated client-facing AMS experience. Equivalent grade is confirmed as role band equivalence — a replacement meets the standard if they occupy the same or higher role band in APPSolve's grade structure within the relevant EBS domain. (EBS-DRM-BU-004 RESOLVED — equivalent grade = role band confirmed; WP15F 2026-06-19)

**EBS-DRM-042**
Emergency substitution: where a named resource becomes unavailable with no advance notice (serious illness, incapacitation, immediate resignation), APPSolve appoints an Acting resource within 2 business days. The Acting resource may be of interim grade (not necessarily equivalent) for the period while APPSolve identifies and assesses a permanent replacement. The permanent replacement process per EBS-DRM-039 applies within 30 days of the emergency substitution.

**EBS-DRM-043**
Substitution KT period: for planned permanent substitutions, the outgoing named resource and the incoming replacement resource conduct a 30-day knowledge transfer per EBS-DRM-050 through EBS-DRM-055, overlapping where possible. For emergency substitutions, KT is conducted on a best-efforts basis using available runbook documentation.

---

## Overlay Section 10: Knowledge Transfer and Onboarding

**EBS-DRM-044**
Initial DRM onboarding period: for a new DRM engagement, the first 30 calendar days are designated as the knowledge transfer and onboarding period. During this period, the DRM team establishes: system access for all named resources; run books and environment documentation; escalation contacts on both sides; support system configuration; and familiarity with the client's EBS environment and business processes.

**EBS-DRM-045**
Runbook creation obligation: as part of the initial DRM onboarding (or the DRM KT on a resource substitution), the relevant named resource creates and maintains a client-specific runbook for their domain. Runbook creation is a standard deliverable in all EBS AMS DRM engagements — not conditional on client request. The SDM maintains the master DRM runbook. Runbooks are stored in APPSolve's document management system and a copy is provided to the client on request. Runbooks are reviewed and updated quarterly. (EBS-DRM-BU-005 RESOLVED — 30-day KT period and runbook creation confirmed as standard in all DRM engagements; WP15F 2026-06-19)

**EBS-DRM-046**
Runbook domains: minimum runbook coverage per role: (a) SDM: client contact list, escalation tree, SLA summary, governance calendar, change register, active OARs; (b) DBA/OCI Specialist: EBS database configuration, OCI environment diagram (where applicable), backup schedule, patch history, access credentials register (stored securely, not in the runbook body); (c) HCM Functional Lead: HCM module configuration, payroll calendar, integration summary (EBS–PaySpace), key reports; (d) Finance Functional Lead: Finance module configuration, period-end checklist, bank interface details, chart of accounts summary; (e) Technical/OIC Specialist: OIC integration inventory, BeBanking integration map (where applicable), technical customisation log.

**EBS-DRM-047**
Client environment documentation: within 30 days of DRM commencement, APPSolve delivers an EBS Environment Summary document to the client. This document covers: EBS version and patch level; database version; OCI environment topology (where applicable); custom objects (RICE/CEMLI) inventory; OIC integration list; active interfaces; and known open issues. The client reviews and approves the document. It is maintained and updated quarterly.

**EBS-DRM-048**
Offboarding KT: where the DRM agreement is terminated (for any reason), APPSolve provides a 30-day transition period from the date of termination notice, during which: (a) the DRM team continues to provide support at the contracted service level; (b) runbooks and documentation are updated to current state and handed to the client; (c) the SDM facilitates a transition briefing with the client's designated successor team or internal team; (d) APPSolve's system access is removed in a managed, agreed sequence to avoid disruption.

---

## Overlay Section 11: Client Governance Meetings

**EBS-DRM-049**
Weekly operational call: the SDM facilitates a weekly operational stand-up (30 minutes, maximum) with the client's AMS Relationship Owner and relevant DRM team members. Agenda: open tickets status; upcoming planned work; resource availability for the week; any at-risk items. Minutes are recorded and distributed within 1 business day of the call.

**EBS-DRM-050**
Monthly SLA review meeting: the SDM facilitates a monthly SLA review meeting (60 minutes) with the client's AMS Relationship Owner. Agenda: SLA performance for the month (by priority tier); hours consumed vs. minimum by role; incident analysis (top 5 by frequency or business impact); change request pipeline; open OARs; proactive recommendations. The monthly SLA report is circulated 2 business days before the monthly meeting.

**EBS-DRM-051**
Quarterly service review: the SDM facilitates a quarterly business review (QBR, 90 minutes) with the client's AMS Relationship Owner and the client's senior stakeholder (CIO, IT Manager, or CFO as applicable). Agenda: quarterly SLA trends; service health assessment; strategic roadmap advisory; upcoming Oracle releases or patches relevant to the client's environment; contract performance review; renewal discussion (where approaching contract term). The QBR presentation is circulated 5 business days before the meeting.

**EBS-DRM-052**
Meeting cancellation policy: where the client cancels a scheduled governance meeting, APPSolve offers a rescheduled meeting within 5 business days of the cancelled date. Where a meeting is cancelled by APPSolve, APPSolve reschedules within 2 business days and circulates any outstanding reports as a written update in lieu of the meeting. Persistent cancellation of governance meetings (3 or more in a rolling quarter by either party) is noted in the QBR as a governance risk.

**EBS-DRM-053**
Meeting hours: SDM governance meeting hours (preparation, facilitation, follow-up) are charged against the SDM's minimum monthly hours. They do not constitute additional billable hours. Where DRM team members attend governance meetings, the attendance hours are charged against their respective role minimums.

---

## Overlay Section 12: Monthly DRM Report

**EBS-DRM-054**
Monthly DRM report delivery: APPSolve delivers the Monthly DRM Report to the client's AMS Relationship Owner by the 5th business day of the following month. The report covers the calendar month of the preceding month. The SDM owns the report.

**EBS-DRM-055**
Monthly DRM report content: (a) SLA performance (per priority tier, per EBS-SLA-053); (b) Hours consumed vs. minimum by role — actual hours, minimum, variance, and reason for material variance (>10%); (c) Ticket summary — count by priority by status (open, closed, in-progress); (d) Incident highlight — top 3 incidents by business impact with resolution summary; (e) Proactive maintenance completed; (f) Change requests — approved, in-progress, completed; (g) Open action items; (h) Next month's planned activities; (i) Resource availability and leave schedule for the coming month.

**EBS-DRM-056**
Hours underspend notification: where any named resource's actual hours in a given month are tracking below 80% of the monthly minimum by the 20th of the month, the SDM notifies the client in writing and proposes activities (from the client's backlog or proactive work queue) to utilise the remaining committed hours. The client may direct the underspend hours or accept them as elapsed.

**EBS-DRM-057**
Report format: the Monthly DRM Report is delivered in PDF format (or the client's preferred format as agreed at DRM commencement). The raw data supporting the report (ticket logs, time entries) is available to the client on request or via the self-service dashboard per EBS-DRM-032.

---

## Overlay Section 13: Out-of-Scope Handling

**EBS-DRM-058**
Out-of-scope identification: where a client request falls outside the contracted DRM scope (as defined in the AMS agreement and this overlay), the SDM identifies the out-of-scope item within 1 business day of the request, notifies the client in writing, and provides a preliminary effort estimate for the out-of-scope work as a Change Request.

**EBS-DRM-059**
CR commercials: out-of-scope work is delivered under a Change Request (CR) at the contracted change request rate per role. The CR is approved by the client's designated approver before APPSolve commences. The CR hours are in addition to the contracted minimum hours and are invoiced separately at the end of the month.

**EBS-DRM-060**
Out-of-scope examples: items always treated as out of scope for EBS AMS DRM include: new EBS module implementations; major EBS upgrades; custom report development; new OIC integration builds; data migration; DR testing; licence procurement; payroll processing (client-executed, with APPSolve advisory only); RICE/CEMLI development; and third-party application support (unless explicitly included in the AMS agreement).

**EBS-DRM-061**
Strategic advisory hours: where the DRM agreement includes a strategic advisory component (architecture review, EBS roadmap planning, upgrade assessment), the hours and scope of the strategic advisory service are defined in the AMS agreement. Strategic advisory hours are separate from the incident-and-service-request DRM minimum hours.

---

## Overlay Section 14: Resource Onboarding and Offboarding

**EBS-DRM-062**
System access provisioning: APPSolve requires the following access for DRM team members to deliver service: (a) Oracle EBS: named user accounts with relevant module access per role; (b) Oracle support portal (My Oracle Support): CSI customer support identifier access for SR management; (c) OCI Console: DBA+OCI Specialist requires OCI tenancy access at the resource level required for EBS database and infrastructure management; (d) APPSolve support system: configured as the client's support channel; (e) Client document management system (read access): for environment documentation and runbook storage. All access is provisioned by the client within 5 business days of DRM commencement. Failure to provision access delays the DRM commencement date by an equivalent period and the SLA clock does not begin until access is complete.

---

## Applied Decision Register

> **All 5 BU Lead decisions resolved WP15F 2026-06-19. Pack status: Approved v1.0.**

| Decision ID | Question | Resolution | Status |
|---|---|---|---|
| EBS-DRM-BU-001 | Is the ARM IT045 model (SDM 40h, HCM Lead 240h, Finance Lead 160h, DBA+OCI 160h, OIC 80h) the EBS AMS DRM standard, or configured per engagement? | Per-engagement model confirmed; ARM IT045 hours are reference architecture only; actual minimums defined in AMS agreement schedule. Applied to EBS-DRM-005/012/016/017/021/025. | **RESOLVED — WP15F 2026-06-19** |
| EBS-DRM-BU-002 | Do unused minimum hours in a given month roll over to the following month, or are they forfeited? | Rollover model confirmed; unused minimum hours roll over to the following month; expire at end of month N+1 if unconsumed. Applied to EBS-DRM-030. | **RESOLVED — WP15F 2026-06-19** |
| EBS-DRM-BU-003 | Is the 3-business-day illness absorption limit and 10-business-day advance leave notice the APPSolve DRM standard? | Confirmed as standard across all EBS AMS DRM engagements. Applied to EBS-DRM-034/035. | **RESOLVED — WP15F 2026-06-19** |
| EBS-DRM-BU-004 | Is 30 days the minimum resource substitution notice period, and is "equivalent grade" defined by role band or named competency profile? | 30 calendar days confirmed (all 30-business-day references replaced). Equivalent grade = role band. Applied to EBS-DRM-039/041/042. | **RESOLVED — WP15F 2026-06-19** |
| EBS-DRM-BU-005 | Is the 30-day KT period and runbook creation obligation included in all DRM engagements as standard, or only on client request? | Standard in all DRM engagements confirmed; not conditional on client request. Applied to EBS-DRM-045. | **RESOLVED — WP15F 2026-06-19** |

---

*EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.0 | Created: WP15D 2026-06-18 | Promoted Approved v1.0: WP15F 2026-06-19*
*62 assumptions across Sections 1–14 | Overlay Pack — applies to Oracle EBS AMS with named/dedicated resource model*
*Parent pack: AMS_ASSUMPTIONS_V1.md | Do not use standalone — load alongside base AMS pack*
*Replaces: AMS-SLA-005 when assembled | Also supplements EBS_AMS_SLA_OVERLAY_V1.md when both are active*
*All 5 BU Lead decisions resolved: EBS-DRM-BU-001–005 (WP15F 2026-06-19) | approved_for_reuse: true*
