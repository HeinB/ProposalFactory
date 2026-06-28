---
document_id: WP18B2-RISK-LIBRARY-AUDIT
title: "WP18B Phase 1 — Risk Library Audit Report"
version: "1.0"
status: "Complete — WP18B Phase 1"
created: "2026-06-25"
created_by: "WP18B — Methodology & Risk Library Foundation"
category: "Audit Report"
scope: "Complete inventory and assessment of all risk-related content in the Tender Knowledge Base. Identifies what exists, where it is, what is reusable, what is missing, and provides the foundation for the Risk Library Standard (RISK_LIBRARY_STANDARD.md)."
---

# WP18B Phase 1 — Risk Library Audit Report

**Date:** 2026-06-25 | **Version:** 1.0 | **Status:** Complete  
**Work Package:** WP18B — Methodology & Risk Library Foundation  
**Phase:** Phase 1 of 5 — Repository Audit  
**Feeds into:** `08_Commercial/RISK_LIBRARY_STANDARD.md`

---

## 1. Audit Scope

This audit searched the entire Tender Knowledge Base for:

- Risk registers, risk logs, and RAID logs (any location)
- Risk management framework content
- Risk-adjacent language in assumption packs (EXC, DEP, CON codes)
- Risk wording in capability assets
- Commercial risk content in gap reports and commercial documents
- Risk references in Assembly Engine and WP12 reference library documents
- Governance risk registers

Search terms: risk, RAID, risk register, risk management, risk log, risk category, delivery risk, commercial risk, technical risk, project risk, risk mitigation

**Audit date:** 2026-06-25

---

## 2. Summary of Findings

| Finding | Detail |
|---|---|
| Formal Risk Library | **DOES NOT EXIST** |
| Standalone risk register template | **DOES NOT EXIST** |
| Risk taxonomy or category definitions | **DOES NOT EXIST** |
| Governance risk register (WP13 scope only) | 1 file — governance campaign risks only |
| Risk registers embedded in capability assets | **11+ files — 55+ individual risk entries** |
| Risk-adjacent language in assumption packs | Multiple packs — risk wording but no structured risk entries |
| Commercial risk documentation in gap reports | 10+ OIC gap reports; BeBanking gap report; others |
| RAID log references in delivery documents | All 13 delivery patterns; all 7 project plan templates |
| Risk Management Approach | Described in W2S1-005 Section 10.1 — not a standalone document |

**Assessment: No Risk Library exists. Risk content is the most dispersed asset type in the Knowledge Base — spread across 11+ capability files, 13+ commercial documents, and assumption pack language. No common format, no category taxonomy, no cross-reference structure. The Risk Library must be built from scratch using a governed taxonomy, but 55+ individual risk entries already exist that can be extracted and catalogued.**

---

## 3. Existing Risk Assets — Full Inventory

### 3.1 GOVERNANCE_RISK_REGISTER.md

| Field | Detail |
|---|---|
| **Location** | `08_Commercial/Assumptions/Governance/GOVERNANCE_RISK_REGISTER.md` |
| **Programme** | WP13 Governance Approval Campaign |
| **Date** | 2026-06-16 |
| **Status** | Active |
| **Scope** | Governance approval campaign risks ONLY |

**Content:** 14 governance risks (GR-001 to GR-014) covering BU Lead availability, BEE certificate expiry, conflicting pack decisions, scope change after approval, Commercial Director availability, Acumatica partner certificate, and proposal assembly from draft packs.

**Reuse potential for Risk Library:** LOW. These are internal governance programme management risks, not proposal delivery or commercial risks. They document operational programme risks, not the categories of risk that APPSolve manages for clients during delivery.

**Key statement from this document:**
> "Risks to the governance approval campaign only. Proposal delivery risks are tracked in the main Tender Programme risk register. Assumption pack content risks are tracked in individual Gap Reports."

This confirms that the Risk Library being designed in WP18B is a separate, more fundamental artefact.

---

### 3.2 Risk Registers Embedded in Capability Assets

This is the primary source of raw risk content for the Risk Library. Every major Oracle HCM capability asset and two Acumatica capability assets contain structured risk registers.

#### Oracle HCM Capability Assets

**W3S1-001 — Oracle HCM Core** (Section 11, 5 risks)

| Risk ID | Risk | Category |
|---|---|---|
| R-W1-001 | Organisational design decisions made late — delay dependent module config | Project / Client Readiness |
| R-W1-002 | Data quality issues in legacy HR systems cause migration delays | Data Migration |
| R-W1-003 | Third-party payroll system integration timelines not aligned with HCM go-live | Integration |
| R-W1-004 | Quarterly Oracle release introduces breaking changes to configured functionality | Platform / Technical |
| R-W1-005 | Super-user availability insufficient during UAT | Resource |

**W3S1-002 — Talent Management** (Section 12, 5 risks)

| Risk ID | Risk | Category |
|---|---|---|
| R-W2-001 | Talent profile architecture not agreed before build — rework across all talent modules | Design Readiness |
| R-W2-002 | Goal framework not aligned across organisation | Project / Business Readiness |
| R-W2-003 | HCM Core phase not complete when Talent phase begins — dependency rework | Sequencing / Dependency |
| R-W2-004 | Performance calendar changes after configuration committed | Change Control |
| R-W2-005 | Talent review and calibration not tested in UAT | Testing |

**W3S1-003 — Recruiting Cloud** (Section 13): Structured risk register — content not read in full  
**W3S1-004 — Learning Cloud** (Section 14): Structured risk register — content not read in full  
**W3S1-005 — Workforce Compensation** (Section 14): Structured risk register — content not read in full  
**W3S1-006 — HCM Analytics** (Section 14): Structured risk register — content not read in full  
**W3S1-007 — Workforce Management** (Section 14): Structured risk register — content not read in full  
**W3S1-008 — Help Desk / HR Service Delivery** (Section 15): Structured risk register — content not read in full  
**W3S1-009 — Payroll Interface / Integration** (Section 14): Structured risk register — content not read in full  

**Estimated total risk entries across W3S1-001 to W3S1-009:** 40–50 individual risks

**Common risk categories appearing in Oracle HCM capability risk registers:**
- Organisational design / client readiness
- Data migration quality
- Integration dependency management
- Oracle platform quarterly release cycle
- Resource availability (super-users, project sponsors)
- Module sequencing and dependency
- Change control after configuration sign-off
- Testing completeness

#### Acumatica Capability Assets

**W1S2-006 — Acumatica Field Services** (Section 11.3, 6 risks — "Factual Risk Register")

| Risk ID | Risk | Category |
|---|---|---|
| R-W6-001 | Source text is Acumatica product marketing copy | Content quality |
| R-W6-002 | Source client named in tender-facing content | Governance |
| R-W6-003 | WorkWave Routing Engine presented as standard Field Services | Scope |
| R-W6-004 | Limited source coverage in Section 2 | Evidence |
| R-W6-005 | Time capture read as payroll processing | Scope boundary |
| R-W6-006 | Fixed Assets conflated with Field Services equipment | Scope boundary |

**Note:** These are content/knowledge risks, not delivery risks. They are specific to the KB asset, not the delivery methodology. They should not be extracted into the client-facing Risk Library.

**W1S2-007 — Acumatica Payroll Integration** (Section 8.3, 5 risks)

| Risk ID | Risk | Category |
|---|---|---|
| R-W7-001 | No corpus evidence — content accuracy depends on BU Lead decision quality | Content quality |
| R-W7-002 | PaySpace-only scope — other payroll systems not covered | Scope limitation |
| R-W7-003 | No named reference clients | Evidence |
| R-W7-004 | Integration method commitment risk — contractual exposure | Commercial |
| R-W7-005 | Bespoke mapping requirements beyond standard patterns — scope underestimation | Commercial / Delivery |

**Note:** R-W7-004 and R-W7-005 are genuine delivery risks that could appear in a client-facing Risk Register. R-W7-001 to R-W7-003 are internal KB quality risks.

---

### 3.3 Risk-Adjacent Language in Assumption Packs

Assumption packs are commercial commitments, not risk documents. However, several assumptions contain explicit risk language that identifies delivery risk categories:

| Assumption Reference | Risk Category | Extract |
|---|---|---|
| ERP-GEN-008 | Project Risk | "Changes to the legal entity structure after legal entity configuration is complete may require significant rework. APPSolve flags legal entity design changes as a project risk with scope impact." |
| OIC-CON-004 | Integration Risk | "APPSolve cannot guarantee third-party vendor API uptime, API versioning stability, or vendor response times during the integration project... APPSolve will document the impact and raise it as a project risk for the client to manage with the vendor." |
| HCM assumption (W3S1-001) | Project Risk | "The absence of an empowered Project Sponsor is a significant project risk and is the client's responsibility to address." |
| BB-EXT-003 | Integration / Platform Risk | "AVS is not available from all supported banks. Where the client's bank does not offer AVS, BeBanking proceeds without this control and the fact is noted in the project risk register." |
| HCM-CUT-005 | Delivery Risk | Payroll parallel run waiver requires written acceptance of risk |

**Key finding:** The assumption packs identify project risks to be managed but do not themselves constitute a risk register. They define the conditions that create risk — the Risk Library will define how APPSolve identifies, rates, and mitigates those risks.

---

### 3.4 Risk Management Framework Content (Embedded)

**W2S1-005 Section 10.1 — Risk Management**

This is the only governance-level description of APPSolve's risk management approach:

> "A centralised risk log is maintained for all identified risks. Risks rated by impact and likelihood at bi-weekly team reviews. Mitigation and reduction ownership assigned at project-team level. Risks where mitigation is blocked are escalated by the Project Manager to the Project Steering Committee. Consistent approach, clear ownership, and communicated risk policies across the project team."

This paragraph is the entirety of APPSolve's published risk management framework. It establishes:
- A centralised risk log (RAID log)
- Impact × Likelihood rating
- PM ownership
- Bi-weekly review cadence
- Steering Committee escalation

This content is directly usable as the basis for METH-X07 (Risk Management Approach) and the Risk Library standard.

**W5-METH-001 Section 10.1** — identical content, de-branded.

**W3S1-001 (HCM Core Section 9) — Delivery approach mention:**
> "Risk management: A centralised risk log is maintained throughout the engagement. Risks are assessed for impact and likelihood at bi-weekly team meetings; unmitigated risks are escalated to the steering committee. The risk log is available to the client at all times."

The phrase "risk log is available to the client at all times" is important — it confirms that the RAID log is a client-facing document, not internal only. This shapes the Risk Library design.

---

### 3.5 Commercial Risk Content in Gap Reports

Multiple gap reports contain explicit commercial risk documentation:

**OIC_GAP_REPORT.md** (10+ commercial risks):
- Integration tier complexity scoring not defined → estimation methodology risk
- No documented pricing consistency → bid-to-bid pricing variation risk
- Integration inventory inconsistency → scope dispute risk at UAT
- Accelerator discount application not governed → pricing error risk
- Mapping Specification inconsistency → sign-off and dispute risk
- TDD (Technical Design Document) without structured format → scope dispute risk
- No completed OIC client reference → competitive positioning risk
- SFTP server responsibility unclear → operational risk and cost exposure
- EDI position undefined → scope uncertainty
- Post-delivery API change responsibility undefined → contractual exposure

**BEBANKING_GAP_REPORT.md:**
- Bank format register not complete → estimation error risk (commercial risk)
- Different bank formats have materially different implementation complexity

**AMS_GAP_REPORT.md, ERP_GAP_REPORT.md:**
- Commercial risks rated HIGH — resolve within current quarter

**Key finding:** Gap reports contain the most detailed commercial risk analysis in the KB. These document risks at the KB programme level (content gaps), not at the project delivery level. However, the commercial risk categories they identify (estimation, scope, contractual exposure) map directly to the Risk Library categories needed for proposal section S-50 (Risk Register).

---

### 3.6 RAID Log References in Delivery Documents

The RAID log (Risks, Assumptions, Issues, Dependencies) is listed as a standard Mobilize deliverable in:
- **All 13 delivery patterns** (DELIVERY_PATTERN_LIBRARY.md) — "Kick-off pack, RAID log, comms plan" in MOB phase
- **All 7 project plan templates** (PROJECT_PLAN_TEMPLATES.md) — "RAID log setup" in MOB phase

**Key finding:** The RAID log is an established project delivery artefact in APPSolve's methodology. It is referenced consistently across all patterns and templates. However, no RAID log template, no RAID structure definition, and no standard risk categories exist — only the reference to the artefact name. This gap prevents automated assembly of the RAID Framework section (S-37) of the proposal.

---

### 3.7 Risk Rating Framework (Implied)

The following rating approaches are referenced across KB documents without a formal standard:

| Source | Rating approach |
|---|---|
| W3S1-001 Risk Register | Likelihood (Low/Medium/High) × Impact (Medium/High) — informal |
| GOVERNANCE_RISK_REGISTER.md | Likelihood × Impact → Rating (LOW/MEDIUM/HIGH/CRITICAL) |
| OIC_GAP_REPORT.md | Severity ratings (HIGH, MEDIUM, LOW) without matrix |
| WP18A PROPOSAL_GAP_ANALYSIS_FRAMEWORK.md | SEV-1 to SEV-4 for gap severity |

**Key finding:** No consistent risk rating framework exists. Three different scales are used across different parts of the KB. The Risk Library must define a single, governed Likelihood × Impact rating matrix and enforce it across all proposal risk registers.

---

## 4. Risk Content by Category — Gap Analysis

Assessment against the 15 risk categories listed in the WP18B brief:

| Category | Current Content | Source | Reusable Entries | Gap |
|---|---|---|---|---|
| Technical | Oracle platform quarterly release, OCI security, EBS patching | W3S1 risk registers | ~8–10 entries | Need Acumatica and BeBanking technical risks |
| Commercial | Pricing methodology, scope dispute, contractual exposure | OIC + BeBanking gap reports | ~15 entries | Need standard commercial risk templates |
| Project | Sponsor authority, design decisions, change control | W3S1 risk registers + HCM assumption | ~8–10 entries | Need cross-BU project risk standards |
| Resource | Super-user availability, consultant continuity | W3S1-001 R-W1-005 | ~3–5 entries | Need PM, BU Lead, client resource risks |
| Infrastructure | OCI security, EBS infrastructure, BeBanking bank connectivity | W2S1-005 + gap reports | ~3 entries | Need OCI infrastructure risk taxonomy |
| Integration | API stability, payroll integration, vendor API uptime | OIC-CON-004, W3S1-001, W3S1-009 | ~6–8 entries | Need BeBanking bank channel risks |
| Security | None (empty `05_Methodologies/Security/`) | None | 0 | Full gap |
| Data | Data migration quality, legacy data completeness | W3S1-001, W2S1-005, ERP-GEN-008 | ~5 entries | Need Acumatica data migration risks |
| Migration | FBDI migration, trial run approach | W2S1-005 | ~3 entries | Need migration risk taxonomy |
| Cutover | Payroll parallel run, go-live contingency | W2S1-005 Section 7.4 | ~3 entries | Need structured cutover risk register |
| Operational | SLA breach, AMS steady state | AMS pack, W2S1-004 | ~3 entries | Need AMS operational risk taxonomy |
| Client Dependencies | Data provision, design sign-off, sponsor availability | W3S1 risk registers | ~5–8 entries | Need cross-BU client dependency risks |
| Compliance | BEE expiry, OPN revalidation, Directors' Resolution | GOVERNANCE_RISK_REGISTER.md + compliance checks | ~4 entries (governance) | Need proposal-level compliance risks |
| Change Management | Training adoption, super-user readiness | W3S1-001 R-W1-005 | ~2–3 entries | Need full change management risk category |
| Third Party | Vendor API stability, bank connectivity | OIC-CON-004, BB-EXT-003 | ~4 entries | Need third-party SLA and dependency risks |

**Categories with zero risk content:** Security (complete gap)  
**Categories with partial content extractable:** All others (2–15 entries each)  
**Estimated total extractable risk entries from existing KB:** 55–80 individual risk entries across all categories

---

## 5. RAID Log Structure — What Exists

The Delivery Pattern Library and Project Plan Templates confirm that every APPSolve engagement produces a RAID log in the Mobilize phase. However, no RAID log template or structure exists in the KB.

**RAID components as implied by existing documents:**

| Component | Evidence | Current definition |
|---|---|---|
| **R — Risks** | W2S1-005 Section 10.1; risk registers in capability assets | Likelihood × Impact rating; PM ownership; bi-weekly review |
| **A — Assumptions** | Assumption schedules (full assembly, 13 packs); ASSUMPTION_SCHEDULE_STANDARD.md | FULLY DEFINED — the entire Assumption Library governs this component |
| **I — Issues** | W2S1-005 Section 10.2 (Issue Management) | Issue log with PM-led resolution; escalation path defined |
| **D — Dependencies** | Assumption packs (DEP code sections) | DEP sections in assumption packs define client dependencies; not project dependencies |

**Key finding:** The A (Assumptions) component of RAID is the most fully governed component in the KB — the entire Assumption Factory handles this. The R (Risks) component has content in capability assets but no standard. The I (Issues) component has a process description but no template. The D (Dependencies) component has assumption-pack-level client dependencies but no project dependency log structure.

---

## 6. Gap Analysis Summary — Risk Library vs Proposal Requirements

The Proposal Factory requires two risk-related sections (from PROPOSAL_SECTION_LIBRARY.md):

| Section | ID | Description | Current automation level | Blocker |
|---|---|---|---|---|
| RAID Framework | S-37 | Risk, Assumptions, Issues, Dependencies register for the engagement | L1 (manual) | No Risk Library; no RAID template |
| Risk Register | S-50 | Standalone risk register for the proposal | L1 (manual) | No Risk Library exists; AI-generate with mandatory human review as interim |

Both are blocked by the absence of the Risk Library. Until the Risk Library is built:
- Gap Analysis Engine will flag G-RISK for every tender
- Assembly method falls back to AI-GENERATE with mandatory human review
- No deterministic risk assembly is possible

---

## 7. Risk Categories Recommended for Risk Library

Based on audit findings, the following 15 categories cover the full risk surface found across the KB:

| Code | Category | Source evidence | Extractable entries |
|---|---|---|---|
| RC-TECH | Technical Risk | W3S1 registers, platform risks | 8–10 |
| RC-COMM | Commercial Risk | OIC gap reports, BeBanking gap | 10–15 |
| RC-PROJ | Project Risk | W3S1 registers, HCM assumptions | 8–10 |
| RC-RES | Resource Risk | W3S1-001 R-W1-005, delivery patterns | 3–5 |
| RC-INFRA | Infrastructure Risk | W2S1-005, OCI references | 3–5 |
| RC-INT | Integration Risk | OIC pack, OIC-CON-004, W3S1-003 | 6–8 |
| RC-SEC | Security Risk | None (complete gap) | 0 |
| RC-DATA | Data Risk | W3S1-001 R-W1-002, ERP-GEN-008, FBDI sections | 5–7 |
| RC-MIG | Migration Risk | W2S1-005, data migration references | 3–4 |
| RC-CUT | Cutover Risk | W2S1-005, HCM-CUT-005, cutover sections | 3–4 |
| RC-OPS | Operational Risk | AMS pack, W2S1-004 | 3–4 |
| RC-CLIENT | Client Dependency Risk | W3S1 registers, HCM assumptions | 5–8 |
| RC-COMP | Compliance Risk | GOVERNANCE_RISK_REGISTER.md | 4–5 |
| RC-CM | Change Management Risk | W3S1-001 R-W1-005 | 2–3 |
| RC-3P | Third Party Risk | OIC-CON-004, BB-EXT-003 | 4–5 |

**Total estimated extractable risk entries: 68–103**

---

## 8. Risk Rating Framework Assessment

The Risk Library must define a single, governed rating framework. Based on what is implied in existing documents:

**Recommended: 3×3 Likelihood × Impact matrix**

| | Low Impact | Medium Impact | High Impact |
|---|---|---|---|
| **Low Likelihood** | LOW | LOW | MEDIUM |
| **Medium Likelihood** | LOW | MEDIUM | HIGH |
| **High Likelihood** | MEDIUM | HIGH | CRITICAL |

**This maps to:**
- GOVERNANCE_RISK_REGISTER.md ratings (LOW / MEDIUM / HIGH)
- W3S1 register informal ratings
- PROPOSAL_GAP_ANALYSIS_FRAMEWORK.md SEV-1 to SEV-4 scale (CRITICAL = SEV-1)

A 3×3 matrix is recommended over 5×5 because:
- Simpler to apply consistently across all proposal Risk Registers
- Sufficient granularity for the risk content available in the KB
- Consistent with W3S1 implicit rating approach (Low/Medium/High on both axes)

---

## 9. Key Audit Findings Summary

| # | Finding | Impact |
|---|---|---|
| F-R01 | No formal Risk Library exists anywhere in the KB | CRITICAL — blocks S-37 and S-50 automation |
| F-R02 | No risk taxonomy, category definitions, or standard risk register template exists | HIGH — every Risk Register is currently authored ad hoc |
| F-R03 | No consistent risk rating framework — 3 different scales used across KB | HIGH — inconsistent Risk Registers undermine proposal quality |
| F-R04 | 11+ capability assets contain structured risk registers with 55–80 individual risk entries | HIGH (positive) — substantial extractable content for Risk Library |
| F-R05 | W2S1-005 Section 10.1 is the only risk management framework description | HIGH — this is the entire published risk management approach; must be expanded |
| F-R06 | RAID log is listed in every delivery pattern and project template but no RAID template or structure exists | HIGH — RAID Framework section (S-37) cannot be assembled without this |
| F-R07 | Assumption component of RAID is fully governed (Assumption Library); Risk component has no governance | MEDIUM — RAID is 75% defined; Risk component is the missing 25% |
| F-R08 | OIC Gap Report contains 10+ commercial risk entries that are directly usable in commercial risk categories | MEDIUM (positive) — good commercial risk source |
| F-R09 | Assumption packs contain risk-adjacent language (EXC/DEP/CON codes) identifying risk conditions, not risk entries | LOW — informs Risk Library content; does not replace it |
| F-R10 | GOVERNANCE_RISK_REGISTER.md is governance programme risk, not delivery risk — not reusable in Risk Library | LOW — clarification only; no content reuse |

---

## 10. Recommended Actions for WP18B Phase 3

| Priority | Action | Rationale |
|---|---|---|
| **A1** | Define Risk Library taxonomy (15 categories, coding standard, rating matrix) | Foundation for all other risk work |
| **A2** | Design standard Risk Register template aligned to RAID structure | Enables S-37 and S-50 proposal sections |
| **A3** | Extract risk entries from W3S1-001 to W3S1-009 and classify by category | 40–50 immediate entries; highest ROI source |
| **A4** | Extract commercial risk entries from OIC_GAP_REPORT.md | 10–15 commercial risk entries; ready to classify |
| **A5** | Define security risk category from first principles (no source material) | RC-SEC is a complete gap; requires risk taxonomy first then AI-assisted drafting with BU review |
| **A6** | Define RAID log template structure | Required before any RAID Framework section can be assembled |

---

*WP18B2_RISK_LIBRARY_AUDIT.md v1.0 | WP18B — Methodology & Risk Library Foundation | 2026-06-25*  
*Phase 1 Risk Library Audit. No formal Risk Library exists. 55–80 risk entries extractable from 11+ capability assets. Feeds: RISK_LIBRARY_STANDARD.md*
