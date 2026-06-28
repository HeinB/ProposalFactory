---
document_id: METHODOLOGY-LIBRARY-STANDARD
title: "Methodology Library Standard"
version: "1.0"
status: "Approved — WP18B"
created: "2026-06-25"
created_by: "WP18B — Methodology & Risk Library Foundation"
category: "Governance Standard"
scope: "Defines the governed structure, metadata standard, naming convention, authoring workflow, approval process, and cross-reference rules for the APPSolve Methodology Library. This document governs all content in 05_Methodologies/ and is the authoritative standard for authoring, approving, and maintaining methodology documents."
---

# Methodology Library Standard

**Date:** 2026-06-25 | **Version:** 1.0 | **Status:** Approved  
**Work Package:** WP18B — Methodology & Risk Library Foundation  
**Governs:** `05_Methodologies/` — all methodology documents

---

## 1. Purpose

The Methodology Library is a first-class source library for the Proposal Factory. It provides approved, reusable methodology content that the Proposal Assembly Engine retrieves to populate methodology and delivery sections of every proposal.

A methodology document describes HOW APPSolve delivers a type of engagement. It does not describe a specific client's project. It is not a project plan. It is the governed, repeatable framework that APPSolve applies consistently, adapted to each client's context.

This Standard defines:
- What a methodology document is (and is not)
- The folder structure and naming convention
- The metadata schema (frontmatter)
- The internal section structure
- The authoring and approval workflow
- How methodology documents integrate with the Proposal Factory pipeline

---

## 2. Design Principles

Four principles govern the Methodology Library:

**P1 — Write once, cite many.** Cross-BU documents are authored once and referenced from Oracle, Acumatica, and BeBanking tenders. They are never copy-pasted and edited per tender — changes are made in one place and propagate everywhere the document is cited.

**P2 — Structure for extraction.** Each methodology document is written in named sections. The Proposal Assembly Engine pulls individual sections ("our testing approach", "our cutover process") without including the full document. Every section must stand alone and be coherent when read in isolation.

**P3 — Framework separate from execution.** A methodology document describes HOW. It does not describe a specific client's project. Evaluator credibility comes from the framework being structured and evidence-based; evidence of having done it comes from reference letters and capability assets cited separately.

**P4 — Authoring from evidence up.** Where historical proposals or approved capability assets exist, extract and formalise what was done. Do not invent approach. Where no evidence exists, conduct BU Lead / SME workshops first, then author.

---

## 3. Scope of the Library

### 3.1 What is a methodology document

A methodology document is any approved document that describes a delivery process, framework, or approach that:

- APPSolve applies consistently across client engagements
- Can be cited in a tender response as evidence of how APPSolve will execute the engagement
- Does not contain client-specific or commercially sensitive information
- Is subject to BU Lead approval before tender use

**Examples:**
- Oracle EBS Implementation Methodology (how we implement Oracle EBS)
- Testing Methodology (how we test every implementation)
- Data Migration Methodology (how we migrate data from any source to any target)
- Go-Live and Cutover Methodology (how we manage go-live events)

### 3.2 What is NOT a methodology document

| Type | Where it belongs |
|---|---|
| Project plan for a specific engagement | `09_Active_Tenders/[TENDER_ID]/` |
| RAID log for a specific project | `09_Active_Tenders/[TENDER_ID]/` |
| Capability asset (what the product does) | `06_Capabilities/` and `07_Approved_Content/` |
| Assumption pack (commercial commitments) | `08_Commercial/Assumptions/` |
| Reference letter | `04_References/` |

---

## 4. Folder Structure

The Methodology Library lives in `05_Methodologies/`. The current folder structure has 7 subfolders. WP18B extends this with Cross_BU, Oracle, Acumatica, and BeBanking subfolders aligned to the 22-document plan.

**Note:** The OneDrive sync restriction prevents creating new subdirectories in this session. The folder structure below is the target state. The 7 current subfolders remain. New subfolders must be created by the user outside a Claude Code session.

### 4.1 Target folder structure

```
05_Methodologies/
│
├── METHODOLOGY_INDEX.md                     ← Master index: all methodology documents
│
├── Implementation/                          ← (exists) Platform-specific implementation methodologies
│   ├── W2S1-005-ORA-ImplementationMethodology.md  (APPROVED — Oracle)
│   ├── W5-METH-001-ERP-ImplementationMethodology.md  (APPROVED — Cross-BU; currently in 07_Approved_Content)
│   ├── METH-O01_EBS_Implementation.md       (target — to be authored)
│   ├── METH-O03_Cloud_Fusion_Implementation.md  (target)
│   ├── METH-A01_SureStep_Implementation.md  (target)
│   └── METH-B01_Client_Onboarding.md        (target)
│
├── Cross_BU/                                ← (target) 7 shared frameworks (product-agnostic)
│   ├── METH-X01_Project_Management.md       (target)
│   ├── METH-X02_Data_Migration.md           (target)
│   ├── METH-X03_Change_Management_Training.md  (target)
│   ├── METH-X04_Testing_Methodology.md      (target)
│   ├── METH-X05_Go_Live_Cutover.md          (target)
│   ├── METH-X06_Quality_Assurance.md        (target)
│   └── METH-X07_Risk_Management.md          (target)
│
├── Testing/                                 ← (exists, empty) Redirect to Cross_BU/METH-X04
├── Project_Management/                      ← (exists, empty) Redirect to Cross_BU/METH-X01
├── Managed_Services/                        ← (exists, empty) Will contain METH-O06, METH-A04, METH-B04
├── Disaster_Recovery/                       ← (exists, empty) Will contain METH-O04 DR sections
├── Security/                                ← (exists, empty) Will contain security methodology
├── Support/                                 ← (exists, empty) Will contain support transition docs
│
├── Oracle/                                  ← (target) Oracle-specific methodologies
│   ├── METH-O02_EBS_Upgrade.md              (target)
│   ├── METH-O04_OCI_Infrastructure.md       (target)
│   ├── METH-O05_OIC_Integration.md          (target)
│   ├── METH-O06_Oracle_Managed_Services.md  (target)
│   └── METH-O07_APEX_Development.md         (target)
│
├── Acumatica/                               ← (target) Acumatica-specific methodologies
│   ├── METH-A02_Manufacturing_Approach.md   (target)
│   ├── METH-A03_Payroll_Approach.md         (target)
│   └── METH-A04_Acumatica_Managed_Services.md  (target)
│
└── BeBanking/                               ← (target) BeBanking-specific methodologies
    ├── METH-B02_ERP_Integration.md          (target)
    ├── METH-B03_Bank_Connectivity_Setup.md  (target)
    └── METH-B04_Support_Reconciliation.md   (target)
```

### 4.2 Resolution of W5-METH-001 deployment anomaly

W5-METH-001 (`07_Approved_Content/Approved/Cross_BU/W5-METH-001-ERP-ImplementationMethodology.md`) has `kb_destination: 05_Methodologies/Implementation/` in its frontmatter but was not deployed there. **Action required:** Copy W5-METH-001 to `05_Methodologies/Implementation/` to align with its stated kb_destination and make it discoverable as a methodology asset. The copy in `07_Approved_Content/Approved/Cross_BU/` may remain as an additional reference.

---

## 5. Document ID and Naming Convention

### 5.1 Naming scheme

| Pattern | Applies to | Example |
|---|---|---|
| `W[n]S[m]-[NNN]-[BU]-[ShortName]` | Wave-produced assets already in KB | `W2S1-005-ORA-ImplementationMethodology.md` |
| `METH-[X/O/A/B][NN]_[ShortDescription].md` | New methodology documents | `METH-O03_Cloud_Fusion_Implementation.md` |

**Methodology ID prefixes:**
- `METH-X` — Cross-BU (platform-agnostic)
- `METH-O` — Oracle-specific
- `METH-A` — Acumatica-specific
- `METH-B` — BeBanking-specific

### 5.2 Document ID in frontmatter

The `document_id` in the YAML frontmatter must match the filename (without .md extension), using hyphens instead of underscores. Example: `METH-O03-Cloud-Fusion-Implementation`.

---

## 6. Metadata Schema (Frontmatter)

Every methodology document must have the following YAML frontmatter:

```yaml
---
document_id: [METH-XX-NN or W-format ID]
title: "[Full document title]"
version: "[version number] [APPROVED / DRAFT]"
source_status: [Approved / Draft]
approved_for_reuse: [Yes / No]
approved_by: "[Approver name]"
approval_date: "[YYYY-MM-DD]"
reviewed_by: "[Reviewer name]"
review_date: "[YYYY-MM-DD]"
review_notes: "[BU decisions, governance outcomes, validation notes]"
bu: [Oracle / Acumatica / BeBanking / Cross-Platform]
scope: "[One-sentence description of what this document covers and does not cover]"
platforms:
  - "[Platform 1]"
  - "[Platform 2]"
sources:
  - "[Source 1 — document name, date]"
  - "[Source 2]"
pre_tender_checks:
  - "[Check ID]: [Short description]"
created: "[YYYY-MM-DD]"
created_by: "[Author]"
kb_destination: "[canonical file path including filename]"
wave: "[Wave number or N/A]"
---
```

**Required fields:** `document_id`, `title`, `version`, `approved_for_reuse`, `approved_by`, `approval_date`, `bu`, `scope`

**Conditional fields:**
- `platforms` — required for Cross-BU documents; optional for single-BU documents
- `pre_tender_checks` — required for any document containing governance-sensitive claims
- `sources` — required; if no source material exists, document the SME basis

---

## 7. Internal Section Structure

Every methodology document must contain the following sections. Optional sections are marked *(optional)*.

### 7.1 Standard section structure

```
## 1. Executive Summary
## 2. Delivery Philosophy / Approach Principles
## 3. Methodology Overview (phase or framework summary)
## 4–N. Phase / Framework Sections (one section per phase, theme, or component)
## [N+1]. Integration with Other Methodologies *(optional — cite related METH documents)*
## [N+2]. Risk Register *(optional — see Section 7.2 below)*
## [N+3]. Client Responsibilities
## [N+4]. Approval Record and Pre-Tender Checks
## Appendix A–D. Platform-Specific Additions *(optional — for Cross-BU documents)*
```

### 7.2 Risk Register section in methodology documents

**Each methodology document may include a Risk Register section** containing 3–8 risks most relevant to that methodology's engagement type. These risks are sourced from the Risk Library (RISK_LIBRARY_STANDARD.md) rather than authored from scratch.

The Risk Register section serves two purposes:
1. In the methodology document itself: provides a standalone risk-aware methodology section
2. As a Risk Library input: contributes approved risk entries back into the Risk Library taxonomy

Format of risks in a methodology document risk section:

```markdown
| Risk ID | Risk | Likelihood | Impact | Rating | Mitigation |
|---|---|---|---|---|---|
| [METH-XX-NN-R01] | [Risk description] | [L/M/H] | [L/M/H] | [LOW/MEDIUM/HIGH/CRITICAL] | [Mitigation approach] |
```

Risk IDs in methodology documents follow the format `[METH-ID]-R[NN]`, e.g., `METH-O03-R01`.

### 7.3 Section extraction rules

Each section must stand alone when extracted for proposal assembly. Rules:
- No pronoun references to previous sections ("As described above...")
- Each section must open with a clear statement of what it describes
- Internal cross-references use document ID, not "the previous section"
- Governance-sensitive claims must have a source citation or pre-tender check reference

---

## 8. Approval Workflow

Identical to the Capability Library approval workflow:

```
1. DRAFT       — AI-assisted draft; not approved for reuse
2. CANDIDATE   — BU Lead review requested; `approved_for_reuse: No`
3. REVIEW_REQUIRED — BU Lead has specific decisions outstanding; `approved_for_reuse: No`
4. APPROVED    — BU Lead sign-off; `approved_for_reuse: Yes`
```

| Stage | Who | What |
|---|---|---|
| Draft | AI (with SME input if required) | Create document following this standard |
| Candidate | AI submits to BU Lead | BU Lead reviews all claims, governance checks, pre-tender checks |
| Review Required | BU Lead identifies open decisions | AI implements decisions; BU Lead confirms resolution |
| Approved | BU Lead | Signs off; sets `approved_for_reuse: Yes` |

**Gate rule:** No methodology document may be used in a tender response until `approved_for_reuse: Yes` is set by the BU Lead. This is the same gate as capability assets (W-format assets) and assumption packs.

**Exception:** A new methodology document may be used in a single tender response if Commercial Director provides written exception approval. The document must still complete the approval workflow before use in subsequent tenders.

---

## 9. Version Control

| Version | Meaning | Trigger |
|---|---|---|
| 1.0 | Initial approved version | BU Lead initial approval |
| 1.1 | Minor update (wording, pre-tender check update) | Change does not affect commercial commitments |
| 2.0 | Major revision (structural change, new phases, new evidence basis) | Significant update to delivery approach |

Version history must be maintained in the document as a change log table below the approval record.

**Restriction:** Documents in Approved status may not be edited without version increment and new BU Lead sign-off.

---

## 10. Cross-Reference Rules

### 10.1 Cross-BU to BU-specific

Cross-BU methodology documents (METH-X01 to X07) are cited by reference from BU-specific documents. BU-specific documents do not reproduce Cross-BU content — they reference it and add BU-specific additions only.

Example: METH-O01 (Oracle EBS Implementation) cites METH-X04 (Testing Methodology) for the testing approach and adds Oracle EBS-specific test scripts and Oracle SIT conventions as a short addition.

### 10.2 Methodology to Risk Library

Risk Register sections in methodology documents source risk entries from the Risk Library (RISK_LIBRARY_STANDARD.md). Risk entries are not invented per-document — they are selected from the governed Risk Library and customised with methodology-specific mitigation language.

### 10.3 Methodology to Assumption Library

Where a methodology document references delivery commitments that are governed by assumption packs, the document must cite the relevant assumption pack section rather than reproduce the assumption language. Example: METH-X05 (Cutover) references HCM-CUT-005 (parallel run default) rather than restating the assumption.

### 10.4 Methodology to Capability Library

Methodology documents do not reproduce capability descriptions. Where the methodology references a specific product delivery pattern (e.g., OIC as mandatory architecture component), it cites the relevant capability asset (W2S1-001 for Oracle Fusion, W5-METH-001 Appendix C for OIC) rather than reproducing capability content.

---

## 11. The 22-Document Library Plan

The complete target state for the Methodology Library is defined in `00_Governance/Archive/METHODOLOGY_LIBRARY_DESIGN.md` (2026-06-05). That document specifies 22 methodology documents with full section structures, source material guidance, extraction yield estimates, and authoring prerequisites.

**WP18B does not author any methodology documents.** WP18B designs the governance framework that future work packages will use. The 22 documents are the authoring pipeline for WP18B+ work packages.

**Priority ranking** (from METHODOLOGY_LIBRARY_DESIGN.md):

| Rank | Code | Document | BU | Effort |
|---|---|---|---|---|
| 1 | METH-X01 | Project Management Framework | Cross | 50–70% extractable |
| 2 | METH-O01 | Oracle EBS Implementation Methodology | Oracle | 60–75% extractable |
| 3 | METH-O03 | Oracle Cloud (Fusion) Implementation Methodology | Oracle | 50–65% extractable |
| 4 | METH-X04 | Testing Methodology | Cross | 30–50% extractable |
| 5 | METH-X02 | Data Migration Methodology | Cross | 40–60% extractable |
| 6 | METH-O06 | Oracle Managed Services Methodology | Oracle | 5–15% extractable; SME required |
| 7 | METH-A01 | Acumatica SureStep Implementation Methodology | Acumatica | 0%; SME workshop required |
| 8 | METH-X05 | Go-Live and Cutover Methodology | Cross | 30–40% extractable |
| 9 | METH-X03 | Change Management and Training Approach | Cross | 30–50% extractable |
| 10 | METH-B01 | BeBanking Client Onboarding Methodology | BeBanking | 0%; SME briefing required |
| 11 | METH-X07 | Risk Management Approach | Cross | 30–40% extractable |
| 12 | METH-O05 | OIC Integration Delivery Methodology | Oracle | 15–25% extractable |
| 13 | METH-X06 | Quality Assurance Framework | Cross | 0%; author from scratch |
| 14 | METH-A02 | Acumatica Manufacturing Approach | Acumatica | 0%; SME required |
| 15 | METH-B02 | BeBanking ERP Integration Methodology | BeBanking | 5–15% extractable |
| 16 | METH-A03 | Acumatica Payroll Approach | Acumatica | 0%; SME required |
| 17 | METH-B04 | BeBanking Support and Reconciliation Model | BeBanking | 60% once METH-O06 done |
| 18 | METH-O04 | OCI Infrastructure Deployment Methodology | Oracle | 0%; OCI specialist required |
| 19 | METH-A04 | Acumatica Managed Services Methodology | Acumatica | 60% once METH-O06 done |
| 20 | METH-B03 | BeBanking Bank Connectivity Setup | BeBanking | 0%; technical team required |
| 21 | METH-O02 | Oracle EBS Upgrade Methodology | Oracle | 10–20% extractable |
| 22 | METH-O07 | Oracle APEX Development Methodology | Oracle | 0%; APEX lead required |

---

## 12. Integration with Proposal Factory

The Methodology Library integrates with the Proposal Factory at Stage 6 (Methodology Selection) of the pipeline:

```
Stage 6 — Select Methodology and Delivery Pattern
  → Input: Tender Profile (platform, engagement type)
  → Action: Match to METHODOLOGY_INDEX.md → select applicable METH document(s)
  → Output: [TENDER_ID]_METHODOLOGY_SELECTION.md — selected METH IDs + sections to extract
```

The Proposal Assembly Engine (WP18B) retrieves the selected methodology sections and inserts them into the following proposal sections:

| Methodology sections used | Target proposal section |
|---|---|
| Implementation Methodology overview + phases | S-34 (Implementation Methodology) |
| Testing approach | S-39 (Testing Strategy) |
| Data migration approach | S-40 (Data Migration) |
| Training plan | S-41 (Training Plan) |
| Cutover / go-live approach | S-42 (Cutover / Go-Live) |
| Hypercare approach | S-43 (Hypercare / Transition) |
| Risk management approach | S-37 (RAID Framework) — feeds risk entries |
| Project governance framework | S-36 (Project Governance) |
| Change management approach | S-38 (Change Control) |

**Source hierarchy within methodology selection:**
1. `approved_for_reuse: Yes` methodology document → DIRECT EXTRACT
2. DELIVERY_PATTERN_LIBRARY (phase structure, durations, resource model) → EXTRACT
3. AI-generated methodology (last resort) → AI-GENERATE with mandatory BU Lead review

---

## 13. METHODOLOGY_INDEX.md

Every methodology document must be registered in `05_Methodologies/METHODOLOGY_INDEX.md`. This index is the primary lookup table for the Proposal Assembly Engine.

**Format:**

```markdown
| METH ID | Title | BU | Approved | Platforms | Sections available |
|---|---|---|---|---|---|
| W2S1-005 | Oracle Implementation Methodology | Oracle | Yes — 2026-06-12 | Oracle Fusion, Oracle EBS | Phases 1–6, Project Governance, Platform Considerations |
| W5-METH-001 | ERP Implementation Methodology (Cross-BU) | Cross | Yes — 2026-06-14 | All | Phases 1–6, Project Governance, Platform Appendices |
| METH-X04 | Testing Methodology | Cross | [Pending] | All | [Sections TBD when authored] |
```

The METHODOLOGY_INDEX.md does not yet exist. Creating it is an action item for the WP18B implementation plan.

---

## 14. Governance Restrictions Applicable to All Methodology Documents

The following governance rules from the KB Governance Programme apply to all methodology documents:

| Rule | Requirement |
|---|---|
| No "Gold Partner" | Oracle partnership is "Oracle Level 1 Partner" only |
| "50+ Senior Consultants" | This exact phrasing for headcount claims |
| "over 23 years" | Company age expression |
| OPN annual revalidation | Check current partnership status before use in any Oracle tender |
| BEE certificate | No BEE content in methodology documents (methodology is not a compliance document) |
| Named client references | Methodology documents do not name clients; client names in external proposals require pre-tender check confirmation |
| No DFA, CCBA, SAA, Redpath as named references | Applies to all documents |

---

*METHODOLOGY_LIBRARY_STANDARD.md v1.0 | WP18B — Methodology & Risk Library Foundation | 2026-06-25*  
*Governing standard for all content in 05_Methodologies/. 22-document library plan. Approval workflow identical to Capability Library.*
