---
document_id: KNOWLEDGE-RELATIONSHIP-MODEL-V1
title: "Universal Knowledge Asset Relationship Model — V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-26"
created_by: "WP18B-EXT.3 — Universal Knowledge Asset Governance Standard"
approved_by: "Architecture — WP18B-EXT.3"
approved_date: "2026-06-26"
approved_for_reuse: true
category: "Governance / Knowledge Standards"
scope: "Defines how knowledge assets in the APPSolve Proposal Factory relate to each other. Relationship types, dependency hierarchy, traceability requirements, and cross-library validation rules for WP18D."
related_documents:
  - KNOWLEDGE_ASSET_STANDARD.md
  - KNOWLEDGE_METADATA_STANDARD.md
  - KNOWLEDGE_GOVERNANCE_RULES.md
---

# Universal Knowledge Asset Relationship Model — V1.0

**Authority:** KNOWLEDGE_ASSET_STANDARD.md Section 4.4  
**Primary consumer:** WP18D — Proposal QA Engine (cross-library relationship validation)

---

## 1. Relationship Type Registry

Seven relationship types govern how knowledge assets connect. Each type has a defined direction, cardinality, and traceability requirement.

| Relationship Type | Code | Direction | Description |
|---|---|---|---|
| GOVERNS | GOV | Standard → Asset | A governance document defines the rules for a library of assets |
| SOURCES | SRC | Asset → Asset | One asset was extracted or derived from another |
| CONTAINS | CON | Pack → Item | A pack asset contains individual items |
| CROSS_REFERENCES | XRF | Asset ↔ Asset | Two peer assets reference each other (bidirectional) |
| SUPERSEDES | SUP | New → Old | A newer version replaces an older version |
| GENERATES | GEN | Asset → Output | An asset is consumed by the assembly pipeline to produce a proposal output |
| RESTRICTS | RST | Rule/Control → Asset | A governance rule or pre-tender control restricts an asset's use |

---

## 2. Full Relationship Diagram

```
┌────────────────────────────────────────────────────────────────────────┐
│              GOVERNANCE LAYER (Universal Standards)                     │
│                                                                         │
│  KNOWLEDGE_ASSET_STANDARD.md ──GOV──► All governed assets              │
│  RISK_LIBRARY_STANDARD.md    ──GOV──► All RSK assets                   │
│  METHODOLOGY_LIBRARY_STANDARD.md ─GOV─► All MTH assets                │
│                                                                         │
└─────────────────────────────────┬───────────────────────────────────────┘
                                  │ GOV
                                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        EVIDENCE LAYER                                    │
│                                                                          │
│  Client References (REF) ─────────────────────────────────────────────► │
│  DOCUMENT_REGISTER.csv (HIST-NNN) ────SRC──────────────────────────►    │
│  Consultant Records (CON) ──────────────────────────────────────────►    │
│                                                                          │
└───────────────────────────────────────────────────────────────────────┬─┘
                                                                        │ SRC
                                                                        ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      CAPABILITY LAYER                                    │
│                                                                          │
│  Capability Assets (CAP)                                                 │
│  W1S1-001 through W4-ERP-003, W5-METH-001                               │
│  49 approved assets in 06_Capabilities/                                  │
│                                                                          │
│  CAP ──XRF──► REF (reference_clients field)                             │
│  CAP ──SRC──► HIST documents in DOCUMENT_REGISTER.csv                   │
│  CAP ──XRF──► CAP (related capabilities, e.g., W2S1-001 ↔ W2S1-005)   │
│                                                                          │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │ SRC
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      ASSUMPTION LAYER                                    │
│                                                                          │
│  Assumption Packs (ASP) ──CON──► Individual Assumptions (ASM)           │
│  13 approved packs; 1,136 assumptions                                    │
│                                                                          │
│  ASM ──XRF──► CAP (derived from capability asset content)               │
│  ASM ──XRF──► ASM (related assumptions within and across packs)         │
│  ASM ──XRF──► RSK (related_assumptions cross-reference)                 │
│                                                                          │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │ XRF (related_assumptions)
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        RISK LAYER                                        │
│                                                                          │
│  Enterprise Risks (RSK)                                                  │
│  40 canonical risks in 08_Commercial/Risk_Library/                       │
│                                                                          │
│  RSK ──SRC──► CAP (source_assets — extracted from capability assets)    │
│  RSK ──XRF──► ASM (related_assumptions — governed assumption IDs)       │
│  RSK ──XRF──► RSK (related_risks — peer risks)                          │
│                                                                          │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │ SRC
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                     METHODOLOGY LAYER                                    │
│                                                                          │
│  Methodologies (MTH)                                                     │
│  W2S1-005 (Oracle); W5-METH-001 (Platform-Agnostic)                     │
│                                                                          │
│  MTH ──XRF──► CAP (methodology references capability context)           │
│  MTH ──XRF──► RSK (methodology addresses known project risks)           │
│                                                                          │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │ GEN (combined with above)
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    ASSEMBLY LAYER                                         │
│                                                                          │
│  Project Plan Templates (PPT)  ◄── (not yet created)                   │
│  Proposal Section Templates (PRT) ◄── (not yet created)                 │
│                                                                          │
│  Assembly Engine consumes: CAP + ASM + RSK + MTH + REF + CON           │
│  Output: Section-by-section proposal content                            │
│                                                                          │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │ GEN
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                     PROPOSAL OUTPUT                                      │
│                                                                          │
│  Rendered Proposal (Markdown → Word/PDF via WP19)                       │
│  Assembly manifest: all asset IDs, versions, lifecycle states at use    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Relationship Type Specifications

### 3.1 GOVERNS (GOV)

**Direction:** Standard document → Asset library  
**Cardinality:** One standard governs many assets (1:N)  
**Declared in:** Governance standard's `scope` field; not in individual asset records  
**Example:** KNOWLEDGE_ASSET_STANDARD.md governs all 10 asset types

**Validation rule (WP18D):** Every asset library must have a declared governing standard. A library without a governing standard document is a governance defect.

---

### 3.2 SOURCES (SRC)

**Direction:** Source asset → Derived asset  
**Cardinality:** One or many sources → one derived asset (N:1 at the derived end; 1:N at the source end)  
**Declared in:** `source_assets` field of the derived asset  
**Example:** W3S1-008 (Help Desk capability) ──SRC──► RC-COMM-002 (Help Desk vs Service Cloud confusion risk)

**Constraint:** The source asset must be a governed asset (registered in a library index). An ungoverned source document must be registered in DOCUMENT_REGISTER.csv before it can appear in source_assets.

**Validation rule (WP18D):** Every asset_id in `source_assets` must resolve to a registered governed asset or a HIST-registered source document.

---

### 3.3 CONTAINS (CON)

**Direction:** Pack → Item  
**Cardinality:** One pack contains many items (1:N)  
**Declared in:** `pack_id` field of the item asset  
**Example:** HCM_BASE_ASSUMPTIONS_V1 (ASP) ──CON──► HCM-ORG-001 through HCM-ORG-115 (ASM)

**Constraint:** An item asset cannot exist without a parent pack. Orphan items (no pack_id) are a governance defect.

**Validation rule (WP18D):** Every ASM asset must have a valid `pack_id` that resolves to an approved ASP asset.

---

### 3.4 CROSS_REFERENCES (XRF)

**Direction:** Bidirectional (A ↔ B)  
**Cardinality:** Many-to-many (M:N)  
**Declared in:** `related_assets` field of both assets  
**Example:** RC-PROJ-001 (RSK) ──XRF──► HCM-ORG-001 (ASM) — and — HCM-ORG-001 ──XRF──► RC-PROJ-001

**Constraint:** Cross-references must be reciprocal. If Asset A lists Asset B in related_assets, Asset B should list Asset A. Unreciprocated cross-references are acceptable but noted as a completeness gap.

**Validation rule (WP18D):** Every asset_id in `related_assets` must resolve to a registered governed asset. Dangling references (IDs that don't exist in any library) are a governance defect.

---

### 3.5 SUPERSEDES (SUP)

**Direction:** New version → Old version  
**Cardinality:** One-to-one (1:1)  
**Declared in:** `supersedes` in the new version; `superseded_by` in the old version  
**Example:** ENTERPRISE_RISK_REGISTER_V1.md ──SUP──► ENTERPRISE_RISK_REGISTER_DRAFT.md

**Constraint:** Both ends of the supersession link must be populated (GR-S02). A supersession without both links is a governance defect.

**Validation rule (WP18D):** Verify supersession chain is complete. An asset in SUPERSEDED state must have a `superseded_by` ID that resolves to an APPROVED asset.

---

### 3.6 GENERATES (GEN)

**Direction:** Assembly inputs → Proposal output  
**Cardinality:** Many inputs → one output section (N:1 per section)  
**Declared in:** Assembly manifest (not in individual asset records)  
**Example:** RC-PROJ-001 (RSK) ──GEN──► S-50 risk register section

**Constraint:** The assembly manifest records which asset_ids, versions, and lifecycle states were used to generate each proposal section. This is the primary audit mechanism for proposals.

**Validation rule (WP18D):** At assembly time, verify all contributing assets have `approved_for_reuse: Yes`. Flag any asset with `lifecycle_status ≠ APPROVED` that is included in assembly.

---

### 3.7 RESTRICTS (RST)

**Direction:** Governance rule → Asset  
**Cardinality:** One rule may restrict many assets; one asset may be restricted by many rules  
**Declared in:** `governance_restrictions` or `governance_notes` field of the restricted asset; PT- code register  
**Example:** PT-W8-007 ──RST──► W3S1-008 Section 14.2 (must not appear in external submissions)

**Constraint:** Every RESTRICTS relationship must specify: the restriction text, the trigger condition (always / when condition met), and the consequence of violation.

**Validation rule (WP18D):** Before including an asset in assembly, check for active RESTRICTS relationships. If a PT- code is unsatisfied, block the asset from assembly and surface the restriction to the user.

---

## 4. Cross-Library Relationship Matrix

The following matrix shows which asset types can have relationships with which other asset types.

| From \ To | GOV → | SRC → | CON → | XRF → | SUP → | GEN → | RST → |
|---|---|---|---|---|---|---|---|
| **Standard (STD)** | — | — | — | — | — | — | — |
| **CAP** | ← GOV | SRC ← HIST | — | XRF → CAP, REF | SUP → CAP (old) | GEN → Proposal | ← RST via PT- |
| **ASP** | ← GOV | — | CON → ASM | — | SUP → ASP (old) | — | — |
| **ASM** | ← GOV | SRC ← CAP | ← CON from ASP | XRF → ASM, RSK | — | GEN → S-12, S-05 | ← RST (optional_if) |
| **RSK** | ← GOV | SRC ← CAP | — | XRF → ASM, RSK | SUP → RSK (old) | GEN → S-50, S-37 | ← RST (excluded_if) |
| **MTH** | ← GOV | — | — | XRF → CAP, RSK | SUP → MTH (old) | GEN → S-10, S-11 | — |
| **REF** | ← GOV | — | — | XRF → CAP | SUP → REF (old) | GEN → S-48, S-49 | ← RST via AM req. |
| **PPT** | ← GOV | — | — | XRF → CAP, MTH | SUP → PPT (old) | GEN → S-09 | — |
| **PRT** | ← GOV | SRC ← CAP, ASM, RSK | — | XRF → CAP, ASM, RSK | SUP → PRT (old) | GEN → sections | — |
| **CON** | ← GOV | — | — | — | — | GEN → S-46 | ← RST (ADR-001) |

---

## 5. Dependency Hierarchy for Assembly

The following dependency order governs assembly. Stage N cannot proceed until Stage N-1 has validated its assets.

```
Stage 0 — Tender Profile
  Variables: platform, engagement_type, modules, country, phase_count, etc.

Stage 4 — Capability Selection
  Inputs: CAP library (MASTER_CAPABILITY_INDEX.md)
  Validation: approved_for_reuse = Yes; no unsatisfied PT- codes; 
              governance_restrictions compatible with tender
  Output: Capability manifest (selected Cap IDs)
  Dependencies: Stage 0 variables; REF library for reference validation

Stage 5 — Reference Selection
  Inputs: REF library (REFERENCE_MASTER.csv)
  Validation: approved_for_reuse = Yes; account_manager_required satisfied;
              restrictions compatible with tender profile
  Output: Reference manifest (selected REF IDs)
  Dependencies: Stage 0 variables; Stage 4 (cross-validate cap ↔ ref)

Stage 6 — Methodology Selection
  Inputs: MTH library
  Validation: approved_for_reuse = Yes; applicable_platforms matches tender
  Output: Methodology manifest (selected MTH IDs)
  Dependencies: Stage 0 variables

Stage 7 — Assumption Assembly
  Inputs: ASP/ASM libraries (13 approved packs)
  Validation: Pack approved_for_reuse = Yes; ASM mandatory_if/excluded_if 
              evaluated against tender profile variables
  Output: Assumption schedule (list of qualifying ASM IDs)
  Dependencies: Stage 0 variables; Stage 4 (capability confirms platform scope)

Stage 8 — Risk Assembly
  Inputs: RSK library (ENTERPRISE_RISK_REGISTER_V1.md)
  Validation: RSK approved_for_reuse = Yes; mandatory_if/optional_if/excluded_if
              evaluated; related_assumptions cross-checked against Stage 7 output
  Output: Risk register (list of qualifying RSK IDs, ordered by assembly_priority)
  Dependencies: Stage 0 variables; Stage 7 (assumption cross-refs verified)

Stage 9 — QA Engine (WP18D)
  Validates all manifests for:
  - approved_for_reuse = Yes on all assets
  - No SUPERSEDED or ARCHIVED assets in any manifest
  - All related_assets cross-refs intact (no dangling IDs)
  - All PT- codes satisfied
  - Assembly priority order correct for S-50
  - Cross-library consistency (risks reference assumptions that are in the manifest)
```

---

## 6. Traceability Requirements

Full traceability means the following chain can be followed from a submitted proposal back to governed source material:

```
Rendered Proposal Section
  → Assembly manifest entry (asset_id + version + lifecycle_status at use)
    → Knowledge asset record (approved_for_reuse: Yes at time of use)
      → source_assets (governed asset IDs or HIST-registered documents)
        → DOCUMENT_REGISTER.csv / HIST source documents
```

This chain must be unbroken for every factual claim in any externally submitted proposal.

**Current traceability status:**

| Chain Link | Status | Gap |
|---|---|---|
| Proposal → Assembly manifest | PARTIAL — manifests exist for test runs (ARM IT045); not formalised for all proposals | WP18D |
| Assembly manifest → Knowledge asset | FUNCTIONAL — all assets have governed IDs | — |
| Knowledge asset → source_assets | PARTIAL — RSK and MTH complete; CAP has HIST evidence but not in source_assets field | Remediation recommended |
| source_assets → DOCUMENT_REGISTER | COMPLETE — DOCUMENT_REGISTER.csv exists with HIST-NNN registry | — |

---

## 7. WP18D Enhancement Specification

WP18D (Proposal QA Engine) must extend from single-library validation to cross-library relationship validation. The current WP18D brief (per HANDOVER.md) addresses:
- Risk Selection Engine (mandatory_if / optional_if / excluded_if)
- 12-category QA framework (manual → automated)

This relationship model adds the following WP18D requirements:

### 7.1 Cross-Library Validation Rules (new for WP18D)

| Validation ID | Description | Asset Types | Severity |
|---|---|---|---|
| CLV-001 | Every asset in assembly manifest has approved_for_reuse = Yes | All | BLOCK |
| CLV-002 | Every asset in assembly manifest has lifecycle_status = APPROVED | All | BLOCK |
| CLV-003 | Every asset_id in related_assets resolves to a registered governed asset | All | ERROR |
| CLV-004 | Every asset_id in source_assets resolves to a governed asset or HIST document | All | ERROR |
| CLV-005 | Every PT- code on a CAP asset in the manifest is satisfied | CAP | BLOCK |
| CLV-006 | Every RSK in S-50 has related_assumptions that are present in the assumption manifest | RSK + ASM | WARNING |
| CLV-007 | No SUPERSEDED or ARCHIVED asset appears in any assembly manifest | All | BLOCK |
| CLV-008 | RSK assembly_priority order in S-50 follows CRITICAL+Critical → CRITICAL+High → HIGH+High → MEDIUM → LOW | RSK | WARNING |
| CLV-009 | Every REF used in S-48/S-49 has account_manager_required = No or explicit AM approval documented | REF | BLOCK |
| CLV-010 | Assumption pack scope (platform, engagement_type) is compatible with tender profile | ASP | ERROR |
| CLV-011 | CAP assets restricted to specific sectors are not used in tenders outside that sector | CAP | BLOCK |
| CLV-012 | Supersession chain is complete for any SUPERSEDED asset encountered | All | ERROR |

### 7.2 WP18D Architecture Extension

The existing single-library validation (per-library approved_for_reuse check) must be refactored into a cross-library validation graph:

```
VALIDATION GRAPH
  Node: each asset in assembly manifests
  Edge: each relationship (SRC, XRF, CON)
  
  Graph traversal: from assembly manifest → related_assets → source_assets
  At each node: check approved_for_reuse, lifecycle_status, PT- codes
  At each edge: check the referenced asset_id exists in its library index
  
  Output: VALIDATION_REPORT with BLOCK / ERROR / WARNING findings per CLV-NNN rule
```

### 7.3 Recommended WP18D Work Package Scope Update

The WP18D brief should be updated to explicitly include:

1. **Risk Selection Engine** (originally scoped) — mandatory_if / optional_if / excluded_if logic
2. **Cross-Library Validation Graph** (new) — CLV-001 through CLV-012
3. **Assembly Manifest Generator** (new) — produce and persist manifest for every assembly run
4. **Governance Violation Reporter** (new) — surface BLOCK/ERROR/WARNING findings to user before submission

This extension makes WP18D the universal QA layer for all Proposal Factory knowledge assets, not just the risk register.

---

## 8. Relationship Metadata Summary

When populating `related_assets`, use this format to encode the relationship type:

```yaml
related_assets:
  - asset_id: HCM-ORG-001
    relationship: XRF
    note: "Governing assumption for org design readiness"
  - asset_id: W3S1-002
    relationship: SRC
    note: "Source capability asset — risk extracted from this KB asset"
```

If the relationship type is not specified, default to XRF (cross-reference). The relationship type annotation enables automated graph construction without parsing governance_notes free text.

**Current state:** Most existing assets use simple ID lists in related_assets without relationship type annotation. This is acceptable for manual governance. WP18D should parse both formats.
