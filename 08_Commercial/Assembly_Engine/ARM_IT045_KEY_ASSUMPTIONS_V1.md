---
document_id: ARM-IT045-KEY-ASSUMPTIONS
title: "ARM IT045 — Key Assumptions and Client Obligations"
version: "1.0"
status: "Approved — Client Ready"
generated: "2026-06-24"
generated_by: "WP17D-1 — Inline Text Assembly Engine"
pattern: "EBS AMS Full Stack"
tender_id: "ARM IT045"
client: "African Rainbow Minerals"
category: "Assembly Engine Output — Proposal Body Insert"
body_assumptions: 175
complete_schedule_assumptions: 594
---

# ARM IT045 — Key Assumptions and Client Obligations

**Client:** African Rainbow Minerals  
**Tender Reference:** ARM IT045  
**Solution Pattern:** EBS AMS Full Stack  
**Document Version:** 1.0  
**Generated:** 2026-06-24  
**Status:** Client Ready — Proposal Body Insert  

---

> The following assumptions represent the key assumptions relevant to scope, dependencies, client obligations and exclusions. They are a subset of the Complete Assumption Schedule included in Appendix X. The Complete Assumption Schedule forms part of this proposal and takes precedence where duplication or interpretation differences exist.

---

This section presents the key commercial assumptions, service management definitions, client obligations, and explicit exclusions that govern this engagement. These assumptions form part of the complete Assumption Schedule provided in Appendix X.

**The complete Assumption Schedule in Appendix X contains all 594 governing assumptions and is incorporated by reference as a binding component of this proposal. Engagement of APPSolve's services constitutes client acknowledgement and acceptance of all assumptions in Appendix X.**

---

## Sub-section 1: Engagement and Commercial Assumptions

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

320. Enhancements — adding new functionality, new configuration, new modules, new integrations, or new reports beyond the contracted application scope — are excluded from AMS. Enhancements are delivered as project work under a separate project SOW. *(Ref: AMS-ENH-001)*

321. Where the client requests an enhancement during an AMS support interaction, APPSolve identifies it as an enhancement, logs it, and advises the client that it requires a separate project engagement. APPSolve does not absorb enhancement work into the AMS hours without explicit commercial agreement. *(Ref: AMS-ENH-002)*

322. Enhancement identification: APPSolve's obligation is to tell the client when a request crosses the enhancement boundary. APPSolve is not responsible for the client's decision about whether to proceed with the enhancement or when to schedule it. *(Ref: AMS-ENH-003)*

323. Where a client-requested configuration change is ambiguous (could be interpreted as support or enhancement), APPSolve escalates to the AMS Account Manager and the client's designated AMS contact for classification before work commences. Agreed classifications are logged in the monthly report. *(Ref: AMS-ENH-004)*

324. A change request (CR) is a formally scoped and approved work item that constitutes new or changed scope beyond the standard service request catalogue. The standard CR threshold is 2 hours: changes estimated at more than 2 hours of effort require a formal written CR, an effort estimate, and written client approval before work commences. APPSolve may, at its discretion, absorb changes estimated below 2 hours into the monthly support hours without raising a formal CR. No entitlement to this discretionary treatment is created by previous practice — each case is assessed independently. The CR threshold defined in a specific AMS agreement takes precedence over this standard. *(Ref: AMS-CR-001)*

325. The change request process: (1) Client submits change request description via the support channel; (2) APPSolve assesses and produces a written effort estimate within five (5) business days; (3) Client approves the estimate in writing; (4) APPSolve schedules and delivers the change; (5) Client signs off delivery. No change request work commences without written client approval of the estimate. *(Ref: AMS-CR-002)*

326. Change requests are not subject to the incident SLA. CR delivery timelines are agreed at the time of CR approval based on complexity, resource availability, and the client's priority. APPSolve provides a delivery date at the time of CR approval. *(Ref: AMS-CR-003)*

327. Change requests that introduce risk to the live production system (for example, security role changes affecting multiple users, workflow restructuring, GL period-end configuration changes) are assessed by APPSolve for risk before implementation and require a testing confirmation from the client before production deployment. *(Ref: AMS-CR-004)*

---

## Sub-section 2: Service Management and SLA Summary

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

---

## Sub-section 3: Client Responsibilities

> The following assumptions define obligations on the Client that are conditions of the engagement. APPSolve's commercial position, timeline, and pricing are contingent on the Client fulfilling these obligations as described. Material deviation from these obligations may require scope, timeline, or commercial renegotiation.

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

## Sub-section 4: Explicit Exclusions

> The following items are explicitly excluded from the scope of this engagement. Requests to include excluded items will be treated as change requests and priced separately. APPSolve has no obligation to perform any activity described in this section without a signed change order.

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

> *The complete Assumption Schedule for this engagement is provided in Appendix X. All 594 assumptions listed therein apply to this engagement regardless of whether they appear in this summary section. Please review Appendix X in full before executing this proposal.*

---

*ARM_IT045_KEY_ASSUMPTIONS_V1.md | WP17D-1 | 2026-06-24*  
*175 body assumptions selected from 594 net | EBS AMS Full Stack | ARM IT045*  
*Generated by APPSolve Assembly Engine — Option B Dual-Output Mode v1.1*