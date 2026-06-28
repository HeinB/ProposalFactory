---
title: Governance Baseline Correction Report
version: v1.0
status: Complete
programme: WP14A — Governance Baseline Correction Pass
date: 2026-06-16
preceded_by: WP14 — Governance Decision Resolution Audit
---

# Governance Baseline Correction Report

**Programme:** WP14A | **Date:** 2026-06-16 | **Preceded by:** WP14 Governance Audit

> **Scope:** Correction of governance artefacts and metadata only. No BU decisions were resolved. No assumption wording was changed. No assumptions were added or removed. No packs were promoted or demoted. All corrections address governance inconsistencies identified in WP14 Findings F-01 through F-09.

---

## 1. Authoritative Assumption Inventory

The following table reflects the corrected authoritative state of the APPSolve Tender Knowledge Base assumption library as at 2026-06-16.

| Pack | Document | Status | Assumptions | BU Decisions Pending |
|---|---|---|---|---|
| Oracle HCM Base | `HCM/HCM_BASE_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-15** | 114 | 0 |
| Oracle HCM Recruiting | `HCM/HCM_RECRUITING_ASSUMPTIONS_V1.md` | Draft — Pending BU Lead Approval | 52 | 7 |
| Oracle HCM Learning | `HCM/HCM_LEARNING_ASSUMPTIONS_V1.md` | Draft — Pending BU Lead Approval | 43 | 5 |
| Oracle HCM Talent Management | `HCM/HCM_TALENT_ASSUMPTIONS_V1.md` | Draft — Pending BU Lead Approval | 38 | 4 |
| Oracle HCM Workforce Compensation | `HCM/HCM_COMPENSATION_ASSUMPTIONS_V1.md` | Draft — Pending BU Lead Approval | 40 | 5 |
| Oracle OIC Integration | `OIC/OIC_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-15** | 101 | 0 |
| Oracle ERP | `ERP/ERP_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-15** | 128 | 0 |
| Oracle OCI Infrastructure | `OCI/OCI_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-16** | **174** | 0 |
| Acumatica Base | `Acumatica/ACU_BASE_ASSUMPTIONS_V1.md` | Draft — Pending BU Lead Approval | 152 | 14 |
| BeBanking Base | `BeBanking/BEBANKING_BASE_ASSUMPTIONS_V1.md` | Draft — Pending BU Lead Approval | 122 | 10 |
| Managed Services / AMS | `AMS/AMS_ASSUMPTIONS_V1.md` | **Approved v1.0 — 2026-06-15** | 96 | 0 |
| **Totals** | **11 documents** | **5 Approved / 6 Draft** | **1,060** | **45** |

**Approved assumption total:** 114 + 101 + 128 + 174 + 96 = **613**
**Draft/pending total:** 52 + 43 + 38 + 40 + 152 + 122 = **447**

---

## 2. Findings Resolved

### F-01 — OCI Assumption Count Discrepancy (CRITICAL)

**Finding:** Pack frontmatter (`assumption_count`), pack header, and pack footer all stated 164 assumptions. Independent verification via grep of pack body and assumption register both confirmed 174. A manual section-by-section count across all 19 sections (GEN through EXT) confirmed 174.

**Root cause:** Frontmatter was set to 164 during initial WP11H drafting. Pack body was expanded by 10 assumptions during WP11H-A decision application. Frontmatter, header, and footer were not updated at the time.

**Corrections applied:**
| File | Change |
|---|---|
| `OCI/OCI_ASSUMPTIONS_V1.md` frontmatter | `assumption_count: 164` → `assumption_count: 174` |
| `OCI/OCI_ASSUMPTIONS_V1.md` pack header | `**Assumptions:** 164` → `**Assumptions:** 174` |
| `OCI/OCI_ASSUMPTIONS_V1.md` pack footer | `164 assumptions` → `174 assumptions` |

**Evidence:** `OCI_COUNT_RECONCILIATION.md` — complete section-by-section breakdown with highest assumption ID per section.

**Status: RESOLVED**

---

### F-02 — GOVERNANCE_DASHBOARD Pack Count Wrong (HIGH)

**Finding:** Dashboard stated "Packs at Approved v1.0 = 4" and "Total assumption packs in library = 10". Both figures were incorrect.

**Corrections applied:**
| Field | Was | Now |
|---|---|---|
| Total assumption documents in library | 10 | 11 |
| Packs at Approved v1.0 | 4 | 5 |
| Programme readiness | 14% (4 of 10) | 45% (5 of 11) |
| Pack coverage (Governance Scorecard) | 10/10 | 11/11 |
| Approved packs (Governance Scorecard) | 4/10 (40%) | 5/11 (45%) |

**Status: RESOLVED**

---

### F-03 — GOVERNANCE_DASHBOARD Oracle ERP Row Absent (HIGH)

**Finding:** Oracle ERP pack (128 assumptions, Approved v1.0 2026-06-15) was entirely absent from the Pack Approval Status table in GOVERNANCE_DASHBOARD.md. This caused the "4 approved" count (instead of 5) and an inaccurate Executive Reporting Table.

**Corrections applied:**
- ERP row added to Pack Approval Status table: `Oracle ERP | ERP | 128 | Approved v1.0 | 0 | 0 of 0 | Complete`
- Executive Reporting Table: `Packs fully approved | 4 (OCI, OIC, AMS, HCM Base)` → `5 (HCM Base, OIC, ERP, AMS, OCI)`
- `Total assumptions available for tender use | 603` → `613`
- Governance Scorecard note updated to include ERP

**Status: RESOLVED**

---

### F-04 — GOVERNANCE_DASHBOARD Pack Assumption Counts Wrong (HIGH)

**Finding:** Seven packs had incorrect assumption counts in the dashboard. OCI count (F-01) propagated here as well.

| Pack | Was | Correct |
|---|---|---|
| Oracle HCM Base | 141 | **114** |
| Oracle HCM Recruiting | 57 | **52** |
| Oracle HCM Learning | 48 | **43** |
| Oracle HCM Talent | 43 | **38** |
| Oracle HCM Comp | 52 | **40** |
| Oracle OIC | 112 | **101** |
| Oracle AMS | 105 | **96** |
| Oracle OCI | 164 | **174** |
| Total | 1,050 | **1,060** |

**Corrections applied:** All pack rows in Pack Approval Status table corrected to authoritative counts from individual pack frontmatter. Totals row corrected to 1,060.

**Note on OCI "14 of 14" decisions done:** The original OCI row showed `0 BU Decisions | 14 of 14 Decisions Done`. This was internally inconsistent (0 decisions cannot have 14 done). The correct position is 0 BU decisions, 0 of 0 done (all decisions were resolved before pack approval; the pack has no outstanding decisions). Corrected to `0 | 0 of 0 | Complete`.

**Status: RESOLVED**

---

### F-05 — TENDER_ASSUMPTION_ASSEMBLY_RULES ERP Status Stale (MEDIUM)

**Finding:** BOM table Section 3.1 showed `ERP [Draft]` for BOM lines B86481, B86482, B86483. Oracle ERP was approved on 2026-06-15 (WP11D-A). The ASSEMBLY_RULES document was not updated at approval time.

**Corrections applied:** `ERP [Draft]` → `ERP [Approved]` in all three BOM table rows.

**Status: RESOLVED**

---

### F-06 — TENDER_ASSUMPTION_ASSEMBLY_RULES OCI Status Stale (MEDIUM)

**Finding:** BOM table Section 3.1 showed `OCI [Draft]` for the Oracle Analytics Cloud row. OCI was approved on 2026-06-16 (WP11H-A). ASSEMBLY_RULES was not updated at approval time.

**Corrections applied:** `OCI [Draft]` → `OCI [Approved]` in the OAC BOM row.

**Status: RESOLVED**

---

### F-07 — TENDER_ASSUMPTION_ASSEMBLY_RULES BeBanking "FUTURE" Label (LOW)

**Finding:** Section 3.4 BeBanking Assembly patterns referenced `BeBanking Pack (FUTURE)` and `OIC Pack (FUTURE)`. BeBanking Base Pack was created in WP11J (2026-06-16) and is Draft (not FUTURE). OIC is Approved (not FUTURE).

**Corrections applied:**
- `BeBanking Pack (FUTURE)` → `BeBanking Pack (Draft — Pending BU Lead Approval — 2026-06-16)` (all instances)
- `OIC Pack (FUTURE)` → `OIC Pack (Approved — 2026-06-15)`
- Section 3.4 heading: `V1 Library — packs not yet created` → `V1 Library — Draft pending BU Lead Approval`

**Status: RESOLVED**

---

### F-08 — ASSUMPTION_LIBRARY_ROADMAP Count and Totals (MEDIUM)

**Finding:** ROADMAP intro stated "ten documents". OCI count shown as 164. Programme totals propagated the incorrect 164 figure.

**Corrections applied:**
| Location | Was | Now |
|---|---|---|
| Intro paragraph | "ten documents" | "eleven documents" |
| Current State table OCI row | 164 | 174 |
| Programme totals line | 1,050 / 603 / OCI 164 | 1,060 / 613 / OCI 174 |
| Roadmap Summary OCI row | "164 assumptions" | "174 assumptions" |
| OCI Infrastructure Pack section table — `OCI_ASSUMPTIONS_V1.md` | "164 assumptions" | "174 assumptions" |
| OCI Infrastructure Pack section table — `OCI_ASSUMPTION_REGISTER.csv` | "164 rows" | "174 rows" |
| Pack 9 narrative `File:` | `BEBANKING_ASSUMPTIONS_V1.md` | `BEBANKING_BASE_ASSUMPTIONS_V1.md` |
| Footer | v1.5 | v1.6 |

**Status: RESOLVED**

---

### F-09 — HANDOVER Propagated Errors (MEDIUM)

**Finding:** HANDOVER.md propagated OCI count of 164 in four separate locations and reflected outdated programme totals.

**Corrections applied:**
| Location | Was | Now |
|---|---|---|
| Quick Facts — Approved assumption packs | `OCI 164 = 603 approved` | `OCI 174 = 613 approved` |
| System Maturity — WP11 row | "10 packs total; 5 APPROVED; 5 DRAFT pending 31 BU decisions" | "11 documents total; 5 APPROVED; 6 DRAFT pending 45 BU decisions" |
| System Maturity — WP11H row | "164 assumptions" | "174 assumptions (count corrected WP14A)" |
| Assumption Library table OCI row | 164 | 174 |
| Architecture Decisions OCI entry | "164 assumptions" | "174 assumptions" |
| Document Register ROADMAP | v1.5 / "10 packs" | v1.6 / "11 documents" |
| Document Register ASSEMBLY_RULES | v1.5 / "1,050 / 603" | v1.6 / "1,060 / 613" |
| Document Register OCI pack | "164 assumptions" | "174 assumptions" |
| Document Register DASHBOARD | "4 packs approved" | "5 packs approved / 11 documents" |
| Header update note | WP13 | WP14A |
| Footer | v2.5 | v2.6 |

**Status: RESOLVED**

---

## 3. Recalculated Programme Totals

| Metric | Previous (Incorrect) | Corrected |
|---|---|---|
| OCI assumption count | 164 | **174** |
| Total registered assumptions | 1,050 | **1,060** |
| Total approved assumptions | 603 | **613** |
| Total draft/pending assumptions | 447 | **447** (no change) |
| Approved packs | 4 (ERP omitted in dashboard) | **5** |
| Draft packs | 6 (already correct) | **6** |
| Total documents in library | 10 (some documents) / 11 (authoritative) | **11** |
| Total BU decisions outstanding | 45 (already correct in Master Register) | **45** |

**Arithmetic verification:**
- Approved: 114 + 101 + 128 + 96 + 174 = **613** ✓
- Draft: 52 + 43 + 38 + 40 + 152 + 122 = **447** ✓
- Total: 613 + 447 = **1,060** ✓

---

## 4. Files Modified

| File | Changes | Version |
|---|---|---|
| `08_Commercial/Assumptions/OCI/OCI_ASSUMPTIONS_V1.md` | 3 count corrections (frontmatter, header, footer) | No version bump (content unchanged) |
| `08_Commercial/Assumptions/OCI/OCI_COUNT_RECONCILIATION.md` | **CREATED** — F-01 audit evidence document | v1.0 (new) |
| `08_Commercial/Assumptions/Governance/GOVERNANCE_DASHBOARD.md` | 11 corrections across 5 sections | v1.0 → v1.1 |
| `08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md` | ERP status (3 rows), OCI status (1 row), BeBanking FUTURE (2 instances), Section 9 counts and totals | v1.5 → v1.6 |
| `08_Commercial/ASSUMPTION_LIBRARY_ROADMAP.md` | Intro count, OCI row, totals, Roadmap Summary, OCI section (2 lines), Pack 9 filename | v1.5 → v1.6 |
| `HANDOVER.md` | 10 corrections across Quick Facts, System Maturity, Assumption Library, Architecture Decisions, Document Register | v2.5 → v2.6 |
| `08_Commercial/Assumptions/Governance/GOVERNANCE_BASELINE_CORRECTION_REPORT.md` | **CREATED** — this document | v1.0 (new) |

**Files NOT modified (verified correct or out of scope):**
| File | Reason |
|---|---|
| `OCI/OCI_ASSUMPTION_REGISTER.csv` | Register was already correct at 174 rows — no change needed |
| `GOVERNANCE_MASTER_DECISION_REGISTER.md` | Verified CLEAN in WP14 — 45 decisions, 0 OCI decisions |
| `GOVERNANCE_APPROVAL_ROADMAP.md` | Verified CLEAN in WP14 |
| `GOVERNANCE_RISK_REGISTER.md` | Verified CLEAN in WP14 |
| `GOVERNANCE_WORKSHOP_PLAN.md` | Not in scope for count corrections |
| `GOVERNANCE_DECISION_RECORD_TEMPLATE.md` | Not in scope for count corrections |
| Individual assumption pack files (HCM, OIC, ERP, AMS, ACU, BB) | Counts in frontmatter already match actual counts — verified correct |

---

## 5. Constraints Observed

The following rules were observed throughout WP14A without exception:

- No BU decisions resolved
- No assumption wording changed
- No assumptions added
- No assumptions removed
- No pack promoted or demoted
- No approval status altered
- `approved_for_reuse` flag not modified
- All corrections limited to governance artefacts and metadata

---

## 6. Governance Baseline Certified

All findings identified in the WP14 Governance Decision Resolution Audit (F-01 through F-09) have been resolved. The authoritative programme state is now consistent across all governance artefacts:

- **OCI Infrastructure Pack: 174 assumptions** — confirmed by pack body, register (both 174 rows), and manual section-by-section count
- **Total registered: 1,060** — consistent across HANDOVER, ROADMAP, ASSEMBLY_RULES, DASHBOARD
- **Total approved: 613** — consistent across HANDOVER, ROADMAP, ASSEMBLY_RULES, DASHBOARD
- **Total draft/pending: 447** — unchanged, consistent
- **Approved packs: 5** (HCM Base, OIC, ERP, AMS, OCI) — consistent across all governance documents
- **Draft packs: 6** (REC, LRN, TLT, COM, ACU, BB) — consistent across all governance documents
- **Total documents: 11** — consistent across ROADMAP, DASHBOARD, HANDOVER

**No further reconciliation is required at this time.**

---

**Governance Baseline Certified**

*All nine WP14 findings resolved. Programme totals consistent. Single source of truth established for governance commencement.*

---

*GOVERNANCE_BASELINE_CORRECTION_REPORT v1.0 | WP14A — Governance Baseline Correction Pass | 2026-06-16*
