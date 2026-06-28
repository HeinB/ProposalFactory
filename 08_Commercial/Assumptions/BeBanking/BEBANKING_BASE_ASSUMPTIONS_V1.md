---
title: BeBanking Base Assumption Pack
version: v1.0-Approved
status: Approved v1.0
pack_code: BB
section_range: "140–153"
assumption_count: 117
bu_lead_decisions_pending: []
bu_lead_decisions_resolved:
  - BU-BB-001
  - BU-BB-002
  - BU-BB-003
  - BU-BB-004
  - BU-BB-005
  - BU-BB-006
  - BU-BB-007
  - BU-BB-008
  - BU-BB-009
  - BU-BB-010
created: WP11J
created_date: 2026-06-16
last_updated: WP14F
last_updated_date: 2026-06-18
approved_for_reuse: Yes
lifecycle_status: APPROVED
approval_date: 2026-06-18
approval_programme: WP14F
---

# BeBanking Base Assumption Pack

**Pack:** BB | **Sections:** 140–153 | **Assumptions:** 117 | **Status:** Approved v1.0 | **Approved:** 2026-06-18 (WP14F)

> **APPROVED FOR USE.** This pack is Approved v1.0. All 10 BU Lead decisions resolved (BU-BB-001 through BU-BB-010). This pack may be included in BeBanking client-facing proposals and tender submissions.

> **Governance:** BeBanking is APPSolve's proprietary banking integration platform. All assumptions in this pack apply to BeBanking implementations only. Infrastructure assumptions for OCI-hosted BeBanking environments are governed by the OCI Pack. ERP-side integration assumptions are governed by the applicable ERP Pack. OIC middleware assumptions are governed by the OIC Pack. AMS support tier assumptions are governed by the AMS Pack.

---

## Section Index

| Section | Code | Topic | Count |
|---|---|---|---|
| 140 | BB-GEN | General Engagement | 8 |
| 141 | BB-BNK | Banking Relationships | 10 |
| 142 | BB-PAY | Payments | 12 |
| 143 | BB-PYR | Payroll Payments | 9 |
| 144 | BB-FX | Forex Payments | 8 |
| 145 | BB-INT | Integrations | 12 |
| 146 | BB-SEC | Security and Access Control | 8 |
| 147 | BB-DAT | Data and Retention | 8 |
| 148 | BB-RPT | Reporting | 5 |
| 149 | BB-ENV | Environments | 5 |
| 150 | BB-CUT | Cutover and Go-Live | 6 |
| 151 | BB-SUP | Support and Managed Services | 8 |
| 152 | BB-EXC | Explicit Exclusions | 10 |
| 153 | BB-EXT | External Dependencies | 8 |
| **Total** | | | **117** |

---

## Section 140 — BB-GEN: General Engagement

**BB-GEN-001:** BeBanking is APPSolve's proprietary Host-to-Host banking integration platform. All BeBanking implementations are delivered exclusively by APPSolve as both the platform vendor and the implementation partner.

**BB-GEN-002:** BeBanking onboarding is scoped per client engagement. The BB Base Assumptions define the standard boundaries for a single-entity, single-country BeBanking implementation. Multi-entity or multi-country implementations are separately scoped and priced.

**BB-GEN-003:** BeBanking is delivered as a managed application hosted and operated by APPSolve. Clients do not receive source code, platform binaries, database access, or direct access to the BeBanking application infrastructure.

**BB-GEN-004:** BeBanking is a payment processing and banking integration platform. It is not an ERP system and does not replace the client's ERP, accounting system, or payroll system of record. All payment instructions originate from the client's ERP and all results are returned to it.

**BB-GEN-005:** All BeBanking implementations include an onboarding project phase covering: platform configuration, bank connectivity setup, ERP integration, user access configuration, and go-live readiness testing. The minimum standard onboarding period is 6 weeks from project kick-off to go-live readiness. Complex implementations involving multiple banks, multiple payment types, or multiple ERP sources may require 12–20 weeks.

**BB-GEN-006:** APPSolve assigns a BeBanking Solution Consultant as the primary APPSolve delivery contact for all onboarding engagements. Where a dedicated Project Manager is required, this is explicitly stated in the Statement of Work. Where a dedicated APPSolve PM is not in scope, the client's Project Manager coordinates overall delivery and APPSolve's Solution Consultant manages BeBanking-side activities.

**BB-GEN-007:** BeBanking onboarding is executed in sequential phases: (a) Discovery and scoping; (b) Platform configuration; (c) Bank connectivity and format testing; (d) ERP integration testing; (e) User acceptance testing; (f) Go-live cutover. Each phase requires written client sign-off before the subsequent phase commences.

**BB-GEN-008:** BeBanking licensing is subscription-based. The subscription tier, supported bank list, included payment types, and transaction volume limits applicable to the client are confirmed in the commercial schedule before onboarding commences. Transaction volumes or payment types that exceed the subscribed tier require a subscription amendment.

---

## Section 141 — BB-BNK: Banking Relationships

**BB-BNK-001:** BeBanking currently supports the following banking partners: South African — ABSA, FNB, Nedbank, Standard Bank, and Investec; International — Citi Bank UK and Santander Bank Chile. Standard Bank and Nedbank Common Monetary Area integrations are covered. Connectivity to any bank not on this list requires a new bank onboarding assessment and is separately scoped.

**BB-BNK-002:** BeBanking connects to client banks using bank-sanctioned connectivity mechanisms. APPSolve does not hold or claim direct SWIFT membership. All cross-border and inter-bank payment instructions are transmitted through the client's bank, which acts as the SWIFT intermediary.

**BB-BNK-003:** Each new bank connectivity requires a formal registration and certification process between APPSolve and the bank. Bank onboarding timelines, approval processes, and certification requirements are controlled by the bank and outside APPSolve's control. Standard bank onboarding is assumed to take 4–8 weeks from bank registration submission to confirmed production connectivity approval.

**BB-BNK-004:** The client is responsible for maintaining their bank account structure (account numbers, branch codes, beneficiary payment limits, authorised signatories, and payment channel agreements) with their bank. APPSolve configures BeBanking to use the client's confirmed account structure. Changes to the bank account structure after BeBanking configuration are a Change Request.

**BB-BNK-005:** BeBanking does not hold client funds, operate as a payment service provider, or act as a licensed financial institution. All payment instructions are transmitted from the client's designated bank accounts via the client's bank under the client's payment authority. APPSolve's role is to transmit payment files to the bank on behalf of the client.

**BB-BNK-006:** The client is responsible for establishing and maintaining all bank agreements required for BeBanking to operate. This includes: Host-to-Host agreements, bulk payment facility agreements, SFTP or API access agreements, and any bank-specific channel activation requirements. These agreements must be in place and confirmed before BeBanking bank connectivity testing begins.

**BB-BNK-007:** BeBanking supports SFTP-based and API-based connectivity with banks. The specific connectivity method used for each bank is determined during the bank onboarding assessment. Where a bank supports multiple connectivity methods, APPSolve recommends the most reliable and maintainable method available.

**BB-BNK-008:** Bank file format specifications — payment file layouts, statement file layouts, and acknowledgement file layouts — are bank-defined and may be updated by the bank. APPSolve implements BeBanking to the bank's published specification at the time of onboarding. Bank-initiated format changes post-go-live are addressed under the agreed support or AMS arrangement and are assessed per BB-SUP-007.

**BB-BNK-009:** Namibian banking connectivity (Nedbank Namibia, Standard Bank Namibia) is available where the client has confirmed banking relationships with those entities. Namibian H2H implementations carry additional onboarding effort compared to South African implementations and are separately scoped.

**BB-BNK-010:** BeBanking does not include cash management, overdraft facility management, interest calculation, or treasury management functions. BeBanking is a payment instruction and bank statement processing platform only.

---

## Section 142 — BB-PAY: Payments

**BB-PAY-001:** BeBanking supports Electronic Funds Transfer (EFT) credit payments, including supplier payments, intercompany payments, and miscellaneous creditor payments. EFT debit (debit order) processing is not included in the standard BeBanking scope.

**BB-PAY-002:** Payment batches are initiated by the client's ERP or financial system and transmitted to BeBanking for bank submission. BeBanking does not originate payment instructions independently of the client's ERP. All payment authority rests with the client's ERP data and the client's authorised approvers in BeBanking.

**BB-PAY-003:** BeBanking supports a configurable payment authorisation workflow. The standard implementation includes a two-level maker-checker model: a Payment Creator initiates the batch and a Payment Authoriser approves it before submission to the bank. Additional authorisation levels, value-based approval tiers, or workflow branching beyond the standard two-level model are a separately scoped configuration item.

**BB-PAY-004:** BeBanking performs Account Verification Service (AVS) checks when new or changed bank details are received before submitting EFT payments to the bank where the client's bank supports this service. AVS confirms that the beneficiary account number, branch code, and legal owner are valid before payment submission. AVS charges levied by the bank are the client's responsibility. Where the client's bank does not offer AVS, this step is omitted.

**BB-PAY-005:** BeBanking returns bank acknowledgement and payment result status to the originating ERP. The format and timing of bank acknowledgements are bank-defined. BeBanking transmits acknowledgements as received from the bank. APPSolve is not responsible for bank processing delays, bank system outages, or bank rejection reasons outside BeBanking's control.

**BB-PAY-006:** Standard remittance advice generation and distribution is included in the BeBanking implementation. Standard remittance advice is delivered to beneficiaries via email using the beneficiary email address held in the client's ERP. Custom remittance advice formats, branded templates, delivery via SMS, or delivery through a self-service portal are separately scoped.

**BB-PAY-007:** Beneficiary master data — supplier bank account numbers, payment references, and remittance email addresses — is owned and maintained by the client in their ERP. BeBanking consumes beneficiary data from the ERP at the time of payment batch processing. APPSolve does not maintain a separate beneficiary master in BeBanking.

**BB-PAY-008:** Duplicate payment detection is a standard BeBanking control. BeBanking flags potential duplicate payments (same beneficiary, within a configurable detection window) before bank submission. The duplicate detection parameters are agreed and configured during onboarding. Changes to detection parameters post-go-live are a Change Request.

**BB-PAY-009:** Real-time gross settlement (RTGS) is supported where the client's bank offers this service and the client holds the required bank agreements. RTGS carries higher transaction fees levied by the bank. These fees are the client's responsibility and are not included in BeBanking's subscription cost.

**BB-PAY-010:** BeBanking maintains payment instruction records for audit and dispute resolution purposes. Approved payment instructions cannot be reversed or recalled through BeBanking after the payment file has been submitted to and accepted by the bank. Payment recalls and reversals must be initiated directly with the bank by the client.

**BB-PAY-011:** Intercompany EFT payments between entities using the same BeBanking implementation are supported within the standard scope. Cross-instance intercompany payments (where each entity operates a separate BeBanking instance) require a separately scoped integration design.

**BB-PAY-012:** Scheduled payment runs (configuring BeBanking to submit payment batches at specified times) are a standard BeBanking capability. Payment run schedules are agreed and configured during onboarding. Modifications to payment run schedules post-go-live are managed under the support arrangement.

---

## Section 143 — BB-PYR: Payroll Payments

**BB-PYR-001:** BeBanking supports payroll payment disbursement via EFT. Payroll payment instructions are generated by the client's payroll system and transmitted to BeBanking for bank submission. BeBanking does not perform payroll calculations, statutory deduction processing, payslip generation, or IRP5 production.

**BB-PYR-002:** BeBanking Payroll H2H currently supports payroll payment files originating from Oracle EBS Payroll and PaySpace. These are APPSolve's primary supported payroll source platforms. Payroll files originating from other payroll systems require a separate payroll integration assessment at pre-sales. Other payroll source integration is not covered by BB-PYR assumptions without explicit SOW inclusion.

**BB-PYR-003:** Employee bank account data used for payroll disbursement is owned and maintained by the client's HR or payroll system. BeBanking consumes employee payment data as provided in the payroll payment file. APPSolve does not validate, maintain, or independently verify employee bank account details within BeBanking.

**BB-PYR-004:** Payroll payment confidentiality controls are enforced within BeBanking. Payroll payment batches are restricted to authorised payroll users. Payroll transactions are segregated from creditor payment transactions and are not visible to standard AP payment users.

**BB-PYR-005:** BeBanking supports split payroll disbursements (payment to multiple bank accounts per employee per payroll run) where the originating payroll system's payment file includes the individual split payment instructions.

**BB-PYR-007:** Payroll payment cutoff times and same-day processing eligibility are governed by the client's bank's payroll batch acceptance windows. APPSolve configures BeBanking to submit payroll files within the bank's required processing window. The client is responsible for completing payroll runs and initiating the BeBanking submission in sufficient time for the bank to process within the required value date.

**BB-PYR-008:** Payroll payment reversals and recalls follow the same bank-driven process as EFT payment reversals (BB-PAY-010). BeBanking cannot reverse or recall a payroll payment after it has been accepted by the bank. The client must liaise directly with their bank to initiate any payment recall.

**BB-PYR-009:** Payroll payment result reconciliation — confirming accepted, rejected, and returned employee payments — is returned to the client's payroll or ERP system via BeBanking's acknowledgement mechanism. The reconciliation file format is defined by the integration design agreed during onboarding.

**BB-PYR-010:** Where the client operates multiple payroll runs within a single period (for example, weekly casual staff and monthly permanent staff, or multiple legal entities with separate payroll runs), each payroll run configuration and schedule is defined and separately confirmed during onboarding.

---

## Section 144 — BB-FX: Forex Payments

**BB-FX-001:** BeBanking supports foreign exchange payment initiation for international supplier payments and cross-border disbursements. BeBanking transmits foreign currency payment instructions to the client's bank; the bank executes the forex transaction at the agreed exchange rate. BeBanking is not a forex trading platform and does not hold, manage, or price foreign currency positions.

**BB-FX-002:** BeBanking currently supports forex payment processing through Citi Bank UK, ABSA, Nedbank, and FNB. Forex payment processing through other banking partners requires a new forex bank onboarding assessment and is separately scoped.

**BB-FX-003:** The client is responsible for maintaining a SARB-compliant forex mandate with their bank, including the approved foreign currency list, approved country list, and applicable forex allowances. BeBanking facilitates the transmission of forex payment instructions only. Compliance with SARB exchange control regulations is the client's legal and regulatory responsibility.

**BB-FX-004:** BeBanking supports foreign currency payment instructions in the currencies enabled by the client's bank forex agreement. Currency additions after go-live are confirmed with the client's bank and may trigger a BeBanking configuration Change Request.

**BB-FX-005:** Foreign exchange rates are determined by the client's bank at the time of transaction execution. BeBanking does not calculate, display, fix, or negotiate exchange rates. Where the client requires rate confirmation or forward cover booking before payment execution, these arrangements are made between the client and their bank outside BeBanking.

**BB-FX-006:** Supporting documentation required by SARB for forex payments — invoices, contracts, shipping documents, Balance of Payments (BoP) category declarations — is the client's responsibility to obtain and submit. BeBanking does not validate forex supporting documentation. SARB documentation is submitted by the client through the bank's forex documentation channel.

**BB-FX-007:** Forex payment reconciliation returns the same acknowledgement data as domestic EFT payments. Additional forex-specific fields (exchange rate applied, settlement date, SARB reference number) are returned where provided by the client's bank; availability of these fields is bank-dependent and not guaranteed across all forex banking partners.

**BB-FX-008:** Inward forex remittance — receiving international payments into the client's bank account — is not a BeBanking function. BeBanking processes outward payment instructions only. Inward payment processing, bank statement import, and ERP reconciliation of received funds are governed by bank statement import functionality (BB-INT-008) and the applicable ERP Pack.

---

## Section 145 — BB-INT: Integrations

**BB-INT-001:** BeBanking integrates with the client's ERP or financial system to receive payment instructions and return payment results. The ERP integration is a mandatory component of every BeBanking implementation. Integration scope — ERP platform, integration method, data objects, and transaction volumes — is confirmed during the onboarding discovery phase and documented in an integration design document.

**BB-INT-002:** BeBanking supports integration with Oracle EBS, Oracle Fusion Applications, Acumatica ERP, and PaySpace. BeBanking can integrate with SAP and Sage for payroll, with the client taking responsibility for the integration. ERP-side integration assumptions are governed by the applicable ERP Pack (Oracle ERP Pack for Oracle ERP or Acumatica Pack for Acumatica). BB-INT assumptions govern BeBanking-side configuration only.

**BB-INT-003:** BeBanking supports API-based integration (REST), SFTP-based file exchange, and structured bank file exchange mechanisms. The preferred integration method for each client and ERP combination is determined during the onboarding discovery phase. Where multiple methods are technically available, APPSolve recommends the most reliable and maintainable approach.

**BB-INT-004:** ERP-side integration configuration — AP payment format setup, bank account configuration in the ERP, payment batch extract processes, and ERP-side bank statement import processing — is the responsibility of the ERP implementation team or the client's ERP support team. BeBanking-side configuration is APPSolve's responsibility. The demarcation between ERP-side and BeBanking-side responsibilities is agreed in the integration design document.

**BB-INT-005:** Where Oracle Integration Cloud (OIC) is used as middleware between the client's ERP and BeBanking, the OIC integration components — adapters, process flows, connection definitions — are governed by the OIC Assumption Pack. BB-INT assumptions govern BeBanking-side configuration only. The use of OIC as middleware is confirmed at pre-sales in the Statement of Work.

**BB-INT-006:** The standard BeBanking implementation integrates with a single ERP instance as the payment instruction source. Multi-ERP or multi-instance integrations (different ERP platforms or separate ERP instances feeding a single BeBanking environment) are separately scoped.

**BB-INT-007:** Integration testing covers: (a) payment file format validation; (b) payment instruction transmission and acknowledgement; (c) payment result return to ERP; (d) bank statement import and format validation; (e) reconciliation data matching. Integration testing is conducted in the BeBanking UAT environment before production go-live and requires active participation from the client's ERP team.

**BB-INT-008:** Bank statement import — receiving electronic bank statements from the client's bank, processing them within BeBanking, and returning the statement data to the client's ERP for bank reconciliation — is included in the standard implementation for the banks in scope. ERP-side bank statement processing (upload, automatic matching, posting, and clearing) is the ERP team's responsibility and governed by the applicable ERP Pack.

**BB-INT-009:** SFTP-based integration requires a secure SFTP server. APPSolve provides the BeBanking SFTP endpoint. The client's ERP team is responsible for configuring the ERP SFTP client and the outbound payment extract process. SFTP firewall rules and IP whitelisting are the client's network team's responsibility.

**BB-INT-010:** API-based integration requires the client's ERP to call BeBanking's published REST API endpoints. APPSolve provides API specifications during onboarding. Changes to BeBanking API versions that affect client integrations are communicated to affected clients with a minimum of 60 days advance notice before the prior version is deprecated.

**BB-INT-011:** Third-party system integrations — non-ERP systems such as treasury management platforms, procurement portals, expense management tools, or standalone accounts payable solutions — requiring connectivity to BeBanking are separately scoped and assessed at pre-sales.

**BB-INT-012:** BeBanking does not consume real-time market data, currency rate APIs, or bank rate feeds from external data providers. All market-rate information is sourced from the client's bank as part of the forex transaction execution process.

---

## Section 146 — BB-SEC: Security and Access Control

**BB-SEC-001:** BeBanking implements role-based access control. Standard roles are: Payment Creator (creates and submits payment batches for approval), Payment Authoriser (approves payment batches for bank submission), Bank Administrator (manages bank account configurations and beneficiary lists), and System Administrator (manages users and system configuration). Additional roles or role modifications beyond the standard set are a configuration Change Request.

**BB-SEC-002:** User provisioning and deprovisioning is the client's operational responsibility. The client's designated BeBanking System Administrator manages the addition, modification, and removal of user accounts. APPSolve configures the initial user accounts during onboarding. Ongoing user management is a client function and is not a BeBanking support activity.

**BB-SEC-003:** BeBanking enforces dual authorisation (maker-checker) for all payment batches as a non-negotiable platform control. A user who creates a payment batch cannot also approve it for bank submission. This segregation of duties control cannot be disabled or bypassed.

**BB-SEC-004:** BeBanking supports multi-factor authentication (MFA) for user access. The MFA mechanism (email OTP, TOTP authenticator app, or equivalent) is confirmed during onboarding.

**BB-SEC-005:** All data transmitted between BeBanking and the client's bank is encrypted in transit using TLS 1.2 or higher. Data at rest within the BeBanking application is encrypted using AES-256 or an equivalent standard. The specific encryption standards in use are documented in the BeBanking Security Architecture document provided at onboarding.

**BB-SEC-006:** BeBanking conducts periodic platform-level security reviews. Where a client requires a dedicated security assessment, penetration test, or audit of the BeBanking platform, this is separately scoped and may require coordination between APPSolve, the client's security team, and the client's bank.

**BB-SEC-007:** BeBanking access logs and full payment audit trails are retained within the platform for the retention period specified in BB-DAT-001. Clients may export audit logs during the retention period via the standard BeBanking reporting capability. Integration of BeBanking audit logs with the client's SIEM, SOAR, or centralised log management platform is separately scoped.

**BB-SEC-008:** The client is responsible for the security of their own network, end-user devices, and credentials used to access BeBanking. APPSolve is not responsible for security incidents arising from compromised client credentials, client-side malware, client network vulnerabilities, or social engineering attacks targeting the client's BeBanking users.

---

## Section 147 — BB-DAT: Data and Retention

**BB-DAT-001:** BeBanking retains payment instruction records, payment results, bank statements, and audit logs for a minimum of 7 years from the transaction date, consistent with South African financial record-keeping requirements under the Companies Act and SARS requirements. Clients requiring retention periods exceeding 7 years must specify this requirement in the commercial schedule.

**BB-DAT-002:** Bank statement data received by BeBanking from the client's bank is stored in the BeBanking database and made available for reconciliation, reporting, and audit purposes throughout the retention period. Bank statement data is not archived off the BeBanking platform during the active retention period.

**BB-DAT-003:** All client payment data is the client's data. APPSolve does not use client payment data for any purpose other than operating the BeBanking service for that client. Client data is not shared with other clients, used for benchmarking, or disclosed to third parties except where required by law.

**BB-DAT-004:** Historical payment data migration — loading prior-period payment transactions into BeBanking from a legacy payment system — is not included in the standard onboarding scope. BeBanking captures transactions from the go-live date forward. Historical data migration, where required, is separately scoped and assessed.

**BB-DAT-005:** BeBanking does not maintain a standing beneficiary master database independently of the client's ERP. Beneficiary data is consumed from the client's ERP at the time of payment batch submission. Where a BeBanking-side beneficiary whitelist is required as an additional fraud prevention control, this is a separately scoped configuration item.

**BB-DAT-006:** POPIA: BeBanking processes personal information (employee bank account details for payroll disbursement, individual supplier banking details) as an operator acting on behalf of the client, who is the responsible party under POPIA. APPSolve operates BeBanking in accordance with its obligations as a POPIA Data Processor. The client, as responsible party, remains accountable for the lawful basis for processing personal information through BeBanking and for issuing appropriate data subject notices.

**BB-DAT-007:** BeBanking production data for South African clients is hosted in South African data centre regions. Clients with data residency requirements (POPIA, sector-specific regulations, or contractual obligations) must confirm data residency availability with APPSolve during pre-sales. For OCI-hosted BeBanking environments, data residency assumptions are governed by the OCI Pack. For AWS-hosted environments, data residency is confirmed in the relevant SOW.

**BB-DAT-008:** BeBanking database backups are performed at a frequency consistent with the RPO targets specified in the client's BeBanking subscription agreement. Backup and recovery procedures are APPSolve's operational responsibility. Clients do not have access to the BeBanking database backup files.

---

## Section 148 — BB-RPT: Reporting

**BB-RPT-001:** The standard BeBanking reporting pack includes: (a) Payment Batch Status Report — open, pending, submitted, and completed batches; (b) Payment Register Report — including invoice details; (c) Bank Account Approval Report — listing processed and pending approvals; (d) Remittance Advice — proof of payment sent to supplier; (e) Email Error Report — indicating non-delivery reasons; (f) Roles Report — listing access granted. All standard reports are available within the BeBanking application and exportable in PDF format.

**BB-RPT-002:** Custom reports, scheduled report distribution, management dashboards, or analytics integrations (Power BI, Tableau, or similar BI tools) are not included in the standard BeBanking implementation. Custom reporting capability is separately scoped.

**BB-RPT-003:** BeBanking does not produce general ledger reconciliation reports. GL reconciliation of bank statement entries against ERP transactions is performed in the client's ERP using bank statement data imported via BeBanking. The ERP-side reconciliation process is governed by the applicable ERP Pack.

**BB-RPT-004:** Payment exception reporting — rejected payments, returned payments, and failed bank submissions — is available in real-time within the BeBanking application. Email notification of exceptions is configurable during onboarding and is included in the standard implementation.

**BB-RPT-006:** Standard report formats and layouts are delivered as part of onboarding and are confirmed during the discovery phase. Modifications to standard report formats or the addition of new standard reports after go-live are Change Requests.

---

## Section 149 — BB-ENV: Environments

**BB-ENV-001:** The standard BeBanking environment configuration includes: (a) Production environment; and (b) User Acceptance Testing (UAT) environment. A dedicated Development environment is not provided as standard. Where a dedicated integration development or staging environment is required, this is separately scoped.

**BB-ENV-002:** The UAT environment mirrors the Production configuration and is used for integration testing, user acceptance testing, and regression testing of updates. The UAT environment uses bank sandbox or test connectivity where the client's bank provides a sandbox facility. Where the client's bank does not offer a sandbox, testing is conducted using controlled test transactions in a bank-approved test window.

**BB-ENV-003:** The UAT environment is available to the client during the onboarding period for acceptance testing and after go-live for regression testing of platform updates. The UAT environment is included in the standard BeBanking subscription. Decommissioning the UAT environment after go-live is strongly discouraged, as it removes APPSolve's ability to test updates before production deployment.

**BB-ENV-004:** BeBanking Production environment availability is governed by the uptime SLA in the client's BeBanking subscription agreement. Planned maintenance windows are communicated to clients with a minimum of 48 hours advance notice. Emergency maintenance — security patches and critical fixes — may be applied with shorter notice where required to protect platform or bank connectivity integrity.

**BB-ENV-005:** BeBanking platform updates and version upgrades are applied by APPSolve. Clients do not manage BeBanking application software. The standard update process is: (a) APPSolve applies update to UAT; (b) APPSolve conducts internal testing on critical processes; (c) client UAT users complete regression testing and provide written sign-off; (d) APPSolve applies update to Production. No Production update proceeds without written client sign-off from step (c).

---

## Section 150 — BB-CUT: Cutover and Go-Live

**BB-CUT-001:** BeBanking production go-live is authorised only after all of the following conditions are confirmed: (a) bank connectivity tested and approved in the Production environment; (b) ERP integration tested and client-accepted in the UAT environment; (c) all user accounts configured, tested, and user access confirmed; (d) written UAT sign-off received from the client; (e) dual authorisation control verified operational with at least two live authorised users. All five conditions must be satisfied before any production payment is initiated through BeBanking.

**BB-CUT-002:** Go-live support — APPSolve's BeBanking Solution Consultant available for the first production payment cycle — is included in the onboarding scope. Go-live support covers the first 1–3 business days of production payment processing. Extended hypercare beyond the standard go-live support period is separately defined.

**BB-CUT-003:** Parallel running of the legacy payment process alongside BeBanking is the client's decision. APPSolve supports parallel run planning and provides a parallel run checklist. The operational effort and cost of running legacy and BeBanking payments simultaneously is the client's responsibility. A maximum parallel run period of 4 weeks is assumed; extended parallel running requires explicit BU Lead approval.

**BB-CUT-004:** The client's bank must confirm production connectivity approval before BeBanking production payment processing begins. Bank connectivity certification is a bank-controlled process; APPSolve cannot override or accelerate bank certification requirements.

**BB-CUT-005:** Go-live cutover includes deactivating the legacy payment export process from the client's ERP and activating BeBanking as the sole payment origination channel for in-scope payment types. The deactivation of the legacy payment process in the ERP is the client's ERP team's responsibility. APPSolve provides a BeBanking cutover checklist and confirms BeBanking readiness.

**BB-CUT-006:** Where the client is onboarding multiple payment types (EFT, payroll, and forex) simultaneously, a phased cutover approach — going live with one payment type at a time — is recommended. Simultaneous cutover of all payment types in a single event is higher risk and requires explicit client acceptance documented in the project sign-off.

---

## Section 151 — BB-SUP: Support and Managed Services

**BB-SUP-001:** Post-go-live BeBanking support is provided under a BeBanking Support arrangement included in or accompanying the client's BeBanking subscription. Support scope, SLA tiers, and included services are defined in the applicable BeBanking support schedule. Where no formal BeBanking support arrangement is in place at go-live, APPSolve provides reactive platform-level break/fix support only.

**BB-SUP-002:** BeBanking support covers the BeBanking application layer and BeBanking-side bank connectivity. Bank-side issues — bank SFTP or API outages, bank format changes initiated by the bank, bank processing delays, and bank payment rejections — are the client's responsibility to resolve directly with their bank. APPSolve assists with diagnosis and escalation within its capability but cannot compel banks to resolve issues on a specific timeline.

**BB-SUP-003:** ERP-side issues — payment batch generation failures, ERP integration errors, and AP module configuration faults — are governed by the applicable ERP AMS arrangement, not the BeBanking support arrangement. Where ERP-BeBanking boundary disputes arise, APPSolve's BeBanking and ERP support teams collaborate to identify the root cause, and the responsible team resolves their component.

**BB-SUP-004:** Standard BeBanking support hours are 08:00–17:00 SAST, Monday to Friday, excluding South African public holidays. P1 incidents (BeBanking Production environment down; no payment processing possible) receive out-of-hours response under the standard support arrangement. SLA response targets follow the APPSolve-wide framework: P1 = 1 hour; P2 = 4 hours; P3 = 1 business day; P4 = 3 business days.

**BB-SUP-005:** Routine user management — adding, modifying, and removing BeBanking user accounts — is performed by the client's BeBanking System Administrator and is not a BeBanking support ticket. Where the client's System Administrator role is vacant or the administrator is locked out of the system, APPSolve provides emergency access restoration under the support arrangement.

**BB-SUP-006:** BeBanking configuration changes post-go-live — adding new banks, modifying payment approval workflows, adding new payment types, adding new ERP integration points — are Change Requests. CR assessment, scoping, and approval follow the Commercial Framework CR process. CR work is billed at the applicable rate.

**BB-SUP-007:** Bank-initiated format changes — where a bank unilaterally updates their payment file specification — are addressed by APPSolve as a support activity where the change is a like-for-like format update (field rename, field position change, or encoding adjustment). Structural bank format changes requiring significant BeBanking reconfiguration, new payment file types, or new connectivity setup are assessed as Change Requests.

**BB-SUP-008:** BeBanking platform updates — minor releases, patches, and security fixes — are applied by APPSolve under the BeBanking subscription without additional cost. Major version upgrades or significant new feature releases may require client acceptance testing in UAT before production deployment. The update process follows BB-ENV-005.

---

## Section 152 — BB-EXC: Explicit Exclusions

**BB-EXC-001:** BeBanking does not include ERP module configuration, ERP AP module setup, ERP bank account master configuration, ERP payment format setup, or ERP GL posting rules. These are ERP implementation scope governed by the applicable ERP Pack.

**BB-EXC-002:** BeBanking does not include OIC integration design, OIC adapter configuration, or OIC process orchestration. Where OIC is used as middleware between the client's ERP and BeBanking, OIC components are governed by the OIC Assumption Pack.

**BB-EXC-003:** BeBanking does not include OCI infrastructure provisioning, OCI network configuration, OCI security zone setup, or OCI cost management. For OCI-hosted BeBanking deployments, all infrastructure assumptions are governed by the OCI Pack.

**BB-EXC-004:** BeBanking does not include payroll calculation, payroll tax processing, PAYE/UIF/SDL administration, IRP5 generation, employee payslip production, or payroll system configuration. These are payroll system functions.

**BB-EXC-005:** BeBanking does not include forex hedging, forward cover booking, treasury management, interest rate management, or exchange rate management. These are treasury or forex system functions.

**BB-EXC-006:** BeBanking does not include direct debit (debit order) processing, debit mandate management, or collections processing of any kind. BeBanking supports outgoing EFT credit payments only.

**BB-EXC-007:** BeBanking does not include integration with card payment systems, point-of-sale (POS) systems, e-commerce payment gateways, or mobile payment platforms.

**BB-EXC-008:** BeBanking does not include direct SWIFT membership connectivity. All cross-border payment instructions are routed through the client's bank as the SWIFT member institution. APPSolve does not provide or claim direct SWIFT connectivity.

**BB-EXC-009:** BeBanking does not include inward payment processing (receiving third-party payments into the client's bank account). BeBanking processes outgoing payment instructions only. Inward receipt matching and ERP posting are performed in the client's ERP using bank statement data imported via BeBanking.

**BB-EXC-010:** Custom software development beyond BeBanking's standard Low-Code/No-Code configuration capability is excluded from the standard BeBanking implementation. BeBanking is a configurable platform with defined extension points. Bespoke platform development requires a separate custom development assessment, SOW, and approval prior to commencement.

---

## Section 153 — BB-EXT: External Dependencies

**BB-EXT-001:** BeBanking implementation timelines are dependent on the client's bank completing their onboarding, certification, and connectivity approval processes. Bank delays are outside APPSolve's control and do not constitute an APPSolve delivery failure. The project plan includes explicit bank onboarding milestones with documented ownership of bank dependencies.

**BB-EXT-002:** Where the client's ERP is being implemented simultaneously with BeBanking, ERP integration readiness — including the ERP being sufficiently configured to generate and transmit payment files — must be achieved before BeBanking integration testing can begin. ERP implementation timeline delays may directly delay BeBanking go-live and are outside APPSolve's BeBanking delivery control.

**BB-EXT-003:** Account Verification Service (AVS) availability and per-transaction pricing are bank-controlled. AVS is not available from all supported banks. Where the client's bank does not offer AVS, BeBanking proceeds without this control and the fact is noted in the project risk register. Per-transaction AVS charges are the client's responsibility and are not included in the BeBanking subscription cost.

**BB-EXT-004:** Bank SFTP and API endpoints are maintained by the banks. Bank-side outages, maintenance windows, and endpoint changes are outside APPSolve's control. APPSolve monitors BeBanking's connectivity to bank endpoints and notifies the client of detected connectivity failures. Resolution of bank-side outages is between the client and their bank.

**BB-EXT-005:** Where the client uses a third-party managed service provider or outsourced IT team for network, firewall, or endpoint management, BeBanking onboarding may require coordination with that provider for IP whitelisting, firewall rule updates, and SFTP connectivity. Delays attributable to third-party IT providers are outside APPSolve's control.

**BB-EXT-006:** South African regulatory compliance requirements applicable to the client's payment activities — including SARB exchange control requirements, National Credit Act obligations, Financial Intelligence Centre Act (FICA) requirements, and SARS reporting — are the client's legal responsibility. APPSolve provides BeBanking as a payment processing platform and does not provide regulatory compliance advice.

**BB-EXT-007:** Where the client is subject to an external audit — annual financial audit, internal audit, or SARS audit — that requires access to BeBanking payment records, APPSolve provides standard data export capability and assists with reasonable auditor enquiries within normal business hours. Dedicated audit preparation, auditor interview support, or preparation of complex audit schedules is separately scoped.

**BB-EXT-008:** New bank connectivity requirements arising after go-live — whether from the client acquiring a new banking relationship, expanding to a new country, or changing their primary bank — are treated as new bank onboarding engagements. They are separately scoped, assessed, and priced. The bank onboarding process (BB-BNK-003) applies in full.

---

## BU Lead Review Items

> **WP14F (2026-06-18):** All 10 BU Lead decisions resolved. No outstanding governance items. Pack promoted to Approved v1.0.

**No outstanding decisions.**

**All resolved decisions (WP14D + WP14E/WP14F — 2026-06-18):**

| ID | Topic | Resolution |
|---|---|---|
| BU-BB-001 | Supported bank list | Confirmed: ABSA, FNB, Nedbank, Standard Bank, Investec + CMA extensions. BB-BNK-001 updated. (WP14D) |
| BU-BB-002 | New bank onboarding fee model | Confirmed: fixed-price Change Request per BeBanking Bank Addition SOW Schedule. BB-EXT-008 and BB-SUP-006 locked. (WP14E + WP14F) |
| BU-BB-003 | Forex payment inclusion | Confirmed: Citi Bank UK, ABSA, Nedbank, FNB. BB-FX-002 updated; BB-GEN-008 tag removed. (WP14D) |
| BU-BB-004 | Hypercare duration | Confirmed: first 1–3 business days. BB-CUT-002 tag removed. (WP14D) |
| BU-BB-005 | Standard reporting pack | Confirmed: 6 standard reports per updated BB-RPT-001. (WP14D) |
| BU-BB-006 | Post-go-live support model | Confirmed: support included in subscription per BB-SUP-001. Tag removed. (WP14D) |
| BU-BB-007 | Multi-country scope | Confirmed: Namibia separately scoped. BB-BNK-009 tag removed. (WP14D) |
| BU-BB-008 | Payroll source support policy | Confirmed: Oracle EBS Payroll and PaySpace. BB-PYR-002 updated. (WP14D) |
| BU-BB-009 | POPIA disclosure | Confirmed: "POPIA Data Processor" terminology. BB-DAT-006 updated. (WP14D) |
| BU-BB-010 | DR testing | Resolved by deletion: BB-ENV-006 removed from pack. DR not asserted. (WP14D) |

---

## WP11J Delivery Summary

### Assumption Count by Section

| Section | Code | Assumptions |
|---|---|---|
| 140 | BB-GEN | 8 |
| 141 | BB-BNK | 10 |
| 142 | BB-PAY | 12 |
| 143 | BB-PYR | 9 |
| 144 | BB-FX | 8 |
| 145 | BB-INT | 12 |
| 146 | BB-SEC | 8 |
| 147 | BB-DAT | 8 |
| 148 | BB-RPT | 5 |
| 149 | BB-ENV | 5 |
| 150 | BB-CUT | 6 |
| 151 | BB-SUP | 8 |
| 152 | BB-EXC | 10 |
| 153 | BB-EXT | 8 |
| **Total** | | **117** |

### BU Decision Count: 0 — All Resolved

> **WP14F (2026-06-18):** All 10 decisions resolved. BU-BB-002 confirmed via WP14E decision paper: fixed-price Change Request per BeBanking Bank Addition SOW Schedule. Pack promoted to Approved v1.0.

### Top 10 Highest-Risk Assumptions (if these are wrong in a proposal, the risk is highest)

| Rank | Assumption | Risk |
|---|---|---|
| 1 | BB-BNK-002 | SWIFT non-membership claim — if incorrectly omitted, legal and regulatory risk |
| 2 | BB-PYR-002 | Payroll source restriction (Oracle only) — if violated, Acumatica payroll rule breach |
| 3 | BB-BNK-005 | APPSolve does not hold client funds — misstatement = financial services licensing risk |
| 4 | BB-SEC-003 | Maker-checker non-negotiable — if a client believes this can be disabled, go-live conflict |
| 5 | BB-INT-005 | OIC = OIC Pack scope — if duplicated in proposals, pricing conflicts arise |
| 6 | BB-FX-003 | SARB compliance is client responsibility — misattribution creates regulatory exposure |
| 7 | BB-DAT-006 | POPIA operator vs responsible party — if wrongly framed, POPIA liability risk |
| 8 | BB-BNK-003 | Bank onboarding timeline outside APPSolve control — missing this creates delay claims |
| 9 | BB-ENV-005 | No Production update without client written sign-off — if bypassed, client disputes |
| 10 | BB-BNK-006 | Bank agreements are client's responsibility to establish — missing this blocks go-live |

### Readiness Assessment

| Dimension | Score | Notes |
|---|---|---|
| Structural completeness | 9/10 | All major functional areas covered; 14 sections; 5 deleted assumptions removed cleanly |
| Governance consistency | 9/10 | Consistent with OCI, ACU, HCM, ERP, AMS patterns; cross-pack references correct; WP14D aligned |
| Commercial protection | 9/10 | Clear client vs APPSolve responsibilities; key exclusions explicit; bank list and support model confirmed |
| Technical accuracy | 9/10 | Platform facts updated per BU Lead review; 15 assumptions modified for accuracy |
| SA-specific coverage | 9/10 | SARB, POPIA, South African banking law, SA payroll, NCA all addressed; CMA banking added |
| BU Decision Register quality | 10/10 | All 10 decisions resolved. BU-BB-002 confirmed WP14E + WP14F. |
| **Overall** | **9.5/10** | **Approved v1.0 — WP14F 2026-06-18** |

> **WP14F Approval Note (2026-06-18):** All governance blockers resolved. Pack promoted from Draft to Approved v1.0. Score raised from 9.0/10 to 9.5/10 reflecting full decision closure.

### Recommendation

**APPROVED v1.0 — No further decisions required.**

The BeBanking Base Assumption Pack is fully approved. All 10 BU Lead decisions are resolved and applied. All major payment types, banking relationships, integration patterns, security controls, data obligations, and exclusion boundaries are addressed and confirmed. The pack is structurally consistent with all approved packs (OCI, ERP, HCM Base, AMS, OIC) and applies all standing BeBanking governance rules.

**This pack may be assembled into client-facing BeBanking proposals without restriction.**

---

*BeBanking Base Assumption Pack v1.0-Approved | WP11J + WP14F | 2026-06-18*  
*Status: Approved v1.0 | 117 assumptions across Sections 140–153 | 0 BU decisions outstanding | approved_for_reuse: Yes*
