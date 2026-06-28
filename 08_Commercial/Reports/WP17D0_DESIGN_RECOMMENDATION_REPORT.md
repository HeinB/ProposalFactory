---
document_id: WP17D0-DESIGN-RECOMMENDATION-REPORT
title: "WP17D-0 — Assumption Schedule Design Recommendation Report"
version: "1.0"
status: "Complete"
created: "2026-06-22"
created_by: "WP17D-0 — Assumption Schedule Design Standard"
category: "Assembly Engine / Design Report"
scope: "Formal design recommendation for the client-facing Assumption Schedule standard. Synthesises output review, classification model, grouping rules, numbering, traceability, deduplication, and output format decisions into a single approved design baseline for WP17D-1 implementation."
---

# WP17D-0 — Assumption Schedule Design Recommendation Report

**Date:** 2026-06-22  
**Status:** COMPLETE  
**Work Package:** WP17D-0 (prerequisite to WP17D-1 — Inline Text Assembly)  
**Baseline:** WP17C Assembly Engine PRODUCTION READY; 13/13 packs Approved v1.0; 1,136 assumptions

---

## 1. Executive Summary

WP17D-0 has completed the design standard for client-facing Assumption Schedules. Three formal standard documents have been produced and are now the authoritative specifications for WP17D-1 implementation:

| Document | Purpose | Location |
|----------|---------|----------|
| `ASSUMPTION_SCHEDULE_STANDARD.md` | Format, numbering, traceability, deduplication, output format | `08_Commercial/Assembly_Engine/` |
| `ASSUMPTION_PUBLICATION_RULES.md` | Classification model; what is published vs internal | `08_Commercial/Assembly_Engine/` |
| `ASSUMPTION_GROUPING_RULES.md` | Section mapping; algorithmic grouping rules; per-pattern section structure | `08_Commercial/Assembly_Engine/` |

**Key design decisions (8)** are summarised in Section 4. All decisions are approved and binding for WP17D-1.

**WP17D-1 can now begin.** There are no outstanding design decisions. The standard provides sufficient specification for unambiguous implementation.

---

## 2. Current Output Assessment

### 2.1 Files reviewed

| File | Format | Purpose |
|------|--------|---------|
| `ARM_IT045_ASSEMBLED_ASSUMPTION_SCHEDULE.md` | ID-only schedule | WP17B dry-run output |
| `ARM_IT045_ASSEMBLY_AUDIT_REPORT.md` | Internal audit trail | WP17B dry-run output |
| `WP17B_ASSEMBLY_ENGINE_MVP.md` | Build report | WP17B process report |
| `WP17C_REGRESSION_TEST_REPORT.md` | Regression test results | WP17C test report |

### 2.2 Assessment findings

**The current Assembly Schedule output (ARM_IT045_ASSEMBLED_ASSUMPTION_SCHEDULE.md) is NOT client-consumable.**

| Finding | Issue | Impact |
|---------|-------|--------|
| **ID-only output** | Assumptions listed as bold IDs only — no text | Bid manager must manually look up every assumption in source packs before inserting into a proposal |
| **Pack-oriented structure** | Organised by source pack (ERP Pack, OCI Pack, AMS Pack, etc.) | Client must navigate 6 separate sections to understand their SLA commitments; client responsibilities are scattered across 4 sections |
| **Engineering notation** | Suppressed assumptions shown with strikethrough and rule codes (S1, S2, S3) | Engineering notation is confusing and unprofessional in a client document |
| **Suppression metadata in output** | Suppression rules, replacement mappings, and pack manifest are in the client schedule | Internal governance detail that should never appear externally |
| **Pack technical names** | "AMS Pack", "EBS DRM Overlay", "EBS SLA Overlay" used as section headings | Client does not understand these terms; confusing to non-Oracle specialists |
| **Count discrepancy** | Section 1.2 shows 1 suppressed; Section 5 shows 6 suppressed; frontmatter says 599 net but actual is 594 | Inconsistency undermines client confidence |
| **No document preamble** | No commercial protection language, no validity period, no non-objection clause | Reduces legal weight of the schedule in contract |
| **Customer responsibilities scattered** | ERP-CUS, OIC-CUS, AMS-CUS in separate sections | Client evaluator must scan 4+ sections to understand their obligations |
| **Exclusions scattered** | ERP-EXC, OCI-EXT, OIC-EXC, AMS-EXC in separate sections | Client cannot easily review what is excluded |

### 2.3 Assessment verdict

A complete redesign of the output format is required. The current format is appropriate as an internal engineering artefact (ID-level check) but is not suitable for:
- Direct insertion into a client proposal
- Client sign-off as a commercial schedule
- Legal enforceability as a scope boundary document

The Assembly Audit Report (ARM_IT045_ASSEMBLY_AUDIT_REPORT.md) is correctly structured as an internal document and requires no format change.

---

## 3. Source Assumptions in Current Packs

### 3.1 Pack assumption density by type

Based on review of the ARM IT045 dry-run output and pack structure knowledge:

| Assembly type | Pack sources | Net assumptions | Key sections |
|---------------|-------------|----------------|-------------|
| EBS AMS Full Stack | ERP + OCI + OIC + AMS + EBS-SLA + EBS-DRM | 594 | GEN, GL, AP, AR, FA, CM, PRO, PPM, REP, DAT, INT, SEC, WFL, TST, TRN, CUT, HYP, CUS, EXC + OCI full + AMS full + overlays |
| HCM Full Suite | HCM Base + 4 modules | 267 | HCM base sections + REC/LRN/TLT/COM module sections |
| OIC Standalone | OIC | 104 | SCP, DES, END, SEC, CERT, MAP, TST, PERF, CUT, MON, SUP, CUS, DEP, CON, EXC |
| BeBanking + OIC + AMS | BB + OIC + AMS | 305 | BB sections + OIC sections + AMS sections |
| Acumatica Standalone | ACU | 152 | ACU functional + delivery + compliance + CUS + EXC |

### 3.2 Proportion breakdown (illustrative, EBS AMS Full Stack)

| Client-facing section | Approx assumptions | % of schedule |
|----------------------|--------------------|--------------|
| A — Engagement & Commercial | ~24 | 4% |
| B — Project & Implementation | ~30 | 5% |
| C.1 — Oracle ERP | ~68 | 11% |
| C.3 — Oracle Integration | ~55 | 9% |
| D — Infrastructure (OCI) | ~152 | 26% |
| E — Service Management | ~175 | 29% |
| F — Security & Compliance | ~22 | 4% |
| G — Client Responsibilities | ~40 | 7% |
| H — Explicit Exclusions | ~39 | 7% |
| **Total (approx)** | **~605** | **100%** |

*Note: Indicative breakdown only. Actual counts determined by WP17D-1 implementation after full text extraction and section assignment. Count total differs slightly from 594 due to some assumptions classifying differently than the rough estimate. WP17D-1 count balance check is the authoritative measure.*

---

## 4. Design Decisions — Summary

All 8 design decisions made in WP17D-0. Each is documented below with the rationale and the authoritative document where it is codified.

---

### Decision 1: Assumption Type Classification

**Decision:** Define 7 assumption types: SCOPE, EXCL, CLIENT, TECH, SERVICE, COMM, GOV.

**Rationale:** Classification is needed to determine publication status and inform grouping. The 7 types cover all assumptions in all 13 approved packs. The classification is inferred from the assumption ID section code — no manual tagging required.

**Verdict for publication:** All 7 types are published. No internal-only individual assumptions exist in approved packs.

**Codified in:** `ASSUMPTION_PUBLICATION_RULES.md` Section 2

---

### Decision 2: Publication Rules

**Decision:** All assembled net assumptions (after suppression) are published in the client-facing schedule. No individual assumptions are withheld.

**Rationale:** The Assumption Library was designed as a commercial protection mechanism. All approved assumptions are authored for client-facing use. No approved assumption contains confidential rate, margin, or cost data (those are in the Commercial Director authority schedule).

**Suppressed assumptions:** Never published. Replacement assumptions are always published.

**Internal-only documents:** Assembly Audit Report, suppression log, BOM resolution, pack manifest — these are internal and never shared with clients.

**Codified in:** `ASSUMPTION_PUBLICATION_RULES.md` Sections 3 and 4

---

### Decision 3: Grouping Standard

**Decision:** Assumptions are re-grouped from their source pack organisation into 8 client-facing sections (A through H) based on a deterministic mapping using the assumption ID's pack prefix and section code.

**Rejected alternatives:**
- *Retain pack grouping* — Rejected: too technical; scatters client responsibilities and exclusions across multiple sections; confuses clients with pack names
- *Full semantic re-classification* — Rejected: requires reading all assumption text and subjective judgement; not deterministic; error-prone

**Selected approach:** Rule-based mapping (23 priority-ordered rules) that maps each assumption to a section purely from its ID, without reading the text. Deterministic, unambiguous, and implementable algorithmically.

**The 8 sections:**
| Section | Purpose |
|---------|---------|
| A — Engagement & Commercial | Commercial context and engagement scope |
| B — Project & Implementation | Delivery methodology, testing, training, cutover |
| C — Application Functional (sub-sections per product) | What is being built/configured |
| D — Infrastructure | OCI scope and approach (conditional) |
| E — Service Management | Managed services, SLA, resource model (conditional) |
| F — Security & Compliance | Security approach and regulatory posture |
| G — Client Responsibilities | All client obligations consolidated |
| H — Explicit Exclusions | All scope exclusions consolidated |

**Codified in:** `ASSUMPTION_GROUPING_RULES.md` Sections 2, 3, and 4

---

### Decision 4: Numbering Standard

**Decision:** Sequential numbering across the entire document (1, 2, 3 ... N), with source ID as an inline reference suffix in italics: `*(Ref: ERP-GEN-001)*`.

**Rejected alternatives:**
- *Source ID only (e.g., ERP-GEN-001)* — Rejected: cryptic for clients; exposes internal pack structure; long and unwieldy in legal references
- *Section-scoped numbering (A.1, A.2, B.1, B.2)* — Rejected: complicates cross-referencing ("was A.12 in v1 becomes B.3 in v2 after re-grouping"); makes CR citations ambiguous

**Selected approach:** Document-wide sequential numbering starting at 1. Inline ref suffix provides traceability without exposing full internal structure to the client.

**Rule:** Suppressed assumptions do not appear and do not consume a number. Replacement assumptions appear in their natural section position and do consume a number.

**Codified in:** `ASSUMPTION_SCHEDULE_STANDARD.md` Section 5

---

### Decision 5: Traceability Model

**Decision:** Two-layer traceability.

**Client layer:** Sequential number + Ref ID suffix in client document. Sufficient for contract reference and CR linkage.

**Internal layer:** Full mapping in Assembly Audit Report: `Client Seq# | Source ID | Pack | Pack Version | Section | Assembly Rule | Assembly Date`. This is the complete audit trail for any BU Lead or commercial query.

**Separation:** Clients see the clean commercial document. Internal teams see the full engineering and governance trail in the Audit Report.

**Codified in:** `ASSUMPTION_SCHEDULE_STANDARD.md` Sections 5 and 7

---

### Decision 6: Deduplication Rules

**Decision:** Three-tier deduplication model.

| Tier | Mechanism | Rule |
|------|-----------|------|
| ID-level | Unique ID prefixes per pack | Cannot occur by design — no additional logic needed |
| Suppression-level | S1–S4 rules | Overlay wins; suppressed assumption omitted from client output |
| Semantic-level | Human governance | Not automated; BU Lead escalation if suspected duplication |

**Rejected:** Automated semantic deduplication — rejected because it requires reading assumption text for every pair across 1,136 assumptions, introduces subjective judgement, and is not deterministic. The existing rule structure (S1–S4) handles all known overlaps.

**Codified in:** `ASSUMPTION_SCHEDULE_STANDARD.md` Section 8

---

### Decision 7: Suppression Handling in Client Output

**Decision:** Suppressed assumptions are completely absent from the client-facing schedule. No strikethrough, no rule codes, no notation. The replacement assumption appears in its natural section position without any reference to what it replaced.

**Rationale:** The suppression mechanism is an internal Assembly Engine concept. Exposing it to clients:
- Reveals that different SLA tiers have different assumption packs (commercial sensitivity)
- Confuses evaluators with engineering-level detail
- Weakens the commercial authority of the schedule

**Codified in:** `ASSUMPTION_SCHEDULE_STANDARD.md` Section 6 and `ASSUMPTION_PUBLICATION_RULES.md` Section 4

---

### Decision 8: Output Format

**Decision:** WP17D target output is **Proposal-Ready Markdown** (`.md` file).

| Format | Decision |
|--------|----------|
| Proposal-Ready Markdown | **PRIMARY OUTPUT for WP17D** |
| HTML | Not in WP17D scope — future enhancement |
| PDF | Generated by bid manager from DOCX; not engine output |
| Direct DOCX generation | Not in WP17D scope — WP17E target |

**DOCX integration:** Bid manager performs manual insertion into proposal template. Standard Word styles are mapped in `ASSUMPTION_SCHEDULE_STANDARD.md` Section 9.

**File naming:** `[TENDER_ID]_ASSUMPTION_SCHEDULE_V[X].md`

**Codified in:** `ASSUMPTION_SCHEDULE_STANDARD.md` Section 9

---

## 5. Approved Design Standard — Reference Summary

The following is the complete approved standard for client-facing Assumption Schedules, suitable for inclusion in WP17D-1 briefing.

### 5.1 Document structure

```
[Header block: client name, version, date, tender ref, engagement, assembled-by]
[Preamble: commercial protection language and non-objection clause]
[Engagement context summary table]

A. Engagement and Commercial Assumptions
   [numbered list — GEN sections from all packs, OCI-CST]

B. Project and Implementation Assumptions
   [numbered list — delivery sections: DAT/MIG, TST, TRN, CUT, HYP]

C. Application Functional Assumptions
   C.1 Oracle ERP           [if ERP Pack loaded]
   C.2 Oracle HCM           [if HCM Base loaded, sub-sections per module]
   C.3 Oracle Integration   [if OIC Pack loaded]
   C.4 Acumatica ERP        [if Acumatica Base loaded]
   C.5 BeBanking            [if BeBanking Base loaded]

D. Infrastructure Assumptions
   [if OCI Pack loaded — OCI sections except GEN, EXT, SEC, CST, SUP]

E. Service Management and Support Assumptions
   [if AMS Pack loaded — AMS sections + EBS-SLA-* + EBS-DRM-*]

F. Security and Compliance Assumptions
   [all -SEC- sections from all packs]

G. Client Responsibilities
   [all -CUS-, -CON-, -DEP- sections from all packs — consolidated]

H. Explicit Exclusions
   [all -EXC-, -EXT- sections from all packs — consolidated]
```

### 5.2 Entry format

```
N. [Full assumption text.] *(Ref: PACK-SECTION-NNN)*
```

### 5.3 What the ASSUMPTION_EXTRACTOR must do differently in WP17D-1

| WP17B behaviour | WP17D-1 behaviour |
|----------------|-----------------|
| Output assumption ID only | Output full assumption text + inline Ref |
| Group by source pack | Group by client-facing section (A–H) |
| Show suppression strikethrough | Omit suppressed assumptions entirely |
| Show suppression rule codes | No suppression notation |
| Output pack names as headings | Output client-friendly section headings |
| Number by pack (not by document) | Number sequentially across whole document |
| Include pack manifest metadata | Omit all internal metadata |
| Include suppression register | Omit suppression register |
| No commercial preamble | Include standard commercial preamble |

---

## 6. WP17D-1 Specification

### 6.1 What WP17D-1 must build

WP17D-1 must update the Assembly Engine to produce a client-facing Assumption Schedule conforming to this design standard, tested against the ARM IT045 pattern (EBS AMS Full Stack, 6 packs, 594 net assumptions).

### 6.2 Deliverables required from WP17D-1

| Deliverable | Description | Path |
|-------------|-------------|------|
| Updated `ASSUMPTION_EXTRACTOR.md` | v1.1 — defines the full-text extraction format and implements the grouping and numbering standard | `08_Commercial/Assembly_Engine/` |
| `ARM_IT045_ASSUMPTION_SCHEDULE_V1.md` | Full client-facing schedule for ARM IT045 (EBS AMS Full Stack) — proposal-ready markdown | `08_Commercial/Assembly_Engine/` |
| `WP17D1_INLINE_TEXT_ASSEMBLY_REPORT.md` | Method description, section counts, count balance verification, quality check results | `08_Commercial/Reports/` |

### 6.3 Source files to read at WP17D-1 start

WP17D-1 requires reading all 6 source packs to extract full assumption text:

```
08_Commercial/Assumptions/ERP/ERP_ASSUMPTIONS_V1.md         (123 assumptions)
08_Commercial/Assumptions/OCI/OCI_ASSUMPTIONS_V1.md         (174 assumptions)
08_Commercial/Assumptions/OIC/OIC_ASSUMPTIONS_V1.md         (104 assumptions)
08_Commercial/Assumptions/AMS/AMS_ASSUMPTIONS_V1.md         (84 loaded; 6 suppressed; 78 active)
08_Commercial/Assumptions/AMS/EBS_AMS_SLA_OVERLAY_V1.md    (53 assumptions)
08_Commercial/Assumptions/AMS/EBS_DEDICATED_RESOURCE_MODEL_ASSUMPTIONS_V1.md  (62 assumptions)
```

And the design standards:
```
08_Commercial/Assembly_Engine/ASSUMPTION_SCHEDULE_STANDARD.md
08_Commercial/Assembly_Engine/ASSUMPTION_PUBLICATION_RULES.md
08_Commercial/Assembly_Engine/ASSUMPTION_GROUPING_RULES.md
08_Commercial/Assembly_Engine/ARM_IT045_ASSEMBLED_ASSUMPTION_SCHEDULE.md  (ID list reference)
08_Commercial/Assembly_Engine/ARM_IT045_ASSEMBLY_AUDIT_REPORT.md          (suppression log)
```

### 6.4 WP17D-1 validation criteria

Before the WP17D-1 deliverables are accepted:

| Check | Pass condition |
|-------|--------------|
| Count balance | sum of all section assumptions = 594 (ARM IT045 net) |
| No suppressed assumptions visible | AMS-SLA-001, AMS-PRI-001, AMS-PRI-002, AMS-PRI-003, AMS-SLA-005, AMS-INC-004 absent from client schedule |
| Section G consolidated | All -CUS-, -CON-, -DEP- assumptions in Section G only; none in sections A–F |
| Section H consolidated | All -EXC-, -EXT- assumptions in Section H only; none in sections A–F |
| Numbering sequential | Numbers 1 through N with no gaps or resets |
| Ref IDs present | Every entry has `*(Ref: ID)*` suffix |
| No pack names in headings | Section headings use client-friendly labels from this standard |
| No internal metadata in output | No pack version, load count, suppression rule code, or assembly pattern name |
| Preamble present | Standard commercial protection preamble included |
| Header block present | Client name, version, date, tender ref, engagement |

---

## 7. Post-WP17D-1 Roadmap

Once the ARM IT045 pattern is proven in WP17D-1, the following patterns should be tested in subsequent sub-tasks:

| Sub-task | Pattern | Packs | Notes |
|----------|---------|-------|-------|
| WP17D-1 | EBS AMS Full Stack | 6 packs | Primary test (ARM IT045) |
| WP17D-2 | HCM Full Suite | 5 packs | Tests Section C.2 multi-module sub-sections |
| WP17D-3 | Acumatica Standalone | 1 pack | Tests Section C.4 |
| WP17D-4 | BeBanking + OIC + AMS | 3 packs | Tests Section C.5 + cross-product G/H consolidation |
| WP17D-5 | Plennegy (HCM + OIC + AMS) | 5+ packs | Live tender test case |

Plennegy-specific note: Plennegy requires HCM Full Suite (5 packs: HCM Base + REC + LRN + TLT + COM) + OIC + AMS = 7 packs, 455 assumptions. This pattern is not yet regression-tested for inline text. WP17D-5 should be the live Plennegy schedule, to be produced as soon as OAR-C01 and OAR-C02 are resolved.

---

## 8. Files Created by WP17D-0

| File | Path | Purpose |
|------|------|---------|
| `ASSUMPTION_SCHEDULE_STANDARD.md` | `08_Commercial/Assembly_Engine/` | Master format spec — structure, numbering, traceability, deduplication, output format |
| `ASSUMPTION_PUBLICATION_RULES.md` | `08_Commercial/Assembly_Engine/` | Classification model; publication status per type; suppression rules |
| `ASSUMPTION_GROUPING_RULES.md` | `08_Commercial/Assembly_Engine/` | Section mapping; algorithmic grouping rules; per-pattern structure |
| `WP17D0_DESIGN_RECOMMENDATION_REPORT.md` | `08_Commercial/Reports/` | This document — design summary, decisions, WP17D-1 specification |

---

## 9. Success Criteria — Met

WP17D-0 success criteria as defined in the session brief:

| Criterion | Status |
|-----------|--------|
| Which assumptions are published externally | **RESOLVED** — All assembled net assumptions are published (ASSUMPTION_PUBLICATION_RULES.md §3) |
| How assumptions are grouped | **RESOLVED** — 8 client-facing sections with deterministic 23-rule mapping (ASSUMPTION_GROUPING_RULES.md §3) |
| How assumptions are numbered | **RESOLVED** — Sequential document-wide numbering with inline Ref ID (ASSUMPTION_SCHEDULE_STANDARD.md §5) |
| How assumptions are formatted | **RESOLVED** — Numbered list with text + Ref suffix; proposal-ready markdown (ASSUMPTION_SCHEDULE_STANDARD.md §5, §9) |
| How traceability is maintained | **RESOLVED** — Two-layer model: client Ref ID + internal Audit Report mapping (ASSUMPTION_SCHEDULE_STANDARD.md §7) |
| How duplicates are handled | **RESOLVED** — Three-tier model: structural (impossible) / suppression (S1–S4) / semantic (BU Lead escalation) (ASSUMPTION_SCHEDULE_STANDARD.md §8) |
| How proposal-ready schedules are generated | **RESOLVED** — Proposal-ready markdown primary format; DOCX mapping defined; WP17D-1 implementation spec complete (ASSUMPTION_SCHEDULE_STANDARD.md §9) |
| Formally approved design standard | **COMPLETE** — 3 standard documents created and ready for WP17D-1 |

**WP17D-0 is COMPLETE. WP17D-1 may begin.**

---

*WP17D0_DESIGN_RECOMMENDATION_REPORT.md v1.0 | 2026-06-22 | COMPLETE*  
*Design standard approved. WP17D-1 implementation is authorised to proceed.*  
*Next: WP17D-1 — Inline Text Assembly (ARM IT045 first test case)*
