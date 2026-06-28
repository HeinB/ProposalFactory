---
document_id: KNOWLEDGE-ASSET-LIFECYCLE-V1
title: "Universal Knowledge Asset Lifecycle — V1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-26"
created_by: "WP18B-EXT.3 — Universal Knowledge Asset Governance Standard"
approved_by: "Architecture — WP18B-EXT.3"
approved_date: "2026-06-26"
approved_for_reuse: true
category: "Governance / Knowledge Standards"
scope: "Defines the universal lifecycle for all knowledge assets in the APPSolve Proposal Factory. Applies to all asset types listed in KNOWLEDGE_ASSET_STANDARD.md."
related_documents:
  - KNOWLEDGE_ASSET_STANDARD.md
  - KNOWLEDGE_METADATA_STANDARD.md
  - KNOWLEDGE_GOVERNANCE_RULES.md
---

# Universal Knowledge Asset Lifecycle — V1.0

**Authority:** KNOWLEDGE_ASSET_STANDARD.md Section 4.1  
**Applies to:** All asset types: CAP, ASP, ASM, RSK, MTH, REF, PPT, PRT, CON, COM

---

## 1. Lifecycle State Diagram

```
                    ┌─────────────────────┐
                    │        DRAFT        │  ← Entry point for all new assets
                    └──────────┬──────────┘
                               │ Normalisation complete
                               ▼
                    ┌─────────────────────┐
                    │     NORMALISED      │  ← Schema complete; cross-refs verified
                    └──────────┬──────────┘
                               │ Classification performed
                               ▼
                    ┌─────────────────────┐
                    │  READY_FOR_REVIEW   │  ← Governance pack prepared
                    └──────────┬──────────┘
                               │
               ┌───────────────┴───────────────┐
               ▼                               ▼
   ┌───────────────────────┐    ┌───────────────────────────┐
   │    AUTO_APPROVED      │    │     REVIEW_REQUIRED       │
   │  (Category A assets)  │    │  (Category B/C assets)    │
   └───────────┬───────────┘    └─────────────┬─────────────┘
               │                              │
               └──────────────┬───────────────┘
                              │ BU Lead sign-off
                              ▼
                   ┌─────────────────────┐
                   │      APPROVED       │  ← approved_for_reuse: Yes
                   └──────────┬──────────┘
                              │
              ┌───────────────┴──────────────────┐
              │ New version created               │ Withdrawn
              ▼                                  ▼
   ┌─────────────────────┐            ┌─────────────────────┐
   │     SUPERSEDED      │            │      ARCHIVED       │
   └─────────────────────┘            └─────────────────────┘
              │
              │ (automatically)
              ▼
   ┌─────────────────────┐
   │      ARCHIVED       │
   └─────────────────────┘
```

---

## 2. State Definitions

### DRAFT

The initial state of every new or extracted knowledge asset. Content is present but incomplete or unvalidated.

| Attribute | Value |
|---|---|
| `lifecycle_status` | `DRAFT` |
| `approved_for_reuse` | `No` |
| Assembly eligible | No |
| BU review ready | No |

**Entry criteria:**
- Asset has been created (extraction, authoring, or system-generated)
- Asset ID assigned
- Minimum content present (title, description, source)
- Mandatory metadata fields may be incomplete at this stage

**Exit criteria:**
- All mandatory metadata fields populated (see KNOWLEDGE_METADATA_STANDARD.md Section 2)
- Source assets identified and verified as governed IDs (not free text)
- Related assets cross-referenced using governed IDs
- Content validated against source material (no fabricated claims)
- Review frequency set; next_review date calculated
- Transition trigger: facilitator confirms normalisation complete → advance to NORMALISED

**Permitted next states:** NORMALISED  
**Prohibited transitions:** DRAFT → APPROVED (skip not permitted — normalisation is mandatory)

---

### NORMALISED

Schema-complete state. All metadata fields are populated and validated. Content is verified against source material. The asset is ready for governance classification.

| Attribute | Value |
|---|---|
| `lifecycle_status` | `NORMALISED` |
| `approved_for_reuse` | `No` |
| Assembly eligible | No |
| BU review ready | Not yet — classification required first |

**Entry criteria (must all be true):**
- All mandatory metadata fields complete
- All optional fields populated where applicable
- All cross-references use governed IDs (no free text)
- Source assets verified
- Rating/confidence calculations validated (for risks: 3×3 matrix; for capabilities: evidence tier confirmed)
- Lifecycle metadata complete (review_frequency, last_reviewed, next_review)

**Exit criteria:**
- Governance classification performed: Category A (auto-approve), B (approval required), or C (research required)
- For Category A: auto-approval register entry prepared
- For Category B: decision register entry prepared
- For Category C: research gap documented with resolution path
- Transition trigger: classification complete → advance to READY_FOR_REVIEW

**Permitted next states:** READY_FOR_REVIEW  
**Prohibited transitions:** NORMALISED → APPROVED (BU review cannot be skipped)

---

### READY_FOR_REVIEW

Governance pack prepared. The asset is classified and packaged for BU Lead review. The appropriate governance channel (email or workshop) has been determined.

| Attribute | Value |
|---|---|
| `lifecycle_status` | `READY_FOR_REVIEW` |
| `approved_for_reuse` | `No` |
| Assembly eligible | No |
| BU review ready | Yes |

**Entry criteria:**
- NORMALISED state complete
- Governance classification confirmed
- Appropriate governance pack prepared (auto-approval register or decision register)
- BU Lead notified

**Exit criteria:**
- BU Lead has reviewed and responded
- Category A: batch sign-off confirmed → advance to AUTO_APPROVED
- Category B: decision recorded → advance to REVIEW_REQUIRED (then to APPROVED on sign-off)
- Category C: research complete → return to NORMALISED (if resolved) or remain READY_FOR_REVIEW pending resolution

**Permitted next states:** AUTO_APPROVED, REVIEW_REQUIRED  
**Prohibited transitions:** READY_FOR_REVIEW → APPROVED (must pass through AUTO_APPROVED or REVIEW_REQUIRED)

---

### AUTO_APPROVED

Category A: The BU Lead has confirmed batch approval for this asset. No individual decision was required.

| Attribute | Value |
|---|---|
| `lifecycle_status` | `AUTO_APPROVED` |
| `approved_for_reuse` | `No` → set to `Yes` on transition to APPROVED |
| Assembly eligible | No (approved_for_reuse not yet set) |
| BU review ready | Complete |

**Entry criteria:**
- READY_FOR_REVIEW complete
- Asset classified as Category A (all auto-approval criteria met)
- BU Lead batch sign-off received

**Exit criteria:**
- `approved_for_reuse: Yes` set in asset record
- `approved_by` and `approval_date` populated
- Transition trigger: facilitator applies approval → advance to APPROVED

**Permitted next states:** APPROVED  
**Prohibited transitions:** AUTO_APPROVED → any state other than APPROVED

**Note:** AUTO_APPROVED is a transient state. The facilitator advances the asset to APPROVED immediately after batch sign-off is received. It exists to record that the approval path was automatic (no deliberation), for audit purposes.

---

### REVIEW_REQUIRED

Category B or C: The asset requires a BU Lead decision before it can be approved. The decision register entry defines the options and recommendation.

| Attribute | Value |
|---|---|
| `lifecycle_status` | `REVIEW_REQUIRED` |
| `approved_for_reuse` | `No` |
| Assembly eligible | No |
| BU review required | Yes — decision pending |

**Entry criteria:**
- READY_FOR_REVIEW complete
- Asset classified as Category B (approval required) or Category C (research required, resolved)
- Decision register entry prepared with current state, proposed state, options, recommendation

**Exit criteria:**
- BU Lead decision recorded in Decision Status Tracker
- Decision applied (rating updated, merger confirmed, governance rule confirmed, etc.)
- `approved_for_reuse: Yes` set
- `approved_by` and `approval_date` populated
- Transition trigger: facilitator applies decision → advance to APPROVED

**Exception path:** If BU Lead rejects the asset (e.g., rating reverted to a fundamentally different posture), the asset may return to NORMALISED for revision before re-entering the review cycle.

**Permitted next states:** APPROVED, NORMALISED (on rejection requiring rework)

---

### APPROVED

The asset is governance-complete. It has been reviewed and approved by the BU Lead (and Commercial Director where applicable). It is eligible for use in proposals.

| Attribute | Value |
|---|---|
| `lifecycle_status` | `APPROVED` |
| `approved_for_reuse` | `Yes` |
| Assembly eligible | **Yes** |
| Review clock | Active — next_review date governs scheduled review |

**Entry criteria (both must be true):**
- Asset has passed through AUTO_APPROVED or REVIEW_REQUIRED
- `approved_for_reuse: Yes`, `approved_by`, `approval_date` all populated

**Exit criteria (any of the following):**
- A new version is created → this version transitions to SUPERSEDED
- BU Lead withdraws approval → transitions to ARCHIVED
- Review date passed with no review action → remains APPROVED but flagged for overdue review (does not automatically change state)

**Permitted next states:** SUPERSEDED, ARCHIVED  
**Prohibited transitions:** APPROVED → DRAFT or APPROVED → NORMALISED (a version in APPROVED state is immutable; any change creates a new version)

**Review obligation:** APPROVED assets must be reviewed on the schedule defined by `review_frequency`. The review may confirm the asset unchanged (no state transition, update `last_reviewed` and `next_review`), or trigger a revision (new version created, old version → SUPERSEDED).

---

### SUPERSEDED

The asset has been replaced by a newer version. It is no longer eligible for use in new proposals but must be retained for audit trail of proposals that used this version.

| Attribute | Value |
|---|---|
| `lifecycle_status` | `SUPERSEDED` |
| `approved_for_reuse` | `No` (set to No on supersession) |
| Assembly eligible | No (for new proposals) |
| Retained | Yes — for audit trail |

**Entry criteria:**
- A new version of this asset has been created and approved
- `superseded_by` field set to the new version's asset_id

**Exit criteria:**
- Transition trigger: after audit retention period (default: 24 months), advance to ARCHIVED

**Permitted next states:** ARCHIVED  
**Restoration:** A SUPERSEDED asset may be restored to APPROVED if the superseding version is withdrawn, provided the BU Lead explicitly approves restoration.

---

### ARCHIVED

The asset is no longer active and no longer referenced by any active proposal. It is retained in read-only storage for historical audit only.

| Attribute | Value |
|---|---|
| `lifecycle_status` | `ARCHIVED` |
| `approved_for_reuse` | `No` |
| Assembly eligible | No |
| Modifiable | No — read-only |

**Entry criteria (any of the following):**
- Asset transitioned from SUPERSEDED after 24-month retention
- BU Lead withdraws asset from APPROVED state
- Asset has never been used in a proposal and is determined irrelevant

**Exit criteria:**
- No automatic exit. Restoration requires BU Lead explicit approval and a new version creation (ARCHIVED → new DRAFT, then full lifecycle).

**Permitted next states:** None (terminal state for read-only retention). New version may be created from an archived asset's content, but the archived asset itself does not change state.

---

## 3. Transition Permission Matrix

| From | To | Permitted | Authority | Notes |
|---|---|---|---|---|
| DRAFT | NORMALISED | Yes | Facilitator | Normalisation complete |
| DRAFT | APPROVED | **No** | — | Normalisation cannot be skipped |
| NORMALISED | READY_FOR_REVIEW | Yes | Facilitator | Classification complete |
| NORMALISED | APPROVED | **No** | — | BU review cannot be skipped |
| READY_FOR_REVIEW | AUTO_APPROVED | Yes | Facilitator | Category A batch sign-off received |
| READY_FOR_REVIEW | REVIEW_REQUIRED | Yes | Facilitator | Category B/C session conducted |
| READY_FOR_REVIEW | NORMALISED | Yes | Facilitator | Category C — research gap; return for rework |
| AUTO_APPROVED | APPROVED | Yes | Facilitator | Apply approved_for_reuse = Yes |
| REVIEW_REQUIRED | APPROVED | Yes | Facilitator | Apply decision + approved_for_reuse = Yes |
| REVIEW_REQUIRED | NORMALISED | Yes | BU Lead | Rejection requiring rework |
| APPROVED | SUPERSEDED | Yes | Facilitator | New version created and approved |
| APPROVED | ARCHIVED | Yes | BU Lead | Withdrawal |
| SUPERSEDED | ARCHIVED | Yes | Facilitator | After 24-month retention |
| ARCHIVED | any | **No** | — | Terminal state; new version via separate WP |

---

## 4. Lifecycle-to-Existing-Library Mapping

| Asset Type | Previous Lifecycle Labels | Universal Equivalent |
|---|---|---|
| Capability Asset (draft wave) | Candidate / Draft | DRAFT |
| Capability Asset (review required) | Review Required | READY_FOR_REVIEW → REVIEW_REQUIRED |
| Capability Asset (approved wave) | Approved v1.0 | APPROVED |
| Assumption Pack (draft) | Draft | DRAFT → NORMALISED |
| Assumption Pack (decisions outstanding) | Draft (BU decisions pending) | READY_FOR_REVIEW → REVIEW_REQUIRED |
| Assumption Pack (approved) | Approved v1.0 | APPROVED |
| Enterprise Risk (draft-0.1) | draft-0.1 | DRAFT |
| Enterprise Risk (V1.0 normalised) | Draft (pending BU review) | NORMALISED |
| Enterprise Risk (Cat A) | Category A | AUTO_APPROVED → APPROVED |
| Enterprise Risk (Cat B) | Category B | REVIEW_REQUIRED → APPROVED |
| Enterprise Risk (superseded) | Superseded | SUPERSEDED |
| Methodology (approved) | Approved | APPROVED |
| Reference (registered) | Active | APPROVED |
| Reference (restricted) | Restricted — requires AM approval | APPROVED (with governance_notes restrictions) |

**Note:** Assets currently labelled "Approved" in library-specific terms are treated as APPROVED for assembly purposes. Formal lifecycle_status field population is recommended remediation (low effort) — see WP18B_EXT3_UNIVERSAL_GOVERNANCE_REPORT.md Section 6.

---

## 5. Review Cycle Obligations

Every APPROVED asset has a scheduled review date (`next_review`). Review frequency is set at normalisation based on asset type and risk level:

| Asset Type | Default Review Frequency | Override Conditions |
|---|---|---|
| Enterprise Risk (CRITICAL/HIGH) | Quarterly | — |
| Enterprise Risk (MEDIUM) | Bi-annually | — |
| Enterprise Risk (LOW) | Annually | — |
| Capability Asset | Annually | Shorten to Bi-annually if reference restrictions change |
| Assumption Pack | Bi-annually | Shorten to Quarterly if legislative changes affect the pack |
| Individual Assumption | (follows pack) | — |
| Methodology | Annually | — |
| Client Reference | Annually | Review on contract renewal or client go-live completion |
| Project Plan Template | Bi-annually | — |
| Proposal Template | Bi-annually | — |

**Review outcomes:**
- **No change** — update `last_reviewed`, `next_review`; confirm APPROVED state unchanged
- **Minor update** — increment version (e.g., 1.0 → 1.1); create new version in NORMALISED state; old version → SUPERSEDED
- **Major revision** — new version in DRAFT state; full lifecycle; old version → SUPERSEDED
- **Retirement** — old version → ARCHIVED; no successor

---

## 6. Category Classification Reference

| Category | Criteria | Governance channel |
|---|---|---|
| **A — Auto Approve** | Single source; no content change from source; schema complete; business meaning confirmed | Batch sign-off (email or workshop pre-read) |
| **B — Approval Required** | Merger of sources; rating/content change; governance rule confirmation needed | Email (clear rationale) or Workshop (judgment required) |
| **C — Research Required** | Missing source; contradictions; evidence gap with no resolution path | Facilitator research first; reclassify on resolution |

This classification model applies universally. Library-specific sub-criteria may be defined but must map to A/B/C.
