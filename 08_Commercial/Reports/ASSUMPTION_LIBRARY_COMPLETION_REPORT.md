---
document_id: ASSUMPTION-LIBRARY-COMPLETION-REPORT
title: Assumption Library Completion Report
version: "1.0"
status: COMPLETE
date: "2026-06-30"
work_package: PF2-005
platform_maturity: L5.6
---

# Assumption Library Completion Report

**Work Package:** PF2-005 — Assumption Library Materialisation
**Date:** 2026-06-30
**Outcome:** COMPLETE — 0 NOT_FOUND assumption packs across all 6 regression scenarios

---

## 1. Objective

Eliminate all NOT_FOUND assumption asset resolutions during proposal rendering by ensuring every
Assumption Pack (ASP) referenced in the Proposal Factory is discoverable by the renderer.

---

## 2. Pre-Condition State (PF2-004 Baseline)

After PF2-004 (Proposal Renderer v1.0), ARM-IT045 rendered with:

| Status | Count |
|---|---|
| RENDERED | 16 |
| PLACEHOLDER | 17 |
| AI-DRAFT | 3 |
| NOT_FOUND | **9** |

The 9 NOT_FOUND assets were all Assumption Packs (ASP type). The `AssetIndex` scanned only
`07_Approved_Content/Approved/`, which contains no ASP files. ASP source files live in
`08_Commercial/Assumptions/` and use underscore-based filenames (`OIC_ASSUMPTIONS_V1.md`)
that do not match hyphenated canonical IDs (`OIC-ASSUMPTIONS-V1`).

---

## 3. Root Cause

The `AssetIndex` in `proposal_renderer.py` used filename stem as the sole lookup key.
Assumption Pack files had mismatched filenames vs. canonical IDs, and resided in a directory
outside the content scan root. No new files needed to be created — the 13 approved ASP files
already existed with correct `document_id` fields and `lifecycle_status: APPROVED`.

---

## 4. Solution: AssetIndex Extension

**Change:** Extended `AssetIndex.__init__` to accept `additional_roots: Optional[List[str]]`.
A new `_extract_document_id()` static method parses YAML frontmatter from each `.md` file and
returns the `document_id` value. When scanning additional roots, files are indexed by
`document_id` rather than filename stem, enabling ID-based lookup regardless of filename
convention.

**Zero data duplication:** No ASP files were copied or moved. The single canonical source in
`08_Commercial/Assumptions/` is used directly.

**Single source of truth:** `document_id` in frontmatter is the authoritative identity; the
`AssetIndex` now respects this for all secondary roots.

### Code Change Summary

```python
# Before (PF2-004)
asset_index = AssetIndex(args.content_root)  # scanned 07_Approved_Content/Approved/ only

# After (PF2-005)
asset_index = AssetIndex(args.content_root, additional_roots=[ASSUMPTIONS_ROOT])
# also scans 08_Commercial/Assumptions/ and indexes by document_id
```

`AssetIndex` stats after change:
- Files indexed: **76** (was 50)
- IDs indexed: **125** (was 99)
- Net addition: 26 files / 26 IDs (all from Assumptions directory)

---

## 5. Pre-existing Fix: BeBanking document_id

`BEBANKING_BASE_ASSUMPTIONS_V1.md` was the only ASP file missing a `document_id` field
in its YAML frontmatter. This was identified during investigation and corrected (added
`document_id: BEBANKING-BASE-ASSUMPTIONS-V1`) before the `AssetIndex` extension was applied.
All 13 ASP files now carry a `document_id` that matches their canonical registry ID.

---

## 6. All 13 Assumption Packs — Resolution Status

| Canonical ID | Source File | Status |
|---|---|---|
| OIC-ASSUMPTIONS-V1 | OIC/OIC_ASSUMPTIONS_V1.md | RESOLVED |
| AMS-ASSUMPTIONS-V1 | AMS/AMS_ASSUMPTIONS_V1.md | RESOLVED |
| HCM-BASE-ASSUMPTIONS-V1 | HCM/HCM_BASE_ASSUMPTIONS_V1.md | RESOLVED |
| HCM-RECRUITING-ASSUMPTIONS-V1 | HCM/HCM_RECRUITING_ASSUMPTIONS_V1.md | RESOLVED |
| HCM-LEARNING-ASSUMPTIONS-V1 | HCM/HCM_LEARNING_ASSUMPTIONS_V1.md | RESOLVED |
| HCM-TALENT-ASSUMPTIONS-V1 | HCM/HCM_TALENT_ASSUMPTIONS_V1.md | RESOLVED |
| HCM-COMPENSATION-ASSUMPTIONS-V1 | HCM/HCM_COMPENSATION_ASSUMPTIONS_V1.md | RESOLVED |
| EBS-AMS-SLA-OVERLAY-V1 | AMS/EBS_AMS_SLA_OVERLAY_V1.md | RESOLVED |
| EBS-DRM-ASSUMPTIONS-V1 | AMS/EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md | RESOLVED |
| ACU-BASE-ASSUMPTIONS-V1 | Acumatica/ACU_BASE_ASSUMPTIONS_V1.md | RESOLVED |
| BEBANKING-BASE-ASSUMPTIONS-V1 | BeBanking/BEBANKING_BASE_ASSUMPTIONS_V1.md | RESOLVED |
| ERP-ASSUMPTIONS-V1 | ERP/ERP_ASSUMPTIONS_V1.md | RESOLVED |
| OCI-ASSUMPTIONS-V1 | OCI/OCI_ASSUMPTIONS_V1.md | RESOLVED |

---

## 7. Full Pipeline Validation

| Step | Tool | Result |
|---|---|---|
| Registry rebuild | krpe.py | SUCCESS — 213 core / 1,136 ASM |
| KVE health check | kve_engine.py --mode health | KHS 91/100 EXCELLENT |
| PSAE regression | proposal_section_engine.py --regression | 6/6 PASS |
| Renderer regression | proposal_renderer.py --regression | **6/6 PASS / NOT_FOUND=0** |

---

## 8. Post-Condition: Regression Results

| Tender | Status | RENDERED | PLACEHOLDER | AI-DRAFT | NOT_FOUND |
|---|---|---|---|---|---|
| ARM-IT045 | PASS | 25 | 17 | 3 | **0** |
| REG-HCM-P3-MINING | PASS | 21 | 18 | 3 | **0** |
| REG-OIC-P7 | PASS | 20 | 18 | 3 | **0** |
| REG-ERP-P7-FULLSUITE | PASS | 21 | 18 | 4 | **0** |
| REG-ACU-P11 | PASS | 23 | 18 | 3 | **0** |
| REG-BEB-P12 | PASS | 19 | 18 | 3 | **0** |

ARM-IT045 RENDERED count improved from 16 (PF2-004) to **25** (+9 assumption packs resolved).
ARM-IT045 rendered output: **7,347 lines** (was 3,537 — growth reflects assumption pack content now included).

---

## 9. Governance Compliance

- No new files created in `07_Approved_Content/` — all ASP sources remain in `08_Commercial/Assumptions/`
- No registry entries modified — existing 13 ASP entries unchanged
- No PSAE logic modified — manifests regenerated deterministically
- `document_id` in frontmatter is the single authoritative identifier — no duplicates
- All 13 ASP files carry `lifecycle_status: APPROVED` and `approved_for_reuse: true`
- Renderer change is additive only — backward-compatible with all existing tenders

---

*Generated by PF2-005 — Assumption Library Materialisation | 2026-06-30*
