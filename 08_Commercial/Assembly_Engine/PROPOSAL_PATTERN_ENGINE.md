---
document_id: PROPOSAL-PATTERN-ENGINE
title: "Proposal Pattern Engine — Classification and Section Scoping Rules"
version: "1.0"
status: "Approved — WP18C.3"
created: "2026-06-25"
created_by: "WP18C.3 — Tender Intelligence Layer"
category: "Architecture / Intelligence Layer"
scope: "Defines the deterministic classification logic for all 13 delivery patterns; section inclusion and exclusion rules per engagement type (AO-002); and combination pattern handling. Input: completed Tender Profile. Output: proposal_pattern + sections_in_scope + sections_excluded."
---

# Proposal Pattern Engine

**Date:** 2026-06-25 | **Version:** 1.0 | **Status:** Approved  
**Work Package:** WP18C.3 — Tender Intelligence Layer  
**Input:** `[TENDER_ID]_TENDER_PROFILE.md` (Blocks C, D)  
**Output:** `proposal_pattern`, `sections_in_scope`, `sections_excluded`

---

## 1. Purpose

The Proposal Pattern Engine determines, from the Tender Profile, which of the 13 standard delivery patterns applies to a tender. The pattern assignment drives:
- Section inclusion and exclusion (AO-002 scoping rules)
- Methodology asset selection (via METHODOLOGY_SELECTION_ENGINE.md)
- Project plan template selection
- Resource model for team section (S-46)

Classification is **deterministic**. Given the same Tender Profile inputs, the engine must always produce the same pattern. Judgement is not applied — if the inputs are ambiguous, the pattern is flagged UNKNOWN and escalated to the BU Lead.

---

## 2. Pattern Classification — Decision Tree

Pattern classification is a three-level hierarchy. Apply levels in order: a match at Level 1 overrides all lower levels.

### Level 1 — Engagement Type

| `engagement_type` | Candidate Patterns |
|---|---|
| AMS | Pattern 13 (all platforms) |
| Standalone-DBA | Pattern 10 |
| Standalone-Integration | Pattern 6 |
| Implementation | Proceed to Level 2 |
| Upgrade | Pattern 9 (EBS) or platform-matched Implementation pattern |
| NewModule | Same as Implementation for that module |
| Hybrid (Implementation + AMS) | Combination — see Section 5 |
| BeBanking standalone | Pattern 12 |
| UNKNOWN | ESCALATE — pattern cannot be determined |

### Level 2 — Primary Platform

| `primary_platform` (for Implementation) | Candidate Patterns |
|---|---|
| Oracle-EBS | Pattern 9 |
| Oracle-Fusion | Proceed to Level 3 |
| Acumatica | Pattern 11 |
| BeBanking | Pattern 12 |
| Hybrid | Combination — see Section 5 |

### Level 3 — Module Scope (Oracle Fusion Implementation only)

| Module Configuration | Pattern |
|---|---|
| HCM: ≥4 modules AND single go-live | Pattern 1 |
| HCM: ≥4 modules AND phased go-live (2+ waves) | Pattern 2 |
| HCM: Core HR + OIC ↔ PaySpace integration as primary | Pattern 3 |
| HCM: Recruiting Cloud only (no other HCM) | Pattern 4 |
| HCM: Learning Cloud only (no other HCM) | Pattern 5 |
| HCM: ≤3 HCM modules (not Recruiting or Learning standalone) | Pattern 1 (simplified) |
| ERP: Financials + Procurement (or any 2+ ERP modules) | Pattern 7 |
| ERP: Single module only | Pattern 8 |
| PPM only | Pattern 8 (single module) |
| OIC standalone (no HCM/ERP implementation) | Pattern 6 |

**HCM module count threshold note:** 4 modules = any 4 of CoreHR, Absence, Journeys, Recruiting, Learning, Talent, Compensation, AISkills, Payroll-Interface, OIC. CoreHR is always counted as one module.

---

## 3. Pattern Reference Table

| Pattern | Name | Platform | Engagement | Typical Duration | Methodology |
|---|---|---|---|---|---|
| 1 | Oracle HCM Full Suite — Single Go-Live | Oracle-Fusion | Implementation | 35–46 weeks | W2S1-005 |
| 2 | Oracle HCM Full Suite — Phased Go-Live | Oracle-Fusion | Implementation | 44–58 weeks | W2S1-005 |
| 3 | Oracle HCM Core + Payroll Interface | Oracle-Fusion | Implementation | 24–38 weeks | W2S1-005 |
| 4 | Oracle Recruiting Cloud (Standalone) | Oracle-Fusion | Implementation | 19–29 weeks | W2S1-005 |
| 5 | Oracle Learning Cloud (Standalone) | Oracle-Fusion | Implementation | 18–26 weeks | W2S1-005 |
| 6 | Oracle OIC Integration (Standalone) | Oracle-OIC | Implementation | 16–23 weeks | W2S1-005 |
| 7 | Oracle Fusion ERP (Multi-Module) | Oracle-Fusion | Implementation | 34–42 weeks | W2S1-005 |
| 8 | Oracle Fusion ERP (Single Module) | Oracle-Fusion | Implementation | 21–29 weeks | W2S1-005 |
| 9 | Oracle EBS Implementation | Oracle-EBS | Implementation | 33–41 weeks | W2S1-005 |
| 10 | Oracle DBA / Managed Services | Oracle-EBS | DBA-Managed | Ongoing monthly | None |
| 11 | Acumatica ERP | Acumatica | Implementation | 24–34 weeks | W5-METH-001 |
| 12 | BeBanking H2H | BeBanking | Implementation | 21–30 weeks | W5-METH-001 |
| 13 | AMS / Managed Services Onboarding | Any | AMS | Ongoing monthly | None |

---

## 4. Section Scoping Rules (AO-002)

These are the engagement-type scoping rules identified in WP18C.1 Automation Opportunity AO-002. They convert the WP18C finding that "AMS excludes S-34/35/39–43 and implementation excludes S-70–76" into a deterministic, governed lookup table.

### 4.1 Engagement-Type Exclusion Rules

| Engagement Type | Excluded Sections | Reason |
|---|---|---|
| AMS (Pattern 13) | S-34, S-35 | AMS has no implementation methodology or project timeline |
| AMS (Pattern 13) | S-38 | **SI-001 FIX:** S-38 (Change Control Framework) duplicates S-73 (Change Request Process) for AMS; S-73 is the AMS-correct version — S-38 is excluded to prevent duplication |
| AMS (Pattern 13) | S-39, S-40, S-41, S-42, S-43 | No CRP/SIT/UAT, data migration, training, cutover, or hypercare for AMS onboarding |
| AMS (Pattern 13) | S-46, S-47, S-48 | AMS resource model uses shared pool — named team and CVs not applicable |
| Implementation (Patterns 1–9, 11, 12) | S-70, S-71, S-72, S-73, S-74, S-75, S-76 | AMS support sections not relevant for implementation proposals |
| Standalone-DBA (Pattern 10) | S-34, S-35, S-39, S-40, S-41, S-42, S-43, S-70–76 | DBA has its own delivery model; full methodology and AMS sections not applicable |
| Standalone-Integration (Pattern 6) | S-39, S-40, S-41, S-42, S-70–76 | No full lifecycle; testing strategy per Pattern 6 only; no AMS sections |
| BeBanking (Pattern 12) | S-70–76 | H2H implementation; not a managed service |

### 4.2 Platform-Conditional Sections

These sections are included ONLY when the corresponding platform or product is in scope.

| Section ID | Section Name | Condition | Include When |
|---|---|---|---|
| S-09 | Oracle Partnership | COND-ORA | `oracle_products` non-empty |
| S-10 | Acumatica Partnership | COND-ACU | `primary_platform = Acumatica` |
| S-11 | BeBanking Product Overview | COND-BB | `primary_platform = BeBanking` |
| S-16 | Oracle Fusion HCM Capability | COND-HCM | `oracle_products` includes HCM |
| S-17 | Oracle Fusion ERP Capability | COND-ERP | `oracle_products` includes ERP-Financials, ERP-Procurement, or PPM |
| S-18 | Oracle EBS Capability | COND-EBS | `oracle_products` includes EBS |
| S-19 | Oracle OIC / Integration | COND-OIC | `oracle_products` includes OIC |
| S-20 | Oracle DBA Capability | COND-DBA | `oracle_products` includes DBA |
| S-21 | Oracle Managed Services | COND-AMS | `engagement_type = AMS` AND `primary_platform` includes Oracle |
| S-22 | OCI Infrastructure | COND-OCI | `oci_in_scope = YES` |
| S-23 | Acumatica Financials | COND-ACU | `modules_in_scope` includes Acumatica-Financials |
| S-24 | Acumatica Distribution | COND-ACU | `modules_in_scope` includes Acumatica-Distribution |
| S-25 | Acumatica Manufacturing | COND-ACU | `modules_in_scope` includes Acumatica-Manufacturing |
| S-26 | Acumatica CRM | COND-ACU | `modules_in_scope` includes Acumatica-CRM |
| S-27 | Acumatica Other Modules | COND-ACU | `modules_in_scope` includes other Acumatica modules |
| S-28 | Acumatica Managed Services | COND-ACU-AMS | `primary_platform = Acumatica` AND `engagement_type = AMS` |
| S-29 | BeBanking H2H Banking | COND-BB | `primary_platform = BeBanking` |
| S-40 | Data Migration | COND-MIG | `migration_scope = YES` |
| S-44 | Disaster Recovery | OPT | `dr_in_scope = YES` — **EMPTY ASSET (GAP-013)**; flag SEV-2 |
| S-45 | Security Architecture | COND-OCI | `security_in_scope = YES` |
| S-59 | B-BBEE Certificate | M-SA | `country = ZA` |
| S-70 | Support Model | COND-AMS | `engagement_type = AMS` |
| S-71 | SLA Framework | COND-AMS | `engagement_type = AMS` |
| S-72 | Incident Management | COND-AMS | `engagement_type = AMS` |
| S-73 | Change Request Process | COND-AMS | `engagement_type = AMS` |
| S-74 | Resource Model (AMS) | COND-AMS | `engagement_type = AMS` |
| S-75 | Release Management | COND-AMS | `engagement_type = AMS` |
| S-76 | Monitoring and Reporting | COND-AMS | `engagement_type = AMS` |
| A-02 | Consultant CVs | OPT | Named team required (BU Lead decides); always PLACEHOLDER |
| A-05 | B-BBEE Certificate | M-SA | `country = ZA` |

### 4.3 Commercial Scope Sections

| Section ID | Section Name | Include Condition |
|---|---|---|
| S-30 | Scope of Work — Inclusions | M-FIXED — include for all fixed-price and AMS tenders |
| S-31 | Scope of Work — Exclusions | M-FIXED — include for all fixed-price and AMS tenders |
| S-33 | Dependencies | M-FIXED — include for all structured proposals |
| S-38 | Change Control Framework | M-FIXED for Implementation; EXCLUDED for AMS (see SI-001 fix above) |
| S-42 | Cutover / Go-Live Plan | M-FIXED for Implementation; not applicable for AMS |
| S-49 | Key Assumptions (Body) | M-FIXED — all proposals |
| S-51 | Commercial Assumptions | M-FIXED — all proposals |
| S-52 | Commercials / Pricing | M-FIXED — all proposals (PLACEHOLDER for Commercial Director) |
| S-53 | Rate Card Basis | OPT — only if RFP requests rate card |
| S-54 | Estimation Basis | OPT — only if RFP requests estimation methodology |

---

## 5. Combination Pattern Rules

Some tenders span multiple patterns. The following combination rules apply:

### Rule C-1: Implementation + AMS in same tender
When `scope_dimensions.support_scope = YES` AND `engagement_type = Implementation`:
- Assign both pattern codes: e.g. `"Pattern-9+Pattern-13"` (EBS implementation + AMS onboarding)
- Include BOTH implementation sections AND AMS sections
- S-38 (Change Control): INCLUDE for implementation scope
- S-73 (Change Request Process): INCLUDE for AMS scope
- Both S-38 and S-73 are included and must be clearly labelled as applying to their respective scopes

### Rule C-2: Multi-platform tender (Hybrid)
When `primary_platform = Hybrid` (confirmed multi-platform in one tender):
- Assign one pattern per platform
- Include all relevant conditional sections for each platform
- Example: Oracle EBS (BOM 13) + BeBanking (BOM 15) → Pattern-9+Pattern-12

### Rule C-3: OIC within HCM or ERP implementation
When `oracle_products` includes OIC AND another Oracle product:
- Do NOT assign Pattern 6 (OIC standalone)
- OIC is integrated within the primary pattern (1–9)
- S-19 (Oracle OIC) is triggered by COND-OIC; S-45 (Security) if OCI also in scope

### Rule C-4: Module additions to live system (NewModule)
When `engagement_type = NewModule`:
- Assign the Implementation pattern for that module
- Flag that several sections may be abbreviated (e.g. Company Overview is shorter; fewer BOM triggers)
- Mark derived pattern as e.g. `"Pattern-4-NewModule"` for traceability

### Rule C-5: Upgrade
When `engagement_type = Upgrade` AND `primary_platform = Oracle-EBS`:
- Assign Pattern 9
- Note upgrade characteristics (no full SDD; reduced data migration; DBA involvement)

---

## 6. Section Scope by Pattern — Quick Reference Tables

### 6.1 Patterns 1–9 (Oracle Fusion and EBS Implementation)

| Section Range | Included for Patterns 1–9 | Notes |
|---|---|---|
| S-01 to S-12 (Corporate) | All M-ALL sections; COND sections per platform | S-09 always for Oracle; S-10/S-11 excluded |
| S-13 to S-15 (Understanding/Solution Overview) | Yes — M-ALL | S-13 AI-GENERATE; S-14 AI-assisted |
| S-16 to S-21 (Capability) | COND — per platform and module | S-16 HCM; S-17 ERP; S-18 EBS; S-19 OIC; S-20 DBA; S-21 AMS excluded |
| S-22 (OCI) | Only if `oci_in_scope = YES` | AI-GENERATE; GAP-004 active |
| S-23 to S-29 (Acumatica/BeBanking) | Excluded | Wrong platform |
| S-30 to S-43 (Scope and Delivery) | S-30, S-31, S-32, S-33, S-34, S-35, S-36, S-37, S-38, S-39, S-42, S-43 included | S-40 only if migration; S-41 only if training explicit |
| S-44, S-45 (DR/Security) | Only if `dr_in_scope = YES` / `security_in_scope = YES` | S-44 EMPTY — GAP-013 |
| S-46 to S-48 (People) | S-46 yes; S-47/S-48 if CVs required | CVs always PLACEHOLDER (ADR-001) |
| S-49 to S-54 (Commercial) | S-49, S-50, S-51, S-52 always; S-53/S-54 optional | S-52 always PLACEHOLDER |
| S-55 to S-66 (Compliance) | S-55–60 always; S-61–66 conditional | S-62 OPN; S-65/S-66 only if obtained |
| S-67 to S-69 (References) | S-67 always; S-68/S-69 optional | AM approval required |
| S-70 to S-76 (AMS/Support) | **EXCLUDED for all Implementation patterns** | — |
| A-01 to A-06 (Appendices) | A-01, A-04, A-05 always; others conditional | A-02 CVs always PLACEHOLDER |

### 6.2 Pattern 13 (AMS — All Platforms)

| Section Range | Included for Pattern 13 | Notes |
|---|---|---|
| S-01 to S-12 (Corporate) | All M-ALL; COND per platform | S-09 for Oracle; S-10 for Acumatica; S-11 for BeBanking |
| S-13 to S-15 | Yes | S-13 AI-GENERATE |
| S-16 to S-21 (Capability) | Platform-appropriate capability sections | S-21 (Oracle Managed Services) always for Oracle AMS |
| S-22 (OCI) | Only if OCI in scope | Usually excluded for EBS AMS |
| S-30 to S-33 (Scope inclusions/exclusions/deliverables/dependencies) | Yes | |
| S-34, S-35 | **EXCLUDED** | No implementation methodology or project plan for AMS |
| S-36, S-37 (Governance, RAID) | Yes | AMS still requires governance framework |
| S-38 | **EXCLUDED (SI-001 FIX)** | Replaced by S-73 for AMS context |
| S-39 to S-43 | **EXCLUDED** | No CRP/SIT/UAT, migration, training, cutover for AMS |
| S-44, S-45 | Excluded unless explicitly required | |
| S-46, S-47, S-48 (People/CVs) | **EXCLUDED** | AMS uses shared pool; no named team commitment |
| S-49 to S-52 (Commercial/Assumptions) | Yes | S-52 always PLACEHOLDER |
| S-55 to S-60 (Compliance) | Yes | B-BBEE check (OAR-A01 if near expiry) |
| S-67 to S-69 (References) | S-67 always; S-69 optional | AM approval required |
| S-70 to S-76 (AMS/Support) | **ALL INCLUDED** | Core AMS sections |
| A-01 to A-06 | A-01, A-03, A-04, A-05 | A-02 CVs excluded for AMS |

### 6.3 Pattern 10 (Oracle DBA / Managed Services) and Pattern 11 (Acumatica)

**Pattern 10 (DBA):**
- INCLUDE: S-01–12, S-13–15, S-20, S-30–33, S-36, S-37, S-49–52, S-55–60, S-67, A-01, A-04, A-05
- EXCLUDE: S-34, S-35, S-38–43, S-70–76, S-16–19, S-21, S-22

**Pattern 11 (Acumatica):**
- INCLUDE: S-01–12 (S-10 instead of S-09), S-13–15, S-23–28 (per modules), S-30–43, S-46–52, S-55–60, S-67, A-01–A-06
- EXCLUDE: S-09, S-16–22 (Oracle-specific), S-29, S-70–76

**Pattern 12 (BeBanking H2H):**
- INCLUDE: S-01–12 (S-11), S-13–15, S-29, S-30–37, S-49–52, S-55–60, S-67, A-01, A-04, A-05
- EXCLUDE: S-70–76; S-34 optional (methodology limited for BeBanking)

---

## 7. Section Order Corrections (SI-005, SI-006)

Two structural ordering issues identified in WP18C.1 are encoded here as rules:

**SI-005 — References before AMS model:**  
For Pattern 13 (AMS), the section order must be:
`Corporate → Understanding → Solution Capability → Scope (S-30–37) → AMS Support Model (S-70–76) → Commercial (S-49–52) → Compliance (S-55–66) → References (S-67–69) → Appendices`

References appear AFTER the AMS model sections, not before. Reference placement in the document should follow section 10 (post-commercial), not section 5.

**SI-006 — Assumptions before commercial:**  
For all patterns, Key Assumptions (S-49) must appear BEFORE Commercials/Pricing (S-52). The standard order within the Commercial section is:
`S-49 (Key Assumptions Body) → S-50 (Risk Register) → S-51 (Commercial Assumptions) → S-52 (Pricing) → S-53/S-54 (optional rate/estimation)`

---

## 8. Pattern Confidence and Override

### When pattern assignment is uncertain
If Level 3 classification produces two candidate patterns (e.g. Pattern 1 vs Pattern 2 for HCM — single or phased unclear):
1. Record both candidates in profile: `"Pattern-1 OR Pattern-2 — pending BU Lead confirmation"`
2. Set `confidence_per_field.proposal_pattern = MEDIUM`
3. Generate human follow-up question: "Is the HCM implementation a single go-live or phased across multiple waves?"
4. Do not proceed to section scoping until confirmed

### Overriding a derived pattern
If BU Lead overrides the derived pattern:
- Document the override in the Tender Profile with rationale
- Re-derive `sections_in_scope` and `sections_excluded` from the override pattern
- Record as deviation in the Tender Intelligence Report

---

## 9. ARM IT045 Example

**Tender Profile inputs:**  
- `engagement_type`: AMS  
- `primary_platform`: Oracle-EBS  
- `modules_in_scope`: [EBS-Finance, EBS-HRMS, OIC]  
- `support_scope`: YES  

**Level 1 decision:** `engagement_type = AMS` → **Pattern 13**

**Section scoping result:**

| Category | Decision |
|---|---|
| S-34, S-35 | EXCLUDED — no implementation methodology for AMS |
| S-38 | EXCLUDED — SI-001 fix; replaced by S-73 |
| S-39 to S-43 | EXCLUDED — no CRP/SIT/UAT/migration/training/cutover |
| S-46, S-47, S-48 | EXCLUDED — shared pool; no named team |
| S-70 to S-76 | INCLUDED — core AMS delivery sections |
| S-18 (Oracle EBS Capability) | INCLUDED — COND-EBS triggered |
| S-19 (Oracle OIC) | INCLUDED — COND-OIC triggered |
| S-21 (Oracle Managed Services) | INCLUDED — COND-AMS triggered |
| S-09 (Oracle Partnership) | INCLUDED — COND-ORA |
| S-10, S-11 | EXCLUDED — wrong platform |
| S-59, A-05 | INCLUDED — M-SA (country = ZA) |

**Net sections in scope:** 43 sections (vs 82 total; 39 excluded)

---

*PROPOSAL_PATTERN_ENGINE.md v1.0 | WP18C.3 — Tender Intelligence Layer | 2026-06-25*  
*Companion: TENDER_INTELLIGENCE_RULES.md | CAPABILITY_SELECTION_ENGINE.md | METHODOLOGY_SELECTION_ENGINE.md*
