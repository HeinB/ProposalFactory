---
doc_id: COMP-XXX
title: ""
doc_type: COMP
sub_type: ""           # BEE | Tax | VAT | COID | Insurance | Registration | CSD | Employment-Equity
business_unit: Corporate
service_area: ""
status: ""             # Active | Expired | Pending-Renewal | Archived | Draft
expiry_date: ""        # YYYY-MM-DD or None
days_to_expiry: 0      # Recalculate on each review: expiry_date minus today
expiry_status: ""      # Current (>90d) | Expiring-Soon (1-90d) | Expired (<0d) | No-Expiry
source_path: ""        # Relative path in legacy Tender Pack
kb_path: ""            # Relative path of copied file in Knowledge Base
date_added: ""         # YYYY-MM-DD
last_reviewed: ""      # YYYY-MM-DD
document_owner: ""     # Person responsible for keeping this current
review_frequency: ""   # Annual | Quarterly | On-Change | As-Needed
tags: []               # e.g. [BEE, compliance, empowerment, level-2]
issuing_authority: ""  # e.g. DTIC | SARS | CIPC | DoL | Compensation Fund
issue_date: ""         # YYYY-MM-DD
expiry_date_notes: ""  # Clarification if expiry is conditional or unclear
document_number: ""    # Certificate or reference number on the document
rating: ""             # BEE level only — e.g. "Level 2". Leave blank for other types.
verified: false        # Has a human confirmed this document is authentic and current?
verified_by: ""        # Full name of person who verified
verified_date: ""      # YYYY-MM-DD
scanned_ocr: false     # Is machine-readable OCR text available for this document?
notes: ""
---

## Document Summary

[Brief description of this compliance document — what it certifies, who issued it, and its relevance to tender submissions.]

## Usage Rules

- Only cite this document in tenders submitted **before** `expiry_date`.
- If `status` is `Expired` or `Pending-Renewal`, flag to the tender manager before use.
- If `verified` is false, do not cite without human confirmation.

## Renewal Actions

[What steps are needed to renew this document? Who is responsible? What is the lead time?]

## AI Retrieval Notes

[Notes to help the AI use this document correctly — e.g. "This BEE certificate covers all APPSolve entities" or "Applies only to the holding company, not subsidiaries."]
