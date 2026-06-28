---
document_id: HCM-LEARNING-ASSUMPTIONS-V1
title: "Oracle Fusion Learning Cloud — Assumptions, Exclusions, and Customer Responsibilities"
version: "1.1"
status: "Approved v1.0"
created: "2026-06-15"
created_by: "WP11 — Commercial Assumptions Library"
approved_by: "Oracle HCM BU Lead"
approved_date: "2026-06-19"
approved_for_reuse: true
lifecycle_status: APPROVED
category: "Commercial / Assumptions"
scope: "Oracle Fusion Learning Cloud (B85242). Extends HCM_BASE_ASSUMPTIONS_V1.md — always load HCM Base before this pack."
apply_with: "TENDER_ASSUMPTION_ASSEMBLY_RULES.md"
parent_pack: "HCM_BASE_ASSUMPTIONS_V1.md"
assumption_count: 37
oracle_part_number: "B85242"
kb_reference: "W3S1-004-ORA-LearningCloud.md"
governance_constraint: "C-W3-002 — Mr Price Group is the sole referenceable Oracle Fusion Learning Cloud implementation client. Only cite Mr Price for Learning Cloud scope."
bu_lead_review_items: []
---

# Oracle Fusion Learning Cloud — Assumptions V1.0

**Scope:** This document governs Oracle Fusion Learning Cloud (B85242) implementations. It extends `HCM_BASE_ASSUMPTIONS_V1.md` — all HCM Base assumptions apply to Learning Cloud implementations. This pack adds Learning-specific scope boundaries, exclusions, and customer responsibilities.

**Load order:** HCM Base Assumptions (complete) → this pack (additive). Where a Learning assumption restates or modifies a Base assumption, the Learning assumption takes precedence for Learning Cloud contexts. Do not use this pack without first including HCM Base.

**Governance:** Governed under ASSUMPTION_GOVERNANCE.md. Status: **Approved v1.0 — 2026-06-19 (WP16C)**. All BU-LRN-XXX decisions resolved. Approved for use in external proposals. `approved_for_reuse: true`.

---

## 28. Learning Content Assumptions

**LRN-CON-001**  
Oracle Fusion Learning Cloud supports the following content formats natively: SCORM 1.2, SCORM 2004, AICC, PDF documents, video files (MP4), web links, and Oracle-native assessments and quizzes. APPSolve configures the Learning platform to accept and deliver content in these formats. Content formats not in this list require assessment before inclusion in scope.

**LRN-CON-002**  
All learning content — including course materials, SCORM packages, videos, PDF guides, assessment questions, and compliance course content — is the client's responsibility. APPSolve configures the Oracle Learning platform framework; the client creates, procures, and provides all content for upload. APPSolve does not author, edit, translate, or review learning content on the client's behalf.

**LRN-CON-003**  
The client's designated Learning Administrator is responsible for uploading and maintaining content in Oracle Learning after go-live. APPSolve provides training to the Learning Administrator on content upload, version management, and catalogue maintenance during the training phase of the implementation. Content upload during the implementation is performed by the client under APPSolve's guidance, not by APPSolve.

**LRN-CON-004**  
eLearning content authoring tools — including Articulate Storyline, Articulate Rise, Lectora Inspire, Adobe Captivate, iSpring, and similar platforms — are not in APPSolve's scope. The client is responsible for procuring authoring tool licences, creating SCORM content, and exporting it in a format compatible with Oracle Learning. APPSolve provides specification of the required content format.

**LRN-CON-005**  
APPSolve is not responsible for the instructional design quality, pedagogical effectiveness, or learning outcome of content provided by the client. APPSolve confirms that content can be uploaded and delivered by Oracle Learning; it does not review content for learning effectiveness.

---

## 29. Learning Platform Configuration

**LRN-PLT-001**  
APPSolve designs and configures the Oracle Learning catalogue structure, including learning categories, learning communities, course types, specialisations, and learning item taxonomy. The catalogue hierarchy design is agreed with the client's Learning and Development team during the Scope and Design phase. The client is responsible for reviewing and approving the catalogue design before configuration commences.

**LRN-PLT-002**  
A maximum of two (2) learning communities are configured in base scope. Learning communities create audience-specific learning environments within Oracle Learning. Additional learning communities beyond the agreed count constitute a scope change. The client defines the community membership rules (by business unit, job family, location, or other attribute).

**LRN-PLT-003**  
APPSolve configures automated learning assignment rules for mandatory compliance training. Assignment rules are based on criteria agreed during the Scope and Design phase (for example: assign Induction Training to all new hires; assign Safety Compliance to all employees in Operations). The client provides the complete list of mandatory training requirements and assignment criteria before assignment rule configuration commences.

**LRN-PLT-004**  
Oracle Fusion Learning Cloud includes certification tracking capability. APPSolve configures certification definitions, validity periods, and expiry-based recertification automation as agreed in the Scope and Design phase. Certification tracking is a confirmed APPSolve implementation deliverable.

**LRN-PLT-005**  
Social and collaborative learning features (discussion forums, peer recommendations, user-generated content sharing, learning ratings, and comments) are Oracle-delivered platform features. APPSolve enables these features as part of the standard Learning configuration. The client's Learning Administrator manages the social learning environment after go-live.

**LRN-PLT-006**  
Oracle Fusion Learning Cloud is mobile-responsive and accessible from any device via a standard web browser. APPSolve does not develop, configure, or test a dedicated native mobile application for Oracle Learning — no such application is part of Oracle's standard Learning Cloud product.

**LRN-PLT-007**  
Learning notification emails (course assignment notifications, completion confirmations, expiry reminders, and manager notifications) are configured using Oracle's standard notification framework. Custom HTML-branded email templates are not included in base scope. HCM Base assumption HCM-WFL-004 applies.

---

## 30. AI and Personalised Learning

**LRN-AI-001**  
Oracle Fusion Learning Cloud includes Oracle's AI-powered personalised learning recommendation engine. APPSolve enables and configures the recommendation engine as part of the standard Learning implementation. AI-driven learning recommendations are generated by Oracle's machine learning models based on the learner's role, skills profile, career goals, and learning history.

**LRN-AI-002**  
AI learning recommendations require the Oracle AI Dynamic Skills feature (included in HCM Base B85800) to be enabled and populated with employee skills data. Without active skills profiles, AI learning recommendations default to role-based content only. APPSolve recommends enabling Oracle AI Dynamic Skills in the same implementation wave as Oracle Learning Cloud for maximum personalisation value.

**LRN-AI-003**  
APPSolve enables Oracle's AI personalisation engine but does not manually curate or tune the AI recommendation model. Oracle's machine learning engine curates recommendations automatically based on the learner's activity, skills, and Oracle's global skills intelligence. Custom recommendation algorithms or integration to a third-party recommendation engine are excluded.

---

## 31. Statutory Compliance and Reporting (SETA / WSP / ATR)

**LRN-SAT-001**  
Oracle Fusion Learning Cloud captures the learning data required for South African statutory reporting, including Workplace Skills Plan (WSP) and Annual Training Report (ATR) submissions to the relevant SETA. APPSolve configures Oracle Learning to capture training activity at the required level of detail. The statutory submission itself is the client's responsibility. APPSolve provides guidance on the Oracle Fusion Learning OTBI subject areas available for WSP/ATR data extraction. No bespoke SETA-specific OTBI report template or Skills Development Act–specific BI Publisher report is delivered in base scope. The client's Learning Administrator is responsible for generating OTBI data and populating the applicable WSP/ATR template. APPSolve does not submit WSP/ATR reports to any SETA on the client's behalf.

**LRN-SAT-002**  
Employment Equity (EEA2/EEA4) training tracking is supported through Oracle Learning completion records. APPSolve configures Oracle Learning to tag training activities by race, gender, and disability category as required for EE reporting. The client's HR team is responsible for extracting, validating, and submitting Employment Equity reports to the Department of Employment and Labour. HCM Base assumption HCM-EXC-012 applies.

**LRN-SAT-003**  
The accuracy of statutory reporting data depends on the completeness and accuracy of employee demographic records in Oracle HCM and learning completion records in Oracle Learning. The client is responsible for ensuring that employee demographic data and learning completion data are accurate before statutory extracts are generated.

**LRN-SAT-004**  
Oracle Fusion Learning Cloud does not produce a pre-formatted SETA WSP/ATR submission form. The OTBI extract provided by APPSolve outputs raw data that the client's Learning team maps to the applicable SETA template for their sector. The client's Learning and Development team is responsible for SETA template completion and submission timing.

---

## 32. Third-Party Learning System Integration

**LRN-3PT-001**  
Where the client requires integration between Oracle Fusion Learning Cloud and a third-party learning content platform or existing LMS (for example, Moodle, Skillstown, Docebo, Cornerstone, or equivalent), a maximum of one (1) standard third-party learning integration is included in base scope. Additional third-party learning integrations beyond the first are assessed and priced separately. Each third-party learning integration constitutes a separately scoped item. APPSolve configures Oracle OIC or Oracle's standard Learning Cloud connectors for the agreed integration. Third-party platform configuration and API provision is the vendor's and client's responsibility.

**LRN-3PT-002**  
Oracle Fusion Learning Cloud includes a standard Oracle connector for Moodle LMS and the Skillstown platform. Where these connectors are used, APPSolve configures the Oracle-side of the integration using the standard connector. The third-party platform's configuration for the integration is outside APPSolve's scope.

**LRN-3PT-003**  
LinkedIn Learning integration (enabling Oracle Learning to surface LinkedIn Learning content within the Oracle Learning interface) requires the client to hold active LinkedIn Learning licences. The integration is available via Oracle's standard LinkedIn Learning connector. APPSolve configures the Oracle-side integration where in scope; the client's LinkedIn Learning licence and content catalogue are the client's commercial responsibility.

**LRN-3PT-004**  
Third-party learning content library subscriptions — including Skillsoft (Percipio), LinkedIn Learning, Udemy Business, Coursera for Business, OpenSesame, and similar platforms — are commercial arrangements between the client and the content provider. The cost of content library subscriptions is not included in APPSolve's commercial proposal.

---

## 33. Learning Data Migration

**LRN-DAT-001**  
Historical learning completion data is migrated from the client's source system(s) for active employees only, covering a maximum of two (2) years of prior completion history. Completion records older than two years are excluded from migration. The client is responsible for extracting historical completion data from the source system and providing it in APPSolve's Oracle FBDI-compliant learning migration template.

**LRN-DAT-002**  
Only learning completion records (pass/fail/completed status, completion date, and score where available) are migrated. Detailed learner attempt logs, video playback progress, per-question assessment responses, and forum activity from the legacy system are excluded from migration.

**LRN-DAT-003**  
Where the client holds employee certification records with active expiry dates, these certifications may be migrated to Oracle Learning if the data is available in a structured format. The client provides certification data (employee ID, certification name, completion date, expiry date) in the required template. Certifications without structured expiry date data are out of scope for migration.

**LRN-DAT-004**  
The client is responsible for the accuracy of all historical learning completion data provided for migration. APPSolve confirms the data has loaded correctly into Oracle Learning; it does not validate historical completion records against source system reports.

---

## 34. Learning Training and Administration Assumptions

**LRN-TRN-001**  
APPSolve delivers train-the-trainer (TTT) learning training for three user populations: (1) **Learning Administrator** — catalogue management, content upload, assignment rule management, certification administration, SETA extract generation, and Oracle Learning system administration; (2) **Managers** — team learning overview, assigning mandatory learning to team members, monitoring completion, and approval of discretionary learning requests; (3) **Employees** — self-service learning, browsing and enrolling in courses, completing learning, accessing transcripts and certificates.

**LRN-TRN-002**  
The client's Learning Administrator is the primary post-go-live operational owner of Oracle Fusion Learning Cloud. APPSolve's implementation delivers a fully configured and operational learning environment; the ongoing task of catalogue management, content refresh, and learner enrolment is the Learning Administrator's responsibility from go-live.

---

## 35. Learning Exclusions

**LRN-EXC-001**  
**eLearning Authoring Tool Procurement and Licensing:** Articulate Storyline, Articulate Rise, Lectora Inspire, Adobe Captivate, iSpring, and all similar authoring tools are excluded from APPSolve's scope. These tools are the client's commercial responsibility. APPSolve specifies the content format requirements for Oracle Learning compatibility.

**LRN-EXC-002**  
**Historical Learning Data Beyond Two Years:** Learning completion records older than two years are excluded from migration. Where the client requires more than two years of historical data, this is assessed and priced as a scope addition. HCM Base assumption HCM-DAT-005 applies.

**LRN-EXC-003**  
**Third-Party Learning Content Library Subscriptions:** The cost of external content library subscriptions (Skillsoft/Percipio, LinkedIn Learning, Udemy Business, Coursera for Business, or equivalent) is excluded from APPSolve's commercial proposal. Content library procurement is the client's direct commercial arrangement with the content provider.

**LRN-EXC-004**  
**Oracle Learning Publisher (OLP):** Oracle Learning Publisher (the tool used to create Oracle-native learning content within the Oracle Learning platform) is an Oracle product feature. APPSolve provides awareness training to the Learning Administrator on Oracle Learning Publisher as part of standard Learning administration training. Dedicated Oracle Learning Publisher content authoring on behalf of the client is not in scope.

**LRN-EXC-005**  
**Statutory WSP/ATR Report Preparation and SETA Submission:** APPSolve configures Oracle Learning to capture the data required for statutory compliance reporting. Populating the WSP/ATR templates, completing the statutory submission, liaising with the relevant SETA, and managing submission deadlines are the client's responsibility. APPSolve does not prepare or submit statutory skills development reports on the client's behalf.

**LRN-EXC-006**  
**Legacy LMS Decommissioning:** Shutdown, data archival, and decommissioning of the client's legacy LMS (for example, Moodle, Cornerstone, SAP SuccessFactors Learning, or equivalent) after Oracle Learning go-live is the client's responsibility and is excluded from this engagement. HCM Base assumption HCM-EXC-008 applies.

**LRN-EXC-007**  
**Instructor-Led Training (ILT) Logistics and Venue Management:** While Oracle Learning supports Instructor-Led Training (ILT) course management, scheduling, and attendance tracking, the physical logistics of running ILT sessions (venue booking, catering, instructor travel, printed materials) is the client's responsibility and is not in scope.

**LRN-EXC-008**  
**Virtual Classroom Platform Integration:** Integration between Oracle Learning and a virtual classroom platform (Zoom, Microsoft Teams, Webex, or equivalent) for live ILT delivery is not included in base scope. Where the client requires virtual classroom integration, this is assessed and priced as a scope addition.

---

## Approval Record

All BU Lead review items confirmed. Status: **Approved v1.0 — 2026-06-19 (WP16C)**.

| Decision ID | Item | Confirmed Position | Resolved |
|---|---|---|---|
| BU-LRN-001 | Learning community count | Two (2) communities as standard in base scope | WP16C 2026-06-19 |
| BU-LRN-002 | Historical migration years | Two (2) years of completion history | WP15F 2026-06-19 |
| BU-LRN-003 | Third-party LMS integration count | One (1) standard integration in base scope; additional separately priced | WP16C 2026-06-19 |
| BU-LRN-004 | LinkedIn Learning connector | APPSolve configures Oracle-side connector where in scope; client licence required | WP15F 2026-06-19 |
| BU-LRN-005 | SETA extract format | OTBI guidance only; no bespoke SETA extract template in base scope | WP16C 2026-06-19 |

---

*HCM_LEARNING_ASSUMPTIONS_V1.1 | WP11 — Commercial Assumptions Library | 2026-06-15 | **Approved v1.0 — 2026-06-19 (WP16C)***  
*37 assumptions / exclusions / responsibilities across Sections 28–35 (+6 pending authoring — BAU v1.2 additions; sections defined, wording TBD)*  
*Parent pack: HCM_BASE_ASSUMPTIONS_V1.md | Governed under: 08_Commercial/ASSUMPTION_GOVERNANCE.md*
