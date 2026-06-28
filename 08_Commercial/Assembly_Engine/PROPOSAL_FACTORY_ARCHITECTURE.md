---
document_id: PROPOSAL-FACTORY-ARCHITECTURE
title: "Proposal Factory Architecture — End-to-End Blueprint"
version: "1.2"
status: "Updated — WP18C.2 (Stage 0 TIL added; Platform Components table updated; Governing Documents updated)"
created: "2026-06-25"
created_by: "WP18A — Proposal Factory Architecture"
updated: "2026-06-26"
updated_by: "WP18C.2 — Section Library Consolidation"
category: "Architecture / Design Blueprint"
scope: "End-to-end architecture for the APPSolve Proposal Factory. Defines every pipeline stage from tender receipt to rendered proposal document. This document is the master blueprint for all future Proposal Factory components (WP18B, WP18C, WP18D, WP19)."
---

# Proposal Factory Architecture — End-to-End Blueprint

**Date:** 2026-06-25 | **Version:** 1.1 | **Status:** Updated — WP18B  
**Work Package:** WP18A — Proposal Factory Architecture | **Updated by:** WP18B — Methodology & Risk Library Foundation  
**Baseline:** Assembly Engine PRODUCTION READY; 49 capability assets; 13 assumption packs; 1,136 assumptions; WP17D-1 COMPLETE  
**WP18B changes:** Methodology Library updated to reflect 2 approved files (W2S1-005 + W5-METH-001); Risk Library Standard now defined; governing documents table updated.

---

## 1. Executive Summary

The APPSolve Proposal Factory transforms the current Assumption Factory into a fully automated proposal production platform. The Assumption Factory can already produce complete, proposal-ready assumption schedules from a BOM code. The Proposal Factory extends this to assemble complete proposals — every section, every source, every governance check — from a tender document.

This architecture document defines the complete pipeline, every stage, and every dependency. It is the governing blueprint for WP18B (Proposal Assembly Engine), WP18C (Gap Analysis Engine), WP18D (QA Engine), and WP19 (Rendering Engine).

---

## 2. Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         PROPOSAL FACTORY PIPELINE                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  [TENDER DOCUMENT]                                                        │
│        │                                                                  │
│        ▼                                                                  │
│  ┌──────────────────────┐                                                │
│  │  STAGE 0             │  Tender Intelligence Layer (TIL) — WP18C.3    │
│  │  Tender Intelligence │  10-step TIL sequence: extract Tender Profile; │
│  │                      │  classify pattern; scope sections; select      │
│  │                      │  capabilities, references, methodology         │
│  └──────────┬───────────┘  ★ OPERATIONAL — L3.5 (WP18C.3 2026-06-26)  │
│             │                                                             │
│             ▼                                                             │
│  ┌──────────────────────┐                                                │
│  │  STAGE 1             │  Tender Analysis Engine                        │
│  │  Tender Analysis     │  Classify tender type, platform, BU, scope    │
│  └──────────┬───────────┘                                                │
│             │                                                             │
│             ▼                                                             │
│  ┌──────────────────────┐                                                │
│  │  STAGE 2             │  Requirement Extraction Engine                 │
│  │  Requirement         │  Structured requirements matrix from RFP      │
│  │  Extraction          │                                                │
│  └──────────┬───────────┘                                                │
│             │                                                             │
│             ▼                                                             │
│  ┌──────────────────────┐                                                │
│  │  STAGE 3             │  BOM_RESOLVER (EXISTING — WP17B)               │
│  │  BOM Resolution      │  Requirement matrix → Pack Manifest            │
│  └──────────┬───────────┘                                                │
│             │                                                             │
│             ▼                                                             │
│  ┌──────────────────────┐                                                │
│  │  STAGE 4             │  Capability Selector                           │
│  │  Capability          │  Select approved capability assets from KB     │
│  │  Selection           │                                                │
│  └──────────┬───────────┘                                                │
│             │                                                             │
│             ▼                                                             │
│  ┌──────────────────────┐                                                │
│  │  STAGE 5             │  Reference Selector                            │
│  │  Reference           │  Match reference letters to tender profile     │
│  │  Selection           │                                                │
│  └──────────┬───────────┘                                                │
│             │                                                             │
│             ▼                                                             │
│  ┌──────────────────────┐                                                │
│  │  STAGE 6             │  Methodology Selector                          │
│  │  Methodology         │  Select methodology assets per engagement      │
│  │  Selection           │  type and delivery pattern                     │
│  └──────────┬───────────┘                                                │
│             │                                                             │
│             ▼                                                             │
│  ┌──────────────────────┐                                                │
│  │  STAGE 7             │  Assembly Engine (EXISTING — WP17B/WP17D)      │
│  │  Assumption          │  Full-text assumption schedule + key           │
│  │  Assembly            │  assumptions body section                      │
│  └──────────┬───────────┘                                                │
│             │                                                             │
│             ▼                                                             │
│  ┌──────────────────────┐                                                │
│  │  STAGE 8             │  Proposal Assembly Engine (WP18B)              │
│  │  Proposal            │  Assemble all sections into a structured       │
│  │  Assembly            │  proposal document                             │
│  └──────────┬───────────┘                                                │
│             │                                                             │
│             ▼                                                             │
│  ┌──────────────────────┐                                                │
│  │  STAGE 9             │  Proposal QA Engine (WP18D)                   │
│  │  Proposal QA         │  Completeness, consistency, compliance,        │
│  │                      │  traceability, scoring                         │
│  └──────────┬───────────┘                                                │
│             │                                                             │
│             ▼                                                             │
│  ┌──────────────────────┐                                                │
│  │  STAGE 10            │  Rendering Engine (WP19)                       │
│  │  Document            │  DOCX / PDF / HTML output                      │
│  │  Rendering           │                                                │
│  └──────────┬───────────┘                                                │
│             │                                                             │
│             ▼                                                             │
│  [RENDERED PROPOSAL DOCUMENT]                                             │
│                                                                           │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Stage Specifications

---

### Stage 0 — Tender Intelligence Layer (TIL)

**Purpose:** Convert an unstructured tender document into a governed, machine-readable Tender Profile that deterministically drives all downstream factory stages. Stage 0 is the entry point for every factory run. All subsequent stages receive structured, validated inputs from the Tender Profile.

| Dimension | Detail |
|---|---|
| **Inputs** | Tender document (PDF / Word / text) |
| **Outputs** | `[TENDER_ID]_TENDER_PROFILE.md` (YAML schema; 8 blocks; 30+ fields) + `[TENDER_ID]_INTELLIGENCE_REPORT.md` (governance flags; human follow-up questions; assembly gate) |
| **Dependencies** | Tender document available and readable |
| **10-Step TIL Sequence** | TIL-01 Register → TIL-02 Block A (Metadata) → TIL-03 Block B (Client Profile) → TIL-04 Block C (Platform/Products) → TIL-05 Block D (Scope Dimensions) → TIL-06 Block E (Commercial Model) → TIL-07 Block F (Compliance/Governance) → TIL-08 Block G (Pattern/BOM/Sections — invokes 7 downstream engines) → TIL-09 Block H (Intelligence Quality) → TIL-10 Profile Approval |
| **Key Outputs from TIL-08** | Pattern classification (1–13); sections_in_scope + sections_excluded; capability_assets_required; methodology_asset; reference_pool; assumption_packs |
| **Assembly Gate** | GO / HOLD / ESCALATE — based on unknown field resolution |
| **Governance** | All 15 GOV rules applied at Stage 0; TENDER_INTELLIGENCE_RULES.md governs |
| **Owner** | AI + Bid Manager (TIL-01 to TIL-09) + BU Lead (TIL-10 approval) |

**Status:** OPERATIONAL — L3.5. Built in WP18C.3 (2026-06-26). 6 TIL engine files in `08_Commercial/Assembly_Engine/`. Governed by TENDER_INTELLIGENCE_RULES.md.

---

### Stage 1 — Tender Analysis

**Purpose:** Parse the incoming tender document (RFQ/RFP/ITT) and extract structured metadata. This is the entry gate for the entire pipeline.

| Dimension | Detail |
|---|---|
| **Inputs** | Tender document (PDF / Word / text) |
| **Outputs** | Tender Profile (structured JSON/YAML): tender type, client name, platform(s), BU(s), required modules, engagement type (implementation/AMS/both), deadline, submission format, compliance requirements, scoring criteria |
| **Dependencies** | Tender document available and readable |
| **Rules** | R1.1: Classify BU — Oracle / Acumatica / BeBanking / Multi-BU. R1.2: Identify engagement type — Fixed Price / T&M / AMS / Hybrid. R1.3: Extract compliance requirements (BEE level, ISO certifications, sector certifications). R1.4: Extract scoring criteria if tender is scored. R1.5: Flag any terms that conflict with standard commercial framework. R1.6: Identify submission deadline. |
| **Validation** | V1.1: Tender Profile must contain platform classification. V1.2: At least one BU identified. V1.3: Engagement type determined. V1.4: Deadline extracted. V1.5: Human review required if AI confidence < 0.80 on any field. |
| **Owner** | Bid Manager (tender intake) + AI Tender Analysis Engine |

**Implementation note:** Stage 1 is currently fully manual. WP18B should prioritise a structured Tender Profile intake form (human-completed) as an interim before AI parsing is available.

---

### Stage 2 — Requirement Extraction

**Purpose:** Convert the raw tender document into a structured requirements matrix, mapping each RFP requirement to a proposal section, capability asset, or gap.

| Dimension | Detail |
|---|---|
| **Inputs** | Tender document + Tender Profile (Stage 1 output) |
| **Outputs** | Requirement Matrix: list of requirements, each tagged with requirement ID, source paragraph, category (functional/commercial/compliance/technical), priority (mandatory/preferred/nice-to-have), and mapped asset or gap indicator |
| **Dependencies** | Stage 1 complete; Tender Profile available |
| **Rules** | R2.1: Every mandatory tender requirement must appear in the Requirement Matrix. R2.2: Requirements are tagged by section category (Functional, Technical, Commercial, Compliance, Governance). R2.3: Each requirement is mapped to zero or more KB assets. R2.4: Unmapped requirements are flagged as gaps. R2.5: Compliance requirements are cross-referenced with COMPLIANCE_REGISTER.csv. R2.6: Requirement Matrix is the traceability anchor for QA Stage 9. |
| **Validation** | V2.1: No tender section is skipped. V2.2: All mandatory requirements tagged as such. V2.3: All compliance requirements cross-checked. V2.4: Gap count produced (input to Stage 8 Gap Analysis). |
| **Owner** | Bid Manager (review) + AI Requirement Extraction Engine |

---

### Stage 3 — BOM Resolution

**Purpose:** Convert the Tender Profile and Requirement Matrix into an ordered Pack Manifest for the Assumption Assembly Engine.

| Dimension | Detail |
|---|---|
| **Inputs** | Tender Profile (Stage 1) + Requirement Matrix (Stage 2) |
| **Outputs** | Pack Manifest (ordered list of assumption packs with load sequence and BOM triggers) |
| **Dependencies** | Stage 2 complete; TENDER_BOM_LIBRARY.md current; all packs Approved v1.0 |
| **Rules** | All existing BOM_RESOLVER rules (TENDER_ASSUMPTION_ASSEMBLY_RULES.md v2.0). R3.1: Rule A (base first). R3.2: Rule B (additive). R3.3: Rule C (no duplicate IDs). R3.4: Rule D (BOM trigger required). R3.5: Rule E (all -EXC- included). R3.6: Rule OCI-1 (OCI pack mandatory for OCI-hosted engagements). R3.7: Rule JRN-1 (HCM-JRN-001 auto-included). |
| **Validation** | All BOM_RESOLVER validation rules apply. |
| **Owner** | Assembly Engine — BOM_RESOLVER (automated) |

**Existing component:** BOM_RESOLVER.md in `08_Commercial/Assembly_Engine/`. No new build required.

---

### Stage 4 — Capability Selection

**Purpose:** Identify which of the 49 approved capability assets should appear in this proposal, in which sections, and at what level of detail.

| Dimension | Detail |
|---|---|
| **Inputs** | Tender Profile + Requirement Matrix + MASTER_CAPABILITY_INDEX.md |
| **Outputs** | Capability Selection List: for each selected asset, the asset ID, target proposal section, inclusion reason (BOM trigger, requirement match, mandatory), and governance restrictions to apply |
| **Dependencies** | Stage 3 complete; MASTER_CAPABILITY_INDEX.md current |
| **Rules** | R4.1: Only Approved assets (`approved_for_reuse: Yes`) may be selected. R4.2: All mandatory governance restrictions from MASTER_CAPABILITY_INDEX.md apply. R4.3: Section exclusions (PT-W8-007, PT-W9-008) always applied. R4.4: Product boundary rules always applied. R4.5: Cross-BU assets (W1S1-001 through W1S1-009) are included in every proposal. R4.6: Platform-specific assets selected based on BOM trigger from Stage 3. R4.7: W4-HCM-004 is RETIRED — never selected. |
| **Validation** | V4.1: No Candidate_Content or Review_Required assets selected. V4.2: All governance restrictions recorded in Capability Selection List. V4.3: Client naming restrictions checked for all selected assets. V4.4: Section exclusion rules applied. |
| **Owner** | Capability Selector (automated rule-based) + BU Lead (validation) |

**Existing component:** ASSEMBLY_READINESS_MATRIX.md provides the current per-asset readiness assessment. Stage 4 formalises this into an automated selection step.

---

### Stage 5 — Reference Selection

**Purpose:** Identify which reference letters and case studies should be included in the proposal, matching by product, industry, engagement type, and client sensitivity rules.

| Dimension | Detail |
|---|---|
| **Inputs** | Tender Profile + REFERENCE_MASTER.csv + client naming governance rules |
| **Outputs** | Reference Selection List: for each selected reference, the Ref ID, client name, products covered, relevance score (product match + sector match), and AM approval flag |
| **Dependencies** | Stage 4 complete; REFERENCE_MASTER.csv current; AM approval obtained where required |
| **Rules** | R5.1: Only signed, registered letters may be cited (Ref IDs REF-ORA-001 to REF-ORA-011, REF-ACU-001 to REF-ACU-005). R5.2: DFA permanently excluded (Rule 21.4). R5.3: CCBA permanently excluded. R5.4: SAA permanently excluded (Rule 21.1). R5.5: Redpath Mining excluded until Rule 21.5 waived. R5.6: Hollywood Bets requires AM approval at each tender. R5.7: KPMG excluded until AM-W4E3-001 cleared. R5.8: References ranked by product match score (exact product = 3 points; platform match = 2 points; sector match = 1 point). R5.9: Minimum 2 references per proposal. R5.10: Reference vintage > 5 years flagged for BU Lead review. |
| **Validation** | V5.1: No prohibited client named. V5.2: AM approval obtained before final selection. V5.3: All selected letters are signed PDFs in `04_References/`. V5.4: Unsigned templates not used. |
| **Owner** | Reference Selector (automated ranking) + BU Lead / AM (approval) |

---

### Stage 6 — Methodology Selection

**Purpose:** Select the appropriate implementation methodology, delivery pattern, and project plan template for the engagement.

| Dimension | Detail |
|---|---|
| **Inputs** | Tender Profile + DELIVERY_PATTERN_LIBRARY.md + PROJECT_PLAN_TEMPLATES.md + `05_Methodologies/` |
| **Outputs** | Methodology Selection: delivery pattern ID, methodology asset ID, project plan template ID, phase structure, timeline assumptions |
| **Dependencies** | Stage 4 complete; DELIVERY_PATTERN_LIBRARY.md current |
| **Rules** | R6.1: Select from 13 delivery patterns in DELIVERY_PATTERN_LIBRARY.md. R6.2: Platform-agnostic engagements use W5-METH-001. R6.3: Oracle-specific engagements use W2S1-005. R6.4: Multi-platform uses W5-METH-001 as base. R6.5: Project plan template is week-based only — calendar dates added at submission. R6.6: AMS-only engagements use Pattern 12 or 13. R6.7: Phased go-live tenders use phased patterns (Patterns 2, 4, 6, 8). |
| **Validation** | V6.1: Delivery pattern matched to engagement type. V6.2: Project plan template compatible with selected pattern. V6.3: Methodology asset in approved status. |
| **Owner** | Methodology Selector (automated) + BU Lead (approval for non-standard patterns) |

---

### Stage 7 — Assumption Assembly

**Purpose:** Produce the complete assumption schedule and key assumptions body section using the existing Assembly Engine.

| Dimension | Detail |
|---|---|
| **Inputs** | Pack Manifest (Stage 3) + ASSUMPTION_GROUPING_RULES.md + EXECUTIVE_ASSUMPTION_SUMMARY_RULES.md |
| **Outputs** | `[TENDER_ID]_ASSUMPTION_SCHEDULE_V1.md` (complete appendix) + `[TENDER_ID]_KEY_ASSUMPTIONS_V1.md` (body section) + Assembly Audit Report |
| **Dependencies** | Stages 3–4 complete; all packs Approved v1.0 |
| **Rules** | All Assembly Engine rules: A–E, JRN-1, OCI-1, S1–S4. Option B dual-output model (WP17D-0A). Sequential numbering. 8 client-facing sections (A–H). |
| **Validation** | All 10 WP17D-1 validation checks (V1–V10). |
| **Owner** | Assembly Engine (automated) |

**Existing component:** Full stack in `08_Commercial/Assembly_Engine/`. Production ready.

---

### Stage 8 — Proposal Assembly

**Purpose:** Assemble all selected assets, methodologies, references, and assumptions into a structured, complete proposal document — one section at a time, in deterministic sequence.

| Dimension | Detail |
|---|---|
| **Inputs** | Capability Selection List (Stage 4) + Reference Selection List (Stage 5) + Methodology Selection (Stage 6) + Assumption outputs (Stage 7) + PROPOSAL_STRUCTURE_LIBRARY.md + Requirement Matrix (Stage 2) |
| **Outputs** | Assembled Proposal (markdown) — all sections populated with content from approved KB assets, with gaps flagged inline as `[GAP: description]` placeholders |
| **Dependencies** | All Stages 1–7 complete; Gap Analysis run (Stage 8a) |
| **Rules** | R8.1: Assembly follows PROPOSAL_ASSEMBLY_SEQUENCE.md. R8.2: All content from approved sources only. R8.3: Client-specific customisation points marked as `[CUSTOMISE]` placeholders. R8.4: Commercial section always `[PLACEHOLDER — COMMERCIAL INPUT REQUIRED]`. R8.5: CV sections always `[PLACEHOLDER — OBTAIN FROM APPTIMEAPTIME]`. R8.6: Governance restrictions applied inline. R8.7: Gaps produce `[GAP: severity — description]` markers. |
| **Validation** | V8.1: Every mandatory proposal section present. V8.2: No prohibited content included. V8.3: All governance restriction markers applied. V8.4: Gap log produced (input to WP18C). |
| **Owner** | Proposal Assembly Engine (WP18B) + Bid Manager (review) |

**Future component:** WP18B — Proposal Assembly Engine. Design governed by this architecture document.

---

### Stage 9 — Proposal QA

**Purpose:** Automatically verify the assembled proposal against the Requirement Matrix, governance rules, completeness criteria, and consistency checks before human review.

| Dimension | Detail |
|---|---|
| **Inputs** | Assembled Proposal (Stage 8) + Requirement Matrix (Stage 2) + Capability Selection List (Stage 4) + Reference Selection List (Stage 5) |
| **Outputs** | QA Report + Completeness Score + Risk Score + Gap Register + Compliance Checklist |
| **Dependencies** | Stage 8 complete |
| **Rules** | All rules defined in PROPOSAL_QA_FRAMEWORK.md. |
| **Validation** | QA must achieve minimum completeness score before proceeding to rendering. |
| **Owner** | Proposal QA Engine (WP18D) + BU Lead (sign-off) |

**Future component:** WP18D — Proposal QA Engine. Design governed by PROPOSAL_QA_FRAMEWORK.md.

---

### Stage 10 — Document Rendering

**Purpose:** Convert the assembled, QA-passed proposal markdown into the final client-facing document format (DOCX, PDF, HTML).

| Dimension | Detail |
|---|---|
| **Inputs** | QA-passed assembled proposal (Stage 9) + Document template (APPSolve proposal template) |
| **Outputs** | Final proposal document: `[TENDER_ID]_PROPOSAL_V[X].docx` + `[TENDER_ID]_PROPOSAL_V[X].pdf` (optional) |
| **Dependencies** | Stage 9 QA pass; document template available |
| **Rules** | R10.1: Styles mapped per ASSUMPTION_SCHEDULE_STANDARD.md Section 9. R10.2: TOC generated automatically. R10.3: Appendices attached in order. R10.4: Version number incremented at each render. R10.5: Rendered document not considered final until BU Lead sign-off. |
| **Validation** | V10.1: Word count within expected range for tender type. V10.2: All `[GAP]` and `[PLACEHOLDER]` markers resolved or documented. V10.3: TOC generated. V10.4: Appendices in correct sequence. |
| **Owner** | Rendering Engine (WP19) + Bid Manager (final review) |

**Future component:** WP19 — Rendering Engine. No design in this WP.

---

## 4. Cross-Pipeline Governance Rules

The following rules apply across the entire pipeline and override any stage-level rule.

| Rule | Content |
|---|---|
| G-01 | DFA never named in any output at any stage |
| G-02 | CCBA never named in any output at any stage |
| G-03 | SAA never named as client at any stage |
| G-04 | Redpath Mining not referenceable until Rule 21.5 waived |
| G-05 | Hollywood Bets: AM approval at each tender, obtained before Stage 5 |
| G-06 | KPMG: not named until AM-W4E3-001 cleared |
| G-07 | Oracle Gold Partner: expired August 2021 — never cite |
| G-08 | BEE Level 3: do not cite after 2026-07-31 without renewed certificate |
| G-09 | Section 14.2 (W3S1-008): never in any output |
| G-10 | Section 13.2 (W3S1-009): never in any output |
| G-11 | HIST-018 billing (R825,170): never in any output |
| G-12 | Commercial figures: never in any output without Commercial Director authorisation |
| G-13 | CV text: never generated from KB records — always from APPTime |
| G-14 | approved_for_reuse: only set by BU Lead — never by AI |

---

## 5. Stage Dependency Map

```
Stage 0 (Tender Intelligence Layer) ★ OPERATIONAL — L3.5
    └── Stage 1 (Tender Analysis)
            └── Stage 2 (Requirement Extraction)
                    └── Stage 3 (BOM Resolution)
                    │       └── Stage 4 (Capability Selection) ← driven by Stage 0 TIL outputs
                    │       │       └── Stage 5 (Reference Selection) ← driven by Stage 0 TIL outputs
                    │       │       └── Stage 6 (Methodology Selection) ← driven by Stage 0 TIL outputs
                    │       │
                    │       └── Stage 7 (Assumption Assembly)
                    │
                    └── [Stages 4, 5, 6, 7 all feed Stage 8]
                            └── Stage 8 (Proposal Assembly)
                                    └── Stage 9 (Proposal QA)
                                            └── Stage 10 (Document Rendering)
```

**Note:** Stage 0 (TIL) drives Stages 4, 5, and 6 deterministically. Once the Tender Profile is approved at Stage 0, the capability selection, reference ranking, and methodology selection are all pre-computed — Stages 4, 5, 6 execute as lookup operations rather than analytical tasks.

Stages 4, 5, and 6 can run in parallel after Stage 3. Stage 7 runs in parallel with Stages 4–6.
Stage 8 requires all of Stages 4–7 complete.

---

## 6. Platform Components — Current and Future

| Stage | Component | Status | Work Package |
|---|---|---|---|
| 0 | TENDER_PROFILE_STANDARD.md | **OPERATIONAL — L3.5** | WP18C.3 |
| 0 | TENDER_INTELLIGENCE_RULES.md | **OPERATIONAL — L3.5** | WP18C.3 |
| 0 | PROPOSAL_PATTERN_ENGINE.md | **OPERATIONAL — L3.5** | WP18C.3 |
| 0 | CAPABILITY_SELECTION_ENGINE.md | **OPERATIONAL — L3.5** | WP18C.3 |
| 0 | METHODOLOGY_SELECTION_ENGINE.md | **OPERATIONAL — L3.5** | WP18C.3 |
| 0 | REFERENCE_SELECTION_ENGINE.md | **OPERATIONAL — L3.5** | WP18C.3 |
| 3 | BOM_RESOLVER | **PRODUCTION READY** | WP17B |
| 3 | PACK_LOADER v1.1 | **PRODUCTION READY** | WP17B/WP17C |
| 3 | RULE_PROCESSOR | **PRODUCTION READY** | WP17B |
| 7 | ASSUMPTION_EXTRACTOR v1.1 | **PRODUCTION READY** | WP17D-1 |
| 7 | ASSEMBLY_AUDITOR | **PRODUCTION READY** | WP17B |
| 7 | ENGINE_ORCHESTRATOR | **PRODUCTION READY** | WP17B |
| 7 | ASSEMBLY_SCHEDULE output | **PRODUCTION READY** | WP17D-1 |
| 7 | KEY_ASSUMPTIONS output | **PRODUCTION READY** | WP17D-1 |
| 3, 6 | DELIVERY_PATTERN_LIBRARY | **ACTIVE** | WP12 |
| 3, 6 | PROJECT_PLAN_TEMPLATES | **ACTIVE** | WP12 |
| 4 | PROPOSAL_STRUCTURE_LIBRARY | **ACTIVE** | WP12 |
| 4 | ASSEMBLY_READINESS_MATRIX | **ACTIVE** | WP12 |
| 3 | TENDER_BOM_LIBRARY | **ACTIVE** | WP12 |
| 2, 8 | Tender Analysis Engine | **NOT BUILT** | Future |
| 4 | Capability Selector (automated) | **PARTIAL** (manual via PROPOSAL_STRUCTURE_LIBRARY) | WP18B |
| 5 | Reference Selector (automated) | **NOT BUILT** | WP18B |
| 6 | Methodology Selector (automated) | **NOT BUILT** | WP18B |
| 8 | Proposal Assembly Engine | **NOT BUILT** | WP18B |
| 8 | Gap Analysis Engine | **NOT BUILT** | WP18C |
| 9 | Proposal QA Engine | **NOT BUILT** | WP18D |
| 10 | Rendering Engine | **NOT BUILT** | WP19 |

---

## 7. Source Libraries

The Proposal Factory draws content from the following libraries:

| Library | Location | Status | Contents |
|---|---|---|---|
| Capability Library | `07_Approved_Content/Approved/` + `06_Capabilities/` | **COMPLETE** | 49 approved assets |
| Assumption Library | `08_Commercial/Assumptions/` | **COMPLETE** | 13 packs; 1,136 assumptions |
| Methodology Library | `05_Methodologies/` | **PARTIAL** | 2 approved files (W2S1-005 Oracle; W5-METH-001 Cross-BU); 6 subfolders empty; 20 further documents planned; governed by METHODOLOGY_LIBRARY_STANDARD.md |
| Risk Library | `08_Commercial/` (standard defined; content folder not yet created) | **STANDARD DEFINED** | RISK_LIBRARY_STANDARD.md approved; 15 categories defined; 75–90 entries extractable; no approved entries yet; governed by RISK_LIBRARY_STANDARD.md |
| Reference Library | `04_References/` | **ACTIVE** | 16 signed letters |
| Corporate Library | `02_Corporate/` | **ACTIVE** | Company profile, financial statements, resolutions |
| CV Library | APPTime (external) | **ACTIVE** | Not in KB — ADR-001 |
| Certification Library | `01_Compliance/` | **ACTIVE** | COMPLIANCE_REGISTER.csv; 17 items |
| Commercial Library | `08_Commercial/` | **ACTIVE** | 5 framework docs; internal only |
| Governance Library | `08_Commercial/Assumptions/Governance/` | **ACTIVE** | Decision register, governance templates |
| Pricing Library | Not yet created | **GAP** | Commercial Director authority schedule |
| Assembly Engine | `08_Commercial/Assembly_Engine/` | **PRODUCTION READY** | 22 files |

---

## 8. Governing Documents

| Document | Location | Governs |
|---|---|---|
| PROPOSAL_FACTORY_ARCHITECTURE.md (this file) | `08_Commercial/Assembly_Engine/` | Overall pipeline |
| TENDER_PROFILE_STANDARD.md | `08_Commercial/Assembly_Engine/` | Stage 0 — Tender Profile YAML schema (8 blocks; 30+ fields) |
| TENDER_INTELLIGENCE_RULES.md | `08_Commercial/Assembly_Engine/` | Stage 0 — 10-step TIL processing; 15 governance rules; unknown handling |
| PROPOSAL_PATTERN_ENGINE.md | `08_Commercial/Assembly_Engine/` | Stage 0 — Pattern classification (13 patterns); section scoping per pattern |
| CAPABILITY_SELECTION_ENGINE.md | `08_Commercial/Assembly_Engine/` | Stage 0/4 — BOM→capability asset lookup; deselection rules |
| METHODOLOGY_SELECTION_ENGINE.md | `08_Commercial/Assembly_Engine/` | Stage 0/6 — Pattern→methodology asset + project plan template |
| REFERENCE_SELECTION_ENGINE.md | `08_Commercial/Assembly_Engine/` | Stage 0/5 — 7-dimension scoring; 12 exclusion rules; AM workflow |
| PROPOSAL_SECTION_LIBRARY.md | `08_Commercial/Assembly_Engine/` | Every proposal section (v1.2 — WP18C.2) |
| CONTENT_SOURCE_MATRIX.md | `08_Commercial/Assembly_Engine/` | Section → source mapping (v1.2 — WP18C.2) |
| PROPOSAL_ASSEMBLY_SEQUENCE.md | `08_Commercial/Assembly_Engine/` | Assembly order (v1.1 — WP18C.2) |
| AUTOMATION_MATURITY_MODEL.md | `08_Commercial/Assembly_Engine/` | Per-section maturity |
| PROPOSAL_GAP_ANALYSIS_FRAMEWORK.md | `08_Commercial/Assembly_Engine/` | Gap identification |
| PROPOSAL_QA_FRAMEWORK.md | `08_Commercial/Assembly_Engine/` | QA engine design |
| WP18A_ARCHITECTURE_RECOMMENDATION.md | `08_Commercial/Reports/` | Decisions and roadmap |
| TENDER_ASSUMPTION_ASSEMBLY_RULES.md v2.0 | `08_Commercial/` | Assumption assembly rules |
| MASTER_CAPABILITY_INDEX.md v1.2 | `06_Capabilities/` | Capability governance |
| PROPOSAL_STRUCTURE_LIBRARY.md | `08_Commercial/Assembly_Engine/` | Proposal structures by type |
| DELIVERY_PATTERN_LIBRARY.md | `08_Commercial/Assembly_Engine/` | Delivery patterns |
| METHODOLOGY_LIBRARY_STANDARD.md | `08_Commercial/` | Methodology Library governance; 22-document plan |
| RISK_LIBRARY_STANDARD.md | `08_Commercial/` | Risk Library governance; 15 categories; RAID log standard |

---

*PROPOSAL_FACTORY_ARCHITECTURE.md v1.2 | WP18A — Proposal Factory Architecture | Updated WP18C.2 2026-06-26*  
*Governs: WP18B (Assembly Engine), WP18C (Gap Analysis), WP18D (QA Engine), WP19 (Rendering)*  
*v1.2: Stage 0 (Tender Intelligence Layer — WP18C.3) added to pipeline diagram, Stage specifications, Stage Dependency Map, Platform Components table, and Governing Documents table. Platform Maturity: L3.5.*
