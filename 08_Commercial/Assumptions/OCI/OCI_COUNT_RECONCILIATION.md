---
title: OCI Assumption Count Reconciliation
version: v1.0
status: Complete
created: 2026-06-16
created_by: WP14A — Governance Baseline Correction Pass
finding_ref: F-01
---

# OCI Assumption Count Reconciliation

**WP14A — Finding F-01 | 2026-06-16**

---

## Summary

A discrepancy between the OCI pack frontmatter and the pack body/register was identified during the WP14 Governance Audit. This document records the reconciliation investigation and the authoritative corrected count.

---

## Evidence Table

| Source | Reported Count | Verification Method |
|---|---|---|
| `OCI_ASSUMPTIONS_V1.md` frontmatter (`assumption_count`) | 164 | Direct file read (line 13) |
| `OCI_ASSUMPTIONS_V1.md` pack header (`**Assumptions:** 164`) | 164 | Direct file read (line 44) |
| `OCI_ASSUMPTIONS_V1.md` pack footer (`164 assumptions`) | 164 | Direct file read (line 504) |
| `OCI_ASSUMPTIONS_V1.md` body (grep `^\*\*OCI-`) | **174** | `grep -c "^\*\*OCI-"` = 174 |
| `OCI_ASSUMPTION_REGISTER.csv` (grep `^OCI-`) | **174** | `grep -c "^OCI-"` = 174 |
| HANDOVER.md | 164 | File read (propagated from frontmatter) |
| ASSUMPTION_LIBRARY_ROADMAP.md | 164 | File read (propagated from frontmatter) |
| GOVERNANCE_DASHBOARD.md | 164 | File read (propagated from frontmatter) |
| TENDER_ASSUMPTION_ASSEMBLY_RULES.md Section 9 | 164 | File read (propagated from frontmatter) |

**Key finding:** The pack body and the assumption register are independently consistent at **174**. The frontmatter, pack header, footer, and all downstream governance documents propagated the incorrect value of **164**.

---

## Manual Section-by-Section Count

Each OCI section was read in full and assumptions counted by the `**OCI-XXX-NNN.**` pattern.

| Section | Code | Assumptions | Highest ID |
|---|---|---|---|
| 101 | OCI-GEN | 8 | OCI-GEN-008 |
| 102 | OCI-LZ | 10 | OCI-LZ-010 |
| 103 | OCI-IAM | 10 | OCI-IAM-010 |
| 104 | OCI-NET | 12 | OCI-NET-012 |
| 105 | OCI-SEC | 10 | OCI-SEC-010 |
| 106 | OCI-CMP | 8 | OCI-CMP-008 |
| 107 | OCI-STO | 8 | OCI-STO-008 |
| 108 | OCI-DB | 12 | OCI-DB-012 |
| 109 | OCI-MW | 8 | OCI-MW-008 |
| 110 | OCI-INT | 8 | OCI-INT-008 |
| 111 | OCI-BKP | 8 | OCI-BKP-008 |
| 112 | OCI-DR | 10 | OCI-DR-010 |
| 113 | OCI-MON | 8 | OCI-MON-008 |
| 114 | OCI-OPS | 8 | OCI-OPS-008 |
| 115 | OCI-CST | 8 | OCI-CST-008 |
| 116 | OCI-MIG | 12 | OCI-MIG-012 |
| 117 | OCI-PER | 8 | OCI-PER-008 |
| 118 | OCI-SUP | 8 | OCI-SUP-008 |
| 119 | OCI-EXT | 10 | OCI-EXT-010 |
| **Total** | **19 sections** | **174** | — |

**Manual count confirmed: 174 assumptions across 19 sections.**

---

## Root Cause

The frontmatter `assumption_count` field was set to 164 during the initial WP11H drafting phase. When the pack was expanded during WP11H-A (BU Lead decision application), 10 additional assumptions were added across multiple sections. The pack body was updated correctly, and the register was generated from the pack body (also correct at 174). However, the frontmatter metadata field, the pack header summary line, and the pack footer were not updated at the same time. All downstream governance documents then propagated the incorrect count of 164 from the frontmatter.

The register (`OCI_ASSUMPTION_REGISTER.csv`) independently confirms 174 rows, providing a cross-check that was not performed until WP14.

---

## Authoritative Count

**OCI Infrastructure Assumption Pack: 174 assumptions across 19 sections (101–119)**

---

## Corrections Applied (WP14A)

| File | Change | Status |
|---|---|---|
| `OCI_ASSUMPTIONS_V1.md` frontmatter `assumption_count` | 164 → 174 | **Applied 2026-06-16** |
| `OCI_ASSUMPTIONS_V1.md` pack header `**Assumptions:**` | 164 → 174 | **Applied 2026-06-16** |
| `OCI_ASSUMPTIONS_V1.md` pack footer | 164 → 174 | **Applied 2026-06-16** |
| `HANDOVER.md` (Quick Facts, Assumption Library table, Architecture Decisions, Document Register) | 164 → 174; programme totals updated | **Applied 2026-06-16** |
| `ASSUMPTION_LIBRARY_ROADMAP.md` (Current State table, Roadmap Summary, OCI section, totals) | 164 → 174; programme totals updated | **Applied 2026-06-16** |
| `TENDER_ASSUMPTION_ASSEMBLY_RULES.md` (Section 9 table, totals) | 164 → 174; programme totals updated | **Applied 2026-06-16** |
| `GOVERNANCE_DASHBOARD.md` (OCI row, programme totals) | 164 → 174; programme totals updated | **Applied 2026-06-16** |
| `OCI_ASSUMPTION_REGISTER.csv` | No change — register was already correct at 174 rows | Verified correct |

---

## Corrected Programme Totals

| Metric | Previously Stated | Corrected |
|---|---|---|
| OCI assumption count | 164 | **174** |
| Total registered assumptions | 1,050 | **1,060** |
| Total approved assumptions | 603 | **613** |
| Total draft/pending assumptions | 447 | **447** (unchanged) |

*Approved breakdown: HCM Base 114 + OIC 101 + ERP 128 + AMS 96 + OCI 174 = 613*
*Pending breakdown: HCM Recruiting 52 + Learning 43 + Talent 38 + Compensation 40 + Acumatica 152 + BeBanking 122 = 447*

---

*OCI Count Reconciliation v1.0 | WP14A — F-01 | 2026-06-16*
