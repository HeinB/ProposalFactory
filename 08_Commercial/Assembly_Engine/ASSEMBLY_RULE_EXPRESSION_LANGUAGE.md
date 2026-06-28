---
document_id: ASSEMBLY-RULE-EXPRESSION-LANGUAGE-V1
title: "Assembly Rule Expression Language (AREL) — Specification V1.0"
version: "1.0"
status: "FROZEN"
created: "2026-06-28"
created_by: "WP19B — Assembly Rule Expression Language Specification"
approved_by: "Architecture — WP19B"
approved_date: "2026-06-28"
approved_for_reuse: true
category: "Assembly Engine / Expression Language"
scope: "Defines the complete, frozen grammar for the Assembly Rule Expression Language (AREL) — the domain-specific language used in mandatory_if, optional_if, and excluded_if fields in the Knowledge Asset Registry. Specifies syntax, operators, context variable vocabulary, null handling, precedence, and determinism guarantee."
governing_standard: "KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md V1.0"
related_documents:
  - KNOWLEDGE_ASSET_REGISTRY_SCHEMA.md
  - KNOWLEDGE_VALIDATION_ENGINE.md
  - VALIDATION_RULE_EXECUTION_MODEL.md
  - ASSEMBLY_RULE_VALIDATION_STANDARD.md
  - ASSEMBLY_RULE_TEST_SUITE.md
---

# Assembly Rule Expression Language (AREL) — Specification V1.0

**Work Package:** WP19B  
**Status:** FROZEN — Grammar is locked before large-scale rule population. Changes require ADR amendment.  
**Governs:** All `mandatory_if`, `optional_if`, `excluded_if` fields in the Knowledge Asset Registry.

---

## 1. Purpose

AREL is the single, deterministic expression language used by the Knowledge Validation Engine to evaluate assembly rules against a tender context. It replaces the unsafe Python `eval()` approach used in KVE Phase A with a formally specified, sandboxed, purpose-built language.

**AREL is intentionally minimal.** It covers exactly the vocabulary needed to express capability, assumption pack, and risk assembly rules for tender proposals. It does not support arithmetic, string manipulation, function calls, or imperative logic.

**Every AREL expression must be evaluable by a deterministic evaluator.** Given the same expression and the same context, the result is always identical — no randomness, no date sensitivity (except where the `tender_date` variable is explicitly used), no side effects.

---

## 2. Design Principles

1. **Minimal surface area.** Include only what is needed. The grammar is intentionally small to keep rule authoring simple and evaluation deterministic.
2. **Safe failure.** Any reference to an undefined context variable evaluates to `false`, not an error. Rules that cannot be resolved never accidentally enable features.
3. **No Python leakage.** AREL is not Python. Expressions that happen to be valid Python but are not valid AREL are rejected. Single-quoted strings, `=` (single equals), `[0]` indexing, and method calls are all invalid.
4. **Double-quotes only.** All string literals use double quotes. Single quotes are a syntax error.
5. **Lowercase keywords.** Logical operators (`and`, `or`, `not`) and comparison operators (`in`, `not in`, `contains`) are lowercase. The evaluator is case-sensitive for these keywords.
6. **Unconditional shorthands.** `TRUE` and `FALSE` (uppercase, no quotes) are reserved shorthands meaning "always include" and "always exclude", respectively. They are backward-compatible with existing registry entries.
7. **Empty means false.** An empty string `""` evaluates to `false`. This is the correct behaviour for `mandatory_if` (not mandatory by default) and `excluded_if` (not excluded by default).

---

## 3. Grammar — Formal BNF

```
expression      ::= "TRUE"
                  | "FALSE"
                  | or_expr

or_expr         ::= and_expr
                  | or_expr WS "or" WS and_expr

and_expr        ::= not_expr
                  | and_expr WS "and" WS not_expr

not_expr        ::= "not" WS not_expr
                  | atom

atom            ::= "(" WS? expression WS? ")"
                  | comparison

comparison      ::= operand WS "==" WS operand
                  | operand WS "!=" WS operand
                  | operand WS ">"  WS operand
                  | operand WS ">=" WS operand
                  | operand WS "<"  WS operand
                  | operand WS "<=" WS operand
                  | operand WS "in" WS list_literal
                  | operand WS "not" WS "in" WS list_literal
                  | variable WS "contains" WS scalar_literal

operand         ::= variable
                  | string_literal
                  | number_literal
                  | boolean_literal

list_literal    ::= "[" WS? "]"
                  | "[" WS? scalar_literal ( WS? "," WS? scalar_literal )* WS? "]"

scalar_literal  ::= string_literal
                  | number_literal
                  | boolean_literal

string_literal  ::= '"' character* '"'
number_literal  ::= "-"? digit+ ( "." digit+ )?
boolean_literal ::= "true" | "false"

variable        ::= alpha ( alpha | digit | "_" )*
alpha           ::= [a-zA-Z]
digit           ::= [0-9]
character       ::= any Unicode character except '"' and unescaped newline
WS              ::= ( " " | "\t" )+
```

**Pre-parse check:** Before applying the grammar, the evaluator trims leading and trailing whitespace from the expression string. If the result is empty, the expression evaluates to `false` immediately (no grammar parsing needed).

---

## 4. Operator Reference

### 4.1 Comparison Operators

| Operator | Applies To | Meaning | Example |
|---|---|---|---|
| `==` | scalar == scalar | Exact equality (case-sensitive) | `engagement_type == "AMS"` |
| `!=` | scalar != scalar | Exact inequality (case-sensitive) | `country != "ZA"` |
| `>` | number > number | Strictly greater than | `project_duration_months > 12` |
| `>=` | number >= number | Greater than or equal | `project_duration_months >= 6` |
| `<` | number < number | Strictly less than | `project_duration_months < 24` |
| `<=` | number <= number | Less than or equal | `project_duration_months <= 36` |
| `in` | scalar in [list] | Scalar is a member of the literal list | `platform in ["Oracle HCM Cloud", "Oracle ERP Cloud"]` |
| `not in` | scalar not in [list] | Scalar is not in the literal list | `engagement_type not in ["AMS", "Managed Services"]` |
| `contains` | list_var contains scalar | List variable contains the scalar value | `modules contains "Oracle Recruiting Cloud"` |

**Rules for comparison operators:**
- `>`, `>=`, `<`, `<=` apply only to numeric operands. If either operand is non-numeric, the expression is a semantic error (evaluates to `false`; see §7).
- `==` and `!=` on list-type variables are semantic errors (evaluates to `false`).
- Chained comparisons (`a < b < c`) are not supported. They will parse as `(a < b) < c`, which is a semantic error.

### 4.2 Logical Operators

| Operator | Arity | Precedence | Meaning |
|---|---|---|---|
| `not` | Unary prefix | Highest | Logical negation |
| `and` | Binary infix | Middle | Logical conjunction (both must be true) |
| `or` | Binary infix | Lowest | Logical disjunction (either must be true) |

**Short-circuit behaviour:** `and` short-circuits on the first `false` operand; `or` short-circuits on the first `true` operand. However, because AREL has no side effects, short-circuit behaviour does not change the result — it is noted here for evaluator implementors only.

### 4.3 Special Forms

| Form | Evaluates To | Notes |
|---|---|---|
| `TRUE` | `true` | Reserved keyword — always include. Uppercase required. |
| `FALSE` | `false` | Reserved keyword — always exclude. Uppercase required. |
| `""` (empty string) | `false` | Empty expression — not mandatory / not excluded. Pre-parse shortcut. |
| `true` | `true` | Boolean literal — context-independent truth |
| `false` | `false` | Boolean literal — context-independent false |

---

## 5. Operator Precedence

Precedence from highest (binds tightest) to lowest (binds loosest):

| Level | Operator(s) | Associativity |
|---|---|---|
| 1 (highest) | `(` `)` — grouping | N/A |
| 2 | `not` — unary prefix | Right-to-left |
| 3 | `==`, `!=`, `>`, `>=`, `<`, `<=`, `in`, `not in`, `contains` — comparisons | Non-associative |
| 4 | `and` | Left-to-right |
| 5 (lowest) | `or` | Left-to-right |

**Implication:** `a or b and c` parses as `a or (b and c)`. Use parentheses whenever precedence is not obvious.

**Comparison operators are non-associative.** `a == b == c` is a syntax error. Write `a == b and b == c` if you need both comparisons.

---

## 6. Context Variable Vocabulary

The following variables are available in every AREL evaluation context. Variables are populated from the `tender_context.yaml` file produced by the Tender Intelligence Layer (TIL).

### 6.1 Core Variables (implemented in KVE Phase A)

| Variable | Type | Allowed Values | Source |
|---|---|---|---|
| `pattern` | string | `"P1"` … `"P13"` | `tender_context.pattern` |
| `platform` | string | See §6.3 | `tender_context.platform` |
| `engagement_type` | string | `"Implementation"` / `"AMS"` / `"Managed Services"` | `tender_context.engagement_type` |
| `modules` | list of string | See §6.4 | `tender_context.modules` |
| `country` | string | ISO 3166-1 alpha-2; `"RSA"` is a synonym for `"ZA"` | `tender_context.country` |
| `client_size` | string | `"SME"` / `"Enterprise"` / `"Government"` | `tender_context.client_size` |
| `client_sector` | string | `"Government"` / `"Private"` / `"Financial Services"` / `"All"` | `tender_context.client_sector` |

### 6.2 Extended Variables (available in KVE Phase B and AREL authoring)

These variables extend the context when the TIL Block G fully populates the tender context. Expressions using these variables are valid AREL syntax; if the variable is absent from the context at runtime, the expression safely evaluates to `false`.

| Variable | Type | Allowed Values | Source |
|---|---|---|---|
| `industry` | string | `"Mining"` / `"Financial-Services"` / `"Retail"` / `"Manufacturing"` / `"Healthcare"` / `"Government"` / `"Education"` / `"Telecommunications"` / `"Other"` | `tender_context.industry` |
| `bom` | list of string | BOM trigger IDs e.g. `["BOM-1", "BOM-6"]` | `tender_context.bom_triggers` |
| `payroll_integration` | boolean | `true` / `false` | `tender_context.payroll_integration` |
| `oci_in_scope` | boolean | `true` / `false` | `tender_context.oci_in_scope` |
| `client_has_oic` | boolean | `true` / `false` | derived: `"OIC" in tender_context.oracle_products` |
| `dr_in_scope` | boolean | `true` / `false` | `tender_context.dr_in_scope` |
| `security_in_scope` | boolean | `true` / `false` | `tender_context.security_in_scope` |
| `migration_scope` | boolean | `true` / `false` | derived: `tender_context.migration_scope == "YES"` |
| `integration_scope` | boolean | `true` / `false` | derived: `tender_context.integration_scope == "YES"` |
| `support_scope` | boolean | `true` / `false` | derived: `tender_context.support_scope == "YES"` |
| `pricing_type` | string | `"Fixed-Price"` / `"T&M"` / `"Retainer"` / `"Hybrid"` | `tender_context.pricing_type` |
| `project_duration_months` | number | positive integer | `tender_context.project_duration_months` |

### 6.3 Canonical Platform Values

The `platform` variable contains the tender-level platform, not the asset-level platform. These are the canonical string values:

| Value | Meaning |
|---|---|
| `"Oracle HCM Cloud"` | Oracle Fusion HCM — any HCM module scope |
| `"Oracle ERP Cloud"` | Oracle Fusion ERP — Financials, Procurement, PPM |
| `"Oracle EBS"` | Oracle E-Business Suite (any version) |
| `"Oracle Integration Cloud"` | Oracle Integration Cloud (standalone OIC engagement) |
| `"Acumatica"` | Acumatica ERP (any module scope) |
| `"BeBanking"` | BeBanking H2H platform |

**Note on kve_engine.py:** The current Phase A implementation has `VALID_PLATFORMS = {"Oracle HCM Cloud", "Oracle Fusion ERP", "Acumatica", "BeBanking"}`. This set must be updated in Phase B to the canonical set above. Existing ARM-IT045 context (`platform: "Oracle HCM Cloud"`) is already correct.

### 6.4 Canonical Module Values

The `modules` list contains the modules in scope for this tender. Canonical values:

| Module String | Platform |
|---|---|
| `"Oracle HCM Core"` | Oracle HCM Cloud |
| `"Oracle Absence Management"` | Oracle HCM Cloud |
| `"Oracle Journeys"` | Oracle HCM Cloud |
| `"Oracle Recruiting Cloud"` | Oracle HCM Cloud |
| `"Oracle Learning Cloud"` | Oracle HCM Cloud |
| `"Oracle Talent Management"` | Oracle HCM Cloud |
| `"Oracle Workforce Compensation"` | Oracle HCM Cloud |
| `"Oracle AI Skills"` | Oracle HCM Cloud |
| `"Oracle Payroll Interface"` | Oracle HCM Cloud |
| `"Oracle Fusion Financials"` | Oracle ERP Cloud |
| `"Oracle Fusion Procurement"` | Oracle ERP Cloud |
| `"Oracle PPM"` | Oracle ERP Cloud |
| `"Oracle EBS Finance"` | Oracle EBS |
| `"Oracle EBS HRMS"` | Oracle EBS |
| `"Oracle Integration Cloud"` | Cross-Platform |
| `"Acumatica Financials"` | Acumatica |
| `"Acumatica Distribution"` | Acumatica |
| `"Acumatica Manufacturing"` | Acumatica |
| `"Acumatica CRM"` | Acumatica |
| `"BeBanking Supplier Payments"` | BeBanking |
| `"BeBanking Payroll Payments"` | BeBanking |
| `"BeBanking Forex"` | BeBanking |

---

## 7. Null / Unknown Variable Handling

**Rule:** If a context variable referenced in an expression is absent from the context (null, undefined, or not populated), **every comparison that references that variable evaluates to `false`**, regardless of the operator.

This applies to all operators: `==`, `!=`, `>`, `>=`, `<`, `<=`, `in`, `not in`, `contains`.

| Expression | Context state | Result |
|---|---|---|
| `industry == "Mining"` | `industry` absent | `false` |
| `industry != "Mining"` | `industry` absent | `false` |
| `industry in ["Mining", "Manufacturing"]` | `industry` absent | `false` |
| `modules contains "Oracle Recruiting Cloud"` | `modules` absent | `false` |
| `payroll_integration == true` | `payroll_integration` absent | `false` |

**Rationale:** Safe failure. An undefined variable must never silently enable a mandatory asset or silently disable an exclusion. When the context is incomplete, the conservative (false) outcome is always correct.

**Consequence for `!=` and `not in`:** `!=` and `not in` with a null variable also return `false`, not `true`. Rule authors must not write `industry != "Other"` as a shorthand for "industry is one of our known values" — the intent should be expressed with an explicit `in` list instead.

---

## 8. Type System

AREL has three scalar types and one collection type:

| Type | Description | Variables | Literals |
|---|---|---|---|
| string | Unicode string, case-sensitive | `pattern`, `platform`, `engagement_type`, `country`, `client_size`, `client_sector`, `industry`, `pricing_type` | `"Oracle HCM Cloud"`, `"P1"` |
| number | Signed decimal number | `project_duration_months` | `12`, `36`, `0.5` |
| boolean | True or false | `payroll_integration`, `oci_in_scope`, `client_has_oic`, `dr_in_scope`, `security_in_scope`, `migration_scope`, `integration_scope`, `support_scope` | `true`, `false` |
| list | Ordered collection of scalars | `modules`, `bom` | `["A", "B"]`, `[1, 2]` |

**Type rules:**
- `>`, `>=`, `<`, `<=` require both operands to be numeric type. If either operand is not a number (including a variable that resolves to a string), the expression evaluates to `false` at runtime and flags a semantic warning at validation time.
- `==` and `!=` require both operands to be the same scalar type. String-to-number or string-to-boolean comparisons evaluate to `false`.
- `in` and `not in` require the left operand to be a scalar and the right operand to be a list literal. The list elements must be the same type as the left operand.
- `contains` requires the left operand to be a list-typed variable and the right operand to be a scalar literal of the matching element type.
- Lists are not comparable with `==` or `!=`.

---

## 9. Reserved Keywords

The following identifiers are reserved and may not be used as variable names:

```
TRUE  FALSE  true  false  and  or  not  in  contains
```

---

## 10. Expression Examples

The following examples demonstrate all AREL constructs. These serve as the canonical set for implementors and rule authors.

### 10.1 Simple Equality

```
platform == "Oracle HCM Cloud"
engagement_type == "AMS"
country == "ZA"
pattern == "P13"
```

### 10.2 Inequality

```
platform != "BeBanking"
pricing_type != "T&M"
```

### 10.3 Membership in List

```
platform in ["Oracle HCM Cloud", "Oracle ERP Cloud"]
industry in ["Mining", "Manufacturing"]
pattern in ["P1", "P2", "P3"]
engagement_type not in ["AMS", "Managed Services"]
```

### 10.4 List Contains Element

```
modules contains "Oracle Recruiting Cloud"
modules contains "Oracle Workforce Compensation"
bom contains "BOM-6"
```

### 10.5 Numeric Comparison

```
project_duration_months > 12
project_duration_months >= 24
project_duration_months <= 36
```

### 10.6 Boolean Variables

```
payroll_integration == true
oci_in_scope == true
client_has_oic == false
migration_scope == true
```

### 10.7 Logical Operators

```
platform == "Oracle HCM Cloud" and engagement_type == "Implementation"
platform == "Oracle HCM Cloud" or platform == "Oracle ERP Cloud"
not engagement_type == "AMS"
```

### 10.8 Complex Expressions

```
platform == "Oracle HCM Cloud" and engagement_type == "Implementation" and modules contains "Oracle Workforce Compensation" and industry == "Mining"
```

```
(platform == "Oracle HCM Cloud" or platform == "Oracle ERP Cloud") and engagement_type == "Implementation"
```

```
platform in ["Oracle HCM Cloud", "Oracle ERP Cloud"] and payroll_integration == true and country == "ZA"
```

```
modules contains "Oracle Recruiting Cloud" and not engagement_type == "AMS"
```

### 10.9 Unconditional Forms

```
TRUE
FALSE
```

### 10.10 Pattern Matching for Non-AMS Proposals

```
pattern != "P13"
engagement_type not in ["AMS", "Managed Services"]
```

---

## 11. Forbidden Patterns

The following patterns look syntactically like AREL but are **invalid** and must be rejected by the AREL validator:

| Forbidden Pattern | Reason | Valid Alternative |
|---|---|---|
| `platform = "Oracle HCM Cloud"` | Single `=` is not a valid AREL operator | `platform == "Oracle HCM Cloud"` |
| `platform IN ['Oracle HCM Cloud']` | Single-quoted strings; uppercase `IN` | `platform in ["Oracle HCM Cloud"]` |
| `engagement_type = 'AMS'` | Single `=` and single quotes | `engagement_type == "AMS"` |
| `a == b == c` | Chained comparison | `a == b and b == c` |
| `"Oracle HCM Cloud" == platform` | Literal on left of comparison | `platform == "Oracle HCM Cloud"` |
| `modules[0] == "CoreHR"` | Index access not supported | `modules contains "CoreHR"` |
| `len(modules) > 3` | Function calls not supported | Use explicit `modules contains` checks |
| `platform.startswith("Oracle")` | Method calls not supported | `platform in ["Oracle HCM Cloud", "Oracle ERP Cloud", "Oracle EBS", "Oracle Integration Cloud"]` |
| `engagement_type == AMS` | Unquoted string literal | `engagement_type == "AMS"` |

**Note on `TRUE` / `FALSE` case:** `True`, `False`, `true`, `false` (mixed case) are boolean literals. `TRUE` and `FALSE` (fully uppercase, no quotes) are unconditional shorthands. `"TRUE"` and `"FALSE"` (quoted) are string literals that evaluate `false` as an expression (they are not the shorthands).

---

## 12. Operator Restriction: Left-Hand Variable Convention

For `==`, `!=`, `>`, `>=`, `<`, `<=`: the **left operand must be a variable** and the right operand must be a literal. The reverse (`"P1" == pattern`) is syntactically valid AREL but semantically ambiguous and is rejected by the AREL validator (ARVAL-006).

For `in` and `not in`: the left operand must be a variable or scalar literal; the right operand must be a list literal.

For `contains`: the left operand must be a list-typed variable; the right operand must be a scalar literal.

---

## 13. Evaluator Integration Contract

The AREL evaluator must satisfy these requirements before it may be used in production:

1. **Deterministic:** Same expression + same context → always same boolean result.
2. **Safe failure:** Any parse error, type mismatch, or undefined variable → `false` (never an exception propagated to the caller).
3. **No side effects:** Evaluation must not modify the context, the registry, or any global state.
4. **Sandboxed:** The evaluator must not execute arbitrary code. Python `eval()` with `__builtins__: {}` is insufficient — the production evaluator must use a purpose-built parser (e.g. `lark`, `pyparsing`, or hand-written recursive descent).
5. **Timeout:** Expression evaluation must complete within 100ms for any valid expression. Infinite loops are impossible given the grammar; this is a belt-and-braces requirement.
6. **Character encoding:** Expressions are UTF-8. String comparisons are byte-for-byte (case-sensitive).

---

## 14. Versioning and Change Control

AREL V1.0 is **FROZEN**. The grammar defined in this document governs all registry entries as of the date of freeze. Changes to the grammar require:
1. A new ADR (Architecture Decision Record) documenting the rationale.
2. A version bump to this document (V1.x for backward-compatible additions; V2.0 for breaking changes).
3. A migration pass over existing registry entries if any existing expressions become invalid.
4. An update to ASSEMBLY_RULE_VALIDATION_STANDARD.md and ASSEMBLY_RULE_TEST_SUITE.md.

**No breaking changes to AREL V1.0 may be made without BU Lead approval.**

Backward-compatible additions (V1.x) may add:
- New context variables (new entries in §6)
- New list-typed comparisons

Breaking changes (V2.0) include:
- Removing operators or keywords
- Changing null/unknown handling
- Changing operator precedence
- Renaming context variables

---

## 15. Amendment History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-06-28 | WP19B | Initial frozen specification — grammar, operators, context vocabulary, null handling, type system, examples, forbidden patterns |
