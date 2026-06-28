---
document_id: ENGINE-ASSUMPTION-EXTRACTOR
title: "Assembly Engine — Assumption Extractor"
version: "1.0"
created: "2026-06-19"
created_by: "WP17B — Assembly Engine Core (MVP)"
status: "Active"
component: "Step 4 of 5 — see ENGINE_ORCHESTRATOR.md"
---

# Assembly Engine — Assumption Extractor

**Purpose:** Extracts individual assumptions from each approved pack in load order, applying the suppression and replacement decisions from RULE_PROCESSOR.md, to produce the ASSEMBLED_ASSUMPTION_SCHEDULE.md.

**Inputs:** Rule-Processed Manifest from RULE_PROCESSOR.md  
**Outputs:** ASSEMBLED_ASSUMPTION_SCHEDULE.md in the tender workspace  
**Authority:** `08_Commercial/TENDER_ASSUMPTION_ASSEMBLY_RULES.md` (v1.9)

---

## Assumption ID Format by Pack

All assumptions follow the format `PREFIX-CATEGORY-NNN`. The prefix is pack-specific:

| Pack | ID Prefix | Examples |
|---|---|---|
| HCM Base | HCM- | HCM-GEN-001, HCM-SEC-001, HCM-JRN-001 |
| HCM Recruiting | HCM-REC- | HCM-REC-001 |
| HCM Learning | HCM-LRN- | HCM-LRN-001 |
| HCM Talent | HCM-TAL- | HCM-TAL-001 |
| HCM Compensation | HCM-CMP- | HCM-CMP-001 |
| ERP Pack | ERP- | ERP-GEN-001, ERP-GL-001, ERP-EXC-001 |
| OCI Pack | OCI- | OCI-GEN-001, OCI-LZ-001, OCI-EXT-001 |
| OIC Pack | OIC- | OIC-SCP-001, OIC-DES-001, OIC-EXC-001 |
| AMS Pack | AMS- | AMS-SCP-001, AMS-INC-001, AMS-EXC-001 |
| EBS SLA Overlay | EBS-SLA- | EBS-SLA-001, EBS-SLA-053 |
| EBS DRM Overlay | EBS-DRM- | EBS-DRM-001, EBS-DRM-062 |
| Acumatica Base | ACU- | ACU-GEN-001 |
| BeBanking Base | BB- | BB-GEN-001 |

---

## Pack Extraction Instructions

### For each pack in load order:

1. Open the pack file at the registered path (from PACK_LOADER registry)
2. Identify assumptions by their bold ID markers: `**[ID]**`
3. Extract: assumption ID, full assumption text (everything after the bold ID marker up to the next bold ID marker)
4. Apply suppression decisions from RULE_PROCESSOR: skip any ID listed in the suppression log
5. Apply replacement annotations: where an assumption is marked `[REPLACES: AMS-XXX]`, record the replacement in the schedule
6. Continue until all non-suppressed assumptions from the pack are extracted
7. Record pack-level count: loaded count, suppressed count, net count

### Handling Replacement Annotations

Some overlay assumptions carry inline replacement annotations (e.g., `**EBS-SLA-002 [REPLACES: AMS-SLA-001]**`). These are informational — the replacement has already been applied by RULE_PROCESSOR. Extract the assumption text and record the replacement mapping in the schedule footer, not inline with the assumption text.

### Handling Exclusion Sections

Assumptions with category code `-EXC-` are Explicit Exclusions (Rule E — always included). Extract these exactly as authored; do not paraphrase or summarise exclusion text.

### Handling Customer Responsibilities

Assumptions with category code `-CUS-` or `-CON-` are Customer Responsibilities and Dependencies. Extract in full; list in the Customer Responsibilities section of the schedule, not the Assumptions section.

---

## ASSEMBLED_ASSUMPTION_SCHEDULE.md Structure

The extractor produces the schedule in the following structure. All sections are mandatory.

```markdown
# Assembled Assumption Schedule
**Tender:** [Tender ID — Client — Date]
**Assembly Pattern:** [Named pattern]
**Assembled:** [YYYY-MM-DD]
**Total Assumptions:** [N] (raw: [M]; suppressed: [P]; net: [N])

---

## Section 1 — Assembly Metadata

[Pack manifest table: Pack Name | Version | Assumptions Loaded | Suppressed | Net]

---

## Section 2 — Assumptions

### [Pack 1 Name]
*(Pack version | N assumptions)*

**[ID]**  
[Full assumption text]

**[ID]**  
[Full assumption text]

...

### [Pack 2 Name]
*(Pack version | N assumptions)*

...

---

## Section 3 — Explicit Exclusions

[All -EXC- assumptions from all packs, listed by pack]

---

## Section 4 — Customer Responsibilities

[All -CUS- and -CON- assumptions from all packs, listed by pack]

---

## Section 5 — Suppression Register

| Suppressed ID | Rule | Replaced By | Reason |
|---|---|---|---|

---

## Section 6 — Replacement Mappings

| Original ID (Suppressed) | Replacement ID (Active) |
|---|---|
```

---

## Proposal Insertion Guidance

When inserting the assembled assumption schedule into a proposal:

1. Use the section heading: **"Assumptions, Exclusions and Customer Responsibilities"**
2. Place after the proposed solution description and before the pricing table
3. Remove the assembly metadata header (Section 1) — internal use only
4. Exclusions (Section 3) must be presented separately from Assumptions (Section 2)
5. Customer Responsibilities (Section 4) may be presented as a sub-section or table
6. Suppression Register (Section 5) is internal — do not include in external submission
7. Sub-headings within the Assumptions section follow pack section structure (see `TENDER_ASSUMPTION_ASSEMBLY_RULES.md` Section 5.2)

---

*ASSUMPTION_EXTRACTOR v1.0 | WP17B — Assembly Engine Core (MVP) | 2026-06-19*
