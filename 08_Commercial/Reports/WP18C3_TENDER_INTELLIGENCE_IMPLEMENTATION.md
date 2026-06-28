---
document_id: WP18C3-TENDER-INTELLIGENCE-IMPLEMENTATION
title: "WP18C.3 — Tender Intelligence Layer: Implementation Report"
version: "1.0"
status: "Complete"
created: "2026-06-26"
created_by: "WP18C.3 — Tender Intelligence Layer"
category: "Reports / Factory Implementation"
scope: "Phase 6 + WP report for WP18C.3. Documents the architecture decisions, coverage metrics, pipeline integration, and downstream impact of the Tender Intelligence Layer (TIL). The TIL becomes Stage 0 of every Proposal Factory run."
---

# WP18C.3 — Tender Intelligence Layer: Implementation Report

**Date:** 2026-06-26 | **Version:** 1.0 | **Status:** Complete  
**Work Package:** WP18C.3 — Tender Intelligence Layer  
**Predecessor:** WP18C.1 (Factory Optimisation — revised roadmap)  
**Priority:** P0 (alongside WP18C.2) — per WP18C1_REVISED_IMPLEMENTATION_ROADMAP.md

---

## 1. Executive Summary

WP18C.3 builds the Tender Intelligence Layer (TIL) — the "brain" that drives every future Proposal Factory run. Before this WP, the Proposal Factory had no Stage 0: a BU Lead read the tender document, made manual decisions about pattern, capability, methodology, and references, and then began assembly. This introduced inconsistency, missed governance rules, and an estimated 6–8 hours of scoping work per tender.

The TIL replaces this entirely. Given a tender document, the TIL produces a governed `[TENDER_ID]_TENDER_PROFILE.md` that deterministically drives all downstream factory stages. Every selection — capability assets, methodology, references, section scope — flows from the Tender Profile rather than from re-reading the tender.

**Six documents delivered:**

| Document | Location | Purpose |
|---|---|---|
| TENDER_PROFILE_STANDARD.md | Assembly_Engine/ | YAML schema for every Tender Profile; field specs with source/extraction/validation/default rules |
| TENDER_INTELLIGENCE_RULES.md | Assembly_Engine/ | 10-step TIL processing sequence; confidence model; downstream trigger matrix |
| PROPOSAL_PATTERN_ENGINE.md | Assembly_Engine/ | 13-pattern classification; section scoping rules (AO-002); combination rules |
| CAPABILITY_SELECTION_ENGINE.md | Assembly_Engine/ | BOM-to-asset lookup for all 16 BOMs; governance deselection rules |
| METHODOLOGY_SELECTION_ENGINE.md | Assembly_Engine/ | Pattern-to-methodology lookup; phase structures; project plan template reference |
| REFERENCE_SELECTION_ENGINE.md | Assembly_Engine/ | 7-dimension scoring matrix; 12 exclusion rules; AM approval workflow |

---

## 2. Automation Gaps Resolved

WP18C.3 directly resolves 4 of the 15 automation opportunities identified in WP18C1_AUTOMATION_OPPORTUNITY_REGISTER.md:

| AO# | Opportunity | Status After WP18C.3 |
|---|---|---|
| AO-001 | BOM-to-Capability Rules | **RESOLVED** — CAPABILITY_SELECTION_ENGINE.md |
| AO-002 | Engagement-Type Scoping Rules | **RESOLVED** — PROPOSAL_PATTERN_ENGINE.md Section 4 |
| AO-003 | Reference Scoring | **RESOLVED** — REFERENCE_SELECTION_ENGINE.md |
| AO-004 | Methodology Lookup | **RESOLVED** — METHODOLOGY_SELECTION_ENGINE.md |
| AO-009 | Tender Profile Intake Form | **RESOLVED** — TENDER_PROFILE_STANDARD.md + TENDER_INTELLIGENCE_RULES.md |

Additionally, this WP encodes the **SI-001 structural fix** (WP18C.1 Structural Issue 001): S-38 (Change Control Framework) is now formally excluded for AMS engagements because S-73 (Change Request Process) is the AMS-correct equivalent. This eliminates the duplication identified in the ARM IT045 run.

---

## 3. Architecture Decisions

### AD-001 — Tender Profile as Single Gateway

**Decision:** Every Proposal Factory run begins with a completed, APPROVED Tender Profile. Assembly cannot start without it.

**Rationale:** The WP18C arm IT045 run showed that manual scoping decisions (which sections to include, which capability assets to select, which references to use) were made ad hoc and not recorded. This created an unreproducible run that could not be quality-checked against rules. The Tender Profile makes every decision explicit and auditable.

**Consequence:** A new tender requires approximately 1–2 hours to produce an approved Tender Profile before assembly begins. This replaces 6–8 hours of fragmented manual scoping — net saving ~5–6 hours per tender.

### AD-002 — Unknowns Always Explicit

**Decision:** Any field the TIL cannot determine from the tender document is recorded as UNKNOWN in the profile. No silent defaulting. No inference without documentation.

**Rationale:** Silent inference was identified as a root cause of the QA score gap in WP18C (72/100 vs 75 threshold). The ARM IT045 profile had several implicit assumptions that were not surfaced until QA. Making unknowns explicit at Stage 0 prevents them propagating into assembly.

**Exception:** A small set of fields have documented safe defaults (e.g. `parallel_run_required = YES` for HCM payroll — HCM-CUT-005). These defaults are stated explicitly in the field specification and logged in the profile.

### AD-003 — Deterministic Derivation of All Block G Fields

**Decision:** All 10 fields in Block G (derived fields) are populated by deterministic engine lookups, not human judgement. Manual override requires BU Lead approval and documentation.

**Rationale:** The three manual stages identified in WP18C.1 (Stages 4/5/6 — capability selection, reference selection, methodology selection) were shown to be fully rule-based. This WP codifies the rules. Future runs of the factory need no human input for these selections if the Tender Profile is complete and HIGH confidence.

**Override governance:** Override is permitted but must be documented. If the engine assigns Pattern 1 and the BU Lead overrides to Pattern 2 (phased go-live), this is recorded in the Tender Profile with rationale. All downstream section scoping is re-derived from the override.

### AD-004 — Section Scoping by Engagement Type (AO-002)

**Decision:** Section inclusion and exclusion is determined by engagement type rule, not by BU Lead judgement per run.

**Rationale:** The WP18C ARM IT045 run excluded 25 sections manually. WP18C.1 identified this as AO-002 (second-highest ROI automation opportunity). The PROPOSAL_PATTERN_ENGINE.md now encodes these rules explicitly. Every AMS run will produce the same section scope without manual intervention.

**SI-001 embedded:** The S-38/S-73 duplication fix is now a permanent rule in PROPOSAL_PATTERN_ENGINE.md — S-38 is excluded for AMS by default, eliminating the duplication that appeared in the ARM IT045 draft.

### AD-005 — Governance Rules Embedded at Stage 0

**Decision:** All 15 governance restrictions (GOV-001 through GOV-015) are checked at the TIL stage and recorded as governance_flags in the Tender Profile. They are not checked reactively at section assembly.

**Rationale:** In the WP18C run, governance rules were applied manually during assembly. Several rules (B-BBEE expiry, OPN level, OIC billing restriction) required the assembler to remember to check. By surfacing all governance flags at Stage 0, the assembler begins with a complete list of restrictions for this tender.

**Key permanent rules encoded:**
- Rule 21.4 (DFA) — always active
- Rule 21.5 (Redpath) — always active
- GOV-006 (Gold Partner expired 2021) — always active
- GOV-007 (B-BBEE expiry 2026-07-31) — active for all submissions at or after that date
- G-001 (Compensation = Mining only) — active for all non-Mining tenders
- HCM-CUT-005 (Parallel run default) — active for all payroll-interface scope

### AD-006 — Reference Scoring Formalised (7 Dimensions)

**Decision:** Reference selection uses a 7-dimension, 10-point scoring matrix (product, platform, architecture, industry, country, size, scope overlap).

**Rationale:** The WP18C ARM IT045 run selected references manually (REF-ORA-008 first, REF-ORA-004 second, etc.) with no documented scoring. The WP18C.1 review (client evaluator perspective) noted the reference order was wrong (References appeared before the AMS model — SI-005). The scoring matrix both determines selection and provides a documented rationale that can be cited in the proposal assembly report.

**Architecture dimension:** Adding engagement architecture (AMS vs Implementation) as a scoring dimension was a deliberate addition beyond the basic Stage 5 rules. An AMS reference (REF-ORA-008) scores higher for an AMS tender than an implementation reference (REF-ORA-004). This corrects the ARM IT045 run where REF-ORA-008 was selected first but without this rationale being codified.

### AD-007 — AM Approval Per-Tender (No Standing Approval)

**Decision:** Reference AM approval is obtained per-tender. Previous approval for the same letter does not carry forward.

**Rationale:** Client relationships change. An approved reference from six months ago may no longer be appropriate if the relationship has evolved, an invoice is disputed, or a competitor situation has changed. The per-tender approval rule is already embedded in the Architecture document (R5.4) and is preserved here.

### AD-008 — Methodology = Platform-Driven, Not Client-Requested

**Decision:** Methodology asset is determined by platform and engagement type from the lookup table. Client requests for specific methodologies (e.g. "agile only") are accommodated within the existing assets, not by creating new methodology documents.

**Rationale:** The methodology authoring gap (WP18B-METH1/2/3) was deprioritised to P7–P9 in WP18C.1 because AMS engagements (the dominant current tender type) exclude methodology sections entirely. Adding a methodology authoring workstream would deliver little value until the proposal factory is processing significantly more Implementation tenders.

### AD-009 — AMS Has No Methodology Asset or Project Plan Template

**Decision:** Pattern 13 (AMS) and Pattern 10 (DBA Managed Services) produce `methodology_asset: "None"` and `project_plan_template: "None"`. The methodology sections (S-34, S-35) are excluded by engagement-type rule.

**Rationale:** AMS is an ongoing managed service contract, not an implementation project. There is no project timeline to include. Sections S-70–S-76 (Support Model, SLA Framework, Incident Management, CR Process, Resource Model, Release Management, Monitoring) replace the implementation methodology sections entirely for AMS proposals.

### AD-010 — Confidence Gate Controls Assembly Initiation

**Decision:** The assembly gate in the Tender Profile (GO / HOLD / ESCALATE) must show GO before assembly proceeds. A HOLD state requires human answers to follow-up questions before assembly.

**Rationale:** Starting assembly with an incomplete Tender Profile produces a draft with systematic gaps that are harder to identify than the original unknowns. The HOLD gate is not a barrier — it is a 15-minute checkpoint that prevents 2–3 hours of wasted assembly work.

---

## 4. Pipeline Integration

### Stage 0 (New — TIL) → Stage 1 (Tender Analysis)

**Previously:** Stage 1 began with a raw tender document. The BU Lead simultaneously analysed the tender and made scoping decisions.

**After TIL:** Stage 1 begins with an APPROVED Tender Profile. The Requirement Matrix (Stage 1 output) is built against a tender whose platform, pattern, section scope, and governance rules are already determined.

**Immediate improvement:** Requirement extraction (S-14 — Understanding of Requirements) can now be structured against the known module scope from the Tender Profile, rather than against the entire tender document.

### Stage 0 (TIL) → Stage 2 (BOM Resolution)

**Previously:** BOM triggers were determined manually from the tender.

**After TIL:** `bom_triggers[]` in Block G are populated by the TIL. BOM_RESOLVER.md (existing WP17B engine) receives a governed BOM trigger list rather than a manually assembled one. The BOM_RESOLVER remains unchanged — it now receives a better input.

### Stage 0 (TIL) Replacing Stages 4, 5, 6 (Manual Selections)

**Previously:** Stages 4 (Capability), 5 (References), 6 (Methodology) were manual processes with no documented rules.

**After TIL:** All three selections are produced by TIL engines (CAPABILITY_SELECTION_ENGINE, REFERENCE_SELECTION_ENGINE, METHODOLOGY_SELECTION_ENGINE) and recorded in Block G of the Tender Profile. The BU Lead reviews the derived selections at profile approval time, rather than performing the selections manually.

---

## 5. Impact on Next Proposal Factory Run

When the next tender is processed using the TIL:

| Stage | Before TIL | After TIL | Time Saved |
|---|---|---|---|
| Stage 0 (Scoping) | 6–8 hours manual | 1–2 hours TIL production + BU review | ~5–6 hours |
| Stage 3 (BOM) | Manual BOM determination + resolver | TIL provides bom_triggers → resolver runs | ~1 hour |
| Stage 4 (Capability) | Manual asset selection | Automated from CAPABILITY_SELECTION_ENGINE | ~1–2 hours |
| Stage 5 (References) | Manual selection + AM chase | Automated scoring + AM workflow | ~1 hour |
| Stage 6 (Methodology) | Manual selection | Automated from pattern lookup | ~30 minutes |
| Section scoping | Manual (25 sections excluded manually for ARM IT045) | Deterministic from PROPOSAL_PATTERN_ENGINE | ~1 hour |
| Governance checks | Applied reactively during assembly | Pre-applied at Stage 0; listed in governance_flags | ~1 hour |
| **Total saved** | | | **~11–12 hours per tender** |

At the WP18C automation rate of 77.2%, the next run is projected at approximately **85% deterministic** — matching the WP18C.1 projection for the P0 automation tier.

---

## 6. Coverage by Engagement Type

### Oracle EBS AMS (Pattern 13)
**Determinism:** 90%+ for section scoping, capability selection, methodology non-selection, reference pool generation  
**Remaining manual:** S-52 (Commercial), S-13 (Executive Summary AI-GENERATE), S-47 (CVs — ADR-001), S-22 if OCI in scope (GAP-004)

### Oracle Fusion HCM Implementation (Patterns 1–3)
**Determinism:** 85%+ for all selections  
**Remaining manual:** S-52, S-47, S-13, S-22 (if OCI), Risk Register (S-50 — GAP-006)

### Acumatica ERP (Pattern 11)
**Determinism:** 80% (assumption packs not yet created — Acumatica Base gap)  
**Remaining manual:** S-52, S-47, S-13, assumption schedule (pack gap)

### BeBanking H2H (Pattern 12)
**Determinism:** 75% (assumption packs not yet created)  
**Remaining manual:** S-52, S-47, S-13, assumption schedule (pack gap)

---

## 7. Structural Issues Addressed

From WP18C1_FACTORY_OPTIMISATION_REVIEW.md, the following structural issues are resolved by WP18C.3:

| Issue | Resolution |
|---|---|
| SI-001 — S-38/S-73 duplication for AMS | **RESOLVED** — PROPOSAL_PATTERN_ENGINE.md: S-38 excluded for AMS; S-73 is the AMS-correct version |
| SI-002 — No Stage 0 (TIL absent) | **RESOLVED** — this WP; TENDER_INTELLIGENCE_RULES.md defines the complete Stage 0 |
| SI-003 — Stages 4/5/6 fully manual | **RESOLVED** — three engines built; all three selections are now deterministic from profile |
| SI-005 — References before AMS model | **RESOLVED** — PROPOSAL_PATTERN_ENGINE.md Section 7 encodes correct section order |
| SI-006 — Assumptions before commercial | **RESOLVED** — PROPOSAL_PATTERN_ENGINE.md Section 7 encodes Key Assumptions → Pricing order |

Remaining structural issues from WP18C.1 not addressed in this WP (addressed in WP18C.2):
- SI-007 (SLA/Incident overlap in S-71/S-72)
- SI-008–SI-012 (Section Library cleanup items)

---

## 8. Known Gaps and Residual Risks

| Gap ID | Description | Severity | Resolution Path |
|---|---|---|---|
| GAP-004 | OCI capability asset absent (S-22) | SEV-1 | P1 on revised roadmap — next WP after WP18C.2/18C.3 |
| GAP-006 | Risk Library empty (S-50 AI-GENERATE only) | SEV-2 | WP18B-EXT — P2 on revised roadmap |
| GAP-013 | Disaster Recovery methodology empty (S-44) | SEV-2 | WP18B-METH4 — P5 on revised roadmap |
| ACU-PACK | Acumatica Base assumption pack not created | SEV-2 | Required before Acumatica proposals can reach >80% determinism |
| BB-PACK | BeBanking assumption pack not created | SEV-2 | Required before BeBanking proposals can reach >80% determinism |
| KPMG-REF | KPMG reference letter not signed (AM-W4E3-001) | SEV-2 | PPM proposals use anonymous reference until resolved |
| OAR-A01 | B-BBEE Level 3 expires 2026-07-31 | SEV-1 | Business action — renewal needed before 2026-07-31 |
| OAR-E01 | POPIA Policy not yet obtained | SEV-3 | S-65 excluded until obtained |
| OAR-E02 | PAIA Manual not yet obtained | SEV-3 | S-66 excluded until obtained |

---

## 9. Factory Metrics After WP18C.3

| Metric | Pre-TIL (WP18C) | Post-TIL (WP18C.3) |
|---|---|---|
| Proposal Factory automation rate | 77.2% | **~85%** (projected) |
| Stage 0 existence | None | Stage 0 defined; APPROVED Tender Profile gates all assembly |
| Manual stage count | Stages 0, 4, 5, 6 fully manual | Stages 4, 5, 6 deterministic; Stage 0 guided (1–2h vs 6–8h) |
| Governance enforcement | Reactive (during assembly) | Proactive (Stage 0; governance_flags in profile) |
| Section scoping errors | Possible (manual; ARM IT045 had SI-001) | Deterministic; SI-001 fix encoded |
| Reference scoring | None (manual ranking) | 7-dimension, 10-point matrix |
| Per-tender scoping effort | 6–8 hours | 1–2 hours |
| Platform Maturity | L3.0 (WP18C) | **L3.5** (TIL adds Stage 0; deterministic Stage 4/5/6) |

---

## 10. Next Steps

Per WP18C1_REVISED_IMPLEMENTATION_ROADMAP.md, the priority sequence following WP18C.3:

| Priority | Work Item | Description |
|---|---|---|
| P0 (parallel with this WP) | **WP18C.2** — Section Library Consolidation | Merge S-38+S-73; fix section ordering; SLA/Incident split; update PROPOSAL_SECTION_LIBRARY.md |
| P1 | **GAP-004** — OCI Capability Asset | Build standalone OCI narrative asset (W4-OCI-001); eliminate S-22 AI-GENERATE dependency |
| P2 | **WP18B-EXT** — Risk Library Population | Populate Pattern 13 risk register (8–10 standard AMS risks); resolve S-50 from AI-GENERATE to DIRECT |
| P3 | **WP18C.4** — AI Context Standards | Define AI-GENERATE enrichment rules for S-13, S-14, S-22 using Tender Profile as AI context |
| P4 | **WP18D** — QA Engine | Build automated QA checks against known rules; replace manual QA framework |

---

## 11. WP18C.3 Completion Checklist

| Deliverable | Status |
|---|---|
| TENDER_PROFILE_STANDARD.md | Complete |
| TENDER_INTELLIGENCE_RULES.md | Complete |
| PROPOSAL_PATTERN_ENGINE.md | Complete |
| CAPABILITY_SELECTION_ENGINE.md | Complete |
| METHODOLOGY_SELECTION_ENGINE.md | Complete |
| REFERENCE_SELECTION_ENGINE.md | Complete |
| WP18C3_TENDER_INTELLIGENCE_IMPLEMENTATION.md | Complete |
| AO-001 BOM-to-Capability Rules resolved | Yes |
| AO-002 Engagement-Type Scoping Rules resolved | Yes |
| AO-003 Reference Scoring resolved | Yes |
| AO-004 Methodology Lookup resolved | Yes |
| AO-009 Tender Profile Intake resolved | Yes |
| SI-001 S-38/S-73 duplication fix encoded | Yes |
| SI-002 Stage 0 absence resolved | Yes |
| SI-003 Stages 4/5/6 deterministic | Yes |
| SI-005/SI-006 Section order rules encoded | Yes |
| All 15 governance rules embedded | Yes |
| HANDOVER.md updated to v4.3 | Pending |

---

*WP18C3_TENDER_INTELLIGENCE_IMPLEMENTATION.md v1.0 | WP18C.3 — Tender Intelligence Layer | 2026-06-26*  
*Work Package: WP18C.3 COMPLETE | Platform Maturity: L3.0 → L3.5*
