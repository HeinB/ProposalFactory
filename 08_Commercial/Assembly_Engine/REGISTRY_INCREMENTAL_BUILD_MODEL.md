---
document_id: REGISTRY-INCREMENTAL-BUILD-MODEL-V1
title: "Registry Incremental Build Model — Architecture Specification V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-27"
created_by: "WP18E — Knowledge Registry Population Engine Architecture"
approved_by: "Architecture — WP18E"
approved_date: "2026-06-27"
approved_for_reuse: true
category: "Assembly Engine / Registry"
scope: "Defines the first-build process, incremental rebuild algorithm, change detection strategy, deleted asset handling, dependency rebuild tracking, cache strategy, and rebuild triggers for the KRPE."
related_documents:
  - KNOWLEDGE_REGISTRY_POPULATION_ENGINE.md
  - REGISTRY_DISCOVERY_ENGINE.md
  - REGISTRY_OUTPUT_SPECIFICATION.md
---

# Registry Incremental Build Model — Architecture Specification V1.0

**Work Package:** WP18E  
**Status:** APPROVED — Architecture specification complete.

---

## 1. Purpose

The Incremental Build Model defines how the KRPE avoids full extraction on every run. After the first build, subsequent runs detect which source files have changed and re-extract only those files and their dependents.

**Why this matters:** The repository will grow. With 49 CAP files, 13 ASP packs (1,136 ASM), 40 RSK, and multi-entry documents, a full rebuild costs meaningful time (~45s). For frequent rebuilds triggered by CI or pre-proposal validation, incremental mode reduces this to under 5s for single-file changes.

**Design constraint:** Incremental mode must produce output files byte-for-byte identical to a full build given the same repository state. Incremental is a performance optimisation, not a different algorithm.

---

## 2. Build Modes

| Mode | Trigger | Behaviour |
|---|---|---|
| FULL | First run, forced rebuild, schema version change, configuration change | Re-extracts everything. Overwrites all output files. |
| INCREMENTAL | Subsequent runs on unchanged schema | Detects changes; re-extracts only changed files and their dependents. |
| DRY_RUN | Audit / validation run | Full discovery + extraction but writes no output files. Produces DRY_RUN_REPORT only. |

**Fallback to FULL:** INCREMENTAL mode automatically falls back to FULL build when:
- BUILD_MANIFEST.yaml does not exist (first run or state lost)
- `population_rules_version` in BUILD_MANIFEST differs from current version
- `schema_version` in BUILD_MANIFEST differs from current version
- KRPE configuration has changed (detected by hashing krpe_config)
- BUILD_MANIFEST is corrupt or unreadable

---

## 3. First Build

On first run, no BUILD_MANIFEST exists. The KRPE runs a full build per the KNOWLEDGE_REGISTRY_POPULATION_ENGINE.md §5.1 sequence. After writing the 5 output files, it writes:

```
[repo_root]/.krpe_state/BUILD_MANIFEST.yaml
```

The BUILD_MANIFEST records:
- Every scanned file's path, modification time (mtime as Unix epoch), and SHA-256 hash
- Which asset IDs were extracted from each file
- The build ID, KRPE version, schema version, and population rules version

This file is the "known good" baseline for all subsequent incremental builds.

---

## 4. Incremental Build Algorithm

```
FUNCTION incremental_build(repo_root, config):

  # Step 1: Load previous state
  manifest = load(BUILD_MANIFEST.yaml)
  old_registry = load(KNOWLEDGE_ASSET_REGISTRY.yaml)
  old_assumptions = load(KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml)
  old_relationship_graph = load(KNOWLEDGE_RELATIONSHIP_GRAPH.yaml)

  # Step 2: Discover current repository state
  current_files = discover_all_files(repo_root, config.exclusion_paths)

  # Step 3: Classify file changes
  added_files   = [f FOR f IN current_files IF f NOT IN manifest.files]
  deleted_files = [f FOR f IN manifest.files IF f NOT IN current_files]
  changed_files = [f FOR f IN current_files
                   IF f IN manifest.files
                   AND (mtime(f) != manifest.files[f].mtime
                        OR sha256(f) != manifest.files[f].sha256)]
  unchanged_files = current_files - added_files - changed_files

  # Step 4: Build dependency graph for re-extraction
  affected_asset_ids = set()
  FOR f IN added_files + changed_files:
    affected_asset_ids.update(classify_and_extract(f))

  # Also include assets that REFERENCE any affected asset (dependency rebuild)
  FOR asset_id IN copy(affected_asset_ids):
    referencing_assets = reverse_dependency_lookup(asset_id, old_relationship_graph)
    affected_asset_ids.update(referencing_assets)

  # Step 5: Handle deleted files
  removed_asset_ids = set()
  FOR f IN deleted_files:
    removed_asset_ids.update(manifest.files[f].asset_ids_extracted)
    # Log: "Asset [id] source file deleted — marking ARCHIVED"
    FOR asset_id IN manifest.files[f].asset_ids_extracted:
      mark_archived(asset_id, old_registry, old_assumptions)

  # Step 6: Rebuild affected entries
  fresh_entries = extract_all(added_files + changed_files)

  # Step 7: Merge
  merged_registry = old_registry.copy()
  merged_assumptions = old_assumptions.copy()
  FOR entry IN fresh_entries:
    IF entry.asset_type == "ASM":
      merged_assumptions[entry.asset_id] = entry
    ELSE:
      merged_registry[entry.asset_id] = entry
  FOR asset_id IN removed_asset_ids:
    update_lifecycle_status(asset_id, "ARCHIVED", merged_registry, merged_assumptions)

  # Step 8: Rebuild relationship graph and indexes
  # Always rebuild full relationship graph and indexes — these are cheap to derive
  # and partial rebuild would risk consistency errors
  relationship_graph = resolve_relationships(merged_registry, merged_assumptions)
  lookup_index = build_indexes(merged_registry, merged_assumptions, relationship_graph)

  # Step 9: Write output files (same atomic write protocol as full build)
  write_all_output_files(merged_registry, merged_assumptions, relationship_graph, lookup_index)

  # Step 10: Update BUILD_MANIFEST
  update_manifest(current_files, fresh_entries, removed_asset_ids)

  # Step 11: Generate build report
  generate_build_report(build_mode="INCREMENTAL", added=added_files, changed=changed_files, deleted=deleted_files)
```

---

## 5. Change Detection

### 5.1 Detection Method — Two-Factor

The KRPE uses **two factors** to detect file changes:

1. **mtime (modification time):** Fast — O(1) filesystem stat. Used as the primary signal. If mtime is unchanged, the file is treated as unchanged.
2. **SHA-256 hash:** Authoritative — computed only when mtime has changed (to guard against mtime clock skew or OS-level mtime manipulation). If mtime changed but hash is identical, the file is treated as unchanged (e.g., file was touched but not modified).

This two-factor approach avoids both false-negative (missing real changes) and false-positive (unnecessary re-extraction) errors.

### 5.2 Multi-Entry Files

Files like `ENTERPRISE_RISK_REGISTER_V1.md` (40 RSK entries) and `07_Assumption_Packs/*.md` (1 ASP + N ASM entries) produce multiple registry entries from a single source file.

When a multi-entry file changes:
- ALL entries previously extracted from that file are invalidated
- The entire file is re-extracted
- The new set of entries replaces the old set in the merged registry

This is simpler and safer than attempting line-level diff of multi-entry files.

---

## 6. Deleted Asset Handling

When a source file is deleted from the repository:

1. The asset IDs previously extracted from that file are identified from BUILD_MANIFEST
2. Each identified asset is updated: `lifecycle_status: "ARCHIVED"`
3. The `registry_last_synced` field is updated to the current build timestamp
4. A note is added to `governance_notes`: `"Source file deleted [date]. Asset auto-archived by KRPE."`
5. The asset remains in the registry (not removed) — ARCHIVED assets are retained for governance history
6. REGISTRY_BUILD_REPORT.yaml records the deletion under `incremental_changes.removed`

**Rationale for retaining ARCHIVED assets:** The registry is the governance record. Deleting an asset from the registry obscures the fact that it ever existed. ARCHIVED status is visible, auditable, and reversible. KVE rules explicitly exclude ARCHIVED assets from assembly manifests.

---

## 7. Dependency Rebuild

When asset X changes, any asset that references X must be re-extracted and re-linked, because its resolved relationship set has changed.

**Dependency graph:** Built from KNOWLEDGE_RELATIONSHIP_GRAPH.yaml (the previous build's relationship graph). This is the "reverse dependency index" — for each asset, which other assets reference it.

**Reverse dependency lookup pseudocode:**
```
FUNCTION reverse_dependency_lookup(changed_asset_id, relationship_graph):
  dependents = set()
  FOR rel IN relationship_graph:
    IF rel.target_id == changed_asset_id:
      dependents.add(rel.source_id)
  RETURN dependents
```

**Practical scope:** In the current repository:
- Changing one CAP file → re-extract that CAP; re-link SEC entries that source from it; re-link PAT entries that include those sections
- Changing ENTERPRISE_RISK_REGISTER_V1.md → re-extract all 40 RSK; re-link related ASM; re-link patterns that apply those risks
- Changing PROPOSAL_PATTERN_ENGINE.md → re-extract all 13 PAT; re-link all SEC and MTH entries referencing patterns

**Relationship rebuild is always FULL:** After step 4 of the incremental algorithm, the relationship graph and indexes are always rebuilt in full (not incrementally). The relationship graph is fast to rebuild (~1s) and partial relationship updates are too error-prone.

---

## 8. Cache Strategy

### 8.1 Parsed Frontmatter Cache

The KRPE maintains a session-level (in-memory) cache of parsed YAML frontmatter:

```
cache: Dict[file_path + ":" + mtime, parsed_yaml_dict]
```

This avoids parsing the same file twice during a single build run (e.g., if a file is re-scanned during dependency resolution).

**Cache scope:** In-memory only. The cache does not persist between build runs (BUILD_MANIFEST handles that function).

### 8.2 No Persistent Parsed Cache

Persisting parsed YAML across runs is not implemented. The cost of re-parsing changed files is low. The risk of cache invalidation bugs is not worth the marginal performance gain. BUILD_MANIFEST file-level change detection is sufficient.

### 8.3 Schema and Rules Cache

The KRPE configuration files (KNOWLEDGE_REGISTRY_POPULATION_RULES.md, KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md) are loaded once at Phase 0 and cached in memory for the build duration. They are not re-loaded mid-build.

---

## 9. Rebuild Triggers

The KRPE may be triggered by:

| Trigger | Mode | Notes |
|---|---|---|
| Manual invocation | FULL or INCREMENTAL (per config) | BU Lead runs KRPE to update registry |
| Pre-proposal validation | INCREMENTAL preferred | TIL triggers KRPE before generating tender_context.yaml |
| CI/CD hook on file commit | INCREMENTAL | Triggered on any commit to `06_Capabilities/`, `07_Assumption_Packs/`, `08_Commercial/Risk_Library/` |
| Schema version change | FULL (forced) | Detected automatically from BUILD_MANIFEST schema_version field |
| Governance state change | INCREMENTAL | When a BU Lead approves an asset, only that file changes |
| Scheduled (weekly) | FULL | Full rebuild ensures no drift from accumulated incremental builds |

**Recommended trigger cadence:**
- On any file save in the repository: INCREMENTAL (real-time sync)
- Once per week: FULL (drift protection)
- Before any proposal generation run: INCREMENTAL (fast freshness check)

---

## 10. Technical Debt

| TD ID | Issue | Impact | Resolution |
|---|---|---|---|
| TD-015 | First-build has no previous graph for dependency lookup | Incremental not possible before first full build | Acceptable — first run is always FULL |
| TD-016 | Relationship graph rebuilt FULL on every incremental | ~1s overhead per incremental run | Acceptable for current repo size; revisit at 500+ assets |
| TD-017 | mtime granularity on some filesystems is 1-second | Two files saved in same second may not both trigger re-extraction | Mitigated by SHA-256 second factor |
| TD-018 | No concurrent build protection | Two parallel KRPE runs can write conflicting output files | Implement file lock on BUILD_MANIFEST in implementation phase |

---

## 11. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-27 | WP18E | Initial specification — 3 build modes; full incremental algorithm; two-factor change detection; deleted asset handling; dependency rebuild; cache strategy; rebuild triggers |
