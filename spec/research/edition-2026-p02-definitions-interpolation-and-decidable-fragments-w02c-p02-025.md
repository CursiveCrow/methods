# Edition 2026, P2 section 21.8: Büchi's prefix form of the refined reduction formula (packet w02ca-p02-025)

## Duty

MP-0(a) of 21.8: supply BGG 1997 Sect. 2.1.2 Exercise 2.1.31 (book pp. 35-36; PDF pp. 42-43) with a written proof, and the Remark after it.

## Source reading (held file opened this session)

- File: source/references/acq-r1-ACQ-2026-10-0056/borger-gradel-gurevich-1997-classical-decision-problem.pdf (authors' TeX file, held-sources.json entry BorgerGradelGurevich1997).
- PDF p. 42 = book p. 35: end of proof of Thm 2.1.30; display of prec_{K,M} = forall x exists u forall y (not Kxx and (Hyx -> Kxu) and (Kyx -> Kyu)); start of Exercise 2.1.31 ("[64] Show that rho_{M,prec} can be chosen as formula of the form exists x Zx and forall x exists u forall y beta ...").
- PDF p. 43 = book p. 36: rest of the exercise (variables x, u, y only; binary H, T_0, K; finitely many monadic; hint: universality of binary-alphabet TMs, Zx as x = 0, START as Zy -> START[0/y]); Remark ("due to the subformula Zxx -> Hxx, Büchi's reduction formulae also satisfy exists y Hyy").
- PDF pp. 27-29 = book pp. 20-22: basic formulae H, T_j, I_i, S; (2.1)-(2.3); START := I_0(0) and H(0,0) and forall x T_0(0,x); NONSTOP; ORDER.
- PDF p. 41 = book p. 34: H_1, H_2, H_infinity and the refined reduction property (i), (ii).
- PDF pp. 122-123 = book pp. 115-116: Büchi formulas exists v alpha and forall x exists u forall y beta in [exists and forall exists forall, (omega, 3)]; Step 1 of Thm 3.2.1 uses exists v Hvv.
- Bibliography entry [64]: J. Büchi, Turing machines and the Entscheidungsproblem, Math. Annalen 148:201-213, 1962 (not held; not cited with \cite).

## Discrepancies between the duty text and the source (recorded, not acted on as changes of target)

- The duty text writes the form as "forall x Zx and forall x exists u forall y phi". The source prints "exists x Zx and forall x exists u forall y beta" (PDF p. 42, last line). The handbook follows the source: exists x Zx, and the source's letter beta.
- The duty text writes the Remark as "(forall y Hyy)". The source prints "exists y Hyy" (PDF p. 43). The handbook proves exists y Hyy. (forall y Hyy is false in the intended models: H(t,t) holds only at t = 0.)
- The source names the subformula "Zxx -> Hxx"; in the handbook formula the conjunct is Zy -> Hyy inside START[0/y]. The body states the conjunct without asserting the source's printed form.

## Construction decisions (handbook completion; the source leaves the exercise to the reader)

- Machines: binary one-way programs with states 0..r (0 start, 1 and 2 stop), moves L/N/R, as in the source's Sect. 2.1 conventions; admissibility (N1) no left move at cell 0, (N2) a right move at time t only when h_t <= t-2.
- Universality: block simulation Sim(M) folding the two-way tape into blocks f gamma(T(j)) gamma(T(-j-1)) of length k = 2m+1, then Slow (two idle steps at the start, one after each step). Full correctness proof in the annex (Claims A-D).
- Formula: one element is both a time and a cell; the u of forall x exists u forall y is the successor. K splits pairs into three regions: below the diagonal H/T_0 carry the configuration; diagonal T_0 always (blank), H only at (0,0); above the diagonal H carries the post-move head record and T_0 carries "cell <= head" marks. Conjuncts beta1-beta9 (START, BLANK, OFFDIAG, STEP_P, MOVE, FRAME, ONEHEAD, NONSTOP, prec_{K,P} plus Act x -> Kxu). No equality; beta quantifier-free.
- Because letter 1 is not-T_0 the source's frugal argument does not apply verbatim; head uniqueness (ONEHEAD, OFFDIAG) makes FRAME's not-Hxy mean "not the head cell". Simulation lemma proves exact agreement on the tape.
- Proved: shape and computability; Remark exists y Hyy; intended model (finite with s+1 elements when halting in 2; on N when divergent); simulation lemma; refined reduction property (i)-(iii); Exercise 2.1.31 for every valid code e; corollary: pairwise recursive inseparability of Fin-sat, Non-sat, Inf-axioms within the class B.
- Not claimed: that B is a conservative reduction class (source p. 115 asserts it; needs a reduction of all FO formulas).

## Placement

Proposed after the input of definitions-interpolation-and-decidable-fragments-w02-p02-036 (body and annex), since this section refines def:p02-w02-p02-036-refined and uses its halting sets and lemma. The packet's default proposal is after w02-p02-035.

## MP-1

Trakhtenbrot 1950 Doklady (ACQ-2026-10-0615) is not held. Nothing written from it.

## Continuation

- Written: body handbook/parts/p02/definitions-interpolation-and-decidable-fragments-w02c-p02-025.tex; annex handbook/annex/p02/definitions-interpolation-and-decidable-fragments-w02c-p02-025.tex; symbol intake; empty bib intake (no new keys).
- Open: lead inserts the two \input lines; MP-1 remains blocked_source.
