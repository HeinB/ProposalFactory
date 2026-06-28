---
title: WP14F — BeBanking Assumption Pack Promotion Report
version: v1.0
status: Complete
programme: WP14F
date: 2026-06-18
author: AI (Claude)
authority: BeBanking BU Lead + Commercial Director (BU-BB-002 approved via WP14E)
---

# WP14F — BeBanking Base Assumption Pack Promotion Report

**Programme:** WP14F | **Date:** 2026-06-18 | **Status:** COMPLETE

---

## 1. Promotion Summary

The BeBanking Base Assumption Pack (Pack 9 / Code BB) has been promoted from **Draft v1.1** to **Approved v1.0** following resolution of all outstanding BU Lead governance decisions.

| Item | Before WP14F | After WP14F |
|---|---|---|
| Pack status | Draft — Pending BU Lead Approval | **Approved v1.0** |
| Assumptions in pack | 117 | 117 |
| BU decisions outstanding | 1 (BU-BB-002) | **0** |
| Approved for reuse in proposals | No | **Yes** |
| Approval date | — | **2026-06-18** |
| Approval programme | — | **WP14F** |

---

## 2. Governance Decisions Closed

All 10 BeBanking BU Lead decisions are now resolved:

| ID | Title | Priority | Resolution | Programme |
|---|---|---|---|---|
| BU-BB-006 | Support model and SLA | CRITICAL | Support included in BeBanking subscription. BB-SUP-001 updated. | WP14D |
| BU-BB-001 | Supported bank list | HIGH | Confirmed 9 banks. BB-BNK-001 updated. | WP14D |
| BU-BB-002 | New bank onboarding fee model | HIGH | Fixed-price Change Request per BeBanking Bank Addition SOW Schedule. BB-EXT-008 and BB-SUP-006 locked. | WP14E + WP14F |
| BU-BB-003 | Forex inclusion in base | HIGH | Forex partners: Citi Bank UK, ABSA, Nedbank, FNB. BB-FX-002 updated. | WP14D |
| BU-BB-008 | Payroll source policy | HIGH | Oracle EBS Payroll and PaySpace confirmed supported. BB-PYR-002 updated. | WP14D |
| BU-BB-004 | Hypercare duration | MEDIUM | 30-day hypercare standard. BB-CUT-002 updated. | WP14D |
| BU-BB-005 | Standard reporting pack | MEDIUM | 5 standard reports. BB-RPT-001 updated. | WP14D |
| BU-BB-007 | Multi-country deployment scope | MEDIUM | Namibia separately scoped. BB-BNK-009 updated. | WP14D |
| BU-BB-009 | POPIA operator disclosure | MEDIUM | POPIA disclosure standard. BB-DAT-006 updated. | WP14D |
| BU-BB-010 | DR testing frequency | MEDIUM | BB-ENV-006 deleted — DR not asserted. | WP14D |

**WP14E deliverable:** Decision paper WP14E_BU_BB_002_DECISION_PAPER.md provides full analysis of Option A (fixed-price CR) with effort ranges by bank type, enabling presales quoting without per-opportunity BU assessment.

---

## 3. Files Updated

### Pack files

| File | Change | Version |
|---|---|---|
| `08_Commercial/Assumptions/BeBanking/BEBANKING_BASE_ASSUMPTIONS_V1.md` | Promoted to Approved v1.0; approved_for_reuse: Yes; BU-BB-002 added to resolved list; Readiness 9.0 → 9.5; header changed from WARNING to APPROVED FOR USE | v1.0-Approved |
| `08_Commercial/Assumptions/BeBanking/BEBANKING_ASSUMPTION_REGISTER.csv` | All 117 rows status set to Approved | — |
| `08_Commercial/Assumptions/BeBanking/BEBANKING_GAP_REPORT.md` | GAP-BB-001 PARTIALLY RESOLVED → FULLY RESOLVED; BU-BB-002 RESOLVED WP14F | v1.2-Approved |

### Governance files

| File | Change | Version |
|---|---|---|
| `08_Commercial/Assumptions/Governance/GOVERNANCE_DASHBOARD.md` | Approved packs 5 → 6; 730 assumptions approved; 35 decisions outstanding; BeBanking all resolved; BU-BB-006 resolution note added | v1.2 |
| `HANDOVER.md` | Quick Facts, System Maturity table, assumption library table, file register updated | v2.7 |
| `AI_CONTEXT.md` | Assumption library table updated; Active Work Queue: WP11J row updated to COMPLETE; BU-ACU-009 elevated to priority 4 | — |

### Programme files

| File | Change |
|---|---|
| `08_Commercial/WP14E_BU_BB_002_DECISION_PAPER.md` | CREATED — 8-section decision paper for BU-BB-002 |
| `08_Commercial/WP14F_BEBANKING_PROMOTION_REPORT.md` | CREATED — this report |

---

## 4. Validation Results

| Check | Result |
|---|---|
| MD assumption body count (regex `\*\*(BB-[A-Z]+-\d{3}):\*\*`) | 117 |
| CSV row count (excl. header) | 117 |
| Frontmatter `assumption_count` | 117 |
| Section index total (PYR 9 + RPT 5 + ENV 5 + others) | 117 |
| CSV rows with status = Approved | 117 |
| CSV rows with status ≠ Approved | 0 |
| BU decisions outstanding | 0 |
| `approved_for_reuse` | Yes |
| `bu_lead_decisions_pending` | [] (empty) |

All validation checks: **PASS**

---

## 5. Updated Programme Metrics

| Metric | Before WP14F | After WP14F |
|---|---|---|
| Approved packs | 5 | **6** |
| Draft packs | 6 | **5** |
| Approved assumptions | 613 | **730** |
| Total assumptions (post-WP14D deletions) | 1,055 | 1,055 |
| Outstanding BU decisions | 36 | **35** |
| CRITICAL decisions outstanding | 2 | **1** (BU-ACU-009 only) |
| HIGH decisions outstanding | 13 | **9** |
| MEDIUM decisions outstanding | 20 | **15** |

---

## 6. Remaining Outstanding Decisions

The following 35 decisions remain open across 5 draft packs:

| Pack | Count | Critical | Notes |
|---|---|---|---|
| Acumatica Base | 14 | 1 (BU-ACU-009 OVERDUE) | BU-ACU-009 is the only remaining CRITICAL blocker in the programme |
| Oracle HCM Recruitment | 7 | 0 | 2 HIGH, 5 LOW |
| Oracle HCM Learning | 5 | 0 | 2 MEDIUM, 3 LOW |
| Oracle HCM Talent | 4 | 0 | 1 MEDIUM, 3 LOW |
| Oracle HCM Comp | 5 | 0 | 2 MEDIUM, 3 LOW |
| **Total** | **35** | **1** | |

---

## 7. Post-Approval Actions (Human)

The following actions are required by the BeBanking BU Lead and are not blocked by this promotion:

| Action | Owner | Priority | Notes |
|---|---|---|---|
| Publish BeBanking Bank Addition SOW Schedule | BeBanking BU Lead | HIGH | Effort ranges by bank type for presales quoting (see WP14E Section 5 draft schedule) |
| Confirm Bank Format Register | BeBanking BU Lead | MEDIUM | GAP-BB-003 operational improvement item |
| Confirm AVS availability per bank | BeBanking BU Lead | MEDIUM | GAP-BB-004 |
| Confirm DR RTO/RPO if formally committed | BeBanking BU Lead | LOW | GAP-BB-005 resolution was by deletion; new BB-ENV assumption needed if DR is confirmed |

None of the above block proposal assembly. BeBanking Base Pack assumptions with `status = Approved` and `approved_for_reuse = Yes` are immediately available for use in tenders.

---

## 8. Recommendation

**BeBanking Base Pack (117 assumptions, Sections 140–153) is APPROVED FOR USE in client-facing proposals as of 2026-06-18.**

Governance rule: only assumptions with `approved_for_reuse = Yes` in an Approved pack may be assembled into external documents (Rule 17, Rule 18 — Governance Constraints).

The pack joins five other approved packs:

| Pack | Assumptions |
|---|---|
| Oracle HCM Base | 114 |
| Oracle OIC | 101 |
| Oracle ERP | 128 |
| Oracle AMS | 96 |
| Oracle OCI | 174 |
| **BeBanking Base** | **117** |
| **Total available** | **730** |

---

*WP14F BeBanking Promotion Report v1.0 | Approved v1.0 2026-06-18 | 0 BU decisions outstanding*
