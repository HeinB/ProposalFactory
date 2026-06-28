---
title: BeBanking Base Assumption Pack — Gap Report
version: v1.2-Approved
status: Approved — Pack Promoted v1.0 WP14F
pack_code: BB
date: 2026-06-18
---

# BeBanking Base Assumption Pack — Gap Report

**Pack:** BB | **Sections:** 140–153 | **Date:** 2026-06-16 | **Status:** Approved v1.0 — WP14F 2026-06-18

> **WP14F (2026-06-18):** Pack promoted to Approved v1.0. All governance decisions resolved. GAP-BB-001 fully resolved (BU-BB-002 confirmed WP14E + WP14F). All governance blockers cleared. Remaining gaps (GAP-BB-003, GAP-BB-004, GAP-BB-007 through GAP-BB-011) are operational improvement items — they do not block proposal use.

---

## Gap Classification

| Priority | Description |
|---|---|
| CRITICAL | Missing information that blocks safe use of the pack in any proposal |
| HIGH | Material gap that creates proposal risk, delivery ambiguity, or commercial exposure |
| MEDIUM | Gap that reduces pack precision or requires manual handling in proposals |
| RESEARCH | Factual question requiring BU or platform confirmation before the assumption can be finalised |

---

## CRITICAL Gaps

### GAP-BB-001 — BeBanking Commercial Pricing Model Not Documented

**Status:** FULLY RESOLVED (WP14F 2026-06-18) — BU-BB-003 resolved WP14D; BU-BB-002 confirmed WP14E + WP14F: fixed-price Change Request per BeBanking Bank Addition SOW Schedule.

**Gap:** The BeBanking subscription pricing model — subscription tiers, transaction volume thresholds, per-payment-type pricing, and per-bank pricing — is not documented anywhere in the Knowledge Base. BB-GEN-008 and BB-EXT-008 reference the commercial schedule but no commercial schedule exists as a KB artefact.

**WP14D resolution:** BU-BB-003 resolved — forex partners confirmed as Citi Bank UK, ABSA, Nedbank, FNB. BB-FX-002 updated.

**WP14E + WP14F resolution:** BU-BB-002 confirmed — new bank onboarding post-go-live = fixed-price Change Request per BeBanking Bank Addition SOW Schedule. BB-EXT-008 and BB-SUP-006 locked. Decision paper: WP14E_BU_BB_002_DECISION_PAPER.md.

**Impact:** All commercial pricing gaps for bank additions are now resolved.

**Owner:** Commercial Director + BeBanking BU Lead

**Recommended action:** BeBanking BU Lead to publish BeBanking Bank Addition SOW Schedule (effort ranges by bank type) for presales use. This is an operational action and does not block proposal assembly.

---

### GAP-BB-002 — BeBanking Support SLA Not Confirmed

**Status:** RESOLVED (WP14D 2026-06-18)

**Gap:** BU-BB-006 (post-go-live support model) was a pending BU decision. The BeBanking support SLA and whether support is included in the subscription were unconfirmed.

**WP14D resolution:** BU-BB-006 resolved via BU Lead Master Review. Post-go-live support is confirmed as included in the BeBanking subscription. BB-SUP-001 updated; BU-BB-006 tag removed. BB-SUP-004 retains standard SLA tiers (P1=1h / P2=4h / P3=1bd / P4=3bd) which are confirmed as applicable. No further action required for this gap.

**Owner:** BeBanking BU Lead + Commercial Director

**Recommended action:** None — resolved. If a distinct BeBanking-specific SLA schedule ever differs from standard AMS SLA tiers, update BB-SUP-004 at that time.

---

## HIGH Gaps

### GAP-BB-003 — Bank-by-Bank File Format Specifications Not in KB

**Gap:** BB-BNK-008 assumes that APPSolve implements BeBanking to the bank's published specification at the time of onboarding. However, no bank-by-bank payment file format register exists in the KB. Each supported bank has different payment file layouts, statement file layouts, and acknowledgement file formats.

**Impact:** Without a format register, APPSolve cannot confirm the actual effort level for each bank during estimation. Different bank formats may have materially different implementation complexity. Estimation errors drive commercial risk.

**Owner:** BeBanking BU Lead / BeBanking technical team

**Recommended action:** Create a BeBanking Bank Format Register documenting the payment file specification for each of the 9 supported banks. Minimum: list file format type (fixed-width, CSV, XML, ISO 20022), bank-side connectivity type (SFTP, API), and relative implementation complexity (Low/Medium/High) per bank.

---

### GAP-BB-004 — Account Verification Service (AVS) Per-Bank Availability Unknown

**Gap:** BB-PAY-004 and BB-EXT-003 reference AVS but the KB does not confirm which of the 9 supported banks offer AVS and at what per-transaction cost. At least one of the international banks (Santander Chile) may not offer SA-style AVS.

**Impact:** Proposals to clients banking with non-AVS banks that include an AVS assumption are factually incorrect. This is a payment fraud control gap that clients may rely on.

**Owner:** BeBanking BU Lead / BeBanking technical team

**Recommended action:** BeBanking BU Lead to confirm AVS availability for each supported bank and note this in the Bank Format Register (GAP-BB-003). Update BB-PAY-004 if AVS availability list can be confirmed for the KB.

---

### GAP-BB-005 — BeBanking Disaster Recovery RTO/RPO Not Confirmed

**Status:** RESOLVED BY DELETION (WP14D 2026-06-18)

**Gap:** BB-ENV-006 asserted DR capability without confirmed RTO/RPO targets. BU-BB-010 flagged DR testing inclusion as a pending decision.

**WP14D resolution:** BU-BB-010 resolved via BU Lead Master Review by DELETING BB-ENV-006 from the pack. DR capability is no longer asserted in any assumption in this pack. This eliminates the risk of an unconfirmed DR commitment appearing in proposals. When BeBanking DR RTO/RPO is formally confirmed, a new BB-ENV-006 assumption may be re-introduced.

**Owner:** BeBanking BU Lead / APPSolve infrastructure team

**Recommended action:** None required for this gap at this time. When APPSolve formally documents its BeBanking DR RTO/RPO commitments, the BU Lead should author a new DR assumption and register it in this pack.

---

### GAP-BB-006 — Multi-Country Implementation Patterns Undefined

**Status:** RESOLVED (WP14D 2026-06-18)

**Gap:** No defined implementation pattern existed for multi-country BeBanking deployments. BU-BB-007 was pending.

**WP14D resolution:** BU-BB-007 resolved via BU Lead Master Review. Namibia is confirmed as separately scoped. BB-BNK-009 updated; BU-BB-007 tag removed. Standard position: single-country SA is standard scope; Namibian and other CMA country banking always requires a separately scoped onboarding engagement. This eliminates the scoping ambiguity.

**Owner:** BeBanking BU Lead

**Recommended action:** None required for proposal use. If a formal multi-country deployment architecture note is needed for a specific opportunity, the BeBanking BU Lead should author it at that time.

---

## MEDIUM Gaps

### GAP-BB-007 — Bank Sandbox Environment Availability Not Confirmed Per Bank

**Gap:** BB-ENV-002 states that the UAT environment uses bank sandbox connectivity where available. Not all SA banks offer dedicated sandbox or test environments for H2H payment testing. Where no sandbox is available, testing uses controlled live transactions in a bank-approved test window — which is higher risk.

**Impact:** Proposals and project plans that assume sandbox testing will be faster or lower risk may be inaccurate for banks without sandbox facilities. This affects testing timeline and approach.

**Owner:** BeBanking BU Lead / BeBanking technical team

**Recommended action:** BeBanking BU Lead to confirm which supported banks offer sandbox environments and document this per-bank in the Bank Format Register (GAP-BB-003).

---

### GAP-BB-008 — BeBanking Version/Release History and Current Version Not in KB

**Gap:** The KB does not document which BeBanking platform version is current, what the release cadence is, or what the upgrade approach is for existing clients. BB-ENV-005 documents the update process but does not describe the release model.

**Impact:** Without version knowledge, compatibility claims and upgrade timeline assumptions cannot be validated. Proposals for clients upgrading from older BeBanking versions cannot be accurately scoped.

**Owner:** BeBanking BU Lead / APPSolve development team

**Recommended action:** Register current BeBanking platform version and release model in the KB. Minimum: current major version, minor release cadence (quarterly? monthly?), and major upgrade frequency.

---

### GAP-BB-009 — OCI Migration Pattern for BeBanking Not Documented

**Gap:** BB-ENV-008 notes that OCI-hosted BeBanking deployments are governed by the OCI Pack. However, no defined BeBanking OCI migration pattern exists — specifically the approach for migrating an existing AWS-hosted BeBanking instance to OCI. Some clients may require this as part of a broader OCI consolidation programme.

**Impact:** Without a defined migration pattern, OCI migration proposals for BeBanking clients may be incorrectly scoped. Conversely, clients may not know this option is available.

**Owner:** BeBanking BU Lead + OCI team (WP11H)

**Recommended action:** BeBanking BU Lead and OCI team to define the BeBanking OCI migration approach, even at a high level. This can be a short-form Architecture Note rather than a full assumption pack addition.

---

## RESEARCH Gaps

### GAP-BB-010 — SARB BoP Category Mapping for BeBanking Forex

**Gap:** BB-FX-006 states that SARB Balance of Payments (BoP) category declarations are the client's responsibility. The exact BoP categories relevant to different BeBanking forex payment types (supplier payments, intercompany forex, forex payroll disbursements) are not documented in the KB.

**Impact:** Without a BoP category reference, BeBanking consultants cannot guide clients on SARB forex documentation requirements during onboarding. This may result in SARB non-compliance by clients who are not aware of their BoP obligations.

**Owner:** BeBanking BU Lead / forex banking partners (Citi UK / Santander Chile)

**Research question:** What are the applicable SARB BoP categories for (a) international supplier EFT payments; (b) intercompany forex disbursements; (c) cross-border payroll disbursements? Should BeBanking onboarding include a SARB BoP documentation guide as a standard client deliverable?

---

### GAP-BB-011 — BeBanking API Specification Versioning Policy

**Gap:** BB-INT-010 states that BeBanking API version changes are communicated 60 days before deprecation. The 60-day figure is a reasonable default but has not been confirmed as the actual APPSolve BeBanking API versioning policy.

**Impact:** If the actual notice period is shorter (e.g., 30 days) and proposals state 60 days, APPSolve may be in breach of a proposal commitment. If the actual period is longer, 60 days is conservative.

**Owner:** BeBanking BU Lead / APPSolve development team

**Research question:** What is the confirmed BeBanking API versioning and deprecation notice policy? Has this been documented in any client agreements? Update BB-INT-010 once confirmed.

---

### GAP-BB-012 — Non-Oracle Payroll Source Integration Technical Feasibility

**Status:** RESOLVED (WP14D 2026-06-18)

**Gap:** Technical feasibility of non-Oracle payroll integration was unconfirmed. BU-BB-008 was pending.

**WP14D resolution:** BU-BB-008 resolved via BU Lead Master Review. PaySpace integration confirmed as technically feasible and supported. BB-PYR-002 updated to list Oracle EBS Payroll and PaySpace as the two confirmed supported payroll sources. Other payroll systems (including Acumatica) remain prohibited or require separate assessment. BU-BB-008 tag removed.

**Owner:** BeBanking BU Lead / BeBanking technical team

**Recommended action:** None required. If other non-Oracle/non-PaySpace payroll systems are assessed in future, a new BU decision and BB-PYR assumption amendment will be needed.

---

## Gap Summary

| Priority | Count | IDs |
|---|---|---|
| CRITICAL | 2 | GAP-BB-001, GAP-BB-002 |
| HIGH | 4 | GAP-BB-003, GAP-BB-004, GAP-BB-005, GAP-BB-006 |
| MEDIUM | 3 | GAP-BB-007, GAP-BB-008, GAP-BB-009 |
| RESEARCH | 3 | GAP-BB-010, GAP-BB-011, GAP-BB-012 |
| **Total** | **12** | |

---

## BU Lead Review Items Aligned to Gaps

| Gap | BU Decision | Status | Dependency |
|---|---|---|---|
| GAP-BB-001 | BU-BB-002 | RESOLVED WP14F | Fixed-price CR confirmed per BeBanking Bank Addition SOW Schedule |
| GAP-BB-001 | BU-BB-003 | RESOLVED WP14D | Forex bank list confirmed (Citi Bank UK, ABSA, Nedbank, FNB) |
| GAP-BB-002 | BU-BB-006 | RESOLVED WP14D | Support model confirmed — included in subscription |
| GAP-BB-003 | BU-BB-001 | RESOLVED WP14D | Supported bank list confirmed; Bank Format Register still recommended |
| GAP-BB-005 | BU-BB-010 | RESOLVED BY DELETION WP14D | BB-ENV-006 deleted; DR no longer asserted |
| GAP-BB-006 | BU-BB-007 | RESOLVED WP14D | Namibia confirmed as separately scoped |
| GAP-BB-012 | BU-BB-008 | RESOLVED WP14D | PaySpace + Oracle EBS confirmed as supported payroll sources |

---

*BeBanking Base Assumption Pack Gap Report v1.2-Approved | WP11J + WP14F | 2026-06-18*
