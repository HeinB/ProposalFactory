---
document_id: WP18C2-SECTION-LIBRARY-CONSOLIDATION
title: "WP18C.2 — Proposal Section Library Consolidation"
version: "1.0"
status: "COMPLETE"
created: "2026-06-26"
created_by: "WP18C.2 — Section Library Consolidation"
programme_state: "WP18C.2 COMPLETE → next: WP18D"
platform_maturity: "L3.5 (unchanged — architecture synchronized)"
---

# WP18C.2 — Proposal Section Library Consolidation

**Work Package:** WP18C.2  
**Objective:** Resolve structural inconsistencies in the Proposal Section Library, synchronise downstream architecture documents, and validate changes against the ARM IT045 regression test.  
**Date completed:** 2026-06-26  
**Baseline:** WP18C.1 (Factory Optimisation) — 15 automation opportunities; revised roadmap; QA 72/100  
**Status:** COMPLETE

---

## 1. Executive Summary

WP18C.2 resolved four structural inconsistencies (SI-001, SI-005, SI-006, SI-007) and one known data issue (KI-001) identified in WP18C.1. The work was exclusively architectural — no proposal content was authored, no assumptions were changed, and no capability assets were modified. Seven architecture documents were updated, two ARM IT045 factory output documents were regression-corrected, and all 13 assumption packs now show accurate status.

The Section Library (PROPOSAL_SECTION_LIBRARY.md) is now the single authoritative structure. Duplicate section governance has been eliminated. Section ordering is deterministic for Pattern 13. The Pattern Engine and Section Library are fully aligned. The Content Source Matrix is internally consistent. The Assembly Sequence reflects production implementation. Platform maturity remains L3.5.

---

## 2. Issues Addressed

### SI-001 — S-38 / S-73 Structural Duplication (P0-A)

**Problem:** S-38 (Change Control Framework) and S-73 (Change Request Process) both appeared in scope for AMS proposals, creating structural duplication. S-38 was POPULATED in the ARM IT045 factory output despite ARM IT045 being an AMS engagement.

**Root cause:** The PROPOSAL_PATTERN_ENGINE.md had already encoded the SI-001 fix (S-38 excluded for AMS at Rule C-1), but three downstream documents had not been updated to reflect this, and two ARM IT045 factory outputs had been assembled before the fix was propagated.

**Resolution:**
- PROPOSAL_SECTION_LIBRARY.md v1.2: S-38 row updated to M-FIXED (Impl) / EXCL-AMS; footnote ¹ added with full SI-001 governance rule including Combination Pattern exception.
- PROPOSAL_SECTION_LIBRARY.md v1.2: S-73 row updated to COND-AMS; footnote ² added designating S-73 as AMS-authoritative.
- CONTENT_SOURCE_MATRIX.md v1.2: S-38 AMS exclusion applied; incorrect secondary source (AMS pack CR sections) removed; S-73 row updated to reflect sole governing status for AMS change management.
- PROPOSAL_ASSEMBLY_SEQUENCE.md v1.1: Step 15 note added — S-38 not assembled for AMS (SI-001); S-73 governs within AMS Support Model.
- ARM_IT045_PROPOSAL_ASSEMBLY_REPORT.md v1.1: S-38 row removed and marked EXCL-AMS; S-73 note updated to AMS-authoritative designation; regression note Section 13 added.
- ARM_IT045_PROPOSAL_STRUCTURE.md v1.1: S-38 row changed to NO (AMS); W2S1-005 target sections corrected from S-36/S-37/S-38 to S-36/S-37; section count corrected 57→56.

**Combination Pattern exception (preserved):** When an Implementation and AMS scope appear in the same tender, both S-38 and S-73 are included with clearly distinct scope boundaries. S-38 governs the implementation change process; S-73 governs the AMS change request process. Authority: PROPOSAL_PATTERN_ENGINE.md Rule C-1.

---

### SI-005 — AMS Section Ordering: References Before Commercial (P0-A)

**Problem:** References (S-67–S-69) were sequenced before the AMS Support Model and Commercial sections in the AMS assembly. Per the implemented Pattern 13 structure, References must appear AFTER Commercial and Compliance.

**Correct Pattern 13 document order:**
`Corporate → Understanding → Solution → Scope → AMS Support Model → Commercial → Compliance → References → Appendices`

**Resolution:**
- PROPOSAL_ASSEMBLY_SEQUENCE.md v1.1: Step 14 note added — References sub-step must execute after Step 15 (Commercial) for AMS pattern.
- PROPOSAL_ASSEMBLY_SEQUENCE.md v1.1: New Section 6 (Pattern 13 complete assembly order table) added showing all sections with correct document position and assembly step.
- ARM_IT045_PROPOSAL_STRUCTURE.md v1.1: SI-005 assembly order note added (section grouping in document reflects logical type, not assembly order; actual order governed by PROPOSAL_ASSEMBLY_SEQUENCE.md v1.1).

---

### SI-006 — Commercial Block Ordering: Pricing Before Assumptions (P1-B)

**Problem:** S-52 (Pricing) could be assembled before S-49 (Key Assumptions Body) in some assembly paths, violating the logical dependency (assumptions must be stated before pricing is presented).

**Correct commercial block order:** `S-49 → S-50 → S-51 → S-52`

**Resolution:**
- PROPOSAL_ASSEMBLY_SEQUENCE.md v1.1: Step 15 note added — Commercial block must follow SI-006 ordering: S-49 (Key Assumptions Body) → S-50 (Risk Register) → S-51 (Commercial Assumptions) → S-52 (Pricing).
- PROPOSAL_ASSEMBLY_SEQUENCE.md v1.1: Section 6 Pattern 13 table shows commercial block order explicitly.

---

### SI-007 — S-71 / S-72 Content Overlap: SLA and Incident (P1-B)

**Problem:** S-71 (SLA Framework) and S-72 (Incident Management) had no content boundary definitions. Assemblers could include SLA tier tables in S-72 or incident process narrative in S-71, creating duplicated or inconsistent content.

**Resolution:**
- PROPOSAL_SECTION_LIBRARY.md v1.2: Footnote added after S-76 row defining authoritative content boundaries for S-71 and S-72:
  - S-71: SLA tier table only + service hours + response≠resolution language. No incident narrative.
  - S-72: Incident classification process + escalation path + lifecycle only. No SLA tier table — reference S-71 instead.
- CONTENT_SOURCE_MATRIX.md v1.2: S-71 and S-72 rows updated with SI-007 assembly instructions as assembly directives.
- ARM_IT045_PROPOSAL_ASSEMBLY_REPORT.md v1.1: S-71 and S-72 assembly notes updated with SI-007 boundary instructions.

---

### KI-001 — Stale Assumption Pack Statuses in TENDER_BOM_LIBRARY.md (DATA)

**Problem:** TENDER_BOM_LIBRARY.md (v1.0, created 2026-06-16) showed 6 assumption packs with incorrect statuses:
- HCM Recruiting: "Draft" (actual: Approved v1.0 WP16C 2026-06-19)
- HCM Learning: "Draft" (actual: Approved v1.0 WP16C 2026-06-19)
- HCM Talent: "Draft" (actual: Approved v1.0 WP16C 2026-06-19)
- HCM Compensation: "Draft" (actual: Approved v1.0 WP16C 2026-06-19)
- Acumatica Base: "NOT YET CREATED" (actual: Approved v1.0 WP15C 2026-06-18 — 152 assumptions)
- BeBanking Base: "NOT YET CREATED" (actual: Approved v1.0 WP14F 2026-06-18 — 117 assumptions)

**Additional gap found:** EBS SLA Overlay and EBS DRM Overlay packs (both Approved v1.0 WP15F 2026-06-19) were absent from BOM 16 despite being used in ARM IT045 assembly.

**Resolution:**
- TENDER_BOM_LIBRARY.md v1.1: All six pack statuses corrected to Approved v1.0 with WP reference and date.
- TENDER_BOM_LIBRARY.md v1.1: EBS SLA Overlay and EBS DRM Overlay packs added to BOM 16 with status, assumption count, trigger conditions, and suppression rule reference.
- TENDER_BOM_LIBRARY.md v1.1: BOM 16 Key Restrictions updated: "Change control governed by S-73 (not S-38) in AMS proposals."

---

## 3. Architecture Documents Updated

| Document | Before | After | Changes Applied |
|---|---|---|---|
| PROPOSAL_SECTION_LIBRARY.md | v1.1 | **v1.2** | SI-001 (S-38 EXCL-AMS; S-73 COND-AMS); SI-007 (S-71/S-72 content boundaries); scoping cross-reference; Section 12 count note |
| CONTENT_SOURCE_MATRIX.md | v1.1 | **v1.2** | SI-001 (S-38 AMS exclusion + secondary source removed; S-73 AMS designation); SI-007 (S-71/S-72 boundary assembly instructions) |
| PROPOSAL_ASSEMBLY_SEQUENCE.md | v1.0 | **v1.1** | SI-001 (Step 15: S-38 not assembled for AMS); SI-005 (Step 14: References after Commercial); SI-006 (Step 15: S-49→S-50→S-51→S-52); SI-007 (Steps 13/15 references); Section 6 Pattern 13 complete assembly table |
| PROPOSAL_FACTORY_ARCHITECTURE.md | v1.1 | **v1.2** | Stage 0 TIL added to pipeline diagram; Stage 0 specification (inputs/outputs/10-step sequence); Stage dependency map; Platform Components table (6 TIL engine files); Governing Documents table (7 TIL docs) |
| TENDER_BOM_LIBRARY.md | v1.0 | **v1.1** | KI-001: 4 HCM module packs + Acumatica Base + BeBanking Base statuses corrected; EBS SLA + DRM overlays added to BOM 16; BOM 16 restrictions updated |
| ARM_IT045_PROPOSAL_ASSEMBLY_REPORT.md | v1.0 | **v1.1** | RF-001: S-38 excluded (EXCL-AMS); RF-002: S-73 AMS-authoritative; RF-003: SI-007 boundaries on S-71/S-72; RF-004: A15 S-73 only; Section 13 regression notes; section count 57→56 |
| ARM_IT045_PROPOSAL_STRUCTURE.md | v1.0 | **v1.1** | S-38 row changed to NO (AMS); W2S1-005 targets corrected; section count 57→56; SI-005 assembly order note |

**Total documents updated:** 7

---

## 4. Regression Review Results

**ARM IT045 regression test** (Oracle EBS AMS — Pattern 13):

| Check | Expected | Result | Finding |
|---|---|---|---|
| Duplicate Change Control removed | S-38 excluded for AMS | **PASS** | RF-001 identified and corrected; S-38 now EXCL-AMS across all documents |
| S-73 designated sole governing section | S-73 = AMS-authoritative | **PASS** | RF-002 corrected; S-73 note updated |
| Section ordering corrected (SI-005) | References after Commercial | **PASS** | PROPOSAL_ASSEMBLY_SEQUENCE.md v1.1 governs; SI-005 note added to ARM IT045 structure |
| Assumptions ordering (SI-006) | S-49→S-50→S-51→S-52 | **PASS** | PROPOSAL_ASSEMBLY_SEQUENCE.md v1.1 Step 15 note applied |
| SLA/Incident overlap removed (SI-007) | S-71 SLA only; S-72 incident only | **PASS** | RF-003 corrected; boundary instructions in Section Library, Content Matrix, Assembly Report |
| No downstream dependency failures | All engine files consistent | **PASS** | All 5 architecture documents internally consistent; no broken references |
| Pattern Engine remains valid | Pattern 13 Rule C-1 intact | **PASS** | PROPOSAL_PATTERN_ENGINE.md v1.0 unchanged; SI-001 already encoded |

**Regression findings resolved:**

| ID | Finding | Severity | Resolution |
|---|---|---|---|
| RF-001 | S-38 in AMS assembly (ARM IT045 PROPOSAL_STRUCTURE, ASSEMBLY_REPORT) | CRITICAL | CORRECTED — S-38 removed; section count 57→56 |
| RF-002 | S-73 described as "consistent with S-38" (ASSEMBLY_REPORT Section 9) | HIGH | CORRECTED — S-73 AMS-authoritative designation applied |
| RF-003 | S-71/S-72 no SI-007 boundary instructions (ASSEMBLY_REPORT Section 9) | MEDIUM | CORRECTED — boundary instructions added |
| RF-004 | A15 action references "S-38/S-73" (ASSEMBLY_REPORT Section 11) | LOW | CORRECTED — S-73 only |

**Downstream architecture validation (all PASS):**

| Document | Version | Status |
|---|---|---|
| PROPOSAL_PATTERN_ENGINE.md | v1.0 | PASS — SI-001 Rule C-1 encoded; no changes required |
| PROPOSAL_SECTION_LIBRARY.md | v1.2 | PASS — SI-001/SI-007 applied; Pattern Engine cross-reference added |
| CONTENT_SOURCE_MATRIX.md | v1.2 | PASS — S-38/S-73/S-71/S-72 all corrected |
| PROPOSAL_ASSEMBLY_SEQUENCE.md | v1.1 | PASS — SI-001/SI-005/SI-006/SI-007 applied; Pattern 13 order table complete |
| PROPOSAL_FACTORY_ARCHITECTURE.md | v1.2 | PASS — Stage 0 operational; dependency map current |
| TENDER_BOM_LIBRARY.md | v1.1 | PASS — all pack statuses accurate; overlays documented |

---

## 5. Before / After Metrics

### Section Library

| Metric | Before (v1.1) | After (v1.2) | Delta |
|---|---|---|---|
| Total sections in library | 82 | 82 | 0 (S-38 retained in library; excluded per pattern, not deleted) |
| AMS in-scope sections (Pattern 13) | 44 *(S-38 incorrectly included)* | 43 *(S-38 correctly excluded)* | -1 |
| Sections with AMS exclusion rules | 0 | 1 (S-38) | +1 |
| Sections with content boundary definitions | 0 | 2 (S-71, S-72) | +2 |
| Sections with AMS-authoritative designation | 0 | 1 (S-73) | +1 |
| Scoping cross-reference to Pattern Engine | No | Yes | Added |
| Structural duplicates (AMS scope) | 1 (S-38 + S-73 both in AMS) | 0 | -1 |

### ARM IT045 Assembly (Regression Test)

| Metric | Before | After | Delta |
|---|---|---|---|
| Sections in scope | 57 | 56 | -1 (S-38 correctly excluded) |
| Change management sections | 2 (S-38 + S-73 — duplicate) | 1 (S-73 only) | -1 |
| SI-007 boundary instructions present | 0 | 2 (S-71, S-72) | +2 |

### Assumption Pack Library

| Metric | Before | After | Delta |
|---|---|---|---|
| Packs with accurate status | 7 of 13 | 13 of 13 | +6 |
| Packs listed as Draft/Not Created | 6 | 0 | -6 |
| EBS overlay packs documented in BOM | 0 | 2 | +2 |

### Architecture Documents

| Metric | Before | After | Delta |
|---|---|---|---|
| Documents reflecting Stage 0 TIL | 0 | 1 (PROPOSAL_FACTORY_ARCHITECTURE.md) | +1 |
| Documents with SI-001 applied | 1 (Pattern Engine only) | 6 | +5 |
| Documents with SI-007 boundaries | 0 | 3 | +3 |
| Documents with SI-005/SI-006 ordering | 0 | 2 (Assembly Sequence, both ARM IT045 docs) | +2 |

### Platform Metrics

| Metric | Before (WP18C.1) | After (WP18C.2) | Notes |
|---|---|---|---|
| Platform maturity | L3.5 | L3.5 | Unchanged — no new engine components |
| ARM IT045 QA score | 72/100 | 72/100 | Unchanged — structural fixes; no content regeneration |
| QA projection (next AMS tender) | 72 | ~74–75 | +2–3 pts estimated from structural correctness (no duplicate Change Control; SI-007 prevents content duplication) |
| Current automation (ARM IT045) | 67% (assembly report) / 77.2% (factory) | 66% (corrected count — 37/56) | Assembly report % corrected for section count |
| Open known issues (KI-xxx) | 6 | 5 | KI-001 RESOLVED; KI-002 to KI-006 remain |
| Technical debt items (TD-xxx) | 5 | 5 | No new items; no items resolved |

---

## 6. Remaining Technical Debt

| ID | Item | Impact | Resolution Path |
|---|---|---|---|
| TD-001 | Risk Library: 0 approved entries (AI-only for S-50) | QA -5 pts; S-50 MANDATORY human review | WP18D or dedicated risk library WP |
| TD-002 | Rendering Engine: not built (Markdown → formatted proposal) | All proposals remain in Markdown; no client-ready PDF | WP19 |
| TD-003 | QA Engine: not built (automated section QA) | QA scoring manual; cannot enforce SI-007 boundaries programmatically | WP20 |
| TD-004 | Requirement Extraction Engine: not built (Stage 2) | S-14 (Understanding of Requirements) is AI-only; mandatory human review | WP18D.2+ |
| TD-005 | OCI capability narrative: no standalone asset (GAP-S22) | S-22 is AI-generated for all OCI engagements; GAP status in all OCI proposals | Create W4-OCI-001 capability asset |
| TD-006 | ARM_IT045_PROPOSAL_READINESS.md: v1.0 not regression-corrected | Minor — section count discrepancy (57→56) in readiness dashboard | Update at next ARM IT045 proposal refresh |

---

## 7. Open Known Issues (Post WP18C.2)

| ID | Issue | Status |
|---|---|---|
| KI-001 | Stale pack statuses in TENDER_BOM_LIBRARY.md | **RESOLVED** — v1.1 applied |
| KI-002 | ARM_IT045_PROPOSAL_DRAFT.md: S-50 Risk Register AI-only; 9 risks need BU approval | OPEN — requires BU Lead action |
| KI-003 | B-BBEE certificate expires 2026-07-31 — Plennegy and all active tenders | OPEN — CRITICAL; renewal in progress (OAR-C01) |
| KI-004 | KPMG reference blocked (AM-W4E3-001 ACTIVE) — affects BOM 12 PPM | OPEN — AM action required; signed letter not yet obtained |
| KI-005 | Mining Charter gap: no assumption pack covers mining-specific compliance | OPEN — flagged in ARM IT045 (GAP-005); no resolution path yet |
| KI-006 | Plennegy blockers: OAR-C01 (B-BBEE renewal) + OAR-C02 (board resolution) + OAR-A01 (AM approval required) — deadline 2026-07-31 | OPEN — escalated |

---

## 8. Success Criteria Verification

| Criterion | Status |
|---|---|
| Section Library becomes single authoritative structure | **PASS** — v1.2 with Pattern Engine cross-reference; all 82 sections; clear scoping boundary |
| All duplicate sections eliminated | **PASS** — S-38/S-73 duplication eliminated for AMS; Combination Pattern exception preserved |
| Ordering deterministic | **PASS** — PROPOSAL_ASSEMBLY_SEQUENCE.md v1.1 Section 6 defines complete Pattern 13 order |
| Pattern Engine and Section Library fully aligned | **PASS** — SI-001 Rule C-1 in Pattern Engine matches S-38 EXCL-AMS in Section Library |
| Content Source Matrix internally consistent | **PASS** — S-38 AMS exclusion applied; secondary source corrected; S-73/S-71/S-72 all updated |
| Assembly Sequence reflects production implementation | **PASS** — v1.1 with SI-001/SI-005/SI-006/SI-007 notes and Pattern 13 complete order table |

All six success criteria met.

---

## 9. Recommendations for WP18D

Priority order based on QA impact and factory readiness:

1. **Risk Library Population (TD-001) — QA impact +5 pts.** S-50 is the highest-risk open gap. Populating the Risk Library with approved entries (10–15 standard risks for AMS/EBS/OCI engagements) would move ARM IT045 QA from ~74 to ~79 and cross the 75 submission threshold. This is the single highest-ROI action for factory quality.

2. **Requirement Extraction Engine (TD-004).** S-14 (Understanding of Requirements) is currently AI-generated with mandatory human review. A structured Requirement Extraction Engine (Stage 2) would improve automation and reduce rework. Complexity: HIGH.

3. **OCI Capability Narrative Asset (TD-005) — W4-OCI-001.** S-22 is GAP status for all OCI proposals. A dedicated OCI capability narrative asset would convert S-22 from AI-GENERATE/GAP to EXTRACT/READY, adding approximately 2 QA points per OCI proposal.

4. **ARM IT045 Proposal Readiness Update (TD-006).** Minor — update ARM_IT045_PROPOSAL_READINESS.md to v1.1 to reflect corrected section count (56) and Scope and Governance recategorisation.

5. **Pattern Engine expansion.** Validate SI-001 through SI-007 ordering rules against all 13 patterns, not just Pattern 13. Some ordering rules may apply to Implementation patterns (e.g., SI-006 commercial ordering applies to all patterns with S-49–S-52 in scope).

6. **Rendering Engine (TD-002) — WP19.** Required before any client-ready proposal can be produced from the factory. Deferred per roadmap.

---

## 10. Governance Compliance

All WP18C.2 changes comply with programme governance constraints:

| Constraint | Compliance |
|---|---|
| Do not author proposal content | COMPLIANT — no proposal content was written or modified |
| Do not change assumptions | COMPLIANT — no assumption text was modified; pack statuses corrected (factual correction) |
| Do not change capability assets | COMPLIANT — no capability assets modified; target section references corrected |
| Do not build Rendering Engine | COMPLIANT |
| Do not build QA Engine | COMPLIANT |
| Do not populate Risk Library | COMPLIANT |
| Focus exclusively on Proposal Factory architecture | COMPLIANT — all changes are architectural (document structure, assembly rules, section metadata) |

---

*WP18C2_SECTION_LIBRARY_CONSOLIDATION.md v1.0 | WP18C.2 — Section Library Consolidation | 2026-06-26*  
*Status: COMPLETE. 7 architecture documents updated. 5 structural issues resolved. 6 regression findings corrected. Platform maturity L3.5 maintained. Next: WP18D.*
