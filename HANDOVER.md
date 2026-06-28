# Handover
**Last updated:** 2026-06-28 — **WP19D COMPLETE — KNOWLEDGE PLATFORM VERSION 1.0 COMPLETE.** KVE v2.0 (Phase B): 76 validation rules; AREL V1.0 recursive-descent evaluator (86/86 tests PASS); Mode 1 Platform Health (KHS 91/100 — EXCELLENT); KNOWLEDGE_HEALTH_REPORT generated. 5 regression scenarios (ARM-IT045, OIC-P7, Acumatica-P11, BeBanking-P13, OracleHCM-P3) — all 76 rules, deterministic. VALID_PLATFORMS corrected to canonical 6-value set. **KVE is the sole governance gateway.** **Platform maturity L5.0 → L5.1.** **NEXT: WP18D (Risk Selection Engine — RSK assembly rules) → assembly_rules population (mandatory_if AREL expressions for 49 CAP + 13 ASP) → data quality: RC-OPS-001 mandatory_if_engagement; ASM section_code; CAP content_source_type.**

*Previous: 2026-06-28 — WP19C COMPLETE — KNOWLEDGE REGISTRY V1.0 CERTIFIED. KRPE v2.0 (Phase A+B) operational. Registry Build 6 (BUILD-20260628-150801): 213 core assets (49 CAP + 13 ASP + 13 PAT + 82 SEC + 16 REF + 40 RSK) + 1,136 ASM. 1,855 relationships (CON/INC/USE/SUP/APP). AV-011 CLEARED — KVE Phase A: BLOCK=0, ERROR=0. Registry V1.0 CERTIFIED (KNOWLEDGE_REGISTRY_V1_CERTIFICATION.md). Platform maturity L4.3 → L5.0.*

*Previous: 2026-06-28 — WP19B COMPLETE — AREL V1.0 FROZEN. 4 deliverables: ASSEMBLY_RULE_EXPRESSION_LANGUAGE.md (grammar; 3 operators; 20 context variables; null-safe semantics), ASSEMBLY_RULE_VALIDATION_STANDARD.md (30 ARVAL rules; 3 validation tiers), ASSEMBLY_RULE_TEST_SUITE.md (80 test cases; 12 sections; 100% pass threshold), WP19B_EXPRESSION_LANGUAGE_REPORT.md. AREL V1.0 frozen: `==`, `!=`, `>`, `>=`, `<`, `<=`, `in`, `not in`, `contains`, `and`, `or`, `not`; double-quotes only; null→false for all operators. Canonical platform vocabulary: 6 values. KVE VALID_PLATFORMS update required in Phase B. Platform maturity L4.1 → L4.2.*

*Previous: 2026-06-28 — WP19A.1 COMPLETE — Registry Data Quality Remediation. 16 KRPE defects fixed (v1.0 → v1.1): `governance_notes`, `pattern_applicability`, `proposal_sections`, `created`, `created_by` now populated for all 49 CAP + 13 ASP + 1,136 ASM entries. `cap_ext.platform` corrected with product-specific platform taxonomy (Oracle HCM Cloud / Oracle ERP Cloud / Oracle EBS / Oracle Integration Cloud / Acumatica / BeBanking / Corporate / Cross-Platform). KVE AV-006 severity corrected (ERROR → WARNING — expected filter behaviour). Clean KVE run: ARM-IT045 — BLOCK=1 (AV-011) / ERROR=0 / WARNING=1 (RI-004) / 641 assets in manifest. RI-014 eliminated across all 1,198 entries. Registry Build BUILD-20260628-064745. Platform maturity L4.1.*

*Previous: 2026-06-27 — WP19A COMPLETE — Knowledge Validation Engine Phase A. `kve_engine.py` implemented (Python 3; ~600 lines; Mode 1 + Mode 2; DRY_RUN). All 22 BLOCK rules. First run: ARM-IT045 — 1 BLOCK (AV-011) / 1 ERROR (RI-014 — 1,198 entries) / 0 assets in manifest. ADR-002 enforced. IG-001 CLOSED. Platform maturity L4.0.*

*Previous: 2026-06-27 — WP18G COMPLETE — KVE Readiness Cleanup. SIMP-001 + SIMP-002 resolved. KMS v1.1. lifecycle_status: APPROVED in 49 CAP + 13 ASP. KRPE Build 5: 62/62 APPROVED, 0 errors. KVE Phase A unblocked.*

*Previous: 2026-06-27 — WP18F COMPLETE — Platform Integration Review & Architecture Freeze. Full independent architecture review of 17 governing documents. 12 architectural findings. 5 architectural concerns (none blocking freeze). 13 ADRs frozen, 1 deferred. 9 simplification opportunities (2 P1 pre-KVE: SIMP-001 KMS BU values; SIMP-002 lifecycle_status field population). Implementation Readiness Assessment: **7.80/10 — READY WITH MINOR OBSERVATIONS**. 6 deliverable documents produced. **ARCHITECTURE FREEZE DECLARED 2026-06-27.** Platform maturity L3.8.

*Previous: 2026-06-27 — WP18E-IMP-B COMPLETE — Knowledge Registry Verification & Certification. 19-check programmatic verification. 4 defects found and fixed in `krpe.py`. Registry (Build 4): 1,198 APPROVED | 0 errors | 0 blocking defects. Certified "for Production with Observations." 5 deliverable docs produced. Platform L3.8.

*Previous: 2026-06-27 — WP18E-IMP-A COMPLETE — KRPE Phase A Implementation. Engine: `08_Commercial/Assembly_Engine/krpe.py` (Python 3.12 + PyYAML; ~600 lines; FULL + DRY_RUN modes). First live registry generated: 49 CAP + 13 ASP + 1,136 ASM | 1,136 relationships | 20 indexes | 0 errors | 1.1s. 6 implementation adaptations (secondary tables; Wave 3/4 ID mismatch; digit-category IDs; em-dash annotation; BeBanking no document_id; Cross_BU → Corporate). Platform maturity L3.8.

*Previous: 2026-06-27 — WP18E COMPLETE — Knowledge Registry Population Engine Architecture. 7 documents: KNOWLEDGE_REGISTRY_POPULATION_ENGINE.md (KRPE architecture; 7 components; 3 source formats; 8-phase execution; determinism guarantees), REGISTRY_DISCOVERY_ENGINE.md (10 discovery rules; 20 exclusion rules; traversal algorithm; duplicate detection), REGISTRY_EXTRACTION_ENGINE.md (3 adapters; extractors for all 10 asset types; 10 relationship resolution rules; error taxonomy), REGISTRY_INDEX_ENGINE.md (20 named lookup indexes; 3-pass derivation algorithm), REGISTRY_OUTPUT_SPECIFICATION.md (schemas for all 5 YAML output files; serialisation rules; atomic write protocol), REGISTRY_INCREMENTAL_BUILD_MODEL.md (3 build modes; two-factor change detection; dependency rebuild; deleted-asset archiving), WP18E_POPULATION_ENGINE_ARCHITECTURE.md (completion report; 3-phase implementation roadmap ~28–40h; TD-014–TD-018). KRPE is the compiler front-end — converts governed Markdown repository into machine-readable registry.

*Previous: 2026-06-27 — WP18B-EXT.3A COMPLETE — Universal Knowledge Asset Registry Architecture. 4 docs: REGISTRY_STANDARD.md + REGISTRY_SCHEMA.md + POPULATION_RULES.md + VALIDATION_RULES.md. 76 rules / 22 BLOCK. 1,325 entries designed. Previous: 2026-06-26 — WP18B-EXT.3 COMPLETE — Universal Knowledge Asset Governance Standard. 5 docs. 42 rules. 8-state lifecycle. 7 relationship types. CLV-001–012. Previous: 2026-06-26 — WP18B-EXT.1B COMPLETE — Risk Library Decision Harvest. 40 risks: 20 Cat-A / 20 Cat-B. **NEXT: WP18B-EXT.2 — RISK_GOVERNANCE_WORKSHOP_PACK.md → apply decisions to ENTERPRISE_RISK_REGISTER_V1.md → TD-001 resolved.**

*Previous: 2026-06-26 — WP18C.2 COMPLETE — Section Library Consolidation — 7 architecture docs updated; SI-001/005/006/007/KI-001 resolved; ARM IT045 56 sections; platform L3.5. Previous: 2026-06-26 — WP18C.3 COMPLETE — Tender Intelligence Layer — Stage 0 defined; Stages 4/5/6 deterministic; platform L3.5. Previous: 2026-06-25 — WP18C.1 COMPLETE — Proposal Factory Optimisation — 15 ranked opportunities; governing roadmap.*


---

## Quick Facts

| Field | Value |
|---|---|
| **Approved KB capability assets** | **49** (7 Corporate / 21 Oracle / 10 Acumatica / 11 BeBanking) — registry-verified BU distribution |
| **Approved assumption packs** | **13** (HCM Base 115 + HCM REC 54 + HCM LRN 37 + HCM TLT 31 + HCM COM 30 + OIC 104 + ERP 123 + AMS 84 + OCI 174 + BeBanking Base 117 + Acumatica Base 152 + EBS SLA Overlay 53 + EBS DRM Overlay 62 = **1,136** approved assumptions *(WP16D — HCM-JRN-001 added; PROGRAMME COMPLETE)*) |
| **Draft assumption packs** | **0** — all packs Approved v1.0 (WP16C 2026-06-19) |
| **Active reference letters** | **16** (11 Oracle / 5 Acumatica; REF-ORA-001 through REF-ORA-011; REF-ACU-001 through REF-ACU-005) |
| **Indexed consultants** | **49** (37 Oracle / 7 Cross-BU / 5 Associates; full index at `00_Governance/CONSULTANT_INDEX.csv`) |
| **Commercial Framework** | **5 documents Approved (BU Lead) 2026-06-16** — 6 Commercial Director decisions outstanding (BU-RC-004/008, BU-CR-003, BU-EM-006, BU-GOV-001/003) |
| **Active tender** | **Plennegy** — WP12 Proposal Assembly Engine; WP13 DOCX Draft ~80% complete |
| **Current compliance status** | B-BBEE: expires 2026-07-31 (URGENT). Directors' Resolution: RENEWED 2026-06-15. Public Liability: OBTAINED 2026-06-15. Tax Clearance: valid to 2027-02-23. |

---

## Platform Status at Session Close (WP17Z — 2026-06-22)

| Dimension | Status | Detail |
|---|---|---|
| **Capability Library** | **COMPLETE** | 49 approved capability assets (W1–W4+WP7) |
| **Assumption Library** | **COMPLETE** | 13/13 packs Approved v1.0 — 1,136 assumptions — 0 draft |
| **Governance Programme** | **COMPLETE** | 0 outstanding BU decisions across all 13 packs |
| **Repository Hygiene** | **ASSEMBLY READY** | WP17A cleanup complete; 393 files; no duplicates |
| **Assembly Engine MVP** | **OPERATIONAL** | 6 engine components; ARM IT045 dry-run 594 net assumptions |
| **Regression Test Suite** | **ALL PASS** | 5/5 archetypes; 1,422 net assumptions; 0 blockers |
| **Assembly Engine** | **PRODUCTION READY** | WP17C COMPLETE — cleared for live tender use |
| **Active Tender (Plennegy)** | **BLOCKED** | OAR-C01 (HB AM approval) + OAR-C02 (Costing) + OAR-A01 (BEE) |
| **Outstanding blockers** | **3** | All human actions — no AI blockers; 0 governance decisions outstanding |

### What is DONE — no further setup required

- All 49 capability assets approved and indexed in MASTER_CAPABILITY_INDEX.md
- All 13 assumption packs approved v1.0; 0 decisions outstanding; 0 draft assumptions
- Assembly Engine components built and regression-tested
- Assembly Rules v2.0 current; PACK_LOADER v1.1 current
- Repository structured and cleaned; all engine/report files at correct paths
- Commercial Framework approved (5 documents; 6 CD items outstanding but not blocking)

### What is NEXT

| Priority | Work Package | Prerequisite |
|---|---|---|
| **1** | **WP18B-EXT.2 — Risk Library BU Lead Governance Session** | Use RISK_GOVERNANCE_WORKSHOP_PACK.md. Step 1: send pre-session email (7 items, 20 min BU Lead effort). Step 2: 90-min workshop (13 decisions). Step 3: batch sign-off of 20 Category A risks (RISK_AUTO_APPROVAL_REGISTER.md). Step 4: facilitator applies decisions to ENTERPRISE_RISK_REGISTER_V1.md (`approved_for_reuse: Yes`). Projected: 38–40/40 approved. TD-001 resolved. S-50 upgrades AI-GENERATE → EXTRACT. Prerequisite for WP18D. Total BU effort: ~2h 10min. |
| 2 | **WP18D — Proposal QA Engine** | After Risk Library BU Lead approval (WP18B-EXT.2). See WP18C1 roadmap. |
| 3 | **GAP-TD-005 — OCI Capability Asset (W4-OCI-001)** | Build standalone OCI capability narrative; eliminates S-22 AI-GENERATE gap. 4–8h + BU review. Converts S-22 READY for all OCI-scope tenders. |
| 4 | WP19 — Rendering Engine | WP18D complete |
| 5 | WP18B-METH2 — Oracle Methodology (METH-O01, O03, O06) | Oracle proposals readable; SME for O06 |
| 6 | WP18B-METH3 — Acumatica + BeBanking Methodology | SME workshops required |
| 7 | Live Plennegy assembly | OAR-C01 + OAR-C02 + OAR-A01 human actions first |
| 8 | ARM IT045 Readiness Dashboard update (TD-006) | Update ARM_IT045_PROPOSAL_READINESS.md v1.0→v1.1 to reflect corrected section count 56 and Scope/Governance recategorisation |

---

## System Maturity

| Work Package | Status | Output |
|---|---|---|
| W1 — Wave 1 extraction | **COMPLETE 2026-06-10** | 25 assets (Cross-BU 9; BeBanking 10; Acumatica 6) |
| W2 — Wave 2 Oracle platform | **COMPLETE 2026-06-11/12** | 5 Oracle platform/methodology assets |
| W3 — Wave 3 Oracle HCM | **COMPLETE 2026-06-13** | 9 Oracle HCM suite assets |
| W4 — Wave 4 Oracle ERP/OIC/HCM | **COMPLETE 2026-06-14** | 6 promoted (Journeys, AI Skills, OIC Accelerators, Fusion Finance, Fusion Procurement, PPM); 1 retired (T&L) |
| WP7 — Reference registration + W5 | **COMPLETE 2026-06-14** | 9 reference letters registered; W5-ACU-001 + W5-METH-001 added → 49 total |
| WP8 — Compliance Register | **COMPLETE 2026-06-15** | COMPLIANCE_REGISTER.csv with 17 items |
| WP9 — Reference registration expanded | **COMPLETE 2026-06-15** | REF-ORA-007–011 + REF-ACU-001–005 added; REF-ARC-001–011 archived |
| WP10 — Consultant Index | **COMPLETE 2026-06-15** | CONSULTANT_INDEX.csv; 49 consultants across Oracle/Cross-BU/Associate pools |
| WP11 — Assumption Library | **COMPLETE** | 13 documents total; **13 APPROVED** (HCM Base, HCM REC, HCM LRN, HCM TLT, HCM COM, OIC, ERP, AMS, OCI, BeBanking Base, Acumatica Base, EBS SLA Overlay, EBS DRM Overlay); 0 DRAFT; **GOVERNANCE PROGRAMME COMPLETE** |
| WP11I — Acumatica Base Assumption Pack | **COMPLETE 2026-06-16** | 4 deliverables: ACU_BASE_ASSUMPTIONS_V1.md (152 assumptions), ACU_ASSUMPTION_REGISTER.csv, ACU_GAP_REPORT.md, ACU_SCOPE_BOUNDARY_GUIDE.md |
| WP11I-A — Acumatica Pre-Approval Validation | **COMPLETE 2026-06-16** | 17 new assumptions; Section 139 ACU-SEC; 4 new BU decisions (BU-ACU-011/012/014/015); WP11I_A_REMEDIATION_REPORT.md |
| WP15A.1 — Acumatica Decision Harvest Pack | **COMPLETE 2026-06-18** | 3 deliverables: WP15A1_ACUMATICA_EMAIL_APPROVAL_PACK.md (10 decisions), WP15A1_ACUMATICA_COMMERCIAL_REVIEW_PACK.md (1 decision), WP15A1_ACUMATICA_REDUCED_WORKSHOP_AGENDA.md (2 decisions) |
| WP15C — Acumatica Final Decision Application | **COMPLETE 2026-06-18** | All 14 BU decisions resolved + applied; Acumatica Base Pack promoted Draft → **Approved v1.0**; 6 governance artefacts updated; WP15C_ACUMATICA_PROMOTION_REPORT.md created |
| WP15D — EBS AMS Remediation | **COMPLETE 2026-06-18** | 2 EBS overlay packs created (Draft): EBS_AMS_SLA_OVERLAY_V1.md (53 assumptions) + EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md (62 assumptions); 114 new assumptions; 9 BU decisions registered; EBS AMS readiness 66%→96%; WP15D report created |
| WP15E — EBS Decision Harvest | **COMPLETE 2026-06-19** | 9 decisions classified (6A email/1B CD/2C workshop); decision harvest pack created; WP15E report created |
| WP15F — EBS AMS Overlay Promotion | **COMPLETE 2026-06-19** | All 9 EBS overlay decisions applied; both EBS overlay packs promoted Draft → **Approved v1.0**; 9 HCM MEDIUM decisions resolved via email governance; 7 governance artefacts updated; WP15F report created |
| WP16A — Library Reconciliation Baseline | **COMPLETE 2026-06-19** | All pack counts corrected to body/register-authoritative; approved 996→**983** (OIC +3, ERP −5, AMS −12); draft 173→**152**; total 1,174→**1,135**; 7 files corrected; ASSUMPTION_LIBRARY_ROADMAP.md overhauled v1.6→v1.7; GOVERNANCE_DASHBOARD HCM section fixed; WP16A report created; **9 packs; 983 approved assumptions** |
| WP16B — Oracle HCM Decision Pack Preparation | **COMPLETE 2026-06-19** | 3 deliverables: WP16B_HCM_HIGH_PRIORITY_DECISION_PACK.md (BU-REC-005/006); WP16B_HCM_LOW_PRIORITY_APPROVAL_PACK.md (10 LOW decisions); WP16B_HCM_PROMOTION_READINESS.md. All 12 decisions classified Category A (email only). |
| WP16C — Oracle HCM Final Promotion and Governance Closure | **COMPLETE 2026-06-19** | All 12 decisions applied; all 4 HCM module packs promoted Draft → **Approved v1.0**; all governance artefacts updated; GOVERNANCE PROGRAMME COMPLETE. Final: 13/13 packs / 1,135/1,135 assumptions / 0 outstanding decisions / 54/54 resolved. WP16C_GOVERNANCE_PROGRAMME_CLOSURE_REPORT.md created. |
| WP16D — Oracle Journeys Post-Programme Enhancement | **COMPLETE 2026-06-19** | HCM-JRN-001 added (BU-HCM-022 applied); HCM Base v1.0→v1.1 (114→115 assumptions); TENDER_ASSUMPTION_ASSEMBLY_RULES v1.8→v1.9 (Rule JRN-1 + Section 3.2a; WP16C statuses propagated; approved 983→1,136; draft 152→0); 0 conflicts across all 13 packs; WP16D_JOURNEYS_ENHANCEMENT_REPORT.md created. |
| WP17A-0 — Tender Factory Directory Structure Audit | **COMPLETE 2026-06-19** | Full audit of 373-file repository across 16 top-level folders. Verdict: **Apply light targeted cleanup before WP17 (Assembly Engine)**. Key findings: 2 duplicate KB files (W1S2-003, W1S3-010); W4-ERP/OIC loose at Oracle/ root; pipeline staging not purged (~68 stale files); 00_Governance overstuffed (104 files — 7 Assembly Engine components should move to 08_Commercial/Assembly_Engine/); 21 WP reports to move to 08_Commercial/Reports/; 02_Corporate shadow copy of Cross_BU assets. Priority 1 fixes must be done BEFORE WP17B. Deliverable: `00_Governance/WP17A0_DIRECTORY_STRUCTURE_AUDIT.md`. No files modified. |
| WP17A — Repository Hygiene and Assembly Readiness Cleanup | **COMPLETE 2026-06-19** | All cleanup tasks executed. 2 KB duplicates removed (W1S2-003 from Acumatica/ERP/, W1S3-010 from BeBanking/Banking/); W4-ERP-001/002/003 → Oracle_ERP/, W4-INT-001 → Oracle_OIC/, W5-METH-001 → Approved/Cross_BU/; 7 Assembly Engine files → 08_Commercial/Assembly_Engine/; 25 WP reports → 08_Commercial/Reports/; 66 historical files → 00_Governance/Archive/; 47 pipeline DRAFTs → _Archived_Superseded/; MASTER_CAPABILITY_INDEX v1.3 paths corrected. **Repository ASSEMBLY READY.** Deliverable: `08_Commercial/Reports/WP17A_REPOSITORY_CLEANUP_REPORT.md`. |
| WP17B — Assembly Engine Core (MVP) | **COMPLETE 2026-06-19** | 6 engine components built: BOM_RESOLVER, PACK_LOADER, RULE_PROCESSOR, ASSUMPTION_EXTRACTOR, ASSEMBLY_AUDITOR, ENGINE_ORCHESTRATOR (all in `08_Commercial/Assembly_Engine/`). ARM IT045 dry-run: EBS AMS Full Stack pattern; 6 packs; 600 raw → 594 net assumptions; 6 WP14C critical gaps RESOLVED. Assembly Engine OPERATIONAL. Deliverables: ARM_IT045_ASSEMBLED_ASSUMPTION_SCHEDULE.md, ARM_IT045_ASSEMBLY_AUDIT_REPORT.md, `08_Commercial/Reports/WP17B_ASSEMBLY_ENGINE_MVP.md`. |
| WP17C — Assembly Engine Regression Test Suite | **COMPLETE 2026-06-22** | 5 archetype regression tests: T1 ARM IT045 (EBS AMS Full Stack) / T2 HCM Full Suite / T3 OIC Standalone / T4 BeBanking+OIC+AMS / T5 Acumatica. Results: ALL PASS; 1,428 raw → 6 suppressed → 1,422 net; 0 blockers; 3 advisories (non-blocking). Pre-flight fixes: PACK_LOADER v1.0→v1.1; Assembly Rules v1.9→v2.0. Assembly Engine PRODUCTION READY. Deliverable: `08_Commercial/Reports/WP17C_REGRESSION_TEST_REPORT.md`. |
| WP17D-0 — Assumption Schedule Design Standard | **COMPLETE 2026-06-22** | 4 deliverables in `08_Commercial/Assembly_Engine/` and `08_Commercial/Reports/`: ASSUMPTION_SCHEDULE_STANDARD.md (format, numbering, traceability, deduplication, output format); ASSUMPTION_PUBLICATION_RULES.md (7 assumption types; all net assumptions publish; no internal-only individual assumptions); ASSUMPTION_GROUPING_RULES.md (8 client-facing sections A–H; 23-rule deterministic section mapping algorithm; per-pattern section counts); WP17D0_DESIGN_RECOMMENDATION_REPORT.md (current output assessment; 8 design decisions; WP17D-1 implementation spec). Design standard formally approved. |
| WP17D-0A — Assumption Schedule Consumption Model | **COMPLETE 2026-06-22** | 3 deliverables: ASSUMPTION_SCHEDULE_PRESENTATION_STANDARD.md (Option A/B/C evaluated; Option B approved — body section + appendix; scale threshold: ≤200 assumptions = Option A discretionary; >200 = Option B mandatory); EXECUTIVE_ASSUMPTION_SUMMARY_RULES.md (5 deterministic selection rules by ID section code; Priority 1: EXC/EXT mandatory; Priority 2: CUS/CON/DEP mandatory; Priority 3: SLA/PRI selected; Priority 4: GEN selected; Priority 5: CR/ENH selected); WP17D0A_PRESENTATION_RECOMMENDATION.md (formal recommendation; scoring matrix; 5 BU Lead action items; dual-output WP17D-1 impact). **ARM IT045: body ~130 assumptions (~13 pages) + appendix 594 assumptions (~58 pages).** |
| WP17D-1 — Inline Text Assembly (ARM IT045) | **COMPLETE 2026-06-25** | 3 deliverables: ARM_IT045_ASSUMPTION_SCHEDULE_V1.md (594 complete assumptions in 8 sections A–H; proposal-ready markdown); ARM_IT045_KEY_ASSUMPTIONS_V1.md (175 body assumptions in 4 sub-sections; dual-output Option B); WP17D1_IMPLEMENTATION_REPORT.md (10/10 validation PASS; suppression log; section counts). Assembly Engine v1.1 OPERATIONAL. |
| WP18A — Proposal Factory Architecture | **COMPLETE 2026-06-25** | 8 deliverables (7 in `08_Commercial/Assembly_Engine/`; 1 in `08_Commercial/Reports/`): PROPOSAL_FACTORY_ARCHITECTURE.md (10-stage pipeline); PROPOSAL_SECTION_LIBRARY.md (82 sections); CONTENT_SOURCE_MATRIX.md (section→source mapping); PROPOSAL_ASSEMBLY_SEQUENCE.md (19-step sequence); AUTOMATION_MATURITY_MODEL.md (L1–L5 per section); PROPOSAL_GAP_ANALYSIS_FRAMEWORK.md (WP18C spec; 14 gap categories); PROPOSAL_QA_FRAMEWORK.md (WP18D spec; QA scorecard); WP18A_ARCHITECTURE_RECOMMENDATION.md (platform maturity; arch decisions; roadmap). |
| WP18B — Methodology & Risk Library Foundation | **COMPLETE 2026-06-25** | 9 deliverables: WP18B1_METHODOLOGY_AUDIT.md; WP18B2_RISK_LIBRARY_AUDIT.md; METHODOLOGY_LIBRARY_STANDARD.md (22-doc roadmap; METH-X/O/A/B; approval workflow); RISK_LIBRARY_STANDARD.md (15 RC-categories; 3×3 matrix; RAID standard); 4 WP18A architecture docs updated v1.0→v1.1; WP18B_IMPLEMENTATION_PLAN.md. Platform maturity L2.5→L2.6 (after WP18B-EXT). |
| WP18C — Proposal Factory Assembly Engine v1.0 | **COMPLETE 2026-06-25** | 6 deliverables in `08_Commercial/Reports/`. Reference tender: ARM IT045 (EBS AMS Full Stack). 57 sections; 77.2% deterministic assembly; QA 72/100; 14 gaps (5 SEV-1 / 5 SEV-2 / 4 SEV-3); platform maturity L2.5→L3.0. Path note: Proposal_Factory/ folder not created (OneDrive mkdir restriction) — all files in Reports/. |
| WP18C.1 — Proposal Factory Optimisation | **COMPLETE 2026-06-25** | 3 deliverables: WP18C1_FACTORY_OPTIMISATION_REVIEW.md (12 structural issues; 4 reviewer perspectives; engine analysis); WP18C1_AUTOMATION_OPPORTUNITY_REGISTER.md (15 ranked opportunities; P0 = 7 actions ~10h → 79% automation); WP18C1_REVISED_IMPLEMENTATION_ROADMAP.md (governing roadmap; WP18C.2/18C.3/18C.4 new WPs; methodology authoring deprioritised; supersedes WP18B plan). |
| WP18C.3 — Tender Intelligence Layer | **COMPLETE 2026-06-26** | 6 deliverables in `08_Commercial/Assembly_Engine/` + 1 in `08_Commercial/Reports/`. Stage 0 defined: TENDER_PROFILE_STANDARD.md (YAML schema; 8 blocks; 30+ fields with source/extraction/validation/default); TENDER_INTELLIGENCE_RULES.md (10-step TIL sequence; downstream trigger matrix; 15 governance rules); PROPOSAL_PATTERN_ENGINE.md (13 patterns; AO-002 section scoping; SI-001 fix embedded); CAPABILITY_SELECTION_ENGINE.md (all 16 BOMs; deselection rules); METHODOLOGY_SELECTION_ENGINE.md (pattern→asset lookup; phase structures); REFERENCE_SELECTION_ENGINE.md (7-dimension 10pt matrix; 12 exclusion rules; AM workflow). Platform maturity L3.0→L3.5. AO-001/002/003/004/009 resolved. |
| WP18C.2 — Section Library Consolidation | **COMPLETE 2026-06-26** | 7 deliverables: PROPOSAL_SECTION_LIBRARY.md v1.2 (SI-001 S-38 EXCL-AMS; SI-007 S-71/S-72 boundaries; scoping cross-reference); CONTENT_SOURCE_MATRIX.md v1.2 (S-38 AMS exclusion; S-73 AMS-authoritative; SI-007 boundaries); PROPOSAL_ASSEMBLY_SEQUENCE.md v1.1 (SI-001/SI-005/SI-006/SI-007 notes; Pattern 13 complete order table); PROPOSAL_FACTORY_ARCHITECTURE.md v1.2 (Stage 0 TIL added); TENDER_BOM_LIBRARY.md v1.1 (KI-001: 6 pack statuses corrected; EBS overlays added to BOM 16); ARM_IT045_PROPOSAL_ASSEMBLY_REPORT.md v1.1 (RF-001–004 corrected; section count 57→56); ARM_IT045_PROPOSAL_STRUCTURE.md v1.1 (S-38 excluded; section count corrected). Platform maturity L3.5 maintained. Deliverable: WP18C2_SECTION_LIBRARY_CONSOLIDATION.md. |
| WP18B-EXT.1 — Risk Library Foundation Phase 1 | **COMPLETE 2026-06-26** | 3 deliverables: WP18B_EXT1_RISK_EXTRACTION_REPORT.md (08_Commercial/Reports/); ENTERPRISE_RISK_REGISTER_DRAFT.md (08_Commercial/Risk_Library/ — NEW folder created); RISK_DUPLICATION_ANALYSIS.md (08_Commercial/Reports/). 49 assets audited; 10 with formal risk registers; 51 source risks; 8 duplication groups; 40 canonical risks across 8 categories (RC-PROJ/DATA/INT/TECH/CLIENT/COMM/OPS/COMP). 7 categories have no source (RC-RES/INFRA/CM/MIG/CUT/3P/SEC — WP18B-EXT.2 BU interview needed). All entries DRAFT pending BU Lead approval. TD-001 partially resolved. |
| WP18B-EXT.1A — Enterprise Risk Library Normalisation | **COMPLETE 2026-06-26** | 5 deliverables: RISK_METADATA_STANDARD.md; ENTERPRISE_RISK_REGISTER_V1.md (supersedes DRAFT v0.1; 40 risks × 32 fields; V1.0 schema); RISK_ASSUMPTION_CROSS_REFERENCE.md (40 risks × governed assumption IDs; 12 packs); RISK_PROPOSAL_MAPPING.md (40 risks × sections × patterns; pattern-centric view); WP18B_EXT1A_NORMALISATION_REPORT.md (readiness score 76/100; 12 rating recalculations; gap analysis; BU effort estimate 3–4h). Selection hooks (mandatory_if/optional_if/excluded_if) defined for all 40 risks. Risk Selection Engine NOT built (WP18D). |
| WP11J — BeBanking Base Assumption Pack | **COMPLETE 2026-06-16** | 4 deliverables in `08_Commercial/Assumptions/BeBanking/`: BEBANKING_BASE_ASSUMPTIONS_V1.md (122 assumptions at creation), BEBANKING_ASSUMPTION_REGISTER.csv, BEBANKING_GAP_REPORT.md, BEBANKING_SCOPE_BOUNDARY_GUIDE.md |
| WP14B — Assumption Library Master Review Workbook | **COMPLETE 2026-06-17** | ASSUMPTION_LIBRARY_MASTER_REVIEW.xlsx (1,025 rows / 45 decisions / 12 exceptions); ASSUMPTION_LIBRARY_MASTER_REVIEW_REPORT.md — awaiting Acumatica + HCM human review |
| WP14C — Tender Factory Validation Run | **COMPLETE 2026-06-17** | ARM IT045 (WON 2025-08-28) used as validation case. Verdict: YES WITH QUALIFICATIONS. 3 CRITICAL gaps. Remediation roadmap WP15A–WP15I. Report: 08_Commercial/WP14C_TENDER_FACTORY_VALIDATION_REPORT.md |
| WP14D — BeBanking Assumption Pack Remediation | **COMPLETE 2026-06-18** | 5 assumptions deleted, 15 modified; 117 assumptions remain; 9 of 10 BU decisions resolved; Report: 08_Commercial/WP14D_BEBANKING_REMEDIATION_REPORT.md |
| WP14E — BU-BB-002 Decision Paper | **COMPLETE 2026-06-18** | Decision paper for new bank onboarding fee model. Recommended Option A (fixed-price CR). Report: 08_Commercial/WP14E_BU_BB_002_DECISION_PAPER.md |
| WP14F — BeBanking Pack Promotion | **COMPLETE 2026-06-18** | BeBanking Base Pack promoted Draft → **Approved v1.0**. All 10 BU decisions closed. 117 approved assumptions. Governance dashboard updated. Report: 08_Commercial/WP14F_BEBANKING_PROMOTION_REPORT.md |
| WP11F — Commercial Framework | **DRAFT 2026-06-15** | 5 documents in `08_Commercial/`; 25 BU review items outstanding |
| WP11F-A — Commercial Framework Approval | **COMPLETE 2026-06-16** | All 5 documents promoted to Approved v1.0. 34/40 decisions approved. 6 CD items outstanding (OAR-D05). 5 change logs created. |
| WP11G — Governance reconciliation | **COMPLETE 2026-06-16** | HANDOVER, AI_CONTEXT, OUTSTANDING_ACTION_REGISTER, GOVERNANCE_DELTA_REPORT rewritten/created |
| WP11H — OCI Infrastructure Assumption Pack | **COMPLETE 2026-06-16** | 4 deliverables: OCI_ASSUMPTIONS_V1.md (174 assumptions — count corrected WP14A), OCI_ASSUMPTION_REGISTER.csv, OCI_GAP_REPORT.md, OCI_SCOPE_BOUNDARY_GUIDE.md |
| WP11H-A — OCI Pack BU Lead Approval | **COMPLETE 2026-06-16** | All decisions resolved. 14 approved + 1 withdrawn (BU-OCI-007). Pack promoted to Approved v1.0. |
| WP12 — Proposal Assembly Engine | **COMPLETE 2026-06-16** | 8 deliverables: TENDER_BOM_LIBRARY, PROPOSAL_STRUCTURE_LIBRARY, DELIVERY_PATTERN_LIBRARY, PROJECT_PLAN_TEMPLATES, ASSEMBLY_RULES_ENGINE, ESTIMATION_INPUT_MODEL, ASSEMBLY_READINESS_MATRIX, PLENNEGY_ASSEMBLY_TEST |
| Plennegy DOCX Draft | **~80% COMPLETE** | PLENNEGY_DRAFT_RESPONSE.docx — pending Costing section + TOC |
| WP13 — Governance Approval Campaign | **COMPLETE 2026-06-16** | 6 deliverables in `08_Commercial/Assumptions/Governance/`: MASTER_DECISION_REGISTER (45 decisions), APPROVAL_ROADMAP (3-wave plan), WORKSHOP_PLAN, DECISION_RECORD_TEMPLATE, DASHBOARD, RISK_REGISTER. Target: all 6 Draft packs Approved v1.0 by 2026-07-28. |

---

## Approved Asset Summary (49 total)

### Cross-BU — 6 files (`07_Approved_Content/Approved/Cross_BU/`)
W1S1-001 Company Overview | W1S1-002 Company History | W1S1-006 Awards and Recognition | W1S1-007 Delivery Model | W1S1-008 Geographic Presence | W1S1-009 Key Differentiators

### Oracle — 21 files (`07_Approved_Content/Approved/Oracle/` + KB copies in `06_Capabilities/Oracle/`)
W1S1-003 Oracle Partnership | W2S1-001 Fusion Capability | W2S1-002 EBS Capability | W2S1-003 DBA Executive Summary | W2S1-004 Managed Services | W2S1-005 Implementation Methodology
W3S1-001 HCM Core | W3S1-002 Talent Management | W3S1-003 Recruiting Cloud | W3S1-004 Learning Cloud | W3S1-005 Workforce Compensation | W3S1-006 HCM Analytics | W3S1-007 Workforce Management | W3S1-008 Help Desk & HR Service Delivery | W3S1-009 Payroll Interface & Integration
W4-HCM-002 Oracle Journeys | W4-AI-002 Oracle AI Skills | W4-INT-001 OIC Accelerators | W4-ERP-001 Fusion Financials | W4-ERP-002 Fusion Procurement | W4-ERP-003 PPM

### Acumatica — 9 files (`07_Approved_Content/Approved/Acumatica/`)
W1S1-004 Acumatica Partnership | W1S2-001 Financials | W1S2-002 Distribution | W1S2-003 Inventory | W1S2-004 Manufacturing | W1S2-005 CRM | W1S2-006 Field Services | W1S2-007 PaySpace Payroll Integration | W1S2-009 Project Accounting | W5-ACU-001 Support & Managed Services

### BeBanking — 11 files (`07_Approved_Content/Approved/BeBanking/`)
W1S1-005 BeBanking Overview | W1S3-001 through W1S3-010 (all 10 BeBanking modules)

### Cross-Platform — 2 files (`07_Approved_Content/Approved/`)
W5-METH-001 ERP Implementation Methodology (platform-agnostic)

**Full detail:** `06_Capabilities/MASTER_CAPABILITY_INDEX.md` (v1.2, 49 assets, governance restrictions per asset)

---

## Assumption Library

| Pack | File | Status | Assumptions | BU Review Items |
|---|---|---|---|---|
| HCM Base | `08_Commercial/Assumptions/HCM/HCM_BASE_ASSUMPTIONS_V1.md` | **Approved v1.1 — WP16D 2026-06-19** | **115** | 0 (BU-HCM-022 applied) |
| HCM Recruiting | `08_Commercial/Assumptions/HCM/HCM_RECRUITING_ASSUMPTIONS_V1.md` | **Approved v1.0 (WP16C 2026-06-19)** | **54** | **0** — all 7 resolved |
| HCM Learning | `08_Commercial/Assumptions/HCM/HCM_LEARNING_ASSUMPTIONS_V1.md` | **Approved v1.0 (WP16C 2026-06-19)** | **37** | **0** — all 5 resolved |
| HCM Talent | `08_Commercial/Assumptions/HCM/HCM_TALENT_ASSUMPTIONS_V1.md` | **Approved v1.0 (WP16C 2026-06-19)** | **31** | **0** — all 4 resolved |
| HCM Compensation | `08_Commercial/Assumptions/HCM/HCM_COMPENSATION_ASSUMPTIONS_V1.md` | **Approved v1.0 (WP16C 2026-06-19)** | **30** | **0** — all 5 resolved |
| OIC Integration | `08_Commercial/Assumptions/OIC/OIC_ASSUMPTIONS_V1.md` | **Approved 2026-06-15** | **104** | 0 |
| Oracle ERP | `08_Commercial/Assumptions/ERP/ERP_ASSUMPTIONS_V1.md` | **Approved 2026-06-15** | **123** | 0 |
| OCI Infrastructure | `08_Commercial/Assumptions/OCI/OCI_ASSUMPTIONS_V1.md` | **Approved 2026-06-16** | 174 | 0 |
| Acumatica Base | `08_Commercial/Assumptions/Acumatica/ACU_BASE_ASSUMPTIONS_V1.md` | **Approved v1.0 (WP15C 2026-06-18)** | **152** | **0** — all resolved |
| BeBanking Base | `08_Commercial/Assumptions/BeBanking/BEBANKING_BASE_ASSUMPTIONS_V1.md` | **Approved v1.0 (WP14F 2026-06-18)** | **117** | **0** — all resolved |
| AMS | `08_Commercial/Assumptions/AMS/AMS_ASSUMPTIONS_V1.md` | **Approved 2026-06-15** | **84** | 0 |
| EBS SLA Overlay | `08_Commercial/Assumptions/AMS/EBS_AMS_SLA_OVERLAY_V1.md` | **Approved v1.0 (WP15F 2026-06-19)** | **53** | **0** — all resolved |
| EBS DRM Overlay | `08_Commercial/Assumptions/AMS/EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md` | **Approved v1.0 (WP15F 2026-06-19)** | **62** | **0** — all resolved |

Assembly rules: `08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md` | Governance: `08_Commercial/ASSUMPTION_GOVERNANCE.md`

---

## Active Tender — Plennegy

**Status:** WP12 active — assembly in progress. WP13 DOCX draft ~80% complete.

**Plennegy-specific governance:**
- Parallel payroll run is **INCLUDED** by default (HCM-CUT-005 reversal, BU-WP11-001 applied)
- Section 13.1 of the DOCX reflects this — do not revert
- Hollywood Bets can be named as reference ONLY with AM approval (OAR-C01 — pending)
- Costing section must be added before submission (OAR-C02 — pending)

**Pending Plennegy actions before submission:**
1. AM approval — Hollywood Bets naming (OAR-C01) — **CRITICAL**
2. Add Costing section to PLENNEGY_DRAFT_RESPONSE.docx (OAR-C02) — **CRITICAL**
3. Oracle awards verification — BU Lead to confirm (OAR-C05)
4. Plennegy payroll/entity confirmation (OAR-C04)
5. Generate Word TOC (OAR-C03)
6. B-BBEE certificate valid at submission date (OAR-A01 — expires 2026-07-31)

---

## Governance Restrictions — Permanent Rules

### Client Naming Restrictions

| Client | Rule | Status |
|---|---|---|
| **Dark Fibre Africa (DFA)** | **Rule 21.4 PERMANENT** — NEVER named in any KB content or external submission | Archived — internal evidence only (REF-ARC-002) |
| **Redpath Mining** | **Rule 21.5** — Not referenceable until go-live confirmed + BU Lead approval | Active pipeline — passive rule |
| **CCBA** | **PROHIBITED** — Must never be named in any KB content or tender submission | Internal evidence only (HIST-014) |
| **SAA** | **Rule 21.1 Aviation** — Never named as client, reference, or implementation | Source material only (HIST-006 — aviation prohibited) |
| **Hollywood Bets** | **AM approval required at each tender submission** | Referenceable but requires AM sign-off every time |
| **KPMG** | **AM-W4E3-001 ACTIVE** — Not named until signed letter registered | Signed letter not yet obtained |

### Section Exclusions (MUST NOT appear in external submissions)

| Asset | Exclusion | Rule |
|---|---|---|
| W3S1-008 Help Desk | Section 14.2 — internal governance table | PT-W8-007 |
| W3S1-009 Payroll Interface | Section 13.2 — internal governance table | PT-W9-008 |

### Product Boundary Rules

| Rule | Content |
|---|---|
| BeBanking SAP | Use "BeBanking integrates with SAP environments" only — no module-level claims until BQ-WEB-04 confirmed |
| BeBanking SWIFT | Bank-intermediated model only — do not claim direct SWIFT membership |
| BeBanking Payroll H2H | Oracle EBS and Oracle Fusion payroll sources only — never imply Acumatica payroll integration |
| Oracle HR Help Desk | Product is B87388 — never describe as Oracle Service Cloud / Fusion Service / B2C Service / ITSM |
| Oracle EBS Payroll framing | "Oracle Fusion HCM ↔ OIC ↔ PaySpace" is authoritative — never use "EBS Payroll" heading for the integration |
| W3S1-005 Compensation | Mining sector ONLY (G-001) — Retail attribution prohibited |
| T&L statement | W4-HCM-004 RETIRED — governed through W3S1-007 only; no standalone T&L statement until production evidence |
| Oracle partner tier | Level 1 Partner only — Gold Partner EXPIRED August 2021 — never cite |
| Headcount | "more than 50 Senior Consultants" — never use 100+ or 110+ |
| Reference letters | Only signed letters in `04_References/` may be cited — no unsigned templates; AM approval at each submission |
| HIST-018 billing | R825,170 from HIST-018 ANN1-V4.1 MUST NEVER appear in any external submission |
| Approved KB supersedes old content | Content from KB-approved Wave 1–4 assets supersedes old company profile content — use KB sources |

---

## Do Not Do

1. **Do not cite DFA, CCBA, SAA as client or reference** — ever, in any context
2. **Do not cite Redpath Mining as a reference** until Rule 21.5 is waived by BU Lead
3. **Do not name Hollywood Bets without AM approval** for that specific tender
4. **Do not name KPMG** in PPM/ERP content until AM-W4E3-001 cleared (signed letter registered)
5. **Do not include Section 14.2 (W3S1-008) or Section 13.2 (W3S1-009)** in any external submission
6. **Do not use old company profile** — KB-approved content supersedes 2024 company profile for all covered topics
7. **Do not use Candidate_Content/ or Review_Required/ content** in any tender — Approved/ only
8. **Do not generate CV text** from KB consultant records — use for skill matching only; obtain CVs from APPTime
9. **Do not cite "Oracle Gold Partner"** — expired August 2021
10. **Do not cite BEE status after 2026-07-31** unless renewal cert confirmed on file
11. **Do not assemble a fixed-price proposal** without the commercial file (bottom-up estimate, multiplier justification, rate card calculation, discount approval if any, assumption pack selected)
12. **Do not submit a proposal** with expired compliance documents — Directors' Resolution or B-BBEE

---

## Outstanding Blockers (Summary)

**Full register:** `00_Governance/OUTSTANDING_ACTION_REGISTER.md`

| Priority | Item | Owner | Deadline |
|---|---|---|---|
| CRITICAL | B-BBEE Certificate renewal (OAR-A01) | Finance Director | 2026-07-31 |
| CRITICAL | AM approval — Hollywood Bets in Plennegy (OAR-C01) | Oracle BU Lead / AM | Before Plennegy submission |
| HIGH | Costing section in Plennegy draft (OAR-C02) | Bid Manager | Before Plennegy submission |
| — | HCM module pack BU decisions — **ALL RESOLVED WP16C 2026-06-19** (OAR-D01–D04 CLOSED) | — | 13/13 packs Approved v1.0; 54/54 decisions resolved |
| MEDIUM | Commercial Framework CD decisions — 6 items (OAR-D05) | Commercial Director | Open — BU Lead component COMPLETE |
| HIGH | KPMG reference letter (OAR-B02 / AM-W4E3-001) | Oracle BU Lead / AM | Open |
| HIGH | Harmony Gold 2024 letter — obtain text copy (OAR-G07 / OAR-B03) | Oracle BU Lead | Open |
| MEDIUM | POPIA Policy (OAR-E01) | Company Secretary | Open |
| MEDIUM | PAIA Manual (OAR-E02) | Company Secretary | Open |
| MEDIUM | Acumatica Gold Partner Certificate (OAR-E03) | Acumatica BU Lead | Open |

---

## Retrieval-First Rule

**A new AI session MUST:**
1. Read this HANDOVER.md and AI_CONTEXT.md before any work
2. Do NOT load the full KB corpus into context — retrieve only the specific file(s) needed for the task
3. For tender assembly: retrieve the relevant approved capability statements + assumption pack(s) by BU and module — do not load all 49 assets
4. When referencing client facts: retrieve from `00_Governance/ORACLE_FACT_BASELINE.md` or `00_Governance/REFERENCE_MASTER.md` — do not rely on memory
5. When checking compliance status: read `01_Compliance/COMPLIANCE_REGISTER.csv` — do not assume
6. When checking governance restrictions: read `06_Capabilities/MASTER_CAPABILITY_INDEX.md` Section headers for the specific asset

---

## Pending Human Actions

| Action | Owner | Notes |
|---|---|---|
| Engage B-BBEE rating agency | Finance Director | Deadline 2026-07-31 — do not defer |
| AM approval: Hollywood Bets for Plennegy | Oracle BU Lead / AM | Blocking Plennegy final submission |
| BU Lead decisions: HCM module items | Oracle BU Lead | **COMPLETE WP16C 2026-06-19** — All 12 decisions confirmed; all 4 packs Approved v1.0; OAR-D01–D04 CLOSED. |
| Commercial Framework — CD decisions: 6 items | Commercial Director | BU-RC-004/008, BU-CR-003, BU-EM-006, BU-GOV-001/003 — BU Lead component COMPLETE (WP11F-A 2026-06-16) |
| KPMG account manager contact | Oracle BU Lead | KPMG letter for AM-W4E3-001 |
| Harmony Gold reference letter — text copy | Oracle BU Lead | Contact ARM/Harmony mining sector contact |
| Acumatica BU Lead team roster | Acumatica BU Lead | By July 2026 |
| BeBanking BU Lead team roster | BeBanking BU Lead | By July 2026 |
| HIST-006/007/014/015/016/017 registration | Bid Manager | DOCUMENT_REGISTER.csv |
| Delete superseded DRAFT files (Finder) | Hein | W2S1-001, -002, -004, -005 in Candidate_Content/ |
| Confirm Public Liability Insurance expiry | Finance Director | Update COMP-008 with exact expiry date |

---

## Architecture Decisions (Summary)

| Decision | Summary |
|---|---|
| **Extraction-first** (D-STRAT-001) | Extract from 18,400-file historical corpus. Author from scratch only for confirmed gaps. CONTENT_GAP_ANALYSIS.md unreliable — do not use. |
| **APPTime as CV source** (ADR-001) | APPTime = authoritative for all consultant CVs. KB stores Consultant Index Records only (skill tags, certs, availability). AI must never generate CV text from KB records. |
| **Assumption Library** (WP11) | Commercial protection mechanism. Must be included in all fixed-price proposals. Assembly rules in `08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md`. 5 packs approved; 4 HCM module packs pending. |
| **Commercial Framework** (WP11F-A) | 5 framework documents in `08_Commercial/` — Approved by BU Lead 2026-06-16. 6 Commercial Director decisions outstanding (monetary thresholds, margin floors, AMS rate policy). Do not include actual rates or monetary thresholds in external submissions. |
| **OCI Infrastructure Pack** (WP11H-A) | 174 assumptions across 19 sections (count corrected WP14A — frontmatter had 164, body/register correct at 174). Approved v1.0 2026-06-16. 14 BU decisions applied; BU-OCI-007 permanently withdrawn (concept does not exist). OCI Pack now included in all OCI-related proposals without qualification. |
| **Acumatica Base Pack** (WP11I + WP11I-A + WP15C) | 152 assumptions across Sections 120–139. **Approved v1.0 WP15C 2026-06-18.** All 14 BU decisions resolved. approved_for_reuse = Yes. **May be used in all Acumatica client-facing proposals without restriction.** See WP15C_ACUMATICA_PROMOTION_REPORT.md. |
| **BeBanking Base Pack** (WP11J → WP14F) | **117 assumptions** across Sections 140–153 (14 sections). **Approved v1.0 2026-06-18 (WP14F).** All 10 BU decisions resolved. 5 assumptions deleted and 15 modified via WP14D BU Lead Master Review. **May be used in all BeBanking client-facing proposals without restriction.** BU Lead action outstanding: publish BeBanking Bank Addition SOW Schedule for presales use. |
| **EBS SLA Overlay** (WP15D → WP15F) | **53 assumptions** — Oracle EBS AMS non-standard SLA commitments. **Approved v1.0 2026-06-19 (WP15F).** All 4 BU decisions resolved (P1 configurable; resolution SLAs on-request; fixed premium; service credits per engagement). **Overlays (supplements) AMS base pack.** approved_for_reuse = Yes. See WP15F_EBS_AMS_OVERLAY_PROMOTION_REPORT.md. |
| **EBS DRM Overlay** (WP15D → WP15F) | **62 assumptions** — Oracle EBS AMS dedicated/named resource model. **Approved v1.0 2026-06-19 (WP15F).** All 5 BU decisions resolved (per-engagement hours; rollover model; illness/leave; 30-day notice; runbook standard). **Overlays (supplements) AMS base pack.** approved_for_reuse = Yes. See WP15F_EBS_AMS_OVERLAY_PROMOTION_REPORT.md. |
| **HCM Recruiting Pack** (WP11 → WP16C) | **54 assumptions** across Sections 16–27. **Approved v1.0 2026-06-19 (WP16C).** All 7 decisions resolved (BU-REC-001–004/007 WP15F; BU-REC-005/006 WP16C). approved_for_reuse = Yes. Load after HCM Base for Oracle Recruiting (B87675/B95763) proposals. |
| **HCM Learning Pack** (WP11 → WP16C) | **37 assumptions** across Sections 28–35 (+6 BAU v1.2 pending authoring). **Approved v1.0 2026-06-19 (WP16C).** All 5 decisions resolved. LRN-SAT-001 confirmed as OTBI guidance only — no bespoke SETA extract. approved_for_reuse = Yes. Load after HCM Base for Learning Cloud (B85242) proposals. Governance constraint C-W3-002: cite Mr Price as sole referenceable Learning Cloud client only. |
| **HCM Talent Management Pack** (WP11 → WP16C) | **31 assumptions** across Sections 36–42 (+7 BAU v1.2 pending authoring). **Approved v1.0 2026-06-19 (WP16C).** All 4 decisions resolved. approved_for_reuse = Yes. Load after HCM Base for Talent Management (B94925) proposals. |
| **HCM Workforce Compensation Pack** (WP11 → WP16C) | **30 assumptions** across Sections 43–50 (+10 BAU v1.2 pending authoring). **Approved v1.0 2026-06-19 (WP16C).** All 5 decisions resolved. 1 merit plan + 1 bonus plan standard. approved_for_reuse = Yes. Load after HCM Base for Workforce Compensation (B109620) proposals. |

---

## Validated Facts (Do Not Override Without New Confirmed Source)

| Fact | Value |
|---|---|
| Founded | 2002 — "over 23 years" or "established in 2002" |
| Headcount | "more than 50 Senior Consultants" — do not use 100+ or 110+ |
| Oracle partner tier | Level 1 Partner (Gold EXPIRED August 2021) |
| Oracle expertise | Fusion Cloud Financials; Fusion Cloud HCM Core; Oracle Integration; EBS Migration to OCI; OCI Migration |
| Acumatica partner tier | Gold Partner (not Gold Certified) |
| B-BBEE level | Level 3 (RS-19451 — expires 2026-07-31) |
| Oracle awards | Business Impact Award EMEA 2024; Business Impact Award ECEMEA 2024 (+ 4 prior awards) |
| DBA team | "one of the largest locally based Oracle Applications DBA teams in South Africa" |
| Banking partners | 9: ABSA, FNB, Nedbank SA, Nedbank Namibia, Standard Bank SA, Standard Bank Namibia, Investec, Citi Bank UK, Santander Bank Chile |
| Sub-Saharan Africa | Botswana, Zambia, Mozambique, Namibia, Tanzania |
| International markets | USA, France, Abu Dhabi, Pakistan |
| Geographies NOT cited | Nigeria, Uganda, Bangladesh, Qatar, Ghana — no corpus evidence |
| Hein Blignaut IT career | Started 1996 at MTN — ~30 years |

---

## Document Register Notes

| Document | Currency | Action |
|---|---|---|
| `AI_CONTEXT.md` | CURRENT — rewritten 2026-06-16 | Primary AI session entry point |
| `HANDOVER.md` | CURRENT — rewritten 2026-06-16 | Primary human session entry point |
| `00_Governance/OUTSTANDING_ACTION_REGISTER.md` | CURRENT — created 2026-06-16 | Task register — update each session |
| `00_Governance/CURRENT_STATE.md` | **STALE** — v3.4 from 2026-06-14 | Secondary reference. Approved count is 47 (actual 49). Does not reflect WP8–WP13. |
| `00_Governance/COMPLIANCE_REGISTER.csv` | CURRENT — updated 2026-06-16 | COMP-008 and COMP-011 updated. |
| `06_Capabilities/MASTER_CAPABILITY_INDEX.md` | CURRENT — v1.2 from 2026-06-14 | 49 assets; governance restrictions per asset. |
| `08_Commercial/ASSUMPTION_LIBRARY_ROADMAP.md` | CURRENT — 2026-06-19 (v1.7) | 13 documents; 9 approved; 4 draft; EBS overlay packs + Acumatica + BeBanking promotions + WP16A counts applied. |
| `08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md` | CURRENT — 2026-06-22 (v2.0) | WP17C: Section 3.5 code block labels corrected Draft→Approved v1.0 for both EBS overlay packs; version v1.9→v2.0. Total 1,136 / approved 1,136 / draft 0. |
| `08_Commercial/Assumptions/OCI/OCI_ASSUMPTIONS_V1.md` | CURRENT — Approved v1.0 2026-06-16 | 174 assumptions (corrected WP14A); 14 decisions applied; BU-OCI-007 withdrawn |
| `08_Commercial/Assumptions/Acumatica/ACU_BASE_ASSUMPTIONS_V1.md` | **CURRENT — Approved v1.0 WP15C 2026-06-18** | 152 assumptions; Sections 120–139; 0 BU decisions pending; approved_for_reuse: Yes |
| `08_Commercial/Assumptions/Acumatica/ACU_ASSUMPTION_REGISTER.csv` | **CURRENT — Approved WP15C 2026-06-18** | 152 rows; all status = Approved |
| `08_Commercial/Assumptions/Acumatica/ACU_GAP_REPORT.md` | **CURRENT — Closed v1.2-Approved WP15C 2026-06-18** | All 14 gaps resolved; 0 outstanding |
| `08_Commercial/Assumptions/Acumatica/WP11I_A_REMEDIATION_REPORT.md` | CURRENT — Superseded WP15C 2026-06-18 | All blockers resolved |
| `08_Commercial/WP15C_ACUMATICA_PROMOTION_REPORT.md` | **CURRENT — WP15C 2026-06-18** | Acumatica promotion report — all 14 decisions, files updated, validation results |
| `08_Commercial/Assumptions/BeBanking/BEBANKING_BASE_ASSUMPTIONS_V1.md` | **CURRENT — Approved v1.0 2026-06-18 (WP14F)** | 117 assumptions; Sections 140–153; 0 BU decisions pending; approved_for_reuse: Yes |
| `08_Commercial/Assumptions/BeBanking/BEBANKING_ASSUMPTION_REGISTER.csv` | **CURRENT — Approved 2026-06-18 (WP14F)** | 117 rows; all status = Approved |
| `08_Commercial/Assumptions/BeBanking/BEBANKING_GAP_REPORT.md` | **CURRENT — Approved v1.2 2026-06-18 (WP14F)** | GAP-BB-001 fully resolved; all governance blockers cleared |
| `08_Commercial/WP14B_ASSUMPTION_LIBRARY_MASTER_REVIEW_REPORT.md` | **CURRENT 2026-06-17 (WP14B)** | 1,025 assumptions extracted; 12 exceptions; awaiting Acumatica + HCM human review |
| `08_Commercial/WP14C_TENDER_FACTORY_VALIDATION_REPORT.md` | **CURRENT 2026-06-17 (WP14C)** | ARM IT045 validation; YES WITH QUALIFICATIONS; WP15A–WP15I roadmap |
| `08_Commercial/WP14D_BEBANKING_REMEDIATION_REPORT.md` | **CURRENT 2026-06-18 (WP14D)** | 5 deleted / 15 modified / 9 decisions resolved |
| `08_Commercial/WP14E_BU_BB_002_DECISION_PAPER.md` | **CURRENT 2026-06-18 (WP14E)** | BU-BB-002 decision paper — Option A confirmed |
| `08_Commercial/WP14F_BEBANKING_PROMOTION_REPORT.md` | **CURRENT 2026-06-18 (WP14F)** | Promotion report — BeBanking Approved v1.0 |
| `08_Commercial/Assumptions/BeBanking/BEBANKING_GAP_REPORT.md` | CURRENT — Draft 2026-06-16 | 12 gaps (2 CRITICAL, 4 HIGH, 3 MEDIUM, 3 RESEARCH) |
| `08_Commercial/Assumptions/BeBanking/BEBANKING_SCOPE_BOUNDARY_GUIDE.md` | CURRENT — Draft 2026-06-16 | 15 scope boundary scenarios |
| `08_Commercial/[5 WP11F docs]` | CURRENT — Approved 2026-06-16 | Commercial Framework v1.0. Change logs in `08_Commercial/`. 6 CD items outstanding. |
| `08_Commercial/Assembly_Engine/` | **CURRENT — 2026-06-22 (WP17C: Engine PRODUCTION READY)** | 15 files: 7 WP12 reference library files + 6 WP17B engine components (BOM_RESOLVER, PACK_LOADER v1.1, RULE_PROCESSOR, ASSUMPTION_EXTRACTOR, ASSEMBLY_AUDITOR, ENGINE_ORCHESTRATOR) + 2 ARM IT045 dry-run outputs. |
| `08_Commercial/Reports/WP17C_REGRESSION_TEST_REPORT.md` | **CURRENT — WP17C 2026-06-22** | Assembly Engine regression test report — 5 tests / ALL PASS / PRODUCTION READY verdict / proceed to WP17D. |
| `00_Governance/WP17A0_DIRECTORY_STRUCTURE_AUDIT.md` | **CURRENT — WP17A-0 2026-06-19** | Full directory structure audit. Verdict: light targeted cleanup before WP17B Assembly Engine. 373 files / 16 top-level folders audited. 5 Priority 1 fixes required before Assembly Engine build. Migration plan in Sections 7–8. |
| `08_Commercial/Assumptions/Governance/GOVERNANCE_MASTER_DECISION_REGISTER.md` | CURRENT — 2026-06-16 (WP13) | 45 outstanding decisions: 2 CRITICAL + 13 HIGH + 20 MEDIUM + 10 LOW. OCI reconciled to 0 outstanding. |
| `08_Commercial/Assumptions/Governance/GOVERNANCE_APPROVAL_ROADMAP.md` | CURRENT — 2026-06-16 (WP13) | Three-wave plan: Wave 1 target 2026-06-23; Wave 2 target 2026-07-07; Wave 3 target 2026-07-28. |
| `08_Commercial/Assumptions/Governance/GOVERNANCE_WORKSHOP_PLAN.md` | CURRENT — 2026-06-16 (WP13) | Detailed agenda for BeBanking, Acumatica, Oracle HCM workshops. OCI not required (already approved). |
| `08_Commercial/Assumptions/Governance/GOVERNANCE_DECISION_RECORD_TEMPLATE.md` | CURRENT — 2026-06-16 (WP13) | Reusable template for decision records. 7 sections; naming convention table; governance constraints list. |
| `08_Commercial/Assumptions/AMS/EBS_AMS_SLA_OVERLAY_V1.md` | **CURRENT — Approved v1.0 WP15F 2026-06-19** | 53 assumptions; 4 decisions applied; approved_for_reuse: Yes |
| `08_Commercial/Assumptions/AMS/EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md` | **CURRENT — Approved v1.0 WP15F 2026-06-19** | 62 assumptions; 5 decisions applied; approved_for_reuse: Yes |
| `08_Commercial/WP15F_EBS_AMS_OVERLAY_PROMOTION_REPORT.md` | **CURRENT — WP15F 2026-06-19** | EBS overlay promotion report — 9 decisions, both packs Approved v1.0, before/after metrics |
| `08_Commercial/Assumptions/Governance/GOVERNANCE_DASHBOARD.md` | **CURRENT — 2026-06-19 (WP16C v1.7)** | PROGRAMME COMPLETE — **13 packs approved / 0 draft**; 1,135/1,135 assumptions approved; **0 decisions outstanding**; **100% resolved**; 38 days ahead of 2026-07-28 target. |
| `08_Commercial/WP16A_LIBRARY_RECONCILIATION_REPORT.md` | **CURRENT — WP16A 2026-06-19** | Library reconciliation baseline report — counts, discrepancies, corrections applied, classification model, WP16A baseline. |
| `08_Commercial/WP16B_HCM_HIGH_PRIORITY_DECISION_PACK.md` | **CURRENT — WP16B 2026-06-19** | BU Lead email pack — BU-REC-005 (Booster scope trigger) + BU-REC-006 (background check integration). Both HIGH priority. Reply "Confirmed" to each section. No wording changes needed on approval. |
| `08_Commercial/WP16B_HCM_LOW_PRIORITY_APPROVAL_PACK.md` | **CURRENT — WP16B 2026-06-19** | BU Lead batch email pack — 10 LOW decisions (BU-REC-007, BU-LRN-001/003/005, BU-TLT-001/003/004, BU-COM-001/002/005). Single email reply. Only BU-LRN-001 requires a placeholder fill; all others are tag removals. |
| `08_Commercial/WP16B_HCM_PROMOTION_READINESS.md` | **CURRENT — WP16B 2026-06-19** | Per-module promotion readiness: Recruiting (3 decisions, HIGH blocked), Learning/Talent/Compensation (3 LOW each, clear). Full critical path. Post-approval: 1,158 approved / 13 packs. |
| `08_Commercial/Assumptions/Governance/GOVERNANCE_RISK_REGISTER.md` | CURRENT — 2026-06-16 (WP13) | 14 governance risks (GR-001–014); 4 HIGH, 7 MEDIUM, 3 LOW. Critical: GR-010 Acumatica cert; GR-012 Draft pack misuse. |
| `00_Governance/REFERENCE_MASTER.csv` | CURRENT — 16 active + 11 archived | Primary reference register. |

---

*HANDOVER v4.3 | WP18C.2 COMPLETE — Section Library Consolidation — 7 architecture documents updated; SI-001/SI-005/SI-006/SI-007/KI-001 resolved; ARM IT045 regression corrected (56 sections); Platform maturity L3.5; NEXT: Risk Library Population → WP18D QA Engine | 2026-06-26*
*Previous handover history: CHECKPOINT_WAVE1_2026-06-10.md | CHECKPOINT_ORACLE_WAVE2_2026-06-11.md*
