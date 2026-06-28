---
document_id: WP15E-EBS-DECISION-HARVEST-REPORT
title: "WP15E — EBS AMS Overlay Decision Harvest Report"
version: "1.0"
status: "Final"
created: "2026-06-19"
created_by: "WP15E — EBS AMS Overlay Decision Harvest"
input_overlay_sla: "EBS_AMS_SLA_OVERLAY_V1.md (52 assumptions; 4 pending decisions)"
input_overlay_drm: "EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md (62 assumptions; 5 pending decisions)"
total_decisions: 9
category_a_email: 6
category_b_commercial: 1
category_c_workshop: 2
workshop_target_minutes: 15
---

# WP15E — EBS AMS Overlay Decision Harvest Report

**Date:** 2026-06-19 | **Programme:** WP15E — EBS AMS Overlay Decision Harvest

---

## 1. Objective

Classify all 9 EBS AMS overlay governance decisions into the fastest possible approval pathway, reducing the burden on BU Lead and Commercial Director time while ensuring each decision receives the right level of deliberation. The goal is to establish the earliest credible promotion path for both overlay packs to Approved v1.0.

---

## 2. Decision Inventory and Classification

### 2.1 Classification Framework

| Category | Label | Criteria | Approver |
|---|---|---|---|
| A | Email Approval | Decision is binary or has a clear recommended position; no live deliberation required; BU Lead can confirm in writing | EBS BU Lead |
| B | Commercial Director Review | Decision has direct margin, pricing, or contractual liability implications; CD can assess and respond independently | Commercial Director |
| C | Workshop — Joint Session | Decision requires real-time deliberation between BU Lead AND Commercial Director because operational feasibility (BU Lead) and commercial structuring (CD) are interdependent; email alone would produce an incomplete or misaligned answer | EBS BU Lead + Commercial Director |

### 2.2 Classification Summary

| Decision ID | Title | Category | Route | Rationale |
|---|---|---|---|---|
| EBS-SLA-BU-001 | P1 15-min response — EBS AMS standard or client-configurable? | **A** | Email | Binary positioning choice; BU Lead knows operationally whether 15 min is a default commitment or a per-engagement negotiation; clear recommended position |
| EBS-SLA-BU-002 | Resolution time SLAs — default offering or on explicit client request? | **C** | Workshop | Requires BU Lead to confirm operational feasibility (P1=2hr resolve achievable?) AND CD to assess liability exposure; answers are interdependent — if BU Lead says operationally achievable, CD decides whether to commercialise as default |
| EBS-SLA-BU-003 | 24/7 on-call commercial structure — fixed/per-callout/hybrid? | **C** | Workshop | Requires BU Lead to confirm staffing model (roster, coverage cost, capacity impact) AND CD to set commercial pricing; neither party can decide in isolation |
| EBS-SLA-BU-004 | Service credits — standard option or negotiated-only? | **B** | Commercial Director | Pure commercial liability decision; CD determines credit exposure cap and trigger conditions independently; BU Lead input not required for this decision |
| EBS-DRM-BU-001 | ARM IT045 hours model — EBS AMS DRM standard or per-engagement? | **A** | Email | Operational staffing model question; BU Lead knows whether the ARM IT045 team profile (SDM 40h + HCM 240h + Finance 160h + DBA 160h + OIC 80h) is consistently what EBS AMS clients require, or whether it varies; clear recommended position (per-engagement) |
| EBS-DRM-BU-002 | Unused minimum hours — roll over or forfeit? | **A** | Email | Commercial retainer model question; recommended position (forfeit) is the professional services industry standard and the BU Lead can confirm; no CD input required unless rollover is preferred |
| EBS-DRM-BU-003 | Illness absorption (3 days/month) + advance leave notice (10 BD) — confirm as standard? | **A** | Email | HR/operational policy confirmation; BU Lead confirms whether the proposed limits are workable for the EBS AMS team; no ambiguity — answer is confirm or adjust |
| EBS-DRM-BU-004 | Substitution notice period (30 BD) + equivalent-grade definition — confirm? | **A** | Email | HR/delivery policy confirmation; BU Lead confirms 30 BD notice as the minimum and provides the equivalent-grade definition (role band or competency profile); no CD input required |
| EBS-DRM-BU-005 | 30-day KT period + runbook obligation — standard in all DRM or on request? | **A** | Email | Delivery model standard; BU Lead confirms whether KT and runbook creation are always included (recommended) or only on client request; no CD input required |

---

## 3. Detailed Classification Rationale

### EBS-SLA-BU-001 — Category A (Email)

**Why email is sufficient:** The P1 response target positioning is an operational and market-positioning decision. The BU Lead knows whether APPSolve's on-call capability can reliably guarantee a 15-minute acknowledgement across all EBS AMS engagements, or whether it depends on the client's contracted coverage model (business hours vs 24/7). The recommended position — "client-configurable, defined in the AMS agreement schedule" — is conservative and correct for the majority of EBS AMS tenders. The BU Lead either confirms this or states that 15 minutes is the APPSolve EBS AMS default.

**No CD involvement needed:** P1 response time is an operational commitment, not a financial one. Service credits (the financial consequence of missing response SLAs) are addressed separately in EBS-SLA-BU-004.

---

### EBS-SLA-BU-002 — Category C (Workshop)

**Why live discussion is required:** Resolution time commitments (P1=2hr, P2=4hr) are the most commercially consequential positions in the SLA overlay. Two separate assessments must align:

1. **BU Lead must assess:** Is a 2-hour P1 resolution achievable across all EBS AMS engagements? What percentage of EBS P1 incidents can APPSolve genuinely resolve within 2 hours? Where does Oracle SR dependency make this promise dangerous (e.g., EBS bugs requiring an Oracle fix)?

2. **CD must assess:** If resolution SLAs are offered as default, what is the financial exposure when a resolution SLA is missed and service credits apply? Is the service credit exposure bounded by the cap in EBS-SLA-BU-004, or does it open APPSolve to penalty claims?

These two assessments interact: if the BU Lead assesses that resolution SLAs are achievable with acceptable Oracle SR carve-out terms, the CD may be willing to include them as default. If the BU Lead identifies a high miss rate, the CD may insist on "on-request only" to limit exposure. A sequential email process (BU Lead answers first, then CD reviews BU Lead's answer) would work but would delay the outcome by two email cycles. A joint 10-minute discussion resolves this in one session.

**Workshop: 10 minutes** (see agenda document).

---

### EBS-SLA-BU-003 — Category C (Workshop)

**Why live discussion is required:** The 24/7 on-call commercial structure requires APPSolve to define both the staffing model and the price simultaneously.

1. **BU Lead must answer:** How is the 24/7 on-call roster structured for EBS AMS? Is it a dedicated on-call resource with a fixed monthly cost to APPSolve, or is it a shared roster across multiple clients? What is APPSolve's internal cost of maintaining an EBS AMS on-call resource?

2. **CD must answer:** Given the BU Lead's cost model, what should the client-facing price be? Is it a fixed monthly on-call premium (absorbed into the DRM monthly fee), a separate on-call line item, or a per-callout charge for actual activations?

Without the BU Lead's cost structure, the CD cannot set an appropriate market price. Without the CD's commercial framework, the BU Lead cannot commit to what the EBS overlay assumes. A joint discussion where BU Lead explains the staffing cost and CD sets the commercial price is the only efficient path.

**Workshop: 10 minutes** (see agenda document).

---

### EBS-SLA-BU-004 — Category B (Commercial Director)

**Why CD-only is sufficient:** Service credit structures are a pure commercial liability decision. The CD sets: (a) whether to offer credits at all; (b) the credit percentage per SLA breach; (c) the monthly cap as a percentage of AMS fee; (d) the trigger threshold (number of breaches required before credits apply). None of these require BU Lead operational input — they are pricing and liability decisions. BU Lead awareness of the final position is required, but BU Lead deliberation is not.

**No workshop needed:** CD can review the options in the commercial review pack, confirm the position, and the BU Lead is notified of the outcome.

---

### EBS-DRM-BU-001 through EBS-DRM-BU-005 — Category A (Email)

All five DRM decisions share the same characteristic: they are operational confirmation questions with a clear recommended position. The BU Lead either confirms the recommendation or provides an adjusted position. None requires the CD or live discussion:

- **BU-001 (hours model):** Is the ARM IT045 team profile the standard or a per-engagement design? Recommended: per-engagement. BU Lead confirms or overrides.
- **BU-002 (unused hours):** Rollover or forfeit? Recommended: forfeit. This is a billing model question the BU Lead can confirm independently.
- **BU-003 (illness absorption):** 3 days/month threshold and 10 BD leave notice. Recommended: confirm as stated. BU Lead validates against HR policy.
- **BU-004 (substitution notice):** 30 BD notice and equivalent-grade definition. Recommended: confirm 30 BD; grade = same EBS module domain and role band. BU Lead validates operationally.
- **BU-005 (KT + runbook):** Always standard. Recommended: standard. BU Lead confirms.

---

## 4. Route Summary by Approver

### Category A — EBS BU Lead (email, 6 decisions)
> **Deliverable:** `WP15E_EBS_EMAIL_APPROVAL_PACK.md`

| # | ID | Decision question |
|---|---|---|
| 1 | EBS-SLA-BU-001 | P1 15-min response — standard or configurable? |
| 2 | EBS-DRM-BU-001 | ARM IT045 hours model — standard or per-engagement? |
| 3 | EBS-DRM-BU-002 | Unused hours — rollover or forfeit? |
| 4 | EBS-DRM-BU-003 | Illness absorption (3 days) + leave notice (10 BD) — confirm? |
| 5 | EBS-DRM-BU-004 | Substitution notice (30 BD) + equivalent grade — confirm? |
| 6 | EBS-DRM-BU-005 | KT + runbook — standard or on-request? |

### Category B — Commercial Director (written review, 1 decision)
> **Deliverable:** `WP15E_EBS_COMMERCIAL_REVIEW_PACK.md`

| # | ID | Decision question |
|---|---|---|
| 1 | EBS-SLA-BU-004 | Service credits — standard option or negotiated-only? |

### Category C — Joint Workshop (BU Lead + CD, 2 decisions)
> **Deliverable:** `WP15E_EBS_REDUCED_WORKSHOP_AGENDA.md`

| # | ID | Decision question |
|---|---|---|
| 1 | EBS-SLA-BU-002 | Resolution time SLAs — default or on client request? |
| 2 | EBS-SLA-BU-003 | 24/7 on-call commercial structure |

---

## 5. Promotion Path

### 5.1 Critical Path

The Category C workshop (EBS-SLA-BU-002 + EBS-SLA-BU-003) is the rate-limiting step because it requires scheduling both BU Lead and Commercial Director simultaneously. All other decisions can proceed in parallel before the workshop.

```
Day 0:     Dispatch Email Approval Pack to EBS BU Lead (6 decisions)
           Dispatch Commercial Review Pack to Commercial Director (1 decision)

Day 1–5:   EBS BU Lead responds to 6 email decisions
           Commercial Director reviews EBS-SLA-BU-004

Day 5–7:   Schedule 15-min joint workshop (EBS BU Lead + Commercial Director)
           Prerequisite: Category A email responses received (BU Lead context for workshop)

Day 7–10:  Hold 15-min workshop (EBS-SLA-BU-002 + EBS-SLA-BU-003)

Day 10–12: AI applies all 9 decisions to EBS_AMS_SLA_OVERLAY_V1.md and
           EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md

Day 12–14: BU Lead confirms implementation; sets approved_for_reuse: true
           Both overlays promoted to Approved v1.0

EARLIEST PROMOTION DATE: 14 calendar days from Day 0
REALISTIC PROMOTION DATE: 10–15 business days from Day 0
```

### 5.2 What Changes at Promotion

| Pack | Pre-promotion | Post-promotion |
|---|---|---|
| EBS_AMS_SLA_OVERLAY_V1.md | Draft — 4 decisions pending; cannot be assembled in external proposals | Approved v1.0 — available for EBS AMS tenders with enhanced SLA requirements |
| EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md | Draft — 5 decisions pending; cannot be assembled in external proposals | Approved v1.0 — available for EBS AMS tenders with dedicated resource model |

### 5.3 What Cannot Change at Promotion

Per WP15D constraints — no modifications to approved packs:
- `AMS_ASSUMPTIONS_V1.md` remains unchanged
- All approved packs remain unchanged
- No modifications to assumptions based on promotion (only frontmatter + governance updates)

### 5.4 Parallel vs Sequential

All Category A decisions (email) can be sent and responded to in parallel. There is no interdependency between BU-001 through BU-005 (DRM decisions) — they can all be approved in a single BU Lead email reply.

EBS-SLA-BU-001 (SLA response standard vs configurable) is also independent of EBS-SLA-BU-002 and EBS-SLA-BU-003 — it can be resolved by email before the workshop.

The only sequential dependency is: the workshop discussion of EBS-SLA-BU-002 and EBS-SLA-BU-003 is more productive if the BU Lead has already confirmed EBS-SLA-BU-001 (the P1 response position), since that gives context for the resolution time discussion.

**Recommended sequence:**
1. Email all 6 Category A decisions on Day 0 with a 5-business-day reply deadline
2. Send Category B (CD review) on Day 0 with a 5-business-day reply deadline
3. Schedule workshop for Day 7 (to allow BU Lead email responses first)
4. Hold workshop Day 7 with EBS-SLA-BU-001 already resolved

---

## 6. Validation Checks

| Check | Result | Notes |
|---|---|---|
| All 9 decisions classified | **PASS** | 6A + 1B + 2C = 9 |
| No assumption changes proposed | **PASS** | Classification only; no pack modifications |
| No decision resolutions | **PASS** | Findings only — no resolutions recorded |
| Workshop target 15–20 min achieved | **PASS** | 2 decisions × 7.5 min each = 15 min workshop |
| Promotion path defined | **PASS** | 14 calendar days from Day 0 (optimistic); 10–15 BD realistic |
| Deliverables match task specification | **PASS** | 4 files: this report + email pack + commercial pack + workshop agenda |

---

*WP15E EBS Decision Harvest Report v1.0 | 2026-06-19 | WP15E — EBS AMS Overlay Decision Harvest*
*9 decisions: 6 Category A (email) + 1 Category B (CD review) + 2 Category C (workshop)*
*Earliest promotion: 14 calendar days | Next: dispatch email pack + CD pack + schedule workshop*
