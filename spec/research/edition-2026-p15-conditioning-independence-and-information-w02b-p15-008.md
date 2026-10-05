# Packet w02b-p15-008: provenance note

Part P15, chapter 159, sections 159.7 and 159.10. Label tag `p15-w02b-p15-008`.

## Owned files

- Body: `handbook/parts/p15/conditioning-independence-and-information-w02b-p15-008.tex`
- Annex: `handbook/annex/p15/conditioning-independence-and-information-w02b-p15-008.tex`
- Symbol intake: `handbook/registry/symbols-intake-p15-conditioning-independence-and-information-w02b-p15-008.csv`
- Bib intake: no new keys (only `DurrettPTEAuthor2019`, already in `handbook/bib/handbook.bib`).
- Patch requests: `work/waves/w02b/patches/w02b-p15-008.json` (three entries).

## Source held and opened

`source/references/durrett-probability-2019-01-11/PTE5_011119.pdf` (Durrett, Probability: Theory
and Examples, author version 5 dated 11 January 2019). PDF page = printed page + 8 in Chapter 4.

Locators seen in this session (via pdftotext):
- Printed p. 210 (PDF p. 218): Theorem 4.1.9 (a) linearity, (b) order, (c) X_n >= 0, X_n increasing
  to X with EX finite gives E(X_n|F) increasing to E(X|F); the Remark directly after it obtains the
  decreasing variant by applying (c) to Y_1 - Y_n, under E|Y_1| and E|Y| finite.
- Printed p. 209 (PDF p. 217): Example 4.1.6 (joint density) and its Remark.
- Printed pp. 210-211 (PDF pp. 218-219): proof of Theorem 4.1.9 and Theorem 4.1.10 (conditional
  Jensen) with the rational affine family.
- Printed p. 214 (PDF p. 222): Section 4.1.3, the r.c.d. definition, continuation of Example 4.1.6,
  Theorem 4.1.16, and the statement that r.c.d.'s do not always exist. Printed p. 215 (PDF p. 223):
  Theorems 4.1.17 and 4.1.18. These locators, used in the earlier sections of the body, were
  re-checked in this session.

## Assessment gaps addressed in this session (ED26-P15-CH-conditional-expectation-C004)

1. The host sentence "Arbitrary modifications on an F_0-null set need not preserve G-measurability"
   (thm:p15-conditional-limits) had no witness. Written: thm:p15-w02b-p15-008-null-modification
   (exact criterion: a.s.-equal modification is a version iff G-measurable; resets on G-null sets
   by G-measurable values are versions; trivial G on [0,1] with Lebesgue measure: versions are
   pointwise unique and EX + 1_{0} is not a version), proof annex:p15-w02b-p15-008-null-modification.
2. Durrett's decreasing variant (remark after Theorem 4.1.9, printed p. 210) was not stated. Written:
   thm:p15-w02b-p15-008-decreasing part (i), with an explicit G-measurable exceptional set; part (ii)
   shows E|Y_1| finite cannot be dropped (Y_n = 1/omega on (0,1/n), trivial G). Proof
   annex:p15-w02b-p15-008-decreasing derives it from item 1 of thm:p15-conditional-limits via
   Y_1 - Y_n, as in the source. Worked example def:p15-w02b-p15-008-decreasing-worked (two-cell
   partition, Y_n = omega^n).
3. Host links: two patch requests (host body after thm:p15-conditional-limits; host annex at end of
   annex:p15.conditional-limits). The lead applies these; the hosts are read-only for this packet.

## Overlap with packet w02b-p15-002

The unit ED26-P15-CH-conditional-expectation is listed as owned by w02b-p15-002. While this session
ran, w02b-p15-002 wrote thm:p15-w02b-p15-002-null-modification in its own file, a superset of
thm:p15-w02b-p15-008-null-modification, and that file cross-references this packet's labels
(thm:p15-w02b-p15-008-null-modification, thm:p15-w02b-p15-008-ae-counterexample). Removing this
packet's theorem would break those references, so it is kept; consolidation is a lead decision
(proposed in the return file). w02b-p15-002 has no decreasing-variant treatment at the time of writing.

## Continuation

- Written this session: text for the two C004 gaps above, symbol rows, patch requests, unit-compile ok,
  fused-space check clean, check.py shows no finding in owned files.
- Open: lead to apply the two conditional-expectation patch requests; lead decision on consolidating
  the two null-modification theorems (w02b-p15-002 and w02b-p15-008).
