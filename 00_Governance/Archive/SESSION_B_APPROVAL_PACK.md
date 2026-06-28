# Session B Approval Pack — Acumatica DIRECT Files
**Date:** 2026-06-10 | **Prepared by:** Claude (AI — requires human review by Hein Blignaut)
**Scope:** W1S2-002, W1S2-001, W1S2-003, W1S2-004, W1S2-005, W1S2-009
**Status:** Review analysis only — no content edited, no files promoted
**Related:** SESSION_B_STATUS_REPORT.md | EXTRACTION_WORKFLOW.md | AI_CONTEXT.md

---

## Executive Summary

Six of nine Acumatica DIRECT-rated files reviewed. All six are approvable — none require rejection. Two files have mandatory edits that must be applied before promotion (W1S2-003, W1S2-004). Two require minor edits (W1S2-001, W1S2-009). Two can go directly to Review_Required with reviewer notes only (W1S2-002, W1S2-005).

The most serious issue found is **LIFO costing in W1S2-003 Inventory Control**. LIFO is prohibited under IFRS/IAS 2, which applies to all South African entities. Citing it as a supported method in a live tender would be factually incorrect for SA clients. This must be addressed before promotion.

The second issue is a **cascade description error in W1S2-004 Manufacturing** — two rows in the capability table have each other's descriptions. The MRP standalone section also describes Project Accounting integration, not demand-driven planning. These errors would read as technically incompetent to a manufacturing client's ERP team.

All other issues are minor or editorial. The six files collectively cover the most commonly tendered Acumatica modules: Financials, Distribution, Inventory, Manufacturing, CRM, and Project Accounting. Approving them brings the total approved KB content from 18 to 24 files.

| File | Recommendation | Mandatory edits? | Estimated effort |
|---|---|---|---|
| W1S2-002 Distribution | **Approve with note** | No | 15 min |
| W1S2-001 Financials | **Approve with minor edit** | No (advisory) | 20 min |
| W1S2-003 Inventory | **Approve with mandatory edit** | Yes — LIFO | 25 min |
| W1S2-004 Manufacturing | **Approve with mandatory edits** | Yes — 3 description errors | 45 min |
| W1S2-005 CRM | **Approve with note** | No | 20 min |
| W1S2-009 Project Accounting | **Approve with verification** | No (flag only) | 40 min |

---

## File 1 — W1S2-002: Acumatica Distribution Edition

### 1. Summary of Content

Four-capability statement covering Distribution Edition fundamentals: Order Management (order-to-cash, drop shipments, backorders), Procurement and Purchase Order Management (automated purchasing, vendor management), Sales and Customer Management (CRM integration, 360° customer view), and Financial Management Integration. Six benefits stated. Source: Acumatica Proposal Template September 2025 — current active template.

### 2. Factual Risks

| Risk | Severity | Detail |
|---|---|---|
| Thin capability coverage | Low | Four capability rows describe Distribution at a broad level. A detailed module-specific tender may require additional content — warehouse management, shipping carriers, returns/RMA management are absent. This is a sourcing limitation, not an error. Flag for reviewer awareness only. |
| "360-degree visibility" | None | Marketing language — universally used in ERP vendor materials. Acceptable. |
| "Drop shipments and backorders" | None | Standard Acumatica Order Management features. Accurate. |

No US-centric terminology found. No client language found. No IFRS or accounting concerns. No AI-authored additions identified.

### 3. Recommended Edits

No edits required. Add a reviewer note: *"This file covers Distribution Edition at overview depth. For tenders requiring detailed warehouse or logistics capability, supplemental content from the historical corpus may be needed."*

### 4. Approval Recommendation

**Approve with note.** Move to `Review_Required/Acumatica/` — no content changes required. Reviewer note only.

### 5. Estimated Remediation Effort

15 minutes — metadata review, reviewer note addition, promotion.

---

## File 2 — W1S2-001: Acumatica Financial Management

### 1. Summary of Content

Ten-capability statement covering the full Acumatica Financials suite: General Ledger, Accounts Receivable, Accounts Payable, Cash Management, Currency Management, Tax Management, Deferred Revenue, Mobile Applications, Recurring Revenue Management, and Fixed Assets. Five benefit themes. Source: Acumatica Proposal Template September 2025 — current active template. Strongest content depth in the DIRECT set.

### 2. Factual Risks

| Risk | Severity | Detail |
|---|---|---|
| **ASC 606 cited alongside IFRS 15 in Deferred Revenue row** | Low | The Deferred Revenue capability row states: *"in compliance with ASC 606 and IFRS 15."* ASC 606 is the US GAAP revenue recognition standard. IFRS 15 is the international standard applicable in South Africa. Both standards are substantially converged (they were developed jointly), so the content is not factually wrong. However, leading with a US-specific standard in an SA tender is unnecessary and could suggest the template wasn't localised. Fix: reorder to "IFRS 15 (and ASC 606 international equivalent)" or simply "IFRS 15." |
| General Ledger "instant access" language | None | "Provides instant access to mission-critical financial data" — standard marketing language. Acceptable. |
| Recurring Revenue Management | None | This is a valid Acumatica module. Confirmed in current product documentation. Safe to cite. |
| Tax Management | None | "Centralised tax configuration" — generic ERP claim. No SA-specific tax claim made (e.g., no claim about SARS eFiling integration). Safe. |

No client language found. No AI-authored additions identified. No other US-centric issues beyond ASC 606.

### 3. Recommended Edits

Single-line edit in the Deferred Revenue table row: reorder standard references to lead with IFRS 15.

Before: *"...in compliance with ASC 606 and IFRS 15."*
After: *"...in compliance with IFRS 15 (ASC 606 equivalent)."*

### 4. Approval Recommendation

**Approve with minor edit.** Apply the one-line IFRS 15 reorder. Move to `Review_Required/Acumatica/`.

### 5. Estimated Remediation Effort

20 minutes — one-line edit, metadata update, promotion.

---

## File 3 — W1S2-003: Acumatica Inventory Control

### 1. Summary of Content

Seven-section capability statement: real-time visibility, inventory transactions (adjustments, transfers, kitting), lot/serial/expiry tracking, replenishment and stock management, costing methods, allocation and reservations, reporting. Source: Acumatica Proposal Template September 2025.

### 2. Factual Risks

| Risk | Severity | Detail |
|---|---|---|
| **LIFO costing method cited** | **High — mandatory fix** | The costing methods table lists: *"FIFO, LIFO, Weighted Average Cost, and Standard Costing."* **LIFO (Last In, First Out) is explicitly prohibited under IAS 2 — Inventories** (the IFRS standard governing inventory costing in South Africa). All SA entities that follow IFRS — including listed companies, state-owned entities, banks, and most large businesses — cannot use LIFO. Citing LIFO as a supported costing method in an SA tender could: (a) appear factually incorrect to a CFO or auditor reviewer; (b) suggest APPSolve has not localised its content for SA; (c) create compliance questions. **This row must be corrected before promotion.** See Recommended Edits. |
| Demand forecasting integration | Low | "Demand forecasting integration" is listed under Replenishment. Acumatica does provide demand forecasting as part of its Distribution and Manufacturing planning capabilities, but it may require a specific edition or planning module (not standard in all Acumatica tiers). Recommend replacing with the more conservative: "Integration with demand and supply planning tools." |
| "Multi-company" inventory | None | Standard Acumatica capability. Safe. |
| Lot/serial expiry management | None | Valid for FMCG, food, pharmaceutical clients. Accurate. |

No client language found. No AI-authored additions. No other US-centric or IFRS issues beyond LIFO.

### 3. Recommended Edits

**Mandatory:** In the costing methods table row, revise as follows:

Before: *"Supports FIFO, LIFO, Weighted Average Cost, and Standard Costing."*

After: *"Supports FIFO, Weighted Average Cost, and Standard Costing. LIFO is available in certain jurisdictions but is not permitted under IFRS/IAS 2 — not recommended for South African implementations."*

*Alternatively (simpler):* Remove LIFO entirely: *"Supports FIFO, Weighted Average Cost, and Standard Costing."*

The simpler removal is recommended — citing a prohibited method at all (even with a caveat) adds unnecessary complexity for SA tenders.

**Advisory:** Soften "Demand forecasting integration" to avoid an unsupported module claim.

### 4. Approval Recommendation

**Approve with mandatory edit.** File must not be promoted to Review_Required until the LIFO row is corrected. Once corrected, it is approvable.

### 5. Estimated Remediation Effort

25 minutes — mandatory LIFO row edit, advisory demand forecasting edit, metadata update, promotion.

---

## File 4 — W1S2-004: Acumatica Manufacturing Edition

### 1. Summary of Content

Comprehensive coverage of Acumatica Prime Manufacturing Edition: nine-row capability table (Manufacturing Platform), followed by five standalone sections (Manufacturing Foundation, Discrete Manufacturing, MRP, Estimating, ECC). Source: HyDac V5.1 December 2024 (won engagement). This is the only source for Manufacturing content in the entire KB — no Manufacturing sections exist in the Sept 2025 Acumatica template.

### 2. Factual Risks

Three errors found in the Manufacturing Platform capability table. Two are content-swap errors; one is a structural issue.

| Risk | Severity | Detail |
|---|---|---|
| **"Advanced Inventory" row has Estimating content** | **High — mandatory fix** | In the Manufacturing Platform table, the "Advanced Inventory" row reads: *"Create estimates for new or existing items and convert them into bills of materials, production orders, and/or other estimates."* This is the correct description of the **Estimating** module, not Advanced Inventory. Advanced Inventory in the Acumatica manufacturing context covers advanced warehouse management capabilities (directed put-away, pick and pack, barcode support). The Estimating content has been placed in the wrong row. |
| **"Estimating" row has ECC content** | **High — mandatory fix** | In the same table, the "Estimating" row reads: *"Automate, control, and organise all change requests, plans, and actual changes to a bill of materials. Full control from engineering change request through to engineering change notice with approvals throughout."* This is the correct description of **Engineering Change Control (ECC)** — confirmed by the standalone ECC section which says the same thing. The Estimating row contains ECC content. The correct Estimating description (create estimates, convert to production orders, cost rollup) appears correctly in the standalone Estimating section. |
| **MRP standalone section describes Project Accounting, not MRP** | **High — mandatory fix** | The MRP standalone section reads: *"Manufacture to a project and track all associated costs at the project task level. Compare actual costs to a user-established budget. Production orders can be tied directly as a task to a project or produced to stock."* This is project-tied manufacturing cost tracking — a feature of **Project Accounting integration** (cross-referenced in W1S2-009), not MRP. MRP is demand-driven production planning: calculating material and capacity requirements from demand signals (sales orders, forecasts). The MRP section in the table (*"Manufacture to a project..."*) is similarly incorrect. Correct MRP description appears in the bullet list later in the file (*"Demand-driven production planning; Automatic replenishment recommendations; Supply and demand balancing..."*) — that bullet list is correct. The standalone paragraph and the table row need replacing. |
| AI-augmented standalone sections | Medium | The five standalone sections (Foundation, Discrete, MRP, Estimating, ECC) appear expanded beyond the brief table entries in HyDac V5.1. The review notes confirm HyDac as the source for the table rows but the expanded bullet-point standalone sections were likely AI-authored. The content in Foundation and Discrete Manufacturing appears accurate. The ECC section is accurate. The MRP section is wrong (see above). |
| "APS" (Advanced Planning and Scheduling) | None | Valid Acumatica capability. Standard. |
| "WMS" (Warehouse Management System) | None | Valid Acumatica capability. Standard. |

No client language found. No US-centric terminology found. No IFRS issues.

### 3. Recommended Edits

**Mandatory Edit 1 — Correct the "Advanced Inventory" table row:**

Before: *"Create estimates for new or existing items and convert them into bills of materials, production orders, and/or other estimates."*

After: *"Advanced warehouse management within the manufacturing environment — directed put-away, pick and pack, barcode scanning, multi-bin support, and real-time visibility of materials across the shop floor."*

*(Note: If the correct "Advanced Inventory" description cannot be confirmed from the HyDac source, replace the row content with the briefer: "Advanced warehouse and materials management capabilities supporting manufacturing operations.")*

**Mandatory Edit 2 — Correct the "Estimating" table row:**

Before: *"Automate, control, and organise all change requests, plans, and actual changes to a bill of materials. Full control from engineering change request through to engineering change notice with approvals throughout."*

After: *"Create cost estimates for new or existing items from materials, labour, and overhead. Convert estimates directly to bills of materials, production orders, or sales quotes. Revision history and cost comparison maintained."*

*(The correct description is already in the standalone Estimating section — reuse it.)*

**Mandatory Edit 3 — Correct the MRP standalone section:**

Before (standalone paragraph): *"Manufacture to a project and track all associated costs at the project task level. Compare actual costs to a user-established budget. Production orders can be tied directly as a task to a project or produced to stock."*

After: *"Demand-driven production planning that calculates material and capacity requirements from sales orders, forecasts, and stock levels. Automatic replenishment recommendations across multiple planning horizons with supply and demand balancing. Exception-based planning alerts identify shortages and overages. Production orders can be tied to projects or produced to general stock."*

*(Retain the existing correct bullet list in the MRP section; replace only the opening paragraph.)*

### 4. Approval Recommendation

**Approve with mandatory edits.** Three description errors must be corrected before promotion. Once corrected, the file is the sole Manufacturing capability content in the KB and is high value for manufacturing tenders.

### 5. Estimated Remediation Effort

45 minutes — three targeted edits, review of surrounding context for consistency, metadata update, promotion.

---

## File 5 — W1S2-005: Acumatica CRM

### 1. Summary of Content

Eight-capability overview of Acumatica CRM: Contact/Account Management, Sales Pipeline, Quote Management, Case Management, Customer Portal, Marketing Activities, Outlook Integration, Dashboards. Key positioning: CRM is native and fully integrated (not an add-on). Source: HyDac V5.1 December 2024 (won). Review notes flag the content is at overview depth — HyDac's primary focus was Manufacturing, not CRM.

### 2. Factual Risks

| Risk | Severity | Detail |
|---|---|---|
| Overview depth | Low | Eight rows is adequate for most tender CRM sections. For a CRM-specific tender, additional product detail may be needed. Not an error — a sourcing depth limitation. |
| "Case Management integrated with the service module" | Low | This implies Field Services integration (W1S2-006 is a STRUCTURE ONLY gap). The claim is technically valid — Acumatica Case Management does integrate with Field Services — but it references a module APPSolve has no approved content for yet. Low risk in practice; field service integration is a general ERP feature. Keep. |
| Outlook Integration | None | Standard Acumatica feature. Valid. |
| Customer Portal | None | Valid Acumatica feature across current editions. |
| "Real-time pipeline data" | None | Marketing language. Accurate. |

No US-centric terminology found. No IFRS concerns. No client language. No AI-authored additions beyond standard product description.

### 3. Recommended Edits

No content edits required. Add a reviewer note: *"CRM content is at overview depth sourced from HyDac V5.1 (Manufacturing focus). For a CRM-centric tender, check the Sept 2025 Acumatica template for a more detailed CRM section, or source from a CRM-primary Acumatica proposal in the corpus."*

### 4. Approval Recommendation

**Approve with note.** No content changes required. Move to `Review_Required/Acumatica/` with reviewer note.

### 5. Estimated Remediation Effort

20 minutes — reviewer note addition, metadata update, promotion.

---

## File 6 — W1S2-009: Acumatica Project Accounting

### 1. Summary of Content

Nine-capability statement covering Acumatica Project Accounting: Project Budget Management, Time and Expense Tracking, Revenue Recognition, Billing Rules, WIP Accounting, Project Profitability Reporting, Change Order Management, Intercompany Projects, and Manufacturing Integration. Includes an Intercompany Accounting note (from HyDac scope). Source: HyDac V5.1 December 2024 overview table, expanded with AI-augmented detail.

### 2. Factual Risks

| Risk | Severity | Detail |
|---|---|---|
| **AI-augmented feature rows** | Medium | Review notes explicitly state the feature table was "augmented from product knowledge." Three rows are most likely AI-authored beyond direct extraction: (1) Change Order Management ("Track scope changes with budget impact, update project financials, maintain audit trail"); (2) Intercompany Projects ("Manage projects spanning multiple legal entities with intercompany billing and cost allocation"); (3) Manufacturing Integration ("Production orders tied directly to project tasks — manufacturing costs flow automatically to project cost tracking"). All three claims are accurate descriptions of Acumatica capabilities, but they were not extracted from the source document. Flag for human verification before BU lead sign-off. |
| Revenue recognition methods | None | "Percentage-complete, milestone, and completed-contract" — these are IFRS 15-compliant methods. Accurate. |
| WIP Accounting approach | None | "Capitalise project costs to WIP accounts and recognise revenue upon project completion or milestone events" — valid under IFRS. Accurate. |
| Billing Rules: "T&M, fixed-fee, cap, retainage, and billing limits" | Low | "Retainage" is a construction-specific billing term (contractor withholds a percentage until project completion). In the SA context, retainage billing is used but the term is more common in construction/engineering. In a general professional services tender, this row is fine. For construction-specific tenders, this reinforces the gap in W1S2-008. Keep. |
| Intercompany Accounting note | Low | The standalone Intercompany Accounting note at the end is from HyDac's scope. It is a capability of the Acumatica Advanced Financials module, not specifically Project Accounting. Low risk to leave it as a note. If a tender asks specifically about intercompany accounting, this note is useful. Consider adding a clarifying sentence: "Intercompany accounting is part of Acumatica's Advanced Financials module and integrates natively with project financials." |

No US-centric terminology found. No LIFO or IFRS issues. No client language found.

### 3. Recommended Edits

No mandatory edits. Two advisory items:

1. **Flag AI-augmented rows:** Add an internal review note to the file (before the BU lead reviews): *"Reviewer note: Change Order Management, Intercompany Projects, and Manufacturing Integration rows were AI-augmented beyond the source document. Please verify these three rows against current Acumatica product documentation or your own implementation experience before approving."*

2. **Intercompany Accounting clarification:** In the Intercompany Accounting note, add: *"Note: Intercompany Accounting is a capability of Acumatica Advanced Financials — it integrates natively with project cost tracking when both modules are in scope."*

### 4. Approval Recommendation

**Approve with verification.** No content must be changed before promotion to Review_Required. The three AI-augmented rows should be flagged for the BU lead reviewer's attention — they are likely accurate but were not directly extracted. The BU lead review is the verification step for these rows.

### 5. Estimated Remediation Effort

40 minutes — add AI-augmentation flag note, add Intercompany Accounting clarification, metadata update, promotion.

---

## Approval Matrix

| File | Title | Recommendation | Mandatory Edit | Minor Edit | Reviewer Note | Estimated Effort |
|---|---|---|---|---|---|---|
| W1S2-002 | Distribution | **Approve** | None | None | Coverage depth note | 15 min |
| W1S2-001 | Financials | **Approve** | None | IFRS 15 reorder (1 line) | None | 20 min |
| W1S2-003 | Inventory Control | **Approve after mandatory edit** | LIFO row — remove or caveat | Demand forecasting softening | None | 25 min |
| W1S2-004 | Manufacturing | **Approve after mandatory edits** | (1) Advanced Inventory row; (2) Estimating row; (3) MRP standalone paragraph | None | AI-augmented sections noted | 45 min |
| W1S2-005 | CRM | **Approve** | None | None | Depth note + corpus check | 20 min |
| W1S2-009 | Project Accounting | **Approve** | None | Intercompany note clarification | AI-augmented rows flagged | 40 min |
| **Total** | | **All 6 approvable** | | | | **~2 hr 40 min** |

**No file is recommended for rejection.** All six files contain accurate, current Acumatica product content. The issues found are targeted edits, not structural rewrites.

---

## Recommended Review Sequence

Sequence for maximum throughput — lowest-risk files first to create early momentum.

| Order | File | Why This Position |
|---|---|---|
| 1 | **W1S2-002 Distribution** | No edits. Fastest throughput. Sets the approval cadence. |
| 2 | **W1S2-005 CRM** | No edits. Note only. Complete second. |
| 3 | **W1S2-001 Financials** | One-line edit only. Highest coverage (10 capabilities). Core module for every Acumatica tender. |
| 4 | **W1S2-003 Inventory** | Mandatory LIFO edit but straightforward. Core module for Distribution and Manufacturing tenders. |
| 5 | **W1S2-009 Project Accounting** | Verification flag only. Core module for Professional Services tenders. |
| 6 | **W1S2-004 Manufacturing** | Three targeted edits; highest effort. Leave last — most technically specialised. |

---

## Fast-Track Approval Candidates

Two files can enter Review_Required immediately with no content changes:

**W1S2-002 Distribution** — Zero content edits. Update metadata, add reviewer note, promote.

**W1S2-005 CRM** — Zero content edits. Update metadata, add reviewer note, promote.

These two files can be in `Review_Required/` within 35 minutes of starting Session B Part 1 remediation.

The remaining four files require edits before promotion but none require significant rewrites. Total remediation time for all six files is approximately 2 hours 40 minutes.

---

## Approval Prerequisites (All Files)

Before any W1S2 file is presented to the BU lead for final approval:

- [ ] Acumatica Gold Partner status confirmed current (annual renewal)
- [ ] September 2025 Acumatica template confirmed as the current active template
- [ ] LIFO removed or IFRS-caveated in W1S2-003
- [ ] Three manufacturing table/section corrections applied in W1S2-004
- [ ] AI-augmentation flag added to W1S2-009 for reviewer awareness
- [ ] No client names (HyDac, other) remain in any file — confirmed by pre-promotion scan
- [ ] BU lead questions (SA payroll, Construction Edition, Field Services) batched for a separate short input session — these do not block Part 1

---

*This approval pack was produced from a read-only review of candidate files. No files have been edited. No files have been promoted. Remediation begins on explicit instruction from Hein Blignaut.*
