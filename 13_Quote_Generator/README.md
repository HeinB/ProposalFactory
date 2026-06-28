# 13_Quote_Generator — Planning Document

**Status: NOT BUILT — folder structure reserved for future development.**

---

## Purpose

The Quote Generator is a separate module for producing short-form commercial documents that do not warrant a full tender response process. It is intentionally decoupled from the Tender Knowledge Base workflow.

**In scope:**
- Time-and-materials quotes (day rates, hours, milestones)
- Fixed-price quotes for small, well-defined engagements
- Statements of Work (SOW) for existing clients or simple new engagements
- Renewal and extension quotes for managed services or support contracts

**Out of scope — use the Tender KB instead:**
- Formal tender responses (RFQ, RFP, RFT)
- Government procurement submissions
- Anything requiring compliance documents, BEE certificates, or formal reference letters

---

## Planned Folder Structure

```
13_Quote_Generator/
  README.md                       ← this file
  Rate_Cards/                     ← pricing by role, BU, and service type
  Historical_Quotes/
    Won/                          ← accepted quotes for reuse reference
    Lost/                         ← declined quotes for pricing analysis
  SOW_Templates/                  ← blank SOW shells per engagement type
  Standard_Terms/                 ← payment terms, warranty clauses, IP ownership
  Assumptions_Exclusions/         ← reusable assumption and exclusion blocks
  Active_Quotes/                  ← quotes currently in preparation
  Submitted_Quotes/               ← archive of all submitted quotes
```

---

## Planned Content Per Folder

### Rate_Cards/
- Day rates by role and seniority (Oracle, Acumatica, BeBanking)
- Managed services monthly fee structures
- Travel and disbursement policy
- Rate review dates and approval history
- Separate rate cards per client where negotiated rates apply

### Historical_Quotes/
- One subfolder per quote (named by client and date)
- Won quotes: used as starting points for similar future quotes
- Lost quotes: pricing and scope lessons
- Each quote folder to contain the source document and a short outcome note

### SOW_Templates/
- Oracle EBS / Fusion implementation SOW shell
- Acumatica ERP implementation SOW shell
- Managed services SOW shell
- BeBanking integration SOW shell
- Ad-hoc support / T&M engagement shell

### Standard_Terms/
- Standard payment terms (net 30, milestone-based, retainer)
- Warranty and defect liability clauses
- IP ownership and confidentiality boilerplate
- Governing law and dispute resolution clauses
- Version-controlled — do not use outdated versions

### Assumptions_Exclusions/
- Standard assumption blocks per service type
- Standard exclusion blocks per service type
- Client-responsibility statements
- Out-of-scope boundary statements
- These are the primary risk-management mechanism in a quote

### Active_Quotes/
- Working folder for quotes in progress
- One subfolder per quote, named `QUOTE-NNN_ClientName_YYYY-MM`
- Cleared out once submitted (moved to Submitted_Quotes/)

### Submitted_Quotes/
- Archive of all submitted quotes, won and lost
- Mirrored in Historical_Quotes/ for those used as reuse references

---

## Separation from Tender Knowledge Base

The Quote Generator is a **peer module**, not a sub-module of the Tender KB.

| Dimension | Tender KB | Quote Generator |
|---|---|---|
| Document type | Tender responses, RFPs, RFQs | Quotes, SOWs |
| Compliance required | Yes — BEE, Tax, COID etc. | No — or attach from KB as needed |
| Procurement process | Formal | Informal or existing relationship |
| Typical value | Any | Small to medium engagements |
| Turnaround | Days to weeks | Hours to days |
| Approval chain | Full sign-off | Lighter approval |

When a quote grows into a formal tender, migrate it to `09_Active_Tenders/` in the Tender KB and treat it from there.

---

## Prerequisites Before Building

Before populating this module, the following should be in place:

1. **Approved rate cards** — current, signed-off day rates per role across all three BUs.
2. **Standard terms reviewed** — legal sign-off on the standard T&C blocks.
3. **Historical quotes inventory** — at least 5-10 past quotes identified and copied in.
4. **Naming convention agreed** — `QUOTE-NNN_ClientName_YYYY-MM` or similar.
5. **Approval workflow defined** — who signs off quotes before submission, and at what value threshold.

---

## Future AI Integration Notes

When this module is built out, the AI assistant should be able to:
- Draft a quote shell from rate card + scope description
- Pull standard assumptions/exclusions relevant to the engagement type
- Reference similar historical quotes for pricing sense-checks
- Flag if a standard terms version is outdated

The AI must **never invent rates, terms, or assumptions**. All content must come from approved sources in this folder.
