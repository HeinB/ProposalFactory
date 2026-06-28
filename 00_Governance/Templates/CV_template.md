---
doc_id: CV-XXX
doc_type: CV
record_type: Consultant-Index-Record
business_unit: ""         # Oracle | Acumatica | BeBanking | Cross
status: Active            # Active | Archived (set to Archived when person leaves APPSolve)
kb_path: ""               # 03_People/Resource_Profiles/[BU]/CV-XXX.md
date_added: ""
last_reviewed: ""
document_owner: ""        # HR/PM lead responsible for keeping this current
person_name: ""           # Full name as it should appear in a tender
role: ""                  # Formal tender title — e.g. "Senior Oracle Fusion Consultant"
skill_tags: []            # 5–10 keywords for AI skill matching
                          # e.g. [Oracle Fusion, Financials, AP, AR, GL, implementation, functional]
modules_or_products: []   # Specific modules/products — e.g. [Oracle EBS R12, Fusion HCM, SQL]
active_certifications: [] # Current, non-expired certifications only
                          # Format: "Cert name (CERT-XXX, expires YYYY-MM)"
                          # Remove when cert expires — do not leave expired certs here
available_for_tenders: true  # Set to false if on long-term deployment, unavailable, or left APPSolve
apptime_id: ""            # APPTime employee/consultant reference ID — primary link to authoritative source
notes: ""                 # Availability notes, deployment status, or any qualifier
                          # e.g. "Deployed at [Client] until 2027-03 — available from 2027-04"
---

> **⚠ NOT A CV.**
> This is a Consultant Index Record used for AI skill matching and candidate identification only.
> Full CV content is maintained in APPTime. This record contains metadata only.
> To obtain the current CV for this consultant, generate it from APPTime.
> **Architecture Decision:** ADR-001-CV_SOURCE_OF_TRUTH.md (2026-06-10).

---

## Skill Tags

[Repeat the `skill_tags` and `modules_or_products` frontmatter as a short bulleted list for human readability. Do not add narrative text — the tags themselves are the content.]

**Technology and product focus:**
- 

**Modules and specialisations:**
- 

## Active Certifications

[List current, non-expired certifications. Cross-reference to CERT-XXX records in KB. Remove expired certifications — stale certifications in this record create accuracy risk in tenders.]

Format: `Cert Name (CERT-XXX, expires YYYY-MM)`

- 

## AI Retrieval Notes

[One or two sentences instructing the AI when to propose this consultant and when not to. This is the most important section for AI-assisted tender composition. Be specific about technology focus and any limitations.]

Examples:
- "Use this record when the tender requires Oracle Fusion Financials module experience. Do not propose if the tender requires Oracle HCM — this consultant specialises in Finance only."
- "Use for any Oracle EBS DBA or managed services engagement. Available for CMA-region (SA, Namibia) and remote engagements."
- "Do not propose for tenders requiring Acumatica payroll — this consultant's Acumatica experience is limited to Manufacturing and Distribution."

## APPTime Reference

**APPTime ID:** [apptime_id from frontmatter]

To obtain the current CV for this consultant: log into APPTime and generate the CV export for this consultant using the standard CV template.

**Do not copy CV text into this record.** This record is intentionally metadata-only. Any CV narrative added here will become stale and will create accuracy risk in tender responses.

---

*Governed by ADR-001-CV_SOURCE_OF_TRUTH.md. See CONSULTANT_INDEX_PROGRAMME.md for field definitions, ownership model, and maintenance cycle.*
