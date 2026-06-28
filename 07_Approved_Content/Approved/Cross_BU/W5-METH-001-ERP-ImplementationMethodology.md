---
document_id: W5-METH-001-ERP-ImplementationMethodology
title: "APPSolve ERP Implementation Methodology (Platform-Agnostic)"
version: "1.0 APPROVED"
source_status: Approved
approved_for_reuse: Yes
lifecycle_status: APPROVED
approved_by: "Hein Blignaut"
approval_date: "2026-06-14"
reviewed_by: "Hein Blignaut"
review_date: "2026-06-14"
derived_from: "W2S1-005-ORA-ImplementationMethodology (approved 2026-06-12) — de-branded and generalised"
evidence_basis:
  - "Hollywood Bets Oracle HCM Implementation (April 2023 — Won; HIST-007)"
  - "Interconnect Systems Acumatica Field Services Implementation (Won; W1S2-006)"
  - "HyDac Acumatica Manufacturing + BeBanking Implementation (Dec 2024 — Won; HIST-005)"
  - "RedPath Mining Oracle HCM (in delivery; RFI March 2026 — HIST-008)"
created: "2026-06-14"
created_by: "Claude (AI — WP7 W5-METH-001 de-brand from W2S1-005)"
wave: "Wave 5"
bu: "Cross-Platform (Oracle, Acumatica, OCI, OIC, BeBanking)"
kb_destination: "05_Methodologies/Implementation/W5-METH-001-ERP-ImplementationMethodology.md"
platform_appendices:
  - "Appendix A: Oracle-specific additions (OUM alignment, FBDI, Modern Best Practices)"
  - "Appendix B: Acumatica-specific additions (import scenarios, Acumatica University)"
  - "Appendix C: OCI/OIC-specific additions"
  - "Appendix D: BeBanking-specific additions"
usage_note: "Use this document as the primary methodology asset for ALL tender types. Select applicable platform appendix. W2S1-005 remains the Oracle-specific detailed version for Oracle-only tenders where Oracle branding is appropriate."
---

> **APPROVED — approved_for_reuse: Yes — Approved by Hein Blignaut (BU Lead), 2026-06-14**
> WP7 Wave 5 Deliverable. Platform-agnostic. Use for Acumatica, OCI/OIC, BeBanking, and multi-platform tenders.
> For Oracle-only tenders where Oracle branding is appropriate, W2S1-005 may still be used directly.

---

# APPSolve ERP Implementation Methodology
**APPSolve Proprietary Delivery Framework — All Platforms**

---

## 1. Executive Summary

APPSolve is a technology implementation partner with over 23 years of experience delivering enterprise ERP, integration, and banking solutions across Southern Africa and internationally. Our implementation methodology is a structured, iterative delivery framework built from more than two decades of real-world project delivery across Oracle Fusion Cloud, Oracle E-Business Suite (EBS), Acumatica Cloud ERP, Oracle Cloud Infrastructure (OCI), Oracle Integration Cloud (OIC), and BeBanking Host-to-Host payment solutions.

The APPSolve implementation methodology guides every engagement from initial mobilisation through to a supported production go-live and hypercare stabilisation. It provides clients, project sponsors, and procurement evaluators with a clear, repeatable process that manages scope, quality, risk, and business change at every stage of delivery.

Our methodology is not a generic project management approach — it is a technology-native delivery framework that incorporates modern ERP best practices, iterative configuration cycles, structured data migration, and integration-first thinking as core structural components. It has been applied and refined across Oracle Fusion HCM, Finance, Procurement, and PPM; Oracle EBS R12/R12.2; Acumatica Manufacturing, Distribution, and Field Services; OCI migration programmes; and BeBanking H2H banking implementations.

**Platform-specific tools and standards** are documented in the Appendices of this document. The core six-phase methodology and delivery philosophy apply equally across all platforms.

---

## 2. APPSolve Delivery Philosophy

### 2.1 Senior-Only Delivery

APPSolve deploys senior consultants on all implementation engagements. Our 50+ Senior Consultants each bring 10 or more years of enterprise technology experience. There are no junior resources assigned to implementation delivery without senior oversight. This approach reduces delivery risk, accelerates design decisions, and ensures clients engage with experienced practitioners at every project touchpoint.

### 2.2 Standard Configuration First

APPSolve's default position on every engagement is to adopt the platform's standard, out-of-the-box configuration before introducing customisation or development. Modern ERP platforms are built around proven business best practices. Maximising standard functionality reduces implementation cost, lowers upgrade risk, and ensures clients benefit from the platform vendor's continuous product investment. Customisation is introduced only when a confirmed, justified business requirement cannot be met through configuration.

### 2.3 Iterative Prototype-to-Production

Rather than designing on paper and building from a fixed specification, APPSolve uses an iterative approach: the solution is built, demonstrated, refined, and validated in cycles. Each iteration — a Conference Room Pilot (CRP) — brings stakeholders progressively closer to the final production solution. This approach surfaces issues early, keeps the business engaged throughout the project, and ensures the delivered solution reflects operational reality rather than abstract requirements.

### 2.4 Customer Ownership from Day One

The APPSolve methodology transfers solution ownership to the client organisation progressively throughout the project — not only at go-live. Super users are involved in design decisions from the Prototype phase. Data migration is customer-led with APPSolve guidance. UAT is client-driven. The objective is a client team that is confident, capable, and operationally self-sufficient from the first day of steady-state operation.

### 2.5 Cloud Readiness Embedded

APPSolve embeds cloud readiness into every engagement from the Mobilize phase. For cloud ERP platforms (Oracle Fusion Cloud, Acumatica), this includes environment management strategy, SaaS configuration governance, and integration architecture. For hybrid or on-premise-to-cloud migrations, a migration readiness assessment is conducted in the early phases.

### 2.6 Change Management Throughout

Change management is not a separate workstream that happens at the end of the project. APPSolve embeds organisational change management principles across all six delivery phases — from stakeholder identification in Mobilize through to adoption measurement in Evolve.

---

## 3. Implementation Methodology Overview

The APPSolve implementation methodology is structured across six delivery phases, followed by a transition to the steady-state support model:

```
Mobilize → Scope & Design → Prototype → Validate → Deploy → Evolve
```

Each phase has defined entry criteria, activities, and exit deliverables. Phases do not run in strict sequence — technical delivery, data preparation, and integration build activities often run in parallel with design and configuration work.

| Phase | Key Activities |
|---|---|
| **Mobilize** | Team assembly; initiative charter; work plan; kick-off |
| **Scope & Design** | Scope confirmation; best-practices alignment; data assessment; workshop scheduling |
| **Prototype** | Design workshops; CRP1 (Prototype 1); CRP2 (Prototype 2); end-to-end integration testing |
| **Validate** | Final validation; documentation finalisation; go-live preparation |
| **Deploy** | Production build; user enablement; training delivery; go-live execution |
| **Evolve** | Hypercare; critical care; transition to steady-state support |

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
- Budget and commercial model

The charter is agreed and signed off by the implementation sponsor before Scope & Design begins.

### 4.3 Work Plan Definition

A detailed project work plan is produced, covering all activities and tasks required to achieve the programme objectives. Tasks are assigned to named resources. The work plan supports workload management and progress tracking and is aligned to agreed milestone dates.

### 4.4 Kick-off

An official project kick-off is hosted with the APPSolve Project Manager, the client project sponsor, and all key stakeholders. Sponsor attendance at kick-off is a key success factor — it signals executive commitment and establishes the governance tone for the engagement.

---

## 5. Scope and Design Phase

The Scope and Design phase confirms the project boundary, aligns the solution to ERP best practices, and prepares the environment and teams for structured design workshops.

### 5.1 Scope Confirmation

Project scope is formally confirmed, with inclusions and exclusions documented. Scope is aligned to the platform's standard best-practice process flows as the default functional baseline. Where business requirements differ from the standard configuration, these are recorded as decision points for the design workshops rather than resolved unilaterally.

### 5.2 ERP Best Practices Alignment

APPSolve uses the relevant platform's best-practices framework and starter configuration as the starting point for every engagement. The starter configuration provides a working, pre-configured system instance before detailed design begins — allowing the client team to react to a concrete solution rather than abstract requirements documents. This reduces workshop time and accelerates design decisions.

*(See Appendices A and B for platform-specific best-practice frameworks.)*

### 5.3 Data Requirements and Assessment

Data readiness is assessed at the start of the engagement:
- Existing data completeness is evaluated against the target system's data model requirements
- Data migration templates are provided for each module in scope
- Data gaps are identified and a remediation plan is agreed with the client
- The client is accountable for data accuracy; APPSolve is accountable for loading structure, template guidance, and delivery to the correct target

### 5.4 Workshop Scheduling and Environment Preparation

A schedule of design workshops is produced and calendar invites issued in advance. Test environments are configured and an environment management strategy is agreed to govern the use of development, test, and production instances throughout the engagement.

---

## 6. Prototype Phase

The Prototype phase is the iterative core of the APPSolve methodology. Two full prototype cycles — CRP1 and CRP2 — are completed before the solution advances to final validation.

### 6.1 Design Governance

A solution authority is established at the start of the Prototype phase — meets regularly to ensure design decisions align to project objectives and business outcomes; is empowered to make final design decisions; receives regular updates on key decisions and their business implications.

### 6.2 Conference Room Pilot 1 (CRP1 — Prototype 1)

CRP1 focuses on the core business processes in scope. The system is configured to the agreed design decisions and demonstrated to business stakeholders in a structured walkthrough. Issues and gaps identified in CRP1 are logged, assigned owners, and resolved before CRP2.

**CRP1 activities:**
- Core module configuration
- Initial data load (sample or legacy data)
- Process walkthroughs with business teams
- Issue and gap logging
- Design decision finalisation

### 6.3 Conference Room Pilot 2 (CRP2 — Prototype 2)

CRP2 presents the refined solution incorporating all CRP1 resolutions. It is a near-complete prototype of the production system. End-to-end process flows are demonstrated, including integrations and data migration.

**CRP2 activities:**
- Refined configuration incorporating all CRP1 changes
- End-to-end integration testing
- Data migration dry run
- Performance baseline
- Sign-off by solution authority

---

## 7. Validate Phase

The Validate phase confirms the solution is complete, tested, and ready for production deployment.

### 7.1 User Acceptance Testing (UAT)

UAT is client-led. APPSolve provides:
- UAT test scripts covering all in-scope business processes
- Test environment configuration and data
- Support desk for UAT defect logging and resolution
- UAT status tracking and reporting

UAT is complete when all high-priority test scripts pass and the client's UAT signatory formally accepts the solution.

### 7.2 Documentation Finalisation

Configuration documentation, user guides, and training materials are finalised during the Validate phase. Documentation is client-owned — APPSolve prepares it; the client maintains it.

### 7.3 Go-Live Readiness Assessment

Before go-live approval, APPSolve conducts a formal Go-Live Readiness Assessment covering: system configuration complete; data migration tested and approved; integrations live and tested; training delivered and super users signed off; business continuity plan agreed; support model activated.

---

## 8. Deploy Phase

The Deploy phase executes the go-live and transitions the client from project mode to operational mode.

### 8.1 Production Build

Final production environment configuration is applied. Data migration is executed from the approved legacy extract. Integrations are activated and tested against production endpoints.

### 8.2 Training Delivery

End-user training is delivered using a **train-the-trainer** model:
1. APPSolve trains the client's designated super users (trainers)
2. Super users deliver role-based training to end users
3. APPSolve provides training quality assurance — observes sessions and addresses gaps
4. eLearning or system-guided training tools are configured where available *(see Appendices)*

### 8.3 Go-Live Execution

Go-live is executed according to the agreed cutover plan. Key activities:
- Legacy system cutover (agreed date/time)
- Production data migration execution
- Integration activation and validation
- Go-live checkpoint — confirmed by client sponsor before opening to end users
- Hypercare support activated from go-live moment

### 8.4 Change Management at Deploy

End-user communications are issued before go-live. Change champions (super users) are briefed and positioned as the first point of contact for end-user questions. Resistance management plans are activated as needed.

---

## 9. Evolve Phase — Hypercare and Steady-State Transition

The Evolve phase begins at go-live and runs until the client has stabilised and transitioned to steady-state support.

### 9.1 Hypercare

Hypercare is a dedicated post-go-live stabilisation period (typically 4–8 weeks). During hypercare:
- APPSolve provides on-site or near-site senior consultant availability
- Same-day response to all production issues
- Daily stand-up with client key users
- Issue log maintained and reviewed daily
- Knowledge transfer to client super users

Hypercare closes when no critical issues remain open and the client team is operationally self-sufficient.

### 9.2 Steady-State Transition

At hypercare closure, the client transitions to the APPSolve managed support model. A handover meeting between delivery and support teams ensures full context transfer.

---

## 10. Project Governance Framework

### 10.1 Project Management Structure

| Role | Responsibility |
|---|---|
| APPSolve Project Manager | Delivery ownership; scope management; risk management; client reporting |
| APPSolve Practice Lead | Technical oversight; quality assurance; escalation point |
| APPSolve Account Manager | Commercial management; client relationship; escalation |
| Client Project Sponsor | Executive ownership; decision authority; change approval |
| Client Project Manager | Day-to-day client coordination; resource management |
| Client Super Users | Design participation; UAT execution; train-the-trainer delivery |

### 10.2 Steering Committee

A Steering Committee meets regularly (typically monthly) with attendance from APPSolve and client executive representatives. The Steering Committee reviews:
- Project status and milestone progress
- Risk and issue register
- Scope change requests
- Commercial and contractual matters

### 10.3 RACI

A RACI matrix is produced during Mobilize and maintained throughout the project. All key activities and decisions are mapped to Responsible, Accountable, Consulted, and Informed parties.

### 10.4 Change Control

All changes to agreed project scope, budget, or timeline are managed through a formal change control process:
1. Change Request submitted by either party
2. Impact assessment by APPSolve
3. Change approved/rejected by client project sponsor
4. Change implemented only after written approval

---

## 11. Data Migration Approach

Data migration is a client-critical activity managed as a structured workstream from Scope & Design through Deploy.

### 11.1 Migration Approach

APPSolve follows a three-stage migration approach:
1. **Extract** — client extracts legacy data into agreed templates (APPSolve provides templates)
2. **Cleanse** — client cleanses data; APPSolve provides validation rules and reviews output
3. **Load** — APPSolve loads data using platform-native import tools; validation report produced after each load

*(See Appendices for platform-specific migration tools: FBDI for Oracle; Import Scenarios for Acumatica.)*

### 11.2 Migration Testing

Data migration is executed and tested in the Prototype phase (sample load), the Validate phase (full UAT load), and the Deploy phase (production load). Three migration cycles are planned — the production load should be the third or fourth execution, ensuring a practised and validated process.

---

## 12. Integration Approach

### 12.1 Integration Design Principles

- **Integration-first design:** Integration requirements are identified in Scope & Design and designed before configuration begins
- **Standard connectors first:** Platform-native integration tools are preferred over bespoke middleware
- **Documented interfaces:** All interfaces are formally specified in an Interface Control Document (ICD)
- **Tested in isolation and end-to-end:** Each interface is unit-tested before end-to-end testing

*(See Appendices for platform-specific integration tools.)*

---

## 13. Quality Assurance

### 13.1 Quality Gates

Quality gates are applied at each phase exit:
- **Mobilize exit:** Initiative charter signed; team confirmed; work plan agreed
- **Scope & Design exit:** Scope confirmed; data requirements documented; workshop schedule agreed
- **Prototype exit (CRP2):** All CRP1 issues resolved; end-to-end tested; design authority signed off
- **Validate exit:** UAT passed; documentation complete; go-live readiness confirmed
- **Deploy exit:** Production go-live achieved; hypercare activated
- **Evolve exit:** Hypercare issues resolved; client self-sufficient; steady-state support active

### 13.2 Internal Review Process

APPSolve applies an internal peer review process at each quality gate — a senior consultant not directly assigned to the project reviews key deliverables and raises issues before the gate is presented to the client. This provides a quality assurance function independent of the delivery team.

---

## 14. Pre-Tender Checks

Before using this document in any external tender submission:

| Check | Action |
|---|---|
| Select applicable platform appendix | Appendix A (Oracle), B (Acumatica), C (OCI/OIC), D (BeBanking) |
| Confirm named references cited are approved for this tender | Refer to NAMED_REFERENCE_MATRIX.md |
| BEE Level 3 confirmed (expires 2026-07-31) | Annual compliance check |
| OPN certification current (if Oracle tender) | Annual OPN revalidation |
| Acumatica Gold Partner status current (if Acumatica tender) | Annual revalidation |

---

## Appendix A — Oracle-Specific Additions

*Use when this methodology is applied to Oracle Fusion Cloud or Oracle EBS implementations.*

### A.1 Methodology Framework Alignment

APPSolve's Oracle implementations are structured in alignment with the **Oracle Unified Method (OUM)** — Oracle's own methodology framework for cloud and on-premise implementations — combined with the **Oracle Customer Success Navigator** for Fusion Cloud engagements. This alignment ensures APPSolve's delivery approach is consistent with Oracle's own quality benchmarks.

### A.2 Oracle-Specific Phase Tools

| Phase | Oracle Tool |
|---|---|
| Scope & Design | Oracle Modern Best Practices library; Oracle Starter Configurator |
| Data Migration | Oracle FBDI (File-Based Data Import) templates per module |
| Integration | Oracle Integration Cloud (OIC) as preferred middleware |
| Training | Oracle Guided Learning (where licensed); Oracle University |
| Monitoring | Oracle Cloud Console; OCI Monitoring |

### A.3 Oracle SaaS Environment Model

For Oracle Fusion Cloud engagements, environment management follows Oracle's three-environment model:
- **Development:** Configuration and build
- **Test/UAT:** CRP1, CRP2, UAT
- **Production:** Go-live and steady state

Quarterly Fusion updates (Oracle Cloud Update cycles) are managed by APPSolve as part of the implementation scope for hypercare-period updates.

---

## Appendix B — Acumatica-Specific Additions

*Use when this methodology is applied to Acumatica Cloud ERP implementations.*

### B.1 Acumatica Delivery Approach

APPSolve delivers Acumatica implementations as an **Acumatica Gold Partner**, drawing on Acumatica's implementation best practices and the APPSolve Acumatica delivery playbook refined across Manufacturing, Distribution, Field Services, Professional Services, and inter-governmental sector engagements.

### B.2 Acumatica-Specific Phase Tools

| Phase | Acumatica Tool |
|---|---|
| Scope & Design | Acumatica module selection guide; configuration workbook |
| Data Migration | Acumatica Import Scenarios (native tool); Excel import templates |
| Integration | Acumatica REST API / OData endpoints; BeBanking H2H connector (where applicable) |
| Training | Acumatica University (self-paced learning); APPSolve role-based training guides |
| Configuration | Acumatica snapshots (configuration backup before major changes) |

### B.3 Acumatica SaaS Environment Model

For Acumatica Cloud (SaaS) engagements:
- **Sandbox environment:** Configuration, testing, UAT
- **Production environment:** Go-live and steady state
- **Automated backup:** Acumatica platform provides daily automated backups

Acumatica major releases (twice yearly) are managed by APPSolve post-implementation — see W5-ACU-001 for the release management process.

### B.4 Acumatica Licensing

APPSolve, as an authorised Acumatica Value-Added Reseller, manages Acumatica licensing procurement on the client's behalf. License provisioning is coordinated during the Mobilize phase to ensure environments are available before Scope & Design begins.

---

## Appendix C — OCI / OIC-Specific Additions

*Use when this methodology covers Oracle Cloud Infrastructure (OCI) deployments or Oracle Integration Cloud (OIC) implementations.*

### C.1 OCI Deployment Approach

For OCI workload migrations and cloud infrastructure projects, APPSolve applies the standard six-phase framework with OCI-specific activities:

| Phase | OCI Activity |
|---|---|
| Scope & Design | Cloud architecture design; workload assessment; network topology; security model |
| Prototype | Sandbox environment provisioning; connectivity testing |
| Validate | Performance benchmarking; security validation; DR testing |
| Deploy | Production environment provisioning; workload migration; DNS cutover |
| Evolve | Cost optimisation; monitoring setup; steady-state operations handover |

### C.2 OIC Integration Projects

For OIC integration implementations:
- Integration interface specifications documented in Interface Control Document (ICD)
- Integrations built in OIC Development environment; tested in UAT environment
- Production deployment via OIC release packaging
- Monitoring configured in OIC Console + OCI Monitoring

---

## Appendix D — BeBanking-Specific Additions

*Use when this methodology covers BeBanking Host-to-Host (H2H) payment implementations.*

### D.1 BeBanking Implementation Approach

BeBanking H2H implementations follow the APPSolve six-phase methodology adapted for banking integration delivery:

| Phase | BeBanking Activity |
|---|---|
| Mobilize | Banking partner liaison; bank onboarding initiation; ERP connector selection |
| Scope & Design | Payment module scoping; bank format requirements; ERP integration design |
| Prototype | BeBanking sandbox configuration; test payment file generation; bank acknowledgement testing |
| Validate | End-to-end payment file testing with banking partner; reconciliation testing |
| Deploy | Production BeBanking configuration; first live payment run; reconciliation validation |
| Evolve | Hypercare on payment processing; bank reconciliation validation |

### D.2 Banking Partner Coordination

BeBanking implementation requires parallel coordination with the client's banking partner(s). APPSolve manages the banking onboarding process and provides the client with required bank account mandate documentation and payment file format specifications.

---

## Section 17 — Approval Record

| Field | Value |
|---|---|
| Document ID | W5-METH-001-ERP-ImplementationMethodology |
| Title | APPSolve ERP Implementation Methodology (Platform-Agnostic) |
| Version | 1.0 |
| Derived from | W2S1-005 (Oracle Implementation Methodology — approved 2026-06-12) |
| Wave | Wave 5 |
| Work Package | WP7 |
| Approved by | Hein Blignaut (BU Lead) |
| Approval date | 2026-06-14 |
| approved_for_reuse | **Yes** |
| Scope | Platform-agnostic core + Oracle / Acumatica / OCI/OIC / BeBanking appendices |
| KB destination | `05_Methodologies/Implementation/W5-METH-001-ERP-ImplementationMethodology.md` |
| Next review | 2027-06-14 (annual) |

---

*W5-METH-001 v1.0 — Approved 2026-06-14 by Hein Blignaut. WP7 Wave 5. Platform-agnostic ERP implementation methodology. Derived from W2S1-005. Use for all non-Oracle or multi-platform tenders. Select applicable appendix.*
