# ADR-001 — CV Source of Truth: APPTime as System of Record
**Type:** Architecture Decision Record
**Status:** Accepted
**Decision ID:** D-ARCH-001
**Date:** 2026-06-10
**Decision maker:** Hein Blignaut (APPSolve)
**Prepared by:** Claude (AI — design review and documentation)
**Cross-references:** CONSULTANT_INDEX_PROGRAMME.md; AI_CONTEXT.md (Consultant Records section); PROJECT.md (D-ARCH-001)

---

## Context

APPSolve's Tender Knowledge Base was initially designed to include full CV documents extracted from the Tender Pack `Rate Card/` folder and maintained as KB content in `03_People/CVs/`. The CV_template.md sidecar template was designed accordingly — encoding a full CV structure including Professional Summary, Relevant Project Experience table, Certifications section, and Education narrative.

During Wave 1 planning, MIGRATION_ANALYSIS.md identified 42 consultant CV PDFs for migration into the KB, with planned destinations `03_CVs/[BU]/`.

**New information (2026-06-10):** APPSolve maintains all consultant CVs in APPTime (internal time and resource management system). CVs are generated from APPTime on demand for quotes, proposals, RFPs, and tender submissions. APPTime is the actively maintained, authoritative record of consultant profiles.

---

## Problem Statement

If full CV documents are extracted into the Knowledge Base, four problems result:

1. **They will drift.** The KB copies will fall behind APPTime. Certifications expire, projects complete, roles change. There is no automated synchronisation between APPTime and the KB.

2. **They create a third source of truth.** Consultant CV data already exists in APPTime (authoritative) and the Tender Pack `Rate Card/` folder (APPTime exports at various timestamps). A third KB copy adds maintenance burden without adding value.

3. **They create accuracy risk.** An AI-assisted tender response drawing from a stale KB CV could misrepresent a consultant's current credentials, certifications, or project experience — a material accuracy risk in competitive tenders.

4. **The proposed migration already shows version problems.** MIGRATION_ANALYSIS.md records multiple duplicate CV versions for the same consultant across different tender submission folders (root `Rate Card/` vs `Rate Card/ETS Tender/` copies). Migrating these into the KB imports the version confusion rather than resolving it.

---

## Alternatives Considered

### Option A — No CV content in KB; APPTime only

**Pros:** Zero maintenance overhead; no drift; APPTime always current.

**Cons:** AI-assisted tender composition cannot identify candidate consultants without reading CV data. The AI is blind to who has what skills and cannot assist with resource matching for tenders.

**Verdict: Rejected.** The AI needs structured consultant data to assist with tender composition. Without any consultant data in the KB, skill-matching and resource identification must be done manually for every tender.

---

### Option B — CV metadata in KB; APPTime authoritative ✅ SELECTED

**Pros:** Lean Consultant Index Records provide AI skill-matching capability; metadata is stable and low-maintenance compared to full CV narrative; APPTime remains the single source for full CV content.

**Cons:** Metadata still requires periodic updates; ownership must be defined.

**Verdict: Accepted.** The metadata fields needed for AI tender assistance (skill tags, certifications, availability) are stable and event-driven to update. Full CV narrative text is not needed for AI matching — it is needed only at the point of tender submission, at which time the current CV is generated from APPTime.

---

### Option C — Full CV copies in KB; periodic sync

**Pros:** Full content available for AI; complete offline reference.

**Cons:** Highest maintenance burden; highest drift risk; duplicates APPTime; periodic sync is unreliable in practice and tends to be skipped. The Tender Pack `Rate Card/` folder already demonstrates this with duplicate/versioning problems across tender-specific subfolders.

**Verdict: Rejected.** This is the worst option for data integrity and produces the highest risk of AI fabricating or misrepresenting consultant credentials.

---

## Decision

**APPTime is the authoritative source for consultant CV content.**

The Knowledge Base stores **Consultant Index Records** only — lightweight metadata records that enable AI skill-matching and consultant candidate identification, without reproducing CV narrative content.

### What Consultant Index Records contain

| Field | Purpose |
|---|---|
| Consultant name | Identity |
| Role (tender title) | How to describe this person in a tender |
| Business unit | Oracle / Acumatica / BeBanking / Cross |
| `skill_tags` (5–10 keywords) | AI skill-matching: "who can work on Oracle Fusion Financials?" |
| `active_certifications` (name + expiry) | AI matching; links to CERT-XXX records in KB; expiry visible for compliance |
| `available_for_tenders` flag | Prevents AI from recommending a consultant on long-term deployment |
| APPTime reference ID | Escalation path: pull current CV from APPTime at tender time |

### What Consultant Index Records do NOT contain

| Excluded field | Reason |
|---|---|
| Professional Summary paragraph | Authored and maintained in APPTime; KB copy will drift |
| Relevant Project Experience table | Grows with every project; APPTime owns this |
| Years of experience / years at APPSolve | Calculated fields; APPTime owns them |
| Education narrative | Not needed for AI skill-matching |
| Any full CV text | APPTime is authoritative |

### How AI should use Consultant Index Records

1. Tender requirement identified → AI reads index records to identify consultants whose `skill_tags` and `active_certifications` match
2. AI proposes candidates with matching profiles, noting `available_for_tenders` status
3. AI instructs the user: "Obtain current CVs from APPTime for [listed candidates]"
4. User generates current CVs from APPTime and attaches to tender response
5. AI drafts surrounding narrative (team introduction, resource plan) using skill tags + approved capability content from the KB

**The AI must never generate CV text from KB index records.** Skill tags are for identification only — not for content generation.

---

## Rationale

1. The drift risk of full CV copies in the KB is real and demonstrated by the Tender Pack `Rate Card/` folder, which already has multiple duplicate versions of the same CV.

2. The KB design pre-dated the discovery that APPTime is the authoritative CV source. This decision corrects the design.

3. The AI value from CV data is skill-matching (who has the right skills?), not content generation (what should this CV say?). Skill tags achieve the former without the maintenance burden of the latter.

4. Event-driven updates (new certification earned, role change, departure, long-term deployment start/end) are more reliable than scheduled sync cycles for a team of 50+ consultants.

---

## Consequences

### Immediate (applied 2026-06-10)

| Document | Change |
|---|---|
| `00_Governance/Templates/CV_template.md` | Redesigned as Consultant Index Record template — content sections removed |
| `00_Governance/MIGRATION_ANALYSIS.md` | Priority 25 (CV migration) cancelled; historical table preserved |
| `03_People/CVs/` folder | Documented as not used for KB content; APPTime-only note added |
| `03_People/Resource_Profiles/` | Promoted as active folder for Consultant Index Records |
| `AI_CONTEXT.md` | Permanent consultant record rules added |
| `PROJECT.md` | D-ARCH-001 strategy decision recorded |
| `HANDOVER.md` | CV Architecture Review milestone added |
| `00_Governance/KNOWLEDGE_BASE_STATUS.md` | CV extraction gap replaced with Consultant Index Record Programme entry |
| `00_Governance/CONSULTANT_INDEX_PROGRAMME.md` | Implementation backlog created |

### Future

- Consultant Index Records created in `03_People/Resource_Profiles/` per CONSULTANT_INDEX_PROGRAMME.md
- At tender time: AI identifies candidates from index records → user retrieves current CVs from APPTime → user provides CVs for tender composition
- Full CV PDFs in Tender Pack `Rate Card/` remain read-only in their original location as historical records — never migrated into the KB

---

## Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| `available_for_tenders` flag not updated when consultant starts long-term deployment | Medium | Medium — AI recommends unavailable consultant | Ownership assigned in CONSULTANT_INDEX_PROGRAMME.md; PM lead responsibility |
| `active_certifications` not updated when cert expires | Medium | High — AI references expired credential | CERT-XXX records in KB have independent expiry tracking; cross-reference at tender time |
| APPTime inaccessible at tender time | Low | High — no fallback CV content | AI can draft surrounding narrative from skill tags; user must retrieve CV directly |
| Future session reverts to full CV extraction model | Low | High — re-imports drift risk | Rules encoded permanently in AI_CONTEXT.md; this ADR is the blocker |

---

## Future Maintenance Model

| Activity | Owner | Trigger |
|---|---|---|
| Create Consultant Index Records (initial) | HR/PM lead | CONSULTANT_INDEX_PROGRAMME.md rollout |
| Update `available_for_tenders` flag | PM lead | Consultant starts or ends long-term deployment |
| Update `active_certifications` | HR lead | Certification earned, expired, or renewed |
| Update `skill_tags` | BU lead | Major project completion; technology focus change |
| Update `role` | HR lead | Formal title change |
| Retire record (`status: Archived`) | HR lead | Consultant leaves APPSolve |

**No mandatory review schedule.** Updates are event-driven. APPTime is the primary maintenance target — KB index records reflect APPTime, not the other way around.

---

*This ADR supersedes the CV extraction design in MIGRATION_ANALYSIS.md (Wave 1 Priority 25) and the original CV_template.md full-CV design.*
