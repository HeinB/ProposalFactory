---
document_id: REGISTRY-INDEX-ENGINE-V1
title: "Registry Index Engine — Architecture Specification V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-27"
created_by: "WP18E — Knowledge Registry Population Engine Architecture"
approved_by: "Architecture — WP18E"
approved_date: "2026-06-27"
approved_for_reuse: true
category: "Assembly Engine / Registry"
scope: "Defines all lookup indexes built by the KRPE Index Engine — their purpose, derivation logic, schema, and usage by downstream engines."
related_documents:
  - KNOWLEDGE_REGISTRY_POPULATION_ENGINE.md
  - REGISTRY_EXTRACTION_ENGINE.md
  - REGISTRY_OUTPUT_SPECIFICATION.md
  - KNOWLEDGE_VALIDATION_ENGINE.md
---

# Registry Index Engine — Architecture Specification V1.0

**Work Package:** WP18E  
**Status:** APPROVED — Architecture specification complete.

---

## 1. Purpose

The Index Engine builds a set of named lookup tables from the fully extracted and linked registry. These indexes are serialised into `KNOWLEDGE_LOOKUP_INDEX.yaml` and consumed by:

- The **KVE** (for fast ID resolution during validation runs)
- The **Assembly Engine** (for pattern-to-asset mapping during proposal generation)
- The **Tender Intelligence Layer** (for capability gap analysis)
- Future platform components (dashboards, analytics)

**Design principle:** Every index is derived from — and must be derivable from — the registry and relationship graph. No index contains any information that is not already in the registry. Indexes are cache structures, not authoritative data. If an index conflicts with the registry, the registry wins.

---

## 2. Index Derivation Algorithm

The Index Engine processes inputs in three passes:

```
INDEX ENGINE EXECUTION:

PASS 1 — Asset-by-type indexes
  For each entry in core_registry + assumption_registry:
    Add entry.asset_id to asset_by_type[entry.asset_type]
    Add entry.asset_id to lifecycle_by_status[entry.lifecycle_status]
    Add entry.asset_id to approved_only (if entry.approved_for_reuse = true)

PASS 2 — Relationship-derived indexes
  For each relationship in relationship_graph:
    Apply relationship to the relevant named indexes (§4)

PASS 3 — Computed composite indexes
  Derive pattern_readiness_summary
  Derive platform_capability_map
  Derive governance_category_map (RSK only)
```

---

## 3. Index Inventory

| Index Name | Key | Values | Primary Consumer |
|---|---|---|---|
| asset_by_type | asset_type (CAP/ASP/ASM/...) | list of asset_ids | KVE RI rules |
| lifecycle_by_status | lifecycle_status | list of asset_ids | KVE LV rules |
| approved_assets | — | list of approved_for_reuse asset_ids | Assembly Engine |
| pattern_to_sections | pattern_id | list of section_ids (typical_sections) | Assembly Engine |
| pattern_to_mandatory_sections | pattern_id | list of section_ids (mandatory only) | Assembly Engine |
| section_to_patterns | section_id | list of pattern_ids where section appears | Assembly Engine |
| pattern_to_capabilities | pattern_id | list of cap_ids applicable to pattern | TIL + Assembly |
| capability_to_sections | cap_id | list of section_ids sourced from that CAP | Assembly Engine |
| cap_to_assumption_packs | cap_id | list of asp_ids linked to that CAP | Assembly Engine |
| pack_to_assumptions | asp_id | list of asm_ids within the pack | KVE LV-ASP rules |
| assumption_to_pack | asm_id | asp_id (parent pack) | KVE CLV-006 |
| risk_to_assumptions | rsk_id | list of asm_ids cross-referenced by the risk | KVE CLV-006 |
| risk_to_sections | rsk_id | list of section_ids where risk is disclosed | Assembly Engine |
| mandatory_risks | — | list of rsk_ids where mandatory_if_engagement = TRUE | Assembly Engine |
| pattern_to_risks | pattern_id | list of rsk_ids applicable to pattern | Assembly Engine |
| capability_to_references | cap_id | list of ref_ids linked to that CAP | Assembly Engine |
| pattern_to_methodologies | pattern_id | list of mth_ids applicable to pattern | Assembly Engine |
| platform_capability_map | platform (Oracle/Acumatica/BeBanking) | list of cap_ids for that platform | TIL |
| governance_category_map | Category-A / Category-B | list of rsk_ids | KVE LV-RSK rules |
| supersession_chains | asset_id | {supersedes: id, superseded_by: id} | KVE CLV-007 |
| orphan_detection | — | list of asset_ids with no relationships | KVE CLV rules |
| pattern_readiness_summary | pattern_id | {total_sections, mandatory_sections, approved_caps, missing_caps} | Reporting |

---

## 4. Index Schemas

### 4.1 asset_by_type

```yaml
asset_by_type:
  CAP: [W3S1-001, W3S1-002, W3S1-003, ...]
  ASP: [HCM-ORG-001, HCM-PAY-001, ...]
  ASM: [HCM-ORG-001-ASM-001, HCM-ORG-001-ASM-002, ...]
  RSK: [RC-PROJ-001, RC-OPS-001, ...]
  MTH: [MTH-001, MTH-002, ...]
  REF: [REF-001, REF-002, ...]
  PAT: [P1, P2, P3, ...]
  SEC: [S-1, S-2, S-3, ...]
  CON: []
  COM: []
  PPT: []
  PRT: []
```

**Derivation:** PASS 1 — direct iteration over all registry entries.

---

### 4.2 lifecycle_by_status

```yaml
lifecycle_by_status:
  DRAFT: [RC-PROJ-001, RC-OPS-001, ...]   # all 40 RSK are DRAFT per TD-001
  APPROVED: [W3S1-001, W3S1-002, ...]
  SUPERSEDED: []
  ARCHIVED: []
  NORMALISED: []
  READY_FOR_REVIEW: []
  AUTO_APPROVED: []
  REVIEW_REQUIRED: []
```

**Derivation:** PASS 1 — group by `lifecycle_status` field.

---

### 4.3 approved_assets

```yaml
approved_assets:
  - W3S1-001
  - W3S1-002
  ...
```

**Derivation:** PASS 1 — all entries where `approved_for_reuse = true`.

---

### 4.4 pattern_to_sections

```yaml
pattern_to_sections:
  P1:
    all_sections: [S-1, S-2, S-3, S-7, S-21, S-22, ...]
    mandatory_sections: [S-1, S-2, S-3]
    optional_sections: [S-7, S-21, ...]
  P2:
    all_sections: [...]
    mandatory_sections: [...]
    optional_sections: [...]
```

**Derivation:** PASS 2 — from PAT entries: `pat_ext.typical_sections`, `pat_ext.mandatory_sections`, `pat_ext.optional_sections`.

---

### 4.5 section_to_patterns

```yaml
section_to_patterns:
  S-21:
    appears_in_patterns: [P1, P2, P5, P7]
    mandatory_in_patterns: [P1, P5]
    optional_in_patterns: [P2, P7]
```

**Derivation:** PASS 2 — invert pattern_to_sections.

---

### 4.6 pattern_to_capabilities

```yaml
pattern_to_capabilities:
  P1:
    - W3S1-001
    - W3S1-002
    - W3S1-003
  P2:
    - ...
```

**Derivation:** PASS 2 — for each CAP entry, check `pattern_applicability` list. Invert to build pattern→CAP mapping. If `pattern_applicability` is populated for a CAP, add CAP to all listed pattern indexes. If empty (DEFERRED), the CAP does not appear in any pattern index yet.

---

### 4.7 capability_to_sections

```yaml
capability_to_sections:
  W3S1-001: [S-21, S-22, S-38]
  W3S1-002: [S-21, S-38]
```

**Derivation:** PASS 2 — from SEC entries: `sec_ext.source_capability_ids`. Invert to build CAP→SEC mapping.

---

### 4.8 cap_to_assumption_packs

```yaml
cap_to_assumption_packs:
  W3S1-001: [HCM-ORG-001]
  W3S1-002: [HCM-ORG-001, HCM-PAY-001]
```

**Derivation:** PASS 2 — from REL-002 and REL-010 relationships (SRC and XRF from CAP to ASP). Built from `prereq_statement` parsing and `source_document` cross-reference.

---

### 4.9 pack_to_assumptions

```yaml
pack_to_assumptions:
  HCM-ORG-001:
    - HCM-ORG-001-ASM-001
    - HCM-ORG-001-ASM-002
    - ...   # all N ASM entries for this pack
  HCM-PAY-001:
    - ...
```

**Derivation:** PASS 2 — from REL-001 (CON relationships from ASM to parent ASP). Group by parent ASP ID.

---

### 4.10 assumption_to_pack

```yaml
assumption_to_pack:
  HCM-ORG-001-ASM-001: HCM-ORG-001
  HCM-ORG-001-ASM-002: HCM-ORG-001
```

**Derivation:** PASS 2 — invert pack_to_assumptions.

---

### 4.11 risk_to_assumptions

```yaml
risk_to_assumptions:
  RC-PROJ-001: [HCM-ORG-001-ASM-017, HCM-PAY-001-ASM-005]
  RC-OPS-001: []
```

**Derivation:** PASS 2 — from REL-003 (XRF relationships from RSK to ASM): `rsk_ext.related_assumptions`.

---

### 4.12 mandatory_risks

```yaml
mandatory_risks:
  - RC-OPS-001   # mandatory_if_engagement = TRUE — applies to all non-P10 proposals
```

**Derivation:** PASS 1 — all RSK entries where `rsk_ext.mandatory_if_engagement = true`. Sorted by assembly_priority ascending.

---

### 4.13 pattern_to_risks

```yaml
pattern_to_risks:
  P1: [RC-OPS-001, RC-PROJ-001, RC-PROJ-002, ...]
  P2: [RC-OPS-001, ...]
```

**Derivation:** PASS 2 — from REL-009 (RST relationships from RSK to PAT). Invert RSK → PAT to PAT → RSK.

---

### 4.14 capability_to_references

```yaml
capability_to_references:
  W3S1-001: [REF-003, REF-007]
  W3S1-002: [REF-003]
```

**Derivation:** PASS 2 — from REL-007 (XRF from CAP to REF via `cap_ext.reference_clients`).

---

### 4.15 pattern_to_methodologies

```yaml
pattern_to_methodologies:
  P1: [MTH-001, MTH-002]
  P2: [MTH-001]
```

**Derivation:** PASS 2 — from MTH entries: `mth_ext.applicable_engagement_types` and `pattern_applicability`. Invert MTH→PAT to PAT→MTH.

---

### 4.16 platform_capability_map

```yaml
platform_capability_map:
  Oracle:
    Oracle_HCM: [W3S1-001, W3S1-002, ...]
    Oracle_ERP: [W3S1-100, ...]
  Acumatica:
    Distribution: [W3S1-200, ...]
  BeBanking: []
```

**Derivation:** PASS 1 — from `cap_ext.kb_destination` or `source_file` path segment. The first two path components of `source_file` after `06_Capabilities/` give Platform and ProductArea.

---

### 4.17 governance_category_map

```yaml
governance_category_map:
  Category-A: [RC-OPS-001, RC-PROJ-001, ...]   # 20 risks
  Category-B: [RC-COMM-001, ...]               # 20 risks
```

**Derivation:** PASS 1 — from `rsk_ext.governance_category`.

---

### 4.18 supersession_chains

```yaml
supersession_chains:
  W3S1-001:
    supersedes: ""          # empty if no predecessor
    superseded_by: ""       # empty if still active
  W3S1-OLD-001:
    supersedes: ""
    superseded_by: W3S1-001
```

**Derivation:** PASS 1 — from `supersedes` and `superseded_by` fields in each registry entry. Used by KVE CLV-007 (SUPERSEDED blocking) and CLV-012 (supersession chain complete).

---

### 4.19 orphan_detection

```yaml
orphan_detection:
  assets_with_no_relationships: []
  assets_with_unresolved_relationships: []
```

**Derivation:** PASS 2 — assets not appearing as source OR target in any relationship graph entry are flagged as orphans. KVE CLV rules then decide whether orphan status is a BLOCK, ERROR, or WARNING based on asset type.

---

### 4.20 pattern_readiness_summary

```yaml
pattern_readiness_summary:
  P1:
    total_sections: 38
    mandatory_sections: 12
    sections_with_approved_cap: 34
    sections_missing_cap: 4
    approved_caps_count: 49
    applicable_methodologies_count: 2
    applicable_references_count: 8
    readiness_pct: 89
  P2:
    ...
```

**Derivation:** PASS 3 — composite calculation:
- `total_sections` = len(pattern_to_sections[pat].all_sections)
- `sections_with_approved_cap` = count of sections where at least one linked CAP is `approved_for_reuse = true`
- `readiness_pct` = round(sections_with_approved_cap / total_sections * 100)

This index is the primary input to the PROPOSAL_READINESS_REPORT (future dashboard component).

---

## 5. Index Determinism

All indexes are deterministic:
- Lists are sorted alphabetically by asset_id
- All integers are computed, never randomised
- Empty lists are represented as `[]` (not null or absent)
- Key order within each index dict is alphabetical

---

## 6. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-27 | WP18E | Initial specification — 20 named indexes; 3-pass derivation algorithm; YAML schemas |
