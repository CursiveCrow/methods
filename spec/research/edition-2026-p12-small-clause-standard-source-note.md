# Standard small-clause transformation: completed authoring batch

Date: 9 September 2026. Allocation: HAR2001-C06-G01, the introduction and
Sections 2–3 of Nonnengart and Weidenbach's *Computing Small Clause Normal
Forms*, through the end of Section 3.7 on printed page 347. Section 4 begins
on the same page and belongs to the separately owned optimization treatment.

## Exact source and reading

The retained source was obtained from the DFKI author/institutional address
`https://www.dfki.de/~nonnenga/publications/small.ps.gz`. Its acquisition and
PostScript decompression/render history remain under `tmp/acquisition/src037/`.
The readable source used here is
`dfki-small-clause-retry-01.body.derived-decompressed.ps.derived-render.pdf`:

- 286,434 bytes; 33 physical pages.
- SHA-256 `41EA6003E78E88D20EBE639EF7943F6A4BCC983D8F074D73F41B72C28AA32264`.
- Actual title: *Computing Small Clause Normal Forms*, Andreas Nonnengart
  and Christoph Weidenbach; second readers Thierry Boy de la Tour and Uwe Egly.
- The source title page identifies *Handbook of Automated Reasoning*,
  edited by Alan Robinson and Andrei Voronkov, Elsevier, 2001.
- Chapter pagination is 335–367. The introduction begins at 337;
  the selected standard pipeline ends at 347.

The complete selected text was read from the actual held chapter, using its
page-separated extraction and the existing high-resolution source-page images
where extraction loses mathematical glyphs. The polarity signs, raw renaming,
Skolem rule, quantifier-pulling rules and running-example matrices were checked
against those source images. The local PDF hash was verified again during this
batch. This is a PostScript-rendered source presentation, not a claim of byte
identity with a publisher PDF. No substituted textbook, preview or later edition
supplies the selected proof obligations.

The shared bibliography key is `NonnengartWeidenbach2001SmallClauses`.
The optimization writer supplies that entry in the unique optimization intake,
using the title-page identity and DOI `10.1016/b978-044450813-3/50008-4`.
This writer deliberately supplies no duplicate bibliography record. Root must
merge that shared key before routing the completed pair.

## Completed manuscript files

Body: `handbook/parts/p12/small-clause-standard.tex`.
Annex: `handbook/annex/p12/small-clause-standard.tex`.
Notation intake:
`handbook/registry/symbols-intake-p12-small-clause-standard.csv`.

All thirteen previously promised body results now have complete ordinary proofs
inside their reciprocal `annexitem` environments:

| Body result suffix | Annex suffix | Completed argument |
| --- | --- | --- |
| small-sat-closure | small.sat.closure | Term/formula coincidence, both quantifiers, exact existential closure and an open/universal-closure separation. |
| small-context | small.context | Pointwise Boolean monotonicity/antitonicity, both quantified cases, zero-polarity equivalence and retained background assumptions. |
| small-simplify | small.simplify | All eighteen Boolean and two quantifier schemes, strict tree decrease, irreducibility invariant and logical-constant outputs. |
| small-nnf | small.nnf | Every rewrite's semantic identity and exact decreasing weight, termination and terminal NNF; complete biconditional example. |
| small-miniscope | small.miniscope | All four guarded and two distributive schemes, nonempty-domain uses and a measure that handles duplicated quantifiers. |
| small-renaming | small.renaming | Term induction, every Boolean constructor and both quantifiers for raw renaming injective on occurring variables. |
| small-rectification | small.rectification | Strong induction with exact disjoint fresh-name blocks, unchanged free variables and initially repeated binder names. |
| small-skolem | small.skolem | Nonempty witness fibers and default values, Choice-based expansion, capture-free substitution induction and choice-free reduct. |
| small-cnf | small.cnf | Prefix pulling before distribution, exact measures and terminal shape, plus a premature-distribution obstruction. |
| small-clause-simplify | small.clause.simplify | Universal instance semantics, multiset subsumption, retained witnesses, condensation equivalence, renaming apart and termination. |
| small-pipeline | small.pipeline | Composition of every phase with exact fixed-structure expansion/reduct guarantees and finite signature extension. |
| small-example | small.example | All miniscoping transformations, five fresh binders, both Skolem steps, prefix formation and the correct two clauses. |
| small-failures | small.failures | Explicit finite countermodels for the forbidden quantifier transformations, capture, old-symbol reuse, simultaneous subsumption deletion and the wrong example output. |

Body labels have prefix `thm:p12-`; annex labels have prefix `annex:p12.`.
The existing interfaces `thm:p12-small-context`, `thm:p12-small-sat-closure`
and `thm:p12-small-rectification` remain unchanged for the optimization writer.

## Direct corrections and explicit proof qualifications

The active running example now has the diagonal unit `R(u,u)` and the clause
`P(a) or R(v,f(v)) or Q(w)`. The source's displayed transition on printed
346 and resulting three pairwise clauses on 347 do not follow from its
preceding conjunctive matrix. The body presents the corrected output directly;
the annex supplies the complete derivation. The correction history remains here.
The countermodel uses the two-element domain, off-diagonal R, universal P and Q,
constant a=0 and swapping f. All three wrong clauses hold while the diagonal
unit fails. Adding universally negative diagonal R makes the original sentence
inconsistent while that wrong output remains satisfiable.

The miniscoping sum is a **nonnegative** integer, with zero for a quantifier-free
formula. A positive-only description has been removed. The proof tracks changes
to the selected quantifier contributions and every other quantifier's scope.
The NNF proof uses an explicit strictly monotone weight that handles duplication;
an informal count of connectives alone is insufficient for arbitrary nested
biconditionals. CNF formation uses an explicit two-phase schedule, first pulling
the universal prefix and then distributing the matrix, so no duplicated binder
names can defeat a later side condition.

Raw renaming is injective on the occurring-variable set. It is not incorrectly
required to be an injective identity-extension on the entire variable alphabet.
The indexed algorithm's induction includes the case where its temporary raw
renaming reuses an outer fresh name at an inner original binder; the recursive
call then gives the inner binder its own new name. Both quantifier branches are
written in full.

The source's freshness relative to the formula is strengthened explicitly to
freshness outside the declared current signature for the stronger fixed-model
expansion theorem. Choice is an explicit assumption for simultaneous witness
selection over arbitrary nonempty parameter fibers. The reverse implication
does not use Choice. Open-input satisfiability uses existential closure of
exactly the free variables. A stipulated universal closure is a different input.
These qualifications are stated in the active body, not left as repair requests.

## Author read-through and bounded calculations

A full author read-through of the actual completed body and annex was performed.
One direct structural extraction found thirteen body proved targets, thirteen
annex items, thirteen ordinary annex proofs, zero ordinary body proofs, and a
matching reciprocal body/annex pair for every result. No shared checker or new
software test framework was added.

A one-off finite calculation enumerated all 256 interpretations of unary P,
unary Q and binary R on a two-element domain. The original example was true
in 64 interpretations. In every interpretation it agreed with the miniscoped
sentence and with existence of an interpretation of the new constant/unary
function satisfying the corrected clause pair. There were zero disagreements.
The explicit off-diagonal countermodel separately evaluated the original as
false, all three wrong clauses as true and the negative diagonal clause as true.
This finite calculation supports the example and is not substituted for the
general proofs in the annex.

## Remaining work and ownership boundary

No promised G01 proof is left unwritten in this pair. The 33-page chapter as a
whole is not claimed complete: optimization Groups G02–G05 have a separate
writer and separate source extents. Root owns driver routing, shared-key
bibliography integration and canonical symbol-registry integration. The source
note and notation intake remain as evidence after any integration.

Consolidated independent source/mathematical/publication reviews, the relevant
final static/build checks and manuscript output inspection remain required
after the full authoring/correction batch. No manuscript build or render and
no independent acceptance review was run for this change.
