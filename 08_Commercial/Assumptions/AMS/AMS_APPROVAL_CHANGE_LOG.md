---
document_id: AMS-APPROVAL-CHANGE-LOG
title: "AMS Assumptions — Approval Change Log (WP11E-A)"
version: "1.0"
created: "2026-06-15"
created_by: "WP11E-A — AMS Assumptions Approval"
status: "Final"
applies_to: "AMS_ASSUMPTIONS_V1.md"
---

# AMS Assumptions — Approval Change Log

This change log records all changes applied to `AMS_ASSUMPTIONS_V1.md` during the WP11E-A approval cycle. Changes implement the seven BU Lead decisions (BU-AMS-001 through BU-AMS-007) that promoted the AMS pack from Draft to Approved v1.0 on 2026-06-15.

---

## Change Summary

| Change ID | Item | Assumption(s) Updated | BU Decision | Date |
|---|---|---|---|---|
| CL-AMS-001 | Pack status promoted to Approved | Frontmatter + governance note | All 7 BU-AMS items closed | 2026-06-15 |
| CL-AMS-002 | SLA response targets defined | AMS-SLA-001 | BU-AMS-001 | 2026-06-15 |
| CL-AMS-003 | Priority definitions updated with response targets | AMS-PRI-001 | BU-AMS-001 | 2026-06-15 |
| CL-AMS-004 | Support hours confirmed | AMS-HRS-001 | BU-AMS-002 | 2026-06-15 |
| CL-AMS-005 | Monthly hours model updated | AMS-HRS-003 | BU-AMS-003 | 2026-06-15 |
| CL-AMS-006 | CR threshold set at 2 hours | AMS-CR-001 | BU-AMS-004 | 2026-06-15 |
| CL-AMS-007 | Release advisory confirmed; regression testing excluded | AMS-REL-001 | BU-AMS-005 | 2026-06-15 |
| CL-AMS-008 | Named consultant not included; best-effort team confirmed | AMS-SLA-005 | BU-AMS-006 | 2026-06-15 |
| CL-AMS-009 | Monitoring scope defined; mailbox-only as standard | AMS-MON-001 | BU-AMS-007 | 2026-06-15 |
| CL-AMS-010 | Register updated — all 96 rows to Active | AMS_ASSUMPTION_REGISTER.csv | All BU-AMS items | 2026-06-15 |

---

## Detailed Change Records

### CL-AMS-001 — Pack Status Promoted to Approved

**Change type:** Status promotion  
**Assumptions affected:** Frontmatter, governance note, footer, BU Lead decisions table  
**BU decision:** All 7 BU-AMS items closed by BU Lead — Oracle Practice (Cross-BU)

**Before:**
```
status: "Draft — Pending BU Lead Approval"
approved_by: ""
approved_date: ""
approved_for_reuse: false
bu_lead_review_items: [7 open items]
Governance note: Draft — Not for use in external AMS proposals
```

**After:**
```
status: "Approved"
approved_by: "BU Lead — Oracle Practice (Cross-BU)"
approved_date: "2026-06-15"
approved_for_reuse: true
bu_lead_decisions_applied: [7 closed items]
Governance note: Approved — 2026-06-15. All BU-AMS-XXX items closed.
```

**Commercial reason:** AMS pack is the final Cross-BU pack in the WP11 library v1.0. Approval enables inclusion in all AMS proposals and SOWs across Oracle, Acumatica, and BeBanking tracks. Pack was the only gap preventing a complete library covering all AMS engagements.

---

### CL-AMS-002 — SLA Response Targets Defined (AMS-SLA-001)

**BU decision:** BU-AMS-001  
**Assumption:** AMS-SLA-001

**Before:**
```
AMS-SLA-001 *(Pending BU-AMS-001)*
APPSolve's standard AMS SLA defines response time targets per priority level. [No targets specified.]
```

**After:**
```
AMS-SLA-001
Standard AMS SLA response time targets:
P1 — Critical: 1 hour
P2 — Major: 4 business hours
P3 — Normal: 1 business day
P4 — Minor: 3 business days
Uniform across Oracle, Acumatica, BeBanking. Response time ≠ resolution time.
```

**Commercial reason:** Without defined SLA targets, APPSolve cannot commit to or measure SLA performance in AMS agreements. Every AMS proposal previously used different response times or none at all. Standardised targets create a consistent baseline across all AMS agreements and provide the foundation for the SLA schedule attached to each AMS SOW.

---

### CL-AMS-003 — Priority Definitions Updated with Response Targets (AMS-PRI-001)

**BU decision:** BU-AMS-001  
**Assumption:** AMS-PRI-001

**Before:**
```
AMS-PRI-001 *(Pending BU-AMS-001)*
Priority classification: P1/P2/P3/P4 definitions only. No response time targets attached to priorities.
```

**After:**
```
AMS-PRI-001
Priority classification table with response targets embedded:
P1 — Critical: complete outage / payroll blocked / financial close blocked / data loss → 1 hour
P2 — Major: major functionality impaired / critical process blocked → 4 business hours
P3 — Normal: non-critical impaired / workaround exists → 1 business day
P4 — Minor: cosmetic / how-to / non-urgent → 3 business days
Response targets uniform across Oracle, Acumatica, BeBanking.
```

**Commercial reason:** Embedding response targets directly in the priority table makes the SLA self-contained and unambiguous. Clients and APPSolve teams can reference a single table rather than cross-referencing two assumptions.

---

### CL-AMS-004 — Support Hours Confirmed (AMS-HRS-001)

**BU decision:** BU-AMS-002  
**Assumption:** AMS-HRS-001

**Before:**
```
AMS-HRS-001 *(Pending BU-AMS-002)*
...Extended hours support (18:00–22:00 weekdays, Saturday, Sunday) and 24/7 support are available as separately contracted add-on services at the applicable uplift rate.
```

**After:**
```
AMS-HRS-001
Standard: 08:00–17:00 SAST, Monday–Friday, excluding South African public holidays.
Extended hours, weekend, and 24x7 require a separate commercial agreement — not included in standard AMS.
```

**Commercial reason:** "Available at uplift rate" is ambiguous — it implies APPSolve has a standard uplift rate to offer. The BU decision confirms the correct commercial position: extended hours and 24/7 are not in standard AMS at all and require a separately negotiated and contracted arrangement. This prevents clients from assuming they can upgrade hours by paying a small uplift on the existing agreement.

---

### CL-AMS-005 — Monthly Hours Model Updated (AMS-HRS-003)

**BU decision:** BU-AMS-003  
**Assumption:** AMS-HRS-003

**Before:**
```
AMS-HRS-003 *(Pending BU-AMS-003)*
Each AMS agreement includes a monthly support hours allocation. The allocation is defined per contract...
[Implied a default allocation exists]
```

**After:**
```
AMS-HRS-003
No default monthly support hours allocation.
Support model and allocation governed by the specific AMS agreement.
Both retainer-based (fixed monthly fee / defined support scope) and allocated-hour (monthly hour bucket) models are permitted.
Where an allocated-hour model applies, unused hours do not roll over.
```

**Commercial reason:** The prior draft text implied every AMS agreement includes a monthly hours bucket, which is not always true — some agreements are pure retainers with no defined hour allocation. Clarifying that both models are supported, and that no default allocation exists, prevents commercial misalignment when pricing AMS agreements. The hour allocation (if any) is now explicitly a per-agreement commercial decision.

---

### CL-AMS-006 — CR Threshold Set at 2 Hours (AMS-CR-001)

**BU decision:** BU-AMS-004  
**Assumption:** AMS-CR-001

**Before:**
```
AMS-CR-001 *(Pending BU-AMS-004)*
...The CR threshold — the minimum effort above which a CR is separately invoiced — is defined in the AMS agreement.
[No standard threshold defined]
```

**After:**
```
AMS-CR-001
Standard CR threshold: 2 hours.
Changes estimated above 2 hours require a formal written CR and written client approval.
APPSolve may absorb items below 2 hours at its discretion.
No entitlement created by previous discretionary absorption.
Threshold in a specific AMS agreement takes precedence over this standard.
```

**Commercial reason:** Without a defined threshold, every small change creates administrative overhead (formal CR, estimate, approval), damaging the client relationship, or the threshold is applied inconsistently between consultants. A 2-hour standard creates a predictable, practical boundary: small adjustments (adding a user, updating a workflow limit) proceed without CR friction; larger changes (new report, workflow restructuring) are formally scoped. The discretion clause protects APPSolve from entitlement claims while preserving flexibility.

---

### CL-AMS-007 — Release Advisory Confirmed; Regression Testing Excluded (AMS-REL-001)

**BU decision:** BU-AMS-005  
**Assumption:** AMS-REL-001

**Before:**
```
AMS-REL-001 *(Pending BU-AMS-005)*
...regression testing of the client's configuration after each quarterly update is not included in standard AMS unless specifically contracted.
```

**After:**
```
AMS-REL-001
Oracle quarterly release advisory is a standard AMS service item.
Regression testing, UAT execution, and business process validation excluded unless specifically contracted as a separately priced service.
Customer remains responsible for business testing of their own processes.
```

**Commercial reason:** Advisory (reviewing release notes and flagging impact to the client) is included. Execution (running test scripts, signing off UAT) is excluded. The BU decision explicitly adds UAT execution and business process validation to the exclusion list — closing the ambiguity where a client could argue that "regression testing" advisory includes helping them test. The customer responsibility line is now explicit.

---

### CL-AMS-008 — Named Consultant Not Included (AMS-SLA-005)

**BU decision:** BU-AMS-006  
**Assumption:** AMS-SLA-005

**Before:**
```
AMS-SLA-005 *(Pending BU-AMS-006)*
Named consultant: APPSolve uses best-efforts scheduling to assign a consistent named consultant to each AMS client... A named consultant is not a contractual guarantee unless explicitly contracted...
```

**After:**
```
AMS-SLA-005
Named consultant allocation is not included in standard AMS.
AMS support is delivered by the APPSolve support team on a best-effort resource allocation basis.
APPSolve endeavours to assign consultants with client-specific knowledge but makes no named consultant commitment.
Dedicated named consultant requires a separate commercial agreement at the applicable dedicated-resource rate.
```

**Commercial reason:** The prior text's "best-efforts scheduling to assign a consistent named consultant" could be read as a soft commitment. The BU decision confirms no commitment exists — the correct position is team-based support. A dedicated named consultant is a premium service requiring separate commercial agreement and rate. This eliminates the risk of a client arguing they were promised a specific consultant who is no longer available.

---

### CL-AMS-009 — Monitoring Scope Defined; Mailbox-Only as Standard (AMS-MON-001)

**BU decision:** BU-AMS-007  
**Assumption:** AMS-MON-001

**Before:**
```
AMS-MON-001 *(Pending BU-AMS-007)*
Basic monitoring — periodic review of the Oracle OIC integration error console... is available as a contracted AMS service item. Monitoring is not included in base AMS unless specifically contracted.
[Ambiguous — "basic monitoring" could imply it is a standard option that is simply optional]
```

**After:**
```
AMS-MON-001
Standard AMS = mailbox monitoring during contracted support hours only.
Proactive OIC error console monitoring, automated alerting, infrastructure monitoring, and application performance monitoring excluded unless specifically contracted.
24x7 monitoring, automated alerting, and infrastructure monitoring require a separately scoped and priced engagement.
```

**Commercial reason:** The prior text was ambiguous — "available as a contracted AMS service item" suggested OIC monitoring was a standard add-on at a known price. The BU decision clarifies the baseline: APPSolve monitors its support inbox during business hours. Everything beyond that (including reviewing the OIC error console proactively) is an add-on. This prevents consultants from defaulting to including OIC monitoring in base AMS pricing without commercial approval.

---

### CL-AMS-010 — Register Status Updated to Active (All 96 Rows)

**Change type:** Bulk status update  
**File:** AMS_ASSUMPTION_REGISTER.csv

**Before:** All 96 rows Status = "Draft" (8 rows with BU-AMS pending labels; 88 rows plain Draft)  
**After:** All 96 rows Status = "Active"; all BU-AMS category labels removed

**Method:** 7 sequential replace_all operations (one per BU-AMS pending label in Status column) + 7 sequential replace_all operations (one per BU-AMS pending label in Category column) + one final replace_all of `,Draft` → `,Active` for remaining rows.

---

## Impact Assessment

**Retroactive proposal updates required:** No. The AMS pack is new — there are no prior AMS proposals built from this library.

**TENDER_ASSUMPTION_ASSEMBLY_RULES.md:** Requires update — AMS pack status from Draft to Approved; totals updated.

**ASSUMPTION_LIBRARY_ROADMAP.md:** Requires update — Pack 10 AMS from Draft to Approved.

**Key commercial defaults now active across all AMS agreements:**
- SLA response targets: P1 = 1h; P2 = 4h; P3 = 1 day; P4 = 3 days
- Support hours: 08:00–17:00 SAST Mon–Fri (excluding public holidays)
- No default monthly hours; model per agreement
- CR threshold: 2 hours
- Release advisory: included; regression testing: excluded
- Named consultant: excluded from standard AMS
- Proactive monitoring: excluded from standard AMS; mailbox-only standard

---

*AMS_APPROVAL_CHANGE_LOG v1.0 | WP11E-A — AMS Assumptions Approval | 2026-06-15*  
*10 change records | All 7 BU-AMS items closed | AMS pack Approved — 96 assumptions Active*  
*Next action: Update TENDER_ASSUMPTION_ASSEMBLY_RULES.md and ASSUMPTION_LIBRARY_ROADMAP.md*
