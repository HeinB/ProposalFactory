---
document_id: WP15C-ACUMATICA-PROMOTION-REPORT
title: "WP15C — Acumatica Base Pack Promotion Report"
version: "1.0"
status: "Final"
created: "2026-06-18"
created_by: "WP15C — Acumatica Final Decision Application and Promotion to Approved v1.0"
pack_promoted: "Acumatica Base (ACU)"
pack_version_before: "Draft — Pending BU Lead Approval"
pack_version_after: "Approved v1.0"
decisions_applied: 14
decisions_outstanding_before: 14
decisions_outstanding_after: 0
approved_for_reuse: true
---

# WP15C — Acumatica Base Pack Promotion Report

**Pack:** Acumatica Base (ACU) | **Date:** 2026-06-18 | **Programme:** WP15C

---

## 1. Promotion Summary

The Acumatica Base Assumption Pack has been formally promoted from **Draft — Pending BU Lead Approval** to **Approved v1.0** following the resolution and application of all 14 BU Lead governance decisions.

| Metric | Before WP15C | After WP15C |
|---|---|---|
| Pack status | Draft — Pending BU Lead Approval | **Approved v1.0** |
| `approved_for_reuse` | false | **true** |
| BU decisions outstanding | 14 | **0** |
| BU decisions resolved | 1 (BU-ACU-009 via WP14G) | **14** |
| Assumptions in pack | 152 (all Draft status) | **152 (all Approved)** |
| Usable in proposals | No | **Yes — without restriction** |

---

## 2. Decision Summary — All 14 BU Lead Decisions

| ID | Title | Priority | Resolution | Applied to |
|---|---|---|---|---|
| BU-ACU-001 | PaySpace integration method | HIGH | **RESOLVED** — Method confirmed at pre-sales per PaySpace licence tier (API preferred; file-based fallback if no API access) | ACU-PAY-001, ACU-PAY-004 |
| BU-ACU-002 | Integration tier definitions | HIGH | **RESOLVED** — AMS Pack tiers adopted for Acumatica: Simple (standard connector/API, no transformation) / Standard (custom API, mapping, transformation) / Complex (multi-step, event-driven, bi-directional real-time) | ACU-INT-001 |
| BU-ACU-003 | BI connector scope | HIGH | **RESOLVED** — Always separately scoped; never assumed within standard implementation scope | ACU-REP-004 |
| BU-ACU-004 | ISV support policy | HIGH | **RESOLVED** — APPSolve maintains a published ISV Support List; proposals include ISV products only if on the list; list maintained by Acumatica BU Lead | ACU-EXT-003 |
| BU-ACU-005 | Parallel run default | MEDIUM | **RESOLVED** — Excluded by default; must be explicitly included in the SOW with defined duration, scope, and reconciliation responsibilities | ACU-CUT-002 |
| BU-ACU-006 | Standard report set per module | MEDIUM | **RESOLVED** — All factory-delivered Acumatica reports for each module in scope are included as standard; custom report development separately scoped | ACU-REP-001 |
| BU-ACU-007 | Training delivery format | MEDIUM | **RESOLVED** — Virtual facilitated training (MS Teams or Zoom) is the standard default; on-site training available at additional cost; travel and accommodation billed at actual cost | ACU-TRN-002 |
| BU-ACU-008 | Hypercare duration | MEDIUM | **RESOLVED** — 4 weeks (28 calendar days) standard; consistent with BeBanking Base Pack (BU-BB-004) and Oracle implementation standards; commences on go-live date | ACU-CUT-005 |
| BU-ACU-009 | Acumatica partner tier | CRITICAL | **RESOLVED WP14G 2026-06-18** — APPSolve is an Acumatica Gold Partner; never cite "Gold Certified" | ACU-GEN-009 |
| BU-ACU-010 | Legacy data migration default | MEDIUM | **RESOLVED** — Opening balances and open items only (GL trial balance, open AR, open AP, open POs, open SOs, current inventory on-hand); historical transaction migration always separately scoped | ACU-DAT-005 |
| BU-ACU-011 | Non-PaySpace payroll policy | HIGH | **RESOLVED** — PaySpace is the standard Acumatica payroll integration target; clients using alternative SA payroll systems assessed at pre-sales; where feasible, delivered as Custom Integration, separately scoped and priced at custom integration rates | ACU-PAY-008 |
| BU-ACU-012 | POPIA data residency disclosure | HIGH | **RESOLVED** — Mandatory disclosure in all Acumatica proposals regardless of client industry sector; specific wording locked in ACU-SEC-003 | ACU-SEC-003 |
| BU-ACU-013 | (Not created — factual business relationship, not a governance decision) | — | NOT CREATED — excluded from scope by design | — |
| BU-ACU-014 | PM inclusion default | MEDIUM | **RESOLVED** — Dedicated APPSolve PM included where 3 or more Acumatica modules in scope, or where implementation spans more than one client business unit; Lead Consultant manages smaller implementations | ACU-GEN-010 |
| BU-ACU-015 | Multi-entity consolidated reporting default | MEDIUM | **RESOLVED** — Consolidated reporting not assumed by default for any multi-entity implementation; always separately scoped | ACU-ORG-006 |

---

## 3. Files Updated

### Pack Files

| File | Change | Status |
|---|---|---|
| `ACU_BASE_ASSUMPTIONS_V1.md` | Frontmatter promoted (Draft → Approved v1.0); `approved_for_reuse: true`; all 14 decisions applied to relevant assumptions; BU Lead Review Items table rewritten to "All RESOLVED"; footer updated | **UPDATED** |
| `ACU_ASSUMPTION_REGISTER.csv` | All 152 rows: status "Draft" → "Approved"; 6 short_description fields updated to reflect resolved wording | **UPDATED** |
| `ACU_GAP_REPORT.md` | Status: Closed; all 14 BU Decision entries → "RESOLVED WP15C 2026-06-18"; frontmatter updated (decisions_resolved: 14, outstanding: 0, version: 1.2-Approved) | **UPDATED** |
| `ACU_SCOPE_BOUNDARY_GUIDE.md` | Version: 1.0-Draft → 1.0-Approved; status: Approved v1.0 — WP15C 2026-06-18 | **UPDATED** |
| `WP11I_A_REMEDIATION_REPORT.md` | Status: Complete — Superseded by WP15C; all decision table entries → RESOLVED; post-remediation section updated | **UPDATED** |

### Governance Files

| File | Change | Status |
|---|---|---|
| `GOVERNANCE_MASTER_DECISION_REGISTER.md` | v1.2 → v1.3; decisions_resolved 11 → 24; outstanding 34 → 21; HIGH outstanding 9 → 2; MEDIUM outstanding 15 → 9; Acumatica sections rewritten to "ALL RESOLVED WP15C"; programme totals table updated | **UPDATED** |
| `GOVERNANCE_DASHBOARD.md` | v1.3 → v1.4; Pack Approval Status: Acumatica Draft → Approved v1.0; Decision Priority View: HIGH 9→2 outstanding, MEDIUM 15→9 outstanding, Total 34→21 outstanding; Acumatica pack progress 1/14 → 14/14; Governance Scorecard: approved packs 6/11→7/11; Executive Reporting Table updated; footer updated | **UPDATED** |
| `GOVERNANCE_APPROVAL_ROADMAP.md` | v1.1 → v1.2; W2-A and W3-A/B marked COMPLETE; Post-Wave 3 steps 1–4 marked COMPLETE; outstanding: 34 → 21 | **UPDATED** |
| `GOVERNANCE_WORKSHOP_PLAN.md` | v1.0 → v1.1; Workshop 2 Acumatica section marked COMPLETE; all wave 2 + wave 3 agenda items replaced with resolution summaries | **UPDATED** |
| `OUTSTANDING_ACTION_REGISTER.md` | v1.2 → v1.4; OAR-D07 status CLOSED; Category D open items 6→5; Category total 48→47; WP15C resolved section added | **UPDATED** |
| `HANDOVER.md` | v2.7 → v2.8; header updated; Quick Facts updated (7 approved packs; 882 assumptions; 4 draft packs; 173 pending); System Maturity rows added (WP15A.1, WP15C); Assumption Library table updated; Architecture Decisions updated; Document Register updated | **UPDATED** |
| `AI_CONTEXT.md` | Header updated; Current active work updated; Assumption Library table updated (Acumatica → Approved v1.0); Work Queue item 4 marked COMPLETE | **UPDATED** |

---

## 4. Validation Results

| Check | Result | Notes |
|---|---|---|
| All 14 BU decisions resolved | **PASS** | BU-ACU-001–015 (excl. 013); BU-ACU-009 via WP14G; remainder via WP15C |
| `approved_for_reuse` set to true | **PASS** | Set in frontmatter of ACU_BASE_ASSUMPTIONS_V1.md |
| `status` updated to "Approved v1.0" | **PASS** | Frontmatter and header updated |
| `approved_by` field populated | **PASS** | "Acumatica BU Lead" |
| `approved_date` field populated | **PASS** | "2026-06-18" |
| All 152 register rows status = Approved | **PASS** | replace_all operation applied |
| Resolution tags applied to assumptions | **PASS** | 14 assumptions updated with `[BU-ACU-NNN: RESOLVED WP15C 2026-06-18]` |
| Cross-pack alignment — hypercare 4 weeks | **PASS** | BU-ACU-008 (4 weeks) = BU-BB-004 (BeBanking) = Oracle AMS standard |
| Cross-pack alignment — POPIA | **PASS** | BU-ACU-012 mandatory disclosure consistent with BeBanking POPIA standard |
| Governance counts consistent | **PASS** | 24 resolved + 21 outstanding = 45 total; verified across Dashboard, Roadmap, Register |
| GAP_REPORT closed | **PASS** | 0 outstanding gaps; status = Closed |
| BU-ACU-013 correctly excluded | **PASS** | Not created; excluded from scope; documented in Gap Report |
| Dependency check — BeBanking payroll rule | **PASS** | BeBanking Payroll H2H = Oracle EBS/Fusion only; Acumatica payroll prohibition unchanged |
| No CRITICAL decisions outstanding | **PASS** | 0 CRITICAL decisions remain across all packs |

---

## 5. Programme Impact

### Before / After WP15C

| Metric | Before | After | Delta |
|---|---|---|---|
| Approved packs | 6 | **7** | +1 |
| Approved assumptions | 730 | **882** | +152 |
| Pending/Draft assumptions | 325 | **173** | -152 |
| Outstanding BU decisions | 34 | **21** | -13 |
| Resolved BU decisions | 11 | **24** | +13 |
| Programme readiness | 55% (6/11 packs) | **64% (7/11 packs)** | +9% |
| HIGH decisions outstanding | 9 | **2** | -7 |
| MEDIUM decisions outstanding | 15 | **9** | -6 |
| CRITICAL decisions outstanding | 0 | **0** | — |

### Governance Scorecard After WP15C

| Dimension | Score |
|---|---|
| Approved packs | **7 / 11 (64%)** |
| Critical decisions resolved | **2 / 2 (100%)** |
| HIGH decisions resolved | **11 / 13 (85%)** |
| Overall governance readiness | **7.5 / 10** |

---

## 6. Remaining Outstanding Decisions

All 21 remaining decisions are in Oracle HCM module packs (not Acumatica). No Acumatica decisions remain.

| Pack | Count | IDs | Priority |
|---|---|---|---|
| HCM Recruiting | 7 | BU-REC-001–007 | 2 HIGH (005, 006); 4 MEDIUM (001–004); 1 LOW (007) |
| HCM Learning | 5 | BU-LRN-001–005 | 0 HIGH; 2 MEDIUM (002, 004); 3 LOW (001, 003, 005) |
| HCM Talent | 4 | BU-TLT-001–004 | 0 HIGH; 1 MEDIUM (002); 3 LOW (001, 003, 004) |
| HCM Compensation | 5 | BU-COM-001–005 | 0 HIGH; 2 MEDIUM (003, 004); 3 LOW (001, 002, 005) |
| **Total** | **21** | | **2 HIGH; 9 MEDIUM; 10 LOW** |

**Owner:** Oracle HCM BU Lead (all 21 decisions)

---

## 7. Governance Constraints Applied (Active in Promoted Pack)

The following permanent governance rules are embedded in the promoted Acumatica Base Pack and must be observed in all proposals using this pack:

| Rule | Wording in Pack |
|---|---|
| Partner tier | "Acumatica Gold Partner" only — never "Gold Certified" (BU-ACU-009; Constraint 9) |
| PaySpace standard | PaySpace is the standard Acumatica payroll integration; non-PaySpace assessed at pre-sales (BU-ACU-011) |
| POPIA disclosure | Mandatory in all Acumatica proposals regardless of client industry sector (BU-ACU-012) |
| ISV support | Only ISVs on the published ISV Support List may be included in proposals (BU-ACU-004) |
| Parallel run | Excluded by default; SOW explicit inclusion required (BU-ACU-005) |
| Historical data migration | Opening balances and open items only; history always separately scoped (BU-ACU-010) |
| Hypercare | 4 weeks standard; consistent with BeBanking and Oracle (BU-ACU-008) |
| BeBanking payroll H2H | BeBanking Payroll H2H = Oracle EBS/Fusion payroll only — never Acumatica payroll (Constraint 15, permanent) |
| Source pipeline | Only Approved status assumptions may be assembled into external documents (Constraint 18) |

---

## 8. Recommended Next Priority

**Immediate (before next tender):**
1. Obtain COMP-016 Acumatica Gold Partner Certificate from partner portal (OAR-E03) — individual certs on file; company-level cert missing
2. Acumatica BU Lead: publish ISV Support List (BU-ACU-004 resolution pending list creation)

**Next AI task:**
3. Oracle HCM module BU decisions (21 items) — schedule HCM BU Lead governance session using GOVERNANCE_WORKSHOP_PLAN.md Workshop 3 agenda
4. WP15A–WP15I remediation roadmap remaining items

**Ongoing:**
5. Plennegy: OAR-C01 (HB AM approval) + OAR-C02 (Costing section) + OAR-A01 (B-BBEE renewal 2026-07-31)

---

## 9. Promotion Confirmation

> **The Acumatica Base Assumption Pack (ACU_BASE_ASSUMPTIONS_V1.md) is formally Approved v1.0 as of 2026-06-18.**
>
> - All 14 BU Lead governance decisions resolved
> - `approved_for_reuse: true`
> - 152 assumptions available for inclusion in client-facing Acumatica proposals
> - No restrictions on proposal use
> - Governed by the permanent security, product boundary, and source pipeline rules listed in Section 7 above

---

*WP15C Acumatica Promotion Report v1.0 | 2026-06-18 | WP15C — Acumatica Final Decision Application and Promotion*
*Approved packs after WP15C: HCM Base, OIC, ERP, AMS, OCI, BeBanking Base, Acumatica Base (7 total)*
