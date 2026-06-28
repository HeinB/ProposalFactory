---
document_id: ARM-IT045-PROPOSAL-STRUCTURE
title: "ARM IT045 — Proposal Structure"
tender_id: "ARM IT045"
client: "African Rainbow Minerals"
engagement: "Oracle EBS Application Managed Services"
assembly_pattern: "EBS AMS Full Stack"
version: "1.1"
status: "Assembled — WP18C Proposal Factory MVP | Regression corrected WP18C.2 (SI-001: S-38 excluded; section count 57→56)"
created: "2026-06-25"
created_by: "WP18C — Proposal Factory Assembly Engine v1.0"
updated: "2026-06-26"
updated_by: "WP18C.2 — Section Library Consolidation (regression review)"
---

# ARM IT045 — Proposal Structure

**Tender:** ARM IT045 | African Rainbow Minerals | Oracle EBS AMS  
**Stage 1 Output:** PROPOSAL_ASSEMBLY_SEQUENCE.md Steps 1–9  
**Assembly Pattern:** EBS AMS Full Stack (ERP + OCI + OIC + AMS + EBS SLA Overlay + EBS DRM Overlay)  
**Net Assumptions:** 594 (6 packs; 6 suppressions)  
**Delivery Pattern:** Pattern 13 — AMS / Managed Services Onboarding  
**Methodology Asset:** W2S1-005 (governance framework); W2S1-004 (AMS model)

---

## 1. Tender Profile

| Field | Value |
|---|---|
| Tender ID | ARM IT045 |
| Client | African Rainbow Minerals (ARM) — JSE-listed diversified mining group |
| Engagement Type | Oracle EBS Application Managed Services (fixed-price monthly retainer) |
| Systems in Scope | EBS HR & Payroll v12.2.8 (5 sites; 1,787 users) + EBS Financials v12.2.10 (3 sites) |
| Infrastructure | OCI — Oracle Cloud Infrastructure (Johannesburg region; APPSolve-managed) |
| Integrations | Oracle Integration Cloud (OIC) Enterprise — active integration flows |
| Resource Model | Dedicated Named Resources: 680h/month total |
| SLA Tier | Enhanced: P1=15min/2h; P2=1h/4h; P3=4h/8h; P4=8h/16h; P5=3BD/5BD; 24/7 P1 |
| Status | WON — 28 August 2025 |
| Submission Format | Markdown proposal (WP18C MVP); rendering deferred to WP19 |
| BEE Required | Yes — Level 3 minimum; certificate expires 2026-07-31 [FLAG] |
| Mining Charter | Yes — applicable; no assumption pack covers Mining Charter [GAP-005] |

---

## 2. Capability Selection

The following 12 approved capability assets are selected for this proposal:

| # | Asset ID | Description | Assembly Method | Target Section(s) | Governance Restrictions |
|---|---|---|---|---|---|
| 1 | W1S1-001 | Company Overview | DIRECT | S-03, S-13 | Headcount "more than 50 Senior Consultants" only; year = 2002 (24+ years) |
| 2 | W1S1-002 | Company History | DIRECT | S-04 | KB-approved version supersedes 2024 company profile |
| 3 | W1S1-003 | Oracle Partnership Statement | DIRECT | S-09 | Level 1 Partner only — NEVER Gold Partner; OPN revalidation current |
| 4 | W1S1-006 | Awards and Recognition | DIRECT | S-05 | Award table unrestricted; success story URLs omitted |
| 5 | W1S1-007 | Delivery Model | DIRECT | S-06 | 8 service lines; 3 costing models present |
| 6 | W1S1-008 | Geographic Presence | DIRECT | S-07 | Sub-Saharan Africa + International approved lists only |
| 7 | W1S1-009 | Key Differentiators | DIRECT | S-08 | No prohibited product claims; no Gold Partner |
| 8 | W2S1-002 | Oracle EBS Capability Statement | EXTRACT | S-15, S-18 | Vintage content modernised for critical tenders; SARB excluded; no Gold Partner |
| 9 | W2S1-003 | Oracle DBA Executive Summary | EXTRACT | S-20 | POPIA framing applied; 24×7 qualified; "at no cost" removed |
| 10 | W2S1-004 | Oracle Managed Services Support Model | EXTRACT | S-21, S-70, S-71, S-72, S-73, S-75, S-76 | AMS scope matches assumption pack language |
| 11 | W4-INT-001 | Oracle OIC Accelerators | DIRECT | S-19 | HIST-018 billing (R825,170) NEVER in external document |
| 12 | W2S1-005 | Oracle Implementation Methodology | EXTRACT | S-36, S-37 | Governance framework sections 10–12 only; phases not applicable to AMS. **SI-001 (WP18C.2): S-38 removed from target — excluded for AMS; change management governed by S-73.** |

**Assets NOT selected (with reason):**

| Asset | Reason |
|---|---|
| W2S1-001 Fusion Capability | EBS engagement — Oracle Fusion not in scope |
| W3S1-001 to W3S1-009 HCM Suite | AMS support engagement — not HCM implementation |
| W4-HCM-002, W4-AI-002 | HCM products not in AMS scope |
| W4-ERP-001/002/003 Fusion ERP | Oracle Fusion ERP not in scope (EBS, not Fusion) |
| W1S1-004/005, W1S2-xxx, W1S3-xxx | Acumatica/BeBanking — not in scope |
| W5-METH-001 | Cross-BU platform-agnostic; W2S1-005 is the Oracle-specific standard |
| W5-ACU-001 | Acumatica AMS — not in scope |
| W4-HCM-004 | RETIRED — T&L; not applicable |

---

## 3. Reference Selection

| Ref ID | Client | Products | Sector Match | AM Approval Required | Status |
|---|---|---|---|---|---|
| **REF-ORA-008** | ARM | Oracle EBS Finance + HCM + OIC + OCI + APEX | **Exact** (same client — prior Oracle work) | Yes — required at each tender | Priority 1 |
| **REF-ORA-004** | Assore | Oracle EBS Finance + DBA | Mining/Resources | Yes | Priority 2 |
| **REF-ORA-005** | Adcock Ingram | Oracle EBS Finance + DBA + APEX | Manufacturing | Yes | Priority 3 |
| **REF-ORA-009** | MTN Group | Oracle OIC + Cloud Finance + OCI (managed services) | Managed Services + OCI | Yes | Priority 4 |

**Excluded references (with reason):**

| Ref ID | Reason |
|---|---|
| REF-ARC-002 DFA | Rule 21.4 — PERMANENTLY EXCLUDED |
| Hollywood Bets | No signed letter registered (AM approval required; no letter on file) |
| REF-ORA-011 Stellenbosch | EBS Performance Management only — low relevance for EBS AMS |
| Acumatica references | Not relevant to Oracle EBS engagement |

---

## 4. Methodology Selection

| Dimension | Selection |
|---|---|
| **Delivery Pattern** | Pattern 13 — AMS / Managed Services Onboarding |
| **Supplementary Pattern** | Pattern 10 — Oracle DBA / Managed Services (Non-AMS) for DBA onboarding element |
| **Primary Methodology Asset** | W2S1-004 Oracle Managed Services Support Model |
| **Governance Framework** | W2S1-005 Sections 10–12 (Project Governance, Issue Management, Change Control) |
| **Project Plan Template** | AMS Onboarding timeline (Pattern 13 phase structure) |
| **Phases** | Onboarding (4 weeks) → Stabilisation (2 weeks) → BAU (monthly retainer) |

---

## 5. Assumption Pack Manifest

| # | Pack | Status | Count | Trigger |
|---|---|---|---|---|
| 1 | Oracle ERP Pack | Approved v1.0 | 123 | BOM 13 — EBS Financials |
| 2 | Oracle OCI Pack | Approved v1.0 | 174 | Rule OCI-1 — EBS on OCI |
| 3 | Oracle OIC Pack | Approved v1.0 | 104 | BOM code B91110 — OIC Enterprise |
| 4 | AMS Pack | Approved v1.0 | 84 | BOM 16 — AMS engagement |
| 5 | EBS SLA Overlay | Approved v1.0 | 53 | S2 trigger — P1 < 1 hour (15min) |
| 6 | EBS DRM Overlay | Approved v1.0 | 62 | S3 trigger — named roles + monthly hours |
| — | **Total loaded** | | **600** | |
| — | **Suppressions** | — | **6** | Rules S1, S2, S3, S4 |
| — | **Net assumptions** | | **594** | |

**Assembly Engine outputs (existing):**
- `ARM_IT045_ASSUMPTION_SCHEDULE_V1.md` — 594 complete assumptions (appendix)
- `ARM_IT045_KEY_ASSUMPTIONS_V1.md` — 175 body assumptions
- `ARM_IT045_ASSEMBLY_AUDIT_REPORT.md` — full audit trail

---

## 6. Proposal Section Plan

### 6.1 Section Scope Decision: ARM IT045 EBS AMS

This is an AMS engagement, not an implementation tender. The section selection follows the AMS proposal pattern.

| Section ID | Section Name | Include | Assembly Method | Source Asset(s) | Status |
|---|---|---|---|---|---|
| **Corporate and Partnership** | | | | | |
| S-01 | Cover Page | YES | TEMPLATE | Template + Tender metadata | POPULATED |
| S-02 | Table of Contents | YES | DIRECT | Auto-generated | POPULATED |
| S-03 | Company Overview | YES | DIRECT | W1S1-001 | POPULATED |
| S-04 | Company History | YES | DIRECT | W1S1-002 | POPULATED |
| S-05 | Awards and Recognition | YES | DIRECT | W1S1-006 | POPULATED |
| S-06 | Delivery Model | YES | DIRECT | W1S1-007 | POPULATED |
| S-07 | Geographic Presence | YES | DIRECT | W1S1-008 | POPULATED |
| S-08 | Key Differentiators | YES | DIRECT | W1S1-009 | POPULATED |
| S-09 | Oracle Partnership | YES | DIRECT | W1S1-003 | POPULATED |
| S-10 | Acumatica Partnership | NO | — | — | EXCLUDED — not in scope |
| S-11 | BeBanking Overview | NO | — | — | EXCLUDED — not in scope |
| S-12 | B-BBEE Statement | YES | EXTRACT | COMP-001 + COMPLIANCE_REGISTER | POPULATED [FLAG: expires 2026-07-31] |
| **Understanding and Solution** | | | | | |
| S-13 | Executive Summary | YES | AI-GENERATE | W1S1-001 + Tender context | POPULATED [HUMAN REVIEW REQUIRED] |
| S-14 | Understanding of Requirements | YES | AI-GENERATE | Requirement Matrix | POPULATED [HUMAN REVIEW REQUIRED] |
| S-15 | Proposed Solution Overview | YES | MERGE | W2S1-002 + W2S1-004 + W4-INT-001 | POPULATED |
| S-16 | Oracle Fusion HCM | NO | — | — | EXCLUDED — EBS not Fusion |
| S-17 | Oracle Fusion ERP | NO | — | — | EXCLUDED — EBS not Fusion |
| S-18 | Oracle EBS Capability | YES | EXTRACT | W2S1-002 | POPULATED |
| S-19 | Oracle OIC | YES | DIRECT | W4-INT-001 | POPULATED |
| S-20 | Oracle DBA Capability | YES | EXTRACT | W2S1-003 | POPULATED |
| S-21 | Oracle Managed Services | YES | EXTRACT | W2S1-004 | POPULATED |
| S-22 | OCI Infrastructure | YES | AI-GENERATE | OCI assumption pack (proxy) | POPULATED [HUMAN REVIEW REQUIRED] |
| S-23–S-28 | Acumatica sections | NO | — | — | EXCLUDED — not in scope |
| S-29 | BeBanking H2H | NO | — | — | EXCLUDED — not in scope |
| **Scope and Delivery** | | | | | |
| S-30 | Scope — Inclusions | YES | EXTRACT | ASS: INC sections (ERP+OCI+OIC+AMS+EBS-DRM) | POPULATED |
| S-31 | Scope — Exclusions | YES | EXTRACT | ASS: EXC/EXT sections (Section H output) | POPULATED |
| S-33 | Dependencies | YES | EXTRACT | ASS: DEP sections (Section G) | POPULATED |
| S-34 | Implementation Methodology | NO (AMS) | — | Replaced by S-70–S-76 | EXCLUDED — AMS not implementation |
| S-35 | Project Plan | NO (AMS) | — | Replaced by AMS onboarding timeline in S-70 | EXCLUDED — AMS timeline embedded |
| S-36 | Project Governance | YES | EXTRACT | W2S1-005 Sections 11–12 | POPULATED |
| S-37 | RAID Framework | YES | TEMPLATE | RISK_LIBRARY_STANDARD.md (standard defined; no entries yet) | POPULATED [GAP-MED: Risk Library pending] |
| S-38 | Change Control | **NO (AMS)** | — | — | **EXCLUDED — SI-001 (WP18C.2): AMS engagement. Change management governed by S-73 (AMS Support block). S-38 excluded for all AMS proposals per PROPOSAL_PATTERN_ENGINE.md Rule C-1.** |
| S-39 | Testing Strategy | NO (AMS) | — | — | EXCLUDED — AMS regression testing excluded by default |
| S-40 | Data Migration | NO (AMS) | — | — | EXCLUDED — AMS not migration |
| S-41 | Training Plan | NO (AMS) | — | — | EXCLUDED — KT embedded in AMS onboarding |
| S-42 | Cutover / Go-Live | NO (AMS) | — | — | EXCLUDED — AMS not go-live |
| S-43 | Hypercare | NO (AMS) | — | — | EXCLUDED — not applicable (hypercare is post-implementation) |
| S-44 | Disaster Recovery | OPT | — | `05_Methodologies/Disaster_Recovery/` — EMPTY | [GAP-MED: DR methodology absent] |
| S-45 | Security Architecture | YES | EXTRACT | ASS: SEC sections from OCI pack | POPULATED |
| **People** | | | | | |
| S-46 | Team Structure | YES | TEMPLATE | CONSULTANT_INDEX.csv + EBS DRM Overlay resource model | POPULATED [BU Lead confirmation required] |
| S-47 | Named Consultant CVs | YES | PLACEHOLDER | APPTime | [PLACEHOLDER — OBTAIN FROM APPTME] |
| S-48 | Consultant Profiles (Summary) | OPT | PLACEHOLDER | APPTime | [PLACEHOLDER] |
| **Commercial and Governance** | | | | | |
| S-49 | Key Assumptions (Body Section) | YES | DIRECT | Assembly Engine KEY_ASSUMPTIONS output | POPULATED — 175 assumptions |
| S-50 | Risk Register | YES | AI-GENERATE | Risk Library (STANDARD DEFINED; no entries yet) | POPULATED [GAP-HIGH: AI-generated; mandatory human review] |
| S-51 | Commercial Assumptions | YES | DIRECT | Assembly Engine ASSUMPTION_SCHEDULE output | POPULATED — 594 assumptions (Appendix A-01) |
| S-52 | Commercials / Pricing | YES | PLACEHOLDER | Commercial Director | [PLACEHOLDER — COMMERCIAL INPUT REQUIRED] |
| S-53 | Rate Card Basis | OPT | EXTRACT | RATE_CARD_FRAMEWORK.md | Omit unless RFP requires rate card — no actual rates |
| S-54 | Estimation Basis | OPT | EXTRACT | ESTIMATION_GUIDE.md | Omit unless RFP requires methodology |
| **Compliance and Credentials** | | | | | |
| S-55 | Compliance Schedule | YES | EXTRACT | COMPLIANCE_REGISTER.csv | POPULATED |
| S-56 | Company Registration | YES | DIRECT | `02_Corporate/Resolutions/` | POPULATED |
| S-57 | Tax Clearance | YES | DIRECT | COMP-005 | POPULATED (valid to 2027-02-23) |
| S-58 | Directors' Resolution | YES | DIRECT | COMP-011 | POPULATED (renewed 2026-06-15) |
| S-59 | B-BBEE Certificate | YES | DIRECT | COMP-001 | POPULATED [FLAG: expires 2026-07-31] |
| S-60 | Public Liability Insurance | YES | DIRECT | COMP-008 | POPULATED (obtained 2026-06-15) |
| S-61 | Professional Indemnity | OPT | DIRECT | COMP | POPULATED |
| S-62 | Oracle OPN Certificate | YES | DIRECT | COMP-007 | POPULATED |
| S-63 | Acumatica Partner Cert | NO | — | — | EXCLUDED — not applicable |
| S-65 | POPIA Policy | OPT | PLACEHOLDER | OAR-E01 — not obtained | [GAP-MED: not available] |
| **References** | | | | | |
| S-67 | Client References | YES | TEMPLATE | REF-ORA-008, REF-ORA-004, REF-ORA-005, REF-ORA-009 | POPULATED [AM approval required for all] |
| S-68 | Case Studies | OPT | AI-GENERATE | ARM + Assore context | OMITTED (not required for this tender type) |
| S-69 | Reference Letters | YES | DIRECT | `04_References/Oracle/` | [APPENDIX A-03 — attach signed PDFs] |
| **AMS Support Sections** | | | | | |
| S-70 | Support Model | YES | MERGE | W2S1-004 + AMS pack | POPULATED |
| S-71 | SLA Framework | YES | EXTRACT | EBS-SLA Overlay | POPULATED |
| S-72 | Incident Management | YES | EXTRACT | AMS pack + EBS-SLA Overlay | POPULATED |
| S-73 | Change Request Process | YES | EXTRACT | AMS pack CR sections | POPULATED |
| S-74 | Resource Model (AMS) | YES | EXTRACT | EBS-DRM Overlay | POPULATED |
| S-75 | Release Management | YES | EXTRACT | AMS pack REL sections | POPULATED |
| S-76 | Monitoring and Reporting | YES | EXTRACT | AMS pack MON sections | POPULATED |
| **Appendices** | | | | | |
| A-01 | Complete Assumption Schedule | YES | DIRECT | Assembly Engine output | ARM_IT045_ASSUMPTION_SCHEDULE_V1.md (594 assumptions) |
| A-02 | Consultant CVs | YES | PLACEHOLDER | APPTime | [PLACEHOLDER — BU Lead selects; obtain from APPTime] |
| A-03 | Reference Letters | YES | DIRECT | `04_References/Oracle/` | Attach 4 signed PDFs |
| A-04 | Certifications and Compliance | YES | DIRECT | `01_Compliance/` | Oracle OPN + Public Liability + Tax Clearance + Directors' Resolution |
| A-05 | B-BBEE Certificate | YES | DIRECT | COMP-001 | [FLAG: expires 2026-07-31 — confirm renewal before submission] |
| A-06 | Company Registration | OPT | DIRECT | `02_Corporate/` | Include if required by tender |

---

## 7. Section Counts

| Category | Sections Included | Sections Excluded | Total Applicable |
|---|---|---|---|
| Corporate and Partnership | 10 | 2 (Acumatica, BeBanking) | 12 |
| Understanding and Solution | 9 | 8 (Fusion, HCM, Acumatica, BeBanking) | 17 |
| Scope and Delivery | 7 *(S-38 excluded — SI-001)* | 9 (Implementation, Methodology, Testing, Migration, Training, Cutover, Hypercare, S-38) | 16 |
| People | 3 | 0 | 3 |
| Commercial and Governance | 5 | 1 (Rate Card/Estimation — omit unless required) | 6 |
| Compliance and Credentials | 8 | 4 (Acumatica, POPIA/PAIA omitted) | 12 |
| References | 2 | 1 (Case Studies — omit) | 3 |
| AMS Support Sections | 7 | 0 | 7 |
| Appendices | 5 | 1 (Company Registration — conditional) | 6 |
| **TOTAL** | **56** *(SI-001: S-38 excluded)* | **26** | **82** |

---

## 8. Cross-Pipeline Governance Checks Applied

| Rule | Check | Status |
|---|---|---|
| G-01 | DFA never named | PASS — DFA excluded from reference selection |
| G-02 | CCBA never named | PASS — CCBA not referenced anywhere |
| G-03 | SAA never named as client | PASS |
| G-04 | Redpath Mining not cited | PASS |
| G-05 | Hollywood Bets AM approval | N/A — HB not selected as reference |
| G-06 | KPMG not named | PASS — KPMG not relevant to EBS AMS |
| G-07 | Oracle Gold Partner not cited | PASS — Level 1 Partner only |
| G-08 | BEE Level 3 — expiry check | FLAG — expires 2026-07-31; flag if submission after that date |
| G-09 | Section 14.2 (W3S1-008) excluded | N/A — W3S1-008 not selected |
| G-10 | Section 13.2 (W3S1-009) excluded | PASS — W3S1-009 not selected (no implementation scope) |
| G-11 | HIST-018 billing absent | PASS — flagged in W4-INT-001 selection governance |
| G-12 | Commercial figures excluded | PASS — S-52 is PLACEHOLDER |
| G-13 | CV text never from KB records | PASS — S-47/S-48 are PLACEHOLDER; APPTime instruction explicit |
| G-14 | approved_for_reuse set by BU Lead only | PASS — all 12 selected assets have approved_for_reuse: Yes |

---

> **SI-005 Assembly Order Note (WP18C.2):** The section groupings in Section 6.1 reflect logical type (not document assembly order). For Pattern 13 (AMS), the actual proposal document follows the order defined in PROPOSAL_ASSEMBLY_SEQUENCE.md v1.1 Section 6: Scope → AMS Support Model (S-74→S-70→S-71→S-72→S-73→S-75→S-76) → Commercial (S-49→S-50→S-51→S-52) → Compliance → References (assembled after Commercial per SI-005) → Appendices.

---

*ARM_IT045_PROPOSAL_STRUCTURE.md v1.1 | WP18C — Proposal Factory MVP | 2026-06-25*  
*v1.1 (WP18C.2 2026-06-26): SI-001 applied — S-38 excluded for AMS; W2S1-005 target corrected; section count corrected 57→56; SI-005 assembly order note added.*  
*Stage 1 output: 56 sections in scope; 12 capability assets selected; 4 references ranked; 6 assumption packs (594 net); Pattern 13 methodology.*
