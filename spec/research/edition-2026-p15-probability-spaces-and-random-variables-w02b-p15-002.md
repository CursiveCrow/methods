# Edition 2026, P15 chapter 157 (sections 157.5, 157.6, 157.7): packet w02b-p15-002

Packet: `work/waves/w02b/packets/w02b-p15-002.json`; label tag `p15-w02b-p15-002`.

## Files

- Body: `handbook/parts/p15/probability-spaces-and-random-variables-w02b-p15-002.tex`
  (chapter `sec:p15-w02b-p15-002-mixed-laws`). Present at the start of this
  session; edited here only for overfull lines, two shortened titles, the
  explicit naming of the three classes in the mixed-law clause of
  `thm:p15-w02b-p15-002-regimes`, and a link to the overlapping
  `thm:p15-w02b-p15-008-null-modification`.
- Annex: `handbook/annex/p15/probability-spaces-and-random-variables-w02b-p15-002.tex`
  (section `sec:annex-p15-w02b-p15-002-mixed-laws`). Written in this session;
  it did not exist before.
- Symbol intake: `handbook/registry/symbols-intake-p15-probability-spaces-and-random-variables-w02b-p15-002.csv`.
- No intake bib: the chapter cites only `DurrettPTEAuthor2019` and
  `Feller1971ProbabilityII`, both already in `handbook/bib/handbook.bib`.

## Gaps addressed in this session

| Gap | Annex label | Annex lines |
|---|---|---|
| X-157.5-mixed-decomposition-proofs | `annex:p15-w02b-p15-002-atomic-split`, `annex:p15-w02b-p15-002-three-part`, `annex:p15-w02b-p15-002-mixed-examples` | 112-183, 185-353, 430-544 |
| X-157.7-regimes-corollary-proof | `annex:p15-w02b-p15-002-regimes` | 355-428 |
| X-157.6-null-modification-proof | `annex:p15-w02b-p15-002-null-modification` | 546-652 |

Shared preliminaries (Facts P1-P3: integrals against sums, multiples and
restrictions of measures; the distribution function of a finite Borel measure;
a step-function squeeze for the integral of x over (0, c]) are at annex lines
6-110. Every proof step relies on handbook results by label
(`thm:p15-cdf-laws`, `thm:p15-lebesgue-decomposition` with its uniqueness
clause, `thm:p15-radon-nikodym`, `thm:p15-density-calculus` item 1,
`thm:p15-stieltjes-construction`, `thm:p15-cantor-singular-law`,
`thm:p15-conditional-existence`, `thm:p15-signed-integral-laws`, and the
integration-chapter results), not on source locators.

## Source locators checked in this session

- Feller, *An Introduction to Probability Theory and Its Applications*, vol. II,
  2nd ed. (held: `source/references/feller-probability-volume2-second-edition/feller-volume2-second-edition.pdf`):
  sec. V.2 Definition 2 (atom, atomic distribution) and the dense-atoms example
  immediately before the p. 138 page header, so p. 137; atomic component (2.4),
  mixture (2.5) and the "Jordan decomposition theorem" on p. 138; sec. V.3
  Lebesgue decomposition (3.9) and the three-part remark just before the
  p. 143 header, so p. 142. These match the body's locators.
- Durrett, PTE author version 5, 11 January 2019 (held:
  `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`):
  absolutely continuous, singular and discrete distribution functions and
  Example 1.2.7 on p. 13 (page header "1.2. DISTRIBUTIONS 13"); Example 1.2.9 on
  p. 14; Theorem A.4.7 (Lebesgue decomposition) on p. 469; definition of
  conditional expectation and its uniqueness on pp. 205-206. These match the
  body's locators.

## Existing treatments found

- `thm:p15-w02b-p15-008-null-modification`
  (`handbook/parts/p15/conditioning-independence-and-information-w02b-p15-008.tex`
  line 270) overlaps 157.6: its parts (ii) and (i) are items 1 and 2 of
  `thm:p15-w02b-p15-002-null-modification`, and its part (iii) is the
  Lebesgue-on-[0,1] case of item 5. It was not in the packet's existing list.
  The body now states the correspondence; the annex proof of items 1 and 2
  records it. Items 3, 4, 6 and the general trivial-sigma-algebra case of
  item 5 are not in the 008 theorem.
- No other file on the handbook tree states a three-part (atomic, absolutely
  continuous, continuous singular) decomposition of a real law
  (searched "continuous singular", "singular continuous", "purely atomic").

## Interpretation recorded

- Corollary `thm:p15-w02b-p15-002-regimes`, mixed-law clause: "the classes of
  items 1, 3 and 5" is read as the laws with mu = mu_d, mu = mu_ac and
  mu = mu_sc (the class to which item 5 assigns the Cantor law). The body
  sentence now names the three classes explicitly; the annex proves the
  clause for all three.

## Continuation

- All three named gaps have annex proofs written; `tools/waves.py unit-compile`
  reports ok (remaining overfull boxes in these files are under 3 pt, plus two
  in the bibliography entry for Feller that are not in these files).
- `tools/check.py --tree handbook` shows no finding in this packet's files.
- `tools/find_fused_spaces.py` reports no hit on the body, annex and symbol
  intake.
- Open: none of the packet's units had a recorded missing piece; the 143
  component ids were mapped to existing labelled environments by exact title
  and are reported in the return file as existing treatments not modified here.
