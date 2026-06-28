---
document_id: KNOWLEDGE-VALIDATION-REPORT-STANDARD-V1
title: "Knowledge Validation Report Standard — V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-27"
created_by: "WP18D — Knowledge Validation Engine"
approved_by: "Architecture — WP18D"
approved_date: "2026-06-27"
approved_for_reuse: true
category: "Assembly Engine / Validation"
scope: "Defines the standard format for all reports produced by the Knowledge Validation Engine — including the Assembly Validation Report (Mode 2), the Platform Health Report (Mode 1), and the Assembly Manifest. Covers both machine-readable (YAML) and human-readable (Markdown) output formats."
governing_standard: "KNOWLEDGE_VALIDATION_ENGINE.md V1.0"
related_documents:
  - KNOWLEDGE_VALIDATION_ENGINE.md
  - VALIDATION_RULE_EXECUTION_MODEL.md
  - KNOWLEDGE_HEALTH_SCORE.md
---

# Knowledge Validation Report Standard — V1.0

**Work Package:** WP18D  
**Status:** APPROVED

---

## 1. Report Types

The KVE produces three document types:

| Report Type | Mode | Format | Purpose |
|---|---|---|---|
| Assembly Validation Report | Mode 2 | YAML + Markdown | Validation result for a specific tender |
| Platform Health Report | Mode 1 | YAML + Markdown | Periodic health check of the knowledge platform |
| Assembly Manifest | Mode 2 | YAML only | Certified asset list consumed by Assembly Engine |

Reports are always produced in pairs: a YAML (machine-readable) and a Markdown (human-readable). The Assembly Manifest is YAML-only and is the primary output consumed by downstream engines.

---

## 2. File Naming Convention

| Document | File Name | Location |
|---|---|---|
| Assembly Validation Report (YAML) | `VALIDATION_REPORT_[tender_id]_[YYYYMMDD].yaml` | `08_Commercial/Proposals/[tender_id]/` |
| Assembly Validation Report (MD) | `VALIDATION_REPORT_[tender_id]_[YYYYMMDD].md` | `08_Commercial/Proposals/[tender_id]/` |
| Assembly Manifest (YAML) | `ASSEMBLY_MANIFEST_[tender_id]_[YYYYMMDD].yaml` | `08_Commercial/Proposals/[tender_id]/` |
| Platform Health Report (YAML) | `KNOWLEDGE_HEALTH_REPORT_[YYYYMMDD].yaml` | `08_Commercial/Reports/` |
| Platform Health Report (MD) | `KNOWLEDGE_HEALTH_REPORT_[YYYYMMDD].md` | `08_Commercial/Reports/` |

---

## 3. Assembly Validation Report — YAML Format

### 3.1 Complete Schema

```yaml
---
report_type: ASSEMBLY_VALIDATION
report_id: ""                      # [tender_id]-VAL-[YYYYMMDD]
tender_id: ""
tender_pattern: ""                 # P1–P13
tender_platform: ""
engagement_type: ""
validation_timestamp: ""          # ISO 8601 datetime
registry_version: ""
validation_rules_version: "1.0"   # KNOWLEDGE_REGISTRY_VALIDATION_RULES.md version
engine_version: "1.0"             # KVE version

summary:
  manifest_status: ""             # VALID / BLOCKED / APPROVED_WITH_CONDITIONS
  proceed: false                  # true = Assembly Engine may consume manifest
  health_score_at_validation: 0   # Platform health score at time of this run (0–100)
  total_rules_evaluated: 0
  rules_passed: 0
  rules_failed: 0
  blocks: 0
  errors: 0
  warnings: 0
  assets_in_manifest: 0
  assets_removed: 0
  assets_flagged: 0

blockers:                         # List of BLOCK conditions — must be empty for proceed=true
  - rule_code: ""
    rule_name: ""
    severity: BLOCK
    asset_id: ""
    asset_type: ""
    asset_title: ""
    condition_triggered: ""       # Exact condition that evaluated to true
    description: ""               # Plain-language description
    recommended_action: ""        # Specific remediation step
    escalation: ""                # Who must act (BU_LEAD / AM / AUTHOR)

errors:                           # ERROR conditions — asset removed from manifest
  - rule_code: ""
    rule_name: ""
    severity: ERROR
    asset_id: ""
    asset_type: ""
    asset_title: ""
    description: ""
    recommended_action: ""
    manifest_impact: "REMOVED"    # Asset was removed from manifest

warnings:                         # WARNING conditions — asset included with flag
  - rule_code: ""
    rule_name: ""
    severity: WARNING
    asset_id: ""
    asset_type: ""
    asset_title: ""
    description: ""

orphan_assets:                    # Assets in registry with no declared relationships
  - asset_id: ""
    asset_type: ""
    asset_title: ""
    note: ""

missing_relationships:            # Declared relationships that could not be resolved
  - asset_id: ""
    related_id: ""
    relationship_type: ""         # related_assets / supersedes / superseded_by
    note: ""

metadata_failures:                # Assets with mandatory field violations (RI-014)
  - asset_id: ""
    asset_type: ""
    missing_fields: []            # List of missing mandatory field names

lifecycle_failures:               # Assets with lifecycle inconsistencies (RI-010–013)
  - asset_id: ""
    asset_type: ""
    lifecycle_status: ""
    approved_for_reuse: false
    violation: ""                 # Description of the inconsistency

phase_results:                    # Summary of each validation phase
  - phase: 1
    phase_name: "Registry Integrity"
    rules_evaluated: 15
    blocks: 0
    errors: 0
    warnings: 0
    halted: false
  - phase: 2
    phase_name: "Tender Profile Establishment"
    rules_evaluated: 0            # N/A for Mode 2 profile setup
    blocks: 0
    errors: 0
    warnings: 0
  # ... phases 3–8

recommendations:                  # Prioritised remediation steps
  - priority: 1
    category: ""                  # BLOCKER / GOVERNANCE / METADATA / RELATIONSHIP
    action: ""
    owner: ""                     # BU_LEAD / AM / AUTHOR / REGISTRY_FACILITATOR
    effort: ""                    # Estimated effort (e.g., "30min", "1h")
    resolves_rules: []            # Rule codes this action resolves

manifest_ref: ""                  # Path to ASSEMBLY_MANIFEST file
---
```

### 3.2 Example — BLOCKED Report

```yaml
---
report_type: ASSEMBLY_VALIDATION
report_id: "ARM-IT045-VAL-20260627"
tender_id: "ARM-IT045"
tender_pattern: "P1"
tender_platform: "Oracle HCM Cloud"
engagement_type: "Implementation"
validation_timestamp: "2026-06-27T09:15:00Z"
registry_version: "1.0"

summary:
  manifest_status: BLOCKED
  proceed: false
  health_score_at_validation: 52
  total_rules_evaluated: 76
  rules_passed: 70
  rules_failed: 6
  blocks: 2
  errors: 3
  warnings: 5
  assets_in_manifest: 47
  assets_removed: 5
  assets_flagged: 8

blockers:
  - rule_code: LV-RSK-008
    rule_name: "DRAFT Risk Not Assembled"
    severity: BLOCK
    asset_id: RC-PROJ-001
    asset_type: RSK
    asset_title: "Project Scope Change Risk"
    condition_triggered: "lifecycle_status = DRAFT AND asset in candidate manifest"
    description: "RC-PROJ-001 is in DRAFT state. DRAFT risks may not appear in proposals."
    recommended_action: "Complete WP18B-EXT.2 governance session to approve the Risk Library. Until approved, remove all RSK assets from the tender scope or substitute with manual narrative."
    escalation: BU_LEAD

  - rule_code: AV-011
    rule_name: "RC-OPS-001 Unconditional"
    severity: BLOCK
    asset_id: RC-OPS-001
    asset_type: RSK
    asset_title: "Operational Risk — APPSolve Obligations"
    condition_triggered: "tender_pattern != P10 AND RC-OPS-001 not in manifest"
    description: "RC-OPS-001 is unconditionally mandatory for all non-P10 proposals. It is not in the manifest — likely because it is DRAFT."
    recommended_action: "Approve RC-OPS-001 via WP18B-EXT.2. No workaround — this asset cannot be omitted."
    escalation: BU_LEAD

recommendations:
  - priority: 1
    category: BLOCKER
    action: "Conduct WP18B-EXT.2 Risk Library governance session. Apply decisions to ENTERPRISE_RISK_REGISTER_V1.md. Update registry. Re-run validation."
    owner: BU_LEAD
    effort: "2h 10min"
    resolves_rules: [LV-RSK-008, AV-011, LV-RSK-004]
---
```

### 3.3 Example — VALID Report

```yaml
---
report_type: ASSEMBLY_VALIDATION
report_id: "ARM-IT045-VAL-20261201"
tender_id: "ARM-IT045"
tender_pattern: "P1"
tender_platform: "Oracle HCM Cloud"
validation_timestamp: "2026-12-01T10:00:00Z"

summary:
  manifest_status: VALID
  proceed: true
  health_score_at_validation: 88
  total_rules_evaluated: 76
  rules_passed: 74
  rules_failed: 2
  blocks: 0
  errors: 0
  warnings: 2
  assets_in_manifest: 52
  assets_removed: 0
  assets_flagged: 3

warnings:
  - rule_code: AV-012
    severity: WARNING
    asset_id: W3S1-001
    asset_title: "Oracle HCM Core — Global HR"
    description: "Annual review due 2026-11-30 — overdue by 1 day. Asset included."

recommendations:
  - priority: 1
    category: METADATA
    action: "Schedule annual review for W3S1-001 and any other CAP assets with review_due in the past."
    owner: BU_LEAD
    effort: "30min per asset"
    resolves_rules: [AV-012, AV-013]

manifest_ref: "08_Commercial/Proposals/ARM-IT045/ASSEMBLY_MANIFEST_ARM-IT045_20261201.yaml"
---
```

---

## 4. Assembly Validation Report — Markdown Format

The Markdown report is the human-readable version of the YAML report. It follows this structure:

```markdown
# Validation Report — [Tender ID]

**Date:** [YYYY-MM-DD]  
**Tender Pattern:** P[N]  
**Platform:** [Platform]  
**Manifest Status:** [VALID / BLOCKED / APPROVED_WITH_CONDITIONS]  
**Proceed to Assembly:** [YES / NO]  
**Platform Health Score:** [N]/100

---

## Summary

| Metric | Count |
|---|---|
| Rules Evaluated | N |
| BLOCK conditions | N |
| ERROR conditions | N |
| WARNING conditions | N |
| Assets in Manifest | N |
| Assets Removed | N |

---

## BLOCK Conditions — Assembly Halted

> **Assembly is BLOCKED. The following issues must be resolved before any proposal generation.**

### [rule_code] — [rule_name]

**Asset:** [asset_id] — [asset_title]  
**Condition:** [condition_triggered]  
**Description:** [description]  
**Action Required:** [recommended_action]  
**Escalation:** [escalation]

[Repeat for each BLOCK]

---

## ERROR Conditions — Assets Removed

[List of error conditions; each with asset, condition, action]

---

## WARNING Conditions — Assets Flagged

[List of warnings; each with asset and note]

---

## Orphan Assets ([N])

[Table of assets with no declared relationships]

---

## Missing Relationships ([N])

[Table of declared relationships that could not be resolved]

---

## Metadata Failures ([N])

[Table of assets with missing mandatory fields]

---

## Lifecycle Failures ([N])

[Table of assets with lifecycle inconsistencies]

---

## Recommendations

| Priority | Action | Owner | Effort |
|---|---|---|---|
| 1 | [action] | [owner] | [effort] |
...

---

*Generated by Knowledge Validation Engine V1.0*  
*Registry Version: [n] | Rules Version: 1.0*
```

---

## 5. Platform Health Report — YAML Format

The Platform Health Report is produced in Mode 1 (no tender context).

```yaml
---
report_type: PLATFORM_HEALTH
report_id: ""                      # HEALTH-[YYYYMMDD]
validation_timestamp: ""
registry_version: ""
engine_version: "1.0"
mode: PLATFORM_HEALTH

summary:
  health_score: 0                  # 0–100 (see KNOWLEDGE_HEALTH_SCORE.md)
  health_band: ""                  # EXCELLENT / GOOD / ADEQUATE / POOR / CRITICAL
  total_assets: 0
  approved_assets: 0
  draft_assets: 0
  archived_assets: 0
  superseded_assets: 0
  total_rules_evaluated: 0
  rules_passed: 0
  rules_failed: 0
  blocks: 0
  errors: 0
  warnings: 0

health_score_breakdown:            # Per-dimension scores (see KNOWLEDGE_HEALTH_SCORE.md)
  registry_integrity:
    score: 0
    weight: 0.25
    weighted_contribution: 0.0
    notes: ""
  lifecycle_compliance:
    score: 0
    weight: 0.20
    weighted_contribution: 0.0
    notes: ""
  approval_status:
    score: 0
    weight: 0.20
    weighted_contribution: 0.0
    notes: ""
  governance_compliance:
    score: 0
    weight: 0.15
    weighted_contribution: 0.0
    notes: ""
  metadata_completeness:
    score: 0
    weight: 0.10
    weighted_contribution: 0.0
    notes: ""
  relationship_integrity:
    score: 0
    weight: 0.05
    weighted_contribution: 0.0
    notes: ""
  validation_success:
    score: 0
    weight: 0.05
    weighted_contribution: 0.0
    notes: ""

asset_type_summary:
  - asset_type: CAP
    total: 0
    approved: 0
    draft: 0
    blocked: 0
    metadata_complete: 0
  # ... for each asset type

blockers: []
errors: []
warnings: []

orphan_assets: []
missing_relationships: []
metadata_failures: []
lifecycle_failures: []

recommendations:
  - priority: 1
    category: ""
    action: ""
    owner: ""
    effort: ""
    resolves_rules: []
    expected_score_impact: 0      # Estimated health score increase if resolved

trend:                             # Populated on second+ run; empty on first
  previous_score: 0
  previous_date: ""
  score_delta: 0
  direction: ""                   # IMPROVING / DECLINING / STABLE
---
```

---

## 6. Platform Health Report — Markdown Format

```markdown
# Platform Knowledge Health Report

**Date:** [YYYY-MM-DD]  
**Registry Version:** [N]  

---

## Health Score: [N]/100 — [BAND]

| Dimension | Score | Weight | Contribution |
|---|---|---|---|
| Registry Integrity | N/100 | 25% | N |
| Lifecycle Compliance | N/100 | 20% | N |
| Approval Status | N/100 | 20% | N |
| Governance Compliance | N/100 | 15% | N |
| Metadata Completeness | N/100 | 10% | N |
| Relationship Integrity | N/100 | 5% | N |
| Validation Success | N/100 | 5% | N |
| **TOTAL** | | **100%** | **N** |

---

## Asset Library Status

| Type | Total | Approved | Draft | Blocked | Metadata Complete |
|---|---|---|---|---|---|
| CAP | N | N | N | N | N |
| ASP | N | N | N | N | N |
| ASM | N | N | N | N | N |
| RSK | N | N | N | N | N |
| MTH | N | N | N | N | N |
| REF | N | N | N | N | N |
| PAT | N | N | N | N | N |
| SEC | N | N | N | N | N |

---

## Issues

### BLOCK Conditions ([N])
[Table of blocker conditions with remediation]

### ERROR Conditions ([N])
[Table of error conditions]

### WARNING Conditions ([N])
[Table of warnings]

---

## Remediation Roadmap

| Priority | Action | Owner | Effort | Score Impact |
|---|---|---|---|---|
| 1 | [action] | [owner] | [effort] | +[N] pts |
...

---

## Trend
[Score delta vs previous run, if available]

*Generated by Knowledge Validation Engine V1.0*
```

---

## 7. Assembly Manifest — YAML Format

The Assembly Manifest is the primary machine-readable output consumed by the Assembly Engine. It contains only the certified assets eligible for this specific tender.

```yaml
---
manifest_id: ""                    # [tender_id]-MANIFEST-[YYYYMMDD]
report_type: ASSEMBLY_MANIFEST
tender_id: ""
tender_pattern: ""
tender_platform: ""
engagement_type: ""
manifest_status: ""               # VALID / BLOCKED / APPROVED_WITH_CONDITIONS
proceed: false
manifest_timestamp: ""
registry_version: ""
validation_report_ref: ""         # Path to companion VALIDATION_REPORT.yaml
blocks: 0
errors: 0
warnings: 0
assets_in_manifest: 0
---

manifest_assets:

  # === CAPABILITY ASSETS (CAP) ===
  - asset_id: ""
    asset_type: CAP
    title: ""
    version: ""
    source_file: ""
    lifecycle_status: APPROVED
    approved_for_reuse: true
    assembly_rules:
      mandatory_if: ""
      optional_if: ""
      excluded_if: ""
      assembly_priority: ""
      section_placement: []
      content_source_type: ""
    validation_flags: []           # WARNING rule codes fired for this asset

  # === ASSUMPTION PACKS (ASP) ===
  - asset_id: ""
    asset_type: ASP
    title: ""
    version: ""
    source_file: ""
    lifecycle_status: APPROVED
    approved_for_reuse: true
    assembly_rules:
      mandatory_if: ""
      section_placement: []
      content_source_type: "DIRECT"
    child_assumption_count: 0     # Informational — actual ASMs in assumptions registry
    validation_flags: []

  # === ENTERPRISE RISKS (RSK) ===
  # Ordered by assembly_priority: CRITICAL → HIGH → MEDIUM → LOW
  - asset_id: ""
    asset_type: RSK
    title: ""
    version: ""
    source_file: ""
    lifecycle_status: APPROVED
    approved_for_reuse: true
    assembly_rules:
      assembly_priority: ""
      section_placement: [S-50]
      content_source_type: "EXTRACT"
    validation_flags: []

  # === CLIENT REFERENCES (REF) ===
  - asset_id: ""
    asset_type: REF
    title: ""
    version: ""
    source_file: ""
    lifecycle_status: APPROVED
    approved_for_reuse: true
    assembly_rules:
      section_placement: [S-9]
      content_source_type: "DIRECT"
    am_clearance_confirmed: true  # Always true if in manifest
    validation_flags: []

  # === METHODOLOGIES (MTH) ===
  - asset_id: ""
    asset_type: MTH
    title: ""
    version: ""
    source_file: ""
    lifecycle_status: APPROVED
    approved_for_reuse: true
    assembly_rules:
      section_placement: [S-30]
      content_source_type: "DIRECT"
    validation_flags: []
```

---

## 8. Report Retention Policy

| Report Type | Retention Period | Notes |
|---|---|---|
| Assembly Validation Report | Indefinite — with the tender file | Required for audit; proves governance state at time of assembly |
| Assembly Manifest | Indefinite — with the tender file | Provenance of the assembled proposal |
| Platform Health Report | 3 years | Historical trend data; annual audit evidence |

All reports are version-controlled alongside the registry. A future regulatory audit should be able to recover any historical report alongside the registry snapshot that produced it.

---

## 9. Report Usage Guidance

**For BU Lead:**
- Review the Markdown reports (human-readable)
- BLOCK conditions require BU Lead action before assembly proceeds
- Platform Health Report: review monthly; target health score ≥ 80

**For Assembly Engine / AI:**
- Read only the YAML Assembly Manifest — never read the registry directly
- Check `proceed` field first — if false, do not assemble
- Check `manifest_status` — log it in the assembly audit trail
- Check `validation_flags` per asset — surface flagged assets in the QA report

**For Governance Audit:**
- YAML reports are the evidence of governance state
- The manifest proves which assets were approved at the time of each proposal
- Registry version + validation_timestamp can be used to reconstruct the exact validation state

---

## 10. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-27 | WP18D | Initial standard — Assembly Validation Report (YAML + MD), Platform Health Report (YAML + MD), Assembly Manifest schema; retention policy; usage guidance |
