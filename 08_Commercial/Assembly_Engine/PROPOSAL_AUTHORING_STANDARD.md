---
document_id: TD-020
title: Proposal Authoring Standard v1.0
version: "1.0"
status: APPROVED
date: "2026-06-30"
engine: proposal_authoring_engine.py v1.0
platform_maturity: L6.2
---

# Proposal Authoring Standard v1.0

## Purpose

This document governs how the Proposal Authoring Engine (PAE) produces client-facing Oracle implementation proposals. PAE is the **final publishing step** of the Proposal Factory — it authors proposals from scratch, treating Knowledge Base assets as source evidence rather than proposal sections.

---

## Core Authoring Principles

| # | Principle | Imperative |
|---|---|---|
| 1 | PAE is an author, not a renderer | Never copy Knowledge Base asset text verbatim into the client proposal |
| 2 | Executive narrative first | The client sees a business story, not a feature list |
| 3 | "You" and "your" language | Write from the client's perspective, not APPSolve's |
| 4 | Page discipline | Client proposal must not exceed 40 pages including appendices |
| 5 | Internal content stays internal | Nothing with an asterisk, bracket notation, or source reference appears in client output |

---

## Permanent Governed Publishing Rules

### GOV-PAE-001 — Oracle Methodology (PERMANENT PLATFORM RULE)

> **Oracle Fusion Cloud proposals MUST use "Oracle's Modern Best Practices" and "Oracle Success Navigator" as the primary delivery methodology.**
>
> Oracle Unified Method (OUM) is **prohibited** for Oracle Fusion Cloud (SaaS) proposals. OUM may only be cited in proposals specifically addressing Oracle E-Business Suite (EBS) legacy engagements.
>
> No Fusion Cloud proposal may state:
> - "Our methodology is based on OUM"
> - "We follow Oracle Unified Method"
> - Any phrase that presents OUM as the primary delivery framework for cloud
>
> Permitted methodology citations for Fusion Cloud:
> - Oracle's Modern Best Practices
> - Oracle Success Navigator
> - Oracle Cloud implementation accelerators
> - Oracle reference architecture
> - Oracle Starter Configuration

**Enforcement:** This rule is hard-coded in `proposal_authoring_engine.py`. The authored methodology section explicitly uses Oracle Modern Best Practices language.

---

### Other Permanent Content Rules

| Rule | Prohibition |
|---|---|
| GOV-PAE-002 | Never name DFA, CCBA, or SAA as reference clients |
| GOV-PAE-003 | Never name Redpath Mining until Rule 21.5 waived |
| GOV-PAE-004 | Never name Hollywood Bets without AM approval |
| GOV-PAE-005 | Never cite "Oracle Gold Partner" (expired August 2021) |
| GOV-PAE-006 | Never cite BEE status after 2026-07-31 unless renewal confirmed |
| GOV-PAE-007 | Headcount: "more than 50 Senior Consultants" ONLY — never 100+/110+ |
| GOV-PAE-008 | Never include pricing, rates, or commercial estimates in authored sections |
| GOV-PAE-009 | References always "available on request" — never named without AM approval |

---

## Section Authority Matrix

| Section | Who Authors | Review Required |
|---|---|---|
| Executive Summary | BU Lead + Account Manager | Yes — BU Lead sign-off |
| Understanding of Requirements | Account Manager | Yes — BU Lead review |
| The Solution We Propose | PAE (authored) | BU Lead confirms scope table |
| Why APPSolve | PAE (authored) | Account Manager verifies awards/facts |
| How We Deliver | PAE (authored) | BU Lead confirms methodology accuracy |
| What We Deliver (Capability) | PAE (authored) | BU Lead confirms module claims |
| Project Governance | PAE (authored) | Project Manager confirms |
| Roadmap | PAE (authored) | PM confirms phase durations |
| Key Assumptions | PAE (authored) + Appendix | BU Lead + AM |
| Commercial | PAE (authored) | Commercial Director issues separate Commercial Proposal |
| Your Next Steps | PAE (authored) | AM confirms client action list |
| Appendix A — Assumptions | KB assets (PAE extracted) | BU Lead |
| Appendix B — References | AM approval required | AM sign-off before use |

---

## Quality Gates

A CLIENT_PROPOSAL output is submission-ready when ALL of the following are satisfied:

| Gate | Check |
|---|---|
| Q1 | No section marked [PENDING] remains — all authored or explicitly scoped out |
| Q2 | Executive Summary authored with this tender's win themes |
| Q2 | Understanding of Requirements reflects actual RFP/client brief |
| Q3 | Scope table confirmed by BU Lead (correct modules, correct entities) |
| Q4 | No OUM reference in any client-facing section |
| Q5 | No named references without AM approval |
| Q6 | B-BBEE certificate is current (not after 2026-07-31 without renewal) |
| Q7 | OPN status claim verified by Account Manager |
| Q8 | All sections BU Lead-reviewed before release |
| Q9 | Commercial Proposal issued separately — no pricing in this document |
| Q10 | Document named correctly: CLIENT_PROPOSAL_[TenderID].docx |
