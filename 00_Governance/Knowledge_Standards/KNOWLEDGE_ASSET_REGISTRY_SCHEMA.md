---
document_id: KNOWLEDGE-ASSET-REGISTRY-SCHEMA-V1
title: "Universal Knowledge Asset Registry Schema — V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-26"
created_by: "WP18B-EXT.3A — Universal Knowledge Asset Registry"
approved_by: "Architecture — WP18B-EXT.3A"
approved_date: "2026-06-26"
approved_for_reuse: true
category: "Governance / Knowledge Standards"
scope: "Defines the complete field schema for every entry in the Universal Knowledge Asset Registry — including mandatory fields, optional fields, asset-type extensions, field formats, and annotated YAML examples."
related_documents:
  - KNOWLEDGE_ASSET_REGISTRY_STANDARD.md
  - KNOWLEDGE_METADATA_STANDARD.md
  - KNOWLEDGE_REGISTRY_POPULATION_RULES.md
  - KNOWLEDGE_REGISTRY_VALIDATION_RULES.md
---

# Universal Knowledge Asset Registry Schema — V1.0

**Work Package:** WP18B-EXT.3A  
**Status:** APPROVED  
**Authority:** Governed by KNOWLEDGE_ASSET_REGISTRY_STANDARD.md. Field semantics governed by KNOWLEDGE_METADATA_STANDARD.md where overlapping.

---

## 1. Schema Design Principles

1. **Flat first**: All fields are top-level where possible. Nesting is only used for assembly_rules (a logical unit) and asset-type extensions.
2. **Mandatory fields are queryable**: Every field used for filtering, assembly, or validation is mandatory. No engine logic depends on an optional field being present.
3. **Extensions don't break the core**: Asset-type-specific fields go in a typed extension block (`cap_ext`, `asp_ext`, `rsk_ext`, etc.). A parser that ignores extensions still has a complete core record.
4. **Empty is never null**: If a field has no value, use `""` (string) or `[]` (list). Never omit mandatory fields.
5. **Booleans as booleans**: `approved_for_reuse`, `account_manager_required` etc. use YAML boolean (`true`/`false`), not strings.
6. **Dates as ISO 8601 strings**: `"2026-06-26"` — always `YYYY-MM-DD`.

---

## 2. Core Schema — Mandatory Fields

These fields are mandatory for every registry entry, regardless of asset type.

### 2.1 Identity and Type

| Field | Type | Format | Description |
|---|---|---|---|
| `asset_id` | string | Varies by type (see below) | Unique asset identifier — globally unique within the registry |
| `asset_type` | string | CAP / ASP / ASM / RSK / MTH / REF / PPT / PRT / CON / COM / PAT / SEC | Asset type code per KNOWLEDGE_ASSET_STANDARD.md |
| `title` | string | Free text (max 200 chars) | Human-readable asset title |
| `version` | string | `"N.N"` | Asset content version (not registry version) |
| `source_file` | string | Relative path from repo root | Path to the authoritative library file for this asset |

**Asset ID Formats by Type:**

| Type | Format | Example |
|---|---|---|
| CAP | `W[wave]S[sector]-[seq]` or `[PLATFORM]-[DOMAIN]-[seq]` | `W3S1-001`, `OAX-HCM-001` |
| ASP | `[PLATFORM]-[SCOPE]-[seq]` | `HCM-ORG-001`, `OAX-GL-001` |
| ASM | `[pack_id]-ASM-[seq]` | `HCM-ORG-001-ASM-001` |
| RSK | `RC-[CAT]-[seq]` | `RC-PROJ-001`, `RC-TECH-006` |
| MTH | `MTH-[TYPE]-[seq]` | `MTH-OAX-001`, `MTH-ACU-001` |
| REF | `REF-[CLIENT_CODE]-[seq]` | `REF-CAS-001` |
| PPT | `PPT-[PATTERN]-[seq]` | `PPT-P1-001` |
| PRT | `PRT-[SEC]-[seq]` | `PRT-S21-001` |
| CON | `CON-[INITIALS]-[seq]` | `CON-HB-001` |
| COM | `COM-[TYPE]-[seq]` | `COM-BBBEE-001` |
| PAT | `P[seq]` | `P1`, `P7`, `P13` |
| SEC | `S-[seq]` | `S-21`, `S-50` |

### 2.2 Governance and Lifecycle

| Field | Type | Format | Description |
|---|---|---|---|
| `lifecycle_status` | string | DRAFT / NORMALISED / READY_FOR_REVIEW / AUTO_APPROVED / REVIEW_REQUIRED / APPROVED / SUPERSEDED / ARCHIVED | Current state per KNOWLEDGE_ASSET_LIFECYCLE.md |
| `approved_for_reuse` | boolean | true / false | Assembly gate. false = blocked from all proposals. |
| `owner_role` | string | Free text | Role of the asset owner |
| `owner_business_unit` | string | Free text | Business unit responsible for this asset |
| `approval_authority` | string | BU_LEAD / MANAGEMENT / EXTERNAL | Governs who can approve |
| `governing_standard` | string | `"KNOWLEDGE_ASSET_STANDARD.md V[N]"` | The standard that governs this asset |
| `registry_version_added` | string | `"N.N"` | Registry version when this entry was first created |

### 2.3 Provenance

| Field | Type | Format | Description |
|---|---|---|---|
| `created` | string | ISO 8601 date | Date asset was first created |
| `created_by` | string | Free text | Work package, person, or source event that created the asset |
| `governance_notes` | string | Free text | Restrictions, pre-tender controls, decisions, DFA rules |

### 2.4 Assembly State

| Field | Type | Format | Description |
|---|---|---|---|
| `pattern_applicability` | list of string | `[P1, P7, P13]` or `[ALL]` | Delivery patterns where this asset applies. `[ALL]` means all 13 patterns. |
| `proposal_sections` | list of string | `[S-21, S-50]` | Proposal section codes where this asset contributes content |

---

## 3. Core Schema — Optional Fields

These fields are populated where available. Their absence must not break any engine logic — engines check presence before use.

| Field | Type | Format | Description |
|---|---|---|---|
| `description` | string | Free text | Brief asset description (for human review) |
| `confidence_level` | string | High / Medium / Low | Evidence confidence (CAP) or data confidence (RSK) |
| `review_frequency` | string | Monthly / Quarterly / Semi-Annual / Annually | Required review cycle |
| `last_reviewed` | string | ISO 8601 date | Date of last substantive review |
| `review_due` | string | ISO 8601 date | Date next review is due |
| `approved_by` | string | Free text | Name of approving authority |
| `approval_date` | string | ISO 8601 date | Date approval was granted |
| `tags` | list of string | Free text | Keywords for search and filtering |
| `source_assets` | list of string | Asset IDs | Assets that sourced this asset (provenance chain) |
| `related_assets` | list of string | Asset IDs | Assets this asset has a declared relationship to |
| `supersedes` | string | Asset ID or `""` | ID of asset this asset replaces (if any) |
| `superseded_by` | string | Asset ID or `""` | ID of asset that replaces this asset (if any) |
| `library_index_ref` | string | File path | Path to the library index entry for this asset (e.g., row reference in MASTER_CAPABILITY_INDEX.md) |
| `registry_last_synced` | string | ISO 8601 date | Date this registry entry was last synchronised from the library |
| `validation_status` | string | VALID / INVALID / PENDING / BLOCKED | Result of last validation run. BLOCKED = approved_for_reuse gate failed. |
| `validation_issues` | list of string | Validation rule codes | VR codes of failed validation rules at last run |

---

## 4. Assembly Rules Block

The assembly_rules block is a structured sub-object grouping all fields that govern how the asset is selected and included during proposal assembly.

```yaml
assembly_rules:
  mandatory_if: ""          # Variable expression; "" = not mandatory
  optional_if: ""           # Variable expression; "" = always optional
  excluded_if: ""           # Variable expression; "" = never excluded
  assembly_priority: ""     # S-50 priority: Critical / High / Medium / Low / ""
  section_placement: []     # Ordered list of section codes (primary placement first)
  content_source_type: ""   # DIRECT / EXTRACT / MERGE / AI-GENERATE / TEMPLATE / PLACEHOLDER
```

**Assembly rule field semantics:**

| Field | Mandatory? | Engine Rule |
|---|---|---|
| `mandatory_if` | Yes (set `""` if not applicable) | If expression evaluates TRUE for a tender profile, asset is mandatory. If absent from manifest, BLOCK. |
| `optional_if` | Yes (set `""` if not applicable) | If expression evaluates TRUE, asset may be included. If evaluates FALSE, asset is excluded. |
| `excluded_if` | Yes (set `""` if not applicable) | If expression evaluates TRUE, asset is excluded even if other rules would include it. Overrides mandatory_if. |
| `assembly_priority` | No | S-50 ordering when multiple CAPs target the same section |
| `section_placement` | No | Section codes where this asset contributes (order = primary first) |
| `content_source_type` | No | How the Assembly Engine retrieves content from the library file |

**Variable vocabulary for expressions** (consistent with RULE_PROCESSOR.md and assembly engine):
- `platform` — `Oracle HCM Cloud`, `Oracle Fusion ERP`, `Acumatica`, `BeBanking`
- `engagement_type` — `Implementation`, `AMS`, `Managed Services`
- `modules[]` — list of selected modules
- `payroll_integration` — boolean
- `country` — ISO 3166-1 alpha-2 or `RSA`
- `pattern` — P1–P13
- `client_size` — SME / Enterprise / Government

---

## 5. Asset-Type Extension Schemas

Extension blocks are nested under the field `[type_code]_ext`. They add asset-type-specific fields without modifying the core schema.

### 5.1 CAP Extension (`cap_ext`)

```yaml
cap_ext:
  evidence_tier: ""           # Tier 1 / Tier 2 / Tier 3 / Tier 4
  platform: ""                # Oracle HCM Cloud / Oracle Fusion ERP / Acumatica / BeBanking / Cross-Platform
  module: ""                  # Module name (for HCM: Global HR, Payroll, etc.)
  pre_tender_controls: []     # List of pre-tender control requirement strings
  reference_clients: []       # List of REF asset IDs that evidence this capability
  annual_review_obligation: true  # true for all CAP assets
  governance_restrictions: "" # Free text — DFA rules, named client restrictions, etc.
  sector: []                  # Sectors where applicable: Government / Private / Financial Services / All
```

### 5.2 ASP Extension (`asp_ext`)

```yaml
asp_ext:
  pack_code: ""               # Pack identifier code (e.g., HCM-ORG-001)
  platform: ""                # Platform this pack covers
  engagement_type: ""         # Implementation / AMS / All
  assumption_count: 0         # Total number of assumptions in this pack
  pending_decisions: 0        # Number of assumptions with PENDING status (must be 0 for APPROVED)
  section_codes: []           # Section codes this pack contributes to (e.g., [S-38, S-39])
```

### 5.3 ASM Extension (`asm_ext`)

```yaml
asm_ext:
  parent_pack_id: ""          # ID of the ASP this assumption belongs to (mandatory for ASM)
  assumption_text: ""         # Full assumption statement text
  section_code: ""            # Single section code where this assumption appears
  rationale: ""               # Why this assumption exists
  assumption_status: ""       # Approved / Pending Decision / Draft
  decision_reference: ""      # Reference to decision log entry (if Pending Decision)
```

### 5.4 RSK Extension (`rsk_ext`)

```yaml
rsk_ext:
  risk_category: ""           # Project / Technical / Commercial / Operational / Governance
  risk_subcategory: ""        # More specific category
  risk_description: ""        # Plain-language description of the risk
  likelihood: ""              # Low / Medium / High
  impact: ""                  # Low / Medium / High
  gross_rating: ""            # CRITICAL / HIGH / MEDIUM / LOW
  net_rating: ""              # Rating after controls applied
  likelihood_basis: ""        # Evidence basis for likelihood
  impact_basis: ""            # Evidence basis for impact
  primary_control: ""         # Primary mitigation control
  secondary_control: ""       # Secondary mitigation control
  owner: ""                   # Risk owner role
  review_trigger: ""          # Condition that triggers re-rating
  related_assumptions: []     # List of ASM asset IDs that this risk cross-references
  mandatory_if_engagement: "" # Expression or TRUE / FALSE
  proposal_section: ""        # Section code where risk appears in proposal (typically S-50)
  presentation_format: ""     # Standard / Tabular / Narrative
  governance_category: ""     # A / B / C (exception-based classification)
  governance_decision_ref: "" # Reference to BU-RL decision (for Cat-B)
  approval_basis: ""          # Auto-approved basis text (for Cat-A)
  dg_number: ""               # Design Governance item number if applicable
  platform_restriction: ""    # Platform restriction if applicable
```

### 5.5 MTH Extension (`mth_ext`)

```yaml
mth_ext:
  methodology_type: ""        # Implementation / AMS / Managed Services
  applicable_platforms: []    # Platforms this methodology applies to
  applicable_engagement_types: []  # Engagement types
  phase_structure: []         # List of phase names in order
  phase_count: 0              # Total phases
  deliverable_count: 0        # Total deliverables across all phases
  source_document: ""         # Source document (SURE / ACURE / custom)
```

### 5.6 REF Extension (`ref_ext`)

```yaml
ref_ext:
  client_name: ""             # Client organisation name
  client_industry: ""         # Industry sector
  engagement_scope: ""        # Description of what was delivered
  platform: ""                # Platform delivered
  signed_date: ""             # Date reference letter was signed
  account_manager_required: true  # true = must check with AM before use
  restrictions: ""            # Usage restrictions (confidentiality, competitor, etc.)
  letter_on_file: false       # Whether physical letter is on file
```

### 5.7 PPT Extension (`ppt_ext`)

```yaml
ppt_ext:
  applicable_patterns: []     # Delivery patterns this template applies to
  phase_count: 0              # Number of phases in this plan
  typical_duration_weeks: 0   # Typical engagement duration in weeks
  module_scope: []            # Modules covered by this plan
```

### 5.8 PRT Extension (`prt_ext`)

```yaml
prt_ext:
  section_code: ""            # Proposal section code this template produces
  assembly_status: ""         # DIRECT / EXTRACT / MERGE / AI-GENERATE / TEMPLATE / PLACEHOLDER
  source_library: ""          # Library or file this template is drawn from
```

### 5.9 PAT Extension (`pat_ext`)

```yaml
pat_ext:
  pattern_name: ""            # Human-readable pattern name (e.g., "HCM Full Suite Single")
  platform: ""                # Primary platform
  engagement_type: ""         # Implementation / AMS / etc.
  module_scope: []            # Modules included in this pattern
  typical_sections: []        # Section codes typically included for this pattern
  requires_payroll_integration: false  # true if P3 (Payroll Integration pattern)
  bom_reference: ""           # Reference to BOM entry in TENDER_BOM_LIBRARY.md
```

### 5.10 SEC Extension (`sec_ext`)

```yaml
sec_ext:
  section_title: ""           # Section title as appears in proposal
  section_group: ""           # Group/category this section belongs to
  automation_type: ""         # DIRECT / EXTRACT / MERGE / AI-GENERATE / TEMPLATE / PLACEHOLDER
  primary_source_library: ""  # Library type that primarily contributes to this section
  content_source_assets: []   # List of asset IDs that contribute content to this section
  mandatory_for_patterns: []  # Patterns where this section is mandatory
  optional_for_patterns: []   # Patterns where this section is optional
  s50_priority: ""            # Priority within S-50 ordering (if applicable)
```

---

## 6. Complete Example Entry — CAP Asset

```yaml
- asset_id: W3S1-001
  asset_type: CAP
  title: "Oracle HCM Core — Global HR"
  version: "1.0"
  source_file: "06_Capabilities/Oracle/Oracle_HCM/W3S1-001-ORA-HCMCore.md"

  lifecycle_status: APPROVED
  approved_for_reuse: true
  owner_role: "BU Lead"
  owner_business_unit: "Oracle HCM"
  approval_authority: BU_LEAD
  governing_standard: "KNOWLEDGE_ASSET_STANDARD.md V1.0"
  registry_version_added: "1.0"

  created: "2026-06-13"
  created_by: "W3 — Wave 3 Capability Extraction"
  governance_notes: "DFA: never name a specific person. Redpath Rule 21.5 applies — do not reference by project number."

  pattern_applicability: [P1, P2, P3, P7]
  proposal_sections: [S-21, S-22, S-38]

  description: "Core Global HR capability for Oracle HCM Cloud engagements"
  confidence_level: "High"
  review_frequency: "Annually"
  last_reviewed: "2026-06-13"
  review_due: "2027-06-13"
  approved_by: "Hein Blignaut"
  approval_date: "2026-06-13"
  tags: ["Oracle HCM", "Global HR", "Core HR", "HCM Cloud"]
  source_assets: ["HIST-007"]
  related_assets: ["HCM-ORG-001", "W3S1-002"]
  supersedes: ""
  superseded_by: ""
  library_index_ref: "06_Capabilities/MASTER_CAPABILITY_INDEX.md:row-W3S1-001"
  registry_last_synced: "2026-06-26"
  validation_status: PENDING
  validation_issues: []

  assembly_rules:
    mandatory_if: "platform IN ['Oracle HCM Cloud'] AND engagement_type = 'Implementation'"
    optional_if: "platform IN ['Oracle HCM Cloud'] AND engagement_type = 'AMS'"
    excluded_if: "platform NOT IN ['Oracle HCM Cloud']"
    assembly_priority: "Critical"
    section_placement: [S-21, S-22]
    content_source_type: "DIRECT"

  cap_ext:
    evidence_tier: "Tier 1"
    platform: "Oracle HCM Cloud"
    module: "Global HR"
    pre_tender_controls: ["Confirm current client list with AM", "Verify DFA compliance"]
    reference_clients: ["REF-CAS-001", "REF-CAS-002"]
    annual_review_obligation: true
    governance_restrictions: "DFA: never name. Redpath: Rule 21.5."
    sector: ["All"]
```

---

## 7. Complete Example Entry — RSK Asset

```yaml
- asset_id: RC-PROJ-001
  asset_type: RSK
  title: "Project Scope Change Risk"
  version: "1.0"
  source_file: "08_Commercial/Risk_Library/Risks/RC-PROJ-001.md"

  lifecycle_status: DRAFT
  approved_for_reuse: false
  owner_role: "BU Lead"
  owner_business_unit: "Commercial"
  approval_authority: BU_LEAD
  governing_standard: "KNOWLEDGE_ASSET_STANDARD.md V1.0"
  registry_version_added: "1.0"

  created: "2026-06-26"
  created_by: "WP18B-EXT.1A — Enterprise Risk Library Normalisation"
  governance_notes: "Category A — auto-approve eligible. No governance restrictions."

  pattern_applicability: [ALL]
  proposal_sections: [S-50]

  confidence_level: "High"
  review_frequency: "Quarterly"
  tags: ["Project Risk", "Scope", "Change Management"]
  related_assets: ["HCM-ORG-001-ASM-017"]
  validation_status: PENDING
  validation_issues: []

  assembly_rules:
    mandatory_if: ""
    optional_if: ""
    excluded_if: ""
    assembly_priority: "High"
    section_placement: [S-50]
    content_source_type: "EXTRACT"

  rsk_ext:
    risk_category: "Project"
    risk_subcategory: "Scope Management"
    risk_description: "Client requests for scope changes after project initiation may exceed contracted deliverables."
    likelihood: "High"
    impact: "High"
    gross_rating: "CRITICAL"
    net_rating: "HIGH"
    likelihood_basis: "Observed in >60% of historical engagements"
    impact_basis: "Scope change causes schedule and cost overruns; commercial exposure significant"
    primary_control: "Formally governed change control process with written sign-off"
    secondary_control: "Weekly scope boundary review with project steering committee"
    owner: "Project Manager"
    review_trigger: "Any scope change request received"
    related_assumptions: ["HCM-ORG-001-ASM-017", "OAX-GL-001-ASM-004"]
    mandatory_if_engagement: "FALSE"
    proposal_section: "S-50"
    presentation_format: "Tabular"
    governance_category: "A"
    governance_decision_ref: ""
    approval_basis: "Standard cross-engagement risk; likelihood and impact are well-established; rating consistent with historical data"
    dg_number: ""
    platform_restriction: ""
```

---

## 8. Complete Example Entry — ASP Asset

```yaml
- asset_id: HCM-ORG-001
  asset_type: ASP
  title: "Oracle HCM — Organisation Foundation Assumptions"
  version: "1.0"
  source_file: "07_Assumption_Packs/Oracle_HCM/HCM-ORG-001.md"

  lifecycle_status: APPROVED
  approved_for_reuse: true
  owner_role: "BU Lead"
  owner_business_unit: "Oracle HCM"
  approval_authority: BU_LEAD
  governing_standard: "KNOWLEDGE_ASSET_STANDARD.md V1.0"
  registry_version_added: "1.0"

  created: "2026-06-01"
  created_by: "Governance Programme — Wave 1"
  governance_notes: ""

  pattern_applicability: [P1, P2, P3, P7]
  proposal_sections: [S-38, S-39]

  approved_by: "Hein Blignaut"
  approval_date: "2026-06-13"
  tags: ["Oracle HCM", "Organisation", "Foundation", "Structure"]
  validation_status: PENDING
  validation_issues: []

  assembly_rules:
    mandatory_if: "platform IN ['Oracle HCM Cloud']"
    optional_if: ""
    excluded_if: "platform NOT IN ['Oracle HCM Cloud']"
    assembly_priority: "Critical"
    section_placement: [S-38]
    content_source_type: "DIRECT"

  asp_ext:
    pack_code: "HCM-ORG-001"
    platform: "Oracle HCM Cloud"
    engagement_type: "All"
    assumption_count: 89
    pending_decisions: 0
    section_codes: [S-38, S-39]
```

---

## 9. Complete Example Entry — PAT Asset

```yaml
- asset_id: P1
  asset_type: PAT
  title: "HCM Full Suite — Single Phase"
  version: "1.0"
  source_file: "08_Commercial/Assembly_Engine/PROPOSAL_PATTERN_ENGINE.md"

  lifecycle_status: APPROVED
  approved_for_reuse: true
  owner_role: "BU Lead"
  owner_business_unit: "Proposal Factory"
  approval_authority: BU_LEAD
  governing_standard: "KNOWLEDGE_ASSET_STANDARD.md V1.0"
  registry_version_added: "1.0"

  created: "2026-06-13"
  created_by: "WP18A — Proposal Factory Architecture"
  governance_notes: ""

  pattern_applicability: [P1]
  proposal_sections: []

  tags: ["Oracle HCM", "Full Suite", "Single Phase", "P1"]
  validation_status: PENDING
  validation_issues: []

  assembly_rules:
    mandatory_if: ""
    optional_if: ""
    excluded_if: ""
    assembly_priority: ""
    section_placement: []
    content_source_type: ""

  pat_ext:
    pattern_name: "HCM Full Suite — Single Phase"
    platform: "Oracle HCM Cloud"
    engagement_type: "Implementation"
    module_scope: ["Global HR", "Payroll", "Absence", "Performance", "Recruiting", "Learning", "OIC"]
    typical_sections: [S-1, S-2, S-3, S-7, S-8, S-9, S-21, S-22, S-23, S-30, S-38, S-39, S-40, S-41, S-42, S-50]
    requires_payroll_integration: false
    bom_reference: "08_Commercial/Assembly_Engine/TENDER_BOM_LIBRARY.md:P1"
```

---

## 10. Schema Compliance Levels

When validating registry entries, use these compliance levels:

| Level | Criteria |
|---|---|
| FULLY COMPLIANT | All mandatory fields populated; all mandatory lists non-empty; asset-type extension block present and populated |
| SUBSTANTIALLY COMPLIANT | All mandatory fields populated; extension block present; ≤2 optional fields missing |
| PARTIALLY COMPLIANT | All identity and lifecycle fields populated; assembly_rules populated; extension block missing or incomplete |
| NON-COMPLIANT | Any mandatory field missing or empty; lifecycle_status or approved_for_reuse missing |
| BLOCKED | approved_for_reuse = false due to lifecycle or governance gate; engine-blocked regardless of compliance level |

---

## 11. Schema Changelog

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-06-26 | Initial schema — 12 asset types; core mandatory fields; optional fields; assembly_rules block; 10 extension schemas; 4 example entries |
