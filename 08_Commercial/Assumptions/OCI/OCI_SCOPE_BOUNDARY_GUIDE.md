---
document_id: OCI-SCOPE-BOUNDARY-GUIDE
title: "OCI Infrastructure — Scope Boundary Guide"
version: "1.0"
status: "Approved"
approved_by: "Hein Blignaut (BU Lead)"
approved_date: "2026-06-16"
approval_ref: "WP11H-A"
created: "2026-06-16"
created_by: "WP11H — OCI Infrastructure Assumption Pack"
pack_code: OCI
---

# OCI Infrastructure — Scope Boundary Guide

**Purpose:** Provides practical guidance on where APPSolve's OCI scope ends and where client, Oracle, or third-party responsibility begins. Use this guide when reviewing proposals, responding to client scope queries, or raising Change Requests.

**How to use:** When a client raises a request or question during delivery, locate the closest scenario below to determine whether the item is In Scope, Out of Scope, or requires a Change Request.

---

## Scenario 1 — FastConnect Provisioning

**Scenario:** The client's network team requests that APPSolve arrange the FastConnect dedicated circuit to OCI.

**Boundary:**
- **APPSolve IN SCOPE:** FastConnect architecture design; OCI-side Virtual Circuit configuration; technical specifications handed to the FastConnect provider; integration testing once circuit is live.
- **CLIENT RESPONSIBILITY:** Selecting and contracting a FastConnect partner (BCX, Liquid, Vox, etc.); commercial agreement with the FastConnect partner; physical circuit installation; paying the FastConnect partner's monthly fee.
- **Key risk:** FastConnect lead times are 6–12 weeks. If not planned in the project schedule from the start, FastConnect will delay go-live.
- **Related assumption:** OCI-EXT-001, OCI-NET-003

---

## Scenario 2 — Security Audit / Pen Testing Request

**Scenario:** The client's CISO requests a penetration test of the OCI environment as part of project sign-off.

**Boundary:**
- **APPSolve IN SCOPE:** Providing architecture documentation to the client's pen test vendor; clarifying configuration details; coordinating Oracle's pen test notification (required before testing OCI infrastructure).
- **OUT OF SCOPE:** Conducting or managing the penetration test; engaging the pen test vendor; paying for pen test services.
- **Change Request trigger:** If APPSolve is asked to remediate pen test findings, this is a CR — findings that are design defects are included; findings that represent policy decisions or hardening beyond the agreed baseline are a CR.
- **Related assumption:** OCI-SEC-007

---

## Scenario 3 — Additional OCI Environments

**Scenario:** Mid-project, the client asks for a separate Performance Testing environment on OCI in addition to the agreed Dev, Test, and UAT environments.

**Boundary:**
- **APPSolve IN SCOPE:** Delivering the environments agreed in the SOW.
- **Change Request:** Any new OCI environment not in the SOW is a CR. This covers: Performance/Load Test, Training, Sandbox, Proof-of-Concept environments, and any additional environment for a subsidiary or business unit.
- **Effort note:** Environment provisioning from IaC is relatively fast (1–3 days) but the CR covers: Terraform module update, network config, IAM policy extension, budget alert addition, monitoring extension, and documentation update.
- **Related assumption:** OCI-GEN-001, OCI-LZ-002

---

## Scenario 4 — DR Region Activation

**Scenario:** A production incident occurs and the client asks APPSolve to activate the DR environment.

**Boundary:**
- **In a project delivery context (during DR test):** APPSolve leads the DR failover test and execution as scoped.
- **In an AMS Managed OCI context:** APPSolve follows the DR runbook and activates the DR environment per the AMS SOW.
- **NOT in scope (project delivery context, after acceptance sign-off):** Unplanned production DR activation after project close and before AMS SOW is in place. This is the client's responsibility or requires an emergency SOW.
- **Key risk:** DR activation without APPSolve AMS coverage must be executed by the client using the DR runbook provided. Clients must train their team on the runbook before accepting the project.
- **Related assumption:** OCI-DR-001 through OCI-DR-010

---

## Scenario 5 — Non-Oracle Workloads on OCI

**Scenario:** The client asks APPSolve to host a non-Oracle application (e.g., a Java microservice, a Python analytics tool, or a third-party SaaS connector) on the OCI infrastructure that APPSolve built.

**Boundary:**
- **APPSolve IN SCOPE:** Providing infrastructure (compute, network, storage) for the workloads named in the SOW.
- **OUT OF SCOPE:** Installing, configuring, or supporting non-Oracle application software unless explicitly named in the SOW.
- **Change Request trigger:** Hosting a new non-Oracle application on OCI is a CR. Effort depends on the application's infrastructure requirements.
- **Key message to client:** OCI is the platform; APPSolve delivers the OCI platform. What runs on that platform beyond the agreed Oracle workloads is the client's responsibility unless separately scoped.
- **Related assumption:** OCI-GEN-001, OCI-MW-008

---

## Scenario 6 — OCI Cost Optimisation Request

**Scenario:** Six months after go-live, the client asks APPSolve to review and reduce the OCI monthly bill.

**Boundary:**
- **In an AMS Managed OCI context:** OCI cost spike investigation and right-sizing recommendations are included as standard AMS service requests (see OCI-SUP-007). Cost optimisation review is included in the quarterly AMS review.
- **NOT in scope (project delivery, post-handover):** Cost optimisation advisory after project close and in the absence of an AMS SOW. This is a separately billable advisory engagement.
- **Note:** APPSolve provides right-sizing recommendations at project close and at the 30-day post-go-live review as standard. What the client does with those recommendations after the 30-day review is the client's responsibility.
- **Related assumption:** OCI-CST-003, OCI-PER-008, OCI-SUP-007

---

## Scenario 7 — OCI Patching Request

**Scenario:** The client's IT team asks APPSolve to apply Oracle Database patch bundles and OS patches to the production OCI environment.

**Boundary:**
- **In an AMS Managed OCI context:** OCI patching at the agreed cadence (BU-OCI-010, pending) is included in the AMS SOW. APPSolve prepares patch plans, tests in non-production, and executes in production during agreed maintenance windows.
- **NOT in scope (project delivery, post-handover):** Post-handover patching is the client's responsibility. APPSolve has provided a patching runbook; the client executes using it.
- **Emergency patching (Critical Security Patch Update):** If Oracle issues a Critical Security Patch Update requiring immediate patching, this is a CR in a non-AMS context. Under AMS, it is handled per the AMS emergency change procedure.
- **Related assumption:** OCI-DB-007, OCI-OPS-002

---

## Scenario 8 — Load / Performance Testing on OCI

**Scenario:** During UAT, the client's QA team wants to run load tests against the OCI production environment to validate performance before go-live.

**Boundary:**
- **APPSolve IN SCOPE:** Providing the OCI infrastructure environment; co-ordinating a maintenance window if production-equivalent testing is needed; advising on OCI-side performance metrics to monitor during the test.
- **OUT OF SCOPE:** Designing or executing the load test; procuring load test tooling (JMeter, Gatling, LoadRunner); writing test scripts; analysing application-level results.
- **Risk to flag:** Load testing on OCI can generate significant egress traffic, which incurs OCI costs. The client must factor egress costs into the load test budget.
- **Related assumption:** OCI-PER-002

---

## Scenario 9 — OS-Level Hardening Beyond Baseline

**Scenario:** The client's security team provides a hardening checklist with 200 OS-level controls (CIS Level 2, DISA STIG) and asks APPSolve to apply them all.

**Boundary:**
- **APPSolve IN SCOPE (baseline):** Oracle's standard OS hardening baseline applied to all compute instances as part of provisioning.
- **OUT OF SCOPE:** Additional hardening beyond the Oracle baseline (CIS Level 2, STIG, custom security policy controls).
- **Change Request trigger:** Applying a client-specific or regulatory hardening profile is a CR. Effort depends on the number of controls and the scope of testing required to validate each control.
- **Key message:** Hardening controls beyond the baseline are a specialised security advisory activity, not a standard infrastructure delivery item.
- **Related assumption:** OCI-CMP-004, OCI-SEC-001

---

## Scenario 10 — FinOps / Showback Implementation

**Scenario:** The client's CFO requests that OCI costs be allocated per business unit, with monthly chargeback reports to each BU cost centre.

**Boundary:**
- **APPSolve IN SCOPE (standard):** Standard OCI tagging (environment/cost centre/project/owner); OCI Cost Analysis dashboard; budget alerts per compartment.
- **OUT OF SCOPE:** FinOps programme design; showback/chargeback model development; automated cost allocation reports; integration of OCI costs into the client's ERP or finance system.
- **Change Request trigger:** Any FinOps implementation beyond standard tagging and OCI dashboard is a CR or a separate advisory engagement.
- **Related assumption:** OCI-CST-007, OCI-LZ-005

---

## Scenario 11 — Customer-Managed Encryption Key (CMEK) Request

**Scenario:** The client's security team requires that all OCI data be encrypted with keys the client manages, not Oracle-managed keys.

**Boundary:**
- **APPSolve IN SCOPE (if in SOW):** OCI Vault provisioning; CMEK key creation and policy assignment; applying CMEK to Block Volumes, Object Storage buckets, and DB Systems. CMEK is included if explicitly stated in the SOW.
- **OUT OF SCOPE (if not in SOW):** CMEK was not scoped and is now a CR. CMEK requires: OCI Vault setup, key rotation policy design, key management operational procedures, and integration testing.
- **Key risk for CMEK:** If the client loses or deletes the master encryption key, all CMEK-encrypted data becomes permanently unrecoverable. APPSolve documents this risk prominently in CMEK configurations.
- **Related assumption:** OCI-SEC-004, OCI-STO-008

---

## Scenario 12 — Workload Outside South Africa Region

**Scenario:** A client with operations in Europe asks APPSolve to host the OCI environment in the Frankfurt region instead of Johannesburg.

**Boundary:**
- **APPSolve IN SCOPE:** Delivering OCI infrastructure in whatever region(s) the client specifies. Non-SA regions are a valid deployment target.
- **Change impact:** Non-South Africa regions may have different Oracle pricing, different service availability (not all OCI services are available in all regions), higher network latency for SA-based users, and potential data residency/POPIA implications.
- **Client responsibility:** Data residency compliance decision; selecting the correct region for their legal/regulatory obligations; accepting latency impact.
- **APPSolve action:** Update the design to specify the agreed region; flag POPIA cross-border data transfer obligations in the project record.
- **Related assumption:** OCI-GEN-004, OCI-SEC-009, OCI-EXT-007

---

## Quick Reference — In Scope vs Out of Scope

| Item | In Scope | Out of Scope |
|---|---|---|
| OCI VCN, subnets, routing, NSGs | Yes | |
| IPSec VPN configuration (OCI side) | Yes | |
| FastConnect architecture and OCI Virtual Circuit | Yes | FastConnect partner contract and physical circuit |
| OCI Landing Zone (Terraform/ORM) | Yes | |
| OCI IAM groups, policies, Identity Domains | Yes | PAM tooling integration |
| OCI Bastion Service | Yes | |
| Cloud Guard, Security Zones, Security Advisor | Yes | |
| Oracle Linux OS provisioning | Yes | |
| OS hardening (Oracle baseline) | Yes | Advanced hardening (CIS L2, STIG) |
| Block Volume, Object Storage, FSS provisioning | Yes | |
| Oracle DB System (VM DB) provisioning | Yes | DBA services (tuning, schema) |
| Data Guard HA setup | Yes | |
| Oracle GoldenGate | Only if in SOW | |
| OIC / APEX / WebLogic provisioning | Yes | Integration flows, APEX content |
| OCI Monitoring dashboards and alerting | Yes | Third-party monitoring tool integration |
| OCI Backup configuration | Yes | Third-party backup tools |
| DR design and Pilot Light setup | Only if in SOW | Active-Active DR (always separately priced) |
| Migration Plan and execution | Only if in SOW | Third-party app migration |
| Post-migration performance validation (30-day) | Yes | |
| Operational handover training | Yes | Advanced OCI certification training |
| Performance testing (load/stress) | Out of scope | |
| Penetration testing | Out of scope | |
| FinOps / showback / chargeback | Out of scope | |
| OCI Reserved Instance purchasing | Recommendation only | Client purchases directly with Oracle |
| OCI tenancy costs | Out of scope (client pays Oracle) | |
| Oracle support subscription | Out of scope (client relationship) | |
| Third-party middleware on OCI | Out of scope | |
| Third-party network appliances on OCI | Out of scope | |

---

*OCI Scope Boundary Guide v1.0 | WP11H + WP11H-A | 2026-06-16*
*12 scenarios | Status: Approved — Hein Blignaut (BU Lead) 2026-06-16*
