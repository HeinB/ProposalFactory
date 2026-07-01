---
document_id: PEE-RULES-V1
title: "Proposal Editorial Engine — Editorial Rule Library v1.0"
version: "1.0"
status: "APPROVED"
created: "2026-06-30"
created_by: "PF2-008 — Proposal Editorial Engine"
---

# Editorial Rule Library v1.0

Editorial rules applied by `pee.py` when transforming a V3 structured proposal into a client-ready V4 proposal.

---

## 1. Rule Categories

| Category | Code Prefix | Description |
|---|---|---|
| Content Filter | CF | Remove internal-only content from CLIENT profile |
| Boilerplate | BP | Remove Oracle/vendor marketing boilerplate |
| Deduplication | DD | Remove near-identical content repeated across sections |
| Budget | BG | Enforce page budget per section |
| Authored | AU | Replace placeholder/over-budget content with PEE-authored narrative |
| Classification | CL | Classify assets: body / appendix / internal-only / traceability |

---

## 2. Content Filter Rules (CF)

| Rule | Pattern | Action |
|---|---|---|
| CF-001 | HTML comment blocks (`<!-- ... -->`) | Remove entirely |
| CF-002 | Marker blockquotes containing `action required|ai-draft required|human review required|governance flags` | Remove from CLIENT |
| CF-003 | Paragraphs matching `Capability Statement \|` or `Methodology Statement \|` (KB metadata headers) | Remove from CLIENT |
| CF-004 | Paragraphs matching `Document ID: W[0-9]S[0-9]-\d+` (registry asset IDs) | Remove from CLIENT |
| CF-005 | Paragraphs matching `**(Scope|Governance|Usage):**` (KB governance tags) | Remove from CLIENT |
| CF-006 | Paragraphs matching `*Standalone pack` or `*Mandatory attachment` | Remove from CLIENT |
| CF-007 | Paragraphs matching `Governed under ASSUMPTION_GOVERNANCE` | Remove from CLIENT |
| CF-008 | AI sentinel paragraphs containing `AI-generated content to be inserted|must be reviewed and approved` | Remove from CLIENT |

---

## 3. Boilerplate Rules (BP)

Paragraphs matching any pattern below are removed from CLIENT profile.

| Rule | Pattern (regex) |
|---|---|
| BP-001 | `oracle cloud is the world'?s? \w+ cloud` |
| BP-002 | `oracle offers a (complete\|comprehensive\|full) suite` |
| BP-003 | `oracle partner network (is\|provides\|enables)` |
| BP-004 | `oracle corporation (is the\|provides\|offers)` |
| BP-005 | `as an? oracle \w+ partner[,.]` |
| BP-006 | `oracle has been (helping\|enabling\|powering)` |
| BP-007 | SQL/DDL content: `SELECT \w+ FROM|DDL script|SQL script` |
| BP-008 | Technical infrastructure noise: `JSON payload|REST endpoint|WSDL|XML schema|git commit|CI/CD` |

---

## 4. Deduplication Rules (DD)

| Rule | Description | Threshold |
|---|---|---|
| DD-001 | Normalise paragraph text: lowercase, strip punctuation, collapse whitespace | — |
| DD-002 | Hash first 300 characters of normalised text (MD5) | — |
| DD-003 | If hash seen in previous section → skip segment | Exact match |
| DD-004 | Minimum length for dedup consideration: 40 characters | — |
| DD-005 | Non-paragraph kinds (table, ulist, heading) are exempt from dedup | — |
| DD-006 | Hash scope is per-document (cross-section); resets between renders | — |

---

## 5. Budget Rules (BG)

Page budget = maximum content segments per section. 1 content segment ≈ 0.125 pages.

| V4 Section | Budget (segs) | Overflow Reference |
|---|---|---|
| 1. Executive Summary | 12 | — |
| 2. Understanding Requirements | 12 | — |
| 3. Proposed Oracle HCM Solution | 40 | — (authored) |
| 4. Why APPSolve | 24 | Appendix D |
| 5. Delivery Approach | 40 | Appendix B |
| 6. Project Governance | 24 | — |
| 7. Implementation Roadmap | 20 | — (authored) |
| 8. Key Assumptions | 24 | Appendix C |
| 9. Key Project Risks | 16 | — (authored) |
| 10. Commercial Inputs | 16 | — |
| 11. Next Steps | 12 | — |
| App A: HCM Capability Summary | 20 | — (authored) |
| App B: Detailed Capability Catalogue | 96 | — |
| App C: Assumption Schedule | 120 | — |
| App D: Reference Projects | 24 | — (authored) |
| App E: Glossary | 16 | — (authored) |

**BG-001**: When a section exceeds its budget, truncate at `max_content` segments.  
**BG-002**: Append cross-reference notice: `_This section has been summarised for conciseness. Full detail is provided in [overflow reference]._`  
**BG-003**: Budget does not apply to heading or comment segments — only paragraph, table, ulist, olist kinds.

---

## 6. Authored Content Rules (AU)

| Rule | Description |
|---|---|
| AU-001 | When a V3 section is PLACEHOLDER or AI_DRAFT and mode is `budgeted`, preserve section status (do not upgrade to AUTHORED) |
| AU-002 | When mode is `authored`, replace section content entirely with PEE-authored Seg list |
| AU-003 | Authored content must comply with all CF, BP, and governance rules before rendering |
| AU-004 | Authored content must use customer-facing language (no internal action language, no AM references visible in CLIENT output) |
| AU-005 | Authored content for CLIENT must not reveal OAR action item codes or internal governance identifiers |

---

## 7. Classification Rules (CL)

| Rule | Asset Category | Editorial Classification | V4 Location |
|---|---|---|---|
| CL-001 | Full Oracle HCM Capability Asset | Summary in body + full in appendix | App A (summary) + App B (full) |
| CL-002 | Implementation Methodology | Delivery approach in body; internal process detail unpublished | Sec 5 (approach only) |
| CL-003 | Full Assumption Schedule | Category summary in body + full schedule in appendix | Sec 8 (summary) + App C (full) |
| CL-004 | Risk Register | Top 5 authored project risks in body; full register unpublished | Sec 9 (authored top 5) |
| CL-005 | Reference Projects | Concise summaries in body (App D); detailed project descriptions available on request | App D (summaries only) |
| CL-006 | Governance documentation | INTERNAL REVIEW WORKBOOK only — never CLIENT | Internal only |
| CL-007 | Traceability panels | TRACEABILITY REPORT only | Traceability only |
| CL-008 | AI sentinel paragraphs | Remove from all CLIENT outputs | None (stripped) |

---

## 8. Publication Rules (PR)

The following must NEVER appear in the CLIENT V4 proposal under any circumstances.

| Rule | Prohibited Content |
|---|---|
| PR-001 | Approval Records (approver names, approval dates, reviewer signatures) |
| PR-002 | Governance Reviews (governance check outputs, SVRL reports) |
| PR-003 | Extraction Notes (source mapping, extraction rationale) |
| PR-004 | Fact Verification Summaries (FACT_BASELINE references, verification outputs) |
| PR-005 | Assembly Diagnostics (engine output logs, section status codes) |
| PR-006 | Source Mapping Tables (W2S1-xxx, KB asset IDs, document_id references) |
| PR-007 | Registry Identifiers (KRPE Build IDs, KVE validation outputs) |
| PR-008 | Engine Metadata (proposal_shaper.py output, pee.py processing notes) |
| PR-009 | Internal Comments (HTML comment blocks, editorial notes) |
| PR-010 | Human Review Instructions (Action Required notices, OAR codes) |
| PR-011 | AI Markers (AI-generated content notices, confidence scores) |
| PR-012 | Traceability Information (V2→V3→V4 source mapping, editorial log) |

---

*EDITORIAL_RULE_LIBRARY.md v1.0 — PF2-008 Proposal Editorial Engine | 2026-06-30*
