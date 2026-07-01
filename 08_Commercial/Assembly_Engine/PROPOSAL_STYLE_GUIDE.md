---
document_id: TD-027
title: APPSolve Proposal Style Guide
engine: Proposal V5 Narrative & Style Engine (PF2-010)
platform: L6.5
last_updated: "2026-06-30"
status: APPROVED
---

# APPSolve Proposal Style Guide

## Purpose

This guide defines how APPSolve proposals are written. It applies to every section of every client-facing proposal produced by the Proposal Narrative & Style Engine (V5) and written by human authors.

The goal is one thing: a proposal that reads like it was written by APPSolve's best proposal manager — not like a knowledge repository, capability catalogue, Oracle documentation, or AI output.

---

## The Four Questions

Every section of every proposal must answer four questions. If a paragraph does not answer at least one of these, it should not exist.

1. **What is the customer's challenge?** — Specific to this client. Not generic.
2. **What does APPSolve propose?** — Concrete. Scoped. Not aspirational.
3. **Why is this approach better?** — Against the alternative. Not against a strawman.
4. **What business outcome will the customer receive?** — Measurable. Plennegy-specific.

---

## Writing Style Rules

### Voice and Tone

| Rule | Correct | Incorrect |
|---|---|---|
| Write in active voice | "APPSolve configures Oracle to reflect your entity structure" | "Oracle is configured by APPSolve to reflect your entity structure" |
| Short paragraphs — 3–4 sentences maximum | Single point per paragraph | Multi-point multi-sentence paragraphs |
| Strong opening sentence | "Plennegy's HR function manages multiple sets of employee records" | "In order to meet the objectives of this project, it is important that..." |
| Business outcome before technology | "Payroll errors are eliminated because..." | "Oracle Integration Cloud is configured to..." |
| Technology supports the story | Introduce a module because it solves a problem | Describe a module because it exists |

### Sentence Construction

| Rule | Example |
|---|---|
| Start sentences with the subject | "APPSolve brings..." | Not "It is APPSolve's view that..." |
| Use concrete verbs | "delivers", "eliminates", "reduces", "replaces" | Not "leverages", "enables", "facilitates" |
| Avoid hedging language | "APPSolve will configure" | Not "APPSolve would aim to potentially configure" |
| Name the client in key claims | "Plennegy's payroll team" | Not "the client's team" |

---

## Words and Phrases — Prohibited

The following words and phrases make proposals read like AI output, Oracle documentation, or marketing material. Do not use them.

| Prohibited | Use instead |
|---|---|
| "leverages" | "uses", "applies", "draws on" |
| "robust" | Describe what makes it reliable |
| "seamlessly" | Describe the integration specifically |
| "world-class" | Unsupported claim — remove entirely |
| "best-of-breed" | Unsupported claim — remove entirely |
| "best practice" | "Oracle's standard approach" or describe the practice specifically |
| "end-to-end" | Describe the actual scope |
| "holistic" | Describe what is included |
| "innovative" | Describe the innovation specifically |
| "cutting-edge" | Describe what is new and why it matters |
| "state-of-the-art" | Remove entirely |
| "turnkey solution" | Describe what is delivered |
| "deep expertise" | Quantify or specify — "more than 50 Senior Consultants" |
| "our team of experts" | Name the team or specify its capabilities |
| "proven track record" | Specify the track record — client, outcome, scope |
| "strategic partner" | Describe the relationship specifically |
| "value-add" | Describe the value specifically |
| "scalable" | Describe how it scales and to what |
| "out of the box" | "Oracle's standard configuration" |
| "empower" | Describe what people can do |
| "transform" | Describe what changes and how |

---

## Section Templates

### Every Major Section

```
[Challenge — what is the client's specific problem?]

[Proposal — what does APPSolve propose, specifically?]

[Why — what makes this approach better than the alternative?]

[Outcome — what does the client receive, measurable?]
```

### Capability / Solution Section

```
[Current situation — client-specific, concrete]

[Future state — what life looks like after implementation]

[How the technology makes this possible — module by module, connected to the why]

[How APPSolve delivers it — brief, pointing to How We Deliver section]

[Business outcome — measurable, attributed to specific capabilities]
```

### Risk Section

```
[Risk — specific, honest about probability and impact]

[APPSolve's mitigation — what APPSolve actually does, not a plan to make a plan]

[Residual — what remains after mitigation, and how it is monitored]
```

---

## What Never Appears in a Client Proposal

| Prohibited Content | Why |
|---|---|
| Assumption IDs (ASM-xxx, CAP-xxx) | Internal KB identifiers — invisible to clients |
| Document IDs (TD-xxx, ADR-xxx, WP-xxx) | Internal governance artefacts |
| "AI Draft" or "Action Required" markers | Internal review flags |
| Oracle Unified Method / OUM | GOV-PAE-001 — prohibited for Fusion Cloud |
| Full assumption schedule verbatim | 60-page asset — summarise commercially |
| KB section content verbatim | Source material — not proposal sections |
| Extraction notes or governance self-review | Internal KB quality checks |
| Headcount as "100+" or "110+" | Use "more than 50 Senior Consultants" only |
| "Oracle Gold Partner" | Expired August 2021 — use "Oracle Level 1 Partner" |
| BEE status after 2026-07-31 | Certificate renewal required — check before submission |
| Hollywood Bets by name | AM approval required per tender |
| DFA, CCBA, SAA as references | Never cite in any context |
| Redpath Mining as reference | BU Lead waiver (Rule 21.5) required |

---

## Governance Rule GOV-PAE-001 (Permanent)

> Oracle Unified Method (OUM) MUST NOT be presented as the primary delivery methodology for Oracle Fusion Cloud proposals.

**Correct:** Oracle's Modern Best Practices, Oracle Success Navigator, Oracle Cloud implementation accelerators, APPSolve Delivery Framework.

**Never:** "Our methodology is based on OUM." "We follow the OUM lifecycle." "OUM phases."

OUM may only be referenced historically or where a client has explicitly specified it for Oracle E-Business Suite legacy engagements.

---

## Tone Reference — Good vs Bad

### Executive Summary

**Bad:**
> "APPSolve is pleased to present this proposal for a comprehensive, end-to-end Oracle Fusion HCM Cloud implementation leveraging our world-class Oracle expertise and proven track record to deliver a holistic HR transformation for Plennegy."

**Good:**
> "Plennegy Group is at an inflection point. The organisation has grown to a scale where the informal HR processes and disconnected systems that supported smaller operations can no longer carry the weight of a large, multi-entity agribusiness group."

---

### Solution Section

**Bad:**
> "Oracle Fusion HCM Core is a robust, scalable HCM module that seamlessly integrates with Oracle Recruiting Cloud and Oracle Integration Cloud to provide a best-of-breed, end-to-end human capital management solution."

**Good:**
> "After implementation, every Plennegy HR business partner works from the same employee record. Position transfers happen in Oracle — the record follows the employee. Payroll inputs flow automatically to the payroll provider at period-end."

---

### Why APPSolve

**Bad:**
> "APPSolve has deep expertise in Oracle Fusion HCM and has successfully delivered numerous world-class implementations across various industries, leveraging our team of highly skilled Oracle experts to empower clients with innovative solutions."

**Good:**
> "APPSolve has implemented Oracle Fusion HCM Cloud in South African enterprise organisations facing the same challenges Plennegy faces today. We understand South African HR as a configuration challenge, not a research project."

---

## Quality Targets (V5)

| Criterion | Target |
|---|---|
| Proposal length | 25–35 pages |
| Executive readability | 9/10 |
| Sales quality | 9/10 |
| Technical credibility | 10/10 |
| Internal governance leakage | 0 |
| Empty sections | 0 |
| Placeholders | 0 |
| OUM occurrences | 0 |
| Internal IDs | 0 |
