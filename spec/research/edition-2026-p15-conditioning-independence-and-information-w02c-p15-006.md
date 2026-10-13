# P15 159.1-159.2 (packet w02ca-p15-006): continuation of the w02b-p15-006 chapter

Label tag for new labels: `p15-w02c-p15-006`. All edits are in the editable
hosts `handbook/parts/p15/conditioning-independence-and-information-w02b-p15-006.tex`
and `handbook/annex/p15/conditioning-independence-and-information-w02b-p15-006.tex`,
which are already input by `handbook/parts/p15.tex` line 28 and
`handbook/annex/p15.tex` line 27. No owned body or annex `.tex` file was
created, because every gap belongs in the existing chapter.

## Sources opened in this session

- Grinstead and Snell, CHANCE version dated 4 July 2006,
  `source/references/grinstead-snell-chance-2006/prob-2006-07-04.pdf`.
  PDF p. 150 is printed p. 142 (Definition 4.3); PDF p. 151 is printed
  p. 143, running head "4.1. DISCRETE CONDITIONAL PROBABILITY", carrying
  Definition 4.4 (mutual independence of X_1, ..., X_n, point-mass form).
- Durrett, Probability: Theory and Examples, author Version 5 dated
  11 January 2019, `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`.
  PDF p. 54 = printed p. 46 (pi-system, lambda-system definitions,
  Theorem 2.1.6, Theorem 2.1.7 and its proof with the class L);
  PDF p. 55 = printed p. 47, the Remark directly after that proof.

## Changes

1. ED26-P15-CH-finite-probability-C010 (159.2) and the 159.1 attribution
   dispute: the Definition 4.4 locator corrected from p. 142 to p. 143 in
   item 7 of thm:p15-w02b-p15-006-arbitrary-transfer (body line 180) and in
   the closing Sources paragraph (body line 469).
2. ED26-P15-CH-independent-random-variables-C004 (159.1): new connecting
   paragraph (body lines 186-196) citing Durrett's p. 47 Remark in own
   words, and lemma thm:p15-w02c-p15-006-lambda-class (body lines 198-232)
   with annex proof annex:p15-w02c-p15-006-lambda-class (annex lines
   149-201): L_D contains Omega, is closed under proper differences,
   increasing unions and complements; in the four-point model of item 2 of
   thm:p15-independence-counterexamples with D = C = {1,4}, A = {1,2} and
   B = {1,3} lie in L_C while A cap B = {1} (1/4 vs 1/8) and
   A cup B = {1,2,3} (1/4 vs 3/8) do not; so {A,B} is inside L_C but
   sigma({A,B}) is not, while a pi-system inside L_D has its sigma-algebra
   inside L_D by thm:p15-measure-uniqueness. The Sources paragraph also
   records the p. 47 Remark.

## Symbols

Intake `handbook/registry/symbols-intake-p15-conditioning-independence-and-information-w02c-p15-006.csv`:
`\mathcal L_D` (same role as in annex:p15.independence-generators) and
`\mathcal C` (a pi-system, same role as the generating collections of
thm:p15-independence-generators). No new meaning for either glyph.

## Continuation

- Session 1 (10 October 2026): both duties above written; locators verified
  with pdftotext in this session.
- `python -B tools/waves.py unit-compile work/waves/w02ca/packets/w02ca-p15-006.json`
  fails only because the packet's owned body/annex pair
  (`...-w02c-p15-006.tex`) does not exist: the unit template inputs those
  paths, and no content belongs in them. The same unit-compile routine
  (`waves.unit_compile_packet`) run with the two editable hosts substituted
  as the body/annex pair reports ok, no undefined citations or references,
  and 3 overfull boxes, all from pre-existing long annex labels in headings
  (none from the new item).
- `tools/find_fused_spaces.py` on the edited files: no hits.
- `tools/check.py --tree handbook`: no hard finding in the edited files.
  A soft notation-scope finding for `\mathcal C` at annex line 196 is
  addressed by the intake row.
- No further open item identified in this session for the recorded duties.
