# Packet w02b-p15-045: provenance note

Part P15, chapter 166, section 166.4 ("Relative information and
Kullback--Leibler divergence"). Label tag `p15-w02b-p15-045`. Heading level
`\chapter`. toc tag `%% toc: P15 166 166.4`.

## Owned files

- Body: `handbook/parts/p15/information-and-description-based-inference-w02b-p15-045.tex`
- Annex: `handbook/annex/p15/information-and-description-based-inference-w02b-p15-045.tex`
- Bib intake: `handbook/bib/intake-p15-information-and-description-based-inference-w02b-p15-045.bib`
  (one key, `KullbackLeibler1951Information`)
- Symbol intake: `handbook/registry/symbols-intake-p15-information-and-description-based-inference-w02b-p15-045.csv`

## Held source opened in this session

- S. Kullback and R. A. Leibler, "On Information and Sufficiency", Ann. Math.
  Statist. 22(1) (1951) 79--86. Held file
  `source/references/acq-r1-ACQ-2026-10-0362/kullback-leibler-1951-information-sufficiency.pdf`
  (8 PDF pages, image-only JSTOR scan; PDF page n = printed page 78+n). All 8
  pages read as images in this session. Locators used:
  - p. 79: Sec. 1 (generalization of Shannon; Halmos--Savage quotation;
    Jeffreys' divergence); Sec. 2 opening (probability spaces (X,S,mu_i),
    mu_1 == mu_2, lambda == {mu_1,mu_2}, lambda a probability measure, e.g.
    mu_1, mu_2 or (mu_1+mu_2)/2); footnote 1 (perfect discrimination when
    some E has mass under one measure only; mutual absolute continuity
    assumed to avoid it).
  - p. 80: (2.1) densities, 0<f_i<infinity [lambda]; (2.2) information in x;
    (2.3) I_{1:2}(E), 0 when mu_1(E)=0; existence of the integral, possibly
    +infinity, since the measures are finite (footnote 3); Lemma 3.2 quoted
    in the form "for mu_1(E)>0"; (2.4) I(1:2); footnote 2 (Bayes reading);
    footnote 3 (E=(0,1), mu_1 Lebesgue, f_2/f_1 = k e^{-1/x}, I(1:2)
    infinite); footnote 4.
  - p. 81: (2.5) J_12(E); (2.6) J(1,2), "divergence"; Shannon generalization
    paragraph; (2.7)--(2.9) Fisher matrix expansion "with suitable
    assumptions"; (2.10) normal case.
  - p. 82: Sec. 3; Lemma 3.1 (almost positive definite) with proof
    (3.1)--(3.5); Lemma 3.2 statement "for lambda(E)>0" and proof; Theorem 3.1
    statement (additivity for independent random events); footnotes 6, 7.
  - p. 83: proof (3.6); Sec. 4: T onto (Y,T,nu_i), nu_i(G)=mu_i(T^{-1}G),
    gamma = lambda T^{-1}; (4.1)--(4.3); Theorem 4.1; its proof begins
    ("If I(1:2)=infinity the result is trivial"; Lemma 3 of Halmos and
    Savage; (4.4), (4.5)).
  - p. 84: (4.6)--(4.8), mu_12; Corollary 2, Theorem 1, Lemma 2 of Halmos
    and Savage invoked; Corollary 4.1 (non-singular T); Theorem 4.2 and (4.9);
    footnotes 8, 9.
  - p. 85: Sec. 5 (identical results for J; symmetric; independent of a
    priori probabilities); Sec. 6 (1) (6.1) and (2) (6.2)--(6.6).
  - p. 86: conclusion of Sec. 6 (2): J = 0.1986, grouping (p1),(p2+p3+p4),
    .1193/.1986 = .6007, "loss of 40%"; references.
- Notation kept from the source: (X, S, mu_i), lambda, f_i, [lambda],
  H_i, I_{1:2}(E), I(1:2), J_12(E), J(1,2), g(x), phi(t)=t log t, h(x),
  I_x, I_y, I_xy, f_i^{(1)}, f_i^{(2)}, lambda_1, lambda_2, T, (Y, T, nu_i),
  gamma, g_i, I'_{1:2}(G), I'(1:2), J'_12(G), mu_12, alpha_i, P(H_i|x),
  and the symbol == for mutual absolute continuity / same null sets
  (declared locally in the body).

## Corrections recorded (correction policy of 2026-09-06)

1. Theorem 4.1, infinite case. The source proof says the infinite case is
   trivial. That is true for the inequality only. When I(1:2)=infinity,
   equality I(1:2)=I'(1:2) can hold for a statistic that is not sufficient:
   product of the footnote-3 pair (infinite information) with a binary pair
   of finite positive information, T = first coordinate. The body states
   the inequality in general, "sufficient implies equality" in general, and
   "equality implies sufficient" under I(1:2) < infinity, and proves the
   counterexample (thm:p15-w02b-p15-045-infinite-equality).
2. Theorem 4.2 has the same defect; stated under I(1:2) < infinity, and the
   same example shows the forward implication fails without it.
3. Sec. 6 (2), p. 85: formula (6.2) with p = (.5,.3,.1,.1), k = 4, base-10
   logs gives J' = .1193, .1806, .0716, 0 for r = 1,2,3,4. The printed r = 2
   value is .0903 (exactly half). With .1806 the maximum is at r = 2,
   efficiency .1806/.1986 = .9095 (loss about 9%), not r = 1 with .6007
   (loss 40%) as printed on p. 86. Recomputed with Python in this session.
   The body reports the printed values and the recomputation.

4. Sec. 6(1), p. 85: KL say I_{1:2}(G) < I_{1:2}(F) "may be readily
   verified". Reading (6.1) through (2.3), the difference is
   log(alpha(1-c)/(2c(1-alpha))) - (1/2) log(p(1-p)); the inequality holds iff
   alpha(1-c) > 2c(1-alpha) sqrt(p(1-p)) (always for c < alpha; never for
   p = 1/2, c >= alpha). Lehmann 1950 (p. 2), which fixes the parameter range,
   is not held, so whether KL's claim holds on Lehmann's range is unverified.
   The body states the condition (thm:p15-w02b-p15-045-critical).

## Session 2 additions (4 October 2026)

- Pages 81, 82 (top), 85 and 86 of the held KL scan re-read as images in
  this session (rendered with PyMuPDF at 200 dpi). Locators used: p. 81
  (2.7)-(2.9) "with suitable assumptions", reference to p. 774 of [4]
  (Doob 1934); (2.10); p. 82 top: J in (2.10) is k times Mahalanobis'
  generalized distance [13]; p. 85 Sec. 6(1), (6.1), Lehmann p. 2 of [20];
  p. 86 reference [20] = Lehmann, Ann. Math. Stat. 21 (1950) 1-26.
- (2.7)-(2.9): hypotheses R1-R3 are the chapter's own (sufficient
  conditions; not Doob's, which are not held). Proof: differentiation of
  int f = 1 twice under the integral (R2), Taylor with integral remainder,
  Fubini on [0,1] x X, dominated convergence (R3), both directions for J.
- (2.10): proved for every k without a k-dimensional change of variables:
  mu_i is the image of the product standard normal under z -> m_i + Az;
  T(x) = A^{-1}(x - m_2) is non-singular (Corollary 4.1), image pair is a
  product of (N(d_j,1), N(0,1)), additivity (Theorem 3.1) plus the k = 1
  computation. The "k times Mahalanobis" identification is reported as the
  source's statement; Mahalanobis 1936 is not held.
- Disputes C01 and C05 closed in the text: new def:p15-w02b-p15-045-extension
  and thm:p15-w02b-p15-045-extension; thm:p15-w02b-p15-045-support part (1)
  now uses two-sided mixtures (no mu_2 << mu_1), part (2) proves
  I^eps(2:1) <= (1-eps) I(2:1) and I^eps(2:1) -> I(2:1) (convexity, Fatou).

## Existing treatments found (linked, not repeated)

- `handbook/parts/p16/rationality-4-2.tex` def:p16-rat42-kl (finite directed
  divergence, non-metric remark).
- `handbook/parts/p15/rationality-4-1.tex` sec:p15-rat41-dynamics (finite
  relative entropy in minimal-change updating).
- `handbook/parts/p15/rissanen-structural-and-numerical-inference.tex`
  thm:p15-rmdl-gibbs (countable Gibbs inequality).
- `handbook/parts/p15/robust-sequential-endpoints.tex`
  thm:p15-directional-log-integrability (relative entropy as extended mean of
  a log score, singular mass).
- `handbook/parts/p15/rationality-4-3.tex` thm:p15-r43-sufficiency (finite
  binary experiment, likelihood ratio minimal sufficient).
- `handbook/parts/p15/sequential-evidence.tex` thm:p15-se-information (Wald
  information lower bounds) -- uses expected log likelihood ratios.
- `handbook/parts/p15/huber-information-game.tex` (Fisher information game).
- Measure tools reused: thm:p15-radon-nikodym, thm:p15-density-calculus,
  thm:p15-conditional-existence, thm:p15-conditional-pullout,
  thm:p15-tonelli, thm:p15-product-existence, thm:p15-monotone-integral.
- Not listed in the packet: `information-and-description-based-inference-w02b-p15-044.tex`
  (same wave, 166.7) defines D(P||Q) with +infinity off absolute continuity
  and proves its nonnegativity (thm:p15-w02b-p15-044-gibbs-inequality). That
  file belongs to another packet in progress; it is not cross-referenced
  because its labels may still change. The present chapter's statements
  are in KL's notation and hypotheses.

## Continuation

- Session 1 (4 October 2026): body (701 lines) and annex (693 lines, 16
  annexitems) written for C01-C05; bib and symbol intakes written; return
  JSON written. Checks: unit-compile ok (10 overfull boxes, each under 5pt),
  find_fused_spaces clean, check.py shows only the own-intake bib-key.
- Open items for a later session (KL 1951 results outside C01-C05, not
  written): (2.7)-(2.9) Fisher-matrix expansion (no hypotheses in source);
  (2.10) for k > 1 (needs a multivariate-normal result; k = 1 is in
  thm:p15-w02b-p15-045-not-metric); Sec. 6(1) example (6.1) (needs Lehmann
  1950, not held).
- Driver insertion (parts/p15.tex after line 84, annex/p15.tex after line
  83) is for the lead.
- Session 2 (4 October 2026): closed the three source-extent items
  ((2.7)-(2.9) thm:p15-w02b-p15-045-fisher; (2.10) all k
  thm:p15-w02b-p15-045-normal; (6.1) thm:p15-w02b-p15-045-critical) and the
  C01/C05 disputes (def/thm:p15-w02b-p15-045-extension, support theorem
  rewritten). Body 994 lines, annex 1091 lines, 20 annexitems. Checks:
  unit-compile ok (10 overfull, each under 5pt), find_fused_spaces clean,
  check.py only the own-intake bib-key.
- Open: Lehmann 1950 p. 2 (not held) is needed to confirm KL's "readily
  verified" claim in Sec. 6(1) on Lehmann's parameter range.
- Session 3 (4 October 2026): held KL scan (SHA digest 16c2c13e...) re-opened at
  pp. 82-85 as images. Section 5 (p. 85) checked: J counterpart asserted for
  every result of Secs. 3-4 (Lemma 3.1, Lemma 3.2, Theorem 3.1, Theorem 4.1,
  Corollary 4.1, Theorem 4.2); Jeffreys (par. 3.9) noted symmetry, positive
  definiteness, additivity and invariance for non-singular transformations.
  Added thm:p15-w02b-p15-045-j-counterparts (J versions of Lemma 3.2,
  Corollary 4.1(1), Theorem 4.2; the last with J < infinity for the converse)
  with annex proof; infinite-equality example part (3) for J. Grouping
  example now assumes p_k > 0 and works the p = (0.6,0.4,0) case. Body 1077
  lines, annex 1172 lines, 21 annexitems. Checks: unit-compile ok (12
  overfull, each under 5pt), find_fused_spaces clean, check.py only the
  own-intake bib-key.
- Open: driver \input lines (parts/p15.tex after line 84, annex/p15.tex
  after line 83) for the lead; Lehmann 1950 p. 2 (not held).
- G1 guard hits on w02b-p01-014 and w02b-p02-036 research notes are other
  packets' files; not touched.
- Session 4 (4 October 2026): the only gap listed was G1 on
  spec/research/edition-2026-p01-symbol-registry-w02b-p01-014{.md,-return.json}
  and spec/research/edition-2026-p02-fol-metatheorem-table-and-nd-cpl-sheet-w02b-p02-036{.md,-return.json}.
  Checked: untracked, timestamps 22:34 and 18:23, written by the
  unit_accounting packets w02b-p01-014 and w02b-p02-036, whose owned_files
  lists are empty, so the G1 scan (tools/waves.py, wave_packet_paths
  attribution) cannot attribute them to any packet and reports them against
  every packet. This packet did not write them and may not edit or delete
  them. Needed (lead): add each note and return path to the owned_files of
  its packet (or exempt unit_accounting notes from the scan) and re-snapshot.
  No content change this session. Lehmann 1950 still not held. Checks:
  unit-compile ok (12 overfull), find_fused_spaces clean, check.py only the
  own-intake bib-key.
