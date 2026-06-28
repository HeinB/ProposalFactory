---
document_id: KNOWLEDGE-METADATA-STANDARD-V1
title: "Universal Knowledge Asset Metadata Standard — V1.0"
version: "1.1"
status: "APPROVED"
created: "2026-06-26"
created_by: "WP18B-EXT.3 — Universal Knowledge Asset Governance Standard"
updated: "2026-06-27"
updated_by: "WP18G — KVE Readiness Cleanup (SIMP-001)"
approved_by: "Architecture — WP18B-EXT.3"
approved_date: "2026-06-26"
approved_for_reuse: true
category: "Governance / Knowledge Standards"
scope: "Defines the universal metadata model for all knowledge assets in the APPSolve Proposal Factory. Mandatory, optional, and derived fields. Asset-type extension mappings."
related_documents:
  - KNOWLEDGE_ASSET_STANDARD.md
  - KNOWLEDGE_ASSET_LIFECYCLE.md
  - RISK_METADATA_STANDARD.md
---

# Universal Knowledge Asset Metadata Standard — V1.0

**Authority:** KNOWLEDGE_ASSET_STANDARD.md Section 4.2  
**Applies to:** All asset types: CAP, ASP, ASM, RSK, MTH, REF, PPT, PRT, CON, COM

---

## 1. Metadata Tier Overview

The universal metadata model has three tiers:

| Tier | Purpose | Required? |
|---|---|---|
| **Mandatory** | Fields required for every governed asset regardless of type | Always |
| **Optional** | Fields applied where applicable; absence must be explicitly noted as "not applicable" | Where applicable |
| **Derived** | Fields computed from other metadata or set automatically on lifecycle transition | Automatic |

Asset-type extensions add asset-specific fields on top of the universal tiers. Extensions are defined in Section 4. Extensions may not omit or redefine universal mandatory fields.

---

## 2. Mandatory Metadata

Every governed knowledge asset must carry all fields in this section. An asset that omits any mandatory field cannot advance past DRAFT state.

### 2.1 Identity

| Field | Type | Permitted Values | Notes |
|---|---|---|---|
| `asset_id` | String | Per ID format in KNOWLEDGE_ASSET_STANDARD.md Section 5 | Permanent; never changes after assignment |
| `asset_type` | Enum | CAP / ASP / ASM / RSK / MTH / REF / PPT / PRT / CON / COM | Must match registered asset types |
| `title` | String | ≤15 words | Human-readable; used in indexes and assembly |
| `version` | String | Semantic: 1.0 / 1.1 / 2.0 | Major version = breaking schema change; minor = content update |
| `lifecycle_status` | Enum | DRAFT / NORMALISED / READY_FOR_REVIEW / AUTO_APPROVED / REVIEW_REQUIRED / APPROVED / SUPERSEDED / ARCHIVED | Per KNOWLEDGE_ASSET_LIFECYCLE.md |
| `approved_for_reuse` | Boolean | Yes / No | The assembly gate. No = not eligible for proposals |

### 2.2 Ownership

| Field | Type | Permitted Values | Notes |
|---|---|---|---|
| `owner_role` | String | Role title (e.g., BU Lead, Project Manager, Solution Architect, Commercial Manager) | Role responsible for reviewing and governing this asset |
| `owner_business_unit` | Enum | Corporate / Oracle / Acumatica / BeBanking | BU with deepest authority over this asset's content. **These are the four canonical values produced by KRPE at extraction time.** Granular Oracle sub-BUs (Oracle HCM, Oracle ERP, Oracle OIC, Oracle Analytics, Oracle EBS) are normalised to `Oracle`. Cross-Platform, Cross_BU, and Governance assets are normalised to `Corporate`. Commercial assets use `Corporate`. KVE validates against this canonical list. (SIMP-001 — WP18G 2026-06-27) |

### 2.3 Provenance

| Field | Type | Permitted Values | Notes |
|---|---|---|---|
| `created` | Date | YYYY-MM-DD | Asset creation date |
| `created_by` | String | Work package ID or author role | e.g., "WP18B-EXT.1A" or "BU Lead" |

### 2.4 Governance

| Field | Type | Permitted Values | Notes |
|---|---|---|---|
| `governance_notes` | String | Free text | Mandatory field; "None" is acceptable where no restrictions apply. Record any restrictions, pre-tender controls, or special approval rules here. |

---

## 3. Optional Metadata

These fields must be populated where applicable. Where not applicable, note "N/A" explicitly (do not leave blank, as blank is ambiguous — it could mean "not yet populated" or "not applicable").

### 3.1 Descriptive

| Field | Type | Permitted Values | Notes |
|---|---|---|---|
| `description` | String | Free text | Longer description of asset purpose, scope, and key characteristics |
| `tags` | List | Free-form taxonomy tags | Used for search; not used in assembly logic |
| `confidence_level` | Enum | High / Medium / Low | High = multiple project observations; Medium = at least one observation; Low = theoretical or inferred |

### 3.2 Lifecycle

| Field | Type | Permitted Values | Notes |
|---|---|---|---|
| `review_frequency` | Enum | Quarterly / Bi-annually / Annually | Per review schedule in KNOWLEDGE_ASSET_LIFECYCLE.md Section 5 |
| `last_reviewed` | Date | YYYY-MM-DD | Set at creation (to created date); updated on each review |
| `next_review` | Date | YYYY-MM-DD | Calculated from last_reviewed + review_frequency |

### 3.3 Relationships

| Field | Type | Permitted Values | Notes |
|---|---|---|---|
| `source_assets` | List of asset_ids | Governed asset IDs only | Assets that this asset was extracted or derived from. Free-text source citations are not permitted where a governed ID exists. |
| `related_assets` | List of asset_ids | Governed asset IDs only | Peer assets in other libraries (e.g., risk → assumptions; capability → risks). Use relationship types from KNOWLEDGE_RELATIONSHIP_MODEL.md |
| `supersedes` | asset_id | Single governed asset ID | The previous version that this asset replaces |
| `superseded_by` | asset_id | Single governed asset ID | The newer version that replaces this asset (set when this asset is superseded) |

### 3.4 Assembly

| Field | Type | Permitted Values | Notes |
|---|---|---|---|
| `assembly_priority` | Enum | Critical / High / Medium / Low | Ordering priority within a proposal section (e.g., S-50 risk register order) |
| `mandatory_if` | Condition expression | Variable expression or TRUE | Conditions under which this asset MUST be included in assembly |
| `optional_if` | Condition expression | Variable expression | Conditions under which this asset MAY be included |
| `excluded_if` | Condition expression | Variable expression | Conditions under which this asset MUST NOT be included |

**Condition expression vocabulary** (from RISK_METADATA_STANDARD.md Section 2.6 — applies universally):
- Variables: `platform`, `engagement_type`, `modules`, `payroll_integration`, `integration_count`, `country`, `fixed_price`, `oax_in_scope`, `oda_in_scope`, `help_desk_in_scope`, `delivery_model`, `phase_count`, `wfm_in_scope`, `learning_in_scope`, `recruiting_in_scope`, `ebs_in_scope`, `oci_in_scope`, `bebanking_in_scope`, `acumatica_in_scope`
- Operators: `=`, `!=`, `IN [list]`, `NOT IN [list]`, `>`, `<`, `≥`
- Special value: `TRUE` = unconditional (always include regardless of variables)
- Combining: `AND`, `OR`

---

## 4. Derived Metadata

These fields are set automatically by the governance process. They must not be manually authored before the relevant lifecycle event occurs.

| Field | Type | Set When | Notes |
|---|---|---|---|
| `approved_by` | String | On transition to APPROVED | Name or role of approving authority |
| `approval_date` | Date | On transition to APPROVED | YYYY-MM-DD |
| `approval_status` | Derived | From lifecycle_status | PENDING (DRAFT/NORMALISED/READY_FOR_REVIEW), AUTO_APPROVED, REVIEW_APPROVED, WITHDRAWN |

---

## 5. Completeness Rules

### 5.1 Mandatory Field Completeness

| Lifecycle State | Mandatory Fields Required |
|---|---|
| DRAFT | asset_id, asset_type, title, version, lifecycle_status, approved_for_reuse, owner_role, owner_business_unit, created, created_by, governance_notes |
| NORMALISED | All mandatory fields complete + all applicable optional fields populated |
| READY_FOR_REVIEW | NORMALISED requirements complete |
| APPROVED | All mandatory fields + derived fields (approved_by, approval_date) |

### 5.2 Optional Field Applicability by Asset Type

| Field | CAP | ASP | ASM | RSK | MTH | REF | PPT | PRT |
|---|---|---|---|---|---|---|---|---|
| description | R | R | R | R | R | R | R | R |
| confidence_level | O | O | O | **R** | O | O | N | O |
| review_frequency | R | R | R | **R** | R | R | R | R |
| last_reviewed | R | R | R | **R** | R | R | R | R |
| next_review | R | R | R | **R** | R | R | R | R |
| source_assets | R | R | O | **R** | O | N | O | O |
| related_assets | R | R | O | **R** | O | O | O | O |
| supersedes | O | O | O | O | O | O | O | O |
| assembly_priority | O | N | R | R | O | N | R | R |
| mandatory_if | N | N | R | **R** | O | N | O | O |
| optional_if | N | N | O | O | O | N | O | O |
| excluded_if | N | N | O | O | O | N | O | O |
| tags | O | O | O | O | O | O | O | O |

Key: **R** = Required for this asset type | O = Optional | N = Not applicable

---

## 6. Asset-Type Extension Schemas

Each asset type extends the universal metadata with type-specific fields. Universal mandatory and optional fields take precedence.

### 6.1 Capability Asset (CAP) Extension

| Extension Field | Type | Notes |
|---|---|---|
| `evidence_tier` | Enum | Tier 1 (direct engagement); Tier 1 Contractual (HIST-registered); Tier 2 (platform capability + internal); N/A — Positioning |
| `governance_restrictions` | String | Specific restrictions on use: pre-tender controls, client naming restrictions, sector restrictions |
| `pre_tender_controls` | List | PT- codes that must be completed before external submission |
| `reference_clients` | List | Named reference client IDs (REF-ORA-001, etc.) or "None" |
| `annual_review_obligation` | Boolean | Yes/No — whether OPN revalidation or other annual refresh is required |

### 6.2 Assumption Pack (ASP) Extension

| Extension Field | Type | Notes |
|---|---|---|
| `pack_code` | String | Short code for ID prefixing (e.g., HCM, OIC, AMS) |
| `platform` | List | Applicable platforms (Oracle HCM / Oracle OIC / etc.) |
| `engagement_type` | List | Applicable engagement types |
| `assumption_count` | Integer | Total assumptions in pack |
| `pending_decisions` | Integer | Outstanding BU decisions |

### 6.3 Individual Assumption (ASM) Extension

| Extension Field | Type | Notes |
|---|---|---|
| `pack_id` | String | Parent pack's asset_id |
| `assumption_text` | String | Full assumption text |
| `section_code` | String | Section within pack (e.g., ORG, MAP, REL) |
| `rationale` | String | Why this assumption is required |

### 6.4 Enterprise Risk (RSK) Extension

| Extension Field | Type | Notes |
|---|---|---|
| `category` | Enum | RC-TECH / RC-COMM / RC-PROJ / RC-RES / RC-INFRA / RC-INT / RC-SEC / RC-DATA / RC-MIG / RC-CUT / RC-OPS / RC-CLIENT / RC-COMP / RC-CM / RC-3P |
| `likelihood` | Enum | Low / Medium / High |
| `impact` | Enum | Low / Medium / High |
| `net_rating` | Computed | LOW / MEDIUM / HIGH / CRITICAL — 3×3 matrix |
| `mitigation` | String | Risk mitigation statement |
| `related_assumptions` | List | Governed assumption IDs (subset of related_assets) |
| `proposal_sections` | List | Proposal section codes (S-37, S-50, S-71, etc.) |
| `proposal_patterns` | List | Pattern codes (P1–P13) |

**Note:** The RSK extension fields align exactly with RISK_METADATA_STANDARD.md V1.0. No changes are required to the existing Risk Library schema to comply with this standard. The RISK_METADATA_STANDARD is the authoritative RSK extension definition.

### 6.5 Methodology (MTH) Extension

| Extension Field | Type | Notes |
|---|---|---|
| `methodology_type` | Enum | Implementation / AMS / DBA / Universal |
| `applicable_platforms` | List | Oracle / Acumatica / BeBanking / All |
| `applicable_engagement_types` | List | Implementation / AMS / DBA |
| `phase_structure` | String | Summary of methodology phases |

### 6.6 Client Reference (REF) Extension

| Extension Field | Type | Notes |
|---|---|---|
| `client_name` | String | Client name (may be restricted — see governance_notes) |
| `client_industry` | String | Industry sector |
| `engagement_scope` | String | What was delivered |
| `signed_date` | Date | YYYY-MM-DD — date reference letter was signed |
| `account_manager_required` | Boolean | Yes/No — whether AM approval required before citing in tender |
| `restrictions` | String | Naming restrictions, sector restrictions, scope restrictions |

### 6.7 Project Plan Template (PPT) Extension

| Extension Field | Type | Notes |
|---|---|---|
| `applicable_patterns` | List | Proposal patterns (P1–P13) this template applies to |
| `phase_count` | Integer | Number of project phases |
| `typical_duration_weeks` | Integer | Typical delivery duration in weeks |

### 6.8 Proposal Template (PRT) Extension

| Extension Field | Type | Notes |
|---|---|---|
| `section_code` | String | Proposal section code (S-01 through S-73) |
| `assembly_status` | Enum | EXTRACT / AI-GENERATE / PLACEHOLDER / READY |
| `source_library` | List | Which libraries contribute to this section |

---

## 7. Metadata Format Standards

### 7.1 YAML Frontmatter

All knowledge asset documents must carry their mandatory metadata in YAML frontmatter at the top of the file. The YAML block must be enclosed by `---` delimiters. This enables automated metadata extraction without parsing document body content.

```yaml
---
document_id: [asset_id]-V[version-integer]
asset_type: RSK
title: "Module design not signed off before build begins"
version: "1.0"
lifecycle_status: APPROVED
approved_for_reuse: Yes
owner_role: "Project Manager"
owner_business_unit: "Oracle HCM"
created: "2026-06-26"
created_by: "WP18B-EXT.1A"
governance_notes: "None"
---
```

### 7.2 CSV Index Records

Library index documents (MASTER_CAPABILITY_INDEX.md, REFERENCE_MASTER.csv, CONSULTANT_INDEX.csv) must include at minimum: asset_id, title, lifecycle_status, approved_for_reuse, last_reviewed. These fields enable automated governance validation without reading individual asset files.

### 7.3 Date Format

All dates: YYYY-MM-DD. Never use relative dates ("next quarter"), ambiguous formats ("June '26"), or empty strings.

### 7.4 Cross-Reference Format

All cross-references between governed assets must use the governed asset_id, not the asset title or a free-text description. Example:
- Correct: `related_assets: [RC-PROJ-001, HCM-ORG-001]`
- Incorrect: `related_assets: ["Module design risk", "Organisational structure assumption"]`

---

## 8. Mapping to Existing Library Schemas

| Universal Field | Capability (MASTER_CAPABILITY_INDEX.md) | Assumption Pack | Enterprise Risk (RISK_METADATA_STANDARD) |
|---|---|---|---|
| `asset_id` | Cap ID (W3S1-001) | Pack filename | risk_id (RC-PROJ-001) |
| `asset_type` | CAP | ASP | RSK |
| `title` | Capability Name | Pack title | title |
| `version` | (implicit v1.0) | "v1.0" in filename | version |
| `lifecycle_status` | **APPROVED** (WP18G SIMP-002: field populated in all 49 CAP and 13 ASP files 2026-06-27) | Draft / Approved | lifecycle_status |
| `approved_for_reuse` | approved_for_reuse: Yes | Approved | approved_for_reuse |
| `owner_role` | Owner: Hein Blignaut | (implicit) | owner_role |
| `owner_business_unit` | BU inferred from Wave | (inferred from platform) | owner_business_unit |
| `confidence_level` | Evidence Tier | (not yet) | confidence_level |
| `review_frequency` | Last Review (date) | (not yet) | review_frequency |
| `source_assets` | Tier 1 Evidence field | (not yet) | source_assets |
| `related_assets` | (not yet) | (not yet) | related_risks / related_assumptions |
| `governance_notes` | Governance Restrictions | (governance notes in pack) | governance_notes |
| `mandatory_if` | (not applicable) | (conditional in pack) | mandatory_if |
| `approved_by` | "Approved by Hein Blignaut" (narrative) | "Approved by Hein Blignaut" | approved_by |
| `approval_date` | Last Review date (approximate) | "Approved 2026-06-15" | approval_date |

**Gap summary (updated WP18G 2026-06-27):** Capability Library and Assumption Library now implement `lifecycle_status` (SIMP-002 complete). The enterprise Risk Library is the most fully compliant. `owner_business_unit` canonical values aligned with KRPE output (SIMP-001 complete). Remaining gaps: `confidence_level`, `review_frequency`, `source_assets`, `related_assets` not yet populated in CAP/ASP.

---

## Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-26 | WP18B-EXT.3 | Initial standard |
| 1.1 | 2026-06-27 | WP18G — SIMP-001 | Section 2.2: `owner_business_unit` enum updated to 4 canonical KRPE values (Corporate / Oracle / Acumatica / BeBanking). Section 8: `lifecycle_status` mapping updated to reflect SIMP-002 completion. |
