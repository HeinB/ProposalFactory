---
document_id: WP18B1-METHODOLOGY-AUDIT
title: "WP18B Phase 1 — Methodology Library Audit Report"
version: "1.0"
status: "Complete — WP18B Phase 1"
created: "2026-06-25"
created_by: "WP18B — Methodology & Risk Library Foundation"
category: "Audit Report"
scope: "Complete inventory and quality assessment of all methodology assets in the Tender Knowledge Base. Identifies what exists, where it is, whether it is reusable, what is missing, and the recommended library structure for the Methodology Library Standard (METHODOLOGY_LIBRARY_STANDARD.md)."
---

# WP18B Phase 1 — Methodology Library Audit Report

**Date:** 2026-06-25 | **Version:** 1.0 | **Status:** Complete  
**Work Package:** WP18B — Methodology & Risk Library Foundation  
**Phase:** Phase 1 of 5 — Repository Audit  
**Feeds into:** `08_Commercial/METHODOLOGY_LIBRARY_STANDARD.md`

---

## 1. Audit Scope

This audit searched the entire Tender Knowledge Base for:

- Standalone methodology documents in `05_Methodologies/`
- Methodology documents in `07_Approved_Content/`
- Archived methodology design documents in `00_Governance/Archive/`
- Methodology-adjacent content embedded in capability assets (`06_Capabilities/`)
- Delivery methodology references in Assembly Engine documents
- Project methodology references in WP12 reference library files

**Audit date:** 2026-06-25  
**Repository baseline:** 13 packs / 1,136 assumptions / 49 capability assets / WP18A COMPLETE

---

## 2. Summary of Findings

| Finding | Detail |
|---|---|
| Standalone approved methodology files | **2** (not 1 — W5-METH-001 was previously untracked in WP18A) |
| Empty methodology folders | **6 of 7** |
| Archived methodology library design | **1 comprehensive design document (22 documents planned)** |
| Methodology content embedded in capability assets | **11+ files with embedded methodology and risk sections** |
| Methodology coverage gaps by category | **14 of 18 planned categories have zero dedicated methodology content** |
| Critical deployment anomaly | **W5-METH-001 is in `07_Approved_Content/` not in `05_Methodologies/`** |

**Assessment: The Methodology Library has 2 approved files against a planned library of 22 documents. 9% completion. Six of seven folders are empty. However, an archived design document provides a complete, detailed library framework that WP18B can build on directly.**

---

## 3. Approved Methodology Files — Full Inventory

### 3.1 W2S1-005-ORA-ImplementationMethodology.md

| Field | Detail |
|---|---|
| **Document ID** | W2S1-005-ORA-ImplementationMethodology |
| **Title** | Oracle Implementation Methodology |
| **Version** | 1.2 APPROVED |
| **Location** | `05_Methodologies/Implementation/` (canonical) |
| **Also copied to** | `07_Approved_Content/Approved/Oracle/` |
| **approved_for_reuse** | Yes |
| **Approved by** | Hein Blignaut, 2026-06-12 |
| **Wave** | Wave 2 |
| **BU** | Oracle |
| **Scope** | Oracle Fusion Cloud + Oracle EBS only |

**Content summary:**

| Section | Content | Reuse potential |
|---|---|---|
| Sections 1–2 | Executive summary; delivery philosophy (senior-only, standard config, iterative CRP) | HIGH |
| Section 3 | 6-phase overview: Mobilize → Scope & Design → Prototype → Validate → Deploy → Evolve | HIGH |
| Sections 4–9 | Full phase descriptions with entry criteria, activities, and exit deliverables | HIGH |
| Section 10 | Project Governance Framework: risk management, issue management, change control, configuration management | HIGH — directly usable in Risk Library |
| Section 11 | Oracle Delivery Accelerators (OIC, FBDI, Starter Configurator, OGL, Oracle University, OUM, OCI security) | Oracle-specific |
| Sections 12–13 | Oracle Fusion and EBS platform-specific delivery considerations | Oracle-specific |
| Section 14 | Transition to managed services and support | HIGH |
| Section 15 | Why APPSolve (credentials, OIC leadership, local presence) | HIGH |
| Section 16 | Conclusion | HIGH |
| Section 17 | Approval record and pre-tender checks (D-W5-003 to D-W5-006) | Must apply at tender time |
| Appendices A–C | Extraction notes, fact verification, governance review | Internal reference |

**Quality assessment:** EXCELLENT. Comprehensive, evidence-based, all claims traceable to approved sources. Pre-tender checks clearly defined. No governance violations.

**Extraction yield for Methodology Library:**
- For Oracle-specific methodology documents: 70–80%
- For Cross-BU framework: 40–60% (requires de-branding and generalisation)
- Section 10 (governance framework) is directly usable as the basis for METH-X01 and METH-X07

**Reuse restrictions (from pre-tender checks):**
- D-W5-003: Verify OPN annual revalidation before use
- D-W5-004: BEE certificate expires 2026-07-31 (document itself has no BEE content — no action needed at document level)
- D-W5-005: No named client references in this document; select from W2S1-001/002 lists for specific tenders
- D-W5-006: Do not add awards claims without BU Lead confirmation

---

### 3.2 W5-METH-001-ERP-ImplementationMethodology.md

| Field | Detail |
|---|---|
| **Document ID** | W5-METH-001-ERP-ImplementationMethodology |
| **Title** | APPSolve ERP Implementation Methodology (Platform-Agnostic) |
| **Version** | 1.0 APPROVED |
| **Location (actual)** | `07_Approved_Content/Approved/Cross_BU/` |
| **Location (intended per kb_destination)** | `05_Methodologies/Implementation/` |
| **approved_for_reuse** | Yes |
| **Approved by** | Hein Blignaut, 2026-06-14 |
| **Wave** | Wave 5 |
| **BU** | Cross-Platform (Oracle, Acumatica, OCI, OIC, BeBanking) |
| **Derived from** | W2S1-005 — de-branded and generalised |

**CRITICAL FINDING: Deployment anomaly.** W5-METH-001 has `kb_destination: 05_Methodologies/Implementation/W5-METH-001-ERP-ImplementationMethodology.md` in its frontmatter, but the file is NOT in `05_Methodologies/`. It was placed in `07_Approved_Content/Approved/Cross_BU/` during Wave 5. WP18B should note this as a resolution action.

**Content summary:**

| Section | Content | Reuse potential |
|---|---|---|
| Core body | Same 6-phase structure as W2S1-005 but platform-agnostic | HIGH — primary methodology asset for all non-Oracle tenders |
| Usage note | "Use for Acumatica, OCI/OIC, BeBanking, and multi-platform tenders; W2S1-005 for Oracle-only" | HIGH |
| Appendix A | Oracle-specific additions (OUM alignment, FBDI, Modern Best Practices) | Oracle tenders |
| Appendix B | Acumatica-specific additions (import scenarios, Acumatica University) | Acumatica tenders |
| Appendix C | OCI/OIC-specific additions | OCI/OIC tenders |
| Appendix D | BeBanking-specific additions | BeBanking tenders |

**Evidence basis:** Hollywood Bets Oracle HCM (HIST-007), Interconnect Systems Acumatica (W1S2-006), HyDac Acumatica + BeBanking (HIST-005), RedPath Mining Oracle (HIST-008)

**Quality assessment:** GOOD. Directly usable for all multi-platform or non-Oracle tenders. Cross-BU platform appendices provide BU-specific guidance. Pre-tender checks inherited from W2S1-005 base.

---

## 4. Methodology Folder Structure — Current State

| Folder | Files | Status |
|---|---|---|
| `05_Methodologies/Implementation/` | 1 (W2S1-005) | PARTIALLY POPULATED — W5-METH-001 not deployed here |
| `05_Methodologies/Disaster_Recovery/` | 0 | **EMPTY** |
| `05_Methodologies/Managed_Services/` | 0 | **EMPTY** |
| `05_Methodologies/Project_Management/` | 0 | **EMPTY** |
| `05_Methodologies/Security/` | 0 | **EMPTY** |
| `05_Methodologies/Support/` | 0 | **EMPTY** |
| `05_Methodologies/Testing/` | 0 | **EMPTY** |

**Finding:** The current folder structure covers 7 categories. The archived library design identifies 22 documents across 4 folder groups. The folder structure is incomplete relative to the planned library and does not include the Cross_BU, Oracle, Acumatica, or BeBanking subfolders designed in `METHODOLOGY_LIBRARY_DESIGN.md`.

---

## 5. Archived Methodology Design Document

### 5.1 METHODOLOGY_LIBRARY_DESIGN.md

| Field | Detail |
|---|---|
| **Location** | `00_Governance/Archive/METHODOLOGY_LIBRARY_DESIGN.md` |
| **Date** | 2026-06-05 |
| **Status** | Archived design — not yet executed |
| **Purpose** | Define the complete target Methodology Library before authoring begins |

**This document is the most important asset for WP18B.** It contains a complete, detailed library design including:

- 4 design principles (write once cite many; structure for extraction; framework vs execution; authoring from evidence up)
- Cross-BU vs BU-specific decision framework
- 22 document specifications with purpose, sections, source material, and estimated extraction yields
- Priority ranking (top 22 documents by tender frequency × evaluator weight × BU urgency)
- Authoring prerequisites per document
- Summary of extraction vs fresh authoring requirements

**The 22 planned documents from METHODOLOGY_LIBRARY_DESIGN.md:**

| Code | Document | BU | Source Availability | Priority |
|---|---|---|---|---|
| METH-X01 | Project Management Framework | Cross | 50–70% extractable from Oracle proposals | 1 |
| METH-O01 | Oracle EBS Implementation Methodology | Oracle | 60–75% extractable | 2 |
| METH-O03 | Oracle Cloud (Fusion) Implementation Methodology | Oracle | 50–65% extractable | 3 |
| METH-X04 | Testing Methodology | Cross | 30–50% extractable | 4 |
| METH-X02 | Data Migration Methodology | Cross | 40–60% extractable | 5 |
| METH-O06 | Oracle Managed Services Methodology | Oracle | 5–15% extractable | 6 |
| METH-A01 | Acumatica SureStep Implementation Methodology | Acumatica | 0% (SME workshop required) | 7 |
| METH-X05 | Go-Live and Cutover Methodology | Cross | 30–40% extractable | 8 |
| METH-X03 | Change Management and Training Approach | Cross | 30–50% extractable | 9 |
| METH-B01 | BeBanking Client Onboarding Methodology | BeBanking | 0% (SME required) | 10 |
| METH-X07 | Risk Management Approach | Cross | 30–40% extractable | 11 |
| METH-O05 | OIC Integration Delivery Methodology | Oracle | 15–25% extractable | 12 |
| METH-X06 | Quality Assurance Framework | Cross | 0% (author from scratch) | 13 |
| METH-A02 | Acumatica Manufacturing Approach | Acumatica | 0% (SME required) | 14 |
| METH-B02 | BeBanking ERP Integration Methodology | BeBanking | 5–15% extractable | 15 |
| METH-A03 | Acumatica Payroll Approach | Acumatica | 0% (SME required) | 16 |
| METH-B04 | BeBanking Support and Reconciliation Model | BeBanking | 0% (inherits from METH-O06) | 17 |
| METH-O04 | OCI Infrastructure Deployment Methodology | Oracle | 0–10% (OCI specialist required) | 18 |
| METH-A04 | Acumatica Managed Services Methodology | Acumatica | 60% once METH-O06 done | 19 |
| METH-B03 | BeBanking Bank Connectivity Setup | BeBanking | 0% (technical team required) | 20 |
| METH-O02 | Oracle EBS Upgrade Methodology | Oracle | 10–20% extractable | 21 |
| METH-O07 | Oracle APEX Development Methodology | Oracle | 0% (APEX lead required) | 22 |

**Note on folder naming in METHODOLOGY_LIBRARY_DESIGN.md:** The archived design proposes `08_Methodologies/` as the folder path. The actual repository folder is `05_Methodologies/`. The METHODOLOGY_LIBRARY_STANDARD.md should use `05_Methodologies/` as the canonical path.

---

## 6. Methodology Content Embedded in Other Assets

### 6.1 Delivery Pattern Library

`08_Commercial/Assembly_Engine/DELIVERY_PATTERN_LIBRARY.md` (13 patterns) contains methodology-adjacent content for each engagement type:

| Pattern | Methodology elements present |
|---|---|
| All 13 patterns | RAID log listed as MOB phase deliverable |
| All patterns | Testing cycles (CRP, SIT, UAT) defined per pattern |
| All patterns | Hypercare standard defined |
| All patterns | Resource model (who delivers) defined |
| All patterns | Key exclusions and governance notes defined |

**Reuse assessment:** RAID log structure, testing cycles, hypercare model, and resource model from the 13 patterns are directly extractable into METH-X01 (Project Management), METH-X04 (Testing), METH-X05 (Go-Live), and the BU-specific methodology documents. This is the richest secondary source available.

### 6.2 Project Plan Templates

`08_Commercial/Assembly_Engine/PROJECT_PLAN_TEMPLATES.md` (7 templates) contains:
- RAID log setup as Mobilize deliverable (all templates)
- Phase-by-phase activity lists with named deliverables and gate conditions
- Week-based timeline ranges by engagement type

**Reuse assessment:** HIGH — templates directly inform section structure for BU-specific methodology documents.

### 6.3 Capability Asset Embedded Sections

The following capability assets contain methodology-relevant embedded sections:

| Asset | Embedded Sections | Reuse potential |
|---|---|---|
| W3S1-001 (HCM Core) | Delivery approach (Sections 6–9), Risk Register (Section 11), Assumptions Register (Section 12) | HIGH — confirms delivery phases and HCM-specific risks |
| W3S1-002 (Talent Mgmt) | Risk Register (Section 12) — 5 talent-specific delivery risks | HIGH — feeds METH-O03 risk section |
| W3S1-003 (Recruiting Cloud) | Risk Register (Section 13) | HIGH |
| W3S1-004 (Learning Cloud) | Risk Register (Section 14) | HIGH |
| W3S1-005 (Workforce Compensation) | Risk Register (Section 14) | HIGH |
| W3S1-006 (HCM Analytics) | Risk Register (Section 14) | HIGH |
| W3S1-007 (Workforce Management) | Risk Register (Section 14) | HIGH |
| W3S1-008 (Help Desk) | Risk Register (Section 15) | HIGH |
| W3S1-009 (Payroll Interface) | Risk Register (Section 14) | HIGH |
| W1S2-006 (Acumatica Field Services) | Factual Risk Register (Section 11.3) | HIGH — knowledge/content risks |
| W1S2-007 (Acumatica Payroll Integration) | Risk Register (Section 8.3) — 5 integration risks | HIGH — feeds METH-A03 |
| W2S1-001 (Oracle Fusion Capability) | Issue and Risk Management mention | Moderate |

**Key finding:** 11 capability assets each contain structured risk registers. These are the primary source material for the Risk Library (WP18B Phase 3). They are NOT methodology documents — they are evidence that methodology-level risk content already exists embedded in capability assets and needs to be extracted and formalised into a standalone Risk Library.

### 6.4 Resource Response Library

`00_Governance/RESOURCE_RESPONSE_LIBRARY.md` mentions:
> "Project Manager | Day-to-day delivery coordination; risk register; status reporting | Dedicated PM per workstream"

This confirms that risk register ownership sits with the Project Manager role — a structural governance rule that should be reflected in METH-X01 (Project Management Framework).

---

## 7. Methodology Coverage Gap Analysis

Assessment of coverage per the 18 methodology categories listed in the WP18B brief:

| Category | Dedicated File | Coverage | Gap Severity | Notes |
|---|---|---|---|---|
| Oracle Cloud Implementation | W2S1-005 (Oracle), W5-METH-001 (Cross) | PARTIAL | LOW | Good coverage in both files; METH-O03 needed for complete dedicated document |
| Oracle EBS Upgrade | None | NONE | MEDIUM | W2S1-005 has EBS section but no upgrade-specific content |
| Oracle EBS AMS | None | NONE | HIGH | `05_Methodologies/Managed_Services/` empty; W2S1-004 covers AMS from capability perspective |
| Oracle OIC Delivery | None | NONE | HIGH | OIC methodology absent; W5-METH-001 Appendix C covers basics only |
| Oracle HCM Delivery | W2S1-005 (Oracle) | PARTIAL | LOW | Section 12 covers HCM delivery considerations; no standalone HCM-specific file |
| Oracle ERP Delivery | W2S1-005 (Oracle) | PARTIAL | LOW | EBS delivery in Sections 13–14; Cloud ERP in Section 12 |
| Acumatica Implementation | W5-METH-001 (Appendix B) | PARTIAL | HIGH | Appendix B is brief; no full SureStep methodology document |
| BeBanking Implementation | W5-METH-001 (Appendix D) | PARTIAL | HIGH | Appendix D is brief; no full onboarding methodology document |
| Data Migration | None | NONE | HIGH | Referenced in W2S1-005 Sections 5.3, 8.1; no dedicated file |
| Testing | None | NONE | HIGH | `05_Methodologies/Testing/` empty; test cycles in DELIVERY_PATTERN_LIBRARY only |
| Cutover | None | NONE | MEDIUM | Cutover planning described in W2S1-005 Section 7.4 but no dedicated file |
| Hypercare | None | NONE | LOW | Hypercare in W2S1-005 Section 9; DELIVERY_PATTERN_LIBRARY for each pattern |
| Security | None | NONE | HIGH | `05_Methodologies/Security/` empty; OCI security certs mentioned in W2S1-005 but no methodology |
| Managed Services | None | NONE | HIGH | `05_Methodologies/Managed_Services/` empty |
| Disaster Recovery | None | NONE | HIGH | `05_Methodologies/Disaster_Recovery/` empty |
| Project Governance | None (standalone) | PARTIAL | LOW | W2S1-005 Section 10 is comprehensive; needs extraction into standalone file |
| Change Management | None | NONE | MEDIUM | Mentioned in W2S1-005 delivery philosophy; no dedicated methodology |
| Training | None | NONE | LOW | Deploy phase in W2S1-005 Section 8.2 covers training; no dedicated file |

**Gap summary:** 14 of 18 categories have zero dedicated methodology content. 4 have partial coverage (Oracle Cloud, Oracle HCM, Oracle ERP, Project Governance). None have full dedicated methodology documents except Implementation (W2S1-005 + W5-METH-001).

---

## 8. Quality Assessment of Existing Assets

| Asset | Version | Approved | Evidence-based | Extraction yield | Pre-tender checks |
|---|---|---|---|---|---|
| W2S1-005 | 1.2 | Yes — 2026-06-12 | Yes (HIST-007, HIST-008) | 70–80% for Oracle | D-W5-003 to D-W5-006 |
| W5-METH-001 | 1.0 | Yes — 2026-06-14 | Yes (4 sources) | 70–80% for Cross-BU | Inherited from W2S1-005 |
| METHODOLOGY_LIBRARY_DESIGN.md | n/a | No (archived) | Design only | n/a — framework use | n/a |

Both approved methodology files are high-quality and immediately usable in tenders. The archived library design provides a complete authoring roadmap.

---

## 9. Reuse Potential Assessment

### 9.1 Assets that can be extracted into Methodology Library documents NOW

| Source | Target Methodology Document | Estimated Extraction Yield |
|---|---|---|
| W2S1-005 Section 10 | METH-X01 (Project Management Framework) | 60% |
| W2S1-005 Section 10.1 | METH-X07 (Risk Management Approach) | 50% |
| W2S1-005 Sections 7.4, 8–9 | METH-X05 (Go-Live and Cutover) | 40% |
| W5-METH-001 (full) | METH-O03 (Oracle Cloud) + METH-O01 (Oracle EBS) starting point | 60–70% |
| DELIVERY_PATTERN_LIBRARY (13 patterns) | All BU-specific methodology documents (phasing, testing, hypercare) | 40–50% |
| PROJECT_PLAN_TEMPLATES (7 templates) | BU-specific methodology documents (phase structure, deliverables) | 30–40% |
| W3S1-001 to W3S1-009 Risk Registers | Risk Library (WP18B Phase 3) | HIGH — see Risk Audit |
| W2S1-005 Sections 5.3, 8.1 (FBDI, data migration) | METH-X02 (Data Migration) | 30–40% |

### 9.2 Assets that require SME sessions before authoring

| Target Document | SME Required | Why |
|---|---|---|
| METH-A01 (Acumatica SureStep) | Acumatica delivery lead | No source material exists; 0% extraction |
| METH-B01 (BeBanking Onboarding) | BeBanking product owner | No source material exists; 0% extraction |
| METH-O04 (OCI Infrastructure) | OCI specialist | Technical content; 0% extraction |
| METH-O06 (Oracle Managed Services) | Service delivery manager | Brief fragments only; 5–15% extraction |
| METH-A02 (Acumatica Manufacturing) | Acumatica Manufacturing specialist | No source material; 0% extraction |
| METH-A03 (Acumatica Payroll) | Acumatica Payroll specialist | No source material; 0% extraction |

---

## 10. Recommended Library Structure for METHODOLOGY_LIBRARY_STANDARD.md

Based on the audit, the METHODOLOGY_LIBRARY_STANDARD.md should define a library that:

1. **Uses `05_Methodologies/` as the canonical root** (not `08_Methodologies/` as proposed in the archived design)
2. **Adds subfolder structure** below `05_Methodologies/` to align with the 22-document plan
3. **Acknowledges W5-METH-001 deployment anomaly** and provides a path to resolution (copy to `05_Methodologies/Implementation/` or update kb_destination to reflect current location)
4. **Defines a sidecar-style metadata standard** (YAML frontmatter + body structure identical to capability assets)
5. **Defines ownership and approval workflow** (same as capability library: AI drafts → BU Lead reviews → BU Lead approves → `approved_for_reuse: Yes`)
6. **Preserves the METHODOLOGY_LIBRARY_DESIGN.md priority ranking** — the 22 documents in priority order remain the authoring roadmap
7. **Cross-references the Risk Library** so that BU-specific risk sections within methodology documents are derived from Risk Library templates

---

## 11. Recommended Actions for WP18B

| Priority | Action | Rationale |
|---|---|---|
| **A1** | Resolve W5-METH-001 deployment anomaly — copy to `05_Methodologies/Implementation/` | File is not where kb_destination says it should be; causes confusion in assembly |
| **A2** | Design METHODOLOGY_LIBRARY_STANDARD.md with folder structure aligned to 22-document plan | Provides governance framework before authoring begins |
| **A3** | Update CONTENT_SOURCE_MATRIX.md to reference W5-METH-001 as source for Cross-BU methodology sections | Currently only W2S1-005 is referenced |
| **A4** | Extract Section 10 of W2S1-005 into a standalone Project Management Framework section | This section is the highest-reuse methodology content in the KB |
| **A5** | Note Acumatica + BeBanking methodology documents as SME-dependency items | These cannot be authored from existing KB content; require formal SME sessions first |

---

## 12. Key Audit Findings Summary

| # | Finding | Impact |
|---|---|---|
| F-M01 | 2 approved methodology files exist (not 1); W5-METH-001 was not reflected in WP18A Source Matrix | MEDIUM — architecture docs need updating |
| F-M02 | W5-METH-001 deployment anomaly: file is in `07_Approved_Content/` not `05_Methodologies/` | MEDIUM — resolves with copy operation |
| F-M03 | 6 of 7 methodology folders are empty | HIGH — blocks 14 of 18 methodology sections |
| F-M04 | METHODOLOGY_LIBRARY_DESIGN.md (archived) is a complete, detailed library framework — no need to redesign | HIGH (positive) — WP18B builds on this, does not start from scratch |
| F-M05 | 13 delivery patterns in DELIVERY_PATTERN_LIBRARY provide 40–50% of the content for BU-specific methodology docs | HIGH (positive) — underutilised source |
| F-M06 | 11 capability assets have embedded risk registers — methodology-level risk content already exists embedded | HIGH — feeds WP18B Phase 3 (Risk Library) |
| F-M07 | METHODOLOGY_LIBRARY_DESIGN.md uses `08_Methodologies/` folder path; actual folder is `05_Methodologies/` | LOW — path correction only |
| F-M08 | No methodology document exists for: Data Migration, Testing, Cutover, Security, Managed Services, Disaster Recovery, Change Management, Training | HIGH — these are the primary WP18B authoring targets |

---

*WP18B1_METHODOLOGY_AUDIT.md v1.0 | WP18B — Methodology & Risk Library Foundation | 2026-06-25*  
*Phase 1 Methodology Audit. 2 approved files / 22 planned. 14 categories have zero dedicated content. Feeds: METHODOLOGY_LIBRARY_STANDARD.md*
