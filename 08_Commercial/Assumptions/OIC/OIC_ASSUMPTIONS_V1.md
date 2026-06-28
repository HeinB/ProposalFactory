---
document_id: OIC-ASSUMPTIONS-V1
title: "Oracle Integration Cloud (OIC) — Assumptions, Exclusions, Dependencies, Constraints and Customer Responsibilities"
version: "1.0"
status: "Approved"
created: "2026-06-15"
created_by: "WP11C — OIC Assumptions Pack"
approved_by: "BU Lead — Oracle Practice"
approved_date: "2026-06-15"
approved_for_reuse: true
lifecycle_status: APPROVED
category: "Commercial / Assumptions"
scope: "Oracle Integration Cloud Enterprise (B91110) and OIC Standard (B85207). Applies to all OIC implementation work: Oracle HCM integrations, Oracle ERP integrations, BeBanking OIC, standalone OIC engagements. This pack is standalone — not subordinate to HCM Base. Load in addition to the relevant primary module pack (HCM Base, ERP Base)."
apply_with: "TENDER_ASSUMPTION_ASSEMBLY_RULES.md"
parent_pack: "None — OIC is a standalone track; load alongside HCM Base, ERP Base, or BeBanking pack as applicable"
oracle_part_number_enterprise: "B91110"
oracle_part_number_standard: "B85207"
kb_reference: "W4-INT-001-ORA-OICAccelerators.md"
assumption_count: 104
attachment_mandate: "This pack is a mandatory attachment to all estimates, SOWs, proposals, and tender responses that include Oracle Integration Cloud (OIC) work. It must never be omitted when OIC is in scope."
bu_lead_decisions_applied:
  - "BU-OIC-001 CLOSED 2026-06-15: One integration = one directional flow. A→B and B→A are two integrations. Applied to OIC-SCP-002."
  - "BU-OIC-002 CLOSED 2026-06-15: 1 Production + 1 standard non-production OIC environment where licensed by customer. APPSolve does not provide OIC licensing. Applied to OIC-SCP-005."
  - "BU-OIC-003 CLOSED 2026-06-15: Error notifications to: (1) customer nominated support mailbox; (2) APPSolve support mailbox during hypercare only. Post-hypercare = customer responsibility unless AMS contracted. Applied to OIC-MON-002."
  - "BU-OIC-004 CLOSED 2026-06-15: OIC hypercare runs concurrently with primary project hypercare. Default 4 weeks. Applied to OIC-SUP-002."
  - "BU-OIC-005 CLOSED 2026-06-15: Simple/Standard/Complex tier model confirmed. Simple = one source/target, standard adapter, limited mapping, no orchestration. Standard = moderate mapping, standard error handling. Complex = multi-step orchestration, complex transformations, high-volume or non-standard endpoints. Applied to OIC-CON-006."
  - "BU-OIC-006 CLOSED 2026-06-15: No automatic accelerator discounts. Accelerator reuse assessed per integration during estimation. Applied to OIC-DES-007."
  - "BU-OIC-007 CLOSED 2026-06-15: SFTP is standard fallback where REST/SOAP unavailable, subject to customer security approval. Applied to OIC-DES-005."
---

# Oracle Integration Cloud (OIC) — Assumptions V1.0

**Scope:** This document governs all Oracle Integration Cloud (OIC) implementation work delivered by APPSolve. It applies to OIC Enterprise (B91110) and OIC Standard (B85207) across all contexts: Oracle Fusion HCM integrations, Oracle Fusion ERP integrations, BeBanking OIC-mediated bank connectivity, standalone OIC engagements, and multi-system integration programmes.

**Attachment mandate:** This pack must be attached to every estimate, SOW, proposal, or tender response that includes OIC work. It is the primary commercial scope-protection instrument for integration engagements and defines APPSolve's delivery boundaries, customer obligations, and what is explicitly excluded from standard OIC scope.

**Relationship to other packs:** This pack is standalone. It is loaded in addition to (not instead of) the relevant primary module pack. For Oracle HCM + OIC: load HCM Base + this pack. For Oracle ERP + OIC: load ERP Base (when available) + this pack. For BeBanking H2H: load BeBanking pack + this pack.

**Governance:** Status: Approved — 2026-06-15. Approved for use in external proposals. This pack is a mandatory attachment for all estimates, SOWs, proposals, and tender responses that include Oracle Integration Cloud work.

---

## 51. Scope Assumptions

**OIC-SCP-001**  
APPSolve's scope in Oracle Integration Cloud engagements covers: integration design (technical architecture, connection design, data flow design); integration build (OIC connection configuration, integration flow development, data transformation mapping, error handling); integration testing (SIT execution, UAT support); integration cutover (production deployment, cutover runbook); and hypercare (post-go-live stabilisation). APPSolve does not manage, configure, or support the endpoint systems on either side of the integration.

**OIC-SCP-002**  
One integration is defined as one directional data flow between one source system and one target system. An integration that sends data from System A to System B is one integration. An integration that returns data from System B to System A is a second, separate integration — two integrations must therefore be scoped, estimated, and priced where a bidirectional flow is required. This definition is the basis for APPSolve's integration count and estimate. Where the client uses the word "integration" to mean a business process spanning multiple flows, each directional flow within that process is counted and priced separately.

**OIC-SCP-003**  
The number of integrations in scope for an engagement is agreed and documented in an Integration Inventory during the Scope and Design phase. The Integration Inventory lists every integration by: integration ID, source system, target system, integration type (real-time/batch/file-based), trigger mechanism, frequency, and data payload summary. The signed Integration Inventory is the authoritative scope document for OIC work.

**OIC-SCP-004**  
The client is responsible for holding a valid Oracle Integration Cloud Enterprise (B91110) or Standard (B85207) subscription before integration development commences. APPSolve does not procure, manage, or renew Oracle OIC licences on the client's behalf. The client's Oracle OIC environment must be provisioned and accessible before the build phase commences.

**OIC-SCP-005**  
APPSolve assumes one (1) Production OIC environment and one (1) standard non-production OIC environment, where these are included in the customer's Oracle OIC licence. APPSolve does not provide, procure, or license Oracle OIC environments. The client confirms that both environments are provisioned and accessible before the build phase commences. Additional OIC environments beyond the standard customer subscription require the client to licence them separately from Oracle.

**OIC-SCP-006**  
Integrations not listed in the agreed Integration Inventory at the time of SOW execution constitute a scope addition. Each additional integration requires a formal Change Request that re-prices the additional design, build, test, and cutover effort. The Integration Inventory may be updated by mutual agreement during the Scope and Design phase; changes after Scope and Design closure are subject to the Change Request process.

**OIC-SCP-007**  
Where APPSolve has published OIC accelerators for a specific integration pattern (as documented in W4-INT-001 and OIC_IMPLEMENTATION_PATTERNS.md), the estimate for that integration reflects the accelerator's reuse benefit. The accelerator reduces but does not eliminate design, configuration, and testing effort. The specific effort reduction associated with each accelerator is confirmed in the project estimate.

**OIC-SCP-008**  
APPSolve implements Oracle-to-Oracle integrations (Oracle HCM ↔ Oracle ERP; Oracle HCM ↔ Oracle OCI; Oracle Fusion ↔ Oracle Analytics Cloud) using Oracle's native integration capabilities where available. Native Oracle-to-Oracle connectivity may use Oracle-delivered OTBI extracts, Oracle Integration Cloud, or Oracle-native REST APIs. The preferred mechanism is confirmed during the Scope and Design phase.

---

## 52. Integration Design Assumptions

**OIC-DES-001**  
The default integration architecture for APPSolve OIC implementations is point-to-point: one source system sends data directly to one target system via OIC. Point-to-point is preferred for its simplicity, maintainability, and lower design risk compared to hub-and-spoke or enterprise service bus (ESB) patterns. APPSolve does not implement ESB architectures or message broker replacements under a standard OIC engagement.

**OIC-DES-002**  
Orchestration integrations — flows where OIC coordinates data between three or more systems in a single integration transaction — are not included in the standard point-to-point scope. Where the client's business process requires multi-step orchestration, APPSolve assesses the orchestration design as a separately scoped item. Orchestration integrations typically carry higher design and testing complexity and are priced accordingly.

**OIC-DES-003**  
Standard Oracle-delivered adapters are the default mechanism for all OIC connections. APPSolve uses Oracle's published adapter catalogue (Oracle Fusion Applications adapter, REST adapter, SOAP adapter, File adapter, FTP adapter, Database adapter, and available pre-built connectors). Where no Oracle-delivered adapter exists for a target system, APPSolve uses the Oracle REST or SOAP adapter with the vendor's published API. Custom adapter development is excluded.

**OIC-DES-004**  
APPSolve produces an Integration Inventory and a Technical Design Document (TDD) for each integration in scope. The TDD covers: connection design, trigger mechanism and frequency, payload structure, data transformation logic, error handling approach, and retry strategy. The client reviews and approves the TDD before build commences. Changes to an approved TDD after build commencement constitute a Change Request.

**OIC-DES-005**  
Where a third-party system does not support a REST or SOAP API for integration, SFTP file-based integration is the standard fallback mechanism, subject to the customer's IT security approval of the SFTP connectivity approach. File-based integrations use the Oracle FTP Adapter. The client confirms the SFTP server host, port, directory path, file format, and file naming convention before file-based integration design commences. Where the client's system supports neither API nor SFTP, or where the client's security policy does not permit SFTP-based integration, the integration approach requires assessment before it can be included in scope.

**OIC-DES-006**  
REST API integration is preferred over SOAP where both protocols are available from the vendor. Where SOAP is the only available protocol, APPSolve implements the SOAP integration using Oracle's SOAP adapter. Protocol selection is documented in the Integration Inventory and TDD.

**OIC-DES-007**  
Where an applicable OIC accelerator exists in APPSolve's integration pattern library (W4-INT-001), the accelerator is used as the starting point for integration design. Accelerator applicability is assessed per integration during the estimation phase — no automatic effort discount is applied. Where an accelerator is confirmed applicable, the actual effort reduction is documented explicitly in the project estimate. Accelerator reuse does not eliminate design, testing, or cutover effort; it reduces the build component of effort for the specific integration flow covered by the accelerator.

**OIC-DES-008**  
Error handling is included in every integration's design. Standard error handling covers: field-level validation errors (payload does not match schema), connection errors (target system unavailable), transformation errors (data type mismatches), and business validation errors (business rule violation at the target system). Error handling design follows APPSolve's standard error pattern library (OIC_IMPLEMENTATION_PATTERNS.md Section 4).

**OIC-DES-009**  
Retry logic is included in every integration design where technically appropriate. Standard retry configuration: 3 retry attempts with exponential backoff. Custom retry rules (different retry counts, non-standard backoff intervals, or conditional retry based on error type) are assessed per complexity. Retry configuration is documented in the TDD.

---

## 53. Endpoint Assumptions

**OIC-END-001**  
All source and target system endpoints are technically available and accessible from Oracle OIC during SIT and UAT. If an endpoint is not available during the agreed testing window, SIT or UAT for that integration is deferred. Timeline impact arising from endpoint unavailability is the client's risk.

**OIC-END-002**  
The client provides all technical endpoint connection details — including: API base URL, authentication credentials (username/password, API key, OAuth client ID/secret), SSL certificate information, SFTP host/port/directory/credentials, and any endpoint-specific connection parameters — before the design phase commences. APPSolve cannot begin integration design without complete endpoint specifications.

**OIC-END-003**  
Where a third-party system is involved in the integration (for example, a payroll system, background check provider, banking platform, or HR portal), the third-party vendor is responsible for providing: API documentation, a sandbox environment for development and testing, technical support during integration testing, and timely response to integration queries. APPSolve facilitates the integration from the Oracle OIC side; it does not provide third-party vendor technical support.

**OIC-END-004**  
Where a third-party vendor does not provide a sandbox environment for development, APPSolve uses mock data and mocked endpoint responses during the development phase. The client acknowledges that mock-based development may not surface all integration issues until SIT against the real endpoint commences. Production credentials and the live endpoint must be available before SIT commences.

**OIC-END-005**  
If a third-party endpoint system is unavailable during agreed SIT or UAT testing windows due to vendor issues (planned maintenance, API downtime, API version changes, infrastructure problems), APPSolve cannot be held responsible for testing delays caused by vendor unavailability. The client is responsible for managing the vendor relationship and escalating endpoint availability issues to the vendor.

**OIC-END-006**  
Oracle Fusion HCM and Oracle Fusion ERP endpoints use Oracle's standard REST APIs published in Oracle's API documentation. APPSolve designs HCM/ERP integrations using Oracle-standard REST endpoints. Custom Oracle Fusion endpoints (custom-developed APEX APIs, bespoke PaaS extensions) require assessment and are not assumed to follow Oracle's standard API patterns.

---

## 54. Security Assumptions

**OIC-SEC-001**  
The client's IT team is responsible for all endpoint security configuration required to enable OIC connectivity. This includes, but is not limited to: firewall rules permitting outbound and inbound traffic on required ports; IP address whitelisting of Oracle OIC's published IP ranges at third-party endpoints; VPN configuration where required; network access control list (ACL) changes. APPSolve provides Oracle OIC's IP ranges and required port specifications; the client's IT team implements the network configuration.

**OIC-SEC-002**  
All firewall rule changes required to allow Oracle OIC traffic to reach source or target systems must be completed before SIT commences. Delays in firewall configuration directly delay SIT and extend the project timeline. Timeline impact from delayed firewall changes is the client's risk.

**OIC-SEC-003**  
Third-party endpoint IP whitelisting — where the third-party vendor must approve Oracle OIC's IP addresses before the connection is permitted — is the client's responsibility to coordinate with the vendor. APPSolve provides the Oracle OIC IP address ranges; the client manages the vendor approval process.

**OIC-SEC-004**  
APPSolve is responsible for OIC connection configuration within the Oracle OIC platform: configuring connection agents, setting authentication parameters, configuring connection properties, and testing connectivity from OIC to the endpoint. APPSolve is not responsible for network-layer security, infrastructure security, or endpoint system security configuration.

**OIC-SEC-005**  
The default authentication method for REST-based integrations is OAuth 2.0 (client credentials grant) where supported by the endpoint, or Basic Authentication where OAuth is not available. Alternative authentication methods (API key, JWT bearer token, custom token, certificate-based mutual TLS) are implemented where required by the endpoint. The authentication method is confirmed per endpoint in the Integration Inventory and TDD.

**OIC-SEC-006**  
Service accounts required for Oracle OIC to authenticate to source and target systems are provisioned by the client's IT team or system administrators. APPSolve specifies the required service account permissions for each integration. Service accounts must be created and credentials provided to APPSolve before the build phase commences. APPSolve does not create user accounts or modify access controls in the endpoint systems.

---

## 55. Certificate Assumptions

**OIC-CERT-001**  
The client is responsible for procuring all SSL/TLS certificates required to establish secure HTTPS connectivity between Oracle OIC and endpoint systems. This includes: server certificates for client-managed SFTP servers; certificates required for mutual TLS (mTLS) integrations; any custom certificates required by the third-party vendor. Certificate procurement from certificate authorities (CAs), vendors, or internal PKI systems is the client's responsibility.

**OIC-CERT-002**  
All SSL/TLS certificates required for integration connectivity must be provided to APPSolve before SIT commences. Where certificates are not available at SIT commencement, SIT for the affected integrations is deferred until certificates are available. Timeline impact from delayed certificate availability is the client's risk.

**OIC-CERT-003**  
APPSolve installs and configures all provided certificates in Oracle OIC — including importing certificates into OIC's certificate management, configuring connections to use the correct certificate, and validating that certificate-secured connections are functional. Certificate installation in endpoint systems is the client's or vendor's responsibility.

**OIC-CERT-004**  
Oracle OIC's own platform certificate (the OIC platform's public HTTPS certificate) is an Oracle-managed certificate included in the Oracle OIC subscription. APPSolve does not procure or manage Oracle OIC's platform certificate.

**OIC-CERT-005**  
Post-go-live certificate lifecycle management — including certificate expiry monitoring, certificate renewal before expiry, and updating expired certificates in Oracle OIC — is the client's IT team's responsibility. APPSolve may assist with certificate renewal updates in OIC during a managed services or AMS engagement, but not under a standard implementation project.

---

## 56. Data Mapping Assumptions

**OIC-MAP-001**  
Business data mapping decisions — which source system field maps to which target system field, and what business rule governs the mapping — are the client's responsibility. The client's functional team or business analyst is the owner of business mapping decisions. APPSolve facilitates mapping workshops, documents the outcomes, and implements the approved mappings in OIC.

**OIC-MAP-002**  
APPSolve conducts data mapping workshops with the client's functional team during the Scope and Design phase. Workshop outputs: a complete Mapping Specification document listing every source field, target field, transformation rule, and default value for each integration. APPSolve produces the Mapping Specification; the client reviews and approves it.

**OIC-MAP-003**  
A signed Mapping Specification is a mandatory prerequisite before integration build commences. APPSolve will not commence building an integration whose mapping has not been approved by the client. Where mapping workshops are delayed, the integration build is deferred and the project timeline is extended accordingly.

**OIC-MAP-004**  
Data transformation logic — including lookups (translating a source code to a target code), calculations (deriving a target value from source values), conditional logic (different mapping rules for different record types), and string manipulations — is implemented by APPSolve in OIC based on the client-approved Mapping Specification. APPSolve does not make business transformation decisions independently.

**OIC-MAP-005**  
Code-set translations — where source and target systems use different code values for the same business concept (for example, source system uses department code "10" where the target system uses "DEPT-010") — are the client's responsibility to define. The client provides complete source-to-target code mapping tables before the mapping workshop for all applicable code sets (department codes, cost centre codes, employee status codes, pay type codes, location codes, and equivalent). APPSolve implements the translation in OIC based on the client-provided lookup table.

**OIC-MAP-006**  
Changes to an approved Mapping Specification after integration build has commenced constitute a Change Request. The impact of mapping changes on build, testing, and re-testing effort is assessed and agreed before changes are implemented. Minor mapping corrections (factual errors in the approved mapping) are distinguished from mapping scope changes (new fields, new transformation rules, new code sets) in the Change Request assessment.

---

## 57. Testing Assumptions

**OIC-TST-001**  
Two testing cycles are standard for each OIC integration engagement: (1) **System Integration Testing (SIT)** — executed by APPSolve against all endpoints; validates technical connectivity, data format, transformation logic, error handling, and integration flow behaviour; (2) **User Acceptance Testing (UAT)** — executed by the client's functional team with APPSolve support; validates that the integration meets business requirements and end-to-end business processes work as expected.

**OIC-TST-002**  
The client provides all test data required for SIT and UAT before testing commences. Test data must be realistic (representative of actual production transactions) and must cover positive scenarios (successful transactions), negative scenarios (invalid data, missing mandatory fields), and edge cases (extreme values, boundary conditions) as agreed in the test plan. APPSolve does not source, create, or validate test data on the client's behalf.

**OIC-TST-003**  
APPSolve executes SIT and produces SIT test results for each integration. UAT is executed by the client's designated UAT testers. APPSolve provides UAT support: attending UAT sessions, investigating defects raised during UAT, and resolving build defects (defects caused by APPSolve's implementation). APPSolve does not execute UAT on behalf of the client.

**OIC-TST-004**  
APPSolve classifies defects raised during testing as follows: (a) **Build defects** — caused by APPSolve's implementation (incorrect transformation logic, incorrect OIC configuration, error handling failures) — resolved by APPSolve at no additional charge; (b) **Data defects** — caused by incorrect or incomplete test data provided by the client — the client's responsibility to resolve; (c) **Mapping defects** — caused by incorrect business mapping decisions (which may require a Mapping Specification amendment) — assessed as a mapping change; (d) **Vendor defects** — caused by the third-party endpoint (API errors, incorrect API documentation, unstable sandbox) — the vendor's and client's responsibility to resolve.

**OIC-TST-005**  
The client signs off SIT completion before UAT commences, and signs off UAT completion before production cutover proceeds. APPSolve does not proceed to the next test phase or to cutover without written client sign-off on the completion of the preceding phase. Sign-off may be provided by email from the client's designated project sponsor or project manager.

**OIC-TST-006**  
The client is responsible for coordinating third-party vendor participation in integration testing where the integration connects to a non-Oracle system. If a third-party vendor is not available during the agreed SIT testing window, SIT for that integration is deferred. APPSolve is not responsible for delays caused by third-party vendor unavailability during testing.

---

## 58. Performance Assumptions

**OIC-PERF-001**  
OIC integrations are designed for normal business transaction volumes as defined in the Integration Inventory. The client provides estimated transaction volumes — messages per hour (for real-time integrations), file sizes and record counts (for batch/file-based integrations), and peak volume periods — before the design phase. OIC design assumes these volumes will not be exceeded in production without prior notification and design review.

**OIC-PERF-002**  
Load testing and stress testing — including testing at projected peak volume, testing at multiples of expected volume to identify breaking points, and sustained-load testing — are excluded from standard OIC scope. Where the client requires load testing, this is assessed and priced as a scope addition.

**OIC-PERF-003**  
Performance tuning beyond standard Oracle OIC configuration is excluded from standard scope. APPSolve configures Oracle OIC using Oracle's recommended configuration practices. Bespoke performance tuning, custom Oracle OIC instance configuration, or infrastructure-level tuning of Oracle OIC resources are Oracle's responsibility for the managed OIC platform.

**OIC-PERF-004**  
Oracle OIC Enterprise (B91110) has published message volume limits and platform constraints (messages per hour, maximum payload size, maximum concurrent connections) as defined by Oracle's current product documentation. APPSolve designs integrations within these limits. The client is responsible for selecting an Oracle OIC licence tier (Standard vs Enterprise) that provides sufficient message capacity for their expected volumes. Licence tier selection is the client's commercial decision.

**OIC-PERF-005**  
Where the estimated transaction volumes provided by the client materially understate actual production volumes (for example, actual volumes exceed estimated volumes by more than 50%), the integration design may require review. APPSolve flags this risk during design if estimated volumes appear atypically low. The client is responsible for providing accurate volume estimates.

---

## 59. Cutover Assumptions

**OIC-CUT-001**  
One production cutover event is included per integration. The cutover event covers: APPSolve promoting the integration from the non-production OIC environment to the production OIC environment; executing the cutover runbook; performing initial production connectivity tests; and confirming the integration is live in production.

**OIC-CUT-002**  
APPSolve produces a cutover runbook for each integration covering: pre-cutover steps; production credential configuration; production environment promotion; initial connectivity test; go-live confirmation check; and rollback steps. The cutover runbook is reviewed and approved by the client's project manager before production cutover commences.

**OIC-CUT-003**  
Multiple production cutover rehearsals (integration dress rehearsals) are not included in standard scope. Where the client requires production rehearsal runs — deploying to a production-like environment before the actual go-live — each rehearsal is assessed as a scope addition. APPSolve recommends rehearsals where the integration is business-critical or where the go-live window is time-constrained.

**OIC-CUT-004**  
Production cutover requires the client's written go-ahead (go/no-go decision) from the designated project sponsor. APPSolve does not deploy to production without receiving the client's explicit go-live authorisation. The client's project manager or sponsor provides go-live authorisation in writing (email is acceptable) before APPSolve commences production deployment.

**OIC-CUT-005**  
End-to-end data reconciliation between source and target systems at cutover — verifying that every record processed during the initial production run was correctly received and processed by the target system — is the client's operational responsibility. APPSolve provides integration-level validation (confirming OIC processed the expected number of messages without errors). Business-level reconciliation (confirming that business records in the target system match the source) is the client's team's responsibility.

---

## 60. Monitoring Assumptions

**OIC-MON-001**  
Standard Oracle OIC monitoring capability is configured as part of every OIC implementation. This includes: Oracle OIC Activity Stream (real-time view of integration executions); Oracle OIC Error Management console (view and resubmit failed messages); Oracle OIC Dashboard (integration health summary); and Oracle OIC Alerts (notification of failed integrations). APPSolve configures these standard monitoring tools as part of the implementation.

**OIC-MON-002**  
APPSolve configures Oracle OIC error notification alerts to send email notifications when an integration fails. Error notification emails are sent to: (1) the customer's nominated integration support mailbox — configured at project outset and confirmed by the client during Scope and Design; and (2) APPSolve's integration support mailbox during the hypercare period only. After hypercare, APPSolve's mailbox is removed from the error notification configuration. Post-hypercare monitoring and error response is the customer's operational team's responsibility unless an APPSolve AMS agreement is in place.

**OIC-MON-003**  
Custom monitoring dashboards — external to the Oracle OIC native monitoring interface — are excluded from standard scope. This includes: custom BI dashboards showing integration volume or error trends; integration monitoring portals built on top of Oracle OIC data; or Grafana/Kibana-style operational monitoring dashboards. Where a client requires integration monitoring beyond OIC's native tools, this is assessed as a scope addition.

**OIC-MON-004**  
Third-party monitoring platform integration — connecting Oracle OIC monitoring data to Splunk, Dynatrace, New Relic, Datadog, IBM Instana, or any equivalent observability platform — is excluded from standard OIC scope. Where the client requires third-party observability platform integration, this is assessed as a separately scoped integration.

**OIC-MON-005**  
Post-go-live monitoring ownership is the client's IT operations team. After hypercare, the client's operations team monitors Oracle OIC error dashboards, responds to alert emails, investigates and resubmits failed messages, and escalates persistent integration failures to Oracle Support or APPSolve AMS (if under a managed services agreement). APPSolve does not actively monitor client OIC environments post-hypercare under a standard implementation contract.

---

## 61. Support Assumptions

**OIC-SUP-001**  
Hypercare for OIC integrations aligns with APPSolve's HCM Base hypercare standard (HCM-HYP-001 through HCM-HYP-003): four (4) weeks' duration; business hours (08:00–17:00 SAST, Monday to Friday); defect resolution and stabilisation only; enhancements, new integrations, and scope additions excluded.

**OIC-SUP-002**  
OIC hypercare runs concurrently with the primary project's hypercare period. Where OIC is delivered as part of the same project as Oracle HCM or Oracle ERP, the single four-week hypercare period covers both the primary modules and the OIC integrations. The hypercare period commences on the go-live date of the last module or integration to go live in the project. Where OIC is delivered as a standalone project without a primary HCM or ERP module, hypercare commences on the date of the last integration go-live. OIC hypercare does not extend beyond the four-week default unless separately contracted.

**OIC-SUP-003**  
Integration enhancements during hypercare — including adding new fields to an existing integration, adding new integrations not in the agreed Integration Inventory, changing the integration's frequency or trigger mechanism, or adding new error handling behaviour — are excluded from hypercare scope. These are assessed as Change Requests or as new project work.

**OIC-SUP-004**  
Third-party vendor API changes — including vendor-initiated API version upgrades, vendor API deprecations, vendor authentication method changes, or vendor endpoint URL changes — that occur during or after hypercare are outside APPSolve's hypercare obligation. The client is responsible for: maintaining the vendor relationship; notifying APPSolve of impending vendor API changes; and engaging APPSolve to assess and implement required integration changes. Integration updates required as a result of vendor-initiated API changes are priced as Change Requests.

---

## 62. Customer Responsibilities

**OIC-CUS-001**  
**Business Ownership:** The client appoints a designated business owner for each integration. The business owner is accountable for: defining and approving integration requirements; attending and contributing to mapping workshops; validating mapping decisions; reviewing and signing off the Mapping Specification and TDD; executing or overseeing UAT; and providing go-live sign-off. Without a designated business owner, integration requirements cannot be finalised.

**OIC-CUS-002**  
**Test Participation:** The client appoints UAT testers for each integration. UAT testers attend UAT sessions, execute test scenarios, record defect observations, and provide test sign-off. The client ensures UAT testers are available during the agreed UAT testing window. If UAT testers are unavailable during the agreed window, UAT is deferred and the timeline is extended.

**OIC-CUS-003**  
**Infrastructure Readiness:** The client ensures that all source and target systems are technically configured and accessible before SIT commences. For each integration endpoint, the client confirms: (a) the system is deployed and accessible in the relevant environment; (b) test data is available in the system; (c) technical credentials for OIC connectivity have been provisioned; (d) the system administrator is available to support connectivity testing.

**OIC-CUS-004**  
**Security Readiness:** The client's IT team completes all firewall rule changes, IP whitelisting configurations, network ACL updates, and VPN configurations required to allow Oracle OIC to reach source and target systems before SIT commences. APPSolve provides the required Oracle OIC IP ranges and port requirements. The client manages the IT change management process internally to ensure changes are implemented before the agreed SIT start date.

**OIC-CUS-005**  
**Certificates:** The client procures all SSL/TLS certificates required for integration connectivity and provides them to APPSolve before SIT commences. The client confirms that all provided certificates are valid (not expired), correctly configured (covering the correct domain names), and in the correct format for Oracle OIC import. Certificate expiry dates must extend beyond the project's planned go-live date.

**OIC-CUS-006**  
**Endpoint Availability:** The client ensures that all integration endpoints (source systems, target systems, and third-party vendor sandboxes) are available during agreed SIT and UAT testing windows. Where planned maintenance of endpoint systems is scheduled during testing windows, the client notifies APPSolve at least five (5) business days in advance. APPSolve adjusts the testing schedule where operationally feasible.

**OIC-CUS-007**  
**Vendor Coordination:** The client is responsible for the commercial and technical relationship with all third-party vendors whose systems are included in the integration scope. Client responsibilities include: obtaining API documentation from each vendor; requesting vendor sandbox access; escalating vendor responsiveness issues; managing vendor participation in SIT; and managing vendor API version change communications. APPSolve is not a party to the client–vendor commercial relationship and cannot compel vendors to provide access, documentation, or support.

**OIC-CUS-008**  
**Data Validation:** The client is responsible for validating the business accuracy of data flowing through integrations during UAT. APPSolve validates technical accuracy (data was transmitted correctly, in the correct format, to the correct endpoint). Business accuracy — confirming that the data in the target system is correctly classified, coded, and attributed according to the client's business rules — is the client's UAT team's responsibility.

**OIC-CUS-009**  
**Sign-Offs:** The client provides written sign-off at each of the following integration milestones: (a) Mapping Specification sign-off (prerequisite for build); (b) Technical Design Document sign-off (prerequisite for build); (c) SIT completion sign-off (prerequisite for UAT); (d) UAT completion sign-off (prerequisite for production cutover); (e) Go-live authorisation (prerequisite for production deployment). Sign-off by email from the client's designated project manager or sponsor is acceptable.

**OIC-CUS-010**  
**Service Accounts:** The client's IT team or system administrators provision all service accounts required for Oracle OIC to authenticate to source and target systems. APPSolve specifies the required service accounts, required permissions, and required credentials format for each integration. Service accounts must be created and credentials confirmed before the build phase commences. APPSolve does not create user accounts, modify access controls, or manage access provisioning in endpoint systems.

**OIC-CUS-011**  
**API Documentation:** The client obtains and provides complete API documentation from all third-party vendors before the integration design phase commences. API documentation must include: the vendor's API reference (endpoints, request/response schema, authentication requirements, error codes); the vendor's connectivity prerequisites; and the vendor's support contact for technical integration queries. Where a vendor requires the client to complete an onboarding or registration process before API access is granted, the client initiates and completes this process in advance.

**OIC-CUS-012**  
**OIC Licence and Environment:** The client ensures a valid Oracle OIC Enterprise or Standard subscription is active and that the OIC environment is provisioned, accessible, and at the correct release version before integration development commences. The client is responsible for Oracle licence renewal, Oracle OIC upgrade management, and Oracle OIC environment administration throughout the project and post-go-live.

---

## 63. Dependencies

**OIC-DEP-001**  
Oracle OIC Enterprise (B91110) licence must be active and the OIC environment provisioned and accessible before integration development commences. If OIC provisioning is delayed, integration development is deferred accordingly.

**OIC-DEP-002**  
All source and target system technical specifications must be available and agreed before the integration design phase is completed. Undefined or changing endpoint specifications after design sign-off delay build and constitute a mapping change.

**OIC-DEP-003**  
Where OIC integrations connect to Oracle Fusion HCM or Oracle Fusion ERP modules, those modules must be sufficiently configured in the non-production environment before SIT of dependent integrations commences. For example, an integration that sends employee data from HCM to a payroll system depends on the HCM Core module being configured and test data being available in HCM.

**OIC-DEP-004**  
Third-party vendor API availability and technical documentation are a dependency for all integrations connecting to non-Oracle systems. If a vendor does not provide API documentation or sandbox access before the design phase, the integration design cannot be completed. The client is responsible for managing this dependency.

**OIC-DEP-005**  
The Mapping Specification and Technical Design Document for each integration must be signed off before build commences. All mapping workshops, business mapping decisions, and code-set translation tables must be provided by the client before workshop outcomes can be finalised.

**OIC-DEP-006**  
Production credentials for all source and target systems must be available before production cutover. Where production credentials differ from non-production credentials (for example, different service accounts, different API endpoints, different certificates), the client provides production credentials at least five (5) business days before the scheduled cutover date.

---

## 64. Constraints

**OIC-CON-001**  
APPSolve configures Oracle OIC only. APPSolve does not configure, administer, support, or troubleshoot the source or target systems on either side of an integration. Any configuration changes, data corrections, or system administration actions required in source or target systems during the integration project are the responsibility of the respective system administrators.

**OIC-CON-002**  
Integration performance is subject to Oracle OIC's published platform constraints — including maximum message payload size, maximum messages per hour per integration, maximum concurrent integration executions, and API gateway rate limits. APPSolve designs integrations within these constraints. Performance issues caused by Oracle OIC platform limits are escalated to Oracle Support; APPSolve assists with the technical escalation but cannot override Oracle's platform constraints.

**OIC-CON-003**  
Oracle OIC integration capability depends on the existence of an Oracle-supported adapter or the availability of a standard REST/SOAP API at the endpoint. Where an endpoint system does not expose a REST or SOAP API, and where SFTP/file-based integration is not feasible, the integration cannot be implemented using Oracle OIC without custom adapter development. Custom adapter development is excluded from standard scope and requires assessment.

**OIC-CON-004**  
APPSolve cannot guarantee third-party vendor API uptime, API versioning stability, or vendor response times during the integration project. If a vendor's API is unstable, underdocumented, or subject to breaking changes during the project, APPSolve will document the impact and raise it as a project risk for the client to manage with the vendor.

**OIC-CON-005**  
OIC integration scope is bounded by the Integration Inventory agreed in the Scope and Design phase. Integrations added after the Integration Inventory is signed off require a formal Change Request that re-prices the design, build, test, and cutover effort for the new integration.

**OIC-CON-006**  
APPSolve classifies all OIC integrations using a three-tier complexity model for estimation. Every integration in the Integration Inventory is assigned a tier during Scope and Design; the tier is documented in the project estimate.

- **Simple:** One source system, one target system. Standard Oracle adapter. Limited data transformation — direct field mapping with minimal lookups. No orchestration. Standard authentication (OAuth 2.0, Basic Auth). Small to medium payload. Well-documented vendor API with sandbox available.

- **Standard:** One source system, one target system. Moderate data transformation — code-set lookups, conditional logic, data splitting or merging. Standard error handling and retry. One-to-one field mapping plus lookups. Typical payload. Reasonably documented vendor API.

- **Complex:** Multi-step orchestration involving three or more systems, or multi-step processing within a single flow. Multiple business objects in a single integration. Complex transformations — calculations, aggregations, multi-level conditional branching. High-volume or near-real-time processing. Non-standard adapter. Custom or complex authentication — mTLS, JWT, custom token. No vendor sandbox available; production credentials only for testing.

Integrations that do not clearly fit a single tier are assessed by the project lead and categorised with a documented rationale in the estimate.

---

## 65. Exclusions

**OIC-EXC-001**  
**Data Cleansing:** Cleansing, de-duplicating, reformatting, or improving the quality of source system data before it passes through an OIC integration is excluded. Where poor source data quality causes integration failures, the root cause is the data quality issue in the source system, not the integration itself. The client is responsible for source data quality.

**OIC-EXC-002**  
**Source System Remediation:** Fixing configuration defects, data integrity issues, missing master data, or API defects in source systems that prevent the integration from functioning is excluded. APPSolve identifies and documents source system issues encountered during SIT; resolution is the source system owner's responsibility.

**OIC-EXC-003**  
**Third-Party Vendor Management:** Managing the commercial relationship, SLA, or performance of third-party vendors whose systems are integration endpoints is excluded. APPSolve provides technical integration expertise; the client owns the vendor relationship.

**OIC-EXC-004**  
**Infrastructure Procurement:** Procuring, provisioning, or managing any infrastructure components required by the integration — including servers, networks, cloud infrastructure beyond Oracle OIC, SFTP servers, load balancers, or API gateways — is excluded. Oracle OIC itself is managed by Oracle; the client is responsible for all other infrastructure.

**OIC-EXC-005**  
**Network Troubleshooting:** Diagnosing or resolving network connectivity issues between the client's infrastructure and third-party endpoints — including network latency, packet loss, DNS resolution failures, and routing issues — is excluded. Oracle OIC connects via the public internet or via Oracle's private network fabric; network troubleshooting at the client or vendor network layer is the respective IT team's responsibility.

**OIC-EXC-006**  
**Business Process Redesign:** Redesigning the business process that the integration supports — including changing workflow, changing approval hierarchies, redesigning data flows for business reasons, or re-engineering systems to accommodate integration — is excluded from OIC scope.

**OIC-EXC-007**  
**Change Management and User Adoption:** Change management activities associated with the business impact of integrations — including stakeholder communication about integrated system changes, training users on new process flows enabled by the integration, or user adoption measurement — are excluded.

**OIC-EXC-008**  
**Training Beyond Agreed Super-User Scope:** Training delivery beyond the agreed super-user or administrator training scope for Oracle OIC monitoring and operations is excluded. APPSolve delivers one round of admin/operational training covering OIC monitoring, error management, and basic troubleshooting. Broad end-user training on integrated business processes is excluded.

**OIC-EXC-009**  
**Managed Services and Post-Hypercare Ongoing Support:** Ongoing management of OIC integrations after hypercare — including monitoring, incident management, error resolution, and integration maintenance — is excluded from a standard implementation contract. Post-hypercare managed services are a separate commercial engagement (AMS).

**OIC-EXC-010**  
**24x7 Support:** Round-the-clock support for OIC integrations — including evening, overnight, weekend, and public holiday support — is excluded from both the implementation scope and the standard hypercare scope. Extended support hours during hypercare are separately priced.

**OIC-EXC-011**  
**EDI and AS2 Integrations:** Electronic Data Interchange (EDI) integrations (EDIFACT, X12, or equivalent) and AS2-protocol-based integrations are excluded from standard OIC scope. EDI and AS2 require specialist integration expertise and tooling beyond standard Oracle OIC configuration. Where EDI is required, APPSolve assesses the requirement separately.

**OIC-EXC-012**  
**Custom Proprietary Protocols:** Integration with systems that communicate only via custom proprietary protocols — protocols not supported by any Oracle OIC adapter, and not exposed as REST, SOAP, SFTP, or database connections — is excluded from standard scope. Assessment is required before such integrations can be scoped.

**OIC-EXC-013**  
**Message Broker and ESB Replacement Programmes:** Replacing an existing enterprise service bus (ESB) or message broker platform (IBM MQ, MuleSoft, Tibco, WSO2, BizTalk, or equivalent) with Oracle OIC is an enterprise integration architecture programme, not a standard implementation scope item. APPSolve can deliver individual point-to-point integrations that replace specific broker-managed flows; a full ESB migration programme requires separate scoping and architecture planning.

**OIC-EXC-014**  
**Load Testing and Performance Benchmarking:** Executing structured load tests, measuring OIC throughput at projected peak volumes, or formally benchmarking Oracle OIC against performance SLAs is excluded from standard scope. Load testing is a separately scoped and priced activity.

**OIC-EXC-015**  
**Custom Monitoring Dashboards:** Building custom monitoring dashboards, integration operations portals, or observability tooling beyond Oracle OIC's native monitoring console is excluded. Third-party monitoring platform integration (Splunk, Dynatrace, Datadog, New Relic, etc.) is excluded.

---

## BU Lead Decisions Applied — All Items Closed

All seven BU Lead review items were resolved on 2026-06-15 and the document has been promoted to Approved v1.0.

| Item ID | Item | Decision Applied | Assumption Updated |
|---|---|---|---|
| BU-OIC-001 | Integration definition | One integration = one directional flow. A→B and B→A = two integrations. | OIC-SCP-002 |
| BU-OIC-002 | OIC environment | 1 Production + 1 standard non-production where licensed by customer. APPSolve does not provide OIC licensing. | OIC-SCP-005 |
| BU-OIC-003 | Error notification | Customer nominated support mailbox + APPSolve support mailbox during hypercare only. Post-hypercare = customer responsibility unless AMS. | OIC-MON-002 |
| BU-OIC-004 | Hypercare concurrency | OIC hypercare runs concurrently with primary project hypercare. Default 4 weeks. | OIC-SUP-002 |
| BU-OIC-005 | Complexity tiers | Simple / Standard / Complex confirmed with tier definitions. | OIC-CON-006 |
| BU-OIC-006 | Accelerator discounts | No automatic accelerator discounts. Assessed per integration during estimation. | OIC-DES-007 |
| BU-OIC-007 | SFTP fallback | SFTP is standard fallback where REST/SOAP unavailable, subject to customer security approval. | OIC-DES-005 |

---

*OIC_ASSUMPTIONS_V1.0 | WP11C — Oracle Integration Cloud Assumptions Pack | Approved 2026-06-15 | BU Lead — Oracle Practice*  
*104 assumptions / exclusions / dependencies / constraints / responsibilities across Sections 51–65*  
*Standalone pack — load alongside HCM Base, ERP Base, or BeBanking pack | Governed under: 08_Commercial/ASSUMPTION_GOVERNANCE.md*  
*Mandatory attachment: all estimates, SOWs, proposals, and tender responses including Oracle Integration Cloud work*
