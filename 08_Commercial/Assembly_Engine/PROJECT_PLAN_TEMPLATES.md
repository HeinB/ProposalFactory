---
document_id: PROJECT-PLAN-TEMPLATES
title: "Project Plan Templates"
version: "1.0"
created: "2026-06-16"
created_by: "WP12 — Proposal Assembly Engine"
status: "Active"
---

# Project Plan Templates

**Purpose:** Week-based project plan templates for insertion into proposals. Select the template matching the product type, then substitute actual calendar dates for week offsets when preparing final submission.

**How to use:**
1. Select the template matching the delivery type.
2. Insert into the proposal project plan section.
3. Add go-live week (anchor point) — work backwards to set Week 1.
4. Convert week offsets to calendar dates only in the final submission document.
5. Add client-specific milestones as rows in grey shading (clearly marked as TBC).

**Phase codes:** MOB (Mobilize) | SDD (Scope & Design) | PRO (Prototype) | VAL (Validate) | DEP (Deploy) | EVO (Evolve) | PM (cross-phase)

---

## Template 1 — Oracle HCM Full Suite

**Use for:** Delivery Pattern 1 (single go-live) or Pattern 2 (phased go-live — adapt per wave). Maps to BOM 1.

| Phase | Week(s) | Key Activities | Key Deliverables | Gate / Decision |
|---|---|---|---|---|
| MOB | W1 | Project charter; team introductions; environment access; RAID log setup | Project Charter; RAID Log; Communication Plan | Kick-off sign-off by both PMs |
| MOB | W2 | Environment confirmation; security provisioning; sprint cadence set | Environment Readiness Confirmation | Access gates confirmed |
| SDD | W3–W4 | Business Process Discovery workshops (HCM Core, Absence, Journeys) | BPD Workbooks (Core, Absence, Journeys) | |
| SDD | W5–W6 | Business Process Discovery workshops (Recruiting, Learning) | BPD Workbooks (Recruiting, Learning) | |
| SDD | W7–W8 | Business Process Discovery workshops (Talent, Compensation, Payroll Interface) | BPD Workbooks (Talent, Compensation, OIC) | |
| SDD | W9–W10 | SDD document; gap analysis; integration specifications; LE config plan | SDD; Gap Register; BR100 | **SDD Sign-off Gate** — client must approve SDD before PRO begins |
| PRO | W11–W14 | HCM Core + Absence + Journeys configuration; CRP 1 | CRP 1 Defect Register | |
| PRO | W15–W18 | Recruiting + Learning configuration; CRP 1 | CRP 1 Defect Register (continued) | |
| PRO | W19–W22 | Talent + Compensation + AI Skills configuration; OIC integration build | OIC Unit Test Results | |
| PRO | W23–W24 | CRP 2 (all modules); custom report prototypes; data migration template prep | CRP 2 Defect Register | **CRP 2 Sign-off Gate** |
| PRO | W25–W26 | Defect fixes; report finalisation; integration regression | Finalised Configuration | |
| VAL | W27–W28 | SIT Round 1 (APPSolve-led; all modules + integrations) | SIT R1 Defect Register | |
| VAL | W29–W30 | SIT Round 1 defect fixes; Data Migration Mock Run 1 | Mock Run 1 Reconciliation Report | |
| VAL | W31–W32 | UAT preparation; UAT Round 1 (client-led) | UAT R1 Sign-off Sheet | |
| VAL | W33–W34 | UAT defect resolution; Parallel Run initiation (if Payroll Interface) | UAT Sign-off; Parallel Run Checklist | **UAT Sign-off Gate** |
| DEP | W35 | Data Migration Mock Run 2; cutover rehearsal | Mock Run 2 Reconciliation | |
| DEP | W36 | Production readiness review; go/no-go decision | Go/No-Go Checklist | **Go/No-Go Gate** |
| DEP | W37 | Final data migration + cutover (go-live week) | Go-Live Confirmation | **GO-LIVE** |
| DEP | W38 | Hypercare Week 1 (named lead on-call) | Incident Log | |
| EVO | W39 | Hypercare Week 2 (senior consultant; 4-hour response) | Stabilisation Report | |
| EVO | W40 | Hypercare Week 3 (1-business-day response) | | |
| EVO | W41 | Hypercare Week 4 + month-end close support | Hypercare Closure Report | **Project Closure Gate** |
| EVO | W42 | Project retrospective; lessons learned; AMS handover (if in scope) | Lessons Learned; AMS Handover Pack | |
| PM | All | Weekly status report; steering committee (biweekly); change control; RAID updates | Status Reports; Steering Committee Packs | |

**Total: 42 weeks (~10 months)**

---

## Template 2 — Oracle HCM Base (Core HR)

**Use for:** Core HR + Absence Management + Journeys only. Maps to BOM 2, Delivery Pattern 3 (with OIC) or Pattern 1 base scope.

| Phase | Week(s) | Key Activities | Key Deliverables | Gate |
|---|---|---|---|---|
| MOB | W1–W2 | Kick-off; environment access; RAID | Project Charter; RAID Log | Kick-off sign-off |
| SDD | W3–W5 | BPD workshops: HCM Core, Absence, Journeys | BPD Workbooks | |
| SDD | W6–W8 | SDD document; gap analysis; config plan; OIC spec (if applicable) | SDD; BR100; Integration Spec | **SDD Sign-off Gate** |
| PRO | W9–W12 | HCM Core + Absence configuration; CRP 1 | CRP 1 Defect Register | |
| PRO | W13–W16 | Journeys configuration; OIC build (if applicable); custom reports | OIC Unit Tests; Report Prototypes | |
| PRO | W17–W18 | CRP 2; defect fixes | CRP 2 Sign-off | **CRP 2 Gate** |
| VAL | W19–W20 | SIT Round 1; integration testing | SIT Defect Register | |
| VAL | W21–W22 | UAT Round 1 (client-led); data migration template | UAT Sign-off | **UAT Gate** |
| VAL | W23–W24 | Parallel run (payroll) — if OIC in scope; data migration Mock 1 | Mock Run 1 Reconciliation | |
| DEP | W25 | Data migration Mock 2; cutover rehearsal | Mock 2 Reconciliation | |
| DEP | W26 | Go/No-Go; final data migration + cutover | Go-Live Confirmation | **GO-LIVE** |
| DEP | W27 | Hypercare W1 (named lead on-call) | Incident Log | |
| EVO | W28–W30 | Hypercare W2–W4; month-end support; retrospective | Hypercare Closure Report | **Project Closure** |
| PM | All | Weekly status; steering committee | Status Reports | |

**Total: 30 weeks (~7 months)**

---

## Template 3 — Oracle Fusion ERP (Financials + Procurement)

**Use for:** Fusion Financials with or without Procurement and PPM. Maps to BOM 10/11/12, Delivery Patterns 7 and 8.

| Phase | Week(s) | Key Activities | Key Deliverables | Gate |
|---|---|---|---|---|
| MOB | W1–W2 | Kick-off; environment; COA workshop; LE structure confirmation | Project Charter; COA Design | Kick-off sign-off |
| SDD | W3–W5 | BPD: GL, AP, AR, CM, FA | Financial BPD Workbooks | |
| SDD | W6–W8 | BPD: Procurement, PPM; bank integration spec; data migration assessment | Procurement/PPM BPD; Integration Spec | |
| SDD | W9–W10 | SDD; gap register; integration specifications; opening balance migration plan | SDD; BR100; Migration Plan | **SDD Sign-off Gate** |
| PRO | W11–W14 | GL + AP + AR configuration; CRP 1 | CRP 1 Defect Register | |
| PRO | W15–W18 | CM + FA + Procurement configuration; bank OIC build | OIC Unit Tests | |
| PRO | W19–W22 | PPM configuration (if applicable); supplier integration; CRP 2 | CRP 2 Defect Register | |
| PRO | W23–W26 | Custom report build; data migration template; defect fixes | Report Prototypes; Migration Templates | **CRP 2 Gate** |
| VAL | W27–W29 | SIT Round 1 (Finance + Procurement + integrations) | SIT Defect Register | |
| VAL | W30 | Data Migration Mock Run 1; SIT defect fixes | Mock 1 Reconciliation | |
| VAL | W31–W33 | UAT Round 1 (client finance team); financial reconciliation | UAT Sign-off | |
| VAL | W34 | UAT defect fixes; parallel bank run (if applicable) | Final UAT Confirmation | **UAT Gate** |
| DEP | W35 | Data Migration Mock Run 2 | Mock 2 Reconciliation | |
| DEP | W36 | Production readiness; go/no-go | Go/No-Go Checklist | **Go/No-Go Gate** |
| DEP | W37 | Final data migration + cutover; financial year-end alignment | Go-Live Confirmation | **GO-LIVE** |
| DEP | W38 | Hypercare W1; month-end close support | Incident Log | |
| EVO | W39–W42 | Hypercare W2–W4; second month-end support; retrospective; AMS handover | Closure Report | **Project Closure** |
| PM | All | Status reports; steering committee | | |

**Total: 42 weeks (~10 months)**

*Note: For single-module ERP (Pattern 8), compress SDD to W3–W7, PRO to W8–W18, VAL to W19–W24, DEP to W25–W27, EVO to W28–W30. Total: 30 weeks.*

---

## Template 4 — Oracle OIC Integration Track

**Use for:** OIC integration delivery independent of core implementation. Maps to BOM 9, Delivery Pattern 6.

| Phase | Week(s) | Key Activities | Key Deliverables | Gate |
|---|---|---|---|---|
| MOB | W1 | Kick-off; confirm source/target APIs; OIC tier confirmed; access | Project Charter; API Inventory | Kick-off sign-off |
| SDD | W2–W4 | Integration specification per flow; error handling design; field mapping | Integration Specification; Field Mapping | **Spec Sign-off Gate** |
| SDD | W5 | Security design; OCI environment confirmation | Security Design | |
| PRO | W6–W8 | Integration adapter build; unit tests per integration | Unit Test Results | |
| PRO | W9–W12 | Full integration build; end-to-end tests; error retry testing | E2E Test Results | **Build Complete Gate** |
| VAL | W13–W14 | Performance and volume testing; exception scenario testing | Performance Report | |
| VAL | W15–W16 | UAT (client-led); integration validation | UAT Sign-off | **UAT Gate** |
| DEP | W17 | Production configuration; cutover | Go-Live Confirmation | **GO-LIVE** |
| DEP | W18 | Hypercare W1; monitoring validation | Incident Log | |
| EVO | W19–W20 | Hypercare W2–W3; handover to BAU or AMS | Closure Report | **Project Closure** |
| PM | All | Status reports | | |

**Total: 20 weeks (~5 months)**

---

## Template 5 — Acumatica ERP

**Use for:** Acumatica ERP implementation (any module combination). Maps to BOM 14, Delivery Pattern 11.

| Phase | Week(s) | Key Activities | Key Deliverables | Gate |
|---|---|---|---|---|
| MOB | W1–W2 | Kick-off; Acumatica tenant provisioning; RAID; team onboarding | Project Charter; RAID Log | Kick-off sign-off |
| SDD | W3–W5 | BPD workshops (Financials, Distribution, Manufacturing per scope) | BPD Workbooks | |
| SDD | W6–W8 | Customisation requirements; PaySpace integration spec (if applicable); SDD | SDD; Customisation List | **SDD Sign-off Gate** |
| PRO | W9–W12 | Core module configuration; CRP 1 | CRP 1 Defect Register | |
| PRO | W13–W18 | Distribution/Manufacturing build; PaySpace integration; customisations; CRP 2 | CRP 2 Defect Register; OIC Unit Tests | **CRP 2 Gate** |
| VAL | W19–W21 | SIT Round 1; integration testing | SIT Defect Register | |
| VAL | W22–W24 | UAT (client-led); data migration mock 1; parallel run (if payroll) | UAT Sign-off | **UAT Gate** |
| DEP | W25–W26 | Data migration mock 2 + final; cutover; go-live | Go-Live Confirmation | **GO-LIVE** |
| DEP | W27 | Hypercare W1 | Incident Log | |
| EVO | W28–W30 | Hypercare W2–W4; retrospective; AMS handover (if in scope) | Closure Report | **Project Closure** |
| PM | All | Status reports; steering committee | | |

**Total: 30 weeks (~7 months)**

---

## Template 6 — BeBanking H2H

**Use for:** BeBanking implementation (any combination of payment services). Maps to BOM 15, Delivery Pattern 12.

| Phase | Week(s) | Key Activities | Key Deliverables | Gate |
|---|---|---|---|---|
| MOB | W1 | Kick-off; bank contacts established; ERP and banking environment access | Project Charter; Bank Contact Sheet | Kick-off sign-off |
| SDD | W2–W3 | Banking flow specifications; ERP integration spec; bank format requirements | Integration Spec; Bank Format Requirements | **Spec Sign-off Gate** |
| SDD | W4 | Security and hosting design; BeBanking configuration plan | Security Design | |
| PRO | W5–W8 | BeBanking platform configuration; ERP integration build; format build | Build Completion Report | |
| PRO | W9–W12 | APPSolve integration testing; ERP end-to-end test; format validation | Unit + E2E Test Results | **Build Complete Gate** |
| Bank Testing | W13–W24 | Bank-controlled testing (UAT at bank) — TIMELINE NOT CONTROLLED BY APPSOLVE | Bank UAT Sign-off | **Bank Sign-off Gate** (bank-dependent) |
| DEP | W25 | Production configuration; dual-run period initiation | Production Confirmation | |
| DEP | W26 | Cutover; go-live | Go-Live Confirmation | **GO-LIVE** |
| EVO | W27–W28 | Hypercare; first live transaction monitoring | Closure Report | **Project Closure** |
| PM | All | Status reports | | |

**Total: 28 weeks (~7 months) — Bank testing phase highly variable**

**Proposal disclaimer required:** "Bank testing timelines are controlled by the client's banking partner and are outside APPSolve's delivery control. Total project duration will be confirmed once bank testing schedule is agreed."

---

## Template 7 — AMS / Managed Services Onboarding

**Use for:** New AMS contract onboarding (Oracle or Acumatica). Maps to BOM 16, Delivery Pattern 13.

| Phase | Week(s) | Key Activities | Key Deliverables | Gate |
|---|---|---|---|---|
| Onboarding | W1 | Contract countersigned; AMS Lead assigned; introduction call | Signed AMS Agreement | Contract sign-off |
| Onboarding | W2 | System discovery; access provisioning; ITSM tool setup (ServiceNow or equivalent) | System Inventory; Access Confirmation | |
| Onboarding | W3 | Run-book documentation; SLA parameters configured; escalation matrix signed | Run-Book; Escalation Matrix | |
| Onboarding | W4 | Knowledge transfer (from implementation team or prior SI); P1/P2 drill | Knowledge Transfer Report | **Onboarding Complete Gate** |
| Stabilisation | W5 | First release advisory (Oracle); monitoring baseline; alert thresholds set | Oracle Release Advisory; Alert Config | |
| Stabilisation | W6 | First monthly support review; CR register initialised | Monthly Review Report; CR Register | **Stabilisation Complete Gate** |
| BAU | Monthly | Proactive SLA monitoring; CR management; quarterly health check | Monthly Status Report; CR Tracker | Ongoing |
| BAU | Quarterly | Health check; patch advisory (Oracle quarterly); system performance review | Quarterly Health Check Report | |

**Total onboarding: 6 weeks; BAU ongoing thereafter**

**SLA reference (from AMS_ASSUMPTIONS_V1.md):** P1=1h response; P2=4h; P3=1 business day; P4=3 business days. 08:00–17:00 SAST Mon–Fri.

**Exclusions from AMS BAU:** New module implementation; new integration development; new report development; data migration; Oracle upgrade projects (advisory only — not upgrade delivery).

---

*PROJECT_PLAN_TEMPLATES v1.0 | WP12 — Proposal Assembly Engine | 2026-06-16*
*Companion: DELIVERY_PATTERN_LIBRARY.md | PROPOSAL_STRUCTURE_LIBRARY.md | ESTIMATION_INPUT_MODEL.md*
