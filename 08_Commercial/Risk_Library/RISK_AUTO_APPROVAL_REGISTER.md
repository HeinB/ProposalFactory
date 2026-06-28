---
document_id: RISK-AUTO-APPROVAL-REGISTER-V1
title: "Risk Library — Auto Approval Register"
version: "1.0"
status: "AWAITING BU LEAD REVIEW"
created: "2026-06-26"
created_by: "WP18B-EXT.1B — Risk Library Decision Harvest"
approved_by: ""
approved_date: ""
category: "Commercial / Risk Library / Governance"
scope: "Register of 20 Category A risks eligible for auto-approval during governance session. No decision required per risk — BU Lead confirms the batch register as a whole. Approvals are applied in ENTERPRISE_RISK_REGISTER_V1.md after the governance session."
related_documents:
  - ENTERPRISE_RISK_REGISTER_V1.md
  - RISK_GOVERNANCE_DECISION_REGISTER.md
  - RISK_GOVERNANCE_WORKSHOP_PACK.md
---

# Risk Library — Auto Approval Register

**Work Package:** WP18B-EXT.1B  
**Status:** AWAITING BU LEAD REVIEW  
**Auto-approval eligible:** 20 risks  
**Auto-approval criteria:** Single approved source; no rating change from source; no merger decision; faithful extraction; schema-complete; assumption-cross-referenced; pattern-mapped  

**Instructions for BU Lead:** Review the batch summary below. The individual entries confirm business meaning is unchanged from source material. No individual risk requires a decision. Sign off the batch register in the Approval section at the bottom to promote all 20 risks to `approved_for_reuse: Yes`.

**Do not apply approvals in this document.** Approvals are applied by updating ENTERPRISE_RISK_REGISTER_V1.md fields after sign-off.

---

## Auto-Approval Criteria Reference

A risk is eligible for auto-approval if ALL of the following are true:

| Criterion | Requirement |
|---|---|
| Source count | Single approved KB asset (no merger decision required) |
| Rating change | None — V1.0 rating equals source risk rating |
| Merger decision | None required (no deduplication group involving this risk) |
| Schema completeness | All 32 fields populated in ENTERPRISE_RISK_REGISTER_V1.md |
| Assumption cross-reference | At least one governed assumption ID cited |
| Proposal mapping | Mapped to at least one section and one pattern |
| Business meaning | Confirmed unchanged from source material (see entries below) |

---

## Batch Summary

| Risk ID | Title | Category | Rating | Source Asset | Pattern(s) |
|---|---|---|---|---|---|
| RC-DATA-002 | Employee record mapping errors at migration | RC-DATA | MEDIUM | W3S1-002 | P1, P2, P3, P7, P9 |
| RC-DATA-005 | Data migration reconciliation not signed off | RC-DATA | MEDIUM | W3S1-009 | P1, P2, P3, P7, P8, P9 |
| RC-INT-001 | Oracle integration API version deprecation | RC-INT | MEDIUM | W3S1-004 | P1, P2, P3, P6, P7, P8 |
| RC-INT-003 | Integration data volume exceeds API limits | RC-INT | MEDIUM | W3S1-003 | P1, P2, P3, P6, P7, P8 |
| RC-INT-004 | Integration failure causes payroll input errors | RC-INT | HIGH | W3S1-009 | P1, P2, P3 |
| RC-INT-006 | OIC connectivity to on-premise systems | RC-INT | MEDIUM | W3S1-004 | P3, P6 |
| RC-INT-007 | Integration testing window insufficient | RC-INT | MEDIUM | W3S1-005 | P1, P2, P3, P6, P7, P8 |
| RC-TECH-001 | Oracle Cloud quarterly update impacts configuration | RC-TECH | MEDIUM | W3S1-002 | P1–P9, P11–P13 |
| RC-TECH-004 | WFM scheduling rule complexity | RC-TECH | HIGH | W3S1-008 | P1, P2 |
| RC-TECH-005 | Oracle HCM localisation gaps for South Africa | RC-TECH | HIGH | W3S1-004 | P1, P2, P3 |
| RC-TECH-007 | Oracle Cloud environment provisioning delay | RC-TECH | LOW | W3S1-002 | P1–P9, P11 |
| RC-TECH-009 | Custom report performance at scale | RC-TECH | MEDIUM | W3S1-006 | P1, P2, P3, P7, P8 |
| RC-TECH-010 | Oracle BI Publisher / OTBI limitations | RC-TECH | MEDIUM | W3S1-006 | P1, P2, P3, P7, P8 |
| RC-TECH-011 | Acumatica customisation complexity | RC-TECH | MEDIUM | W3S1-007 | P11 |
| RC-CLIENT-001 | Client project sponsor unavailable | RC-CLIENT | HIGH | W3S1-002 | P1–P9, P11–P13 |
| RC-CLIENT-002 | Client UAT not completed on schedule | RC-CLIENT | HIGH | W3S1-002 | P1–P9, P11–P13 |
| RC-CLIENT-003 | Client change management not executed | RC-CLIENT | HIGH | W3S1-003 | P1–P9, P11–P13 |
| RC-CLIENT-005 | Training attendance below threshold | RC-CLIENT | MEDIUM | W3S1-002 | P1–P9, P11–P13 |
| RC-CLIENT-006 | Client IT infrastructure not ready | RC-CLIENT | MEDIUM | W3S1-004 | P1, P2, P3, P7, P8, P11 |
| RC-COMM-003 | Proposal scope misalignment with actual requirements | RC-COMM | HIGH | W3S1-002 | P1–P9, P11–P13 |

---

## Individual Entry Confirmations

### RC-DATA-002 — Employee Record Mapping Errors at Migration

**Source:** W3S1-002 (HCM Base — HCM-ORG-002, HCM-ORG-003)  
**Rating:** MEDIUM (Medium likelihood × Medium impact)  
**Auto-approval basis:** Single source; rating unchanged; single-stage extraction; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; assumption IDs formalised; pattern mapping added (P1, P2, P3, P7, P9)  
**Business meaning confirmation:** Risk is unchanged from source — employee-to-position mapping errors in legacy data require cleansing before migration. No scope change. No rating change.

---

### RC-DATA-005 — Data Migration Reconciliation Not Signed Off

**Source:** W3S1-009 (Payroll Integration — HCM-PAY-001, HCM-PAY-003)  
**Rating:** MEDIUM (Medium likelihood × Medium impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; assumption IDs formalised; pattern mapping added (P1, P2, P3, P7, P8, P9)  
**Business meaning confirmation:** Risk is unchanged — client sign-off on data reconciliation results is required before go-live. No scope change. No rating change.

---

### RC-INT-001 — Oracle Integration API Version Deprecation

**Source:** W3S1-004 (HCM Recruiting — OIC-MAP-001, OIC-VER-001)  
**Rating:** MEDIUM (Medium likelihood × Medium impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; OIC assumption IDs formalised; pattern mapping added (P1, P2, P3, P6, P7, P8)  
**Business meaning confirmation:** Oracle API version changes between project phases can break integration configurations. Risk and mitigation (version pinning; Oracle release monitoring) unchanged from source.

---

### RC-INT-003 — Integration Data Volume Exceeds API Limits

**Source:** W3S1-003 (HCM Learning — OIC-VOL-001)  
**Rating:** MEDIUM (Medium likelihood × Medium impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; OIC volume assumption ID formalised; pattern mapping added (P1, P2, P3, P6, P7, P8)  
**Business meaning confirmation:** High-volume integration batches can exceed Oracle API rate limits. Risk unchanged from source. Mitigation (volume testing; batch-size tuning) unchanged.

---

### RC-INT-004 — Integration Failure Causes Payroll Input Errors

**Source:** W3S1-009 (Payroll Integration — HCM-PAY-002, AMS-REL-001)  
**Rating:** HIGH (High likelihood × Medium impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; payroll assumption IDs formalised; pattern mapping restricted to payroll-integration patterns (P1, P2, P3)  
**Business meaning confirmation:** Upstream integration failures that cause incorrect payroll input data are a HIGH risk in payroll-integrated implementations. Risk unchanged from source.

---

### RC-INT-006 — OIC Connectivity to On-Premise Systems

**Source:** W3S1-004 (HCM Recruiting — OIC-CON-001)  
**Rating:** MEDIUM (Medium likelihood × Medium impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; OIC connectivity assumption ID formalised; pattern mapping restricted to OIC-applicable patterns (P3, P6)  
**Business meaning confirmation:** OIC cloud-to-on-premise connectivity requires network configuration that may not be in project scope. Risk unchanged from source.

---

### RC-INT-007 — Integration Testing Window Insufficient

**Source:** W3S1-005 (HCM Compensation — OIC-TEST-001)  
**Rating:** MEDIUM (Medium likelihood × Medium impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; OIC testing assumption ID formalised; pattern mapping added for all integration-applicable patterns  
**Business meaning confirmation:** Client environment availability constraints compress integration testing windows. Risk unchanged from source.

---

### RC-TECH-001 — Oracle Cloud Quarterly Update Impacts Configuration

**Source:** W3S1-002 (HCM Base — HCM-ORG-001)  
**Rating:** MEDIUM (Medium likelihood × Medium impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; HCM base assumption ID formalised; pattern mapping broad (P1–P9, P11–P13 — applicable to all Oracle Cloud implementations)  
**Business meaning confirmation:** Oracle's quarterly patch releases can affect configured workflow, UI, and report outputs between project phases. Risk unchanged from source. Excluded from P10 (DBA, managed service, no implementation).

---

### RC-TECH-004 — WFM Scheduling Rule Complexity

**Source:** W3S1-008 (Oracle WFM — HCM-WFM-001)  
**Rating:** HIGH (High likelihood × High impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; WFM assumption ID formalised; pattern mapping restricted to WFM-applicable patterns (P1, P2)  
**Business meaning confirmation:** Oracle WFM scheduling rules for shift patterns, rotating shifts, and multi-employment-type configurations routinely exceed initial scope estimates. Risk unchanged from source. Note: distinct from RC-TECH-003 (absence rules) — scheduling rules and absence rules are separate WFM configuration domains.

---

### RC-TECH-005 — Oracle HCM Localisation Gaps for South Africa

**Source:** W3S1-004 (HCM Recruiting — HCM-SETA-001, AMS-LEG-001)  
**Rating:** HIGH (High likelihood × High impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; localisation assumption IDs formalised; pattern mapping restricted to SA-specific HCM patterns (P1, P2, P3); country selector variable added  
**Business meaning confirmation:** Oracle HCM global cloud platform does not natively address all SA legislative nuances (BCEA leave calculations, Employment Equity reporting formats, payroll tax edge cases). Risk unchanged from source. Excluded when country ≠ ZA.

---

### RC-TECH-007 — Oracle Cloud Environment Provisioning Delay

**Source:** W3S1-002 (HCM Base — HCM-ORG-001)  
**Rating:** LOW (Low likelihood × Medium impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; HCM environment assumption ID formalised; pattern mapping broad (P1–P9, P11); excluded from P10 and P12 (non-Oracle patterns)  
**Business meaning confirmation:** Oracle environment provisioning delays are infrequent but can affect project kickoff timelines. LOW rating reflects observed low frequency. Risk unchanged from source.

---

### RC-TECH-009 — Custom Report Performance at Scale

**Source:** W3S1-006 (HCM Analytics — HCM-RPT-001)  
**Rating:** MEDIUM (Medium likelihood × Medium impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; HCM Analytics reporting assumption ID formalised; pattern mapping for reporting-applicable patterns (P1, P2, P3, P7, P8)  
**Business meaning confirmation:** Custom OTBI and BI Publisher reports built during implementation can degrade under production data volumes. Risk unchanged from source.

---

### RC-TECH-010 — Oracle BI Publisher / OTBI Limitations

**Source:** W3S1-006 (HCM Analytics — HCM-RPT-002)  
**Rating:** MEDIUM (Medium likelihood × Medium impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; HCM Analytics OTBI assumption ID formalised; pattern mapping for reporting-applicable patterns (P1, P2, P3, P7, P8)  
**Business meaning confirmation:** Oracle's standard reporting tools (OTBI, BI Publisher) have functional limitations for complex analytical requirements. Risk unchanged from source. Distinct from RC-TECH-009 (performance) — this risk concerns capability gaps, not volume-induced degradation.

---

### RC-TECH-011 — Acumatica Customisation Complexity

**Source:** W3S1-007 (Acumatica — ACU-DEV-001, ACU-INT-001)  
**Rating:** MEDIUM (Medium likelihood × Medium impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete; Acumatica-specific  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; Acumatica assumption IDs formalised; pattern mapping restricted to P11 only  
**Business meaning confirmation:** Acumatica customisation requirements (beyond out-of-the-box configuration) introduce development complexity and testing overhead. Risk unchanged from source. Excluded from all Oracle and BeBanking patterns.

---

### RC-CLIENT-001 — Client Project Sponsor Unavailable

**Source:** W3S1-002 (HCM Base — HCM-ORG-001)  
**Rating:** HIGH (High likelihood × High impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; assumption ID formalised; pattern mapping broad (P1–P9, P11–P13)  
**Business meaning confirmation:** Absence of an authorised client project sponsor prevents escalation, design sign-off, and commercial decisions. HIGH rating reflects both the frequency and severity of this constraint. Risk unchanged from source.

---

### RC-CLIENT-002 — Client UAT Not Completed on Schedule

**Source:** W3S1-002 (HCM Base — HCM-ORG-001)  
**Rating:** HIGH (High likelihood × High impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; assumption ID formalised; pattern mapping broad (P1–P9, P11–P13)  
**Business meaning confirmation:** Client UAT delays push go-live dates and compress post-UAT activities. HIGH rating reflects consistent observation across implementations. Risk unchanged from source.

---

### RC-CLIENT-003 — Client Change Management Not Executed

**Source:** W3S1-003 (HCM Learning — HCM-CHG-001)  
**Rating:** HIGH (High likelihood × High impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; HCM change management assumption ID formalised; pattern mapping broad (P1–P9, P11–P13)  
**Business meaning confirmation:** Failure to execute user adoption, communications, and training causes post-go-live support burden and end-user resistance. Risk unchanged from source. Note: distinct from RC-CLIENT-005 (training attendance) — this risk concerns the change management programme itself not being executed, not just low training attendance.

---

### RC-CLIENT-005 — Training Attendance Below Threshold

**Source:** W3S1-002 (HCM Base — HCM-ORG-001)  
**Rating:** MEDIUM (Medium likelihood × Medium impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; assumption ID formalised; pattern mapping broad (P1–P9, P11–P13)  
**Business meaning confirmation:** Insufficient end-user training attendance produces elevated support ticket volumes post-go-live. MEDIUM reflects that training attendance is a manageable risk with clear mitigations. Risk unchanged from source.

---

### RC-CLIENT-006 — Client IT Infrastructure Not Ready

**Source:** W3S1-004 (HCM Recruiting — OIC-CON-001)  
**Rating:** MEDIUM (Medium likelihood × Medium impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; OIC connectivity assumption ID formalised; pattern mapping restricted to infrastructure-relevant patterns (P1, P2, P3, P7, P8, P11)  
**Business meaning confirmation:** Client network, firewall, and SSO infrastructure readiness can block integration and cloud access during the project. Risk unchanged from source.

---

### RC-COMM-003 — Proposal Scope Misalignment with Actual Requirements

**Source:** W3S1-002 (HCM Base — HCM-ORG-001)  
**Rating:** HIGH (High likelihood × High impact)  
**Auto-approval basis:** Single source; rating unchanged; schema-complete  
**Metadata changes applied in V1.0:** All 18 normalisation fields added; assumption ID formalised; pattern mapping broad (P1–P9, P11–P13)  
**Business meaning confirmation:** Scope written into a proposal based on tender documentation may not reflect the client's actual configuration or implementation requirements, producing rework at discovery. Risk unchanged from source.

---

## Batch Approval Sign-Off

*To be completed during or after the governance session.*

| Field | Value |
|---|---|
| **Approved by** | |
| **Approval date** | |
| **Approved risks (count)** | / 20 |
| **Exceptions noted** | |
| **Post-approval action** | Update ENTERPRISE_RISK_REGISTER_V1.md: set `approved_for_reuse: Yes` and `approved_by` for all 20 risks listed above |

**Note:** Any risk in this batch that the BU Lead wishes to review individually should be moved to the Decision Register (RISK_GOVERNANCE_DECISION_REGISTER.md) before sign-off.
