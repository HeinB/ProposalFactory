---
document_id: CONTENT-SOURCE-MATRIX
title: "Content Source Matrix — Proposal Section to Source Library Mapping"
version: "1.2"
status: "Updated — WP18C.2 (SI-001 S-38 AMS exclusion; S-73 AMS replacement designation; SI-007 S-71/S-72 content boundary assembly instructions)"
created: "2026-06-25"
created_by: "WP18A — Proposal Factory Architecture"
updated: "2026-06-26"
updated_by: "WP18C.2 — Section Library Consolidation"
category: "Architecture / Content Mapping"
scope: "Maps every proposal section to its primary and secondary source libraries, assembly method, and validation rules. The authoritative reference for Stage 4 (Capability Selection), Stage 5 (Reference Selection), Stage 6 (Methodology Selection), and Stage 8 (Proposal Assembly)."
---

# Content Source Matrix

**Date:** 2026-06-25 | **Version:** 1.0 | **Status:** Approved  
**Work Package:** WP18A — Proposal Factory Architecture  
**References:** PROPOSAL_SECTION_LIBRARY.md (section IDs); PROPOSAL_FACTORY_ARCHITECTURE.md (stage definitions)

---

## 1. Purpose

This matrix answers: for every proposal section, where does the content come from, how is it assembled, and what must be validated before it can be used?

Assembly methods:
- **DIRECT** — Content is taken verbatim from the source asset with only metadata substitution (client name, date, tender ref)
- **EXTRACT** — Specific clauses or sections extracted from a source asset
- **MERGE** — Multiple source assets combined into a single section
- **TEMPLATE** — Source asset provides structure; content filled from tender-specific inputs
- **AI-GENERATE** — No approved source exists; AI generates draft; mandatory human review
- **PLACEHOLDER** — Section cannot be auto-populated; human authoring required

---

## 2. Source Library Reference

| Library Code | Library Name | Location | Status |
|---|---|---|---|
| CAP | Capability Library | `07_Approved_Content/Approved/` + `06_Capabilities/` | COMPLETE — 49 assets |
| ASS | Assumption Library | `08_Commercial/Assumptions/` | COMPLETE — 13 packs; 1,136 assumptions |
| METH | Methodology Library | `05_Methodologies/` | PARTIAL — 2 files (W2S1-005 Oracle; W5-METH-001 Cross-BU); 6 subfolders empty; 20 further docs planned; governed by METHODOLOGY_LIBRARY_STANDARD.md |
| REF | Reference Library | `04_References/` | ACTIVE — 16 signed letters |
| CORP | Corporate Library | `02_Corporate/` | ACTIVE |
| CONS | Consultant Library | APPTime (external) | ACTIVE — not in KB |
| COMP | Certification Library | `01_Compliance/` | ACTIVE — 17 items |
| COMM | Commercial Library | `08_Commercial/` WP11F docs | ACTIVE — internal only |
| GOV | Governance Library | `08_Commercial/Assumptions/Governance/` | ACTIVE |
| ENG | Assembly Engine | `08_Commercial/Assembly_Engine/` | PRODUCTION READY |
| RISK | Risk Library | `08_Commercial/` (standard defined; `08_Commercial/Risk_Library/` not yet created) | STANDARD DEFINED — RISK_LIBRARY_STANDARD.md approved; 15 categories; 75–90 entries extractable; content population pending |
| PRICE | Pricing Library | Commercial Director (external) | GAP |
| TENDER | Tender Document | Customer submission | Per engagement |
| APPTM | APPTime | External HR system | Per engagement |

---

## 3. Content Source Matrix — Corporate and Partnership (S-01 to S-12)

| Section ID | Section Name | Primary Source | Secondary Source | Assembly Method | Validation Rules |
|---|---|---|---|---|---|
| S-01 | Cover Page | Template + TENDER | CORP | TEMPLATE | V: client name matches tender; date is submission date; no expired compliance dates cited |
| S-02 | Table of Contents | Auto-generated | — | DIRECT | V: all headings present; all page numbers accurate |
| S-03 | Company Overview | CAP: W1S1-001 | — | DIRECT | V: year counts current (2002 = 24+ years in 2026); headcount "more than 50 Senior Consultants" only; no Nigeria/Uganda/Ghana/Bangladesh/Qatar |
| S-04 | Company History | CAP: W1S1-002 | CAP: W1S1-001 | DIRECT | V: no outdated statistics; KB-approved version supersedes 2024 company profile |
| S-05 | Awards and Recognition | CAP: W1S1-006 | — | DIRECT | V: award table unrestricted; success story URLs (Tiger Brands, USAID, UT Grain) omitted until BU Lead confirms |
| S-06 | Delivery Model | CAP: W1S1-007 | — | DIRECT | V: 8 service lines; 3 costing models; Monthly Recurring Invoice Model present |
| S-07 | Geographic Presence | CAP: W1S1-008 | — | DIRECT | V: Sub-Saharan list (BW, ZM, MZ, NA, TZ) only; international (USA, France, Abu Dhabi, Pakistan) only; no unapproved geographies |
| S-08 | Key Differentiators | CAP: W1S1-009 | — | DIRECT | V: no prohibited product claims; no Gold Partner citation |
| S-09 | Oracle Partnership | CAP: W1S1-003 | — | DIRECT | V: Level 1 only — never Gold Partner; OPN revalidation current |
| S-10 | Acumatica Partnership | CAP: W1S1-004 | — | DIRECT | V: Gold Partner — not Gold Certified; annual cert current (OAR-E03 if pending, flag) |
| S-11 | BeBanking Overview | CAP: W1S1-005 | — | DIRECT | V: SAP rule (environments only); SWIFT rule (bank-intermediated); Acumatica payroll rule |
| S-12 | B-BBEE Statement | COMP: COMP-001 | COMPLIANCE_REGISTER.csv | EXTRACT | V: certificate expiry > submission date; Level 3 only if current cert on file; do not cite after 2026-07-31 without renewal |

---

## 4. Content Source Matrix — Understanding and Solution (S-13 to S-29)

| Section ID | Section Name | Primary Source | Secondary Source | Assembly Method | Validation Rules |
|---|---|---|---|---|---|
| S-13 | Executive Summary | CAP: W1S1-001 + TENDER | Requirement Matrix | AI-GENERATE | V: no prohibited claims; references to solution match BOM; commercial claims within approved framework; mandatory BU Lead review |
| S-14 | Understanding of Requirements | TENDER: Requirement Matrix | CAP assets per BOM | AI-GENERATE | V: every mandatory RFP requirement addressed; capability claimed maps to approved KB asset; gaps flagged as [GAP]; mandatory human review |
| S-15 | Proposed Solution Overview | CAP assets per BOM | METH: W2S1-005 | MERGE | V: solution claims limited to approved KB assets; no product boundary violations; BOM-matched |
| S-16 | Oracle Fusion HCM Capability | CAP: W3S1-001 + module assets per BOM | — | MERGE | V: only modules in BOM; G-001 (Compensation = mining only); Section 14.2 of W3S1-008 excluded; Section 13.2 of W3S1-009 excluded |
| S-17 | Oracle Fusion ERP Capability | CAP: W2S1-001 + W4-ERP-001/002/003 per BOM | — | MERGE | V: modules match BOM; HIST-018 billing absent |
| S-18 | Oracle EBS Capability | CAP: W2S1-002 | — | EXTRACT | V: vintage content modernised for critical tenders; no Oracle Gold Partner cited |
| S-19 | Oracle OIC Capability | CAP: W4-INT-001 | — | DIRECT | V: HIST-018 billing (R825,170) absent; OIC tier confirmed |
| S-20 | Oracle DBA Capability | CAP: W2S1-003 | — | EXTRACT | V: statistics verified with BU Lead for critical tenders; "one of the largest locally based Oracle Applications DBA teams in SA" |
| S-21 | Oracle Managed Services | CAP: W2S1-004 | — | EXTRACT | V: AMS scope matches assumption pack language |
| S-22 | OCI Infrastructure | ASS: OCI pack (primary) | No standalone capability narrative | AI-GENERATE | V: no capability claims beyond what OCI assumption pack supports; OCI pack sections A–F used as source; mandatory human review |
| S-23 | Acumatica Financials | CAP: W1S2-001 | — | DIRECT | V: Financial module in BOM |
| S-24 | Acumatica Distribution | CAP: W1S2-002 | — | DIRECT | V: Distribution in BOM |
| S-25 | Acumatica Manufacturing | CAP: W1S2-004 | — | DIRECT | V: Manufacturing in BOM |
| S-26 | Acumatica CRM | CAP: W1S2-005 | — | DIRECT | V: CRM in BOM |
| S-27 | Acumatica Other Modules | CAP: W1S2-003/006/007/009 per BOM | — | EXTRACT | V: only modules in BOM; W1S2-008 ARCHIVED — never selected |
| S-28 | Acumatica Managed Services | CAP: W5-ACU-001 | — | DIRECT | V: AMS scope in BOM |
| S-29 | BeBanking H2H Banking | CAP: W1S3-001 to W1S3-010 per BOM | — | MERGE | V: SAP rule; SWIFT rule; Acumatica payroll rule; only modules in BOM |

---

## 5. Content Source Matrix — Scope and Delivery (S-30 to S-45)

| Section ID | Section Name | Primary Source | Secondary Source | Assembly Method | Validation Rules |
|---|---|---|---|---|---|
| S-30 | Scope — Inclusions | ASS: INC sections per pack | CAP assets per BOM | EXTRACT | V: inclusion language from approved pack verbatim; scope matches BOM |
| S-31 | Scope — Exclusions | ASS: EXC/EXT sections per pack (Section H output) | — | EXTRACT | V: all exclusion assumptions from Section H of ASSUMPTION_SCHEDULE output included; no exclusions added that contradict assumption pack language |
| S-32 | Deliverables | ENG: DELIVERY_PATTERN_LIBRARY.md | METH: W2S1-005 | EXTRACT | V: deliverables match selected delivery pattern; no deliverables promised that have no KB evidence |
| S-33 | Dependencies | ASS: DEP sections (subset of Section G) | TENDER: client obligations | EXTRACT | V: all DEP-coded assumptions from Section G included; client obligations accurately reflected |
| S-34 | Implementation Methodology | METH: W2S1-005 (Oracle) or W5-METH-001 (platform-agnostic) | ENG: DELIVERY_PATTERN_LIBRARY.md | TEMPLATE | V: phases match delivery pattern; OUM-based for Oracle; tailored for client go-live target |
| S-35 | Project Plan | ENG: PROJECT_PLAN_TEMPLATES.md (pattern-matched) | ENG: DELIVERY_PATTERN_LIBRARY.md | TEMPLATE | V: week-based only (no calendar dates until final submission); resource model matches delivery pattern; parallel payroll run INCLUDED by default for HCM (HCM-CUT-005) |
| S-36 | Project Governance | METH: W2S1-005 Sections 11–12 | — | EXTRACT | V: RAID structure present; steering committee cadence defined; escalation path present |
| S-37 | RAID Framework | METH: W2S1-005 or W5-METH-001 | RISK: Risk Library (STANDARD DEFINED — content pending) | TEMPLATE | V: at least 5 risks identified; risks use RC-category taxonomy from RISK_LIBRARY_STANDARD.md; no risks cited that contradict assumption pack language; G-RISK gap flagged until Risk Library populated |
| S-38 | Change Control | COMM: CR_PRICING_MODEL.md | — | EXTRACT (Implementation only) | V: 2-hour CR threshold not exposed in client doc. **SI-001: EXCLUDED for Pattern 13 (AMS) — for AMS, use S-73 (Change Request Process) instead. Secondary source removed: AMS pack CR sections now exclusively govern S-73, not S-38. For Combination Pattern (Impl+AMS), assemble S-38 for implementation scope only.** |
| S-39 | Testing Strategy | ENG: DELIVERY_PATTERN_LIBRARY.md | ASS: TST sections | EXTRACT | V: CRP/SIT/UAT cycles match delivery pattern; regression testing default = excluded |
| S-40 | Data Migration | ASS: DAT/MIG sections per pack | ENG: DELIVERY_PATTERN_LIBRARY.md | EXTRACT | V: 2 mock + final standard; opening balance only default; migration objects list from tender |
| S-41 | Training Plan | ASS: TRN sections per pack | ENG: DELIVERY_PATTERN_LIBRARY.md | EXTRACT | V: training type (end-user vs admin) confirmed; SETA reporting scope confirmed |
| S-42 | Cutover / Go-Live | ASS: CUT sections per pack | ENG: DELIVERY_PATTERN_LIBRARY.md | EXTRACT | V: parallel run default INCLUDED (HCM-CUT-005); hypercare model present; client responsibilities for cutover identified |
| S-43 | Hypercare / Transition | ENG: DELIVERY_PATTERN_LIBRARY.md | — | EXTRACT | V: 4-week hypercare standard; named lead W1; response times W2–W4 per delivery pattern |
| S-44 | Disaster Recovery | METH: `05_Methodologies/Disaster_Recovery/` (EMPTY) | — | PLACEHOLDER | V: FLAG — no DR methodology in KB; AI-GENERATE with mandatory human review until gap filled |
| S-45 | Security Architecture | ASS: SEC sections per pack | CAP assets | EXTRACT | V: security claims limited to assumption pack language; no regulatory certifications claimed without COMP evidence |

---

## 6. Content Source Matrix — People (S-46 to S-48)

| Section ID | Section Name | Primary Source | Secondary Source | Assembly Method | Validation Rules |
|---|---|---|---|---|---|
| S-46 | Team Structure | CONS: CONSULTANT_INDEX.csv | ENG: DELIVERY_PATTERN_LIBRARY.md (resource model) | TEMPLATE | V: BU Lead confirms team selection; available_for_tenders flag = Yes; do not propose unavailable consultants |
| S-47 | Named Consultant CVs | APPTM: APPTime | — | PLACEHOLDER | V: full CVs from APPTime only; never generated from KB records (ADR-001) |
| S-48 | Consultant Profiles (Summary) | APPTM: APPTime | CONS: CONSULTANT_INDEX.csv (metadata) | PLACEHOLDER | V: confirm with APPTime; KB index used for skill matching only |

---

## 7. Content Source Matrix — Commercial and Governance (S-49 to S-54)

| Section ID | Section Name | Primary Source | Secondary Source | Assembly Method | Validation Rules |
|---|---|---|---|---|---|
| S-49 | Key Assumptions (Body Section) | ENG: Assembly Engine KEY_ASSUMPTIONS output | — | DIRECT | V: all 10 WP17D-1 validation checks pass; body section present; Section G and H fully represented |
| S-50 | Risk Register | RISK: Risk Library (STANDARD DEFINED — content pending) | METH: W2S1-005 or W5-METH-001 | EXTRACT (when Risk Library populated) / AI-GENERATE (interim) | V: minimum 5 risks; RC-category taxonomy from RISK_LIBRARY_STANDARD.md used; Likelihood × Impact rating present; mitigation per risk; mandatory human review until Risk Library approved entries exist |
| S-51 | Commercial Assumptions | ENG: Assembly Engine ASSUMPTION_SCHEDULE output | — | DIRECT | V: all 10 WP17D-1 validation checks pass; complete schedule present; suppressed assumptions absent |
| S-52 | Commercials / Pricing | PRICE: Commercial Director | COMM: WP11F framework | PLACEHOLDER | V: never generated without Commercial Director authorisation; COMMERCIAL_GOVERNANCE.md sign-off sequence must be followed; no actual rates in external document |
| S-53 | Rate Card Basis | COMM: RATE_CARD_FRAMEWORK.md | — | EXTRACT | V: no actual rates disclosed; do not expose CD decisions pending (BU-RC-004, BU-RC-008) |
| S-54 | Estimation Basis | COMM: ESTIMATION_GUIDE.md | — | EXTRACT | V: complexity tiers defined; phase model present; no bottom-up estimates in external document |

---

## 8. Content Source Matrix — Compliance and Credentials (S-55 to S-66)

| Section ID | Section Name | Primary Source | Secondary Source | Assembly Method | Validation Rules |
|---|---|---|---|---|---|
| S-55 | Compliance Schedule | COMP: COMPLIANCE_REGISTER.csv | — | EXTRACT | V: all items have validity date > submission date; expired items flagged; COMP-001 B-BBEE checked |
| S-56 | Company Registration | CORP: `02_Corporate/Resolutions/` | COMPLIANCE_REGISTER.csv | DIRECT | V: CIPC registration current |
| S-57 | Tax Clearance | COMP: COMP-005 | — | DIRECT | V: expiry date > submission date (current valid to 2027-02-23) |
| S-58 | Directors' Resolution | CORP: `02_Corporate/Resolutions/` | COMP: COMP-011 | DIRECT | V: renewed 2026-06-15; confirm still valid at submission |
| S-59 | B-BBEE Certificate | COMP: COMP-001 | — | DIRECT | V: expires 2026-07-31 — do not submit after that date without renewal cert (G-08) |
| S-60 | Public Liability Insurance | COMP: COMP-008 | — | DIRECT | V: obtained 2026-06-15; confirm exact expiry from policy (OAR — pending confirmation) |
| S-61 | Professional Indemnity | COMP: COMP | — | DIRECT | V: expiry date > submission date |
| S-62 | Oracle OPN Certificate | COMP: COMP-007 | — | DIRECT | V: Level 1 Partner only; annual OPN revalidation; never cite Gold Partner |
| S-63 | Acumatica Partner Certificate | COMP: COMP-016 | — | DIRECT | V: Gold Partner — not Gold Certified; OAR-E03 gap — flag if not obtained |
| S-64 | ISO / Other Certifications | COMP: `01_Compliance/` | — | DIRECT | V: expiry date > submission date |
| S-65 | POPIA Policy | OAR-E01 — not yet obtained | — | PLACEHOLDER | V: not available until OAR-E01 resolved |
| S-66 | PAIA Manual | OAR-E02 — not yet obtained | — | PLACEHOLDER | V: not available until OAR-E02 resolved |

---

## 9. Content Source Matrix — References (S-67 to S-69)

| Section ID | Section Name | Primary Source | Secondary Source | Assembly Method | Validation Rules |
|---|---|---|---|---|---|
| S-67 | Client References | REF: REFERENCE_MASTER.csv | REF: `04_References/` signed PDFs | TEMPLATE | V: AM approval at each tender; only signed letters; no unsigned templates; prohibited client rules G-01 to G-07; vintage > 5 years flagged |
| S-68 | Case Studies | CAP assets | REF: Reference letters | AI-GENERATE | V: client naming restrictions applied; no DFA/CCBA/SAA; all facts from approved KB sources only; mandatory human review |
| S-69 | Reference Letters | REF: `04_References/` signed PDFs | — | DIRECT | V: AM approval; only signed, registered letters; REFERENCE_MASTER.csv used as canonical register |

---

## 10. Content Source Matrix — Support and Managed Services (S-70 to S-76)

| Section ID | Section Name | Primary Source | Secondary Source | Assembly Method | Validation Rules |
|---|---|---|---|---|---|
| S-70 | Support Model | CAP: W2S1-004 (Oracle) or W5-ACU-001 (Acumatica) | ASS: AMS pack | MERGE | V: SLA tiers from assumption pack; AMS scope from BOM |
| S-71 | SLA Framework | ASS: AMS pack (SLA section) or EBS-SLA overlay | — | EXTRACT | V: P1=1h response; P2=4h; P3=1BD; P4=3BD; 08:00–17:00 SAST; response ≠ resolution. **SI-007 CONTENT BOUNDARY: Assemble SLA tier table and service hours ONLY. Do NOT include incident classification process, escalation workflow, or any process narrative — that content belongs in S-72. Assembler must include the "response time ≠ resolution time" disclaimer.** |
| S-72 | Incident Management | ASS: AMS pack (INC/PRI sections) | EBS-SLA overlay if EBS AMS | EXTRACT | V: EBS-SLA overlay takes precedence for EBS AMS. **SI-007 CONTENT BOUNDARY: Assemble incident classification process and lifecycle ONLY (log → triage → assign → resolve → close → review); escalation path; communication standards. Do NOT re-state SLA tier values — reference as "per S-71 SLA Framework" instead. Never duplicate the SLA tier table from S-71.** |
| S-73 | Change Request Process | ASS: AMS pack (CR section) | COMM: CR_PRICING_MODEL.md | EXTRACT | V: 2-hour CR threshold NOT exposed; use assumption pack language verbatim; CD decisions BU-CR-003 not exposed. **SI-001: This section replaces S-38 for all AMS proposals (Pattern 13) and is the single governing change management section for AMS. Assembled within the AMS Support Model block (S-70–S-76), not in the Scope/Delivery block. For Combination Pattern (Impl+AMS), S-73 governs AMS scope only; S-38 governs the implementation change process separately.** |
| S-74 | Resource Model | ASS: AMS pack (INC section) or EBS-DRM overlay | — | EXTRACT | V: dedicated vs shared model from BOM; EBS-DRM overlay if EBS dedicated resource in scope |
| S-75 | Release Management | ASS: AMS pack (REL section) | — | EXTRACT | V: Oracle quarterly release advisory included; regression testing of patch = excluded unless scoped |
| S-76 | Monitoring and Reporting | ASS: AMS pack (MON section) | — | EXTRACT | V: mailbox monitoring standard; proactive monitoring = separate scope unless contracted |

---

## 11. Content Source Matrix — Appendices (A-01 to A-06)

| Section ID | Section Name | Primary Source | Secondary Source | Assembly Method | Validation Rules |
|---|---|---|---|---|---|
| A-01 | Complete Assumption Schedule | ENG: Assembly Engine ASSUMPTION_SCHEDULE output | — | DIRECT | V: all 10 WP17D-1 validation checks pass; counts match body section numbers |
| A-02 | Consultant CVs | APPTM: APPTime | — | PLACEHOLDER | V: ADR-001 applies always |
| A-03 | Reference Letters | REF: `04_References/` | — | DIRECT | V: AM approval; signed only |
| A-04 | Certifications | COMP: `01_Compliance/` | — | DIRECT | V: all expiry dates > submission date |
| A-05 | B-BBEE Certificate | COMP: COMP-001 | — | DIRECT | V: expiry > submission date; Level 3 if current cert on file |
| A-06 | Company Registration | CORP: `02_Corporate/` | — | DIRECT | V: CIPC current |

---

## 12. Source Library Gap Analysis

| Library | Current State | Gap Description | Priority | Recommended Action |
|---|---|---|---|---|
| Capability Library | COMPLETE — 49 assets | OCI standalone narrative missing (using assumption pack as proxy) | HIGH | Author OCI capability statement |
| Assumption Library | COMPLETE — 1,136 assumptions | Mining Charter (GAP-005); AMS KT (GAP-007) | MEDIUM | Future pack authoring |
| Methodology Library | PARTIAL — 2 files (W2S1-005 + W5-METH-001); standard defined | Disaster Recovery, Security, Support, Testing, PM, Managed Services methodologies missing; 20 additional documents planned | HIGH | Execute METHODOLOGY_LIBRARY_STANDARD.md authoring roadmap (Ranks 1–22) |
| Risk Library | STANDARD DEFINED (RISK_LIBRARY_STANDARD.md); content not yet populated | No approved risk entries yet; 75–90 entries extractable from existing KB; Risk Library folder not yet created | HIGH | Create `08_Commercial/Risk_Library/` folder; extract risk entries from capability assets; BU Lead approval |
| Reference Library | ACTIVE — 16 letters | KPMG blocked (OAR-B02); Harmony Gold unreadable (OAR-B03) | MEDIUM | Resolve OAR-B02/B03 |
| Pricing Library | NOT CREATED | Commercial Director authority; not in KB | LOW | Commercial Director to establish external |
| CV Library | NOT IN KB | ADR-001 — APPTime is authoritative | N/A | No action required |
| POPIA / PAIA | NOT OBTAINED | OAR-E01/E02 | MEDIUM | Company Secretary action |

---

*CONTENT_SOURCE_MATRIX.md v1.2 | WP18A — Proposal Factory Architecture | Updated WP18C.2 2026-06-26*  
*Maps all 82 proposal sections to source libraries. Governs Stage 4, 5, 6, 8 of the Proposal Factory pipeline.*  
*v1.2: SI-001 applied — S-38 excluded for AMS; AMS secondary source moved to S-73; S-73 designated as AMS change management replacement. SI-007 applied — S-71/S-72 content boundaries defined as assembly instructions to prevent SLA/Incident duplication.*
