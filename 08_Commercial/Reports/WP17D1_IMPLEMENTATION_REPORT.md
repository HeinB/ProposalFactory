---
document_id: WP17D1-IMPLEMENTATION-REPORT
title: "WP17D-1 Implementation Report — ARM IT045 Inline Text Assembly"
version: "1.0"
status: "Complete — Quality Pass Applied 2026-06-25"
generated: "2026-06-24"
generated_by: "WP17D-1 — Inline Text Assembly Engine"
---

# WP17D-1 Implementation Report — ARM IT045 Inline Text Assembly

**Date:** 2026-06-24 | **Version:** 1.0 | **Status:** Complete — Quality Pass Applied 2026-06-25

---

## 1. Work Package Summary

WP17D-1 extends the Assembly Engine to produce client-ready assumption schedules containing full assumption text, replacing the ID-only dry-run output produced by WP17B.

**Objective:** Implement the Option B dual-output model approved in WP17D-0A. Two client-ready documents per assembly: (1) complete assumption schedule (appendix); (2) key assumptions section (proposal body).

**Test case:** ARM IT045 — African Rainbow Minerals, Oracle EBS AMS Full Stack pattern, 6 packs, 594 net assumptions.

**Governance decisions binding on WP17D-1:**
- Decision 1: Executive Assumption Summary uses deterministic rules only — no AI judgement, no manual curation
- Decision 2: Master schedule numbering generated first; body section reuses exact same numbering
- Decision 3: Legal linkage statement included verbatim per governance standard

---

## 2. Inputs Used

| Source File | Pack | Version | Assumptions |
|---|---|---|---|
| ERP_ASSUMPTIONS_V1.md | Oracle ERP (Fusion Financials + PPM) | 1.0 Approved | 123 |
| OCI_ASSUMPTIONS_V1.md | Oracle Cloud Infrastructure | 1.0 Approved | 174 |
| OIC_ASSUMPTIONS_V1.md | Oracle Integration Cloud | 1.0 Approved | 104 |
| AMS_ASSUMPTIONS_V1.md | Application Managed Services (Base) | 1.0 Approved | 84 |
| EBS_AMS_SLA_OVERLAY_V1.md | EBS AMS SLA Overlay | 1.0 Approved | 53 |
| EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md | EBS Dedicated Resource Model | 1.0 Approved | 62 |
| ASSUMPTION_SCHEDULE_STANDARD.md | Format specification | 1.0 Approved | — |
| EXECUTIVE_ASSUMPTION_SUMMARY_RULES.md | Body selection rules | 1.0 Approved | — |
| ASSUMPTION_GROUPING_RULES.md | Section mapping rules | 1.0 Approved | — |

---

## 3. Packs Loaded and Assumption Inventory

| Pack | Total | Suppressed | Net Active |
|---|---|---|---|
| ERP (Oracle Fusion ERP) | 123 | 0 | 123 |
| OCI (Oracle Cloud Infrastructure) | 174 | 0 | 174 |
| OIC (Oracle Integration Cloud) | 104 | 0 | 104 |
| AMS (Managed Services Base) | 84 | 6 | 78 |
| EBS-SLA Overlay | 53 | 0 | 53 |
| EBS-DRM Overlay | 62 | 0 | 62 |
| **Total** | **600** | **6** | **594** |

---

## 4. Suppression Log

| Suppressed ID | Rule | Reason | Replacement |
|---|---|---|---|
| AMS-INC-004 | S1 — Pack-level INC replacement | Dedicated resource model covers this obligation | EBS-DRM-013 |
| AMS-SLA-001 | S2 — SLA overlay supersedes | EBS-SLA overlay provides full SLA framework | EBS-SLA-002 |
| AMS-SLA-005 | S3 — DRM overlay supersedes | EBS-DRM framework covers this commitment | EBS-DRM-001 |
| AMS-PRI-001 | S2 — SLA overlay supersedes | EBS-SLA priority tier definitions replace base | EBS-SLA-004, EBS-SLA-011 |
| AMS-PRI-002 | S2 — SLA overlay supersedes | EBS-SLA response/resolution times replace base | EBS-SLA-005 to EBS-SLA-009 |
| AMS-PRI-003 | S2 — SLA overlay supersedes | EBS-SLA escalation framework replaces base | EBS-SLA-012 |

Net effect: AMS PRI section has 0 active assumptions (all 3 suppressed). AMS SLA section has 3 active assumptions (002, 003, 004).

---

## 5. Section Assignment Results

| Section | Description | Count | Range | Pack Sources |
|---|---|---|---|---|
| A | General and Engagement | 24 | 1–24 | ERP, OCI |
| B | Project Execution | 42 | 25–66 | ERP, OIC |
| C.1 | ERP Functional | 54 | 67–120 | ERP |
| C.3 | OIC Integration | 44 | 121–164 | OIC |
| D | Infrastructure (OCI) | 130 | 165–294 | OCI |
| E | Managed Services (AMS) | 183 | 295–477 | AMS, EBS-SLA, EBS-DRM, OCI, OIC |
| F | Security | 22 | 478–499 | ERP, OCI, OIC |
| G | Client Responsibilities | 46 | 500–545 | ERP, OIC, AMS |
| H | Explicit Exclusions | 49 | 546–594 | ERP, OCI, OIC, AMS |
| **Total** | | **594** | **1–594** | |

---

## 6. Executive Assumption Summary (Body Section) Results

| Sub-section | Selection Rule | Count | Sequential Numbers |
|---|---|---|---|
| 1 — Engagement & Commercial | GEN (P4), ENH (P5), CR (P5) | 24 | 1–16, 320–327 |
| 2 — Service Management & SLA | SLA (P3, incl. EBS-SLA) | 56 | 332–387 |
| 3 — Client Responsibilities | CUS, CON, DEP (P2) | 46 | 500–545 |
| 4 — Explicit Exclusions | EXC, EXT (P1) | 49 | 546–594 |
| **Body total** | | **175** | Non-contiguous (correct) |
| Appendix only | All other codes | 419 | Various |

**Note on variance from WP17D-0A estimate:** The original estimate was ~130 body assumptions. Actual count is 175. The discrepancy arises entirely from Sub-section 2 (SLA): estimated ~20 items, actual 56. Reason: EBS-SLA-001 through EBS-SLA-053 (all 53 items) carry the SLA section code and are all selected under Priority 3 (no cap applies). This is the correct deterministic result — no rule was deviated from.

---

## 7. Validation Checks

| # | Check | Expected | Actual | Result |
|---|---|---|---|---|
| V1 | Numbering continuity | 1–594 sequential | 1–594 assigned | ✅ PASS |
| V2 | Traceability integrity | Every entry has *(Ref: ID)* | All 594 entries have Ref IDs (tabular assumptions Ref ID on own line — valid) | ✅ PASS |
| V3 | Grouping rule compliance | 23 rules applied | OIC-SUP corrected C.3→E; C.3=44, E=183 | ✅ PASS |
| V4 | Suppression rule compliance | 6 suppressed IDs absent | 0 missing found | ✅ PASS |
| V5 | Executive summary rule compliance | Priority 1–5 applied | 175 selected | ✅ PASS |
| V6 | Ref ID preservation | All IDs in PACK-SECTION-NNN form | All 594 have Ref IDs | ✅ PASS |
| V7 | Duplicate detection | 0 duplicate seq numbers | 0 duplicates (fixed dict) | ✅ PASS |
| V8 | Schedule completeness | 594 net assumptions | 594 in schedule | ✅ PASS |
| V9 | Executive summary completeness | EXC(49)==H(49); CUS/CON/DEP(46)==G(46) | As stated | ✅ PASS |
| V10 | ARM IT045 audit consistency | 6 packs, 6 suppressions match WP17B | Confirmed | ✅ PASS |

---

## 8. Deliverables Produced

| Deliverable | File | Status |
|---|---|---|
| Complete Assumption Schedule | ARM_IT045_ASSUMPTION_SCHEDULE_V1.md | ✅ Complete |
| Key Assumptions (Proposal Body) | ARM_IT045_KEY_ASSUMPTIONS_V1.md | ✅ Complete |
| Implementation Report | WP17D1_IMPLEMENTATION_REPORT.md | ✅ Complete |

---

## 9. Known Limitations and Observations

- **Body count variance:** Estimate ~130; actual 175. Entire difference in Sub-section 2 (SLA). Correct result.
- **OCI-GEN in Section A:** Placed per P3/P5 rule (OCI+GEN → A). Not in Section D. Correct.
- **OCI-CST in Section A:** Placed per P5 rule (OCI+CST → A). Correct.
- **OCI-SUP in Section E (end):** Placed per Section 4.5 ordering. Correct (items 466–473).
- **OIC-SUP corrected to Section E:** Initial assembly placed OIC-SUP-001 to OIC-SUP-004 in Section C.3 (grouping error). Corrected in WP17D-1 quality pass (2026-06-25): removed from C.3, items 169–477 renumbered to 165–473, OIC-SUP inserted as items 474–477 at end of Section E. C.3=44 items, E=183 items.
- **AMS-PRI: 0 active items.** All 3 suppressed by EBS-SLA overlay. No Priority 3 items from AMS-PRI appear in body Sub-section 2.
- **EBS-DRM-013** replaces AMS-INC-004. The dedicated resource model covers the incident escalation obligation.
- **22 assumption texts cleaned:** Initial assembly included internal BU Lead decision resolution notes and pack approval footers in 22 assumption texts. Stripped in WP17D-1 quality pass (2026-06-25). Two assumptions (EBS-SLA-011 item 349; EBS-SLA-017 item 355) also had missing response/resolution time tables restored from source pack.
- **Assembly method:** AI agent assembly with manual quality review pass. Output verified assumption-by-assumption against source packs.

---

## 10. Recommendations for WP17E

- Formalise the Python assembly script as the canonical WP17E automation baseline
- Add pack version check: verify all loaded packs are Approved v1.0 or later before assembly
- Implement automated V9 validation as post-generation CI check
- WP17D-2 (HCM Full Suite) should test pattern without AMS pack — Sub-section 2 should be absent
- Document the body count variance in the Assembly Engine specification
- Consider adding a `valid_from` / `valid_to` field to each pack file for temporal governance

---

## Design Programme Status

| Work Package | Description | Status |
|---|---|---|
| WP17D-0 | Assumption Schedule Design Standard | ✅ COMPLETE |
| WP17D-0A | Assumption Schedule Consumption Model | ✅ COMPLETE |
| WP17D-1 | Inline Text Assembly (ARM IT045) | ✅ COMPLETE |
| WP17D-2 | HCM Full Suite pattern | 🔴 NOT STARTED |
| WP17D-3 | Acumatica standalone pattern | 🔴 NOT STARTED |
| WP17D-4 | BeBanking + OIC + AMS pattern | 🔴 NOT STARTED |
| WP17D-5 | Plennegy live assembly | 🔴 BLOCKED (OAR-C01, OAR-C02, OAR-A01) |

---

*WP17D1_IMPLEMENTATION_REPORT.md | WP17D-1 Complete | 2026-06-24*  
*ARM IT045 | EBS AMS Full Stack | 594 net assumptions | 175 body assumptions*  
*Assembly Engine v1.1 | Option B Dual-Output Model*