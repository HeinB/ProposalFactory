---
document_id: KNOWLEDGE-HEALTH-SCORE-V1
title: "Knowledge Health Score — Definition and Scoring Model V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-27"
created_by: "WP18D — Knowledge Validation Engine"
approved_by: "Architecture — WP18D"
approved_date: "2026-06-27"
approved_for_reuse: true
category: "Assembly Engine / Validation"
scope: "Defines the deterministic Knowledge Health Score (KHS) — a single 0–100 metric representing the overall governance, completeness, and assembly-readiness of the Knowledge Platform. Includes 7-dimension scoring model, weightings, score bands, calculation formula, and current-state estimates."
related_documents:
  - KNOWLEDGE_VALIDATION_ENGINE.md
  - KNOWLEDGE_REGISTRY_VALIDATION_RULES.md
  - KNOWLEDGE_VALIDATION_REPORT_STANDARD.md
---

# Knowledge Health Score — Definition and Scoring Model V1.0

**Work Package:** WP18D  
**Status:** APPROVED

---

## 1. Purpose

The Knowledge Health Score (KHS) is a single 0–100 integer that represents the overall health of the Knowledge Platform — its governance completeness, metadata quality, relationship integrity, and assembly readiness.

**The KHS is:**
- Deterministic: same registry state always produces the same score
- Decomposable: always accompanied by 7 dimension scores showing exactly what drives the total
- Actionable: each dimension maps to specific rules and specific remediation actions
- Comparable over time: enables trend tracking (improving / stable / declining)
- Independent of any specific proposal: it measures the platform, not a tender outcome

**The KHS is NOT:**
- A proposal quality score (that is the Proposal QA Engine's function)
- A pass/fail gate (only the KVE BLOCK rules are absolute gates)
- A subjective rating

---

## 2. Scoring Dimensions

The KHS is composed of 7 dimensions. Each dimension scores 0–100. The final KHS is the weighted sum of all 7 dimension scores.

| Dimension | Code | Weight | Rules It Measures |
|---|---|---|---|
| Registry Integrity | D1 | 25% | RI-001 to RI-015 |
| Lifecycle Compliance | D2 | 20% | RI-010 to RI-013; AV-002; AV-004 |
| Approval Status | D3 | 20% | lifecycle_status = APPROVED across all assets |
| Governance Compliance | D4 | 15% | LV-RSK-003 to 008; LV-CAP-002/004; LV-ASP-002/003; LV-REF-002 |
| Metadata Completeness | D5 | 10% | RI-014; RI-015 |
| Relationship Integrity | D6 | 5% | RI-005 to RI-009; CLV-003; CLV-004 |
| Validation Success | D7 | 5% | Overall pass rate across all 76 rules |

**Total weight: 100%**

---

## 3. Dimension Definitions and Calculation

### D1 — Registry Integrity (Weight: 25%)

Registry Integrity measures whether the registry file itself is structurally sound. A registry with structural defects cannot be trusted for any downstream use.

**Base score: 100**

**Deductions:**

| Violation | Deduction |
|---|---|
| RI-001 fires (duplicate IDs) | −100 (registry is unusable; D1 = 0) |
| RI-008 fires (circular supersession) | −100 (D1 = 0) |
| RI-009 fires (circular parent-child) | −100 (D1 = 0) |
| Each RI-002 violation (invalid asset_type) | −5 per instance (max −25) |
| Each RI-003 violation (invalid lifecycle_status) | −5 per instance (max −25) |
| Each RI-004 violation (source file not found) | −2 per instance (max −20) |
| Each RI-006 violation (broken supersedes ref) | −5 per instance (max −20) |
| Each RI-007 violation (broken superseded_by ref) | −5 per instance (max −20) |
| RI-011 fires (DRAFT approved_for_reuse = true) | −10 per instance (max −30) |
| RI-012 fires (ARCHIVED approved_for_reuse = true) | −10 per instance (max −30) |
| RI-013 fires (SUPERSEDED approved_for_reuse = true) | −5 per instance (max −15) |

**Formula:** `D1 = max(0, 100 − sum_of_deductions)`

If any of RI-001, RI-008, RI-009 fire → D1 = 0 regardless of other violations.

### D2 — Lifecycle Compliance (Weight: 20%)

Lifecycle Compliance measures whether all assets are in valid, consistent lifecycle states. Assets must progress through the lifecycle correctly; inconsistent states indicate governance failures.

**Calculation:**
```
total_entries = count(all registry entries)
compliant_entries = count(entries where:
    lifecycle_status IN {DRAFT, NORMALISED, READY_FOR_REVIEW, AUTO_APPROVED,
                         REVIEW_REQUIRED, APPROVED, SUPERSEDED, ARCHIVED}
    AND approved_for_reuse is consistent with lifecycle_status
    AND (if APPROVED: approved_by is populated)
)
D2 = round((compliant_entries / total_entries) × 100)
```

**Additional deductions:**
- Each RI-010 violation: −3 (inconsistent approved_for_reuse)
- Each RI-011 violation: −10 (DRAFT marked reusable — serious)
- Each RI-012 violation: −10 (ARCHIVED marked reusable — serious)

**Formula:** `D2 = max(0, base_percentage − deductions)`

### D3 — Approval Status (Weight: 20%)

Approval Status measures what proportion of assets across all libraries are in APPROVED state. This is the most direct measure of library readiness.

Approval status is weighted by asset type priority (P1 > P2 > P3), because unapproved P1 assets block more proposals than unapproved P3 assets.

**Asset type priority weights:**

| Asset Type | Priority | Weight |
|---|---|---|
| CAP | P1 | 3.0 |
| ASP | P1 | 3.0 |
| RSK | P1 | 3.0 |
| PAT | P1 | 3.0 |
| MTH | P2 | 2.0 |
| REF | P2 | 2.0 |
| SEC | P2 | 2.0 |
| ASM | P1 (implied by ASP) | 1.5 (lower because governed via pack) |
| PPT | P3 | 1.0 |
| PRT | P3 | 1.0 |
| CON | P3 | 0.5 |
| COM | P3 | 0.5 |

**Calculation:**
```
weighted_approved = sum(asset.priority_weight for asset if lifecycle_status = APPROVED)
weighted_total = sum(asset.priority_weight for all assets)
D3 = round((weighted_approved / weighted_total) × 100)
```

### D4 — Governance Compliance (Weight: 15%)

Governance Compliance measures whether assets meet their governance requirements — not just that they are approved, but that the governance metadata supporting that approval is correctly populated.

**Governance requirement checks by asset type:**

| Asset Type | Governance Requirement | Rule |
|---|---|---|
| CAP | evidence_tier populated | LV-CAP-002 |
| CAP | annual_review_obligation = true | LV-CAP-004 |
| ASP | pending_decisions = 0 | LV-ASP-002 |
| ASP | pack_code = asset_id | LV-ASP-003 |
| ASM | parent_pack_id populated | LV-ASM-001 |
| RSK | mandatory_if_engagement populated | LV-RSK-003 |
| RSK | governance_category populated | LV-RSK-006 |
| RSK | Category B has decision_ref | LV-RSK-007 |
| RSK | net_rating consistent | LV-RSK-001 |
| REF | signed_date populated | LV-REF-002 |
| MTH | applicable_platforms populated | LV-MTH-001 |
| PAT | typical_sections populated | LV-PAT-002 |

**Calculation:**
```
governance_checks_total = count(all governance checks applicable across all entries)
governance_checks_passed = count(checks that pass)
D4 = round((governance_checks_passed / governance_checks_total) × 100)
```

### D5 — Metadata Completeness (Weight: 10%)

Metadata Completeness measures whether all mandatory registry fields are populated for every entry.

**Calculation:**
```
For each entry in registry + assumptions:
  mandatory_field_count = count(mandatory fields per KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md §2)
  populated_field_count = count(mandatory fields that are non-empty)
  entry_completeness = populated_field_count / mandatory_field_count

  extension_completeness = 0.0
  IF asset_type has extension block:
    ext_field_count = count(expected extension fields)
    ext_populated = count(extension fields that are non-empty)
    extension_completeness = ext_populated / ext_field_count

  entry_score = (0.7 × entry_completeness) + (0.3 × extension_completeness)
  # Core fields worth 70%; extension worth 30%

D5 = round(mean(entry_score for all entries) × 100)
```

### D6 — Relationship Integrity (Weight: 5%)

Relationship Integrity measures whether all declared relationships can be resolved within the registry.

**Calculation:**
```
total_declared_relationships = 0
resolved_relationships = 0

FOR each entry in registry + assumptions:
  FOR each ref_id IN entry.related_assets:
    total_declared_relationships += 1
    IF ref_id IN all_asset_ids: resolved_relationships += 1

  IF entry.supersedes != "":
    total_declared_relationships += 1
    IF entry.supersedes IN all_asset_ids: resolved_relationships += 1

  IF entry.superseded_by != "":
    total_declared_relationships += 1
    IF entry.superseded_by IN all_asset_ids: resolved_relationships += 1

IF total_declared_relationships = 0:
  D6 = 100  # No relationships declared — not a defect for a new registry
ELSE:
  D6 = round((resolved_relationships / total_declared_relationships) × 100)
```

**Additional deduction:**
- RI-008 fires (circular supersession): D6 = 0
- RI-009 fires (circular parent-child): D6 = 0

### D7 — Validation Success (Weight: 5%)

Validation Success is the overall pass rate across all applicable rules.

**Calculation:**
```
total_rules_evaluated = count(all rules that were applicable and evaluated)
rules_passed = count(rules that returned no violation)
D7 = round((rules_passed / total_rules_evaluated) × 100)
```

---

## 4. Final Score Calculation

```
KHS = round(
  (D1 × 0.25) +
  (D2 × 0.20) +
  (D3 × 0.20) +
  (D4 × 0.15) +
  (D5 × 0.10) +
  (D6 × 0.05) +
  (D7 × 0.05)
)
```

KHS is always an integer in the range [0, 100].

---

## 5. Score Bands

| Band | Score Range | Platform State | Assembly Status |
|---|---|---|---|
| EXCELLENT | 90–100 | Platform fully governed and assembly-ready | Proceed with confidence |
| GOOD | 75–89 | Platform ready; minor conditions present | Proceed; review warnings |
| ADEQUATE | 60–74 | Significant gaps; assembly possible with exceptions | Proceed cautiously; manual checks required |
| POOR | 40–59 | Major governance or metadata deficiencies | Do not assemble without BU Lead sign-off |
| CRITICAL | 0–39 | Platform not ready; fundamental structural issues | Do not assemble; remediate first |

---

## 6. Dimension Score Lookup Table

For rapid assessment during governance reviews:

| Score | D1 (Registry) | D2 (Lifecycle) | D3 (Approval) | D4 (Governance) |
|---|---|---|---|---|
| 100 | Zero RI violations | All states consistent | All assets APPROVED | All governance fields correct |
| 90+ | 1–2 minor warnings | 1–2 minor inconsistencies | ≥90% assets APPROVED | ≥90% checks pass |
| 75+ | No BLOCK violations | No BLOCK violations | ≥75% approved | ≥75% checks pass |
| 60+ | Structural concerns | Some inconsistencies | ≥60% approved | ≥60% checks pass |
| 40+ | BLOCK violations present | BLOCK violations | ≥40% approved | ≥40% checks pass |
| <40 | RI-001/008/009 fired | Systemic failure | <40% approved | Systemic failure |

---

## 7. Current State Estimate (Pre-Population)

Before the registry is populated (current state at WP18D completion), the KHS cannot be calculated — there are no entries to evaluate. The table below projects KHS at each milestone:

| Milestone | D1 | D2 | D3 | D4 | D5 | D6 | D7 | **KHS** | Band |
|---|---|---|---|---|---|---|---|---|---|
| Registry populated; RSK still DRAFT | 90 | 85 | 65 | 55 | 75 | 80 | 70 | **73** | ADEQUATE |
| + WP18B-EXT.2 complete (RSK approved) | 90 | 95 | 90 | 85 | 75 | 80 | 85 | **87** | GOOD |
| + Metadata extension fields populated | 90 | 95 | 90 | 90 | 95 | 85 | 90 | **92** | EXCELLENT |
| Full production state | 95 | 98 | 98 | 95 | 95 | 90 | 95 | **96** | EXCELLENT |

**Key insight:** The Risk Library DRAFT state (TD-001) is the primary driver suppressing D3 (40 DRAFT risks out of ~189 core assets ≈ 21% of P1 assets unapproved). Resolving TD-001 via WP18B-EXT.2 drives KHS from ADEQUATE (~73) to GOOD (~87). This is the single highest-value governance action available.

---

## 8. Remediation Score Impact Table

The following table shows the estimated KHS impact of each available remediation action, in descending impact order:

| Priority | Action | Work Package | KHS Impact |
|---|---|---|---|
| 1 | Approve Risk Library (WP18B-EXT.2) | WP18B-EXT.2 | +14 pts (73 → 87) |
| 2 | Populate all extension metadata fields | Population WP | +5 pts (87 → 92) |
| 3 | Populate REF signed_dates and on-file status | Population WP | +2 pts |
| 4 | Set review_due for all CAP assets | Population WP | +1 pt |
| 5 | Link all Category B risks to decision references | WP18B-EXT.2 | +1 pt |
| 6 | Populate MTH phase structures | Population WP | +1 pt |
| 7 | Declare cross-library relationships (RSK → ASM) | Population WP | +1 pt |

---

## 9. Score Reporting

The KHS is reported in both the Platform Health Report and the Assembly Validation Report. When reported in an Assembly Validation Report, it is the score at the time of that validation run — not a real-time score.

**Health Report KHS block (Markdown):**

```
## Knowledge Health Score: 87/100 — GOOD

| Dimension | Score | Weight | Contribution |
|---|---|---|---|
| Registry Integrity | 90/100 | 25% | 22.5 |
| Lifecycle Compliance | 95/100 | 20% | 19.0 |
| Approval Status | 90/100 | 20% | 18.0 |
| Governance Compliance | 85/100 | 15% | 12.75 |
| Metadata Completeness | 75/100 | 10% | 7.5 |
| Relationship Integrity | 80/100 | 5% | 4.0 |
| Validation Success | 85/100 | 5% | 4.25 |
| **TOTAL** | | **100%** | **88.0 → 88** |

Platform is GOOD. Proceed with minor conditions noted.
Change from previous run: +15 pts (ADEQUATE 73 → GOOD 88) — driven by WP18B-EXT.2 approval.
```

---

## 10. Score Governance

- **Review trigger:** KHS below 75 triggers a mandatory governance review with BU Lead
- **Monthly reporting:** KHS is calculated and logged in the Platform Health Report every month
- **Proposal gate:** KHS is informational only — the BLOCK rules are the absolute assembly gates. A GOOD or EXCELLENT KHS without BLOCK violations means proceed.
- **Target KHS for platform maturity L4.0:** KHS ≥ 85 (GOOD band) sustained for ≥ 2 consecutive monthly runs

---

## 11. Changelog

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-27 | WP18D | Initial scoring model — 7 dimensions, weightings, formulas, score bands, current-state estimates, remediation impact table |
