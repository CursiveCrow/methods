# w02b-p15-039: RAT2021 5.3 Ranking Theory (section 165.5), block 1

Packet `work/waves/w02b/packets/w02b-p15-039.json`; unit `ED26-BM-RAT2021-5-3`.
Label tag `p15-w02b-p15-039`. Date 4 October 2026.

## Source held and read this session

- `source/references/p15-rationality-5-3/ranking-2021-institutional.txt`
  (held; SHA256 2bf5eaeb...c9043), text of the KOPS publisher-layout PDF
  `ranking-2021-institutional.pdf` (held; SHA256 f8d025f6...b94c), printed
  pp. 337-346 of Knauff and Spohn (eds.), *The Handbook of Rationality*, MIT
  Press 2021, chapter 5.3. Whole chapter, notes 1-9 and references read.
- Provenance of the earlier treatment: `spec/research/p15-rationality-5-3-source-note.md`.

Locators used and seen in the held text this session: p. 337 (section 1:
belief simpliciter, truth vs action, doxastic logic static, belief revision
iterated-revision problem, ranking promises both); p. 338 (qualitative belief
sets cannot model change; entrenchment); p. 339 (law of conjunction
justification; cardinality presupposition; material vs conditional belief
"precisely ... non-vacuously"; reason explanation; Carnap incremental
confirmation); p. 340 (Definition 3; Bayes nets restatable, Spohn 1988,
Goldszmidt and Pearl 1996); p. 341 (ordinal AGM, no clear solution; Shackle,
Rescher, Cohen lack conditional ranks); p. 342 (Darwiche-Pearl etc.;
psychological belief revision extension; Da Silva Neves et al. System P plus
rational monotonicity; no direct ranking test); p. 344 n. 4 (Merin sections 1-4
transfer), n. 9 (|~ default entailment).

## Gaps closed in this block (host edits, not new files)

Per A9 the existing treatment in the editable hosts was extended instead of
writing a second chapter. Owned body/annex files were not created; temporary
wrappers that \input the hosts were created only to run the packet's
unit-compile and then removed. No driver insertion is needed.

- C02 (i) `sec:p15-w02b-p15-039-motivation` + example
  `def:p15-w02b-p15-039-same-order` (editorial; same order, different
  cardinal ranks, different iterated outcome).
- C02 (ii) law-of-conjunction paragraph at the head of "Conditionals and reasons".
- C02 (iii) + C04 (4-3) `sec:p15-w02b-p15-039-reasons`,
  `thm:p15-w02b-p15-039-reason-laws` (cross-sum criterion a+d<b+c, symmetry,
  negation, irrelevance, Delta_P = p1p4-p2p3, weak betweenness of tau(B) and
  failure of strict prior comparison, nontransitivity).
- C05 `thm:p15-w02b-p15-039-material` (kappa(A)=0 hypothesis; vacuous case).
- C04 (4-4) `thm:p15-w02b-p15-039-rational-monotony` + comparison paragraph.
- C04 (p16 4-2) `thm:p15-w02b-p15-039-chain` + comparison paragraph.
- C04 (p19 5-4) paragraph realizing `thm:p19-r54-two-revisions` orders as ranks.

Author arithmetic check (scratch, not a test suite): brute force over cell
ranks in {0,1,2,3,inf} confirmed the cross-sum criterion, symmetry and weak
betweenness; rational monotonicity confirmed over all rankings 0-2 of eight
worlds.

## Open items

- Hild and Spohn 2008, *Artificial Intelligence* 172, 1195-1218 (measurement
  axioms and ratio-scale uniqueness theorem) is not held; the cardinality
  justification remains reported by citation through the chapter (p. 340, n. 7).
- Da Silva Neves, Bonnefon and Raufaste 2002 not held: no task, sample or
  uncertainty reported beyond the chapter's description.
- Ranking analogues of the parental Markov condition and semigraphoid
  operations (Spohn 1988; Goldszmidt and Pearl 1996) are not held and not derived.

## Continuation

Block 1 finished the three assessed gaps (C02, C04, C05) in the hosts.
Remaining: Hild-Spohn 2008 measurement theorem (blocked_source). Overfull boxes
in the scoped build that predate this block (host lines for Definition 1.2,
Theorem 1.3 statement, Definition 1.9, Theorem 1.10) were not touched.
