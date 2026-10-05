# P15 166.3 continuous entropy, coordinates and reference measures (packet w02b-p15-042)

## Provenance

- Packet: `work/waves/w02b/packets/w02b-p15-042.json`, label tag `p15-w02b-p15-042`,
  heading level `\chapter`, toc tag `%% toc: P15 166 166.3`.
- Duty MP-0 (166.3 share): the reference-measure part of the allocated
  entropy method: continuous (differential) entropy relative to an explicit
  reference measure and coordinate with integrability conditions; Shannon
  Section 20 continuous properties with proofs; the coordinate-change formula
  and its linear case; a worked change-of-coordinates boundary.
- Readonly units (A14): ED26-METHOD-entropy is owned by w02b-p15-040 (166.1,
  discrete entropy, characterization, joint/conditional finite properties,
  semantic separation, discrete dependence comparison);
  ED26-BM-RAT2021-4-1 is owned by w02b-p15-022. This packet writes only the
  continuous/reference-measure share named in the assessment gap.

## Held source opened in this session

- `source/references/acq-r1-ACQ-2026-10-0320/shannon-1948-mathematical-theory-communication.pdf`
  (55-page corrected reprint; p. 1 header "Reprinted with corrections from
  The Bell System Technical Journal, Vol. 27 ..."). PDF page = printed page.
  Read with pdftotext: pp. 1--2 (logarithmic base as unit; bits; natural
  units; base change), p. 10--11 (Section 6; Theorem 2 on p. 11; the
  notation H(x) as a label, p. 11), pp. 34--35 (Section 19, n-dimensional
  density p(x_1,...,x_n) for band-limited ensembles), pp. 35--38 (Section 20:
  definitions of H, H(x,y), H_x(y), H_y(x) p. 35; property 1 p. 35;
  properties 2--5 p. 36; properties 6--7 p. 37; property 8 pp. 37--38;
  remarks on coordinate standard, differences and negative entropy p. 38;
  property 9 p. 38).
- Source notation kept: H(x), H(x,y), H_x(y), H_y(x), p(x), p(x,y),
  a(x,y), p'(y), A_ij, a_ij, |a_ij| (Shannon's determinant), J(x/y).
  Shannon's J(x/y) is written inside a logarithm; the chapter reads it as
  the absolute value of the Jacobian determinant of x with respect to y.

## Existing treatments found

- `handbook/parts/p15/measurement-uncertainty.tex` lines 224--247 and annex
  `annex:p15.measurement.asymmetric-model`: differential entropy relative to
  the chosen numerical coordinate and the maximum-entropy density on a
  bounded interval with fixed mean (Gibbs argument). Linked, not repeated.
- `handbook/parts/p15/convolution-gamma-normal.tex`: densities relative to
  Borel Lebesgue measure, one-variable affine substitution, normal law.
- `handbook/parts/p15/characteristic-function-criteria-and-moments.tex`
  `thm:p15-criteria-real-integration`: one-variable monotone C^1 substitution.
- No handbook proof of the multivariable C^1 change-of-variables theorem
  exists; the chapter makes the Jacobian identity an explicit hypothesis and
  proves it for linear and affine maps, one-variable monotone C^1 maps and
  products.

## Background facts used without a handbook proof

- Determinant multiplicativity and the determinants of the three elementary
  matrix types (linear algebra, used in the linear Lebesgue lemma).

## Continuation

- Session 1 (4 October 2026): body (15 results, method, example, warning,
  relationships) and annex (15 annexitems) written for the 166.3 share of
  MP-0. unit-compile ok; check.py hard finding only bib-key for the own
  intake key ShannonMTC1948Reprint; find_fused_spaces clean.
- Open: multivariable C^1 change of variables (n >= 2) is a stated
  hypothesis, not proved in the handbook; the cross-reference to the 166.1
  chapter of w02b-p15-040 needs its label once it exists (body lines 26--30).
- Not written here (A14 readonly units): ED26-METHOD-entropy discrete
  share (C01 discrete domain, C02, C04 full separation, C05 discrete
  dependence comparison) owned by w02b-p15-040; ED26-BM-RAT2021-4-1 owned
  by w02b-p15-022. ED26-GAP-SCI-001-C01..C04 are closed (open=false) in the
  packet with their treatment in measurement-uncertainty.tex; not modified.
- Session 2 (4 October 2026, continuation r3): assessment gaps ED26-BM-RAT2021-4-1 C03
  and C05 were routed to this packet, but the unit is readonly here (owner
  w02b-p15-022) and the host rationality-4-1.tex is a readonly host; nothing
  was authored for them. Verified for the lead in the held file
  source/references/p15-rationality-4-1/hajek-staffel-2021-publisher.pdf,
  PDF page 9 = printed p. 247: the source reports the Kullback-Leibler closest
  coherent function for <0.3, 0.4> as C*(p) = 0.438, C*(~p) = 0.572 (sum 1.010).
  Host rationality-4-1.tex lines 572-576 give (3/7, 4/7) and do not record the
  reported values. For C05, the owner packet has written the finite
  dependent-source set (sec:/tab:p15-w02b-p15-022-dependent-sources); host
  lines 161-162 still say the primary axiomatizations "remain separately
  identified presentations" with no pointer. Exact host changes are in the
  return file. Own files re-checked: unit-compile ok, check.py only own bib-key,
  fused spaces clean. Packet w02b-p15-040 now has sec:p15-w02b-p15-040-information;
  the crosslink at body lines 26-30 stays a request until that chapter is on the input route.
- Session 3 (4 October 2026, continuation r4): assessment gaps
  ED26-BM-RAT2021-4-1 C01, C03, C04, C05 routed again. The unit is readonly here
  (owner w02b-p15-022) and rationality-4-1.tex is a readonly host.
  - C04 (the part that lives in section 166.3): owned body lines 418-433 add
    thm:p15-w02b-p15-042-power-coordinates (annex lines 552-595, full proof);
    body lines 529-580 add the comparison with the source's continuous
    generalization and cube factory (Hajek and Staffel p. 244, read this session
    with pdftotext from source/references/p15-rationality-4-1/hajek-staffel-2021-publisher.pdf),
    a 3x3 table of each uniform prior's entropy in each coordinate, transport
    versus reimposition (thm:p15-bayes-transformation), and the preserved
    objection (Norton, White, Novack as defenders). References
    sec:p15-rat41-synchronic and thm:p15-rat41-indifference; refers to
    thm:p15-w02b-p15-044-cubes/-reference instead of repeating them.
  - Patch requests for the host: work/waves/w02b/patches/w02b-p15-042.json
    (6 entries, anchors checked unique against host SHA-256 digest ec91719a...):
    C04 reverse link; C01 information loss/self-location (no handbook credal
    unit; nearest def:/thm:p17-rat91-memory); C01 alternatives mapped to
    def:p15-r47-mass, sec:p15-r47-evidence, sec:p15-ip-conditioning,
    sec:p15-rationality-5-3, def:/thm:p15-r47-ranking, sec:p15-r47-modal,
    def:p08-agm, thm:p08-agm-representation, sec:p08-ranked-models-rational-closure;
    C03 two readings of an empty cell and growth statement (p. 247) and the
    ellipsis row/column of Table 4.1.1 (p. 248); C05 pointer to
    tab:p15-w02b-p15-022-dependent-sources (conflicts with w02b-p15-041's
    replacement at the same anchor; one must be chosen).
  - Not re-filed: the KL figures 0.438/0.572 (p. 247) are in w02b-p15-041's
    patches (same anchor region); filing again would double-insert.
  - Assessment-suggested labels sec:p15-w02b-p15-025-ranking and
    sec:p15-r43-rankings rank evidence by confirmation measures; not used.
  - Hard-guard G1 files (spec/research/edition-2026-p01-symbol-registry-w02b-p01-014*,
    edition-2026-p02-fol-metatheorem-table-and-nd-cpl-sheet-w02b-p02-036*) are
    untracked notes of packets w02b-p01-014 and w02b-p02-036; this packet never
    wrote them and did not touch them.
  - Checks: unit-compile ok (20 overfull, none fatal); check.py only own
    bib-key ShannonMTC1948Reprint; find_fused_spaces clean.
- Session 4 (4 October 2026, continuation): G8 fixed (line 99 token rewritten
  as "SHA-256 digest"). G1 files are other packets' untracked notes; not
  touched (A8), reported for the lead. Closed the earlier open item on the
  multivariable change of variables: body def:p15-w02b-p15-042-coordinate-change
  gains case 4 (C^1 diffeomorphisms, j = |det DT|), new
  thm:p15-w02b-p15-042-diffeomorphism (body lines 343-355), full proof
  annex:p15-w02b-p15-042-diffeomorphism (annex lines 433-608; uses
  thm:p15-finite-product-measures, thm:p15-w02b-p15-042-linear-lebesgue,
  thm:p15-monotone-integral, thm:p15-measure-laws, thm:p15-measure-uniqueness,
  thm:p15-measurable-limits). Remaining open: the inverse function theorem is
  not proved in the handbook, so the lemma assumes the inverse is C^1.
  Checks: unit-compile ok (24 overfull), check.py only own bib-key, fused clean.
