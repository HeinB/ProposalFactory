# AI Context
**Last updated:** 2026-06-30 — **PF2-010 (V5) COMPLETE — PROPOSAL V5 NARRATIVE & STYLE ENGINE.** `proposal_v5_engine.py` v1.0. 11/11 sections authored (0 pending). Writing standard: four questions per section (challenge / proposal / why / outcome). Key rewrites: Exec Summary (Plennegy-specific from scratch); Understanding (specific problem statement); Proposed Solution (story structure); Why APPSolve (trust argument not company profile); Commercial (collaborative not legal); Next Steps (joint initiation). Two outputs: `CLIENT_PROPOSAL_PLENNEGY_V5.docx` (48 KB) + `CLIENT_PROPOSAL_PLENNEGY_V5.md` (10 KB — new type). TD-027 PROPOSAL_STYLE_GUIDE.md. Readiness 91/100. OUM = 0. 6/6 regression PASS. Platform **L6.5**.

*Previous: 2026-06-30 — **PF2-009 (PNE) COMPLETE.** `proposal_narrative_engine.py` v1.0: 11-section authored narrative (9 authored / 2 PENDING). Business-outcome framework. Three outputs: CLIENT (45 KB) + INTERNAL (429 KB) + TRACEABILITY (39 KB). Content compression: HCM 555 segs→6 pages; Methodology 140 segs→4 pages; Assumptions 497 segs→2 pages. GOV-PAE-001 enforced — zero OUM in client. TD-026. CLI: `python3 proposal_narrative_engine.py --tender <ID>`. 6/6 regression PASS. Platform **L6.4**.

*Previous: 2026-06-30 — **PF2-010 COMPLETE (PPPE OPERATIONAL).** `proposal_publishing_policy.py` v1.0: 10-rule policy enforcement layer between Renderer and DOCX. R6 fixed 48 OUM occurrences in KB-sourced content (R6 applies to ALL rendered KB sections — not just PAE-authored). R5 replaced 10 assumption packs (3 duplicate sections → 1 appendix executive summaries). R1 removed 64 governance subsections (Extraction Notes, Fact Verification, BU Decisions). Three profiles: CUSTOMER (94 KB / 33 secs) + INTERNAL (421 KB / 41 V2 secs) + REVIEW. TD-023/024/025. CLI: `python3 proposal_publishing_policy.py --tender <ID>`. 7/7 regression PASS. Platform **L6.3**.

*Previous: 2026-06-30 — **PF2-009 COMPLETE (PROPOSAL AUTHORING ENGINE OPERATIONAL).** `proposal_authoring_engine.py` v1.0: PAE authors client proposals from scratch. Two outputs: `CLIENT_PROPOSAL_[Tender].docx` (9 authored sections + 2 pending + 2 appendices; 61 KB Plennegy) + `INTERNAL_REVIEW_PACK_[Tender].docx` (Action Register + all 41 V2 KB sections; 431 KB Plennegy). **PERMANENT RULE GOV-PAE-001:** Oracle Fusion Cloud → Oracle Modern Best Practices / Oracle Success Navigator (OUM prohibited for Fusion Cloud). Architecture docs: TD-020 PROPOSAL_AUTHORING_STANDARD.md + TD-021 CLIENT_PROPOSAL_STANDARD.md + TD-022 INTERNAL_REVIEW_PACK_STANDARD.md. CLI: `python3 proposal_authoring_engine.py --tender <ID>`. 6/6 regression PASS, 0 violations. Full pipeline: KRPE→KVE→ARE→RSE→PSAE→Renderer→PPE→Shaper→PEE→**PAE**. Platform **L6.2**.

*Previous: 2026-06-30 — **PF2-008 COMPLETE (PROPOSAL EDITORIAL ENGINE OPERATIONAL).** `pee.py` v1.0: 5 editorial transforms (CF+BP+DD+BG+AU); V4 structure 11 body + 5 app; 6 authored sections; boilerplate strip (8 regex patterns); cross-section dedup (MD5); per-section budget caps. Plennegy V4: CLIENT 94KB / INTERNAL 97KB / TRACEABILITY 40KB / Editorial MD 5KB. Readiness 4.1→4.5/5. EDITORIAL_RULE_LIBRARY.md (33 rules) + PROPOSAL_EDITORIAL_STANDARD.md. CLI: `python3 pee.py --tender <ID>`. Full pipeline: KRPE→KVE→ARE→RSE→PSAE→Renderer→PPE→Shaper→PEE. Platform **L6.1**.

*Previous: 2026-06-30 — **PF2-008 COMPLETE (PROPOSAL SHAPING LAYER OPERATIONAL).** `proposal_shaper.py` v1.0: 5 modes (passthrough/full/full_multi/authored/authored_with_excerpt); V3 structure 10 body + 3 app; 4 authored sections (Governance table + Assumptions summary + Commercial framework + Next steps priority table). Plennegy V3 outputs: CLIENT 307 KB / INTERNAL 309 KB / TRACEABILITY 40 KB / Review MD 5 KB. V3 readiness 4.1/5 (V2 was 2.0/5). Pipeline: KRPE → KVE → ARE → RSE → PSAE → Renderer → PPE (V2) → Shaper (V3). PPE regression PASS. CLI: `python3 proposal_shaper.py --tender <ID>`. Platform maturity **L6.0**.

*Previous: 2026-06-30 — **PF2-007 COMPLETE (PROPOSAL PUBLISHING ENGINE OPERATIONAL).** `ppe.py` v1.0: 4 audience-specific DOCX outputs from rendered Markdown + Section Manifest. CLIENT (410 KB / 19 sections / no metadata) + INTERNAL (422 KB / 40 sections / completeness matrix) + TRACEABILITY (423 KB / 40 sections / manifest panels) + REVIEW REPORT (44 KB / 10-criteria / 65/100). Section classifier: PLACEHOLDER comment authoritative; AI sentinel para excluded from has_body. CLI: `python3 ppe.py --tender <ID>`. Architecture: PUBLISHING_ENGINE.md + PUBLICATION_PROFILE_STANDARD.md. Proposal Factory pipeline COMPLETE. Platform maturity **L5.9**. Open human actions: OAR-A01 (B-BBEE 2026-07-31 URGENT), OAR-C01/C02/C04.

*Previous: 2026-06-30 — **PF2-004A COMPLETE (DOCX RENDERER OPERATIONAL).** `docx_renderer.py` v1.0: professional Word proposal from Markdown; APPSolve brand styles; PLACEHOLDER/AI-DRAFT/HUMAN REVIEW callout boxes in review mode; auto-TOC; cover page; headers+footers+page numbers; tables with navy header rows. Plennegy pilot: 422 KB DOCX (4,259 paras / 332 tables / 40 sections) + 45 KB Review Report (10-criteria / 62/100 proposal readiness). 6/6 regression PASS. CLI: `python3 docx_renderer.py --tender <ID>`. Platform maturity **L5.8**.

*Previous: 2026-06-30 — **PF2-006 COMPLETE (FIRST LIVE OPERATIONAL VALIDATION — PLENNEGY BOM).** PLENNEGY-HCM-001 rendered end-to-end. 2 Platform Defects fixed: C-PSAE-001 (`--context YAML_FILE` added to PSAE); C-RENDERER-001 (S-49/S-51/A-01 DIRECT→MERGE; all assumption packs now rendered). Plennegy: RENDERED=21/PH=18/AI=3/NF=0 / 11,066 lines / 5 ASP packs / G-001 enforced. 6/6 regression PASS. Operational Readiness 78/100. Platform maturity **L5.7**. Open: OAR-C01/C02/A01.

*Previous: 2026-06-30 — PF2-005 COMPLETE (ASSUMPTION LIBRARY MATERIALISATION COMPLETE). `AssetIndex` extended with `additional_roots` + `document_id` indexing from YAML frontmatter. `ASSUMPTIONS_ROOT` (`08_Commercial/Assumptions/`) added as secondary scan root. BeBanking `document_id` defect fixed. AssetIndex 76 files / 125 IDs. Full pipeline: KRPE SUCCESS → KVE KHS 91/100 → PSAE 6/6 PASS → Renderer 6/6 PASS / NF=0. ARM-IT045: RENDERED=25/PH=17/AI=3/NF=0 (7,347 lines). Platform maturity **L5.6**.

*Previous: 2026-06-29 — PF2-004 COMPLETE (MARKDOWN PROPOSAL RENDERER OPERATIONAL). Renderer v1.0 (`proposal_renderer.py`): AssetIndex 50 files / 99 IDs; frontmatter stripping + internal section stripping + heading demotion; 6/6 regression PASS; ARM-IT045 full render 3,537 lines (RENDERED=16/PH=17/AI=3/NF=9); per-section audit 261 lines; 4 standard documents. Platform maturity L5.5.*

*Previous: 2026-06-29 — PF2-003 COMPLETE (PROPOSAL SECTION ASSEMBLY ENGINE OPERATIONAL). PSAE v1.0 (`proposal_section_engine.py`): 82 sections; deterministic Proposal Section Manifest per tender; 22/22 self-tests PASS; 6 regression scenarios (ARM-IT045 EBS-AMS→43, HCM-Mining→41, OIC→41, ERP→42, Acumatica→41, BeBanking→40 mandatory); 0 violations; SI-001/005/006/007 ordering rules enforced; GOV-010/ADR-001/B-BBEE governance encoded; Section Manifest YAML written for all 6 regression tenders. Platform maturity L5.4.*

*Previous: 2026-06-29 — PF2-002 COMPLETE (ASSEMBLY RULE ENRICHMENT ENGINE OPERATIONAL). ARE v1.0 (`are.py`): 49 CAP + 13 ASP enriched; 20/20 PASS; 62/62 valid; 6 regression 0 violations; GOV-010 encoded. Registry BUILD-20260629-ARE-001. Platform maturity L5.3.*

*Previous: 2026-06-29 — PF2-001 COMPLETE (RISK SELECTION ENGINE OPERATIONAL). RSE v1.0 (`rse.py`): 40 RSK via AREL V1.0; 17/17 PASS; 5 regression, 0 violations. Platform maturity L5.2.*

*Previous: 2026-06-28 — WP19D COMPLETE (KNOWLEDGE PLATFORM VERSION 1.0 COMPLETE). KVE v2.0: 76 rules; AREL V1.0 evaluator (86/86 PASS); KHS 91/100 EXCELLENT; platform maturity L5.1.*

*Previous: 2026-06-28 — WP18B-EXT.2 COMPLETE (Enterprise Risk Library APPROVED). 40/40 risks approved; TD-001 RESOLVED; AV-011 BLOCK UNBLOCKED. 1 rating reversion: RC-DATA-004 CRITICAL→HIGH (BU-RL-007 Option B). mandatory_if=TRUE confirmed for RC-OPS-001. Platform maturity L4.3.*

*Previous: 2026-06-28 — WP19B COMPLETE (AREL V1.0 FROZEN). ASSEMBLY_RULE_EXPRESSION_LANGUAGE.md frozen: grammar + 20 context variables + null-safe semantics. ASSEMBLY_RULE_VALIDATION_STANDARD.md: 30 ARVAL rules (3 tiers). ASSEMBLY_RULE_TEST_SUITE.md: 80 test cases (100% pass threshold). Platform maturity L4.2.*

*Previous: 2026-06-28 — WP19A.1 COMPLETE (Registry Data Quality Remediation). KRPE v1.0 → v1.1: 16 defects fixed — all mandatory fields now populated (governance_notes, pattern_applicability, proposal_sections, created, created_by, cap_ext.platform). Registry Build BUILD-20260628-064745: 1,198 entries / 0 RI-014 failures. KVE clean run ARM-IT045: BLOCK=1 (AV-011) / ERROR=0 / WARNING=1 (RI-004) / 641 assets in manifest. Platform maturity L4.1.*

*Previous: 2026-06-27 — WP19A COMPLETE (KVE Phase A). `kve_engine.py` implemented: 22 BLOCK rules. First run: BLOCK=1/ERROR=1(RI-014)/0 assets. ADR-002 enforced. IG-001 CLOSED. Platform maturity L4.0.*

*Previous: 2026-06-27 — WP18G COMPLETE (KVE Readiness Cleanup). SIMP-001 + SIMP-002 resolved. KMS v1.1. lifecycle_status: APPROVED in 49 CAP + 13 ASP. KRPE Build 5: 62/62 APPROVED, 0 errors.*

*Previous: 2026-06-27 — WP18F COMPLETE (Platform Integration Review & Architecture Freeze). 17 governing documents reviewed. 12 architectural findings. 13 ADRs frozen. 9 simplifications (2 P1 pre-KVE). Implementation readiness: **7.80/10 — READY WITH MINOR OBSERVATIONS**. 6 deliverable docs at `08_Commercial/Assembly_Engine/` and `08_Commercial/Reports/`. **ARCHITECTURE FREEZE DECLARED.** Platform maturity L3.8.*

*Previous: 2026-06-27 — WP18E-IMP-B COMPLETE (Registry Verification & Certification). 4 defects fixed. Build 4: 1,198 APPROVED | 0 errors. Certified "for Production with Observations." Previous: WP18E-IMP-A COMPLETE (KRPE Phase A). Engine `08_Commercial/Assembly_Engine/krpe.py` operational. 49 CAP + 13 ASP + 1,136 ASM | 0 errors | 1.1s. Previous: WP18B-EXT.3A COMPLETE (Registry Architecture). 76 rules.

> **STALE CONTEXT WARNING:** If the date above is more than 14 days ago, read HANDOVER.md before using this file. Project state changes rapidly. Do not assume the asset counts, governance restrictions, or compliance status below are still current without checking.

> **RETRIEVAL-FIRST:** Never load the full KB corpus into context. Retrieve only the specific file(s) needed for each task. Check MASTER_CAPABILITY_INDEX.md for asset paths and governance restrictions before using any capability statement.

---

## Governing Principles (Post-V5 — Established 2026-06-30)

These principles apply to all future AI proposal work. They were established when V5 (Proposal Narrative & Style Engine) set a new quality floor of 91/100 readiness.

**Narrative quality is permanent.** Do not regress to V2-style knowledge-dump output. V5 is the floor. The PROPOSAL_STYLE_GUIDE.md (TD-027) is the governing standard for all client-facing proposal writing.

**The four questions.** Every section of every client proposal must answer: (1) What is the customer's challenge? (2) What does APPSolve propose? (3) Why is this approach better? (4) What business outcome will the customer receive? If a paragraph does not answer one of these, it should not exist.

**Knowledge assets are source material.** They are not proposal sections. Never paste KB content verbatim into a client proposal. Compress, author, and narrate.

**GOV-PAE-001 is permanent.** Oracle Unified Method (OUM) must never appear in a Fusion Cloud proposal. Oracle Modern Best Practices / Oracle Success Navigator are the required terms.

**Client proposal clean room.** No IDs (ASM, CAP, ADR, etc.), no governance artefacts, no draft markers, no extraction notes, no source evidence tables in any client-facing document.

**Architecture is stable.** The Proposal Factory pipeline is COMPLETE at L6.5. Do not add architectural complexity unless a defect requires it. Future work is narrative quality, KB content, and new tender contexts — not new pipeline components.

**Human gate before next engine work.** The immediate next action after any session that produces a client proposal is human review of the DOCX, not the next AI work package.

---

## Tender Factory Objective

Build and maintain a reusable, governed Knowledge Base that enables APPSolve to assemble high-quality, factually accurate, commercially protected tender responses for Oracle, Acumatica, and BeBanking engagements — without authoring from scratch each time.

**Current active work:** PF2-010 (V5) COMPLETE 2026-06-30 — Proposal V5 Narrative & Style Engine operational. Outputs: `CLIENT_PROPOSAL_PLENNEGY_V5.docx` + `CLIENT_PROPOSAL_PLENNEGY_V5.md`. Platform maturity **L6.5**. Open Plennegy human actions: OAR-A01 (B-BBEE URGENT 2026-07-31), OAR-C01 (HB AM), OAR-C02 (Costing), OAR-C04 (client parameters). Next AI work: PIR-001 (sub-section EXTRACT), RFP extractor, or KB Wave 5 assets.

**WP17D-1 status (correction):** COMPLETE 2026-06-25 — Inline text assembly operational. ARM IT045: 594 assumptions inline text + 175 body Key Assumptions (dual-output Option B). 10/10 validation PASS.

---

## Company

APPSolve is a South African technology services company. Established 2002. Over 23 years of operation. Offices in Gauteng and Western Cape. **More than 50 Senior Consultants** (each with 10+ years' experience).

**International presence:** Sub-Saharan Africa (Botswana, Zambia, Mozambique, Namibia, Tanzania). Project delivery: USA, France, Abu Dhabi, Pakistan.

**Do not cite:** Nigeria, Uganda, Bangladesh, Qatar, Ghana — no corpus evidence across 18,400 files.

---

## Business Units

### Oracle
Oracle Level 1 Partner (Gold EXPIRED August 2021 — **never cite "Gold Partner"**). Services: OCI, Oracle EBS (R11/R12), Oracle Fusion (ERP, HCM, SCM, OIC, APEX, EPM/BI), Oracle DBA, Managed Services. Oracle Value-Added Reseller.

### Acumatica
Acumatica Gold Partner (**not Gold Certified**). VAR. Industries: Manufacturing, Distribution, FMCG, Professional Services, Higher Education.

### BeBanking
APPSolve's proprietary Host-to-Host banking integration product. ERP integration: Oracle EBS (R11/R12), Oracle Fusion, Acumatica, SAP (environments only — see SAP rule).

**Banking partners (9 confirmed):** ABSA, FNB, Nedbank SA, Nedbank Namibia, Standard Bank SA, Standard Bank Namibia, Investec, Citi Bank UK, Santander Bank Chile.

**BeBanking permanent rules:**
- **SAP rule:** Use "BeBanking integrates with SAP environments" only — no module-level claims until BQ-WEB-04 confirmed
- **SWIFT rule:** Bank-intermediated model only — do not claim direct SWIFT membership
- **Acumatica payroll rule:** BeBanking Payroll H2H = Oracle EBS and Oracle Fusion payroll sources only — never imply Acumatica payroll integration (Acumatica has no SA payroll module)

---

## Consultant Records

**ADR-001 (2026-06-10):** APPTime is authoritative for all consultant CVs. KB stores Consultant Index Records only.

**Permanent rules — enforced without exception:**
1. Never generate CV text from KB records — records are for skill matching only
2. Use records to identify candidates — then instruct user to obtain current CVs from APPTime
3. APPTime overrides any KB record where data conflicts
4. Respect `available_for_tenders` flag — do not propose unavailable consultants

**Index location:** `00_Governance/CONSULTANT_INDEX.csv` (49 consultants: 37 Oracle / 7 Cross-BU / 5 Associates; no Acumatica-specific or BeBanking consultants yet)

---

## Approved Content (49 assets)

All `approved_for_reuse: Yes`. Approved by Hein Blignaut (BU Lead). Read from `07_Approved_Content/Approved/` or KB copies in `06_Capabilities/`.
Full governance per asset: `06_Capabilities/MASTER_CAPABILITY_INDEX.md` (v1.2).

### Cross-BU — 6 assets (`Approved/Cross_BU/`)
W1S1-001 Company Overview | W1S1-002 Company History | W1S1-006 Awards & Recognition | W1S1-007 Delivery Model | W1S1-008 Geographic Presence | W1S1-009 Key Differentiators

*W1S1-006: award table unrestricted; success story URLs (Tiger Brands, USAID, UT Grain) pending verification — do not cite those URLs.*

### Oracle — 21 assets (`Approved/Oracle/` + `06_Capabilities/Oracle/`)

**Partnership (1):** W1S1-003 Oracle Partnership Statement — Level 1 only; annual OPN revalidation required

**Platform and Managed Services (5):**
W2S1-001 Fusion Capability | W2S1-002 EBS Capability | W2S1-003 DBA Executive Summary | W2S1-004 Managed Services | W2S1-005 Implementation Methodology

**HCM Wave 3 (9) — all in `06_Capabilities/Oracle/Oracle_HCM/`:**
W3S1-001 HCM Core | W3S1-002 Talent Management | W3S1-003 Recruiting Cloud | W3S1-004 Learning Cloud | W3S1-005 Workforce Compensation | W3S1-006 HCM Analytics | W3S1-007 Workforce Management | W3S1-008 Help Desk & HR Service Delivery | W3S1-009 Payroll Interface & Integration

**Wave 4 ERP/OIC/HCM (6) — `06_Capabilities/Oracle/`:**
W4-HCM-002 Oracle Journeys | W4-AI-002 Oracle AI Skills | W4-INT-001 OIC Accelerators | W4-ERP-001 Fusion Financials | W4-ERP-002 Fusion Procurement | W4-ERP-003 PPM

### Acumatica — 9 assets (`Approved/Acumatica/`)
W1S1-004 Partnership | W1S2-001 Financials | W1S2-002 Distribution | W1S2-003 Inventory | W1S2-004 Manufacturing | W1S2-005 CRM | W1S2-006 Field Services | W1S2-007 PaySpace Payroll Integration | W1S2-009 Project Accounting | W5-ACU-001 Support & Managed Services

### BeBanking — 11 assets (`Approved/BeBanking/` + `Approved/Cross_BU/`)
W1S1-005 BeBanking Overview | W1S3-001 through W1S3-010 (all 10 H2H banking modules)

### Cross-Platform — 2 assets
W2S1-005 Oracle Implementation Methodology (Oracle-specific) | W5-METH-001 ERP Implementation Methodology (platform-agnostic — use for Acumatica/BeBanking/multi-platform tenders)

---

## Assumption Library (WP11)

Assembly rules: `08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md` | Governance: `08_Commercial/ASSUMPTION_GOVERNANCE.md`

| Pack | Status | Count | Location |
|---|---|---|---|
| HCM Base | **Approved v1.1 — WP16D 2026-06-19** | **115** | `08_Commercial/Assumptions/HCM/HCM_BASE_ASSUMPTIONS_V1.md` |
| OIC Integration | **Approved 2026-06-15** | **104** *(WP16A)* | `08_Commercial/Assumptions/OIC/OIC_ASSUMPTIONS_V1.md` |
| Oracle ERP | **Approved 2026-06-15** | **123** *(WP16A)* | `08_Commercial/Assumptions/ERP/ERP_ASSUMPTIONS_V1.md` |
| OCI Infrastructure | **Approved 2026-06-16** | 174 | `08_Commercial/Assumptions/OCI/OCI_ASSUMPTIONS_V1.md` |
| AMS / Managed Services | **Approved 2026-06-15** | **84** *(WP16A)* | `08_Commercial/Assumptions/AMS/AMS_ASSUMPTIONS_V1.md` |
| HCM Recruiting | **Approved v1.0 — WP16C 2026-06-19 — 0 BU items outstanding** | **54** | `08_Commercial/Assumptions/HCM/HCM_RECRUITING_ASSUMPTIONS_V1.md` |
| HCM Learning | **Approved v1.0 — WP16C 2026-06-19 — 0 BU items outstanding** | **37** | `08_Commercial/Assumptions/HCM/HCM_LEARNING_ASSUMPTIONS_V1.md` |
| HCM Talent | **Approved v1.0 — WP16C 2026-06-19 — 0 BU items outstanding** | **31** | `08_Commercial/Assumptions/HCM/HCM_TALENT_ASSUMPTIONS_V1.md` |
| HCM Compensation | **Approved v1.0 — WP16C 2026-06-19 — 0 BU items outstanding** | **30** | `08_Commercial/Assumptions/HCM/HCM_COMPENSATION_ASSUMPTIONS_V1.md` |
| Acumatica Base | **Approved v1.0 — WP15C 2026-06-18 — 0 BU items outstanding** | **152** | `08_Commercial/Assumptions/Acumatica/ACU_BASE_ASSUMPTIONS_V1.md` |
| BeBanking Base | **Approved v1.0 — WP14F 2026-06-18 — 0 BU items outstanding** | **117** | `08_Commercial/Assumptions/BeBanking/BEBANKING_BASE_ASSUMPTIONS_V1.md` |
| EBS SLA Overlay | **Approved v1.0 — WP15F 2026-06-19 — 0 BU items outstanding** | **53** | `08_Commercial/Assumptions/AMS/EBS_AMS_SLA_OVERLAY_V1.md` |
| EBS DRM Overlay | **Approved v1.0 — WP15F 2026-06-19 — 0 BU items outstanding** | **62** | `08_Commercial/Assumptions/AMS/EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md` |

**All 13 assumption packs Approved v1.0. GOVERNANCE PROGRAMME COMPLETE (WP16C 2026-06-19). WP16D post-programme enhancement: HCM-JRN-001 added 2026-06-19.** Total: **1,136** approved assumptions across 13 packs. All packs available for immediate proposal use (approved_for_reuse: true).

---

## Assembly Engine (WP17B + WP17C)

**Status:** PRODUCTION READY (WP17C 2026-06-22). All 5 regression tests pass. Cleared for live tender use.

**Location:** `08_Commercial/Assembly_Engine/`

### Engine Components (Step 1–5)

| Step | File | Purpose |
|---|---|---|
| 1 | `BOM_RESOLVER.md` | Translates tender profile + BOM codes → ordered pack manifest |
| 2 | `PACK_LOADER.md` (v1.1) | Validates pack eligibility; confirms versions and counts; establishes load order |
| 3 | `RULE_PROCESSOR.md` | Applies assembly rules (A–E) and suppression rules (S1–S4) |
| 4 | `ASSUMPTION_EXTRACTOR.md` | Extracts assumptions; handles suppressions; produces ASSEMBLED_ASSUMPTION_SCHEDULE.md |
| 5 | `ASSEMBLY_AUDITOR.md` | Generates ASSEMBLY_AUDIT_REPORT.md with full decision trail |
| — | `ENGINE_ORCHESTRATOR.md` | Entry point; sequences Steps 1–5; pre-submission checklist |

### Assembly Rules Reference

- **Rule A:** Base pack loads first; module packs second; overlays last
- **Rule B:** All packs additive — no base assumption overrides
- **Rule C:** No duplicate IDs (enforced structurally by unique ID prefixes per pack)
- **Rule D:** Every loaded pack must have a BOM trigger
- **Rule E:** All -EXC- exclusion assumptions must be included
- **Rule JRN-1:** HCM-JRN-001 auto-included when HCM Base loads (embedded in assumption #115)
- **Rule OCI-1:** OCI Pack mandatory for EBS on OCI / Fusion on OCI / OIC on OCI / AMS-managed OCI

### Suppression Rules

| Rule | Suppresses | Replaced By | Context |
|---|---|---|---|
| S1 | AMS-INC-004 | EBS-DRM-013 | EBS AMS only — not Fusion AMS |
| S2 | AMS-SLA-001, AMS-PRI-001/002/003 | EBS-SLA equivalents | When EBS SLA Overlay loaded |
| S3 | AMS-SLA-005 | EBS-DRM-001 | When EBS DRM Overlay loaded |
| S4 | SLA Overlay defers to DRM Overlay | — | On shared topics when both overlays loaded |

### Tested Assembly Patterns (WP17C)

| Pattern | Packs | Net Assumptions |
|---|---|---|
| EBS AMS Full Stack | ERP + OCI + OIC + AMS + EBS SLA Overlay + EBS DRM Overlay | 594 |
| HCM Full Suite | HCM Base + REC + LRN + TLT + COM | 267 |
| OIC Standalone | OIC | 104 |
| BeBanking + OIC + AMS | BeBanking + OIC + AMS | 305 |
| Acumatica Standalone | Acumatica | 152 |

### Known Limitations (WP17D-1 COMPLETE; Proposal Factory MVP proven WP18C)

1. **ID-only output resolved** — WP17D-1 COMPLETE 2026-06-25. ARM IT045: 594 assumptions inline text + 175 body Key Assumptions. Full text assembly operational.
2. **No named BeBanking+AMS pattern** — assembled additively; Advisory AF-01 (add to Section 3.4 in future revision)
3. **AMS-PAT-001 context note** — applies to Oracle Fusion component only in BeBanking; Advisory AF-02
4. **GAP-007 (KT/onboarding pack)** — medium priority; no AMS KT assumption pack
5. **GAP-005 (Mining Charter)** — medium priority; no mining compliance assumption pack
6. **OneDrive mkdir restriction** — new subdirectories cannot be created in synced paths; use `08_Commercial/Reports/` for all new output files

---

## Proposal Factory (WP18A–WP18C.3)

**Status:** OPERATIONAL at Platform Maturity L3.5  
**Architecture:** `08_Commercial/Assembly_Engine/PROPOSAL_FACTORY_ARCHITECTURE.md`  
**Baseline:** `08_Commercial/Reports/WP18Z_SESSION_BASELINE.md`

### Tender Intelligence Layer (Stage 0) — NEW WP18C.3

The TIL is the entry point for every proposal. Given a tender document, it produces an APPROVED `[TENDER_ID]_TENDER_PROFILE.md` that deterministically drives all downstream stages.

| File | Purpose |
|---|---|
| `TENDER_PROFILE_STANDARD.md` | YAML schema (8 blocks; 30+ fields with source/extraction/validation/default rules) |
| `TENDER_INTELLIGENCE_RULES.md` | 10-step TIL processing sequence; downstream trigger matrix; 15 governance rules |
| `PROPOSAL_PATTERN_ENGINE.md` | 13-pattern classification; section scoping (AO-002); SI-001 fix (S-38 excluded for AMS) |
| `CAPABILITY_SELECTION_ENGINE.md` | BOM→capability asset lookup for all 16 BOMs; deselection rules |
| `METHODOLOGY_SELECTION_ENGINE.md` | Pattern→methodology asset + project plan template |
| `REFERENCE_SELECTION_ENGINE.md` | 7-dimension/10-point scoring; 12 exclusion rules; AM approval per-tender |

**Key rules encoded:**
- AMS (Pattern 13): EXCLUDES S-34, S-35, S-38, S-39–43; INCLUDES S-70–76
- Implementation (Patterns 1–9, 11, 12): EXCLUDES S-70–76
- S-38 excluded for AMS (SI-001 fix) — S-73 is the AMS-correct equivalent
- All 15 governance rules pre-applied at Stage 0

### Current Proposal Pipeline

| Stage | Name | Status | Engine |
|---|---|---|---|
| 0 | Tender Intelligence (TIL) | **L3.5 OPERATIONAL** | 6 TIL engines (WP18C.3) |
| 1 | Tender Analysis | L1 Manual | None |
| 2 | Requirement Extraction | L2 AI-Assisted | None |
| 3 | BOM Resolution | **L5 PRODUCTION READY** | Assembly Engine (WP17B/C) |
| 4 | Capability Selection | **L3.5 DETERMINISTIC** | CAPABILITY_SELECTION_ENGINE.md |
| 5 | Reference Selection | **L3.5 DETERMINISTIC** | REFERENCE_SELECTION_ENGINE.md |
| 6 | Methodology Selection | **L3.5 DETERMINISTIC** | METHODOLOGY_SELECTION_ENGINE.md |
| 7 | Assumption Assembly | **L5 PRODUCTION READY** | Assembly Engine + WP17D-1 |
| 8 | Proposal Assembly | L3.0 MVP | Manual; CONTENT_SOURCE_MATRIX guides |
| 9 | QA | L1 Manual Framework | PROPOSAL_QA_FRAMEWORK.md |
| 10 | Rendering | L0 Not Built | WP19 future |

### Proposal Sections

82 sections defined in PROPOSAL_SECTION_LIBRARY.md (S-01 to S-76, A-01 to A-06).

**For AMS (Pattern 13, ARM IT045 example):** 43 sections in scope / 39 excluded  
**For HCM Full Suite (Pattern 1):** ~65 sections in scope / ~17 excluded

Automation: ~85% deterministic (DIRECT/EXTRACT/MERGE); ~15% human-required (AI-GENERATE 9%, TEMPLATE 4%, PLACEHOLDER 2%)

### Delivery Patterns (13)

1. Oracle HCM Full Suite — Single Go-Live  
2. Oracle HCM Full Suite — Phased Go-Live  
3. Oracle HCM Core + Payroll Interface  
4. Oracle Recruiting Cloud (Standalone)  
5. Oracle Learning Cloud (Standalone)  
6. Oracle OIC Integration (Standalone)  
7. Oracle Fusion ERP (Multi-Module)  
8. Oracle Fusion ERP (Single Module)  
9. Oracle EBS Implementation  
10. Oracle DBA / Managed Services  
11. Acumatica ERP  
12. BeBanking H2H  
13. AMS / Managed Services Onboarding ← current dominant tender type

### Factory Governance Rules Embedded at Stage 0

| Rule | Summary |
|---|---|
| GOV-006 | Oracle Gold Partner EXPIRED 2021 — Level 1 only; never cite "Gold Partner" |
| GOV-007 | B-BBEE Level 3 expires 2026-07-31 — OAR-A01 ACTIVE for all submissions at/after that date |
| GOV-001/002/003 | DFA/CCBA/SAA never named externally |
| GOV-004 | Redpath Mining not referenceable (Rule 21.5) |
| GOV-005 | Hollywood Bets — AM approval required at each tender |
| GOV-008/009 | OIC: Section 13.2 never external; HIST-018 billing never external |
| GOV-010 | W3S1-005 Compensation — Mining sector ONLY (G-001) |
| GOV-011 | Headcount — "more than 50 Senior Consultants" ONLY |
| GOV-012 | W4-HCM-004 RETIRED — never select |
| GOV-013 | W1S2-008 ARCHIVED — never select |
| GOV-015 | KPMG — AM-W4E3-001 ACTIVE — anonymous reference only for PPM |

---

## Commercial Framework (WP11F — Approved by BU Lead 2026-06-16)

5 documents in `08_Commercial/` — all **Approved v1.0 by BU Lead (Hein Blignaut) 2026-06-16** (WP11F-A).
These are internal governance documents. Do not include actual rates or monetary thresholds in external submissions — these are held in the Commercial Director's authority schedule.

| Document | Purpose | Change Log |
|---|---|---|
| `RATE_CARD_FRAMEWORK.md` | Role taxonomy, rate band structure, rate types — no actual rates | `RATE_CARD_CHANGE_LOG.md` |
| `ESTIMATION_GUIDE.md` | Bottom-up estimation methodology, phase model, complexity tiers | `ESTIMATION_CHANGE_LOG.md` |
| `CR_PRICING_MODEL.md` | Change Request classification, pricing methods, AMS CR threshold (2 hours) | `CR_PRICING_CHANGE_LOG.md` |
| `EFFORT_MULTIPLIERS.md` | Complexity and risk adjustment factors (C1–C4, LE, timeline, geography) | `EFFORT_MULTIPLIER_CHANGE_LOG.md` |
| `COMMERCIAL_GOVERNANCE.md` | Approval thresholds, discount authority, commercial file requirements | `COMMERCIAL_GOVERNANCE_CHANGE_LOG.md` |

**WP11F-A decision summary:** 40 BU items raised; 34 approved; 6 deferred to Commercial Director; 1 pending BU action.
**Commercial Director items outstanding (6):** BU-RC-004 (AMS rate disclosure), BU-RC-008 (AMS escalation rate), BU-CR-003 (CR monetary thresholds), BU-EM-006 (compound multiplier cap), BU-GOV-001 (approval thresholds), BU-GOV-003 (margin floors).

---

## Reference Register

**Full register:** `00_Governance/REFERENCE_MASTER.csv`
**AM approval required at every submission for all named clients.**

### Oracle — Active (11 letters)
| Ref | Client | Products | Letter Date |
|---|---|---|---|
| REF-ORA-007 | Oracle Corporation SA | Partner endorsement | 2024 |
| REF-ORA-001 | Investec Bank | Oracle Fusion Finance + Procurement | Sep 2023 |
| REF-ORA-002 | NALA Renewables | Oracle Fusion ERP (GL, AP, AR, FA, CM, Projects) | Aug 2025 |
| REF-ORA-003 | Cape Union Mart | Oracle Fusion Finance + Procurement | 2025 |
| REF-ORA-004 | Assore | Oracle EBS Finance + DBA | Aug 2025 |
| REF-ORA-005 | Adcock Ingram | Oracle EBS Finance + DBA + APEX | Aug 2025 |
| REF-ORA-006 | Mr Price Group | Oracle Learning Cloud (implementation only; T&L = PoC) | Sep 2024 |
| REF-ORA-008 | ARM | Oracle EBS Finance + HCM + OIC + OCI + APEX | Jul 2025 |
| REF-ORA-009 | MTN Group | Oracle OIC + Cloud Finance + OCI (managed services) | Aug 2025 |
| REF-ORA-010 | WITS | Oracle EBS + BeBanking H2H | Aug 2025 |
| REF-ORA-011 | Stellenbosch University | Oracle EBS Performance Management | Aug 2025 |

**Not yet registered as signed letter:** Hollywood Bets (AM approval required each time); KPMG (AM-W4E3-001 ACTIVE — blocked).

### Acumatica — Active (5 letters)
REF-ACU-001 Dunlop Srixon (Distribution) | REF-ACU-002 FuelU2 (Distribution — PDF scanned) | REF-ACU-003 Maxiflex (Manufacturing + CRM) | REF-ACU-004 At Source (Manufacturing + WMS) | REF-ACU-005 Interconnect Systems (Distribution + CRM + PA — largest Acumatica contract value)

### Archived / Excluded
- **REF-ARC-002 DFA — EXCLUDED PERMANENTLY (Rule 21.4)**. Internal corroboration only.
- REF-ARC-001 Afrocentric — restricted; BU Lead approval required to name.
- REF-ARC-003 Tiger Brands — 2021 letter; assess vintage per tender.
- REF-ARC-004 SARB — ~8 year old scanned PDF; unreadable.
- REF-ARC-005 FNB — ~9 year old scanned PDF; unreadable.
- REF-ARC-006 Harmony Gold — 2024 date but scanned PDF; obtain text copy.

---

## Governance Rules

### Client Naming — Permanent
| Client | Rule |
|---|---|
| **DFA** | NEVER named — Rule 21.4 PERMANENT |
| **CCBA** | NEVER named — internal evidence only |
| **SAA** | NEVER named as client — source material only (Rule 21.1 Aviation) |
| **Redpath Mining** | NOT referenceable — Rule 21.5 — until go-live + BU Lead waiver |
| **Hollywood Bets** | Referenceable — AM approval required at each tender |
| **KPMG** | NOT named — AM-W4E3-001 ACTIVE — pending signed letter |

### Section Exclusions
- W3S1-008 Help Desk: **Section 14.2 MUST NOT appear in external submissions** (PT-W8-007)
- W3S1-009 Payroll Interface: **Section 13.2 MUST NOT appear in external submissions** (PT-W9-008)

### Product Integrity
- HIST-018 billing (R825,170): MUST NEVER appear in any external submission (W4-INT-001)
- Oracle HR Help Desk (B87388) ≠ Oracle Service Cloud / Fusion Service / B2C Service / ITSM
- W3S1-005 Compensation: Mining sector ONLY (G-001) — Retail attribution prohibited
- W4-HCM-004 T&L: RETIRED — no standalone T&L statement until production evidence
- Approved KB supersedes old company profile for all covered capability areas

### Source Pipeline Enforcement
- `Candidate_Content/` and `Review_Required/`: NEVER cite in tender — Approved/ only
- `approved_for_reuse: Yes`: BU Lead action only — never set by AI or extractor
- Source files in `Parties/Customers/` and `Tender Pack/`: read-only — never move, copy, or modify
- Rule 6 (Evidence Source Registration): Every cited source must have a registered HIST ID in DOCUMENT_REGISTER.csv

---

## Source Hierarchy

When drafting tender content, use sources in this order:

1. **Approved content** — `07_Approved_Content/Approved/` or KB destinations (`06_Capabilities/`, etc.)
2. **Reference letters** — `04_References/` or `Tender Pack/References/` — signed PDFs only (REFERENCE_MASTER.csv)
3. **Historical proposal templates** — `Parties/Customers/0. Proposal Templates/` — extract; do not copy verbatim
4. **Historical tender submissions** — `Parties/Customers/[Client]/RFP/` — extract and modernise
5. **Tender Pack documents** — compliance, evidence archive
6. **AI-authored content** — only when no source exists; flag as AI-authored; must be reviewed before use

---

## Validated Facts (Do Not Override Without New Confirmed Source)

| Fact | Value |
|---|---|
| Founded | 2002 — "over 23 years" or "established in 2002" |
| Headcount | "more than 50 Senior Consultants" — never use 100+ or 110+ |
| BEE level | Level 3 (RS-19451 — **expires 2026-07-31**) — do not cite after expiry |
| Oracle partner tier | Level 1 Partner (Gold EXPIRED August 2021) |
| Oracle expertise (published) | Fusion Cloud Financials; Fusion Cloud HCM Core; Oracle Integration; EBS Migration to OCI; OCI Migration |
| Acumatica partner tier | Gold Partner (not Gold Certified) |
| Oracle awards | Business Impact Award EMEA 2024; Business Impact Award ECEMEA 2024; SaaS Partner of Year 2016 SADC; SaaS Partner of Year — New Entrant 2019 SADC; Innovation Sustainability Award 2015 + 2016 Global |
| DBA team | "one of the largest locally based Oracle Applications DBA teams in South Africa" |
| Banking partners | 9: ABSA, FNB, Nedbank SA, Nedbank Namibia, Standard Bank SA, Standard Bank Namibia, Investec, Citi Bank UK, Santander Bank Chile |
| Sub-Saharan Africa | Botswana, Zambia, Mozambique, Namibia, Tanzania |
| International markets | USA, France, Abu Dhabi, Pakistan |
| Removed geographies | Nigeria, Uganda, Bangladesh, Qatar, Ghana — no corpus evidence |
| Directors' Resolution | RENEWED 2026-06-15 — valid for all tender submissions |
| Public Liability Insurance | OBTAINED 2026-06-15 — confirm exact expiry from policy |
| Hein Blignaut IT career | Started 1996 at MTN — ~30 years |

---

## Content Gap Awareness

### Gaps now resolved (since last AI_CONTEXT update):
All Waves 1–4 gaps (Oracle methodology, Acumatica modules, BeBanking modules) — fully covered by 49 approved assets.

### Remaining capability gaps:
- **Acumatica Field Services** — W1S2-006 approved but narrow (Interconnect Systems only)
- **Acumatica Payroll** — W1S2-007 approved but no Tier 1 delivery evidence; SA payroll integration approach documented
- **Acumatica Construction** — W1S2-008 ARCHIVED — not an APPSolve offering
- **BeBanking Acumatica integration detail** — compatibility confirmed; detailed architecture undocumented (OAR-G04)
- **OCI Infrastructure** — OCI Assumption Pack Approved v1.0 (WP11H-A 2026-06-16); no standalone OCI capability statement narrative yet — assumption pack is the primary OCI commercial artefact
- **W3S1-005 Workforce Compensation** — Mining sector only; no Tier 1 referenceable client yet
- **W1S2-007 Payroll Integration** — no Tier 1 delivery evidence
- **KPMG PPM reference** — blocked until AM-W4E3-001 cleared

### Module packs not yet created:
None — all 13 packs exist and are **Approved v1.0** (WP16C 2026-06-19). No Draft packs remain.

---

## Repository Structure

```
Tender Knowledge Base/
├── 00_Governance/          ← All governance, registers, logs, reports
│   ├── OUTSTANDING_ACTION_REGISTER.md  ← Task register — update each session
│   ├── GOVERNANCE_DELTA_REPORT.md      ← WP11G delta record
│   ├── MASTER_CAPABILITY_INDEX.md      ← MASTER_CAPABILITY_INDEX is in 06_Capabilities/
│   ├── REFERENCE_MASTER.csv            ← Authoritative reference register
│   ├── CONSULTANT_INDEX.csv            ← 49 consultants indexed
│   └── ORACLE_FACT_BASELINE.md         ← Fact validation record
├── 01_Compliance/          ← COMPLIANCE_REGISTER.csv + compliance documents
├── 04_References/          ← Signed reference letters by BU
├── 06_Capabilities/        ← KB copies of approved capability statements
│   ├── MASTER_CAPABILITY_INDEX.md      ← Single entry point — all 49 assets
│   └── Oracle/Oracle_HCM/              ← Wave 3 + 4 HCM assets
├── 07_Approved_Content/    ← Extraction pipeline (Candidate → Review → Approved)
│   └── Approved/           ← ONLY source for tender content
├── 08_Commercial/          ← Assumption library + commercial framework + assembly engine
│   ├── Assumptions/        ← 13 assumption packs (all Approved v1.0)
│   ├── Assembly_Engine/    ← 35 files: 7 WP12 reference library + 6 WP17B engine components + 4 WP17D outputs + 8 WP18A/18B architecture docs + 6 WP18C.3 TIL engines (TENDER_PROFILE_STANDARD, TENDER_INTELLIGENCE_RULES, PROPOSAL_PATTERN_ENGINE, CAPABILITY_SELECTION_ENGINE, METHODOLOGY_SELECTION_ENGINE, REFERENCE_SELECTION_ENGINE) + ARM IT045 assembly outputs
│   ├── Reports/            ← WP historical reports (WP14C–WP18C.3; WP18Z_SESSION_BASELINE.md)
│   ├── TENDER_ASSUMPTION_ASSEMBLY_RULES.md
│   └── [5 WP11F framework docs]
├── 03_People/              ← Consultant Index Records (metadata only — ADR-001)
└── HANDOVER.md / AI_CONTEXT.md  ← Session entry points

Source repositories (read-only):
├── Tender Pack/                           ← Evidence, compliance, reference letters
│   └── References/0. Oracle Reference to Include in all Proposals/  ← PRIORITY source for reference letters
└── Parties/Customers/[Client]/RFP/        ← 18,400-file historical corpus
    └── 0. Proposal Templates/             ← Active proposal templates
```

---

## Current Active Work Queue

### Factory Development (AI Tasks)

| Priority | Item | Effort | Next action |
|---|---|---|---|
| **NEXT** | **WP18C.2 — Section Library Consolidation** | 2–3h | Merge S-38+S-73 for AMS in PROPOSAL_SECTION_LIBRARY.md; fix SI-007; align CONTENT_SOURCE_MATRIX.md + PROPOSAL_ASSEMBLY_SEQUENCE.md |
| P1 | **GAP-004 — OCI Capability Asset** | 4–8h | Author W4-OCI-001 standalone OCI narrative; BU review required |
| P2 | **WP18B-EXT — Risk Library Population** | 4–6h | Populate RISK_LIBRARY_STANDARD.md with Pattern 13 AMS risks (8–10 entries) |
| P3 | **WP18C.4 — AI Context Standards** | 3–4h | Define AI-GENERATE enrichment rules for S-13, S-14, S-22 using Tender Profile as context |
| P4 | **WP18D — QA Engine** | 8–12h | After automation rate confirmed >85% |

### Business Actions (Human Tasks)

| Priority | Item | Owner | Deadline |
|---|---|---|---|
| **CRITICAL** | **OAR-A01 — B-BBEE renewal** | Finance Director | 2026-07-31 |
| Blocked | **OAR-C01 — Hollywood Bets AM approval** (Plennegy) | Oracle BU Lead | Before Plennegy submission |
| Blocked | **OAR-C02 — Plennegy costing section** | Commercial Director + Bid Manager | Before Plennegy submission |
| Open | **OAR-B02 — KPMG reference letter** | Oracle BU Lead | — |
| Open | **OAR-D05 — Commercial Director decisions** (6 items: BU-RC-004/008, BU-CR-003, BU-EM-006, BU-GOV-001/003) | Commercial Director | — |
