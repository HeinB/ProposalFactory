---
file_id: W2S1-004
title: Oracle Managed Services Support Model
bu: Oracle
wave: 2
session: 1
source_status: Approved
approved_for_reuse: Yes
lifecycle_status: APPROVED
approved_by: Hein Blignaut
approval_date: 2026-06-11
extraction_date: 2026-06-11
extracted_by: "AI (Claude Sonnet 4.6) — Wave 2 Session 1"
reviewed_by: Hein Blignaut
review_date: 2026-06-11
review_notes: "Approved 2026-06-11 by Hein Blignaut. Assumptions A-W4-001 through A-W4-007 scoped and resolved. All factual risks FR-W4-001 through FR-W4-009 resolved. No prohibited wording, MTN-specific metrics, fixed SLA commitments, or commercial commitments remain. Suitable for reuse in Oracle managed services tenders."
readiness_rating: MODERNISE
kb_destination: "06_Capabilities/Oracle/DBA_Managed_Services/"
related_files:
  - 07_Approved_Content/Approved/Oracle/W2S1-003-ORA-DBAExecutiveSummary.md
  - 00_Governance/ORACLE_FACT_BASELINE.md
  - 00_Governance/CHECKPOINT_ORACLE_WAVE2_2026-06-11.md
  - 00_Governance/ORACLE_WAVE2_EXECUTION_PLAN.md
  - 07_Approved_Content/Approved/Cross_BU/W1S1-003-ORA-OraclePartnership.md
  - 07_Approved_Content/Approved/Cross_BU/W1S1-007-CORP-DeliveryModel.md
  - 07_Approved_Content/Approved/Cross_BU/W1S1-009-CORP-KeyDifferentiators.md
tags: [oracle-dba, managed-services, itil, csi, service-delivery, capacity-management, performance-management, monitoring, cmdb, deployment, segregation-of-duties, backup-recovery, migration, etl, 24x7, release-management]
---

> **APPROVED — 2026-06-11 | Approved by: Hein Blignaut | approved_for_reuse: Yes**
> Source: APPSolve MTN DBA RFP (RFX-1000004246, April 2026) — 16 pre-assigned content blocks (B-001 through B-016).
> Complements W2S1-003 Oracle DBA Executive Summary (Approved 2026-06-11). Do NOT use as a standalone document without W2S1-003.
> KB destination: `06_Capabilities/Oracle/DBA_Managed_Services/`

---

# Oracle Managed Services Support Model

## Section 1 — Executive Overview

This document provides the operational delivery framework for APPSolve's Oracle DBA Managed Services offering. It is structured as the methodology and governance depth layer that complements the Oracle DBA Executive Summary (W2S1-003). In tender use, W2S1-003 provides the capability profile and executive narrative; this document provides the proof-of-methodology content that evaluators require in scored service delivery sections of Oracle managed-services tenders.

APPSolve's managed services model is built on four operating principles:

- **Governance first** — every service activity operates within a structured, ITIL-aligned framework covering Incident, Problem, Change, and Event Management
- **Proactive over reactive** — monitoring, capacity management, and performance engineering are designed to prevent issues before they become incidents
- **Continuous improvement** — a formal CSI model with a managed register ensures service quality improves measurably over time
- **Accountability at every layer** — segregation of duties, access governance, and audit-ready documentation are embedded into the operating model, not added after the fact

APPSolve is an **Oracle Level 1 Partner** and maintains **one of the largest locally-based Oracle Applications DBA teams in South Africa**, providing depth and continuity across Oracle 12c, 19c, Fusion Cloud, and Microsoft SQL Server environments.

The managed services model is delivered through a **Hybrid Support Model** — combining on-site and remote resource allocation — a dedicated Customer Success Manager engagement, and a **Monthly Recurring Invoice Model** that provides flexible and predictable cost management for long-term engagements.

*Source: W1S1-003 (Oracle Level 1 Partner — approved 2026-06-09); W1S1-007 (DBA team claim, Hybrid Support Model, Monthly Recurring Invoice Model — approved 2026-06-09); W1S1-009 (Key Differentiators — approved 2026-06-09)*

> **Relationship to W2S1-003 (approved 2026-06-11):** This document expands the ITIL, CSI, monitoring, capacity, CMDB, deployment, and segregation of duties topics that W2S1-003 introduced at executive-summary level. When assembling a tender response, draw the executive capability overview from W2S1-003 and the operational methodology proof from this document. Do not use both documents as parallel standalone chapters — they are complementary layers. See Section 14.2 for the full overlap boundary table.

---

## Section 2 — ITIL Service Management Framework

APPSolve aligns fully with ITIL-based ITSM frameworks and embeds these disciplines into daily operations, tooling, and governance to ensure consistent, measurable, and high-quality service delivery. APPSolve integrates with the client's monitoring and service desk platforms to enable real-time alerting and automated ticket creation across all service management disciplines.

### 2.1 Incident Management

APPSolve prioritises rapid restoration of service through a structured incident lifecycle: detection, logging, categorisation, prioritisation, resolution, and closure. Predefined runbooks and escalation matrices ensure swift resolution, particularly for P1/P2 incidents, with a strong focus on minimising Mean Time to Restore (MTTR) and business impact. All incidents are managed through the client's ITSM tooling with full traceability from detection to closure.

### 2.2 Problem Management

APPSolve adopts a proactive approach to problem management by identifying recurring incidents and underlying root causes through trend analysis and incident correlation. Detailed Root Cause Analysis (RCA) is conducted for major incidents within agreed SLA timelines. The focus is on eliminating repeat failures and improving long-term platform stability — not on producing RCA documents as a compliance artefact, but on driving permanent fixes that prevent recurrence.

### 2.3 Event Management

APPSolve implements proactive event monitoring across the database landscape, covering performance, capacity, availability, and security metrics. Events are filtered, correlated, and prioritised to distinguish between informational alerts and actionable incidents. This enables pre-emptive intervention before service degradation occurs and reduces alert noise for operational teams.

### 2.4 Change Management

All changes are governed through the client's Change Management processes, ensuring full compliance with CAB approvals, risk assessments, and rollback planning. APPSolve follows structured release and deployment practices, particularly for after-hours changes such as patching, upgrades, and migrations. Each change is thoroughly tested, documented, and executed with minimal disruption to business operations.

### 2.5 ITIL Discipline Integration

The four disciplines are not operated in isolation. Incident outputs feed problem management; change management controls event-driven responses; event monitoring feeds incident detection. This integration creates a closed-loop operational model where each discipline reinforces the others, producing measurably improved service outcomes over time.

*Source: MTN-2026 lines 435–445 (Q8 ITIL framework competency) — Block B-001*

---

## Section 3 — Continuous Service Improvement Model

APPSolve embeds Continual Service Improvement (CSI) as a core pillar of the managed services delivery model, ensuring that Oracle database services are not only maintained but consistently enhanced in performance, stability, and cost efficiency.

### 3.1 CSI Framework

APPSolve's approach is built on a data-driven, ITIL-aligned CSI framework. Improvement opportunities are continuously identified, prioritised, and implemented through a formal CSI register that captures inputs from:

- Incident trend analysis
- Problem management outputs
- Performance metrics and benchmarks
- Capacity reports and growth forecasts
- Stakeholder feedback from service reviews

Each improvement initiative in the CSI register is assigned clear ownership, target timelines, and measurable outcomes. Progress is tracked and reported through structured service review forums.

### 3.2 CSI Closed-Loop Model

APPSolve operates a four-stage closed-loop CSI model:

| Stage | Activity |
|---|---|
| **Measure** | Define and track KPIs — SLA adherence, MTTR, system availability, performance benchmarks |
| **Analyse** | Trend analysis on incidents, recurring issues, capacity constraints, and performance patterns |
| **Improve** | Targeted optimisation initiatives — query tuning, index optimisation, patch alignment, automation enhancements |
| **Review** | Structured service reviews presenting outcomes; initiatives refined and tracked continuously |

### 3.3 Systematic Improvement Disciplines

APPSolve enhances service delivery through five systematic improvement disciplines:

| Initiative | Description |
|---|---|
| **Proactive Operations** | Moving from reactive support to predictive monitoring — automated alerts, threshold-based interventions, and early escalation before user impact occurs |
| **Automation at Scale** | Automating routine DBA tasks — health checks, patch tracking, backup validation, reporting — to improve consistency and reduce manual effort |
| **Performance Engineering Focus** | Dedicated optimisation cycles for high-impact systems, with prioritisation based on business criticality and incident frequency |
| **Capacity and Demand Forecasting** | Predictive modelling to prevent resource constraints before they impact services |
| **Standardised Runbooks** | Reducing resolution times and ensuring consistent handling of incidents and changes across all team members |

*Source: MTN-2026 lines 482–497 (Q12 CSI approach and service delivery improvement) — Block B-002*

---

## Section 4 — Service Delivery Management

APPSolve delivers a structured, governance-led Service Delivery Management model aligned to the client's ITIL framework, ensuring transparency, accountability, and continuous alignment with business objectives.

### 4.1 Service Delivery Structure

The model is built around three core layers:

- **Operational Control** — day-to-day service execution through SLA-driven incident, request, and change management; supported by real-time monitoring and structured escalation
- **Service Governance** — formal service cadence ensuring consistent engagement, performance oversight, and stakeholder alignment
- **Continuous Improvement** — structured CSI model (Section 3) integrated into all governance activities

### 4.2 Governance Cadence

APPSolve establishes a formal meeting cadence to ensure consistent engagement and performance oversight. Governance cadence is tailored during service initiation and agreed in the SLA or service governance plan. The structure below is **indicative** — the actual frequency, attendees, and content vary by engagement size and client operating model.

| Meeting Type | Indicative Frequency | Purpose |
|---|---|---|
| Operational Stand-up | Daily | Review incidents, priorities, risks, and actions from the previous period |
| Service Review | Weekly | Incident trends, change activity, forward planning, risks |
| SLA Performance Review | Monthly | SLA adherence, KPI tracking, service quality, CSI initiative progress |
| Executive Review | Quarterly | Strategic alignment, CSI roadmap, capacity planning, escalation governance |

### 4.3 Service Reporting Framework

APPSolve provides comprehensive SLA and operational reporting, ensuring clients have full visibility into service performance. Reporting categories are tailored to client requirements and agreed during service initiation. The categories below represent the standard reporting framework — specific content, frequency, format, and delivery channel are defined in the service agreement for each engagement.

| Report Type | Content | Indicative Frequency |
|---|---|---|
| SLA Report | SLA adherence, MTTR, system availability | Monthly |
| Incident Report | Volume, trends, root causes, recurring issues | Weekly / Monthly |
| Change Report | Change success rate, failed changes, risk summary | Monthly |
| Capacity Report | Growth trends, threshold status, forecasts | Monthly |
| CSI Register | Improvement initiatives, progress, and outcomes | Monthly |

### 4.4 Single Point of Contact and Customer Success Management

APPSolve assigns a dedicated **Service Delivery Manager (SDM)** as the single point of contact for each engagement, responsible for SLA performance, stakeholder engagement, and driving continuous improvement initiatives.

In addition, APPSolve assigns a **Customer Success Manager** (C-level) to managed service engagements, meeting regularly with client stakeholders to ensure APPSolve's strategy and delivery focus remain aligned with the client's business objectives and operational priorities.

*Source: MTN-2026 lines 499–541 (Q13 Service Delivery Management strategy, governance cadence, reporting framework) — Block B-003*
*CSM engagement model: W2S1-003 Section 9.3 and Section 11 (approved 2026-06-11) — "at no cost" wording removed per BU Lead A-007*

---

## Section 5 — Capacity and Demand Management

APPSolve approaches Capacity and Demand Management as a proactive, data-driven discipline designed to ensure Oracle database environments consistently meet performance requirements without service impact, while enabling rapid scalability for new demands.

### 5.1 Capacity Management

APPSolve implements continuous monitoring across Oracle and Microsoft SQL Server environments, focusing on CPU, memory, I/O, storage growth, and workload patterns. This is supported by trend analysis and predictive modelling, enabling capacity requirements to be forecasted well in advance of constraints materialising.

Capacity management activities include:

- **Predictive growth analysis** — forecasting storage, compute, and memory requirements based on historical trends and forward workload planning
- **Threshold-based alerting** — automated alerts trigger early intervention before constraints impact services
- **Monthly capacity reports** — growth trajectories, risk thresholds, and recommended actions enabling informed decisions before constraints affect services
- **Workload-specific tuning** — for high-volume environments, workload profiling and partitioning strategies are applied to optimise resource utilisation at scale

### 5.2 Demand Management

APPSolve aligns closely with client application teams to understand upcoming business initiatives, releases, and workload changes. Demand is managed through:

- Forward planning sessions aligned to change and release cycles
- Workload profiling to understand peak usage patterns and seasonal variations
- Prioritisation frameworks ensuring critical services are always protected against resource contention

This ensures database capacity evolves in line with business demand rather than reacting to it.

### 5.3 Rapid Environment Provisioning

APPSolve adopts a standardised build and automation model to ensure speedy, consistent delivery of new environments:

| Component | Approach |
|---|---|
| Predefined database templates | Gold images for Oracle and SQL Server environments conforming to approved security and configuration baselines |
| Automated provisioning scripts | Scripted deployment of Oracle and SQL environments reducing lead times and ensuring repeatability |
| Pre-approved configurations | Standard configurations aligned to client security and governance standards, approved in advance to remove approval bottlenecks |
| Infrastructure coordination | Integration with client infrastructure and platform teams for rapid allocation of compute and storage |

This model enables the consistent, reliable deployment of new environments — Dev, QA, UAT, and Production — with minimal lead time.

*Source: MTN-2026 lines 543–561, 566–572 (Q14 Capacity and Demand Management) — Blocks B-004 / B-011*
*Governance note: MTN-2026 lines 562–565 excluded — "1000+ databases", "reduced capacity-related incidents by over 40%", and "environment build times from days to hours" are client-specific operational metrics prohibited from use as generic APPSolve claims per ORACLE_FACT_BASELINE.md Section 13*

---

## Section 6 — Performance Management

APPSolve delivers a holistic, engineering-led Performance Management framework designed to ensure Oracle database environments operate optimally and without disruption. The approach combines continuous monitoring, automated maintenance, and ongoing optimisation across all managed Oracle and Microsoft SQL Server platforms.

### 6.1 Database Performance Optimisation

APPSolve implements continuous performance monitoring and tuning:

- Real-time tracking of CPU, memory, I/O, wait events, and query execution times
- Proactive identification of bottlenecks with targeted interventions — query optimisation, indexing strategies, and execution plan tuning
- Sustained performance management in high-throughput environments including Business Intelligence and EIS systems
- Trend-based performance forecasting to identify degradation patterns before they manifest as incidents

### 6.2 Space Management

Space management is tightly controlled through automated monitoring of data files, log files, and tablespaces:

- Threshold-based alerts and predictive growth analysis prevent capacity-driven outages
- Regular housekeeping includes log file management, archiving, purging of obsolete data, and proactive space allocation
- Automated monitoring of auto-growth events and tablespace utilisation trends
- Retention management aligned to client data governance policies

### 6.3 Database Account Management

APPSolve enforces strict governance aligned to security and audit requirements:

- Regular reviews to identify expired, inactive, or orphaned accounts
- Timely deactivation or removal of accounts no longer required
- Role-based access controls maintained and all changes tracked through the client's Change Management process
- Account lifecycle management integrated with identity governance processes where applicable

### 6.4 Daily Database Health Checks

APPSolve executes a standardised daily health-check programme across every Oracle environment under management:

| Health Check | Scope |
|---|---|
| Database availability and connectivity | Instance up/down status and connection validation |
| Backup status and success rates | RMAN backup job confirmation, failure alerting, retention verification |
| Replication health | DataGuard / AlwaysOn lag, sync status, failover readiness |
| Tablespace and disk utilisation | Growth trends, auto-growth events, threshold breach status |
| Index fragmentation and statistics status | Freshness of statistics, fragmentation levels, rebuild flags |
| Error logs and alert logs | Oracle alert log review, ORA- error identification and triage |

Findings are consolidated into daily reports with actionable insights and escalation triggers.

### 6.5 Continuous Improvement in Performance Management

Performance management includes a continuous improvement cycle:

- Trend analysis on performance metrics, RCA outputs, and capacity data
- Ongoing optimisation initiatives — index rebuilds, table defragmentation, workload balancing, and automation enhancements
- Post-incident performance review to identify and address systemic patterns
- Regular benchmarking of key performance indicators against agreed service baselines

*Source: MTN-2026 lines 579–599 (Q16 Performance Management full detail) — Block B-012*

---

## Section 7 — Monitoring Framework

APPSolve implements a comprehensive, multi-layered monitoring framework providing full visibility across Oracle database estates, enabling proactive detection of risks and maintaining optimal service performance. The framework integrates with the client's existing monitoring infrastructure while supplementing it with database-specific intelligence and automation.

### 7.1 Monitoring Architecture

APPSolve integrates directly with client monitoring tools — Oracle OEM, SQL Server DMVs, custom scripts, and ITSM platforms — while adding database-native monitoring capabilities. This creates a unified view of service health aligned to client ITSM processes.

Monitoring is structured across three layers:

| Layer | Scope |
|---|---|
| **Infrastructure Layer** | CPU, memory, disk I/O, network — platform-level health |
| **Database Layer** | Core database health, performance, replication status, capacity, security metrics |
| **Service Layer** | Application-to-database performance correlation — degradation detected before user impact |

### 7.2 Monitoring Domains

**Space and Storage Management**

| Item | Coverage |
|---|---|
| Tablespace and data file utilisation | Capacity status, growth rate, threshold breach tracking |
| Disk capacity and growth trends | Predictive growth analysis across all database volumes |
| Log file usage | Redo logs, transaction logs, archive log space |
| Auto-growth and threshold alerts | Automated alerting before space exhaustion occurs |

*Outcome: Prevents outages due to space exhaustion; enables proactive allocation*

**Logs and Error Monitoring**

| Item | Coverage |
|---|---|
| Oracle alert logs and trace files | ORA- errors, critical events, instance status |
| SQL Server error logs | SQL Agent failures, connectivity issues |
| Backup logs and job failures | RMAN and SQL backup job status, failure notification |
| Replication logs | DataGuard, GoldenGate, AlwaysOn replication status and lag |

*Outcome: Early detection of failures and anomalies before they escalate to incidents*

**Indexing, Fragmentation and Partitioning**

| Item | Coverage |
|---|---|
| Index fragmentation levels | Rebuild thresholds; automated rebuild scheduling |
| Missing or unused indexes | Identification and remediation recommendations |
| Table partition health | Partition optimisation, archiving triggers |
| Statistics freshness | Stale statistics identification; automated update scheduling |

*Outcome: Sustained query performance and reduced execution time variability*

**Performance Monitoring**

| Item | Coverage |
|---|---|
| Query performance and execution plans | Slow query identification, execution plan drift detection |
| Wait events and blocking sessions | Lock contention, blocking chain analysis |
| CPU, memory, and I/O utilisation | Resource utilisation trends and peak analysis |
| Session activity and concurrency | Active session monitoring, connection pool health |

*Outcome: Database performance directly correlated to application service performance — degradation identified and resolved before user impact*

**Availability and Replication**

| Item | Coverage |
|---|---|
| Database uptime and connectivity | Instance availability, connection validation |
| Replication lag | DataGuard lag, GoldenGate lag, AlwaysOn sync status |
| Failover readiness and DR status | DR environment health, failover readiness verification |

### 7.3 Proactive and Intelligent Monitoring

APPSolve moves beyond reactive monitoring through:

| Capability | Description |
|---|---|
| Threshold-based alerting with predictive triggers | Alerts fire before breach, not at breach — providing lead time for intervention |
| Automated health checks and daily reporting | Scheduled checks across all domains with daily consolidated reports |
| Event correlation | Reduces alert noise — correlated events surfaced as single actionable items rather than multiple individual alerts |
| Self-healing scripts | Common issues resolved automatically without manual intervention (e.g., tablespace auto-extension triggers, log archiving, stale statistics updates) |

### 7.4 Monitoring Outputs

Monitoring outputs feed directly into the service delivery model:

- Real-time dashboards for operational visibility
- Weekly and monthly trend reports
- Incident and Problem Management inputs
- CSI register improvement initiatives

*Source: MTN-2026 lines 670–722 (Q20 Monitoring framework full detail) — Block B-014*

---

## Section 8 — Configuration Management and CMDB Governance

APPSolve recognises that accurate and up-to-date Configuration Management Database (CMDB) information is critical to operational stability, governance, and service management effectiveness. The approach is built on a controlled, automated, and continuously validated Configuration Management framework, fully aligned to the client's ITIL processes.

### 8.1 Structured CMDB Governance Model

APPSolve establishes a single source of truth for all database-related Configuration Items (CIs), ensuring the following attributes are always current and accurate:

| CI Attribute | Description |
|---|---|
| Database instance and name | Unique identifier for each managed database instance |
| Hostname and environment tier | Mapped to Dev / QA / UAT / Pre-Prod / Prod / DR |
| Data centre location | DC alignment including geographic and physical location |
| Port numbers and connectivity details | Service port, listener configuration, connection details |
| Database versions and patch levels | Current version, last patch applied, next scheduled patch |
| Application-to-database relationships | Full traceability — application component to database instance |

Each CI is uniquely identified and linked to its corresponding application services, ensuring full traceability across the client's technology ecosystem.

### 8.2 Automated Discovery and Reconciliation

To manage large-scale database estates efficiently, APPSolve leverages automated discovery and reconciliation:

- Scheduled scripts and tools to extract database configuration details (Oracle and SQL Server)
- Integration with monitoring tools to validate real-time configuration states
- Automated comparison against CMDB records to detect discrepancies
- Any variance triggers controlled update and validation workflows, ensuring CMDB accuracy is maintained continuously

### 8.3 Change-Driven CMDB Updates

All CMDB updates are tightly integrated with the client's Change Management process:

- Every deployment, upgrade, migration, or decommissioning includes a mandatory CMDB update step
- Changes are only closed in the ITSM tool once CMDB updates are verified and approved
- CAB governance ensures full visibility and compliance
- CMDB accuracy is embedded into operational process — not treated as a separate administrative activity

### 8.4 Continuous Validation and Audit Readiness

APPSolve performs regular CMDB audits and reconciliations:

- Monthly validation against live environments
- Cross-checking of database inventories against configuration baseline records
- Verification of relationships between databases, applications, and infrastructure components
- Alignment with client audit requirements, preventing configuration drift

### 8.5 Data Quality and Ownership

| Element | Approach |
|---|---|
| Defined ownership per CI category | Named ownership for Oracle, SQL Server, and other database environment types |
| Standardised data capture templates | Consistent attributes captured across all CI types; no partial or ad-hoc records |
| SLA-driven update timelines | CMDB updates completed within agreed SLA windows for each change type |

*Source: MTN-2026 lines 629–668 (Q19 CMDB governance full model) — Blocks B-005 / B-013*
*Governance note: MTN-2026 line 631 ("300+ Oracle and 2000+ MS SQL databases") excluded — MTN-specific scale descriptor excluded per FR-G treatment in W2S1-003; replaced with "large-scale database estate" framing throughout*

---

## Section 9 — Release and Deployment Management

APPSolve delivers a controlled, auditable, and low-risk deployment approach ensuring database and ETL changes are implemented with minimal to zero business disruption. All deployments — whether database patches, ETL code, or configuration changes — operate within a single, integrated release management framework governed by ITIL Change Management and DevOps principles.

### 9.1 Pre-Deployment Planning and Governance

All changes are logged and approved through the client's Change Management process before execution:

- Classification into Standard / Normal / Emergency change categories
- Defined maintenance windows (typically after-hours) to minimise business impact
- Full impact assessment and dependency mapping
- Risk assessment documented and reviewed by CAB before approval

### 9.2 Database Patch Management

| Stage | Activity |
|---|---|
| OEM Monitoring | Continuous review of Oracle and Microsoft patch advisories for relevance, risk, and impact |
| N-1 Strategy | Adoption of N-1 patching compliance — most recent minor release minus one — balancing stability with security |
| Non-Production Validation | Patch deployed into Dev → QA → UAT with regression testing, workload simulation, and compatibility validation |
| Automated Deployment | Scripted patch deployments ensuring consistency, repeatability, and full audit trail |
| Rollback Procedures | Pre-defined rollback plans and backup validation points for every patch deployment |
| Tooling | Oracle OPatch / Oracle Fleet Maintenance; SQL Server patch management frameworks |

### 9.3 ETL Code Deployment

APPSolve follows a structured promotion pipeline for all ETL code changes:

**Promotion pathway:** Development → Integration → UAT → Production

| Activity | Description |
|---|---|
| Scheduling | Deployments aligned to business cycles, batch windows, and agreed maintenance windows |
| Orchestration | Use of scheduling tools (e.g., Control-M, native Oracle DBMS_SCHEDULER) |
| Data validation | Pre- and post-deployment data validation — row counts, checksums, business rule verification |
| Backout strategy | Defined rollback procedures for failed transformations; source data preserved until successful validation confirmed |

### 9.4 Version Control and Release Management

All database and ETL code changes are managed through:

| Practice | Description |
|---|---|
| Centralised version control | Enterprise tools (Git-based repositories, Azure DevOps) |
| Branching strategy | Structured feature, release, and hotfix branching — controlled merging with review gates |
| Full audit trail | Complete history of who changed what, when, and why — traceable from change request to production |
| Release packaging and tagging | Every release tagged for reproducibility — supports rollback and future reference |

*Source: MTN-2026 lines 993–1037 (Q27 Deployment framework — patches, ETL, version control) — Block B-008*

---

## Section 10 — Security, Access Governance and Segregation of Duties

APPSolve complies with segregation of duties requirements by structuring the managed DBA service so that access, change execution, review, and approval are separated across roles, systems, and processes. The objective is to prevent unauthorised change, error, or concealment of activity by ensuring that critical activities are never performed without independent oversight.

### 10.1 Role-Based Separation of Responsibilities

| Role | Responsibilities |
|---|---|
| DBA Support Staff | Operational database administration — monitoring, backup validation, performance tuning, patch implementation, incident response |
| Client System / Application Owners | Approve business-impacting changes, privileged access requests, and production releases |
| Infrastructure / OS Administrators | Manage server-level access separately from database administration |
| Security / Audit / Governance Stakeholders | Review privileged access, audit logs, exceptions, and compliance reports |
| Service Delivery Management | Oversees process compliance, escalation, and reporting — does not independently execute unauthorised technical changes |

### 10.2 Privileged Access Controls

APPSolve applies least-privilege access principles across all managed service operations:

| Control | Description |
|---|---|
| Named individual accounts | No shared generic privileged logins unless technically unavoidable |
| Separate accounts for privileged operations | Normal access account and privileged administration account are distinct |
| Production access governance | Production access granted only to approved personnel |
| Elevated access time-bounding | Elevated access restricted to specific tasks, systems, and time periods |
| Periodic access reviews | Regular removal of unnecessary privileges; deactivation of inactive or orphaned accounts |
| Emergency access (Break-Glass) | Formal break-glass procedure — time-bound; full activity logging; incident reference and business justification required before access granted; retrospective approval mandatory; elevated access removed immediately after resolution |
| PAM / MFA controls | Where applicable, privileged access brokered through PAM tools, bastion hosts, jump servers, and multi-factor authentication with full session logging |

### 10.3 Change Management as a Segregation Control

All non-emergency production changes are executed through a formal change process:

1. Documented change request with business justification
2. Risk and impact assessment
3. Client or authorised stakeholder approval before implementation
4. Scheduling within approved maintenance windows
5. Execution by authorised DBA personnel only
6. Post-change validation by the requester, system owner, or an independent party
7. Rollback plan and evidence retained

### 10.4 Environment Separation and Controlled Promotion Paths

| Practice | Description |
|---|---|
| Strict environment separation | Development, Test, UAT, and Production are maintained as separate, governed environments |
| No uncontrolled production changes | No direct development or ad-hoc changes in production |
| Controlled promotion paths | Code, scripts, and schema changes promoted through approved release paths only |
| Production data protection | Production data access controlled more tightly than non-production; masked or sanitised data used in lower environments |

### 10.5 Independent Logging, Monitoring and Audit

All privileged administrative activity is fully auditable:

- Logging of logins, privileged commands, schema changes, and critical database actions
- Retention of audit trails for governance and compliance review
- Monitoring of failed logins, unusual privilege usage, and sensitive operations
- Regular review of DBA activities by client management, security teams, or service governance leads
- Full traceability from service request → access grant → implementation → closure

### 10.6 Emergency and Incident Access Controls

Emergency access is managed without breaking segregation of duties:

- Emergency access granted only for defined, logged incidents
- Access is time-bound to the incident window
- All activity logged in full during the emergency window
- Incident reference and business justification recorded before access is granted
- Retrospective approval and review are mandatory after resolution
- Elevated access removed immediately after the incident is resolved

### 10.7 Dual Control for Sensitive Activities

For particularly sensitive operations, APPSolve implements two-person control or additional approval layers:

| Sensitive Activity | Control Applied |
|---|---|
| Creation of new privileged accounts | Two-person approval required |
| Changes to audit or logging settings | Two-person approval required |
| Security policy changes | Two-person approval required |
| Data correction scripts on business-critical tables | Client-approved written instruction required before execution |
| Direct updates to production data | Client-approved written instruction required; activity logged in full |
| Backup restore of sensitive data sets | Client-approved written instruction required |

### 10.8 Governance and Compliance Reporting

Compliance is sustained through recurring governance activities:

- User and privileged access recertification (quarterly or as defined by client)
- Review of dormant and excessive privileges
- Exception reporting
- Audit log review
- Monthly service reports covering access, incidents, changes, and policy deviations
- Internal and external audit support

### 10.9 SoD Documentation Framework

APPSolve's SoD approach is formally embedded in the service through:

- Access control policies
- RACI matrices — approved authorities defined per role
- Onboarding and offboarding procedures for DBA personnel
- Change management procedures referencing SoD controls
- Incident and escalation procedures
- Audit and compliance reporting
- Contractual definitions of approval authority and support boundaries

### 10.10 Access Management SOP Structure

APPSolve maintains formal Standard Operating Procedures for access governance across all managed service engagements. Access governance documentation is adapted to each client's IAM model, audit requirements, and operational controls. The structure below is drawn from an active access management SOP deployed at an existing managed services engagement (client name redacted) and represents the depth and coverage of APPSolve's access governance documentation standard:

| Section | Content |
|---|---|
| 1 | Purpose |
| 2 | Scope |
| 3 | Roles and Responsibilities |
| 4 | Prerequisites |
| 5 | Quarterly Access Review Process — Preparation → Validation and Verification → Remediation → Documentation and Evidence → Communication and Change Management → Post-Review Activities |
| 6 | Access Control and Security Controls — IAM, RBAC and Least Privilege, Logging and Monitoring, Data Handling, Termination and Deprovisioning, Access Requests |
| 7 | Testing and Validation |
| 8 | Compliance and Audit |
| 9 | KPIs — performance indicators, exceptions and escalations, training and awareness |
| 10 | Change History and SOP Versioning |

*Source: MTN-2026 lines 1053–1167 (Q28 Segregation of Duties full framework) — Block B-009*
*Access Management SOP TOC: MTN-2026 lines 751–780 (Q21 documentation evidence)*

---

## Section 11 — Documentation Standards

APPSolve maintains a structured library of Standard Operating Procedures, reporting templates, and governance documents across all managed service engagements. The documentation standards below are drawn from active production SOPs in use at existing managed services clients.

### 11.1 Backup and Recovery SOP Structure

Backup and recovery SOPs are maintained per client environment, aligned to agreed backup policies, retention requirements, and recovery objectives. APPSolve's Backup and Recovery SOP provides the governance framework for all backup operations, scheduling, and recovery activities. The structure below represents the standard SOP framework — sections are adapted to each client's technology environment and contractual recovery requirements:

| Section | Content |
|---|---|
| 1 | Purpose |
| 2 | Scope |
| 3 | Responsibility |
| 4 | Definitions |
| 5 | References |
| 6 | Appendices |
| 7 | Configurations — 7.1 Considerations; 7.2 Media Sets and Retention Periods; 7.3 RMAN Backups |
| 8 | Scheduling Jobs — 8.1 Schedule Jobs; 8.2 Test Backup; 8.3 Partial Restore |
| 9 | Media Management |
| 10 | Reports — 10.1 Scheduling Reports |
| 11 | Handling Failed Backups |
| 12 | Handling Restore Requests |
| 13 | Current Backup Software |
| 14 | Contact Persons and Responsible Parties |
| 15 | Revision Record |

This SOP governs Oracle RMAN backups, incremental and full backup scheduling, media set and retention period configuration, restore testing procedures, and escalation on backup failures.

### 11.2 Monthly Service Report Structure

APPSolve provides monthly service reports tailored to each client's requirements. The following comprehensive structure was developed for a large-scale Oracle DBA managed services engagement and represents the depth of reporting APPSolve maintains. Content, structure, and subsection detail are adapted per client during service initiation.

| Section | Content |
|---|---|
| 1 | Foreword |
| 2 | Service Management and Management Roles — 2.1 Management Reports; 2.2 Responsibilities |
| 3 | Incident / Call Management — 3.1 Call Management Statistics; 3.2 Open Service Requests with Oracle |
| 4 | DBA Activity Log — 4.1 DBA Activities; 4.2 ERP System Availability; 4.3 System Maintenance; 4.4 Patch Monitoring; 4.5 Password Control (System); 4.6 DR Site Status |
| 5 | Risk and Issue Logs — 5.1 Risk and Issue Log |
| 6 | Major Achievements During the Month — 6.1 Oracle Database Activities |
| 7 | Appendices — 7.1 Activity Extract; 7.2 Risk and Issue Log |

> **Note:** This report structure reflects APPSolve's reporting maturity across long-running Oracle DBA managed services engagements. The section headings and subsection labels shown above are current — technology-specific subsection labels from historical engagements (such as references to legacy platforms, superseded Oracle versions, or decommissioned infrastructure) have been removed and replaced with current equivalents. The seven-section structure and DBA Activity Log framework demonstrate reporting depth and governance discipline; the exact subsections are tailored to each client's active technology environment during service initiation.

### 11.3 Standard Report Components (All Engagements)

The following components are included as standard across all active managed service engagements regardless of client-specific report structure:

| Component | Content |
|---|---|
| KPI Performance | SLA adherence, MTTR, availability |
| Call Management Statistics | Incident volumes, categories, resolution rates |
| Service Requests | Request volumes, completion rates, backlog status |
| Support Hours | Hours consumed by category — incident, change, project, administration |
| Security and Governance | Access review status, policy exceptions, compliance items |
| Commercial Feedback | Invoice status, hours reconciliation |
| Risks and Issues | Active risk and issue log with owners and resolution timelines |

*Source: MTN-2026 lines 725–749 (Q21 Backup and Recovery SOP table of contents) — Blocks B-006 / B-015*
*Source: MTN-2026 lines 783–828 (Q22 Monthly report table of contents) — Blocks B-007 / B-016*

---

## Section 12 — Migration and ETL Support Capability

APPSolve applies a structured, low-risk migration framework to support cross-platform data movement and ETL operations, ensuring data integrity, minimal downtime, and full business continuity. The approach is built on a repeatable Migration Factory model enabling consistent, scalable, and controlled execution. Migration factory and ETL services are delivered where explicitly included in the engagement scope — they are not a default component of all Oracle DBA managed services contracts.

### 12.1 Migration Scenarios and Tooling

| Scenario | Mechanism | Tools |
|---|---|---|
| Homogeneous (Oracle → Oracle / SQL → SQL) | Native backup/restore, replication | RMAN, DataGuard, SQL AlwaysOn |
| Heterogeneous (MS SQL → Oracle / Oracle → MS SQL) | ETL / data conversion | Oracle GoldenGate, SSIS, Azure Data Factory |
| Large-scale / Near-zero downtime | Real-time replication | GoldenGate, Change Data Capture (CDC) |
| OS Migration (Unix → Linux) | Lift-and-shift / replatforming | RMAN duplicate, file system migration |
| BI / EIS workloads | Parallel ETL pipelines | PL/SQL, SQL*Loader |

### 12.2 Migration Factory Approach

APPSolve implements a repeatable, industrialised migration framework ensuring consistency, quality, and scalability:

**Discovery and Assessment**
- Full inventory of source systems — schemas, data volumes, dependencies, integrations
- Workload profiling — transaction rates, peak usage, batch windows
- Complexity classification (low / medium / high) to prioritise migration waves

**Design and Mapping**
- Data model mapping — Oracle ↔ MS SQL datatype conversions, MySQL nuances
- Code and object conversion strategy — PL/SQL, T-SQL, procedures, triggers
- Integration and interface alignment — ETL, APIs, flat files

**Migration Factory Execution**
- Standardised pipelines for schema conversion, data migration, validation, and reconciliation
- Automation using Oracle Data Pump, GoldenGate, SSIS, or custom scripts
- Parallel processing where feasible to accelerate large dataset movement

**Testing Framework**
- Unit testing of converted objects
- System Integration Testing (SIT)
- User Acceptance Testing (UAT)
- Data validation and reconciliation reports — row counts, checksums, business rule verification

### 12.3 Cutover Strategy

| Phase | Activity |
|---|---|
| Cutover Planning | Defined runbook with step-by-step execution tasks, owners, and timelines; multiple dry runs (mock cutovers) to validate timing and dependencies; business sign-off checkpoints before final execution |
| Execution | Freeze window on source systems; final delta data synchronisation; application switch-over and connectivity validation; post-cutover technical and business verification |
| Rollback | Source system maintained in a fully operational state during cutover; backup and restore points established prior to migration; defined rollback decision criteria (performance thresholds, data discrepancies); ability to revert applications and integrations within agreed SLA timelines |

### 12.4 Downtime Minimisation Techniques

| Technique | Description |
|---|---|
| Incremental / Data Replication | Oracle GoldenGate or equivalent CDC for near real-time sync; pre-loading of bulk data followed by delta synchronisation |
| Parallel Run / Dual Systems | Source and target systems operated in parallel during transition; gradual cutover of users or workloads where feasible |
| Optimised Data Movement | Partition-level migration for large datasets; compression and high-throughput transfer mechanisms |

### 12.5 ETL Capability

APPSolve delivers ETL functions through a controlled, auditable, and automation-driven approach using Oracle-native capabilities.

**Flat File Integration:** Secure, standardised intake process for source files via agreed channels (SFTP, shared locations, system drop zones). File handling includes validation of naming conventions, structure, encoding, delimiter consistency, mandatory fields, and record counts before processing. Files loaded into staging tables using Oracle External Tables or SQL*Loader, preserving raw source data for reconciliation and audit.

**PL/SQL Scheduling:** Oracle DBMS_SCHEDULER and database-resident PL/SQL packages orchestrate ETL cycles. Jobs configured with clear separation between extract, staging, transformation, validation, and final load phases. All jobs include logging, exception handling, restart capability, and notification mechanisms.

**Multi-Source Data Extraction:** Source-specific extraction methods — direct database connectivity (database links), API-based extraction, staged file-based imports, or controlled queries against upstream operational systems. All extraction processes designed to minimise source-system impact and support incremental or full loads as required.

**Data Transformation:** Layered transformation model — raw source data normalised in staging, then processed into target-ready structures using documented business rules. Rules include: mapping, data cleansing, format standardisation, derivation of calculated values, lookups against reference tables, duplicate handling, mandatory field validation, and cross-field logic. All business rules documented, version-controlled, and verified with stakeholders.

### 12.6 Migration Evidence

**MySQL → Oracle Migration:** Migrated operational data from MySQL into Oracle for improved reporting and integration with ERP systems. Minimal downtime achieved using staged data loads and final delta synchronisation.

**Oracle Endian Migration (Platform Migration):** Migrated Oracle databases across platforms with different endian formats using RMAN and Data Pump methodologies. Data integrity confirmed through checksum validation and multiple test cycles.

**Hybrid Data Consolidation:** Consolidated data from multiple source systems into a centralised database platform. Standardised ETL and validation pipelines implemented as part of the migration factory approach.

*Source: MTN-2026 lines 352–480 (Q5 migration factory approach, Q6 ETL functions, Q11 migration mechanisms) — Block B-010*

---

## Section 13 — 24x7 Support Structure

APPSolve implements a robust, always-on support capability to ensure continuous database availability for large-scale, business-critical environments. Where contractually required, 24x7 coverage is provided across all contracted hours — including weekdays, weekends, and public holidays.

### 13.1 Tiered Support Model

APPSolve implements a tiered on-call support model:

| Role | Responsibility |
|---|---|
| **Primary On-Call DBA (L2/L3)** | Certified database specialist assigned per shift; responsible for incident triage, response, and change execution |
| **Secondary Escalation DBA (L3/SME)** | Available for complex issues requiring deep technical expertise — Oracle internals, RAC, DataGuard, GoldenGate |
| **Service Delivery Lead (On-call)** | Ensures SLA adherence and stakeholder communication for critical incidents; escalation point for P1/P2 events |

### 13.2 Coverage Model

| Coverage Window | Structure |
|---|---|
| Business hours | Full BAU support team in place |
| Extended hours (weekday evenings) | On-call standby with agreed response SLAs |
| Weekends | Dedicated standby rotation with full escalation coverage |
| Public holidays | Dedicated standby rotation with full escalation coverage |
| 24/7 Monitoring | Client monitoring tools supplemented by APPSolve database-specific monitoring for proactive alerting |

Coverage windows and response SLAs are defined per engagement during service initiation and formalised in the service agreement.

### 13.3 Incident Support Approach

- Integration with the client's Incident Management process (ITIL-aligned)
- Priority-based response aligned to SLA severity levels (P1/P2/P3/P4 or equivalent client tier classification)
- Immediate triage, containment, and resolution — structured escalation from L2 to L3 to SME
- Continuous communication with client stakeholders throughout P1/P2 incidents
- Post-incident review and RCA for major events

### 13.4 Change Implementation Support

APPSolve provides after-hours support for planned change execution:

- Pre-approved changes executed during agreed maintenance windows
- Strict adherence to client Change Management controls — no change executed without approval and rollback plan
- Pre-change validation, rollback planning, and post-change verification for every deployment
- Coordination with client application, infrastructure, and security teams as required

### 13.5 Shift and Resource Management

| Practice | Description |
|---|---|
| Rotational standby roster | Fatigue management and operational continuity — no single resource on permanent standby |
| Skills-aligned scheduling | On-call resources matched to platform skills — Oracle, SQL Server, specialised tools |
| Backup resource assignment | Backup on-call resource always assigned to eliminate single points of failure |
| Skills depth | Multiple resources with equivalent skills ensure continuity during leave, illness, or escalation events |

*Source: MTN-2026 lines 832–872 (Q23 24x7 support structure full detail)*
*24x7 framing: consistent with A-005 BU Lead decision in W2S1-003 (confirmed 2026-06-11) — "where contractually required"; after-hours response SLA times excluded (line 852: "<15-minute response SLA" is a client-specific commitment; response times agreed per engagement during service initiation)*

---

## Section 14 — Limitations and Review Notes

### 14.1 Extraction Constraints Applied

| Constraint | Action Taken |
|---|---|
| MTN-specific capacity metrics (lines 562–565) | Excluded: "1000+ databases", "reduced capacity-related incidents by over 40%", "environment build times from days to hours" are client-specific operational metrics prohibited by ORACLE_FACT_BASELINE.md Section 13 |
| MTN-specific database count (line 631) | Excluded: "300+ Oracle and 2000+ MS SQL databases" — same treatment as FR-G in W2S1-003; replaced with "large-scale enterprise database estate" throughout |
| System availability percentage (line 578) | Excluded: ">99.99% availability in previous enterprise environments" is a client-specific SLA achievement — cannot be asserted as a generic APPSolve standard |
| After-hours response SLA time (line 852) | Excluded: "<15-minute response SLA" is a client-specific commitment — replaced with "response SLAs agreed during service initiation and defined in the service agreement" |
| Fixed meeting cadence (lines 503–517) | Framed as indicative governance model throughout Section 4.2 — not presented as a committed service schedule |
| Fixed report frequencies (lines 519–537) | Framed as indicative model — reporting categories tailored to client requirements and agreed during service initiation |
| MTN company profile section (lines 1187–1410) | Not accessed — company and partnership claims sourced exclusively from approved W1S1 files |
| Historical technology references in monthly report TOC | Resolved per A-W4-005 — technology-specific subsection labels from historical engagements removed; current labels used throughout |
| Q24 (other DB technologies, lines 875–911) | Excluded per A-W4-007 — document remains Oracle-managed-services focused; Q24 excluded permanently from this document |

### 14.2 W2S1-003 Overlap Boundary

W2S1-004 deliberately expands content that W2S1-003 introduced at executive-summary level. The following table defines the boundary:

| Topic | W2S1-003 Coverage | W2S1-004 Coverage |
|---|---|---|
| ITIL Framework | 4-bullet summary (Section 9.2) | Full per-discipline narrative with runbooks, escalation, MTTR focus (Section 2) |
| CSI Model | 4-stage headline + 3-pillar (Section 9.3) | Full closed-loop with CSI register and improvement disciplines (Section 3) |
| Service Delivery Management | Not covered | Full governance cadence, reporting framework, SDM/CSM roles (Section 4) |
| Capacity Management | Not covered | Full capacity, demand, and provisioning framework (Section 5) |
| Performance Management | Executive narrative (Section 4) | Full sub-domain detail — space, accounts, health checks, continuous improvement (Section 6) |
| Monitoring | 3-layer table (Section 4.3) | Full domain coverage — 5 domains per-item, proactive monitoring capabilities (Section 7) |
| CMDB | CI attributes summary (Section 3.3) | Full model — automated discovery, change-driven updates, continuous validation (Section 8) |
| Release and Deployment | N-1, upgrade governance, version control (Sections 6.1–6.3) | Full ITIL-DevOps integrated framework — patch management, ETL pipeline, tooling specifics (Section 9) |
| Segregation of Duties | Access control table — 5 controls (Section 7.2) | Full SoD framework — 7 control dimensions, emergency access, dual control, RACI matrices (Section 10) |
| Documentation Standards | Not covered | Backup SOP structure, Monthly Report TOC, standard components (Section 11) |
| Migration and ETL | Not covered (excluded from exec summary) | Full migration factory, cutover strategy, rollback, ETL functions, migration evidence (Section 12) |
| 24x7 Support | Support tier table and coverage hours (Section 9.1) | Full tiered model with incident approach, change support, shift management (Section 13) |

### 14.3 MS SQL Scope Note

**BU Lead decision applied (A-W4-007, 2026-06-11):** This document remains Oracle-managed-services focused. Microsoft SQL Server references are retained only where required to explain large-scale estate management experience or cross-platform tooling breadth in the context of Oracle engagements. No Acumatica, MongoDB, MySQL managed services, or other non-Oracle platform claims have been added or expanded. Q24 multi-platform content (MTN-2026 lines 875–911) remains excluded from this document. If a separate multi-platform managed services capability block is required in future, it must be created as a distinct KB document with independent BU Lead review.

### 14.4 Migration Evidence Scope

**BU Lead decision applied (A-W4-003, 2026-06-11):** Migration evidence in Section 12.6 is retained as general migration capability examples — MySQL → Oracle, Oracle Endian Migration, Hybrid Data Consolidation. These are presented as migration type categories demonstrating methodology and tooling breadth. A note has been added to Section 12 confirming that migration factory and ETL services are engagement-specific, not a default component of all Oracle DBA managed services contracts. The examples do not name specific clients in the source document (MTN-2026 Q5) and are usable as general capability evidence.

---

---

# EXTRACTION DOCUMENTATION

> The sections below are internal extraction records. They do not form part of the managed services content and must be removed before any tender use.

---

## Approval Record

| Field | Value |
|---|---|
| **Approved by** | Hein Blignaut |
| **Approval date** | 2026-06-11 |
| **Approval rationale** | All factual risks FR-W4-001 through FR-W4-009 resolved. All assumptions A-W4-001 through A-W4-007 resolved and documented. No unsupported client-specific metrics remain. No MTN-specific SLA commitments remain. No unsupported commercial commitments remain. No prohibited wording remains. No unresolved source attribution issues remain. Document is suitable for reuse in Oracle managed services tenders. |
| **Extraction date** | 2026-06-11 |
| **Review date** | 2026-06-11 |
| **Reviewed by** | Hein Blignaut |
| **Pipeline path** | Candidate (2026-06-11) → Review_Required (2026-06-11) → Approved (2026-06-11) |
| **Superseded file** | `07_Approved_Content/Candidate_Content/Oracle/W2S1-004-ORA-ManagedServicesSupportModel.md` — marked SUPERSEDED; manual deletion via Finder required (OneDrive blocks terminal deletion) |

---

## Source Mapping Table

| Claim / Section | Primary Source | Supporting Source | Sourced / AI-Authored |
|---|---|---|---|
| Section 1 — Executive Overview | W1S1-003 (partner tier); W1S1-007 (DBA team, Hybrid Support Model, Monthly Recurring Invoice Model); W1S1-009 (differentiators) | W2S1-003 Section 1 (framing) | Sourced — approved W1S1 files; introductory paragraph and overlap framing AI-authored (required) |
| Section 2 — ITIL Framework (all subsections) | MTN-2026 lines 435–445 (Q8) | — | Sourced — narrative expanded from source; discipline sequence and structure preserved |
| Section 3 — CSI Model (all subsections) | MTN-2026 lines 482–497 (Q12) | — | Sourced — 4-stage table direct extraction; improvement disciplines table structured from source list |
| Section 4 — Service Delivery Management | MTN-2026 lines 499–541 (Q13) | W2S1-003 Section 9.3 and 11 (CSM engagement model) | Sourced — cadence and reporting tables direct extractions; indicative framing and mandated wording updates AI-authored per BU Lead decisions A-W4-001 and A-W4-002 |
| Section 5 — Capacity and Demand Management | MTN-2026 lines 543–561, 566–572 (Q14; lines 562–565 excluded) | — | Sourced — provisioning table structured from source list; prohibited lines excluded |
| Section 6 — Performance Management | MTN-2026 lines 579–599 (Q16) | — | Sourced — health check table direct extraction; section headings structured by extractor |
| Section 7 — Monitoring Framework | MTN-2026 lines 670–722 (Q20) | — | Sourced — domain coverage tables structured from source lists; domain headings and outcome statements preserved from source |
| Section 8 — CMDB Governance | MTN-2026 lines 629–668 (Q19) | — | Sourced — CI attributes table, discovery mechanisms, change-driven updates all sourced; scale descriptor excluded per governance |
| Section 9 — Release and Deployment | MTN-2026 lines 993–1037 (Q27) | — | Sourced — patch management table, ETL pipeline, version control table all sourced from source structure |
| Section 10 — Segregation of Duties | MTN-2026 lines 1053–1167 (Q28) | MTN-2026 lines 751–780 (Access Management SOP TOC) | Sourced — role separation table, access controls table, dual control table, governance activities all sourced; cross-engagement framing per A-W4-004 AI-authored |
| Section 11.1 — Backup SOP TOC | MTN-2026 lines 725–749 (Q21) | — | Sourced — direct extraction of SOP table of contents; per-client framing per A-W4-006 AI-authored |
| Section 11.2–11.3 — Monthly Report TOC | MTN-2026 lines 783–828 (Q22) | — | Sourced — comprehensive TOC direct extraction; standard components table structured from simplified TOC; historical technology note updated per A-W4-005 |
| Section 12 — Migration and ETL | MTN-2026 lines 352–480 (Q5, Q6, Q11) | — | Sourced — migration scenarios table, factory stages, cutover strategy, ETL functions all sourced; engagement-specific scoping note per A-W4-003 AI-authored |
| Section 13 — 24x7 Support Structure | MTN-2026 lines 832–872 (Q23) | W2S1-003 Section 9.1 and A-005 (BU Lead confirmed framing) | Sourced — tiered model table, coverage model table, shift management table all sourced; response SLA exclusion and 24x7 framing AI-authored (required per A-005 governance) |
| Section 14 — Limitations and overlap | BU Lead decisions (W2S1-003 approved); ORACLE_FACT_BASELINE.md | — | AI-authored documentation — no capability claims |

---

## Assumptions Register

All assumptions scoped by Hein Blignaut — 2026-06-11. No open items remain.

| ID | Assumption | Section | Decision Applied | Status |
|---|---|---|---|---|
| A-W4-001 | Governance cadence (Daily/Weekly/Monthly/Quarterly) — indicative framework, not a committed contractual schedule | Section 4.2 | Retained as indicative. Wording updated: "Governance cadence is tailored during service initiation and agreed in the SLA or service governance plan." | **RESOLVED 2026-06-11** |
| A-W4-002 | Five report types (SLA, Incident, Change, Capacity, CSI Register) — standard categories, not fixed deliverables or frequencies | Section 4.3 | Retained as standard categories. Wording updated: "Reporting categories are tailored to client requirements and agreed during service initiation." | **RESOLVED 2026-06-11** |
| A-W4-003 | Migration evidence examples — general capability evidence, not single-client-specific | Section 12, 14.4 | Retained. Section 12 intro updated: migration factory services are engagement-specific, not included by default. Section 14.4 updated to confirm scope. | **RESOLVED 2026-06-11** |
| A-W4-004 | Access Management SOP TOC — cross-engagement documentary evidence, client name redacted | Section 10.10 | Retained. Wording updated: "Access governance documentation is adapted to each client's IAM model, audit requirements, and operational controls." | **RESOLVED 2026-06-11** |
| A-W4-005 | Monthly report structure — current reporting maturity evidence, historical technology subsections removed | Section 11.2 | Retained. Note strengthened to explicitly state historical technology-specific subsection labels have been removed and replaced with current equivalents. | **RESOLVED 2026-06-11** |
| A-W4-006 | Backup and Recovery SOP — per-client, aligned to agreed backup policies and recovery objectives | Section 11.1 | Retained. Framing updated: "Backup and recovery SOPs are maintained per client environment, aligned to agreed backup policies, retention requirements, and recovery objectives." | **RESOLVED 2026-06-11** |
| A-W4-007 | Q24 multi-platform content (MongoDB, MySQL, HeatWave) excluded — document remains Oracle-focused | Section 14.3 | Confirmed: W2S1-004 remains Oracle-managed-services focused. MS SQL references retained only where contextually required. No multi-platform expansion. Q24 remains excluded. Section 14.3 updated to record this as a confirmed BU Lead decision. | **RESOLVED 2026-06-11** |

---

## Factual Risk Assessment

| ID | Risk | Section | Severity | Status |
|---|---|---|---|---|
| FR-W4-001 | **Capacity metrics prohibited** — Lines 562–565: "1000+ databases", "40% reduction in capacity-related incidents", "environment build times from days to hours" | Section 5 | CRITICAL | **RESOLVED** — Lines 562–565 excluded. "Large-scale enterprise database estate" framing used throughout. |
| FR-W4-002 | **MTN-specific database count** — Line 631: "300+ Oracle and 2000+ MS SQL databases" | Section 8 | HIGH | **RESOLVED** — Excluded. Consistent with FR-G treatment in W2S1-003 (approved 2026-06-11). |
| FR-W4-003 | **SLA achievement percentage** — Line 578: ">99.99% availability in previous enterprise environments" | — | HIGH | **RESOLVED** — Excluded. Not asserted as a generic APPSolve standard. |
| FR-W4-004 | **After-hours response SLA time** — Line 852: "<15-minute response SLA" | Section 13 | MEDIUM | **RESOLVED** — Excluded. "Response SLAs agreed during service initiation and defined in the service agreement" used in Section 13.2. |
| FR-W4-005 | **Meeting cadence as contractual commitment** — Lines 503–517 | Section 4.2 | MEDIUM | **RESOLVED** — Framed as indicative governance model throughout Section 4.2. Not presented as a committed service schedule. |
| FR-W4-006 | **Report frequency as contractual commitment** — Lines 519–537 | Section 4.3 | MEDIUM | **RESOLVED** — Framed as indicative model. Reporting categories stated as tailored to client requirements and agreed during service initiation. |
| FR-W4-007 | **Historical technology references** — Lines 803–827: monthly report TOC contains references from earlier Oracle versions | Section 11.2 | LOW | **RESOLVED** — Note strengthened per A-W4-005. Technology-specific historical subsections explicitly removed. |
| FR-W4-008 | **Q24 excluded content** — "Acumatica Growth Partner of the Year" and MongoDB/MySQL/HeatWave capability claims not verified in ORACLE_FACT_BASELINE.md | — | LOW | **RESOLVED by exclusion** — Q24 not included. BU Lead decision confirmed: Q24 permanently excluded from this document (A-W4-007). |
| FR-W4-009 | **CSM commercial commitment** — consistency with W2S1-003 A-007 resolution ("at no cost" removed) | Section 4.4, 13 | MEDIUM | **RESOLVED** — CSM presented as engagement model throughout; no commercial term; consistent with W2S1-003 approved wording (BU Lead confirmed 2026-06-11). |

---

## Approval Gate Summary

**Approved: 2026-06-11 by Hein Blignaut**

All 16 pre-assigned MTN-2026 content blocks extracted. All mandatory exclusions applied. All required generalisations complete. All 9 factual risks resolved. All 7 assumptions scoped and resolved. Wording updated per BU Lead decisions. Document suitable for reuse in Oracle managed services tenders.

---

*Extraction: 2026-06-11 — Wave 2 Session 1*
*Extracted by: AI (Claude Sonnet 4.6)*
*Primary source: APPSolve_MTN_DBA_RFP_RFX-1000004246_v1.0.docx — 05 April 2026 (1,495 lines)*
*16 pre-assigned content blocks: B-001, B-002, B-003, B-004/B-011, B-005/B-013, B-006/B-015, B-007/B-016, B-008, B-009, B-010, B-012, B-014, Q23*
*Governance: ORACLE_FACT_BASELINE.md; CHECKPOINT_ORACLE_WAVE2_2026-06-11.md*
*Approved content sources: W1S1-003 Oracle Partnership; W1S1-007 Delivery Model; W1S1-009 Key Differentiators*
*Complements: W2S1-003 Oracle DBA Executive Summary (Approved 2026-06-11)*
*Physical location: 07_Approved_Content/Approved/Oracle/*
