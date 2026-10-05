# w02b-p15-056: Bayes-factor computation extensions (168.5-168.8)

4 October 2026. Packet work/waves/w02b/packets/w02b-p15-056.json, block 1.
Placement: in-place extension of the two editable hosts
handbook/parts/p15/bayes-factor-computation.tex and
handbook/annex/p15/bayes-factor-computation.tex. The owned new chapter files
(parts/annex ...-w02b-p15-056.tex) were not created; no driver insertion is
needed. Unit compile was run with temporary wrapper files at the owned paths
that input the two hosts; the wrappers were removed afterwards.

## Source read in this session

source/references/kass-raftery-bayes-factors-1995/kass-raftery-1995.pdf
(held; key KassRaftery1995BayesFactors). Read journal pp. 777-781 (PDF
pages 6-10) as text, and as page images for pp. 777 (eq. 4), 778
(eqs. 5-9, Sec. 4.1.2-4.1.3), 779 (Sec. 4.1.3 unit-information prior,
eqs. 10-11, Sec. 4.2 adaptive quadrature), 780 (pr3, pr4, eq. 12,
Laplace-Metropolis, Savage-Dickey display, latent-data ratio). Also read
p. 782 Sec. 5.2 (null orthogonality defined as block-diagonal Fisher
information at psi=psi0; local alternatives psi-psi0=O(n^-1/2)) and p. 781
Sec. 5.1 (Borel-paradox remark on pi(beta|H0)=pi(beta|psi=psi0,H1)).

Locators written: Sec. 4.1.2 p. 778 (expected information O(n^-1/2);
eqs. (7)-(8); "often improves"), Sec. 4.1.3 p. 779 (unit-information prior,
O(n^-1/2)), Sec. 5.2 p. 782, Sec. 4.3 p. 780 (estimators, Savage-Dickey,
latent data, Meng-Wong mention, Laplace-Metropolis alternatives),
Sec. 5.1 p. 781, Sec. 4.2 p. 779 (adaptive quadrature, dimension < 9).

## What was written (labels)

- C004: thm:p15-w02b-p15-056-information-replacement-boundary /
  annex:p15-w02b-p15-056-infobound. Logistic location model, normal(0,1)
  prior, symmetric two-point data +-a_n with 2f(a_n)=1/3+n^-1/2:
  delta_n=n^-1/2 exactly, MLE-Laplace hypotheses verified, expected-info
  log error 1/2 log(1+3n^-1/2)+O(n^-1) (exact order n^-1/2, limit 3/2 after
  sqrt n scaling). Boundary: a=log(11+sqrt 120), J=1/12, ||Jtilde-J||=1/4,
  no c with delta<c/2; expected-info approximation ratio -> 1/2.
  Numerically checked (n=400..6400) in scratch.
- MP-0 one-step Newton: def:p15-w02b-p15-056-one-step-newton (method,
  eqs. (7)-(8) in source notation), thm:p15-w02b-p15-056-one-step-newton /
  annex:p15-w02b-p15-056-newton: expansion identity (quadratic ell, linear
  lambda, curvature F+G at the Newton point), O(n^-1) error under MLE-Laplace
  hypotheses with bounded prior precision, normal calculation (one-step error
  D^2 s^4/(2 tau^2(s^2+tau^2)^2) vs (5) exact order n^-1).
- C005: thm:p15-w02b-p15-056-unit-information-schwarz /
  annex:p15-w02b-p15-056-unitinfo: deterministic hypotheses (independence +
  normal(psi0,W) prior; local alternative at data scale; null orthogonality
  as off-diagonal block O(n^-1/2) and log det D_n + log det W = O(n^-1/2)),
  argument from c_{k,n} using Schur complement and the determinant comparison
  of the curvature-replacement annex; normal-mean instance with exact
  difference -1/2 log(1+1/n) - z^2/(2(n+1)), and fixed-alternative failure.
- MP-0 mixture: def/thm:p15-w02b-p15-056-mixture-estimators /
  annex:p15-w02b-p15-056-mixture. pr3 and pr4 are constructed from the
  verbal description on p. 780 (the source prints no formula). Finding:
  under that construction the imagined prior draws cancel from the pr4
  estimating equation; pr4 converges to the root of E_P psi_p = 0, which is
  I only under the displayed integral condition; two-point example gives
  (1+sqrt13)/2 vs I=2. pr3 is consistent with a normal limit (bounded
  estimating function). Checked numerically.
- MP-0 bridge identity: thm:p15-w02b-p15-056-bridge-identity /
  annex:p15-w02b-p15-056-bridge (general identity, strong-law ratio,
  importance and generalized-harmonic special cases with support conditions).
  Meng and Wong (1993) is not held; no claim from it beyond the source's
  one-sentence mention.
- MP-0 Laplace-Metropolis: thm:p15-w02b-p15-056-laplace-metropolis /
  annex:p15-w02b-p15-056-lapmet (two-sided mode-error bound, covariance
  error bound, inheritance iff errors O(n^-1); normal instance with error
  1/2 min Z_i^2 free of n).
- MP-0 Savage-Dickey: thm:p15-w02b-p15-056-savage-dickey /
  annex:p15-w02b-p15-056-sdratio (source display B10=pi(psi0|H1)/pr(psi0|D,H1)
  under the conditional-prior condition, general correction factor, version
  dependence, normal check, failure example factor sqrt(5/2)).
- MP-0 latent-data ratio: thm:p15-w02b-p15-056-latent-ratio /
  annex:p15-w02b-p15-056-latent (identity with support condition, i.i.d.
  convergence and variance criterion, harmonic-mean special case as one
  precise reading of the p. 780 remark).
- Host closing paragraph (formerly disclaiming these developments) replaced
  by a limitation paragraph naming what remains: adaptive Gaussian quadrature
  error bounds, the optimal bridge function, dependent-chain averaging.

## Open items (not written)

- Adaptive Gaussian quadrature (Genz and Kass 1993): the held Kass-Raftery
  gives only a verbal description (p. 779); the Genz-Kass paper is not held.
- General dependent-chain (Gibbs/Metropolis/weighted likelihood bootstrap)
  averaging: no held source with an ergodic theorem for this chapter.
- Optimal bridge function (Meng and Wong 1993): not held.

## Block 2 (4 October 2026): dependent simulation output

Gap closed in this block: an averaging theorem for dependent simulation
output covering the direct, importance, harmonic, mixture, bridge and
latent-ratio averages, with the normal limits claimed by the independent
theorems.

Source read in this session: citations/Durrett - Probability - Theory and
Examples (2019-01-11, Version 5).pdf (key DurrettPTEAuthor2019, already in
handbook.bib; held per held-sources.json entry 43). Text extracted with
pdftotext. Read: Sec. 5.2 construction of the canonical chain, P_mu as the
mixture of P_x and the shift (p. 273); Theorem 5.2.1 (p. 274);
Theorem 5.2.3 Markov property (p. 275); Sec. 5.8 opening (Harris chains,
pp. 322-324, read only for orientation, not cited); Sec. 6.2 Theorem 6.2.1
and Lemma 6.2.2 (p. 335) and the proof of Theorem 6.2.1 (pp. 335-336).
Locators written: Sec. 5.2 p. 273; Theorem 5.2.1 p. 274; Theorem 5.2.3
p. 275; Lemma 6.2.2 p. 335; Theorem 6.2.1 pp. 335-336; Sec. 6.2
pp. 335-336. No new Kass-Raftery locator was written; the one added
citation uses the section range Secs. 4.2-4.3 already used in the host for
equations (10) and (12).

Hypotheses chosen (stated in def:p15-w02b-p15-056-chain-hypotheses):
(E) shift-ergodic stationary path law, initial law absolutely continuous
with respect to the invariant law; (D) one-step minorization
K(x,.) >= eps zeta(.) for every x, arbitrary initial law. The martingale
central limit lemma is proved by the truncated characteristic-product
argument written out in the annex; no source attribution is made for it
because no held source presenting that argument was read.

Written (labels):
- sec:p15-w02b-p15-056-dependent-averages (body), with
  def:p15-w02b-p15-056-chain-hypotheses,
  thm:p15-w02b-p15-056-doeblin / annex:p15-w02b-p15-056-doeblin,
  thm:p15-w02b-p15-056-ergodic-averages / annex:p15-w02b-p15-056-ergodic
  (maximal inequality, ergodic theorem in the ergodic case, transfer to
  mu << gamma, every start under (D)),
  thm:p15-w02b-p15-056-martingale-clt / annex:p15-w02b-p15-056-mgclt,
  thm:p15-w02b-p15-056-chain-clt / annex:p15-w02b-p15-056-chainclt
  (Poisson equation in L2, variance series, bounded-density start, then
  arbitrary start via mu K^k = (1-eps)^k rho_k + lambda_k),
  thm:p15-w02b-p15-056-dependent-estimators / annex:p15-w02b-p15-056-depest
  (all six estimator families; normal limits for ordinary, self-normalized,
  harmonic, pr3 and latent averages),
  thm:p15-w02b-p15-056-two-state-chain / annex:p15-w02b-p15-056-twostate
  (worked example: sigma^2_K(H) = 2/3 versus Var 4/3; inverse-harmonic
  limit variance 1/24 versus 1/12; E_1 A_M formula; independence Metropolis
  satisfies (D) with eps = 1/w*; identity kernel fails (D) and (E)),
  def:p15-w02b-p15-056-dependence-limits (warning).
- Host edits: the paragraph after thm:p15-mc-evidence-boundaries now points
  to the new section; the latent-ratio remark points to the estimator
  theorem; the limitation paragraph now lists two open developments
  (adaptive quadrature error bounds, optimal bridge function) and states
  that no limit is proved for weighted-likelihood-bootstrap output.
- Numerical checks (scratch only): two-state invariance, sigma^2 = 2/3 by
  covariance series, E_1 A_M for M = 1, 2, 3, 7, and a 4000-run simulation
  of sqrt M (A_M^{-1} - 1/2) at M = 4000 giving variance 0.0417 against
  1/24 = 0.04167.

Not established (unchanged from block 1): adaptive Gaussian quadrature error
bounds (Genz and Kass 1993 not held); optimal bridge function (Meng and Wong
1993 not held). Normal limits under (E) without (D), and for the bridge
ratio and pr4, are not asserted; the independent theorems assert none for
the latter two.

## Block 3 (4 October 2026): adaptive quadrature and the optimal bridge function

Gaps closed in this block (from the independent assessment): adaptive
Gaussian quadrature for a peaked marginal-likelihood integral, and the
optimal bridge function with its iteration. Both were reported
blocked_source in blocks 1-2 because Genz and Kass (1993) and Meng and Wong
(1993) are not held (rechecked in held-sources.json this block: neither is
listed). This block writes both as general mathematics, stated and proved
in full in the annex, and attributes to a source only what the held
Kass-Raftery file says.

Source read in this session: source/references/kass-raftery-bayes-factors-1995/kass-raftery-1995.txt
(text of the held PDF), journal pp. 779-781. Locators written in this
block: Sec. 4.2, p. 779 (verbal description of adaptive Gaussian quadrature
for integrals peaked around a dominant mode; effective when the dimension
is modest, roughly less than 9); Sec. 4.3, p. 780 (Meng and Wong considered
an optimal choice of f, computed iteratively from an initial guess; their
framework applies to ratios of integrals). Both were already used in the
host; no new locator. No sentence attributes a specific algorithm, theorem
or notation to Genz-Kass or Meng-Wong; the reader text says the
constructions are this chapter's precise forms, not transcriptions.
General results cited by label: thm:p15-criteria-moment-identities
(Gaussian moments), thm:p15-clt-iid, thm:p15-clt-perturbation,
thm:p15-criteria-limit-operations (independent sums), the strong law.

Written (labels):
- sec:p15-w02b-p15-056-adaptive-quadrature (body, before
  sec:p15-bic-consequence): def:p15-w02b-p15-056-gauss-hermite (Hermite
  polynomials, Gauss-Hermite and product rules, adaptive rule Q_{n,K}
  centred at theta_n and scaled by J_n^{-1/2});
  thm:p15-w02b-p15-056-gauss-hermite-exactness / annex ghexact (distinct
  real zeros, positive weights, exactness to degree 2K-1 and failure at
  He_K^2, reflection symmetry, product rule and odd polynomials, explicit
  K = 1, 2, 3 rules); thm:p15-w02b-p15-056-adaptive-quadrature / annex agq
  (Q_{n,1} is the Laplace value; I_n/Q_{n,K} = 1 + O(1/n) under
  def:p15-laplace-family; under C^6/C^4 bounds,
  I_n/Q_{n,K} = 1 + Delta_{n,K}/n + O(n^-2) with explicit P_{n,2}, and
  Delta = 0 for K >= 4); thm:p15-w02b-p15-056-adaptive-quadrature-example /
  annex agqex (gamma integral: Delta = 1/12, 5/18, 1/3, 0; second mode with
  failed tail condition: ratio 2 Phi(1.5 sqrt n) -> 2 for every K).
- After thm:p15-w02b-p15-056-bridge-identity (replacing the paragraph that
  said the optimal choice was not derived):
  def:p15-w02b-p15-056-bridge-estimator; thm:p15-w02b-p15-056-optimal-bridge
  / annex optbridge (normal limit with criterion V(alpha); H in (0,1];
  V(alpha) >= (1/H - 1)/(s1 s2) with equality iff alpha is a nonzero
  multiple of alpha_r on S; for a fixed sample with overlap the iteration
  map has a unique fixed point, the root of a strictly increasing
  estimating function, and the iteration converges from every start with a
  geometric bound on the log scale; the fixed point is consistent and has
  the optimal limit variance); thm:p15-w02b-p15-056-bridge-example / annex
  bridgeex (two exponential kernels: optimal 4/(2 - log 3) - 4 = 0.4376,
  geometric 1/2, 1/q_1 bridge 2/3, 1/q_2 bridge infinite variance).
- Host edits: chapter introduction lists adaptive quadrature and the
  optimal bridge; the limitation paragraph before the dependent-averages
  section now points to the new results.
- Numerical checks (scratch only): adaptive Gauss-Hermite on the gamma
  integral for n = 100, 1000, 10000 and K = 1..5 gave n(I/Q - 1) = 0.08333,
  0.2778, 0.3333 and n^2-scale errors for K = 4, 5; a 4000-replicate
  simulation of the iterated optimal bridge (M = 2000) gave
  M Var(r_hat/r) = 0.4381 against 0.4376, geometric 0.5035 against 0.5;
  the iteration converged in at most 9 steps from r0 = 0.01.

Not asserted: convergence as K -> infinity at fixed n; error bounds with
computed (approximate) mode and curvature; optimality for Markov chain
output; the s1 -> 0 or s2 -> 0 endpoint cases.

## Continuation

Status after block 3: all edits saved. Official unit compile ok (run with
temporary wrapper files at the owned paths inputting the two hosts, removed
afterwards; 18 overfull, none above 2pt in block-3 material).
find_fused_spaces: no hits. check.py --tree: no finding in the edited
files. Body host: adaptive-quadrature section 267-426, optimal-bridge
material 827-942, limitation paragraph 1076-1081. Annex host: ghexact
492-584, agq 585-755, agqex 756-820, optbridge 1002-1212, bridgeex
1213-1254. Both assessed gaps were written in this block; whether they
meet the duty is for the next assessment. Extensions not asserted are
listed under "Not asserted" above. Block-1 "Open items" for adaptive
quadrature and the optimal bridge are superseded by block 3.
