---
document_id: ESTIMATION-INPUT-MODEL
title: "Estimation Input Model"
version: "1.0"
created: "2026-06-16"
created_by: "WP12 — Proposal Assembly Engine"
status: "Active"
---

# Estimation Input Model

**Purpose:** Structured intake model for gathering all inputs required to support commercial estimation. This document collects scope parameters; it is NOT a pricing model. Completed inputs are handed to the Commercial Director to apply ESTIMATION_GUIDE.md and EFFORT_MULTIPLIERS.md.

**How to use:**
1. Bid Manager completes Sections 1–5 during initial engagement qualification.
2. BU Technical Lead completes Sections 6–9 after SDD scope confirmation.
3. BU Lead reviews Section 10 (risk flags) before submitting to Commercial Director.
4. Commercial Director applies RATE_CARD_FRAMEWORK.md and ESTIMATION_GUIDE.md to produce the pricing model.
5. Return completed model to tender file before commercial section is drafted.

---

## Section 1 — Engagement Metadata

| Field | Response |
|---|---|
| Client name | |
| Client sector (e.g., Financial Services, Mining, Retail, Public Sector) | |
| Tender / RFP reference number | |
| Submission due date | |
| BU responsible (Oracle HCM / Oracle ERP / Acumatica / BeBanking / AMS / Mixed) | |
| Bid Manager | |
| Technical Lead (BU) | |
| Account Manager (if applicable) | |
| Estimated contract start date | |
| Desired go-live date | |

---

## Section 2 — Product and Module Scope

### 2A — Oracle HCM

| Module | In scope? (Y/N) | Notes |
|---|---|---|
| Core HR / Global HR | | |
| Absence Management | | |
| Oracle Journeys / Onboarding | | |
| Oracle AI Skills | | |
| Recruiting Cloud | | |
| Learning Cloud | | |
| Talent Management | | |
| Workforce Compensation | | |
| HR Help Desk | | |
| Payroll Interface (to PaySpace or other) | | |
| OIC Integrations (non-payroll) | | |
| HCM Analytics | | |

### 2B — Oracle ERP

| Module | In scope? | Notes |
|---|---|---|
| General Ledger | | |
| Accounts Payable | | |
| Accounts Receivable | | |
| Cash Management | | |
| Fixed Assets | | |
| Procurement / Purchasing | | |
| Project Portfolio Management | | |
| Oracle EBS (if EBS, not Fusion) | | |

### 2C — Acumatica

| Module | In scope? | Notes |
|---|---|---|
| Financials (GL/AP/AR) | | |
| Distribution | | |
| Inventory | | |
| Manufacturing | | |
| CRM | | |
| Field Services | | |
| PaySpace Integration | | |
| Project Accounting | | |

### 2D — BeBanking

| Service | In scope? | Notes |
|---|---|---|
| Supplier Payments (H2H) | | |
| Payroll Payments (H2H) | | |
| Forex | | |
| ERP Integration | | |
| Security / Compliance module | | |

### 2E — Post-Implementation Support

| Item | In scope? | Notes |
|---|---|---|
| AMS / Managed Services | | |
| DBA Managed Services (Oracle) | | |

---

## Section 3 — Scale Inputs

| Parameter | Value | Notes |
|---|---|---|
| Total active employees | | Full headcount in scope |
| Employees in payroll (if payroll interface) | | May differ from total |
| Number of legal entities | | Each LE = separate config scope unit |
| Number of countries | | Each country may add localisation effort |
| Number of languages required | | Beyond English |
| Number of payroll cycles per month | | Weekly / bi-weekly / monthly |
| Number of currencies | | Beyond ZAR |
| Number of bank accounts (BeBanking scope) | | Per entity and bank combination |
| Number of named banks (BeBanking) | | Each bank = separate bank testing schedule |
| Client active users (ERP or HCM system users) | | Affects security role build scope |

---

## Section 4 — Integration Scope

| Parameter | Value | Notes |
|---|---|---|
| Total number of integrations | | Count each direction as 1 |
| OIC Foundation integrations | | Standard message volume; capped |
| OIC Enterprise integrations | | High volume or complex transformation |
| ERP bank integrations | | ISO 20022 / SWIFT / local format |
| Payroll integrations (HCM ↔ PaySpace) | | Standard via OIC |
| 3rd-party system integrations | | HR portal, time, benefit providers, etc. |
| SFTP / file-based integrations | | Older format — higher manual effort |
| Complexity per integration (Low / Medium / High) | | Use OIC_ASSUMPTIONS_V1.md definitions |
| Parallel run required (payroll interface) | | Default = YES unless client waives in writing |

---

## Section 5 — Data Migration Scope

| Parameter | Value | Notes |
|---|---|---|
| Primary migration objects (e.g., employees, positions, GL chart of accounts) | | List each |
| Historical data years required | | Beyond opening balance = CR for ERP |
| Source system(s) | | From which system(s) is data being extracted |
| Data quality rating (Good / Fair / Poor) | | Client self-assessment |
| Number of data migration mock runs required | | Standard = 2 mocks + final |
| Legacy attachments / documents to migrate | | Often excluded by default |
| Data cleansing responsibility | | Client / APPSolve / Shared |

---

## Section 6 — Configuration Scope

| Parameter | Value | Notes |
|---|---|---|
| Number of HCM workflows to configure | | Approval chains |
| Number of absence plans | | Each plan = configuration unit |
| Number of compensation plans (Compensation module) | | Verify Mining sector before scoping |
| Number of positions / jobs to load | | |
| Number of custom reports | | Beyond standard Oracle/Acumatica reports |
| Number of BI Publisher reports | | Oracle ERP |
| Number of OTBI analyses | | Oracle HCM |
| Number of custom extensions (OTBI, Groovy, Acumatica customisations) | | Complexity risk |
| Number of security roles to design | | |
| Number of journal approval rules (ERP) | | |
| Number of subledger accounting rules (ERP) | | |

---

## Section 7 — Environment Model

| Parameter | Y/N | Notes |
|---|---|---|
| Development (DEV) environment provided by Oracle/Acumatica | | Standard assumption |
| Test (TEST / Stage) environment | | Required for SIT |
| Production (PROD) environment | | Go-live environment |
| Additional environment required (e.g., training, DR) | | Separate cost line if applicable |
| Environments fully provisioned at kick-off | | If not, add MOB scope |

---

## Section 8 — Timeline and Delivery Model

| Parameter | Value | Notes |
|---|---|---|
| Proposed go-live date | | Anchor for project plan |
| Financial year-end (ERP) | | Preferred go-live alignment |
| Timeline compression from standard | | None / Minor (< 10%) / Significant (> 10%) |
| Blackout periods (client freeze, payroll, board, etc.) | | Dates where no go-live or major testing |
| Remote vs. on-site delivery ratio | | E.g., 80% remote / 20% on-site |
| On-site city / location | | Travel cost implication |
| Training delivery model (classroom / self-service / blended) | | |
| Training scope (train-the-trainer / end-user / both) | | |

---

## Section 9 — Post-Implementation Support (AMS)

| Parameter | Value | Notes |
|---|---|---|
| AMS required (Y/N) | | |
| AMS model (Retainer / Allocated Hours / Per-Incident) | | |
| SLA tier (Standard: P1=1h P2=4h P3=1d P4=3d) | | Default — note if client requires non-standard |
| Extended hours required (beyond 08:00–17:00 SAST) | | Non-standard — cost impact |
| 24x7 monitoring required | | Excluded by default; cost impact |
| Modules in AMS scope | | List |
| AMS start date (if different from go-live + hypercare) | | |

---

## Section 10 — Client Readiness and Risk Flags

Complete before handing to Commercial Director. Each risk factor may trigger an effort multiplier per EFFORT_MULTIPLIERS.md.

| Risk Factor | Rating (Low / Medium / High) | Notes |
|---|---|---|
| Executive sponsor commitment | | Low = weak sponsorship; increases PM effort |
| Business process documentation maturity | | Low = SDD effort multiplied |
| Prior ERP/HCM experience (client team) | | Low = more training and change management |
| Data quality / data governance readiness | | Low = data migration risk |
| IT infrastructure readiness | | Cloud-first vs. hybrid |
| Competing priorities during implementation period | | |
| Number of stakeholder groups requiring consultation | | Each group = workshop unit |
| Union / ER considerations (HCM) | | |
| Regulatory complexity (e.g., multi-country, POPIA, BCEA) | | |
| Payroll parallel run scope | | Default = 1 cycle; additional cycles = effort increase |
| Custom development risk | | High custom = high risk; should trigger T&M consideration |
| Geography and time-zone complexity | | Africa-wide or international |

---

## Section 11 — Commercial Flags

| Flag | Response |
|---|---|
| Proposed commercial model (Fixed Price / T&M / Hybrid) | |
| Fixed-price acceptance criteria defined? | Y/N |
| Change request process agreed with client? | Y/N |
| Milestone-based payment schedule or monthly billing? | |
| Retainer model for AMS (Y/N)? | |
| Currency of pricing (ZAR / USD / EUR / mixed) | |
| Any competitor pricing known? | |
| Client budget indication available? | Y/N (do NOT record amount here — confidential commercial field) |

---

## Output — Hand-Off Checklist to Commercial Director

Before handing this model to the Commercial Director, confirm:

- [ ] All Sections 1–10 completed
- [ ] Scope confirmed by BU Technical Lead
- [ ] Risk flags reviewed by BU Lead
- [ ] Module list matches BOM selection (TENDER_BOM_LIBRARY.md)
- [ ] Assumption packs selected (HCM Base confirmed; OIC confirmed if OIC; ERP confirmed if ERP; AMS confirmed if AMS)
- [ ] Timeline constraints captured (Section 8)
- [ ] Commercial model preference captured (Section 11)

Commercial Director applies:
- `08_Commercial/ESTIMATION_GUIDE.md` (phase effort bands)
- `08_Commercial/EFFORT_MULTIPLIERS.md` (risk-adjusted multipliers)
- `08_Commercial/RATE_CARD_FRAMEWORK.md` (confidential — role rates)
- `08_Commercial/CR_PRICING_MODEL.md` (change request rates)

---

*ESTIMATION_INPUT_MODEL v1.0 | WP12 — Proposal Assembly Engine | 2026-06-16*
*Companion: DELIVERY_PATTERN_LIBRARY.md | ASSEMBLY_RULES_ENGINE.md | TENDER_BOM_LIBRARY.md*
