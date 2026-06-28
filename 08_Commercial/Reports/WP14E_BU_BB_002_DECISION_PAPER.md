---
title: WP14E — BU-BB-002 Decision Paper: New Bank Onboarding Fee Model Post-Go-Live
version: v1.0
status: Awaiting Decision
programme: WP14E — Resolve Final BeBanking Governance Decision
date: 2026-06-18
decision_id: BU-BB-002
decision_owner: BeBanking BU Lead + Commercial Director
target_date: 2026-07-07
pack_impact: BEBANKING_BASE_ASSUMPTIONS_V1.md (v1.1-Draft → v1.1-Approved or Approved v1.0)
---

# WP14E — BU-BB-002 Decision Paper

## New Bank Onboarding Fee Model Post-Go-Live

**Decision ID:** BU-BB-002  
**Owners:** BeBanking BU Lead + Commercial Director  
**Target:** 2026-07-07 (OVERDUE per Governance Approval Campaign — see §7)  
**Pack blocked:** BEBANKING_BASE_ASSUMPTIONS_V1.md cannot be promoted to Approved v1.0 until this decision is recorded.

---

## 1. Executive Summary

This decision paper supports BeBanking BU Lead and Commercial Director resolution of **BU-BB-002**: the commercial model that applies when an existing BeBanking customer requests connectivity to an additional bank after their initial go-live.

**The existing pack content implicitly supports Option A (always a Change Request)**. BB-EXT-008 positions post-go-live bank additions as separately scoped and priced. BB-SUP-006 classifies adding new banks as a Change Request. SB-BB-001 in the Scope Boundary Guide directs proposals to treat new bank additions as a separately scoped CR. The Governance Master Decision Register's own recommendation is Option A.

**However, no explicit BU Lead + Commercial Director sign-off exists on this position.** That is the only reason BU-BB-002 is still open. This paper exists to generate that sign-off.

**Recommended decision: Option A — Fixed-Price Change Request per bank addition, using a standard effort schedule published by the BeBanking BU Lead.**

> **Approval action required:** Review §5 (Options Analysis), confirm the recommended option in §5.5, and record the decision per §7.

---

## 2. Current State Analysis

### 2.1 Current Onboarding Approach

Bank connectivity setup is a material delivery activity. BB-GEN-007 describes the standard onboarding as a 6-phase sequential process:

1. Discovery and scoping
2. Platform configuration
3. Bank connectivity and format testing
4. ERP integration testing
5. User acceptance testing
6. Go-live cutover

Each phase requires written client sign-off before the next commences. Adding a bank post-go-live restarts this process for the new bank — specifically phases 3, and elements of phases 4 and 5. BB-BNK-003 documents that bank onboarding itself (the bank registration and certification process) takes **4–8 weeks from submission to confirmed production connectivity approval** — independent of APPSolve's delivery effort within that window.

**Typical delivery effort for a single post-go-live bank addition (estimated):**

| Activity | Effort |
|---|---|
| Bank onboarding assessment + discovery | 0.5–1 day |
| Bank registration and documentation support | 0.5 day |
| Format specification review and configuration | 1–3 days |
| SFTP/API connectivity setup and testing | 1–2 days |
| Payment file test cycle (bank sandbox or controlled window) | 1–2 days |
| UAT (client + APPSolve on-site or remote) | 0.5–1 day |
| Go-live sign-off and post-go-live monitoring | 0.5 day |
| **Total typical range** | **5–10.5 days** |

This places a typical single bank addition in the **Standard to Large CR category** per the CR Pricing Model (Standard = 1–5 days; Large = 5–20 days). It is never trivial. It cannot be absorbed into the support subscription without material margin erosion.

### 2.2 Current Commercial Treatment

The following assumptions currently treat post-go-live bank additions as separately billable:

| Assumption | Current Position |
|---|---|
| **BB-EXT-008** | Post-go-live bank additions are new onboarding engagements — separately scoped, assessed, and priced |
| **BB-SUP-006** | Adding new banks = Change Request; follows Commercial Framework CR process; billed at applicable rate |
| **BB-BNK-003** | Bank onboarding timeline 4–8 weeks; bank certification process is bank-controlled; APPSolve delivery effort is in addition |
| **BB-BNK-001** | Banks not on the supported list require a new bank onboarding assessment |

The Scope Boundary Guide (SB-BB-001) provides the client-facing standard response for this scenario: new bank connectivity after go-live is not included in standard scope; it requires a separate bank onboarding engagement as a CR.

### 2.3 Existing Customer Examples

No named client examples are available in the Knowledge Base for post-go-live bank additions. The KB does not document historical BeBanking engagement commercial terms. **The BeBanking BU Lead should confirm whether any post-go-live bank additions have been delivered to existing clients and on what commercial basis.**

If prior engagements exist:
- Were they billed as CRs at T&M rates?
- Were they included in the subscription as a goodwill gesture?
- Was there a fixed-price arrangement?

Any prior commercial precedent should inform the decision and the BU Lead should disclose it at the decision meeting.

### 2.4 Impact on Support Model

BB-SUP-001 confirms post-go-live support is included in the BeBanking subscription (resolved BU-BB-006). The support model covers:

- Application layer support (P1–P4 SLA)
- Bank-initiated like-for-like format changes (BB-SUP-007 — treated as support, not CR)
- Platform updates and patches (BB-SUP-008 — included in subscription)

**What is explicitly NOT support:**
- New bank connectivity (BB-EXT-008, BB-SUP-006)
- New payment types (BB-SUP-006)
- New ERP integration points (BB-SUP-006)
- Structural bank format changes (BB-SUP-007 — assessed as CR)

The support model is clean. Post-go-live bank additions are structurally distinct from support activities. This distinction is already embedded in the pack and is not in dispute.

---

## 3. Decision Definition

**Precise question:**

> When an existing BeBanking client has gone live and subsequently requests that APPSolve onboard an additional bank (i.e., establish new Host-to-Host connectivity, format specification work, connectivity testing, and UAT for a bank not included in the client's original implementation SOW), what is the commercial model that governs how APPSolve scopes and charges for that work?

**Scope of this decision:**

| In scope | Out of scope |
|---|---|
| Adding a bank not in the original implementation SOW after go-live | Adding a bank that WAS in the original SOW but was deferred (SOW-covered deferral) |
| Adding Namibian banking post-go-live (separately scoped per BU-BB-007) | Bank-initiated format changes to existing banks (BB-SUP-007 — support activity) |
| Adding a new forex banking partner post-go-live | Subscription tier amendment for transaction volumes |
| Adding a bank from APPSolve's supported list AND banks not yet on the supported list | Like-for-like bank connectivity upgrades (connectivity method change with same bank) |

**What is NOT in dispute:**

- That the work is real and involves APPSolve delivery effort — BB-BNK-003 and BB-GEN-007 confirm this
- That it is outside the initial SOW — BB-EXT-008 confirms this
- That it should not be free — no assumption suggests this; the open question is HOW it is charged, not WHETHER

---

## 4. Options Analysis

### Option A — Fixed-Price Change Request per Bank

**Description:** Every post-go-live bank addition is scoped and priced as a fixed-price Change Request. APPSolve publishes a standard bank onboarding effort schedule (by bank type: standard SA clearing bank, standard CMA bank, new/unsupported bank, international bank). The client receives a fixed price before approving. APPSolve bears effort risk within the estimate.

**Commercial impact:**
- Every bank addition generates revenue — no margin leakage
- Fixed-price gives clients certainty; no invoice surprises
- Effort schedule allows presales to quote consistently without waiting for BU assessment
- Standard SA clearing bank addition (known format, existing APPSolve tooling) = faster quote, lower risk
- New/unsupported bank = higher estimate + 10% risk allowance per CR Pricing Model

**Margin impact:** POSITIVE — full T&M equivalent recovery with effort risk absorbed into estimate; standard bank additions are well-understood; risk allowance covers variance.

**Delivery impact:**
- CR process follows Commercial Framework: CR form + scoping + fixed price + written client approval before work starts
- Standard delivery phases apply (BB-GEN-007 phases 3–5 as applicable)
- No delivery model change required

**Customer experience impact:**
- Client receives a clear, pre-agreed price before committing
- No ambiguity about what is included
- Predictable: clients can budget for bank additions in advance once they know the standard schedule

**Risks:**
- If actual effort significantly exceeds estimate for a complex new bank, APPSolve absorbs the difference (but 10% risk allowance should cover standard variance)
- Presales must be briefed on the standard effort schedule to quote correctly

**Assessment: RECOMMENDED** — aligns with existing pack assumptions (BB-EXT-008, BB-SUP-006); fits the CR Pricing Model; commercially clean; client-friendly; manageable from a presales perspective.

---

### Option B — T&M Bank Onboarding

**Description:** Every post-go-live bank addition is scoped as a CR but billed at actual hours/days worked at the applicable T&M rate. A capped estimate is provided upfront; actual billing is within the cap.

**Commercial impact:**
- Revenue generated per engagement
- Estimate cap required (per CR Pricing Model §6.2) — provides client a cost ceiling

**Margin impact:** POSITIVE to NEUTRAL — recovers actual effort; no margin risk on under-estimation; but requires accurate time recording and monthly billing administration.

**Delivery impact:**
- More administration than fixed-price: requires time-sheeting per bank onboarding engagement
- Monthly billing cycle creates latency between delivery and recognition

**Customer experience impact:**
- Less predictable for the client — final bill unknown until delivery is complete
- Some clients resist T&M for discrete, well-defined work items
- Capped T&M partially mitigates uncertainty but complicates billing

**Risks:**
- If the bank addition comes in under estimate, client may question why they were charged the cap
- T&M requires tighter time-recording discipline across the BeBanking delivery team

**Assessment:** VIABLE but inferior to Option A for a defined, repeatable activity. Reserve T&M for new/unsupported banks where effort is genuinely unpredictable.

---

### Option C — Included in Support Subscription

**Description:** Post-go-live bank additions are included in the BeBanking subscription — no additional charge. The subscription price implicitly covers this.

**Commercial impact:**
- Zero direct revenue from bank additions
- Creates a perverse incentive: clients defer bank additions from the implementation SOW to post-go-live to avoid project costs, then expect free additions under support
- Subscription would need to be repriced to reflect this inclusion — adding roughly 5–15 days of effort value per potential bank addition over the subscription term

**Margin impact:** HIGHLY NEGATIVE — absorbs 5–10 days of delivery effort per bank addition with no recovery mechanism. For clients with multiple planned bank additions, this could erase the entire AMS margin in Year 1.

**Delivery impact:**
- Unlimited obligation: if subscription includes bank additions, the client could theoretically request additions frequently
- No commercial control mechanism without introducing an explicit limit (which turns Option C into a tiered model — see Option D)

**Customer experience impact:** Clients value this — it is commercially generous — but it is not sustainable at APPSolve's delivery cost structure.

**Risks:** CRITICAL margin risk. Existing subscription pricing does not factor in this delivery obligation. Retroactive subscription repricing would be commercially complex and client-facing.

**Assessment: NOT RECOMMENDED** — commercially unviable without fundamental subscription repricing.

---

### Option D — Tiered Onboarding Model

**Description:** A tiered commercial model that distinguishes between:
- **Tier 1 (Standard SA Banks):** Banks already on APPSolve's supported bank list (ABSA, FNB, Nedbank, Standard Bank, Investec) — fixed-price CR at a published standard rate
- **Tier 2 (Forex/International Banks):** Citi Bank UK, ABSA Forex, Nedbank Forex, FNB Forex — fixed-price CR with a forex bank premium (SARB compliance documentation, different connectivity)
- **Tier 3 (New/Unsupported Banks):** Banks not currently on APPSolve's supported list — T&M CR with a capped estimate; higher risk allowance; BU Lead review required

**Commercial impact:**
- Predictable pricing for the most common scenarios (Tier 1)
- Accurate pricing for genuinely unpredictable scenarios (Tier 3)
- Revenue from all bank additions — no margin leakage

**Margin impact:** POSITIVE — each tier is priced to recover effort; Tier 1 is highest-margin (known effort, standard tooling); Tier 3 adds risk allowance proportional to uncertainty.

**Delivery impact:**
- Requires effort schedule publication per tier (BeBanking BU Lead to define)
- Tier classification at pre-sales stage is straightforward
- No fundamental delivery model change

**Customer experience impact:**
- More transparent than T&M
- Slightly more complex than a single fixed-price schedule (Option A)
- Clients understand tiering once explained — common in technology services

**Risks:**
- Requires tier definitions to be maintained as APPSolve's supported bank list evolves
- Tier 3 (T&M) still carries billing unpredictability

**Assessment:** VIABLE and more sophisticated than Option A — appropriate if the BU Lead wants to explicitly differentiate effort across bank types. Recommend as Option A+ if the BU Lead has reliable effort data per bank type. **If effort data is not yet available by bank type, start with Option A (flat fixed-price CR) and migrate to Option D once data accumulates.**

---

### 5.5 Recommendation Summary

| Option | Margin | Client Experience | Admin | Recommended? |
|---|---|---|---|---|
| A — Fixed-price CR | High | Excellent (certain price) | Low | **YES — PRIMARY** |
| B — T&M CR | Medium | Moderate | Medium | Fallback for Tier 3 |
| C — Included in subscription | Negative | Excellent (free) | Very Low | **NO** |
| D — Tiered fixed-price | High | Good | Medium | YES — if effort data exists |

---

## 5. Recommended Default

**Recommended: Option A — Fixed-Price Change Request per bank addition.**

Rationale:

1. **Consistent with existing pack content.** BB-EXT-008 and BB-SUP-006 already position this as a CR. Confirming Option A requires only finalising the exact commercial terms — no assumption rewriting required.

2. **Commercially sustainable.** Bank onboarding effort (5–10 days) is too material to absorb into the subscription. Option C destroys margin. Option A recovers full cost with a reasonable risk buffer.

3. **Client-friendly.** A fixed price before approval is a better client experience than T&M uncertainty. It also removes the approval friction of "how much will this cost?" — a common reason clients defer decisions.

4. **Presales-ready.** Publishing a standard effort schedule allows bid managers and Account Managers to quote bank addition costs in proposals without a BU assessment cycle per opportunity.

5. **Aligned with CR framework.** The CR Pricing Model supports fixed-price CRs with a 0–10% risk allowance. Standard bank additions fit the Standard CR category (1–5 days for known banks); complex additions fit the Large CR category (5–20 days for new banks).

**Recommended standard effort schedule (for BU Lead confirmation):**

| Bank Addition Type | Typical Effort | Pricing Model | Notes |
|---|---|---|---|
| Standard SA clearing bank (on supported list) | 5–8 days | Fixed-price CR | ABSA, FNB, Nedbank, Std Bank, Investec; established format specs and tooling |
| CMA country bank (Nedbank Namibia, Standard Bank Namibia) | 7–10 days | Fixed-price CR | Additional documentation and cross-border compliance effort |
| Forex bank partner (on supported list) | 6–10 days | Fixed-price CR | SARB documentation support; bank forex connectivity configuration |
| New/unsupported bank | 10–20 days | Fixed-price CR with 10% risk allowance | Bank-specific format specification; no prior tooling; BU Lead review required |

**BU Lead action:** Confirm or revise the effort ranges above. Once confirmed, publish as the standard BeBanking Bank Addition SOW Schedule and register in the Commercial framework.

---

## 6. Proposed Assumption Updates

No assumption wording changes are required beyond confirming the current text. The following assumptions are consistent with Option A and will be locked when BU-BB-002 is resolved:

| Assumption | Current Text (consistent with Option A) | Action |
|---|---|---|
| **BB-EXT-008** | "New bank connectivity requirements arising after go-live... are treated as new bank onboarding engagements. They are separately scoped, assessed, and priced." | **LOCK** — no wording change needed |
| **BB-SUP-006** | "BeBanking configuration changes post-go-live — adding new banks... are Change Requests. CR assessment, scoping, and approval follow the Commercial Framework CR process. CR work is billed at the applicable rate." | **LOCK** — no wording change needed |
| **BB-BNK-003** | "Each new bank connectivity requires a formal registration and certification process... Bank onboarding timelines are controlled by the bank and outside APPSolve's control. Standard bank onboarding is assumed to take 4–8 weeks." | **LOCK** — no wording change needed |

**Optional enhancement (recommended for completeness):**

BB-EXT-008 could be enhanced to explicitly reference the standard effort schedule and confirm the fixed-price CR model. This is optional — the current text is sufficient for governance purposes — but would improve pack completeness:

> *Current:* "...They are separately scoped, assessed, and priced. The bank onboarding process (BB-BNK-003) applies in full."
> 
> *Proposed enhancement:* "...They are separately scoped and priced as fixed-price Change Requests per the BeBanking Bank Addition SOW Schedule. The bank onboarding process (BB-BNK-003) applies in full. The Commercial Director holds the standard effort schedule for each bank addition tier."

**BU Lead to decide** whether to apply this enhancement before pack promotion.

### Scope Boundary Guide Updates

SB-BB-001 (New Bank Onboarding After Go-Live) currently references BU-BB-002:

> "Refer to BU-BB-002 for standard new-bank charging model."

Once BU-BB-002 is resolved, this reference should be updated to state the confirmed model:

> "New bank connectivity is priced as a fixed-price Change Request. The BeBanking BU Lead holds the standard effort schedule for each bank addition type. Contact the BeBanking BU Lead or Commercial Director for the current rate."

### Register Updates

BEBANKING_ASSUMPTION_REGISTER.csv: BB-EXT-008 row update — `bu_decision_ref` field to be cleared (BU-BB-002) and `notes` updated to reflect confirmed commercial model.

---

## 7. Governance Recommendation

### 7.1 Decision Wording for Approval

The following text should be recorded as the official BU-BB-002 decision:

> **BU-BB-002 APPROVED**
> 
> New bank connectivity requested by an existing BeBanking client after initial go-live is always treated as a separately scoped and priced Change Request. The applicable commercial model is a fixed-price Change Request per the BeBanking Bank Addition SOW Schedule (to be published by the BeBanking BU Lead). No bank addition is included in the standard BeBanking subscription. The bank onboarding process (BB-BNK-003) applies in full to all post-go-live bank additions.
> 
> *Approved by:* BeBanking BU Lead (name) _____________ *Date:* _____________  
> *Approved by:* Commercial Director (name) _____________ *Date:* _____________

### 7.2 Decision Record Entry

For the Governance Master Decision Register (`GOVERNANCE_MASTER_DECISION_REGISTER.md`):

```
| BU-BB-002 | New bank onboarding charging model | APPROVED [date] |
Option A — Fixed-price Change Request per bank addition.
Commercial model: fixed-price CR per BeBanking Bank Addition SOW Schedule.
No bank addition included in standard subscription.
BB-EXT-008 and BB-SUP-006 confirmed as authoritative; no wording change required.
Optional: BB-EXT-008 enhancement to explicitly reference fixed-price CR model.
Owners: BeBanking BU Lead + Commercial Director. Approved [date].
```

### 7.3 Pack Impact Assessment

| File | Change Required | When |
|---|---|---|
| BEBANKING_BASE_ASSUMPTIONS_V1.md | Promote status: Draft → Approved v1.0; update version v1.1-Draft → v1.0 Approved; clear BU-BB-002 from bu_lead_decisions_pending; update BU Lead Review Items table (remove BU-BB-002 row; update Resolved table) | Immediately after approval |
| BEBANKING_ASSUMPTION_REGISTER.csv | BB-EXT-008 row: clear `bu_decision_ref` (BU-BB-002); update `notes` to reflect confirmed model | Immediately after approval |
| BEBANKING_GAP_REPORT.md | GAP-BB-001: update status from PARTIALLY RESOLVED → RESOLVED; BU decision table: BU-BB-002 → RESOLVED | Immediately after approval |
| BEBANKING_SCOPE_BOUNDARY_GUIDE.md | SB-BB-001: replace BU-BB-002 reference with confirmed commercial model statement | Immediately after approval |
| GOVERNANCE_MASTER_DECISION_REGISTER.md | BU-BB-002 row: Pending → Approved; add decision text | Immediately after approval |
| HANDOVER.md / AI_CONTEXT.md | BeBanking pack status: Draft → Approved v1.0; BU-BB-002 → RESOLVED | After all file updates complete |

### 7.4 Post-Approval Next Action

Once BU-BB-002 is approved, the BeBanking BU Lead should complete the following within 14 days:

1. **Publish the BeBanking Bank Addition SOW Schedule** — effort ranges by bank type (can be a short internal document held by the Commercial Director; does not need to be a KB artefact)
2. **Communicate to presales and bid management teams** — Account Managers and bid managers need to know how to quote bank additions in proposals
3. **Update the BeBanking subscription terms template** — ensure the standard client subscription agreement explicitly excludes post-go-live bank additions from subscription scope

---

## 8. Output Summary

| Item | Value |
|---|---|
| **Recommended option** | Option A — Fixed-price Change Request per bank addition |
| **Exact approval wording** | See §7.1 |
| **Assumptions affected** | BB-EXT-008 (lock), BB-SUP-006 (lock), BB-BNK-003 (lock) |
| **Optional enhancement** | BB-EXT-008 — add explicit fixed-price CR + effort schedule reference |
| **Scope Guide update** | SB-BB-001 — replace BU-BB-002 reference with confirmed model statement |
| **Register update** | BB-EXT-008 row — clear bu_decision_ref; update notes |
| **Governance records** | GOVERNANCE_MASTER_DECISION_REGISTER.md — mark resolved + decision text |
| **Pack outcome** | BEBANKING_BASE_ASSUMPTIONS_V1.md → Approved v1.0 |
| **Additional BU Lead action** | Publish BeBanking Bank Addition SOW Schedule with effort ranges per bank type |

---

## Appendix — Reference Assumptions (current wording, read-only)

**BB-EXT-008:**
> New bank connectivity requirements arising after go-live — whether from the client acquiring a new banking relationship, expanding to a new country, or changing their primary bank — are treated as new bank onboarding engagements. They are separately scoped, assessed, and priced. The bank onboarding process (BB-BNK-003) applies in full.

**BB-SUP-006:**
> BeBanking configuration changes post-go-live — adding new banks, modifying payment approval workflows, adding new payment types, adding new ERP integration points — are Change Requests. CR assessment, scoping, and approval follow the Commercial Framework CR process. CR work is billed at the applicable rate.

**BB-BNK-003:**
> Each new bank connectivity requires a formal registration and certification process between APPSolve and the bank. Bank onboarding timelines, approval processes, and certification requirements are controlled by the bank and outside APPSolve's control. Standard bank onboarding is assumed to take 4–8 weeks from bank registration submission to confirmed production connectivity approval.

**BB-GEN-007 (onboarding phases):**
> BeBanking onboarding is executed in sequential phases: (a) Discovery and scoping; (b) Platform configuration; (c) Bank connectivity and format testing; (d) ERP integration testing; (e) User acceptance testing; (f) Go-live cutover. Each phase requires written client sign-off before the subsequent phase commences.

---

*WP14E_BU_BB_002_DECISION_PAPER v1.0 | WP14E | 2026-06-18*  
*Decision required from: BeBanking BU Lead + Commercial Director | Target: 2026-07-07*
