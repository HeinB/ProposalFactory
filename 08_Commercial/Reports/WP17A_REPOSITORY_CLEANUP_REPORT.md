---
document_id: WP17A-REPOSITORY-CLEANUP-REPORT
title: "WP17A — Repository Hygiene and Assembly Readiness Cleanup Report"
version: "1.0"
status: "Complete"
created: "2026-06-19"
created_by: "WP17A — Repository Hygiene and Assembly Readiness Cleanup"
source_audit: "00_Governance/WP17A0_DIRECTORY_STRUCTURE_AUDIT.md"
category: "Governance / Cleanup Report"
scope: "Repository hygiene before Assembly Engine build (WP17B)"
---

# WP17A — Repository Hygiene and Assembly Readiness Cleanup Report

**Date:** 2026-06-19  
**Status:** COMPLETE  
**Source audit:** `00_Governance/WP17A0_DIRECTORY_STRUCTURE_AUDIT.md`  
**Scope:** Light targeted cleanup — no assumption content, governance decisions, or approved pack content was modified.

---

## 1. Executive Summary

All six cleanup tasks from WP17A were completed successfully. The repository passed all validation checks. The Tender Knowledge Base is now Assembly Ready.

**Before:** 373 files, 16 top-level folders. Active governance documents buried among 66 historical records. Assembly engine components scattered in 00_Governance. Active KB assets had 2 duplicates and 4 misplaced files. Pipeline staging areas held 47 stale files alongside 1 active README.

**After:** All 49 approved assets correctly placed with single authoritative paths. 7 Assembly Engine components consolidated in `08_Commercial/Assembly_Engine/`. 25 WP process reports in `08_Commercial/Reports/`. 66 historical records archived to `00_Governance/Archive/`. 47 superseded pipeline files moved to `_Archived_Superseded/`. Pipeline staging areas contain only archive. No active duplicates.

**Assembly readiness verdict: READY. No known path ambiguities or structural blockers for WP17B.**

---

## 2. Files Moved

### 2.1 Assembly Engine Components — 00_Governance → 08_Commercial/Assembly_Engine/ (7 files)

| File | From | To |
|---|---|---|
| ASSEMBLY_READINESS_MATRIX.md | `00_Governance/` | `08_Commercial/Assembly_Engine/` |
| ASSEMBLY_RULES_ENGINE.md | `00_Governance/` | `08_Commercial/Assembly_Engine/` |
| TENDER_BOM_LIBRARY.md | `00_Governance/` | `08_Commercial/Assembly_Engine/` |
| PROPOSAL_STRUCTURE_LIBRARY.md | `00_Governance/` | `08_Commercial/Assembly_Engine/` |
| DELIVERY_PATTERN_LIBRARY.md | `00_Governance/` | `08_Commercial/Assembly_Engine/` |
| PROJECT_PLAN_TEMPLATES.md | `00_Governance/` | `08_Commercial/Assembly_Engine/` |
| ESTIMATION_INPUT_MODEL.md | `00_Governance/` | `08_Commercial/Assembly_Engine/` |

### 2.2 WP Process Reports — 08_Commercial/ root → 08_Commercial/Reports/ (25 files)

All WP14–WP17A process reports moved. Active governance documents retained at root.

| Files moved | Range |
|---|---|
| WP14C through WP14G (5 reports) | BeBanking remediation, Acumatica decision, governance reconciliation |
| WP15A through WP15F (11 packs/reports) | Acumatica decision harvest + workshop; EBS overlay remediation, harvest, promotion |
| WP16A through WP16D (7 reports) | Library reconciliation, HCM decisions, governance programme closure, journeys |
| ASSUMPTION_LIBRARY_MASTER_REVIEW.xlsx + _REPORT.md (2 files) | WP14B master review workbook |

### 2.3 Oracle KB Asset Placements Corrected (4 files in 06_Capabilities/Oracle/)

| File | From | To |
|---|---|---|
| W4-ERP-001-ORA-FusionFinancials.md | `06_Capabilities/Oracle/` | `06_Capabilities/Oracle/Oracle_ERP/` |
| W4-ERP-002-ORA-FusionProcurement.md | `06_Capabilities/Oracle/` | `06_Capabilities/Oracle/Oracle_ERP/` |
| W4-ERP-003-ORA-PPM.md | `06_Capabilities/Oracle/` | `06_Capabilities/Oracle/Oracle_ERP/` |
| W4-INT-001-ORA-OICAccelerators.md | `06_Capabilities/Oracle/` | `06_Capabilities/Oracle/Oracle_OIC/` |

**Also corrected:**

| File | From | To |
|---|---|---|
| W1S1-003-ORA-OraclePartnership.md | `06_Capabilities/Oracle/Oracle_ERP/` | `06_Capabilities/Oracle/` root |
| W5-METH-001-ERP-ImplementationMethodology.md | `07_Approved_Content/Approved/` root | `07_Approved_Content/Approved/Cross_BU/` |

---

## 3. Files Archived

### 3.1 00_Governance/Archive/ — 66 historical files

| Category | Files | Count |
|---|---|---|
| Session records | SESSION_A_CLOSEOUT, Session_A_Review_Workbook, SESSION_B_APPROVAL_PACK/SUMMARY/STATUS, SESSION_C_APPROVAL_PACK/PLAN/SUMMARY/REVIEW/IMPACT/FACT_BASELINE | 11 |
| Checkpoints and milestones | CHECKPOINT_WAVE1, CHECKPOINT_ORACLE_WAVE2, MILESTONE_2026-06-10, APPROVAL_SUMMARY_WAVE1 | 4 |
| Wave planning documents | ORACLE_WAVE2_EXECUTION_PLAN, ORACLE_WAVE2_SOURCE_MAP, POST_WAVE1_ROADMAP, WAVE1_CLOSEOUT, WAVE1_EXTRACTION_SUMMARY, WAVE1_REVIEW_PACK, WAVE2_CANDIDATE_DECISIONS, WAVE3_HCM_SOURCE_DISCOVERY_REPORT, WAVE4_CLOSURE/DISCOVERY/PORTFOLIO/PROMOTION_REVIEW | 12 |
| SVR files (Wave 3) | SVR-W3S1-005 through SVR-W3S1-009 | 5 |
| Pre-extraction notes | ORACLE_FINANCE_SOURCE_NOTES, W2S1-003_READINESS_REPORT, W2S1-005-PRE-EXTRACTION-READINESS, FUSION_EXTRACTION_NOTES, EVIDENCE_UPGRADE_PLAN | 5 |
| Stale / superseded assessment docs | CURRENT_STATE, CONTENT_GAP_ANALYSIS, KNOWLEDGE_BASE_STATUS, APPROVED_TENDER_CONTENT, APPROVED_CONTENT_PLACEMENT_PLAN, APPROVED_CONTENT_USAGE_GUIDE | 6 |
| RAG and automation historical docs | RAG_INSTRUCTIONS, TENDER_RAG_HANDOVER, ANSWER_ASSEMBLY_FRAMEWORK, RESPONSE_ASSEMBLY_TEST, AUTOMATION_READINESS_SCORECARD, UPDATED_AUTOMATION_SCORECARD, TENDER_AUTOMATION_ROADMAP | 7 |
| Historical planning / taxonomy | REVIEW_QUEUE_APPROVAL_PACK, ORACLE_TENDER_READINESS_ASSESSMENT, FACT_RESOLUTION_REPORT, GAP_ANALYSIS_FROM_REAL_TENDER, GAP_REGISTER, READINESS_DELTA_REPORT, TENDER_COVERAGE_REPORT, WEBSITE_ALIGNMENT_REPORT, WP7_RECOMMENDATIONS | 9 |
| Extraction and methodology planning | EXTRACTION_PLAN, EXTRACTION_WORKFLOW, CORPUS_DISCOVERY_PLAN, MASTER_TEMPLATE_REGISTER, METHODOLOGY_LIBRARY_DESIGN, TENDER_COMPONENT_LIBRARY, TENDER_QUESTION_TAXONOMY | 7 |

### 3.2 Duplicate KB Files — 06_Capabilities/ → 99_Archive/ (2 files)

| File | Removed From | Authoritative Location Retained |
|---|---|---|
| W1S2-003-ACU-Inventory.md | `06_Capabilities/Acumatica/ERP/` | `06_Capabilities/Acumatica/Distribution/` |
| W1S3-010-BB-MonitoringAutomation.md | `06_Capabilities/BeBanking/Banking/` | `06_Capabilities/BeBanking/Architecture/` |

---

## 4. Duplicates Removed

| Asset | Duplicate Location (removed) | Authoritative Location (retained) | Rationale |
|---|---|---|---|
| W1S2-003-ACU-Inventory.md | `06_Capabilities/Acumatica/ERP/` | `06_Capabilities/Acumatica/Distribution/` | Inventory is a Distribution capability, not ERP-specific; copy sent to 99_Archive |
| W1S3-010-BB-MonitoringAutomation.md | `06_Capabilities/BeBanking/Banking/` | `06_Capabilities/BeBanking/Architecture/` | Monitoring/Automation is an Architecture-layer capability; copy sent to 99_Archive |

**Indexes updated:** MASTER_CAPABILITY_INDEX.md paths verified against `07_Approved_Content/Approved/` (authoritative sources unchanged). Both assets remain correctly referenced by their approved paths.

---

## 5. Candidate Pipeline Results

### 5.1 Candidate_Content — Classification

| Stage | Files | Classification | Action |
|---|---|---|---|
| `_Archived_Superseded/` (pre-WP17A) | 18 | Already archived (W1S1 and W1S3 DRAFTs) | No action — already correct |
| `Acumatica/` | 7 | Approved — all 7 assets in `07_Approved_Content/Approved/Acumatica/` | Moved to `_Archived_Superseded/` |
| `Cross_BU/` | 3 | Approved — W1S1-002/003/006 in `Approved/Cross_BU/` | Moved to `_Archived_Superseded/` |
| `Oracle/` | 17 | 15 Approved (W3S1-001–009 + W4 × 6); W3S1-001-SVR = SVR doc (not capability); W4-HCM-004 = RETIRED | Moved all to `_Archived_Superseded/` |

**Total moved to _Archived_Superseded/ from Candidate_Content:** 27 additional files

### 5.2 Review_Required — Classification

| Stage | Files | Classification | Action |
|---|---|---|---|
| `Acumatica/` | 6 | Approved — all in `07_Approved_Content/Approved/Acumatica/` | Moved to new `Review_Required/_Archived_Superseded/` |
| `BeBanking/` | 10 | Approved — all in `07_Approved_Content/Approved/BeBanking/` | Moved to `Review_Required/_Archived_Superseded/` |
| `Cross_BU/` | 6 | Approved — all in `07_Approved_Content/Approved/Cross_BU/` | Moved to `Review_Required/_Archived_Superseded/` |
| `Oracle/` | 2 | Approved — W3S1-001 and W3S1-002 in `Approved/Oracle/` | Moved to `Review_Required/_Archived_Superseded/` |

**Total moved to _Archived_Superseded/ from Review_Required:** 24 files

### 5.3 Pipeline Summary

| Status | Count |
|---|---|
| **Approved (all Waves 1–4)** | **49** |
| Superseded/archived DRAFT copies | 45 (Candidate_Content) + 24 (Review_Required) = **69** |
| RETIRED (W4-HCM-004 T&L) | 1 |
| Active pipeline items (genuinely awaiting review) | **0** |
| Items in Candidate_Content/README.md | 1 (retained) |
| Items in Review_Required/README.md | 1 (retained) |

---

## 6. Validation Results

| Check | Result | Notes |
|---|---|---|
| No active duplicate KB assets | **PASS** | `find 06_Capabilities -name "*.md" | xargs basename | sort | uniq -d` = empty |
| W4-ERP-001/002/003 in Oracle_ERP/ | **PASS** | All 3 files confirmed at `06_Capabilities/Oracle/Oracle_ERP/` |
| W4-INT-001 in Oracle_OIC/ | **PASS** | Confirmed at `06_Capabilities/Oracle/Oracle_OIC/` |
| Oracle/ root has only W1S1-003 | **PASS** | Only one .md file at `06_Capabilities/Oracle/` root |
| W5-METH-001 in Approved/Cross_BU/ | **PASS** | Confirmed at `07_Approved_Content/Approved/Cross_BU/` |
| Assembly engine files NOT in 00_Governance | **PASS** | Zero ASSEMBLY_*/TENDER_BOM*/etc. in 00_Governance root |
| Assembly engine files in 08_Commercial/Assembly_Engine/ | **PASS** | All 7 confirmed present |
| Candidate_Content active files = README only | **PASS** | Only README.md at active levels |
| Review_Required active files = README only | **PASS** | Only README.md at active levels |
| TENDER_ASSUMPTION_ASSEMBLY_RULES.md unchanged | **PASS** | Version remains 1.9 |
| Assumption pack files unchanged | **PASS** | All 13 V1.md files present at unchanged paths |
| MASTER_CAPABILITY_INDEX.md paths updated | **PASS** | All 5 corrected paths verified against disk |
| No broken governance file references | **PASS** | HANDOVER.md and AI_CONTEXT.md updated with new Assembly_Engine location |
| 49 approved assets present | **PASS** | Cross_BU 10 + Oracle 20 + Acumatica 9 + BeBanking 10 = 49 |
| Authoritative assumption library count unchanged | **PASS** | 1,136 approved assumptions across 13 packs — not touched |

---

## 7. Updated Repository Statistics

### Before WP17A

| Metric | Value |
|---|---|
| Total files | ~373 |
| 00_Governance root files | 104 (mixed: active + historical + assembly engine) |
| 08_Commercial root files | ~40 (15 active + 25 WP reports mixed) |
| Active pipeline files (Candidate/Review) | 47 |
| Active KB duplicates | 2 |
| Misplaced ERP/OIC files | 4 |
| Assembly engine files in wrong folder | 7 |
| MASTER_CAPABILITY_INDEX paths incorrect | 5 |

### After WP17A

| Metric | Value |
|---|---|
| 00_Governance root files | **22** (active governance only; +66 archived) |
| 08_Commercial root files | **15** (active governance framework only) |
| 08_Commercial/Assembly_Engine/ | **7** (all assembly engine components) |
| 08_Commercial/Reports/ | **25** (all WP process reports) |
| 00_Governance/Archive/ | **66** (historical records) |
| Active pipeline files (Candidate/Review) | **0** (only README.md; all 69 superseded copies archived) |
| Active KB duplicates | **0** |
| Misplaced ERP/OIC/Partnership/Methodology files | **0** |
| MASTER_CAPABILITY_INDEX paths incorrect | **0** |
| All 49 approved assets with correct paths | **CONFIRMED** |

---

## 8. Assembly Readiness Assessment

### Readiness Checklist

| Criterion | Status | Notes |
|---|---|---|
| Single source of truth for all KB assets | **✅ ACHIEVED** | 49 assets; each has exactly one active path in 06_Capabilities/ |
| No active duplicates | **✅ ACHIEVED** | 0 duplicate KB assets |
| Oracle assets correctly located | **✅ ACHIEVED** | W4-ERP in Oracle_ERP/; W4-INT in Oracle_OIC/; W1S1-003 at Oracle/ root |
| Assembly artefacts correctly located | **✅ ACHIEVED** | All 7 components in 08_Commercial/Assembly_Engine/ |
| Active governance folder clean | **✅ ACHIEVED** | 00_Governance: 22 active files; 66 in Archive/ |
| No broken MASTER_CAPABILITY_INDEX references | **✅ ACHIEVED** | v1.3 — all 5 corrected paths verified |
| Assembly rules unchanged | **✅ CONFIRMED** | TENDER_ASSUMPTION_ASSEMBLY_RULES.md v1.9 untouched |
| Assumption library unchanged | **✅ CONFIRMED** | 13 packs / 1,136 assumptions — all at original paths |
| Pipeline staging areas clear | **✅ ACHIEVED** | Candidate and Review_Required: active files = README only |
| HANDOVER.md and AI_CONTEXT.md updated | **✅ ACHIEVED** | Assembly_Engine location updated; statistics current |

### Verdict

**ASSEMBLY READY. Proceed to WP17B — Assembly Engine Build.**

The repository has a clean, unambiguous structure:
- Every capability asset has exactly one active path
- Assembly engine components are co-located with commercial assets
- Governance folder contains only active registers, logs, and reference documents
- Pipeline staging areas are clean
- All MASTER_CAPABILITY_INDEX paths resolve to existing files

### Deferred Items (No Blocker for WP17B)

The following items were noted in WP17A-0 but not actioned in WP17A (deferred to a future BAU session):

| Item | Location | Status |
|---|---|---|
| BeBanking_CAPABILITY_MAP.md | `00_Governance/` | Should move to `06_Capabilities/BeBanking/` — benign location for now |
| HCM_BASELINE_CHANGE_LOG.md | `08_Commercial/` root | All other pack change logs are in pack subdirs — minor inconsistency; not a blocker |
| ASSUMPTION_REGISTER.csv | `08_Commercial/` root | Legacy HCM-only register (115 rows; superseded by pack-specific registers) — delete at next BAU session after BU Lead confirmation |
| 02_Corporate/Company_Profile/ | `02_Corporate/` | Shadow copies of Cross_BU assets — add README noting `07_Approved_Content/Approved/Cross_BU/` is authoritative; not a blocker |
| Empty scaffold directories (30+) | Various | `06_Capabilities/`, `07_Approved_Content/`, etc. — cosmetic noise; harmless |
| 08_Historical_Tenders/ naming conflict | Top-level | Shares "08" prefix with 08_Commercial; no runtime impact; rename to 14_Historical_Tenders at next cleanup |

---

*WP17A — Repository Hygiene and Assembly Readiness Cleanup v1.0 | 2026-06-19 | COMPLETE*  
*Repository is Assembly Ready. Proceed to WP17B — Assembly Engine Build.*  
*No assumption content, governance decisions, or approved pack content was modified.*
