---
document_id: COMPONENT-INTERFACE-SPECIFICATION-V1
title: "Proposal Factory Component Interface Specification"
version: "1.0"
status: "Approved — Architecture Freeze"
created: "2026-06-27"
created_by: "WP18F — Platform Integration Review & Architecture Freeze"
approved_by: "WP18F"
approved_date: "2026-06-27"
work_package: "WP18F"
category: "Architecture / Interface Specification"
scope: "Defines the interface contract for every engine and data store in the Proposal Factory platform. Every input, output, dependency, upstream provider, downstream consumer, failure behaviour, and validation expectation is specified here. This document is the authoritative interface reference for all implementation work packages."
---

# Proposal Factory Component Interface Specification

**Date:** 2026-06-27 | **Version:** 1.0 | **Status:** Approved — Architecture Freeze  
**Work Package:** WP18F — Platform Integration Review & Architecture Freeze

---

## 1. Purpose and Scope

This specification defines the interface contract for every platform component. "Interface contract" means: what a component receives, what it produces, who it depends on, who depends on it, how it fails, and what validation it expects from its inputs.

This document is the authoritative reference for implementation. If a component's internal architecture document conflicts with this specification on interface matters, raise a change request — do not implement the conflict.

**Notation:**
- **Input:** data the component reads or receives
- **Output:** data the component writes or returns
- **Upstream:** components that produce this component's inputs
- **Downstream:** components that consume this component's outputs
- **Failure mode:** what the component does when it cannot proceed
- **Validation contract:** what the component is entitled to assume about its inputs

---

## 2. Platform Data Flows

```
Knowledge Libraries (CAP/ASP/ASM/RSK/MTH/REF)
        │
        ▼  Source files (YAML frontmatter + Markdown)
   ┌─────────┐
   │  KRPE   │  Knowledge Registry Population Engine
   └────┬────┘
        │  Registry YAML files (4 files)
        ▼
   ┌─────────┐
   │  KVE    │  Knowledge Validation Engine
   └────┬────┘
        │  Assembly Manifest (per-tender)
        ▼
   ┌──────────────────────────────────────────┐
   │  PROPOSAL FACTORY PIPELINE               │
   │                                          │
   │  TIL → PPE → CAP Selection → REF        │
   │           → METH Selection              │
   │           → Assembly Engine             │
   └──────────────────────────────────────────┘
        │
        ▼
   Proposal Output (Markdown → Word/PDF via WP19)
```

---

## 3. Knowledge Libraries

### 3.1 Interface Summary

The Knowledge Libraries are the source of truth for all governed content. They are read-only to all engines. Only authorised human-AI governance processes may write to them.

**Type:** Data store  
**Format:** Markdown files with YAML frontmatter; structured Markdown tables; section-structured Markdown  
**Location:** Multiple directories per asset type:
- CAP: `07_Approved_Content/Approved/`, `06_Capabilities/`
- ASP/ASM: `08_Commercial/Assumptions/`
- MTH: `05_Methodologies/`
- REF: `04_References/`
- COMP: `01_Compliance/`
- CORP: `02_Corporate/`

**Upstream (writes to libraries):** Human-AI governance sessions (BU Lead, Governance Process)  
**Downstream (reads from libraries):** KRPE only  
**Validation contract:** All files are at APPROVED lifecycle state. No file is in DRAFT or REVIEW state at assembly time. (This is a governance process guarantee, not enforced by KRPE pre-extraction.)

**Failure mode:** If a source file is missing, KRPE logs `FILE_NOT_FOUND` and registers the asset from index metadata only (OBS-001 precedent: W2S1-004). KRPE does not abort.

---

## 4. KRPE — Knowledge Registry Population Engine

### 4.1 Role

KRPE is the sole mechanism by which content from the Knowledge Libraries enters the Knowledge Registry. No other process may write to the Registry.

### 4.2 Inputs

| Input | Format | Source | Required |
|---|---|---|---|
| Source files | Markdown + YAML frontmatter | Knowledge Libraries | Yes |
| MASTER_CAPABILITY_INDEX.md | Markdown table | `07_Approved_Content/` | Yes |
| Pack frontmatter files | YAML frontmatter | `08_Commercial/Assumptions/` | Yes |
| krpe_config.yaml | YAML configuration | Engine directory | Yes |

**Extraction order:** PAT→SEC→MTH→REF→ASP→ASM→CAP→RSK  
This order is mandatory. ASP must be extracted before ASM (parent_pack_id forward reference). RSK must be extracted last in Phase B (RSK references CAP assets). Do not change extraction order without an ADR.

### 4.3 Outputs

| Output File | Format | Contents | Consumers |
|---|---|---|---|
| `KNOWLEDGE_ASSET_REGISTRY.yaml` | YAML | CAP + MTH + REF records (Phase A: CAP only) | KVE |
| `KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml` | YAML | ASP + ASM records | KVE |
| `KNOWLEDGE_RELATIONSHIP_GRAPH.yaml` | YAML | Relationship edges (Phase A: REL-001 only) | KVE |
| `KNOWLEDGE_LOOKUP_INDEX.yaml` | YAML | 20 lookup indexes | KVE, Assembly Engine (interim) |

**Output location:** `00_Governance/Knowledge_Standards/`  
**Output guarantee:** Identical output across runs on identical source state (determinism). Only `generated_at` and `build_id` fields differ between runs.

### 4.4 Upstream Providers

- Knowledge Libraries (all asset types)
- MASTER_CAPABILITY_INDEX.md (capability discovery index)

### 4.5 Downstream Consumers

**Direct consumer:** KVE only  
**Indirect consumer:** Assembly Engine (interim mode only — until KVE is implemented, the Assembly Engine reads KNOWLEDGE_LOOKUP_INDEX.yaml directly. This is the authorised interim mode and must end when KVE Phase A is complete.)

### 4.6 Failure Modes

| Failure Condition | KRPE Behaviour |
|---|---|
| Source file missing | Log FILE_NOT_FOUND; register asset from index; continue |
| YAML frontmatter parse error | Log PARSE_ERROR; skip asset; continue |
| Duplicate asset_id detected | Log DUPLICATE_ID; keep first occurrence; flag for review |
| Required field missing | Log MISSING_FIELD; set empty string; continue |
| Index entry without matching file | Log ID_MISMATCH (warning); register from index |
| Circular relationship detected | Log CIRCULAR_REF; skip relationship; continue |

KRPE does not abort on non-fatal errors. All errors are logged to the build report. The build is marked FAILED only if the error count exceeds the configured threshold (default: 0 BLOCKING errors tolerated).

### 4.7 Validation Contract

KRPE is entitled to assume:
- All source files are governed Markdown with YAML frontmatter, Markdown tables, or section-structured format
- All assets in the MASTER_CAPABILITY_INDEX.md have `status: Approved` or equivalent
- The extraction order will not be changed without an ADR

KRPE does NOT validate lifecycle_status or relationship integrity — that is KVE's responsibility.

---

## 5. Knowledge Registry

### 5.1 Role

The Knowledge Registry is the governed, machine-readable representation of all approved knowledge assets. It is produced by KRPE and consumed by KVE. It is never written to directly.

### 5.2 State

| Metric | Value (WP18E-IMP-B Build 4) |
|---|---|
| Total entries | 1,198 |
| CAP | 49 |
| ASP | 13 |
| ASM | 1,136 |
| Relationships (Phase A) | 1,136 |
| Lookup indexes | 20 |
| Lifecycle status | 100% APPROVED |
| Certification | "Certified for Production with Observations" |

### 5.3 Schema Contract

The registry schema is defined in `REGISTRY_OUTPUT_SPECIFICATION.md`. Schema changes require:
1. An ADR entry
2. An updated REGISTRY_OUTPUT_SPECIFICATION.md
3. KRPE code update
4. Re-certification of the registry

KVE, Assembly Engine, and all other consumers are entitled to assume the registry conforms to the certified schema. Schema changes without re-certification invalidate the KVE's ability to trust its input.

### 5.4 Upstream Providers

- KRPE (sole writer)

### 5.5 Downstream Consumers

- KVE (authorised consumer)
- Assembly Engine (interim consumer until KVE Phase A complete)

---

## 6. KVE — Knowledge Validation Engine

### 6.1 Role

KVE is the exclusive intermediary between the Knowledge Registry and all downstream Proposal Factory engines. KVE:
- Mode 1: Runs proactive Platform Health checks (batch, not per-tender)
- Mode 2: Runs per-tender Assembly Validation on invocation by TIL-08, producing an Assembly Manifest

No downstream engine (Assembly Engine, Pattern Engine, Rendering Engine) may read the Registry directly. All downstream engines consume the KVE-certified Assembly Manifest only. This is a non-negotiable architectural constraint.

### 6.2 Inputs

| Input | Format | Source | Mode |
|---|---|---|---|
| KNOWLEDGE_ASSET_REGISTRY.yaml | YAML | Registry | Both |
| KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml | YAML | Registry | Both |
| KNOWLEDGE_RELATIONSHIP_GRAPH.yaml | YAML | Registry | Both |
| KNOWLEDGE_LOOKUP_INDEX.yaml | YAML | Registry | Both |
| Tender Profile | Structured JSON/YAML | TIL output | Mode 2 only |
| BOM (Bill of Materials) | Structured list | Stage 3 output | Mode 2 only |

### 6.3 Outputs

| Output | Format | Consumers | Mode |
|---|---|---|---|
| Platform Health Report | Markdown / YAML | Governance; human review | Mode 1 |
| Assembly Manifest | YAML | ALL downstream engines | Mode 2 |
| Validation Report | Markdown | BU Lead; governance audit | Both |
| Block List | YAML | Caller (TIL-08) | Mode 2 |

**Assembly Manifest schema** (Mode 2 output — frozen):

```yaml
assembly_manifest:
  manifest_id: "AM-[tender_ref]-[timestamp]"
  generated_at: "[ISO 8601]"
  tender_ref: "[string]"
  validation_status: "PASS | BLOCK"
  block_conditions: []          # populated if BLOCK
  eligible_capabilities: []     # CAP assets eligible for this tender
  eligible_packs: []            # ASP packs eligible for this tender
  eligible_assumptions: []      # ASM IDs eligible (by pack inclusion)
  eligible_references: []       # REF assets eligible
  eligible_methodologies: []    # MTH assets eligible
  deselected_capabilities: []   # CAP assets explicitly excluded
  deselected_packs: []          # ASP packs explicitly excluded
  pattern: "[P1–P13]"           # PPE-assigned pattern
  bom: {}                       # BOM from Stage 3
  governance_checks: []         # all 76 validation results
```

### 6.4 Upstream Providers

- Knowledge Registry (read via 4 YAML files)
- TIL (Tender Profile — Mode 2 trigger)
- Stage 3 BOM Resolution (BOM — Mode 2 input)

### 6.5 Downstream Consumers

All Proposal Factory engines from Stage 4 onward:
- Stage 4: Capability Selection Engine
- Stage 5: Reference Selection Engine
- Stage 6: Methodology Selection Engine
- Stage 7: (KVE itself — this is the validation stage)
- Stage 8: Assembly Engine (19-step sequence)
- Stage 9: QA Engine (WP18D scope)
- Stage 10: Rendering Engine (WP19 scope)

### 6.6 Validation Rules — 22 BLOCK Conditions

All 22 conditions must evaluate to PASS for the Assembly Manifest status to be PASS. Any single BLOCK condition fails the manifest.

| Category | BLOCK Conditions |
|---|---|
| Lifecycle | VR-L01: all eligible assets are lifecycle_status = APPROVED |
| Lifecycle | VR-L02: no asset is lifecycle_status = RETIRED or ARCHIVED |
| Completeness | VR-C01 through VR-C08: mandatory fields populated for each asset type |
| Relationships | VR-R01: all ASM assets have resolved parent_pack_id |
| Relationships | VR-R02: no broken source/target references in graph |
| Pack integrity | VR-P01: declared assumption_count = actual count for all packs |
| Pack integrity | VR-P02: all packs have ≥1 assumption |
| Governance | VR-G01: all eligible assets have approved_for_reuse = true |
| Governance | VR-G02: no asset is in REVIEW state |
| BOM | VR-B01: every BOM item maps to a CAP or ASP asset in the registry |
| BOM | VR-B02: every selected CAP is eligible for the BOM platform |
| BOM | VR-B03: no selected CAP is in the deselected list |
| BOM | VR-B04: mandatory packs per pattern are all present |
| BOM | VR-B05: excluded packs per pattern are all absent |

(Remaining BLOCK conditions are specified in KNOWLEDGE_VALIDATION_ENGINE.md Section 5.)

### 6.7 Failure Modes

| Failure Condition | KVE Behaviour |
|---|---|
| Any BLOCK condition met | Assembly Manifest status = BLOCK; block_conditions populated; caller notified |
| Registry file missing or malformed | FATAL — halt; report to governance; do not issue manifest |
| Tender Profile missing required field | Assembly Manifest status = BLOCK; specific field flagged |
| BOM references unknown asset | Assembly Manifest status = BLOCK; VR-B01 triggered |

KVE never issues a PASS manifest when any BLOCK condition exists. KVE never silently ignores errors. This is a non-negotiable guarantee.

### 6.8 Validation Contract

KVE is entitled to assume:
- Registry files are produced by KRPE and conform to the certified schema
- Registry files have not been manually edited
- The Tender Profile has been produced by an authorised TIL session
- Lifecycle status of approved assets is APPROVED (but KVE validates this — it is not a pre-assumption)

---

## 7. TIL — Tender Intelligence Layer (Stage 0)

### 7.1 Role

TIL is the single entry point to the Proposal Factory pipeline. TIL produces the Tender Profile from the raw tender document. The Tender Profile drives all subsequent stages. No stage downstream of TIL reads the tender document directly.

**Operational mode:** Human-AI collaborative. TIL is not fully automated. Each of the 10 steps involves a human analyst with AI assistance interpreting the tender. TIL's output is a governed, human-validated document.

### 7.2 Inputs

| Input | Format | Source | Required |
|---|---|---|---|
| Tender document | PDF, Word, or equivalent | Customer submission | Yes |
| TENDER_INTELLIGENCE_RULES.md | Governed rules | KB Assembly Engine | Yes |
| Knowledge Registry (LOOKUP_INDEX) | YAML | KRPE output | Yes — for asset eligibility |

### 7.3 Outputs

| Output | Format | Consumers |
|---|---|---|
| Tender Profile | Governed Markdown document | All downstream stages |
| Tender Profile fields (assembly-blocking) | 4 fields: engagement_type, primary_platform, delivery_model, contract_type | Stage 3 (BOM), Stage 4 (CAP), KVE Mode 2 trigger |

**4 assembly-blocking fields** — these fields must be populated or assembly cannot proceed:

| Field | Permitted Values | Drives |
|---|---|---|
| engagement_type | Implementation / AMS / Combination | PPE pattern selection |
| primary_platform | Oracle HCM / Oracle ERP / Oracle EBS / Oracle OIC / OCI / Acumatica / BeBanking / Multi-platform | BOM construction |
| delivery_model | Fixed Price / Time and Materials / Managed Service / Subscription | Pattern variant selection |
| contract_type | New Implementation / Upgrade / Extension / Migration | Scope rules |

**Unknown Field Protocol:** If any assembly-blocking field cannot be determined to KNOWN confidence level, TIL records it as UNKNOWN, PARTIAL, or CONTRADICTORY. Assembly does not proceed until UNKNOWN fields are resolved. This protocol is enforced by TIL-08 (KVE Mode 2 invocation — pending KVE implementation).

### 7.4 Downstream Trigger Matrix

TIL drives downstream stages through four trigger chains:

| TIL Input | Output Field | Drives |
|---|---|---|
| Engagement type | engagement_type | PPE: Tier 1 classification → pattern |
| Primary platform | primary_platform | Stage 3: BOM construction |
| Industry + modules | industry_flag | Stage 4: CAP deselection (e.g., G-001 Compensation = mining only) |
| Country + jurisdiction | compliance_jurisdiction | Compliance section inclusion |

### 7.5 Upstream Providers

- Customer (tender document)
- Knowledge Registry (asset lookup)
- TENDER_INTELLIGENCE_RULES.md (process authority)

### 7.6 Downstream Consumers

All pipeline stages from Stage 1 onward:
- Stage 1: Tender Analysis (reads Tender Profile for requirement classification)
- Stage 2: Requirements Extraction (reads Tender Profile for scope determination)
- Stage 3: BOM Resolution (reads primary_platform for BOM build)
- Stage 4: Capability Selection (reads engagement_type, platform, BOM)
- KVE Mode 2 (triggered at TIL-08; receives Tender Profile + BOM)

### 7.7 Failure Modes

| Failure Condition | TIL Behaviour |
|---|---|
| Assembly-blocking field cannot be determined | Record as UNKNOWN; halt progression to Stage 3 |
| Tender document is incomplete | Flag missing sections; request clarification from client |
| Conflicting requirements in tender | Record as CONTRADICTORY; BU Lead resolution required |
| No matching engagement type | Flag; BU Lead determines correct classification |

---

## 8. Proposal Pattern Engine (PPE)

### 8.1 Role

PPE determines which of the 13 defined patterns (P1–P12 + P13 AMS) applies to a specific tender. PPE also determines which of the 82 sections in the Section Library are in scope for that pattern.

**Operational mode:** Currently human-invoked using the PPE decision tree. Can be automated when TIL produces a structured Tender Profile.

### 8.2 Inputs

| Input | Format | Source | Required |
|---|---|---|---|
| Tender Profile (engagement_type, primary_platform, delivery_model) | Governed document | TIL output | Yes |
| PROPOSAL_PATTERN_ENGINE.md | Governed rules | KB Assembly Engine | Yes |

### 8.3 Outputs

| Output | Format | Consumers |
|---|---|---|
| Pattern designation | String (P1–P13 or combination) | Assembly Engine; KVE Mode 2 |
| Section scope list | List of section IDs (from 82) | Assembly Engine Stage 8 |
| Section ordering | Ordered list | Assembly Engine Stage 8 |

### 8.4 Upstream Providers

- TIL (Tender Profile)
- PROPOSAL_PATTERN_ENGINE.md (classification rules)

### 8.5 Downstream Consumers

- Assembly Engine (receives pattern designation and section scope)
- KVE Mode 2 (receives pattern designation; validates mandatory packs per pattern)

### 8.6 Section Scoping Rules (Frozen)

| Rule | Description |
|---|---|
| SI-001 | S-38 (Change Control) excluded for Pattern 13 (AMS); S-73 used instead |
| SI-007 | S-71/S-72 content boundaries defined for AMS SLA sections |
| Combination pattern | P12+P13: S-38 included for implementation scope; S-73 included for AMS scope |

### 8.7 Failure Modes

| Failure Condition | PPE Behaviour |
|---|---|
| Tender Profile fields ambiguous | PPE cannot classify; return to TIL for clarification |
| No matching pattern | Flag to BU Lead; check if new pattern is needed |
| Combination detected | Apply both pattern section lists with overlap rules |

---

## 9. Assembly Engine

### 9.1 Role

The Assembly Engine executes the 19-step assembly sequence to produce the complete proposal document from approved KB sources. It is the most mature platform component — PRODUCTION READY (WP17C 5/5 tests pass).

### 9.2 Inputs

| Input | Format | Source | Required |
|---|---|---|---|
| Assembly Manifest | YAML | KVE Mode 2 (or LOOKUP_INDEX in interim mode) | Yes |
| Tender Profile | Governed document | TIL | Yes |
| Pattern designation + section list | String + list | PPE | Yes |
| Source content | Markdown | Knowledge Libraries (via Assembly Manifest eligibility lists) | Yes |

**Interim mode note:** Until KVE Phase A is implemented, the Assembly Engine reads KNOWLEDGE_LOOKUP_INDEX.yaml directly. This interim mode is authorised but must be replaced by Assembly Manifest consumption when KVE Phase A is complete.

### 9.3 Outputs

| Output | Format | Consumers |
|---|---|---|
| Assumption Schedule (Section G) | Governed Markdown | Proposal document; Key Assumptions section |
| Exclusion Schedule (Section H) | Governed Markdown | Proposal document |
| Key Assumptions section | Governed Markdown | Proposal body |
| BOM Specification | Structured list | QA Engine; Rendering Engine |
| Assembly Audit Log | YAML | Governance audit |
| Full Proposal Draft | Markdown | QA Engine (Stage 9); Rendering (Stage 10) |

### 9.4 Upstream Providers

- KVE (Assembly Manifest — authorised mode)
- TIL (Tender Profile)
- PPE (Pattern designation, section scope)
- Knowledge Libraries (source content referenced by manifest)

### 9.5 Downstream Consumers

- QA Engine (Stage 9 — WP18D scope; not yet implemented)
- Rendering Engine (Stage 10 — WP19 scope; not yet implemented)

### 9.6 19-Step Assembly Sequence (Frozen)

| Step | Action | Gate |
|---|---|---|
| 1 | Load Assembly Manifest | BLOCK if manifest status ≠ PASS |
| 2 | Validate Tender Profile fields | BLOCK if any assembly-blocking field missing |
| 3 | Build Requirement Matrix | Continue |
| 4 | Identify requirement gaps | Flag gaps; continue |
| 5 | Build BOM from Tender Profile | Continue |
| 6 | Load eligible CAP assets from manifest | Continue |
| 7 | Apply eligibility rules | Continue |
| 8 | Apply deselection rules | Continue |
| 9 | Shortlist REF assets | Continue |
| 10 | Select METH assets | Continue |
| 11 | KVE Mode 2 final validation | BLOCK if new BLOCK conditions found |
| 12 | Build Section Structure from PPE | Continue |
| 13 | Assemble Corporate and Partnership sections | Continue |
| 14 | Assemble Understanding and Solution sections | Continue |
| 14.1 | Generate Assumption Schedule (Section G) | Continue |
| 15 | Assemble Scope and Delivery sections | Continue |
| 16 | Assemble People sections | PLACEHOLDER for CVs |
| 17 | Assemble Commercial and Governance sections | Continue |
| 18 | Apply Section Integrity rules (SI-001–007) | Continue |
| 19 | Final QA gate | Flag for human review; continue to output |

### 9.7 Failure Modes

| Failure Condition | Assembly Engine Behaviour |
|---|---|
| Assembly Manifest status = BLOCK | Halt; report block conditions; do not proceed |
| Missing required section content | Insert [PLACEHOLDER — reason]; continue; flag in audit log |
| Assumption Schedule fails validation | Halt; report which of the 10 WP17D-1 checks failed |
| Section Integrity rule violated | Apply rule fix; log; continue |

---

## 10. Content Source Matrix Interface

### 10.1 Role

The CSM is not an engine — it is the specification that the Assembly Engine uses to determine: for each section, what is the primary source, secondary source, assembly method, and validation rules.

**Authority:** CSM is the authoritative reference for Stage 8 assembly. The Assembly Engine must implement CSM rules; it may not deviate from them without an ADR.

### 10.2 Interface

| Input to CSM | Output from CSM |
|---|---|
| Section ID (S-01 through S-82) | Primary source (library code + asset ID) |
| Pattern designation (P1–P13) | Secondary source (if any) |
| BOM (platform scope) | Assembly method (DIRECT/EXTRACT/MERGE/TEMPLATE/AI-GENERATE/PLACEHOLDER) |
| | Validation rules (field-level) |

### 10.3 Assembly Method Definitions (Frozen)

| Method | Definition |
|---|---|
| DIRECT | Content taken verbatim from source asset; metadata substitution only |
| EXTRACT | Specific clauses or sections extracted from source asset |
| MERGE | Multiple source assets combined into one section |
| TEMPLATE | Source provides structure; content filled from tender-specific inputs |
| AI-GENERATE | No approved source; AI generates draft; mandatory human review |
| PLACEHOLDER | Cannot be auto-populated; human authoring required |

---

## 11. QA Engine (Stage 9 — Architecture Reserved)

### 11.1 Status

Not yet implemented. WP18D scope.

### 11.2 Interface (Reserved)

| Input | Source |
|---|---|
| Full Proposal Draft | Assembly Engine output |
| Assembly Audit Log | Assembly Engine |
| QA Framework (12 categories) | PROPOSAL_QA_FRAMEWORK.md (WP18D) |

| Output | Consumers |
|---|---|
| QA Report | Human reviewer |
| Approved Proposal Draft | Rendering Engine |

---

## 12. Rendering Engine (Stage 10 — Architecture Reserved)

### 12.1 Status

Not yet implemented. WP19 scope.

### 12.2 Interface (Reserved)

| Input | Source |
|---|---|
| QA-approved Proposal Draft | QA Engine |
| Rendering Templates | WP19 templates |
| Client metadata | Tender Profile |

| Output | Consumers |
|---|---|
| Word document | Proposal submission |
| PDF document | Proposal submission |

---

## 13. Interface Dependency Summary

| Produces | Consumed By | Status |
|---|---|---|
| Knowledge Libraries → source files | KRPE | Active |
| KRPE → Registry YAML | KVE | Active |
| TIL → Tender Profile | All stages | Active (human-AI) |
| PPE → Pattern + Section List | Assembly Engine | Active (human-invoked) |
| KVE → Assembly Manifest | ALL downstream engines | **Not yet implemented** |
| Assembly Engine → Proposal Draft | QA Engine | Active (manual QA) |
| QA Engine → Approved Draft | Rendering Engine | Not yet implemented |
| Rendering Engine → Word/PDF | Submission | Not yet implemented |

**Critical gap:** KVE → Assembly Manifest. Until KVE Phase A is implemented, the Assembly Engine uses the Registry directly (interim mode). This is the primary architecture implementation gap.

---

## 14. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-27 | WP18F | Initial interface specification — all platform components |
