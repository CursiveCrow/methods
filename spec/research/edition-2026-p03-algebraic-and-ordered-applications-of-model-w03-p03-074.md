# P3 41.2 Nilpotent groups of class two and further group examples (packet w03a-p03-074)

## Scope of this packet

Section 41.2 had no body/proof region (duty US-1: owned files did not
exist). This packet creates:

- body `handbook/parts/p03/algebraic-and-ordered-applications-of-model-w03-p03-074.tex`
  (`sec:p03-w03-p03-074-nilpotent`, heading `\section`, toc tag `%% toc: P3 41 41.2`);
- annex `handbook/annex/p03/algebraic-and-ordered-applications-of-model-w03-p03-074.tex`
  (`sec:annex-p03-w03-p03-074-nilpotent`).

Both packet units (ED26-SRC-048-0013, Hodges 1993 Appendix A.1-A.6; and
ED26-SRC-049-0011, Eklof, Model-Theoretic Logics ch. XI sections 1-7) are
`readonly_units` owned by w03-p03-073 (section 41.1). Their components are
therefore not written here (rule A14). The body states the dependency in one
sentence (introduction: the source-specific accounts sit with the preceding
section). No 073 labels existed at writing time, so no `\cref` to them was
possible; once 073 publishes labels, a one-line cross-reference could be
added to the introduction paragraph of 41.2.

## Content written (general reference treatment, all proofs in annex)

- Conventions: commutator, left-normed commutators, class laws lambda_k,
  centre and centralizer.
- Upper central series definition; theorem: Z_c(G)=G iff lambda_{c+1};
  monotonicity; closure of each class under subgroups, homomorphic images,
  products, ultraproducts.
- Lemma: lambda_{k+1} iff weight-k commutators central; transfer along a
  surjection with kernel Z(G).
- Lemma: class-two computing rules (bilinearity, power rules,
  (xy)^n = x^n y^n [y,x]^{n(n-1)/2}).
- Heisenberg group H(R) over any commutative ring with 1: group, commutator
  formula, centre, centralizers, class exactly 2 for nonzero R, power formula.
- Theorem: with parameters x,y whose determinant is a unit, the ring R is
  interpreted on the centre (isomorphism zeta(r) -> r delta^{-1}).
- Lemma: the admissible pairs are defined by a first-order formula beta
  (for every commutative ring with 1; the proof uses only a Cramer identity).
- Theorem: Th(R) and Th(H(R)) are many-one equivalent by R-independent
  computable maps (ring-to-group via sigma^sharp; group-to-ring via the
  parameter-free 3-dimensional interpretation and thm:p03-w03-p03-022-transfer).
- Corollary: Th(H(Z)) undecidable (via thm:p02-w02c-p02-003-integers);
  H(K) decidable when Th(K) decidable; finite fields.
- Worked example (2*3 = 6 via commutators; a pair with determinant -1;
  exponents of H(F_p)); failure case (determinant 2).
- Dihedral groups G_{2^k} of class exactly k; nilpotency is not
  first-order (ultraproduct argument, thm:los, lem:nonprincipal-ultrafilter).

## Sources read in this session

- Burris and Sankappanavar, A Course in Universal Algebra, Millennium
  Edition 2012 update (held: `tmp/pdfs/p10-burris-sankappanavar-1981/univ-algebra2012.pdf`,
  key `BurrisSankappanavar2012` already in handbook.bib): Chapter V, section 1,
  exercises on p. 201, Exercise 5(c) (first-order expressibility of "nilpotent of
  class k"). Cited only for that exercise. Re-opened 2026-10-12 (PDF page 215 =
  printed p. 201; Chapter V heading on the preceding pages); locator refined to 5(c).
- Handbook results used by label: def:p03-imaginaries-standing,
  def:p03-imaginaries-interpretation, def:p03-imaginaries-translation,
  thm:p03-imaginaries-quotient-truth, thm:p03-w03-p03-022-transfer,
  sec:p03-w03-p03-022-procedures, thm:p02-w02c-p02-003-integers,
  sec:types-ultraproducts-05, thm:los, lem:nonprincipal-ultrafilter.
- No online sources were read.

## Open items

- Historical attribution of the interpretation of a ring in its Heisenberg
  group (commonly credited to Mal'cev) is not made in the reader text: no
  source for it was opened in this session. If a held or open copy of the
  original or of a textbook account becomes available, an attribution with a
  verified locator can be added to the Relationships paragraph.
- Existing treatments: a handbook-wide search for nilpotent, Heisenberg,
  unitriangular, Mal'cev, Mekler and commutator subgroup found no prior
  treatment of these topics in the handbook (Malcev appears only in P2
  historical remarks on compactness). The packet's `existing` list is empty.

## Symbols

Intake: `handbook/registry/symbols-intake-p03-algebraic-and-ordered-applications-of-model-w03-p03-074.csv`.
Overlap: `\Delta` is a global letter for formula multisets (with
`\Gamma,\Sigma,\Pi`); here `\Delta(g,h)` is a ring-valued function local to
`sec:p03-w03-p03-074-nilpotent`. Proposed decision: keep the local scope.

## Continuation

- Status 2026-10-11: body and annex written; unit-compile ok; fused-space
  check clean; tree check showed only the three ultraproduct labels as
  dangling before they were repointed to in-tree labels (thm:los,
  lem:nonprincipal-ultrafilter, sec:types-ultraproducts-05).
- Remaining: none for US-1 within this packet's own files. The 13 unit
  components belong to w03-p03-073 (readonly units).
- Rerun 2026-10-12 (block 1): files found present; all proofs re-checked step by
  step (Cramer identity, unit criterion, worked example signs, dihedral centre and
  induction, power formula). Changes: intro sentence no longer claims 41.1 already
  carries the Hodges/Eklof accounts (it states the dependency only); Burris locator
  refined to Exercise 5(c) after re-reading p. 201. unit-compile ok; fused-space
  check clean; tree check shows no finding for these files. Return file written.
- Insert-time dependency: thm:p03-w03-p03-022-transfer, sec:p03-w03-p03-022-procedures
  and thm:p02-w02c-p02-003-integers live in wave files not yet input by the drivers.
