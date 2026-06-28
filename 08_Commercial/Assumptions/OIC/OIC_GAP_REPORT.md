---
document_id: OIC-GAP-REPORT
title: "OIC Assumptions Pack — Gap Report and Tender Readiness Assessment"
version: "1.0"
created: "2026-06-15"
created_by: "WP11C — Oracle Integration Cloud Assumptions Pack"
status: "Active"
applies_to: "OIC_ASSUMPTIONS_V1.md | OIC_ASSUMPTION_REGISTER.csv"
---

# OIC Assumptions Pack — Gap Report

This document identifies gaps in APPSolve's current OIC commercial, governance, and delivery assets — gaps that expose the business to scope disputes, estimation errors, or delivery risk in OIC engagements. Each gap is rated by severity and assigned a recommended action.

---

## 1. Executive Summary

| Category | Count |
|---|---|
| Critical Gaps (immediate action) | 3 |
| High Gaps (resolve before next OIC tender) | 5 |
| Medium Gaps (resolve within 90 days) | 5 |
| Low Gaps (roadmap items) | 4 |
| Total Gaps | 17 |

---

## 2. Critical Gaps

### GAP-OIC-001 — Integration Complexity Tier Model Not Documented

**Severity:** CRITICAL  
**Description:** APPSolve does not have a documented, BU-Lead-approved complexity tier model for OIC integrations. OIC-CON-006 in the assumptions pack acknowledges three tiers (Simple / Standard / Complex) but the definitions are pending BU-OIC-005 confirmation. Without an agreed tier model, estimates are produced ad hoc and cannot be defended in scope disputes.  
**Commercial risk:** Clients dispute that a "simple" integration was priced correctly, or that a complex integration should have been in the same tier as a simple one. Estimation methodology cannot be explained or audited.  
**Recommended action:** BU Lead defines Simple / Standard / Complex with specific criteria (trigger type, transformation complexity, number of code-set lookups, authentication complexity, payload size threshold). Document in `OIC_IMPLEMENTATION_PATTERNS.md` Section 6 and resolve BU-OIC-005.  
**Owner:** Oracle BU Lead  
**Target:** Before next OIC SOW is issued

---

### GAP-OIC-002 — No OIC Effort Rate Card or Estimate Template

**Severity:** CRITICAL  
**Description:** There is no standardised OIC effort rate card (e.g., Simple integration = X days; Standard = Y days; Complex = Z days) or OIC estimate template. Each OIC estimate is produced from scratch, leading to inconsistency between bids and over/under-pricing.  
**Commercial risk:** Two bid managers produce materially different estimates for the same integration scope. One APPSolve project is profitable; the next identical scope is a loss. No basis for defending estimates to clients.  
**Recommended action:** Create `OIC_EFFORT_RATE_CARD.md` with effort by tier and by phase (design / build / SIT / UAT support / cutover). Include accelerator discounts per W4-INT-001. Tie to complexity tier model (GAP-OIC-001).  
**Owner:** Oracle BU Lead + Delivery Lead  
**Target:** Before next OIC tender

---

### GAP-OIC-003 — No Standard Integration Inventory Template

**Severity:** CRITICAL  
**Description:** OIC-SCP-003 requires a signed Integration Inventory as the authoritative scope document, but no standard Integration Inventory template exists in the KB. Bid managers and project managers produce different versions with different columns and different levels of detail.  
**Commercial risk:** Integration Inventories omit key fields (frequency, trigger mechanism, payload direction) that become scope dispute points. Different project teams capture different levels of detail — leading to inconsistent scope control.  
**Recommended action:** Create `INTEGRATION_INVENTORY_TEMPLATE.csv` with mandatory columns: Integration_ID, Source_System, Target_System, Direction, Trigger_Type, Frequency, Estimated_Volume, Protocol, Authentication_Type, Complexity_Tier, Accelerator_Applicable, Status. Store in `08_Commercial/Templates/OIC/`.  
**Owner:** Oracle Delivery Lead  
**Target:** Before next OIC project kickoff

---

## 3. High Gaps

### GAP-OIC-004 — W4-INT-001 Accelerator Catalogue Not Linked to Assumptions Pack

**Severity:** HIGH  
**Description:** OIC-DES-007 references `W4-INT-001-ORA-OICAccelerators.md` but the assumptions pack does not specify which accelerators are available, their effort reduction, or their applicable integration patterns. BU-OIC-006 flags this as a pending BU Lead decision.  
**Commercial risk:** Estimates include accelerator discounts for patterns that are not yet production-ready, or fail to include discounts where an accelerator does exist — both resulting in pricing errors.  
**Recommended action:** BU Lead reviews W4-INT-001 and confirms: (a) which accelerators are production-ready; (b) effort reduction by tier per accelerator; (c) applicable integration scenarios. Update `OIC_IMPLEMENTATION_PATTERNS.md` Pattern Library with accelerator status.  
**Owner:** Oracle BU Lead  
**Target:** Resolve BU-OIC-006 in next BU Lead review cycle

---

### GAP-OIC-005 — No Mapping Specification Template

**Severity:** HIGH  
**Description:** OIC-MAP-002 requires APPSolve to produce a Mapping Specification per integration, but no standard template exists. Each consultant produces a different format, making it impossible to enforce sign-off consistency or compare mapping documents across projects.  
**Commercial risk:** Mapping Specifications without consistent structure are harder to get signed off, easier to dispute later, and harder to hand over to other consultants mid-project.  
**Recommended action:** Create `MAPPING_SPECIFICATION_TEMPLATE.xlsx` with tabs: Integration Overview, Field Mapping (source field / target field / transformation rule / default / lookup table reference), Code Set Lookups, Sign-off Record. Store in `08_Commercial/Templates/OIC/`.  
**Owner:** Oracle Delivery Lead  
**Target:** Within 30 days

---

### GAP-OIC-006 — OIC TDD (Technical Design Document) Template Not Available

**Severity:** HIGH  
**Description:** OIC-DES-004 requires a Technical Design Document per integration, but no standard TDD template exists in the KB. Consultants produce ad hoc design documents or adapt templates from previous projects.  
**Commercial risk:** Incomplete TDDs lead to build decisions being made without client sign-off, creating scope disputes at UAT when the build does not match unstated client expectations.  
**Recommended action:** Create `OIC_TDD_TEMPLATE.md` covering: Integration Overview, Source System Details, Target System Details, Connection Design, Trigger and Schedule, Payload Schema (request/response), Transformation Logic, Error Handling Approach, Retry Configuration, Security Configuration, Monitoring Setup. Store in `08_Commercial/Templates/OIC/`.  
**Owner:** Oracle Delivery Lead  
**Target:** Within 30 days

---

### GAP-OIC-007 — No Published OIC Reference Engagement

**Severity:** HIGH  
**Description:** APPSolve has multiple OIC implementations in production (Hollywood Bets HCM↔PaySpace bidirectional integration confirmed in W3S1-009; W4-INT-001 accelerators from production engagements) but no structured OIC reference case exists for tender use.  
**Commercial risk:** OIC proposals cannot cite a completed OIC engagement with named client, integration count, and business outcome — weakening competitive positioning against MuleSoft or Tibco specialists.  
**Recommended action:** Create a reference engagement record for the Hollywood Bets OIC implementation (HCM↔PaySpace bidirectional, OIC monitoring, production go-live July 2025). Register in `00_Governance/REFERENCE_MASTER.csv` as an OIC reference. Confirm anonymisation rules (Hollywood Bets AM approval required per W3S1-009 governance constraint).  
**Owner:** Oracle BU Lead + Account Manager  
**Target:** Before next OIC-heavy tender

---

### GAP-OIC-008 — SFTP Server Ownership Not Consistently Addressed in Previous Tenders

**Severity:** HIGH  
**Description:** OIC-DES-005 assumes SFTP as the fallback integration method and OIC-END-002 requires the client to provide SFTP connection details. However, APPSolve has historically been asked to provision SFTP servers for clients who do not have an SFTP host. The assumption pack now clarifies this, but it contradicts assumptions made in previous proposals.  
**Commercial risk:** Clients who received earlier proposals where APPSolve appeared to take SFTP responsibility will push back on the new assumptions. SFTP server provisioning and hosting is infrastructure — if APPSolve does it, it carries operational risk and cost.  
**Recommended action:** BU Lead confirms OIC-EXC-004 (infrastructure procurement excluded) covers SFTP server provisioning. Where clients have no SFTP capability, document the options: (a) client procures cloud SFTP (AWS Transfer Family, Azure SFTP, etc.); (b) Oracle SFTP agent; (c) client's IT team provisions SFTP. Add this decision tree to `OIC_IMPLEMENTATION_PATTERNS.md`.  
**Owner:** Oracle BU Lead  
**Target:** Resolve in BU Lead review cycle

---

## 4. Medium Gaps

### GAP-OIC-009 — No Cutover Runbook Template

**Severity:** MEDIUM  
**Description:** OIC-CUT-002 requires a cutover runbook per integration but no standard template exists.  
**Recommended action:** Create a standard OIC cutover runbook template covering: pre-cutover checklist, production promotion steps, production connectivity test, go-live confirmation check, rollback triggers, and rollback steps.  
**Owner:** Oracle Delivery Lead  
**Target:** Within 60 days

---

### GAP-OIC-010 — No Standard OIC Test Plan Template

**Severity:** MEDIUM  
**Description:** OIC-TST-001 through OIC-TST-006 define testing expectations but no standard OIC SIT test plan or UAT test script template exists.  
**Recommended action:** Create `OIC_SIT_TEST_PLAN_TEMPLATE.md` and `OIC_UAT_TEST_SCRIPT_TEMPLATE.xlsx` covering: integration ID, test scenario, test data requirements, expected result, actual result, pass/fail, defect reference.  
**Owner:** Oracle Delivery Lead  
**Target:** Within 60 days

---

### GAP-OIC-011 — EDI and AS2 Scope Not Addressed in Proposals

**Severity:** MEDIUM  
**Description:** OIC-EXC-011 excludes EDI and AS2 from standard OIC scope, but APPSolve does not have an assessed approach or partner for EDI engagements where clients require it (retail, wholesale distribution, logistics).  
**Commercial risk:** APPSolve is asked about EDI on ERP proposals (Acumatica distribution clients) and cannot respond with a defined position.  
**Recommended action:** BU Lead documents APPSolve's position on EDI: (a) can APPSolve deliver EDI integrations? (b) does APPSolve partner with an EDI specialist? (c) is this a lost scope or a referral? Add to `OIC_IMPLEMENTATION_PATTERNS.md` as a Pattern note.  
**Owner:** Oracle BU Lead  
**Target:** Within 90 days

---

### GAP-OIC-012 — No API Version Change Protocol

**Severity:** MEDIUM  
**Description:** OIC-SUP-004 and OIC-CON-004 acknowledge that vendor API changes can break integrations, but APPSolve does not have a documented protocol for managing API version change impacts on live OIC integrations.  
**Commercial risk:** A vendor upgrades their API 6 months after go-live; the OIC integration breaks; the client expects APPSolve to fix it under the original project contract.  
**Recommended action:** Create an API version change protocol: (a) how APPSolve is notified; (b) impact assessment SLA; (c) pricing model for API change updates; (d) recommended AMS clause for OIC support engagements. Add to `OIC_IMPLEMENTATION_PATTERNS.md`.  
**Owner:** Oracle BU Lead + AMS Lead  
**Target:** Within 90 days

---

### GAP-OIC-013 — OIC Licencing Tier Guidance Not Available to Bid Teams

**Severity:** MEDIUM  
**Description:** OIC-PERF-004 and OIC-CUS-012 require the client to select an appropriate OIC licence tier, but APPSolve bid teams do not have reference material to advise clients on OIC licence tier selection based on estimated transaction volumes.  
**Commercial risk:** Client under-licences OIC → performance issues at go-live → APPSolve blamed. Or client over-licences → unnecessary cost → APPSolve credibility affected.  
**Recommended action:** Add OIC licence tier guidance to `OIC_IMPLEMENTATION_PATTERNS.md` — covering the Standard vs Enterprise distinction, message volume thresholds, and how to translate Integration Inventory volumes into a licence tier recommendation.  
**Owner:** Oracle BU Lead  
**Target:** Within 90 days

---

## 5. Low Gaps

### GAP-OIC-014 — No BeBanking-Specific OIC Assumptions

**Severity:** LOW  
**Description:** BeBanking bank connectivity is implemented via OIC (Carin Webb is the sole BeBanking OIC specialist per CONSULTANT_SKILL_MATRIX.md). The BeBanking assumptions pack (FUTURE) should include OIC-specific assumptions for H2H bank connectivity. Currently, the OIC pack is generic across all integration contexts.  
**Recommended action:** When creating the BeBanking assumptions pack, add a BeBanking OIC section that cross-references OIC_ASSUMPTIONS_V1.md with BeBanking-specific overrides (H2H SFTP patterns, bank IP whitelisting, payment file certification).  
**Owner:** BeBanking BU Lead  
**Target:** When BeBanking assumptions pack is created (Pack 9 in roadmap)

---

### GAP-OIC-015 — No OCI-Hosted OIC Assumptions

**Severity:** LOW  
**Description:** Where Oracle OCI is in scope (e.g., EBS on OCI migrations, OCI-hosted SFTP services), OIC behaviour may differ from cloud-native OIC. OCI-hosted OIC connectivity assumptions (private endpoints, VPN/FastConnect, OCI compartment setup) are not in the current pack.  
**Recommended action:** Add OCI-specific OIC notes to `OIC_IMPLEMENTATION_PATTERNS.md` when the OCI assumptions pack is created (Pack 7 in roadmap).  
**Owner:** Oracle BU Lead  
**Target:** When OCI assumptions pack is created

---

### GAP-OIC-016 — Acumatica-to-Oracle OIC Patterns Not Documented

**Severity:** LOW  
**Description:** Where clients run both Acumatica ERP and Oracle HCM (or vice versa), OIC is used to bridge them. No standard integration patterns for Acumatica-Oracle OIC exist in the KB.  
**Recommended action:** Add Acumatica↔Oracle OIC pattern to `OIC_IMPLEMENTATION_PATTERNS.md` when the Acumatica assumptions pack is created (Pack 8 in roadmap).  
**Owner:** Acumatica BU Lead + Oracle OIC Lead  
**Target:** When Acumatica assumptions pack is created

---

### GAP-OIC-017 — No Post-Go-Live OIC Managed Services Assumptions

**Severity:** LOW  
**Description:** The OIC pack explicitly excludes managed services (OIC-EXC-009). The AMS assumptions pack (Pack 10 in roadmap) will need OIC-specific AMS assumptions: OIC monitoring SLA, error resubmission response time, API change management, version upgrade support.  
**Recommended action:** Flag this gap as an input requirement for the AMS assumptions pack (Pack 10). The AMS pack must address OIC monitoring, incident response, and API change management as distinct AMS service lines.  
**Owner:** AMS Lead  
**Target:** When AMS assumptions pack is created

---

## 6. Gap Summary Table

| Gap ID | Description | Severity | Owner | Target |
|---|---|---|---|---|
| GAP-OIC-001 | Integration complexity tier model not documented | CRITICAL | Oracle BU Lead | Next OIC SOW |
| GAP-OIC-002 | No OIC effort rate card or estimate template | CRITICAL | BU Lead + Delivery | Next OIC tender |
| GAP-OIC-003 | No standard Integration Inventory template | CRITICAL | Delivery Lead | Next OIC kickoff |
| GAP-OIC-004 | W4-INT-001 accelerator catalogue not linked to assumptions | HIGH | Oracle BU Lead | Next BU review |
| GAP-OIC-005 | No Mapping Specification template | HIGH | Delivery Lead | 30 days |
| GAP-OIC-006 | No OIC TDD template | HIGH | Delivery Lead | 30 days |
| GAP-OIC-007 | No published OIC reference engagement | HIGH | BU Lead + AM | Next OIC tender |
| GAP-OIC-008 | SFTP server ownership not consistently addressed | HIGH | Oracle BU Lead | BU Lead review |
| GAP-OIC-009 | No cutover runbook template | MEDIUM | Delivery Lead | 60 days |
| GAP-OIC-010 | No standard OIC test plan or UAT script | MEDIUM | Delivery Lead | 60 days |
| GAP-OIC-011 | EDI/AS2 position not defined | MEDIUM | Oracle BU Lead | 90 days |
| GAP-OIC-012 | No API version change protocol | MEDIUM | BU Lead + AMS | 90 days |
| GAP-OIC-013 | No OIC licence tier guidance for bid teams | MEDIUM | Oracle BU Lead | 90 days |
| GAP-OIC-014 | No BeBanking-specific OIC assumptions | LOW | BeBanking BU Lead | With BeBanking pack |
| GAP-OIC-015 | No OCI-hosted OIC assumptions | LOW | Oracle BU Lead | With OCI pack |
| GAP-OIC-016 | No Acumatica-Oracle OIC patterns | LOW | ACU BU + OIC Lead | With Acumatica pack |
| GAP-OIC-017 | No post-go-live OIC AMS assumptions | LOW | AMS Lead | With AMS pack |

---

## 7. Immediate BU Lead Actions Required (Pre-Approval Gates)

Before `OIC_ASSUMPTIONS_V1.md` can be promoted from Draft to Approved, the following must be resolved:

| Item | Required for Approval | BU-OIC Item |
|---|---|---|
| Define what constitutes "one integration" | Yes — OIC-SCP-002 is the most litigated scope item | BU-OIC-001 |
| Confirm non-production OIC environment standard inclusion | Yes — affects every OIC estimate | BU-OIC-002 |
| Confirm error notification recipient | Yes — operational default needed | BU-OIC-003 |
| Confirm concurrent vs separate hypercare model | Yes — affects every combined HCM+OIC project | BU-OIC-004 |
| Confirm complexity tier definitions | Yes — underpins GAP-OIC-001 and GAP-OIC-002 | BU-OIC-005 |
| Confirm accelerator library and effort reduction | Yes — affects estimate accuracy | BU-OIC-006 |
| Confirm SFTP fallback is APPSolve default | Yes — affects endpoint approach in every file-based integration | BU-OIC-007 |

---

*OIC_GAP_REPORT v1.0 | WP11C — Oracle Integration Cloud Assumptions Pack | 2026-06-15*  
*17 gaps identified | 3 CRITICAL | 5 HIGH | 5 MEDIUM | 4 LOW*
