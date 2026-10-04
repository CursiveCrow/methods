# Lawvere theories, equational presentations, and free models

Date: 6 September 2026 Pacific time.

The actual Part X body and annex now include lawvere-theories,
lawvere-presentations, and lawvere-free-algebras. The previous
short Lawvere-theory paragraph has been replaced by definitions,
constructions, examples, and seven complete theorem/proof pairs.

## Seven integrated proof pairs

| Body result | Annex proof |
| --- | --- |
| thm:p10-lawvere-term-theory | annex:p10.lawvere.1 |
| thm:p10-lawvere-models | annex:p10.lawvere.2 |
| thm:p10-lawvere-presentation-recovery | annex:p10.lawvere-present.1 |
| thm:p10-lawvere-model-restriction | annex:p10.lawvere-present.2 |
| thm:p10-lawvere-finite-free | annex:p10.lawvere-free.1 |
| thm:p10-lawvere-free-adjunction | annex:p10.lawvere-free.2 |
| thm:p10-lawvere-empty-carriers | annex:p10.lawvere-free.3 |

The core defines the structural functor from the opposite finite-ordinal
category, selected powers and projections, equations with explicit
finite contexts, the least family of congruences preserved by all
context substitutions, and the resulting tuple-arrow category.
Its composition and evaluation are proved well-defined, including
empty contexts and nonfaithful structural maps.

The model equivalence includes every algebra homomorphism and natural
transformation. It extracts operations using the canonical product
comparisons, proves all defining equations, and supplies comparison
isomorphisms natural in both models and theory objects.
The singleton power A^1 is not treated as literally A; the explicit
singleton-tuple comparison also verifies both triangle identities.

The abstract-theory recovery uses one operation name for every arrow
to the distinguished generator. Projection and substitution equations
suffice: structural induction reduces every term to its named
interpretation and proves that those equations are exactly the
evaluation kernel. The inverse functor is explicit, including
nullaries, composition through object 0, and coincident projections.
Theory morphisms induce restriction on models and all transformations.

Representable models are free on finite generator sets by Yoneda
applied with the correct opposite variance. The arbitrary-generator
construction proves its semantic term quotient satisfies the
presentation, gives extension uniqueness, and transports it to a
free-model/underlying-set adjunction. Only finitely many representatives
are selected for any one equation; no section of a quotient is assumed.

## Carrier and size conventions

The categorical equivalence first uses algebras with all permitted
carriers in the fixed universe. It then restricts to the full
subcategory of models whose value at generator object 1 is nonempty.
This preserves the earlier universal-algebra section's nonempty
convention.

Every model sends terminal object 0 to a singleton. An empty-carrier
model exists exactly when the theory has no arrow 0 to 1.
The unrestricted initial model is the representable at 0.
The nonempty subcategory may lack an initial object, as proved for
nonempty sets and semigroups. The unary equation d(x)=d(y) gives a
counterexample to the stronger claim that absence of nullary symbols
always precludes an initial nonempty algebra.

The universe scope is explicit for signatures, equation sets, carriers,
and generator sets. Larger instances are interpreted in a suitably
larger universe before forming the set-valued models.

## Sources and independent review

The acquired Lawvere source is the authorized 2004 TAC reprint,
containing the 1963 thesis, the separate 1968 article, and author
commentary. The manuscript explicitly distinguishes the thesis's
coproduct convention from the later product convention, with the
opposite-category translation.

The acquired Adamek--Rosicky--Vitale text is the author draft dated
1 February 2010, not the final 2011 publisher manifestation.
Pitts1995Draft supplies the context-category and model-equivalence
construction under its own local pagination.
The new bibliography keys are Lawvere2004FunctorialReprint and
AdamekRosickyVitale2010Draft.

Source records:

- p10-lawvere-theories-source-note-2026-09-06.md;
- p10-lawvere-source-verification-2026-09-06.md.

Independent actual-LaTeX mathematical reviews:

- p10-lawvere-core-review-2026-09-06.md;
- p10-lawvere-presentation-review-2026-09-06.md;
- p10-lawvere-free-review-2026-09-06.md.

The core and presentation reviews passed. The free-model review
requested the explicit universe scope and local notation/wording
repairs; the actual changes were read back and passed.
The source check found no remaining version, locator, or attribution
defect in the reviewed material. These bounded reviews do not establish
whole-Part-X or whole-book acceptance.

## Navigation and current amount written

The three body fragments and their three proof fragments are included
by the active host and annex driver.
The actual Part X annex route was recounted at 62 proof items:
the previous 55 plus these seven.

The existing Part X formatter produced 123 theorem/definition rows.
The existing named-theorem generator supplied the seven new index rows,
applied as a scoped update. Seventeen notation entries were added,
and the symbol formatter regenerated both tables with 812 registry rows.
The scoped whitespace check passed.

The current per-part record is
manuscript-completion-status-2026-09-06.md.
The new proof counts do not establish completed register-row counts
or a whole-book percentage.

## Remaining writing and source scope

The next categorical development is quantifiers as adjoints and
first-order categorical semantics, then the internal logic of topoi.
Its source packet is ready at
p10-quantifier-adjunctions-source-note-2026-09-06.md.

The final 2011 Adamek--Rosicky--Vitale manifestation remains unacquired.
These complete proofs do not claim a full reconstruction of every
part of that book or every separate registered source presentation.
Other algebraic treatments, Part XI truth theories, complete
requirement reconciliation, and the rest of the publication objective
remain open.

No software tests, manuscript build, or page renders were used for
this writing. The saved PDF still predates the additions. The full
manuscript goal remains active.
