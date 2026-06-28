# Stage 1 — Candidate Content

**Stage in pipeline:** Candidate → Review_Required → Approved

## What belongs here

Raw extracted text from a source document, following the steps in `00_Governance/EXTRACTION_PLAN.md`. Content has been pulled from the source but has NOT yet been independently reviewed.

## Before a file may enter this folder

The extractor must have:
1. Read the source document in full (not sampled)
2. Removed all client names, client-specific figures, and client-specific project context
3. Retained only APPSolve's own methodology, capability description, or company narrative
4. Added the extraction metadata block (see `00_Governance/Templates/EXTRACTION_CANDIDATE.meta.md`) as the first lines of the file
5. Set `review_status: Candidate` in the metadata block
6. Set `approved_for_reuse: No` in the metadata block

## What must NOT happen

- Content must not be used in a tender response while it is in this folder
- Content must not have `approved_for_reuse: Yes` while in this folder
- Content must not skip directly to `Approved/`
- Source files must not be modified or moved as part of extraction

## File naming convention

`[EXTRACTION_ID]-[BU]-[ContentType]-DRAFT.md`

Examples:
- `1A-ORA-ExecutiveSummary-DRAFT.md`
- `3A-ACU-ModuleLibrary-DRAFT.md`
- `7A-BB-H2H-Capability-DRAFT.md`

Extraction IDs match the codes in `00_Governance/EXTRACTION_PLAN.md`.

## Sub-folders

Create BU sub-folders as needed:
- `Oracle/`
- `Acumatica/`
- `BeBanking/`
- `Cross_BU/`
