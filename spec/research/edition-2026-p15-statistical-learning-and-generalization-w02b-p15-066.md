# w02b-p15-066: section 171.11, generalization failure under high capacity or distribution shift

Observed 2026-10-04. Packet work/waves/w02b/packets/w02b-p15-066.json (section 171.11; label tag p15-w02b-p15-066; heading level chapter).

## Source opened in this session

- source/references/p15-vc-learning/luxburg-scholkopf-2008.pdf (von Luxburg and Schoelkopf, Statistical Learning Theory: Models, Concepts, and Results, September 2008 author presentation; key LuxburgScholkopf2008Author; held, listed in held-sources.json). Printed page = physical page (footers checked on pp. 3, 4, 13, 14, 30, 31, 32).
- Read: pp. 2-4 (Section 2.2, assumptions 1-5: no assumption on P, label noise, independent sampling, P fixed and the remark that training and test laws may differ under "covariate shift", P unknown); pp. 13-14 (Section 4.2, memorizing classifier); pp. 30-32 (Section 8, no free lunch; Theorem 9 on p. 32, stated with reference to Devroye et al. and Wolpert, not proved there).
- Locators used in the text: Section 2.2, pp. 3-4; Section 4.2, pp. 13-14; Section 8, pp. 30-32; Theorem 9, p. 32.
- No other held source covers dataset shift, covariate shift or transfer bounds (searched held-sources.json for shift, covariate, adapt, Ben-David, Quinonero, Sugiyama, Shimodaira, Kifer, total variation: no hits). All shift results are therefore the book's own, proved in the annex, and credited to no source.

## Placement

- Body: handbook/parts/p15/statistical-learning-and-generalization-w02b-p15-066.tex, input after parts/p15/bounded-concentration-learning (handbook/parts/p15.tex after line 57) per the packet insertion proposal.
- Annex: handbook/annex/p15/statistical-learning-and-generalization-w02b-p15-066.tex, input after annex/p15/bounded-concentration-learning (handbook/annex/p15.tex after line 56).
- The chapter cross-references sec:p15-w02b-p15-065-lower and its theorems; if the lead places 065 after this chapter the references still resolve.

## What was written

- def:p15-w02b-p15-066-two-laws: training law, evaluation law, risks under each, total variation (reusing def:p15-weak-total-variation), covariate shift and label/concept change for a finite label set, enclosing class.
- thm:p15-w02b-p15-066-enclosing: the five earlier capacity failures (conc-selection-example; occam-unseen-labels; occam-boundaries item 3; vcl-examples items 3 and 2) as instances of an enclosing class too rich for the sample: zero-fit threshold K >= 2^n ln(1/delta) and b_n > 1/2 once K >= 2^n; H_m size >= (N/m)^m, dimension m+1 for N >= m+2, Occam finite bound informative only for epsilon > 1/2 when N >= 2m; memorizer class and finite-subset class of infinite dimension.
- thm:p15-w02b-p15-066-tv-transport: |int f dQ - int f dP| <= TV for f in [0,1], attained via the Hahn positive set of Q-P (thm:p15-hahn-decomposition); transfer of thm:p15-conc-finite-learning (+2d), thm:p15-vcl-erm (+2d), thm:p15-occam-finite (+d); covariate shift TV equals input TV.
- thm:p15-w02b-p15-066-density-transport: bounded density ratio gives R_Q <= B R_P; sharp; impossible when Q charges a P-null set.
- thm:p15-w02b-p15-066-shift-attained: (1) covariate shift with consistent h attains d (d = 1 is occam-boundaries item 2); (2) label shift where the selected candidate loses 2(d - gamma), ERM picks it with probability >= 1 - e^{-2 n gamma^2}; (3) no training-sample certificate for R_Q without an assumption on Q; (4) TV = 1 for a tiny location shift, attained only by thresholds between the supports.
- thm:p15-w02b-p15-066-worked: selection example with n = 10, K = 3068; noisy example of thm:p15-conc-noisy-example under covariate shift (TV bound loose, selected predictor stays optimal) and under concept reversal (TV bound attained, excess 1/2).
- Relations section (fit + capacity + shift decomposition; validation from Q versus from P), hbmethod def:p15-w02b-p15-066-diagnosis, hbwarning def:p15-w02b-p15-066-limits.
- This supplies the "additional transport argument" named at bounded-concentration-learning.tex:417-418 (the host itself is read-only; no pointer from it was added).

## Existing treatments found

- Listed: bounded-concentration-learning and occam-learning chapters (linked, not duplicated).
- Not listed, found and linked: vc-dimension-and-uniform-learning (thm:p15-vcl-examples, thm:p15-vcl-erm, thm:p15-vcl-samples); def:p15-weak-total-variation (weak-convergence-of-laws); thm:p15-hahn-decomposition and thm:p15-signed-measure-examples (radon-nikodym); thm:p15-monotone-integral and thm:p15-nonnegative-integral-laws (integration-expectation); packet w02b-p15-065's lower bounds sec:p15-w02b-p15-065-lower (thm:p15-w02b-p15-065-lower-realizable, -lower-infinite, def:p15-w02b-p15-065-minimax-warning). A first draft of this chapter contained its own shattering lower bound (expected error 1/2(1 - m/N) inside any shattering class) and a dimension-necessity corollary; both were removed in favour of the 065 results to avoid a second treatment.

## Open items

- The readonly units ED26-P15-CH-bounded-concentration-learning (owner w02b-p15-063) and ED26-P15-CH-occam-learning (owner w02b-p15-047) were not edited. The assessment disputes C004, C005 and C008 on handbook/parts/p15/bounded-concentration-learning.tex (Hoeffding p. 15 optimality assertion for bound (2.1); the p. 19 / Section 3 locator for the comparison (3.6)-(3.9); Hoeffding's comparisons of (2.2) and (2.6) with the normal bound (2.16) and of the exponential bounds with (1.5)-(1.6), pp. 14 and 17) remain for the owner packet; Hoeffding 1963 was not opened in this session.
- unit-compile reports one biber WARN on the canonical entry LuxburgScholkopf2008Author (month = {September}); patch request filed at work/waves/w02b/patches/w02b-p15-066.json (same as w02b-p15-064's).
- Transfer under other distances between laws (Wasserstein, discrepancy distances) and reweighting methods are not treated; no held source supports them.

## Checks

- python -B tools/find_fused_spaces.py on both .tex files: no hits.
- python -B tools/waves.py unit-compile: only the canonical biber WARN above; no undefined citations; no unknown references; 1 overfull box (annex item heading).
- python -B tools/check.py --tree handbook: no finding mentions the owned files.

## Continuation

- 2026-10-04: 171.11 US-0 written (body lines 1-415, annex lines 1-345). Remaining for a later pass, if wanted: none recorded within the owned files; the bounded-concentration disputes belong to w02b-p15-063.
- 2026-10-04 (continuation pass): asked to close assessment disputes C004 (Hoeffding p. 15 within-method optimality of (2.1)) and C008 (p. 17 comparisons of (2.2), (2.6), (2.1) with (2.16)) of ED26-P15-CH-bounded-concentration-learning. Not written here: the unit is in this packet's readonly_units, the host handbook/parts/p15/bounded-concentration-learning.tex is read-only, and the treatments already exist in packet w02b-p15-063's chapter: thm:p15-w02b-p15-063-exponential-optimality with annex:p15-w02b-p15-063-exponential-optimality (C004: chord and AM-GM steps are equalities for the Bernoulli law, strict convexity, minimum at lambda_*, smallest uniform bound, n = 1 gap), thm:p15-w02b-p15-063-normal-benchmark parts 2-4 with its annex item (C008: A_2 = normal value iff binomial for p >= 1/2; Theorem 2 bound = normal value iff symmetric two-point; A_1 attained at t = 1-p while Phi(-y) < e^{-y^2/2} never attained), and thm:p15-w02b-p15-063-chebyshev-comparison. Host links are requested in work/waves/w02b/patches/w02b-p15-063.json. A second treatment here would duplicate them. Re-ran unit-compile (only the canonical biber WARN, patch filed), find_fused_spaces (no hits), check.py (no finding on owned files).
