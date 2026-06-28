# Stage 3 — Approved

**Stage in pipeline:** Candidate → Review_Required → Approved

## What belongs here

Content that has passed BU lead review and is cleared for use in tender responses. This is the only folder in this pipeline from which content may be cited, copied into a tender, or passed to an AI system.

## Before a file may move here from Review_Required

The BU lead must have:
1. Completed a full review (not just metadata check)
2. Confirmed the content is factually accurate and current
3. Confirmed no client-specific language or confidential figures remain
4. Set `approved_for_reuse: Yes` in the metadata block
5. Set `review_status: Approved` in the metadata block
6. Added their name to `approved_by` in the metadata block
7. Updated the corresponding row in `00_Governance/DOCUMENT_REGISTER.csv`:
   - Set `approved_for_reuse = Yes`
   - Set `kb_path` to the final destination in the KB (e.g. `06_Capabilities/Oracle/...`)

## After approval

Once a file is in this folder and the register is updated:
1. Copy the file to its KB destination path (as listed in `EXTRACTION_PLAN.md` and the register)
2. The copy in `Approved/` serves as the staging record; the KB destination is the working copy
3. If the content requires updates in future, the file returns to `Candidate_Content/` for a new extraction cycle — it does not get edited in-place in `Approved/`

## What must NOT happen

- Do not edit files in `Approved/` directly — start a new extraction cycle instead
- Do not copy unapproved files from `Candidate_Content/` or `Review_Required/` into a tender
- Do not set `approved_for_reuse: Yes` in the metadata block without BU lead sign-off

## Sub-folders

Mirror the KB structure:
- `Oracle/`
- `Acumatica/`
- `BeBanking/`
- `Cross_BU/`
