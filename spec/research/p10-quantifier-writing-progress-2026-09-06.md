# Quantifier adjunctions and contextual first-order semantics

Date: 6 September 2026 Pacific time.

The actual Part X host and annex now include doctrine-quantifiers,
powerset-quantifiers, and first-order-categorical-semantics.
The contextual-first-order calculus sheet is included in Part X and
in the Part XIV rule catalogue.

## Ten complete proof pairs

| Body result | Annex proof |
| --- | --- |
| thm:p10-doctrine-quantifier-laws | annex:p10.quant.1 |
| thm:p10-doctrine-frobenius | annex:p10.quant.2 |
| thm:p10-doctrine-equality-laws | annex:p10.quant.3 |
| thm:p10-doctrine-inhabited | annex:p10.quant.4 |
| thm:p10-powerset-adjunctions | annex:p10.quant-set.1 |
| thm:p10-powerset-base-change | annex:p10.quant-set.2 |
| thm:p10-powerset-equality | annex:p10.quant-set.3 |
| thm:p10-doctrine-substitution | annex:p10.quant-fol.1 |
| thm:p10-doctrine-soundness | annex:p10.quant-fol.2 |
| thm:p10-doctrine-tarski | annex:p10.quant-fol.3 |

The general treatment states the precise indexed Heyting-algebra
convention, projection adjoints, both parameter-product
Beck--Chevalley identities, and the full parameterized equality
adjunction. It proves quantifier order laws, Frobenius from
implication preservation, reflexivity/replacement/symmetry/transitivity
and arrow congruence, and the inhabited-sort condition needed to
reflect predicate order along context extension.

The powerset example treats arbitrary set maps. Its proofs include
both adjunctions, identity and composition laws, Boolean duality,
unions and intersections including empty families, both base-change
identities for arbitrary pullbacks, automatic comparisons and strict
counterexamples for merely commuting squares, and parameterized
diagonal equality. The empty set and empty fibres are retained.
No family of witnesses is selected.

The contextual language distinguishes sorted variable contexts,
finite hypothesis lists, external term-equation judgments, and
internal equality formulas. The sheet has 27 rule rows: all 25
primitive schemes in Pitts's Figures 1, 2, 3, 5, and 7, plus two
explicit theory-axiom leaves. Its source attribution appears on the
sheet itself.

The full semantic proofs cover term/formula substitution, both
quantifier Beck--Chevalley steps, every displayed rule, arbitrary
sets of theory axioms, and agreement with finite-assignment
Tarskian semantics. Products retain their leading terminal factors.
The abstract inhabitance result concerns predicate sequents;
surjective Set projections separately reflect equality of term
functions in the nonempty-sort comparison.

## Source fidelity and mathematical review

The primary source packet is
p10-quantifier-adjunctions-source-note-2026-09-06.md.
Pitts1995Draft is the inspected 18 May 1995 manuscript; its
sections 5.2--5.6 supply the precise posetal assumptions and
contextual calculus. Lawvere2006AdjointnessReprint identifies
the authorized revised 2006 reprint of the 1969 article.
The original printing's layout was not acquired. The source's
category-valued convention is explicitly distinguished from
the selected Pitts-based posetal convention.

Independent actual-text reviews:

- p10-doctrine-quantifiers-review-2026-09-06.md;
- p10-powerset-quantifiers-review-2026-09-06.md;
- p10-first-order-categorical-review-2026-09-06.md;
- p10-contextual-first-order-source-review-2026-09-06.md.

The first-order reviewer found an overbroad abstract context-removal
claim. The theorem and proof now restrict that abstract statement to
predicate sequents and separately prove reflection of term-function
equality for nonempty Set interpretations.

The source reviewer identified an introduced binder notation.
The actual syntax, calculus, interpretation, and substitution proof
now use Pitts's printed quantifier forms and metalevel abstraction
convention. The header defines application of an abstraction using
its body. The source's implicit well-sorted witness condition for
existential introduction is explicitly displayed and disclosed;
the sheet is not described as a verbatim copy of the printed fractions.
Every repair was read back. The four bounded reviews now pass within
their respective scopes.

## Integration and navigation

The actual Part X annex route was recounted at 72 proof items:
the previous 62 plus these ten.
The existing Part X generator produced 141 theorem/definition rows.
The existing named-theorem generator supplied the ten new index
rows as a scoped update. Twenty-three notation rows were added,
and the existing symbol formatter regenerated both tables with
835 registry rows. The scoped whitespace check passed.

The per-part record is
manuscript-completion-status-2026-09-06.md.
These proof counts do not establish a count of completed register
requirements or an overall manuscript percentage.

## Next source material and remaining work

Pitts's alternative adjoint-rule presentations in Figures 4, 6, and 8
have since been displayed and supplied with full syntactic
interderivability proofs, including variable-dependent antecedents
in Figure 8 and the separate parameter-free equality variant.
See p10-adjoint-presheaf-writing-progress-2026-09-06.md.

The presheaf-topos source packet is ready at
p10-presheaf-topos-source-note-2026-09-06.md.
It includes an acquired and edition-verified Mac Lane--Moerdijk 1992
scan, the author-hosted Moerdijk--van Oosten 2007 lecture notes,
and Lawvere's original-layout Quantifiers and Sheaves article.
The presheaf construction has since been integrated in that same
writing continuation. Its internal logic and precisely scoped
forcing semantics remain the next development.

That research also verified that Quantifiers and Sheaves was
published in 1971 in the proceedings of the 1970 conference.
The bibliography's stable Lawvere1970 key now has publication year
1971 and event year 1970.

The supplied first-order proofs do not establish a full reconstruction
of every separately registered categorical source, completeness of
every doctrine presentation, whole-Part-X fulfillment, or whole-book
publication readiness. Other algebraic and philosophical treatments,
complete requirement reconciliation, and final production remain.

No software tests, manuscript build, or manuscript-page renders were
used in this writing. The saved PDF is still the 18 August artifact.
The full manuscript goal remains active.
