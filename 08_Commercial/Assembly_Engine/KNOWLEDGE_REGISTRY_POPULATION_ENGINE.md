---
document_id: KNOWLEDGE-REGISTRY-POPULATION-ENGINE-V1
title: "Knowledge Registry Population Engine — Architecture Specification V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-27"
created_by: "WP18E — Knowledge Registry Population Engine Architecture"
approved_by: "Architecture — WP18E"
approved_date: "2026-06-27"
approved_for_reuse: true
category: "Assembly Engine / Registry"
scope: "Defines the complete architecture, execution model, and component responsibilities for the Knowledge Registry Population Engine (KRPE) — the first executable component of the Knowledge Platform, responsible for converting the governed Markdown repository into the machine-readable registry consumed by the Knowledge Validation Engine."
related_documents:
  - KNOWLEDGE_ASSET_REGISTRY_STANDARD.md
  - KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md
  - KNOWLEDGE_REGISTRY_POPULATION_RULES.md
  - KNOWLEDGE_REGISTRY_VALIDATION_RULES.md
  - KNOWLEDGE_VALIDATION_ENGINE.md
  - REGISTRY_DISCOVERY_ENGINE.md
  - REGISTRY_EXTRACTION_ENGINE.md
  - REGISTRY_INDEX_ENGINE.md
  - REGISTRY_OUTPUT_SPECIFICATION.md
  - REGISTRY_INCREMENTAL_BUILD_MODEL.md
---

# Knowledge Registry Population Engine — Architecture Specification V1.0

**Work Package:** WP18E  
**Status:** APPROVED — Architecture specification complete. Implementation deferred to implementation work package.  
**Metaphor:** The KRPE is the compiler front-end of the Knowledge Platform. Like a compiler's lexer and parser, it reads source files, tokenises structured metadata, and produces an intermediate representation (the Registry) that the back-end (the KVE) can analyse.

---

## 1. Purpose

The Knowledge Registry Population Engine (KRPE) converts the governed Markdown repository into the five machine-readable registry files consumed by every downstream platform component.

**The KRPE has five responsibilities:**
1. **Discover** every governed knowledge asset in the repository
2. **Extract** structured metadata from each asset's source format
3. **Link** cross-asset relationships declared in that metadata
4. **Build** lookup indexes for fast engine queries
5. **Publish** the registry files and a build report

**The KRPE does NOT:**
- Infer business meaning — it only extracts what is explicitly declared
- Modify existing assets — it is read-only with respect to the repository
- Make governance decisions — it reports governance state, it does not apply it
- Validate the registry — that is the KVE's function (KNOWLEDGE_VALIDATION_ENGINE.md)

**Design principle:** If a field is not explicitly present in a source file, the KRPE either applies a documented default (per KNOWLEDGE_REGISTRY_POPULATION_RULES.md) or leaves the field as the empty sentinel (`""` or `[]`). The engine never guesses or infers.

---

## 2. Architectural Position

```
Knowledge Repository (Markdown + YAML frontmatter source files)
    │
    │  discovery + extraction (read-only)
    ▼
┌───────────────────────────────────────────────────────────────────┐
│              KNOWLEDGE REGISTRY POPULATION ENGINE                 │
│                                                                   │
│  ┌──────────────────┐   ┌──────────────────┐                    │
│  │ Discovery Engine │──►│ Extraction Engine│                    │
│  │ (asset location) │   │ (metadata parse) │                    │
│  └──────────────────┘   └────────┬─────────┘                    │
│                                   │                               │
│                        ┌──────────▼──────────┐                  │
│                        │ Relationship Linker  │                  │
│                        │ (cross-ref resolve) │                  │
│                        └──────────┬──────────┘                  │
│                                   │                               │
│              ┌────────────────────▼──────────────────┐           │
│              │ Index Engine + Registry Writer + Report│           │
│              └────────────────────┬──────────────────┘           │
└──────────────────────────────────-┼───────────────────────────────┘
                                    │
             ┌──────────────────────┼──────────────────────┐
             ▼                      ▼                      ▼
  KNOWLEDGE_ASSET_      KNOWLEDGE_RELATIONSHIP_   KNOWLEDGE_LOOKUP_
  REGISTRY.yaml         GRAPH.yaml                INDEX.yaml
             ▼                                            │
  KNOWLEDGE_ASSET_                         REGISTRY_BUILD_REPORT.yaml
  REGISTRY_ASSUMPTIONS.yaml
             │
             ▼ (all 5 output files consumed by)
  KNOWLEDGE VALIDATION ENGINE (KVE)
```

---

## 3. Engine Responsibilities

### 3.1 What the KRPE Owns

| Responsibility | Detail |
|---|---|
| Repository discovery | Identifying all governed asset files by path, type, and content |
| Metadata extraction | Parsing YAML frontmatter, Markdown tables, section-structured files |
| Field mapping | Applying KNOWLEDGE_REGISTRY_POPULATION_RULES.md mappings |
| Derivation | Computing derived fields (approved_for_reuse, review_due, pattern_applicability) |
| Relationship resolution | Building the cross-asset relationship graph |
| Index construction | Building all lookup indexes (REGISTRY_INDEX_ENGINE.md) |
| Registry publication | Writing the 5 output YAML files |
| Build reporting | Producing REGISTRY_BUILD_REPORT.yaml |
| Incremental rebuild | Detecting changed files and rebuilding only affected entries |

### 3.2 What the KRPE Does Not Own

| Outside Scope | Owner |
|---|---|
| Validating the registry contents | KVE (KNOWLEDGE_VALIDATION_ENGINE.md) |
| Applying governance decisions | BU Lead (human action) |
| Modifying asset content | BU Lead / Author |
| Deciding which assets to include | Governed by asset lifecycle_status |
| Proposal assembly | Assembly Engine |

---

## 4. Source Formats

The repository contains three distinct content formats. The KRPE uses a different **extraction adapter** for each:

### Format A — YAML Frontmatter Files

Used by: Capability Assets (individual .md files), Assumption Packs

Structure:
```
---
field_1: value
field_2: value
---

Markdown content body (not extracted — content stays in library files)
```

Adapter: `YAMLFrontmatterAdapter`  
Operation: Split file on `---` delimiter; parse first block as YAML; discard body

### Format B — Markdown Table Documents

Used by: MASTER_CAPABILITY_INDEX.md (augments CAP YAML), REFERENCE_MASTER.md

Structure:
```
# Header

| Col1 | Col2 | Col3 |
|---|---|---|
| val1 | val2 | val3 |
| val1 | val2 | val3 |
```

Adapter: `MarkdownTableAdapter`  
Operation: Locate `|---|` separator rows; extract header names; parse each data row into a dict keyed by column name

### Format C — Section-Structured Documents

Used by: ENTERPRISE_RISK_REGISTER_V1.md, PROPOSAL_PATTERN_ENGINE.md, CONTENT_SOURCE_MATRIX.md, METHODOLOGY_SELECTION_ENGINE.md, ASSUMPTION packs (for ASM rows)

Structure:
```
## Asset Title

[Optional YAML frontmatter or structured text within the section]

| field | value |
| --- | --- |
```

Adapter: `SectionStructuredAdapter`  
Operation: Split on `## ` heading boundaries; within each section, detect and parse embedded YAML or key-value table; each section = one asset entry

---

## 5. Engine Execution Model

### 5.1 Full Build Sequence

```
KRPE START (full build)
│
├── Phase 0: Load configuration
│     Read: KNOWLEDGE_REGISTRY_POPULATION_RULES.md (field mappings)
│     Read: KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md (schema + defaults)
│     Read: KNOWLEDGE_ASSET_STANDARD.md (asset types + ID formats)
│     Set: repo_root = [repository root path]
│     Set: output_dir = 00_Governance/Knowledge_Standards/
│
├── Phase 1: Discovery
│     Invoke: REGISTRY_DISCOVERY_ENGINE
│     Output: asset_manifest = list of {file_path, asset_type, source_format}
│     See: REGISTRY_DISCOVERY_ENGINE.md §4
│
├── Phase 2: Extraction
│     FOR each entry in asset_manifest (ordered by dependency):
│       PAT → SEC → MTH → REF → ASP → ASM → CAP → RSK
│     Invoke: REGISTRY_EXTRACTION_ENGINE[asset_type]
│     Each extractor returns: registry_entry dict (partial — no relationships yet)
│     Accumulate: core_registry = [] (non-ASM entries)
│     Accumulate: assumption_registry = [] (ASM entries only)
│
├── Phase 3: Cross-reference (MASTER_CAPABILITY_INDEX.md augmentation)
│     For each CAP entry in core_registry:
│       Look up row in MASTER_CAPABILITY_INDEX.md by asset_id
│       Merge: evidence_tier, governance_restrictions, pre_tender_controls,
│               reference_clients, industry, last_reviewed
│       (File-level YAML frontmatter takes precedence over index row on conflict)
│
├── Phase 4: Relationship Linking
│     Invoke: REGISTRY_RELATIONSHIP_LINKER
│     INPUT: core_registry + assumption_registry
│     PROCESS:
│       Resolve related_assets references (verify IDs exist)
│       Resolve supersedes / superseded_by chains
│       Link ASM → ASP (via parent_pack_id)
│       Link RSK → ASM (via related_assumptions)
│       Link CAP → REF (via reference_clients)
│       Link PAT → SEC (via pat_ext.typical_sections)
│     OUTPUT: relationship_graph = list of {source_id, rel_type, target_id, declared_in}
│     OUTPUT: Updated entries with resolved / flagged relationships
│
├── Phase 5: Index Building
│     Invoke: REGISTRY_INDEX_ENGINE
│     INPUT: core_registry + assumption_registry + relationship_graph
│     OUTPUT: lookup_index = {all named indexes}
│     See: REGISTRY_INDEX_ENGINE.md
│
├── Phase 6: Registry Writing
│     Write: KNOWLEDGE_ASSET_REGISTRY.yaml (core_registry — non-ASM)
│     Write: KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml (assumption_registry)
│     Write: KNOWLEDGE_RELATIONSHIP_GRAPH.yaml (relationship_graph)
│     Write: KNOWLEDGE_LOOKUP_INDEX.yaml (lookup_index)
│     Write: BUILD_MANIFEST.yaml (file paths + mtimes + hashes for incremental)
│
├── Phase 7: Build Report
│     Generate: REGISTRY_BUILD_REPORT.yaml
│     Include: entry counts by type, extraction errors, unresolved references,
│               derivation warnings, field coverage %, build timestamp
│
└── KRPE END
```

### 5.2 Extraction Ordering (Dependency Order)

Assets must be extracted in this order so parent records exist before child relationships are resolved:

```
1. PAT (Patterns — no dependencies)
2. SEC (Sections — depend on PAT for typical_sections)
3. MTH (Methodologies — depend on PAT for pattern_applicability)
4. REF (References — depend on PAT for pattern_applicability)
5. ASP (Packs — depend on PAT for pattern_applicability)
6. ASM (Assumptions — depend on ASP for parent_pack_id)
7. CAP (Capabilities — depend on PAT, SEC, REF)
8. RSK (Risks — depend on ASM for related_assumptions)
```

### 5.3 Failure Handling

| Failure | Engine Behaviour |
|---|---|
| File not found (expected by discovery) | Log EXTRACTION_ERROR; skip file; continue |
| YAML parse error | Log EXTRACTION_ERROR with file path + line; skip asset; continue |
| Table parse error | Log EXTRACTION_ERROR; skip row; continue |
| Missing mandatory field (after defaults applied) | Log EXTRACTION_WARNING; populate with empty sentinel; continue |
| Unresolvable relationship reference | Log LINK_WARNING; record relationship as UNRESOLVED; continue |
| Asset ID conflict (two files claim same ID) | Log EXTRACTION_ERROR; include first encountered; skip duplicate; continue |
| Output directory not writable | FATAL ERROR — halt engine; report path and permission issue |

The KRPE never halts on a per-asset error. A single bad file never stops the full build. All errors are collected and surfaced in REGISTRY_BUILD_REPORT.yaml.

---

## 6. Engine Components

### 6.1 Discovery Engine

**Specification:** REGISTRY_DISCOVERY_ENGINE.md  
**Responsibility:** Walk the repository, classify every file as a governed asset or not, return a typed asset manifest  
**Key output:** `asset_manifest = [{file_path, asset_type, source_format, index_source}]`

### 6.2 Extraction Engine

**Specification:** REGISTRY_EXTRACTION_ENGINE.md  
**Responsibility:** Parse each file using the appropriate adapter; map extracted fields to the registry schema per KNOWLEDGE_REGISTRY_POPULATION_RULES.md  
**Key output:** Per-asset registry entry dicts (pre-relationship)

### 6.3 Relationship Linker

**Specification:** REGISTRY_EXTRACTION_ENGINE.md §11 (relationship extraction) and REGISTRY_INDEX_ENGINE.md §2  
**Responsibility:** After all assets are extracted, resolve all declared relationships and build the relationship graph

### 6.4 Index Engine

**Specification:** REGISTRY_INDEX_ENGINE.md  
**Responsibility:** Build all named lookup indexes from the extracted + linked registry

### 6.5 Registry Writer

**Specification:** REGISTRY_OUTPUT_SPECIFICATION.md  
**Responsibility:** Serialise core_registry, assumption_registry, relationship_graph, and lookup_index to the 5 YAML output files

### 6.6 Build Reporter

**Specification:** REGISTRY_OUTPUT_SPECIFICATION.md §5  
**Responsibility:** Aggregate all extraction errors, warnings, counts, and metrics into REGISTRY_BUILD_REPORT.yaml

### 6.7 Incremental Build Manager

**Specification:** REGISTRY_INCREMENTAL_BUILD_MODEL.md  
**Responsibility:** On subsequent runs, compare file modification times and hashes to BUILD_MANIFEST; extract only changed files; re-link only affected relationships

---

## 7. Determinism Guarantees

The KRPE produces the same registry output given the same repository state. Determinism is achieved by:

1. **Ordered traversal**: Directory traversal is alphabetical. Entry order in YAML output is alphabetical by asset_id within each asset type.
2. **No randomness**: No UUIDs, no timestamps in asset data (timestamps only in build metadata)
3. **No inference**: Only explicitly declared metadata is extracted. Nothing is guessed.
4. **Idempotent writes**: The output files are completely overwritten on each full build. No append operations.
5. **Canonical YAML serialisation**: Fields are written in the same order on every run (field order per KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md §2)

---

## 8. Configuration

The KRPE is configured by three constants that may be set at invocation time:

```yaml
krpe_config:
  repo_root: ""                    # Absolute path to repository root
  output_dir: "00_Governance/Knowledge_Standards/"
  build_mode: "FULL"               # FULL / INCREMENTAL / DRY_RUN
  exclusion_paths:                 # Paths to skip during discovery
    - ".claude/"
    - "00_Governance/Archive/"
    - "07_Approved_Content/Candidate_Content/"
    - "07_Approved_Content/Review_Required/"
    - "08_Commercial/Reports/"
    - "08_Commercial/Assembly_Engine/KNOWLEDGE_VALIDATION_ENGINE.md"
    - "08_Commercial/Assembly_Engine/VALIDATION_RULE_EXECUTION_MODEL.md"
    - "08_Commercial/Assembly_Engine/KNOWLEDGE_VALIDATION_REPORT_STANDARD.md"
    - "08_Commercial/Assembly_Engine/KNOWLEDGE_HEALTH_SCORE.md"
  include_archived_assets: false   # If true, include ARCHIVED assets in registry
  write_dry_run_report: false      # If true (DRY_RUN mode), report what would change without writing
  population_rules_version: "1.0"
  schema_version: "1.0"
```

**DRY_RUN mode:** The engine performs full discovery and extraction but writes nothing. Outputs a DRY_RUN_REPORT showing what would be created, updated, or removed. Useful for validating configuration before committing.

---

## 9. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-27 | WP18E | Initial architecture — 7 components; 3 source formats; 8-phase execution; failure handling; determinism guarantees |
