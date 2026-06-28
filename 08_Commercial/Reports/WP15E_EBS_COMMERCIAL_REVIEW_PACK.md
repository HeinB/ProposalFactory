---
document_id: WP15E-EBS-COMMERCIAL-REVIEW-PACK
title: "WP15E — EBS AMS Overlay: Commercial Review Pack (Category B Decision)"
version: "1.0"
status: "Awaiting Commercial Director Response"
created: "2026-06-19"
created_by: "WP15E — EBS AMS Overlay Decision Harvest"
decisions_included: 1
decision: "EBS-SLA-BU-004 — Service Credits"
approver: "Commercial Director"
reply_deadline: "5 business days from dispatch"
---

# WP15E — EBS AMS Overlay: Commercial Review Pack

**To:** Commercial Director
**From:** APPSolve Tender Factory (WP15E)
**Subject:** EBS AMS Overlay — Commercial Governance Decision: Service Credits
**Reply deadline:** 5 business days

**CC for awareness:** EBS BU Lead (no input required for this decision)

---

## Purpose

One EBS AMS overlay governance decision requires Commercial Director resolution. It is separated from the BU Lead email pack because it involves direct financial liability exposure rather than an operational or delivery policy question.

This document provides the full commercial analysis you need to make the decision. No supplementary documents are required.

---

## Decision: EBS-SLA-BU-004

**Decision ID:** EBS-SLA-BU-004
**Pack:** EBS AMS SLA Overlay
**Assumptions affected:** EBS-SLA-048 (service credit entitlement), EBS-SLA-049 (service credit exclusions), EBS-SLA-050 (service credit claim process)
**Priority:** HIGH — cannot promote EBS SLA overlay to Approved v1.0 without this decision

---

### Background

The EBS AMS SLA Overlay introduces a 5-tier SLA with P1=15-minute response and, where contracted, P1=2-hour resolution. These are materially stronger SLA commitments than APPSolve's standard AMS pack (AMS-SLA-001: P1=1 hour, response only, no resolution commitment).

With stronger SLA commitments comes the question of remedy when those commitments are missed. The EBS SLA overlay currently includes three assumptions (EBS-SLA-048 through EBS-SLA-050) that define a service credit mechanism — but the commercial position (whether credits are offered at all, and on what terms) is marked as pending BU Lead decision.

This decision is re-routed to the Commercial Director because it is a financial liability question, not an operational one.

---

### Options Analysis

#### Option A — Service credits are never offered

**Position:** APPSolve does not offer financial service credits for EBS AMS SLA failures under any circumstances. SLA commitments are best-efforts obligations only.

| Dimension | Analysis |
|---|---|
| **Margin impact** | Zero direct financial exposure from service credits. No credit accrual risk. |
| **SLA liability** | SLA miss is acknowledged in monthly report; no financial remedy to client. |
| **Competitive position** | **Weakest.** EBS AMS tenders of the ARM IT045 type (enterprise, named resource, 24/7 P1) almost universally expect some form of SLA remedy. "No credits offered" may be a disqualifier in a competitive bid. |
| **Client risk** | Client has no financial incentive to care whether APPSolve misses P1. This weakens APPSolve's accountability in the client's eyes. |
| **Assumptions to update** | Delete EBS-SLA-048, 049, 050 from the overlay. |
| **Recommended?** | **No** |

---

#### Option B — Service credits are a standard line item in all EBS AMS proposals using the enhanced SLA overlay

**Position:** Every EBS AMS proposal assembled with the SLA Overlay automatically includes APPSolve's standard service credit schedule. Credits apply where APPSolve misses contracted P1 or P2 SLAs.

**Proposed standard credit schedule (for CD review and confirmation):**

| Priority | Missed commitment | Credit per breach | Monthly cap |
|---|---|---|---|
| P1 Response (15-min) | APPSolve fails to respond within 15 minutes | 2% of monthly AMS fee | Capped at 10% of monthly fee across all P1 response breaches |
| P1 Resolution (2-hr) | APPSolve fails to resolve within 2 hours (where resolution SLAs contracted) | 3% of monthly AMS fee | Included in 10% monthly cap |
| P2 Response (1-hr) | APPSolve fails to respond within 1 hour | 1% of monthly AMS fee | Capped at 5% of monthly fee across all P2 breaches |
| **Overall monthly cap** | | | **15% of monthly AMS fee** — credits cannot exceed this regardless of breach count |

| Dimension | Analysis |
|---|---|
| **Margin impact** | **Moderate exposure.** At a monthly AMS fee of R200,000, the maximum credit exposure is R30,000/month (15% cap). In a well-run EBS AMS engagement, P1 breaches should be rare (target: zero per quarter). The credit risk is primarily a discipline tool, not a major financial exposure, PROVIDED the SLA clock pause rules (EBS-SLA-031–034) are correctly implemented. Oracle SR delays and client dependency pauses must be rigorously tracked. |
| **SLA liability** | Clear, bounded. Client knows exactly what remedy they receive. APPSolve's exposure is capped. |
| **Competitive position** | **Strongest.** Service credits demonstrate APPSolve's confidence in its SLA commitments. |
| **Exclusion conditions** | Credits do NOT apply where: Oracle SR is the blocking dependency; client failed to provide access; client failed to respond to escalation within required window; force majeure. These exclusions must be rigorously applied via EBS-SLA-049. |
| **Assumptions to update** | EBS-SLA-048: populate credit percentages (2%/3%/1%) and monthly cap (15%); EBS-SLA-049: confirm exclusion list; EBS-SLA-050: confirm claim process (10-day claim window; 5-day review). |
| **Recommended?** | **Partial** — recommended as the **competitive default** for large EBS AMS tenders (monthly fee > R150,000). Not recommended as universal default for all EBS AMS. |

---

#### Option C — Service credits are negotiated per engagement (no standard schedule)

**Position:** APPSolve does not publish a standard service credit schedule. Where a client requests credits in their RFP or tender, APPSolve's Commercial Director negotiates terms on a per-engagement basis.

| Dimension | Analysis |
|---|---|
| **Margin impact** | **Low and controlled.** Credits are only accepted where the CD approves the specific terms. No risk of inadvertently committing to unfavourable credit terms via standard pack. |
| **SLA liability** | Flexible. APPSolve can offer stronger credits for premium engagements and decline for smaller ones. |
| **Competitive position** | **Moderate.** APPSolve can offer credits when needed to win, without committing to them universally. |
| **Bid process impact** | Requires CD involvement in any EBS AMS RFP that requests service credits. Adds a step to the bid process for competitive tenders. |
| **Assumptions to update** | EBS-SLA-048 is updated to state that service credits are available "where specifically included in the AMS agreement on terms agreed with the client." EBS-SLA-049 and EBS-SLA-050 retain the general credit structure as a template but are marked "applicable only where service credits are included in the AMS agreement." |
| **Recommended?** | **Yes — preferred position** |

---

### Recommended Position

**Option C — Negotiated per engagement** is recommended, with **Option B as the pre-approved template** for engagements where credits are agreed.

**Rationale:** APPSolve should retain the flexibility to offer credits when needed to win a competitive tender without being contractually obligated to offer them in all EBS AMS engagements. The service credit assumptions (EBS-SLA-048 through EBS-SLA-050) in the overlay provide the ready-made credit schedule that can be activated per engagement without further design work.

**Practical implementation:**

> When a client's RFP requests service credits:
> 1. EBS BU Lead requests CD approval before including credits in the proposal
> 2. CD approves the standard schedule (Option B) or negotiates modified terms
> 3. Approved schedule is included in the SOW or AMS agreement schedule
> 4. EBS-SLA-048 through 050 are included in the assembled proposal

> When a client's RFP does not request credits:
> 1. EBS-SLA-048 through 050 are not assembled into the proposal
> 2. The SLA overlay assumptions on response and resolution times are included without financial remedy

---

### SLA Liability Summary

The following table quantifies the financial exposure under Option B (standard schedule) at typical EBS AMS engagement sizes:

| Monthly AMS Fee | 15% Monthly Credit Cap | Annual Credit Exposure (if cap hit every month — worst case) |
|---|---|---|
| R100,000/month | R15,000/month | R180,000/year |
| R200,000/month (ARM IT045 approximate) | R30,000/month | R360,000/year |
| R350,000/month | R52,500/month | R630,000/year |

**Assessment:** At standard EBS AMS engagement sizes, the worst-case annual credit exposure (if the cap is hit every month — which would indicate a catastrophically under-performing engagement) represents less than 1 month's AMS fee. This is not a material existential risk for APPSolve. The greater risk is reputational: persistent P1 breaches that generate credits are a leading indicator of a client termination, which has a much larger revenue impact than the credits themselves.

---

### Service Credit Exclusions (Not Negotiable)

Regardless of the option selected, the following exclusions must always apply and are non-negotiable per APPSolve's operating model:

1. Oracle SR blocking (Oracle has not provided the required patch, fix, or resolution)
2. Client dependency pause (client has not provided access, approvals, or test environment in the required timeframe)
3. Force majeure
4. Client-initiated change that caused the incident
5. Client failure to activate the P1 emergency call procedure (did not call the emergency line)

These exclusions protect APPSolve from SLA liability for factors outside its direct control. They are already documented in EBS-SLA-049.

---

### Staffing and Capacity Commitment Note

Service credits are relevant only to the SLA overlay (EBS_AMS_SLA_OVERLAY_V1.md). The DRM overlay (EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md) does not include service credits — minimum hours commitments in the DRM are capacity commitments, not SLA commitments. No credit mechanism applies to DRM hours underspend (see EBS-DRM-035: APPSolve's obligations for illness absorption).

---

## CD Response Required

Please respond with one of the following:

**Option C (recommended):**
> "I confirm Option C for EBS-SLA-BU-004. Service credits are available on negotiated terms per engagement. EBS-SLA-048 through 050 in the overlay provide the template credit schedule for use when negotiated. CD approval required before including credits in any EBS AMS proposal."

**Option B (if preferred as universal standard):**
> "I confirm Option B for EBS-SLA-BU-004. Standard service credit schedule applies to all EBS AMS proposals using the SLA Overlay. Approved schedule: [confirm or modify the table above — credit percentages, monthly cap]."

**Option A (if credits are prohibited):**
> "I confirm Option A for EBS-SLA-BU-004. No service credits are offered. Delete EBS-SLA-048, 049, 050 from the SLA Overlay."

**Modified position (any variation):**
> "For EBS-SLA-BU-004, my position is: [state position]."

---

## Next Steps After CD Response

1. CD response is forwarded to the AI work package.
2. AI records the decision in DR_EBS-SLA-BU-004.md.
3. AI updates EBS-SLA-048 through EBS-SLA-050 in the SLA overlay to reflect the approved position.
4. Promotion proceeds after all 9 decisions are resolved (including BU Lead email responses and the workshop).

---

*WP15E EBS Commercial Review Pack v1.0 | 2026-06-19 | WP15E — EBS AMS Overlay Decision Harvest*
*1 Category B decision | Commercial Director approval required | Reply deadline: 5 business days*
*Decision: EBS-SLA-BU-004 — Service Credits | Pack: EBS_AMS_SLA_OVERLAY_V1.md*
