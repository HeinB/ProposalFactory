---
document_id: ESTIMATION-GUIDE
title: "APPSolve Estimation Guide — Methodology and Complexity Models"
version: "1.0"
created: "2026-06-15"
created_by: "WP11F — Tender Commercial Framework"
status: "Approved — 2026-06-16"
approved_by: "Hein Blignaut (BU Lead)"
approval_ref: "WP11F-A"
applies_to: "All Oracle, Acumatica, and BeBanking implementation proposals and SOWs"
companion_docs:
  - "RATE_CARD_FRAMEWORK.md"
  - "EFFORT_MULTIPLIERS.md"
  - "CR_PRICING_MODEL.md"
  - "COMMERCIAL_GOVERNANCE.md"
---

# APPSolve Estimation Guide

## 1. Purpose

This guide defines APPSolve's standard methodology for estimating implementation effort. It provides:
- A bottom-up estimation framework
- Phase-based effort structure aligned to the Oracle OUM / Customer Success Navigator delivery model
- Complexity classification models per module and integration
- Standard task-level effort templates
- Rules for applying contingency and risk allowances

The guide is for internal use by bid managers, functional leads, and project managers. It does not contain actual effort figures — it defines the structure within which effort is derived from delivered client engagements.

---

## 2. Estimation Principles

### 2.1 Bottom-Up Estimation

APPSolve uses bottom-up estimation as the primary method. This means:
1. Decompose the scope into deliverable tasks at the phase and workstream level
2. Estimate each task in person-days using the complexity model and historical baselines
3. Sum task estimates to produce a phase total
4. Apply effort multipliers where applicable (see EFFORT_MULTIPLIERS.md)
5. Add contingency per the contingency model (Section 7)

Top-down estimation (estimating total effort from high-level scope descriptions without task decomposition) may be used for rough-order-of-magnitude estimates only. Top-down estimates must not be used as the basis for a fixed-price SOW.

### 2.2 Unit of Measure

The standard unit is the **person-day** (8 working hours). All estimates, rate cards, and billing schedules use person-days.

For AMS and CR estimation, the unit may be **person-hours** where the effort is less than one full day. The conversion is:
```
1 person-day = 8 person-hours
```

### 2.3 What is Estimated

Estimates include:
- All consultant effort for analysis, design, configuration, testing, training, and cutover
- Project management effort (estimated as a percentage of total project effort)
- Change management effort where in scope

Estimates exclude:
- Travel time (separately quoted where applicable)
- Oracle support subscription costs
- Third-party software licensing
- Client-side effort (configuration of client IT, client user testing, client data preparation)
- Bank testing phase (BeBanking) — bank-controlled UAT is excluded from APPSolve effort estimates; scoped separately or billed on a milestone basis

### 2.4 Estimate Ownership

| Context | Owner | Sign-off required |
|---|---|---|
| Initial proposal estimate | Functional Lead + BU Lead | BU Lead |
| SOW fixed-price estimate | Functional Lead + PM + Commercial Director | Commercial Director |
| Change request estimate | Functional Lead (or Senior Consultant) | PM + client |
| AMS CR estimate (>2 hours) | AMS Consultant + AMS Account Manager | AMS Account Manager + client written approval |

---

## 3. Delivery Phase Model

APPSolve implementations follow the Oracle OUM / Customer Success Navigator phase structure:

| Phase | Code | Purpose | Typical Duration |
|---|---|---|---|
| Mobilize | MOB | Project kick-off; access; environment setup; plan confirmation | 2–4 weeks |
| Scope & Design | SDD | Business requirements; gap analysis; Scope and Design Document | 3–8 weeks (scope-dependent) |
| Prototype | PRO | Configuration build; iteration cycles; demo checkpoints | 6–16 weeks (scope-dependent) |
| Validate | VAL | System Integration Testing; UAT; data validation; training delivery | 4–8 weeks |
| Deploy | DEP | Data migration (mock + final); cutover; hypercare | 2–4 weeks |
| Evolve | EVO | Post-go-live stabilisation; hypercare; knowledge transfer | 2–4 weeks |

**Phase proportions — indicative (varies by engagement):**

| Phase | Typical % of Total Implementation Effort |
|---|---|
| Mobilize | 3–5% |
| Scope & Design | 15–25% |
| Prototype | 40–55% |
| Validate | 15–20% |
| Deploy | 5–10% |
| Evolve | 5–8% |
| Project Management (cross-phase) | 8–15% |

These proportions are starting points. The functional lead adjusts phase proportions based on engagement specifics (e.g., a data-heavy engagement increases Deploy; a complex design engagement increases Scope & Design).

---

## 4. Complexity Classification Model

### 4.1 Four-Tier Complexity Model

APPSolve classifies each module, workstream, and integration against a four-tier complexity model. The tier determines the effort baseline before multipliers are applied.

| Tier | Label | Definition |
|---|---|---|
| C1 | Simple | Standard configuration; minimal customisation; straightforward data model; no cross-module complexity; client has clear requirements |
| C2 | Standard | Moderate configuration; some workflow customisation; standard integrations; minor data migration; typical for a well-scoped implementation |
| C3 | Complex | Multiple legal entities or operating units; advanced workflow; complex integrations; significant data migration; client requirements not fully defined at scope stage |
| C4 | Highly Complex | Multi-entity, multi-country, multi-currency; custom reporting and analytics; multiple complex integrations; large data volumes; tight timeline; limited client clarity |

**C4 governance:** Any module or workstream classified as C4 triggers a mandatory BU Lead review of the estimate before it is submitted to the client. C4 classification on a fixed-price proposal also triggers a RED risk flag per COMMERCIAL_GOVERNANCE.md Section 5.1.

### 4.2 Applying Complexity to a Module

For each Oracle Fusion HCM module, Oracle Fusion ERP module, OIC integration, or Acumatica module in scope:

1. Classify the module against the C1–C4 model using the module-specific complexity indicators below (Section 4.3)
2. Apply the module base effort from the internal effort baseline register (maintained by the BU Lead — not included in this document)
3. Apply any relevant multipliers from EFFORT_MULTIPLIERS.md
4. Record the classification and rationale in the Scope and Design Document

### 4.3 Module-Specific Complexity Indicators

#### Oracle Fusion HCM Modules

| Module | C1 Indicators | C2 Indicators | C3 Indicators | C4 Indicators |
|---|---|---|---|---|
| Core HR | 1 LE; <200 employees; standard absence types; no custom approval workflows | 1–3 LE; 200–1,000 employees; some custom workflows | 3–5 LE; 1,000–5,000 employees; complex org structure; multiple absence types | >5 LE; >5,000 employees; multi-country; complex HR policies |
| Recruiting | 1 career site; <100 vacancies/year; standard offer template | 1–2 career sites; standard JDs; 100–500 vacancies/year | 2–4 career sites; custom journey steps; ATS migration; complex offers | 4+ career sites; Recruiting Booster; complex job board integrations; 500+ vacancies/year |
| Learning | Standard catalogue; <500 employees; no SCORM content | Blended learning; moderate catalogue; SETA reporting | Custom catalogue; content migration; third-party LMS integration | Large content library; multiple SCORM packages; external LMS integration; multiple SETA reports |
| Talent Management | Standard performance template; <500 employees | 1–2 performance templates; basic succession | Multiple performance templates; 9-box grid; succession pools | Complex goal cascades; multiple review cycles; large succession portfolio |
| Workforce Compensation | 1 merit plan; standard approval | 2–3 plans; custom approval | 4+ plans; budget modelling; custom total comp statements | Complex variable pay; equity analysis; integration with benchmarking tool |
| OIC (per integration) | Standard adapter; well-documented API; client has existing test environment | Custom mapping; moderate business logic; SFTP/file-based | Complex transformation; real-time trigger; error reprocessing logic; limited vendor API documentation | Bi-directional; multiple payload types; high transaction volume; limited vendor cooperation |

#### Oracle Fusion ERP Modules

| Module | C1 Indicators | C2 Indicators | C3 Indicators | C4 Indicators |
|---|---|---|---|---|
| GL / Financials | 1 LE; standard COA; 1 currency; 1 ledger | 2–3 LE; custom COA segments; 2 currencies | 4–6 LE; multi-currency; secondary ledgers assessed | >6 LE; multi-country; IFRS vs local GAAP; reporting ledgers |
| AP / Procurement | Standard 3-way match; <100 suppliers | Moderate supplier count; BPA; approval routing | Complex invoice approval; multi-site receiving; high supplier count | Advanced Procurement; SLA; custom invoice matching; EDI integration |
| Fixed Assets | Opening balance migration only; <500 assets | Opening balance; moderate asset count; 500–2,000 assets | Opening balance; large asset count; complex depreciation methods | Large asset count; impairment; revaluation; IFRS 16 assessed separately |
| Cash Management | 1 bank account; simple reconciliation | 2–5 bank accounts; auto-reconciliation | Multiple banks; complex bank statement formats; OIC bank integration | Multiple banks; multi-currency; complex matching rules; BeBanking |
| PPM | 1–5 projects; simple costing | 10–50 projects; project billing | 50–200 projects; cross-charge; PPM to GL integration | >200 projects; complex billing rules; revenue recognition; integration with procurement |

*Oracle HCM module complexity indicators are confirmed based on delivered projects (Hollywood Bets full HCM suite 2023–2025). Oracle ERP module indicators are conditionally approved — ERP BU Lead to validate against NALA/Investec/ARM/CUM delivered engagements in a separate session. Acumatica module indicators require validation with the Acumatica BU Lead before first fixed-price Acumatica proposal.*

#### BeBanking H2H

| Complexity | Indicators |
|---|---|
| C1 | 1 bank; simple payment type; well-documented bank format; bank has completed APPSolve testing before |
| C2 | 1–2 banks; 2 payment types; standard MT940 import; bank testing within normal cycle |
| C3 | 2–3 banks; multiple payment types; custom format mapping required; bank testing uncertain |
| C4 | 3+ banks; multi-currency; complex payment categories; bank testing schedule outside APPSolve's control; new bank (no prior APPSolve integration) |

---

## 5. Standard Task List by Phase

### 5.1 Mobilize Phase — Standard Tasks

| Task | Typical effort |
|---|---|
| Project kick-off meeting (preparation + facilitation) | Per PM rate, 0.5–1 day |
| Project plan preparation | 1–2 days PM |
| Environment access and configuration setup | 0.5–1 day per environment type |
| RAID log initialisation | 0.5 day PM |
| Stakeholder register | 0.5 day PM |
| Communication plan | 0.5 day (PM + CM where in scope) |

### 5.2 Scope & Design Phase — Standard Tasks

| Task | Typical effort |
|---|---|
| Business requirements workshops (per workstream) | 0.5–2 days per workshop (functional lead + BA) |
| Configuration workbook preparation (per module) | Complexity-dependent (see module baseline) |
| Gap analysis documentation | 0.5–1 day per gap |
| Scope and Design Document drafting | 1–3 days per module functional lead |
| Scope and Design Document review and sign-off facilitation | 0.5–1 day PM |
| Integration specification per OIC integration | 0.5–2 days (OIC consultant + functional lead) |

### 5.3 Prototype Phase — Standard Tasks

| Task | Typical effort |
|---|---|
| Configuration — per module (complexity-weighted) | See module baseline |
| Data conversion mapping (per data object) | 0.5–2 days per object (BA + functional lead) |
| Conference room pilot (CRP) preparation + facilitation | 1–2 days per CRP |
| OIC integration development (per integration) | Complexity-weighted |
| Security role design and setup | 0.5–2 days (functional lead) |
| Approval workflow configuration (per workflow) | Complexity-weighted |

### 5.4 Validate Phase — Standard Tasks

| Task | Typical effort |
|---|---|
| SIT test script development (per workstream) | 1–3 days test lead + functional consultant |
| SIT execution | 1–3 days per workstream |
| Defect remediation (budget per risk level) | % of SIT effort (see contingency model) |
| UAT support | 0.5–1 day per workstream per UAT cycle |
| Training material preparation (per module) | 1–3 days functional consultant |
| Training delivery (per session) | 0.5–1 day per session + preparation |

### 5.5 Deploy Phase — Standard Tasks

| Task | Typical effort |
|---|---|
| Mock migration 1 (per data object) | Object-complexity-weighted |
| Mock migration 2 (per data object) | 70–80% of Mock 1 effort (corrections only) |
| Cutover plan preparation | 0.5–1 day PM |
| Cutover execution support | 1–3 days (team-dependent) |
| Go-live day support | 1–2 days |

### 5.6 Evolve Phase — Standard Tasks

| Task | Typical effort |
|---|---|
| Hypercare incident support | Resource-on-call — see hypercare model (Section 6) |
| Hypercare daily status call | 0.5 hour/day × hypercare duration |
| Post-go-live configuration adjustments | Contingency allowance |
| Knowledge transfer to client IT | 0.5–1 day per module |
| Lessons learned documentation | 0.5 day PM |

---

## 6. Hypercare Model

### 6.1 Standard Hypercare Definition

APPSolve's standard hypercare period is **four (4) weeks** post-go-live. The hypercare model is:

| Week | Support intensity | Billable model |
|---|---|---|
| Week 1 (go-live week) | Named functional lead(s) on-call during business hours | Included in implementation fee |
| Week 2 | Senior consultant available, 4-hour response | Included in implementation fee |
| Week 3–4 | Consultant available, 1-business-day response | Included in implementation fee |

Extended hypercare (beyond 4 weeks) transitions to AMS scope and is governed by the AMS assumptions pack (AMS_ASSUMPTIONS_V1.md). Where a client requires a defined extended hypercare period before AMS commencement, this is priced at the implementation daily rate as a Hypercare Extension SOW — no standard pricing uplift is defined; assessed per engagement by the BU Lead.

### 6.2 Hypercare Effort Allocation

Standard hypercare effort per module = [defined in internal effort baselines per complexity tier]. This effort is included in the Evolve phase estimate and is not separately quoted unless the client requires a defined hypercare SLA beyond the standard model.

---

## 7. Contingency Model

### 7.1 Contingency Definition

Contingency is an allowance for known risk areas that cannot be fully estimated at proposal stage. Contingency is not scope creep — it is the bounded risk reserve for the agreed scope.

### 7.2 Standard Contingency Bands

| Risk Level | Contingency % | Applicable When |
|---|---|---|
| Low | 5% of total implementation effort | Well-defined scope; experienced client ERP team; stable business requirements; completed prior implementation |
| Standard | 10–15% of total implementation effort | Typical implementation; some scope ambiguity; normal client readiness |
| Elevated | 15–20% of total implementation effort | Multiple legal entities; first ERP implementation for client; complex integrations; untested third-party interfaces |
| High | 20–30% of total implementation effort | Significant scope complexity; first Oracle Fusion deployment; highly compressed timeline; limited client engagement |

### 7.3 Contingency Governance

- Contingency is held by the Project Manager and can only be consumed by the PM after formal risk event documentation
- Contingency is not visible to the client in a fixed-price proposal — it is included in the total fee
- In T&M engagements, contingency is surfaced as an estimated range ("estimated X to Y days")
- If contingency is not consumed, the remaining amount is retained by APPSolve (not refunded to the client)

---

## 8. Project Management Effort

Project management (PM) effort is estimated as a percentage of total implementation effort:

| Engagement Size | PM % of Total Effort |
|---|---|
| Small (< 50 days total) | 8–10% |
| Medium (50–150 days total) | 10–12% |
| Large (150–400 days total) | 12–15% |
| Enterprise (> 400 days total) | 10–13% (with dedicated PM resource) |

PM effort covers: project planning; RAID management; status reporting; client meeting facilitation; escalation management; milestone tracking; budget tracking; change request coordination.

---

## 9. Estimation Quality Control

Before a fixed-price estimate is submitted to a client:

| Check | Owner |
|---|---|
| Bottom-up task decomposition complete (no lump-sum estimation) | Functional Lead |
| Complexity tiers assigned and recorded per module/integration | Functional Lead |
| Effort multipliers reviewed and applied | Functional Lead + BU Lead |
| PM effort calculated | PM |
| Contingency applied at correct band | Functional Lead + BU Lead |
| Rate card applied to total effort | Bid Manager + Commercial Director |
| Commercial Director sign-off on total fee (per COMMERCIAL_GOVERNANCE.md) | Commercial Director |
| Assumptions in SOW match the estimation assumptions | Functional Lead |

---

## 10. Decision Record

*WP11F-A — Commercial Framework Approval | 2026-06-16 | BU Lead: Hein Blignaut*

| Decision ID | Item | Decision | Applied |
|---|---|---|---|
| BU-EST-001 | Phase proportion percentages | **APPROVED** — MOB 3–5%, SDD 15–25%, PRO 40–55%, VAL 15–20%, DEP 5–10%, EVO 5–8%, PM 8–15% confirmed as consistent with Oracle OUM and delivered project experience | Section 3 confirmed |
| BU-EST-002 | Four-tier C1–C4 complexity model | **APPROVED** — Four-tier model confirmed as sufficient; C4 classification triggers mandatory BU Lead review and RED risk flag on fixed-price proposals | Section 4.1 updated |
| BU-EST-003 | Module-specific complexity indicators | **CONDITIONALLY APPROVED** — Oracle HCM indicators confirmed based on Hollywood Bets delivered evidence; Oracle ERP indicators require ERP BU Lead validation against NALA/Investec/ARM/CUM; Acumatica indicators require Acumatica BU Lead validation before first fixed-price proposal | Section 4.3 noted |
| BU-EST-004 | Hypercare model and extended hypercare | **APPROVED** — 4-week standard hypercare confirmed; extended hypercare transitions to AMS at implementation daily rate as a Hypercare Extension SOW; no standard pricing uplift defined; assessed per engagement | Section 6.1 updated |
| BU-EST-005 | Contingency bands | **APPROVED** — Low 5%, Standard 10–15%, Elevated 15–20%, High 20–30% confirmed as correctly calibrated against project experience | Section 7.2 confirmed |
| BU-EST-006 | Internal effort baseline register | **DECISION** — BU Lead maintains internal effort baseline register (module base effort by complexity tier) as a separate confidential document not stored in KB; Oracle BU Lead to create and maintain | Action: BU Lead — register not in this document |
| BU-EST-007 | BeBanking bank testing exclusion | **APPROVED** — Bank-controlled UAT excluded from APPSolve effort estimates; separately scoped or billed by milestone; bank testing timeline is bank-controlled and not within APPSolve's delivery control | Section 2.3 updated |
| BU-EST-008 | ROM vs bottom-up threshold | **APPROVED** — Top-down ROM estimation permitted for early-stage qualification only; bottom-up estimation required before any fixed-price SOW | Section 2.1 confirmed |

**Commercial Director items outstanding: None from this document**
**Pending BU Lead action: BU-EST-006 — Internal effort baseline register to be created**

---

*ESTIMATION_GUIDE v1.0 | WP11F — Tender Commercial Framework | 2026-06-15 → Approved 2026-06-16 | BU Lead: Hein Blignaut*  
*Internal use only — do not include in external proposal documents*  
*Companion: RATE_CARD_FRAMEWORK.md · EFFORT_MULTIPLIERS.md · CR_PRICING_MODEL.md · COMMERCIAL_GOVERNANCE.md*
