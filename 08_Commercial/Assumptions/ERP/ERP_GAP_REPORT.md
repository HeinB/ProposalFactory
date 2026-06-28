---
document_id: ERP-GAP-REPORT
title: "Oracle ERP Assumptions — Gap Report"
version: "1.0"
created: "2026-06-15"
created_by: "WP11D — Oracle ERP Assumptions Pack"
status: "Draft — Active Gaps"
tracks: "ERP_ASSUMPTIONS_V1.md"
---

# Oracle ERP Assumptions — Gap Report

This report identifies gaps in APPSolve's commercial governance for Oracle Fusion ERP implementations. A gap exists where an assumption in the ERP pack requires supporting documentation, a rate card, a template, or a policy decision that does not yet exist.

Gaps are classified as:
- **CRITICAL** — Must be resolved before the next Oracle ERP SOW is issued or a tender response submitted
- **HIGH** — Material commercial risk; should be resolved within current quarter
- **MEDIUM** — Beneficial to formalise; manageable without resolution for near-term proposals
- **LOW** — Useful governance; not blocking any current activity

---

## Gap Summary

| Gap ID | Area | Criticality | Status | Owner |
|---|---|---|---|---|
| GAP-ERP-001 | COA Design Standard | CRITICAL | Open | Oracle BU Lead |
| GAP-ERP-002 | Legal Entity Configuration Guide | CRITICAL | Open | Oracle BU Lead |
| GAP-ERP-003 | Data Migration Templates (FBDI) | CRITICAL | Open | Delivery Lead / Data Migration Lead |
| GAP-ERP-004 | ERP Effort Rate Card | CRITICAL | Open | Oracle BU Lead / Delivery Lead |
| GAP-ERP-005 | Bank Format Specifications | HIGH | Open | BeBanking Lead / Delivery Lead |
| GAP-ERP-006 | ERP Testing Script Library | HIGH | Open | Delivery Lead |
| GAP-ERP-007 | Procurement Authority Matrix Template | HIGH | Open | Delivery Lead |
| GAP-ERP-008 | ERP Scope Boundary Guide (Companion) | HIGH | Open | Oracle BU Lead |
| GAP-ERP-009 | Multi-Entity / Intercompany Design Guide | MEDIUM | Open | Delivery Lead |
| GAP-ERP-010 | Fixed Asset Category Template | MEDIUM | Open | Delivery Lead |
| GAP-ERP-011 | SoD Role Design Standard | MEDIUM | Open | Security Lead |
| GAP-ERP-012 | COA Validation Rules Reference | MEDIUM | Open | Delivery Lead |
| GAP-ERP-013 | Oracle ERP Training Framework | LOW | Open | Delivery Lead |
| GAP-ERP-014 | Cutover Runbook Template | LOW | Open | Delivery Lead |
| GAP-ERP-015 | ERP Hypercare Scope Definition | LOW | Open | Oracle BU Lead |

---

## Detailed Gap Records

### GAP-ERP-001 — COA Design Standard
**Criticality:** CRITICAL  
**Description:** The Chart of Accounts is the single most important design deliverable in every Oracle ERP Financials implementation. `ERP-GL-002` and `ERP-GL-003` state that the client provides the COA design and that APPSolve configures from it. However, APPSolve has no standard COA design facilitation guide, no template for the COA workshop output, and no reference for what a "good" COA design looks like.  
**Impact of gap:** Without a COA design guide, COA workshop quality varies by consultant. Poor COA design (wrong segment count, inadequate value set design, missing cross-validation rules) is one of the most expensive post-go-live problems in ERP — it can require a full re-implementation to fix.  
**Resolution required:**
1. A COA design workshop facilitation guide (key questions, segment design considerations, value set design best practices)
2. A COA design template (Excel or similar) that the client completes during the workshop
3. A COA sign-off checklist (validation criteria before APPSolve begins ledger configuration)
**Owned by:** Oracle BU Lead + Delivery Lead  
**Required before:** Next Oracle Fusion Financials SOW

---

### GAP-ERP-002 — Legal Entity Configuration Guide
**Criticality:** CRITICAL  
**Description:** `ERP-GEN-008` requires that the legal entity structure is confirmed and stable before LE configuration commences. `ERP-DAT-007` requires tax registration data before LE and tax configuration. APPSolve has no standard LE information-gathering template or configuration guide.  
**Impact of gap:** Legal entity configuration errors propagate throughout the ERP implementation — incorrect LE structure affects intercompany, bank accounts, tax profiles, and GL ledger mapping. Errors discovered late are expensive to correct.  
**Resolution required:**
1. Legal entity information template (company legal name / registration number / tax registration / functional currency / address / applicable legislation)
2. LE-to-Ledger mapping guide
3. Tax profile setup guide for South African entities (VAT / PAYE / income tax)
**Owned by:** Delivery Lead  
**Required before:** Next Oracle Fusion Financials SOW

---

### GAP-ERP-003 — Data Migration Templates (FBDI)
**Criticality:** CRITICAL  
**Description:** `ERP-DAT-001` states APPSolve provides FBDI templates; `ERP-DAT-002` lists the standard migration objects. APPSolve does not have a standard set of pre-configured, client-ready FBDI templates with instruction tabs, data validation rules, and format guidance.  
**Impact of gap:** Without ready-made FBDI templates, each delivery consultant recreates templates from Oracle documentation — inconsistent, error-prone, and time-consuming. Data quality failures in migration are one of the top causes of go-live delays.  
**Resolution required:**
1. Pre-configured FBDI templates for each standard migration object: suppliers, customers, open AP invoices, open AR invoices, fixed assets, projects and budgets, open POs
2. Each template must include: mandatory field markers, value set reference lists, format examples, client instruction tab, validation formula column
3. FBDI loading guide (step-by-step instructions for loading each template in Oracle)
**Owned by:** Delivery Lead / Data Migration Lead  
**Required before:** Next Oracle ERP implementation with data migration scope (all implementations)

---

### GAP-ERP-004 — ERP Effort Rate Card
**Criticality:** CRITICAL  
**Description:** APPSolve has no standard effort rate card for Oracle Fusion ERP implementations. Bid managers estimate ERP effort using prior project actuals and judgement. This produces inconsistent pricing across proposals and makes it difficult to defend estimates under client scrutiny.  
**Impact of gap:** Under-priced ERP implementations reduce margin and over-extend delivery resources. Over-priced implementations lose the bid. Without a rate card, APPSolve cannot consistently price multi-entity, multi-module ERP proposals.  
**Resolution required:**
1. Effort rate card by module: Financials (GL, AP, AR, FA, CM) / Procurement / PPM — days per phase per module (Scope and Design, Configuration, Data Migration, CRP1, CRP2, UAT Support, Cutover, Hypercare)
2. Configuration complexity multipliers: single LE vs. multi-LE; standard COA vs. complex COA (6+ segments); standard workflows vs. complex hierarchies
3. Data migration effort model: base effort + per-object multiplier + data volume factor
4. Rate card must reflect South African delivery rates (on-site vs. remote)
**Owned by:** Oracle BU Lead / Delivery Lead  
**Required before:** Next Oracle ERP tender response or proposal

---

### GAP-ERP-005 — Bank Format Specifications
**Criticality:** HIGH  
**Description:** `ERP-AP-005` and `ERP-CM-002` reference bank-specific payment file formats and bank statement import formats. APPSolve does not have a documented library of South African bank format specifications (ABSA, FNB, Nedbank, Standard Bank, Investec) for EFT payment files and MT940 bank statement formats.  
**Impact of gap:** Each implementation team researches bank format specifications from scratch, contacting banks independently. Delays in bank format confirmation are a consistent cause of AP and CM configuration delays.  
**Resolution required:**
1. SA bank payment format reference: bank name / format name / format type (ISO 20022 pain.001 / proprietary) / Oracle CM configuration requirement
2. SA bank statement import format reference: bank name / format type (MT940 / camt.053 / proprietary) / Oracle CM import configuration
3. BeBanking H2H format reference (already partially in OIC pack — consolidate)
**Owned by:** BeBanking Lead / Delivery Lead  
**Required by:** Q3 2026

---

### GAP-ERP-006 — ERP Testing Script Library
**Criticality:** HIGH  
**Description:** APPSolve does not have a standard library of ERP testing scripts for CRP1, CRP2, and UAT. `ERP-TST-001` through `ERP-TST-006` describe the testing framework but APPSolve provides no standard scripts.  
**Impact of gap:** Client teams are asked to test without scripts, leading to shallow testing, missed defects in CRP, and post-go-live failures. APPSolve consultants create scripts per project, inconsistent across the practice.  
**Resolution required:**
1. CRP1 demonstration script (Design Validation walkthrough per module)
2. CRP2 end-to-end test scenarios (Procure-to-Pay / Order-to-Cash / Project-to-Invoice / Record-to-Report) with test data requirements
3. UAT test script template with pass/fail criteria and defect log linkage
**Owned by:** Delivery Lead  
**Required by:** Q3 2026

---

### GAP-ERP-007 — Procurement Authority Matrix Template
**Criticality:** HIGH  
**Description:** `ERP-PRO-003`, `ERP-WFL-001`, and `ERP-WFL-007` all require the client to provide an authority matrix before workflow configuration commences. APPSolve has no standard template for capturing procurement and financial approval authority.  
**Impact of gap:** Each project collects authority matrix information in an ad hoc format, leading to incomplete data collection and approval workflow configuration errors.  
**Resolution required:**
1. Standard authority matrix template: transaction type / approval dimension (amount / department / project) / approver level 1/2/3 (role and job title) / escalation / time-out action
2. Separate sheets for: Requisition Approval / PO Approval / Invoice Approval / Journal Approval / Capex Approval / Project Budget Approval
3. Guidance notes explaining Oracle AME capabilities and constraints
**Owned by:** Delivery Lead  
**Required by:** Q3 2026

---

### GAP-ERP-008 — ERP Scope Boundary Guide (Companion)
**Criticality:** HIGH  
**Description:** The OIC pack has `OIC_IMPLEMENTATION_PATTERNS.md` as its companion document. The ERP pack has `ERP_SCOPE_BOUNDARY_GUIDE.md` (created alongside this gap report) as its companion. However, the scope boundary guide needs to be validated and extended with actual project experience.  
**Impact of gap:** Without clear scope boundary examples, bid managers and project managers make inconsistent in/out scope decisions on ERP engagements.  
**Resolution required:** Validate `ERP_SCOPE_BOUNDARY_GUIDE.md` against the first two Oracle ERP SOWs issued; update with any additional boundary scenarios identified during delivery.  
**Owned by:** Oracle BU Lead  
**Required by:** Before issuing third Oracle ERP SOW

---

### GAP-ERP-009 — Multi-Entity / Intercompany Design Guide
**Criticality:** MEDIUM  
**Description:** `ERP-GL-006` addresses standard intercompany accounting but BU-ERP-002 (pending) asks whether complex intercompany scenarios are in scope. APPSolve has no guide for designing multi-entity Oracle ERP configurations.  
**Impact of gap:** Multi-entity implementations (2+ legal entities, intercompany transactions) are significantly more complex than single-entity. Without a design guide, multi-entity implementations are underscoped.  
**Resolution required:** Multi-entity design guide covering: LE-to-ledger relationships, intercompany balancing, intercompany reconciliation workflow, consolidation reporting approach.  
**Owned by:** Delivery Lead  
**Required by:** Q4 2026

---

### GAP-ERP-010 — Fixed Asset Category Template
**Criticality:** MEDIUM  
**Description:** `ERP-FA-001` requires the client to provide the asset category list with depreciation rules. APPSolve has no standard template for collecting this information.  
**Impact of gap:** Asset category data collected inconsistently; FA configuration requires rework when category data is incomplete.  
**Resolution required:** Fixed asset category template: category name / Oracle FA asset category / depreciation method / useful life (accounting) / useful life (tax book where applicable) / residual value percentage.  
**Owned by:** Delivery Lead  
**Required by:** Q3 2026

---

### GAP-ERP-011 — SoD Role Design Standard
**Criticality:** MEDIUM  
**Description:** `ERP-SEC-001` states APPSolve designs roles following Oracle SoD guidelines. APPSolve has no documented SoD role design standard defining which role combinations are prohibited and which Oracle role archetypes are SoD-safe.  
**Impact of gap:** SoD issues discovered during audit after go-live require expensive remediation. Without a design standard, SoD risks are not consistently identified during implementation.  
**Resolution required:** SoD role design reference: list of high-risk Oracle ERP duty role combinations; Oracle's recommended SoD matrix for Financials and Procurement; guidance on custom role design to avoid SoD conflicts.  
**Owned by:** Security Lead  
**Required by:** Q4 2026

---

### GAP-ERP-012 — COA Validation Rules Reference
**Criticality:** MEDIUM  
**Description:** Oracle Fusion GL cross-validation rules (CVRs) restrict which account code combinations are valid (e.g., Capital Expense account can only be coded to Capex cost centres). APPSolve has no standard guide for designing CVRs.  
**Impact of gap:** Missing CVRs allow invalid GL coding, producing financial reports with coding errors; too many CVRs break user productivity by blocking valid transactions.  
**Resolution required:** CVR design guide: when to use CVRs; how to structure CVR rules; examples of common South African financial reporting CVR patterns; CVR testing checklist.  
**Owned by:** Delivery Lead  
**Required by:** Q4 2026

---

### GAP-ERP-013 — Oracle ERP Training Framework
**Criticality:** LOW  
**Description:** `ERP-TRN-001` through `ERP-TRN-004` define the TTT training approach but APPSolve has no standard ERP training framework document defining training objectives, training material format, and success criteria per role.  
**Resolution required:** Standard ERP training framework: training objectives per user population; material format standards (quick reference cards, process walkthrough guides, system demo scripts); competency assessment criteria.  
**Owned by:** Delivery Lead  
**Required by:** Q4 2026

---

### GAP-ERP-014 — Cutover Runbook Template
**Criticality:** LOW  
**Description:** `ERP-CUT-002` states APPSolve produces a cutover runbook. No standard runbook template exists — each project creates one from scratch.  
**Resolution required:** Cutover runbook template covering: pre-cutover checklist / cutover day task list with owner and time estimate / go-live confirmation criteria / rollback decision criteria / war room communication plan.  
**Owned by:** Delivery Lead  
**Required by:** Q4 2026

---

### GAP-ERP-015 — ERP Hypercare Scope Definition
**Criticality:** LOW  
**Description:** `ERP-HYP-001` through `ERP-HYP-004` define the hypercare approach but APPSolve has no standard ERP hypercare scope definition document (what is and is not a hypercare defect; severity classification; response time targets; escalation path).  
**Resolution required:** ERP hypercare scope definition aligned to HCM Base hypercare assumptions; should be a Cross_BU document eventually (applicable to both HCM and ERP).  
**Owned by:** Oracle BU Lead  
**Required by:** Q4 2026

---

## Next Steps

**Before next Oracle ERP tender response:**
1. Resolve BU-ERP-001 through BU-ERP-008 (BU Lead decision list) — required to promote `ERP_ASSUMPTIONS_V1.md` to Approved
2. Resolve GAP-ERP-001 (COA Design Standard) — consult on next proposal without this
3. Resolve GAP-ERP-002 (LE Configuration Guide) — every ERP project needs LE information
4. Resolve GAP-ERP-003 (FBDI Templates) — blocking data migration on all implementations
5. Resolve GAP-ERP-004 (Effort Rate Card) — required for defensible ERP pricing

**Q3 2026:**
- GAP-ERP-005, GAP-ERP-006, GAP-ERP-007 — high-value delivery tools

**Q4 2026:**
- GAP-ERP-008 through GAP-ERP-015 — complete governance and design library

---

*ERP_GAP_REPORT v1.0 | WP11D — Oracle ERP Assumptions Pack | 2026-06-15*  
*15 gaps identified: 4 CRITICAL / 4 HIGH / 5 MEDIUM / 2 LOW*  
*Owner: Oracle BU Lead — review in conjunction with ERP Assumptions BU Lead approval process*
