---
# Extraction Metadata Block
# Copy this block to the TOP of every extracted content file.
# All 8 fields are required. Do not remove any field.

source_document: ""
# The filename of the source document only (not the full path).
# Example: "Oracle Fusion Template.docx"

source_path: ""
# The full path to the source file in the historical corpus or Tender Pack.
# Must be a path within Parties/Customers/ or Tender Pack/ — never a KB path.
# Example: "Parties/Customers/0. Proposal Templates/Oracle Fusion/Oracle Fusion Template.docx"

extraction_date: ""
# Date this extraction was performed. Format: YYYY-MM-DD.
# Example: "2026-06-08"

extracted_by: ""
# Name of the person who performed the extraction.
# Example: "Hein Blignaut"

readiness: ""
# One of three values only:
# DIRECT         — Use with minor name/date updates only. No substantive rewriting needed.
# MODERNISE      — Content is structurally sound but requires updating before use.
#                  (Outdated technology references, old company stats, deprecated features.)
# STRUCTURE ONLY — The document structure is reusable but the text must be written fresh.
#                  (Client-specific text, legally prescribed format, or too outdated to use.)

approved_for_reuse: "No"
# No          — Default. Not yet reviewed or approved.
# Conditional — Approved for use but with restrictions noted in the document body.
# Yes         — Fully approved. BU lead sign-off obtained. Register updated.
# Must be "No" when the file is in Candidate_Content/ or Review_Required/.
# May only be set to "Yes" or "Conditional" by the BU lead reviewer.

business_unit: ""
# The primary business unit this content serves.
# One of: Oracle | Acumatica | BeBanking | Cross_BU

review_status: "Candidate"
# Tracks which stage of the extraction pipeline the file is in.
# Candidate      — File is in 07_Approved_Content/Candidate_Content/
# Review_Required — File is in 07_Approved_Content/Review_Required/
# Approved       — File is in 07_Approved_Content/Approved/ and register updated
# Must match the folder the file currently lives in.
---
