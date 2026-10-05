# w02b-p15-065: uniform convergence beyond a countable core, bounded losses, minimax lower bounds

Packet: `work/waves/w02b/packets/w02b-p15-065.json` (P15 chapter 171, sections 171.5-171.8), label_tag `p15-w02b-p15-065`.

## Files

- Body: `handbook/parts/p15/statistical-learning-and-generalization-w02b-p15-065.tex` (new `\chapter`, label `sec:p15-w02b-p15-065-beyond-core`).
- Annex: `handbook/annex/p15/statistical-learning-and-generalization-w02b-p15-065.tex` (14 annexitems, one per body result).
- Host edits: `handbook/parts/p15/vc-dimension-and-uniform-learning.tex` — the paragraph after `def:p15-vcl-countable-core` (singletons have no countable core) now points to `sec:p15-w02b-p15-065-outer`; the closing paragraph points to `sec:p15-w02b-p15-065-beyond-core` and no longer lists the real-loss analogue as absent.
- Bib intake: no new keys. Symbol intake: 8 rows.
- Patch request: `work/waves/w02b/patches/w02b-p15-065.json` (month field of `LuxburgScholkopf2008Author` in handbook.bib; same change as the w02b-p15-064 request).

## Sources opened in this session

- `source/references/p15-vc-learning/luxburg-scholkopf-2008.pdf` (held; 40 pages; printed page = PDF page). Locators used and seen: Section 2.2, p. 5 (measurability set aside when F_all is introduced); Section 5.2, p. 17, Lemma 4 (ghost-sample comparison under m eps^2 >= 2, stated "without proof" by the source). Nothing else from this source is presented.
- `held-sources.json`: the only held copy of Vapnik-Chervonenkis 1971 is `source/references/acq-r1-ACQ-2026-10-0372/vapnik-chervonenkis-1971-uniform-convergence-ru.pdf`, the Russian original (TVP XVI(2), pp. 264-279). The unit requires the SIAM English presentation (Theory Probab. Appl. 16(2), 264-280). Different version, so no source-specific 1971 presentation was written (A3).

## Provenance of the mathematics

All results in the new chapter are proved in the annex from first principles plus already-proved handbook results (`thm:p15-vcl-sauer`, `thm:p15-vcl-core`, the arithmetic of `annex:p15.vcl.samples`, `thm:p15-w02b-p15-064-decomposition`). No constant is credited to a source. The CH well-ordering example and the Sierpinski-type holdout failure are written with explicit hypothesis (continuum hypothesis) and are not attributed (no held source).

## Decisions

- Measurability regime: "symmetrization-measurable" = D_m and K_m completion-measurable for every m. Conclusions in outer probability. Ghost step uses the outer Fubini inequality (iterated <= joint), which needs no measurability; swap averaging is the only step needing completion-measurability.
- Real loss: level-set (layer-cake) reduction to an event class, so the same theorem, growth and sample sizes apply.
- Lower bounds: realizable m <= (d-1)/(16 eps) => P(R >= eps) >= 1/8 (eps <= 1/8, d >= 2); agnostic m <= d/(512 tau^2) => P(excess >= tau) >= 1/16 (tau <= 1/16). Constants unoptimized; proofs via unseen-point fair bits and the Bhattacharyya affinity / Cauchy-Schwarz bound.
- Readonly units ED26-P15-CH-bounded-concentration-learning (owner w02b-p15-063) and ED26-P15-CH-occam-learning (owner w02b-p15-047): not written here. The 171.8 disputes C004 and C008 belong to w02b-p15-063.

## Not supplied

- Source-specific reconstruction of the 1971 paper's finite-sample estimates and the necessary-and-sufficient entropy condition: blocked_source (SIAM English version not held).
- The 2011 Handbook of the History of Logic chapter (von Luxburg-Schoelkopf, ch. 16, pp. 651-706): not held; only the 2008 author version is held.
- Rates under the intermediate noise conditions are proved for finite classes only; for infinite classes of finite VC dimension (localized / relative-deviation bounds) they are not derived. The body warning says so.

## Earlier continuation (block 2)

- Status at stop: body and annex written for C01, C03, C04, C05 material; C02 blocked_source. `unit-compile` fails only on the biber WARN for the canonical bib entry `LuxburgScholkopf2008Author` (month = {September}); the patch request is filed. No undefined refs or citations in the unit.
- Next: after the lead applies the bib patch and inserts the chapter into `handbook/parts/p15.tex` after `parts/p15/bounded-concentration-learning` and the annex into `handbook/annex/p15.tex` after `annex/p15/bounded-concentration-learning`, rerun unit-compile and `check.py --tree handbook`. If the SIAM 1971 English presentation is acquired, write the source-specific reconstruction (C02).

### Block 3 (171.7 noise conditions; 171.8 cross-links)

- New body section `sec:p15-w02b-p15-065-noise-conditions` (body lines 415-621): definition of bounded-noise (margin gamma), margin (exponent a, constant C) and variance (kappa, B, relative to a minimizing member) conditions; lemma of relations (realizable => gamma=1; bounded noise => margin cond. and kappa=1, B=1/gamma; margin => kappa=a/(1+a), B=2C^{1/(1+a)}; kappa=0 always; P(eta=1/2)>0 excludes kappa>0); rate theorem for ERM over a finite class via the Bernstein form of thm:p15-variance-tail-chain; sample-size corollary for the four regimes; lower-bound corollary (the agnostic construction has bounded noise with margin 16 tau, so 1/(gamma eps) cannot be removed when eps = gamma/16); worked threshold example (7611 vs 166080 vs 608869); warning. Annex items at annex lines 553-815.
- Names "Massart" and "Tsybakov" are not used: no held source for them (held-sources.json has no Massart-Nedelec, Mammen-Tsybakov or Tsybakov 2004). The only source anchors are von Luxburg-Schoelkopf 2008 author version, Section 2.2 p. 3 (learning harder as eta approaches 1/2) and Section 7.4 p. 29 (assumptions on label noise improve estimation-error rates; "fast rates"), both read this session from the held PDF (printed page = PDF page).
- Within the noise section the optimization tolerance is written vartheta, since eta is the conditional label probability (as in sec:p15-w02b-p15-064-prediction-risk).
- 171.8 C004/C008 disputes: material is in the owner packet w02b-p15-063 (thm:p15-w02b-p15-063-exponential-optimality, -chebyshev-comparison, -normal-benchmark); this chapter's Relationships paragraph cross-links them. Not written here (readonly unit).

### Block 4 (171.7 noise rates for classes of finite VC dimension)

- Body lines 614-780: def:p15-w02b-p15-065-ternary (ternary class T, pattern growth, n_g, self-normalized two-sample discrepancy J_m, completion-measurability of J_m as the hypothesis; T_H = {xi_h} u {-chi_h}); lemma ternary-core (xi_h^2=|xi_h|=chi_h, Pi_{T_H} <= 2 Pi_H, countable core => J_m measurable); lemma relative (P* of {exists g: Pg - P_m g > sqrt(80 max{P|g|,P_m|g|} L/m)} <= 2 Pi_T(2m) e^{-L}); theorem vc-noise-rate (constants 160, 80; item 1 max{(640BL/m)^{1/(2-kappa)},160L/m}; item 2 max{3 vartheta,(1440BL/m)^{1/(2-kappa)},240L/m}; L = ln(4 Pi_H(2m)/delta)); corollary vc-noise-orders (realizable 640L/m, bounded noise 640L/(gamma m), margin, unconditioned); example with all thresholds (m=1550000 gives 0.01 at delta=0.05; item 4 > 0.089). Warning, Method step 4, Limitations, Relationships, chapter item 4 and section inputs updated.
- Annex lines 817-1119: full proofs. Ghost step: Chebyshev (variance <= P|g|) plus Markov on P'_m|g| <= 4P|g|, probability >= 1/2 since L > ln 2; outer-Fubini as in annex outer-uniform; swaps: cosh bound normalized by s <= 2 n_g; union over patterns.
- No source is credited with these constants; the result is proved, not reproduced. No held source for the relative-deviation literature (Vapnik-Chervonenkis 1974, Anthony-Shawe-Taylor) was used; none is cited.

## Continuation

- Status at stop: VC-class noise rates written with annex proofs (block 4). find_fused_spaces clean; check.py --tree shows no finding in this packet's files; unit-compile reports only the biber WARN for the canonical `LuxburgScholkopf2008Author` month field (patch request work/waves/w02b/patches/w02b-p15-065.json unchanged, lead must apply); overfull 23.
- G1 guard: the four untracked spec/research files of w02b-p01-014 and w02b-p02-036 are not this packet's; not touched.
- Remaining: removal of the ln(2em/d) factor (localized complexity) not derived; C02 of ED26-METHOD-uniform-generalization still blocked_source (SIAM English 1971 version not held); 2011 published chapter not held.
