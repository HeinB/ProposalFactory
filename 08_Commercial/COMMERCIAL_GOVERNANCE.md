---
document_id: COMMERCIAL-GOVERNANCE
title: "APPSolve Commercial Governance Framework"
version: "1.0"
created: "2026-06-15"
created_by: "WP11F — Tender Commercial Framework"
status: "Approved — 2026-06-16"
approved_by: "Hein Blignaut (BU Lead)"
approval_ref: "WP11F-A"
applies_to: "All Oracle, Acumatica, and BeBanking proposals, SOWs, and AMS agreements"
companion_docs:
  - "RATE_CARD_FRAMEWORK.md"
  - "ESTIMATION_GUIDE.md"
  - "CR_PRICING_MODEL.md"
  - "EFFORT_MULTIPLIERS.md"
  - "ASSUMPTION_GOVERNANCE.md"
---

# APPSolve Commercial Governance Framework

## 1. Purpose

This framework defines the commercial decision-making authority, approval thresholds, pricing sign-off process, T&M vs. fixed-price decision criteria, and commercial review cadence for all APPSolve proposals, SOWs, and AMS agreements. It ensures:

- No proposal is submitted with a price that has not been commercially reviewed
- Discount authority is controlled and documented
- Fixed-price commitments are made only where scope is sufficiently defined
- AMS commercial terms are consistent across the client portfolio
- The commercial pipeline is visible to BU Leads and the Commercial Director

---

## 2. Commercial Approval Thresholds

### 2.1 Proposal Approval Authority

| Total Proposal Value | Required Approver(s) | Notes |
|---|---|---|
| Up to Tier 1 threshold | BU Lead | Standard proposals within BU Lead authority |
| Tier 1 to Tier 2 threshold | BU Lead + Commercial Director | BU Lead confirms scope; Commercial Director confirms price |
| Above Tier 2 threshold | BU Lead + Commercial Director + Director | High-value proposals require Director sign-off |
| Multi-BU proposals | All relevant BU Leads + Commercial Director | Cross-BU proposals require all relevant BU sign-off |

*Specific monetary thresholds for Tier 1 and Tier 2 are defined in the Commercial Director's authority schedule and are not contained in this document.*

### 2.2 Discount Authority

| Discount Level | Authority | Documentation Required |
|---|---|---|
| 0–5% | BU Lead | Email confirmation of discount rationale |
| 6–10% | Commercial Director | Commercial justification document |
| 11–15% | Commercial Director + Director | Written business case |
| > 15% | Director + Board | Board resolution required |

**No discount may be applied to a proposal without the required written approval.** Verbal approval is not sufficient. All discount approvals are stored in the commercial file for the engagement.

**Discount does not mean reduced scope.** A discounted proposal must deliver the full agreed scope. Where scope must be reduced to achieve a target price, the scope reduction must be documented and approved separately.

### 2.3 Change Request Approval

Per CR_PRICING_MODEL.md Section 8:

| CR Size | APPSolve Authority | Client Authority |
|---|---|---|
| Small (≤ 1 day) | AMS Account Manager or PM | Client designated AMS contact or PM |
| Standard (1–5 days) | PM + BU Lead awareness | Client project sponsor or designated approver |
| Large (5–20 days) | BU Lead + Commercial Director | Client project sponsor + written approval |
| Major (> 20 days) | Commercial Director + Director | Client senior sponsor + SOW addendum |

### 2.4 AMS Agreement Authority

| AMS Agreement Value | Required Approver(s) |
|---|---|
| Up to Tier 1 threshold | BU Lead |
| Above Tier 1 threshold | BU Lead + Commercial Director |
| New AMS agreement type (non-standard terms) | Commercial Director + Director |
| AMS agreement renewal with material change | BU Lead + Commercial Director |

*AMS agreements without a defined SLA schedule or without standard APPSolve assumptions applied require Commercial Director review before signing.*

**Renewal clarification:** Routine AMS renewals (same terms, same scope, no material change to SLA, rates, or service definition) may be approved at BU Lead level. AMS renewals involving material changes (scope expansion or reduction, SLA amendment, rate adjustment, or non-standard terms) always require Commercial Director review before renewal execution.

---

## 3. Proposal Pricing Sign-Off Process

### 3.1 Standard Sign-Off Sequence

```
1. Scope confirmed → Assumptions pack selected (see TENDER_ASSUMPTION_ASSEMBLY_RULES.md)
2. Estimation complete → Effort estimated per ESTIMATION_GUIDE.md
3. Multipliers applied → Adjusted effort per EFFORT_MULTIPLIERS.md
4. Rate card applied → Total fee calculated per RATE_CARD_FRAMEWORK.md
5. Contingency included → Per ESTIMATION_GUIDE.md Section 7
6. Commercial review → BU Lead validates scope accuracy and effort reasonableness
7. Pricing sign-off → Per Section 2.1 authority thresholds
8. Proposal submitted → Bid manager submits with signed commercial file on record
```

### 3.2 Commercial File Requirements

For every submitted proposal with a fixed price, the following documents must be on file before submission:

| Document | Owner | Purpose |
|---|---|---|
| Scope summary | Functional Lead | What is included and excluded |
| Effort estimate (bottom-up) | Functional Lead | Task-level estimate with complexity classification |
| Multiplier justification | Functional Lead + BU Lead | Which multipliers applied and why |
| Rate card calculation | Bid Manager | Total fee derivation |
| Discount approval (if applicable) | Commercial Director | Written approval for any discount |
| Assumption pack selected | Bid Manager | Which assumption packs are used (per assembly rules) |
| Pricing sign-off email | Approver per Section 2.1 | Email trail confirming price approval |

Commercial files are stored in the engagement folder under `09_Active_Tenders/[Client]/Commercial/`.

### 3.3 Emergency Pricing Process

Where a tender deadline requires price submission before the full sign-off process can be completed:

1. Bid Manager notifies Commercial Director immediately upon identifying the conflict
2. Commercial Director approves an indicative price range (not a specific price)
3. Functional Lead completes the estimate during the submission window
4. Commercial Director provides final written approval within 24 hours of submission
5. If the final estimate differs materially from the submitted price (>10% variance), the Commercial Director determines whether client notification or re-submission is required before contract execution

---

## 4. T&M vs. Fixed-Price Decision Framework

### 4.1 When to Use Fixed-Price

Fixed-price engagements are appropriate when:
- Scope is fully documented in a signed Scope and Design Document or detailed RFP specification
- All major integration endpoints are confirmed by the client
- Data migration scope is defined (entities, objects, volumes)
- Client readiness is high (experienced internal team, clean data, fast decision-making)
- There is no dependency on an external party whose timeline is not within APPSolve's control
- APPSolve has delivered similar engagements at C2 complexity or below

**Always include in a fixed-price SOW:**
- A comprehensive assumptions section (assembled per TENDER_ASSUMPTION_ASSEMBLY_RULES.md)
- Explicit scope inclusions and exclusions
- A clear change request clause referencing CR_PRICING_MODEL.md
- The payment milestone schedule

### 4.2 When to Use T&M

T&M engagements are appropriate when:
- Full scope cannot be defined at proposal stage (exploratory or strategic advisory)
- Third-party dependencies make delivery timeline unpredictable
- Client requirements are likely to evolve materially during delivery
- The engagement involves significant discovery work before design is possible
- Complexity is C3 or C4 and risk cannot be bounded in a fixed price

**T&M SOW must include:**
- A capped estimate (client approves the cap; APPSolve tracks against it)
- Monthly billing cycle with time and activity reporting
- Written client approval required before exceeding the cap
- Rate schedule per role per RATE_CARD_FRAMEWORK.md

### 4.3 Hybrid Arrangements

Hybrid engagements (some phases fixed, some T&M) are permitted where:
- Mobilize and Scope & Design are T&M (discovery; risk)
- Prototype through Deploy are fixed-price (agreed scope from SDD)
- This is the preferred model for C3/C4 engagements

Commercial Director sign-off is required for all hybrid arrangements.

### 4.4 AMS Contract Type

AMS agreements follow the model defined in AMS_ASSUMPTIONS_V1.md:
- Retainer-based: fixed monthly fee for defined support scope
- Allocated-hours: fixed monthly hour bucket at contracted rate

AMS agreements are never fixed-price for CRs. CRs within AMS are always separately estimated and approved per CR_PRICING_MODEL.md.

---

## 5. Commercial Risk Assessment

### 5.1 Risk Flags

Before a proposal is approved, the following risk flags must be assessed:

| Risk | Flag | Mitigation required |
|---|---|---|
| Fixed-price on C4 complexity | RED | Commercial Director sign-off mandatory; elevated contingency |
| First engagement with this client | AMBER | Scope tightening; assumptions reviewed for completeness |
| Multi-BU engagement (cross-BU delivery risk) | AMBER | All BU Leads sign off scope in their area |
| Compressed timeline (>20% compression) | AMBER | Timeline multiplier applied; risk logged; client acknowledgement |
| SPOF resource dependency (see CONSULTANT_SKILL_MATRIX.md) | AMBER | Named resource confirmed available for engagement duration |
| Compliance documents expired (Directors' Resolution, B-BBEE) | RED | Resolve before submission; cannot submit with expired documents |
| No signed reference letters for claimed references | AMBER | Confirm AM approval before naming clients in proposal |
| Third-party integration dependency (new vendor) | AMBER | Vendor cooperation confirmed in writing before fixed-price commitment |

### 5.2 Risk Register in Commercial File

For each RED or AMBER risk flag, the commercial file must include:
- Risk description
- Mitigation planned
- Approval obtained (who confirmed the risk is acceptable)

---

## 6. Margin Governance

### 6.1 Margin Floors

Margin floors (minimum acceptable margin per engagement type) are defined in the Commercial Director's authority schedule and are not documented here. The framework principles:

| Principle | Application |
|---|---|
| No engagement below minimum margin floor | All fixed-price proposals must be above the margin floor before any discount |
| Margin floor is non-negotiable at BU Lead level | Only the Commercial Director + Director can approve below-floor pricing |
| AMS agreements must maintain AMS margin floor | AMS pricing reductions affect long-term recurring margin — higher bar for approval |
| Margin erodes under scope creep | All CRs are margin-positive — absorbing CR scope into base price is prohibited |

### 6.2 Margin Protection Rules

1. Assumptions packs (from the WP11 library) must be included in every fixed-price proposal — they are the primary commercial protection mechanism
2. CRs must be raised and priced — absorbing CR scope into implementation hours without commercial approval is not permitted
3. T&M billing must be aligned to actual effort — no underbilling to "keep the client happy"
4. AMS monthly hours must be tracked — consuming more hours than allocated without client approval erodes AMS margin

---

## 7. Commercial Review Cadence

### 7.1 Pipeline Review

| Review | Frequency | Attendees | Output |
|---|---|---|---|
| BU commercial pipeline | Monthly | BU Lead + Commercial Director | Open proposal status; outstanding estimates; pricing decisions needed |
| Cross-BU commercial review | Quarterly | All BU Leads + Commercial Director + Director | Portfolio margin analysis; discount trends; rate card review trigger |
| AMS portfolio review | Quarterly | AMS Account Managers + Commercial Director | AMS margin per client; CR pipeline; renewal schedule; at-risk agreements |

Monthly BU commercial pipeline reviews are standing calendar events. The BU Lead schedules these reviews at the start of each year and maintains the standing invitation. The Commercial Director attends the quarterly cross-BU review and may attend monthly BU reviews on request.

### 7.2 Rate Card Review

Rate cards are reviewed annually in January. Mid-year review is triggered if:
- Market rates shift materially (>10% variance from current card)
- A significant new competitor changes the market rate landscape
- APPSolve's cost base changes materially (new office, senior hires)

### 7.3 Assumption Library Review

The WP11 assumption library is reviewed when:
- A BU Lead identifies a material scope dispute not covered by current assumptions
- A new product or module is added to APPSolve's portfolio
- An assumption is overridden at the project level three or more times (indicating the assumption needs updating)

---

## 8. Prohibited Commercial Actions

The following actions are prohibited without the specified approvals:

| Prohibited Action | Exception |
|---|---|
| Submitting a fixed-price proposal without a bottom-up estimate on file | None |
| Applying a discount without written Commercial Director approval | Discounts within BU Lead authority (≤5%) may be approved by BU Lead email |
| Commencing CR work without written client approval | None — including micro CRs (document even if absorbed) |
| Exceeding a T&M cap without written client approval | None |
| Including an assumption in a proposal that has not been approved per ASSUMPTION_GOVERNANCE.md | None |
| Using a client reference in a proposal without AM and BU Lead approval | None — per ORACLE_FACT_BASELINE.md and W3S1 governance rules |
| Submitting a proposal with an expired Directors' Resolution or expired B-BBEE certificate | None — these are compliance documents; tender submission is blocked without them |

---

## 9. Decision Record

*WP11F-A — Commercial Framework Approval | 2026-06-16 | BU Lead: Hein Blignaut*

| Decision ID | Item | Decision | Applied |
|---|---|---|---|
| BU-GOV-001 | Tier 1 and Tier 2 monetary thresholds | **DEFERRED TO COMMERCIAL DIRECTOR** — Monetary approval thresholds are maintained in the Commercial Director's authority schedule and are not documented in this framework | CD decision item — placeholder maintained in Section 2.1 |
| BU-GOV-002 | Discount authority bands | **APPROVED** — 0–5% BU Lead; 6–10% Commercial Director; 11–15% CD+Director; >15% Director+Board confirmed as documented in Section 2.2 | Section 2.2 confirmed |
| BU-GOV-003 | Margin floor per engagement type | **DEFERRED TO COMMERCIAL DIRECTOR** — Margin floors are defined in the Commercial Director's authority schedule; not documented in this framework | CD decision item — placeholder maintained in Section 6.1 |
| BU-GOV-004 | AMS renewal and CD review | **APPROVED with clarification** — Routine renewals (same terms, same scope) approved at BU Lead level; renewals with material changes (scope, SLA, rates, non-standard terms) always require Commercial Director review | Section 2.4 updated |
| BU-GOV-005 | Monthly pipeline review as standing event | **APPROVED** — Monthly BU commercial pipeline review confirmed as a standing calendar event; BU Lead schedules at start of year; CD attends quarterly cross-BU review | Section 7.1 updated |
| BU-GOV-006 | Sign-off sequence mandatory | **APPROVED** — 8-step sign-off sequence (Section 3.1) is the mandatory process for all fixed-price proposals; no exceptions at BU Lead level | Section 3.1 confirmed |
| BU-GOV-007 | Emergency pricing 24-hour window | **APPROVED** — 24-hour final approval window confirmed; >10% variance triggers CD review of whether client notification or re-submission is required before contract execution | Section 3.3 updated |
| BU-GOV-008 | Risk flags applied consistently | **APPROVED** — RED/AMBER risk flag categorisation (Section 5.1) applied consistently across all BUs; BU Lead cannot override a RED flag without Commercial Director approval | Section 5.1 confirmed |
| BU-GOV-009 | Prohibition list absolute | **APPROVED** — All prohibited actions (Section 8) are absolute at BU Lead level; Commercial Director + Director approval required for any exception | Section 8 confirmed |

**Commercial Director items outstanding: BU-GOV-001, BU-GOV-003**

---

*COMMERCIAL_GOVERNANCE v1.0 | WP11F — Tender Commercial Framework | 2026-06-15 → Approved 2026-06-16 | BU Lead: Hein Blignaut*  
*Companion: RATE_CARD_FRAMEWORK.md · ESTIMATION_GUIDE.md · CR_PRICING_MODEL.md · EFFORT_MULTIPLIERS.md*  
*Related: ASSUMPTION_GOVERNANCE.md · TENDER_ASSUMPTION_ASSEMBLY_RULES.md*
