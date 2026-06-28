---
document_id: KNOWLEDGE-VALIDATION-ENGINE-V1
title: "Knowledge Validation Engine — Architecture Specification V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-27"
created_by: "WP18D — Knowledge Validation Engine"
approved_by: "Architecture — WP18D"
approved_date: "2026-06-27"
approved_for_reuse: true
category: "Assembly Engine / Validation"
scope: "Defines the architecture, operating modes, inputs, outputs, execution model, failure handling, and integration points for the Knowledge Validation Engine (KVE) — the deterministic validation layer between the Universal Knowledge Asset Registry and the Proposal Factory."
governing_standard: "KNOWLEDGE_REGISTRY_VALIDATION_RULES.md V1.0"
related_documents:
  - KNOWLEDGE_ASSET_REGISTRY_STANDARD.md
  - KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md
  - KNOWLEDGE_REGISTRY_VALIDATION_RULES.md
  - VALIDATION_RULE_EXECUTION_MODEL.md
  - KNOWLEDGE_VALIDATION_REPORT_STANDARD.md
  - KNOWLEDGE_HEALTH_SCORE.md
  - ENGINE_ORCHESTRATOR.md
---

# Knowledge Validation Engine — Architecture Specification V1.0

**Work Package:** WP18D  
**Status:** APPROVED — Architecture specification complete. Implementation deferred to implementation work package.  
**Metaphor:** The KVE is the compiler of the Proposal Platform. Like a compiler, it does not produce output — it validates the inputs and either certifies them as assembly-ready or reports exactly what is wrong and why.

---

## 1. Engine Purpose

The Knowledge Validation Engine (KVE) has one mission: to verify that the Knowledge Platform is internally consistent, fully governed, and safe to use before any proposal generation occurs.

The KVE validates **the platform itself**, not proposal content. It runs against the Knowledge Asset Registry and answers:

1. Is the registry structurally sound? (no duplicate IDs, no circular references, no broken chains)
2. Are all assets in a valid lifecycle state with consistent governance metadata?
3. Are cross-library relationships correctly declared and resolvable?
4. For a given tender profile: which assets are eligible, which are mandatory, which are blocked?
5. What is the current health score of the Knowledge Platform?

The KVE does not assemble proposals. It produces a **validation report** and, in Assembly Mode, a **certified assembly manifest** that the Assembly Engine consumes.

### 1.1 Why the KVE Is the "Compiler"

A traditional compiler takes source code and verifies it is syntactically and semantically correct before producing an executable. The KVE does the same:

| Compiler concept | KVE equivalent |
|---|---|
| Source code | Knowledge Asset Registry |
| Syntax check | Registry Integrity rules (RI-) |
| Type checking | Library-Specific rules (LV-) |
| Dependency resolution | Cross-Library rules (CLV-) |
| Build environment validation | Assembly Validation rules (AV-) |
| Compilation output | Assembly Manifest (certified asset list) |
| Build log | Validation Report |
| Compilation errors | BLOCK conditions |
| Compiler warnings | ERROR and WARNING conditions |

This analogy is precise: just as code that fails to compile cannot run, a registry that fails KVE validation cannot be safely assembled into a proposal.

---

## 2. Architectural Position

```
Knowledge Libraries (CAP / ASP / ASM / RSK / MTH / REF / PAT / SEC)
        │
        │  one-way sync (per KNOWLEDGE_REGISTRY_POPULATION_RULES.md)
        ▼
KNOWLEDGE ASSET REGISTRY (KNOWLEDGE_ASSET_REGISTRY.yaml)
        │
        │  read-only input
        ▼
┌─────────────────────────────────────────────────────────┐
│              KNOWLEDGE VALIDATION ENGINE                │
│                                                         │
│  ┌──────────────┐  ┌──────────────┐  ┌───────────────┐ │
│  │ Registry     │  │ Rule Engine  │  │ Report        │ │
│  │ Loader       │→ │ (76 rules)   │→ │ Generator     │ │
│  └──────────────┘  └──────────────┘  └───────────────┘ │
│                           │                             │
│                    ┌──────┴──────┐                      │
│                    │             │                      │
│             ┌──────┴──┐   ┌─────┴──────┐              │
│             │ Manifest │   │ Health     │              │
│             │ Builder  │   │ Calculator │              │
│             └──────────┘   └────────────┘              │
└─────────────────────────────────────────────────────────┘
        │                           │
        ▼                           ▼
ASSEMBLY MANIFEST               VALIDATION REPORT
(certified asset list)          (health / blocker / warning log)
        │
        ▼
Tender Intelligence Layer → Assembly Engine → QA Engine → Rendering Engine
```

The KVE is the only component that reads the Registry. All downstream engines consume only the certified Assembly Manifest and the Validation Report. The Registry is never read directly by the Assembly Engine or TIL.

---

## 3. Operating Modes

The KVE has two operating modes. The same engine and rule set run in both; the difference is whether a tender context is provided.

### Mode 1 — Platform Health Validation

**Trigger:** Scheduled (monthly), manual request, or on registry sync  
**Context:** None — no tender profile  
**Scope:** Full registry — all 1,325+ entries  
**Rules executed:** RI-001 to RI-015, CLV-003, CLV-004, LV- series (all)  
**Output:** Knowledge Health Report + Health Score  
**Purpose:** Certify the platform is ready for any assembly run

Platform Health Validation answers: "Is the Knowledge Platform itself in good order?"

It does not filter by pattern or platform — it validates every asset in the registry regardless of engagement type. This is the periodic maintenance check.

### Mode 2 — Assembly Validation

**Trigger:** Invoked by Tender Intelligence Layer at assembly start  
**Context:** tender_context.yaml (pattern, platform, engagement_type, modules, country, client_size)  
**Scope:** Registry filtered to applicable assets  
**Rules executed:** All 76 rules in the execution order defined in KNOWLEDGE_REGISTRY_VALIDATION_RULES.md §7  
**Output:** Assembly Manifest + Assembly Validation Report  
**Purpose:** Certify the asset set for a specific proposal is ready for assembly

Assembly Validation answers: "For this specific tender, are all required assets available, approved, and correctly configured?"

### Mode Comparison

| Dimension | Mode 1 — Health | Mode 2 — Assembly |
|---|---|---|
| Tender context required | No | Yes |
| Registry scope | Full (all assets) | Filtered (pattern-applicable assets) |
| Rules executed | RI + CLV-003/004 + LV | All 76 |
| Primary output | Health Report + Score | Assembly Manifest + Validation Report |
| Produces manifest | No | Yes |
| Run frequency | Monthly / on sync | Every assembly run |
| Triggered by | Schedule / manual | TIL (Stage 0) |

---

## 4. Engine Inputs

### 4.1 Mandatory Inputs

| Input | File / Format | Source | Mode |
|---|---|---|---|
| Registry (core) | `KNOWLEDGE_ASSET_REGISTRY.yaml` | 00_Governance/Knowledge_Standards/ | Both |
| Registry (assumptions) | `KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml` | 00_Governance/Knowledge_Standards/ | Both |
| Validation rules | `KNOWLEDGE_REGISTRY_VALIDATION_RULES.md` | 00_Governance/Knowledge_Standards/ | Both |

### 4.2 Conditional Inputs

| Input | File / Format | Source | Mode |
|---|---|---|---|
| Tender context | `tender_context.yaml` | TIL output (Stage 0) | Mode 2 only |
| Pre-tender control clearances | `ptc_clearances.yaml` | BU Lead input | Mode 2 only (CLV-005) |
| Account manager clearances | `am_clearances.yaml` | AM input | Mode 2 only (CLV-008, LV-REF-001) |

### 4.3 Tender Context Schema

```yaml
tender_context:
  tender_id: ""           # Unique tender identifier
  tender_date: ""         # Date of tender submission (ISO 8601)
  pattern: ""             # P1–P13 — delivery pattern
  platform: ""            # Oracle HCM Cloud / Oracle Fusion ERP / Acumatica / BeBanking
  engagement_type: ""     # Implementation / AMS / Managed Services
  modules: []             # List of selected modules
  country: ""             # ISO 3166-1 alpha-2 or "RSA"
  client_size: ""         # SME / Enterprise / Government
  client_sector: ""       # Government / Private / Financial Services
  payroll_integration: false  # boolean
  am_clearances: []       # List of REF asset IDs with AM clearance confirmed
  ptc_clearances: []      # List of CAP asset IDs with pre-tender controls cleared
```

---

## 5. Engine Outputs

### 5.1 Mode 1 Outputs

| Output | File | Content |
|---|---|---|
| Health Report (Markdown) | `KNOWLEDGE_HEALTH_REPORT_[date].md` | Human-readable health assessment with score, dimension breakdown, blocker list, remediation recommendations |
| Health Report (YAML) | `KNOWLEDGE_HEALTH_REPORT_[date].yaml` | Machine-readable health data for integration |
| Health Score | Field in both reports | Single 0–100 integer with dimension breakdown |

### 5.2 Mode 2 Outputs

| Output | File | Content |
|---|---|---|
| Assembly Manifest | `ASSEMBLY_MANIFEST_[tender_id].yaml` | Certified list of asset IDs, types, source files, and assembly rules — ready for Assembly Engine |
| Validation Report (Markdown) | `VALIDATION_REPORT_[tender_id].md` | Human-readable validation result with BLOCK/ERROR/WARNING breakdown |
| Validation Report (YAML) | `VALIDATION_REPORT_[tender_id].yaml` | Machine-readable validation data for audit and integration |
| Manifest Status | Field in manifest | VALID / BLOCKED / APPROVED_WITH_CONDITIONS |

### 5.3 Assembly Manifest Schema

```yaml
---
manifest_id: ""                    # [tender_id]-MANIFEST-[timestamp]
tender_id: ""
tender_pattern: ""
tender_platform: ""
manifest_status: ""                # VALID / BLOCKED / APPROVED_WITH_CONDITIONS
manifest_timestamp: ""             # ISO 8601
registry_version: ""               # Registry version used for this validation
validation_report_ref: ""          # Path to sidecar VALIDATION_REPORT.yaml
blocks: 0
errors: 0
warnings: 0
---

manifest_assets:
  - asset_id: ""
    asset_type: ""
    title: ""
    version: ""
    source_file: ""
    lifecycle_status: APPROVED
    approved_for_reuse: true
    assembly_rules:
      mandatory_if: ""
      optional_if: ""
      excluded_if: ""
      assembly_priority: ""
      section_placement: []
      content_source_type: ""
    validation_flags: []           # List of WARNING-level rule codes fired for this asset
```

---

## 6. Execution Model

### 6.1 Overview

The KVE is a **stateless, sequential rules evaluator**. It does not maintain state between runs. Each run is independent and produces a complete, self-contained report. Given the same inputs, it always produces the same outputs (deterministic).

```
START
  │
  ├── LOAD registry (core + assumptions)
  │
  ├── MODE 1? ──── Phase H1: Registry Integrity (RI-)
  │   (Health)         Phase H2: Relationship Checks (CLV-003, CLV-004)
  │                    Phase H3: Library-Specific (all LV-)
  │                    Phase H4: Health Score Calculation
  │                    Phase H5: Health Report Generation
  │                    END (health report)
  │
  └── MODE 2? ──── Phase 1: Registry Integrity (RI-)
      (Assembly)        Phase 2: Tender Profile Establishment
                        Phase 3: Candidate Manifest Construction (AV-005–011)
                        Phase 4: Gate Checks (AV-001–004, AV-012–013)
                        Phase 5: Cross-Library Validation (CLV-001–012)
                        Phase 6: Library-Specific Validation (LV-)
                        Phase 7: Manifest Finalisation
                        Phase 8: Report Generation
                        END (manifest + validation report)
```

### 6.2 Failure Handling

| Condition | Engine Behaviour |
|---|---|
| BLOCK rule fires during Phase 1 (RI-001, RI-008, RI-009) | Halt immediately. Do not proceed to subsequent phases. Report includes: rule code, description, affected asset IDs, remediation steps. Manifest is not produced. |
| BLOCK rule fires during Phase 3–6 | Record BLOCK condition. Continue evaluating remaining rules. At Phase 7, if any BLOCK exists, manifest_status = BLOCKED. Manifest is produced but marked BLOCKED. Assembly Engine must not consume a BLOCKED manifest. |
| ERROR rule fires | Record ERROR condition. Affected asset is removed from manifest. Continue. |
| WARNING rule fires | Record WARNING condition. Affected asset remains in manifest with validation_flags entry. Continue. |
| Registry file not found | Fatal error. Engine cannot start. Report: "Registry file not found at [path]. Run registry population before validation." |
| Tender context missing (Mode 2) | Fatal error. Engine cannot start in Mode 2. Report: "Tender context required for assembly validation. Provide tender_context.yaml." |
| Rule evaluation error (unexpected) | Log technical error for that rule. Continue with remaining rules. Include in report under "Engine Errors" section. |

### 6.3 Determinism Guarantee

The KVE is deterministic under these conditions:
- Same registry YAML file version
- Same tender context (Mode 2)
- Same validation rules version

The engine has no random elements, no date-sensitive logic except review_due comparisons (which use the current date), and no external lookups. A validation run can be exactly reproduced from its inputs.

---

## 7. Engine Components

### 7.1 Registry Loader

**Responsibility:** Load and parse KNOWLEDGE_ASSET_REGISTRY.yaml and KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml into memory. Validate YAML syntax. Build an in-memory index keyed by asset_id.

**Failure condition:** If the YAML is malformed, report syntax error and halt. Do not attempt partial loading.

**Output data structure:**
```
registry_index: Dict[asset_id → registry_entry]
assumptions_index: Dict[asset_id → assumption_entry]
registry_metadata: { registry_version, asset_count, last_sync }
```

### 7.2 Rule Engine

**Responsibility:** Execute all applicable validation rules in the defined order. Return a list of rule results (each with: rule_code, severity, asset_id, passed, message, recommended_action).

**Design:** Each rule is an independent, named function. Rules are composed into phases. Phases execute sequentially. Within a phase, rules execute in rule-code order (RI-001 before RI-002, etc.). A BLOCK result within Phase 1 halts the engine. A BLOCK result in later phases is recorded but does not halt the phase — all rules in the phase are evaluated.

**Rule function signature:**
```
rule_RI_001(registry_index) → RuleResult(rule_code, severity, passed, affected_ids, message)
rule_AV_008(registry_index, manifest, tender_context) → RuleResult
```

### 7.3 Manifest Builder (Mode 2 only)

**Responsibility:** Construct the assembly manifest from the registry entries that pass the AV- filter rules. Start with all APPROVED assets, apply AV-005/006/007 to filter, apply AV-008 to add mandatory assets, apply AV-009/010 to remove excluded assets. Output is the candidate manifest before gate checks.

### 7.4 Health Score Calculator (Mode 1 only)

**Responsibility:** Calculate the Knowledge Health Score (0–100) from the rule results. See KNOWLEDGE_HEALTH_SCORE.md for scoring model.

### 7.5 Report Generator

**Responsibility:** Produce both Markdown (human-readable) and YAML (machine-readable) outputs. For Mode 1: health report + score. For Mode 2: validation report + assembly manifest. Report format defined in KNOWLEDGE_VALIDATION_REPORT_STANDARD.md.

---

## 8. Blocking Rules — Summary

The 22 BLOCK rules that halt or mark manifests as BLOCKED are, in evaluation order:

**Registry Integrity (run in Phase 1 — engine halt if violated):**

| Rule | Trigger |
|---|---|
| RI-001 | Duplicate asset IDs |
| RI-008 | Circular supersession chain |
| RI-009 | Circular parent-child chain |

**Governance Consistency (run in Phase 1 — recorded, continue):**

| Rule | Trigger |
|---|---|
| RI-011 | DRAFT asset has approved_for_reuse = true |
| RI-012 | ARCHIVED asset has approved_for_reuse = true |

**Assembly Gate (Phase 4):**

| Rule | Trigger |
|---|---|
| AV-001 | approved_for_reuse = false in manifest |
| AV-002 | Non-APPROVED asset in manifest (mandatory) |
| AV-004 | ARCHIVED asset in manifest |
| AV-008 | Mandatory asset absent from manifest |
| AV-009 | Excluded asset present (mandatory) |
| AV-010 | mandatory_if AND excluded_if both TRUE |
| AV-011 | RC-OPS-001 absent from non-P10 proposal |

**Cross-Library (Phase 5):**

| Rule | Trigger |
|---|---|
| CLV-001 | approved_for_reuse = false |
| CLV-002 | Lifecycle state ≠ APPROVED |
| CLV-007 | SUPERSEDED/ARCHIVED in manifest |
| CLV-008 | REF without AM clearance |

**Library-Specific (Phase 6):**

| Rule | Trigger |
|---|---|
| LV-ASM-001 | ASM has no parent pack |
| LV-ASM-002 | ASM parent not APPROVED |
| LV-ASP-002 | ASP has pending decisions |
| LV-RSK-004 | RC-OPS-001 not unconditional |
| LV-RSK-008 | DRAFT RSK in manifest |
| LV-REF-001 | REF without AM clearance |

---

## 9. Reporting Model

See KNOWLEDGE_VALIDATION_REPORT_STANDARD.md for the complete report format specification.

**Report structure summary:**

```
VALIDATION_REPORT / HEALTH_REPORT
│
├── Header (tender_id / registry_version / timestamp / mode)
├── Summary (manifest_status / health_score / blocks / errors / warnings)
├── BLOCK conditions (list: rule_code / asset_id / description / action)
├── ERROR conditions (list: rule_code / asset_id / description / action)
├── WARNING conditions (list: rule_code / asset_id / description)
├── Asset Health (per-asset lifecycle / metadata / relationship status)
│   ├── Orphan assets (assets with no relationships declared)
│   ├── Missing relationships (declared but unresolvable)
│   └── Metadata failures (mandatory fields missing)
├── Health Score Breakdown (Mode 1 only)
│   ├── Dimension scores (7 dimensions, 0–100 each)
│   └── Weighted total (0–100)
└── Recommendations (prioritised remediation steps)
```

---

## 10. Integration with the Proposal Factory Pipeline

The KVE integrates into the 10-stage pipeline at Stage 0 (TIL) and before Stage 4 (Capability Selection).

```
Stage 0: Tender Intelligence Layer
    └── TIL-08 Block G → invokes KVE in Mode 2
            └── KVE produces: Assembly Manifest + Validation Report
                    
Stage 1: Analysis (reads Validation Report — checks for BLOCKs)
    └── If BLOCKED → stop pipeline, escalate to BU Lead
    └── If VALID or APPROVED_WITH_CONDITIONS → proceed

Stage 4: Capability Selection
    └── Reads Assembly Manifest (not registry) — selects from certified CAP list
    
Stage 5: Reference Selection
    └── Reads Assembly Manifest — selects from certified REF list
    
Stage 6: Methodology Selection
    └── Reads Assembly Manifest — selects from certified MTH list
    
Stage 7: Assumption Assembly
    └── Reads Assembly Manifest — loads ASP/ASM from certified list
    
Stage 8: Proposal Assembly (RSK, remaining assets)
    └── Reads Assembly Manifest — no registry access needed
    
Stage 9: Proposal QA Engine (future — WP18D+)
    └── Reads Validation Report for context
```

**Key integration rule:** No downstream engine (Stage 4–8) reads the Registry directly. All engines read only from the certified Assembly Manifest produced by the KVE. This is enforced by convention in the current implementation; in a future automated implementation, the registry file should be access-controlled.

---

## 11. Engine Reusability

The KVE is designed to be usable outside the Proposal Factory context. Its inputs (a YAML registry + optional context) and outputs (YAML reports) are format-neutral. Potential reuse scenarios:

- **Annual library audit**: Run Mode 1 to produce a health report for BU Lead review
- **Pre-tender check**: Run Mode 2 to confirm an asset set is valid before a proposal kickoff
- **Governance programme tracking**: Track health score over time as governance decisions are applied
- **New library integration**: Run Mode 1 after adding a new asset type to verify no new violations
- **Compliance audit**: Provide the YAML validation report as evidence of governance state

---

## 12. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-27 | WP18D | Initial architecture specification — two modes, 7 components, 22 BLOCK rules, pipeline integration, engine reusability |
