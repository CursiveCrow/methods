# w02b-p15-063: section 170.10, simultaneous concentration bands and confidence sequences

Packet: work/waves/w02b/packets/w02b-p15-063.json. Label tag p15-w02b-p15-063.
Heading level \chapter; toc tag `%% toc: P15 170 170.10`.

## Files

- handbook/parts/p15/sequential-evidence-and-multiple-testing-w02b-p15-063.tex (611 lines)
- handbook/annex/p15/sequential-evidence-and-multiple-testing-w02b-p15-063.tex (566 lines)
- handbook/registry/symbols-intake-p15-sequential-evidence-and-multiple-testing-w02b-p15-063.csv
- work/waves/w02b/patches/w02b-p15-063.json (three cross-reference patch requests to the read-only host handbook/parts/p15/bounded-concentration-learning.tex)
- No bib intake written: the only key cited is Hoeffding1963BoundedSums, already in handbook.bib.

Placement: body after `\input{parts/p15/multiple-testing}` in handbook/parts/p15.tex (line 77);
annex after `\input{annex/p15/multiple-testing}` in handbook/annex/p15.tex (line 76). The lead
inserts these; no driver was edited.

## Sources read in this session

Hoeffding, Probability Inequalities for Sums of Bounded Random Variables, JASA 58 (1963)
13-30, held at source/references/hoeffding-bounded-sums-1963/hoeffding-1963.pdf
(printed page = physical page + 11; physical 2-6 = printed 13-17). Read as images:
printed pp. 13 (eqs. 1.1-1.6), 14 (eqs. 1.7-1.9, optimality sentence, n. 3), 15 (Theorem 1,
eqs. 2.1-2.5, the sentence that (2.1) is the minimum over h of (1.7) under (2.5), n. 4),
16 (Theorem 2, corollary, Theorem 3), 17 (eqs. 2.12-2.17 and the comparisons with 2.16).
Every locator written (pp. 13, 14, n. 3, 15, 17; equation numbers 1.2, 1.5-1.8, 2.1, 2.2,
2.5, 2.6, 2.8, 2.16) was seen there.

No held source presents confidence sequences (held-sources.json has no Darling-Robbins,
Ville, Lai or later work). The chapter therefore attributes no definition, name or result
to an outside presentation of confidence sequences; everything outside the Hoeffding
statements is derived from on-route results (thm:p15-conc-time-uniform,
thm:p15-conc-martingale, thm:p15-doob-weak-maximal, thm:p15-clt-oscillation,
thm:p15-iid-series-strong-law, the Holm chapter and the Wald chapter). A source-specific
historical presentation of confidence sequences, if wanted, would need a held copy of
Darling and Robbins, Confidence sequences for mean, variance, and median, PNAS 58 (1967).

## Map

| Label suffix (thm:/annex:p15-w02b-p15-063-) | Content |
| --- | --- |
| exponential-optimality | C004 dispute: (2.1) is the minimum over h of (1.7) under the Bernoulli law; smallest bound obtainable uniformly; not the least upper bound (n=1 case p/(p+t) < e^{-D}). |
| chebyshev-comparison | C008(i): sigma^2 <= p(1-p) with equality case; exact crossing x_* of e^{-2nt^2} and the one-sided Chebyshev bound, x_* < 1/(2 sigma^2) - 1; small-t reversal for A_1; exponential vs 1/n decay; part 5 (added block 2): two-sided 2A_3 vs K_5 (1.5), set where 2A_3 >= K_5 is [x_-,x_+], 0<x_-<ln2/2<1/2<x_+<ln(2/sigma^2), both bounds exceed one below x_-. |
| normal-benchmark | C008(ii),(iii): Gaussian optimization (2.16); A_2 >= normal value with equality iff binomial; Theorem 2 bound >= normal value with equality iff symmetric two-point; e^{-y^2/2}/Phi(-y) >= sqrt(2 pi) y and never attained, contrasted with attainment of (2.1), (2.8); part 5: B_1, Bennett and Bernstein bounds within factors exp(-nt^3/(2b sigma^2)) and exp(nbt^3/(6 sigma^4)) of the normal value (p. 17 remark on (2.13) and Theorem 3). |
| cs-equivalence | Confidence sequence definition consequence: simultaneous coverage = inf of coverage over a.s. finite random times = over stopping times = over bounded stopping times; running intersections. |
| union-band-cs | thm:p15-conc-time-uniform band is a confidence sequence (general deterministic ranges, [0,1] clipped case, drifting deterministic means cover the running average). |
| reuse-failure | Fixed-sample interval reused: fixed-n coverage, a.s. infinitely many exclusions (via thm:p15-clt-oscillation), degenerate case, finite-horizon Bonferroni, exact Bernoulli recursion. |
| allocation | Time-indexed obtained levels; union band = countable weighted Bonferroni, reuse = unadjusted, finite horizon = equal-weight Bonferroni; Holm and weighted Holm reject some member iff Bonferroni does, so identical confidence sets; width comparison of the finite horizon. |
| sprt-comparison | Wald upper boundary via Doob: P_{p0}(ever cross) <= 1/A; mean-scale boundary c_* + a/(m Delta), p0 < c_* < p1; power < 1 (A^{-h}) for p0 < p < c_*, union band rejects a.s.; crossing a.s. for p > c_*. |
| epoch-band | Doubling-epoch band from the finite-horizon maximal inequality, telescoping allocation delta/((k+1)(k+2)), V_n = 0 replacement. |
| width-comparison | n=1 equality and trivial-interval threshold delta <= 4e^{-2}; n=2 ratio sqrt(3/2); epoch starts/ends; k_0(delta) condition with induction; k_0(0.05)=10, k_0=7 on [10368/16512,1); limits as delta -> 1; V_n = 0 and unbounded width ratio. |

Examples (no status): def:...-chebyshev-example, -reuse-example, -width-table; warning
-limitations; method -method.

## Numerical values (computed in this session)

Computed with Python floats from the closed forms; the reuse probabilities from the exact
recursion with exact rational masses (comparisons checked with margin >= 3e-7):
fair coin, delta=0.05: reuse exclusion by N=100 = 0.0530066, by N=1000 = 0.1031522; union
band 1.027e-5 and 1.157e-5. Width table at delta=0.05 and the last n with e_n >= r_n (528,
scanned to n < 2^22). x_*(1/4) = 0.62822. SPRT p0=1/2, p1=3/4, A=20: c_* = ln2/ln3 =
0.63093, root h(0.55) = 0.62004, 20^{-h} = 0.15607.

## Decisions

- \mathcal I^{\rm fix}_n names the reused interval to avoid a clash with the filtration
  \mathcal F_n.
- The confidence-sequence parameter must be the same for every n; drifting conditional
  means are handled by covering the running average, stated explicitly.
- Holm comparison is stated pointwise (some-rejection equivalence), so it needs no
  distributional assumption; Holm's guarantee itself needs (V), proved in part 1.
- Overfull boxes: 14 in the unit build, the largest from theorem headers with long labels;
  no content consequence.

## Continuation

Written in this block: all ten body results with annex proofs, three examples, warning,
method, symbol intake, patch request. Self-checks run: find_fused_spaces (no hits),
unit-compile ok, check.py --tree handbook shows no finding in these files.

Open items for a later block or the lead:
- Apply work/waves/w02b/patches/w02b-p15-063.json and insert the two driver lines.
- Optional: a held copy of Darling and Robbins (1967) would allow an attributed historical
  presentation of confidence sequences; nothing in the present chapter depends on it.
- The p. 17 remark that Bernstein's (2.13) and the Theorem 3 bounds are close to (2.16)
  for small lambda is written as part 5 of thm:p15-w02b-p15-063-normal-benchmark.

Block 2 (continuation of the C004/C008 assessment disputes). The disputes were raised
against the read-only host handbook/parts/p15/bounded-concentration-learning.tex, which this
packet cannot edit; the material they name is in this chapter
(thm:p15-w02b-p15-063-exponential-optimality for C004; -chebyshev-comparison and
-normal-benchmark for C008) and the host links to it once the lead applies
work/waves/w02b/patches/w02b-p15-063.json and the two driver insertions. Re-read printed
pp. 14-17 of the held PDF this block; every locator re-checked. Added part 5 of
-chebyshev-comparison (the two-sided comparison with (1.5), which part 2 had covered only via
K_6 <= K_5) with annex proof, and the n = 108 two-sided numbers to -chebyshev-example
(fair coin, t = 0.1: x_- = 0.17870, x_+ = 1.07665; 2A_3 < K_5 for n <= 17 and n >= 108).
Checks: find_fused_spaces no hits; unit-compile ok (14 overfull); check.py no finding in
these files.

Block 3 (assessment disputes C005, C008; guard G1).
- G1: the four flagged files (spec/research/edition-2026-p01-symbol-registry-w02b-p01-014*.{md,json},
  edition-2026-p02-fol-metatheorem-table-and-nd-cpl-sheet-w02b-p02-036*.{md,json}) belong to packets
  w02b-p01-014 and w02b-p02-036. This packet did not write them in any block and may not modify or
  revert them (no write git commands, other agents' files); the change originates outside this packet.
- C005: re-read printed pp. 17-20 of the held PDF (physical 6-9) as images this block. Section 3 runs
  pp. 18-20: (3.1)-(3.5) on p. 18; (3.6)-(3.9), the A_2 = A_3 iff mu = 1/2 remark (p. 18), the
  small-t remark and identity (3.8) on p. 19; (3.10)-(3.15) on p. 20. Added in the body (after
  thm:p15-w02b-p15-063-chebyshev-comparison) a paragraph attributing thm:p15-conc-common-comparison to
  Section 3 with \cite[pp.~18--19], and the same locator in the closing Sources paragraph. Patch
  requests appended to work/waves/w02b/patches/w02b-p15-063.json: replace the host's line-13 locator
  pp. 13--18 and 20--23 by pp. 13--23; insert the Section 3 attribution with pp. 18--19 after the host
  theorem's last sentence.
- C008: the p. 17 coincidences with (2.16) are parts 2-3 of thm:p15-w02b-p15-063-normal-benchmark
  (annex:p15-w02b-p15-063-normal-benchmark). Patch request 2 rewritten to state both coincidences in
  the host benchmark theorem with \cite[p.~17] and route to that proof.
- Checks: find_fused_spaces no hits; unit-compile ok (14 overfull); check.py no finding in these files.

Block 3, round r3 continuation (assessment disputes C004, C008 against host lines; guard G1).
- The cited lines (body 79-103 and 192-233, annex 49-130 and 323-388) are in the read-only host
  handbook/parts/p15/bounded-concentration-learning.tex and its annex, not in this packet's files. The
  disputed content is already stated and proved in this chapter: C004 in
  thm:p15-w02b-p15-063-exponential-optimality (parts 2-3: exact minimum over h under (2.5), attained at
  lambda_*, hence the smallest bound the method yields; part 4: not the least upper bound), C008 (i)-(ii)
  in thm:p15-w02b-p15-063-normal-benchmark parts 2-3, C008 (iii) in thm:p15-w02b-p15-063-chebyshev-comparison
  parts 2-5 with the p. 14 summary. Neither the host nor the driver inputs can be edited by this packet.
- Re-read printed pp. 14, 15, 17 (physical 3, 4, 6) as images this session; locators p. 14, n. 3, p. 15,
  p. 17, eqs. (1.5)-(1.8), (2.1)-(2.6), (2.16) all seen.
- Patch requests 1 and 2 in work/waves/w02b/patches/w02b-p15-063.json rewritten so the host itself states
  the claims with locators: request 1 states the minimum-over-h result under (2.5) (p. 15) and the
  least-upper-bound distinction (p. 14, n. 3); request 2 states (i), (ii) (p. 17) and (iii) (p. 14). Anchors
  re-verified: each matches the host exactly once.
- G1: same as above; the p01-014 and p02-036 research files are not this packet's and were not touched.
- Checks: find_fused_spaces no hits; unit-compile ok (14 overfull); check.py no finding in these files.
