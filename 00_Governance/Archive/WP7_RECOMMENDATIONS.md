# WP7 Recommendations — Minimum Additions for 80% and 90% Automation
**Work Package:** WP6 — Tender Simulation & Coverage Assessment | **Version:** 1.0 | **Created:** 2026-06-14
**Purpose:** Define the smallest set of additions required to move the KB from the current 68% automation readiness score to 80% and then to 90%.
**Constraint:** Do not recommend capability extraction unless it directly improves tender coverage.

---

## Guiding Principle

WP7 should contain only actions that directly close tender coverage gaps identified in the WP6 simulation. No speculative extraction, no nice-to-have content, no governance projects that do not improve tender coverage.

**Every recommendation below maps to a specific gap in GAP_REGISTER.md and a specific coverage deficit in TENDER_COVERAGE_REPORT.md.**

---

## Current State

| Metric | Value |
|---|---|
| Automation Readiness Score | 68/100 |
| AFROSAI-E narrative coverage | 56% |
| Oracle HCM coverage | ~85% |
| Oracle EBS/DBA coverage | ~90% |
| BeBanking coverage | ~95% |
| Open content gaps | 8 (GAP-001 through GAP-008) |
| Reference letters in 04_References/ | 0 registered |

---

## Path to 80% Automation Readiness

**4 actions. No new Wave of extraction required. Achievable in 2-4 weeks.**

### Action 1 — Register Oracle ERP Reference Letters
**Closes:** GAP-004 | **Gaps in KB:** AM-W4E1-001, AM-W4E2-001 (partial), AM-W4E3-001
**Dimension improved:** Reference Coverage (+5 pts), Content Coverage (+2 pts)

**What to do:**
1. BU Lead reviews the following letters (all physically present in SABS ETS corpus at `Parties/Customers/SABS/RFP/ETS - Oracle Fusion/References/`):
   - Investec Reference Letter 2023-09
   - NALA Reference Letter Appsolve
   - Cape Union Mart Reference Letter (confirm scope = Oracle Finance/Procurement)
   - Assore Reference Letter
   - Adcock Ingram Reference Letter
   - Mr Price Reference Letter (scope = Learning Cloud)
2. BU Lead confirms each is signed and approves registration
3. KB Operator copies to `04_References/Oracle/` and registers in DOCUMENT_REGISTER.csv
4. KB Operator removes AM-W4E1-001 restriction from W4-ERP-001, W4-ERP-002 once letters confirmed
5. Cape Union Mart scope must be confirmed before AM-W4E2-001 is removed

**Effort:** 2-3 hours total (KB Operator) + BU Lead review session
**Timeline:** Can be completed in 1 day
**Note:** DFA Reference Letter.pdf is in the same folder. It must NOT be registered. Rule 21.4 is permanent.

---

### Action 2 — Register Acumatica Reference Letters
**Closes:** GAP-003 | **Gaps in KB:** Acumatica reference set (1 registered client → 4)
**Dimension improved:** Reference Coverage (+3 pts), Content Coverage (+1 pt)

**What to do:**
1. BU Lead confirms the following letters from AFROSAI-E corpus are signed:
   - DSSSA Reference Letter
   - FuelU2 Reference Letter
   - Maxiflex Reference Letter
   - ATS Acumatica Partner Letter (register in `04_References/Acumatica/Partners/`)
2. KB Operator registers in `04_References/Acumatica/`
3. Update DOCUMENT_REGISTER.csv

**Effort:** 1-2 hours
**Timeline:** 1 day (parallel with Action 1)

---

### Action 3 — De-brand W2S1-005 into a Platform-Agnostic Methodology Statement
**Closes:** GAP-002 | **Gaps in KB:** Methodology B-class on all Acumatica tenders
**Dimension improved:** Content Coverage (+4 pts), Automation Readiness (+2 pts)

**What to do:**
This is not a new extraction. It is an adaptation of the already-approved W2S1-005.

1. Create `W5-METH-001-ERP-ImplementationMethodology.md` (new file)
2. Source content: W2S1-005 (approved 2026-06-12) as the base
3. Replace Oracle-specific terms:
   - "Oracle Unified Method (OUM)" → "APPSolve Delivery Framework"
   - "Oracle Customer Success Navigator" → "APPSolve Client Success Programme"
   - "Oracle FBDI" → "ERP data import tools"
   - "Oracle Guided Learning" → "system training tools"
   - "Oracle Modern Best Practices" → "ERP Modern Best Practices"
   - Oracle-specific tool references → generic equivalents
4. Add Acumatica-specific subsection (Phase 3 Build): Acumatica Import Scenarios; Acumatica configuration approach; Acumatica University training integration
5. BU Lead review and approval
6. Mark W2S1-005 as "Oracle-specific — use W5-METH-001 for non-Oracle tenders"

**Effort:** 3-4 hours (KB Operator) + BU Lead review (30 min)
**Timeline:** 1 week
**Result:** Methodology section in Acumatica tenders upgrades from B (2-3 hours de-branding per tender) to A (< 15 min with contextualisation). Saves ~2-3 hours per Acumatica tender going forward.

---

### Action 4 — Author Acumatica Support & Managed Services Capability Statement
**Closes:** GAP-001 | **Gaps in KB:** Section 6 support (0% coverage on all Acumatica tenders)
**Dimension improved:** Content Coverage (+8 pts), Automation Readiness (+6 pts)
**Designation:** W5-ACU-001

**What to do:**
1. BU Lead authorises Wave 5 extraction for W5-ACU-001
2. KB Operator drafts from confirmed evidence — sources to use:
   - APPSolve's Acumatica support relationships (Interconnect, HyDac, DSSSA, FuelU2, Maxiflex — verify current support status)
   - W2S1-004 (Oracle Managed Services model) as structural template — do NOT reuse Oracle-specific content
   - W1S1-009 (Hybrid Support Model) as introduction
3. Content to cover:
   - Tier model (Respond, Retain, Evolve — or similar 3-tier)
   - Response time commitments per severity tier (P1/P2/P3/P4)
   - Help desk process (log → triage → resolve)
   - Escalation path (APPSolve → Acumatica Global Support)
   - Hypercare-to-steady-state transition
   - Support evidence: reference to Interconnect and HyDac as active support clients (pre-tender checks required)
4. BU Lead reviews and approves

**Effort:** 1 day (KB Operator draft) + BU Lead review session
**Timeline:** 1-2 weeks (BU Lead authorisation is the dependency)
**Result:** Acumatica support section upgrades from C-GAP (2-3 hours authoring per tender) to A (< 15 min). This single action saves the most time per tender.

---

### 80% Target — Actions Summary

| # | Action | Effort | Timeline | Score gain |
|---|---|---|---|---|
| 1 | Register Oracle ERP reference letters | 2-3 hrs | Day 1 | +7 pts |
| 2 | Register Acumatica reference letters | 1-2 hrs | Day 1 | +4 pts |
| 3 | De-brand W2S1-005 → platform-agnostic | 4-5 hrs | Week 1 | +6 pts |
| 4 | Author W5-ACU-001 Acumatica support model | 1-2 days | Week 2 | +8 pts |
| | **TOTAL** | | **~2 weeks** | **+25 pts → Score: 80** |

**After completing these 4 actions:**
- AFROSAI-E Acumatica coverage: 56% → **82%**
- Oracle ERP coverage: 75% → **88%** (named references unlocked)
- Overall automation readiness: 68 → **80**

---

## Path to 90% Automation Readiness

**7 additional actions. Requires Phase 2 of TENDER_AUTOMATION_ROADMAP. Timeline: Q3 2026.**

### Action 5 — Build AI Prompt Library
**Closes:** Automation Readiness gap | **Automation Readiness: +12 pts**

**What to do:**
1. For each of the 13 question categories in TENDER_QUESTION_TAXONOMY.md (Sections A–M), create a structured prompt that:
   - Specifies which KB assets to retrieve
   - Provides assembly instructions
   - Includes governance flags inline
   - Flags gaps for human authoring
2. Test each prompt against a live tender section before finalising
3. Store prompts in `00_Governance/Prompts/` (or equivalent)

**Effort:** 2-3 days | **Owner:** KB Operator + BU Lead validation

---

### Action 6 — Author Acumatica Security and Data Governance Statement
**Closes:** GAP-005 | **Content Coverage: +2 pts**
**Designation:** W5-ACU-002

**What to do:**
1. BU Lead authorises W5-ACU-002
2. Source content primarily from Acumatica's public documentation (SOC 2 Type II certification, AWS/Azure hosting, RBAC documentation, POPIA compliance posture)
3. Add APPSolve-specific access control approach (role design, user provisioning, access review)
4. BU Lead review and approval

**Effort:** 3-4 hours | **Note:** This is the lowest-effort new capability statement in the gap list because most content comes from Acumatica's own published documentation.

---

### Action 7 — Author Platform-Agnostic Change Management / OCM Statement
**Closes:** GAP-006 | **Content Coverage: +1 pt**
**Designation:** W5-OCM-001

**What to do:**
1. Extract OCM content from W2S1-005 Deploy phase
2. Add adoption measurement framework (what to measure; how; over what period)
3. Make platform-agnostic (remove Oracle-specific tools)
4. BU Lead review and approval

**Effort:** 2-3 hours

---

### Action 8 — Author Acumatica Cloud Hosting / SaaS Model Statement
**Closes:** GAP-007 | **Content Coverage: +1 pt**
**Designation:** W5-ACU-003

**What to do:**
1. Describe Acumatica's true-cloud SaaS model (from Acumatica public documentation)
2. Cover: AWS/Azure hosting, 99.5%+ uptime SLA, no on-premise hardware, automatic upgrades, data backup, DR, subscription licensing
3. Add APPSolve's role in cloud implementation (cloud configuration vs. infrastructure)
4. BU Lead review and approval

**Effort:** 2-3 hours

---

### Action 9 — Implement Tender Briefing Template
**Closes:** Process gap (no structured AI input) | **Automation Readiness: +5 pts**

**What to do:**
Create a standard intake form for every new tender:
- Tender name and reference number
- Client name and sector
- Tender type (Oracle HCM / Oracle ERP / Acumatica / BeBanking / Mixed)
- Modules required
- Named references permitted (Y/N; which clients)
- Geography and multi-currency requirements
- Compliance documents required
- Submission deadline
- AI assembly recipe to use

**Format:** Markdown template stored in `00_Governance/Templates/Tender_Briefing_Template.md`
**Effort:** 2 hours

---

### Action 10 — Register BeBanking Reference Letters
**Closes:** Reference Coverage gap for BeBanking | **Reference Coverage: +2 pts**

**What to do:**
1. Identify formal signed reference letters for SITA (H2H BeBanking) and HyDac (BeBanking ERP integration)
2. Register in `04_References/BeBanking/`
3. Update capability statements to reference formally

**Effort:** 1-2 hours

---

### Action 11 — Wave 5 Selective Extraction (BU Lead authorisation required)
**Closes:** Targeted content gaps | **Content Coverage: +1 pt, Evidence Quality: +1 pt**

**Recommended Wave 5 candidates (priority order, minimum set for 90% target):**

| Asset ID | Title | Rationale | Evidence source |
|---|---|---|---|
| W5-ACU-001 | Acumatica Support Model | Already in 80% plan — critical | Interconnect/HyDac support relationships |
| W5-METH-001 | Platform-Agnostic Methodology | Already in 80% plan — adaptation | W2S1-005 de-brand |
| W5-ACU-002 | Acumatica Security | GAP-005 — public sector requirement | Acumatica SOC 2 documentation |
| W5-ACU-003 | Acumatica Cloud Hosting | GAP-007 — routine question | Acumatica public documentation |
| W5-OCM-001 | Change Management (generic) | GAP-006 — recurring ask | W2S1-005 extract + expand |

**Excluded from Wave 5 minimum set:** OCI capability statement, Oracle Field Service, Acumatica Advanced Financial Reporting, Consultant Index Programme. These improve coverage but are not required for 90% target.

---

### 90% Target — Full Actions Summary

| # | Action | Effort | Timeline | Score gain |
|---|---|---|---|---|
| 1-4 | 80% target actions (above) | ~2 weeks | Weeks 1-2 | +12 pts |
| 5 | Build AI prompt library | 2-3 days | Week 3-4 | +12 pts |
| 6 | W5-ACU-002 Acumatica Security | 3-4 hrs | Week 3 | +2 pts |
| 7 | W5-OCM-001 Change Management | 2-3 hrs | Week 4 | +1 pt |
| 8 | W5-ACU-003 Acumatica Cloud Hosting | 2-3 hrs | Week 4 | +1 pt |
| 9 | Tender Briefing Template | 2 hrs | Week 3 | +3 pts |
| 10 | BeBanking reference letters | 1-2 hrs | Week 3 | +2 pts |
| 11 | Wave 5 selective extraction | 2-3 days | Weeks 4-6 | +1 pt |
| | **TOTAL** | | **~6 weeks** | **+34 pts → Score: 90** |

---

## WP7 Scope Boundary

The following are explicitly excluded from WP7 because they do not directly improve tender coverage:

| Excluded item | Reason |
|---|---|
| Oracle HCM Wave 5 extraction (ORC analytics, advanced talent) | Oracle HCM already at 85%; improvement is marginal |
| OCI capability statement | No OCI tenders in recent pipeline |
| Oracle Field Service | No confirmed APPSolve OFS delivery evidence |
| KPMG full evidence registration | AM-W4E3-001 is a reference-letter issue, not a content gap |
| Consultant Index Programme | ADR-001 architecture — APPTime, not KB |
| Compliance document register | Governance improvement, not coverage improvement |
| Automated governance scan | Phase 3 TENDER_AUTOMATION_ROADMAP — not WP7 |
| RFP auto-parsing | Phase 4 TENDER_AUTOMATION_ROADMAP — not WP7 |

---

## Decision Required from BU Lead

To proceed with WP7:

| # | Decision | Required for |
|---|---|---|
| **D1** | Authorise registration of Oracle ERP letters (Investec, NALA, CUM, Assore, Adcock, Mr Price) | 80% target |
| **D2** | Confirm Cape Union Mart scope = Oracle Finance/Procurement (not Acumatica/PaySpace) | 80% target |
| **D3** | Authorise W5-ACU-001 Acumatica Support Model extraction | 80% target |
| **D4** | Authorise W5-METH-001 methodology de-brand (no new extraction — adaptation of W2S1-005) | 80% target |
| **D5** | Confirm Acumatica reference letters (DSSSA, FuelU2, Maxiflex) signed — authorise registration | 80% target |
| **D6** | Authorise W5-ACU-002 (Security), W5-ACU-003 (Cloud), W5-OCM-001 (OCM) | 90% target |

---

*WP7_RECOMMENDATIONS.md v1.0 — WP6 2026-06-14. 4 actions to reach 80% (2 weeks). 11 actions total to reach 90% (6 weeks). All actions directly derived from AFROSAI-E pilot coverage gaps. No speculative extraction recommended.*
