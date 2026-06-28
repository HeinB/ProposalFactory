---
document_id: WP18A-ARCHITECTURE-RECOMMENDATION
title: "WP18A — Proposal Factory Architecture Recommendation Report"
version: "1.0"
status: "Complete — WP18A 2026-06-25"
created: "2026-06-25"
created_by: "WP18A — Proposal Factory Architecture"
category: "Architecture Report"
scope: "Formal architecture recommendation for the Proposal Factory. Assesses current platform maturity, identifies strengths and weaknesses, records architecture decisions, identifies risks, and provides the implementation roadmap for WP18B through WP19."
---

# WP18A — Proposal Factory Architecture Recommendation Report

**Date:** 2026-06-25 | **Version:** 1.0 | **Status:** Complete  
**Work Package:** WP18A — Proposal Factory Architecture  
**Baseline:** 13 packs / 1,136 assumptions / 49 capability assets / 5 regression tests ALL PASS / WP17D-1 COMPLETE

---

## 1. Executive Summary

WP18A has designed the complete Proposal Factory architecture that transforms the Assumption Factory into a fully automated proposal production platform.

The current platform is a world-class Assumption Factory. It produces complete, validated, proposal-ready assumption schedules from a BOM code with zero manual authoring. This is Level 5 automation for its class of output.

The Proposal Factory extends this across the full proposal lifecycle — from tender receipt to rendered document. The architecture is designed to reach Level 4 automation for the majority of proposal sections, with Level 5 for all fully deterministic sections.

**Eight architecture deliverables have been produced:**

| Document | Purpose |
|---|---|
| `PROPOSAL_FACTORY_ARCHITECTURE.md` | End-to-end 10-stage pipeline blueprint |
| `PROPOSAL_SECTION_LIBRARY.md` | 82 proposal sections catalogued |
| `CONTENT_SOURCE_MATRIX.md` | Every section mapped to its source library |
| `PROPOSAL_ASSEMBLY_SEQUENCE.md` | 19-step deterministic assembly order |
| `AUTOMATION_MATURITY_MODEL.md` | L1–L5 maturity per section; implementation priorities |
| `PROPOSAL_GAP_ANALYSIS_FRAMEWORK.md` | Gap Analysis Engine design (WP18C spec) |
| `PROPOSAL_QA_FRAMEWORK.md` | QA Engine design (WP18D spec) |
| `WP18A_ARCHITECTURE_RECOMMENDATION.md` | This document — decisions and roadmap |

---

## 2. Current Platform Maturity Assessment

### 2.1 What is COMPLETE and PRODUCTION READY

| Component | Status | Quality |
|---|---|---|
| Capability Library (49 assets) | COMPLETE | All approved; governance restrictions documented; BU Lead approved |
| Assumption Library (13 packs / 1,136 assumptions) | COMPLETE | All approved v1.0; 0 draft; 0 outstanding decisions |
| Assembly Engine (6 components) | PRODUCTION READY | 5/5 regression tests PASS |
| Assumption Schedule output (full text) | PRODUCTION READY | WP17D-1 COMPLETE; 594 assumptions; 10/10 validation |
| Key Assumptions body section | PRODUCTION READY | WP17D-0A Option B; 175 body assumptions |
| Governance Programme | COMPLETE | 54 decisions resolved; 0 outstanding |
| WP12 Reference Libraries | ACTIVE | DELIVERY_PATTERN_LIBRARY (13 patterns); PROJECT_PLAN_TEMPLATES (7 templates); PROPOSAL_STRUCTURE_LIBRARY (7 structures); TENDER_BOM_LIBRARY (16 BOM codes) |

**The Assumption Factory is fully operational.** ARM IT045 can be re-assembled at any time. Five other patterns are regression-tested.

### 2.2 Current maturity by function

| Function | Current Maturity | Assessment |
|---|---|---|
| Assumption Assembly | **L5 — Fully Automated** | Best-in-class for this function |
| BOM Resolution | **L5 — Fully Automated** | Engine-driven; 0 manual decisions |
| Capability Asset Management | **L3 — Deterministic** | Assets available; selection is guided but manual |
| Reference Management | **L2 — Template-Driven** | Register exists; selection is manual |
| Methodology Selection | **L2 — Template-Driven** | Library exists; selection is manual |
| Proposal Structure | **L2 — Template-Driven** | Structure defined; assembly is manual |
| Gap Analysis | **L1 — Manual** | No engine; Bid Manager assesses informally |
| Proposal QA | **L1 — Manual** | No engine; BU Lead reviews manually |
| Document Rendering | **L1 — Manual** | Manual DOCX assembly |

---

## 3. Strengths

### 3.1 Assumption Factory is an exceptional foundation

The Assumption Factory is the strongest possible foundation for the Proposal Factory. The hardest technical problem — deterministic assembly of 1,136 commercial assumptions from 13 packs, with suppression rules, grouping, numbering, traceability, and dual-output formatting — is completely solved. The Proposal Factory inherits this capability without modification.

### 3.2 Governance architecture is complete

The governance framework that protects APPSolve from commercial and reputational risk is complete. 54 BU decisions are recorded. 13 packs are approved. The governance architecture is strong enough to extend to all Proposal Factory content without redesign.

### 3.3 WP12 reference library is underutilised

WP12 produced DELIVERY_PATTERN_LIBRARY (13 patterns), PROJECT_PLAN_TEMPLATES (7 templates), PROPOSAL_STRUCTURE_LIBRARY (7 structures), and TENDER_BOM_LIBRARY. These are production-quality assets that the factory can use immediately. They are currently used only in the Plennegy manual assembly process. Integrating them into WP18B provides significant automation uplift at low additional effort.

### 3.4 Strong KB IP base

49 approved capability assets cover every product in the portfolio. The content quality is high and the governance restrictions are well-documented. The assembly AI will have unambiguous, approved source material for most proposal sections.

### 3.5 Commercial Framework is approved

The Commercial Framework (5 documents, Approved v1.0) provides the governing structure for all commercial sections. The rate card structure, estimation methodology, CR pricing model, and effort multipliers are defined. This provides the Proposal Factory with a credible commercial assembly framework even before pricing automation is available.

---

## 4. Weaknesses

### 4.1 Methodology Library is almost empty

`05_Methodologies/` has 7 subfolders but only 1 file (W2S1-005 Oracle Implementation Methodology). Six subfolders are empty: Disaster Recovery, Managed Services, Project Management, Security, Support, Testing. This directly blocks 6 proposal sections (S-34 alternative patterns, S-37, S-39, S-44, S-45, and AMS-specific content).

**Remediation:** Author 6 methodology documents using the same extraction-first approach as the Capability Library build. Priority: Implementation → Security → Testing → Support → Project Management → Disaster Recovery.

### 4.2 No Risk Library

There is no Risk Library, no standard risk taxonomy, and no risk register template. The Risk Register (S-50) and RAID Framework (S-37) are both L1 (manual). This is the most significant structural gap outside of the methodology library.

**Remediation:** Create a Risk Library in `08_Commercial/` with a standard risk taxonomy covering Oracle ERP, HCM, OIC, OCI, AMS, Acumatica, and BeBanking risk profiles. This is a medium-effort, high-impact initiative.

### 4.3 OCI has no standalone capability narrative

The OCI assumption pack (174 assumptions) is excellent as a commercial protection document but functions poorly as a solution capability section. Clients receiving an OCI-based proposal receive assumption-pack text as their capability overview. This is not competitive for OCI-first engagements.

**Remediation:** Author a standalone OCI Infrastructure capability statement using the assumption pack and historical OCI engagement evidence as source material. Relatively low effort; high impact for OCI tenders.

### 4.4 Compliance items remain open (OAR)

Several compliance gaps have been open since WP8: POPIA Policy (OAR-E01), PAIA Manual (OAR-E02), Acumatica Partner Certificate (OAR-E03). These are not Proposal Factory architecture problems — they are human procurement actions. The Proposal Factory correctly flags them as gaps. However, until they are resolved, every tender that requires them will receive a gap marker.

### 4.5 CV Library is permanently outside the KB

ADR-001 correctly places CVs in APPTime. This is the right decision. However, it means the Proposal Factory will permanently have a human gate at the CV section. Consultant Summary Profiles (brief, not full CVs) could be partially automated using CONSULTANT_INDEX.csv metadata. This is a low-effort improvement worth implementing in WP18B.

### 4.6 Case Study Library does not exist

There is no case study library. Case studies are available in the 18,400-file historical corpus but have not been extracted and structured. For high-scoring tenders, case studies are often worth 10–20% of the technical score. This is a significant competitive gap.

**Remediation:** Extract and structure 10–15 case studies from the historical corpus. Candidate engagements: ARM IT045, MTN OIC, Investec Fusion Finance, NALA Renewables, ARM Mining EBS, Dunlop Srixon Acumatica.

---

## 5. Architecture Decisions

### AD-01: WP17 Assumption Assembly is the canonical module — do not redesign it

The Assembly Engine (WP17B/WP17C/WP17D) is production-ready and regression-tested. WP18B must call the Assembly Engine as a module — it must not duplicate or replace the assumption assembly logic. The Assembly Engine outputs (ASSUMPTION_SCHEDULE, KEY_ASSUMPTIONS) are inserted verbatim into the assembled proposal.

### AD-02: Proposal Assembly is additive over the WP12 reference library

WP12 defined proposal structures, delivery patterns, and project plan templates. WP18B must build on these — not replace them. The PROPOSAL_STRUCTURE_LIBRARY.md is the per-tender-type assembly guide. WP18B converts this from a human-reference document into an engine-executable specification.

### AD-03: Deterministic sections first — AI-generated sections second

Where content can be assembled deterministically from approved KB assets (L3 → L5), the factory assembles it deterministically. AI generation is reserved for sections where no approved KB source exists and tailoring is required (Executive Summary, Understanding of Requirements, Case Studies). This maintains governance integrity and commercial protection.

### AD-04: Commercial section is permanently a human gate

The Commercials/Pricing section will never be automated beyond L2. Commercial Director authorisation is a permanent governance requirement. The factory inserts a `[PLACEHOLDER — COMMERCIAL INPUT REQUIRED]` that is replaced manually. This is by design, not a limitation.

### AD-05: Gap Analysis runs before section assembly, not after

The Gap Analysis Engine (WP18C) runs at Step 9 — before any narrative sections are assembled. Running it after assembly would produce a gap-riddled document that is harder to rework. Running it before ensures assembly effort is only invested in sections that can be completed, and `[GAP]` markers are inserted at the right sections from the start.

### AD-06: QA score of 75+ with no CRITICAL fails is the rendering gate

A proposal may not be rendered into DOCX/PDF unless the QA score ≥ 75 and no CRITICAL checks fail. This threshold is calibrated to allow proposals with minor gaps to proceed while blocking materially incomplete proposals. The BU Lead can override by explicitly accepting risk on individual CRITICAL fails.

### AD-07: Source hierarchy applies to all assembly

The source hierarchy from AI_CONTEXT.md applies to all Proposal Factory assembly:
1. Approved content (KB) — primary
2. Reference letters — secondary
3. Historical proposal templates — extract only; do not copy verbatim
4. Historical tender submissions — extract and modernise
5. AI-generated content — last resort; mandatory review

This hierarchy is enforced at Stage 4 (Capability Selection) and Stage 8 (Proposal Assembly).

### AD-08: Interim mode preserves existing process while engines are built

WP18B, WP18C, and WP18D are future builds. In the interim, the existing process (PROPOSAL_STRUCTURE_LIBRARY as guide, manual DOCX assembly) remains valid. The 19-step assembly sequence in PROPOSAL_ASSEMBLY_SEQUENCE.md is designed to be executable manually. The QA checklist in PROPOSAL_QA_FRAMEWORK.md is executable manually today.

---

## 6. Risks

| Risk ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-01 | Methodology Library gap remains unfilled — blocking 6 proposal sections | HIGH | HIGH | Schedule methodology authoring in next work cycle; use AI-generation with human review as interim |
| R-02 | Risk Library never created — Risk Register section permanently L1 | MEDIUM | MEDIUM | Include Risk Library as WP18B prerequisite scope |
| R-03 | WP18B scope is underestimated — 82 sections × multiple tender types is large | HIGH | MEDIUM | Implement incrementally; start with corporate + solution sections; add delivery + compliance in phases |
| R-04 | Case study gap weakens scored proposals | HIGH | MEDIUM | Extract 10–15 case studies from historical corpus before next major tender |
| R-05 | OCI standalone narrative gap — OCI-first tenders are weak | MEDIUM | HIGH | Author OCI capability statement in WP18B or as standalone micro-WP |
| R-06 | B-BBEE expiry (2026-07-31) — all proposals blocked | HIGH | CRITICAL | Finance Director to renew — OAR-A01; not a factory problem |
| R-07 | CV section permanently manual — APPTime integration never built | LOW | LOW | Consultant profiles from CONSULTANT_INDEX are sufficient interim; accepted design decision |
| R-08 | AI-generated sections (S-13, S-14) produce low-quality output | MEDIUM | HIGH | Mandatory BU Lead review for all AI-generated sections; do not use AI output without approval |

---

## 7. Repository Gap Analysis — Additional Assets

### 7.1 Significant underutilised assets identified

#### WP12 Reference Library (HIGH value — not yet integrated into pipeline)

The following WP12 files exist in `08_Commercial/Assembly_Engine/` but are currently only used as human-reference documents:

| File | Content | Proposal Factory Integration Opportunity |
|---|---|---|
| `DELIVERY_PATTERN_LIBRARY.md` | 13 delivery patterns with phases, durations, resource models | Feed Stage 6 (Methodology Selection); feed S-35 (Project Plan) |
| `PROJECT_PLAN_TEMPLATES.md` | 7 week-based templates | Direct source for S-35 (Project Plan) |
| `PROPOSAL_STRUCTURE_LIBRARY.md` | 7 tender structures with section definitions | Governs WP18B assembly per tender type |
| `TENDER_BOM_LIBRARY.md` | 16 BOM codes | Feeds BOM_RESOLVER (already used) |
| `ASSEMBLY_READINESS_MATRIX.md` | Per-asset readiness assessment | Feeds Stage 4 Capability Selection |
| `ESTIMATION_INPUT_MODEL.md` | Commercial estimation intake form | Feeds commercial file preparation |

**Recommendation:** WP18B should formally integrate these 6 files as engine inputs, not just reference documents. This converts WP12 work from documentation to active factory components at near-zero additional cost.

#### Plennegy Tender Files (HIGH value — pattern templates)

The following files in `09_Active_Tenders/Plennegy/` contain patterns worth generalising:

| File | Content | Value |
|---|---|---|
| `PLENNEGY_QUESTION_MATRIX.md` | RFP question → response mapping | Template for Requirement Matrix (Step 3) |
| `PLENNEGY_COVERAGE_REPORT.md` | Section coverage assessment | Template for interim Gap Register |
| `PLENNEGY_READINESS_SCORECARD.md` | Proposal readiness scoring | Template for interim QA scorecard |
| `WP13_FACTORY_ASSESSMENT.md` | Factory capability assessment | Benchmark for future factory assessments |
| `PLENNEGY_ASSEMBLY_TEST.md` | BOM resolution test | Template for BOM resolution documentation |

**Recommendation:** Extract and generalise these 5 files into reusable templates in `08_Commercial/Assembly_Engine/`. They represent the first-ever Proposal Factory operational run and contain patterns that should be preserved and reused.

#### Governance Templates (MEDIUM value)

`08_Commercial/Assumptions/Governance/` contains:
- `GOVERNANCE_DECISION_RECORD_TEMPLATE.md` — reusable for all future governance decisions
- `GOVERNANCE_MASTER_DECISION_REGISTER.md` — master register of all BU decisions

These should be generalised to cover not just assumption governance but all Proposal Factory governance decisions (reference approvals, commercial decisions, etc.).

#### Commercial Framework (HIGH value — not yet integrated as assembly source)

The 5 WP11F documents in `08_Commercial/` are currently internal governance documents used by the Commercial Director and BU Lead. They contain structural content that can be extracted for proposal sections:
- `ESTIMATION_GUIDE.md` → feeds S-54 (Estimation Basis)
- `CR_PRICING_MODEL.md` → feeds S-38 (Change Control), S-73 (CR Process)
- `EFFORT_MULTIPLIERS.md` → feeds internal commercial file; not for external publication
- `RATE_CARD_FRAMEWORK.md` → feeds S-53 (Rate Card Basis), internal only
- `COMMERCIAL_GOVERNANCE.md` → governs commercial sign-off chain

**Recommendation:** Formally register these as source files in the CONTENT_SOURCE_MATRIX.md (already done in WP18A). WP18B should extract the client-safe language from these documents for relevant sections.

### 7.2 Gap assets to create

| Asset | Type | Priority | Responsible | Location |
|---|---|---|---|---|
| Risk Library | New methodology library | HIGH | BU Lead + BD | `08_Commercial/` or `05_Methodologies/` |
| OCI Capability Statement | New capability asset | HIGH | BU Lead | `06_Capabilities/Oracle/` |
| Oracle EBS Modernised Statement | Asset update | MEDIUM | BU Lead | `07_Approved_Content/Approved/Oracle/` |
| Security Methodology | New methodology | HIGH | BU Lead | `05_Methodologies/Security/` |
| Testing Methodology | New methodology | MEDIUM | BU Lead | `05_Methodologies/Testing/` |
| DR Methodology | New methodology | MEDIUM | BU Lead | `05_Methodologies/Disaster_Recovery/` |
| PM Methodology | New methodology | LOW | BU Lead | `05_Methodologies/Project_Management/` |
| AMS Methodology | New methodology | MEDIUM | BU Lead | `05_Methodologies/Managed_Services/` |
| Support Methodology | New methodology | LOW | BU Lead | `05_Methodologies/Support/` |
| Case Study Library | New content type | HIGH | Bid Manager | `08_Commercial/` new folder (OneDrive mkdir — plan required) |
| Tender Profile Template | Template | HIGH | Bid Manager | `09_Active_Tenders/` |
| Requirement Matrix Template | Template | HIGH | Bid Manager | `09_Active_Tenders/` |

---

## 8. Implementation Roadmap

### 8.1 Recommended Work Package order

| Priority | Work Package | Description | Rationale |
|---|---|---|---|
| 1 | **WP18B** — Proposal Assembly Engine | Build the assembly engine that integrates all existing components into the Stages 4–8 pipeline | This is the core factory build. It activates WP12, the Capability Library, and the Assembly Engine as a unified pipeline. The highest impact single initiative. |
| 2 | **WP18C** — Proposal Gap Analysis Engine | Build the automated gap detection engine | Gap Analysis is the fastest win after WP18B. It eliminates the largest manual work item for Bid Managers. The framework is fully specified in PROPOSAL_GAP_ANALYSIS_FRAMEWORK.md. Moderate implementation effort. |
| 3 | **WP18D** — Proposal QA Engine | Build the automated QA engine | QA Engine requires a complete proposal to operate. It can only be built after WP18B. The framework is fully specified in PROPOSAL_QA_FRAMEWORK.md. High implementation effort but high risk-reduction value. |
| 4 | **WP19** — Rendering Engine | Build DOCX/PDF/HTML output capability | Rendering is the final step. It requires a QA-passed assembled document. High technical effort but the logical endpoint of the factory. |

### 8.2 Prerequisite work before WP18B

Before WP18B can reach full capability, the following content gaps should be resolved:

| Task | Owner | Priority | Effort |
|---|---|---|---|
| Generalise Plennegy templates to reusable factory templates | Bid Manager | HIGH | LOW |
| Create Risk Library starter template | BU Lead | HIGH | MEDIUM |
| Author OCI capability narrative | BU Lead | HIGH | LOW |
| Author Security Methodology document | BU Lead | MEDIUM | MEDIUM |
| Resolve OAR-E03 (Acumatica Partner Certificate) | Acumatica BU Lead | MEDIUM | LOW |

### 8.3 WP18B recommended scope

WP18B should implement the assembly engine in phases:

**Phase 1 — Corporate and Capability sections (L3 → L5)**  
Automate assembly of S-01 to S-29 (corporate, partnership, solution). These sections are fully covered by approved KB assets and require no AI generation. This phase delivers a production-ready automated section for the majority of proposal content by volume.

**Phase 2 — Delivery and Compliance sections (L2 → L3)**  
Integrate WP12 DELIVERY_PATTERN_LIBRARY and PROJECT_PLAN_TEMPLATES into automated assembly of S-30 to S-45 and S-55 to S-66. Compliance expiry checking automated against COMPLIANCE_REGISTER.csv.

**Phase 3 — References, Support, and Appendices (L2 → L4)**  
Automated Reference Selector with AM approval workflow. AMS sections from Assembly Engine. Appendices assembled automatically.

**Phase 4 — AI-assisted sections (L1 → L4)**  
Executive Summary and Understanding of Requirements using AI generation with mandatory human review gate.

### 8.4 Timeline estimate (calendar effort, not elapsed time)

| Work Package | Phase | Estimated Effort | Notes |
|---|---|---|---|
| WP18B Phase 1 | Corporate + Solution | 2–3 sessions | Low complexity; direct KB assembly |
| WP18B Phase 2 | Delivery + Compliance | 3–4 sessions | WP12 integration; moderate complexity |
| WP18B Phase 3 | References + Support + Appendices | 2–3 sessions | AM workflow is the main new mechanism |
| WP18B Phase 4 | AI-assisted sections | 3–5 sessions | Highest complexity; most validation needed |
| WP18C | Gap Analysis Engine | 2–3 sessions | Framework complete; build is specification-to-code |
| WP18D | QA Engine | 3–4 sessions | Framework complete; large check count to implement |
| WP19 | Rendering Engine | 4–6 sessions | Technical complexity (DOCX generation) |

---

## 9. Governance Notes for Future WPs

The following governance rules apply to all future Proposal Factory work packages:

1. **No new engines alter the Assembly Engine** (WP17B/WP17C/WP17D). The Assembly Engine is production-ready. Future WPs call it as a module; they do not modify it.

2. **No new assets added to the KB without BU Lead approval.** `approved_for_reuse: Yes` is a BU Lead action only.

3. **No assembly of Draft assumption packs** in any proposal. Only Approved v1.0 packs may be used.

4. **All governance restrictions in MASTER_CAPABILITY_INDEX.md are non-negotiable** in all future assembly.

5. **Commercial Director authority schedule is never automated.** The pricing authority chain (COMMERCIAL_GOVERNANCE.md) applies to all proposals regardless of automation level.

6. **The OneDrive mkdir restriction applies.** New subdirectories cannot be created in this repository. All new files must go into existing directories. Work around this constraint by using descriptive file names.

7. **HANDOVER.md and AI_CONTEXT.md are updated at the close of every work package.** This document marks WP18A as COMPLETE.

---

## 10. WP18A Completion Status

| Deliverable | File | Status |
|---|---|---|
| End-to-end architecture | `PROPOSAL_FACTORY_ARCHITECTURE.md` | ✅ COMPLETE |
| Proposal Section Library | `PROPOSAL_SECTION_LIBRARY.md` | ✅ COMPLETE |
| Content Source Matrix | `CONTENT_SOURCE_MATRIX.md` | ✅ COMPLETE |
| Assembly Sequence | `PROPOSAL_ASSEMBLY_SEQUENCE.md` | ✅ COMPLETE |
| Automation Maturity Model | `AUTOMATION_MATURITY_MODEL.md` | ✅ COMPLETE |
| Gap Analysis Framework | `PROPOSAL_GAP_ANALYSIS_FRAMEWORK.md` | ✅ COMPLETE |
| QA Framework | `PROPOSAL_QA_FRAMEWORK.md` | ✅ COMPLETE |
| Architecture Recommendation | `WP18A_ARCHITECTURE_RECOMMENDATION.md` | ✅ COMPLETE |

**WP18A is COMPLETE.** The Proposal Factory is fully designed. The architecture defines every proposal section, every content source, every assembly stage, every validation stage, every future engine, and every dependency.

---

*WP18A_ARCHITECTURE_RECOMMENDATION.md v1.0 | WP18A COMPLETE | 2026-06-25*  
*Next work package: WP18B — Proposal Assembly Engine (Phase 1: Corporate + Capability sections)*
