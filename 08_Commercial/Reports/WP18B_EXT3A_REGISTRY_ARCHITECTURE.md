---
document_id: WP18B-EXT3A-REGISTRY-ARCHITECTURE-REPORT
title: "WP18B-EXT.3A — Universal Knowledge Asset Registry: Architecture Report"
version: "1.0"
status: "COMPLETE"
created: "2026-06-27"
created_by: "WP18B-EXT.3A — Universal Knowledge Asset Registry"
approved_by: "Architecture — WP18B-EXT.3A"
approved_date: "2026-06-27"
work_package: WP18B-EXT.3A
---

# WP18B-EXT.3A — Universal Knowledge Asset Registry: Architecture Report

**Date:** 2026-06-27  
**Status:** COMPLETE  
**Platform Maturity Impact:** L3.5 → L4.0 (post-WP18D implementation)

---

## 1. Executive Summary

WP18B-EXT.3A designed the Universal Knowledge Asset Registry — a machine-readable metadata catalogue that sits between the Knowledge Libraries and the Proposal Assembly / Validation engines. The Registry is the key structural component needed to make WP18D (Knowledge Validation Engine) deterministic: instead of parsing individual library files, WP18D will load a single YAML file and execute 76 rule checks against the structured metadata.

**Four architecture documents and one completion report were delivered:**

| Document | Location | Purpose |
|---|---|---|
| KNOWLEDGE_ASSET_REGISTRY_STANDARD.md | 00_Governance/Knowledge_Standards/ | Purpose, principles, authority, sync rules, relationship to WP18D |
| KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md | 00_Governance/Knowledge_Standards/ | Complete field schema, 12 asset type extensions, 4 annotated YAML examples |
| KNOWLEDGE_REGISTRY_POPULATION_RULES.md | 00_Governance/Knowledge_Standards/ | Source-to-registry mapping for all 9 live asset types; population sequence |
| KNOWLEDGE_REGISTRY_VALIDATION_RULES.md | 00_Governance/Knowledge_Standards/ | 76 deterministic validation rules across 11 series; WP18D execution order |
| WP18B_EXT3A_REGISTRY_ARCHITECTURE.md | 08_Commercial/Reports/ | This document |

No existing approved assets were modified. No registry entries were created. This work package delivered architecture and design only, per user constraint.

---

## 2. Architecture Decisions

### 2.1 Registry Is Metadata Only (Not Content)

**Decision:** The Registry stores metadata, relationships, and assembly rules. Asset content (capability narrative, assumption text, risk descriptions) stays in the library files.

**Rationale:** Duplicating content creates synchronisation debt. Engines needing governance state query the Registry; engines needing content read the library file at the path recorded in `source_file`. This separation means the Registry stays small enough to load entirely into memory at assembly time, regardless of how many assets exist.

**Impact:** The Assembly Engine retains its existing file-reading behaviour for content. The Registry replaces the governance-state-checking behaviour (currently done by reading individual library indexes).

### 2.2 YAML Format, Flat Schema

**Decision:** The authoritative registry is a YAML file (`KNOWLEDGE_ASSET_REGISTRY.yaml`). The schema is flat (top-level fields), with typed extension blocks (`cap_ext`, `rsk_ext`, etc.) for asset-type-specific fields.

**Rationale:** YAML is human-readable, version-controlled, and consistent with the platform's existing Markdown-with-YAML-frontmatter conventions. A flat schema makes filtering and querying straightforward without a query engine — a simple YAML parser plus filter expressions is sufficient for WP18D. Extension blocks keep the core schema stable as new asset types are added.

**Impact:** WP18D does not require a database. A Python/Node script that loads the YAML and applies rule expressions is sufficient for the validation engine MVP.

### 2.3 Two-Tier ASM Strategy

**Decision:** Individual Assumptions (ASM — 1,136 entries) are stored in a separate `KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml`. The primary registry file holds the 13 ASP pack-level entries.

**Rationale:** Loading 1,136 assumption entries alongside ~130 other core entries for every assembly run is wasteful when most operations only need pack-level metadata. The separate file is loaded only when assumption-level validation is required (Phase 6 of the WP18D execution order).

**Impact:** The primary registry file stays manageable (~130 core entries across CAP/ASP/RSK/MTH/REF/PAT/SEC). Assumption-level validation is still fully supported, but as a separate load step.

### 2.4 Registry Is the Governance Gate for Engines

**Decision:** The Registry is the authoritative governance source for all assembly engines. If the Registry records `approved_for_reuse = false`, no engine may use that asset in a proposal — regardless of what the library file says.

**Rationale:** Without a single authoritative governance source, engines must individually implement governance checks against potentially inconsistent library files. The Registry enforces consistency: one update to the Registry (on lifecycle advancement) propagates immediately to all engines.

**Impact:** This creates a synchronisation obligation: when a library file's governance state changes, the registry must be updated within the same work package. This is specified in KNOWLEDGE_ASSET_REGISTRY_STANDARD.md §6.

### 2.5 76 Deterministic Validation Rules

**Decision:** All validation logic is specified as discrete, named rules (RI-, AV-, CLV-, LV- series). Each rule has a defined condition, severity, and engine action.

**Rationale:** Named rules can be independently implemented, tested, and reported. A validation report that says "CLV-008 BLOCK: REF-CAS-001 lacks AM clearance" is actionable; a generic "validation failed" is not. Named rules also form a stable API: WP18D can implement rules incrementally and report which rules were evaluated.

**Impact:** WP18D has a complete implementation specification. The 22 BLOCK rules define the minimum viable validation set for the first WP18D release.

### 2.6 PAT and SEC Added as Catalogued Asset Types

**Decision:** Proposal Patterns (PAT) and Proposal Sections (SEC) are added to the Registry as catalogued asset types (P1–P13 and S-1–S-56), even though they are structural assets rather than content assets.

**Rationale:** Without cataloguing patterns and sections, validation rules cannot check that a selected pattern's expected sections are all present, or that a section's referenced source assets are all approved. Cataloguing them closes the validation loop and enables LV-PAT and LV-SEC rules in WP18D.

**Impact:** The population work package must catalogue 13 PAT entries and 56 SEC entries in addition to the content asset types. These are low-effort entries (most fields default or extract from PROPOSAL_PATTERN_ENGINE.md and CONTENT_SOURCE_MATRIX.md).

---

## 3. Asset Coverage at WP18B-EXT.3A

| Asset Type | Count | Registry Priority | Population Source |
|---|---|---|---|
| CAP | 49 | P1 | MASTER_CAPABILITY_INDEX.md + individual files |
| ASP | 13 | P1 | Pack files + ASSUMPTION_LIBRARY_ROADMAP.md |
| ASM | 1,136 | P1 (separate file) | Individual assumption rows in pack files |
| RSK | 40 | P1 | ENTERPRISE_RISK_REGISTER_V1.md |
| MTH | 2 | P2 | METHODOLOGY_SELECTION_ENGINE.md + methodology files |
| REF | 16 | P2 | REFERENCE_MASTER.csv or equivalent |
| PAT | 13 | P1 | PROPOSAL_PATTERN_ENGINE.md |
| SEC | 56 | P2 | CONTENT_SOURCE_MATRIX.md + ASSEMBLY_READINESS_MATRIX.md |
| PPT | 0 | P3 | Not yet created |
| PRT | 0 | P3 | Not yet created |
| **Total (excl. ASM)** | **189** | | |
| **Total (incl. ASM)** | **1,325** | | |

---

## 4. Validation Rule Coverage

| Series | Count | BLOCK Rules | Status |
|---|---|---|---|
| RI- (Registry Integrity) | 15 | 3 | Designed ✓ |
| AV- (Assembly Validation) | 13 | 9 | Designed ✓ |
| CLV- (Cross-Library) | 12 | 5 | Designed ✓ (extends KNOWLEDGE_RELATIONSHIP_MODEL.md CLV-001–012) |
| LV-CAP- | 5 | 0 | Designed ✓ |
| LV-ASP- | 4 | 1 | Designed ✓ |
| LV-ASM- | 5 | 2 | Designed ✓ |
| LV-RSK- | 8 | 2 | Designed ✓ |
| LV-MTH- | 3 | 0 | Designed ✓ |
| LV-REF- | 4 | 1 | Designed ✓ |
| LV-PAT- | 3 | 0 | Designed ✓ |
| LV-SEC- | 4 | 0 | Designed ✓ |
| **Total** | **76** | **22** | |

---

## 5. Implementation Effort Estimate

### 5.1 Population Work Package (Registry Entries)

This is the deferred work: creating the actual KNOWLEDGE_ASSET_REGISTRY.yaml and KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml files by applying the population rules to the existing library data.

| Task | Effort | Notes |
|---|---|---|
| Populate PAT entries (13) | 1h | Mechanical extraction from PROPOSAL_PATTERN_ENGINE.md |
| Populate SEC entries (56) | 2h | Extract from CONTENT_SOURCE_MATRIX.md |
| Populate ASP entries (13) | 1h | Extract from pack frontmatter |
| Populate CAP entries (49) | 3h | Extract from MASTER_CAPABILITY_INDEX.md; some derivation required |
| Populate RSK entries (40) | 2h | Extract from ENTERPRISE_RISK_REGISTER_V1.md — well-structured |
| Populate REF entries (16) | 1h | Extract from REFERENCE_MASTER.csv |
| Populate MTH entries (2) | 30min | Two files only |
| Populate ASM entries (1,136) | 6h | Highest volume; mostly mechanical but large |
| Registry validation run | 2h | Apply RI- rules; resolve violations |
| **Total population effort** | **~18h** | Two AI-assisted work sessions |

Note: ASM population is the largest effort item. Given the structured format of the packs, it can be automated with a script that reads each pack file and generates YAML entries.

### 5.2 WP18D Implementation (Knowledge Validation Engine)

The Registry architecture makes WP18D implementation more focused: the engine reads one YAML file, applies 76 rule expressions, and outputs a structured validation report.

| Component | Effort | Dependency |
|---|---|---|
| Registry YAML loader | 2h | Population work package complete |
| Assembly context builder (tender profile) | 3h | TIL integration |
| Phase 1–4 rule evaluator (RI, AV) | 4h | Registry schema stable |
| Phase 5–6 rule evaluator (CLV, LV) | 6h | Population complete (all assets in registry) |
| Validation report generator | 3h | All rules implemented |
| Assembly manifest finalisation | 2h | Validation report implemented |
| Integration with Assembly Engine | 4h | PACK_LOADER.md and ENGINE_ORCHESTRATOR.md |
| Testing (regression against ARM IT045) | 3h | All components integrated |
| **Total WP18D effort** | **~27h** | |

---

## 6. Migration Impact

### 6.1 No Modification to Existing Assets

Per the governing constraint, no existing approved assets were modified in this work package. All 49 CAP assets, 13 ASP packs, 1,136 ASM assumptions, and 40 RSK entries remain unchanged.

### 6.2 Registry Supersedes Fragmented Governance Checks

Post-population, the following existing behaviours change:

| Current Behaviour | Post-Registry Behaviour |
|---|---|
| Assembly Engine reads MASTER_CAPABILITY_INDEX.md to check approval status | Engine reads Registry YAML; CAP entry has `approved_for_reuse` and `lifecycle_status` directly |
| BOM_RESOLVER.md manually cross-references platform to capabilities | Registry query: filter by `pattern_applicability` and `cap_ext.platform` |
| RULE_PROCESSOR.md evaluates mandatory_if from scattered frontmatter | Registry query: read `assembly_rules.mandatory_if` from CAP/ASM/RSK entries |
| Risk selection requires reading full ENTERPRISE_RISK_REGISTER_V1.md | Registry query: filter by `pattern_applicability` and evaluate `assembly_rules.mandatory_if` |
| REF clearance is checked manually | LV-REF-001 and CLV-008 enforce clearance as a BLOCK rule in WP18D |

### 6.3 No New File-Format Dependencies

The Registry uses YAML, which is already natively supported by the platform's markdown-with-frontmatter conventions. No new parser or runtime dependency is introduced.

---

## 7. Risks and Technical Debt

| Risk / TD | Description | Mitigation |
|---|---|---|
| TD-001 (existing) | Risk Library in DRAFT; 40 RSK entries cannot be set `approved_for_reuse = true` in the registry until WP18B-EXT.2 governance session completes | WP18B-EXT.2 resolves TD-001; registry RSK entries are populated as DRAFT and updated post-approval |
| TD-007 (new) | Population work package is high-effort (~18h) and must complete before WP18D can run live validation | Prioritise CAP/ASP/RSK/PAT population first (P1 assets); SEC/REF/MTH can follow |
| TD-008 (new) | ASM population (1,136 entries) requires scripted extraction or very long AI session; risk of formatting errors | Design and test extraction script before running; validate 10% sample manually |
| TD-009 (new) | Registry sync protocol is manual (no event bus); registry can drift from libraries between sync cycles | Monthly batch sync rule (KNOWLEDGE_ASSET_REGISTRY_STANDARD.md §6.2) reduces drift; WP18D RI-004 flags path violations |
| RISK-A | assembly_rules.mandatory_if expressions use a natural-language-style vocabulary; expressions must be evaluated consistently across engines | Formalise expression evaluator specification in WP18D; document variable vocabulary in RULE_PROCESSOR.md |

---

## 8. Recommendations for WP18D

**Critical path:**

1. Complete the population work package before WP18D implementation begins (the engine cannot run without a populated registry).
2. Complete WP18B-EXT.2 (Risk Library governance session) to unlock RSK entries — without approved risks, LV-RSK-008 will BLOCK all assembly runs that include risk assets.

**Implementation priorities:**

1. Implement the 22 BLOCK rules first — they define the minimum viable validation engine.
2. Add ERROR rules in Phase 2 of WP18D development.
3. WARNING rules are low-risk additions that can follow.

**WP18D scope confirmation:**

WP18D should implement all four components defined in KNOWLEDGE_RELATIONSHIP_MODEL.md §7 and confirmed in KNOWLEDGE_REGISTRY_VALIDATION_RULES.md §7:
1. Registry Loader + Context Builder
2. 76-Rule Validation Engine (phased: BLOCK → ERROR → WARNING)
3. Assembly Manifest Generator
4. Validation Report Generator

**Platform maturity gate:**

Platform maturity L4.0 is defined as: Registry populated + WP18D operational + at least the 22 BLOCK rules passing on a live assembly run. This is achievable in a single WP18D work package once the population work package is complete.

---

## 9. Governance Standard Deliverables Summary

WP18B-EXT.3A produced 4 architecture documents forming a complete design specification:

| Document | Sections | Key Content |
|---|---|---|
| KNOWLEDGE_ASSET_REGISTRY_STANDARD.md | 11 sections | Purpose, 7 principles, file locations, authority, 10 sync rules, versioning, 10 integrity rules, library relationships, WP18D relationship |
| KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md | 11 sections | 2 mandatory field groups (5+4 fields), 15 optional fields, assembly_rules block (6 fields), 10 extension schemas, 4 complete YAML examples, 5 compliance levels |
| KNOWLEDGE_REGISTRY_POPULATION_RULES.md | 11 sections | 9 asset type mapping tables; deterministic source-to-registry notation; 10-step population sequence; batch sync rules; extension protocol |
| KNOWLEDGE_REGISTRY_VALIDATION_RULES.md | 9 sections | 76 rules across 11 series; 22 BLOCK rules; 7-phase WP18D execution order; validation report YAML format |

---

## 10. Constraints Compliance

| Constraint | Status |
|---|---|
| Do NOT modify existing approved assets | COMPLIED — no existing file was modified |
| Do NOT migrate libraries | COMPLIED — no library content was moved or restructured |
| Do NOT create registry entries | COMPLIED — KNOWLEDGE_ASSET_REGISTRY.yaml not created; population deferred |
| Only design the architecture, schema, validation model, and population rules | COMPLIED — 4 design documents only |

---

## 11. Platform Status After WP18B-EXT.3A

| Dimension | Status |
|---|---|
| Platform Maturity | L3.5 (unchanged; L4.0 requires WP18D operational) |
| Registry Standard | COMPLETE ✓ |
| Registry Schema | COMPLETE ✓ |
| Population Rules | COMPLETE ✓ |
| Validation Rules | COMPLETE ✓ |
| Registry Population | DEFERRED (population work package) |
| WP18D Implementation | DEFERRED (post-population) |

---

## 12. Recommended Next Steps

| Priority | Work Package | Action | Effort |
|---|---|---|---|
| 1 | WP18B-EXT.2 | BU Lead governance session — apply decisions from RISK_GOVERNANCE_WORKSHOP_PACK.md to ENTERPRISE_RISK_REGISTER_V1.md; resolves TD-001 | ~2h 10min (BU Lead) |
| 2 | Registry Population | Populate KNOWLEDGE_ASSET_REGISTRY.yaml — PAT, SEC, ASP, CAP, RSK (post-WP18B-EXT.2), REF, MTH; ASM in separate file | ~18h |
| 3 | WP18D | Implement Knowledge Validation Engine against 76 rules in KNOWLEDGE_REGISTRY_VALIDATION_RULES.md | ~27h |
| 4 | WP19 | Rendering Engine (DOCX/PDF/HTML output) — after WP18D | TBD |
