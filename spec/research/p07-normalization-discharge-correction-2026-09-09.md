# Correcting the discharge hypothesis of natural-deduction normalization

The root read the actual `handbook/registry/calculi/nj.tex` and active
`handbook/restoration/inherited-11961-12029.tex`. The former explicitly forbids
empty discharge classes; the latter had claimed unrestricted normalization
for that same derivation system. The conjunction/K derivation demonstrates
that those claims are incompatible.

From open assumptions A carrying label i and B carrying label j, introduce
A and B's conjunction, apply first-conjunct elimination to retain A, discharge
j to obtain B implies A, and discharge i to obtain A implies (B implies A).
Every discharge in that original tree is nonempty. Contracting its conjunction
detour erases the B assumption, making the surrounding j-discharge invalid
under the restricted rule. With distinct atomic A and B this derivation has
no other principal redex or disjunction/existential permutation that could
repair that problem. A complete countertheorem is being authored separately.

## Direct active correction

The active normalization passage now explicitly defines NJ_v by permitting
empty discharge classes in implication introduction, either disjunction
elimination branch, and the existential-elimination minor premise. Other
conditions, including the exact eigenvariable restrictions, are retained.
Its theorem is now titled *Normalization with empty discharge classes*.
The source's existing hook identity is preserved, and its title binding in
the named-theorem-index generator is updated to match the actual declaration.

The `sheet:nj` nonvacuous system is unchanged and explicitly distinguished.
The frozen original source is unchanged. This correction does not fabricate
a normalization proof for the restricted system or equate the two reduction
relations. The planned consequence bridge separately simulates vacuous
discharges using dummy conjunction introduction/elimination, with the
quantifier and branch conditions proved rather than assumed.

## Integrated full construction

The full new body, annex and fourteen-rule NJ_v sheet are now routed. Nine
reciprocal proofs include the restricted countertheorem, consequence bridge,
quantified conversions, substitution, continuation simulation, terminating
measure, full normalization and its principal/permutation-only corollary.
The active corrected original theorem now applies that last corollary
directly, replacing its old sketch. Its original principal/permutation
reduction relation is matched exactly; the additional bottom-absorption
phase has a separately identified theorem. The Part VII comparison tables
now point to the actual new results and preserve the nonvacuous distinction.

The full source and construction record is
`spec/research/p07-natural-deduction-normalization-source-note.md`.

## Authoring ownership and remaining acceptance

The natural-deduction author owns the distinct `p07-nj-vacuous` sheet,
countertheorem, consequence bridge and full quantified normalization proof.
A second author owns the quantified principal/permutation constructions and
termination argument. Both use the now-written full STLC normalization
dependency, not the earlier sketch. Their exact primary-source reading and
final source note will supplement this root correction record.

The specified corrected theorem and bridge are authored. Distinct historical
Prawitz and Troelstra--Schwichtenberg presentation obligations remain as recorded
by the author. Independent acceptance, broader manuscript work and final
publication checks remain open. The edition coverage baseline is unchanged.
