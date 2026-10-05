# w02b-p15-071 research note (P15, sections 172.3, 172.4)

Source held and opened this session: source/references/huber-robust-location-1964/huber-1964.pdf
(Huber 1964, Ann. Math. Statist. 35(1), pp. 73-101; physical page = printed page - 72).
Pages read visually this session: pp. 82, 83, 96, 97, 100, 101.
Locators used in the new text: Sec. 7 pp. 82-83 (bias identity, bound (2), o(c) remark,
0.17/0.021/0.0027, n = 9/600/35000); Sec. 11 p. 96 (minimax and Winsorizing claims),
pp. 96-97 (proposal comparisons, preference, Proposal 3 conjecture); Sec. 12 pp. 100-101
(V(psi_2,F) < (1-eps)^{-4} pi/3 for symmetric H, approached as H spreads to infinity).

## Scope decisions
- ED26-P15-CH-huber-information-game (172.3, incl. C009, C010) is a readonly unit owned by
  w02b-p15-045; not written here (A14).
- Body results placed in the owned chapter file; short \cref sentences added to the editable
  host handbook/parts/p15/huber-remaining-methods.tex at the bias paragraph, the end of
  def:p15-huber-three-proposals, and inside thm:p15-huber-pair-median.
- Proofs in the owned annex file (the host annex is not editable).

## Provenance of added results
- thm:p15-w02b-p15-071-bias-identity (ii) follows the source's mean-value identity and
  bound (2); (iii) is an added variant avoiding lambda_H'; (iv) formalizes "replace
  vartheta c by 0".
- thm:p15-w02b-p15-071-bias-variance supplies explicit regularity for the o(c) remark;
  for psi_k, G=Phi it compares with V*(k,eps) of thm:p15-huber-normal-variance.
- Numbers (scipy, scratch script w071/num.py): first-order biases 0.169860, 0.0207594,
  0.00266473; exact c_* 0.170383, 0.0207597, 0.00266474; k_eps 1.140171, 1.945111,
  2.632880; matched Proposal 2 k and r_eps as tabulated; crossing of eps = 1 - r_eps
  near 0.269886 (brentq; uniqueness of the crossing not proved, so only "a computed
  crossing" is claimed); 1 - r_0.5 = 0.113881.
- thm:p15-w02b-p15-071-pair-median-risk: risk-form bound for every symmetric H; atom case
  pins T_n at zero; no limit law claimed for singular / non-L2 contaminants.

## Round 3 additions (remaining-methods C015)
- Source pages re-read visually this session: pp. 95, 96, 97 (physical pages 23-25). The source
  counts observations in the closed interval [T - kS, T + kS] (p. 96); the convention
  def:p15-w02b-p15-071-prop1-convention reads this as kS = D_(m_n)(T), m_n any integer with
  |m_n - nA(k)| <= 1.
- New results: def:...-prop1-convention, thm:...-empirical-tools (layer-cake uniform bound,
  concentration function, sign/Kolmogorov bound for the cutoff change, local oscillation of the
  empirical df at a differentiability point, quotient limit), thm:...-prop1-consistency,
  thm:...-prop1-limit, thm:...-prop1-minimax, def:...-prop1-numbers, thm:...-scale-compare.
- Finding: under this convention Proposal 1 with matched k is NOT asymptotically minimax over the
  whole symmetric class: a symmetric contaminant with atoms at +-q, (1-eps)A(q) < A(k) <
  (1-eps)A(q) + eps h, makes the window exclude both atoms and gives risk V*(q,eps) > 1/I_*.
  It is minimax over regular laws (no atoms at +-q_0). Checked by simulation (scratch w071/sim*.py):
  eps=0.3, q=0.4275: simulated n E T^2 = 2.836 +- 0.069 vs predicted 2.872 (regular formula 1.227);
  configuration (iv) eps=0.3, q=0.25: 0.306 +- 0.010 at n=16000 vs predicted 0.2995.
- Finding: Huber's "log S of Proposal 2 has the smaller asymptotic variance" fails at Phi for k=1
  (v1=0.92496 < v2=1.03350) and holds for k=2 (0.93117 > 0.56486); computed single crossing near
  k=1.2974 on a grid 0.01..6 (uniqueness not proved). Proposal 1 log-scale variance at Phi, k=1,
  simulated 0.951 vs 0.925 (n=4000, 3000 reps).
- Numbers: scratch w071/nums2.py (matched Proposal 1 k, q_*, V*(q_*,eps), crossing eps=A(k) near
  0.32545, interval checks at k=1,2).

## Continuation
- remaining-methods C005: written (round 2).
- remaining-methods C021: written (round 2).
- remaining-methods C015: partial. Written this round: Proposal 1 sampling theory under the
  closed-window convention (existence, consistency of every solution, limiting risk V_1(F) for
  regular laws, Gaussian limits in the two interior edge-atom configurations, universal bound,
  log-scale limit at differentiable F), its minimax standing (minimax over regular laws; a
  counterexample family over the full class), and the log-scale variance comparison at the normal
  law (fails at k=1, holds at k=2). Still missing: (a) the limit law of Proposal 1 when p_0>0 and
  A(k) equals alpha_0, alpha_0+p_0 or alpha_0+2p_0 (only the bound of thm prop1-limit (i));
  (b) the exact supremum R_eps(T^(1)) over the class (only lower and upper bounds);
  (c) a proof that k ~ 1.2974 is the unique crossing at Phi and any comparison of the log-scale
  variances under contaminated laws other than Phi; (d) Proposal 2 minimaxity over the whole
  symmetric class when eps >= 1 - r_eps; (e) a limit theorem comparing Proposal 1 with a
  fixed-count Winsorized mean; (f) small-sample comparisons and the Proposal 3 conjecture.
- ED26-P15-CH-huber-information-game (C001, C009, C010, C013 assessed partial): readonly unit owned
  by w02b-p15-045 and host handbook/parts/p15/huber-information-game.tex is read-only for this
  packet, so not written here (A14/A8).
- Self-checks run this round: find_fused_spaces (no hits), unit-compile ok, check.py shows no
  finding for the owned files or the hosts.
