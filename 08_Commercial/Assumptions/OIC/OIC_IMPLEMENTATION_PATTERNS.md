---
document_id: OIC-IMPLEMENTATION-PATTERNS
title: "Oracle Integration Cloud — APPSolve Implementation Patterns and Standard Practices"
version: "1.0"
created: "2026-06-15"
created_by: "WP11C — Oracle Integration Cloud Assumptions Pack"
status: "Active — To Be Updated After BU-OIC-005 and BU-OIC-006 Decisions"
applies_to: "All Oracle OIC implementations delivered by APPSolve"
kb_reference: "W4-INT-001-ORA-OICAccelerators.md | OIC_ASSUMPTIONS_V1.md"
---

# Oracle Integration Cloud — APPSolve Implementation Patterns

This document defines APPSolve's standard integration patterns, confirmed delivery approaches, and reusable design decisions for Oracle Integration Cloud (OIC) implementations. It is a living reference — updated as new patterns are confirmed and new accelerators are validated.

**Purpose:** Ensure consistent integration design across projects; reduce design time by documenting proven patterns; support estimate accuracy by linking patterns to complexity tiers; and provide bid managers with concrete integration examples for tender responses.

---

## 1. Standard APPSolve OIC Architecture Model

APPSolve implements Oracle OIC using the following architecture principles:

**1.1 Point-to-Point by Default**  
Every integration connects one source system to one target system. This keeps individual integration flows simple, independently deployable, and easier to test and troubleshoot. APPSolve does not implement ESB or hub-and-spoke topologies under standard OIC scope.

**1.2 Adapter-First Selection Order**  
For every integration, APPSolve selects the connection mechanism in this priority order:
1. Oracle-delivered adapter with an Oracle-signed connector (e.g., Oracle Fusion Applications Adapter for HCM/ERP, Oracle REST Adapter)
2. Standard REST API (vendor-published, OpenAPI-documented)
3. Standard SOAP API (vendor-published WSDL)
4. SFTP file-based (scheduled batch)
5. Oracle FTP Adapter with agreed file format
6. Database adapter (where direct database access is available and approved)

Custom adapter development is not in standard scope.

**1.3 Error-First Design**  
Every integration is designed with error handling defined before build commences. Error design covers: what happens on validation failure (reject record, send to error queue, notify); what happens on connection failure (retry, alert, escalate); what happens on transformation failure (log, alert, quarantine). Standard error handling pattern is documented in Section 4.

**1.4 Resubmit-Capable**  
All integrations are designed to allow failed messages to be resubmitted from the Oracle OIC Error Management console by the client's operations team without APPSolve intervention. This is a standard design principle for all OIC flows.

---

## 2. Confirmed Integration Patterns (Production Evidence)

The following patterns have been delivered in production by APPSolve and are confirmed for reuse.

### Pattern 1 — Oracle HCM to PaySpace (Bidirectional Payroll Interface)
**Reference:** Hollywood Bets Oracle Fusion HCM ↔ PaySpace, go-live July 2025 (W3S1-009)  
**Direction:** Bidirectional — HCM → PaySpace (employee master, salary, cost centre) AND PaySpace → HCM (payment confirmation, GL posting)  
**Protocol:** File-based (SFTP) for outbound; REST API where available for confirmation  
**Trigger:** Scheduled (payroll run cycle — typically monthly; additional ad hoc runs for salary changes)  
**Adapters:** Oracle FTP Adapter (outbound); Oracle REST Adapter (inbound confirmation)  
**Accelerator:** Yes — APPSolve HCM-PaySpace accelerator (W4-INT-001)  
**Complexity tier:** Standard  
**Key design decisions:**
- HCM → PaySpace: Payroll interface extract from Oracle OTBI or Oracle BI Publisher → SFTP drop → PaySpace picks up on schedule
- PaySpace → HCM: Payment confirmation file or GL posting → SFTP → OIC → HCM Payables or GL interface
- Error notification: File processing errors generate email alert to both APPSolve (during hypercare) and client payroll team
- Reconciliation: Client payroll team reconciles SFTP file record count to PaySpace processing confirmation

**Applicable to:** All Oracle HCM implementations where PaySpace is the payroll system of record (confirmed APPSolve standard for SA market)

---

### Pattern 2 — Oracle HCM to Biometric / Time and Labour System
**Reference:** Hollywood Bets Phase 3.3.1 (HCM Absence Management + Biometric Integration, W3S1-007 and W3S1-009)  
**Direction:** Bidirectional — HCM → Biometric (employee master, schedule) AND Biometric → HCM (clock-in/out data, attendance, absence events)  
**Protocol:** REST API (where biometric vendor exposes REST) or SFTP file-based  
**Trigger:** Near-real-time or scheduled (vendor-dependent)  
**Adapters:** Oracle REST Adapter or Oracle FTP Adapter  
**Complexity tier:** Standard to Complex (depends on biometric vendor API quality)  
**Key design decisions:**
- Biometric vendor's API quality is highly variable — always request API documentation before scoping
- Employee ID consistency between HCM and biometric system is critical — confirm primary key alignment before mapping workshop
- Shift schedule definition: confirmed in HCM or biometric system — design depends on system of record

---

### Pattern 3 — Oracle HCM to Background Check Provider
**Reference:** Scoped in HCM Recruiting Assumptions (REC-INT-004); no production evidence yet  
**Direction:** Bidirectional — HCM Recruiting → Background Check (candidate data) AND Background Check → HCM Recruiting (result / status)  
**Protocol:** REST API (most background check providers offer REST)  
**Adapters:** Oracle REST Adapter  
**Accelerator:** None confirmed — treat as Standard complexity  
**Complexity tier:** Standard  
**Key design decisions:**
- Vendor provides sandbox before SIT (most major providers do — Checkr, Sterling, LexisNexis)
- Candidate data contains PII — POPIA / GDPR consent management must be confirmed with client before design
- Integration triggers: Hiring manager initiates background check from Oracle Recruiting; result returned asynchronously

---

### Pattern 4 — Oracle Fusion ERP to Bank (via BeBanking)
**Reference:** BeBanking H2H payment file integrations — multiple production clients (W1S3-002, W1S3-003)  
**Direction:** Bidirectional — ERP (Oracle EBS or Fusion) → BeBanking (payment file) AND Bank → BeBanking → ERP (remittance / MT940 bank statement)  
**Protocol:** SFTP (BeBanking H2H is file-based — see W1S3-002 for technical details)  
**Adapters:** Oracle FTP Adapter  
**BeBanking specialist:** Carin Webb (sole BeBanking OIC resource — CONSULTANT_SKILL_MATRIX.md SPOF)  
**Complexity tier:** Standard (where using BeBanking standard connectors)  
**Key design decisions:**
- File format: ISO 20022 XML (pain.001) for outbound; MT940 or BAI2 for inbound bank statements
- Bank-side configuration (BeBanking connectivity setup) is BeBanking's responsibility — not OIC scope
- IP whitelisting at the bank is client's responsibility — coordinate with the specific bank's H2H onboarding team

---

### Pattern 5 — Oracle Recruiting to Job Board (LinkedIn / PNet)
**Reference:** Scoped in HCM Recruiting Assumptions (REC-INT-002); no separate OIC in scope — Oracle Recruiting has native job posting connectors  
**Note:** Oracle Recruiting Cloud (B87675) includes native job board posting connectors for LinkedIn and other major job boards. This integration does not typically require OIC. If the client's job board is not on Oracle's native connector list, OIC is used via REST. Confirm before scoping.

---

### Pattern 6 — Oracle HCM to HR Document Management System
**Reference:** Not yet in production — scoped in multiple proposals  
**Direction:** One-way — HCM events → Document Management (trigger document generation on hire, termination, contract change)  
**Protocol:** REST API or SFTP  
**Common target systems:** SharePoint Online, Google Drive, OpenText, DocuWare  
**Complexity tier:** Simple to Standard (depends on target system API)

---

### Pattern 7 — Oracle ERP to Financial Reporting / Analytics Extract
**Reference:** Multiple Oracle EBS and Fusion ERP clients  
**Direction:** One-way — Oracle ERP OTBI / BI Publisher extract → SFTP or REST → Target reporting system  
**Protocol:** SFTP file-based (standard) or REST (if target has inbound API)  
**Note:** For Oracle Analytics Cloud (OAX) as the target, the extraction mechanism is Oracle-native (FAW or OTBI direct connection) and does not require OIC. Only use OIC when extracting to a non-Oracle reporting platform.

---

## 3. Protocol Selection Guide

| Scenario | Recommended Protocol | Notes |
|---|---|---|
| Oracle HCM/ERP ↔ any endpoint | Oracle Fusion Applications Adapter | Native; lowest build effort; most reliable |
| Oracle system ↔ vendor with REST API | Oracle REST Adapter | Confirm vendor has OpenAPI/Swagger spec |
| Oracle system ↔ vendor with SOAP API | Oracle SOAP Adapter (WSDL required) | Higher build effort than REST |
| Oracle system ↔ legacy system / no API | Oracle FTP Adapter (SFTP) | Client must provide or procure SFTP server |
| Oracle system ↔ database (approved) | Oracle DB Adapter | Confirm DBA approval and connection credentials |
| Oracle HCM ↔ BeBanking | Oracle FTP Adapter | BeBanking is always file-based |
| Oracle Fusion ↔ Oracle Analytics | Native OTBI/FAW | OIC not required |
| Oracle HCM ↔ Oracle ERP (same tenant) | Oracle native API / FBDI | OIC adds unnecessary complexity for same-tenant flows |

---

## 4. Standard Error Handling Pattern

All APPSolve OIC integrations implement the following standard error handling framework:

**Layer 1 — Field Validation (before processing)**  
Check required fields, data type conformance, code-set validity, field length constraints. Action on failure: reject record, log error to OIC Error Management, send email alert, do not process batch until error is resolved (for file-based) or skip and continue (for real-time, where client has approved record-skipping).

**Layer 2 — Connection Errors (during processing)**  
Detect target system unavailability (HTTP 5xx, connection timeout, SFTP connection failure). Action: implement retry (3 attempts, exponential backoff — 1 min, 5 min, 15 min). After 3 failures: alert recipient via email; quarantine failed messages in OIC Error Management for manual resubmit.

**Layer 3 — Business Validation Errors (returned by target)**  
Target system returns a business error (HTTP 4xx, SOAP fault, business rule violation in error response). Action: log the error response, notify alert recipient, mark message as failed in OIC Error Management for client review. APPSolve resolves build errors; business validation errors are the client's responsibility.

**Layer 4 — Resubmit Capability**  
All failed messages are available for resubmit from the OIC Error Management console. The client's operations team can resubmit individual messages or bulk resubmit after the root cause is resolved. APPSolve trains the client's OIC administrator on resubmit procedures during admin training.

---

## 5. Security Patterns

**5.1 Authentication Decision Matrix**

| Scenario | Authentication | Notes |
|---|---|---|
| Oracle HCM/ERP endpoint | Oracle Fusion App Adapter credentials | OAuth 2.0 via Fusion App adapter — APPSolve configures |
| REST vendor with OAuth 2.0 | OAuth 2.0 client credentials | Client provides client_id and client_secret |
| REST vendor with Basic Auth | Basic Authentication | Username + password; less secure — document in TDD |
| REST vendor with API key | Custom header / query param | APPSolve configures per vendor spec |
| SFTP endpoint | SSH key or password | SSH key preferred; client generates key pair; APPSolve configures public key in OIC |
| mTLS required | Certificate-based | Client procures client certificate; APPSolve configures in OIC |

**5.2 Service Account Naming Convention**  
APPSolve recommends that clients follow this naming convention for OIC service accounts: `svc_oic_[source]_[target]` (e.g., `svc_oic_hcm_payspace`, `svc_oic_erp_bebanking`). This convention makes service accounts identifiable in access reviews and distinguishable from user accounts.

---

## 6. Integration Complexity Tier Model (BU-OIC-005 Confirmed — 2026-06-15)

APPSolve's three-tier complexity model is the confirmed basis for all OIC integration estimates. Every integration in the Integration Inventory is assigned a tier during Scope and Design. The tier is documented in the project estimate. No automatic effort discount is applied by tier — the tier informs the estimate; the bid manager determines effort per phase.

| Tier | Confirmed Criteria | Effort Rate Card |
|---|---|---|
| **Simple** | One source, one target. Standard Oracle adapter. Limited transformation — direct field mapping, minimal lookups. No orchestration. Standard auth (OAuth 2.0 or Basic Auth). Small to medium payload. Well-documented vendor API with sandbox. | See GAP-OIC-002 — Effort Rate Card pending |
| **Standard** | One source, one target. Moderate transformation — code-set lookups, conditional logic, data splitting. Standard error handling and retry. Typical payload. Reasonably documented vendor API. | See GAP-OIC-002 — Effort Rate Card pending |
| **Complex** | Multi-step orchestration or multiple objects per flow. Complex transformations — calculations, aggregations, multi-level branching. High-volume or near-real-time. Non-standard adapter or complex auth (mTLS, JWT, custom token). No vendor sandbox. | See GAP-OIC-002 — Effort Rate Card pending |

*Effort ranges per tier to be documented in OIC Effort Rate Card (GAP-OIC-002).*

**BU Lead action required:** Confirm tier definitions above and provide effort ranges per tier per phase (design / build / SIT / UAT support / cutover). This will form the OIC Effort Rate Card (GAP-OIC-002).

---

## 7. Accelerator Library (BU-OIC-006 Confirmed — Per-Integration Assessment Required)

**No automatic accelerator discounts are applied.** Accelerator applicability is assessed per integration during estimation. Where confirmed applicable, the effort reduction is documented explicitly in the project estimate.

Reference W4-INT-001-ORA-OICAccelerators.md for detailed accelerator documentation.

| Accelerator | Integration Pattern | Applicable Tiers | Effort Reduction | Production Status |
|---|---|---|---|---|
| HCM-PaySpace Payroll Interface | Oracle HCM → PaySpace (SFTP outbound) | Standard | To be confirmed | Confirmed (W4-INT-001, HB production) |
| PaySpace-HCM GL Confirmation | PaySpace → Oracle HCM (SFTP inbound) | Standard | To be confirmed | Confirmed (W4-INT-001, HB production) |
| HCM Biometric Employee Master | Oracle HCM → Biometric system | Standard | To be confirmed | Confirmed (W4-INT-001, HB production) |
| BeBanking H2H Payment File | Oracle ERP → BeBanking SFTP | Standard | To be confirmed | Confirmed (BeBanking production) |
| BeBanking MT940 Inbound | BeBanking → Oracle ERP bank statement | Standard | To be confirmed | Confirmed (BeBanking production) |
| Oracle HCM OTBI Payroll Extract | OTBI report → SFTP drop → Payroll | Simple | To be confirmed | Confirmed (multiple clients) |

**BU Lead action required:** Review the above accelerator list, add any missing confirmed accelerators from W4-INT-001, confirm production-ready status of each, and assign effort reduction percentage per tier.

---

## 8. SFTP Infrastructure Decision Tree

When a client's integration endpoint does not support REST or SOAP API, SFTP file-based integration is the fallback. The following decision tree defines SFTP server responsibility:

```
Does the target/source system have an SFTP server?
  YES → Use client's SFTP server. Client provides: host, port, directory, credentials.
  NO  → Does the client have a cloud SFTP service (AWS Transfer Family / Azure SFTP / SFTP-as-a-service)?
          YES → Use client's cloud SFTP. Client provisions and provides credentials.
          NO  → Does Oracle OCI have a managed SFTP option in scope?
                  YES → Assess OCI-hosted SFTP as project infrastructure item (separately scoped).
                  NO  → Client must procure an SFTP server before file-based integration can proceed.
                        APPSolve does not provision, host, or manage SFTP infrastructure.
```

**Standard SFTP design parameters confirmed with client before design:**
- Host (FQDN or IP)
- Port (default 22)
- Directory structure (inbound / outbound / archive)
- File naming convention (include date/time stamp)
- File format (CSV, XML, JSON, fixed-width)
- Transfer protocol confirmation (SFTP vs FTP vs FTPS — SFTP strongly preferred)
- Authentication (SSH key preferred; password accepted)
- Retention / archive policy (how long does the SFTP directory hold files before purge)

---

## 9. OIC Monitoring Operations Guide (Client Handover Reference)

This section summarises what APPSolve trains the client's OIC administrator on during admin training (OIC-TST-001 UAT phase).

**9.1 Viewing Integration Activity**  
Oracle OIC → Monitoring → Activity Stream. Shows all integration executions (successful, failed, in-progress). Filter by integration, date range, status.

**9.2 Investigating a Failed Integration**  
Click on a failed instance in the Activity Stream. View the error details panel — shows the failed step, the error message, and the payload at the point of failure. Download the failed payload for root-cause analysis.

**9.3 Resubmitting a Failed Message**  
For integrations configured to allow resubmission: from the Activity Stream, select the failed instance, click Resubmit. Check the Resubmit button is enabled (APPSolve configures resubmit capability in all standard integrations per Section 4).

**9.4 Managing Error Notifications**  
Oracle OIC sends email alerts on integration failure to the configured recipients (confirmed in OIC-MON-002). Alert email contains: integration name, failure time, error summary, link to OIC console.

**9.5 Checking Connection Health**  
Oracle OIC → Design → Connections. Click Test on any connection to verify current connectivity status. Run connection tests after firewall changes, certificate renewals, or vendor API maintenance windows.

---

*OIC_IMPLEMENTATION_PATTERNS v1.0 | WP11C — Oracle Integration Cloud Assumptions Pack | 2026-06-15*  
*Sections 6 and 7 pending BU-OIC-005 and BU-OIC-006 BU Lead decisions*  
*Living document — update as new accelerators are validated and new patterns confirmed in production*
