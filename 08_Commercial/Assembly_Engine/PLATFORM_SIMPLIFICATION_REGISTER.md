---
document_id: PLATFORM-SIMPLIFICATION-REGISTER-V1
title: "Proposal Factory Platform Simplification Register"
version: "1.0"
status: "Approved — Architecture Freeze"
created: "2026-06-27"
created_by: "WP18F — Platform Integration Review & Architecture Freeze"
approved_by: "WP18F"
approved_date: "2026-06-27"
work_package: "WP18F"
category: "Architecture / Simplification"
scope: "Registers realistic simplification opportunities identified during the WP18F architecture review. Each entry is evidence-based, scoped to a specific complexity, and assessed for effort, risk, and benefit. Entries that would require architectural redesign are excluded. The register is actionable, not aspirational."
---

# Proposal Factory Platform Simplification Register

**Date:** 2026-06-27 | **Version:** 1.0 | **Status:** Approved — Architecture Freeze  
**Work Package:** WP18F — Platform Integration Review & Architecture Freeze

---

## 1. Scope and Principles

This register captures simplification opportunities — changes that reduce complexity, remove duplication, or resolve inconsistency — without architectural redesign. Each entry must meet all three criteria:

1. **Evidence-based:** The complexity identified has a specific document and line reference
2. **Proportionate:** The simplification benefit justifies the change effort
3. **Low disruption:** The change does not affect the core architecture or require re-certification of stable components

Entries that would require redesigning the pipeline, changing the governance standard structure, or re-implementing core engines are NOT included. This register is about targeted cleanup, not transformation.

**Priority levels:**
- **P1 — Before KVE Phase A:** Must resolve before KVE implementation begins
- **P2 — Before KRPE Phase B:** Must resolve before Phase B extraction begins
- **P3 — Opportunistic:** Resolve when touching the relevant document for another reason
- **P4 — Deferred:** Complexity is real but cost/benefit does not justify near-term action

---

## 2. Simplification Register

### SIMP-001 — BU Permitted Values Inconsistency

**Priority:** P1 — Before KVE Phase A  
**Type:** Documentation inconsistency  
**Status:** ✅ **RESOLVED — WP18G 2026-06-27**

**Resolution:**  
KNOWLEDGE_METADATA_STANDARD.md v1.0 → v1.1: Section 2.2 `owner_business_unit` enum updated from the granular 10-value list to the 4 canonical KRPE values: `Corporate / Oracle / Acumatica / BeBanking`. Note added: "KRPE normalises all BU representations to these four canonical values at extraction time." Registry Build 5 confirms all 62 CAP+ASP entries use these 4 values (Corporate: 7, Oracle: 32, Acumatica: 11, BeBanking: 12).

**KVE unblocked:** VR-BU01 can now validate against the 4-value canonical list without false positives.

---

### SIMP-002 — Lifecycle Status Field Population Gap

**Priority:** P1 — Before KVE Phase A  
**Type:** Implementation gap with structural consequence  
**Status:** ✅ **RESOLVED — WP18G 2026-06-27**

**Resolution (Option 1 — direct field population):**  
`lifecycle_status: APPROVED` added to frontmatter of all 49 CAP files (in `07_Approved_Content/Approved/`) and all 13 ASP files (in `08_Commercial/Assumptions/`). OCI_ASSUMPTIONS_V1.md also received `approved_for_reuse: true` (was absent). KRPE Build 5 regenerated: 62/62 registry entries now carry `lifecycle_status: APPROVED`. 0 errors. Pre-existing 21 warnings unchanged (TD-IMP-001/002/003/004 — not in scope of SIMP-002).

**KVE unblocked:** VR-L01 (`lifecycle_status = APPROVED`) will pass for all 62 CAP+ASP entries without false positives.

---

### SIMP-003 — Pipeline View Cross-Reference Missing

**Priority:** P3 — Opportunistic  
**Type:** Documentation gap

**Current complexity:**  
Three documents describe the pipeline at different levels of detail:
- PROPOSAL_FACTORY_ARCHITECTURE.md: 11 stages (Stage 0 through Stage 10)
- PROPOSAL_ASSEMBLY_SEQUENCE.md: 19 assembly steps (within Stages 4–8)
- TENDER_INTELLIGENCE_RULES.md: 10-step TIL process (within Stage 0)

No document contains a cross-reference table showing how these three views relate. A reader following PFA alone would not know which PAS steps correspond to which PFA stage. A reader following TIL alone would not know which TIL step triggers Stage 3.

**Proposed simplification:**  
Add a "Pipeline View Cross-Reference" table to PROPOSAL_FACTORY_ARCHITECTURE.md Section 3 (as a new sub-section 3.x). The table maps PFA stages to PAS steps and TIL steps where applicable. Content of the cross-reference table is documented in PLATFORM_ARCHITECTURE_REVIEW.md Section 6.

**Effort:** 30 minutes (one document edit)  
**Risk:** None — this is documentation only  
**Benefit:** Any implementation engineer reading PFA will immediately understand the full pipeline structure without cross-referencing three documents  
**Recommendation:** **Resolve when PFA v1.3 is authored (triggered by KVE Phase A or similar)**

---

### SIMP-004 — KVE Missing from PFA Pipeline

**Priority:** P3 — Opportunistic (same as SIMP-003)  
**Type:** Documentation omission

**Current complexity:**  
PROPOSAL_FACTORY_ARCHITECTURE.md v1.2 does not show KVE in its pipeline component table or stage descriptions. KVE is described as operating at Stage 0 (TIL-08 triggers Mode 2) and producing the Assembly Manifest consumed by Stages 4–10. A reader following only PFA would not know KVE exists or where it operates.

**Proposed simplification:**  
Update PFA Section 3 pipeline table to add Stage 7 (KVE Validation) between Stage 6 (Methodology Selection) and Stage 8 (Proposal Assembly). Update the component status table to include KVE. Update PFA to version 1.3.

**Note:** This change was identified as AF-005 in PLATFORM_ARCHITECTURE_REVIEW.md. Resolve in the same PFA v1.3 update as SIMP-003.

**Effort:** 20 minutes (combined with SIMP-003)  
**Risk:** None — documentation only  
**Benefit:** PFA accurately reflects the platform architecture  
**Recommendation:** **Resolve in PFA v1.3 alongside SIMP-003**

---

### SIMP-005 — Three Packs Missing `assumption_count` Field

**Priority:** P2 — Before KRPE Phase B  
**Type:** Data quality gap

**Current complexity:**  
Three packs (HCM-LEARNING, HCM-TALENT, EBS-DRM) are missing the `assumption_count` field in their frontmatter (OBS-006 from certification). KRPE's pack count reconciliation (VR-P01 in KVE) checks declared count against actual count. If count is missing, KVE cannot validate pack completeness for these three packs.

**Proposed simplification:**  
Add `assumption_count:` to the frontmatter of three pack files:
- HCM-LEARNING pack: `assumption_count: 37`
- HCM-TALENT pack: `assumption_count: 31`
- EBS-DRM pack: `assumption_count: 62`

Values are known from registry Build 4 statistics.

**Effort:** 10 minutes  
**Risk:** None — metadata only  
**Benefit:** KVE VR-P01 can validate all 13 packs; eliminates 3 residual TD items (TD-IMP-003/004)  
**Recommendation:** **Resolve in first BU Lead session touching assumption packs**

---

### SIMP-006 — W2S1-004 Missing Source File

**Priority:** P2 — Before KRPE Phase B  
**Type:** Repository gap

**Current complexity:**  
W2S1-004 (Oracle Managed Services capability asset) was registered in MASTER_CAPABILITY_INDEX.md but the source Markdown file is absent from the repository (OBS-001, TD-IMP-001). KRPE registered the asset from index metadata only. The registered asset has minimal field population. S-21 (Oracle Managed Services section) lists CAP: W2S1-004 as its primary source.

**Proposed simplification:**  
Locate or recreate the W2S1-004 capability asset file and place it in `07_Approved_Content/Approved/`. If recreated, it must go through the standard approval process before the registry is regenerated.

**Effort:** 2–4 hours (locate file in backup or email archive) or 1 day (recreate from AMS assumption pack language)  
**Risk:** Low — the asset is already registered; recreation just adds content  
**Benefit:** S-21 can be assembled at DIRECT method instead of PLACEHOLDER; eliminates TD-IMP-001  
**Recommendation:** **Assign to BU Lead as a P2 task; resolve before KRPE Phase B**

---

### SIMP-007 — MASTER_CAPABILITY_INDEX Wave 3/4 ID Mismatches

**Priority:** P4 — Deferred  
**Type:** Data quality gap (non-blocking)

**Current complexity:**  
19 Wave 3/4 CAP assets have ID_MISMATCH warnings in KRPE builds (OBS-002, TD-IMP-002). The MASTER_CAPABILITY_INDEX.md uses short IDs for these assets (e.g., "W3S1-001") while the file frontmatter uses more descriptive document_ids (e.g., "W3S1-001-HCM-PAYROLL-CAPABILITY"). KRPE logs these as warnings but registers the assets correctly using the file's own ID.

**Proposed simplification:**  
Update MASTER_CAPABILITY_INDEX.md to use the full `document_id` values from the Wave 3/4 file frontmatter. This would eliminate the 19 ID_MISMATCH warnings and ensure the index is the canonical identifier source.

**Effort:** 1–2 hours (index update)  
**Risk:** Low — no impact on registry output (KRPE already uses the file's own ID)  
**Benefit:** Eliminates 19 KRPE build warnings; cleaner build reports; easier future audits  
**Recommendation:** **Defer — resolve when MASTER_CAPABILITY_INDEX.md is being updated for another purpose**

---

### SIMP-008 — Sub-Section Exclusion Rules in CSM

**Priority:** P4 — Deferred  
**Type:** Governance pattern inconsistency

**Current complexity:**  
CONTENT_SOURCE_MATRIX.md Section 4 contains sub-section exclusion rules for specific capability assets (e.g., "W3S1-008 Section 14.2 excluded"; "W3S1-009 Section 13.2 excluded"). These rules are evidence-based — they reflect approved governance decisions about which parts of those assets cannot be included in proposals. However, they are stored in the CSM rather than in the capability asset's own frontmatter. If W3S1-008 is updated and Section 14.2 is renumbered, the CSM rule becomes stale without any alert.

**Proposed simplification:**  
Add a `content_exclusions` list to the frontmatter of the relevant capability assets (W3S1-008, W3S1-009). The CSM entry references the asset; the asset governs its own exclusions. KRPE Phase B would extract content_exclusions into the registry.

**Effort:** 30 minutes (frontmatter addition); requires KRPE Phase B schema support  
**Risk:** Low — documentation governance improvement only; CSM still references the assets  
**Benefit:** Exclusion rules are maintained with the asset they govern; eliminates stale-rule risk  
**Recommendation:** **Defer to KRPE Phase B scope when asset-level content_exclusions extraction is implemented**

---

### SIMP-009 — CON/COM Type Reservations Cleanup

**Priority:** P4 — Deferred  
**Type:** Governance standard simplification

**Current complexity:**  
KNOWLEDGE_ASSET_STANDARD.md defines 10 asset types. CON (Consultant Records) and COM (Compliance Records) are included as full asset types with their own ID formats, governance rules, and metadata schemas. Neither type has any KB content: CON lives in APPTime (ADR-001) and COM is a CSV registry. The Universal Standard creates governance expectations (lifecycle, relationship graph, KRPE extraction) for types that will never have KB content.

**Proposed simplification:**  
Update KNOWLEDGE_ASSET_STANDARD.md to reclassify CON and COM as "external reference types" — retaining their ID formats for cross-referencing but explicitly exempting them from lifecycle governance, KRPE extraction, and KVE validation. Add a note to KNOWLEDGE_GOVERNANCE_RULES.md that GR-C01 through GR-AU05 do not apply to external reference types.

**Effort:** 1 hour (two document updates)  
**Risk:** Low — no impact on working platform; only affects how the standard describes these types  
**Benefit:** Eliminates confusion for any future contributor reading the Universal Standard and wondering why there are no CON/COM assets  
**Recommendation:** **Defer to WP18B-EXT rules update WP; combine with ADR-010 resolution**

---

## 3. Summary Table

| ID | Description | Priority | Effort | Recommendation |
|---|---|---|---|---|
| SIMP-001 | BU permitted values inconsistency in KMS | P1 | 15 min | **Resolve immediately** |
| SIMP-002 | lifecycle_status field not populated in CAPs | P1 | 2–3h (Option 1) | **Resolve before KVE Phase A** |
| SIMP-003 | Pipeline view cross-reference missing from PFA | P3 | 30 min | Resolve in PFA v1.3 |
| SIMP-004 | KVE missing from PFA pipeline | P3 | 20 min | Resolve in PFA v1.3 (same session as SIMP-003) |
| SIMP-005 | 3 packs missing assumption_count field | P2 | 10 min | Resolve in first BU Lead pack session |
| SIMP-006 | W2S1-004 source file missing | P2 | 2–4h | Assign to BU Lead P2 task |
| SIMP-007 | Wave 3/4 ID mismatches in MASTER_CAPABILITY_INDEX | P4 | 1–2h | Defer |
| SIMP-008 | Sub-section exclusion rules in CSM not in assets | P4 | 30 min + KRPE Phase B | Defer to Phase B |
| SIMP-009 | CON/COM type reservation cleanup | P4 | 1h | Defer to rules update WP |

**P1 items total effort:** ~3 hours  
**P2 items total effort:** ~5 hours  
**P3 items total effort:** ~50 minutes  
**P4 items total effort:** ~4.5 hours (deferred)

---

## 4. What This Register Excludes

The following were evaluated and excluded because they would require architectural changes, not simplifications:

- **Merging KRPE and KVE into one engine** — rejected (the separation is an architectural principle, ADR-002; merging would conflate extraction with validation)
- **Reducing the 5-document Universal Standard to 2–3 documents** — rejected (each document has a distinct change management rate; the separation prevents unnecessary re-approval)
- **Automating TIL** — rejected (automation of tender classification has unacceptable error rate for unstructured PDF tenders; TIL's human-AI mode is correct)
- **Simplifying the 19-step assembly sequence** — no simplification available; each step has a distinct purpose and gate

---

## 5. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-27 | WP18F | Initial simplification register — 9 entries from architecture review |
