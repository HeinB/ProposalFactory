---
document_id: WP16B-LOW-PRIORITY
title: "WP16B — Oracle HCM Low Priority Batch Approval Pack"
version: "1.0"
created: "2026-06-19"
created_by: "WP16B — Oracle HCM Final Governance Closure"
status: "Awaiting BU Lead Email Approval"
decisions_covered: "BU-REC-007, BU-LRN-001, BU-LRN-003, BU-LRN-005, BU-TLT-001, BU-TLT-003, BU-TLT-004, BU-COM-001, BU-COM-002, BU-COM-005"
priority: "LOW"
decision_count: 10
---

# WP16B — Oracle HCM Low Priority Batch Approval Pack

**Date:** 2026-06-19 | **Decisions:** 10 LOW | **Route:** Single batch email to Oracle HCM BU Lead | **Format:** Approve-or-redirect each recommended default

> **Context for BU Lead:** These 10 decisions are factual defaults — "what is our standard count or position for this capability?" Each has a recommended answer already embedded in the draft assumption. A senior Oracle HCM Consultant can confirm these without a workshop. The recommended option for each is shown; reply with "Confirmed" or indicate if you want to redirect a specific item.

---

## How to Respond

Reply to the email with a list confirming or redirecting each decision. Example:

> BU-REC-007: Confirmed
> BU-LRN-001: Redirect — we typically use 3 communities as our standard
> BU-LRN-003 through BU-COM-005: All confirmed

Partial confirmations are fine. Any redirected decision will be updated before pack promotion.

---

## RECRUITING MODULE — 1 Decision

---

### BU-REC-007 — Requisition Template Count

**Question:** Does APPSolve use a standard default number of requisition templates and approval workflow variants in scope, or is this confirmed per engagement?

**Recommendation:** No default count. The number of requisition templates and approval workflow variants is agreed and fixed in the Scope and Design phase. Each additional template or variant beyond the agreed count is a scope change.

**Why no default?** Requisition template complexity varies significantly — a client with 3 business units may need 5 templates; a multi-division enterprise may need 30. Unlike career sites or offer letters (where a sensible baseline exists), requisition templates are too client-specific to carry a numeric default.

**Current draft assumption (REC-REQ-001):**
> "The number of distinct requisition templates and approval workflow variants is agreed in the Scope and Design phase. Each additional requisition template or approval variant beyond the agreed count constitutes a scope change."

**Pack change if confirmed:** Remove `*(Pending BU-REC-007)*` from REC-REQ-001. No wording change required.

**Confirm?** → BU-REC-007: Confirmed *(or redirect with preferred default)*

---

## LEARNING MODULE — 3 Decisions

---

### BU-LRN-001 — Learning Community Count

**Question:** What is APPSolve's standard number of Oracle Fusion Learning Communities configured in base scope?

**Recommendation:** Two (2) learning communities as standard (e.g., one for permanent employees, one for contractors or extended workforce).

**Why 2?** Most clients have two primary learner populations requiring separate community branding, catalogue visibility rules, or completion requirements. A single community is frequently insufficient; three or more is generally a phased-implementation consideration rather than a standard baseline.

**Current draft assumption (LRN-PLT-002) — requires placeholder fill:**
> "A maximum of **[CONFIRM — BU Lead]** learning communities are configured in base scope. Each learning community has its own home page, catalogue visibility rules, and learner group assignment. Additional learning communities beyond the base count are assessed and priced as a scope extension."

**Pack change if confirmed:** Replace `[CONFIRM — BU Lead]` with `two (2)`. Remove `*(Pending BU-LRN-001)*` tag. This is the only LOW decision requiring a wording fill.

**Confirm?** → BU-LRN-001: Confirmed at 2 communities *(or redirect with preferred number)*

---

### BU-LRN-003 — Third-Party Learning Integration Count

**Question:** What is APPSolve's standard number of third-party learning platform integrations included in base scope?

**Recommendation:** One (1) standard third-party integration is included in base scope. Additional integrations are assessed and priced separately.

**Typical use case:** Client integrates Oracle Fusion Learning with one existing content platform (e.g., LinkedIn Learning connector, Udemy Business, or a SCORM content library). A second integration (e.g., adding a compliance-training platform) would be separately scoped.

**Current draft assumption (LRN-3PT-001) — minor wording update required:**
> "Where the client requires integration between Oracle Fusion Learning Cloud and a third-party learning content platform or LMS, a maximum of one (1) standard integration is included in base scope. Additional third-party learning integrations are assessed and priced separately. Each integration constitutes a separately scoped item."

**Pack change if confirmed:** Confirm wording above. Remove `*(Pending BU-LRN-003)*` tag. Minor wording update to add explicit "one (1)" where current draft says count "agreed in Scope and Design."

**Confirm?** → BU-LRN-003: Confirmed at 1 standard integration *(or redirect with preferred default)*

---

### BU-LRN-005 — SETA Extract Format (WSP/ATR Reporting)

**Question:** When clients require WSP/ATR SETA reporting outputs, does APPSolve deliver a bespoke SETA extract template, or does it provide guidance on available OTBI subject areas?

**Recommendation:** OTBI guidance only. APPSolve provides guidance on relevant Oracle Fusion Learning OTBI subject areas for WSP/ATR data. No bespoke SETA extract template or custom BI Publisher report is delivered in standard scope.

**Why OTBI guidance only?** SETA reporting templates differ by SETA (CHIETA vs MERSETA vs CETA etc.) and by the client's HR department's internal reporting processes. A single "standard" SETA extract cannot be correct for all clients. APPSolve equips the Learning Administrator with the OTBI data they need to populate their SETA's specific WSP/ATR template.

**Current draft assumption (LRN-SAT-001):**
> "Where clients require data for Skills Development Levy (SDL) and SETA reporting, APPSolve provides guidance on the Oracle Fusion Learning OTBI subject areas available for WSP/ATR reporting. No bespoke SETA extract template or Skills Development Act–specific BI Publisher report is delivered in base scope. The client's Learning Administrator is responsible for completing WSP/ATR templates using OTBI-sourced data."

**Pack change if confirmed:** Remove `*(Pending BU-LRN-005)*` tag. Confirm above wording.

**Confirm?** → BU-LRN-005: Confirmed — OTBI guidance only, no bespoke SETA extract *(or redirect)*

---

## TALENT MANAGEMENT MODULE — 3 Decisions

---

### BU-TLT-001 — Performance Review Template Count

**Question:** What is APPSolve's standard number and type of Oracle Fusion Performance review templates configured in base scope?

**Recommendation:** One (1) annual performance review template and one (1) mid-year check-in template — two templates total.

**Why this default?** The annual review / mid-year check-in combination is the most common Oracle Fusion Performance configuration. Both templates are structurally similar and can be configured efficiently as a pair. Additional review types (e.g., probationary reviews, project-based reviews, continuous feedback structures) are assessed per engagement.

**Current draft assumption (TLT-PER-001) — already reflects recommendation:**
> "The base scope includes: one (1) annual performance review template; and one (1) mid-year check-in template. Additional performance review types (probation reviews, project-based reviews, continuous check-in flows) are assessed and priced separately."

**Pack change if confirmed:** Remove `*(Pending BU-TLT-001)*` tag. No wording change required.

**Confirm?** → BU-TLT-001: Confirmed — 1 annual + 1 mid-year *(or redirect with preferred default)*

---

### BU-TLT-003 — Succession Plan Count

**Question:** Does APPSolve use a default number of Oracle Fusion Succession Plans in scope, or is this confirmed per engagement?

**Recommendation:** No default count. The number of succession plans in scope is confirmed during the Scope and Design phase.

**Why no default?** Succession planning scope varies significantly by client maturity and organisational complexity. A lean organisation may want 1 succession pool for critical roles; a multi-division enterprise may require 20+ talent pools covering C-suite, functional directors, and regional leadership. A numeric default would either under-scope large clients or over-commit to small ones.

**Current draft assumption (TLT-SUC-002):**
> "The number of succession plans and talent pools configured in base scope is confirmed during the Scope and Design phase; each additional plan beyond the agreed count constitutes a Change Request."

**Pack change if confirmed:** Remove `*(Pending BU-TLT-003)*` tag. No wording change required.

**Confirm?** → BU-TLT-003: Confirmed — no default count, agreed in Scope and Design *(or redirect)*

---

### BU-TLT-004 — Career Path Configuration

**Question:** What is APPSolve's standard position on Oracle Career Development (career path) configuration — does APPSolve define career path content, or only configure the Oracle framework?

**Recommendation:** APPSolve configures the Oracle Career Development framework; career path content is the client's responsibility. APPSolve does not define, maintain, or populate career path data (roles, qualifications, skills, development activities) as part of standard scope.

**Why client-owned content?** Career paths are organisation-specific. The client's HR strategy team must define the roles, skills, and progression logic. APPSolve's role is to configure the Oracle platform to carry client-provided content, not to create that content from scratch.

**Current draft assumption (TLT-CAR-001):**
> "Oracle Career Development framework configuration is included in base scope where the client confirms that career path content is available and ready for configuration. Career path content (roles, required qualifications, skills profiles, and development activity assignments for each path) is the client's responsibility to define and provide. APPSolve configures the Oracle framework to reflect client-supplied content; APPSolve does not author career path content."

**Pack change if confirmed:** Remove `*(Pending BU-TLT-004)*` tag. Confirm above wording.

**Confirm?** → BU-TLT-004: Confirmed — configure framework; client owns content *(or redirect)*

---

## COMPENSATION MODULE — 3 Decisions

---

### BU-COM-001 — Merit Plan Count

**Question:** What is APPSolve's standard number of Oracle Fusion Workforce Compensation merit plans configured in base scope?

**Recommendation:** One (1) merit plan as the standard base scope.

**Why 1?** A single organisation-wide merit plan covers the most common scenario — one annual merit cycle for all eligible employees. Clients with multiple business units requiring separate merit budgets, eligibility rules, or manager worksheet configurations need additional plans, which are assessed per engagement.

**Current draft assumption (COM-PLN-001) — already reflects recommendation:**
> "A maximum of one (1) merit plan is configured in base scope. This plan supports a standard annual merit review cycle. Additional merit plans (e.g., for separate business units with distinct eligibility populations, separate merit budget hierarchies, or off-cycle merit adjustments) are assessed and priced separately."

**Pack change if confirmed:** Remove `*(Pending BU-COM-001)*` tag. No wording change required.

**Confirm?** → BU-COM-001: Confirmed — 1 merit plan in standard scope *(or redirect)*

---

### BU-COM-002 — Bonus / Incentive Plan Count

**Question:** What is APPSolve's standard number of Oracle Fusion Workforce Compensation short-term incentive (bonus) plans configured in base scope?

**Recommendation:** One (1) bonus/short-term incentive plan as the standard base scope.

**Why 1?** A single STI plan covers the most common implementation scenario — one annual bonus cycle for all eligible employees. Clients with multiple incentive structures (e.g., sales commission plan + corporate bonus + regional incentive) require additional plans, each assessed separately.

**Current draft assumption (COM-PLN-002) — already reflects recommendation:**
> "A maximum of one (1) short-term incentive (bonus) plan is configured in base scope. This plan supports a standard annual bonus review cycle. Additional incentive plans (e.g., sales commission structures, tiered incentive programmes, or separate divisional bonus pools) are assessed and priced separately."

**Pack change if confirmed:** Remove `*(Pending BU-COM-002)*` tag. No wording change required.

**Confirm?** → BU-COM-002: Confirmed — 1 bonus plan in standard scope *(or redirect)*

---

### BU-COM-005 — Pay Equity Reporting

**Question:** Does APPSolve deliver a standard pay equity analysis report/extract, or does it provide guidance on available OTBI subject areas?

**Recommendation:** OTBI guidance only. No standard pay equity extract or report template is delivered in base scope.

**Why OTBI guidance only?** Pay equity analysis requirements differ significantly by client (earnings gap analysis by gender, race, grade, or employment equity category). South African Employment Equity reporting requirements and internal pay equity frameworks vary by organisation. A single standard extract cannot serve all use cases. APPSolve guides the client's HR Analytics team on which OTBI Compensation and HR subject areas contain the data fields needed for their specific pay equity analysis.

**Current draft assumption (COM-DAT-004):**
> "Where pay equity analysis reporting is required, APPSolve provides guidance on the Oracle Fusion Compensation and HCM OTBI subject areas relevant to pay gap analysis and Employment Equity reporting. No standard pay equity extract template or Employment Equity-specific BI Publisher report is delivered in base Compensation scope. Pay equity analysis design and reporting is the client's responsibility, using OTBI subject areas identified during knowledge transfer."

**Pack change if confirmed:** Remove `*(Pending BU-COM-005)*` tag. Confirm above wording.

**Confirm?** → BU-COM-005: Confirmed — OTBI guidance only, no standard pay equity extract *(or redirect)*

---

## Confirmation Summary Template

> Copy and reply with your confirmations:
>
> **BU-REC-007:** Confirmed / [Redirect:]
> **BU-LRN-001:** Confirmed — 2 communities / [Redirect:]
> **BU-LRN-003:** Confirmed — 1 standard integration / [Redirect:]
> **BU-LRN-005:** Confirmed — OTBI guidance only / [Redirect:]
> **BU-TLT-001:** Confirmed — 1 annual + 1 mid-year / [Redirect:]
> **BU-TLT-003:** Confirmed — no default, confirmed per engagement / [Redirect:]
> **BU-TLT-004:** Confirmed — configure framework, client owns content / [Redirect:]
> **BU-COM-001:** Confirmed — 1 merit plan / [Redirect:]
> **BU-COM-002:** Confirmed — 1 bonus plan / [Redirect:]
> **BU-COM-005:** Confirmed — OTBI guidance only / [Redirect:]

---

## What Happens After Confirmation

| On confirmation | Pack changes required |
|---|---|
| BU-REC-007 confirmed | Remove tag from REC-REQ-001. No wording change. |
| BU-LRN-001 confirmed | Replace "[CONFIRM — BU Lead]" with "two (2)" in LRN-PLT-002. Remove tag. |
| BU-LRN-003 confirmed | Confirm/update LRN-3PT-001 wording to state "one (1) standard integration". Remove tag. |
| BU-LRN-005 confirmed | Confirm LRN-SAT-001 wording. Remove tag. |
| BU-TLT-001 confirmed | Remove tag from TLT-PER-001. No wording change. |
| BU-TLT-003 confirmed | Remove tag from TLT-SUC-002. No wording change. |
| BU-TLT-004 confirmed | Confirm TLT-CAR-001 wording. Remove tag. |
| BU-COM-001 confirmed | Remove tag from COM-PLN-001. No wording change. |
| BU-COM-002 confirmed | Remove tag from COM-PLN-002. No wording change. |
| BU-COM-005 confirmed | Confirm COM-DAT-004 wording. Remove tag. |

**After all 10 LOW decisions confirmed (+ 2 HIGH from HIGH Priority Pack):**
All 4 HCM module packs will be cleared for the promotion pass — authoring the remaining +23 pending assumptions, removing all BU Lead pending tags, updating frontmatter, and promoting each pack to Approved v1.0.

---

*WP16B_HCM_LOW_PRIORITY_APPROVAL_PACK v1.0 | WP16B | 2026-06-19 | Awaiting Oracle HCM BU Lead batch email confirmation*
