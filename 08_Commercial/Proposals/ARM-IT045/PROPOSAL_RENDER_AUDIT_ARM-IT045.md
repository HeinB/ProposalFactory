---
document_id: RENDER-AUDIT-ARM-IT045-V1
title: "Proposal Render Audit — ARM-IT045"
version: "1.0"
status: "COMPLETE"
rendered_at: "2026-06-30T07:23:43.104719+00:00"
renderer_version: "1.0"
manifest_id: "ARM-IT045-PSM-20260629-100759"
---

# Proposal Render Audit — ARM-IT045

**Tender:** ARM-IT045  
**Platform:** Oracle EBS  
**Engagement Type:** AMS  
**Rendered:** 2026-06-30T07:23:43.104719+00:00  
**Renderer Version:** 1.0  

---

## 1. Render Summary

| Metric | Count |
|---|---|
| Sections in manifest | 82 |
| Assembly sequence length | 45 |
| RENDERED | 25 |
| PLACEHOLDER | 17 |
| AI-DRAFT | 3 |
| NOT_FOUND | 0 |
| SKIPPED (excluded) | 0 |

---

## 2. Governance Flags

- GOV-BBEE-001: B-BBEE cert expires 2026-07-31 (OAR-C01/C02/A01); verify renewal before submission after that date
- GOV-ADR-001: CVs (S-47, S-48, A-02) from APPTime only — never from KB records

---

## 3. Section Audit Trail

| Section | Name | Status | Render Status | Method | Assets Found | Assets Missing | Notes |
|---|---|---|---|---|---|---|---|
| A-01 | Complete Assumption Schedule | MANDATORY | RENDERED | DIRECT | OIC_ASSUMPTIONS_V1.md | — | DIRECT: rendered from OIC_ASSUMPTIONS_V1.md |
| A-02 | Consultant CVs | DEFAULT_EXCLUDED | SKIPPED | PLACEHOLDER | — | — | Excluded from assembly sequence (status: DEFAULT_EXCLUDED) |
| A-03 | Reference Letters | DEFAULT_EXCLUDED | SKIPPED | DIRECT | — | — | Excluded from assembly sequence (status: DEFAULT_EXCLUDED) |
| A-04 | Certifications and Compliance | MANDATORY | PLACEHOLDER | DIRECT | — | — | DIRECT — no source_assets declared; rendered as PLACEHOLDER |
| A-05 | B-BBEE Certificate | MANDATORY | PLACEHOLDER | DIRECT | — | — | DIRECT — no source_assets declared; rendered as PLACEHOLDER |
| A-06 | Company Registration | DEFAULT_EXCLUDED | SKIPPED | DIRECT | — | — | Excluded from assembly sequence (status: DEFAULT_EXCLUDED) |
| S-01 | Cover Page / Transmittal | MANDATORY | RENDERED | TEMPLATE | — | — | TEMPLATE; placeholders: ['client_name', 'submission_date', 'rfp_reference', 'tender_title'] |
| S-02 | Table of Contents | MANDATORY | RENDERED | TEMPLATE | — | — | TOC auto-generated from assembly sequence |
| S-03 | Company Overview | MANDATORY | RENDERED | DIRECT | W1S1-001-CORP-CompanyOverview.md | — | DIRECT: rendered from W1S1-001-CORP-CompanyOverview.md |
| S-04 | Company History | MANDATORY | RENDERED | DIRECT | W1S1-002-CORP-CompanyHistory.md | — | DIRECT: rendered from W1S1-002-CORP-CompanyHistory.md |
| S-05 | Awards and Recognition | MANDATORY | RENDERED | DIRECT | W1S1-006-CORP-AwardsRecognition.md | — | DIRECT: rendered from W1S1-006-CORP-AwardsRecognition.md |
| S-06 | Delivery Model | MANDATORY | RENDERED | DIRECT | W1S1-007-CORP-DeliveryModel.md | — | DIRECT: rendered from W1S1-007-CORP-DeliveryModel.md |
| S-07 | Geographic Presence | MANDATORY | RENDERED | DIRECT | W1S1-008-CORP-GeographicPresence.md | — | DIRECT: rendered from W1S1-008-CORP-GeographicPresence.md |
| S-08 | Key Differentiators | MANDATORY | RENDERED | DIRECT | W1S1-009-CORP-KeyDifferentiators.md | — | DIRECT: rendered from W1S1-009-CORP-KeyDifferentiators.md |
| S-09 | Oracle Partnership | MANDATORY | RENDERED | DIRECT | W1S1-003-ORA-OraclePartnership.md | — | DIRECT: rendered from W1S1-003-ORA-OraclePartnership.md |
| S-10 | Acumatica Partnership | EXCLUDED | SKIPPED | DIRECT | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-11 | BeBanking Product Overview | EXCLUDED | SKIPPED | DIRECT | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-12 | B-BBEE Compliance Statement | MANDATORY | PLACEHOLDER | DIRECT | — | — | DIRECT — no source_assets declared; rendered as PLACEHOLDER |
| S-13 | Executive Summary | MANDATORY | AI-DRAFT | AI-GENERATE | — | — | AI-GENERATE: draft required; instruction: Mandatory human review; tailor to tender-specific win themes |
| S-14 | Understanding of Requirements | MANDATORY | AI-DRAFT | AI-GENERATE | — | — | AI-GENERATE: draft required; instruction: Mandatory human review; drawn from tender RFP/RFQ document |
| S-15 | Proposed Solution Overview | MANDATORY | PLACEHOLDER | MERGE | — | — | MERGE — no source_assets declared; rendered as PLACEHOLDER |
| S-16 | Oracle Fusion HCM Capability | DEFAULT_EXCLUDED | SKIPPED | MERGE | — | — | Excluded from assembly sequence (status: DEFAULT_EXCLUDED) |
| S-17 | Oracle Fusion ERP Capability | DEFAULT_EXCLUDED | SKIPPED | MERGE | — | — | Excluded from assembly sequence (status: DEFAULT_EXCLUDED) |
| S-18 | Oracle EBS Capability | MANDATORY | RENDERED | DIRECT | W2S1-002-ORA-EBSCapability.md | — | DIRECT: rendered from W2S1-002-ORA-EBSCapability.md |
| S-19 | Oracle OIC / Integration Capability | OPTIONAL_SELECTED | RENDERED | DIRECT | W4-INT-001-ORA-OICAccelerators.md | — | DIRECT: rendered from W4-INT-001-ORA-OICAccelerators.md |
| S-20 | Oracle DBA Capability | OPTIONAL_SELECTED | RENDERED | DIRECT | W2S1-003-ORA-DBAExecutiveSummary.md | — | DIRECT: rendered from W2S1-003-ORA-DBAExecutiveSummary.md |
| S-21 | Oracle Managed Services Capability | MANDATORY | RENDERED | DIRECT | W2S1-004-ORA-ManagedServicesSupportModel.md | — | DIRECT: rendered from W2S1-004-ORA-ManagedServicesSupportModel.md |
| S-22 | OCI Infrastructure | DEFAULT_EXCLUDED | SKIPPED | AI-GENERATE | — | — | Excluded from assembly sequence (status: DEFAULT_EXCLUDED) |
| S-23 | Acumatica Financials | EXCLUDED | SKIPPED | DIRECT | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-24 | Acumatica Distribution | EXCLUDED | SKIPPED | DIRECT | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-25 | Acumatica Manufacturing | EXCLUDED | SKIPPED | DIRECT | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-26 | Acumatica CRM | EXCLUDED | SKIPPED | DIRECT | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-27 | Acumatica Other Modules | EXCLUDED | SKIPPED | DIRECT | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-28 | Acumatica Managed Services | EXCLUDED | SKIPPED | DIRECT | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-29 | BeBanking H2H Banking | EXCLUDED | SKIPPED | MERGE | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-30 | Scope of Work — Inclusions | MANDATORY | PLACEHOLDER | EXTRACT | — | — | EXTRACT — no source_assets declared; rendered as PLACEHOLDER |
| S-31 | Scope of Work — Exclusions | MANDATORY | PLACEHOLDER | EXTRACT | — | — | EXTRACT — no source_assets declared; rendered as PLACEHOLDER |
| S-32 | Deliverables | MANDATORY | PLACEHOLDER | EXTRACT | — | — | EXTRACT — no source_assets declared; rendered as PLACEHOLDER |
| S-33 | Dependencies | MANDATORY | PLACEHOLDER | EXTRACT | — | — | EXTRACT — no source_assets declared; rendered as PLACEHOLDER |
| S-34 | Implementation Methodology | EXCLUDED | SKIPPED | DIRECT | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-35 | Project Plan / Timeline | EXCLUDED | SKIPPED | TEMPLATE | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-36 | Project Governance | MANDATORY | PLACEHOLDER | EXTRACT | — | — | EXTRACT — no source_assets declared; rendered as PLACEHOLDER |
| S-37 | RAID Framework | MANDATORY | PLACEHOLDER | MERGE | — | — | MERGE — no source_assets declared; rendered as PLACEHOLDER |
| S-38 | Change Control Framework | EXCLUDED | SKIPPED | DIRECT | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-39 | Testing Strategy | EXCLUDED | SKIPPED | EXTRACT | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-40 | Data Migration | EXCLUDED | SKIPPED | EXTRACT | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-41 | Training Plan | EXCLUDED | SKIPPED | EXTRACT | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-42 | Cutover / Go-Live Plan | EXCLUDED | SKIPPED | EXTRACT | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-43 | Hypercare / Post-Go-Live Transition | EXCLUDED | SKIPPED | EXTRACT | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-44 | Disaster Recovery | DEFAULT_EXCLUDED | SKIPPED | PLACEHOLDER | — | — | Excluded from assembly sequence (status: DEFAULT_EXCLUDED) |
| S-45 | Security Architecture | DEFAULT_EXCLUDED | SKIPPED | EXTRACT | — | — | Excluded from assembly sequence (status: DEFAULT_EXCLUDED) |
| S-46 | Team Structure | EXCLUDED | SKIPPED | TEMPLATE | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-47 | Named Consultant CVs | EXCLUDED | SKIPPED | PLACEHOLDER | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-48 | Consultant Profiles (Summary) | EXCLUDED | SKIPPED | PLACEHOLDER | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-49 | Key Assumptions (Body Section) | MANDATORY | RENDERED | DIRECT | OIC_ASSUMPTIONS_V1.md | — | DIRECT: rendered from OIC_ASSUMPTIONS_V1.md |
| S-50 | Risk Register | MANDATORY | AI-DRAFT | AI-GENERATE | — | — | AI-GENERATE: draft required; instruction: Mandatory human review; Risk Library standard defined (WP18B) |
| S-51 | Commercial Assumptions | MANDATORY | RENDERED | DIRECT | OIC_ASSUMPTIONS_V1.md | — | DIRECT: rendered from OIC_ASSUMPTIONS_V1.md |
| S-52 | Commercials / Pricing | MANDATORY | PLACEHOLDER | PLACEHOLDER | — | — | PLACEHOLDER: Commercial Director authority; never expose rates; SI-006: S-49 must precede this |
| S-53 | Rate Card Basis | DEFAULT_EXCLUDED | SKIPPED | PLACEHOLDER | — | — | Excluded from assembly sequence (status: DEFAULT_EXCLUDED) |
| S-54 | Estimation Basis | DEFAULT_EXCLUDED | SKIPPED | PLACEHOLDER | — | — | Excluded from assembly sequence (status: DEFAULT_EXCLUDED) |
| S-55 | Compliance Schedule | MANDATORY | PLACEHOLDER | EXTRACT | — | — | EXTRACT — no source_assets declared; rendered as PLACEHOLDER |
| S-56 | Company Registration | MANDATORY | PLACEHOLDER | DIRECT | — | — | DIRECT — no source_assets declared; rendered as PLACEHOLDER |
| S-57 | Tax Clearance | MANDATORY | PLACEHOLDER | DIRECT | — | — | DIRECT — no source_assets declared; rendered as PLACEHOLDER |
| S-58 | Directors' Resolution | MANDATORY | PLACEHOLDER | DIRECT | — | — | DIRECT — no source_assets declared; rendered as PLACEHOLDER |
| S-59 | B-BBEE Certificate | MANDATORY | PLACEHOLDER | DIRECT | — | — | DIRECT — no source_assets declared; rendered as PLACEHOLDER |
| S-60 | Public Liability Insurance | MANDATORY | PLACEHOLDER | DIRECT | — | — | DIRECT — no source_assets declared; rendered as PLACEHOLDER |
| S-61 | Professional Indemnity | DEFAULT_EXCLUDED | SKIPPED | DIRECT | — | — | Excluded from assembly sequence (status: DEFAULT_EXCLUDED) |
| S-62 | Oracle OPN Certificate | MANDATORY | RENDERED | DIRECT | W1S1-003-ORA-OraclePartnership.md | — | DIRECT: rendered from W1S1-003-ORA-OraclePartnership.md |
| S-63 | Acumatica Partner Certificate | EXCLUDED | SKIPPED | DIRECT | — | — | Excluded from assembly sequence (status: EXCLUDED) |
| S-64 | ISO / Other Certifications | DEFAULT_EXCLUDED | SKIPPED | DIRECT | — | — | Excluded from assembly sequence (status: DEFAULT_EXCLUDED) |
| S-65 | POPIA Policy | DEFAULT_EXCLUDED | SKIPPED | PLACEHOLDER | — | — | Excluded from assembly sequence (status: DEFAULT_EXCLUDED) |
| S-66 | PAIA Manual | DEFAULT_EXCLUDED | SKIPPED | PLACEHOLDER | — | — | Excluded from assembly sequence (status: DEFAULT_EXCLUDED) |
| S-67 | Client References | MANDATORY | RENDERED | TEMPLATE | — | — | TEMPLATE; placeholders: ['client_references_table'] |
| S-68 | Case Studies | DEFAULT_EXCLUDED | SKIPPED | AI-GENERATE | — | — | Excluded from assembly sequence (status: DEFAULT_EXCLUDED) |
| S-69 | Reference Letters | DEFAULT_EXCLUDED | SKIPPED | DIRECT | — | — | Excluded from assembly sequence (status: DEFAULT_EXCLUDED) |
| S-70 | Support Model | MANDATORY | RENDERED | MERGE | W2S1-004-ORA-ManagedServicesSupportModel.md; AMS_ASSUMPTIONS_V1.md | — | MERGE: 2 asset(s) rendered; 0 not found |
| S-71 | SLA Framework | MANDATORY | RENDERED | EXTRACT | AMS_ASSUMPTIONS_V1.md | — | EXTRACT: full body of AMS_ASSUMPTIONS_V1.md included; sub-section extraction not automated — manual curation required |
| S-72 | Incident Management | MANDATORY | RENDERED | EXTRACT | AMS_ASSUMPTIONS_V1.md | — | EXTRACT: full body of AMS_ASSUMPTIONS_V1.md included; sub-section extraction not automated — manual curation required |
| S-73 | Change Request Process | MANDATORY | RENDERED | EXTRACT | AMS_ASSUMPTIONS_V1.md | — | EXTRACT: full body of AMS_ASSUMPTIONS_V1.md included; sub-section extraction not automated — manual curation required |
| S-74 | Resource Model (AMS) | MANDATORY | RENDERED | EXTRACT | AMS_ASSUMPTIONS_V1.md | — | EXTRACT: full body of AMS_ASSUMPTIONS_V1.md included; sub-section extraction not automated — manual curation required |
| S-75 | Release Management | MANDATORY | RENDERED | EXTRACT | AMS_ASSUMPTIONS_V1.md | — | EXTRACT: full body of AMS_ASSUMPTIONS_V1.md included; sub-section extraction not automated — manual curation required |
| S-76 | Monitoring and Reporting | MANDATORY | RENDERED | EXTRACT | AMS_ASSUMPTIONS_V1.md | — | EXTRACT: full body of AMS_ASSUMPTIONS_V1.md included; sub-section extraction not automated — manual curation required |

---

## 4. Governance Constraint Detail

**A-04 — Certifications and Compliance:**
- Never submit a proposal with expired compliance documents

**A-05 — B-BBEE Certificate:**
- B-BBEE cert expires 2026-07-31; never cite BEE status after that date without renewal cert

**S-03 — Company Overview:**
- Never use old company profile; KB-approved content supersedes

**S-06 — Delivery Model:**
- Headcount: 'more than 50 Senior Consultants' ONLY

**S-08 — Key Differentiators:**
- Included when W1S1-009 mandatory (always in corporate block)

**S-09 — Oracle Partnership:**
- Never cite 'Oracle Gold Partner' — expired August 2021. Level 1 Partner only.

**S-12 — B-BBEE Compliance Statement:**
- B-BBEE cert expires 2026-07-31 (OAR-C01/C02/A01); flag if submission after that date

**S-13 — Executive Summary:**
- Never use Candidate_Content/ or Review_Required/ in any tender

**S-19 — Oracle OIC / Integration Capability:**
- HIST-018 billing (R825,170) MUST NEVER appear in external submissions. Section 13.2 (W3S1-009) NEVER external.

**S-21 — Oracle Managed Services Capability:**
- Oracle platforms only; excluded for Acumatica/BeBanking

**S-49 — Key Assumptions (Body Section):**
- SI-006: S-49 Key Assumptions assembled BEFORE S-52 Pricing in all proposals

**S-51 — Commercial Assumptions:**
- Never assemble a fixed-price proposal without the commercial file

**S-52 — Commercials / Pricing:**
- SI-006: S-49 Key Assumptions BEFORE S-52 Pricing in all proposals

**S-55 — Compliance Schedule:**
- Never submit a proposal with expired compliance documents

**S-59 — B-BBEE Certificate:**
- OAR-C01/C02/A01: B-BBEE cert expires 2026-07-31; never cite BEE status after that date without renewal

**S-62 — Oracle OPN Certificate:**
- Never cite 'Oracle Gold Partner' — expired August 2021

**S-67 — Client References:**
- Never cite DFA, CCBA, SAA. Never cite Redpath Mining until Rule 21.5 waived. Never name Hollywood Bets without AM approval. Never name KPMG in PPM/ERP until AM-W4E3-001 cleared.

**S-70 — Support Model:**
- AMS-only section; assembled second in AMS Support block

**S-71 — SLA Framework:**
- SI-007: SLA tier table ONLY (P1=1h, P2=4h, P3=1BD, P4=3BD); response ≠ resolution disclaimer; DO NOT include incident process — belongs in S-72

**S-72 — Incident Management:**
- SI-007: Incident classification process ONLY; escalation path; lifecycle (log→triage→assign→resolve→close→review); DO NOT re-state SLA tier values — reference as 'per S-71 SLA Framework'

**S-73 — Change Request Process:**
- SI-001: This section REPLACES S-38 for all AMS proposals (Pattern 13). Single governing change management section for AMS.

**S-74 — Resource Model (AMS):**
- AMS-only; assembled FIRST in AMS Support block (before S-70)

**S-75 — Release Management:**
- Oracle quarterly release advisory included; regression testing of patch = excluded unless scoped

**S-76 — Monitoring and Reporting:**
- Mailbox monitoring standard; proactive monitoring = separate scope unless contracted

---

## 5. Asset Not Found Register

*All referenced assets located in AssetIndex.*

---

## 6. Human Action Register

Sections requiring human completion or review before submission:

| Section | Name | Render Status | Action Required |
|---|---|---|---|
| A-04 | Certifications and Compliance | PLACEHOLDER | DIRECT — no source_assets declared; rendered as PLACEHOLDER |
| A-05 | B-BBEE Certificate | PLACEHOLDER | DIRECT — no source_assets declared; rendered as PLACEHOLDER |
| S-12 | B-BBEE Compliance Statement | PLACEHOLDER | DIRECT — no source_assets declared; rendered as PLACEHOLDER |
| S-13 | Executive Summary | AI-DRAFT | AI-GENERATE: draft required; instruction: Mandatory human review; tailor to tend |
| S-14 | Understanding of Requirements | AI-DRAFT | AI-GENERATE: draft required; instruction: Mandatory human review; drawn from ten |
| S-15 | Proposed Solution Overview | PLACEHOLDER | MERGE — no source_assets declared; rendered as PLACEHOLDER |
| S-30 | Scope of Work — Inclusions | PLACEHOLDER | EXTRACT — no source_assets declared; rendered as PLACEHOLDER |
| S-31 | Scope of Work — Exclusions | PLACEHOLDER | EXTRACT — no source_assets declared; rendered as PLACEHOLDER |
| S-32 | Deliverables | PLACEHOLDER | EXTRACT — no source_assets declared; rendered as PLACEHOLDER |
| S-33 | Dependencies | PLACEHOLDER | EXTRACT — no source_assets declared; rendered as PLACEHOLDER |
| S-36 | Project Governance | PLACEHOLDER | EXTRACT — no source_assets declared; rendered as PLACEHOLDER |
| S-37 | RAID Framework | PLACEHOLDER | MERGE — no source_assets declared; rendered as PLACEHOLDER |
| S-50 | Risk Register | AI-DRAFT | AI-GENERATE: draft required; instruction: Mandatory human review; Risk Library s |
| S-52 | Commercials / Pricing | PLACEHOLDER | PLACEHOLDER: Commercial Director authority; never expose rates; SI-006: S-49 mus |
| S-55 | Compliance Schedule | PLACEHOLDER | EXTRACT — no source_assets declared; rendered as PLACEHOLDER |
| S-56 | Company Registration | PLACEHOLDER | DIRECT — no source_assets declared; rendered as PLACEHOLDER |
| S-57 | Tax Clearance | PLACEHOLDER | DIRECT — no source_assets declared; rendered as PLACEHOLDER |
| S-58 | Directors' Resolution | PLACEHOLDER | DIRECT — no source_assets declared; rendered as PLACEHOLDER |
| S-59 | B-BBEE Certificate | PLACEHOLDER | DIRECT — no source_assets declared; rendered as PLACEHOLDER |
| S-60 | Public Liability Insurance | PLACEHOLDER | DIRECT — no source_assets declared; rendered as PLACEHOLDER |

---

*PROPOSAL_RENDER_AUDIT_ARM-IT045.md | proposal_renderer.py v1.0 | 2026-06-30T07:23:43.104719+00:00*