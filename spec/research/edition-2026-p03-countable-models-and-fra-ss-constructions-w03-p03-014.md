# P3 26.1-26.3 (packet w03a-p03-014): Fraisse 1954 and Rado 1964 source remarks

Label tag: `p03-w03-p03-014`. Chapter 26, sections 26.1, 26.2, 26.3.

## Sources read in this session

- Fraisse1954: held PDF `source/references/fraisse-1954/fraisse-1954-asens-71-363-388.pdf`
  (NUMDAM scan of Ann. Sci. ENS (3) 71, 1954, pp. 363-388, version of record).
  Text layer extracted with pdftotext; pages read for this block: 363-365 (Sec. 1.1-1.4,
  nn. 1-4), 369 (Sec. 2.4-3.2, n. 5), 372 (Sec. 3.8-3.9), 374 (Sec. 4.1-4.3),
  376-377 (Sec. 4.4-5.3, nn. 7-8), 379-380 (Sec. 5.5-6.3), 382 (Sec. 7.3-7.4),
  383 (Sec. 8.1-8.3), 387 (Sec. 9.4-9.5), 388 (Sec. 10.1-10.2, nn. 9-11).
- Rado1964: held page images `source/references/rado-1964/rado-original-1.png` (p. 331),
  `rado-original-2.png` (pp. 332-333), `rado-original-3.png` (pp. 334-335),
  `rado-page337-4.png` (p. 337). Version of record, Acta Arith. 9 (1964).
- Hodges1993 ch. 7: not held (only contents and 2011 corrigenda are held). Web search
  2026-10-12 found only the paywalled Cambridge Core chapter page
  (https://www.cambridge.org/core/books/model-theory/countable-case/07C420D2BE9BF122AA1BCA621A853BB3)
  and contents listings; no legitimate free copy.

No sources were read online for content.

## What this block changed

Fraisse host (`handbook/parts/p03/presentations/fraisse-1954.tex`):
- Opening: order facts of Sec. 1.1 (pp. 363-364); announcements n. 1; projection-filter
  history (Sec. 1.1 text with n. 2, p. 363; n. 5, p. 369). Wording corrected so that the
  "set out differently" remark is attributed to the Sec. 1.1 text, not to a footnote.
- Principal-filter lemma (Sec. 3.9, p. 372); Gamma_R of an infinite order (Sec. 1.4,
  p. 365) and the ordering corollary (Sec. 4.1, p. 374); condition C hosts for orders and
  the Lindenbaum / Fraisse 1948 attribution (Sec. 4.7, nn. 7-8, pp. 376-377); printed
  one-positive-point example of Sec. 7.3, p. 382 with the explicit repair; Sec. 6.3
  conclusions (p. 380); Henkin / Tarski attribution (Sec. 10.1, nn. 9-10, p. 388).
- New: `thm:p03-w03-p03-014-arithmetic-types`. Part 1: Theorem IV conclusion for an
  arithmetic type plus countable host for countably many countable members (downward LS).
  Part 2: an arithmetic type of binary relations (marked successor chains, every finite
  mark pattern present) fails condition C. This refutes the Sec. 10.1 claim "every
  arithmetic type satisfies C" under the Sec. 4.7 definition of C; the source gives no
  proof (it cites Henkin 1953 p. 414 without stating the theorem). Reader text says the
  claim fails and proves it.

Rado host (`handbook/parts/p03/presentations/rado-1964.tex`):
- Sec. 1.1 p. 331: two distinct edges meet in at most one point.
- Sec. 2.1 p. 333: graphs as one-dimensional simplicial complexes.
- Sec. 2.2 n. 4 p. 333: only "into" needed for the Lemma.
- Sec. 3 p. 335: Theorem 1 -> K_21, Theorem 3 -> K_2l, Theorem 4 -> K_2, Theorem 5
  generalizes them: `thm:p03-w03-p03-014-rado-k2` with annex proof.
- Sec. 4.1 p. 337: Tarski's cofinality function with the source's definition;
  `thm:p03-w03-p03-014-tarski-cf` proves cf(aleph_n) = aleph_cf(n).
- Sec. 4.2 p. 337: the "without loss of generality m initial" remark, reported in
  `def:p03-w03-p03-014-rado-initial` and shown contradicted (as a reduction) by
  `thm:p03-rado64-order-type-boundary`.

Owned annex: proof of the arithmetic-types theorem added; amalgam base in the K_1
proof corrected (the primed copy of the positive point a is no longer adjoined).
LS reference uses the routed label `thm:downward-ls`.

## Existing treatments found

Listed ones used. Also found (not listed in packet): `thm:downward-ls`
(restoration, routed), `thm:fol-compactness` (restoration, routed),
`thm:p06-cofinality-facts` defined in both `parts/p06/cardinal-arithmetic.tex` and
`parts/p06/cardinal-arithmetic-supplement.tex` (duplicate label, not mine).

## Open items

- Hodges 1993 Sec. 7.1 and 7.4 presentation (unit ED26-REQ-N-a-002-03, MAP-06):
  blocked_source.
- Registry row for `\mathrm{cf}(n)` (symbols.csv line 2533) describes it as "aleph index
  of the ordinary cofinality"; proposed note update to name it Tarski's cofinality
  function (source Sec. 4.1, p. 337).

## Continuation

Block 1 finished its listed gaps for units ED26-REQ-N-a-002-01 and -02. Next block:
nothing further is writable for the Hodges unit until Hodges 1993 ch. 7 is held.
Unit-compile ok after this block; no hard check findings in the touched files.
