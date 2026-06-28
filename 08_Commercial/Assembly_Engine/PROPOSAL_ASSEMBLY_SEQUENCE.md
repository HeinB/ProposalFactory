---
document_id: PROPOSAL-ASSEMBLY-SEQUENCE
title: "Proposal Assembly Sequence — Deterministic Assembly Order"
version: "1.1"
status: "Updated — WP18C.2 (AMS pattern notes; SI-001 S-38 exclusion; SI-005 reference ordering; SI-006 assumptions ordering; Pattern 13 complete assembly table)"
created: "2026-06-25"
created_by: "WP18A — Proposal Factory Architecture"
updated: "2026-06-26"
updated_by: "WP18C.2 — Section Library Consolidation"
category: "Architecture / Assembly Rules"
scope: "Defines the deterministic order in which the Proposal Factory assembles a complete proposal. Every step is specified, with the dependency reason and what it provides to subsequent steps. This is the governing sequence for WP18B (Proposal Assembly Engine). Pattern-specific ordering notes added for Pattern 13 (AMS) in Section 6."
---

# Proposal Assembly Sequence

**Date:** 2026-06-25 | **Version:** 1.0 | **Status:** Approved  
**Work Package:** WP18A — Proposal Factory Architecture  
**Governs:** WP18B — Proposal Assembly Engine

---

## 1. Purpose

The Proposal Factory assembles proposals in a fixed, deterministic order. Every step depends on the output of prior steps. No step can be skipped or reordered without breaking downstream validation.

This sequence ensures:
- Content is selected before it is assembled
- Governance rules are applied before content is included
- Gaps are identified before assembly reaches the affected section
- The QA engine receives a fully assembled document with a complete requirement traceability layer

---

## 2. The Assembly Sequence

---

### Step 1 — Ingest Tender Document

**What:** Accept the raw tender document (PDF, Word, text) into the Proposal Factory.

**Output:** Raw tender file registered in the Active Tenders workspace (`09_Active_Tenders/[TENDER_ID]/`)

**Why this is Step 1:** All subsequent steps depend on the tender document. Nothing can proceed without it.

**Gate condition:** File readable; tender reference ID assigned; workspace created.

---

### Step 2 — Produce Tender Profile

**What:** Parse the tender document to produce the Tender Profile: client name, platform, BU, engagement type, key dates, compliance requirements, submission format, scoring criteria.

**Output:** `[TENDER_ID]_TENDER_PROFILE.md` — structured YAML/Markdown metadata

**Why this order:** The Tender Profile is the master input for all selection and assembly steps (3–10). Without it, no downstream selection can be made.

**Gate condition:** Platform identified; engagement type determined; deadline recorded; BU Lead notified.

---

### Step 3 — Build Requirement Matrix

**What:** Extract every RFP requirement from the tender document, tag by category (Functional / Technical / Commercial / Compliance / Governance), and mark mandatory/preferred/nice-to-have.

**Output:** `[TENDER_ID]_REQUIREMENT_MATRIX.md` — indexed list of requirements

**Why this order:** The Requirement Matrix is the traceability anchor. The Gap Analysis (Step 9), Proposal QA (Step 16), and Understanding of Requirements section (Step 12) all trace back to this matrix. It must exist before any assembly begins.

**Gate condition:** All mandatory tender requirements captured; compliance requirements extracted; minimum of one requirement per category.

---

### Step 4 — Resolve BOM

**What:** Convert the Tender Profile into an ordered Pack Manifest using BOM_RESOLVER. Identify which assumption packs are triggered.

**Output:** Pack Manifest (ordered list with BOM trigger per pack)

**Why this order:** The Pack Manifest is required before capability selection (Step 5), assumption assembly (Step 8), and scope definition (Step 11). Pack selection drives which capability assets are relevant.

**Gate condition:** At least one pack triggered; all Rule D (BOM trigger) checks pass.

**Engine:** BOM_RESOLVER.md (existing — WP17B)

---

### Step 5 — Select Capability Assets

**What:** Using the Tender Profile and Pack Manifest, identify which of the 49 approved capability assets will appear in this proposal. Record governance restrictions per asset.

**Output:** `[TENDER_ID]_CAPABILITY_SELECTION.md` — list of selected asset IDs, target sections, and governance restrictions

**Why this order:** Capability selection must precede section assembly (Steps 11–15) because section content is drawn directly from selected assets. Selection also informs the Gap Analysis (Step 9) — if a required capability has no approved asset, it is a gap.

**Gate condition:** Only Approved assets selected; all governance restrictions recorded; section exclusions (PT-W8-007, PT-W9-008) applied.

---

### Step 6 — Select References

**What:** Rank and select reference letters from REFERENCE_MASTER.csv based on product match, sector match, and client sensitivity rules.

**Output:** `[TENDER_ID]_REFERENCE_SELECTION.md` — ranked reference list with AM approval status per letter

**Why this order:** Reference selection depends on Tender Profile (client sector, products). It feeds the Client References section (Step 14) and the Cover Letter / Executive Summary (Step 11). AM approval must be obtained before reference letters are included in the final proposal.

**Gate condition:** No prohibited clients included; minimum 2 references selected; AM approval status recorded for all selected letters.

---

### Step 7 — Select Methodology and Delivery Pattern

**What:** Identify the delivery pattern (from DELIVERY_PATTERN_LIBRARY.md), methodology asset (W2S1-005 or W5-METH-001), and project plan template (from PROJECT_PLAN_TEMPLATES.md).

**Output:** `[TENDER_ID]_METHODOLOGY_SELECTION.md` — pattern ID, methodology asset, template ID, phase structure

**Why this order:** Methodology selection feeds the Project Plan (Step 12), Deliverables (Step 12), Testing Strategy (Step 12), and Cutover sections. It must be completed before those sections are assembled.

**Gate condition:** Delivery pattern matched to engagement type; project plan template compatible with pattern.

---

### Step 8 — Assemble Assumption Schedule

**What:** Run the full Assembly Engine pipeline (BOM_RESOLVER → PACK_LOADER → RULE_PROCESSOR → ASSUMPTION_EXTRACTOR → ASSEMBLY_AUDITOR) to produce the complete assumption schedule and key assumptions body section.

**Output:** `[TENDER_ID]_ASSUMPTION_SCHEDULE_V1.md` + `[TENDER_ID]_KEY_ASSUMPTIONS_V1.md` + `[TENDER_ID]_ASSEMBLY_AUDIT_REPORT.md`

**Why this order:** The assumption outputs are inserted verbatim into the proposal. They must exist before the Scope (Step 11), Key Assumptions (Step 13), and Appendix (Step 15) sections are assembled. The body Key Assumptions section feeds the commercial commitment understanding.

**Gate condition:** All 10 WP17D-1 validation checks pass; count balance verified; no suppressed assumptions visible.

**Engine:** Full Assembly Engine stack (WP17B + WP17D-1)

---

### Step 9 — Run Gap Analysis

**What:** Compare the Requirement Matrix (Step 3), Capability Selection (Step 5), Reference Selection (Step 6), and Assumption Schedule (Step 8) to identify every gap: missing capabilities, missing references, missing commercial decisions, missing compliance documents.

**Output:** `[TENDER_ID]_GAP_REGISTER.md` — prioritised list of gaps with severity, blocking/non-blocking status, responsible owner, and remediation guidance

**Why this order:** Gap Analysis must occur before section assembly begins. Gaps produce `[GAP]` placeholders in the assembled proposal. If blocking gaps exist, assembly should pause and be escalated before proceeding. Running Gap Analysis here — before any narrative is written — prevents wasted authoring effort on sections that cannot be completed.

**Gate condition:** All blocking gaps escalated and either resolved or accepted by BU Lead; non-blocking gaps recorded as `[GAP]` markers.

**Engine:** Gap Analysis Engine (WP18C — future). Manual gap check in interim.

---

### Step 10 — Assemble Corporate Sections

**What:** Assemble the fixed corporate sections (S-01 to S-12): cover page, TOC placeholder, Company Overview, Company History, Awards, Delivery Model, Geographic Presence, Key Differentiators, Partnership Statements, B-BBEE Statement.

**Output:** Corporate section markdown blocks

**Why this order:** These sections are independent of tender-specific content and can be assembled once Tender Profile is known (client name, date, tender ref). They are assembled first because they form the document structure that all subsequent sections are inserted into. Their content is fully deterministic from approved KB assets.

**Gate condition:** All governance restrictions applied (no Gold Partner, no unapproved geographies, headcount "more than 50 Senior Consultants" only, B-BBEE expiry checked).

---

### Step 11 — Assemble Solution Sections

**What:** Assemble the solution capability sections (S-15 to S-29): Proposed Solution Overview, all platform capability sections, BeBanking sections.

**Output:** Solution section markdown blocks

**Why this order:** Solution sections depend on the Capability Selection (Step 5). They cannot be assembled before the selection is complete. The solution sections precede Understanding of Requirements (Step 12) in document position but are assembled after the Requirement Matrix is built — this ensures the solution accurately addresses the requirements rather than being copy-pasted without alignment.

**Gate condition:** Only BOM-triggered assets included; product boundary rules applied; all governance restrictions from Capability Selection list applied.

---

### Step 12 — Assemble Understanding of Requirements

**What:** Assemble the Understanding of Requirements section (S-14) by mapping each RFP requirement from the Requirement Matrix to a proposed solution element.

**Output:** Understanding of Requirements section markdown block

**Why this order:** This section depends on both the Requirement Matrix (Step 3) and the Solution sections (Step 11). It cannot be assembled before both are complete. This section demonstrates that the proposal has been written to the specific tender — it is the highest-priority AI-assisted section.

**Gate condition:** Every mandatory requirement addressed; gaps marked `[GAP: requirement not addressed — gap registered]`; AI-generated content flagged for human review.

---

### Step 13 — Assemble Delivery Sections

**What:** Assemble the methodology, project plan, governance, testing, data migration, training, and cutover sections (S-34 to S-43).

**Pattern 13 (AMS) note:** For AMS engagements, this step assembles only the governance sub-sections (S-36 Project Governance, S-37 RAID Framework) from the standard S-34–S-43 range — S-34, S-35, S-39–S-43 are excluded per AO-002 scoping rules. S-38 (Change Control) is also excluded for AMS (SI-001 fix). Following S-36/S-37, assemble the AMS Support Model sections within this step in the following order: **S-74 (Resource Model) → S-70 (Support Model) → S-71 (SLA Framework) → S-72 (Incident Management) → S-73 (Change Request Process) → S-75 (Release Management) → S-76 (Monitoring and Reporting)**. S-74 is assembled first as it defines who is delivering before the what (SI-005). Apply SI-007 content boundaries when assembling S-71 and S-72 — see CONTENT_SOURCE_MATRIX.md.

**Output:** Delivery section markdown blocks

**Why this order:** Delivery sections depend on the Methodology Selection (Step 7) and the Assumption Schedule (Step 8), which provides the delivery obligation language (DAT, TST, TRN, CUT assumption codes). The parallel payroll run default (HCM-CUT-005) is applied here.

**Gate condition:** Delivery pattern applied; project plan template used; parallel run default applied for HCM; CUT assumption language from pack used verbatim.

---

### Step 14 — Assemble People and References

**What:** Assemble the Team Structure section (S-46) from CONSULTANT_INDEX.csv and insert CV placeholders. Assemble the Client References section (S-67) from the Reference Selection (Step 6).

**Pattern 13 (AMS) note — SI-005:** For AMS engagements: (1) S-46, S-47, S-48 (Team Structure/CVs) are excluded — AMS uses a shared resource pool with no named team commitment. (2) References (S-67–S-69) must be assembled AFTER Step 15 (Commercial and Compliance), not before. The correct AMS proposal order per SI-005 is: AMS Support Model → Commercial (S-49→S-50→S-51→S-52) → Compliance → References → Appendices. Execute Step 14 References sub-step after Step 15 for AMS pattern.

**Output:** Team and References section markdown blocks

**Why this order:** People sections depend on the delivery pattern (resource model from Step 7). References depend on the Reference Selection (Step 6). These sections are assembled after solution sections because they support and validate the proposed solution with evidence — they follow solution commitment, not precede it.

**Gate condition:** AM approval obtained for all named references; CV placeholders inserted for APPTime retrieval; ADR-001 applied (no CV text from KB records); prohibited client naming rules applied.

---

### Step 15 — Assemble Commercial and Compliance Sections

**What:** Assemble the Key Assumptions body section (S-49), Scope Inclusions (S-30), Scope Exclusions (S-31), Change Control (S-38), and all compliance sections (S-55 to S-66).

**Pattern 13 (AMS) notes — SI-001, SI-006:** For AMS engagements: (1) S-38 (Change Control) is NOT assembled here — it is excluded for AMS; the change control governance is provided by S-73, assembled in Step 13 within the AMS Support Model. (2) The Commercial block must follow SI-006 ordering: **S-49 (Key Assumptions Body) → S-50 (Risk Register) → S-51 (Commercial Assumptions) → S-52 (Pricing) → S-53/S-54 (optional)**. (3) References (S-67–S-69) are assembled AFTER this step for AMS (SI-005) — complete Step 15 before returning to Step 14 References sub-step.

**Output:** Commercial and compliance section markdown blocks

**Why this order:** These sections depend on the Assumption Schedule (Step 8). The Key Assumptions body section is taken directly from the Assembly Engine KEY_ASSUMPTIONS output. Compliance sections require the Compliance Register to be checked against the submission date. Commercial Pricing remains a `[PLACEHOLDER — COMMERCIAL INPUT REQUIRED]` at this stage.

**Gate condition:** Key Assumptions section matches Assembly Engine output exactly; all compliance expiry dates verified; Commercial Pricing section explicitly flagged as placeholder.

---

### Step 16 — Assemble Appendices

**What:** Attach the complete Assumption Schedule (A-01), insert CV placeholders (A-02), insert reference letter placeholders (A-03), attach certifications and compliance documents (A-04 to A-06).

**Output:** Appendices section

**Why this order:** Appendices are assembled last because they consolidate the outputs of all prior steps. The Assumption Schedule appendix is inserted directly from the Assembly Engine output. This is the final content assembly step.

**Gate condition:** Assumption Schedule appendix is the WP17D-1 ASSUMPTION_SCHEDULE output exactly; no internal metadata present; all appendix items present or flagged.

---

### Step 17 — Run Proposal QA

**What:** Execute the Proposal QA Engine against the assembled proposal. Check completeness, consistency, traceability, governance compliance, scoring.

**Output:** `[TENDER_ID]_QA_REPORT.md` + Completeness Score + Risk Score

**Why this order:** QA runs on the complete assembled document. Running it on an incomplete document produces misleading results. QA is the final gate before human review and rendering.

**Gate condition:** Completeness Score ≥ 80 before proceeding to rendering; all blocking QA findings resolved or accepted by BU Lead.

**Engine:** Proposal QA Engine (WP18D — future). Manual review checklist in interim.

---

### Step 18 — BU Lead Review and Sign-Off

**What:** BU Lead reviews the assembled proposal, resolves `[GAP]` and `[PLACEHOLDER]` items, approves commercial sections, confirms reference and client naming compliance.

**Output:** Approved proposal document ready for rendering

**Why this order:** Human review is the final governance gate before a document is rendered and submitted. The factory produces the maximum automated output; BU Lead resolves the residual human-judgment items.

**Gate condition:** All `[GAP]` items either resolved or formally accepted; Commercial Pricing section populated; all `[CUSTOMISE]` items addressed; BU Lead sign-off recorded.

---

### Step 19 — Render Document

**What:** Convert the approved markdown proposal into the final DOCX/PDF format using the APPSolve proposal template.

**Output:** `[TENDER_ID]_PROPOSAL_V[X].docx`

**Why this order:** Rendering is the last step. A rendered document that requires further editing creates version control problems. Render only when content is approved.

**Gate condition:** QA Completeness Score passed; BU Lead sign-off obtained; all placeholders resolved.

**Engine:** Rendering Engine (WP19 — future). Manual DOCX assembly in interim.

---

## 3. Sequence Summary

| Step | Activity | Depends On | Engine / Owner |
|---|---|---|---|
| 1 | Ingest Tender Document | — | Bid Manager |
| 2 | Produce Tender Profile | Step 1 | AI + Bid Manager |
| 3 | Build Requirement Matrix | Step 2 | AI + Bid Manager |
| 4 | Resolve BOM | Step 2 | BOM_RESOLVER (existing) |
| 5 | Select Capability Assets | Steps 3, 4 | Capability Selector (WP18B) |
| 6 | Select References | Step 2 | Reference Selector (WP18B) |
| 7 | Select Methodology | Steps 2, 4 | Methodology Selector (WP18B) |
| 8 | Assemble Assumption Schedule | Step 4 | Assembly Engine (existing) |
| 9 | Run Gap Analysis | Steps 3–8 | Gap Analysis Engine (WP18C) |
| 10 | Assemble Corporate Sections | Step 2 | Proposal Assembly Engine (WP18B) |
| 11 | Assemble Solution Sections | Steps 5, 9 | Proposal Assembly Engine (WP18B) |
| 12 | Assemble Understanding of Requirements | Steps 3, 11 | Proposal Assembly Engine (WP18B) |
| 13 | Assemble Delivery Sections | Steps 7, 8 | Proposal Assembly Engine (WP18B) |
| 14 | Assemble People and References | Steps 6, 7 | Proposal Assembly Engine (WP18B) |
| 15 | Assemble Commercial and Compliance | Steps 8, Compliance check | Proposal Assembly Engine (WP18B) |
| 16 | Assemble Appendices | Steps 8, 13–15 | Proposal Assembly Engine (WP18B) |
| 17 | Run Proposal QA | Steps 3, 10–16 | Proposal QA Engine (WP18D) |
| 18 | BU Lead Review and Sign-Off | Step 17 | BU Lead |
| 19 | Render Document | Step 18 | Rendering Engine (WP19) |

---

## 4. Parallel Execution Opportunities

Steps 5, 6, and 7 can run in parallel after Step 4 completes.  
Step 8 can run in parallel with Steps 5–7 after Step 4 completes.  
Steps 10 and 11 can begin concurrently once Steps 5 and 9 are complete.  
Steps 13 and 14 can run in parallel once Steps 7 and 8 are complete.  

---

## 5. Interim Operating Mode (Before Full WP18B/WP18C/WP18D Build)

Until WP18B, WP18C, and WP18D are built, the following interim process applies:

| Step | Interim Method |
|---|---|
| Steps 1–4 | Bid Manager completes Tender Profile + BOM manually; BOM_RESOLVER runs as existing |
| Steps 5–7 | Bid Manager uses PROPOSAL_STRUCTURE_LIBRARY.md and ASSEMBLY_READINESS_MATRIX.md to select assets |
| Step 8 | Assembly Engine runs as existing (PRODUCTION READY) |
| Step 9 | Bid Manager reviews gap checklist from PROPOSAL_GAP_ANALYSIS_FRAMEWORK.md |
| Steps 10–16 | Bid Manager assembles sections using PROPOSAL_STRUCTURE_LIBRARY.md as guide |
| Step 17 | Bid Manager runs manual QA checklist from PROPOSAL_QA_FRAMEWORK.md |
| Steps 18–19 | BU Lead review + manual DOCX assembly (as per current Plennegy process) |

---

## 6. Pattern-Specific Assembly Notes (WP18C.2)

### Pattern 13 — AMS Complete Assembly Order

AMS proposals follow a different section order than Implementation patterns. The complete AMS-specific sequence is:

| Document Position | Sections | Assembled In Step |
|---|---|---|
| Corporate | S-01 to S-12 (M-ALL + COND-ORA/ACU/BB per platform) | Step 10 |
| Executive Summary + Understanding | S-13, S-14 | Steps 12, 12 |
| Solution Capability | S-15; platform capability sections (S-16–S-21 per BOM) | Step 11 |
| Scope | S-30, S-31, S-32, S-33 | Step 13 |
| Governance | S-36, S-37 | Step 13 |
| AMS Support Model | **S-74 → S-70 → S-71 → S-72 → S-73 → S-75 → S-76** | Step 13 |
| Commercial (SI-006 order) | **S-49 → S-50 → S-51 → S-52** | Step 15 |
| Compliance | S-55 to S-60 | Step 15 |
| References (SI-005 — after commercial) | S-67, S-69 | Step 14 (run after Step 15) |
| Appendices | A-01, A-03, A-04, A-05 | Step 16 |

**AMS sections excluded (per PROPOSAL_PATTERN_ENGINE.md Section 4.1):**
S-34, S-35, S-38, S-39, S-40, S-41, S-42, S-43, S-46, S-47, S-48

**SI-005 — Reference ordering fix:** For AMS proposals, References appear AFTER Commercial and Compliance, not before. Assemble Step 14 (References sub-step) after Step 15 is complete.

**SI-006 — Assumption ordering fix:** Key Assumptions (S-49) appears BEFORE Pricing (S-52) in all proposals: S-49 → S-50 → S-51 → S-52 → S-53/S-54 (optional).

**AMS Support Model internal order:** S-74 (Resource Model) is assembled FIRST — the client must understand who is delivering before they can contextualise the delivery model, SLAs, and incident process.

**SI-007 — Content boundaries:** When assembling S-71 and S-72, apply content boundaries from CONTENT_SOURCE_MATRIX.md: S-71 = SLA tier table only; S-72 = incident process only; never duplicate SLA values in S-72.

---

*PROPOSAL_ASSEMBLY_SEQUENCE.md v1.1 | WP18A — Proposal Factory Architecture | Updated WP18C.2 2026-06-26*  
*19-step deterministic assembly sequence. Governs WP18B Proposal Assembly Engine.*  
*v1.1: SI-001 S-38 AMS exclusion notes; SI-005 AMS reference ordering; SI-006 assumptions-before-pricing; SI-007 S-71/S-72 content boundaries; Pattern 13 AMS complete assembly table added (Section 6).*
