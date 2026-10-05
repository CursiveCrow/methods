# P15 166.2 Joint and conditional entropy, dependence and information loss (w02b-p15-041)

## Provenance

- Source opened this session: `source/references/acq-r1-ACQ-2026-10-0320/shannon-1948-mathematical-theory-communication.pdf`
  (55-page reprint with corrections; PDF page = printed page, checked on pp. 10-13, 29-30, 35-37).
  Locators used and seen: p. 11 (Theorem 2 statement; x labels a number), p. 12 (Section 6 properties 3-6),
  p. 20 (Section 12: equivocation, R = H(x) - H_y(x), 0.081 bits, 919 bits/s, independent channel),
  p. 21 (H_y(x,z) >= H_y(x); H_{yz}(x) >= H_y(x) - H_y(z) >= H_y(x) - H(z); three forms of R),
  pp. 35-38 (Section 20, properties 1-9).
- Re-opened this session (4 October 2026, block 2): pp. 11, 12, 20 (Theorem 10 statement is on p. 20), 21, 35, 36, 37, 38 via pdftotext; all locators kept in the files were seen.
- Theorem 2 / Appendix 2 (pp. 28-29) was read but is presented in 166.1 by w02b-p15-040
  (`thm:p15-w02b-p15-040-characterization`); this unit cross-references it and does not repeat it.
- Hajek-Staffel held PDF (`source/references/p15-rationality-4-1/hajek-staffel-2021-publisher.pdf`): printed p. 247
  rendered and read; source figures are C*(p) = 0.438, C*(~p) = 0.572 (sum 1.010). Both orientations of the KL objective,
  and the generalized unnormalized form, are minimized at (3/7, 4/7) = (0.4286, 0.5714) on probability pairs; the
  source's figures are not reproduced by any of these. Reference-list pages: 249 (De Bona-Staffel, de Finetti,
  Diaconis-Zabell, Jeffrey), 250 (Kemeny, Ramsey, Savage, Schervish et al.), 251 (Zynda). No Bolker entry (p. 241).

## Editorial decisions

- Positive-cell convention for finite sums (source sums over all cells).
- Averaging exception read as "the averaged vector is a rearrangement" (the matrix reading is false for uniform p).
- Theorem `thm:p15-w02b-p15-041-loss` and the conditional subadditivity part of
  `thm:p15-w02b-p15-041-correction` are editorial consequences, marked as not in the source.
- Block 2 de-duplication: the earlier continuous section (density Gibbs lemma, volume bound, joint/conditional
  densities, density averaging, change-of-variables premise `def:p15-w02b-p15-041-cov`, coordinate theorem, moment
  maxima, y=x^2 warning) duplicated w02b-p15-042 (166.3, `sec:p15-w02b-p15-042-continuous-entropy`), which proves all
  nine Section 20 items with a sharper coordinate-change hypothesis and a proved linear/product case. Those items were
  removed and replaced by cross-references plus pair-specific content not in 042: `def:p15-w02b-p15-041-density`
  (rate of a pair with a joint density), `thm:p15-w02b-p15-041-density-rate` (three forms, symmetry, nonnegativity,
  independence equality), `thm:p15-w02b-p15-041-coordinates` (item 1 = 042 item 8 restated for the label used by
  w02b-p15-040; item 2 = how H(y,u), H_u(y), H_y(u), R move when one variable is recoded), and
  `def:p15-w02b-p15-041-recoding-example` (negative entropies with positive rate; linear, nonlinear zero-shift and
  mixing recodings). Labels `def:p15-w02b-p15-041-density` and `thm:p15-w02b-p15-041-coordinates` are kept because
  w02b-p15-040 references them; 040's example (y=-log x, H(y)=H(x)-E log|J|) still matches item 1.
- Removed labels: thm:...-density-gibbs, -volume, -density-joint, -density-averaging, -moment-max, def:...-cov,
  def:...-coordinate-boundary. Only w02b-p15-044's return note mentioned -moment-max (as not cited).

## Continuation

- Written: body `handbook/parts/p15/information-and-description-based-inference-w02b-p15-041.tex` (499 lines),
  annex `handbook/annex/p15/information-and-description-based-inference-w02b-p15-041.tex` (347 lines);
  unit-compile ok; check.py shows only the intake bib-key finding; fused-space check clean.
- Guard G1 findings name spec/research files of w02b-p01-014 and w02b-p02-036 (untracked, written 18:15-18:23 by
  those packets). This packet did not write them and may not modify or delete them; the lead must attribute them.
- Patch requests for the RAT2021 4.1 disputes are in `work/waves/w02b/patches/w02b-p15-041.json` (owner w02b-p15-022).
- Route: both files still need \input lines in handbook/parts/p15.tex and handbook/annex/p15.tex after the
  w02b-p15-040 inputs (lead-owned drivers).
- Open: (1) the multivariable C^1 change-of-variables theorem is not proved in the handbook and no held analysis
  text carries it; 042's hypothesis definition isolates it; (2) the coding half of Shannon's Theorem 10
  (p. 20 statement, pp. 20-21 proof sketch on long sequences) is not presented.
