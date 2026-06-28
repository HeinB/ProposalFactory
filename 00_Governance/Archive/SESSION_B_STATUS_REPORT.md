# Session B Status Report — Acumatica Module Library
**Date:** 2026-06-10 | **Prepared by:** Claude (AI — requires human review)
**Scope:** W1S2-001 through W1S2-009 (9 files)
**Status:** Part 1 remediation complete 2026-06-10 — 6 DIRECT files promoted to Review_Required; 3 STRUCTURE ONLY remain Candidate

> **Part 1 complete (2026-06-10):** W1S2-001, 002, 003, 004, 005, 009 remediated and promoted to `07_Approved_Content/Review_Required/Acumatica/`. Corrections applied: IFRS 15 primary in W1S2-001; LIFO and unconfirmed demand forecasting removed from W1S2-003; three Manufacturing Platform table rows corrected in W1S2-004; AI-augmented rows flagged in W1S2-009. Next step: BU lead approval of 6 Review_Required files.

---

## 1. Session B Scope

Session B reviews the Acumatica Module Library — nine capability statement DRAFTs covering the core Acumatica ERP module portfolio. These files are the only Acumatica-specific content in the extraction pipeline. Approving the 6 DIRECT-rated files unlocks the ability to respond to module-specific Acumatica tender requirements for the first time.

**Prerequisite context:** Session A approved W1S1-004 (Acumatica Partnership Statement) which covers the partner tier, industry footprint, and delivery credentials. Session B adds module-level product depth on top of that foundation.

---

## 2. Candidate File Inventory

| ID | Title | Source | Readiness | Status | Effort |
|---|---|---|---|---|---|
| W1S2-001 | Acumatica Financial Management | Sept 2025 Template | DIRECT | **Review_Required** | Complete |
| W1S2-002 | Acumatica Distribution Edition | Sept 2025 Template | DIRECT | **Review_Required** | Complete |
| W1S2-003 | Acumatica Inventory Control | Sept 2025 Template | DIRECT | **Review_Required** | Complete |
| W1S2-004 | Acumatica Manufacturing Edition | HyDac V5.1 (Dec 2024, won) | DIRECT | **Review_Required** | Complete |
| W1S2-005 | Acumatica CRM | HyDac V5.1 (Dec 2024, won) | DIRECT | **Review_Required** | Complete |
| W1S2-006 | Acumatica Field Services | None (content gap) | STRUCTURE ONLY | Candidate | Cannot progress — BU decision needed |
| W1S2-007 | Acumatica Payroll | None (content gap) | STRUCTURE ONLY | Candidate | Cannot progress — BU decision needed |
| W1S2-008 | Acumatica Construction Edition | None (content gap) | STRUCTURE ONLY | Candidate | Cannot progress — BU decision needed |
| W1S2-009 | Acumatica Project Accounting | HyDac V5.1 (Dec 2024, won) | DIRECT | **Review_Required** | Complete — AI row verification done 2026-06-10 |

**Source note:** W1S2-001, 002, 003 sourced from the September 2025 Acumatica proposal template (the most current Acumatica source in the corpus). W1S2-004, 005, 009 sourced from HyDac V5.1 (December 2024, won engagement) — the only source for Manufacturing and Project Accounting content.

---

## 3. DIRECT vs MODERNISE vs STRUCTURE ONLY

### DIRECT (6 files) — W1S2-001, 002, 003, 004, 005, 009

These files contain current Acumatica product content from 2024–2025 sources. The content is generic product marketing with no client-specific language found. DIRECT means: verify currency, check for any prohibited claims, remove any remaining client language, and promote. No significant rewrites required.

**Source vintage:** Sept 2025 template (W1S2-001, 002, 003) and HyDac V5.1 Dec 2024 won engagement (W1S2-004, 005, 009). Both sources are within 18 months — content is current for Acumatica's stable ERP modules.

### MODERNISE — None

No W1S2 files are rated MODERNISE. The 2024–2025 source vintage means no significant modernisation is needed for DIRECT-rated files.

### STRUCTURE ONLY (3 files) — W1S2-006, 007, 008

These files have no usable source content. They are placeholder structures that require authoring from scratch or a new corpus search before they can progress. They cannot move to Review_Required under any circumstances until content is written and sourced.

---

## 4. Known Factual Risks

Each risk is assessed by impact and action required. All apply to the DIRECT-rated files.

| Risk | File(s) | Severity | Action Required |
|---|---|---|---|
| **LIFO costing method** | W1S2-003 | **High** | LIFO is prohibited under IFRS (which SA follows). Citing LIFO as a supported costing method could be technically incorrect or misleading in SA tenders. Action: remove LIFO from the costing methods table, or add a bracket note: *(LIFO not applicable under IFRS — used in US jurisdictions only)*. |
| **MRP section contains Project Accounting content** | W1S2-004 | Medium | The MRP section description reads: "Manufacture to a project and track all associated costs at the project task level" — this is Project Accounting functionality, not MRP. The MRP section description appears to be crossed with the Project Accounting overview. Action: rewrite MRP description to focus on demand-driven production planning; move project-tied manufacturing cost note to W1S2-009 cross-reference. |
| **Estimating section mislabelled** | W1S2-004 | Medium | The "Estimating" capability in the Manufacturing Platform table is described using Engineering Change Control (ECC) language ("Automate, control, and organise all change requests, plans, and actual changes to a bill of materials..."). This appears to be the ECC description mistakenly placed in the Estimating row. Action: replace the Estimating table entry with the correct estimating description (create/convert estimates to production orders, cost rollup). |
| **AI-augmented feature table — RESOLVED 2026-06-10** | W1S2-009 | ~~Medium~~ Resolved | Independent verification against help.acumatica.com completed 2026-06-10. Change Order Management: CONFIRMED — row retained, wording revised to note feature must be enabled (CS100000). Manufacturing Integration: CONFIRMED with prerequisites — row retained, wording revised to specify PJ order type, Update Project setting, and dual-module dependency. Intercompany Projects: NOT CONFIRMED — row removed; Acumatica Intercompany Accounting is a separate Financial Management module. W1S2-009 now has 8 rows (6 extracted + 2 verified). Remaining reviewer decision: Intercompany Accounting section at end of file — standalone file or embedded note. |
| **ASC 606 reference** | W1S2-001 | Low | The Deferred Revenue row cites "ASC 606" alongside "IFRS 15." ASC 606 is the US GAAP standard; IFRS 15 is the international equivalent (used in SA). Both standards are substantially converged, so this is low risk — but citing a US-specific standard in an SA tender without the IFRS equivalent could raise questions. Action: reorder to lead with IFRS 15, note ASC 606 as an internationally recognised equivalent. |
| **CRM at overview depth only** | W1S2-005 | Low | Review notes confirm CRM was not the primary focus of the HyDac engagement. The feature table may not be comprehensive. Action: confirm with Acumatica BU lead whether this depth is sufficient for tender use, or source a more detailed CRM section from the Sept 2025 template if one exists. |

---

## 5. Missing Acumatica Information

Issues that require human/BU lead input before the relevant files can progress. These are not blockers for the 6 DIRECT files — they affect the 3 STRUCTURE ONLY files only.

| Gap | File | Question for Hein Blignaut |
|---|---|---|
| **SA payroll approach** | W1S2-007 | Acumatica Payroll is a US-market module. Does APPSolve position Acumatica Payroll in South African implementations? If not, what is the standard SA payroll integration approach (VIP, Sage, other)? |
| **Construction Edition availability** | W1S2-008 | Does APPSolve actively sell Acumatica Construction Edition? Has APPSolve implemented it for any SA client? If not, this gap is acceptable to leave unfilled. |
| **Field Services content** | W1S2-006 | Should Wave 2 include a corpus search for Acumatica Field Services proposals? Alternatively, is Field Services content available on the Acumatica partner portal? |
| **CRM depth** | W1S2-005 | Is the current CRM feature depth (8 rows) sufficient for typical Acumatica tender requirements, or do we need a more detailed capability section? |

---

## 6. Expected Review Effort

| File | Estimated Effort | Reason |
|---|---|---|
| W1S2-001 Financials | 20 min | Clean content; ASC 606 terminology tweak only |
| W1S2-002 Distribution | 15 min | Cleanest file; no issues found |
| W1S2-003 Inventory | 25 min | Clean content; LIFO removal/caveat required |
| W1S2-004 Manufacturing | 45 min | Two description errors to fix (MRP and Estimating rows) |
| W1S2-005 CRM | 20 min | Clean content; depth confirmation only |
| W1S2-009 Project Accounting | 40 min | Verify AI-augmented rows against Acumatica product |
| W1S2-006 Field Services | BU decision + authoring | Cannot estimate — gap fill required first |
| W1S2-007 Payroll | BU decision first | Cannot estimate — SA compliance approach required |
| W1S2-008 Construction | BU decision first | Cannot estimate — product availability confirmation required |
| **DIRECT files total** | **~2.5 hours** | Includes remediation + self-review + promotion to Review_Required |

---

## 7. Recommended Review Sequence

Sequence optimised for fastest approval of the highest-value files.

| Rank | File | Why First |
|---|---|---|
| 1 | **W1S2-002 Distribution** | Lowest risk; cleanest extraction; no edits anticipated; fast throughput |
| 2 | **W1S2-001 Financials** | Low risk; one terminology tweak; covers the most universally required ERP module |
| 3 | **W1S2-005 CRM** | Low risk; CRM section is expected in most Acumatica tenders |
| 4 | **W1S2-003 Inventory** | DIRECT but LIFO flag must be resolved; core module for Distribution/Manufacturing tenders |
| 5 | **W1S2-004 Manufacturing** | DIRECT but two description fixes; highest value for manufacturing tenders (sole source for this content) |
| 6 | **W1S2-009 Project Accounting** | DIRECT but AI-augmented rows require verification; important for Professional Services tenders |
| 7 | **W1S2-007 Payroll** | Requires BU lead decision on SA payroll approach before authoring |
| 8 | **W1S2-008 Construction** | Requires BU lead to confirm whether APPSolve sells this edition |
| 9 | **W1S2-006 Field Services** | Requires corpus search or partner portal content; lowest urgency |

**Session B can be split into two parts:**
- **Part 1 (2–2.5 hours):** Remediate and promote DIRECT files (W1S2-001, 002, 003, 004, 005, 009)
- **Part 2 (separate session):** Address the 3 STRUCTURE ONLY files after BU lead decisions

---

## 8. Fastest Path to Approval

**Minimum viable Session B** — approve the 6 DIRECT files without waiting for the 3 STRUCTURE ONLY decisions:

```
Step 1: Remediate W1S2-002 (no changes needed → move to Review_Required)
Step 2: Remediate W1S2-001 (ASC 606 → IFRS 15 lead → move to Review_Required)
Step 3: Remediate W1S2-005 (confirm depth → move to Review_Required)
Step 4: Remediate W1S2-003 (remove/caveat LIFO → move to Review_Required)
Step 5: Remediate W1S2-004 (fix MRP and Estimating descriptions → move to Review_Required)
Step 6: Remediate W1S2-009 (verify AI-augmented rows → move to Review_Required)
Step 7: Hein Blignaut reviews 6 files in Review_Required → approve → move to Approved/
Step 8: Register 6 files in DOCUMENT_REGISTER.csv
```

**Result:** 6 additional approved capability statements (Financials, Distribution, Inventory, Manufacturing, CRM, Project Accounting). Total approved KB content rises from 18 to 24.

**Remaining 3 files (W1S2-006, 007, 008):** Gate on BU lead decisions. They do not block Part 1.

---

## Pre-Review Checklist

Before the BU lead reviews any W1S2 file, confirm:

- [ ] Acumatica partner status remains Gold Partner (annual renewal check)
- [ ] Sept 2025 template is still the current Acumatica template version
- [ ] W1S2-003: LIFO caveat applied or row removed
- [ ] W1S2-004: MRP description corrected; Estimating row description corrected
- [ ] W1S2-009: AI-augmented feature rows verified against Acumatica product
- [ ] No client names (HyDac, other) remain in any file
- [ ] BU lead questions (SA payroll, Construction Edition, Field Services) batched for a separate 30-min input session

---

*This report is a pre-review analysis only. No content has been modified. No files have been promoted. Session B remediation begins on explicit instruction from Hein Blignaut.*
