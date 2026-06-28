---
document_id: WP18D-VALIDATION-ENGINE-ARCHITECTURE-REPORT
title: "WP18D — Knowledge Validation Engine: Architecture Report"
version: "1.0"
status: "COMPLETE"
created: "2026-06-27"
created_by: "WP18D — Knowledge Validation Engine"
approved_by: "Architecture — WP18D"
approved_date: "2026-06-27"
work_package: WP18D
---

# WP18D — Knowledge Validation Engine: Architecture Report

**Date:** 2026-06-27  
**Status:** COMPLETE — Architecture specification delivered. Implementation deferred to implementation work package.  
**Platform Maturity Impact:** L3.5 → L4.0 (on successful implementation)

---

## 1. Executive Summary

WP18D designed the Knowledge Validation Engine (KVE) — the deterministic validation layer that sits between the Universal Knowledge Asset Registry and the Proposal Assembly Engine. Five architecture documents were delivered, constituting a complete implementation specification.

The KVE is the "compiler" of the Proposal Platform: it validates the Knowledge Platform itself — not proposal content — before any assembly begins. Given a populated registry, a developer can implement the KVE from these documents without additional design work.

**Deliverables:**

| Document | Location | Purpose |
|---|---|---|
| KNOWLEDGE_VALIDATION_ENGINE.md | 08_Commercial/Assembly_Engine/ | Engine architecture — two modes, 7 components, integration, reusability |
| VALIDATION_RULE_EXECUTION_MODEL.md | 08_Commercial/Assembly_Engine/ | 76 rules in executable pseudocode — complete Phase 1–8 execution model |
| KNOWLEDGE_VALIDATION_REPORT_STANDARD.md | 08_Commercial/Assembly_Engine/ | Report formats — Assembly Validation, Platform Health, Assembly Manifest (YAML + MD) |
| KNOWLEDGE_HEALTH_SCORE.md | 08_Commercial/Assembly_Engine/ | 7-dimension 0–100 scoring model — formulas, weights, bands, current-state estimates |
| WP18D_VALIDATION_ENGINE_ARCHITECTURE.md | 08_Commercial/Reports/ | This document |

**Constraints compliance:**
- No registry entries created ✓
- No capability assets modified ✓
- No assumption packs modified ✓
- No governance standards redesigned ✓
- Architecture only ✓

---

## 2. Architecture Decisions

### 2.1 Two-Mode Engine (Platform Health + Assembly Validation)

**Decision:** The KVE operates in two distinct modes. Mode 1 (Platform Health) validates the full registry with no tender context. Mode 2 (Assembly Validation) validates the registry filtered to a specific tender profile and produces a certified assembly manifest.

**Rationale:** The user instruction specifies that the Validation Engine validates the Knowledge Platform itself, not just individual proposals. A single-mode engine that requires tender context cannot fulfil the platform health function. Separating modes keeps the purpose of each run unambiguous: Mode 1 is a periodic maintenance check; Mode 2 is a pre-assembly certification.

**Impact:** Mode 1 produces the Health Report and Health Score. Mode 2 produces the Assembly Manifest (the primary output consumed by downstream engines). Both use the same 76 rules; Mode 2 uses all of them, Mode 1 uses the subset applicable without tender context.

### 2.2 Stateless Sequential Rules Evaluator

**Decision:** The KVE is stateless. Each run loads the registry fresh, evaluates rules sequentially, and produces a complete self-contained report. No state is carried between runs.

**Rationale:** Statefulness creates consistency risks: a previous run's state could mask or exaggerate current violations. Statelessness guarantees that the report always reflects the current registry state, no history, no drift.

**Impact:** Runs are idempotent and reproducible. The same inputs always produce the same outputs. This is the "deterministic" property required by the governing brief.

### 2.3 BLOCK Rules Halt at Three Points Only

**Decision:** Three rules (RI-001, RI-008, RI-009) halt the engine immediately on violation. All other BLOCK rules are recorded and continue — the engine completes all phases before producing the report.

**Rationale:** RI-001 (duplicate IDs), RI-008 (circular supersession), and RI-009 (circular parent-child) make it impossible to safely evaluate any subsequent rule — the registry graph cannot be traversed. All other BLOCKs (e.g., LV-RSK-008: DRAFT risk in manifest) do not invalidate the engine's ability to evaluate remaining rules; it is more useful to report all BLOCKs in one run than to require iterative fixing.

**Impact:** A single validation run surfaces all issues simultaneously. The BU Lead sees the complete picture of what needs fixing, not one issue at a time.

### 2.4 7-Dimension Health Score with Weighted Average

**Decision:** The Knowledge Health Score (KHS) is composed of 7 weighted dimensions: Registry Integrity (25%), Lifecycle Compliance (20%), Approval Status (20%), Governance Compliance (15%), Metadata Completeness (10%), Relationship Integrity (5%), Validation Success (5%).

**Rationale:** Registry integrity and lifecycle/approval status dominate the score (65% combined) because a registry with structural defects or unapproved assets cannot safely drive assembly — these are load-bearing concerns. Metadata completeness and relationship integrity (15% combined) are important but not assembly-blocking on their own. The weighting reflects the severity hierarchy: structural integrity > governance state > metadata quality.

**Impact:** The score is directly actionable. Improving D3 (Approval Status) by completing WP18B-EXT.2 adds ~14 KHS points. Populating extension metadata adds ~5 points. Both improvements are estimable before they happen, which makes governance planning concrete.

### 2.5 Assembly Manifest as Primary Engine Output

**Decision:** The certified Assembly Manifest (ASSEMBLY_MANIFEST_[tender_id].yaml) is the primary output that downstream engines consume. The Validation Report is a companion document. No downstream engine reads the Registry directly.

**Rationale:** The manifest is the KVE's certification output. Downstream engines (TIL, Assembly Engine, QA Engine) consuming the manifest instead of the registry is what makes the platform's governance enforcement deterministic. The manifest has been filtered, gated, and certified. The registry is raw data.

**Impact:** This creates a clean interface boundary: the KVE owns the registry interface; all other engines own the manifest interface. Downstream engines can be implemented without knowledge of registry structure.

### 2.6 Pre-Tender Controls and AM Clearances as Explicit Inputs

**Decision:** Pre-tender control clearances (ptc_clearances.yaml) and account manager clearances (am_clearances.yaml) are explicit inputs to the engine in Mode 2, not derived from the registry.

**Rationale:** These clearances are human actions performed before assembly, not properties of assets. They cannot be stored in the registry (the registry is authoritative for asset governance state, not per-proposal human actions). Making them explicit inputs enforces that a human must actively provide them; their absence causes BLOCK.

**Impact:** CLV-005 (pre-tender controls) and CLV-008/LV-REF-001 (AM clearances) are the only BLOCK rules that require human action per tender, not per governance session. This aligns with the platform design: most governance is done once (in the registry); per-tender human actions are minimal and explicit.

---

## 3. Validation Model Summary

| Metric | Value |
|---|---|
| Total validation rules | 76 |
| BLOCK rules (halt or mark BLOCKED) | 22 |
| ERROR rules (asset removed, continue) | 29 |
| WARNING rules (asset flagged, continue) | 25 |
| Rule series | 11 (RI, AV, CLV, LV-CAP, LV-ASP, LV-ASM, LV-RSK, LV-MTH, LV-REF, LV-PAT, LV-SEC) |
| Execution phases | 8 (Mode 2) / 5 (Mode 1) |
| Engine-halt BLOCKs | 3 (RI-001, RI-008, RI-009) |
| Score dimensions | 7 |
| Score range | 0–100 |
| Score bands | 5 (CRITICAL / POOR / ADEQUATE / GOOD / EXCELLENT) |

---

## 4. Engine Component Map

```
Knowledge Validation Engine (KVE)
│
├── Registry Loader
│     Input:  KNOWLEDGE_ASSET_REGISTRY.yaml
│             KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml
│     Output: registry_index (Dict[asset_id → entry])
│             assumptions_index (Dict[asset_id → entry])
│             all_asset_ids (Set)
│
├── Rule Engine (sequential, 76 rules, 8 phases)
│     Phase 1: RI-001 to RI-015 (Registry Integrity)
│     Phase 2: Profile establishment (Mode 2 only)
│     Phase 3: AV-005–011 (Manifest construction, Mode 2)
│     Phase 4: AV-001–004, 012–013 (Gate checks, Mode 2)
│     Phase 5: CLV-001–012 (Cross-library, Mode 2 / CLV-003,004 Mode 1)
│     Phase 6: LV-* (Library-specific, both modes)
│     Phase 7: Manifest finalisation (Mode 2 only)
│     Phase 8: Report generation
│
├── Manifest Builder (Mode 2 only)
│     Input:  registry_index, context, AV- rule results
│     Output: manifest (certified asset list)
│
├── Health Score Calculator (Mode 1 only)
│     Input:  rule results from all phases
│     Output: KHS (0–100), 7 dimension scores
│             Per KNOWLEDGE_HEALTH_SCORE.md formulas
│
└── Report Generator
      Input:  rule results, manifest (Mode 2), health score (Mode 1)
      Output: YAML report + Markdown report
              Per KNOWLEDGE_VALIDATION_REPORT_STANDARD.md
```

---

## 5. Implementation Roadmap

### Phase A — Minimum Viable Engine (Priority: MVP)

**Deliverable:** An engine that runs the 22 BLOCK rules and produces a minimal validation report and assembly manifest.

**Scope:**
- Registry Loader (YAML parsing + index building)
- Rule Engine: RI-001, RI-008, RI-009 (engine-halt BLOCKs) + remaining 19 BLOCK rules
- Manifest Builder (AV-005–011 filter + AV-001–004 gate)
- Minimal Report Generator (manifest_status + BLOCK list only)

**Effort estimate:** 8–10 hours (AI-assisted)  
**Dependency:** Registry must be populated (at least PAT, ASP, CAP, RSK entries)  
**Gate:** Passes when ARM IT045 assembly run produces VALID or APPROVED_WITH_CONDITIONS manifest

### Phase B — Full Rule Engine

**Deliverable:** All 76 rules implemented and producing complete validation reports.

**Scope:**
- Complete all ERROR and WARNING rules
- CLV-001–012 full cross-library validation
- All 11 LV- series fully implemented
- Complete Markdown + YAML report generation

**Effort estimate:** 12–15 hours (AI-assisted)  
**Dependency:** Phase A complete; full registry populated (including ASM separate file)  
**Gate:** Full regression test — ARM IT045 produces clean report with expected BLOCK/ERROR/WARNING counts

### Phase C — Health Score and Mode 1

**Deliverable:** Platform Health Validation mode with KHS calculation.

**Scope:**
- Health Score Calculator (7 dimensions per KNOWLEDGE_HEALTH_SCORE.md)
- Mode 1 execution path (no tender context)
- Platform Health Report format
- Score trend tracking (previous run comparison)

**Effort estimate:** 5–7 hours (AI-assisted)  
**Dependency:** Phase B complete  
**Gate:** Health Report for current registry produces KHS ≥ 73 (ADEQUATE) pre-WP18B-EXT.2; ≥ 87 (GOOD) post-WP18B-EXT.2

**Total implementation effort: ~25–32 hours**

---

## 6. Implementation Readiness Assessment

| Component | Specification Complete | Dependency | Ready to Implement? |
|---|---|---|---|
| Registry Loader | Yes — schema in KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md | Registry populated | After population WP |
| Rule Engine — BLOCK rules | Yes — pseudocode in VALIDATION_RULE_EXECUTION_MODEL.md | Registry populated | After population WP |
| Rule Engine — ERROR/WARNING rules | Yes — pseudocode complete | Registry populated | After population WP |
| Manifest Builder | Yes — schema in KNOWLEDGE_VALIDATION_REPORT_STANDARD.md §7 | Registry populated | After population WP |
| Health Score Calculator | Yes — formulas in KNOWLEDGE_HEALTH_SCORE.md | Phase B complete | After Phase B |
| Report Generator (YAML) | Yes — schema in KNOWLEDGE_VALIDATION_REPORT_STANDARD.md | Phase A complete | After Phase A |
| Report Generator (Markdown) | Yes — format in KNOWLEDGE_VALIDATION_REPORT_STANDARD.md | Phase A complete | After Phase A |

**Blocking dependency:** The registry must be populated before the engine can be implemented. The population work package (~18h) is the critical path gate.

**Non-blocking dependency:** WP18B-EXT.2 (Risk Library approval) does not block implementation — the engine will correctly report LV-RSK-008 BLOCK conditions for all DRAFT RSK assets. The engine works correctly even against an unapproved risk library; it just reports the BLOCKs.

---

## 7. Technical Debt

| TD | Description | Resolution Path | Priority |
|---|---|---|---|
| TD-001 (existing) | Risk Library in DRAFT; all 40 RSK entries will produce LV-RSK-008 BLOCK | WP18B-EXT.2 governance session | URGENT — before any live tender |
| TD-007 (existing) | Registry not yet populated — engine cannot run | Population work package (~18h) | Critical path |
| TD-010 (new) | Expression evaluator for mandatory_if / excluded_if strings not yet specified | Define expression language grammar in implementation WP | Before Phase B |
| TD-011 (new) | ptc_clearances.yaml and am_clearances.yaml formats not yet specified | Define schema in implementation WP (extend tender_context.yaml) | Before Phase B |
| TD-012 (new) | No test fixtures exist — no sample registry data to test against | Create test fixture registry (10–20 representative entries) in implementation WP | Before Phase A |
| TD-013 (new) | Score trend tracking requires persistent health score history — no storage mechanism defined | Add score history YAML to 08_Commercial/Reports/ | Before Phase C |

---

## 8. Assumptions

The following assumptions underlie the KVE architecture. If any prove incorrect, the architecture may need revision:

| Assumption | Impact if Wrong |
|---|---|
| Registry YAML is the sole registry format (no database) | If a database is introduced, the Registry Loader must be replaced with a DB adapter |
| Expression evaluator for mandatory_if can be implemented as a simple variable-substitution evaluator | If expressions become complex (nested conditions, functions), a proper expression parser is needed |
| 1,325 registry entries is the expected maximum for 2–3 years | If asset count grows >10,000, the in-memory index approach may need optimisation |
| All engines are AI-assisted (not compiled code) | If a compiled implementation is needed, the YAML pseudocode must be translated to the target language |
| The tender context is always machine-readable (tender_context.yaml) | If TIL output format changes, the Context Builder must be updated |
| ptc_clearances and am_clearances are provided per-tender | If these become persistent approvals (e.g., a standing AM clearance list), the engine input model changes |

---

## 9. Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Expression evaluator is harder to implement than expected | Medium | High — Phase B gate depends on it | Define expression grammar explicitly in TD-010; start with simple expressions (IN, =, TRUE/FALSE) and extend |
| Registry population produces invalid YAML | Medium | High — engine cannot start | Run YAML syntax check as first step in Registry Loader; provide clear error messages |
| Full ASM validation (1,136 entries) makes Phase 6 slow | Low | Low — estimated <3 seconds | Profile during implementation; if slow, move ASM validation to a separate "deep validation" mode |
| BLOCK rule fires on first production run with no clear owner | Low | Medium — assembly blocked with no path forward | Every BLOCK result includes escalation owner and recommended_action; KVE never blocks without a resolution path |

---

## 10. Future Extensions

The KVE architecture is designed to be extended without structural changes:

| Extension | What Changes | Effort |
|---|---|---|
| New asset type (e.g., CON — Consultant Records) | Add LV-CON- rules to KNOWLEDGE_REGISTRY_VALIDATION_RULES.md; add CON population rules | Low — modular addition |
| New validation rule | Add to KNOWLEDGE_REGISTRY_VALIDATION_RULES.md; implement in Rule Engine | Low — isolated change |
| Real-time validation (on registry sync) | Add trigger mechanism; Rule Engine is already stateless so it can run on any trigger | Medium |
| External audit export | Add a report generator variant that produces an audit-ready PDF or structured XML | Low — report format only |
| Validation API | Wrap the Rule Engine as a REST API endpoint | Medium — implementation only |
| Proposal QA integration | Stage 9 QA Engine reads the Assembly Validation Report and the assembled proposal sections | Low — the report format is already designed for this |
| Score dashboarding | Surface KHS trend data in a dashboard tool | Low — health score data is already in YAML |

---

## 11. Recommendations for the Implementation Work Package

**Before starting:**
1. Complete the registry population work package first. The KVE cannot be tested without a populated registry.
2. Complete WP18B-EXT.2 before the first live production run (not before implementation — the engine works correctly with DRAFT RSK; it just reports BLOCKs).
3. Create a test fixture registry with at least 10–20 representative entries covering all asset types, including deliberate violations (DRAFT approved_for_reuse=true, circular supersession, missing mandatory fields) for regression testing.

**Implementation sequence (within the implementation WP):**
1. Implement Registry Loader + basic YAML validation
2. Implement RI-001, RI-008, RI-009 (engine-halt BLOCKs) and verify halt behaviour
3. Implement remaining BLOCK rules (19 rules)
4. Build Manifest Builder and basic report generator
5. Run against ARM IT045 tender profile as the Phase A gate test
6. Implement ERROR and WARNING rules
7. Implement Health Score Calculator
8. Implement Mode 1 (Platform Health)
9. Full regression test

**Technology choice guidance:** The engine can be implemented as:
- **AI-assisted (prompt-based):** Load registry YAML into context, apply rules as a structured prompt. This aligns with the current platform approach. Suitable for Phase A–B.
- **Python script:** Full deterministic implementation. Recommended for Phase B–C if the platform moves toward automated CI-style validation.
- **No preference is mandated** — the architecture is implementation-language-agnostic.

---

## 12. Platform Status After WP18D Architecture

| Dimension | Status |
|---|---|
| KVE Architecture | COMPLETE ✓ |
| KVE Implementation | DEFERRED — after registry population |
| Registry Population | DEFERRED — ~18h; critical path |
| WP18B-EXT.2 (Risk approval) | DEFERRED — BU Lead action (~2h 10min) |
| Platform Maturity | L3.5 (L4.0 requires KVE implementation + KHS ≥ 85 for 2 months) |
| Next critical path | WP18B-EXT.2 → Registry Population → KVE Implementation |

---

## 13. Recommended Next Steps

| Priority | Work Package | Action | Effort |
|---|---|---|---|
| 1 | WP18B-EXT.2 | BU Lead governance session — apply decisions to ENTERPRISE_RISK_REGISTER_V1.md; resolves TD-001 | ~2h 10min (BU Lead) |
| 2 | Registry Population | Populate KNOWLEDGE_ASSET_REGISTRY.yaml (189 core entries + 1,136 ASM entries) | ~18h |
| 3 | KVE Implementation — Phase A | Implement BLOCK rules + manifest builder; gate test on ARM IT045 | ~10h |
| 4 | KVE Implementation — Phase B | Implement ERROR/WARNING rules + full reports | ~15h |
| 5 | KVE Implementation — Phase C | Implement Health Score (Mode 1) | ~7h |
| 6 | WP19 — Rendering Engine | DOCX/PDF/HTML output (post-KVE) | TBD |
