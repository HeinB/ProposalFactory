---
document_id: PLATFORM-ARCHITECTURE-REVIEW-V1
title: "Proposal Factory Platform Architecture Review"
version: "1.0"
status: "Approved — Architecture Freeze"
created: "2026-06-27"
created_by: "WP18F — Platform Integration Review & Architecture Freeze"
approved_by: "WP18F"
approved_date: "2026-06-27"
work_package: "WP18F"
category: "Architecture / Review"
scope: "Complete architectural assessment of the APPSolve Proposal Factory platform as at WP18E-IMP-B completion. Evidence-based review of all components, interfaces, dependencies, and governance structures. Basis for the Architecture Freeze declaration."
---

# Proposal Factory Platform Architecture Review

**Date:** 2026-06-27 | **Version:** 1.0 | **Status:** Approved — Architecture Freeze  
**Work Package:** WP18F — Platform Integration Review & Architecture Freeze  
**Reviewer scope:** All platform components from Knowledge Libraries through Proposal Assembly (WP12 through WP18E-IMP-B)

---

## 1. Review Methodology

This review was conducted as an independent architectural assessment — treating the platform as an external review board would before certifying it for implementation. The review was based exclusively on evidence from the 17 governing documents specified in the WP18F brief:

- Platform continuity documents (HANDOVER.md, AI_CONTEXT.md, WP18Z_SESSION_BASELINE.md)
- Universal Governance Standard (5 documents: KAS, KAL, KMS, KGR, KRM)
- Engine architecture documents (KRPE, KVE, PFA, TIL, PAS, PPE)
- Content definitions (PSL, CSM)
- Certification evidence (KNOWLEDGE_REGISTRY_CERTIFICATION.md)

**Scope constraints:**
- No new capability added.
- No architecture redesigned.
- All findings are evidence-based with document and section citations.
- The review distinguishes between architectural debt (structural decisions that create long-term problems) and implementation debt (gaps in execution that do not affect architectural soundness).

---

## 2. Platform Overview

### 2.1 Two-Subsystem Architecture

The Proposal Factory comprises two distinct subsystems joined by a governed interface:

```
┌─────────────────────────────────────────────────────────────────┐
│  KNOWLEDGE PLATFORM                                             │
│                                                                 │
│  Knowledge Libraries ──► KRPE ──► Registry ──► KVE            │
│  (CAP, ASP, ASM, RSK,                         (Assembly        │
│   MTH, REF, PPT, PRT,                          Manifest)       │
│   CON, COM)                                                     │
└────────────────────────────────┬────────────────────────────────┘
                                 │  Assembly Manifest
                                 │  (KVE output — certified per tender)
┌────────────────────────────────▼────────────────────────────────┐
│  PROPOSAL FACTORY                                               │
│                                                                 │
│  TIL (Stage 0) ──► BOM Resolution ──► Capability Selection     │
│                                    ──► Reference Selection      │
│                                    ──► Methodology Selection    │
│                    ──► Assembly Engine ──► Output               │
└─────────────────────────────────────────────────────────────────┘
```

The boundary between subsystems is the Assembly Manifest. No downstream Proposal Factory engine reads the Registry directly. This is the platform's primary architectural principle.

### 2.2 Component Inventory

| Component | Document | Status | Maturity |
|---|---|---|---|
| Knowledge Libraries | KNOWLEDGE_ASSET_STANDARD.md | COMPLETE (Phase A scope) | L3.8 |
| KRPE | KNOWLEDGE_REGISTRY_POPULATION_ENGINE.md | IMPLEMENTED — Phase A certified | L3.8 |
| Knowledge Registry | KNOWLEDGE_REGISTRY_CERTIFICATION.md | CERTIFIED (Build 4) | L3.8 |
| KVE | KNOWLEDGE_VALIDATION_ENGINE.md | ARCHITECTURE COMPLETE — not implemented | L3.8 |
| Universal Governance Standard | KAS, KAL, KMS, KGR, KRM | COMPLETE | L3.8 |
| TIL | TENDER_INTELLIGENCE_RULES.md | OPERATIONAL (human-AI assisted) | L3.8 |
| Proposal Pattern Engine | PROPOSAL_PATTERN_ENGINE.md | ARCHITECTURE COMPLETE — human-invoked | L3.8 |
| Section Library | PROPOSAL_SECTION_LIBRARY.md | COMPLETE (82 sections) | L3.8 |
| Content Source Matrix | CONTENT_SOURCE_MATRIX.md | COMPLETE (S-01 to S-82) | L3.8 |
| Assembly Engine | PROPOSAL_FACTORY_ARCHITECTURE.md | PRODUCTION READY (WP17C 5/5 PASS) | L3.8 |
| Assembly Sequence | PROPOSAL_ASSEMBLY_SEQUENCE.md | COMPLETE (19 steps, SI-001–007 incorporated) | L3.8 |

---

## 3. Knowledge Platform Assessment

### 3.1 Knowledge Libraries

**Current content (Phase A):**

| Type | Count | Status |
|---|---|---|
| CAP — Capability Assets | 49 | All APPROVED; certified |
| ASP — Assumption Packs | 13 | All APPROVED; certified |
| ASM — Assumptions | 1,136 | All APPROVED; certified |
| RSK — Risk Assets | 0 | Standard defined (RISK_LIBRARY_STANDARD.md); content pending |
| MTH — Methodology Assets | 2 | Partial (W2S1-005, W5-METH-001) |
| REF — Reference Letters | 16 | Active |
| PPT, PRT, CON, COM | 0 | Type-reserved; not yet populated |

**Architectural finding — Phase A completeness (AF-001):** The Phase A registry is complete for its declared scope. The remaining asset types are in one of three categories: (a) standard defined, content pending (RSK), (b) content exists but not yet formally governed (MTH, REF), and (c) type-reserved with no current implementation path (PPT, PRT, CON, COM). Category (c) represents unnecessary complexity in the Universal Standard — see Section 7.

**Architectural finding — BU normalisation (AF-002):** Three representations of business unit exist in the platform:
1. Metadata Standard (KMS Section 8): granular Oracle sub-BUs (Oracle HCM, Oracle ERP, Oracle OIC, Oracle Analytics, Oracle EBS)
2. Asset frontmatter: mixed formats (Wave 1/2 use `bu:` with free text; Wave 3+ use `business_unit:`)
3. Registry: four canonical values (Corporate, Oracle, Acumatica, BeBanking)

The KRPE normalises at extraction time. This collapses Oracle sub-BUs into a single "Oracle" value in the registry. This is a deliberate trade-off (simplicity vs. granularity) but has not been formally decided in an ADR. The KMS Section 8 "permitted values" list is inconsistent with what KRPE produces. **Recommendation: freeze the four canonical registry values as authoritative; update KMS Section 8 to match. No code change required.**

### 3.2 Knowledge Registry Population Engine (KRPE)

**Architecture quality:** High. KRPE has a clean 7-component design (SOURCE_SCANNER, FRONTMATTER_PARSER, TABLE_EXTRACTOR, SECTION_EXTRACTOR, RELATIONSHIP_BUILDER, INDEX_BUILDER, REGISTRY_WRITER) with well-defined interfaces and determinism guarantees.

**Implementation quality:** Certified. Build 4 produced 1,198 entries in 1.1 seconds with 0 errors across 3 deterministic builds. Four pre-certification defects were identified and fixed.

**Phase B gap:** KRPE Phase A only populates CAP, ASP, and ASM. RSK, MTH, REF, PAT, and SEC extractors are Phase B scope. KVE's ability to validate RSK-dependent rules is deferred until KRPE Phase B completes. This is a documented architectural gap with a clear remediation path.

**Architectural finding — extraction order (AF-003):** KRPE Phase A extraction order (PAT→SEC→MTH→REF→ASP→ASM→CAP→RSK) establishes the dependency resolution sequence. ASP must be extracted before ASM because ASM records reference their parent_pack_id. CAP is extracted last because CAP→ASP relationships (Phase B) require ASP to be registered first. This order is correct and should be preserved in Phase B.

### 3.3 Knowledge Validation Engine (KVE)

**Architecture quality:** High. KVE's two-mode design (Mode 1 Platform Health batch; Mode 2 Assembly Validation per-tender) correctly separates proactive governance from reactive assembly validation.

**Key architectural principle (KP-001):** KVE is the exclusive intermediary between the Registry and all downstream assembly engines. No downstream engine reads the Registry directly. KVE's certified Assembly Manifest is the only authorised data source for Stages 4 through 10. This principle is critical for governance integrity.

**Implementation gap (IG-001):** KVE is not yet implemented. This is the platform's single largest functional gap. Until KVE is implemented, Mode 2 (Assembly Validation at TIL-08) cannot execute, and Stages 4–10 consume the Registry directly (interim mode). This is architecturally unsafe for production — see Section 9.

**Architectural finding — 22 BLOCK conditions (AF-004):** The 22 BLOCK conditions in KVE are well-defined and evidence-based. They cover: asset lifecycle state, mandatory field completeness, relationship integrity, pack count reconciliation, cross-BU linking, and governance rule compliance. All 22 can be evaluated against the certified Phase A registry. 6 graph-traversal rules requiring CAP→ASP edges are deferred to Phase B.

**Architectural finding — PFA missing KVE (AF-005):** PROPOSAL_FACTORY_ARCHITECTURE.md (v1.2) does not show KVE in its pipeline component diagram. KNOWLEDGE_VALIDATION_ENGINE.md describes KVE as integrating at Stage 0 (TIL-08 invokes KVE Mode 2) and producing the Assembly Manifest consumed by Stages 4–10. This is a documentation inconsistency, not an architectural one. **Recommendation: PFA should be updated to show KVE between Stage 0 and Stage 4 in a future version.** This is NOT an Architecture Freeze blocker — the KVE document is authoritative for KVE placement.

---

## 4. Proposal Factory Assessment

### 4.1 Tender Intelligence Layer (Stage 0)

**Architecture quality:** High. The 10-step TIL process produces a governed Tender Profile with 4 assembly-blocking fields (engagement_type, primary_platform, delivery_model, contract_type). The downstream trigger matrix (engagement type → pattern, platform → BOM, industry+module → deselections, country → compliance) is explicit and deterministic.

**Operational mode:** Human-AI collaborative. TIL is OPERATIONAL at L3.5, meaning it can be executed by a human analyst with AI assistance. There is no automated TIL invocation. This is the correct operational mode — TIL requires judgement about ambiguous tender requirements that cannot be reliably automated.

**Architectural finding — unknown field handling (AF-006):** TENDER_INTELLIGENCE_RULES.md Section 8 specifies an Unknown Field Protocol with three states (UNKNOWN, PARTIAL, CONTRADICTORY). This protocol prevents assembly from proceeding with incomplete classification. The protocol is architecturally sound but requires KVE Mode 2 implementation to enforce formally.

**Architectural finding — Stage 0 vs Stage 1 overlap (AF-007):** TIL (Stage 0) processes the tender document. Stage 1 (Tender Analysis) also starts from the tender document. The boundary between Stage 0 output (Tender Profile) and Stage 1 input is not explicitly stated in PFA. TENDER_INTELLIGENCE_RULES.md clarifies that TIL produces the Tender Profile which is then the input for all subsequent stages, not just the deterministic ones. The relationship is: Stage 0 → Tender Profile → drives all Stages 1–10. Stage 1 does not independently re-read the tender; it uses the Tender Profile. **This should be made explicit in a PFA update.**

### 4.2 Proposal Pattern Engine

**Architecture quality:** High. The 3-level classification decision tree (Tier 1 engagement type → Tier 2 platform → Tier 3 delivery model) produces a deterministic pattern selection. 13 patterns are defined (P1–P12 implementation variants + P13 AMS).

**Section scoping interface:** Clean. PPE governs which sections are in scope. PSL governs what each section is. CSM governs where content comes from. These are three distinct, non-overlapping concerns.

**Combination pattern (P12+P13):** Section 9 of PPE explicitly handles Implementation+AMS combinations including SI-001 (S-38 excluded for AMS; S-73 used instead). This was a documented defect in an earlier version, now resolved.

### 4.3 Section Library and Content Source Matrix

**Architecture quality:** High. 82 sections covering the full proposal structure. CSM provides assembly method, primary source, secondary source, and validation rules per section. This is a complete specification.

**Architectural finding — sub-section exclusion rules (AF-008):** CSM Section 4 contains sub-section exclusion rules for individual capability assets (e.g., W3S1-008 Section 14.2 excluded; W3S1-009 Section 13.2 excluded). These rules are evidence-based governance constraints but are embedded in CSM rather than in the capability asset's own frontmatter. If the capability asset changes, CSM will not automatically reflect the change. **Recommendation: add a `content_exclusions` list to the relevant capability asset frontmatter as the authoritative source; CSM references the asset, not duplicates it. This is implementation debt, not architecture debt.**

**Automation coverage:** The PSL documents current and target automation percentages for all 82 sections. This is a useful operational metric. Total target automation is ~91% (ceiling, not a commitment), limited by CVs (always PLACEHOLDER) and commercial pricing (always PLACEHOLDER).

### 4.4 Assembly Engine

**Architecture quality:** High. The Assembly Engine is the platform's most mature component — PRODUCTION READY with 5/5 regression tests passing.

**Assembly Sequence:** 19 deterministic steps with defined gates. SI-001 through SI-007 (Section Integrity issues) are all resolved and incorporated.

**Architectural finding — Risk Selection in Assembly Sequence (AF-009):** KNOWLEDGE_RELATIONSHIP_MODEL.md Section 7.3 defines a "Risk Selection Engine" for Stage 8 (RSK assets with mandatory_if/optional_if/excluded_if conditions). However, PROPOSAL_ASSEMBLY_SEQUENCE.md's 19-step sequence does not explicitly include Risk Selection as a named step. Step 15 (Assemble Commercial and Compliance Sections) implicitly includes risk content but does not explicitly invoke a Risk Selection Engine. **Recommendation: when the Risk Library is populated, add an explicit Risk Selection step between Step 14 (Assumption Schedule) and Step 15 in the assembly sequence.**

---

## 5. Governance Framework Assessment

### 5.1 Universal Governance Standard

**Assessment:** The Universal Governance Standard (5 documents: KAS, KAL, KMS, KGR, KRM) is comprehensive, internally consistent, and well-designed. 42 governance rules are defined. The 8-state lifecycle covers the full asset lifecycle with explicit entry/exit criteria and transition matrix.

**Architectural finding — lifecycle field migration (AF-010):** KNOWLEDGE_METADATA_STANDARD.md Section 8 notes that CAP assets "partially implement" the standard and that the `lifecycle_status` field is "not yet formal → APPROVED". Existing CAP assets use informal "Approved v1.0" language in their frontmatter, not the formal `lifecycle_status: APPROVED` field. This means the KVE's lifecycle validation rules (which check `lifecycle_status` = APPROVED) would find empty fields in existing assets. This is implementation debt that must be resolved before KVE Phase A can operate. It is not an architectural problem.

**Architectural finding — relationship model Phase B dependency (AF-011):** KNOWLEDGE_RELATIONSHIP_MODEL.md defines 7 relationship types (GOV, SRC, CON, XRF, SUP, GEN, RST) and 10 additional CLV cross-library validation rules for Phase B (CLV-001 through CLV-012). Phase A only implements REL-001 (CON: ASP CONTAINS ASM). The full relationship graph requires KRPE Phase B. This is a correctly sequenced dependency.

### 5.2 Governance Rule Coverage

| Rule Category | Rules | Coverage |
|---|---|---|
| Creation rules (GR-C01 to GR-C04) | 4 | Enforced by process |
| Normalisation rules (GR-N01 to GR-N08) | 8 | Enforced by KRPE |
| Review rules (GR-R01 to GR-R06) | 6 | Enforced by process |
| Approval rules (GR-A01 to GR-A06) | 6 | Enforced by process; KVE will enforce |
| Versioning rules (GR-V01 to GR-V05) | 5 | Enforced by process |
| Retirement rules (GR-RE01 to GR-RE05) | 5 | Enforced by process |
| Archival rules (GR-AU01 to GR-AU05) | 5 | Enforced by process |
| Missing (no rule) | — | 42 rules cover all lifecycle states |

The governance rules are comprehensive. Automated enforcement currently covers normalisation rules (KRPE). Full automated enforcement requires KVE implementation.

---

## 6. Pipeline View Consistency

The platform describes the proposal factory pipeline at three levels of granularity:

| View | Document | Scope |
|---|---|---|
| 11-stage view | PROPOSAL_FACTORY_ARCHITECTURE.md | Full pipeline Stage 0 through Stage 10 |
| 19-step view | PROPOSAL_ASSEMBLY_SEQUENCE.md | Assembly detail (Steps 1–19 within Stages 4–8) |
| 10-step TIL view | TENDER_INTELLIGENCE_RULES.md | Stage 0 internal detail |

These are complementary views of the same pipeline, not contradictions. The mapping is:

| PFA Stage | PAS Steps | TIL Steps |
|---|---|---|
| Stage 0 — Tender Intelligence | Steps 1–2 (Tender Profile creation) | Steps 1–10 (TIL internal) |
| Stage 1 — Tender Analysis | Step 3 (Requirement Matrix) | — |
| Stage 2 — Requirements | Step 4 (Requirement gaps) | — |
| Stage 3 — BOM Resolution | Step 5 (BOM build) | — |
| Stage 4 — Capability Selection | Steps 6–8 (CAP selection, eligibility, deselection) | — |
| Stage 5 — Reference Selection | Step 9 (REF shortlisting) | — |
| Stage 6 — Methodology Selection | Step 10 (METH pairing) | — |
| Stage 7 — KVE Validation | Step 11 (KVE Mode 2 invocation) | — |
| Stage 8 — Proposal Assembly | Steps 12–19 (full assembly) | — |
| Stage 9 — QA | — (WP18D scope) | — |
| Stage 10 — Rendering | — (WP19 scope) | — |

**Architectural finding — missing cross-reference (AF-012):** No governing document contains the mapping table above. The relationship between the three pipeline views is implied but never made explicit. **Recommendation: add this cross-reference table to PROPOSAL_FACTORY_ARCHITECTURE.md Section 3 in a future update. This is implementation debt.**

---

## 7. Architectural Concerns

### 7.1 Type Reservations Without Implementation Path (AC-001)

**Severity:** Low  
**Evidence:** KNOWLEDGE_ASSET_STANDARD.md Section 2.4 defines CON (Consultant Records) and COM (Compliance Records) as formal asset types with governance rules. CONTENT_SOURCE_MATRIX.md lists CONS (Consultant Library) with status "ACTIVE — not in KB" (APPTime) and COMP (Certification Library) with status "ACTIVE."

**Problem:** CON and COM are defined in the Universal Standard but have no implementation path in the Knowledge Base. CON records live permanently in APPTime (ADR-001). COM records are a CSV registry, not governed KB assets. Treating them as full asset types in the Universal Standard creates governance expectations that will never be met.

**Disposition:** Implementation debt. The type reservations do not harm the working platform but add cognitive complexity to the governance standard. Recommended action: reclassify CON and COM as "external asset references" rather than governed KB asset types, or explicitly document that governance rules GR-C01 through GR-AU05 do not apply to CON/COM. Defer to WP18B-EXT or later.

### 7.2 KVE Not In PFA Pipeline (AC-002)

**Severity:** Low (documentation, not architectural)  
**Evidence:** PROPOSAL_FACTORY_ARCHITECTURE.md v1.2 component table does not show KVE. KNOWLEDGE_VALIDATION_ENGINE.md Section 6 states "KVE is invoked at Stage 0 TIL-08 and produces Assembly Manifest consumed by Stages 4–10."

**Problem:** The primary pipeline document (PFA) omits the KVE, which is the most significant architectural addition since PFA v1.0. A reader following only PFA would not understand the KVE's role.

**Disposition:** Documentation debt. PFA should be updated to show KVE in Stage 7 (KVE Validation), or the pipeline overview table should include KVE. This does NOT require changing the architecture; the KVE document is authoritative. Target: PFA v1.3 when KVE Phase A begins.

### 7.3 BU Granularity Inconsistency (AC-003)

**Severity:** Low  
**Evidence:** KNOWLEDGE_METADATA_STANDARD.md Section 8 lists granular Oracle sub-BU values (Oracle HCM, Oracle ERP, Oracle OIC, Oracle Analytics, Oracle EBS). KRPE produces four canonical values (Corporate, Oracle, Acumatica, BeBanking). KVE validation rules in KNOWLEDGE_VALIDATION_ENGINE.md use the four canonical values.

**Problem:** KMS permits values that KRPE does not produce and KVE does not recognise. If KVE validation rules check `owner_business_unit` against the KMS permitted values list, all Oracle assets will fail validation.

**Disposition:** Implementation debt with an architectural fix required before KVE Phase A. The canonical registry values (four) must be designated as the authoritative permitted values, and KMS Section 8 must be updated to reflect this before KVE is implemented. No code change to KRPE is required.

### 7.4 Lifecycle Field Population Gap (AC-004)

**Severity:** Medium (blocks KVE Phase A rule VR-L01 through VR-L04)  
**Evidence:** KNOWLEDGE_METADATA_STANDARD.md Section 8 confirms CAP assets "partially implement" the standard. Specifically, `lifecycle_status` is not populated as a formal field in Wave 1–4 CAP frontmatter. KVE rule VR-L01 checks `lifecycle_status: APPROVED` for all assets.

**Problem:** If KVE Phase A runs on current registry, VR-L01 will report all 49 CAPs as lifecycle violations because the field is empty (not "APPROVED"). This is a false positive that would block the Assembly Manifest.

**Disposition:** Implementation debt that must be resolved before KVE Phase A can operate correctly. Resolution requires either: (a) adding `lifecycle_status: APPROVED` to all 49 CAP files and regenerating the registry, or (b) adding a KVE interpretation rule that treats a missing `lifecycle_status` field as APPROVED when `approved_for_reuse: true` is set. Option (b) is a KVE implementation detail. The Architecture Freeze does not block this — it is scoped to KVE Phase A.

### 7.5 Risk Library Content Gap (AC-005)

**Severity:** Medium (operational impact; no assembly-blocking)  
**Evidence:** CONTENT_SOURCE_MATRIX.md Section 7 shows S-37 (RAID Framework) and S-50 (Risk Register) with assembly method AI-GENERATE and validation rule "G-RISK gap flagged until Risk Library populated."

**Problem:** The Risk Library standard is defined (RISK_LIBRARY_STANDARD.md) but content is pending. For tenders requiring risk registers, the factory cannot produce deterministic risk content. Risk sections default to AI-GENERATE with mandatory human review — a regression from the target automation level.

**Disposition:** Implementation gap with a defined remediation path (WP18B-EXT.2 → KRPE Phase B). This is not an architectural problem; the risk integration design is complete. The gap is in content population only.

---

## 8. Architectural Strengths

The following architectural decisions represent validated, high-quality design choices that should be preserved:

| Strength | Evidence | Rationale |
|---|---|---|
| Registry as single source of truth | KVE architecture; KRPE certification | All downstream engines consume certified data only |
| KVE as exclusive mediator | KVE Section 5 | Prevents governance drift in per-tender assembly |
| Deterministic assembly | PAS 19-step sequence; PPE decision tree | Removes authoring subjectivity from governed sections |
| Pattern Engine for section scoping | PPE Section 3 | Separates "what sections" from "what content" cleanly |
| Universal Governance Standard | 5-document framework | Single standard across all 10 asset types |
| KRPE determinism guarantee | Certification: 3 builds identical | Registry state is reproducible and auditable |
| Assembly Engine PRODUCTION READY | WP17C 5/5 PASS | Proven execution with regression test baseline |
| Stage 0 TIL as single entry | TIL Section 2 | All subsequent stages derive from one governed input |
| TIL downstream trigger matrix | TIL Section 7 | All deterministic stage assignments are explicit |
| 42 governance rules | KGR Section 3–9 | Complete coverage of full asset lifecycle |
| Failure handling in KRPE | KRPE Section 6 | No silent failures; all failures surfaced and logged |
| 22 BLOCK conditions in KVE | KVE Section 5 | Validation is strict and complete for Phase A scope |
| Section Library defers to PPE for scoping | PSL Section 1 | Clean separation of concerns between PSL and PPE |

---

## 9. Implementation Readiness

The platform is architecturally sound and ready for implementation to continue. The gaps identified (AC-001 through AC-005) are all implementation debt or documentation debt — none represent fundamental architectural problems.

The critical path to full platform maturity is:

1. **KVE Phase A** (highest priority): Implement 22 BLOCK rules + manifest builder. Pre-requisite: resolve AC-003 (BU permitted values) and AC-004 (lifecycle field population) before KVE Phase A begins.
2. **KRPE Phase B**: RSK/MTH/REF/PAT/SEC extractors + full relationship graph. Pre-requisite: WP18B-EXT.2 (RSK asset classification).
3. **Risk Library population**: WP18B-EXT.2 scope. Unlocks deterministic risk content.
4. **PFA documentation update**: Show KVE in pipeline; add pipeline cross-reference table. Can be done in parallel with any work package.

---

## 10. Summary of Architectural Findings

| ID | Finding | Severity | Type | Action |
|---|---|---|---|---|
| AF-001 | PPT/PRT/CON/COM asset types reserved but unpopulated | Low | Implementation debt | Note in ADR |
| AF-002 | BU normalisation produces values inconsistent with KMS | Medium | Implementation debt — must fix before KVE | Fix KMS Section 8 |
| AF-003 | KRPE extraction order is correct and must be preserved in Phase B | — | Positive finding | Freeze in KRPE ADR |
| AF-004 | 22 KVE BLOCK conditions are complete for Phase A | — | Positive finding | Proceed with KVE |
| AF-005 | KVE missing from PFA pipeline diagram | Low | Documentation debt | PFA v1.3 update |
| AF-006 | TIL Unknown Field Protocol requires KVE to enforce | — | Implementation dependency | Noted |
| AF-007 | Stage 0 → Stage 1 boundary not explicit in PFA | Low | Documentation debt | PFA v1.3 |
| AF-008 | Sub-section exclusion rules in CSM, not in asset frontmatter | Low | Implementation debt | Future cleanup |
| AF-009 | Risk Selection Engine not named in Assembly Sequence | Low | Implementation debt — add step when Risk Library ready | Noted |
| AF-010 | lifecycle_status field not formally populated in CAP/ASP assets | Medium | Implementation debt — blocks KVE VR-L01 | Resolve before KVE Phase A |
| AF-011 | Full relationship graph requires KRPE Phase B | — | Documented dependency | Correct sequencing |
| AF-012 | No cross-reference between three pipeline views | Low | Documentation debt | PFA v1.3 |
| AC-001 | CON/COM type reservations have no implementation path | Low | Implementation debt | Note in ADR |
| AC-002 | KVE absent from PFA pipeline | Low | Documentation debt | PFA v1.3 |
| AC-003 | BU granularity inconsistency (KMS vs KRPE vs KVE) | Medium | Implementation debt — fix before KVE | Fix KMS Section 8 |
| AC-004 | lifecycle_status field population gap | Medium | Implementation debt — fix before KVE | Populate or add KVE interpretation |
| AC-005 | Risk Library content pending | Medium | Operational gap | WP18B-EXT.2 |

**Blocking findings (prevent KVE Phase A):** AC-003, AC-004  
**Non-blocking findings:** All others

---

## 11. Architecture Freeze Recommendation

Based on this review, the platform architecture is:

- **Internally consistent** — no contradictions between governing documents on structural decisions
- **Well-bounded** — all component interfaces are defined; all data flows are explicit
- **Deterministic** — assembly, registry population, and validation are all rule-governed with no ambiguity
- **Implementable** — the implementation gaps are execution gaps, not design gaps

**Recommendation: Approve Architecture Freeze.**

The Architecture Freeze covers all components listed in Section 2.2. Structural changes to frozen components require formal change control as per the amendment process in each governing document.

Two pre-conditions must be resolved before KVE Phase A begins (not before Architecture Freeze):
1. AC-003: Update KMS Section 8 permitted BU values to match KRPE canonical values
2. AC-004: Populate `lifecycle_status: APPROVED` in all CAP/ASP frontmatter files, or implement a KVE interpretation rule

---

## 12. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-27 | WP18F | Initial platform architecture review — basis for Architecture Freeze |
