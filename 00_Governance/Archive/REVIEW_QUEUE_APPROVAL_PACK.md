# Review Queue — Approval Preparation Pack
**Version:** 1.0 | **Prepared:** 2026-06-10 | **Prepared by:** Claude (AI — requires human review)
**Reviewer:** Hein Blignaut (BU Lead) | **Status:** Awaiting BU lead approval session

> **Purpose:** Pre-approval review document for the BU lead. Covers all 7 files currently in `07_Approved_Content/Review_Required/`. For each file: executive summary, remaining factual risks, reviewer decisions required, recommended approval outcome, and estimated review time. Followed by a consolidated approval matrix and recommended sequence.
>
> **READ-ONLY DOCUMENT.** Do not modify Review_Required files, promote files, or update governance artefacts based on this document alone. All promotions require explicit BU lead approval.

---

## Pipeline Summary — Review_Required Queue

| Stage | Count | Notes |
|---|---|---|
| **Approved** | 18 | W1S1-001–009; W1S3-001–004, 006–010 |
| **Review_Required — this pack** | **7** | W1S2-001, 002, 003, 004, 005, 009 (Acumatica); W1S3-005 (BeBanking) |
| **Candidate (STRUCTURE ONLY — blocked)** | 3 | W1S2-006, 007, 008 — BU decisions needed; not in this pack |
| **If all 7 approved** | **25** | New total approved |

---

## File-by-File Review

---

### W1S2-001 — Acumatica Financial Management

**Path:** `07_Approved_Content/Review_Required/Acumatica/W1S2-001-ACU-Financials.md`
**Source:** APPSolve Acumatica Proposal Template September 2025
**Readiness:** DIRECT | **Remediation date:** 2026-06-10

#### Executive Summary

- Core Acumatica Financial Management capability statement covering 10 modules: GL, AR, AP, Cash Management, Currency Management, Tax Management, Deferred Revenue, Mobile Applications, Recurring Revenue Management, Fixed Assets.
- Content extracted verbatim from the September 2025 Acumatica proposal template — the most current Acumatica source in the corpus.
- One remediation applied: Deferred Revenue row reworded to lead with IFRS 15 as the primary applicable standard in South Africa; ASC 606 (US GAAP equivalent) retained as a secondary reference. Original had ASC 606 listed first.
- Two spelling corrections: "centralized" → "centralised"; "optimize" → "optimise" (SA market alignment).
- No client-specific language. No remaining IFRS concerns. No US-centric product claims.

#### Remaining Factual Risks

| Risk | Severity | Notes |
|---|---|---|
| Content vintage | Low | September 2025 source is current. Standard ERP financials modules are stable — no expected material changes. |
| IFRS 15 wording | Low | Correction applied. Verify the revised wording reads correctly in context: *"…in compliance with IFRS 15 (the international revenue recognition standard, also aligned with its US GAAP equivalent ASC 606)."* |

#### Reviewer Decisions Required

None. All corrections have been applied. Reviewer confirms the corrected Deferred Revenue wording is acceptable for tender use.

#### Recommended Approval Outcome

**Approve.** No remaining risks. Corrections already applied. Confirm wording and approve.

#### Estimated Review Time

**10 minutes.** Read once, confirm IFRS 15 wording in Deferred Revenue row, approve.

---

### W1S2-002 — Acumatica Distribution Edition

**Path:** `07_Approved_Content/Review_Required/Acumatica/W1S2-002-ACU-Distribution.md`
**Source:** APPSolve Acumatica Proposal Template September 2025
**Readiness:** DIRECT | **Remediation date:** 2026-06-10

#### Executive Summary

- Acumatica Distribution Edition capability statement covering 4 high-level areas: Order Management, Procurement and Purchase Order Management, Sales and Customer Management, Financial Management Integration.
- Cleanest file in the queue. No corrections applied — content verified as clean product marketing with no client-specific language, no IFRS concerns, and no US-centric terminology.
- Content is at overview depth only. Four capability rows cover the distribution workflow at summary level.
- Suitable for general distribution-focused tenders. Detailed warehouse management, shipping carrier integration, and RMA processing capability will need supplemental content if a tender requires that depth.
- Source is September 2025 template — most current Acumatica source available.

#### Remaining Factual Risks

| Risk | Severity | Notes |
|---|---|---|
| Overview depth | Low | 4 capability rows cover distribution at summary level. Not a risk for approval — is a limitation to be aware of for use in detailed distribution tenders. |
| No warehouse detail | Low | No WMS-specific content (putaway rules, pick strategies, shipping carrier integration, RMA). Warehouse depth is covered separately in W1S2-004 Manufacturing (WMS row) and W1S2-003 Inventory. Not an accuracy risk — a coverage note. |

#### Reviewer Decisions Required

**One optional decision:** Confirm whether 4-row overview depth is sufficient for the typical Acumatica distribution tender, or whether supplemental warehouse/RMA content should be sourced before this file enters active use.

#### Recommended Approval Outcome

**Approve.** No factual risks. Cleanest file in the batch. Depth limitation noted but does not affect accuracy.

#### Estimated Review Time

**10 minutes.** Read once, confirm depth acceptable for anticipated tender use, approve.

---

### W1S2-003 — Acumatica Inventory Control

**Path:** `07_Approved_Content/Review_Required/Acumatica/W1S2-003-ACU-Inventory.md`
**Source:** APPSolve Acumatica Proposal Template September 2025
**Readiness:** DIRECT | **Remediation date:** 2026-06-10

#### Executive Summary

- Acumatica Inventory Control capability statement covering 7 modules: Real-Time Inventory Visibility, Inventory Transactions, Lot and Serial Number Tracking, Replenishment and Stock Management, Multiple Costing Methods, Inventory Allocation and Reservations, Inventory Reporting and Analytics.
- Two remediations applied. (1) LIFO removed from Multiple Costing Methods row — LIFO is prohibited under IFRS/IAS 2 in South Africa. Corrected to: *"Supports FIFO, Weighted Average Cost, and Standard Costing in compliance with IFRS/IAS 2."* (2) "Demand forecasting integration" removed from Replenishment row — Acumatica does not include a native demand forecasting module; this requires third-party integration.
- Remaining 3 costing methods (FIFO, WAC, Standard) are all valid under IAS 2.
- No client-specific language. No US-centric terminology. Content current as at September 2025.

#### Remaining Factual Risks

| Risk | Severity | Notes |
|---|---|---|
| Content vintage | Low | September 2025 source. Standard inventory module — stable. |
| Demand forecasting | Low | Removed from file. If a tender asks about demand forecasting, the response should note that third-party integration is available (not a native module). No risk in this file as currently written. |

#### Reviewer Decisions Required

None. Both corrections already applied. No open decisions.

#### Recommended Approval Outcome

**Approve.** All corrections applied. IFRS/IAS 2 compliance language in place. No remaining risks.

#### Estimated Review Time

**10 minutes.** Read once, confirm FIFO/WAC/Standard costing methods correct, confirm demand forecasting removal acceptable, approve.

---

### W1S2-004 — Acumatica Manufacturing Edition

**Path:** `07_Approved_Content/Review_Required/Acumatica/W1S2-004-ACU-Manufacturing.md`
**Source:** APPSolve HyDac Proposal V5.1 (December 2024 — won engagement)
**Readiness:** DIRECT | **Remediation date:** 2026-06-10

#### Executive Summary

- Acumatica Manufacturing Edition capability statement. **This is the only KB source for Acumatica Manufacturing content** — it is not present in the September 2025 template. HyDac V5.1 (won, December 2024) is the sole source.
- Three critical table row corrections applied to the Manufacturing Platform Core Components table. The original DRAFT contained a cascade content mismatch — three row descriptions had shifted one position out of alignment:
  - **Advanced Inventory row:** Had Estimating content. Corrected to: advanced warehouse and materials management for the manufacturing floor.
  - **MRP row:** Had Project Accounting content ("Manufacture to a project and track all associated costs..."). Corrected to: demand-driven production planning from the standalone MRP section.
  - **Estimating row:** Had ECC content. Corrected to: estimate creation/conversion from the standalone Estimating section.
- Standalone sections (Manufacturing Foundation, Discrete Manufacturing, MRP, Estimating, ECC) were correct in the DRAFT and are untouched.
- File contains 9 Manufacturing Platform rows plus 5 standalone sections. Rich and complete for Manufacturing tenders.

#### Remaining Factual Risks

| Risk | Severity | Notes |
|---|---|---|
| Corrected row accuracy | Medium | The three corrected table rows were written from the standalone sections of the same HyDac DRAFT — internal consistency is high. However, the reviewer should confirm the corrected descriptions accurately represent current Acumatica Manufacturing capabilities. |
| Single source | Low | HyDac V5.1 is the only source. If Acumatica has released significant Manufacturing module updates since December 2024, some capability descriptions may be behind the current product version. Stable core ERP modules are unlikely to have changed materially in 6 months. |
| ECC section depth | Low | Engineering Change Control (ECC) section lists 5 bullet points. This is the correct content for ECC — it was not changed. If a tender specifically focuses on ECC, confirm this depth is sufficient. |

#### Reviewer Decisions Required

| Decision | Question |
|---|---|
| **Verify corrected rows** | Confirm the three corrected table rows (Advanced Inventory, MRP, Estimating) accurately represent Acumatica Manufacturing capabilities. The descriptions were drawn from the standalone sections of the same source DRAFT and are internally consistent — but Hein Blignaut should confirm they are product-accurate before approval. |
| **Source vintage** | Confirm December 2024 (HyDac V5.1) is current enough for new Manufacturing tenders, or flag if a more recent Acumatica Manufacturing source should be located before this file is used. |

#### Recommended Approval Outcome

**Approve with minor edit** — pending confirmation of the three corrected rows. If Hein Blignaut reads the corrected rows and confirms they are product-accurate, this upgrades to Approve. No other open issues.

#### Estimated Review Time

**20–25 minutes.** Focus review on the Manufacturing Platform table (rows: Advanced Inventory, MRP, Estimating). Standalone sections do not need re-verification. Confirm corrected rows, then approve.

---

### W1S2-005 — Acumatica CRM

**Path:** `07_Approved_Content/Review_Required/Acumatica/W1S2-005-ACU-CRM.md`
**Source:** APPSolve HyDac Proposal V5.1 (December 2024 — won engagement)
**Readiness:** DIRECT | **Remediation date:** 2026-06-10

#### Executive Summary

- Acumatica CRM capability statement covering 8 modules: Contact and Account Management, Sales Pipeline Management, Quote Management, Case Management, Customer Portal, Marketing Activities, Outlook Integration, Dashboards and Reporting.
- No corrections applied. Content verified clean — no client-specific language, no IFRS concerns, no US-centric terminology.
- Key positioning: CRM is not an add-on in Acumatica — it is fully integrated. This is the core differentiator and is clearly stated in the Overview.
- Sourced from HyDac V5.1. CRM was not the primary focus of the HyDac engagement (manufacturing was) — this is reflected in the overview-level depth.
- Case Management row references integration with "the service module" — this is accurate (Acumatica CRM integrates with Field Services). Field Services content (W1S2-006) is currently STRUCTURE ONLY.

#### Remaining Factual Risks

| Risk | Severity | Notes |
|---|---|---|
| Overview depth | Low | 8 rows at summary level. Not an accuracy risk. For a CRM-primary tender, the September 2025 Acumatica template may have a more detailed CRM section — this has not been checked. |
| Field Services reference | Low | Case Management row references "service module." This is accurate — but W1S2-006 Field Services is currently unfilled. Not an error in this file; just a cross-reference to a content gap. |

#### Reviewer Decisions Required

| Decision | Question |
|---|---|
| **Depth confirmation** | Confirm whether the current 8-row overview is sufficient for typical Acumatica CRM tender requirements, or whether the September 2025 template should be checked for a deeper CRM section before this file is used in CRM-primary tenders. This decision affects file usage, not approval. |

#### Recommended Approval Outcome

**Approve.** No factual risks. Clean extraction. The depth limitation is a usage note, not an accuracy concern. Approve and note depth limitation for CRM-primary tenders.

#### Estimated Review Time

**10 minutes.** Read once, confirm overview depth acceptable, approve.

---

### W1S2-009 — Acumatica Project Accounting

**Path:** `07_Approved_Content/Review_Required/Acumatica/W1S2-009-ACU-ProjectAccounting.md`
**Source:** APPSolve HyDac Proposal V5.1 (December 2024 — won engagement)
**Readiness:** DIRECT | **Remediation date:** 2026-06-10

#### Executive Summary

- Acumatica Project Accounting capability statement covering **8 capability rows** (6 directly extracted from HyDac V5.1; 2 independently verified against Acumatica documentation).
- **6 rows extracted from HyDac V5.1:** Project Budget Management, Time and Expense Tracking, Revenue Recognition, Billing Rules, WIP Accounting, Project Profitability Reporting.
- **2 rows verified 2026-06-10 against help.acumatica.com:** Change Order Management (PM308000 confirmed — standard Project Accounting feature requiring feature enablement); Manufacturing Integration (PJ order type confirmed — requires Manufacturing Edition + Project Accounting; Update Project setting required).
- **1 row removed 2026-06-10:** Intercompany Projects — not a Project Accounting feature. Acumatica Intercompany Accounting is a separate Financial Management module. The AI-authored claim was unsupportable and has been deleted per KB governance rule.
- Intercompany Accounting section at end of file covers the separate Financial module — one reviewer decision remains on whether to keep it embedded here or extract to a standalone KB entry.

#### Remaining Factual Risks

| Risk | Severity | Notes |
|---|---|---|
| Change Order Management — feature enablement | Low | The row now states the Change Orders feature must be enabled (CS100000). Reviewers should confirm this prerequisite is acceptable to disclose in tender responses. For most tender contexts, this is normal — it is standard Acumatica configuration, not a paid add-on. |
| Manufacturing Integration — module prerequisite | Low | The row now states both Manufacturing Edition and Project Accounting are required, and the Update Project setting must be enabled. This is accurate. For tenders where a client has both modules, this is directly applicable. |
| Intercompany Accounting section | Low | The section describes a confirmed separate module (Acumatica Intercompany Accounting). Content accuracy is not the risk — placement is the only open decision. |

#### Reviewer Decisions Required

| Decision | Question |
|---|---|
| **Intercompany Accounting section** | Should the Intercompany Accounting section (4-bullet capabilities: multi-entity transactions, automated eliminations, consolidated reporting, IC AR/AP) remain embedded in this Project Accounting file as a cross-reference note, or be extracted to a new standalone Intercompany Accounting KB entry (new file number)? Either is acceptable — the content is accurate for the separate module. |

#### Recommended Approval Outcome

**Approve.** All AI-augmented rows have been resolved: two verified and updated; one removed. The remaining reviewer decision (Intercompany Accounting section placement) does not affect the accuracy or approvability of the file — it is a structural preference question that can be actioned at approval time or deferred.

#### Estimated Review Time

**10–15 minutes.** Read the 8 feature rows, confirm the two verified rows read correctly, make the Intercompany Accounting section call, approve.

---

### W1S3-005 — BeBanking International and Forex Payment Processing

**Path:** `07_Approved_Content/Review_Required/BeBanking/W1S3-005-BB-InternationalAndForexPayments.md`
**Source:** Session C Confirmed Fact Baseline (BQ7, BQ11, BQ12); partial SITA v1.06 (Automated Exchange Rates section)
**Readiness:** MODERNISE | **Remediation date:** 2026-06-10

#### Executive Summary

- BeBanking's International and Forex Payment Processing capability statement. 12-section structure authored from confirmed Session C facts. This is the most comprehensive BeBanking product file in the queue.
- **Six review findings already resolved by BU lead decisions:** (1) SWIFT indirect model confirmed and applied throughout; (2) Lesotho/Eswatini named bank integrations removed; (3) SAP retained as supported ERP — no module-level forex detail claimed; (4) Treasury use case replaced with AP-initiated international payments use case; (5) International reach wording standardised to "subject to capabilities and international reach of selected bank"; (6) Parliament FX document recorded as future enhancement only.
- BeBanking does not claim direct SWIFT network membership anywhere in this file. The indirect model (transmit to banking partners → partners execute SWIFT) is consistently applied.
- Confirmed bank integrations: ABSA, FNB, Nedbank SA, Nedbank Namibia, Standard Bank SA, Standard Bank Namibia, Investec (CMA); Citi Bank UK, Santander Chile (international).
- GDPR roadmap status is stated as: *"GDPR compliance is on the BeBanking product roadmap."*

#### Remaining Factual Risks

| Risk | Severity | Notes |
|---|---|---|
| GDPR roadmap status | Low | File states GDPR is "on the BeBanking product roadmap." Confirm this is still accurate as of today — if GDPR compliance has since been achieved or the roadmap item has been removed, the wording must change. |
| SAP row wording | Low | SAP row states: "Supported — no module-level or workflow-level forex detail stated." This is conservative and correct. Confirm this framing is acceptable for tender use — some procurement reviewers may expect more detail for a claimed integration. |
| Citi Bank and Santander citability | Low | Citi Bank (UK) and Santander (Chile) are named in the banking integration table. Confirm these integrations are confirmed, current, and publicly citable in tender responses (not confidential or lapsed). |
| Parliament FX document | Informational | Recorded as future enhancement source only. Does not affect current content accuracy. No action required for approval. |

#### Reviewer Decisions Required

| Decision | Question |
|---|---|
| **GDPR roadmap** | Is GDPR compliance still on the BeBanking product roadmap, or has the status changed? |
| **SAP row** | Is "Supported — no module-level or workflow-level forex detail stated" acceptable for tender use, or should this row be removed until BQ-WEB-04 is answered? |
| **Citi Bank UK / Santander Chile** | Confirm both integrations are current and citable in tender documents. |

#### Recommended Approval Outcome

**Approve.** All six identified risks were resolved by BU lead decisions before promotion. The remaining factual risks are low and require only confirmation (not content rewrites). The BU lead has been closely engaged throughout the authoring of this file — the content reflects decisions already made. If the three confirmation questions can be answered quickly (yes/yes/yes), approve immediately.

#### Estimated Review Time

**20–25 minutes.** The BU lead is already familiar with this file. Confirm the 3 open questions, do a structural read-through of the 12 sections, and approve.

---

## Consolidated Approval Matrix

| File | Readiness | Source | Corrections Applied | AI-Augmented Content | Open Decisions | Recommendation | Est. Time |
|---|---|---|---|---|---|---|---|
| W1S2-001 Financials | DIRECT | Sept 2025 | IFRS 15 reorder; US spellings | None | None | **Approve** | 10 min |
| W1S2-002 Distribution | DIRECT | Sept 2025 | None (clean) | None | Depth confirmation (optional) | **Approve** | 10 min |
| W1S2-003 Inventory | DIRECT | Sept 2025 | LIFO removed; demand forecasting removed | None | None | **Approve** | 10 min |
| W1S2-004 Manufacturing | DIRECT | HyDac Dec 2024 | 3 cascade row corrections | None | Verify 3 corrected rows; source vintage | **Approve with minor edit** | 20–25 min |
| W1S2-005 CRM | DIRECT | HyDac Dec 2024 | None (clean) | None | Depth confirmation (optional) | **Approve** | 10 min |
| W1S2-009 Project Accounting | DIRECT | HyDac Dec 2024 | Source column + flagging; AI row verification complete 2026-06-10 | 0 (verified/removed) | Intercompany Accounting section: standalone file vs. embedded note | **Approve** | 10–15 min |
| W1S3-005 Forex Payments | MODERNISE | Session C BQ7/BQ11/BQ12 | 6 BU lead decisions applied | None | GDPR status; SAP row; bank citability | **Approve** | 20–25 min |
| **Total** | | | | | | | **~105–115 min** |

---

## Recommended Approval Sequence

Sequence optimised for fastest momentum: clean files first, decision-heavy files last.

| Order | File | Rationale |
|---|---|---|
| 1 | **W1S2-002 Distribution** | Cleanest file. No corrections, no decisions. Confirms the review rhythm and sets the pace. |
| 2 | **W1S2-001 Financials** | One confirmed fix (IFRS 15). Core module — high tender reuse value. Quick win. |
| 3 | **W1S2-003 Inventory** | Two confirmed fixes (LIFO, demand forecasting). Core module. Quick win. |
| 4 | **W1S2-005 CRM** | No corrections. Optional depth decision. Fast throughput. |
| 5 | **W1S3-005 Forex Payments** | BU lead already engaged. Three confirmation questions — if all yes, approve immediately. Rewarding review before the heavier Acumatica files. |
| 6 | **W1S2-004 Manufacturing** | Verify 3 corrected rows. Requires focused reading of the Manufacturing Platform table. |
| 7 | **W1S2-009 Project Accounting** | Most decisions in the queue. Verify or remove 3 AI rows. Intercompany structure decision. Allocate the most time here. |

---

## Files Approvable Immediately (No Product Verification Required)

These four files have no open verification tasks. Reviewer reads, confirms, approves.

| File | What to Confirm |
|---|---|
| W1S2-001 Financials | IFRS 15 wording in Deferred Revenue row reads correctly. |
| W1S2-002 Distribution | Overview depth acceptable for anticipated tender use. |
| W1S2-003 Inventory | FIFO/WAC/Standard costing methods correct. Demand forecasting removal acceptable. |
| W1S2-005 CRM | Overview depth acceptable for anticipated tender use. |

**Approving these four files takes ~40 minutes and raises the approved total from 18 to 22.**

---

## Files Requiring Discussion or Verification

| File | What Must Happen First |
|---|---|
| **W1S2-004 Manufacturing** | Hein Blignaut reads the three corrected table rows (Advanced Inventory, MRP, Estimating) and confirms they are product-accurate. No external lookup required — this is a knowledge confirmation. |
| **W1S2-009 Project Accounting** | One decision: Intercompany Accounting section at end of file — stays embedded in this file or extracted to a new standalone KB entry. AI row verification is complete; this is the only remaining call. |
| **W1S3-005 Forex Payments** | Confirm: GDPR roadmap status current; SAP row acceptable for tender; Citi Bank UK and Santander Chile integrations citable. All three are confirmation questions, not rewrites. |

---

## Total Expected Approval Effort

*Note: W1S2-009 AI row verification completed 2026-06-10 — effort estimate reduced from 25–30 min to 10–15 min.*

| Scenario | Effort | Files Approved | Total Approved KB |
|---|---|---|---|
| Quick wins only (W1S2-001, 002, 003, 005) | ~40 min | 4 | 22 |
| Add W1S3-005 (3 confirmation questions answered) | ~60–65 min | 5 | 23 |
| Full batch — all 7 files | ~85–95 min | 7 | 25 |

**Recommended:** Run the full batch in a single review session. Approving all 7 in one sitting takes under 90 minutes (down from the original 105–115 min estimate, since W1S2-009 AI rows are now pre-resolved) and brings the approved total to 25, unlocking the complete Acumatica module library (6 modules) and BeBanking international payments for tender use.

---

## Post-Approval Actions (Not Part of This Pack)

Once all 7 files are approved, the following actions are required to complete the pipeline. These are noted here for planning purposes only — do not action until files are approved.

1. For each approved file: update `approved_for_reuse` to `Yes` in the file header.
2. Move each file from `07_Approved_Content/Review_Required/` to `07_Approved_Content/Approved/` in the appropriate BU subfolder.
3. Update `00_Governance/EXTRACTION_LOG.csv` — set `review_status` to `Approved` and `approved_for_reuse` to `Yes` for all 7 rows.
4. Register all 7 files in `DOCUMENT_REGISTER.csv`.
5. Update `HANDOVER.md`, `00_Governance/KNOWLEDGE_BASE_STATUS.md`, and `00_Governance/CURRENT_STATE.md` to reflect 25 approved files.
6. Copy approved files to their KB destination folders (`06_Capabilities/`, `08_Methodologies/`, `09_Executive_Summaries/`) per `EXTRACTION_LOG.csv` destination paths.

---

*This document is read-only. Created by Claude (AI) 2026-06-10 as a pre-approval review aid for Hein Blignaut. All approval decisions must be made by the BU lead.*
