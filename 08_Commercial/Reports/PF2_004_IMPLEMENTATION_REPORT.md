---
document_id: PF2-004-IMPLEMENTATION-REPORT-V1
title: "PF2-004 — Markdown Proposal Renderer — Implementation Report"
version: "1.0"
status: "COMPLETE"
created: "2026-06-29"
created_by: "PF2-004 — Markdown Proposal Renderer"
approved_by: "PF2-004"
approved_date: "2026-06-29"
approved_for_reuse: true
category: "Work Package Report"
scope: "Documents the design, implementation, and verification of the Markdown Proposal Renderer — the final assembly engine in the APPSolve Proposal Factory."
---

# PF2-004 — Markdown Proposal Renderer — Implementation Report

**Work Package:** PF2-004  
**Date:** 2026-06-29  
**Status:** COMPLETE  
**Platform Maturity:** L5.4 → **L5.5**

---

## 1. Objective

Build the Markdown Proposal Renderer — the final assembly engine in the Proposal Factory. Consume the certified Proposal Section Manifest (PSAE output) and governed source assets (.md files) to generate:

1. A complete, ordered, governance-clean Markdown proposal for every tender
2. A full per-section render audit with traceability back to source assets

**Success criteria:**
- Deterministic rendering: same manifest + same assets → same output every run
- No AI-authored proposal content (AI markers flag where drafting is needed)
- All governed content assembled from approved assets only
- Internal KB metadata stripped from rendered output
- Full traceability in audit report
- ARM-IT045 full render complete; 5 regression smoke tests PASS

---

## 2. Pre-Conditions Confirmed at PF2-004 Start

| Pre-condition | Status |
|---|---|
| Platform Maturity | L5.4 |
| PSAE operational | proposal_section_engine.py v1.0; 22/22 tests; 6 regression manifests |
| Section Manifest Standard | SECTION_MANIFEST_STANDARD.md v1.0 |
| 49 CAP assets present | 07_Approved_Content/Approved/**/*.md — 50 files confirmed |
| Canonical asset ID naming | File stems exactly match ARE canonical IDs |
| ARM-IT045 manifest | PROPOSAL_SECTION_MANIFEST_ARM-IT045.yaml — PASS; M=43, O=2 |
| 5 regression manifests | All present in 08_Commercial/Proposals/ |

---

## 3. Architecture Decision

**Why a separate renderer from PSAE?**

PSAE's output is the certified Section Manifest — a governance document specifying *what* to assemble and *how*. The renderer's job is to *execute* that specification against the governed content. Separating them ensures:

- PSAE governs the assembly plan; it never touches content files
- The renderer executes the plan; it never modifies the registry or manifest
- The rendered proposal is fully traceable back through manifest → PSAE → ARE → registry
- Governance checks (content stripping, heading demotion) are localised to the renderer

**Content pipeline design:**
The renderer strips internal KB metadata (frontmatter, approval banners, review notes, pre-tender checklists, extraction documentation) from source assets before inclusion. This ensures the proposal contains only external-facing content, not KB governance documentation.

---

## 4. Implementation

### 4.1 proposal_renderer.py

**Location:** `08_Commercial/Assembly_Engine/proposal_renderer.py`  
**Version:** v1.0  
**Dependencies:** PyYAML (stdlib otherwise)  
**CLI:** `--tender TENDER_ID`, `--regression`, `--all`

**Key components:**

| Component | Description |
|---|---|
| `AssetIndex` | Scans `07_Approved_Content/Approved/`; dual-indexes canonical + short IDs |
| `strip_frontmatter()` | Strips YAML frontmatter, approval banners, and trailing internal sections |
| `demote_headings()` | Demotes all ATX headings by 2 levels for correct document hierarchy |
| `load_asset_body()` | Composes strip + demote pipeline for any approved asset |
| `render_section()` | Dispatches to method-specific renderer; builds audit entry |
| `_render_direct()` | Loads primary source asset; inserts cleaned body |
| `_render_merge()` | Loads all source assets in order; concatenates cleaned bodies |
| `_render_extract()` | Loads primary; inserts full body + audit note |
| `_render_template()` | Generates structured template with `{{placeholder}}` markers |
| `_render_ai_generate()` | Inserts AI-DRAFT marker + human action callout |
| `_render_placeholder()` | Inserts PLACEHOLDER marker + human action callout |
| `build_toc()` | Generates TOC bullet list from assembly sequence |
| `build_audit_report()` | Generates full 6-section render audit Markdown |
| `render_proposal()` | Main orchestration: load manifest → render → write outputs |
| `run_smoke_test()` | 5 structural checks on every render result |
| `run_regression()` | Runs ARM-IT045 full + 5 smoke tests; produces results table |

### 4.2 Asset Index Statistics

| Metric | Value |
|---|---|
| Files indexed | 50 (49 CAP + 1 Cross-BU methodology) |
| IDs indexed | 99 (50 canonical + 49 short prefix) |
| Content root | `07_Approved_Content/Approved/` |
| Platforms | Cross_BU, Oracle, Acumatica, BeBanking |

### 4.3 Internal Section Stripping

The following markers are detected and stripped from asset bodies:

| Marker | Mode | Files affected |
|---|---|---|
| `**Pre-tender ...` | startswith | W2S1-002, W2S1-003, W2S1-004, most Oracle assets |
| `**Review notes:` | startswith | W1S1-001, W1S1-002, Cross_BU assets |
| `## Approval Record` | startswith | W2S1-002, W2S1-004 |
| `**File location:` | startswith | W2S1-003 |
| `Internal — Not for Tender Use` | contains | W2S1-002 Section 13 |
| `Extraction Documentation (Internal` | contains | W2S1-002 Section 13 |

### 4.4 Heading Demotion

All ATX headings demoted by 2 levels:

```
Source: # Oracle E-Business Suite Capability Statement
Output: ### Oracle E-Business Suite Capability Statement

Source: ## Our Oracle EBS Practice
Output: #### Our Oracle EBS Practice
```

This positions body sub-headings correctly under `## N. Section Name` without hierarchy collisions.

---

## 5. Regression Results — 6/6 PASS

| Scenario | Platform | Type | Rendered | Placeholder | AI-Draft | Not Found | Status |
|---|---|---|---|---|---|---|---|
| ARM-IT045 | Oracle EBS | AMS | 16 | 17 | 3 | 9 | PASS |
| REG-HCM-P3-MINING | Oracle HCM Cloud | Implementation | 18 | 18 | 3 | 3 | PASS |
| REG-OIC-P7 | Oracle Integration Cloud | Implementation | 17 | 18 | 3 | 3 | PASS |
| REG-ERP-P7-FULLSUITE | Oracle ERP Cloud | Implementation | 17 | 18 | 4 | 4 | PASS |
| REG-ACU-P11 | Acumatica | Implementation | 20 | 18 | 3 | 3 | PASS |
| REG-BEB-P12 | BeBanking | Implementation | 16 | 18 | 3 | 3 | PASS |

**ARM-IT045 NOT_FOUND analysis (9 sections):**
All 9 NOT_FOUND entries are ASP assumption pack IDs (`OIC-ASSUMPTIONS-V1`, `AMS-ASSUMPTIONS-V1`) that are not yet materialised as `.md` files in the Approved Content directory. This is a known gap (ASP content materialisation) documented in PSAE Known Gaps. The renderer correctly produces a NOT_FOUND marker with human action callout for these sections.

**Smoke test checks (per scenario):**
1. At least one section rendered (not all-placeholder)
2. S-01 Cover Page renders as RENDERED (TEMPLATE)
3. S-02 Table of Contents renders as RENDERED
4. No sections in assembly sequence with empty render_status
5. Both output files created on disk

---

## 6. ARM-IT045 Full Render Summary

**Output:** `08_Commercial/Proposals/ARM-IT045/PROPOSAL_RENDERED_ARM-IT045.md`  
**Lines:** 3,537  
**Audit:** `08_Commercial/Proposals/ARM-IT045/PROPOSAL_RENDER_AUDIT_ARM-IT045.md` (261 lines)

| Category | Count | Notes |
|---|---|---|
| RENDERED | 16 | Populated from governed assets: corporate, Oracle EBS, DBA, OIC, Managed Services, Oracle Partnership, awards, delivery model, geographic, key differentiators |
| PLACEHOLDER | 17 | Sections awaiting human content: scope inclusions/exclusions, deliverables, dependencies, project governance, pricing, compliance docs, references |
| AI-DRAFT | 3 | Executive Summary (S-13), Understanding of Requirements (S-14), Risk Register (S-50) |
| NOT_FOUND | 9 | ASP packs OIC-ASSUMPTIONS-V1 and AMS-ASSUMPTIONS-V1 (6 AMS sections + 3 commercial/assumption sections) |
| SKIPPED | 37 | Excluded or DEFAULT_EXCLUDED sections (AMS exclusions, platform-specific exclusions) |

**Governance flags applied:**
- B-BBEE expiry 2026-07-31 — displayed prominently in document header
- ADR-001 CVs from APPTime only
- GOV-EBS-001 EBS vintage content warning

---

## 7. Rendered Output Files

| Tender | Rendered Proposal | Audit |
|---|---|---|
| ARM-IT045 | `08_Commercial/Proposals/ARM-IT045/PROPOSAL_RENDERED_ARM-IT045.md` | `PROPOSAL_RENDER_AUDIT_ARM-IT045.md` |
| REG-HCM-P3-MINING | `08_Commercial/Proposals/REG-HCM-P3-MINING/PROPOSAL_RENDERED_REG-HCM-P3-MINING.md` | `PROPOSAL_RENDER_AUDIT_REG-HCM-P3-MINING.md` |
| REG-OIC-P7 | `08_Commercial/Proposals/REG-OIC-P7/PROPOSAL_RENDERED_REG-OIC-P7.md` | `PROPOSAL_RENDER_AUDIT_REG-OIC-P7.md` |
| REG-ERP-P7-FULLSUITE | `08_Commercial/Proposals/REG-ERP-P7-FULLSUITE/PROPOSAL_RENDERED_REG-ERP-P7-FULLSUITE.md` | `PROPOSAL_RENDER_AUDIT_REG-ERP-P7-FULLSUITE.md` |
| REG-ACU-P11 | `08_Commercial/Proposals/REG-ACU-P11/PROPOSAL_RENDERED_REG-ACU-P11.md` | `PROPOSAL_RENDER_AUDIT_REG-ACU-P11.md` |
| REG-BEB-P12 | `08_Commercial/Proposals/REG-BEB-P12/PROPOSAL_RENDERED_REG-BEB-P12.md` | `PROPOSAL_RENDER_AUDIT_REG-BEB-P12.md` |

---

## 8. Platform Maturity Declaration

| Dimension | Before PF2-004 | After PF2-004 |
|---|---|---|
| Proposal assembly | Section manifest only; no physical document | **First complete Markdown proposal assembled** |
| Content sourcing | Manual; copy-paste from approved assets | **Automated from AssetIndex; frontmatter stripped** |
| Heading hierarchy | Manual | **Enforced: body headings demoted 2 levels** |
| Internal content | Included accidentally | **Stripped: 6 internal marker patterns** |
| Governance flags | Manual review | **Automated: flags visible in document header** |
| Audit trail | None | **Full per-section audit: 82 rows + 6 registers** |
| Renderer engine | Not implemented | **proposal_renderer.py v1.0 operational** |
| Regression | — | **6 scenarios PASS; ARM-IT045 full render complete** |
| Platform maturity | L5.4 | **L5.5** |

---

## 9. Deliverables

| Deliverable | Location | Status |
|---|---|---|
| proposal_renderer.py v1.0 | 08_Commercial/Assembly_Engine/ | COMPLETE |
| PROPOSAL_RENDERER.md | 08_Commercial/Assembly_Engine/ | COMPLETE |
| PROPOSAL_RENDER_STANDARD.md | 08_Commercial/Assembly_Engine/ | COMPLETE |
| PROPOSAL_RENDER_AUDIT_STANDARD.md | 08_Commercial/Assembly_Engine/ | COMPLETE |
| PROPOSAL_RENDERED_ARM-IT045.md | 08_Commercial/Proposals/ARM-IT045/ | COMPLETE |
| PROPOSAL_RENDER_AUDIT_ARM-IT045.md | 08_Commercial/Proposals/ARM-IT045/ | COMPLETE |
| PROPOSAL_RENDERED + AUDIT (5 regression) | 08_Commercial/Proposals/[TENDER]/ | COMPLETE |
| PF2_004_IMPLEMENTATION_REPORT.md | 08_Commercial/Reports/ | COMPLETE |

---

## 10. Known Gaps and Next Steps

| Item | Description | Priority |
|---|---|---|
| ASP pack materialisation | OIC-ASSUMPTIONS-V1, AMS-ASSUMPTIONS-V1 must be written as .md files | High |
| EXTRACT sub-section automation | S-30/S-31/S-33/S-36 extract full body; sub-section tagging not automated | Medium |
| RSE integration | Risk selections from rse.py not yet driving S-37/S-50 content | Medium |
| S-37 RAID content | Risk Library (40 risks) defined in WP18B; Risk Register assembly from RSE output pending | Medium |
| Word/PDF export | Proposal Renderer produces Markdown; Word/PDF conversion not implemented | Low |
| Compliance document assembly | S-55–S-60 require actual compliance document files (CIPC, tax, B-BBEE, etc.) | High |

---

## 11. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-29 | PF2-004 | Initial implementation report |
