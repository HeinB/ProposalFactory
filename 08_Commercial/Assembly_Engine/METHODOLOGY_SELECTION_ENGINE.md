---
document_id: METHODOLOGY-SELECTION-ENGINE
title: "Methodology Selection Engine — Pattern-to-Methodology Lookup"
version: "1.0"
status: "Approved — WP18C.3"
created: "2026-06-25"
created_by: "WP18C.3 — Tender Intelligence Layer"
category: "Architecture / Intelligence Layer"
scope: "Defines the deterministic pattern-to-methodology lookup for all 13 delivery patterns. For each pattern: methodology asset, project plan template, phase structure, and section inclusions/exclusions driven by methodology type. Input: proposal_pattern from Tender Profile. Output: methodology_asset, project_plan_template, phase_structure, methodology-driven section list."
---

# Methodology Selection Engine

**Date:** 2026-06-25 | **Version:** 1.0 | **Status:** Approved  
**Work Package:** WP18C.3 — Tender Intelligence Layer  
**Input:** `proposal_pattern` from Tender Profile Block G  
**Output:** `methodology_asset`, `project_plan_template`, phase structure, section scope impact

---

## 1. Purpose

The Methodology Selection Engine determines, from the proposal pattern, which methodology document to use and which project plan template to apply. It eliminates the manual Stage 5 process identified in WP18C.1.

**Selection principle:** Methodology is determined by platform and engagement type, not by client request. A client asking for "Oracle AIM" gets W2S1-005; a client asking for "agile delivery" gets W5-METH-001 with agile framing from the available asset.

**AMS rule:** Patterns 13 and 10 do not use a project plan template. AMS and DBA managed services have no implementation timeline; sections S-34 and S-35 are excluded entirely.

---

## 2. Master Lookup Table

| Pattern | Name | Methodology Asset | Project Plan Template | Phase Structure | Sections Excluded by Methodology |
|---|---|---|---|---|---|
| Pattern 1 | HCM Full Suite — Single Go-Live | W2S1-005 | PT-01 | MOB → SDD → PRO → VAL → DEP → EVO | None additional |
| Pattern 2 | HCM Full Suite — Phased Go-Live | W2S1-005 | PT-02 | MOB → SDD → PRO-W1 → VAL-W1 → DEP-W1 → PRO-W2 → VAL-W2 → DEP-W2 → EVO | None additional |
| Pattern 3 | HCM Core + Payroll Interface | W2S1-005 | PT-03 | MOB → SDD → PRO → VAL → DEP → EVO | None additional |
| Pattern 4 | Recruiting Cloud Standalone | W2S1-005 | PT-04 | MOB → SDD → PRO → VAL → DEP → EVO | S-40 (migration not standard for Recruiting standalone) |
| Pattern 5 | Learning Cloud Standalone | W2S1-005 | PT-05 | MOB → SDD → PRO → VAL → DEP → EVO | None additional |
| Pattern 6 | OIC Integration Standalone | W2S1-005 | PT-06 | MOB → SDD → PRO → VAL → DEP → EVO | S-34 (abbreviated), S-41 (no training standard for integration) |
| Pattern 7 | Oracle Fusion ERP Multi-Module | W2S1-005 | PT-07 | MOB → SDD → PRO → VAL → DEP → EVO | None additional |
| Pattern 8 | Oracle Fusion ERP Single Module | W2S1-005 | PT-08 | MOB → SDD → PRO → VAL → DEP → EVO | None additional |
| Pattern 9 | Oracle EBS Implementation | W2S1-005 | PT-09 | MOB → SDD → PRO → VAL → DEP → EVO | None additional |
| Pattern 10 | Oracle DBA / Managed Services | **None** | **None** | Onboarding → Stabilisation → BAU | S-34, S-35, S-39, S-40, S-41, S-42, S-43 |
| Pattern 11 | Acumatica ERP | W5-METH-001 | PT-11 | MOB → SDD → PRO → VAL → DEP → EVO | None additional |
| Pattern 12 | BeBanking H2H | W5-METH-001 | PT-12 | MOB → SDD → PRO → Bank Testing → DEP → EVO | S-34 (optional — abbreviated) |
| Pattern 13 | AMS / Managed Services | **None** | **None** | Onboarding → Stabilisation → BAU | S-34, S-35, S-38, S-39, S-40, S-41, S-42, S-43 |

---

## 3. Methodology Asset Specifications

### W2S1-005 — Oracle Consulting Methodology

**Applies to:** Patterns 1–9 (Oracle Fusion and EBS implementation)  
**Content:** Oracle AIM-derived implementation methodology tailored to APPSolve delivery standards  
**Sections it populates:** S-34 (Implementation Methodology), S-36 (Project Governance), S-37 (RAID Framework)  
**Phase code definitions:** MOB / SDD / PRO / VAL / DEP / EVO / PM

**Phase narrative by pattern:**

| Phase | Pattern 1/2 (HCM Full Suite) | Pattern 7/8 (ERP) | Pattern 9 (EBS) |
|---|---|---|---|
| MOB | Kick-off pack, RAID log, comms plan, environment access | Chart of accounts workshop, LE structure confirmation | Environment access, DBA setup if required |
| SDD | Business Process Design workbooks per module; SDD document; gap register; BR100 | Financial design workbooks; procurement catalogue; bank integration spec | AIM documentation; EBS config plan |
| PRO | Configured system, CRP cycles (min 2), integration unit tests, data migration template | GL/AP/AR/FA/Procurement config; CRP cycles; OIC bank integration build | EBS config; DBA production setup; APEX if in scope |
| VAL | SIT (1–2 cycles), UAT (client-led), defect register, data migration mock 1 | SIT; UAT; data migration mock 1; financial reconciliation | SIT; UAT; CEMLI testing |
| DEP | Data migration mock 2 + final; cutover plan; production readiness checklist; go-live | Data migration mock 2 + final; financial year-end go-live preferred | Data migration; cutover; DBA production |
| EVO | Hypercare 4 weeks; stabilisation log | Hypercare; month-end close support | Hypercare |

**Hypercare standard (all Oracle implementation patterns):**
- Week 1: named functional lead on-call
- Week 2: senior consultant 4-hour response
- Weeks 3–4: consultant 1-business-day response

**Parallel run rule (HCM patterns with payroll interface):** Parallel run INCLUDED by default (HCM-CUT-005). Minimum 1 payroll cycle. Client waiver requires written acceptance of risk.

**ERP data migration standard:**
- Opening balance migration only (standard); full transaction history = CR (ERP-DAT-006)
- 2 migration mocks + final cutover (standard); third mock = CR
- Financial year-end go-live strongly preferred — flag if not available in the tender

### W5-METH-001 — Platform-Agnostic Methodology

**Applies to:** Patterns 11 (Acumatica) and 12 (BeBanking)  
**Content:** Platform-neutral project methodology applicable to non-Oracle platforms  
**Sections it populates:** S-34, S-36, S-37

**BeBanking additional note (Pattern 12):**  
Bank testing timelines are bank-controlled and can extend significantly beyond the standard PRO phase. The Bank Testing phase must include an explicit disclaimer in the proposal: *"Bank testing timelines are controlled by the client's bank and are outside APPSolve's direct control. The indicative timeline assumes [X] weeks of bank testing; actual duration may vary."*

**Acumatica additional note (Pattern 11):**  
Acumatica has no standard parallel run for payroll (PaySpace is always the payroll SOR; Acumatica has no SA payroll functionality). Do not include HCM-CUT-005 parallel run language for Acumatica proposals.

### No Methodology — AMS (Pattern 13) and DBA (Pattern 10)

**Applies to:** Patterns 10 and 13  
**Reason:** These are managed services contracts with no implementation timeline. The delivery structure is Onboarding → Stabilisation → BAU, not a project lifecycle.  
**What replaces methodology sections:** S-70 (Support Model), S-71 (SLA Framework), S-72 (Incident Management), S-73 (CR Process), S-74 (Resource Model), S-75 (Release Management), S-76 (Monitoring). These sections collectively replace S-34/S-35 for AMS and are sourced from AMS assumption packs rather than methodology assets.

---

## 4. Project Plan Template Reference

Templates are held in PROJECT_PLAN_TEMPLATES.md. Each template provides:
- Week-by-week activity schedule (phase coded: MOB/SDD/PRO/VAL/DEP/EVO/PM)
- Resource allocation model (roles per week)
- Key milestone dates (placeholder — actual dates populated from `submission_deadline` and agreed kick-off)

| Template ID | Pattern | Typical Duration | Key Distinguishing Feature |
|---|---|---|---|
| PT-01 | Pattern 1 (HCM Full Suite Single) | 35–46 weeks | CRP minimum 2 rounds; 2 migration mocks + final |
| PT-02 | Pattern 2 (HCM Full Suite Phased) | 44–58 weeks | Dual-wave structure; Wave 1 and Wave 2 go-live events |
| PT-03 | Pattern 3 (HCM + Payroll Interface) | 24–38 weeks | PaySpace parallel run period; OIC integration build within PRO |
| PT-04 | Pattern 4 (Recruiting Standalone) | 19–29 weeks | Career site build; ATS migration assessment; hiring manager UAT |
| PT-05 | Pattern 5 (Learning Standalone) | 18–26 weeks | Content loading approach; SETA validation in VAL |
| PT-06 | Pattern 6 (OIC Standalone) | 16–23 weeks | Per-integration unit tests; end-to-end performance testing |
| PT-07 | Pattern 7 (ERP Multi-Module) | 34–42 weeks | Financial year-end go-live preferred; bank integration build within PRO |
| PT-08 | Pattern 8 (ERP Single Module) | 21–29 weeks | Simplified from PT-07; one module focus |
| PT-09 | Pattern 9 (Oracle EBS) | 33–41 weeks | AIM documentation; CEMLI testing in VAL; DBA setup in PRO |
| PT-10 | Pattern 10 (DBA Managed Services) | Ongoing | Onboarding 3–4 weeks + Stabilisation 2 weeks + BAU monthly |
| PT-11 | Pattern 11 (Acumatica ERP) | 24–34 weeks | Customisation list in SDD; PaySpace integration in PRO |
| PT-12 | Pattern 12 (BeBanking H2H) | 21–30 weeks | Bank Testing phase (bank-controlled; variable duration) |
| PT-13 | Pattern 13 (AMS Onboarding) | Ongoing | Onboarding 3–4 weeks + Stabilisation 2 weeks + BAU monthly |

---

## 5. Section Impact by Methodology Type

### Oracle Methodology (W2S1-005) — Sections Populated

| Section ID | Section Name | Methodology Contribution |
|---|---|---|
| S-34 | Implementation Methodology | Direct: methodology overview, phase descriptions, key activities |
| S-35 | Project Plan / Timeline | Template PT-xx applied; dates derived from submission_deadline + agreed kick-off |
| S-36 | Project Governance | W2S1-005 Sections 11–12: governance structure, steering committee, RAID |
| S-37 | RAID Framework | Methodology asset (risk / action / issue / decision log structure) |
| S-39 | Testing Strategy | Delivery pattern (CRP/SIT/UAT cycle definitions from pattern) |
| S-42 | Cutover / Go-Live Plan | Pattern-specific cutover; HCM-CUT-005 parallel run default if payroll in scope |
| S-43 | Hypercare / Transition | Pattern-specific hypercare model (weeks 1–4 structure) |

### Platform-Agnostic Methodology (W5-METH-001) — Sections Populated

Same sections as W2S1-005 but sourced from W5-METH-001 content. Phase structure aligns to the same MOB/SDD/PRO/VAL/DEP/EVO code set.

### No Methodology (Patterns 10, 13) — Replacement Sections

| Replaced By | Section ID | Section Name |
|---|---|---|
| S-70 | Support Model | Replaces high-level delivery model |
| S-71 | SLA Framework | Replaces project governance for managed services |
| S-72 | Incident Management | Replaces testing strategy |
| S-73 | Change Request Process | Replaces change control |
| S-74 | Resource Model (AMS) | Replaces team structure |
| S-75 | Release Management | — |
| S-76 | Monitoring and Reporting | — |

---

## 6. Combination Pattern Methodology Rules

When a tender spans multiple patterns:

**Implementation + AMS (Hybrid):**
- Use W2S1-005 for the implementation component (S-34, S-35, S-39, S-42, S-43)
- Use AMS assumption pack content for AMS component (S-70–S-76)
- Both sets of sections appear in the proposal with clear labelling

**Multi-product tenders (e.g. Oracle EBS + BeBanking):**
- Use the primary platform's methodology
- If Oracle EBS is primary → W2S1-005
- BeBanking sections (S-29) are included with methodology narrative from W5-METH-001 for the BeBanking phase

---

## 7. Methodology Authoring Gap Status

| Asset | Status | Gap Note |
|---|---|---|
| W2S1-005 — Oracle Consulting Methodology | Available | — |
| W5-METH-001 — Platform-Agnostic Methodology | Available | — |
| W2S1-006 — Security / DR Methodology | NOT YET CREATED | WP18B-METH4 — Priority P5 on revised roadmap |
| W2S1-007 — Oracle ERP Methodology (dedicated) | NOT YET CREATED | WP18B-METH2 — Priority P7 on revised roadmap |
| Cross-BU Methodology | NOT YET CREATED | WP18B-METH1 — deprioritised (P9); AMS engagements don't use methodology sections |

---

*METHODOLOGY_SELECTION_ENGINE.md v1.0 | WP18C.3 — Tender Intelligence Layer | 2026-06-25*  
*Companion: DELIVERY_PATTERN_LIBRARY.md | PROJECT_PLAN_TEMPLATES.md | PROPOSAL_PATTERN_ENGINE.md*
