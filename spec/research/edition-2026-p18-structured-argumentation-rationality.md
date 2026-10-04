# P18 A2: rationality source and corrected theorem

Integration update: structured-priority-rationality.tex now supplies the
direct corrected-priority proof and the actual retained-assumption
Caminada-Amgoud construction. All four corrected priorities give global
return for unrestricted trees and the proved support-qualified route for
c-restricted trees. The exact last-link profile claim remains refuted;
this is not admission of an abstract theorem for arbitrary orderings.
See edition-2026-p18-structured-priority-rationality.md for the complete
eleven-pair proof map and remaining representation-source obligations.

## Outcome and exact scope

The assigned historical theorem cannot be certified from the source proof
chain unchanged. The finite-set reading of its ordering condition is
insufficient; a repetition-permitting indexed-family reading is stronger.
The manuscript gives a full
finite countermodel and proves a general replacement with an explicit
local return condition. The unrestricted and c-restricted universes are
distinguished. This is not acceptance of the original source scope.

Owned body and annex: handbook/parts/p18/structured-argumentation-rationality.tex
and handbook/annex/p18/structured-argumentation-rationality.tex.
The previous tutorial chapter and all shared integration files remain
root-owned. Block began 2026-09-09 01:08:37 UTC.

## Frozen primary captures

Modgil and Prakken, *A General Account of Argumentation with Preferences*,
Artificial Intelligence 195 (2013), 361–397. The official author page
identifies the selected object as the **corrected version 1 March 2018**.
This is distinct from both the original 2013 PDF and the 2014 tutorial.

- Version evidence: https://webspace.science.uu.nl/~prakk101/publications.html
- Download: https://webspace.science.uu.nl/~prakk101/pubs/AIJfinalErratum.pdf
- Held original: source/references/modgil-prakken-general-account-corrected-2018-03-01/AIJfinalErratum.pdf
- **53 pages; 719453 bytes.**
- SHA-256: **09A9753EE00345A690E937044963B5564EEC01FA9143759258E6AA0D3ABF37C5**.

Companion: Modgil and Prakken, *Corrigendum for: A General Account of
Argumentation with Preferences*, Artificial Intelligence 263 (2018),
107–110. Its author layout has five pages.

- Download: https://webspace.science.uu.nl/~prakk101/pubs/AIJErratumExplanation.pdf
- Held original: same capture directory, AIJErratumExplanation.pdf.
- **5 pages; 187235 bytes.**
- SHA-256: **C7FDCF74DB5DA42BBD2F96341FB6F810DBFF6AE03B4C8AAEA256BCE2DA34D5BC**.

Both originals were downloaded from official author endpoints without
modification. A slow web extraction was stopped before the local download.

## Complete read extent for the selected chain

The full corrigendum, pages 1–5, was read.
The main source was read in these exact extents:

| Main PDF pages | Personally read content |
| --- | --- |
| 1–8 | Identity and conceptual context through official PDF text |
| 8–15 | Definitions 2–17: systems, c-consistency, attacks, universes, closure, continuations |
| 16–19 | Definition 18 and the Proposition 8–Corollary 17 chain |
| 20–22 | Corrected Definitions 19–22 and Propositions 19–24 |
| 23 | Boundary with the distinct abstract-logic presentation |
| 36–40 | Whole Appendix 8.1–8.3 proofs, Lemmas 35–38 and Theorems 12–15 |
| 40–44 | Whole Appendix 8.4 preference proofs and the start of 8.5 |

Pages 36–38 and page 22 were reread after a combined output truncated.
The remaining main-source pages are not claimed read. The separate
Caminada–Amgoud (2007) Lemma 6 referral has been identified but not acquired.
Its referral does not establish the stronger deletion claim refuted here.

## Exact failure of the source implication

Ordinary premises are p,q. Axioms and defeasible rules are empty.
Include both antecedent permutations of each strict schema:

- p,q -> r
- p,q -> not r
- not r,q -> not p
- p,not r -> not q
- r,q -> not p
- p,r -> not q

These twelve ordered rules are closed under every transposition.
Exactly 22 trees result: two positive premise trees, four for r/not r,
eight for not p, eight for not q. Every nonleaf has support {p,q}.
Put every full-support argument strictly below both singleton arguments,
with no other strict comparisons.

All Definition 18 conditions under the finite-set reading hold.
Singleton profile continuations retain
their support. In the finite-family clause, a family containing a
full-support argument cannot make the omitted-member continuation lower
than that full-support argument: no argument is lower than one.
Otherwise the family is a subset of the two unique singleton arguments,
and no strict comparison is available. Repetition of the same argument
does not create additional set members. With repetitions permitted in the
indexing, the family P,P,Q,Q violates the stronger condition: every
omitted-index continuation may have support {p,q} and is below its
singleton target. The manuscript proves this distinction explicitly.

Every attack undermines one of the singleton premises from full support,
and every attack fails. The defeat graph is empty; the entire inconsistent
universe is its unique complete, grounded, preferred, and stable extension.

For the exact Proposition 8 failure, take B concluding not p and A=[p].
The frontier of B is {[p],[q]}. Removing [q] as required would need a
strict argument for not q from p alone. No listed rule can apply from p
alone. Thus transposition does not provide the claimed deletion.
This is an unrestricted SAF countermodel. It is not claimed to be a
c-SAF satisfying c-classicality.

## Complete replacement and reciprocal proof map

Condition (R) requires that a failed attack X T Y have an admitted
returning defeater W D X, and that every defeater of W defeat X or Y.
This is a local attack/defeat property, decidable from complete finite
tables; it does not assume that accepted conclusions are consistent.

The replacement theorem retains arbitrary finite/infinite argument
universes, unrestricted or c-restricted supports, finite rule arity,
contrary well-formedness, axiom consistency, and either contraposition
or paired-literal transposition. The c-restricted case also requires
c-classicality. It proves equality of attack/defeat extension semantics,
direct consistency for admissible extensions, and subargument closure,
strict closure, and indirect consistency for complete extensions.
Every tree-construction and defense step is proved. Actual strict grafts
are not identified with equal component profiles.

Six reciprocal pairs:

| Body label | Annex label |
| --- | --- |
| thm:p18-rationality-strict-sets | annex:p18.ratsets |
| thm:p18-rationality-transposition-boundary | annex:p18.ratcounter |
| thm:p18-rationality-joint-defense | annex:p18.ratdefense |
| thm:p18-rationality-support-union | annex:p18.ratsupport |
| thm:p18-rationality-general | annex:p18.ratgeneral |
| thm:p18-rationality-corrigendum-example | annex:p18.ratexample |

The complete corrigendum example has 28 ordered trees, four nine-argument
preferred/stable extensions, those four plus the empty complete extension,
and empty grounded extension. Its full c-classicality and support
conditions are proved. Corrected strict priorities make attacks equal
defeats, so (R) holds. Tutorial weak-then-strict elitism instead makes
all attacks fail; this comparison is calculated explicitly.

## Direct corrections and variant boundaries

- Proper-subtree maximality defines the fallible frontier.
- Profile continuation is recorded literally as a component-set relation.
- Corrected strict set comparisons use the base strict relation directly.
- Democratic irreflexivity is proved with a finite ascending-chain argument.
- The general account uses extensionwise formula skepticism; the tutorial
  uses the common-argument reading. The earlier chapter distinguishes them.
- The source's general priority-lifting claims are not inferred from
  equality of rule sets or from the proved strict set lemma.

## Integration and remaining source obligations

Requested bibliography keys: ModgilPrakken2013GeneralCorrected and
ModgilPrakken2018Corrigendum, with the publication metadata and author
version/layout qualifications above.
Route after structured-argumentation.tex in P18 A2.
Labels: sec:p18-structured-rationality and
sec:annex-p18-structured-rationality.

Notation intake: attack T, defeat D, Str(A), Prem_n(A), c-consistency,
strict consequence, maximal fallible frontier M(A), profile continuation,
corrected direct strict set/link comparisons, and local return condition (R).

Remaining obligations:

1. The finite-set reading of reasonableness-plus-transposition is refuted.
   The stronger repetition-permitting indexed-family version is not
   refuted by this countermodel, but its source proof is not completed:
   Proposition 8's transposition-based deletion still fails in the
   displayed rule system and requires a valid replacement.
2. Prove exact priority/logic regimes implying (R), accounting for shared
   subtrees, actual grafts, and any restricted-support conditions.
   General source Propositions 19/20 are not completed by the set lemma.
3. Complete separate classical/Tarskian representations and the
   preferred-subtheory equivalence.
4. Acquire/read the separate Caminada–Amgoud referral and complete
   later argument-scheme/ABA source presentations if assigned.

Research and PDF skills supported source reading and provenance.
The complete body, complete annex, and complete source note were read
back once after the writing batch. The finite-set/indexed-family boundary
is explicit in all three files. The body also links the existing complete
countermodels for axiom consistency, strict-rule closure, and strict-root
rebuttal.
No independent reviews, scanners, tests, builds, or manuscript renders
were performed.
