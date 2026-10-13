# w02ca-p15-021 research note (P15 chapter 162; sections 162.5, 162.7, 162.8, 162.9)

Label tag: `p15-w02c-p15-021`.

## Sources opened in this session

- Durrett, *Probability: Theory and Examples*, Version 5 (2019-01-11), held file
  `citations/Durrett - Probability - Theory and Examples (2019-01-11, Version 5).pdf`.
  - Theorem 4.5.2, printed p. 240 (PDF p. 248): convergence on {A_infty < infty}; proof with
    N = inf{n : A_{n+1} > a^2} and the bound A_{N and n} <= a^2. Cited as
    `\cite[thm.~4.5.2, p.~240]{DurrettPTEAuthor2019}` in the new body file.
  - Theorem 4.3.8, printed pp. 229-230 (PDF pp. 237-238): Kakutani product criterion
    (read to confirm the host's existing citation; no new locator written in the host annex).

## Work done

- C010 (predictable quadratic variation, worked boundary for body l.182-183): new body and annex
  files. The first-exceedance time S_c = inf{n: A_n > c} equals T_c + 1; the bound
  A_{S_c and n} <= c for every n holds at a sample point iff S_c = infty iff A_infty <= c, so it holds
  almost surely only when the stop is idle. With a deterministic bound K on the variance increments
  the stopped variation is at most c + K. Single-jump martingale (P(J=k)=2^{-k}, jump of variance
  2^J at time J) gives X_{S_c and n} = X_n with E X_n^2 = n for every c, infinite expected overshoot,
  while the T_c stop keeps E X^2 <= c. The characterization and example are the handbook's own
  arguments; the source does not state them (said so in the reader text).
- C012 (Gaussian product 'singular otherwise'): host annex annex:p15.product-gaussian-comparison now
  writes coordinate equivalence, the two-sided equivalence in the summable case (reverse-measure
  part), the step sum(1-h_m)=infty => H_infty=0 => mu perp nu, exclusivity, both directions of the
  sigma=tau criterion, and a concrete divergent example backing the support remark.
- C013 (Bernoulli boundaries): host annex annex:p15.product-bernoulli-boundaries now writes the
  equivalence of the coordinate laws, nu<<mu via the reversed affinity, the singular case through
  H_infty=0, and both numerical examples.
- Patch request work/waves/w02ca/patches/w02ca-p15-021.json: links the host sentence at
  predictable-quadratic-variation.tex l.182-183 to the new results (read-only host).

## Existing treatment found

Searched the handbook for first-exceedance/overshoot treatments of the variance process and for a
written H_infty=0 singular step in the normal and Bernoulli cases; none found beyond the packet's
listed files. The one-step-early stop is reused at annex:p15.square-root-variation-bound.

## Continuation

All three gaps named for this round are written. Lead actions: input the new body and annex files
at the placement in the return file, then apply the patch request. Section 162.9 belongs to the
readonly unit owned by w02c-p15-003.
