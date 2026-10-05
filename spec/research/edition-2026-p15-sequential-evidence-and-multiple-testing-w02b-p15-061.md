# P15 170.5–170.6: repeated fixed-sample tests on accumulating data (w02b-p15-061)

Date: 4 October 2026. Packet `work/waves/w02b/packets/w02b-p15-061.json`,
label tag `p15-w02b-p15-061`, toc tag `%% toc: P15 170 170.5,170.6`.

## Assigned gap

170.6: the repeated fixed-sample test on accumulating (overlapping) data.
The existing treatment `thm:p15-se-repeated-fixed`
(`handbook/parts/p15/sequential-evidence.tex` 538–554, annex 448–463)
covers only independent looks and says the overlapping-sample case needs its
own calculation. This packet supplies that calculation in its own files.

## Existing treatments read (linked, not repeated)

- `thm:p15-se-repeated-fixed` and its annex item: independent looks,
  `1-(1-alpha)^M`. Linked as the independent-look comparison.
- `thm:p15-se-errors`: SPRT coupled error inequalities (upper-exit error at
  most `1/A` style bound). Linked as the valid sequential comparison.
- `thm:p15-clt-oscillation` (`central-limit-theorems.tex` 156–167):
  `limsup S_n/sqrt n = +infinity` along all `n`. Found during search; not
  listed in the packet's `existing`. The new unbounded-inspection theorem is
  the subsequence (arbitrary fixed look schedule) version and is proved
  directly; the all-`n` case is the schedule `n_k = k`.
- `thm:p15-kolmogorov-tail-zero-one` (`limsup-events-and-zero-one-laws.tex`
  181) and `thm:p15-clt-iid` (`central-limit-theorems.tex` 76): used as
  prerequisites by `\cref`.
- `sec:p15-multiple-testing`, `sec:p15-optional-stopping-and-random-walks`:
  related chapters, cross-referenced.
- No existing treatment of Gaussian cumulative-look error, its recursion or
  a calibrated constant boundary was found (grep for repeated significance,
  Armitage, Pocock, group sequential, iterated logarithm in parts/annex).

## Sources

Held and opened this session:
`source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`
(SHA-256 `aeac36cb…910886`), bib key `DurrettPTEAuthor2019`.
Locators seen (printed page = PDF page minus 8):
- Theorem 2.1.20 (sum of independent normals), p. 52.
- Example 2.5.2 (tail events built from `S_n/c_n`) and Theorem 2.5.3
  (Kolmogorov's 0-1 law), p. 81.
- Theorem 3.4.1 (i.i.d. central limit theorem), p. 144.

Not held: Armitage, McPherson and Rowe (1969) and Pocock (1977) on repeated
significance tests. No source-specific presentation or attribution to them is
written; the chapter's mathematics is self-contained and proved in the annex.
Numerical values are computed here (method below), not quoted.

## Numerical method (provenance for the worked example)

Script: Gauss–Legendre quadrature (1000/2000/4000 nodes) of the backward
recursion on `(-12, c]`, cross-checked with SciPy 1.17.1
`multivariate_normal.cdf` (Genz) and, for two looks, mpmath 30-digit
quadrature of the one-dimensional integral. One-sided `alpha=.05`,
`c=1.6448536270`:
K=1 .050000, 2 .080076 (exact quad .0800755257), 3 .101054, 4 .117064,
5 .129970, 10 .171756, 20 .214491 (Genz .214488–.214490), 50 .270119.
Independent looks: .0975, .142625, .185494, .226219, .401263, .641514,
.923055. Two-sided `c=1.9599639845`: K=2 .083118, 5 .141689, 10 .193357.
Calibrated constant one-sided thresholds: `c_2=1.875423`, `c_5=2.121715`.

## Ownership note

All three units in the packet (`ED26-METHOD-sequential-evidence`,
`ED26-P15-CH-robust-hypothesis-testing`, `ED26-P15-CH-robust-sequential-endpoints`)
are listed in `readonly_units` with other owner packets. The computed task
for this block nevertheless directs the overlapping-look calculation for
170.6 to this packet; it is written only in this packet's owned files and
does not edit `sequential-evidence.tex`. 170.5 components were not written.

## Continuation

- Body `handbook/parts/p15/sequential-evidence-and-multiple-testing-w02b-p15-061.tex`
  1-358; annex same slug 16-454: procedure definition, look-dependence
  lemma, exact finite-look error (integral, recursion, two-look formula,
  strict excess, skipping bound), association lemma for monotone functions
  of independent variables, comparison with independent looks (general
  product inequality; strict in the Gaussian model; two-sided bound on
  alpha_K), unbounded inspection (any i.i.d. finite positive variance, any
  infinite fixed schedule), two-sided corollary, calibrated constant
  threshold, method, worked example, warning, relationships and sources.
- Latest block added annex proofs annex:p15-w02b-p15-061-association
  (139-231) and annex:p15-w02b-p15-061-versus-independent (233-344).
  Prerequisites cited by label: thm:p15-independent-product-law,
  thm:p15-expectation-law-integral, thm:p15-signed-integral-laws,
  thm:p15-fubini, thm:p15-tonelli, thm:p15-product-sections,
  thm:p15-finite-product-measures, thm:p15-independent-blocks,
  thm:p15-independent-expectations, thm:p15-nonnegative-integral-laws.
  Two body titles shortened to remove overfull headings.
  Unit compile ok with 0 overfull boxes.
- Patch request `work/waves/w02b/patches/w02b-p15-061.json`: routing
  sentences in `sequential-evidence.tex` and its annex.
- Open: historical repeated-significance sources not held. 170.5 robust
  components untouched (owned by w02b-p15-058 and w02b-p15-060). Driver
  insertion is a lead action.
- Block r3-b2 (4 October 2026): the G1 hard findings name
  `spec/research/edition-2026-p01-symbol-registry-w02b-p01-014{.md,-return.json}`
  and `spec/research/edition-2026-p02-fol-metatheorem-table-and-nd-cpl-sheet-w02b-p02-036{.md,-return.json}`.
  These are the notes of packets w02b-p01-014 and w02b-p02-036 (mtimes
  22:05 and 18:23), not written by this packet; both packets have an empty
  `owned_files` list, so the snapshot's `wave_packet_paths` cannot attribute
  them and verify reports them as hard G1 for every packet. Not modified
  here (other agents' files). Lead action: add each note and return file to
  its packet's owned set (and the snapshot's `wave_packet_paths`), then
  re-run verify. No content change to this packet's files in this block;
  unit compile ok (0 overfull), check.py tree filtered: no findings,
  find_fused_spaces: no hits.
