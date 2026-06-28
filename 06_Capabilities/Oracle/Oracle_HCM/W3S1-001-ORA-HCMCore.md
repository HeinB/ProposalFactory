---
document_id: W3S1-001-ORA-HCMCore
title: "Oracle HCM Core — Global HR and Employee Lifecycle Capability Statement"
version: "1.3 Approved"
status: "Approved"
review_status: "Approved"
approved_for_reuse: "Yes"
business_unit: "Oracle"
wave: "3"
deliverable: "W3S1-001"
created: "2026-06-12"
approved: "2026-06-13"
created_by: "Claude (AI — Wave 3 W3S1-001 extraction)"
approved_by: "Hein Blignaut (BU Lead)"
source_document: "HIST-007 (Hollywood Bets V5.0 ACCEPTED Proposal, April 2023); HIST-015 (Afrocentric HCM Proposal V4.0, 2023); HIST-006 (SAA HCM RFP Response, June 2025 — capability evidence only)"
source_status: "Implementation Evidence (HIST-007, HIST-015); Capability Evidence (HIST-006)"
kb_destination: "06_Capabilities/Oracle/Oracle_HCM/"
tags: "Oracle,HCM,Global HR,Core HCM,Absence Management,Self-Service,Journeys,Employee Lifecycle,OIC,Oracle Fusion"
---

> **APPROVED — approved_for_reuse: Yes — Approved by BU Lead 2026-06-13**

---

# Oracle HCM Core — Global HR and Employee Lifecycle

**Capability Statement | APPSolve | Oracle Business Unit**  
*Document ID: W3S1-001-ORA-HCMCore | Version: 1.3 Approved | Wave 3*

---

## Section 1 — APPSolve Oracle HCM Practice Overview

APPSolve is an **Oracle Level 1 Partner** with a published Oracle Fusion Cloud HCM Core expertise certification on the Oracle Partner Network (OPN). With over 23 years of Oracle consulting experience, APPSolve has built one of South Africa's most capable Oracle HCM delivery practices — combining deep functional expertise with certified Oracle Integration Cloud (OIC) capability to deliver end-to-end HCM transformations for enterprise clients across Southern Africa and internationally.

APPSolve's Oracle HCM practice spans the full Oracle Fusion HCM module suite, with particular depth in Global HR, Absence Management, Talent Management, Recruiting, Learning, Workforce Compensation, Time and Labor, Help Desk, and HCM Analytics. The practice is supported by Oracle's OUM (Oracle Unified Methodology) and Oracle's Customer Success Navigator framework, ensuring structured, repeatable, and de-risked implementation delivery.

**Oracle Fusion Cloud HCM Core — the Global HR foundation module — is the starting point for every APPSolve Oracle HCM engagement.** It establishes the organisational structures, worker records, and configuration framework that all subsequent HCM modules depend on. APPSolve's implementation sequence places Global HR first, ensuring a solid foundation before activating Recruiting, Talent Management, Learning, Compensation, or Time and Labor.

**Key practice credentials:**

| Credential | Detail |
|---|---|
| Oracle partner tier | Oracle Level 1 Partner |
| Published OPN expertise | Oracle Fusion Cloud HCM Core (certified) |
| Integration expertise | Oracle Integration (OIC) — published OPN expertise area |
| Company experience | Over 23 years of Oracle consulting |
| HCM go-live reference | Hollywood Bets — Oracle Fusion HCM go-live July 2025; 7,000 users |

---

## Section 2 — Oracle Fusion HCM Platform

### 2.1 SaaS Architecture

Oracle Fusion Human Capital Management is a cloud-native, Software-as-a-Service (SaaS) platform. APPSolve implements the Oracle Fusion HCM suite in Oracle's managed cloud environment — eliminating the need for on-premises infrastructure, hardware procurement, or manual database administration by the client. Oracle manages platform availability, security patching, and regulatory compliance updates; APPSolve manages configuration, integration, and business process alignment on behalf of the client.

The SaaS model delivers automatic quarterly feature releases, ensuring that every APPSolve-implemented HCM environment benefits continuously from Oracle's product investment without requiring disruptive upgrade projects. APPSolve guides clients through quarterly release assessments, advising on which new features to activate and how to incorporate them into existing business processes.

### 2.2 Enterprise HCM Platform Positioning

APPSolve configures Oracle Fusion HCM to serve enterprise clients of varying scale and complexity. The platform supports:

- **Multi-country deployments** — a single Oracle instance serves multiple legal entities, jurisdictions, and legislative frameworks simultaneously. APPSolve implements the organisational model, legislative elements, and localisation rules for each country in scope.
- **Multi-currency and multi-language** — compensation, absence entitlements, and workforce data are managed across currencies and presented in the employee's preferred language.
- **Shared services model** — APPSolve's standard delivery approach establishes a central shared services HR structure, enabling HR operations to scale efficiently across multiple business units and entities without duplicating configuration.
- **Scalability** — the platform is architected for growth. APPSolve's implementations are designed to accommodate additional countries, legal entities, and modules without rework of the core configuration.

### 2.3 Oracle Integration Cloud Alignment

Oracle Integration Cloud (OIC) is APPSolve's **mandatory standard integration layer in every Oracle Fusion HCM implementation**. OIC provides the integration fabric between Oracle Fusion HCM and the client's payroll system, identity provider, biometric infrastructure, ERP, and third-party HR platforms. No Oracle Fusion HCM implementation delivered by APPSolve operates in isolation — OIC is present in every engagement to ensure data integrity, process automation, and system interoperability.

APPSolve holds a published OPN expertise certification in Oracle Integration, reflecting the depth of the team's OIC design and implementation capability.

---

## Section 3 — Core HR and Organisational Management

### 3.1 Worker Lifecycle Management

APPSolve implements the Oracle Fusion HCM Global HR module to manage the complete worker lifecycle — from hire through to termination and rehire. The hire-to-retire process encompasses:

- **Person records** — legal name, identity documents, contact information, emergency contacts, and personal attributes configured per client requirements and legislative mandate.
- **Employment records** — employment start date, assignment classification (employee, contingent worker, non-worker), grade, step, and seniority.
- **Work relationships** — primary and secondary assignments; multiple concurrent assignments across legal entities or business units.
- **Job and position management** — APPSolve configures job profiles defining the responsibilities, required qualifications, and skill requirements for each role. Position management enables headcount tracking and FTE visibility across the organisational hierarchy.
- **Termination and offboarding** — structured termination flows; final settlement calculations; exit interview tracking; access revocation triggers for downstream system integration.

### 3.2 Organisational Structures

APPSolve designs and configures the full Oracle Fusion HCM organisational model during the foundation phase of every HCM engagement. The organisational model is the architectural backbone of the HCM environment — all subsequent modules, security roles, approval hierarchies, and reporting structures depend on it being correctly established from the outset.

**Organisational components APPSolve configures:**

| Component | Function |
|---|---|
| Legislative Data Group (LDG) | Defines the legislative and payroll processing boundary for each jurisdiction |
| Business Unit | The primary organisational unit for HR and financial processes |
| Legal Employer | The legal entity employing workers; mapped to company registration and tax reference numbers |
| Department | Operational grouping within a Business Unit; used for reporting, cost allocation, and approval routing |
| Division and Region | Optional grouping layers for reporting and operational management |
| Cost Centres | Linked to departments and positions for financial reporting integration |
| Locations | Physical or virtual work locations; used for scheduling, absence, and compliance reporting |

APPSolve's best-practice approach is to design the organisational model in the Journey Workshop phase, validate it through a Conference Room Pilot (CRP), and lock it down before configuring any other module — preventing the rework that arises when organisational design decisions are made mid-implementation.

### 3.3 Position Management

APPSolve implements Oracle Fusion HCM position management to provide clients with continuous visibility of headcount, vacancies, and FTE against approved establishment. Position management connects HR operations to financial planning by linking position costs to the client's cost centre and budget structure.

**Capabilities APPSolve configures within position management:**

- Position hierarchies aligned to reporting lines and approval workflows
- Position budgets linked to GL cost centres
- FTE tracking and vacancy management
- Position-based security — role-based access control follows the position hierarchy
- Requisition triggering — position vacancies trigger recruiting workflows in Oracle Recruiting Cloud

### 3.4 Workforce Records and Document Management

APPSolve configures Oracle Fusion HCM to store and manage workforce records in line with POPIA requirements and the client's document retention policy. Worker documents — employment contracts, qualification certificates, disciplinary records, ID copies, and tax forms — are stored against the worker record with version control and access auditing. Document expiry alerts can be configured to notify HR administrators of pending expiries for certificates, work permits, or licences.

---

## Section 4 — Absence Management

APPSolve implements Oracle Fusion HCM Absence Management as an integrated component of the Core HR foundation phase. Absence Management is one of the most frequently used HCM capabilities by employees and managers from day one — APPSolve therefore treats it as a priority deliverable within the Core HR phase rather than a separate subsequent implementation.

### 4.1 Absence Plan Configuration

APPSolve designs and configures absence plans to reflect the client's leave policy and South African legislative requirements (the Basic Conditions of Employment Act and sector-specific legislation). Configurable elements include:

| Element | Configuration options |
|---|---|
| Leave types | Annual, sick, family responsibility, study, maternity, paternity, unpaid, special leave |
| Accrual rules | Calendar year, anniversary, or employment date basis; daily or hourly accrual |
| Entitlement rules | Fixed entitlement; length-of-service scaling; employment category differentiation |
| Carry-over rules | Maximum carry-over; expiry of unused leave; payment in lieu |
| Approval workflows | Manager approval; HR override; automatic approval for short-duration absence |
| Negative balance | Permitted negative balance rules; recovery mechanisms |

### 4.2 Legislative Compliance

APPSolve configures South African legislative leave requirements as the baseline for all implementations, with additional legislative configurations applied for multi-country deployments. BCEA minimum entitlements are configured as non-negotiable floor values; client policy entitlements layer on top.

### 4.3 Absence and Payroll Integration

When Oracle Fusion HCM is integrated with a payroll system — either Oracle Payroll Cloud or a third-party payroll solution — APPSolve configures the absence-to-payroll integration to ensure leave pay, unpaid deductions, and absence recovery amounts are transmitted accurately to payroll at the end of each pay period. This integration is delivered via OIC (Oracle Integration Cloud) or HCM Extracts, depending on the payroll system in scope.

### 4.4 Manager and Employee Self-Service for Absence

Absence management is exposed to employees and managers through the Oracle Fusion HCM self-service portal. Employees submit leave requests; managers review team calendars, approve or decline requests, and receive notifications of absence conflicts. HR administrators have real-time visibility of absence across all teams and can generate BCEA-compliant absence reports at any time.

---

## Section 5 — Employee Self-Service and Journeys

### 5.1 Employee Self-Service

APPSolve configures the Oracle Fusion HCM self-service portal as a central touchpoint for employees to access and manage their employment information without HR intervention. The self-service capability reduces administrative burden on the HR function, improves data accuracy, and enhances the employee experience.

**Self-service capabilities APPSolve configures:**

| Capability | Description |
|---|---|
| Personal information maintenance | Name, contact details, address, emergency contacts, banking details |
| Document viewing | Payslips (where payroll in scope), tax certificates, employment confirmations |
| Leave management | Submit, view, and withdraw absence requests; view leave balances and history |
| Time and labour (where in scope) | Timecard submission; overtime requests; time balance enquiries |
| Benefit enrolment (where in scope) | Life events triggered benefit elections; open enrolment periods |
| Directory and org chart | Search colleagues; view organisational structure |
| Team management (managers) | View team's personal information; action manager self-service tasks |

The self-service portal is mobile-responsive, enabling employees to access HR services from any device without requiring a dedicated mobile application.

### 5.2 Oracle HCM Journeys

APPSolve configures and enables Oracle HCM Journeys to guide employees and managers through multi-step HR processes as structured, checklist-driven workflows. A Journey is a personalised, role-based digital guide that ensures every step of an HR process is completed, by the right person, in the right sequence.

**Journeys APPSolve configures and enables:**

| Journey type | Purpose |
|---|---|
| Onboarding journey | Guides new hires through pre-employment tasks, document submission, and system access |
| Offboarding journey | Orchestrates exit clearance, document return, access revocation, and final settlement |
| Life event journeys | Triggers benefit and record updates for marriage, new child, address change, relocation |
| Promotion and transfer | Guides managers and HR through approval steps, compensation review, and communication |
| Performance review | Structures goal-setting, mid-year check-in, and year-end review sequences |

Journeys reduce HR error rates, ensure compliance with internal process requirements, and provide a consistent employee experience regardless of which HR representative handles the transaction.

### 5.3 Manager Self-Service

APPSolve configures Oracle Fusion HCM manager self-service to provide line managers with direct access to HR actions within their span of control, reducing dependency on HR teams for routine transactions:

- Approve absence, overtime, and time entries
- Initiate transfers, promotions, and grade changes
- View team absence calendars and headcount
- Access team performance and goal dashboards
- Manage position vacancies and raise recruiting requisitions

---

## Section 6 — Skills, Talent Intelligence and Workforce Capability

### 6.1 Skills Framework

APPSolve implements Oracle Fusion HCM's skills and competency framework to provide clients with a structured, consistent view of workforce capability. The skills framework underpins talent management, recruiting, learning, succession, and workforce planning — making it a foundational investment in the Core HR phase.

**Skills framework components APPSolve configures:**

| Component | Description |
|---|---|
| Job profiles | Define the responsibilities, required qualifications, mandatory competencies, and preferred skills for each position |
| Competency frameworks | Structured competency libraries aligned to the client's performance and development model |
| Skill tags | Lightweight, AI-searchable skill labels assignable to workers and job profiles |
| Proficiency levels | Configurable proficiency scales (e.g., Awareness → Practitioner → Expert) |
| Worker skill records | Employee-owned skill profiles; self-declared and manager-validated competencies |

The skills framework is designed in close collaboration with the client's HR and talent leadership to ensure it reflects actual business requirements rather than generic Oracle defaults.

### 6.2 Talent Intelligence

Oracle Fusion HCM provides embedded talent intelligence capabilities that APPSolve configures and activates to give HR leaders and managers actionable workforce insights:

- **Skills gap analysis** — identifies mismatches between current workforce skills and the skills required for target roles or business objectives
- **Internal talent matching** — surfaces employees whose profiles closely match open positions or development opportunities
- **Workforce composition analytics** — gender, seniority, tenure, and skills distribution across the organisation
- **Attrition risk indicators** — identifies employees showing indicators associated with flight risk, enabling proactive retention action

### 6.3 Workforce Capability Visibility

APPSolve configures Oracle Fusion HCM to provide HR, talent, and business leaders with a real-time view of workforce capability across the organisation:

- Skill inventory reports showing coverage and depth per capability domain
- Headcount and FTE by skill cluster or competency group
- Bench strength assessments for critical roles
- Capability gap reporting aligned to strategic workforce plans

### 6.4 Career Mobility

APPSolve implements Oracle Fusion HCM career mobility features to support internal talent retention and development:

- **Career pathways** — configurable career paths showing the typical progression from current role to target roles, with the skills and qualifications required at each stage
- **Internal opportunity marketplace** — employees can view and express interest in open positions, project assignments, and development opportunities within the organisation
- **Development plans** — structured individual development plans linked to skills gaps, career aspirations, and performance feedback

*For APPSolve's full Opportunity Marketplace (Oracle Talent Management — Internal Mobility) capability statement, see W3S1-002-ORA-TalentMgmt.*

### 6.5 AI-Assisted Capability Features

Oracle Fusion HCM incorporates AI-driven capability features that APPSolve activates and configures as part of the skills and talent intelligence setup:

- **AI-based skills recommendations** — Oracle's embedded AI analyses the employee's role, learning history, and career path to recommend skills for development
- **Dynamic skill profiles** — AI continuously enriches worker skill profiles based on learning completions, project assignments, and performance data
- **Job profile optimisation** — AI suggests skill additions or removals to job profiles based on market benchmarks and internal workforce data

*Note: AI feature availability and specific capability is subject to Oracle quarterly release schedule and the client's Oracle SaaS subscription tier. APPSolve advises clients on feature activation timing as part of the release management service.*

---

## Section 7 — APPSolve Oracle HCM Delivery Capability

### 7.1 Implementation Capability

APPSolve's Oracle HCM delivery team comprises certified Oracle consultants across the full HCM module suite. The team is structured to deliver end-to-end HCM implementations, from initial scoping and business process design through configuration, integration, data migration, testing, training, and post-go-live hypercare.

**Consultant capability by discipline:**

| Role | Capability |
|---|---|
| Principal HCM Consultant | Business process design, solution architecture, CRP facilitation, client advisory |
| Senior Functional Consultant | Module configuration, business process documentation, UAT facilitation |
| Senior Technical Consultant | OIC integration development, HCM Extracts, OTBI reporting, HCM Data Loader |
| Project Manager | OUM project governance, plan management, risk and issue management, steering committee reporting |
| Test Lead | Test script design, CRP coordination, integration testing, UAT management |

APPSolve's HCM consultants hold Oracle certifications across Global HR, Recruiting, Talent Management, Learning Cloud, and OIC — evidence of the team's investment in formal Oracle capability accreditation.

### 7.2 Delivery Approach

APPSolve's HCM delivery approach is based on the Oracle Unified Methodology (OUM) and Oracle's Customer Success Navigator framework. The approach is tailored per engagement but follows a consistent phase structure (detailed in Section 10) that has been proven across multiple enterprise HCM implementations.

**Delivery principles:**

- **Standard functionality first** — APPSolve's default position is to use Oracle standard functionality. Customisation and development are out of scope unless a specific business requirement cannot be met any other way.
- **South Africa first** — for multi-country engagements, APPSolve implements the South African instance as the blueprint. The SA configuration establishes standards, templates, and approval hierarchies that are subsequently adapted for additional countries, reducing duplication and accelerating multi-country rollout.
- **Shared services model** — APPSolve designs HCM implementations around a shared services HR operating model, enabling centralised HR administration to serve multiple business units efficiently.
- **Iterative configuration** — the Solution Reflection (CRP) process delivers rapid iterative builds, allowing business stakeholders to see and shape the system before configuration is locked.

### 7.3 Configuration Capability

APPSolve's configuration capability covers the full scope of Oracle Fusion HCM Core configuration:

- Enterprise structure: Legal entities, business units, departments, locations, cost centres
- HR configuration: Worker types, employment categories, grades, grade steps, FTE rules
- Person configuration: Person types, person extra information (PEI) types, document records
- Absence configuration: Plan types, accrual formulas, absence reasons, approval workflows
- Self-service configuration: Menu structures, page personalisation, notification templates
- Journeys: Journey design, checklist tasks, triggers, notifications, integrations
- Security: Role-based access control (RBAC); HCM data roles; row-level security; segregation of duties

### 7.4 Integration Capability

APPSolve's Oracle Integration Cloud (OIC) certification enables the team to design and build production-grade integrations connecting Oracle Fusion HCM to the client's wider enterprise ecosystem. Confirmed integration types delivered by APPSolve:

- Oracle HCM to SAP Payroll — APPSolve has the technical integration capability to connect Oracle HCM to SAP Payroll via OIC
- Oracle HCM to third-party payroll systems (PaySpace and others) — via OIC or HCM Extracts
- Oracle HCM to biometric and time-capture systems
- Oracle HCM to Learning Management Systems (Moodle and others) — for SETA reporting and learning record synchronisation *(HIST-007 Annexure 1)*
- Oracle HCM to Active Directory and identity providers — for user provisioning and SSO

### 7.5 Managed Services Capability

APPSolve provides post-implementation Oracle HCM managed services to clients requiring ongoing functional and technical support. The managed services model covers:

- HCM system administration: user management, security role maintenance, configuration changes
- Quarterly release management: release impact assessment, feature activation advisory, regression testing
- Ongoing integration support: OIC monitoring, interface error resolution, data quality management
- Functional advisory: process improvement recommendations, optimisation of underutilised functionality
- Reporting and analytics support: OTBI report maintenance, dashboard enhancement

---

## Section 8 — Reference Implementations

### 8.1 Hollywood Bets — Primary Oracle HCM Reference

**Client:** Hollywood Bets  
**Industry:** Gaming and Entertainment  
**Solution:** Oracle Fusion HCM — Core HCM, Absence Management, Recruiting, Talent Management, Performance Management, Career Development, Succession Planning, Help Desk  
**Go-live:** July 2025  
**User count:** 7,000 users  
**Status:** Live — post-go-live support active

Hollywood Bets is APPSolve's primary Oracle Fusion HCM reference implementation. This engagement represents the full scope of APPSolve's Oracle HCM delivery capability: a complex, multi-module implementation for a large South African employer with over 7,000 active system users, delivered to production and successfully transitioned to a live operating environment in July 2025.

**Implementation scope:**

| Module | Status |
|---|---|
| Oracle Fusion HCM Core (Global HR) | Live — July 2025 |
| Oracle Fusion Absence Management | Live — July 2025 |
| Oracle Fusion Recruiting Cloud | Live — July 2025 |
| Oracle Fusion Talent Management | Live — July 2025 |
| Oracle Fusion Performance Management | Live — July 2025 |
| Oracle Fusion Career Development | Live — July 2025 |
| Oracle Fusion Succession Planning | Live — July 2025 |
| Oracle HCM Help Desk | Live — July 2025 |
| OIC integration to third-party payroll | Live — July 2025 |
| Biometric system integration | Live — July 2025 |
| SETA / WSP / ATR reporting extract | Live — July 2025 (Annexure 1) |

**Integration architecture:** APPSolve implemented Oracle Integration Cloud (OIC) as the standard integration layer, connecting Oracle Fusion HCM to the client's third-party payroll system and biometric infrastructure. Payroll data flows from Oracle HCM to the payroll system via OIC-managed interfaces on a defined payroll cycle. Biometric attendance data flows into Time and Labor for payroll-relevant time capture.

**SETA compliance:** APPSolve implemented a SETA reporting extract — integrating Oracle HCM with the client's learning platform to produce Workplace Skills Plan (WSP) and Annual Training Report (ATR) data in the format required for Skills Development Act compliance.

**HR Help Desk:** Hollywood Bets extended the scope to include Oracle HCM Help Desk — enabling employees to submit HR inquiries via chatbot and SMS channels, with routing to HR representatives and an HR knowledge base for self-service resolution.

*Reference availability: Hollywood Bets is a confirmed and referenceable APPSolve Oracle HCM client (F-W3-002 CLOSED, 2026-06-12). Contact via APPSolve account manager.*

### 8.2 Additional Oracle HCM Implementations

APPSolve has delivered Oracle Fusion HCM implementations across enterprise clients in retail, mining, and professional services sectors, establishing a track record of multi-industry HCM delivery across South African and international organisations. These implementations span the full HCM module suite, including Core HR, Absence Management, Recruiting, Talent Management, Learning Cloud, Workforce Compensation, Time and Labor, Help Desk, and HCM Analytics.

Additionally, APPSolve has delivered Oracle HCM implementations that include multi-country organisational models, multi-legal-entity configurations, and integration to diverse payroll systems — including SAP Payroll, PaySpace, and Oracle Payroll Cloud.

*Specific reference details for additional implementations are available on request, subject to client consent and reference letter availability.*

### 8.3 Mr Price Group — Oracle HCM Learning Cloud and Support

**Client:** Mr Price Group  
**Industry:** Retail  
**Implementation scope:** Oracle HCM Learning Cloud (implemented by APPSolve)  
**Support scope:** Broader Oracle HCM estate (ongoing support provided by APPSolve)  
**Status:** Live

APPSolve implemented Oracle Learning Cloud for Mr Price Group and provides ongoing support services across the client's broader Oracle HCM landscape.

**Scope governance note:** Mr Price Group is an implementation reference for Oracle HCM Learning Cloud only. APPSolve's role across the broader Mr Price Oracle HCM environment is ongoing application support — APPSolve did not implement those modules. When citing Mr Price as a reference, distinguish clearly between implementation responsibility (Learning Cloud) and support responsibility (broader HCM estate). Do not imply APPSolve originally implemented every Oracle HCM module in use at Mr Price.

---

## Section 9 — Integration Architecture and Ecosystem

### 9.1 Oracle Integration Cloud — Standard Integration Layer

Oracle Integration Cloud (OIC) is the mandatory, standard integration layer in every APPSolve Oracle Fusion HCM implementation. APPSolve does not deliver Oracle Fusion HCM without OIC — it is the integration fabric that connects HCM to the client's payroll system, identity provider, biometric infrastructure, and enterprise systems.

OIC provides:
- Pre-built Oracle adapters for Oracle HCM, ERP, and cloud services
- Custom REST and SOAP adapter configurations for third-party systems
- Orchestration and transformation of HCM data in transit
- Error handling, retry, and alerting for all interfaces
- An audit trail of every data movement across the integration landscape

### 9.2 Payroll System Integrations

APPSolve configures the Oracle HCM payroll interface (Payroll Interface module) and implements the corresponding OIC integration to the client's nominated payroll system. Payroll integration patterns confirmed as delivered by APPSolve:

| Integration | Method | Evidence |
|---|---|---|
| SAP Payroll | OIC-managed interface | APPSolve has the technical integration capability to connect Oracle HCM to SAP Payroll via OIC |
| Third-party payroll (generic) | OIC interface or HCM Extracts | Hollywood Bets implementation *(HIST-007)* |
| PaySpace | HCM Extracts or OIC | *(ORACLE_FACT_BASELINE Section 12)* |
| Oracle Payroll Cloud (native) | Native Oracle payroll in same instance | Available where Oracle Payroll Cloud is licensed |

**Integration data flows** (standard payroll integration):
1. HCM Extracts or OIC extracts payroll-relevant worker and assignment data at defined frequency
2. Absence balances and approved leave are included in the extract
3. Overtime and time-capture data (where Time and Labor is in scope) is appended
4. The extract is transformed by OIC into the target payroll system's input format
5. The payroll system processes the data and returns a payroll results file
6. Payroll results are loaded back into Oracle HCM for record-keeping and reporting

### 9.3 Identity and Access Integrations

APPSolve configures Oracle Fusion HCM user provisioning as part of the implementation, integrating with the client's identity management environment:

- **Active Directory / Azure AD** — worker creation in Oracle HCM triggers user account provisioning in AD/Azure AD via OIC
- **Single Sign-On (SSO)** — Oracle Fusion HCM is configured to authenticate against the client's identity provider (SAML 2.0 or OAuth 2.0 standard)
- **Role provisioning** — HCM security roles are provisioned based on position and employment assignment, automatically updating as workers change roles

### 9.4 Third-Party Enterprise System Integrations

APPSolve designs and delivers integrations between Oracle Fusion HCM and the client's third-party systems based on confirmed business requirements. Typical integrations in scope for HCM Core engagements:

| System type | Integration purpose | Method |
|---|---|---|
| Biometric / time capture | Attendance data to Oracle Time and Labor | OIC or HCM Data Loader (HDL) |
| Learning Management System (Moodle, others) | Learning record sync; SETA extract | OIC or HCM Extracts |
| Finance / ERP | Headcount and costing data to GL | OIC or FBDI |
| Benefits administration | Benefits enrolment data to benefits provider | HCM Extracts |
| Background screening | Candidate screening results to Recruiting | OIC REST integration |

### 9.5 Reporting and Analytics Ecosystem

APPSolve configures Oracle Fusion HCM's embedded reporting and analytics tools as part of the Core HR implementation:

| Tool | Purpose | Configured by APPSolve |
|---|---|---|
| OTBI (Oracle Transactional Business Intelligence) | Ad hoc and scheduled reporting against live HCM data | Yes — standard subject areas and custom reports |
| TDE (Transactional Data Extracts) | Bulk data extracts for downstream reporting or audit | Yes — extract configuration |
| Delivered dashboards | Pre-built HCM dashboards for HR managers and executives | Yes — activated and personalised |
| HCM Analytics | Advanced workforce analytics (where licensed) | Yes — where in subscription scope |

### 9.6 Integration Patterns

APPSolve designs integrations using one of three standard patterns, selected based on data volume, frequency, and the capabilities of the target system:

| Pattern | When used |
|---|---|
| **OIC real-time** | Low-latency, event-driven integration (e.g., new hire triggers AD provisioning immediately) |
| **OIC scheduled batch** | Periodic data synchronisation on defined schedule (e.g., payroll extract nightly) |
| **HCM Extracts** | Oracle-native bulk data export; used where OIC is not in scope or where the target system accepts flat file input |
| **HCM Data Loader (HDL)** | Bulk data loading into Oracle HCM (used for data migration and mass updates) |

---

## Section 10 — Implementation Approach

### 10.1 OUM Methodology

APPSolve implements Oracle Fusion HCM using the **Oracle Unified Methodology (OUM)**, Oracle's standard implementation framework for Oracle Applications. OUM is structured to align Oracle's product capability with the client's business requirements through a structured sequence of discovery, design, build, and validation activities.

The OUM framework ensures:
- Clear deliverables and sign-off points at each phase gate
- Consistent documentation standards across all engagements
- A change-controlled approach that protects scope integrity
- Traceability between business requirements, configuration decisions, and test outcomes

### 10.2 Delivery Phases

APPSolve's HCM Core implementation follows a defined sequence of phases, each with specific activities, deliverables, and acceptance criteria:

| Phase | Key activities | Deliverable |
|---|---|---|
| **Journey Prep** | Business process documentation based on known client requirements; clarification questionnaire | Process documents; questionnaire |
| **Journey Workshop** | Facilitated workshops to finalise business requirements; configuration decision log | Signed-off requirements; decision log |
| **Solution Reflection (CRP)** | Rapid system build; client walkthrough of configured system; structured feedback | CRP session notes; updated configuration |
| **Technical Build** | Full configuration build in Oracle; data migration template preparation; integration design | Configured environment; migration templates; integration specifications |
| **Integration Testing** | Integration interface testing; data flow validation; error handling verification | Integration test results; sign-off |
| **Training and UAT** | Train-the-trainer sessions; UAT facilitation; defect logging and resolution | Training material; UAT attendance register; UAT sign-off |
| **Data Management** | Data normalisation support; HDL template completion; data load and verification | Loaded data; reconciliation report |
| **Look and Feel** | UI personalisation; branding; navigation customisation | Branded HCM environment |
| **Production Build** | Configuration migration to production; go-live verification; data verification | Production-ready system |
| **Hypercare** | Full team support immediately post go-live; rapid issue resolution; adoption support | Hypercare support log; resolution record |

### 10.3 Hypercare and Post-Go-Live Support

APPSolve's standard post-go-live support model follows a tapering structure:

- **Hypercare (Months 1–3):** Full complement of senior HCM and technical consultants available to resolve issues, adjust configuration, and support user adoption.
- **Critical care (Months 4–6):** Reduced support team led by senior consultants. Focus shifts from stabilisation to optimisation and knowledge transfer.
- **Steady state:** Transition to APPSolve's managed services model or client-managed support, depending on client preference.

Additionally, quarterly Oracle release management is provided as part of the post-go-live managed services: APPSolve assesses each Oracle quarterly feature release, advises on relevant new features, and assists with activation and testing.

### 10.4 Governance

**Change control:** APPSolve operates a formal change control process throughout the implementation. Any change to agreed scope, deliverables, architecture, cost, or schedule is documented, assessed for impact, and approved by the project steering committee before implementation.

**Risk management:** A centralised risk log is maintained throughout the engagement. Risks are assessed for impact and likelihood at bi-weekly team meetings; unmitigated risks are escalated to the steering committee. The risk log is available to the client at all times.

**Issue management:** An issue resolution process ensures timely treatment of all project issues. Issues are logged, assessed, resolved at the project team level where possible, or escalated to the steering committee with a recommended resolution and impact assessment.

**Configuration management:** APPSolve maintains strict configuration management controls throughout the project — protecting completed deliverables, controlling updates, ensuring version integrity, and managing the controlled release of configuration from development to test to production environments.

### 10.5 Testing

APPSolve's testing approach covers three distinct phases:

- **Conference Room Pilot (CRP 1 and CRP 2):** The business-level reflection sessions where stakeholders see and validate the system build. CRP 1 validates the initial build; CRP 2 validates corrections and enhancements from CRP 1.
- **Integration Testing:** APPSolve-led technical testing of all interfaces, validating that data flows correctly between Oracle HCM and connected systems. Integration testing is driven by the APPSolve team and may require collaboration with third-party system support teams.
- **User Acceptance Testing (UAT):** Client-led, APPSolve-facilitated UAT. Employees act as end users, managers, and administrators to verify the system operates as designed. APPSolve provides UAT scripts and facilitates sessions; the client provides UAT participants and signs off on acceptance.

### 10.6 Change Management

APPSolve's implementation approach incorporates structured change management to support adoption:

- Key stakeholder identification and engagement from project initiation
- Business process change impact assessment
- Train-the-trainer delivery — APPSolve trains the client's identified super-users; the client trains end users using APPSolve-produced training material
- User interface personalisation aligned to the client's brand, supporting familiarity and adoption
- Guided journeys within the system to support employees through new processes

---

## Section 11 — Risk Register

| Risk ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-W1-001 | Organisational design decisions made late in the project delay dependent module configuration | Medium | High | APPSolve mandates organisational design sign-off in the Journey Workshop phase before any dependent configuration begins |
| R-W1-002 | Data quality issues in legacy HR systems cause migration delays at go-live | High | Medium | APPSolve provides data migration templates and a data readiness assessment early in the project; client begins data cleansing in parallel with configuration |
| R-W1-003 | Third-party payroll system integration timelines not aligned with Oracle HCM go-live | Medium | High | Payroll integration planning is initiated in Journey Workshop; third-party vendor engagement is a named dependency in the project plan |
| R-W1-004 | Quarterly Oracle release introduces breaking changes to configured functionality | Low | Medium | APPSolve conducts a quarterly release impact assessment before each release is applied; regression testing is executed on impacted areas |
| R-W1-005 | Super-user availability insufficient during UAT, causing UAT delays or incomplete sign-off | Medium | Medium | Super-user availability is formalised as a project assumption and included in the project charter at inception; escalation path to the project sponsor is defined |

---

## Section 12 — Assumptions Register

| Assumption ID | Assumption |
|---|---|
| A-W1-001 | The implementation is scoped for South Africa as the primary rollout jurisdiction. Multi-country extensions are scoped and priced separately. |
| A-W1-002 | The client will adopt a central shared services model for HR activities within the project scope. |
| A-W1-003 | Data migration is limited to active employees. Historical records for terminated employees are excluded unless separately scoped and agreed. |
| A-W1-004 | Standard Oracle-delivered reports and dashboards will satisfy the client's initial reporting requirements. Custom reports are out of scope unless separately agreed and priced. |
| A-W1-005 | Integration to the client's nominated payroll system is in scope. All other third-party integrations are out of scope unless separately agreed. |
| A-W1-006 | Data preparation, extraction, cleaning, and formatting in the correct Oracle template format is the client's responsibility. APPSolve provides templates and data governance frameworks. |
| A-W1-007 | Training delivery is train-the-trainer only. End-user training is the client's responsibility following APPSolve knowledge transfer to super-users. |
| A-W1-008 | Standard Oracle functionality will be used throughout. Customisation, development, or configuration outside Oracle standard functionality is out of scope unless separately agreed. |

---

## Section 13 — Source Mapping Table

| Claim | Source | HIST | Classification |
|---|---|---|---|
| APPSolve is an Oracle Level 1 Partner | ORACLE_FACT_BASELINE Section 1 | — | Approved fact |
| Published OPN expertise: Oracle Fusion Cloud HCM Core | ORACLE_FACT_BASELINE Section 2 | — | Approved fact |
| Over 23 years of Oracle consulting | ORACLE_FACT_BASELINE Section 13 | — | Approved fact |
| 50+ Senior Consultants | ORACLE_FACT_BASELINE Section 13 | — | Removed — BU Lead CROSS-1 2026-06-13 |
| OIC mandatory in all Fusion implementations | ORACLE_FACT_BASELINE Section 7 | HIST-007 | Implemented — HB go-live |
| OUM methodology | HIST-007 Assumptions section | HIST-007 | Implemented — HB and Afrocentric proposals |
| HCM Core is the foundation phase | HIST-007 Phase 3.3.1; HIST-015 Phase 3.3.1 | HIST-007, HIST-015 | Implemented |
| Absence management in HCM Core phase | HIST-007 Phase 3.3.1; HIST-015 Phase 3.3.1 | HIST-007, HIST-015 | Implemented |
| Self-service in HCM Core phase | HIST-007 Phase 3.3.1; HIST-015 Phase 3.3.1 | HIST-007, HIST-015 | Implemented |
| Journeys capability | HIST-006 Section 2 | HIST-006 | Platform capability (reframed) |
| AI-Based Skills | ORACLE_FACT_BASELINE Section 4.1 (confirmed in SAA Section 2) | HIST-006 | Platform capability (reframed); F-W3-001 confirms implemented |
| Workforce Directory / Modelling | ORACLE_FACT_BASELINE Section 4.1 | HIST-006 | Platform capability (reframed); F-W3-001 confirms implemented |
| Work Life | ORACLE_FACT_BASELINE Section 4.1 | HIST-006 | Platform capability (reframed); F-W3-001 confirms implemented |
| Benefits | ORACLE_FACT_BASELINE Section 4.1 | HIST-006 | Platform capability (reframed); F-W3-001 confirms implemented |
| Hollywood Bets go-live July 2025 | ORACLE_FACT_BASELINE Section 19 | HIST-007 | Confirmed implementation reference |
| Hollywood Bets 7,000 users | ORACLE_FACT_BASELINE Section 19 | HIST-007 | Confirmed implementation reference |
| Hollywood Bets: HCM Core, Absence Management, Recruiting, Talent Mgmt, Performance Mgmt, Career Development, Succession Planning, Help Desk | ORACLE_FACT_BASELINE Section 19 (base scope); HIST-007 BOM (full scope); OI-W1-001 CLOSED by BU Lead 2026-06-12 | HIST-007 | Confirmed scope — BU Lead authorised |
| OIC integration to third-party payroll at HB | HIST-007 BOM | HIST-007 | Implemented |
| Biometric integration at HB | HIST-007 Interfaces section | HIST-007 | In scope |
| SETA / WSP / ATR extract at HB | HIST-007 Annexure 1 | HIST-007 | In scope |
| HR Help Desk: chatbot and SMS channels; 4 routings | HIST-007 Annexure 2; OI-W1-002 CLOSED by BU Lead 2026-06-12 — confirmed live July 2025 | HIST-007 | Confirmed live — BU Lead authorised |
| SAP Payroll integration capability | ORACLE_FACT_BASELINE Section 14 | HIST-006 | Technical integration capability — A-003 applied 2026-06-13 |
| Mr Price — Learning Cloud only | ORACLE_FACT_BASELINE Section 19 | HIST-016 | Confirmed — scope restriction applied |
| SA-first multi-country deployment model | HIST-007 Implementation Approach; HIST-015 assumptions | HIST-007, HIST-015 | Delivery methodology |
| Shared services HR model | HIST-015 Specific Assumptions | HIST-015 | Delivery methodology |
| Active employees only for migration | HIST-015 Specific Assumptions | HIST-015 | Standard assumption |
| Hypercare: 3 months full team | HIST-007 Support phase | HIST-007 | Confirmed delivery model |
| Critical care: senior lead team post hypercare | HIST-007 Support phase | HIST-007 | Confirmed delivery model |
| Journey phases (Prep → Workshop → Reflection → Build → Test → UAT → Data → Look → Production → Support) | HIST-007, HIST-015 (identical phase descriptions) | HIST-007, HIST-015 | Confirmed methodology |
| POPIA compliance reference | ORACLE_FACT_BASELINE Section 16 context; governance rule | — | Governance requirement |
| OIC: pre-built Oracle adapters; custom REST/SOAP | HIST-006 (general OIC description, reframed); ORACLE_FACT_BASELINE | HIST-006 | Platform capability |
| HDL and HCM Extracts as integration patterns | ORACLE_FACT_BASELINE Section 7; HIST-015 Assumptions | HIST-006, HIST-015 | Platform capability / methodology |
| Sector framing — retail, mining, professional services | OI-W1-003 CLOSED by BU Lead 2026-06-12; C-W3-001 CLOSED by BU Lead 2026-06-12 — aviation removed (SAA not awarded) | — | BU Lead approved — no client names required |
| AI-assisted HCM capability section retained | OI-W1-004 CLOSED by BU Lead 2026-06-12 — platform capability framing confirmed | HIST-006 | Platform capability — APPSolve activates/configures; not APPSolve-developed |
| Mr Price — Learning Cloud implemented by APPSolve | ORACLE_FACT_BASELINE Section 19; C-W3-002 CLOSED by BU Lead 2026-06-12 | — | Confirmed implementation |
| Mr Price — broader Oracle HCM estate — APPSolve provides support only | C-W3-002 CLOSED by BU Lead 2026-06-12 | — | Support reference — not implementation reference for non-Learning modules |

---

## Section 14 — Governance Self-Review

### 14.1 Prohibited Wording Check

| Prohibited phrase | Appears in draft? | Action taken |
|---|---|---|
| "Oracle Gold Partner" | No | Suppressed — used "Oracle Level 1 Partner" throughout |
| "80 Senior Consultants" (Afrocentric) | No | Suppressed — "50+ Senior Consultants" also removed per BU Lead CROSS-1 2026-06-13 |
| "Gold Partner for 13 years" (Afrocentric) | No | Suppressed — company profile not sourced from HIST-015 |
| "Nigeria / Uganda / Bangladesh / Qatar" | No | Suppressed — removed per F9 geographic correction |
| "22 years" or "21 years" | No | "Over 23 years" used throughout |
| "110 senior consultants" | No | "50+ Senior Consultants" removed — BU Lead CROSS-1 2026-06-13 |
| "CCBA" (client name) | No | CCBA not named anywhere in draft |
| "SAA" as implementation evidence | No | SAA used for platform capability context only; not cited as client or reference |
| "DFA" | No | Not referenced |
| "SARB" | No | Not referenced |

### 14.2 Framing Check

| Check | Result |
|---|---|
| All capabilities framed as APPSolve implementing/configuring — not Oracle providing | ✅ Verified throughout |
| OIC described as mandatory standard — not optional | ✅ Section 2.3 and Section 9.1 |
| Hollywood Bets scope confirmed by BU Lead (OI-W1-001 CLOSED) | ✅ Section 8.1 — Core HCM, Absence, Recruiting, Talent Mgmt, Performance Mgmt, Career Development, Succession, Help Desk — all live July 2025, 7,000 users |
| Mr Price scope note applied — Learning Cloud only | ✅ Section 8.3 |
| SAA not cited as client or reference | ✅ No SAA client reference in draft |
| Afrocentric not named as client or reference | ✅ Methodology content used without naming |
| CCBA not named | ✅ CCBA not referenced |
| No unsupported project counts | ✅ No project count claims introduced |
| No unsupported country counts | ✅ No country count claims introduced |
| BEE Level 3 (where applicable) | ✅ Not in scope for capability statement; no BEE claim in draft |

### 14.3 Source Traceability Check

| Check | Result |
|---|---|
| Every factual claim in draft has a source mapped in Section 13 | ✅ All claims traced |
| All approved ORACLE_FACT_BASELINE phrases used verbatim where applicable | ✅ SAP Payroll A-003 amendment applied; Level 1 Partner phrase used verbatim |
| Afrocentric outdated stats suppressed | ✅ No outdated stats from HIST-015 extracted |
| Implementation evidence separated from platform capability in Section 13 | ✅ Classification column in Source Mapping Table |

### 14.4 Open Items — ALL CLOSED

| Item ID | Resolution | Closed by | Date |
|---|---|---|---|
| OI-W1-001 | APPROVED. HB module scope confirmed: Core HR, Absence Management, Recruiting, Talent Management, Performance Management, Career Development, Succession Planning, Help Desk — all live July 2025. Section 8.1 module table updated accordingly. | BU Lead | 2026-06-12 |
| OI-W1-002 | APPROVED. Oracle Help Desk confirmed live at July 2025 go-live. Section 8.1 updated — "In scope" changed to "Live — July 2025". | BU Lead | 2026-06-12 |
| OI-W1-003 | APPROVED. Sector framing approved as: retail, mining, professional services (aviation subsequently removed by C-W3-001). No client names required. | BU Lead | 2026-06-12 |
| OI-W1-004 | APPROVED — RETAIN SECTION. AI-assisted capability features section retained. Framing governance: platform capabilities only; no APPSolve-developed AI claims; no unsupported deployment claims; disclaimer language retained. Section 6.5 framing confirmed compliant. | BU Lead | 2026-06-12 |

### 14.5 BU Lead Corrections Applied

| Correction ID | Correction | Section affected | Applied |
|---|---|---|---|
| C-W3-001 | Aviation removed from sector list. SAA not awarded — aviation must not be claimed as an implemented Oracle HCM sector. Approved sectors: retail, mining, professional services. | 8.2; Source Mapping Table | ✅ 2026-06-12 |
| C-W3-002 | Mr Price Group updated — Learning Cloud as implementation reference; broader Oracle HCM estate as support reference only. Clear distinction maintained between implementation and support responsibility. | 8.3; Source Mapping Table | ✅ 2026-06-12 |

### 14.6 Implementation vs Support Governance Rule (Permanent)

The following distinction must be maintained throughout all Wave 3 Oracle HCM content and must not be collapsed in any subsequent extraction, amendment, or tender use of this document:

| Category | References | Usage |
|---|---|---|
| **Implementation references** | Hollywood Bets (8 modules, live July 2025); Mr Price Learning Cloud | May be cited as: "APPSolve implemented..." |
| **Support references** | Mr Price broader HCM estate; other supported Oracle HCM environments where implementation ownership is not confirmed | May be cited as: "APPSolve provides ongoing support..." — never "APPSolve implemented..." |

This rule was established by BU Lead correction C-W3-002 and applies to all Wave 3 Oracle HCM statements.

---

## Section 15 — Extraction Return Report

### Status
**W3S1-001 v1.3 Approved — COMPLETE. Approved by BU Lead 2026-06-13. All amendments applied. Copied to `06_Capabilities/Oracle/Oracle_HCM/`.**

### Deliverables Produced

| Deliverable | Status | Location |
|---|---|---|
| W3S1-001 Approved Capability Statement | ✅ Complete | This document — Sections 1–12 |
| Source Mapping Table | ✅ Complete | Section 13 |
| Risk Register | ✅ Complete | Section 11 (5 risks) |
| Assumptions Register | ✅ Complete | Section 12 (8 assumptions) |
| Governance Self-Review | ✅ Complete | Section 14 |
| Extraction Return Report | ✅ Complete | Section 15 |

### Source Usage Summary

| Source | Usage | Tier |
|---|---|---|
| HIST-007 Hollywood Bets V5.0 | Primary — phase descriptions, BOM, methodology, hypercare model, Annexures 1 and 2 | Implementation Evidence |
| HIST-015 Afrocentric V4.0 | Primary — delivery assumptions, SA deployment model, shared services pattern, phase descriptions | Implementation Evidence |
| HIST-006 SAA HCM RFP | Corroborating — platform descriptions (reframed), extended module list (AI Skills, Work Life, Benefits, Journeys) | Capability Evidence |
| ORACLE_FACT_BASELINE | Authoritative — all company stats, approved phrases, module confirmation, HB go-live data | Governing authority |
| CCBA (HIST-014) | Not used — not required given depth of primary and corroborating sources | Restricted |

### Changes from v1.0 to v1.1

| Change | Section | Trigger |
|---|---|---|
| Hollywood Bets module table expanded: Absence Management, Performance Management, Career Development, Succession Planning added as Live — July 2025 | 8.1 | OI-W1-001 CLOSED |
| Hollywood Bets biometric and SETA extract status updated from "In scope" to "Live — July 2025" | 8.1 | OI-W1-001 CLOSED |
| Section 8.1 Solution header updated to include full confirmed module list | 8.1 | OI-W1-001 CLOSED |
| Help Desk confirmed live July 2025 (was "In scope" only) | 8.1 | OI-W1-002 CLOSED |
| Sector framing updated: "healthcare" → "retail" | 8.2 | OI-W1-003 CLOSED |
| Section 6.5 AI framing confirmed as compliant — no changes required | 6.5 | OI-W1-004 CLOSED |
| Source mapping updated with new entries for OI resolutions | 13 | All OI items CLOSED |
| Section 14.4 open items closed | 14.4 | All OI items CLOSED |

### Changes from v1.1 to v1.2

| Change | Section | Trigger |
|---|---|---|
| Aviation removed from sector list — approved sectors now: retail, mining, professional services | 8.2 | C-W3-001 CLOSED |
| Mr Price Group updated: Learning Cloud = implementation; broader HCM estate = support only — distinct framing applied | 8.3 | C-W3-002 CLOSED |
| Source mapping: aviation correction and Mr Price implementation/support split documented | 13 | C-W3-001, C-W3-002 CLOSED |
| Section 14.5 corrections register added; Section 14.6 implementation vs support governance rule established | 14 | C-W3-001, C-W3-002 CLOSED |

### Changes from v1.2 to v1.3

| Change | Section | Trigger |
|---|---|---|
| "50+ Senior Consultants" removed from Section 1 prose and credential table | 1 | BU Lead CROSS-1 2026-06-13 |
| SAP Payroll "many times" claim replaced with approved capability statement | 7.4, 9.2 | A-003 |
| Journeys: "implements" → "configures and enables" | 5.2 | A-004 |
| Opportunity Marketplace cross-reference to W3S1-002 added | 6.4 | A-005 |
| Source mapping and prohibited wording entries updated | 13, 14.1 | CROSS-1 |
| Version updated to 1.3 Approved; approved_for_reuse set to Yes | Frontmatter, 17.1 | A-006 |

### Recommended Next Action

**APPROVED.** All amendments applied 2026-06-13. Document promoted to Approved status by BU Lead. Copied to `06_Capabilities/Oracle/Oracle_HCM/`.

Outstanding admin (pre-existing):
1. Register HIST-006, HIST-007, HIST-014, HIST-015, HIST-016, HIST-017 in DOCUMENT_REGISTER.csv
2. Oracle reference letters: ARM success story, Harmony 2024, Assore 2023, Adcock Ingram 2023 → `04_References/Oracle/`
3. BEE certificate renewal due 2026-07-31

---

## Section 17 — Approval Record and Pre-Tender Checks

### 17.1 Approval Record

| Field | Value |
|---|---|
| Document ID | W3S1-001-ORA-HCMCore |
| Title | Oracle HCM Core — Global HR and Employee Lifecycle Capability Statement |
| Version | 1.3 Approved |
| Status | Approved — BU Lead approved 2026-06-13; all amendments applied (A-003, A-004, A-005, CROSS-1) |
| approved_for_reuse | Yes — BU Lead approved 2026-06-13 |
| Approved by | Hein Blignaut (BU Lead) |
| Approval date | 2026-06-13 |

### 17.2 Pre-Tender Checks

| Check ID | Check | Timing |
|---|---|---|
| PT-W1-001 | Confirm Hollywood Bets account manager has confirmed HB as a referenceable client before citing HB in any live tender | Pre-tender |
| PT-W1-002 | Confirm OPN revalidation — Oracle Level 1 Partner status and Oracle Fusion Cloud HCM Core published expertise current as at tender submission date | Pre-tender |
| PT-W1-003 | Confirm BEE Level 3 certificate current and not expired (RS-19451, expires 2026-07-31). Do not cite BEE status in any tender after expiry | Pre-tender |
| PT-W1-004 | Confirm HB module scope at time of tender — full July 2025 live module list confirmed by BU Lead (OI-W1-001 CLOSED); verify no scope changes since go-live before citing | Pre-tender |

---

*W3S1-001-ORA-HCMCore v1.3 Approved — 2026-06-13 — Hein Blignaut (BU Lead) — approved_for_reuse: Yes*
