---
document_id: WP18B-IMPLEMENTATION-PLAN
title: "WP18B Implementation Plan — Methodology & Risk Library Foundation"
version: "1.0"
status: "Complete — WP18B"
created: "2026-06-25"
created_by: "WP18B — Methodology & Risk Library Foundation"
category: "Implementation Plan"
scope: "Defines the implementation roadmap for completing the Methodology Library and Risk Library. Covers priority order, estimated effort, dependencies, quick wins, recommended work packages, expected automation maturity increase, and impact on the Proposal Factory."
---

# WP18B Implementation Plan — Methodology & Risk Library Foundation

**Date:** 2026-06-25 | **Version:** 1.0 | **Status:** Complete  
**Work Package:** WP18B — Methodology & Risk Library Foundation  
**Phase:** Phase 5 of 5 — Implementation Roadmap

---

## 1. WP18B Deliverables — Summary

WP18B has delivered the following 6 deliverables (all complete as of 2026-06-25):

| Deliverable | File | Status |
|---|---|---|
| Phase 1 — Methodology Audit | `08_Commercial/Reports/WP18B1_METHODOLOGY_AUDIT.md` | COMPLETE |
| Phase 1 — Risk Library Audit | `08_Commercial/Reports/WP18B2_RISK_LIBRARY_AUDIT.md` | COMPLETE |
| Phase 2 — Methodology Library Standard | `08_Commercial/METHODOLOGY_LIBRARY_STANDARD.md` | COMPLETE |
| Phase 3 — Risk Library Standard | `08_Commercial/RISK_LIBRARY_STANDARD.md` | COMPLETE |
| Phase 4 — Architecture Documents Updated | 4 files in `08_Commercial/Assembly_Engine/` | COMPLETE (v1.1) |
| Phase 5 — Implementation Plan (this document) | `08_Commercial/Reports/WP18B_IMPLEMENTATION_PLAN.md` | COMPLETE |

WP18B is an architecture and governance work package. It does NOT author methodology content. It does NOT build the Proposal Assembly Engine. It establishes the governed framework that all future work packages will use.

---

## 2. What WP18B Enables

The governance framework established by WP18B enables the following:

| Before WP18B | After WP18B |
|---|---|
| Methodology Library: 1 file (actual 2 — W5-METH-001 untracked) | Methodology Library: 2 approved files; 22-document roadmap; governed standard |
| Risk Library: does not exist | Risk Library: Standard approved; 15 categories defined; RAID template defined; 75–90 entries ready to extract |
| S-37 and S-50 blocked: no framework | S-37 and S-50 unblocked by standard: can be assembled using RC-category taxonomy + 3×3 rating matrix |
| 4 WP18A architecture docs referenced 1 methodology file | 4 WP18A architecture docs reference 2 files + both new standards |
| No methodology approval workflow | Approval workflow defined: same as Capability Library |
| No risk rating standard | Single 3×3 Likelihood × Impact matrix governs all Risk Registers |

---

## 3. What Must Happen Next

WP18B establishes governance. The following work packages must execute against that governance to populate the libraries with usable content.

### 3.1 Immediate actions (no new work package required)

These actions can be completed by the user or in a short follow-on session:

| Action | Who | Effort | Impact |
|---|---|---|---|
| **A1** — Copy W5-METH-001 to `05_Methodologies/Implementation/` | User | 2 minutes | Resolves deployment anomaly; file discoverable as methodology asset |
| **A2** — Create `08_Commercial/Risk_Library/` folder | User | 1 minute | Enables Risk Library content files to be created |
| **A3** — Create `METHODOLOGY_INDEX.md` in `05_Methodologies/` | AI session | 30 minutes | Enables Assembly Engine to discover methodology assets |
| **A4** — Create `RISK_INDEX.md` in `08_Commercial/Risk_Library/` | AI session | 30 minutes | Enables Assembly Engine to discover risk entries |

### 3.2 Quick wins (high value, low effort)

The following produce immediate, approved-content gains from existing KB material:

| Quick Win | Source | Target | Effort | Automation gain |
|---|---|---|---|---|
| **QW1** — Extract W3S1-001 to W3S1-009 risk registers into Risk Library | 9 capability assets (already read) | 9 × RC-category files | LOW (4–6 hours AI + BU review) | S-50 automation: L1 → L2 |
| **QW2** — Extract W2S1-005 Section 10 into METH-X01 draft | W2S1-005 (already approved) | `05_Methodologies/Cross_BU/METH-X01.md` | LOW (2–3 hours AI + BU review) | S-36 automation: L2 → L4 |
| **QW3** — Extract OIC_GAP_REPORT commercial risks into RC-COMM | OIC_GAP_REPORT.md | `08_Commercial/Risk_Library/RC-COMM_Commercial_Risks.md` | LOW (2 hours AI + BU review) | S-50 commercial risk coverage |
| **QW4** — Extract DELIVERY_PATTERN_LIBRARY hypercare + testing → METH-X05 draft | DELIVERY_PATTERN_LIBRARY.md (13 patterns) | `05_Methodologies/Cross_BU/METH-X05.md` | LOW (3–4 hours AI + BU review) | S-42/S-43 automation: L2 → L3 |

**Recommendation:** QW1 and QW3 (Risk Library) should be completed before any tender that requires a Risk Register. QW2 and QW4 can run in parallel.

---

## 4. Recommended Work Package Roadmap

### WP18B-EXT — Risk Library Population (Quick Win batch)

**Objective:** Extract and approve an initial Risk Library corpus from existing KB assets.  
**What:** Extract risk entries from W3S1-001 to W3S1-009, W1S2-007, OIC_GAP_REPORT, BeBanking assumptions, and ERP-GEN-008 into the 15 RC-category files. Get BU Lead approval.  
**Output:** 15 RC-category files in `08_Commercial/Risk_Library/`; `RISK_INDEX.md`; S-50 assembly method upgrades to EXTRACT.  
**Dependencies:** A2 (folder created).  
**Estimated effort:** 1 AI session + BU Lead review.  
**Automation gain:** S-50 L1 → L2; S-37 L1 → L2.

---

### WP18B-METH1 — Cross-BU Methodology Authoring (METH-X01 to METH-X07)

**Objective:** Author the 7 Cross-BU methodology documents using W2S1-005, W5-METH-001, and DELIVERY_PATTERN_LIBRARY as primary sources.  
**What:** 7 documents in priority order: METH-X01 (Project Management), METH-X04 (Testing), METH-X02 (Data Migration), METH-X05 (Go-Live/Cutover), METH-X03 (Change Management), METH-X07 (Risk Management), METH-X06 (QA Framework).  
**Constraint:** Do not author METH-X06 (QA Framework) or METH-X07 (Risk Management) without BU Lead/Delivery Director SME input session first.  
**Dependencies:** METH-X02, METH-X04, METH-X05 require Oracle proposals as source material (listed in METHODOLOGY_LIBRARY_DESIGN.md).  
**Estimated effort:** 3–4 AI sessions + BU Lead approvals per document.  
**Automation gain:**
- S-36 (Project Governance): L2 → L4
- S-39 (Testing Strategy): L2 → L3
- S-40 (Data Migration): L2 → L3
- S-42 (Cutover): L2 → L3
- S-43 (Hypercare): L2 → L3
- S-37 (RAID Framework): L1 → L3

---

### WP18B-METH2 — Oracle Methodology Authoring (METH-O01 to METH-O03)

**Objective:** Author the 3 highest-priority Oracle methodology documents.  
**What:** METH-O03 (Oracle Cloud Fusion — derivable from W2S1-005 + Mauritius Telecom HCM proposal), METH-O01 (Oracle EBS — derivable from SARB + PPro proposals), METH-O06 (Oracle Managed Services — requires SME session).  
**Dependencies:** METH-O01 and METH-O03 require reading historical Oracle proposals (SARB, PPro, Mauritius Telecom). METH-O06 requires service delivery manager SME session.  
**Estimated effort:** 2 AI sessions for O01/O03; 1 SME session + 1 AI session for O06.  
**Automation gain:**
- S-34 (Implementation Methodology): L2 → L4 (Oracle)
- S-36, S-39, S-42 (Oracle-specific): L2 → L4

---

### WP18B-METH3 — Acumatica and BeBanking Methodology Authoring

**Objective:** Author the Acumatica (METH-A01 to A04) and BeBanking (METH-B01 to B04) methodology documents.  
**Constraint:** All 8 documents require SME sessions before authoring — 0% extraction yield from current KB.  
**What:** Conduct BU Lead workshops; then author per the METHODOLOGY_LIBRARY_DESIGN.md specifications.  
**Dependencies:** Acumatica delivery lead availability; BeBanking product owner availability.  
**Estimated effort:** 2 SME workshops + 2 AI authoring sessions per BU.  
**Automation gain:**
- S-34 (Implementation Methodology): L2 → L4 (Acumatica + BeBanking)

---

### WP18B-METH4 — DR and Security Methodology (Empty folder resolution)

**Objective:** Fill the `05_Methodologies/Disaster_Recovery/` and `05_Methodologies/Security/` empty folders.  
**Constraint:** These are the two hardest gaps — no source material exists for either. DR requires OCI/infrastructure specialist; Security requires security architect input.  
**What:** DR methodology (OCI DR patterns, RPO/RTO approach); Security methodology (access control design, role design, OCI security baseline).  
**Dependencies:** OCI specialist availability; security architect availability.  
**Automation gain:**
- S-44 (Disaster Recovery): L1 → L3 (currently 0%)

---

## 5. Full Priority Sequence

| Priority | Work Package | Effort | Dependencies | Automation sections unblocked |
|---|---|---|---|---|
| **P1** | A1 + A2 + A3 + A4 (Immediate actions) | <1 day | None | Foundation for all subsequent work |
| **P2** | WP18B-EXT — Risk Library Population | 1 day | A2 complete | S-50 L1→L2; S-37 L1→L2 |
| **P3** | WP18B-METH1 — Cross-BU Methodology (METH-X01 to X07) | 2–3 weeks | A1 complete | S-34, S-36, S-37, S-39, S-40, S-42, S-43 to L3+ |
| **P4** | WP18B-METH2 — Oracle Methodology (METH-O01, O03, O06) | 2–3 weeks | Oracle proposals readable | S-34 (Oracle) to L4 |
| **P5** | WP18C — Gap Analysis Engine | 2–3 weeks | WP18B-EXT + WP18B-METH1 | S-37 automated; gap detection L1→L4 |
| **P6** | WP18D — Proposal QA Engine | 3–4 weeks | WP18C complete | QA automated L1→L4 |
| **P7** | WP18B-METH3 — Acumatica + BeBanking Methodology | 4–6 weeks (SME dependent) | Acumatica + BeBanking SME sessions | S-34 (Acumatica + BeBanking) to L4 |
| **P8** | WP18B-METH4 — DR + Security Methodology | 4–6 weeks (specialist dependent) | OCI + security specialists | S-44 L1→L3 |
| **P9** | WP19 — Rendering Engine | 3–4 weeks | WP18D complete | S-01, S-02, rendering L1→L4 |
| **P10** | Remaining Oracle methodology (METH-O02, O04, O05, O07) | 2–4 weeks | Specialist inputs | S-34, S-39 deeper Oracle coverage |

---

## 6. Expected Automation Maturity Increase

### 6.1 Overall platform maturity trajectory

| State | Platform maturity | Key improvement |
|---|---|---|
| WP18A baseline | L2.5 | Assumption Factory at L5; all other components L1–L3 |
| After WP18B-EXT (Risk Library) | L2.6 | S-50 and S-37 move from L1 to L2 |
| After WP18B-METH1 (Cross-BU) | L2.9 | S-34, S-36, S-39, S-42, S-43 all move to L3 |
| After WP18B-METH2 (Oracle) | L3.1 | S-34 Oracle moves to L4 |
| After full WP18B + WP18C + WP18D | L3.8 | Gap analysis and QA automated; most methodology sections at L3–L4 |
| Target (WP19 + all methodologies) | L4.2 | Document rendering automated; most sections at L4 |

### 6.2 Section-level maturity improvements (WP18B directly)

| Section | Before WP18B | After WP18B-EXT | After WP18B-METH1 | After WP18B-METH2 |
|---|---|---|---|---|
| S-34 Implementation Methodology | L2 | L2 | L3 | L4 (Oracle) |
| S-36 Project Governance | L2 | L2 | L4 | L4 |
| S-37 RAID Framework | L1 | L2 | L3 | L3 |
| S-39 Testing Strategy | L2 | L2 | L3 | L3 |
| S-40 Data Migration | L2 | L2 | L3 | L3 |
| S-42 Cutover / Go-Live | L2 | L2 | L3 | L3 |
| S-43 Hypercare / Transition | L2 | L2 | L3 | L3 |
| S-50 Risk Register | L1 | L2 | L2 | L2 |

---

## 7. Impact on Proposal Factory

### 7.1 Direct impact on active tenders

For the next tender (e.g., Plennegy or any Oracle HCM tender):
- **S-34 (Implementation Methodology):** W2S1-005 (Oracle) and W5-METH-001 (Cross-BU) are both approved and immediately usable. No gap for Oracle methodology sections.
- **S-36 (Project Governance):** W2S1-005 Section 10 is the immediate source. METH-X01 will improve this to L4 when authored.
- **S-37 (RAID Framework):** RISK_LIBRARY_STANDARD.md provides the structure. Content must be assembled from existing capability asset risk registers until WP18B-EXT is complete.
- **S-50 (Risk Register):** Use RC-category taxonomy from RISK_LIBRARY_STANDARD.md and extract from W3S1-001/W3S1-002 risk registers manually until WP18B-EXT completes. Bid Manager should document 5+ risks using the 3×3 rating matrix.

### 7.2 Proposal Factory source library status after WP18B

| Library | Status | Proposal impact |
|---|---|---|
| Capability Library | COMPLETE — 49 assets | Full deterministic assembly for all BOM-triggered sections |
| Assumption Library | COMPLETE — 1,136 assumptions | S-49 and A-01 at L5 (WP17D-1 complete) |
| Methodology Library | 2 files approved; 20 planned | S-34, S-36 usable immediately; others require authoring |
| Risk Library | Standard defined; content pending | S-37 and S-50 require interim manual assembly; standard provides framework |
| Reference Library | 16 letters | Reference sections usable; AM approval gate still manual |
| Corporate Library | Active | S-03 to S-12 fully deterministic |

### 7.3 Critical path to full Proposal Factory operation

```
WP18B-EXT (Risk Library population)
    └── WP18C (Gap Analysis Engine)
            └── WP18D (QA Engine)
                    └── WP19 (Rendering Engine)

WP18B-METH1 (Cross-BU Methodology)
    └── WP18B-METH2 (Oracle Methodology)
            └── WP18B-METH3 (Acumatica + BeBanking)

Both tracks converge at WP19 — full automated proposal production.
```

---

## 8. WP18B Key Decisions and Architecture Commitments

The following architecture decisions are locked by WP18B governance documents and must be respected by all future work packages:

| Decision | Commitment | Document |
|---|---|---|
| D-MB01 | `05_Methodologies/` is the canonical methodology library root | METHODOLOGY_LIBRARY_STANDARD.md |
| D-MB02 | W5-METH-001 is the primary methodology asset for all non-Oracle tenders; W2S1-005 for Oracle-only | METHODOLOGY_LIBRARY_STANDARD.md |
| D-MB03 | METHODOLOGY_LIBRARY_DESIGN.md (22-document plan, 2026-06-05) is the authoring roadmap; WP18B does not supersede it | METHODOLOGY_LIBRARY_STANDARD.md |
| D-MB04 | METH documents use the same approval workflow as capability assets (BU Lead sign-off for `approved_for_reuse: Yes`) | METHODOLOGY_LIBRARY_STANDARD.md |
| D-RB01 | Risk Library uses 15 RC-category codes (RC-TECH to RC-3P) — no other categories | RISK_LIBRARY_STANDARD.md |
| D-RB02 | Single risk rating framework: 3×3 Likelihood × Impact matrix → LOW/MEDIUM/HIGH/CRITICAL | RISK_LIBRARY_STANDARD.md |
| D-RB03 | Assumption component of RAID is governed by the Assumption Library — not the Risk Library | RISK_LIBRARY_STANDARD.md |
| D-RB04 | Risk Library entries require BU Lead approval before `approved_for_reuse: Yes` — same gate as all KB content | RISK_LIBRARY_STANDARD.md |
| D-RB05 | RAID log is a client-facing document — "available to the client at all times" (from W3S1-001 Section 9) | RISK_LIBRARY_STANDARD.md |

---

## 9. Files Produced by WP18B

| File | Path | Type | Version |
|---|---|---|---|
| WP18B1_METHODOLOGY_AUDIT.md | `08_Commercial/Reports/` | Audit Report | 1.0 |
| WP18B2_RISK_LIBRARY_AUDIT.md | `08_Commercial/Reports/` | Audit Report | 1.0 |
| METHODOLOGY_LIBRARY_STANDARD.md | `08_Commercial/` | Governance Standard | 1.0 |
| RISK_LIBRARY_STANDARD.md | `08_Commercial/` | Governance Standard | 1.0 |
| PROPOSAL_FACTORY_ARCHITECTURE.md | `08_Commercial/Assembly_Engine/` | Architecture Blueprint | 1.1 |
| CONTENT_SOURCE_MATRIX.md | `08_Commercial/Assembly_Engine/` | Content Mapping | 1.1 |
| PROPOSAL_SECTION_LIBRARY.md | `08_Commercial/Assembly_Engine/` | Section Catalogue | 1.1 |
| AUTOMATION_MATURITY_MODEL.md | `08_Commercial/Assembly_Engine/` | Maturity Assessment | 1.1 |
| WP18B_IMPLEMENTATION_PLAN.md | `08_Commercial/Reports/` | Implementation Plan | 1.0 |

---

## 10. WP18B Completion Confirmation

**WP18B is COMPLETE as of 2026-06-25.**

All 5 phases delivered:
- Phase 1: Repository Audit (methodology + risk) — COMPLETE
- Phase 2: Methodology Library Standard — COMPLETE
- Phase 3: Risk Library Standard — COMPLETE
- Phase 4: Architecture document updates (4 docs) — COMPLETE
- Phase 5: Implementation Plan — COMPLETE

Constraints respected:
- No methodology content authored
- No Proposal Assembly Engine built
- Architecture and governance only
- All documents in existing directories (OneDrive mkdir restriction respected)

---

*WP18B_IMPLEMENTATION_PLAN.md v1.0 | WP18B — Methodology & Risk Library Foundation | 2026-06-25*  
*WP18B COMPLETE. Next: WP18B-EXT (Risk Library population — quick win) or WP18C (Gap Analysis Engine).*
