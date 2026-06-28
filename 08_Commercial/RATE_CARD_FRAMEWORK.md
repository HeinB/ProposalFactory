---
document_id: RATE-CARD-FRAMEWORK
title: "APPSolve Rate Card Framework"
version: "1.0"
created: "2026-06-15"
created_by: "WP11F — Tender Commercial Framework"
status: "Approved — 2026-06-16"
approved_by: "Hein Blignaut (BU Lead)"
approval_ref: "WP11F-A"
applies_to: "All Oracle, Acumatica, and BeBanking proposals, SOWs, and AMS agreements"
companion_docs:
  - "ESTIMATION_GUIDE.md"
  - "CR_PRICING_MODEL.md"
  - "EFFORT_MULTIPLIERS.md"
  - "COMMERCIAL_GOVERNANCE.md"
note: "This document defines the rate card structure, role taxonomy, and pricing framework only. Actual rate values are not contained in this document. Rate values are maintained in the Commercial Director's rate schedule and are not to be committed to document form."
---

# APPSolve Rate Card Framework

## 1. Purpose

This framework defines APPSolve's rate card structure: the role taxonomy, rate bands, rate card components, and the rules for selecting and applying the correct rate in proposals, SOWs, and AMS agreements. It does not contain actual rates. Rates are maintained separately by the Commercial Director.

This framework ensures:
- Consistent role definition and pricing logic across all BUs (Oracle, Acumatica, BeBanking)
- Appropriate rate band selection for each engagement context
- Transparent rate card structure that bid managers can apply without needing to rediscover pricing logic per tender

---

## 2. Rate Card Principles

### 2.1 Daily Rate Unit

The APPSolve standard unit of commercial pricing is the **person-day** (8 working hours). All estimates are expressed in person-days. All rate cards are expressed as a rate per person-day.

Where a scope of work is expressed in hours (e.g., AMS service requests), the formula is:

```
Rate per hour = Daily Rate ÷ 8
```

### 2.2 Rate Bands

APPSolve consultants are classified into five rate bands reflecting seniority, certification level, and delivery responsibility:

| Band | Role Level | Typical Responsibilities |
|---|---|---|
| Band 1 | Associate Consultant | Execution under supervision; data loading; test execution; standard report configuration |
| Band 2 | Consultant | Module configuration; workflow setup; standard integration work; UAT coordination |
| Band 3 | Senior Consultant | Full module ownership; solution design; complex configuration; senior stakeholder engagement |
| Band 4 | Principal Consultant / Functional Lead | Cross-module solution architecture; BU lead oversight; complex integration design; presales support |
| Band 5 | Director / Solution Architect | Engagement oversight; commercial decisions; client relationship; complex architecture; tender strategy |

### 2.3 Rate Types

| Rate Type | Definition | When to Apply |
|---|---|---|
| Standard Day Rate | Base rate for the applicable band during standard delivery | All project work unless otherwise specified |
| T&M Daily Rate | Time and materials billing rate | T&M engagements and change requests |
| AMS Hourly Rate | Hourly rate for AMS support services | AMS agreements and CR billing |
| Extended Hours Rate | Rate for support outside standard business hours | AMS extended hours SLA tier |
| Public Holiday Rate | Rate for support on SA public holidays | AMS public holiday support |
| On-Site Rate | Supplement for on-site delivery where applicable | On-site project delivery and AMS on-site support |

### 2.4 Currency

APPSolve standard pricing is in South African Rand (ZAR). Where engagements are priced in other currencies (USD, EUR, GBP, USD for international clients), the Commercial Director specifies the applicable rate in the relevant currency. Rate cards in other currencies are maintained separately.

### 2.5 Rate Escalation

Rate escalation applies on an annual basis. The escalation rate and trigger are defined in the AMS agreement or SOW escalation clause. Where no escalation clause is specified, the standard APPSolve escalation policy applies (as determined by the Commercial Director annually). Rates quoted in a fixed-price SOW are fixed for the contracted engagement period, subject to the SOW escalation clause.

---

## 3. Role Taxonomy

### 3.1 Oracle Fusion HCM Roles

| Role Code | Role Name | Band | Key Skills |
|---|---|---|---|
| ORA-HCM-ARCH | Oracle HCM Solution Architect | 4–5 | Full HCM suite architecture; integration design; presales |
| ORA-HCM-LEAD | Oracle HCM Functional Lead | 4 | Module ownership across multiple HCM modules; BU oversight |
| ORA-HCM-SR | Oracle HCM Senior Consultant | 3 | Core HR, Recruiting, Learning, Talent, Compensation (specialist) |
| ORA-HCM-CON | Oracle HCM Consultant | 2 | Standard module configuration; workflow; OTBI; security |
| ORA-HCM-JR | Oracle HCM Associate Consultant | 1 | Data loading (HDL); test execution; report configuration |
| ORA-OIC-SR | OIC Senior Integration Consultant | 3–4 | Complex integration architecture; BeBanking; API design |
| ORA-OIC-CON | OIC Integration Consultant | 2–3 | Standard integration development; error investigation |
| ORA-DBA-SR | Senior Oracle DBA | 3–4 | Oracle Cloud DBA; OCI; performance tuning; patching |
| ORA-DBA-CON | Oracle DBA Consultant | 2–3 | Standard DBA tasks; backup/recovery; monitoring |

### 3.2 Oracle Fusion ERP Roles

| Role Code | Role Name | Band | Key Skills |
|---|---|---|---|
| ORA-ERP-ARCH | Oracle ERP Solution Architect | 4–5 | ERP + OIC solution design; multi-entity; presales |
| ORA-ERP-LEAD | Oracle ERP Functional Lead | 4 | Financials + Procurement + PPM cross-module ownership |
| ORA-ERP-FIN | Oracle ERP Finance Consultant (Senior) | 3 | GL; AP; AR; FA; Cash Management; multi-ledger |
| ORA-ERP-PROC | Oracle ERP Procurement Consultant (Senior) | 3 | Purchasing; Receiving; Supplier Management; BPA |
| ORA-ERP-PPM | Oracle ERP PPM Consultant (Senior) | 3 | Project Financial Management; Project Costing; Billing |
| ORA-ERP-CON | Oracle ERP Consultant | 2 | Standard module configuration; OTBI; security; UAT |
| ORA-ERP-JR | Oracle ERP Associate Consultant | 1 | FBDI data loading; test execution; COA setup |

### 3.3 Acumatica Roles

| Role Code | Role Name | Band | Key Skills |
|---|---|---|---|
| ACU-ARCH | Acumatica Solution Architect | 4–5 | Full-suite architecture; customisation design; presales |
| ACU-LEAD | Acumatica Functional Lead | 4 | Cross-module delivery ownership |
| ACU-SR | Acumatica Senior Consultant | 3 | ERP Financials; Distribution; Field Services; Payroll integration |
| ACU-CON | Acumatica Consultant | 2 | Standard configuration; reporting; approval maps; workflow |
| ACU-DEV | Acumatica Developer | 3 | Customisation; SDK; Acumatica low-code extensions |
| ACU-JR | Acumatica Associate Consultant | 1 | Data migration; test execution; basic configuration |

### 3.4 BeBanking Roles

| Role Code | Role Name | Band | Key Skills |
|---|---|---|---|
| BB-LEAD | BeBanking OIC Lead Consultant | 3–4 | BeBanking H2H architecture; bank testing; OIC design |
| BB-CON | BeBanking OIC Consultant | 2–3 | BeBanking integration development; bank format mapping |

### 3.5 Cross-BU Roles

| Role Code | Role Name | Band | Key Skills |
|---|---|---|---|
| XBU-PM | Project Manager | 3–4 | Oracle OUM; delivery governance; risk; client management |
| XBU-BA | Business Analyst | 2–3 | Requirements; process documentation; gap analysis; UAT |
| XBU-TST | Test Lead | 3 | Test strategy; test script design; UAT coordination |
| XBU-CM | Change Management Consultant | 3 | Training planning; stakeholder engagement; communication |
| XBU-ARCH | Enterprise Architect | 4–5 | Cross-BU architecture; technology strategy |
| XBU-AMS | AMS Account Manager | 3–4 | AMS portfolio management; CR pipeline oversight; client relationship; monthly service reporting |
| XBU-AMS-CON | AMS Support Consultant | 2–3 | First-line application support; incident triage; service request fulfilment; CR effort estimation |

---

## 4. Rate Card Components

### 4.1 Implementation Rate Card

The implementation rate card applies to all project-based engagements (Mobilize through Evolve). The rate card maps:

```
Role × Band → Daily Rate
```

For each proposal, the bid manager selects:
1. The delivery roles required for the engagement
2. The band applicable to each assigned resource
3. The total days per role (from ESTIMATION_GUIDE.md)
4. Whether effort multipliers apply (from EFFORT_MULTIPLIERS.md)

The total fee is:
```
∑ (Days per Role × Daily Rate per Role × Applicable Multiplier)
```

### 4.2 AMS Rate Card

The AMS rate card applies to all AMS agreements. It has two components:

**Scope of AMS rate types:** Extended Hours rate applies during project cutover week and hypercare on-call periods in addition to AMS extended hours. Public Holiday rate applies for confirmed on-site cutover delivery on SA public holidays. Neither rate applies to standard remote-first project delivery phases.

**Monthly retainer component (where applicable):**
```
Monthly Retainer = agreed scope × retainer rate
```

**Allocated-hours component (where applicable):**
```
Monthly hours fee = contracted hours × AMS Hourly Rate (per applicable band)
```

**Overage component:**
```
Overage = (hours consumed − monthly allocation) × overage AMS hourly rate
```

**CR component:**
```
CR fee = CR effort days × T&M daily rate OR CR effort hours × AMS hourly rate
```
(Selection of daily or hourly rate depends on CR duration; daily rate for multi-day CRs; hourly rate for sub-day CRs)

### 4.3 Rate Card Uplift for Complexity

The base rate is the Band 1–5 daily rate. Complexity uplifts are not applied to the rate itself — they are applied to the effort estimate (see EFFORT_MULTIPLIERS.md). This keeps rate cards clean and auditable: rate = rate, effort = effort.

---

## 5. Rate Card Selection Rules

### 5.1 Which Rate Card to Apply

| Engagement Type | Rate Card | Notes |
|---|---|---|
| Fixed-price implementation | Implementation rate card (internal use only) | Rates not disclosed to client; total fee only in proposal |
| Time and materials (T&M) | T&M daily rate card | Rates may be disclosed in SOW rate schedule |
| AMS retainer | AMS rate card (retainer tier) | Monthly retainer fee disclosed in AMS SOW |
| AMS allocated hours | AMS rate card (hourly tier) | Hourly rate disclosed in AMS SOW hourly schedule |
| Change requests (in AMS) | AMS CR rate (hourly or daily) | CR rate disclosed per CR estimate |
| Change requests (in project SOW) | T&M project rate | Rate per SOW rate schedule |

### 5.2 Rate Disclosure Rules

| Context | Disclose rate? | What to disclose |
|---|---|---|
| Fixed-price proposal | No | Total fee and payment milestones only |
| T&M SOW | Yes | T&M rate schedule per role/band |
| AMS SOW (retainer) | Partial | Monthly retainer amount; overage hourly rate |
| AMS SOW (hourly) | Yes | Hourly rate per band; overage rate |
| Tender/RFP (public sector) | As required | Follow tender format; disclose where mandated |

### 5.3 Discounting

Discounts from the standard rate card require Commercial Director approval. No discount may be offered in a proposal without sign-off per the Commercial Governance framework (see COMMERCIAL_GOVERNANCE.md). All discounts are applied to the total fee, not to the individual daily rate, to preserve rate card integrity.

---

## 6. Rate Card Maintenance

| Trigger | Action | Owner |
|---|---|---|
| Annual review (January) | Review and update rate schedule | Commercial Director |
| New role added to taxonomy | Add role to this framework; confirm rate band; update rate schedule | Commercial Director + BU Lead |
| Market rate shift (mid-year) | Ad hoc review; update rate schedule if materially misaligned | Commercial Director |
| New BU or service line | Add role taxonomy section; confirm rate schedule | Commercial Director + New BU Lead |

Rate cards are maintained in the Commercial Director's rate schedule document. The framework (this document) is updated when the structure changes — not when individual rates change.

---

## 7. Decision Record

*WP11F-A — Commercial Framework Approval | 2026-06-16 | BU Lead: Hein Blignaut*

| Decision ID | Item | Decision | Applied |
|---|---|---|---|
| BU-RC-001 | Confirm five-band taxonomy | **APPROVED** — Five-band taxonomy (Band 1 Associate → Band 5 Director/Architect) confirmed as APPSolve standard across all BUs | Section 2.2 confirmed |
| BU-RC-002 | AMS-specific roles needed | **APPROVED** — AMS Account Manager (Band 3–4) and AMS Support Consultant (Band 2–3) added to Cross-BU roles | Section 3.5 updated |
| BU-RC-003 | Extended Hours/Public Holiday scope | **APPROVED** — Extended Hours applies at project cutover and hypercare on-call; Public Holiday for on-site cutover on SA public holidays; neither applies to standard remote delivery phases | Section 4.2 updated |
| BU-RC-004 | Rate disclosure in AMS SOWs | **DEFERRED TO COMMERCIAL DIRECTOR** — Whether to disclose hourly rate or total monthly fee only in AMS SOWs is a pricing policy decision for the Commercial Director | CD decision item — no change applied |
| BU-RC-005 | Discounting authority | **RESOLVED** — Discount authority bands confirmed in COMMERCIAL_GOVERNANCE.md Section 2.2: 0–5% BU Lead; 6–10% CD; 11–15% CD+Director; >15% Director+Board | Section 5.3 cross-reference confirmed |
| BU-RC-006 | Oracle HCM Architect band | **APPROVED** — ORA-HCM-ARCH confirmed as Band 4–5; applicable for engagement oversight and presales roles | Section 3.1 confirmed |
| BU-RC-007 | BeBanking role taxonomy completeness | **APPROVED** — BB-LEAD and BB-CON sufficient for current BeBanking portfolio; BeBanking engagements use XBU-PM and XBU-BA for PM and BA roles | Section 3.4 confirmed |
| BU-RC-008 | AMS annual escalation rate | **DEFERRED TO COMMERCIAL DIRECTOR** — Standard annual escalation % for AMS agreements without a specific escalation clause is defined by the Commercial Director annually | CD decision item — no change applied |

**Commercial Director items outstanding: BU-RC-004, BU-RC-008**

---

*RATE_CARD_FRAMEWORK v1.0 | WP11F — Tender Commercial Framework | 2026-06-15 → Approved 2026-06-16 | BU Lead: Hein Blignaut*  
*No actual rates contained in this document | Rates maintained in Commercial Director's rate schedule*  
*Companion: ESTIMATION_GUIDE.md · CR_PRICING_MODEL.md · EFFORT_MULTIPLIERS.md · COMMERCIAL_GOVERNANCE.md*
