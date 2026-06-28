---
document_id: CR-PRICING-MODEL
title: "APPSolve Change Request Pricing Model"
version: "1.0"
created: "2026-06-15"
created_by: "WP11F — Tender Commercial Framework"
status: "Approved — 2026-06-16"
approved_by: "Hein Blignaut (BU Lead)"
approval_ref: "WP11F-A"
applies_to: "All Oracle, Acumatica, and BeBanking implementation projects and AMS agreements"
companion_docs:
  - "RATE_CARD_FRAMEWORK.md"
  - "ESTIMATION_GUIDE.md"
  - "COMMERCIAL_GOVERNANCE.md"
related_assumptions:
  - "AMS-CR-001 (AMS_ASSUMPTIONS_V1.md) — CR threshold 2 hours"
  - "AMS-CR-002 (AMS_ASSUMPTIONS_V1.md) — CR process"
  - "AMS-CR-003 (AMS_ASSUMPTIONS_V1.md) — CR not subject to incident SLA"
---

# APPSolve Change Request Pricing Model

## 1. Purpose

This document defines APPSolve's standard model for pricing and managing Change Requests (CRs) in implementation projects and AMS agreements. It covers:

- The distinction between project CRs and AMS CRs
- CR classification framework
- Effort estimation approach for CRs
- Pricing methods (fixed-price CR vs. T&M CR)
- CR commercial documentation requirements
- AMS CR threshold (standardised at 2 hours per BU-AMS-004)

---

## 2. What is a Change Request?

### 2.1 Definition

A Change Request is a formally scoped, estimated, and approved work item that represents scope or effort outside the agreed project SOW or AMS agreement.

A CR is NOT:
- A defect fix (system not working per agreed design) — fix under warranty/AMS at no charge
- A service request within monthly AMS hours (see AMS assumptions pack)
- A scope clarification or design question during implementation (managed through the RAID log)

A CR IS:
- A client-requested change to agreed design after the Scope and Design Document is signed
- An enhancement to an agreed integration after specification is signed
- A new data object, new module, or new configuration element added post-design
- A scope increase in a data migration (new data objects, additional entities)
- Additional test cycles beyond the standard model (per ERP-DAT-006: two mock + final)

### 2.2 CR vs. Design Change

Not every design iteration is a CR. During the Scope & Design phase, refinements to requirements are expected and managed within the estimated design effort. A CR is triggered when:
- The Scope and Design Document has been signed and the client changes a requirement
- The change adds effort or introduces risk beyond the signed SOW scope
- The change affects the agreed commercial price, timeline, or resource plan

If the effort impact of a change is zero (the new approach takes the same effort as the original), document the change as a design variation — not a formal CR.

---

## 3. CR Classification

### 3.1 Project CR Categories

| Category | Description | Typical Examples |
|---|---|---|
| **CR-SCOPE** | Adds new functionality, modules, or deliverables not in the SOW | New legal entity added; new integration requested; Recruiting Booster added after initial BOM |
| **CR-DESIGN** | Changes agreed design after SDD sign-off in a way that increases effort | COA segment added; workflow approval path changed after configuration started; additional security roles required |
| **CR-DATA** | Changes agreed data migration scope or adds data objects | Additional entities to migrate; new data object (e.g., open purchase orders added to migration); third migration cycle requested |
| **CR-TIMELINE** | Client-requested timeline compression or extension that affects resource allocation | Fast-track cutover; delayed go-live requiring resource re-scheduling |
| **CR-TECH** | Technical change outside original specification | New integration adapter required; third-party vendor changes API post-integration-spec sign-off |

### 3.2 AMS CR Categories

| Category | Description | Examples |
|---|---|---|
| **CR-CONFIG** | Configuration change above 2-hour threshold | New multi-level approval workflow; new GL cost centre structure |
| **CR-REPORT** | New report development (always a CR — not a service request) | New FRS report; new OTBI report from scratch |
| **CR-ENHANCE** | Enhancement to existing module functionality | New absence type with complex eligibility rules; new compensation plan added to existing Compensation cycle |
| **CR-INT** | OIC integration modification above threshold | New field mapping added to existing integration; new trigger added |
| **CR-MIGRATE** | Post-go-live data migration | New entity onboarded to existing ERP; historical data load requested after go-live |

---

## 4. CR Threshold (AMS)

Per BU-AMS-004 (approved 2026-06-15):

**Standard AMS CR threshold: 2 hours**

| Effort | Treatment |
|---|---|
| ≤ 2 hours | APPSolve may absorb at its discretion; no formal CR required; logged as service request |
| > 2 hours | Formal CR required: written scope, written estimate, written client approval before work commences |
| Multi-day | Always a formal CR; daily rate billing applies (not hourly rate) |

**No entitlement:** Prior absorptions below the threshold do not create an entitlement to future absorptions. Each case is assessed independently.

**Specific AMS agreement:** Where the AMS agreement specifies a different CR threshold, the agreement threshold takes precedence over the 2-hour standard.

---

## 5. CR Effort Estimation

### 5.1 Estimation Method

CRs are estimated using the same bottom-up method as implementation estimates (ESTIMATION_GUIDE.md). For small CRs (< 5 days), the estimate is produced by the assessing consultant and reviewed by the AMS Account Manager or Project Manager. For large CRs (≥ 5 days), the Functional Lead or BU Lead reviews before the estimate is submitted to the client.

### 5.2 CR Estimation Template

For each CR, document:

```
CR Reference:      [CR-XXX-YYYY]
Client:            [Client name]
Engagement:        [Project / AMS — AMS agreement reference]
Date raised:       [YYYY-MM-DD]
Raised by:         [Client contact name and role]
Category:          [CR-SCOPE / CR-DESIGN / CR-DATA / CR-TIMELINE / CR-TECH / CR-CONFIG / CR-REPORT / CR-ENHANCE / CR-INT / CR-MIGRATE]
Description:       [Clear description of what is requested]
Root cause:        [Why is this a CR? What changed from the original agreement?]
Effort estimate:   [X days / Y hours per role]
Rate applied:      [T&M daily rate / AMS hourly rate / Band]
Total CR fee:      [Amount in ZAR]
Pricing method:    [Fixed-price / T&M]
Assumptions:       [Key assumptions underpinning the estimate]
Exclusions:        [What is not included in the CR]
Timeline:          [Estimated delivery date]
Approval required: [Client contact authorised to approve CRs]
Approval status:   [Pending / Approved / Declined]
Approval date:     [YYYY-MM-DD]
```

### 5.3 CR Effort Size Bands

| Size | Effort | Treatment |
|---|---|---|
| Micro | ≤ 2 hours | Absorbed at APPSolve discretion (AMS only); no formal CR |
| Small | 2 hours – 1 day | Formal CR; hourly estimation; AMS hourly rate or T&M |
| Standard | 1–5 days | Formal CR; daily estimation; standard T&M or fixed-price CR |
| Large | 5–20 days | Formal CR; bottom-up estimation required; BU Lead review; Commercial Director sign-off on price |
| Major | > 20 days | Treat as mini-project; separate SOW or SOW addendum; Commercial Director sign-off mandatory |

---

## 6. CR Pricing Methods

### 6.1 Fixed-Price CR

A fixed-price CR is quoted as a total fee. The client knows the total cost before approving. APPSolve bears the risk if effort exceeds the estimate.

**Project CR rate:** Project CRs are priced at the same T&M daily rate as specified in the originating project SOW rate schedule. No separate CR premium rate applies. For AMS CRs, the AMS hourly rate applies per the AMS agreement.

**Use fixed-price CRs when:**
- Scope of the CR is fully definable upfront
- Risk of scope expansion is low
- Client preference is for certainty
- CR size is Standard or below

**Price formula:**
```
Fixed-Price CR = (Effort days × Daily rate × Applicable multiplier) + Risk allowance (0–10%)
```

### 6.2 Time and Materials CR

A T&M CR is estimated (for client awareness) but billed at the actual hours worked at the agreed T&M rate.

**Use T&M CRs when:**
- Scope of the CR is partially defined (e.g., defect remediation where root cause is unknown)
- CR involves third-party dependencies (vendor cooperation, bank testing)
- Client accepts T&M risk and it is agreed in the SOW

**T&M billing formula:**
```
T&M CR billing = Actual hours worked × AMS hourly rate OR actual days × T&M daily rate
```

T&M CRs require a capped estimate — the client approves the cap, and APPSolve does not exceed the cap without a further written approval.

### 6.3 Milestone-Based CR

For large or Major CRs, payment may be structured by milestone (design approval, build completion, UAT sign-off, go-live). Milestone structure is agreed in the CR approval document.

---

## 7. CR Commercial Documentation Requirements

### 7.1 Minimum Documentation for All CRs

1. **CR Estimate Document** — completed per Section 5.2 template
2. **Client written approval** — email with explicit reference to the CR number and fee is sufficient; formal signature required for CRs > 5 days
3. **Scope confirmation** — scope included in the CR must be as specific as the original SOW

### 7.2 Additional Requirements by CR Size

| Size | Additional requirements |
|---|---|
| Small | Client email approval sufficient |
| Standard | CR Estimate Document + client email approval |
| Large | CR Estimate Document + BU Lead review + Commercial Director sign-off + client email or formal sign |
| Major | CR Estimate Document + BU Lead + Commercial Director + separate SOW addendum + client signature |

### 7.3 Prohibited Actions

- Do not commence CR work before written client approval
- Do not absorb CR work into project hours without explicit Commercial Director approval
- Do not invoice a CR at a rate higher than the applicable T&M or AMS rate schedule
- Do not allow CRs to accumulate without regular billing — invoice CRs at completion or at agreed intervals for multi-month CRs

---

## 8. CR Approval Authority

| CR Size | APPSolve authority | Client authority |
|---|---|---|
| Micro (≤2h, absorbed) | AMS Consultant decision | Not required |
| Small (2h–1 day) | AMS Account Manager or PM | Designated client AMS contact or PM |
| Standard (1–5 days) | PM + BU Lead awareness | Designated client AMS contact or PM |
| Large (5–20 days) | BU Lead + Commercial Director sign-off | Client project sponsor or designated approver |
| Major (>20 days) | Commercial Director + Director sign-off | Client senior sponsor + written SOW addendum |

---

## 9. CR Pipeline Management

### 9.1 AMS CR Register

The AMS Account Manager maintains a CR pipeline register for each AMS client, tracking:
- All open CRs (raised, estimated, awaiting approval)
- All approved CRs (in progress, completed, invoiced)
- All declined CRs
- CR hours consumed against AMS monthly hours allocation (where absorbed below threshold)

The CR register is reported in the monthly AMS support report (AMS-REP-001).

**Micro CR logging:** Even micro CRs absorbed below the 2-hour threshold must be logged in the CR register. No formal CR document is required for absorbed micro CRs, but a log entry is required: client, date, brief description of the work, hours absorbed, and the reason for the absorb decision. This log is used for pattern analysis (identifying assumption gaps) and volume tracking (identifying clients where micro CR accumulation is eroding AMS margin).

### 9.2 Project CR Register

The Project Manager maintains a project CR register in the project RAID log, tracking:
- All CRs raised (date, category, value)
- Status (pending estimate, pending approval, approved, in delivery, completed, invoiced)
- Commercial impact (cumulative CR value vs. original SOW value)
- Schedule impact (effect on project go-live date)

---

## 10. Decision Record

*WP11F-A — Commercial Framework Approval | 2026-06-16 | BU Lead: Hein Blignaut*

| Decision ID | Item | Decision | Applied |
|---|---|---|---|
| BU-CR-001 | 2-hour AMS CR threshold | **APPROVED** — 2-hour threshold (BU-AMS-004, approved 2026-06-15) confirmed across Oracle, Acumatica, and BeBanking AMS; no BU-specific adjustments at this time | Section 4 confirmed |
| BU-CR-002 | Micro CR logging | **APPROVED** — Absorbed micro CRs (≤2h) must still be logged in the CR register: client, date, description, hours absorbed, absorb rationale; required for pattern analysis and margin protection | Section 9.1 updated |
| BU-CR-003 | Commercial Director sign-off threshold | **DEFERRED TO COMMERCIAL DIRECTOR** — Monetary equivalents for CR size bands (Large/Major ZAR thresholds) require Commercial Director input; effort-day thresholds (Large ≥5 days, Major >20 days) remain as documented | CD decision item — Section 8 thresholds remain effort-based |
| BU-CR-004 | Project CR billing rate | **APPROVED** — Project CRs priced at same T&M daily rate as originating project SOW; no separate CR premium rate | Section 6.1 updated |
| BU-CR-005 | Major CR documentation | **APPROVED** — Major CRs (>20 days) always require a separate SOW addendum regardless of Commercial Director sign-off; formal contractual documentation mandatory | Section 7.2 confirmed |
| BU-CR-006 | CR numbering convention | **APPROVED** — Standard numbering: `CR-[ClientCode]-[YYYY]-[###]` e.g. CR-PLN-2026-001; resets per year per client | Section 5.2 template reference |
| BU-CR-007 | Emergency CR approval | **APPROVED** — No verbal approvals for any CR; minimum: written email from client-authorised person before work commences | Section 7.3 confirmed |
| BU-CR-008 | CR size definitions (project vs AMS) | **APPROVED** — CR size definitions apply equally to project CRs and AMS CRs | Section 5.3 confirmed |

**Commercial Director items outstanding: BU-CR-003**

---

*CR_PRICING_MODEL v1.0 | WP11F — Tender Commercial Framework | 2026-06-15 → Approved 2026-06-16 | BU Lead: Hein Blignaut*  
*Companion: RATE_CARD_FRAMEWORK.md · ESTIMATION_GUIDE.md · EFFORT_MULTIPLIERS.md · COMMERCIAL_GOVERNANCE.md*  
*Key reference: AMS-CR-001 (2-hour threshold) in AMS_ASSUMPTIONS_V1.md*
