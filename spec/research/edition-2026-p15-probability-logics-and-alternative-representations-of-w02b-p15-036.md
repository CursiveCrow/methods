# w02b-p15-036: section 165.10 (comparisons with classical probability, qualitative belief and decision criteria)

Packet: `work/waves/w02b/packets/w02b-p15-036.json`, label tag
`p15-w02b-p15-036`, blocks 1 and 2.

## Ownership finding

Every component in this packet belongs to a unit listed in the packet's
`readonly_units`:

- `ED26-BM-RAT2021-4-7` (C01-C05) -> owner `w02b-p15-032`.
- `ED26-METHOD-imprecise-probability` (C01-C05) -> owner `w02b-p15-034`.

This packet therefore owns no component it may write. The assessment gaps
relayed to this block (MP-0, C03 partition updating, C05 decision comparison)
are gaps of the owner's unit.

Evidence that the owner is writing them in this same wave: at 2026-10-04
17:36 the owner's body file
`handbook/parts/p15/probability-logics-and-alternative-representations-of-w02b-p15-034.tex`
already holds `sec:p15-w02b-p15-034-partition-updates` (C03: partition,
joint coherence, conglomerability, counterexample, Williams coherence) and
`sec:p15-w02b-p15-034-independence-decision` with
`thm:p15-w02b-p15-034-independence-models` and
`thm:p15-w02b-p15-034-independence-decision` (C05: agreement bet against a
sure payment, independence judgements compared, the acts left unranked
under maximality). A second treatment here would duplicate it.

## Source status (MP-0)

- Walley, Imprecise Probabilities, Wiley StatsRef, 29 September 2014,
  DOI 10.1002/9781118445112.stat01581: no entry in
  `spec/coverage/edition-2026/held-sources.json`, no file under
  `source/references/p15-imprecise-probability/` (held there: Miranda survey,
  De Bock and de Cooman 2015), packet `held_paths: []`, and no entry in
  `work/waves/w02b/acquisition-needs.json`.
- RAT2021 4.7 held path: `source/references/p15-rationality-4-7/dubois-prade-2021-publisher.pdf`
  (owner `w02b-p15-032`).

## What was written (block 1)

No handbook file. A chapter for 165.10 consisting only of pointers to the
owners' labels would be a stub, so none was created. Consequence:
`tools/waves.py unit-compile` on this packet fails with "File
parts/p15/probability-logics-and-alternative-representations-of-w02b-p15-036.tex
not found".

## Block 2 (2026-10-04)

The block-1 decision not to write any file left the unit compile failing
(G10). Section 165.10 itself ("Comparisons with classical probability,
qualitative belief and decision criteria") is this packet's section, so a
chapter for it was written whose content is not a component of either
readonly unit and is not already in the handbook (searched: E-admissib,
interval dominance, Gamma-maximin, maximality, robust dominance, Wald,
vacuous; found only the two-act comparisons in 032/r47/P17 and Hill's
three-act menu in thm:p17-rat84-criteria, all cross-referenced, none
duplicated).

Files:

- `handbook/parts/p15/probability-logics-and-alternative-representations-of-w02b-p15-036.tex`
  (chapter `sec:p15-w02b-p15-036`): standing assumptions; five choice rules
  (alpha-maxmin incl. Gamma-maximin, interval dominance, maximality,
  E-admissibility); `thm:...-inclusions` (nesting, two-act coincidence,
  infinite-menu emptiness); `thm:...-precise` (all rules coincide iff the
  lower prevision is linear); `def:...-menu`/`thm:...-menu` (one four-act
  menu making every inclusion strict; strict-part-of-unanimity contrast);
  `thm:...-accepted` (lower probability one iff decisions may ignore the
  complement); `thm:...-threshold` (necessity-measure acceptance at 9/10
  does not license deciding as if); `thm:...-vacuous` (vacuous model, worst
  / best outcome criteria); warning on limits; relationships.
- `handbook/annex/p15/probability-logics-and-alternative-representations-of-w02b-p15-036.tex`:
  full proofs of all six results.
- Bib intake: no new keys. Symbol intake: 6 rows.

Sources opened this session and locators used:
- Miranda survey (`source/references/p15-imprecise-probability/miranda-survey-lirmm.pdf`):
  §6 p. 37 (names E-admissibility, interval dominance, Gamma-maximinity,
  maximality; no definitions; refers to Troffaes [65], not held); §7 p. 38
  (challenges 3, linear utility; 8, choice of criterion).
- Hill 2021 (`source/references/p17-rationality-8-4/hill-2021-extracted.txt`):
  Sec. 2, p. 497, eq. (2) alpha-maximin (alpha=1 maximin), eq. (3)
  unanimity, called maximality in statistics (Walley 1991), Levi's
  E-admissibility.
- Dubois and Prade 2021 (`source/references/p15-rationality-4-7/dubois-prade-2021-publisher.pdf`):
  p. 308, qualitative counterparts of expected utility extend Wald's
  pessimistic and optimistic criteria (attribution only).

All theorems and examples are constructed for this chapter (stated in the
reader text).

Guard G1 (spec/research files of w02b-p01-014 and w02b-p02-036): these are
untracked files of those packets; this packet did not create or modify
them and A8 forbids touching them. The guard attributes tree-wide
untracked files to this packet; the lead must scope G1 per packet.

## Continuation

Remaining for the lead: (1) route the new chapter (insert
`\input{parts/p15/probability-logics-and-alternative-representations-of-w02b-p15-036}`
after `parts/p15/rationality-5-3` in handbook/parts/p15.tex, and the annex
input after `annex/p15/rationality-5-3` in handbook/annex/p15.tex);
(2) MP-0 stays blocked_source: Walley, Imprecise Probabilities, Wiley
StatsRef 29 September 2014, DOI 10.1002/9781118445112.stat01581, complete
article, not held; (3) all ten components belong to readonly units owned by
w02b-p15-032 and w02b-p15-034. Optional source that would let the
definitions be matched to a published presentation: Troffaes 2007,
"Decision making under uncertainty using imprecise probabilities" (Miranda
ref. [65]), not held.
