---
created: "2026-06-12"
created_by: "Claude (AI — W2S1-005 pre-extraction readiness assessment)"
status: "Active — pre-extraction readiness report for W2S1-005"
deliverable: "W2S1-005-ORA-ImplementationMethodology"
---

# W2S1-005 Oracle Implementation Methodology — Pre-Extraction Readiness Report

**Date:** 2026-06-12 | **Owner:** Hein Blignaut | **Purpose:** Assess source completeness and extraction readiness before beginning W2S1-005 extraction.

---

## 1. Context

Wave 2 Oracle extraction is 4 of 5 complete. W2S1-001 (Fusion Capability), W2S1-002 (EBS Capability), W2S1-003 (DBA Executive Summary), and W2S1-004 (Managed Services Support Model) are all APPROVED. W2S1-005 Oracle Implementation Methodology is the final Wave 2 deliverable.

**Critical scope rule:** W2S1-005 covers the implementation delivery methodology from Mobilize through Hyper-care. It is NOT a managed services methodology. ITIL governance, CSI model, and steady-state support frameworks are already covered in W2S1-004 and must not be duplicated.

---

## 2. Primary Sources Reviewed

### 2.1 Hollywood Bets Accepted Proposal V5.0 (April 2023)

**File:** `Parties/Customers/Hollywood Bets/RFP/HCM and Payroll Implementation/Accepted proposal/APPSolve_HollywoodBets_Oracle Implementation 3rd part_V5.0.docx`

**Classification:** Tier 1 — Accepted/Won proposal. Confirmed in Accepted proposal folder.

**Scope:** Oracle Fusion HCM implementation with 3rd party payroll integration via OIC. 7 HCM modules: Core HCM/Self Service/Absence, Talent Management Base, Recruiting, Goal and Performance Management, Talent Review and Success Management, Career Development, plus OIC integration to 3rd party payroll.

**Methodology content confirmed:**

| Element | Confirmed | Source line |
|---|---|---|
| OUM basis | Yes | Line 66: "OUM Methodology" / Line 505: "Oracle Unified Methodology (OUM) will be adhered to" |
| Phase structure | Yes | Phase 0 Scoping → Phases 1–4 (HCM-module-centric) |
| Journey Prep (pre-workshop) | Yes | Lines 342–343 |
| Journey Workshop (design sessions) | Yes | Lines 344–348 |
| Solution Reflection — CRP1/CRP2 | Yes | Lines 346–349 — two rounds of guided + free reflection |
| Technical Build | Yes | Lines 350–352 |
| Integration Testing | Yes | Lines 353–354 |
| Training & UAT | Yes | Lines 355–358 |
| Data Management | Yes | Lines 359–360 |
| Production Build | Yes | Lines 363–364 |
| Hyper-care model | Yes | Lines 365–367 — 3 months full team; 6 months critical care; then steady state |
| OIC as integration layer | Yes | Line 58: "Integration to be done Utilising Oracle Integration Cloud Service" |
| Risk Management process | Yes | Lines 381–391 (centralised risk log, mitigation ownership, bi-weekly review) |
| Issue Management process | Yes | Lines 393–413 (issue log, PM-led triage, steering committee escalation path) |
| Change Control process | Yes | Lines 417–433 (formal change request, log, review, sign-off, tracking) |
| Configuration Management | Yes | Lines 435–441 (version control, deliverable integrity, release management) |
| Team roles | Yes | Lines 313–330 (PM, Principal, Senior Functional, Functional/Technical, Data Specialist, Senior Technical x2) |
| Training approach (Train the Trainer) | Yes | Line 507 |
| Documentation (OUM-based manuals) | Yes | Line 66 |
| Phased cost breakdown | Yes | Phase 0 = R417,100; Total = R6,925,150 (for context only — not for extraction) |

**Source quality:** HIGH. Accepted proposal with full methodology narrative. OUM explicitly confirmed. Hyper-care model is uniquely well-sourced here and not available elsewhere. Phase 0 "Scoping" naming differs from ORACLE_FACT_BASELINE Phase 0 "Mobilize" — use BASELINE naming in W2S1-005.

**Prohibited wording to avoid from this source:**
- None in the methodology sections. Company claims are not prominently made in the methodology body. No prohibited headcount, year, or partner tier claims present in the content extracted.

**KPMG reference:** Line 335 — "most recently at KPMG" used as a similar-rollout reference. KPMG citability is classified as "source evidence only" per W2S1-002 BU-EBS-002 decision. Do not use KPMG as a referenceable client in W2S1-005. May be referenced obliquely as "prior similar multi-country EBS rollout experience" only if no referenceable name is required.

---

### 2.2 RedPath Mining RFI Reply (March 2026)

**File:** `Parties/Customers/RedPath Mining/Working/RedPath Mining_APPSolve_RFI Reply Detail.docx`

**Classification:** Tier 1 — Recent RFI response (March 2026) with full methodology narrative.

**Scope:** Oracle Fusion Cloud implementation (HCM + Finance + SCM/Procurement + Projects) for RedPath Mining (South Africa). This is the most recent methodology document in the source corpus.

**Methodology content confirmed:**

| Element | Confirmed | Source line |
|---|---|---|
| OUM + Customer Success Navigator basis | Yes | Line 158: "based on Oracle's OUM and current Customer Success Navigator stages" |
| Iterative approach to CRP2 | Yes | Line 158: "embedded and iterative approach...to full solution in Prototype 2 (CRP2)" |
| Phase 0 — Mobilize (team, charter, work plan, kick-off) | Yes | Lines 161–169 |
| Phase 1 — Scoping (scope confirmation, Oracle Modern Best Practices, data requirements, workshop prep) | Yes | Lines 170–176 |
| Phase 2 — Prototype (design workshops, CRP1, CRP2, end-to-end testing) | Yes | Lines 177–200 |
| Design governance (solution authority, executive sponsors) | Yes | Lines 179–187 |
| CRP1 — Prototype 1 build and validation | Yes | Lines 190–193 |
| CRP2 — Prototype 2 build and validation | Yes | Lines 196–199 |
| End-to-end SIT | Yes | Lines 200–201 |
| Phase 3 — Validate (final validation, documentation handover, go-live prep) | Yes | Lines 204–212 |
| Phase 4 — Deploy (production build, user enablement, training, go-live) | Yes | Lines 213–221 |
| Phase 5 — Evolve (adoption monitoring, continued support) | Yes | Lines 222–226 |
| OIC as standard in all Fusion implementations | Yes | Line 109: "All our Fusion implementation we have also implemented Oracle Integration Cloud" |
| FBDI data migration | Yes | Line 111: "Oracle's standard APIs and FBDI sheets" |
| Financial data reconciliation to Trial Balance | Yes | Line 112: "always reconciled back to control accounts in the Trial Balances" |
| Project governance (fit into client structure) | Yes | Lines 227–228 |
| Change management capability | Yes | Line 229 |
| Training (Train the Trainer + End User) | Yes | Lines 231–232 |
| Program Manager capability | Yes | Line 233 |
| Resource stability | Yes | Lines 243–244 |

**Source quality:** VERY HIGH. Most current (March 2026) and most structurally aligned with ORACLE_FACT_BASELINE.md Section 17. Phase naming (Mobilize/Scoping/Prototype/Deploy/Evolve) matches the BASELINE naming exactly — use RedPath Mining as the structural backbone for W2S1-005.

**Prohibited wording found — must not be extracted:**

| Prohibited claim | Source line | Rule | Use instead |
|---|---|---|---|
| "over the last 22 years" | 33 | BASELINE: "over 23 years" | "over 23 years" |
| "more than 110 Senior Consultants" | 39 | BASELINE: "50+ Senior Consultants" | "50+ Senior Consultants" |
| "Nala...across all 8 countries" | 151 | BASELINE Section 19: 4 countries, not 8 | Omit or use "4 countries" |
| "DFA (Dark Fibre Africa)" in client list | 124–129 | FR-D: internal-use only | Omit entirely |
| "APPSolve is an Oracle Partner" | 40 | Must use "Oracle Level 1 Partner" | "Oracle Level 1 Partner" |
| "2 awards as APPS/SAAS Partner Business Impact award in two regions EMEA and ECEMEA" | 34 | Not in approved W1S1-006 awards table — verify before citing | Do not include in W2S1-005 unless BU-confirmed |

---

### 2.3 SAA RFP Response Section 5 (June 2025)

**Status:** Identified as supplementary source in ORACLE_WAVE2_EXECUTION_PLAN.md. Not yet read.

**Assessment:** Not required for GO decision. Both Tier 1 sources (HB V5.0 + RedPath Mining) provide complete methodology coverage. SAA Section 5 can optionally be read during extraction for phrasing verification but is not a readiness gate.

---

## 3. Coverage Assessment — W2S1-005 Document Sections

Mapping confirmed source content to the ORACLE_WAVE2_EXECUTION_PLAN.md Deliverable 5 recommended structure:

| Section | Coverage | Primary Source | Confidence |
|---|---|---|---|
| 1. Methodology Overview (OUM + CSN basis) | FULL | RedPath Mining line 158 + HB V5.0 lines 66, 505 | HIGH |
| 2a. Phase 0 — Mobilize (charter, work plan, kick-off) | FULL | RedPath Mining lines 161–169 | HIGH |
| 2b. Phase 1 — Scoping (scope, best practices, data, workshop prep) | FULL | RedPath Mining lines 170–176 | HIGH |
| 2c. Phase 2 — Prototype (design workshops, CRP1/CRP2, change control) | FULL | RedPath Mining lines 177–199 + HB V5.0 Solution Reflection sections | HIGH |
| 2d. Phase 3 — Build (config, integration, data migration) | PARTIAL | HB V5.0 Technical Build + RedPath Mining FBDI (line 111) | MEDIUM |
| 2e. Phase 4 — Deploy (production build, training, UAT, go-live) | FULL | RedPath Mining lines 213–221 + HB V5.0 lines 363–364 | HIGH |
| 3. Project Infrastructure (Risk/Issue/Change/Config) | FULL | HB V5.0 lines 381–441 (most detailed source) | HIGH |
| 4. Data Migration (FBDI, APIs, reconciliation) | FULL | RedPath Mining lines 111–113 | HIGH |
| 5. Post Go-Live Support (hyper-care 3m, critical care 6m, steady state) | FULL | HB V5.0 lines 365–367 | HIGH |

**Gap note on Phase 3 — Build:** HB V5.0 Technical Build section (lines 350–352) is brief and primarily describes OIC/integration exclusion from the technical build phase (integration is tested separately). The configuration build description is thin. RedPath Mining's Prototype 2 build (lines 196–199) covers configuration + integration + data migration together. Combined, both sources provide adequate Build phase content. This is a minor gap — LOW risk for extraction.

---

## 4. Scope Boundary: W2S1-005 vs W2S1-004

The following content is W2S1-004 territory and must NOT appear in W2S1-005:

| Content | Belongs in | Status |
|---|---|---|
| ITIL service management framework | W2S1-004 | APPROVED — do not duplicate |
| CSI (Continual Service Improvement) model | W2S1-004 | APPROVED — do not duplicate |
| P1/P2/P3/P4 SLA tiers (post-implementation) | W2S1-004 | APPROVED — do not duplicate |
| Monthly/quarterly governance review cadence | W2S1-004 | APPROVED — do not duplicate |
| CMDB governance | W2S1-004 | APPROVED — do not duplicate |
| Segregation of duties framework | W2S1-004 | APPROVED — do not duplicate |

**Hyper-care is IN SCOPE for W2S1-005** — it is the final phase of implementation delivery, not a managed services function. The handover from hyper-care to W2S1-004 steady-state support should be referenced at the end of W2S1-005's post go-live section.

---

## 5. Governance Constraints for Extraction

The following rules apply during extraction. These are not reminders — they are gates.

| Rule | Application to W2S1-005 |
|---|---|
| Use "Oracle Level 1 Partner" only | If partnership tier is cited in methodology overview, use approved wording only |
| BEE Level 3 (RS-19451, expires 2026-07-31) | W2S1-005 is a methodology document — BEE claim unlikely to appear; if it does, Level 3 only |
| Do not cite DFA externally | RedPath Mining source contains DFA in client list (line 124); do not extract |
| SARB requires separate BU approval | SARB unlikely in methodology context; omit if it arises |
| "50+ Senior Consultants" only | If resource depth is cited in methodology overview |
| "over 23 years" | If company tenure is cited |
| OIC = standard in all Fusion implementations | Confirmed by RedPath Mining line 109 — state this as a matter of fact in the methodology |
| FBDI = standard data migration tool | Confirmed by RedPath Mining line 111 |
| Distinguish implemented from supported footprint | Any client references in methodology context should reference delivered implementations |
| Do not duplicate W2S1-004 ITIL content | Confirmed boundary above |
| No new claims outside evidence base | All methodology phase descriptions must trace to HB V5.0 or RedPath Mining RFI |
| approved_for_reuse: Yes only by BU Lead | Do not set this at extraction time |

---

## 6. Extraction Assumptions (Pre-Confirmed)

All extraction assumptions are confirmed. No blockers.

| Assumption | Status | Source |
|---|---|---|
| OUM is confirmed as APPSolve's methodology basis | CONFIRMED | HB V5.0 line 505; RedPath Mining line 158 |
| Phase structure aligns with ORACLE_FACT_BASELINE Section 17 | CONFIRMED | RedPath Mining phase naming matches exactly |
| OIC is standard in all Fusion implementations | CONFIRMED | RedPath Mining line 109 |
| FBDI is the standard data migration approach | CONFIRMED | RedPath Mining lines 111–112 |
| Hyper-care model has specific timelines | CONFIRMED | HB V5.0 lines 365–367 (3m full team + 6m critical care) |
| Project governance processes are documented | CONFIRMED | HB V5.0 lines 381–441 |
| W2S1-005 is Fusion-centric but OUM applies to EBS too | CONFIRMED | OUM applicability confirmed across both platforms |

---

## 7. Recommended Document Structure for Extraction

```
W2S1-005-ORA-ImplementationMethodology
KB Destination: 05_Methodologies/Implementation/

Frontmatter:
  source_status: Candidate_Content
  reviewed_by: (blank until BU review)
  sources: Hollywood Bets V5.0 (April 2023); RedPath Mining RFI Reply (March 2026)

1. Methodology Overview
   - APPSolve's OUM-based implementation framework
   - Oracle UIM/OUM + Customer Success Navigator alignment
   - Iterative approach: prototype-to-production in two CRP cycles
   - OIC as standard integration layer (all Fusion implementations)

2. Implementation Phases

   2.1 Phase 0 — Mobilize
       - Team assembly and scheduling
       - Initiative charter (vision, drivers, scope, success criteria, budget)
       - Work plan definition
       - Kick-off (with confirmed executive sponsor attendance)

   2.2 Phase 1 — Scoping
       - Scope confirmation and Oracle Modern Best Practices alignment
       - Starter Configurator walkthrough
       - Data assessment and template provision
       - Design workshop scheduling and environment preparation

   2.3 Phase 2 — Prototype (CRP1 / CRP2)
       - Design governance model (solution authority, executive sponsors, change control)
       - High-level design workshops (Prototype 0 / Starter Configuration)
       - Prototype 1 (CRP1): functional config, reports, integrations, converted data
       - Playback and validation sessions (guided then self-directed)
       - Detailed design workshops
       - Prototype 2 (CRP2): refined config, extensions, migrated data
       - End-to-end system integration test (SIT)

   2.4 Phase 3 — Build
       - Configuration finalisation from CRP2 outcomes
       - OIC integration build (inbound/outbound interfaces)
       - Oracle FBDI data migration (customer-led with APPSolve guidance)
       - Financial data reconciliation to Trial Balance control accounts
       - Custom reports and workflows

   2.5 Phase 4 — Deploy
       - Production build (configuration, extensions, security controls)
       - User enablement and training (Train the Trainer)
       - UAT facilitation
       - Cutover planning (roles, timelines, contingencies)
       - Go-live

   2.6 Post Go-Live — Hyper-care
       - Hyper-care (~3 months): full senior team available for defects, design adjustments
       - Critical care (~6 months): reduced team, senior-led, managing adoption
       - Steady state: transition to W2S1-004 managed services support model

3. Project Infrastructure
   - Risk management: centralised risk log, bi-weekly review, steering committee escalation
   - Issue management: issue log, PM triage, change request process for scope/budget/schedule impact
   - Change control: formal request, log, review, sign-off, tracking
   - Configuration management: version control, deliverable integrity, environment management

4. Data Migration Approach
   - Oracle standard APIs and FBDI as primary migration tools
   - Financial transactional data reconciled to Trial Balance before loading
   - Customer-led data preparation with APPSolve guidance
   - Data sign-off: customer accountable for accuracy; APPSolve accountable for delivery to correct location

5. Team Model and Roles
   - Roles: Project Manager, Principal Consultant (Design Authority), Senior Functional Consultant,
     Functional/Technical Consultant, Data Specialist, Senior Technical Resource (reports/workflows),
     Integration Technical Resource (OIC)
   - 50+ Senior Consultants practice depth
   - Resource stability: experienced team assigned for full project duration

6. Pre-Tender Checks (at extraction time)
   - FR-W5-001: OPN certificate verification (FR-EBS-012 cross-reference)
   - Verify award claims before citing in any tender where not currently in approved W1S1-003 or W1S1-006
```

---

## 8. Open Items (Not Extraction Blockers)

| Item | Action Required | Urgency |
|---|---|---|
| SAA Section 5 methodology language | Optionally read during extraction for phrasing refinement | Low |
| KPMG as methodology reference | Cannot cite as referenceable client; note source evidence only | Pre-tender |
| Awards claims (APPS/SAAS Partner Business Impact) | Confirm with BU before including in W2S1-005 | BU review gate |

---

## 9. GO / NO-GO Decision

**GO — EXTRACTION APPROVED.**

**Basis for GO:**

1. Both Tier 1 sources confirmed and fully read:
   - Hollywood Bets V5.0 (Accepted Proposal, April 2023) — Tier 1
   - RedPath Mining RFI Reply (March 2026) — Tier 1

2. Full phase structure is evidenced and traceable:
   - Mobilize through Hyper-care confirmed across both sources
   - Phase naming aligns with ORACLE_FACT_BASELINE.md Section 17

3. All five planned W2S1-005 document sections have sufficient source material:
   - Methodology Overview: both sources confirm OUM basis
   - Implementation Phases: RedPath Mining provides structural backbone; HB V5.0 supplements
   - Project Infrastructure: HB V5.0 provides the most detailed governance process descriptions
   - Data Migration: RedPath Mining provides the FBDI + reconciliation framework
   - Hyper-care model: HB V5.0 provides specific 3-month / 6-month timeline evidence

4. Scope boundary with W2S1-004 is clear — no duplication risk identified.

5. All governance constraints are documented and manageable:
   - Prohibited wording from RedPath Mining identified and flagged
   - DFA exclusion confirmed
   - Approved company facts available for substitution

6. No unresolved extraction assumptions. No new claims required outside the evidence base.

**Extraction may begin immediately.** Produce `W2S1-005-ORA-ImplementationMethodology` as a CANDIDATE file, then promote to Review_Required upon self-review completion.

---

*Prepared 2026-06-12 by Claude (AI) — readiness assessment only. No extraction work performed. Extraction authorised upon BU Lead review of this report or explicit instruction to proceed.*
