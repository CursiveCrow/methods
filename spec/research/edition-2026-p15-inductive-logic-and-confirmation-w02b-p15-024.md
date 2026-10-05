# w02b-p15-024 research note (P15, sections 164.1, 164.11)

Packet: work/waves/w02b/packets/w02b-p15-024.json. Label tag `p15-w02b-p15-024`.

## Sources opened in this session

- source/references/p15-rationality-4-3/merin-2021-publisher.pdf (Merin 2021, ch. 4.3, printed pp. 265-275, all twenty notes and references). Text extracted with PyMuPDF; locators read: p. 266 (Def. 4 "Carnap 1950, modified"; Lemma 1), p. 268 (accounting-convention analogy; A1/A3 question; Def. 6; old evidence), p. 269 (Def. 8; Eells and Fitelson 2002; Crupi and Tentori 2016), p. 270 (provenance of D, Q, L, QL, LL, KO, Z; Defs 9; KO, Z formulas; axioms POP-D, LIK-D, MCIE), p. 271 (MDHD; Theorem 7; the status argument for the four axioms; Steel 2003; Good 1960, Heckerman 1988; Lemma 3; Theorems 8-9; Lemma 4; raven paradox), p. 272 (amount symmetry; Carnap's R_C; Eells and Fitelson 2002 on inversion), p. 273 (Theorem 10; Good 1983 quasi-utility; psychology), p. 274 (conclusion; notes 1-20), p. 275 (references).
- source/references/p15-rationality-4-3/crupi-tentori-2016-confirmation-theory.pdf (CT2016, pp. 650-665). Page images rendered for pp. 654, 655, 656, 657, 658, 659 because the text layer drops lining digits. Read: p. 654 (F) formality and n. 5 (first definitions); p. 655 (r0-r4 variants; axioms C1-C4 with labels; n. 7 label provenance incl. Heckerman 1988 pp. 18-19, Hacking 1965); p. 656 (Theorem 1; n. 9 Carnap, Mortimer, Nozick measures depart from C1; Carnap's implies C2); p. 657 (card example; pluralism); p. 658 (z; C5 partial inconsistency; C6 confirmation complementarity); p. 659 (Theorem 2: F, C1, C5, C6 iff relative distance measure; proof attributed to Crupi and Tentori 2013).
- source/references/p15-carnap-induction/carnap-1950-relevance-346-427.txt and carnap-1950-archive-ocr.txt, with PDF page image for printed p. 412. Read: pp. 346-348 (chapter summary; D65-1 incl. D65-1d(2)); p. 357 (relevance quotient, Keynes pp. 150-55 coefficient of influence from Johnson's notes; quotient or difference as the two simple ways); p. 361-362 (additivity; D67-1 relevance measure r); pp. 409-412 (sec. 74; D74-1; T74-1(i)).
- source/references/p15-hempel-confirmation/hempel-1945-part-i.reading.txt, printed p. 21 n. 2 (continuing to the foot of p. 21): Hosiasson-Lindenbaum's numerical assumption and the co-ordinate language objection.

## Dependent-source set (fixed before authoring)

Formal claims of Merin's chapter that need proof: Theorems 1-10, Lemmas 1-4, the axiom-status inferences on p. 271. Fixed dependent set: CrupiChaterTentori2013Axioms and CrupiTentori2016Confirmation (Theorem 7), plus direct proofs. Additional works named by Merin as carrying claims: Steel 2003 (Erkenntnis 58, 213-227), Crupi and Tentori 2013 (J. Applied Logic 11, 364-372), Festa and Cevolani 2016 (Phil. Sci. 84, 56-81), Merin 1999 (CSLI, Logic, Language and Computation 2, 179-221). None of these four is held. The Z uniqueness result is stated in held CT2016 p. 659 Theorem 2; this packet proves it independently in the annex. Steel's enumerative-induction argument, Festa's Matthew properties and Merin 1999 function-word semantics are reported only as Merin's attributions and recorded as blocked_source.

## Decisions

- New chapter rather than edits to rationality-4-3.tex (readonly host). It links the existing labels and supplies: axiom status argument (p. 271), history/provenance (p. 270, 272, 273), notes 1, 5, 8, 11, 12, 13, 14, 17, 20, the A1/A3 question and the accounting analogy (p. 268), the Carnap comparison and Hempel's objection, and the Z characterization.
- Patch request (work/waves/w02b/patches/w02b-p15-024.json) replaces the sentence at rationality-4-3.tex lines 9-10 that claims the chapter follows all twenty notes, pointing to the new chapter.
- Historical priority claims (MacColl, Johnson, Peirce/Turing/Good, Good 1950/1960/1983, Kemeny-Oppenheim 1952, Heckerman 1988, Eells-Fitelson 2002) are written as attributions by Merin and, where CT2016 or Carnap 1950 differ or corroborate, with their locators. The primary works are not held.

## Continuation

- Written: body handbook/parts/p15/inductive-logic-and-confirmation-w02b-p15-024.tex (521 lines); annex handbook/annex/p15/inductive-logic-and-confirmation-w02b-p15-024.tex (317 lines); symbol intake; patch file work/waves/w02b/patches/w02b-p15-024.json; return JSON.
- Checks run: unit-compile ok (10 paragraph-level overfull boxes, largest 12.4pt); find_fused_spaces no hits; check.py --tree shows no finding for these files.
- C01-C04 written; C05 partial (Steel 2003 argument only). Systematic-power and finite-abduction components are closed in the packet and were not touched.
- Next run: if Steel 2003 is acquired, reconstruct its POP-D/enumerative-induction argument in sec:p15-w02b-p15-024-axiom-case and update def:p15-w02b-p15-024-dependents.
- Remaining blocked: Steel 2003 argument; Festa-Cevolani 2016 Matthew properties; Merin 1999 function-word semantics; Woods 2002 (SRC-060, ch. 3, pp. 105-169) for section 164.1 induction presentation.

### Run of 4 October 2026

- G1 guard: the four flagged files belong to packets w02b-p01-014 and w02b-p02-036 (untracked, written by those agents). This packet never touched them; left as they are (A8). Explained in the return JSON `guard_note`.
- Added sec:p15-w02b-p15-024-direction and thm:p15-w02b-p15-024-direction (Merin's Lemma 4, p. 271, read in the held PDF this run): unique sound ranking = posterior ranking; Q amount-symmetric so reversed Q gives it; any POP-D+LIK-D measure also; D counterexample with an explicit eight-atom joint model. Proof annex:p15-w02b-p15-024-direction.
- Extended def:p15-w02b-p15-024-dependents: Lemma 4 standing; the p. 273 empirical pointers (Tentori-Crupi-Russo 2013, Cevolani-Crupi 2015, Wilson-Sperber 2004, Sperber-Cara-Girotto 1995, Skovgaard-Olsen-Singmann-Klauer 2016a,b) bounded as research leads with no reported task, population, design, measure or uncertainty. Locator p. 273 verified; notes 18-19 checked and not cited for these.
- Checks: unit-compile ok (11 overfull); find_fused_spaces no hits; check.py --tree no finding for these files.
- Still open: C05 Steel 2003 (not held); SRC-060 Woods 2002 C001-C003 (not held); patch and \input insertion are lead actions.

### Run of 4 October 2026 (second)

- Gap closed per assessment of C05: re-read held Merin PDF pp. 265-275 this run (PyMuPDF text; PDF page index 0-10 = printed pp. 265-275). Verified locators: p. 267 (Reichenbach 1956 Theorem 6, Pearl 1988 thesis and search test, Carnap 1950 ch. 6, Pearl ch. 7.1), p. 268 (Glymour 1980; Jeffrey 2004; Earman 1992; Fitelson-Hartmann 2015; Hajek-Joyce 2008; term "relevance": Keynes, Carnap, Jeffrey), p. 269 (Eells-Fitelson 2002), p. 271 (raven: Hosiasson-Lindenbaum 1940, Earman 1992, Hajek-Joyce 2008, Crupi 2015), p. 272 (Hosiasson p. 138), p. 273 (note 18 and 19 markers; Savage; Peterson ch. 8.2), p. 274 (conclusion with Hajek-Joyce; notes 1-20), p. 275 (reference list, 33 entries in total with Carnap on p. 274).
- Added sec:p15-w02b-p15-024-cited-routes (old-evidence routes, common cause / Pearl, pluralism, notes 18-19) with thm:p15-w02b-p15-024-near-certain and thm:p15-w02b-p15-024-search, annex proofs; rewrote def:p15-w02b-p15-024-dependents as the full finite set (33 references + 7 same-handbook chapters) with standings; updated claim-kinds and intro; corrected the Carnap ch. 6 paradoxical-conjunction pointer to thm:p15-carnap-relevance-sign-cases.
- Updated patch text (rationality-4-3 lines 9-10) to name notes 17-20 and the new sections.
- None of Glymour 1980, Jeffrey 2004, Earman 1992, Fitelson-Hartmann 2015, Hajek-Joyce 2008, Pearl 1988, Reichenbach 1956, Kahneman 2011, Huber 2007, Crupi 2015 is in held-sources.json (checked); written only as Merin's attributions.
- Checks: unit-compile ok (15 overfull, max 14.0pt); find_fused_spaces no hits; check.py --tree no finding for these files.
- Still open: C05 reconstructions of non-held works (Steel 2003 etc.); SRC-060 Woods 2002; lead insertion and patch.

### Run of 4 October 2026 (third)

- Re-read held Merin PDF this run (PyMuPDF): printed pp. 266, 267, 270, 271, 273, 274. Verified: note 4 marker on p. 267 at Pearl's thesis, note 4 text p. 274; Lemma 3 and the KO remark p. 271 (printed LL identity has subscript L on its first summand); MDHD embarrassment and "L and Q do not face this problem" p. 271; Theorem 10 p. 273; conclusion's "mutual extreme negativity of disjuncts" p. 274; note 7 tanh form p. 274 (log taken of R_LL in print; correct form tanh(LL/2)); Def. 4 exneg p. 266; Def. 9 ordinal equivalence p. 270.
- C02 (a): body sec:p15-w02b-p15-024-common-cause, note 4 paragraph and thm:p15-w02b-p15-024-diagnostic-additivity (L product / LL sum for screened symptoms; positivity of the conjunction; paradoxical symptomatology refutes screening). Annex proof added.
- C02 (b): new subsection sec:p15-w02b-p15-024-disjuncts with thm:p15-w02b-p15-024-exneg-disjuncts (exneg symmetric; P(AB)=0 iff mutual exneg when both disjuncts have positive probability; null-disjunct case gives trivial mixture). Annex proof added.
- C05 (a): new subsection sec:p15-w02b-p15-024-lemma3 with thm:p15-w02b-p15-024-ko-transform (KO composition law, counterexample 1/2,1/2 -> 4/5, Cauchy characterization: only c ln keeps sums, only x^c keeps products). C05 (b): thm:p15-w02b-p15-024-mdhd-ratios (general D/Q/L values; cards: L = 0 and 25/27). Annex proofs added. axiom-case items for MCIE and MDHD now point to them.
- Symbol intake: rows for a_i,b_i,l_i,k_i; f,c,g; G,g,h.
- Checks: unit-compile ok (18 overfull, max 24.7pt annexitem header); find_fused_spaces no hits; check.py --tree no finding for owned files.
- G1: the four flagged spec/research files belong to w02b-p01-014 and w02b-p02-036; untouched (A8).
- Still open: C04 route (lead inserts \input lines; blocked_policy); C05 non-held works (Steel 2003 etc.); SRC-060 Woods 2002.
