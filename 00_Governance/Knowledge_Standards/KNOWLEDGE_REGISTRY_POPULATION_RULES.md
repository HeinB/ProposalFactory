---
document_id: KNOWLEDGE-REGISTRY-POPULATION-RULES-V1
title: "Knowledge Registry Population Rules — V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-26"
created_by: "WP18B-EXT.3A — Universal Knowledge Asset Registry"
approved_by: "Architecture — WP18B-EXT.3A"
approved_date: "2026-06-26"
approved_for_reuse: true
category: "Governance / Knowledge Standards"
scope: "Specifies exactly how each knowledge library maps to the Universal Knowledge Asset Registry — source fields, extraction rules, derivation logic, default values, and update triggers for all asset types."
related_documents:
  - KNOWLEDGE_ASSET_REGISTRY_STANDARD.md
  - KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md
  - KNOWLEDGE_REGISTRY_VALIDATION_RULES.md
  - KNOWLEDGE_METADATA_STANDARD.md
---

# Knowledge Registry Population Rules — V1.0

**Work Package:** WP18B-EXT.3A  
**Status:** APPROVED

---

## 1. Purpose and Scope

Population rules define the deterministic mapping from library source data to registry entries. Every registry field either:
- **Extracted**: Comes from a specific, named field in a library document
- **Derived**: Calculated from other extracted fields using a documented rule
- **Defaulted**: Set to a documented fixed value when no source data exists
- **Deferred**: Left empty (`""` or `[]`) until a future work package populates it

No field is ambiguous. This document specifies the source mapping for all 12 asset types catalogued in the Registry.

### 1.1 Notation

| Notation | Meaning |
|---|---|
| `FILE[field]` | Extract `field` from the named file |
| `DERIVE(rule)` | Derive the value using the documented rule |
| `DEFAULT(value)` | Set to this fixed default value |
| `DEFERRED` | Not populated at WP18B-EXT.3A; population deferred |
| `INHERIT(asset_id)` | Inherit value from the parent asset's registry entry |

---

## 2. Capability Assets (CAP)

**Source library:** `06_Capabilities/`  
**Primary index:** `06_Capabilities/MASTER_CAPABILITY_INDEX.md`  
**Asset count at WP18B-EXT.3A:** 49

### 2.1 Source-to-Registry Mapping

| Registry Field | Source | Rule |
|---|---|---|
| `asset_id` | MASTER_CAPABILITY_INDEX.md[Asset ID column] | EXTRACT directly |
| `asset_type` | — | DEFAULT(`CAP`) |
| `title` | MASTER_CAPABILITY_INDEX.md[Capability Title column] | EXTRACT directly |
| `version` | Individual capability file YAML frontmatter[version] | EXTRACT; DEFAULT(`"1.0"`) if absent |
| `source_file` | — | DERIVE: `"06_Capabilities/[subdirectory]/[filename].md"` — locate by asset_id match |
| `lifecycle_status` | MASTER_CAPABILITY_INDEX.md[Status column] | EXTRACT; map `Approved` → `APPROVED`, `Draft` → `DRAFT` |
| `approved_for_reuse` | DERIVE | `true` if lifecycle_status = APPROVED; else `false` |
| `owner_role` | — | DEFAULT(`"BU Lead"`) |
| `owner_business_unit` | MASTER_CAPABILITY_INDEX.md[Platform column] | EXTRACT; map `Oracle HCM` → `"Oracle HCM"` |
| `approval_authority` | — | DEFAULT(`BU_LEAD`) |
| `governing_standard` | — | DEFAULT(`"KNOWLEDGE_ASSET_STANDARD.md V1.0"`) |
| `registry_version_added` | — | SET to current registry version at population time |
| `created` | Individual capability file YAML[created] | EXTRACT; DEFERRED if absent |
| `created_by` | — | DEFAULT(`"W3 — Wave 3 Capability Extraction"`) for all v1.0 assets |
| `governance_notes` | MASTER_CAPABILITY_INDEX.md[Governance Notes / Restrictions column] | EXTRACT; concatenate all applicable columns |
| `pattern_applicability` | MASTER_CAPABILITY_INDEX.md[Patterns column] or Platform column | DERIVE: Oracle HCM → [P1,P2,P3]; Oracle ERP → [P7,P8,P9]; Acumatica → [P11]; BeBanking → [P12]; AMS → [P10,P13]; Cross-Platform → [ALL] |
| `proposal_sections` | MASTER_CAPABILITY_INDEX.md[Section column] | EXTRACT; parse comma-separated codes |
| `description` | Individual capability file first paragraph | DEFERRED (extract during population work package) |
| `confidence_level` | MASTER_CAPABILITY_INDEX.md[Evidence Tier column] | DERIVE: Tier 1 → `"High"`, Tier 2 → `"High"`, Tier 3 → `"Medium"`, Tier 4 → `"Low"` |
| `review_frequency` | — | DEFAULT(`"Annually"`) |
| `last_reviewed` | — | DEFAULT to approval_date |
| `review_due` | DERIVE | last_reviewed + 365 days |
| `approved_by` | — | DEFAULT(`"Hein Blignaut"`) for all Approved v1.0 assets |
| `approval_date` | Individual capability file YAML[approved_date] | EXTRACT; DEFERRED if absent |
| `tags` | MASTER_CAPABILITY_INDEX.md[Platform, Module columns] | DERIVE: extract unique values from Platform and Module |
| `source_assets` | Individual capability file[source_assets] | EXTRACT; DEFAULT `[]` if absent |
| `related_assets` | Individual capability file[related_assets] | EXTRACT; DEFAULT `[]` if absent |
| `supersedes` | — | DEFAULT(`""`) |
| `superseded_by` | — | DEFAULT(`""`) |
| `library_index_ref` | — | DERIVE: `"06_Capabilities/MASTER_CAPABILITY_INDEX.md:row-[asset_id]"` |
| `validation_status` | — | DEFAULT(`PENDING`) at population |

**assembly_rules block:**

| Field | Source |
|---|---|
| `mandatory_if` | Individual capability file[mandatory_if] or DEFERRED if absent |
| `optional_if` | Individual capability file[optional_if] or DEFERRED if absent |
| `excluded_if` | Individual capability file[excluded_if] or DEFERRED if absent |
| `assembly_priority` | MASTER_CAPABILITY_INDEX.md[Priority column] if exists; else `"High"` |
| `section_placement` | Same as proposal_sections (first entry = primary) |
| `content_source_type` | DEFAULT(`"DIRECT"`) for all CAP assets |

**cap_ext block:**

| Field | Source |
|---|---|
| `evidence_tier` | MASTER_CAPABILITY_INDEX.md[Evidence Tier column] |
| `platform` | MASTER_CAPABILITY_INDEX.md[Platform column] |
| `module` | MASTER_CAPABILITY_INDEX.md[Module column] |
| `pre_tender_controls` | MASTER_CAPABILITY_INDEX.md[Pre-Tender Controls column] — parse into list |
| `reference_clients` | MASTER_CAPABILITY_INDEX.md[References column] — parse to REF asset IDs |
| `annual_review_obligation` | DEFAULT(`true`) |
| `governance_restrictions` | MASTER_CAPABILITY_INDEX.md[Restrictions / DFA / Named Client columns] — concatenate |
| `sector` | MASTER_CAPABILITY_INDEX.md[Sector column] if exists; else DEFAULT(`["All"]`) |

### 2.2 Update Triggers

| Trigger | Registry Action |
|---|---|
| New row added to MASTER_CAPABILITY_INDEX.md | Add new CAP entry in DRAFT |
| Status column changes in MASTER_CAPABILITY_INDEX.md | Update lifecycle_status and approved_for_reuse |
| Governance Notes updated | Update governance_notes |
| Individual capability file content revised | Update version; add new entry; mark old entry SUPERSEDED |

---

## 3. Assumption Packs (ASP) and Individual Assumptions (ASM)

**Source library:** `07_Assumption_Packs/`  
**Primary index:** `08_Commercial/ASSUMPTION_LIBRARY_ROADMAP.md`  
**Asset count at WP18B-EXT.3A:** 13 packs / 1,136 assumptions

### 3.1 ASP Source-to-Registry Mapping

| Registry Field | Source | Rule |
|---|---|---|
| `asset_id` | Pack file YAML frontmatter[pack_id] | EXTRACT |
| `asset_type` | — | DEFAULT(`ASP`) |
| `title` | Pack file YAML frontmatter[title] | EXTRACT |
| `version` | Pack file YAML frontmatter[version] | EXTRACT; DEFAULT `"1.0"` if absent |
| `source_file` | — | DERIVE: `"07_Assumption_Packs/[platform]/[pack_filename].md"` |
| `lifecycle_status` | ASSUMPTION_LIBRARY_ROADMAP.md[Pack Status column] or pack file YAML[lifecycle_status] | EXTRACT; map `Complete` / `Approved` → `APPROVED` |
| `approved_for_reuse` | DERIVE | `true` if lifecycle_status = APPROVED and pending_decisions = 0 |
| `owner_role` | — | DEFAULT(`"BU Lead"`) |
| `owner_business_unit` | Pack file YAML[platform] | EXTRACT |
| `approval_authority` | — | DEFAULT(`BU_LEAD`) |
| `created` | Pack file YAML[created] | EXTRACT |
| `created_by` | Pack file YAML[created_by] | EXTRACT |
| `governance_notes` | Pack file YAML[governance_notes] | EXTRACT; DEFAULT `""` if absent |
| `pattern_applicability` | Pack file YAML[platform] | DERIVE using same platform-to-pattern mapping as CAP |
| `proposal_sections` | Pack file YAML[section_codes] | EXTRACT |
| `approved_by` | — | DEFAULT(`"Hein Blignaut"`) for all Approved v1.0 packs |
| `approval_date` | Pack file YAML[approved_date] | EXTRACT |
| `tags` | Pack file YAML[tags] or DERIVE from platform + pack name | EXTRACT or DERIVE |

**asp_ext block:**

| Field | Source |
|---|---|
| `pack_code` | Pack file YAML[pack_id] |
| `platform` | Pack file YAML[platform] |
| `engagement_type` | Pack file YAML[engagement_type] or DEFAULT(`"All"`) |
| `assumption_count` | Count of ASM entries in pack file |
| `pending_decisions` | Count of assumptions with status = PENDING DECISION |
| `section_codes` | Pack file YAML[section_codes] |

### 3.2 ASM Source-to-Registry Mapping

ASM entries are populated from the individual assumption rows within each pack file. Given the 1,136 count, ASM entries are stored in `KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml` (separate from the core registry YAML).

| Registry Field | Source | Rule |
|---|---|---|
| `asset_id` | `[parent_pack_id]-ASM-[seq]` | DERIVE from pack ID + sequential position |
| `asset_type` | — | DEFAULT(`ASM`) |
| `title` | Assumption text (truncated to 100 chars) | EXTRACT from assumption row |
| `version` | — | INHERIT from parent pack version |
| `source_file` | — | INHERIT from parent pack source_file + anchor/line reference |
| `lifecycle_status` | Assumption-level status column in pack file | EXTRACT; map `Approved` → `APPROVED` |
| `approved_for_reuse` | DERIVE | `true` only if parent ASP is APPROVED and this assumption is APPROVED |
| `owner_role` | — | INHERIT from parent ASP |
| `owner_business_unit` | — | INHERIT from parent ASP |
| `approval_authority` | — | INHERIT from parent ASP |
| `created` | — | INHERIT from parent ASP |
| `governance_notes` | Assumption-level decision reference | EXTRACT if exists |
| `pattern_applicability` | — | INHERIT from parent ASP |
| `proposal_sections` | Section code column in pack file | EXTRACT from assumption row |

**assembly_rules for ASM:**

| Field | Source |
|---|---|
| `mandatory_if` | mandatory_if column in pack file assumption row |
| `optional_if` | optional_if column in pack file assumption row |
| `excluded_if` | excluded_if column in pack file assumption row |
| `assembly_priority` | DEFAULT(`"Medium"`) |
| `section_placement` | Same as proposal_sections |
| `content_source_type` | DEFAULT(`"DIRECT"`) |

**asm_ext block:**

| Field | Source |
|---|---|
| `parent_pack_id` | Parent ASP asset_id |
| `assumption_text` | Full assumption text from pack row |
| `section_code` | Section code from pack row |
| `rationale` | Rationale column from pack row (if exists) |
| `assumption_status` | Status column from pack row |
| `decision_reference` | Decision log reference from pack row (if PENDING) |

---

## 4. Enterprise Risks (RSK)

**Source library:** `08_Commercial/Risk_Library/`  
**Primary index:** `08_Commercial/Risk_Library/ENTERPRISE_RISK_REGISTER_V1.md`  
**Asset count at WP18B-EXT.3A:** 40 (all DRAFT)

### 4.1 RSK Source-to-Registry Mapping

The ENTERPRISE_RISK_REGISTER_V1.md YAML frontmatter per risk entry is the authoritative source. All 32 fields in the risk schema map to registry fields.

| Registry Field | Source | Rule |
|---|---|---|
| `asset_id` | Risk entry YAML[risk_id] | EXTRACT directly |
| `asset_type` | — | DEFAULT(`RSK`) |
| `title` | Risk entry YAML[title] | EXTRACT |
| `version` | Risk entry YAML[version] | EXTRACT |
| `source_file` | — | DERIVE: `"08_Commercial/Risk_Library/Risks/[risk_id].md"` if individual files exist; else `"08_Commercial/Risk_Library/ENTERPRISE_RISK_REGISTER_V1.md:[risk_id]"` |
| `lifecycle_status` | Risk entry YAML[lifecycle_status] | EXTRACT |
| `approved_for_reuse` | Risk entry YAML[approved_for_reuse] | EXTRACT |
| `owner_role` | Risk entry YAML[owner_role] | EXTRACT |
| `owner_business_unit` | Risk entry YAML[owner_business_unit] | EXTRACT |
| `approval_authority` | Risk entry YAML[approval_authority] | EXTRACT |
| `created` | Risk entry YAML[created] | EXTRACT |
| `created_by` | Risk entry YAML[created_by] | EXTRACT |
| `governance_notes` | Risk entry YAML[governance_notes] | EXTRACT |
| `pattern_applicability` | Risk entry YAML[applicable_patterns] | EXTRACT |
| `proposal_sections` | — | DERIVE: DEFAULT `[S-50]` for all RSK |
| `confidence_level` | Risk entry YAML[confidence_level] | EXTRACT |
| `tags` | Risk entry YAML[tags] | EXTRACT |
| `related_assets` | Risk entry YAML[related_assumptions] | EXTRACT (these are the ASM cross-references) |
| `validation_status` | — | DEFAULT(`PENDING`) |

**assembly_rules for RSK:**

| Field | Source |
|---|---|
| `mandatory_if` | Risk entry YAML[mandatory_if] |
| `optional_if` | DEFAULT(`""`) — risks are included based on pattern and profile, not optional_if logic |
| `excluded_if` | Risk entry YAML[excluded_if] or DEFAULT(`""`) |
| `assembly_priority` | Risk entry YAML[net_rating] → map CRITICAL → `"Critical"`, HIGH → `"High"`, MEDIUM → `"Medium"`, LOW → `"Low"` |
| `section_placement` | DEFAULT(`[S-50]`) |
| `content_source_type` | DEFAULT(`"EXTRACT"`) — risk content is extracted from template |

**rsk_ext block:** All 32 normalised risk fields from ENTERPRISE_RISK_REGISTER_V1.md YAML frontmatter are extracted directly. See KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md §5.4 for the full field list.

### 4.2 RSK Update Triggers

| Trigger | Registry Action |
|---|---|
| Risk approved in WP18B-EXT.2 governance session | Update lifecycle_status → APPROVED; approved_for_reuse → true; approved_by; approval_date |
| Risk split or merged (e.g., DG-008) | Update affected entries; set supersedes/superseded_by |
| mandatory_if changed (e.g., RC-OPS-001) | Update assembly_rules.mandatory_if |
| Category B decision resolved | Update governance_notes; trigger lifecycle advancement |

---

## 5. Methodologies (MTH)

**Source library:** `08_Commercial/Assembly_Engine/` (methodology files)  
**Primary index:** Inferred from METHODOLOGY_SELECTION_ENGINE.md  
**Asset count at WP18B-EXT.3A:** 2 (OAX, Acumatica)

### 5.1 MTH Source-to-Registry Mapping

| Registry Field | Source | Rule |
|---|---|---|
| `asset_id` | DERIVE: `MTH-OAX-001`, `MTH-ACU-001` | Assign during population |
| `asset_type` | — | DEFAULT(`MTH`) |
| `title` | Methodology document title | EXTRACT from document heading |
| `version` | Methodology document YAML[version] | EXTRACT |
| `source_file` | — | Locate methodology file in Assembly_Engine/ |
| `lifecycle_status` | Methodology document YAML[status] | EXTRACT; map `APPROVED` → `APPROVED` |
| `approved_for_reuse` | DERIVE | `true` if lifecycle_status = APPROVED |
| `pattern_applicability` | METHODOLOGY_SELECTION_ENGINE.md[applicable patterns for this methodology] | EXTRACT |
| `proposal_sections` | — | DEFAULT(`[S-30]`) — methodologies appear in section S-30 |

**mth_ext block:** Extract from methodology document YAML frontmatter.

---

## 6. Client References (REF)

**Source library:** `05_References/`  
**Primary index:** `05_References/REFERENCE_MASTER.csv` (or equivalent)  
**Asset count at WP18B-EXT.3A:** 16

### 6.1 REF Source-to-Registry Mapping

| Registry Field | Source | Rule |
|---|---|---|
| `asset_id` | DERIVE: `REF-[CLIENT_CODE]-[seq]` | Assign from client name abbreviation |
| `asset_type` | — | DEFAULT(`REF`) |
| `title` | `"[Client Name] — [Engagement Summary]"` | DERIVE from REFERENCE_MASTER.csv |
| `version` | — | DEFAULT(`"1.0"`) |
| `source_file` | REFERENCE_MASTER.csv or individual reference file path | EXTRACT |
| `lifecycle_status` | REFERENCE_MASTER.csv[Status column] | EXTRACT; map `Active` → `APPROVED` |
| `approved_for_reuse` | DERIVE | `true` only if lifecycle_status = APPROVED AND account_manager_cleared = Yes |
| `governance_notes` | REFERENCE_MASTER.csv[Restrictions column] | EXTRACT |
| `pattern_applicability` | REFERENCE_MASTER.csv[Platform column] | DERIVE using platform-to-pattern mapping |
| `proposal_sections` | — | DEFAULT(`[S-9]`) — references appear in S-9 (Experience/References section) |

**ref_ext block:**

| Field | Source |
|---|---|
| `client_name` | REFERENCE_MASTER.csv[Client column] |
| `client_industry` | REFERENCE_MASTER.csv[Industry column] |
| `engagement_scope` | REFERENCE_MASTER.csv[Scope column] |
| `platform` | REFERENCE_MASTER.csv[Platform column] |
| `signed_date` | REFERENCE_MASTER.csv[Date Signed column] |
| `account_manager_required` | DEFAULT(`true`) for all REF assets (per ADR-001 principle) |
| `restrictions` | REFERENCE_MASTER.csv[Restrictions column] |
| `letter_on_file` | REFERENCE_MASTER.csv[On File column] — map Yes/No to boolean |

### 6.2 REF Special Rules

- `approved_for_reuse` is NEVER set to `true` in the registry without account manager clearance. This is enforced by CLV-008 in KNOWLEDGE_REGISTRY_VALIDATION_RULES.md.
- The ADR-001 rule (CV content from APPTime only; no AI-generated CV text) does not apply to REF but is related. REF assets do not contain CV content.

---

## 7. Proposal Patterns (PAT)

**Source:** `08_Commercial/Assembly_Engine/PROPOSAL_PATTERN_ENGINE.md`  
**Asset count at WP18B-EXT.3A:** 13 (P1–P13)

### 7.1 PAT Source-to-Registry Mapping

| Registry Field | Source | Rule |
|---|---|---|
| `asset_id` | `P[seq]` | DERIVE: P1, P2, ... P13 |
| `asset_type` | — | DEFAULT(`PAT`) |
| `title` | PROPOSAL_PATTERN_ENGINE.md[Pattern Name for P-N] | EXTRACT |
| `version` | — | DEFAULT(`"1.0"`) |
| `source_file` | — | DEFAULT(`"08_Commercial/Assembly_Engine/PROPOSAL_PATTERN_ENGINE.md"`) |
| `lifecycle_status` | — | DEFAULT(`APPROVED`) — all 13 patterns were approved in WP18A |
| `approved_for_reuse` | — | DEFAULT(`true`) |
| `pattern_applicability` | — | DEFAULT(`[self]`) — a pattern is applicable to itself |
| `proposal_sections` | — | DEFAULT(`[]`) — patterns reference sections, not the reverse |

**pat_ext block:** Extract pattern details from PROPOSAL_PATTERN_ENGINE.md for each P-code entry. Module scope, BOM reference, and typical sections are available in TENDER_BOM_LIBRARY.md.

---

## 8. Proposal Sections (SEC)

**Source:** `08_Commercial/Assembly_Engine/CONTENT_SOURCE_MATRIX.md` and `ASSEMBLY_READINESS_MATRIX.md`  
**Asset count at WP18B-EXT.3A:** 56 (from ARM IT045 assembly)

### 8.1 SEC Source-to-Registry Mapping

| Registry Field | Source | Rule |
|---|---|---|
| `asset_id` | `S-[seq]` | EXTRACT from CONTENT_SOURCE_MATRIX.md section code column |
| `asset_type` | — | DEFAULT(`SEC`) |
| `title` | CONTENT_SOURCE_MATRIX.md[Section Title column] | EXTRACT |
| `version` | — | DEFAULT(`"1.0"`) |
| `source_file` | — | DEFAULT(`"08_Commercial/Assembly_Engine/CONTENT_SOURCE_MATRIX.md"`) |
| `lifecycle_status` | ASSEMBLY_READINESS_MATRIX.md[Status column for this section] | EXTRACT |
| `approved_for_reuse` | DERIVE | `true` if automation_type ≠ PLACEHOLDER |
| `proposal_sections` | — | DEFAULT(`[self]`) — section refers to itself |
| `pattern_applicability` | CONTENT_SOURCE_MATRIX.md or ARM IT045 — patterns where this section appears | EXTRACT |

**sec_ext block:** Extract automation type, primary source library, mandatory/optional pattern mapping from CONTENT_SOURCE_MATRIX.md and ASSEMBLY_READINESS_MATRIX.md.

---

## 9. Project Plan Templates (PPT) and Proposal Templates (PRT)

**Asset count at WP18B-EXT.3A:** 0  
These asset types do not yet exist. Population rules apply when they are created.

### 9.1 PPT Population Rules (when assets exist)

Source will be `09_Project_Plans/` or equivalent. Extract:
- Pattern applicability from file name or frontmatter
- Phase count from phase headings
- Duration from timeline data
- Module scope from file name or frontmatter

### 9.2 PRT Population Rules (when assets exist)

Source will be proposal template files. Extract:
- Section code from frontmatter
- Assembly status from frontmatter
- Source library from frontmatter

---

## 10. Population Process

### 10.1 Initial Population Sequence (Deferred to Population Work Package)

The initial Registry population should proceed in this order, to ensure parent assets exist before child relationships are declared:

```
Step 1: PAT assets (P1–P13)
        — No dependencies
        
Step 2: SEC assets (S-1–S-56)
        — Depends on: PAT (pattern_applicability)
        
Step 3: MTH assets (MTH-OAX-001, MTH-ACU-001)
        — Depends on: PAT (pattern_applicability)
        
Step 4: ASP assets (13 packs)
        — Depends on: PAT (pattern_applicability)
        
Step 5: ASM assets (1,136 assumptions — in REGISTRY_ASSUMPTIONS.yaml)
        — Depends on: ASP (parent_pack_id)
        — Depends on: SEC (section_placement)
        
Step 6: CAP assets (49 capabilities)
        — Depends on: PAT (pattern_applicability)
        — Depends on: SEC (proposal_sections)
        
Step 7: RSK assets (40 risks)
        — Depends on: PAT (pattern_applicability)
        — Depends on: ASM (related_assumptions)
        
Step 8: REF assets (16 references)
        — Depends on: PAT (pattern_applicability)
        
Step 9: MTH, REF cross-references
        — Update related_assets on CAP/ASP entries
        
Step 10: Full registry validation run
        — Apply KNOWLEDGE_REGISTRY_VALIDATION_RULES.md
        — Resolve PENDING/INVALID entries
```

### 10.2 Adding a New Asset Type

When a new asset type is introduced (e.g., PPT when project plans are created):

1. Add the type code to KNOWLEDGE_ASSET_STANDARD.md scope table
2. Add the extension schema to KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md
3. Add a section to this document with source-to-registry mapping
4. Add library-specific validation rules to KNOWLEDGE_REGISTRY_VALIDATION_RULES.md
5. Populate entries following the standard population sequence

The core schema and registry file do not require modification — only extension schemas and population rules change.

### 10.3 Batch Synchronisation Rules

Full registry synchronisation runs against library indexes to detect drift:

| Check | Source | Registry Action |
|---|---|---|
| Asset in library but not in registry | Library index | Add PENDING entry |
| Asset in registry but not in library | Library index | Flag VALIDATION DEFECT — investigate |
| lifecycle_status disagrees | Library index vs registry | Update registry to match library; log discrepancy |
| source_file path does not resolve | Filesystem | Flag RI-004 violation |
| review_due in the past | Registry field | Flag for review scheduling |

---

## 11. Population Rules Changelog

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-06-26 | Initial rules — CAP, ASP, ASM, RSK, MTH, REF, PAT, SEC, PPT, PRT; population sequence; batch sync rules; extension protocol |
