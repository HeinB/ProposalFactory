---
document_id: DELIVERY-PATTERN-LIBRARY
title: "Delivery Pattern Library"
version: "1.0"
created: "2026-06-16"
created_by: "WP12 — Proposal Assembly Engine"
status: "Active"
---

# Delivery Pattern Library

**Purpose:** Defines the standard delivery pattern for each major engagement scenario. Use these patterns to select the appropriate project plan template, resource model, testing strategy, and hypercare structure.

**How to use:**
1. Match the engagement to the closest pattern.
2. Read pattern restrictions and client-readiness notes.
3. Use the linked project plan template (PROJECT_PLAN_TEMPLATES.md) for the week-based timeline.
4. Add notes where the actual engagement deviates from the pattern.

**Phase codes:** MOB (Mobilize) | SDD (Scope & Design) | PRO (Prototype) | VAL (Validate) | DEP (Deploy) | EVO (Evolve) | PM (Project Management — cross-phase)

---

## Pattern 1 — Oracle HCM Full Suite (Single Go-Live)

**Applies to:** Core HR + 4 or more modules (Recruiting, Learning, Talent, Compensation, Absence, Journeys, AI Skills, Payroll Interface) going live simultaneously.

| Phase | Typical Duration | Key Deliverables |
|---|---|---|
| MOB | 2 weeks | Kick-off pack, RAID log, comms plan, environment access confirmed |
| SDD | 6–8 weeks | Business Process Design workbooks (per module), SDD document, gap register, LE config register, BR100 (configuration plan) |
| PRO | 14–18 weeks | Configured and validated system, CRP cycles (min 2), integration unit tests, custom report prototypes, data migration template |
| VAL | 6–8 weeks | SIT (1–2 cycles), UAT (client-led), defect register, sign-off, data migration mock 1 |
| DEP | 3–4 weeks | Data migration mock 2 + final, cutover plan, production readiness checklist, go-live |
| EVO | 4 weeks | Hypercare (4 weeks post go-live), stabilisation log |
| PM | Cross-phase | Weekly status report, steering committee pack, monthly financial status |

**Typical total duration:** 35–46 weeks

**Resource model:** HCM Principal (lead); 2–4 Senior HCM Module Specialists; OIC Consultant (if integrations); Project Manager; Programme Manager (large deals).

**On-site requirements:** Kick-off (full team on-site); SDD workshops (on-site preferred); CRP sessions (on-site preferred); UAT support (on-site or hybrid); Cutover week (on-site).

**Testing cycles:**
- CRP: minimum 2 rounds within PRO phase
- SIT: 1–2 rounds within VAL phase (APPSolve-led)
- UAT: 1–2 rounds within VAL phase (client-led, APPSolve support)
- Data migration mocks: 2 mock runs + final cutover run

**Hypercare standard:** W1 = named functional lead on-call; W2 = senior consultant 4-hour response; W3–W4 = consultant 1-business-day response.

**Key exclusions:** Payroll processing (PaySpace is SOR); SETA regulatory reporting beyond standard (unless explicitly scoped); 3rd-party ATS migration (Taleo/SuccessFactors content — assessment only); Regression testing of new Oracle quarterly patch (post-EVO).

**Governance notes:**
- Payroll Interface: parallel run INCLUDED by default (HCM-CUT-005). If client waives: must be in writing.
- If Compensation in scope: confirm Mining sector before committing W3S1-005 (G-001).

---

## Pattern 2 — Oracle HCM Full Suite (Phased Go-Live)

**Applies to:** HCM suite delivered in 2 or more release waves. Typically: Wave 1 = Core HR + Absence + Journeys; Wave 2 = Recruiting + Learning + Talent + Compensation.

| Phase | Typical Duration | Notes |
|---|---|---|
| MOB | 2 weeks | Combined mobilise for all waves |
| SDD | 8–10 weeks | Design all waves concurrently; sequence by go-live priority |
| PRO Wave 1 | 10–14 weeks | Build and CRP Wave 1 modules |
| VAL + DEP Wave 1 | 6–8 weeks | UAT, data migration, Wave 1 go-live |
| PRO Wave 2 | 8–12 weeks | Build and CRP Wave 2 modules |
| VAL + DEP Wave 2 | 6–8 weeks | UAT, data migration, Wave 2 go-live |
| EVO | 4 weeks | Post-Wave 2 hypercare |

**Typical total duration:** 44–58 weeks

**Key deviation from Pattern 1:** Resource model may include second SDD specialist team working in parallel. Integration consultants active across both waves. Dual data migration cycles.

**Hypercare:** Apply Pattern 1 hypercare at each go-live event.

---

## Pattern 3 — Oracle HCM Core + Payroll Interface

**Applies to:** Core HR (Global HR, Absence, Journeys) + OIC ↔ PaySpace integration as primary scope.

| Phase | Duration | Notes |
|---|---|---|
| MOB | 1–2 weeks | Confirm PaySpace API access; confirm parallel run scope |
| SDD | 5–7 weeks | HCM design workbooks + OIC integration specification |
| PRO | 10–14 weeks | HCM config + OIC integration build; integration unit tests |
| VAL | 5–7 weeks | SIT + integration testing + UAT; parallel run initiation |
| DEP | 3–4 weeks | Parallel run completion (minimum 1 pay period); cutover |
| EVO | 4 weeks | Hypercare |

**Typical total duration:** 24–38 weeks

**Parallel run rule:** Parallel run for payroll interface is INCLUDED by default (HCM-CUT-005). Minimum = 1 payroll cycle. Client waiver requires written acceptance of risk.

**OIC restrictions:** Section 13.2 of W3S1-009 NEVER in external submissions (PT-W9-008). HIST-018 billing amounts NEVER in proposals.

---

## Pattern 4 — Oracle Recruiting Cloud (Standalone)

**Applies to:** Recruiting Cloud implementation with no other HCM modules in scope.

| Phase | Duration | Notes |
|---|---|---|
| MOB | 1 week | |
| SDD | 4–6 weeks | Recruiting process workbooks; career site design; offer management flow |
| PRO | 8–12 weeks | Config, CRP, career site build; ATS data migration assessment |
| VAL | 4–6 weeks | UAT (hiring manager + recruiter sign-off); integration test if requisition-to-payroll |
| DEP | 2 weeks | Cutover (requisitions, templates, approval chains) |
| EVO | 3 weeks | Hypercare |

**Typical total duration:** 19–29 weeks

**Restrictions:** DFA Taleo references = internal only (Rule 21.4). Redpath Recruiting = Rule 21.5. HCM Recruiting assumption pack is Draft (7 BU decisions pending) — use HCM Base coverage as interim.

---

## Pattern 5 — Oracle Learning Cloud (Standalone)

| Phase | Duration | Notes |
|---|---|---|
| MOB | 1 week | Confirm content strategy; SETA reporting scope |
| SDD | 4–6 weeks | Catalogue design; enrolment flows; content loading approach |
| PRO | 8–10 weeks | Config, CRP, bulk content upload |
| VAL | 4–5 weeks | UAT; SETA report validation |
| DEP | 2 weeks | Cutover (learner records, historic completion data) |
| EVO | 3 weeks | Hypercare |

**Typical total duration:** 18–26 weeks

**Reference restriction:** Mr Price Group (REF-ORA-006) = Learning Cloud scope only (C-W3-002).

---

## Pattern 6 — Oracle OIC Integration (Standalone)

**Applies to:** OIC integration track delivered independently of an HCM or ERP implementation.

| Phase | Duration | Notes |
|---|---|---|
| MOB | 1 week | Confirm source/target APIs; confirm OIC tier (Standard/Enterprise) |
| SDD | 3–4 weeks | Integration specification per flow; error handling design |
| PRO | 6–10 weeks | Build and unit test; adapter configuration |
| VAL | 3–4 weeks | End-to-end integration testing; performance testing |
| DEP | 1–2 weeks | Production cut-over; monitoring setup |
| EVO | 2 weeks | Hypercare |

**Typical total duration:** 16–23 weeks

**Restrictions:** HIST-018 billing NEVER external. Per-integration pricing is T&M unless fixed scope agreed. OIC Foundation model = capped; Enterprise = uncapped (per OIC_ASSUMPTIONS_V1.md).

---

## Pattern 7 — Oracle Fusion ERP (Multi-Module: Financials + Procurement)

| Phase | Duration | Notes |
|---|---|---|
| MOB | 2 weeks | Chart of accounts workshop; LE structure confirmation |
| SDD | 6–8 weeks | Financial design workbooks; procurement catalogue; bank integration spec |
| PRO | 12–16 weeks | GL, AP, AR, CM, FA, Procurement config; CRP cycles; OIC bank integration build |
| VAL | 6–8 weeks | SIT; UAT; data migration mock 1; financial reconciliation |
| DEP | 4 weeks | Data migration mock 2 + final; financial year-end go-live preferred; cutover |
| EVO | 4 weeks | Hypercare; month-end close support |

**Typical total duration:** 34–42 weeks

**Key ERP notes:**
- Opening balance migration only (standard); full transaction history = CR (ERP-DAT-006).
- 2 migration mocks + final standard (third mock = CR).
- Financial year-end go-live strongly preferred — flag if not available.

---

## Pattern 8 — Oracle Fusion ERP (Single Module)

**Applies to:** One ERP module (e.g., Financials only, or Procurement only) where other modules are already live or not in scope.

| Phase | Duration | Notes |
|---|---|---|
| MOB | 1 week | |
| SDD | 4–5 weeks | |
| PRO | 8–12 weeks | |
| VAL | 4–6 weeks | Data migration mock 1 |
| DEP | 3 weeks | Mock 2 + final cutover |
| EVO | 3 weeks | |

**Typical total duration:** 21–29 weeks

---

## Pattern 9 — Oracle EBS Implementation

**Applies to:** New Oracle EBS Finance + HRMS implementation or major upgrade.

| Phase | Duration | Notes |
|---|---|---|
| MOB | 2 weeks | |
| SDD | 5–7 weeks | AIM methodology documentation |
| PRO | 12–16 weeks | EBS config; DBA setup; APEX custom development if in scope |
| VAL | 6–8 weeks | Includes CEMLI testing |
| DEP | 4 weeks | Data migration; cutover; DBA production environment |
| EVO | 4 weeks | |

**Typical total duration:** 33–41 weeks

**Notes:** Content assets (W2S1-002, W2S1-003) are 2012–2014 vintage — modernise statistics and examples for critical tenders. Gold Partner claim NEVER included.

---

## Pattern 10 — Oracle DBA / Managed Services (Non-AMS)

**Applies to:** Oracle database administration and infrastructure managed service engagements (not application-level AMS).

| Phase | Duration | Notes |
|---|---|---|
| Onboarding | 3–4 weeks | Environment discovery; access provisioning; run-book setup |
| Stabilisation | 2 weeks | Baseline monitoring; DR test; alert threshold setup |
| BAU | Monthly | Proactive DBA activities per contracted schedule |

**Resource model:** Senior DBA + Junior DBA.

---

## Pattern 11 — Acumatica ERP

| Phase | Duration | Notes |
|---|---|---|
| MOB | 1–2 weeks | |
| SDD | 4–6 weeks | Acumatica workbooks; customisation list |
| PRO | 10–14 weeks | Configuration + screen customisations; integration build (if PaySpace) |
| VAL | 4–6 weeks | UAT; parallel run if payroll (PaySpace) |
| DEP | 2–3 weeks | Data migration; cutover |
| EVO | 3 weeks | Hypercare |

**Typical total duration:** 24–34 weeks

**Notes:** Acumatica Base assumption pack NOT YET CREATED — flag in all proposals until created. No SA payroll within Acumatica — PaySpace integration is standard payroll SOR.

---

## Pattern 12 — BeBanking H2H

**Applies to:** H2H banking platform implementation (Supplier Payments, Payroll Payments, Forex, or combined).

| Phase | Duration | Notes |
|---|---|---|
| MOB | 1 week | Confirm bank and ERP environment access |
| SDD | 2–3 weeks | Banking flow specifications; format requirements per bank |
| PRO | 6–8 weeks | BeBanking configuration; ERP integration; bank format build |
| Bank Testing | 8–14 weeks | Bank-controlled testing schedule (not APPSolve-controlled) |
| DEP | 2 weeks | Production cutover; dual-run period |
| EVO | 2 weeks | |

**Typical total duration:** 21–30 weeks (highly variable due to bank testing timelines)

**Critical note:** Bank testing timelines are bank-controlled and can extend significantly. Proposal must include explicit disclaimer. Payroll H2H requires Oracle EBS or Oracle Fusion as payroll SOR — Acumatica payroll not supported.

---

## Pattern 13 — AMS / Managed Services Onboarding

**Applies to:** New AMS contract onboarding (Oracle or Acumatica application support).

| Phase | Duration | Notes |
|---|---|---|
| Onboarding | 3–4 weeks | System discovery; access provisioning; SLA parameters confirmed; ITSM tool setup; knowledge transfer from implementation team |
| Stabilisation | 2 weeks | P1/P2 incident response test; first release advisory |
| BAU | Monthly retainer or allocated hours | Monthly CR register review; quarterly health check |

**Resource model:** AMS Account Lead + module support consultants (shared pool; best-efforts allocation — no named consultant guarantee).

**SLA standards:** P1=1h response; P2=4h; P3=1 business day; P4=3 business days. Hours 08:00–17:00 SAST (Mon–Fri). Response ≠ resolution.

**CR threshold:** 2 hours. Above 2 hours = formal CR with signed SOW before work begins.

---

*DELIVERY_PATTERN_LIBRARY v1.0 | WP12 — Proposal Assembly Engine | 2026-06-16*
*Companion: PROJECT_PLAN_TEMPLATES.md | PROPOSAL_STRUCTURE_LIBRARY.md | ESTIMATION_INPUT_MODEL.md*
