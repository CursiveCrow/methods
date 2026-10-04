# P5 checker arithmetization: saved construction and completion handoff

Date: 7 September 2026. Repository: `C:\Dev\the-methods-of-reason`.
This authoring block was assigned at 23:07 UTC with a 45-minute maximum.
The lead's subsequent instruction was to finish this note for the saved files,
return, and stop while the lead prepares the user's completion plan. No further
authoring block was started.

## Exact current status

Two new manuscript files are saved:

- `handbook/parts/p05/pa-checker-arithmetization.tex`, 516 lines,
  SHA-256 `33195DFF4BB6D2D7BD898E0AF9D8EC1980A1272593139624AA17577E132C15F5`.
- `handbook/annex/p05/pa-checker-arithmetization.tex`, 537 lines,
  SHA-256 `03BAF39D646901DC307812B0D22FE8823CFEC53B3D7B85A3FF0ADF754AAF71E5`.

These are authored mathematical constructions awaiting the three independent
reviews and integration gates. They have not been admitted, built, or rendered.
No regression tests, manuscript tests, code generator, executable checker,
subagent, or external source search was used in this authoring block.

The body defines a finite expansion convention for primitive recursive
descriptions: initial functions, composition, primitive recursion, bounded
folds, bounded searches with defaults, list states, fixed-order Boolean cases,
and constructor-pattern expansion. It then specifies the actual cons/list
library, type and variable tables, bounded substitution and alpha machines,
canonical direct axiom recognition, all twenty row rules, parent counts,
surviving open occurrences, and the outer tag-19 checker. The selected formula
is `Prf^19_PA(p,x) := Gamma_d19(p,x,1)`, with `Prv^19_PA(x) := exists p Prf`.
The formation tree is specified through the printed finite expansion rules;
the fully expanded, enormous arithmetic formula is not separately serialized.

The annex supplies proof text for numerical agreement with the existing direct
checker and for internal PA list/table equations. It proves the internal
modus-ponens invariant by row-offset, open-occurrence, parent-count, unchanged
content-call, and direct-axiom-product arguments. It derives D2 for the newly
selected formula and D1 from finite numeral evaluation in PA. These claims have
actual proofs in matching annexitems; they are not inferred solely from the
primitive recursiveness or standard-model values of a numerical operation.

This does not establish the full promised standard-predicate result. D3,
the evidence-to-proof builders, downstream predicate binding, and the relevant
GL proof obligations remain open. The earlier arbitrary numeralwise
representative in Q has not been internally equated with this new Gamma graph.

## Claims supplied in the saved proof text

| Claim | Current status | Principal content |
| --- | --- | --- |
| A fixed finite description of the actual tag-19 checker | Authored; independent verification pending | Definition sequence fixes composition/recursion expansion, raw-list operations and defaults, syntax tables, command arities and machine bounds, induction recognition, all twenty rules, and final tests. |
| Exact arithmetic graph selection from that description | Authored; independent verification pending | `d19` is the expanded formation tree and the selected proof formula is exactly its Gamma graph at output one. This uses the supplied graph-construction fresh-variable convention. Review must confirm that every abbreviation and pattern fixes one expansion. |
| Standard-model proof meaning | Proof supplied; independent verification pending | Numerical identification with the direct checker followed by the established direct PA proof-meaning theorem. |
| Internal PA cons/list/table equations | Proof supplied; independent verification pending | Pair inverse sums, bounded tail descent, length and entry equations, list extensionality, reversal invariant, concatenation equations, map/filter equations, products, and table-prefix induction. |
| Internal sentence condition at implication subformulas | Proof supplied; independent verification pending | Syntax-table equations plus an internal free-index bound imply that both children of a sentence implication are sentences. |
| Internal PA modus ponens and D2 for the selected formula | Proof supplied; independent verification pending | Offset lookup equations; row-by-row preservation of all checks; formula-specific discharge and nonvacuity; FV/all-variable freshness; parent-count equations; and final direct-axiom product. |
| D1 for the selected PA formula | Proof supplied; independent verification pending | A standard successful proof code gives a finite PA graph computation and existential introduction. This is explicitly a PA conclusion. |
| Q numeralwise claims for the previously cited representative | Existing separate dependency | The new construction neither changes that theorem nor infers internal equivalence with its unspecified representative. |
| Evidence-to-proof invariant and D3 | OPEN | The exact remaining formula is stated at the end of the new body and described below. |
| Binding old consumers and GL results to the selected formula | OPEN; lead-owned | Existing selectors/consumers have not been rewritten, and no GL gate is closed. |

## Integration and notation requests for the lead

1. In `handbook/parts/p05.tex`, insert
   `\input{parts/p05/pa-checker-arithmetization}` immediately after the existing
   `\input{parts/p05/standard-pa-proof-predicate}`. The Gamma construction is
   already on the preceding active reader route.
2. In `handbook/annex/p05-route.tex`, insert
   `\input{annex/p05/pa-checker-arithmetization}` after the existing
   `\input{annex/p05/standard-pa-proof-predicate}`. The internal graph/sequence
   proof must remain available before the new annex is invoked.
3. Register the new section and theorem/definition identities through the
   normal projection/intake process. The section is
   `sec:p05-pa-checker-arithmetization`. The theorem identities are
   `thm:p05-selected-direct-pa-graph` and
   `thm:p05-direct-pa-internal-mp`; their annexitems are respectively
   `annex:p5.checker-description` and `annex:p5.checker-internal-mp`.
4. New reader-level notation is `\mathsf{Prf}^{19}_{\PA}`,
   `\mathsf{Prv}^{19}_{\PA}`, `d_{19}`, `\chi_{19}`,
   `\mathsf{mp}_{19}`, and `d_{\rm mp}`. The remaining named arithmetic/list,
   table, syntax, row, and machine functions are local description names,
   expressly eliminated through their particular Gamma graphs. Their local
   typography includes `D,Z,M,L,E,I,h,t,T,V,e`, `\mathsf{range}`,
   `\mathsf{rev}`, `\mathsf{cat}`, `\mathsf{map}`, `\mathsf{filter}`,
   `\mathsf{take}`, `\mathsf{Tm}`, `\mathsf{Fm}`, `\mathsf{AV}`,
   `\mathsf{FV}`, `\mathsf{Sent}`, `\mathsf{ar}`, `\mathsf{ae}`,
   `\mathsf{Ax}_{19}`, `\mathsf{Rows}`, `\mathsf{Tree}`,
   `\mathsf{pc}`, `\mathsf{root}`, `\mathsf{open}`, `\mathsf{sh}`,
   `\mathsf{sr}`, and `\mathsf{SR}`. Shared symbols and bibliography were not
   edited. There are no new external citation keys.
5. Preserve the old numerical unit and existing source artifacts while
   deciding the explicit selector/provenance migration. The old text's
   subsequent-work paragraphs should acquire the correct new cross-reference
   and disposition through the lead's authorized integration work; this
   authoring block did not edit those accepted files.

## Next concrete work and pass/fail conditions

### A. Freeze and independently inspect this exact description and proof

Work distribution: three fresh contexts, with the lead owning the frozen
manifest and admission record. One reviewer checks source/dependency fidelity
against the actual constructor, substitution, and twenty-rule definitions;
one checks the mathematics of the finite descriptions and PA inductions; one
checks the artifact adversarially for unbound notation, undeclared choices,
missing defaults, scope changes, and reader-facing completeness. Each files
before seeing the other conclusions.

Pass: every declared helper has a finite acyclic expansion in initial
functions/composition/primitive recursion; all case orders, argument orders,
bounded machine updates, extraction failures, pattern projections, and Gamma
variable conventions determine the selected formula; the numerical checker
agrees with the inherited rule tests; every internal invariant has valid PA
base/step evidence; and the D2 conclusion uses the selected graph throughout.

Fail: any unnamed helper, circular expansion, unspecified decision procedure,
ambiguous formula selection, missing machine case/bound/default, incorrect row
or discharge order, unsupported internal syntax fact, or use of standard-model
agreement as an internal PA implication. A failure reopens the exact affected
definition/proof and must be repaired before the corresponding claim is
admitted. The current author does not independently accept these files.

### B. Supply numeral and bounded-formula proof builders for the selected checker

Suggested concrete first block: one writer owns new body/annex files for
specified constructors that produce annotated ND proofs of the elementary
numeral arithmetic and bounded literal facts required by the existing evidence
formula. Specify their finite descriptions, actual axiom leaves, term/matrix
parameters, labels, and literal root formulas. Prove PA invariants against
`chi19`, using the saved list and row equations.

Pass: each promised builder has a description and a PA theorem that its
displayed arithmetic evidence implies an accepted tag-19 proof with the exact
required root. Equality, negation, comparison abbreviations, variable names,
temporary assumptions, and zero/empty bounds receive their actual ND cases.

Fail: returning only numerical correctness, an appeal to Q representability,
the truth of a bounded formula, an unspecified proof search, or an abstract
logical proof with no annotated-code constructor and internal checker
invariant. That would leave the evidence-to-proof obligation open.

### C. Complete the fixed-formula evidence-to-proof construction and D3

Suggested following block: one writer owns the structural compiler for each
fixed closed Sigma-1 sentence sigma, using the already supplied exact evidence
clauses. It must compose the builders through conjunction, disjunction,
existential introduction, and marked bounded universal cases, preserving
literal substitutions, all-occurrence eigenvariable freshness, and
formula-specific nonvacuous discharge. The negation-normal-form conversion
back to the original fixed sigma must also have the required exact derivation
and code transport.

The target for each fixed sigma is a specified description `d_sigma` and a
PA proof of

`forall e (Ev_sigma(e) -> exists p (Gamma_d_sigma(e,p) and Prf^19_PA(p,code(sigma))))`.

Pass: every evidence constructor has its actual proof-code operation and PA
invariant; dependent bounded witnesses, zero bounds, and label/name management
are covered. Combine that theorem with the existing PA equivalence
`sigma <-> exists e Ev_sigma(e)`. Instantiate at the literal expanded sentence
`Prv^19_PA(code(phi))` for each fixed phi to obtain D3 for exactly the selected
predicate.

Fail: identifying bounded evidence with an ND derivation, substituting an
arbitrary numeralwise representative, choosing a builder only by its standard
values, silently changing the target formula, or claiming D3 before all
evidence cases and their internal checker obligations pass.

### D. Bind the selected formula and complete downstream obligations

Work distribution: the lead owns old selectors, source correction dispositions,
GL consumers, canonical notation/bibliography, drivers, and provenance. A
separate writer/reviewer may own the still-required GL proof components under
an explicit assignment after the selected-predicate prerequisites are ready.

Pass: each consumer states the actual selected formula and the representation
strength it uses; every old arbitrary-representative use has an explicit
scope-preserving repair; D1, D2, and D3 cited there concern that same literal
predicate. Every promised GL proof component must then be supplied and
independently accepted at its actual scope. Three derivability conditions
alone do not stand in for a separately promised arithmetical-completeness proof.

Fail: transferring internal theorems through the existing external equivalence
of proof existence, treating different serialized code sorts/formulas as
identical, narrowing the original promised standard-predicate result, or
marking GL complete from only the new D1/D2 proof.

### E. Production and admission

After content review and any corrections, the lead runs the scoped static,
build, and rendered-page checks and records separate admission for the exact
frozen source and dependencies. Pass requires all mandatory content reviews
and production evidence for the same versions. Missing review, build, visual,
provenance, or admission evidence remains an explicit open gate.

## Read extents and dependency identities

All paths are relative to `C:\Dev\the-methods-of-reason`. Full-file hashes
identify dependencies even where only a routing excerpt was needed.

| File | Read extent used | SHA-256 |
| --- | --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | Full, 1-168 | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `handbook/parts/p05/standard-pa-proof-predicate.tex` | Full, 1-252; live reread | `71D3E5569BFB7BAE907CA818BE65DBBCE5E48DBA86D9D8942819DCC5110331E2` |
| `handbook/annex/p05/standard-pa-proof-predicate.tex` | Full, 1-315; live reread | `7F3E3F751832ACACFFC8F2383E2AC14A8D8DC7A9DEA2DA4B837F3A9DF648DFDF` |
| `handbook/restoration/inherited-09262-09327.tex` | Full, 1-253 | `B49A3B30AFF36050841D4F384A6BA80FCF36F4661B3C4085E58D2371B4E003CB` |
| `handbook/annex/p05/internal-proof-predicate.tex` | Full, 1-524 | `F11B72E5AE8FF2407C58FA434320D08095C0C543AE8C610237EED42EAFFFA1C1` |
| `handbook/restoration/inherited-09328-09438.tex` | Full, 1-546 in the immediately preceding review in this context; current hash reverified and relevant rule snippets consulted | `A6E37FA592E81B888C14A2DA97CC70F1A05EC69BAE0CE4D36E2E60C59F09C541` |
| `handbook/parts/p05.tex` | Full, 1-53, integration placement | `7E6022FE4FBD9DC5A28554DA88B9B6CEEC02857D51E981AC0CE7171B1FD2E0D6` |
| `handbook/annex/p05-route.tex` | Input matches at 15-16, integration placement | `170038165BD025BCF715B8D2E7479DE6D285E6A0E2F55D02F18847A2D773FAF0` |

The earlier unchanged syntax and ND definitions were available from the full
immediately preceding review in this same context. No other author's new
construction or independent conclusion was used as evidence for accepting this
author's work. Only the two new LaTeX files and this note were written by this
authoring block. The note's own hash is returned separately in the handoff.
