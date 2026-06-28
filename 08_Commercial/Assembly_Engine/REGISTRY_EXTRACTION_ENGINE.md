---
document_id: REGISTRY-EXTRACTION-ENGINE-V1
title: "Registry Extraction Engine — Architecture Specification V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-27"
created_by: "WP18E — Knowledge Registry Population Engine Architecture"
approved_by: "Architecture — WP18E"
approved_date: "2026-06-27"
approved_for_reuse: true
category: "Assembly Engine / Registry"
scope: "Defines the per-asset-type extraction rules, adapter specifications, field mapping logic, relationship extraction rules, and error handling for the KRPE Extraction Engine. This document is the implementation specification for converting each source format into a registry entry."
related_documents:
  - KNOWLEDGE_REGISTRY_POPULATION_ENGINE.md
  - REGISTRY_DISCOVERY_ENGINE.md
  - KNOWLEDGE_REGISTRY_POPULATION_RULES.md
  - KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md
---

# Registry Extraction Engine — Architecture Specification V1.0

**Work Package:** WP18E  
**Status:** APPROVED — Architecture specification complete.

---

## 1. Extraction Adapters

Three adapters handle all source formats. Each adapter is called by the type-specific extractor.

### 1.1 YAMLFrontmatterAdapter

**Used by:** CAP (individual files), ASP (pack header)

```
FUNCTION extract_yaml_frontmatter(file_path):
  content = read_file(file_path)
  IF NOT content.startswith("---"):
    RAISE ExtractionError("No YAML frontmatter found", file_path)
  
  parts = content.split("---", maxsplit=2)
  # parts[0] = "" (before first ---), parts[1] = YAML block, parts[2] = body
  IF len(parts) < 3:
    RAISE ExtractionError("Malformed YAML frontmatter (no closing ---)", file_path)
  
  TRY:
    metadata = yaml.safe_load(parts[1])
  EXCEPT yaml.YAMLError AS e:
    RAISE ExtractionError(f"YAML parse error: {e}", file_path)
  
  body = parts[2]  # Markdown content — not extracted; stays in library files
  RETURN metadata, body
```

### 1.2 MarkdownTableAdapter

**Used by:** MASTER_CAPABILITY_INDEX.md (CAP augmentation), REFERENCE_MASTER.md (REF)

```
FUNCTION extract_markdown_table(file_path):
  content = read_file(file_path)
  lines = content.split("\n")
  
  tables = []
  current_table = None
  
  FOR line IN lines:
    stripped = line.strip()
    IF stripped.startswith("|") AND stripped.endswith("|"):
      IF current_table IS None:
        current_table = {"headers": [], "rows": []}
      
      cells = [c.strip() FOR c IN stripped.strip("|").split("|")]
      
      # Detect separator row (---|---|---)
      IF all(re.match(r"^-+$", c) FOR c IN cells IF c):
        CONTINUE  # skip separator
      
      IF NOT current_table["headers"]:
        current_table["headers"] = cells
      ELSE:
        IF len(cells) == len(current_table["headers"]):
          row = dict(zip(current_table["headers"], cells))
          current_table["rows"].append(row)
    ELSE:
      IF current_table IS NOT None AND current_table["rows"]:
        tables.append(current_table)
      current_table = None
  
  IF current_table IS NOT None AND current_table["rows"]:
    tables.append(current_table)
  
  RETURN tables  # list of {headers: [], rows: [{col: val, ...}]}
```

### 1.3 SectionStructuredAdapter

**Used by:** PROPOSAL_PATTERN_ENGINE.md (PAT), CONTENT_SOURCE_MATRIX.md (SEC), ENTERPRISE_RISK_REGISTER_V1.md (RSK), METHODOLOGY_SELECTION_ENGINE.md (MTH)

```
FUNCTION extract_sections(file_path, heading_level="##"):
  content = read_file(file_path)
  
  # Split on the heading boundary
  heading_prefix = f"\n{heading_level} "
  raw_sections = content.split(heading_prefix)
  
  # First element is document preamble — skip
  sections = []
  FOR raw IN raw_sections[1:]:
    lines = raw.split("\n")
    title = lines[0].strip()
    body = "\n".join(lines[1:])
    
    # Attempt to extract key-value table within section
    kv_data = extract_kv_table(body)
    
    sections.append({
      "title": title,
      "body": body,
      "kv_data": kv_data
    })
  
  RETURN sections
```

```
FUNCTION extract_kv_table(body):
  # Finds and parses a | field | value | table within a section body
  result = {}
  FOR line IN body.split("\n"):
    IF "|" IN line AND line.strip().startswith("|"):
      cells = [c.strip() FOR c IN line.strip().strip("|").split("|")]
      IF len(cells) == 2 AND cells[0] AND NOT all(c == "-" FOR c IN cells[0]):
        result[cells[0]] = cells[1]
  RETURN result
```

---

## 2. Field Mapping Conventions

All extractors apply field mappings from `KNOWLEDGE_REGISTRY_POPULATION_RULES.md`. Mapping notation:

| Notation | Meaning |
|---|---|
| EXTRACT | Take the value directly from the named source field |
| DERIVE | Compute the value from one or more source fields |
| DEFAULT | Use a fixed value when the source field is absent |
| DEFERRED | Leave empty — will be populated in a later work package |
| INHERIT | Copy from the parent asset (e.g., ASM inherits pack_id from ASP) |

**Missing mandatory fields:** Apply DEFAULT if one is defined in KNOWLEDGE_REGISTRY_POPULATION_RULES.md. If no default exists, populate with empty sentinel (`""` or `[]`). Log EXTRACTION_WARNING.

**Type coercion:**
- Boolean fields: `"true"`, `"yes"`, `"1"` → `true`; `"false"`, `"no"`, `"0"` → `false`; absent → `false`
- List fields: Comma-separated strings are split on `,` and stripped. Already-list YAML values are used as-is.
- Date fields: Passed through as strings. No normalisation (dates in source files are canonical).

---

## 3. CAP Extractor

**Source:** Individual .md files in `06_Capabilities/**/*.md`  
**Adapter:** YAMLFrontmatterAdapter (primary) + MarkdownTableAdapter (augmentation from MASTER_CAPABILITY_INDEX.md)

### 3.1 Phase 2 Extraction (from individual file frontmatter)

| Registry Field | Source Field | Notation | Notes |
|---|---|---|---|
| asset_id | document_id | EXTRACT | |
| asset_type | — | DEFAULT: "CAP" | |
| title | title | EXTRACT | |
| version | version | EXTRACT | |
| lifecycle_status | status | EXTRACT | |
| approved_for_reuse | approved_for_reuse | EXTRACT | Boolean coercion |
| owner_business_unit | business_unit | EXTRACT | |
| owner_role | — | DEFAULT: "BU Lead" | |
| approval_authority | — | DEFAULT: "BU Lead" | |
| governing_standard | — | DEFAULT: "KNOWLEDGE_ASSET_STANDARD.md" | |
| registry_version_added | — | DEFAULT: "1.0" | |
| created | created | EXTRACT | |
| created_by | created_by | EXTRACT | |
| approved_by | approved_by | EXTRACT | |
| approval_date | approved | EXTRACT | |
| source_file | — | DERIVE: file_path (relative) | |
| tags | tags | EXTRACT | List field |
| cap_ext.source_document | source_document | EXTRACT | |
| cap_ext.source_status | source_status | EXTRACT | |
| cap_ext.prereq_statement | prereq_statement | EXTRACT | |
| cap_ext.kb_destination | kb_destination | EXTRACT | |
| cap_ext.wave | wave | EXTRACT | |
| cap_ext.deliverable | deliverable | EXTRACT | |
| cap_ext.evidence_tier | — | DEFERRED | Populated in Phase 3 from MASTER_CAPABILITY_INDEX.md |
| cap_ext.governance_restrictions | — | DEFERRED | Populated in Phase 3 |
| cap_ext.pre_tender_controls | — | DEFERRED | Populated in Phase 3 |
| cap_ext.reference_clients | — | DEFERRED | Populated in Phase 3 |
| cap_ext.industry | — | DEFERRED | Populated in Phase 3 |
| last_reviewed | — | DEFERRED | Populated in Phase 3 |
| pattern_applicability | — | DEFERRED | Populated in Phase 4 relationship linking |
| proposal_sections | — | DEFERRED | Populated in Phase 4 relationship linking |
| assembly_rules | — | DEFERRED | Populated in Phase 4 from pattern definitions |

### 3.2 Phase 3 Augmentation (from MASTER_CAPABILITY_INDEX.md)

The MASTER_CAPABILITY_INDEX.md has 11 columns:
`Cap ID | Capability Name | Product Area | Approved Document | Tier 1 Evidence | Named Reference | Reference Client | Industry | Evidence Tier | Governance Restrictions | Last Review`

Column mapping:
| Index Column | Registry Field |
|---|---|
| Cap ID | Match key — verify equals asset_id from Phase 2 |
| Capability Name | (verified matches title — log warning on mismatch) |
| Approved Document | cap_ext.source_file_index (secondary record — not overwriting source_file) |
| Tier 1 Evidence | cap_ext.tier1_evidence |
| Named Reference | cap_ext.named_reference |
| Reference Client | cap_ext.reference_clients |
| Industry | cap_ext.industry |
| Evidence Tier | cap_ext.evidence_tier |
| Governance Restrictions | cap_ext.governance_restrictions |
| Last Review | last_reviewed |

**Conflict resolution:** File-level YAML frontmatter takes precedence on any field present in both sources.

**Unmatched CAP:** If a CAP file's `document_id` is not found in MASTER_CAPABILITY_INDEX.md, log EXTRACTION_WARNING and continue. The CAP entry is still registered — it may be a newly created asset awaiting index update.

---

## 4. RSK Extractor

**Source:** `08_Commercial/Risk_Library/ENTERPRISE_RISK_REGISTER_V1.md`  
**Adapter:** SectionStructuredAdapter

Each section in the risk register = one RSK entry.

| Registry Field | Source KV Field | Notation | Notes |
|---|---|---|---|
| asset_id | risk_id | EXTRACT | |
| asset_type | — | DEFAULT: "RSK" | |
| title | risk_name | EXTRACT | |
| version | — | DEFAULT: "1.0" | |
| lifecycle_status | approval_status | EXTRACT | |
| approved_for_reuse | — | DERIVE: `true` if lifecycle_status = "APPROVED" else `false` | |
| owner_business_unit | — | DEFAULT: "Commercial" | |
| owner_role | — | DEFAULT: "BU Lead" | |
| approval_authority | — | DEFAULT: "BU Lead" | |
| governing_standard | — | DEFAULT: "KNOWLEDGE_ASSET_STANDARD.md" | |
| registry_version_added | — | DEFAULT: "1.0" | |
| created | — | DEFAULT: "" | DEFERRED — not in current register format |
| created_by | — | DEFAULT: "" | |
| source_file | — | DERIVE: "08_Commercial/Risk_Library/ENTERPRISE_RISK_REGISTER_V1.md" | |
| rsk_ext.governance_category | category | EXTRACT | Category-A or Category-B |
| rsk_ext.risk_title | risk_name | EXTRACT | |
| rsk_ext.risk_description | risk_description | EXTRACT | |
| rsk_ext.probability | probability | EXTRACT | |
| rsk_ext.impact | impact | EXTRACT | |
| rsk_ext.net_rating | net_rating | EXTRACT | |
| rsk_ext.mandatory_if_engagement | mandatory_if_engagement | EXTRACT | Boolean |
| rsk_ext.applicable_patterns | applicable_patterns | EXTRACT | List |
| rsk_ext.risk_response | risk_response | EXTRACT | |
| rsk_ext.mitigation_strategy | mitigation_strategy | EXTRACT | |
| rsk_ext.contractual_lever | contractual_lever | EXTRACT | |
| rsk_ext.owner_role | owner_role | EXTRACT | |
| rsk_ext.decision_ref | decision_ref | EXTRACT | For Category-B |
| rsk_ext.related_assumptions | related_assumptions | EXTRACT | List — resolved in Phase 4 |
| assembly_rules.mandatory_if | — | DERIVE: `mandatory_if_engagement = "TRUE"` → mandatory_if: "TRUE" | |
| assembly_rules.assembly_priority | net_rating | DERIVE: HIGH=1, MEDIUM=2, LOW=3 | |
| lifecycle_status | approval_status | EXTRACT | Map: "DRAFT" / "APPROVED" |

---

## 5. ASP Extractor

**Source:** `07_Assumption_Packs/**/*.md`  
**Adapter:** YAMLFrontmatterAdapter (for pack-level metadata)

| Registry Field | Source Field | Notation | Notes |
|---|---|---|---|
| asset_id | pack_id | EXTRACT | |
| asset_type | — | DEFAULT: "ASP" | |
| title | pack_name | EXTRACT | |
| version | version | EXTRACT | |
| lifecycle_status | status | EXTRACT | |
| approved_for_reuse | approved_for_reuse | EXTRACT | Boolean |
| owner_business_unit | business_unit | EXTRACT | |
| owner_role | — | DEFAULT: "BU Lead" | |
| approval_authority | — | DEFAULT: "BU Lead" | |
| governing_standard | — | DEFAULT: "KNOWLEDGE_ASSET_STANDARD.md" | |
| registry_version_added | — | DEFAULT: "1.0" | |
| created | created | EXTRACT | |
| created_by | created_by | EXTRACT | |
| approved_by | approved_by | EXTRACT | |
| approval_date | approved | EXTRACT | |
| source_file | — | DERIVE: file_path (relative) | |
| asp_ext.module_scope | module_scope | EXTRACT | |
| asp_ext.pack_scope | pack_scope | EXTRACT | |
| asp_ext.assumption_count | — | DERIVE: count of ASM rows extracted from this file |
| asp_ext.pending_decisions | pending_decisions | EXTRACT | |
| asp_ext.pattern_applicability | pattern_applicability | EXTRACT | List |
| asp_ext.engagement_types | engagement_types | EXTRACT | List |

---

## 6. ASM Extractor

**Source:** Same `07_Assumption_Packs/**/*.md` files as ASP  
**Adapter:** SectionStructuredAdapter applied to the file body (after YAML frontmatter)  
**Parent:** The ASP entry extracted in §5

The body of each assumption pack file contains structured assumption rows. Each row is one ASM entry.

### 6.1 Assumption Row Detection

Assumption rows are identified by a structured Markdown format within the pack body. Supported formats:

**Format 1 — Numbered section headings:**
```
### ASM-NNN: Assumption Title

| Field | Value |
|---|---|
| assumption_text | ... |
| rationale | ... |
```

**Format 2 — Table row per assumption:**
```
| ASM-ID | Assumption Text | Rationale | Status | ... |
|---|---|---|---|---|
| HCM-ORG-001-ASM-001 | ... | ... | APPROVED | ... |
```

**Adapter behaviour:** Try Format 1 first (section detection). If no `### ` headings with ASM IDs are found, fall back to Format 2 (table row detection). Log which format was detected in build report.

### 6.2 ASM Field Mapping

| Registry Field | Source | Notation | Notes |
|---|---|---|---|
| asset_id | assumption_id | EXTRACT | Format: `[PACK_ID]-ASM-[NNN]` |
| asset_type | — | DEFAULT: "ASM" | |
| title | assumption_title | EXTRACT | |
| version | — | INHERIT: parent ASP version | |
| lifecycle_status | status | EXTRACT | |
| approved_for_reuse | — | DERIVE: `true` if lifecycle_status = "APPROVED" | |
| owner_business_unit | — | INHERIT: parent ASP owner_business_unit | |
| source_file | — | DERIVE: parent ASP source_file | |
| asm_ext.parent_pack_id | — | INHERIT: parent ASP asset_id | |
| asm_ext.assumption_text | assumption_text | EXTRACT | |
| asm_ext.rationale | rationale | EXTRACT | |
| asm_ext.assumption_type | assumption_type | EXTRACT | TECHNICAL / COMMERCIAL / OPERATIONAL |
| asm_ext.dependency | dependency | EXTRACT | |
| asm_ext.risk_exposure | risk_exposure | EXTRACT | |
| asm_ext.pending | pending | EXTRACT | Boolean |
| asm_ext.sequence | — | DERIVE: ordinal position within pack (1-N) | |

---

## 7. PAT Extractor

**Source:** `08_Commercial/Assembly_Engine/PROPOSAL_PATTERN_ENGINE.md`  
**Adapter:** SectionStructuredAdapter (split on `## P` headings)

| Registry Field | Source KV | Notation | Notes |
|---|---|---|---|
| asset_id | pattern_id | EXTRACT | Format: P1–P13 |
| asset_type | — | DEFAULT: "PAT" | |
| title | pattern_name | EXTRACT | |
| version | — | DEFAULT: "1.0" | |
| lifecycle_status | — | DEFAULT: "APPROVED" | Patterns are governed document |
| approved_for_reuse | — | DEFAULT: true | |
| source_file | — | DERIVE: "08_Commercial/Assembly_Engine/PROPOSAL_PATTERN_ENGINE.md" | |
| pat_ext.typical_sections | typical_sections | EXTRACT | List of S-IDs |
| pat_ext.mandatory_sections | mandatory_sections | EXTRACT | List of S-IDs |
| pat_ext.optional_sections | optional_sections | EXTRACT | List of S-IDs |
| pat_ext.applicable_platforms | applicable_platforms | EXTRACT | List |
| pat_ext.engagement_types | engagement_types | EXTRACT | List |
| pat_ext.pattern_description | pattern_description | EXTRACT | |
| assembly_rules.assembly_priority | — | DEFAULT: 5 | |
| assembly_rules.content_source_type | — | DEFAULT: "PATTERN" | |

---

## 8. SEC Extractor

**Source:** `08_Commercial/Assembly_Engine/CONTENT_SOURCE_MATRIX.md`  
**Adapter:** SectionStructuredAdapter (split on `## S-` headings)

| Registry Field | Source KV | Notation | Notes |
|---|---|---|---|
| asset_id | section_id | EXTRACT | Format: S-1 through S-56 |
| asset_type | — | DEFAULT: "SEC" | |
| title | section_name | EXTRACT | |
| version | — | DEFAULT: "1.0" | |
| lifecycle_status | — | DEFAULT: "APPROVED" | |
| approved_for_reuse | — | DEFAULT: true | |
| source_file | — | DERIVE: "08_Commercial/Assembly_Engine/CONTENT_SOURCE_MATRIX.md" | |
| sec_ext.section_description | description | EXTRACT | |
| sec_ext.content_source_type | content_source | EXTRACT | DETERMINISTIC / DYNAMIC / HYBRID |
| sec_ext.applicable_patterns | applicable_patterns | EXTRACT | List of P-IDs |
| sec_ext.mandatory_in_patterns | mandatory_in | EXTRACT | List of P-IDs |
| sec_ext.source_capability_ids | source_capabilities | EXTRACT | List of CAP IDs |
| sec_ext.generation_method | generation_method | EXTRACT | |
| assembly_rules.section_placement | section_order | EXTRACT | Integer |
| assembly_rules.content_source_type | content_source | EXTRACT | |
| assembly_rules.mandatory_if | mandatory_in | DERIVE: if non-empty, "pattern IN [mandatory_in]" | |

---

## 9. MTH Extractor

**Source:** `08_Commercial/Assembly_Engine/METHODOLOGY_SELECTION_ENGINE.md`  
**Adapter:** SectionStructuredAdapter

| Registry Field | Source KV | Notation | Notes |
|---|---|---|---|
| asset_id | methodology_id | EXTRACT | Format: MTH-NNN |
| asset_type | — | DEFAULT: "MTH" | |
| title | methodology_name | EXTRACT | |
| version | — | DEFAULT: "1.0" | |
| lifecycle_status | — | DEFAULT: "APPROVED" | |
| approved_for_reuse | — | DEFAULT: true | |
| source_file | — | DERIVE: "08_Commercial/Assembly_Engine/METHODOLOGY_SELECTION_ENGINE.md" | |
| mth_ext.methodology_description | description | EXTRACT | |
| mth_ext.applicable_platforms | platforms | EXTRACT | List |
| mth_ext.applicable_engagement_types | engagement_types | EXTRACT | List |
| mth_ext.phase_structure | phases | EXTRACT | |
| mth_ext.deliverables | deliverables | EXTRACT | |
| pattern_applicability | applicable_patterns | EXTRACT | List of P-IDs |

---

## 10. REF Extractor

**Source:** `00_Governance/REFERENCE_MASTER.md`  
**Adapter:** MarkdownTableAdapter  
**Note:** File is .md not .csv — see Technical Debt TD-014 in REGISTRY_DISCOVERY_ENGINE.md

Each row in the reference table = one REF asset.

Expected columns (to be confirmed against actual file content):
`Reference ID | Client Name | Project Name | Platform | Engagement Type | Signed Date | NDA | Scope | Outcome | BEE Level | Industry | Geography`

| Registry Field | Table Column | Notation | Notes |
|---|---|---|---|
| asset_id | Reference ID | EXTRACT | |
| asset_type | — | DEFAULT: "REF" | |
| title | Project Name | EXTRACT | |
| version | — | DEFAULT: "1.0" | |
| lifecycle_status | — | DEFAULT: "APPROVED" | |
| approved_for_reuse | NDA | DERIVE: `false` if NDA = "YES", else `true` | |
| source_file | — | DERIVE: "00_Governance/REFERENCE_MASTER.md" | |
| ref_ext.client_name | Client Name | EXTRACT | |
| ref_ext.project_name | Project Name | EXTRACT | |
| ref_ext.platform | Platform | EXTRACT | |
| ref_ext.engagement_type | Engagement Type | EXTRACT | |
| ref_ext.signed_date | Signed Date | EXTRACT | |
| ref_ext.nda | NDA | EXTRACT | Boolean |
| ref_ext.scope | Scope | EXTRACT | |
| ref_ext.outcome | Outcome | EXTRACT | |
| ref_ext.bee_level | BEE Level | EXTRACT | |
| ref_ext.industry | Industry | EXTRACT | |
| ref_ext.geography | Geography | EXTRACT | |

**Column name mismatch handling:** If an expected column is absent from the table header, log EXTRACTION_WARNING and populate the corresponding registry field with `""`. The engine does not fail on missing columns.

---

## 11. Relationship Extraction

After all assets are extracted into `core_registry` and `assumption_registry`, the Relationship Linker runs a second pass to build the relationship graph.

### 11.1 Relationship Resolution Rules

| Rule ID | Source Asset | Relationship | Target Lookup | Notes |
|---|---|---|---|---|
| REL-001 | ASM | CON (CONTAINS) ← ASP | `parent_pack_id` → ASP | INHERIT relationship — every ASM is contained by its parent ASP |
| REL-002 | ASP | SRC (SOURCES) ← CAP | `source_document` field in CAP frontmatter matches pack source | DERIVE from CAP.cap_ext.source_document containing pack reference |
| REL-003 | RSK | XRF (CROSS_REF) ↔ ASM | `rsk_ext.related_assumptions` list → each ASM ID | EXTRACT from RSK — resolve each ID |
| REL-004 | PAT | RST (RESTRICTS) → CAP | `pat_ext.applicable_platforms` restricts which CAP assets apply | DERIVE from platform overlap |
| REL-005 | PAT | CON (CONTAINS) → SEC | `pat_ext.typical_sections` list → each SEC ID | EXTRACT from PAT — resolve each S-ID |
| REL-006 | SEC | SRC (SOURCES) ← CAP | `sec_ext.source_capability_ids` → each CAP ID | EXTRACT from SEC |
| REL-007 | CAP | XRF (CROSS_REF) → REF | `cap_ext.reference_clients` → REF asset IDs | EXTRACT from CAP augmentation |
| REL-008 | ASP | GOV (GOVERNS) ← PAT | `asp_ext.pattern_applicability` → PAT IDs | EXTRACT from ASP |
| REL-009 | RSK | RST (RESTRICTS) → PAT | `rsk_ext.applicable_patterns` → PAT IDs | EXTRACT from RSK |
| REL-010 | CAP | XRF → ASP | `prereq_statement` parsed for pack ID references | EXTRACT + PARSE from CAP.cap_ext.prereq_statement |

### 11.2 Resolution Algorithm

```
FUNCTION resolve_relationships(core_registry, assumption_registry):
  all_ids = {e.asset_id for e IN core_registry + assumption_registry}
  relationship_graph = []
  unresolved = []
  
  FOR rule IN [REL-001 ... REL-010]:
    FOR source_entry IN get_sources(rule, core_registry, assumption_registry):
      target_ids = get_target_ids(rule, source_entry)
      
      FOR target_id IN target_ids:
        IF target_id IN all_ids:
          relationship_graph.append({
            "source_id": source_entry.asset_id,
            "source_type": source_entry.asset_type,
            "relationship_type": rule.rel_type,
            "target_id": target_id,
            "target_type": get_type(target_id, all_ids),
            "declared_in": rule.declared_in,
            "rule_id": rule.id,
            "resolved": true
          })
        ELSE:
          unresolved.append({
            "source_id": source_entry.asset_id,
            "target_id_declared": target_id,
            "rule_id": rule.id,
            "error": "TARGET_NOT_FOUND"
          })
  
  RETURN relationship_graph, unresolved
```

### 11.3 Unresolved Reference Handling

All unresolved references are logged in REGISTRY_BUILD_REPORT.yaml under `unresolved_relationships`. The relationship is NOT added to the graph. The KVE CLV rules will then detect the missing relationship and report it as a validation issue.

---

## 12. Extraction Error Taxonomy

| Error Code | Severity | Meaning |
|---|---|---|
| EXTRACTION_ERROR | ERROR | Fatal per-asset — asset skipped; build continues |
| EXTRACTION_WARNING | WARNING | Non-fatal — asset extracted with missing/defaulted fields |
| LINK_WARNING | WARNING | Relationship declared but target not found |
| AUGMENT_WARNING | WARNING | MASTER_CAPABILITY_INDEX.md row not found for CAP asset |
| DUPLICATE_ID | ERROR | Two files claim the same asset_id — second skipped |
| FORMAT_MISMATCH | WARNING | File content does not match expected format pattern |

---

## 13. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-27 | WP18E | Initial specification — 3 adapters; 10 asset-type extractors; 10 relationship resolution rules; error taxonomy |
