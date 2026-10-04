# P8 ranked representation and rational-closure authoring

Bounded independent authoring assignment started 2026-10-03 approximately
17:48 UTC; at most 45 minutes. This is authored, unreviewed work, not admitted
content. Root owns routing, canonical bibliography/symbol/scope integration
and section-ledger disposition. Existing KLM files and all other writers'
files were preserved. No children, reviewers, tests, builds, manuscript
renders, edits to shared drivers/canonical records, or ledger updates.

## Source and actual reading

Primary author posting: Daniel Lehmann and Menachem Magidor, *What does a
conditional knowledge base entail?*, [cs/0202022v1](https://arxiv.org/abs/cs/0202022v1),
submitted 18 February 2002, author PDF 58 pages, held at
`source/references/p08-rational-closure/lehmann-magidor-author-cs-0202022v1.pdf`.
SHA256 `EA0CBC0C384FB8CFB90D6A3C8B0E3CFB52E728F8EC92ED13DEB4EA3F38577F1F`.
PDF header confirms identity; PDF metadata reports Ghostscript regeneration
22 October 2018, which is not the submission or journal publication date.
The posting describes minor corrections of the journal version and separately
lists the journal 55(1), 1992, pp1–60 and the 1994 erratum 68,p411.
Neither exact journal bytes nor the erratum body are held by this packet.
Intake `LehmannMagidor2002Author` remains distinct from canonical
`LehmannMagidor1992`; no title-only merging or final-journal completeness credit.

Read local PDF pp1,5–24,28–44,46–51. Relevant authored intervals are:

- pp5–8: native six-rule P basis, derived S/Cut, full valuation universe,
  model/smoothness and source non-well-founded example.
- pp10–13: consistency, exception operator, transfinite ranks/admissibility.
- pp17–23: Rational Monotonicity, modular/ranked equivalences, rules14–18,
  representation theorem and the distinction between ranked entailment and
  selected rational extension.
- pp29–36: the exact two-condition relation preference, rational closure
  definition and admissible-base selection Theorem7.
- pp38–41: material exception test, finite algorithm, Nixon/penguin and
  generic inheritance limitations.
- pp46–48: all Appendix A canonical representation dependencies.

HTML was additionally consulted at
[versioned author HTML](https://arxiv.org/html/cs/0202022v1).
Windows curl and Invoke-WebRequest failed authentication/TLS initialization;
ordinary Python urllib using its default verified TLS successfully captured
the PDF. There was no security/TLS bypass. Source archive retrieval returned
HTTP406 and was not retried through alternate wrappers. No archive or source
TeX is claimed held. The PDF is the readable mathematical source.

Before writing, read the saved KLM reader and annex in full (a truncated
annex passage was repaired by a bounded reread), its research note, the
nonmonotonic host section, both governing contracts, conventions, the supplied
full-TOC attachment, and the research skill. The research task is already a
bounded background author assignment; parent explicitly forbade children.

## Fifteen complete reciprocal proof pairs

Reader: `handbook/parts/p08/ranked-models-and-rational-closure.tex`.
Annex: `handbook/annex/p08/ranked-models-and-rational-closure.tex`.
All result statuses are proved with a matching body/annex back-reference.

1. `rational-modularity` / `.modularity`: all four source modular-order
   conditions, incomparability quotient and exact definable smoothness.
2. `rational-soundness` / `.soundness`: actual negative-premise witness,
   every conjunction minimum and precise smoothness use.
3. `rational-transport` / `.transport`: classical compact normal witnesses,
   source rules14–18 with supplied proofs, total preorder, quotient
   well-definedness, normality transport, class inequalities and consistency.
4. `rational-canonical-minima` / `.minima`: both directions, inconsistent
   formula empty sets and explicit minimum predecessors.
5. `rational-general-representation` / `.representation`: arbitrary atom-set
   preservation/reflection and actual counterstates; finite logical quotient
   instead of wrongly treating syntactic formula sets as finite.
6. `rational-nonwellfounded` / `.nonwellfounded`: source chain-with-bottom
   model, finite-formula smoothness and obstruction to every well-founded
   representation of its relation.
7. `rational-source-selection` / `.selection`: rationality of the ordinal
   rank criterion, transfinite default retention, inclusion, and both
   preference conditions against every different rational extension.
8. `rational-material-exception` / `.material`: arbitrary-base equivalence,
   actual one-state countermodel, compact finite material support and S.
9. `rational-finite-admissibility` / `.admissibility`: stabilization by n
   deletions and finite disjunction of persistent antecedents; handles
   nonempty stable completely exceptional bases without ordinal-model or
   finite-language assumptions.
10. `rational-finite-realization` / `.realization`: every world's least
    material stage, exact formula minima, base satisfaction, smoothness and
    both directions of the rank criterion, including no-rank omission.
11. `rational-finite-algorithm` / `.algorithm`: every stopping case, actual
    classical exception tests and O(n²) SAT queries; no unwarranted
    unrestricted polynomial-time or infinite-base decision claim.
12. `rational-ranked-intersection` / `.intersection`: explicit two ranked
    models with nonrational relation intersection; finite selected closure
    differs from all-ranked-model entailment.
13. `rational-pointwise-minimum` / `.minimum`: exactly possible labels,
    least-copy compression, finite-layer normalization and full induction
    giving the unique least complete valuation ranking.
14. `rational-penguin-example` / `.penguin`: all eight valuation ranks,
    irrelevant atom case, both nonflying-bird failures and separately
    computed generic-property inheritance failure.
15. `rational-nixon-example` / `.nixon`: both branches at rank1, fresh-atom
    persistence and distinction from a stable contradictory antecedent with
    no states.

The selection proof was initially left source-cited while its difficult
case was being resolved, then replaced coherently with the full annex proof.
In the no-least-competing-layer case it does not assume one fixed witness
is preferred to every missing antecedent. For each missing antecedent xi,
choose the least K-exception rank among competing-consistent formulas at or
below xi's competing layer, then use a strictly lower competing-layer
formula. This gives an actual R-minus-T witness below xi for condition2.
The all-H-inconsistent case is handled separately, and the least-layer case
supplies the upward-copy expansion before cutting a smooth tail.
This is a source-grounded expansion of the construction, not independent
acceptance or a claim to have reconstructed every result in the paper.

## Notation and source distinctions

Native hooked-bar conditional notation and unbarred alpha-sim-beta formula
class equivalence remain distinct. S is the consistent-formula set, unlike
the earlier KLM state-set S. E is a quotient-class set in AppendixA, while
E(K) is the exception operator. State preference and whole-relation
preference reuse prec with explicit distinct domains. Class order and the
formula comparison abbreviation in the closure definition are not collapsed,
especially for inconsistent formulas. Full-universe source validity is not
silently replaced by earlier relative background validity. A hard constraint
delta is represented by not-delta conditionally entails bottom, not a
top-default. All raw intake glyph cells contain actual LaTeX, not ASCII
placeholder names.

The scalar/ordinal h, world function k, proof-local H/T/lambda/Gamma and
incomparability proof notation are explicitly declared, with intakes
recording these as proof/construction names rather than source-native
primitive logical symbols. The pointwise minimum theorem is a justified
construction property, distinct from the source whole-relation preference.

## Integration and continuation

Suggested seam: immediately after the full KLM preferential packet, in the
existing nonmonotonic chapter. It is a subsection, not a new chapter.
The sheet `registry/calculi/p08-rational-closure.tex` is literally included
only after language, model, class comparisons, exception/materialization and
finite realization have been defined. It records six P rules, RM, derived
S/Cut and source14–18, plus the exception test and finite loop procedure.
The added sheet is not treated as a substitute for proofs.

Still open beyond this packet: full source ordering Lemma25 pp29–31 and its
global loop/reciprocity/cumulativity consequences; the arbitrary infinite
base nonexistence example's full renaming proof; rank stability Lemmas5–6;
minimum-extension transformation and full general ranked-equals-preferential
entailment proof; source depth-ranking construction for well-founded
relations and all its standing; Adams and AppendixB nonstandard probability
representations; the remaining C/CL/CM/M source constructions; AGM and
Makinson allocations. Exact journal/erratum manifestations remain separate.
None is credited merely because this packet names or cites it.

No independent review, static checker, build or manuscript render was run.
Saved extents/hashes returned to root are filesystem observations only.

## Frozen author return, 2026-10-03 18:30 UTC

Fifteen body proved declarations and fifteen annex items; 39 typed raw
symbol rows; one new author-version bibliography record; nineteen literal
sheet entries. Reader367 lines, SHA256
`EF05147D6167C05F865BB5A80B3D3CDE65F90AD33FB4B03FD66A939A73CF07C3`.
Annex682 lines, SHA256
`BB600034357E296CDACF5338F65E4E4B49E51AC86E9E9F3E44692C907DD49964`.
The selection proof additionally derives asymmetry directly from preference
conditions1–2, hence uniqueness, without claiming the unsupplied full
transitivity proof. The new intersection example is included exactly once;
a duplicate created while applying the author's own patch was removed by a
fresh-read two-copies-to-one correction. No other content was removed.
These counts and hashes are observations, not a review or acceptance pass.
