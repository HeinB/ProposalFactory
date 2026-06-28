---
created: "2026-06-10"
updated: "2026-06-11"
created_by: "Claude (AI — Wave 2 content strategy planning)"
updated_by: "Claude (AI — W2S1-001 promoted to Review_Required 2026-06-11 by Hein Blignaut; Nala scope confirmed; A-003 closed; FR-004 resolved Option A)"
status: "ALL APPROVED — Oracle Wave 2 COMPLETE. W2S1-001 APPROVED (2026-06-11); W2S1-002 APPROVED (2026-06-12); W2S1-003 APPROVED (2026-06-11); W2S1-004 APPROVED (2026-06-11); W2S1-005 APPROVED (2026-06-12). Total Oracle approved: 5. Total KB approved: 30."
---

# Oracle Wave 2 Execution Plan
**Date:** 2026-06-10 (updated same day) | **Owner:** Hein Blignaut | **Purpose:** Content strategy for five Oracle Wave 2 deliverables

This document defines the target audience, tender usage, document structure, extraction vs. synthesis breakdown, approval risk, and effort for each Oracle Wave 2 document. Updated to incorporate BU-confirmed sources (Hollywood Bets, SAA, RedPath Mining). No extraction has been performed.

---

## Source Role Summary

Three source tiers now apply to Oracle Wave 2:

| Source tier | Role | Documents |
|---|---|---|
| **Primary templates** | Primary extraction source — structural authority | TMPL-001 (Fusion), TMPL-002 (EBS) |
| **Real-world validation** | Confirm capability language, methodology, client examples | SAA RFP (June 2025), Hollywood Bets accepted proposal (2023), RedPath Mining RFI (March 2026) |
| **Historical methodology** | DBA/managed services depth; SLA/governance framework | HIST-002 MTN (2014), ATNS EBS Support (2025) |

**Extraction rule:** Extract from primary templates. Use real-world validation sources to verify claim accuracy, confirm current terminology, and supply implementation methodology detail that templates do not contain. Use historical sources for DBA and managed services depth only.

---

## Overview

Five Oracle documents are planned for Wave 2:

| # | Deliverable | Primary source | Validation source | Priority | Effort |
|---|---|---|---|---|---|
| 1 | Oracle Fusion Capability Statement | TMPL-001 | SAA RFP Section 2; RedPath Mining RFI | **Critical** | **APPROVED 2026-06-11** |
| 2 | Oracle EBS Capability Statement | TMPL-002 + ATNS 2025 + KPMG SADC + ARM + Assore + EBS Customer List + ARM-2025-IT045 | Multiple — 8 sources | High | **APPROVED 2026-06-12** |
| 3 | Oracle DBA Executive Summary | MTN 2026 DBA RFP (RFX-1000004246) — PRIMARY; HIST-002 superseded | W1S1-003, W1S1-007 | High | **CANDIDATE created 2026-06-11** |
| 4 | Oracle Managed Services / Support Model | MTN 2026 DBA RFP (RFX-1000004246) — PRIMARY; ATNS EBS 2025 superseded | W2S1-003 (approved 2026-06-11); W1S1-003, W1S1-007 | High | **APPROVED 2026-06-11** |
| 5 | Oracle Implementation Methodology | Hollywood Bets accepted proposal; RedPath Mining RFI | SAA RFP Section 5 | Medium | **APPROVED 2026-06-12** |

**Note on expanded scope vs. original three-document plan:** Deliverables 4 and 5 are added because the new sources contain rich managed services/support and methodology content not available in the templates. Total Wave 2 effort estimate: 5–7 hours extraction + BU lead review sessions.

---

## Deliverable 1: Oracle Fusion Capability Statement

### Target Audience

Procurement evaluators, IT directors, and ERP selection committees at organisations issuing Oracle Cloud / Oracle Fusion RFPs. Common tender profiles: cloud ERP implementations, Fusion Finance or HCM migrations, Oracle OCI-hosted solutions, post-EBS-upgrade cloud transitions.

### Intended Tender Usage

| Usage context | How this document is used |
|---|---|
| Oracle Cloud implementation tender | Section 3–5 of standard RFP response — "Vendor Capability and Experience" |
| Oracle Fusion Finance / HCM RFP | Module-level capability section directly addressing evaluator questions |
| Post-EBS modernisation | Establishes APPSolve's Cloud capability as a complement to EBS history |
| Capability overview quote | First-page or one-page summary of Oracle Cloud service offering |
| Combined Oracle + Cloud + Infrastructure tender | Oracle Cloud section of multi-section response |

### Recommended Document Structure

```
1. Oracle Fusion Overview
   - APPSolve positioning as Oracle Cloud implementer
   - Partner context: Oracle Level 1 Partner; Cloud Excellence Implementer designation

2. Oracle Fusion Capability Matrix
   - Functional areas: Financial Management; HCM; SCM; CRM/Sales; Procurement; GRC
   - For each area: brief description, APPSolve delivery experience note, key modules listed

3. Oracle Integration Cloud (OIC)
   - Integration capability statement
   - Common integration patterns (ERP-to-third-party; legacy EBS-to-Cloud migration)

4. Cloud Infrastructure and Deployment
   - OCI deployment capability
   - On-premises to cloud migration approach
   - APPSolve-managed vs client-managed cloud

5. Oracle Fusion Implementation Methodology (reference only)
   - Point to W1S1-007 (Delivery Model) for methodology detail
   - Note: full methodology is a Wave 3 item; this section is a bridging reference

6. Oracle Fusion Reference Projects (when references are approved)
   - Placeholder section — currently no approved Oracle Fusion reference content
   - List structure for future population
```

### Sections: Extractable vs Requiring Synthesis

| Section | Primary source | Validation source | Approach |
|---|---|---|---|
| Fusion Overview | TMPL-001 "Oracle Fusion Information" | SAA Section 2 intro | Extract from TMPL-001; cross-check currency with SAA (June 2025) |
| Fusion Core Components Table | TMPL-001 component table | SAA core components table | Extract from TMPL-001; SAA has near-identical table — use to confirm wording |
| Oracle Fusion HCM detail | TMPL-001 | SAA Section 2 HCM modules (15+ modules, each with Overview/Benefits/Capabilities) | SAA is RICHER — extract Fusion HCM from SAA; use TMPL-001 as structural guide |
| OIC section | TMPL-001 | RedPath Mining RFI: "All Fusion implementations used OIC for all inbound and outbound interfaces" | Extract — OIC is confirmed standard; include as mandatory integration layer |
| Cloud deployment / OCI | TMPL-001 | OCI SOC 1 and SOC 2 Bridge Letters (available for supporting docs) | Extract — confirm OCI is the cloud platform |
| Partner context | W1S1-003 (already approved) | — | Link only — do not duplicate |
| Delivery model reference | W1S1-007 (already approved) | — | Link only — do not duplicate |
| Implementation methodology | Hollywood Bets / RedPath Mining RFI | SAA Section 5 | Placeholder reference only in this document — methodology is Deliverable 5 |
| Reference projects | SABS ETS table; confirmed client list | RedPath Mining RFI implementation list | Use as Appendix or reference section; note DFA as most comprehensive reference |

**Synthesis required:** Minimal. The SAA "Oracle Fusion Information" section (Section 2) is the most complete Oracle Fusion capability description in the corpus and can largely be extracted with client-specific content removed. TMPL-001 provides the structural authority; SAA provides the depth.

### Expected Approval Risk

**Low-Medium** (revised down from Medium after source assessment):
- SAA document used in a formal June 2025 submission — content is current and tender-tested
- TMPL-001 confirmed active in SABS 2025 and SANPARKS 2024 — structural authority is clear
- Company profile numbers in SAA/RedPath documents are OUTDATED (110 consultants, 22 years) — must use approved values (50+, 23 years) — this is the primary risk, but it is a known and manageable correction
- OIC as standard integration layer is confirmed in all recent implementations — low approval risk
- Cloud Excellence Implementer designation: verify on OPN before claiming

### Estimated Effort

| Task | Time |
|---|---|
| Read and cross-reference TMPL-001 Oracle Fusion section + SAA Section 2 | 30 min |
| Extract Fusion overview + core components table from TMPL-001 | 15 min |
| Extract Oracle HCM capability matrix from SAA Section 2 | 30 min |
| Extract OIC, OCI sections | 10 min |
| Apply company facts from approved sources; verify all stats | 10 min |
| Self-review against Oracle Fact Baseline | 10 min |
| Promote to Review_Required | 5 min |
| **Total (extractor)** | **~1.75 hours** |
| BU lead review | Separate — 30 min read |

### KB Destination

`06_Capabilities/Oracle/Oracle_ERP/` (alongside W1S1-003 Oracle Partnership Statement)

### Draft File ID

`W2S1-001-ORA-FusionCapability` (assign in EXTRACTION_LOG.csv at extraction time)

---

## Deliverable 2: Oracle EBS Capability Statement

### Target Audience

IT directors, procurement evaluators, and Oracle EBS administrators at organisations running Oracle EBS R12 who require implementation, upgrade, support, or managed services engagements.

### Intended Tender Usage

| Usage context | How this document is used |
|---|---|
| Oracle EBS R12 implementation RFP | Module capability section |
| EBS upgrade (R11/R12 to Cloud) | EBS section establishing history; Cloud section notes migration capability |
| Oracle EBS managed services / AMS | Capability overview before DBA and support scope |
| Multi-system Oracle tender | EBS chapter in a multi-chapter Oracle capability response |
| Government ERP tender (Oracle track) | Standard module capability matrix with local compliance notes |

### Recommended Document Structure

```
1. Oracle EBS Overview
   - APPSolve as Oracle EBS implementer and support provider
   - EBS R12 / R11 delivery history

2. Oracle EBS Module Capability Matrix
   - Financial Management (GL/AR/AP/Cash/Fixed Assets)
   - HRMS and Payroll (note SA payroll rules — see Critical Repository Rules)
   - Supply Chain Management (PO/INV/OM)
   - Projects
   - DBA and Technical Services
   - For each: brief description, module name, delivery notes

3. EBS to Oracle Cloud Migration
   - EBS as the starting point for cloud migration engagements
   - APPSolve's experience bridging EBS to Fusion

4. Oracle EBS Support and Managed Services (reference)
   - Point to HIST-002-derived DBA Executive Summary (Deliverable 3)
   - Do not duplicate — link

5. Reference Projects (when references are approved)
   - Placeholder section
```

### Sections: Extractable vs Requiring Synthesis

| Section | Source | Approach |
|---|---|---|
| EBS Overview | TMPL-002 "Oracle EBS Information" | Extract |
| Module Capability Matrix | TMPL-002 module sections | Extract — check for Payroll claims (Critical Rule 3 applies) |
| EBS-to-Cloud Migration | TMPL-002 or ATNS 2025 proposal | Extract if present; synthesise if not |
| Support and Managed Services | TMPL-002 or ATNS 2025 | Extract if present; link to DBA document otherwise |
| Partner context | W1S1-003 (approved) | Link only |
| Reference projects | Corpus | Placeholder |

**Payroll governance:** If TMPL-002 contains an Oracle EBS Payroll module claim, read it carefully before extracting. South African Oracle EBS R12 Payroll is a legitimate APPSolve delivery area. This is distinct from the BeBanking Payroll H2H rule (which covers payment processing, not implementation). Confirm with Hein Blignaut whether EBS Payroll (HRMS) implementation is in active APPSolve scope before claiming.

### Expected Approval Risk

**Low-Medium.** Risk factors:
- TMPL-002 is the current master template — high confidence that module coverage is accurate
- EBS is APPSolve's historical foundation — BU lead knows this material well
- Payroll module claims require a one-sentence BU confirmation
- If ATNS 2025 discovered source (Discovered Source A) is incorporated, ensure ATNS client references are removed

### Estimated Effort

| Task | Time |
|---|---|
| Read and assess TMPL-002 Oracle EBS section | 20–30 min |
| Extract, structure, check payroll claims | 20–25 min |
| Self-review; verify company facts | 10 min |
| Promote to Review_Required | 5 min |
| **Total (extractor)** | **~1 hour** |

### KB Destination

`06_Capabilities/Oracle/Oracle_EBS/` (currently empty — Wave 2 target folder)

### Draft File ID

`W2S1-002-ORA-EBSCapability` (assign in EXTRACTION_LOG.csv at extraction time)

---

## Deliverable 3: Oracle DBA Executive Summary

### Target Audience

IT leadership, operations directors, and procurement evaluators at organisations issuing Oracle DBA managed services or Oracle technical support RFPs. Also useful as an "about APPSolve Oracle DBA" insert in any Oracle tender where DBA team depth is evaluated.

### Intended Tender Usage

| Usage context | How this document is used |
|---|---|
| Oracle DBA managed services RFP | Lead section establishing APPSolve DBA capability |
| Oracle technical support tender | DBA team capability section |
| General Oracle tender (capability pack) | Supporting document behind Fusion and EBS statements |
| NHLS-type DBA support RFP | Purpose-built: this document was originally written for an MTN DBA managed services bid |
| Government Oracle managed services | Positions APPSolve as a specialised DBA resource, not a generalist |

### Recommended Document Structure

```
1. Executive Summary Statement
   - APPSolve Oracle DBA positioning: "one of the largest locally-based Oracle Applications DBA teams"
   - Anchor to approved claim (W1S1-007 validated: "one of the largest locally-based Oracle Applications DBA teams in South Africa")

2. Oracle DBA Service Offering
   - Database management: performance tuning, patching, upgrades, monitoring
   - Application DBA: EBS-specific DBA services
   - DBA on-site vs. remote delivery model
   - 24x7 monitoring (not 24x7x365 — Critical Rule)

3. DBA Team Profile
   - Team size range (do not give specific headcount — use approved range from W1S1-001)
   - Certifications held (reference approved certifications from DOCUMENT_REGISTER)
   - Years of specialisation (link to company history — W1S1-002)

4. SLA Framework (modernised from HIST-002)
   - Generic SLA tier structure: P1/P2/P3/P4 response and resolution targets
   - Note: extract the framework; do not copy MTN-specific SLA commitments verbatim

5. Governance Model (modernised from HIST-002)
   - Service review cadence (monthly/quarterly)
   - Escalation path
   - Reporting framework

6. Transition and Onboarding
   - Approach to knowledge transfer and environment discovery
   - Onboarding process (from HIST-002 Section 2.5)
```

### Sections: Extractable vs Requiring Synthesis

| Section | Source | Approach |
|---|---|---|
| Executive Summary Statement | HIST-002 Exec Summary PDF | Extract and modernise — update company stats, years, partner tier |
| DBA Service Offering | HIST-002 Section 2.2 Services | Extract — generalise from MTN-specific scope |
| DBA Team Profile | W1S1-001, W1S1-007 (approved) | Derive from approved content — do not fabricate headcount |
| SLA Framework | HIST-002 Section 2.3 | Extract structure; generalise tiers; remove MTN-specific numbers |
| Governance Model | HIST-002 Section 2.4 | Extract and modernise |
| Transition | HIST-002 Section 2.5 | Extract — generalise from MTN transition specifics |

**Modernisation required:** All company statistics (years in business, headcount, partner tier, awards) must be updated from the 2012/2014 source. Use approved content from Wave 1 files as the source for all company facts. Do not introduce new facts not in approved files.

### Expected Approval Risk

**Medium-High.** Risk factors:
- Source is 2012/2014 vintage — higher modernisation burden than the active templates
- SLA commitments must be generalised (not cited verbatim — MTN-specific) or confirmed with BU lead
- DBA team headcount claims in the source may not match current sizing — use approved headcount language only
- The "one of the largest locally-based Oracle Applications DBA teams" claim is approved (W1S1-007) — this is the anchor; do not go beyond it
- Executive Summary is a PDF — may require OCR or retyping rather than copy-paste

### Estimated Effort

| Task | Time |
|---|---|
| Read Executive Summary PDF and Section 2.1–2.5 | 20 min |
| Extract, structure, modernise from approved facts | 20–25 min |
| Self-review; check all company claims against Wave 1 approved files | 10 min |
| Promote to Review_Required | 5 min |
| **Total (extractor)** | **~45–55 min** |

### KB Destination

`06_Capabilities/Oracle/Oracle_Managed_Services/` (currently empty — appropriate for DBA managed services positioning)

Alternative: `02_Corporate/Executive_Summaries/` — create this folder if an executive summary tier is preferred. Recommend Oracle_Managed_Services/ as the primary destination since this is a capability statement, not a pure corporate document.

### Draft File ID

`W2S1-003-ORA-DBAExecutiveSummary` (assign in EXTRACTION_LOG.csv at extraction time)

---

## Deliverable 4: Oracle Managed Services and Support Model

### Target Audience

IT operations, procurement, and managed services buyers at organisations running Oracle EBS or Oracle Fusion who need a support contract or application managed services engagement.

### Intended Tender Usage

Oracle DBA support tenders; Oracle AMS (Application Managed Services); Oracle functional support tenders; government Oracle support RFPs (ATNS-type, NHLS-type).

### Recommended Document Structure

```
1. Oracle Support Service Overview
   - APPSolve Oracle managed services positioning
   - On-site / remote / hybrid delivery model
   - 24x7 monitoring (with after-hours support)

2. SLA Framework
   - P1/P2/P3/P4 priority tiers
   - Response and resolution targets (generalised — not MTN-specific)
   - Escalation path

3. Governance and Reporting Model
   - Monthly service review
   - Quarterly governance review
   - Reporting framework

4. Transition and Onboarding Approach
   - Environment discovery
   - Knowledge transfer approach
   - Onboarding process
```

### Primary Source

**MTN 2026 DBA RFP (RFX-1000004246, April 2026)** — used as primary source for W2S1-004 (supersedes ATNS EBS 2025 plan). 16 content blocks pre-assigned from W2S1-003 reuse map. ATNS EBS 2025 not required — MTN-2026 Q8/Q12/Q13/Q14/Q16/Q19/Q20/Q21/Q22/Q23/Q27/Q28 provided richer and more current content across all planned sections.

**Update 2026-06-11:** W2S1-004 APPROVED by Hein Blignaut. 15 sections. Complements W2S1-003 (approved 2026-06-11). All 9 factual risks resolved. All 7 assumptions (A-W4-001 through A-W4-007) scoped and resolved. Location: `07_Approved_Content/Approved/Oracle/W2S1-004-ORA-ManagedServicesSupportModel.md`.

### Expected Approval Risk

**Low** — standard service delivery structure; no controversial claims; SLA tiers are generalised.

### Estimated Effort

45–60 min extraction; 20 min BU lead review.

### KB Destination

`06_Capabilities/Oracle/Oracle_Managed_Services/`

### Draft File ID

`W2S1-004-ORA-ManagedServicesSupport`

---

## Deliverable 5: Oracle Implementation Methodology

### Target Audience

Procurement evaluators and project sponsors in Oracle implementation tenders who require evidence of a structured, repeatable delivery approach.

### Intended Tender Usage

Oracle Fusion Cloud implementation RFPs; Oracle EBS implementation or upgrade tenders; government Oracle ERP tenders that require a methodology section.

### Recommended Document Structure

```
1. Methodology Overview
   - Based on Oracle UIM (Unified Implementation Methodology) / OUM
   - APPSolve's customised OUM-based approach: Mobilize → Scoping → Prototype → Build → Deploy

2. Implementation Phases
   Phase 0 — Mobilize: Charter, work plan, kick-off
   Phase 1 — Scoping: Confirm scope, align to Oracle Modern Best Practices, data assessment
   Phase 2 — Prototype: Design workshops, Solution Reflection (CRP1 / CRP2), change control
   Phase 3 — Build: Configuration, integration build, data migration
   Phase 4 — Test: SIT, UAT, training
   Phase 5 — Deploy: Production build, data verification, hyper-care

3. Project Infrastructure
   - Risk Management: centralised risk log, mitigation ownership
   - Issue Management: severity tiers, resolution ownership, escalation
   - Change Control: formal review, approval, documentation
   - Configuration Management: environment management, release tracking

4. Data Migration Approach
   - Oracle FBDI sheets and standard APIs
   - Data reconciliation to Trial Balance control accounts
   - Customer-led with APPSolve guidance

5. Post Go-Live Support
   - Hyper-care: full complement of senior resources (3 months)
   - Critical care: reduced team (6 months)
   - Steady state: ongoing support
```

### Primary Sources

Hollywood Bets accepted proposal (V5.0, 2023) — Phase structure, Project Infrastructure sections.
RedPath Mining RFI Reply (March 2026) — Mobilize → Scoping → Prototype → Build stages; Data Migration approach; Security and Controls; OIC integration architecture.
SAA RFP Response Section 5 (June 2025) — current methodology language; customer success navigator alignment.

### Expected Approval Risk

**Low** — methodology content does not make product capability claims; risk is lower than capability statements.

### Estimated Effort

1–1.5 hours extraction; 25 min BU lead review.

### KB Destination

`05_Methodologies/Implementation/` (Oracle sub-path or directly in Implementation/)

### Draft File ID

`W2S1-005-ORA-ImplementationMethodology`

---

## Sequencing and Dependencies (Updated)

```
Pre-work (30–45 min before first extraction):
  ├── Register SAA, Hollywood Bets, RedPath Mining, ATNS in DOCUMENT_REGISTER.csv
  ├── Update BEE Level to 3 in AI_CONTEXT.md and CHECKPOINT
  ├── Create ORACLE_FACT_BASELINE.md (use as reference during extraction)
  └── Copy 25 Wave 1 files to KB destinations

Extraction Session 1 — Oracle Fusion (2–2.5 hours):
  ├── Read TMPL-001 Oracle Fusion section + SAA Section 2 (cross-reference)
  ├── Read Oracle Fact Baseline for prohibited wording and verified facts
  ├── Extract Deliverable 1: W2S1-001-ORA-FusionCapability-DRAFT.md
  └── Self-review → promote to Review_Required

Extraction Session 2 — Oracle EBS + DBA (2 hours):
  ├── Read TMPL-002 Oracle EBS section + ATNS EBS 2025 (cross-reference)
  ├── Extract Deliverable 2: W2S1-002-ORA-EBSCapability-DRAFT.md
  ├── Self-review → promote to Review_Required
  ├── Read HIST-002 Executive Summary + ATNS EBS for DBA content
  ├── Extract Deliverable 3: W2S1-003-ORA-DBAExecutiveSummary-DRAFT.md
  └── Self-review → promote to Review_Required

Extraction Session 3 — Support Model + Methodology (2–2.5 hours):
  ├── Read ATNS EBS 2025 + HIST-002 Sections 2.2–2.5
  ├── Extract Deliverable 4: W2S1-004-ORA-ManagedServicesSupport-DRAFT.md
  ├── Self-review → promote to Review_Required
  ├── Read Hollywood Bets V5.0 + RedPath Mining RFI methodology sections
  ├── Extract Deliverable 5: W2S1-005-ORA-ImplementationMethodology-DRAFT.md
  └── Self-review → promote to Review_Required

BU Lead Review (separate session — ~2 hours total):
  ├── Review W2S1-001 (Fusion): 30–40 min — most important
  ├── Review W2S1-002 (EBS): 20–25 min
  ├── Review W2S1-003 (DBA): 20 min
  ├── Review W2S1-004 (Support): 20 min
  └── Review W2S1-005 (Methodology): 20 min
```
  └── Self-review → promote to Review_Required

Extraction Session 2 (1 hour):
  ├── Read HIST-002 Executive Summary + Sections 2.1–2.5
  ├── Extract Deliverable 3: W2S1-003-ORA-DBAExecutiveSummary-DRAFT.md
  └── Self-review → promote to Review_Required

BU Lead Review (separate):
  ├── Review W2S1-001 (Fusion): ~25 min
  ├── Review W2S1-002 (EBS): ~20 min
  └── Review W2S1-003 (DBA): ~25 min — payroll claim, SLA wording
```

---

## What This Execution Plan Does NOT Cover

- Oracle HCM Capability Statement — source documents exist (Bet Software, Primedia, TBWA HCM proposals) but this is a Wave 3 item
- Oracle Cloud DBA/OCI capability — requires OCI source documents; Wave 3
- Oracle APEX capability — no source identified; Wave 3+
- Oracle upgrade/migration methodology — methodology depth is a Wave 3 item
- BeBanking Implementation Methodology — independent stream (see POST_WAVE1_ROADMAP.md Priority 4)

---

*Prepared 2026-06-10 by Claude (AI) — planning only. No extraction work performed.*
