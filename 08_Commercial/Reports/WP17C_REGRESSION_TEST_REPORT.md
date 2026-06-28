---
document_id: WP17C-REGRESSION-TEST-REPORT
title: "WP17C — Assembly Engine Regression Test Suite"
version: "1.0"
status: "Complete"
created: "2026-06-22"
created_by: "WP17C — Assembly Engine Regression Test Suite"
category: "Assembly Engine / Validation Report"
scope: "Five archetype regression tests validating Assembly Engine before inline text assembly (WP17D)"
---

# WP17C — Assembly Engine Regression Test Suite

**Date:** 2026-06-22  
**Status:** COMPLETE  
**Baseline:** WP17B Assembly Engine MVP (2026-06-19) — ARM IT045 dry-run complete; Engine operational  
**Scope:** Five independent regression tests across Oracle EBS AMS, HCM Full Suite, OIC standalone, BeBanking, and Acumatica

---

## 1. Executive Summary

All five regression tests pass. The Assembly Engine correctly identifies packs, applies suppression and replacement rules, excludes prohibited packs, and produces consistent assumption counts across all tested archetypes. No manual assumption selection was required for any test. One minor advisory finding (Test 4: AMS patch assumption context for non-Oracle-SaaS engagements) does not block production use.

**Verdict: Assembly Engine is PRODUCTION READY for assumption assembly.**  
**Recommendation: Proceed to WP17D — Inline Text Assembly.**

---

## 2. Test Matrix

| Test | Archetype | Pattern | Packs Loaded | Raw | Suppressed | Net | Result |
|---|---|---|---|---|---|---|---|
| T1 | ARM IT045 — EBS AMS Full Stack | EBS AMS Full Stack | 6 | 600 | 6 | 594 | **PASS** |
| T2 | Oracle HCM Full Suite | HCM Base + 4 Modules | 5 | 267 | 0 | 267 | **PASS** |
| T3 | Oracle OIC Standalone | OIC Only | 1 | 104 | 0 | 104 | **PASS** |
| T4 | BeBanking + OIC + AMS | BeBanking + Oracle Integration + Support | 3 | 305 | 0 | 305 | **PASS (advisory)** |
| T5 | Acumatica Standalone | Acumatica Base | 1 | 152 | 0 | 152 | **PASS** |
| | **TOTAL assumptions tested** | | | **1,428** | **6** | **1,422** | |

---

## 3. Test 1 — ARM IT045 (EBS AMS Full Stack)

### 3.1 Tender Profile

| Field | Value |
|---|---|
| Reference | ARM IT045 — African Rainbow Minerals; WON 2026-08-28 |
| Engagement | Oracle EBS Application Managed Services |
| Systems | EBS HR & Payroll v12.2.8 + EBS Financials v12.2.10 on OCI |
| OIC | In scope |
| AMS model | Dedicated Resource Model (680h/month, 5 named roles) |
| SLA | Enhanced 5-tier (P1=15min/2hr; 24/7 P1) |
| Validation source | WP17B dry-run artefacts (ARM_IT045_ASSEMBLED_ASSUMPTION_SCHEDULE.md + ARM_IT045_ASSEMBLY_AUDIT_REPORT.md) |

### 3.2 BOM Resolution

| Input | Decision | Pack |
|---|---|---|
| EBS in scope | ERP track (standalone) | ERP Pack ✓ |
| EBS on OCI | Rule OCI-1 triggered | OCI Pack ✓ |
| OIC integrations | OIC in scope | OIC Pack ✓ |
| AMS engagement | BOM 16 | AMS Pack ✓ |
| P1=15min, 5-tier, 24/7 | Enhanced SLA trigger | EBS SLA Overlay ✓ |
| Named roles, monthly hours | DRM trigger | EBS DRM Overlay ✓ |
| HCM Base | EBS AMS exclusion applied | **NOT LOADED ✓** |

**Pattern matched:** EBS AMS Full Stack (TENDER_ASSUMPTION_ASSEMBLY_RULES.md Section 3.5)

### 3.3 Packs Loaded

| # | Pack | Version | Count | Load Result |
|---|---|---|---|---|
| 1 | ERP Pack | 1.0 | 123 | LOADED |
| 2 | OCI Pack | 1.0 | 174 | LOADED |
| 3 | OIC Pack | 1.0 | 104 | LOADED |
| 4 | AMS Pack | 1.0 | 84 | LOADED |
| 5 | EBS SLA Overlay | 1.0 | 53 | LOADED |
| 6 | EBS DRM Overlay | 1.0 | 62 | LOADED |
| — | HCM Base | 1.1 | — | NOT LOADED (EBS AMS exclusion) |
| **Total** | | | **600** | |

### 3.4 Rules Triggered

| Rule | Result |
|---|---|
| Rule A — Base First | ERP Pack loads before OCI, OIC, AMS ✓ |
| Rule B — Additive Only | All overlays additive; no base overrides ✓ |
| Rule C — No Duplication | 0 duplicate IDs (unique prefixes: ERP-, OCI-, OIC-, AMS-, EBS-SLA-, EBS-DRM-) ✓ |
| Rule D — BOM Trigger | All 6 packs triggered from profile inputs ✓ |
| Rule E — Exclusions Included | ERP-EXC-001–012; OIC-EXC-001–015; AMS-EXC-001–012 included ✓ |
| Rule S1 — AMS-INC-004 | SUPPRESSED → EBS-DRM-013 ✓ |
| Rule S2 — SLA replacements | AMS-SLA-001, AMS-PRI-001/002/003 SUPPRESSED → EBS-SLA equivalents ✓ |
| Rule S3 — AMS-SLA-005 | SUPPRESSED → EBS-DRM-001 ✓ |
| Rule S4 — Overlay precedence | DRM Overlay takes precedence over SLA Overlay on shared topics ✓ |
| EBS AMS exclusion | HCM Base excluded ✓ |

### 3.5 Suppression Results

| Suppressed | Rule | Net Effect |
|---|---|---|
| AMS-INC-004 | S1 | Replaced by EBS-DRM-013 — correct EBS infrastructure statement ✓ |
| AMS-SLA-001 | S2 | Replaced by EBS-SLA-002 ✓ |
| AMS-PRI-001 | S2 | Replaced by EBS-SLA-004 + EBS-SLA-011 ✓ |
| AMS-PRI-002 | S2 | Replaced by EBS-SLA-005–009 ✓ |
| AMS-PRI-003 | S2 | Replaced by EBS-SLA-012 ✓ |
| AMS-SLA-005 | S3 | Replaced by EBS-DRM-001 ✓ |

**Total suppressed: 6 | Net active: 594**

### 3.6 Duplicate Detection

| Check | Result |
|---|---|
| ID-level duplicates | 0 — all prefixes unique across packs |
| Topic-level conflicts (overlay vs base) | 0 blocking conflicts — all replacements governed by S1–S4 |

### 3.7 Missing Content

| WP14C Gap | Status |
|---|---|
| GAP-001/002/003 (SLA, resolution times, DRM) | RESOLVED — EBS SLA + DRM Overlay |
| GAP-006 (P5 tier) | RESOLVED — EBS-SLA-009 |
| GAP-010 (no EBS AMS pattern) | RESOLVED — Section 3.5 v2.0 |
| GAP-011 (AMS-INC-004 EBS error) | RESOLVED — S1 suppression |
| GAP-005 (Mining Charter) | OPEN — no assumption pack; manual handling |
| GAP-007 (KT programme) | OPEN — no AMS KT assumption pack |
| GAP-009 (multi-site mine access) | OPEN — no multi-site assumption pack |

### 3.8 Manual Intervention Required

None. All assembly decisions governed by rules.

### 3.9 Verdict

**PASS** — Full dry-run artefacts in `08_Commercial/Assembly_Engine/`. 594 net assumptions. 6 suppressions correct.

---

## 4. Test 2 — Oracle HCM Full Suite

### 4.1 Tender Profile

| Field | Value |
|---|---|
| Reference | Hypothetical Oracle HCM Full Suite implementation |
| Engagement | Oracle Fusion HCM implementation — Core HR + Recruiting + Learning + Talent + Compensation |
| Scope | All 4 functional modules + Core HR; no OIC integrations in this test; no AMS |
| BOM codes | B85800 (HCM Base), B87675 (Recruiting), B85242 (Learning), B94925 (Talent), B109620 (Compensation) |

### 4.2 BOM Resolution

| Input | Decision | Pack |
|---|---|---|
| B85800 — HCM Base | HCM track base | HCM Base ✓ |
| B87675 — Recruiting | Requires HCM Base (Rule A) | Recruiting Pack ✓ |
| B85242 — Learning | Requires HCM Base (Rule A) | Learning Pack ✓ |
| B94925 — Talent | Requires HCM Base (Rule A) | Talent Pack ✓ |
| B109620 — Compensation | Requires HCM Base (Rule A) | Compensation Pack ✓ |
| OIC not specified | No OIC trigger | OIC Pack NOT loaded ✓ |
| AMS not specified | No AMS trigger | AMS Pack NOT loaded ✓ |
| OCI not specified | Rule OCI-1 not triggered | OCI Pack NOT loaded ✓ |
| ERP not specified | No ERP trigger | ERP Pack NOT loaded ✓ |

**Pattern matched:** HCM Full Suite (TENDER_ASSUMPTION_ASSEMBLY_RULES.md Section 3.2)

### 4.3 Packs Loaded

| # | Pack | Version | Count | Load Result |
|---|---|---|---|---|
| 1 | HCM Base | 1.1 | 115 | LOADED (base — load order 1) |
| 2 | HCM Recruiting | 1.1 | 54 | LOADED (module — load order 2) |
| 3 | HCM Learning | 1.1 | 37 | LOADED (module — load order 2) |
| 4 | HCM Talent | 1.1 | 31 | LOADED (module — load order 2) |
| 5 | HCM Compensation | 1.1 | 30 | LOADED (module — load order 2) |
| **Total** | | | **267** | |

### 4.4 Rules Triggered

| Rule | Result |
|---|---|
| Rule A — Base First | HCM Base loads before all module packs ✓ |
| Rule B — Additive Only | All module packs additive; HCM Base not overridden ✓ |
| Rule C — No Duplication | 0 duplicate IDs (HCM-, REC-, LRN-, TLT-, COM- all unique) ✓ |
| Rule D — BOM Trigger | All 5 packs triggered from BOM codes ✓ |
| Rule E — Exclusions Included | HCM-EXC-001–012; REC-EXC-001–008; LRN-EXC-001–008; TLT-EXC-001–006; COM-EXC-001–007 included ✓ |
| Rule JRN-1 — Journey scope | HCM-JRN-001 included in HCM Base (load order 1) — 3 standard Journeys in scope ✓ |

### 4.5 Journey Rule Validation (Rule JRN-1)

**Rule JRN-1** states: HCM-JRN-001 is automatically included whenever HCM Base loads. No additional BOM trigger required.

| Check | Result |
|---|---|
| HCM Base loads | ✓ |
| HCM-JRN-001 present in HCM Base pack | ✓ — assumption #115; Section 14 |
| Journey count scope | 3 standard Journeys (Onboarding, Transfer/Promotion, Offboarding) — in scope without escalation |
| Additional Journeys beyond 3 | Trigger CR escalation — not a pack loading rule; noted for bid manager |
| Journey Booster (W4-HCM-002 capability asset) | Not an assumption pack — loaded via TENDER_BOM_LIBRARY (separate from assumption assembly) |

**Verdict:** Rule JRN-1 behaves correctly. HCM-JRN-001 is inherent to HCM Base load; no separate trigger mechanism needed.

### 4.6 Suppression Results

None. All 5 packs are HCM-track with distinct prefixes. No EBS AMS rules apply.

**Total suppressed: 0 | Net active: 267**

### 4.7 Duplicate Detection

| Check | Result |
|---|---|
| ID-level duplicates | 0 — all prefixes unique: HCM-, REC-, LRN-, TLT-, COM- |
| Rule A compliance | HCM Base loaded first; all module packs loaded second ✓ |
| Rule B compliance | Module packs add new section-specific assumptions only; do not re-address HCM Base categories ✓ |
| Topic-level overlap | No base categories replicated in module packs (HCM-ENV/ORG/SEC vs REC-SIT/REQ, LRN-PLT/CON, etc.) ✓ |

**Structural uniqueness confirmed: 267 unique assumption IDs across 5 packs.**

### 4.8 Missing Content

| Topic | Coverage |
|---|---|
| Journeys | HCM-JRN-001 in HCM Base — 3 standard Journeys covered |
| OIC integration (if needed) | Not in this test scope — OIC Pack adds 104 assumptions when triggered |
| Booster (Recruiting) | REC-BOO-001–007 present in Recruiting Pack — covered ✓ |
| KT / onboarding assumptions | Covered in HCM-TRN-001–006 (base) + module-specific TRN assumptions |

### 4.9 Manual Intervention Required

None.

### 4.10 Verdict

**PASS** — 267 assumptions; Rule A load order correct; Rule JRN-1 validated; 0 suppressions; 0 duplicates.

---

## 5. Test 3 — Oracle OIC Standalone

### 5.1 Tender Profile

| Field | Value |
|---|---|
| Reference | Hypothetical Oracle OIC-only engagement |
| Engagement | Oracle Integration Cloud standalone implementation — 10 integration flows |
| Scope | OIC only; no HCM, no ERP, no AMS |
| BOM code | B91110 (Oracle Integration Cloud Enterprise) |

### 5.2 BOM Resolution

| Input | Decision | Pack |
|---|---|---|
| B91110 — OIC Enterprise | OIC integration layer | OIC Pack ✓ |
| No HCM BOM codes | No HCM trigger | HCM Base NOT loaded ✓ |
| No ERP BOM codes | No ERP trigger | ERP Pack NOT loaded ✓ |
| No AMS engagement | No AMS trigger | AMS Pack NOT loaded ✓ |
| No OCI specification | Rule OCI-1 not triggered | OCI Pack NOT loaded ✓ |

**Pattern matched:** OIC Standalone (TENDER_ASSUMPTION_ASSEMBLY_RULES.md Section 3.1 — B91110 row; standalone)

### 5.3 Packs Loaded

| # | Pack | Version | Count | Load Result |
|---|---|---|---|---|
| 1 | OIC Pack | 1.0 | 104 | LOADED |
| **Total** | | | **104** | |

### 5.4 Rules Triggered

| Rule | Result |
|---|---|
| Rule D — BOM Trigger | OIC Pack triggered by B91110 ✓ |
| Rule E — Exclusions Included | OIC-EXC-001–015 included ✓ |
| All other rules | Not applicable — single pack, no base/module/overlay hierarchy |

### 5.5 Suppression Results

None. Single pack; no suppression rules apply.

**Total suppressed: 0 | Net active: 104**

### 5.6 Duplicate Detection

Single pack — trivially no duplicates. All OIC- prefix IDs are unique within the pack.

### 5.7 Isolation Check

| Check | Result |
|---|---|
| No ERP assumptions in output | ✓ — no ERP- IDs present |
| No HCM assumptions in output | ✓ — no HCM- IDs present |
| No AMS assumptions in output | ✓ — no AMS- IDs present |
| No OCI assumptions in output | ✓ — no OCI- IDs present (OCI Pack not triggered) |

**Clean isolation confirmed: 104 OIC assumptions only.**

### 5.8 Missing Content

| Topic | Coverage |
|---|---|
| OIC scope, design, endpoints | OIC-SCP, OIC-DES, OIC-END — covered ✓ |
| Security, certification | OIC-SEC, OIC-CERT — covered ✓ |
| Mapping, testing, performance | OIC-MAP, OIC-TST, OIC-PERF — covered ✓ |
| Monitoring, support, cutover | OIC-MON, OIC-SUP, OIC-CUT — covered ✓ |
| OCI hosting assumptions | Not triggered — if OIC runs on OCI, OCI Pack should be added |

**Advisory:** For OIC engagements where OIC instance runs on OCI (private endpoint), Rule OCI-1 should be triggered, adding the OCI Pack. In this test, OIC is assumed SaaS-managed — no OCI Pack required.

### 5.9 Manual Intervention Required

None.

### 5.10 Verdict

**PASS** — 104 assumptions; clean isolation; correct exclusions included.

---

## 6. Test 4 — BeBanking + Oracle Integration + AMS

### 6.1 Tender Profile

| Field | Value |
|---|---|
| Reference | Hypothetical BeBanking post-implementation support engagement |
| Engagement | BeBanking implementation (with Oracle Fusion ERP as source system) + OIC integration + AMS post-go-live support |
| Scope | BeBanking Base + OIC Pack (BeBanking ↔ Oracle Fusion via OIC) + AMS Pack (support model) |
| Source system | Oracle Fusion ERP (SaaS) — not EBS |
| Infrastructure | BeBanking SaaS hosted (not OCI) |

### 6.2 BOM Resolution

| Input | Decision | Pack |
|---|---|---|
| BeBanking services in scope | BeBanking track | BeBanking Base ✓ |
| OIC integration (BeBanking ↔ Oracle Fusion) | OIC in scope | OIC Pack ✓ |
| AMS engagement (post-go-live support) | BOM 16 | AMS Pack ✓ |
| Oracle Fusion SaaS (source ERP) | Oracle Fusion is SaaS — ERP Pack NOT loaded | ERP Pack NOT loaded ✓ |
| BeBanking SaaS hosted | No OCI trigger | OCI Pack NOT loaded ✓ |
| HCM not in scope | No HCM trigger | HCM Base NOT loaded ✓ |

**Pattern matched:** BeBanking + Oracle Integration (Section 3.4) + AMS (Section 3.2 additive)

> **Note:** No named assembly pattern exists for BeBanking + OIC + AMS combined. The pattern is constructed from: BeBanking Section 3.4 + AMS additive rule. This is a minor gap — see Section 6.8.

### 6.3 Packs Loaded

| # | Pack | Version | Count | Load Result |
|---|---|---|---|---|
| 1 | BeBanking Base | 1.0 | 117 | LOADED |
| 2 | OIC Pack | 1.0 | 104 | LOADED |
| 3 | AMS Pack | 1.0 | 84 | LOADED |
| **Total** | | | **305** | |

### 6.4 Rules Triggered

| Rule | Result |
|---|---|
| Rule A — Base First | BeBanking Base loads before OIC and AMS ✓ |
| Rule B — Additive Only | OIC and AMS packs additive to BeBanking Base ✓ |
| Rule C — No Duplication | 0 duplicate IDs (BB-, OIC-, AMS- all unique) ✓ |
| Rule D — BOM Trigger | All 3 packs triggered from profile inputs ✓ |
| Rule E — Exclusions Included | OIC-EXC-001–015; AMS-EXC-001–012 included ✓ |
| Rule S1 — AMS-INC-004 | NOT triggered — S1 fires for EBS AMS only; Oracle Fusion SaaS is the correct context for AMS-INC-004 ✓ |

**AMS-INC-004 assessment for this test:**  
AMS-INC-004 states: "Oracle Fusion HCM and ERP are delivered on Oracle's SaaS infrastructure." In this engagement, Oracle Fusion ERP is the source system and IS delivered as SaaS. AMS-INC-004 is factually correct and correctly retained.

### 6.5 Suppression Results

None required. AMS-INC-004 is contextually appropriate (Fusion SaaS source).

**Total suppressed: 0 | Net active: 305**

### 6.6 Duplicate Detection

| Check | Result |
|---|---|
| ID-level duplicates | 0 — all prefixes unique: BB-, OIC-, AMS- |
| BeBanking-specific constraints | BeBanking SAP rule (Constraint 24), SWIFT rule (Constraint 14), Payroll H2H rule (Constraint 15) — all encoded in pack text; no conflicting AMS or OIC assumptions on these topics ✓ |

### 6.7 Governance Constraint Check

| Constraint | Status |
|---|---|
| BeBanking SAP: "integrates with SAP environments" only | Pack text applies; no module-level SAP claims ✓ |
| BeBanking Payroll H2H: Oracle EBS/Fusion only | Pack text applies; Acumatica payroll prohibition intact ✓ |
| SWIFT: bank-intermediated model only | Pack text applies; no direct SWIFT membership claims ✓ |
| BU-OCI-007 withdrawn: no BeBanking OCI pricing assumption | OCI Pack not loaded; BU-OCI-007 not in play ✓ |

### 6.8 Advisory Finding — AF-01: No Named BeBanking + AMS Pattern

**Finding:** TENDER_ASSUMPTION_ASSEMBLY_RULES.md Section 3.4 defines BeBanking assembly patterns up to "BeBanking + Oracle integration" (BeBanking + OIC). No named pattern exists for BeBanking + OIC + AMS.

**Impact:** Low. The assembly is constructed by applying the BeBanking + OIC pattern and then adding AMS additively (same approach as Acumatica + AMS in Section 3.3). Engine correctly assembles the combination without a named pattern.

**Recommendation:** Add "BeBanking + Oracle integration + AMS" pattern to Section 3.4 at next Assembly Rules update.

**Severity:** Advisory — does not block assembly or proposal submission.

### 6.9 Advisory Finding — AF-02: AMS-PAT-001 Context for Non-Oracle-SaaS Engagements

**Finding:** AMS-PAT-001 states: "Oracle Fusion HCM and ERP patches are applied by Oracle as part of the SaaS subscription." In a BeBanking engagement, BeBanking itself is not an Oracle SaaS product. AMS-PAT-001 is technically inapplicable to the BeBanking application layer.

**Impact:** Low. The assumption is accurate regarding the Oracle Fusion source system (which IS SaaS). BeBanking's own patch management is covered separately by BeBanking assumptions.

**Recommendation:** Bid manager to note AMS-PAT-001 applies to Oracle Fusion component only; BeBanking patching follows BeBanking's SaaS delivery model. No suppression rule needed — contextual clarification in proposal is sufficient.

**Severity:** Advisory — does not block assembly or proposal submission.

### 6.10 Missing Content

| Topic | Coverage |
|---|---|
| BeBanking banking assumptions (H2H, payments) | BB-XXX assumptions — covered ✓ |
| OIC integration assumptions | OIC-XXX — covered ✓ |
| Support model (scope, SLA, channels) | AMS-SCP, AMS-SLA, AMS-CHN, AMS-INC — covered ✓ |
| BeBanking-specific KT programme | No BeBanking KT assumptions — gap consistent with GAP-007; manual authoring required |
| New bank onboarding (post-go-live) | BB-EXT-008 (new bank = CR — fixed-price per BU-BB-002 WP14E) ✓ |

### 6.11 Manual Intervention Required

None for assembly. Bid manager advisory: clarify AMS-PAT-001 scope in proposal for BeBanking context.

### 6.12 Verdict

**PASS** (with 2 advisories) — 305 assumptions; 0 suppressions; 0 duplicates. Advisories AF-01 and AF-02 are non-blocking. No manual assumption selection required.

---

## 7. Test 5 — Acumatica Standalone

### 7.1 Tender Profile

| Field | Value |
|---|---|
| Reference | Hypothetical Acumatica ERP implementation |
| Engagement | Acumatica ERP — Financials + Distribution + Manufacturing; PaySpace payroll integration |
| Scope | Acumatica Base only (PaySpace integration method confirmed at pre-sales per BU-ACU-001) |
| Infrastructure | Cloud SaaS (Acumatica-hosted) — no OCI |

### 7.2 BOM Resolution

| Input | Decision | Pack |
|---|---|---|
| Acumatica ERP in scope | Acumatica track | Acumatica Base ✓ |
| Acumatica-hosted SaaS | No OCI trigger | OCI Pack NOT loaded ✓ |
| No BeBanking integration | No BeBanking trigger | BeBanking Base NOT loaded ✓ |
| No Oracle products | No Oracle trigger | HCM Base, ERP Pack, OIC, AMS NOT loaded ✓ |

**Pattern matched:** Acumatica ERP (TENDER_ASSUMPTION_ASSEMBLY_RULES.md Section 3.3)

### 7.3 Packs Loaded

| # | Pack | Version | Count | Load Result |
|---|---|---|---|---|
| 1 | Acumatica Base | 1.0 | 152 | LOADED |
| **Total** | | | **152** | |

### 7.4 Rules Triggered

| Rule | Result |
|---|---|
| Rule D — BOM Trigger | Acumatica Base triggered by Acumatica in scope ✓ |
| Rule E — Exclusions Included | ACU exclusion assumptions included ✓ |
| All other rules | Not applicable — single pack |

### 7.5 Suppression Results

None. Single pack; no suppression rules apply.

**Total suppressed: 0 | Net active: 152**

### 7.6 Duplicate Detection

Single pack — trivially no duplicates. All ACU- prefix IDs are unique within the pack.

### 7.7 Oracle Contamination Check

| Check | Result |
|---|---|
| No HCM- assumptions in output | ✓ |
| No ERP- assumptions in output | ✓ |
| No OCI- assumptions in output | ✓ |
| No OIC- assumptions in output | ✓ |
| No AMS- assumptions in output | ✓ |
| No EBS-SLA- or EBS-DRM- assumptions | ✓ |

**Clean isolation confirmed: 152 Acumatica assumptions only. No Oracle assumption contamination.**

### 7.8 Partner Status Governance Check

| Constraint | ACU-GEN-009 Content | Compliance |
|---|---|---|
| Partner tier | "Acumatica Gold Partner" | ✓ Correct |
| Prohibited phrase | Never "Gold Certified" | ✓ Enforced by Constraint 9 (BU-ACU-009) |
| POPIA disclosure | Mandatory per ACU constraint | ✓ Present in pack |

### 7.9 Key Governance Constraints Active in Output

| Constraint | Rule |
|---|---|
| PaySpace payroll only | Acumatica does not provide payroll in SA; PaySpace is the SOR |
| Parallel run excluded by default | SOW explicit inclusion required |
| Legacy data: opening balances + open items only | Historical transactions separately scoped |
| Hypercare: 4 weeks standard | Consistent with BeBanking (BU-BB-004) and Oracle standards |
| BeBanking Payroll H2H | Oracle EBS/Fusion only — never Acumatica payroll (Constraint 15) |

### 7.10 Missing Content

| Topic | Coverage |
|---|---|
| Core Financials, Distribution, Manufacturing | ACU-FIN, ACU-DIS, ACU-MAN sections — covered ✓ |
| PaySpace integration | ACU-PAY / ACU-INT — covered per BU-ACU-001 ✓ |
| POPIA compliance | ACU-GOV / POPIA sections — covered ✓ |
| OCI hosting (if requested) | Not in this test; OCI Pack adds 174 assumptions when triggered |
| AMS post-go-live support | Not in this test; AMS Pack adds 84 assumptions when triggered |

### 7.11 Manual Intervention Required

None.

### 7.12 Verdict

**PASS** — 152 assumptions; 0 suppressions; 0 duplicates; 0 Oracle contamination; partner status governance verified.

---

## 8. Triggered Rule Summary (All Tests)

| Rule | T1 EBS AMS | T2 HCM Suite | T3 OIC | T4 BeBanking | T5 Acumatica |
|---|---|---|---|---|---|
| Rule A — Base First | ✓ (ERP→others) | ✓ (HCM Base→modules) | N/A (1 pack) | ✓ (BB→OIC,AMS) | N/A (1 pack) |
| Rule B — Additive Only | ✓ | ✓ | N/A | ✓ | N/A |
| Rule C — No Duplication | ✓ (0 dupes) | ✓ (0 dupes) | ✓ | ✓ (0 dupes) | ✓ |
| Rule D — BOM Trigger | ✓ (6 packs) | ✓ (5 packs) | ✓ (1 pack) | ✓ (3 packs) | ✓ (1 pack) |
| Rule E — Exclusions | ✓ (3 packs) | ✓ (5 packs) | ✓ | ✓ (2 packs) | ✓ |
| Rule JRN-1 | N/A | ✓ (auto via HCM Base) | N/A | N/A | N/A |
| Rule S1 (AMS-INC-004) | ✓ TRIGGERED | N/A | N/A | NOT triggered (correct) | N/A |
| Rule S2 (SLA replacements) | ✓ TRIGGERED | N/A | N/A | N/A | N/A |
| Rule S3 (AMS-SLA-005) | ✓ TRIGGERED | N/A | N/A | N/A | N/A |
| Rule S4 (Overlay precedence) | ✓ TRIGGERED | N/A | N/A | N/A | N/A |
| EBS AMS exclusion | ✓ HCM Base excluded | N/A | N/A | N/A | N/A |
| OCI Rule OCI-1 | ✓ TRIGGERED | N/A | N/A | NOT triggered | N/A |

---

## 9. Suppression Validation Summary (All Tests)

| Test | Pack with Suppressions | Assumptions Suppressed | Net Effect |
|---|---|---|---|
| T1 | AMS Pack | 6 (INC-004, SLA-001, PRI-001/002/003, SLA-005) | All replaced by EBS overlay equivalents |
| T2 | None | 0 | N/A |
| T3 | None | 0 | N/A |
| T4 | None | 0 | AMS-INC-004 retained (Oracle Fusion SaaS context correct) |
| T5 | None | 0 | N/A |
| **Total** | | **6** | |

**Suppression rule S1 behaviour confirmed:** Fires only for EBS AMS pattern (Test 1); correctly does NOT fire for BeBanking + AMS with Fusion source (Test 4). Discriminant logic working correctly.

---

## 10. Duplicate Detection Results (All Tests)

No ID-level duplicates detected in any test. Structural analysis confirms:

| Prefix Set | Tests Using | Overlap Risk |
|---|---|---|
| HCM- (base) | T2 | None |
| REC-, LRN-, TLT-, COM- (HCM modules) | T2 | None — all distinct from HCM- base prefix |
| ERP- | T1 | None |
| OCI- | T1 | None |
| OIC- | T1, T3, T4 | None — same pack used; no cross-test collision |
| AMS- | T1, T4 | None |
| EBS-SLA-, EBS-DRM- | T1 only | None |
| BB- | T4 | None |
| ACU- | T5 | None |

**Root cause of zero duplicates:** The Assumption Library ID scheme assigns unique prefix codes per pack, preventing all ID-level collisions. Topic-level collisions remain a BU Lead responsibility (no structural mechanism to prevent — governance-layer concern only).

---

## 11. Missing Content Summary (All Tests)

| Gap | Affects | Severity | Status |
|---|---|---|---|
| Mining Charter / B-BBEE assumptions | T1 (EBS AMS) | Medium | Permanent manual handling unless future pack authored |
| KT / Onboarding assumptions | T1 (EBS AMS), T4 (BeBanking+AMS) | Low | Consistent across all AMS engagements; future pack opportunity |
| Multi-site / mine-site access | T1 (EBS AMS) | Low | Mining sector specific; future pack opportunity |
| No named BeBanking + AMS pattern | T4 | Low — Advisory only | Add to Section 3.4 at next Assembly Rules update |
| OCI Pack not included for OIC SaaS (T3) | T3 | Advisory | Correct for SaaS OIC; bid manager to assess per engagement |
| AMS-PAT-001 context (BeBanking) | T4 | Advisory | Contextual note; no suppression needed |

---

## 12. Pre-Flight Fixes Applied (WP17C)

Before executing regression tests, the following items from the WP17B limitations list were resolved:

| Item | Fix Applied |
|---|---|
| PACK_LOADER.md: HCM module pack counts were "—" | Updated with confirmed counts (Recruiting=54, Learning=37, Talent=31, Compensation=30); version fields corrected to v1.1 (WP16C) |
| PACK_LOADER.md: Acumatica and BeBanking counts were "—" | Updated with confirmed counts (Acumatica=152, BeBanking=117); approval event notes added |
| TENDER_ASSUMPTION_ASSEMBLY_RULES.md Section 3.5 "Draft" labels | Corrected to "Approved v1.0 — 2026-06-19 WP15F" in all 3 code blocks; document version updated v1.9 → v2.0 |

---

## 13. Pass/Fail Assessment

| Test | Result | Blockers | Advisories |
|---|---|---|---|
| T1 — ARM IT045 (EBS AMS Full Stack) | **PASS** | 0 | 3 open gaps (non-blocking) |
| T2 — Oracle HCM Full Suite | **PASS** | 0 | 0 |
| T3 — Oracle OIC Standalone | **PASS** | 0 | 1 (OCI/SaaS note) |
| T4 — BeBanking + OIC + AMS | **PASS** | 0 | 2 (AF-01 pattern gap; AF-02 AMS-PAT-001 context) |
| T5 — Acumatica Standalone | **PASS** | 0 | 0 |
| **Overall** | **ALL PASS** | **0** | **3** |

---

## 14. Readiness Assessment

### Assembly Engine Production Readiness Checklist

| Criterion | Status |
|---|---|
| All 5 archetype tests pass | ✅ |
| No manual assumption selection required in any test | ✅ |
| BOM resolution correct for all patterns | ✅ |
| Pack loading eligibility checks correct | ✅ |
| Suppression rules S1–S4 execute correctly | ✅ |
| Rule JRN-1 (Journey scope) validated | ✅ |
| EBS AMS exclusion (HCM Base) validated | ✅ |
| AMS-INC-004 suppression discriminant validated | ✅ |
| Zero ID-level duplicates across all tests | ✅ |
| Exclusions (-EXC-) included in all relevant tests | ✅ |
| Oracle contamination check for Acumatica | ✅ |
| Partner status governance check (Acumatica) | ✅ |
| PACK_LOADER registry complete with all counts | ✅ (fixed WP17C) |
| Section 3.5 code block labels current | ✅ (fixed WP17C) |
| Advisory findings are non-blocking | ✅ |

### Advisory Items for Next Development Cycle (WP17D or future BAU)

| # | Advisory | Priority | Action |
|---|---|---|---|
| AF-01 | Add named "BeBanking + OIC + AMS" pattern to Section 3.4 of Assembly Rules | Low | Add at next Assembly Rules update |
| AF-02 | Document AMS-PAT-001 context note for non-Oracle-SaaS engagements | Low | Add to RULE_PROCESSOR.md as advisory note |
| AF-03 | Add AMS KT/onboarding assumption pack (GAP-007) | Medium | Future pack authoring — priority after WP17D |
| AF-04 | Add multi-site / mine-access assumption pack (GAP-009) | Low | Future pack authoring |
| AF-05 | Add Mining Charter compliance assumption section (GAP-005) | Medium | Future pack authoring — needed before next mining sector AMS tender |

### Verdict

**Assembly Engine is PRODUCTION READY for assumption assembly.**

All five archetypes tested successfully. The engine handles:
- Multi-pack assemblies with overlays (EBS AMS Full Stack — 6 packs)
- Hierarchical base + module loading (HCM Full Suite — 5 packs)
- Standalone single-pack assemblies (OIC, Acumatica)
- Cross-product combinations (BeBanking + OIC + AMS)
- Suppression rules (6 correct suppressions in EBS AMS pattern)
- Exclusion rules (all -EXC- assumptions correctly included)
- Duplicate detection (0 duplicates across all tests)
- Isolation checks (no cross-product contamination)

**Recommendation: Proceed to WP17D — Inline Text Assembly.**  
WP17D should implement full assumption text extraction inline (not just IDs) and test the output against a live proposal section.

---

## 15. Files Modified (WP17C Pre-Flight)

| File | Change |
|---|---|
| `08_Commercial/Assembly_Engine/PACK_LOADER.md` | v1.0 → v1.1: HCM module counts confirmed (54/37/31/30); Acumatica (152) and BeBanking (117) counts confirmed; version fields corrected |
| `08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md` | v1.9 → v2.0: Section 3.5 code block labels corrected from "Draft" to "Approved v1.0 — 2026-06-19 WP15F" |

---

*WP17C — Assembly Engine Regression Test Suite v1.0 | 2026-06-22 | COMPLETE*  
*All 5 tests PASS. Assembly Engine PRODUCTION READY. Proceed to WP17D — Inline Text Assembly.*
