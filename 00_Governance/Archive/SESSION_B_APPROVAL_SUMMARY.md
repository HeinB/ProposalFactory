---
created: "2026-06-10"
created_by: "Claude (AI — Session B approval processing)"
approved_by: "Hein Blignaut"
approval_date: "2026-06-10"
---

# Session B Approval Summary
**Date:** 2026-06-10 | **Approved by:** Hein Blignaut | **Session:** Wave 1 Session B

---

## Files Approved

Six Acumatica module capability statements approved 2026-06-10 by Hein Blignaut and promoted from `07_Approved_Content/Review_Required/Acumatica/` to `07_Approved_Content/Approved/Acumatica/`.

| File | Capability Area | Rows | Corrections Applied |
|---|---|---|---|
| W1S2-001-ACU-Financials.md | Acumatica Financials | 10 | IFRS 15 set as primary standard; ASC 606 noted as secondary |
| W1S2-002-ACU-Distribution.md | Acumatica Distribution | 4 | None — content clean |
| W1S2-003-ACU-Inventory.md | Acumatica Inventory | 7 | LIFO removed (IFRS/IAS 2 prohibited in SA); demand forecasting claim removed (not a native feature) |
| W1S2-004-ACU-Manufacturing.md | Acumatica Manufacturing | 9 platform rows + 5 sections | Three cascade table errors corrected (Advanced Inventory had Estimating content; MRP had Project Accounting content; Estimating had ECC content) |
| W1S2-005-ACU-CRM.md | Acumatica CRM | 8 | None — content clean |
| W1S2-009-ACU-ProjectAccounting.md | Acumatica Project Accounting | 8 (6 extracted + 2 verified) | AI-augmented rows resolved by independent verification — see below |

---

## W1S2-009 AI Row Verification Detail

Three AI-augmented rows were independently verified against help.acumatica.com, community.acumatica.com, and openuni.acumatica.com before approval.

| Capability | Verification Outcome | Action |
|---|---|---|
| Change Order Management | **CONFIRMED** — Standard Project Accounting feature; requires Change Orders feature enabled via CS100000 (Enable/Disable Features); form PM308000 | Row retained with revised wording noting the enablement prerequisite |
| Intercompany Projects | **NOT CONFIRMED** — Acumatica Intercompany Accounting is a separate Financial Management module. "Intercompany Projects" (projects spanning entities with intercompany billing) is not a documented Project Accounting feature. | Row removed in full |
| Manufacturing Integration | **CONFIRMED** — Production orders using the PJ (Project) order type tie to project tasks; manufacturing costs flow via project-linked WIP account groups; requires both Manufacturing Edition and Project Accounting modules; Update Project setting must be enabled | Row retained with revised wording stating all prerequisites |

Final feature count for W1S2-009: **8 rows** (6 HyDac V5.1 extracted + 2 verified from official Acumatica documentation).

---

## Key Corrections Made Before Approval

| Correction | File | Reason |
|---|---|---|
| IFRS 15 set as primary revenue recognition standard | W1S2-001 | IFRS 15 is the mandatory SA standard; ASC 606 is the US equivalent — should not lead in an SA context |
| LIFO costing method removed | W1S2-003 | LIFO is prohibited under IFRS/IAS 2 in South Africa; citing LIFO as a supported method would be misleading in any SA tender |
| "Demand forecasting integration" removed from Replenishment row | W1S2-003 | Not a native Acumatica inventory feature — external integration only |
| Three Manufacturing Platform table cascade errors corrected | W1S2-004 | Advanced Inventory, MRP, and Estimating rows had wrong descriptions due to a copy-paste cascade error in the original DRAFT |
| Intercompany Projects row removed | W1S2-009 | Not a Project Accounting feature; Intercompany Accounting is a separate Financial Management module |
| Change Order Management wording updated | W1S2-009 | Row now accurately states the enablement prerequisite (CS100000) |
| Manufacturing Integration wording updated | W1S2-009 | Row now states all prerequisites: PJ order type, Update Project setting, dual-module dependency |

---

## Approved Content Totals by Business Unit

| Business Unit | Previously Approved | Newly Approved | Total Approved | Physical Location |
|---|---|---|---|---|
| Cross-BU | 9 | 0 | 9 | `Approved/Cross_BU/` |
| Acumatica | 1 | 6 | 7 | `Approved/Cross_BU/` (W1S1-004) + `Approved/Acumatica/` (W1S2) |
| BeBanking | 10 | 0 | 10 | `Approved/Cross_BU/` (W1S1-005) + `Approved/BeBanking/` (W1S3) |
| Oracle | 1 | 0 | 1 | `Approved/Cross_BU/` (W1S1-003) |
| **Total** | **18** | **6** | **24** | |

---

## Updated Repository Totals

| Stage | Previous | Change | New |
|---|---|---|---|
| Approved | 18 | +6 | **24** |
| Review_Required | 7 | −6 | **1** |
| Candidate (blocking) | 0 | 0 | **0** |
| Candidate (STRUCTURE ONLY — not yet reviewed) | 3 | 0 | **3** |

---

## Remaining Candidate Files

| File | Status | Reason |
|---|---|---|
| W1S2-006-ACU-FieldServices.md | Candidate (STRUCTURE ONLY) | No source content found in corpus; BU lead must decide whether to source from Acumatica partner portal or confirm this is not in scope |
| W1S2-007-ACU-Payroll.md | Candidate (STRUCTURE ONLY) | Acumatica Payroll is US-focused; SA compliance approach unconfirmed; BU lead decision required |
| W1S2-008-ACU-Construction.md | Candidate (STRUCTURE ONLY) | Acumatica Construction Edition availability for APPSolve SA clients unconfirmed; BU lead decision required |
| W1S3-005-BB-ForexPayments.md | **Review_Required** | Authored from Session C fact baseline; promoted 2026-06-10; Parliament FX Rates document is a future enhancement source only and does not block approval |

---

## Recommended Next Activity

**Immediate priority:** Approve W1S3-005 (BeBanking International and Forex Payments) — the only file currently in Review_Required. This completes the BeBanking H2H capability set and closes content gap H7.

The Parliament FX Rates document (`Parties/Customers/Parliament/APPSolve BeBanking Parliament FX Rates.docx`) is a useful future enrichment source for this file but does not block approval. W1S3-005 is complete as authored from the confirmed Session C fact baseline (BQ7, BQ11, BQ12).

**After W1S3-005 approval:**
1. Copy 24 approved files to KB destination folders (`06_Capabilities/`, `08_Methodologies/`, `09_Executive_Summaries/`) per EXTRACTION_LOG.csv destination paths
2. Initiate BEE certificate renewal — deadline 2026-07-31 (~51 days)
3. Wave 2 extractions — Oracle DBA Executive Summary (HIST-002), Oracle Fusion Capability Statement (TMPL-001)
4. BU lead decisions on W1S2-006, 007, 008 (STRUCTURE ONLY gate)

---

## Governance Updates Applied (2026-06-10)

The following governance documents were updated during Session B approval processing:

| Document | Changes |
|---|---|
| `07_Approved_Content/Approved/Acumatica/` | Directory created; 6 approved files written |
| `07_Approved_Content/Review_Required/Acumatica/` | 6 files deleted (after promotion to Approved) |
| `00_Governance/EXTRACTION_LOG.csv` | 6 rows updated: review_status → Approved, final_disposition → Approved, destination_path → Approved/Acumatica/ paths |
| `00_Governance/DOCUMENT_REGISTER.csv` | 6 new CAP rows appended (W1S2-001, 002, 003, 004, 005, 009) with full metadata |
| `HANDOVER.md` | Current Status updated; pipeline table updated (Approved 18→24, Review_Required 7→1) |
| `00_Governance/CURRENT_STATE.md` | Pipeline snapshot updated; Approved Content section updated; blockers updated |
| `00_Governance/KNOWLEDGE_BASE_STATUS.md` | Pipeline counts updated; By BU table updated; Acumatica coverage table updated; Session Progress Tracker updated |
| `AI_CONTEXT.md` | Acumatica Approved Content section added; BeBanking SAP rule corrected; W1S3-005 status corrected; Validated Fact Baseline banking partners and SAP rows corrected; Content Gap Awareness updated |
| `PROJECT.md` | Session B milestones added; Pipeline Status table updated; Wave 1 Summary table updated; SAP fact row corrected |
| `memory/project_context.md` | Pipeline status updated; frontmatter description updated; fact baseline rows updated |
| `memory/MEMORY.md` | Index description updated |
