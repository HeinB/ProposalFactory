---
document_id: OCI-ASSUMPTIONS-V1
title: "APPSolve OCI Infrastructure Assumption Pack"
version: "1.0"
status: "Approved"
lifecycle_status: APPROVED
approved_for_reuse: true
approved_by: "Hein Blignaut (BU Lead)"
approved_date: "2026-06-16"
approval_ref: "WP11H-A"
created: "2026-06-16"
created_by: "WP11H — OCI Infrastructure Assumption Pack"
pack_code: OCI
section_range: "101–119"
assumption_count: 174
applies_to:
  - OCI migrations
  - OCI landing zones
  - EBS on OCI
  - Oracle Database on OCI
  - OIC on OCI
  - APEX on OCI
  - OCI Managed Services
bu_lead_decisions_applied:
  - BU-OCI-001
  - BU-OCI-002
  - BU-OCI-003
  - BU-OCI-004
  - BU-OCI-005
  - BU-OCI-006
  - BU-OCI-008
  - BU-OCI-009
  - BU-OCI-010
  - NEW-OCI-011
  - NEW-OCI-012
  - NEW-OCI-013
  - NEW-OCI-014
  - NEW-OCI-015
bu_lead_decisions_pending: []
bu_lead_decisions_withdrawn:
  - BU-OCI-007
---

# APPSolve OCI Infrastructure Assumption Pack

**Pack:** OCI | **Sections:** 101–119 | **Assumptions:** 174 | **Status:** Approved v1.0 — 2026-06-16

This pack defines the standard assumptions governing APPSolve's delivery of Oracle Cloud Infrastructure (OCI) engagements. Assumptions in this pack apply to any engagement that includes OCI as a hosting platform, migration target, or managed service environment. This pack is additive to the applicable application pack (ERP, HCM, Integration, or AMS) — it does not replace it.

**Scope:** OCI deployments for EBS on OCI, Oracle Database on OCI, OIC on OCI, APEX on OCI, and Managed OCI services. This pack does NOT apply to Oracle SaaS (Fusion HCM/ERP Cloud) — Fusion HCM and ERP Cloud are Oracle-operated and do not require customer OCI tenancy management.

**Assumption Principles:** Assume simplest reasonable implementation. These assumptions protect APPSolve from unknown scope, security ownership ambiguity, DR ambiguity, network ambiguity, third-party dependencies, cloud cost responsibility, performance guarantees, and migration surprises.

---

## Section 101 — OCI-GEN: General Engagement Scope

**OCI-GEN-001.** APPSolve's OCI engagement scope is limited to the workloads and environments explicitly named in the Statement of Work. Any workload not named in the SOW is out of scope. If the client identifies additional workloads during delivery that require OCI hosting, these will be treated as a Change Request.

**OCI-GEN-002.** APPSolve is engaged to design, configure, and deliver OCI infrastructure. APPSolve is not engaged as the client's ongoing cloud operations team unless an explicit AMS or Managed OCI Services SOW is in place. Operational responsibility for OCI tenancy post-handover transfers to the client or the client's designated cloud operations team.

**OCI-GEN-003.** The client holds the Oracle Cloud (OCI) tenancy agreement directly with Oracle. APPSolve does not enter into OCI tenancy agreements on behalf of clients. The client is responsible for all OCI subscription costs, support tiers, and contractual obligations with Oracle. Where a client requires assistance activating and configuring a new OCI tenancy before engagement work begins, this is treated as a billable pre-engagement activity and must be explicitly included in the SOW. OCI tenancy activation assistance is not assumed as a standard included service.

**OCI-GEN-004.** OCI region selection is assumed to be Oracle's South Africa (Johannesburg) region as the primary region, unless the client specifies otherwise in writing. Multi-region deployments (e.g., primary South Africa with a secondary DR region) require explicit SOW definition and are not assumed by default.

**OCI-GEN-005.** APPSolve assumes a single OCI tenancy for the engagement. If the client requires multiple tenancies (e.g., separate tenancies for subsidiaries, business units, or geographic entities), each additional tenancy is a separate scoped item and may require additional effort.

**OCI-GEN-006.** APPSolve assumes the client will provide named technical contacts with authority to approve OCI architecture decisions, network configuration changes, and security policies. Without authorised client technical contacts, APPSolve cannot progress infrastructure delivery. Delayed approval of OCI architecture decisions is treated as a client-side delay per the CR framework.

**OCI-GEN-007.** APPSolve delivers OCI engagements using Oracle's documented Well-Architected Framework principles as the baseline. Deviations from Oracle's recommended architecture require client approval and are documented as risk-accepted variances in the project record.

**OCI-GEN-008.** Oracle SaaS products (Fusion HCM Cloud, Fusion ERP Cloud, Oracle CX Cloud) are hosted by Oracle on Oracle-managed infrastructure. APPSolve does not configure, access, or manage Oracle SaaS infrastructure. Any OCI work in a SaaS engagement is limited to integration middleware (OIC), custom extensions (APEX), or connected on-premise/hybrid systems.

---

## Section 102 — OCI-LZ: Landing Zone

**OCI-LZ-001.** APPSolve deploys OCI environments using Oracle's Landing Zone framework as the baseline configuration. The standard Landing Zone includes: compartment structure, identity domains, basic IAM policies, default tagging framework, and budget alerts. Customisation beyond the standard Landing Zone baseline is scoped separately.

**OCI-LZ-002.** The standard APPSolve OCI Landing Zone delivers three compartments as a minimum: Production, Non-Production (two environments: Dev/Test combined and UAT separate), and Shared Services. The two non-production environments (Dev/Test combined and UAT separate) are the standard delivery model. Engagements requiring three separate non-production environments (Dev, Test, UAT fully independent) are treated as an expanded scope item. Additional compartments for separate business units, subsidiary entities, or regulatory isolation are out of scope unless explicitly included in the SOW.

**OCI-LZ-003.** Landing Zone deployment is assumed to be a greenfield deployment into a new OCI tenancy. If the client has an existing OCI tenancy with existing resources, a tenancy audit is required before Landing Zone deployment. The tenancy audit is a separate billable activity not included in standard Landing Zone effort.

**OCI-LZ-004.** APPSolve delivers the Landing Zone configuration as infrastructure-as-code (Terraform via OCI Resource Manager). The client receives the IaC artefacts at project close. Ongoing maintenance of the IaC repository post-handover is the client's responsibility unless covered by an AMS SOW.

**OCI-LZ-005.** The standard Landing Zone includes one set of default tagging policies covering: environment (Production/Non-Production), cost centre, project, and owner. Custom tagging taxonomies beyond this set are out of scope unless explicitly included.

**OCI-LZ-006.** Budget alerts are configured at tenancy level and compartment level as part of the standard Landing Zone. Alert thresholds are set based on client-provided budget data. APPSolve does not define the client's OCI budget — the client provides the approved budget values before Landing Zone configuration begins.

**OCI-LZ-007.** APPSolve's Landing Zone does not include multi-cloud federation (e.g., Azure Arc, AWS Control Tower integration). If the client requires OCI resources to be visible in a multi-cloud management plane, this is a separate scope item.

**OCI-LZ-008.** The Landing Zone does not include automatic resource lifecycle management (auto-shutdown of non-production environments, automated right-sizing). These capabilities are available as optional add-on services and are scoped separately if required.

**OCI-LZ-009.** APPSolve assumes OCI Resource Manager (ORM) as the Terraform execution environment. If the client requires a self-managed Terraform pipeline (e.g., GitLab CI/CD, GitHub Actions), pipeline integration is a separate scope item.

**OCI-LZ-010.** Post-Landing Zone, APPSolve hands over a Landing Zone Runbook documenting compartment structure, IAM policies, tagging taxonomy, and operational procedures. The Runbook is a standard deliverable. Bespoke operational procedure manuals beyond the standard Runbook are out of scope.

---

## Section 103 — OCI-IAM: Identity and Access Management

**OCI-IAM-001.** OCI Identity and Access Management (IAM) is configured using Oracle Identity Domains as the default. Legacy IDCS-based identity configuration is not used for new engagements. If the client has an existing IDCS configuration, migration to Identity Domains is a separate scoped item.

**OCI-IAM-002.** APPSolve configures a standard set of IAM groups and policies covering: tenancy administrators, compartment administrators, network administrators, security administrators, database administrators, and read-only auditors. Custom groups beyond this standard set require explicit scoping.

**OCI-IAM-003.** Federation with the client's corporate identity provider (e.g., Microsoft Entra ID / Azure AD, Okta, ADFS) is included in scope where explicitly stated in the SOW. Federation configuration requires the client's identity team to provide SAML metadata and federation approval. APPSolve cannot configure federation without client identity team participation.

**OCI-IAM-004.** APPSolve assumes a single Identity Domain for the engagement. Multiple Identity Domains (e.g., separate domains for employees vs. contractors, or for separate business units) are out of scope unless explicitly included. Each additional Identity Domain may require separate Oracle licensing.

**OCI-IAM-005.** Privileged Access Management (PAM) tooling integration (e.g., CyberArk, BeyondTrust, Delinea) with OCI IAM is not included in the standard engagement. PAM integration is a specialist security scope item requiring a separate SOW or sub-contract with a security specialist.

**OCI-IAM-006.** Service accounts for APPSolve automation (Terraform, ORM, monitoring agents) are created with least-privilege policies. These service accounts are handed over to the client at project close. APPSolve does not retain access to client tenancies after project close unless covered by an AMS SOW.

**OCI-IAM-007.** APPSolve assumes the client will designate at least one internal OCI tenancy administrator who holds credentials to the tenancy administrator group. This is a client responsibility. APPSolve will not be the sole administrator of a production tenancy.

**OCI-IAM-008.** Multi-Factor Authentication (MFA) policy is enabled by default for all IAM users accessing the OCI Console. APPSolve configures MFA enforcement as a standard security baseline. Disabling MFA requires explicit written client approval and is documented as a risk-accepted variance.

**OCI-IAM-009.** OCI IAM policy design uses the principle of least privilege. All policies are reviewed against Oracle's security baseline before handover. APPSolve does not configure open or wildcard policies (e.g., "Allow any-user to manage all-resources in tenancy") in production environments.

**OCI-IAM-010.** Emergency Break-Glass access procedures are documented as part of the Landing Zone Runbook. The client's tenancy administrator team is responsible for Break-Glass procedure maintenance after handover. APPSolve does not hold Break-Glass credentials to client tenancies post-project.

---

## Section 104 — OCI-NET: Networking

**OCI-NET-001.** APPSolve designs and deploys Virtual Cloud Networks (VCNs) according to Oracle's networking best practices. The standard deployment includes one VCN per major environment (Production, Non-Production). Additional VCNs for specific workload isolation (e.g., DMZ, partner networks) are out of scope unless explicitly included.

**OCI-NET-002.** VCN address space (CIDR) is assigned by the client's network team before OCI networking configuration begins. APPSolve does not allocate IP address ranges without client network team confirmation. CIDR conflicts with existing on-premise or cloud networks are a client responsibility to identify before design sign-off.

**OCI-NET-003.** On-premise to OCI connectivity is implemented via IPSec VPN as the default for most client profiles. APPSolve recommends upgrading to FastConnect (dedicated circuit) when any of the following conditions apply: sustained bandwidth requirement exceeds 100 Mbps, the engagement has more than 100 concurrent users accessing OCI-hosted applications, the OIC or integration layer requires sub-second OCI-to-on-premise latency, or the DR design specifies an RTO of less than 2 hours. FastConnect requires a separate commercial engagement with a FastConnect partner and is separately priced in all cases.

**OCI-NET-004.** IPSec VPN configuration requires the client's network team to provide VPN gateway IP addresses, pre-shared keys, and routing information. APPSolve cannot configure the OCI VPN without the corresponding on-premise VPN configuration being provided. VPN commissioning requires coordination windows that must be agreed in the project schedule.

**OCI-NET-005.** The standard network design uses a Hub-and-Spoke topology with a dedicated network VCN (hub) connected to spoke VCNs via Local Peering Gateways or OCI Network Firewall. Flat single-VCN designs are available for simple or single-workload engagements at client request.

**OCI-NET-006.** OCI Service Gateway is enabled by default to allow OCI resources to access Oracle Services (Object Storage, Autonomous Database) without traversing the public internet. Internet Gateway is enabled only where explicitly required (e.g., for public-facing application tiers). Private OCI deployments without public internet access are the default security posture.

**OCI-NET-007.** DNS resolution for OCI resources uses OCI Private DNS zones for internal resolution. External DNS (public-facing) is managed by the client's DNS provider. APPSolve configures OCI Private DNS records as part of the engagement. External DNS record management is the client's responsibility.

**OCI-NET-008.** Network Security Groups and Security Lists are configured at minimum to restrict traffic between tiers (web, application, database). Port-level firewall rules are defined in the network design document, which requires client approval before deployment. APPSolve does not open unrestricted ports in production environments.

**OCI-NET-009.** OCI Network Firewall (where required) is an additional licensed OCI service. If the client requires deep packet inspection, IDS/IPS, or URL filtering beyond NSG/Security List capabilities, OCI Network Firewall must be included in the OCI subscription and is separately scoped.

**OCI-NET-010.** Load Balancing is included where specified in the SOW (e.g., for EBS web tier HA, APEX public access). The standard configuration uses OCI's flexible load balancer. Application-specific load balancer tuning (session persistence, health check configurations) is included for the named application. Generic infrastructure load balancers not tied to a specific application are out of scope.

**OCI-NET-011.** OCI Bastion Service is configured as the standard secure access mechanism for administrative access to OCI resources. Direct public IP access to compute instances is not provisioned in production environments. Access to production compute requires Bastion Session initiation.

**OCI-NET-012.** Third-party network appliances (e.g., Palo Alto, Fortinet, Cisco ASA on OCI) are out of scope. APPSolve delivers OCI-native networking components only. If the client requires third-party network appliances on OCI, this is a specialist network scope item requiring a separate SOW.

---

## Section 105 — OCI-SEC: Security

**OCI-SEC-001.** OCI security configuration is delivered against Oracle's CIS OCI Foundations Benchmark (Level 1) as APPSolve's standard OCI security delivery baseline. Compliance with higher security standards (CIS Level 2, ISO 27001, PCI-DSS, SOC 2) requires explicit scoping and may require specialist security advisory services. Where a client operates in a regulated industry (South African financial services, government, healthcare), APPSolve will flag this at pre-sales and recommend an OCI Security Addendum discussion before proposal finalisation. Regulated-industry security requirements that exceed the CIS Level 1 baseline are out of scope for the standard OCI pack and must be separately scoped.

**OCI-SEC-002.** OCI Cloud Guard is enabled and configured in the tenancy as part of the standard security baseline. Cloud Guard detects misconfigurations and threat indicators. Remediation of Cloud Guard findings post-handover is the client's operational responsibility. APPSolve configures Cloud Guard detector rules during the engagement and provides a Cloud Guard baseline report at project close.

**OCI-SEC-003.** OCI Security Zones are applied to the Production compartment as a standard control. Security Zone policies enforce mandatory encryption, prevent public access to storage objects, and enforce other baseline controls. Any client request to disable Security Zone policies in production must be approved in writing by the client's CISO or equivalent and documented as a risk-accepted variance.

**OCI-SEC-004.** Encryption at rest is enabled for all OCI resources using Oracle-managed encryption keys as the default. Customer-managed encryption keys (CMEK) via OCI Vault are available but require additional configuration and key management operational procedures. CMEK is not assumed by default — it must be explicitly included in the SOW if required by the client's security policy.

**OCI-SEC-005.** Encryption in transit is enforced for all data moving between OCI services, between OCI and on-premise networks, and between OCI public internet endpoints and users. APPSolve configures TLS termination at load balancers and ensures all OCI service endpoints use HTTPS/TLS. Plaintext communication channels in production environments are not configured.

**OCI-SEC-006.** OCI Audit logging is enabled for all tenancy-level and compartment-level events. Audit logs are retained per Oracle's default 90-day retention window. If the client requires longer audit log retention (e.g., 1 year for regulatory compliance), logs must be exported to OCI Object Storage and the client provides the retention policy. Extended retention is not assumed by default.

**OCI-SEC-007.** Penetration testing of OCI infrastructure is not included in APPSolve's scope. If the client requires penetration testing, this is procured from a specialist security vendor and coordinated through Oracle's penetration testing notification process. APPSolve will provide architecture documentation to the pen test vendor on request.

**OCI-SEC-008.** Vulnerability scanning of OCI compute instances is the client's operational responsibility after handover. APPSolve may recommend OCI's native vulnerability scanning service (OS Management Hub) and configure it if explicitly included in the SOW. Ongoing scan management and remediation are not included in the standard engagement.

**OCI-SEC-009.** Data residency: APPSolve configures OCI workloads to reside exclusively within the contracted OCI region(s). Cross-region data replication for DR purposes (where included in scope) is explicitly defined in the DR design document. APPSolve does not configure cross-border data replication without explicit client approval.

**OCI-SEC-010.** OCI Security Advisor is run during the engagement to validate the architecture against Oracle's security recommendations. The Security Advisor report is provided to the client as a handover deliverable. Any accepted findings not fully remediated are documented with the client's written acknowledgement.

---

## Section 106 — OCI-CMP: Compute

**OCI-CMP-001.** Compute instance sizing (shape, OCPU count, memory) is based on the sizing requirements provided by the application team or derived from the client's existing on-premise workload specifications. APPSolve does not independently validate application performance requirements — sizing is based on client-provided or Oracle-recommended specifications for the specific application.

**OCI-CMP-002.** The standard compute shape uses Oracle's Flexible shapes (VM.Standard.E4.Flex or VM.Standard3.Flex) unless a specific shape is required by the application (e.g., bare metal for high-performance databases, GPU shapes for analytics workloads). Shape selection is documented in the design and approved by the client before provisioning.

**OCI-CMP-003.** APPSolve provisions compute instances with Oracle Linux as the default operating system unless the application requires a specific certified OS (e.g., RHEL for EBS, Windows Server for Windows-based applications). For EBS on OCI, the OS selection (Oracle Linux or RHEL) is confirmed at design sign-off in consultation with the client; both are valid EBS-certified platforms and the choice affects ongoing OS support costs and patching tooling. OS licensing for non-Oracle operating systems is the client's responsibility to procure.

**OCI-CMP-004.** Operating system hardening is performed to Oracle's baseline OS hardening standards. Additional hardening requirements (CIS Benchmarks, STIG, NIST) are out of scope unless explicitly included. If advanced OS hardening is required, a separate specialist engagement is needed.

**OCI-CMP-005.** APPSolve provisions compute instances using Terraform/ORM as the deployment mechanism. Manual console-based provisioning is not used for production environments. All compute configuration is codified in the IaC repository provided at project close.

**OCI-CMP-006.** Auto-scaling of compute resources (instance pools, autoscaling configurations) is configured where explicitly required by the application design (e.g., for OIC compute nodes, APEX web tier scaling). Auto-scaling is not assumed by default for all compute workloads.

**OCI-CMP-007.** Compute high availability within a single region uses Availability Domain or Fault Domain placement strategies as appropriate for the region and application. Multi-AD HA and Fault Domain placement are designed per application requirements and documented in the architecture design document.

**OCI-CMP-008.** Compute instance backup (boot volume backups) is configured as part of the standard deployment for production instances. Backup frequency and retention period are agreed with the client before configuration. Non-production instance backups are optional and not assumed by default.

---

## Section 107 — OCI-STO: Storage

**OCI-STO-001.** OCI Object Storage is used for: database backups, application file exports, OCI audit log archiving, and static content hosting where applicable. Object Storage bucket structure, lifecycle policies, and access controls are defined in the storage design document and approved before provisioning.

**OCI-STO-002.** Object Storage bucket access is private by default. Public buckets are not configured without explicit client approval. Pre-Authenticated Requests are used for controlled temporary external access. APPSolve does not configure permanent public read access to Object Storage buckets in production environments.

**OCI-STO-003.** Block Volume storage sizing for compute instances is based on client-provided storage requirements. APPSolve does not independently validate application storage growth projections. Storage capacity planning is the client's responsibility; APPSolve provisions what is specified. Block Volume expansion is a straightforward operational action and does not require a Change Request.

**OCI-STO-004.** Block Volume performance tier (Balanced, Higher Performance, Ultra High Performance) is selected based on application I/O requirements. For database workloads, Higher Performance or Ultra High Performance tiers may be required. Performance tier selection is documented and approved before provisioning.

**OCI-STO-005.** File Storage Service (NFS) is included where the application requires shared file system access across multiple compute instances (e.g., EBS shared application tier, multi-node middleware). File Storage Service is not assumed by default — it is only provisioned where explicitly required by the application design.

**OCI-STO-006.** Object Storage lifecycle policies are configured to transition objects from Standard to Infrequent Access or Archive tiers based on client-defined age thresholds. Default lifecycle policy: Standard for 30 days, Infrequent Access for 60 days, then Archive. Clients may override these thresholds in the storage design document.

**OCI-STO-007.** APPSolve does not configure cross-region Object Storage replication as part of the standard engagement. Cross-region replication for DR Object Storage is included only where the DR design explicitly requires it and is separately scoped.

**OCI-STO-008.** Storage encryption uses Oracle-managed keys by default. Customer-managed key integration with OCI Vault for Block Volumes and Object Storage is available as an optional capability and must be explicitly included in the SOW if required by the client's security policy.

---

## Section 108 — OCI-DB: Database

**OCI-DB-001.** Oracle Database on OCI is deployed as a Virtual Machine DB System for standard enterprise workloads unless a specific database service type is required (e.g., Exadata Cloud Service for high-performance EBS, Autonomous Database for analytics/reporting). The database service type is confirmed in the design and approved before provisioning.

**OCI-DB-002.** Oracle Database licensing for OCI DB Systems defaults to Bring Your Own License (BYOL). BYOL assumes the client holds current Oracle Database software licences that are eligible for use on OCI under Oracle's cloud licensing policies. The pre-sales discovery process must confirm the client's Oracle Database licence position before finalising OCI DB pricing. Where a client confirms they hold no Oracle Database licences (or licences insufficient for the required edition), License Included pricing is used. Proposing BYOL without confirming the client's licence position is not permitted.

**OCI-DB-003.** APPSolve deploys Oracle Database to the version certified for the application being deployed (e.g., EBS-certified DB version, SOA-certified DB version). Database version selection is confirmed before provisioning. Upgrading to a non-certified database version at client request is a risk-accepted variance requiring client sign-off.

**OCI-DB-004.** Database High Availability for production Oracle VM DB Systems is implemented using Oracle Data Guard (primary + standby) as the standard default. Data Guard is included in all production VM DB System deployments unless the client provides written risk acceptance for single-instance production. Single-instance production deployments require explicit client sign-off acknowledging the absence of database HA and the implications for RTO/RPO. OCI cost estimates for production VM DB Systems must reflect the dual-node (primary + standby) sizing. Active Data Guard for read-scale-out scenarios is available where licensed and must be explicitly included in scope.

**OCI-DB-005.** Database Automatic Backups are enabled for all Oracle DB Systems. Production database backup retention is set to 30 days. Non-production database backup retention is set to 7 days. Clients requiring longer production retention periods (e.g., 60 or 90 days for regulatory compliance) must specify this in the SOW; extended retention increases Object Storage costs. Database backups are stored in OCI Object Storage within the same region as the database.

**OCI-DB-006.** Database Automatic Backups do not replace application-level data exports or logical backups. For EBS on OCI, application-level database exports (Data Pump) are configured separately as part of the EBS design and are not assumed as part of the OCI database configuration.

**OCI-DB-007.** Oracle Database patching (OS patching, DB software patching) is the client's operational responsibility after handover. APPSolve configures an initial patching schedule and documents the patching runbook as a handover deliverable. Ongoing patch execution is not included in the project scope unless covered by an AMS SOW.

**OCI-DB-008.** OCI infrastructure DBA activities — Oracle Database patching, RMAN backup and restore operations, Data Guard administration, storage expansion, and OCI DB System availability management — are within the OCI AMS pack scope. Application DBA activities — AWR analysis, SQL performance tuning, schema design, index optimisation, Data Pump export/import — are within the ERP or HCM AMS pack scope as applicable to the hosted application. Application-level DBA activities are not included in the OCI infrastructure scope regardless of whether the database is hosted on OCI.

**OCI-DB-009.** Autonomous Database deployments are included where the solution specifically requires Autonomous Database services (e.g., Oracle Analytics Cloud data warehouse, APEX with ADB). The provisioning, network configuration, and access setup for Autonomous Database are included. ADB application-level schema design and query optimisation are not included.

**OCI-DB-010.** Cross-region database replication (for DR purposes) is included only where the DR design explicitly requires it. Cross-region Data Guard configurations are a significant additional effort item and are separately scoped. Single-region database HA does not include cross-region replication.

**OCI-DB-011.** Oracle GoldenGate on OCI (for real-time replication or migration) is a separate licensed service. If GoldenGate is required for migration or DR, it is explicitly scoped and licensed. GoldenGate is not assumed as part of the standard OCI database delivery.

**OCI-DB-012.** Database performance benchmarking, stress testing, or capacity planning simulations are not included in the OCI scope. Performance testing of database workloads on OCI is a separate optional activity. The database infrastructure is provisioned to the specified sizing; actual performance validation is the client's responsibility or a separately scoped activity.

---

## Section 109 — OCI-MW: Middleware

**OCI-MW-001.** Oracle Integration Cloud (OIC) on OCI is provisioned as a managed Oracle PaaS instance. APPSolve provisions and configures the OIC instance; integration flows and adapters are in scope per the Integration pack assumptions, not this OCI pack. OCI network access to OIC (private endpoints, VCN peering) is within this pack's scope.

**OCI-MW-002.** Oracle Application Express (APEX) on OCI is deployed using Oracle's managed APEX Application Development service unless the application design requires a self-managed APEX installation on a compute instance. The APEX service type (managed vs. self-managed) is confirmed in the design and approved before provisioning.

**OCI-MW-003.** Oracle WebLogic Server on OCI (for EBS web/DMZ tier or custom JEE applications) is provisioned using the Oracle WebLogic for OCI Marketplace image as the baseline. WebLogic patching post-handover is the client's operational responsibility.

**OCI-MW-004.** Oracle SOA Suite on OCI (where required for on-premise SOA lift-and-shift) is provisioned using the Oracle SOA for OCI Marketplace image. APPSolve does not re-architect SOA composites during an OCI lift-and-shift engagement. Application-level SOA changes are a separate scope item.

**OCI-MW-005.** Oracle Analytics Cloud (OAC) on OCI is a managed Oracle PaaS service. OAC provisioning, VCN private access configuration, and initial setup are within scope where explicitly included. OAC content development (dashboards, datasets, analytics flows) is in scope per a separate Analytics or BI engagement, not this OCI pack.

**OCI-MW-006.** APPSolve assumes Oracle Marketplace images as the deployment baseline for Oracle-branded middleware (WebLogic, SOA, self-managed APEX). Custom OS configuration or software installation outside Oracle Marketplace images requires additional effort and is separately scoped.

**OCI-MW-007.** Middleware HA configuration (WebLogic cluster, SOA cluster) is included where required by the application design. The HA design is documented and approved before provisioning. Single-node non-HA middleware deployment is the default for non-production environments.

**OCI-MW-008.** Third-party middleware (IBM MQ, Apache Kafka, MuleSoft, Tibco) on OCI compute is out of scope for the OCI pack. Third-party middleware installation and configuration on OCI requires a separate sub-engagement or sub-contract with the relevant technology specialist.

---

## Section 110 — OCI-INT: Integration

**OCI-INT-001.** OCI integration scope covers network connectivity between OCI-hosted applications and external systems (on-premise, SaaS, partner systems). Application-level integration logic (adapters, mappings, flows) is in scope per the Integration pack (OIC/AMS assumptions), not this OCI pack.

**OCI-INT-002.** OCI API Gateway is provisioned where the solution requires managed API exposure (e.g., APEX APIs, custom OCI Function endpoints). API content (routes, policies, authentication schemes) is configured as part of the API Gateway setup. API design and backend integration logic are not in scope for the OCI pack.

**OCI-INT-003.** OCI Functions (serverless) is included where the solution design explicitly includes serverless components (e.g., event-driven triggers, lightweight data processing). OCI Function code development is not in scope for the OCI pack — function code is provided by the application team or Integration workstream.

**OCI-INT-004.** Oracle Streaming Service (Kafka-compatible) is provisioned where the solution design requires event streaming. Topic configuration, partition sizing, and retention periods are defined in the integration design. Application-level message producers and consumers are not in scope for the OCI pack.

**OCI-INT-005.** File-based integration via OCI (SFTP, AS2, EDI) uses OCI's B2B Service within OIC where applicable. Dedicated SFTP server configuration on OCI compute is an alternative for legacy file-based integrations. The approach is defined per integration point in the integration design document.

**OCI-INT-006.** OCI Email Delivery service configuration (for application-generated emails from OCI-hosted applications) is included where required. APPSolve configures approved sender domains and suppression lists. The client is responsible for verifying email sender domain ownership via DNS records.

**OCI-INT-007.** OCI Notifications and Events service configuration (for operational alerting and event-driven automation) is included as part of the monitoring setup (see OCI-MON). Application-level event subscriptions beyond operational monitoring are a separate scope item.

**OCI-INT-008.** Third-party iPaaS tools (Boomi, Informatica, Talend) hosted on OCI compute are not configured as part of the OCI pack. Third-party iPaaS installation and configuration require a separate sub-engagement or sub-contract with the relevant tool specialist.

---

## Section 111 — OCI-BKP: Backup

**OCI-BKP-001.** OCI backup scope covers: Block Volume Backups, Boot Volume Backups, and Oracle DB System Automatic Backups. Application-level backups (EBS database exports, application tier file backups) are in scope per the respective application pack, not this OCI pack.

**OCI-BKP-002.** Block Volume and Boot Volume backups are configured using OCI's automatic backup policies. The standard APPSolve backup schedule is: daily incremental (30-day retention), weekly full (60-day retention). Clients may define alternative retention periods in the backup design document.

**OCI-BKP-003.** Database backups use Oracle's automated RMAN-based backup to OCI Object Storage. Backup windows are configured during low-activity periods agreed with the client. The backup window is confirmed before configuration and documented in the operations runbook.

**OCI-BKP-004.** Backup restore testing is performed once during the engagement (using a pre-production or staging environment) to validate backup integrity. Ongoing periodic restore testing post-handover is the client's operational responsibility. The restore procedure is documented in the operations runbook.

**OCI-BKP-005.** Cross-region backup replication is not assumed by default. If the client's DR or data protection policy requires backups to be replicated to a secondary OCI region, this is explicitly included in the DR design and separately scoped (see OCI-DR).

**OCI-BKP-006.** Third-party backup tools (Veeam, Commvault, Veritas) on OCI are out of scope. APPSolve delivers OCI-native backup services only. Integration of OCI workloads into a third-party backup environment is a separate specialist scope item.

**OCI-BKP-007.** Backup alerting (failed backup notifications, missed backup schedule alerts) is configured as part of the monitoring setup. Alert delivery uses OCI Notifications to client-designated email addresses. PagerDuty or equivalent on-call alerting tool integration is not included unless explicitly specified.

**OCI-BKP-008.** Archive-tier backup storage is used for long-term retention where backup data does not require rapid restore capability. Archive retrieval times (typically 1–4 hours for Oracle Archive tier) are documented in the backup runbook. Clients requiring sub-1-hour restore from archive must use Standard or Infrequent Access storage tiers.

---

## Section 112 — OCI-DR: Disaster Recovery

**OCI-DR-001.** Disaster Recovery (DR) design and implementation is included only where explicitly stated in the SOW. DR is not assumed by default in any OCI engagement. An engagement without an explicit DR SOW item delivers single-region, single-availability-domain infrastructure only.

**OCI-DR-002.** APPSolve's standard OCI DR approach is a Pilot Light DR configuration: critical infrastructure is provisioned in the DR region in a shut-down or minimal state and can be activated when disaster is declared. Pilot Light DR is always separately priced and is never assumed or included in the base OCI engagement. When DR is required, Pilot Light DR is presented as a named engagement option in the SOW with explicit pricing. Proposals must not include DR assumptions unless DR is explicitly included in the SOW.

**OCI-DR-003.** Full Active-Active DR (warm standby or hot standby across two regions) is a premium DR configuration and is always separately priced. Active-Active DR typically doubles the OCI infrastructure cost and requires application-level HA support. APPSolve provides Active-Active DR design and implementation as a separately scoped engagement.

**OCI-DR-004.** Recovery Time Objective (RTO) and Recovery Point Objective (RPO) targets are defined by the client and documented in the DR design before implementation. APPSolve designs the DR architecture to meet the stated RTO/RPO. APPSolve does not independently validate or guarantee RTO/RPO achievement — performance against RTO/RPO is validated in the DR test.

**OCI-DR-005.** DR testing (DR failover test, DR failback test) is performed once during the engagement as a planned DR test. The DR test is conducted in a controlled window agreed with the client. Failed DR tests require remediation and re-testing; re-test effort is included for one remediation cycle. Multiple remediation cycles are a Change Request.

**OCI-DR-006.** Database DR uses Oracle Data Guard cross-region standby as the standard database DR mechanism. Application tier DR uses OCI Full Stack DR Service or Pilot Light compute re-provisioning. The DR mechanism per tier is defined in the DR design document.

**OCI-DR-007.** APPSolve does not deliver or test DR for third-party applications hosted on OCI unless those applications are within the project scope and the DR mechanism is OCI-native. Third-party application DR is out of scope.

**OCI-DR-008.** DR runbook development is included as a standard deliverable for all DR-scoped engagements. The runbook covers: disaster declaration criteria, activation steps per tier, estimated recovery time, communication contacts, and failback procedure. Runbook maintenance after handover is the client's responsibility.

**OCI-DR-009.** Network DR (routing failover, DNS failover, load balancer DR) is included as part of the DR design for DR-scoped engagements. DNS TTL reduction before planned DR tests is the client's DNS team responsibility. APPSolve documents the DNS changes required in the DR runbook.

**OCI-DR-010.** OCI Full Stack DR Service is used where applicable to orchestrate DR failover for supported resource types. Manual DR runbooks are maintained for resource types not supported by Full Stack DR. The combination of automated and manual DR procedures is documented in the DR runbook.

---

## Section 113 — OCI-MON: Monitoring

**OCI-MON-001.** OCI Monitoring (Metrics) is enabled for all provisioned OCI resources. Standard metrics dashboards are configured for: compute CPU/memory/disk utilisation, database performance metrics, network throughput, and Object Storage usage. Custom metrics dashboards beyond the standard set are out of scope.

**OCI-MON-002.** OCI Logging (service logs, audit logs, custom application logs) is configured for all provisioned OCI services. Log ingestion into OCI Logging Analytics is included where the client has a Logging Analytics subscription. Without a Logging Analytics subscription, raw logs are available in OCI Logging only (90-day retention).

**OCI-MON-003.** Alerting is configured for the following standard conditions: CPU sustained above 90% for 15 minutes, Memory sustained above 85% for 15 minutes, Disk above 80% used, Database availability below 100%, Backup job failure, and network anomaly. Alert thresholds are adjusted based on client-provided operational baselines. Notifications are delivered to client-designated email addresses.

**OCI-MON-004.** Third-party monitoring tool integration (Splunk, Dynatrace, Datadog, New Relic) is not included in the standard OCI monitoring configuration. If the client requires OCI metrics and logs to flow to a third-party monitoring platform, this is an optional integration item that must be explicitly included in the SOW.

**OCI-MON-005.** Application Performance Monitoring (APM) using OCI APM or third-party tools is not included in the standard OCI monitoring scope. APM requires agent installation on application servers and application-level instrumentation. If APM is required, it is a separate scope item.

**OCI-MON-006.** OCI Operations Insights for database performance analysis is an optional monitoring enhancement. If included, it provides AWR data analysis, capacity planning, and SQL performance insights. Operations Insights is not assumed by default; it must be explicitly included.

**OCI-MON-007.** A Monitoring Runbook is delivered at project close documenting: dashboard locations, alert configurations, alert response procedures, and escalation contacts. Runbook maintenance after handover is the client's responsibility.

**OCI-MON-008.** Uptime monitoring and SLA reporting are not included in the standard OCI monitoring scope. If the client requires uptime SLA reports (e.g., 99.9% availability reporting), this is configured as part of an AMS Managed OCI Services SOW, not a project delivery engagement.

---

## Section 114 — OCI-OPS: Operations

**OCI-OPS-001.** APPSolve delivers OCI infrastructure in a project mode. Operations begin at project close when the client's operational team takes responsibility. Operational readiness (team training, runbook review, first-month hypercare) is a standard project close activity. Post-hypercare ongoing operations are covered by an AMS SOW if required.

**OCI-OPS-002.** OS Management Hub is enabled on Oracle Linux instances for centrally managed OS patching. APPSolve configures the initial patching groups and schedule. Patch approval and execution after project close is the client's operational responsibility unless covered by an AMS SOW. Under a Managed OCI Services AMS SOW, the standard APPSolve patching cadence is quarterly (OS patches and DB patch bundles applied in a quarterly maintenance window). Monthly patching cadence is available as a premium tier where the client's risk profile or regulatory obligations require more frequent patching cycles. Critical Security Patch Updates (CPU) issued by Oracle are applied within 30 days of Oracle release under all AMS tiers regardless of the standard cadence.

**OCI-OPS-003.** Oracle Cloud Lift (OCI's free implementation assistance program) resources are not assumed to be available for any client engagement. APPSolve scopes and prices its OCI work independently of Oracle Cloud Lift availability.

**OCI-OPS-004.** OCI Governance rules (Quotas, Budget Alerts, Compartment-level policies) are configured during delivery to prevent resource sprawl. Post-handover, quota management is the client's tenancy administrator responsibility. APPSolve documents the quota configuration in the operations runbook.

**OCI-OPS-005.** Change management for OCI infrastructure post-handover follows the client's internal IT change management process. APPSolve does not manage the client's change advisory board process. Changes to OCI infrastructure during the project delivery phase follow APPSolve's project-mode change process per COMMERCIAL_GOVERNANCE.md.

**OCI-OPS-006.** Scheduled maintenance windows for OCI patching, database patching, and planned changes are agreed with the client before the operational handover. Maintenance windows outside South Africa business hours may apply for production changes. Coordination with the client's IT operations team is required for all production maintenance activities.

**OCI-OPS-007.** APPSolve provides operational handover training to the client's designated OCI administrator team. The standard training package covers: OCI Console navigation, key monitoring dashboards, backup verification, alert acknowledgement, and escalation procedures. Advanced OCI administrator training is a separate scope item.

**OCI-OPS-008.** Incident management post-handover uses the client's incident management tooling (ServiceNow, Jira Service Desk, etc.). APPSolve does not provide an incident management platform. Under an AMS SOW, APPSolve integrates with the client's ITSM tool for AMS-managed incidents.

---

## Section 115 — OCI-CST: Cost Management

**OCI-CST-001.** OCI infrastructure costs (compute, storage, database licensing, network egress, managed services) are the client's financial responsibility. APPSolve does not absorb, share, or guarantee OCI infrastructure costs. All OCI costs are billed by Oracle directly to the client's OCI tenancy.

**OCI-CST-002.** APPSolve provides indicative OCI infrastructure cost estimates for budgeting purposes only. These estimates are based on Oracle's published price list at the time of proposal preparation and reflect the workload specifications provided. Indicative OCI cost estimates are not contractual commitments. Actual OCI infrastructure costs will vary based on: actual resource consumption, Oracle pricing changes, workload growth, additional environments, and usage outside normal business hours. OCI infrastructure costs are billed by Oracle directly to the client's OCI tenancy. APPSolve's engagement fees cover design, implementation, and professional delivery services only — they do not include OCI subscription or consumption costs.

**OCI-CST-003.** OCI cost optimisation recommendations are provided as part of the standard delivery (right-sizing, scheduling non-production environments, Reserved Instance recommendations). Implementation of cost optimisation actions post-delivery is the client's operational responsibility unless covered by a Managed OCI Services AMS SOW.

**OCI-CST-004.** Reserved Instances (Universal Credits / Annual Flex) for OCI cost reduction require client commitment for 1-year or 3-year periods. APPSolve may recommend Reserved Instance commitments but does not make these commitments on behalf of the client. Reserved Instance purchasing is the client's commercial decision with Oracle.

**OCI-CST-005.** Non-production OCI environments (Development, Test, UAT) can be scheduled to shut down outside business hours to reduce OCI costs. Auto-shutdown scheduling is configured if explicitly requested. The client defines the non-production uptime schedule. Auto-shutdown is not enabled by default.

**OCI-CST-006.** OCI network egress costs (data transfer from OCI to internet or on-premise) can be significant for high-volume data integrations. APPSolve highlights egress cost risk in the architecture design review where applicable. Actual egress costs are based on Oracle's pricing and are the client's responsibility.

**OCI-CST-007.** FinOps (cloud financial operations) maturity implementation — tagging governance, showback/chargeback models, unit cost economics — is not included in the standard OCI delivery. FinOps advisory is a separate optional engagement and is not assumed by default.

**OCI-CST-008.** OCI Cost Analysis and Budgets dashboards are configured as part of the standard Landing Zone. The client's finance team is responsible for OCI budget management and cost anomaly investigation post-handover. Cost anomaly alerts are configured in OCI Budgets to notify the client's designated contacts.

---

## Section 116 — OCI-MIG: Migration

**OCI-MIG-001.** OCI migration scope is explicitly defined in the Migration Plan document, which is a mandatory deliverable for any OCI migration engagement. The Migration Plan defines: migration approach (lift-and-shift, re-platform, re-architecture), migration sequence, rollback criteria, and acceptance criteria for each migrated workload.

**OCI-MIG-002.** APPSolve supports the following OCI migration approaches: (a) Lift-and-Shift using OCI VM migration tools or manual replication; (b) Database migration using Oracle Zero Downtime Migration (ZDM); (c) Application re-platform using Oracle Marketplace images. Migration approach per workload is confirmed in the Migration Plan.

**OCI-MIG-003.** Zero Downtime Migration (ZDM) is the preferred database migration tool for Oracle Database migrations to OCI. ZDM minimises downtime using online data transfer and redo log shipping. ZDM requires access to both source and target database environments. If ZDM is not viable (source DB version incompatibility, network restrictions), an alternative migration approach is documented and approved.

**OCI-MIG-004.** Pre-migration workload assessment is a prerequisite for all OCI migrations. APPSolve performs a pre-migration assessment covering: source environment inventory, dependency mapping, network connectivity requirements, and cutover risk assessment. Assessment results are documented before migration execution begins.

**OCI-MIG-005.** Migration cutover is a planned event with an agreed cutover window (typically a weekend). APPSolve provides APPSolve resources during the cutover window as specified in the project plan. Extended cutover windows (greater than 48 hours) require explicit resourcing agreement and may involve additional cost.

**OCI-MIG-006.** Rollback capability is maintained during the migration cutover window. The rollback plan is documented in the Migration Plan. After the client signs the migration acceptance sign-off, rollback is no longer supported. Rollback after acceptance sign-off constitutes a new project activity.

**OCI-MIG-007.** Source environment decommissioning is the client's responsibility. APPSolve does not decommission on-premise servers, SAN storage, or data centre infrastructure as part of an OCI migration engagement. APPSolve may provide a decommissioning checklist but does not execute decommissioning actions.

**OCI-MIG-008.** Data migration for large volumes (greater than 10 TB) requires a data transfer strategy review. Options include: OCI FastConnect-based bulk transfer, Oracle Data Transfer Appliance (physical media), or direct internet transfer with compression. The data transfer strategy is confirmed in the Migration Plan based on available bandwidth and timeline.

**OCI-MIG-009.** Parallel running of source and OCI target environments during migration testing is the recommended approach. Parallel run costs (double infrastructure, network, licensing) are the client's responsibility. The parallel run period is defined in the Migration Plan and ends at acceptance sign-off.

**OCI-MIG-010.** Application compatibility validation (confirming the migrated application behaves identically on OCI as on-premise) is the client's and application vendor's responsibility. APPSolve ensures the OCI infrastructure meets the application's documented system requirements. Application-level functional testing is in scope per the application pack, not the OCI pack.

**OCI-MIG-011.** Third-party application migration (non-Oracle applications co-resident with Oracle on on-premise infrastructure) is out of scope for the OCI pack. APPSolve migrates Oracle workloads defined in the SOW. Third-party applications sharing the same physical infrastructure require separate migration planning.

**OCI-MIG-012.** Post-migration performance validation is included as a standard migration deliverable. APPSolve validates that the migrated workload on OCI meets the documented performance baseline established from the pre-migration assessment. A pre-migration performance baseline must be established and agreed before migration execution begins; without a baseline, post-migration performance validation cannot be performed. OCI infrastructure performance issues identified within 30 calendar days of client acceptance sign-off are treated as migration defects and remediated within the project scope. Performance issues identified after 30 days are treated as operational matters and handled under AMS or a new engagement. Application-level performance issues (slow queries, application code inefficiencies, integration bottlenecks) are excluded from the 30-day infrastructure performance warranty.

---

## Section 117 — OCI-PER: Performance

**OCI-PER-001.** APPSolve designs OCI infrastructure to Oracle's documented sizing guidelines for the applicable application (EBS on OCI Sizing Guide, OIC performance guidelines, etc.). APPSolve does not independently develop performance models for applications not covered by Oracle's documented sizing guidelines.

**OCI-PER-002.** Performance testing (load testing, stress testing, soak testing) of OCI-hosted applications is not included in the standard OCI delivery. If performance testing is required, it is a separate scope item. Performance testing against production OCI environments requires advance coordination and a maintenance window.

**OCI-PER-003.** OCI Compute auto-scaling (instance pools) is configured where the application design requires dynamic scaling. Auto-scaling triggers are defined based on CPU/memory metrics. Application-level validation that the application handles OCI auto-scaling correctly is the application team's responsibility.

**OCI-PER-004.** Network bandwidth between OCI and on-premise environments is a significant performance variable. IPSec VPN bandwidth limitations may impact performance for high-volume OCI integrations. APPSolve documents network bandwidth requirements in the architecture design; if bandwidth is insufficient, FastConnect upgrade is recommended as a separate commercial item.

**OCI-PER-005.** OCI Storage I/O performance (Block Volume IOPS) is provisioned based on application requirements specified before implementation. APPSolve does not conduct production I/O profiling of existing on-premise workloads unless a pre-migration assessment is explicitly included in the SOW.

**OCI-PER-006.** Database performance on OCI VM DB Systems is subject to the compute shape selected and Block Volume I/O performance tier. APPSolve recommends the appropriate shape and I/O tier based on the sizing assessment. Sub-optimal performance caused by incorrect sizing information provided by the client is not a delivery defect.

**OCI-PER-007.** APPSolve does not provide performance guarantees (SLA-backed response times, guaranteed throughput) for OCI infrastructure as part of a project delivery. Performance SLAs are a feature of AMS Managed OCI Services SOWs only.

**OCI-PER-008.** Compute right-sizing recommendations are provided as part of the standard delivery and updated at the 30-day post-go-live review. Right-sizing actions post-review are the client's operational responsibility unless covered by an AMS SOW.

---

## Section 118 — OCI-SUP: Support

**OCI-SUP-001.** Oracle Cloud support for OCI is the client's direct relationship with Oracle. The client must hold an appropriate Oracle support subscription (Premier Support recommended for production workloads). APPSolve assists the client in raising Oracle support requests where required but is not a proxy for Oracle support.

**OCI-SUP-002.** APPSolve's OCI project delivery support covers: configuration defects, deployment issues, and infrastructure design queries during the project delivery period. The project delivery support period ends at acceptance sign-off. Post-acceptance support is provided under a separate AMS or Managed OCI Services SOW.

**OCI-SUP-003.** APPSolve's AMS OCI support scope covers the OCI infrastructure services explicitly named in the AMS SOW. OCI services not named in the AMS SOW are not covered by the AMS support agreement. Expansion of AMS OCI scope requires a SOW amendment.

**OCI-SUP-004.** Critical OCI infrastructure incidents under an AMS SOW are escalated to Oracle support by APPSolve on the client's behalf where the root cause is an OCI platform issue. APPSolve cannot resolve Oracle platform outages — Oracle's support SLA governs resolution. APPSolve communicates Oracle's support status to the client.

**OCI-SUP-005.** OCI tenancy administration support (user management, compartment changes, policy amendments) is included under an AMS SOW as a standard service request type. The volume of service requests covered per period is defined in the AMS SOW.

**OCI-SUP-006.** Security incident response for OCI (Cloud Guard alert response, suspected breach, anomalous activity) under an AMS SOW follows APPSolve's incident response procedures. APPSolve does not provide a dedicated 24x7 SOC for OCI security monitoring. Security incident response outside business hours requires a separately scoped on-call retainer.

**OCI-SUP-007.** OCI cost spike investigation (unexpected OCI bill increases) is included as a standard service request under a Managed OCI Services AMS SOW. APPSolve investigates root causes and recommends remediation. APPSolve cannot reverse or credit OCI charges — Oracle billing is the client's direct financial relationship.

**OCI-SUP-008.** APPSolve's OCI support team holds current Oracle OCI certifications. The minimum OCI certification requirement for APPSolve OCI support is Oracle Cloud Infrastructure Architect Associate. Senior OCI support engineers hold OCI Architect Professional certification. Certification currency is validated at AMS renewal.

---

## Section 119 — OCI-EXT: External and Third-Party Dependencies

**OCI-EXT-001.** FastConnect (OCI dedicated circuit) provisioning requires coordination with a FastConnect partner (e.g., BCX, Liquid Telecom, Vox Telecom). APPSolve designs the FastConnect architecture and provides specifications to the FastConnect partner. Procurement, commercial agreements with the FastConnect partner, and physical circuit provisioning are the client's responsibility. FastConnect lead times are typically 6–12 weeks and must be planned accordingly.

**OCI-EXT-002.** Third-party SaaS application integration with OCI-hosted Oracle applications is in scope for OCI network connectivity only (e.g., configuring outbound OCI network access to a third-party SaaS endpoint). Application-level integration logic (API calls, data mapping, authentication) is in scope per the Integration pack. APPSolve does not configure or support third-party SaaS applications directly.

**OCI-EXT-003.** Oracle Cloud Marketplace ISV solutions (third-party software from the OCI Marketplace) deployed on OCI are provisioned by APPSolve using the Marketplace image. The ISV's support relationship is directly between the client and the ISV. APPSolve does not support, patch, or maintain ISV software post-handover.

**OCI-EXT-004.** Content Delivery Network (CDN) integration (OCI's Akamai-powered CDN) for OCI-hosted applications is included where explicitly required by the application design (e.g., for APEX public applications requiring global content distribution). CDN configuration is a separate scope item and is not assumed by default.

**OCI-EXT-005.** Oracle Cloud for Government region requirements are out of scope for the standard OCI pack. South African government clients with data sovereignty requirements mandating Government regions require a separate engagement design. OCI Government regions may have limited service availability compared to commercial regions.

**OCI-EXT-006.** Third-party product-specific OCI infrastructure assumptions (for example, assumptions specific to BeBanking, Acumatica, or other products hosted on OCI) are not included in the standard OCI Infrastructure Assumption Pack. Product-specific OCI assumptions are maintained within the relevant product assumption packs where required. The OCI Infrastructure Assumption Pack governs the shared OCI infrastructure layer applicable to any supported workload.

**OCI-EXT-007.** Export control and cross-border data compliance: OCI data residency is maintained within the contracted OCI region. Cross-border data transfer requirements (e.g., POPIA Section 72, financial sector cross-border restrictions) are the client's legal responsibility to identify. APPSolve configures OCI to maintain data within the specified region but is not the client's legal compliance advisor.

**OCI-EXT-008.** Oracle Cloud Customer Connect resources are available to clients with active Oracle support subscriptions. APPSolve may reference Customer Connect knowledge base articles during engagements. Customer Connect does not replace Oracle's paid support for production issues.

**OCI-EXT-009.** Independent Software Vendor software licence compliance on OCI is the client's responsibility. APPSolve provisions OCI infrastructure to the specifications required by the ISV's licensing documentation. Over-provisioning or under-provisioning that results in ISV licence non-compliance is not APPSolve's liability.

**OCI-EXT-010.** EBS on OCI: Oracle's EBS on OCI program (EBS Cloud Manager, EBS lift-and-shift) requires an active Oracle E-Business Suite software support subscription. APPSolve assumes the client holds current EBS software support with Oracle. The ERP Assumption Pack and OCI Infrastructure Assumption Pack together provide sufficient assumption coverage for EBS on OCI engagements. A separate EBS-OCI Addendum assumption pack is not required at this time; if EBS-specific OCI assumptions beyond the current combined pack coverage are identified in a specific engagement, they will be documented as project-level assumption supplements in that engagement's SOW.

---

## BU Lead Decision Record

All BU Lead decisions for this pack were reviewed and resolved on 2026-06-16 (WP11H-A). This pack is approved for use in client-facing proposals.

| Decision ID | Item | Decision Applied | Ref |
|---|---|---|---|
| BU-OCI-001 | OCI tenancy provisioning service scope | Tenancy provisioning assistance is a billable pre-engagement activity; not included as a standard service | OCI-GEN-003 |
| BU-OCI-002 | FastConnect vs IPSec VPN threshold | FastConnect recommended when: >100 Mbps sustained, >100 concurrent users, sub-second OIC latency required, or DR RTO <2 hours | OCI-NET-003 |
| BU-OCI-003 | Oracle DB licensing default on OCI | BYOL is the default; pre-sales discovery must confirm client's licence position; LI only where no eligible licences confirmed | OCI-DB-002 |
| BU-OCI-004 | Pilot Light DR pricing status | Pilot Light DR is always separately priced; never assumed or included by default; presented as named SOW option | OCI-DR-002 |
| BU-OCI-005 | OCI DBA AMS scope boundary | OCI AMS: infrastructure DBA (patching, backup, Data Guard, storage, availability). ERP/HCM AMS: application DBA (AWR, SQL tuning, schema, Data Pump) | OCI-DB-008 |
| BU-OCI-006 | EBS on OCI addendum pack | ERP Pack + OCI Pack together are sufficient; no separate EBS-OCI Addendum pack required at this time | OCI-EXT-010 |
| **BU-OCI-007** | **BeBanking OCI hosting cost responsibility** | **WITHDRAWN — this concept does not exist in APPSolve's operating model. No BeBanking-specific OCI cost assumption is created or maintained in this pack or any pack.** | OCI-EXT-006 |
| BU-OCI-008 | OCI cost estimate disclaimer language | Approved mandatory disclaimer wording applied verbatim | OCI-CST-002 |
| BU-OCI-009 | Non-production environment count standard | 2 non-production environments: Dev/Test combined + UAT separate | OCI-LZ-002 |
| BU-OCI-010 | OCI patching cadence in AMS | Standard: quarterly; premium tier: monthly; critical patches: within 30 days of Oracle release | OCI-OPS-002 |
| NEW-OCI-011 | Data Guard default for production VM DB | Data Guard (primary + standby) included by default; single-instance requires written risk acceptance | OCI-DB-004 |
| NEW-OCI-012 | 30-day migration performance warranty | 30-day infrastructure warranty post acceptance sign-off; requires pre-migration baseline; application-level excluded | OCI-MIG-012 |
| NEW-OCI-013 | EBS OS choice at design sign-off | Oracle Linux or RHEL confirmed at design sign-off; client chooses; both are EBS-certified | OCI-CMP-003 |
| NEW-OCI-014 | Regulated-industry security escalation | Clients in regulated industries flagged for OCI Security Addendum discussion at pre-sales | OCI-SEC-001 |
| NEW-OCI-015 | Production DB backup retention | Production: 30 days; non-production: 7 days | OCI-DB-005 |

---

*OCI Infrastructure Assumption Pack v1.0 | WP11H + WP11H-A | 2026-06-16*
*Status: Approved — Hein Blignaut (BU Lead) | 14 decisions applied, 1 withdrawn (BU-OCI-007)*
*174 assumptions | Sections 101–119 | Pack Code: OCI*
