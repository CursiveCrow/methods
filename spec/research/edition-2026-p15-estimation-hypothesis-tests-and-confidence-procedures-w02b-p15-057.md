# w02b-p15-057 research note (P15, sections 169.1-169.4)

## Provenance

- Source held and opened this session: `source/references/p15-fisher-estimation/fisher-1922-published-scan.pdf`
  (Fisher 1922, Phil. Trans. A 222, 309-368; physical page = printed page - 308).
  Pages read from pixels this session: printed 328-342 (physical 20-34).
- Every locator written in the new chapter is in 328-342. No other page is cited from this session.
- Handbook prerequisites used by \cref (not re-proved): `thm:p15-iid-series-strong-law`, `thm:p15-clt-iid`,
  `thm:p15-clt-perturbation`, `thm:p15-conditional-existence`, `def:p15-general-conditional-expectation`,
  `def:p15-statistical-experiment`, `def:p15-fe-properties`, `thm:p15-fe-score`, `thm:p15-fe-failures`,
  `thm:p15-fe-cauchy`, `def:p15-confidence-procedure`, `def:p15-bayes-experiment`.
- Algebra checked with sympy: gamma fourth central moment 3k^2+6k; Type III det M = (2F-2/p+1/p^2)/(p-1);
  (m,a) block determinant 2/(p-1) and inverse diagonal ((p^2-1)/2, 1/2) times a^2.

## Direct source qualifications recorded in the reader text

- p. 331-332 "least possible value" claim: true for unbiased statistics under stated premises at fixed n;
  false as a claim over all asymptotically normal sequences (Hodges construction).
- p. 339 cross and scale second differentials hold as equalities of expectations, not samplewise.
- p. 333 / 336: for p <= 1 the Type III location information is not finite (and is zero at p = 0, minus infinity
  for -1 < p < 0); tabulated shape efficiencies at p = 0, 1 evaluate a continued formula, not an information ratio.
- Support {x > m} depends on m, so the regular theorem does not cover the joint Type III MLE.


## Provenance, block 2 (r3 continuation)

- Same held scan reopened. Pages read from pixels this session: printed 334, 335, 336, 337
  (physical 26-29). New locators written: pp. 334, 335, 335-337, 336, 337. All seen this session.
- Algebra checked with sympy this session: gamma central moments nu_2..nu_6
  (k, 2k, 3k^2+6k, 20k^2+24k, 15k^3+130k^2+120k); E R^2 for the moment-shape influence
  R = -z^3+3z^2+3kz-k equals 6k(k+1)(k+5); gradient of G(x,y)=4x^3/y^2-1 at (a^2k, 2a^3k) is (3/a^2, -1/a^3).
- Numerics (mpmath) this session: exact shape efficiency 2/((2F-2/p+1/p^2) 6(p+1)(p+2)(p+6)) at
  p = 1..5 gives 0.02738, 0.08709, 0.15317, 0.21592, 0.27269 (Fisher's table p. 336); it crosses 0.8 at
  p = 38.106 (Fisher states 38.1 from his large-p approximation; the crossing is not written in reader text).
- Direct source correction recorded in reader text: p. 335 calls the joint solution "the set of values ...
  which has the maximum likelihood"; with p ranging over (-1, inf) the Type III likelihood is unbounded
  (m up to the least observation with p<0), so the joint solution is a local root
  (thm:p15-w02b-p15-057-typeiii-joint item 5).

## Provenance, block 3 (r3 continuation)

- Same held scan reopened. Pages read from pixels this session: printed 337, 340, 341, 342
  (physical 29, 32-34). New locators written: pp. 337, 340, 340-342, 341, 341-342. All seen this session.
- Algebra checked this session (sympy, mpmath quadrature): Type IV E phi'', E xi phi'', E xi^2 phi'' - 1,
  centre -nu/(r+4), Schur complement 2(r+1)/(r+4), Var xi, beta_2, (beta_2-1)/4, displays (3) and (4)
  and the r = 7 values 121/132, 49/132, 2695/3430, 55/214.
- Fixed-phase grouped information bounds checked numerically at a = 0.3, 0.7, 1, 1.5 over several phases
  (actual deviations 5.6e-5, 1.6e-3, 6.4e-3, 3.0e-2 for location against bounds 3.1e-3, 8.8e-2, 0.55, 10).
- Direct source correction written in reader text: p. 340 gives the centre of location of Type IV at
  -nu a/(r+4) "from the mode"; that displacement is from the point xi = 0 of the displayed form; from the
  mode it is 2 nu a/((r+2)(r+4)).
- Qualification written in reader text: at p = 1 the least observation has error of exact order n^{-1/2}
  (Rayleigh-type limit), so Fisher's faster-than-n weight at p = 1 (p. 337) is not established by it.

## Provenance, block 4 (r3 continuation)

- Same held scan reopened. Pages read from pixels this session: printed 359, 363, 364, 365, 366
  (physical 51, 55-58). New locators written: pp. 359, 363-366, 364, 365, 366. All seen this session.
- Numerics (mpmath) this session: for a = 2, W(0) over all integers = 2.373264 (printed column total
  2.373251; average pi^2/(6 log 2) = 2.373138); D(theta)^2/(V W) over 41 phases in [0, log 2] lies in
  [0.876995, 0.877112]; 6/(pi^2 log 2) = 0.877053; V(theta) = 1 identically (telescoping, proved).
  Fisher's table p. 365 recomputed: rows x = -4 (p printed 0.00000014167 vs e^{-16} = 1.1254e-7; w 0.000036
  vs 0.0000288), x = 1 (w 0.385355 vs 0.385374) and x = 4 (p 0.9394110 vs 0.9394131) disagree beyond
  printed precision; all other rows agree. Table heading prints log p = 2^{-x} without the minus sign.
- Direct source qualifications written in reader text: the 87.71 per cent and the independence of the
  dilution ratio hold for the ratio of phase averages, not for the efficiency at a fixed density; the
  infinite series has infinitely many sterile plates, so the counting method needs finite D.
- Wald-type noncompact consistency (thm:p15-w02b-p15-057-wald-noncompact) is a general theorem written in
  own words; no source locator attached.

## Provenance, block 5 (r3 continuation)

- Same held scan reopened (PyMuPDF render, 0-based page index = printed - 309). Pages read from pixels this
  session: printed 316, 317, 318, 335, 336, 337, 357, 358. New locators written: pp. 316, 316-317, 335-336,
  337, 357-358. All seen this session.
- Algebra checked this session: coefficient polynomials c_0(k) = -16k(k-1)(k-2)(k+2)/45 and
  c_1(k) = 16k(k-1)(k-2)(k-3)(8k^2+12k+13)/945 for (1+u^2/3-u^4/45[+2u^6/945]) sinh u - u cosh u
  (tabulated k = 0..11 with sympy); D, N(p) expansions; n' remainder algebra.
- Numerics (mpmath) this session: exact E(p) crosses 0.8 at p = 38.10622 (approximation crossing 38.10621);
  g(38.1) = -9.519, g(38.11) = 5.815131; 2/D - 6(p^3+p/5) in (-0.31, 0) for p in [1, 200];
  (n' - (3/2 p^2 - p + 4/5)) p in (-0.33, -0.30). Binomial n = 4, z_{0.95} = 1.6448536: intervals,
  coverages 0.6958/0.8682 at p = 5/8, 0.875/1 at p = 1/2, posterior contents 0, 0.91758, 0.98780, 0.91758, 0;
  observed-version minimum coverage on a grid 0.8526 (not written).
- Direct source corrections written in reader text: p. 357 prints the denominator of chi^2 as n_s (Pearson's
  discrepancy, for which the next display holds, has nbar_s); the display 1 + chi^2 = S(n_s^2/nbar_s) holds
  for proportions; with counts it is N + chi^2.
- Qualification written: Fisher's pp. 316-317 sufficiency-to-efficiency argument is exact for a bivariate
  normal pair; for asymptotically normal statistics the parameter-free conditional law of the limit is an
  extra premise.
- Existing treatments found and linked, not duplicated: thm:p15-fg-deviance (deterministic |2D-Q| bound and
  the two score equations, fisher-grouping-and-moments.tex); thm:p15-binomial-confidence-coverage and
  thm:p15-confidence-credibility-boundary (hypothesis-tests-and-confidence.tex).

## Provenance, block 6 (r3 continuation)

- Same held scan reopened (PyMuPDF render, 0-based page index = printed - 309). Pages read from pixels this
  session: printed 342-356 and 358 (physical 34-48, 50). New locators written: pp. 342, 342-355, 343, 344-345,
  345, 345-347, 346, 347, 347-348, 348, 348-349, 350, 351, 351-353, 353, 354-355, 355, 355-356, 356.
  All seen this session.
- Misspecification (sec:p15-w02b-p15-057-misspecified): general theorem written in own words, no source locator.
  Numbers (mpmath): 2 Phi(1.96/sqrt 2) - 1 = 0.834232; 2 Phi(1.96) - 1 = 0.950004; e^{-1} = 0.367879.
  Existing related treatment found and linked: thm:p15-convex-location-normality (huber-robust-location.tex),
  the B/a^2 limit variance for location M-estimates.
- Algebra checked with sympy this session: Type IV moment recurrence (r-k) mu'_{k+1} = k mu'_{k-1} - nu mu'_k,
  raw and central moments to order 4, beta_1 = 16 nu^2 (r-1)/((r-2)^2 (r^2+nu^2)), Pearson kappa_2 =
  nu^2/(r^2+nu^2) (p. 345 identity), factors of beta_2+3, 4 beta_2 - 3 beta_1, 2 beta_2 - 3 beta_1 - 6;
  Fisher's diagram coordinates (p. 345) solved for nu^2; 1-E_1 and 1-E_2 as rational functions of (x,y)
  with denominators equal to 1 at N and quadratic parts 8x^2+6y^2 and 12x^2+12y^2 (p. 347 contours);
  typed N_i, D_i verified against the (r,nu) forms. mpmath quadrature check of mu'_1, mu'_2 at r=9, nu=1.5.
- Direct source corrections/qualifications written: p. 349 large-n midrange law and variance a^2/(2n^2)
  replaced by exact density (n/a)(1-2|x|/a)^{n-1} and variance a^2/(2(n+1)(n+2)); p. 350 "actual mean
  square error" 6.86 is the root mean square about the average (-1.14) of the 25 printed errors; about the
  true mean it is sqrt(1208.75/25) = 6.953 (exact model value 6.967, Fisher 7.07); p. 345 kappa_2 criterion
  defined only for r > 3; p. 347 contours proved only on the Type IV side of N; p. 356 quartic curve
  integrable only for k_2 < 0 (or k_1 = k_2 = 0), and first-order agreement with the Pearson equation
  holds only on bounded x/sigma; at an end exponent 1 the zero-efficiency claim for the mean is not
  established.

## Provenance, block 7 (r3 continuation)

- Same held scan reopened (PyMuPDF render, 0-based page index = printed - 309). Pages read from pixels this
  session: printed 351, 352, 353, 354, 355. New locators written: pp. 351, 352, 352-353, 353, 354, 355.
  All seen this session.
- Algebra checked with sympy this session: Type VII/II moment-ratio variances
  EV^2/mu_2^3 = 6(r^2+r+10)/((r-3)(r-5)), EU^2 = 24r(r-1)^2(r^2-r+18)/((r-3)^3(r-5)(r-7)) and their
  r -> -r Type II forms; Fisher's n sigma^2 for nu_mu and r_mu (p. 352) reproduced exactly; Type IV c_2, c_3
  from the recurrence; Type I recurrence (r+k) mu'_{k+1} = k mu'_{k-1} - nu mu'_k and its c_2, c_3;
  G_nu = 16/3 - 16/(15 s^2) + 64 theta/(21 s^4) exactly; expansions 1 - 144/(5r^2), 1 - 160/(3r^2);
  contour intermediate forms N_1 = -2[...], N_2 = -12 Q_2, D_2 = (y^2+y-1) R~_2 checked against the
  displayed polynomials.
- Numerics (mpmath) this session: Type VII table recomputed for r = 5..18 (all entries within 3 units of
  the last printed place except r = 10 efficiency of r_mu: exact 0.42891, printed 0.4403); Type II table
  r = 2..15 within 2 units; r = 3, 4 Type II entries are formula values (0.05764, 0.20556, 0.043071, 0.14446);
  E_r = 0.8 at r = 17.17184 (beta_2 = 3.42337) Type VII and r = 14.05907 (beta_2 = 2.64828) Type II;
  E_nu = 0.8 at 12.11239 (VII), 10.98533 (II).
- Direct source corrections written in reader text: p. 351 matrix has the opposite sign on the four
  (m,a)x(nu,r) entries (congruent under diag(1,1,-1,-1)); p. 353 table r = 10 entry; p. 354 second identity
  printed with (r+1)^2 where (r-1)^2 is required.
- Sign of the Type IV information cross entries checked independently: I_{m nu} = -E[1/(1+xi^2)]/a < 0.

## Provenance, block 8 (r3 continuation)

- Same held scan reopened (PyMuPDF render, 0-based page index = printed - 309). Pages read from pixels this
  session: printed 337, 347, 348, 357, 358, 366. New locators written: p. 337, p. 347, pp. 347-348, p. 358,
  p. 366. All seen this session. Fisher p. 358: n' is one more than the number of degrees of freedom in which
  the sample may differ from expectation; p. 337: the faster-than-n claim at p = 1 is stated whether or not
  p and a are known; p. 347: at the upper boundary the ratio of probable errors of the moments to the optimum
  tends to infinity, attributed to the curve meeting the axis at a finite angle.
- New general results written in own words (no source locator): linear-end (capped-reciprocal M-estimate and
  diagonal construction, via thm:p15-convex-location-normality), periodization lemma (Poisson summation with a
  Fejer-kernel uniqueness step and a contour-shift strip bound), grouped-exp, lindeberg-vector (Lindeberg
  replacement), chisq-law, dilution-oscillation.
- Numerics (mpmath) this session: grouped fixed-phase periodic parts over 20 phases: location 6.4e-17 (a=0.5),
  9.9e-10 (a=1), 7.8e-5 (a=1.5), 4.3e-3 (a=2); bounds with tau = pi/4: 1.6e-7, 0.080, 0.86, 2.24. Scale parts
  8.4e-17, 1.2e-7, 3.5e-3, 9.3e-2 against 1.5e-6, 0.57, 5.6, 14.1. Linear-end example (f = y e^{-y}):
  J(0.01) = 4.037930, kappa = 0.995017, v = 0.217392; J(1e-6) = 13.238296, v = 0.0726854. Dilution: exact-term
  and closed-form deltas; efficiency over 40 phases a=2 [0.876995, 0.877112], a=3 [0.87242, 0.88172],
  a=4 [0.85945, 0.89516], a=10 [0.77833, 0.96754] (a=10 range is written in reader text only as an
  illustration). Closed-form bounds (b = e/sin 1): a=2 delta_D <= 3.8353e-5, delta_W <= 8.0875e-4,
  interval [0.876553, 0.877554]; a=3 deltas 4.6362e-3, 6.1697e-2, 1.6211e-3, interval [0.83522, 0.92225].
- Euler's reflection formula is not proved in the handbook, so the dilution bound uses the self-contained
  strip bound |Gamma(1-i w)| <= (e/sin 1)|w| e^{-pi|w|/2} (about 4 times the exact modulus at a=2).

## Continuation

State after block 8 (written, not reviewed):

Written in block 8 (C03 gaps of the r3 assessment):
- (a) thm chisq-law + lemma lindeberg-vector: limit law chi^2_{K-1-q} for Q and 2D under fitting first-order
  equivalent to the count MLE; grouped normal MLE shown to qualify (q=2); fixed cells r=K-1.
- (b) thm linear-end items 1-2: at p=1 with a known, an equivariant estimate with sqrt(n)(T_n-m) -> 0.
- (d) thm linear-end item 3-4: mean has relative efficiency -> 0 at an end exponent 1 (Type III p=1, Type I
  m_1=1 or m_2=1, known form).
- (g) lemma periodization + thm grouped-exp: fixed-phase periodic part O(poly(1/a) e^{-11 pi^2/(18 a^2)});
  fg-expansion (eighth order, inverses) holds at every fixed phase. Host proofboundary updated.
- (h) thm dilution-oscillation: exact Fourier series of LD, LW, LV; uniform oscillation bounds for every a;
  closed forms for a <= e^{2 pi}; efficiency at every density in [0.8765, 0.8776] at a=2, [0.835, 0.923] at a=3.

Still owed (in this order):
1. (f) Type II condition (C) (moving range) so the Type II inverse-information values are limit variances of
   a likelihood root; plan as in typeiii-joint.
2. (e) monotonicity of E_r on each side (Type VII and Type II) behind the 2.65-3.42 beta_2 band, and written
   evaluations/bounds of the 0.8 crossings r = 17.172, 14.059 and E_nu crossings 12.112, 10.985.
3. (c) Types I/II side of the p. 347 contours (y > 0): Type I efficiencies of mean and second moment as
   rational functions, identification with the nu^2 < 0 continuation, with regularity scope (m1, m2 > 1).
4. (b) residual: Fisher's p. 337 claim with a (and p) unknown; exact order (n log n)^{-1/2} not proved.
