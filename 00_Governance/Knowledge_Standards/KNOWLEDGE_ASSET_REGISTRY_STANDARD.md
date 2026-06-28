---
document_id: KNOWLEDGE-ASSET-REGISTRY-STANDARD-V1
title: "Universal Knowledge Asset Registry Standard — V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-26"
created_by: "WP18B-EXT.3A — Universal Knowledge Asset Registry"
approved_by: "Architecture — WP18B-EXT.3A"
approved_date: "2026-06-26"
approved_for_reuse: true
category: "Governance / Knowledge Standards"
scope: "Defines the purpose, principles, authority, and operating rules for the Universal Knowledge Asset Registry — the single authoritative machine-readable catalogue that sits between the Knowledge Libraries and the Proposal Assembly / Validation engines."
related_documents:
  - KNOWLEDGE_ASSET_STANDARD.md
  - KNOWLEDGE_ASSET_LIFECYCLE.md
  - KNOWLEDGE_METADATA_STANDARD.md
  - KNOWLEDGE_GOVERNANCE_RULES.md
  - KNOWLEDGE_RELATIONSHIP_MODEL.md
  - KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md
  - KNOWLEDGE_REGISTRY_POPULATION_RULES.md
  - KNOWLEDGE_REGISTRY_VALIDATION_RULES.md
---

# Universal Knowledge Asset Registry Standard — V1.0

**Work Package:** WP18B-EXT.3A  
**Status:** APPROVED  
**Authority:** Extends KNOWLEDGE_ASSET_STANDARD.md. The Registry is the operational implementation of the governance standards defined in WP18B-EXT.3.

---

## 1. Purpose

The Universal Knowledge Asset Registry (the Registry) is the single authoritative catalogue of every governed knowledge asset used by the Proposal Factory.

**The Registry is not:**
- Another copy of asset content (assets live in their library files)
- A document inventory or file list
- A replacement for existing library indexes (MASTER_CAPABILITY_INDEX.md, ENTERPRISE_RISK_REGISTER_V1.md, etc.)

**The Registry is:**
- The machine-readable metadata layer that the Assembly Engine and Validation Engine query at runtime
- The authoritative source for: asset lifecycle state, approval status, pattern applicability, assembly rules, and relationship declarations
- The foundation that makes WP18D (Knowledge Validation Engine) deterministic rather than dependent on parsing individual library files at assembly time
- The single place where cross-library relationships are declared and validated

### 1.1 Why the Registry Is Needed

Without the Registry, every engine component (Tender Intelligence Layer, Assembly Engine, QA Engine) must:
1. Parse multiple library files to determine which assets are approved
2. Re-derive pattern applicability from scattered metadata
3. Resolve relationships by searching across separate index files
4. Validate governance state without a single authoritative source

This is slow, error-prone, and does not scale as new libraries are added. The Registry eliminates this by providing a single structured metadata source that all engines query.

### 1.2 Architectural Position

```
Knowledge Libraries (content source)
    │
    │ population (one-way sync — library → registry)
    ▼
KNOWLEDGE ASSET REGISTRY (this system)
    │
    ├──► Tender Intelligence Layer (Stage 0 — asset selection)
    │
    ├──► Assembly Engine (Stages 4–8 — asset retrieval and assembly)
    │
    └──► Knowledge Validation Engine (Stage 9 / WP18D — pre-assembly validation)
```

The Registry is downstream of the libraries and upstream of all engines. It does not push changes back to libraries.

---

## 2. Scope

The Registry catalogues every governed knowledge asset defined in KNOWLEDGE_ASSET_STANDARD.md:

| Asset Type | Code | Count at WP18B-EXT.3A | Registry Priority |
|---|---|---|---|
| Capability Asset | CAP | 49 | P1 — immediate |
| Assumption Pack | ASP | 13 | P1 — immediate |
| Individual Assumption | ASM | 1,136 | P1 — immediate (but see Section 4.3) |
| Enterprise Risk | RSK | 40 | P1 — immediate |
| Methodology | MTH | 2 | P2 — after CAP/ASP/RSK |
| Client Reference | REF | 16 | P2 — after CAP/ASP/RSK |
| Project Plan Template | PPT | 0 | P3 — on creation |
| Proposal Template | PRT | 0 | P3 — on creation |
| Consultant Record | CON | 49 | P3 — limited value in registry |
| Compliance Record | COM | 17 | P3 — limited value in registry |
| Proposal Pattern | PAT | 13 | P1 — immediate (new type) |
| Proposal Section | SEC | 56 | P2 — after patterns |

**Proposal Pattern (PAT)** and **Proposal Section (SEC)** are added to the Registry scope as new catalogued types. They are not content assets but structural assets consumed by the assembly pipeline. Cataloguing them in the Registry enables the Validation Engine to verify that selected patterns and sections are valid and consistent.

---

## 3. Registry Principles

### 3.1 Single Source of Truth for Metadata

The Registry is the definitive source for asset metadata at assembly time. If the Registry says an asset is APPROVED with `approved_for_reuse: Yes`, that is the truth for assembly purposes. If the library file says otherwise, the discrepancy is a synchronisation defect that must be resolved — but the Registry governs the engine.

### 3.2 Content Stays in Libraries

The Registry stores metadata and relationship declarations only. Asset content (capability narrative text, assumption text, risk descriptions, mitigation guidance) stays in the library files. Engines that need content read the library file; engines that need governance state read the Registry.

### 3.3 Libraries Are the Write Origin

All changes to asset data originate in the library files. The Registry is populated and updated by reading library files (one-way flow: library → registry). The Registry does not write back to libraries.

### 3.4 Registry Is Append-Then-Supersede

Registry entries are never deleted. When an asset is superseded, its registry entry is updated to `lifecycle_status: SUPERSEDED` and `superseded_by: [new_id]` is set. When an asset is archived, its entry is updated to `lifecycle_status: ARCHIVED`. The history is preserved.

### 3.5 Flat Schema, Typed Extension

The core registry schema is flat (no deeply nested structures). Asset-type extensions add typed fields to the flat record without changing the core schema. This keeps the registry queryable without a complex query engine.

### 3.6 Machine-Readable First

The Registry's primary format is YAML (for programmatic consumption). A human-readable Markdown summary is maintained alongside the YAML for review and governance audit purposes. The YAML is authoritative; the Markdown is derived.

### 3.7 Deterministic Population

Every field in a registry entry either comes from a specific source field in the library file (deterministic extraction) or is explicitly set to a documented default (documented derivation). There are no ambiguous fields. Population rules are specified in KNOWLEDGE_REGISTRY_POPULATION_RULES.md for every asset type.

---

## 4. Registry Files and Locations

### 4.1 Registry File Structure

```
00_Governance/Knowledge_Standards/Registry/
│
├── KNOWLEDGE_ASSET_REGISTRY.yaml           ← AUTHORITATIVE (machine-readable)
├── KNOWLEDGE_ASSET_REGISTRY_INDEX.md       ← Human-readable summary index
├── KNOWLEDGE_ASSET_REGISTRY_STANDARD.md    ← This document
├── KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md      ← Schema definition
├── KNOWLEDGE_REGISTRY_POPULATION_RULES.md  ← Library-to-registry mapping
├── KNOWLEDGE_REGISTRY_VALIDATION_RULES.md  ← Validation rule definitions
└── Archive/                                ← Superseded registry versions
    └── KNOWLEDGE_ASSET_REGISTRY_V[N-1].yaml
```

The YAML file is the single authoritative registry. The Markdown index provides a human-readable view keyed by asset type and lifecycle state.

### 4.2 Registry YAML File Structure

The YAML file is structured as a document with a header block and an assets array:

```yaml
---
registry_id: KNOWLEDGE-ASSET-REGISTRY
registry_version: "1.0"
registry_timestamp: "YYYY-MM-DDThh:mm:ssZ"
asset_count: 1234
last_sync: "YYYY-MM-DD"
governing_standard: "KNOWLEDGE_ASSET_REGISTRY_STANDARD.md V1.0"
population_rules: "KNOWLEDGE_REGISTRY_POPULATION_RULES.md V1.0"
validation_rules: "KNOWLEDGE_REGISTRY_VALIDATION_RULES.md V1.0"
---

assets:
  - asset_id: W3S1-001
    [full schema per KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md]
  
  - asset_id: HCM-ORG-001
    [full schema per KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md]
    ...
```

### 4.3 Individual Assumption (ASM) Registry Strategy

1,136 individual assumption entries are too granular for most engine operations. The Registry uses a two-tier approach:
- **Pack-level entries (ASP)**: 13 entries covering pack-level governance (approved_for_reuse, lifecycle_status, pattern_applicability)
- **Assumption-level entries (ASM)**: 1,136 entries in a separate section of the YAML, or a separate `KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml`, covering individual assumption selection hooks (mandatory_if, optional_if, excluded_if)

This keeps the primary registry file manageable (≈130 core entries) while supporting full assumption-level validation in WP18D.

---

## 5. Authority and Ownership

### 5.1 Registry Authority

The Registry Standard (this document) is authoritative over:
- Registry schema (KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md)
- Population rules (KNOWLEDGE_REGISTRY_POPULATION_RULES.md)
- Validation rules (KNOWLEDGE_REGISTRY_VALIDATION_RULES.md)
- The KNOWLEDGE_ASSET_REGISTRY.yaml file

The Registry Standard is subordinate to:
- KNOWLEDGE_ASSET_STANDARD.md (master governance standard)
- KNOWLEDGE_METADATA_STANDARD.md (metadata field definitions)
- KNOWLEDGE_GOVERNANCE_RULES.md (governance rules)
- Individual library standards (for asset-type-specific fields)

### 5.2 Registry Ownership

| Role | Responsibility |
|---|---|
| Registry Owner | BU Lead (Hein Blignaut) — ultimate authority on registry content |
| Registry Facilitator | Proposal Factory Owner / AI Facilitator — maintains registry synchronisation |
| Engine Consumer | Assembly Engine, TIL, WP18D — read-only consumers of registry data |
| Library Curators | BU Leads per library — update library files (triggers registry sync) |

---

## 6. Update and Synchronisation Rules

### 6.1 Update Trigger Events

The Registry must be updated whenever any of the following occur:

| Trigger | Registry Update Required |
|---|---|
| New asset created in any library | Add new entry in DRAFT state |
| Asset advances lifecycle state | Update lifecycle_status, approved_for_reuse, approved_by, approval_date |
| Asset content revised (new version) | Update version, supersedes, superseded_by; add new entry; old entry → SUPERSEDED |
| Asset retired | Update lifecycle_status → ARCHIVED; update approved_for_reuse → No |
| New relationship declared | Update related_assets for all affected entries |
| Assembly rule (mandatory_if etc.) revised | Update assembly_rules block |
| Pre-tender control added/removed | Update validation_rules and governance_notes |
| Governance restriction added/removed | Update governance_notes |

### 6.2 Synchronisation Protocol

The Registry is not updated in real-time (no event bus exists). Updates follow this protocol:

**Synchronous update (required within the same work package):**
- Lifecycle state transitions (APPROVED, SUPERSEDED, ARCHIVED)
- approved_for_reuse changes
- New asset creation

**Deferred update (acceptable within 5 business days):**
- Non-critical metadata updates (tags, confidence_level revisions)
- Relationship cross-reference additions

**Batch sync (scheduled — recommended monthly):**
- Full registry reconciliation against all library indexes
- Validate all file paths resolve
- Validate all cross-referenced IDs exist
- Validate all review_due dates

### 6.3 Registry Version Increment

The registry version increments when:
- Any entry's lifecycle_status changes
- A new entry is added
- An entry is removed (archived)
- The schema version changes

Minor increments (1.0 → 1.1) for entry changes. Major increments (1.0 → 2.0) for schema version changes.

---

## 7. Versioning

### 7.1 Registry Version vs Asset Version

| Concept | Scope | Example |
|---|---|---|
| Registry version | The registry file as a whole | `registry_version: 1.47` |
| Asset version | A single asset's content version | `version: 1.1` (for RC-PROJ-001 V1.1) |
| Schema version | The registry schema definition version | `schema_version: KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md V1.0` |

These are independent. The registry version tracks registry state changes; asset versions track content changes in library files.

### 7.2 Historical Registry Versions

Each time the registry is re-synced after significant changes, a snapshot of the previous KNOWLEDGE_ASSET_REGISTRY.yaml is moved to the Archive/ folder with a version suffix:
```
Archive/KNOWLEDGE_ASSET_REGISTRY_V1.47.yaml
```

This enables retrospective validation of any proposal by recovering the registry state at the time of assembly.

---

## 8. Validation Rules

### 8.1 Registry Integrity Rules

These rules validate the registry itself (not asset content):

| Rule | Description |
|---|---|
| RI-001 | All asset_ids are unique within the registry |
| RI-002 | All asset_types are from the approved type list |
| RI-003 | All lifecycle_status values are from the approved state list |
| RI-004 | All source_file paths resolve to existing files |
| RI-005 | All related_assets IDs exist in the registry |
| RI-006 | All supersedes IDs exist in the registry |
| RI-007 | All superseded_by IDs exist in the registry |
| RI-008 | No circular supersession chains (A supersedes B; B supersedes A) |
| RI-009 | No circular parent-child chains |
| RI-010 | approved_for_reuse = Yes only when lifecycle_status = APPROVED |

### 8.2 Assembly Validation Rules

These rules validate the registry state before assembly begins. Defined in full in KNOWLEDGE_REGISTRY_VALIDATION_RULES.md.

See also CLV-001 through CLV-012 in KNOWLEDGE_RELATIONSHIP_MODEL.md — all CLV rules are implemented at the registry layer in WP18D.

---

## 9. Relationship to Existing Library Indexes

The Registry does not replace existing library index documents. They serve different purposes:

| Document | Purpose | Audience |
|---|---|---|
| MASTER_CAPABILITY_INDEX.md | Human-readable capability reference; evidence tier; governance restrictions | BU Leads, bid managers, human reviewers |
| ENTERPRISE_RISK_REGISTER_V1.md | Full risk entries with content (description, mitigation, guidance) | Risk reviewers, proposal authors |
| ASSUMPTION_LIBRARY_ROADMAP.md | Pack status tracking, roadmap, BU decision register | Governance programme management |
| REFERENCE_MASTER.csv | Reference letter registry with restrictions | Bid managers, account managers |
| **KNOWLEDGE_ASSET_REGISTRY.yaml** | Machine-readable metadata for all assets; engine consumption | Assembly Engine, Validation Engine, TIL |

The Registry and the library indexes must remain synchronised. Where they disagree on lifecycle_status or approved_for_reuse, the library index is the source of truth for content decisions; the Registry governs engine behaviour. Discrepancies must be resolved immediately.

---

## 10. Relationship to WP18D

The Registry is the primary input to WP18D (Knowledge Validation Engine). WP18D should be designed to:

1. Load the Registry YAML at the start of every assembly run
2. Filter the registry to assets applicable to the current tender profile (pattern, platform, engagement type)
3. Apply validation rules (RV-, AV-, CLV-, LV- series) to the filtered set
4. Build the assembly manifest (list of eligible asset_ids with their metadata)
5. Flag BLOCK / ERROR / WARNING conditions before assembly proceeds
6. Output a VALIDATION_REPORT alongside each assembly manifest

The Registry eliminates the need for WP18D to parse individual library files. WP18D reads only the Registry and acts on the structured metadata. This is the key architectural advantage of the Registry: it makes WP18D a deterministic rules engine rather than a document parser.

---

## 11. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-26 | WP18B-EXT.3A | Initial Registry Standard — defines purpose, principles, file structure, sync rules, and relationship to WP18D |
