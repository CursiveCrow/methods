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
  sqrt n scaling). Boundary: a=log(11+sqrt120), J=1/12, ||Jtilde-J||=1/4,
  no c with delta<c/2; expected-info approximation ratio -> 1/2.
  Numerically checked (n=400..6400) in scratch.
- MP-0 one-step Newton: def:p15-w02b-p15-056-one-step-newton (method,
  eqs. (7)-(8) in source notation), thm:p15-w02b-p15-056-one-step-newton /
  annex:p15-w02b-p15-056-newton: expansion identity (quadratic ell, linear
  lambda, curvature F+G at the Newton point), O(n^-1) error under MLE-Laplace
  hypotheses with bounded prior precision, normal calculation (one-step error
  D^2 s^4/(2tau^2(s^2+tau^2)^2) vs (5) exact order n^-1).
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

## Continuation

Status at return: all edits saved; unit compile ok (14 overfull, of which
new: annex lines 429, 492-500, 561, each under 10pt, caused by long
annex-label headings and one inline formula). find_fused_spaces: no hits.
check.py --tree: no finding in the edited files.
Next block, if any: acquire Genz and Kass (1993) for adaptive quadrature
error bounds and a held ergodic-theorem source for dependent-chain averages;
optionally Meng and Wong (1993) for the optimal bridge choice.
