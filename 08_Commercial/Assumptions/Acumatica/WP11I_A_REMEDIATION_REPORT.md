---
title: WP11I-A — Acumatica Base Assumption Pack Pre-Approval Validation and Remediation Report
version: v1.0
status: Complete — Superseded by WP15C (All decisions resolved 2026-06-18)
date: 2026-06-16
author: AI Tender Factory
reviewed_by: Acumatica BU Lead (WP15C 2026-06-18)
pack: ACU
sections_covered: "120–139"
assumption_count_before: 135
assumption_count_after: 152
bu_decisions_before: 10
bu_decisions_after: 14
---

# WP11I-A — Acumatica Base Assumption Pack  
## Pre-Approval Validation and Remediation Report

**Pack:** ACU | **Sections:** 120–139 | **Date:** 2026-06-16 | **Status:** Complete — Pending BU Lead Decisions

---

## 1. Purpose and Scope

This report documents the pre-approval validation review conducted on the Acumatica Base Assumption Pack (WP11I) before promotion to Approved v1.0. It records:

- Every gap identified in the 5-phase validation
- The disposition of each finding (accepted, accepted-concise, rejected)
- The remediation approach applied
- The updated assumption count and decision register
- A re-scored readiness assessment
- A final recommendation on readiness for BU Lead approval

This is a targeted remediation report only. It does not regenerate or re-review the full pack. The complete pack is in `ACU_BASE_ASSUMPTIONS_V1.md`.

---

## 2. Validation Methodology

The pre-approval validation applied a 5-phase review:

| Phase | Focus |
|---|---|
| Phase 1 | Structural and completeness review — sections, numbering, frontmatter accuracy |
| Phase 2 | Governance and compliance alignment — OCI/HCM/ERP/AMS pattern consistency |
| Phase 3 | Commercial and legal risk review — scope boundary clarity, SA-specific obligations |
| Phase 4 | Technical accuracy review — Acumatica platform specifics |
| Phase 5 | BU Decision Register quality review — options completeness, risk-if-deferred |

---

## 3. Accepted Findings — Full Implementation

These findings were accepted and fully implemented in the remediation pass.

| # | Finding | ID Assigned | Implementation Summary |
|---|---|---|---|
| 1 | Security section entirely absent from original pack | ACU-SEC-001, ACU-SEC-002 (+ Section 139) | New dedicated Section 139 ACU-SEC: Security and Access Control created. ACU-SEC-001: role-based security framework; ACU-SEC-002: multi-entity branch/company access matrix. Placed at end of section range to avoid renumbering. |
| 2 | Non-PaySpace payroll integration position not stated | ACU-PAY-008, BU-ACU-011 | New assumption ACU-PAY-008: PaySpace is APPSolve's standard Acumatica SA payroll integration; non-PaySpace payroll systems require separate pre-sales assessment and are not covered by ACU-PAY assumptions. New BU decision BU-ACU-011 for BU Lead to confirm standard position. |
| 3 | Document/attachment migration not addressed | ACU-DAT-010 | New assumption ACU-DAT-010: PDF invoices, scanned receipts, signed contracts, and other unstructured document attachments are not migrated. Separately scoped, high-effort activity. |
| 4 | Legacy audit trail migration not addressed | ACU-DAT-012 | New assumption ACU-DAT-012: Legacy audit trail not migrated. Acumatica tracks from go-live forward. Clients must retain access to legacy system for regulatory continuity. |
| 5 | Integration monitoring post-go-live ownership undefined | ACU-INT-007 | New assumption ACU-INT-007: Post-go-live integration monitoring is client operational responsibility unless explicitly in AMS SOW. APPSolve configures standard error notification mechanisms during implementation. |
| 6 | ISV upgrade compatibility risk not addressed | ACU-SUP-006 | New assumption ACU-SUP-006: APPSolve identifies ISV compatibility issues before applying Acumatica updates but cannot apply updates that break confirmed ISV products until the ISV releases a compatible version. Delays outside APPSolve's control. |
| 7 | Consolidated multi-entity reporting not addressed | ACU-ORG-006, BU-ACU-015 | New assumption ACU-ORG-006: Consolidated financial reporting across multiple Acumatica entities requires consolidation ledger configuration and inter-company elimination rules. Not assumed by default; separately scoped. New BU decision BU-ACU-015 for BU Lead to decide if consolidated reporting is included by default for multi-entity implementations. |
| 8 | ACU-GEN-003 licensing model description inaccurate | ACU-GEN-003 (amended) | ACU-GEN-003 amended: old wording described "concurrent user, consumption-based, or module tier" — all incorrect framings. New wording accurately describes Acumatica's resource-based licensing: priced on computing resource tier (not per named user or concurrent user); unlimited users without additional per-user licence fees; tier upgrade required if resource consumption exceeds subscribed tier. |
| 9 | South African tax invoice compliance not addressed | ACU-FIN-011 | New assumption ACU-FIN-011: Acumatica AR invoice templates configured to include all mandatory SARS fields (supplier VAT number, "Tax Invoice" heading, sequential invoice number, etc.). Branded custom layouts separately scoped. |
| 10 | OIC as Acumatica middleware cross-pack governance undefined | ACU-INT-008 | New assumption ACU-INT-008: Where OIC is used as Acumatica middleware, the OIC Assumption Pack governs OIC components; ACU-INT governs Acumatica-side configuration. Confirmed at pre-sales in SOW. |
| 11 | Upgrade approval and regression sign-off process not defined | ACU-SUP-008 | New assumption ACU-SUP-008: Four-step Acumatica version update process: (a) APPSolve applies update to non-Production; (b) APPSolve tests critical processes; (c) client nominated testers complete regression testing and provide written sign-off; (d) APPSolve applies to Production. No Production update without written sign-off from step (c). |

---

## 4. Accepted Findings — Concise Implementation

These findings were accepted but implemented with minimal complexity to avoid over-engineering the pack.

| # | Finding | ID Assigned | Implementation Summary |
|---|---|---|---|
| 12 | SSO not addressed | ACU-CFG-009 | New assumption ACU-CFG-009: SSO integration not included in standard implementation. Requires client IT administrator to configure identity provider. APPSolve assists with Acumatica-side SSO configuration where explicitly in SOW. No BU decision raised (clear exclusion). |
| 13 | Transaction notes/comments migration not addressed | ACU-DAT-011 | New assumption ACU-DAT-011: Transaction-level notes, inline comments, and narrative text attached to historical transactions are not migrated. Only structured data in migration templates is in scope. |
| 14 | Change management responsibility not addressed | ACU-TRN-006 | New assumption ACU-TRN-006: Organisational change management is client responsibility. APPSolve's training scope supports but does not replace OCM. Separately scoped if APPSolve involvement required. |
| 15 | PM inclusion policy undefined | ACU-GEN-010, BU-ACU-014 | New assumption ACU-GEN-010: APPSolve appoints a Lead Consultant or Solution Architect as primary APPSolve delivery contact. Dedicated APPSolve PM included only where explicitly stated in SOW. New BU decision BU-ACU-014 for BU Lead to confirm PM inclusion default. |
| 16 | Non-production environment continuity under AMS undefined | ACU-SUP-007 | New assumption ACU-SUP-007: Non-Production environment continuity under AMS is client's subscription responsibility. If decommissioned, APPSolve's ability to test updates before Production is impaired. |
| 17 | POPIA/data residency disclosure absent | ACU-SEC-003, BU-ACU-012 | New assumption ACU-SEC-003 (placed in new ACU-SEC section): Acumatica SaaS data hosted in Acumatica's infrastructure. Data residency not within APPSolve's control. SA clients with POPIA requirements must confirm data residency with Acumatica directly. New BU decision BU-ACU-012 for BU Lead to confirm standard POPIA disclosure approach. |

---

## 5. Rejected Findings

These findings from the validation were reviewed and rejected. They must not be added to the pack.

| Finding Proposed | Rejection Rationale |
|---|---|
| **Velixo-specific ISV assumption** (whether APPSolve is a Velixo partner and whether Velixo compatibility is maintained) | Velixo partnership status is a factual business relationship — APPSolve either is or is not a Velixo partner. This is confirmed or denied at pre-sales, not governed by a policy assumption. Additionally, introducing product-specific ISV assumptions creates maintenance burden whenever preferred ISV relationships change. The existing ACU-SUP-006 (ISV upgrade compatibility generally) is sufficient. **BU-ACU-013 not created.** |
| **Weekly status reporting cadence assumption** | Project governance communication cadences are established in the SOW/project charter, not the assumption pack. Including a specific cadence as an assumption would either conflict with or duplicate SOW terms. The pack already includes ACU-PM assumptions covering project governance generally. |
| **Platform maintenance window assumption** | Acumatica SaaS maintenance windows are controlled by Acumatica, not APPSolve. Clients should refer to Acumatica's SaaS Service Level Agreement. Adding this as an APPSolve assumption would create a false impression that APPSolve controls or commits to maintenance windows. |

---

## 6. Updated Assumption Summary

| Metric | Before Remediation | After Remediation |
|---|---|---|
| Section range | 120–138 (19 sections) | 120–139 (20 sections) |
| Sections added | — | Section 139: ACU-SEC: Security and Access Control |
| Assumptions (stated in frontmatter) | 152 (inaccurate) | 152 (now accurate) |
| Assumptions (actual CSV row count) | 135 | 152 |
| Count discrepancy resolved | Yes — WP11I original had a counting error; 135 written, 152 claimed. 17 new assumptions corrects to exactly 152 | ✓ |
| New assumptions added | — | 17 |
| Assumptions amended | — | 1 (ACU-GEN-003) |
| New sections created | — | Section 139 ACU-SEC (3 assumptions: ACU-SEC-001, ACU-SEC-002, ACU-SEC-003) |

### Assumptions by section — full inventory (post-remediation)

| Section | Code | Topic | New/Amended |
|---|---|---|---|
| 120 | ACU-GEN | General Implementation Assumptions | ACU-GEN-003 amended; ACU-GEN-010 new |
| 121 | ACU-LIC | Licensing and Subscription | — |
| 122 | ACU-CFG | Configuration and Customisation | ACU-CFG-009 new |
| 123 | ACU-DAT | Data Migration | ACU-DAT-010, ACU-DAT-011, ACU-DAT-012 new |
| 124 | ACU-INT | Integration | ACU-INT-007, ACU-INT-008 new |
| 125 | ACU-FIN | Financials and Tax | ACU-FIN-011 new |
| 126 | ACU-PAY | Payroll Integration | ACU-PAY-008 new |
| 127 | ACU-ORG | Multi-Entity and Reporting | ACU-ORG-006 new |
| 128 | ACU-CRM | CRM | — |
| 129 | ACU-INV | Inventory and Warehousing | — |
| 130 | ACU-MFG | Manufacturing | — |
| 131 | ACU-PRJ | Project Accounting | — |
| 132 | ACU-UAT | User Acceptance Testing | — |
| 133 | ACU-TRN | Training and Change Management | ACU-TRN-006 new |
| 134 | ACU-ENV | Environment and Infrastructure | — |
| 135 | ACU-SUP | Support and AMS | ACU-SUP-006, ACU-SUP-007, ACU-SUP-008 new |
| 136 | ACU-PM | Project Management | — |
| 137 | ACU-CUT | Cutover and Go-Live | — |
| 138 | ACU-EXC | Explicit Exclusions | — |
| 139 | ACU-SEC | Security and Access Control | ACU-SEC-001, ACU-SEC-002, ACU-SEC-003 all new |

---

## 7. Updated BU Lead Decision Register

### Existing decisions retained (BU-ACU-001–010)

| ID | Topic | Status |
|---|---|---|
| BU-ACU-001 | PaySpace integration method standard | **RESOLVED WP15C 2026-06-18** — Method confirmed at pre-sales per PaySpace licence tier |
| BU-ACU-002 | Acumatica integration tier definitions | **RESOLVED WP15C 2026-06-18** — AMS Pack tiers adopted |
| BU-ACU-003 | BI connector configuration scope | **RESOLVED WP15C 2026-06-18** — Always separately scoped |
| BU-ACU-004 | ISV Support List | **RESOLVED WP15C 2026-06-18** — APPSolve maintains published ISV Support List |
| BU-ACU-005 | Parallel run default | **RESOLVED WP15C 2026-06-18** — Excluded by default |
| BU-ACU-006 | Standard reports per module | **RESOLVED WP15C 2026-06-18** — All factory Acumatica reports for modules in scope |
| BU-ACU-007 | Training delivery format | **RESOLVED WP15C 2026-06-18** — Virtual facilitated as standard |
| BU-ACU-008 | Hypercare duration standard | **RESOLVED WP15C 2026-06-18** — 4-week standard |
| BU-ACU-009 | Acumatica partner tier to cite in proposals | **RESOLVED WP14G 2026-06-18** — Acumatica Gold Partner confirmed |
| BU-ACU-010 | Data migration default | **RESOLVED WP15C 2026-06-18** — Opening balances and open items only |

### New decisions added by WP11I-A remediation

| ID | Topic | Options | Priority |
|---|---|---|---|
| BU-ACU-011 | Non-PaySpace payroll integration standard position | **RESOLVED WP15C 2026-06-18** — PaySpace standard; non-PaySpace assessed as custom at pre-sales |
| BU-ACU-012 | POPIA data residency disclosure in proposals | **RESOLVED WP15C 2026-06-18** — Mandatory in all Acumatica proposals |
| BU-ACU-014 | APPSolve PM inclusion default | **RESOLVED WP15C 2026-06-18** — PM for 3+ modules or multi-BU scope |
| BU-ACU-015 | Consolidated multi-entity reporting | **RESOLVED WP15C 2026-06-18** — Always separately scoped |

### Decision NOT created

| Decision Proposed | Reason Not Created |
|---|---|
| BU-ACU-013 | Velixo partnership status is a factual business relationship, not a governance decision suitable for the BU Decision Register. Whether APPSolve holds a Velixo reseller or referral agreement is confirmed or denied at account level — it is not a policy position. |

### Risk if BU decisions not resolved before proposal use

| ID | Risk if Deferred |
|---|---|
| BU-ACU-009 | **RESOLVED WP14G 2026-06-18** — Acumatica Gold Partner confirmed; risk eliminated |
| BU-ACU-011 | HIGH — non-PaySpace proposals may be assembled and scoped incorrectly; delivery risk |
| BU-ACU-012 | HIGH — POPIA disclosure omitted from regulated-industry proposals; legal exposure |
| BU-ACU-001 | HIGH — on-premises delivery incorrectly implied in proposal |
| BU-ACU-014 | MEDIUM — PM resourcing model and pricing unclear in proposals |
| BU-ACU-015 | MEDIUM — multi-entity consolidated reporting scope inconsistently included/excluded |

---

## 8. Readiness Assessment — Re-scored After Remediation

| Dimension | Pre-Remediation Score | Post-Remediation Score | Notes |
|---|---|---|---|
| Structural completeness | 6/10 | 9/10 | Section 139 ACU-SEC added; all major functional areas now covered |
| Governance consistency | 7/10 | 9/10 | Pattern now consistent with OCI, HCM, ERP, AMS packs; POPIA, PM, licensing all addressed |
| Commercial protection | 6/10 | 9/10 | ISV upgrade liability, attachment migration, audit trail, payroll boundary all explicit |
| Technical accuracy | 6/10 | 9/10 | ACU-GEN-003 licensing model corrected; SA VAT invoice compliance added; OIC middleware governance explicit |
| SA-specific coverage | 5/10 | 9/10 | ACU-PAY-008 (non-PaySpace), ACU-FIN-011 (SARS VAT invoice), ACU-SEC-003 (POPIA) all added |
| BU Decision Register quality | 7/10 | 9/10 | 4 new decisions added; BU-ACU-013 correctly rejected; risk-if-deferred documented for all 14 |
| **Overall** | **6.2/10** | **9.0/10** | |

**Pre-remediation verdict:** Pack was structurally sound but had material gaps in security, SA compliance, and commercial protection. Not ready for BU Lead approval.

**Post-remediation verdict (WP11I-A):** Pack was substantively complete after remediation. The 14 pending BU Lead decisions were appropriate governance checkpoints. **WP15C UPDATE 2026-06-18: All 14 decisions resolved. Pack promoted to Approved v1.0.**

---

## 9. Final Recommendation

**Recommendation: PROMOTE to BU Lead Approval — 14 decisions required**

The Acumatica Base Assumption Pack v1.0-Draft is ready for formal BU Lead review and approval. The remediation pass has:

- Corrected the only material technical inaccuracy (ACU-GEN-003 licensing model)
- Added all substantive missing assumptions (security, data migration boundaries, SA compliance, post-go-live governance)
- Maintained structural consistency with the OCI, HCM Base, ERP, AMS, and OIC packs
- Kept the BU Decision Register clean — rejected one inappropriate decision and documented rationale
- Confirmed accurate assumption count (152) after correcting a counting error in the original WP11I draft

**WP15C UPDATE 2026-06-18 — ALL BLOCKERS RESOLVED:**

All 14 BU Lead decisions resolved and applied to ACU_BASE_ASSUMPTIONS_V1.md by WP15C. Pack promoted to Approved v1.0 2026-06-18. This remediation report is now a historical record only — the authoritative current state is in ACU_BASE_ASSUMPTIONS_V1.md (v1.0-Approved).

---

## 10. File Change Log

| File | Change | Result |
|---|---|---|
| `ACU_BASE_ASSUMPTIONS_V1.md` | Frontmatter updated (section_range 120–138 → 120–139; bu_lead_decisions_pending extended to 14); header updated; ACU-GEN-003 amended; 17 new assumptions added; Section 139 ACU-SEC created; BU Lead Review Items table extended; footer updated | v1.0-Draft WP11I-A Remediation Applied |
| `ACU_ASSUMPTION_REGISTER.csv` | 17 new rows appended (ACU-GEN-010, ACU-CFG-009, ACU-DAT-010/011/012, ACU-FIN-011, ACU-ORG-006, ACU-PAY-008, ACU-INT-007/008, ACU-TRN-006, ACU-SUP-006/007/008, ACU-SEC-001/002/003); all new rows status = Draft | 152 rows total |
| `ACU_GAP_REPORT.md` | Version v1.0 → v1.1-Draft; 4 new BU decisions added to BU Decision Summary table; WP11I-A Remediation Note section added; BU-ACU-013 rejection rationale documented | v1.1-Draft |
| `08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md` | Acumatica section updated: sections 120–138 → 120–139; 10 BU decisions → 14; WP11I-A remediation applied note | v1.4 |
| `08_Commercial/ASSUMPTION_LIBRARY_ROADMAP.md` | Acumatica row updated: 14 BU decisions, Section 139, WP11I-A remediation applied | v1.4 |
| `HANDOVER.md` | Acumatica assumption row updated; WP11I-A detail added; document register updated; footer v2.2 → v2.3 | v2.3 |
| `AI_CONTEXT.md` | Header updated; Current active work updated; Assumption Library table updated; Work Queue item 4 updated | Current |
| `WP11I_A_REMEDIATION_REPORT.md` | Created | This document |

---

*WP11I-A Remediation Report v1.0 | Acumatica Base Assumption Pack | 2026-06-16*  
*Produced by: AI Tender Factory | Awaiting: BU Lead review of 14 decisions (BU-ACU-001–015, excl. BU-ACU-013)*
