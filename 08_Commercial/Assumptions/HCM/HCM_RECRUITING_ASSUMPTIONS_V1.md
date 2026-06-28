---
document_id: HCM-RECRUITING-ASSUMPTIONS-V1
title: "Oracle Fusion Recruiting Cloud — Assumptions, Exclusions, and Customer Responsibilities"
version: "1.1"
status: "Approved v1.0"
created: "2026-06-15"
created_by: "WP11B — Recruiting Assumptions Pack"
approved_by: "Oracle HCM BU Lead"
approved_date: "2026-06-19"
approved_for_reuse: true
lifecycle_status: APPROVED
category: "Commercial / Assumptions"
scope: "Oracle Fusion Recruiting Cloud (B87675) and Oracle Fusion Recruiting Booster (B95763). Extends HCM_BASE_ASSUMPTIONS_V1.md — always load HCM Base before this pack."
apply_with: "TENDER_ASSUMPTION_ASSEMBLY_RULES.md"
parent_pack: "HCM_BASE_ASSUMPTIONS_V1.md"
assumption_count: 54
bu_lead_review_items: []
---

# Oracle Fusion Recruiting Cloud — Assumptions V1.0

**Scope:** This document governs Oracle Fusion Recruiting Cloud (B87675) and Oracle Fusion Recruiting Booster (B95763) implementations delivered by APPSolve. It extends `HCM_BASE_ASSUMPTIONS_V1.md` — all HCM Base assumptions apply to Recruiting implementations. This pack adds Recruiting-specific scope boundaries only.

**Load order:** HCM Base Assumptions (complete) → this pack (additive). Do not use this pack without first including HCM Base.

**Governance:** Governed under ASSUMPTION_GOVERNANCE.md. Status: **Approved v1.0 — 2026-06-19 (WP16C)**. All BU-REC-XXX decisions resolved. Approved for use in external proposals. `approved_for_reuse: true`.

---

## 16. Career Site Assumptions

**REC-SIT-001**  
The default Oracle Recruiting career site configuration includes: one (1) external career site (branded and publicly accessible, designed for external candidates); one (1) internal career site (accessible to current employees for internal mobility and referrals); and one (1) agency/recruiter portal (accessible to approved external recruiting agencies). Each additional career site type beyond this default constitutes a scope change requiring a Change Request.

**REC-SIT-002**  
APPSolve configures career site branding using the client's logo, primary brand colour, and approved typography. Career site design is based on Oracle's standard career site builder toolset. Custom HTML/CSS development, multi-page microsite design, animated components, and complex interactive page designs beyond Oracle's standard career site builder capability are excluded from base scope.

**REC-SIT-003**  
Where an agency portal is included in scope, APPSolve configures one (1) agency portal with one (1) agency supplier registered at go-live. Additional agency suppliers are added by the client's Recruiting Administrator after go-live as a standard administrative task. APPSolve provides training to the Recruiting Administrator on agency supplier management.

**REC-SIT-004**  
Career site content — including all job description text, employer brand copy, videos, photography, and supporting marketing content — is the client's responsibility. APPSolve configures the career site structure and branding framework; the client populates and maintains all content.

**REC-SIT-005**  
Job posting to external job boards (including LinkedIn, PNet, and any additional boards) from Oracle Recruiting is configured for the boards confirmed in the Scope and Design phase. Each additional job board integration beyond those agreed constitutes a scope change. Job board account credentials and commercial arrangements with job board providers are the client's responsibility.

---

## 17. Requisition Assumptions

**REC-REQ-001**  
APPSolve configures Oracle Recruiting requisition management including: job requisition templates, requisition approval workflows, posting workflows, and job offer approval workflows. The number of distinct requisition templates and approval workflow variants is agreed in the Scope and Design phase. Each additional requisition template or approval variant beyond the agreed count constitutes a scope change.

**REC-REQ-002**  
A maximum of one (1) requisition approval workflow is configured in base scope. This workflow applies across all requisition types unless differentiated approval requirements per department, subsidiary, or job family are agreed as a scope addition.

**REC-REQ-003**  
Job profiles (competencies, skills, qualifications, and responsibilities) used to populate requisitions must be available in Oracle HCM before Recruiting Design workshops commence. The client is responsible for defining and providing job profile content. APPSolve configures the Oracle job profile framework; the client populates job profiles.

**REC-REQ-004**  
APPSolve configures Oracle Recruiting to support the candidate selection process as agreed during the Scope and Design phase. A maximum of one (1) candidate selection process (CSP) with up to five (5) interview stages is configured in base scope. Additional candidate selection processes (for example, separate CSPs for different job families, geographic regions, or employment types) constitute a scope addition.

**REC-REQ-005**  
No historical open or closed requisitions are migrated from the client's legacy ATS to Oracle Recruiting. New requisitions are created by end users in Oracle Recruiting from go-live date. The client's HR team is responsible for closing open requisitions in the legacy ATS before or at go-live.

---

## 18. Candidate Migration Assumptions

**REC-CAN-001**  
No candidate data migration is included in base scope. Oracle Recruiting launches as a clean system; all new candidate applications are captured natively in Oracle Recruiting from go-live. Historical candidate records, application history, and talent pools from the client's legacy ATS are excluded from migration.

**REC-CAN-002**  
Where the client has active candidates in final selection stages (for example, offer stage) at the time of Oracle Recruiting go-live, those candidates will be managed to completion in the legacy ATS and/or migrated manually by the client's recruitment team. APPSolve does not migrate individual active candidate records from the legacy ATS.

**REC-CAN-003**  
The client is responsible for communicating to candidates in process how their application will be managed during the system transition. APPSolve does not provide candidate communication services or manage candidate experience during the go-live transition.

---

## 19. Recruiting Agency Assumptions

**REC-AGY-001**  
APPSolve configures Oracle Recruiting's agency management capability to allow approved external recruiting agencies to submit candidates directly into Oracle Recruiting. Agency portal access is limited to the agencies explicitly registered by the client's Recruiting Administrator.

**REC-AGY-002**  
Agency commission management, fee calculations, agency billing, and vendor management system (VMS) integration are excluded from base scope. Oracle Recruiting's agency module is used for candidate submission only; commercial fee management with agencies is the client's responsibility and is handled outside Oracle Recruiting unless a VMS integration is explicitly scoped.

**REC-AGY-003**  
The client is responsible for commercially engaging all recruiting agencies used in Oracle Recruiting's agency portal. APPSolve configures the Oracle system to support the approved agency list provided by the client; APPSolve does not manage, evaluate, or onboard agencies on the client's behalf.

---

## 20. Offer Management Assumptions

**REC-OFF-001**  
APPSolve configures Oracle Recruiting offer management including: offer creation, approval workflow, offer letter generation via Oracle BI Publisher, and offer status tracking. The offer management configuration is aligned to the one (1) requisition approval workflow included in base scope.

**REC-OFF-002**  
A maximum of three (3) offer letter templates are configured in Oracle BI Publisher as part of base scope. Additional offer letter templates beyond three constitute a scope change. Each offer letter template must be provided by the client in Microsoft Word format with all required variable fields clearly marked before BI Publisher configuration commences.

**REC-OFF-003**  
Electronic signature integration (for example, DocuSign, Adobe Sign, or equivalent) for offer letters is not included in base scope. Oracle Recruiting's standard offer management delivers offer letters via email with the client downloading and returning the signed letter, or via Oracle's platform-level digital signature capability (if enabled in the Oracle tenancy). Dedicated e-signature platform integration is assessed and priced separately.

**REC-OFF-004**  
The offer approval workflow configured in Oracle Recruiting routes offers through the client's management hierarchy or an approval group, as confirmed in the Scope and Design phase. Offer approval workflows that require conditional routing logic (for example, salary above a threshold routes to an additional approver) are assessed as a scope addition.

**REC-OFF-005**  
Once a candidate accepts an offer in Oracle Recruiting, the transition to Oracle HCM (creation of the employee/pending worker record and initiation of onboarding Journeys) is configured as part of this implementation. The client is responsible for confirming all required pre-employment data fields and onboarding task lists before Recruiting-to-HCM transition configuration commences.

---

## 21. Interview Scheduling Assumptions

**REC-INT-001**  
APPSolve configures interview scheduling within Oracle Recruiting. Interview scheduling includes: interview stage configuration within the candidate selection process; interviewer assignment; interview invitation; and feedback collection via Oracle Recruiting's interview feedback forms.

**REC-INT-002**  
Where Oracle Fusion Recruiting Booster (B95763) is included in the BOM, APPSolve configures Booster's advanced interview scheduling: two-way calendar integration with the client's calendar system; automated availability-based scheduling; and centralized interview schedule management for the recruitment team. See Section 24 (Recruiting Booster Assumptions).

**REC-INT-003**  
Calendar integration for interview scheduling is based on Microsoft 365 / Outlook. The client is responsible for providing an appropriate Microsoft 365 service account or integration credentials for calendar access. Google Workspace (Google Calendar) integration for interview scheduling requires assessment before commitment — confirm feasibility with the Oracle product team during Scope and Design if Google Workspace is the client's calendar platform.

**REC-INT-004**  
Background check provider integration is not included in base scope. APPSolve can design and configure an OIC integration between Oracle Recruiting and a third-party background check provider (for example, Managed Integrity Screening, iFacts, LexisNexis, or equivalent) as a separately scoped and priced integration. The background check provider must offer a documented API. The client is responsible for all commercial engagement with the background check provider.

---

## 22. LinkedIn Integration Assumptions

**REC-LIN-001**  
Oracle Recruiting integrates with LinkedIn for job posting via LinkedIn Limited Listings. This integration is available as part of Oracle Recruiting (B87675) at no additional Oracle licence cost. APPSolve configures the LinkedIn integration as part of the career site and posting configuration. The client is responsible for holding a LinkedIn Company Page and accepting LinkedIn's terms for job posting.

**REC-LIN-002**  
LinkedIn Recruiter System Connect (RSC) integration — which enables LinkedIn Recruiter seat holders to view candidate Oracle Recruiting profiles from within LinkedIn Recruiter — requires the client to hold LinkedIn Recruiter seat licences and is configured where in scope. LinkedIn RSC is an Oracle-delivered connector and is configured by APPSolve; the client's LinkedIn commercial relationship is the client's responsibility.

**REC-LIN-003**  
Direct Apply via LinkedIn (enabling candidates to apply for jobs from LinkedIn using their LinkedIn profile) is available where Oracle Fusion Recruiting Booster (B95763) is included in the BOM. Configuration of Direct Apply is included in the Booster scope. See Section 24.

**REC-LIN-004**  
LinkedIn talent insights, LinkedIn Learning integration, and LinkedIn Talent Hub are separate LinkedIn products and are not part of Oracle Recruiting or Recruiting Booster. These are excluded from APPSolve's implementation scope.

---

## 23. Recruiting Reporting Assumptions

**REC-RPT-001**  
APPSolve configures Oracle Recruiting's standard administration dashboards, including the Oracle Recruiting Administration dashboards for requisition pipeline, source effectiveness, and candidate stage reporting. These are Oracle-delivered dashboards and are available within the Oracle Recruiting licence at no additional analytics licence cost.

**REC-RPT-002**  
Custom OTBI reports for Oracle Recruiting consume from the base OTBI custom report allowance defined in HCM Base assumption HCM-RPT-002. Recruiting-specific custom reports do not have a separate allowance; they are counted against the same total. Where all custom report slots are consumed by non-Recruiting modules, additional custom Recruiting reports are a Change Request.

**REC-RPT-003**  
Oracle Analytics Cloud (OAC/OAX) advanced Recruiting analytics (advanced hiring funnel analysis, diversity pipeline analytics, AI-driven sourcing recommendations) are separately licensed and are excluded from this scope. HCM Base assumption HCM-RPT-003 applies.

**REC-RPT-004**  
The client is responsible for defining all custom Recruiting report requirements (fields, filters, grouping, and calculation logic) in the same format as general HCM reporting requirements. HCM Base assumption HCM-RPT-006 applies to Recruiting reports.

---

## 24. Recruiting Booster Assumptions

**REC-BOO-001**  
The assumptions in this section (REC-BOO-XXX) apply only where Oracle Fusion Recruiting Booster (B95763) is included in the Bill of Materials. Where only Oracle Fusion Recruiting Cloud (B87675) is licensed, Booster-specific capabilities (Two-Way Messaging, Digital Assistant chatbot, Event Management, Direct Apply) are not available and are excluded.

**REC-BOO-002**  
**Two-Way Messaging:** APPSolve configures Oracle Recruiting Booster's two-way candidate communication (SMS and email). The client provides the approved sender identity (phone number/email domain) and complies with POPIA requirements for direct candidate communication via SMS/email. APPSolve configures the Oracle system; SMS transmission costs (if applicable) are governed by Oracle's platform model and are the client's commercial arrangement with Oracle.

**REC-BOO-003**  
**Advanced Interview Scheduling (Booster):** APPSolve configures Booster's automated interview scheduling including calendar integration (Microsoft 365/Outlook — see REC-INT-003), interviewer availability-based scheduling, and centralised interview schedule management. Panel interview scheduling and multi-interviewer scheduling are supported by Oracle Booster's standard capability.

**REC-BOO-004**  
**Oracle Digital Assistant (Chatbot):** APPSolve configures Oracle Recruiting Booster's Digital Assistant chatbot capability, enabling candidates to search jobs, receive AI-powered job recommendations, and start applications from a conversational chatbot interface. The chatbot is deployed on the client's Oracle career site. Custom chatbot scripts, custom NLP training, or integration to a third-party chatbot platform (for example, Intercom, Drift, or equivalent) are excluded.

**REC-BOO-005**  
**Recruiting Event Management:** APPSolve configures Oracle Recruiting Booster's Event Management capability, enabling the client to create and promote recruitment events within Oracle Recruiting, manage event registration, and track candidate attendance. A maximum of two (2) event types are configured in base scope. Additional event types are a Change Request.

**REC-BOO-006**  
**Direct Apply (LinkedIn):** APPSolve configures Oracle Recruiting Booster's Direct Apply integration with LinkedIn, enabling candidates to apply for jobs from LinkedIn job listings using their LinkedIn profile. This requires the client to hold a LinkedIn Company Page and accept LinkedIn's Direct Apply terms. The client's LinkedIn commercial relationship is the client's responsibility.

**REC-BOO-007**  
**Bulk Communications:** APPSolve configures Oracle Recruiting Booster's bulk communication capability for sending mass candidate communications within Oracle Recruiting. The client is responsible for all communication content, POPIA consent compliance, and communication approval. APPSolve provides the technical configuration; the client manages communication campaigns.

---

## 25. Recruiting Security Assumptions

**REC-SEC-001**  
APPSolve configures Oracle Recruiting roles using Oracle's seeded Recruiting duty roles as the baseline: Recruiter, Hiring Manager, Interviewer, Recruiting Administrator, and Agency Recruiter. Custom modifications to Oracle seeded Recruiting duty roles are excluded. HCM Base assumption HCM-SEC-001 applies.

**REC-SEC-002**  
Recruiting security is configured as a global model by default. Where the client requires subsidiary-level or regional security (for example, Recruiter A can only see requisitions for Business Unit X, not Business Unit Y), this constitutes a scope addition and is assessed during the Scope and Design phase. Subsidiary-level Recruiting security increases configuration complexity.

**REC-SEC-003**  
The client is responsible for defining the Recruiting security model — who can see which requisitions, which candidates, and which teams — before Recruiting security design commences. HCM Base assumption HCM-CUS-006 applies to Recruiting business rule documentation.

---

## 26. Recruiting Training Assumptions

**REC-TRN-001**  
APPSolve delivers Recruiting train-the-trainer (TTT) training for the following user populations: (1) Recruiters — Oracle Recruiting workflow, requisition management, candidate management, offer management; (2) Hiring Managers — requisition approval, interview scheduling, feedback submission, offer approval; (3) Recruiting Administrator — system administration, agency management, career site maintenance, reporting. HCM Base assumption HCM-TRN-001 applies.

**REC-TRN-002**  
Where Oracle Recruiting Booster (B95763) is in scope, APPSolve delivers additional TTT training covering Booster-specific features: Two-Way Messaging, Advanced Interview Scheduling, Digital Assistant, Event Management. Booster training is included in the Recruiting training scope where B95763 is licensed.

**REC-TRN-003**  
Candidate-facing guidance (how to apply, how to navigate the career site, how to track application status) is not delivered by APPSolve. Where the client requires candidate-facing help content, this is created and published by the client on their career site. APPSolve provides guidance to the Recruiting Administrator on how to add help content to the career site.

---

## 27. Recruiting Exclusions

**REC-EXC-001**  
**Legacy ATS Data Migration:** No candidate data, requisition data, or application history is migrated from the client's legacy applicant tracking system (ATS — for example, Taleo, Workday Recruiting, SAP SuccessFactors, SmartRecruiters, Oracle Taleo, or equivalent) to Oracle Recruiting. Oracle Recruiting launches as a new system. The client is responsible for archiving legacy ATS data.

**REC-EXC-002**  
**Taleo Integration:** Where the client operates Oracle Taleo Business Edition (TBE) or Oracle Taleo Enterprise Edition (TEE), migration or integration between Taleo and Oracle Fusion Recruiting is excluded from base scope. APPSolve has Taleo implementation experience; however, Taleo-to-Oracle Fusion Recruiting migration is a standalone engagement assessed and priced separately.

**REC-EXC-003**  
**Agency Commission and VMS Integration:** Recruiting agency commission management, fee calculation, purchase order generation, and vendor management system (VMS) integration (for example, Beeline, Fieldglass, Coupa) are excluded. Oracle Recruiting is used for candidate submission from agencies only; all financial transactions with recruiting agencies are managed outside Oracle Recruiting.

**REC-EXC-004**  
**Background Check Provider Configuration:** Third-party background check platform configuration (portal setup, screening package definition, result management) is excluded. APPSolve's scope is limited to the Oracle OIC integration design (where this is separately scoped); the background check provider's own platform configuration is the client's and the provider's responsibility.

**REC-EXC-005**  
**E-Signature Platform Integration:** Integration between Oracle Recruiting offer management and a dedicated e-signature platform (DocuSign, Adobe Sign, Dropbox Sign, or equivalent) is excluded from base scope. This integration is assessed and priced separately.

**REC-EXC-006**  
**Recruitment Process Outsourcing (RPO) Configuration:** Where the client operates with a Recruitment Process Outsourcing provider managing their recruitment function, configuration of the RPO's access model, reporting requirements, and process customisation for the RPO is not in base scope. RPO-specific configuration is assessed during the Scope and Design phase.

**REC-EXC-007**  
**Oracle Taleo CRM and Candidate Relationship Management (CRM) beyond Booster:** Advanced candidate CRM functionality beyond what is available in Oracle Recruiting Booster (event management, bulk communications, two-way messaging) is excluded. Oracle's dedicated Talent Acquisition CRM modules beyond Booster are not in scope.

**REC-EXC-008**  
**Social Media Publishing Beyond LinkedIn:** Automated job posting to social media platforms beyond LinkedIn (for example, Twitter/X, Facebook, Instagram, TikTok) is not available as a standard Oracle Recruiting feature and is excluded. Job promotion on social media is the client's marketing team's responsibility.

---

## Approval Record

All BU Lead review items confirmed. Status: **Approved v1.0 — 2026-06-19 (WP16C)**.

| Decision ID | Item | Confirmed Position | Resolved |
|---|---|---|---|
| BU-REC-001 | Career site default count | 1 external + 1 internal + 1 agency portal as default | WP15F 2026-06-19 |
| BU-REC-002 | Interview scheduling calendar | Microsoft 365 / Outlook; Google Workspace requires assessment | WP15F 2026-06-19 |
| BU-REC-003 | Offer letter template count | 3 templates in base scope | WP15F 2026-06-19 |
| BU-REC-004 | Agency portal default inclusion | Agency portal included where in scope / requested | WP15F 2026-06-19 |
| BU-REC-005 | Recruiting Booster scope trigger | Booster assumptions apply only when B95763 is in the BOM | WP16C 2026-06-19 |
| BU-REC-006 | Background check integration scope | OIC integration design only; provider portal excluded | WP16C 2026-06-19 |
| BU-REC-007 | Requisition template count | No default limit — confirmed per engagement in Scope and Design | WP16C 2026-06-19 |

---

*HCM_RECRUITING_ASSUMPTIONS_V1.1 | WP11B — Recruiting Assumptions Pack | 2026-06-15 | **Approved v1.0 — 2026-06-19 (WP16C)***  
*54 assumptions / exclusions / responsibilities across 12 sections (Sections 16–27)*  
*Parent pack: HCM_BASE_ASSUMPTIONS_V1.md | Governed under: 08_Commercial/ASSUMPTION_GOVERNANCE.md*  
*Assembly rules: 08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md*
