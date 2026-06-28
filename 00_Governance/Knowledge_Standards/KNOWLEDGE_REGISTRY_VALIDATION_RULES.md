---
document_id: KNOWLEDGE-REGISTRY-VALIDATION-RULES-V1
title: "Knowledge Registry Validation Rules — V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-27"
created_by: "WP18B-EXT.3A — Universal Knowledge Asset Registry"
approved_by: "Architecture — WP18B-EXT.3A"
approved_date: "2026-06-27"
approved_for_reuse: true
category: "Governance / Knowledge Standards"
scope: "Defines all deterministic validation rules for the Universal Knowledge Asset Registry — registry integrity rules (RI-), assembly validation rules (AV-), cross-library validation rules (CLV-), and library-specific validation rules (LV-). These rules are the primary input specification for WP18D (Knowledge Validation Engine)."
related_documents:
  - KNOWLEDGE_ASSET_REGISTRY_STANDARD.md
  - KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md
  - KNOWLEDGE_REGISTRY_POPULATION_RULES.md
  - KNOWLEDGE_RELATIONSHIP_MODEL.md
---

# Knowledge Registry Validation Rules — V1.0

**Work Package:** WP18B-EXT.3A  
**Status:** APPROVED  
**Scope for WP18D:** All rules in this document constitute the implementation specification for the Knowledge Validation Engine (WP18D). Each rule maps to a deterministic check that the engine executes against the registry.

---

## 1. Rule Structure

Each validation rule has:

| Field | Description |
|---|---|
| **Rule Code** | Unique identifier — series prefix + sequence (e.g., `RI-001`) |
| **Rule Name** | Short descriptive name |
| **Type** | BLOCK / ERROR / WARNING — severity at assembly time |
| **Scope** | Registry / Assembly / Cross-Library / Library-Specific |
| **Condition** | Exact Boolean condition that triggers the rule |
| **Trigger** | When this rule is evaluated |
| **WP18D Action** | What the engine does when this rule fires |

**Severity definitions:**

| Severity | Engine Behaviour |
|---|---|
| BLOCK | Assembly is halted. Proposal cannot proceed. BU Lead must resolve. |
| ERROR | Assembly continues but the violated asset is excluded from the manifest. Warning reported. |
| WARNING | Assembly continues. Asset included. Issue logged for review. |

---

## 2. Registry Integrity Rules (RI-)

These rules validate the registry file itself, independent of any specific tender. Run on every registry sync and before every assembly run.

| Rule | Name | Type | Condition | WP18D Action |
|---|---|---|---|---|
| RI-001 | Unique Asset IDs | BLOCK | Any `asset_id` appears more than once in the registry | Halt; report duplicate IDs |
| RI-002 | Valid Asset Type | ERROR | `asset_type` is not one of: CAP / ASP / ASM / RSK / MTH / REF / PPT / PRT / CON / COM / PAT / SEC | Exclude entry; flag for correction |
| RI-003 | Valid Lifecycle Status | ERROR | `lifecycle_status` is not one of the 8 approved states | Exclude entry; flag for correction |
| RI-004 | Source File Resolves | WARNING | `source_file` path does not resolve to an existing file on the filesystem | Log warning; entry remains |
| RI-005 | Related Assets Exist | WARNING | Any ID in `related_assets[]` does not exist in the registry | Log warning; cross-reference flagged as unresolved |
| RI-006 | Supersedes ID Exists | ERROR | `supersedes` is non-empty AND the referenced ID does not exist in registry | Flag supersession chain as broken |
| RI-007 | Superseded_by ID Exists | ERROR | `superseded_by` is non-empty AND the referenced ID does not exist in registry | Flag supersession chain as broken |
| RI-008 | No Circular Supersession | BLOCK | Asset A.supersedes = B AND B.supersedes = A (any cycle length) | Halt; report circular chain |
| RI-009 | No Circular Parent-Child | BLOCK | Any parent-child chain forms a cycle via related_assets | Halt; report circular chain |
| RI-010 | Approved-for-Reuse Consistency | ERROR | `approved_for_reuse = true` AND `lifecycle_status ≠ APPROVED` | Set approved_for_reuse → false; flag for correction |
| RI-011 | DRAFT Cannot Be Reused | BLOCK | `approved_for_reuse = true` AND `lifecycle_status = DRAFT` | Set approved_for_reuse → false; BLOCK assembly use |
| RI-012 | ARCHIVED Cannot Be Reused | BLOCK | `approved_for_reuse = true` AND `lifecycle_status = ARCHIVED` | Set approved_for_reuse → false; BLOCK assembly use |
| RI-013 | SUPERSEDED Cannot Be Reused | ERROR | `approved_for_reuse = true` AND `lifecycle_status = SUPERSEDED` | Set approved_for_reuse → false; flag successor for assembly |
| RI-014 | Mandatory Fields Present | ERROR | Any mandatory field (per KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md §2) is absent or empty string | Exclude entry from assembly; flag for population |
| RI-015 | Asset Type Has Extension Block | WARNING | `asset_type` is CAP / ASP / ASM / RSK / MTH / REF / PAT / SEC AND corresponding `[type]_ext` block is absent | Log warning; flag for population |

---

## 3. Assembly Validation Rules (AV-)

These rules validate the registry state relative to a specific tender profile. Run at the start of every assembly run, after the tender profile (pattern, platform, engagement type, modules) is established.

### 3.1 Gate Rules (BLOCK if violated)

| Rule | Name | Type | Condition | WP18D Action |
|---|---|---|---|---|
| AV-001 | Approved-for-Reuse Gate | BLOCK | Any asset in the candidate manifest has `approved_for_reuse = false` | Remove asset from manifest; if mandatory → BLOCK assembly |
| AV-002 | Lifecycle Gate | BLOCK | Any asset in candidate manifest has `lifecycle_status ≠ APPROVED` | Remove asset from manifest; if mandatory → BLOCK assembly |
| AV-003 | SUPERSEDED Asset Gate | ERROR | Any asset in candidate manifest has `lifecycle_status = SUPERSEDED` | Replace with superseded_by asset if it exists and is APPROVED; else remove |
| AV-004 | ARCHIVED Asset Gate | BLOCK | Any asset in candidate manifest has `lifecycle_status = ARCHIVED` | Remove asset from manifest; flag as invalid selection |

### 3.2 Pattern Applicability Rules

| Rule | Name | Type | Condition | WP18D Action |
|---|---|---|---|---|
| AV-005 | Pattern Applicability | ERROR | Asset's `pattern_applicability` does not include the tender's pattern AND `pattern_applicability ≠ [ALL]` | Remove asset from candidate manifest |
| AV-006 | Platform Applicability | ERROR | Asset's `cap_ext.platform` does not match the tender's platform (for CAP assets) | Remove asset from candidate manifest |
| AV-007 | Engagement Type Applicability | ERROR | `asp_ext.engagement_type` does not include the tender's engagement type AND `engagement_type ≠ "All"` | Remove ASP and its child ASMs from manifest |

### 3.3 Mandatory Inclusion Rules

| Rule | Name | Type | Condition | WP18D Action |
|---|---|---|---|---|
| AV-008 | Mandatory Asset Present | BLOCK | `assembly_rules.mandatory_if` evaluates TRUE for the tender profile AND asset is not in manifest | BLOCK assembly; report missing mandatory asset |
| AV-009 | Excluded Asset Absent | BLOCK | `assembly_rules.excluded_if` evaluates TRUE for the tender profile AND asset IS in manifest | Remove asset from manifest; if mandatory_if also TRUE → BLOCK (conflict) |
| AV-010 | Mandatory-Excluded Conflict | BLOCK | `mandatory_if` AND `excluded_if` both evaluate TRUE for the same asset in the same tender profile | BLOCK assembly; flag rule conflict; escalate to BU Lead |
| AV-011 | RC-OPS-001 Unconditional | BLOCK | `asset_id = RC-OPS-001` AND tender pattern ≠ P10 AND RC-OPS-001 is not in manifest | BLOCK assembly; this risk is unconditionally mandatory for all non-P10 proposals |

### 3.4 Review Currency Rules

| Rule | Name | Type | Condition | WP18D Action |
|---|---|---|---|---|
| AV-012 | Review Overdue | WARNING | `review_due` is in the past at the time of assembly | Log warning; include asset with REVIEW_OVERDUE flag |
| AV-013 | Annual Review Overdue for CAP | ERROR | `cap_ext.annual_review_obligation = true` AND `review_due` is more than 90 days in the past | Exclude CAP from manifest; flag for urgent review |

---

## 4. Cross-Library Validation Rules (CLV-)

These rules validate relationships between assets across different libraries. They implement and extend CLV-001 through CLV-012 defined in KNOWLEDGE_RELATIONSHIP_MODEL.md. All 12 original CLV rules are reproduced here with WP18D implementation detail added.

| Rule | Name | Type | Original Ref | Condition | WP18D Action |
|---|---|---|---|---|---|
| CLV-001 | Approved-for-Reuse Gate | BLOCK | KNOWLEDGE_RELATIONSHIP_MODEL §6 | Any asset in assembly manifest has `approved_for_reuse = false` | Halt assembly for that asset; if mandatory → BLOCK |
| CLV-002 | Lifecycle Status Check | BLOCK | KNOWLEDGE_RELATIONSHIP_MODEL §6 | Any asset in manifest has `lifecycle_status ≠ APPROVED` | Remove from manifest; if mandatory → BLOCK |
| CLV-003 | Related Assets Resolve | WARNING | KNOWLEDGE_RELATIONSHIP_MODEL §6 | Any ID in `related_assets[]` does not resolve to an existing registry entry | Log unresolved relationship; assembly continues |
| CLV-004 | Source Assets Resolve | WARNING | KNOWLEDGE_RELATIONSHIP_MODEL §6 | Any ID in `source_assets[]` does not resolve to an existing registry entry | Log unresolved provenance; assembly continues |
| CLV-005 | PT- Code Satisfaction | ERROR | KNOWLEDGE_RELATIONSHIP_MODEL §6 | A pre-tender control (`pre_tender_controls[]`) is listed on a CAP asset AND no evidence of control completion exists in the assembly context | Exclude CAP from manifest; log PT code |
| CLV-006 | Risk–Assumption Cross-Reference | WARNING | KNOWLEDGE_RELATIONSHIP_MODEL §6 | A RSK asset has `rsk_ext.related_assumptions[]` populated AND any referenced ASM is not APPROVED or not in manifest | Log cross-reference gap; include risk with warning |
| CLV-007 | SUPERSEDED/ARCHIVED Blocking | BLOCK | KNOWLEDGE_RELATIONSHIP_MODEL §6 | Any asset in manifest has lifecycle SUPERSEDED or ARCHIVED | Block that asset; use successor if available |
| CLV-008 | REF Account Manager Approval | BLOCK | KNOWLEDGE_RELATIONSHIP_MODEL §6 | A REF asset has `ref_ext.account_manager_required = true` AND no account manager clearance is recorded in the assembly context | Remove REF from manifest; log BLOCK |
| CLV-009 | Pack Scope Compatibility | ERROR | KNOWLEDGE_RELATIONSHIP_MODEL §6 | An ASP pack's `asp_ext.platform` does not match the tender's platform | Remove ASP and all child ASMs from manifest |
| CLV-010 | CAP Sector Restriction | ERROR | KNOWLEDGE_RELATIONSHIP_MODEL §6 | A CAP's `cap_ext.sector` does not include the tender's client sector AND sector is not `["All"]` | Remove CAP from manifest |
| CLV-011 | S-50 Priority Order | WARNING | KNOWLEDGE_RELATIONSHIP_MODEL §6 | The assembled risk list in S-50 is not ordered by assembly_priority (CRITICAL → HIGH → MEDIUM → LOW) | Log ordering defect; flag for QA |
| CLV-012 | Supersession Chain Complete | ERROR | KNOWLEDGE_RELATIONSHIP_MODEL §6 | An asset has `superseded_by` set AND the successor does not exist or is not APPROVED | Log broken chain; exclude SUPERSEDED asset |

---

## 5. Library-Specific Validation Rules (LV-)

These rules validate properties specific to a single asset type. They extend the cross-library rules with type-specific integrity requirements.

### 5.1 Capability Asset Rules (LV-CAP-)

| Rule | Name | Type | Condition | WP18D Action |
|---|---|---|---|---|
| LV-CAP-001 | Proposal Section Declared | ERROR | `proposal_sections[]` is empty for a CAP asset | Exclude from manifest; flag for population |
| LV-CAP-002 | Evidence Tier Populated | WARNING | `cap_ext.evidence_tier` is empty | Log warning; include with flag |
| LV-CAP-003 | Pattern Applicability Non-Empty | ERROR | `pattern_applicability[]` is empty | Exclude from manifest |
| LV-CAP-004 | Annual Review Date Set | WARNING | `cap_ext.annual_review_obligation = true` AND `review_due` is empty | Log warning |
| LV-CAP-005 | Content Source Type Valid | ERROR | `assembly_rules.content_source_type` is not one of: DIRECT / EXTRACT / MERGE / AI-GENERATE / TEMPLATE / PLACEHOLDER | Exclude from manifest |

### 5.2 Assumption Pack Rules (LV-ASP-)

| Rule | Name | Type | Condition | WP18D Action |
|---|---|---|---|---|
| LV-ASP-001 | Pack Has Child Assumptions | ERROR | A ASP asset has no child ASM entries in the registry (assumption registry) with matching parent_pack_id | Exclude ASP from manifest; flag for population |
| LV-ASP-002 | No Pending Decisions | BLOCK | `asp_ext.pending_decisions > 0` at assembly time | BLOCK use of ASP; flag pending decision count |
| LV-ASP-003 | Pack Code Matches ID | ERROR | `asp_ext.pack_code ≠ asset_id` | Flag inconsistency; exclude from manifest |
| LV-ASP-004 | Section Codes Declared | WARNING | `asp_ext.section_codes[]` is empty | Log warning |

### 5.3 Individual Assumption Rules (LV-ASM-)

| Rule | Name | Type | Condition | WP18D Action |
|---|---|---|---|---|
| LV-ASM-001 | Exactly One Parent Pack | BLOCK | `asm_ext.parent_pack_id` is empty | BLOCK; assumption cannot be assembled without a pack |
| LV-ASM-002 | Parent Pack Exists and Is Approved | BLOCK | `asm_ext.parent_pack_id` references a pack that does not exist or is not APPROVED | BLOCK this assumption; flag parent pack |
| LV-ASM-003 | Mandatory_if Declared | WARNING | `assembly_rules.mandatory_if` is empty for an ASM asset | Log warning; assumption treated as optional |
| LV-ASM-004 | Assumption Text Populated | ERROR | `asm_ext.assumption_text` is empty | Exclude from manifest; no content to assemble |
| LV-ASM-005 | Section Code Declared | ERROR | `asm_ext.section_code` is empty | Exclude from manifest; cannot place in proposal |

### 5.4 Enterprise Risk Rules (LV-RSK-)

| Rule | Name | Type | Condition | WP18D Action |
|---|---|---|---|---|
| LV-RSK-001 | Net Rating Consistent | ERROR | `rsk_ext.net_rating` is not consistent with the 3×3 matrix (likelihood × impact → rating tier) | Flag inconsistency; include with WARNING |
| LV-RSK-002 | Related Assumptions Declared | WARNING | `rsk_ext.related_assumptions[]` is empty for a non-governance RSK | Log; risk included without assumption cross-reference |
| LV-RSK-003 | Mandatory_if Declared | ERROR | `rsk_ext.mandatory_if_engagement` is empty | Exclude from manifest; selection rule undefined |
| LV-RSK-004 | RC-OPS-001 Is Unconditional | BLOCK | `asset_id = RC-OPS-001` AND `rsk_ext.mandatory_if_engagement ≠ "TRUE"` | BLOCK; RC-OPS-001 must always be mandatory |
| LV-RSK-005 | Proposal Section Declared | ERROR | `proposal_sections[]` is empty for RSK | Exclude; cannot place in proposal |
| LV-RSK-006 | Governance Category Declared | WARNING | `rsk_ext.governance_category` is empty | Log; risk included without classification |
| LV-RSK-007 | Category B Has Decision Reference | ERROR | `rsk_ext.governance_category = "B"` AND `rsk_ext.governance_decision_ref` is empty | Flag; include with WARNING — decision not yet linked |
| LV-RSK-008 | DRAFT Risk Not Assembled | BLOCK | Any RSK with `lifecycle_status = DRAFT` is in the candidate manifest | BLOCK; DRAFT risks may not appear in proposals |

### 5.5 Methodology Rules (LV-MTH-)

| Rule | Name | Type | Condition | WP18D Action |
|---|---|---|---|---|
| LV-MTH-001 | Platform Declared | ERROR | `mth_ext.applicable_platforms[]` is empty | Exclude from manifest |
| LV-MTH-002 | Phase Structure Declared | WARNING | `mth_ext.phase_structure[]` is empty | Log warning; methodology included |
| LV-MTH-003 | One Methodology Per Platform | ERROR | More than one MTH asset with APPROVED status targets the same platform | Flag conflict; use most recent version |

### 5.6 Client Reference Rules (LV-REF-)

| Rule | Name | Type | Condition | WP18D Action |
|---|---|---|---|---|
| LV-REF-001 | Account Manager Required | BLOCK | `ref_ext.account_manager_required = true` AND clearance not confirmed in assembly context | BLOCK; REF excluded from manifest |
| LV-REF-002 | Signed Date Populated | ERROR | `ref_ext.signed_date` is empty | Exclude from manifest; cannot verify currency |
| LV-REF-003 | Letter On File | WARNING | `ref_ext.letter_on_file = false` | Log warning; include with flag |
| LV-REF-004 | Restrictions Checked | WARNING | `ref_ext.restrictions` is non-empty | Surface restrictions text in assembly report for manual review |

### 5.7 Pattern Rules (LV-PAT-)

| Rule | Name | Type | Condition | WP18D Action |
|---|---|---|---|---|
| LV-PAT-001 | BOM Reference Declared | WARNING | `pat_ext.bom_reference` is empty | Log warning |
| LV-PAT-002 | Typical Sections Declared | ERROR | `pat_ext.typical_sections[]` is empty | Flag; pattern cannot drive section assembly |
| LV-PAT-003 | All 13 Patterns Registered | ERROR | Registry contains fewer than 13 PAT entries with APPROVED status | Flag population gap |

### 5.8 Proposal Section Rules (LV-SEC-)

| Rule | Name | Type | Condition | WP18D Action |
|---|---|---|---|---|
| LV-SEC-001 | Automation Type Declared | ERROR | `sec_ext.automation_type` is empty | Exclude from manifest; cannot drive content assembly |
| LV-SEC-002 | Content Source Assets Declared | WARNING | `sec_ext.content_source_assets[]` is empty for sections with automation_type = DIRECT or EXTRACT | Log warning; section included but may assemble without content |
| LV-SEC-003 | PLACEHOLDER Sections Flagged | WARNING | Any section with `sec_ext.automation_type = PLACEHOLDER` is in the manifest | Log; section will appear blank in output |
| LV-SEC-004 | Mandatory Pattern Coverage | ERROR | A PAT's `pat_ext.typical_sections` references a SEC that is not in the registry | Flag missing section registration |

---

## 6. Validation Rule Index

### 6.1 Summary Count

| Series | Count | Scope |
|---|---|---|
| RI- | 15 | Registry integrity — run on sync and before every assembly |
| AV- | 13 | Assembly validation — run per tender profile at assembly start |
| CLV- | 12 | Cross-library — run against assembled manifest |
| LV-CAP- | 5 | CAP-specific |
| LV-ASP- | 4 | ASP-specific |
| LV-ASM- | 5 | ASM-specific |
| LV-RSK- | 8 | RSK-specific |
| LV-MTH- | 3 | MTH-specific |
| LV-REF- | 4 | REF-specific |
| LV-PAT- | 3 | PAT-specific |
| LV-SEC- | 4 | SEC-specific |
| **Total** | **76** | |

### 6.2 BLOCK Rules (Assembly Halting)

The following rules halt assembly entirely when violated. These are the highest-priority rules for WP18D implementation.

| Rule | Trigger |
|---|---|
| RI-001 | Duplicate asset IDs in registry |
| RI-008 | Circular supersession chain |
| RI-009 | Circular parent-child chain |
| RI-011 | DRAFT asset marked approved_for_reuse |
| RI-012 | ARCHIVED asset marked approved_for_reuse |
| AV-001 | approved_for_reuse = false in manifest |
| AV-002 | Non-APPROVED asset in manifest (mandatory) |
| AV-004 | ARCHIVED asset in manifest |
| AV-008 | Mandatory asset missing from manifest |
| AV-009 | Excluded asset present in manifest (mandatory) |
| AV-010 | mandatory_if AND excluded_if both TRUE for same asset |
| AV-011 | RC-OPS-001 missing from non-P10 proposal |
| CLV-001 | approved_for_reuse gate |
| CLV-002 | Lifecycle state gate |
| CLV-007 | SUPERSEDED/ARCHIVED asset in manifest |
| CLV-008 | REF without AM clearance |
| LV-ASM-001 | ASM has no parent pack |
| LV-ASM-002 | ASM parent pack not APPROVED |
| LV-ASP-002 | ASP has pending decisions |
| LV-RSK-004 | RC-OPS-001 not marked unconditional |
| LV-RSK-008 | DRAFT risk in candidate manifest |
| LV-REF-001 | REF without AM clearance |

---

## 7. Validation Execution Order

WP18D should execute rules in this order for each assembly run:

```
Phase 1 — Registry Integrity (RI-001 to RI-015)
    Run once. If RI-001, RI-008, or RI-009 → BLOCK immediately.
    Log all other violations; continue if non-BLOCK.

Phase 2 — Tender Profile Establishment
    Resolve: pattern, platform, engagement_type, modules, country, client_size.
    Store as assembly context.

Phase 3 — Candidate Manifest Construction
    Apply AV-005, AV-006, AV-007 → filter registry to applicable assets.
    Apply AV-008 → add mandatory assets.
    Apply AV-009, AV-010 → remove excluded assets; flag conflicts.
    Apply AV-011 → check RC-OPS-001 for non-P10.

Phase 4 — Gate Checks on Manifest
    Apply AV-001, AV-002, AV-003, AV-004, AV-012, AV-013.
    Any BLOCK → halt; report.

Phase 5 — Cross-Library Validation
    Apply CLV-001 through CLV-012 on the filtered manifest.
    Any BLOCK → halt; report.

Phase 6 — Library-Specific Validation
    Apply LV-CAP, LV-ASP, LV-ASM, LV-RSK, LV-MTH, LV-REF, LV-PAT, LV-SEC.
    Order: PAT → SEC → ASP → ASM → CAP → RSK → REF → MTH.

Phase 7 — Validation Report Generation
    Aggregate all BLOCK / ERROR / WARNING results.
    Output VALIDATION_REPORT.md alongside the assembly manifest.
    VALIDATION_REPORT format: rule code, asset_id, severity, description, recommended action.

Phase 8 — Manifest Finalisation
    If zero BLOCK results: assembly manifest is VALID. Proceed.
    If any BLOCK results: manifest is BLOCKED. Do not proceed to assembly.
    If only ERROR/WARNING: manifest is APPROVED WITH CONDITIONS. Proceed with flags.
```

---

## 8. Validation Report Output Format

Each validation run produces a VALIDATION_REPORT embedded in the assembly manifest or as a sidecar file. Required fields per report entry:

```yaml
validation_results:
  - rule_code: AV-008
    severity: BLOCK
    asset_id: RC-OPS-001
    asset_type: RSK
    description: "Mandatory asset RC-OPS-001 is missing from the assembly manifest for a non-P10 proposal."
    recommended_action: "Add RC-OPS-001 to the manifest. This risk is unconditionally mandatory for all non-P10 proposals (LV-RSK-004)."
    
  - rule_code: CLV-008
    severity: BLOCK
    asset_id: REF-CAS-001
    asset_type: REF
    description: "REF-CAS-001 requires account manager clearance (account_manager_required = true). No clearance recorded in assembly context."
    recommended_action: "Obtain AM clearance for REF-CAS-001 or select an alternative reference. Do not include in proposal without clearance."
```

**Report summary block:**

```yaml
validation_summary:
  registry_version: "1.47"
  tender_id: "[Tender ID]"
  tender_pattern: "P1"
  validation_timestamp: "2026-06-27T10:30:00Z"
  total_rules_evaluated: 76
  blocks: 0
  errors: 2
  warnings: 5
  manifest_status: "APPROVED_WITH_CONDITIONS"
  proceed: true
```

---

## 9. Changelog

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-06-27 | Initial rules — 76 rules across 11 series; 22 BLOCK rules identified; execution order defined; validation report format specified |
