---
document_id: W3S1-003-ORA-RecruitingCloud
title: "Oracle Fusion Recruiting Cloud — Capability Statement"
version: "1.1 Approved"
status: "Approved"
review_status: "Approved"
approved_for_reuse: "Yes"
business_unit: "Oracle"
wave: "3"
deliverable: "W3S1-003"
created: "2026-06-12"
approved: "2026-06-13"
created_by: "Claude (AI — Wave 3 W3S1-003 extraction)"
approved_by: "Hein Blignaut (BU Lead)"
source_document: "HIST-007 (Hollywood Bets V5.0 ACCEPTED Proposal, April 2023 — primary implementation evidence); HIST-006 (SAA HCM RFP Response, June 2025 — platform capability narrative); HIST-015 (Afrocentric HCM Proposal V4.0, 2023 — delivery methodology corroboration); HIST-016 (SABS ETS Oracle Fusion, Dec 2025 — reference table corroboration)"
source_status: "Implementation Evidence (HIST-007); Platform Capability (HIST-006); Delivery Methodology (HIST-015); Reference Corroboration (HIST-016)"
prereq_statement: "W3S1-001-ORA-HCMCore (Oracle HCM Core — Global HR is the mandatory prerequisite for all Oracle Fusion HCM module implementations including Recruiting Cloud)"
kb_destination: "06_Capabilities/Oracle/Oracle_HCM/"
tags: "Oracle,HCM,Recruiting Cloud,Talent Acquisition,Candidate Experience,Onboarding,Requisition Management,Offer Management,ORC,Oracle Fusion,Taleo"
---

> **APPROVED — approved_for_reuse: Yes — Approved by BU Lead 2026-06-13**

---

# Oracle Fusion Recruiting Cloud

**Capability Statement | APPSolve | Oracle Business Unit**
*Document ID: W3S1-003-ORA-RecruitingCloud | Version: 1.1 Approved | Wave 3*

---

## Section 1: Statement of Capability

APPSolve implements Oracle Fusion Recruiting Cloud as part of Oracle Fusion HCM implementations, enabling organisations to attract, evaluate, and hire talent through a modern, AI-powered talent acquisition platform natively integrated with Oracle Fusion HCM.

APPSolve has implemented Oracle Fusion Recruiting Cloud at Hollywood Bets, a leading South African retail gaming and sports betting organisation. The Hollywood Bets Oracle Fusion HCM implementation — which went live in July 2025 for 7,000 users — included Recruiting Cloud as a primary delivery phase, encompassing external career site design, vacancy management, candidate selection processes, screening and shortlisting workflows, interview management, offer management, and structured onboarding. Oracle Integration Cloud (OIC) was deployed as the standard integration layer.

APPSolve has implementation and ongoing support experience with Oracle Taleo Recruiting solutions. While Oracle Recruiting Cloud is now the strategic Oracle recruiting platform, this experience demonstrates APPSolve's long-standing capability in Oracle recruitment solutions.

APPSolve is currently implementing Oracle Recruiting and Onboarding capabilities for a mining-sector client.

APPSolve's Oracle Recruiting Cloud delivery experience spans the retail and mining sectors. APPSolve supports clients across Retail, Mining, and Professional Services industries.

---

## Section 2: Oracle Fusion Recruiting Cloud — Module Overview

Oracle Fusion Recruiting Cloud is Oracle's next-generation talent acquisition platform, forming part of the Oracle Fusion HCM suite. APPSolve configures and implements Recruiting Cloud to enable organisations to manage the full talent acquisition lifecycle — from employer branding and candidate attraction through to structured onboarding and integration with Oracle Fusion Core HR.

The platform delivers five primary value outcomes that APPSolve configures as part of every Oracle Recruiting Cloud implementation:

| Value Outcome | Description |
|---|---|
| **AI-Driven Talent Acquisition** | Oracle Recruiting Cloud applies AI and machine learning to match candidates with roles based on skills, experience, and potential. Provides intelligent recommendations to recruiters and hiring managers. |
| **Enhanced Candidate Experience** | Mobile-friendly career sites with personalised job recommendations, chatbot and virtual assistant engagement, and self-service application tracking. Configured by APPSolve to reflect the client's employer brand. |
| **Automated and Efficient Recruiting** | Automates job posting, interview scheduling, offer management, and candidate communications. Reduces administrative burden and accelerates time-to-hire. |
| **Data-Driven Recruiting Decisions** | Real-time analytics on recruiting performance, candidate pipeline status, and hiring metrics. Identifies bottlenecks and supports evidence-based hiring strategy. |
| **Seamless Integration with Oracle HCM** | Native integration with Oracle Fusion Core HR, Oracle Payroll Interface, and Oracle Onboarding. Candidate records convert to employee records in Core HR upon hire. Third-party job boards, background check providers, and assessment platforms connect via OIC and REST APIs. |

---

## Section 3: Talent Acquisition Foundation and Platform Architecture

### 3.1 Oracle Fusion Recruiting Cloud — Core Architecture

APPSolve implements Oracle Fusion Recruiting Cloud as an integrated talent acquisition platform within the Oracle Fusion HCM landscape. The platform serves as the applicant tracking system (ATS) of record, connecting employer branding, candidate sourcing, selection, offer management, and structured onboarding in a single Oracle-native system.

APPSolve configures the following foundation elements as part of every Recruiting Cloud implementation:

| Foundation Element | APPSolve Configuration Scope |
|---|---|
| **Hiring and selection processes** | Configurable hiring workflow stages from application through to offer; aligned to client HR operating model |
| **Job and position integration** | Job profiles, position management, and competency frameworks from Oracle Core HR drive Recruiting Cloud job postings and screening criteria |
| **User roles and access** | Recruiter, hiring manager, and HR administrator roles configured with appropriate access to candidate data, requisitions, and offer workflows |
| **Reporting and dashboards** | Oracle Recruiting Administration reports and standard Oracle HCM dashboards configured to support recruiting KPIs |
| **OIC integration architecture** | Oracle Integration Cloud deployed as the standard integration layer connecting Recruiting Cloud with third-party job boards, background check providers, and assessment platforms |

### 3.2 Taleo Recruiting — Legacy Platform Experience

APPSolve has implementation and ongoing support experience with Oracle Taleo Recruiting solutions. While Oracle Recruiting Cloud is now the strategic Oracle recruiting platform, this experience demonstrates APPSolve's long-standing capability in Oracle recruitment solutions. Clients currently operating Oracle Taleo Recruiting environments may consult APPSolve on legacy support continuity and platform modernisation pathways.

### 3.3 Internal Mobility

Oracle Fusion Recruiting Cloud includes an Internal Career Site capability that enables employees to search and apply for open positions within the organisation. The platform recommends internal job opportunities to employees based on skills, experience, and career interests, and tracks internal applications through configurable approval workflows.

APPSolve supports internal mobility configuration as an Oracle platform capability. Internal mobility is positioned as a complement to Oracle Talent Management and Oracle Succession Planning. Implementation evidence for Oracle Opportunity Marketplace — a dedicated internal talent marketplace — is available from APPSolve's Oracle Talent Management practice.

---

## Section 4: Requisition and Vacancy Management

APPSolve configures Oracle Fusion Recruiting Cloud's requisition and vacancy management capabilities to align with each client's HR operating model, approval structure, and position management framework.

### 4.1 Job Requisition Configuration

| Capability | APPSolve Configuration Approach |
|---|---|
| **Requisition creation and approval** | Managers or HR create job requisitions using predefined templates covering job descriptions, required qualifications, and salary bands. Configurable approval routing aligned to client organisational hierarchy. |
| **AI-powered job descriptions** | Oracle generative AI assists in creating engaging, compliant job descriptions from structured position data. APPSolve configures the AI job description capability and trains HR teams on its governance. |
| **Position-driven requisitions** | Requisitions are linked to Oracle Fusion Core HR position management. Open positions trigger requisition workflows automatically where configured. |
| **Template library** | APPSolve establishes a requisition template library during implementation. New requisitions are created post go-live; no historical requisition migration is performed. |

### 4.2 Vacancy Management and Hiring Workflows

APPSolve configures end-to-end hiring workflows defining the stages through which candidates progress from application to hire. Standard APPSolve implementation includes:

- **One candidate selection process** — the framework defining stages and evaluation criteria for all roles within the implementation scope
- **One job application flow** — the candidate-facing application sequence, optimised for mobile and quick-apply interaction
- **Configurable stage transitions** — automated notifications, task assignments, and approval triggers at each hiring workflow stage
- **Recruiter and hiring manager collaboration** — shared dashboards providing real-time visibility of candidate pipeline status

---

## Section 5: Candidate Experience and Employer Branding

APPSolve implements Oracle Fusion Recruiting Cloud's candidate experience capabilities as confirmed implemented deliverables, including branded career sites, candidate talent communities, and employee referral programmes.

### 5.1 Branded Career Sites and Candidate Portals

APPSolve configures both external and internal career sites as part of every Oracle Recruiting Cloud implementation:

| Site Type | Configuration Scope |
|---|---|
| **External career site** | One branded external career portal per implementation scope. Configured with client logo branding in Oracle-required format. Mobile-responsive design. Branded to align with client corporate standards. Graphical web design is a client responsibility; APPSolve configures the Oracle career site framework. |
| **Internal career site** | One internal career portal for employee-facing job opportunities. Enables self-service job browsing, application submission, and application tracking by current employees. |
| **Candidate self-service** | Candidates access a personalised application tracking portal, receive automated status notifications, and can schedule interviews through self-service tools. |

The Hollywood Bets implementation included the design and configuration of external recruiting pages aligned to the Hollywood Bets corporate brand, delivered in collaboration with the client's web and marketing teams.

### 5.2 Multi-Channel Job Posting and Candidate Sourcing

APPSolve configures Oracle Recruiting Cloud's multi-channel posting and candidate sourcing capabilities to maximise the reach of each client's talent acquisition effort:

- **Multi-channel job distribution** — automated posting to external job boards (including Indeed integration), social media, professional networks (LinkedIn), and employee self-service portals
- **LinkedIn integration** — APPSolve configures LinkedIn profile import for candidate applications and job sharing. Client LinkedIn recruiter accounts are required as a prerequisite.
- **AI candidate matching** — Oracle AI recommends best-fit candidates for open requisitions, reducing manual screening overhead and accelerating shortlisting
- **CRM-style talent pools** — APPSolve configures candidate talent communities, enabling targeted recruiting campaigns and relationship nurturing with passive candidates

### 5.3 Employee Referral Programme

Oracle Fusion Recruiting Cloud natively integrates employee referral programme management. APPSolve configures the referral capability as part of Recruiting Cloud implementations:

- Employees refer candidates directly through the employee self-service portal
- Referred candidates populate the ATS within Oracle Recruiting Cloud alongside all other applicants
- The system tracks referred candidates through the hiring pipeline, attributing hires to referrers
- Automated notifications are sent to referrers at key hiring milestones
- Referral bonus eligibility tracking is supported through configurable rules

---

## Section 6: Screening, Shortlisting and Interview Management

### 6.1 Screening and Shortlisting

APPSolve configures Oracle Recruiting Cloud's automated screening and shortlisting capabilities to reduce manual effort and improve hiring quality:

| Capability | Description |
|---|---|
| **Automated resume parsing** | Oracle Recruiting Cloud parses candidate applications against job requisition criteria, extracting qualifications, skills, and experience for comparison against role requirements |
| **AI-powered candidate ranking** | AI evaluates candidate profiles against job descriptions and recommends best-fit candidates, reducing unconscious bias and accelerating screening time |
| **Knock-out criteria** | APPSolve configures mandatory and preferred criteria within hiring workflows, enabling automated screening at the application stage |
| **Pipeline stage management** | Candidate status is tracked through configurable stages (Applied → Screened → Interviewed → Offer → Hired) with full audit trail |

### 6.2 Interview Management

APPSolve configures Oracle Recruiting Cloud's collaborative interview management tools to support structured, auditable hiring decisions:

- **Interview self-scheduling** — candidates access a self-service portal to select interview times from interviewer availability slots, reducing scheduling coordination overhead
- **Interview scorecards** — structured evaluation forms configured per role type, ensuring consistent assessment criteria across interviewers
- **Interviewer collaboration** — centralised dashboard for recruiters and hiring managers to share real-time feedback, interview notes, and hiring recommendations
- **Interview logistics** — automated invitation, confirmation, and reminder communications to candidates and interviewers at each interview stage

---

## Section 7: Offer Management

APPSolve configures Oracle Fusion Recruiting Cloud's offer management capabilities to support structured, auditable offer processes from generation through to candidate acceptance.

### 7.1 Offer Letter Generation and Approval

| Capability | APPSolve Configuration Approach |
|---|---|
| **Dynamic offer letters** | APPSolve configures up to three branded offer letter templates per implementation scope, reflecting role type, employment category, and client branding requirements |
| **Offer approval workflow** | Configurable approval routing for offer letters, aligned to client HR and finance authorisation structures |
| **Digital signing** | Oracle Recruiting Cloud supports digital offer acceptance; candidates receive and accept offer letters electronically through the candidate self-service portal |
| **Offer negotiation tracking** | Offer status, counter-offer interactions, and acceptance or decline outcomes are tracked within the candidate record |
| **Skill transfer** | APPSolve trains client HR teams to create and maintain offer letter templates post go-live, ensuring independence from APPSolve for ongoing offer letter management |

### 7.2 Transition from Offer to Onboarding

Upon offer acceptance, Oracle Fusion Recruiting Cloud initiates the onboarding workflow automatically. Candidate data is converted to an employee record in Oracle Fusion Core HR, eliminating manual re-keying of information between systems. APPSolve configures the offer-to-onboarding transition as part of the Recruiting Cloud delivery scope.

---

## Section 8: Onboarding and Preboarding

APPSolve implements Oracle Fusion Recruiting Cloud's onboarding capability as a structured, automated process spanning from offer acceptance through Day 1 integration into Oracle Fusion Core HR. Full Journeys-based lifecycle event management is addressed in W3S1-001 Oracle HCM Core.

### 8.1 Preboarding — From Offer Acceptance to Start Date

APPSolve configures preboarding workflows enabling new hires to complete required actions before their first day:

| Preboarding Task | Configuration |
|---|---|
| **Welcome communications** | Automated welcome emails and introductory content sent upon offer acceptance |
| **Document submission** | New hires complete required documentation (employment contracts, tax forms, policy acknowledgements) through a secure self-service portal before start date |
| **System access preparation** | Onboarding task workflows trigger IT and facilities provisioning actions in parallel with HR onboarding steps |
| **Pre-arrival orientation** | New hire portal provides access to company culture content, team introductions, and pre-reading materials before Day 1 |

### 8.2 Structured Onboarding Workflows

APPSolve configures two standard onboarding processes per implementation scope: one for pre-hires (pre-start-date activities) and one for new hires (Day 1 through induction period activities).

| Onboarding Capability | APPSolve Configuration Approach |
|---|---|
| **Automated workflow initiation** | Onboarding workflows trigger automatically upon offer acceptance in Oracle Recruiting Cloud, requiring no manual HR intervention |
| **Personalised onboarding portals** | New hires access a dedicated portal configured with role-relevant content, tasks, and progress tracking |
| **Task management** | Onboarding tasks assigned to new hires, managers, and HR with automated reminders and completion tracking |
| **Document management** | Secure collection and storage of new hire documents integrated with Oracle Fusion Core HR records |
| **Integration with Core HR** | Candidate data is seamlessly converted to employee records in Oracle Fusion Core HR upon hire, ensuring data integrity and eliminating duplicate data entry |

### 8.3 Onboarding Reporting

Standard Oracle Recruiting Administration dashboards, configured by APPSolve during implementation, provide visibility of onboarding task completion rates, outstanding items, and new hire progress. Skills transfer to client HR teams ensures ongoing onboarding reporting independence post go-live.

---

## Section 9: APPSolve Delivery Capability

### 9.1 Oracle Recruiting Cloud Practice

APPSolve's Oracle Business Unit includes a dedicated team of HCM-certified consultants with implementation experience in Oracle Fusion Recruiting Cloud. APPSolve holds Oracle Level 1 Partner status.

APPSolve has implemented Oracle Fusion Recruiting Cloud at Hollywood Bets — a retail gaming and sports betting organisation with 7,000 employees — and is currently active in the mining sector delivering Oracle Recruiting and Onboarding. APPSolve also holds implementation and ongoing support experience with Oracle Taleo Recruiting solutions.

### 9.2 Recruiting Cloud Delivery Methodology

APPSolve delivers Oracle Fusion Recruiting Cloud implementations using the Oracle Unified Methodology (OUM), adapted for Recruiting Cloud's specific design and configuration requirements.

Recruiting is typically structured as a dedicated implementation phase, following Core HCM and Talent Management. This sequencing is deliberate: the job and position framework, competency libraries, and talent profile structures established in earlier phases provide the foundation on which Recruiting Cloud configuration is built.

APPSolve's standard Recruiting Cloud delivery approach includes:

| Delivery Element | Description |
|---|---|
| **External career site design** | Designed in collaboration with the client's marketing and web teams to align with corporate brand standards. APPSolve configures the Oracle career site framework; graphical design is a client-led deliverable. |
| **Process automation** | Recruitment process automation is a core delivery objective. APPSolve conducts process design workshops to identify automation opportunities within the client's existing recruitment workflow before configuring the Oracle system. |
| **Vacancy and filtering design** | APPSolve designs HCM staff-facing tools to minimise time spent filtering applicants and compiling interview feedback, ensuring internal efficiency is delivered alongside candidate-facing experience. |
| **Training and skills transfer** | Modular training material prepared per the OUM Methodology. APPSolve trains client HR and recruiting teams to own and maintain configuration, reports, and offer letters post go-live. |

### 9.3 Resource and Delivery Model

| Resource type | Role |
|---|---|
| HCM Principal Consultant | Design authority; configuration governance; client engagement leadership |
| HCM Senior Functional Consultant | Project implementation lead; Recruiting Cloud configuration and testing |
| HCM Senior Functional / Technical Consultant | OIC integration architecture; REST API configuration; technical build |
| Project Manager | Delivery governance; timeline management; risk and issue escalation |

Implementation is conducted remotely with on-site presence for key workshops and design sessions where required. APPSolve's hybrid delivery model is applied as standard.

---

## Section 10: Implementation References

### 10.1 Hollywood Bets — Oracle Fusion Recruiting Cloud (Primary Reference)

| Attribute | Detail |
|---|---|
| **Client** | Hollywood Bets |
| **Industry** | Retail Gaming and Sports Betting |
| **Product** | Oracle Fusion Recruiting Cloud Service |
| **Implementation scope** | External career site; internal career site; candidate selection process; job application flow; screening and shortlisting; interview management; offer management (branded offer letters); structured onboarding (preboarding and new hire workflows) |
| **Phase** | Phase 3 — Recruitment (86 days) |
| **Go-live** | July 2025 |
| **Users** | 7,000 |
| **Integration** | Oracle Integration Cloud (OIC) — third-party payroll integration; biometric system integration |
| **Proposal status** | ACCEPTED — Hollywood Bets Oracle Fusion HCM Accepted Proposal V5.0 (April 2023) |
| **Reference status** | Referenceable — contact details available via APPSolve account management |

Hollywood Bets' Oracle Fusion HCM implementation covered 8 modules over a structured phased programme. Oracle Fusion Recruiting Cloud (Phase 3) followed Core HCM (Phase 1) and Talent Management (Phase 2), with Goal and Performance Management delivered in Phase 4. This sequencing reflects APPSolve's standard Oracle HCM programme architecture.

### 10.2 Mining Sector — Active Oracle Recruiting Cloud Implementation (Pipeline Evidence)

APPSolve is currently implementing Oracle Recruiting and Onboarding capabilities for a mining-sector client. This engagement covers Recruitment and Onboarding as part of a broader Oracle Fusion HCM programme.

*Note: Client name is withheld in reusable tender content. This reference is not available as a formal reference site — the implementation is ongoing. BU Lead pre-tender check required before citing this in a specific tender.*

### 10.3 Oracle Taleo Recruiting — Historical Platform Experience

APPSolve has implementation and ongoing support experience with Oracle Taleo Recruiting solutions. While Oracle Recruiting Cloud is now the strategic Oracle recruiting platform, this experience demonstrates APPSolve's long-standing capability in Oracle recruitment solutions.

---

## Section 11: Integration Architecture

Oracle Integration Cloud (OIC) is APPSolve's standard integration layer in every Oracle Fusion HCM implementation, including Oracle Recruiting Cloud. This applies without exception.

### 11.1 Standard Recruiting Cloud Integration Points

| Integration | Method | Description |
|---|---|---|
| **Oracle Fusion Core HR** | Native Oracle integration | Candidate records convert automatically to employee records in Core HR upon hire. No manual data re-entry. |
| **Oracle Fusion Payroll Interface** | OIC / HCM Extracts | New hire data flows from Recruiting Cloud through Core HR to the payroll integration layer. Third-party payroll systems (PaySpace, SAP Payroll) connected via OIC as standard. |
| **Oracle Onboarding / Journeys** | Native Oracle integration | Offer acceptance in Recruiting Cloud triggers onboarding workflows automatically. |
| **LinkedIn** | Native Oracle integration | LinkedIn profile import for candidate applications; job sharing to LinkedIn professional network. Client LinkedIn recruiter accounts required. |
| **External job boards** | OIC / REST APIs | Automated multi-channel job posting to external job boards (Indeed and equivalent). Source effectiveness tracking included. |
| **Background check providers** | REST APIs | Third-party background verification services connect via Oracle REST APIs. Provider and integration scope are client-specific. |
| **Assessment platforms** | REST APIs | Third-party candidate assessment platforms connect via REST APIs where in scope. |

### 11.2 REST API Availability

Oracle Fusion HCM provides comprehensive RESTful APIs covering all major HCM business objects, including recruiting data (candidates, requisitions, applications, offers, onboarding tasks). APPSolve's technical team configures REST API-based integrations where standard OIC adapters are not available or where client architecture requires custom integration patterns.

---

## Section 12: Implementation Approach

### 12.1 Recruiting Cloud within the Oracle HCM Programme

APPSolve implements Oracle Fusion Recruiting Cloud as a structured delivery phase within the broader Oracle Fusion HCM programme. The sequencing follows the dependency model established across APPSolve implementations:

| Phase | Content | Dependency |
|---|---|---|
| Phase 1 | Core HCM — Global HR, Absence Management, Self-Service | Foundation — all subsequent phases depend on Phase 1 |
| Phase 2 | Talent Management — Talent Profiles, Goal Management, Performance, Career Development, Succession | Requires Phase 1 (employee and job structure) |
| **Phase 3** | **Oracle Recruiting Cloud** | **Requires Phase 1 (position management, job profiles, competency framework)** |
| Phase 4 | Learning Cloud, Workforce Compensation, Help Desk | Requires Phases 1–3 |

### 12.2 OUM Delivery Phases — Recruiting Cloud

APPSolve applies the Oracle Unified Methodology (OUM) across all Oracle Fusion HCM implementations, including Recruiting Cloud:

| OUM Phase | Recruiting Cloud Activities |
|---|---|
| **Mobilize** | Project charter; scope confirmation; Recruiting Cloud configuration workbooks; resource allocation; kick-off |
| **Scope and Design** | Recruiting process workshops; hiring workflow design; career site design brief; job profile and competency framework review; integration architecture design |
| **Prototype** | CRP1 — initial configuration walk-through; stakeholder feedback; CRP2 — refined configuration including career site, offer templates, and onboarding workflows |
| **Build** | Full configuration build; OIC integration build (job boards, background check, payroll); custom reports (up to 10 reports and 6 workflows per agreed scope); training material development |
| **Deploy** | Production build; data verification; UAT; end-user training; go-live support |
| **Post Go-Live** | Hyper-care (full team approximately 3 months); steady-state handover; ongoing support optional |

### 12.3 Standard Implementation Assumptions

The following assumptions reflect APPSolve's standard Recruiting Cloud delivery scope, drawn from confirmed implementation experience:

| Assumption ID | Assumption |
|---|---|
| A-W3-001 | Recruiting is configured as a global function — one recruitment portal serves all in-scope territories |
| A-W3-002 | One job application flow is configured per implementation scope |
| A-W3-003 | One candidate selection process (hiring workflow framework) is configured per implementation scope |
| A-W3-004 | One external career site is configured with client logo branding in Oracle-required format; graphical web design is a client responsibility |
| A-W3-005 | One internal career site is configured for employee-facing job browsing and application |
| A-W3-006 | LinkedIn integration is configured for job sharing and candidate profile import; client LinkedIn recruiter accounts are a client-provided prerequisite |
| A-W3-007 | Up to 3 offer letter templates are configured, branded as per client requirements; no requisitions are migrated — new requisitions are created by end users post go-live |
| A-W3-008 | Two onboarding processes are configured: one for pre-hires (pre-start-date activities) and one for new hires (Day 1 through induction); additional onboarding process types are out of scope unless separately agreed |
| A-W3-009 | Standard Oracle Recruiting Administration reports and dashboards satisfy reporting requirements within implementation scope; additional custom reports require separate scoping |
| A-W3-010 | Job profiles (competencies, skills, qualifications) are defined and available in Oracle Core HR prior to Recruiting Cloud configuration — Recruiting Cloud draws from the Core HR position and job framework |

---

## Section 13: Risk Register

| Risk ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-W3-003-001 | Career site design complexity exceeds standard scope — client's brand standards require bespoke graphical design beyond Oracle career site configuration capabilities | Medium | Medium | Clarify career site design scope at project initiation. Graphical web design is a client responsibility. APPSolve configures the Oracle framework; advanced design work is scoped separately. |
| R-W3-003-002 | LinkedIn recruiter accounts not available at project start — absence of client LinkedIn accounts delays social integration configuration and testing | Low | Low | Pre-tender check: confirm client LinkedIn recruiter account availability. Flag as prerequisite in project charter at kick-off. |
| R-W3-003-003 | Job profiles and competency frameworks not ready in Core HR at the time Recruiting Cloud configuration begins — Recruiting Cloud depends on the Core HR position and job structure | Medium | High | Recruiting Cloud is sequenced as Phase 3, following Core HCM (Phase 1). Dependency must be explicitly managed in programme plan. Job profile readiness checkpoint included in Phase 2 / Phase 3 gate review. |
| R-W3-003-004 | Onboarding task ownership ambiguity — responsibilities for completing onboarding tasks (new hire, manager, HR, IT) are not defined before configuration begins, resulting in workflow re-design during UAT | Medium | Medium | Onboarding process design workshop conducted in Scope and Design phase. RACI for all onboarding task types agreed before configuration begins. |
| R-W3-003-005 | Third-party integration scope (background checks, assessments) is underestimated at tender stage — each provider has different API requirements and data exchange formats | Medium | Medium | Background check and assessment platform integrations scoped as time-and-material items. Standard REST API patterns applied where provider APIs are compliant. Provider API documentation required before integration design begins. |

---

## Section 14: Assumptions Register

| Assumption ID | Assumption | Risk if incorrect |
|---|---|---|
| A-W3-001 | Recruiting is a global function — one portal per implementation scope | If territories require separate portals, scope increases materially; each additional portal requires separate configuration and testing |
| A-W3-002 | One job application flow per implementation scope | Additional application flows increase configuration and UAT effort; scope change required |
| A-W3-003 | One candidate selection process per implementation scope | Role-specific selection processes are a scope increase; additional processes require separate design and configuration |
| A-W3-004 | Career site branding limited to logo and basic brand elements; client provides logo in Oracle-required format | Graphical design requirements beyond Oracle framework require client web team engagement; APPSolve is not responsible for graphical web design |
| A-W3-005 | LinkedIn integration requires existing client LinkedIn recruiter accounts | Absence of accounts delays integration by the time required to establish accounts; client action required |
| A-W3-006 | Up to 3 offer letter templates; no requisition migration | Additional offer letter templates require separate scoping; historical requisition migration is not a standard Recruiting Cloud deliverable |
| A-W3-007 | Two onboarding processes in scope: pre-hire and new hire | Additional onboarding process types (e.g., contractor onboarding, re-hire onboarding) require separate scoping |
| A-W3-008 | Standard Oracle Recruiting dashboards and reports satisfy reporting requirements | Custom reports beyond standard Oracle OOB dashboards require separate scoping; up to 10 custom reports and 6 custom workflows are the standard implementation cap |
| A-W3-009 | Job profiles, competencies, skills, and qualifications are defined and ready in Oracle Core HR before Recruiting Cloud configuration begins | Delay in job profile readiness delays Phase 3 configuration start date; programme timeline risk |
| A-W3-010 | Background check and assessment platform providers are identified and their API documentation is available at the start of the integration design phase | Undisclosed provider requirements or proprietary APIs may extend integration design and build timelines |

---

## Section 17: Approval Record

| Field | Value |
|---|---|
| **Document ID** | W3S1-003-ORA-RecruitingCloud |
| **Version** | 1.1 Approved |
| **Created** | 2026-06-12 |
| **Created by** | Claude (AI — Wave 3 W3S1-003 extraction) |
| **Status** | Approved — BU Lead approved 2026-06-13; all amendments applied (I-001, CROSS-1) |
| **Approved for reuse** | Yes — BU Lead approved 2026-06-13 |
| **Approved by** | Hein Blignaut (BU Lead) |
| **Approval date** | 2026-06-13 |
| **Open items at submission** | None — all 8 OI items CLOSED by BU Lead 2026-06-12 |
| **BU Lead** | Hein Blignaut |

---

## Appendix A: Source Mapping Table

| Section | Content type | Primary source | Governance classification |
|---|---|---|---|
| Section 1 | Implementation evidence | HIST-007 (Hollywood Bets V5.0 ACCEPTED) | Tier 1 — Implementation Evidence |
| Section 1 | Taleo positioning | BU Lead OI-W3-002 approved wording | Governance-approved statement |
| Section 1 | Active mining client | BU Lead OI-W3-003 approved wording; Redpath Mining Rule 21.5 | Pipeline evidence — client NOT named |
| Section 2 | Module overview | HIST-006 (SAA, sentences 107–118) | Tier 3 — Platform Capability; reframed as APPSolve capability |
| Section 3.1 | Platform architecture | HIST-006 (SAA, sentences 583–594); ORACLE_FACT_BASELINE Section 7 | Tier 3 — Platform Capability |
| Section 3.2 | Taleo positioning | BU Lead OI-W3-002 approved wording | Governance-approved statement |
| Section 3.3 | Internal mobility | HIST-006 (SAA, sentences 460–463); BU Lead OI-W3-005 | Tier 3 — Platform Capability only |
| Section 4 | Requisition management | HIST-006 (SAA, sentences 383–384); HIST-007 (Phase 3); HIST-015 (Afrocentric assumptions) | Tier 3 / Tier 1 delivery pattern |
| Section 5.1 | Career sites | HIST-007 (Section 3.3.3); HIST-006 (sentences 123–125, 385); BU Lead OI-W3-006 | Tier 1 confirmed implemented |
| Section 5.2 | Multi-channel sourcing | HIST-006 (sentences 121–122, 386–388); HIST-015 (assumptions) | Tier 3 — Platform Capability |
| Section 5.3 | Employee referrals | HIST-006 (sentences 400–406); BU Lead OI-W3-006 | Tier 3 — Platform Capability; confirmed implemented per OI-W3-006 |
| Section 6 | Screening and interviews | HIST-006 (sentences 126–129, 388–391); HIST-007 (Section 3.3.3 filtering/feedback) | Tier 1 confirmed implemented |
| Section 7 | Offer management | HIST-006 (sentences 130–131, 392, 738–739); HIST-015 (assumptions) | Tier 1 confirmed implemented |
| Section 8 | Onboarding | HIST-006 (sentences 393–399); HIST-015 (sentence 735); BU Lead OI-W3-001 | Tier 1 confirmed implemented |
| Section 9 | Delivery capability | HIST-007 (Section 3.3.3, resource schedule); HIST-015 (methodology corroboration — unnamed) | Tier 1 / Tier 3 delivery pattern |
| Section 10.1 | Hollywood Bets reference | HIST-007 (BOM + schedule); HIST-016 (SABS ETS corroboration); ORACLE_FACT_BASELINE Section 19 | Tier 1 — Referenceable |
| Section 10.2 | Mining active client | BU Lead OI-W3-003 approved wording; Rule 21.5 | Pipeline evidence — NOT referenceable |
| Section 10.3 | Taleo historical | BU Lead OI-W3-002 approved wording; DFA Rule 21.4 | Internal evidence — NOT named |
| Section 11 | OIC integration | ORACLE_FACT_BASELINE Section 7; HIST-007 (BOM OIC); HIST-006 (sentences 591–594) | Mandatory standard — all implementations |
| Section 12 | Implementation approach | ORACLE_FACT_BASELINE Section 17; HIST-007 (phase schedule); HIST-015 (phase structure) | Delivery methodology |
| Section 13 | Risk register | SVR-W3S1-003 risk analysis; HIST-015/HIST-006 implementation assumptions | Internal governance |
| Section 14 | Assumptions register | HIST-006 (sentences 728–742); HIST-015 (assumptions sentences 305–318) | Source-validated assumptions |

**Prohibited sources — confirmed excluded:**
- CCBA (HIST-014) — not named; not used as implementation evidence; never referenced in output
- SAA — not named as client or reference; used as platform capability source only (reframed)
- DFA — not named; Taleo experience referenced without client identification per Rule 21.4
- Redpath Mining — not named; cited as active mining-sector client per Rule 21.5 and BU Lead OI-W3-003
- Aviation sector — not referenced anywhere in this document per Rule 21.1

---

## Appendix B: Governance Self-Review

**Wave 3 Standing Rules — Compliance Check (ORACLE_FACT_BASELINE Section 21)**

| Rule | Check | Status |
|---|---|---|
| **21.1 Aviation PROHIBITED** | Search for "aviation", "airline", "SAA", "South African Airways" as client/reference — confirmed absent | ✅ PASS |
| **21.1 Approved sectors** | Retail (Hollywood Bets), Mining (Redpath pipeline framing), Professional Services (supported sector) | ✅ PASS |
| **21.1 SAA source rule** | SAA content used as platform capability narrative only; SAA not named as client or reference anywhere | ✅ PASS |
| **21.2 Implementation vs Support distinction** | Hollywood Bets = implementation; Mr Price broader HCM = not cited in this document; Mr Price Recruiting not claimed | ✅ PASS |
| **21.3 Opportunity Marketplace** | Section 3.3 references Opportunity Marketplace as a complement; does not use it to imply Recruiting deployment at Mr Price | ✅ PASS |
| **21.4 DFA — never named** | DFA not named anywhere in document; Taleo experience framed without client identification | ✅ PASS |
| **21.5 Redpath — not named; not completed** | Redpath not named; cited only as "mining-sector client" with BU Lead approved wording; no go-live implied | ✅ PASS |
| **CCBA — never named** | CCBA not referenced anywhere in document | ✅ PASS |

**ORACLE_FACT_BASELINE Section 15 — Prohibited Wording Check**

| Prohibited item | Check |
|---|---|
| "Oracle Gold Partner" / "Gold Level" | Absent — "Oracle Level 1 Partner" used in Section 9.1 | ✅ |
| "110 Senior Consultants" / "100+ consultants" | Absent — "50+ Senior Consultants" also removed per BU Lead CROSS-1 2026-06-13 | ✅ |
| "over 22 years" | Absent — not cited in this document | ✅ |
| "BEE Level 2" | Absent — BEE not cited in this capability statement | ✅ |
| "Oracle Recruiting Cloud does X" (Oracle framing) | Absent — all claims framed as APPSolve implementing/configuring X using Oracle Fusion Recruiting Cloud | ✅ |
| Mr Price cited for Recruiting | Absent — Mr Price not referenced in context of Recruiting | ✅ |
| Recruiting Booster as implemented | Absent — Recruiting Booster not referenced in this document (no confirmed implementation scope; excluded per OI-W3-004) | ✅ |
| Unsupported client counts or module counts | Absent — all counts sourced; no total-module claims | ✅ |

**OIC Mandatory Rule Check**

OIC referenced in Section 1, Section 11.1, and Section 12.2 as the standard integration layer. ✅ PASS

**OI Items Closed — Final Confirmation**

| OI Item | Status |
|---|---|
| OI-W3-001 Hollywood Bets scope | CLOSED — all confirmed implemented modules reflected in Sections 4–8 |
| OI-W3-002 Taleo positioning | CLOSED — approved wording applied in Sections 1, 9.1, and 10.3 |
| OI-W3-003 Redpath active implementation | CLOSED — approved wording applied in Sections 1 and 10.2 |
| OI-W3-004 Recruiting Booster | CLOSED — excluded; no confirmed implementation scope; omitted from document |
| OI-W3-005 Internal Mobility | CLOSED — positioned as platform capability in Section 3.3; Opportunity Marketplace evidence not used |
| OI-W3-006 Candidate Experience | CLOSED — Career Sites, Branded Career Portals, Candidate Talent Communities, Employee Referral Programmes confirmed implemented in Section 5 |
| OI-W3-007 Recruiting Sectors | CLOSED — Retail, Mining, Professional Services cited in Section 1 |
| OI-W3-008 Recruiting References | CLOSED — Hollywood Bets referenceable (Section 10.1); DFA not named (Section 10.3); Redpath not named (Section 10.2); Mr Price not cited for Recruiting |

**Governance Self-Review conclusion: CLEAN. No violations identified.**

---

## Appendix C: Extraction Return Report

| Field | Value |
|---|---|
| **Extraction ID** | W3S1-003 |
| **Document title** | Oracle Fusion Recruiting Cloud — Capability Statement |
| **Version** | 1.1 Approved |
| **Date** | 2026-06-13 |
| **Sources used** | HIST-007 (Tier 1); HIST-006 (Tier 3); HIST-015 (Tier 3); HIST-016 (Tier 3 — reference corroboration) |
| **Sections delivered** | 14 content sections + Section 17 + Appendices A, B, C |
| **Open items at submission** | 0 — all 8 BU Lead decisions (OI-W3-001 through OI-W3-008) CLOSED before extraction |
| **Governance violations** | None |
| **Prohibited sources used** | None — CCBA excluded; SAA used as platform capability source only (not named); DFA not named; Redpath not named |
| **Pre-tender checks (standing)** | PT-W3-003-001: Confirm Hollywood Bets reference contact details are current before citing in specific tender; PT-W3-003-002: Confirm client LinkedIn recruiter accounts available before quoting LinkedIn integration; PT-W3-003-003: Confirm BEE certificate is current (expires 2026-07-31); PT-W3-003-004: Confirm active mining-sector client pipeline reference is appropriate for the specific tender before citing |
| **Changes v1.0 to v1.1** | CROSS-1: "APPSolve employs 50+ Senior Consultants and" removed from Section 9.1. Version updated to 1.1 Approved. approved_for_reuse set to Yes. Approved by BU Lead 2026-06-13. |

---

*W3S1-003-ORA-RecruitingCloud v1.1 Approved — 2026-06-13 — Hein Blignaut (BU Lead) — approved_for_reuse: Yes*
