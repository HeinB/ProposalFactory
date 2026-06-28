---
document_id: ENGINE-RULE-PROCESSOR
title: "Assembly Engine — Rule Processor"
version: "1.0"
created: "2026-06-19"
created_by: "WP17B — Assembly Engine Core (MVP)"
status: "Active"
component: "Step 3 of 5 — see ENGINE_ORCHESTRATOR.md"
---

# Assembly Engine — Rule Processor

**Purpose:** Applies all assembly rules to the Loaded Pack Registry, resolving suppressions, replacements, conflict handling, and overlay precedence. Produces a clean assumption list for ASSUMPTION_EXTRACTOR.md.

**Inputs:** Loaded Pack Registry from PACK_LOADER.md  
**Outputs:** Rule-processed assumption manifest → passed to ASSUMPTION_EXTRACTOR.md  
**Authority:** `08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md` (v1.9)

---

## Rule Set — Assembly Rules

### Rule A — Base First

The relevant base pack always loads before any module pack. Module packs are never assembled without their parent base pack. Applied by PACK_LOADER load order; RULE_PROCESSOR validates compliance.

**Validation check:** If any module pack is in the loaded list without its parent base, flag RULE_A_VIOLATION and halt.

---

### Rule B — Additive Only

Module packs add new assumptions. They do not override base pack assumptions. If a base assumption is inapplicable to a specific tender, a BU Lead override is required.

**Validation check:** No module assumption should duplicate a base assumption ID. If duplication detected, apply Rule C.

---

### Rule C — No Duplication

Where a base assumption and a module assumption address the same topic, the module assumption takes precedence and the base assumption is suppressed for that topic only.

**Action:** Record suppression in the suppression log with assumption ID, reason, and authority.

---

### Rule D — BOM Trigger Mapping

Assembly triggers derive from the tender profile BOM items. No assumption pack is loaded without a BOM trigger. Validated by BOM_RESOLVER — RULE_PROCESSOR confirms the loaded registry matches the BOM manifest.

---

### Rule E — Exclusions Always Included

Explicit Exclusion sections (IDs ending in -EXC-XXX) are always included in full. Exclusions must never be omitted from a proposal.

---

## Suppression Rules

### S1 — AMS-INC-004 (EBS AMS engagements)

| Condition | Action | Replacement |
|---|---|---|
| Engagement type = EBS AMS (any variant) | Suppress AMS-INC-004 | EBS-DRM-013 (from DRM Overlay) provides the correct EBS infrastructure statement |

**AMS-INC-004 states:** "Oracle Fusion HCM and ERP are delivered on Oracle's SaaS infrastructure." This is factually incorrect for EBS AMS engagements where EBS runs on client-managed OCI infrastructure.

**Suppression log entry:** `SUPPRESSED: AMS-INC-004 | Rule: S1 — EBS AMS engagement | Replaced by: EBS-DRM-013`

---

### S2 — AMS SLA Assumptions (when EBS SLA Overlay loaded)

When the EBS SLA Overlay is in the loaded pack list, the following AMS Pack assumptions are superseded:

| AMS Assumption Suppressed | Replaced By | Notes |
|---|---|---|
| AMS-SLA-001 | EBS-SLA-002 | EBS overlay defines EBS-specific SLA structure |
| AMS-PRI-001 | EBS-SLA-004 + EBS-SLA-011 | 5-tier priority classification replaces 4-tier |
| AMS-PRI-002 | EBS-SLA-005 through EBS-SLA-009 | Per-tier response targets replaced |
| AMS-PRI-003 | EBS-SLA-012 | 24/7 operational model assumption replaces general coverage note |

Record each suppression individually in the suppression log.

---

### S3 — AMS-SLA-005 (when EBS DRM Overlay loaded)

| Condition | Action | Replacement |
|---|---|---|
| EBS DRM Overlay in loaded pack list | Suppress AMS-SLA-005 | EBS-DRM-001 replaces the named consultant assumption |

---

### S4 — Overlay Precedence (both SLA and DRM Overlay loaded)

Where both EBS SLA Overlay and EBS DRM Overlay are loaded and assumptions overlap on the same topic:
1. DRM Overlay assumption takes precedence (more specific)
2. SLA Overlay assumption is suppressed on that topic

Topics where DRM Overlay supersedes SLA Overlay:
- Role-specific SLA commitments (DRM specifies per-role response obligations)
- Named resource SLA accountability (DRM assumption is more specific than generic SLA)

---

## Conflict Resolution Rules

| Conflict Type | Resolution |
|---|---|
| Module assumption more specific than base assumption | Use module assumption; suppress base for that topic |
| Module assumption contradicts base assumption | Flag BU_LEAD_REQUIRED; do not suppress either; surface in audit report |
| Base assumption inapplicable to specific module context | Apply BU Lead override if on file; else flag for manual review |
| Overlay assumption replaces base assumption | Apply replacement; log in suppression log with replacement ID |

---

## Rule Processor Output Format

RULE_PROCESSOR produces a **Rule-Processed Manifest** for ASSUMPTION_EXTRACTOR:

```
RULE-PROCESSED MANIFEST
Tender: [Tender ID]
Rule Processing Date: [YYYY-MM-DD]

ACTIVE ASSUMPTIONS:
Pack: [Pack name] | [N] assumptions active (of [total] loaded)
- [Assumption ID] — ACTIVE
...

SUPPRESSION LOG:
- [Assumption ID] | Rule: [rule code] | Replaced by: [ID or N/A] | Reason: [text]

CONFLICT FLAGS (require BU Lead before submission):
- [Description if any — else: None]

REPLACEMENT MAPPINGS APPLIED:
- [Source ID] → [Replacement ID]

NET ASSUMPTION COUNT: [total active after suppressions]
```

---

*RULE_PROCESSOR v1.0 | WP17B — Assembly Engine Core (MVP) | 2026-06-19*
