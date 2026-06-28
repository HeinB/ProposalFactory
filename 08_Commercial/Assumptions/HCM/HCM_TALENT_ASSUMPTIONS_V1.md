---
document_id: HCM-TALENT-ASSUMPTIONS-V1
title: "Oracle Fusion Talent Management — Assumptions, Exclusions, and Customer Responsibilities"
version: "1.1"
status: "Approved v1.0"
created: "2026-06-15"
created_by: "WP11 — Commercial Assumptions Library"
approved_by: "Oracle HCM BU Lead"
approved_date: "2026-06-19"
approved_for_reuse: true
lifecycle_status: APPROVED
category: "Commercial / Assumptions"
scope: "Oracle Fusion Talent Management Cloud Service (B94925): Goal Management, Performance Management, Talent Review and Succession, Career Development. Extends HCM_BASE_ASSUMPTIONS_V1.md."
apply_with: "TENDER_ASSUMPTION_ASSEMBLY_RULES.md"
parent_pack: "HCM_BASE_ASSUMPTIONS_V1.md"
assumption_count: 31
oracle_part_number: "B94925"
kb_reference: "W3S1-002-ORA-TalentMgmt.md"
bu_lead_review_items: []
---

# Oracle Fusion Talent Management — Assumptions V1.0

**Scope:** This document governs Oracle Fusion Talent Management Cloud Service (B94925) implementations. It extends `HCM_BASE_ASSUMPTIONS_V1.md`. All four Talent Management sub-modules are in scope: Goal Management, Performance Management, Talent Review and Succession, and Career Development. Talent Profiles are configured as part of HCM Base (B85800); the Talent Management module deepens and activates them.

**Load order:** HCM Base Assumptions (complete) → this pack (additive). For full HCM suite proposals, also load relevant module packs for Learning, Compensation, and Recruiting.

---

## 36. Performance Management Assumptions

**TLT-PER-001**  
APPSolve configures Oracle Performance Management using Oracle-delivered performance document templates. The base scope includes: one (1) annual performance review template and one (1) mid-year check-in template. Each additional performance template (for example, a separate template for a specific job family, subsidiary, or employment type) constitutes a scope addition requiring a Change Request.

**TLT-PER-002**  
The rating model for Oracle Performance Management is confirmed during the Scope and Design phase. The default implementation is a single overall performance rating. Multi-dimension ratings (for example, separate ratings for performance, potential, and values alignment for a combined 9-box input) require a design decision and additional configuration effort to be agreed before Scope and Design commences.

**TLT-PER-003**  
Oracle Performance Management supports peer feedback and upward feedback (360-degree feedback) as a standard platform feature. APPSolve configures 360-degree feedback where included in the agreed Scope and Design. Where 360-degree feedback is not in scope, the performance template is configured for self-assessment and manager assessment only. The client confirms which feedback sources are required before template configuration commences.

**TLT-PER-004**  
Competency assessment within performance reviews requires a configured competency framework in Oracle HCM. The client is responsible for defining all competencies, proficiency levels, and their alignment to roles before performance template configuration commences. APPSolve configures the competency framework in Oracle HCM; the client defines the content.

**TLT-PER-005**  
Continuous feedback (employee and manager ad-hoc feedback outside the formal performance cycle) is an Oracle-delivered feature within Oracle Performance Management. APPSolve enables continuous feedback as part of the standard Talent Management configuration. No additional configuration is required; the feature is activated by enabling the relevant Oracle HCM profile option.

**TLT-PER-006**  
Oracle Performance Management workflow notifications (performance document assignment notifications, reminder notifications, approval notifications) are configured using Oracle's standard notification framework. Custom HTML-branded email templates are not included in base scope. HCM Base assumption HCM-WFL-004 applies.

---

## 37. Goal Management Assumptions

**TLT-GOL-001**  
APPSolve configures Oracle Goal Management to support the client's goal-setting and cascading process. The base scope includes: corporate-to-individual goal cascading; SMART goal configuration; goal weighting; goal progress tracking; and goal alignment across the management hierarchy. The goal framework design is agreed in the Scope and Design phase.

**TLT-GOL-002**  
A maximum of one (1) goal plan is configured in base scope. A goal plan defines the active goal cycle, period, and eligibility criteria. Additional goal plans (for example, separate goal cycles per business unit, subsidiary, or job family) constitute a scope addition. The client confirms the number of concurrent goal plans required before configuration commences.

**TLT-GOL-003**  
The client is responsible for defining and providing all corporate-level goals that are to be cascaded to employees before Oracle Goal Management configuration commences. APPSolve configures the Oracle goal framework and cascade mechanism; it does not define the client's corporate goals, strategic objectives, or performance targets.

**TLT-GOL-004**  
Goal weightings — the percentage weight assigned to each goal within an employee's goal plan — are configured according to rules provided by the client. APPSolve configures the weighting framework; the client defines the weighting rules (for example, all goals weighted equally; strategic goals weighted 60%; operational goals weighted 40%).

**TLT-GOL-005**  
Oracle Goal Management integrates with Oracle Performance Management so that goal achievement is reflected in the annual performance review. This integration is configured as part of the standard Talent Management implementation where both modules are in scope.

---

## 38. Talent Review and Succession Assumptions

**TLT-SUC-001**  
APPSolve configures Oracle Talent Review using Oracle's standard 9-box grid (performance vs potential axes) as the default calibration tool. The 9-box grid axes are labelled based on the client's confirmed performance and potential definitions. Custom calibration axes beyond performance and potential (for example, values alignment or engagement as a third dimension) are assessed as a scope addition.

**TLT-SUC-002**  
APPSolve configures Oracle Succession Planning for the succession plans agreed in the Scope and Design phase. The number of succession plans in scope is confirmed during Scope and Design; each additional succession plan beyond the agreed count constitutes a Change Request. Succession plans are built for agreed critical roles; the client identifies which roles require succession coverage before succession configuration commences.

**TLT-SUC-003**  
Oracle Talent Review supports unlimited talent pool creation (a platform capability). APPSolve configures the initial talent pool structure as agreed in the Scope and Design phase. Ongoing talent pool management (adding, moving, and rating talent pool members) is the HR team's responsibility after go-live.

**TLT-SUC-004**  
APPSolve configures Oracle Talent Review to support the client's HR Talent Review meeting process — including talent review meeting setup, participant configuration, and 9-box calibration capability. APPSolve does not facilitate or run the client's Talent Review meetings. Facilitating Talent Review meetings is an HR leadership responsibility.

**TLT-SUC-005**  
Talent readiness assessments (rating succession candidates as Ready Now, Ready in 1–2 Years, or Ready in 3+ Years) are configured within Oracle Talent Review. The client's HR team is responsible for populating and maintaining readiness ratings for nominated succession candidates after go-live.

---

## 39. Career Development Assumptions

**TLT-CAR-001**  
APPSolve configures Oracle Career Development to provide employees with self-service access to career path exploration, development plan creation, and learning recommendations aligned to career goals. Career path content (the roles, skills, qualifications, and development activities associated with each career path) is the client's responsibility. APPSolve configures the Oracle Career Development framework; the client populates career path content.

**TLT-CAR-002**  
Oracle Career Development includes integration with Oracle AI Dynamic Skills (HCM Base B85800). Skills gaps identified against a target role in the career path automatically surface as recommended learning items in Oracle Learning Cloud (where Learning Cloud is also in scope). APPSolve configures this end-to-end skills-to-learning integration as part of the Talent Management and Learning implementation.

**TLT-CAR-003**  
Development plans in Oracle Career Development are employee-owned and manager-supported. APPSolve configures the development plan framework and provides plan templates; employees and managers are responsible for creating and maintaining individual development plans after go-live. APPSolve does not create individual development plans for employees.

---

## 40. Talent Profile Assumptions

**TLT-PRO-001**  
Oracle Talent Profiles (part of HCM Base B85800) store employee competencies, qualifications, certifications, work history, and skills. APPSolve configures the talent profile fields and structure as agreed in the Scope and Design phase. The activation of talent profiles is part of the HCM Base implementation; the Talent Management pack extends talent profiles with performance, succession, and career development data.

**TLT-PRO-002**  
The client is responsible for defining the competency framework — including competency names, proficiency levels (for example: Developing, Proficient, Expert), and role-to-competency mappings — before talent profile configuration commences. APPSolve configures the Oracle competency framework based on the client's definitions.

**TLT-PRO-003**  
Talent profile completeness — the degree to which employee talent profiles are populated with skills, competencies, and career goal data — is the responsibility of employees and the HR team after go-live. APPSolve configures the Oracle system and enables profile completion workflows; it does not populate individual employee talent profiles.

**TLT-PRO-004**  
Oracle AI Dynamic Skills (HCM Base) continuously updates the skills dimension of talent profiles based on employee activity (role history, learning completions, performance data, and Oracle's global skills intelligence). APPSolve enables and configures the AI Dynamic Skills feature as part of the HCM Base implementation. Talent Management (B94925) activates the talent review, succession, and career development use cases for AI skills data.

---

## 41. Talent Management Training Assumptions

**TLT-TRN-001**  
APPSolve delivers train-the-trainer (TTT) training for Oracle Talent Management across four user populations: (1) **HR Administrators** — Talent Management module configuration and administration, goal plan management, performance cycle management, succession plan administration; (2) **HR Business Partners** — Talent Review facilitation, 9-box calibration, succession candidate management, career development guidance; (3) **Managers** — goal setting and cascading, performance reviews, continuous feedback, development plan oversight, talent review participation; (4) **Employees** — self-service goal setting, performance review completion, career path exploration, and development plan creation.

**TLT-TRN-002**  
APPSolve recommends that senior HR leaders (CHRO, HR Directors) who chair Talent Review meetings receive a dedicated orientation session on Oracle Talent Review's 9-box calibration interface. This orientation is included as part of the HR Business Partner training session (TLT-TRN-001). A separate executive briefing session is available as an optional service.

---

## 42. Talent Management Exclusions

**TLT-EXC-001**  
**OKR (Objectives and Key Results) Management:** Where the client operates an OKR framework distinct from SMART goals, the Oracle Goal Management module supports structured goal-setting but is not a dedicated OKR platform. Clients requiring deep OKR capability (OKR hierarchies, real-time OKR tracking dashboards, OKR-specific team alignment views) should confirm Oracle Goal Management meets their OKR requirements during the Scope and Design phase. Dedicated OKR platform integration (Lattice, Betterworks, Ally.io, or equivalent) is excluded.

**TLT-EXC-002**  
**Third-Party Psychometric Assessment Integration:** Integration between Oracle Talent Management and third-party psychometric assessment platforms (Hogan Assessments, SHL/Talogy, Korn Ferry Assessment, MHS Talent, or equivalent) is excluded from base scope. These assessments are typically administered externally; results may be recorded manually in Oracle HCM talent profiles. OIC integration to a psychometric platform is a separately scoped and priced addition.

**TLT-EXC-003**  
**External Talent Market Intelligence and Benchmarking:** Oracle Talent Management does not include external talent market benchmarking or labour market intelligence (for example, LinkedIn Talent Insights, Mercer Comptryx, or Korn Ferry benchmarking data). Such data is sourced from third-party providers and is the client's commercial arrangement.

**TLT-EXC-004**  
**Talent Acquisition Integration (Recruiting-to-Talent):** Where Oracle Fusion Recruiting Cloud (B87675) is also in scope, the transition of a hired candidate into Oracle HCM and the activation of their talent profile is included in the Recruiting implementation. Where Oracle Recruiting is not in scope, no Recruiting-to-Talent integration is included.

**TLT-EXC-005**  
**HR Talent Review Meeting Facilitation:** APPSolve configures Oracle Talent Review to support the client's Talent Review process. Running, facilitating, and moderating Talent Review meetings is the HR leadership's responsibility and is not in APPSolve's scope.

**TLT-EXC-006**  
**Long-Term Incentive (LTI) Tracking Integration:** Tracking of long-term incentive awards (restricted share units, share options, performance shares) within Oracle HCM is not supported by Oracle Talent Management. Long-term incentive administration is typically managed by a dedicated equity management platform (Certent, Morgan Stanley Equity Edge, or similar). Integration to an equity management platform is excluded unless explicitly scoped.

---

## Approval Record

All BU Lead review items confirmed. Status: **Approved v1.0 — 2026-06-19 (WP16C)**.

| Decision ID | Item | Confirmed Position | Resolved |
|---|---|---|---|
| BU-TLT-001 | Performance template count | One (1) annual review + one (1) mid-year check-in as standard | WP16C 2026-06-19 |
| BU-TLT-002 | 360-degree feedback | Configured where included in agreed Scope and Design | WP15F 2026-06-19 |
| BU-TLT-003 | Succession plan count | No default limit — confirmed per engagement in Scope and Design | WP16C 2026-06-19 |
| BU-TLT-004 | Career path configuration | Configure Oracle Career Development framework where client provides career path content | WP16C 2026-06-19 |

---

*HCM_TALENT_ASSUMPTIONS_V1.1 | WP11 — Commercial Assumptions Library | 2026-06-15 | **Approved v1.0 — 2026-06-19 (WP16C)***  
*31 assumptions / exclusions / responsibilities across Sections 36–42 (+7 pending authoring — BAU v1.2 additions; sections defined, wording TBD)*  
*Parent pack: HCM_BASE_ASSUMPTIONS_V1.md | Governed under: 08_Commercial/ASSUMPTION_GOVERNANCE.md*
