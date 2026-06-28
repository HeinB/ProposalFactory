# Consultant Index Programme
**Status:** Planned — not started
**Architecture basis:** ADR-001-CV_SOURCE_OF_TRUTH.md
**Date created:** 2026-06-10
**Decision:** D-ARCH-001

> This is a planning document. No consultant index records exist yet.
> Do not create records until this programme is formally initiated.
> Do not import CV content from APPTime or the Tender Pack.

---

## Purpose

This document defines the scope, field design, ownership model, maintenance cycle, and effort estimate for creating and maintaining Consultant Index Records in the Knowledge Base.

Consultant Index Records are the KB's representation of APPSolve's consultant team. They enable AI-assisted tender composition — specifically, skill matching and consultant candidate identification — without reproducing CV content that is authoritative in APPTime.

---

## Scope

### In scope

- All active APPSolve consultants who may be named in tender responses
- Metadata fields only: name, role, BU, skill tags, active certifications, availability flag, APPTime reference
- Location: `03_People/Resource_Profiles/[BU]/CV-XXX.md`

### Out of scope

- Full CV text, Professional Summary paragraphs, Project Experience narratives
- Education narratives
- Historical / archived consultant records (create only for active consultants initially)
- Contractors or associates who are not APPSolve employees (unless regularly named in tenders)

---

## Record Design

Each record uses the redesigned `CV_template.md` (see `00_Governance/Templates/CV_template.md`).

### Metadata fields

| Field | Type | Purpose | Owner |
|---|---|---|---|
| `doc_id` | String (CV-XXX) | Unique KB identifier | HR/PM lead at creation |
| `person_name` | String | Full name as it appears in tenders | HR lead |
| `role` | String | Formal tender title (e.g. "Senior Oracle Fusion Consultant") | BU lead |
| `business_unit` | Enum | Oracle / Acumatica / BeBanking / Cross | BU lead |
| `status` | Enum | Active / Archived | HR lead |
| `skill_tags` | List of strings | 5–10 keywords for AI matching | BU lead |
| `modules_or_products` | List of strings | Specific module/product expertise | BU lead |
| `active_certifications` | List of strings | Name + expiry; links to CERT-XXX | HR lead |
| `available_for_tenders` | Boolean | False if long-term deployed | PM lead |
| `apptime_id` | String | APPTime employee/consultant ID | HR lead at creation |
| `notes` | String | Deployment status, availability notes | PM lead |
| `last_reviewed` | Date | When record was last verified | HR/PM lead |

### Fields deliberately excluded

| Field | Why excluded |
|---|---|
| `years_experience` | Calculated field; APPTime authoritative; drifts if static |
| `years_at_appsolve` | Same reason |
| `cv_version` | Version management is APPTime's responsibility |
| Professional Summary | Full CV text — APPTime only |
| Project Experience | Full CV text — APPTime only |
| Education | Not needed for AI matching |

---

## APPTime Extraction Process

### What to extract from APPTime (per consultant)

At record creation time, the following data should be sourced from APPTime:

1. **Full name** — as it should appear in tenders
2. **Current role/title** — formal title for tender use
3. **APPTime employee ID** — for the `apptime_id` field
4. **Skills/competencies** — derive `skill_tags` from APPTime's competency/skill records
5. **Active certifications** — current, non-expired certifications with expiry dates
6. **Current deployment status** — derive `available_for_tenders` flag

### What NOT to copy from APPTime into the KB record

- CV narrative text of any kind
- Project history / work history
- Education / qualifications

### Process for creating a record

1. Log into APPTime
2. Open consultant profile
3. Copy the metadata fields listed above into a new `CV-XXX.md` record using the CV_template.md
4. Complete the `AI Retrieval Notes` section based on BU lead knowledge of the consultant's tender relevance
5. Set `apptime_id` to the consultant's APPTime reference
6. Submit to HR/PM lead for review
7. Register the new record in DOCUMENT_REGISTER.csv with `doc_type: CV`, `status: Active`

---

## Folder Structure

```
03_People/
├── Certifications/         ← Individual and company certification documents (CERT-XXX)
├── CVs/                    ← NOT USED — APPTime only. See ADR-001.
└── Resource_Profiles/      ← Consultant Index Records (CV-XXX.md files)
    ├── Oracle/
    ├── Acumatica/
    ├── BeBanking/
    └── Cross/
```

**03_People/CVs/** contains no KB content. Full CV PDFs are generated from APPTime on demand. The folder exists structurally but should not be populated.

---

## Naming Convention

| Field | Convention |
|---|---|
| Doc ID | `CV-001`, `CV-002`, ... (sequential) |
| Filename | `CV-XXX-[Surname]-[Initials].md` — e.g. `CV-001-Blignaut-HB.md` |
| Folder | BU of primary service area: `Oracle/`, `Acumatica/`, `BeBanking/`, `Cross/` |

---

## Ownership Model

| Role | Responsibility |
|---|---|
| **HR/PM lead** | Creates records at onboarding; retires records at departure; maintains `apptime_id`, `available_for_tenders`, `last_reviewed` |
| **BU lead (Oracle/Acumatica/BeBanking)** | Approves `skill_tags`, `role`, `modules_or_products`; updates when focus area changes |
| **HR lead** | Maintains `active_certifications` when certs are earned, renewed, or expire |
| **PM lead** | Updates `available_for_tenders` when consultant starts or ends long-term deployment |

No mandatory review schedule. Updates are event-driven. The KB index record should reflect APPTime — verify against APPTime when any field changes.

---

## Maintenance Cycle

Records are updated when any of the following events occur:

| Event | Update required |
|---|---|
| New consultant joins APPSolve | Create new CV-XXX record |
| Consultant leaves APPSolve | Set `status: Archived`; set `available_for_tenders: false` |
| Certification earned | Add to `active_certifications` (with expiry); link to new CERT-XXX record |
| Certification expires | Remove from `active_certifications` |
| Consultant starts long-term deployment | Set `available_for_tenders: false`; add notes with expected return date |
| Consultant returns from long-term deployment | Set `available_for_tenders: true`; clear deployment note |
| Role/title changes | Update `role` field |
| Technology focus changes significantly | Update `skill_tags` and `modules_or_products` |

---

## Effort Estimate

### Initial programme (50+ active consultants)

| Activity | Effort per record | Total (50 consultants) |
|---|---|---|
| APPTime data extraction and record creation | 15–20 min | 12–17 hours |
| BU lead review of skill tags and role titles | 5–10 min | 4–8 hours |
| Registration in DOCUMENT_REGISTER.csv | 5 min | 4 hours |
| **Total estimated** | **25–35 min** | **~20–29 hours** |

**Recommended approach:** Complete one BU at a time. Oracle first (largest team), then Acumatica, then BeBanking, then Cross-BU. This allows BU leads to review their consultants as a batch.

### Ongoing maintenance (per year)

Estimated 10–20 record updates per year across certification changes, role changes, and availability changes. At 10 minutes per update: approximately 2–3 hours/year.

---

## Pre-conditions for Starting

Before the programme begins, confirm:

- [ ] APPTime access confirmed for the programme lead
- [ ] BU leads for Oracle, Acumatica, and BeBanking confirmed as skill tag approvers
- [ ] HR lead confirmed as certification and status owner
- [ ] PM lead confirmed as deployment status owner
- [ ] Sequential CV-XXX numbering scheme agreed (start at CV-001)
- [ ] `03_People/Resource_Profiles/[BU]/` sub-folder structure created in KB

---

## Relationship to Other KB Components

| KB Component | Relationship |
|---|---|
| `CERT-XXX` records in `03_People/Certifications/` | CV records reference CERT-XXX doc IDs in `active_certifications` |
| `DOCUMENT_REGISTER.csv` | Each CV-XXX record has a corresponding register row |
| APPTime | Primary source for all consultant data; KB is a derived metadata index |
| `AI_CONTEXT.md` | Defines how AI uses CV records (skill-matching only; never CV text generation) |
| `ADR-001-CV_SOURCE_OF_TRUTH.md` | Architecture decision underpinning this programme |
