# Stage 2 — Review Required

**Stage in pipeline:** Candidate → Review_Required → Approved

## What belongs here

Content that has been self-reviewed by the extractor and is ready for independent BU lead review. The extractor believes the content is clean (no client specifics, factually current, accurately attributed) but has not yet received sign-off from the BU lead.

## Before a file may move here from Candidate_Content

The extractor must have:
1. Re-read the extracted file against the source document to confirm nothing was missed or misquoted
2. Confirmed every factual claim (company stats, certifications, product versions, awards) is still accurate as of today
3. Confirmed no client names, tender references, or client-specific commercial terms remain
4. Updated `review_status: Review_Required` in the metadata block
5. Added `extracted_by` and `extraction_date` to the metadata block

## What the reviewer must do

The reviewer (BU lead) must:
1. Read the extracted content in full — not skim
2. Read the relevant section of the source document to verify accuracy
3. Confirm the `readiness` rating is correct (DIRECT / MODERNISE / STRUCTURE ONLY)
4. Add review comments as a Markdown section at the bottom of the file: `## Reviewer Notes`
5. Either approve (move to `Approved/`) or return to `Candidate_Content/` with notes

## Reviewer assignments

| Business Unit | Reviewer |
|---|---|
| Oracle | Hein Blignaut |
| Acumatica | Hein Blignaut |
| BeBanking | Hein Blignaut |
| Cross_BU | Hein Blignaut |

## What must NOT happen

- Files in this folder must not be used in tender responses
- The extractor must not self-approve their own extractions without a second read separated by at least one day
