---
document_id: WP18C1-FACTORY-OPTIMISATION-REVIEW
title: "WP18C.1 — Proposal Factory Optimisation Review"
version: "1.0"
status: "COMPLETE — 2026-06-25"
created: "2026-06-25"
created_by: "WP18C.1 — Proposal Factory Optimisation"
input: "WP18C first production run: ARM IT045 (EBS AMS Full Stack)"
scope: "Architecture refinement based on evidence from first production run. No content authoring."
---

# WP18C.1 — Proposal Factory Optimisation Review

**Purpose:** Use the WP18C ARM IT045 first production run as a diagnostic instrument to identify structural weaknesses in both the assembled proposal and the factory engine. This is an architecture refinement exercise.

**Evidence base:** ARM_IT045_PROPOSAL_DRAFT.md, ARM_IT045_PROPOSAL_ASSEMBLY_REPORT.md, ARM_IT045_PROPOSAL_READINESS.md, ARM_IT045_FACTORY_GAP_REGISTER.md, WP18C_PROPOSAL_FACTORY_IMPLEMENTATION.md.

---

## 1. Phase 1 — Proposal Review

Four reviewer perspectives on the assembled ARM IT045 proposal draft.

---

### 1.1 Client Evaluator Perspective

Reading as the procurement lead at African Rainbow Minerals evaluating APPSolve's AMS proposal.

**Strong sections:**
- The AMS Support Model sections (S-70 through S-76) are comprehensive, structured, and clearly sourced. An ARM evaluator would find the SLA table (S-71) and Incident Management process (S-72) credible and specific.
- The Assumption Schedule (A-01, 594 assumptions) is unusual and differentiating — very few AMS vendors provide this level of scope definition up front.
- The company credentials sections (S-03 through S-12) are consistent and professional.

**Weak sections — evaluation risk:**

| Issue | Section | Severity | Observation |
|---|---|---|---|
| Executive Summary lacks personalisation | S-13 | HIGH | ARM is an existing client. The AI-generated executive summary reads as generic ("APPSolve proposes..."). A client who previously engaged APPSolve expects acknowledgement of that history. The unique selling point of ARM IT045 — continuity of knowledge — is buried in point 2. It should be the opening line. |
| OCI narrative is generic | S-22 | HIGH | The OCI Infrastructure section reads as technical documentation, not a capability statement. It describes what APPSolve will manage but not why APPSolve is the right choice to manage it. No reference to OCI delivery experience; no ARM-specific OCI context (existing environment, tenancy setup). |
| No solution architecture diagram | ALL | MEDIUM | For an OCI-hosted EBS AMS engagement, a single architecture diagram showing "ARM Oracle Stack → OCI → APPSolve AMS Team" would be the most persuasive page in the proposal. Text descriptions of a technical architecture are hard to evaluate. The current draft has no diagram, map, or visual. |
| Risk Register reads as AI-generated | S-50 | HIGH | The 9 risks are plausible but generic. A client evaluating an AMS RFP for their specific Oracle environment would notice that none of the risks reference ARM's specific context (Oracle EBS v12.2.8 HR, 1,787 users, multi-site payroll). Generic risk registers signal a generic vendor. |
| No case study | S-68 | MEDIUM | For AMS proposals, the question is always "who else are you doing this for?" The proposal answers with references (S-67) but has no case study showing what a day in the life of APPSolve's AMS service looks like. |
| Understanding section has no RFP traceability | S-14 | MEDIUM | S-14 reads as "here is what we think you need" rather than "here is what you said you need in clause 3.2 of your RFP." Without mapping back to actual RFP requirements, the client cannot verify that APPSolve understood and responded to their specific requirements. |

**Flow issues:**

The proposal's reading sequence places References (S-67) immediately after the Risk Register and before the AMS Support Model. This is backwards for an AMS proposal. A client evaluating an AMS service needs to understand the service model before they care about credentials. The current sequence presents credentials before service delivery, which creates the impression of a company listing its history before explaining what it will do.

**Missing transition: Corporate → Understanding.** The proposal moves abruptly from the B-BBEE statement (S-12) to the Executive Summary (S-13). A two-sentence bridge (currently absent) would make this transition coherent.

---

### 1.2 APPSolve Delivery Manager Perspective

Reading as the person who would deliver this service and be held accountable for the proposal's commitments.

**Structural issue 1 — Change Control is described twice:**

S-38 (Part 3 — Governance) and S-73 (Part 8 — AMS Support) both describe the change request process and change classification table. The content is substantially the same. A client who reads carefully will notice this repetition and question whether the two descriptions are consistent. They are, in this case — but this is a factory defect, not a proposal quality achievement.

**Root cause:** S-38 is a generic governance section applicable to all proposal types. S-73 is an AMS-specific change request section. For an AMS proposal, the AMS section (S-73) is the correct and complete source. S-38 should be excluded from AMS proposals entirely.

**Structural issue 2 — SLA Framework and Incident Management overlap:**

S-71 (SLA Framework) contains the priority table with Acknowledgement and Resolution SLAs. S-72 (Incident Management) contains the P1 escalation timeline (T+0, T+15, T+30, T+60, T+120 minutes). The T+15 milestone in S-72 ("ARM IT Contact notified — acknowledgement SLA") duplicates the "15 minutes acknowledgement" figure already in S-71's table. They're not inconsistent, but a delivery manager would ask: where is the authoritative source for P1 acknowledgement time — S-71 or S-72?

**Root cause:** These two sections were assembled from different sources (EBS-SLA Overlay for S-71; AMS pack for S-72) without a deduplication pass. The SLA table and the escalation process should reference each other but not duplicate SLA time values.

**Structural issue 3 — Team Structure / Resource Model split:**

S-46 (Team Structure — Part 4) defines roles and allocation. S-74 (Resource Model — Part 8) defines hours governance, utilisation reporting, and rollover rules. These are two halves of the same topic. A delivery manager committing to the team structure needs to read both sections to understand the complete picture. A client evaluating whether 680h/month is adequate needs to read both sections to see who does what.

**Root cause:** The PROPOSAL_SECTION_LIBRARY places S-46 in "People" (Section 8 of the library) and S-74 in "Support and Managed Services" (Section 10). The distinction makes sense for the library but produces a fragmented reading experience in a proposal.

**Structural issue 4 — Assumptions appear before commercial:**

S-49 (175 Key Assumptions) appears in Part 5 before S-52 (Commercial). The assumptions define the commercial scope. A client who hasn't seen the commercial offer yet has no framework for evaluating what the assumptions mean. In a well-structured AMS proposal, the sequence should be: Commercial Proposal → Key Assumptions governing it → Full Assumption Schedule (appendix).

**Structural issue 5 — No resource hour breakdown per role:**

The Team Structure (S-46) shows 7 roles, 680h/month total, with [X]h/month per role. The monthly hour allocation per role is left as a placeholder. From a delivery management perspective, this is incomplete — the client cannot evaluate whether the hours allocation is sufficient for their needs without seeing the breakdown. The BU Lead must fill this in, but the template does not prompt a specific breakdown.

---

### 1.3 Commercial Director Perspective

Reading as the Commercial Director who must approve the submission and sign off the commercial structure.

**Issue 1 — S-52 is entirely blank:**

The commercial section is a pure PLACEHOLDER with no structure at all. The Commercial Director has no template, no heading structure, and no indication of what the proposal expects. For a fixed-price AMS engagement, the minimum structure needed is: Monthly Retainer Fee, Change Request Rate (basis only, no actual rate), Optional Services, Contract Term, Payment Terms. None of this structure exists in the current draft.

**Impact:** The Commercial Director must build the entire section from scratch. This is 2–4 hours of authoring when a 30-minute fill-in would suffice with a template.

**Issue 2 — Resource hours are commercially visible without pricing context:**

680h/month is cited in S-74 (Resource Model) without any commercial context. A client sees a large monthly hours commitment and may perceive APPSolve as expensive before seeing the pricing. The relationship between hours and cost should be managed carefully — the commercial section should frame the value of 680h/month before the client does their own cost-per-hour arithmetic.

**Issue 3 — No commercial structure for out-of-scope work:**

The proposal mentions that out-of-scope changes will be "separately priced" multiple times (S-38, S-73), but there is no indication of the mechanism. Is it T&M? Project-priced? Day-rate? Without this, the client cannot evaluate the commercial risk of scope changes. The commercial section template should include at minimum: "Out-of-scope changes are governed by a Change Request process and priced at [COMMERCIAL INPUT — mechanism]."

**Issue 4 — Contract term not mentioned:**

Nowhere in the proposal is the contract term or renewal structure mentioned. AMS proposals typically specify: initial term, notice period, renewal mechanism, price escalation clause. None of this appears. A client planning a multi-year Oracle AMS contract would expect to see this.

---

### 1.4 Oracle Pre-Sales Reviewer Perspective

Reading as an Oracle practice expert assessing whether the proposal makes APPSolve look qualified for EBS AMS.

**Issue 1 — Oracle Partnership section is thin:**

S-09 (Oracle Partnership) states that APPSolve holds Oracle Level 1 Partner status and describes what OPN membership provides. This is accurate but generic. For an AMS RFP, the relevant Oracle partnership capability is access to Oracle Support escalation, Oracle patch information ahead of general availability, and Oracle co-support models. These are not mentioned. The section describes the partnership's benefits to APPSolve, not to ARM.

**Issue 2 — EBS version coverage gap:**

S-14 (Understanding of Requirements) correctly identifies ARM's EBS versions (v12.2.8 HR/Payroll, v12.2.10 Financials). S-18 (Oracle EBS Capability) does not confirm that APPSolve has experience with these specific versions. An evaluator would expect the capability statement to mirror back the client's version environment. Currently they must connect S-14 and S-18 themselves.

**Issue 3 — OIC section is disconnected from ARM's OIC landscape:**

S-19 describes APPSolve's OIC capability and accelerator library in general terms. The ARM-specific paragraph is one sentence: "For ARM IT045: ARM's OIC integration landscape will be baselined during onboarding." An Oracle pre-sales reviewer would want more: what is ARM's known OIC configuration? What integration flows are currently active? At minimum, a sentence about OIC in the context of ARM's multi-site EBS environment would personalise this section.

**Issue 4 — S-15 (Proposed Solution Overview) duplicates capability sections:**

S-15 describes four pillars: EBS Application Support, DBA Services, OIC, OCI. Each of these pillars then has its own dedicated section (S-18 through S-22). The result is that EBS AMS services are described at two levels of detail — overview in S-15 and deep-dive in S-18–S-22. This is appropriate in principle, but in the current draft, S-15 and S-21 (Oracle Managed Services) overlap significantly — both describe the AMS service model. An Oracle pre-sales reviewer would identify this as redundant and potentially confusing.

---

## 2. Phase 2 — Assembly Engine Review

Stage-by-stage analysis of the 10-stage factory pipeline.

---

### 2.1 Stage 0 — Tender Intake (Not in Current Pipeline)

**Status: MISSING — CRITICAL GAP**

The current 10-stage pipeline begins at Stage 1 (Tender Analysis). But there is no structured intake mechanism. In the WP18C run, the engagement type (EBS AMS Full Stack), BOM codes, SLA tier, and resource model were all known a priori — this was a won tender used as a test case. For a live tender, there is no mechanism to capture these inputs in a structured form before Stage 1 begins.

**Impact:** Every factory run currently starts with an implicit, unstructured context-gathering step. This step is invisible, inconsistent, and not documented in the assembly audit trail. For the factory to be repeatable, a structured Tender Profile must be the first output of every run.

**Recommendation:** Add Stage 0 — Tender Profile Intake — as the factory's entry gate. Output: a structured YAML/markdown file with: tender_id, client, engagement_type, bom_codes[], modules[], sla_tier, resource_model, client_sector, submission_date, compliance_requirements[]. This is created by the Bid Manager and becomes the input to all subsequent stages. See AO-009 in the Automation Opportunity Register.

---

### 2.2 Stage 1 — Tender Analysis

**Status: Defined in architecture; not yet built.**

The architecture document defines this stage correctly. The implementation shortcut — a human-completed Tender Profile form — is the right interim approach. The full AI parsing engine is a longer-term investment.

**Issue:** The 19-step PROPOSAL_ASSEMBLY_SEQUENCE.md conflates "processing sequence" (what to compute first) with "reading sequence" (section order in the final document). These are different concerns and should be documented separately. The ASSEMBLY_SEQUENCE's 19 steps are a useful processing checklist but are not the same as the table of contents structure. A future assembly engine implementation will need both.

---

### 2.3 Stage 2 — Requirement Extraction

**Status: Not built; AI proxy used in WP18C.**

S-14 (Understanding of Requirements) was AI-generated from tender context. No formal requirement matrix was produced. The gap between "AI guess at requirements" and "formal requirement-to-section mapping" is the largest quality gap in the current output.

**Issue:** Without a requirements matrix, there is no traceability from RFP clauses to proposal sections. This matters most for scored tenders (tenders with evaluation criteria). For ARM IT045 (a negotiated win), this was acceptable. For a competitive tender, missing a specific RFP requirement could be disqualifying.

**Recommendation:** Before Stage 2 is built as an engine, introduce a "Requirements Checklist" step where the Bid Manager manually populates a structured list of RFP requirements and maps each to a proposal section. This can be a markdown table. It is not automated but it is structured, traceable, and inspectable. This costs 2–4 hours per tender and provides significant quality benefit.

---

### 2.4 Stage 3 — BOM Resolution

**Status: PRODUCTION READY — no issues.**

The BOM_RESOLVER and PACK_LOADER performed correctly in WP18C. 6 packs loaded; 594 net assumptions; 6 suppressions applied correctly. This stage is mature and requires no change.

---

### 2.5 Stage 4 — Capability Selection

**Status: Manual; high automation potential.**

In WP18C, Stage 4 was performed manually: the analyst read the BOM, thought about the engagement type, and selected 12 capability assets. This process took approximately 60 minutes and required significant context knowledge.

**Issue:** The selection logic is deterministic and already documented:
- BOM includes EBS → select W2S1-002
- BOM includes DBA → select W2S1-003
- BOM includes AMS → select W2S1-004
- BOM includes OIC → select W4-INT-001
- BOM includes OCI → select W2S1-004 (infrastructure section) + [OCI narrative — GAP]
- All proposals → select W1S1-001 through W1S1-009 (corporate sections)
- Engagement type = Oracle → select W1S1-003 (Oracle Partnership)

This is a lookup table. It requires no AI. Encoding it as a capability selection rule table in the CONTENT_SOURCE_MATRIX.md would convert Stage 4 from 60-minute manual to <5-minute deterministic. See AO-001.

**Issue 2:** There is no "deselection rule" — the factory selected all corporate assets by default. For a short-form tender or an Acumatica proposal, some corporate assets may be inappropriate or redundant. A deselection rule (e.g., do not include W1S1-003 Oracle Partnership if platform = Acumatica) would prevent inappropriate asset inclusion.

---

### 2.6 Stage 5 — Reference Selection

**Status: Manual; partially automatable.**

Reference selection was manual in WP18C. The analyst ranked references by relevance (ARM=exact match, Assore/Adcock=EBS sector match, MTN=OCI/OIC match). This logic is already codified in the architecture (R5.8 scoring rules). REFERENCE_MASTER.csv contains product, sector, and client fields that enable algorithmic scoring.

**Issue:** The AM approval requirement is correctly non-negotiable but is not documented as a formal workflow step. Currently it is a note in the Assembly Report. It should be a named stage gate: reference selection is not final until AM approval is logged.

**Recommendation:** Encode R5.8 scoring as a computation against REFERENCE_MASTER.csv. Output: ranked reference list with scores. The Bid Manager and AM review and approve. AM approval is a logged gate — no submission without it. See AO-003.

---

### 2.7 Stage 6 — Methodology Selection

**Status: Manual; fully automatable via lookup.**

The methodology selection for ARM IT045 (Pattern 13 — AMS Onboarding; W2S1-004 for AMS model; W2S1-005 for governance framework) was correct but manual. The DELIVERY_PATTERN_LIBRARY.md defines 13 patterns. The selection rule is: engagement_type → pattern_id.

This is a 1:1 lookup:
- AMS engagement → Pattern 13
- Implementation + Oracle → Patterns 1–9 (further refined by module mix)
- Implementation + Acumatica → Pattern 11
- BeBanking → Pattern 12
- DBA-only → Pattern 10

Encoding this as a lookup in the PROPOSAL_ASSEMBLY_SEQUENCE.md (or a new METHODOLOGY_SELECTOR_RULES.md) would make Stage 6 fully deterministic. See AO-004.

---

### 2.8 Stage 7 — Assumption Assembly

**Status: L5 — PRODUCTION READY — no issues.**

The Assembly Engine produced 594 net assumptions in 8 sections, correctly applied 6 suppression rules, and produced both the complete schedule and the 175-assumption key assumptions body section. This stage is the factory's most mature component and requires no improvement.

---

### 2.9 Stage 8 — Proposal Assembly

**Status: Operational (WP18C); structural issues identified.**

The WP18C run validated that Stage 8 can produce a 57-section proposal from governed KB assets. The structural issues identified are primarily in two areas:

**Issue 1 — Section order vs processing order conflation:**
The PROPOSAL_ASSEMBLY_SEQUENCE.md defines a 19-step assembly processing sequence. The WP18C run assembled sections in the document's reading order (front-to-back). These are different. The processing sequence should determine what data is computed first (e.g., BOM resolution before capability selection, assumptions before scope inclusions). The reading sequence determines what the client reads first. Both are needed; neither is currently authoritative for Stage 8.

**Issue 2 — One-pass assembly; no feedback loop:**
Stage 8 assembles all sections in a single pass. If a section is identified as GAP during assembly, there is no mechanism to attempt an alternative source or flag it for a targeted enrichment pass. The factory moves past gaps to completion. For a production system, a second pass — attempting fallback sources for GAP sections — would increase deterministic coverage without requiring human intervention.

**Issue 3 — Cross-section consistency not checked:**
After assembly, there is no cross-section consistency check. In ARM IT045, S-38 and S-73 describe the same CR process. S-71 and S-72 duplicate SLA times. These inconsistencies are invisible to Stage 8 because it assembles each section independently. A post-assembly consistency check (comparing SLA values, CR descriptions across sections) would catch these before QA.

---

### 2.10 Stage 9 — Proposal QA

**Status: Manual computation (WP18C); QA framework validated.**

The QA Framework (PROPOSAL_QA_FRAMEWORK.md) was applied manually in WP18C to produce a score of 72/100. The scoring model is well-defined. Most QA checks are binary and deterministic:
- Is section X at READY/PARTIAL/GAP? → deterministic
- Is the B-BBEE certificate expired? → deterministic (compare dates)
- Is the commercial section PLACEHOLDER? → deterministic
- Are all governance rules applied? → deterministic

Only 2 of 12 QA categories genuinely require human judgement (content quality of AI-generated sections; reference completeness with AM approval). All others can be automated.

**Recommendation:** WP18D (Proposal QA Engine) should prioritise the 10 deterministic QA checks first. The 2 subjective checks remain human. This would produce an automated QA score for the deterministic dimensions, with the human-only dimensions clearly flagged.

---

### 2.11 Stage 10 — Rendering

**Status: Not built; markdown-only output.**

The WP18C output is markdown. No DOCX or PDF rendering is available. For live tender submissions, this is the final bottleneck. However, rendering is the last dependency — the content must be correct before rendering matters.

**Issue:** The rendering engine must handle two output types: a formatted Word document (for tender submission) and a structured markdown document (for the KB). These are different layouts. The DOCX must follow a style guide; the markdown must maintain source attribution headers. These require separate templates.

---

## 3. Structural Issues — Priority Summary

The following structural issues were identified across Phase 1 and Phase 2. Listed by impact:

| # | Issue | Type | Sections Affected | Impact | Fix Effort |
|---|---|---|---|---|---|
| SI-001 | Change Control described twice | Duplication | S-38 + S-73 | HIGH — client confusion; quality signal | 1h — library rule update |
| SI-002 | No Stage 0 Tender Profile Intake | Pipeline gap | All stages | HIGH — every run starts without structured input | 2h — form design |
| SI-003 | Stage 4/5/6 selection is manual | Automation gap | Stage 4, 5, 6 | HIGH — 60–90 min manual effort per run | 8–12h — rules encoding |
| SI-004 | Team Structure / Resource Model split | Fragmentation | S-46 + S-74 | MEDIUM — reading experience; BU coordination | 2h — cross-reference rule |
| SI-005 | References appear before AMS model | Ordering | S-67 vs S-70–S-76 | MEDIUM — reading sequence logic | 30min — section order change |
| SI-006 | Assumptions appear before commercial | Ordering | S-49 vs S-52 | MEDIUM — client evaluates assumptions without commercial context | 30min — section order change |
| SI-007 | SLA/Incident Management overlap | Duplication | S-71 + S-72 | MEDIUM — SLA values cited twice; which is authoritative? | 1h — clean-split rule |
| SI-008 | Executive Summary not personalised | Content | S-13 | MEDIUM — generic for a known client | Factory limitation; requires AI context enrichment |
| SI-009 | Processing sequence ≠ reading sequence | Architecture | PROPOSAL_ASSEMBLY_SEQUENCE.md | MEDIUM — future build risk | 2h — document both explicitly |
| SI-010 | No commercial section template | Content gap | S-52 | MEDIUM — CD authors from scratch | 1h — template |
| SI-011 | One-pass assembly; no fallback | Engine | Stage 8 | LOW (MVP limitation) | Future build |
| SI-012 | No cross-section consistency check | Engine | Stage 8 | LOW (MVP limitation) | Future build |

---

## 4. What the Factory Did Well

This section preserves evidence of what should not change.

| Category | Finding |
|---|---|
| Assumption Assembly | Perfect. 594/594 assumptions; both output formats; governance rules applied. No change needed. |
| Scope extraction | S-30, S-31, S-33 were all READY from assumption pack sections. The INC/EXC/DEP assumption code classification works excellently as a scope source. |
| AMS support section assembly | S-70–S-76 were all READY or PARTIAL from assumption packs + W2S1-004. The AMS pack is an excellent proposal content source, not just a commercial protection mechanism. |
| Governance rule checking | All 14 rules checked; 13 PASS; 1 FLAG. The governance check was comprehensive and proactive (G-08 B-BBEE flag identified without prompting). |
| Section scoping decision | 57 from 82 sections correctly identified. The 25 excluded sections were all correct for an EBS AMS engagement. |
| Corporate sections | S-03 through S-09 all READY from KB assets. The corporate section library is production-quality. |
| Gap identification | 14 gaps with severity, root cause, and remediation were comprehensive and actionable. The gap framework (PROPOSAL_GAP_ANALYSIS_FRAMEWORK.md) works. |
| Compliance section | COMPLIANCE_REGISTER.csv-derived compliance schedule identified the B-BBEE expiry automatically. Compliance section assembly was reliable. |

---

## 5. Summary Findings

**Headline finding:** The factory's architecture is sound. The 77.2% deterministic assembly rate on the first production run exceeds the 60% success criterion. The remaining 22.8% non-deterministic content divides cleanly into: permanently non-automatable (CVs, commercial pricing ~7%), temporarily non-automatable due to missing KB assets (OCI, Risk Register ~12%), and AI-assisted content that will remain partially human-gated by design (Executive Summary, Understanding ~4%).

**Most valuable near-term action:** Encode Stages 4, 5, and 6 as lookup tables. These three manual stages are the largest source of non-systematic variation between factory runs. They require no content authoring — only rules documentation. They are currently taking 60–90 minutes of manual effort per run. Encoding them as deterministic rules reduces this to near-zero while making future runs reproducible.

**Most damaging structural issue:** S-38 and S-73 describe the same process. This is a factory defect that will recur on every AMS tender until it is fixed. The fix is a 1-hour update to the PROPOSAL_SECTION_LIBRARY to add a scoping rule: for AMS proposals, exclude S-38 (Change Control is entirely covered by S-73).

**Biggest proposal quality gap:** The Executive Summary (S-13) is the most-read section of any proposal and the one with the weakest assembly in this run. It requires AI generation and is inherently relationship-specific — the factory cannot eliminate human review here. But it can produce a better AI draft by injecting richer context: prior relationship details (from REFERENCE_MASTER.csv), the specific client pain point addressed, and the unique differentiator relevant to this tender. This requires a richer AI context brief, not more KB content.

**Pipeline readiness for live tenders:** The factory is ready for supervised use on live tenders. A Bid Manager can use the WP18C process with confidence for any Oracle EBS AMS tender. The 3-action pre-run checklist is: (1) create Tender Profile, (2) confirm BOM codes, (3) confirm AM for reference approval. All other factory stages follow deterministically from those inputs.

---

*WP18C1_FACTORY_OPTIMISATION_REVIEW.md v1.0 | WP18C.1 — Proposal Factory Optimisation | 2026-06-25*  
*Phase 1 (Proposal Review) + Phase 2 (Engine Review) complete. 12 structural issues identified; 4 reviewer perspectives covered; 11 "what worked" findings preserved.*
