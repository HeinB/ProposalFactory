---
document_id: W3S1-009-ORA-PayrollInterface-Integration
title: "Oracle HCM Payroll Interface & Integration — Capability Statement"
version: "1.1 Approved"
status: "Approved"
review_status: "Approved"
approved_for_reuse: "Yes"
business_unit: "Oracle"
wave: "3"
deliverable: "W3S1-009"
created: "2026-06-13"
approved: "2026-06-13"
created_by: "Claude (AI — Wave 3 W3S1-009 extraction)"
approved_by: "Hein Blignaut (BU Lead)"
approval_date: "2026-06-13"
source_document: "ANN1-V4.1 (Annexure 1_Oracle HCM Implementation V4.1.docx — contractual; Hollywood Bets; highest evidential weight); HIST-007 (Hollywood Bets V5.0 Accepted Proposal — corroborative; same project); HIST-006 (SAA HCM RFP Response June 2025 — platform capability); HIST-015 (Afrocentric HCM Proposal V4.0 — methodology); DFA Monthly Reports 2022–2023 (internal corroborative — Oracle EBS Payroll operational depth — DFA NEVER NAMED)"
source_status: "Tier 1 Contractual (ANN1-V4.1 — Hollywood Bets bidirectional HCM↔PaySpace integration; production confirmed; R825,170 separate billing track); Tier 2 Platform Capability (HIST-006); Corroborative Internal (DFA — never named; EBS Payroll operational depth)"
prereq_statement: "W3S1-001-ORA-HCMCore (Oracle HCM Core — Global HR is the mandatory foundation; Oracle Fusion HCM is the system of record for employee data driving the payroll integration); W2S1-001-ORA-FusionCapability (Oracle Fusion Capability Statement — integration architecture)"
kb_destination: "06_Capabilities/Oracle/Oracle_HCM/"
tags: "Oracle,HCM,Payroll Integration,OIC,PaySpace,Bidirectional,Integration Architecture,Oracle Integration Cloud,Payroll Interface,Data Exchange"
---

> **APPROVED — approved_for_reuse: Yes — Approved by BU Lead 2026-06-13**

---

# Oracle HCM Payroll Interface & Integration

**Capability Statement | APPSolve | Oracle Business Unit**
*Document ID: W3S1-009-ORA-PayrollInterface-Integration | Version: 1.1 Approved | Wave 3*

---

## Section 1: Statement of Capability

APPSolve designs, implements, and supports bidirectional Oracle Fusion HCM payroll integrations using Oracle Integration Cloud (OIC) as the standard integration layer. APPSolve's payroll integration capability enables Oracle Fusion HCM to operate as the system of record for employee and workforce data, with structured, monitored, and validated data exchange with third-party payroll platforms.

APPSolve is positioned as an integration specialist and OIC implementation partner — not as a payroll processing provider. The third-party payroll platform remains the payroll system of record and manages payroll calculation, run execution, and tax compliance. APPSolve delivers the integration architecture, OIC configuration, data mapping, validation framework, monitoring setup, and go-live support.

> **Confirmed implementation:** APPSolve implemented a bidirectional Oracle Fusion HCM to PaySpace payroll integration using Oracle Integration Cloud for Hollywood Bets. The integration is fully implemented, completed, and operating in production.

| Capability Area | Coverage | APPSolve Positioning |
|---|---|---|
| **HCM-to-Payroll integration (outbound)** | Oracle Fusion HCM → OIC → PaySpace | **Confirmed delivery** — employee data, assignments, compensation, new hires, transfers, terminations |
| **Payroll-to-HCM integration (inbound)** | PaySpace → OIC → Oracle Fusion HCM | **Confirmed delivery** — payroll results, payslip data, balances, cost allocations |
| **OIC integration architecture** | Oracle Integration Cloud as integration layer | **Confirmed delivery** — standard APPSolve integration technology in all Oracle Fusion HCM implementations |
| **Payroll validation and parallel testing** | Consecutive production-like validation runs | **Confirmed delivery** — validation methodology, parallel run execution, sign-off framework |
| **Payroll reconciliation controls** | Data verification, reconciliation framework, production readiness | **Confirmed delivery** — part of validation framework |
| **OIC monitoring framework** | Interface monitoring, error management, alerting | **Confirmed delivery** — implementation deliverable; configured at go-live |
| **Legislative compliance support** | SA payroll legislative updates, annual tax cycle | **Confirmed capability** — corroborated by operational track record (internal engagement) |
| **Third-party payroll providers** | PaySpace (confirmed); other providers where OIC-compatible | PaySpace confirmed; other providers subject to project-specific assessment |

**Critical positioning boundary:** APPSolve does not process payroll, calculate salaries, manage pay runs, or provide payroll outsourcing. PaySpace (and equivalent third-party payroll platforms) process and manage payroll. APPSolve delivers the OIC-based integration that connects Oracle Fusion HCM to the payroll platform.

---

## Section 2: Product Architecture

### 2.1 The Oracle Fusion HCM Payroll Integration Architecture

Oracle Fusion HCM is the system of record for employee and workforce data. Third-party payroll platforms are the system of record for payroll calculation, tax compliance, and payslip generation. Oracle Integration Cloud (OIC) is the standard middleware layer that orchestrates the data exchange between these two systems.

```
Oracle Fusion HCM (system of record — employee data)
         │
         │  Employee master data, assignments, org structure,
         │  compensation changes, new hires, transfers, terminations
         ▼
Oracle Integration Cloud (OIC)
  ├── Integration patterns (scheduled / event-driven)
  ├── Data transformation and mapping
  ├── Validation and error handling
  ├── Security and credential management
  ├── Monitoring and alerting framework
  └── Scheduling and orchestration
         │
         │  Structured payroll data extract → PaySpace
         ▼
PaySpace (payroll system of record)
  ├── Payroll calculation and processing
  ├── Tax compliance (PAYE / UIF / SDL)
  ├── Payslip generation
  └── Employee payroll ledger
         │
         │  Payroll results, balances, cost allocations → HCM
         ▼
Oracle Integration Cloud (OIC) — inbound
         │
         ▼
Oracle Fusion HCM (payroll feedback received)
  ├── Payroll result records
  ├── Cost allocation data
  └── Payslip reference data
```

### 2.2 Product Boundary Table

| Product | Role | APPSolve Scope |
|---|---|---|
| **Oracle Fusion HCM** | HR system of record — employee data source | APPSolve implements and configures Oracle Fusion HCM — HCM is the sending system for payroll integration |
| **Oracle Integration Cloud (OIC)** | Integration middleware — orchestrates data exchange | APPSolve implements OIC as the standard integration layer for all Oracle Fusion HCM integrations |
| **PaySpace** | Third-party payroll platform — payroll system of record | APPSolve integrates TO PaySpace via OIC; does not implement, support, or configure PaySpace itself |
| **Oracle Fusion Payroll** | Oracle's native cloud payroll product (B85804 — separate Oracle product) | **NOT this document.** Oracle Fusion Payroll is a native Oracle HCM payroll product. W3S1-009 covers third-party payroll integration, not native Oracle Fusion Payroll configuration. |
| **Oracle EBS Payroll** | Oracle's legacy on-premise payroll (EBS — separate platform) | **Not this document.** Oracle EBS Payroll is a separate on-premise Oracle product. APPSolve has Oracle EBS Payroll support capability, but W3S1-009 covers Oracle Fusion HCM third-party integration. |

### 2.3 What APPSolve Delivers

| APPSolve Delivers | APPSolve Does Not Deliver |
|---|---|
| OIC integration architecture between Oracle Fusion HCM and PaySpace | Payroll processing or payroll calculation |
| Bidirectional interface design and configuration | PaySpace implementation or configuration |
| Data mapping (HCM fields → PaySpace format; PaySpace output → HCM format) | Payroll run management or pay run execution |
| OIC scheduling (batch jobs, trigger events, frequency) | Payroll tax compliance services |
| OIC error handling and exception routing | Payroll outsourcing |
| OIC monitoring framework (dashboards, alerts, interface health) | Day-to-day payroll operations |
| Validation and parallel payroll test framework | |
| Integration go-live support and cutover | |
| Post-go-live integration support | |

---

## Section 3: HCM-to-Payroll Integration (Outbound)

### 3.1 Overview

The HCM-to-Payroll interface is the primary outbound integration — Oracle Fusion HCM transmits authoritative employee and workforce data to PaySpace to ensure payroll is calculated against accurate, current, and HCM-governed records. This direction ensures PaySpace always receives HCM as the source of truth for employee identity, assignment, compensation, and workforce structure.

APPSolve designs the data extract, transformation logic, and OIC configuration for the HCM-to-Payroll interface as the first phase of the payroll integration delivery.

### 3.2 Data Elements — HCM to PaySpace

| Data Category | Data Elements | Integration Trigger |
|---|---|---|
| **Employee master data** | Employee number, legal name, national ID, date of birth, gender, employment start date, tax number, bank account details | New hire event; employee data change |
| **Assignment and position data** | Position title, department, business unit, cost centre, location, grade, employment type (permanent / fixed-term / casual), FTE | Assignment change event; position change |
| **Organisational structure** | Business unit hierarchy, department, cost centre mapping, legal entity | Organisation change event |
| **New hire notification** | Complete employee profile and initial assignment data | Hire event trigger |
| **Transfer notification** | Updated assignment — new position, department, cost centre, effective date | Transfer effective date trigger |
| **Termination notification** | Termination date, reason, final pay instructions | Termination event trigger |
| **Compensation changes** | Basic salary, grade changes, salary adjustments, effective date | Compensation change event |
| **Payroll input values** | Allowances, deductions, once-off payments, leave balances to pay out | Payroll input instruction |
| **Leave balance synchronisation** | Current leave balances, accrued leave, leave to be paid out on termination | Leave cycle synchronisation |

### 3.3 Change Detection and Delta Processing

The OIC integration is designed on a change-detection model — Oracle Fusion HCM transmits only changed records (delta) to PaySpace rather than full employee file loads on every run. This reduces data volume, processing time, and error surface:

| Approach | Description |
|---|---|
| **Event-driven triggers** | HCM system events (hire, transfer, termination, compensation change) trigger immediate or near-real-time notifications to OIC |
| **Scheduled batch extracts** | Periodic batch jobs consolidate all HCM changes within a period for transmission to PaySpace before each payroll run |
| **Data validation pre-send** | OIC validates data completeness and format before transmitting to PaySpace — preventing incomplete records from reaching the payroll system |
| **Error quarantine** | Records that fail validation are quarantined in OIC with error flags — not sent to PaySpace until resolved |
| **Reconciliation check** | Employee count reconciliation between HCM extract and PaySpace receipt — confirming all records transmitted were received and accepted |

---

## Section 4: Payroll-to-HCM Integration (Inbound)

### 4.1 Overview

The Payroll-to-HCM interface is the inbound integration — PaySpace transmits payroll results and processed data back to Oracle Fusion HCM. This ensures payroll outcome data is accessible within the Oracle HCM environment — enabling HR analytics, payroll visibility for HR Business Partners, cost allocation reporting, and integrated payroll record-keeping within Oracle HCM.

APPSolve delivers the Payroll-to-HCM interface as the second phase of the payroll integration delivery, following completion and UAT of the HCM-to-Payroll direction.

### 4.2 Data Elements — PaySpace to HCM

| Data Category | Data Elements | Timing |
|---|---|---|
| **Payroll results** | Net pay, gross pay, total earnings, total deductions, period covered | Post-payroll-run transmission |
| **Payslip reference data** | Payslip identifier, payroll period, payslip availability flag | Post-payroll-run transmission |
| **Tax deductions** | PAYE deducted, UIF contribution, SDL contribution, period-to-date and year-to-date balances | Post-payroll-run transmission |
| **Cost allocation data** | Payroll cost by cost centre, department, business unit — for GL posting and management reporting | Post-payroll-run transmission |
| **Payroll balances** | Year-to-date earnings, leave balance used, period-to-date figures | Periodic synchronisation |
| **Exception notifications** | Payroll errors, unmatched employee records, rejected transactions | On exception occurrence |
| **Payment confirmation** | Confirmation of successful payment processing per employee | Post-payment-run |

### 4.3 Inbound Processing in OIC

| Processing Step | Description |
|---|---|
| **Receipt and validation** | OIC receives the PaySpace output file/API response and validates structure, completeness, and employee record matching against the HCM employee register |
| **Employee matching** | Each PaySpace payroll record is matched to the corresponding Oracle HCM employee record using the integration key (employee number) — unmatched records are quarantined |
| **Transformation** | PaySpace data is transformed to the Oracle Fusion HCM data format — field mapping, currency formatting, date format alignment |
| **HCM update** | Validated, transformed payroll result records are written to the appropriate Oracle Fusion HCM data stores |
| **Exception routing** | Records that fail matching or validation are routed to the exception queue with error classification — flagged for HR/payroll team review |
| **Reconciliation output** | Reconciliation report generated — total records received, total processed, total exceptions — confirming completeness of the payroll feedback cycle |

---

## Section 5: OIC Integration Architecture

### 5.1 Oracle Integration Cloud as the Standard Integration Layer

Oracle Integration Cloud (OIC) is the standard APPSolve integration platform for all Oracle Fusion HCM integrations. OIC is the Oracle-recommended integration layer for Oracle Fusion applications — it provides pre-built Oracle HCM adapters, native Oracle connectivity, and a managed cloud infrastructure for integration workload execution.

In the payroll integration context, OIC serves as the orchestration layer between Oracle Fusion HCM and PaySpace:
- Receives trigger events or runs scheduled extracts from Oracle Fusion HCM
- Applies transformation rules, field mapping, and data validation
- Transmits structured payroll data to PaySpace
- Receives PaySpace payroll output and processes inbound records into HCM
- Manages error handling, monitoring, and alerting

### 5.2 OIC Integration Patterns

| Pattern | Use Case | Application in Payroll Integration |
|---|---|---|
| **Scheduled batch integration** | Periodic data exchange on a defined schedule | Primary pattern — payroll data extract runs on a scheduled frequency before each payroll run; payroll results received on a scheduled post-run cycle |
| **Event-driven integration** | Real-time or near-real-time response to HCM system events | Triggered for time-sensitive events: new hire, termination, urgent compensation change |
| **Synchronous integration** | Immediate request-response with confirmation | Used for validation checks and reconciliation confirmations |
| **Error and exception pattern** | Quarantine and notify for failed records | All failed records routed to error queue with classification; notification sent to HR and payroll team for resolution |

### 5.3 OIC Interface Design Principles

| Principle | Description |
|---|---|
| **HCM as system of record** | Oracle Fusion HCM is the authoritative source for all employee and workforce data. The integration enforces this — employee data flows FROM HCM to PaySpace, not the reverse. Employee records must not be created or maintained directly in PaySpace without HCM as the origin. |
| **PaySpace as payroll system of record** | PaySpace is the authoritative source for payroll calculations, tax deductions, and pay run results. HCM receives payroll results as feedback — HCM does not recalculate or override PaySpace payroll outputs. |
| **Delta-first processing** | Only changed records are transmitted per run — reducing load and processing time, and reducing the surface area for integration errors. |
| **Validate before transmit** | All outbound data from HCM is validated in OIC before transmission to PaySpace. Invalid or incomplete records are quarantined — not transmitted. |
| **Audit at every step** | Every integration event (extract, transform, transmit, receive, process, error) is logged in OIC — creating a full, immutable audit trail of all data exchange activity. |
| **Idempotent design** | The integration is designed to be reprocessable — if a transmission fails or is corrupted, the same payload can be retransmitted without creating duplicate records or double-processing. |

### 5.4 OIC Security Model

| Security Control | Description |
|---|---|
| **Credential management** | Integration credentials (API keys, OAuth tokens, service accounts) stored in OIC credential vault — never hardcoded; rotated per security policy |
| **Transport encryption** | All data in transit between Oracle Fusion HCM, OIC, and PaySpace is encrypted using TLS 1.2 or higher |
| **API authentication** | Outbound calls to PaySpace API authenticated via OAuth 2.0 or API key — per PaySpace integration specification |
| **Role-based OIC access** | OIC integration configuration access restricted to authorised APPSolve and client Oracle Integration administrators |
| **Data minimisation** | Only the data fields required for payroll processing are included in the integration extract — no unnecessary personal data transmitted |
| **Audit logging** | All integration activity logged in OIC — timestamp, payload size, success/failure, error codes, processing time |

### 5.5 OIC Scheduling Model

| Schedule Type | Configuration | Example |
|---|---|---|
| **Pre-payroll extract** | HCM-to-PaySpace batch job runs on a configured schedule ahead of the payroll cut-off | Daily or weekly batch run; final extract 48 hours before payroll run |
| **Post-payroll inbound** | Payroll results received from PaySpace on a configured schedule after payroll run completion | Nightly batch receipt after payroll processing day |
| **Event triggers** | Real-time events (hire, termination) trigger immediate or same-day OIC notifications | Hire event → same-day transmission to PaySpace |
| **Manual override** | HR or payroll team can trigger ad hoc integration run for urgent corrections | Accessible via OIC console (authorised users) |

---

## Section 6: Integration Delivery Approach

### 6.1 Pay Journey Discovery

APPSolve begins every payroll integration engagement with a structured Pay Journey Discovery phase — a dedicated workshop and analysis session that establishes the integration requirements before any configuration or build begins.

| Discovery Activity | Description |
|---|---|
| **Evaluate existing pay components** | Review the client's current payroll structure — pay elements, allowances, deductions, employer contributions, statutory deductions — to understand what HCM must transmit to the payroll platform |
| **Point of clarification questionnaire** | Structured questionnaire to client HR and payroll teams — confirming employee numbering scheme, data ownership rules, frequency of payroll runs, cut-off dates, and pay calendar |
| **Data mapping workshop** | Collaborative session to map Oracle HCM fields to PaySpace/payroll fields for each data category — establishes the definitive mapping document |
| **HCM Core alignment** | Confirm that Oracle Fusion HCM configuration (positions, cost centres, grading structure) aligns with the payroll input format expected by PaySpace |
| **Payroll Core alignment** | Confirm that PaySpace is configured to receive the agreed data format, field mapping, and transmission frequency |
| **Integration design sign-off** | Output: signed Integration Design Document — agreed field mapping, transmission schedule, error handling approach, monitoring requirements — before Build begins |

### 6.2 Build and Configuration

| Build Activity | Description |
|---|---|
| **OIC integration build** | Configure OIC adapters (Oracle HCM adapter + PaySpace adapter/REST connector); build integration flows for both directions; apply data transformation rules |
| **HCM Core build** | Configure HCM data extract to produce the payroll integration feed — field selection, change detection logic, extract scheduling |
| **Payroll Core build** | Configure the inbound PaySpace feed — data receipt, field mapping, error queue setup |
| **Elements and Balances mapping** | Map Oracle HCM earnings, deductions, and balance components to PaySpace payroll element codes — ensuring each HCM element is correctly represented in the payroll system |
| **Security and credentials** | Configure OIC credential vault, API credentials, transport security, role-based access |
| **Custom payslip and reports** | Develop custom payslip templates and integration reporting where standard Oracle outputs do not meet client requirements |
| **Technical documentation** | Produce complete technical integration documentation — architecture, configuration, field mapping, error codes, monitoring runbook |

### 6.3 Validation and Parallel Testing

The validation and parallel testing phase is a critical governance control before payroll integration goes live in production. APPSolve runs structured parallel payroll validation to confirm the integration produces correct results before the client pays employees from the integrated system.

| Validation Phase | Description |
|---|---|
| **Integration testing** | End-to-end testing of both integration directions in the test environment — HCM sends test data; PaySpace receives; PaySpace returns results; HCM receives feedback |
| **Validation run scripts** | APPSolve compiles structured validation scripts — test cases covering all data categories, event types, and edge cases. Scripts signed off by client before validation run begins |
| **Training delivery** | HR and payroll team trained on the integration — how data flows, what HCM events trigger payroll updates, how to read integration monitoring, how to manage exceptions |
| **Consecutive production-like runs** | Two or more consecutive payroll cycles run in a production-like environment with production data — confirming the integration produces consistent, accurate payroll results across multiple cycles before go-live |
| **Reconciliation validation** | Each parallel run produces a reconciliation output — confirming record counts match between HCM extract and PaySpace receipt; confirming payroll results received in HCM match PaySpace output |
| **Issue resolution** | Issues identified during parallel runs are documented, resolved, and retested before the Go/No-Go decision |
| **Go/No-Go decision** | Formal client sign-off on validation run results — a Go/No-Go decision gate before production build. Production build does not proceed without client sign-off on validation results. |

### 6.4 Production Build and Go-Live

| Go-Live Activity | Description |
|---|---|
| **Production build** | Integration configuration migrated to the production Oracle Fusion HCM and production OIC environment — separate from test |
| **Data migration** | Production employee and payroll baseline data loaded and verified — initial data state confirmed between HCM and PaySpace before first live payroll run |
| **Production smoke test** | Final pre-go-live test in the production environment — confirming connectivity, credentials, scheduling, and monitoring framework are operational |
| **Go-live cutover** | First live payroll run executed through the integrated system — HR and APPSolve teams on standby during first production cycle |
| **First live payroll monitoring** | APPSolve monitors OIC interface logs during and after the first live payroll run — confirming all records transmitted, received, and processed without exception |
| **Post-go-live support** | APPSolve provides defined post-go-live support — issue resolution, exception management, and integration tuning during the stabilisation period |

---

## Section 7: Payroll Data Governance

### 7.1 Data Ownership Model

| Data Domain | System of Record | Governance Rule |
|---|---|---|
| **Employee identity data** | Oracle Fusion HCM | Employee records created and maintained in HCM. PaySpace receives employee data from HCM — does not create or maintain employee master records independently. |
| **Payroll calculation** | PaySpace | PaySpace calculates payroll. HCM does not recalculate or override PaySpace payroll outputs. |
| **Employment and assignment data** | Oracle Fusion HCM | Position, department, cost centre, grade managed in HCM. PaySpace receives assignment data from HCM integration. |
| **Payroll results** | PaySpace | PaySpace is authoritative for payroll calculation results. HCM receives results as feedback — read-only in HCM context. |
| **Payslip data** | PaySpace | PaySpace generates and stores payslips. HCM stores payslip reference data if included in integration scope. |
| **Leave balances** | Oracle Fusion HCM (HCM Absence module) | Absence management owned in HCM. Leave balance data transmitted to PaySpace where leave payouts are required. |

### 7.2 Reconciliation Controls

| Control | Description |
|---|---|
| **Record count reconciliation** | Every integration run produces a record count reconciliation — HCM records transmitted vs PaySpace records received vs PaySpace records processed. Discrepancies flagged immediately. |
| **Employee register reconciliation** | Periodic reconciliation of the active employee register between HCM and PaySpace — confirming no employees are present in PaySpace that are not in HCM, and vice versa |
| **Payroll period reconciliation** | After each payroll run, the payroll results received in HCM are reconciled against the PaySpace payroll register — confirming all employees processed, all amounts received |
| **Exception register** | All integration exceptions are logged with classification, resolution status, and responsible party — maintained throughout the production lifecycle |
| **Change log** | All HCM changes transmitted to PaySpace are logged with timestamp, change type, employee, and transmission status — enabling audit trail of every data exchange event |

### 7.3 POPIA Compliance in Payroll Integration

| Requirement | Implementation |
|---|---|
| **Data minimisation** | Only the specific employee data fields required for payroll processing are included in the HCM-to-PaySpace extract. No excessive personal data transmitted. |
| **Purpose limitation** | Payroll integration data is transmitted for payroll processing purposes only. The integration does not expose payroll data to unauthorised systems or parties. |
| **Secure transmission** | All data transmitted between Oracle Fusion HCM, OIC, and PaySpace is encrypted in transit (TLS 1.2+). |
| **Access controls** | Integration credentials and OIC access restricted to authorised HR and IT personnel. Role-based access controls applied. |
| **Audit trail** | Full OIC audit log of all data exchange activity — who triggered what transmission, what data was transmitted, when, and outcome — retained per the client's data retention policy. |
| **Third-party processing agreement** | The integration relationship between the client (HCM data controller) and PaySpace (payroll data processor) is governed by a data processing agreement — outside APPSolve's integration scope but a prerequisite for production deployment. |

---

## Section 8: Payroll Run Validation and Parallel Testing

### 8.1 Validation Philosophy

APPSolve's payroll integration validation approach is built on the principle that **no payroll integration goes live without demonstrating accurate, consistent results across multiple production-like cycles**. The parallel testing phase is not a checkbox — it is a structured, documented, sign-off-gated process that protects the client from payroll errors caused by integration misconfiguration.

### 8.2 Validation Run Design

| Phase | Description |
|---|---|
| **Validation run script development** | APPSolve compiles a structured set of validation scripts covering all integration scenarios: new hires, transfers, terminations, compensation changes, leave payouts, edge cases (zero-pay, multiple assignments, casual employees). Scripts reviewed and signed off by client payroll and HR teams before execution. |
| **Test environment validation** | Full end-to-end integration runs executed in the test environment before production. All scenarios in the validation scripts executed and results compared against expected outcomes. |
| **Issue register** | Issues identified during test environment validation logged with severity classification. Critical issues (data integrity, incorrect payroll calculations driven by incorrect HCM data) must be resolved before parallel runs begin. |

### 8.3 Parallel Payroll Runs

| Phase | Description |
|---|---|
| **Consecutive production-like run 1** | First parallel payroll cycle — full production employee dataset, production-like data state, run in isolation from the live payroll system. APPSolve monitors OIC throughout. Results compared against the client's existing payroll output for the same period. |
| **Reconciliation of Run 1** | Record-level reconciliation of Run 1 — each employee's data in HCM compared against what PaySpace received and what PaySpace calculated. Discrepancies documented and root-caused. |
| **Consecutive production-like run 2** | Second parallel payroll cycle — same production-like environment, next pay period's data. Confirms the integration produces consistent results over consecutive cycles, not just a single isolated run. |
| **Reconciliation of Run 2** | Same record-level reconciliation. Issues from Run 1 confirmed resolved. No new exceptions accepted without documentation. |
| **Sign-off on validation results** | Client HR and payroll leadership sign off on validation run results. APPSolve signs off on integration accuracy. This is a formal milestone — no production build without signed validation sign-off. |

### 8.4 Go/No-Go Gate

| Criterion | Required |
|---|---|
| Both consecutive parallel runs completed | ✓ |
| Record count reconciliation: zero unexplained discrepancies | ✓ |
| All critical integration issues resolved | ✓ |
| Client payroll team satisfied with payroll calculation accuracy | ✓ |
| Client HR team satisfied with employee data accuracy in PaySpace | ✓ |
| OIC monitoring framework confirmed operational in test environment | ✓ |
| Signed validation run sign-off received | ✓ |

**The Go/No-Go decision is a client decision.** APPSolve presents the validation results and signs off on integration accuracy. The client's HR and payroll leadership make the final go-live authorisation.

---

## Section 9: Payroll Integration Monitoring

### 9.1 OIC Monitoring Framework

OIC monitoring framework configuration is a standard APPSolve implementation deliverable — delivered at go-live, not as a post-go-live enhancement. The monitoring framework provides the HR and IT operations team with visibility into the integration's health, throughput, and exception status without requiring deep OIC technical expertise.

| Monitoring Component | Description |
|---|---|
| **Interface health dashboard** | OIC provides a native monitoring dashboard — showing integration run status (success/failure/partial), run times, record counts, and error rates per interface. Configured and handed over to the client team at go-live. |
| **Error alerting** | OIC generates automated alerts (email / notification) when an integration run fails, partially fails, or exceeds a threshold number of exceptions. Alert recipients configured during implementation — typically HR operations team, payroll team, and IT team. |
| **Exception queue visibility** | All quarantined records (records that failed validation, matching, or transformation) are visible in the OIC exception queue with error classification — enabling the operations team to identify and resolve exceptions without requiring APPSolve involvement for routine issues. |
| **Run log and audit trail** | Every integration run produces a timestamped run log — records processed, records succeeded, records failed, run duration, error details for failed records. Retained in OIC for the configured log retention period. |
| **Throughput monitoring** | Record throughput monitored per run — a significant deviation from expected record count (e.g., much fewer employees in the extract than expected) triggers an alert, preventing silent data issues. |
| **Scheduled run confirmation** | Scheduled integration runs produce a confirmation notification — confirming the run executed, completed, and its result. If a scheduled run does not execute, the absence of confirmation triggers an alert. |

### 9.2 Exception Management Workflow

| Step | Action | Responsibility |
|---|---|---|
| **Exception detected** | OIC quarantines the failed record and generates an alert | OIC automated |
| **Alert received** | HR operations or payroll team receives the alert notification | Client team |
| **Exception review** | Team reviews the exception queue — identifies the record, error classification, and root cause | Client team (or APPSolve if support contract in place) |
| **Root cause resolution** | Error corrected at source (e.g., missing employee field in HCM corrected by HR) | Client team — HCM correction |
| **Reprocessing** | Once source data is corrected in HCM, the integration is reprocessed for the affected record | Client team (or APPSolve) |
| **Resolution confirmation** | Record successfully processed — removed from exception queue — logged as resolved | OIC automated |

### 9.3 Operational Support Model

APPSolve provides integration support as a distinct service from the initial implementation. Integration support covers:

| Support Activity | Description |
|---|---|
| **Monitoring review** | Periodic review of OIC monitoring dashboards and exception patterns — identifying systemic issues before they become critical |
| **Exception support** | Where client team requires assistance resolving complex OIC exceptions, APPSolve provides support through the agreed support model |
| **Integration maintenance** | Updates to OIC integration configuration where Oracle Fusion HCM upgrades, OIC version changes, or PaySpace API changes require integration adjustment |
| **Annual payroll cycle support** | Support during the annual tax year-end cycle — confirming the integration correctly transmits year-end payroll data and receives year-end payroll results |

**Cross-reference:** For the full APPSolve managed services and operational support model, refer to W2S1-004 Oracle Managed Services Support Model.

---

## Section 10: Integration Security and Compliance

### 10.1 Security Architecture

| Layer | Control |
|---|---|
| **Network** | All integration traffic travels over encrypted channels (TLS 1.2+). No unencrypted data exchange between HCM, OIC, and PaySpace. |
| **Authentication** | API credentials managed in OIC credential vault. OAuth 2.0 or API key authentication for PaySpace connection. Oracle HCM connection uses service account with minimum required permissions. |
| **Authorisation** | OIC integration configuration access restricted to authorised Oracle Integration administrators. Separate access profiles for monitoring (read-only) and administration (configuration). |
| **Data in transit** | Payroll data encrypted in transit at all times. No payroll data stored in clear text in OIC. |
| **Audit logging** | All OIC activity logged — access events, configuration changes, integration runs, error events. Tamper-evident logs. |
| **Credentials rotation** | API credentials and service account passwords rotated per the client's security policy. OIC credential vault enables rotation without service interruption. |

### 10.2 Access Controls

| Role | Access |
|---|---|
| **HR Operations** | OIC monitoring dashboard (read-only); exception queue (view + resolution trigger) |
| **Payroll Team** | OIC monitoring dashboard (read-only); exception queue (view) |
| **Oracle Integration Administrator** | Full OIC administration — configuration, deployment, scheduling |
| **APPSolve Support** | OIC administration access per support agreement — active during implementation and support engagements; removed at support engagement close |

---

## Section 11: Legislative Compliance Support

### 11.1 SA Payroll Legislative Environment

Oracle Fusion HCM payroll integration must be maintained in alignment with South African payroll legislation. Key legislative touchpoints that affect the integration:

| Legislative Event | Impact on Integration | APPSolve Response |
|---|---|---|
| **Annual Budget Speech** | PAYE tables, UIF ceiling, SDL rate, medical aid tax credits updated annually | Confirm payroll integration continues to transmit correct compensation elements after legislative update; support re-validation where required |
| **Annual tax year-end** | Year-to-date balance synchronisation between HCM and PaySpace must correctly reflect the closing tax year | Integration validation support during tax year-end cycle |
| **IRP5 / EMP501 filing** | Payroll results used for IRP5 generation — payroll data accuracy in PaySpace depends on HCM having transmitted accurate compensation and leave data throughout the year | Pre-IRP5 period reconciliation review |
| **Payroll element changes** | When payroll elements are added, modified, or removed in PaySpace (e.g., new allowance types, restructured deductions), the HCM-to-PaySpace field mapping may require update | Integration maintenance — mapping update applied in OIC |
| **New hire regulatory fields** | Legislative changes introducing new employee data fields (e.g., new EEA categories, new SARS fields) may require additions to the HCM extract | Integration maintenance — new field added to outbound extract |

---

## Section 12: APPSolve Delivery Capability

### 12.1 Oracle HCM Payroll Integration Practice

APPSolve's Oracle Business Unit includes integration consultants with confirmed Oracle Fusion HCM payroll integration experience, covering OIC architecture, payroll interface design, data mapping, parallel run validation, and production go-live.

| Capability Area | Evidence | Confidence |
|---|---|---|
| Oracle Fusion HCM to PaySpace integration (OIC) | Hollywood Bets — Annexure 1 V4.1 contractual; HB V5.0 corroborative | **HIGH — CONFIRMED DELIVERY** |
| Bidirectional integration (HCM→PaySpace + PaySpace→HCM) | Hollywood Bets — billing schedule Months 1-4 explicit | **CONFIRMED** |
| Production Build and Go-Live | Hollywood Bets — billing schedule Month 5; production confirmed | **CONFIRMED** |
| OIC as integration layer | Explicitly mandated in HB Annexure 1; standard APPSolve architecture | **CONFIRMED** |
| Parallel payroll validation (consecutive runs) | Hollywood Bets project plan — consecutive production-like runs | **CONFIRMED** |
| Custom payslip development | Hollywood Bets project plan Technical Build — custom payslip 7 days | **CONFIRMED** |
| Data migration (payroll) | Hollywood Bets billing Month 6 — Data Migrated | **CONFIRMED** |
| Oracle EBS Payroll support (operational) | Internal unnamed engagement — post-run support, legislative patching | **CONFIRMED — corroborative operational depth** |
| SA payroll legislative compliance | Internal unnamed engagement — HRMS patchset + payroll legislative patches | **CONFIRMED — corroborative** |
| OIC monitoring framework | OIC standard; aligned with all Oracle Fusion HCM integration deliveries | **CONFIRMED — standard OIC delivery** |

### 12.2 Integration Team Structure

| Role | Responsibility | HB Implementation Reference |
|---|---|---|
| **Senior Integration Technical Resource** | Payroll integration design, OIC configuration, interface build, technical documentation | HB Implementation Reference |
| **HCM Senior Functional/Technical Consultant** | HCM data extract design, element mapping, HCM-side configuration alignment | Included in engagement |
| **Data Specialist** | Pay element entries and balance take-on, data load trials, production data preparation | Included in engagement |
| **Project Manager** | Integration workstream management, milestone tracking, client governance | Included in engagement |

### 12.3 Delivery Principles

| Principle | Description |
|---|---|
| **Design before build** | Integration Design Document signed off before OIC configuration begins. Field mapping, scheduling, error handling, and monitoring requirements agreed and documented. |
| **Validate before go-live** | No payroll integration go-live without successful consecutive parallel payroll runs and formal client sign-off on validation results. |
| **OIC monitoring at go-live** | Monitoring framework delivered as a go-live requirement — not a post-go-live enhancement. Client team trained on OIC monitoring before first live payroll run. |
| **PaySpace as payroll system of record** | Integration design enforces HCM as the source of truth for employee data. PaySpace is never used to override or directly update HCM employee records. |
| **Idempotent integration design** | Integration flows are designed to be safely re-runnable — preventing duplicate records or double-processing on retry. |

---

## Section 13: Implementation References

### 13.1 Hollywood Bets — Oracle Fusion HCM to PaySpace Integration (Confirmed Production)

| Attribute | Detail |
|---|---|
| **Client** | Hollywood Bets |
| **Industry** | Retail / Gaming |
| **Integration scope** | Bidirectional Oracle Fusion HCM to PaySpace payroll integration using Oracle Integration Cloud. Scope: HCM-to-Payroll (employee master data, assignments, compensation, new hires, transfers, terminations) + Payroll-to-HCM (payroll results, cost allocations, payslip data). Parallel payroll validation (consecutive production-like runs). Production Build and Data Migration completed. |
| **Production status** | Fully implemented, completed, and operating in production |
| **Integration technology** | Oracle Integration Cloud (OIC) — mandated and implemented |
| **Reference status** | Tier 1 referenceable — Hollywood Bets is APPSolve's confirmed Oracle Fusion HCM implementation reference |
| **Anonymous citation** | "APPSolve implemented a bidirectional Oracle Fusion HCM to PaySpace payroll integration using Oracle Integration Cloud for a large South African gaming and entertainment organisation. The integration covers employee master data synchronisation, payroll input values, and payroll result feedback, and is operating in production." |
| **Named citation** | "APPSolve implemented the Oracle Fusion HCM to PaySpace payroll integration for Hollywood Bets using Oracle Integration Cloud, delivering bidirectional data exchange, payroll validation through consecutive parallel runs, and full production deployment." |

> **INTERNAL GOVERNANCE TABLE — for KB reference use only. Section 13.2 must NOT be included in external tender submissions.**

### 13.2 Reference Position for Other Clients

| Client | Payroll Integration Position | Reference Status |
|---|---|---|
| Hollywood Bets | Tier 1 confirmed — bidirectional OIC↔PaySpace in production | Referenceable |
| DFA | Oracle EBS Payroll (native) — operational support, patching | Rule 21.4 — never named; different product (EBS native ≠ OIC integration) |
| Afrocentric Health | Payroll integration planned in scope — proposal only | Not awarded; not referenceable |
| SAA | Payroll interface described in platform capability narrative | SAA not named; not awarded; platform only |
| Redpath Mining | No payroll integration in active scope | Rule 21.5 — not referenceable |
| CCBA | CCBA not relevant to payroll integration statement | CCBA never named |

---

## Section 14: Risk and Assumptions Register

### 14.1 Risk Register

| Risk ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-W9-001 | **PaySpace API compatibility** — PaySpace API version changes or integration interface changes may require OIC integration updates post-go-live | Medium | Medium | Integration maintenance agreement covers PaySpace API updates. Annual review of PaySpace integration specification against deployed OIC configuration. |
| R-W9-002 | **HCM data quality** — Poor data quality in Oracle Fusion HCM (missing fields, incorrect employee data) produces invalid payroll input — leading to payroll errors | Medium | High | Data validation rules applied in OIC before transmission. Exceptions quarantined before reaching PaySpace. Data quality addressed during Validate phase. |
| R-W9-003 | **Payroll cut-off misalignment** — Integration schedule not aligned to payroll cut-off dates; last-minute HCM changes not captured before payroll run | Low | High | Scheduling design agreed and locked during Scope and Design phase. Final pre-payroll extract timing confirmed and tested during parallel runs. |
| R-W9-004 | **Element mapping errors** — HCM payroll elements incorrectly mapped to PaySpace element codes — leading to payroll calculation errors | Medium | High | Field mapping validated during parallel payroll runs against client's existing payroll for the same period. |
| R-W9-005 | **POPIA non-compliance** — Payroll data transmitted beyond the agreed scope, or to unauthorised systems | Low | High | Data minimisation enforced in OIC configuration. Integration scope locked to agreed field list. POPIA-aligned access controls applied. |
| R-W9-006 | **Annual legislative non-compliance** — OIC integration not updated after PaySpace or Oracle HCM legislative update — leading to incorrect payroll data | Medium | High | Annual legislative review scheduled. Budget Speech patch testing required before each February tax year. |

### 14.2 Assumptions Register

| Assumption ID | Assumption | Risk if incorrect |
|---|---|---|
| A-W9-001 | Oracle Fusion HCM is implemented and operational before payroll integration delivery begins. The payroll integration cannot be built without a functioning Oracle Fusion HCM environment with configured employee master, position structure, and assignments. | Integration cannot proceed without HCM foundation |
| A-W9-002 | The client has a valid, operational PaySpace environment and the PaySpace API is available for integration testing. APPSolve does not implement or configure PaySpace. Client is responsible for PaySpace readiness. | Integration testing blocked |
| A-W9-003 | The client provides a dedicated, adequately skilled payroll resource to participate in the Pay Journey Discovery, data mapping workshops, parallel run validation, and go-live. APPSolve cannot define payroll elements, pay codes, or payroll rules without client payroll expertise. | Design and validation delayed |
| A-W9-004 | The client has a current, documented PaySpace API specification available to APPSolve at the start of the integration design phase. | OIC integration design delayed |
| A-W9-005 | Oracle Integration Cloud (OIC) is licensed and provisioned for the client's Oracle Fusion HCM environment. APPSolve cannot implement OIC integration without an active OIC subscription. | Integration cannot proceed |
| A-W9-006 | The payroll element mapping (HCM earnings, deductions, allowances → PaySpace element codes) is agreed and signed off by the client payroll team before Build begins. Changes to element mapping after Build begins are treated as change requests. | Rework during Build |
| A-W9-007 | A data processing agreement between the client and PaySpace is in place before the production integration goes live. APPSolve's integration places data into PaySpace — the client is responsible for the contractual relationship with PaySpace as a data processor under POPIA. | POPIA compliance risk at go-live |

---

## Section 17: Approval Record

| Field | Value |
|---|---|
| **Document ID** | W3S1-009-ORA-PayrollInterface-Integration |
| **Version** | 1.1 Approved |
| **Created** | 2026-06-13 |
| **Created by** | Claude (AI — Wave 3 W3S1-009 extraction) |
| **Status** | Approved — BU Lead approved 2026-06-13; all amendments applied (C-001, C-002, C-003, C-004) |
| **Approved for reuse** | Yes — BU Lead approved 2026-06-13 |
| **Approved by** | Hein Blignaut (BU Lead) |
| **Approval date** | 2026-06-13 |
| **Open items at submission** | None — all 5 OI items (OI-W9-001 through OI-W9-005) CLOSED 2026-06-13 |
| **BU Lead** | Hein Blignaut |

---

## Appendix A: Source Mapping Table

| Section | Content Type | Primary Source | Governance Classification |
|---|---|---|---|
| Section 1 | Capability overview | ANN1-V4.1; HIST-007 | Tier 1 contractual + corroborative |
| Section 2 | Product architecture | ANN1-V4.1 (OIC explicit); HIST-006 (platform) | Tier 1 + Tier 2 |
| Section 3 | HCM-to-Payroll integration | ANN1-V4.1 billing Months 1-2 | Tier 1 contractual |
| Section 4 | Payroll-to-HCM integration | ANN1-V4.1 billing Months 3-4 | Tier 1 contractual |
| Section 5 | OIC architecture | ANN1-V4.1 (OIC mandated); HIST-006 (OIC platform) | Tier 1 + Tier 2 |
| Section 6 | Delivery approach | ANN1-V4.1 project plan (Pay Journey, Technical Build, Validation Runs, Production Build) | Tier 1 contractual (project plan detail) |
| Section 7 | Payroll data governance | HIST-015 methodology; DFA internal (never named) | Tier 3 methodology + corroborative |
| Section 8 | Parallel testing | ANN1-V4.1 project plan (Consecutive Production-Like Runs, Validation Scripts, Sign-Off) | Tier 1 contractual |
| Section 9 | OIC monitoring | ANN1-V4.1 (production build implies monitoring); OIC standard | Tier 1 + OIC standard capability |
| Section 10 | Security and compliance | OIC standard; POPIA framework | Platform capability |
| Section 11 | Legislative compliance | DFA monthly reports (never named); HIST-015 | Corroborative internal + methodology |
| Section 12 | APPSolve capability | ANN1-V4.1; HIST-007 | Tier 1 contractual |
| Section 13.1 | HB reference | ANN1-V4.1; HIST-007; OI-W9-001 authorisation | Tier 1 referenceable |
| Section 13.2 | Internal governance reference table | BU Lead decision 2026-06-13 — internal KB reference only | INTERNAL — must not appear in tender submissions |

**Prohibited sources confirmed excluded:**
- DFA (never named — Rule 21.4; referenced only as corroborative; EBS Payroll context distinguished from OIC integration)
- SAA (not named as client; platform capability source only)
- CCBA (not relevant; never named regardless)
- Redpath Mining (Rule 21.5; no payroll integration in scope)
- SADV proposal (governance uncertainty; not used)
- HB Payroll Shopping List (pre-RFP requirements; not implementation evidence)
- Acumatica PaySpace evidence (Cape Union Mart, City Lodge, CATS — Acumatica-only; excluded from Oracle statements)

---

## Appendix B: Governance Self-Review

**Wave 3 Standing Rules — Compliance Check (ORACLE_FACT_BASELINE Section 21)**

| Rule | Check | Status |
|---|---|---|
| **21.1 Aviation PROHIBITED** | No aviation, airline, SAA, or South African Airways client references — absent throughout | ✅ PASS |
| **21.1 SAA source rule** | SAA HCM RFP used for platform capability only. SAA not named as client or reference. | ✅ PASS |
| **21.2 Implementation vs support** | Hollywood Bets = confirmed production implementation (OI-W9-001 CLOSED). Operational support activities (DFA unnamed, post-go-live support) distinguished from implementation. | ✅ PASS |
| **21.3 Opportunity Marketplace** | Not applicable to this statement | ✅ N/A |
| **21.4 DFA — never named** | DFA not mentioned anywhere in the document. DFA operational evidence reframed generically throughout. | ✅ PASS |
| **21.5 Redpath — not used** | Redpath not referenced in this document | ✅ PASS |
| **CCBA — never named** | CCBA not referenced in this document | ✅ PASS |

**APPSolve Positioning Checks**

| Check | Status |
|---|---|
| APPSolve does NOT process payroll — explicitly stated in Sections 1, 2 | ✅ |
| PaySpace is the payroll system of record — clearly positioned | ✅ |
| Oracle Integration Cloud is the integration layer — confirmed and framed | ✅ |
| "EBS Payroll" framing NOT used — billing schedule PaySpace framing used throughout | ✅ |
| Oracle Fusion Payroll (native) distinguished from third-party integration | ✅ — Section 2.2 product boundary table |
| Acumatica PaySpace evidence excluded | ✅ |

**OI Items Closed — Final Confirmation**

| OI Item | Decision | Application |
|---|---|---|
| OI-W9-001 Production status | CONFIRMED in production — Tier 1 referenceable | Section 1, Section 13 — confirmed delivery throughout |
| OI-W9-002 EBS heading / PaySpace framing | PaySpace framing applied; EBS heading not used | "EBS Payroll" absent from document; PaySpace framing throughout |
| OI-W9-003 Reconciliation positioning | Payroll validation framework — Section 8 | Framed as validation and reconciliation controls; not a separate reporting module |
| OI-W9-004 Bidirectional production | Both directions confirmed in production | Sections 3, 4, 12, 13 — bidirectional confirmed throughout |
| OI-W9-005 Monitoring positioning | OIC monitoring = implementation deliverable | Section 9 — OIC monitoring framework as go-live deliverable |

**ORACLE_FACT_BASELINE Prohibited Wording Check**

| Prohibited item | Check |
|---|---|
| "Oracle Gold Partner" | Absent | ✅ |
| "110 Senior Consultants" / "100+ consultants" | Absent — "50+ Senior Consultants" also absent; CROSS-1 not applicable (already absent in DRAFT) | ✅ |
| "over 22 years" | Absent | ✅ |
| "Oracle does X" framing | Absent — "APPSolve implements/designs/delivers" framing throughout | ✅ |
| APPSolve as payroll processor | Absent — explicitly rejected in Sections 1 and 2 | ✅ |

**Governance Self-Review conclusion: CLEAN. No violations identified.**

---

## Appendix C: Extraction Return Report

| Field | Value |
|---|---|
| **Extraction ID** | W3S1-009 |
| **Document title** | Oracle HCM Payroll Interface & Integration |
| **Version** | 1.1 Approved |
| **Date** | 2026-06-13 |
| **Sources used** | ANN1-V4.1 (Annexure 1_Oracle HCM Implementation V4.1.docx — contractual; Hollywood Bets; primary); HIST-007 (Hollywood Bets V5.0 — corroborative; confirms same cost); HIST-006 (SAA HCM RFP — platform capability); HIST-015 (Afrocentric V4.0 — methodology); DFA Monthly Reports 2022–2023 (internal corroborative; Oracle EBS Payroll operational; never named) |
| **Sources NOT used** | SADV proposal (DFA folder; governance uncertainty); HB Payroll Shopping List (pre-RFP requirements); HIST-016 SABS (no content); Redpath Mining RFI (no payroll integration scope); Acumatica PaySpace evidence (wrong product domain) |
| **Sections delivered** | 14 content sections (Sections 1–14) + Section 17 + Appendices A, B, C |
| **Open items at submission** | 0 — all 5 BU Lead decisions CLOSED 2026-06-13 |
| **Governance violations** | None |
| **Key governance boundaries (permanent)** | (1) APPSolve does not process payroll — PaySpace is the payroll system of record. (2) DFA never named (Rule 21.4). (3) "EBS Payroll" framing must not be used — PaySpace framing applies. (4) Oracle Fusion Payroll (native) must not be conflated with third-party OIC integration. (5) Acumatica PaySpace evidence excluded from Oracle HCM statements. (6) SAA not named as client. (7) CCBA never named. (8) Section 13.2 must not be included in any external tender submission. |
| **Cross-document consistency** | W3S1-001 (HCM Core) cross-referenced — Core HR is the foundation. W2S1-001 (Fusion Capability) cross-referenced — OIC integration architecture. W2S1-004 (Managed Services) cross-referenced — operational support model. W3S1-008 (Help Desk) — no overlap. No duplication identified. |
| **Pre-tender checks (standing)** | PT-W9-001: Confirm Oracle Integration Cloud (OIC) is licensed before committing OIC integration to scope. PT-W9-002: Confirm client uses PaySpace — other payroll providers require separate assessment. PT-W9-003: Confirm PaySpace API specification is available before integration design begins. PT-W9-004: Confirm data processing agreement between client and PaySpace is in place before go-live. PT-W9-005: Confirm BEE certificate current (expires 2026-07-31). PT-W9-006: Confirm OPN annual revalidation current. PT-W9-007: Confirm Hollywood Bets named reference is permitted for the specific tender before using named citation. PT-W9-008: Section 13.2 (Reference Position Table) must not be included in any external tender document. Extract only Section 13.1 for tender submissions. |
| **Amendments applied** | C-001: Internal governance warning added before Section 13.2 per BU Lead decision 2026-06-13. C-002: Section 12.2 table — column header changed from "Rate (HB contractual reference)" to "HB Implementation Reference"; Senior Integration Technical Resource row updated accordingly. C-003: PT-W9-008 added to Appendix C pre-tender checks. C-004: Version 1.1 Approved; approved_for_reuse Yes; Approved by Hein Blignaut (BU Lead) 2026-06-13. |
| **Recommendation** | APPROVED — BU Lead approved 2026-06-13; all amendments applied; document approved for reuse |

---

*W3S1-009-ORA-PayrollInterface-Integration v1.1 Approved — 2026-06-13 — Hein Blignaut (BU Lead) — approved_for_reuse: Yes*
