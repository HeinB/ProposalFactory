---
document_id: OCI-GAP-REPORT
title: "OCI Infrastructure Assumption Pack — Gap Report"
version: "1.0"
status: "Approved — BU Lead Review Complete 2026-06-16"
created: "2026-06-16"
created_by: "WP11H — OCI Infrastructure Assumption Pack"
updated: "2026-06-16"
updated_by: "WP11H-A — BU Lead Decision Application"
pack_code: OCI
---

# OCI Infrastructure Assumption Pack — Gap Report

**Purpose:** Identifies gaps in the OCI assumption pack that require BU Lead decisions, additional research, or future pack development before the OCI pack can be used in live proposals without qualification.

**As at:** 2026-06-16
**Total gaps identified:** 12 (13 originally identified; GAP-OCI-C02 removed — concept invalid)
**BU decisions required:** 0 (9 APPROVED 2026-06-16; BU-OCI-007 WITHDRAWN — concept does not exist)
**Research gaps:** 3

---

## Gap Summary

| Severity | Count | Description |
|---|---|---|
| CRITICAL | 1 | GAP-OCI-C01 resolved (BU-OCI-008 APPROVED); GAP-OCI-C02 removed (invalid concept) |
| HIGH | 5 | All 5 HIGH BU decisions APPROVED 2026-06-16 |
| MEDIUM | 6 | 3 BU decisions APPROVED; 3 remain as future research/pack development items |
| **Total** | **12** | |

---

## CRITICAL Gaps

### GAP-OCI-C01 — OCI Cost Estimate Disclaimer Language (BU-OCI-008) — RESOLVED

**Severity:** CRITICAL → **RESOLVED 2026-06-16**
**Pack reference:** OCI-CST-002
**Issue:** APPSolve provides indicative OCI cost estimates in proposals. Without an approved disclaimer, these estimates carry a risk of being treated as contractual commitments.
**Resolution applied:** BU Lead approved mandatory disclaimer wording on 2026-06-16. Wording applied verbatim to OCI-CST-002. All future OCI proposals must include this wording.
**BU decision:** BU-OCI-008 — **APPROVED**

---


## HIGH Gaps

### GAP-OCI-H01 — Oracle DB Licensing Default (BU-OCI-003)

**Severity:** HIGH
**Pack reference:** OCI-DB-002
**Issue:** OCI DB proposals require a licensing position: BYOL (client has existing Oracle licences) or License Included (subscription). Using the wrong assumption creates a significant pricing error — BYOL proposals may underprice for clients who don't hold Oracle licences; LI proposals may overprice BYOL clients. There is no current APPSolve standard position.
**Consequence if unresolved:** Inconsistent and potentially incorrect OCI DB costing across proposals.
**Resolution required:** BU Lead to set a default licensing position and document exceptions.
**Owner:** Oracle BU Lead
**BU decision:** BU-OCI-003

---

### GAP-OCI-H02 — FastConnect vs VPN Threshold (BU-OCI-002)

**Severity:** HIGH
**Pack reference:** OCI-NET-003
**Issue:** There is no defined threshold for when APPSolve recommends FastConnect instead of IPSec VPN. Without this, consultants will make inconsistent recommendations. FastConnect can be 10–20x more expensive than VPN and changes the network design significantly.
**Consequence if unresolved:** Some proposals may under-scope network connectivity (VPN where FastConnect is needed), leading to performance problems in production.
**Resolution required:** BU Lead to set threshold criteria (e.g., user count, bandwidth requirement, SLA tier).
**Owner:** Oracle BU Lead / OCI Architect
**BU decision:** BU-OCI-002

---

### GAP-OCI-H03 — Non-Production Environment Count Standard (BU-OCI-009)

**Severity:** HIGH
**Pack reference:** OCI-GEN-005
**Issue:** The number of non-production environments (1, 2, or 3) directly affects OCI cost estimates — a three-environment model costs approximately 3x more than a single combined environment. Without a standard, proposals will be inconsistent and comparisons across bids will be unreliable.
**Consequence if unresolved:** Inconsistent non-production sizing across OCI proposals; client expectation mismatches.
**Resolution required:** BU Lead to set a standard non-production environment count (with defined override criteria for larger engagements).
**Owner:** Oracle BU Lead
**BU decision:** BU-OCI-009

---

### GAP-OCI-H04 — OCI DBA AMS Scope Boundary (BU-OCI-005)

**Severity:** HIGH
**Pack reference:** OCI-DB-008
**Issue:** When APPSolve provides AMS for an OCI-hosted Oracle database, it is unclear whether OCI DBA work (DB patching, performance tuning, AWR analysis) falls within the OCI AMS pack or the ERP AMS pack. This boundary ambiguity will cause scoping inconsistencies and may result in either a gap (no one covers OCI DBA) or a double-count across packs.
**Consequence if unresolved:** AMS proposals for OCI-hosted databases will have undefined DBA scope, leading to post-contract disputes.
**Resolution required:** BU Lead to define the scope boundary between OCI AMS and ERP/HCM AMS for DBA-type activities.
**Owner:** Oracle BU Lead
**BU decision:** BU-OCI-005

---

### GAP-OCI-H05 — OCI Patching Cadence in AMS (BU-OCI-010)

**Severity:** HIGH
**Pack reference:** OCI-OPS-002
**Issue:** AMS Managed OCI engagements require a defined patching cadence to estimate monthly effort. Monthly patching requires approximately 4x the effort of quarterly patching. Without a defined cadence, AMS OCI proposals cannot be reliably priced.
**Consequence if unresolved:** OCI AMS proposals will have unquantifiable patching effort.
**Resolution required:** BU Lead to set a default patching cadence for OCI AMS engagements.
**Owner:** Oracle BU Lead
**BU decision:** BU-OCI-010

---

## MEDIUM Gaps

### GAP-OCI-M01 — OCI Tenancy Provisioning Service Scope (BU-OCI-001)

**Severity:** MEDIUM
**Pack reference:** OCI-GEN-003
**Issue:** New OCI clients need to create an OCI tenancy. It is unclear whether APPSolve assists with this as a standard service (included or billable) or whether clients are expected to self-provision. Inconsistent handling creates client experience variation.
**Resolution required:** BU Lead to define whether tenancy provisioning assistance is included, billable, or client self-serve.
**Owner:** Oracle BU Lead
**BU decision:** BU-OCI-001

---

### GAP-OCI-M02 — Pilot Light DR Pricing Status (BU-OCI-004)

**Severity:** MEDIUM
**Pack reference:** OCI-DR-002
**Issue:** Pilot Light DR is the most common DR approach for OCI. It is unclear whether this is offered as a standard "OCI with DR" engagement profile or always requires separate pricing. Without consistency, DR proposals will vary.
**Resolution required:** BU Lead to confirm whether Pilot Light DR is a standard engagement variant (with a defined engagement profile) or always a separately priced option.
**Owner:** Oracle BU Lead
**BU decision:** BU-OCI-004

---

### GAP-OCI-M03 — EBS on OCI Addendum Pack (BU-OCI-006)

**Severity:** MEDIUM
**Pack reference:** OCI-EXT-010
**Issue:** EBS on OCI has specific assumptions beyond the generic OCI pack (EBS Cloud Manager, EBS-specific patching, EBS DB version certification, EBS storage layout, Rapid Clone, AD integration specifics). The current OCI pack touches EBS briefly but does not cover EBS-specific OCI deployment assumptions in depth.
**Resolution required:** BU Lead to decide whether EBS-on-OCI requires a separate addendum assumption pack or whether the ERP pack + OCI pack together are sufficient.
**Owner:** Oracle BU Lead (ERP BU)
**BU decision:** BU-OCI-006

---

### GAP-OCI-M04 — OCI Security Standards Beyond CIS Level 1

**Severity:** MEDIUM
**Pack reference:** OCI-SEC-001
**Issue:** South African financial services clients (banks, insurance companies) increasingly require compliance with SARB-aligned security controls, ISO 27001, or PCI-DSS. The current OCI pack's baseline is CIS Level 1 only. There is no defined APPSolve OCI security pack for regulated industries.
**Resolution required:** Future work item — develop an OCI Security Addendum for regulated-industry clients. Not a BU decision; a future pack development item (OAR-D type action).
**Owner:** Oracle BU Lead / Security Specialist
**Future pack:** OCI Security Addendum (not yet created)

---

### GAP-OCI-M05 — OCI Exadata Cloud Service Assumptions

**Severity:** MEDIUM
**Pack reference:** OCI-DB-001
**Issue:** Exadata Cloud Service (ExaCS) is a significant OCI workload for high-performance EBS and Oracle Database. The current OCI pack covers VM DB Systems but does not cover ExaCS-specific assumptions (shape selection, storage cell configuration, Exadata patching, ExaCS licensing, minimum commit periods).
**Resolution required:** Future work item — develop OCI-DB addendum for ExaCS if APPSolve expects ExaCS proposals. Not a current blocker for standard VM DB System proposals.
**Owner:** Oracle BU Lead / OCI DBA
**Future pack:** ExaCS Addendum (if required)

---

### GAP-OCI-M06 — OCI for Oracle Analytics Cloud (OAC) Depth

**Severity:** MEDIUM
**Pack reference:** OCI-MW-005
**Issue:** The current pack covers OAC provisioning and network access. It does not cover OAC-specific assumptions: OAC instance sizing (OCPU count), OAC Private Access Channel configuration, OAC connection to on-premise data sources, OAC snapshot/backup, and OAC upgrade impact on custom content. An OAC proposal using only the OCI pack will be under-assumed.
**Resolution required:** Future work item — develop an OAC assumption section (possibly as an Analytics pack addendum). Recommend treating as a gap when OAC is in scope and documenting explicitly in the proposal that OAC-specific assumptions are subject to BU Lead review.
**Owner:** Oracle BU Lead (Analytics)
**Future pack:** OAC Addendum or Analytics Pack (not yet created)

---

## BU Decision Summary

All BU decisions reviewed and resolved 2026-06-16 (WP11H-A).

| Decision ID | Description | Severity | Status |
|---|---|---|---|
| BU-OCI-001 | OCI tenancy provisioning service scope | MEDIUM | **APPROVED 2026-06-16** |
| BU-OCI-002 | FastConnect vs IPSec VPN threshold | HIGH | **APPROVED 2026-06-16** |
| BU-OCI-003 | Oracle DB licensing default (BYOL vs LI) | HIGH | **APPROVED 2026-06-16** |
| BU-OCI-004 | Pilot Light DR pricing status | MEDIUM | **APPROVED 2026-06-16** |
| BU-OCI-005 | OCI DBA AMS scope boundary | HIGH | **APPROVED 2026-06-16** |
| BU-OCI-006 | EBS on OCI addendum pack decision | MEDIUM | **APPROVED 2026-06-16** |
| BU-OCI-007 | BeBanking OCI hosting cost responsibility | — | **WITHDRAWN — concept does not exist in APPSolve's operating model** |
| BU-OCI-008 | OCI cost estimate disclaimer language | CRITICAL | **APPROVED 2026-06-16** |
| BU-OCI-009 | Non-production environment count standard | HIGH | **APPROVED 2026-06-16** |
| BU-OCI-010 | OCI patching cadence in AMS | HIGH | **APPROVED 2026-06-16** |

---

## Research Gaps (Not BU Decisions)

| Gap ID | Description | Recommended Action |
|---|---|---|
| GAP-OCI-M04 | OCI Security Addendum for regulated industries | Create future OCI Security pack for SARB / ISO 27001 / PCI-DSS clients |
| GAP-OCI-M05 | Exadata Cloud Service assumptions | Create ExaCS addendum if ExaCS proposals expected |
| GAP-OCI-M06 | Oracle Analytics Cloud depth | Develop OAC assumptions in Analytics Pack or as OCI addendum |

---

*OCI Gap Report v1.0 | WP11H + WP11H-A | 2026-06-16*
*12 gaps identified | 9 BU decisions APPROVED; BU-OCI-007 WITHDRAWN | 3 research gaps remain*
