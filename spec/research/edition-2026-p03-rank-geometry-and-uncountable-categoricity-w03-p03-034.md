# Research note: packet w03a-p03-034 (P3 ch. 33, sections 33.5-33.8)

## Source read in this session

- Morley, *Categoricity in Power*, Trans. AMS 114 (1965) 514-538, held file
  `source/references/p03-morley1965/morley1965-categoricity-in-power.pdf`
  (key `Morley1965`). Read in full from the text layer (pdftotext), with page
  535 rendered as an image to check footnotes 22-24 (the text layer garbles the
  exponent in n. 24: it reads kappa^{aleph_0} != kappa).
- No online sources were used.

## Task of this block

Close the assessment gaps listed for ED26-REQ-N-a-006-01 (components N-a-006-C01,
N-a-006-MAP-01, N-a-006-MAP-02): items (1)-(12) of the article not supplied on
the route `presentations/n-a-006-01.tex` + `annex/p03/n-a-006-01.tex`.

Note on ownership: the packet lists all four units as `readonly_units` owned by
w03-p03-033, but the computed task text directed this block to close these
gaps. Edits were confined to this packet's owned files and its editable host
`handbook/parts/p03/presentations/n-a-006-01.tex`. The w03-p03-033 files were
not modified; items already drafted there are cross-referenced.

## Item map (locators all seen in the held PDF)

| item | locator | where now |
|---|---|---|
| (1) intro: Łoś [9], Vaught [16] 1954; DLO / ACF0 framing; Łoś's question; saturated gloss; at most one saturated model per power (n. 2: [10] from Jónsson [5]); derived-space / Cantor-Bendixson analogue; n. 1 dissertation | pp. 514-515, 522 | body sec:p03-w03-p03-034-opening, sec:p03-w03-p03-034-analogue; thm:p03-w03-p03-034-dlo-powers (proved); n-a-006-01 intro sentence and remark after the countability theorem |
| (2) completeness attributed to Vaught [16], Łoś [9] | p. 516 | n-a-006-01 completeness paragraph; also body opening |
| (3) basis power = kappa(A) mod aleph_0 | p. 518 | thm:p03-w03-p03-034-basis-power (proved); n-a-006-01 remark after the types lemma |
| (4) p. 520 remark on other categories; n. 12 terms | p. 520 | def:p03-w03-p03-034-abstract-category, thm:p03-w03-p03-034-abstract-derivative, thm:p03-w03-p03-034-cantor-bendixson (proved); n-a-006-01 remark after Def. 2.2 |
| (5) n. 13 single-point rank | p. 521 | n-a-006-01 remark after degree theorem -> sec:p03-w03-p03-033-variant-rank |
| (6) automorphism condition, n. 14 | p. 523 | n-a-006-01 remark at examples subsection -> thm:p03-w03-p03-033-automorphism-test |
| (7) Thms 3.2, 3.4, 3.5 slight variants of EM [3]; section 3 related to Ehrenfeucht [1],[2] | pp. 515, 525 | n-a-006-01 Ramsey subsection opening |
| (8) nn. 16-18 | p. 528 | n-a-006-01 remark after no-order theorem -> sec:p03-w03-p03-033-attributions |
| (9) n. 20 prime models over countable A, Vaught [18] | p. 530 | n-a-006-01 remark after prime-models theorem (links sec:p03-n-a-003-01) |
| (10) n. 21 | p. 532 | same remark -> thm:p03-w03-p03-033-dlo-density |
| (11) nn. 22-24 | p. 535 | def/thm universal-homogeneous (proved, all infinite powers), thm limit-power (proved, no GCH), thm mv-existence (proved, kappa = kappa^aleph0), thm continuum-bound (proved; gives Morley's asserted example under 2^aleph0 > aleph1); hbwarning def:p03-w03-p03-034-example-limit; n-a-006-01 remark after saturation theorem |
| (12) p. 537 consequence of 4.3+4.6; question (5) verbatim content; conditional remark; Ehrenfeucht [1] Thm 2 and Vaught's fallacy; n. 25 | p. 537 | n-a-006-01 closing questions rewritten with all seven questions stated as in the source; links to thm:p03-w03-p03-033-endomorphism, thm:p03-w03-p03-033-question-five |

## Open items

- n. 24 example: supplied here under 2^aleph_0 > aleph_1 (thm continuum-bound);
  the ZFC example (kappa = aleph_omega) is thm:p03-w03-p03-033-coding-theory in the
  w03-p03-033 file, now cross-referenced from the warning and from n-a-006-01.
- Routing (lead action): the new body/annex files of this packet and the
  w03-p03-033 files must be inserted, otherwise the cross-references added to
  n-a-006-01.tex dangle in the full build. Labels referenced from n-a-006-01.tex:
  sec:p03-w03-p03-034-opening, sec:p03-w03-p03-034-analogue,
  thm:p03-w03-p03-034-basis-power, thm:p03-w03-p03-034-abstract-derivative,
  thm:p03-w03-p03-034-cantor-bendixson, thm:p03-w03-p03-034-universal-homogeneous,
  thm:p03-w03-p03-034-limit-power, thm:p03-w03-p03-034-mv-existence,
  thm:p03-w03-p03-034-continuum-bound, def:p03-w03-p03-034-example-limit,
  sec:p03-w03-p03-033-variant-rank, thm:p03-w03-p03-033-automorphism-test,
  sec:p03-w03-p03-033-attributions, thm:p03-w03-p03-033-dlo-density,
  thm:p03-w03-p03-033-endomorphism, thm:p03-w03-p03-033-question-five.
- The universal-homogeneous theorem is proved directly; Keisler's Theorem A2 and
  Vaught's [18] arguments are not reconstructed (only attributed via Morley n. 22).
- Three overfull boxes in the unit build come from long label-derived annex
  headings.

## Continuation

Rerun of block 1 (same gap list; the assessment quoted HEAD line numbers of
n-a-006-01.tex, i.e. it predates the uncommitted edits of the first run). Verified
items (1)-(12) are each addressed in n-a-006-01.tex or this packet's body file.
Applied the w03a-p03-033 patch requests that target this packet's files
(work/waves/w03a/patches/w03a-p03-033.json): p.517 n.5 Jonsson conditions and the
attribution of Lemma 1.2 to [10] (checked against the rendered p.517); n.12 link to
jonsson-algebraic; n.20 link to countable-prime; n.24 links to coding-theory in
n-a-006-01 and in the example-limit warning. Wrote routing patch
work/waves/w03a/patches/w03a-p03-034.json (body and annex inputs). unit-compile ok;
check.py: only the pre-existing duplicate annex:p3.morley.stabilization; fused
spaces clean. Body 1-369, annex 1-359. Credit for items (5), (6), (8), (10), (12)
and n.24 depends on the lead routing the w03-p03-033 file as well.
