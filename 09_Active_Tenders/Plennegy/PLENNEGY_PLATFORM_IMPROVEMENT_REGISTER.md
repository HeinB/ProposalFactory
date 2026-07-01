---
document_id: PLENNEGY-PLATFORM-IMPROVEMENT-REGISTER
title: "PF2-006 — Platform Improvement Register"
version: "1.0"
created: "2026-06-30"
work_package: "PF2-006"
---

# PF2-006 — Platform Improvement Register

**Source:** PF2-006 Operational Validation — Plennegy Oracle HCM Full Suite
**Date:** 2026-06-30

This register captures all platform improvements identified during the first live operational validation. Items marked IMPLEMENTED were fixed in PF2-006. Items marked BACKLOG are recommendations for future work packages.

---

## Implemented in PF2-006

### C-PSAE-001 — PSAE `--context` Flag

| Field | Value |
|---|---|
| **Component** | `proposal_section_engine.py` (PSAE) |
| **Priority** | P0 — Blocked production use of PSAE |
| **Type** | Platform Defect |
| **Status** | IMPLEMENTED |
| **Fix** | Added `--context YAML_FILE` CLI argument. Loads tender context from any YAML file with `tender_context:` wrapper. Normalises `pattern` field to `tender_pattern`. Calls `build_section_manifest()`, writes manifest to `Proposals/[TENDER_ID]/`, prints section counts and validation messages. |
| **Regression** | 6/6 PASS after fix |
| **Generalises to** | All future production tenders — any tender can now be processed by providing a context YAML |

---

### C-RENDERER-001 — Assumption Pack Multi-Source MERGE Fix

| Field | Value |
|---|---|
| **Component** | `proposal_section_engine.py` (PSAE SECTION_DEFS) |
| **Priority** | P0 — Silently dropped assumption packs 2–N |
| **Type** | Platform Defect |
| **Status** | IMPLEMENTED |
| **Fix** | Changed `assembly_method` from `"DIRECT"` to `"MERGE"` for sections S-49 (Key Assumptions), S-51 (Commercial Assumptions), and A-01 (Complete Assumption Schedule). `MERGE` iterates all `source_assets` and concatenates in selection order. |
| **Root cause** | `DIRECT` is designed for single-source sections; using it for multi-source assumption aggregation sections was architecturally incorrect. Hidden in regression because ARM-IT045 (EBS AMS) has only 1 ASP pack. |
| **Impact** | All multi-pack HCM tenders now render complete assumption schedules. For Plennegy: 5 packs (HCM Base + Recruiting + Learning + Talent + OIC) correctly rendered across S-49, S-51, A-01. |
| **Regression** | 6/6 PASS after fix |
| **Generalises to** | All Oracle HCM tenders with 2+ assumption packs selected |

---

## Backlog — Recommended for Future Work Packages

### PIR-001 — Sub-section EXTRACT capability for methodology assets

| Field | Value |
|---|---|
| **Component** | Renderer (`_render_extract`) |
| **Priority** | P2 |
| **Type** | Enhancement |
| **Description** | S-36 (Project Governance) uses EXTRACT method with W2S1-005 as source, but the renderer includes the full asset body instead of extracting the governance sub-section. Sub-section extraction (by heading title or marker) would allow S-34 (Methodology) and S-36 (Governance) to draw from different parts of W2S1-005 without duplication. |
| **Effort estimate** | Medium — requires heading-based extraction logic in renderer |
| **Generalises to** | Any section using EXTRACT method from a multi-section asset |

---

### PIR-002 — Oracle Recruiting Booster KB Asset (Wave 5)

| Field | Value |
|---|---|
| **Component** | Knowledge Base content |
| **Priority** | P2 |
| **Type** | Knowledge Gap |
| **Description** | No governed KB asset exists for Oracle Recruiting Booster. Relevant for Plennegy and any future Oracle Recruiting Cloud tender with Booster scope. Asset should follow W3S1-xxx naming convention and be governed through standard approval process. |
| **Generalises to** | All Oracle Recruiting Cloud tenders where Booster is in scope |

---

### PIR-003 — Oracle Touch Points KB Asset (Wave 5)

| Field | Value |
|---|---|
| **Component** | Knowledge Base content |
| **Priority** | P2 |
| **Type** | Knowledge Gap |
| **Description** | No governed KB asset exists for Oracle Touch Points. Relevant for Plennegy and any future Oracle HCM tenant with Touch Points in scope. |
| **Generalises to** | All Oracle HCM tenders where Touch Points is in scope |

---

### PIR-004 — Agribusiness/FMCG Sector Context Asset

| Field | Value |
|---|---|
| **Component** | Knowledge Base content |
| **Priority** | P3 |
| **Type** | Knowledge Gap |
| **Description** | No sector-specific reference or context exists for Agribusiness/FMCG. Future tender to Agribusiness clients (food producers, agricultural holdings, FMCG) would benefit from a governed sector context statement. |
| **Generalises to** | Future Agribusiness/FMCG tenders |

---

### PIR-005 — Tender context YAML validation against PSAE schema

| Field | Value |
|---|---|
| **Component** | `proposal_section_engine.py` (PSAE CLI `--context`) |
| **Priority** | P3 |
| **Type** | Enhancement |
| **Description** | The `--context` flag does not validate required fields in the YAML against the known schema (tender_id, platform, engagement_type, etc.). Adding schema validation would catch malformed context files early with useful error messages. |
| **Generalises to** | All production tender context files |

---

*PLENNEGY_PLATFORM_IMPROVEMENT_REGISTER v1.0 | PF2-006 | 2026-06-30*
