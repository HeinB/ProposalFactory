---
file_id: W2S1-003
title: Oracle DBA and Database Managed Services — Executive Summary
bu: Oracle
wave: 2
session: 1
source_status: Approved
approved_for_reuse: Yes
approved_by: Hein Blignaut
approval_date: 2026-06-11
extraction_date: 2026-06-11
extracted_by: AI (Claude Sonnet 4.6) — Wave 2 Session 1
reviewed_by: Hein Blignaut
review_date: 2026-06-11
review_notes: "Approved 2026-06-11 by Hein Blignaut. BU Lead decisions applied: FR-D (DFA exclusion), FR-F (capacity wording), FR-G (scale wording), Section 7.4 (rewritten — POPIA framing changed to client-obligation-facing; AI-authored bridging removed), A-005 (24x7 qualified to where contractually required), A-006 (CIM confirmed standard across all managed service accounts), A-007 (at no cost removed — Dedicated Customer Success Manager engagement model). Pre-tender use: confirm client citability A-001, A-002, A-003 with account managers before first tender submission."
kb_destination: 06_Capabilities/Oracle/DBA_Managed_Services/
related_files:
  - 00_Governance/ORACLE_FACT_BASELINE.md
  - 00_Governance/W2S1-003_READINESS_REPORT.md
  - 00_Governance/ORACLE_WAVE2_EXECUTION_PLAN.md
  - 07_Approved_Content/Approved/Cross_BU/W1S1-003-ORA-OraclePartnership.md
  - 07_Approved_Content/Approved/Cross_BU/W1S1-007-CORP-DeliveryModel.md
tags: [oracle-dba, database-administration, managed-services, monitoring, patching, backup-recovery, dr, performance-tuning, capacity-planning, security, itil, 24x7]
---

> **APPROVED — 2026-06-11 | Approved by: Hein Blignaut**
> BU Lead decisions applied: FR-D (DFA exclusion), FR-F (capacity wording), FR-G (scale wording), Section 7.4 (rewritten — POPIA framing changed to client-obligation-facing), A-005 (24x7 qualified to where contractually required), A-006 (CIM confirmed standard), A-007 ("at no cost" removed; Dedicated Customer Success Manager engagement model applied).
> Pre-tender use confirmation required: confirm client citability for all named reference accounts (A-001, A-002, A-003) with account managers before first tender submission.

---

# Oracle DBA and Database Managed Services — Executive Summary

## Section 1 — Executive Overview

APPSolve delivers end-to-end Database Administration (DBA) and database managed services as a core capability, with a team built over more than two decades of Oracle database practice in Southern Africa. Our DBA offering covers the full lifecycle of Oracle database environments — from installation and configuration through proactive monitoring, performance optimisation, lifecycle management, security governance, and disaster recovery — all delivered through a structured, ITIL-aligned service model with 24/7 support available where contractually required.

APPSolve's approach positions database managed services not as reactive support, but as a proactive, engineering-led capability that continuously improves platform resilience, performance, and cost efficiency. Our service model is built on disciplined operational execution, structured governance, and forward-looking innovation — leveraging automation, advanced monitoring, and continuous optimisation to protect high-availability environments while preparing the database estate for future demands.

APPSolve is an **Oracle Level 1 Partner** and **Oracle Cloud Excellence Implementer** with established OEM vendor relationships that enable efficient escalation and resolution of complex Oracle database issues, as well as proactive input into product improvements. We maintain **one of the largest locally-based Oracle Applications DBA teams in South Africa**, providing clients with depth and continuity of service that is difficult to replicate.

APPSolve's DBA managed services are delivered through a **Hybrid Support Model** that combines on-site and remote resource allocation, a dedicated Customer Success Manager, and a **Monthly Recurring Invoice Model** that provides flexible and predictable cost management for long-term engagements.

*Source: MTN-2026 lines 47–55 (executive summary narrative — corrected); W1S1-003 (partner tier); W1S1-007 (DBA team claim, delivery model, Monthly Recurring Invoice Model)*

---

## Section 2 — DBA Service Scope

APPSolve delivers full lifecycle DBA services across Oracle and MS SQL platforms. The service scope is organised into three layers:

### 2.1 Core DBA Services

| Service | Description |
|---|---|
| Database Installation and Configuration | Deployment of Oracle database instances to approved standards and baselines |
| Proactive Monitoring | Real-time and threshold-based monitoring of availability, performance, capacity, and replication |
| Performance Tuning and Optimisation | Query optimisation, execution plan analysis, index management, and workload balancing |
| Backup, Recovery, and DR | RMAN-based backups, incremental and full strategies, DR environment configuration and testing |
| Patch and Version Management | N-1 compliance patching across Oracle and MS SQL, with non-production validation |
| Capacity and Space Management | Predictive growth analysis, threshold-based alerts, space and tablespace governance |
| Security, Auditing, and Access Control | Role-based access control (RBAC), user account governance, audit log review, POPIA alignment |
| Database Decommissioning | Structured retirement of database instances with data archiving and CMDB closure |

*Source: MTN-2026 lines 100–106 (scope categories); W1S1-007 lines 50–56 (DBA services list — approved)*

### 2.2 Advanced and Platform-Specific Services

| Service | Description |
|---|---|
| ETL and Data Integration | PL/SQL, SQL Loader, Oracle Heterogeneous Services — file-based and source-based data movement |
| Oracle Ecosystem Tools | Oracle APEX, RAC, DataGuard, GoldenGate, Oracle Enterprise Manager (OEM) |
| Cross-Platform Database Migration | Oracle to Oracle, OS migrations, heterogeneous migrations (MySQL → Oracle, MS SQL ↔ Oracle) |
| BI and EIS Database Support | High-throughput Business Intelligence and enterprise information system environments |
| OEM Vendor Engagement | Oracle Service Request (SR) management, defect escalation, patch roadmap input |

*Source: MTN-2026 lines 108–113 (advanced services scope)*

### 2.3 Service Management Disciplines

APPSolve aligns all services to the client's ITIL framework:
- Incident, Problem, Change, and Event Management
- Request Fulfilment and Release Management
- Service Level Management and Reporting
- Continuous Service Improvement
- Configuration and Asset Management (CMDB)

*Source: MTN-2026 lines 115–121 (service management alignment)*

---

## Section 3 — Oracle Database Administration Capability

APPSolve's Oracle DBA team provides structured, standards-driven administration across Oracle 12c, 19c, and Fusion Cloud environments, covering both on-premise and cloud-hosted database deployments.

### 3.1 Daily Operational Activities

APPSolve executes a standardised daily health-check programme across every Oracle environment under management:

| Check | Scope |
|---|---|
| Database availability and connectivity | Instance up/down status and connection validation |
| Backup status and success rates | RMAN backup job confirmation, failure alerting |
| Replication health | DataGuard / AlwaysOn lag, sync status, failover readiness |
| Tablespace and disk utilisation | Growth trends, auto-growth events, threshold breaches |
| Index fragmentation and statistics status | Freshness of statistics, fragmentation levels, rebuild flags |
| Error logs and alert logs | Oracle alert log review, ORA- error identification and triage |

Findings are consolidated into daily reports with actionable insights and escalation triggers.

*Source: MTN-2026 lines 590–597 (daily health check components)*

### 3.2 Database Account Management

APPSolve enforces strict governance aligned to security and audit requirements. Account reviews are conducted regularly to identify expired, inactive, or orphaned accounts, ensuring timely deactivation or removal. Role-based access controls are maintained in alignment with least-privilege principles, and all changes are tracked through the client's Change Management process.

*Source: MTN-2026 lines 589 (account management approach)*

### 3.3 CMDB and Configuration Governance

APPSolve maintains Configuration Item accuracy for all database instances under management. Standard CI attributes captured include database instance name, hostname, environment tier (Dev / QA / UAT / Prod / DR), data centre location, port numbers, database version and patch level, and application-to-database relationships. Changes to CI data are integrated into the client's Change Management process to ensure CMDB accuracy is maintained continuously — not treated as a separate activity.

*Source: MTN-2026 lines 629–657 (CMDB governance approach — summarised for executive summary)*

---

## Section 4 — Performance Monitoring and Tuning

APPSolve delivers a holistic, engineering-led Performance Management framework designed to ensure Oracle environments operate optimally and without disruption. The approach combines continuous performance monitoring, automated maintenance, and ongoing optimisation.

### 4.1 Performance Monitoring Approach

APPSolve implements continuous performance monitoring and tuning covering:
- Real-time tracking of CPU, memory, I/O, wait events, and query execution times
- Proactive identification of bottlenecks with targeted interventions (query optimisation, indexing strategies, execution plan tuning)
- Sustained performance under high-throughput environments including Business Intelligence and EIS systems

### 4.2 Space Management

Space management is tightly controlled through automated monitoring of data files, log files, and tablespaces. Threshold-based alerts and predictive growth analysis prevent capacity issues. Regular housekeeping includes log file management, archiving, purging of obsolete data, and proactive space allocation.

### 4.3 Monitoring Architecture

APPSolve implements monitoring across three layers:

| Layer | Scope |
|---|---|
| Infrastructure Layer | CPU, memory, disk I/O, network |
| Database Layer | Core database health, performance, replication, capacity |
| Service Layer | Application-to-database performance correlation — degradation detected before user impact |

APPSolve integrates with client monitoring infrastructure (Oracle OEM, SQL Server DMVs, custom scripts) while supplementing with database-specific intelligence and automated alerting.

> **W2S1-004 note:** Full detail on monitoring domain coverage (space, logs, indexing, fragmentation, partitioning — Q20) and the full CSI model are reserved for W2S1-004 Oracle Managed Services Support Model.

*Source: MTN-2026 lines 579–599 (Q16 performance management); lines 670–722 (Q20 monitoring framework — summarised)*

---

## Section 5 — Backup, Recovery and DR Support

APPSolve delivers a resilient, multi-layered Disaster Recovery and Business Continuity framework ensuring database services remain available with minimal or no business impact in the event of system, database, or data centre outages.

### 5.1 High Availability Architecture

APPSolve leverages the following technologies across Oracle environments:

| Technology | Purpose |
|---|---|
| Oracle DataGuard | Real-time or near real-time data replication between primary and standby environments |
| Oracle RAC (Real Application Clusters) | Multi-instance database availability; workload distribution |
| Oracle GoldenGate | Near-zero downtime replication; used in migrations and cross-platform synchronisation |
| SQL Server AlwaysOn | High availability for MS SQL environments |
| Geographically Separated DR Environments | Resilience against full data centre failures |

### 5.2 Backup Strategy

APPSolve implements automated backup strategies using:
- Full, incremental, and log backups via Oracle RMAN
- Regular restore testing to confirm data recoverability
- Backup success monitoring as part of daily health checks
- Retention periods aligned to client data management policies

### 5.3 DR Process

In the event of an outage, APPSolve follows a predefined, SLA-driven recovery process:
1. Rapid incident assessment and classification
2. Immediate activation of DR procedures
3. Controlled failover to standby systems
4. Continuous communication with client stakeholders
5. Post-recovery validation and performance checks

APPSolve conducts scheduled failover and failback exercises to validate system readiness, data integrity, and recovery timelines. DR tests are fully documented and aligned to the client's governance processes.

RTOs and RPOs are defined per environment tier and agreed during service initiation.

*Source: MTN-2026 lines 601–613 (Q17 DR/BCM approach)*

---

## Section 6 — Patching, Upgrades and Lifecycle Management

### 6.1 N-1 Patching Strategy

APPSolve adopts a structured, risk-balanced patching strategy to ensure all database platforms are consistently maintained at N-1 compliance — the most recent minor release minus one — balancing stability with security. The N-1 approach ensures systems benefit from enhanced security and defect resolution without exposure to unverified latest releases.

**Patch lifecycle:**

| Stage | Activity |
|---|---|
| OEM Monitoring | Continuous review of Oracle and Microsoft patch advisories for relevance, risk, and impact |
| Non-Production Validation | Deployment into Dev → QA → UAT with automated regression testing, workload simulation, and compatibility validation |
| Compliance Tracking | Automated patch tracking dashboards showing version status across the estate |
| Controlled Deployment | CAB-approved after-hours deployments with pre- and post-validation checks and rollback procedures |

*Source: MTN-2026 lines 447–452 (Q9 N-1 patching strategy)*

### 6.2 Database Upgrades

APPSolve manages database upgrades through a structured, delivery-driven project management framework integrated with the client's ITIL processes:
- Scope definition, stakeholder alignment, and impact assessment
- Standardised build, test, and release processes (factory-based approach)
- CAB governance with documented risk assessments and back-out procedures
- After-hours execution with full pre- and post-validation
- Post-implementation review and lessons-learned capture

*Source: MTN-2026 lines 453–459 (Q10 project management for upgrades)*

### 6.3 Version Control and Release Management

All database and ETL code changes are managed through:
- Centralised version control (Git-based repositories or Azure DevOps)
- Structured branching and merging strategies (feature, release, hotfix)
- Full audit trail of changes (who, what, when)
- Release packaging and tagging for reproducibility

*Source: MTN-2026 lines 1030–1035 (Q27 version control)*

---

## Section 7 — Security and Access Governance

### 7.1 Security Compliance Model

APPSolve ensures compliance with client audit committee security findings through a closed-loop security governance model focused on prevention, remediation, and continuous assurance.

All security findings are logged, categorised, and prioritised within a formal remediation register. Each finding is assigned ownership, target resolution timelines, and measurable outcomes. Post-remediation validation and trend analysis ensures that corrective actions are effective and systemic improvements are implemented to eliminate recurrence.

*Source: MTN-2026 lines 615–627 (Q18 security compliance approach)*

### 7.2 Access Control Framework

| Control | Description |
|---|---|
| Role-Based Access Control (RBAC) | Least-privilege principles; separate accounts for normal access and privileged administration |
| Named Individual Accounts | No shared generic privileged logins unless technically unavoidable |
| Production Access Controls | Production access granted only to approved personnel; elevated access restricted to specific tasks, systems, and time periods |
| Periodic Access Reviews | Regular removal of unnecessary privileges; deactivation of inactive or orphaned accounts |
| Emergency Access (Break-Glass) | Time-bound; full activity logging; incident reference and business justification required; retrospective approval mandatory; elevated access removed immediately after resolution |

*Source: MTN-2026 lines 1053–1080 (Q28 segregation of duties — summarised access controls)*

### 7.3 Database Security Hardening

- Encryption of sensitive data and secure configuration of database services
- Integration with client audit tools (e.g. Guardium) for continuous monitoring and logging
- Proactive vulnerability management — Oracle and Microsoft security advisories monitored continuously
- Security patches prioritised based on risk severity; critical patches addressed without delay
- Automated checks to detect configuration drift, unauthorised access, or policy violations

*Source: MTN-2026 lines 619–626 (Q18 security hardening measures)*

### 7.4 Regulatory Alignment

APPSolve's DBA security practices are structured to support the compliance and regulatory requirements applicable to each client environment:

- **POPIA (Protection of Personal Information Act)** — database access controls, audit logging, and data lifecycle governance assist clients in meeting their POPIA obligations for personal information processed within environments under APPSolve management
- **ITIL Security Management** — APPSolve's security practices are integrated with Incident, Change, and Problem Management disciplines, providing structured governance aligned to client compliance and audit frameworks
- **Client audit committee requirements** — structured audit-ready logging, role-based access recertification, and compliance reporting, calibrated to each client's specific audit findings and standards

*Source: MTN-2026 lines 615–627 (Q18 security compliance approach); ITIL alignment — MTN-2026 lines 435–445 (Q8)*

---

## Section 8 — Oracle Tooling and Technical Competency

APPSolve's DBA team carries established competency across the full Oracle database tooling ecosystem. Evidence is drawn from active and historical managed services engagements.

| Oracle Tool | Experience | Reference Clients |
|---|---|---|
| Oracle APEX | 15+ years, multiple sites | Investec, Adcock Ingram, American Tower Corporation, MTN Group |
| Oracle R | 15+ years | South African Reserve Bank |
| Oracle Heterogeneous Services | 20+ years | Adcock Ingram, Mr Price Group, Investec, KPMG, American Tower Corporation |
| Oracle GoldenGate | 20+ years, multiple sites | FNB, South African Reserve Bank, Assore, Technology Management Network Services |
| Oracle Enterprise Manager (OEM) | 20+ years, multiple sites | KPMG, Adcock Ingram, South African Reserve Bank, African Rainbow Minerals |
| Oracle RAC (Real Application Clusters) | Multiple sites | South African Reserve Bank, Adcock Ingram, Cell C |
| Oracle DBFS | Oracle Database File System Content Store, Secure File Store, DBFS Client | Confirmed capability |
| Oracle DataGuard | Multiple sites | South African Reserve Bank, Adcock Ingram, KPMG, FNB, Harmony Gold, African Rainbow Minerals |

*Source: MTN-2026 lines 926–990 (Q26 EIS tool competency response — direct extraction)*

> **Note to BU Lead:** Reference client names in this table appear in the April 2026 MTN submission. Confirm all clients are still willing to be cited for tool-specific competency before tender use.

---

## Section 9 — 24x7 Support and Operational Governance

### 9.1 Support Model

APPSolve provides 24/7 support services where contractually required for large-scale, business-critical database environments. The support structure is tiered:

| Role | Coverage |
|---|---|
| Primary On-Call DBA (L2/L3) | Certified database specialist assigned per shift; responsible for incident response and change execution |
| Secondary Escalation DBA (L3/SME) | Available for complex issues requiring deep expertise |
| Service Delivery Lead (On-call) | Ensures SLA adherence and stakeholder communication for critical incidents |

**Coverage hours:**
- Weekdays 17:00–08:00: On-call standby
- Weekends and Public Holidays: Dedicated standby rotation with full escalation coverage
- 24/7 Monitoring: Client monitoring tools supplemented by APPSolve augmentation for proactive alerting

*Source: MTN-2026 lines 840–872 (Q23 after-hours support — summarised)*

### 9.2 ITIL-Aligned Service Delivery

All DBA service activities are governed through the client's ITIL framework. APPSolve aligns fully with:
- **Incident Management** — structured lifecycle (detection, logging, categorisation, prioritisation, resolution, closure); predefined runbooks; SLA-driven MTTR focus
- **Problem Management** — proactive Root Cause Analysis (RCA) for major incidents; elimination of recurring failures
- **Change Management** — all production changes via Change Management; CAB-approved; risk-assessed; rollback-planned
- **Event Management** — proactive monitoring; threshold-based alerting; event correlation to reduce alert noise

*Source: MTN-2026 lines 435–445 (Q8 ITIL framework alignment)*

### 9.3 Continuous Improvement Model (CIM)

APPSolve's Continuous Improvement Model is embedded across all managed service engagements:

**Four stages:** Analyse → Plan → Implement → Measure

**Three pillars:** People | Processes | Technology

Improvement opportunities are sourced from incident trends, problem management outputs, performance metrics, capacity reports, and stakeholder feedback. A dedicated CSI register tracks initiatives against ownership, timelines, and benefits realisation.

APPSolve assigns a **Customer Success Manager** (C-level) to managed service engagements, meeting regularly with client stakeholders to ensure strategic alignment.

> **W2S1-004 note:** Full governance cadence (daily/weekly/monthly/quarterly meeting structure), full SLA and operational reporting framework, full CSI closed-loop model, and full capacity/demand management detail are reserved for W2S1-004 Oracle Managed Services Support Model.

*Source: MTN-2026 lines 482–497 (CSI); lines 1377–1392 (CIM structure); line 541 (Customer Success Manager); W1S1-007 line 71 (Monthly Recurring Invoice Model)*

---

## Section 10 — Large-Scale Database Estate Experience

### 10.1 Environment Scale Context

APPSolve has supported large-scale Oracle database estates in enterprise telecommunications, financial services, and mining environments. APPSolve's DBA practice has experience supporting large-scale enterprise database estates, including environments comprising thousands of database instances across Oracle and Microsoft SQL Server platforms, spanning multiple data centres, environment tiers (Dev / QA / UAT / Pre-Prod / Prod / DR), and Oracle technology stacks including RAC, DataGuard, and GoldenGate.

*Source: MTN-2026 lines 62–75 (scope context — 300+ Oracle, 2,000+ MS SQL); BU Lead FR-G approved wording applied 2026-06-11*

### 10.2 Managed Services Reference Clients — Oracle DBA

| Client | Sector | Scope | Platform | Notes |
|---|---|---|---|---|
| MTN SA | Telecommunications | Database monitoring, performance management, backup/recovery, security, patching, upgrades, migrations, cloud DB support | Oracle | Long-standing relationship since APPSolve's founding in 2002 |
| Cell C | Telecommunications | Database monitoring, performance management, backup/recovery, security, patching, upgrades, migrations, DR | Oracle | Historical managed service engagement |
| Virgin Mobile | Telecommunications | Database monitoring, performance management, backup/recovery, security, patching, upgrades, monitoring, DR | Oracle | Historical managed service engagement |
| African Rainbow Minerals (ARM) | Mining | Operating systems, database administration, and application managed services | Oracle | Currently active |
| South African Reserve Bank | Financial Services | Enterprise architecture, DBA, and application support | Oracle | Currently active; BI/EIS environment experience (Daan van der Merwe) |
| KPMG Africa | Professional Services | Operating systems and database support | Oracle | Currently active; 9+ year relationship |
| Adcock Ingram | Pharmaceutical | DBA support including OEM, Heterogeneous Services, DataGuard | Oracle | Confirmed via tool competency evidence |
| Investec | Banking | DBA support including APEX, Heterogeneous Services | Oracle | Confirmed via tool competency evidence |

> **Reviewer note (FR-D — confirmed 2026-06-11):** DFA (Dark Fibre Africa) is excluded from this table and all tender-facing reference content per BU Lead decision FR-D (Hein Blignaut, 2026-06-11). DFA may not be cited as a named reference in any tender response. It may be retained as internal corroborating evidence only. Reinstatement requires a new BU Lead instruction.

*Source: MTN-2026 lines 155–174 (Q1 RFI reference answer); lines 345–347 (Q3 RFP similar size clients); lines 926–990 (Q26 tool evidence — reference clients extracted)*

### 10.3 Telecom Sector Depth

APPSolve has supported three South African telecommunications operators (MTN, Cell C, Virgin Mobile) with Oracle DBA managed services. The team has managed mission-critical billing, CRM, BI, and integration platform databases in high-throughput, zero-tolerance-downtime environments.

*Source: MTN-2026 lines 224–275 (telecom client scope descriptions)*

---

## Section 11 — Differentiators

| Differentiator | Description |
|---|---|
| **One of the largest locally-based Oracle DBA teams in South Africa** | Team depth and breadth provides continuity of service, skills coverage across Oracle versions and tools, and no single points of failure (W1S1-007 approved claim) |
| **Design Assurance Methodology** | Architectural review of database configurations and integration points to prevent recurring defects before they become audit findings. APPSolve engages Oracle engineering directly to drive permanent fixes into patch releases — not just workarounds |
| **Long-standing MTN Oracle DBA experience** | APPSolve has supported MTN's Oracle environment since 2002, providing an unmatched depth of environmental knowledge in the South African telecommunications sector |
| **Oracle Partner Relationships** | Oracle Level 1 Partner status and established OEM vendor relationships enable accelerated SR prioritisation and direct engineering escalation for complex Oracle database defects |
| **Hybrid Support Model** | Unique blended on-site and remote resource model — on-site presence for critical activities; remote delivery for monitoring and BAU; Remote Support Centre for 24/7 standby. Provides cost efficiency without sacrificing service quality |
| **Dedicated Customer Success Manager engagement model** | C-level APPSolve executive assigned to managed service engagements — ensures strategic alignment between APPSolve's delivery team and the client's business objectives |
| **Monthly Recurring Invoice Model** | Flexible and predictable costing method — measured on time spent but monthly cost remains stable. Capacity can be transferred between months. Preferred by clients requiring long-term cost predictability (W1S1-007 approved) |
| **Oracle Cloud DBA Competency** | APPSolve's OCI certifications and Oracle Fusion Cloud implementations (Oracle Level 1 — Oracle E-Business Suite Migration to OCI; Oracle Cloud Infrastructure Migration) extend DBA capability into cloud-hosted Oracle environments |
| **Database optimisation and capacity management** | APPSolve has delivered database optimisation and capacity-management initiatives that reduced infrastructure consumption and improved database performance through proactive monitoring, tuning, and lifecycle management practices |

*Source: MTN-2026 lines 145–149 (key success factors); lines 427–431 (Design Assurance Methodology); lines 1393–1401 (Hybrid Support Model); W1S1-003 (Oracle partnership); W1S1-007 (DBA team claim, delivery model); AI-authored framing for differentiator table structure*

---

## Section 12 — Limitations and Review Notes

### 12.1 Extraction Constraints Applied

| Constraint | Action Taken |
|---|---|
| **MTN-2026 company profile (lines 1187–1410) excluded** | Company and partnership claims sourced exclusively from approved W1S1 files (W1S1-001, W1S1-003, W1S1-007) |
| **FR-D: DFA excluded — confirmed 2026-06-11** | DFA removed from all tender-facing tables and reference sections. Reviewer note added in Section 10.2. DFA retained as internal corroborating evidence only. Reinstatement requires new BU Lead instruction. |
| **FR-F: Quantified claim removed — BU Lead wording applied 2026-06-11** | "Reduced capacity-related incidents by over 40%" removed. BU Lead approved wording applied in Section 11: "APPSolve has delivered database optimisation and capacity-management initiatives that reduced infrastructure consumption and improved database performance through proactive monitoring, tuning, and lifecycle management practices." |
| **FR-G: Database count — BU Lead wording applied 2026-06-11** | BU Lead approved wording applied in Section 10.1: "APPSolve's DBA practice has experience supporting large-scale enterprise database estates, including environments comprising thousands of database instances across Oracle and Microsoft SQL Server platforms." Sourced to MTN-2026 scope (300+ Oracle + 2,000+ MS SQL). |
| **Additional governance rule applied** | Client-specific operational metrics, SLA achievement percentages, incident reduction percentages, performance improvement percentages, specific database counts, staffing numbers, and response-time commitments from MTN-2026 are not extracted into KB. These remain client-engagement-specific. |

### 12.2 HIST-002 Assessment

HIST-002 (MTN 2014 APPSolve Executive Summary, 95 lines) contributed zero unique content to this extraction. All HIST-002 content is superseded by MTN-2026 (April 2026). Confirmed concepts originating in HIST-002 (Hybrid Support Model, CIM, Monthly Recurring Invoice Model) are all more fully articulated and updated in MTN-2026. HIST-002 may be safely archived after this extraction.

### 12.3 MS SQL Scope Boundary

MTN-2026 covers both Oracle and MS SQL database managed services. This KB file (W2S1-003) covers the Oracle DBA scope only. MS SQL managed services capability is a separate extraction task outside the Oracle Wave 2 scope. All MS SQL client references (Expert Buying Group, Truman and Orange, NeuCoat) have been excluded from this file.

*Source: Decision by extractor; consistent with W2S1-003 scope definition*

### 12.4 Oracle Awards

The 2026 MTN-2026 proposal lists only pre-2024 Oracle awards (Innovation 2015/2016; SaaS Partner 2016/2019). The Oracle Business Impact Awards for EMEA and ECEMEA 2024 — confirmed in W1S1-003 and W1S1-006 — are more current and should be cited in any tender use of this file. The awards table in Section 11 references the approved W1S1-003 source.

---

---

# EXTRACTION DOCUMENTATION

> The sections below are internal extraction records. They do not form part of the executive summary content and must be removed before any tender use.

---

## Source Mapping Table

| Claim / Section | Primary Source | Supporting Source | Sourced / AI-Authored |
|---|---|---|---|
| Section 1 — Executive Overview narrative | MTN-2026 lines 47–55 (corrected) | W1S1-003 (partner tier); W1S1-007 (DBA claim, model) | Sourced — narrative adapted; prohibited wording corrected |
| Section 1 — Level 1 Partner claim | W1S1-003 (approved) | ORACLE_FACT_BASELINE.md Section 1 | Sourced |
| Section 1 — "One of the largest DBA teams" | W1S1-007 line 50 (approved) | ORACLE_FACT_BASELINE.md Section 9 | Sourced |
| Section 2.1 — Core DBA services table | MTN-2026 lines 100–106 | W1S1-007 lines 50–56 | Sourced |
| Section 2.2 — Advanced services table | MTN-2026 lines 108–113 | — | Sourced |
| Section 2.3 — Service management disciplines | MTN-2026 lines 115–121 | — | Sourced |
| Section 3.1 — Daily health check table | MTN-2026 lines 590–597 | — | Sourced |
| Section 3.2 — Account management | MTN-2026 line 589 | — | Sourced (condensed) |
| Section 3.3 — CMDB governance | MTN-2026 lines 629–657 | — | Sourced (summarised for exec summary) |
| Section 4.1 — Performance monitoring | MTN-2026 lines 579–599 (Q16) | — | Sourced (condensed) |
| Section 4.2 — Space management | MTN-2026 line 588 | — | Sourced |
| Section 4.3 — Monitoring architecture table | MTN-2026 lines 670–722 (Q20) | — | Sourced (3-layer framework extracted as table) |
| Section 5.1 — HA technology table | MTN-2026 lines 601–603 (Q17) | — | Sourced |
| Section 5.2 — Backup strategy | MTN-2026 lines 611–613 | — | Sourced |
| Section 5.3 — DR process steps | MTN-2026 lines 605–610 | — | Sourced |
| Section 6.1 — N-1 patching table | MTN-2026 lines 447–452 (Q9) | — | Sourced |
| Section 6.2 — Upgrade management | MTN-2026 lines 453–459 (Q10) | — | Sourced (condensed) |
| Section 6.3 — Version control | MTN-2026 lines 1030–1035 (Q27) | — | Sourced |
| Section 7.1 — Security compliance model | MTN-2026 lines 615–627 (Q18) | — | Sourced |
| Section 7.2 — Access control table | MTN-2026 lines 1053–1080 (Q28) | — | Sourced (selected controls extracted) |
| Section 7.3 — Security hardening | MTN-2026 lines 619–626 | — | Sourced |
| Section 7.4 — Regulatory alignment | MTN-2026 lines 615–627 (Q18); lines 435–445 (Q8) | — | **BU Lead confirmed 2026-06-11** — rewritten per BU Lead decision; POPIA framing changed to client-obligation-facing; AI-authored bridging removed |
| Section 8 — Oracle tool competency table | MTN-2026 lines 926–990 (Q26) | — | **Sourced — direct extraction** |
| Section 9.1 — Support structure table | MTN-2026 lines 840–872 (Q23) | — | Sourced (condensed) |
| Section 9.2 — ITIL alignment | MTN-2026 lines 435–445 (Q8) | — | Sourced (condensed) |
| Section 9.3 — CIM (4-stage, 3-pillar) | MTN-2026 lines 1377–1392 | W1S1-007 (CIM reference approved) | Sourced |
| Section 9.3 — Customer Success Manager | MTN-2026 line 541 | — | Sourced |
| Section 9.3 — Monthly Recurring Invoice Model | W1S1-007 lines 69–71 (approved) | MTN-2026 lines 1402–1406 | Sourced from approved W1S1-007 |
| Section 10.1 — Environment scale context | MTN-2026 lines 62–75 | — | Sourced (FR-G applied — no specific count) |
| Section 10.2 — DBA reference client table | MTN-2026 lines 155–174, 345–347, 926–990 | — | Sourced; DFA removed per FR-D |
| Section 10.3 — Telecom sector depth | MTN-2026 lines 224–275 | — | Sourced (AI-authored framing) |
| Section 11 — Differentiators table | MTN-2026 lines 145–149, 427–431, 1393–1401 | W1S1-003; W1S1-007 | Sourced + AI-authored table structure |
| Section 12 — Limitations and constraints | BU Lead decisions FR-D, FR-F, FR-G | — | AI-authored documentation |

---

## Assumptions Register

| ID | Assumption | Section | Impact if Wrong | Action Required |
|---|---|---|---|---|
| A-001 | All reference clients in tool competency table (Section 8) remain willing to be cited for Oracle DBA tool experience as at 2026 | Section 8 | Incorrect tool reference claim if client relationship ended or client has changed view | Confirm with account managers before first tender use |
| A-002 | MTN, Cell C, Virgin Mobile engagements in Section 10.2 are appropriate to cite as DBA reference evidence (not under NDA restriction) | Section 10 | Cannot cite if under NDA or if client has requested restriction | Confirm each with account manager |
| A-003 | ARM, SA Reserve Bank, and KPMG Africa are currently active engagements (per MTN-2026 line 347 — "Currently") | Section 10 | Overstates current delivery if any has ended | Confirm as at June 2026 with delivery team |
| A-004 | Oracle tool competency experience is current — all 8 tools have active resource skill coverage as at 2026 | Section 8 | Overstates tool capability if resources have changed | Confirm with DBA team lead |
| A-005 | **BU Lead confirmed 2026-06-11** — 24x7 support services available where contractually required. Wording updated in Section 1 and Section 9.1. | Section 9 | **Resolved** | Confirmed by Hein Blignaut |
| A-006 | **BU Lead confirmed 2026-06-11** — CIM (4-stage / 3-pillar) is standard across all managed service accounts. Retained without restriction. | Section 9 | **Resolved** | Confirmed by Hein Blignaut |
| A-007 | **BU Lead confirmed 2026-06-11** — CSM engagement model retained; "at no cost" removed per BU Lead decision. Replaced with Dedicated Customer Success Manager engagement model in Section 9.3 and Section 11. Commercial commitment risk eliminated. | Section 9, 11 | **Resolved** | Confirmed by Hein Blignaut |
| A-008 | POPIA regulatory alignment in Section 7.4 accurately describes APPSolve's approach | Section 7 | Risk of incorrect compliance claim | **BU Lead confirmed 2026-06-11** — Section 7.4 rewritten; POPIA framing changed to client-obligation-facing. Resolved. |

---

## Factual Risk Assessment

| ID | Risk | Section | Severity | Resolution |
|---|---|---|---|---|
| FR-001 | **Gold Partner claim** — MTN-2026 line 1307 contains "Gold Level partnership with Oracle" (company profile section) | — | CRITICAL | Resolved: company profile section excluded. W1S1-003 used for all partnership claims. No Gold references in this file. |
| FR-002 | **Consultant count** — MTN-2026 lines 1249 and 1373 contain "110 Senior Consultants" and "100 senior resources" | — | CRITICAL | Resolved: company profile section excluded. W1S1-007 and W1S1-001 "50+ Senior Consultants" not directly cited in this file (exec summary focuses on DBA team, not total headcount). |
| FR-003 | **DBA superlative claim** — MTN-2026 line 1313: "APPSolve has the largest number of locally based Oracle Applications DBAs" | Section 1, 11 | HIGH | Resolved: "one of the largest locally-based Oracle Applications DBA teams in South Africa" used throughout (W1S1-007 approved; ORACLE_FACT_BASELINE.md Section 9) |
| FR-004 | **DFA exclusion** — DFA excluded from all public-facing references per BU Lead FR-D | Section 10 | HIGH | **RESOLVED 2026-06-11** — Confirmed by Hein Blignaut. DFA removed from all tender-facing tables and sections. Reviewer note added in Section 10.2. Internal evidence only. |
| FR-005 | **Regulatory alignment (Section 7.4)** — POPIA and ITIL framing was AI-authored bridging | Section 7 | MEDIUM | **RESOLVED 2026-06-11** — Section 7.4 rewritten per BU Lead decision. POPIA framing changed to client-obligation-facing; AI-authored bridging removed; source attribution updated. |
| FR-006 | **Customer Success Manager universality** — MTN-2026 line 541 states CSM at no cost for MTN engagement specifically | Section 9, 11 | MEDIUM | **RESOLVED 2026-06-11** — "At no cost" removed per BU Lead decision. Replaced with "Dedicated Customer Success Manager engagement model". Commercial commitment risk eliminated. |
| FR-007 | **24x7 universality** — support structure described mirrors the MTN 2026 tender model; may not be the standard for all accounts | Section 9 | MEDIUM | **RESOLVED 2026-06-11** — 24x7 wording updated to "available where contractually required" per BU Lead decision. Applied in Section 1 and Section 9.1. |
| FR-008 | **Currently active clients** — ARM, SA Reserve Bank, KPMG Africa described as "currently active" per April 2026 proposal | Section 10 | LOW | Confirm as at June 2026. Low risk given recency of source. |
| FR-009 | **HIST-002 superseded** — no content extracted from HIST-002; document may be archived | — | LOW | Confirmed: HIST-002 has zero unique content beyond what MTN-2026 provides more fully. |
| FR-010 | **"19 years" Hein / "22 years" APPSolve / geography claims** | — | CRITICAL | Resolved: company profile section excluded entirely. No outdated stats in this file. |

---

## W2S1-004 Reuse Map

The following content blocks from MTN-2026 are identified for W2S1-004 Oracle Managed Services Support Model. They are NOT included in W2S1-003 to avoid duplication.

| Content block | MTN-2026 Lines | W2S1-004 Section (planned) | Notes |
|---|---|---|---|
| ITIL framework full detail (Q8) — Incident B-55, Problem B-137, Event B-151, Change B-163 | 435–445 | Managed Services Framework | Summarised in W2S1-003 Section 9.2; full detail reserved |
| SLA meeting cadence table (daily/weekly/monthly/quarterly) | 500–517 | Service Governance Model | Not included in exec summary |
| SLA and operational reporting table (5 report types) | 519–537 | Service Reporting | Not included in exec summary |
| CSI closed-loop model (Measure/Analyse/Improve/Review) with CSI register | 484–497 | Continuous Improvement | Headline only in W2S1-003 Section 9.3 |
| Capacity management full approach (Q14) | 543–571 | Capacity and Demand Management | Not included in exec summary |
| Demand management approach | 549–553 | Capacity and Demand Management | Not included |
| Rapid provisioning model | 554–571 | Environment Provisioning | Not included |
| 24x7 support structure full detail with table (Q23) | 832–872 | 24x7 Support Model | Summarised in W2S1-003 Section 9.1; full structure reserved |
| Segregation of duties full framework (Q28) | 1040–1167 | Security and Governance Controls | Not included in exec summary |
| CMDB governance full model (Q19) | 629–668 | Configuration Management | Summarised in W2S1-003 Section 3.3 |
| ETL / migration factory detail (Q5, Q6, Q11) | 352–480 | Migration and ETL Capability | Not included in exec summary |
| Deployment framework — patch, ETL, version control detail (Q27) | 993–1037 | Release Management | Not included in exec summary |
| Backup SOP structure — TOC reference (Q21) | 725–749 | Documentation Standards | Not included |
| Monthly report TOC reference (Q22) | 784–828 | Reporting Standards | Not included |
| Performance management full detail (Q16) | 579–599 | Performance Engineering | Executive-summary version in W2S1-003 Section 4; full detail reserved |
| Monitoring domains full detail (Q20) — space, logs, indexing, fragmentation, partitioning | 670–723 | Monitoring Framework | 3-layer table in W2S1-003 Section 4.3; full domain coverage reserved |

---

## Extraction Quality Assessment

| Dimension | Rating | Notes |
|---|---|---|
| DBA Service Scope Coverage | **STRONG** | All core and advanced DBA service domains covered with sourced content from MTN-2026 |
| Performance Monitoring Content | **GOOD** | Executive-level detail appropriate for summary; full detail reserved for W2S1-004 |
| Backup / Recovery / DR Content | **GOOD** | Technology stack, process steps, and DR framework all sourced |
| Patching / Lifecycle Management | **GOOD** | N-1 strategy, patch lifecycle table, upgrade governance all sourced |
| Security and Access Governance | **STRONG** | Sections 7.1–7.3 fully sourced; Section 7.4 rewritten per BU Lead decision (FR-005 resolved 2026-06-11) |
| Oracle Tool Competency | **STRONG** | Direct extraction from Q26 tool table; 8 tools with named reference clients; no DFA |
| 24x7 Support Model | **GOOD** | Structure and roles sourced; full cadence detail reserved for W2S1-004 |
| Reference Client Evidence | **GOOD** | 8 Oracle DBA managed services clients (DFA excluded); 3 telecom operators; currently active clients confirmed |
| Prohibited Wording Compliance | **FULL** | All 9 MTN-2026 profile violations excluded. Company profile not extracted. Zero prohibited phrases in this file. |
| Source Attribution | **FULL** | All content attributed to source document line numbers where available |
| W2S1-004 Reuse Map | **COMPLETE** | 16 content blocks identified and pre-assigned |

**Overall quality: STRONG — Approved 2026-06-11**

---

## Promotion Record: Review_Required → Approved

**Status: APPROVED — 2026-06-11 | Approved by: Hein Blignaut**

**BU Lead decisions applied:**

| Decision | Action taken | Date |
|---|---|---|
| FR-D — DFA exclusion | DFA removed from all tender-facing tables and sections throughout | 2026-06-11 |
| FR-F — Capacity wording | Quantified claim removed; BU Lead approved wording applied in Section 11 | 2026-06-11 |
| FR-G — Scale wording | BU Lead approved wording applied in Section 10.1 | 2026-06-11 |
| FR-005 — Section 7.4 | Rewritten: POPIA framing changed to client-obligation-facing; AI-authored bridging removed; source attribution updated | 2026-06-11 |
| A-005 — 24x7 universality | Wording updated to "24x7 support services available where contractually required" in Section 1 and Section 9.1 | 2026-06-11 |
| A-006 — CIM universality | CIM confirmed as standard across all managed service accounts; retained without restriction | 2026-06-11 |
| A-007 — CSM commercial claim | "At no cost" removed throughout; "Dedicated Customer Success Manager engagement model" applied in Section 9.3 and Section 11 | 2026-06-11 |

**Pre-tender use confirmation required (not blocking for Approved status):**

| Item | Section | Action before tender use |
|---|---|---|
| A-001 / A-002 — reference client citability | Section 8, 10 | Confirm with account managers that all named clients are willing to be cited as of 2026 |
| A-003 — currently active clients | Section 10 | Confirm ARM, SA Reserve Bank, KPMG Africa still active as at June 2026 |

**File location:** `07_Approved_Content/Approved/Oracle/W2S1-003-ORA-DBAExecutiveSummary.md`

---

*Extraction: 2026-06-11 — Wave 2 Session 1*
*Extracted by: AI (Claude Sonnet 4.6)*
*Primary source: APPSolve_MTN_DBA_RFP_RFX-1000004246_v1.0.docx — 05 April 2026 (1,495 lines)*
*Secondary source: HIST-002 MTN 2014 Executive Summary (95 lines — superseded; zero content extracted)*
*Approved content sources: W1S1-003 Oracle Partnership; W1S1-007 Delivery Model*
*Governance: ORACLE_FACT_BASELINE.md; W2S1-003_READINESS_REPORT.md*
*Approved: 2026-06-11 by Hein Blignaut. Physical location: 07_Approved_Content/Approved/Oracle/*
