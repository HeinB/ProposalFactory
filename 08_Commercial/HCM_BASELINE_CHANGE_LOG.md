---
document_id: HCM_BASELINE_CHANGE_LOG
title: "HCM Base Assumptions — Baseline Change Log"
version: "1.0"
created: "2026-06-15"
tracks: "HCM_BASE_ASSUMPTIONS_V1.md"
---

# HCM Base Assumptions — Baseline Change Log

This log records every assumption modified, added, or reclassified during the WP11A BU Lead approval cycle. Changes are permanent and reflected in `HCM_BASE_ASSUMPTIONS_V1.md` (version 1.0, Approved 2026-06-15) and `ASSUMPTION_REGISTER.csv`.

---

## Change Summary

| Change # | Assumption ID | Change Type | BU Decision | Summary |
|---|---|---|---|---|
| CL-001 | HCM-ENV-003 | Modified | BU-WP11-002 | Environment count specified: 1 Production + 1 Non-Production |
| CL-002 | HCM-ORG-006 | Modified | BU-WP11-004 | Position Management explicitly excluded; Job Management confirmed as default |
| CL-003 | HCM-SEC-002 | Modified | BU-WP11-005 | Custom role count confirmed: 4 roles (Employee, Line Manager, HR Admin, 1 additional) |
| CL-004 | HCM-TST-003 | Modified | BU-WP11-006 | CRP cycles named: CRP1=Design Validation; CRP2=End-to-End Validation |
| CL-005 | HCM-CUT-005 | Reclassified + Modified | BU-WP11-001 | Reversed from Exclusion to Assumption; parallel payroll run now INCLUDED where payroll replacement is in scope |
| CL-006 | HCM-CUT-008 | Added | BU-WP11-001 | New assumption defining parallel run conditions and scope boundaries |
| CL-007 | HCM-HYP-001 | Modified | BU-WP11-003 | Hypercare upgraded from "minimum" / guideline to contractual default; scope clarified |
| CL-008 | HCM-HYP-002 | Modified | BU-WP11-003 | SLAs confirmed contractual; extended hours explicitly excluded from default |
| CL-009 | HCM-HYP-003 | Modified | BU-WP11-003 | Enhancement exclusion itemised: enhancements, new scope, CRs, training all excluded from hypercare |
| CL-010 | HCM-GEN-001 | Modified | BU-WP11-007 | On-site activities revised from 5 (kick-off, CRP1, CRP2, UAT, go-live) to 2 (UAT support + Go-Live support) |
| CL-011 | HCM-GEN-002 | Modified | BU-WP11-007 | Travel assumption updated to reflect revised on-site scope |
| CL-012 | Frontmatter | Updated | All 7 decisions | Status: Draft → Approved; approved_by/approved_date set; assumption_count 97→114; bu_lead_review_items removed; bu_lead_decisions_applied added |
| CL-013 | ASSUMPTION_REGISTER.csv | Updated | All 7 decisions | 11 rows modified (statement + category); 1 row added (HCM-CUT-008); all statuses updated to Active |

---

## Detailed Change Records

### CL-001 — HCM-ENV-003 (BU-WP11-002)
**Change type:** Modified  
**Before:** "Oracle provides a standard set of non-production environments as part of the SaaS subscription. APPSolve scopes configuration and testing activities to the environments included in the Oracle SaaS contract. Additional environments beyond those included in the subscription are Oracle's commercial responsibility, not APPSolve's."  
**After:** Specifies exactly 1 production + 1 standard non-production environment. Explicitly states no assumption about multiple non-production tenants. Additional tenants must be client-licensed.  
**Commercial reason:** Prevents scope disputes where client expects DEV + TEST + UAT + PROD environments and assumes APPSolve configures all of them. Oracle standard SaaS includes 1 non-production tenant; additional tenants are separately purchased.  
**Risk mitigated:** Client expects APPSolve to configure 3–4 non-production environments; effort is materially higher than estimated for 1.

---

### CL-002 — HCM-ORG-006 (BU-WP11-004)
**Change type:** Modified  
**Before:** "APPSolve defaults to a job-based worker assignment model. If the client requires Oracle Position Management (hard or soft position control), this must be identified and agreed during the Scope and Design phase. Position Management imposes additional configuration complexity and may increase implementation effort."  
**After:** Explicitly states Job Management is the APPSolve default. Position Management is excluded (not just an optional addition) and requires explicit scoping. Use cases for Position Management added to guidance (headcount control, vacancy management).  
**Commercial reason:** Position Management is a fundamentally different configuration model — not a feature toggle. Clients who need it require a different implementation approach. The old wording implied it was a simple optional add. The new wording makes the commercial impact clear.  
**Risk mitigated:** Client assumes Position Management is a simple add-on; actual impact is significant additional design, testing, and data migration effort not priced in base estimate.

---

### CL-003 — HCM-SEC-002 (BU-WP11-005)
**Change type:** Modified  
**Before:** "APPSolve will configure a maximum of [INSERT NUMBER — confirm with BU Lead per engagement] custom job roles during this implementation. Custom job roles beyond the agreed number constitute a scope change."  
**After:** Confirmed count = 4 custom roles: (1) Employee, (2) Line Manager, (3) HR Administrator, (4) one additional custom role confirmed in Scope and Design. Roles beyond 4 are a Change Request.  
**Commercial reason:** The placeholder was a governance risk — proposals were going out with an unresolved number. Four roles covers >90% of standard HCM implementations. Bespoke security models requiring more roles require explicit scoping.  
**Risk mitigated:** Client expects 10+ custom roles for subsidiary HR leads, regional managers, compliance officers, etc.; scope not bounded in base estimate.

---

### CL-004 — HCM-TST-003 (BU-WP11-006)
**Change type:** Modified  
**Before:** "The implementation plan includes two Conference Room Pilot (CRP) cycles (CRP1 and CRP2) and one UAT cycle. Additional testing cycles beyond this plan (for example, a third CRP or a second UAT) constitute a scope change."  
**After:** CRP cycles named with purpose: CRP1=Design Validation (first rapid build; structured design feedback); CRP2=End-to-End Validation (complete end-to-end scenario test; final configuration sign-off). Wording makes it explicit that additional CRP cycles are not included and are a Change Request.  
**Commercial reason:** Naming the CRP cycles with their purpose sets client expectations on what each cycle achieves, reducing requests for additional cycles. CRP1 is often misunderstood as a full UAT; clarifying it as Design Validation reduces this confusion.  
**Risk mitigated:** Client expects additional CRP cycles when designs are incomplete; each additional CRP cycle adds consultant time not in budget.

---

### CL-005 — HCM-CUT-005 (BU-WP11-001)
**Change type:** Reclassified (Exclusion → Assumption) + Modified  
**Before (Exclusion):** "Parallel run of the legacy HR system and Oracle HCM simultaneously (dual processing) is not included in base scope. If the client requires a parallel processing period, this constitutes a scope addition and requires assessment of the effort involved in managing dual-system data integrity."  
**After (Assumption):** Parallel payroll run is INCLUDED by default where Oracle HCM is replacing a payroll-connected system. The duration, reconciliation approach, and exit criteria are confirmed in Scope and Design. See also HCM-CUT-008 for conditions.  
**Commercial reason:** The BU Lead confirmed that APPSolve's standard practice is to include a parallel payroll run for payroll-replacement implementations. Excluding it as the default was misaligned with delivery practice. This change correctly represents what APPSolve actually delivers.  
**Risk mitigated (original, now closed):** Proposal excludes parallel run; client expects it; scope dispute at cutover stage. New risk introduced: parallel run scope must be clearly bounded (addressed by HCM-CUT-008).  
**Register change:** Category changed from Exclusion to Assumption. Statement completely rewritten.

---

### CL-006 — HCM-CUT-008 (BU-WP11-001) — NEW
**Change type:** Added  
**Content:** New assumption defining the four conditions that bound the parallel payroll run inclusion: (a) applies to payroll interface outputs only (not Oracle native payroll); (b) payroll calculations remain the payroll provider's responsibility; (c) client's payroll team owns reconciliation; APPSolve provides configuration and interface support; (d) not applicable where Oracle HCM does not replace a payroll-connected system.  
**Commercial reason:** HCM-CUT-005 reversal creates the inclusion without defining its scope. HCM-CUT-008 bounds the scope so the parallel run is not interpreted as a full payroll migration, payroll outsourcing, or payroll calculation service.  
**Risk mitigated:** Without CUT-008, the parallel run inclusion could be misread as APPSolve running payroll. CUT-008 reinforces APPSolve's position as an integration partner, not a payroll provider (consistent with HCM-3PT-006 and the position in W3S1-009).

---

### CL-007 — HCM-HYP-001 (BU-WP11-003)
**Change type:** Modified  
**Before:** "A minimum four (4) week hypercare period commences immediately after the production go-live date. During hypercare, a senior APPSolve team is available to respond to and resolve production issues with high priority. Hypercare resource allocation and availability are defined in the SOW."  
**After:** "Minimum" removed — replaced with "contractual default." Scope of hypercare explicitly limited to defect resolution and stabilisation. Business hours constraint explicitly stated (08:00–17:00 SAST Mon–Fri). Enhancements, new functionality, new scope, and change requests explicitly excluded.  
**Commercial reason:** "Minimum" implied APPSolve might do more. "Contractual default" sets a clear, defensible standard. The scope limitation is essential — hypercare engagements frequently suffer scope creep when clients treat hypercare as an open-support commitment.  
**Risk mitigated:** Client assumes hypercare = unlimited support for any issue type; APPSolve team absorbed into enhancement work during hypercare at no additional cost.

---

### CL-008 — HCM-HYP-002 (BU-WP11-003)
**Change type:** Modified  
**Before:** SLA tiers listed; noted as applying "during standard South African business hours unless extended hours agreed in the SOW."  
**After:** SLAs described as "contractual during hypercare." Extended-hours/weekend support during hypercare explicitly priced as an additional service.  
**Commercial reason:** Making the SLAs contractual gives them enforceability in the SOW. Making extended hours a separate priced service prevents expectation that hypercare is 24/7.  
**Risk mitigated:** Client escalates P1 at 22:00 on a Friday and expects 2-hour response; APPSolve consultant on-call without commercial agreement.

---

### CL-009 — HCM-HYP-003 (BU-WP11-003)
**Change type:** Modified  
**Before:** "Issues classified as enhancements, new scope requests, or change requests (items not in the original agreed scope) are not resolved under hypercare."  
**After:** Expanded to itemise four excluded categories with specific examples: (a) enhancements — changes to delivered functionality; (b) new scope requests — functionality not in original SOW; (c) Change Requests — out-of-scope items; (d) training and user adoption support beyond the hypercare plan.  
**Commercial reason:** A short one-line exclusion was insufficient to prevent scope creep. The itemised list gives project managers a defensible checklist when clients push back on what is and is not in hypercare.  
**Risk mitigated:** "But this is a bug, not an enhancement" is the most common hypercare scope dispute. The itemised exclusions make the distinction unambiguous.

---

### CL-010 — HCM-GEN-001 (BU-WP11-007)
**Change type:** Modified  
**Before:** On-site activities: project kick-off, CRP1, CRP2, UAT facilitation, and go-live (5 events).  
**After:** On-site activities: UAT support and Go-Live support only (2 events). All other activities (kick-off, CRP1, CRP2) are explicitly remote.  
**Commercial reason:** The old assumption included 5 on-site milestones, creating significant implicit travel cost in every engagement. Reducing the default to 2 on-site events more accurately reflects APPSolve's remote-first delivery model and reduces proposal cost without reducing delivery quality. Clients who require more on-site presence can negotiate this in the SOW.  
**Risk mitigated:** Travel costs significantly exceed budget; APPSolve absorbs cost of 5 on-site trips not agreed in commercial proposal.

---

### CL-011 — HCM-GEN-002 (BU-WP11-007)
**Change type:** Modified  
**Before:** "Travel, accommodation, and subsistence costs for APPSolve consultants attending on-site at the client's premises are for the client's account."  
**After:** Updated to reference the revised on-site scope (UAT support and Go-Live support, and any additional days agreed in SOW). Travel approval process mention retained.  
**Commercial reason:** Aligned to CL-010 to ensure the travel assumption is consistent with the on-site assumption. A travel assumption that doesn't reference the on-site scope is incomplete.

---

### CL-012 — Frontmatter
**Change type:** Updated  
- `status`: Draft — Pending BU Lead Approval → **Approved**  
- `approved_by`: blank → **BU Lead — Oracle Practice**  
- `approved_date`: blank → **2026-06-15**  
- `approved_for_reuse`: false → **true**  
- `assumption_count`: 97 → **114** (includes HCM-CUT-008 and reflects correct total count of 113 from register + 1 new = 114)  
- `bu_lead_review_items`: removed (all 7 items closed)  
- `bu_lead_decisions_applied`: added (all 7 decisions recorded with affected assumptions)  

---

### CL-013 — ASSUMPTION_REGISTER.csv
**Change type:** Updated  
Rows modified: HCM-ENV-003, HCM-ORG-006, HCM-SEC-002, HCM-TST-003, HCM-CUT-005, HCM-HYP-001, HCM-HYP-002, HCM-HYP-003, HCM-GEN-001, HCM-GEN-002 (10 rows)  
Row added: HCM-CUT-008 (1 row)  
Status column: All 113 existing rows updated from `Draft` to `Active`; HCM-CUT-008 added as `Active`  
HCM-CUT-005 Category: `Exclusion` → `Assumption`  

---

## Impact Assessment

### Proposals Issued Before This Approval (WP13 — Plennegy Draft)
The Plennegy proposal draft (`PLENNEGY_DRAFT_RESPONSE.docx`) was generated before this approval. The following changes from this log affect that draft:

| Change | Impact on Plennegy Draft | Action |
|---|---|---|
| CL-001 (environments) | Plennegy draft does not specify environment count | Low impact — no conflict |
| CL-002 (Position Management) | Not referenced in Plennegy draft | No action required |
| CL-003 (custom roles) | Not referenced in Plennegy draft | No action required |
| CL-004 (CRP naming) | Section 8 uses CRP1/CRP2 language but without purpose names | Low impact — bid manager may update in final version |
| CL-005/CL-006 (parallel payroll run) | Section 13.1 Assumption implies parallel run excluded; this was based on the old draft assumption | **Update required** — Plennegy is a payroll-replacement implementation; revised assumption (CL-005) applies; bid manager to update assumptions section before submission |
| CL-007–CL-009 (hypercare) | Section 10 broadly consistent with updated HYP-001/002/003 | Minor — bid manager to confirm hypercare language is contractually consistent |
| CL-010/CL-011 (on-site) | Section 8 mentions CRP phases but does not specify on-site vs. remote | Low impact — bid manager to clarify on-site scope in final version |

**Net impact on Plennegy draft:** One update recommended (parallel run assumption in Section 13.1). All other changes are low-impact.

---

*HCM_BASELINE_CHANGE_LOG v1.0 | WP11A — BU Lead Approval | 2026-06-15*  
*13 changes applied | 7 BU decisions closed | HCM Base promoted to Approved*
