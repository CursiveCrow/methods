# Edition 2026 P17: restricted decisions and binary testing

Date: 8 September 2026. Author: /root. Scope: P17.8.
The body and full annex are written, read back and connected to the P17
drivers after value-of-information. The canonical notation is integrated.
Consolidated reviews remain deferred until all manuscript changes are made.

## Exact source and supplied scope

The primary is the acquired Blackwell 1953 paper, bibliography key
Blackwell1953EquivalentExperiments:
source/references/blackwell-equivalent-experiments-1953/blackwell-1953-equivalent-comparisons.pdf.
Its SHA-256 is F490B8395187EDC34AB46A3D45455F1F59CBBC9632964C63218A2F4C8BA8CD1D.
The acquisition and original complete eight-page reading are recorded in
edition-2026-p17-value-of-information.md. Before this writing root reread
the complete scanned pages 269–272, including the Section 5 hull lemma,
both applications, all of Theorems 9–11, the two-state corollary and its
coordinatewise affine-map proof, and the testing-error paragraph.

The chapter supplies the finite-signal forms, with complete constructive
proofs. It retains the source's deterministic partition and convex-mixture
arguments, its loss-hull converse, its finite-support supporting-function
selection, its least-maximizer partition, the two-linear-piece reduction
and the line-segment risk transformation. The finite matrix separation
argument is also supplied as a direct alternative. The source's uniform
standard measure is the uniform-prior case of the proved full-support
posterior formulation. No general observation-space result is inferred
without its additional kernel and measure constructions.

The product weights use every signal coordinate, correcting the printed
upper-index issue identified in the earlier source note. The actual lower
testing boundary at size zero is stated correctly for singular signal
laws; the always-accept point belongs to the region even when it is above
that lower boundary. Source pages 269–272 have not been reproduced.

## Complete authored statements and proofs

Body: handbook/parts/p17/restricted-decisions-binary-testing.tex,
319 lines, 13,511 bytes, SHA-256
CD1875B296717A04D7BD91240296CF708A5ED6F5C213814FAC5B30323F06CABA.

Annex: handbook/annex/p17/restricted-decisions-binary-testing.tex,
468 lines, 22,957 bytes, SHA-256
DE3B842CABE2CC824D97872120A76853DB1512013AC3357B5BF27CAA00163A3F.

The nine reciprocal suffixes use thm:p17- and annex:p17.:

- randomized-decision-hulls: explicit deterministic selection weights,
  arbitrary nonempty loss generating sets and diagonal risk images.
- finite-k-comparison: all five comparisons, the direct separator and all
  source loss-set, finite-support and deterministic-partition proof routes.
- k-comparison-hierarchy: preorder, the one-action equivalence, nesting,
  padding and the sufficient output-count bound for full dominance.
- convex-hinge-decomposition: all pairwise affine intersections, continuity,
  nondecreasing slopes and every nonnegative hinge coefficient.
- binary-two-decisions: common posterior means and the reduction of every
  finite-action problem to two-action comparisons.
- testing-error-region: complete compact vertical sections, central symmetry,
  convexity, monotonicity, exact/at-most size optima and both curve equivalences.
- finite-likelihood-optimality: explicit ratio ordering, singular signals,
  fractional threshold, tied blocks and the complete threshold inequality.
- repeated-experiment-comparison: row normalization and an explicit product
  garbling certificate at every positive sample size with a fixed state.
- testing-calculations-boundaries: one- and two-observation error curves,
  unavailable deterministic sizes, disjoint supports and the complete
  dependent-joint counterexample with equal uninformative marginals.

The numerical two-observation calculation gives error 3/10 at size 1/10,
compared with 3/5 for one observation. The dependent counterexample has
state-guessing values 1/2 and 1, despite identical single-coordinate laws.
All tables are stipulated mathematical examples. The likelihood-ratio
construction is a handbook derivation; the source supplies the error-region
comparison rather than that full explicit sorting calculation.

The prior value-of-information body now points to this chapter. Its current
body hash after that forward-reference update is
1998D2B069B1FA5577F08667C5BF456FAE9CEAB16BE5215DDA977A65F092D5BA;
its full annex retains
1913B9035ACFB7CD9907414E2C55FBE7B7301D8982EA6B4C4306115EDCFB95F0.

Remaining writing includes the general observation-space Blackwell
construction and its corrected weak-convergence step, sequential decision
models and the approved further strategic regimes. The finite component
does not assert those additional results or identify a preferred empirical
test for unspecified data. No new tests, manuscript renders or independent
review tasks were created for this chapter.
