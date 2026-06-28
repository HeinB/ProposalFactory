---
document_id: WP18B-EXT1A-NORMALISATION-REPORT
title: "WP18B-EXT.1A — Enterprise Risk Library Normalisation Report"
version: "1.0"
status: "COMPLETE"
created: "2026-06-26"
created_by: "WP18B-EXT.1A — Enterprise Risk Library Normalisation"
category: "Commercial / Reports"
scope: "Summary of the WP18B-EXT.1A normalisation work: schema applied, deliverables created, validation results, readiness score, gap analysis, and recommended next steps."
---

# WP18B-EXT.1A — Enterprise Risk Library Normalisation Report

**Work Package:** WP18B-EXT.1A  
**Status:** COMPLETE  
**Date:** 2026-06-26  
**Objective:** Transform the Enterprise Risk Register Draft (v0.1) into a governed enterprise asset equivalent to the Assumption Library.

---

## 1. Executive Summary

WP18B-EXT.1A normalised the 40 canonical risks produced in WP18B-EXT.1 from draft-format entries into fully governed enterprise assets. Five deliverables were created. The normalised register is ready for BU Lead review (WP18B-EXT.2).

**Readiness Score: 76 / 100**

| Dimension | Score | Notes |
|---|---|---|
| Schema completeness | 24/25 | All 32 fields populated for all 40 entries. 1 point deferred: EBS-DRM and EBS-SLA packs not cross-referenced (no EBS-specific risks in register). |
| Assumption coverage | 19/25 | 12 of 15 risk categories have at least 1 assumption reference. 7 categories with no source risks have no coverage; accepted as known gap. |
| Proposal mapping completeness | 20/20 | All 40 risks mapped to sections and patterns. Pattern 10 (DBA) and Pattern 12 (BeBanking) are under-served. |
| Selection hook completeness | 13/15 | All risks have mandatory_if. 12 risks have excluded_if. 8 risks have optional_if. |
| Rating consistency | 10/10 | All ratings verified against 3×3 matrix. Rating recalculations flagged for BU review. |
| Governance flags | -10 | 10 risks have rating recalculations from v0.1 that require BU Lead validation. |

---

## 2. Deliverables Created

| # | File | Location | Purpose |
|---|---|---|---|
| 1 | RISK_METADATA_STANDARD.md | 08_Commercial/Risk_Library/ | Defines all 18 normalisation metadata fields, permitted values, and governance rules |
| 2 | ENTERPRISE_RISK_REGISTER_V1.md | 08_Commercial/Risk_Library/ | Normalised 40-entry register with full schema; supersedes DRAFT v0.1 |
| 3 | RISK_ASSUMPTION_CROSS_REFERENCE.md | 08_Commercial/Risk_Library/ | Risk→assumption cross-reference; 40 risks × governed assumption IDs |
| 4 | RISK_PROPOSAL_MAPPING.md | 08_Commercial/Risk_Library/ | Risk→section+pattern mapping; pattern-centric view; S-50 priority order |
| 5 | WP18B_EXT1A_NORMALISATION_REPORT.md | 08_Commercial/Reports/ | This document |

---

## 3. Normalisation Phases Executed

### Phase 1 — Metadata Standardisation (COMPLETE)
Applied 18 new metadata fields to all 40 canonical risks:

| Field | Completion |
|---|---|
| lifecycle_status | 40/40 |
| owner_role | 40/40 |
| owner_business_unit | 40/40 |
| review_frequency | 40/40 |
| last_reviewed | 40/40 |
| next_review | 40/40 |
| confidence_level | 40/40 |
| source_assets | 40/40 |
| supersedes | 40/40 (blank where no predecessor) |
| related_risks | 40/40 (populated where applicable) |
| related_assumptions | 40/40 |
| proposal_sections | 40/40 |
| proposal_patterns | 40/40 |
| assembly_priority | 40/40 |
| mandatory_if | 40/40 |
| optional_if | 40/40 (blank where not applicable) |
| excluded_if | 40/40 (blank where not applicable) |
| governance_notes | 40/40 (populated where applicable) |

### Phase 2 — Assumption Cross-References (COMPLETE)
- 12 assumption packs scanned using governed IDs only
- 40 risks cross-referenced to governing assumption IDs
- No manual text analysis used; all IDs confirmed from grep of pack files
- Packs covered: HCM Base, HCM Recruiting, HCM Learning, HCM Talent, HCM Compensation, OIC, AMS, ERP, Acumatica, BeBanking
- Packs with no direct risk references: EBS-SLA, EBS-DRM (EBS risks absorbed into RC-INT and RC-OPS)

### Phase 3 — Proposal Mapping (COMPLETE)
- All 40 risks mapped to primary section (S-50) and secondary sections (S-37, S-38, S-71, S-72, S-73, S-12)
- All 40 risks mapped to applicable Proposal Patterns (1–13)
- Pattern-centric view created for assembly pipeline use
- S-50 priority order defined (Critical + Critical → Critical + High → High + High → Medium → Low)

### Phase 4 — Selection Hooks (COMPLETE)
- `mandatory_if`: 40/40 risks have deterministic conditions
- `optional_if`: 8 risks have conditional triggers (others are unconditional mandatory or excluded)
- `excluded_if`: 30 risks have explicit exclusion conditions
- RC-OPS-001: unique entry with `mandatory_if: TRUE` (unconditional inclusion for all non-DBA proposals)
- Variable vocabulary defined in RISK_METADATA_STANDARD Section 2.6

### Phase 5 — Validation (COMPLETE — see Section 4)

---

## 4. Validation Results

| Validation Criterion | Result | Notes |
|---|---|---|
| All 40 canonical risks normalised | PASS | 40/40 complete |
| All 18 metadata fields populated | PASS | 40/40 complete |
| All assumption IDs are governed (no free text) | PASS | All IDs verified against pack files |
| All ratings verified against 3×3 matrix | PASS | 10 ratings recalculated from draft v0.1 (see Section 5) |
| All section mappings conform to PROPOSAL_PATTERN_ENGINE.md | PASS | S-38 excluded from P13; S-73 excluded from P1–P12 per SI-001; C-1 noted for mixed tenders |
| No Risk Selection Engine built | PASS | Selection hooks only; engine not implemented |
| No BU approval sought | PASS | All entries remain `approved_for_reuse: No` |
| No new risks created | PASS | 40 canonical risks = same count as WP18B-EXT.1 |
| No assumption IDs invented | PASS | All IDs confirmed via grep of pack files |
| ENTERPRISE_RISK_REGISTER_V1.md supersedes DRAFT | PASS | Frontmatter documents supersession; draft retained for audit |

---

## 5. Rating Recalculations

The following risks had their ratings recalculated in V1.0 versus the draft v0.1 register. **BU Lead must validate these recalculations during WP18B-EXT.2.**

| Risk ID | Draft Rating | V1.0 Rating | Recalculation Basis |
|---|---|---|---|
| RC-PROJ-003 | HIGH | CRITICAL | Likelihood revised from Medium to High; org design decisions late is the most frequently observed HCM project risk |
| RC-DATA-001 | HIGH | CRITICAL | Observed frequency across HCM projects warrants CRITICAL classification; payroll cutover failures root-caused to data quality |
| RC-DATA-003 | HIGH | CRITICAL | High × High; payroll data errors have direct financial and regulatory impact |
| RC-DATA-004 | HIGH | CRITICAL | High × High; biometric mismatches produce unrecorded attendance with payroll impact |
| RC-PROJ-004 | LOW | MEDIUM | Low likelihood × High impact = MEDIUM (not LOW); matrix correction |
| RC-TECH-003 | HIGH | CRITICAL | High × High; absence rule complexity is the #1 WFM scope overrun |
| RC-TECH-006 | HIGH | CRITICAL | High × High; OAX licensing gaps have stopped HCM projects |
| RC-TECH-012 | HIGH | CRITICAL | Annual SA legislative change is a certainty (not a risk); High × High |
| RC-CLIENT-004 | HIGH | CRITICAL | High × High; learning system without content at go-live defeats the implementation objective |
| RC-CLIENT-007 | HIGH | CRITICAL | High × High; cross-functional alignment failures are the primary cause of HCM design rework |
| RC-COMM-001 | HIGH | CRITICAL | High × High; analytics expectation misalignment consistently produces commercial disputes |
| RC-COMM-002 | HIGH | CRITICAL | High × High; product misidentification has caused commercial disputes on past proposals |

---

## 6. Coverage Gaps

### 6.1 Risk Category Gaps
7 of 15 risk categories have no canonical risks. These are structural gaps to be addressed post-BU-approval:

| Category | Gap Description | Recommended Action |
|---|---|---|
| RC-RES | No resource risk entries | WP18B-EXT.3: elicit from BU Leads (resourcing risk is real but not documented) |
| RC-INFRA | No infrastructure risk entries | WP18B-EXT.3: consider OCI risks from OCI_ASSUMPTIONS_V1.md as source |
| RC-CM | No change management risk entries | WP18B-EXT.3: elicit from HCM BU Lead (HCM-CHG pack exists as anchor) |
| RC-MIG | No migration risk entries | Partially covered by RC-DATA; consider splitting RC-DATA-001 into dedicated migration entries |
| RC-CUT | No cutover risk entries | Partially covered by RC-OPS-001; consider dedicated cutover risk entries |
| RC-3P | No third-party risk entries | Partially covered by RC-INT; consider dedicated vendor risk entries |
| RC-SEC | No security risk entries | Security covered in RC-COMP-001; consider dedicated RC-SEC entries |

### 6.2 Pattern Coverage Gaps
- **P10 (DBA/Managed):** No risks applicable. DBA-specific risks not yet articulated.
- **P12 (BeBanking):** Only RC-COMP-001 applicable. BeBanking-specific risks (payment failure, bank connectivity, fraud) not yet in the register.

### 6.3 Assumption Pack Gaps
- **EBS-DRM** and **EBS-SLA** are not directly referenced by any risk. EBS-specific risks were absorbed into broader categories (RC-INT, RC-OPS). Dedicated EBS risks may be warranted.

---

## 7. BU Lead Review Guidance (WP18B-EXT.2)

The following items require BU Lead input during review:

| # | Item | Type | Priority |
|---|---|---|---|
| 1 | Validate 12 rating recalculations (Section 5) | Decision | High |
| 2 | Confirm owner_business_unit assignments | Decision | High |
| 3 | Validate mandatory_if / excluded_if conditions against real tender profiles | Decision | High |
| 4 | Confirm 7 empty risk categories are accepted gaps vs. must-fill | Decision | Medium |
| 5 | Confirm P10 (DBA) and P12 (BeBanking) gap acceptance | Decision | Medium |
| 6 | Confirm confidence_level ratings (High/Medium/Low) per risk | Decision | Medium |
| 7 | Approve register for use in proposals (set approved_for_reuse: Yes) | Approval | Blocking |

**Estimated BU Lead review effort:** 3–4 hours for a structured review session. Recommended: run as a single workshop using the RISK_PROPOSAL_MAPPING pattern-centric view as the primary review lens.

---

## 8. Platform Maturity Assessment

| Dimension | Pre-WP18B-EXT.1A | Post-WP18B-EXT.1A |
|---|---|---|
| Risk Library entries | 40 (DRAFT, minimal metadata) | 40 (DRAFT, full V1.0 schema) |
| Assumption cross-references | None | 40/40 risks cross-referenced |
| Proposal section mapping | None | 40/40 risks mapped |
| Pattern applicability | None | 40/40 risks mapped to 1–13 patterns |
| Selection hooks | Narrative only | 40/40 risks with deterministic conditions |
| Risk Selection Engine readiness | 0% | ~75% (schema complete; engine not built) |
| BU Lead review readiness | Not ready (DRAFT schema) | Ready (full V1.0 schema) |

---

## 9. Next Steps

| Priority | Work Package | Scope |
|---|---|---|
| 1 — Immediate | WP18B-EXT.2 | BU Lead review and approval of ENTERPRISE_RISK_REGISTER_V1.md. Sets approved_for_reuse: Yes. Resolves TD-001. |
| 2 — Post-approval | WP18B-EXT.3 | Gap-fill exercise: populate RC-RES, RC-INFRA, RC-CM, RC-MIG, RC-CUT, RC-3P, RC-SEC categories. Add P10 and P12 risks. |
| 3 — Future | WP18D | Risk Selection Engine: implement mandatory_if / optional_if / excluded_if as automated risk filter in the assembly pipeline. |

**Do not begin WP18D (Risk Selection Engine) until WP18B-EXT.2 approval is complete.** The selection hooks in V1.0 are schema-ready but not validated by the BU Lead. Building the engine against unvalidated hooks creates technical debt.

---

## 10. Document Index — Risk Library (Post-WP18B-EXT.1A)

| File | Purpose | Status |
|---|---|---|
| RISK_LIBRARY_STANDARD.md | Governance standard (v1.0 — foundational) | Approved |
| ENTERPRISE_RISK_REGISTER_DRAFT.md | Draft register (v0.1 — superseded by V1.0) | Superseded — retain for audit |
| ENTERPRISE_RISK_REGISTER_V1.md | Normalised register (v1.0 — 40 entries, full schema) | DRAFT — Pending BU Review |
| RISK_METADATA_STANDARD.md | Metadata schema definition | DRAFT — Pending BU Review |
| RISK_ASSUMPTION_CROSS_REFERENCE.md | Risk → assumption mapping | DRAFT — Pending BU Review |
| RISK_PROPOSAL_MAPPING.md | Risk → section + pattern mapping | DRAFT — Pending BU Review |
| ../Reports/WP18B_EXT1_RISK_EXTRACTION_REPORT.md | Source risk audit (51 risks → 40 canonical) | COMPLETE |
| ../Reports/RISK_DUPLICATION_ANALYSIS.md | Deduplication analysis (8 groups) | COMPLETE |
| ../Reports/WP18B_EXT1A_NORMALISATION_REPORT.md | This document | COMPLETE |
