---
document_id: VALIDATION-RULE-EXECUTION-MODEL-V1
title: "Validation Rule Execution Model — V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-27"
created_by: "WP18D — Knowledge Validation Engine"
approved_by: "Architecture — WP18D"
approved_date: "2026-06-27"
approved_for_reuse: true
category: "Assembly Engine / Validation"
scope: "Converts the 76 validation rules defined in KNOWLEDGE_REGISTRY_VALIDATION_RULES.md into a complete executable model — specifying execution order, input data requirements, dependency chains, pseudocode conditions, PASS/WARN/BLOCK criteria, and execution flow for each rule series."
governing_standard: "KNOWLEDGE_REGISTRY_VALIDATION_RULES.md V1.0"
related_documents:
  - KNOWLEDGE_VALIDATION_ENGINE.md
  - KNOWLEDGE_REGISTRY_VALIDATION_RULES.md
  - KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md
---

# Validation Rule Execution Model — V1.0

**Work Package:** WP18D  
**Status:** APPROVED

This document is the implementation specification for the Knowledge Validation Engine Rule Engine component (KNOWLEDGE_VALIDATION_ENGINE.md §7.2). It converts each of the 76 rules into executable pseudocode with explicit input requirements and PASS/WARN/BLOCK criteria.

---

## 1. Execution Context Data Structures

Before any rules execute, the Rule Engine must have these data structures populated:

```
# Built by Registry Loader
registry        : Dict[str → RegistryEntry]     # all core entries, keyed by asset_id
assumptions     : Dict[str → RegistryEntry]     # all ASM entries, keyed by asset_id
all_asset_ids   : Set[str]                       # union of registry.keys() + assumptions.keys()
registry_meta   : { registry_version, asset_count, last_sync }

# Built by Tender Profile Establishment (Mode 2 only)
context         : {
  tender_id, pattern, platform, engagement_type,
  modules[], country, client_size, client_sector,
  am_clearances[], ptc_clearances[]
}

# Built by Manifest Builder (Mode 2 only, after Phase 3)
manifest        : Dict[str → RegistryEntry]     # filtered and mandatory assets
```

---

## 2. Phase 1 — Registry Integrity (RI-001 to RI-015)

**Runs in:** Both modes  
**Inputs:** `registry`, `assumptions`, `all_asset_ids`  
**Execution:** Sequential — RI-001 first. If RI-001 fires: **halt engine immediately**. RI-008 or RI-009 fire: **halt engine immediately**. All other RI rules: record result and continue.

### Execution Flow — Phase 1

```
PHASE 1 START
│
├── RI-001: Check for duplicate asset_ids
│     IF any asset_id appears >1 time in all_asset_ids → BLOCK → ENGINE HALT
│
├── RI-002: Validate asset_type values
│     FOR each entry in registry + assumptions:
│       IF asset_type NOT IN {CAP,ASP,ASM,RSK,MTH,REF,PPT,PRT,CON,COM,PAT,SEC}
│         → ERROR(entry.asset_id)
│
├── RI-003: Validate lifecycle_status values
│     FOR each entry:
│       IF lifecycle_status NOT IN {DRAFT,NORMALISED,READY_FOR_REVIEW,
│          AUTO_APPROVED,REVIEW_REQUIRED,APPROVED,SUPERSEDED,ARCHIVED}
│         → ERROR(entry.asset_id)
│
├── RI-004: Validate source_file paths resolve
│     FOR each entry:
│       IF NOT file_exists(entry.source_file) → WARNING(entry.asset_id)
│
├── RI-005: Validate related_assets references
│     FOR each entry:
│       FOR each ref_id IN entry.related_assets:
│         IF ref_id NOT IN all_asset_ids → WARNING(entry.asset_id, ref_id)
│
├── RI-006: Validate supersedes references
│     FOR each entry WHERE entry.supersedes != "":
│       IF entry.supersedes NOT IN all_asset_ids → ERROR(entry.asset_id)
│
├── RI-007: Validate superseded_by references
│     FOR each entry WHERE entry.superseded_by != "":
│       IF entry.superseded_by NOT IN all_asset_ids → ERROR(entry.asset_id)
│
├── RI-008: Check for circular supersession chains
│     Build supersession graph. Run cycle detection (DFS).
│     IF any cycle exists → BLOCK → ENGINE HALT
│
├── RI-009: Check for circular parent-child chains
│     Build parent-child graph from asm_ext.parent_pack_id.
│     Run cycle detection (DFS).
│     IF any cycle exists → BLOCK → ENGINE HALT
│
├── RI-010: Validate approved_for_reuse consistency
│     FOR each entry:
│       IF approved_for_reuse = true AND lifecycle_status != APPROVED
│         → ERROR(entry.asset_id)
│
├── RI-011: DRAFT cannot be approved_for_reuse
│     FOR each entry:
│       IF approved_for_reuse = true AND lifecycle_status = DRAFT
│         → BLOCK(entry.asset_id)
│
├── RI-012: ARCHIVED cannot be approved_for_reuse
│     FOR each entry:
│       IF approved_for_reuse = true AND lifecycle_status = ARCHIVED
│         → BLOCK(entry.asset_id)
│
├── RI-013: SUPERSEDED cannot be approved_for_reuse
│     FOR each entry:
│       IF approved_for_reuse = true AND lifecycle_status = SUPERSEDED
│         → ERROR(entry.asset_id)
│
├── RI-014: Mandatory fields present
│     MANDATORY_FIELDS = [asset_id, asset_type, title, version, source_file,
│       lifecycle_status, approved_for_reuse, owner_role, owner_business_unit,
│       approval_authority, governing_standard, registry_version_added,
│       created, created_by, governance_notes, pattern_applicability, proposal_sections]
│     FOR each entry:
│       FOR each field IN MANDATORY_FIELDS:
│         IF entry[field] is None OR entry[field] = "" OR entry[field] = []
│           → ERROR(entry.asset_id, field)
│
└── RI-015: Extension block present for typed assets
      TYPED_ASSETS = {CAP, ASP, ASM, RSK, MTH, REF, PAT, SEC}
      EXTENSION_BLOCKS = {CAP:"cap_ext", ASP:"asp_ext", ASM:"asm_ext",
                          RSK:"rsk_ext", MTH:"mth_ext", REF:"ref_ext",
                          PAT:"pat_ext", SEC:"sec_ext"}
      FOR each entry WHERE entry.asset_type IN TYPED_ASSETS:
        ext_key = EXTENSION_BLOCKS[entry.asset_type]
        IF ext_key NOT IN entry OR entry[ext_key] is None
          → WARNING(entry.asset_id)

PHASE 1 END
  → Aggregate RI rule results
  → If any BLOCK (RI-011, RI-012 only in this phase) → record but continue to Phase 2
  → Engine halted only if RI-001, RI-008, RI-009 fired
```

**PASS criteria:** All 15 RI rules produce no BLOCK, no ERROR, no WARNING  
**WARN criteria:** Only WARNING results (RI-004, RI-005, RI-015)  
**BLOCK criteria:** Any of RI-001, RI-008, RI-009 fire → engine halt

---

## 3. Phase 2 — Tender Profile Establishment (Mode 2 Only)

**Runs in:** Mode 2 (Assembly Validation) only  
**Inputs:** `tender_context.yaml`  
**Output:** Validated `context` object

```
PHASE 2 START
│
├── Load tender_context.yaml
├── Validate required fields present: [tender_id, pattern, platform, engagement_type]
│     IF any missing → FATAL ERROR (engine cannot proceed in Mode 2)
│
├── Validate pattern IN {P1,...,P13}
│     IF invalid → FATAL ERROR
│
├── Validate platform IN {Oracle HCM Cloud, Oracle Fusion ERP, Acumatica, BeBanking}
│     IF invalid → FATAL ERROR
│
├── Set defaults for optional fields:
│     modules = [] if absent
│     country = "RSA" if absent
│     client_size = "Enterprise" if absent
│     client_sector = "All" if absent
│     am_clearances = [] if absent
│     ptc_clearances = [] if absent
│
└── Store as context object

PHASE 2 END
  → context object available for Phases 3–6
```

---

## 4. Phase 3 — Candidate Manifest Construction (Mode 2 Only)

**Runs in:** Mode 2 only  
**Inputs:** `registry`, `assumptions`, `context`  
**Output:** `manifest` (initial candidate set before gate checks)

```
PHASE 3 START: Build candidate set
│
├── AV-005: Pattern applicability filter
│     FOR each entry in registry + assumptions:
│       IF context.pattern IN entry.pattern_applicability
│         OR "ALL" IN entry.pattern_applicability
│         → INCLUDE in candidates
│       ELSE → EXCLUDE (silent — not an error, just not applicable)
│
├── AV-006: Platform applicability filter (CAP assets only)
│     FOR each CAP entry in candidates:
│       IF entry.cap_ext.platform != context.platform
│         AND entry.cap_ext.platform != "Cross-Platform"
│         → ERROR(entry.asset_id) + REMOVE from candidates
│
├── AV-007: Engagement type filter (ASP assets only)
│     FOR each ASP entry in candidates:
│       IF context.engagement_type NOT IN entry.asp_ext.applicable_engagement_types
│         AND entry.asp_ext.applicable_engagement_types != ["All"]
│         → ERROR(entry.asset_id) + REMOVE ASP and all child ASMs from candidates
│
├── AV-008: Add mandatory assets
│     FOR each entry in registry + assumptions:
│       IF entry NOT IN candidates:
│         IF evaluate_expression(entry.assembly_rules.mandatory_if, context) = TRUE
│           → ADD to candidates (mandatory asset)
│           → Mark as MANDATORY in manifest
│           → If entry.approved_for_reuse = false → BLOCK (AV-001 will fire in Phase 4)
│
├── AV-009: Remove excluded assets
│     FOR each entry in candidates:
│       IF evaluate_expression(entry.assembly_rules.excluded_if, context) = TRUE
│         → REMOVE from candidates
│         IF entry.assembly_rules.mandatory_if also evaluates TRUE
│           → Do NOT remove (AV-010 will fire in Phase 4 — conflict)
│           → Instead: mark as CONFLICT
│
├── AV-010: Flag mandatory-excluded conflicts
│     FOR each entry with CONFLICT flag:
│       → BLOCK(entry.asset_id) — cannot be both mandatory and excluded
│
├── AV-011: RC-OPS-001 unconditional check
│     IF context.pattern != "P10":
│       IF "RC-OPS-001" NOT IN candidates
│         → BLOCK — mandatory risk missing
│
└── Build manifest from candidates list

PHASE 3 END
  → manifest: initial candidate set
  → All AV-005–011 results recorded
```

**Expression evaluator:**  
`evaluate_expression(expr, context)` evaluates the mandatory_if / optional_if / excluded_if string against the context object. For the current platform, this is a simple variable-substitution and comparison evaluator:
- `"platform IN ['Oracle HCM Cloud']"` → evaluates to boolean
- `"TRUE"` → always true
- `"FALSE"` → always false
- `""` → false (no condition — not mandatory, not excluded)

---

## 5. Phase 4 — Gate Checks on Manifest (Mode 2 Only)

**Runs in:** Mode 2 only  
**Inputs:** `manifest`, `context`

```
PHASE 4 START
│
├── AV-001: approved_for_reuse gate
│     FOR each entry in manifest:
│       IF entry.approved_for_reuse = false
│         → BLOCK(entry.asset_id)
│         → REMOVE from manifest (but record BLOCK)
│
├── AV-002: Lifecycle gate
│     FOR each entry in manifest:
│       IF entry.lifecycle_status != APPROVED
│         → BLOCK(entry.asset_id) — if entry is MANDATORY
│         → ERROR(entry.asset_id) — if entry is optional
│         → REMOVE from manifest
│
├── AV-003: SUPERSEDED asset gate
│     FOR each entry in manifest:
│       IF entry.lifecycle_status = SUPERSEDED
│         successor_id = entry.superseded_by
│         IF successor_id != "" AND successor_id IN registry
│           AND registry[successor_id].lifecycle_status = APPROVED
│           → Replace entry with successor in manifest
│           → WARNING: "Replaced SUPERSEDED asset [id] with successor [successor_id]"
│         ELSE
│           → ERROR(entry.asset_id) + REMOVE
│
├── AV-004: ARCHIVED asset gate
│     FOR each entry in manifest:
│       IF entry.lifecycle_status = ARCHIVED
│         → BLOCK(entry.asset_id) + REMOVE from manifest
│
├── AV-012: Review overdue
│     today = current_date()
│     FOR each entry in manifest:
│       IF entry.review_due != "" AND parse_date(entry.review_due) < today
│         → WARNING(entry.asset_id): "Review overdue since [date]"
│
└── AV-013: Annual review critically overdue (CAP only)
      FOR each CAP entry in manifest:
        IF entry.cap_ext.annual_review_obligation = true
          AND entry.review_due != ""
          AND (today - parse_date(entry.review_due)).days > 90
            → ERROR(entry.asset_id): "Annual review >90 days overdue"
            → REMOVE from manifest

PHASE 4 END
  → manifest updated (removed blocked/errored assets)
  → If any BLOCK recorded → manifest_status will be BLOCKED at Phase 7
```

---

## 6. Phase 5 — Cross-Library Validation (Both Modes, Manifest in Mode 2 / Full Registry in Mode 1)

**Runs in:** Both modes  
**Mode 1:** Evaluate CLV-003 and CLV-004 only (relationship resolution), against full registry  
**Mode 2:** Evaluate all CLV-001–CLV-012, against manifest

```
PHASE 5 START (Mode 2)
│
├── CLV-001: Approved-for-Reuse gate (redundant with AV-001 — belt-and-braces)
│     FOR each entry in manifest:
│       IF entry.approved_for_reuse = false → BLOCK
│
├── CLV-002: Lifecycle gate (redundant with AV-002 — belt-and-braces)
│     FOR each entry in manifest:
│       IF entry.lifecycle_status != APPROVED → BLOCK
│
├── CLV-003: Related assets resolve
│     FOR each entry in manifest:
│       FOR each ref_id IN entry.related_assets:
│         IF ref_id NOT IN all_asset_ids → WARNING(entry.asset_id, ref_id)
│
├── CLV-004: Source assets resolve
│     FOR each entry in manifest:
│       FOR each ref_id IN entry.source_assets:
│         IF ref_id NOT IN all_asset_ids → WARNING(entry.asset_id, ref_id)
│
├── CLV-005: Pre-tender controls satisfied (CAP only)
│     FOR each CAP entry in manifest:
│       FOR each control IN entry.cap_ext.pre_tender_controls:
│         IF entry.asset_id NOT IN context.ptc_clearances
│           → ERROR(entry.asset_id): "Pre-tender control not cleared"
│           → REMOVE from manifest
│
├── CLV-006: Risk-assumption cross-reference (RSK only)
│     FOR each RSK entry in manifest:
│       FOR each asm_id IN entry.rsk_ext.related_assumptions:
│         IF asm_id NOT IN assumptions
│           OR assumptions[asm_id].lifecycle_status != APPROVED
│           → WARNING(entry.asset_id, asm_id)
│
├── CLV-007: SUPERSEDED/ARCHIVED blocking
│     FOR each entry in manifest:
│       IF entry.lifecycle_status IN {SUPERSEDED, ARCHIVED}
│         → BLOCK(entry.asset_id) + REMOVE from manifest
│
├── CLV-008: REF account manager clearance
│     FOR each REF entry in manifest:
│       IF entry.ref_ext.account_manager_required = true
│         AND entry.asset_id NOT IN context.am_clearances
│           → BLOCK(entry.asset_id) + REMOVE from manifest
│
├── CLV-009: Pack scope compatibility (ASP only)
│     FOR each ASP entry in manifest:
│       IF entry.asp_ext.platform != context.platform
│         AND entry.asp_ext.platform != "All"
│           → ERROR(entry.asset_id) + REMOVE ASP and child ASMs
│
├── CLV-010: CAP sector restriction
│     FOR each CAP entry in manifest:
│       IF context.client_sector NOT IN entry.cap_ext.sector
│         AND "All" NOT IN entry.cap_ext.sector
│           → ERROR(entry.asset_id) + REMOVE from manifest
│
├── CLV-011: S-50 priority order (RSK only)
│     rsk_in_manifest = [e for e in manifest if e.asset_type = RSK]
│     Sort rsk_in_manifest by assembly_priority: CRITICAL → HIGH → MEDIUM → LOW
│     IF current order != sorted order → WARNING: "S-50 risk ordering defect"
│
└── CLV-012: Supersession chain complete
      FOR each entry in manifest WHERE entry.superseded_by != "":
        succ_id = entry.superseded_by
        IF succ_id NOT IN all_asset_ids
          OR registry[succ_id].lifecycle_status != APPROVED
          → ERROR(entry.asset_id): "Broken supersession chain"
          + REMOVE from manifest

PHASE 5 END
  → manifest updated
  → All CLV results recorded
```

---

## 7. Phase 6 — Library-Specific Validation

**Runs in:** Both modes (against manifest in Mode 2, against full registry in Mode 1)  
**Execution order within phase:** PAT → SEC → ASP → ASM → CAP → RSK → REF → MTH

### LV-PAT- Rules

```
LV-PAT-001: BOM reference declared
  FOR each PAT entry:
    IF entry.pat_ext.bom_reference = "" → WARNING

LV-PAT-002: Typical sections declared
  FOR each PAT entry:
    IF entry.pat_ext.typical_sections = [] → ERROR + flag

LV-PAT-003: All 13 patterns registered
  pat_count = count(e for e in registry if e.asset_type = PAT
                    AND e.lifecycle_status = APPROVED)
  IF pat_count < 13 → ERROR: "Only [n]/13 patterns registered as APPROVED"
```

### LV-SEC- Rules

```
LV-SEC-001: Automation type declared
  FOR each SEC entry:
    VALID_TYPES = {DIRECT, EXTRACT, MERGE, AI-GENERATE, TEMPLATE, PLACEHOLDER}
    IF entry.sec_ext.automation_type NOT IN VALID_TYPES → ERROR + REMOVE from manifest

LV-SEC-002: Content source assets declared
  FOR each SEC entry WHERE automation_type IN {DIRECT, EXTRACT}:
    IF entry.sec_ext.content_source_assets = [] → WARNING

LV-SEC-003: PLACEHOLDER sections flagged
  FOR each SEC entry WHERE automation_type = PLACEHOLDER:
    → WARNING: "Section [id] will appear blank in proposal output"

LV-SEC-004: Mandatory pattern coverage
  FOR each PAT entry in manifest:
    FOR each sec_id IN entry.pat_ext.typical_sections:
      IF sec_id NOT IN all_asset_ids → ERROR: "Section [sec_id] referenced by PAT [pat_id] not in registry"
```

### LV-ASP- Rules

```
LV-ASP-001: Pack has child assumptions
  FOR each ASP entry:
    children = [e for e in assumptions if e.asm_ext.parent_pack_id = entry.asset_id]
    IF len(children) = 0 → ERROR + REMOVE from manifest

LV-ASP-002: No pending decisions
  FOR each ASP entry:
    IF entry.asp_ext.pending_decisions > 0
      → BLOCK: "[n] pending decisions in pack [id]" + BLOCK ASP use

LV-ASP-003: Pack code matches ID
  FOR each ASP entry:
    IF entry.asp_ext.pack_code != entry.asset_id → ERROR

LV-ASP-004: Section codes declared
  FOR each ASP entry:
    IF entry.asp_ext.section_codes = [] → WARNING
```

### LV-ASM- Rules

```
LV-ASM-001: Exactly one parent pack
  FOR each ASM entry:
    IF entry.asm_ext.parent_pack_id = "" → BLOCK + REMOVE

LV-ASM-002: Parent pack exists and is approved
  FOR each ASM entry:
    pack_id = entry.asm_ext.parent_pack_id
    IF pack_id NOT IN registry
      OR registry[pack_id].lifecycle_status != APPROVED
        → BLOCK + REMOVE

LV-ASM-003: mandatory_if declared
  FOR each ASM entry:
    IF entry.assembly_rules.mandatory_if = "" → WARNING

LV-ASM-004: Assumption text populated
  FOR each ASM entry:
    IF entry.asm_ext.assumption_text = "" → ERROR + REMOVE

LV-ASM-005: Section code declared
  FOR each ASM entry:
    IF entry.asm_ext.section_code = "" → ERROR + REMOVE
```

### LV-CAP- Rules

```
LV-CAP-001: Proposal section declared
  FOR each CAP entry:
    IF entry.proposal_sections = [] → ERROR + REMOVE

LV-CAP-002: Evidence tier populated
  FOR each CAP entry:
    IF entry.cap_ext.evidence_tier = "" → WARNING

LV-CAP-003: Pattern applicability non-empty
  FOR each CAP entry:
    IF entry.pattern_applicability = [] → ERROR + REMOVE

LV-CAP-004: Annual review date set
  FOR each CAP entry:
    IF entry.cap_ext.annual_review_obligation = true AND entry.review_due = ""
      → WARNING

LV-CAP-005: Content source type valid
  FOR each CAP entry:
    VALID = {DIRECT, EXTRACT, MERGE, AI-GENERATE, TEMPLATE, PLACEHOLDER}
    IF entry.assembly_rules.content_source_type NOT IN VALID → ERROR + REMOVE
```

### LV-RSK- Rules

```
RATING_MATRIX = {
  (Low, Low): LOW, (Low, Medium): LOW, (Low, High): MEDIUM,
  (Medium, Low): LOW, (Medium, Medium): MEDIUM, (Medium, High): HIGH,
  (High, Low): MEDIUM, (High, Medium): HIGH, (High, High): CRITICAL
}

LV-RSK-001: Net rating consistent
  FOR each RSK entry:
    expected = RATING_MATRIX[(entry.rsk_ext.likelihood, entry.rsk_ext.impact)]
    IF entry.rsk_ext.net_rating != expected → ERROR: "Rating inconsistency"

LV-RSK-002: Related assumptions declared
  FOR each RSK entry WHERE rsk_ext.governance_category != "G" (governance):
    IF entry.rsk_ext.related_assumptions = [] → WARNING

LV-RSK-003: mandatory_if_engagement declared
  FOR each RSK entry:
    IF entry.rsk_ext.mandatory_if_engagement = "" → ERROR + REMOVE

LV-RSK-004: RC-OPS-001 is unconditional
  rc_ops = registry.get("RC-OPS-001")
  IF rc_ops AND rc_ops.rsk_ext.mandatory_if_engagement != "TRUE"
    → BLOCK: "RC-OPS-001 must be unconditional"

LV-RSK-005: Proposal section declared
  FOR each RSK entry:
    IF entry.proposal_sections = [] → ERROR + REMOVE

LV-RSK-006: Governance category declared
  FOR each RSK entry:
    IF entry.rsk_ext.governance_category = "" → WARNING

LV-RSK-007: Category B has decision reference
  FOR each RSK entry WHERE rsk_ext.governance_category = "B":
    IF entry.rsk_ext.governance_decision_ref = "" → ERROR

LV-RSK-008: DRAFT risk not assembled
  FOR each RSK entry in manifest:
    IF entry.lifecycle_status = DRAFT → BLOCK + REMOVE
```

### LV-REF- Rules

```
LV-REF-001: Account manager clearance (belt-and-braces with CLV-008)
  FOR each REF entry in manifest:
    IF entry.ref_ext.account_manager_required = true
      AND entry.asset_id NOT IN context.am_clearances
        → BLOCK + REMOVE

LV-REF-002: Signed date populated
  FOR each REF entry:
    IF entry.ref_ext.signed_date = "" → ERROR + REMOVE

LV-REF-003: Letter on file
  FOR each REF entry:
    IF entry.ref_ext.letter_on_file = false → WARNING

LV-REF-004: Restrictions checked
  FOR each REF entry:
    IF entry.ref_ext.restrictions != "" → WARNING: "[restrictions text] — review before use"
```

### LV-MTH- Rules

```
LV-MTH-001: Platform declared
  FOR each MTH entry:
    IF entry.mth_ext.applicable_platforms = [] → ERROR + REMOVE

LV-MTH-002: Phase structure declared
  FOR each MTH entry:
    IF entry.mth_ext.phase_structure = [] → WARNING

LV-MTH-003: One methodology per platform
  platform_to_mth = {}
  FOR each MTH entry WHERE lifecycle_status = APPROVED:
    FOR each platform IN entry.mth_ext.applicable_platforms:
      IF platform IN platform_to_mth → ERROR: "Multiple APPROVED methodologies for [platform]"
      ELSE platform_to_mth[platform] = entry.asset_id
```

---

## 8. Phase 7 — Manifest Finalisation (Mode 2 Only)

```
PHASE 7 START
│
├── Collect all BLOCK conditions from phases 1–6
│
├── Determine manifest_status:
│     IF blocks > 0 → manifest_status = BLOCKED
│     ELSE IF errors > 0 → manifest_status = APPROVED_WITH_CONDITIONS
│     ELSE → manifest_status = VALID
│
├── Set manifest.proceed:
│     IF manifest_status = BLOCKED → proceed = false
│     ELSE → proceed = true
│
├── Apply S-50 ordering to RSK assets in manifest:
│     Sort RSK entries by assembly_priority: CRITICAL first, then HIGH, MEDIUM, LOW
│
└── Stamp manifest:
      manifest.manifest_timestamp = current_timestamp()
      manifest.registry_version = registry_meta.registry_version
      manifest.blocks = count(BLOCK results)
      manifest.errors = count(ERROR results)
      manifest.warnings = count(WARNING results)

PHASE 7 END → manifest finalised
```

---

## 9. Phase 8 — Report Generation

```
PHASE 8 START
│
├── Aggregate rule results: group by severity (BLOCK / ERROR / WARNING)
│
├── Build per-asset health summary:
│     FOR each entry in registry:
│       asset_health[asset_id] = {
│         metadata_complete: (no RI-014 violations),
│         lifecycle_valid: (no RI-010/011/012/013 violations),
│         relationships_resolved: (no RI-005/CLV-003/004 violations),
│         validation_flags: [list of rule codes that fired for this asset]
│       }
│
├── Generate YAML report (VALIDATION_REPORT_[tender_id].yaml or HEALTH_REPORT_[date].yaml)
│
├── Generate Markdown report (human-readable)
│
└── If Mode 1: Calculate Health Score (see KNOWLEDGE_HEALTH_SCORE.md)

PHASE 8 END
```

---

## 10. Rule Dependency Graph

Not all rules are independent. The following dependencies must be respected:

| Rule | Depends On | Reason |
|---|---|---|
| AV-005–011 | RI-001 passed | Cannot filter by asset_id if IDs are not unique |
| AV-001–004 | AV-005–011 | Gate checks run on the filtered manifest |
| CLV-001–012 | AV-001–004 | Cross-library runs on the gated manifest |
| LV- rules | CLV-001–012 | Library rules run on the gated + cross-validated manifest |
| Phase 7 | All LV- rules | Finalisation needs complete picture of all violations |
| Health Score | Phase 6 complete | Score requires complete LV- results |
| AV-009 | AV-008 | Must know mandatory assets before applying excluded-asset rule |
| CLV-003/004 | RI-001 | Cannot check reference resolution with duplicate IDs |
| LV-ASM-002 | LV-ASP-001 | Parent pack must exist before checking its approval |

---

## 11. Execution Timing Estimates

Based on expected registry size (1,325 entries):

| Phase | Operation | Estimated Time |
|---|---|---|
| Registry Load | Parse YAML, build index | <1 second |
| Phase 1 (RI) | 15 rules × 1,325 entries | <2 seconds |
| Phase 2 (Profile) | Parse tender context | <0.1 seconds |
| Phase 3 (AV filter) | 7 rules × 1,325 entries | <2 seconds |
| Phase 4 (AV gates) | 6 rules × filtered manifest (~200 entries) | <1 second |
| Phase 5 (CLV) | 12 rules × 200 entries | <1 second |
| Phase 6 (LV) | 37 rules × 200 entries | <3 seconds |
| Phase 7 (Finalise) | Aggregation + ordering | <0.5 seconds |
| Phase 8 (Report) | Generate YAML + Markdown | <1 second |
| **Total** | | **<12 seconds** |

The engine should complete within 30 seconds even on worst-case input (full ASM registry). No optimisation is needed for the initial implementation.

---

## 12. Changelog

| Version | Date | Changes |
|---|---|---|
| 1.0 | 2026-06-27 | Initial execution model — all 76 rules in pseudocode; 8-phase flow; dependency graph; timing estimates |
