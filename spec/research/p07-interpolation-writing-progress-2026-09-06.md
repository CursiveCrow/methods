# Craig interpolation and Beth definability: completed proof writing

The active manuscript now supplies the general Craig/Beth proof previously
identified as missing from the interpolation supplement. The proof uses
Maehara's method and an explicit relationalization of functions and equality.
The older source statements and navigation were updated at their existing
public labels.
This supplies the proof writing requested by N-a-070 and D-P8-004.
The separate model-theoretic treatment and Robinson equivalence listed
under N-a-013 have since been completed in the active Part III text;
see p03-interpolation-writing-progress-2026-09-06.md.

## Actual proof chain

1. annex:p7.interp.1 proves Maehara's partition lemma for the exact
   equality-free purely relational LK_d calculus, including the common
   free-variable condition.
2. annex:p7.interp.2 proves soundness for that fragment and direct
   cut-free completeness for finite sequents. Persistent backward expansion,
   fair scheduling over all parameter variables, and a saturated
   countermodel establish completeness for the exact registered rules.
3. annex:p7.interp.3 proves Craig interpolation in signatures with
   functions, constants, and equality. Finite graph axioms give quotient
   interpretations. The asymmetric axiom split preserves common
   vocabulary; canonical graph expansions and atomic decoding give both
   implications. Fresh constants then handle arbitrary free variables.
4. annex:p7.interp.4 proves Beth definability for arbitrary theories and
   signatures under the book's ambient Choice assumption. Compactness
   extracts one finite interpolation problem; predicate renaming and
   parameter removal give one finite subtheory proving one uniform
   definition. Arity zero, inconsistent theories, and tuples with equal
   entries are included.

The full general cut-elimination sketch is not used as a missing premise.
Beth uses the existing proved first-order compactness and completeness
theorems at thm:fol-compactness and thm:fol-completeness.

## Reader text

- handbook/restoration/inherited-11914-11960.tex retains the Craig and
  Beth public labels, now with proof-annex links and exact proved scope.
- handbook/parts/p07/cut-elimination-and-interpolation-supplement.tex
  includes the adequacy theorem, corrected quantifier-method table, the
  graph-translation explanation, a private-function interpolation example,
  and a monoid right-inverse example of implicit definability.
- handbook/annex/p07/interpolation-supplement.tex contains all four proofs.
- Part VII's source map, proof-complexity navigation, and lookup table
  now point to these proofs.

The related primary proof-search source is Gallier's author-hosted second
edition, added to the bibliography as Gallier2015. Exact source locators
are in p07-craig-beth-dependencies-source-note.md. Independent mathematical
derivations are in p07-craig-relationalization-proof-note.md and
p07-beth-proof-note.md.

## Direct mathematical readings

Bounded independent readers checked the actual LaTeX for all four proof
items and their theorem statements. They found no substantive defect.
The Maehara reader requested an explicit free-occurrence and fresh-bound-
variable convention before the quantifier cases; that clarification is
incorporated. The Beth reader also checked the right-inverse example.

This records completion of the interpolation proof writing. It does not
claim completion of the entire book or its final publication preparation.
