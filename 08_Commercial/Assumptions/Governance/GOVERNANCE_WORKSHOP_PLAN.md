---
title: Governance Workshop Plan
version: v1.3
status: COMPLETE
programme: WP13 Governance Approval Campaign
date: 2026-06-16
last_updated: 2026-06-19
last_updated_by: WP16C — Oracle HCM Final Promotion and Governance Closure
---

# Governance Workshop Plan

**Programme:** WP13 | **Date:** 2026-06-16 | **Last updated:** 2026-06-19 (WP16C — PROGRAMME COMPLETE; all 54 decisions resolved; all 13 packs Approved v1.0; 0 outstanding)

> **Workshop order (all COMPLETE):** (1) BeBanking Workshop [COMPLETE WP14D/F] → (2) Acumatica Workshop [COMPLETE WP15C] → (3) EBS AMS Overlay [COMPLETE WP15F] → (4) Oracle HCM Workshop [COMPLETE WP16C — all 12 decisions confirmed via email 2026-06-19] → (5) OCI — not required.

---

## Workshop 1 — BeBanking Assumption Pack

**Priority:** Highest — BU-BB-006 is CRITICAL and blocks all BeBanking proposals.

### Overview

| Item | Detail |
|---|---|
| Pack | BeBanking Base (BB) |
| Decisions | 10 (BU-BB-001 through BU-BB-010) |
| Wave 1 (pre-workshop) | BU-BB-006 — CRITICAL: resolve before workshop via call |
| Wave 2 session | BU-BB-001, 002, 003, 008 (HIGH) — 60 minutes |
| Wave 3 session | BU-BB-004, 005, 007, 009, 010 (MEDIUM) — 45 minutes |

### Recommended Attendees

| Role | Attendance | Decisions |
|---|---|---|
| BeBanking BU Lead | Mandatory — all sessions | All 10 decisions |
| Commercial Director | Mandatory — Wave 2 | BU-BB-002, 003, 006 (commercial model) |
| BeBanking Solution Consultant | Recommended | BU-BB-004, 007, 010 (operational defaults) |
| Legal / Compliance representative | Optional | BU-BB-009 (POPIA disclosure) |

### Wave 1 Call (30 minutes — target: 2026-06-23)

**Objective:** Resolve BU-BB-006 before full workshop.

**Agenda:**
1. (5 min) Context: Why BU-BB-006 is CRITICAL — every BeBanking proposal is affected
2. (15 min) Review 4 options for support model; confirm commercial position
3. (5 min) Record decision
4. (5 min) Confirm Wave 2 workshop date

**Pre-reading:** `BEBANKING_BASE_ASSUMPTIONS_V1.md` Section 151 (BB-SUP), `GOVERNANCE_MASTER_DECISION_REGISTER.md` BU-BB-006 section

---

### Wave 2 Workshop — HIGH Decisions (60 minutes)

**Agenda:**

| Time | Item | Decision |
|---|---|---|
| 0:00–0:05 | Context: BeBanking pack overview; 10 decisions to resolve | — |
| 0:05–0:15 | Supported bank list — confirm standard scope | BU-BB-001 |
| 0:15–0:25 | New bank onboarding charging model | BU-BB-002 |
| 0:25–0:40 | Forex in base subscription — Commercial Director input required | BU-BB-003 |
| 0:40–0:55 | BeBanking payroll source policy — confirm Oracle-only position | BU-BB-008 |
| 0:55–1:00 | Next steps; confirm Wave 3 date | — |

**Governance note for BU-BB-008:** Acumatica payroll integration is permanently prohibited regardless of how this decision is resolved. The decision only affects non-Oracle payroll systems (PaySpace, VIP, Sage). Document this constraint explicitly in the Decision Record.

**Required pre-reading:** `GOVERNANCE_MASTER_DECISION_REGISTER.md` HIGH decisions section; `BEBANKING_BASE_ASSUMPTIONS_V1.md` Sections 141 (BB-BNK), 143 (BB-PYR), 144 (BB-FX)

---

### Wave 3 Workshop — MEDIUM Decisions (45 minutes)

**Agenda:**

| Time | Item | Decision |
|---|---|---|
| 0:00–0:08 | Hypercare duration — align with Acumatica decision | BU-BB-004 |
| 0:08–0:15 | Standard reporting pack — confirm 5-report set or amend | BU-BB-005 |
| 0:15–0:22 | Multi-country scope — SA only vs Namibia in standard | BU-BB-007 |
| 0:22–0:32 | POPIA operator disclosure — align with Acumatica decision | BU-BB-009 |
| 0:32–0:40 | DR testing inclusion and frequency | BU-BB-010 |
| 0:40–0:45 | Confirm all 10 decisions recorded; pack status change to Approved | — |

**Note:** BU-BB-004 (hypercare) and BU-BB-009 (POPIA) should be pre-aligned with the Acumatica workshop outcomes before this session. Present the Acumatica-approved answers as recommended defaults.

---

## Workshop 1b — EBS AMS Overlay Packs — **COMPLETE WP15F 2026-06-19**

> **All 9 EBS AMS overlay decisions resolved via email (6), Commercial Director (1), and workshop (2). Both EBS overlay packs promoted to Approved v1.0. No further workshop action required for EBS overlay.**

### Overview

| Item | Detail |
|---|---|
| Packs | EBS SLA Overlay (53 assumptions) + EBS DRM Overlay (62 assumptions) |
| Decisions | 9 total (4 EBS-SLA + 5 EBS-DRM) |
| Resolution path (WP15E classification) | 6A email, 1B Commercial Director, 2C workshop |
| Pack status | **Both Approved v1.0 — WP15F 2026-06-19** |

### Resolved Decisions

| ID | Decision | Resolution Path | Status |
|---|---|---|---|
| EBS-SLA-BU-001 | P1 response target | Email | **RESOLVED** — client-configurable; specific target in AMS agreement schedule |
| EBS-SLA-BU-002 | Resolution SLA scope | Workshop | **RESOLVED** — Option B: resolution SLAs on explicit client request only |
| EBS-SLA-BU-003 | Premium model | Commercial Director | **RESOLVED** — fixed monthly premium confirmed commercial standard |
| EBS-SLA-BU-004 | Service credits | Email | **RESOLVED** — Option C: negotiate per engagement |
| EBS-DRM-BU-001 | Resource hours model | Email | **RESOLVED** — per-engagement hours; ARM IT045 reference architecture |
| EBS-DRM-BU-002 | Rollover model | Email | **RESOLVED** — unused hours roll over; expire end of month N+1 |
| EBS-DRM-BU-003 | Leave/illness standard | Email | **RESOLVED** — 3-BD illness absorption; 10-BD annual leave notice confirmed |
| EBS-DRM-BU-004 | Notice period | Email | **RESOLVED** — 30 calendar days; all 6-week / 30-BD references replaced |
| EBS-DRM-BU-005 | Runbook standard | Email | **RESOLVED** — runbook standard deliverable in all EBS AMS DRM engagements |

---

## Workshop 2 — Acumatica Assumption Pack — **COMPLETE WP15C 2026-06-18**

> **All 14 Acumatica BU Lead decisions resolved. Pack promoted to Approved v1.0. No further workshop action required for Acumatica.**

### Overview

| Item | Detail |
|---|---|
| Pack | Acumatica Base (ACU) |
| Decisions | 14 (BU-ACU-001–015, excl. BU-ACU-013) |
| Wave 1 (pre-workshop) | BU-ACU-009 — **RESOLVED WP14G 2026-06-18** — Acumatica Gold Partner confirmed |
| Wave 2 session | BU-ACU-001, 002, 003, 004, 010, 011, 012 (7 HIGH) — **RESOLVED WP15C 2026-06-18** |
| Wave 3 session | BU-ACU-005, 006, 007, 008, 014, 015 (6 MEDIUM) — **RESOLVED WP15C 2026-06-18** |
| Pack status | **Approved v1.0 — WP15C 2026-06-18** |

### Recommended Attendees

| Role | Attendance | Decisions |
|---|---|---|
| Acumatica BU Lead | Mandatory — all sessions | All 14 decisions |
| Commercial Director | Wave 2 — BU-ACU-011 item | BU-ACU-011 (non-PaySpace policy) |
| Senior Acumatica Consultant | Recommended | BU-ACU-001, 003, 004, 005, 006 (operational defaults) |
| Legal / Compliance representative | Optional | BU-ACU-012 (POPIA) |

### Wave 1 Action — RESOLVED WP14G 2026-06-18

BU-ACU-009 — Acumatica partner tier. Acumatica BU Lead confirmed APPSolve is an Acumatica Gold Partner. ACU-GEN-009 updated. Note: COMP-016 (Acumatica Partner Certificate) still MISSING (OAR-E03) — obtain from partner portal.

---

### Wave 2 Workshop — HIGH Decisions — **ALL RESOLVED WP15C 2026-06-18**

| Decision | Resolution |
|---|---|
| BU-ACU-001 | PaySpace integration method confirmed at pre-sales per PaySpace licence tier (API preferred; file-based fallback) |
| BU-ACU-002 | AMS Pack tiers adopted for Acumatica: Simple / Standard / Complex |
| BU-ACU-003 | BI connector always separately scoped — never in standard implementation scope |
| BU-ACU-004 | APPSolve maintains published ISV Support List; proposals include ISV only if on the list |
| BU-ACU-010 | Opening balances and open items only; historical transaction migration separately scoped |
| BU-ACU-011 | PaySpace is standard; non-PaySpace assessed at pre-sales as Custom Integration |
| BU-ACU-012 | Mandatory POPIA data residency disclosure in all Acumatica proposals |

---

### Wave 3 Workshop — MEDIUM Decisions — **ALL RESOLVED WP15C 2026-06-18**

| Decision | Resolution |
|---|---|
| BU-ACU-005 | Parallel run excluded by default; SOW explicit inclusion required |
| BU-ACU-006 | All factory-delivered Acumatica reports for modules in scope included standard |
| BU-ACU-007 | Virtual facilitated training standard; on-site available at additional cost |
| BU-ACU-008 | 4-week hypercare standard (consistent with BeBanking + Oracle) |
| BU-ACU-014 | PM included for 3+ modules or multi-BU scope; Lead Consultant manages smaller implementations |
| BU-ACU-015 | Consolidated reporting always separately scoped for multi-entity |

---

## Workshop 3 — Oracle HCM Module Packs — **COMPLETE WP16C 2026-06-19**

> **All 21 Oracle HCM module decisions resolved. All 4 module packs promoted to Approved v1.0. No further workshop action required.**

**Resolution path:** 9 MEDIUM decisions resolved WP15F via email governance; 2 HIGH (BU-REC-005/006) and 10 LOW decisions confirmed by Oracle HCM BU Lead email WP16C 2026-06-19.

### Overview

| Item | Detail |
|---|---|
| Packs | HCM Recruiting (54), Learning (37), Talent Management (31), Workforce Compensation (30) |
| Original decisions | 21 (7 REC + 5 LRN + 4 TLT + 5 COM) |
| MEDIUM decisions resolved | 9 resolved WP15F 2026-06-19 via email governance |
| HIGH decisions resolved | 2 (BU-REC-005, BU-REC-006) — WP16C 2026-06-19 |
| LOW decisions resolved | 10 — WP16C 2026-06-19 (email ratification; no workshop required) |
| Pack status | **All 4 module packs Approved v1.0 — WP16C 2026-06-19** |

### Recommended Attendees

| Role | Attendance |
|---|---|
| Oracle HCM BU Lead | Mandatory — all sessions |
| Senior Recruiting Consultant | Recommended for REC decisions |
| Senior HCM Consultant (Learning/Talent/Comp) | Recommended for LRN, TLT, COM decisions |

### Pre-Workshop — LOW Decision Email Confirmation

Send the following list to the Oracle HCM BU Lead for email approval **before** the workshop. This removes 10 decisions from workshop agenda time.

| ID | Decision | Recommended Default |
|---|---|---|
| BU-REC-007 | Requisition template count | No default limit — confirmed per engagement |
| BU-LRN-001 | Learning community count | 2 communities as standard |
| BU-LRN-003 | Third-party LMS integrations | 1 standard; additional separately scoped |
| BU-LRN-005 | SETA extract format | OTBI guidance only — no bespoke extract |
| BU-TLT-001 | Performance template count | 1 annual + 1 mid-year review |
| BU-TLT-003 | Succession plan count | No default limit — confirmed per engagement |
| BU-TLT-004 | Career path configuration | Configure where client provides content |
| BU-COM-001 | Merit plan count | 1 merit plan |
| BU-COM-002 | Bonus plan count | 1 bonus plan |
| BU-COM-005 | Pay equity reporting | OTBI guidance only; no standard extract |

---

### Wave 2 Call — HIGH Decisions (30 minutes)

**Agenda:**

| Time | Item | Decision |
|---|---|---|
| 0:00–0:15 | Recruiting Booster scope trigger — BOM-driven only | BU-REC-005 |
| 0:15–0:28 | Background check integration — OIC design only vs portal config | BU-REC-006 |
| 0:28–0:30 | Confirm; schedule Wave 3 sessions | — |

---

### Wave 3 Session A — Recruiting and Learning MEDIUM (60 minutes)

**Agenda:**

| Time | Item | Decision |
|---|---|---|
| 0:00–0:10 | Career site default — 1+1+1 or 1+1 only | BU-REC-001 |
| 0:10–0:18 | Interview scheduling calendar — MS365 only or Google Workspace | BU-REC-002 |
| 0:18–0:26 | Offer letter templates — 3 as standard | BU-REC-003 |
| 0:26–0:36 | Agency portal — explicit request only | BU-REC-004 |
| 0:36–0:44 | Learning completion history migration — 2 years or project-defined | BU-LRN-002 |
| 0:44–0:54 | LinkedIn Learning connector — scope on explicit request | BU-LRN-004 |
| 0:54–1:00 | Ratify LOW decisions confirmed by email | BU-REC-007, BU-LRN-001, 003, 005 |

---

### Wave 3 Session B — Talent and Compensation MEDIUM (60 minutes)

**Agenda:**

| Time | Item | Decision |
|---|---|---|
| 0:00–0:12 | 360-degree feedback — in scope or explicit request only | BU-TLT-002 |
| 0:12–0:24 | Compensation history migration — covered by HCM Base or standalone | BU-COM-003 |
| 0:24–0:36 | Total Compensation Statement — standard WFC or separate BOM | BU-COM-004 |
| 0:36–0:56 | Ratify LOW decisions: BU-TLT-001, 003, 004, BU-COM-001, 002, 005 | LOW decisions |
| 0:56–1:00 | Confirm all 21 decisions recorded; promote all 4 module packs | — |

**Required pre-reading:** All 4 HCM module pack BU Lead Review tables; `GOVERNANCE_MASTER_DECISION_REGISTER.md` Oracle HCM section

---

## Workshop 4 — OCI

**Status: NOT REQUIRED**

> The OCI Pack was fully approved via WP11H-A (2026-06-16). All 14 BU-OCI decisions were resolved and applied. BU-OCI-007 was permanently withdrawn. The OCI Pack is Approved v1.0 with zero outstanding decisions. No workshop is required for OCI.

If a review of applied OCI decisions is desired for completeness, a 30-minute BU Lead briefing (not a decision workshop) can be scheduled to walk through the 14 applied decisions and confirm no changes are required.

---

*Governance Workshop Plan v1.3 | WP13 + WP16C | 2026-06-16 | Updated 2026-06-19 WP16C — PROGRAMME COMPLETE; 54/54 decisions resolved; 13/13 packs Approved v1.0; 0 outstanding*
