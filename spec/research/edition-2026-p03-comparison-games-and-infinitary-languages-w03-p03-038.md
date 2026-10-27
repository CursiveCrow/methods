# P3 chapter 35, sections 35.1-35.4: comparison games (packet w03a-p03-038)

## Files

- Body: `handbook/parts/p03/comparison-games-and-infinitary-languages-w03-p03-038.tex` (sec:p03-w03-p03-038-comparison-games, subsections 35.1-35.4).
- Annex: `handbook/annex/p03/comparison-games-and-infinitary-languages-w03-p03-038.tex` (20 annexitems, one per proved= body result).
- Bib intake: no new keys (cites only Fraisse1954).
- Symbol intake: 12 rows.
- Patch requests: `work/waves/w03a/patches/w03a-p03-038.json` (driver inputs; pointer sentences in qe-categoricity-games-supplement.tex for thm:p03-ef, thm:p03-ef-inexpressibility, def:p03-ef-connectivity).

## Sources opened in this block

- `source/references/fraisse-1954/fraisse-1954-asens-71-363-388.pdf` (hash recorded in held-sources.json), extracted with pdftotext and read: section 5 (5.1, Theorem V, 5.2, 5.2.1, 5.3 on p. 377; 5.4 on p. 378; 5.4(2) proof end, 5.5, 5.5.1 on p. 379), section 10.1-10.2 (p. 388). The whole text was searched for jeu, joueur, rang, quantif, formule, elementaire, logique: the only first-order-logic content is 10.1 (and the introduction's announcement of it). This supports the statement that the article contains no game, no quantifier rank and no characterization of elementary equivalence.
- The condition named in 10.1 is OCR-garbled in the extraction, so the reader text names only "the conclusion of Theorem IV on common extensions", which is legible.
- `tmp/edition-2026-catalog-src038/tail-039-068/SRC-049-pageplace-preview-2026-09-09.reading.txt`: the contents list Chapter X (Kolaitis, Game Quantification) at p. 365, but the preview body ends in Chapter II. No Chapter X body is held.
- Online attempt: https://projecteuclid.org/ebooks/perspectives-in-logic/Model-Theoretic-Logics/chapter/Chapter-X-Game-Quantification/pl/1235417276 returned a bot-check page. It was not bypassed.

## Proof provenance

All proofs in the annex were written in this block. They are self-contained or use proved handbook results: thm:p08-bvb501-potential-isomorphism, thm:p03-morley-approximant-properties, thm:p03-rn-dlo-extension, thm:p03-rn-dlo-uniqueness, thm:p01-w02-p01-011-finite-coding and def:p06-club-stationary. No external locator is attributed to the finite-game theorem, the connectivity bound, the long-game analysis or the orders Phi(S). The Phi(S) construction and its club analysis are presented without attribution, because no held or online source for them was read in this block.

## Existing treatments found (A9)

- Listed in the packet: def:p03-ef-game, thm:p03-ef, thm:p03-ef-inexpressibility, def:p03-ef-parity, def:p03-ef-connectivity (supplement), and def:p02-lomega-one-omega.
- Not listed, and linked from the new text: the P8 potential isomorphism and finite-rank game (src-025-501), the Morley approximants (n-a-004-02), the DLO extension and uniqueness results (n-a-001-01), and the P6 club definitions and Gale-Stewart theorem.
- Not listed, and found in this wave: `handbook/parts/p03/comparison-games-and-infinitary-languages-w03-p03-039.tex` (sections 35.5-35.7, written after Marker's lectures). It contains its own game G(M,N), Karp's theorem, an approximant rank characterization and a (Q,<)/(R,<) example. Those overlap the comparison lemmas of 35.3 here, which are game-form statements built on the P8 and Morley results. A crosslink request was raised; no \cref to that in-flight file was written.

## Symbol overlaps for the lead

- \mathbin{\triangle} (symmetric difference, local to 35.4) and P6's \mathop{\triangle} (diagonal intersection).
- \Phi(S) (local to 35.4) and the Scott formulas \Phi^M_{a,alpha} in the 039 file.
- \equiv_k (rank-k formula agreement) and \equiv_\alpha (Morley approximants).

## Block 1 rerun (2026-10-12)

- Re-read the whole body and annex against the assessment gaps (GOAL-02, GOAL-03, S01-BRIDGE, 35.3 MP-0, 35.4 MP-0); the gaps were stated against qe-categoricity-games-supplement.tex, and this file is not yet on the input route (driver insertion pending with the lead). Proofs re-checked; two edits: dropped the word "standard" in the 35.3 opening, and replaced an unproved "need not contain the union" remark about long-game determinacy by a statement about what the closed-game argument does not give.
- Ehrenfeucht 1961 is now held: source/references/acq-r1-ACQ-2026-10-0115/ACQ-2026-10-0115.pdf (hash recorded in held-sources.json; image-only scan of pp. 129-141). Rendered with pdftoppm and read all 13 printed pages in this block. Wrote the subsubsection sec:p03-w03-p03-038-ehrenfeucht (body) with annex proofs: setting and Definitions 1-2 (pp. 129-130), games H_n and G_n (p. 130), integers/rationals example (p. 131), strategies and determinacy (pp. 131-132), support s(x) (p. 132), Theorems 1-3 (pp. 132-133), Theorem 4 (p. 134), section 3 example (pp. 134-135), Theorems 5-7 and the example after Theorem 7 (pp. 135-136), the Remark (p. 136), Theorem 8, its Lemma, Theorems 9-10 (pp. 136-137).
- Reading conventions written into def:p03-w03-p03-038-e61-reading (individuals are atoms; at least one individual; iota in A; restricted quantifier as one prefix symbol and the n-k quantifier count). Each is tied in the text to the source use that forces it. Theorem 4 is stated with A countable, which the source's proof uses (aleph_0 Skolem functions).
- Printed slips recorded in reader text: the Lemma refers to "Theorem 7" and Theorem 9 cites "Theorem 3"; Theorem 18 lists "i = 1, 2, 2" (Part II, not written).
- The source's reference [3] for Fraisse is the 1954 Alger publication, not the Annales ENS article (Fraisse1954); the reader text says so.

## Block 2 (2026-10-12)

- Fixed the G8 hits in this note (hash strings replaced by a pointer to held-sources.json).
- Re-rendered the held Ehrenfeucht 1961 scan (pdf pages 6-7 = printed pp. 138-141; the pdf holds two printed pages per sheet) with pdftoppm at 200 dpi and read Part II in full.
- Wrote sec:p03-w03-p03-038-e61-ordinals (body 731-1113) and annex items e61-wins ... e61-thm18 (annex 858-1486): the models M_a, M_ab and the class of all ordinals for T_1, T_2, T_3; the relation W_j (choice-free "II wins the remaining j rounds", needed because Theorem 18 applies the game theorems to the class of all ordinals); an ordinal-arithmetic lemma (left subtraction, division, CNF bounds, absorption, CNF comparison, addition and multiplication formulas) proved from the cited P6 laws; Theorem 11 and the segment lemma via ordered sums; congruence mod c; Theorem 12 by the source's induction, with a class form; Theorem 13; the exponent-lifting lemma and Theorems 14 and 16 (and class forms); Theorems 15 and 17 (and class forms); definability, the source's (bullet) and (bullet bullet), the initial-segment lemma (proof completed via the map h), Theorem 18 with the Tarski conjecture context; worked example (first move in H_2(M_{omega^2}, M_{omega^2 2}) and omega^omega definable in T_2); failure case omega vs omega+1.
- Reading decisions recorded in reader text: open vs half-open segment types; printed "+ a d_1" in the first b-display; Theorem 14 index slip; Theorem 15 cites "12 and 13" and Theorem 16 cites "Theorem 13" where 14 is meant; Theorem 18 printed for i = 1, 2, 2; the source's side condition on c in the congruence definition (phrased via cofinality) is reported but not used; the source's proof of Theorem 18 applies set-pair theorems to the class, supplied here by class forms.
- (bullet) is called "not difficult" in the source and not proved there; the annex proof (multiples of omega^k in T_1, relativization to additive principal ordinals for T_2 and T_3) is this handbook's own.
- The source's footnote on p. 138 cites a Feferman summary (Cornell 1956) for the segment argument; not read, not cited with a locator.

## Block 2 rerun (2026-10-13)

- Assessment gap was the G3/G4 guard: `tools/check.py --tree handbook` timed out at 180 s in the assessor run. Re-ran it here without the 180 s cap; result recorded below.
- Moved two long inline formulas to displays (body: the H_n prefix form in def:p03-w03-p03-038-e61-setting; annex: the AP(v) formula in annex:p03-w03-p03-038-e61-below) to reduce overfull boxes; no content change.
- Online attempts this run (none yielded a readable copy):
  - Kolaitis, Chapter X, Model-Theoretic Logics: Project Euclid lists it as open access, but https://projecteuclid.org/download/pdf_1/euclid.pl/1235417276 and the chapter .pdf URL both return a JavaScript bot-check page (HTTP 200, 1 KB HTML). Not bypassed.
  - Hodges 1993: web search found only Cambridge Core abstract pages, library catalogues and paid retailers; no free legitimate copy of any version.
  - Ebbinghaus-Flum-Thomas 1994 (2nd ed.) and 2021 (3rd ed.): Springer pages only (paywalled); no free legitimate copy of any version.

## Continuation

Written: D-P4-001 GOAL-01..03 and C01, S01-BRIDGE, S02 (Parts I and II), 35.3 MP-0, 35.4 MP-0.

Block 2 rerun (2026-10-13): `tools/check.py --tree handbook` finished in 150 s; no finding names a file of this packet. unit-compile ok (27 overfull boxes). find_fused_spaces: no hits.

Remaining:
- N-a-065-S03 (Hodges 1993) and N-a-065-S04 (EFT 1994, 2nd ed.): blocked_source; online search 2026-10-13 found no legitimate free copy of any version.
- ED26-SRC-049-0010 C001-C004 (Kolaitis Chapter X): blocked_source (held preview lacks the body; Project Euclid open-access PDF behind a bot check).
- Patch requests in work/waves/w03a/patches/w03a-p03-038.json still with the lead (driver insertion).
