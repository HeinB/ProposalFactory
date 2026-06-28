---
document_id: W4-ERP-001-ORA-FusionFinancials
title: "Oracle Fusion Financials — Capability Statement"
version: "1.0"
status: "Approved"
review_status: "Approved"
approved_for_reuse: "Yes"
lifecycle_status: APPROVED
approved_date: "2026-06-14"
approved_by: "Hein Blignaut (BU Lead)"
business_unit: "Oracle"
wave: "4"
deliverable: "W4-ERP-001"
created: "2026-06-14"
created_by: "Claude (AI — Wave 4 W4-ERP-001 extraction)"
source_document: "ORACLE_FACT_BASELINE Section 11 (Cape Union Mart — Oracle Fusion Finance + Procurement; Investec — Oracle Fusion Finance multi-country SA/USA/UK; NALA Renewables — Oracle Fusion Finance 8 countries Lithuania/Finland/Romania + others; DFA — Oracle Fusion Finance full suite internal — NEVER NAMED Rule 21.4); HIST-002 (MTN — Oracle EBS DBA; not Fusion Finance but confirms Oracle ERP relationship); Reference letters in corpus: Reference 2023 09 Investec Letter.pdf (ATNS + SABS ETS); Nala Renewables Reference Letter Appsolve.pdf; Cape Union Mart_Reference Letter.pdf"
source_status: "Tier 1 Confirmed Delivery (Cape Union Mart — Fusion Finance + Procurement; Investec — Fusion Finance multi-country; NALA Renewables — Fusion Finance 8 countries; DFA — internal Rule 21.4); Reference letters identified in corpus but not yet confirmed/registered"
prereq_statement: "W2S1-001-ORA-FusionCapability (Oracle Fusion Capability Statement — parent platform overview; W4-ERP-001 provides module-level Finance depth)"
kb_destination: "06_Capabilities/Oracle/"
tags: "Oracle,Fusion,Financials,Finance,Oracle Fusion Finance,GL,AR,AP,Fixed Assets,Cash Management,Multi-Country,IFRS,Oracle Cloud ERP,Treasury"
---

> **CRITICAL GOVERNANCE NOTE — NAMED REFERENCES (AM-W4E1-001):** No reference client (Investec, NALA Renewables, Cape Union Mart) may be named in any external tender submission until: (a) their signed reference letter is confirmed and registered in `04_References/Oracle/`; (b) account manager approval is obtained for the specific tender. Where no letter is yet registered, use: *"APPSolve has delivered Oracle Fusion Financials across multi-country environments in Sub-Saharan Africa, Europe, and North America."*

---

# Oracle Fusion Financials

**Capability Statement | APPSolve | Oracle Business Unit**
*Document ID: W4-ERP-001-ORA-FusionFinancials | Version: 1.0 | Wave 4 | Approved 2026-06-14*

---

## Section 1: Statement of Capability

APPSolve implements and supports Oracle Fusion Financials — Oracle's cloud-native enterprise financial management platform. Oracle Fusion Financials is the core financial module of the Oracle Fusion Cloud ERP suite, providing organisations with a unified, multi-currency, multi-entity financial management environment that is fully IFRS-compliant and globally deployable.

APPSolve has delivered Oracle Fusion Financials across multi-country environments spanning Sub-Saharan Africa, Europe, and North America. APPSolve's Fusion Finance capability covers the full financial management suite from General Ledger and Accounts Payable through Fixed Assets, Cash Management, and Financial Reporting.

> **Confirmed delivery:** Oracle Fusion Financials delivered for Investec (3 countries: SA, USA, UK), NALA Renewables (8 countries including EU markets), and Cape Union Mart (Oracle Fusion Finance + Procurement). Reference letters identified in corpus — pending registration confirmation.

| Capability Area | Coverage | APPSolve Positioning |
|---|---|---|
| **General Ledger (GL)** | Chart of accounts design, journal entries, period management, intercompany, consolidation, IFRS-compliant reporting | **Confirmed delivery** — multi-entity GL across multiple international implementations |
| **Accounts Payable (AP)** | Supplier invoice processing, payment runs, supplier statements, AP automation, three-way matching | **Confirmed delivery** — AP within Oracle Fusion Finance implementations |
| **Accounts Receivable (AR)** | Customer invoicing, receipts, credit management, collections, AR ageing | **Confirmed delivery** — AR within Oracle Fusion Finance implementations |
| **Fixed Assets** | Asset register, depreciation calculations, revaluations, disposals, IFRS compliance | **Confirmed delivery** — Fixed Assets within Fusion Finance scope |
| **Cash Management** | Bank reconciliation, bank statement import, cash forecasting, treasury integration | **Confirmed delivery** — Cash Management within Fusion Finance implementations |
| **Multi-Currency & Multi-Entity** | Currency revaluation, translation, multi-ledger architecture, intercompany eliminations | **Confirmed delivery** — Investec (SA, USA, UK); NALA Renewables (8 countries) |
| **Tax Management** | Oracle Tax (VAT, WHT, GST configuration) — multi-jurisdictional tax rules | **Confirmed delivery** — multi-country tax configuration across implementations |
| **Financial Reporting** | Oracle Financial Reporting Cloud (FRC), OTBI dashboards, trial balance, management accounts | **Confirmed delivery** — reporting framework within all Fusion Finance implementations |
| **IFRS Compliance** | IFRS 9 (financial instruments), IFRS 15 (revenue recognition), IFRS 16 (leases), IAS 16, IAS 2 | **Confirmed delivery capability** — all implementations designed to IFRS standards |

---

## Section 2: Product Architecture

### 2.1 Oracle Fusion Cloud ERP Financial Suite

```
Oracle Fusion Cloud ERP — Financial Management Suite
  ├── General Ledger
  │   ├── Multi-ledger (Primary + Secondary)
  │   ├── Multi-currency (functional + reporting currencies)
  │   ├── Period close management
  │   ├── Intercompany balancing
  │   └── Financial Reporting Cloud (FRC)
  ├── Accounts Payable
  │   ├── Supplier master management
  │   ├── Invoice processing (manual + automated)
  │   ├── Payment runs (domestic + international)
  │   └── AP reconciliation
  ├── Accounts Receivable
  │   ├── Customer master management
  │   ├── Invoice generation
  │   ├── Receipt application
  │   └── Collections management
  ├── Fixed Assets
  │   ├── Asset register
  │   ├── Depreciation (straight-line, reducing balance, IFRS)
  │   ├── Asset disposals and transfers
  │   └── IFRS 16 right-of-use assets
  ├── Cash Management
  │   ├── Bank statement import (ISO 20022, MT940)
  │   ├── Bank reconciliation (manual + auto-matching)
  │   └── Cash forecasting
  └── Tax Management
      ├── Multi-jurisdictional tax rules
      ├── VAT (SA), GST, WHT
      └── IFRS-compliant tax reporting
```

### 2.2 Multi-Country Architecture (APPSolve Differentiator)

APPSolve has delivered Oracle Fusion Financials across multi-country, multi-entity environments:
- **Investec:** 3 countries (South Africa, USA, UK) — separate ledgers, inter-entity reporting
- **NALA Renewables:** 8 countries (Lithuania, Finland, Romania + EU markets) — multi-lingual, multi-currency, EU VAT compliance
- Multi-country Oracle Fusion Finance is a rare differentiator — enables APPSolve to compete for international scope tenders

---

## Section 3: Source Mapping

| Source | HIST ID / Reference | Evidence Type | Applicable Sections | Usage Restrictions |
|---|---|---|---|---|
| ORACLE_FACT_BASELINE Section 11 — Investec | Internal reference | Tier 1 Confirmed Delivery | Oracle Fusion Finance + Procurement; 3 countries (SA, USA, UK) | Reference letter "Reference 2023 09 Investec Letter.pdf" — confirm signed before naming in tender |
| ORACLE_FACT_BASELINE Section 11 — NALA Renewables | Internal reference | Tier 1 Confirmed Delivery | Oracle Fusion Finance; 8 countries (EU markets) | "Nala Renewables Reference Letter Appsolve.pdf" — confirm signed before naming in tender |
| ORACLE_FACT_BASELINE Section 11 — Cape Union Mart | Internal reference | Tier 1 Confirmed Delivery | Oracle Fusion Finance + Procurement | "Cape Union Mart_Reference Letter.pdf" — confirm signed before naming in tender. Note: separate Acumatica PaySpace engagement (CATS) — confirm which solution this letter covers. |
| DFA (internal) | Internal (Rule 21.4) | Internal Evidence Only | Oracle Fusion Finance — full suite | **DFA NEVER NAMED — Rule 21.4 permanent** |

---

## Section 4: Evidence Classification

| Field | Value |
|---|---|
| **Evidence Tier** | **Tier 1 — Confirmed Delivery** (multiple clients) |
| **Primary Evidence** | Investec (Fusion Finance multi-country); NALA Renewables (Fusion Finance 8 countries); Cape Union Mart (Fusion Finance + Procurement) |
| **Internal Evidence** | DFA (Rule 21.4 — full Fusion Finance suite; never named) |
| **Named References** | Investec; NALA Renewables; Cape Union Mart — all **pending letter confirmation.** Reference letters identified in corpus but signed status not confirmed and letters not registered in `04_References/Oracle/` as of 2026-06-14. |
| **Sector Coverage** | Financial Services (Investec); Renewable Energy / International (NALA Renewables); Retail (Cape Union Mart) |
| **Key Differentiator** | Multi-country Oracle Fusion Finance (3 countries and 8 countries) — rare capability in South African Oracle partner market |
| **Restriction Summary** | DFA never named (Rule 21.4); reference letters must be confirmed signed before naming clients in tender submissions |

---

## Section 5: Approved and Prohibited Wording

### Approved Wording

> "APPSolve implements Oracle Fusion Financials across multi-country, multi-entity environments, delivering GL, AP, AR, Fixed Assets, and Cash Management within a unified, IFRS-compliant Oracle Cloud ERP platform."

> "APPSolve has delivered Oracle Fusion Financials across geographies including South Africa, the United Kingdom, the United States of America, and European Union markets — providing multi-currency consolidation, multi-jurisdictional tax compliance, and real-time financial reporting across complex international financial structures."

> "APPSolve's Oracle Fusion Finance implementations are designed to IFRS standards from inception, ensuring that chart of accounts design, period close procedures, fixed asset depreciation, and revenue recognition align with applicable IFRS requirements."

### Prohibited Wording

- Do NOT name DFA as a client, example, or reference (Rule 21.4 permanent)
- Do NOT name Investec, NALA Renewables, or Cape Union Mart as references until signed letters are confirmed and BU Lead / account manager approval obtained for the specific tender
- Do NOT conflate Oracle Fusion Finance (W4-ERP-001) with Oracle EBS Finance (W2S1-002) — these are different platforms; do not claim EBS Finance evidence for Fusion Finance tenders
- Do NOT conflate Oracle Fusion Finance with Acumatica Financials (W1S2-001) — entirely different products

---

## Section 6: Pre-Tender Validation Checks

Before including this capability statement in any tender submission, confirm all of the following:

- [ ] **PT-W4E1-001:** For each client to be named — confirm signed reference letter exists and is registered in `04_References/Oracle/`
- [ ] **PT-W4E1-002:** For each client to be named — account manager or BU Lead approval obtained for this specific tender submission
- [ ] **PT-W4E1-003:** DFA is NOT named in any Finance content — Rule 21.4 check
- [ ] **PT-W4E1-004:** Tender specifies Oracle Fusion Finance (Cloud) — not Oracle EBS Finance; if EBS, use W2S1-002 instead
- [ ] **PT-W4E1-005:** Cape Union Mart scope confirmed explicitly with BU Lead: confirm which APPSolve engagement is covered by the Cape Union Mart reference letter — Oracle Fusion Finance vs. Acumatica/PaySpace (Cape Union Mart has two separate APPSolve engagements). Do not cite the Cape Union Mart letter for Oracle Finance until this is confirmed. If unconfirmed, remove Cape Union Mart from Finance references in this tender.
- [ ] **PT-W4E1-006:** BEE certificate validity confirmed (expires 2026-07-31)

---

## Section 7: Named Reference Controls

| Client | Reference Status | Permitted Use | Restrictions |
|---|---|---|---|
| **Investec** | Pending letter confirmation | Oracle Fusion Finance multi-country (SA, USA, UK) — strong differentiator | **Letter "Reference 2023 09 Investec Letter.pdf" not confirmed signed; not registered in KB.** Do not name until confirmed. |
| **NALA Renewables** | Pending letter confirmation | Oracle Fusion Finance international (8 countries, EU markets) | **Letter "Nala Renewables Reference Letter Appsolve.pdf" not confirmed signed; not registered.** Do not name until confirmed. |
| **Cape Union Mart** | Pending letter confirmation | Oracle Fusion Finance + Procurement (Retail sector) | **Letter "Cape Union Mart_Reference Letter.pdf" not confirmed signed; not registered. Also — confirm this letter covers Oracle Fusion Finance (not Acumatica/PaySpace).** |
| DFA | NEVER NAMED | Internal evidence only | **Rule 21.4 — permanent and absolute** |

---

## Section 8: Product Boundary Controls

| Product | Relationship | Boundary Rule |
|---|---|---|
| **Oracle Fusion Financials** | THIS STATEMENT | Oracle Fusion Cloud ERP — GL, AP, AR, Fixed Assets, Cash Management; cloud-native platform |
| **Oracle EBS Finance (W2S1-002)** | Different platform | Oracle EBS is the legacy on-premises platform. Fusion is cloud-native. Do NOT conflate. Different clients, different architecture. |
| **Oracle Fusion Procurement (W4-ERP-002)** | Companion statement | Procurement is a sub-module of Oracle Fusion ERP alongside Finance. Cape Union Mart and Investec cover both. Use together for full Fusion ERP positioning. |
| **Acumatica Financials (W1S2-001)** | Different product | Acumatica is a completely different ERP. Do NOT conflate. |
| **Oracle PPM (W4-ERP-003)** | Integration | PPM project costs flow to Oracle Finance GL. Finance is the accounting system of record. |
| **BeBanking H2H** | Integration target | BeBanking connects to Oracle ERP for payment initiation. Oracle Finance is a BeBanking integration target — not the same product. |

---

## Section 9: Extraction Log

| Field | Value |
|---|---|
| **Wave** | 4 |
| **Extraction Date** | 2026-06-14 |
| **Extractor** | Claude (AI — Wave 4 extraction authorised by BU Lead 2026-06-14) |
| **BU Lead Decision** | W4-ERP-001 Oracle Fusion Financials — High priority; Tier 1 evidence (Cape Union Mart, Investec, NALA Renewables); eligible for Wave 4 extraction |
| **Primary Source** | ORACLE_FACT_BASELINE Section 11 (Investec, NALA Renewables, Cape Union Mart) |
| **Evidence Tier at Extraction** | Tier 1 (multiple confirmed clients) |
| **Named Reference Restriction** | No client may be named externally until signed reference letter confirmed and registered in `04_References/Oracle/` |
| **Status** | **Approved — approved_for_reuse: Yes (Hein Blignaut, BU Lead, 2026-06-14)** |
| **Next Action** | Approved 2026-06-14. Reference letter registration required to unlock named client references. Apply all pre-tender validation checks (PT-W4E1-001 through PT-W4E1-006) before use in any tender. |
| **Promotion Requirement** | BU Lead set approved_for_reuse: Yes (Hein Blignaut, 2026-06-14). Wave 4 promotion complete. |

---

*W4-ERP-001-ORA-FusionFinancials.md v1.0 — Approved 2026-06-14 by Hein Blignaut (BU Lead). approved_for_reuse: Yes.*
