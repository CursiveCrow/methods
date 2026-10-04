# Categorical foundations and the typed internal language

Date: 6 September 2026 Pacific time.

The active Part X body and proof annex now include categorical-toolkit,
cartesian-lambda, and internal-cartesian-language. The formerly brief
category/adjunction paragraph and cited-only Yoneda statement have
been developed into complete definitions and proofs. The imprecise
assertion that an arbitrary interpreted category is recovered by bare
beta-eta syntax has been replaced directly by the two correctly
specified constructions.

## Twelve integrated proof pairs

| Body result | Annex proof |
| --- | --- |
| thm:p10-limits-unique | annex:p10.cat.1 |
| thm:p10-limits-products-equalizers | annex:p10.cat.2 |
| thm:p10-yoneda | annex:p10.cat.3 |
| thm:p10-adjunction-data | annex:p10.cat.4 |
| thm:p10-adjoint-preservation | annex:p10.cat.5 |
| thm:p10-exponential-adjunction | annex:p10.cat.6 |
| thm:p10-stlc-equational-substitution | annex:p10.lambda.1 |
| thm:p10-stlc-context-ccc | annex:p10.lambda.2 |
| thm:p10-stlc-ccc-completeness | annex:p10.lambda.3 |
| thm:p10-internal-ccc-comparisons | annex:p10.internal.1 |
| thm:p10-internal-ccc-equivalence | annex:p10.internal.2 |
| thm:p10-internal-ccc-structure | annex:p10.internal.3 |

The elementary toolkit defines categories, functors, natural
transformations, equivalence, cones/cocones and their universal
properties, products/coproducts, equalizers/coequalizers,
pullbacks/pushouts, monomorphisms/epimorphisms, adjunctions,
and cartesian closure. The proofs include both general small-diagram
constructions, their finite and empty cases, Set tuple and quotient
models, both Yoneda maps and naturalities, full faithfulness of
representables, both directions of the unit/counit theorem, both
adjoint preservation arguments, and the exponential functor and
adjunction. Set and Heyting-order examples are proved.

The typed-language construction retains the registered arrow-only
syntax. It introduces typed beta-eta equality separately, proves
capture-avoiding simultaneous substitution in full, and forms a
category of finite type lists with term tuples as arrows.
Empty contexts give a terminal object and concatenation gives
products. Curried-list exponentials require no product or unit
type constructor. The generic syntactic interpretation proves
equality completeness without using a normalization theorem.

The named internal language is a different signature for a small
CCC with given universal constructions. It includes the full true
equational diagram. Recursive type comparisons and context
packing/unpacking give an explicit evaluation equivalence, natural
quasi-inverse, both triangles, and product/exponential comparison
isomorphisms. General context interpretations retain their leading
terminal factor. No assertion of effective axiomatizability of an
arbitrary category's full diagram is made.

## Primary sources

Pitts1995Draft identifies the author manuscript dated 18 May 1995,
UCAM-CL-TR-367, independently of the later published chapter.
Its sections 3.3 and 4.2--4.4 support the context and function-type
constructions; section 4.3 supplies the full-diagram reconstruction.
Section 4.4, p. 38, expressly supports arrow-only curried-list
exponentials.

Riehl2026ContextOnline identifies the acquired author-hosted
second-edition text. No unverified printed publication date is
assigned. Its exact source locators for Yoneda, universal
constructions, adjunction data, and preservation by adjoints were
checked against that version, rather than against the 2016 edition.

The held exact editions of Mac Lane, Awodey, Lambek, and
Lambek--Scott were not identified by the scoped source investigation.
The new proofs and citations do not establish separate full
reconstructions of those unread source presentations.

Sources and verification are recorded in:

- p10-categorical-source-note-2026-09-06.md;
- p10-categorical-source-verification-2026-09-06.md.

## Direct mathematical review

Independent reviewers read the actual LaTeX in four bounded scopes:

- p10-categorical-limits-yoneda-review-2026-09-06.md;
- p10-categorical-adjunction-review-2026-09-06.md;
- p10-cartesian-lambda-review-2026-09-06.md;
- p10-internal-cartesian-language-review-2026-09-06.md.

The first-half review found a universe-size error: a large family
of natural transformations being parametrized by a small set does
not put each complete component family inside the smaller universe.
The statement and proof now give the exact canonical bijection,
without the invalid universe-membership conclusion. The small
diagram definition now constrains its indexing category. The
equalizer and coequalizer hypotheses in two local arguments were
also made explicit. The reviewer read back and accepted the repairs.
The other mathematical scopes reported no concrete defect.

## Integration and current counts

Both active Part X drivers include all three body/annex pairs.
The actual annex route was recounted: 55 proof items, comprising
the previous 43 plus these 12.

The existing Part X navigation generator produced 110 theorem and
definition rows. The named-theorem index was updated using the
existing generator's Part X rows, preserving unrelated rows.
Twenty-two notation rows were added, and the existing formatter
regenerated both symbol tables with 795 registry rows.
The scoped whitespace check passed.

The current per-part record is
manuscript-completion-status-2026-09-06.md. It records these additions
without converting proof counts into a whole-book percentage.

## Remaining work

The next Part X treatments are Lawvere theories and functorial
semantics, quantifiers as adjoints, and the internal logic of topoi.
Other algebraic treatments and Part XI truth theories remain to
be developed and reviewed to their required source-specific scopes.
Historical survey/pointer treatment codes are not completeness
ceilings under the full-compendium contract.

No software tests, manuscript compilation, or page renders were
used for this writing and mathematical review. The saved PDF still
predates these additions. Whole-book source coverage, complete
requirement fulfillment, current global navigation, final production,
and publication acceptance are not established. The full manuscript
goal remains active.
