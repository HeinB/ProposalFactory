---
document_id: RISK-GOVERNANCE-DECISION-REGISTER-V1
title: "Risk Library — Governance Decision Register"
version: "1.0"
status: "COMPLETE — All 20 decisions recorded (WP18B-EXT.2, 2026-06-28)"
created: "2026-06-26"
created_by: "WP18B-EXT.1B — Risk Library Decision Harvest"
approved_by: ""
approved_date: ""
category: "Commercial / Risk Library / Governance"
scope: "Decision register for all Category B (Approval Required) items in the Enterprise Risk Register V1.0. 20 decisions. Format mirrors Assumption Library governance packs."
related_documents:
  - ENTERPRISE_RISK_REGISTER_V1.md
  - RISK_AUTO_APPROVAL_REGISTER.md
  - RISK_GOVERNANCE_WORKSHOP_PACK.md
  - WP18B_EXT1B_DECISION_HARVEST_REPORT.md
---

# Risk Library — Governance Decision Register

**Work Package:** WP18B-EXT.1B  
**Status:** AWAITING BU LEAD REVIEW  
**Total decisions:** 20 Category B items  
**Recommended channel:** 7 via email pre-approval; 13 via 90-minute workshop  
**Do not apply approvals in this document.** Approvals are applied in ENTERPRISE_RISK_REGISTER_V1.md by updating `approved_for_reuse` and `approved_by` after the governance session.

---

## Decision Summary

| Decision ID | Risk ID | Decision Type | Channel | Priority |
|---|---|---|---|---|
| BU-RL-001 | RC-PROJ-001 | Merger confirmation (DG-001) | Email | Medium |
| BU-RL-002 | RC-PROJ-002 | Merger confirmation (DG-002) | Email | Medium |
| BU-RL-003 | RC-PROJ-003 | Rating change: HIGH → CRITICAL | Workshop | High |
| BU-RL-004 | RC-PROJ-004 | Rating change: LOW → MEDIUM (matrix) | Email | Low |
| BU-RL-005 | RC-DATA-001 | Rating change: HIGH → CRITICAL | Workshop | High |
| BU-RL-006 | RC-DATA-003 | Rating change: HIGH → CRITICAL | Workshop | High |
| BU-RL-007 | RC-DATA-004 | Rating change: HIGH → CRITICAL | Workshop | High |
| BU-RL-008 | RC-INT-002 | Merger confirmation (DG-004) | Email | Medium |
| BU-RL-009 | RC-INT-005 | Merger confirmation (DG-006) | Email | Medium |
| BU-RL-010 | RC-TECH-002 | Merger confirmation (DG-003) | Email | Medium |
| BU-RL-011 | RC-TECH-003 | Rating change: HIGH → CRITICAL | Workshop | High |
| BU-RL-012 | RC-TECH-006 | Rating change: HIGH → CRITICAL + split decision (DG-008) | Workshop | High |
| BU-RL-013 | RC-TECH-008 | Rating change: HIGH → CRITICAL + split decision (DG-008) | Workshop | High |
| BU-RL-014 | RC-TECH-012 | Rating change: HIGH → CRITICAL | Workshop | High |
| BU-RL-015 | RC-CLIENT-004 | Rating change: HIGH → CRITICAL | Workshop | High |
| BU-RL-016 | RC-CLIENT-007 | Rating change: HIGH → CRITICAL | Workshop | High |
| BU-RL-017 | RC-COMM-001 | Merger (DG-005, 3 sources) + rating change: HIGH → CRITICAL | Workshop | High |
| BU-RL-018 | RC-COMM-002 | Rating change: HIGH → CRITICAL | Workshop | High |
| BU-RL-019 | RC-COMP-001 | Merger confirmation (DG-007) | Email | Medium |
| BU-RL-020 | RC-OPS-001 | Governance rule: mandatory_if = TRUE (unconditional inclusion) | Workshop | High |

---

## EMAIL DECISIONS (7 items — Pre-Session Approval)

These decisions have clear rationale, are mathematically or logically self-evident, and do not require group deliberation. Send as a pre-read pack with the request to respond Approve / Revise before the workshop.

---

### BU-RL-001 — RC-PROJ-001: Merger Confirmation (DG-001)

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-001 |
| **Risk ID** | RC-PROJ-001 |
| **Decision type** | Merger confirmation |
| **Channel** | Email |
| **Source evidence** | DG-001 in RISK_DUPLICATION_ANALYSIS.md |

**Current state:** Two source risks exist in approved KB assets:
- R-W2-001 (W3S1-002): "Module design not approved before build commences"
- R-W3-005-001 (W3S1-005): "Module design not signed off before build begins"

**Proposed state:** Single canonical risk RC-PROJ-001 representing both. Wording: "Module design not signed off before build begins." Rating: HIGH (unchanged from both sources).

**Reason for review:** Consolidation of two approved source risks into one canonical entry is a governance decision.

**Supporting evidence:** Both source risks describe identical root cause (unapproved design leads to build rework) from different KB asset perspectives. The 2-word difference in title is stylistic, not substantive.

**Recommendation:** Approve merger. The two sources are functionally identical. A single canonical entry is cleaner and avoids conflicting risk registers across proposals.

**Decision options:**
- A. Approve merger as RC-PROJ-001 → promote to Approved
- B. Keep separate → requires RC-PROJ-001A and RC-PROJ-001B

**Recommendation rationale:** Option A. Both source assets address the same project risk at the same project stage. Maintaining two entries would produce duplicate risk registers in HCM proposals. Merger reduces noise and increases register clarity.

---

### BU-RL-002 — RC-PROJ-002: Merger Confirmation (DG-002)

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-002 |
| **Risk ID** | RC-PROJ-002 |
| **Decision type** | Merger confirmation |
| **Channel** | Email |
| **Source evidence** | DG-002 in RISK_DUPLICATION_ANALYSIS.md |

**Current state:** Two source risks:
- R-W2-003 (W3S1-002): "Upstream phase instability impacts dependent phase"
- R-W3-003-003 (W3S1-003): "Phase dependency not managed causes downstream delay"

**Proposed state:** Single canonical risk RC-PROJ-002 — "Upstream phase not stable when dependent phase begins." Rating: HIGH.

**Reason for review:** Consolidation decision.

**Supporting evidence:** Both express phase-dependency instability in phased HCM implementations. Proposal pattern restricted to P2 (HCM Full Suite Phased) only.

**Recommendation:** Approve merger. Identical risk, different asset origins.

**Decision options:**
- A. Approve merger as RC-PROJ-002 → promote to Approved
- B. Keep separate → two very similar Phase 2 risks

**Recommendation rationale:** Option A. The risk only applies to phased delivery (Pattern 2). One canonical entry is sufficient.

---

### BU-RL-004 — RC-PROJ-004: Rating Change LOW → MEDIUM

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-004 |
| **Risk ID** | RC-PROJ-004 |
| **Decision type** | Rating correction |
| **Channel** | Email |
| **Source evidence** | 3×3 rating matrix in RISK_LIBRARY_STANDARD.md |

**Current state (draft v0.1):** Rating = LOW. Likelihood = Low, Impact = High.

**Proposed state (V1.0):** Rating = MEDIUM. Likelihood = Low × Impact = High → MEDIUM per matrix.

**Reason for review:** Mathematical correction. LOW rating was incorrect per the defined matrix.

**Supporting evidence:**
Rating matrix from RISK_LIBRARY_STANDARD.md:
- Low Likelihood × High Impact = **MEDIUM** (not LOW)
- LOW rating requires Low Likelihood × Low or Medium Impact

**Recommendation:** Approve rating correction to MEDIUM. This is a matrix arithmetic fix, not a business judgment.

**Decision options:**
- A. Approve MEDIUM → mathematically correct per defined matrix
- B. Revert to LOW → requires changing the likelihood or impact field, or overriding the matrix

**Recommendation rationale:** Option A. The rating matrix is an approved governance standard. The draft error was computational; this correction aligns the register to the approved standard.

---

### BU-RL-008 — RC-INT-002: Merger Confirmation (DG-004)

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-008 |
| **Risk ID** | RC-INT-002 |
| **Decision type** | Merger confirmation |
| **Channel** | Email |
| **Source evidence** | DG-004 in RISK_DUPLICATION_ANALYSIS.md |

**Current state:** Two source risks:
- R-W3-003-005 (W3S1-003): "Third-party integration scope underestimated"
- R-W3-004-005 (W3S1-004): "Integration scope estimation error causes overrun"

**Proposed state:** Single canonical risk RC-INT-002 — "Third-party integration scope underestimated." Rating: MEDIUM.

**Reason for review:** Consolidation decision.

**Supporting evidence:** Both risks describe the same integration scoping problem from HCM Recruiting and HCM Learning asset contexts respectively. The mitigation (Integration Discovery workshop; OIC-DES-001 scope document) is identical.

**Recommendation:** Approve merger. Different assets, same risk.

**Decision options:**
- A. Approve merger → promote to Approved
- B. Keep separate → two near-identical integration scope entries

**Recommendation rationale:** Option A. The risk is platform-generic (OIC integration underestimation). One canonical entry applies to all applicable patterns.

---

### BU-RL-009 — RC-INT-005: Merger Confirmation (DG-006)

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-009 |
| **Risk ID** | RC-INT-005 |
| **Decision type** | Merger confirmation |
| **Channel** | Email |
| **Source evidence** | DG-006 in RISK_DUPLICATION_ANALYSIS.md |

**Current state:** Two source risks:
- R-W9-003 (W3S1-009): "Integration not ready before payroll processing window"
- R-W3-005-005 (W3S1-005): "Payroll cutoff alignment not managed in project plan"

**Proposed state:** Single canonical risk RC-INT-005 — "Integration schedule not aligned to payroll cutoff." Rating: HIGH.

**Reason for review:** Consolidation decision.

**Supporting evidence:** Both risks describe the consequence of misaligned integration and payroll cycle timing. Root cause is identical (project plan does not account for fixed payroll cutoff windows).

**Recommendation:** Approve merger. The combined entry is more complete than either source.

**Decision options:**
- A. Approve merger → promote to Approved
- B. Keep separate → two overlapping payroll timing entries

**Recommendation rationale:** Option A. Merged entry captures both the integration readiness angle and the project planning angle in one risk.

---

### BU-RL-010 — RC-TECH-002: Merger Confirmation (DG-003)

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-010 |
| **Risk ID** | RC-TECH-002 |
| **Decision type** | Merger confirmation |
| **Channel** | Email |
| **Source evidence** | DG-003 in RISK_DUPLICATION_ANALYSIS.md |

**Current state:** Two source risks:
- R-W3-004-004 (W3S1-004): "SETA/WSP extract configuration complexity — HCM Learning"
- R-W3-006-004 (W3S1-006): "SETA/ATR extract complexity — HCM Analytics"

**Proposed state:** Single canonical risk RC-TECH-002 — "SETA/WSP/ATR extract complexity." Rating: MEDIUM.

**Reason for review:** Consolidation decision.

**Supporting evidence:** SETA reporting complexity is a South Africa-specific legislative requirement that spans both Learning (WSP/ATR) and HCM Analytics (reporting extract). The root cause (SETA data model complexity exceeding Oracle standard extracts) is the same regardless of which module surfaces it.

**Recommendation:** Approve merger. The merged risk is South Africa-scoped and applies when Oracle HCM is in scope.

**Decision options:**
- A. Approve merger → promote to Approved
- B. Keep separate → one Learning-specific and one Analytics-specific SETA risk

**Recommendation rationale:** Option A. The mitigation (SETA Reporting Assessment; custom extract configuration) is the same for both. Splitting creates artificial redundancy.

---

### BU-RL-019 — RC-COMP-001: Merger Confirmation (DG-007)

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-019 |
| **Risk ID** | RC-COMP-001 |
| **Decision type** | Merger confirmation |
| **Channel** | Email |
| **Source evidence** | DG-007 in RISK_DUPLICATION_ANALYSIS.md |

**Current state:** Two source risks:
- R-W8-007 (W3S1-008): "POPIA non-compliance in WFM time and attendance data"
- R-W9-005 (W3S1-009): "POPIA non-compliance in payroll integration data flow"

**Proposed state:** Single canonical risk RC-COMP-001 — "POPIA non-compliance in HR or payroll data handling." Rating: MEDIUM.

**Reason for review:** Consolidation decision. Also: RC-COMP-001 is the sole entry in the RC-COMP category; consolidation determines category coverage.

**Supporting evidence:** Both source risks describe POPIA obligations arising from personal data handling in different modules. The regulatory framework (POPIA operator/responsible party model) and mitigation (DPA, data minimisation, encryption) are identical regardless of data source.

**Recommendation:** Approve merger. A single compliance risk entry is appropriate; POPIA scope is defined by the data processed, not the specific module.

**Decision options:**
- A. Approve merger → promote to Approved
- B. Keep separate → two module-specific POPIA entries
- C. Expand scope to include BeBanking (BB-DAT-006 already referenced as an assumption)

**Recommendation rationale:** Option A is minimum viable; Option C is the stronger choice as it acknowledges BeBanking's POPIA obligations are already cross-referenced. Recommend the BU Lead choose A or C. Both are approvable.

---

## WORKSHOP DECISIONS (13 items)

These items require group deliberation. Each has either a CRITICAL rating implication (raising proposals' risk posture) or a structural governance decision affecting how the Risk Selection Engine will operate.

---

### BU-RL-003 — RC-PROJ-003: Rating HIGH → CRITICAL

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-003 |
| **Risk ID** | RC-PROJ-003 |
| **Decision type** | Rating change |
| **Channel** | Workshop — Batch 1 (Project Fundamentals) |
| **Source evidence** | W3S1-004 (R-W3-004-001) |

**Current state (draft v0.1):** Rating = HIGH. Likelihood = Medium, Impact = High.

**Proposed state (V1.0):** Rating = CRITICAL. Likelihood = **High**, Impact = High.

**Reason for review:** Likelihood raised from Medium to High on the basis that late org design decisions are "the most frequently observed HCM project risk."

**Supporting evidence:** Likelihood elevation from Medium to High is based on observed project frequency across APPSolve's HCM implementations. If confirmed High × High → CRITICAL per matrix. This risk would lead every HCM proposal risk register.

**Commercial impact:** CRITICAL designation means this risk appears at the top of every P1 and P2 proposal risk register. It signals to the client that APPSolve views org design readiness as the most serious project risk. This is accurate but can be commercially sensitive if the client's org is in flux.

**Recommendation:** Confirm CRITICAL. The observed frequency of late org design decisions as a project blocker is real and well-documented in HCM project experience.

**Decision options:**
- A. Confirm CRITICAL (High × High) — reflects observed frequency
- B. Revert to HIGH (Medium × High) — more conservative; avoids over-stating certainty
- C. Accept HIGH rating, elevate `assembly_priority` to Critical — communicates urgency without changing the matrix rating

**Recommendation rationale:** Option A. Org design readiness is a genuine CRITICAL failure point in HCM implementations. The rating should match delivery reality, not commercial optics. If the BU Lead has seen fewer than 50% of HCM projects impacted by late org design, revert to Option B.

---

### BU-RL-005 — RC-DATA-001: Rating HIGH → CRITICAL

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-005 |
| **Risk ID** | RC-DATA-001 |
| **Decision type** | Rating change |
| **Channel** | Workshop — Batch 1 (Project Fundamentals) |
| **Source evidence** | W3S1-002 (R-W2-004) |

**Current state (draft v0.1):** Rating = HIGH. Likelihood = High, Impact = High.

**Proposed state (V1.0):** Rating = CRITICAL. Likelihood = High, Impact = High.

**Reason for review:** The High × High combination produces CRITICAL per the rating matrix. The draft rating of HIGH was incorrect — the matrix requires CRITICAL for High × High.

**Supporting evidence:** This is a matrix correction, not a likelihood or impact change. Unlike BU-RL-003 (where likelihood was raised), the likelihood was already High in the draft.

**Commercial impact:** CRITICAL designation. Payroll cutover failures being root-caused to HR data quality is a real and observed pattern. This risk should lead every HCM proposal risk register that includes data migration.

**Recommendation:** Confirm CRITICAL. High × High = CRITICAL per matrix. The draft HIGH rating was a matrix error; this is a correction.

**Decision options:**
- A. Confirm CRITICAL (High × High matrix correction) — correct
- B. Revert likelihood to Medium → overall rating HIGH — if observed frequency is lower than assumed

**Recommendation rationale:** Option A. This is the same situation as BU-RL-004 (matrix arithmetic) but for a High × High combination. Data quality as a source of HCM go-live failure is industry-wide and well-documented.

---

### BU-RL-006 — RC-DATA-003: Rating HIGH → CRITICAL

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-006 |
| **Risk ID** | RC-DATA-003 |
| **Decision type** | Rating change |
| **Channel** | Workshop — Batch 2 (Payroll and Data) |
| **Source evidence** | W3S1-009 (R-W9-001) |

**Current state (draft v0.1):** Rating = HIGH.

**Proposed state (V1.0):** Rating = CRITICAL. Likelihood = High, Impact = High.

**Reason for review:** High × High = CRITICAL per matrix.

**Supporting evidence:** HCM data quality errors propagating to payroll produce incorrect payroll runs. This is a High-impact risk because payroll errors have direct financial consequence and regulatory exposure. Likelihood is High because data quality issues are common in legacy-to-HCM migrations.

**Commercial impact:** Mandatory for all payroll-integrated proposals. CRITICAL designation signals to clients that parallel payroll runs are essential, not optional.

**Recommendation:** Confirm CRITICAL.

**Decision options:**
- A. Confirm CRITICAL — matrix-correct and delivery-reality-aligned
- B. Revise likelihood to Medium → rating HIGH — if data quality issues are less frequent than assumed

**Recommendation rationale:** Option A. Payroll data errors are a confirmed delivery pattern. CRITICAL rating supports the business case for parallel payroll runs (which add cost but prevent regulatory exposure).

---

### BU-RL-007 — RC-DATA-004: Rating HIGH → CRITICAL

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-007 |
| **Risk ID** | RC-DATA-004 |
| **Decision type** | Rating change |
| **Channel** | Workshop — Batch 2 (Payroll and Data) |
| **Source evidence** | W3S1-008 (R-W8-002) |

**Current state (draft v0.1):** Rating = HIGH.

**Proposed state (V1.0):** Rating = CRITICAL. Likelihood = High, Impact = High.

**Reason for review:** High × High = CRITICAL per matrix. Also: confidence_level is Medium (not High), reflecting limited project evidence for WFM-specific biometric reconciliation scenarios.

**Supporting evidence:** Biometric device mismatches affect time and attendance records, which propagate to payroll. Impact is High. Likelihood elevated to High because biometric data quality is consistently problematic at Oracle WFM go-live.

**Commercial impact:** Narrow applicability — only triggered when Oracle WFM is in scope. CRITICAL designation for a niche scenario may appear disproportionate.

**Consideration:** The confidence_level for this risk is Medium (not High). There is less project evidence for WFM biometric implementations than for general HCM data migration. This is a case where the BU Lead's WFM implementation experience matters.

**Recommendation:** Confirm CRITICAL but note limited evidence base. If WFM project history shows biometric reconciliation is resolved quickly, revert to HIGH.

**Decision options:**
- A. Confirm CRITICAL (High × High) — strong signal for WFM proposals
- B. Revert likelihood to Medium → HIGH — more conservative; confidence_level is only Medium
- C. Confirm CRITICAL but set confidence_level to Low — signals limited evidence while maintaining posture

**Recommendation rationale:** Option B is defensible given the Medium confidence level. This is the most nuanced decision in the register — BU Lead WFM experience should determine the outcome.

---

### BU-RL-011 — RC-TECH-003: Rating HIGH → CRITICAL

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-011 |
| **Risk ID** | RC-TECH-003 |
| **Decision type** | Rating change |
| **Channel** | Workshop — Batch 3 (Technical and Scope) |
| **Source evidence** | W3S1-008 (R-W8-001) |

**Current state (draft v0.1):** Rating = HIGH.

**Proposed state (V1.0):** Rating = CRITICAL. Likelihood = High, Impact = High.

**Reason for review:** Characterised as "the #1 WFM scope overrun." High × High = CRITICAL.

**Supporting evidence:** Absence rule complexity in Oracle WFM implementations is consistently underestimated. Union agreements, multi-employment-type leave entitlements, and BCEA interaction with shift patterns produce configuration volumes beyond standard scope. This drives rework and timeline extension.

**Commercial impact:** CRITICAL designation for an inclusion that is only triggered when Oracle WFM is in scope. Important for WFM proposal risk sections.

**Recommendation:** Confirm CRITICAL. Absence rule complexity being the #1 WFM overrun is a strong delivery claim — the BU Lead should confirm this from WFM project history.

**Decision options:**
- A. Confirm CRITICAL — reflects observed WFM delivery experience
- B. Revert to HIGH — if absence rule overruns are common but not always HIGH impact

**Recommendation rationale:** Option A if WFM project overruns due to absence complexity are confirmed. Option B if the impact is typically contained within contingency.

---

### BU-RL-012 — RC-TECH-006: Rating HIGH → CRITICAL + DG-008 Split Decision

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-012 |
| **Risk ID** | RC-TECH-006 |
| **Decision type** | Rating change + split decision |
| **Channel** | Workshop — Batch 3 (Technical and Scope) |
| **Source evidence** | W3S1-004 (R-W3-004-003); DG-008 |

**Current state (draft v0.1):** Rating = HIGH. Source risk covered OAX licensing specifically.

**Proposed state (V1.0):** Rating = CRITICAL. Scope: OAX-specific. Deliberately kept separate from RC-TECH-008 (general licensing).

**Reason for review:** Two decisions required:
1. Rating change: HIGH → CRITICAL
2. DG-008 split confirmation: RC-TECH-006 (OAX-specific) and RC-TECH-008 (general Oracle licensing) are kept as two separate canonical risks, not merged

**Supporting evidence:**
- Rating: OAX licensing gaps have been observed to stop HCM analytics workstreams. High × High = CRITICAL.
- Split: RC-TECH-006 covers OAX specifically (separately licensed analytics product); RC-TECH-008 covers any Oracle feature with separate licensing dependency (broader scope). These are distinct risks with different triggers and mitigations.

**Commercial impact:** CRITICAL OAX licensing risk signals to clients that OAX confirmation is a project gate, not a nice-to-have. This supports APPSolve's commercial position on analytics prerequisites.

**Recommendation:** Confirm CRITICAL and confirm split from RC-TECH-008.

**Decision options for rating:**
- A. Confirm CRITICAL — OAX licensing stops projects; confirmed by delivery experience
- B. Revert to HIGH — if OAX licensing issues are typically discovered and resolved quickly

**Decision options for split:**
- A. Confirm split — RC-TECH-006 (OAX-specific) and RC-TECH-008 (general) remain separate
- B. Merge into one general licensing risk — simpler register; loses OAX-specific specificity
- C. Keep separate but rename RC-TECH-006 to emphasise OAX exclusively

**Recommendation rationale:** Confirm CRITICAL (Option A-rating). Confirm split (Option A-split). The two risks have genuinely different triggers: OAX requires the BU Lead to confirm a specific product licence; general licensing applies to any Oracle feature bundle. Merging them loses precision.

---

### BU-RL-013 — RC-TECH-008: Rating HIGH → CRITICAL + DG-008 Split Decision

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-013 |
| **Risk ID** | RC-TECH-008 |
| **Decision type** | Rating change + split decision |
| **Channel** | Workshop — Batch 3 (Technical and Scope) |
| **Source evidence** | W3S1-005 (R-W3-005-004); DG-008 |

**Current state (draft v0.1):** Rating = HIGH. General Oracle product licensing risk.

**Proposed state (V1.0):** Rating = CRITICAL. Scope: any Oracle Cloud feature with separate licensing dependency.

**Reason for review:** Rating HIGH → CRITICAL; DG-008 split decision (see BU-RL-012 above).

**Supporting evidence:** The broader general licensing risk applies across Oracle Cloud implementations where dependent features (AI/ML capabilities, additional user types, specific module extensions) are included in scope without confirmed licence. CRITICAL because discovering a licence gap early in a project forces a commercial conversation that can delay workstreams.

**Recommendation:** Confirm CRITICAL and confirm split from RC-TECH-006.

**Decision options:**
- A. Confirm CRITICAL + confirm split — consistent with BU-RL-012 decision
- B. Revert to HIGH + confirm split
- C. Merge with RC-TECH-006 — loses specificity; not recommended

**Recommendation rationale:** Handle in the same workshop batch as BU-RL-012. The two decisions are linked — if the split is confirmed, both ratings should be set consistently. If the split is rejected, a single merged entry is created and the rating decision is made once.

---

### BU-RL-014 — RC-TECH-012: Rating HIGH → CRITICAL

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-014 |
| **Risk ID** | RC-TECH-012 |
| **Decision type** | Rating change; also: classification question |
| **Channel** | Workshop — Batch 4 (Legislative and Compliance) |
| **Source evidence** | W3S1-009 (R-W9-007) |

**Current state (draft v0.1):** Rating = HIGH.

**Proposed state (V1.0):** Rating = CRITICAL. Basis: "Annual SA legislative change is a certainty (not a risk)."

**Reason for review:** This is the most conceptually complex decision in the register. Two separate questions are embedded:

1. **Rating question:** Is the risk CRITICAL or HIGH?
2. **Classification question:** If the legislative update is a certainty (it happens every year on 1 March), is this properly a risk register entry, or should it be a formal service process/SLA obligation?

**Supporting evidence:**
- The annual SA budget update (tax tables, UIF, SDL) is a *certain* annual event. The *uncertainty* is whether APPSolve will have completed the integration update before the effective date.
- Rating HIGH → CRITICAL: High × High per matrix. The impact of a missed legislative update is severe (non-compliant payroll output).
- Classification: In the Assumption Library governance model, known certainties are captured as assumptions (process obligations), not risks. This could be an AMS-REL-001 service obligation rather than a risk register entry.

**Commercial impact:** If retained as CRITICAL in the risk register, it strengthens APPSolve's position on the annual update service (clients see it as a critical risk that APPSolve explicitly manages). If moved to the SLA/service framework, it is a stronger commercial commitment.

**Recommendation:** Confirm CRITICAL rating AND retain in risk register (for implementation proposals, the risk is genuine — the integration may not be updated before go-live if the project spans a budget date). For AMS proposals, cross-reference AMS-REL-001 as the governing SLA obligation.

**Decision options:**
- A. Confirm CRITICAL — retain in risk register for both Implementation and AMS
- B. Confirm HIGH — less assertive; implementation tenders
- C. Retain CRITICAL in Implementation register; move to AMS service framework for AMS proposals — reduces risk register duplication with AMS process documentation
- D. Remove from risk register entirely; document as AMS-REL-001 service obligation — only appropriate if AMS is the only applicable engagement type

**Recommendation rationale:** Option A for simplicity. Option C is the architecturally cleaner choice — it treats the AMS update cycle as a contractual service obligation (which it is) while retaining the risk for Implementation proposals where the update window is genuinely unpredictable.

---

### BU-RL-015 — RC-CLIENT-004: Rating HIGH → CRITICAL

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-015 |
| **Risk ID** | RC-CLIENT-004 |
| **Decision type** | Rating change |
| **Channel** | Workshop — Batch 4 (Client Obligations) |
| **Source evidence** | W3S1-006 (R-W3-006-002) |

**Current state (draft v0.1):** Rating = HIGH.

**Proposed state (V1.0):** Rating = CRITICAL. Basis: "A learning system without content at go-live defeats the implementation objective."

**Reason for review:** High × High = CRITICAL per matrix.

**Supporting evidence:** If the Oracle Learning catalog is empty at go-live, employees cannot use the system for its primary purpose. This is a failure of the implementation objective, not merely a performance degradation.

**Commercial impact:** CRITICAL designation for a Learning-only trigger. For Learning Standalone proposals (Pattern 5), this would lead the risk register. Signals to clients that content ownership must be committed before go-live.

**Recommendation:** Confirm CRITICAL. An empty learning system at go-live is a de facto implementation failure. The rating supports APPSolve's requirement for client content commitment.

**Decision options:**
- A. Confirm CRITICAL — strong signal; supports content readiness requirement
- B. Revert to HIGH — more conservative; the system still works, content is just absent

**Recommendation rationale:** Option A. The test is whether the system is usable, not whether it is configured. A learning system without content fails the usability test at go-live.

---

### BU-RL-016 — RC-CLIENT-007: Rating HIGH → CRITICAL

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-016 |
| **Risk ID** | RC-CLIENT-007 |
| **Decision type** | Rating change |
| **Channel** | Workshop — Batch 4 (Client Obligations) |
| **Source evidence** | W3S1-005 (R-W3-005-008) |

**Current state (draft v0.1):** Rating = HIGH.

**Proposed state (V1.0):** Rating = CRITICAL. Basis: "Cross-functional alignment failures are the primary cause of HCM design rework."

**Reason for review:** Likelihood elevated from Medium to High. High × High = CRITICAL.

**Supporting evidence:** When HR, Finance, Payroll, and IT disagree on org design, job architecture, or position management approach, the design workshop stalls and rework occurs. This is observed as the primary cause of HCM design phase overruns.

**Commercial impact:** CRITICAL designation for every HCM full suite proposal. Strong signal to clients that a named Project Sponsor with cross-functional authority is non-negotiable.

**Recommendation:** Confirm CRITICAL. Cross-functional alignment failure is consistently the most complex client-side governance risk in HCM implementations. The rating should match this reality.

**Decision options:**
- A. Confirm CRITICAL — accurate and signals governance requirement
- B. Revert to HIGH — less alarming; more conservative commercial posture

**Recommendation rationale:** Option A. The risk of cross-functional misalignment is not just HIGH — it is the most common reason HCM design phases overrun. The CRITICAL designation strengthens APPSolve's requirement for a named Project Sponsor.

---

### BU-RL-017 — RC-COMM-001: Merger (DG-005, 3 sources) + Rating HIGH → CRITICAL

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-017 |
| **Risk ID** | RC-COMM-001 |
| **Decision type** | Merger (3 sources) + rating change |
| **Channel** | Workshop — Batch 5 (Commercial) |
| **Source evidence** | DG-005 in RISK_DUPLICATION_ANALYSIS.md; W3S1-004, W3S1-005, W3S1-006 |

**Current state (draft v0.1):** Rating = HIGH. Three separate source risks describing analytics expectation misalignment from different HCM asset contexts.

**Proposed state (V1.0):** Single canonical risk RC-COMM-001. Rating = CRITICAL.

**Reason for review:** Two decisions:
1. Merger of three source risks into one canonical entry
2. Rating change: HIGH → CRITICAL

**Supporting evidence:**
- Merger: The three source risks (R-W3-004-002 from Learning Cloud, R-W3-005-003 from Workforce Compensation, R-W3-006-003 from HCM Analytics) all describe the same root cause: client expects analytics capabilities that exceed Oracle HCM's standard reporting. Root cause identical; different asset contexts.
- Rating: Analytics expectation misalignment "consistently produces commercial disputes." High × High = CRITICAL.

**Commercial impact:** CRITICAL designation for analytics misalignment sends a strong message to clients that analytics scope must be enumerated upfront. This supports APPSolve's position on the Analytics Requirements workshop as a mandatory project step.

**Recommendation:** Approve merger. Confirm CRITICAL.

**Decision options for merger:**
- A. Approve merger (3 sources → 1 canonical) — clean
- B. Retain 3 separate entries — clutters risk register; same mitigation three times

**Decision options for rating:**
- A. Confirm CRITICAL — consistent with observed commercial dispute frequency
- B. Revert to HIGH — more conservative

**Recommendation rationale:** Merger Option A. Rating Option A. Analytics expectation disputes are a genuine commercial risk that has caused APPSolve commercial exposure. CRITICAL is appropriate.

---

### BU-RL-018 — RC-COMM-002: Rating HIGH → CRITICAL

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-018 |
| **Risk ID** | RC-COMM-002 |
| **Decision type** | Rating change |
| **Channel** | Workshop — Batch 5 (Commercial) |
| **Source evidence** | W3S1-006 (R-W3-006-007) |

**Current state (draft v0.1):** Rating = HIGH.

**Proposed state (V1.0):** Rating = CRITICAL. Basis: "Product misidentification has caused commercial disputes on past proposals."

**Reason for review:** High × High = CRITICAL. The basis references specific past commercial disputes — the most significant evidence basis in the register.

**Supporting evidence:** Oracle HR Help Desk (part of Oracle HCM) and Oracle Service Cloud (B2C customer service) are fundamentally different products. A proposal written against one when the client requires the other is non-compliant and commercially dangerous. This has occurred on past APPSolve proposals.

**Commercial impact:** CRITICAL designation for every AMS proposal involving Help Desk. Specifically: this risk is AMS-only (Pattern 13). The CRITICAL rating signals that scope clarification at pre-sales is mandatory, not optional.

**Recommendation:** Confirm CRITICAL. The past commercial dispute evidence is the strongest argument in the register. If the BU Lead can confirm this has occurred, CRITICAL is the correct rating.

**Decision options:**
- A. Confirm CRITICAL — past incidents confirmed → proceed
- B. Revert to HIGH — if past incidents cannot be confirmed or are not material

**Recommendation rationale:** Option A, subject to BU Lead confirmation that the past commercial dispute(s) occurred. This is the only decision in the register where the rating depends on a factual claim about past project history that requires BU Lead validation.

---

### BU-RL-020 — RC-OPS-001: Governance Rule mandatory_if = TRUE

| Field | Value |
|---|---|
| **Decision ID** | BU-RL-020 |
| **Risk ID** | RC-OPS-001 |
| **Decision type** | Governance rule decision |
| **Channel** | Workshop — Batch 6 (Governance Rules) |
| **Source evidence** | ENTERPRISE_RISK_REGISTER_V1.md; RISK_METADATA_STANDARD.md Section 2.6 |

**Current state:** RC-OPS-001 has `mandatory_if: TRUE` — the only risk in the register with unconditional inclusion.

**Proposed state:** This rule, if approved, means the Risk Selection Engine will include RC-OPS-001 in every proposal risk register regardless of any tender profile variables, with the sole exception of Pattern 10 (DBA/Managed Services).

**Reason for review:** This is a governance rule that affects every future proposal. The `mandatory_if: TRUE` rule is structurally different from all other selection hooks, which are conditional. BU Lead must explicitly confirm this unconditional inclusion rule before it becomes operative.

**Supporting evidence:** Every implementation, AMS, and non-DBA engagement carries first-live-cycle risk. The risk is not platform-specific or engagement-type-specific — it exists whenever a system goes live for the first time.

**Commercial impact:** RC-OPS-001 will appear in every proposal risk register. This is appropriate — go-live risk is universally applicable — but the BU Lead should confirm this intent.

**Recommendation:** Confirm mandatory_if = TRUE. Confirm Pattern 10 (DBA) exclusion as the only exception.

**Decision options:**
- A. Confirm mandatory_if = TRUE with P10 exclusion only — unconditional for all other patterns
- B. Add additional exclusions (e.g., exclude simple AMS renewals, exclude minor scope changes)
- C. Convert to conditional: `mandatory_if: engagement_type IN ["Implementation", "AMS"]` — effectively the same but explicitly stated

**Recommendation rationale:** Option A for simplicity. The go-live operational risk exists whenever any system goes live. DBA (managed services only, no go-live) is the only defensible exclusion. Option C is equivalent but more explicit — useful if the BU Lead wants the condition stated rather than implied.

---

## Decision Status Tracker

Complete this section during/after the governance session.

| Decision ID | Risk ID | Decision | Decided By | Date | Notes |
|---|---|---|---|---|---|
| BU-RL-001 | RC-PROJ-001 | Approved — Option A (merger confirmed) | BU Lead | 2026-06-28 | Email pre-approval |
| BU-RL-002 | RC-PROJ-002 | Approved — Option A (merger confirmed) | BU Lead | 2026-06-28 | Email pre-approval |
| BU-RL-003 | RC-PROJ-003 | Approved — Option A (Confirm CRITICAL) | BU Lead | 2026-06-28 | Workshop Batch 2 |
| BU-RL-004 | RC-PROJ-004 | Approved — Option A (MEDIUM matrix correction) | BU Lead | 2026-06-28 | Email pre-approval |
| BU-RL-005 | RC-DATA-001 | Approved — Option A (Confirm CRITICAL) | BU Lead | 2026-06-28 | Workshop Batch 2 |
| BU-RL-006 | RC-DATA-003 | Approved — Option A (Confirm CRITICAL) | BU Lead | 2026-06-28 | Workshop Batch 3 |
| BU-RL-007 | RC-DATA-004 | Approved — Option B (Revert to HIGH; Medium × High) | BU Lead | 2026-06-28 | Workshop Batch 1; confidence=Medium; insufficient WFM biometric evidence for High likelihood |
| BU-RL-008 | RC-INT-002 | Approved — Option A (merger confirmed) | BU Lead | 2026-06-28 | Email pre-approval |
| BU-RL-009 | RC-INT-005 | Approved — Option A (merger confirmed) | BU Lead | 2026-06-28 | Email pre-approval |
| BU-RL-010 | RC-TECH-002 | Approved — Option A (merger confirmed) | BU Lead | 2026-06-28 | Email pre-approval |
| BU-RL-011 | RC-TECH-003 | Approved — Option A (Confirm CRITICAL) | BU Lead | 2026-06-28 | Workshop Batch 1; WFM absence overrun confirmed #1 WFM scope risk |
| BU-RL-012 | RC-TECH-006 | Approved — Option A (Confirm CRITICAL) + Option A-split (keep separate from RC-TECH-008) | BU Lead | 2026-06-28 | Workshop Batch 4; DG-008 split confirmed |
| BU-RL-013 | RC-TECH-008 | Approved — Option A (Confirm CRITICAL) + Option A-split | BU Lead | 2026-06-28 | Workshop Batch 4; linked to BU-RL-012 |
| BU-RL-014 | RC-TECH-012 | Approved — Option A (Confirm CRITICAL; all applicable patterns) | BU Lead | 2026-06-28 | Workshop Batch 3; single-entry approach |
| BU-RL-015 | RC-CLIENT-004 | Approved — Option A (Confirm CRITICAL) | BU Lead | 2026-06-28 | Workshop Batch 5; empty learning catalog = go-live failure |
| BU-RL-016 | RC-CLIENT-007 | Approved — Option A (Confirm CRITICAL) | BU Lead | 2026-06-28 | Workshop Batch 2; cross-functional misalignment confirmed as primary HCM design overrun cause |
| BU-RL-017 | RC-COMM-001 | Approved — Option A (merger 3→1) + Option A (Confirm CRITICAL) | BU Lead | 2026-06-28 | Workshop Batch 6; analytics disputes confirmed from project history |
| BU-RL-018 | RC-COMM-002 | Approved — Option A (Confirm CRITICAL) | BU Lead | 2026-06-28 | Workshop Batch 6; past commercial dispute confirmed by BU Lead |
| BU-RL-019 | RC-COMP-001 | Approved — Option A (merger confirmed; HCM+OIC scope) | BU Lead | 2026-06-28 | Email pre-approval; BeBanking expansion deferred to WP18B-EXT.3 |
| BU-RL-020 | RC-OPS-001 | Approved — Option A (mandatory_if=TRUE; Pattern 10 sole exclusion) | BU Lead | 2026-06-28 | Workshop Batch 7; unconditional inclusion rule confirmed |
