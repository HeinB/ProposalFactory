---
document_id: ASSUMPTION_GOVERNANCE
title: "Commercial Assumptions Library — Governance Framework"
version: "1.0"
created: "2026-06-15"
created_by: "WP11 — Commercial Assumptions Library"
status: "Active"
applies_to: "All documents in 08_Commercial/Assumptions/"
owner: "BU Lead — Oracle Practice (HCM, ERP, OIC, OCI); BU Lead — Acumatica; BU Lead — BeBanking; Cross-BU Director for Cross_BU pack"
---

# Commercial Assumptions Library — Governance Framework

## 1. Purpose

This document defines the governance rules, ownership model, version control, change management, and tender usage rules for the Commercial Assumptions Library. The library is governed as a first-class component of the APPSolve Tender Factory, with the same rigour applied to approved capability statements under `07_Approved_Content/`.

An assumption that enters a proposal unapproved, unvalidated, or commercially indefensible is a liability. An assumption that is missing from a proposal is a scope risk. This governance framework ensures every assumption in the library is deliberate, defensible, and current.

---

## 2. Ownership Model

| Pack | Primary Owner | Secondary Owner | Approver |
|---|---|---|---|
| HCM Base Assumptions | Oracle Practice BU Lead | Principal HCM Consultant | BU Lead |
| HCM Recruiting Assumptions | Oracle Practice BU Lead | Principal HCM Consultant | BU Lead |
| HCM Learning Assumptions | Oracle Practice BU Lead | Learning Specialist | BU Lead |
| HCM Talent Assumptions | Oracle Practice BU Lead | Principal HCM Consultant | BU Lead |
| HCM Compensation Assumptions | Oracle Practice BU Lead | Principal HCM Consultant | BU Lead |
| Oracle ERP Assumptions | Oracle Practice BU Lead | Principal ERP Consultant | BU Lead |
| OIC Assumptions | Oracle Practice BU Lead | OIC Principal Developer | BU Lead |
| OCI Assumptions | Oracle Practice BU Lead | OCI Architect | BU Lead |
| Acumatica Assumptions | Acumatica BU Lead | Senior Acumatica Consultant | BU Lead |
| BeBanking Assumptions | BeBanking BU Lead | Senior BeBanking Consultant | BU Lead |
| Cross_BU Assumptions | Managing Director | Cross-BU Director | Managing Director |
| Managed Services / AMS | Oracle Practice BU Lead | AMS Lead Consultant | BU Lead |

**Rule:** No assumption document may be moved from Draft to Approved status without the BU Lead (or Managing Director for Cross_BU) explicitly granting approval. The AI system is never the approver.

---

## 3. Document Statuses

| Status | Meaning | Actions Permitted in Proposals |
|---|---|---|
| `Draft` | Under development; not yet reviewed by BU Lead | MUST NOT be used in external proposals; may be used in internal scoping documents with explicit label |
| `Pending Approval` | Submitted to BU Lead for review | MUST NOT be used in external proposals |
| `Approved` | BU Lead has reviewed and approved | May be used in proposals as per TENDER_ASSUMPTION_ASSEMBLY_RULES.md |
| `Under Review` | Approved version is being revised; current version remains active | Continue using approved version; updated version pending |
| `Superseded` | A newer approved version replaces this document | Must not use; reference only by version number for historical SOWs |
| `Retired` | Document withdrawn; do not use | Remove from all proposal assembly templates |

---

## 4. Versioning Rules

### Version Number Format
`Major.Minor` — Example: `1.0`, `1.1`, `2.0`

| Change Type | Version Increment | Approval Required |
|---|---|---|
| New assumption document | `1.0` (Draft) | BU Lead approval to move to Approved |
| Minor editorial correction (grammar, spelling, non-material wording) | `1.x` minor increment | BU Lead review only (expedited) |
| Addition of new assumptions to an existing document | `1.x` minor increment | BU Lead approval |
| Deletion of an assumption from an approved document | `1.x` minor increment | BU Lead approval + note in register |
| Material change to the scope or risk of an existing assumption | `x.0` major increment | BU Lead approval + change record |
| Structural reorganisation or section addition | `x.0` major increment | BU Lead approval |

### Version Control Rules
1. All versions are retained in the folder at `08_Commercial/Assumptions/[BU]/` with version number in the filename suffix (e.g., `HCM_BASE_ASSUMPTIONS_V2.md`).
2. The current approved version is always the highest version number with status `Approved`.
3. Superseded versions must be updated to status `Superseded` in their frontmatter but must NOT be deleted — retained for reference in active SOWs issued under that version.
4. The `ASSUMPTION_REGISTER.csv` is updated in parallel with every version change.

---

## 5. Approval Process

### Step 1 — Drafting
The Primary Owner (BU Lead nominee or senior consultant) drafts the assumption document. All items flagged for BU Lead confirmation (tagged `BU-WP11-XXX` in the draft) must be resolved before the document progresses to Step 2.

### Step 2 — BU Lead Review
The BU Lead reviews the complete assumption document against:
- Current commercial practice on active engagements
- Known scope disputes and project lessons learned from the past 12 months
- Consistency with approved capability statements in `07_Approved_Content/`
- Consistency with the Master Services Agreement (MSA) template
- Commercially defensible language (specific, unambiguous, enforceable)

### Step 3 — Approval Record
On approval, the BU Lead updates the document frontmatter:
```yaml
approved_by: "[BU Lead name]"
approved_date: "YYYY-MM-DD"
approved_for_reuse: true
status: "Approved"
```

### Step 4 — Register Update
The `ASSUMPTION_REGISTER.csv` is updated: all assumptions in the approved document are updated to `Status: Active`.

### Step 5 — Assembly Rules Update
If any new assumptions require specific assembly rules (for example, a new module-level assumption that activates only for a specific BOM line item), the `TENDER_ASSUMPTION_ASSEMBLY_RULES.md` is updated in the same approval cycle.

---

## 6. Change Control Process

### Minor Changes (editorial, no material scope impact)
1. Primary Owner makes the change in the document
2. BU Lead reviews by email within 3 business days
3. Frontmatter version incremented (e.g., 1.0 → 1.1)
4. `ASSUMPTION_REGISTER.csv` updated
5. No formal meeting required

### Major Changes (material scope, risk, or commercial impact)
1. Change Request raised by Primary Owner, documenting:
   - Assumption ID(s) affected
   - Nature of the change
   - Commercial reason for the change
   - Risk if the change is not made
2. BU Lead reviews and approves/rejects within 5 business days
3. If approved: document version incremented (e.g., 1.1 → 2.0); register updated; assembly rules reviewed
4. If rejected: change is recorded in the change log with rationale; status remains unchanged

### Emergency Change (live tender in progress)
If a material assumption error is identified while an assumption document is in active use on a current tender:
1. The BU Lead is notified immediately
2. A project-level override assumption is drafted and approved by the BU Lead for that specific tender only
3. The underlying assumption document is flagged for update in the next planned review cycle
4. The project-level override is documented in the SOW, not in the library document

---

## 7. Retirement Process

An assumption is retired when:
- It is no longer commercially defensible or accurate
- APPSolve's practice has changed such that the assumption no longer reflects delivery reality
- A change in Oracle product, legislation, or market practice makes the assumption obsolete

### Retirement Steps
1. Primary Owner flags the assumption for retirement and documents the reason
2. BU Lead approves retirement
3. The assumption status in `ASSUMPTION_REGISTER.csv` is updated to `Retired`
4. If the entire document is retired: frontmatter status updated to `Retired`; document renamed with `_RETIRED` suffix
5. Active SOWs and proposals referencing the retired assumption are reviewed by the relevant Project Manager; project-level overrides are applied where necessary

---

## 8. Tender Usage Rules

### Rule 1 — Approved Only
Only assumptions with status `Approved` in `ASSUMPTION_REGISTER.csv` may be used in proposals, SOWs, quotations, and tenders submitted to clients. Draft, Pending, Superseded, and Retired assumptions must not appear in external documents.

### Rule 2 — Assembly First
Assumptions are assembled using `TENDER_ASSUMPTION_ASSEMBLY_RULES.md`. The assembly rules define which packs are included for each BOM line item. Proposal authors must not manually select assumptions from the library without following the assembly rules.

### Rule 3 — No Client-Specific Modifications
Assumption text may not be modified in a proposal to reference a specific client, project, or individual. Client-specific context is added in the SOW cover, project charter, or proposal framing — not in the assumption statements themselves.

### Rule 4 — BU Lead Override Only
If the BU Lead determines that a specific assumption is not applicable to a tender, or that a project-specific variation is required, the BU Lead must approve the override in writing. The override is recorded in the tender's internal scope notes and the SOW; it does not change the library assumption.

### Rule 5 — Version Reference
The version of the assumption document used in a proposal must be recorded in the tender's internal scope notes (e.g., "Assumptions sourced from HCM_BASE_ASSUMPTIONS_V1.0, approved 2026-XX-XX"). This creates an audit trail for scope disputes.

### Rule 6 — Pending BU Lead Items
Assumptions flagged as requiring BU Lead confirmation (tagged `BU-WP11-XXX`) must be resolved by the BU Lead before the document is used in any tender. A document with unresolved BU items is in Draft status and must not be used externally.

---

## 9. Prohibited Practices

The following are prohibited without BU Lead written approval:

| Prohibited Action | Risk |
|---|---|
| Using Draft-status assumptions in external proposals | Commercial liability from unvalidated language |
| Modifying approved assumption text for a specific client without BU Lead approval | Creates a non-standard assumption that is not tracked or governed |
| Removing assumptions from a proposal without recording the removal | Scope gaps not documented; disputes at delivery |
| Adding bespoke assumptions without registering them | Untracked commercial commitments in the field |
| Referencing a specific client or project in an assumption statement | Breaches the reusability principle; creates client-specific liability |

---

## 10. Annual Review Cycle

The Commercial Assumptions Library is reviewed annually (target: every February, aligned to the new commercial year):

1. BU Leads review all `Approved` assumption documents for currency
2. Any assumptions that no longer reflect delivery reality are flagged for change or retirement
3. Any gaps identified from the prior year's tenders or scope disputes are added as new assumptions
4. The review outcome is documented in a brief Annual Review Note appended to `ASSUMPTION_GOVERNANCE.md`
5. Updated documents proceed through the standard approval process

---

## 11. Relationship to Other Tender Factory Documents

| Document | Relationship |
|---|---|
| `07_Approved_Content/` | Capability statements — what APPSolve delivers and its evidence. Assumptions govern the commercial terms under which it is delivered. Both must be used together. |
| `RESOURCE_RESPONSE_LIBRARY.md` | Standard response blocks for team structure, governance, support. Assumptions complement these blocks with the commercial scope boundary. |
| `CONSULTANT_INDEX.csv` | Named resources referenced in proposals. Assumption HCM-GEN-005 governs named resource substitution. |
| `COMPLIANCE_REGISTER.csv` | Compliance documents attached to proposals. Assumptions reference compliance obligations (POPIA, SoD, BEE) as client vs APPSolve responsibilities. |
| `TENDER_ASSUMPTION_ASSEMBLY_RULES.md` | Defines how assumptions are automatically selected and sequenced for each proposal type. Read this document before any proposal assembly. |
| `ASSUMPTION_REGISTER.csv` | The authoritative index of all registered assumptions, their status, and their category. |

---

*ASSUMPTION_GOVERNANCE v1.0 | WP11 — Commercial Assumptions Library | 2026-06-15*  
*Owner: Oracle Practice BU Lead (HCM, ERP, OIC, OCI) | Acumatica BU Lead | BeBanking BU Lead | Managing Director (Cross_BU)*
