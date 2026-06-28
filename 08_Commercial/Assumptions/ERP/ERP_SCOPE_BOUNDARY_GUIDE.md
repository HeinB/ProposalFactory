---
document_id: ERP-SCOPE-BOUNDARY-GUIDE
title: "Oracle ERP — Scope Boundary Guide"
version: "1.0"
created: "2026-06-15"
created_by: "WP11D — Oracle ERP Assumptions Pack"
status: "Draft — Pending BU Lead Review"
applies_to: "All Oracle Fusion ERP (Financials / Procurement / PPM) implementations"
companion_to: "ERP_ASSUMPTIONS_V1.md"
---

# Oracle ERP — Scope Boundary Guide

This document defines scope boundaries for Oracle Fusion ERP implementations. It is the companion document to `ERP_ASSUMPTIONS_V1.md`. Where `ERP_ASSUMPTIONS_V1.md` states what APPSolve does, this guide explains what the boundary looks like in practice — with examples of what is IN scope and what is OUT of scope.

**Authority:** Scope boundary decisions that are not covered by this guide must be escalated to the BU Lead before inclusion in or exclusion from a proposal. Do not make ad hoc scope decisions in the proposal without BU Lead alignment.

---

## How to Use This Guide

1. When preparing an ERP estimate or responding to a tender, check each module against the boundary tables below.
2. Items in the "IN SCOPE" column are included in the APPSolve standard ERP base price.
3. Items in the "OUT OF SCOPE" column are either excluded (priced separately) or not APPSolve's responsibility.
4. Items in "ASSESS CASE BY CASE" require a discussion with the BU Lead before pricing.
5. Pair with `ERP_ASSUMPTIONS_V1.md` for the full assumption statement behind each boundary decision.

---

## 1. General ERP Delivery Boundaries

| IN SCOPE (APPSolve standard) | OUT OF SCOPE (excluded or separately priced) | ASSESS CASE BY CASE |
|---|---|---|
| Oracle ERP configuration using Oracle-delivered configuration tools | Custom code development (APEX apps, PaaS customisations, custom DB schemas) | Groovy scripts in Application Composer — assess per complexity |
| Configuration design workshops and Scope and Design document | Business process redesign consulting | Where business process is entirely undefined — APPSolve can facilitate but client must own output |
| Test script support and testing guidance | Executing UAT on behalf of the client | APPSolve supporting a particularly complex UAT cycle |
| Hypercare: 4 weeks, business hours, defect resolution | Hypercare: enhancements, new modules, new reports | First month-end close support — included by ERP-HYP-004 |
| Train-the-trainer delivery | End-user training delivery | Small team (< 20 users) where client has no internal training capacity |

---

## 2. Chart of Accounts and General Ledger Boundaries

| IN SCOPE (APPSolve standard) | OUT OF SCOPE | ASSESS CASE BY CASE |
|---|---|---|
| One primary ledger per legal entity | Secondary ledgers (IFRS / local GAAP / reporting currency adjustments) | Secondary ledgers where client has a specific statutory reporting requirement (assess per LE count and secondary ledger type) |
| COA configuration based on client-approved design | Designing the client's COA from scratch without client input | APPSolve-facilitated COA workshop where client has a starting point but needs help structuring — included; APPSolve designing from a blank canvas — assess as consulting |
| Up to 6 COA segments | COA redesign post-configuration | Mid-project segment addition — assess as CR |
| Standard cross-validation rules (agreed set) | Complex CVR redesign post-go-live | Large CVR library (>50 rules) — assess effort |
| One standard journal approval workflow | Separate journal approval workflows per BU / journal category / ledger | Multiple journal approval workflows per agreed structure — assess per count |
| Standard FRS financial statement pack (IS / BS / TB / CF) at agreed count | Reports beyond agreed count; custom subledger reports; Oracle Analytics Cloud reports | Additional FRS reports requested in Scope and Design phase — negotiate into agreed count |
| Standard OTBI reporting security | Bespoke OTBI report development beyond agreed count | Data security filters for complex multi-entity access — assess effort |

**Important ledger boundary note:** If the client has a South African operating entity and a Namibian operating entity, they have two legal entities and require two primary ledgers (one ZAR, one NAD). Configuration effort doubles for each additional ledger. Price per LE, not per project.

---

## 3. Accounts Payable Boundaries

| IN SCOPE (APPSolve standard) | OUT OF SCOPE | ASSESS CASE BY CASE |
|---|---|---|
| Manual supplier invoice entry | OCR invoice capture / IDP / intelligent document processing | Any AP automation beyond manual entry — assess as scope addition |
| Three-way match (PO / GRN / Invoice) for PO-based invoices | Oracle Supplier Portal (supplier self-service) | Two-way match where Oracle Receiving is not in scope — per ERP-AP-003 / BU-ERP-003 |
| One non-PO invoice approval workflow | Multiple non-PO approval workflows by BU or department | Complex non-PO approval routing (cross-BU / cross-entity approval) — assess |
| EFT payment file in confirmed bank format | SWIFT direct membership or multi-currency SWIFT payments | FX payment file formatting — assess per bank format |
| Standard payment terms configuration (list provided by client) | Payment terms policy design | Non-standard payment terms (early settlement discount / milestone billing terms) — assess |
| Supplier master FBDI load (data provided by client) | Supplier data extraction from legacy system | Supplier deduplication and data cleansing — client responsibility; APPSolve can advise |

---

## 4. Accounts Receivable Boundaries

| IN SCOPE (APPSolve standard) | OUT OF SCOPE | ASSESS CASE BY CASE |
|---|---|---|
| Customer master FBDI load | Customer data extraction from legacy | Customer credit limit migration — included in standard customer FBDI |
| AR transaction types per confirmed design | Oracle Revenue Management Cloud (complex IFRS 15) | IFRS 15 multi-element arrangement accounting — assess; likely requires Oracle RMC |
| Auto-invoicing from Oracle module (PPM / Order Mgmt) in same project | Auto-invoicing from non-Oracle source without OIC integration | Auto-invoicing from Acumatica or other non-Oracle ERP — requires OIC integration |
| Standard auto-cash rules for EFT receipts | Lockbox processing | High-volume B2C receipts with complex application rules — assess complexity |
| Oracle Collections Management framework | Operating the collections process | Dunning letter content and credit control policy design — client's responsibility |

---

## 5. Fixed Assets Boundaries

| IN SCOPE (APPSolve standard) | OUT OF SCOPE | ASSESS CASE BY CASE |
|---|---|---|
| Asset category and depreciation method configuration | Physical asset verification / stocktake | Assisting client with organising asset data — advisory only |
| Opening balance migration (original cost / accumulated depreciation / NBV / remaining life) | Full historical depreciation run history | Impairment testing and impairment journal posting — excluded (IFRS expertise required) |
| One standard capex approval workflow | Complex capex management workflows (multi-stage CAPEX committee approval) | Capex tracking by project / by budget vs. actual — assess per Oracle PPM integration |
| Monthly depreciation batch configuration | Running monthly depreciation for client post-go-live | Assisting client's finance team with first depreciation run — included in hypercare |
| SA tax book (Section 11/12 SITA) configuration where required | Tax impairment analysis | IFRS 16 lease accounting — excluded; requires Oracle Lease Accounting or separate process |

---

## 6. Cash Management Boundaries

| IN SCOPE (APPSolve standard) | OUT OF SCOPE | ASSESS CASE BY CASE |
|---|---|---|
| Bank account configuration in Oracle CM | Bank account opening at the bank | Adding bank accounts post-go-live — low-effort admin; not a CR |
| Bank statement import configuration (MT940 / camt.053 / BeBanking) | Bank statement format conversion for proprietary formats | Proprietary bank format not natively supported by Oracle — assess OIC file transformation |
| Automated bank reconciliation rules | Manual bank reconciliation on behalf of client | Reconciliation with complex multi-currency expositions — assess effort |
| Cash positioning configuration | Cash flow forecasting model building | Integration to treasury management system — assess as OIC integration |

---

## 7. Procurement Boundaries

| IN SCOPE (APPSolve standard) | OUT OF SCOPE | ASSESS CASE BY CASE |
|---|---|---|
| Self-Service Procurement (PR entry) | Oracle Supplier Portal (supplier self-service) | Oracle Procurement Contracts — only where in BOM |
| One approval hierarchy per workflow type (Requisition / PO) | Multiple parallel hierarchies by BU | Supplier-managed inventory and consignment inventory — not in standard Procurement scope |
| Hosted item catalogue from client-provided data | Punchout catalogues to supplier-hosted catalogues | Catalogue data import from client's existing procurement system — assess per format |
| Oracle Receiving (goods receipts against POs) | Physical goods inspection or quality management | Receiving on mobile device / tablet — Oracle-delivered feature; confirm device availability |
| Oracle Sourcing (RFQ / RFP) where licensed | Reverse auctions / e-procurement platform | Complex sourcing event design and facilitation — consulting, not configuration |

---

## 8. PPM Boundaries

| IN SCOPE (APPSolve standard) | OUT OF SCOPE | ASSESS CASE BY CASE |
|---|---|---|
| Project types and templates configured from client data | Project management office (PMO) setup and operation | Oracle Project Billing — only where in BOM |
| Project costing via Oracle-standard cost collection | External project management tools (MS Project / Smartsheet) | Oracle Time and Labour for project timecards — only where Oracle OTL is in BOM |
| Project budget setup and approval | Project financial performance monitoring and reporting | Oracle Project Contract Management — separately licensed |
| Oracle PPM to Oracle GL via Oracle subledger accounting | OIC integration for PPM to non-Oracle systems | Complex revenue recognition from PPM to AR (milestone billing, T&M, cost-plus) — included where Oracle Project Billing is in BOM |
| Standard OTBI PPM reports at agreed count | Oracle Analytics Cloud project dashboards | Power BI or third-party analytics from Oracle PPM data — requires OIC extract integration |

---

## 9. Integration Scope Boundary (ERP-Specific)

The full integration scope boundary is governed by `OIC_ASSUMPTIONS_V1.md`. The following ERP-specific boundary points supplement the OIC pack:

| Scenario | Boundary Decision | Assumption |
|---|---|---|
| Oracle ERP to Oracle HCM (same project) | Oracle-native — NOT an OIC integration | ERP-INT-002 |
| Oracle AP to Oracle GL (subledger posting) | Oracle-native — NOT an OIC integration | ERP-INT-003 |
| Oracle Procurement to Oracle AP (three-way match) | Oracle-native — NOT an OIC integration | ERP-INT-003 |
| Oracle PPM costs to Oracle GL | Oracle-native — NOT an OIC integration | ERP-INT-003, ERP-PPM-006 |
| Oracle ERP to BeBanking (EFT payment file) | OIC integration — priced per OIC pack (typically Standard tier) | ERP-INT-004 |
| BeBanking to Oracle CM (MT940 bank statement) | OIC integration — priced per OIC pack | ERP-INT-004 |
| Oracle ERP to SARS eFiling | Excluded — not possible; client submits manually | ERP-INT-005, ERP-EXC-003 |
| Oracle ERP to PaySpace (payroll) | OIC integration — priced per OIC pack | ERP-EXC-001 |
| Oracle ERP to third-party reporting (Power BI / Tableau) | OIC integration (extract) or Oracle OTBI direct connector — assess per target |  |
| Oracle ERP to Oracle Analytics Cloud | Oracle-native FAW connector — NOT typically an OIC integration | ERP-REP-004 |
| Oracle ERP to Acumatica (inter-system) | OIC integration — assess complexity; likely Complex tier |  |

---

## 10. Common Scope Creep Scenarios — How to Handle

The following scenarios occur frequently in ERP proposals. The correct response is listed for each.

### "Can you migrate our historical invoices?"
**Correct response:** Historical transaction data is excluded (ERP-DAT-003). Opening balances only. The client retains the legacy system for historical reference. If the client has a regulatory or audit requirement to have historical data accessible, we can discuss an Oracle archive strategy, but this is separately scoped consulting.

### "We need to run the old system in parallel for three months while we get comfortable with Oracle."
**Correct response:** Parallel running is excluded (ERP-CUT-005 / ERP-EXC-008). Parallel running doubles data entry burden and extends the project significantly. We recommend a cutover with a well-tested shadow run in CRP2 and UAT, plus strong hypercare, instead of a formal parallel run. If the client insists, this is a scope addition — assess effort and provide a separate price.

### "We need a dashboard to see all our financial KPIs."
**Correct response:** Standard OTBI reports and FRS financial statements are in scope at the agreed count. An Oracle Analytics Cloud (OAX/FAW) dashboard is separately licensed and excluded (ERP-REP-004). For OTBI-based dashboards within the agreed report count, this is in scope. For OAX dashboards, this requires a separate Oracle licence and is separately priced.

### "Our SARS auditor wants a full audit trail report with every transaction."
**Correct response:** Oracle ERP provides a complete audit trail natively (every transaction in the subledger has a full audit history). OTBI-based audit reports are available from the standard report set. Bespoke CAAT reports for the auditor are excluded (ERP-EXC-012). We can scope bespoke audit reports as a separately priced item if the auditor has a specific format requirement.

### "We need our suppliers to be able to log in and submit invoices directly."
**Correct response:** The Oracle Supplier Portal is excluded from base scope (ERP-AP-007 / ERP-EXC-005). Supplier Portal requires a separate Oracle licence and an OIC integration for portal-to-AP invoice submission. This can be added to the project scope with a separate licence and configuration quote.

### "We want Single Sign-On so our users don't have to log in twice."
**Correct response:** SSO is assessed as a separately scoped item (ERP-SEC-006 / BU-ERP-008 pending). Oracle Fusion ERP supports SAML 2.0 SSO. The IdP-to-Oracle configuration requires a design and configuration engagement with the client's IT security team. This is not in base scope.

### "Can you also handle our commission calculations?"
**Correct response:** Commission schemes are not in Oracle Fusion Financials or Workforce Compensation base scope. Complex commission calculations require Oracle Incentive Compensation (separately licensed) or are managed outside Oracle ERP. The payroll integration carries commission payments once calculated — but the calculation engine is not in scope.

---

*ERP_SCOPE_BOUNDARY_GUIDE v1.0 | WP11D — Oracle ERP Assumptions Pack | 2026-06-15*  
*Companion to ERP_ASSUMPTIONS_V1.md | Draft — validate against first two Oracle ERP SOWs before promoting to Approved*  
*Questions: Oracle BU Lead | Escalation: Delivery Director*
