---
document_id: WP18C1-AUTOMATION-OPPORTUNITY-REGISTER
title: "WP18C.1 — Automation Opportunity Register"
version: "1.0"
status: "COMPLETE — 2026-06-25"
created: "2026-06-25"
created_by: "WP18C.1 — Proposal Factory Optimisation"
scope: "Ranked list of automation opportunities derived from WP18C first production run analysis."
current_automation_pct: 77.2
target_automation_pct_after_register: 86
permanent_ceiling_pct: 91
---

# WP18C.1 — Automation Opportunity Register

**Current automation:** 77.2% (44 of 57 sections deterministically assembled)  
**Theoretical maximum:** ~91% (accounts for permanently non-automatable: CVs, commercial pricing)  
**Projected gain from this register:** +8.8% → 86% after Tier 0 and Tier 1 actions  
**Basis:** Evidence from ARM IT045 first production run (WP18C)

---

## 1. Rating Methodology

Opportunities are ranked by **ROI** = (Automation Gain × Reuse Value) ÷ Implementation Effort.

| Dimension | Scale |
|---|---|
| Automation Gain | HIGH = eliminates manual step for every run; MEDIUM = reduces effort; LOW = quality improvement only |
| Reuse Value | HIGH = applies to all tenders; MEDIUM = applies to multiple tender types; LOW = AMS or specific type only |
| Implementation Effort | VERY LOW = <2h; LOW = 2–8h; MEDIUM = 1–3 days; HIGH = 1–2 weeks |
| Priority | P0 = before next run; P1 = within 2 weeks; P2 = within 2 months; P3 = roadmap |

---

## 2. AO-001 — BOM-to-Capability Selection Rules (Stage 4 Automation)

| Field | Detail |
|---|---|
| **Opportunity ID** | AO-001 |
| **Category** | Engine — Stage 4 (Capability Selection) |
| **Priority** | **P0 — Before next factory run** |
| **Automation Gain** | HIGH — eliminates 60-minute manual capability selection per run |
| **Reuse Value** | HIGH — applies to every tender, every platform |
| **Implementation Effort** | VERY LOW — 2–3 hours |
| **Automation Impact** | +0% section count (sections already assembled) but makes Stage 4 deterministic and reproducible |

**Description:** The 12 capability assets selected for ARM IT045 were chosen manually by reading the BOM codes and matching to the MASTER_CAPABILITY_INDEX. The selection logic is entirely rule-based and already implicit in the index:

| BOM Trigger | Capability Asset(s) Selected |
|---|---|
| ANY proposal | W1S1-001/002/006/007/008/009 (all 6 corporate) |
| Platform = Oracle | W1S1-003 (Oracle Partnership) |
| BOM includes EBS | W2S1-002 (EBS Capability) |
| BOM includes DBA | W2S1-003 (DBA Executive Summary) |
| BOM includes AMS | W2S1-004 (Managed Services Support Model) |
| BOM includes OIC | W4-INT-001 (OIC Accelerators) |
| BOM includes OCI | [OCI capability asset — GAP-004] |
| BOM includes ERP (Fusion) | W2S1-001 + W4-ERP-001/002/003 |
| BOM includes HCM | W3S1-001 + relevant module assets |
| BOM includes Acumatica | W1S1-004 + W1S2-series per module BOM |
| BOM includes BeBanking | W1S1-005 + W1S3-series per module BOM |
| BOM includes AMS (Acumatica) | W5-ACU-001 |

**Implementation:** Add a `bom_triggers` field to each asset entry in the CONTENT_SOURCE_MATRIX.md. The Capability Selector reads BOM codes and automatically generates the selection list. No AI needed.

**Expected benefit:** Stage 4 selection time 60 min → <5 min. Eliminates analyst-dependent variation. Makes capability selection auditable and reproducible.

---

## 3. AO-002 — Engagement-Type Section Scoping Rules (Stage 1 Structure)

| Field | Detail |
|---|---|
| **Opportunity ID** | AO-002 |
| **Category** | Engine — Stage 1 (Structure Decision) |
| **Priority** | **P0 — Before next factory run** |
| **Automation Gain** | HIGH — eliminates manual section scoping decision per run |
| **Reuse Value** | HIGH — applies to every tender |
| **Implementation Effort** | VERY LOW — 2–3 hours |
| **Automation Impact** | Makes Stage 1 section scoping deterministic; reduces time from 45 min to <5 min |

**Description:** The ARM IT045 section scoping decision (57 from 82) was performed manually. The exclusion rules are deterministic and already implicit in the PROPOSAL_SECTION_LIBRARY:

| Engagement Type | Sections Excluded |
|---|---|
| AMS (any platform) | S-34 (Implementation Methodology), S-35 (Project Plan), S-39 (Testing), S-40 (Data Migration), S-41 (Training), S-42 (Cutover), S-43 (Hypercare) |
| AMS (all) + include | S-70–S-76 (AMS Support Model sections) |
| Platform ≠ Oracle | S-09/16/17/18/19/20/21/22 (conditional on Oracle BOM) |
| Platform ≠ Acumatica | S-10/23/24/25/26/27/28 |
| Platform ≠ BeBanking | S-11/29 |
| Implementation (not AMS) | S-70–S-76 excluded |

**Implementation:** Add an `engagement_type_scope` field to each section in the PROPOSAL_SECTION_LIBRARY.md:
- `always`: include in all proposals
- `ams_only`: include only when engagement_type includes AMS
- `implementation_only`: include only when engagement_type = implementation
- `conditional`: include based on BOM code

The section scoping becomes a filter pass over the section library. Output: per-tender section plan. Takes seconds, not 45 minutes.

---

## 4. AO-003 — Reference Scoring Automation (Stage 5)

| Field | Detail |
|---|---|
| **Opportunity ID** | AO-003 |
| **Category** | Engine — Stage 5 (Reference Selection) |
| **Priority** | **P0** |
| **Automation Gain** | MEDIUM — eliminates manual ranking; AM approval remains human gate |
| **Reuse Value** | HIGH — applies to every tender |
| **Implementation Effort** | LOW — 2–3 hours |
| **Automation Impact** | Stage 5 ranking becomes deterministic; AM approval gate remains |

**Description:** The scoring rules are already defined in PROPOSAL_FACTORY_ARCHITECTURE.md (R5.8):
- Exact product match = 3 points
- Platform match = 2 points
- Sector match = 1 point

Apply these rules against REFERENCE_MASTER.csv fields (products, sector) against the Tender Profile fields (bom_codes, client_sector). Output: ranked reference list with scores. Top 4 presented to AM for approval. This eliminates the manual selection step while preserving the human approval gate.

**Add:** An `am_approval_status` field to REFERENCE_MASTER.csv (last_approved_date, last_approval_tender_id). This enables the system to flag which references have recent approval and which need fresh AM confirmation.

---

## 5. AO-004 — Methodology Selection Lookup Table (Stage 6)

| Field | Detail |
|---|---|
| **Opportunity ID** | AO-004 |
| **Category** | Engine — Stage 6 (Methodology Selection) |
| **Priority** | **P0** |
| **Automation Gain** | MEDIUM — eliminates manual pattern selection; 15–20 min → <1 min |
| **Reuse Value** | HIGH — applies to every tender |
| **Implementation Effort** | VERY LOW — 2 hours |
| **Automation Impact** | Stage 6 becomes deterministic for all standard engagement types |

**Description:** The 13 delivery patterns map directly to engagement type and platform:

| Engagement Type | Platform | Pattern |
|---|---|---|
| AMS | Oracle EBS | Pattern 13 |
| AMS (non-EBS) | Oracle Fusion | Pattern 13 (adapted) |
| AMS | Acumatica | Pattern 11 |
| DBA / Infra Only | Oracle | Pattern 10 |
| Implementation | Oracle Fusion HCM | Pattern 1–9 per module |
| Implementation | Oracle Fusion ERP | Pattern 1–9 per module |
| Implementation | Oracle EBS | Pattern 1–9 (EBS-adapted) |
| Implementation | Acumatica | Pattern 11 |
| Implementation | BeBanking | Pattern 12 |
| Multi-platform | Oracle + Acumatica | W5-METH-001 (cross-BU) |

**Implementation:** Add `delivery_pattern_id` as a computed field in Stage 6, derived from Tender Profile fields (engagement_type + platform_bom). This is a lookup — no AI needed. Output: Pattern ID + methodology asset ID(s) to include.

---

## 6. AO-005 — Merge S-38 + S-73 for AMS Proposals

| Field | Detail |
|---|---|
| **Opportunity ID** | AO-005 |
| **Category** | Section Library — Deduplication |
| **Priority** | **P0** |
| **Automation Gain** | LOW (quality) — eliminates content duplication |
| **Reuse Value** | HIGH — applies to all AMS proposals |
| **Implementation Effort** | VERY LOW — 1 hour |
| **Automation Impact** | Eliminates S-38 from AMS proposals; S-73 becomes canonical |

**Description:** S-38 (Change Control Framework — Governance section) and S-73 (Change Request Process — AMS Support section) describe the same process. For an AMS proposal, the change process belongs entirely in the AMS support model. S-38 is a legacy generic section that pre-dates the AMS support section library.

**Implementation:** In PROPOSAL_SECTION_LIBRARY, add a scoping rule to S-38: `exclude_if: engagement_type = AMS`. The content that was in S-38 is fully covered by S-73. Removing S-38 from AMS proposals eliminates the duplication automatically in every future AMS run.

**Side effect:** The in-scope section count for ARM IT045 drops from 57 to 56. Not significant. The quality improvement is the point.

---

## 7. AO-006 — OCI Capability Asset (Content Gap, High Reuse)

| Field | Detail |
|---|---|
| **Opportunity ID** | AO-006 |
| **Category** | Content — New KB Asset |
| **Priority** | **P1 — Within 2 weeks** |
| **Automation Gain** | HIGH — converts S-22 from AI-GENERATE to DIRECT for all OCI-scope tenders |
| **Reuse Value** | HIGH — every OCI-scope tender (ARM-type AMS, OCI infrastructure proposals) |
| **Implementation Effort** | LOW — 4–8 hours authoring + BU Lead review |
| **Automation Impact** | S-22: AI-GENERATE (L1) → DIRECT (L3); ~+1.75% automation rate |

**Description:** GAP-004 identified in WP18C. This is the highest-value single content asset that can be created to improve factory output. Oracle OCI managed services is a growing component of APPSolve's Oracle practice. Every OCI-in-scope proposal currently has a generic AI-generated OCI section. One approved OCI capability asset (similar in format to W2S1-002 EBS or W2S1-003 DBA) fixes S-22 for all future runs.

**Asset specification:** W2S1-006 Oracle OCI Capability Statement. Sections: OCI Practice Overview, OCI Service Scope, OCI-specific differentiators, OCI references (ARM existing; MTN REF-ORA-009), OCI certifications. Target length: 400–600 words. Governance restrictions: no rates; OPN Level 1; no Gold Partner.

---

## 8. AO-007 — Delivery Pattern Risk Registers (Stage 8 Content)

| Field | Detail |
|---|---|
| **Opportunity ID** | AO-007 |
| **Category** | Content Structure — Pattern-Specific |
| **Priority** | **P1 — Within 2 weeks** |
| **Automation Gain** | MEDIUM — converts S-50 from AI-GENERATE to TEMPLATE; reduces BU review from 2h to 30min |
| **Reuse Value** | HIGH — applies to all tenders until Risk Library is fully populated |
| **Implementation Effort** | LOW — 1–2 hours per pattern (start with Pattern 13 AMS) |
| **Automation Impact** | S-50: AI-GENERATE (L1) → TEMPLATE (L2); quality improvement for every run |

**Description:** The WP18C ARM IT045 Risk Register (S-50) was AI-generated with 9 generic EBS AMS risks. These were plausible but not ARM-specific. A pre-approved 10-risk register for Pattern 13 (AMS/Managed Services Onboarding) would give the factory a baseline that the BU Lead reviews and edits rather than reviewing AI-generated content from scratch.

**Structure:** For each delivery pattern, author a 10-risk register using the Risk Library Standard format. Risks are pattern-specific (not tender-specific) and therefore stable across all tenders using that pattern. For Pattern 13 AMS: Resource Continuity, Scope Creep, EBS Patch Failure, Licensing, OIC Failure, Knowledge Loss, OCI Cost Overrun, POPIA Breach, Concurrent Manager Instability, and one pattern-specific risk (e.g., onboarding delay risk). BU Lead approves the pattern register once; it is reused across all AMS tenders.

**Note:** This is distinct from the Risk Library population (WP18B-EXT), which extracts risks from existing capability assets. Pattern Risk Registers are a faster interim solution. Both should be pursued.

---

## 9. AO-008 — Commercial Section Template

| Field | Detail |
|---|---|
| **Opportunity ID** | AO-008 |
| **Category** | Content Structure — Commercial |
| **Priority** | **P0 — Immediate** |
| **Automation Gain** | LOW — Commercial Director still authors; but effort drops from 2–4h to 30min |
| **Reuse Value** | HIGH — every fixed-price tender |
| **Implementation Effort** | VERY LOW — 1 hour |
| **Automation Impact** | S-52: PLACEHOLDER → structured TEMPLATE; section completeness improves |

**Description:** The current S-52 (Commercials/Pricing) is a pure PLACEHOLDER with no structure. The Commercial Director has nothing to work from. A template that provides headings, placeholder labels, and brief instructions reduces authoring to gap-fill.

**Template structure:**
```
## [TENDER_ID] — Commercial Proposal

### Monthly Retainer Fee
[COMMERCIAL DIRECTOR INPUT — total monthly retainer, inclusive of all named services]

### What the Retainer Includes
[Reference to Resource Model (Section X) and Scope Inclusions (Section Y)]

### Out-of-Scope Change Requests
[COMMERCIAL DIRECTOR INPUT — rate basis (T&M / day rate / project priced); do not include actual rates]

### Contract Term and Renewal
[COMMERCIAL DIRECTOR INPUT — initial term, notice period, renewal mechanism, price escalation clause]

### Payment Terms
[COMMERCIAL DIRECTOR INPUT — payment schedule, invoice terms]

### Optional Services
[COMMERCIAL DIRECTOR INPUT — DR, additional training, upgrade project rates — do not include actual rates]
```

No rates, margins, or monetary thresholds appear in the template. These are COMMERCIAL DIRECTOR INPUT placeholders only.

---

## 10. AO-009 — Tender Profile Intake Form (Stage 0)

| Field | Detail |
|---|---|
| **Opportunity ID** | AO-009 |
| **Category** | Pipeline — Stage 0 (New Stage) |
| **Priority** | **P0 — Before next factory run** |
| **Automation Gain** | HIGH — provides structured input for all subsequent stages; eliminates context-gathering overhead |
| **Reuse Value** | HIGH — every tender |
| **Implementation Effort** | LOW — 2–3 hours to design and document the form |
| **Automation Impact** | Not a section automation; but enables AO-001 through AO-004 to function deterministically |

**Description:** Every factory run currently begins with an implicit, undocumented context-gathering step. The Bid Manager (or analyst) collects: client name, tender ID, engagement type, BOM codes, modules, SLA tier, resource model, client sector, submission date, compliance requirements. This information is currently either known from memory or inferred from prior tender documents. It must become a structured artefact.

**Proposed Tender Profile format (YAML frontmatter in a new file `[TENDER_ID]_TENDER_PROFILE.md`):**
```yaml
tender_id: ARM-IT045
client: African Rainbow Minerals
client_sector: Mining and Resources
engagement_type: AMS
platform: Oracle
bom_codes: [EBS, DBA, OIC, OCI, AMS]
sla_tier: Enhanced
monthly_hours: 680
submission_date: [DATE]
bee_requirement: Level 3 minimum
compliance_requirements: [BBBEE, TAX, ORACLE_OPN]
reference_sector_preference: Mining
am_approver: [NAME]
```

This 10-field form, completed by the Bid Manager on tender intake, becomes the input to Stages 1–6 and the anchor for the assembly audit trail. It is the factory's missing Stage 0.

---

## 11. AO-010 — Weighted Readiness Score

| Field | Detail |
|---|---|
| **Opportunity ID** | AO-010 |
| **Category** | Metrics — Stage 5 Dashboard |
| **Priority** | **P1** |
| **Automation Gain** | LOW — quality of readiness signal |
| **Reuse Value** | HIGH |
| **Implementation Effort** | LOW — 2 hours |
| **Automation Impact** | Readiness score becomes more meaningful; blocking items surface faster |

**Description:** The current readiness percentage (67%) counts sections equally. A READY award table (S-05) is weighted the same as a READY Assumption Schedule (A-01). A more useful readiness signal weights sections by mandatory status and evaluator visibility.

**Proposed weighting:** Sections weighted 1–5 based on: is_mandatory (2x multiplier if mandatory) × evaluator_visibility (HIGH=3, MEDIUM=2, LOW=1). The weighted readiness score surfaces the commercial and people gaps (which are HIGH visibility) more prominently than minor PARTIAL sections.

**Example:** Under flat weighting, ARM IT045 is 67% ready. Under weighted scoring, it would be lower (~52%) because the two most visible gaps — S-52 (Commercial, mandatory, HIGH visibility) and S-47/A-02 (CVs, HIGH visibility) — are weighted more heavily than PARTIAL sections like S-05 (Awards) or S-20 (DBA stats).

---

## 12. AO-011 — Gap Type Classification

| Field | Detail |
|---|---|
| **Opportunity ID** | AO-011 |
| **Category** | Gap Register — Schema |
| **Priority** | **P1** |
| **Automation Gain** | LOW — reduces noise; improves decision quality |
| **Reuse Value** | HIGH — every tender |
| **Implementation Effort** | VERY LOW — 1 hour |
| **Automation Impact** | Gap register becomes more actionable; permanent constraints correctly excluded from factory remediation |

**Description:** The current Gap Register lists 14 gaps. Of these, 2 are PERMANENT (CVs, commercial pricing) — they will be in every gap register forever because they reflect governance constraints, not factory deficiencies. Including them as gaps implies they need fixing. They don't.

**Proposed gap_type classification:**
- `PERMANENT`: Governance-mandated constraint; will never be automated (CVs, commercial pricing)
- `LIBRARY`: Resolvable by adding KB content (OCI narrative, Risk Library, methodology assets)
- `ENGINE`: Resolvable by building a factory stage (Stage 2 requirements, Stage 4 selector)
- `PROCESS`: Resolvable by improving a business process (AM approval workflow, B-BBEE renewal)
- `TENDER-SPECIFIC`: Unique to this engagement; not a factory structural issue

Under this classification, the ARM IT045 14 gaps break into: PERMANENT (2), LIBRARY (5), ENGINE (2), PROCESS (3), TENDER-SPECIFIC (2). The factory improvement roadmap only acts on LIBRARY and ENGINE types. PERMANENT and PROCESS types are noted but not counted against factory performance.

---

## 13. AO-012 — Two-Pass Assembly Process

| Field | Detail |
|---|---|
| **Opportunity ID** | AO-012 |
| **Category** | Engine — Stage 8 Process |
| **Priority** | **P2** |
| **Automation Gain** | MEDIUM — reduces unnecessary AI generation; improves early detection |
| **Reuse Value** | HIGH |
| **Implementation Effort** | LOW — 2–3 hours process change |
| **Automation Impact** | Defers AI-GENERATE sections to Pass 2; Pass 1 READY sections validated before AI cost is incurred |

**Description:** The current Stage 8 assembles all sections in a single pass. AI-generated sections (S-13, S-14, S-22, S-50) are produced in the same pass as deterministic sections (S-03, S-30, S-71).

**Better pattern:**
- Pass 1: Assemble all DIRECT/EXTRACT/MERGE sections (77.2% of sections). Review Pass 1 output. If major issues found, fix before AI generation.
- Pass 2: Generate AI-GENERATE sections with full context from Pass 1. AI sections are better when the deterministic proposal context is already assembled (executive summary can reference specific scope inclusions; risk register can reference specific SLA commitments from S-71).

This process change requires no new build — it is a discipline change in how the factory runs. The AI-generated sections will also be better quality because the deterministic context they draw on is already finalised.

---

## 14. AO-013 — AI Context Enrichment for Executive Summary

| Field | Detail |
|---|---|
| **Opportunity ID** | AO-013 |
| **Category** | AI Generation Quality — Stage 8 |
| **Priority** | **P1** |
| **Automation Gain** | LOW (quality, not count) — better AI draft reduces BU edit from 1–2h to 30min |
| **Reuse Value** | HIGH — every tender |
| **Implementation Effort** | VERY LOW — 1–2 hours to document context injection standard |
| **Automation Impact** | S-13 remains AI-GENERATE but produces a better starting draft |

**Description:** The WP18C Executive Summary draft was generic. The AI generator had access to W1S1-001 and tender context but not to the specific relationship signals that make an executive summary persuasive:
1. Prior client relationship details (from REFERENCE_MASTER.csv — client, products, duration)
2. Specific client pain point addressed (from Tender Profile — why they're issuing the RFP)
3. The single most relevant differentiator for this specific engagement type

**Implementation:** Add a structured "Executive Summary Context" block to the Tender Profile (AO-009). Fields:
- `prior_relationship_ref_id`: reference to REFERENCE_MASTER entry (e.g., REF-ORA-008)
- `client_pain_point`: one sentence from RFP analysis
- `key_differentiator`: which of APPSolve's differentiators is most relevant (e.g., "continuity of knowledge — prior ARM work")

This 3-field addition to the Tender Profile gives the AI generator the personalisation anchors it needs to write a draft that the BU Lead edits rather than rewrites.

---

## 15. AO-014 — SLA/Incident Section Clean Split

| Field | Detail |
|---|---|
| **Opportunity ID** | AO-014 |
| **Category** | Section Library — Deduplication |
| **Priority** | **P1** |
| **Automation Gain** | LOW — quality improvement |
| **Reuse Value** | MEDIUM — AMS proposals only |
| **Implementation Effort** | VERY LOW — 30 minutes |
| **Automation Impact** | S-71 and S-72 no longer overlap; single authoritative source for SLA times |

**Description:** S-71 (SLA Framework) contains the SLA table including acknowledgement times. S-72 (Incident Management) contains the P1 escalation timeline which repeats the acknowledgement time (T+15 = ARM IT Contact notified — acknowledgement SLA). A clean split rule:
- S-71: SLA table ONLY (no process narrative)
- S-72: Process narrative ONLY; reference SLA times via "per S-71 SLA Framework" rather than re-stating values

This is a content authoring note (not a system change) that should be added to the CONTENT_SOURCE_MATRIX.md as an assembly instruction for S-71 and S-72.

---

## 16. AO-015 — Section Order Corrections (Three Changes)

| Field | Detail |
|---|---|
| **Opportunity ID** | AO-015 |
| **Category** | Section Library — Ordering |
| **Priority** | **P1** |
| **Automation Gain** | LOW — proposal quality |
| **Reuse Value** | HIGH — all proposals |
| **Implementation Effort** | VERY LOW — 1 hour |
| **Automation Impact** | None; reading experience improvement |

**Three order corrections identified from reviewer analysis:**

**A. Move References (S-67) to after Commercial (S-52):**
Current: Understanding → Solution → Scope → Governance → People → Commercial → Compliance → **References** → AMS Model
Better: Understanding → Solution → Scope → Governance → People → Commercial → **References** → Compliance → AMS Model → Appendices

Rationale: Client evaluates the service model and commercial offer before checking credentials. References serve as post-commercial validation ("now that you know what we'll do and what it costs, here's who confirms we deliver").

**B. Move Key Assumptions (S-49) to after Commercial Proposal (S-52):**
Current: Commercial section contains S-49 → S-50 → S-51 → S-52
Better: Commercial section contains S-52 → S-49 → S-50 → S-51

Rationale: The commercial offer (S-52) sets the context. The assumptions (S-49) govern the offer. The risk register (S-50) contextualises the risks the assumptions are managing. The full schedule (S-51) is the detail. This creates a logical "offer → assumptions → risks → full schedule" flow.

**C. Move Resource Model (S-74) to first position within AMS block:**
Current AMS order: S-70 (Support Model) → S-71 (SLA) → S-72 (Incident) → S-73 (CR) → **S-74 (Resource Model)** → S-75 (Release) → S-76 (Monitoring)
Better: **S-74 (Resource Model)** → S-70 (Support Model) → S-71 (SLA) → S-72 (Incident) → S-73 (CR) → S-75 (Release) → S-76 (Monitoring)

Rationale: The client needs to understand who is delivering (Resource Model) before they can contextualise what is being delivered (Support Model, SLA, Incident process). The team definition should be the entry point to the AMS section.

---

## 17. Summary: Automation Gain Register

| ID | Opportunity | Priority | Effort | Automation Gain | Type |
|---|---|---|---|---|---|
| AO-001 | BOM-to-Capability Selection Rules | **P0** | VERY LOW | HIGH — Stage 4 deterministic | Engine |
| AO-002 | Engagement-Type Section Scoping Rules | **P0** | VERY LOW | HIGH — Stage 1 deterministic | Engine |
| AO-003 | Reference Scoring Automation | **P0** | LOW | MEDIUM — Stage 5 ranking deterministic | Engine |
| AO-004 | Methodology Lookup Table | **P0** | VERY LOW | MEDIUM — Stage 6 deterministic | Engine |
| AO-005 | Merge S-38 + S-73 for AMS | **P0** | VERY LOW | LOW — deduplication | Library |
| AO-008 | Commercial Section Template | **P0** | VERY LOW | LOW — CD effort reduced | Content |
| AO-009 | Tender Profile Intake Form (Stage 0) | **P0** | LOW | HIGH — enables AO-001/002/003/004 | Engine |
| AO-006 | OCI Capability Asset (W2S1-006) | P1 | LOW | HIGH — S-22 AI→DIRECT (+1.75%) | Content |
| AO-007 | Pattern Risk Registers (Pattern 13 first) | P1 | LOW | MEDIUM — S-50 AI→TEMPLATE | Content |
| AO-010 | Weighted Readiness Score | P1 | LOW | LOW — metrics quality | Engine |
| AO-011 | Gap Type Classification | P1 | VERY LOW | LOW — gap register quality | Engine |
| AO-012 | Two-Pass Assembly Process | P1 | LOW | MEDIUM — AI quality + cost | Engine |
| AO-013 | AI Context Enrichment (Exec Summary) | P1 | VERY LOW | LOW — draft quality | Engine |
| AO-014 | SLA/Incident Section Clean Split | P1 | VERY LOW | LOW — deduplication | Library |
| AO-015 | Section Order Corrections (3 changes) | P1 | VERY LOW | LOW — quality | Library |

**Total Tier P0 effort:** ~10 hours  
**Total Tier P1 effort:** ~12–18 hours  
**Combined effort for full register:** ~22–28 hours  
**Projected automation rate after P0+P1:** ~85–86% (up from 77.2%)

---

## 18. Automation Gain by Category

| Section Category | Current Auto% | After AO Register | Gain |
|---|---|---|---|
| Corporate and Partnership | ~88% | ~88% | No change (already high) |
| Understanding and Solution | ~55% | ~62% | +7% (OCI asset; context enrichment) |
| Scope and Governance | ~74% | ~80% | +6% (merge S-38; section rules) |
| People | ~15% | ~20% | +5% (CONSULTANT_INDEX enrichment; not in this register) |
| Commercial and Governance | ~50% | ~52% | +2% (commercial template; pattern risk register) |
| Compliance and Credentials | ~65% | ~65% | No change (already structured) |
| References | ~50% | ~60% | +10% (reference scoring automation) |
| AMS Support Sections | ~80% | ~82% | +2% (SLA clean split; order fix) |
| Appendices | ~55% | ~55% | No change |
| **Overall** | **77.2%** | **~85%** | **+7.8%** |

---

*WP18C1_AUTOMATION_OPPORTUNITY_REGISTER.md v1.0 | WP18C.1 — Proposal Factory Optimisation | 2026-06-25*  
*15 automation opportunities. Tier P0: 7 actions, ~10h, enable all subsequent gains. Tier P1: 8 actions, ~18h, +7.8% automation rate. Combined projected automation: ~85% (from 77.2%).*
