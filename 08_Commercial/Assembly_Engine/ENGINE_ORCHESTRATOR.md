---
document_id: ENGINE-ORCHESTRATOR
title: "Assembly Engine — Orchestrator"
version: "1.0"
created: "2026-06-19"
created_by: "WP17B — Assembly Engine Core (MVP)"
status: "Active"
component: "Entry point — invokes BOM_RESOLVER → PACK_LOADER → RULE_PROCESSOR → ASSUMPTION_EXTRACTOR → ASSEMBLY_AUDITOR"
---

# Assembly Engine — Orchestrator

**Purpose:** End-to-end workflow for executing a full assumption assembly. The Orchestrator is the entry point. It sequences the 5 engine components, passes outputs between them, and produces the two deliverables: ASSEMBLED_ASSUMPTION_SCHEDULE.md and ASSEMBLY_AUDIT_REPORT.md.

**Scope:** Assumption assembly only. The engine does NOT generate proposal responses, score sections, or populate proposal templates. It produces the governed assumption set that bid teams insert into proposals.

---

## Required Inputs

Before running the engine, the following must be available:

| Input | Source | Notes |
|---|---|---|
| Tender Profile | Bid manager / tender document | Engagement type, systems in scope, infrastructure, model flags |
| BOM Selections | Opportunity record or BOM worksheet | Oracle/Acumatica/BeBanking line items in scope |
| Tender workspace path | Bid manager | Where to write output files |
| Tender ID | Bid manager | Used in file headers and audit log |

---

## Execution Steps

### Step 1 — Capture Tender Profile

Document the tender profile before running any engine component:

```
Tender Profile:
  Tender ID:          [e.g., ARM IT045]
  Client:             [e.g., African Rainbow Minerals]
  Engagement type:    [Implementation / AMS / Infrastructure / Integration / Mixed]
  Systems in scope:   [e.g., Oracle EBS HR v12.2.8, EBS Financials v12.2.10]
  Infrastructure:     [On-premises / OCI / Hybrid]
  OIC in scope:       [Yes / No]
  AMS model:          [Pooled / Dedicated Resource Model]
  SLA tier:           [Standard (4-tier) / Enhanced (5-tier with P1<1hr + resolution times)]
  24/7 coverage:      [Yes / No]
  Sector:             [e.g., Mining / Financial Services / Public Sector / Other]
  BOM items:          [List from opportunity record]
```

---

### Step 2 — Run BOM_RESOLVER

**Component:** `08_Commercial/Assembly_Engine/BOM_RESOLVER.md`

1. Apply the engagement type classification (BOM_RESOLVER Step 1)
2. Map each BOM line item to packs (BOM_RESOLVER Step 2)
3. Check AMS overlay triggers if AMS engagement (BOM_RESOLVER Step 2 — overlay section)
4. Apply mandatory exclusion checks (BOM_RESOLVER Step 3)
5. Identify named assembly pattern (BOM_RESOLVER Step 4)
6. Produce Pack Manifest

**Gate:** If no Approved pack is triggered for any item, halt and raise ASSEMBLY_ERROR.

---

### Step 3 — Run PACK_LOADER

**Component:** `08_Commercial/Assembly_Engine/PACK_LOADER.md`

1. For each pack in the manifest, run eligibility check (PACK_LOADER Eligibility Check table)
2. Verify file path, status, version, and assumption count against registry
3. Reject Draft packs (record ASSEMBLY GAP)
4. Order packs by load order
5. Produce Loaded Pack Registry with running assumption total

**Gate:** If any required pack fails eligibility, record ASSEMBLY GAP — assembly may proceed conditionally if optional packs fail, but must halt if a primary pack (ERP, HCM Base, AMS) fails.

---

### Step 4 — Run RULE_PROCESSOR

**Component:** `08_Commercial/Assembly_Engine/RULE_PROCESSOR.md`

1. Validate Rule A compliance (base before module)
2. Apply all suppression rules in order: S1 (AMS-INC-004), S2 (SLA replacements), S3 (AMS-SLA-005), S4 (overlay precedence)
3. Apply conflict resolution rules
4. Flag any BU_LEAD_REQUIRED items
5. Produce Rule-Processed Manifest with suppression log

**Gate:** BU_LEAD_REQUIRED flags do not halt assembly — they are recorded in the audit log and escalation register. Assembly continues.

---

### Step 5 — Run ASSUMPTION_EXTRACTOR

**Component:** `08_Commercial/Assembly_Engine/ASSUMPTION_EXTRACTOR.md`

1. For each pack in load order, extract active assumptions (skipping suppressed IDs)
2. Handle replacement annotations — extract text, record mapping
3. Separate -EXC- assumptions into Explicit Exclusions section
4. Separate -CUS- and -CON- assumptions into Customer Responsibilities section
5. Verify no duplication across packs (Rule C)
6. Produce ASSEMBLED_ASSUMPTION_SCHEDULE.md in the tender workspace

**Output file:** `[tender workspace]/ASSEMBLED_ASSUMPTION_SCHEDULE.md`

---

### Step 6 — Run ASSEMBLY_AUDITOR

**Component:** `08_Commercial/Assembly_Engine/ASSEMBLY_AUDITOR.md`

1. Compile all step outputs into ASSEMBLY_AUDIT_REPORT.md
2. Verify count balances: loaded total − suppressed = net total in schedule
3. Run gap assessment if a prior gap analysis exists
4. Populate escalation register
5. Record assembly verdict

**Output file:** `[tender workspace]/ASSEMBLY_AUDIT_REPORT.md`

---

## Output Files

| File | Location | Purpose |
|---|---|---|
| ASSEMBLED_ASSUMPTION_SCHEDULE.md | Tender workspace | The governed assumption set — insert into proposal |
| ASSEMBLY_AUDIT_REPORT.md | Tender workspace | Decision trail — internal use; accompanies tender file |

The Assembled Assumption Schedule is the only engine output that enters an external proposal. The Audit Report is internal documentation.

---

## Tender Workspace Convention

Store assembly outputs in the relevant tender folder:

```
09_Active_Tenders/[Client]/[Tender ID]/
  └── Assembly/
        ├── ASSEMBLED_ASSUMPTION_SCHEDULE.md
        └── ASSEMBLY_AUDIT_REPORT.md

08_Historical_Tenders/Won|Lost|Submitted/[Client]/[Tender ID]/
  └── Assembly/
        ├── ASSEMBLED_ASSUMPTION_SCHEDULE.md
        └── ASSEMBLY_AUDIT_REPORT.md
```

For dry-run and testing:
```
08_Commercial/Assembly_Engine/Dry_Run/[Tender ID]/
  ├── ASSEMBLED_ASSUMPTION_SCHEDULE.md
  └── ASSEMBLY_AUDIT_REPORT.md
```

---

## Pre-Submission Checklist

Before inserting the assembled schedule into a live proposal, verify:

| Check | Verify |
|---|---|
| B-BBEE certificate current | Not expired (current cert expires 2026-07-31) |
| No Oracle Gold Partner references | Expired August 2021 — never cite |
| AMS-INC-004 suppressed for EBS engagements | Required for all EBS AMS proposals |
| Escalation register cleared | All BU Lead items resolved or formally accepted |
| Suppression register reviewed by BU Lead | BU Lead signs off on suppressions |
| Section 14.2 (W3S1-008) not in submission | Permanent governance restriction PT-W8-007 |
| Section 13.2 (W3S1-009) not in submission | Permanent governance restriction PT-W9-008 |
| No DFA, CCBA, or SAA references | Rule 21.4 — permanent |

---

## Version History

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-06-19 | Initial — WP17B Assembly Engine MVP |

---

*ENGINE_ORCHESTRATOR v1.0 | WP17B — Assembly Engine Core (MVP) | 2026-06-19*
