# P6 classical Prikry forcing: authoring scope and source boundaries

Date: 2026-10-03. Status: authored, not independently reviewed, not built
or manuscript-rendered. The cardinal-characteristics and earlier forcing
packets remain frozen; only the assigned new Prikry files and dedicated
source folder are changed. Research uses primary retrieval and this one
note. The research skill's default child workflow was not used because
the assignment expressly prohibited children. The PDF skill was used to
read exact Mathias source formulas obscured by extraction, not to render
the new manuscript.

## Allocation and actual current dependencies

Read literal proposed row **77.12**, *Prikry-type forcings and changes of
cofinality*, at `spec/proposed-table-of-contents.json:4117`. Read its current
coverage row in `current-fulfillment/p04-p06.jsonl:337` and the complete
`ED26-SRC-002-017` completion-queue record. Its facet is Moti Gitik,
*Prikry-Type Forcings*, the complete published 2010 chapter pp. 1351--1447,
[original DOI](https://doi.org/10.1007/978-1-4020-5764-9_17). SETUP,
DEVELOPMENT, CASES and APPARATUS remain whole-chapter duties. The source
destination is still its existing P5 source-specific path; this P6 subject
packet does not change that allocation. Prerequisite overlays block 3 and
block 5 explicitly keep the ambient axioms/setup distinct from external
named imports; no contents-derived theorem edge is inferred here.

Actual neighboring manuscript extents read:

- `handbook/parts/p06/large-cardinals-absoluteness.tex:234--292`, including
  the strongly inaccessible convention and the nonprincipal kappa-complete
  measurable-cardinal definition. It does not supply the new normality
  equivalence or the Prikry construction.
- `handbook/parts/p06/forcing-recursion-and-truth.tex:15--29` and
  `166--250`: exact transitive-ground/supplied-generic standing; recursive
  monotonicity, decision and density closure; truth and ZFC-transfer;
  external countability kept separate. These are real current dependencies,
  not newly assumed proof conclusions.
- `handbook/parts/p06/forcing-variants-supplement.tex:49--99`: Cohen,
  random and collapse catalog. It does not replace the cofinality forcing
  developed here, and its unqualified collapse/cofinality extrapolations
  are not adopted.
- Full `handbook/CONVENTIONS.md` read, including reciprocal annex proof
  status and the seven-column symbol intake.

The selected external/internal imports actually used are the current
fixed-formula forcing definability/density/truth and ZFC-transfer results,
the standing model's ZFC operations and Choice, and the explicitly supplied
normal measure. No measurable cardinal is inferred from Con(ZFC), no
transitive ground is inferred from mere consistency, and no ambient
completeness is attributed to the ground ultrafilter.

## Source identities and exact read extents

[Karagila's author notes](https://karagila.org/files/Forcing-2023.pdf),
explicitly updated **24 August 2026**, complete Section 9, printed pp.
43--45, extracted lines 2245--2399. The source puts regularity/strong-limit,
diagonal equivalence and the generic-sequence criterion partly in exercises;
the packet supplies the needed actual arguments. Proposition 9.13's
semiproper/not-proper conclusion is not claimed in this packet.
The existing canonical key `Karagila2026ForcingNotes` is reused, not duplicated.

[Gitik's actual author-hosted `hbg1.07.pdf`](https://www.math.tau.ac.il/~gitik/hbg1.07.pdf),
linked as the Handbook chapter from the [author's paper list](https://www.math.tau.ac.il/~gitik/somepapers.html):
107 PDF pages. Read contents/introduction and all of Section 1.1,
draft pp. 1--8, extraction lines 1--256, through 1.13 and its criterion
proof; also bibliography entries 25/26/38/47. Internal revision/publication
date is not qualified merely from `hbg1.07`. All later section bodies are
unread; their actual contents list distinguishes tree, one-element,
supercompact/strongly compact, extender, Radin/Magidor and iteration routes.
No equivalence with the published 2010 manifestation is asserted.

[Mathias's native publisher article](https://doi.org/10.1017/S1446788700028755),
*On sequences generic in the sense of Prikry*, J. Austral. Math. Soc.
15(4), **June 1973**, pp. 409--414: complete paper read, 250 extraction
lines and all six source-page images. Its received 1969, revised 1970,
published 1973 and online 2009 dates remain distinct. Exact important
locators are Definitions 0.1--0.10 (source types and order), Definition
1.3 and Lemma 1.4 (normality), Theorem 1.6 (finite homogeneity), Theorems
2.1--2.2 (Prikry preservation and genericity), Lemma 2.5 (dense-set capture),
and Lemma 2.6 (direct decision). This is a native 1970s primary source,
not Prikry's original monograph under a different name.

The original Prikry volume-68 body was not obtained or read. Its indexed
[primary DML-PL catalog](https://pldml.icm.edu.pl/pldml/element/bwmeta1.element.desklight-3d721e6c-6332-4a74-89e5-a5bd45e5d51f)
dates it 1970; Mathias's literal reference gives 1969 and the Berkeley
1968 dissertation; Gitik's reference 47 gives 1970 and 68:55. These are
retained referrals pending exact original-manifestation qualification,
not a fabricated resolution of the bibliographic difference.

All source binary/extraction hashes are frozen in
`source/references/p06-prikry/SOURCES.md`.

## Ten reciprocal proof developments supplied

All statuses below are authored `proved=` pairs, not independent admission.

1. **Measure tools:** small sets cannot be measure one, every tail is
   measure one, kappa regular and strong limit; regressive/diagonal/
   finite-stem normality equivalence, with the max-stem index bound.
2. **Finite homogeneity:** a complete arity induction for fewer than kappa
   colors and the final countable intersection, not an unproved
   invocation of Rowbottom's theorem.
3. **Actual orders:** finite increasing stem plus normal-measure-one tail,
   full and direct orders, partial-order checks, direct intersection
   bounds, same-stem compatibility, kappa-plus chain condition, and an
   explicit countable full-order closure failure.
4. **Generic sequence:** canonical name for the graph, length and
   unboundedness dense sets, eventual containment in every ground measure
   set, exact filter recovery and M[G]=M[C].
5. **Prikry lemma:** three decision colors, chosen same-stem decision
   tails, finite-stem diagonalization, all-arity homogeneity, and actual
   dense same-decision conditions. Final forcing uses the existing
   recursive density theorem, not generic truth as a definition.
6. **Strong dense-set lemma:** a separate construction giving a uniform
   finite level and all longer pure-tail stem additions in a ground
   dense open set. It does not assume the preceding decision theorem.
7. **No bounded subsets:** fewer-than-kappa direct fusion decisions,
   exact tail-intersection lower bound, ground membership set by
   Separation, and the check-name/existential-density argument forcing
   equality with that ground set. Empty bounded domain handled explicitly.
8. **Preservation:** bounded graph codes below kappa, a separate argument
   at kappa using its ground limit-cardinal property, possible-value
   maximal antichains above kappa, and complete cofinality classification.
9. **Measure loss:** kappa remains a singular strong limit; it is not
   measurable in the extension, and the new countable family of ground
   tails has empty intersection, exposing the internal-completeness boundary.
10. **Mathias criterion:** filter checks and a ground diagonal family of
    dense-set captures; every eventual-measure-one omega sequence meets
    all ground dense sets. The finite initial stems and their capture
    thresholds are explicit.

The worked next-point example separates decision of a fixed proposition
from decision of an arbitrary kappa-valued name, and separates direct
closure from full-order closure. No kappa-long fusion is asserted.

## Presentation variants retained

Gitik's author draft writes stronger conditions with greater-than-or-equal
and direct greater-than-or-equal-star. The local packet explicitly translates
to the existing smaller-is-stronger recursive forcing convention, preserving
the stem/tail clauses. Mathias's native order has the smaller-is-stronger
orientation already, but its finite-subset notation has a separate stem
height; that source notation is not confused with sequence length.

Mathias takes finite-stem thinning as a normality definition and proves
its diagonal equivalence; this packet states the regressive version and
supplies every equivalence direction needed to reach the same thinning.
His Theorem 1.5 (Scott normalization from a general two-valued measure)
is a separate cited source duty. The current construction starts with an
explicit normal measure and does not claim to prove that normalization.
Mathias allows proper-class grounds via theorem/proof schemata; this
packet retains the existing transitive set-ground framework rather than
claiming an unconstructed class-extension result.

## Integration seam, remaining work and standing

Root-owned seam: insert
`handbook/parts/p06/prikry-forcing-and-cofinality.tex` after recursive
forcing and the measurable-cardinal vocabulary, before generalized
cofinality-change forcing applications; route the matching annex through
the live P6 annex. Merge `intake-p06-prikry.bib` and
`symbols-intake-p06-prikry.csv`. The Karagila canonical key already exists.
No new literal calculus rule display is created.

There is no intentionally open proof step in the local classical
normal-measure construction at its stated premises. It depends on the
current general recursive forcing packet, whose independent review status
is not upgraded by this authoring block. Generic existence is supplied;
external countability gives the familiar dense-set enumeration when
available, not a consequence of Con(ZFC).

The entire published Gitik chapter, Prikry's original monograph, Scott
normalization and original source referrals remain separate duties.
Unwritten variants include tree/non-normal measures, one-element forcing,
many Prikry sequences, supercompact/strongly compact forcing, extender
forcing, interleaved collapses/down to aleph-omega, Radin/Magidor forcing,
uncountable target cofinalities and iterations. These are not covered by
the classical cardinal-preservation theorem merely because their names
contain Prikry.

Next useful source step: qualify the exact published 2010 manifestation
against the held author draft and acquire the original Prikry body.
Next mathematical/source component: Gitik draft Section 1.2 tree Prikry
forcing, replacing global normality by measure-one successor sets and
its level-by-level direct decision construction. That entire body is
still unread here.

No children, reviews, tests, builds or manuscript renders were run. The
six Mathias source-page images were used solely for exact historical reading.
