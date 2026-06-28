---
document_id: W3S1-007-ORA-WorkforceManagement
title: "Oracle Workforce Management — Capability Statement"
version: "1.1 Approved"
status: "Approved"
review_status: "Approved"
approved_for_reuse: "Yes"
lifecycle_status: APPROVED
business_unit: "Oracle"
wave: "3"
deliverable: "W3S1-007"
created: "2026-06-13"
approved: "2026-06-13"
created_by: "Claude (AI — Wave 3 W3S1-007 extraction)"
approved_by: "Hein Blignaut (BU Lead)"
source_document: "HIST-006 (SAA HCM RFP Response, June 2025 — platform capability narrative); HIST-007 (Hollywood Bets V5.0, April 2023 — Absence Management Phase 1 evidence; Biometric integration); HIST-015 (Afrocentric HCM Proposal V4.0, 2023 — T&L delivery assumptions; Phase 3.3.1); HIST-016 (SABS ETS Oracle Fusion, Dec 2025 — Mr Price T&L PoC evidence; Mr Price Absence evidence); ORACLE_FACT_BASELINE Sections 4.1, 19, 21"
source_status: "Tier 1 (HB Absence confirmed implementation); Tier 1 PoC (Mr Price T&L proof-of-concept); Tier 2 Platform Capability (HIST-006 — T&L, Scheduling, H&S, Mobile); Active Pipeline (Redpath Mining — Absence); Delivery Methodology (HIST-015 — T&L assumptions)"
prereq_statement: "W3S1-001-ORA-HCMCore (Oracle HCM Core — Global HR is the mandatory prerequisite and foundation for all Workforce Management modules; Absence Management is included within Oracle Fusion HCM; Time and Labor is included within Oracle Fusion HCM)"
kb_destination: "06_Capabilities/Oracle/Oracle_HCM/"
tags: "Oracle,HCM,Workforce Management,Absence Management,Time and Labor,Workforce Scheduling,Health and Safety,Mobile,Self-Service,Biometric,Leave Management"
---

> **APPROVED — approved_for_reuse: Yes — Approved by BU Lead 2026-06-13**

---

# Oracle Workforce Management

**Capability Statement | APPSolve | Oracle Business Unit**
*Document ID: W3S1-007-ORA-WorkforceManagement | Version: 1.1 Approved | Wave 3*

---

## Section 1: Statement of Capability

APPSolve configures and implements Oracle Workforce Management capabilities across the full spectrum of workforce administration — from daily absence tracking and leave management through to time and labor capture, workforce scheduling, and manager self-service workforce operations.

Oracle Fusion HCM's Workforce Management suite comprises four primary capability areas that work together to provide organisations with comprehensive, rules-driven workforce administration:

| Capability Area | Module | Licensing | APPSolve positioning |
|---|---|---|---|
| **Absence Management** | Oracle Absence Management | Included in Oracle HCM | **Confirmed delivery** — standard in every Oracle HCM implementation |
| **Time and Labor** | Oracle Time and Labor | Included in Oracle HCM | **Confirmed capability (PoC evidence)** — implemented as part of a proof-of-concept programme; APPSolve has confirmed functional and technical readiness for production delivery |
| **Workforce Scheduling** | Oracle Workforce Scheduling | Included in Oracle HCM | **Platform Capability** — APPSolve can configure and implement where required and in scope |
| **Workforce Health and Safety** | Oracle Workforce Health and Safety | Included in Oracle HCM | **Platform Capability** — APPSolve can support and configure where required and in scope |

Absence Management is APPSolve's most consistently implemented Oracle Workforce Management module — it is configured as a standard Phase 1 deliverable in every Oracle Fusion HCM implementation engagement. Oracle Time and Labor has been implemented by APPSolve as part of a proof-of-concept programme for a South African retail client, confirming APPSolve's functional and technical capability to deliver T&L in production environments.

APPSolve's Oracle practice includes certified HCM consultants with implementation experience across Absence Management in retail, mining, and professional services sectors. The practice's mobile-first deployment approach enables employee self-service absence and time management from any device, reducing administrative burden on HR teams while improving data accuracy and compliance.

---

## Section 2: Oracle Workforce Management Architecture — Module Scope and Boundaries

### 2.1 Module Architecture

Oracle Fusion HCM Workforce Management is the collective term for the capabilities that govern how employees' time, attendance, leave, and workplace safety are managed within the Oracle HCM platform. Each capability is a configurable module within Oracle Fusion HCM.

**Module dependency and sequencing:**

Workforce Management modules are deployed following Core HR (W3S1-001). Core HR establishes the foundational structures — legal entities, business units, departments, jobs, positions, and employee records — on which all Workforce Management modules depend.

```
Core HR (W3S1-001)
    ├── Absence Management  ← Phase 1 in every HCM implementation
    ├── Time and Labor      ← Phase 2+ where in scope
    ├── Workforce Scheduling ← Where in scope
    └── Workforce H&S       ← Where in scope
```

### 2.2 Absence Management within Workforce Management

Absence Management is the foundational Workforce Management module. It is always implemented in Phase 1 of an Oracle HCM programme, alongside Core HR. Absence Management establishes the leave framework — absence types, accrual rules, entitlements, and self-service processes — that all subsequent phases depend on.

In implementations where Time and Labor is in scope, Absence Management and Time and Labor work in conjunction: absence is tracked within Absence Management and flows to Time and Labor for accurate time validation and payroll processing.

### 2.3 Integration Architecture

All Oracle Workforce Management modules are integrated by design within Oracle Fusion HCM. The integration architecture follows the standard APPSolve Oracle HCM deployment model:

```
Oracle Absence Management ──► Oracle Time and Labor ──► Oracle Payroll / HCM Extracts ──► OIC ──► Payroll Platform
Oracle Workforce Scheduling ──► Oracle Time and Labor (schedule drives time expectations)
Oracle HCM Mobile App ──► All modules (self-service and approval workflows)
Biometric / Access Control System ──► OIC ──► Oracle Time and Labor (time capture)
```

---

## Section 3: Absence Management

### 3.1 Overview

Oracle Absence Management is a comprehensive, cloud-based leave and absence management solution included within Oracle Fusion HCM. It provides organisations with a configurable, rules-driven framework to define, administer, and track all types of employee absence — from annual leave and sick leave to statutory leave types prescribed under South African labour law.

APPSolve configures and implements Oracle Absence Management as a standard deliverable in every Oracle Fusion HCM implementation. It is positioned in Phase 1 of the APPSolve implementation approach, alongside Core HR, because the leave framework underpins the entire Oracle HCM employee experience from day one of go-live.

> **Confirmed implementation reference:** APPSolve's Oracle HCM implementation for a major South African retail and gaming client (go-live July 2025, 7,000 users) included Oracle Absence Management as a Phase 1 deliverable. APPSolve is currently implementing Oracle HCM Absence Management for a mining-sector client as part of an active Oracle HCM programme.

### 3.2 Absence Management Capabilities

| Capability | Description | Notes |
|---|---|---|
| **Absence plan configuration** | Define absence plans for each leave type — annual leave, sick leave, family responsibility, maternity, parental, study leave, bereavement, and other statutory and discretionary leave types | SA-specific plans configured per BCEA requirements |
| **Accrual rules** | Configure accrual rates, accrual frequency (daily, monthly, anniversary), and accrual caps per plan. Accruals calculated automatically based on employee tenure, grade, and assignment | APPSolve configures accrual rules as a standard design deliverable |
| **Leave entitlements** | Define minimum entitlements, carry-over rules, maximum balance caps, and expiry rules per absence type | BCEA statutory minimums enforced |
| **Multiple absence plans per employee** | Employees can hold concurrent absence plans — annual leave, sick leave, maternity simultaneously managed | Standard Oracle Fusion capability |
| **Employee self-service leave requests** | Employees submit leave requests through the Oracle HCM self-service portal or mobile app. Team calendars and personal absence balances visible at point of submission | Reduces HR administrative overhead |
| **Manager approval workflows** | Configurable approval chains — line manager, HR Business Partner, or multi-level. Managers approve, deny, or request modification from self-service or mobile app | Standard workflow — configurable per leave type |
| **Real-time balance visibility** | Employee and manager see real-time leave balances at any point. Oracle HCM calculates entitlements, consumed leave, and projected balance including pending requests | |
| **Team absence calendar** | Managers view team leave calendar to assess coverage before approving leave requests. Absence conflicts flagged | Manager self-service standard feature |
| **HR override and correction** | HR administrators can adjust leave balances, create retroactive absence records, and correct historical entries | Role-based access control governs who can adjust |
| **Absence integration with payroll** | Approved absence transactions flow to payroll (Oracle Payroll Cloud or third-party payroll via HCM Extracts or OIC) for accurate payroll processing — deductions, leave pay-outs, and absence-based payments | Standard integration in every implementation |
| **Audit trail** | Full audit trail of all absence requests, approvals, balance adjustments, and corrections | Governance and compliance standard |
| **Reporting (OTBI)** | OTBI subject areas for absence: leave balances, absence trends, leave liability, top absence types, absenteeism rate, team availability | Standard OTBI — cross-reference W3S1-006 for OAX analytics |

### 3.3 South African Legislative Absence Requirements

APPSolve configures Oracle Absence Management to comply with South African labour legislation. Key SA statutory requirements configured as standard:

| Statutory requirement | Legislation | Configuration |
|---|---|---|
| **Annual leave** | BCEA Section 20 — minimum 15 working days per annual leave cycle (or 1.25 days per month) | Accrual plan configured per BCEA minimum; employer policies apply additional entitlements |
| **Sick leave** | BCEA Section 22 — 30 days in 3-year cycle; 1 day per 26 days worked in first 6 months | Two-tier sick leave plan configured: initial period + full cycle |
| **Family responsibility leave** | BCEA Section 27 — 3 days per year on birth, illness, or death of family members | Entitlement plan configured |
| **Maternity leave** | BCEA Section 25 — 4 consecutive months | Maternity absence plan configured; payroll treatment confirmed during design |
| **Parental leave** | BCEA Section 25A — 10 consecutive days | Parental leave plan configured |
| **Unpaid leave** | By agreement with employer | Configurable plan with nil accrual |
| **Public holidays** | Public Holidays Act — 13 SA public holidays | Oracle Fusion Work Schedules and Absence Management handle public holiday interactions |

**Legislative assumption (standing):** Legislative-specific absence requirements must be documented in a standardised format by the client before the absence plan configuration workshop. APPSolve configures plans to the agreed documented standard.

### 3.4 Employee and Manager Self-Service

| Self-Service Capability | User | Description |
|---|---|---|
| Submit leave request | Employee | Submit any absence type through self-service portal or mobile app; view current balance before submitting |
| View leave balances | Employee | Real-time personal balance per absence plan at any time |
| View absence history | Employee | Full history of all absence requests and their approval status |
| Cancel leave request | Employee | Cancel a pending or approved future absence (subject to policy) |
| Approve / deny leave request | Manager | Review request in context of team calendar; approve, deny, or request modification |
| Submit absence on behalf | Manager | HR administrator or manager submits an absence entry on behalf of an employee where required |
| View team absence calendar | Manager | Full team view of approved and pending leave — visibility before approving new requests |
| Leave balance enquiry | Employee / Manager | View any team member's current balance and leave history (within data access profile) |
| Notification and alerts | All | Automated workflow notifications — request submitted, approved, denied, balance approaching limit |

### 3.5 APPSolve Absence Management Delivery

APPSolve applies a structured delivery approach to Absence Management within every Oracle HCM implementation:

| Delivery activity | Phase | Description |
|---|---|---|
| Absence requirements workshop | Scope and Design | Capture all leave types, accrual rules, entitlements, carry-over, expiry, and payroll treatment. Document legislative requirements in standardised format. |
| Work schedule design | Scope and Design | Define standard work schedules (patterns, hours, shift patterns where applicable) — foundation for absence accruals and time calculations |
| Absence plan configuration | Build | Configure each absence plan per agreed design. Accrual rules, entitlements, eligibility profiles, qualification periods. |
| Approval workflow configuration | Build | Configure approval chains per absence type. Build notification templates. |
| OTBI absence reports | Build | Configure standard OTBI absence reports — balance reports, absence trend, leave liability, team calendar. Develop custom reports per requirements. |
| Payroll integration for absence | Build | Configure HCM Extracts or OIC interface to pass approved absence transactions to payroll platform |
| UAT — absence scenarios | Deploy | Test all absence types: standard request, carry-over, balance depletion, approval rejection, payroll calculation |
| User training | Deploy | Train employees (self-service) and managers (approvals, team calendar) during deployment |
| First-cycle support | Post go-live | Hyper-care support during first leave cycle — assist with any accrual, balance, or payroll issues arising in live operation |

---

## Section 4: Oracle Time and Labor

### 4.1 Overview

Oracle Time and Labor (T&L) is a comprehensive, cloud-based time management solution included within Oracle Fusion HCM. It captures, manages, and validates time worked by employees across an organisation — supporting both exempt and non-exempt workers, standard and shift-based working patterns, and complex overtime and labor compliance rules.

Oracle Time and Labor provides a flexible, rules-driven engine that enables organisations to accurately track hours worked, enforce time and attendance policies, comply with labor legislation (BCEA working time provisions), and integrate time data seamlessly with payroll, absence management, and project costing.

APPSolve implemented Oracle Time and Labor capabilities as part of a proof-of-concept programme for a South African retail client. This engagement confirmed APPSolve's functional and technical readiness to configure and deliver Oracle Time and Labor in production Oracle HCM environments.

### 4.2 Oracle Time and Labor Capabilities

| Capability | Description |
|---|---|
| **Time entry methods** | Employees enter time via: (1) web-based timecard in the Oracle HCM self-service portal; (2) Oracle HCM Mobile App time entry; (3) physical biometric device or access control system via OIC integration; (4) manager entry on behalf of employees |
| **Configurable timecard layout** | Timecard layouts configured per working pattern — daily entry, weekly summary, project-based, cost centre-based. Fields and prompts driven by business rules. |
| **Work schedule integration** | Oracle Work Schedules define expected working patterns per employee. Time and Labor validates actual time against the expected schedule — flagging deviations for manager review. |
| **Absence integration** | Approved absences in Oracle Absence Management flow into Time and Labor automatically — absence periods appear in the timecard; no duplicate entry required. |
| **Overtime rules engine** | Configurable overtime rules — daily overtime threshold, weekly overtime threshold, shift premium rates, BCEA-compliant overtime calculation. Rules engine applies the correct overtime rate automatically. |
| **Time approval workflows** | Configurable timecard approval workflows — employee submits, line manager approves. Multi-level approvals supported. Automated reminders for missing or late timecards. |
| **Manager timecard management** | Managers view, edit (within policy), approve, and submit timecards for their team. Missing timecard alerts for direct reports. Bulk approval for teams with standard schedules. |
| **Labor policy compliance** | Enforces BCEA provisions on maximum working hours, minimum rest periods, and overtime entitlements. Policy violations flagged on the timecard before submission. |
| **Payroll integration** | Approved time data — standard hours, overtime, premiums, shift differentials — flows to Oracle Payroll Cloud or third-party payroll via HCM Extracts or OIC. Ensures accurate pay calculation based on time actually worked. |
| **Project costing integration** | Where Oracle Project Costing or Project Portfolio Management is in scope, Time and Labor passes labor hours to project cost accounts — enabling accurate project labor cost tracking. |
| **Shift differential and premium pay** | Configure shift differentials and premium pay rates (night shift, public holiday, weekend) within the Time and Labor rules engine. Applied automatically to timecards meeting the trigger conditions. |
| **Retroactive time corrections** | Corrections to submitted timecards processed retroactively — payroll recalculation triggers automatically for the affected periods. |
| **OTBI time reporting** | Pre-built OTBI subject areas for time: hours worked by employee/department/cost centre, overtime analysis, timecard completion rates, labor cost by period — cross-reference W3S1-006 for analytics. |

### 4.3 Time and Labor Rules Engine

Oracle Time and Labor's rules-driven engine is one of its core differentiators. Complex time policies — shift premiums, overtime thresholds, public holiday rates, consecutive day rules — are configured as time rules applied automatically on each timecard.

| Rules Engine Capability | Description |
|---|---|
| **Time categories** | Define time categories (regular, overtime, shift premium, public holiday, night shift) — the basis for payroll costing and reporting |
| **Time rules** | Rules evaluate time entries against defined conditions (time of day, day of week, consecutive hours, weekly totals) and apply the correct time category automatically |
| **Shift differentials** | Shift premium rates (e.g., 25% shift allowance, 150% overtime rate, 200% public holiday rate) attached to time categories and applied by rules |
| **BCEA overtime calculation** | Oracle T&L is configured to enforce BCEA-compliant overtime: daily threshold (daily hours beyond 9 ordinary hours), weekly threshold (beyond 45 ordinary hours per week), maximum overtime limits (10 hours per week) |
| **Union/collective agreement rules** | Where collective agreements or bargaining council agreements apply, time rules encode the specific overtime, shift, and premium provisions of the applicable agreement |
| **Period-end processing** | Time is periodically processed to produce payroll-ready time data — rules evaluated for the full period, exceptions resolved before payroll runs |

### 4.4 Time and Labor in APPSolve Implementations

**Proof-of-concept reference:**
APPSolve implemented Oracle Time and Labor capabilities as part of a proof-of-concept programme for a South African retail client. This engagement validated APPSolve's technical and functional capability to configure Oracle Time and Labor, including timecard design, rules engine configuration, and integration architecture. The client did not proceed from proof-of-concept to full production deployment.

**Active pipeline — Time and Labor delivery readiness:**
APPSolve's Oracle HCM practice includes consultants with Oracle Time and Labor configuration and delivery capability. Time and Labor is a confirmed in-scope module for Oracle HCM implementations where time tracking, overtime management, or biometric integration requirements are present.

**APPSolve T&L delivery principles:**

| Principle | Description |
|---|---|
| **No data migration** | Oracle Time and Labor does not require historical time data migration. All time entry starts fresh from go-live date. |
| **Common business rules** | T&L configuration is based on a documented, agreed set of business rules applied consistently across the Oracle HCM instance. Multiple rule sets are supported but increase configuration and testing effort. |
| **Payroll integration in scope** | The only mandatory external integration for T&L is to the payroll system. Additional integrations to time logging/access control systems are configured where a biometric or external time device is in scope. |
| **Biometric as OIC integration** | Biometric and access control system integrations are implemented as OIC interfaces — a confirmed APPSolve capability (Hollywood Bets biometric integration as precedent). |

---

## Section 5: Workforce Scheduling

### 5.1 Overview

Oracle Fusion Workforce Scheduling is a cloud-based workforce scheduling solution within the Oracle Fusion HCM suite. It enables organisations to manage labor resources by aligning workforce schedules with operational demands — ensuring the right employees are scheduled at the right times while maintaining compliance with labor laws, collective agreements, and organisational policies.

Oracle Workforce Scheduling is designed for industries with complex staffing requirements — retail (multi-shift, high-volume, seasonal demand), manufacturing (production scheduling, shift rotations), and healthcare (clinical and support staff rostering). It provides managers with demand-driven scheduling tools, employee self-service shift preferences, and integration with Oracle Time and Labor and Absence Management for end-to-end workforce management.

APPSolve positions Oracle Workforce Scheduling as a platform capability — APPSolve has the product knowledge and technical capability to configure and implement Oracle Workforce Scheduling where it is in scope and required by the client.

### 5.2 Oracle Workforce Scheduling Capabilities

| Capability | Description |
|---|---|
| **Demand-driven scheduling** | Build workforce schedules aligned to operational demand patterns — staffing to peak periods, minimum coverage requirements, and labour cost targets |
| **Schedule templates** | Define shift patterns and schedule templates per department, location, or job type. Apply templates to generate baseline schedules. |
| **Employee schedule management** | Assign employees to shifts; manage shift rotations, swap requests, and schedule adjustments |
| **Self-service shift preferences** | Employees indicate shift preferences and availability windows via self-service. Scheduling engine respects preferences where operationally feasible. |
| **Shift swap and cover requests** | Employees request shift swaps or volunteer for open shifts through self-service. Manager approval workflow configurable per policy. |
| **Labor law compliance in scheduling** | Configure maximum consecutive working days, minimum rest periods between shifts, weekly hour caps, and overtime triggers within the scheduling engine. Schedules validated against these rules before publication. |
| **Collective agreement rules** | Encode collective agreement scheduling provisions — e.g., shift rotation limits, guaranteed rest periods, public holiday scheduling rules |
| **Integration with Time and Labor** | Published employee schedules drive expected time in Oracle Time and Labor. Deviations between scheduled and actual time are flagged for manager review. |
| **Integration with Absence Management** | Approved absences flow to the scheduling engine — vacant slots identified and flagged for cover. |
| **Integration with Payroll** | Schedule data (shifts, premiums, differentials) flows to payroll via Oracle Time and Labor for accurate pay calculation |
| **Labor cost optimisation** | Schedule analytics — compare scheduled labor cost against budget; identify overtime exposure; optimise staffing mix to meet coverage at minimum cost |
| **Manager schedule dashboard** | Managers view team schedules, open shifts, absence conflicts, and labor cost exposure in a single workforce dashboard |

### 5.3 Oracle Workforce Scheduling — APPSolve Positioning

APPSolve can configure and implement Oracle Workforce Scheduling where it is identified as a client requirement during the HCM programme scoping phase.

Workforce Scheduling is particularly relevant for clients in:
- **Retail** — multi-location, variable-hours workforce; peak trading period scheduling; part-time and shift workers
- **Mining** — shift rotation management; safety-driven minimum rest period enforcement; underground vs surface scheduling
- **Manufacturing and distribution** — production shift scheduling; line and warehouse staffing
- **Healthcare** — clinical and support staff rostering; on-call management

APPSolve advises clients on Oracle Workforce Scheduling capabilities and fit during Oracle HCM programme planning. Where Workforce Scheduling is confirmed as in-scope, it is implemented as an additional workstream within the Oracle HCM programme.

**Pre-tender check:** Confirm whether the client's Oracle Workforce Scheduling licensing is in place before positioning Workforce Scheduling as a specific deliverable. Confirm Workforce Scheduling scope and licensing position with the Oracle account team at pre-sales.

---

## Section 6: Oracle Workforce Health and Safety

### 6.1 Overview

Oracle Fusion HCM includes Workforce Health and Safety capabilities that enable organisations to manage workplace safety events, incidents, and compliance obligations within the Oracle HCM platform. This capability is particularly relevant for industries where occupational health and safety management is a core operational requirement — mining, construction, manufacturing, and industrial services.

Oracle Workforce Health and Safety provides a structured case management and event tracking framework within Oracle HCM, connecting safety events to employee records for a unified view of workforce safety performance alongside HR data.

APPSolve positions Oracle Workforce Health and Safety as a platform capability — APPSolve can support and configure Oracle Workforce H&S capabilities where required and in scope as part of an Oracle HCM programme.

### 6.2 Oracle Workforce Health and Safety Capabilities

| Capability | Description |
|---|---|
| **Incident reporting** | Employees and supervisors report safety incidents, near-misses, and hazard observations through the Oracle HCM self-service portal or mobile app |
| **Incident case management** | Each reported incident becomes a structured case — tracked through investigation, corrective action, and closure stages |
| **Injury and illness tracking** | Record and track work-related injuries and illnesses — injury type, affected body part, cause, treatment, and recovery status |
| **Near-miss management** | Log and investigate near-miss events — root cause analysis, contributing factors, and corrective actions |
| **Safety inspection management** | Plan and record workplace safety inspections — inspection checklists, findings, risk ratings, and corrective action assignments |
| **Corrective action management** | Assign, track, and close corrective actions arising from incidents and inspections. Escalation workflows for overdue actions. |
| **OHSA compliance support** | Configuration to support Occupational Health and Safety Act (OHSA) and associated regulations in South Africa — incident notification requirements, injury records, COIDA-related event tracking |
| **Employee-level safety records** | Link safety events to employee profiles — view an individual employee's safety history within their HR record |
| **Safety analytics (OTBI)** | OTBI reporting for safety events — incident frequency rates, incident types, departments affected, corrective action status |
| **Mobile incident reporting** | Employees and supervisors can report incidents directly from the field using the Oracle HCM Mobile App — immediate capture without returning to a desktop |

### 6.3 Oracle Workforce H&S — APPSolve Positioning

APPSolve can configure and implement Oracle Workforce Health and Safety capabilities where they are identified as a client requirement. Workforce H&S configuration is an additional workstream within an Oracle HCM programme — it does not replace dedicated EHS (Environment, Health and Safety) systems but provides integrated safety event management within the Oracle HCM environment.

Oracle Workforce H&S is most relevant to APPSolve's Oracle HCM clients in:
- **Mining** — statutory OHSA/MHSA incident reporting requirements; shift-linked safety event tracking
- **Manufacturing and industrial services** — workplace safety compliance; contractor incident management
- **Any sector** where the client requires safety event management integrated with their HR system rather than a standalone EHS platform

**Pre-tender note:** Confirm whether the client's requirement is for Oracle Fusion HCM Workforce H&S or a dedicated EHS platform. Oracle Fusion HCM Workforce H&S handles incident reporting and case management within the HCM context — it is not a full environmental management or industrial hygiene platform. Where the client requires advanced EHS functionality, a dedicated EHS product (e.g., Oracle EHS Cloud, Intelex, Cority) may be more appropriate.

---

## Section 7: Mobile Workforce Capabilities

### 7.1 Overview

Oracle Fusion HCM is built on a mobile-first design principle. The Oracle HCM Cloud Mobile App (available for iOS and Android) provides employees and managers with access to all core Workforce Management capabilities from any device — enabling time capture, absence management, approvals, and workforce visibility regardless of location.

This is particularly relevant for Oracle HCM clients in industries with distributed, field-based, or shift-working populations — retail stores, mining operations, manufacturing floors, and remote sites — where employees may not have regular access to desktop workstations.

### 7.2 Mobile Time and Labor Capabilities

| Mobile T&L Capability | Description |
|---|---|
| **Mobile timecard entry** | Employees enter time directly from the mobile app — daily time entry, project-based time allocation, overtime codes |
| **Clock-in / clock-out (web clock)** | Mobile web clock capability — employees clock in and out via the Oracle HCM Mobile App; time stamps recorded directly to the timecard |
| **Manager timecard review and approval** | Managers review, edit (within policy), and approve team timecards from the mobile app. Bulk approval for teams with standard schedules. |
| **Overtime alerts** | Push notifications to employees and managers when overtime thresholds are approaching or exceeded |
| **Missing timecard alerts** | Automated alerts to employees with missing or incomplete timecards; manager visibility of non-compliant team members |
| **Payroll cutoff reminders** | Configurable reminders before payroll cutoff — prompting employees to submit and managers to approve outstanding timecards |

### 7.3 Mobile Absence Management Capabilities

| Mobile Absence Capability | Description |
|---|---|
| **Submit leave request** | Employees submit leave requests directly from the mobile app — select absence type, dates, include notes. Balance displayed before submission. |
| **View leave balances** | Real-time personal absence balances for all leave plans — accessible from the mobile app at any time |
| **View absence history** | Full history of all absence requests, approval status, and leave transactions |
| **Approve/deny leave requests** | Managers approve or deny leave requests directly from the mobile app — with team calendar context and coverage visibility |
| **Team calendar view** | Managers view team leave calendar from mobile — see who is on leave, who has pending requests, coverage gaps |
| **Cancel leave request** | Employees cancel pending or approved future leave requests from the mobile app |

### 7.4 Mobile Manager Self-Service

| Mobile Manager Capability | Description |
|---|---|
| **Team dashboard** | Manager's mobile view of team workforce status — who is present, absent, on leave, approaching overtime, with missing timecards |
| **Workforce approvals** | Single approvals queue for all pending team actions — leave requests, timecard approvals, overtime authorisations, from a unified mobile list |
| **Employee profile access** | Access to direct report employment details, leave balances, and assignment information from the mobile app |
| **Push notifications** | Receive real-time notifications for pending approvals — leave requests, timecards, overtime alerts — ensuring prompt action without accessing desktop |
| **Absence submission on behalf** | Submit absence entries on behalf of direct reports where required — manual or retroactive absence recording |

### 7.5 Mobile Workforce Scheduling

| Mobile Scheduling Capability | Description |
|---|---|
| **View published schedule** | Employees view their published shifts and schedule from the mobile app — upcoming shifts, schedule changes, shift assignments |
| **Shift preference submission** | Employees indicate shift preferences and availability from the mobile app |
| **Shift swap requests** | Request shift swaps with colleagues via mobile; manager approval workflow follows |
| **Open shift notifications** | Push notifications to eligible employees when open shifts are available for cover |

---

## Section 8: Manager Self-Service and Workforce Visibility

### 8.1 Manager Self-Service Overview

Oracle Fusion HCM provides managers with a comprehensive self-service capability that covers the full spectrum of workforce administration actions — from absence approvals and time management through to workforce composition visibility and HR action initiation. Manager self-service reduces the administrative burden on HR teams by enabling managers to complete routine workforce transactions without HR intermediation.

### 8.2 Workforce Management Actions Available to Managers

| Action Category | Capability |
|---|---|
| **Absence management** | Approve/deny leave requests; view team absence calendar; submit absence on behalf of employees; view individual leave balances and histories |
| **Time management** | Review and approve team timecards; identify missing or non-compliant timecards; view overtime exposure for team members |
| **Team visibility** | View direct reports' employment details, leave balances, performance status, and learning progress in a unified team view |
| **Workforce actions** | Initiate promotions, transfers, and terminations for direct reports — with approval workflows routing to HR and management stakeholders as configured |
| **Reporting structures** | View and navigate team organisational chart; understand matrix reporting lines; see delegation structures |
| **Absence on behalf** | Submit absence entries for direct reports where the employee is unable to do so — manual or retroactive |
| **Time on behalf** | Submit timecard entries for direct reports where required (subject to policy and role access) |
| **Notifications queue** | Unified notifications and approvals queue — all pending manager actions in one view |

### 8.3 Workforce Visibility Dashboards

Oracle Fusion HCM provides managers with embedded OTBI dashboards within the management self-service pages — giving real-time workforce visibility without navigating to a separate reporting tool:

| Dashboard | Content |
|---|---|
| **Team headcount** | Current team size; pending changes (new hires in pipeline, upcoming terminations, transfers) |
| **Team absence status** | Current absence (who is out today); upcoming approved leave; leave calendar coverage summary |
| **Timecard compliance** | Submitted vs missing timecards for the pay period; overtime alerts |
| **Workforce composition** | Team distribution by grade, job family, tenure, employment type |

---

## Section 9: Time Capture and Biometric Integration

### 9.1 Time Capture Methods

Oracle Time and Labor supports multiple time capture methods — catering for different work environments, working populations, and technology preferences:

| Time Capture Method | Description | Suitable for |
|---|---|---|
| **Web clock (browser)** | Employees clock in and out using a browser-based clock interface — simple, no additional hardware required | Office-based and desk-worker populations |
| **Mobile web clock** | Clock in/out from the Oracle HCM Mobile App — timestamped and GPS-aware (where configured) | Field-based, retail, and remote workers |
| **Manual timecard entry** | Employees enter time directly on a timecard (daily or weekly) — total hours, project allocation, overtime codes | Professional services, project-based workers |
| **Biometric device integration** | Employees clock in/out using biometric devices (fingerprint, facial recognition, access control) — data flows automatically to Oracle Time and Labor via OIC integration | Manufacturing, mining, retail (high-volume) |
| **Manager/HR entry on behalf** | Managers or HR submit time entries for employees who are unable to self-submit — for retrospective corrections or where employees lack system access | Operational and field workers |

### 9.2 Biometric System Integration

APPSolve has confirmed capability to integrate third-party biometric and access control systems with Oracle Time and Labor using Oracle Integration Cloud (OIC).

**Hollywood Bets implementation evidence:** The Hollywood Bets Oracle Fusion HCM implementation (go-live July 2025, 7,000 users) included a confirmed biometric system integration as a defined interface deliverable in the implementation Bill of Materials. The integration was implemented using OIC — APPSolve's standard Oracle Fusion integration layer.

**Integration architecture:**
```
Biometric / Access Control Device
        │
        ▼ (time stamp events — in/out)
OIC Integration Layer (APPSolve OIC implementation)
        │
        ▼
Oracle Time and Labor (time entries created per employee)
        │
        ▼
Oracle Payroll / HCM Extracts (payroll processing)
```

**Biometric integration scope:**
- Inbound: biometric device events (clock-in / clock-out) mapped to Oracle HCM employee records and imported as time entries
- Outbound: employee records (new hires, terminations, access changes) pushed from Oracle HCM to the biometric system to maintain device enrolment
- Error handling: mismatched or unrecognised biometric events flagged in the OIC integration for exception management

**Biometric integration governance note:** Biometric integration is a custom OIC interface delivered as an integration workstream within the Oracle HCM programme. It is not an Oracle standard product feature — it depends on the specific biometric system in scope, the system's API or data export capability, and the required two-way data flow. Integration scope and effort are confirmed during the Scope and Design phase.

---

## Section 10: Workforce Management Integration Architecture

### 10.1 Integration Points

Oracle Workforce Management modules are natively integrated within Oracle Fusion HCM. External integration points follow APPSolve's standard OIC-first architecture:

| Integration | Direction | Method | Standard |
|---|---|---|---|
| Absence Management → Payroll | Outbound | HCM Extracts or OIC | Standard in all implementations |
| Time and Labor → Payroll | Outbound | HCM Extracts or OIC | Standard where T&L in scope |
| Biometric System → Time and Labor | Inbound | OIC custom adapter | Implementation-specific |
| Oracle HCM → Biometric System (employee sync) | Outbound | OIC custom adapter | Implementation-specific |
| Workforce Scheduling → Time and Labor | Internal | Oracle native | Standard Oracle integration |
| Absence Management → Time and Labor | Internal | Oracle native | Standard Oracle integration |
| Oracle HCM → Project Costing | Internal / OIC | Oracle native or OIC | Where PPM in scope |

### 10.2 OIC as Standard Integration Layer

Oracle Integration Cloud (OIC) is the standard integration layer in all APPSolve Oracle Fusion HCM implementations. All external Workforce Management integrations — payroll, biometric systems, access control — are implemented through OIC. This provides:

- Centralised integration monitoring and error management
- Standardised API-based connectivity
- Audit trail for all data flows
- Reusable integration templates for common payroll connectors

---

## Section 11: APPSolve Delivery Capability

### 11.1 Oracle Workforce Management Practice

APPSolve's Oracle Business Unit includes HCM-certified consultants with confirmed delivery experience across Oracle Absence Management and Oracle Time and Labor within Oracle Fusion HCM implementations. APPSolve holds Oracle Level 1 Partner status with Oracle Integration as a published expertise area.

| Capability Area | Evidence | Confidence |
|---|---|---|
| Absence Management configuration | Hollywood Bets Phase 3.3.1 (confirmed go-live July 2025); Redpath Mining active implementation; Afrocentric delivery framework | **HIGH — confirmed delivery** |
| Absence Management (SA legislative) | BCEA-compliant plans configured in multiple implementations; Afrocentric multi-country assumption framework | **HIGH — confirmed** |
| Oracle Time and Labor configuration | Mr Price proof-of-concept implementation (South African retail sector) | **CONFIRMED — PoC evidence** |
| T&L rules engine configuration | Afrocentric T&L delivery assumptions; RedPath RFI technical capability statements | **CONFIRMED — delivery readiness** |
| Biometric OIC integration | Hollywood Bets BOM — biometric interface confirmed implementation deliverable | **CONFIRMED — implementation evidence** |
| OIC integration (general) | All Fusion implementations include OIC; RedPath RFI: "All our Fusion implementations... implemented Oracle Integration Cloud" | **HIGH — confirmed delivery** |
| Oracle Workforce Scheduling | Platform product knowledge; no confirmed implementation | **Platform knowledge — no delivery claim** |
| Oracle Workforce H&S | Platform product knowledge; no confirmed implementation | **Platform knowledge — no delivery claim** |
| Mobile self-service configuration | Standard in all HCM implementations — mobile-first design approach | **CONFIRMED — standard delivery** |

### 11.2 Delivery Principles

| Principle | Description |
|---|---|
| **Phase 1 — Absence always first** | Absence Management is always configured in Phase 1 alongside Core HR. The leave framework must be established before any subsequent module can be deployed. |
| **Rules-before-configuration** | Time and Labor business rules are documented and signed off before configuration begins. The rules document drives the configuration — avoiding scope creep during the Build phase. |
| **Standard-first principle** | Oracle delivered standard work schedules, absence plans, and timecard templates are reviewed first. Custom configuration only where standard Oracle content cannot satisfy the requirement. |
| **No T&L data migration** | Oracle Time and Labor does not require historical time data migration. All time entry starts from go-live. This principle applies universally. |
| **OIC-standard for payroll integration** | All Workforce Management-to-payroll integrations are implemented via OIC or HCM Extracts. Direct database-to-database integrations are not used. |
| **Biometric scope confirmation** | Biometric integration is confirmed as in or out of scope at project initiation. Biometric system API documentation must be provided by the client before OIC development begins. |

### 11.3 Resource and Delivery Model

| Resource Type | Role |
|---|---|
| HCM Principal Consultant | Absence and T&L design authority; rules documentation governance; client engagement leadership |
| HCM Senior Functional Consultant | Absence plan configuration; T&L rules engine configuration; work schedule design; OTBI reporting |
| HCM Technical Developer | OIC biometric integration; HCM Extracts for payroll; custom OTBI report development |
| OIC Integration Developer | Biometric system OIC interface development and testing (where biometric in scope) |
| Project Manager | Workforce Management workstream governance; scope and change management |

---

## Section 12: Implementation References

### 12.1 Oracle Absence Management — Hollywood Bets (Confirmed Implementation)

| Attribute | Detail |
|---|---|
| **Client** | Hollywood Bets |
| **Industry** | Retail / Gaming |
| **Absence scope** | Phase 3.3.1 "Human Capital (Core and Absence and Self Service)" — Absence Management configured and implemented as Phase 1 of the Oracle HCM programme |
| **Go-live** | July 2025 — 7,000 users |
| **Biometric integration** | Biometric system interface confirmed as a Phase 1 implementation deliverable (OIC-based) |
| **Reference status** | Referenceable — Hollywood Bets is confirmed Tier 1 Oracle HCM implementation reference |
| **Citation** | "APPSolve implemented Oracle HCM Absence Management for Hollywood Bets (go-live July 2025, 7,000 users), including biometric time capture integration." |

### 12.2 Oracle Absence Management — Mining Sector Active Pipeline

| Attribute | Detail |
|---|---|
| **Client** | Mining-sector client (active implementation — not yet live) |
| **Absence scope** | Oracle Absence Management confirmed in active implementation scope (RACI) |
| **Status** | Active implementation — not yet live — not referenceable (Rule 21.5) |
| **Citation rule** | Approved pipeline framing: "APPSolve is currently implementing Oracle Absence Management for a mining-sector client as part of an Oracle HCM programme." Client not named. |

### 12.3 Oracle Time and Labor — South African Retail Client (Proof of Concept)

| Attribute | Detail |
|---|---|
| **Client** | South African retail client (not named) |
| **T&L scope** | Oracle Time and Labor implemented as part of a proof-of-concept programme |
| **Outcome** | Proof-of-concept completed — client did not proceed to production deployment |
| **Evidence** | Confirms APPSolve's technical and functional capability to configure Oracle Time and Labor in an Oracle HCM environment |
| **Citation rule** | "APPSolve implemented Oracle Time and Labor capabilities as part of a proof-of-concept programme for a South African retail client." |
| **Prohibited** | "rollout", "go-live", "production deployment", "stores across South Africa", "live implementation" |

### 12.4 Workforce Scheduling and Health and Safety — Reference Position

No referenceable client implementation of Oracle Workforce Scheduling or Oracle Workforce Health and Safety exists at the time of this document. Both are positioned as Oracle platform capabilities that APPSolve can configure and implement where required and in scope.

---

## Section 13: Implementation Approach

### 13.1 Workforce Management within the Oracle HCM Programme

Workforce Management modules are phased within the standard APPSolve Oracle HCM programme structure. Phase sequencing is driven by the client's scope confirmation during the Mobilize phase.

| Phase | Workforce Management Activities |
|---|---|
| **Mobilize** | Confirm WFM scope: Absence only? T&L in scope? Biometric integration? Scheduling? H&S? Confirm biometric system and API availability. Document high-level leave types required. |
| **Scope and Design** | Absence requirements workshop — leave types, accruals, entitlements, carry-over, SA legislative types. T&L rules document — working hours, overtime thresholds, shift patterns, BCEA provisions. Work schedule design. Biometric integration specification (if in scope). Scheduling design (if in scope). |
| **Prototype** | CRP1: Absence plans configured; leave request and approval flows demonstrated. T&L: timecard layouts, basic rules, and approval workflow demonstrated (if in scope). CRP2: Full absence lifecycle tested; T&L rules engine validated with client scenarios; biometric integration tested in development (if in scope). |
| **Build** | Absence plans, entitlements, and workflows built to signed-off design. T&L rules engine built to signed-off rules document. OIC biometric interface developed and unit-tested (if in scope). OTBI absence and time reports developed. Payroll integration configured and tested. |
| **Deploy** | Absence UAT — all leave types tested; payroll integration tested; edge cases (carry-over, expiry, retroactive) tested. T&L UAT — all time scenarios tested; overtime calculations validated; biometric device testing (if in scope). User training — employees (self-service) and managers (approvals, dashboards). |
| **Post Go-Live** | First leave cycle support — absence balance accuracy; payroll integration exceptions. First T&L period-end support — period processing, payroll cutoff compliance. Biometric integration exception management. |

### 13.2 OUM Methodology

APPSolve applies the Oracle Unified Methodology (OUM) across all Oracle Fusion HCM implementations. Workforce Management deliverables are scoped, designed, built, tested, and deployed within the OUM phase structure. All Workforce Management scope changes after Build phase commencement are managed as formal change requests.

---

## Section 14: Risk Register

| Risk ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-W3-007-001 | Absence rules complexity — client has extensive bespoke absence rules (discretionary leave, industry-specific plans, union agreements) beyond standard SA legislative requirements; configuration effort significantly exceeds estimate | Medium | High | Absence requirements fully documented and signed off before Build begins. Standard vs custom plan boundaries agreed during Scope and Design. Bespoke plans scoped as separate cost items. |
| R-W3-007-002 | T&L rules complexity — complex shift patterns, multiple collective agreement variations, or location-specific overtime rules increase T&L rules engine effort | Medium | Medium | T&L rules document produced and signed off before T&L Build begins. Rule count and complexity governs effort estimate. |
| R-W3-007-003 | Biometric system API availability — biometric vendor does not provide API documentation or cannot expose a supported integration method; OIC integration delayed or blocked | Medium | High | Biometric system API documentation required from client before OIC development begins. Alternative: manual extract/import fallback confirmed during Scope and Design if API not available. |
| R-W3-007-004 | Biometric device enrolment data quality — employee records in biometric system do not match Oracle HCM employee records (different IDs, name variants, historical employees); matching logic must be designed and tested | High | Medium | Data mapping workshop between Oracle HCM and biometric system records before OIC development. Employee identifier used as the matching key must be agreed and validated. |
| R-W3-007-005 | BCEA overtime calculation complexity — client's overtime policy differs from BCEA standard (more generous entitlements, sector-specific agreements); additional rules required | Medium | Medium | Overtime rules confirmed during Scope and Design rules document session. BCEA minimum as floor; client-specific rules layered above. |
| R-W3-007-006 | Workforce Scheduling demand forecasting data — Scheduling implementation requires demand data (transaction volumes, customer footfall, production targets) to generate demand-driven schedules; if this data is unavailable or inaccurate, schedule quality is poor | Low | Medium | Scheduling demand data requirements confirmed during Scope and Design. If demand data unavailable, shift-pattern-based scheduling is an alternative (less optimal but functional). |

---

## Section 15: Assumptions Register

| Assumption ID | Assumption | Risk if incorrect |
|---|---|---|
| A-W7-001 | Absence plan types are confirmed and documented during Scope and Design before Build begins. APPSolve configures plans to the documented standard — undocumented absence requirements discovered during UAT are treated as change requests. | Late-discovered absence requirements delay go-live or increase cost |
| A-W7-002 | Legislative-specific absence requirements (BCEA, sector-specific) are provided by the client in a standardised format during Scope and Design. APPSolve configures to the provided standard; legal interpretation is the client's responsibility. | Incorrect legislative configuration; compliance risk |
| A-W7-003 | Time and Labor configuration is based on a common, agreed set of business rules applied across the Oracle HCM instance. If multiple distinct rule sets are required (e.g., per bargaining unit), effort is re-scoped accordingly. | Multiple rule sets significantly increase T&L Build effort |
| A-W7-004 | No historical time data is migrated into Oracle Time and Labor. All T&L data entry begins from the go-live date. | No risk — this is a firm constraint, not an assumption |
| A-W7-005 | Where biometric integration is in scope: the biometric system vendor provides API documentation before OIC development begins. The biometric system is operational in the production environment before OIC go-live testing. Employee identifier mapping between Oracle HCM and the biometric system is agreed during Scope and Design. | Biometric integration delay or scope change |
| A-W7-006 | The client will nominate a superuser / administrator for Absence Management and Time and Labor who participates in build validation and skills transfer. This individual owns ongoing absence plan administration and T&L rules management post go-live. | Ongoing dependency on APPSolve for routine absence and T&L administration |
| A-W7-007 | Workforce Scheduling (if in scope): demand data required for demand-driven scheduling is available and accurate. The client's minimum staffing requirements and labor cost targets are documented before Scheduling Build begins. | Poor schedule quality; potential re-scoping |
| A-W7-008 | Oracle Work Schedules defining standard working hours for each population are confirmed and signed off before Absence Management and Time and Labor configuration begins. Work Schedules are foundational inputs for both modules. | Absence accrual and T&L time validation errors if work schedules are incomplete or incorrect |

---

## Section 17: Approval Record

| Field | Value |
|---|---|
| **Document ID** | W3S1-007-ORA-WorkforceManagement |
| **Version** | 1.1 Approved |
| **Created** | 2026-06-13 |
| **Created by** | Claude (AI — Wave 3 W3S1-007 extraction) |
| **Status** | Approved — BU Lead approved 2026-06-13; all amendments applied (E-001, E-002, CROSS-1) |
| **Approved for reuse** | Yes — BU Lead approved 2026-06-13 |
| **Approved by** | Hein Blignaut (BU Lead) |
| **Approval date** | 2026-06-13 |
| **Open items at submission** | None — all 5 OI items (OI-W7-001 through OI-W7-005) CLOSED 2026-06-13 |
| **BU Lead** | Hein Blignaut |

---

## Appendix A: Source Mapping Table

| Section | Content type | Primary source | Governance classification |
|---|---|---|---|
| Section 1 | Capability overview; module hierarchy | HIST-007 BOM; HIST-016 Table 3; ORACLE_FACT_BASELINE Section 4.1 | Confirmed delivery (Absence); PoC evidence (T&L); Platform (Scheduling, H&S) |
| Section 2 | Architecture; module sequencing | HIST-006 para 333; HIST-007 para 147; HIST-015 para 193 | Platform architecture; delivery methodology |
| Section 3.1–3.2 | Absence Management overview and capabilities | HIST-006 paras 334–344 | Platform capability — reframed; SAA not named |
| Section 3.3 | SA legislative absence types | HIST-006 paras 788, 795; HIST-015 para 264; ORACLE_FACT_BASELINE | Platform capability; SA-specific |
| Section 3.4 | Absence self-service | HIST-006 paras 520–535 | Platform capability |
| Section 3.5 | APPSolve Absence delivery | HIST-007 para 147; Redpath RACI para 9; HIST-015 para 193 | Tier 1 (HB); Active pipeline (Redpath); Delivery methodology (Afrocentric) |
| Section 4.1–4.2 | T&L overview and capabilities | HIST-006 paras 216–232 | Platform capability — reframed; SAA not named |
| Section 4.3 | T&L rules engine | HIST-006 paras 218–226; HIST-015 paras 296–299 | Platform capability; delivery assumptions |
| Section 4.4 | T&L in APPSolve implementations | HIST-016 Table 3 (Mr Price); OI-W7-001 BU Lead decision | Tier 1 PoC — "proof-of-concept programme for a South African retail client"; Mr Price not named |
| Section 5 | Workforce Scheduling | HIST-006 paras 233–247 | Platform capability only — OI-W7-002 CLOSED |
| Section 6 | Workforce Health and Safety | Oracle platform knowledge; OI-W7-003 CLOSED | Platform capability only — no implementation evidence |
| Section 7 | Mobile capabilities | HIST-006 paras 538–550, 341 | Platform capability |
| Section 8 | Manager self-service | HIST-006 paras 520–535 | Platform capability |
| Section 9.1 | Time capture methods | HIST-006 para 341 | Platform capability |
| Section 9.2 | Biometric integration | HIST-007 para 64 | Tier 1 implementation evidence (Hollywood Bets) |
| Section 10 | Integration architecture | ORACLE_FACT_BASELINE Section 7; HIST-008 para 148 | OIC standard confirmed |
| Section 11 | Delivery capability | HIST-007; HIST-016; HIST-008 para 158 | Confirmed delivery evidence |
| Section 12.1 | Hollywood Bets Absence reference | HIST-007 paras 50–64, 147 | Tier 1 — referenceable |
| Section 12.2 | Redpath Mining pipeline | Redpath RACI para 9; Rule 21.5 | Pipeline — not named; not referenceable |
| Section 12.3 | Mr Price T&L PoC | HIST-016 Table 3; OI-W7-001 BU Lead decision | PoC evidence — not named; not production deployment |
| Section 12.4 | Scheduling and H&S reference position | OI-W7-002, OI-W7-003 BU Lead decisions | Platform capability — no reference client |
| Section 13 | Implementation approach | ORACLE_FACT_BASELINE Section 17 | OUM methodology standard |

**Prohibited sources — confirmed excluded:**
- CCBA (HIST-014) — SVR research only; no CCBA content extracted; CCBA never named
- SAA — not named; platform capability source only (reframed throughout)
- DFA — not named (Rule 21.4); DFA absence scope not confirmed with specific T&L evidence
- Redpath Mining — cited with approved pipeline framing only; not named; not completed (Rule 21.5)

---

## Appendix B: Governance Self-Review

**Wave 3 Standing Rules — Compliance Check (ORACLE_FACT_BASELINE Section 21)**

| Rule | Check | Status |
|---|---|---|
| **21.1 Aviation PROHIBITED** | No aviation, airline, SAA, or South African Airways client references — absent throughout | ✅ PASS |
| **21.1 SAA source rule** | SAA HCM RFP used for platform capability narrative only (T&L, Scheduling, Mobile, Manager SS); SAA not named anywhere | ✅ PASS |
| **21.2 Implementation vs Support** | Hollywood Bets Absence = implementation (confirmed). Mr Price T&L = PoC (framed as proof-of-concept, not production). Distinction maintained throughout. | ✅ PASS |
| **21.3 Opportunity Marketplace** | Not applicable to this statement | ✅ N/A |
| **21.4 DFA — never named** | DFA not mentioned anywhere in the document | ✅ PASS |
| **21.5 Redpath — not used as completed implementation** | Redpath cited as active pipeline (Absence Management); "a mining-sector client currently implementing Oracle HCM"; not named; not presented as completed | ✅ PASS |
| **CCBA — never named** | CCBA not referenced anywhere | ✅ PASS |
| **SARB — excluded** | Not applicable to Workforce Management | ✅ N/A |

**Product and Evidence Framing Checks**

| Check | Status |
|---|---|
| Mr Price T&L PoC framing — "proof-of-concept", not "rollout" or "go-live" | ✅ Section 4.4 and Section 12.3 — approved framing applied throughout |
| Workforce Scheduling = Platform Capability Only — no implementation claim | ✅ Section 5.3 — explicitly stated; no client reference |
| Workforce H&S = Platform Capability Only — no implementation claim | ✅ Section 6.3 — explicitly stated; no client reference |
| Biometric integration framed as custom OIC integration, not Oracle standard feature | ✅ Section 9.2 — governance note included |
| Hollywood Bets cited for Absence Management (Phase 3.3.1) — not for T&L (absent from HB BOM) | ✅ Section 12.1 — Absence only |
| "APPSolve implemented Oracle Time and Labor capabilities as part of a proof-of-concept programme for a South African retail client" — approved wording used | ✅ Sections 4.4 and 12.3 |

**ORACLE_FACT_BASELINE Prohibited Wording Check**

| Prohibited item | Check |
|---|---|
| "Oracle Gold Partner" | Absent | ✅ |
| "110 Senior Consultants" / "100+ consultants" | Absent — "50+ Senior Consultants" also removed per BU Lead CROSS-1 2026-06-13 | ✅ |
| "over 22 years" | Absent | ✅ |
| "Oracle does X" framing | Absent — reframed throughout as "Oracle platform" + "APPSolve configures/implements" | ✅ |
| T&L PoC presented as go-live or production rollout | Absent — "proof-of-concept programme" used consistently | ✅ |

**OI Items Closed — Final Confirmation**

| OI Item | Decision | Application |
|---|---|---|
| OI-W7-001 Mr Price T&L | PoC evidence — not production deployment | Sections 4.4, 12.3 — approved framing applied |
| OI-W7-002 Workforce Scheduling licensing | Platform Capability Only | Section 5 — no implementation claims; no client references |
| OI-W7-003 Health and Safety | Platform Capability — include | Section 6 — platform capability framing; no implementation claims |
| OI-W7-004 Absence Management scope | Full standalone section | Section 3 — primary evidence area; full standalone treatment |
| OI-W7-005 Document title | "Oracle Workforce Management" | Title confirmed throughout |

**Governance Self-Review conclusion: CLEAN. No violations identified.**

---

## Appendix C: Extraction Return Report

| Field | Value |
|---|---|
| **Extraction ID** | W3S1-007 |
| **Document title** | Oracle Workforce Management |
| **Version** | 1.1 Approved |
| **Date** | 2026-06-13 |
| **Sources used** | HIST-006 (T&L, Scheduling, H&S, Mobile, Manager SS platform narratives); HIST-007 (Absence Phase 3.3.1; Biometric integration BOM); HIST-015 (T&L delivery assumptions; Absence Phase 3.3.1); HIST-016 (Mr Price T&L PoC and Absence evidence); ORACLE_FACT_BASELINE Sections 4.1, 7, 17, 19, 21; Redpath Mining RACI (Absence scope confirmation) |
| **Sources NOT used** | HIST-014 CCBA (SVR research only — no CCBA content extracted; not named); HIST-017 SAA Additional Info (no WFM content — not used); HIST-008 RedPath RFI (no T&L content; RFI general — RACI used instead) |
| **Sections delivered** | 15 content sections (Sections 1–15) + Section 17 + Appendices A, B, C |
| **Open items at submission** | 0 — all 5 BU Lead decisions CLOSED 2026-06-13 |
| **Governance violations** | None |
| **Key governance boundaries (permanent)** | (1) Mr Price T&L = proof-of-concept — never described as production rollout, go-live, or store deployment. (2) Workforce Scheduling and Workforce H&S = Platform Capability Only — no implementation claims, no client references. (3) Biometric integration = custom OIC interface, not Oracle standard. (4) Redpath Mining = active pipeline, not live, never named. (5) DFA never named (Rule 21.4). |
| **Cross-document consistency** | W3S1-001 (HCM Core) cross-referenced for Core HR foundation. W3S1-005 (Workforce Compensation) does not overlap. W3S1-006 (Analytics) cross-referenced for OTBI absence and time reporting — no duplication. |
| **Pre-tender checks (standing)** | PT-W7-001: Confirm Workforce Scheduling licensing position with Oracle account team before citing in tender. PT-W7-002: Confirm Workforce H&S in scope before citing — not a default HCM programme deliverable. PT-W7-003: Confirm biometric system API availability before committing OIC integration to tender. PT-W7-004: Confirm Redpath Mining pipeline is still active before citing mining-sector pipeline reference. PT-W7-005: Confirm OPN annual revalidation current. PT-W7-006: Confirm BEE certificate current (expires 2026-07-31). |
| **Changes v1.0 to v1.1** | E-001: Section 1 T&L row updated — positioning changed to "Confirmed capability (PoC evidence)" with confirmed readiness statement. E-002 / CROSS-1: "APPSolve employs 50+ Senior Consultants and" removed from Section 11.1. Version updated to 1.1 Approved. approved_for_reuse set to Yes. Approved by BU Lead 2026-06-13. |

---

*W3S1-007-ORA-WorkforceManagement v1.1 Approved — 2026-06-13 — Hein Blignaut (BU Lead) — approved_for_reuse: Yes*
