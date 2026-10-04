# P1 section 5.6: equivalence closure and quotient proof completion

Record date: 2 October 2026. This packet addresses only the exact current
fulfillment gap for P1 section 5.6, not the broader source-allocation catalog.
Root owns routing, canonical merges, source baseline and admission; prior
author packets remain frozen.

## Exact obligation and actual authority reading

The complete row with `part=P1`, `section_id=5.6` in
`spec/coverage/edition-2026/current-fulfillment/p01-p03.jsonl` was read. It
marks the interval partial: equivalence closure is defined, but existence/
minimality construction and an integrated quotient example are missing.
The row identifies inherited facet `ED26-FLRV1-U00111-01`; definition
presence does not discharge construction, example or proof admission.

Read in full at the relevant connected extent:

- Frozen `source/formal-logic-reference.tex`, lines 444-532: binary relations,
  relation properties, functions and their types, injections/surjections,
  image/inverse image, equivalence classes and the quotient method.
- Frozen lines 1343-1397: reflexive-transitive closure, the complete finite
  directed-path characterization/proof, equivalence-closure definition and
  distinction between the closures. The preceding finite-sequence/
  construction conventions and formal-definition audit were also inspected.
- Current routed `handbook/restoration/inherited-00507-00532.tex`, all 26
  lines: equivalence relation, class/quotient definitions and independence
  of representative method; current hash
  `86B061703F0365E02F3C182D30046B450FA9898232B58EBA1E2A60B3AA9880F1`.
- Current routed `handbook/restoration/inherited-01343-01397.tex`, all 55
  lines, including its complete directed-path proof and final closure
  definition; current hash
  `738D2BD4619504D02B2D64682E3F1E62B589BF7F8D6FC11D3EAA11055208A15A`.
- Corresponding current P1 lookup clauses for sets/functions/classes,
  natural numbers including zero, finite sequences, generated sets and
  relation closures. The actual P1 driver and relevant shared macro guards
  were inspected solely to identify the integration seam and usable notation.

The frozen source's whole-file SHA256 is
`0509750C13B88A4E18914BD52BDE171C725CBA14221CBFC2227D7693A2B421CC`,
matching `spec/INHERITED-CORPUS-MANIFEST.md`. The actual archived title-page
identity is *Formal Logic: Language, Semantics, Deduction, and Metatheory*,
Version 1.0, 9 August 2026. This archival identity is not a restoration of
the retired public opening. No frozen or current inherited file is edited.

No external book or article supplies the new proofs. The existing lookup's
general Jech2003 citation is not represented as a reading of an external
equivalence-closure presentation. A unique bibliography intake identifies
the actually read frozen manuscript. The new proof construction, universal
property and finite example are explicitly editorial completions rather
than falsely attributed original-source proofs.

## Completed mathematical content and dependencies

Body: `handbook/parts/p01/equivalence-closure-and-quotients.tex`, anchor
`sec:p01-equivalence-closure-and-quotients`.
Annex: `handbook/annex/p01/equivalence-closure-and-quotients.tex`.

The finite dependency chain is relation/sequence/set bounds → explicit
zig-zag construction and minimality → class equality/partition/projection →
choice-free factorization and generator criterion → the computed finite
quotient and rejected representative formula. Definitions precede results.

Four actual formal promises have four full reciprocal annex proofs:

1. `thm:p01-ec-construction` ↔ `annex:p01.ec.construction` constructs E by
   bounded separation using finite witnesses. Length zero has one vertex
   and no edges; reversal checks every edge; concatenation checks agreement
   at the shared index and both edge ranges, including zero lengths.
   Containment and induction on path length prove leastness directly.
   The equivalence-superset family is a set and contains the full relation;
   its bounded intersection is equivalent and contains R. Both inclusions
   establish equality with E. A further direct minimality argument identifies
   E with `(R union converse R)*`, without assuming that naming a least
   relation established its existence. Empty-carrier, empty-generator and
   already-equivalent-generator cases are proved.
2. `thm:p01-ec-classes` ↔ `annex:p01.ec.classes` proves membership of each
   representative, equality/intersection criteria, nonempty classes, exact
   coverage and disjointness. Quotient and projection graphs have explicit
   set bounds. The empty quotient is empty, not a singleton containing the
   empty set; projection remains a total surjection.
3. `thm:p01-ec-factorization` ↔ `annex:p01.ec.factorization` proves necessity
   and sufficiency of constancy on equivalent inputs, constructs the factor
   as all appropriate pairs in a bounded product, proves totality and
   single-valuedness, verifies the factorization equation and uniqueness,
   and handles empty sets. For generated E, finite-path induction proves
   that equality on R-edges is equivalent to constancy on E. No global
   representative selection, well-order or axiom of choice is used.
4. `thm:p01-ec-finite-example` ↔ `annex:p01.ec.finite-example` computes the
   closure of the four displayed directed generators on `{0,...,5}` as
   two complete blocks `{0,1,2,3}` and `{4,5}`, hence twenty pairs and
   two quotient elements. It checks every projection/factor value. The
   directed reflexive-transitive closure is diagonal union R and does not
   contain `(0,3)`, while the zig-zag closure does. The identity-valued
   function fails constancy at zero/one. The separately justified finite
   minimum selector is a section, but its composite with projection is
   not the identity-valued function, so it does not repair that failure.

The general theorem requires only a set carrier and an arbitrary binary
relation. Finiteness appears only in the connected worked example; no
decision/termination claim for arbitrary infinite X is introduced.
The universal property concerns functions of sets. Arbitrary operations,
relations or other source-specific quotient structures are not licensed
without their own compatibility proofs.

## Notation and intended integration seam

The inherited displayed notation is retained: X, R, R*, E, `[a]_E`, A/E,
and bar f, including the class orientation `xEa`. R inverse is explicitly
typed as relation converse. Star is explicitly relation closure rather
than finite-string closure. Composition is introduced as typed function
composition rather than the earlier binary-connective metavariable.
Local carrier-element variables are not object-language variable tokens.

Source-only `set`, `tuple` and `Pow` macros are guarded against editorial
use in the existing stylesheet. This fragment uses ordinary brace/angle/
power-set commands with the same displayed mathematical notation; it does
not alter those guards or rename source glyphs to evade type collisions.
Every genuine locally typed role is retained in the seven-field symbol
intake `handbook/registry/symbols-intake-p01-equivalence-closure.csv` under
the named scope `P1 Equivalence closure and quotients`, with actual body/
annex anchors. Root owns binding that scope and canonical merging.

The fragment is section-level, intended after the strings chapter's
restored exercises (`scope-SRC-01398-01410`) and before the next restored
chapter (`scope-SRC-01411-01504`), supplying planned fulfillment identity
P1 5.6 while leaving the existing source sequence and section labels intact.
That ledger identity is not a forced literal reader section number; physical
numbering is determined by the live route. Root must route
the new body and annex and merge the unique bibliography/symbol intakes.
No shared driver was edited and no manuscript render or build was run.

## Author-side adoption preparation, 2 October 2026

The full body and all four annex proofs were reread with the current P1
ordered-pair/product, relation/function, finite-string and source
equivalence-closure clauses. The existing source definitions precede the
selected insertion seam after `restoration/inherited-01398-01410.tex`
and before `restoration/inherited-01411-01504.tex`. Empty paths are the
existing finite-indexed functions, not nonempty sequences or a new Choice
assumption. Relations use a fixed carrier, classes have the inherited
orientation `xEa`, and the factorization is a bounded graph with a unique
output, not selection of representatives. The constructive four-pair
packet therefore keeps its exact original notation and hypotheses.

No body, annex, unique bibliography or symbol row changed in this adoption
block. Only the note's misleading identification of planned P1 5.6 with a
literal new reader number was corrected. Root supplies the body input at
the selected seam, an input to the new live `handbook/annex/p01-route.tex`
without historical-annex duplication, and canonical intake/scope merging.
These local relocation observations are not independent proof review,
source admission, tests, builds or manuscript renders. Broader source
comparisons remain separate from this exact editorial proof completion.

## Verification standing and residual boundaries

The body and all four proofs are author-checked against the exact requested
mathematical clauses, including zero-edge paths, reversal direction,
concatenation indices, fixed-carrier intersection, quotient equality,
bounded graph existence, unique outputs, empty-domain/codomain cases,
generator constancy and the representative failure. These are author
mathematical checks, not an independent review or admission verdict.

Bounded author data checks found 36 symbol records, zero malformed quoted
seven-field rows, zero invalid math-delimited glyph or precedence values,
four reciprocal body/annex pairs with zero mismatches, and four complete
proof-environment pairs in the annex. The body has no proof environment;
the new TeX has no restoration-guarded set/tuple/Pow macro call. Final source
and routed-interval hashes still match the authority hashes above. These
checks inspect identifiers and intake structure; they are not prose tests,
a book build, a rendered-page inspection or an independent proof review.

This packet supplies the particular construction/quotient example gap at
the stated hypotheses. It does not close broader allocated presentations,
source comparisons or any unrelated P1-P3 residual. Root integration,
canonical merges, consolidated review/static/build/render gates and
independent admission remain separate. No existing/shared/canonical/
baseline/source file or earlier released packet was changed. No reviews,
prose tests, builds or manuscript renders were performed.
