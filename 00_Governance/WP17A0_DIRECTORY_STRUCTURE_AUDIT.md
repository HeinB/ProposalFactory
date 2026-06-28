---
document_id: WP17A0-DIRECTORY-STRUCTURE-AUDIT
title: "WP17A-0 — Tender Factory Directory Structure Audit"
version: "1.0"
status: "Complete"
created: "2026-06-19"
created_by: "WP17A-0 — Pre-Assembly Engine Audit"
category: "Governance / Audit"
scope: "Full repository structure audit before Assembly Engine build (WP17)"
---

# WP17A-0 — Tender Factory Directory Structure Audit

**Date:** 2026-06-19  
**Status:** COMPLETE — Audit Only  
**No files were moved, renamed, or modified during this audit.**

---

## 1. Executive Summary

The Tender Knowledge Base repository has grown organically across 17 work packages without a planned cleanup cycle. The core approved content (49 assets, 1,136 assumptions) is correctly placed and governed. However, the repository has accumulated significant structural drift that will impede the Assembly Engine if not addressed.

**Primary finding:** Three categories of drift require attention before WP17:

| Category | Severity | Impact |
|---|---|---|
| Duplicate files across folders | HIGH | Assembly Engine path resolution ambiguity |
| Pipeline staging area (Candidate/Review_Required) never purged | MEDIUM | Confusion between approved and draft content; bloated 07_Approved_Content |
| 00_Governance overstuffed with mixed content | MEDIUM | Findability; assembly engine components mixed with historical records |
| WP reports mixed with active governance in 08_Commercial | MEDIUM | Readability; active documents buried under 40+ historical reports |
| Empty scaffold folders throughout | LOW | Noise; misleading navigation |

**Recommendation:** Apply **light targeted cleanup** before building the Assembly Engine. Full restructuring is not necessary and carries broken-reference risk. The 5 targeted cleanups identified in Section 8 can be completed in one session without touching any active assembly or assumption content.

---

## 2. Current Directory Tree

### Top-Level Structure

```
Tender Knowledge Base/
├── .claude/                      (IDE config — 1 file)
├── 00_Governance/                (104 files — OVERSTUFFED)
├── 01_Compliance/                (3 files + empty subfolders)
├── 02_Corporate/                 (8 files in Company_Profile subdir)
├── 03_People/                    (0 files — empty scaffold)
├── 04_References/                (0 files — empty scaffold)
├── 05_Methodologies/             (1 file + many empty subfolders)
├── 06_Capabilities/              (43 files — includes 2 duplicates + 13 empty dirs)
├── 07_Approved_Content/          (121 files — pipeline not purged)
├── 08_Commercial/                (83 files — WP reports mixed with active docs)
├── 08_Historical_Tenders/        (0 files — EMPTY)
├── 09_Active_Tenders/            (6 files — Plennegy workspace)
├── 10_Incoming_Tender_Docs/      (0 files — EMPTY)
├── 11_Submitted_Tenders/         (0 files — EMPTY)
├── 12_OCR_Working/               (0 files — EMPTY)
├── 13_Quote_Generator/           (placeholder .keep files only)
├── 99_Archive/                   (0 files — EMPTY)
├── AI_CONTEXT.md                 (active — session entry point)
├── HANDOVER.md                   (active — session entry point)
└── PROJECT.md                    (stale — last updated 2026-06-12)
```

---

## 3. Folder Classification

| Folder | Purpose | Naming | Overlaps | Verdict |
|---|---|---|---|---|
| `00_Governance` | Governance, control, registers, + everything that didn't have a home | Correct | Partial overlap with 08_Commercial (assembly engine) | **Keep — but prune heavily** |
| `01_Compliance` | Compliance register + empty subfolders for documents | Correct | None | Keep — populate |
| `02_Corporate` | Company_Profile subdir with KB copies of Cross_BU approved assets | Misleading — duplicates 07_Approved_Content/Approved/Cross_BU | Duplicates 06_Capabilities and 07_Approved_Content | **Shadow copy — investigate synchronisation** |
| `03_People` | Consultant profiles (ADR-001: metadata only) | Correct | None | Keep — but Resource_Profiles subdir has no files |
| `04_References` | Signed reference letters by BU | Correct — but EMPTY | None | Keep — letters not migrated from Tender Pack |
| `05_Methodologies` | Implementation and other methodology documents | Correct | Partial overlap with 07_Approved_Content/Approved/Oracle/ (W2S1-005 in both) | Keep — only 1 file |
| `06_Capabilities` | KB working copies of approved capability statements | Correct | Intentional overlap with 07_Approved_Content/Approved/ | **Keep — fix duplicates and empty dirs** |
| `07_Approved_Content` | Three-stage extraction pipeline (Candidate → Review_Required → Approved) | Correct | Intentional overlap with 06_Capabilities | **Keep — purge stale pipeline stages** |
| `08_Commercial` | Assumption library + commercial framework + WP reports (mixed) | Correct for framework; WP reports are noise | WP reports overlap with 00_Governance (both have records) | **Keep — move WP reports to Reports/ subdir** |
| `08_Historical_Tenders` | Historical won/lost tender submissions | NAMING CONFLICT — same prefix as 08_Commercial | Future corpus for Assembly Engine | **Rename to 09_Historical_Tenders or merge with 09_Active_Tenders** |
| `09_Active_Tenders` | Active tender workspaces (Plennegy) | Correct | Number conflict with 08_Historical_Tenders | Keep |
| `10_Incoming_Tender_Docs` | Incoming tender documents for processing | Correct concept | None | Keep as scaffold |
| `11_Submitted_Tenders` | Archive of submitted tender responses | Correct | Overlaps with 11 but currently empty | Keep as scaffold |
| `12_OCR_Working` | OCR processing workspace | Correct concept | None | Keep as scaffold |
| `13_Quote_Generator` | Quote generation workspace | Correct concept | Overlaps with 08_Commercial Rate Card | Keep — but its Rate_Cards and Assumptions_Exclusions subdirs duplicate 08_Commercial content |
| `99_Archive` | Archive / superseded material | Correct | None | Keep — but empty; all archiving has happened within folders |

---

## 4. Drift Findings

### 4.1 00_Governance — Overstuffed (104 files)

`00_Governance` was designed as the governance and control register. It has become a catch-all for everything that didn't have a designated home. Content currently in 00_Governance falls into seven distinct categories:

| Category | Files | Should Live | Urgency |
|---|---|---|---|
| **Active governance registers** | OUTSTANDING_ACTION_REGISTER, ORACLE_FACT_BASELINE, REFERENCE_MASTER.csv/.md, CONSULTANT_INDEX.csv, DOCUMENT_REGISTER.csv, EXTRACTION_LOG.csv, NAMED_REFERENCE_MATRIX, GOVERNANCE_DELTA_REPORT, ADR-001 | 00_Governance ✓ | Stay |
| **Assembly Engine components** | ASSEMBLY_READINESS_MATRIX, ASSEMBLY_RULES_ENGINE, TENDER_BOM_LIBRARY, PROPOSAL_STRUCTURE_LIBRARY, DELIVERY_PATTERN_LIBRARY, PROJECT_PLAN_TEMPLATES, ESTIMATION_INPUT_MODEL | 08_Commercial/ or new Assembly_Engine/ | Move before WP17 |
| **Session historical records** | CHECKPOINT_WAVE1, CHECKPOINT_ORACLE_WAVE2, MILESTONE_2026-06-10, SESSION_A_CLOSEOUT, SESSION_B_APPROVAL_PACK/SUMMARY/STATUS, SESSION_C_APPROVAL_PACK/PLAN/SUMMARY/REVIEW/IMPACT/FACT_BASELINE | 99_Archive/ or 00_Governance/_Archive | Archive |
| **Wave planning docs** | ORACLE_WAVE2_EXECUTION_PLAN, ORACLE_WAVE2_SOURCE_MAP, WAVE1_CLOSEOUT, WAVE1_EXTRACTION_SUMMARY, WAVE1_REVIEW_PACK, WAVE2_CANDIDATE_DECISIONS, WAVE3_HCM_SOURCE_DISCOVERY, WAVE4_CLOSURE/DISCOVERY/PORTFOLIO/PROMOTION_REVIEW, POST_WAVE1_ROADMAP | 00_Governance/_Archive | Archive |
| **SVR files (Wave 3)** | SVR-W3S1-005 through SVR-W3S1-009 | 07_Approved_Content or 00_Governance/_Archive | Archive — all items resolved |
| **Capability reference** | BeBanking_CAPABILITY_MAP | 06_Capabilities/BeBanking/ | Move |
| **Stale / superseded** | CURRENT_STATE.md (v3.4, 2026-06-14 — explicitly marked stale in HANDOVER), CONTENT_GAP_ANALYSIS.md (marked unreliable since Wave 3), KNOWLEDGE_BASE_STATUS.md, APPROVED_TENDER_CONTENT.md, APPROVED_CONTENT_PLACEMENT_PLAN.md, APPROVED_CONTENT_USAGE_GUIDE.md | 99_Archive or delete | Archive/Delete |
| **Pre-extraction notes** | ORACLE_FINANCE_SOURCE_NOTES, W2S1-003_READINESS_REPORT, W2S1-005-PRE-EXTRACTION-READINESS, FUSION_EXTRACTION_NOTES, EVIDENCE_UPGRADE_PLAN | 99_Archive | Archive |
| **RAG/AI operations** | RAG_INSTRUCTIONS, TENDER_RAG_HANDOVER, ANSWER_ASSEMBLY_FRAMEWORK, AUTOMATION_READINESS_SCORECARD, UPDATED_AUTOMATION_SCORECARD, TENDER_AUTOMATION_ROADMAP, RESPONSE_ASSEMBLY_TEST | Relocate to Assembly Engine dir or archive | Evaluate |

### 4.2 07_Approved_Content — Pipeline Staging Not Purged

The three-stage pipeline was designed to move files forward (Candidate → Review_Required → Approved). Files were correctly promoted, but the earlier-stage copies were never removed after promotion. This means every approved asset exists in up to four locations simultaneously.

**Pattern:** Acumatica Financials (W1S2-001) exists in:
1. `07_Approved_Content/Candidate_Content/Acumatica/W1S2-001-ACU-Financials-DRAFT.md` (stale — promoted 2026-06-10)
2. `07_Approved_Content/Review_Required/Acumatica/W1S2-001-ACU-Financials.md` (stale — promoted 2026-06-10)
3. `07_Approved_Content/Approved/Acumatica/W1S2-001-ACU-Financials.md` (**authoritative**)
4. `06_Capabilities/Acumatica/ERP/W1S2-001-ACU-Financials.md` (KB working copy — authoritative)

This applies to all 49 approved assets. The Candidate_Content and Review_Required folders collectively hold ~70 stale files — copies of approved content at earlier pipeline stages.

**Additional pipeline drift:**
- `07_Approved_Content/Candidate_Content/Oracle/W4-HCM-004-ORA-TimeLabour-DRAFT.md` exists as a RETIRED asset — correctly noted as RETIRED in its frontmatter but still sits in the active Candidate_Content pipeline folder
- `07_Approved_Content/Candidate_Content/Oracle/W3S1-001-SVR-HCM-Core.md` — an SVR (Source Validation Report) incorrectly placed inside Candidate_Content

**Empty top-level BU folders in 07_Approved_Content:**
- `07_Approved_Content/Acumatica/` — 0 files (legacy scaffold, never used)
- `07_Approved_Content/BeBanking/` — 0 files (legacy scaffold, never used)
- `07_Approved_Content/Oracle/` — 0 files (legacy scaffold, never used)
- `07_Approved_Content/Executive_Summaries/` — 0 files (never populated)

**Misplaced approved asset:**
- `07_Approved_Content/Approved/W5-METH-001-ERP-ImplementationMethodology.md` sits in the root of `/Approved/` rather than in a BU subfolder. All other assets are in `/Approved/[BU]/`. This asset should be in `/Approved/Cross_BU/` or a new `/Approved/Cross_Platform/` subfolder consistent with MASTER_CAPABILITY_INDEX classification.

### 4.3 06_Capabilities — Duplicate Files and Misplacements

**Confirmed duplicate files:**

| File | Location 1 | Location 2 | Root Cause |
|---|---|---|---|
| `W1S2-003-ACU-Inventory.md` | `06_Capabilities/Acumatica/Distribution/` | `06_Capabilities/Acumatica/ERP/` | Inventory spans Distribution and ERP — copied to both without removing one |
| `W1S3-010-BB-MonitoringAutomation.md` | `06_Capabilities/BeBanking/Architecture/` | `06_Capabilities/BeBanking/Banking/` | Monitoring/Automation spans both — copied to both |

These are confirmed byte-for-byte duplicates. The Assembly Engine needs one canonical path per asset.

**Misplaced files:**
- `W4-ERP-001-ORA-FusionFinancials.md`, `W4-ERP-002-ORA-FusionProcurement.md`, `W4-ERP-003-ORA-PPM.md`, `W4-INT-001-ORA-OICAccelerators.md` — all placed directly in `06_Capabilities/Oracle/` root rather than in `06_Capabilities/Oracle/Oracle_ERP/` or `06_Capabilities/Oracle/Oracle_OIC/`
- `W1S1-003-ORA-OraclePartnership.md` — placed in `06_Capabilities/Oracle/Oracle_ERP/` but this is a corporate statement, not an ERP capability; should be in `06_Capabilities/Oracle/` root or a `06_Capabilities/Oracle/Partnership/` subfolder

**Empty subdirectories (13):**

| Empty Dir | Status |
|---|---|
| `06_Capabilities/Acumatica/Integration` | Planned — no asset yet |
| `06_Capabilities/Acumatica/Managed_Services` | Planned — no asset yet (W5-ACU-001 not linked here) |
| `06_Capabilities/Acumatica/Payroll` | Planned — W1S2-007 went to Payroll_Integration instead |
| `06_Capabilities/Oracle/Oracle_Database` | Planned — no DBA asset linked here (W2S1-003 went to DBA_Managed_Services) |
| `06_Capabilities/Oracle/Oracle_Security` | Planned — no asset |
| `06_Capabilities/Oracle/Oracle_OIC` | Planned — W4-INT-001 is at parent level instead |
| `06_Capabilities/Oracle/Oracle_DR` | Planned — no asset |
| `06_Capabilities/Oracle/Oracle_Managed_Services` | Planned — W2S1-004 went to DBA_Managed_Services instead |
| `06_Capabilities/Oracle/Oracle_OCI` | Planned — no OCI capability statement (only assumption pack) |
| `06_Capabilities/Oracle/Oracle_APEX` | Planned — no APEX capability statement |
| `06_Capabilities/BeBanking/Client_References` | Planned — reference letters not migrated |
| `06_Capabilities/Acumatica` (root) | Parent of populated subdirs — no root-level files needed |
| `06_Capabilities/BeBanking` (root) | Parent of populated subdirs — no root-level files needed |

### 4.4 02_Corporate — Shadow Copy of Cross_BU Approved Assets

`02_Corporate/Company_Profile/` contains 8 of the 9 Cross_BU approved assets. These are likely the **original pre-pipeline copies** that were not removed when the approved versions were placed in `07_Approved_Content/Approved/Cross_BU/`.

**W1S1-005 (BeBanking Overview) is missing from 02_Corporate/Company_Profile** — present in Cross_BU Approved but not here. This confirms desynchronisation.

**Risk:** If the copies differ, an AI session reading from `02_Corporate/Company_Profile/` would get an older version than the approved governance copy. The Assembly Engine must know which copy is authoritative.

**Authoritative location:** `07_Approved_Content/Approved/Cross_BU/` (or KB copy in `06_Capabilities/`)

### 4.5 08_Commercial — WP Reports Mixed with Active Governance

`08_Commercial/` root contains 40 files of which:
- **Active governance (keep at root):** ASSUMPTION_GOVERNANCE, ASSUMPTION_LIBRARY_ROADMAP, TENDER_ASSUMPTION_ASSEMBLY_RULES, RATE_CARD_FRAMEWORK, ESTIMATION_GUIDE, CR_PRICING_MODEL, EFFORT_MULTIPLIERS, COMMERCIAL_GOVERNANCE + 5 change logs
- **WP process reports (should be in Reports/ subdir):** WP14C, WP14D, WP14E, WP14F, WP14G, WP15A, WP15A1 (×4), WP15C, WP15D, WP15E (×4), WP15F, WP16A, WP16B (×3), WP16C, WP16D = 21 report files
- **Stale / legacy:** `ASSUMPTION_REGISTER.csv` at root level (115 rows — contains only HCM Base assumptions; superseded by pack-specific registers in subdirs; not updated since WP11)
- **Misplaced:** `HCM_BASELINE_CHANGE_LOG.md` at root (all other pack change logs are in their pack subdirs — ERP, OIC, AMS each have their change log inside the pack folder)
- **WP artifact:** `ASSUMPTION_LIBRARY_MASTER_REVIEW.xlsx` + `ASSUMPTION_LIBRARY_MASTER_REVIEW_REPORT.md` (WP14B outputs — technically archived work products)
- **Misplaced governance report:** `CONSULTANT_INDEX_PROGRAMME.md` is in `00_Governance/` which is correct, but a second consultant-related file `RESOURCE_RESPONSE_LIBRARY.md` is also in `00_Governance/` — these consultant/people documents should be in `03_People/`

### 4.6 ASSUMPTION_REGISTER.csv — Stale Top-Level File

`08_Commercial/ASSUMPTION_REGISTER.csv` (115 rows) contains only HCM Base assumptions in an older format. This predates the pack-specific registers created in WP11C-D-E-H-I-J. It is now misleading — it appears to be a master register but covers only one pack. The authoritative per-pack registers are:
- `Assumptions/OIC/OIC_ASSUMPTION_REGISTER.csv`
- `Assumptions/ERP/ERP_ASSUMPTION_REGISTER.csv`
- `Assumptions/AMS/AMS_ASSUMPTION_REGISTER.csv`
- `Assumptions/OCI/OCI_ASSUMPTION_REGISTER.csv`
- `Assumptions/Acumatica/ACU_ASSUMPTION_REGISTER.csv`
- `Assumptions/BeBanking/BEBANKING_ASSUMPTION_REGISTER.csv`

No HCM-specific register CSV was ever created (the HCM packs use only the .md files). The top-level ASSUMPTION_REGISTER.csv is an orphaned relic.

### 4.7 Governance Subfolder in Assumptions — Mixed Content

`08_Commercial/Assumptions/Governance/` contains:
- **WP13 campaign artefacts** (now historical — programme complete): GOVERNANCE_APPROVAL_ROADMAP, GOVERNANCE_WORKSHOP_PLAN, GOVERNANCE_DECISION_RECORD_TEMPLATE, GOVERNANCE_RISK_REGISTER
- **Active operational artefacts**: GOVERNANCE_DASHBOARD, GOVERNANCE_MASTER_DECISION_REGISTER, GOVERNANCE_BASELINE_CORRECTION_REPORT

With the governance programme complete (WP16C), most of these are historical. The GOVERNANCE_DASHBOARD remains useful as a summary reference.

### 4.8 Folder Numbering Conflict

`08_Historical_Tenders` has the same numeric prefix as `08_Commercial`. In the sorted directory listing they appear adjacent and confusingly named. `08_Historical_Tenders` is completely empty (0 files). It should be renumbered (e.g., `14_Historical_Tenders`) to eliminate the naming conflict.

---

## 5. Duplicate and Misplaced Files Summary

### 5.1 Files with Multiple Active Copies

| File | Active Copy Count | Authoritative Location | Stale Copies |
|---|---|---|---|
| W1S2-003-ACU-Inventory.md | 4 | `07_Approved_Content/Approved/Acumatica/` | Candidate (DRAFT), Review_Required, and BOTH `06_Capabilities/Acumatica/Distribution/` + `06_Capabilities/Acumatica/ERP/` |
| W1S3-010-BB-MonitoringAutomation.md | 4 | `07_Approved_Content/Approved/BeBanking/` | Review_Required and BOTH `06_Capabilities/BeBanking/Architecture/` + `06_Capabilities/BeBanking/Banking/` |
| W1S1-003-ORA-OraclePartnership.md | 3 | `07_Approved_Content/Approved/Cross_BU/` | `02_Corporate/Company_Profile/` and `06_Capabilities/Oracle/Oracle_ERP/` |
| W2S1-005-ORA-ImplementationMethodology.md | 2 | `07_Approved_Content/Approved/Oracle/` | `05_Methodologies/Implementation/` — OR vice versa |
| W5-METH-001-ERP-ImplementationMethodology.md | 1 active, 1 stale | `07_Approved_Content/Approved/` (root — misplaced) | — |
| W1S1-001 through W1S1-009 (Cross_BU) | 2-3 each | `07_Approved_Content/Approved/Cross_BU/` | `02_Corporate/Company_Profile/` (all 8 present there) |

### 5.2 Stale Pipeline Files (Candidate_Content and Review_Required)

All files in `Candidate_Content/` and `Review_Required/` that correspond to assets now in `Approved/` are stale. Total count:

| Folder | Files | Status |
|---|---|---|
| `Candidate_Content/_Archived_Superseded/` | 18 | Already marked archived — safe to delete |
| `Candidate_Content/Acumatica/` | 7 | DRAFT versions of approved assets — stale |
| `Candidate_Content/Cross_BU/` | 3 | DRAFT versions of approved assets — stale |
| `Candidate_Content/Oracle/` | 16 | DRAFT versions of approved assets (+ 1 SVR misfile + W4-HCM-004 RETIRED) — stale |
| `Candidate_Content/BeBanking/` | Empty | — |
| `Review_Required/Acumatica/` | 6 | Pre-approval versions — stale |
| `Review_Required/BeBanking/` | 10 | Pre-approval versions — stale |
| `Review_Required/Cross_BU/` | 6 | Pre-approval versions (confusingly still have -DRAFT suffix) — stale |
| `Review_Required/Oracle/` | 2 | Pre-approval versions — stale (W3S1-001 and W3S1-002 early versions) |
| **Total stale pipeline files** | **~68** | All have approved versions |

**Exception:** `W4-HCM-004-ORA-TimeLabour-DRAFT.md` is RETIRED (not promoted to Approved). It should go to `_Archived_Superseded/` or `99_Archive/`.

### 5.3 Files Placed in Wrong Folder

| File | Current Location | Correct Location |
|---|---|---|
| `BeBanking_CAPABILITY_MAP.md` | `00_Governance/` | `06_Capabilities/BeBanking/` |
| `W3S1-001-SVR-HCM-Core.md` | `07_Approved_Content/Candidate_Content/Oracle/` | `00_Governance/` or `00_Governance/_Archive/` |
| `W5-METH-001-ERP-ImplementationMethodology.md` | `07_Approved_Content/Approved/` (root) | `07_Approved_Content/Approved/Cross_BU/` or new `Approved/Cross_Platform/` |
| `W4-ERP-001/002/003, W4-INT-001` | `06_Capabilities/Oracle/` (root) | `06_Capabilities/Oracle/Oracle_ERP/` and `06_Capabilities/Oracle/Oracle_OIC/` |
| `W1S1-003-ORA-OraclePartnership.md` | `06_Capabilities/Oracle/Oracle_ERP/` | `06_Capabilities/Oracle/` root (it's a partnership statement, not ERP capability) |
| `HCM_BASELINE_CHANGE_LOG.md` | `08_Commercial/` root | `08_Commercial/Assumptions/HCM/` (consistent with other pack change logs) |
| `RESOURCE_RESPONSE_LIBRARY.md` | `00_Governance/` | `03_People/` or `00_Governance/` (borderline — tender response blocks relate to people/consultants) |
| All WP14-WP16 report files | `08_Commercial/` root | `08_Commercial/Reports/` (new subdir) |
| `ASSEMBLY_READINESS_MATRIX.md` | `00_Governance/` | `08_Commercial/` or new `Assembly_Engine/` |
| `ASSEMBLY_RULES_ENGINE.md` | `00_Governance/` | `08_Commercial/` or new `Assembly_Engine/` |
| `TENDER_BOM_LIBRARY.md` | `00_Governance/` | `08_Commercial/` or new `Assembly_Engine/` |
| `PROPOSAL_STRUCTURE_LIBRARY.md` | `00_Governance/` | `08_Commercial/` or new `Assembly_Engine/` |
| `DELIVERY_PATTERN_LIBRARY.md` | `00_Governance/` | `08_Commercial/` or new `Assembly_Engine/` |
| `PROJECT_PLAN_TEMPLATES.md` | `00_Governance/` | `08_Commercial/` or new `Assembly_Engine/` |
| `ESTIMATION_INPUT_MODEL.md` | `00_Governance/` | `08_Commercial/` or new `Assembly_Engine/` |

---

## 6. Recommended Target Structure

The target structure preserves all existing folder names and numbering. The key change is introducing a `Reports/` subfolder in `08_Commercial/`, an `Assembly_Engine/` subfolder (or directory) in `08_Commercial/`, and an `_Archive/` subfolder in `00_Governance/` and `07_Approved_Content/`. No numeric re-ordering of top-level folders is required except renaming `08_Historical_Tenders`.

```
Tender Knowledge Base/
│
├── AI_CONTEXT.md                     ← Session entry point (keep at root)
├── HANDOVER.md                       ← Session entry point (keep at root)
├── PROJECT.md                        ← Update or archive (currently stale)
│
├── 00_Governance/                    ← PRUNE: ~40 files move to _Archive/
│   ├── _Archive/                     ← NEW: session records, wave docs, SVRs
│   ├── Templates/                    ← Keep (content document templates)
│   ├── ADR-001-CV_SOURCE_OF_TRUTH.md
│   ├── CONSULTANT_INDEX.csv          ← Active register
│   ├── CONSULTANT_SKILL_MATRIX.md    ← Active register
│   ├── CONSULTANT_MCP_READINESS.md   ← Active
│   ├── CV_GAP_ANALYSIS.md            ← Active
│   ├── DOCUMENT_REGISTER.csv         ← Active register
│   ├── EXTRACTION_LOG.csv            ← Active register
│   ├── GOVERNANCE_DELTA_REPORT.md    ← Active
│   ├── NAMED_REFERENCE_MATRIX.md     ← Active
│   ├── ORACLE_FACT_BASELINE.md       ← Active — always load before tender use
│   ├── OUTSTANDING_ACTION_REGISTER.md ← Active — update each session
│   ├── REFERENCE_GAP_ANALYSIS.md     ← Active
│   ├── REFERENCE_MASTER.csv          ← Active register
│   ├── REFERENCE_MASTER.md           ← Active
│   ├── REFERENCE_OPPORTUNITY_REGISTER.md ← Active
│   ├── REFERENCE_REGISTRATION_REPORT.md ← Active
│   ├── RESOURCE_RESPONSE_LIBRARY.md  ← Keep (tender response blocks)
│   └── [~20 historical files → _Archive/]
│
├── 01_Compliance/
│   ├── COMPLIANCE_REGISTER.csv       ← Active register
│   ├── COMPLIANCE_LIBRARY_INDEX.md   ← Active
│   ├── COMPLIANCE_GAP_REPORT.md      ← Active
│   └── [BEE/, Tax/, etc. subdirs — populate from Tender Pack]
│
├── 02_Corporate/
│   └── Company_Profile/              ← RESOLVE: either keep as shadow copy
│                                        (and note it as non-authoritative)
│                                        or remove 8 files (authoritative = 07_Approved_Content)
│
├── 03_People/
│   └── Resource_Profiles/            ← Consultant Index Records (ADR-001)
│
├── 04_References/
│   ├── Oracle/                       ← Migrate signed letters from Tender Pack
│   ├── Acumatica/
│   ├── BeBanking/
│   └── Managed_Services/
│
├── 05_Methodologies/
│   └── Implementation/
│       └── W2S1-005-ORA-ImplementationMethodology.md (or remove — also in 07_Approved_Content)
│
├── 06_Capabilities/
│   ├── MASTER_CAPABILITY_INDEX.md    ← Active — primary assembly lookup
│   ├── Acumatica/
│   │   ├── Distribution/
│   │   ├── ERP/                      ← Remove W1S2-003 duplicate (keep in Distribution)
│   │   ├── Field_Services/
│   │   ├── Manufacturing/
│   │   ├── Payroll_Integration/
│   │   └── [Remove Integration/, Managed_Services/, Payroll/ — empty]
│   ├── BeBanking/
│   │   ├── Architecture/             ← Remove W1S3-010 duplicate (keep here)
│   │   ├── Banking/                  ← Remove W1S3-010 duplicate from here
│   │   ├── Forex/
│   │   ├── Integrations/
│   │   ├── OCI_Hosting/
│   │   ├── Payroll/
│   │   ├── Product_Overview/
│   │   ├── Security/
│   │   └── Supplier_Payments/
│   └── Oracle/
│       ├── DBA_Managed_Services/
│       ├── Oracle_EBS/
│       ├── Oracle_ERP/               ← Remove W1S1-003 (not an ERP file)
│       │   ├── W4-ERP-001            ← MOVE here from Oracle/ root
│       │   ├── W4-ERP-002            ← MOVE here
│       │   └── W4-ERP-003            ← MOVE here
│       ├── Oracle_Fusion/
│       ├── Oracle_HCM/               ← All 11 HCM assets (W3S1-001–009 + W4-HCM-002 + W4-AI-002)
│       ├── Oracle_OIC/               ← MOVE W4-INT-001 here
│       └── [Remove Oracle_Database, Oracle_DR, Oracle_Managed_Services,
│              Oracle_OCI, Oracle_APEX, Oracle_Security — all empty]
│
├── 07_Approved_Content/
│   ├── Approved/                     ← AUTHORITATIVE approved asset location
│   │   ├── Cross_BU/                 ← 9 approved assets
│   │   │   └── [MOVE W5-METH-001 out of Approved/ root to here or Cross_Platform/]
│   │   ├── Oracle/                   ← 21 approved assets
│   │   ├── Acumatica/                ← 9 approved assets
│   │   ├── BeBanking/                ← 11 approved assets
│   │   └── README.md
│   ├── Candidate_Content/
│   │   ├── _Archived_Superseded/     ← Existing archived DRAFTs (keep)
│   │   └── [All DRAFT files for approved assets → _Archived_Superseded/]
│   ├── Review_Required/
│   │   └── [All files for assets now in Approved/ → _Archived_Superseded/]
│   └── [Remove empty Acumatica/, BeBanking/, Oracle/, Executive_Summaries/ top-level dirs]
│
├── 08_Commercial/
│   ├── Assumptions/                  ← Assumption library (keep as-is)
│   │   ├── HCM/                      ← 5 assumption packs
│   │   ├── OIC/
│   │   ├── ERP/
│   │   ├── AMS/
│   │   ├── OCI/
│   │   ├── Acumatica/
│   │   ├── BeBanking/
│   │   ├── Cross_BU/                 ← Empty placeholder
│   │   └── Governance/               ← WP13 governance campaign docs (mostly historical)
│   ├── Assembly_Engine/              ← NEW: consolidate assembly engine components
│   │   ├── ASSEMBLY_READINESS_MATRIX.md  (from 00_Governance)
│   │   ├── ASSEMBLY_RULES_ENGINE.md      (from 00_Governance)
│   │   ├── TENDER_BOM_LIBRARY.md         (from 00_Governance)
│   │   ├── PROPOSAL_STRUCTURE_LIBRARY.md (from 00_Governance)
│   │   ├── DELIVERY_PATTERN_LIBRARY.md   (from 00_Governance)
│   │   ├── PROJECT_PLAN_TEMPLATES.md     (from 00_Governance)
│   │   └── ESTIMATION_INPUT_MODEL.md     (from 00_Governance)
│   ├── Reports/                      ← NEW: all WP14–WP16 process reports
│   │   └── [WP14C through WP16D — 21 files]
│   ├── ASSUMPTION_GOVERNANCE.md      ← Active
│   ├── ASSUMPTION_LIBRARY_ROADMAP.md ← Active
│   ├── TENDER_ASSUMPTION_ASSEMBLY_RULES.md ← Active
│   ├── RATE_CARD_FRAMEWORK.md        ← Active
│   ├── RATE_CARD_CHANGE_LOG.md
│   ├── ESTIMATION_GUIDE.md           ← Active
│   ├── ESTIMATION_CHANGE_LOG.md
│   ├── CR_PRICING_MODEL.md           ← Active
│   ├── CR_PRICING_CHANGE_LOG.md
│   ├── EFFORT_MULTIPLIERS.md         ← Active
│   ├── EFFORT_MULTIPLIER_CHANGE_LOG.md
│   ├── COMMERCIAL_GOVERNANCE.md      ← Active
│   ├── COMMERCIAL_GOVERNANCE_CHANGE_LOG.md
│   └── [Remove ASSUMPTION_REGISTER.csv — stale HCM-only legacy file]
│
├── 09_Active_Tenders/
│   └── Plennegy/                     ← Keep as-is
│
├── 10_Incoming_Tender_Docs/          ← Keep as scaffold
├── 11_Submitted_Tenders/             ← Keep as scaffold
├── 12_OCR_Working/                   ← Keep as scaffold
├── 13_Quote_Generator/               ← Keep scaffold; evaluate overlap with Assembly Engine
├── 14_Historical_Tenders/            ← RENAME from 08_Historical_Tenders
└── 99_Archive/                       ← Keep; populate from cleanup
```

---

## 7. Migration Plan

### Priority 1 — Fix Active Content Confusion (do before WP17)

These fixes directly affect Assembly Engine path resolution and should be done before WP17:

| Action | Files | Risk | Notes |
|---|---|---|---|
| **Remove W1S2-003 duplicate** | `06_Capabilities/Acumatica/ERP/W1S2-003-ACU-Inventory.md` | LOW | Keep in Distribution/; remove from ERP/ |
| **Remove W1S3-010 duplicate** | `06_Capabilities/BeBanking/Banking/W1S3-010-BB-MonitoringAutomation.md` | LOW | Keep in Architecture/; remove from Banking/ |
| **Move W4-ERP-001/002/003** | From `06_Capabilities/Oracle/` to `06_Capabilities/Oracle/Oracle_ERP/` | MEDIUM | Update MASTER_CAPABILITY_INDEX.md paths |
| **Move W4-INT-001** | From `06_Capabilities/Oracle/` to `06_Capabilities/Oracle/Oracle_OIC/` | MEDIUM | Update MASTER_CAPABILITY_INDEX.md paths |
| **Move W5-METH-001** | From `07_Approved_Content/Approved/` root to `07_Approved_Content/Approved/Cross_BU/` | LOW | Update MASTER_CAPABILITY_INDEX.md |
| **Create `08_Commercial/Reports/`** | Move all WP14C–WP16D files (21 files) | LOW | No active references point to report files |
| **Create `08_Commercial/Assembly_Engine/`** | Move 7 assembly engine files from `00_Governance/` | MEDIUM | Update AI_CONTEXT.md and HANDOVER.md references |

### Priority 2 — Purge Stale Pipeline (safe to do; improves clarity)

| Action | Files | Risk | Notes |
|---|---|---|---|
| **Move all `Candidate_Content/[BU]/` DRAFT files to `_Archived_Superseded/`** | ~26 DRAFT files | LOW | Approved versions exist; pipeline purpose served |
| **Move all `Review_Required/` files to `_Archived_Superseded/`** | ~24 files | LOW | All have been promoted to Approved/ |
| **Move `W4-HCM-004-ORA-TimeLabour-DRAFT.md` to `_Archived_Superseded/`** | 1 file | LOW | Marked RETIRED in frontmatter |
| **Move `W3S1-001-SVR-HCM-Core.md`** | 1 file | LOW | Misplaced SVR; move to `00_Governance/_Archive/` |

### Priority 3 — Archive Historical Records in 00_Governance (low urgency)

| Action | Files | Risk | Notes |
|---|---|---|---|
| **Create `00_Governance/_Archive/`** and move session records | ~40 files | LOW | CHECKPOINT, SESSION_X, WAVE_X, SVR, pre-extraction notes |
| **Move BeBanking_CAPABILITY_MAP.md** to `06_Capabilities/BeBanking/` | 1 file | LOW | Update any references |
| **Archive CURRENT_STATE.md** | 1 file | LOW | Explicitly marked stale in HANDOVER.md |

### Priority 4 — Resolve 02_Corporate Shadow Copy

| Action | Options | Risk | Notes |
|---|---|---|---|
| **02_Corporate/Company_Profile** — keep or remove duplicates | Option A: Delete 8 files (keep only in 07_Approved_Content + 06_Capabilities); Option B: Add README noting non-authoritative status | LOW | Option B safer — 02_Corporate may be used by other tools |

### Do Not Touch (Priority 5 — leave for now)

- Empty scaffold folders (`10_Incoming_Tender_Docs`, `11_Submitted_Tenders`, `12_OCR_Working`, `99_Archive`) — exist by design for future use
- `08_Historical_Tenders` — renaming carries low risk but is cosmetic only
- `13_Quote_Generator` — populated with `.keep` files only; evaluate overlap with Assembly Engine during WP17 planning
- `03_People/Resource_Profiles/` — empty by design (ADR-001: consultant records not stored in KB)
- `04_References/` subfolders — empty by design; letters not yet migrated from Tender Pack

---

## 8. Files Not To Touch

The following files must not be moved, renamed, or modified during any cleanup:

| File / Path | Reason |
|---|---|
| `AI_CONTEXT.md` | Session entry point; referenced by HANDOVER.md |
| `HANDOVER.md` | Session entry point; authoritative state |
| `PROJECT.md` | May be referenced externally — update separately |
| All `07_Approved_Content/Approved/[BU]/` files | Authoritative approved content |
| All `06_Capabilities/MASTER_CAPABILITY_INDEX.md` | Primary assembly lookup — update paths carefully if other moves are made |
| All `08_Commercial/Assumptions/[Pack]/[Pack]_ASSUMPTIONS_V1.md` | All 13 approved assumption packs |
| All `08_Commercial/Assumptions/[Pack]/[Pack]_ASSUMPTION_REGISTER.csv` | All 6 active pack registers |
| `08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md` | Active assembly governance |
| `08_Commercial/ASSUMPTION_GOVERNANCE.md` | Active governance |
| `00_Governance/OUTSTANDING_ACTION_REGISTER.md` | Active task register |
| `00_Governance/ORACLE_FACT_BASELINE.md` | Active fact validation |
| `00_Governance/REFERENCE_MASTER.csv` | Active reference register |
| `00_Governance/CONSULTANT_INDEX.csv` | Active consultant register |
| `09_Active_Tenders/Plennegy/PLENNEGY_DRAFT_RESPONSE.docx` | Active tender document |
| All `08_Commercial/[Commercial Framework 5 docs]` | Active commercial governance |

---

## 9. Risk Assessment

### Risks if Restructuring is Done Now

| Risk | Severity | Mitigation |
|---|---|---|
| **Broken paths in MASTER_CAPABILITY_INDEX.md** | HIGH — if W4 ERP/OIC files are moved without updating index | Update MASTER_CAPABILITY_INDEX.md paths as part of the same migration step |
| **AI session reads from stale 02_Corporate/Company_Profile** | MEDIUM — copies may differ from approved versions | Add README to Company_Profile noting `07_Approved_Content/Approved/Cross_BU/` is authoritative; or remove copies |
| **Assembly Engine (WP17) references files at old paths** | MEDIUM — if Assembly Engine is built before reorganisation | Do Priority 1 moves BEFORE WP17 begins |
| **AI_CONTEXT.md references `00_Governance/` paths for assembly files** | LOW — current references are file names not paths; check for any absolute path references | Review AI_CONTEXT/HANDOVER after Priority 1 moves |
| **Duplicate W1S2-003 causing wrong file selected** | HIGH NOW — Assembly Engine would have ambiguous path resolution | Fix before WP17 (Priority 1) |
| **WP13 campaign docs in Assumptions/Governance/ confusing active governance** | LOW — programme complete; documents clearly named | Low urgency; archive after confirming GOVERNANCE_DASHBOARD.md is the only actively referenced file |

### Risks if Restructuring is NOT Done

| Risk | Severity |
|---|---|
| Assembly Engine resolves ambiguous paths for W1S2-003 and W1S3-010 (two copies each) | HIGH |
| Assembly Engine looks in wrong folder for W4-ERP and W4-INT-001 (loose at Oracle/ root) | HIGH |
| AI sessions reading from wrong Cross_BU copy (02_Corporate vs 07_Approved_Content) | MEDIUM |
| 00_Governance remains too large to navigate efficiently | MEDIUM |
| Report files buried active governance documents | LOW |

---

## 10. Final Recommendation

**Verdict: Apply light targeted cleanup before proceeding to WP17 (Assembly Engine).**

Do NOT attempt full restructuring now. Full restructuring carries unnecessary risk and the repository's core content is correctly governed. The light cleanup (Priority 1 from Section 7) addresses the two issues that will directly break the Assembly Engine:

1. Duplicate KB files (W1S2-003, W1S3-010) — ambiguous path resolution
2. Misplaced ERP/OIC capability files at `06_Capabilities/Oracle/` root — incorrect paths

**Proposed next work package: WP17A — Light Cleanup**

Scope:
- Fix 2 duplicates in 06_Capabilities
- Move 4 ERP/OIC files to correct Oracle subfolders
- Move W5-METH-001 to Approved/Cross_BU/
- Create `08_Commercial/Reports/` and move 21 WP reports
- Create `08_Commercial/Assembly_Engine/` and move 7 assembly engine files from 00_Governance
- Add non-authoritative notice to `02_Corporate/Company_Profile/`
- Update MASTER_CAPABILITY_INDEX.md for any path changes made

**Then proceed to WP17B — Assembly Engine Build.**

Priority 2 (purge pipeline staging), Priority 3 (archive 00_Governance historical records), and Priority 4 (02_Corporate resolution) can be deferred to a separate cleanup sprint or done alongside WP17 without blocking it.

---

### Numeric Scorecard

| Metric | Value |
|---|---|
| Total top-level folders | 16 |
| Empty top-level folders (0 files) | 4 (`08_Historical_Tenders`, `10_Incoming_Tender`, `11_Submitted`, `12_OCR`) |
| Total files in repository | **373** |
| Active approved assets | 49 |
| Active assumption pack files | 46 (13 packs + registers + supporting docs) |
| Confirmed duplicate files (same asset, multiple active locations) | 2 (W1S2-003, W1S3-010) |
| Stale pipeline files (should be archived) | ~68 |
| Misplaced files (wrong folder) | ~15 |
| WP reports mixed into active governance dirs | 21 |
| Assembly engine files in wrong folder | 7 |
| Empty subdirectories across repository | ~30 |
| Files requiring no action | ~170 |

---

*WP17A-0 — Directory Structure Audit v1.0 | 2026-06-19 | Audit only — no files modified*  
*Recommendation: Light targeted cleanup (WP17A) then Assembly Engine build (WP17B)*
