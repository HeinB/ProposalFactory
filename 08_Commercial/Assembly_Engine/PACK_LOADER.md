---
document_id: ENGINE-PACK-LOADER
title: "Assembly Engine — Pack Loader"
version: "1.0"
created: "2026-06-19"
created_by: "WP17B — Assembly Engine Core (MVP)"
status: "Active"
component: "Step 2 of 5 — see ENGINE_ORCHESTRATOR.md"
---

# Assembly Engine — Pack Loader

**Purpose:** Validates each pack in the BOM_RESOLVER manifest, confirms Approved status, records version and assumption count, and establishes load order for RULE_PROCESSOR.md.

**Inputs:** Pack Manifest from BOM_RESOLVER.md  
**Outputs:** Loaded Pack Registry → passed to RULE_PROCESSOR.md  
**Authority:** `08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md` (v1.9)

---

## Assumption Pack Registry — V1 Library (Current)

All approved packs as of 2026-06-19. This registry is the authoritative source for pack metadata.

### Base and Module Packs

| Pack Name | File Path | Version | Status | Assumption Count | Load Order | Notes |
|---|---|---|---|---|---|---|
| HCM Base | `08_Commercial/Assumptions/HCM/HCM_BASE_ASSUMPTIONS_V1.md` | 1.1 | Approved | 115 | 1 | HCM track base — always loads first for HCM engagements |
| HCM Recruiting | `08_Commercial/Assumptions/HCM/HCM_RECRUITING_ASSUMPTIONS_V1.md` | 1.1 | Approved (WP16C) | 54 | 2 | Requires HCM Base (Rule A); IDs: REC-XXX- prefix |
| HCM Learning | `08_Commercial/Assumptions/HCM/HCM_LEARNING_ASSUMPTIONS_V1.md` | 1.1 | Approved (WP16C) | 37 | 2 | Requires HCM Base (Rule A); IDs: LRN-XXX- prefix |
| HCM Talent | `08_Commercial/Assumptions/HCM/HCM_TALENT_ASSUMPTIONS_V1.md` | 1.1 | Approved (WP16C) | 31 | 2 | Requires HCM Base (Rule A); IDs: TLT-XXX- prefix |
| HCM Compensation | `08_Commercial/Assumptions/HCM/HCM_COMPENSATION_ASSUMPTIONS_V1.md` | 1.1 | Approved (WP16C) | 30 | 2 | Requires HCM Base (Rule A); IDs: COM-XXX- prefix |
| ERP Pack | `08_Commercial/Assumptions/ERP/ERP_ASSUMPTIONS_V1.md` | 1.0 | Approved | 123 | 1 | ERP track base — standalone, no HCM Base dependency |
| OCI Pack | `08_Commercial/Assumptions/OCI/OCI_ASSUMPTIONS_V1.md` | 1.0 | Approved | 174 | 3 | Loads after base packs; triggered by Rule OCI-1 |
| OIC Pack | `08_Commercial/Assumptions/OIC/OIC_ASSUMPTIONS_V1.md` | 1.0 | Approved | 104 | 2 | Standalone; stacks with HCM Base, ERP, or BeBanking |
| AMS Pack | `08_Commercial/Assumptions/AMS/AMS_ASSUMPTIONS_V1.md` | 1.0 | Approved | 84 | 4 | Loads after all base packs — always last of base packs |
| Acumatica Base | `08_Commercial/Assumptions/Acumatica/ACU_BASE_ASSUMPTIONS_V1.md` | 1.0 | Approved (WP15C) | 152 | 1 | Acumatica track only; IDs: ACU-XXX- prefix |
| BeBanking Base | `08_Commercial/Assumptions/BeBanking/BEBANKING_BASE_ASSUMPTIONS_V1.md` | 1.0 | Approved (WP14F) | 117 | 1 | BeBanking track only; IDs: BB-XXX- prefix |

### Overlay Packs

| Pack Name | File Path | Version | Status | Assumption Count | Load Order | Notes |
|---|---|---|---|---|---|---|
| EBS SLA Overlay | `08_Commercial/Assumptions/AMS/EBS_AMS_SLA_OVERLAY_V1.md` | 1.0 | Approved (WP15F) | 53 | 5 | Loads after AMS Pack; REPLACES AMS-SLA-001, AMS-PRI-001/002/003, AMS-SLA-005 where specified |
| EBS DRM Overlay | `08_Commercial/Assumptions/AMS/EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md` | 1.0 | Approved (WP15F) | 62 | 6 | Loads last; takes precedence over SLA Overlay where both address same topic |

### Load Order Rules

Load order governs the sequence in which packs are passed to RULE_PROCESSOR:

1. **Base packs first** — HCM Base or ERP Pack or Acumatica Base or BeBanking Base
2. **Module packs second** — HCM Recruiting, Learning, Talent, Compensation (additive only)
3. **Infrastructure packs third** — OCI Pack (Rule OCI-1)
4. **Service packs fourth** — OIC Pack, AMS Pack
5. **Overlay packs last** — EBS SLA Overlay, then EBS DRM Overlay

Where both SLA Overlay and DRM Overlay are loaded: DRM Overlay takes precedence on any overlapping topics (DRM assumptions are more specific).

---

## Eligibility Check

Before loading any pack, verify:

| Check | Pass Condition | Fail Action |
|---|---|---|
| Status is Approved | `status: "Approved"` or `"Approved v1.0"` in frontmatter | Do not load; record ASSEMBLY GAP in audit log |
| File exists at registered path | File readable at path in registry | Record PATH ERROR in audit log; halt assembly |
| Assumption count matches registry | `assumption_count` in frontmatter = registry value | Record COUNT DISCREPANCY in audit log; proceed with caution flag |
| Version matches registry | `version` in frontmatter = registry value | Record VERSION MISMATCH in audit log |

---

## Loaded Pack Registry Format

PACK_LOADER produces a **Loaded Pack Registry** for RULE_PROCESSOR:

```
LOADED PACK REGISTRY
Tender: [Tender ID]
Load Date: [YYYY-MM-DD]
Total packs loaded: [N]
Total raw assumptions: [sum of assumption counts]

LOADED PACKS (in load order):
Order | Pack Name           | Version | Assumptions | File Path
------|---------------------|---------|-------------|----------
1     | [Pack name]         | [ver]   | [count]     | [path]
...

PACKS NOT LOADED (eligibility failures):
- [Pack name] — Reason: [Draft/Path Error/etc.]

SUPPRESSION CANDIDATES (identified for RULE_PROCESSOR):
- [Assumption ID] — Reason: [suppression rule — see RULE_PROCESSOR.md]
```

---

*PACK_LOADER v1.1 | WP17C — Regression Test Suite 2026-06-22 | HCM module + Acumatica + BeBanking counts confirmed; version fields corrected*
