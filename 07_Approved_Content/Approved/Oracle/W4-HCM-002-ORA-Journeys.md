---
document_id: W4-HCM-002-ORA-Journeys
title: "Oracle Journeys — Employee Self-Service & Guided Workflows Capability Statement"
version: "1.0"
status: "Approved"
review_status: "Approved"
approved_for_reuse: "Yes"
lifecycle_status: APPROVED
approved_date: "2026-06-14"
approved_by: "Hein Blignaut (BU Lead)"
business_unit: "Oracle"
wave: "4"
deliverable: "W4-HCM-002"
created: "2026-06-14"
created_by: "Claude (AI — Wave 4 W4-HCM-002 extraction)"
source_document: "HIST-007 (Hollywood Bets V5.0 Accepted Proposal — primary; Journeys confirmed in HB Phase 1 Global HR scope — BU Lead decision 2026-06-14); HIST-006 (SAA RFP Section 2 — Journeys module listed — SAA NEVER NAMED Rule 21.1); HIST-014 (CCBA Solution V2.0 — Journeys supporting — CCBA NEVER NAMED)"
source_status: "Tier 1 Confirmed Delivery (HIST-007 — Hollywood Bets; BU Lead confirmed 2026-06-14); Tier 2 Platform Capability (HIST-006, HIST-014 — internal corroboration only)"
prereq_statement: "W3S1-001-ORA-HCMCore (Oracle HCM Core — Global HR is the mandatory foundation for Journeys; Journeys is delivered within the Oracle Fusion HCM platform)"
kb_destination: "06_Capabilities/Oracle/Oracle_HCM/"
tags: "Oracle,HCM,Journeys,Guided Journeys,Employee Self-Service,Onboarding,Life Events,HR Automation,Oracle Fusion HCM"
---

---

# Oracle Journeys — Employee Self-Service & Guided Workflows

**Capability Statement | APPSolve | Oracle Business Unit**
*Document ID: W4-HCM-002-ORA-Journeys | Version: 1.0 | Wave 4 | Approved 2026-06-14*

---

## Section 1: Statement of Capability

APPSolve designs, configures, and implements Oracle Journeys — Oracle's guided employee self-service framework embedded within Oracle Fusion HCM. Oracle Journeys enables HR teams to build structured, personalised task checklists and guided workflows for employees navigating significant employment events and HR processes.

APPSolve delivers Oracle Journeys as an integrated component of Oracle Fusion HCM implementations, enabling organisations to standardise HR processes, reduce manual intervention, and create consistent, compliant employee experiences across the full employment lifecycle.

> **Confirmed implementation:** Oracle Journeys was confirmed as a delivered component within the Hollywood Bets Oracle Fusion HCM implementation (BU Lead decision 2026-06-14).

| Capability Area | Coverage | APPSolve Positioning |
|---|---|---|
| **Onboarding Journeys** | New employee onboarding task checklists — pre-hire, day-one, and first-90-days workflows | **Confirmed delivery capability** — standardised onboarding automation within Oracle HCM |
| **Life Event Journeys** | Employee life events — marriage, parental leave, relocation, role changes, retirement | **Confirmed delivery capability** — life event orchestration within Oracle HCM framework |
| **Offboarding Journeys** | Structured employee exit workflows — IT access revocation, equipment return, exit interviews | **Confirmed delivery capability** — compliant exit process automation |
| **HR Process Automation** | Policy acknowledgements, mandatory compliance tasks, document submission workflows | **Confirmed delivery capability** — HR policy and compliance workflow automation |
| **Personalised Employee Experience** | Role-based journey personalisation; manager and employee dual-task assignment | **Confirmed delivery capability** — audience segmentation and task personalisation |
| **Self-Service Portal Integration** | Employee self-service via Oracle Fusion HCM Me module | **Confirmed delivery capability** — integrated within Oracle HCM standard UX |

---

## Section 2: Product Architecture

### 2.1 Oracle Journeys Framework

Oracle Journeys is a standard Oracle Fusion HCM module available within the Oracle HCM Cloud subscription. It operates as a configured workflow engine within Oracle HCM, with no separate licensing requirement.

```
Oracle Journeys
  ├── Journey Templates (configured by APPSolve)
  │   ├── Onboarding (pre-hire → day 1 → 90 days)
  │   ├── Life Events (parental, relocation, status changes)
  │   ├── Offboarding (exit process)
  │   └── Custom HR Processes (compliance, acknowledgements)
  ├── Task Types
  │   ├── Oracle HCM native tasks (profile updates, document upload)
  │   ├── External tasks (manual completion acknowledgements)
  │   ├── Links to external systems (IT provisioning, facilities)
  │   └── DocuSign / e-signature tasks (where configured)
  ├── Assignment Rules
  │   ├── Employee (self-service)
  │   ├── Manager (manager-assigned tasks)
  │   └── HR / Specialist (HR team tasks)
  └── Analytics
      ├── Journey completion tracking
      ├── Task overdue alerting
      └── Compliance dashboards
```

### 2.2 Integration with Oracle HCM Core

Journeys is natively embedded in Oracle HCM and does not require separate integration configuration. Triggers include:
- New hire events from Oracle Global HR (W3S1-001)
- Life event triggers from Oracle HCM benefits and HR modules
- Absence events from Oracle Workforce Management (W3S1-007)
- Recruiting hire events from Oracle Recruiting Cloud (W3S1-003)

---

## Section 3: Source Mapping

| Source | HIST ID | Evidence Type | Applicable Sections | Usage Restrictions |
|---|---|---|---|---|
| Hollywood Bets V5.0 Accepted Proposal | HIST-007 | Tier 1 Confirmed Delivery | Phase 1 Global HR scope — Journeys confirmed as deliverable (BU Lead decision 2026-06-14) | Account manager approval at each tender submission |
| SAA Oracle Fusion HCM RFP Response | HIST-006 | Tier 2 Platform Capability (internal only) | Section 2 — Journeys module listed in scope | **SAA NEVER NAMED — Rule 21.1 (Aviation PROHIBITED)** |
| CCBA HCM Solution V2.0 | HIST-014 | Tier 2 Platform Capability (internal only) | Journeys listed as HCM module | **CCBA NEVER NAMED — HIST-014 restriction** |

---

## Section 4: Evidence Classification

| Field | Value |
|---|---|
| **Evidence Tier** | **Tier 1 — Confirmed Delivery** |
| **Primary Evidence** | Hollywood Bets Oracle Fusion HCM implementation — Journeys confirmed as Phase 1 Global HR deliverable (BU Lead decision 2026-06-14; HIST-007) |
| **Corroborative Evidence** | HIST-006 (SAA — internal); HIST-014 (CCBA — internal) |
| **Named Reference** | Hollywood Bets — subject to account manager approval at each tender submission. No signed reference letter registered in KB as of 2026-06-14. |
| **Sector** | Retail / Gaming (Hollywood Bets ~7,000 users); applicable across all Oracle HCM sectors |
| **Restriction Summary** | SAA never named (Rule 21.1); CCBA never named (HIST-014); DFA never named (Rule 21.4); Redpath Mining not referenceable (Rule 21.5) |

---

## Section 5: Approved and Prohibited Wording

### Approved Wording

> "APPSolve configures and implements Oracle Journeys within Oracle Fusion HCM, enabling organisations to deliver structured, guided workflows for employee onboarding, life events, offboarding, and HR compliance processes."

> "APPSolve has delivered Oracle Journeys as an integrated component of Oracle Fusion HCM implementations, providing employees with personalised, guided self-service workflows across the full employment lifecycle."

> "Oracle Journeys, implemented by APPSolve, enables HR teams to automate task orchestration for significant employment events — reducing manual HR workload while ensuring consistent, compliant employee experiences."

### Prohibited Wording

- Do NOT reference SAA as a client, example, or implementation in any Journeys-related content (Rule 21.1)
- Do NOT reference CCBA as a client or example (HIST-014)
- Do NOT reference DFA as a client or example (Rule 21.4)
- Do NOT describe Journeys as a standalone product requiring separate Oracle licensing — it is included within the Oracle HCM Cloud subscription
- Do NOT conflate Oracle Journeys with Oracle Digital Assistant (ODA) — Journeys is a workflow tool; ODA is conversational AI
- Do NOT conflate Oracle Journeys with Oracle OAX/Experience Design Studio — different toolsets

---

## Section 6: Pre-Tender Validation Checks

Before including this capability statement in any tender submission, confirm all of the following:

- [ ] **PT-W4H2-001:** Hollywood Bets account manager approval obtained for this specific tender submission
- [ ] **PT-W4H2-002:** Client is NOT aviation sector — if aviation, Rule 21.1 applies; review all evidence references
- [ ] **PT-W4H2-003:** Confirm tender does not require a signed customer reference letter for Journeys specifically — if yes, HB letter must be obtained before submission
- [ ] **PT-W4H2-004:** Review tender for specific Journeys use-case requirements — confirm HB implementation scope covers the use cases being claimed
- [ ] **PT-W4H2-005:** BEE certificate validity confirmed (expires 2026-07-31)

---

## Section 7: Named Reference Controls

| Client | Reference Status | Permitted Use | Restrictions |
|---|---|---|---|
| **Hollywood Bets** | Referenceable — pending account manager approval | Named reference for Oracle Journeys capability (BU Lead confirmed Journeys in HB scope) | Account manager approval required at each tender. No signed letter in KB. |
| SAA | NEVER NAMED | Internal evidence only | **Rule 21.1 — Aviation PROHIBITED permanently** |
| CCBA | NEVER NAMED | Internal evidence only | **HIST-014 restriction — CCBA never named** |
| DFA | NEVER NAMED | Internal evidence only | **Rule 21.4 — permanent** |
| Redpath Mining | NOT REFERENCEABLE | Active Pipeline only | **Rule 21.5 — not referenceable until go-live + BU Lead approval** |

---

## Section 8: Product Boundary Controls

| Product | Relationship | Boundary Rule |
|---|---|---|
| **Oracle Journeys** | THIS STATEMENT | Guided workflow framework within Oracle HCM — task checklists, lifecycle event automation |
| **Oracle Digital Assistant (ODA)** | Different product | ODA is conversational AI for HR queries. Journeys is guided task workflow. Do NOT conflate. |
| **Oracle Application Extension (OAX)** | Different product | OAX is a UI configuration tool for Fusion pages. Journeys uses standard HCM UI. Do NOT conflate. |
| **Oracle HCM Core (W3S1-001)** | Prerequisite | Journeys is embedded within Oracle HCM. HCM Core (W3S1-001) is the mandatory prerequisite. |
| **Oracle Workforce Management (W3S1-007)** | Related | Absence events can trigger Journeys. Journeys ≠ absence management. |
| **Oracle Recruiting Cloud (W3S1-003)** | Related | Hire events can trigger onboarding Journeys. Journeys ≠ recruiting. |

---

## Section 9: Extraction Log

| Field | Value |
|---|---|
| **Wave** | 4 |
| **Extraction Date** | 2026-06-14 |
| **Extractor** | Claude (AI — Wave 4 extraction authorised by BU Lead 2026-06-14) |
| **BU Lead Decision** | W4-HCM-002 Oracle Journeys — Confirmed delivery; eligible for Wave 4 extraction (BU Lead decision 2026-06-14) |
| **Primary Source** | HIST-007 (Hollywood Bets V5.0 Accepted Proposal) |
| **Evidence Tier at Extraction** | Tier 1 |
| **Status** | **Approved — approved_for_reuse: Yes (Hein Blignaut, BU Lead, 2026-06-14)** |
| **Next Action** | Approved 2026-06-14. Apply pre-tender validation checks (PT-W4H2-001 through PT-W4H2-005) before use in any tender. |
| **Promotion Requirement** | BU Lead set approved_for_reuse: Yes (Hein Blignaut, 2026-06-14). Wave 4 promotion complete. |

---

*W4-HCM-002-ORA-Journeys.md v1.0 — Approved 2026-06-14 by Hein Blignaut (BU Lead). approved_for_reuse: Yes.*
