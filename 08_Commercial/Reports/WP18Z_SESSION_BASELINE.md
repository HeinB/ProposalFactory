---
document_id: WP18Z-SESSION-BASELINE
title: "WP18Z — Session Closeout and Baseline Lock"
version: "1.0"
status: "Complete"
created: "2026-06-26"
created_by: "WP18Z — Session Closeout"
category: "Reports / Governance"
scope: "Authoritative baseline document locked at WP18C.3 completion. All factory components, maturity metrics, roadmap, and resume instructions as at 2026-06-26. A future session can restart cleanly from this document without historical investigation."
---

# WP18Z — Session Closeout and Baseline Lock

**Date:** 2026-06-26 | **Version:** 1.0 | **Status:** Complete  
**Baseline locked at:** WP18C.3 — Tender Intelligence Layer (COMPLETE 2026-06-26)  
**Platform Maturity:** L3.5

---

## 1. Executive Summary

### Current Platform State

The APPSolve Proposal Factory is operational at Platform Maturity Level 3.5. The factory can produce a complete, governed proposal for any Oracle EBS AMS, Oracle Fusion HCM, Oracle Fusion ERP, Acumatica, or BeBanking tender from the Knowledge Base without starting from scratch.

The following major components are complete:

| Component | Status | Maturity |
|---|---|---|
| Knowledge Base (Capability Assets) | COMPLETE | 49 assets, all Approved v1.0 |
| Assumption Library | COMPLETE | 13 packs, 1,136 assumptions, all Approved v1.0 |
| Governance Programme | COMPLETE | 0 outstanding decisions; 0 draft assumptions |
| Assembly Engine | PRODUCTION READY | WP17C — 5/5 regression tests pass |
| Proposal Factory Architecture | COMPLETE | 10-stage pipeline defined |
| Tender Intelligence Layer | OPERATIONAL | Stage 0 + Stages 4/5/6 deterministic |
| Proposal Assembly | PROVEN | ARM IT045 57 sections assembled |

### Current Automation

| Metric | Value |
|---|---|
| Current automation rate | **~85%** (projected; WP18C measured 77.2%; TIL adds ~8 pp) |
| Theoretical maximum | ~91% (CVs and commercial pricing permanently non-automatable) |
| Minimum permanent manual effort | ~12–16 hours per tender (team 8–12h + commercial 2–4h) |
| Current manual effort (actual) | ~20–26 hours per tender |
| Target manual effort (18-month) | ~15–20 hours per tender |
| Automation floor | Stage 0 (TIL): 1–2h; Stages 4/5/6: now deterministic |

### Current Production Limitations

| Limitation | Impact | Blocking? | Path |
|---|---|---|---|
| OCI capability asset absent (GAP-004) | S-22 is AI-GENERATE for all OCI-scope tenders | No | WP = GAP-004 (P1) |
| Risk Library empty | S-50 (Risk Register) AI-GENERATE | No | WP = WP18B-EXT (P2) |
| Section Library not yet updated | PROPOSAL_SECTION_LIBRARY.md predates PROPOSAL_PATTERN_ENGINE.md S-38 exclusion rule | No | WP = WP18C.2 (NEXT) |
| B-BBEE Level 3 expires 2026-07-31 | All submissions post-date: flag OAR-A01 | Business blocker | OAR-A01 human action |
| CVs: ADR-001 permanent | Named team sections always PLACEHOLDER | Permanent | No fix path |
| Commercial pricing: permanent | S-52 always PLACEHOLDER | Permanent | No fix path |
| QA Engine not built | QA is manual (12-category framework exists) | No | WP = WP18D (P4) |
| Rendering not built | Output is Markdown only; Word/PDF manual | No | WP = WP19 (P8) |
| KPMG reference blocked | PPM proposals use anonymous reference | Business blocker | AM-W4E3-001 — AM action |

---

## 2. Repository Statistics

### Knowledge Base Assets

| Category | Count | Status |
|---|---|---|
| Total approved capability assets | **49** | All Approved v1.0 |
| Cross-BU assets | 6 | — |
| Oracle assets | 21 | — |
| Acumatica assets | 9 | — |
| BeBanking assets | 11 | — |
| Cross-platform (methodology) | 2 | W2S1-005 + W5-METH-001 |

### Assumption Library

| Metric | Value |
|---|---|
| Total assumption packs | **13** |
| Total approved assumptions | **1,136** |
| Draft assumptions | **0** |
| Outstanding governance decisions | **0** |
| Governance Programme status | **COMPLETE (WP16C 2026-06-19)** |

| Pack | Count |
|---|---|
| HCM Base | 115 |
| HCM Recruiting | 54 |
| HCM Learning | 37 |
| HCM Talent | 31 |
| HCM Compensation | 30 |
| OIC Integration | 104 |
| Oracle ERP | 123 |
| AMS / Managed Services | 84 |
| OCI Infrastructure | 174 |
| Acumatica Base | 152 |
| BeBanking Base | 117 |
| EBS SLA Overlay | 53 |
| EBS DRM Overlay | 62 |
| **Total** | **1,136** |

### Proposal Factory Components

| Component | Count | Location |
|---|---|---|
| Delivery patterns | **13** | DELIVERY_PATTERN_LIBRARY.md |
| Proposal sections | **82** | PROPOSAL_SECTION_LIBRARY.md |
| Methodology assets | **2** | W2S1-005 + W5-METH-001 |
| BOMs | **16** | TENDER_BOM_LIBRARY.md |
| Assembly engine components | **6** | Assembly_Engine/ (WP17B) |
| TIL engine files | **6** | Assembly_Engine/ (WP18C.3) |
| Governance rules (TIL) | **15** | TENDER_INTELLIGENCE_RULES.md |
| Assembly rules | **6 + 4 suppression** | RULE_PROCESSOR.md |
| Compliance items | **17** | COMPLIANCE_REGISTER.csv |

### Reference Letters

| Category | Count | Notes |
|---|---|---|
| Oracle active references | 11 | REF-ORA-001 through REF-ORA-011 |
| Acumatica active references | 5 | REF-ACU-001 through REF-ACU-005 |
| Hollywood Bets | 1 | AM approval per-tender |
| Blocked (KPMG) | 1 | AM-W4E3-001 ACTIVE |
| Archived/excluded | 6 | Including DFA (permanent) |
| **Total usable** | **17 (15 confirmed + HB pending + KPMG blocked)** | — |

### Consultants

| Category | Count |
|---|---|
| Oracle consultants indexed | 37 |
| Cross-BU consultants | 7 |
| Associates | 5 |
| **Total indexed** | **49** |
| Automation rate for CVs | 0% (ADR-001 permanent — APPTime only) |

### Factory Automation (WP18C baseline + TIL projection)

| Section Type | WP18C Count | Automation | Sections |
|---|---|---|---|
| DIRECT (deterministic, no edit) | ~24 | ~100% | Most corporate, compliance, assumption pack outputs |
| EXTRACT (deterministic from asset) | ~12 | ~90% | Platform capability sections |
| MERGE (combine multiple assets) | ~8 | ~80% | Solution overview, scope, references |
| AI-GENERATE (AI required) | ~8 | ~50% | Executive summary, UoR, OCI, risk register |
| TEMPLATE (structure only) | ~3 | ~20% | Commercial pricing, rate card, estimation |
| PLACEHOLDER (human required) | ~2 | 0% | CVs, commercial pricing |
| **Total in-scope (AMS example)** | **~43** | **~85%** | — |

---

## 3. Proposal Factory Architecture

### Component Map

```
Stage 0: Tender Intelligence Layer (TIL) — NEW WP18C.3
    TENDER_PROFILE_STANDARD.md      → YAML schema (8 blocks; 30+ fields)
    TENDER_INTELLIGENCE_RULES.md    → 10-step processing; trigger matrix; 15 governance rules
    PROPOSAL_PATTERN_ENGINE.md      → 13 patterns; section scoping rules (AO-002)
    CAPABILITY_SELECTION_ENGINE.md  → BOM→asset lookup; deselection rules
    METHODOLOGY_SELECTION_ENGINE.md → Pattern→methodology; phase structures
    REFERENCE_SELECTION_ENGINE.md   → 7-dim scoring; 12 exclusion rules; AM workflow

Stage 1: Tender Analysis → [TENDER_ID]_REQUIREMENT_MATRIX.md
    Manual: BU Lead reads tender; extracts requirements
    Engine: None built yet

Stage 2: Requirement Extraction → Understanding of Requirements
    Partially automated: AI-GENERATE with Tender Profile context (WP18C.4 will formalise)

Stage 3: BOM Resolution → Pack Manifest [PRODUCTION READY — WP17B]
    BOM_RESOLVER.md                 → Tender profile + BOM codes → ordered pack manifest
    PACK_LOADER.md (v1.1)           → Pack eligibility; version check; load order
    RULE_PROCESSOR.md               → Assembly rules A–E + suppression rules S1–S4
    ASSUMPTION_EXTRACTOR.md         → Extracts + deduplicates assumptions
    ASSEMBLY_AUDITOR.md             → Full decision trail
    ENGINE_ORCHESTRATOR.md          → Entry point; sequences Steps 1–5

Stage 4: Capability Selection → [NOW DETERMINISTIC — WP18C.3]
    CAPABILITY_SELECTION_ENGINE.md  → Required: BOM triggers → capability assets
    Previously manual; now automated from Tender Profile bom_triggers[]

Stage 5: Reference Selection → [NOW DETERMINISTIC — WP18C.3]
    REFERENCE_SELECTION_ENGINE.md   → Scores + ranks 15 references; AM workflow
    Previously manual; now automated from Tender Profile platform/industry/engagement_type

Stage 6: Methodology Selection → [NOW DETERMINISTIC — WP18C.3]
    METHODOLOGY_SELECTION_ENGINE.md → Pattern → methodology asset + template
    Previously manual; now automated from Tender Profile proposal_pattern

Stage 7: Assumption Assembly → [PRODUCTION READY — WP17D-1]
    Full Assembly Engine stack (Stages 1–5 above)
    Produces: ASSUMPTION_SCHEDULE_V1 + KEY_ASSUMPTIONS_V1 + ASSEMBLY_AUDIT_REPORT
    WP17D-1: inline text assembly (594 assumptions for ARM IT045; 175 body)
    Dual-output: body section (Key Assumptions) + appendix (Complete Schedule)

Stage 8: Proposal Assembly → [PROVEN MVP — WP18C]
    Manual section-by-section assembly guided by CONTENT_SOURCE_MATRIX.md
    ARM IT045: 57 sections; 77.2% deterministic; QA 72/100
    Next run (with TIL): projected ~85% deterministic; ~43 sections for AMS

Stage 9: Proposal QA → [FRAMEWORK ONLY — WP18D FUTURE]
    PROPOSAL_QA_FRAMEWORK.md        → 12-category manual QA checklist
    Manual process; automated QA engine = WP18D (P4 on roadmap)

Stage 10: Rendering → [NOT BUILT — WP19 FUTURE]
    Output currently Markdown only
    Word/PDF rendering = WP19 (P8 on roadmap)
```

### Maturity by Stage

| Stage | Name | Maturity | Notes |
|---|---|---|---|
| 0 | Tender Intelligence (TIL) | **L3.5 — OPERATIONAL** | NEW WP18C.3; Stage 0 now exists |
| 1 | Tender Analysis | L1 — Manual | Requirement matrix built manually |
| 2 | Requirement Extraction | L2 — AI-Assisted | AI-GENERATE; no engine |
| 3 | BOM Resolution | **L5 — PRODUCTION READY** | WP17B; WP17C all pass |
| 4 | Capability Selection | **L3.5 — DETERMINISTIC** | WP18C.3 engine built |
| 5 | Reference Selection | **L3.5 — DETERMINISTIC** | WP18C.3 engine built |
| 6 | Methodology Selection | **L3.5 — DETERMINISTIC** | WP18C.3 engine built |
| 7 | Assumption Assembly | **L5 — PRODUCTION READY** | WP17D-1; inline text |
| 8 | Proposal Assembly | L3.0 — MVP | WP18C; 77.2% deterministic |
| 9 | QA | L1 — Manual Framework | WP18D future |
| 10 | Rendering | L0 — Not Built | WP19 future |

### Overall Platform Maturity: **L3.5**

**L3.5 definition:** Stage 0 (TIL) operational and deterministic; Stage 3 and 7 (assumption assembly) production-grade; Stages 4/5/6 deterministic; Proposal assembly proven at MVP; full pipeline defined. Human input required for: requirement analysis (Stage 1), AI-assisted sections (Stage 2, S-13, S-14), team/CVs (permanent), commercial pricing (permanent), QA (Stage 9), and rendering (Stage 10).

---

## 4. Current Roadmap

### COMPLETE

| WP | Description | Date |
|---|---|---|
| W1–W4+WP7 | Capability asset extraction and approval (49 assets) | 2026-06-10 to 2026-06-14 |
| WP8 | Compliance Register | 2026-06-15 |
| WP9 | Reference Registration (16 letters) | 2026-06-15 |
| WP10 | Consultant Index (49 consultants) | 2026-06-15 |
| WP11F | Commercial Framework (5 documents approved) | 2026-06-16 |
| WP12 | Proposal Assembly Reference Library (8 documents) | 2026-06-16 |
| WP11H/H-A | OCI Infrastructure Assumption Pack (174 approved) | 2026-06-16 |
| WP11I/11I-A | Acumatica Base Assumption Pack (152 approved) | 2026-06-16/18 |
| WP11J | BeBanking Base Assumption Pack (117 approved) | 2026-06-16 |
| WP13 | Governance Approval Campaign | 2026-06-16 |
| WP14 series | Assumption pack validation and remediation | 2026-06-17/18 |
| WP15 series | Pack promotion and decision closure | 2026-06-18/19 |
| WP16A–D | Assumption library reconciliation and promotion; GOVERNANCE COMPLETE | 2026-06-19 |
| WP17A | Repository Hygiene and Assembly Readiness | 2026-06-19 |
| WP17B | Assembly Engine MVP (6 components; OPERATIONAL) | 2026-06-19 |
| WP17C | Assembly Engine Regression Tests (5/5 PASS; PRODUCTION READY) | 2026-06-22 |
| WP17D-0 | Assumption Schedule Design Standard | 2026-06-22 |
| WP17D-0A | Assumption Schedule Consumption Model (Option B approved) | 2026-06-22 |
| WP17D-1 | Inline Text Assembly — ARM IT045 (594+175 assumptions) | 2026-06-25 |
| WP18A | Proposal Factory Architecture (10-stage pipeline; 82 sections; 8 deliverables) | 2026-06-25 |
| WP18B | Methodology and Risk Library Foundation | 2026-06-25 |
| WP18C | Proposal Factory Assembly Engine v1.0 (ARM IT045 MVP) | 2026-06-25 |
| WP18C.1 | Proposal Factory Optimisation (15 AOs; revised roadmap) | 2026-06-25 |
| WP18C.3 | Tender Intelligence Layer (6 engine files; Stage 0 + Stages 4/5/6 deterministic) | 2026-06-26 |

### IMMEDIATE NEXT (see Section 6)

| Priority | WP | Description | Effort |
|---|---|---|---|
| **NEXT** | **WP18C.2** | Section Library Consolidation | 2–3h |
| P1 | GAP-004 | OCI Capability Asset (W4-OCI-001) | 4–8h + BU review |
| P2 | WP18B-EXT | Risk Library Population (Pattern 13 AMS risks) | 4–6h |

### IN PROGRESS / ACTIVE (BUSINESS ACTIONS — human-only)

| Item | Owner | Status | Deadline |
|---|---|---|---|
| OAR-A01 — B-BBEE renewal | Finance Director | **URGENT** | 2026-07-31 |
| OAR-C01 — Hollywood Bets AM approval (Plennegy) | Oracle BU Lead | Blocked | Before Plennegy submission |
| OAR-C02 — Plennegy costing section | Commercial Director + Bid Manager | In progress | Before Plennegy submission |
| OAR-B02 — KPMG reference letter | Oracle BU Lead | Open | — |

### DEFERRED (deliberate — see Section 7)

| Priority | WP | Description | Reason for Deferral |
|---|---|---|---|
| P3 | WP18C.4 | AI Context Standards | Needs WP18C.3 stable before defining AI enrichment rules |
| P4 | WP18D | QA Engine | After automation rate confirmed >85% |
| P5 | WP18B-METH4 | Security/DR Methodology | S-44 empty; low AMS demand |
| P6 | CONSULTANT_INDEX AMS tags | Add AMS role tags to index | Low impact; AMS uses shared pool |
| P7 | WP18B-METH2 | Oracle ERP Methodology | SME needed; low ERP tender volume |
| P8 | WP19 | Rendering Engine | After QA engine (WP18D) |
| P9 | WP18B-METH1 | Cross-BU Methodology | AMS tenders exclude methodology sections; very low ROI |

---

## 5. Resume Instructions

A future session can resume cleanly by reading these files **in this order**:

| Priority | File | Why |
|---|---|---|
| 1 | `HANDOVER.md` | Current programme state; active blockers; priority table; System Maturity table |
| 2 | `AI_CONTEXT.md` | Full company context; capability assets; governance rules; assumption library; commercial framework |
| 3 | `08_Commercial/Reports/WP18Z_SESSION_BASELINE.md` | This document; complete factory baseline; roadmap; resume point |
| 4 | `08_Commercial/Reports/WP18C1_REVISED_IMPLEMENTATION_ROADMAP.md` | Governing roadmap for all future factory development (supersedes WP18B plan) |
| 5 | `08_Commercial/Assembly_Engine/TENDER_INTELLIGENCE_RULES.md` | TIL processing sequence; downstream trigger matrix |
| 6 | `08_Commercial/Assembly_Engine/PROPOSAL_PATTERN_ENGINE.md` | Pattern classification; section scoping rules |
| 7 | `06_Capabilities/MASTER_CAPABILITY_INDEX.md` | All 49 assets; governance per asset; approved_for_reuse status |

**For a new tender run specifically**, also read:
- `08_Commercial/Assembly_Engine/TENDER_PROFILE_STANDARD.md` — to produce the Tender Profile
- `08_Commercial/Assembly_Engine/CAPABILITY_SELECTION_ENGINE.md` — to select capability assets
- `08_Commercial/Assembly_Engine/REFERENCE_SELECTION_ENGINE.md` — to score references
- `08_Commercial/Assembly_Engine/ENGINE_ORCHESTRATOR.md` — to run the assembly engine

**For WP18C.2 (NEXT session)**, specifically read:
- `08_Commercial/Assembly_Engine/PROPOSAL_SECTION_LIBRARY.md` — current state (needs updating)
- `08_Commercial/Assembly_Engine/PROPOSAL_PATTERN_ENGINE.md` — the rules that PROPOSAL_SECTION_LIBRARY.md must align with
- `08_Commercial/Assembly_Engine/CONTENT_SOURCE_MATRIX.md` — companion document for section-to-source mapping

**No historical investigation required.** This document plus HANDOVER.md is sufficient to restart any factory work from scratch.

---

## 6. Immediate Next Work: WP18C.2 — Section Library Consolidation

### Brief

**Work Package:** WP18C.2  
**Objective:** Update the PROPOSAL_SECTION_LIBRARY.md to be internally consistent with the new PROPOSAL_PATTERN_ENGINE.md and associated structural fix SI-001. Also resolve SI-007 (SLA/Incident overlap). No new architecture; documentation alignment only.

### Scope

**1. Merge S-38 into S-73 for AMS (SI-001)**

The PROPOSAL_PATTERN_ENGINE.md now encodes that S-38 (Change Control Framework) is EXCLUDED for AMS engagements and replaced by S-73 (Change Request Process). This rule exists in the engine but PROPOSAL_SECTION_LIBRARY.md has not been updated to reflect it.

Required change in PROPOSAL_SECTION_LIBRARY.md:
- Section S-38 entry: add note `exclude_if: engagement_type = AMS` and reference `see S-73`
- Section S-73 entry: add note `replaces S-38 for AMS engagements`
- Update section counts table (Section 12)

**2. Resolve SI-007 — SLA/Incident Content Overlap**

Sections S-71 (SLA Framework) and S-72 (Incident Management) currently have overlapping content in the AMS assumption pack. The clean boundary:
- S-71 (SLA Framework): SLA tiers (P1/P2/P3/P4 response times), service hours (SAST Mon–Fri 08:00–17:00), coverage exclusions (24x7 excluded unless contracted), response ≠ resolution language
- S-72 (Incident Management): Incident classification process, escalation path, incident lifecycle (log → triage → assign → resolve → close → review), communication standards

Add this boundary definition to both sections' entries in PROPOSAL_SECTION_LIBRARY.md to prevent assembler from duplicating content across both sections.

**3. Align Content Source Matrix**

CONTENT_SOURCE_MATRIX.md section mappings for S-38 and S-73 need to be updated to reflect:
- S-38: excluded for AMS; source = `Commercial Framework (CR_PRICING_MODEL.md)` for implementation
- S-73: AMS-specific; source = `AMS pack + CR_PRICING_MODEL.md`; note: do not expose CR rate thresholds

**4. Update Proposal Assembly Sequence**

PROPOSAL_ASSEMBLY_SEQUENCE.md Step 15 currently lists S-38 as part of commercial/compliance assembly. For AMS, this step should note that S-38 is replaced by S-73 (assembled in Step 15 with AMS sections or Step 16 with AMS support model).

**5. Regression Validation**

After updates, verify:
- ARM IT045 (AMS) section scope is unchanged and S-38 exclusion is consistent with all three documents
- A hypothetical Implementation tender still includes S-38 and excludes S-73

### Expected Outputs

| File | Change |
|---|---|
| `PROPOSAL_SECTION_LIBRARY.md` | S-38: add AMS exclusion note; S-73: add AMS-replaces-S-38 note; SI-007 boundary definitions |
| `CONTENT_SOURCE_MATRIX.md` | S-38 source note + AMS exclusion; S-73 source note |
| `PROPOSAL_ASSEMBLY_SEQUENCE.md` | Step 15 note for AMS pattern |

### Expected Impact

| Metric | Before WP18C.2 | After WP18C.2 |
|---|---|---|
| Section Library internally consistent | No (SI-001 fix in engine but not in library) | Yes |
| SI-007 resolved | No | Yes |
| QA score (ARM IT045 re-run) | 72/100 | ~74–75/100 (SI-001 + SI-007 = approx +2–3 pts) |
| Automation improvement | ~85% | ~85–86% (marginal; mostly QA accuracy) |

### Effort Estimate

2–3 hours. Read 3 files; make targeted edits to 3 files; validate consistency.

---

## 7. Platform Health

### Known Issues

| ID | Issue | Severity | Impact |
|---|---|---|---|
| KI-001 | TENDER_BOM_LIBRARY.md (WP12): Acumatica Base and BeBanking Base packs noted as "NOT YET CREATED" — stale (both Approved v1.0) | SEV-3 | CAPABILITY_SELECTION_ENGINE.md was corrected WP18Z; TENDER_BOM_LIBRARY.md needs update in WP18C.2 |
| KI-002 | PROPOSAL_SECTION_LIBRARY.md: S-38 AMS exclusion rule not yet reflected (SI-001 fix is in PROPOSAL_PATTERN_ENGINE.md only) | SEV-2 | WP18C.2 NEXT |
| KI-003 | PROPOSAL_SECTION_LIBRARY.md: SI-007 SLA/Incident boundary not defined | SEV-2 | WP18C.2 NEXT |
| KI-004 | GAP-004: OCI capability asset (W4-OCI-001) absent | SEV-1 | S-22 = AI-GENERATE for all OCI tenders; P1 roadmap |
| KI-005 | Risk Library: RISK_LIBRARY_STANDARD.md defined; no risk entries yet | SEV-2 | S-50 = AI-GENERATE; WP18B-EXT P2 |
| KI-006 | AI_CONTEXT.md was last updated 2026-06-22 (WP17D-0A) — stale by 4 days | SEV-2 | Updated in WP18Z |

### Known Risks

| ID | Risk | Probability | Impact | Mitigation |
|---|---|---|---|---|
| KR-001 | B-BBEE Level 3 expires 2026-07-31 | HIGH | All SA submissions after that date blocked | OAR-A01 — Finance Director action; renewal in progress |
| KR-002 | Oracle EBS content (W2S1-002) is 2012–2014 vintage | MEDIUM | EBS capability section may appear dated | Flag for modernisation at each EBS tender; human review required |
| KR-003 | KPMG reference blocked (AM-W4E3-001) | MEDIUM | PPM proposals limited to anonymous reference | OAR-B02 — AM contact needed |
| KR-004 | Hollywood Bets AM approval per-tender | LOW-MEDIUM | HCM proposals may lose top-scored reference if AM unavailable | Per-tender AM engagement planned |
| KR-005 | TIL is a documentation engine not an execution engine | LOW | "Deterministic" means governed rules, not automated software | Rules are encoded; human must apply them; automation converts to software later |

### Technical Debt

| Item | Description | Impact | Priority |
|---|---|---|---|
| TD-001 | TENDER_BOM_LIBRARY.md (WP12): stale pack creation status for Acumatica + BeBanking | Low — CAPABILITY_SELECTION_ENGINE.md corrected | WP18C.2 |
| TD-002 | PROPOSAL_STRUCTURE_LIBRARY.md (WP12): predecessor to PROPOSAL_SECTION_LIBRARY.md — not updated for WP18A/18B/18C changes | Low — PROPOSAL_SECTION_LIBRARY.md is authoritative | Review in WP18C.2 |
| TD-003 | CONTENT_SOURCE_MATRIX.md: S-38/S-73 entries need WP18C.3 alignment | Medium | WP18C.2 |
| TD-004 | PROPOSAL_ASSEMBLY_SEQUENCE.md: AMS pattern notes for S-38→S-73 replacement not present | Medium | WP18C.2 |
| TD-005 | Assumption pack ID naming: EBS-SLA and EBS-DRM overlays are named as "overlays" in the library but function as standard packs — minor naming inconsistency | Low | No fix needed |

### Deliberately Manual Steps (permanent)

These steps are **never automatable** and are documented here to prevent future work packages from attempting to automate them:

| Step | Reason | Sections Affected |
|---|---|---|
| CV authoring | ADR-001: APPTime is the sole source of truth for consultant CVs | S-47, S-48, A-02 |
| Commercial pricing | Commercial Director authority; rate exposure restrictions | S-52, S-53, S-54 |
| AM approval for references | Per-tender; client relationship is dynamic | All references |
| B-BBEE certificate | Externally issued; annual renewal | S-59, A-05 |
| BU Lead sign-off | Governance requirement; human accountability | All proposals |

### Deliberately Deferred Items

| Item | Deferral Reason |
|---|---|
| WP18B-METH1 Cross-BU Methodology (P9) | AMS tenders exclude methodology sections entirely; very low ROI until implementation tender volume increases |
| WP18B-METH2 Oracle ERP Methodology (P7) | SME workshops required; ERP tender volume currently lower than AMS |
| WP18B-METH3 Acumatica/BeBanking Methodology | SME workshops required |
| WP19 Rendering Engine (P8) | Word/PDF conversion is a manual step that can be performed adequately by a human; automation benefit is modest compared to QA engine and content gaps |
| WP18D QA Engine (P4) | Manual QA framework is sufficient until automation rate stabilises above 85% |

---

## 8. Session Integrity Check

### Architecture Document Consistency

| Document | Last Updated | Consistent with WP18C.3? |
|---|---|---|
| TENDER_PROFILE_STANDARD.md | 2026-06-25 (WP18C.3) | YES — new document |
| TENDER_INTELLIGENCE_RULES.md | 2026-06-25 (WP18C.3) | YES — new document |
| PROPOSAL_PATTERN_ENGINE.md | 2026-06-25 (WP18C.3) | YES — new document; SI-001 fix encoded |
| CAPABILITY_SELECTION_ENGINE.md | 2026-06-26 (WP18Z corrected) | YES — corrected for Acumatica/BeBanking pack status |
| METHODOLOGY_SELECTION_ENGINE.md | 2026-06-25 (WP18C.3) | YES — new document |
| REFERENCE_SELECTION_ENGINE.md | 2026-06-25 (WP18C.3) | YES — new document |
| PROPOSAL_FACTORY_ARCHITECTURE.md | 2026-06-25 (WP18A/18B) | PARTIAL — predates TIL; Stage 0 not yet reflected |
| PROPOSAL_SECTION_LIBRARY.md | 2026-06-25 (WP18A/18B) | PARTIAL — SI-001 fix not reflected; WP18C.2 will update |
| CONTENT_SOURCE_MATRIX.md | 2026-06-25 (WP18A/18B) | PARTIAL — S-38/S-73 entries predate TIL; WP18C.2 will update |
| PROPOSAL_ASSEMBLY_SEQUENCE.md | 2026-06-25 (WP18A) | PARTIAL — Stage 0 not reflected; WP18C.2 will update |
| TENDER_BOM_LIBRARY.md | 2026-06-16 (WP12) | PARTIAL — stale pack status for Acumatica/BeBanking; WP18C.2 will update |
| DELIVERY_PATTERN_LIBRARY.md | 2026-06-16 (WP12) | YES — patterns unchanged |
| BOM_RESOLVER.md | 2026-06-19 (WP17B) | YES — engine unchanged; now receives better input from TIL |
| ASSEMBLY_RULES_ENGINE.md | 2026-06-19 (WP17B) | YES — rules unchanged |
| PROPOSAL_FACTORY_ARCHITECTURE.md | 2026-06-25 (WP18B v1.1) | YES — architecture unchanged; TIL adds Stage 0 |

### Memory and Governance Files

| File | Status |
|---|---|
| HANDOVER.md | UPDATED WP18Z — WP18C.3 row added; WP18C.2 priority updated |
| AI_CONTEXT.md | UPDATED WP18Z — header updated; new sections added |
| memory/MEMORY.md | UPDATED WP18Z — project context description current |
| memory/project_context.md | UPDATED WP18Z — WP18C.3 in description |

### Restartability Verdict

**The Proposal Factory is restartable without historical investigation.**

A new session that reads HANDOVER.md → AI_CONTEXT.md → WP18Z_SESSION_BASELINE.md will have:
- Complete platform context
- Complete governance rules
- Complete capability asset index reference
- Complete assumption library status
- Current roadmap priority
- Specific resume instructions for the next work package (WP18C.2)
- Known issues and deferred items

The three documents listed above are sufficient to resume any factory work. Historical WP reports are available in `08_Commercial/Reports/` for reference but are not required reading.

---

*WP18Z_SESSION_BASELINE.md v1.0 | Session Closeout | 2026-06-26*  
*Baseline locked at: WP18C.3 COMPLETE | Platform Maturity: L3.5 | Automation: ~85%*
