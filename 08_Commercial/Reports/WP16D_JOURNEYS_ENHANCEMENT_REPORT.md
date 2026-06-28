---
document_id: WP16D-JOURNEYS-ENHANCEMENT-REPORT
title: "WP16D — Oracle Journeys Post-Programme Enhancement Report"
version: "1.0"
status: "Complete"
created: "2026-06-19"
created_by: "WP16D — Oracle Journeys Post-Programme Enhancement"
approved_by: "BU Lead — Oracle Practice (BU-HCM-022 pre-approved)"
category: "Governance / Enhancement Report"
work_package: "WP16D"
scope: "Post-programme enhancement to HCM Base Assumptions Pack — Oracle Journeys scope definition"
---

# WP16D — Oracle Journeys Post-Programme Enhancement Report

**Date:** 2026-06-19  
**Status:** COMPLETE  
**Nature:** Post-programme BAU maintenance (not a governance programme reopening)  
**Trigger:** Post-programme review identified absence of a Journey scope assumption in the HCM Base pack — scope ambiguity risk for all Oracle HCM proposals including Journey configuration.

---

## 1. Background

The Assumption Library Governance Programme was completed on 2026-06-19 (WP16C). At programme completion, 13 of 13 packs were Approved v1.0 with 1,135 approved assumptions and 0 outstanding BU decisions.

A post-programme review of the Oracle HCM Base pack identified a gap: while Oracle Journeys is listed as a component of the Oracle Fusion HCM Base Cloud Service (B85800), no assumption existed to establish the default number of Journeys included in a standard implementation. This created commercial exposure — clients could reasonably expect unlimited Journey configuration effort to be included in a fixed-price HCM implementation.

**Business Decision BU-HCM-022** was raised and approved (status: APPROVED) to resolve this gap. This work package applies that decision.

---

## 2. Business Decision Applied

| Field | Value |
|---|---|
| **Decision ID** | BU-HCM-022 |
| **Decision Name** | Default Journey Count |
| **Status** | APPROVED — pre-approved before WP16D execution |
| **Approved Option** | Option B — 3 standard Journeys |
| **Applied by** | WP16D — 2026-06-19 |

**Decision:**  
The standard Oracle HCM implementation includes configuration of up to three (3) Oracle Journeys using Oracle-delivered functionality.

| Journey # | Category | Description |
|---|---|---|
| 1 | New Hire Onboarding | Employee onboarding Journey from hire to productive |
| 2 | Internal Transfer / Promotion | Internal mobility, promotion, or transfer lifecycle |
| 3 | Offboarding | Employee offboarding and exit process |

Additional Journeys are separately scoped and priced as Change Requests.

---

## 3. Assumption Created

### HCM-JRN-001 — Journey Scope

**Location:** `08_Commercial/Assumptions/HCM/HCM_BASE_ASSUMPTIONS_V1.md` — Section 14 (General Assumptions), inserted after HCM-GEN-010.

**Assumption text:**

> Oracle Journeys are configured based on the business processes identified during design workshops. Unless otherwise stated in the Statement of Work, the standard Oracle HCM implementation includes configuration of up to three (3) Oracle Journeys using Oracle-delivered functionality and standard task types. The standard implementation assumes one onboarding Journey, one internal movement Journey (transfer or promotion), and one offboarding Journey. Additional Journeys, complex conditional logic, custom integrations, external system orchestration, advanced approvals, bespoke user experiences, or Journey redesign activities are separately scoped.

**Assumption ID rationale:** `HCM-JRN-001` — "JRN" identifies the Journeys category within the HCM pack family. Placed in Section 14 (General Assumptions) to avoid section numbering conflicts with module packs (Sections 16–50).

**BU decision tag:** `*(BU-HCM-022 — WP16D 2026-06-19)*` applied inline.

---

## 4. Files Updated

### 4.1 HCM_BASE_ASSUMPTIONS_V1.md

| Change | Before | After |
|---|---|---|
| Document version | 1.0 | 1.1 |
| Assumption count (frontmatter) | 114 | 115 |
| Assumption count (footer) | 114 | 115 |
| `last_updated` field | Not present | 2026-06-19 |
| `last_updated_by` field | Not present | WP16D — Oracle Journeys Post-Programme Enhancement |
| BU decisions table rows | 7 | 8 (BU-HCM-022 added) |
| BU decisions applied (frontmatter list) | 7 entries | 8 entries (BU-HCM-022 added) |
| Section 14 assumptions | 10 (HCM-GEN-001–010) | 11 (HCM-GEN-001–010 + HCM-JRN-001) |
| Section count | 15 | 15 (unchanged) |

### 4.2 TENDER_ASSUMPTION_ASSEMBLY_RULES.md

| Change | Before | After |
|---|---|---|
| Document version | 1.7 (frontmatter) / 1.8 (footer) | 1.9 |
| `last_updated_by` | WP16A | WP16D |
| Section 2.1 — Recruiting status | Draft — Pending BU Lead Approval | Approved v1.0 — 2026-06-19 (WP16C) |
| Section 2.1 — Learning status | Draft — Pending BU Lead Approval | Approved v1.0 — 2026-06-19 (WP16C) |
| Section 2.1 — Talent status | Draft — Pending BU Lead Approval | Approved v1.0 — 2026-06-19 (WP16C) |
| Section 2.1 — Compensation status | Draft — Pending BU Lead Approval | Approved v1.0 — 2026-06-19 (WP16C) |
| Section 3.1 — B85800 row | No Journey governance reference | HCM-JRN-001 noted; 3-Journey default and CR trigger documented |
| Section 3.1 — B87675/B95763/B109620/B85242/B94925 rows | [Draft] | [Approved v1.0 — 2026-06-19 (WP16C)] |
| Section 3.2 — Assembly matrix label | "planned" | Active (all packs Approved v1.0) |
| Section 3.2a | Not present | New section — Oracle Journeys Scope Rule (Rule JRN-1) added |
| Section 9 — HCM Base count | 114 | 115 |
| Section 9 — 4 HCM module pack statuses | Draft — Pending BU Lead Approval | Approved v1.0 — 2026-06-19 (WP16C) |
| Section 9 — Total approved | 983 | 1,136 |
| Section 9 — Draft count | 152 | 0 |
| Section 9 — Total assumptions | 1,135 | 1,136 |
| Footer "Next update trigger" | "First HCM module pack approved" | "New assumption pack added, BOM line item changes, or new Journey BU decision" |
| WP16C status propagation note | Not present | Added to Section 9 change log |
| WP16D status note | Not present | Added to Section 9 change log |

---

## 5. Count Reconciliation

| Pack | WP16A Approved | WP16C Change | WP16D Change | Final |
|---|---|---|---|---|
| HCM Base | 114 | — | +1 (HCM-JRN-001) | **115** |
| HCM Recruiting | 54 (draft→approved) | +54 approved | — | **54** |
| HCM Learning | 37 (draft→approved) | +37 approved | — | **37** |
| HCM Talent | 31 (draft→approved) | +31 approved | — | **31** |
| HCM Compensation | 30 (draft→approved) | +30 approved | — | **30** |
| OIC | 104 | — | — | 104 |
| ERP | 123 | — | — | 123 |
| OCI | 174 | — | — | 174 |
| AMS | 84 | — | — | 84 |
| Acumatica | 152 | — | — | 152 |
| BeBanking | 117 | — | — | 117 |
| EBS SLA Overlay | 53 | — | — | 53 |
| EBS DRM Overlay | 62 | — | — | 62 |
| **TOTAL** | **983 approved / 152 draft / 1,135** | **+152 approved / −152 draft** | **+1 approved** | **1,136 approved / 0 draft / 1,136** |

---

## 6. Assembly Rule Changes

### Rule JRN-1 Added (Section 3.2a of TENDER_ASSUMPTION_ASSEMBLY_RULES.md)

**Determination:** HCM-JRN-001 is automatically included in all Oracle HCM proposals. No additional assembly trigger is required.

**Rationale:** Oracle Journeys (B85800) is part of the Oracle Fusion HCM Base Cloud Service. The HCM Base pack is mandatory for all HCM proposals. HCM-JRN-001 is a base pack assumption; therefore it assembles automatically whenever HCM Base is loaded — which is every Oracle HCM proposal without exception.

**Escalation trigger added:** If the client's RFP or workshop notes reference more than three (3) Journeys, or Journey categories outside the three standard types, the proposal author must flag this as a scope addition with a Change Request line item. This is now codified in Rule JRN-1.

**No separate trigger required for:**
- Oracle Core HR present → HCM Base loaded → HCM-JRN-001 included ✓
- Journeys SKU detected → HCM Base is the SKU → HCM-JRN-001 included ✓
- Onboarding scope detected → HCM Base is loaded → HCM-JRN-001 included; confirm client not expecting more than the 3 standard Journeys ✓

---

## 7. Validation Results

### 7.1 Assumption Numbering

| Check | Result |
|---|---|
| HCM-JRN-001 unique across all packs | PASS — no other JRN-prefixed assumption exists |
| Section numbering conflict (Section 16+) | PASS — HCM-JRN-001 placed in Section 14; Section 16 reserved for module packs |
| Assumption count frontmatter matches body | PASS — both updated to 115 |
| Footer count matches | PASS — updated to 115 |

### 7.2 Cross-Pack Conflict Check

| Pack | Journey References Found | Assessment |
|---|---|---|
| HCM Base | HCM-JRN-001 (new) | Source |
| HCM Recruiting | 1 reference — "initiation of onboarding Journeys" in Recruiting-to-HCM transition assumption | **COMPLEMENTARY, NOT CONFLICTING** — describes workflow trigger (candidate acceptance → Journey initiation), not Journey count or scope |
| HCM Learning | None | No conflict |
| HCM Talent | None | No conflict |
| HCM Compensation | None | No conflict |
| OIC | None | No conflict |
| ERP | None | No conflict |
| AMS | None | No conflict |
| OCI | None | No conflict |
| Acumatica Base | None | No conflict |
| BeBanking Base | None | No conflict |
| EBS SLA Overlay | None | No conflict |
| EBS DRM Overlay | None | No conflict |

**Overall conflict status: CLEAR — No conflicting Journey assumptions exist in any pack.**

### 7.3 Note on Recruiting Pack Cross-Reference

The Recruiting pack assumption referencing "initiation of onboarding Journeys" is deliberately complementary to HCM-JRN-001:
- **Recruiting pack:** Governs the Recruiting-to-HCM workflow trigger — i.e., *when* an onboarding Journey is initiated.
- **HCM-JRN-001:** Governs *how many* Journeys are in scope and what Journey types are standard.

These assumptions address different dimensions of the same feature. No resolution required. No amendment to the Recruiting pack is needed.

### 7.4 Library Integrity

| Check | Result |
|---|---|
| All 13 packs remain Approved v1.0 | PASS |
| No governance artefacts reopened | PASS |
| No new BU decisions created | PASS — BU-HCM-022 was pre-approved |
| No new outstanding decisions | PASS |
| Draft assumption count | 0 (unchanged) |
| GOVERNANCE PROGRAMME status | COMPLETE (unchanged) |

---

## 8. Recommendations for Future Journey-Related Enhancements

### 8.1 No Immediate Action Required

The current HCM-JRN-001 assumption is sufficient for all standard Oracle HCM proposals. No further Journey assumptions are required to address the gap identified at WP16D inception.

### 8.2 Future Enhancement Candidates (BAU — No Decision Required Now)

The following enhancements could be considered in future BAU maintenance rounds:

| # | Enhancement | Trigger Condition | Priority |
|---|---|---|---|
| FE-JRN-001 | Journey Exclusions assumption — explicitly exclude Journey types not in base scope (e.g., Probation Reviews, Return-to-Work, Policy Compliance, Cross-Entity Transfers) | Client RFPs begin requesting Journey lists that extend beyond the 3 standard types | LOW — add when pattern emerges |
| FE-JRN-002 | Journey Task Type assumption — clarify Oracle-standard task types included (checklist tasks, forms, e-signatures, document upload) vs custom task integrations | Client proposals raise questions about task type boundaries | LOW — current wording ("standard task types") sufficient for now |
| FE-JRN-003 | Journey Analytics assumption — clarify whether OTBI Journey completion reporting is in scope | Clients request Journey adoption/completion dashboards beyond standard OTBI | LOW — covered by HCM-RPT-001/002 in principle |
| FE-JRN-004 | BeBanking onboarding Journey — clarify whether BeBanking bank account setup tasks can be included in the onboarding Journey via standard Oracle mechanism | BeBanking + Oracle HCM combined proposals | MEDIUM — assess at first combined proposal |

### 8.3 No Oracle Journeys Module Pack Required

Oracle Journeys does not warrant a standalone module assumption pack. Journeys is a configuration feature of the HCM Base platform, not a separately licensed module. HCM-JRN-001 in the base pack, supplemented by the escalation trigger in Rule JRN-1, is the correct and proportionate governance mechanism.

---

## 9. Summary

| Item | Result |
|---|---|
| Assumption created | HCM-JRN-001 — Journey Scope |
| Location | HCM_BASE_ASSUMPTIONS_V1.md — Section 14, after HCM-GEN-010 |
| BU decision applied | BU-HCM-022 — CLOSED |
| HCM Base pack version | 1.0 → 1.1 |
| HCM Base assumption count | 114 → 115 |
| Assembly Rules version | 1.8 → 1.9 |
| New assembly rule | Rule JRN-1 (Section 3.2a) — Journey scope automatically included with HCM Base |
| Library total (approved) | 1,135 → 1,136 |
| Library draft count | 0 (unchanged) |
| Cross-pack conflicts | None |
| Governance programme status | COMPLETE (unchanged) |
| Outstanding BU decisions | 0 (unchanged) |

---

*WP16D — Oracle Journeys Post-Programme Enhancement Report v1.0 | 2026-06-19 | COMPLETE*  
*BU-HCM-022 applied. HCM Base v1.1. Library: 1,136 assumptions / 13 packs / 0 draft / 0 outstanding decisions.*  
*This is a post-programme BAU maintenance enhancement — the Governance Programme remains COMPLETE.*