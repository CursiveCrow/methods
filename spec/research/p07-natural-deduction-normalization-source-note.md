# Full natural-deduction normalization: authoring and calculus correction

Date: 9 September 2026. This block owns the new
`handbook/parts/p07/natural-deduction-normalization.tex`, matching annex,
`handbook/registry/calculi/p07-nj-vacuous.tex`, and unique bibliography/symbol
intakes. Root owns the original active passage, original `nj.tex`, drivers
and canonical records. Other writers' files were preserved.

## Exact initial target and discovered obstruction

The actual `handbook/registry/calculi/nj.tex`, active
`handbook/restoration/inherited-11961-12029.tex`, inactive
`handbook/parts/p07/normalization-and-curry-howard.tex` and
`handbook/annex/p07/normalization.tex` were read. The mapped inherited
normalization units FLRV1-U00808/U00810 and the explicit D-P10-016 normalization
dependency were inspected. The source target is the finite-tree first-order
calculus with bottom, conjunction, disjunction, implication, universal and
existential quantification, without RAA, primitive negation, equality rules
or induction. Its original sheet additionally prohibited empty discharge
classes for implication introduction, both disjunction-elimination branches
and the existential-elimination minor proof.

That last restriction makes the unconditional old normalization assertion
false. The finite derivation
`lambda u:A. lambda v:B. pi_1(pair(u,v))` is valid in the nonvacuous sheet:
both assumptions actually occur and are discharged. Its sole principal
contraction produces `lambda u:A. lambda v:B. u`, whose inner discharge
is empty and therefore illegal there. No other principal/permutation step
exists in the original tree. This obstruction was constructed directly from
the actual registered rules before consulting corroborating literature.

Root verified the exact tree and authorized a distinct standard presentation
allowing empty classes, while preserving `sheet:nj`. The new display is
NJ_v on `sheet:p07-nj-vacuous`. Root directly corrected the old active
unconditional assertion to name this standard variant and its actual
discharge conditions. This author did not silently rename or relax the old
sheet. The new chapter supplies both the proved nonvacuous countertheorem
and the full two-way consequence bridge. The bridge inserts a dummy
conjunction introduction and projection for every missing discharged class;
all new assumptions are discharged and the eigenvariable conditions remain
valid. Thus the two variants have the same consequences, but the bridge
does not preserve normality.

## Sources and exact manifestations

### Constructed proof route: de Groote

Philippe de Groote, *On the Strong Normalisation of Intuitionistic Natural
Deduction with Permutation-Conversions*. The [author's publication list](https://members.loria.fr/PdeGroote/publi.html)
identifies the Information and Computation 178(2), 441–464 (2002) journal
paper separately from the earlier 1999 RTA presentation, and links the
[actual author manuscript](https://members.loria.fr/PdeGroote/papers/ic02.pdf).

The helper acquired and read the complete 30-page manuscript, including
its full quantified development and typing appendix, in
`tmp/pdfs/p07-nj-quantifier-conversions/de-groote-ic02.pdf`.
It is 220,509 bytes, SHA-256
`1C0FEDCF7F4DBA2C667FE69C6EE2453BB9FAF2848B09695152B61B3D3CCC37A8`.
The exact construction note is
`spec/research/p07-nj-quantifier-conversions-construction.md`; its completed
715-line authoring snapshot has SHA-256
`0E0D213FB18AE1A83754D9069931833FFB4147E90A4E26889C16351012779166`.
The main author read the complete construction, the later explicit universal
alpha-renaming/continuation-closure additions, the actual source opening,
and the newly routed STLC dependency. The helper also read the final new
rule sheet and compared all fourteen rules to the declared target.

Relevant source locations are Definitions 1–3, 6–10, 13–16, 19–20;
Lemmas 1–20; Theorems 1–3 and Appendix A. The author's Theorem 4 and
bottom-postponement argument are not imported as an unproved stronger
conclusion. The chapter instead gives an explicit two-phase weak-normalization
proof: principal/permutation normalization first, then bottom absorption,
which preserves the first phase's normality.

The source omits individual terms in its normalization simulation explicitly
(manuscript page 13, footnote 2). The actual handbook proof objects retain
every first-order term, formula annotation and eigenvariable. Erasure occurs
only in the auxiliary termination map. Both annotated substitution lemmas,
the quantified principal reductions and all fourteen permutations are written
with their actual fresh-name conditions. In particular, a later existential
eigenvariable is fresh for the earlier branch assumptions which had already
been discharged at its original position.

The arithmetic measure is proved by complete elimination-frame recurrences.
This directly supplies the correct weight expressions instead of copying
typographical slips in individual source calculations. No claim that whole
proof size decreases under branch duplication is made.

### Corroboration of the nonvacuous obstruction: Read

Stephen Read, *Proof-Theoretic Validity*, author manuscript dated 8 November
2014, was acquired from the [St Andrews repository](https://research-repository.st-andrews.ac.uk/bitstream/handle/10023/10772/PfTh_validity.pdf?isAllowed=y&sequence=1).
Local path:
`source/references/read-proof-theoretic-validity/read-validity.pdf`.
SHA-256:
`7612B8532EB2998865C11F06A1E1C197718A4E18C9BC750C7DA4EB6A409D8456`.
Its actual title/date and the page-18 counterexample discussion were read.
It gives the same conjunction/K obstruction and cites Prawitz 1965,
page 84 and note 2. This manuscript has its own intake identity; no later
publication version is inferred from it.

### Controlling historical references and their remaining limits

Prawitz's *Natural Deduction* (1965, Almqvist & Wiksell) and the separate
Dover 2006 reprint are identified by the author's publication record and
the existing bibliography. The complete 1965 body was not acquired in this
block. The Read manuscript corroborates the reported page-84 issue but is
not a substitute for acquiring the original source presentation.

The public [Basic Proof Theory 2000 text presentation](https://djvu.online/file/VLMSoEdUYgpXs)
exposes the actual second-edition title/copyright/ISBN 0-521-77911-1 and
the relevant Chapter 6 text. Its Sections 6.1.1–6.1.8 describe principal
and permutation conversions and the rightmost top critical-cut strategy.
Section 6.1.8A explicitly leaves the remaining cases to the reader, and
6.1.8B requests the extension from atomic to general bottom elimination.
Section 6.1.10 states full strong normalization but explicitly does not
prove it for the full system; its later arrow-only proof cannot alone
discharge the full quantified target.

The exact retrieved source excerpts are saved at
`source/references/troelstra-schwichtenberg-2000/web-indexed-excerpts-2026-09-09.txt`.
Direct local HTML acquisition returned HTTP 403 and the indexed page-image
clicks failed; no full local publication body or complete historical-source
acceptance is credited. The final handbook theorem is explicitly proved
by the separately attributed de Groote route, not misrepresented as the
completed Prawitz or Troelstra–Schwichtenberg source-specific proof. Their
separate historical presentation obligations survive.

## Completed mathematical construction

The new body/annex supply:

1. The exact nonvacuous countertheorem and same-consequence bridge.
2. Every constructor of the annotated finite-tree NJ_v proof language.
3. Proof substitution and individual substitution with every quantifier case,
   copied discharge ownership, empty classes and strict eigenvariable absence.
4. Seven principal conversions and their contextual preservation proof.
5. Seven exhaustively enumerated elimination frames, each permuted over case
   and unpacking: fourteen concrete permutations, including all nested cases.
6. Seven bottom absorptions, with conclusion and open-support preservation.
7. The explicit normality predicate for those three classes only.
8. First-order annotation erasure, its two substitution identities, and the
   complete arrow-only value/computation type translation.
9. All fourteen modified CPS constructor cases, typing, strict continuation
   closure, proof-substitution compatibility, every principal simulation and
   every permutation identity, lifted through arbitrary contexts.
10. Complete positive n/w recurrences and the exact strict differences for
    case and unpacking permutations, including copied auxiliary trees.
11. A lexicographic beta-height/weight measure for Phase I and a constructor
    count for Phase II, with a proof that Phase II cannot recreate a Phase I
    redex. The combined strategy-state measure lies in the natural numbers
    to the fourth power with lexicographic order.

The exact independent authoring dependency is the already routed
`thm:p07-stlc-strong-normalization`, proved at
`annex:p7.stlc.strong-normalization` in the two `stlc-metatheory.tex` files.
It covers open arrow-only typed terms and supplies the finite beta-height
argument. Its separately authored inert-constant corollary also exists,
although this construction can use the fresh individual marker as an open
target variable. The old inactive STLC sketch is not used as proof evidence.

## Integration and completion boundary

The new normalization result is `thm:p07-nj-vacuous-normalization`, with
proof `annex:p7.nj.vacuous-normalization`. The nonvacuous obstruction is
`thm:p07-nj-nonvacuous-obstruction`; the derivability bridge is
`thm:p07-nj-vacuous-consequence-bridge`. Root owns routing, the corrected
old theorem's proof hook, and all canonical intake merges. Neither the
original restricted sheet nor an inactive theorem was silently relabeled
as this full proof.

For the original passage's principal/permutation-only relation, the exact
corollary is `thm:p07-nj-principal-permutation-normalization`, proved at
`annex:p7.nj.principal-permutation-normalization` by stopping after Phase I.
This avoids using an added bottom-conversion step to justify a claim about
the narrower relation. The new pair contains nine reciprocal proved items.

The exact full first-order weak-normalization theorem is authored; no
principal, permutation, eigenvariable, duplication or terminating-strategy
case in the declared result is left as a sketch. Arbitrary interleaving
strong normalization including bottom absorption is not claimed. The
historical monograph presentations and all independent acceptance work
remain separate. No manuscript build, render, independent review or new
test suite was run for this authoring block.

The main author completed a full read-through of the actual new body and
annex after integration. The direct structural extraction found nine unique
body results, nine unique reciprocal annex items, nine ordinary annex proofs,
zero ordinary body proofs, and fourteen rules on the new sheet. The reading
caught and corrected a duplicated corollary/proof block and three local
LaTeX transcription defects before handoff. The final source files contain
no stray control characters. These checks support authoring integrity and
do not constitute independent source or mathematical acceptance.

Before canonical intake integration, all 29 glyph cells were changed to
their existing macro/display code enclosed in LaTeX inline math delimiters.
The macro, role, scope, precedence, first-use and note cells were preserved.
The notes contain no bare subscript or superscript expressions requiring
additional delimiters. This was an intake-format correction only.
