# w02b-p02-031 — sections 21.1, 21.8 (block 1): BGG 1997 Sect. 2.1.2 remainder

Packet: `work/waves/w02b/packets/w02b-p02-031.json` (label_tag `p02-w02b-p02-031`).

## Files

- Body: `handbook/parts/p02/definitions-interpolation-and-decidable-fragments-w02b-p02-031.tex`
  (`sec:p02-w02b-p02-031-validity-finsat`). Insertion proposal (packet): `handbook/parts/p02/first-order-logic.tex`
  after `\input{parts/p02/definitions-interpolation-and-decidable-fragments-w02-p02-035}`. It depends on labels of
  `w02-p02-036` (body and annex), so the w02-p02-036 inputs must precede it in the driver.
- Annex: `handbook/annex/p02/definitions-interpolation-and-decidable-fragments-w02b-p02-031.tex`; insertion proposal
  `handbook/annex/p02.tex` after `\input{annex/p02/definitions-interpolation-and-decidable-fragments-w02-p02-035}`.
- Bib intake: no new keys. Symbol intake: 4 rows.

## Sources opened in this session and locators used

- BorgerGradelGurevich1997, held file
  `source/references/acq-r1-ACQ-2026-10-0056/borger-gradel-gurevich-1997-classical-decision-problem.pdf`
  (authors' TeX book file). Pages read this session (text layer and rendered PNG at 120-300 dpi): PDF 25-45
  (book pp. 18-38), and the text of Chapter 3, Sect. 3.2, Step 1 (book p. 115-116, where Exercise 2.1.31 is used).
  Locators used in text: Exercise 2.1.33 p. 36; Def. 2.1.38, Thm. 2.1.39 p. 37; Exercise 2.1.40 p. 38;
  "Sect. 2.1.2, pp. 36--38".
- Handbook authorities read: `restoration/inherited-08248-08305.tex` (validity enumerable, hooked label
  `thm:fol-validity-enumerable`; `thm:fol-validity-undecidable`), `inherited-08049-08080.tex` (many-one reductions),
  `inherited-08144-08186.tex` (recursion theorem, proof sketch only; parameter theorem not proved),
  `inherited-07851-08048.tex` (enumeration theorem), w02-p02-036 body and annex in full.

## Source readings recorded (differences from the assessment's wording)

- Remark after Ex. 2.1.31 (p. 36): the held file prints "due to the subformula Zxx -> Hxx, Büchi's reduction
  formulae also satisfy ∃yHyy" (existential, checked at 250 dpi). The assessment wrote "forall y Hyy". "Zxx" is
  presumably a misprint for Zx (Z is monadic). Not yet written in the text.
- Ex. 2.1.37 (p. 37, checked at 300 dpi): the classes are [∃∀∃∀] ∩ KROM ∩ HORN and [∀∃∃∀] ∩ KROM ∩ HORN "with
  only binary predicate symbols". The assessment described them as one class and its binary restriction.
- Ex. 2.1.32 (p. 36): the display of ≺_{K,M} uses u, while the Skolem normal form is ∀x∀y(...): u has to be read as
  the Skolem term x' (Thm. 2.1.15, p. 28: ψ_M = ∃u∀x∃v∀yα with Skolem form ∀x∀y STEP_M, terms 0 and x').
- Ex. 2.1.40(2) (p. 38), read for arbitrary recursive X, Y, is false: X = {≺_K}, Y = {∃x Kxx}, constant f is
  semi-conservative and no g exists. Written as `thm:p02-w02b-p02-031-semi-not-conservative`. For X = FO the item is
  the content of Thm. 2.1.39.

## Provenance of the proofs

- Ex. 2.1.33 is proved by a route different from the source's hint (Herbrand's theorem): recognizer of valid
  sentences + run sentence + path translation + renaming of w02-p02-036. The body says so.
- Ex. 2.1.40(1): pull-back of a separating set along f.

## Existing treatments found

All in the packet's list. Relevant and not listed: `handbook/parts/p04/degrees-and-priority.tex` 335-359 and
`degrees-and-priority-continuation.tex` 241-265 (productive/creative sets, Myhill; relevant to the effective
inseparability argument of Thm. 2.1.39, not yet used); `handbook/parts/p04/machines-effective-procedures-supplement.tex`
116-147 (`def:p04-shepherdson-sturgis-urm`, Shepherdson-Sturgis URM; no two-register universality theorem anywhere in
the handbook); `restoration/inherited-08144-08186.tex` (`thm:recursion-theorem`, sketch only).

## Block 2 (4 October 2026): item (f)

- Pages re-read this session from the held BGG file (text layer + PNG at 120-130 dpi): PDF 27-33 (book pp. 20-26,
  Church-Turing reduction formulae, START/NONSTOP/ORDER, Skolemization), PDF 34-45 (book pp. 27-38). Locators used:
  Thm. 2.1.39 and its proof outline pp. 37-38; effective inseparability definition p. 37; Ex. 2.1.40(2) p. 38.
- Written: Convention W_e (machine-code indices), Def. effective inseparability, Lemma index constructions (incl. a
  fixed-point item proved from items 1-2, not from the sketched recursion theorem), Lemma elementary properties
  (symmetry, implies recursive inseparability, supersets, transfer along computable maps), Lemma D_rej/D_acc and
  H_1/H_2 effectively inseparable, Thm Non-sat/Fin-sat effectively inseparable and c.e. (also for X under a
  semi-conservative f), embedding theorem, Thm 2.1.39, Cor. Ex. 2.1.40(2) for X = FO, example, limits warning.
- Proof dependencies outside this file and their standing: thm:universal-computation (proof sketch in the handbook;
  used in index-construction item 3 for step-by-step simulation), thm:ce-equivalent-forms, many-one preservation lemma
  of sec:universal-reductions-02, parts (a) and (b) of annex:p02-w02-p02-036-halting (code normalization and the
  write-the-code-first map w), thm:fol-validity-enumerable. thm:parameter (cited) and thm:recursion-theorem (sketch)
  are only mentioned in Relationships; the proofs do not use them.
- Notation: the source names the witness function f; renamed p (f is the semi-conservative reduction here). Recorded
  in the symbol intake.
- Source reference [485, Chap. V] in BGG's proof is not identified in this note (bibliography page not read); the text
  does not name it.

## Block 3 (4 October 2026): items (b), (d), (e)

- Pages re-read this session from the held BGG file (text layer, and PNG at 130-200 dpi): PDF 27-45 text;
  rendered PDF 34-36 (book pp. 27-29: Def. 2.1.14, Thm. 2.1.15, Cor. 2.1.16, Ex. 2.1.17-2.1.19), PDF 40-44
  (book pp. 33-37), and PDF 14-17 text (book pp. 7-10, Def. 1.3.1 prefix-vocabulary classes, p. 8).
- Written (body sec:p02-w02b-p02-031-register, annex items from annex:p02-w02b-p02-031-two-register-simulation
  on): Def. two-register machines; Def. Krom/Horn/prefix classes (Def. 2.1.14 p. 27, Def. 1.3.1 p. 8);
  Thm. TM -> two-register simulation with stop-state record, emptied registers and unbounded registers for
  non-halting runs (proved through a four-register program: base-s tape halves, MOVE/ADD/DIVMOD loops, prime-power
  coding 2^L 3^R 5^A 7^C with a step counter in the exponent of 7); Def. formulas alpha_{M,m}, beta_{M,prec,m},
  beta^+_{M,prec,m}, psi_{M,prec}; Thm. reduction property (both prefixes); Cor. Ex. 2.1.32; Thm. logic machine
  M_L (from index constructions items 1 and 3; item 3 extended with "never halts outside W_i cup W_j", statement
  and proof); Cor. Ex. 2.1.34; Cor. Ex. 2.1.37 (both classes); example with three machines; warning incl. a
  never-halting machine with bounded registers whose formula has a 2-element model.
- Source readings recorded: (1) in Ex. 2.1.32 the display of prec_{K,M} uses u inside a Skolem form
  forall x forall y; read as the successor term x' (written so in the text, with the reason). (2) For m(psi) >= 2 the
  start atom (0,m(psi),0) needs the term 0^(m); a prenex exists-forall-exists-forall sentence has no such term,
  so the text derives the atom with auxiliary binary symbols A_0..A_m (Krom-Horn clauses). (3) For the
  forall-exists-exists-forall class the zero is the Skolem term x^+, as in the hint of Ex. 2.1.17 (p. 29); every
  conjunct of the matrix contains either no u or neither x nor v, which is what makes one matrix serve both.
  (4) The source's sharpened stop condition (p. 35) appears as property 4 of the simulation theorem (unbounded
  registers), and the warning shows it is needed.
- Patch request: work/waves/w02b/patches/w02b-p02-031.json replaces w02-p02-036 body lines 691-695 ("neither of
  those results is proved") by pointers to thm:p02-w02b-p02-031-ex-2-1-34 and -ex-2-1-37.
- Universality of two-register machines: the source cites [393, 469] (p. 28); not identified or opened; the text
  names no reference for it and proves it.

## Continuation

State at return of block 3 (4 October 2026). Written in blocks 1-3: Ex. 2.1.33, Def. 2.1.38, Thm. 2.1.39,
Ex. 2.1.40, items (b), (d), (e) as above. Unit compile ok (29 overfull boxes, mostly pre-existing annex
displays); fused-space check clean; check.py --tree shows no finding in these files.

Not yet written:

1. (a) Ex. 2.1.31: rho_{M,prec} as exists x Zx and forall x exists u forall y beta, beta with variables x,u,y only
   and binary symbols H, T_0, K only, plus the following Remark (source p. 36 prints exists y Hyy and the subformula
   "Zxx -> Hxx"). Design notes: head moves (t,c) -> (t+1,c+1) need a two-step transposition through pairs above
   the diagonal ((t,c) -> (c,t+1) -> (t+1,c+1); a premise on (u,y) gives the predecessor direction for left
   moves); the open point is persistence of non-head cells, which needs "y is not the head cell at time x" with
   H as the only head relation and no fourth variable. Buechi 1962 (BGG [64]) is not held.
