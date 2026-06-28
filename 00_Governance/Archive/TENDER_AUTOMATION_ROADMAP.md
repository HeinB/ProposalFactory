# Tender Automation Roadmap
**Work Package:** WP5 — Tender Response Factory | **Version:** 1.0 | **Created:** 2026-06-14
**Purpose:** Defines the phased progression from the current manual tender assembly process toward near-automated tender response generation using the approved Knowledge Base.

---

## 1. Current State Baseline

**As of 2026-06-14:**

| Dimension | Current State |
|---|---|
| Approved KB assets | 47 (6 Corporate, 21 Oracle, 9 Acumatica, 11 BeBanking) |
| Assembly process | Fully manual — consultant searches KB, copies sections, assembles into response |
| Governance checking | Fully manual — relies on consultant knowledge of 20+ governance rules |
| Reference retrieval | Partially manual — approved letters not yet registered in `04_References/` |
| CV sourcing | Fully manual — APPTime (external; no KB integration) |
| Repeatability | Low — no structured assembly framework in use per tender |
| Pilot coverage | 67% (Acumatica); ~85% (Oracle HCM estimated) |

**The core problem:** A consultant producing a tender response today must:
1. Locate relevant KB assets across multiple folders
2. Recall which governance restrictions apply to each asset
3. Manually draft bridging text between assets
4. Apply all section exclusions (14.2, 13.2, etc.) from memory
5. Verify reference letter status
6. Confirm the result with BU Lead before submission

**The target:** An AI-assisted workflow where 80%+ of narrative content is assembled from approved KB assets with minimal human drafting, and all governance checks are run automatically before BU Lead review.

---

## 2. Roadmap Overview

```
Phase 1          Phase 2            Phase 3              Phase 4
Structured       AI-Assisted        Semi-Automated        Near-Automated
Manual Assembly  Draft Generation   Assembly Pipeline     Response Factory
(Now → Q3 2026) (Q3 2026)         (Q4 2026)            (H1 2027)

[Checklists]  → [Prompt Library]  → [KB Integration]   → [Full AI Draft]
[Recipes]     → [AI First Draft]  → [Auto Governance]  → [BU Lead Review Only]
[Gap IDs]     → [Gap Flagging]    → [Ref Integration]  → [80%+ Coverage All Types]
```

---

## 3. Phase 1 — Structured Manual Assembly (Now → Q3 2026)

**Status:** Partially complete. Framework documents written. Implementation in progress.
**Goal:** Every tender response uses the structured assembly recipes from this WP5 session. No more ad-hoc assembly.

### Enabling Actions (Phase 1)

| # | Action | Owner | Deadline | Impact |
|---|---|---|---|---|
| 1.1 | Onboard team to `ANSWER_ASSEMBLY_FRAMEWORK.md` — 8 recipes; governance checklist | BU Lead | 2026-06-30 | Eliminates unstructured tender assembly |
| 1.2 | Onboard team to `TENDER_COMPONENT_LIBRARY.md` — 17 categories; asset classification | BU Lead | 2026-06-30 | Enables rapid asset location |
| 1.3 | Register Oracle reference letters from SABS ETS corpus (Investec, NALA, CUM, Assore, Adcock, Mr Price) | KB Operator | 2026-07-15 | **Unlocks named references for 3 ERP assets; immediate coverage boost** |
| 1.4 | Register Acumatica reference letters (DSSSA, FuelU2, Maxiflex) from AFROSAI-E corpus | KB Operator | 2026-07-15 | Expands Acumatica reference set |
| 1.5 | Confirm CUM scope (Oracle Finance vs. Acumatica/PaySpace) | BU Lead / Account | 2026-07-15 | Resolves AM-W4E2-001 |
| 1.6 | BEE certificate renewal | Admin | **2026-07-31 (HARD)** | Required for all tenders |
| 1.7 | Print and post `TENDER_QUESTION_TAXONOMY.md` (Sections A–M) as a reference guide | BU Lead | 2026-07-31 | Enables rapid question-to-asset lookup during RFP response |
| 1.8 | Apply Standard Governance Checkpoint (from ANSWER_ASSEMBLY_FRAMEWORK.md) to every tender submission | All consultants | Ongoing | Systematic governance compliance |

### Phase 1 Success Criteria
- All tenders use documented assembly recipes (not ad-hoc)
- All 6 SABS ETS reference letters registered in `04_References/Oracle/`
- Standard Governance Checkpoint applied before every submission
- Coverage for Acumatica tenders: 67% → **75%** (reference letters registered)
- Coverage for Oracle HCM tenders: 85% → **85%** (no new assets needed; process improvement)

---

## 4. Phase 2 — AI-Assisted Draft Generation (Q3 2026)

**Goal:** Use an AI assistant (Claude or similar) loaded with the approved KB to generate first-draft tender sections. Human effort shifts from drafting to reviewing and refining AI output.

### Concept

An AI assistant configured with:
- All 47 approved KB asset texts as context
- The TENDER_QUESTION_TAXONOMY.md as a retrieval index
- The ANSWER_ASSEMBLY_FRAMEWORK.md as assembly rules
- The governance checkpoint as a pre-submission filter

...can receive a tender question and output a draft response by combining the relevant KB assets, identifying which assets apply, and flagging governance restrictions inline.

### Enabling Actions (Phase 2)

| # | Action | Owner | Deadline | Impact |
|---|---|---|---|---|
| 2.1 | Develop prompt library: one prompt per question category in TENDER_QUESTION_TAXONOMY.md (Sections A–M) | KB Operator / BU Lead | 2026-08-31 | Foundation for AI draft generation |
| 2.2 | Author Acumatica Support & Managed Services statement (W5-ACU-001) — BU Lead authorisation required | BU Lead decision | 2026-08-31 | **Closes highest narrative gap (Phase 1 Finding 1); +10-15% Acumatica coverage** |
| 2.3 | Extract APPSolve Project Methodology (Feb 2024 PDF) into KB as platform-agnostic methodology statement | KB Operator | 2026-08-31 | Closes methodology gap for Acumatica; +5-10% Acumatica coverage |
| 2.4 | Implement Claude Code project with full KB asset library as context | Technical | 2026-09-30 | Enables AI-assisted draft generation with KB context |
| 2.5 | Create "Tender Briefing Template" — standard intake form capturing: tender type, modules, geography, reference requirements, compliance documents needed | BU Lead | 2026-08-31 | Structured input for AI prompt system |
| 2.6 | Draft and approve standalone Change Management / OCM statement (platform-agnostic) | KB Operator / BU Lead | 2026-09-30 | Closes recurring gap across all tender types |
| 2.7 | Establish APPTime ↔ KB integration protocol for Consultant Index Records (ADR-001) | BU Lead / APPTime admin | 2026-09-30 | Enables AI to reference consultant profiles (not CVs — per ADR-001) without manual lookup |

### Phase 2 Target State

```
INPUT: Tender RFP document + Tender Briefing Template
          ↓
AI (Claude + KB context)
          ↓
OUTPUT: Draft tender response with:
  • Section-by-section narrative (from KB assets)
  • Inline governance flags ("⚠️ AM approval required for HB reference")
  • Gap markers ("✍️ Acumatica support model — requires human authoring")
  • Suggested CV profiles from Consultant Index
          ↓
Human review: fills gaps, confirms governance, refines language
          ↓
BU Lead: signs off named references + final review
```

### Phase 2 Success Criteria
- AI draft generation active for Oracle HCM, Oracle ERP, BeBanking tender types
- Acumatica support model authored (W5-ACU-001)
- Platform-agnostic methodology in KB
- Time from RFP receipt to first draft: **≤ 4 hours** (vs. 1-2 days currently estimated)
- Coverage for Acumatica tenders: 75% → **85%** (support model + methodology closed)
- Coverage for Oracle HCM tenders: 85% → **90%**

---

## 5. Phase 3 — Semi-Automated Assembly Pipeline (Q4 2026)

**Goal:** Formalize the AI-draft process into a repeatable pipeline. Governance checking becomes partially automated. Reference retrieval is integrated.

### Enabling Actions (Phase 3)

| # | Action | Owner | Deadline | Impact |
|---|---|---|---|---|
| 3.1 | Build governance rule engine: automated scan of draft text against 20+ standing rules (DFA, SAA, CCBA, billing figures, section exclusions) | Technical | 2026-10-31 | Auto-flags violations before BU Lead review |
| 3.2 | Integrate `04_References/` letter register into assembly pipeline — auto-check reference availability before citing a client | Technical / KB Operator | 2026-10-31 | Eliminates manual reference status checks |
| 3.3 | Register KPMG source documents as HIST assets per Rule 6 (AM-W4E3-002) | KB Operator | 2026-10-31 | Resolves Rule 6 blocker on W4-ERP-003 |
| 3.4 | Build compliance document register (TenderPack/Compliance/) with expiry tracking | KB Operator | 2026-10-31 | Tax Clearance (expires 2027-02-23), BEE (2026-07-31), CSD auto-remind |
| 3.5 | Pilot Wave 5 extraction (BU Lead authorisation required) — Acumatica Advanced Financial Reporting; OCI Managed Services (top candidates from WAVE4_CLOSURE_REPORT.md Section 4.3) | KB Operator | 2026-11-30 | Expands KB to cover gaps identified in GAP_ANALYSIS |
| 3.6 | Establish formal pre-tender checklist as a digital form (not manual checkbox) | BU Lead | 2026-10-31 | Auditability; removes human error from governance checking |
| 3.7 | Validate pipeline against 3 live tenders (one Oracle, one Acumatica, one mixed) | BU Lead + Consultants | 2026-12-31 | Quality assurance; refine prompts and recipes |

### Phase 3 Target State

```
INPUT: RFP document (parsed) + Tender Briefing Template
          ↓
Assembly Pipeline
  Step 1: Classify tender type (from RFP text or briefing)
  Step 2: Select applicable recipe from ANSWER_ASSEMBLY_FRAMEWORK
  Step 3: Pull KB assets by section
  Step 4: Generate AI draft (Claude with KB context)
  Step 5: Auto-scan governance rules → flag violations
  Step 6: Auto-check reference register → confirm reference status
  Step 7: Flag gaps for human authoring
          ↓
Human review: Gaps only (not full re-draft)
          ↓
BU Lead: Final governance sign-off + named reference approval
```

### Phase 3 Success Criteria
- Pipeline covers all 8 tender types from ANSWER_ASSEMBLY_FRAMEWORK.md
- Governance scan automated (20+ rules checked programmatically)
- Reference letter register integrated into pipeline
- Human authoring required for: CVs (by design) + project-specific content (pricing, project plan) + bespoke tender requirements
- Coverage for all tender types: **85%+** across the board
- Time from RFP receipt to BU Lead-ready draft: **≤ 2 hours**

---

## 6. Phase 4 — Near-Automated Response Factory (H1 2027)

**Goal:** The Tender Response Factory generates a complete, submission-ready draft (pending BU Lead approval) for standard tender types with minimal human intervention. Human effort concentrated at BU Lead review stage only.

### Enabling Actions (Phase 4)

| # | Action | Owner | Deadline | Impact |
|---|---|---|---|---|
| 4.1 | Complete Wave 5 + Wave 6 extraction (per WP5 recommendations) — target 55-60 total approved assets | KB Operator / BU Lead | 2027-03-31 | Coverage gaps closed |
| 4.2 | Implement RFP auto-parsing: extract tender requirements from PDF/DOCX into structured briefing automatically | Technical | 2027-03-31 | Eliminates manual briefing form entry |
| 4.3 | Integrate Consultant Index (ADR-001) into AI draft: AI selects appropriate consultant profiles from index and formats CV summary (without generating CV text) | Technical / APPTime | 2027-03-31 | Reduces CV sourcing to APPTime retrieval only |
| 4.4 | Implement compliance document auto-insertion: Tax Clearance, BEE, CSD auto-attached from TenderPack/Compliance register | Technical | 2027-03-31 | Eliminates compliance pack assembly |
| 4.5 | BU Lead review portal: AI-generated draft presented in structured review interface with governance flags inline; one-click approval flow | Technical / BU Lead | 2027-06-30 | Streamlines BU Lead approval |
| 4.6 | Post-submission learning loop: after each submitted tender, update KB with any bespoke content that proved reusable | KB Operator | Ongoing | KB improves with each tender |

### Phase 4 Target State

```
INPUT: RFP document (email attachment / file upload)
          ↓
Auto-Parser: extracts requirements → structured Tender Brief
          ↓
Response Factory:
  • Recipe selection (automatic)
  • KB asset retrieval (automatic)
  • AI draft generation (automatic)
  • Governance scan (automatic)
  • Reference check (automatic)
  • Compliance pack assembly (automatic)
  • Gap marking for bespoke content (automatic)
  • Consultant Index profile selection (AI-assisted)
          ↓
BU Lead Review Portal:
  • Full draft presented section-by-section
  • Governance flags inline
  • Named reference status inline
  • Human-authoring tasks highlighted
  • BU Lead: approve / reject / edit per section
          ↓
Final assembly → submission-ready tender pack
```

### Phase 4 Success Criteria
- **80%+ of narrative content** generated from approved KB for any tender type
- Human authoring required for: unique tender requirements, client-specific context, pricing/project plan (inherently bespoke)
- BU Lead review time: **≤ 1 hour** per tender (down from days currently)
- Zero governance violations in submitted tenders (automated scan catches all)
- KB grows automatically as each tender adds reusable content

---

## 7. Technology Stack Considerations

| Component | Phase 1 | Phase 2 | Phase 3 | Phase 4 |
|---|---|---|---|---|
| KB storage | OneDrive (Markdown files) | Same | Same | Same |
| AI assistant | Claude (manual prompting) | Claude Code project | Claude API integration | Claude API + workflow orchestration |
| Governance checking | Manual checklist | Prompt-based flagging | Programmatic rule engine | Automated pre-submission scan |
| Reference register | Manual lookup | Manual lookup | Integrated with pipeline | Auto-checked per client name |
| CV sourcing | APPTime (manual) | Consultant Index lookup | AI-assisted profile selection | Integrated APPTime API |
| Compliance pack | Manual file retrieval | Manual | Compliance register | Auto-assembled |
| Input | Manual briefing | Tender Briefing Template | Template + partial parsing | Full RFP auto-parsing |

**Critical architecture decision:** The KB remains authoritative and human-governed (BU Lead approves all content). The automation layer retrieves and assembles — it never generates capability claims or evidence that has not been approved. Rule: **Automation can only recombine approved content; it cannot create new claims.**

---

## 8. Quick-Win Actions (Start Immediately)

These actions are Phase 1 but deliver immediate impact regardless of automation maturity:

| # | Action | Effort | Days to Value |
|---|---|---|---|
| **Q1** | Register Oracle reference letters from SABS ETS corpus (already found — just registration) | Low | **1-2 days** |
| **Q2** | BEE certificate renewal | Medium | By 2026-07-31 |
| **Q3** | Apply assembly recipes to next live tender as a pilot | Low | Next tender received |
| **Q4** | Register Acumatica reference letters from AFROSAI-E corpus | Low | **1-2 days** |
| **Q5** | Authorise W5-ACU-001 Acumatica Support Model extraction (highest-impact content gap) | Medium (BU Lead decision) | 1 week from decision |

---

## 9. Roadmap Timeline Summary

| Quarter | Phase | Key Milestones | Target Coverage |
|---|---|---|---|
| **Q2-Q3 2026 (Now)** | Phase 1 | Structured manual assembly; reference letters registered; BEE renewed; recipes onboarded | Acumatica: 75%; Oracle: 85%; BeBanking: 95% |
| **Q3 2026** | Phase 2 | AI-assisted drafting active; Acumatica support model authored; platform-agnostic methodology in KB | Acumatica: 85%; Oracle: 90%; BeBanking: 95% |
| **Q4 2026** | Phase 3 | Semi-automated pipeline; governance scan automated; reference register integrated; Wave 5 extraction | All types: 85%+ |
| **H1 2027** | Phase 4 | Near-automated factory; BU Lead portal; RFP auto-parsing; post-submission learning | All types: 80%+ with minimal human drafting |

---

## 10. Governance Constraints on Automation (Non-Negotiable)

The following constraints apply regardless of automation level:

| Constraint | Applies to | Cannot be automated away |
|---|---|---|
| `approved_for_reuse: Yes` set only by BU Lead | All KB assets | Automation cannot promote candidate content |
| Named reference approval per tender (AM assets) | HB, ERP clients | BU Lead must confirm reference use at each submission |
| Rule 21.4 (DFA never named) | All outputs | Auto-scan must block; BU Lead cannot override |
| Rule 21.1 (SAA, aviation sector) | All outputs | Auto-scan must block |
| Section 14.2, 13.2 exclusions | W3S1-008, W3S1-009 | Auto-exclusion must be enforced; never appears in output |
| CV generation prohibition (ADR-001) | Consultant records | AI must never generate CV text from KB records |
| Evidence claims must match approved tier | All capability statements | AI cannot claim Tier 1 for Tier 2 evidence |
| BU Lead final sign-off | Every submission | Cannot be removed; only streamlined |

---

*TENDER_AUTOMATION_ROADMAP.md v1.0 — WP5 2026-06-14. Four phases: Structured Manual (now) → AI-Assisted Draft (Q3 2026) → Semi-Automated Pipeline (Q4 2026) → Near-Automated Factory (H1 2027). Target: 80%+ narrative coverage from approved KB.*
