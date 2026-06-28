---
document_id: REGISTRY-OUTPUT-SPECIFICATION-V1
title: "Registry Output Specification — Architecture Specification V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-27"
created_by: "WP18E — Knowledge Registry Population Engine Architecture"
approved_by: "Architecture — WP18E"
approved_date: "2026-06-27"
approved_for_reuse: true
category: "Assembly Engine / Registry"
scope: "Defines the complete schemas, file naming, storage locations, serialisation rules, and retention policies for all five YAML files produced by the KRPE."
related_documents:
  - KNOWLEDGE_REGISTRY_POPULATION_ENGINE.md
  - KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md
  - REGISTRY_INDEX_ENGINE.md
  - KNOWLEDGE_VALIDATION_ENGINE.md
---

# Registry Output Specification — Architecture Specification V1.0

**Work Package:** WP18E  
**Status:** APPROVED — Architecture specification complete.

---

## 1. Output File Inventory

| File | Location | Consumer | When Written |
|---|---|---|---|
| KNOWLEDGE_ASSET_REGISTRY.yaml | `00_Governance/Knowledge_Standards/` | KVE, Assembly Engine, TIL | Every build |
| KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml | `00_Governance/Knowledge_Standards/` | KVE, Assembly Engine | Every build |
| KNOWLEDGE_RELATIONSHIP_GRAPH.yaml | `00_Governance/Knowledge_Standards/` | KVE, Index Engine | Every build |
| KNOWLEDGE_LOOKUP_INDEX.yaml | `00_Governance/Knowledge_Standards/` | KVE, Assembly Engine, TIL | Every build |
| REGISTRY_BUILD_REPORT.yaml | `08_Commercial/Reports/` | Governance, BU Lead | Every build |

**Atomic write protocol:** All 5 files are written in a single transaction. If any write fails, all files from the current build are discarded and the previous build's files remain. This prevents a partial-build state where some files are from one version and some from an earlier version.

---

## 2. KNOWLEDGE_ASSET_REGISTRY.yaml

**Contains:** All non-ASM registry entries. Core entries for CAP, ASP, RSK, MTH, REF, PAT, SEC, CON, COM, PPT, PRT.

**Expected volume:** ~189 entries (as of WP18E).

### 2.1 File Schema

```yaml
---
registry_metadata:
  schema_version: "1.0"
  population_rules_version: "1.0"
  generated_at: "2026-06-27T09:00:00Z"
  generated_by: "KRPE v1.0"
  build_id: "BUILD-2026-06-27-001"
  build_mode: "FULL"
  source_repo_root: "/path/to/repo"
  total_entries: 189
  entries_by_type:
    CAP: 49
    ASP: 13
    RSK: 40
    MTH: 2
    REF: 16
    PAT: 13
    SEC: 56
    CON: 0
    COM: 0
    PPT: 0
    PRT: 0
  health_summary:
    draft_count: 40
    approved_count: 149
    approved_for_reuse_count: 149
    relationship_graph_entries: 0     # populated from KNOWLEDGE_RELATIONSHIP_GRAPH.yaml
---

assets:

  # ─────────────────────────────────────────────────────────────────
  # CAP — Capability Assets
  # ─────────────────────────────────────────────────────────────────

  - asset_id: "W3S1-001"
    asset_type: "CAP"
    title: "Oracle HCM — Organisation Management"
    version: "1.0"
    lifecycle_status: "APPROVED"
    approved_for_reuse: true
    owner_role: "BU Lead"
    owner_business_unit: "Oracle"
    approval_authority: "BU Lead"
    governing_standard: "KNOWLEDGE_ASSET_STANDARD.md"
    registry_version_added: "1.0"
    created: "2025-01-01"
    created_by: "APPSolve"
    approved_by: "BU Lead"
    approval_date: "2025-01-01"
    source_file: "06_Capabilities/Oracle/Oracle_HCM/W3S1-001-ORA-OrgMgmt.md"
    description: ""
    confidence_level: ""
    review_frequency: "annual"
    last_reviewed: ""
    review_due: ""
    governance_notes: ""
    pattern_applicability: []         # DEFERRED — populated in Phase 4
    proposal_sections: []             # DEFERRED — populated in Phase 4
    tags: []
    source_assets: []
    related_assets: []
    supersedes: ""
    superseded_by: ""
    library_index_ref: "06_Capabilities/MASTER_CAPABILITY_INDEX.md"
    registry_last_synced: "2026-06-27"
    validation_status: ""
    validation_issues: []
    assembly_rules:
      mandatory_if: ""
      optional_if: ""
      excluded_if: ""
      assembly_priority: 5
      section_placement: 0
      content_source_type: "CAPABILITY"
    cap_ext:
      source_document: "HIST-NNN"
      source_status: "APPROVED"
      prereq_statement: ""
      kb_destination: "Oracle/Oracle_HCM"
      wave: "W3"
      deliverable: "W3S1-001"
      tier1_evidence: ""
      governance_restrictions: ""
      pre_tender_controls: ""
      reference_clients: []
      industry: ""
      evidence_tier: ""
      named_reference: ""
```

### 2.2 Serialisation Rules

- **Field order:** Fields are written in the exact order defined in KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md §2. Implementers must not vary field order for readability — the canonical order enables diff-stable version control.
- **Empty strings:** `""` (not `null`, not absent)
- **Empty lists:** `[]` (not `null`, not absent)
- **Booleans:** `true` / `false` (not `True`/`False`, not `yes`/`no`)
- **Strings with colons:** Always quoted: `"value: with colon"`
- **Asset ordering:** Within each asset_type group, entries are sorted alphabetically by `asset_id`. Type order: CAP → ASP → RSK → MTH → REF → PAT → SEC → CON → COM → PPT → PRT.
- **Extension blocks:** The `cap_ext` / `asp_ext` etc. block appears LAST in each entry, after all core fields. Only the extension block matching `asset_type` is included.

---

## 3. KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml

**Contains:** All ASM entries (1,136 individual assumption records). Stored separately to keep the core registry manageable.

**Expected volume:** 1,136 entries (as of WP18E).

### 3.1 File Schema

```yaml
---
registry_metadata:
  schema_version: "1.0"
  generated_at: "2026-06-27T09:00:00Z"
  build_id: "BUILD-2026-06-27-001"
  total_asm_entries: 1136
  parent_pack_count: 13
  entries_by_pack:
    HCM-ORG-001: 87
    HCM-PAY-001: 94
    # ... all 13 packs
---

assumptions:

  - asset_id: "HCM-ORG-001-ASM-001"
    asset_type: "ASM"
    title: "Organisation structure defined before configuration"
    version: "1.0"
    lifecycle_status: "APPROVED"
    approved_for_reuse: true
    owner_role: "BU Lead"
    owner_business_unit: "Oracle"
    approval_authority: "BU Lead"
    governing_standard: "KNOWLEDGE_ASSET_STANDARD.md"
    registry_version_added: "1.0"
    created: ""
    created_by: ""
    approved_by: ""
    approval_date: ""
    source_file: "07_Assumption_Packs/HCM-ORG-001-OrganisationManagement.md"
    description: ""
    pattern_applicability: []
    proposal_sections: []
    tags: []
    related_assets: []
    supersedes: ""
    superseded_by: ""
    registry_last_synced: "2026-06-27"
    validation_status: ""
    validation_issues: []
    assembly_rules:
      mandatory_if: ""
      optional_if: ""
      excluded_if: ""
      assembly_priority: 5
      section_placement: 0
      content_source_type: "ASSUMPTION"
    asm_ext:
      parent_pack_id: "HCM-ORG-001"
      assumption_text: "The client's organisation structure will be finalised and documented before configuration begins."
      rationale: "Configuration of organisation management requires stable structure decisions."
      assumption_type: "TECHNICAL"
      dependency: ""
      risk_exposure: "MEDIUM"
      pending: false
      sequence: 1
```

### 3.2 Ordering

Entries are ordered by: `parent_pack_id` (alphabetical), then `asm_ext.sequence` (ascending integer). This groups all assumptions by pack and preserves their pack-internal sequence for readability and diff stability.

---

## 4. KNOWLEDGE_RELATIONSHIP_GRAPH.yaml

**Contains:** All resolved cross-asset relationships as a directed graph. Unresolved references are NOT included (they are recorded in REGISTRY_BUILD_REPORT.yaml).

### 4.1 File Schema

```yaml
---
graph_metadata:
  schema_version: "1.0"
  generated_at: "2026-06-27T09:00:00Z"
  build_id: "BUILD-2026-06-27-001"
  total_relationships: 0
  relationships_by_type:
    GOV: 0
    SRC: 0
    CON: 1136    # one per ASM (ASM contained-by ASP)
    XRF: 0
    SUP: 0
    GEN: 0
    RST: 0
  unresolved_count: 0
---

relationships:

  - source_id: "HCM-ORG-001"
    source_type: "ASP"
    relationship_type: "CON"
    relationship_label: "CONTAINS"
    target_id: "HCM-ORG-001-ASM-001"
    target_type: "ASM"
    declared_in: "KRPE REL-001 (parent_pack_id INHERIT)"
    rule_id: "REL-001"
    resolved: true
    bidirectional: false

  - source_id: "W3S1-001"
    source_type: "CAP"
    relationship_type: "XRF"
    relationship_label: "CROSS_REFERENCES"
    target_id: "HCM-ORG-001"
    target_type: "ASP"
    declared_in: "W3S1-001 frontmatter.prereq_statement"
    rule_id: "REL-010"
    resolved: true
    bidirectional: false
```

### 4.2 Ordering

Relationships are ordered by: `rule_id` ascending (REL-001 through REL-010), then `source_id` alphabetical, then `target_id` alphabetical.

### 4.3 Relationship Type Values

| Value | Label | Meaning |
|---|---|---|
| GOV | GOVERNS | Source asset governs target asset's content decisions |
| SRC | SOURCES | Source asset's content is sourced from target asset |
| CON | CONTAINS | Source asset contains target asset (e.g., ASP contains ASM) |
| XRF | CROSS_REFERENCES | Source asset references target for context or dependency |
| SUP | SUPERSEDES | Source asset supersedes target asset (target becomes SUPERSEDED) |
| GEN | GENERATES | Source asset generates target (e.g., PAT generates a proposal section) |
| RST | RESTRICTS | Source asset's assembly is restricted by target (e.g., RSK restricts patterns) |

---

## 5. KNOWLEDGE_LOOKUP_INDEX.yaml

**Contains:** All named lookup indexes defined in REGISTRY_INDEX_ENGINE.md. Single file for atomic consumption.

### 5.1 File Schema

```yaml
---
index_metadata:
  schema_version: "1.0"
  generated_at: "2026-06-27T09:00:00Z"
  build_id: "BUILD-2026-06-27-001"
  total_indexes: 20
---

indexes:

  asset_by_type:
    CAP: [W3S1-001, W3S1-002, ...]
    ASP: [HCM-ORG-001, ...]
    ASM: [HCM-ORG-001-ASM-001, ...]
    RSK: [RC-PROJ-001, ...]
    MTH: [MTH-001, ...]
    REF: [REF-001, ...]
    PAT: [P1, P2, ...]
    SEC: [S-1, S-2, ...]
    CON: []
    COM: []
    PPT: []
    PRT: []

  lifecycle_by_status:
    DRAFT: [RC-PROJ-001, ...]
    APPROVED: [W3S1-001, ...]
    SUPERSEDED: []
    ARCHIVED: []
    NORMALISED: []
    READY_FOR_REVIEW: []
    AUTO_APPROVED: []
    REVIEW_REQUIRED: []

  approved_assets:
    - W3S1-001
    - W3S1-002

  pattern_to_sections:
    P1:
      all_sections: []
      mandatory_sections: []
      optional_sections: []

  section_to_patterns:
    S-1:
      appears_in_patterns: []
      mandatory_in_patterns: []
      optional_in_patterns: []

  pattern_to_capabilities:
    P1: []

  capability_to_sections:
    W3S1-001: []

  cap_to_assumption_packs:
    W3S1-001: []

  pack_to_assumptions:
    HCM-ORG-001:
      - HCM-ORG-001-ASM-001
      - HCM-ORG-001-ASM-002

  assumption_to_pack:
    HCM-ORG-001-ASM-001: HCM-ORG-001

  risk_to_assumptions:
    RC-PROJ-001: []

  mandatory_risks:
    - RC-OPS-001

  pattern_to_risks:
    P1: []

  capability_to_references:
    W3S1-001: []

  pattern_to_methodologies:
    P1: []

  platform_capability_map:
    Oracle:
      Oracle_HCM: []
      Oracle_ERP: []
    Acumatica:
      Distribution: []
    BeBanking: []

  governance_category_map:
    Category-A: []
    Category-B: []

  supersession_chains:
    W3S1-001:
      supersedes: ""
      superseded_by: ""

  orphan_detection:
    assets_with_no_relationships: []
    assets_with_unresolved_relationships: []

  pattern_readiness_summary:
    P1:
      total_sections: 0
      mandatory_sections: 0
      sections_with_approved_cap: 0
      sections_missing_cap: 0
      approved_caps_count: 0
      applicable_methodologies_count: 0
      applicable_references_count: 0
      readiness_pct: 0
```

---

## 6. REGISTRY_BUILD_REPORT.yaml

**Contains:** Build statistics, extraction errors, unresolved relationships, warnings, coverage metrics, and build provenance.

**Location:** `08_Commercial/Reports/`

### 6.1 File Naming Convention

`REGISTRY_BUILD_REPORT_[YYYYMMDD]-[NNN].yaml`  
Example: `REGISTRY_BUILD_REPORT_20260627-001.yaml`

NNN is a sequence number within the date (allows multiple builds per day).

### 6.2 File Schema

```yaml
---
build_metadata:
  report_type: "REGISTRY_BUILD_REPORT"
  schema_version: "1.0"
  build_id: "BUILD-2026-06-27-001"
  build_mode: "FULL"      # FULL / INCREMENTAL / DRY_RUN
  generated_at: "2026-06-27T09:00:00Z"
  generated_by: "KRPE v1.0"
  source_repo: "/path/to/repo"
  population_rules_version: "1.0"
  schema_version_used: "1.0"
  build_duration_seconds: 45
  build_status: "SUCCESS"   # SUCCESS / SUCCESS_WITH_WARNINGS / FAILED

summary:
  total_files_scanned: 120
  total_assets_discovered: 1325
  total_assets_extracted: 1320
  total_assets_skipped: 5
  extraction_errors: 2
  extraction_warnings: 8
  unresolved_relationships: 12
  entries_by_type:
    CAP: 49
    ASP: 13
    ASM: 1136
    RSK: 40
    MTH: 2
    REF: 16
    PAT: 13
    SEC: 56
    CON: 0
    COM: 0
    PPT: 0
    PRT: 0
  field_coverage:
    core_mandatory_fields_pct: 96.3
    extension_fields_pct: 78.2
    deferred_fields_count: 412

extraction_errors:
  - error_code: "DUPLICATE_ID"
    severity: "ERROR"
    file_path: "06_Capabilities/Oracle/Oracle_HCM/W3S1-002-duplicate.md"
    asset_id: "W3S1-002"
    message: "Asset ID W3S1-002 already registered from W3S1-002-ORA-TalentMgmt.md. Second file skipped."
    action_taken: "SKIPPED"

extraction_warnings:
  - warning_code: "AUGMENT_WARNING"
    severity: "WARNING"
    file_path: "06_Capabilities/Oracle/Oracle_HCM/W3S1-048-ORA-NewCap.md"
    asset_id: "W3S1-048"
    message: "No matching row found in MASTER_CAPABILITY_INDEX.md. Asset registered with empty evidence_tier and governance_restrictions."
    action_taken: "REGISTERED_WITH_DEFAULTS"

unresolved_relationships:
  - source_id: "RC-PROJ-001"
    rule_id: "REL-003"
    target_id_declared: "HCM-ORG-001-ASM-MISSING"
    error: "TARGET_NOT_FOUND"
    message: "RSK related_assumption references ID that does not exist in assumption registry."

duplicate_id_conflicts:
  - asset_id: "W3S1-002"
    winning_file: "06_Capabilities/Oracle/Oracle_HCM/W3S1-002-ORA-TalentMgmt.md"
    losing_file: "06_Capabilities/Oracle/Oracle_HCM/W3S1-002-duplicate.md"

discovery_errors:
  - rule: "DR-006"
    path: "00_Governance/REFERENCE_MASTER.md"
    error: "FILE_NOT_FOUND"
    message: "Expected REFERENCE_MASTER.md not found. No REF entries extracted."

incremental_changes:
  added: []          # asset_ids added since last build (INCREMENTAL mode only)
  updated: []        # asset_ids updated
  removed: []        # asset_ids removed (marked ARCHIVED)
  unchanged_count: 0

output_files_written:
  - path: "00_Governance/Knowledge_Standards/KNOWLEDGE_ASSET_REGISTRY.yaml"
    entries: 189
    size_bytes: 0
  - path: "00_Governance/Knowledge_Standards/KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml"
    entries: 1136
    size_bytes: 0
  - path: "00_Governance/Knowledge_Standards/KNOWLEDGE_RELATIONSHIP_GRAPH.yaml"
    entries: 0
    size_bytes: 0
  - path: "00_Governance/Knowledge_Standards/KNOWLEDGE_LOOKUP_INDEX.yaml"
    entries: 20
    size_bytes: 0

recommendations:
  - priority: "HIGH"
    issue: "40 RSK assets in DRAFT state. WP18B-EXT.2 (BU Lead governance session ~2h) required before RSK assets are KVE-approved."
  - priority: "MEDIUM"
    issue: "12 unresolved relationships detected. Review risk register related_assumptions fields."
  - priority: "LOW"
    issue: "412 DEFERRED fields across all asset types. Populate after pattern mapping is complete."
```

### 6.3 Build Status Values

| Status | Meaning |
|---|---|
| SUCCESS | All extractions succeeded; zero errors |
| SUCCESS_WITH_WARNINGS | Extractions completed; some warnings or unresolved relationships |
| FAILED | Fatal error (e.g., output directory not writable); no files written |

### 6.4 Retention Policy

Build reports are retained for 3 years. Older reports may be archived to `08_Commercial/Reports/Archive/`. The most recent build report is always the canonical record of the registry's current build state.

---

## 7. BUILD_MANIFEST.yaml (Internal State File)

**Purpose:** Records file paths, modification times, and content hashes for the incremental build engine. Not a governance document — internal KRPE state only.  
**Location:** `[repo_root]/.krpe_state/BUILD_MANIFEST.yaml`  
**Excluded from:** discovery (EX-019), governance scope

### 7.1 Schema

```yaml
manifest_metadata:
  build_id: "BUILD-2026-06-27-001"
  generated_at: "2026-06-27T09:00:00Z"
  krpe_version: "1.0"

files:
  - path: "06_Capabilities/Oracle/Oracle_HCM/W3S1-001-ORA-OrgMgmt.md"
    mtime: 1751004800
    sha256: "abc123..."
    asset_ids_extracted: ["W3S1-001"]
    asset_types: ["CAP"]
  - path: "07_Assumption_Packs/HCM-ORG-001-OrganisationManagement.md"
    mtime: 1751004900
    sha256: "def456..."
    asset_ids_extracted: ["HCM-ORG-001", "HCM-ORG-001-ASM-001", ...]
    asset_types: ["ASP", "ASM"]
```

---

## 8. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-27 | WP18E | Initial specification — 5 output files; complete YAML schemas; serialisation rules; naming convention; retention policy |
