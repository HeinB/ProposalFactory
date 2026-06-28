---
document_id: GOVERNANCE-DELTA-REPORT
title: "Governance Delta Report — WP11G"
version: "1.0"
created: "2026-06-16"
created_by: "WP11G — Governance Reconciliation"
---

# Governance Delta Report — WP11G

**Purpose:** Documents what was stale, what was corrected, what remains outstanding, and what blocks or does not block WP12.
**Reference date:** 2026-06-16

---

## 1. What Was Stale

### HANDOVER.md (last updated: 2026-06-14 — Wave 4 only)
- Cited approved count as **47** — actual count is **49** (WP7 added W5-ACU-001 + W5-METH-001)
- Did not reflect WP7 (reference registration, W5-ACU-001, W5-METH-001)
- Did not reflect WP8 (Compliance Register work)
- Did not reflect WP9 (reference letter registration: 11 Oracle + 5 Acumatica letters)
- Did not reflect WP10 (Consultant Index: 49 consultants registered)
- Did not reflect WP11 (Assumption Library: 4 packs approved, 439 assumptions; 4 draft packs)
- Did not reflect WP11F (Commercial Framework: 5 draft documents)
- Did not reflect WP12 (Plennegy pilot: 63/100 complete)
- Did not reflect WP13 (DOCX draft: ~80% complete)
- Did not reflect WP11G (this session — governance reconciliation)
- Listed Directors' Resolution as EXPIRED — **RESOLVED 2026-06-15**
- Listed Public Liability Insurance as MISSING — **OBTAINED 2026-06-15**
- AM-W4E1-001 and AM-W4E2-001 cited as ACTIVE — both **REMOVED in WP7** (letters registered)

### AI_CONTEXT.md (last updated: 2026-06-10 — Wave 1 only)
- Approved content section listed 25 assets — actual count is **49**
- No mention of Wave 2, Wave 3, Wave 4, or WP5-WP13 work
- No Assumption Library section
- No Commercial Framework section
- No Reference Register section
- Compliance fact baseline stale (Directors' Resolution, Public Liability Insurance)
- Content gap awareness section incomplete (most gaps from Wave 1 have since been resolved)
- No current work queue

### COMPLIANCE_REGISTER.csv
- COMP-008 (Public Liability Insurance): status MISSING — **corrected to ACTIVE — OBTAINED 2026-06-15**
- COMP-011 (Directors' Resolution): status RENEWAL REQUIRED, expiry 2026-03-01, days -106 — **corrected to ACTIVE — RENEWED 2026-06-15, expiry 2027-06-15**

### memory/MEMORY.md and memory/project_context.md
- Both correctly reflected WP11E-A, WP11F, and the compliance updates as of 2026-06-15
- project_context.md approved count cited 47 — needs update to 49 (WP7 not captured in memory)

### CURRENT_STATE.md (v3.4, updated 2026-06-14)
- Pipeline snapshot shows 47 approved — actual is 49 (W5-ACU-001, W5-METH-001 added WP7 after CURRENT_STATE was written)
- Does not reflect WP8–WP13 or WP11 assumption library

---

## 2. What Was Corrected in This Session (WP11G)

| File | Change |
|---|---|
| `01_Compliance/COMPLIANCE_REGISTER.csv` | COMP-008: MISSING → ACTIVE — OBTAINED 2026-06-15 |
| `01_Compliance/COMPLIANCE_REGISTER.csv` | COMP-011: RENEWAL REQUIRED → ACTIVE — RENEWED 2026-06-15 |
| `HANDOVER.md` | Full rewrite — reflects WP7–WP13, 49 approved assets, assumption library, commercial framework, Plennegy status, all governance rules |
| `AI_CONTEXT.md` | Full rewrite — reflects all approved assets (49), assumption library (4 packs), commercial framework, reference register (16 active), updated fact baseline, updated governance rules, current work queue |
| `00_Governance/OUTSTANDING_ACTION_REGISTER.md` | Created new — 51 items classified across 9 categories; resolves pre-WP11G governance ambiguity |
| `00_Governance/GOVERNANCE_DELTA_REPORT.md` | Created new — this document |
| `memory/MEMORY.md` | To be updated: 47 → 49 approved; add WP11G complete |

---

## 3. What Remains Outstanding (Not Corrected in WP11G)

| Item | Reason Not Corrected |
|---|---|
| CURRENT_STATE.md (v3.4) | Major rewrite deferred — HANDOVER.md + AI_CONTEXT.md are the primary session entry points; CURRENT_STATE.md is now secondary |
| memory/project_context.md approved count (47 → 49) | Update queued in this session |
| HIST registration (OAR-G01) | Requires manual DOCUMENT_REGISTER.csv work — human action |
| Superseded DRAFT file deletion (OAR-G02) | Requires Finder on OneDrive — human action |
| Hollywood Bets reference letter (OAR-B01) | Requires AM engagement — human action |
| KPMG reference letter (OAR-B02) | Requires account manager contact — human action |

---

## 4. What Blocks WP12 (Proposal Assembly Engine)

For WP12 to produce a complete, submission-ready Plennegy proposal:

| Blocker | ID | Action |
|---|---|---|
| **AM approval for Hollywood Bets** | OAR-C01 | Oracle BU Lead / AM to confirm HB can be named in Plennegy |
| **Costing section** missing from Plennegy draft | OAR-C02 | Add commercial section to PLENNEGY_DRAFT_RESPONSE.docx |
| **Word TOC generation** | OAR-C03 | Generate after all sections are confirmed |
| **Plennegy payroll/entity confirmation** | OAR-C04 | Confirm parallel run scope with client |
| **Oracle awards verification** | OAR-C05 | BU Lead to confirm awards wording before submission |
| **B-BBEE certificate** | OAR-A01 | Not immediately blocking (expires 2026-07-31) — check at submission time |

> WP12 (assembly and formatting) can proceed in parallel with OAR-C01/C02/C03/C04/C05 resolution. The final Plennegy submission cannot be approved without OAR-C01 (HB AM approval) and OAR-C02 (Costing section).

---

## 5. What Does Not Block WP12

| Item | Notes |
|---|---|
| HCM module pack approvals (OAR-D01–D04) | HCM Base pack (114 assumptions) provides full base coverage. Module-specific packs desirable but not blocking. |
| Commercial Framework BU review (OAR-D05) | Internal methodology — does not affect Plennegy assembly |
| POPIA / PAIA (OAR-E01/E02) | Not required for Plennegy tender |
| Consultant evidence gaps (OAR-F01–F06) | Consultant Index complete enough for Plennegy resource section |
| Admin / hygiene items (OAR-G01–G10) | None directly block Plennegy submission |
| Future extraction (OAR-H01–H07) | Desirable but not blocking |

---

## 6. WP12 Recommendation

**WP12 can start immediately.** The assembly engine can produce the full Plennegy draft structure using:
- 49 approved KB capability assets (W1S1, W1S2, W1S3, W2S1, W3S1, W4, W5)
- 4 approved assumption packs (HCM Base, OIC, ERP, AMS)
- 16 active reference letters (11 Oracle + 5 Acumatica)
- 49 consultant records (CONSULTANT_INDEX.csv)

**Items that must be resolved BEFORE final Plennegy submission:**
1. OAR-C01 — AM approval for Hollywood Bets
2. OAR-C02 — Costing section added
3. OAR-C03 — Word TOC generated
4. OAR-A01 — B-BBEE certificate valid at submission date

**Items that can run in parallel with WP12:**
- HCM module pack approvals (OAR-D01–D04)
- Commercial Framework BU review (OAR-D05)
- HIST registrations (OAR-G01)
- Reference letter programme (OAR-B01 HB, OAR-B02 KPMG, OAR-G07 Harmony)

---

*GOVERNANCE_DELTA_REPORT v1.0 | WP11G — Governance Reconciliation | 2026-06-16*
