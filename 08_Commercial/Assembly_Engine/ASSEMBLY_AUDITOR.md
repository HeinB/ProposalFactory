---
document_id: ENGINE-ASSEMBLY-AUDITOR
title: "Assembly Engine — Assembly Auditor"
version: "1.0"
created: "2026-06-19"
created_by: "WP17B — Assembly Engine Core (MVP)"
status: "Active"
component: "Step 5 of 5 — see ENGINE_ORCHESTRATOR.md"
---

# Assembly Engine — Assembly Auditor

**Purpose:** Generates the ASSEMBLY_AUDIT_REPORT.md — a complete decision trail covering every BOM resolution, pack eligibility check, rule application, suppression, and count verification. Enables post-assembly review and identifies gaps requiring BU Lead action before submission.

**Inputs:** All step outputs (BOM manifest, loaded pack registry, rule-processed manifest, assembled schedule)  
**Outputs:** ASSEMBLY_AUDIT_REPORT.md in the tender workspace  
**Authority:** `08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md` (v1.9)

---

## What to Record at Each Step

### Step 1 — BOM Resolution (from BOM_RESOLVER)

Record for each BOM item processed:
- BOM code or engagement characteristic presented
- Classification decision (engagement type)
- Pack(s) triggered
- Assembly pattern matched
- Any exclusions applied at classification stage

### Step 2 — Pack Loading (from PACK_LOADER)

Record for each pack in the manifest:
- Pack name and registered path
- Eligibility check result (Pass/Fail)
- Status confirmed (Approved / Draft / etc.)
- Version confirmed
- Assumption count confirmed
- Load order position
- Any path errors or count discrepancies

### Step 3 — Rule Processing (from RULE_PROCESSOR)

Record for each rule applied:
- Rule code and name
- Assumptions affected (IDs)
- Action taken (suppressed / replaced / flagged)
- Reason
- BU Lead action required (Yes/No)

### Step 4 — Extraction and Count Verification (from ASSUMPTION_EXTRACTOR)

Record for each pack extracted:
- Pack name
- Assumptions extracted
- Assumptions suppressed
- Net assumptions
- Running total

Record at schedule level:
- Total raw assumptions (sum of all packs as loaded)
- Total suppressed
- Total net (included in ASSEMBLED_ASSUMPTION_SCHEDULE.md)

### Step 5 — Gap Assessment

Compare the assembled schedule against known tender requirements (if a prior gap analysis exists):
- Identify which WP14C gaps are now resolved vs. still outstanding
- Flag any tender requirements with no assumption coverage
- Record escalation items for BU Lead

---

## ASSEMBLY_AUDIT_REPORT.md Structure

```markdown
# Assembly Audit Report
**Tender:** [Tender ID — Client — Date]
**Assembly Pattern:** [Named pattern]
**Assembled:** [YYYY-MM-DD]
**Auditor:** Assembly Engine MVP v1.0 (WP17B)

---

## 1. Tender Profile Summary

[Engagement type, key characteristics, triggers identified]

---

## 2. BOM Resolution Log

| Input | Classification | Packs Triggered | Pattern | Notes |
|---|---|---|---|---|

---

## 3. Pack Loading Log

| # | Pack | Path | Status Check | Version | Count | Load Result |
|---|---|---|---|---|---|---|

**Total packs loaded:** [N]  
**Total raw assumptions:** [sum]

---

## 4. Rule Processing Log

| Rule | Assumptions Affected | Action | BU Lead Required |
|---|---|---|---|

**Total suppressions:** [N]  
**Total replacements:** [N]  
**BU Lead actions required:** [N]

---

## 5. Count Verification

| Pack | Loaded | Suppressed | Net |
|---|---|---|---|
| [Pack name] | [N] | [N] | [N] |
| **TOTAL** | **[sum]** | **[sum]** | **[net]** |

---

## 6. Gap Assessment

| Requirement | Coverage Status | Source | Gap vs Prior Analysis |
|---|---|---|---|
| [Requirement] | Covered / Partial / Not Covered | [Assumption ID or "None"] | [Resolved / New gap / Unchanged] |

**Summary:** [N] Covered / [N] Partial / [N] Not Covered

---

## 7. Escalation Register

Items requiring BU Lead action before submission:

| # | Item | Type | Priority |
|---|---|---|---|

---

## 8. Assembly Verdict

**Verdict:** [COMPLETE — ready for proposal insertion] OR [CONDITIONAL — items require BU Lead action] OR [INCOMPLETE — gaps prevent submission]

[1–2 sentences on assembly outcome and any pre-submission requirements]
```

---

## Audit Integrity Rules

- Every suppression must have a corresponding rule code citation
- Every gap must reference the tender requirement it fails to meet
- Count verification must balance: loaded total = sum of all pack assumption_counts
- Net total = loaded total minus suppressed total
- No assumption may appear twice in the schedule (Rule C enforcement)
- All BU Lead actions must be listed even where they are non-blocking

---

*ASSEMBLY_AUDITOR v1.0 | WP17B — Assembly Engine Core (MVP) | 2026-06-19*
