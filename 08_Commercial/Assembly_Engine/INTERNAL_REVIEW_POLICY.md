---
document_id: TD-025
title: Internal Review Policy v1.0
version: "1.0"
status: APPROVED
date: "2026-06-30"
---

# Internal Review Policy v1.0

## Purpose

The `PPPE_INTERNAL_[Tender].docx` (PROFILE_INTERNAL) is the complete, unfiltered internal working document. No publishing rules are applied. It contains the full V2 rendered Knowledge Base content for BU Lead review, governance, and audit purposes.

---

## What PROFILE_INTERNAL Contains

| Content | Present |
|---|---|
| All 41 V2 sections (including PLACEHOLDERs and AI-DRAFTs) | Yes |
| Full assumption libraries with all IDs | Yes |
| OUM references | Yes (unmodified) |
| BU decision tables | Yes |
| Governance notes and approval records | Yes |
| Extraction notes and fact verification | Yes |
| Source evidence columns in tables | Yes |
| Policy application summary table | Yes |

---

## Policy Application Summary (in Internal Pack)

The PPPE writes a Policy Application Summary table at the top of the INTERNAL pack showing:

| Metric | Description |
|---|---|
| Sections excluded from customer | Names of sections excluded by PPPE |
| Assumption packs summarized | Which packs were summarized for customer |
| OUM replacements | Count of OUM → Oracle Modern Best Practices replacements |
| ID removals | Count of internal IDs stripped |
| Annotation removals | Count of change history annotations stripped |
| BU tables removed | Count of BU decision tables removed |
| Gov subsections removed | Count of governance subsections excluded |
| Segments in/out | Total V2 segments → published segments |

---

## Who Uses the Internal Review Pack

| Role | Use |
|---|---|
| BU Lead | Review accuracy of PPPE-authored assumption summaries; verify capability section budget decisions |
| Account Manager | Verify reference sections; approve client-facing content |
| Quality Assurance | Audit what was removed vs published |
| Governance | Audit log of what was excluded from customer output |

---

## PROFILE_REVIEW Usage

The `PPPE_REVIEW_[Tender].docx` (PROFILE_REVIEW) shows customer-facing content with green policy annotations indicating what rules were applied and how many items were removed per section. Use this for editorial review before releasing `PPPE_CUSTOMER_[Tender].docx`.

---

## Distribution

| Profile | Distribution |
|---|---|
| `PPPE_CUSTOMER_[Tender].docx` | Client — after BU Lead and AM sign-off |
| `PPPE_INTERNAL_[Tender].docx` | APPSolve internal only — never to client |
| `PPPE_REVIEW_[Tender].docx` | APPSolve editorial review only — never to client |
| `PPPE_POLICY_REPORT_[Tender].md` | Governance audit record |
