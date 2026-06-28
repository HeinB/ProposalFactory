---
document_id: ARCHITECTURAL-DECISION-RECORD-V1
title: "Proposal Factory Architectural Decision Record"
version: "1.0"
status: "Approved — Architecture Freeze"
created: "2026-06-27"
created_by: "WP18F — Platform Integration Review & Architecture Freeze"
approved_by: "WP18F"
approved_date: "2026-06-27"
work_package: "WP18F"
category: "Architecture / Decision Record"
scope: "Formal record of all major architectural decisions made during WP12 through WP18F. Each decision is frozen as of the Architecture Freeze declaration. Structural reversals require a formal Change Request with evidence of long-term benefit outweighing disruption."
---

# Proposal Factory Architectural Decision Record

**Date:** 2026-06-27 | **Version:** 1.0 | **Status:** Approved — Architecture Freeze  
**Work Package:** WP18F — Platform Integration Review & Architecture Freeze

---

## Record Format

Each ADR entry contains:
- **Status:** FROZEN (no change without formal CR) | DEFERRED (open question) | SUPERSEDED (replaced by another ADR)
- **Context:** The situation that required a decision
- **Decision:** What was decided
- **Alternatives considered:** What else was evaluated
- **Consequences:** What this decision implies
- **Originating WP:** Where the decision was made

---

## ADR-001 — CV and Consultant Data Source (FROZEN)

**Status:** FROZEN  
**Originating WP:** WP17 / Pre-existing KB constraint  
**Decision date:** Pre-WP18; confirmed WP18F Architecture Freeze

### Context

Proposal sections S-46 (Team Structure), S-47 (Named Consultant CVs), and S-48 (Consultant Profiles) require current, accurate consultant data. The Knowledge Base maintains a CONSULTANT_INDEX.csv for skill matching but does not store full CVs.

### Decision

All consultant CV content is sourced exclusively from APPTime (the company's external HR system). KB records are used for skill-matching and team structure only. The Assembly Engine never generates CV content from KB data.

### Alternatives Considered

1. Store CVs in the KB alongside capability assets — rejected (CVs change frequently; maintenance burden would be unacceptable; stale CV risk is severe)
2. Derive CV content from ASM/CAP assets — rejected (governance rules prohibit generating personal data from project assumption language)
3. Cache a CV snapshot in the KB and refresh quarterly — rejected (APPTime is the system of record; any cache creates a data integrity risk)

### Consequences

- S-47 and S-48 are permanently PLACEHOLDER in the Assembly Engine
- Target automation ceiling is ~91% (not 100%) because CVs are always manual
- APPTime access is a hard dependency for all proposal submissions
- No change to this decision is permitted without a formal data governance review

---

## ADR-002 — Registry Mediation by KVE Only (FROZEN)

**Status:** FROZEN  
**Originating WP:** WP18D (KVE Architecture), confirmed WP18F  
**Decision date:** 2026-06-27

### Context

The Knowledge Registry contains 1,198 governed assets. Downstream engines (Assembly Engine, Pattern Engine, Rendering Engine) need access to registry content during proposal assembly. Two access patterns are possible: direct registry access (each engine reads YAML files independently) or mediated access (a single validation engine certifies a manifest that all downstream engines consume).

### Decision

The Knowledge Validation Engine (KVE) is the exclusive intermediary between the Registry and all downstream engines. No downstream Proposal Factory engine reads the Registry directly. KVE produces a per-tender Assembly Manifest in Mode 2. All downstream engines from Stage 4 onward consume only the Assembly Manifest.

### Alternatives Considered

1. Direct registry access by each engine — rejected (no governance enforcement; engines could silently use unapproved assets; no per-tender audit trail)
2. Per-engine validation — rejected (each engine would need to implement the same 76 validation rules independently; inconsistent enforcement)
3. Cached manifest (single KVE run per registry build, not per tender) — rejected (per-tender deselection rules cannot be applied without the specific BOM)

### Consequences

- KVE becomes the single point of failure for assembly validation — this is acceptable because the failure mode is explicit (BLOCK status) not silent
- Until KVE is implemented, the Assembly Engine must use the Registry directly (interim mode) — this is authorised but temporary
- All future engines (QA, Rendering) must consume the Assembly Manifest, not the Registry
- Adding a new engine requires no changes to KVE — it reads the manifest, not the registry

---

## ADR-003 — Universal Governance Standard as Single Framework (FROZEN)

**Status:** FROZEN  
**Originating WP:** WP18B-EXT.3 (Universal Governance Standard)  
**Decision date:** 2026-06-26

### Context

Before WP18B-EXT.3, different asset types had different governance approaches: Capability Assets used MASTER_CAPABILITY_INDEX.md; Assumption Packs used pack-specific frontmatter conventions; Methodology Assets had no formal governance. As the platform expanded, inconsistent governance created extraction complexity in KRPE and validation complexity in KVE.

### Decision

All 10 asset types (CAP, ASP, ASM, RSK, MTH, REF, PPT, PRT, CON, COM) are governed by a single Universal Governance Standard comprising five documents:
1. KNOWLEDGE_ASSET_STANDARD.md — asset types, IDs, formats
2. KNOWLEDGE_ASSET_LIFECYCLE.md — 8-state lifecycle with transition matrix
3. KNOWLEDGE_METADATA_STANDARD.md — mandatory/optional/derived fields for all types
4. KNOWLEDGE_GOVERNANCE_RULES.md — 42 rules covering full lifecycle
5. KNOWLEDGE_RELATIONSHIP_MODEL.md — 7 relationship types, 5-layer hierarchy

### Alternatives Considered

1. Per-asset-type governance documents — rejected (already causing inconsistency; would prevent unified KRPE extraction)
2. Single flat governance document — rejected (too unwieldy; change management would be difficult; reviewer would have to read the whole document for any change)
3. Standard for major types only (CAP, ASP, ASM); informal for others — rejected (creates a two-tier system; KRPE cannot extract informally governed assets reliably)

### Consequences

- All new asset types must be added to the Universal Standard before any content is created
- KRPE can implement a consistent extraction pattern across all asset types
- KVE validation rules apply uniformly across all 10 types
- CON and COM asset types are type-reserved but have no current implementation path — this is implementation debt, not architectural debt (see ADR-010)

---

## ADR-004 — KRPE as Sole Registry Population Mechanism (FROZEN)

**Status:** FROZEN  
**Originating WP:** WP18E (KRPE Architecture)  
**Decision date:** 2026-06-25

### Context

The Knowledge Registry must reflect the exact state of the Knowledge Libraries at extraction time. Two population approaches were possible: (a) KRPE batch extraction from source files, or (b) real-time registry updates as assets are created/approved.

### Decision

KRPE is the sole mechanism by which content from the Knowledge Libraries enters the Registry. Manual editing of registry YAML files is prohibited. Real-time registry updates are prohibited. The registry is always generated by a full KRPE run.

### Alternatives Considered

1. Real-time updates (write to registry on asset approval) — rejected (race conditions; no atomicity guarantee; partial update state possible; hard to audit)
2. Incremental KRPE runs (only update changed assets) — not rejected permanently, but deferred (complex differential logic; full runs take 1.1 seconds, making them fast enough to always run fully)
3. Manual registry editing — rejected (destroys determinism; creates unaudited registry state; directly prohibited in KNOWLEDGE_REGISTRY_CERTIFICATION.md)

### Consequences

- Every content change requires a new KRPE run and re-certification
- KRPE must be maintained as source files evolve (new fields, new asset types)
- Determinism is guaranteed — identical source produces identical registry
- Build 4 certification remains valid until: structural schema change, new asset type addition, or source file changes requiring new registry state

---

## ADR-005 — Deterministic Assembly Over AI-Generated Assembly (FROZEN)

**Status:** FROZEN  
**Originating WP:** WP17A (Assembly Engine), WP18A (Proposal Factory Architecture)  
**Decision date:** Pre-WP18; confirmed WP18F

### Context

The Proposal Factory could assemble proposals in two modes: (a) deterministic (rule-governed selection and combination of approved KB content) or (b) AI-generated (AI writes sections based on KB data without rule-governed selection). For governed sections with approved content, the choice between these modes has significant quality and consistency implications.

### Decision

For all sections where approved KB source content exists, the assembly method is deterministic: DIRECT, EXTRACT, MERGE, or TEMPLATE. AI-GENERATE is used only when no approved source exists (e.g., S-22 OCI Infrastructure, which has no standalone capability narrative; S-13 Executive Summary which requires tender-specific tailoring). AI-GENERATE always requires mandatory human review.

### Alternatives Considered

1. Full AI-generation from KB context — rejected (approved content in KB would be ignored; consistency with past proposals lost; governance controls bypassed)
2. Deterministic only (no AI-GENERATE) — not achievable (some sections have no approved source content; S-13 Executive Summary cannot be deterministic by nature)
3. AI-assisted editing of deterministic content — deferred (adds a post-assembly AI improvement layer; possible in WP19 scope)

### Consequences

- Assembly of governed sections is reproducible and auditable
- AI-GENERATE sections require mandatory human review — they are never submitted without approval
- Automation target (~91%) is bounded by the permanent PLACEHOLDER sections (CVs, commercial pricing) and the current PLACEHOLDER/AI-GENERATE sections where content is not yet in KB

---

## ADR-006 — TIL as Single Pipeline Entry Point (FROZEN)

**Status:** FROZEN  
**Originating WP:** WP18C (Tender Intelligence Layer)  
**Decision date:** 2026-06-26

### Context

The pipeline needs a consistent starting point. Without a governed entry point, different analysts might classify the same tender differently, producing different BOM, different pattern, and different section scope. The Tender Profile is the instrument that ensures all subsequent stages work from a single validated classification.

### Decision

Stage 0 (TIL) is the single entry point to the Proposal Factory pipeline. No pipeline stage may be invoked without a completed, human-validated Tender Profile. The 4 assembly-blocking fields (engagement_type, primary_platform, delivery_model, contract_type) must all be at KNOWN confidence before Stage 3 (BOM Resolution) can proceed.

### Alternatives Considered

1. Pipeline stages invoked independently by each analyst — rejected (inconsistent classification; assembly from wrong BOM possible)
2. Automated TIL from structured tender questionnaire — deferred (many tender documents are unstructured PDFs; fully automated classification has unacceptable error rate)
3. Merged TIL + BOM Resolution into one stage — rejected (TIL requires document reading judgement; BOM Resolution is mechanical; separating them preserves the human-AI boundary)

### Consequences

- Human analyst is always required for Stage 0 — TIL cannot be fully automated for unstructured tenders
- Unknown Field Protocol must be enforced — assembly cannot proceed with incomplete classification
- All 10 TIL steps must be completed in sequence before any downstream stage proceeds

---

## ADR-007 — Pattern Engine Governs Section Scoping; Section Library Governs Section Content (FROZEN)

**Status:** FROZEN  
**Originating WP:** WP18C.2 (Section Library Consolidation)  
**Decision date:** 2026-06-26

### Context

Two documents could theoretically govern section scope: the Section Library (PSL) and the Pattern Engine (PPE). Duplication of scope rules between them would create maintenance risk (one updated without the other).

### Decision

PROPOSAL_PATTERN_ENGINE.md is the sole authority for section scoping (which sections are in scope for each pattern). PROPOSAL_SECTION_LIBRARY.md is the sole authority for section content definition (what each section is, what it contains, what sources it uses). CONTENT_SOURCE_MATRIX.md is the sole authority for source-to-section mapping. These are three distinct, non-overlapping responsibilities.

### Alternatives Considered

1. PSL governs both content and scope — rejected (PPE decision tree would need to be embedded in PSL; unclear ownership)
2. CSM governs both source and scope — rejected (same duplication risk)
3. Single unified document — rejected (a 200+ row unified document would be unmanageable; changes to scoping logic would require full document re-approval)

### Consequences

- Changes to section scoping must be made in PPE only
- Changes to section content definition must be made in PSL only
- Changes to source mapping must be made in CSM only
- All three documents must be consulted when implementing Stage 8 assembly

---

## ADR-008 — Extraction Order Fixed in KRPE (FROZEN)

**Status:** FROZEN  
**Originating WP:** WP18E (KRPE Architecture)  
**Decision date:** 2026-06-25

### Context

KRPE extracts multiple asset types from the Knowledge Libraries. Some asset types reference others (ASM references ASP via parent_pack_id; CAP will reference ASP via REL-002 in Phase B). The extraction order must ensure referenced assets are registered before referencing assets.

### Decision

KRPE extraction order is fixed: PAT → SEC → MTH → REF → ASP → ASM → CAP → RSK. This order ensures all forward references are resolved. Phase B must extend this sequence without changing the relative ordering of Phase A types.

### Alternatives Considered

1. Two-pass extraction (first pass all assets, second pass relationships) — not rejected; but adds complexity without benefit given 1.1-second full run time
2. Alphabetical order — rejected (ASM before ASP would create unresolved parent_pack_id references)
3. Dependency-resolved dynamic order — unnecessary complexity; the fixed order is correct and simple

### Consequences

- Phase B must add RSK before any RSK-referencing types
- A new asset type that references an existing type must be added after the referenced type in the extraction order
- Changing the extraction order requires an ADR amendment

---

## ADR-009 — BU Normalisation at KRPE Extraction Time (FROZEN)

**Status:** FROZEN  
**Originating WP:** WP18E-IMP-B (Registry Verification), WP18F (Architecture Freeze)  
**Decision date:** 2026-06-27

### Context

Asset frontmatter uses varied business unit representations: Wave 1/2 files use `bu:` with free text; Wave 3/4 use `business_unit:` with structured values; Wave 5 uses `bu:` again. The metadata standard permitted a granular sub-BU list for Oracle (Oracle HCM, Oracle ERP, etc.). The registry, KVE, and Assembly Engine need a consistent BU representation.

### Decision

KRPE normalises all business unit values to four canonical registry values at extraction time: `Corporate`, `Oracle`, `Acumatica`, `BeBanking`. All Oracle sub-BUs collapse to `Oracle`. Cross-platform assets are mapped to `Corporate`. These four values are the authoritative BU representation for all platform purposes. The KNOWLEDGE_METADATA_STANDARD.md permitted values list (Section 8) must be updated to reflect these four canonical values before KVE Phase A begins.

### Alternatives Considered

1. Preserve granular Oracle sub-BUs in registry — rejected (would require KRPE to resolve sub-BU from module-level data which is not consistently present; adds 5 oracle values where 1 is sufficient for current use cases)
2. Use raw frontmatter BU values (no normalisation) — rejected (Wave 1/2 files would produce 3+ different representations of the same BU)
3. KVE normalises, not KRPE — rejected (KRPE is the natural normalisation boundary; normalising at KVE adds complexity to a validation engine)

### Consequences

- KMS Section 8 permitted BU values must be updated to the four canonical values before KVE Phase A (prerequisite, not Architecture Freeze blocker)
- All KVE validation rules that reference BU values must use the four canonical values
- Any future BU subdivision (e.g., distinguishing Oracle HCM from Oracle ERP in the registry) requires an ADR and KRPE schema change + re-certification

---

## ADR-010 — CON and COM as Type Reservations (DEFERRED)

**Status:** DEFERRED  
**Originating WP:** WP18B-EXT.3 (Universal Governance Standard)  
**Decision date:** 2026-06-27 (WP18F review)

### Context

KNOWLEDGE_ASSET_STANDARD.md defines 10 asset types. CON (Consultant Records) and COM (Compliance Records) are included. CON records live in APPTime (external, ADR-001). COM records exist as a COMPLIANCE_REGISTER.csv registry, not as governed KB assets.

### Decision (Deferred)

CON and COM are classified as "type reservations" — they are defined in the Universal Standard but are not populated in the Knowledge Base. This is intentional for COM (compliance records are a structured registry, not asset-level content) and permanent for CON (APPTime is the system of record; ADR-001 prevents KB storage). The governance rules GR-C01 through GR-AU05 in KNOWLEDGE_GOVERNANCE_RULES.md do not apply to CON or COM.

This requires a formal update to KNOWLEDGE_GOVERNANCE_RULES.md to explicitly exempt CON/COM from lifecycle rules. Defer to WP18B-EXT (Rules update WP, scope TBD).

### Consequences

- KRPE Phase B will not extract CON or COM records
- KVE will not validate CON or COM assets
- The Universal Standard's asset count (10 types) is accurate but 2 types are reservations

---

## ADR-011 — Assumption-Based Commercial Positioning (FROZEN)

**Status:** FROZEN  
**Originating WP:** Pre-WP18; WP16 Governance Programme  
**Decision date:** Pre-WP18; confirmed WP18F

### Context

Commercial positioning (what APPSolve promises to deliver, what assumptions underpin the price, what exclusions apply) must be consistent, governed, and auditable. Ad-hoc authoring of scope, assumptions, and exclusions creates risk of contradictory statements across proposals and unenforceable contract language.

### Decision

All commercial scope language is governed by assumption packs (ASP/ASM). The assembly engine extracts Section G (Key Assumptions) and Section H (Scope Exclusions) directly from approved assumption language. No commercial scope language is authored outside of an approved assumption pack.

### Alternatives Considered

1. Templates with per-tender authoring — rejected (inconsistency between proposals; unenforced assumptions)
2. Standard sections only (no per-module assumptions) — rejected (clients require module-level scope; standard sections cannot cover module-specific exclusions)
3. Mix of template and assumption language — rejected (unclear which governs in case of contradiction)

### Consequences

- Every assumption in every proposal traces to an approved, versioned ASM record
- Scope changes require a new or updated assumption — no scope claims outside the registry
- The Governance Programme (WP16) is complete: 0 draft assumptions, 0 outstanding decisions

---

## ADR-012 — Assembly Manifest Is the Stage Boundary (FROZEN)

**Status:** FROZEN  
**Originating WP:** WP18D (KVE Architecture)  
**Decision date:** 2026-06-27

### Context

The Knowledge Platform (Registry + KVE) and the Proposal Factory Pipeline are two subsystems. There must be a clean interface between them that downstream engines can rely on without knowing how knowledge assets are governed or stored.

### Decision

The KVE Assembly Manifest is the formal stage boundary between the Knowledge Platform and the Proposal Factory Pipeline. The Assembly Manifest contains all information downstream engines need to assemble a proposal: eligible assets, pattern, BOM, deselection lists, governance check results. Downstream engines do not need to understand KRPE, registry formats, or governance rules.

### Consequences

- The Assembly Manifest schema (defined in COMPONENT_INTERFACE_SPECIFICATION.md Section 6.3) is frozen and schema changes require ADR
- Adding a new downstream engine requires no changes to KVE or the Registry — it reads the manifest
- The manifest provides a complete, per-tender audit record of what was eligible and why

---

## ADR-013 — Pricing as a Permanent Boundary (FROZEN)

**Status:** FROZEN  
**Originating WP:** WP18A (Proposal Factory Architecture)  
**Decision date:** 2026-06-25; confirmed WP18F

### Context

Commercial pricing (Section S-52) requires Commercial Director input, margin calculations, and competitive pricing judgement. Pricing cannot be derived from KB assets.

### Decision

The Pricing Library is a permanent boundary of the Proposal Factory. S-52 (Commercial Pricing Summary) is always PLACEHOLDER. The Assembly Engine never generates pricing content. The target automation ceiling (~91%) reflects this permanent boundary.

### Alternatives Considered

1. Standard rate card embedded in KB — rejected (rate cards are commercially sensitive; margin decisions require human judgement; rates change frequently)
2. Pricing model as a separate protected library — rejected (the sensitivity and judgment requirement make automation unsafe)

### Consequences

- Minimum 2–4 hours of Commercial Director time is always required per proposal
- The Pricing Library entry in CSM will always show "GAP" status
- This is not a platform limitation to be solved — it is a deliberate governance boundary

---

## Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-27 | WP18F | Initial ADR — WP12 through WP18F; 13 decisions frozen or deferred |
