---
document_id: WP18E-COMPLETION-REPORT-V1
title: "WP18E — Knowledge Registry Population Engine Architecture — Completion Report"
version: "1.0"
status: "APPROVED"
created: "2026-06-27"
created_by: "WP18E — Knowledge Registry Population Engine Architecture"
approved_by: "Architecture — WP18E"
approved_date: "2026-06-27"
work_package: "WP18E"
category: "Completion Report"
---

# WP18E — Knowledge Registry Population Engine Architecture
# Completion Report

**Date:** 2026-06-27  
**Status:** COMPLETE — All 7 deliverables produced. Implementation deferred to dedicated implementation work package.  
**Platform Maturity:** L3.5 (unchanged; requires registry population and KVE implementation for L4.0)

---

## 1. Summary

WP18E designed the complete architecture for the Knowledge Registry Population Engine (KRPE) — the first executable component of the APPSolve Proposal Factory. The KRPE converts the governed Markdown repository into the five machine-readable registry files consumed by every downstream platform component.

This work package is architecture only. No registry entries were created. No existing assets were modified. The KRPE is fully specified and ready for implementation.

---

## 2. Deliverables Produced

| # | Document | Location | Purpose |
|---|---|---|---|
| 1 | KNOWLEDGE_REGISTRY_POPULATION_ENGINE.md | 08_Commercial/Assembly_Engine/ | Engine architecture, execution model, 7 components, 3 source formats, determinism guarantees |
| 2 | REGISTRY_DISCOVERY_ENGINE.md | 08_Commercial/Assembly_Engine/ | Repository traversal algorithm, 10 discovery rules, 20 exclusion rules, duplicate detection |
| 3 | REGISTRY_EXTRACTION_ENGINE.md | 08_Commercial/Assembly_Engine/ | 3 adapters, per-asset extractors (CAP/RSK/ASP/ASM/PAT/SEC/MTH/REF), 10 relationship resolution rules |
| 4 | REGISTRY_INDEX_ENGINE.md | 08_Commercial/Assembly_Engine/ | 20 named lookup indexes, 3-pass derivation algorithm, YAML schemas |
| 5 | REGISTRY_OUTPUT_SPECIFICATION.md | 08_Commercial/Assembly_Engine/ | Complete schemas for all 5 YAML output files; serialisation rules; retention policy |
| 6 | REGISTRY_INCREMENTAL_BUILD_MODEL.md | 08_Commercial/Assembly_Engine/ | 3 build modes, incremental algorithm, two-factor change detection, dependency rebuild, cache strategy |
| 7 | WP18E_POPULATION_ENGINE_ARCHITECTURE.md | 08_Commercial/Reports/ | This document |

---

## 3. Architecture Decisions

### AD-001 — Three Source Format Strategy

**Decision:** The KRPE uses three adapters for three distinct source formats: YAMLFrontmatterAdapter (individual CAP, ASP files), MarkdownTableAdapter (MASTER_CAPABILITY_INDEX.md, REFERENCE_MASTER.md), SectionStructuredAdapter (RSK, PAT, SEC, MTH multi-entry documents).

**Rationale:** The repository uses three genuinely different formats because each evolved from a different governance process. A single universal parser would be more fragile and harder to maintain than three clean, specific adapters. Adapter-per-format makes extraction rules explicit and testable.

---

### AD-002 — CAP Dual-Source Extraction (File Frontmatter + Index Table)

**Decision:** CAP assets are extracted in two phases: primary YAML frontmatter from individual files (governance state, version, approval), then augmented by MASTER_CAPABILITY_INDEX.md (evidence tier, governance restrictions, reference clients). File-level frontmatter takes precedence on conflict.

**Rationale:** The file is the authoritative governance record. The index is a management view. The two sources are complementary, not competing. Merging both gives the richest registry entry.

---

### AD-003 — REFERENCE_MASTER Correction

**Decision:** DR-006 classifies `00_Governance/REFERENCE_MASTER.md` as Format B (MarkdownTableAdapter). Previous population rules assumed a .csv file.

**Rationale:** Actual file at `00_Governance/REFERENCE_MASTER.md` is a Markdown file. The extraction engine corrects for this discrepancy. Technical Debt TD-014 filed to update KNOWLEDGE_REGISTRY_POPULATION_RULES.md.

---

### AD-004 — Non-Halting Extraction

**Decision:** The KRPE never halts on a per-asset extraction error. All errors are collected and surfaced in REGISTRY_BUILD_REPORT.yaml. Only a fatal system error (unwritable output directory) halts the engine.

**Rationale:** A single corrupt file should not prevent the rest of the repository from being registered. The BU Lead can investigate and fix the error from the build report, then trigger an incremental rebuild.

---

### AD-005 — Incremental Build with Full Relationship Rebuild

**Decision:** Incremental mode re-extracts only changed files, but always rebuilds the relationship graph and indexes in full.

**Rationale:** Partial relationship graph updates are error-prone. The full relationship rebuild costs ~1s — acceptable overhead. This keeps the incremental algorithm simple and correct.

---

### AD-006 — Deleted Asset Archiving (Not Deletion)

**Decision:** When a source file is deleted, its registry entries are marked `lifecycle_status: ARCHIVED`, not removed from the registry.

**Rationale:** The registry is the governance record. Removing an asset from the registry destroys the audit trail. ARCHIVED status is visible, auditable, and reversible. KVE rules exclude ARCHIVED assets from assembly manifests.

---

### AD-007 — Extraction Dependency Order

**Decision:** Assets are extracted in dependency order: PAT → SEC → MTH → REF → ASP → ASM → CAP → RSK.

**Rationale:** Parent records must exist before child relationships are resolved. The dependency order ensures that when relationship linking runs in Phase 4, all potential target IDs are already in the registry. Extracting out of order would produce false "unresolved relationship" warnings.

---

## 4. Key Technical Discoveries

### 4.1 REFERENCE_MASTER Format Discrepancy

Previous architecture documents (KNOWLEDGE_REGISTRY_POPULATION_RULES.md) assumed `REFERENCE_MASTER.csv`. The actual file is `00_Governance/REFERENCE_MASTER.md`. Discovery Rule DR-006 corrects this. TD-014 filed.

### 4.2 CAP File Structure Confirmed

Individual capability files use YAML frontmatter with fields: `document_id, title, version, status, approved_for_reuse, business_unit, wave, deliverable, created, approved, created_by, approved_by, source_document, source_status, prereq_statement, kb_destination, tags`. All fields are extractable via YAMLFrontmatterAdapter.

### 4.3 MASTER_CAPABILITY_INDEX.md Column Set

11 columns confirmed: `Cap ID | Capability Name | Product Area | Approved Document | Tier 1 Evidence | Named Reference | Reference Client | Industry | Evidence Tier | Governance Restrictions | Last Review`. All columns mapped to registry fields in REGISTRY_EXTRACTION_ENGINE.md §3.

### 4.4 CAP Files in Nested Subdirectories

Capability files are in `06_Capabilities/[Platform]/[ProductArea]/[filename].md`. Discovery must recurse all subdirectories. Exclusion of `MASTER_CAPABILITY_INDEX.md` is explicit (not discovered by pattern match alone).

### 4.5 Two-Tier ASM Strategy Confirmed

Each assumption pack file produces one ASP entry (from frontmatter) and N ASM entries (from body). ASM entries go to the separate KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml. The Index Engine's `pack_to_assumptions` index provides fast ASP→ASM lookup.

---

## 5. Engine Execution Model Summary

```
KRPE Full Build (8 phases):

Phase 0: Load configuration + schema
Phase 1: Discovery (10 rules → asset_manifest)
Phase 2: Extraction (dependency-ordered, per-type extractors)
Phase 3: CAP augmentation (MASTER_CAPABILITY_INDEX.md cross-reference)
Phase 4: Relationship linking (10 REL rules → relationship_graph)
Phase 5: Index building (20 named indexes → lookup_index)
Phase 6: Registry writing (5 YAML output files — atomic write)
Phase 7: Build report (REGISTRY_BUILD_REPORT.yaml)

Estimated runtime: 30–60 seconds full build
Estimated runtime: 5–15 seconds incremental (1-3 files changed)
```

---

## 6. Expected Output Volume

| Output File | Expected Entries | Estimated Size |
|---|---|---|
| KNOWLEDGE_ASSET_REGISTRY.yaml | 189 core entries | ~400 KB |
| KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml | 1,136 ASM entries | ~2.5 MB |
| KNOWLEDGE_RELATIONSHIP_GRAPH.yaml | ~1,500–2,000 relationships | ~300 KB |
| KNOWLEDGE_LOOKUP_INDEX.yaml | 20 indexes | ~200 KB |
| REGISTRY_BUILD_REPORT.yaml | 1 report | ~50 KB |

---

## 7. Implementation Roadmap

### Phase A — Core Build (~15–20 hours)

1. Implement YAMLFrontmatterAdapter, MarkdownTableAdapter, SectionStructuredAdapter
2. Implement Discovery Engine (10 rules + traversal algorithm)
3. Implement CAP Extractor (dual-source) + ASP/ASM Extractor
4. Write KNOWLEDGE_ASSET_REGISTRY.yaml and KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml
5. Produce first REGISTRY_BUILD_REPORT.yaml

**Gate:** All 49 CAP + 13 ASP + 1,136 ASM extracted and written.

### Phase B — Full Extraction (~8–12 hours)

1. Implement RSK, PAT, SEC, MTH, REF extractors
2. Implement 10 relationship resolution rules
3. Write KNOWLEDGE_RELATIONSHIP_GRAPH.yaml
4. Implement 20 indexes (REGISTRY_INDEX_ENGINE.md)
5. Write KNOWLEDGE_LOOKUP_INDEX.yaml

**Gate:** All 5 output files produced with complete entries. KVE can run.

### Phase C — Incremental Build (~5–8 hours)

1. Implement BUILD_MANIFEST write/read
2. Implement two-factor change detection (mtime + SHA-256)
3. Implement dependency rebuild graph
4. Implement deleted asset archiving
5. Implement DRY_RUN mode

**Gate:** INCREMENTAL mode produces output byte-for-byte identical to FULL build on same repository state.

**Total implementation effort: ~28–40 hours**

---

## 8. Implementation Readiness

| Component | Spec Status | Dependency | Ready to Implement? |
|---|---|---|---|
| YAMLFrontmatterAdapter | Complete | None | YES |
| MarkdownTableAdapter | Complete | None | YES |
| SectionStructuredAdapter | Complete | None | YES |
| Discovery Engine | Complete | None | YES |
| CAP Extractor | Complete | Adapters | YES — after adapters |
| ASP/ASM Extractor | Complete | Adapters | YES — after adapters |
| RSK/PAT/SEC/MTH/REF Extractors | Complete | Adapters | YES — after adapters |
| Relationship Linker | Complete | All extractors complete | YES — after Phase B |
| Index Engine | Complete | Relationship graph | YES — after linker |
| Registry Writer | Complete | REGISTRY_OUTPUT_SPECIFICATION.md | YES |
| Incremental Build Manager | Complete | Phase A + B | YES — Phase C |
| BUILD_MANIFEST | Complete | Phase A + B | YES — Phase C |

---

## 9. Technical Debt

| TD ID | Issue | Owner | Priority |
|---|---|---|---|
| TD-014 | KNOWLEDGE_REGISTRY_POPULATION_RULES.md assumes REFERENCE_MASTER.csv; actual file is .md | Architecture | Medium — update population rules doc at next revision |
| TD-015 | First build has no previous relationship graph for dependency lookup | KRPE Implementation | Low — first run is always FULL; acceptable by design |
| TD-016 | Relationship graph rebuilt fully on every incremental run (~1s overhead) | KRPE Implementation | Low — acceptable at current repo size; revisit at 500+ assets |
| TD-017 | mtime granularity edge case (two files saved in same second) | KRPE Implementation | Low — mitigated by SHA-256 second factor |
| TD-018 | No concurrent build protection (parallel runs can conflict) | KRPE Implementation | Medium — implement file lock on BUILD_MANIFEST in Phase C |

---

## 10. Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| MASTER_CAPABILITY_INDEX.md column changes | Low | Medium | Adapter is column-name-keyed; rename detection needed in Phase A |
| ASP pack body format inconsistency across 13 packs | Medium | Medium | SectionStructuredAdapter falls back to table-row format; format is logged in build report |
| ENTERPRISE_RISK_REGISTER restructured at V2 | Low | High | Discovery rule is configurable (version-parameterised filename) |
| Relationship graph misses declared relationships in non-standard formats | Medium | Low | Unresolved relationships are surfaced in build report and caught by KVE CLV rules |

---

## 11. Future Enhancements

| Enhancement | Benefit | Trigger |
|---|---|---|
| KRPE REST API | External tools can trigger rebuilds and query registry state | When platform has web-accessible deployment |
| Real-time file watcher | Sub-second incremental builds on file save | When repository is on a local development machine |
| Registry diff viewer | BU Lead can see exactly what changed between builds | When registry population is in regular use |
| Asset schema validation during extraction | Pre-KVE field validation with rich error messages | Phase C implementation |
| Multi-repo support | Support for capability libraries from multiple repositories | Future platform expansion |

---

## 12. Recommendations for Implementation Work Package

1. **Implement Phase A first** and validate output against KNOWLEDGE_ASSET_REGISTRY.yaml schema before proceeding to Phase B. A build report with 49 CAP entries is an early, verifiable gate.

2. **Test YAMLFrontmatterAdapter against all 49 CAP files** before implementing other extractors. Field name variations across waves and streams may require per-field default handling.

3. **Run KVE against the Phase A registry immediately** after Phase A completes. KVE will report what is missing. This creates a tight feedback loop.

4. **Prioritise RSK extractor** in Phase B — 40 DRAFT risks are currently the largest governance blocker (TD-001, LV-RSK-008 BLOCK). The sooner RSK entries are in the registry, the sooner WP18B-EXT.2 (governance session) can resolve them.

5. **Do not implement incremental build (Phase C) until Phase B is fully verified** via a complete KVE run. Incremental mode must be validated against full-build output before it is trusted.

---

## 13. Next Work Packages

| ID | Description | Dependency |
|---|---|---|
| WP18B-EXT.2 | BU Lead governance session — approve / classify 40 RSK assets | BU Lead availability (~2h 10min); does not require KRPE implementation |
| KRPE Implementation Phase A | Implement core extractors; produce first KNOWLEDGE_ASSET_REGISTRY.yaml | This architecture (WP18E) |
| KRPE Implementation Phase B | Full extraction (RSK/PAT/SEC/MTH/REF); relationship graph; indexes | Phase A |
| KRPE Implementation Phase C | Incremental build mode | Phase B |
| KVE Implementation Phase A | 22 BLOCK rules + manifest builder | Populated registry (Phase B) |
| KVE Implementation Phase B | Full 76 rules + validation reports | Phase A |
| KVE Implementation Phase C | Health Score + Mode 1 Platform Health | Phase B |

---

## 14. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-27 | WP18E | Completion report — 7 deliverables; 7 architecture decisions; 4 key discoveries; implementation roadmap; TD items |
