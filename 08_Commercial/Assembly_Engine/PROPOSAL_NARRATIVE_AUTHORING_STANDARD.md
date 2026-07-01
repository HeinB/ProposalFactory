---
document_id: TD-026
title: Proposal Narrative Authoring Standard
engine: Proposal Narrative Engine (PNE) v1.0
platform: L6.4
last_updated: "2026-06-30"
status: APPROVED
---

# Proposal Narrative Authoring Standard

## Purpose

This document defines how the Proposal Narrative Engine (PNE) transforms governed knowledge asset content into a concise, persuasive customer-facing proposal narrative. It governs the authoring decisions, section structure, content reduction approach, and prohibited patterns for all client proposals produced by the PNE.

---

## Core Rule

**Knowledge assets are source material. They are not proposal sections.**

A proposal is a commercial communication to a client. It must be concise, persuasive, and outcome-focused. It must never expose the internal machinery of APPSolve's Knowledge Base — assumption IDs, governance decisions, draft markers, extraction notes, or capability catalogues — to a client.

The PNE applies this rule by:
1. Reading V2 rendered Markdown as source evidence
2. Authoring each proposal section from scratch using a business-outcome framework
3. Compressing KB content by a factor of 10–70× depending on the section

---

## Business-Outcome Framework

Every section of a PNE-authored proposal must address five dimensions:

| Dimension | Question | Notes |
|---|---|---|
| **Business Outcome** | What does this deliver for the client's business? | Measurable, client-specific language |
| **APPSolve Value** | Why is APPSolve better placed than alternatives? | Evidence-based, no unsupported claims |
| **Delivery Confidence** | Why will this actually get done? | Track record, methodology, team capability |
| **Customer Benefit** | What does the client experience day-to-day? | Operational and experiential outcomes |
| **Relevant Evidence** | What KB asset backs this claim? | Traceability only — not published verbatim |

Not every dimension appears in every paragraph. A capability section may foreground Business Outcome + Delivery Confidence. A "Why APPSolve" section foregrounds APPSolve Value + Customer Benefit. Authors apply judgement.

---

## Permanent Governance Rules (GOV-PAE-001)

**GOV-PAE-001 — PERMANENT AND NON-WAIVABLE:**

> Oracle Unified Method (OUM) MUST NOT be presented as the primary delivery methodology for Oracle Fusion Cloud proposals. Replace with:
> - Oracle's Modern Best Practices
> - Oracle Success Navigator
> - Oracle Cloud implementation accelerators
> - Oracle reference architecture
> - Oracle Starter Configuration
> - APPSolve Delivery Framework

OUM may only be mentioned historically or where specifically required for Oracle E-Business Suite legacy engagements. No Fusion Cloud proposal may ever state "Our methodology is based on OUM."

---

## Required Client Proposal Structure

| # | Section | Author | Target | Hard Max | Notes |
|---|---|---|---|---|---|
| 1 | Executive Summary | BU Lead + AM | 2 pages | 3 pages | PENDING — Plennegy win themes required |
| 2 | Understanding Plennegy's Requirements | Account Manager | 2 pages | 3 pages | PENDING — qualification notes required |
| 3 | Proposed Oracle HCM Solution | PNE (authored) | 6 pages | 8 pages | HCM Core + Recruiting + OIC + Learning + Talent |
| 4 | Why APPSolve | PNE (authored) | 3 pages | 4 pages | Oracle capability + SA track record + accountability |
| 5 | How We Deliver | PNE (authored) | 4 pages | 5 pages | Oracle Modern Best Practices — NOT OUM |
| 6 | Project Governance | PNE (authored) | 2 pages | 3 pages | Governance structure table |
| 7 | Implementation Roadmap | PNE (authored) | 2 pages | 3 pages | Phase table with milestones |
| 8 | Key Commercial Assumptions | PNE (authored) | 2 pages | 3 pages | 5-row summary — no IDs, no full packs |
| 9 | Key Delivery Risks and Mitigations | PNE (authored) | 2 pages | 3 pages | 5 material risks with APPSolve mitigations |
| 10 | Commercial Position | PNE (authored) | 1 page | 2 pages | Framework only — no binding pricing |
| 11 | Your Next Steps | PNE (authored) | 1 page | 2 pages | Client actions ONLY |
| **Total** | | | **27 pages** | **40 pages** | |

---

## What Never Appears in a Client Proposal

The following are PROHIBITED in any document with profile=CLIENT:

| Prohibited Content | Reason |
|---|---|
| Assumption IDs (ASM-xxx, CAP-xxx, etc.) | Internal KB identifiers |
| Document IDs (TD-xxx, ADR-xxx, WP-xxx, etc.) | Internal governance artefacts |
| "AI Draft" or "Action Required" markers | Internal review flags |
| "Human Review Required" labels | Internal quality flags |
| "Extraction Notes" or "Extraction Report" | Internal KB processing |
| "Governance Review" or "Governance Self-Review" | Internal governance |
| "Source Evidence" or "Source Mapping Table" | Internal traceability |
| "Pre-Tender Checks" | Internal readiness |
| Full assumption pack content | Replaces narrative with 60-page schedule |
| Oracle Unified Method / OUM | GOV-PAE-001 |
| BU decision tables | Internal governance records |
| Internal annotations in brackets | Internal change tracking |
| Section numbering with internal IDs | Internal registry references |

---

## Content Compression Targets

| KB Source Section | Typical KB Size | PNE Target | Compression Factor |
|---|---|---|---|
| Oracle Fusion HCM Capability | 555 content segs (≈69 pages) | 6 pages | 11× |
| Implementation Methodology | 140 segs (≈18 pages) | 4 pages | 4.5× |
| Project Governance | 140 segs (≈18 pages) | 2 pages | 9× |
| Key Assumptions (full) | 497 segs (≈62 pages) | 2 pages | 31× |
| Company sections (7) | 76 segs (≈10 pages) | 3 pages | 3.3× |

---

## Section Authority Matrix

| Section | Primary Author | Review Authority | Approved By |
|---|---|---|---|
| 1. Executive Summary | BU Lead + Account Manager | BU Director | BU Lead |
| 2. Understanding of Requirements | Account Manager | BU Lead | BU Lead |
| 3–11. Authored sections | PNE v1.0 (automated) | BU Lead | BU Lead |
| Appendices (if used) | Operations | BU Lead | BU Lead |

---

## Quality Gates (Pre-Submission)

| Gate | Check |
|---|---|
| **QG-001** | Sections 1 and 2 authored by humans — not showing PENDING |
| **QG-002** | No OUM anywhere in client proposal (GOV-PAE-001) |
| **QG-003** | No internal IDs (ASM, CAP, ADR, etc.) in client proposal |
| **QG-004** | Commercial position does not contain binding prices |
| **QG-005** | B-BBEE certificate is current (renewal deadline 2026-07-31) |
| **QG-006** | Next Steps section contains ONLY client actions |
| **QG-007** | All client references approved by referenced client |
| **QG-008** | "Oracle Level 1 Partner" used — NOT "Oracle Gold Partner" (expired Aug 2021) |
| **QG-009** | Headcount stated as "more than 50 Senior Consultants" ONLY |
| **QG-010** | Client name consistent throughout (no placeholder tender IDs) |

---

## Relationship to Other Engines

```
KRPE → KVE → ARE → RSE → PSAE → Renderer → PPE → Shaper → PEE → PAE
                                                                     ↓
                                                                    PNE (replaces PAE for v.NEXT output)
```

PNE is the terminal authoring layer. It reads V2 rendered Markdown (Renderer output) as source and produces authored narrative. It does NOT call PPPE, Shaper, or PEE — it replaces the verbatim rendering pipeline with a purpose-written narrative pipeline.
