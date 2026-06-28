---
title: Governance Risk Register
version: v1.0
status: Active
programme: WP13 Governance Approval Campaign
date: 2026-06-16
---

# Governance Risk Register

**Programme:** WP13 | **Date:** 2026-06-16

> **Scope:** Risks to the governance approval campaign only. Proposal delivery risks are tracked in the main Tender Programme risk register. Assumption pack content risks are tracked in individual Gap Reports.

---

## Risk Matrix

| Risk ID | Risk | Likelihood | Impact | Rating | Mitigation | Owner |
|---|---|---|---|---|---|---|
| GR-001 | BU Lead unavailable for Wave 1 CRITICAL decisions | Medium | Critical | **HIGH** | Escalate immediately to Commercial Director; Wave 1 has 5-business-day window | Commercial Director |
| GR-002 | BU Lead unavailable for Wave 2 workshops | Medium | High | **HIGH** | Schedule workshops 3 weeks in advance; nominate deputy decision-maker | BU Lead (each pack) |
| GR-003 | BEE certificate expires before governance complete | Medium | High | **HIGH** | Target full Wave 3 completion by 2026-07-28; monitor renewal | Commercial Director |
| GR-004 | Conflicting decisions across packs | Low | High | **MEDIUM** | Pre-align BU-ACU-008/BU-BB-004 (hypercare) and BU-ACU-012/BU-BB-009 (POPIA) before BeBanking workshop | AI + BU Lead |
| GR-005 | Scope change to assumption pack after BU approval | Low | High | **MEDIUM** | Version-lock packs at Approved v1.0; any change requires new WP + BU sign-off | BU Lead |
| GR-006 | New pack introduced before governance closure | Low | Medium | **MEDIUM** | Defer any new pack creation until Wave 3 complete; document as WP14+ | Commercial Director |
| GR-007 | Decision deferred at workshop — no outcome reached | Medium | Medium | **MEDIUM** | BU Lead must nominate a fallback if decision cannot be made; defer to safe-default or CRITICAL escalation | BU Lead |
| GR-008 | AI implements decision incorrectly in assumption pack | Low | High | **MEDIUM** | BU Lead spot-checks 3–5 implemented assumptions per pack before final approval | BU Lead |
| GR-009 | Commercial Director unavailable for HIGH decisions requiring dual approval | Medium | High | **HIGH** | Flag BU-BB-006, BU-BB-002, BU-BB-003, BU-ACU-011 early; these require Commercial Director presence | Commercial Director |
| GR-010 | Acumatica partner certificate cannot be obtained before Wave 1 deadline | Medium | Critical | **HIGH** | If certificate missing, BU-ACU-009 cannot be resolved; Acumatica proposals must be suspended until confirmed | Acumatica BU Lead |
| GR-011 | HCM BU Lead approves LOW decisions by email but then overrides in workshop | Low | Low | **LOW** | Record email approval with timestamp; override at workshop requires explicit statement and new Decision Record | Oracle HCM BU Lead |
| GR-012 | Proposal received and tendered before pack is Approved | Medium | Critical | **HIGH** | AI_CONTEXT.md and ASSEMBLY_RULES.md both prohibit use of Draft packs in proposals; enforce strictly | All |
| GR-013 | Pack promoted to Approved with unimplemented decisions | Low | High | **MEDIUM** | AI confirms all decisions implemented before requesting BU promotion; checklist in Decision Record Section 5 | AI |
| GR-014 | Workshop attendee claims decision made outside governance process | Low | Medium | **LOW** | All decisions require a completed Decision Record with BU Lead name and date; verbal decisions are not binding | BU Lead |

---

## Risk Detail

### GR-001 — BU Lead Unavailable for Wave 1 CRITICAL Decisions

**Risk:** BU Lead cannot be reached within 5 business days of Wave 1 initiation. Both CRITICAL decisions (BU-ACU-009 and BU-BB-006) remain unresolved past 2026-06-23.

**Impact:** BeBanking proposals cannot be commercially validated. Acumatica proposals may cite incorrect partner tier. Combined, this blocks approximately 60% of active tender pipeline.

**Mitigation:**
- Wave 1 is asynchronous — email is sufficient, no workshop required
- Commercial Director can initiate BU-BB-006 call directly if BeBanking BU Lead is unreachable
- BU-ACU-009 only requires the BU Lead to check the Acumatica Partner Portal (15-minute task) — can be delegated upward

**Trigger:** BU Lead does not respond within 3 business days of Wave 1 initiation.

**Escalation path:** Commercial Director → Managing Director

---

### GR-002 — BU Lead Unavailable for Wave 2 Workshops

**Risk:** One or more BU Leads cannot attend Wave 2 workshops in the week of 2026-06-30. Wave 2 slips to week of 2026-07-14, compressing Wave 3 to the final two weeks before BEE expiry.

**Impact:** If Wave 2 and Wave 3 both slip by 2 weeks, full approval completes 2026-08-11 — after BEE certificate expiry.

**Mitigation:**
- Schedule Wave 2 workshops by 2026-06-20 (4 weeks in advance)
- Identify deputy decision-maker for each BU Lead before scheduling
- Wave 2 workshops are short (30–90 minutes): flag as hard-calendar blocks

**Trigger:** BU Lead declines Wave 2 calendar invite without rescheduling within 1 business day.

---

### GR-003 — BEE Certificate Expires Before Governance Completion

**Risk:** B-BBEE Level 4 certificate expires 2026-07-31. If any approved packs are needed for a proposal submitted after that date, APPSolve cannot substantiate its BEE status.

**Impact:** Non-compliance on BEE criterion of any tender submitted after 2026-07-31 without renewed certificate. Some tenders may be disqualified.

**Mitigation:**
- Track BEE renewal as OAR-A01 in Plennegy blocker register
- Wave 3 target of 2026-07-28 is designed to complete before expiry
- TENDER_ASSUMPTION_ASSEMBLY_RULES.md already flags BEE expiry constraint
- If renewal is confirmed before expiry, risk is resolved regardless of governance timeline

**Current status:** Renewal in progress (OAR-A01 open).

---

### GR-004 — Conflicting Decisions Across Packs

**Risk:** Acumatica BU Lead approves 4-week hypercare (BU-ACU-008) but BeBanking BU Lead approves 6-week hypercare (BU-BB-004). APPSolve has two different standards in its approved packs.

**Impact:** Proposals combining Acumatica and BeBanking services cannot cite a consistent hypercare policy. Commercial confusion with clients.

**Similar risk:** BU-ACU-012 and BU-BB-009 both address POPIA — if approved with different disclosure language, APPSolve's published POPIA position is inconsistent.

**Mitigation:**
- Resolve BU-ACU-008 and BU-ACU-012 in the Acumatica workshop (Wave 2 or 3)
- Present the Acumatica-approved answers as recommended defaults in the BeBanking workshop
- If BeBanking BU Lead wants to diverge, flag for Commercial Director resolution before finalising

---

### GR-005 — Scope Change to Assumption Pack After BU Approval

**Risk:** After a pack is promoted to Approved v1.0, a BU Lead requests a change to one or more assumptions (new product feature, regulatory change, partner policy change).

**Impact:** Approved pack is stale; proposals assembled from it may include outdated assumptions.

**Mitigation:**
- Changes to Approved packs require: (a) new WP designation, (b) new Decision Record, (c) new BU Lead sign-off
- Version the pack: Approved v1.0 → v1.1 after change
- TENDER_ASSUMPTION_ASSEMBLY_RULES.md governs which pack version is authoritative

---

### GR-009 — Commercial Director Unavailable for Dual-Approval Decisions

**Risk:** The following decisions require both BU Lead and Commercial Director sign-off: BU-BB-006, BU-BB-002, BU-BB-003, BU-ACU-011. If Commercial Director is unavailable for Wave 2 BeBanking and Acumatica HIGH workshops, these decisions are blocked.

**Impact:** BeBanking support model (BU-BB-006 CRITICAL) and forex scope (BU-BB-003) remain unresolved. All BeBanking proposals are blocked. Acumatica non-PaySpace payroll policy (BU-ACU-011) is unresolved.

**Mitigation:**
- Book Commercial Director calendar for Wave 2 workshops as highest priority
- BU-BB-006 Wave 1 call should include Commercial Director — this resolves the most urgent item asynchronously

---

### GR-010 — Acumatica Partner Certificate Cannot Be Obtained

**Risk:** Acumatica BU Lead checks the Partner Portal and finds: (a) certificate expired, (b) partner tier has changed downward, or (c) APPSolve is no longer an active Acumatica partner.

**Impact:** BU-ACU-009 cannot be resolved with a positive outcome. ACU-GEN-001 (partner tier assumption) cannot be approved as written. All Acumatica proposals citing partner status are at risk.

**Mitigation:**
- If downgraded: amend ACU-GEN-001 to reflect current tier; update all proposal language immediately
- If certificate expired: obtain renewal before promoting Acumatica pack to Approved
- This is CRITICAL — do not proceed with any Acumatica proposal until confirmed

---

### GR-012 — Proposal Assembled from Draft Pack

**Risk:** Under time pressure, an AI session or team member assembles a tender response using assumptions from a Draft pack (ACU, BB, REC, LRN, TLT, or COM) before BU Lead approval.

**Impact:** Commercial exposure — proposal may include incorrect partner tier claims, unsupported service commitments, or non-compliant POPIA disclosures.

**Mitigation:**
- AI_CONTEXT.md: "Do NOT use in client-facing proposals until BU Lead approval complete" — both Acumatica and BeBanking packs
- TENDER_ASSUMPTION_ASSEMBLY_RULES.md: `approved_for_reuse: No` in all Draft pack frontmatter
- AI must check `approved_for_reuse` flag before including any assumption in a proposal
- If a proposal cannot wait, Commercial Director must approve an exception in writing

---

## Risk Summary by Pack

| Pack | Primary Risk | Rating | Key Mitigation |
|---|---|---|---|
| Acumatica | GR-010 (partner cert missing) + GR-001 (BU Lead availability) | HIGH | Verify cert immediately; Wave 1 email action |
| BeBanking | GR-001 (BU-BB-006 unresolved) + GR-009 (Commercial Director) | HIGH | Wave 1 call by 2026-06-23; book CD now |
| Oracle HCM | GR-002 (BU Lead availability) | MEDIUM | Schedule Wave 2 call (30 min) by 2026-06-20 |
| OCI | No governance risk | NONE | Already Approved v1.0 |

---

## Risk Register Update Protocol

| Trigger | Action |
|---|---|
| Risk materialises | Update status to "Active"; record date and impact |
| Risk avoided / resolved | Update status to "Closed"; note how it was resolved |
| New risk identified | Add row with next available GR-NNN ID; assign owner |
| Wave completed | Review all MEDIUM and LOW risks; close where appropriate |

---

*Governance Risk Register v1.0 | WP13 | 2026-06-16*
