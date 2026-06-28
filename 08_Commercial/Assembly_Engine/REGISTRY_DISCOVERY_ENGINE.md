---
document_id: REGISTRY-DISCOVERY-ENGINE-V1
title: "Registry Discovery Engine — Architecture Specification V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-27"
created_by: "WP18E — Knowledge Registry Population Engine Architecture"
approved_by: "Architecture — WP18E"
approved_date: "2026-06-27"
approved_for_reuse: true
category: "Assembly Engine / Registry"
scope: "Defines the complete repository traversal algorithm, asset classification rules, exclusion rules, and discovery manifest schema used by the KRPE Discovery Engine."
related_documents:
  - KNOWLEDGE_REGISTRY_POPULATION_ENGINE.md
  - REGISTRY_EXTRACTION_ENGINE.md
  - KNOWLEDGE_ASSET_STANDARD.md
---

# Registry Discovery Engine — Architecture Specification V1.0

**Work Package:** WP18E  
**Status:** APPROVED — Architecture specification complete.

---

## 1. Purpose

The Discovery Engine walks the repository filesystem, classifies every file against the governed asset taxonomy, and returns a typed **asset manifest** — the complete, ordered list of files to be extracted.

The Discovery Engine is purely addressive. It decides **what to extract** but not **how**. Every classification decision is based on declarative rules (path patterns, file naming, and content detection), not heuristics or AI inference.

---

## 2. Asset Manifest Schema

The Discovery Engine's output:

```yaml
asset_manifest:
  generated_at: "2026-06-27T09:00:00Z"
  repo_root: "/path/to/repo"
  total_files_scanned: 0
  total_assets_discovered: 0
  discovery_errors: []
  entries:
    - file_path: "06_Capabilities/Oracle/Oracle_HCM/W3S1-002-ORA-TalentMgmt.md"
      asset_type: "CAP"
      source_format: "YAML_FRONTMATTER"
      discovery_rule: "DR-004"
      asset_id_hint: ""          # Empty — extracted from frontmatter in Phase 2
      index_source: "MASTER_CAPABILITY_INDEX.md"  # Secondary augmentation source
      discovery_notes: ""
    - file_path: "08_Commercial/Risk_Library/ENTERPRISE_RISK_REGISTER_V1.md"
      asset_type: "RSK"
      source_format: "SECTION_STRUCTURED"
      discovery_rule: "DR-007"
      asset_id_hint: "multi-entry"
      index_source: ""
      discovery_notes: "Contains multiple RSK entries — SectionStructuredAdapter"
```

**asset_manifest fields:**

| Field | Description |
|---|---|
| file_path | Repository-relative path to the source file |
| asset_type | CAP / ASP / ASM / RSK / MTH / REF / PAT / SEC |
| source_format | YAML_FRONTMATTER / MARKDOWN_TABLE / SECTION_STRUCTURED |
| discovery_rule | Rule ID that triggered classification (DR-001 through DR-010) |
| asset_id_hint | Pre-classification ID guess if determinable from filename; empty if not |
| index_source | Secondary augmentation file for this asset (e.g., MASTER_CAPABILITY_INDEX.md for CAP) |
| discovery_notes | Human-readable note about multi-entry files or special handling |

---

## 3. Repository Layout (Canonical)

The Discovery Engine operates on this known repository structure:

```
[repo_root]/
├── 00_Governance/
│   ├── Knowledge_Standards/          ← governance docs (not assets; skip)
│   │   └── KNOWLEDGE_ASSET_REGISTRY.yaml  ← output files (skip)
│   ├── Archive/                      ← EXCLUDED — see §5
│   └── REFERENCE_MASTER.md           ← REF source (Format B: Markdown table)
│
├── 06_Capabilities/                  ← CAP source (Format A: YAML frontmatter)
│   ├── MASTER_CAPABILITY_INDEX.md    ← CAP augmentation (Format B: Markdown table)
│   ├── Oracle/
│   │   ├── Oracle_HCM/
│   │   │   └── W3S1-NNN-ORA-*.md    ← individual CAP files
│   │   └── Oracle_ERP/
│   │       └── W3S1-NNN-ORA-*.md
│   ├── Acumatica/
│   │   └── Distribution/
│   │       └── W3S1-NNN-ACU-*.md
│   └── ...
│
├── 07_Assumption_Packs/              ← ASP + ASM source (Format A for ASP header)
│   └── [PACK_ID]-[Name].md          ← each file = 1 ASP + N ASM rows
│
├── 08_Commercial/
│   ├── Risk_Library/
│   │   └── ENTERPRISE_RISK_REGISTER_V1.md  ← RSK source (Format C)
│   ├── Assembly_Engine/
│   │   ├── PROPOSAL_PATTERN_ENGINE.md      ← PAT source (Format C)
│   │   ├── CONTENT_SOURCE_MATRIX.md        ← SEC source (Format C)
│   │   ├── METHODOLOGY_SELECTION_ENGINE.md ← MTH source (Format C)
│   │   └── [engine architecture docs]      ← engine docs (skip — see §5)
│   └── Reports/                            ← EXCLUDED — see §5
│
└── [admin files]                           ← EXCLUDED — see §5
    ├── HANDOVER.md
    ├── AI_CONTEXT.md
    └── WP18Z_SESSION_BASELINE.md
```

---

## 4. Discovery Rules

### DR-001 — Pattern Assets (PAT)

**Trigger:** File path matches exactly `08_Commercial/Assembly_Engine/PROPOSAL_PATTERN_ENGINE.md`  
**Asset type:** PAT  
**Source format:** SECTION_STRUCTURED  
**Index source:** (none)  
**Notes:** Single file contains all P1–P13 pattern definitions. SectionStructuredAdapter splits on `## P` headings.

---

### DR-002 — Section Assets (SEC)

**Trigger:** File path matches exactly `08_Commercial/Assembly_Engine/CONTENT_SOURCE_MATRIX.md`  
**Asset type:** SEC  
**Source format:** SECTION_STRUCTURED  
**Index source:** (none)  
**Notes:** Single file contains all S-1 through S-56 section definitions.

---

### DR-003 — Methodology Assets (MTH)

**Trigger:** File path matches exactly `08_Commercial/Assembly_Engine/METHODOLOGY_SELECTION_ENGINE.md`  
**Asset type:** MTH  
**Source format:** SECTION_STRUCTURED  
**Index source:** (none)  
**Notes:** Single file contains all methodology definitions. Section boundaries identified by `## ` headings with methodology names.

---

### DR-004 — Capability Assets (CAP)

**Trigger:** File path matches pattern `06_Capabilities/**/*.md` AND file is NOT `MASTER_CAPABILITY_INDEX.md`  
**Asset type:** CAP  
**Source format:** YAML_FRONTMATTER  
**Index source:** `06_Capabilities/MASTER_CAPABILITY_INDEX.md`  
**Notes:** Discovery recurses all subdirectories. Files are classified by path prefix. MASTER_CAPABILITY_INDEX.md is explicitly excluded from this rule and handled separately in Phase 3 augmentation.  
**Filename pattern (informational):** `W[wave]S[stream]-[seq]-[product]-[name].md` — not relied upon for classification.

**Secondary classification (MASTER_CAPABILITY_INDEX.md):**  
Path `06_Capabilities/MASTER_CAPABILITY_INDEX.md` → classified as AUGMENTATION_SOURCE, not as a CAP asset. Added to the discovery manifest as a special entry consumed during Phase 3 cross-referencing (§5.1 of KNOWLEDGE_REGISTRY_POPULATION_ENGINE.md).

---

### DR-005 — Assumption Pack Assets (ASP + ASM)

**Trigger:** File path matches pattern `07_Assumption_Packs/**/*.md`  
**Asset type for registration:** ASP (the file itself) + ASM (rows within)  
**Source format:** YAML_FRONTMATTER (for pack header) + SECTION_STRUCTURED (for assumption rows)  
**Index source:** (none)  
**Notes:** Each file produces TWO types of registry entries:
- One ASP entry from the YAML frontmatter at the top of the file
- N ASM entries from the structured assumption rows within the file body

The Extraction Engine handles this dual extraction (REGISTRY_EXTRACTION_ENGINE.md §5 and §6). The discovery manifest registers one entry per pack file with `asset_type = "ASP+ASM"` to signal dual extraction.

---

### DR-006 — Reference Assets (REF)

**Trigger:** File path matches exactly `00_Governance/REFERENCE_MASTER.md`  
**Asset type:** REF  
**Source format:** MARKDOWN_TABLE  
**Index source:** (none)  
**Notes:** The REFERENCE_MASTER is a Markdown file (not .csv as described in older documentation). MarkdownTableAdapter handles it. Each row is one REF asset.

**DISCREPANCY NOTICE:** KNOWLEDGE_REGISTRY_POPULATION_RULES.md assumes `REFERENCE_MASTER.csv`. The actual file at `00_Governance/REFERENCE_MASTER.md` is a Markdown file. Rule DR-006 corrects this. The population rules document should be updated at next revision. **Technical Debt: TD-014.**

---

### DR-007 — Enterprise Risk Assets (RSK)

**Trigger:** File path matches exactly `08_Commercial/Risk_Library/ENTERPRISE_RISK_REGISTER_V1.md`  
**Asset type:** RSK  
**Source format:** SECTION_STRUCTURED  
**Index source:** (none)  
**Notes:** Single file contains all 40 RSK entries. SectionStructuredAdapter splits by risk ID headings. Each section produces one RSK entry.

**Version detection:** The file name includes version (V1). When a V2 is published, the registry must be updated to point to the new file. File naming convention: `ENTERPRISE_RISK_REGISTER_V[N].md`. The discovery rule targets the latest version — defined in KRPE configuration, not hardcoded in the discovery rule.

---

### DR-008 — Consultant Assets (CON)

**Trigger:** File path matches pattern `09_Consultants/**/*.md` AND file has YAML frontmatter with `asset_type: CON`  
**Asset type:** CON  
**Source format:** YAML_FRONTMATTER  
**Index source:** (none)  
**Notes:** CON assets currently DEFERRED — `09_Consultants/` directory does not yet exist. Discovery rule is defined but no entries are expected. The engine logs a discovery note when no CON files are found.  
**Technical Debt: TD-ADR-001 — CV content from APPTime only; no AI-generated CV text.**

---

### DR-009 — Compliance Assets (COM)

**Trigger:** File path matches pattern `00_Governance/**/*.md` AND file has YAML frontmatter with `asset_type: COM`  
**Asset type:** COM  
**Source format:** YAML_FRONTMATTER  
**Index source:** (none)  
**Notes:** COM assets DEFERRED — no COM files currently exist. Rule defined for future population.

---

### DR-010 — Project Plan Template Assets (PPT) and Proposal Template Assets (PRT)

**Trigger PPT:** File path matches pattern `10_Templates/Project_Plans/**/*.md` AND YAML frontmatter has `asset_type: PPT`  
**Trigger PRT:** File path matches pattern `10_Templates/Proposal_Templates/**/*.md` AND YAML frontmatter has `asset_type: PRT`  
**Source format:** YAML_FRONTMATTER  
**Notes:** Both PPT and PRT DEFERRED — template directories not yet created.

---

## 5. Exclusion Rules

Files matching any exclusion rule are completely skipped. Exclusions take priority over classification rules.

| Rule | Path Pattern | Reason |
|---|---|---|
| EX-001 | `.claude/**` | Platform metadata — not knowledge assets |
| EX-002 | `00_Governance/Archive/**` | Archived governance documents — not active assets |
| EX-003 | `00_Governance/Knowledge_Standards/**` | Governance standard documents — they govern the registry, they are not assets in it |
| EX-004 | `00_Governance/Knowledge_Standards/KNOWLEDGE_ASSET_REGISTRY.yaml` | Registry output file — not a source |
| EX-005 | `08_Commercial/Reports/**` | Completion reports — not knowledge assets |
| EX-006 | `08_Commercial/Assembly_Engine/KNOWLEDGE_VALIDATION_ENGINE.md` | Engine architecture document — not an asset |
| EX-007 | `08_Commercial/Assembly_Engine/VALIDATION_RULE_EXECUTION_MODEL.md` | Engine architecture document — not an asset |
| EX-008 | `08_Commercial/Assembly_Engine/KNOWLEDGE_VALIDATION_REPORT_STANDARD.md` | Engine architecture document — not an asset |
| EX-009 | `08_Commercial/Assembly_Engine/KNOWLEDGE_HEALTH_SCORE.md` | Engine architecture document — not an asset |
| EX-010 | `08_Commercial/Assembly_Engine/KNOWLEDGE_REGISTRY_POPULATION_ENGINE.md` | Engine architecture document — not an asset |
| EX-011 | `08_Commercial/Assembly_Engine/REGISTRY_DISCOVERY_ENGINE.md` | This document — not an asset |
| EX-012 | `08_Commercial/Assembly_Engine/REGISTRY_EXTRACTION_ENGINE.md` | Engine architecture document — not an asset |
| EX-013 | `08_Commercial/Assembly_Engine/REGISTRY_INDEX_ENGINE.md` | Engine architecture document — not an asset |
| EX-014 | `08_Commercial/Assembly_Engine/REGISTRY_OUTPUT_SPECIFICATION.md` | Engine architecture document — not an asset |
| EX-015 | `08_Commercial/Assembly_Engine/REGISTRY_INCREMENTAL_BUILD_MODEL.md` | Engine architecture document — not an asset |
| EX-016 | `HANDOVER.md` | Administrative file |
| EX-017 | `AI_CONTEXT.md` | Administrative file |
| EX-018 | `WP18Z_SESSION_BASELINE.md` | Administrative file |
| EX-019 | `BUILD_MANIFEST.yaml` | Internal KRPE state file |
| EX-020 | `.krpe_cache/**` | KRPE incremental build cache |

**EX-003 clarification:** Files in `00_Governance/Knowledge_Standards/` include the governance standard documents (KNOWLEDGE_ASSET_STANDARD.md, KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md, etc.). These are authoritative reference documents consumed by the KRPE configuration phase, not assets managed by the registry. They are excluded from discovery.

---

## 6. Archive Handling

An asset with `lifecycle_status: ARCHIVED` in its YAML frontmatter remains excluded from the registry by default (KRPE config: `include_archived_assets: false`).

When `include_archived_assets: true` (non-default):
- ARCHIVED assets are extracted and registered
- Their `lifecycle_status` field is preserved as `ARCHIVED`
- KVE rules treat ARCHIVED assets as invisible to assembly

Assets in `00_Governance/Archive/` are excluded regardless of `include_archived_assets` — those are archived governance documents, not archived knowledge assets.

---

## 7. Duplicate Detection

Discovery logs an error if two distinct file paths yield the same `asset_id` during extraction Phase 2. The discovery engine itself cannot detect this (asset IDs are inside files, not determinable from paths), but it feeds into the extraction phase duplicate check:

- **Extractor rule:** If `asset_id` already exists in `core_registry`, log `EXTRACTION_ERROR: DUPLICATE_ID`
- The first file encountered in alphabetical traversal order wins
- The second file is skipped
- Both paths are reported in REGISTRY_BUILD_REPORT.yaml under `duplicate_id_conflicts`

---

## 8. Discovery Execution Algorithm

```
FUNCTION discover_assets(repo_root, config):
  asset_manifest = []
  discovery_errors = []

  # Apply fixed-file rules first (DR-001 through DR-003, DR-006, DR-007)
  FOR rule IN [DR-001, DR-002, DR-003, DR-006, DR-007]:
    target_path = join(repo_root, rule.fixed_path)
    IF file_exists(target_path):
      asset_manifest.append(build_entry(target_path, rule))
    ELSE:
      discovery_errors.append({rule: rule.id, path: target_path, error: "FILE_NOT_FOUND"})

  # Walk directories for pattern-matched rules (DR-004, DR-005, DR-008–DR-010)
  FOR dirpath, dirs, files IN os.walk(repo_root, topdown=True):
    # Prune excluded directories in-place (prevents recursion into them)
    dirs[:] = [d FOR d IN dirs IF NOT matches_exclusion(join(dirpath, d), config.exclusion_paths)]

    FOR filename IN sorted(files):  # alphabetical for determinism
      full_path = join(dirpath, filename)
      rel_path = relative(repo_root, full_path)

      IF matches_exclusion(rel_path, config.exclusion_paths):
        CONTINUE

      IF NOT filename.endswith(".md") AND NOT filename.endswith(".yaml"):
        CONTINUE

      matched_rule = classify_file(rel_path)
      IF matched_rule IS NOT None:
        asset_manifest.append(build_entry(rel_path, matched_rule))

  # Sort manifest by dependency extraction order
  asset_manifest.sort(key=lambda e: EXTRACTION_ORDER[e.asset_type])

  RETURN asset_manifest, discovery_errors
```

**`EXTRACTION_ORDER` map:**  
PAT=1, SEC=2, MTH=3, REF=4, ASP=5, ASM=6, CAP=7, RSK=8, CON=99, COM=99, PPT=99, PRT=99

---

## 9. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-27 | WP18E | Initial specification — 10 discovery rules; 20 exclusion rules; archive handling; duplicate detection; traversal algorithm |
