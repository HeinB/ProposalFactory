---
source_document: "APPSolve_HyDac_Proposal_20241211_V5.1.docx"
source_path: "Parties/Customers/HyDac/RFP/Acumatica Implementation/1. Working/APPSolve_HyDac_Proposal_20241211_V5.1.docx"
extraction_date: "2026-06-08"
extracted_by: "Claude (AI extraction — requires human review)"
readiness: "DIRECT"
approved_for_reuse: "No"
business_unit: "Acumatica"
review_status: "Review_Required"
remediation_date: "2026-06-10"
remediated_by: "Claude (AI — Session B Part 1)"
reviewer: "Hein Blignaut (pending)"
---

> **REVIEW REQUIRED — Pending BU lead approval. Not approved for tender use.**
> Readiness: DIRECT | Reviewer: Hein Blignaut

---

# Acumatica Project Accounting

*Source: HyDac V5.1 (December 2024) — Project Accounting section in the Acumatica component overview table. This section is also referenced in the manufacturing modules for project-tied production orders.*

## Overview

Deliver project objectives on time and on budget with Acumatica's Project Accounting Suite. Handle complex billing rules and easily calculate project revenue based on key project-specific attributes. Keep better track of costs by correctly accounting for work in progress (WIP). Manage complex reporting requirements and include project costs in company-wide financial reports.

## Benefits

- **Project Cost Control:** Real-time visibility into budgeted vs. actual costs at project, task, and cost category level
- **Flexible Billing:** Support for time-and-materials, fixed-price, milestone, and percentage-complete billing
- **WIP Accounting:** Accurate work-in-progress accounting ensures financial reports reflect true project status
- **Integration:** Seamlessly integrates with financials, inventory, purchasing, and manufacturing
- **Project Profitability:** Detailed profitability analysis per project, enabling go/no-go decisions on future engagements

## Key Features and Capabilities

| Capability | Description | Source |
|---|---|---|
| Project Budget Management | Set project budgets by task, cost category, and account. Monitor variance between budget and actuals in real time. | HyDac V5.1 — extracted |
| Time and Expense Tracking | Employee time entries and expenses captured against specific projects, tasks, and activities. | HyDac V5.1 — extracted |
| Revenue Recognition | Multiple revenue recognition methods including percentage-complete, milestone, and completed-contract. | HyDac V5.1 — extracted |
| Billing Rules | Complex billing rules per project: T&M, fixed-fee, cap, retainage, and billing limits. | HyDac V5.1 — extracted |
| WIP Accounting | Capitalise project costs to WIP accounts and recognise revenue upon project completion or milestone events. | HyDac V5.1 — extracted |
| Project Profitability Reporting | Real-time project profitability dashboard comparing budgeted and actual revenue, costs, and margin. | HyDac V5.1 — extracted |
| Change Order Management | Track changes to project scope, revenue and cost budgets, and commitments — approved change orders update project financials and maintain a complete audit trail. Requires the Change Orders feature to be enabled in Acumatica (Enable/Disable Features, CS100000). | Verified — help.acumatica.com (Change Orders form PM308000); help.acumatica.com (Change Orders for Commitments); openuni.acumatica.com (Project Billing and Change Management 2025 R2) |
| Manufacturing Integration | Production orders created using the PJ (Project) order type are tied to project tasks, with manufacturing costs (materials, labour, and overhead) flowing to project cost tracking via project-linked WIP account groups. Requires both Manufacturing Edition and Project Accounting modules; the Update Project setting must be enabled on the production order. | Verified — help.acumatica.com (Extension of Project Inventory Tracking to Production Orders); community.acumatica.com (Project Manufacturing Setup); Cross-reference W1S2-004 Manufacturing |

## Intercompany Accounting Note

HyDac V5.1 also included Intercompany Accounting as a separately listed module. Key capabilities:

- Multi-entity transaction management
- Automated intercompany elimination entries
- Consolidated reporting across legal entities
- Intercompany accounts payable/receivable automation

> **Verification note (2026-06-10):** Independent verification confirmed that Acumatica Intercompany Accounting is a distinct Financial Management module — it is not part of Project Accounting. The "Intercompany Projects" capability row that appeared in the original AI-augmented table (suggesting projects spanning multiple legal entities with intercompany project billing) could not be confirmed in Acumatica Project Accounting documentation and has been removed. The four capabilities above describe the separate Intercompany Accounting module (documented at acumatica.com/cloud-erp-software/inter-company-accounting/).
>
> **Reviewer decision required:** Should the Intercompany Accounting capabilities above remain embedded in this Project Accounting file as a cross-reference, or be extracted to a standalone Intercompany Accounting KB entry (new file number)? Either is acceptable — the content itself is accurate for the separate module.

---

**Remediation notes (2026-06-10 — Session B Part 1):**
- **Source column added to features table:** The three AI-augmented rows (Change Order Management, Intercompany Projects, Manufacturing Integration) were flagged explicitly. The remaining six rows are directly extracted from HyDac V5.1.
- **No content changes applied** to any row descriptions in Part 1. The flagging was informational only.
- **Intercompany Accounting section:** Retained from DRAFT with reviewer decision note added (standalone file vs. embedded note).

**Verification notes (2026-06-10 — independent verification against help.acumatica.com):**

- **Change Order Management — CONFIRMED.** Verified against help.acumatica.com (Change Orders form PM308000; Change Orders for Commitments) and openuni.acumatica.com (Project Billing and Change Management course 2025 R2). Change Order Management is a standard Project Accounting feature — not Construction-exclusive. The feature must be enabled via Enable/Disable Features (CS100000). Row description revised to accurately reflect verified capabilities and the prerequisite. Source flag updated from AI-augmented to Verified.

- **Intercompany Projects — NOT CONFIRMED. Row removed.** Extensive search of help.acumatica.com, acumatica.com, and community.acumatica.com found no documentation for "Intercompany Projects" as a Project Accounting capability. Acumatica Intercompany Accounting is a separate Financial Management module covering inter-entity transactions, consolidated reporting, and automated eliminations — it is not a Project Accounting feature. The wording "Manage projects spanning multiple legal entities with intercompany billing and cost allocation" overstated a capability that is not documented in Project Accounting. Row removed in compliance with KB governance rule: AI-authored content must be verified or removed.

- **Manufacturing Integration — CONFIRMED with prerequisites.** Verified against help.acumatica.com (Extension of Project Inventory Tracking to Production Orders) and community.acumatica.com (Project Manufacturing Setup). The PJ (Project) production order type ties manufacturing WIP to project account groups. Manufacturing costs flow to project cost tracking when the Update Project setting is enabled. Requires both Manufacturing Edition and Project Accounting modules. Row description revised to state the prerequisites accurately. Source flag updated from AI-augmented to Verified.

**Final feature count: 8 rows** (was 9 — Intercompany Projects removed; 6 HyDac-extracted + 2 verified from official Acumatica documentation).
