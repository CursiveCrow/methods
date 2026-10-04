# P17 / D4: beliefs, rationality and strategic choice

Date: 9 September 2026. Root-authored finite static treatment with the
complete worked dynamic example, integrated as P17.18. Independent
consolidated reviews and publication admission remain pending.

## Exact source and complete reading

Andrés Perea, Epistemic Game Theory, chapter 9.2 of The Handbook of
Rationality, edited by Markus Knauff and Wolfgang Spohn, MIT Press,
2021, printed pp. 543–551.

- Held source: source/references/knauff-spohn-2021/s042500-perea-copy.pdf.
- Exact unchanged capture: 631,215 bytes; SHA256
  A09F7C87460C7E7D019A23C29A2F7037F9ECB91B95E49D90C9E50C00BB6138E5.
- Author-hosted acquisition URL:
  https://epicenter.name/Perea/Papers/EGT-Ch9-2.pdf.
- The publisher wrapper identifies parent-volume DOI
  10.7551/mitpress/11252.001.0001 and electronic ISBN 9780262366175.
  That DOI is not represented as a separately verified chapter DOI.
- Twelve physical pages: publisher wrapper at 1, all nine original
  chapter pages at 2–10, blank separator at 11, copyright/cataloging
  information at 12. Printed page equals physical page plus 541.
- The wrapper's October 2023 download/producer metadata is distinguished
  from the original 2021 chapter.

The complete original pp. 543–551 were read, including all five numbered
definitions, the attributed Pearce lemma, the fundamental theorem,
Tables 9.2.1–9.2.3, Figures 9.2.1–9.2.2, both notes and the references.
All nine original pages were inspected as source-page images under
tmp/pdfs/p17-epistemic-game-theory/perea-02.png through perea-10.png.
The wrapper, blank page and copyright/cataloging text were also read
and distinguished from chapter content.

The first text extraction encountered the Windows output encoding at
the product glyph; extraction was repeated in UTF-8. The held file's
font maps generate warnings and a column-order extraction, so source
formulas, matrices and the dynamic tree were read from the original
page images. No manuscript PDF was built or rendered.

## Authored scope and complete proof map

Body: handbook/parts/p17/epistemic-game-theory.tex.
Annex: handbook/annex/p17/epistemic-game-theory.tex.
Chapter label: sec:p17-epistemic-game-theory.
Annex label: sec:annex-p17-epistemic-game-theory.
Canonical source key: Perea2021EpistemicGameTheory.

All result suffixes below follow thm:p17-egt-; proof suffixes follow
annex:p17.egt. and replace internal hyphens with dots.

| Result suffix | Source/interface and supplied proof |
| --- | --- |
| hierarchies | Section 2, pp. 544–545: finite type beliefs induce every finite hierarchy level; explicit finite-support spaces, pushforwards and coherent truncation maps. |
| belief-algorithm | Section 3, pp. 545–546: the source's individual belief levels, cumulative intersections, positive-support graph, bad-type reachability and the finite bound; full counterexample separating onefold from twofold alone. |
| best-response-alternative | Section 4's Pearce lemma, p. 546: both mutually exclusive alternatives on every finite restriction, via the actual finite minimax result; full rational vertex-enumeration justification, including lower-dimensional and zero-margin cases. |
| reduction-integrity | Sections 4, pp. 546–547: nonempty restrictions, bounded simultaneous deletion and preservation of all original deviations for every current supporting belief. |
| finite-depth | Section 4, p. 546: exact round/depth indexing in both directions and a complete finite layered-type construction with anchor beliefs. |
| fundamental | Theorem 1, p. 547: all original finite choices, arbitrary correlated opponent conjectures, both implications and one finite type per final surviving action. |
| first-game | Tables 9.2.1–9.2.2, pp. 544–547: all six expected-payoff vectors, correct opponent index in the hierarchy example, every type's belief status and every deletion/retention witness. |
| nash-beliefs | Definition 5 and Section 5, pp. 547–548: the equilibrium-induced one-type-per-player hierarchy and rationality of every supported pair. |
| nash-gap | Table 9.2.3 and Figure 9.2.1, pp. 548–549: full six-type model, all-action rationalizability, complete mixed-equilibrium uniqueness calculation and the higher-belief error. |
| mutual-conjectures | Section 5, p. 548: an explicitly quantified two-actual-type correctness condition yields the Nash conjecture profile. Its precise scope is distinguished from the separate one-person reformulations. |
| many-player-boundaries | Section 5, pp. 548–549: two complete editorial countermodels for correlated conjectures and disagreement about a third player's marginal; exact payoff reversal under product replacement. |
| reny-reasoning | Section 6 and Figure 9.2.2, pp. 549–550: complete tree and strategic form, all four backward comparisons, the stated rational-explanation filter after b, the different off-path plan and exact 3/4 conditional-probability bound. |

These are twelve authored reciprocal pairs. The full active
thm:p17-finite-minimax statement and its proof were read; they establish
attained finite matrix minimax equality from the manuscript's supplied
Nash existence theorem. No unproved separation theorem is substituted.
The source's finite game and finite-type domains are retained, including
arbitrary joint beliefs about all opponents. Finite types are not claimed
to represent every possible hierarchy.

## Direct corrections and important distinctions

The source's p. 544 paragraph about t1-b calls the opponent's type t1-e.
The active construction uses the actual t2-e from Table 9.2.2.
The state/type/action roles are defined separately before use.

The source's individual k-fold levels are not automatically nested.
The active manuscript retains that definition and explicitly forms the
cumulative levels needed for the elimination interpretation. A complete
example shows twofold and every higher individual level without onefold.
The source's finite-depth indexing uses all levels through k-1; the
manuscript states and proves precisely that indexing.

The reduced game's deviation set cannot simply replace the original
choice set in an epistemic optimality statement. A separate induction
proves that deleted actions are strictly below the remaining maximum
for every currently supported belief. This supplies both the finite-depth
and stationary-model construction without an omitted deviation premise.

Arbitrary correlated beliefs on opponent profiles are retained. The
matrices used in the domination alternative and the independent mixed
profile used for Nash have different meanings. No original Bernheim or
Pearce presentation with additional independence requirements is silently
credited by this chapter's correlated-belief theorem.

The two-actual-type conjecture theorem fixes both actual first-order
beliefs and quantifies the probability-one correctness conditions.
Its conclusion is a Nash profile of conjectures. It does not assert
that any unmentioned realized action has positive conjectured mass.
The source's separate single-player formulations and exact belief-depth
claims need their original, more detailed conditions; they are not
accepted by renaming this mutual theorem.

The dynamic calculation proves the explicitly stated explanation rule
in the displayed four-move game. It distinguishes a full contingent
strategy from its outcome and specifies the conjecture needed to make
the surprising move optimal. It does not claim to define or characterize
general extensive-form rationalizability from this one tree.

## Remaining precise scope

The finite static definition/lemma/theorem chain and both original static
examples have complete proofs. The complete dynamic example is also
calculated. The source's cited general boundaries remain identifiable:

- Terminal type structures and the equivalence with alternative
  state-based encodings require their exact mathematical presentations.
- The single-person correctness formulations, the exact two-level
  claim and the additional common-belief implication require the
  underlying Spohn, Aumann–Brandenburger and Polak definitions.
- Common belief in future rationality, strong belief, sequential and
  extensive-form rationalizability need full conditional-belief models.
  The general perfect-information/no-relevant-ties outcome theorem
  attributed to Battigalli is not proved by the example.
- The cited original source versions are not counted as acquired or
  wholly reconstructed merely because this chapter's references were read.

These are precise remaining D4/source-presentation obligations; this
return does not close D4 or the whole first-edition catalog.

## Integration and authoring evidence

P17.18 is routed in the body and annex, and the preceding finite-game
chapter links to its epistemic continuation. The source key and typed
notation are merged through root's canonical integration.
The saved body and all twelve proofs received one complete author
read-through. Clarifications in that batch make the fixed game explicit,
separate the two alternatives typographically, give an actual terminating
rational procedure and split a long arrow display.
The final changed passages were read back.
Research and PDF skills governed the source note and original-source
reading. Independent reviews, manuscript scans/tests/builds/renders and
publication admission remain deferred under the user's sequence.
