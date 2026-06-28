---
document_id: EBS-AMS-SLA-OVERLAY-V1
title: "APPSolve EBS AMS — SLA Assumptions Overlay Pack"
version: "1.0"
status: "Approved v1.0 — all BU Lead decisions resolved; WP15F 2026-06-19"
created: "2026-06-18"
created_by: "WP15D — EBS AMS Remediation Programme"
promoted: "2026-06-19"
promoted_by: "WP15F — EBS AMS Overlay Promotion"
classification: "Overlay Pack — additive to AMS_ASSUMPTIONS_V1.md"
parent_pack: "AMS_ASSUMPTIONS_V1.md"
applies_to: "Oracle EBS AMS engagements where non-standard SLA commitments are required"
override_assumptions: "AMS-SLA-001, AMS-SLA-002, AMS-PRI-001, AMS-PRI-002, AMS-PRI-003"
assumption_count: 53
bu_lead_decisions_resolved:
  - "EBS-SLA-BU-001 RESOLVED WP15F 2026-06-19: P1 15-min response is client-configurable; confirmed in AMS agreement schedule per engagement"
  - "EBS-SLA-BU-002 RESOLVED WP15F 2026-06-19: Option B — resolution SLAs on explicit client request only; Section 4 is a conditional overlay section"
  - "EBS-SLA-BU-003 RESOLVED WP15F 2026-06-19: Fixed monthly premium model confirmed; no per-callout unless agreed in writing"
  - "EBS-SLA-BU-004 RESOLVED WP15F 2026-06-19: Option C — service credits negotiate per engagement; not a standard inclusion"
approved_for_reuse: true
lifecycle_status: APPROVED
---

# APPSolve EBS AMS — SLA Assumptions Overlay Pack

**Pack type:** Overlay — additive to `AMS_ASSUMPTIONS_V1.md`
**Applies to:** Oracle EBS AMS engagements (EBS R11, R12.1, R12.2) where the client specifies a non-standard SLA structure
**Status:** Approved v1.0 — all 4 BU Lead decisions resolved (WP15F 2026-06-19); approved for use in EBS AMS tenders with non-standard SLA requirements

> **Overlay principle:** This pack SUPPLEMENTS and where stated REPLACES specific assumptions in the base AMS pack. Assumptions EBS-SLA-001 through EBS-SLA-052 are additive unless the assumption header explicitly states "[REPLACES: AMS-XXX-NNN]". Where a replacement is stated, the base AMS assumption is suppressed for the duration of the EBS AMS engagement. All non-replaced AMS base assumptions remain in force.
>
> **Do not use this overlay for Oracle Fusion SaaS AMS engagements.** The base AMS pack governs Oracle Fusion. This overlay is specific to EBS on-premises or EBS on OCI environments.

---

## Overlay Section 1: Purpose, Scope, and Precedence

**EBS-SLA-001**
This SLA Assumptions Overlay applies to APPSolve AMS engagements where Oracle EBS (R11, R12.1, or R12.2) is the supported application, and where the client specifies service level commitments that differ from APPSolve's standard AMS SLA defined in AMS-SLA-001 and AMS-PRI-001 of the base AMS pack. This overlay is assembled alongside the base AMS pack; it does not replace the base pack in its entirety.

**EBS-SLA-002 [REPLACES: AMS-SLA-001]**
For EBS AMS engagements using this overlay, the standard AMS response times in AMS-SLA-001 (P1=1 hour, P2=4 business hours, P3=1 business day, P4=3 business days) are superseded by the five-priority SLA tier defined in EBS-SLA-010 through EBS-SLA-014 of this overlay. The base AMS pack four-priority model does not apply where this overlay is assembled.

**EBS-SLA-003**
SLA commitments in this overlay — including response times, resolution times, and 24/7 coverage obligations — apply only where they are explicitly included in the signed AMS agreement. No SLA commitment in this overlay is automatically included unless stated in the commercial agreement. The overlay defines the available SLA positions; the specific targets agreed with a given client are confirmed in the AMS SOW or AMS agreement schedule.

---

## Overlay Section 2: Five-Priority Tier Definitions

**EBS-SLA-004 [REPLACES: AMS-PRI-001]**
EBS AMS engagements using this overlay adopt a five-priority severity classification (P1 through P5). All five tiers are active from the commencement date of the AMS agreement. The priority of a ticket is assigned by the client at the time of logging and may be reclassified by APPSolve per EBS-SLA-008.

**EBS-SLA-005 — P1 Critical**
P1 Critical: the EBS application is completely unavailable to all users; payroll processing is blocked and a pay run is imminent or in progress; Oracle Financial period-end processing is blocked and a statutory reporting deadline is at risk; all OIC or BeBanking integrations have failed and payment runs, bank reconciliations, or inter-company transactions cannot proceed; or data integrity has been compromised and financial records are at risk. P1 requires immediate action and triggers the 24/7 on-call escalation regardless of the time of day or day of week.

**EBS-SLA-006 — P2 Major**
P2 Major: a significant function or module is impaired affecting a material user population; a critical business process (accounts payable run, payroll pre-close, inter-company reconciliation, bank payment authorisation) cannot be completed; a major OIC or BeBanking integration is failing but a manual workaround exists; or a single critical user (CFO, Payroll Manager, Finance Director) is completely locked out of a mission-critical function. P2 requires same-day resolution and, where it occurs outside business hours with 24/7 contracted, triggers the after-hours response procedure.

**EBS-SLA-007 — P3 Normal**
P3 Normal: a non-critical function or a non-mission-critical process is impaired; a subset of users is affected with a practical workaround available; a report is producing incorrect results for non-period-end use; a workflow is not routing correctly for lower-value transactions; or a service request is required for a time-sensitive but non-emergency configuration change. P3 is resolved within business hours at the contracted response and resolution targets.

**EBS-SLA-008 — P4 Minor**
P4 Minor: a low-impact cosmetic issue; a non-urgent configuration question that does not block a business process; a minor report formatting issue; an individual user access query; a non-urgent service request for which the client has no immediate deadline. P4 is planned and delivered within the standard resolution window.

**EBS-SLA-009 — P5 Minimal**
P5 Minimal: a general how-to question that does not require configuration change; a documentation request; an enquiry about EBS functionality; a request for explanation of an existing report result; a non-urgent product advisory question. P5 is addressed in the normal course of monthly support operations and does not carry an SLA response obligation beyond the P5 response target.

**EBS-SLA-010 — Priority Reclassification**
APPSolve may reclassify a ticket from the client-assigned priority where the actual business impact assessed during initial investigation materially differs from the assigned priority. Reclassification in either direction (upgrade or downgrade) is communicated to the client's designated AMS contact at the time of reclassification with the reason recorded in the ticket. Where the client disputes a downgrade, the AMS Account Manager or SDM resolves the classification dispute within two (2) business hours. The SLA clock is not reset on reclassification; it runs from original ticket logging.

---

## Overlay Section 3: Response Time Commitments

**EBS-SLA-011 [REPLACES: AMS-PRI-001, AMS-PRI-002, AMS-PRI-003]**
Response time is the elapsed time from ticket logging to APPSolve's first substantive response — an acknowledgement of receipt, a request for information, an initial diagnosis, or the assignment of an engineer to the incident. Response time is not resolution time. The response time targets for EBS AMS engagements using this overlay are:

| Priority | Response Target |
|---|---|
| P1 — Critical | 15 minutes from ticket logging (24 hours a day, 7 days a week) — client-configurable; specific target confirmed in AMS agreement schedule |
| P2 — Major | 1 hour (within contracted support hours; or 24/7 where contracted) |
| P3 — Normal | 4 business hours |
| P4 — Minor | 8 business hours |
| P5 — Minimal | 3 business days |

> **EBS-SLA-BU-001 RESOLVED (WP15F 2026-06-19):** The P1 15-minute response target is the EBS AMS reference position and applies where 24/7 P1 coverage is contracted. The target is client-configurable — confirmed per engagement in the AMS agreement schedule and not automatically applied as a universal default.

**EBS-SLA-012**
The P1 15-minute response target applies regardless of the day, time, or public holiday status. Where P1 24/7 coverage is contracted, the APPSolve on-call resource must acknowledge the P1 incident within 15 minutes of the ticket being logged or the automated alert being triggered. Where 24/7 coverage is not contracted, APPSolve acknowledges P1 tickets logged outside business hours at the start of the next business day; the 15-minute target applies only within contracted support hours unless 24/7 is in the agreement.

**EBS-SLA-013**
The P2 1-hour response target applies within contracted business hours. Where P2 24/7 response is included in the AMS agreement, the 1-hour target applies at all hours. P2 tickets logged outside business hours under a standard (business-hours) agreement start the SLA clock at 08:00 SAST on the next business day.

**EBS-SLA-014**
Response time measurement: APPSolve's support system timestamps the first outbound communication from an APPSolve resource against the ticket. The timestamp of the client's ticket creation is the SLA start time. Where a ticket is created by automated monitoring (where monitoring is contracted), the SLA start time is the automated alert timestamp.

**EBS-SLA-015**
SLA response performance is reported in the monthly support report per EBS-SLA-050. Where a response SLA is missed, the reason is documented in the report. Persistent P1 or P2 response SLA misses (two or more in any rolling 3-month period) trigger a service review meeting within five (5) business days.

---

## Overlay Section 4: Resolution Time Commitments

> **EBS-SLA-BU-002 RESOLVED — Option B (WP15F 2026-06-19):** Resolution time SLAs apply only on explicit client request. Assumptions EBS-SLA-016 through EBS-SLA-020 are conditional overlay sections — they apply only where resolution time commitments are explicitly contracted in the AMS agreement. Where the AMS agreement includes only response time SLAs (Section 3), this section does not apply and no resolution SLA breach is recorded.

**EBS-SLA-016**
Resolution time commitments define the target elapsed time from ticket logging to confirmed resolution — meaning the application function is restored to the agreed operating state and the client has confirmed, or APPSolve has demonstrated, that the incident has been fully resolved. Resolution time is measured from initial ticket logging and includes any SLA clock pause periods per EBS-SLA-030 through EBS-SLA-034.

**EBS-SLA-017**
Where resolution time SLAs are contracted, the resolution time targets for EBS AMS engagements are:

| Priority | Resolution Target |
|---|---|
| P1 — Critical | 2 hours (restore to operational status) |
| P2 — Major | 4 hours |
| P3 — Normal | 8 business hours |
| P4 — Minor | 16 business hours |
| P5 — Minimal | 5 business days |

**EBS-SLA-018**
Resolution time commitments apply only where explicitly included in the AMS agreement. Where the AMS agreement includes response time SLAs but not resolution time SLAs, APPSolve commits to response time only. Resolution effort is always prioritised in order of severity, but without contractual resolution time commitments, no SLA breach is recorded against resolution timing alone.

**EBS-SLA-019**
P1 resolution is defined as: the application function that triggered the P1 is restored to operational status sufficient to unblock the affected business process. P1 resolution does not require root cause elimination — a validated workaround that restores operations constitutes resolution for P1 SLA purposes. Full root cause correction may be delivered in a subsequent P3 or CR under the agreed root cause timeline.

**EBS-SLA-020**
Resolution extension: where a P1 or P2 incident cannot be resolved within the contracted resolution window — due to Oracle Support escalation, infrastructure root cause, or a factor outside APPSolve's direct control — APPSolve notifies the client's designated AMS contact and SDM (where applicable) at the expiry of the resolution window with an updated resolution estimate and the reason for the extension. Extension notification does not extinguish the SLA breach; it is recorded and reported.

---

## Overlay Section 5: 24/7 Coverage Model

**EBS-SLA-021**
24/7 P1 coverage is available as a contracted AMS add-on. Where 24/7 P1 coverage is included in the AMS agreement, APPSolve maintains an on-call resource for P1 EBS incidents at all hours, including evenings, weekends, and South African public holidays. 24/7 coverage does not apply to P2, P3, P4, or P5 under the standard 24/7 P1 model.

**EBS-SLA-022**
Where 24/7 P1 and P2 coverage is contracted, APPSolve provides an on-call resource available for both P1 and P2 incidents at all hours. The P1 15-minute response and P2 1-hour response targets apply at all hours. Additional commercial terms (on-call premium, after-hours rate) are defined in the AMS agreement.

**EBS-SLA-023**
The 24/7 on-call resource is an APPSolve AMS consultant with direct knowledge of the client's EBS configuration. The specific on-call roster is maintained by APPSolve's AMS Account Manager. The client receives the after-hours emergency contact number for direct on-call access. The emergency contact number is updated whenever the on-call roster changes.

**EBS-SLA-024**
After-hours P1 activation procedure: (1) Client logs a P1 ticket in the support system AND (2) calls the emergency contact number. Logging alone without the call does not guarantee 15-minute activation outside business hours. Where automated monitoring is contracted, a P1 monitoring alert activates the on-call resource without client call.

**EBS-SLA-025**
After-hours commercial model: APPSolve's confirmed 24/7 on-call commercial structure is a fixed monthly premium. After-hours on-call availability is included in the contracted 24/7 monthly fee. No separate per-callout charge applies — all after-hours callout work is covered within the fixed monthly premium. Where a specific engagement requires a different commercial structure, this must be agreed in writing in the AMS agreement as an exception to the fixed premium standard. (EBS-SLA-BU-003 RESOLVED — fixed monthly premium model confirmed; WP15F 2026-06-19)

**EBS-SLA-026**
24/7 coverage for planned payroll runs: where a client payroll run is scheduled outside standard business hours (for example, overnight batch payroll processing), and the client has contracted 24/7 P1 coverage, APPSolve's on-call resource is available to respond to EBS or OIC failures that block the payroll batch. The client notifies APPSolve of payroll run schedules at the start of each month.

**EBS-SLA-027**
24/7 coverage exclusions: 24/7 coverage under this overlay covers P1 (and P2 if contracted) EBS application incidents only. It does not cover: Acumatica or BeBanking incidents (separate AMS agreements apply); client IT infrastructure incidents (client's IT team responsibility); Oracle SaaS platform incidents (Oracle responsibility); or enhancement or project work.

---

## Overlay Section 6: After-Hours Emergency Escalation

**EBS-SLA-028**
After-hours escalation tree: for P1 incidents outside business hours, APPSolve follows the escalation tree documented in the AMS agreement. The standard escalation sequence is: (Level 1) on-call AMS consultant; (Level 2) AMS Account Manager or SDM (if applicable); (Level 3) APPSolve Oracle BU Lead or Technical Lead; (Level 4) APPSolve Managing Director. Each level is engaged if the previous level does not acknowledge within 30 minutes.

**EBS-SLA-029**
Client escalation mirror: the client designates a corresponding after-hours escalation tree — including a named 24/7 contact for P1 declarations (typically the IT Manager or ERP Manager). Without a client 24/7 contact, APPSolve cannot engage the client for P1 resolution steps (access provision, environment decisions, test authorisation) outside business hours. The absence of a client 24/7 contact suspends the SLA clock for time spent awaiting client engagement per EBS-SLA-031.

---

## Overlay Section 7: Major Incident Management

**EBS-SLA-035**
A Major Incident is a P1 incident that has not been resolved within the P1 resolution window, or a P1 incident affecting all users across all client sites simultaneously, or a P1 incident that has a confirmed regulatory, financial reporting, or payroll processing deadline impact. All Major Incidents trigger the Major Incident Management (MIM) process.

**EBS-SLA-036**
MIM war room: APPSolve convenes a conference bridge or virtual war room within 30 minutes of P1 declaration. The client is invited immediately. The bridge remains open until the P1 is resolved. Attendance: APPSolve on-call consultant, APPSolve AMS Account Manager or SDM, client's designated AMS contact, and any technical specialists required.

**EBS-SLA-037**
P1 status updates: APPSolve provides status updates to the client's designated AMS contact at 30-minute intervals for the duration of an active P1 incident. Updates include: current status, actions taken, next steps, estimated resolution time (where determinable), and whether Oracle Support has been engaged.

**EBS-SLA-038**
Executive communication: for P1 incidents exceeding 2 hours without resolution (or immediately if payroll is blocked on a pay run date), APPSolve's AMS Account Manager or Oracle BU Lead notifies the client's CIO, CFO, or designated executive contact. Executive communication is in writing (email) with a verbal brief. Executive communication is maintained every 2 hours thereafter until resolution.

**EBS-SLA-039**
Post-P1 debrief: within 5 business days of P1 resolution, APPSolve and the client conduct a post-incident review call (30 minutes) to review the incident timeline, validate the root cause, and agree on prevention measures. This debrief is separate from and precedes the formal RCA document.

---

## Overlay Section 8: SLA Clock Rules

**EBS-SLA-030 [REPLACES: AMS-SLA-002, AMS-SLA-003]**
SLA clock start: the SLA clock starts at the timestamp of ticket creation in APPSolve's support system — either client-logged or auto-generated by monitoring (where contracted). For P1 incidents with 24/7 coverage, the clock runs continuously. For P2, P3, P4, and P5 under business-hours SLAs, the clock runs only during contracted support hours.

**EBS-SLA-031**
SLA clock pause — client dependency: the SLA clock is paused when APPSolve is actively waiting for client action required to proceed with investigation or resolution. Pause conditions: client has not provided required information requested in writing; client has not granted requested system or environment access; client has not approved a required configuration change; client test environment is unavailable despite being required for resolution. The pause commences when APPSolve documents the dependency in the ticket and notifies the client. The clock resumes when the client fulfils the dependency.

**EBS-SLA-032**
SLA clock pause — Oracle SR: the SLA clock is paused for the period during which an Oracle Support SR is the blocking dependency. Pause commences when APPSolve lodges the Oracle SR and notifies the client. The clock resumes when Oracle provides the required patch, fix, or resolution and APPSolve commences implementation. Oracle SR pause time is documented in the monthly report.

**EBS-SLA-033**
SLA clock pause — maintenance window: the SLA clock is paused during agreed maintenance windows per EBS-SLA-040 through EBS-SLA-043.

**EBS-SLA-034**
SLA clock pause — force majeure: the SLA clock is paused during force majeure events that prevent APPSolve from providing service. Force majeure events are communicated to the client in writing as soon as practicable. The pause does not apply to events that affect only the client's environment (network outage, power failure, hardware failure) as these are the client's IT team's responsibility.

---

## Overlay Section 9: Maintenance Windows and Planned Outages

**EBS-SLA-040**
Standard maintenance window: the default EBS AMS maintenance window is Sunday 00:00–06:00 SAST. During this window, APPSolve may apply configuration changes, EBS patch applications (where DBA scope is contracted), or integration maintenance without SLA obligation. The maintenance window is agreed in the AMS agreement and may be adjusted by mutual written agreement.

**EBS-SLA-041**
Advance notice for maintenance: APPSolve provides the client with a minimum of five (5) business days' advance notice for planned maintenance activities that require system downtime or application restart. The notice includes: maintenance scope, expected duration, expected impact on users, and the date/time of the maintenance window.

**EBS-SLA-042**
Emergency maintenance: where a critical security patch, Oracle-required emergency configuration change, or P1 resolution requires immediate system changes outside the standard maintenance window, APPSolve notifies the client's designated AMS contact as soon as practicable before commencing. Emergency maintenance notification is by telephone followed immediately by written confirmation.

**EBS-SLA-043**
Client-requested downtime: where the client requires planned downtime outside the standard maintenance window (for example, for an internal audit, a data migration, or a DR test), the client provides APPSolve with a minimum of 10 business days' advance notice. SLA is suspended during client-requested downtime where agreed in advance in writing.

---

## Overlay Section 10: Root Cause Analysis (RCA) Obligations

**EBS-SLA-044**
RCA for P1 incidents: APPSolve delivers a written RCA report to the client within five (5) business days of P1 resolution. The RCA report covers: incident timeline (detection to resolution); root cause analysis; contributing factors; immediate corrective actions taken; preventive measures recommended and agreed; and follow-on actions with owners and due dates.

**EBS-SLA-045**
RCA for P2 incidents: APPSolve delivers a written RCA report for P2 incidents on request from the client. The report is delivered within ten (10) business days of the request. Not all P2 incidents require a formal RCA — the client designates which P2 incidents warrant a formal RCA at the time of ticket closure.

**EBS-SLA-046**
RCA format: the RCA report uses the 5-Why or fishbone methodology. It documents the technical root cause, any contributing process or human factors, and the recommended preventive action. Where Oracle is the root cause (Oracle bug, Oracle infrastructure failure), the RCA documents the Oracle SR reference, the Oracle diagnosis, and the workaround applied pending Oracle's permanent fix.

**EBS-SLA-047**
RCA follow-on actions: where an RCA identifies a configuration change, process change, or monitoring requirement as a preventive action, APPSolve provides an effort estimate for implementing the recommendation. The client decides whether to proceed. Preventive actions are tracked in the monthly report until closed.

---

## Overlay Section 11: Service Credits

**EBS-SLA-048**
Service credits (negotiate per engagement): service credits are available as a negotiated commercial option in EBS AMS agreements and are not a standard inclusion. Where service credits are negotiated and included in the AMS agreement, and APPSolve fails to meet the contracted P1 response or resolution SLA in a given month, the client is entitled to a service credit calculated as a percentage of the applicable monthly AMS fee. The credit percentage, monthly cap, and SLA breach trigger conditions are defined through negotiation and confirmed in the AMS agreement. Service credits are the client's exclusive remedy for SLA failures and are applied to the following month's invoice. (EBS-SLA-BU-004 RESOLVED — Option C: negotiate per engagement confirmed; WP15F 2026-06-19)

**EBS-SLA-049**
Service credit exclusions: service credits do not apply where an SLA miss is attributable to: client dependency pause per EBS-SLA-031; Oracle SR blocking per EBS-SLA-032; force majeure per EBS-SLA-034; a client-initiated change that caused the incident; or where the client did not activate the P1 emergency call procedure per EBS-SLA-024. Credits are applied only for SLA breaches within APPSolve's direct control.

**EBS-SLA-050**
Service credit claim process: service credits are not applied automatically. The client submits a credit claim in writing (email to the AMS Account Manager or SDM) within 10 business days of the SLA breach. APPSolve reviews the claim against the support system data within 5 business days and confirms the credit or provides the reason for exclusion. Undisputed credits are applied to the next invoice.

---

## Overlay Section 12: Client Dependency Clauses

**EBS-SLA-051**
Response and resolution SLA commitments are contingent on the client fulfilling its obligations under the AMS agreement. Key client dependencies that, if unmet, suspend SLA obligations: (a) designated AMS contact available during business hours; (b) P1 24/7 contact available for after-hours P1 incidents where 24/7 is contracted; (c) system access provisioned for the APPSolve AMS team prior to engagement commencement; (d) test environment available for APPSolve testing where required for resolution; (e) client CSI access provided for Oracle SR management.

**EBS-SLA-052**
Change approval timing: where an incident or service request resolution requires the client to approve a configuration change before APPSolve can implement it, the SLA clock is paused from the time APPSolve submits the change approval request to the time the client approves. For P1 and P2 incidents, APPSolve requires a response to configuration change approval requests within 30 minutes during P1 and within 2 hours during P2. Delay in approval beyond these times is documented as a client dependency pause.

---

## Overlay Section 13: SLA Reporting

**EBS-SLA-053**
Monthly SLA report (EBS AMS): in addition to the standard AMS monthly report (AMS-REP-001), EBS AMS engagements using this overlay include the following SLA-specific content in the monthly report: (a) ticket count by priority tier (P1–P5); (b) response SLA compliance rate per priority; (c) resolution SLA compliance rate per priority (where resolution SLAs are contracted); (d) SLA pauses: total pause minutes per priority per ticket, with reason; (e) P1 incident log: each P1 with date, duration, root cause category, and resolution; (f) service credit position: credits earned and applied (where applicable).

---

## Applied Decision Register

> **All 4 BU Lead decisions resolved WP15F 2026-06-19. Pack status: Approved v1.0.**

| Decision ID | Question | Resolution | Status |
|---|---|---|---|
| EBS-SLA-BU-001 | Is the P1 15-minute response target the EBS AMS standard, or is it client-negotiable? | Client-configurable; 15 minutes is the EBS AMS reference position confirmed in the AMS agreement schedule per engagement. Applied to EBS-SLA-011. | **RESOLVED — WP15F 2026-06-19** |
| EBS-SLA-BU-002 | Does APPSolve commit to resolution time SLAs as a default offering, or only on explicit client request? | Option B — on explicit client request only. EBS-SLA-016–020 are conditional overlay sections; Section 4 header note added. | **RESOLVED — WP15F 2026-06-19** |
| EBS-SLA-BU-003 | What is the commercial structure for 24/7 on-call? Fixed monthly premium, per-callout fee, or hybrid? | Fixed monthly premium model confirmed. Per-callout interpretation removed from EBS-SLA-025. | **RESOLVED — WP15F 2026-06-19** |
| EBS-SLA-BU-004 | Does APPSolve offer SLA service credits as a standard option, or only where specifically negotiated with the client? | Option C — negotiate per engagement. EBS-SLA-048 updated to reflect negotiated-only position. | **RESOLVED — WP15F 2026-06-19** |

---

*EBS_AMS_SLA_OVERLAY_V1.0 | Created: WP15D 2026-06-18 | Promoted Approved v1.0: WP15F 2026-06-19*
*53 assumptions across Sections 1–13 | Overlay Pack — applies to Oracle EBS AMS with non-standard SLA requirements*
*Parent pack: AMS_ASSUMPTIONS_V1.md | Do not use standalone — load alongside base AMS pack*
*Replaces: AMS-SLA-001, AMS-SLA-002, AMS-PRI-001, AMS-PRI-002, AMS-PRI-003 when assembled*
*All 4 BU Lead decisions resolved: EBS-SLA-BU-001–004 (WP15F 2026-06-19) | approved_for_reuse: true*
