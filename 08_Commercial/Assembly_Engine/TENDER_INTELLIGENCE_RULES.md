---
document_id: TENDER-INTELLIGENCE-RULES
title: "Tender Intelligence Rules — Master Processing Standard"
version: "1.0"
status: "Approved — WP18C.3"
created: "2026-06-25"
created_by: "WP18C.3 — Tender Intelligence Layer"
category: "Architecture / Intelligence Layer"
scope: "Master rules document governing TIL processing: the sequence, confidence model, unknown handling, governance enforcement, and downstream trigger matrix. This document controls how a raw tender document becomes a governed Tender Profile that deterministically drives all downstream factory stages."
---

# Tender Intelligence Rules

**Date:** 2026-06-25 | **Version:** 1.0 | **Status:** Approved  
**Work Package:** WP18C.3 — Tender Intelligence Layer  
**Input:** Raw tender document  
**Output:** Approved `[TENDER_ID]_TENDER_PROFILE.md` + `[TENDER_ID]_INTELLIGENCE_REPORT.md`

---

## 1. Purpose and Governing Principle

The Tender Intelligence Layer (TIL) is Stage 0 of the Proposal Factory pipeline. It converts an unstructured tender document into a governed, machine-readable Tender Profile that controls every subsequent stage.

**Governing principle:** Do not use AI judgement where deterministic rules can be defined. Prefer lookup tables. Prefer governed mappings. When a value cannot be determined from the tender document, record it as UNKNOWN — never infer silently, never guess.

**Position in pipeline:**
```
Stage 0: TIL (this document) → Tender Profile
Stage 1: Tender Analysis → Requirement Matrix
Stage 2: BOM Resolution → Pack Manifest
Stage 3: Capability Selection → Capability Selection List
Stage 4: Reference Selection → Reference Selection List
Stage 5: Methodology Selection → Methodology + Template
Stage 6: Assumption Assembly → Assumption Schedule
Stage 7: Section Assembly → Proposal Draft
Stage 8: QA → QA Report
Stage 9: Rendering (future)
```

---

## 2. TIL Processing Sequence

The TIL processes the tender document in a fixed 10-step sequence. Each step has a gate condition. Steps must not be reordered.

---

### Step TIL-01 — Register Tender

**Input:** Raw tender document (PDF / Word / text)  
**Action:** Assign Tender ID; create workspace `09_Active_Tenders/[TENDER_ID]/`; register received date  
**Output:** Tender ID confirmed; workspace active  
**Gate:** File readable; Tender ID assigned

---

### Step TIL-02 — Extract Block A (Tender Metadata)

**Action:** Extract objective facts from the tender document cover page, header, and submission instructions.

**Extraction targets:**
- Client legal name (cover page / letterhead)
- Tender reference number (header / subject)
- Submission deadline (closing date/time)
- Submission format (instructions section)
- Contact person (contacts / enquiries section)
- Issuing entity (procurement authority, if different from client)

**Confidence assignment:** HIGH for explicitly stated values; MEDIUM for inferred values; UNKNOWN if absent.

**Gate:** `client_name` and `submission_deadline` must be extracted or explicitly flagged UNKNOWN with assembly-blocker status.

---

### Step TIL-03 — Extract Block B (Client Profile)

**Action:** Extract client profile from company background, about section, or RFP context.

**Extraction targets:**
- Industry: match to standard taxonomy (Mining / Financial-Services / Retail / Manufacturing / Healthcare / Government / Education / Telecommunications / Other)
- Sector/subsector: free text description
- Country: infer from RFP issuing entity, currency, regulation references
- Organisation size: from employee count or headcount references
- Current ERP: from as-is environment or migration background

**Industry classification rules:**
- "mining" / "minerals" / "resources" → Mining
- "bank" / "insurance" / "financial" / "investment" → Financial-Services
- "retail" / "consumer" / "fashion" / "merchandise" → Retail
- "manufacturing" / "production" / "industrial" → Manufacturing
- "government" / "municipality" / "provincial" / "SOE" → Government
- "university" / "school" / "education" → Education
- "telecom" / "mobile" / "network" / "spectrum" → Telecommunications
- "hospital" / "clinic" / "pharmaceutical" / "health" → Healthcare

**G-001 trigger:** If industry = Mining AND Compensation module is in scope → flag that W3S1-005 may be included. If industry ≠ Mining AND Compensation in scope → W3S1-005 EXCLUDED (G-001 permanent rule).

**Gate:** Industry and country must be resolved (MEDIUM or better) for reference scoring to function.

---

### Step TIL-04 — Extract Block C (Platform and Products)

**Action:** Identify the primary platform and all products in scope.

**Platform classification rules (apply in order):**

| Signal | Platform Assignment |
|---|---|
| "Oracle E-Business Suite" / "EBS" / "R12" / "Oracle 12" | Oracle-EBS |
| "Oracle Fusion" / "Oracle Cloud HCM" / "Oracle Cloud ERP" / "HCM Cloud" | Oracle-Fusion |
| "Acumatica" / "Acumatica Cloud ERP" | Acumatica |
| "BeBanking" / "H2H" / "host-to-host" / "bank integration platform" | BeBanking |
| Multiple platforms confirmed in one RFP | Hybrid |
| Platform name absent but Oracle products mentioned | Oracle-Fusion (default for SaaS Cloud) or UNKNOWN if unclear |

**Oracle product extraction rules:**

| Tender Signal | Oracle Product Tag |
|---|---|
| "Human Capital Management" / "HCM" / "HR Cloud" / "Core HR" | HCM |
| "Financials" / "General Ledger" / "GL" / "Accounts Payable" / "AP" / "AR" | ERP-Financials |
| "Procurement" / "Purchasing" / "iProcurement" / "Sourcing" | ERP-Procurement |
| "Project Portfolio Management" / "PPM" / "Project Costing" | PPM |
| "Integration Cloud" / "OIC" / "Oracle Integration" / "middleware" | OIC |
| "E-Business Suite" / "EBS" / "R12" | EBS |
| "DBA" / "database administration" / "database management" | DBA |
| "Oracle Cloud Infrastructure" / "OCI" / "cloud hosting" / "cloud infrastructure" | OCI |

**Hosting model derivation:**
- Oracle Fusion products + no on-prem mention → OCI (default for Fusion)
- "Oracle EBS" / "R12" + no OCI mention → On-Premises (default for EBS)
- Explicit OCI mention regardless of product → OCI component present
- PaySpace is always a 3rd-party payroll SOR — never an Oracle product in scope

**Gold Partner validation (GOV-006):** Regardless of what the tender says about Oracle partnership requirements, the proposal must NEVER cite Oracle Gold Partner status (expired August 2021). Only "Level 1 Oracle Partner" language is permitted.

**Gate:** `primary_platform` must resolve. UNKNOWN primary_platform = **BLOCK ASSEMBLY**.

---

### Step TIL-05 — Extract Block D (Scope Dimensions)

**Action:** Determine engagement type and all scope dimensions. This is the most consequential step in TIL — it drives pattern selection and section scoping.

**Engagement type classification rules (apply in order):**

| Signal | Engagement Type |
|---|---|
| "implement" / "go-live" / "deployment" / "new system" / "new implementation" | Implementation |
| "support" / "managed services" / "AMS" / "application management" / "maintenance" / "helpdesk" | AMS |
| "upgrade" / "migration from" / "version upgrade" / "patch" | Upgrade |
| "add module" / "extend" / "additional functionality" / "phase 2" (post go-live) | NewModule |
| "integration only" / "OIC only" / "interface" / "middleware" (no ERP/HCM implementation) | Standalone-Integration |
| "DBA" / "database administration" / "database managed service" | Standalone-DBA |
| Implementation scope + AMS scope in same tender | Hybrid (note both in scope) |
| Cannot determine | UNKNOWN → **BLOCK ASSEMBLY** |

**Module scope extraction:** Parse the requirements, scope, and specification sections. Build `modules_in_scope` list using these signals:

| Signal | Module Tag |
|---|---|
| "Core HR" / "Global HR" / "employee record" / "workforce management" | CoreHR |
| "Absence" / "leave management" / "leave" | Absence |
| "Journeys" / "onboarding" / "Journeys and Checklists" | Journeys |
| "Recruiting" / "Talent Acquisition" / "Oracle Recruiting" / "candidate management" | Recruiting |
| "Learning" / "LMS" / "training catalogue" / "course management" | Learning |
| "Talent" / "Performance" / "9-box" / "goal management" / "succession" | Talent |
| "Compensation" / "salary review" / "merit cycle" | Compensation |
| "AI Skills" / "Dynamic Skills" / "Oracle Grow" | AISkills |
| "Financials" / "GL" / "AP" / "AR" / "Fixed Assets" / "Cash Management" | Financials |
| "Procurement" / "Purchasing" / "sourcing" | Procurement |
| "PPM" / "project costing" / "project management" | PPM |
| "OIC" / "integration" / "middleware" | OIC |
| "EBS Finance" / "Oracle Financials EBS" | EBS-Finance |
| "EBS HRMS" / "Oracle HRMS" / "EBS HR" | EBS-HRMS |
| "Acumatica Financials" / "Acumatica Finance" | Acumatica-Financials |
| "Acumatica Distribution" / "distribution modules" | Acumatica-Distribution |
| "Acumatica Manufacturing" / "manufacturing ERP" | Acumatica-Manufacturing |
| "Supplier Payments" / "H2H supplier" | BeBanking-Supplier |
| "Payroll Payments" / "H2H payroll" | BeBanking-Payroll |
| "Forex" / "FX payments" | BeBanking-Forex |

**Scope dimension defaults:**
- `parallel_run_required`: If `modules_in_scope` includes any payroll-related module OR HCM payroll interface → default YES per HCM-CUT-005; waiver requires written client acceptance
- `training_scope`: Default YES for all implementations
- `migration_scope`: Default YES for implementations (LOW confidence); Opening Balances Only is standard; Full History = CR
- `oci_in_scope`: Derive from hosting_model; if Fusion HCM/ERP → YES by default

**Gate:** `engagement_type` must resolve. UNKNOWN = **BLOCK ASSEMBLY**.

---

### Step TIL-06 — Extract Block E (Commercial Model)

**Action:** Extract commercial terms from the RFP commercial, pricing, and service-level sections.

**Pricing type rules:**
- Fixed lump sum / fixed price → Fixed-Price
- "time and material" / "T&M" / "hourly rate" → T&M
- "monthly retainer" / "monthly fee" / "retainer basis" → Retainer
- Fixed implementation + AMS retainer → Hybrid
- AMS change requests: always T&M regardless of overall pricing type

**SLA rules:**
- Standard AMS SLA defaults (P1=1h, P2=4h, P3=1BD, P4=3BD) are used unless the RFP specifies differently
- Response time ≠ resolution time — this language must always be preserved in S-70/S-71
- 24x7 coverage: EXCLUDED unless explicitly contracted — flag if RFP requires it

**Gate:** `pricing_type` should be resolved; UNKNOWN flagged for Commercial Director.

---

### Step TIL-07 — Extract Block F (Compliance and Governance)

**Action:** Extract compliance requirements and apply all governance rules.

**Compliance extraction:**
- Parse compliance annexures / checklist sections
- List every required document against COMPLIANCE_REGISTER.csv
- Any document required by RFP but missing from COMPLIANCE_REGISTER → SEV-2 gap

**Governance rule application (all permanent):**
- Apply GOV-001 through GOV-015 from TENDER_PROFILE_STANDARD.md Section 5
- Each triggered rule is recorded in `governance_flags`
- B-BBEE expiry check: compare `submission_deadline` against 2026-07-31 → flag OAR-A01 if at risk
- KPMG flag: applies to PPM (BOM 12) engagement — check BOM triggers after TIL-09

**Reference requirement extraction:**
- Identify specific reference requirements (number, sector, product, rand value threshold, format)
- Record in `reference_requirements` for the Reference Selection Engine

**Gate:** All governance rules processed; all flags recorded; compliance gaps identified.

---

### Step TIL-08 — Derive Block G (Pattern + BOM + Section Scope)

**Action:** Using completed Blocks A–F, invoke the three TIL derivation engines.

**Derivation sequence (strict order):**

1. **PROPOSAL_PATTERN_ENGINE.md** — classify pattern from engagement_type + modules_in_scope + platform
2. **TENDER_BOM_LIBRARY.md** — resolve BOM triggers from pattern + modules_in_scope + support_scope
3. **PROPOSAL_PATTERN_ENGINE.md** — apply section scoping rules for this pattern → sections_in_scope + sections_excluded
4. **CAPABILITY_SELECTION_ENGINE.md** — resolve capability_assets_required + capability_assets_optional from BOM triggers
5. **METHODOLOGY_SELECTION_ENGINE.md** — resolve methodology_asset + project_plan_template from pattern
6. **REFERENCE_SELECTION_ENGINE.md** — score and rank eligible references → reference_pool
7. **BOM_RESOLVER.md** (existing WP17B engine) — resolve assumption_packs from BOM triggers

**Gate:** All seven derived fields populated; pattern confirmed; section scope confirmed.

---

### Step TIL-09 — Assess Block H (Intelligence Quality)

**Action:** Calculate confidence ratings and flag unknowns.

**Per-field confidence rating:**
- HIGH: Source document explicitly states the value
- MEDIUM: Inferred from clear context signals
- LOW: Inferred with significant uncertainty
- UNKNOWN: No basis for determination

**Assembly-blockers (fields that must be resolved before assembly can proceed):**
- `client_name` = UNKNOWN
- `submission_deadline` = UNKNOWN
- `primary_platform` = UNKNOWN
- `engagement_type` = UNKNOWN

**Overall confidence calculation:** See TENDER_PROFILE_STANDARD.md Section 4.

**Human follow-up questions:** Generate one question per UNKNOWN or LOW-confidence critical field, using the standard templates from TENDER_PROFILE_STANDARD.md Section 6.

**Gate:** Confidence calculated; unknowns listed; follow-up questions generated; assembly gate set.

---

### Step TIL-10 — Approve Tender Profile

**Action:** BU Lead reviews and approves the Tender Profile before assembly begins.

**Approval requirements:**
- All assembly-blockers resolved (or accepted with documented rationale)
- Governance flags reviewed and acknowledged
- Human follow-up questions answered or explicitly deferred
- Profile status changed from DRAFT → APPROVED

**Gate:** `profile_status: APPROVED` + `assembly_gate: GO` (or HOLD with documented reason)

---

## 3. Downstream Trigger Matrix

The Downstream Trigger Matrix maps Tender Profile field values to specific factory outcomes. This is the core intelligence layer: it converts human-readable profile facts into machine-readable factory instructions.

### 3.1 Engagement Type → Pattern + Section Scope

| `engagement_type` | Pattern | Key Sections IN | Key Sections OUT |
|---|---|---|---|
| Implementation | Pattern 1–9, 11 (platform-dependent) | S-34, S-35, S-39, S-40, S-41, S-42, S-43 | S-70, S-71, S-72, S-73, S-74, S-75, S-76 |
| AMS | Pattern 13 | S-70, S-71, S-72, S-73, S-74, S-75, S-76 | S-34, S-35, S-38, S-39, S-40, S-41, S-42, S-43 |
| Standalone-Integration | Pattern 6 | S-19, S-36, S-37 | S-34, S-35, S-39–43, S-70–76 |
| Standalone-DBA | Pattern 10 | S-20, S-36, S-37 | S-34, S-35, S-39–43, S-70–76 |
| BeBanking H2H | Pattern 12 | S-29, S-36, S-37 | S-34 (methodology not standard), S-70–76 |
| Hybrid (Impl+AMS) | Pattern combination | Both implementation + AMS sections | None from either set |

### 3.2 Platform + Products → BOM Triggers

| Platform / Products | BOM Trigger(s) |
|---|---|
| Oracle EBS (Finance + HRMS) | BOM-13 |
| Oracle EBS + OIC | BOM-13 + BOM-9 |
| Oracle EBS + AMS | BOM-13 + BOM-16 |
| Oracle EBS + AMS + OIC | BOM-13 + BOM-9 + BOM-16 |
| Oracle Fusion HCM Full Suite | BOM-1 |
| Oracle Fusion HCM Base (Core HR + modules ≤3) | BOM-2 |
| + Recruiting module | BOM-3 |
| + Learning module | BOM-4 |
| + Talent module | BOM-5 |
| + Compensation module | BOM-6 (Mining sector ONLY — G-001) |
| + Journeys / Onboarding | BOM-7 |
| + AI Skills | BOM-8 |
| + OIC Integration | BOM-9 |
| Oracle Fusion ERP (Financials + Procurement) | BOM-10 + BOM-11 |
| Oracle Fusion Financials only | BOM-10 |
| Oracle Fusion Procurement only | BOM-11 |
| Oracle PPM | BOM-12 |
| Oracle DBA (standalone) | BOM-13 (EBS-related) |
| Acumatica ERP | BOM-14 |
| BeBanking | BOM-15 |
| AMS (any platform) | BOM-16 |

**Standard Corporate Block (always included regardless of BOM):** W1S1-001/007/008/009 + COMP-001/002/004/011

### 3.3 Pattern → Methodology Asset + Project Plan Template

| Pattern | Methodology Asset | Template | Excluded Sections |
|---|---|---|---|
| Pattern 1 (HCM Full Suite, Single) | W2S1-005 | PT-01 | S-70–76 |
| Pattern 2 (HCM Full Suite, Phased) | W2S1-005 | PT-02 | S-70–76 |
| Pattern 3 (HCM + Payroll Interface) | W2S1-005 | PT-03 | S-70–76 |
| Pattern 4 (Recruiting Standalone) | W2S1-005 | PT-04 | S-70–76; S-40 (no migration standard) |
| Pattern 5 (Learning Standalone) | W2S1-005 | PT-05 | S-70–76 |
| Pattern 6 (OIC Standalone) | W2S1-005 | PT-06 | S-34, S-35, S-70–76 |
| Pattern 7 (ERP Multi-Module) | W2S1-005 | PT-07 | S-70–76 |
| Pattern 8 (ERP Single Module) | W2S1-005 | PT-08 | S-70–76 |
| Pattern 9 (Oracle EBS Implementation) | W2S1-005 | PT-09 | S-70–76 |
| Pattern 10 (Oracle DBA/Managed Services) | None | None | S-34, S-35, S-70–76 |
| Pattern 11 (Acumatica ERP) | W5-METH-001 | PT-11 | S-70–76 |
| Pattern 12 (BeBanking H2H) | W5-METH-001 | PT-12 | S-34 (optional), S-70–76 |
| Pattern 13 (AMS Onboarding) | None | None | S-34, S-35, S-38, S-39, S-40, S-41, S-42, S-43 |

### 3.4 Industry + Module → Governance Deselection

| Industry | Module | Rule | Deselection |
|---|---|---|---|
| NOT Mining | Compensation | G-001 PERMANENT | Exclude W3S1-005 from capability selection |
| ANY | PPM (KPMG) | AM-W4E3-001 ACTIVE | Use anonymous reference only; no KPMG naming |
| ANY | Mr Price reference | C-W3-002 | REF-ORA-006 = Learning Cloud scope ONLY |
| ANY | Hollywood Bets | Rule HB | AM approval required before reference use |

### 3.5 Country + Submission Date → Compliance Triggers

| Condition | Trigger |
|---|---|
| `country = ZA` | B-BBEE certificate required; S-59; A-05 |
| `submission_deadline ≥ 2026-07-31` | OAR-A01 — B-BBEE Level 3 expiry flag; ESCALATE |
| `country ≠ ZA` | B-BBEE section excluded or noted as not applicable |
| `popia_required = YES` | S-65 in scope — but OAR-E01 PENDING; flag as gap |
| `nda_required = YES` | NDA process before assembly; separate action |

### 3.6 Scope Dimension → Additional Section Triggers

| Scope Dimension | Value | Additional Sections Triggered |
|---|---|---|
| `dr_in_scope` | YES | S-44 — but EMPTY (GAP-013); flag SEV-2 gap |
| `security_in_scope` | YES | S-45 — partial; OCI pack covers SEC assumptions |
| `oci_in_scope` | YES | S-22 (OCI Infrastructure) — AI-GENERATE; no standalone narrative (GAP-004) |
| `migration_scope` | YES | S-40; DAT/MIG assumptions in scope |
| `training_scope` | YES | S-41; TRN assumptions in scope |
| `parallel_run_required` | YES | CUT assumptions include HCM-CUT-005 parallel run language |
| `bbee_level_required` | Level-2-or-better AND current Level-3 | Flag potential disqualifier; escalate |

---

## 4. Unknown Field Handling Protocol

When a field cannot be determined from the tender document:

### Rule U-1: Always explicit
Record the unknown in `unknown_fields`. Never suppress. Never default silently.

### Rule U-2: Assess blocking status
Determine if the unknown is an assembly-blocker:
- YES (blocker): client_name, submission_deadline, primary_platform, engagement_type
- NO (non-blocker): headcount, oracle_version, evaluation_methodology, contact_person

### Rule U-3: Generate a question
For every unknown field, generate a standard follow-up question using the templates in TENDER_PROFILE_STANDARD.md Section 6.

### Rule U-4: Set assembly gate appropriately
- Zero assembly-blockers + zero unknowns → GO
- Zero assembly-blockers + unknowns present (non-blockers) → HOLD (obtain answers)
- Any assembly-blocker unresolved → ESCALATE

### Rule U-5: Document the escalation
If escalating, document which field is unknown, why it is a blocker, and who is responsible for resolving it (BU Lead or Account Manager).

---

## 5. TIL Output Documents

Every TIL run produces two documents:

### Document 1: `[TENDER_ID]_TENDER_PROFILE.md`
- Structured YAML conforming to TENDER_PROFILE_STANDARD.md schema
- Saved to `09_Active_Tenders/[TENDER_ID]/`
- Status must reach APPROVED before assembly proceeds

### Document 2: `[TENDER_ID]_INTELLIGENCE_REPORT.md`
- Narrative summary of TIL processing
- Lists all governance flags with explanation
- Lists all human follow-up questions with priority
- Records assembly gate decision and rationale
- Saved to `09_Active_Tenders/[TENDER_ID]/`

---

## 6. TIL Quality Checks

Before marking the Tender Profile as APPROVED, verify:

| Check | Pass Condition |
|---|---|
| All Block A fields present or explicitly UNKNOWN | All fields have a value or UNKNOWN label |
| `primary_platform` resolved | Not UNKNOWN |
| `engagement_type` resolved | Not UNKNOWN |
| Governance rules checked | All 15 GOV rules applied; flags recorded |
| B-BBEE expiry checked | OAR-A01 status assessed against submission_deadline |
| Derived fields populated | All 10 Block G fields non-empty |
| Assembly gate set | GO / HOLD / ESCALATE — not blank |
| Unknown fields listed | `unknown_fields` = complete list, not empty array unless none |
| Human follow-up generated | One question per UNKNOWN/LOW critical field |

---

*TENDER_INTELLIGENCE_RULES.md v1.0 | WP18C.3 — Tender Intelligence Layer | 2026-06-25*  
*Companion: TENDER_PROFILE_STANDARD.md | PROPOSAL_PATTERN_ENGINE.md | CAPABILITY_SELECTION_ENGINE.md*
