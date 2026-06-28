---
document_id: W4-ERP-002-ORA-FusionProcurement
title: "Oracle Fusion Procurement — Capability Statement"
version: "1.0 Candidate Draft"
status: "Candidate Draft"
review_status: "Candidate"
approved_for_reuse: "No"
business_unit: "Oracle"
wave: "4"
deliverable: "W4-ERP-002"
created: "2026-06-14"
created_by: "Claude (AI — Wave 4 W4-ERP-002 extraction)"
source_document: "ORACLE_FACT_BASELINE Section 11 (Cape Union Mart — Oracle Fusion Finance + Procurement confirmed; Investec — Oracle Fusion Finance + Procurement multi-country SA/USA/UK; DFA — Oracle Fusion full suite including Procurement — internal Rule 21.4 — NEVER NAMED); Reference letters: Cape Union Mart_Reference Letter.pdf (SABS ETS); Reference 2023 09 Investec Letter.pdf (ATNS + SABS ETS)"
source_status: "Tier 1 Confirmed Delivery (Cape Union Mart — Fusion Finance + Procurement; Investec — Fusion Finance + Procurement multi-country; DFA — internal Rule 21.4); Reference letters identified in corpus but not yet confirmed/registered"
prereq_statement: "W4-ERP-001-ORA-FusionFinancials (companion Finance statement — Procurement integrates with Oracle AP for supplier invoice matching and payment); W2S1-001-ORA-FusionCapability (parent Oracle Fusion platform overview)"
kb_destination: "06_Capabilities/Oracle/"
tags: "Oracle,Fusion,Procurement,Oracle Fusion Procurement,iProcurement,Purchasing,Sourcing,Supplier Management,Self-Service Procurement,Oracle Cloud ERP"
---

> **CANDIDATE DRAFT — approved_for_reuse: No — Pending BU Lead review and promotion to Review_Required**

> **CRITICAL GOVERNANCE NOTE — NAMED REFERENCES (AM-W4E2-001):** No reference client (Cape Union Mart, Investec) may be named in any external tender submission until: (a) their signed reference letter is confirmed and registered in `04_References/Oracle/`; (b) account manager approval is obtained for the specific tender. Where no letter is yet registered, use: *"APPSolve has delivered Oracle Fusion Procurement across multi-country, multi-entity environments including financial services and retail sectors."*

---

# Oracle Fusion Procurement

**Capability Statement | APPSolve | Oracle Business Unit**
*Document ID: W4-ERP-002-ORA-FusionProcurement | Version: 1.0 Candidate Draft | Wave 4*

---

## Section 1: Statement of Capability

APPSolve implements Oracle Fusion Procurement — Oracle's cloud-native enterprise procurement platform, integrated within the Oracle Fusion Cloud ERP suite. Oracle Fusion Procurement enables organisations to manage the complete procure-to-pay lifecycle: from purchase requisitioning and supplier sourcing through purchase order management, supplier contracts, and invoice matching.

APPSolve delivers Oracle Fusion Procurement as an integrated component of Oracle Fusion ERP implementations, typically deployed alongside Oracle Fusion Financials (W4-ERP-001) within a unified Oracle Cloud ERP environment.

> **Confirmed delivery:** Oracle Fusion Procurement delivered as part of Oracle Fusion ERP implementations for Cape Union Mart and Investec (multi-country: SA, USA, UK). Reference letters identified in corpus — pending signed status confirmation.

| Capability Area | Coverage | APPSolve Positioning |
|---|---|---|
| **Purchase Requisitions (Self-Service)** | Employee self-service purchase requests via Oracle iProcurement / Self-Service portal | **Confirmed delivery capability** — self-service requisitioning within Oracle Fusion |
| **Purchase Order Management** | PO creation, approval workflows, PO amendments, blanket POs | **Confirmed delivery capability** — PO management integrated with Oracle AP |
| **Supplier Sourcing** | Request for Quotation (RFQ), supplier bid evaluation, sourcing award | **Confirmed delivery capability** — sourcing events within Oracle Fusion Procurement |
| **Supplier Master Management** | Supplier registration, supplier qualification, supplier portal | **Confirmed delivery capability** — supplier lifecycle management within Oracle |
| **Contract Management** | Purchase contracts, blanket purchase agreements, contract compliance tracking | **Confirmed delivery capability** — procurement contracts within Oracle |
| **Three-Way Matching** | PO → Goods Receipt → Supplier Invoice automated matching within Oracle AP | **Confirmed delivery capability** — integrated with Oracle AP (W4-ERP-001) |
| **Spend Analytics** | Procurement spend dashboards, supplier performance reporting, savings tracking | **Confirmed delivery capability** — OTBI-based procurement analytics |
| **Multi-Country Procurement** | Cross-entity and cross-currency procurement across multiple legal entities | **Confirmed delivery** — Investec (SA, USA, UK multi-country procurement) |

---

## Section 2: Product Architecture

### 2.1 Oracle Fusion Procurement — Procure-to-Pay Flow

```
Oracle Fusion Procurement — Procure-to-Pay
  ├── Sourcing
  │   ├── RFQ / RFP management
  │   ├── Supplier bid evaluation
  │   └── Sourcing award and contract
  ├── Requisitioning (Self-Service)
  │   ├── Employee purchase requisition (Oracle iProcurement)
  │   ├── Shopping catalogue
  │   └── Requisition approval workflow
  ├── Purchase Orders
  │   ├── Standard PO / Blanket PO / Contract PO
  │   ├── PO approval workflow
  │   └── PO change management
  ├── Supplier Management
  │   ├── Supplier registration and qualification
  │   ├── Supplier portal (self-service)
  │   └── Supplier performance scoring
  └── Integration with Oracle Financials
      ├── Three-way match (PO → Receipt → Invoice)
      ├── AP invoice approval from procurement
      └── Spend → GL cost coding
```

### 2.2 Use with W4-ERP-001 (Oracle Fusion Financials)

Oracle Fusion Procurement is typically tendered and delivered together with Oracle Fusion Financials. The procure-to-pay process spans both modules: procurement manages the requisition-to-PO cycle; Oracle AP (part of W4-ERP-001) manages the invoice-to-payment cycle. For tender responses requiring full Oracle Cloud ERP positioning, W4-ERP-001 and W4-ERP-002 should be used together.

---

## Section 3: Source Mapping

| Source | HIST ID / Reference | Evidence Type | Applicable Sections | Usage Restrictions |
|---|---|---|---|---|
| ORACLE_FACT_BASELINE Section 11 — Cape Union Mart | Internal reference | Tier 1 Confirmed Delivery | Oracle Fusion Finance + Procurement (Retail) | "Cape Union Mart_Reference Letter.pdf" not confirmed signed; not registered. Confirm before naming. Also confirm scope (not Acumatica PaySpace engagement). |
| ORACLE_FACT_BASELINE Section 11 — Investec | Internal reference | Tier 1 Confirmed Delivery | Oracle Fusion Finance + Procurement multi-country (SA, USA, UK) | "Reference 2023 09 Investec Letter.pdf" not confirmed signed; not registered. Confirm before naming. |
| DFA (internal) | Internal (Rule 21.4) | Internal Evidence Only | Oracle Fusion Procurement — full suite | **DFA NEVER NAMED — Rule 21.4 permanent** |

---

## Section 4: Evidence Classification

| Field | Value |
|---|---|
| **Evidence Tier** | **Tier 1 — Confirmed Delivery** (Cape Union Mart, Investec confirmed) |
| **Primary Evidence** | Cape Union Mart (Oracle Fusion Finance + Procurement); Investec (Oracle Fusion Finance + Procurement multi-country) |
| **Internal Evidence** | DFA (Rule 21.4 — full Fusion suite including Procurement; never named) |
| **Named References** | Cape Union Mart; Investec — **pending letter confirmation.** Do not name until signed letters confirmed and registered. |
| **Sector Coverage** | Retail (Cape Union Mart); Financial Services (Investec) |
| **Restriction Summary** | DFA never named (Rule 21.4); reference letters must be confirmed signed before naming clients in tenders |

---

## Section 5: Approved and Prohibited Wording

### Approved Wording

> "APPSolve implements Oracle Fusion Procurement within the Oracle Cloud ERP platform, enabling organisations to manage the complete procure-to-pay lifecycle — from self-service requisitioning and supplier sourcing through purchase order management, supplier contract governance, and three-way invoice matching."

> "APPSolve has delivered Oracle Fusion Procurement across multi-country, multi-entity environments, including cross-border procurement with multi-currency PO processing and multi-jurisdictional supplier management."

> "Oracle Fusion Procurement, implemented by APPSolve, integrates natively with Oracle Accounts Payable — providing complete spend visibility from purchase requisition through supplier payment in a unified Oracle Cloud ERP environment."

### Prohibited Wording

- Do NOT name DFA as a client, example, or reference (Rule 21.4 permanent)
- Do NOT name Cape Union Mart or Investec until signed reference letters confirmed and account manager approval obtained
- Do NOT conflate Oracle Fusion Procurement with Oracle EBS iProcurement — different platform generations (use W2S1-002 for EBS)
- Do NOT conflate Oracle Fusion Procurement with Acumatica Distribution (W1S2-002) — entirely different products

---

## Section 6: Pre-Tender Validation Checks

Before including this capability statement in any tender submission, confirm all of the following:

- [ ] **PT-W4E2-001:** For each client to be named — confirm signed reference letter exists and is registered in `04_References/Oracle/`
- [ ] **PT-W4E2-002:** For each client to be named — account manager or BU Lead approval obtained for this specific tender submission
- [ ] **PT-W4E2-003:** DFA is NOT named in any Procurement content — Rule 21.4 check
- [ ] **PT-W4E2-004:** Tender specifies Oracle Fusion Procurement (Cloud) — not Oracle EBS iProcurement
- [ ] **PT-W4E2-005:** Cape Union Mart scope confirmed explicitly with BU Lead: confirm which APPSolve engagement is covered by the Cape Union Mart reference letter — Oracle Fusion Procurement vs. Acumatica/PaySpace (Cape Union Mart has two separate APPSolve engagements). Do not cite the Cape Union Mart letter for Oracle Procurement until this is confirmed. If unconfirmed, remove Cape Union Mart from Procurement references in this tender.
- [ ] **PT-W4E2-006:** BEE certificate validity confirmed (expires 2026-07-31)

---

## Section 7: Named Reference Controls

| Client | Reference Status | Permitted Use | Restrictions |
|---|---|---|---|
| **Cape Union Mart** | Pending letter confirmation | Oracle Fusion Finance + Procurement (Retail sector) | **Not confirmed signed; not registered.** Do not name until confirmed. Also verify this letter covers Oracle Fusion (not Acumatica/PaySpace). |
| **Investec** | Pending letter confirmation | Oracle Fusion Finance + Procurement multi-country (SA, USA, UK) | **Not confirmed signed; not registered.** Do not name until confirmed. |
| DFA | NEVER NAMED | Internal evidence only | **Rule 21.4 — permanent** |

---

## Section 8: Product Boundary Controls

| Product | Relationship | Boundary Rule |
|---|---|---|
| **Oracle Fusion Procurement** | THIS STATEMENT | Oracle Cloud-native procurement platform — part of Oracle Fusion ERP |
| **Oracle Fusion Financials (W4-ERP-001)** | Companion statement | Procurement + Finance = full procure-to-pay Oracle Cloud ERP. Use together. |
| **Oracle EBS iProcurement / Purchasing (W2S1-002)** | Different platform generation | EBS = on-premises/legacy platform. Fusion = cloud-native. Different architecture. Do NOT conflate evidence. |
| **Acumatica Distribution (W1S2-002)** | Different product | Acumatica is a completely different ERP. No connection. |
| **BeBanking Supplier Payments (W1S3-003)** | Related (payment execution) | BeBanking executes the supplier payment after Oracle AP approves. Different capability layer. |

---

## Section 9: Extraction Log

| Field | Value |
|---|---|
| **Wave** | 4 |
| **Extraction Date** | 2026-06-14 |
| **Extractor** | Claude (AI — Wave 4 extraction authorised by BU Lead 2026-06-14) |
| **BU Lead Decision** | W4-ERP-002 Oracle Fusion Procurement — Medium priority; combine with W4-ERP-001 for full Oracle ERP positioning; eligible for Wave 4 extraction |
| **Primary Source** | ORACLE_FACT_BASELINE Section 11 (Cape Union Mart, Investec) |
| **Evidence Tier at Extraction** | Tier 1 (Cape Union Mart, Investec confirmed) |
| **Blocked Pending** | Reference letter confirmation — do NOT name clients externally until letters confirmed signed and registered |
| **Status** | Candidate Draft — approved_for_reuse: No |
| **Next Action** | BU Lead review → Register reference letters → Promotion to Review_Required |
| **Promotion Requirement** | BU Lead sets approved_for_reuse: Yes after review |

---

*W4-ERP-002-ORA-FusionProcurement-DRAFT.md v1.0 — Candidate Draft 2026-06-14*
*Do not use in tender responses. approved_for_reuse: No.*
