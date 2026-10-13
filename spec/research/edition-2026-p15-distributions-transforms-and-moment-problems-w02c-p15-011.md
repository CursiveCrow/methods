# Edition 2026, P15 chapter 160 (sections 160.1-160.4): packet w02ca-p15-011

Label tag: `p15-w02c-p15-011`. Heading level `\chapter`. Toc tag `%% toc: P15 160 160.1,160.2,160.3,160.4`.

## Files

- Body: `handbook/parts/p15/distributions-transforms-and-moment-problems-w02c-p15-011.tex`
- Annex: `handbook/annex/p15/distributions-transforms-and-moment-problems-w02c-p15-011.tex`
- Symbol intake: `handbook/registry/symbols-intake-p15-distributions-transforms-and-moment-problems-w02c-p15-011.csv`
- Bib intake: `handbook/bib/intake-p15-distributions-transforms-and-moment-problems-w02c-p15-011.bib` (no new keys)
- Patch requests: `work/waves/w02ca/patches/w02ca-p15-011.json` (7 entries; 6-7 are the driver inserts)

## Sources opened in this session (held)

- Durrett, PTE5 author version, `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`.
  - Printed p. 51 (PDF page 59, 1-based): Example 2.1.18 proof, "y = xu, dy = x du", display (2.1.1).
  - Printed pp. 113, 115 (PDF pages 121, 123): opening of Ch. 3 (special cases treated by elementary computation); after Theorem 3.1.3, the remark that it is a special case of the CLT of Section 3.4, so details are left to the reader.
  - Printed p. 136 (PDF page 144): Exercise 3.3.14 with the attribution to E.J.G. Pitman (1956) and John Walsh's part (iii).
- Feller, vol. I, 3rd ed., `source/references/feller-probability-volume1-third-edition/feller-volume1-third-edition.pdf`.
  - Printed pp. 52-54 (PDF pages 67-69): II.9, numerical illustration; footnotes 14 (Stirling, Methodus differentialis, 1730), 15 (Robbins, Amer. Math. Monthly 62 (1955) 26-29), 16 (Wallis; Feller, Amer. Math. Monthly 1967), 17 (refinement); p. 54 remarks after (9.15): 2.0007 at n = 2, 120.01 at n = 5.
  - The numerical constant in "overestimates n!, but with an error of less than [c] n^{-2} per cent" (p. 54) is obscured by a mark in the scan (rendered at 300 dpi, native 340 ppi). It reads as 8 or 9 with a speck before it; not reproduced. The ratio comparison "1 - (12n^2)^{-1}" is legible (with a caret mark over the 2 of 12).

## Decisions

- Convolution C005 and C012 (block 1): replace patches carrying the full text. Superseded in block 2: the assessment asked for supplementary proof items in the owned annex. Block 2 adds body lemmas `thm:p15-w02c-p15-011-cdf-other-order`, `-beta-rescaling`, `-zero-variance-sum` (section `sec:p15-w02c-p15-011-convolution-details`) with annex items, and turns patches 1-3 into short pointer replaces on the three host sentences ("similarly", "similarly", "the same argument with the variables interchanged").
- C015 (b = 0 normal summand): proved directly from `thm:p15-affine-lebesgue` (c = 1, d = nu) rather than by citing the affine clause of `thm:p15-normal-sums`, so the host annex pointer creates no citation cycle. Same for the beta lemma: its proof cites only `def:p15-beta-integral` and `thm:p15-affine-lebesgue`.
- Durrett PTE5 pp. 49-52 (PDF pages 57-60) reopened in block 2: Theorem 2.1.15 states only the order int F(z-y) dG(y); Theorem 2.1.18 proof uses y = xu, dy = x du, (2.1.1) on p. 51; Theorem 2.1.20 (p. 52) assumes positive variances.
- Characteristic-function boundary C021: (1) the Exercise 3.3.24 consequence already exists as `thm:p15-w02c-p15-012-bound-gives-growth` (packet w02ca-p15-012), with a patch by that packet to the criteria host; linked, not rewritten. (2) the Pitman/Walsh attribution: block 1 insert patch on `thm:p15-criteria-pitman-law`, withdrawn in block 2 because `sec:p15-w02c-p15-013-pitman` (packet w02ca-p15-013) already states it; the remaining gap is that file's route insertion (lead).
- De Moivre-Laplace C004, C014, C015: new chapter in owned files (Feller's numerical record certified by Robbins brackets and interval evaluation; Feller's footnote attributions; Durrett's Theorem 3.1.3 derived from `thm:p15-clt-iid`), plus pointer patches on the host boundary and worked-boundaries entry (entries 4-5).
- Finite-probability unit: readonly unit (owner w02c-p15-006); not touched.

## Continuation

- Block 1: body and annex chapter (Feller record, CLT route); patches; intakes.
- Block 2: convolution supplementary section and three annex proof items (C005, C012, C015); patches rewritten (entries 1-3 pointers to the new items; 4-5 unchanged; Pitman insert withdrawn); symbol intake rows H_z, h/k, N. unit-compile ok (5 overfull boxes, all under 6 pt). find_fused_spaces clean.
- Open: the constant of Feller's p. 54 percentage bound (illegible in the held scan); the handbook gives its own certified bound 0.70 n^{-2} per cent and Feller's legible ratio comparison instead.
- Lead actions: put this chapter on the input route at the insertion proposal (after `distributions-transforms-and-moment-problems-w02b-p15-012` in both drivers); apply patches 1-5; put w02c-p15-013 (Pitman/Walsh, C021) and w02c-p15-012 (Exercise 3.3.24) on the route.
- r4 block 1 (2026-10-10): the reassessment found C004, C006, C014, C015 (de Moivre-Laplace) partial only because the chapter is off the input route; every listed item is in the chapter (lines 38-216). Reopened this session: Feller I pp. 52-54 (PDF pages 67-69) and Durrett PTE5 pp. 113, 115 (PDF pages 121, 123); all locators in the chapter confirmed. The p. 54 constant was rechecked at 600 dpi: the glyph is covered by a handwritten "8"-shaped mark (the scan carries other handwritten notes on pp. 53-54), so it stays unread. Added patch entries 6-7: driver insert_after lines for both drivers (anchors unique). The finite-probability C008 gap (Grinstead-Snell Def. 1.4, p. 28, odds recovery p=r/(r+s)) belongs to owner packet w02c-p15-006; nothing written here. unit-compile ok; find_fused_spaces clean; check.py shows no finding for these files.
