---
document_id: W2S1-005-ORA-ImplementationMethodology
title: "Oracle Implementation Methodology"
version: "1.2 APPROVED"
source_status: Approved
approved_for_reuse: Yes
approved_by: "Hein Blignaut"
approval_date: "2026-06-12"
reviewed_by: "Hein Blignaut"
review_date: "2026-06-12"
review_notes: "BU Lead decisions applied 2026-06-12. D-W5-001 CLOSED: multi-country blueprint principle confirmed; wording softened with 'typically' and 'subject to client operating model'. D-W5-002 CLOSED: Oracle Guided Learning softened to available enablement option where licensed and in scope. Full validation pass clean. No prohibited wording. No restricted client references. No W2S1-003/004 duplication. Scope confirmed as implementation methodology ending at hyper-care. Pre-tender checks D-W5-003 through D-W5-006 preserved."
sources:
  - "Hollywood Bets Accepted Proposal V5.0 (April 2023) — HIST-007"
  - "RedPath Mining RFI Reply Detail (March 2026) — HIST-008"
  - "ORACLE_FACT_BASELINE.md (2026-06-10, updated 2026-06-12)"
  - "W2S1-001-ORA-FusionCapability (Approved 2026-06-11)"
  - "W2S1-002-ORA-EBSCapability (Approved 2026-06-12)"
  - "W2S1-003-ORA-DBAExecutiveSummary (Approved 2026-06-11)"
  - "W2S1-004-ORA-ManagedServicesSupportModel (Approved 2026-06-11)"
created: "2026-06-12"
created_by: "Claude (AI — Wave 2 extraction)"
kb_destination: "05_Methodologies/Implementation/"
wave: "Wave 2"
bu: Oracle
---

> **APPROVED — approved_for_reuse: Yes — Approved by Hein Blignaut, 2026-06-12**
> Oracle Wave 2 Deliverable 5 of 5. Wave 2 COMPLETE.
> Pre-tender checks required before use: see Section 17.

---

# Oracle Implementation Methodology
**APPSolve Proprietary Delivery Framework**

---

## 1. Executive Summary

APPSolve is an Oracle Level 1 Partner with over 23 years of experience delivering Oracle solutions across Southern Africa and beyond. Our implementation methodology is a structured, iterative delivery framework built on the Oracle Unified Method (OUM) and the Oracle Customer Success Navigator — adapted through more than two decades of real-world Oracle delivery across Oracle Fusion Cloud, Oracle E-Business Suite (EBS), Oracle Cloud Infrastructure (OCI), and Oracle Integration Cloud (OIC).

The APPSolve implementation methodology guides every engagement from initial mobilisation through to a supported production go-live and hyper-care stabilisation. It provides clients, project sponsors, and procurement evaluators with a clear, repeatable process that manages scope, quality, risk, and business change at every stage of delivery.

Our methodology is not a generic project management approach applied to Oracle — it is an Oracle-native delivery framework that incorporates Oracle Modern Best Practices, the Oracle Starter Configuration, Oracle FBDI data migration standards, and Oracle Integration Cloud as core structural components. It has been applied and refined across Oracle Fusion HCM, Finance, Procurement, PPM, EBS R12/R12.2, and OCI transformation engagements for clients across the mining, financial services, retail, telecommunications, professional services, and public sectors.

This document describes the APPSolve implementation methodology framework — its delivery phases, project governance model, platform-specific delivery considerations, and the Oracle-native accelerators that reduce risk and accelerate time to value. Ongoing managed services and steady-state support following implementation are addressed in the APPSolve Oracle Managed Services Support Model (W2S1-004).

---

## 2. APPSolve Delivery Philosophy

APPSolve's approach to Oracle implementation is grounded in foundational delivery principles that have shaped our methodology and informed every engagement.

### 2.1 Senior-Only Delivery

APPSolve deploys senior consultants on all implementation engagements. Our 50+ Senior Consultants each bring 10 or more years of Oracle experience. There are no junior resources assigned to implementation delivery without senior oversight. This approach reduces delivery risk, accelerates design decisions, and ensures clients engage with experienced practitioners at every project touchpoint.

### 2.2 Standard Configuration First

APPSolve's default position on every engagement is to adopt Oracle's standard, out-of-the-box configuration before introducing customisation. Oracle's Cloud and EBS platforms are built around proven business best practices. Maximising standard functionality reduces implementation cost, lowers upgrade risk, and ensures clients benefit from Oracle's continuous product investment. Customisation is introduced only when a confirmed, justified business requirement cannot be met through configuration.

### 2.3 Iterative Prototype-to-Production

Rather than designing on paper and building from a fixed specification, APPSolve uses an iterative approach: the solution is built, demonstrated, refined, and validated in cycles. Each iteration — a Conference Room Pilot (CRP) — brings stakeholders progressively closer to the final production solution. This approach surfaces issues early, keeps the business engaged throughout the project, and ensures the delivered solution reflects operational reality rather than abstract requirements.

### 2.4 Customer Ownership from Day One

The APPSolve methodology transfers solution ownership to the client organisation progressively throughout the project — not only at go-live. Super users are involved in design decisions from the Prototype phase. Data migration is customer-led with APPSolve guidance. UAT is client-driven. The objective is a client team that is confident, capable, and operationally self-sufficient from the first day of steady-state operation.

### 2.5 Oracle Unified Method Alignment

Every APPSolve Oracle implementation is structured according to the Oracle Unified Method (OUM) — Oracle's own methodology framework for cloud and on-premise implementations — combined with the Oracle Customer Success Navigator for Fusion Cloud engagements. This alignment ensures APPSolve's delivery approach is consistent with Oracle's own quality benchmarks and that all documentation, deliverables, and governance artefacts meet the standards expected in enterprise Oracle programmes.

### 2.6 Cloud Readiness Embedded

APPSolve embeds cloud readiness into every Oracle Fusion engagement from the Mobilize phase. For Oracle EBS clients, the methodology includes an assessment of the OCI migration path as a standard planning consideration. APPSolve holds published Oracle expertise in Oracle E-Business Suite Migration to OCI and Oracle Cloud Infrastructure Migration.

---

## 3. Implementation Methodology Overview

The APPSolve Oracle implementation methodology is structured across six delivery phases, followed by a transition to the steady-state support model:

```
Mobilize → Scope & Design → Prototype → Validate → Deploy → Evolve
```

Each phase has defined entry criteria, activities, and exit deliverables. Phases do not run in strict sequence — technical delivery, data preparation, and integration build activities often run in parallel with design and configuration work. Change management is embedded across all phases, not treated as a separate workstream.

| Phase | Key Activities | Primary Source Evidence |
|---|---|---|
| **Mobilize** | Team assembly, initiative charter, work plan, kick-off | RedPath Mining RFI (March 2026); Hollywood Bets V5.0 (April 2023) |
| **Scope & Design** | Scope confirmation, Oracle Modern Best Practices alignment, data assessment, workshop scheduling | RedPath Mining RFI |
| **Prototype** | Design workshops, CRP1 (Prototype 1), CRP2 (Prototype 2), end-to-end SIT | RedPath Mining RFI; Hollywood Bets V5.0 |
| **Validate** | Final validation, documentation finalisation, go-live preparation | RedPath Mining RFI |
| **Deploy** | Production build, user enablement, training, go-live execution | RedPath Mining RFI; Hollywood Bets V5.0 |
| **Evolve** | Hyper-care, critical care, transition to steady state | Hollywood Bets V5.0 |

**Methodology basis:** Oracle Unified Method (OUM) and Oracle Customer Success Navigator. APPSolve has developed and refined this framework from confirmed delivery experience, embedding iterative CRP cycles, change management, and Oracle FBDI data migration as structural components.

---

## 4. Mobilize Phase

The Mobilize phase establishes the foundation for the entire engagement. No design or configuration work begins until Mobilize is complete.

### 4.1 Team Assembly and Scheduling

The implementation team is identified, scheduled, and assembled with clear expectations for work pace, roles, and responsibilities. APPSolve assigns senior resources at this stage and confirms team members for the full project duration. Resource continuity across the implementation lifecycle is a core APPSolve commitment — the team that mobilises is the team that delivers.

### 4.2 Initiative Charter

An initiative charter is prepared to define:
- Vision and business drivers for the implementation
- Desired business outcomes
- Project scope — inclusions and exclusions
- Success criteria
- Resource plan
- Budget and commercial model (fixed price with change control, or time and materials)

The charter is agreed and signed off by the implementation sponsor before Scope & Design begins.

### 4.3 Work Plan Definition

A detailed project work plan is produced, covering all activities and tasks required to achieve the programme objectives. Tasks are assigned to named resources. The work plan supports workload management and progress tracking and is aligned to agreed milestone dates.

### 4.4 Kick-off

An official project kick-off is hosted with the APPSolve Project Manager, the client project sponsor, and all key stakeholders. Sponsor attendance at kick-off is a key success factor — it signals executive commitment and establishes the governance tone for the engagement.

---

## 5. Scope and Design Phase

The Scope and Design phase confirms the project boundary, aligns the solution to Oracle's standard best practices, and prepares the environment and teams for structured design workshops.

### 5.1 Scope Confirmation

Project scope is formally confirmed, with inclusions and exclusions documented. Scope is aligned to Oracle Modern Best Practices as the default functional baseline. Where business requirements differ from the Modern Best Practice standard, these are recorded as decision points for the design workshops rather than resolved unilaterally.

### 5.2 Oracle Modern Best Practices Alignment

APPSolve uses Oracle's Starter Configurator and Modern Best Practices library as the starting point for all Fusion Cloud engagements. The Starter Configurator provides a working, pre-configured Oracle instance before detailed design begins — allowing the client's team to react to a concrete solution rather than abstract requirements documents. This reduces workshop time and accelerates design decisions.

### 5.3 Data Requirements and Assessment

Data readiness is assessed at the start of the engagement:
- Existing data completeness is evaluated against Oracle's data model requirements
- FBDI templates are provided for each module in scope
- Data gaps are identified and a remediation plan is agreed with the client
- The client is accountable for data accuracy; APPSolve is accountable for loading structure, template guidance, and delivery to the correct Oracle target

### 5.4 Workshop Scheduling and Environment Preparation

A schedule of design workshops is produced and calendar invites issued in advance. Oracle Cloud Application test environments are configured and an environment management strategy is agreed to govern the use of development, test, and production instances throughout the engagement.

---

## 6. Prototype Phase

The Prototype phase is the iterative core of the APPSolve methodology. Two full prototype cycles — CRP1 and CRP2 — are completed before the solution advances to final validation.

### 6.1 Design Governance

A solution authority is established at the start of the Prototype phase:
- Meets regularly to ensure design decisions align to project objectives and business outcomes
- Operates within established architecture and design principles
- Is empowered by the executive sponsors to make final design decisions
- Receives regular updates on key decisions and their business implications

Executive sponsors remain engaged throughout the Prototype phase. Changes to agreed design decisions are managed through formal change control.

### 6.2 High-Level Design Workshops (Prototype 0)

Before CRP1 begins, focused design workshops are conducted using Oracle Modern Best Practices and the Starter Configuration as discussion tools. Each session:
- Opens with design principles and clear expectations for each participant role
- Uses Oracle process flows and use cases to structure discussion
- Documents all decisions, owners, and action items
- Records lower-priority or out-of-scope items for separate tracking

### 6.3 Prototype 1 — CRP1

The first full prototype of the solution is built from the output of the high-level design workshops. CRP1 includes:
- Functional configuration
- Delivered and configured reports
- OIC integration connections and initial interface builds
- Representative converted data

Iterative playback sessions are conducted — initially APPSolve-guided (system demonstration with structured discussion), then client-directed (open exploration). Feedback is documented, assessed against the change control process, and incorporated into CRP2.

### 6.4 Detailed Design Workshops

Detailed design workshops are scheduled between CRP1 and CRP2 to address:
- Design decisions deferred from high-level workshops
- Changes arising from CRP1 feedback
- Exception flows and edge cases
- Security and role design

### 6.5 Prototype 2 — CRP2

The second prototype incorporates all changes agreed from CRP1 feedback and the detailed design workshops. CRP2 includes:
- Refined configuration and extensions
- Full OIC integration build (inbound and outbound interfaces)
- Production-representative migrated data
- Security and roles applied

CRP2 represents the production-intent solution. A second round of playback and validation sessions is conducted. Client sign-off on CRP2 is the gate to the Validate phase.

### 6.6 System Integration Testing (SIT)

Following CRP2, all system components are integrated and a system integration test verifies:
- End-to-end business process support
- Successful data migration from source systems
- OIC interface correctness and error handling
- Solution security and access controls

---

## 7. Validate Phase

The Validate phase prepares the solution and the organisation for final sign-off and production go-live.

### 7.1 Production-to-Test Copy

A production-to-test copy of the Oracle solution is created, incorporating all solution components, to provide the most realistic configuration for final testing. This environment mirrors the intended production state.

### 7.2 Final Validation

The integrated solution is validated against the full set of business requirements. Special attention is given to:
- Recurring business processes (monthly financial period close, monthly payroll runs)
- Data migration accuracy and completeness
- Security and access controls across all roles
- Operational readiness (batch schedules, monitoring points, error handling)

Validation scenarios and test scripts are documented. Business stakeholders are accountable for final sign-off.

### 7.3 Documentation Finalisation

All solution specification documents are updated to reflect the final production configuration:
- Oracle Cloud Applications configuration specifications
- Extension and customisation documentation
- Report and integration (OIC) specifications
- Data migration mapping and reconciliation records
- Security design documentation

Updated specifications are handed over to the team responsible for operating the Oracle solution post go-live.

### 7.4 Go-Live Preparation

A detailed cutover plan is produced and agreed, covering:
- Roles, responsibilities, and timelines for each cutover activity
- Data migration execution sequence
- Integration activation and verification sequence
- Contingency and rollback procedures
- Stakeholder, vendor, and third-party support team coordination

---

## 8. Deploy Phase

The Deploy phase delivers the production go-live and stabilises the organisation in its new operating model.

### 8.1 Production Build

The Oracle solution is deployed to production:
- Final configuration and extension deployment
- Data migration executed using Oracle FBDI sheets and standard APIs
- Security controls activated and validated
- All system components verified against a comprehensive deployment checklist

For financial implementations, all transactional data is reconciled to the corresponding Trial Balance control account before the production load is accepted. Sub-module data is not loaded unless it reconciles to the relevant control account balance.

### 8.2 User Enablement

All end users and administrators are enabled before go-live:
- User training sessions covering system features, navigation, and role-based tasks
- Oracle Guided Learning (OGL) introduced as an enablement option where licensed, included in project scope, and appropriate to the client's user adoption strategy
- Train-the-Trainer approach as default; end-user training at scale managed by the client's trained super users
- Support resources and escalation paths communicated to all users

APPSolve produces modular training materials in accordance with the OUM documentation standard — built for the client's specific configuration, not generic Oracle curriculum.

### 8.3 Go-Live Execution

Go-live is executed against the agreed cutover plan. The APPSolve team is available — on-site or on call — for the full duration of the cutover window. Critical issues encountered during cutover are triaged and resolved within the agreed incident process before the system is declared live.

---

## 9. Evolve / Hyper-care Phase

Hyper-care is the final delivery phase of the APPSolve implementation engagement. It is a structured support transition — not a managed services contract — that ensures the client achieves stable operations before the implementation team demobilises.

### 9.1 Hyper-care (~3 Months)

Immediately following go-live, the full APPSolve implementation team remains available:
- Production defects are triaged and resolved with priority treatment
- Design adjustments required due to go-live operational realities are assessed and implemented via change control
- Business users receive guided operational support as they transition from training to live usage
- Oracle quarterly patch releases falling within the hyper-care window are assessed and tested

### 9.2 Critical Care (~6 Months)

After the initial hyper-care period, the engagement transitions to a critical care model:
- The support team is reduced in size but remains senior-led
- Focus shifts from defect resolution to operational stabilisation and user adoption
- The client team progressively assumes ownership of first-level support and operational maintenance
- The transition timeline from critical care to steady state is calibrated to the level of business ownership achieved

### 9.3 Steady-State Transition

Upon completion of the critical care period, the engagement transitions to APPSolve's steady-state managed services model:
- Formal handover of all operational documentation
- Client environment onboarded to the APPSolve managed services model
- SLA tiers (P1/P2/P3/P4) agreed appropriate to the client's operational risk profile
- 24x7 monitoring activated

The steady-state managed services model is documented in the APPSolve Oracle Managed Services Support Model (W2S1-004).

---

## 10. Project Governance Framework

The APPSolve project governance framework operates across all implementation phases. It provides a structured set of processes for managing risk, issues, changes, and solution integrity throughout the engagement.

### 10.1 Risk Management

A centralised risk log is maintained for all identified risks:
- Risks rated by impact and likelihood at bi-weekly team reviews
- Mitigation and reduction ownership assigned at project-team level
- Risks where mitigation is blocked are escalated by the Project Manager to the Project Steering Committee
- Consistent approach, clear ownership, and communicated risk policies across the project team

### 10.2 Issue Management

An issue resolution process ensures timely treatment of all project issues:
- Issues identified by team leads and documented in the issues log
- PM-led assessment of impact on cost, time, and scope
- If no scope/budget/schedule impact: team-level resolution with Steering Committee notification as appropriate
- If impact on scope/budget/schedule: formal change request raised and escalated to the Project Steering Committee for decision
- The Steering Committee may request additional input before authorising resolution

APPSolve tracks missing information, policy decisions, resource availability, new or changed requirements, estimate accuracy, unfulfilled dependencies, and software defects as standard issue categories.

### 10.3 Change Control

All proposed changes to project scope, deliverables, architecture, cost, or schedule are managed through a formal change control process:
- Change requests are documented, logged, and assigned
- Impact is assessed across cost, time, and scope
- Change recommendation is formulated and presented for sign-off
- Approved changes are implemented and tracked in the project plan
- Changes with budget impact require Steering Committee authorisation before implementation

Change control is established at project inception and applied consistently from Scope & Design through go-live.

### 10.4 Configuration Management

The configuration management process protects the integrity of completed deliverables and ensures version control:
- Completed deliverables are secured and backed up
- Updates to completed deliverables are controlled and documented
- The current approved version of each deliverable is the authoritative reference
- Related deliverables are kept in version alignment

Configuration management governs Oracle environment versions, configuration export files, OIC integration artefacts, data migration templates, and project documentation.

### 10.5 Governance Integration with Client Structures

APPSolve's governance model is designed to integrate with the client's existing governance structure. Where the client operates a formal Programme Management Office (PMO), APPSolve's Project Manager and team leads are incorporated into the client's governance reporting framework. APPSolve adopts the client's risk, issue, and change control conventions where a mature process already exists.

---

## 11. Oracle Delivery Accelerators

APPSolve embeds Oracle-native accelerators into every implementation to reduce risk, accelerate delivery, and maintain alignment with Oracle best practices.

### 11.1 Oracle Integration Cloud (OIC)

OIC is the standard integration layer for all Oracle Fusion Cloud implementations. APPSolve implements OIC on every Fusion engagement to manage all inbound and outbound interfaces between Oracle SaaS and third-party systems. Oracle Integration is a published APPSolve OPN expertise area.

OIC use cases delivered across APPSolve Fusion programmes include:
- Third-party payroll system integration (SAP Payroll, PaySpace, and other payroll platforms)
- Biometric system integration
- HR extract to downstream systems
- Financial module interfaces
- Custom workflow and notification routing

### 11.2 Oracle FBDI (File Based Data Import)

Oracle FBDI is APPSolve's standard data migration approach. FBDI provides:
- Oracle-validated import templates for all modules
- Structured validation before data lands in Oracle tables
- Auditability and error reporting
- Consistency with Oracle's own migration standards

For financial modules, all transactional data loaded via FBDI is reconciled to the corresponding Trial Balance control account before the production load is accepted.

### 11.3 Oracle Starter Configurator and Modern Best Practices

APPSolve uses Oracle's Starter Configurator at the start of every Fusion engagement. This gives the client team an immediate view of a working Oracle solution before detailed design begins, accelerates workshop decisions by providing a concrete starting point, and reduces design time by focusing discussion on confirmed deviations from Oracle best practice.

### 11.4 Oracle Guided Learning

Oracle Guided Learning (OGL) is an available enablement option for Oracle Fusion clients where OGL is licensed, included in project scope, and appropriate to the client's user adoption strategy. Where OGL is included in scope, it provides an in-application guidance layer that can reduce end-user learning time and lower the volume of support queries during the hyper-care period. OGL is discussed during the Scope & Design phase and scoped explicitly where applicable.

### 11.5 Oracle University Training

APPSolve recommends Oracle University training for super users and administrators as a supplement to the project-specific training delivered during the Validate and Deploy phases. Oracle University provides product depth that complements the solution-specific enablement APPSolve delivers.

### 11.6 OUM Documentation Standards

All APPSolve project documentation — training materials, configuration specifications, design documents, and test scripts — is produced in accordance with the Oracle Unified Method documentation standard. This ensures all project artefacts are structured, version-controlled, and transferable to the client and to the APPSolve support team at handover.

### 11.7 OCI Security Documentation

For Oracle Fusion Cloud tenders requiring cloud security evidence, APPSolve holds OCI SOC 1 Type 2 and SOC 2 Type 2 Bridge Letters (current as at June 2025). These letters provide independent assurance of Oracle Cloud Infrastructure security controls and can be attached to tender submissions requiring cloud security compliance evidence.

---

## 12. Oracle Fusion Delivery Considerations

The following platform-specific considerations apply to all Oracle Fusion Cloud implementations.

### 12.1 Module Sequencing

Oracle Fusion HCM implementations follow a defined module sequencing discipline:
- Core HR (Global HR, Absence Management, Self Service) is always implemented first — it provides the foundational data structures (positions, jobs, locations, grades, work structures) for all subsequent HCM modules
- Downstream modules (Recruiting, Talent Management, Goal Management, Performance Management, Learning, Help Desk) are phased in after Core HR is stable in production
- Finance modules are scoped independently and follow their own phased structure

Sequencing reduces downstream rework and ensures master data is established before dependent modules are configured.

### 12.2 OIC as Mandatory Architecture Component

Every Oracle Fusion implementation includes OIC as the integration layer. OIC manages all interfaces between Oracle SaaS and third-party systems. An OIC integration strategy is established from the Scope & Design phase — even where the initial interface count is low — because future integration needs are significantly easier to address when OIC is already provisioned and governed.

### 12.3 Oracle Quarterly Patch Cycle

Oracle Fusion Cloud releases quarterly updates. APPSolve factors the Oracle patch release schedule into the project plan during the Prototype and Validate phases to:
- Avoid releasing a production configuration immediately before a major patch
- Test key business flows against upcoming releases where a patch falls within the project window
- Communicate patch-related functional changes to the business during the Evolve phase

### 12.4 Security and Role Design

Oracle Fusion role design is addressed from the Scope & Design phase:
- Roles and data access are assigned based on confirmed business requirements
- Area of Responsibility (AOR) constructs are applied for HCM data security
- Seeded roles are modified only where confirmed business requirements cannot be met through standard assignment
- Role assignments are validated against Oracle's usage report to confirm that privilege assignments do not trigger licence overage

### 12.5 Multi-Country and Blueprint Rollout

For multi-country or blueprint-based programmes, APPSolve typically recommends establishing the primary country as the first implementation wave, subject to the client's operating model and programme objectives. The first-country implementation builds the global configuration blueprint — the foundation for all subsequent country rollouts. Where this approach is adopted, subsequent country rollouts are typically accelerated using the same core team, the established blueprint, and lessons from the primary-country implementation.

---

## 13. Oracle EBS Delivery Considerations

APPSolve has delivered Oracle E-Business Suite implementations and maintained EBS client environments since the company's founding. The following platform-specific considerations apply to Oracle EBS engagements.

### 13.1 OUM on Oracle EBS

The Oracle Unified Method applies to Oracle EBS implementations. The Mobilize → Scope & Design → Prototype → Validate → Deploy → Evolve phases are followed on all EBS engagements, with the following adaptations:
- The Prototype phase uses Conference Room Pilots (CRP1/CRP2) in the traditional EBS pattern
- Configuration is managed through the EBS setup workbench and documented in version-controlled setup documents
- Custom development (RICEW — Reports, Interfaces, Conversions, Extensions, Workflows) is scoped during Scope & Design and built and tested during the Prototype phase

### 13.2 Customisation Assessment

EBS implementations often inherit a body of existing customisation from prior implementations or upgrade cycles. APPSolve assesses all customisations during the Scope & Design phase:
- Each customisation is reviewed for ongoing business justification
- Standard R12 or R12.2 functionality that covers previously customised areas is identified and presented as a replacement option
- A recommendation is made to retire, migrate, or retain each customisation
- Reducing the customisation footprint lowers ongoing support cost and simplifies future upgrade paths

### 13.3 EBS-to-OCI Migration

APPSolve holds published Oracle expertise in Oracle E-Business Suite Migration to OCI. For clients running EBS on-premise, the methodology includes a cloud readiness assessment as a standard planning consideration:
- Current infrastructure profile and Oracle EBS version assessment
- Lift-and-shift feasibility (technical migration of existing EBS to OCI)
- Re-implementation consideration (migration to Oracle Fusion Cloud using EBS as the legacy data source)
- OCI security certifications available (SOC 1 Type 2 and SOC 2 Type 2 Bridge Letters)

The EBS-to-OCI migration path is agreed with the client during the Mobilize phase where relevant.

### 13.4 DBA Integration During Implementation

APPSolve's Oracle DBA capability is embedded into the EBS implementation team. DBA services provided during implementation include:
- Environment provisioning and configuration (development, test, UAT, production)
- Database patching and EBS patch application
- Performance monitoring during CRP and UAT phases
- Production cutover DBA support
- Post-go-live DBA monitoring during the hyper-care period

For detail on APPSolve's Oracle DBA managed services capability, refer to the Oracle DBA Executive Summary (W2S1-003).

---

## 14. Transition to Support Services

The APPSolve implementation methodology includes a structured handover from the implementation team to the APPSolve managed services support function. This transition is planned from Mobilize and executed across the Evolve phase.

### 14.1 Transition Planning

Transition planning begins at the Mobilize phase:
- The post-go-live support model is agreed and documented
- A support agreement is scoped and initiated during the implementation project
- The transition timeline (hyper-care → critical care → steady state) is confirmed

### 14.2 Knowledge Transfer

During the Validate and Deploy phases, APPSolve transfers operational knowledge to the client's internal team and to the APPSolve managed services team. Knowledge transfer deliverables include:
- System configuration documentation
- OIC integration specifications and connection inventory
- Data migration reconciliation records
- Security design documentation
- Operational runbook (batch schedules, monitoring points, common administrative tasks)

### 14.3 Steady-State Support Handover

Upon completion of the critical care period, the engagement formally transitions to the APPSolve Oracle managed services support model:
- ITIL-aligned service management activated
- SLA tiers (P1/P2/P3/P4) agreed per the client's operational risk profile
- Monthly service reviews and quarterly governance cadence established
- 24x7 monitoring and after-hours support activated for P1/P2 incidents

The full APPSolve Oracle Managed Services Support Model — including ITIL framework, CSI model, service delivery governance, and CMDB — is documented in W2S1-004-ORA-ManagedServicesSupportModel.

---

## 15. Why APPSolve

### 15.1 Oracle Partnership and Credentials

APPSolve is an Oracle Level 1 Partner and Oracle Value-Added Reseller, authorised to sell, implement, and support Oracle software. With over 23 years of Oracle experience, APPSolve is one of the most established Oracle practices in South Africa. Oracle has recognised APPSolve with six awards across global, EMEA, and SADC regions, including Oracle Business Impact Awards in 2024 across the EMEA and ECEMEA regions.

APPSolve holds five published Oracle expertise areas:
- Oracle Fusion Cloud Financials
- Oracle Fusion Cloud HCM Core
- Oracle Integration
- Oracle E-Business Suite Migration to OCI
- Oracle Cloud Infrastructure Migration

### 15.2 Implementation Depth

APPSolve's Oracle implementation practice spans Oracle Fusion Cloud (HCM, Finance, Procurement, PPM) and Oracle E-Business Suite (R12, R12.2) across South Africa, Southern Africa, and internationally. Our 50+ Senior Consultants have delivered Oracle implementations for clients across the mining, financial services, retail, telecommunications, professional services, and public sectors.

Fusion Cloud implementations include multi-module Oracle HCM programmes (Core HR, Absence, Recruiting, Talent, Performance, Goal Management, Help Desk, Learning) and Oracle Finance and Procurement engagements across multi-country environments. EBS implementations span full R12 and R12.2 programmes across financial services, mining, and professional services.

### 15.3 OIC Integration Leadership

Oracle Integration Cloud is a mandatory component of every APPSolve Oracle Fusion implementation. APPSolve has delivered OIC integrations across Oracle Fusion HCM, Oracle EBS, Oracle Fusion Finance, and hybrid cloud environments — including integrations to SAP Payroll, PaySpace, biometric systems, and custom third-party platforms. APPSolve holds a published OPN expertise area in Oracle Integration.

### 15.4 Local Presence and Delivery Model

APPSolve operates from offices in Gauteng and the Western Cape. Senior consultants are locally based in South Africa, enabling on-site delivery when required. Implementation work is conducted remotely, on-site, or in a hybrid model calibrated to client preference and engagement requirements.

### 15.5 Resource Stability

APPSolve assigns resources at project inception and commits to maintaining the assigned team for the full project duration. Long consultant tenures and deep Oracle product familiarity mean client engagements benefit from continuity and accumulated knowledge across the full delivery lifecycle.

---

## 16. Conclusion

APPSolve's Oracle implementation methodology is a structured, evidence-based delivery framework built on the Oracle Unified Method, refined through over two decades of Oracle delivery, and applied consistently across Oracle Fusion Cloud, Oracle E-Business Suite, Oracle Integration Cloud, and Oracle Cloud Infrastructure engagements.

The methodology delivers predictable, governed implementations from Mobilize through Hyper-care — with risk management, issue resolution, and change control embedded at every stage. The senior-only delivery model, iterative CRP approach, and Oracle-native tooling (OIC, FBDI, Oracle Starter Configurator) reduce implementation risk and accelerate the path to a stable, optimised production environment.

For managed services and ongoing support following implementation, refer to the APPSolve Oracle Managed Services Support Model (W2S1-004).

---

## 17. Approval Record and Pre-Tender Checks

### 17.1 Approval Record

| Field | Value |
|---|---|
| **Approved by** | Hein Blignaut |
| **Approval date** | 2026-06-12 |
| **approved_for_reuse** | Yes |
| **Wave** | Wave 2 — Deliverable 5 of 5 |
| **Status** | Oracle Wave 2 COMPLETE |
| **BU Lead decisions** | D-W5-001 CLOSED (multi-country blueprint confirmed; wording softened). D-W5-002 CLOSED (OGL softened to available option where licensed and in scope). |
| **Validation** | Full validation pass clean — zero findings. No prohibited wording. No restricted client references. No W2S1-003/004 duplication. Scope confirmed: implementation methodology ending at hyper-care. |

### 17.2 Pre-Tender Checks

These checks are required before this document is included in any tender response. They are standing operational controls — not approval blockers — and must be confirmed at each tender submission.

| Check | Action required |
|---|---|
| **D-W5-003 — OPN Annual Revalidation** | Verify that all five published Oracle expertise areas and Oracle Level 1 Partner status are current in the OPN portal before including in any tender. Oracle certifications require annual renewal. |
| **D-W5-004 — BEE Certificate Expiry** | Current BEE certificate (RS-19451) expires **2026-07-31**. Do not cite BEE in any tender after expiry without the renewed certificate in hand. This document contains no BEE content — no action needed at document level. |
| **D-W5-005 — Named Client References** | This document contains no named client references. Where a tender requires named implementation references within a methodology submission, select from the citability-classified lists in W2S1-001 (Oracle Fusion referenceable clients) and W2S1-002 (Oracle EBS referenceable clients). Do not add client names to this document without BU Lead instruction for that tender. |
| **D-W5-006 — Awards Claims** | The six Oracle awards in the approved table are sourced from W1S1-003. Do not add additional awards claims (including APPS/SAAS Partner Business Impact awards referenced in source documents) to tender submissions without BU Lead confirmation that those awards are current and approved for external use. |

---

---

# Appendix A — Extraction Notes

| Note | Detail |
|---|---|
| **Primary sources** | Hollywood Bets Accepted Proposal V5.0 (April 2023) — HIST-007; RedPath Mining RFI Reply Detail (March 2026) — HIST-008 |
| **OUM confirmation** | Confirmed in both sources. HB V5.0 line 66: "based on the OUM Methodology." HB V5.0 line 505: "The Oracle Unified Methodology (OUM) will be adhered to within the scope of APPSolve's applications project engagement responsibility." RedPath Mining line 158: "based on Oracle's OUM and current Customer Success Navigator stages." |
| **Phase naming** | User-specified phases (Mobilize → Scope & Design → Prototype → Validate → Deploy → Evolve) adopted as document structure. These align with RedPath Mining RFI phase structure and ORACLE_FACT_BASELINE Section 17. HB V5.0 uses HCM-module-centric phase naming (Phase 0 Scoping, Phase 1–4) — content mapped to standard phase names. |
| **Hyper-care timelines** | Source: HB V5.0 lines 365–367. "3 months of hyper care with a full complement of senior resources available to assist with use and design adjustments or bug fixes. This is followed by critical care where the support team size is reduced and lead by senior resources typically for a period of about 6 months." Extracted by intent, not verbatim. |
| **Project governance** | Source: HB V5.0 lines 381–441. Risk, Issue, Change Control, and Configuration Management processes all sourced from this document. Risk log, issue log, change request process, steering committee escalation path all confirmed. |
| **OIC as mandatory** | Source: RedPath Mining RFI line 109: "All our Fusion implementation we have also implemented Oracle Integration Cloud." ORACLE_FACT_BASELINE Section 7 confirms this as a KB-wide rule. |
| **FBDI and reconciliation** | Source: RedPath Mining RFI lines 111–113. Financial reconciliation to Trial Balance before accepting load also from this source. |
| **Solution Reflection / CRP** | HB V5.0 lines 346–349 describe "Solution Reflection" — two rounds (guided then free exploration) — equivalent to CRP1 and CRP2. Mapped to standard CRP terminology in W2S1-005. |
| **KPMG reference** | HB V5.0 line 335 references "most recently at KPMG" as evidence of similar rollouts. KPMG is source evidence only (W2S1-002 BU-EBS-002 classification). Not cited by name in W2S1-005. |
| **DFA** | RedPath Mining RFI lists DFA in the implementation client list (lines 124–129). DFA is restricted (internal-use only). Not extracted into this document. |
| **Nala country count** | RedPath Mining RFI line 151 claims "8 countries." ORACLE_FACT_BASELINE Section 19 corrects this to 4 countries. Nala not cited in this document. |
| **Company stats overridden** | RedPath Mining RFI company profile contains "22 years" (line 33) and "110 Senior Consultants" (line 39). Both prohibited per ORACLE_FACT_BASELINE Section 15. Approved values applied: "over 23 years" and "50+ Senior Consultants." |
| **Multi-country blueprint principle** | Source: HB V5.0 lines 337–339. Synthesised into Section 12.5. D-W5-001 CLOSED: confirmed with "typically" and "subject to client operating model" qualifiers. |
| **SAA Section 5** | Identified as supplementary source. Not read. Not required — both Tier 1 sources provide complete methodology coverage. Can supplement in a future revision. |
| **Payroll integration wording** | Approved phrase: "APPSolve has implemented an Integration between Oracle HCM and SAP Payroll many times" (ORACLE_FACT_BASELINE Section 14). Used in Section 11.1 by paraphrase only. |
| **W2S1-003 / W2S1-004 scope** | DBA capability claims not reproduced in body — deferred to W2S1-003 reference (Section 13.4). ITIL, CSI, CMDB, P1–P4 SLA framework not reproduced — deferred to W2S1-004 reference (Section 14.3). |

---

# Appendix B — Fact Verification Summary

| Claim | Baseline Reference | Status |
|---|---|---|
| "Oracle Level 1 Partner" | ORACLE_FACT_BASELINE Section 1 | PASS |
| "Oracle Value-Added Reseller" | ORACLE_FACT_BASELINE Section 1 | PASS |
| "over 23 years" | ORACLE_FACT_BASELINE Section 13 (founded 2002) | PASS |
| "50+ Senior Consultants" | ORACLE_FACT_BASELINE Section 13 (F2 — Hein Blignaut) | PASS |
| Five published OPN expertise areas | ORACLE_FACT_BASELINE Section 2 | PASS |
| Six Oracle awards (2015–2024) | ORACLE_FACT_BASELINE Section 3 | PASS |
| OIC as mandatory in all Fusion implementations | ORACLE_FACT_BASELINE Section 7; RedPath Mining RFI line 109 | PASS |
| FBDI as standard data migration tool | ORACLE_FACT_BASELINE Section 17; RedPath Mining RFI line 111 | PASS |
| Trial Balance reconciliation before financial load | RedPath Mining RFI line 112 | PASS |
| Hyper-care: ~3 months full team | HB V5.0 lines 365–367 | PASS |
| Critical care: ~6 months reduced team | HB V5.0 lines 365–367 | PASS |
| OUM + Customer Success Navigator basis | HB V5.0 line 505; RedPath Mining RFI line 158 | PASS |
| "Oracle E-Business Suite Migration to OCI" | ORACLE_FACT_BASELINE Section 2 (published expertise) | PASS |
| "Oracle Cloud Infrastructure Migration" | ORACLE_FACT_BASELINE Section 2 (published expertise) | PASS |
| OCI SOC Bridge Letters (June 2025) | ORACLE_FACT_BASELINE Section 6 | PASS |
| SAP Payroll integration (multiple times) | ORACLE_FACT_BASELINE Section 14 | PASS |
| PaySpace as integration target | ORACLE_FACT_BASELINE Section 12 | PASS |
| AOR data security model for HCM | RedPath Mining RFI line 118 | PASS |
| Oracle Guided Learning reference | RedPath Mining RFI line 202 (indirect) | PASS — D-W5-002 CLOSED: softened to available option where licensed and in scope |
| Multi-country blueprint principle | HB V5.0 lines 337–339 (synthesised) | PASS — D-W5-001 CLOSED: confirmed with "typically" and "subject to client operating model" qualifiers |

---

# Appendix C — Governance Review Summary

| Governance rule | Applied | Notes |
|---|---|---|
| "Oracle Level 1 Partner" only — no "Gold Partner" | YES | Used throughout. No "Gold" anywhere. |
| "50+ Senior Consultants" only | YES | Used in Sections 2.1 and 15.2. |
| "over 23 years" only | YES | Used in Sections 1 and 15.1. |
| No "22 years" | YES | Not used. |
| No "110 Senior Consultants" | YES | Not used. |
| DFA excluded | YES | Not cited anywhere in document. |
| SARB excluded | YES | Not cited anywhere. |
| Nala: no 8-country claim | YES | Nala not cited in this document. |
| KPMG: source evidence only — not cited as reference | YES | Not cited by name. |
| BEE Level 3 only | YES | BEE not cited (methodology document — BEE content not appropriate). |
| No duplicate of W2S1-004 ITIL / CSI / SLA content | YES | ITIL, CSI, P1–P4 SLA tiers, CMDB governance not reproduced. Section 14.3 references W2S1-004 without duplicating it. |
| No duplicate of W2S1-003 DBA content | YES | DBA team claims not reproduced. Section 13.4 references W2S1-003 without duplicating it. |
| Implementation footprint ≠ supported footprint | YES | Document describes delivery methodology. Steady-state support deferred to W2S1-004. |
| Scope ends at Hyper-care | YES | Section 9.3 confirms transition to W2S1-004. |
| No new claims outside evidence base | YES | All claims traceable to confirmed source. D-W5-001 and D-W5-002 both CLOSED. |
| approved_for_reuse: Yes — set by BU Lead | YES | Approved by Hein Blignaut 2026-06-12. |

---

*Extraction date: 2026-06-12 | Extracted by: Claude (AI — Wave 2) | Source hierarchy: ORACLE_FACT_BASELINE → Readiness Report → HB V5.0 → RedPath Mining RFI → Approved W2S1-001/002/003/004*
*Approved by: Hein Blignaut | Approval date: 2026-06-12 | Oracle Wave 2 Deliverable 5 of 5 — Wave 2 COMPLETE.*
