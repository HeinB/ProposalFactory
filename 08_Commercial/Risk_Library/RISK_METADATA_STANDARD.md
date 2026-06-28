---
document_id: RISK-METADATA-STANDARD-V1
title: "Risk Library Metadata Standard — V1.0"
version: "1.0"
status: "DRAFT — Pending BU Lead Review"
created: "2026-06-26"
created_by: "WP18B-EXT.1A — Enterprise Risk Library Normalisation"
approved_by: ""
approved_date: ""
approved_for_reuse: false
category: "Commercial / Risk Library / Governance"
scope: "Defines all metadata fields required for a canonical risk entry in the APPSolve Enterprise Risk Register. Supersedes the draft schema in RISK_LIBRARY_STANDARD.md Section 3.1 for normalised V1 entries."
related_documents:
  - RISK_LIBRARY_STANDARD.md
  - ENTERPRISE_RISK_REGISTER_V1.md
  - ENTERPRISE_RISK_REGISTER_DRAFT.md
---

# Risk Library Metadata Standard — V1.0

**Purpose:** This document defines the complete metadata schema for a canonical risk entry in the APPSolve Enterprise Risk Register. All 18 normalisation fields introduced in WP18B-EXT.1A are defined here, with permitted values, governance rules, and population guidance.

**Authority:** This standard governs all risk entries at V1.0 or later. Entries at `version: draft-0.1` (from ENTERPRISE_RISK_REGISTER_DRAFT.md) are not yet subject to this standard; they must be normalised to V1.0 format before BU Lead review.

**Approval gate:** No risk entry may be published or used in a proposal until `approved_for_reuse: Yes` is confirmed by the BU Lead. Normalisation to V1.0 format is a prerequisite for BU Lead review.

---

## 1. Core Identity Fields (inherited from RISK_LIBRARY_STANDARD.md)

| Field | Type | Permitted Values |
|---|---|---|
| `risk_id` | String | RC-[CATEGORY]-[NNN] |
| `category` | String | RC-TECH / RC-COMM / RC-PROJ / RC-RES / RC-INFRA / RC-INT / RC-SEC / RC-DATA / RC-MIG / RC-CUT / RC-OPS / RC-CLIENT / RC-COMP / RC-CM / RC-3P |
| `title` | String | 10 words or fewer |
| `platforms` | List | Oracle HCM Cloud / Oracle OIC / Oracle ERP Cloud / Oracle EBS / Oracle WFM / Acumatica / BeBanking / All Oracle SaaS |
| `engagement_types` | List | Implementation / AMS / DBA / All |
| `version` | String | `1.0` (normalised) / `draft-0.1` (pre-normalisation) |
| `approved_for_reuse` | Boolean | Yes / No |
| `approved_by` | String | BU Lead name or blank |
| `approval_date` | Date | YYYY-MM-DD or blank |
| `source` | String | Source document and risk ID(s) |
| `likelihood` | Enum | Low / Medium / High |
| `impact` | Enum | Low / Medium / High |
| `rating` | Computed | LOW / MEDIUM / HIGH / CRITICAL (3×3 matrix) |
| `owner` | String | Role title |

---

## 2. Normalisation Fields (new in WP18B-EXT.1A)

### 2.1 Lifecycle Management

**`lifecycle_status`**
- **Type:** Enum
- **Permitted values:** `Draft` / `Under Review` / `Approved` / `Retired`
- **Governance:** Set to `Draft` at creation. Advances to `Under Review` when submitted for BU Lead review. Advances to `Approved` on BU Lead sign-off. Set to `Retired` when superseded or withdrawn.
- **Default for V1 normalised entries:** `Draft`

**`review_frequency`**
- **Type:** Enum
- **Permitted values:** `Quarterly` / `Bi-annually` / `Annually`
- **Governance:** Set based on risk rating. CRITICAL and HIGH risks → `Quarterly`. MEDIUM risks → `Bi-annually`. LOW risks → `Annually`.

**`last_reviewed`**
- **Type:** Date (YYYY-MM-DD)
- **Governance:** Set to WP18B-EXT.1A creation date for initial normalisation. Updated on each review cycle.

**`next_review`**
- **Type:** Date (YYYY-MM-DD)
- **Governance:** Calculated from `last_reviewed` + `review_frequency`. CRITICAL/HIGH: +90 days. MEDIUM: +180 days. LOW: +365 days.

**`confidence_level`**
- **Type:** Enum
- **Permitted values:** `High` / `Medium` / `Low`
- **Definition:** Confidence in the risk definition, rating, and mitigation based on observed project evidence.
  - `High` — risk has been observed on multiple APPSolve projects; mitigation is proven
  - `Medium` — risk has been observed at least once; mitigation is reasonable but not exhaustively tested
  - `Low` — risk is theoretical or inferred; limited direct project evidence

---

### 2.2 Ownership

**`owner_role`**
- **Type:** String
- **Guidance:** Use standard APPSolve role titles. Typical values: `Project Manager` / `Solution Architect` / `Integration Lead` / `Functional Consultant` / `BU Lead` / `Commercial Manager`.
- **Governance:** The owner role is responsible for monitoring this risk in active proposals and escalating if realised.

**`owner_business_unit`**
- **Type:** Enum
- **Permitted values:** `Oracle HCM` / `Oracle ERP` / `Oracle OIC` / `Oracle Analytics` / `Cross-Platform` / `Acumatica` / `BeBanking` / `Commercial`
- **Guidance:** Assign to the BU that has deepest platform expertise for this risk. Use `Cross-Platform` only where the risk genuinely spans two or more BUs with no clear primary owner.

---

### 2.3 Provenance and Relationships

**`source_assets`**
- **Type:** List of strings
- **Guidance:** List the source assumption pack IDs, section pack IDs, or document IDs from which this risk was extracted or validated. Format: `[PACK_CODE]-[SECTION]-[NNN]` or document IDs.
- **Example:** `["HCM-ORG-001", "HCM-ORG-002", "W3S1-002"]`

**`supersedes`**
- **Type:** String (Risk ID) or blank
- **Guidance:** If this canonical entry replaces an earlier canonical entry (e.g., after a merge or split), record the superseded ID here. Leave blank if this is a new entry with no predecessor.

**`related_risks`**
- **Type:** List of Risk IDs
- **Guidance:** Record canonical Risk IDs (RC-CATEGORY-NNN) that are causally or thematically linked. Do not record source risk IDs.
- **Example:** `["RC-INT-001", "RC-DATA-003"]`

**`governance_notes`**
- **Type:** Freeform text
- **Guidance:** Record any governance decisions, split/merge rationale, classification ambiguity, or BU review commentary that is not captured in other fields.

---

### 2.4 Assumption Cross-References

**`related_assumptions`**
- **Type:** List of Assumption IDs
- **Governance:** Use governed assumption IDs only. Format: `[PACK_CODE]-[SECTION]-[NNN]`. Do NOT record free-text assumption descriptions.
- **Meaning:** These assumptions are the contractual boundary conditions that bound this risk. When a risk is realised, these assumptions are the first check: has the client breached an assumption?
- **Example:** `["HCM-DAT-001", "HCM-DAT-002", "HCM-DAT-003", "OIC-MAP-001"]`

---

### 2.5 Proposal Assembly

**`proposal_sections`**
- **Type:** Structured list
- **Schema:**
  ```
  primary: [section IDs]
  secondary: [section IDs]
  ```
- **Permitted section IDs:** S-12, S-37, S-38, S-50, S-71, S-72, S-73
- **Guidance:**
  - `primary` — the section(s) where this risk must appear when triggered
  - `secondary` — sections where this risk provides supporting context but is not the primary risk entry
- **Standard mapping:**
  - S-50 (Risk Register) is the primary output section for all risks except RC-OPS and RC-COMP
  - S-37 (RAID Framework) always appears as secondary for all risks
  - S-38 (Change Control) appears as secondary for risks classified under RC-PROJ or RC-COMM that relate to scope change
  - S-71 (SLA Framework) appears as secondary for RC-OPS-001
  - S-73 (AMS Change Requests) appears as secondary for AMS-applicable risks

**`proposal_patterns`**
- **Type:** List of integers (1–13)
- **Reference:** PROPOSAL_PATTERN_ENGINE.md
- **Pattern key:**
  - 1 = HCM Full Suite Single
  - 2 = HCM Full Suite Phased
  - 3 = HCM + Payroll Integration
  - 4 = Recruiting Standalone
  - 5 = Learning Standalone
  - 6 = OIC Standalone
  - 7 = ERP Multi-Module
  - 8 = ERP Single Module
  - 9 = EBS Implementation
  - 10 = DBA / Managed Services
  - 11 = Acumatica
  - 12 = BeBanking
  - 13 = AMS
- **Guidance:** List all patterns for which this risk is applicable. Leave blank if the risk is category-level and pattern assignment is delegated to `mandatory_if` rules.

**`assembly_priority`**
- **Type:** Enum
- **Permitted values:** `Critical` / `High` / `Standard`
- **Guidance:**
  - `Critical` — risk must appear at the top of every risk register section for applicable proposals; reviewer must confirm mitigation is current
  - `High` — risk should be reviewed first among its category peers
  - `Standard` — no priority ordering required within category

---

### 2.6 Selection Hooks

Selection hooks replace the generic "Assembly trigger" narrative in the draft schema with deterministic, machine-readable conditions. These are the primary mechanism for the future Risk Selection Engine.

**`mandatory_if`**
- **Type:** Structured condition (Boolean expression over tender profile variables)
- **Effect:** Risk MUST be included in the proposal risk register when this condition is TRUE.
- **Variable vocabulary:**
  - `platform` — platform name(s) in scope (string match)
  - `engagement_type` — "Implementation" / "AMS" / "DBA"
  - `modules` — list of modules in scope
  - `payroll_integration` — TRUE / FALSE
  - `integration_count` — integer
  - `country` — ISO country code
  - `fixed_price` — TRUE / FALSE
  - `oax_in_scope` — TRUE / FALSE
  - `oda_in_scope` — TRUE / FALSE
  - `help_desk_in_scope` — TRUE / FALSE
  - `delivery_model` — "Single" / "Phased"
  - `phase_count` — integer
  - `analytics_requirements_in_tender` — TRUE / FALSE
  - `integration_method_prescribed_in_tender` — TRUE / FALSE
  - `third_party_api` — TRUE / FALSE
  - `personal_data_in_scope` — TRUE / FALSE
  - `digital_channels` — TRUE / FALSE
  - `feature_licensing_confirmed` — TRUE / FALSE
- **Example:** `platform CONTAINS "Oracle HCM" AND engagement_type = "Implementation"`

**`optional_if`**
- **Type:** Structured condition
- **Effect:** Risk SHOULD be considered for inclusion; the proposal author must make a judgment call based on context.
- **Example:** `platform CONTAINS "Oracle HCM" AND integration_count <= 2`

**`excluded_if`**
- **Type:** Structured condition
- **Effect:** Risk MUST NOT appear in the proposal risk register when this condition is TRUE.
- **Example:** `engagement_type = "AMS"`

---

## 3. Derived and Computed Fields

These fields are not entered manually but are derived from other fields.

| Derived Field | Source |
|---|---|
| `rating` | 3×3 matrix: likelihood × impact |
| `next_review` | `last_reviewed` + `review_frequency` |
| `applicable_patterns` | Intersection of `proposal_patterns` and current tender profile |

---

## 4. Rating Matrix

| | **Low Impact** | **Medium Impact** | **High Impact** |
|---|---|---|---|
| **High Likelihood** | MEDIUM | HIGH | CRITICAL |
| **Medium Likelihood** | LOW | MEDIUM | HIGH |
| **Low Likelihood** | LOW | LOW | MEDIUM |

---

## 5. Review Frequency by Rating

| Rating | Minimum Review Frequency |
|---|---|
| CRITICAL | Quarterly |
| HIGH | Quarterly |
| MEDIUM | Bi-annually |
| LOW | Annually |

---

## 6. Completeness Checklist (per entry)

Before submitting a risk entry for BU Lead review, all fields below must be populated:

| # | Field | Required |
|---|---|---|
| 1 | risk_id | Mandatory |
| 2 | category | Mandatory |
| 3 | title | Mandatory |
| 4 | platforms | Mandatory |
| 5 | engagement_types | Mandatory |
| 6 | version | Must be "1.0" |
| 7 | approved_for_reuse | Must be "No" until BU review |
| 8 | source | Mandatory |
| 9 | likelihood | Mandatory |
| 10 | impact | Mandatory |
| 11 | rating | Computed — must match matrix |
| 12 | owner | Mandatory |
| 13 | lifecycle_status | Mandatory |
| 14 | owner_role | Mandatory |
| 15 | owner_business_unit | Mandatory |
| 16 | review_frequency | Mandatory |
| 17 | last_reviewed | Mandatory |
| 18 | next_review | Mandatory |
| 19 | confidence_level | Mandatory |
| 20 | source_assets | At least 1 entry |
| 21 | related_risks | Optional (blank acceptable) |
| 22 | related_assumptions | At least 1 governed ID |
| 23 | proposal_sections | Mandatory — primary and secondary |
| 24 | proposal_patterns | At least 1 pattern |
| 25 | assembly_priority | Mandatory |
| 26 | mandatory_if | At least one condition |
| 27 | optional_if | Optional (blank acceptable) |
| 28 | excluded_if | Optional (blank acceptable) |
| 29 | governance_notes | Optional |
| 30 | Risk description | Full text — mandatory |
| 31 | Standard mitigation | Full text — mandatory |
| 32 | Customisation guidance | Full text — mandatory |

---

## 7. Change Control

This standard is versioned. Changes require BU Lead approval. Minor clarifications (adding permitted values, correcting guidance text) may be made by the Risk Library Administrator; structural changes (adding or removing fields) require full BU review.

| Version | Date | Author | Change |
|---|---|---|---|
| 1.0 | 2026-06-26 | WP18B-EXT.1A | Initial standard — normalisation of draft schema |
