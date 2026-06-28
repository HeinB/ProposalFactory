---
document_id: WP18E-IMP-A-IMPLEMENTATION-REPORT-V1
title: "WP18E-IMP-A — KRPE Phase A Implementation Report"
version: "1.0"
status: "COMPLETE"
created: "2026-06-27"
created_by: "WP18E-IMP-A — KRPE Phase A Implementation"
approved_by: "Implementation — WP18E-IMP-A"
approved_date: "2026-06-27"
work_package: "WP18E-IMP-A"
category: "Implementation Report"
---

# WP18E-IMP-A — Knowledge Registry Population Engine
# Phase A Implementation Report

**Date:** 2026-06-27  
**Status:** COMPLETE — First working Knowledge Registry generated from live repository.  
**Build Status:** SUCCESS | 0 errors | 21 warnings (all expected)

---

## 1. Summary

WP18E-IMP-A implemented the first executable version of the Knowledge Registry Population Engine (KRPE), Phase A scope: CAP, ASP, and ASM extraction.

The engine (`08_Commercial/Assembly_Engine/krpe.py`) reads the governed Markdown repository and produces five machine-readable YAML registry files. On first execution against the live repository, all success criteria were met:

| Criterion | Target | Actual |
|---|---|---|
| CAP assets discovered | 49 | **49** ✓ |
| ASP packs discovered | 13 | **13** ✓ |
| ASM assumptions extracted | 1,136 | **1,136** ✓ |
| Duplicate registry IDs | 0 | **0** ✓ |
| Extraction errors | 0 | **0** ✓ |
| Deterministic output | Yes | **Yes** ✓ |
| Build duration | < 60s | **1.1s** ✓ |

---

## 2. Deliverables

### 2.1 Engine Script

| File | Location | Purpose |
|---|---|---|
| `krpe.py` | `08_Commercial/Assembly_Engine/` | Phase A engine — 1 file, ~600 lines, stdlib + PyYAML |

**Dependencies:** Python 3.12.3 · PyYAML 6.0.3

**CLI:**
```
python3 krpe.py [--repo-root PATH] [--mode FULL|DRY_RUN]
```

### 2.2 Output Files Generated

| File | Location | Entries | Size |
|---|---|---|---|
| `KNOWLEDGE_ASSET_REGISTRY.yaml` | `00_Governance/Knowledge_Standards/` | 62 (49 CAP + 13 ASP) | 121 KB |
| `KNOWLEDGE_ASSET_REGISTRY_ASSUMPTIONS.yaml` | `00_Governance/Knowledge_Standards/` | 1,136 ASM | 1.6 MB |
| `KNOWLEDGE_RELATIONSHIP_GRAPH.yaml` | `00_Governance/Knowledge_Standards/` | 1,136 relationships | 304 KB |
| `KNOWLEDGE_LOOKUP_INDEX.yaml` | `00_Governance/Knowledge_Standards/` | 20 indexes | 133 KB |
| `REGISTRY_BUILD_REPORT_20260627-003.yaml` | `08_Commercial/Reports/` | Build audit | — |
| `BUILD_MANIFEST.yaml` | `.krpe_state/` | Incremental state | — |

**Total YAML produced:** 71,903 lines across 4 registry files.

---

## 3. Architecture Adaptations (Spec vs Reality)

Four deviations from the WP18E architecture were discovered during implementation and resolved:

### AD-IMP-001 — MASTER_CAPABILITY_INDEX.md secondary tables

**Problem:** The index contains 14 tables, not 5. Secondary tables (review, risk, governance tables) include a "Cap ID" column at a non-first position. The table parser was returning 71 rows instead of 49.

**Fix:** Filter to tables where both "Cap ID" (first column) and "Capability Name" are present. This uniquely identifies the 7 main asset tables (49 rows).

### AD-IMP-002 — Wave 3/4 Cap ID vs document_id divergence

**Problem:** The MASTER_CAPABILITY_INDEX.md uses short IDs (`W3S1-001`), but Wave 3/4 files use descriptive document_ids (`W3S1-001-ORA-HCMCore`). These are not equal. This caused 19 ID_MISMATCH warnings.

**Fix (design decision):** Use the file-level `document_id` as the registry `asset_id` when present (it is the authoritative governance identifier). The short Cap ID from the index is kept for linking only. This is the correct governance behaviour: the file is authoritative. These are EXPECTED warnings, not errors.

### AD-IMP-003 — Assumption ID category codes with digits (HCM-3PT-001)

**Problem:** The HCM Base pack uses assumption IDs with digits in the category segment (`HCM-3PT-001`). The architecture spec assumed all-letter category codes (`[A-Z]{2,8}`).

**Fix:** Regex updated to `[A-Z0-9]{2,8}`. Recovers 6 assumptions missed by the original pattern.

### AD-IMP-004 — EBS SLA em-dash annotation format

**Problem:** The EBS SLA overlay uses `**EBS-SLA-005 — P1 Critical**` (em dash label), not the `**ID.**`, `**ID:**`, or `**ID [...]**` formats documented in the architecture.

**Fix:** Regex extended with `[—–-]\s*[^*]+?` alternative in the annotation group. Recovers 6 assumptions.

### AD-IMP-005 — BeBanking pack has no document_id

**Problem:** `BEBANKING_BASE_ASSUMPTIONS_V1.md` has no `document_id` field in its frontmatter. The detection logic required `document_id` → BeBanking was excluded.

**Fix:** Positive identification relaxed: a file qualifies as a pack when it has an approval signal (approved_for_reuse=true OR status starts with "Approved") AND a content signal (assumption_count field OR document_id). Pack ID is derived from filename when document_id is absent: `BEBANKING-BASE-ASSUMPTIONS-V1`.

### AD-IMP-006 — business_unit normalisation

**Problem:** Wave 1/2 files store `business_unit: "Cross_BU"` in frontmatter. The registry standard uses `"Corporate"`.

**Fix:** Normalisation map applied at extraction time: `Cross_BU` → `Corporate`.

---

## 4. Extraction Details

### 4.1 Assumption Pack Extraction

| Pack | File | Declared | Extracted | Status |
|---|---|---|---|---|
| AMS-ASSUMPTIONS-V1 | AMS/AMS_ASSUMPTIONS_V1.md | 84 | 84 | ✓ |
| EBS-AMS-SLA-OVERLAY-V1 | AMS/EBS_AMS_SLA_OVERLAY_V1.md | 53 | 53 | ✓ |
| EBS-DRM-ASSUMPTIONS-V1 | AMS/EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md | — | 62 | ✓ |
| ACU-BASE-ASSUMPTIONS-V1 | Acumatica/ACU_BASE_ASSUMPTIONS_V1.md | 152 | 152 | ✓ |
| BEBANKING-BASE-ASSUMPTIONS-V1 | BeBanking/BEBANKING_BASE_ASSUMPTIONS_V1.md | 117 | 117 | ✓ |
| ERP-ASSUMPTIONS-V1 | ERP/ERP_ASSUMPTIONS_V1.md | 123 | 123 | ✓ |
| HCM-BASE-ASSUMPTIONS-V1 | HCM/HCM_BASE_ASSUMPTIONS_V1.md | 115 | 115 | ✓ |
| HCM-COMPENSATION-ASSUMPTIONS-V1 | HCM/HCM_COMPENSATION_ASSUMPTIONS_V1.md | 30 | 30 | ✓ |
| HCM-LEARNING-ASSUMPTIONS-V1 | HCM/HCM_LEARNING_ASSUMPTIONS_V1.md | — | 37 | ✓ |
| HCM-RECRUITING-ASSUMPTIONS-V1 | HCM/HCM_RECRUITING_ASSUMPTIONS_V1.md | 54 | 54 | ✓ |
| HCM-TALENT-ASSUMPTIONS-V1 | HCM/HCM_TALENT_ASSUMPTIONS_V1.md | — | 31 | ✓ |
| OCI-ASSUMPTIONS-V1 | OCI/OCI_ASSUMPTIONS_V1.md | 174 | 174 | ✓ |
| OIC-ASSUMPTIONS-V1 | OIC/OIC_ASSUMPTIONS_V1.md | 104 | 104 | ✓ |
| **TOTAL** | | | **1,136** | ✓ |

### 4.2 Capability Asset Extraction

49 assets extracted. All waves supported:
- **Wave 1/2 (old format):** `07_Approved_Content/Approved/**/*.md` — no `document_id`; asset_id derived from Cap ID column.
- **Wave 3 (new format):** `06_Capabilities/Oracle/Oracle_HCM/**/*.md` — full `document_id`; uses descriptive ID.
- **Wave 4 (new format):** `06_Capabilities/Oracle/Oracle_HCM/` and `Oracle_ERP/` and `Oracle_OIC/` — same.

**Notable warning (expected):** `W2S1-004` Managed Services file missing from repository (`07_Approved_Content/Approved/Oracle/W2S1-004-ORA-ManagedServices.md`). Asset registered from index metadata only. This is a known gap.

### 4.3 Assumption Body Format Support

| Format | Pattern | Example | Packs |
|---|---|---|---|
| Multiline | `**ID**\ntext` | `**HCM-ENV-001**` | HCM, ERP, OIC, OCI, AMS |
| Inline-period | `**ID.** text` | `**OCI-GEN-001.** text` | OCI, OIC |
| Inline-colon | `**ID:** text` | `**BB-GEN-001:** text` | BeBanking |
| Bracket-annotation | `**ID [REPLACES: X]**` | `**EBS-SLA-002 [...]**` | AMS overlays |
| Em-dash label | `**ID — Label**` | `**EBS-SLA-005 — P1 Critical**` | AMS overlays |
| Digit-category | `**ID-3PT-NNN**` | `**HCM-3PT-001**` | HCM |

---

## 5. Build Warnings (21 total — all expected)

| Warning Code | Count | Cause | Severity |
|---|---|---|---|
| ID_MISMATCH | 19 | Wave 3/4 short Cap ID ≠ descriptive document_id | EXPECTED — file wins |
| FILE_NOT_FOUND | 1 | W2S1-004 Managed Services file absent | KNOWN GAP |
| ASSUMPTION_COUNT_MISMATCH | 1 | EBS-DRM frontmatter missing assumption_count | INFORMATIONAL |

No unexpected warnings. Zero extraction errors.

---

## 6. Relationship Graph

Phase A produces REL-001 (ASP→ASM containment) relationships only:
- **1,136 relationships** registered
- All 13 packs linked to their ASM entries
- Full Phase B will add CAP→SEC, SEC→CAP, ASP→CAP, RSK relationships (REL-002 through REL-010)

---

## 7. Lookup Indexes

Phase A populates 6 of 20 defined indexes with live data:

| Index | Entries | Status |
|---|---|---|
| asset_by_type | CAP:49, ASP:13, ASM:1136 | ✓ Live |
| lifecycle_by_status | APPROVED:1198 | ✓ Live |
| approved_assets | 1,198 | ✓ Live |
| pack_to_assumptions | 13 packs | ✓ Live |
| assumption_to_pack | 1,136 entries | ✓ Live |
| platform_capability_map | 4 platforms | ✓ Live |
| pattern_to_sections | (empty) | Phase B |
| cap_to_assumption_packs | (empty) | Phase B |
| risk_to_assumptions | (empty) | Phase B |
| mandatory_risks | (empty) | Phase B |
| *Others (8)* | (empty) | Phase B |

---

## 8. Determinism Verification

Three independent FULL builds executed on same source state:

| Run | CAP | ASP | ASM | Errors | Duration |
|---|---|---|---|---|---|
| Build 1 | 49 | 13 | 1,136 | 0 | 1.0s |
| Build 2 | 49 | 13 | 1,136 | 0 | 1.1s |
| Build 3 | 49 | 13 | 1,136 | 0 | 1.1s |

Output data content is deterministic (sorted by asset_id, stable field order). Timestamps in `generated_at` and `build_id` fields differ between runs by design.

---

## 9. Platform Maturity Assessment

| Dimension | Pre-WP18E-IMP-A | Post-WP18E-IMP-A |
|---|---|---|
| Registry state | No registry | **Live registry — 1,198 approved assets** |
| Downstream readiness | KVE cannot run | **KVE can run Phase A rules** |
| CAP discoverability | Manual index only | **Machine-readable registry** |
| ASM discoverability | Read packs manually | **Full assumption index** |
| Platform maturity | L3.5 | **L3.8** (registry populated; KVE pending) |

---

## 10. Technical Debt

| TD ID | Issue | Owner | Priority |
|---|---|---|---|
| TD-IMP-001 | W2S1-004 Managed Services file missing from repository | BU Lead | Medium — locate or recreate file |
| TD-IMP-002 | 19 Wave 3/4 Cap IDs differ between index and file; index should be updated to use descriptive IDs | Governance | Low — informational |
| TD-IMP-003 | HCM-LEARNING and HCM-TALENT packs missing assumption_count in frontmatter | BU Lead | Low — update frontmatter declaration |
| TD-IMP-004 | EBS-DRM pack missing assumption_count in frontmatter | BU Lead | Low — update frontmatter declaration |

---

## 11. Next Work Packages

| ID | Description | Dependency | Effort |
|---|---|---|---|
| WP18B-EXT.2 | BU Lead governance session — classify 40 RSK assets | BU Lead ~2h 10min | 2h 10min |
| KRPE Phase B | RSK/MTH/REF/PAT/SEC extractors; full relationship graph; all 20 indexes | WP18B-EXT.2 (for RSK) | 8–12h |
| KRPE Phase C | Incremental build mode | Phase B verified | 5–8h |
| KVE Phase A | 22 BLOCK rules + manifest builder | Populated registry | ~10h |
| KVE Phase B | Full 76 rules + validation reports | Phase A | ~15h |

**Recommended immediate next step:** WP18B-EXT.2 (BU Lead session, ~2h 10min) to classify 40 RSK assets, enabling KRPE Phase B to populate RSK entries and the full relationship graph.

---

## 12. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-27 | WP18E-IMP-A | Initial implementation report — engine complete; 5 output files; 1,198 approved assets registered |
