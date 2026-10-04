# w02b-p15-034: partition updates and conglomerability (165.6)

Packet: `work/waves/w02b/packets/w02b-p15-034.json`, label tag
`p15-w02b-p15-034`, block 1. Unit `ED26-METHOD-imprecise-probability`,
gap C03 as stated by the independent assessment: the host
`handbook/parts/p15/imprecise-probability.tex` (lines 384-389) asserted with
a citation only that unconditional coherence is insufficient for joint
conditional claims on infinite partitions and that conglomerability matters.

## Source used (held, opened this session)

- `source/references/p15-imprecise-probability/miranda-survey-lirmm.pdf`
  (SHA-256 B8C24C2E...4C879E, 44 PDF pages), bib key
  `MirandaCoherentLowerPrevisionsCapture` (already in handbook.bib).
  Extracted with pdftotext -layout; printed page numbers read from the page
  footers. Locators used and verified:
  - §3.1, p. 17: contingent/updated readings, updating principle, (SC1)-(SC2), eq. (9).
  - p. 18: dependence on values in B only, eq. (10) for G(f|B) and G(f|\mathcal B), (C1)-(C3) for linear domains with constants.
  - §3.2, p. 19: conglomerative principle; joint coherence condition (11).
  - p. 20: Remark 1 (weak coherence); §3.2.1 natural extension, eq. (12).
  - pp. 20-21: the three infinite-partition defects (citing Walley §§6.6.6-6.6.10, 8.1.3); Example 3 on p. 21 (not reproduced; it is stated with "it can be checked").
  - §3.3, p. 22: (JC1), (JC2), the generalized Bayes rule.
  - p. 23: B-conglomerability definition and the existence equivalence; justification continues p. 24.
  - p. 24: full conglomerability; tie to countable additivity for linear previsions; vacuous model least at P(B)=0.
  - §5.1, p. 31: de Finetti rejects conglomerability.
  - §5.2, p. 32: Williams' condition (13); comparison with (11); W-coherence need not be conglomerable.
- No Walley 2014 StatsRef body is held (packet `held_paths: []` for the
  METHOD unit). Nothing here is presented as that article's content.

## What was written

- Body `handbook/parts/p15/probability-logics-and-alternative-representations-of-w02b-p15-034.tex`
  (chapter, toc tag `%% toc: P15 165 165.6`).
- Annex `handbook/annex/p15/probability-logics-and-alternative-representations-of-w02b-p15-034.tex`
  with five annex items, all full proofs.
- Declared partition-update semantics: `def:p15-w02b-p15-034-semantics`
  (separately coherent on L(Omega) + JC1/JC2 with the test sets of (11)).
- Proved: cellwise lemma; necessity (JC => GBR on positive cells and
  B-conglomerability); existence iff conglomerable with the least update
  (GBR on positive cells, vacuous on null cells); explicit finitely additive
  counterexample on N+ x {0,1} (P = (mu + nu_1)/2, P(B_n) = 2^{-n-1},
  P(Y_1) = 3/4, cellwise 1/2, sure loss -1/2 from the infinite portfolio);
  W-coherence (13) holds for the same assessments.
- The counterexample's own construction is original to this text (a
  mixture of a countably additive and a purely finitely additive part); it is
  not attributed to the source. The finitely additive nu comes from the
  existing representation theorem applied to liminf (Choice as already
  assumed in sec:p15-imprecise-probability).
- Patch request `work/waves/w02b/patches/w02b-p15-034.json`: replace the
  citation-only paragraph in the read-only host with pointers to the new
  results (anchor verified to match once).

## Not settled / open

- MP-0: the selected Walley 2014 StatsRef article body remains unheld;
  source matching for the METHOD unit stays blocked_source.
- Not proved and not used: several partitions at once, restricted domains,
  natural extension on infinite partitions (source pp. 20-21 reports), and
  joint coherence of any more informative choice (e.g. cellwise regular
  extension) on infinitely many null cells. The reader text says so.
- RAT2021 4.7 unit is readonly here (owner w02b-p15-032).

## Checks run

- `python -B tools/waves.py unit-compile work/waves/w02b/packets/w02b-p15-034.json`: ok, no errors, no undefined refs/cites.
- `python -B tools/find_fused_spaces.py` on both tex files: no hits.
- `python -B tools/check.py --tree handbook`: no finding naming these files.

## Continuation

Block 1 finished the C03 partition-update gap. Nothing is left to write for
C03 in the owned files. Next steps belong to the lead: place the body input
after `parts/p15/rationality-5-3` and the annex input after
`annex/p15/rationality-5-3` (or, preferably for reading order, directly
after `imprecise-probability`), apply the patch request, and merge the
symbol intake. The Walley 2014 body acquisition (MP-0) remains open.
