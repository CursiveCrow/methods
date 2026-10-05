# Packet w02b-p15-044: provenance note

Part P15, chapter 166, section 166.7 ("Existence, uniqueness, multipliers and
reference-measure dependence"). Label tag `p15-w02b-p15-044`. Heading level `\chapter`.

## Owned files

- Body: `handbook/parts/p15/information-and-description-based-inference-w02b-p15-044.tex` (266 lines)
- Annex: `handbook/annex/p15/information-and-description-based-inference-w02b-p15-044.tex` (207 lines)
- Symbol intake: `handbook/registry/symbols-intake-p15-information-and-description-based-inference-w02b-p15-044.csv`
- Bib intake: none (only `HajekStaffel2021Dynamics`, already in handbook.bib). An earlier draft
  created an intake with `Shannon1948MathematicalTheory`; it was deleted when the Shannon
  citations were dropped (see below).
- Patch request: `work/waves/w02b/patches/w02b-p15-044.json` (one insert_after on the read-only
  host `handbook/parts/p15/rationality-4-1.tex`, after the factory/reparameterization paragraph).

## Sources held and opened in this session

- Hajek and Staffel 2021, `source/references/p15-rationality-4-1/hajek-staffel-2021-publisher.pdf`.
  Printed p. 244 (left column): entropy generalization of indifference to the maximum-entropy
  principle under a constraint, Jaynes named as advocate; van Fraassen cube factory (side
  length up to 1 foot; answer 1/2 for side length, 1/8 for volume, "yet another answer" for face
  area, value not printed); Norton, White, Novack for defenses.
- Shannon 1948 corrected reprint (opened; Section 20 pp. 35-38 read). Not cited in the final text:
  packet w02b-p15-042 presents Section 20 (items 1-9) in full, so this section links to it.

## Overlap found and resolution (A9)

When work began, none of the sibling files existed. During the session, packets w02b-p15-040,
041, 042 and 043 wrote their chapters. Packet w02b-p15-043 (section 166.6) supplies the
general declared problem, Gibbs identity, dual bound, optimality, uniqueness, partition
lemma, existence of multipliers (regular, minimal), finite case with boundary values, failure
cases (including a non-attainment with the dual minimizer on the edge of the domain),
normalization, transport and constant rescaling, and power-family reference examples.
Packet w02b-p15-042 supplies the entropy shift under reference change and Shannon's items 5-8.
A first draft of this section duplicated most of that; it was rewritten to link to those
labels and to keep only material they do not contain:
1. thm:p15-w02b-p15-044-attainment: attainment criterion from the dual value; dual minimizers
   vs. feasible family members; an interior dual minimizer certifies the maximizer without
   regularity or minimality.
2. thm:p15-w02b-p15-044-reference: reference change by a nonconstant density as a statistic
   ln rho with fixed multiplier -1; affine test (multipliers shift by a, same maximizers);
   disjointness of the families when ln rho is not affine.
3. thm:p15-w02b-p15-044-cubes and def:p15-w02b-p15-044-cube-example: the Hajek-Staffel
   factory on (0,1] with references for side length, face area, volume; unconstrained answers
   1/2, 1/4, 1/8; with declared mean 1/2 the answers 0.5000, 0.5188, 0.5280; pairwise
   distinctness proved.
4. def:p15-w02b-p15-044-procedure and def:p15-w02b-p15-044-limits.
The body depends on these sibling labels (all present at time of writing):
sec:p15-w02b-p15-043-maxent, -multipliers, -jaynes; def:p15-w02b-p15-043-problem, -partition,
-method, -reference-example; thm:p15-w02b-p15-043-gibbs, -optimality, -existence, -finite,
-failures, -transport, -partition, -no-constraint; thm:p15-w02b-p15-042-reference-change.

## Numerical values

Cube example, multipliers in Jaynes's sign (density proportional to l^s exp(-lambda l)).
Computed with mpmath (30 digits): lambda_1 = 2.6879993, P(l <= 1/2) = 0.51883046;
lambda_2 = 5.0714697, P(l <= 1/2) = 0.52802894; s = 0 gives lambda = 0 and 1/2 exactly.
Analytic brackets in the annex: m_1(10) < 0.21, m_2(10) < 0.31 (numerical m_2(10) = 0.2977).

## Assessment items for the RAT2021 4-1 unit

The computed task listed disputes on ED26-BM-RAT2021-4-1 (Cox pointer, KL repair numbers
(0.438, 0.572) vs (3/7, 4/7), Brier practical-use claim, comparisons with rationality-4-7 and
rationality-5-3, finite dependent-source set). That unit is owned by w02b-p15-022
(readonly_units); none of those items was written here. One link is supplied: the
maximum-entropy generalization in rationality-4-1 (HS p. 244, host lines 335-349) is mapped
to sections 166.6 and 166.7 by the patch request.

## Continuation

- Done this session: body and annex rewritten to the non-duplicating scope above; symbol
  intake; patch request; unit-compile ok with 0 overfull; find_fused_spaces clean; check.py
  shows no finding in the owned files.
- Open for the lead: apply the rationality-4-1 patch; keep the cross-packet labels of 042/043
  stable or retarget this section's references if they change; three intake bibs (040, 041
  and the deleted draft here) used `Shannon1948MathematicalTheory` while 042 uses
  `ShannonMTC1948Reprint` for the same reprint.
