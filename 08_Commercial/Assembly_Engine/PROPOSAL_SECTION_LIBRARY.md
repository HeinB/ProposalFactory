---
document_id: PROPOSAL-SECTION-LIBRARY
title: "Proposal Section Library"
version: "1.2"
status: "Updated — WP18C.2 (SI-001 S-38 AMS exclusion; SI-007 SLA/Incident content boundaries; section scoping reference added)"
created: "2026-06-25"
created_by: "WP18A — Proposal Factory Architecture"
updated: "2026-06-26"
updated_by: "WP18C.2 — Section Library Consolidation"
category: "Architecture / Section Catalogue"
scope: "Defines every proposal section supported by the Proposal Factory. For each section: name, mandatory/optional status, tender location, source repositories, deterministic/AI-assisted nature, human review requirement, and automation target. Extends PROPOSAL_STRUCTURE_LIBRARY.md (WP12) to the full Proposal Factory architecture scope. Section scoping per engagement type is governed by PROPOSAL_PATTERN_ENGINE.md."
---

# Proposal Section Library

**Date:** 2026-06-25 | **Version:** 1.0 | **Status:** Approved  
**Work Package:** WP18A — Proposal Factory Architecture  
**Predecessor:** PROPOSAL_STRUCTURE_LIBRARY.md (WP12) — this document extends that to the full factory model

---

## 1. Purpose and Scope

This library defines every proposal section that the Proposal Factory will support. For each section:

- **Section ID** — unique reference for factory pipeline
- **Mandatory / Optional** — mandatory = required in every proposal of this type; optional = included when in scope
- **Typical location** — where it appears in a standard proposal
- **Source repositories** — where the content comes from
- **Deterministic** — can content be selected and assembled by rule alone (no AI judgement)?
- **AI-assisted** — does content benefit from or require AI generation / tailoring?
- **Human review required** — must a human validate before submission?
- **Current automation %** — what is currently automated end-to-end?
- **Target automation %** — what should be automated in the full Proposal Factory?

**Automation definition:** An automated section requires no manual authoring. Content is selected, assembled, and formatted from approved KB sources by the factory pipeline. Human review for governance sign-off is separate from automation.

**Section scoping by engagement type:** This library defines all 82 sections the Proposal Factory supports. Which sections appear in any given proposal is determined deterministically by the Tender Profile and governed by PROPOSAL_PATTERN_ENGINE.md. Refer to that document for section inclusion/exclusion rules per pattern, platform-conditional triggers, section ordering per delivery pattern, and combination pattern rules (Implementation + AMS). PROPOSAL_PATTERN_ENGINE.md is the authoritative scoping reference — this library defines what each section IS; the Pattern Engine defines which sections are IN SCOPE for each engagement.

---

## 2. Section Classification Key

| Code | Meaning |
|---|---|
| M-ALL | Mandatory in all proposals |
| M-[TYPE] | Mandatory in specified tender type only (e.g., M-FIXED = fixed price only) |
| OPT | Optional — included when in scope |
| COND | Conditional — included when a specific BOM condition is met |

---

## 3. Section Library — Corporate and Partnership

| ID | Section Name | M/O | Typical Location | Source Repository | Deterministic | AI-assisted | Human Review | Current Auto% | Target Auto% |
|---|---|---|---|---|---|---|---|---|---|
| S-01 | Cover Page / Transmittal | M-ALL | Page 1 | Template + Tender metadata | Yes | No | Yes — client name, date | 40% | 95% |
| S-02 | Table of Contents | M-ALL | Page 2 | Auto-generated from document | Yes | No | Yes — verify headings | 60% | 100% |
| S-03 | Company Overview | M-ALL | Section 1 | W1S1-001 | Yes | No | No | 90% | 100% |
| S-04 | Company History | M-ALL | Section 1 | W1S1-002 | Yes | No | No | 90% | 100% |
| S-05 | Awards and Recognition | M-ALL | Section 1 | W1S1-006 | Yes | No | Yes — award table current | 85% | 100% |
| S-06 | Delivery Model | M-ALL | Section 1 | W1S1-007 | Yes | No | No | 90% | 100% |
| S-07 | Geographic Presence | M-ALL | Section 1 | W1S1-008 | Yes | No | No | 90% | 100% |
| S-08 | Key Differentiators | OPT | Section 1 | W1S1-009 | Yes | No | No | 85% | 100% |
| S-09 | Oracle Partnership | COND-ORA | Section 2 | W1S1-003 | Yes | No | Yes — OPN revalidation | 85% | 100% |
| S-10 | Acumatica Partnership | COND-ACU | Section 2 | W1S1-004 | Yes | No | Yes — cert currency | 85% | 100% |
| S-11 | BeBanking Product Overview | COND-BB | Section 2 | W1S1-005 | Yes | No | No | 85% | 100% |
| S-12 | B-BBEE Compliance Statement | M-ALL | Compliance section | COMPLIANCE_REGISTER.csv + cert | Yes | No | Yes — expiry date | 70% | 95% |

---

## 4. Section Library — Understanding and Solution

| ID | Section Name | M/O | Typical Location | Source Repository | Deterministic | AI-assisted | Human Review | Current Auto% | Target Auto% |
|---|---|---|---|---|---|---|---|---|---|
| S-13 | Executive Summary | M-ALL | Section 2 | W1S1-001 + tender context | No | Yes | Yes — mandatory | 20% | 60% |
| S-14 | Understanding of Requirements | M-ALL | Section 3 | Requirement Matrix + KB assets | No | Yes | Yes — mandatory | 10% | 50% |
| S-15 | Proposed Solution Overview | M-ALL | Section 4 | Capability assets per BOM | Partial | Yes | Yes | 40% | 75% |
| S-16 | Oracle Fusion HCM Capability | COND-HCM | Section 4 | W3S1-001 + module assets | Yes | No | No | 85% | 100% |
| S-17 | Oracle Fusion ERP Capability | COND-ERP | Section 4 | W2S1-001 + W4-ERP-001/002/003 | Yes | No | No | 85% | 100% |
| S-18 | Oracle EBS Capability | COND-EBS | Section 4 | W2S1-002 | Yes | No | Yes — modernise vintage | 60% | 85% |
| S-19 | Oracle OIC / Integration | COND-OIC | Section 4 | W4-INT-001 | Yes | No | No | 85% | 100% |
| S-20 | Oracle DBA Capability | COND-DBA | Section 4 | W2S1-003 | Yes | No | Yes — verify stats | 70% | 90% |
| S-21 | Oracle Managed Services | COND-AMS | Section 4 | W2S1-004 | Yes | No | No | 80% | 100% |
| S-22 | OCI Infrastructure | COND-OCI | Section 4 | No standalone narrative yet — use OCI assumption pack | No | Yes | Yes | 20% | 70% |
| S-23 | Acumatica Financials | COND-ACU | Section 4 | W1S2-001 | Yes | No | No | 85% | 100% |
| S-24 | Acumatica Distribution | COND-ACU | Section 4 | W1S2-002 | Yes | No | No | 85% | 100% |
| S-25 | Acumatica Manufacturing | COND-ACU | Section 4 | W1S2-004 | Yes | No | No | 85% | 100% |
| S-26 | Acumatica CRM | COND-ACU | Section 4 | W1S2-005 | Yes | No | No | 85% | 100% |
| S-27 | Acumatica Other Modules | COND-ACU | Section 4 | W1S2-003/006/007/009 per BOM | Yes | No | No | 85% | 100% |
| S-28 | Acumatica Managed Services | COND-ACU-AMS | Section 4 | W5-ACU-001 | Yes | No | No | 80% | 100% |
| S-29 | BeBanking H2H Banking | COND-BB | Section 4 | W1S3-001 to W1S3-010 per BOM | Yes | No | No | 85% | 100% |

---

## 5. Section Library — Scope and Delivery

| ID | Section Name | M/O | Typical Location | Source Repository | Deterministic | AI-assisted | Human Review | Current Auto% | Target Auto% |
|---|---|---|---|---|---|---|---|---|---|
| S-30 | Scope of Work — Inclusions | M-FIXED | Section 5 | Assumption packs (INC sections) + Capability assets | Yes | No | Yes | 50% | 90% |
| S-31 | Scope of Work — Exclusions | M-FIXED | Section 5 | Assumption packs (EXC/EXT sections) | Yes | No | Yes | 70% | 95% |
| S-32 | Deliverables | M-ALL | Section 5 | Delivery pattern + methodology asset | Yes | No | Yes | 50% | 85% |
| S-33 | Dependencies | M-FIXED | Section 6 | Assumption packs (DEP sections) | Yes | No | Yes | 60% | 90% |
| S-34 | Implementation Methodology | M-ALL | Section 6 | W2S1-005 (Oracle) or W5-METH-001 (platform-agnostic) | Yes | No | Yes — tailor phases | 65% | 85% |
| S-35 | Project Plan / Timeline | M-ALL | Section 7 | PROJECT_PLAN_TEMPLATES.md (pattern-matched) | Yes | No | Yes — dates, resources | 50% | 80% |
| S-36 | Project Governance | M-ALL | Section 7 | W2S1-005 Sections 11–12 | Yes | No | No | 70% | 90% |
| S-37 | RAID Framework | M-ALL | Section 7 | Methodology asset (W2S1-005/W5-METH-001) + Risk Library (STANDARD DEFINED — RISK_LIBRARY_STANDARD.md) | Partial | No | Yes | 30% | 70% |
| S-38 | Change Control Framework | M-FIXED (Impl); **EXCL-AMS** ¹ | Section 8 | Commercial Framework (CR_PRICING_MODEL.md) | Yes | No | No — do not expose rates | 60% | 90% |
| S-39 | Testing Strategy | OPT | Section 6 | Delivery pattern (CRP/SIT/UAT cycle definitions) | Yes | No | No | 50% | 85% |
| S-40 | Data Migration | COND-MIG | Section 6 | Assumption packs (DAT/MIG sections) | Yes | No | Yes | 60% | 85% |
| S-41 | Training Plan | OPT | Section 6 | Assumption packs (TRN sections) | Yes | No | Yes | 50% | 80% |
| S-42 | Cutover / Go-Live Plan | M-FIXED | Section 6 | Assumption packs (CUT sections) + Delivery pattern | Yes | No | Yes | 50% | 80% |
| S-43 | Hypercare / Transition | COND-POST-GOLIVE | Section 6 | Delivery pattern (hypercare model) | Yes | No | No | 50% | 85% |
| S-44 | Disaster Recovery | OPT | Section 6 | `05_Methodologies/Disaster_Recovery/` — EMPTY | No | No | Yes | 0% | 70% |
| S-45 | Security Architecture | COND-OCI | Section 6 | Assumption packs (SEC sections) + future security methodology | Partial | No | Yes | 30% | 75% |

> ¹ **SI-001 — S-38 AMS Exclusion (WP18C.2):** S-38 is excluded from all AMS proposals (Pattern 13). For AMS, change control governance is provided exclusively by S-73 (Change Request Process) within the AMS support model. Including both sections creates structural duplication — S-73 is the single governing section for change management in AMS. **Exception (Combination Pattern):** When an Implementation and AMS scope are in the same tender, both S-38 and S-73 are included with clearly distinct scope: S-38 governs the implementation change process; S-73 governs the ongoing AMS change request process. Authority: PROPOSAL_PATTERN_ENGINE.md Section 4.1 (Rule C-1).

---

## 6. Section Library — People

| ID | Section Name | M/O | Typical Location | Source Repository | Deterministic | AI-assisted | Human Review | Current Auto% | Target Auto% |
|---|---|---|---|---|---|---|---|---|---|
| S-46 | Team Structure | M-ALL | Section 8 | CONSULTANT_INDEX.csv + Delivery pattern resource model | Partial | No | Yes — BU Lead selects | 30% | 60% |
| S-47 | Named Consultant CVs | OPT | Appendix | APPTime (external) | No | No | Yes — mandatory | 0% | 0% |
| S-48 | Consultant Profiles (Summary) | OPT | Section 8 | APPTime (external) | No | No | Yes — mandatory | 0% | 30% |

**Note:** CVs are never generated from KB records (ADR-001). CV automation target remains 0% for full CVs. Brief summary profiles (name, role, years, certifications) could be partially automated from CONSULTANT_INDEX.csv to 30%.

---

## 7. Section Library — Commercial and Governance

| ID | Section Name | M/O | Typical Location | Source Repository | Deterministic | AI-assisted | Human Review | Current Auto% | Target Auto% |
|---|---|---|---|---|---|---|---|---|---|
| S-49 | Key Assumptions (Body Section) | M-FIXED | Section 9 | Assembly Engine — KEY_ASSUMPTIONS output | Yes | No | Yes — governance sign-off | 95% | 100% |
| S-50 | Risk Register | M-FIXED | Section 9 | Risk Library (STANDARD DEFINED — RISK_LIBRARY_STANDARD.md; content population pending) | No | Yes | Yes — mandatory | 5% | 70% |
| S-51 | Commercial Assumptions | M-FIXED | Section 9 | Assembly Engine — ASSUMPTION_SCHEDULE output | Yes | No | Yes — governance sign-off | 95% | 100% |
| S-52 | Commercials / Pricing | M-FIXED | Last section | WP11F Commercial Framework | No | No | Yes — Commercial Director | 0% | 20% |
| S-53 | Rate Card Basis | OPT | Pricing section | RATE_CARD_FRAMEWORK.md | No | No | Yes — never expose rates | 0% | 20% |
| S-54 | Estimation Basis | OPT | Pricing section | ESTIMATION_GUIDE.md | No | No | Yes — BU Lead | 0% | 20% |

---

## 8. Section Library — Compliance and Credentials

| ID | Section Name | M/O | Typical Location | Source Repository | Deterministic | AI-assisted | Human Review | Current Auto% | Target Auto% |
|---|---|---|---|---|---|---|---|---|---|
| S-55 | Compliance Schedule | M-ALL | Compliance section | COMPLIANCE_REGISTER.csv | Yes | No | Yes — verify expiry dates | 70% | 95% |
| S-56 | Company Registration | M-ALL | Compliance | `02_Corporate/Resolutions/` | Yes | No | Yes — currency | 60% | 90% |
| S-57 | Tax Clearance | M-ALL | Compliance | `01_Compliance/` + COMP-005 | Yes | No | Yes — expiry date | 70% | 95% |
| S-58 | Directors' Resolution | M-ALL | Compliance | `02_Corporate/Resolutions/` + COMP-011 | Yes | No | Yes — currency | 70% | 95% |
| S-59 | B-BBEE Certificate | M-SA | Compliance | `01_Compliance/` + COMP-001 | Yes | No | Yes — expiry date | 70% | 95% |
| S-60 | Public Liability Insurance | M-ALL | Compliance | `01_Compliance/` + COMP-008 | Yes | No | Yes — expiry date | 70% | 95% |
| S-61 | Professional Indemnity | OPT | Compliance | `01_Compliance/` | Yes | No | Yes | 60% | 90% |
| S-62 | Certifications (Oracle OPN) | COND-ORA | Credentials | `01_Compliance/` | Yes | No | Yes — OPN revalidation | 60% | 90% |
| S-63 | Certifications (Acumatica) | COND-ACU | Credentials | `01_Compliance/` — COMP-016 GAP | Yes | No | Yes — OAR-E03 pending | 30% | 90% |
| S-64 | Certifications (ISO/Other) | OPT | Credentials | `01_Compliance/` | Yes | No | Yes | 60% | 90% |
| S-65 | POPIA Policy | OPT | Compliance | OAR-E01 — not yet obtained | No | No | Yes | 0% | 80% |
| S-66 | PAIA Manual | OPT | Compliance | OAR-E02 — not yet obtained | No | No | Yes | 0% | 80% |

---

## 9. Section Library — References

| ID | Section Name | M/O | Typical Location | Source Repository | Deterministic | AI-assisted | Human Review | Current Auto% | Target Auto% |
|---|---|---|---|---|---|---|---|---|---|
| S-67 | Client References | M-ALL | Section 10 | REFERENCE_MASTER.csv + `04_References/` | Partial | No | Yes — AM approval mandatory | 50% | 85% |
| S-68 | Case Studies | OPT | Section 10 | Capability assets + reference letters | No | Yes | Yes — mandatory | 15% | 60% |
| S-69 | Reference Letters | OPT | Appendix | `04_References/` signed PDFs | Yes | No | Yes — AM approval mandatory | 60% | 90% |

---

## 10. Section Library — Support and Managed Services

| ID | Section Name | M/O | Typical Location | Source Repository | Deterministic | AI-assisted | Human Review | Current Auto% | Target Auto% |
|---|---|---|---|---|---|---|---|---|---|
| S-70 | Support Model | COND-AMS | Section 11 | AMS assumption pack + W2S1-004 / W5-ACU-001 | Yes | No | No | 75% | 100% |
| S-71 | SLA Framework | COND-AMS | Section 11 | AMS pack + EBS-SLA overlay | Yes | No | No | 75% | 100% |
| S-72 | Incident Management | COND-AMS | Section 11 | AMS assumption pack | Yes | No | No | 70% | 95% |
| S-73 | Change Request Process | COND-AMS ² | Section 11 | AMS pack + CR_PRICING_MODEL.md | Yes | No | No — do not expose CR thresholds | 70% | 95% |
| S-74 | Resource Model (AMS) | COND-AMS | Section 11 | AMS pack + EBS-DRM overlay | Yes | No | No | 70% | 95% |
| S-75 | Release Management | COND-AMS | Section 11 | AMS assumption pack | Yes | No | No | 70% | 95% |
| S-76 | Monitoring and Reporting | COND-AMS | Section 11 | AMS assumption pack | Yes | No | No | 70% | 95% |

> ² **SI-001 — S-73 AMS Designation (WP18C.2):** S-73 (Change Request Process) is the AMS-authoritative section for all change management governance. It replaces S-38 (Change Control Framework) for all AMS proposals (Pattern 13). S-73 is assembled within the AMS Support Model block and must not be duplicated in the Scope/Delivery section.

> **SI-007 — SLA/Incident Content Boundaries (WP18C.2):**
> - **S-71 (SLA Framework) — authoritative content boundary:** SLA tier table only (P1=1h response, P2=4h, P3=1 business day, P4=3 business days); service hours (SAST Mon–Fri 08:00–17:00); coverage exclusions (24×7 excluded unless contracted); response ≠ resolution language. Do NOT include incident classification process, escalation paths, or any process narrative — that belongs in S-72.
> - **S-72 (Incident Management) — authoritative content boundary:** Incident classification process; escalation path; incident lifecycle (log → triage → assign → resolve → close → review); communication standards. Do NOT re-state SLA times from S-71 — reference them as "per S-71 SLA Framework". Never duplicate the SLA tier table in S-72.

---

## 11. Section Library — Appendices

| ID | Section Name | M/O | Typical Location | Source Repository | Deterministic | AI-assisted | Human Review | Current Auto% | Target Auto% |
|---|---|---|---|---|---|---|---|---|---|
| A-01 | Complete Assumption Schedule | M-FIXED | Appendix A | Assembly Engine output | Yes | No | Yes — governance sign-off | 95% | 100% |
| A-02 | Consultant CVs | OPT | Appendix B | APPTime | No | No | Yes — mandatory | 0% | 0% |
| A-03 | Reference Letters | OPT | Appendix C | `04_References/` | Yes | No | Yes — AM approval | 60% | 90% |
| A-04 | Certifications and Compliance | M-ALL | Appendix D | `01_Compliance/` | Yes | No | Yes — expiry dates | 70% | 95% |
| A-05 | B-BBEE Certificate | M-SA | Appendix E | `01_Compliance/` | Yes | No | Yes — expiry date | 70% | 95% |
| A-06 | Company Registration | OPT | Appendix F | `02_Corporate/` | Yes | No | Yes | 70% | 90% |

---

## 12. Section Counts by Category

| Category | Sections | M-ALL | Conditional/Optional |
|---|---|---|---|
| Corporate and Partnership | 12 | 9 | 3 |
| Understanding and Solution | 17 | 3 | 14 |
| Scope and Delivery | 16 | 8 | 8 |
| People | 3 | 1 | 2 |
| Commercial and Governance | 6 | 4 | 2 |
| Compliance and Credentials | 12 | 8 | 4 |
| References | 3 | 1 | 2 |
| Support and Managed Services | 7 | 0 | 7 |
| Appendices | 6 | 2 | 4 |
| **Total** | **82** | **36** | **46** |

> **Section count note:** 82 is the complete section universe. The in-scope count per proposal is determined by PROPOSAL_PATTERN_ENGINE.md scoping rules. Typical in-scope counts: Pattern 13 (AMS) = 43 sections (39 excluded); Pattern 1 (HCM Full Suite) = ~57–65 sections; Pattern 9 (EBS Implementation) = ~55 sections. Section S-38 remains in the library at 82 total — it is conditionally excluded for AMS (not removed).

---

## 13. Automation Gap Summary

The table below summarises sections that are currently at 0% automation and represent the highest priority gaps for the Proposal Factory.

| ID | Section | Current % | Gap Driver |
|---|---|---|---|
| S-47 | Named Consultant CVs | 0% | ADR-001 — APPTime only; no automation possible for full CVs |
| S-48 | Consultant Profiles | 0% | APPTime only |
| S-50 | Risk Register | 5% | Risk Library Standard defined (WP18B); content population pending — automation will improve to L3 once Risk Library entries approved |
| S-52 | Commercials / Pricing | 0% | Commercial Director authority — not automatable |
| S-44 | Disaster Recovery | 0% | `05_Methodologies/Disaster_Recovery/` empty |
| S-65 | POPIA Policy | 0% | OAR-E01 — document not yet obtained |
| S-66 | PAIA Manual | 0% | OAR-E02 — document not yet obtained |

---

*PROPOSAL_SECTION_LIBRARY.md v1.2 | WP18A — Proposal Factory Architecture | Updated WP18C.2 2026-06-26*  
*82 sections defined. Extends PROPOSAL_STRUCTURE_LIBRARY.md (WP12) to full factory scope.*  
*v1.2: SI-001 applied — S-38 marked EXCL-AMS; SI-007 applied — S-71/S-72 content boundaries defined; Section 1 updated with PROPOSAL_PATTERN_ENGINE.md scoping reference; Section 12 in-scope count note added.*
