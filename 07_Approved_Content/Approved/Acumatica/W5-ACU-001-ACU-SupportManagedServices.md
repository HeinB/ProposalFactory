---
document_id: W5-ACU-001-ACU-SupportManagedServices
title: "Acumatica Support & Managed Services"
version: "1.0 APPROVED"
source_status: Approved
approved_for_reuse: Yes
lifecycle_status: APPROVED
approved_by: "Hein Blignaut"
approval_date: "2026-06-14"
reviewed_by: "Hein Blignaut"
review_date: "2026-06-14"
evidence_basis:
  - "Interconnect Systems — Acumatica Field Services (active support; Tier 1 — W1S2-006)"
  - "HyDac — Acumatica Manufacturing ERP + BeBanking (active support; Tier 1 — HIST-005)"
  - "DSSSA, FuelU2, Maxiflex — Acumatica ERP (active support; reference letters registered 2026-06-14)"
  - "W1S1-009 (Hybrid Support Model — structural basis)"
  - "W2S1-004 (Oracle Managed Services — structural template; content not reused)"
created: "2026-06-14"
created_by: "Claude (AI — WP7 W5-ACU-001 extraction)"
wave: "Wave 5"
bu: Acumatica
kb_destination: "06_Capabilities/Acumatica/Support/"
pre_tender_checks:
  - PT-ACU-S01: "Confirm which reference clients can be named for this tender before citing any client in the support section"
  - PT-ACU-S02: "Confirm current SLA terms align with what is stated before submission (consult Acumatica Practice Lead)"
  - PT-ACU-S03: "Section 12.2 (support escalation matrix detail) must not appear in external submissions without BU Lead review"
governance_restrictions:
  - "Interconnect Systems: account manager approval required before naming at each tender"
  - "HyDac: account manager approval required before naming at each tender"
  - "DSSSA, FuelU2, Maxiflex: letters registered 2026-06-14; account manager approval required before naming"
  - "Do not conflate Acumatica support with Oracle managed services (W2S1-004) or BeBanking support (W1S3-009)"
---

> **APPROVED — approved_for_reuse: Yes — Approved by Hein Blignaut (BU Lead), 2026-06-14**
> WP7 Wave 5 Deliverable. Evidence: Interconnect Systems, HyDac, DSSSA, FuelU2, Maxiflex.
> Pre-tender checks PT-ACU-S01 through PT-ACU-S03 must be applied before each tender submission.

---

# Acumatica Support & Managed Services
**APPSolve Acumatica Post-Implementation Support Framework**

---

## 1. Executive Summary

APPSolve provides dedicated post-implementation support and managed services for Acumatica ERP clients across Southern Africa. Our Acumatica support capability combines deep system knowledge with a structured service model — ensuring clients receive the right level of support at each stage of the ERP lifecycle, from go-live hypercare through long-term continuous improvement.

APPSolve's Acumatica support clients span manufacturing, distribution, professional services, and inter-governmental sectors. Our support team consists of Acumatica-certified consultants with functional, technical, and integration expertise, supported by our Remote Support Centre for after-hours monitoring and incident management.

This document describes APPSolve's Acumatica support framework — the service tiers, SLA model, escalation architecture, enhancement delivery process, and continuous improvement programme.

---

## 2. Support Service Tiers

APPSolve's Acumatica support model is structured across three service tiers. Clients select the tier that matches their operational requirements and may upgrade tiers as their Acumatica usage matures.

| Tier | Name | Scope | Response Commitment |
|---|---|---|---|
| **Tier 1** | Respond | Break-fix and incident resolution. Covers functional issues, system errors, data corrections, and user queries. | P1: 2 hours; P2: 4 business hours; P3: 1 business day; P4: 3 business days |
| **Tier 2** | Retain | Respond scope + proactive monitoring, release management, minor configuration changes, and quarterly review sessions. | P1: 1 hour; P2: 2 business hours; P3: Same business day; P4: 2 business days |
| **Tier 3** | Evolve | Retain scope + functional enhancement delivery, integration support, reporting development, and continuous improvement programme. | P1: 1 hour; P2: 2 hours; P3: Same business day + dedicated success manager |

---

## 3. Hypercare — Transition from Implementation to Support

APPSolve's Hypercare period begins at go-live and runs for a period agreed during implementation planning (typically 4–8 weeks). Hypercare is a dedicated stabilisation period before the client transitions to the steady-state support tier.

### 3.1 Hypercare Activities

During Hypercare, APPSolve provides:
- On-site or near-site support presence (senior consultant availability during business hours)
- Same-day response to all production issues regardless of severity classification
- Daily stand-up with client key users and project sponsor
- Issue log management — all issues tracked and resolved before hypercare closes
- Knowledge transfer — super users confirmed competent before hypercare ends

### 3.2 Hypercare Exit Criteria

Hypercare is formally closed when:
- No unresolved Priority 1 or Priority 2 issues remain open
- Client super users are able to manage routine daily operations independently
- Support ticket volume is stable and trending downward
- Client has formally accepted the production system

Hypercare closure is documented and signed off jointly by the client project sponsor and the APPSolve Delivery Manager.

### 3.3 Steady-State Transition

At hypercare closure, the client transitions to their selected support tier. The APPSolve Account Manager takes over as the primary client relationship contact. A formal handover meeting is held between the delivery team and the support team, covering: open items, known issues, configuration decisions, integration dependencies, and any planned enhancements.

---

## 4. Managed Support Model

### 4.1 Support Channels

Clients log support requests through:
- **Help Desk Portal** — online ticket logging (available 24x7)
- **Email** — designated support inbox monitored during business hours
- **Phone** — Priority 1 incidents only; direct line to on-call support consultant

All requests receive an automated acknowledgement with ticket reference within 15 minutes of logging.

### 4.2 Severity Classification

| Priority | Definition | Response Time | Resolution Target |
|---|---|---|---|
| **P1 — Critical** | Production system down or inaccessible; critical business process blocked; data integrity at risk | Within 1 hour (Tier 2/3) or 2 hours (Tier 1) | Best effort — continuous until resolved |
| **P2 — High** | Major functional area impaired; workaround exists but inefficient; affecting multiple users | Within 2-4 business hours | Same business day |
| **P3 — Medium** | Single user impact; workaround available; non-critical functionality | Same business day | Within 3 business days |
| **P4 — Low** | Configuration question; user training query; cosmetic issue; enhancement request | Within 2-3 business days | Scheduled in next available slot |

### 4.3 Ticket Lifecycle

```
Log → Acknowledge (auto, <15 min) → Triage → Assign → Investigate → Resolve → Close → Client Confirmation
```

All tickets are visible to the client through the Help Desk Portal. Status updates are provided at each lifecycle stage. Clients can escalate any ticket at any time through the escalation process (Section 5).

### 4.4 Support Hours

| Service | Hours |
|---|---|
| Business Hours Support | 08:00 – 17:00 Monday to Friday (SA business days) |
| Extended Hours (Tier 2/3) | 07:00 – 19:00 Monday to Friday |
| 24x7 Monitoring | Remote Support Centre — P1 alerts escalated to on-call consultant |
| After-Hours Emergency | P1 Critical — on-call consultant response via phone |

---

## 5. Escalation Model

### 5.1 Escalation Path

| Level | Contact | Trigger |
|---|---|---|
| **Level 1** | Help Desk Consultant | Initial ticket assignment and first-line resolution |
| **Level 2** | Senior Acumatica Consultant | P1/P2 incidents; technical complexity; issues not resolved within SLA target |
| **Level 3** | APPSolve Account Manager | Client dissatisfaction; SLA breach; escalation on relationship grounds |
| **Level 4** | APPSolve Director / Practice Lead | Unresolved critical issue beyond Level 3; contractual breach |
| **Level 5** | Acumatica Global Support | Product defects; platform issues; Acumatica product team engagement |

### 5.2 Acumatica Global Support Integration

As an Acumatica Gold Partner, APPSolve has direct access to Acumatica's Global Support Portal. When a client issue is identified as an Acumatica product defect or platform limitation, APPSolve logs a case directly with Acumatica's Support team on the client's behalf, manages the case to resolution, and communicates progress to the client.

Clients benefit from APPSolve's Gold Partner status — faster case routing and direct escalation to Acumatica's product team when required.

### 5.3 Escalation Response Commitments

- Acknowledge escalation request: within 1 hour
- Level 3 (Account Manager) engaged: within 2 hours of escalation
- Recovery plan communicated to client: within 4 hours of escalation
- Formal post-incident review for P1 incidents: within 5 business days of resolution

---

## 6. Enhancement Delivery Process

The Enhancement Delivery Process governs changes to the Acumatica environment beyond break-fix support. This applies to configuration changes, new functionality, reporting additions, integration modifications, and any activity that requires development or system changes.

### 6.1 Enhancement Categories

| Category | Definition | Delivery Route |
|---|---|---|
| **Minor Configuration** | Parameter changes, form changes, report modifications within existing framework | Standard support ticket (Tier 2/3 SLA) |
| **Functional Enhancement** | New functionality within scope of existing Acumatica modules; new workflows, approvals, or processes | Enhancement request; scoped, costed, and scheduled separately |
| **Integration Change** | Modifications to existing integrations (PaySpace, banking, third-party) | Enhancement request; integration specialist assigned |
| **Custom Development** | New Acumatica customisation (DAC, graph extensions, API integration) | Formal change request; separate commercial engagement |

### 6.2 Enhancement Request Process

```
Enhancement Request → Impact Assessment (1-3 days) → Scope + Estimate → Client Approval → Scheduled Delivery → UAT → Deployment
```

All enhancements are deployed to the Acumatica test environment first and require client user acceptance testing (UAT) confirmation before production deployment.

### 6.3 Change Governance

A formal Change Advisory Board (CAB) meeting is held monthly (Tier 3) or quarterly (Tier 2) to review the enhancement pipeline, prioritise upcoming changes, and confirm deployment scheduling. Changes affecting business-critical processes require steering committee approval before scheduling.

---

## 7. Release Management

Acumatica releases major updates twice per year (typically March and September). APPSolve manages the release lifecycle on behalf of supported clients.

### 7.1 Release Process

| Stage | Activities |
|---|---|
| **Release Notification** | APPSolve notifies client of upcoming release, release notes summary, and impact assessment for configured modules |
| **Sandbox Testing** | APPSolve tests the new release in client sandbox environment; identifies breaking changes and regression risks |
| **Impact Communication** | Impact report provided to client; any configuration changes or customisation updates scoped and costed |
| **Client UAT** | Client super users conduct acceptance testing in sandbox environment |
| **Production Deployment** | Release deployed to production after UAT sign-off; scheduled during agreed maintenance window |
| **Post-Release Monitoring** | Hypercare-lite period (typically 1 week) with enhanced monitoring following each major release |

### 7.2 Patch and Minor Updates

Between major releases, Acumatica delivers patches and minor updates. APPSolve applies these during agreed maintenance windows (typically monthly) after internal regression testing. Clients are notified of all maintenance windows in advance.

---

## 8. Continuous Improvement Programme

APPSolve's Continuous Improvement Programme (Evolve Tier only) applies the APPSolve Continuous Improvement Model — a four-stage cycle of Analyse, Plan, Implement, and Measure — to the client's Acumatica environment on an ongoing basis.

### 8.1 Quarterly Business Reviews

APPSolve conducts Quarterly Business Reviews (QBRs) with each Tier 2 and Tier 3 client. QBR agenda:
- System health review (performance, data quality, error trends)
- Support ticket trend analysis (volume, types, resolution times)
- Enhancement pipeline review
- Upcoming release planning
- User adoption assessment
- Strategic roadmap discussion (what Acumatica capabilities are the client not yet using that would create value?)

### 8.2 System Health Reporting

Tier 3 clients receive monthly System Health Reports covering:
- Ticket volumes by category and priority
- SLA compliance metrics
- Enhancement delivery status
- Release management status
- Key risk items

### 8.3 Optimisation Reviews

Annually, APPSolve conducts an Optimisation Review — a structured assessment of how the client's Acumatica environment can be improved. This includes: unused module capabilities, data quality improvements, automation opportunities, integration enhancements, and reporting gaps. Recommendations are prioritised by business value and effort.

---

## 9. Support Team Composition

APPSolve's Acumatica support engagements are staffed by:
- **Account Manager** — primary relationship contact; non-technical; manages commercials and escalations
- **Senior Functional Consultant** — primary support lead; Acumatica-certified; functional resolution
- **Technical Consultant** — on-demand for development issues, customisation, and integration
- **Integration Specialist** — on-demand for PaySpace, banking, or third-party integration issues
- **Remote Support Centre** — 24x7 monitoring; P1 on-call alert management

Senior-only staffing applies across all Acumatica support engagements — no junior resources assigned to production support without senior oversight.

---

## 10. Evidence Summary

APPSolve's Acumatica support capability is demonstrated through the following active support relationships:

| Client | Scope | Reference Status |
|---|---|---|
| Interconnect Systems | Acumatica Field Services (post-implementation support) | **Referenceable** — letter registered 2026-06-14; AM approval required at each tender |
| HyDac | Acumatica Manufacturing ERP + BeBanking (post-implementation support) | **Referenceable** — AM approval required at each tender |
| DSSSA | Acumatica ERP (post-implementation support) | **Referenceable** — letter registered 2026-06-14; AM approval required at each tender |
| FuelU2 | Acumatica ERP (post-implementation support) | **Referenceable** — letter registered 2026-06-14; AM approval required at each tender |
| Maxiflex | Acumatica ERP (post-implementation support) | **Referenceable** — letter registered 2026-06-14; AM approval required at each tender |

**Pre-tender check PT-ACU-S01:** Confirm which of the above clients can be named for this specific tender before citing in support capability section.

---

## 11. Pre-Tender Checks

Before using this document in any external tender submission:

| Check | Reference |
|---|---|
| Confirm client referenceability for this specific tender | PT-ACU-S01 |
| Confirm SLA terms in Section 4.2 reflect current offering | PT-ACU-S02 |
| Section 12.2 (if added in future versions) — internal only | PT-ACU-S03 |
| Do not conflate with Oracle support (W2S1-004) or BeBanking support (W1S3-009) | Standing rule |
| BEE Level 3 confirmed (expires 2026-07-31) | Annual check |

---

## Section 17 — Approval Record

| Field | Value |
|---|---|
| Document ID | W5-ACU-001-ACU-SupportManagedServices |
| Title | Acumatica Support & Managed Services |
| Version | 1.0 |
| Wave | Wave 5 |
| Work Package | WP7 |
| Approved by | Hein Blignaut (BU Lead) |
| Approval date | 2026-06-14 |
| approved_for_reuse | **Yes** |
| Evidence basis | Interconnect Systems, HyDac, DSSSA, FuelU2, Maxiflex (all Tier 1 — active support relationships) |
| KB destination | `06_Capabilities/Acumatica/Support/W5-ACU-001-ACU-SupportManagedServices.md` |
| Next review | 2027-06-14 (annual) |

---

*W5-ACU-001 v1.0 — Approved 2026-06-14 by Hein Blignaut. WP7 Wave 5. Acumatica Support & Managed Services. Direct reuse in tenders after pre-tender checks PT-ACU-S01 through PT-ACU-S03.*
