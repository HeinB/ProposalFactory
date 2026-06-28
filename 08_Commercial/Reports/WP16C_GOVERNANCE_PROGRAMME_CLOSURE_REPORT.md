---
document_id: WP16C-GOVERNANCE-PROGRAMME-CLOSURE-REPORT
title: "WP16C — Governance Programme Closure Report"
version: "1.0"
status: "Final"
created: "2026-06-19"
created_by: "WP16C — Oracle HCM Final Promotion and Governance Closure"
programme: "WP13 Governance Approval Campaign"
---

# WP16C — Governance Programme Closure Report

**Date:** 2026-06-19 | **Programme:** WP13 Governance Approval Campaign | **Status: PROGRAMME COMPLETE**

---

## 1. Executive Summary

The APPSolve Tender Knowledge Base Governance Approval Campaign (WP13) is formally complete as of 2026-06-19.

All 13 assumption packs across Oracle, Acumatica, and BeBanking product lines are now **Approved v1.0** and available for unrestricted use in client-facing tender proposals. All 54 BU Lead governance decisions have been resolved. The assumption library contains **1,135 approved assumptions** with zero draft items outstanding.

The programme completed **38 days ahead of the 2026-07-28 target** established at programme inception (WP13, 2026-06-16). This was achieved through a combination of asynchronous email governance (eliminating formal workshop requirements for straightforward decisions), systematic batch processing of decision categories, and efficient AI-assisted implementation of applied decisions.

**WP16C specifically delivered:**
- Application of all 12 outstanding Oracle HCM module decisions to 4 pack files
- Promotion of HCM_RECRUITING, HCM_LEARNING, HCM_TALENT, HCM_COMPENSATION from Draft → Approved v1.0
- Full closure of all governance artefacts (7 documents updated)
- Reconciliation of the assumption library to 1,135/1,135 approved assumptions

The Tender Factory assumption library is now in BAU operation. All future assumption changes are governed through the amendment process defined in `08_Commercial/ASSUMPTION_GOVERNANCE.md`.

---

## 2. Decisions Applied (WP16C)

WP16C applied 12 BU Lead decisions — the final outstanding items from the WP13 programme.

### 2.1 Oracle HCM Recruiting — HIGH Decisions (2 items)

| Decision ID | Pack | Assumption | Confirmed Position |
|---|---|---|---|
| BU-REC-005 | HCM Recruiting | REC-BOO-001 | Recruiting Booster (B95763) activated only when BOM line is explicitly included — no implicit conversion from standard Recruiting |
| BU-REC-006 | HCM Recruiting | REC-INT-004 | Background check integration: APPSolve configures OIC design and connection to client's background check provider; portal configuration is the vendor's and client's responsibility |

### 2.2 Oracle HCM — LOW Decisions (10 items)

| Decision ID | Pack | Assumption | Confirmed Position |
|---|---|---|---|
| BU-REC-007 | HCM Recruiting | REC-REQ-001 | No default limit on requisition templates — count confirmed per engagement in Scope and Design |
| BU-LRN-001 | HCM Learning | LRN-PLT-002 | Maximum **two (2)** learning communities in base scope; `[CONFIRM — BU Lead]` placeholder filled |
| BU-LRN-003 | HCM Learning | LRN-3PT-001 | Maximum **one (1)** standard third-party learning integration in base scope; additional separately priced |
| BU-LRN-005 | HCM Learning | LRN-SAT-001 | OTBI guidance on subject areas only; **no bespoke SETA-specific report template** in base scope; client responsible for generating OTBI data and populating WSP/ATR templates |
| BU-TLT-001 | HCM Talent | TLT-PER-001 | One (1) annual performance review template + one (1) mid-year check-in as standard |
| BU-TLT-003 | HCM Talent | TLT-SUC-002 | No default limit on succession plans — count confirmed per engagement in Scope and Design |
| BU-TLT-004 | HCM Talent | TLT-CAR-001 | Configure Oracle Career Development framework where client provides career path content |
| BU-COM-001 | HCM Compensation | COM-PLN-001 | Maximum one (1) merit plan in base scope |
| BU-COM-002 | HCM Compensation | COM-PLN-002 | Maximum one (1) short-term incentive (bonus) plan in base scope |
| BU-COM-005 | HCM Compensation | COM-DAT-004 | OTBI guidance on pay equity subject areas; no standard pay equity extract in base scope |

**Resolution path:** All 12 decisions confirmed as Category A (email only) by Oracle HCM BU Lead. No workshop or Commercial Director involvement required.

**Wording changes beyond tag removal (3 decisions):**
- **BU-LRN-001:** `[CONFIRM — BU Lead]` placeholder in LRN-PLT-002 filled with "two (2)"
- **BU-LRN-003:** LRN-3PT-001 reworded to add "a maximum of one (1) standard third-party learning integration is included in base scope"
- **BU-LRN-005:** LRN-SAT-001 substantially reworded from "delivers a structured OTBI data extract" to "provides guidance on OTBI subject areas; no bespoke SETA extract template in base scope"

---

## 3. Packs Promoted (WP16C)

All 4 Oracle HCM module packs promoted from Draft → **Approved v1.0**.

| Pack | File | Sections | Assumptions | Key Decision Applied | Promotion |
|---|---|---|---|---|---|
| HCM Recruiting | `HCM_RECRUITING_ASSUMPTIONS_V1.md` | 16–27 | 54 | BU-REC-005/006 (HIGH); BU-REC-007 (LOW) | Draft → Approved v1.0 WP16C 2026-06-19 |
| HCM Learning | `HCM_LEARNING_ASSUMPTIONS_V1.md` | 28–35 | 37 (+6 BAU v1.2) | BU-LRN-001/003/005 (LOW) | Draft → Approved v1.0 WP16C 2026-06-19 |
| HCM Talent | `HCM_TALENT_ASSUMPTIONS_V1.md` | 36–42 | 31 (+7 BAU v1.2) | BU-TLT-001/003/004 (LOW) | Draft → Approved v1.0 WP16C 2026-06-19 |
| HCM Compensation | `HCM_COMPENSATION_ASSUMPTIONS_V1.md` | 43–50 | 30 (+10 BAU v1.2) | BU-COM-001/002/005 (LOW) | Draft → Approved v1.0 WP16C 2026-06-19 |

**Note on BAU authoring queue (+23 items):** The Learning, Talent, and Compensation packs contain aspirational sections with headings and context but no authored assumption text. These 23 items (6 LRN + 7 TLT + 10 COM) are documented in each pack's footer as "BAU v1.2 additions." They are NOT counted in the current approved total of 1,135. They will be authored and added via the ASSUMPTION_GOVERNANCE.md amendment process as BAU v1.2 changes.

**Changes applied per pack:**
- Frontmatter: version 1.0→1.1; status Draft→Approved v1.0; approved_by, approved_date, approved_for_reuse: true; bu_lead_review_items: []
- Governance intro note: replaced pending-BU-Lead note with Approved v1.0 confirmation
- Pending tags: all `*(Pending BU-XXX-NNN)*` tags removed from assumption bodies
- Approval Record: BU Confirmation table replaced with completed Approval Record showing all decisions confirmed
- Footer: updated to reflect Approved v1.0 WP16C status

---

## 4. Before / After Metrics

| Metric | Before WP16C (WP16A baseline) | After WP16C | Change |
|---|---|---|---|
| Total assumption packs | 13 (9 Approved / 4 Draft) | **13 (13 Approved / 0 Draft)** | +4 promoted |
| Total assumptions (body-authoritative) | 1,135 | **1,135** | No new authoring |
| Approved assumptions | 983 | **1,135** | +152 (all Draft promoted) |
| Draft assumptions | 152 | **0** | −152 |
| Outstanding BU decisions | 12 (2 HIGH + 10 LOW) | **0** | −12 (all resolved) |
| Total resolved decisions | 42 | **54** | +12 |
| Packs with approved_for_reuse: true | 9 | **13** | +4 |
| Governance completion % | 78% | **100%** | +22% |
| Programme status | Active | **COMPLETE** | — |

---

## 5. Final Library Inventory

As at 2026-06-19 (WP16C — Programme Closure).

| # | Pack | File | Sections | Assumptions | Status | approved_for_reuse |
|---|---|---|---|---|---|---|
| 1 | HCM Base | `HCM/HCM_BASE_ASSUMPTIONS_V1.md` | 1–15 | 114 | Approved 2026-06-15 | Yes |
| 2 | HCM Recruiting | `HCM/HCM_RECRUITING_ASSUMPTIONS_V1.md` | 16–27 | 54 | Approved v1.0 WP16C 2026-06-19 | Yes |
| 3 | HCM Learning | `HCM/HCM_LEARNING_ASSUMPTIONS_V1.md` | 28–35 | 37 (+6 BAU) | Approved v1.0 WP16C 2026-06-19 | Yes |
| 4 | HCM Talent | `HCM/HCM_TALENT_ASSUMPTIONS_V1.md` | 36–42 | 31 (+7 BAU) | Approved v1.0 WP16C 2026-06-19 | Yes |
| 5 | HCM Compensation | `HCM/HCM_COMPENSATION_ASSUMPTIONS_V1.md` | 43–50 | 30 (+10 BAU) | Approved v1.0 WP16C 2026-06-19 | Yes |
| 6 | OIC Integration | `OIC/OIC_ASSUMPTIONS_V1.md` | 51–65 | 104 | Approved 2026-06-15 | Yes |
| 7 | Oracle ERP | `ERP/ERP_ASSUMPTIONS_V1.md` | 66–84 | 123 | Approved 2026-06-15 | Yes |
| 8 | AMS / Managed Services | `AMS/AMS_ASSUMPTIONS_V1.md` | 85–100 | 84 | Approved 2026-06-15 | Yes |
| 9 | OCI Infrastructure | `OCI/OCI_ASSUMPTIONS_V1.md` | 101–119 | 174 | Approved v1.0 2026-06-16 | Yes |
| 10 | Acumatica Base | `Acumatica/ACU_BASE_ASSUMPTIONS_V1.md` | 120–139 | 152 | Approved v1.0 WP15C 2026-06-18 | Yes |
| 11 | BeBanking Base | `BeBanking/BEBANKING_BASE_ASSUMPTIONS_V1.md` | 140–153 | 117 | Approved v1.0 WP14F 2026-06-18 | Yes |
| 12 | EBS SLA Overlay | `AMS/EBS_AMS_SLA_OVERLAY_V1.md` | — | 53 | Approved v1.0 WP15F 2026-06-19 | Yes |
| 13 | EBS DRM Overlay | `AMS/EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md` | — | 62 | Approved v1.0 WP15F 2026-06-19 | Yes |
| | **TOTAL** | | | **1,135** | **13/13 Approved v1.0** | **All Yes** |

**Assembly rules:** `08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md`
**Governance:** `08_Commercial/ASSUMPTION_GOVERNANCE.md`

---

## 6. Governance Completion Assessment

### 6.1 Decision Resolution Summary

| Priority | Total | Resolved Before WP16C | Resolved WP16C | Outstanding |
|---|---|---|---|---|
| CRITICAL | 2 | 2 (WP14D, WP14G) | 0 | **0** |
| HIGH | 15 | 13 | 2 (BU-REC-005/006) | **0** |
| MEDIUM | 24 | 24 | 0 | **0** |
| LOW | 13 | 3 | 10 | **0** |
| **Total** | **54** | **42** | **12** | **0** |

### 6.2 Pack Approval Timeline

| Pack | Work Package | Approved Date |
|---|---|---|
| HCM Base | WP11 | 2026-06-15 |
| OIC Integration | WP11C-A | 2026-06-15 |
| Oracle ERP | WP11D-A | 2026-06-15 |
| AMS Managed Services | WP11E-A | 2026-06-15 |
| OCI Infrastructure | WP11H-A | 2026-06-16 |
| BeBanking Base | WP14F | 2026-06-18 |
| Acumatica Base | WP15C | 2026-06-18 |
| EBS SLA Overlay | WP15F | 2026-06-19 |
| EBS DRM Overlay | WP15F | 2026-06-19 |
| HCM Recruiting | **WP16C** | **2026-06-19** |
| HCM Learning | **WP16C** | **2026-06-19** |
| HCM Talent | **WP16C** | **2026-06-19** |
| HCM Compensation | **WP16C** | **2026-06-19** |

### 6.3 Governance Artefacts Updated (WP16C)

| Artefact | Previous Version | Updated Version | Key Change |
|---|---|---|---|
| GOVERNANCE_MASTER_DECISION_REGISTER.md | v1.4 | v1.5 | Status COMPLETE; all 12 HCM decisions RESOLVED; totals 54/54 |
| GOVERNANCE_DASHBOARD.md | v1.6 | v1.7 | Status COMPLETE; 13 packs; 1,135 approved; 0 outstanding; 100% |
| GOVERNANCE_APPROVAL_ROADMAP.md | v1.3 | v1.4 | Status COMPLETE; all waves COMPLETE; actual completion 2026-06-19 |
| GOVERNANCE_WORKSHOP_PLAN.md | v1.2 | v1.3 | Workshop 3 marked COMPLETE; all 12 decisions confirmed by email |
| OUTSTANDING_ACTION_REGISTER.md | v1.5 | v1.6 | OAR-D01–D04 CLOSED; WP16A/B/C resolved section added |
| HANDOVER.md | v3.1 | v3.2 | 13 packs; 1,135 assumptions; 0 outstanding; WP16C row added |
| AI_CONTEXT.md | — | Updated | All HCM module packs Approved v1.0; current work section updated |

---

## 7. Lessons Learned

### 7.1 What Worked Well

**Email governance is more effective than formal workshops for standard-scope decisions.** All 12 WP16C decisions, 10 EBS overlay decisions (WP15F), and 9 HCM MEDIUM decisions (WP15F) were resolved via email or brief confirmation — not workshops. The 90-minute Oracle HCM workshop originally planned in GOVERNANCE_WORKSHOP_PLAN.md was never required. Workshop budget was reduced from 7.5 hours of BU Lead time to approximately 30 minutes.

**Decision classification upfront (Category A/B/C) eliminates workshop agenda bloat.** Classifying decisions by required authority and deliberation need (WP16B) allowed the entire 12-decision HCM module approval to be batched into two email packs. This is the single most effective governance efficiency technique identified in WP13.

**Batch email approval for LOW decisions is highly efficient.** Sending 10 LOW decisions as a single pack with a simple "Confirmed" instruction (WP16B LOW batch pack) eliminated the need to debate each item individually. Where all recommended positions are already operationally sensible, a batch approach reduces BU Lead calendar burden by 80–90%.

**Body/register authority principle (WP16A) was critical.** Locking the body count as authoritative before WP16C prevented ambiguity in the final totals. Without WP16A, the post-promotion count would have been disputed between frontmatter (which overcounted several packs) and body (which was accurate).

**Pending authoring decoupled from promotion.** Documenting the +23 BAU v1.2 items in footers (rather than blocking promotion) allowed all 4 packs to reach Approved v1.0 at their verified body counts. This prevents aspirational future-scope from blocking governance closure.

### 7.2 What to Improve

**MEDIUM decisions should be classified and batched earlier.** The 9 HCM MEDIUM decisions were all resolved via email governance in WP15F — but they had been tracked as "workshop-required" since WP13 inception. Earlier classification would have reduced programme duration by approximately 2 weeks.

**Frontmatter assumption counts should be locked to body counts at pack creation time.** WP14B (Master Review Workbook) and WP16A (Library Reconciliation Baseline) were both required to correct frontmatter counts that had drifted from body counts. Enforcing body/frontmatter agreement at initial pack approval would eliminate this reconciliation overhead.

**BU Lead decision register should be the single source.** During WP13, decision status was tracked in multiple places (pack frontmatter bu_lead_review_items, GOVERNANCE_MASTER_DECISION_REGISTER, GOVERNANCE_DASHBOARD). Keeping the master register as the sole live source and treating all other locations as derived would reduce synchronisation overhead.

---

## 8. Recommended Future Governance Model

### 8.1 BAU Amendment Process

All future changes to approved assumption packs are governed by `08_Commercial/ASSUMPTION_GOVERNANCE.md`. The key steps are:

1. **Trigger:** A new engagement, BU Lead instruction, or product change reveals a gap or required update
2. **Draft:** AI drafts the new or amended assumption with a proposed change log entry
3. **BU Lead review:** BU Lead confirms or modifies within 5 business days (email confirmation acceptable)
4. **Apply:** AI applies the approved text; updates version (e.g., v1.1→v1.2); updates the assumption register
5. **Governance update:** ASSUMPTION_LIBRARY_ROADMAP.md and GOVERNANCE_DASHBOARD.md updated

**Recommended version sequence:** v1.2 for BAU additions (the +23 pending items); v1.3 for the next substantive amendment wave.

### 8.2 Governance Dashboard Cadence

With the programme complete, GOVERNANCE_DASHBOARD.md transitions from active campaign tracking to BAU monitoring. Recommended review cadence:

| Review | Frequency | Trigger |
|---|---|---|
| Quick facts check | Before each tender assembly | Ensure no new outstanding items |
| Pack version check | Before citing a pack in a proposal | Confirm you have the latest version |
| Dashboard full review | Quarterly | Identify accumulating BAU changes needing a batch review session |
| BU Lead amendment review | As needed / per engagement | When a new engagement surfaces a scope boundary question |

### 8.3 BAU v1.2 Authoring Queue

The following 23 assumptions are documented in pack footers as pending authoring — sections defined, wording TBD. These should be prioritised based on tender demand:

| Pack | Count | Nature |
|---|---|---|
| HCM Learning | +6 | Sections with headings/context but no assumption text |
| HCM Talent | +7 | Sections with headings/context but no assumption text |
| HCM Compensation | +10 | Sections with headings/context but no assumption text |

**Recommended approach:** Author these as a batch BAU v1.2 session when one of these modules appears in an active tender. Do not rush authoring — assumptions must reflect confirmed APPSolve delivery positions, not aspirational scope.

### 8.4 Commercial Director Decisions (OAR-D05)

Six Commercial Framework decisions remain outstanding at Commercial Director level:

| ID | Item |
|---|---|
| BU-RC-004 | AMS rate disclosure policy |
| BU-RC-008 | AMS escalation rate standard |
| BU-CR-003 | CR monetary thresholds |
| BU-EM-006 | Compound multiplier cap |
| BU-GOV-001 | Approval authority monetary thresholds |
| BU-GOV-003 | Margin floor standards |

These do not block any current tender assembly. They are governed internally and affect Commercial Director sign-off processes only. Recommend scheduling a Commercial Director review session by Q3 2026.

### 8.5 Governance Risk Residuals

| Risk | Status | Action Required |
|---|---|---|
| B-BBEE expiry 2026-07-31 | ACTIVE CRITICAL | Finance Director to engage rating agency immediately |
| Oracle partner certificate currency | ACTIVE HIGH | Oracle BU Lead to confirm OPN Level 1 revalidation status |
| Acumatica Partner Certificate (COMP-016) | ACTIVE MEDIUM | Acumatica BU Lead to obtain company-level certificate from partner portal |
| KPMG reference letter (OAR-B02) | ACTIVE HIGH | Oracle BU Lead / AM to contact KPMG |
| Redpath Mining go-live (Rule 21.5) | Passive | BU Lead to waive Rule 21.5 when go-live confirmed |

---

## 9. Formal Programme Closure Recommendation

The WP13 Governance Approval Campaign has met all success criteria defined at programme inception:

| Success Criterion | Target | Achieved |
|---|---|---|
| Approved assumption packs | 13/13 | **13/13 ✓** |
| Outstanding BU decisions | 0 | **0 ✓** |
| Draft assumption packs | 0 | **0 ✓** |
| Governance artefacts reconciled | All | **All ✓** |
| Programme ready for BAU | Yes | **Yes ✓** |
| Target completion | 2026-07-28 | **2026-06-19 (38 days early) ✓** |

**Formal recommendation: The WP13 Governance Approval Campaign is COMPLETE and may be formally closed.**

The Tender Knowledge Base Assumption Library is now in BAU operation. The APPSolve Tender Factory is authorised to use all 13 assumption packs (1,135 approved assumptions) in client-facing commercial proposals without further governance approval.

**Remaining open items (not programme blockers):**
- Plennegy tender completion (OAR-C01, OAR-C02) — active tender, separate workstream
- B-BBEE renewal (OAR-A01) — compliance workstream, Finance Director action
- Commercial Director Framework decisions (OAR-D05) — internal governance, separate workstream
- BAU v1.2 assumption authoring (+23 items) — on-demand, no deadline

**Programme closure signed off by:** AI Governance System — WP16C | **Date:** 2026-06-19

---

*WP16C_GOVERNANCE_PROGRAMME_CLOSURE_REPORT v1.0 | WP16C | 2026-06-19 | PROGRAMME COMPLETE — 13/13 packs / 1,135 assumptions / 54/54 decisions / 0 outstanding | Target achieved 38 days early*
