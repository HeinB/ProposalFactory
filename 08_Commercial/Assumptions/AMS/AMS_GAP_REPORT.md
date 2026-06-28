---
document_id: AMS-GAP-REPORT
title: "AMS Assumptions — Gap Report"
version: "1.0"
created: "2026-06-15"
created_by: "WP11E — AMS / Managed Services Assumptions Pack"
status: "Draft — Active Gaps"
tracks: "AMS_ASSUMPTIONS_V1.md"
---

# AMS Assumptions — Gap Report

This report identifies gaps in APPSolve's commercial governance for Application Managed Services (AMS). A gap exists where an assumption in the AMS pack requires supporting documentation, a pricing model, a rate card, a process document, or a policy decision that does not yet exist.

**Criticality:**
- **CRITICAL** — Must be resolved before the next AMS SOW is issued
- **HIGH** — Material commercial risk; resolve within current quarter
- **MEDIUM** — Beneficial to formalise; manageable near-term without resolution
- **LOW** — Good governance; not currently blocking

---

## Gap Summary

| Gap ID | Area | Criticality | Status | Owner |
|---|---|---|---|---|
| GAP-AMS-001 | SLA Definition and Rate Card | CRITICAL | Open | Oracle BU Lead / Commercial Director |
| GAP-AMS-002 | AMS Pricing Model | CRITICAL | Open | Commercial Director / BU Leads |
| GAP-AMS-003 | AMS Service Agreement Template (SOW/MSA) | CRITICAL | Open | Legal / Commercial Director |
| GAP-AMS-004 | Standard Service Request Catalogue | HIGH | Open | Delivery Lead / BU Leads |
| GAP-AMS-005 | CR Threshold Policy | HIGH | Open | Commercial Director / BU Lead |
| GAP-AMS-006 | Oracle Release Advisory Process | HIGH | Open | Delivery Lead / Oracle BU Lead |
| GAP-AMS-007 | Defect vs Enhancement Classification Guide | HIGH | Open | Delivery Lead |
| GAP-AMS-008 | AMS Onboarding Checklist | MEDIUM | Open | Delivery Lead |
| GAP-AMS-009 | Monthly Report Template | MEDIUM | Open | Delivery Lead |
| GAP-AMS-010 | BeBanking AMS Succession Plan | MEDIUM | Open | BeBanking BU Lead |
| GAP-AMS-011 | Acumatica AMS Scope Definition | MEDIUM | Open | Acumatica BU Lead |
| GAP-AMS-012 | OIC Monitoring Framework | LOW | Open | Delivery Lead |
| GAP-AMS-013 | AMS Knowledge Transfer Process | LOW | Open | Delivery Lead |

---

## Detailed Gap Records

### GAP-AMS-001 — SLA Definition and Rate Card
**Criticality:** CRITICAL  
**Description:** `AMS-SLA-001` and `AMS-PRI-001` define the framework for P1/P2/P3/P4 priority classification and SLA response time targets, but BU-AMS-001 (pending) confirms that the actual response time targets have not been set. APPSolve has no formally approved SLA definition document.  
**Impact:** Every AMS proposal is issued with different SLA response times — or none at all. When a client disputes SLA performance, there is no authoritative reference. This is the highest-priority governance gap in AMS.  
**Resolution required:**
1. Define standard response time targets per priority (P1/P2/P3/P4) for business hours SLA
2. Define uplift targets for extended hours (18/5) and 24/7 SLA tiers
3. Define whether SLA targets differ by product (Oracle Fusion vs EBS vs Acumatica vs BeBanking)
4. Formalise in a one-page SLA schedule that is attached to every AMS SOW
**Owned by:** Oracle BU Lead + Commercial Director  
**Required before:** Next AMS SOW

---

### GAP-AMS-002 — AMS Pricing Model
**Criticality:** CRITICAL  
**Description:** `AMS-HRS-003` (pending BU-AMS-003) confirms that the standard monthly hour allocation is not yet defined. APPSolve has no standard AMS pricing model — proposals are priced ad hoc per client.  
**Impact:** Ad hoc pricing produces inconsistent AMS agreements across the client portfolio. Some agreements are underpriced (insufficient hours, wrong rate), eroding AMS margin. Some are overpriced, causing clients not to renew.  
**Resolution required:**
1. Define standard AMS hour tier packages (e.g., Starter: 10h/month, Standard: 20h/month, Advanced: 40h/month)
2. Define hourly rate per tier (standard hours, extended hours, public holiday)
3. Define the CR threshold per tier (below threshold = absorbed into monthly hours; above threshold = separately invoiced)
4. Define the overage rate (cost per additional hour beyond the monthly allocation)
5. Differentiate pricing by product where applicable (Oracle Fusion AMS vs EBS AMS vs Acumatica AMS vs BeBanking AMS)
**Owned by:** Commercial Director + BU Leads  
**Required before:** Next AMS SOW

---

### GAP-AMS-003 — AMS Service Agreement Template (SOW/MSA)
**Criticality:** CRITICAL  
**Description:** APPSolve does not have a standard AMS Master Service Agreement (MSA) or SOW template. AMS agreements are drafted ad hoc per client, using the implementation SOW as a base. AMS is a distinct commercial model — retainer-based, monthly, with different obligations from a project SOW — and deserves its own template.  
**Impact:** Without a standard template, AMS agreements are inconsistent. Key commercial protections (SLA schedule, CR process, escalation rights, liability cap, auto-renewal, termination notice) may be missing from some agreements.  
**Resolution required:**
1. AMS Master Service Agreement template (or AMS SOW addendum for clients where a master agreement exists)
2. Includes: scope schedule; SLA schedule; monthly hours schedule; CR process; pricing schedule; escalation path; auto-renewal and notice period; liability cap; confidentiality
3. Legal review recommended
**Owned by:** Legal / Commercial Director  
**Required before:** Next AMS SOW

---

### GAP-AMS-004 — Standard Service Request Catalogue
**Criticality:** HIGH  
**Description:** `AMS-SRQ-004` references a standard service request catalogue with pre-defined effort estimates. This catalogue does not exist. Without it, each SR is individually estimated, creating inconsistency and client friction.  
**Resolution required:** Standard SR catalogue per product (Oracle Fusion HCM, Oracle Fusion ERP, Acumatica) listing common service requests with pre-defined effort in hours:
- Add new Oracle user and assign roles: X hours
- Update approval limit in workflow: Y hours
- Add new GL account to value set: Z hours
- Update supplier payment terms: Z hours
- Add new cost centre: Z hours
- Etc.
**Owned by:** Delivery Lead + BU Leads  
**Required by:** Q3 2026

---

### GAP-AMS-005 — CR Threshold Policy
**Criticality:** HIGH  
**Description:** `AMS-CR-001` (pending BU-AMS-004) identifies the need for a CR threshold — the effort level below which a CR is absorbed into the monthly hours and above which it is separately invoiced. This threshold is currently undefined and varies by agreement.  
**Resolution required:** Define the standard CR threshold (in hours and/or cost) and formalise in the AMS pricing model (GAP-AMS-002). The threshold should balance: client simplicity (not generating a CR for every small change) vs APPSolve margin protection (not absorbing large changes into fixed-fee hours).  
**Owned by:** Commercial Director + BU Lead  
**Required before:** Next AMS SOW

---

### GAP-AMS-006 — Oracle Release Advisory Process
**Criticality:** HIGH  
**Description:** `AMS-REL-001` (pending BU-AMS-005) includes Oracle quarterly release advisory as a standard AMS service item, but APPSolve has no documented process for delivering it. The Oracle quarterly release notes are published by Oracle 4–6 weeks before each update. APPSolve has no standard template for summarising release impacts or communicating them to AMS clients.  
**Resolution required:**
1. Oracle Quarterly Release Advisory process document: who reviews release notes; what to look for; how to document client-specific impact; how to communicate to client
2. Oracle Release Advisory Report template: module-by-module impact summary; recommended client actions; items requiring APPSolve investigation
3. Release advisory calendar (aligned to Oracle's quarterly update schedule)
**Owned by:** Delivery Lead + Oracle BU Lead  
**Required by:** Before next Oracle quarterly update after AMS approval

---

### GAP-AMS-007 — Defect vs Enhancement Classification Guide
**Criticality:** HIGH  
**Description:** `AMS-DEF-002` defines the three-way classification (defect / enhancement / configuration drift) but APPSolve has no decision guide for making the classification in ambiguous cases. This ambiguity causes the most common AMS commercial dispute.  
**Resolution required:** Decision guide with examples:
- Clear defect examples (system doesn't do what the design says it should)
- Clear enhancement examples (client wants new functionality not in the design)
- Clear configuration drift examples (someone changed a setting; now things don't work)
- Ambiguous scenario examples with classification rationale
**Owned by:** Delivery Lead  
**Required by:** Q3 2026

---

### GAP-AMS-008 — AMS Onboarding Checklist
**Criticality:** MEDIUM  
**Description:** `AMS-CUS-010` requires onboarding documentation at AMS start. No standard onboarding checklist exists. Each AMS engagement starts with the AMS team asking ad hoc questions.  
**Resolution required:** AMS onboarding checklist: system access credentials required; documentation to be provided; contacts to be introduced; first support test (log a P3 test ticket); SLA agreement sign-off; CR approval authority confirmation.  
**Owned by:** Delivery Lead  
**Required by:** Q3 2026

---

### GAP-AMS-009 — Monthly Report Template
**Criticality:** MEDIUM  
**Description:** `AMS-REP-001` describes the monthly support report but APPSolve has no standard template. Each AMS consultant produces a different report format, making quality inconsistent.  
**Resolution required:** Standard monthly report template: executive summary; tickets by priority and status; SLA compliance table; hours consumed vs allocation chart; open items list; Oracle SR status; CR pipeline; next month planned activities.  
**Owned by:** Delivery Lead  
**Required by:** Q3 2026

---

### GAP-AMS-010 — BeBanking AMS Succession Plan
**Criticality:** MEDIUM  
**Description:** `AMS-SCP-006` notes that BeBanking AMS is only available where Carin Webb is available — a SPOF. The CONSULTANT_SKILL_MATRIX.md flags this as a critical SPOF. If APPSolve is to offer BeBanking AMS commitments to clients, a succession plan is required.  
**Resolution required:** Either: (a) train a second OIC consultant on BeBanking H2H specifics so that BeBanking AMS can continue during Carin's absence; OR (b) explicitly caveat all BeBanking AMS agreements with a SPOF disclaimer and agree a backup support process (escalation to Carin even during leave for P1s, or a subcontract arrangement).  
**Owned by:** BeBanking BU Lead  
**Required by:** Before the next BeBanking AMS SOW is signed

---

### GAP-AMS-011 — Acumatica AMS Scope Definition
**Criticality:** MEDIUM  
**Description:** `AMS-SCP-007` provides a brief description of Acumatica AMS scope but the Acumatica BU has not contributed to the AMS assumptions. Acumatica-specific AMS scope (which customisations are supportable under AMS; how Acumatica updates are managed; Acumatica ITSM integration) needs Acumatica BU Lead sign-off.  
**Resolution required:** Acumatica BU Lead to review AMS-SCP-007, AMS-REL-004, AMS-PAT-003, AMS-EXC-008, and AMS-EXC-009 and confirm or amend these assumptions.  
**Owned by:** Acumatica BU Lead  
**Required by:** Before next Acumatica AMS SOW

---

### GAP-AMS-012 — OIC Monitoring Framework
**Criticality:** LOW  
**Description:** `AMS-MON-001` describes basic OIC integration monitoring as a contractable service item. APPSolve has no standard monitoring framework document defining: what is checked; at what frequency; what constitutes a monitoring alert; how monitoring findings are reported.  
**Resolution required:** OIC monitoring framework: monitoring scope (which integrations); monitoring frequency (daily / twice-daily / continuous); alert thresholds; monitoring report format; escalation path for monitoring alerts.  
**Owned by:** Delivery Lead  
**Required by:** Q4 2026

---

### GAP-AMS-013 — AMS Knowledge Transfer Process
**Criticality:** LOW  
**Description:** When APPSolve transitions a client from an implementation project to AMS, there is no standard knowledge transfer process to ensure the AMS team has the context to support the client effectively.  
**Resolution required:** AMS knowledge transfer process: what documentation the implementation team hands over; a structured handover meeting; the AMS team's first month of "shadow support" (implementation consultant available for AMS escalation); formal handover sign-off.  
**Owned by:** Delivery Lead  
**Required by:** Q4 2026

---

*AMS_GAP_REPORT v1.0 | WP11E — AMS / Managed Services Assumptions Pack | 2026-06-15*  
*13 gaps identified: 3 CRITICAL / 4 HIGH / 4 MEDIUM / 2 LOW*  
*Owner: Commercial Director + Oracle BU Lead — resolve CRITICAL gaps before next AMS SOW*
