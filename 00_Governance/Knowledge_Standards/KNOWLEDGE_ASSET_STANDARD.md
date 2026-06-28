---
document_id: KNOWLEDGE-ASSET-STANDARD-V1
title: "Universal Knowledge Asset Standard — V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-26"
created_by: "WP18B-EXT.3 — Universal Knowledge Asset Governance Standard"
approved_by: "Architecture — WP18B-EXT.3"
approved_date: "2026-06-26"
approved_for_reuse: true
category: "Governance / Knowledge Standards"
scope: "Master governance standard for all knowledge assets in the APPSolve Proposal Factory. All existing and future knowledge libraries must conform to this standard."
related_documents:
  - KNOWLEDGE_ASSET_LIFECYCLE.md
  - KNOWLEDGE_METADATA_STANDARD.md
  - KNOWLEDGE_GOVERNANCE_RULES.md
  - KNOWLEDGE_RELATIONSHIP_MODEL.md
  - WP18B_EXT3_UNIVERSAL_GOVERNANCE_REPORT.md
---

# Universal Knowledge Asset Standard — V1.0

**Work Package:** WP18B-EXT.3  
**Status:** APPROVED  
**Authority:** This standard takes precedence over all library-specific governance standards where they conflict on matters covered here. Library-specific standards may extend this standard for asset-type details but may not contradict it.

---

## 1. Purpose

The APPSolve Proposal Factory has evolved multiple governed knowledge libraries independently:

| Library | Governing Standard | Created |
|---|---|---|
| Capability Library | MASTER_CAPABILITY_INDEX.md (v1.2) | WP7 — 2026-06-14 |
| Assumption Library | ASSUMPTION_LIBRARY_ROADMAP.md (v1.7) | WP11 — 2026-06-15 |
| Risk Library | RISK_LIBRARY_STANDARD.md + RISK_METADATA_STANDARD.md | WP18B — 2026-06-25 |
| Methodology Library | (METHODOLOGY_LIBRARY_STANDARD.md — WP18B) | WP18B — 2026-06-25 |

Each library invented its own governance model. The result is inconsistent lifecycle states, divergent metadata schemas, and no cross-library traceability. This standard replaces the ad hoc approach with a single governance framework that all libraries must follow.

**Goal:** Any future knowledge library can be created by following this standard, without inventing a new governance model.

---

## 2. Scope

This standard governs every reusable knowledge asset in the Proposal Factory:

| Asset Type | Code | Current Library | Standard Documents |
|---|---|---|---|
| Capability Asset | CAP | Capability Library | MASTER_CAPABILITY_INDEX.md |
| Assumption Pack | ASP | Assumption Library | ASSUMPTION_LIBRARY_ROADMAP.md |
| Individual Assumption | ASM | Assumption Library (within packs) | (governed by pack) |
| Enterprise Risk | RSK | Risk Library | ENTERPRISE_RISK_REGISTER_V1.md |
| Methodology | MTH | Methodology Library | METHODOLOGY_LIBRARY_STANDARD.md |
| Client Reference | REF | Reference Library | REFERENCE_MASTER.csv |
| Project Plan Template | PPT | (not yet created) | — |
| Proposal Template | PRT | (not yet created) | — |
| Consultant Record | CON | Consultant Index | CONSULTANT_INDEX.csv |
| Compliance Record | COM | Compliance Register | COMPLIANCE_REGISTER.csv |

New asset types may be added by extending this standard. The extension must define: asset type code, ID format, mandatory metadata extensions, library location, and governing index document.

---

## 3. Governing Documents

This standard consists of five documents. Read them in the order shown:

| # | Document | Contents |
|---|---|---|
| **1** | **KNOWLEDGE_ASSET_STANDARD.md** (this document) | Purpose, scope, principles, governance authority |
| 2 | KNOWLEDGE_ASSET_LIFECYCLE.md | 8-state lifecycle with entry/exit criteria, permitted transitions, approval authorities |
| 3 | KNOWLEDGE_METADATA_STANDARD.md | Universal metadata model: mandatory, optional, derived fields; asset-type extensions |
| 4 | KNOWLEDGE_GOVERNANCE_RULES.md | Rules for creation, normalisation, approval, versioning, retirement, audit |
| 5 | KNOWLEDGE_RELATIONSHIP_MODEL.md | Relationship types, dependency hierarchy, traceability expectations |

All five documents are equally authoritative. Where a library-specific standard conflicts with any of these five, the conflict must be resolved in favour of this standard. A library-specific standard that extends this standard for asset-type specifics is acceptable without conflict.

---

## 4. Core Principles

### 4.1 Single Lifecycle

Every governed knowledge asset follows the same lifecycle states. The lifecycle is defined in KNOWLEDGE_ASSET_LIFECYCLE.md. Library-specific standards may not introduce additional or alternative lifecycle states.

### 4.2 Universal Metadata

Every governed knowledge asset carries the mandatory metadata fields defined in KNOWLEDGE_METADATA_STANDARD.md. Asset-type extensions are permitted. Omission of mandatory fields is not permitted.

### 4.3 Deterministic Approval Gate

No knowledge asset may be used in a proposal until `approved_for_reuse: Yes` is set. This is the single universal approval gate. Library-specific approval checks do not override this gate; they precede it.

### 4.4 Traceability

Every knowledge asset must declare its relationships to other governed assets using the relationship types defined in KNOWLEDGE_RELATIONSHIP_MODEL.md. Free-text citations are not acceptable where a governed asset ID exists.

### 4.5 Non-Destructive Versioning

Assets are superseded, not deleted. An asset retired from active use must be retained in ARCHIVED state with its full audit trail. The `supersedes` and `superseded_by` fields maintain the version chain.

### 4.6 BU Lead Authority

The BU Lead is the approving authority for all knowledge assets used in external proposals. The Commercial Director has approving authority only for assets with commercial implications (pricing, contractual commitments, partner credentials). This authority cannot be delegated further.

### 4.7 Exception-Based Governance

Review scope is minimised by classifying assets into auto-approve (Category A), approval-required (Category B), and research-required (Category C). This classification model, established in the Assumption Library and Risk Library governance programmes, is universal.

### 4.8 Retrieval-First Assembly

The assembly pipeline must always retrieve governed assets by ID from approved libraries. Generating content from memory or from unapproved sources is prohibited. This principle governs Stage 4 (Capability Selection), Stage 5 (Reference Selection), Stage 6 (Methodology Selection), Stage 7 (Assumption Assembly), and Stage 8 (Proposal Assembly) of the Proposal Factory pipeline.

---

## 5. Asset Identification

Every governed asset has a unique, persistent identifier. Identifier formats are library-specific and must not change after assignment. The following formats are established:

| Asset Type | Format | Example |
|---|---|---|
| Capability Asset | [WAVE]-[MODULE]-[NNN] | W3S1-001, W4-ERP-001 |
| Assumption Pack | [PLATFORM]_[SCOPE]_ASSUMPTIONS_V[N] | HCM_BASE_ASSUMPTIONS_V1 |
| Individual Assumption | [PACK_CODE]-[SECTION]-[NNN] | HCM-ORG-001, OIC-MAP-001 |
| Enterprise Risk | RC-[CATEGORY]-[NNN] | RC-PROJ-001, RC-TECH-003 |
| Methodology | METH-[CODE]-[NN] | METH-O01, METH-ACU-01 |
| Client Reference | REF-[PLATFORM]-[NNN] | REF-ORA-001, REF-ACU-003 |
| Project Plan Template | PPT-[PLATFORM]-[NN] | PPT-HCM-01 |
| Proposal Template | PRT-[SECTION]-[NN] | PRT-S50-01 |
| Consultant Record | (CONSULTANT_INDEX.csv row — no formal ID) | — |
| Compliance Record | (COMPLIANCE_REGISTER.csv row) | — |

New libraries must define their ID format in the library-specific governing standard before any assets are created. IDs once assigned are permanent — assets are superseded not renumbered.

---

## 6. Governance Authority Matrix

| Decision | Authority | Channel |
|---|---|---|
| Asset creation | Facilitator (AI-assisted) | Work package |
| Asset normalisation | Facilitator (AI-assisted) | Work package |
| Asset approval (standard) | BU Lead | Email or workshop |
| Asset approval (commercial) | Commercial Director | Email or meeting |
| Asset retirement | BU Lead | Written confirmation |
| Standard amendment | BU Lead | Formal WP with version increment |
| New asset type introduction | BU Lead | Formal WP extending this standard |

---

## 7. Integration with Proposal Factory Pipeline

This standard integrates with the Proposal Factory at the following stages:

| Stage | Integration Point |
|---|---|
| Stage 0 — Tender Intelligence | Tender Profile variables match asset selection hooks (mandatory_if / optional_if / excluded_if) |
| Stage 4 — Capability Selection | Only assets with `approved_for_reuse: Yes` and `lifecycle_status: APPROVED` are eligible |
| Stage 5 — Reference Selection | Only references with `approved_for_reuse: Yes` and no blocking restrictions are eligible |
| Stage 6 — Methodology Selection | Only methodologies with `approved_for_reuse: Yes` are eligible |
| Stage 7 — Assumption Assembly | Only assumptions from approved packs (`approved_for_reuse: Yes`) are eligible |
| Stage 8 — Proposal Assembly | Risks from S-50, sections from the Section Library — all governed by approved_for_reuse gate |
| Stage 9 — QA Engine (WP18D) | Cross-library relationship validation: all cited assets exist and are approved |

---

## 8. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-26 | WP18B-EXT.3 | Initial standard — establishes universal governance framework for all Proposal Factory knowledge assets |
