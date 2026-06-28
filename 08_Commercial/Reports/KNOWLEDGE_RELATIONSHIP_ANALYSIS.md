---
document_id: KNOWLEDGE-RELATIONSHIP-ANALYSIS-V1
title: "Knowledge Relationship Analysis"
version: "1.0"
status: "COMPLETE"
created: "2026-06-27"
created_by: "WP18E-IMP-B"
approved_by: "WP18E-IMP-B"
approved_date: "2026-06-27"
work_package: "WP18E-IMP-B"
category: "Analysis Report"
---

# Knowledge Relationship Analysis

**Date:** 2026-06-27  
**Work Package:** WP18E-IMP-B  
**Scope:** Phase A — REL-001 (ASP CONTAINS ASM) only  
**Registry build:** Build 4 (FULL, 2026-06-27)

---

## 1. Phase A Relationship Scope

KRPE Phase A generates one relationship type only:

| Rule ID | Type Code | Label | Direction | Cardinality |
|---|---|---|---|---|
| REL-001 | CON | CONTAINS | ASP → ASM | 1:N |

Every assumption in the registry is contained by exactly one pack. Every pack contains one or more assumptions. No orphan assumptions exist.

Phase B will add CAP-level relationship types (REL-002 through REL-010) covering capability-to-section, capability-to-pack, risk linkages, and methodology associations.

---

## 2. Graph Summary Statistics

| Metric | Value |
|---|---|
| Total relationship entries | **1,136** |
| Unique relationship types | **1** (CON/REL-001) |
| Source nodes (ASP) | **13** |
| Target nodes (ASM) | **1,136** |
| Resolved relationships | **1,136 / 1,136 (100%)** |
| Unresolved / broken references | **0** |
| Circular references | **0** |
| Bidirectional relationships | **0** |

The graph is a forest of 13 trees, each rooted at an ASP node with its assumptions as leaves. No edges cross between trees (no assumption belongs to more than one pack in Phase A).

---

## 3. Pack Connectivity

### 3.1 Sorted by Assumption Count

| Rank | Pack | Business Unit | ASM Count | % of Graph |
|---|---|---|---|---|
| 1 | OCI-ASSUMPTIONS-V1 | Oracle | 174 | 15.3% |
| 2 | ACU-BASE-ASSUMPTIONS-V1 | Acumatica | 152 | 13.4% |
| 3 | ERP-ASSUMPTIONS-V1 | Oracle | 123 | 10.8% |
| 4 | BEBANKING-BASE-ASSUMPTIONS-V1 | BeBanking | 117 | 10.3% |
| 5 | HCM-BASE-ASSUMPTIONS-V1 | Oracle | 115 | 10.1% |
| 6 | OIC-ASSUMPTIONS-V1 | Oracle | 104 | 9.2% |
| 7 | AMS-ASSUMPTIONS-V1 | Oracle | 84 | 7.4% |
| 8 | EBS-DRM-ASSUMPTIONS-V1 | Oracle | 62 | 5.5% |
| 9 | HCM-RECRUITING-ASSUMPTIONS-V1 | Oracle | 54 | 4.8% |
| 10 | EBS-AMS-SLA-OVERLAY-V1 | Oracle | 53 | 4.7% |
| 11 | HCM-LEARNING-ASSUMPTIONS-V1 | Oracle | 37 | 3.3% |
| 12 | HCM-TALENT-ASSUMPTIONS-V1 | Oracle | 31 | 2.7% |
| 13 | HCM-COMPENSATION-ASSUMPTIONS-V1 | Oracle | 30 | 2.6% |
| **Total** | | | **1,136** | **100%** |

### 3.2 Distribution Observations

- **Top 3 packs** (OCI, ACU-BASE, ERP) account for 39.5% of all assumptions.
- **Bottom 3 packs** (HCM-LEARNING, HCM-TALENT, HCM-COMPENSATION) account for 8.6%.
- Oracle holds 10 of 13 packs (77%) and 832 of 1,136 assumptions (73%).
- Distribution is right-skewed (mean 87.4, range 30–174).

### 3.3 Business Unit Aggregate

| Business Unit | Packs | Assumptions | % of Total |
|---|---|---|---|
| Oracle | 10 | 832 | 73% |
| Acumatica | 1 | 152 | 13% |
| BeBanking | 1 | 117 | 10% |
| Corporate/Shared | 0 | 0 | 0% |

No cross-BU (Corporate/Shared) assumption pack exists in Phase A scope.

---

## 4. Graph Integrity Checks

### 4.1 Completeness

| Check | Result |
|---|---|
| Every ASM has exactly one parent_pack_id | 1,136 / 1,136 ✓ |
| Every parent_pack_id resolves to a known ASP | 1,136 / 1,136 ✓ |
| Every ASP has at least one outgoing REL-001 edge | 13 / 13 ✓ |
| Every ASM has exactly one incoming REL-001 edge | 1,136 / 1,136 ✓ |

### 4.2 Consistency

| Check | Result |
|---|---|
| Source node type = ASP for all REL-001 | ✓ |
| Target node type = ASM for all REL-001 | ✓ |
| `resolved: true` on all relationships | 1,136 / 1,136 ✓ |
| `bidirectional: false` on all REL-001 | 1,136 / 1,136 ✓ |
| `declared_in` field populated | 1,136 / 1,136 ✓ |

### 4.3 Absence of Structural Issues

| Issue | Count |
|---|---|
| Broken source reference (ASP not in registry) | 0 |
| Broken target reference (ASM not in registry) | 0 |
| Duplicate (source, target) pairs | 0 |
| Circular references | 0 |
| Orphan ASMs (no incoming REL-001) | 0 |

---

## 5. CAP Relationship Status (Phase A)

All 49 CAPs are relationship orphans in Phase A — no CAP is a source or target of any Phase A relationship. This is expected and correct:

- CAP→ASP links (which pack services a capability) are REL-002, Phase B scope.
- CAP→SEC links (which proposal section the capability maps to) are REL-003, Phase B scope.

The absence of CAP relationships in Phase A does not prevent the KVE from validating CAP-level rules (field completeness, BU validity, lifecycle status) — those operate on the asset record, not the graph.

---

## 6. Phase B Relationship Roadmap

When KRPE Phase B is implemented, the following relationship types will be added:

| Rule ID | Type | Direction | Source | Description |
|---|---|---|---|---|
| REL-002 | REF | CAP → ASP | Capability | Capability references assumption pack |
| REL-003 | MAP | SEC → CAP | Section | Proposal section maps to capability |
| REL-004 | REQ | CAP → RSK | Capability | Capability triggers risk |
| REL-005 | MIT | RSK → ASM | Risk | Risk mitigated by assumption |
| REL-006 | USE | CAP → MTH | Capability | Capability uses methodology |
| REL-007 | PAT | CAP → PAT | Capability | Capability instantiates pattern |
| REL-008 through REL-010 | TBD | Various | Various | Additional linkages per architecture |

Phase B will transform the graph from a forest (13 isolated ASP trees) into a connected knowledge graph spanning CAP, ASP, ASM, SEC, RSK, MTH, and PAT nodes.

---

## 7. KVE Readiness Assessment

The Phase A relationship graph is sufficient for KVE Phase A rule execution:

| KVE Rule Category | Phase A Graph Coverage |
|---|---|
| ASM orphan detection | Full — all ASMs have parent_pack_id |
| Pack completeness checks | Full — all 13 packs have ≥1 relationship |
| Pack count validation | Full — declared vs actual via graph degree |
| CAP relationship validation | Deferred — no CAP edges in Phase A |
| Cross-BU linking | Deferred — Phase B |

KVE Phase A can execute all 22 BLOCK conditions using the current registry. The 6 graph-traversal rules that require CAP→ASP edges (REL-002) will be marked as DEFERRED in Phase A KVE execution.

---

## 8. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-27 | WP18E-IMP-B | Initial relationship analysis — Phase A graph |
