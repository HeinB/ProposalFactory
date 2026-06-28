---
document_id: ENGINE-BOM-RESOLVER
title: "Assembly Engine — BOM Resolver"
version: "1.0"
created: "2026-06-19"
created_by: "WP17B — Assembly Engine Core (MVP)"
status: "Active"
component: "Step 1 of 5 — see ENGINE_ORCHESTRATOR.md"
---

# Assembly Engine — BOM Resolver

**Purpose:** Translates tender profile inputs (engagement type + BOM line items + engagement characteristics) into an ordered list of assumption packs for PACK_LOADER.md.

**Inputs:** Tender Profile (engagement type, systems in scope, infrastructure, model flags)  
**Outputs:** Ordered pack list → passed to PACK_LOADER.md  
**Authority:** `08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md` (v1.9)

---

## Step 1 — Classify Engagement Type

Before resolving BOM codes, classify the engagement. Engagement type drives pack selection more than individual BOM codes.

| Engagement Type | Classification Rule | Primary Pack |
|---|---|---|
| Oracle HCM Implementation | HCM BOM codes present (B85800, B87675, B85242, B94925, B109620, etc.) | HCM Base |
| Oracle ERP / Fusion Financials | B86481 or B86482 or B86483 present | ERP Pack (standalone) |
| Oracle EBS Implementation/Migration | "EBS" or "R12" in scope description | ERP Pack (standalone) |
| Oracle AMS / Managed Services | Engagement type = AMS or Managed Services | AMS Pack (mandatory) |
| Oracle OCI Infrastructure | OCI workloads in scope | OCI Pack (via Rule OCI-1) |
| Oracle OIC Integration | OIC or integrations in scope | OIC Pack |
| Acumatica | Acumatica BOM codes present | Acumatica Base |
| BeBanking | BeBanking services in scope | BeBanking Base |

---

## Step 2 — BOM Code to Pack Mapping

### Oracle BOM Line Items

| BOM Code | Description | Pack Triggered | Notes |
|---|---|---|---|
| B85800 | Oracle Fusion HCM Base Cloud Service | HCM Base (mandatory) | Includes Core HR, Absence, Benefits, Journeys, Payroll Interface, AI Skills |
| B87675 | Oracle Fusion Recruiting Cloud Service | HCM Base + Recruiting Pack | HCM Base is prerequisite |
| B85242 | Oracle Fusion Learning Cloud Service | HCM Base + Learning Pack | HCM Base is prerequisite |
| B94925 | Oracle Fusion Talent Management Cloud Service | HCM Base + Talent Pack | HCM Base is prerequisite |
| B109620 | Oracle Fusion Workforce Compensation Cloud Service | HCM Base + Compensation Pack | HCM Base is prerequisite |
| B95763 | Oracle Fusion Recruiting Booster Cloud Service | HCM Base + Recruiting Pack | Booster extends Recruiting; same pack |
| B87388 | Oracle Fusion HR Help Desk Cloud Service | HCM Base + Help Desk Pack | Help Desk pack = FUTURE (not yet approved) |
| B86481 | Oracle Fusion Financials Cloud Service | ERP Pack (standalone) | No HCM Base dependency |
| B86482 | Oracle Fusion Procurement Cloud Service | ERP Pack (standalone) | Procurement is within ERP pack scope |
| B86483 | Oracle Fusion PPM Cloud Service | ERP Pack (standalone) | PPM is within ERP pack scope |
| B91110 | Oracle Integration Cloud Enterprise | OIC Pack | Standalone; stacks with HCM Base, ERP, or BeBanking |
| (OCI) | OCI Infrastructure / OCI Tenancy | OCI Pack via Rule OCI-1 | No single BOM code; triggered by OCI presence in scope |
| (EBS) | Oracle EBS R11/R12 (on-premise or OCI-hosted) | ERP Pack (standalone) | EBS HR/Payroll support = ERP Pack scope; do NOT add HCM Base |
| (AMS) | Managed Services / AMS engagement | AMS Pack (mandatory) | No BOM code; triggered by engagement type |

### AMS Engagement Overlay Triggers

These overlays apply ON TOP of the standard AMS assembly when engagement characteristics match:

| Characteristic | Overlay Triggered | Trigger Condition |
|---|---|---|
| Enhanced SLA (P1 < 1hr, resolution times, 24/7, 5-tier) | EBS SLA Overlay | Any of: P1 response < 1 hour; resolution time commitments; 5-tier (P1–P5); 24/7 coverage |
| Dedicated Resource Model | EBS DRM Overlay | Any of: named consultants by role; minimum monthly hours per role; ring-fenced (non-pooled) allocation; dedicated SDM requirement |

### Rule OCI-1 — Mandatory OCI Pack Trigger

The OCI Pack is mandatory whenever OCI infrastructure is in scope. Trigger conditions:

| Condition | OCI Pack Required |
|---|---|
| EBS hosted on OCI | Yes |
| Oracle Fusion (HCM/ERP) on OCI | Yes |
| OIC hosted on OCI | Yes |
| BeBanking OCI workloads | Yes |
| AMS-managed OCI services | Yes |
| OCI infrastructure engagement (standalone) | Yes |
| On-premises only engagement (no OCI) | No |

---

## Step 3 — Mandatory Exclusion Checks

Apply before finalising the pack list:

| Exclusion Rule | Condition | Action |
|---|---|---|
| HCM Base excluded for EBS | Engagement type = EBS AMS or EBS support | Remove HCM Base from pack list if present; EBS HR/Payroll ≠ Oracle Fusion HCM |
| Implementation packs excluded for support | Engagement type = AMS / Managed Services only | Exclude implementation-phase packs not applicable to support context |
| Draft packs not loadable | Pack status = Draft | Do not include; record as ASSEMBLY GAP in audit log |
| Retired packs not loadable | Pack status = Retired | Do not include; record in audit log |

---

## Step 4 — Resolve Assembly Pattern

After applying BOM mapping and exclusion checks, match to a named assembly pattern from TENDER_ASSUMPTION_ASSEMBLY_RULES.md Section 3:

| Pattern Name | Packs Included |
|---|---|
| HCM Core Only | HCM Base |
| HCM + Module(s) | HCM Base + relevant module pack(s) |
| HCM + OIC | HCM Base + (module packs) + OIC Pack |
| HCM + OIC + OCI | HCM Base + (module packs) + OIC Pack + OCI Pack |
| ERP Standalone | ERP Pack |
| ERP + OIC | ERP Pack + OIC Pack |
| ERP + OCI | ERP Pack + OCI Pack |
| ERP + OCI + OIC | ERP Pack + OCI Pack + OIC Pack |
| EBS AMS Standard | AMS Pack + ERP Pack + OCI Pack (if EBS on OCI) + OIC Pack (if OIC in scope) |
| EBS AMS Enhanced SLA | AMS Pack + ERP Pack + OCI Pack + OIC Pack + EBS SLA Overlay |
| EBS AMS Dedicated Resource | AMS Pack + ERP Pack + OCI Pack + OIC Pack + EBS DRM Overlay |
| **EBS AMS Full Stack** | **AMS Pack + ERP Pack + OCI Pack + OIC Pack + EBS SLA Overlay + EBS DRM Overlay** |
| Acumatica Standard | Acumatica Base |
| BeBanking Standard | BeBanking Base |

---

## Output Format

BOM_RESOLVER produces a **Pack Manifest** for PACK_LOADER:

```
PACK MANIFEST
Tender: [Tender ID]
Pattern: [Named pattern from table above]
Assembly Date: [YYYY-MM-DD]

PACKS TO LOAD (in load order):
1. [Pack name] | [File path] | [Status]
2. [Pack name] | [File path] | [Status]
...

PACKS EXCLUDED:
- [Pack name] — Reason: [exclusion rule applied]

OVERLAYS TO LOAD (after base packs):
1. [Overlay name] | [Trigger] | [File path]
```

---

*BOM_RESOLVER v1.0 | WP17B — Assembly Engine Core (MVP) | 2026-06-19*
