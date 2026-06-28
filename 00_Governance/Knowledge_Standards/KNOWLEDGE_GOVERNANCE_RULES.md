---
document_id: KNOWLEDGE-GOVERNANCE-RULES-V1
title: "Universal Knowledge Asset Governance Rules — V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-26"
created_by: "WP18B-EXT.3 — Universal Knowledge Asset Governance Standard"
approved_by: "Architecture — WP18B-EXT.3"
approved_date: "2026-06-26"
approved_for_reuse: true
category: "Governance / Knowledge Standards"
scope: "Defines the universal governance rules for all knowledge assets in the APPSolve Proposal Factory. Covers creation, normalisation, review, approval, versioning, retirement, supersession, archival, restoration, and audit trail."
related_documents:
  - KNOWLEDGE_ASSET_STANDARD.md
  - KNOWLEDGE_ASSET_LIFECYCLE.md
  - KNOWLEDGE_METADATA_STANDARD.md
---

# Universal Knowledge Asset Governance Rules — V1.0

**Authority:** KNOWLEDGE_ASSET_STANDARD.md Section 3  
**Applies to:** All asset types. Rules marked [UNIVERSAL] apply without exception. Rules marked [ASSET-SPECIFIC] apply only to the specified asset types.

---

## Section 1 — Creation Rules

### GR-C01 [UNIVERSAL] — No Asset Without a Source

Every knowledge asset must declare at least one source. Acceptable sources:
- A governed KB source document (HIST-registered in DOCUMENT_REGISTER.csv)
- An approved capability asset (Cap ID in MASTER_CAPABILITY_INDEX.md)
- A directly observed business event or delivery outcome (documented in governance_notes)
- An approved project document (referenced by document path)

Free-text attribution ("based on project experience") without a traceable source is not acceptable.

**Exception:** Assumptions and risks that arise from recognised industry standards (e.g., POPIA, BCEA, Oracle SaaS licensing model) may cite the standard name as source with the publication date.

### GR-C02 [UNIVERSAL] — ID Assigned at Creation

Every asset must receive its `asset_id` at the moment of creation, before any content is written. IDs are permanent. Once assigned, an ID is never reused, renumbered, or modified.

If an asset is found to have a duplicate ID after creation, the newer asset is assigned a new ID and the duplicate is documented in governance_notes.

### GR-C03 [UNIVERSAL] — No Generated Content

Knowledge asset content must not be generated from general knowledge or inference alone. All factual claims (client names, engagement outcomes, statistics, product capabilities) must be traceable to a governed source document.

**In practice:** The AI facilitator may draft the structure and non-factual framing; factual content requires a source citation.

### GR-C04 [UNIVERSAL] — Library Registration at Creation

Every new asset must be registered in its library's governing index document at creation (not after approval). An unregistered asset is not governed and may not be used. Registration records: asset_id, title, lifecycle_status: DRAFT.

### GR-C05 [ASSET-SPECIFIC: CAP] — Pre-Tender Controls Declared at Creation

Every capability asset must declare any pre-tender controls (PT- codes) at creation. A PT- code blocks external use of the asset until the control is satisfied. PT- codes are documented in the `governance_restrictions` extension field and in MASTER_CAPABILITY_INDEX.md.

---

## Section 2 — Normalisation Rules

### GR-N01 [UNIVERSAL] — Mandatory Fields Before Advancement

An asset may not advance from DRAFT to NORMALISED until all mandatory metadata fields are complete (per KNOWLEDGE_METADATA_STANDARD.md Section 2) and all applicable optional fields are populated.

### GR-N02 [UNIVERSAL] — Governed IDs for All Cross-References

All related_assets, source_assets, related_assumptions, and similar relationship fields must use governed asset IDs. Free-text asset descriptions in relationship fields are not permitted at NORMALISED state or later.

**Verification method:** Grep the ID against the library's governing index document. An ID that does not exist in the index is not a governed ID.

### GR-N03 [UNIVERSAL] — Content Validation Before Normalisation

The facilitator must confirm that content has been validated against source material before advancing to NORMALISED. Validation means:
- All factual claims traceable to a governed source
- No fabricated client names, statistics, or outcomes
- No prohibitive governance restrictions violated

### GR-N04 [ASSET-SPECIFIC: RSK] — Rating Matrix Verification

Every enterprise risk must have its `net_rating` verified against the approved 3×3 matrix before advancing to NORMALISED:

| Likelihood \ Impact | Low | Medium | High |
|---|---|---|---|
| **Low** | LOW | LOW | MEDIUM |
| **Medium** | LOW | MEDIUM | HIGH |
| **High** | MEDIUM | HIGH | CRITICAL |

A rating that contradicts the matrix is a mandatory correction item. The corrected rating must be documented in governance_notes and escalated to the BU Lead as a Category B decision.

### GR-N05 [ASSET-SPECIFIC: RSK] — Selection Hook Completeness

Every enterprise risk must have `mandatory_if` populated (even if the value is `FALSE` — meaning the risk is never auto-included and requires explicit selection). Blank is not permitted. The absence of a selection hook means the Risk Selection Engine cannot include or exclude the risk deterministically.

### GR-N06 [ASSET-SPECIFIC: CAP] — Evidence Tier Confirmed

Every capability asset must have its evidence tier confirmed before advancing to NORMALISED:
- Tier 1: Direct client engagement with a traceable outcome
- Tier 1 Contractual: HIST-registered contract document
- Tier 2: Platform capability with internal project evidence (not externalised)
- N/A — Positioning: No client evidence; positioning statement only

Evidence tier cannot be self-assigned without a traceable source. If no evidence exists, evidence_tier must be "Tier 2" or "N/A — Positioning" with governance_notes documenting the evidence gap.

---

## Section 3 — Review Rules

### GR-R01 [UNIVERSAL] — Scheduled Review Obligation

Every APPROVED asset must be reviewed by its `next_review` date. The owner_role is responsible for initiating the review. If the review date passes without action, the asset is flagged as overdue in the library index. An overdue asset is still APPROVED and still assembly-eligible — the overdue flag is informational only. However:

- An asset that is 180 days overdue for review must be suspended from assembly until reviewed (approved_for_reuse set to No pending review).
- An asset that is 365 days overdue for review must be advanced to SUPERSEDED and a new version created.

### GR-R02 [UNIVERSAL] — Review Must Be Substantive

A review that confirms no change must still update `last_reviewed` and `next_review`. A review is not complete unless these two fields are updated. A review that does not update these fields has not occurred.

### GR-R03 [UNIVERSAL] — Review Authority

Asset reviews are conducted by the `owner_role` for the asset. The BU Lead must be notified of any review that results in a content change. Content changes that affect proposal commercial positioning, evidence claims, or client naming must be approved by the BU Lead before the revised asset advances to APPROVED.

### GR-R04 [ASSET-SPECIFIC: REF] — Reference Currency Verification

Client reference assets must be reviewed annually to confirm:
- The client relationship is still active (or the reference is historical and so noted)
- The reference letter is still signed and authorised
- Account manager approval status is current
- The engagement scope claim has not been contradicted by subsequent project events

### GR-R05 [ASSET-SPECIFIC: CAP] — OPN Partner Credential Annual Revalidation

The Oracle Partnership capability asset (W1S1-003) requires annual OPN revalidation. This is an external constraint — the BU Lead must confirm current OPN tier before each annual review cycle closes. If OPN tier has changed, the asset must be revised to reflect the current tier before the next external submission.

---

## Section 4 — Approval Rules

### GR-A01 [UNIVERSAL] — BU Lead Is the Approving Authority

The BU Lead (currently Hein Blignaut) is the approving authority for all knowledge assets intended for use in external proposals. This authority is not delegated except as explicitly noted in the Governance Authority Matrix (KNOWLEDGE_ASSET_STANDARD.md Section 6).

### GR-A02 [UNIVERSAL] — approved_for_reuse Gate Is Absolute

An asset with `approved_for_reuse: No` may not be cited in any externally submitted proposal. No exceptions. This applies regardless of:
- How complete the asset content is
- Whether the BU Lead informally approved it verbally
- Whether the asset is in APPROVED lifecycle state but the field has not been updated

The field value is the gate, not the lifecycle state alone.

### GR-A03 [UNIVERSAL] — Commercial Director for Commercial Assets

Assets with direct commercial implications require Commercial Director approval in addition to BU Lead approval. Commercial assets include:
- Partner credential claims (Oracle partnership tier, Acumatica Gold Partner)
- Pricing models or costing assumptions
- Contractual commitment assumptions (fixed-price implications, SLA obligations)
- Regulatory compliance claims with commercial exposure

Commercial Director approval is recorded in `approved_by` alongside the BU Lead name: "BU Lead + Commercial Director".

### GR-A04 [UNIVERSAL] — Exception-Based Review Minimises BU Effort

Governance review must use the Category A / B / C classification before any BU Lead review session. The BU Lead reviews decisions only, not every asset. Auto-approval registers must be prepared for Category A assets before any workshop or email review is initiated.

### GR-A05 [UNIVERSAL] — No Retrospective Approvals

An approval applied to an asset after a proposal has already been submitted using that asset does not retroactively validate the proposal submission. Assets must be approved before submission. If an asset was used before approval, the governance gap must be documented in the library's audit trail.

### GR-A06 [ASSET-SPECIFIC: CAP] — Pre-Tender Controls Satisfied Before Submission

Every PT- code on a capability asset must be satisfied before the asset is used in an external submission. PT- codes are not optional checklist items — they are hard submission gates. A proposal submitted with an unsatisfied PT- code is a governance violation.

---

## Section 5 — Versioning Rules

### GR-V01 [UNIVERSAL] — Version Increment on Content Change

Any change to asset content that affects meaning, scope, or restrictions requires a version increment:
- Minor content corrections (typos, formatting) → minor increment (1.0 → 1.1)
- Content changes affecting meaning, restrictions, or ratings → minor increment (1.0 → 1.1)
- Schema changes (new fields, changed field types) → major increment (1.0 → 2.0)

### GR-V02 [UNIVERSAL] — New Version Is a New Asset

A new version is a new asset with a new document. The previous version transitions to SUPERSEDED. The `supersedes` field in the new version points to the previous version's asset_id; the `superseded_by` field in the previous version points to the new asset_id.

### GR-V03 [UNIVERSAL] — Superseded Version Retained

A SUPERSEDED asset must be retained in the repository for 24 months from the date of supersession. It must be clearly labelled "SUPERSEDED" in its frontmatter and in the library index. After 24 months, it transitions to ARCHIVED.

### GR-V04 [UNIVERSAL] — Version Chain Completeness

The version chain from the first version to the current version must be complete and traceable. No version may be deleted from the chain, even if later superseded. An incomplete version chain is a governance defect.

### GR-V05 [ASSET-SPECIFIC: ASP] — Pack Version Governs Assumption Versions

When an assumption pack is updated (e.g., HCM_BASE_ASSUMPTIONS_V1 → V2), all assumptions within the pack inherit the new pack version. Individual assumptions within a pack do not have independent versions — they are versioned with the pack.

---

## Section 6 — Retirement Rules

### GR-RT01 [UNIVERSAL] — Retirement Requires BU Lead Confirmation

An asset may only be retired (transitioned to ARCHIVED without a successor) with explicit BU Lead written confirmation. Retirement differs from supersession (where a successor exists). Retirement is appropriate when:
- The asset's subject matter is no longer relevant (e.g., a retired product capability)
- The asset is determined to be inaccurate with no correctable path
- The asset type is being eliminated

### GR-RT02 [UNIVERSAL] — Retirement Audit Trail

The retirement decision must be documented: reason for retirement, BU Lead confirmer, date. This is recorded in the asset's governance_notes field and in the library index.

### GR-RT03 [UNIVERSAL] — Proposals Using Retired Assets Are Not Invalidated

Retiring an asset does not invalidate proposals that used it while it was approved. Proposals lock their assembly manifest at submission. The retired status affects future proposals only.

---

## Section 7 — Supersession Rules

### GR-S01 [UNIVERSAL] — Supersession Requires APPROVED Successor

An asset may only be superseded when its successor has reached APPROVED state. An asset may not be placed in SUPERSEDED state while its successor is still in DRAFT or NORMALISED — this would create a gap where neither version is approved.

### GR-S02 [UNIVERSAL] — Bidirectional Linking

Supersession links are bidirectional and mandatory:
- New version: `supersedes: [old asset_id]`
- Old version: `superseded_by: [new asset_id]`

A supersession without both links populated is incomplete.

### GR-S03 [ASSET-SPECIFIC: CAP] — Superseded Capabilities Not Used in Active Tenders

Active tenders in progress must be reviewed when a capability asset they rely on is superseded. The proposal team must decide whether to update to the new version or proceed with the superseded version under explicit BU Lead approval.

---

## Section 8 — Archival Rules

### GR-AR01 [UNIVERSAL] — 24-Month Retention Minimum

Superseded assets are retained in ARCHIVED state for a minimum of 24 months from the date of supersession. This allows retrospective verification of proposals submitted during the superseded version's active period.

### GR-AR02 [UNIVERSAL] — Archived Assets Are Read-Only

An ARCHIVED asset may not be modified. If an archived asset's content needs to be used as the basis for a new asset, a new asset in DRAFT state must be created from the archived content. The archived asset itself is not modified.

### GR-AR03 [UNIVERSAL] — Archive Location

Archived assets are moved to the `Archive` subfolder of their library's directory. They retain their original filename but carry `lifecycle_status: ARCHIVED` in frontmatter. The library index entry is updated to reflect ARCHIVED status.

---

## Section 9 — Restoration Rules

### GR-RS01 [UNIVERSAL] — Restoration Requires BU Lead Approval

An ARCHIVED asset may only be restored to APPROVED state with explicit BU Lead approval. Restoration is appropriate when a superseding version is withdrawn and no other replacement exists.

### GR-RS02 [UNIVERSAL] — Restoration Validates Current Accuracy

Before restoring an archived asset, the facilitator must review its content for current accuracy. Any content that has become inaccurate during the archive period must be corrected before restoration. Restoration without content review is not permitted.

### GR-RS03 [UNIVERSAL] — Restored Version Is a New Version

A restored asset is treated as a new version (e.g., 1.0 archived → restored as 1.2). The archived version remains ARCHIVED. The restored content is a new APPROVED asset with an incremented version number.

---

## Section 10 — Audit Trail Rules

### GR-AU01 [UNIVERSAL] — Every Transition Documented

Every lifecycle state transition must be documented with: old state, new state, date, authority (who approved), and reason. This documentation is maintained in the asset's `governance_notes` field and/or the library's governance log.

### GR-AU02 [UNIVERSAL] — Decision Register for Category B/C Transitions

Every REVIEW_REQUIRED transition must produce a decision register entry (per the governance decision register pattern established in WP15A/WP18B-EXT.1B). The entry records: decision ID, asset ID, current state, proposed state, reason, evidence, options, recommendation, outcome.

### GR-AU03 [UNIVERSAL] — Library Index Is the Audit Backbone

The library governing index (MASTER_CAPABILITY_INDEX.md, ENTERPRISE_RISK_REGISTER_V1.md, etc.) must reflect the current lifecycle state of every asset. An out-of-date index is a governance defect. The index is updated synchronously with every lifecycle transition — not retrospectively.

### GR-AU04 [UNIVERSAL] — No Unapproved Assets in Submitted Proposals

The assembly manifest of every submitted proposal must be retained and verifiable. The manifest records every knowledge asset used, its asset_id, its version, and its lifecycle_status at the time of use. This audit trail enables retrospective governance review of any submitted proposal.

### GR-AU05 [UNIVERSAL] — Governance Violations Are Logged

Any governance violation (e.g., an asset used before approval, a PT- code not satisfied, a mandatory field left blank) must be logged in OUTSTANDING_ACTION_REGISTER.md with: violation type, asset ID, date discovered, resolution action, resolution date.

---

## Section 11 — Universal vs Asset-Specific Rule Precedence

| Rule Area | Universal Rules | Asset-Specific Rules |
|---|---|---|
| ID assignment | GR-C02 — universal | ID format per KNOWLEDGE_ASSET_STANDARD Section 5 |
| Content sourcing | GR-C01, GR-C03 — universal | Evidence tier per CAP extension; rating matrix per RSK extension |
| Approval gate | GR-A01, GR-A02 — universal | GR-A03 (CD approval) for commercial; GR-A06 (PT-) for CAP |
| Versioning | GR-V01 through GR-V04 — universal | GR-V05 (pack versioning) for ASP |
| Retention | GR-AR01 — universal | — |
| Audit | GR-AU01 through GR-AU05 — universal | GR-R04 (reference currency) for REF; GR-R05 (OPN) for CAP |

**Where asset-specific rules are more restrictive than universal rules, the more restrictive rule applies.**  
**Where asset-specific rules attempt to relax a universal rule, the universal rule prevails.**

---

## Section 12 — Rule Index

| Rule ID | Title | Type | Section |
|---|---|---|---|
| GR-C01 | No Asset Without a Source | Universal | 1 |
| GR-C02 | ID Assigned at Creation | Universal | 1 |
| GR-C03 | No Generated Content | Universal | 1 |
| GR-C04 | Library Registration at Creation | Universal | 1 |
| GR-C05 | Pre-Tender Controls Declared at Creation | CAP | 1 |
| GR-N01 | Mandatory Fields Before Advancement | Universal | 2 |
| GR-N02 | Governed IDs for All Cross-References | Universal | 2 |
| GR-N03 | Content Validation Before Normalisation | Universal | 2 |
| GR-N04 | Rating Matrix Verification | RSK | 2 |
| GR-N05 | Selection Hook Completeness | RSK | 2 |
| GR-N06 | Evidence Tier Confirmed | CAP | 2 |
| GR-R01 | Scheduled Review Obligation | Universal | 3 |
| GR-R02 | Review Must Be Substantive | Universal | 3 |
| GR-R03 | Review Authority | Universal | 3 |
| GR-R04 | Reference Currency Verification | REF | 3 |
| GR-R05 | OPN Partner Credential Annual Revalidation | CAP | 3 |
| GR-A01 | BU Lead Is the Approving Authority | Universal | 4 |
| GR-A02 | approved_for_reuse Gate Is Absolute | Universal | 4 |
| GR-A03 | Commercial Director for Commercial Assets | Universal | 4 |
| GR-A04 | Exception-Based Review | Universal | 4 |
| GR-A05 | No Retrospective Approvals | Universal | 4 |
| GR-A06 | Pre-Tender Controls Satisfied Before Submission | CAP | 4 |
| GR-V01 | Version Increment on Content Change | Universal | 5 |
| GR-V02 | New Version Is a New Asset | Universal | 5 |
| GR-V03 | Superseded Version Retained | Universal | 5 |
| GR-V04 | Version Chain Completeness | Universal | 5 |
| GR-V05 | Pack Version Governs Assumption Versions | ASP | 5 |
| GR-RT01 | Retirement Requires BU Lead Confirmation | Universal | 6 |
| GR-RT02 | Retirement Audit Trail | Universal | 6 |
| GR-RT03 | Retired Assets Do Not Invalidate Proposals | Universal | 6 |
| GR-S01 | Supersession Requires APPROVED Successor | Universal | 7 |
| GR-S02 | Bidirectional Linking | Universal | 7 |
| GR-S03 | Superseded Capabilities in Active Tenders | CAP | 7 |
| GR-AR01 | 24-Month Retention Minimum | Universal | 8 |
| GR-AR02 | Archived Assets Are Read-Only | Universal | 8 |
| GR-AR03 | Archive Location | Universal | 8 |
| GR-RS01 | Restoration Requires BU Lead Approval | Universal | 9 |
| GR-RS02 | Restoration Validates Current Accuracy | Universal | 9 |
| GR-RS03 | Restored Version Is a New Version | Universal | 9 |
| GR-AU01 | Every Transition Documented | Universal | 10 |
| GR-AU02 | Decision Register for Category B/C | Universal | 10 |
| GR-AU03 | Library Index Is the Audit Backbone | Universal | 10 |
| GR-AU04 | No Unapproved Assets in Submitted Proposals | Universal | 10 |
| GR-AU05 | Governance Violations Are Logged | Universal | 10 |
