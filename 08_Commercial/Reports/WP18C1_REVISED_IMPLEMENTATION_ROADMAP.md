---
document_id: WP18C1-REVISED-IMPLEMENTATION-ROADMAP
title: "WP18C.1 — Revised Implementation Roadmap"
version: "1.0"
status: "COMPLETE — 2026-06-25"
created: "2026-06-25"
created_by: "WP18C.1 — Proposal Factory Optimisation"
supersedes: "WP18B_IMPLEMENTATION_PLAN.md (P1–P10 sequence)"
governing_document: "This document is the governing roadmap for all future Proposal Factory development."
---

# WP18C.1 — Revised Implementation Roadmap

**Purpose:** Revise the Proposal Factory development sequence based on evidence from the first production run (WP18C, ARM IT045). This document supersedes the WP18B_IMPLEMENTATION_PLAN.md priority sequence.

**Basis:** WP18C1_FACTORY_OPTIMISATION_REVIEW.md (structural issues) + WP18C1_AUTOMATION_OPPORTUNITY_REGISTER.md (15 ranked opportunities) + ARM IT045 production run evidence.

---

## 1. Phase 4 — Factory Metrics

### 1.1 Current State Measurements

| Metric | Value | Notes |
|---|---|---|
| Current automation rate | **77.2%** | 44/57 sections DIRECT/EXTRACT/MERGE |
| QA score (ARM IT045) | **72/100** | Below 75 submission threshold |
| Manual effort per tender | **29–42 hours** | Includes team assignment, CVs, commercial, reference approval, AI review |
| Permanent minimum human effort | **~12–16 hours** | Team (8–12h) + commercial (2–4h) — cannot be automated by design |
| Theoretical maximum automation | **~91%** | After CVs (0%) and commercial (0%) excluded |
| Active pipeline stages (BUILT) | **3 of 10** | Stage 3 (BOM), Stage 7 (Assembly), Stage 8 (Proposal Assembly MVP) |
| Active pipeline stages (PARTIALLY BUILT) | **2 of 10** | Stage 9 (manual QA framework), Stage 8 (MVP, no feedback loop) |
| Active pipeline stages (NOT BUILT) | **5 of 10** | Stages 1, 2, 4, 5, 6 — all currently manual |

---

### 1.2 Manual Effort Analysis

Breaking down where the 29–42 hours of manual effort per tender is spent:

| Activity | Effort | Automatable? | Priority to Automate |
|---|---|---|---|
| Team assignment + CV sourcing | 8–12h | **NO** (ADR-001 permanent) | Not applicable |
| Commercial pricing section | 2–4h | **NO** (Commercial Director authority) | Not applicable; template reduces to 30min |
| Executive Summary | 1–2h | Partially (AI draft quality improvement) | MEDIUM (AO-013) |
| Reference AM approval + letter procurement | 2–4h | Partially (ranking automatable; approval human gate) | MEDIUM (AO-003) |
| AI-generated content review (S-14, S-22, S-37, S-50) | 3–6h | Partially (OCI asset + Pattern Risk Register reduces review burden) | HIGH (AO-006, AO-007) |
| PARTIAL section resolution (S-18 vintage, S-05, S-45) | 2–4h | Partially (KB asset updates reduce vintage risk) | LOW |
| Stage 4/5/6 manual selection | 2–3h | **YES** — AO-001/003/004 | VERY HIGH |
| Tender profile / context gathering | 1–2h | **YES** — AO-009 Stage 0 | VERY HIGH |
| Compliance package assembly | 1h | Partially (expiry check automatable) | LOW |
| **TOTAL** | **22–38h** | | |

**After AO register implementation:** Team and commercial remain (~12–16h). Other activities reduce to ~8–10h. Total: ~20–26h per tender (30–40% reduction).

**Target state:** Manual effort ~15–20h per tender (18–month horizon). This is the practical floor accounting for permanent governance constraints.

---

### 1.3 Knowledge Gaps

| Gap Type | Gap Description | Impact | Sections Affected |
|---|---|---|---|
| Content — Missing KB Asset | OCI Capability Narrative (no standalone asset) | S-22 always AI-generated until resolved | S-22 |
| Content — Empty Library | Risk Library (standard defined; 0 approved entries) | S-50 always AI-generated; RAID framework incomplete | S-37, S-50 |
| Content — Missing Library | Case Study Library (no structured case studies) | S-68 always AI-generated; competitive proposals lack proof | S-68 |
| Content — Methodology | Security Methodology (no asset) | S-45 assembled from assumption pack proxy | S-45 |
| Content — Methodology | DR Methodology (no asset; empty directory) | S-44 always GAP | S-44 |
| Content — Methodology | Implementation Methodology — 20 of 22 documents not authored | S-34, S-35 have limited coverage beyond W2S1-005 | S-34, S-35 |
| Engine — Missing Stage | Stage 0 Tender Profile Intake | Every run starts without structured input | All stages |
| Engine — Missing Stage | Stage 1 Tender Analysis Engine | Tender type/BOM not extracted automatically | Stage 1 |
| Engine — Missing Stage | Stage 2 Requirement Extraction | No RFP-to-section traceability | S-14 |
| Engine — Manual Stage | Stage 4 Capability Selection | 60-min manual step, every run | All capability sections |
| Engine — Manual Stage | Stage 5 Reference Selection | Manual ranking; no scoring | S-67 |
| Engine — Manual Stage | Stage 6 Methodology Selection | Manual pattern selection | S-34, S-35 |
| Engine — Not Built | Stage 9 Proposal QA | Manual QA scoring (2h per run) | All sections |
| Engine — Not Built | Stage 10 Rendering | No DOCX/PDF output | Final submission |

---

### 1.4 Automation Rate Trajectory

| Horizon | Action | Projected Rate |
|---|---|---|
| Current (WP18C baseline) | — | 77.2% |
| After Tier P0 (AO-001/002/003/004/005/008/009) | Encode Stage 4/5/6 rules; fix S-38 merge; add Stage 0 form | ~79% (section count) + significant effort reduction |
| After Tier P1 (AO-006/007/010/011/012/013/014/015) | OCI asset; Pattern Risk Registers; process improvements | **~85%** |
| After Risk Library Population (WP18B-EXT) | 75–90 approved risk entries | ~86% (S-50 EXTRACT) |
| After Security Methodology Asset | WP18B-METH4 | ~87% (S-45 improves) |
| After Stage 4/5/6 Automation Engines (WP18C.3) | Formal capability/reference/methodology selectors | ~88% (process becomes auditable) |
| After Pattern Risk Registers (all 13 patterns) | Pattern-specific risk baselines | ~88% (S-37 improves) |
| Theoretical maximum | All above complete; permanent constraints remain | **~91%** |

---

## 2. Phase 5 — Roadmap Revision

### 2.1 Reassessment of Current Priority Sequence

The current priority sequence (from HANDOVER.md as of WP18C):

| # | Item | Previous Rationale |
|---|---|---|
| P1 | WP18B-EXT — Risk Library Population | Quick win; 75–90 entries from capability assets |
| P2 | GAP-004 — OCI Capability Narrative | Fixes S-22 for all OCI tenders |
| P3 | A1 — Deploy W5-METH-001 | User action, 2 minutes |
| P4 | WP18B-METH1 — Cross-BU Methodology (7 docs) | Methodology library authoring |
| P5 | WP18D — Proposal QA Engine | QA automation |
| P6 | WP19 — Rendering Engine | DOCX output |
| P7 | WP18B-METH2 — Oracle Methodology | Oracle methodology |
| P8 | WP18B-METH3 — Acumatica + BeBanking | Platform methodology |
| P9 | Live Plennegy assembly | When blockers resolved |

---

### 2.2 Evidence-Based Reassessment

**WP18B-EXT (Risk Library Population):** Confirmed high priority. S-50 was a SEV-1 gap in ARM IT045. Risk registers appear in every tender. The Risk Library standard is ready; population is the obvious next step. **Maintain at P1.**

**GAP-004 (OCI Capability Narrative):** The WP18C run confirmed that OCI is a core service component for EBS AMS tenders and the missing narrative is a meaningful quality gap. This is one of the fastest-to-fix gaps with the highest per-tender impact. **Maintain at P2; should be done in the same session as WP18B-EXT.**

**AO-001 through AO-009 (Architecture Rules and Stage 0):** These did not appear in the previous roadmap because they were not identified until WP18C was run. They are the highest-ROI actions available. Total effort ~10 hours; converts Stages 4/5/6 from manual to deterministic; eliminates the most common factory friction. **Add as new P0 tier — do before anything else.**

**WP18B-METH1 (Cross-BU Methodology, 7 documents):** The ARM IT045 run revealed that methodology sections (S-34, S-35) were excluded for AMS proposals. AMS is the most common Oracle tender type in APPSolve's current portfolio. WP18B-METH1 primarily benefits Implementation proposals (where S-34/35 are in scope). Plennegy (the only active Implementation proposal) is already ~80% drafted. The 7-document Cross-BU methodology library is needed for future Oracle EBS Implementation proposals but is not urgent for the AMS-first factory. **Move down to P6. Reprioritise when a live Oracle EBS Implementation tender appears.**

**WP18D (Proposal QA Engine):** The manual QA computation in WP18C took ~2 hours. It is not the biggest bottleneck. The QA framework is well-defined and validated. Automating QA scoring is valuable but not blocking — the factory can run acceptably with manual QA until the content quality improves sufficiently that QA is fast. **Move to P4 (after Stage 0/4/5/6 rules). QA automation is most valuable when the deterministic automation rate is >85%; otherwise it mostly confirms what the Assembly Report already shows.**

**WP19 (Rendering Engine):** The rendering engine is the final dependency in the pipeline. It matters for live tender submissions. However, the factory's current bottleneck is content quality (22.8% human-authored), not format. Producing perfect markdown that gets manually converted to DOCX is acceptable for 12–18 more months. A rendering engine requires significant build effort (DOCX style guide, template, rendering logic). **Maintain at P7. Do not advance until QA Engine is complete.**

**WP18B-METH2 (Oracle Methodology, 3 docs):** More relevant than WP18B-METH1 for live Oracle tenders, but still Implementation-focused. ARM IT045 was AMS — methodology sections excluded. Only needed for Fusion HCM Implementation, Fusion ERP Implementation, and EBS Implementation tenders. With W2S1-005 already available for governance sections, the urgency is low. **Move to P7.**

**New additions to roadmap:** WP18C.2 (Architecture Cleanup), WP18C.3 (Stage 0/4/5/6 Automation Rules), WP18C.4 (AI Context Standards). These are new work packages not in the original roadmap that address the highest-ROI opportunities identified in WP18C.1.

---

### 2.3 Revised Priority Sequence

This is the governing roadmap for all future Proposal Factory development.

| Priority | Item | WP | Effort | Rationale |
|---|---|---|---|---|
| **P0-A** | Section Library Architecture Cleanup (SI-001/007/015) | WP18C.2 | 2–3h | Merge S-38+S-73 for AMS; SLA/Incident clean split; section order corrections. Low effort; high quality impact on every future AMS run. Do before next Factory run. |
| **P0-B** | Stage 0 + Stage 4/5/6 Automation Rules | WP18C.3 | 8–10h | Tender Profile Intake Form (Stage 0); BOM-to-Capability Selection Rules; Engagement-Type Section Scoping Rules; Methodology Lookup Table; Reference Scoring. Converts 3 manual stages to deterministic. Enables consistent, reproducible factory runs. |
| **P0-C** | Commercial Section Template | AO-008 | 1h | Unblocks Commercial Director. Critical for every tender. |
| **1** | OCI Capability Narrative Asset (W2S1-006) | GAP-004 | 4–8h + BU review | Fixes the only SEV-1 capability gap from ARM IT045. Single asset; high reuse; permanent fix. |
| **2** | Risk Library Population (WP18B-EXT) + Pattern 13 Risk Register | WP18B-EXT + AO-007 | 8–12h AI + 3h BU | Fixes S-50 for all tenders. Pattern 13 risk register as immediate interim; full library for long-term. |
| **3** | AI Context Standards for Executive Summary | WP18C.4 | 2–3h | Document the context injection standard for AI-GENERATE sections. Tender Profile fields + KB context anchors. Applies immediately; improves every AI-generated section. |
| **4** | Proposal QA Engine (automated QA scoring) | WP18D | Medium WP | Automates 10/12 QA check categories. Most valuable once automation rate >85%. Prerequisite for WP19. |
| **5** | Security Architecture Methodology Asset | WP18B-METH4 | 4–8h + BU review | Fixes S-45 (security architecture from proxy to governed asset). Needed for any OCI-scope or regulated-sector tender. Combined with WP18B-METH4 (DR methodology). |
| **6** | CONSULTANT_INDEX AMS Role Tagging | AO-011 (gap register) | 2–4h | Add AMS role classification to CONSULTANT_INDEX.csv. Enables candidate suggestions for S-46 team structure. |
| **7** | Oracle Methodology Library (3 documents) | WP18B-METH2 | ~12h | METH-O01 (Oracle EBS Implementation), METH-O02 (Oracle Fusion ERP), METH-O06 (Oracle-specific governance). Needed for Fusion/EBS Implementation proposals. Not needed for AMS. |
| **8** | Rendering Engine | WP19 | High WP | Markdown → DOCX/PDF. Prerequisite: QA Engine complete. Final pipeline component. |
| **9** | Cross-BU Methodology Library (7 documents) | WP18B-METH1 | ~28h | METH-X01 through METH-X07. Primarily for multi-platform and platform-agnostic proposals. Low urgency until a live multi-platform Implementation tender appears. |
| **10** | Stage 1 Tender Analysis Engine (AI-powered) | Future WP | High WP | AI parsing of tender documents into structured Tender Profile. Interim: human-completed form (AO-009). Build when volume of tenders exceeds manual intake capacity. |
| **11** | Stage 2 Requirement Extraction Engine | Future WP | Very High WP | RFP requirement-to-section traceability. Required for competitive scored tenders. Complex build. Defer until factory is otherwise mature. |
| **12** | Case Study Library | Future WP | High WP | Extract from won tender case material. Requires historical case study content collection and BU Leader approval for each case study. High effort; high competitive value. |

---

### 2.4 Revised Roadmap — Visual

```
PHASE: PRE-NEXT-RUN (P0 — ~12h total; do in one session)
  ├── WP18C.2: Section Library Cleanup (S-38/S-73 merge; order fixes)
  ├── WP18C.3: Stage 0 + Stage 4/5/6 Rules (Tender Profile; selectors)
  └── AO-008: Commercial Section Template

PHASE: CONTENT (P1-P2 — ~15–25h total)
  ├── P1: GAP-004 OCI Capability Asset (W2S1-006)
  ├── P2a: WP18B-EXT Risk Library Population (75–90 entries)
  ├── P2b: AO-007 Pattern 13 Risk Register (interim while P2a in progress)
  └── P3: WP18C.4 AI Context Standards

PHASE: ENGINE (P4-P5 — 2–3 medium WPs)
  ├── P4: WP18D Proposal QA Engine (automated scoring)
  └── P5: WP18B-METH4 Security + DR Methodology Assets

PHASE: METHODOLOGY LIBRARY (P6-P9 — 2–4 WPs)
  ├── P6: CONSULTANT_INDEX AMS Role Tagging
  ├── P7: WP18B-METH2 Oracle Methodology (3 docs)
  └── P8: WP19 Rendering Engine

PHASE: ADVANCED ENGINE (Future)
  ├── WP18B-METH1 Cross-BU Methodology (7 docs)
  ├── Stage 1 AI Tender Analysis Engine
  ├── Stage 2 Requirement Extraction Engine
  └── Case Study Library
```

---

### 2.5 Reassessment: Work Packages Moved

| Work Package | Previous Priority | New Priority | Reason |
|---|---|---|---|
| Architecture Rules (AO-001/002/004/009) | NOT IN PLAN | **P0** (new) | Identified in WP18C; highest ROI; near-zero effort |
| Section Library Cleanup (AO-005/014/015) | NOT IN PLAN | **P0** (new) | Eliminates recurring duplication defects |
| Commercial Template (AO-008) | NOT IN PLAN | **P0** (new) | Unblocks CD on every tender; 1h effort |
| OCI Capability Narrative | P2 | **P1** (moved up) | Confirmed SEV-1 gap in production run |
| WP18B-EXT Risk Library | P1 | **P2** (moved) | After architecture rules (P0); still high priority |
| WP18D QA Engine | P4 (was P5) | **P4** (maintained) | Most valuable once >85% automation achieved |
| WP18B-METH1 Cross-BU Methodology | P3 | **P9** (moved down) | AMS proposals (majority of current pipeline) don't use it |
| WP18B-METH2 Oracle Methodology | P7 | **P7** (maintained) | Implementation-specific; no urgency until live implementation tender |
| WP19 Rendering Engine | P6 | **P8** (moved down) | Content quality is the bottleneck; format is not |

---

### 2.6 New Work Packages Introduced by WP18C.1

Three new near-term work packages not in the previous roadmap:

**WP18C.2 — Section Library Consolidation and Cleanup**
- Scope: Update PROPOSAL_SECTION_LIBRARY.md and CONTENT_SOURCE_MATRIX.md to: (1) add `exclude_if: engagement_type = AMS` to S-38; (2) add SLA/Incident clean-split assembly instructions; (3) correct section ordering for AMS proposals; (4) add `engagement_type_scope` field to all sections
- Effort: 2–3 hours
- Output: Updated PROPOSAL_SECTION_LIBRARY.md v1.2, CONTENT_SOURCE_MATRIX.md v1.2
- Benefit: Every future AMS run starts with clean, non-duplicated structure

**WP18C.3 — Stage 0/4/5/6 Automation Rules**
- Scope: Design and document: (1) Tender Profile Intake Form (Stage 0 YAML spec); (2) BOM-to-capability selection rule table; (3) Engagement-type section scoping rules; (4) Reference scoring computation rules; (5) Methodology lookup table
- Effort: 8–10 hours
- Output: TENDER_PROFILE_STANDARD.md (new); updates to CONTENT_SOURCE_MATRIX.md, PROPOSAL_SECTION_LIBRARY.md, PROPOSAL_ASSEMBLY_SEQUENCE.md
- Benefit: Stages 4, 5, 6 become deterministic; every factory run starts with a structured Tender Profile; selection is auditable and reproducible

**WP18C.4 — AI Context Standards**
- Scope: Define the standard context injection block for each AI-GENERATE section. For each AI-GENERATE section (S-13, S-14, S-22, S-50), document: what KB sources to include in the prompt; what Tender Profile fields to inject; what output format to expect
- Effort: 2–3 hours
- Output: AI_GENERATION_STANDARDS.md (new, in `08_Commercial/Assembly_Engine/`)
- Benefit: AI-generated sections produce better first drafts; BU review time reduces; AI output is more consistent across factory runs

---

### 2.7 Plennegy Tender — Impact of Revised Roadmap

The Plennegy tender is an Oracle Fusion HCM Implementation (blocked by OAR-C01/C02/A01). When blockers are resolved, the factory must support an HCM Implementation proposal.

**Plennegy's relationship to this roadmap:**

| Plennegy Need | Factory Status | Gap |
|---|---|---|
| HCM assumption packs (13 packs) | PRODUCTION READY (WP17C) | None |
| Corporate sections | PRODUCTION READY | None |
| HCM capability sections | L3 (W3S1-001 through W3S1-009 approved) | None |
| Implementation methodology (S-34) | W2S1-005 available (Oracle governance framework) | Gap: full implementation methodology narrative for HCM not authored |
| Project plan (S-35) | PROJECT_PLAN_TEMPLATES.md available | Gap: dates and resources placeholder |
| References | L2 (manual, AM approval needed) | None blocking |
| Commercial | PLACEHOLDER — always | None blocking (permanent) |
| B-BBEE | FLAG — expires 2026-07-31 | Blocking if submission after 31 July |

**Conclusion:** Plennegy's most critical factory gap is the B-BBEE expiry (OAR-A01) and the two business actions (OAR-C01 AM approval; OAR-C02 commercial input). The WP18C.1 roadmap does not accelerate Plennegy — those are human-action blockers. However, the factory improvements (P0 tier) will make a Plennegy factory run faster and cleaner when those blockers are resolved.

---

## 3. Decision Register — Roadmap Rationale

Decisions made in constructing this roadmap, for future reference:

| Decision | Rationale | Implication |
|---|---|---|
| D-RM-001: Architecture rules (P0) before content authoring (P1/P2) | First production run showed Stages 4/5/6 are the biggest friction source per run. 10h to fix; saves 2–3h on every future run. | Do WP18C.2/18C.3 immediately before any library work. |
| D-RM-002: OCI capability asset before Risk Library population | OCI gap is a SEV-1 gap that affects AMS proposals (the dominant current tender type). Risk Library affects more sections but requires more effort. | OCI asset first; Risk Library second. Both in P1/P2. |
| D-RM-003: Methodology Library deprioritised below automation rules | Methodology sections (S-34/35) are excluded from AMS proposals. The majority of current and near-term Oracle proposals are AMS. No live implementation tender is currently active (Plennegy is blocked). | WP18B-METH1 (Cross-BU) moves to P9; WP18B-METH2 (Oracle) moves to P7. Revisit when live implementation tender is active. |
| D-RM-004: QA Engine (WP18D) at P4, not P3 | Manual QA (2h per run) is not the binding constraint. Content gaps are the binding constraint. Automating QA before fixing the content would automate a score that reflects content gaps, not system health. | WP18D after P0+P1+P2 content work. |
| D-RM-005: Rendering Engine (WP19) at P8 | Format is not the bottleneck. Markdown → manual DOCX is acceptable for up to 18 months. The effort for WP19 (DOCX style, template, rendering logic) should be spent on content and automation rules first. | WP19 is last major pipeline component. Do not accelerate. |
| D-RM-006: Permanent constraints are not roadmap items | CVs (ADR-001) and commercial pricing are permanently non-automatable by governance design. They appear in the Gap Register as PERMANENT type but generate no factory improvement actions. | Every gap register must classify these as PERMANENT and exclude them from factory remediation counts. |

---

## 4. Success Metrics — Roadmap Outcomes

At completion of each roadmap tier, the factory should meet these criteria:

| Tier | Completion Criteria |
|---|---|
| **P0 Complete** | (1) Section scoping for AMS proposals is rule-based and documented; (2) Stage 0 Tender Profile form exists and is used; (3) S-38 excluded from AMS proposals; (4) Commercial section template exists; (5) Reference scoring rules documented |
| **P1 Complete** | (1) OCI capability asset (W2S1-006) approved by BU Lead and loaded in KB; (2) S-22 changes from AI-GENERATE to DIRECT in next factory run |
| **P2 Complete** | (1) Risk Library has ≥50 approved entries; (2) Pattern 13 AMS risk register approved; (3) S-50 changes from AI-GENERATE to TEMPLATE or EXTRACT in next factory run; (4) QA score for next ARM-type run ≥78 |
| **P4 Complete** | (1) QA scoring is automated for all 10 deterministic check categories; (2) QA run time <15 minutes (from 2 hours manual) |
| **P8 Complete** | (1) First DOCX-rendered proposal produced from factory markdown output; (2) Rendering pipeline validated against factory output format |
| **All tiers complete** | (1) Automation rate ≥88%; (2) Manual effort per tender ≤20 hours; (3) QA score ≥78 on first assembly for any AMS tender; (4) End-to-end run time (from Tender Profile to submission-ready package) ≤4 hours active effort |

---

## 5. What This Roadmap Changes vs WP18B Plan

**Dropped from top 5:**
- WP18B-METH1 (Cross-BU Methodology) — moved from P3 to P9 (AMS proposals don't use it)

**Added to top 5:**
- WP18C.2 (Section Library Cleanup) — P0 new entry
- WP18C.3 (Stage 0/4/5/6 Rules) — P0 new entry
- AO-008 (Commercial Template) — P0 new entry
- GAP-004 (OCI asset) — moved from P2 to P1

**Order changes:**
- WP18D (QA Engine): unchanged (P4)
- WP19 (Rendering): moved down from P6 to P8

**Architecture additions:**
- Stage 0 (Tender Profile Intake) — NEW; not in original 10-stage pipeline
- AI Context Standards — NEW; not in original architecture documents
- Pattern Risk Registers — NEW approach; bridges gap between empty Risk Library and AI-only risk registers

---

*WP18C1_REVISED_IMPLEMENTATION_ROADMAP.md v1.0 | WP18C.1 — Proposal Factory Optimisation | 2026-06-25*  
*This document is the governing roadmap for all future Proposal Factory development. Supersedes WP18B_IMPLEMENTATION_PLAN.md priority sequence P1–P10. Next action: WP18C.2 (Section Library Cleanup) — 2–3h session; immediate.*
