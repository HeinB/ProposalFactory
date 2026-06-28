---
document_id: TENDER-PROFILE-STANDARD
title: "Tender Profile Standard — Structured Intelligence Schema"
version: "1.0"
status: "Approved — WP18C.3"
created: "2026-06-25"
created_by: "WP18C.3 — Tender Intelligence Layer"
category: "Architecture / Intelligence Layer"
scope: "Defines the canonical Tender Profile: the single structured intelligence document that every Proposal Factory run begins with. Every field is specified with its source, extraction rule, validation rule, and default behaviour. The Tender Profile completely determines: proposal pattern, capability selection, methodology selection, reference selection, assembly rules, confidence, and human follow-up questions."
---

# Tender Profile Standard

**Date:** 2026-06-25 | **Version:** 1.0 | **Status:** Approved  
**Work Package:** WP18C.3 — Tender Intelligence Layer  
**Governs:** All downstream Proposal Factory stages (Stages 2–10)

---

## 1. Purpose

The Tender Profile is the single structured intelligence output that must exist before any proposal assembly begins. It replaces unstructured tender document review with a deterministic, machine-readable intelligence layer.

Every Proposal Factory run begins by producing a Tender Profile. All downstream selections — capability assets, methodology, references, section scope, governance flags — are derived from the Tender Profile, not from re-reading the tender document.

**A Tender Profile is NOT:**
- A tender summary or narrative
- A copy of tender requirements
- A partially completed document with guesses

**A Tender Profile IS:**
- A structured record of every known fact about the tender
- A complete list of every field that could not be determined (unknowns explicit — never suppressed)
- A set of derived selections (pattern, BOM triggers, section scope) ready for factory input
- A confidence rating that gates human escalation

**Governing principle:** *Unknowns must remain explicit rather than inferred.* A LOW-confidence guess is worse than an acknowledged unknown, because a guess propagates silently into the assembled proposal.

---

## 2. Tender Profile YAML Schema

This is the canonical schema. Every `[TENDER_ID]_TENDER_PROFILE.md` file produced by the factory must conform to this structure.

```yaml
tender_profile:
  schema_version: "1.0"
  tender_id: ""                    # e.g. ARM-IT045
  profile_created: ""              # ISO date: 2026-06-25
  profile_status: ""               # DRAFT / REVIEWED / APPROVED
  confidence_overall: ""           # HIGH / MEDIUM / LOW
  assembly_gate: ""                # GO / HOLD / ESCALATE

  # === Block A: Tender Metadata ===
  tender_metadata:
    client_name: ""
    tender_reference: ""
    submission_deadline: ""        # ISO datetime; include SAST offset +02:00
    submission_format: ""          # PDF-Email / Portal / Physical / Online-Form
    received_date: ""              # ISO date
    contact_person: ""
    issuing_entity: ""             # Legal entity issuing the RFP (may differ from client_name)

  # === Block B: Client Profile ===
  client_profile:
    industry: ""                   # Mining / Financial-Services / Retail / Manufacturing / Healthcare / Government / Education / Telecommunications / Other
    sector_subsector: ""           # e.g. "Diversified Mining (Gold, Platinum, Iron Ore)"
    country: ""                    # ISO 3166-1 alpha-2: ZA / NG / UG / GH / QA / Other
    organisation_size: ""          # Enterprise (>1000 EE) / Mid-market (200–1000 EE) / SME (<200 EE)
    headcount: ""                  # number or range if known
    current_erp: ""                # Oracle-EBS-12.1 / Oracle-EBS-12.2 / Oracle-Fusion / SAP / Sage / None / Unknown

  # === Block C: Platform and Products ===
  platform_products:
    primary_platform: ""           # Oracle-Fusion / Oracle-EBS / Acumatica / BeBanking / Hybrid
    oracle_products: []            # [HCM, ERP-Financials, ERP-Procurement, PPM, OIC, EBS, DBA, OCI]
    non_oracle_products: []        # [Acumatica, BeBanking, PaySpace-Integration, Other]
    hosting_model: ""              # OCI / On-Premises / Hybrid / SaaS-Managed / Unknown
    oracle_version: ""             # EBS: "12.1" / "12.2"; Fusion: "current" / specific release; Unknown

  # === Block D: Scope Dimensions ===
  scope_dimensions:
    engagement_type: ""            # Implementation / AMS / Upgrade / NewModule / Standalone-Integration / Standalone-DBA / Hybrid
    modules_in_scope: []           # [CoreHR, Absence, Journeys, Recruiting, Learning, Talent, Compensation, AISkills, Financials, Procurement, PPM, OIC, EBS-Finance, EBS-HRMS, Acumatica-Financials, Acumatica-Distribution, Acumatica-Manufacturing, BeBanking-Supplier, BeBanking-Payroll, BeBanking-Forex]
    integration_scope: ""          # YES / NO / UNKNOWN
    integration_detail: []         # e.g. [PaySpace-OIC, Bank-OIC, Custom-API]
    migration_scope: ""            # YES / NO / UNKNOWN
    migration_detail: ""           # e.g. "HR data from Sage People; financial opening balances only"
    training_scope: ""             # YES / NO / UNKNOWN
    dr_in_scope: ""                # YES / NO / UNKNOWN
    security_in_scope: ""          # YES / NO / UNKNOWN
    support_scope: ""              # YES / NO / UNKNOWN
    support_detail: ""             # e.g. "AMS retainer 40h/month; EBS Finance + HRMS"
    oci_in_scope: ""               # YES / NO / UNKNOWN
    parallel_run_required: ""      # YES / NO / CLIENT-WAIVER / UNKNOWN  [HCM payroll default = YES per HCM-CUT-005]

  # === Block E: Commercial Model ===
  commercial_model:
    pricing_type: ""               # Fixed-Price / T&M / Retainer / Hybrid / Unknown
    contract_term: ""              # e.g. "24 months initial + 12-month renewal options"
    cr_model: ""                   # T&M-Only / Fixed-CR-Allowed / Unknown  [AMS default: T&M-Only]
    sla_requirements: ""           # YES / NO / UNKNOWN
    sla_detail: ""                 # e.g. "P1=1h, P2=4h, P3=1BD, P4=3BD — SAST Mon–Fri 08:00–17:00"
    hours_model: ""                # Allocated-Monthly / Per-Incident / Retainer / Unknown

  # === Block F: Compliance and Governance ===
  compliance_governance:
    bbee_requirement: ""           # YES / NO / Unknown
    bbee_level_required: ""        # "1" / "2" / "3" / "4" / "Any" / Unknown
    compliance_documents: []       # [CIPC, TaxClearance, PublicLiability, OracleOPN, AcumaticaCert, BBEE, ISO, POPIA, PAIA, NDA, Other]
    mandatory_references: ""       # YES / NO / UNKNOWN
    reference_requirements: ""     # Specific reference requirements from RFP (count, sector, product, rand value threshold)
    scoring_criteria: {}           # e.g. {Technical: 70, Commercial: 20, BBEE: 10}
    evaluation_methodology: ""     # "PPPFA-80/20" / "PPPFA-90/10" / "Quality-Gate-then-Price" / "Weighted-Scoring" / Unknown
    popia_required: ""             # YES / NO / UNKNOWN
    nda_required: ""               # YES / NO / UNKNOWN

  # === Block G: Derived Fields (auto-populated by TIL engines — do not manually override) ===
  derived_fields:
    proposal_pattern: ""           # Pattern-1 through Pattern-13; combination e.g. "Pattern-13+Pattern-6"
    bom_triggers: []               # BOM IDs active for this tender e.g. [BOM-13, BOM-16]
    methodology_asset: ""          # "W2S1-005" / "W5-METH-001" / "None" (AMS)
    project_plan_template: ""      # "PT-01" through "PT-13" / "None" (AMS/DBA)
    sections_in_scope: []          # Full list of section IDs for this engagement
    sections_excluded: []          # Explicit list of excluded sections with reason codes
    capability_assets_required: [] # Required capability asset IDs
    capability_assets_optional: [] # Optional capability asset IDs (BU Lead selects)
    reference_pool: []             # Eligible reference IDs, scored and ranked
    assumption_packs: []           # Pack manifest for BOM_RESOLVER (existing WP17B engine)

  # === Block H: Intelligence Quality ===
  intelligence_quality:
    confidence_per_field: {}       # {field_name: HIGH / MEDIUM / LOW / UNKNOWN}
    unknown_fields: []             # Explicit list of fields that could not be determined
    human_follow_up: []            # Numbered questions for BU Lead or Account Manager
    governance_flags: []           # Active governance restrictions triggered by this profile
    assembly_blockers: []          # Unknown fields that BLOCK assembly if unresolved
```

---

## 3. Field Specification Tables

### Block A — Tender Metadata

| Field | Source | Extraction Rule | Validation Rule | Default / Unknown Behaviour |
|---|---|---|---|---|
| `client_name` | RFP cover page / official letterhead | Legal entity name as stated; capture trading name if different | Check against GOVERNANCE_RESTRICTIONS.md: Rule 21.4 (DFA, CCBA), Rule 21.5 (Redpath Mining), Rule 21.6 (SAA) | UNKNOWN → **BLOCK ASSEMBLY**; flag for human entry |
| `tender_reference` | RFP header / subject line / title page | Alphanumeric code from RFP | Non-empty; must match active tender workspace ID | UNKNOWN → flag for human entry; assembly may proceed cautiously |
| `submission_deadline` | RFP document (closing date/time) | ISO datetime with SAST offset (+02:00) | Must be future-dated; if past-dated → escalate immediately | UNKNOWN → **URGENT escalation**; assembly blocked until confirmed |
| `submission_format` | RFP submission instructions | Portal / PDF-Email / Physical / Online-Form | Validate against known portals (eTenders, SCM systems) | UNKNOWN → flag for human check before final assembly |
| `received_date` | Email metadata / file creation date | ISO date | Non-empty | Fallback: file creation date |
| `contact_person` | RFP contacts section | Name + title + email (phone optional) | — | UNKNOWN → acceptable; flag for BU Lead |
| `issuing_entity` | RFP header / legal terms | Full legal name of issuing organisation | May differ from client_name (e.g. procurement agent vs operating company) | Default: same as client_name |

### Block B — Client Profile

| Field | Source | Extraction Rule | Validation Rule | Default / Unknown Behaviour |
|---|---|---|---|---|
| `industry` | RFP cover / company profile / context section | Map to standard category: Mining / Financial-Services / Retail / Manufacturing / Healthcare / Government / Education / Telecommunications / Other | — | UNKNOWN → MEDIUM confidence; flag for human; affects G-001 (Compensation = Mining only) |
| `sector_subsector` | RFP company description | e.g. "Gold and platinum mining" | Subsector informs governance rules and reference scoring | UNKNOWN → acceptable; note |
| `country` | RFP issuing entity / operations section | ISO 3166-1 alpha-2 | ZA submissions require B-BBEE; non-ZA → flag compliance impact | Default: ZA if no indicator and all signs point to South Africa |
| `organisation_size` | Company profile / headcount | Enterprise (>1000 EE) / Mid-market (200–1000 EE) / SME (<200 EE) | Informs reference scoring (customer_size dimension) | UNKNOWN → MEDIUM; default Mid-market |
| `headcount` | RFP context / company profile | Exact number or "approximately X" | Numeric validation if stated | UNKNOWN → acceptable |
| `current_erp` | As-is environment section | Named system and version | Informs migration scope; EBS engagement must confirm version (12.1 vs 12.2) | UNKNOWN → flag for discovery question |

### Block C — Platform and Products

| Field | Source | Extraction Rule | Validation Rule | Default / Unknown Behaviour |
|---|---|---|---|---|
| `primary_platform` | RFP title / scope section | Match to: Oracle-Fusion / Oracle-EBS / Acumatica / BeBanking / Hybrid | Must resolve; Hybrid only when confirmed multi-platform in single tender | UNKNOWN → **BLOCK ASSEMBLY** |
| `oracle_products` | RFP scope / requirements | List each Oracle product named: HCM / ERP-Financials / ERP-Procurement / PPM / OIC / EBS / DBA / OCI | **NEVER cite Oracle Gold Partner (expired 2021) — Level 1 only** | UNKNOWN products → flag as scope ambiguity |
| `non_oracle_products` | RFP scope section | Acumatica / BeBanking / PaySpace (always integration SOR, not in scope for implementation) | Flag if PaySpace listed as implementation scope — it is not | — |
| `hosting_model` | Hosting / infrastructure section | OCI / On-Premises / Hybrid / SaaS-Managed | If OCI: triggers S-22 and OCI assumption pack; if On-Prem: EBS | UNKNOWN → derive by platform: Fusion HCM/ERP = OCI; EBS = On-Prem default |
| `oracle_version` | As-is environment / technical specs | EBS: "12.1" / "12.2"; Fusion: release or "current" | EBS vintage → flag W2S1-002 content modernisation (2012–2014 vintage assets) | UNKNOWN → acceptable; note for human |

### Block D — Scope Dimensions

| Field | Source | Extraction Rule | Validation Rule | Default / Unknown Behaviour |
|---|---|---|---|---|
| `engagement_type` | RFP title / scope statement / key verbs ("implement", "support", "maintain", "upgrade") | Implementation / AMS / Upgrade / NewModule / Standalone-Integration / Standalone-DBA | **Critical** — drives pattern and section scoping; must not be defaulted by inference alone | UNKNOWN → **BLOCK ASSEMBLY** |
| `modules_in_scope` | Requirements / scope sections | List all named modules; infer from requirements when not explicit | Map to known taxonomy; flag unsupported modules | UNKNOWN → flag for scoping question |
| `integration_scope` | Technical requirements / integration section | YES if integrations mentioned; name each integration | OIC integrations trigger BOM 9; Section 13.2 of W3S1-009 NEVER in external submissions; HIST-018 billing NEVER external | UNKNOWN → treat as NO with LOW confidence |
| `migration_scope` | Data migration section | YES if migration deliverables listed; type: Opening-Balances-Only / Full-History / HR-Data / Financial | Opening Balances = standard; Full History = CR (ERP-DAT-006) | UNKNOWN → YES for implementations (LOW confidence) |
| `training_scope` | Delivery requirements | YES if training deliverables required; flag SETA reporting if Learning Cloud in scope | Default: YES for all implementations | UNKNOWN → YES |
| `dr_in_scope` | Technical / compliance section | YES if DR requirements stated explicitly | Flag S-44 (Disaster Recovery — EMPTY — GAP-013) if YES | UNKNOWN → NO |
| `security_in_scope` | Technical requirements section | YES if security architecture deliverable required | Flag S-45; OCI Security = OCI-SLA-overlay assumption pack | UNKNOWN → NO |
| `support_scope` | Post-go-live / managed services section | YES if AMS or managed services specified | Triggers BOM 16; Pattern 13; sections S-70–S-76 | UNKNOWN → NO |
| `oci_in_scope` | Infrastructure / hosting section | YES if OCI explicitly in scope or Fusion SaaS confirmed | Triggers OCI assumption pack (174 assumptions); S-22 in scope | UNKNOWN → derive from hosting_model |
| `parallel_run_required` | Payroll / cutover section | YES if payroll interface in scope (HCM-CUT-005 default) | Payroll in scope with no explicit client waiver = YES | **Default: YES for all HCM payroll scope** — waiver requires written client acceptance |

### Block E — Commercial Model

| Field | Source | Extraction Rule | Validation Rule | Default / Unknown Behaviour |
|---|---|---|---|---|
| `pricing_type` | Commercial requirements / pricing section | Fixed-Price / T&M / Retainer / Hybrid | AMS CRs are ALWAYS T&M — never fixed price for change requests | UNKNOWN → flag for Commercial Director |
| `contract_term` | RFP commercial section | Term in months; renewal options | — | UNKNOWN → flag for human |
| `cr_model` | RFP change management / commercial section | T&M-Only / Fixed-CR-Allowed | CR threshold = 2 hours standard for AMS | Default: T&M-Only |
| `sla_requirements` | SLA section / service requirements | YES / NO; P1/P2/P3/P4 response times | Standard AMS SLA: P1=1h, P2=4h, P3=1BD, P4=3BD; SAST Mon–Fri 08:00–17:00; response ≠ resolution | Default: YES for AMS |
| `hours_model` | Commercial section | Allocated-Monthly / Per-Incident / Retainer | — | UNKNOWN → flag |

### Block F — Compliance and Governance

| Field | Source | Extraction Rule | Validation Rule | Default / Unknown Behaviour |
|---|---|---|---|---|
| `bbee_requirement` | Compliance / special conditions section | YES if B-BBEE level required | **B-BBEE Level 3 expires 2026-07-31 — OAR-A01 ACTIVE** — any submission on or after that date: flag | Default YES for ZA tenders |
| `bbee_level_required` | Compliance section | Level 1–4 / Any | If Level 2-or-better required and current Level 3 — flag as potential disqualifier | Default: Any acceptable |
| `compliance_documents` | Checklist / compliance annexures | List each required document explicitly | Match against COMPLIANCE_REGISTER.csv; flag any missing document as SEV-2 gap | — |
| `mandatory_references` | Reference section / evaluation criteria | YES if specific references required | Only signed letters in `04_References/` may be cited — AM approval required at each tender | Default: YES; minimum 2 |
| `reference_requirements` | Evaluation criteria | Number, sector, product, rand value threshold | Must be satisfiable from approved reference pool (16 letters); flag if requirements exceed pool | Flag if >4 references required (pool risk) |
| `scoring_criteria` | Evaluation criteria / bid evaluation | Percentage weights per category | Must sum to 100 | UNKNOWN → flag; note for proposal sequencing |
| `evaluation_methodology` | Procurement section | PPPFA-80/20 / PPPFA-90/10 / Quality-Gate-then-Price / Weighted-Scoring | — | UNKNOWN → note for Commercial Director |
| `popia_required` | Compliance section | YES if POPIA policy required | S-65 (POPIA Policy — OAR-E01 PENDING) if YES | UNKNOWN → NO |
| `nda_required` | Submission conditions | YES if NDA required before submission | Process NDA separately from proposal assembly | UNKNOWN → NO |

### Block G — Derived Fields

All derived fields are **auto-populated by TIL engines** after Blocks A–F are complete. They are outputs, not inputs. Manual override requires BU Lead approval and must be documented.

| Derived Field | Engine / Source | Description |
|---|---|---|
| `proposal_pattern` | PROPOSAL_PATTERN_ENGINE.md | Pattern 1–13; combination patterns e.g. "Pattern-13+Pattern-6" |
| `bom_triggers` | TENDER_BOM_LIBRARY.md | BOM IDs active for this tender; drives assumption pack loading |
| `methodology_asset` | METHODOLOGY_SELECTION_ENGINE.md | W2S1-005 (Oracle) / W5-METH-001 (platform-agnostic) / None (AMS/DBA) |
| `project_plan_template` | METHODOLOGY_SELECTION_ENGINE.md | Template ID; None for AMS (Pattern 13) and DBA (Pattern 10) |
| `sections_in_scope` | PROPOSAL_PATTERN_ENGINE.md | Complete list of section IDs for this engagement |
| `sections_excluded` | PROPOSAL_PATTERN_ENGINE.md | Explicit exclusion list with reason codes |
| `capability_assets_required` | CAPABILITY_SELECTION_ENGINE.md | Required assets — always included; governance restrictions recorded |
| `capability_assets_optional` | CAPABILITY_SELECTION_ENGINE.md | Optional assets — BU Lead selection required |
| `reference_pool` | REFERENCE_SELECTION_ENGINE.md | Eligible references scored and ranked; AM approval status |
| `assumption_packs` | BOM_RESOLVER.md | Pack manifest (existing WP17B engine) |

### Block H — Intelligence Quality

| Field | Values | Assembly Impact |
|---|---|---|
| `confidence_overall` | HIGH / MEDIUM / LOW | HIGH = GO; MEDIUM = HOLD pending human answers; LOW = ESCALATE |
| `confidence_per_field` | HIGH / MEDIUM / LOW / UNKNOWN per field | Feeds overall confidence calculation |
| `unknown_fields` | Explicit list | Never suppress; must be empty for HIGH confidence |
| `human_follow_up` | Numbered questions with field reference | Must be resolved before assembly when field is assembly-blocker |
| `governance_flags` | Active restrictions triggered | Always include: Rule 21.4 (DFA), Rule 21.5 (Redpath), B-BBEE expiry, Gold Partner |
| `assembly_blockers` | Subset of unknown_fields | Block assembly gate until resolved |

---

## 4. Confidence Scoring Model

### Per-Field Confidence Levels

| Level | Meaning | Assembly Treatment |
|---|---|---|
| HIGH | Source explicitly states the value; no inference required | Proceed without flag |
| MEDIUM | Value inferred from clear context with high probability | Proceed; note in profile |
| LOW | Value inferred with significant uncertainty | Flag in profile; request human verification |
| UNKNOWN | Cannot determine from available tender documentation | Mark explicitly; check if assembly blocker |

### Overall Confidence Calculation

1. Count fields by confidence level: N_HIGH, N_MEDIUM, N_LOW, N_UNKNOWN
2. Weighted score: (N_HIGH × 3 + N_MEDIUM × 2 + N_LOW × 1) ÷ (Total_Scored_Fields × 3)
3. HIGH overall: score ≥ 80% AND zero UNKNOWN assembly-blockers
4. MEDIUM overall: score 50–79% OR one or more LOW ratings on critical fields
5. LOW overall: score < 50% OR any UNKNOWN assembly-blocker outstanding

### Assembly Gate Rules

| Gate | Trigger Condition | Required Action |
|---|---|---|
| **GO** | Confidence HIGH; zero assembly-blockers | Proceed to Capability Selection (Stage 4) |
| **HOLD** | Confidence MEDIUM; human follow-up questions outstanding | Obtain answers; re-run TIL before proceeding |
| **ESCALATE** | Confidence LOW OR any assembly-blocker unresolved | Escalate to BU Lead; do not begin assembly |

---

## 5. Governance Validation Rules

The following governance rules must be checked against every Tender Profile before the assembly gate is confirmed.

| Rule ID | Field Checked | Rule | Action on Trigger |
|---|---|---|---|
| GOV-001 | `client_name` | DFA: never named externally (Rule 21.4 PERMANENT) | Flag in governance_flags; prevent DFA from appearing in any section |
| GOV-002 | `client_name` | CCBA: never named externally | Flag; prevent CCBA naming |
| GOV-003 | `client_name` | SAA: never named as client | Flag; prevent SAA naming |
| GOV-004 | `client_name` | Redpath Mining: not referenceable (Rule 21.5 PERMANENT) | Flag; exclude from reference pool |
| GOV-005 | `client_name` | Hollywood Bets: AM approval required at each tender | Flag; AM approval must be obtained before reference selection confirmed |
| GOV-006 | Any oracle product | Oracle Gold Partner EXPIRED August 2021: NEVER cite | Flag; ensure W1S1-003 uses "Level 1 Partner" language only |
| GOV-007 | `bbee_requirement` + `submission_deadline` | B-BBEE Level 3 expires 2026-07-31 — OAR-A01 ACTIVE | Flag OAR-A01 for any submission date at or after 2026-07-31 |
| GOV-008 | `oracle_products` includes OIC | Section 13.2 of W3S1-009 NEVER in external submissions | Flag; exclude Section 13.2 from S-19 content |
| GOV-009 | `oracle_products` includes OIC | HIST-018 billing (R825,170) MUST NEVER appear | Flag; prevent HIST-018 reference in any section |
| GOV-010 | `modules_in_scope` includes Compensation | W3S1-005 is Mining sector ONLY (G-001) | Flag if industry ≠ Mining; exclude W3S1-005 from capability selection |
| GOV-011 | Any company overview | Headcount: "more than 50 Senior Consultants" ONLY — never "100+" or "110+" | Flag; validate W1S1-001 headcount language |
| GOV-012 | Oracle capability sections | W4-HCM-004 RETIRED — never selected | Automated deselection; log in capability selection |
| GOV-013 | Oracle capability sections | W1S2-008 ARCHIVED — never selected | Automated deselection |
| GOV-014 | Reference selection | Section 14.2 (W3S1-008) and Section 13.2 (W3S1-009) NEVER in external submissions | Flag at reference and section assembly |
| GOV-015 | `modules_in_scope` includes Compensation (KPMG) | KPMG not named (AM-W4E3-001 ACTIVE — PPM engagement) | Block KPMG reference in PPM/ERP sections |

---

## 6. Mandatory Human Follow-Up Question Templates

When the following fields are UNKNOWN or LOW confidence, use these standard questions:

| Field | Standard Question |
|---|---|
| `engagement_type` | "Is this tender for (a) a new implementation, (b) application managed services on an existing system, or (c) an upgrade/new module addition?" |
| `modules_in_scope` | "Which specific Oracle modules are listed in the RFP scope? Please list all." |
| `integration_scope` | "Does the RFP require any system integrations? If yes, which source/target systems?" |
| `bbee_level_required` | "What B-BBEE level does the RFP require? And what is the submission date?" |
| `pricing_type` | "Is the RFP requesting fixed-price, T&M, or a monthly retainer? Are SLAs specified?" |
| `oracle_version` | "Is this an Oracle EBS engagement? If yes, is the client on EBS 12.1 or 12.2?" |
| `submission_deadline` | "What is the closing date and time for submission?" |
| `reference_requirements` | "Does the RFP specify reference requirements (number, sector, rand value, product)?" |

---

## 7. Example Instance: ARM IT045

```yaml
tender_profile:
  schema_version: "1.0"
  tender_id: "ARM-IT045"
  profile_created: "2025-07-22"
  profile_status: "APPROVED"
  confidence_overall: "HIGH"
  assembly_gate: "GO"

  tender_metadata:
    client_name: "African Rainbow Minerals (ARM)"
    tender_reference: "IT045"
    submission_deadline: "2025-08-10T17:00:00+02:00"
    submission_format: "PDF-Email"
    received_date: "2025-07-21"
    contact_person: "IT Procurement"
    issuing_entity: "African Rainbow Minerals Limited"

  client_profile:
    industry: "Mining"
    sector_subsector: "Diversified Mining (Gold, Platinum, Iron Ore, Manganese, Coal)"
    country: "ZA"
    organisation_size: "Enterprise"
    headcount: "~8,800 employees"
    current_erp: "Oracle-EBS-12.1"

  platform_products:
    primary_platform: "Oracle-EBS"
    oracle_products: [EBS-Finance, EBS-HRMS, OIC]
    non_oracle_products: []
    hosting_model: "On-Premises"
    oracle_version: "EBS 12.1"

  scope_dimensions:
    engagement_type: "AMS"
    modules_in_scope: [EBS-Finance, EBS-HRMS, OIC]
    integration_scope: "YES"
    integration_detail: [OIC-EBS-Payroll, OIC-EBS-Finance]
    migration_scope: "NO"
    migration_detail: ""
    training_scope: "NO"
    dr_in_scope: "NO"
    security_in_scope: "NO"
    support_scope: "YES"
    support_detail: "AMS retainer — EBS Finance, HRMS, OIC; allocated hours model"
    oci_in_scope: "NO"
    parallel_run_required: "NO"

  commercial_model:
    pricing_type: "Retainer"
    contract_term: "24 months initial; renewal options"
    cr_model: "T&M-Only"
    sla_requirements: "YES"
    sla_detail: "P1=1h, P2=4h, P3=1BD, P4=3BD; SAST Mon–Fri 08:00–17:00; response ≠ resolution"
    hours_model: "Allocated-Monthly"

  compliance_governance:
    bbee_requirement: "YES"
    bbee_level_required: "3"
    compliance_documents: [CIPC, TaxClearance, PublicLiability, OracleOPN, BBEE]
    mandatory_references: "YES"
    reference_requirements: "Oracle EBS AMS references preferred; mining sector advantage"
    scoring_criteria: {Technical: 70, Commercial: 20, BBEE: 10}
    evaluation_methodology: "Weighted-Scoring"
    popia_required: "NO"
    nda_required: "YES"

  derived_fields:
    proposal_pattern: "Pattern-13"
    bom_triggers: [BOM-13, BOM-16]
    methodology_asset: "None"
    project_plan_template: "None"
    sections_in_scope: [S-01, S-02, S-03, S-04, S-05, S-06, S-07, S-08, S-09, S-12, S-13, S-14, S-15, S-18, S-19, S-21, S-30, S-31, S-32, S-33, S-36, S-37, S-49, S-50, S-51, S-52, S-55, S-56, S-57, S-58, S-59, S-60, S-67, S-69, S-70, S-71, S-72, S-73, S-74, S-75, S-76, A-01, A-03, A-04, A-05]
    sections_excluded: [S-10, S-11, S-16, S-17, S-20, S-22, S-23, S-24, S-25, S-26, S-27, S-28, S-29, S-34, S-35, S-38, S-39, S-40, S-41, S-42, S-43, S-44, S-45, S-46, S-47, S-48, S-53, S-54, S-61, S-62, S-63, S-64, S-65, S-66, S-68, A-02, A-06]
    capability_assets_required: [W1S1-001, W1S1-003, W1S1-007, W1S1-008, W1S1-009, W2S1-002, W2S1-004]
    capability_assets_optional: [W2S1-003, W4-INT-001]
    reference_pool: [REF-ORA-008, REF-ORA-004, REF-ORA-005, REF-ORA-009]
    assumption_packs: [ERP-123, OCI-174, OIC-104, AMS-84, EBS-SLA-53, EBS-DRM-62]

  intelligence_quality:
    confidence_per_field:
      client_name: HIGH
      engagement_type: HIGH
      modules_in_scope: HIGH
      pricing_type: HIGH
      bbee_level_required: MEDIUM
      oracle_version: HIGH
    unknown_fields: []
    human_follow_up:
      - "1. Confirm exact allocated hours per month for retainer volume — needed for S-52 commercial section"
      - "2. Confirm whether OIC runs on OCI tenant or on-premises — affects hosting model and section scope"
      - "3. B-BBEE Level 3 expires 2026-07-31 — confirm renewal status; OAR-A01 ACTIVE"
    governance_flags:
      - "GOV-001: Rule 21.4 ACTIVE — DFA never referenceable"
      - "GOV-004: Rule 21.5 ACTIVE — Redpath Mining not referenceable"
      - "GOV-006: Oracle Gold Partner EXPIRED 2021 — Level 1 only in S-09"
      - "GOV-007: OAR-A01 — B-BBEE Level 3 expires 2026-07-31; submission date must be confirmed"
      - "GOV-008/009: OIC in scope — Section 13.2 never external; HIST-018 billing never external"
    assembly_blockers: []
```

---

*TENDER_PROFILE_STANDARD.md v1.0 | WP18C.3 — Tender Intelligence Layer | 2026-06-25*  
*Companion documents: TENDER_INTELLIGENCE_RULES.md | PROPOSAL_PATTERN_ENGINE.md | CAPABILITY_SELECTION_ENGINE.md | METHODOLOGY_SELECTION_ENGINE.md | REFERENCE_SELECTION_ENGINE.md*
