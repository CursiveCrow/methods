# w02b-p02-034 (P2, chapter 23, sections 23.1-23.4): research note

## Existing treatment found (A9)

- Packet `existing` list: higher-order supplement (body and annex), registry/calculi/sol.tex,
  restoration intervals 12262-12673, annex:p2.hol.8, sec:p02-sol-matched-calculus,
  sec:second-order-logic-01 references in the 040 and 041 files.
- Not listed but found and linked: the Church 1940 presentation
  `sec:p02-w02-p02-040-church` (handbook/parts/p02/second-and-higher-order-logic-w02-p02-040.tex
  lines 1-1215; annex of the same name), which already gives Church's symbols, formation rules,
  abbreviations, rules I-VI, axioms, theorems 12-43, VII and VIII; the predecessor warning
  `def:p02-w02-p02-041-church-predecessor` (041 body lines 617-632); the footnote 12 paragraph
  (040 body lines 477-487).  The new Church section extends these and does not restate them.
- Two versions of `thm:p04-ce-sigma-one` exist:
  - on the current route: handbook/restoration/inherited-08710-08876.tex line 959 (input by
    handbook/parts/p04.tex line 65 through restoration/scope-SRC-08710-08876), marked
    "Status: complete proof", proved through thm:enumeration and thm:bounded-verification, with
    the history coding written out (def:history-coding, lem:p04-tagged-history-extraction, ...);
  - off route: handbook/parts/p04/decision-problems-and-arithmetical-hierarchy.tex line 330,
    `sketched=annex:p04-hierarchy.8`; its annex item (handbook/annex/p04/decision-problems-and-arithmetical-hierarchy.tex
    line 132) carries the sketch note that history coding inside Comp is omitted.  Neither file is
    input by a driver, so `\cref{annex:p04-hierarchy.8}` is a dangling reference in the tree
    (tools/check.py reports dangling-ref).

## What this packet wrote (this session)

- Body, section 1 (lines 1-338): replaced the four passages the assessment named (old lines
  15-17, 33-37 region, 196-200, 209-214, 258-261, 275-278) and added
  `def:p02-w02b-p02-034-boundary` (proofboundary, lines 40-72).  The boundary states that the 040
  annex proof of clause 3 cites thm:p04-ce-sigma-one for the step "TA c.e. implies TA in
  Sigma^0_1", that the corollary after thm:tarski-undefinability uses the same step unreferenced,
  that both are exactly as complete as the proof of thm:p04-ce-sigma-one, that this proof needs
  the history coding inside Comp, that an outline omitting that coding leaves an unproved
  dependency, and that clause 3 is proved in full without thm:p04-ce-sigma-one only by
  thm:p02-w02b-p02-034-step ... thm:p02-w02b-p02-034-ta-not-ce.
- Why the boundary is phrased conditionally: the requested wording ("thm:p04-ce-sigma-one is
  proved only in outline, annex:p04-hierarchy.8") is true of the off-route P4 rewrite and false of
  the on-route restoration text, which claims a complete proof with history coding; and
  `\cref{annex:p04-hierarchy.8}` is a dangling reference while the P4 rewrite is unrouted.  When
  the lead routes the P4 rewrite, the exact sentence to add at the end of the first paragraph of
  def:p02-w02b-p02-034-boundary is:
  "In this handbook \cref{thm:p04-ce-sigma-one} is proved only in outline
  (\cref{annex:p04-hierarchy.8}), with the history coding inside \(\mathsf{Comp}\) omitted, so the
  proof of clause~3 in \cref{annex:p02-w02-p02-040-no-effective-calculus} rests on that outline."
- Body, section 2 (lines 340-522): `sec:p02-w02b-p02-034-church-conventions` with
  def:p02-w02b-p02-034-autonymy (Church's autonymy convention, S2 pp. 57-58),
  def:p02-w02b-p02-034-autonymy-example, def:p02-w02b-p02-034-induction-proof ("proof by
  induction on the variable", S6 p. 64), the expansion recipe through the 040 proof of VIII,
  def:p02-w02b-p02-034-induction-example (worked derivation that every natural number of type
  alpha' is 0 or a successor, with every rule proviso checked), def:p02-w02b-p02-034-church-open.
- Annex: `\Z` (source-only macro, fatal outside restoration scope) replaced by `\mathbb Z` at
  line 31; no other annex change.
- Symbol intake: two example-local rows (\mathbf C_o, \mathbf G).

## Sources opened in this session

- source/references/acq-r1-ACQ-2026-10-0080/church-1940-simple-theory-of-types.pdf (held;
  JSTOR scan pp. 56-68), text layer via pdftotext.  Locators verified: S2 pp. 57-58 (bold
  syntactic variables; formal symbols name themselves; juxtaposition denotes juxtaposition),
  S2 p. 59 (predecessor remark), S6 p. 64 (VIII; definition of proof by induction on x_alpha'),
  S6 p. 66 n. 12 (Church's and Turing's claims; open problem).

## Open items (not closed in this session)

- Predecessor non-definability (S2 p. 59): the source gives one sentence and does not fix the
  formal sense of "defined"; no proof written.
- Footnote 12 (S6 p. 66): Church's claim (30^iota and 30^iota' replace Axiom 8 given 1-6) and
  Turing's claim (30^iota alone given 1-7 and 9) are reported without proof in the source; no
  derivation written.
- Henkin 1950, Andrews 2002 (2nd ed.), Shapiro 1991: not held (ACQ-2026-10-0187, -0008, -0503).
- Lead-owned: redirect the 040 clause-3 proof; write out the annex:p2.hol.5 converse induction;
  route the 034 files; decide which version of thm:p04-ce-sigma-one is routed.
- Pre-existing overfull displays of Init and Halt (body lines about 136, 154, 168).

## Continuation

- State after this session: boundary statement (conditional form) and Church conventions section
  written; unit-compile ok; check.py shows no finding in the 034 files.
- Next: if the P4 rewrite is routed, add the sentence above to def:p02-w02b-p02-034-boundary
  and restore the unconditional "outline-only" wording in the warning item 2 and the remark after
  thm:p02-w02b-p02-034-ce-sigma-one.  Then break the long Init/Halt displays.
