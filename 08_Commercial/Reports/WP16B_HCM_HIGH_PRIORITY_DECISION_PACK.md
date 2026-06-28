---
document_id: WP16B-HIGH-PRIORITY
title: "WP16B — Oracle HCM High Priority Decision Pack"
version: "1.0"
created: "2026-06-19"
created_by: "WP16B — Oracle HCM Final Governance Closure"
status: "Awaiting BU Lead Email Approval"
decisions_covered: "BU-REC-005, BU-REC-006"
priority: "HIGH"
---

# WP16B — Oracle HCM High Priority Decision Pack

**Date:** 2026-06-19 | **Decisions:** BU-REC-005, BU-REC-006 | **Route:** Email to Oracle HCM BU Lead | **Response required:** Binary confirmation — reply "Confirmed" to each section

> **Why these are HIGH priority:** These two decisions govern the commercial scope trigger for Oracle Fusion Recruiting Booster (a separately purchased product) and the boundary between APPSolve's Oracle/OIC work and a third-party provider's portal. Both affect how Recruiting proposals are priced and what is and is not in scope. Neither requires Commercial Director involvement.

---

## Decision 1 of 2 — BU-REC-005: Recruiting Booster Scope Trigger

### Decision Summary

Oracle Fusion Recruiting Cloud (B87675) and Oracle Fusion Recruiting Booster (B95763) are **two separate Oracle BOM line items**. Recruiting Booster adds advanced capabilities not included in the base Recruiting Cloud licence:

| Feature | B87675 Recruiting Cloud | B95763 Recruiting Booster |
|---|---|---|
| Standard career site, requisitions, offers | ✅ Included | — |
| Basic interview scheduling | ✅ Included | — |
| Two-Way Messaging (SMS/email) | ❌ Not available | ✅ |
| Oracle Digital Assistant chatbot | ❌ Not available | ✅ |
| Recruiting Event Management | ❌ Not available | ✅ |
| Direct Apply (LinkedIn) | ❌ Not available | ✅ |
| Advanced interview scheduling (calendar sync) | ❌ Not available | ✅ |

The question is: **when do the Section 24 Booster assumptions (REC-BOO-001–007) apply?**

### Options

| Option | Description | Risk |
|---|---|---|
| **(a) BOM-driven — RECOMMENDED** | Booster assumptions apply only when B95763 is explicitly in the client's BOM | Lowest. Scope precisely follows what was sold. No unscoped Booster effort. |
| (b) Feature-driven | Booster features apply whenever B87675 is in scope | High. Booster capabilities are not available in B87675 alone — would create undeliverable commitments. |
| (c) Always in scope | Booster included in all Recruiting implementations | Impractical. Client would receive Booster work they may not have purchased. |

### Recommended Option: (a)

**Rationale:** Oracle Fusion Recruiting Booster is a separately purchased product with its own Oracle BOM line number (B95763). Booster capabilities are technically unavailable in B87675 alone — the Oracle platform does not enable Two-Way Messaging, Digital Assistant, Event Management, or Direct Apply without the Booster licence. Scoping these features when B95763 is not in the BOM would create undeliverable proposal commitments.

### Commercial Impact

| Scenario | Impact |
|---|---|
| Client purchases B87675 only | Booster Section 24 is suppressed. No Two-Way Messaging, chatbot, event management, or Direct Apply in scope. |
| Client purchases B87675 + B95763 | Full Section 24 applies. Booster features in scope. |
| Proposal review step | AI to check BOM before loading Booster assumptions. |

**No Commercial Director review required.** This is a technical BOM-driven scope trigger with no pricing dimension.

### Current Draft Wording — REC-BOO-001

> **The existing draft assumption already reflects Option (a).** Approving this decision closes the pending tag with no wording change required.

**Current text (REC-BOO-001):**
> "The assumptions in this section (REC-BOO-XXX) apply only where Oracle Fusion Recruiting Booster (B95763) is included in the Bill of Materials. Where only Oracle Fusion Recruiting Cloud (B87675) is licensed, Booster-specific capabilities (Two-Way Messaging, Digital Assistant chatbot, Event Management, Direct Apply) are not available and are excluded."

**Pack change after approval:** Remove `*(Pending BU-REC-005)*` from REC-BOO-001. Remove BU-REC-005 from frontmatter `bu_lead_review_items`. No wording change needed.

### Exact Approval Wording for Email

> **BU-REC-005 — Please confirm:**
>
> APPSolve's Oracle Fusion Recruiting Booster assumptions (Section 24, REC-BOO-001 to REC-BOO-007) apply only when Oracle Fusion Recruiting Booster (B95763) is explicitly included in the client's Bill of Materials. Where only Oracle Fusion Recruiting Cloud (B87675) is licensed, all Booster-specific capabilities — Two-Way Messaging, Digital Assistant chatbot, Recruiting Event Management, Direct Apply (LinkedIn), and advanced calendar-integrated interview scheduling — are excluded from scope and are not deliverable under B87675 alone.
>
> **Reply "Confirmed" to approve Option (a) — BOM-driven scope trigger.**

---

## Decision 2 of 2 — BU-REC-006: Background Check Integration Scope

### Decision Summary

Background screening is a mandatory step in most South African recruitment workflows. The question is: what is APPSolve's standard scope for background check provider integration — and specifically, does APPSolve configure the background check provider's own portal, or only the Oracle/OIC side of the integration?

**Background check providers in the SA market include:** Managed Integrity Screening (MIS), iFacts, LexisNexis Background Checks, and Sterling Check. Each has its own portal for managing screening packages, result workflows, and compliance documentation.

### Options

| Option | Description | Risk |
|---|---|---|
| **(a) OIC design only — RECOMMENDED** | APPSolve designs/configures the Oracle OIC integration to the provider's API. Provider portal setup is excluded. Always separately scoped from base Recruiting. | Lowest. Provider portals are provider-specific and variable effort. Clear boundary. |
| (b) Includes provider portal | APPSolve also configures the background check provider's own portal (screening packages, result management, workflows) | High. Provider portal effort is unknown at proposal time and provider-specific. Cannot be included in a base scope without knowing the provider. |
| (c) Always separately scoped | Neither the OIC integration nor any background check work is included in base Recruiting scope — always a separately priced engagement | Conservative but limits proposal flexibility. |

### Recommended Option: (a)

**Rationale:** Background check provider portals (MIS, iFacts, LexisNexis) each have distinct administration interfaces, screening package structures, and result management workflows. APPSolve cannot scope this effort without knowing which provider the client uses. The Oracle/OIC integration side (Oracle Recruiting → OIC → Provider API) is standard integration work that APPSolve can design once the provider's API is confirmed. Keeping the OIC design as separately scoped (from base Recruiting) protects against under-pricing.

Note: Option (c) is slightly more conservative than Option (a) but the current draft supports (a) — "separately scoped and priced integration" rather than "always excluded." This gives the sales team flexibility to include background check OIC design in a combined proposal where it makes commercial sense.

### Commercial Impact

| Scenario | Impact |
|---|---|
| Standard Recruiting proposal | Background check integration excluded from base scope (per REC-INT-004 and REC-EXC-004). Flagged as an optional add-on. |
| Client has existing background check contract | APPSolve can separately scope and price the OIC integration design (not the provider portal). Client responsible for API documentation provision. |
| Provider portal configuration | Client's responsibility or provider's professional services. Never APPSolve's scope. |

**No Commercial Director review required.** This is a scope boundary decision with no pricing dimension.

### Current Draft Wording — REC-INT-004 + REC-EXC-004

> **The existing draft assumptions already reflect Option (a).** Approving this decision closes the pending tag with no wording change required.

**Current text (REC-INT-004):**
> "Background check provider integration is not included in base scope. APPSolve can design and configure an OIC integration between Oracle Recruiting and a third-party background check provider (for example, Managed Integrity Screening, iFacts, LexisNexis, or equivalent) as a separately scoped and priced integration. The background check provider must offer a documented API. The client is responsible for all commercial engagement with the background check provider."

**Current text (REC-EXC-004):**
> "Third-party background check platform configuration (portal setup, screening package definition, result management) is excluded. APPSolve's scope is limited to the Oracle OIC integration design (where this is separately scoped); the background check provider's own platform configuration is the client's and the provider's responsibility."

**Pack change after approval:** Remove `*(Pending BU-REC-006)*` from REC-INT-004. Remove BU-REC-006 from frontmatter `bu_lead_review_items`. No wording change needed.

### Exact Approval Wording for Email

> **BU-REC-006 — Please confirm:**
>
> APPSolve's standard scope for background check integration is limited to Oracle OIC integration design and configuration (as a separately scoped and priced engagement). Background check provider portal configuration — including screening package definition, result workflow setup, and result management in the provider's platform (Managed Integrity Screening, iFacts, LexisNexis, Sterling, or equivalent) — is excluded from APPSolve's scope. The background check provider must supply a documented API. All commercial arrangements with the background check provider are the client's responsibility.
>
> **Reply "Confirmed" to approve Option (a) — OIC design only, provider portal excluded.**

---

## Summary

| Decision | Status | Pack change on approval | CD involvement |
|---|---|---|---|
| BU-REC-005 | Awaiting email confirmation | Remove pending tag from REC-BOO-001 only | None |
| BU-REC-006 | Awaiting email confirmation | Remove pending tag from REC-INT-004 only | None |

**Once both decisions are confirmed:** HCM Recruiting will have resolved all 7 BU-REC decisions (4 MEDIUM resolved WP15F + 2 HIGH + 1 LOW). The pack will be ready for the promotion pass (apply all decision tags, update status, promote to Approved v1.0) as soon as BU-REC-007 is also confirmed.

---

*WP16B_HCM_HIGH_PRIORITY_DECISION_PACK v1.0 | WP16B | 2026-06-19 | Awaiting Oracle HCM BU Lead email confirmation*
