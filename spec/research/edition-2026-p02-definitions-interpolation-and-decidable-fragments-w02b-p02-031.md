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

## Continuation

State at return of block 1 (4 October 2026). Written: Ex. 2.1.33 (theorem, example, limits warning, annex proof),
Def. 2.1.38, Ex. 2.1.40(1) with proof, the counterexample to the literal Ex. 2.1.40(2). Unit compile ok (7 overfull
boxes); fused-space check clean; check.py --tree shows no finding in these files.

Not yet written (next block, in this order):

1. (a) Ex. 2.1.31: needs a relational Büchi-type encoding of a binary-alphabet Turing machine in
   ∃xZx ∧ ∀x∃u∀yβ with only H, T_0, K binary. Obstacle found: a head move relates (t,c) to (t+1,c±1), while β only
   gives one successor (u of x); a construction (e.g. a 45-degree re-indexing of the space-time diagram or a machine
   model whose moves avoid the diagonal) must be designed and proved; Büchi 1962 ([64]) is not held. Then the Remark
   (∃yHyy).
2. Two-register machine universality with halting-state preservation (needed by (b), (d), (e)): not in the handbook;
   must be proved in the annex (TM -> counter machines -> two registers via 2^a 3^b 5^c 7^d coding), together with the
   "logic machine" of Cor. 2.1.16 refined to halt in (1,0,0) on Non-sat and (2,0,0) on Fin-sat.
3. (b) Ex. 2.1.32 with ≺_{K,M} as displayed (u read as x'); (d) g(ψ) and Ex. 2.1.34; (e) Ex. 2.1.37 for both prefix
   classes (relational prenex forms of the Skolem normal forms; Krom/Horn clause check; ∃∀∃∀ via u:=0, v:=x';
   ∀∃∃∀ variant must be designed).
4. (f) Thm. 2.1.39: effective inseparability (definition, H_1/H_2 effectively inseparable, transfer along reductions)
   and the embedding theorem (disjoint c.e. P_1, P_2; effectively inseparable c.e. R_1, R_2 => recursive g with
   P_i = g^{-1}(R_i)). Needs a parameter (s-m-n) theorem and a double recursion theorem for the handbook's machine
   model; the handbook has the recursion theorem only as a sketch. An alternative self-referential proof (machine
   searching for unsatisfiability/finite models of ψ and of f(θ_ψ)) also needs the recursion theorem.
