# w02-p02-036 — section 21.8 (finite versus unrestricted validity) and D-P4-010-GOAL-03

Packet: `work/waves/w02/packets/w02-p02-036.json` (label_tag `p02-w02-p02-036`).

## Files

- Body: `handbook/parts/p02/definitions-interpolation-and-decidable-fragments-w02-p02-036.tex`
  (`sec:p02-w02-p02-036-finite-validity`; insertion proposal: `handbook/parts/p02/first-order-logic.tex`
  after `\input{parts/p02/first-order-depth}`).
- Annex: `handbook/annex/p02/definitions-interpolation-and-decidable-fragments-w02-p02-036.tex`
  (fourteen annex items; insertion proposal: `handbook/annex/p02.tex` after
  `\input{annex/p02/first-order-completeness-remainder}`).
- Editable host changed: `handbook/parts/p03/finite-model-theory.tex` (Fagin convention, theorem
  restatement, order conventions, P9 link; Trakhtenbrot paragraph and table row now point to the
  proof).
- Intakes: bib intake (no new keys), symbol intake (13 rows).
- Patch requests: `work/waves/w02/patches/w02-p02-036.json` (restoration capture
  `inherited-08248-08305.tex` and off-route `p04/decision-problems-and-arithmetical-hierarchy.tex`).

## Sources opened in this session and locators used

- BorgerGradelGurevich1997, held file
  `source/references/acq-r1-ACQ-2026-10-0056/borger-gradel-gurevich-1997-classical-decision-problem.pdf`.
  Version: authors' TeX-generated book file (title page Springer-Verlag, no imprint page), not the
  printed 1997 edition. Locators below are the printed page headers and numbering inside that file:
  Sect. 2.1.2 (p. 33, PDF page 40); Exercise 2.1.26 (p. 33; the example formula is
  `forall x exists u forall y (not Kxx and Kxu and (Kyx -> Kyu))`, checked on the rendered page);
  Def. 2.1.27 and Def. 2.1.28 (p. 33); Thm. 2.1.30 and its proof (pp. 34--35); Sect. 1.3 prefix-vocabulary
  class notation (pp. 8--9); Thm. 6.0.2(6) `[all,(omega),(1)]_=` decidable for satisfiability and finite
  satisfiability (p. 240, PDF page 247, checked on the rendered page). Whether the page numbers equal the
  printed edition's is not verified; they are the numbers printed in the held file.
- Fagin1974, held file `source/references/p09-fagin1974/500-genspec-author-scan.layout.txt` (text layer
  of the author scan). Section 4 and the encoding e(A), E(A): pp. 52--53; Theorem 6: p. 53; definitions of
  P, NP, P_1, NP_1: p. 51; proof, machine direction: pp. 53--54; proof, guessed linear order `<` with
  min/max constants and successor, lexicographic successor on k-tuples: pp. 54--55; built-in-order remark
  after Corollary 12: p. 60.
- Handbook-internal authorities (read in this session): Turing machine model
  (`restoration/inherited-07506-07677.tex`), c.e. equivalences and complement criterion
  (`inherited-07753-07843.tex`), K and its undecidability (`inherited-08081-08143.tex`), validity
  enumerable and inherited Trakhtenbrot statement (`inherited-08248-08305.tex`), FOL syntax/semantics,
  coincidence, reduct invariance, isomorphism invariance lemmas.

## Provenance of the proof

Block 1 (Trakhtenbrot, undecidability form): written for the handbook's machine model (two-way infinite
tape, q_acc/q_rej), not a reproduction of BGG's proof. A computation-table encoding with one linear order for
time and cells; head start position left free; acceptance clause forbidding q_rej; reduction from K via a
fixed recognizer; a path-gadget translation to one binary relation (looped vertices = elements); renaming
plus empty expansion to any signature with a binary symbol.

Block 2 (4 October 2026; BGG Thm. 2.1.30 inseparable form and the rest of Sect. 2.1.2):

- Pages opened this session in the held BGG file (rendered at 110 dpi and text layer): pp. 19-22 (PDF 26-29;
  Sect. 2.1.1 heading on p. 18/19, intended readings p. 20, Lemma 2.1.2, STEP_M formulas (2.1)-(2.3) pp. 20-21,
  rho_M, ORDER, START, NONSTOP p. 22), p. 27 (Def. 2.1.14 Krom/Horn), p. 33 (Sect. 2.1.2 opening: FMP
  argument; prec_K with class [forall exists forall] cap KROM cap HORN; Ex. 2.1.26; Def. 2.1.27; Def. 2.1.28;
  Ex. 2.1.29), p. 34 (Thm. 2.1.30; H_i and the non-halting set H; reduction property (i),(ii); transfer
  argument), p. 35 (finite model on {0,...,k+1}; sharpened stop condition; display of prec_{K,M}; infinite-model
  argument), p. 36 (Ex. 2.1.31-2.1.34), p. 37 (Def. 2.1.35, Ex. 2.1.36, Ex. 2.1.37, Def. 2.1.38, Thm. 2.1.39).
  The source's notation is prec_K, prec_{K,M}, rho_{M,prec} (the assessment wrote K, K_{eps,M}); the text uses
  the source's.
- Repair of the source sketch. Read literally (ORDER deleted, successor read as the function x', K occurring
  only in prec_{K,M}), the source's formula does not force S-chains (0, 0', 0'', ...) to be injective, and the
  no-change clause (2.3) then fails to propagate tape letters at collisions; the source's sentence "their
  representatives n are linearly ordered by the relation K" is not derivable from the displayed prec_{K,M}
  (it gives each visited x some K-larger u, unrelated to x'). The handbook formula keeps ORDER minus the
  successor-existence clause (so K is a strict linear order and S its immediate-successor relation, giving
  injectivity), and the relativized axiom prec_{K,M} asserts S-successors for active moments and both
  S-neighbours for visited cells (two-way tape). With this the simulation lemma, reduction property (i),(ii)
  and the infinity-axiom case (iii) are proved in full; the sharpened stop condition (step counter) is not
  needed because active moments form an infinite K-chain. The body states these differences after
  def:p02-w02-p02-036-refined.
- Halting problems: H_1 (reject), H_2 (accept), H_infinity (diverge) on the empty input, as sets of valid
  program codes (sec:universal-reductions-01). Inseparability proved from the definition of a decider (no
  universal machine, parameter or recursion theorem used): diagonal sets D_1, D_2 on self-input, a computable
  "write bin(e) then run M_e" map w, and loop-on-one-halting-state maps lambda_rej, lambda_acc. BGG cite
  [57, 445] for this lemma; enumerability of the H_i (BGG p. 34) is not claimed in the text.
- FO version: derived from the Sent(L) version by intersecting a separator with Sent(L); relies on the coding
  reading recorded in the body Inputs paragraph (codes of all formulas and of the sentences of each finite
  signature form decidable sets).
- FMP theorem: stated for finite signatures with function and constant symbols and for formulas (existential
  closure). The source's two facts give the c.e. half; the co-c.e. half uses enumeration of validities
  (completeness); the body says so.
- Ex. 2.1.29 is proved twice: as a case of the main theorem and by the source's route via rho^infinity_M
  (all models infinite) and undecidability of H_1.
- Ex. 2.1.36 is proved for conservative reduction classes from the FO version. Ex. 2.1.37, Def. 2.1.38,
  Thm. 2.1.39 and Ex. 2.1.40 are mentioned only as the source's (Ex. 2.1.37 by name); not proved.
- Path-formula notation renamed rho_j -> pi_j to free rho for the source's rho_M, rho_{M,prec}.
- Example infinity axiom: the earlier varphi_infinity is replaced by the source's prec_K.

## Existing treatments found

All listed in the packet. Additionally relevant (not listed): `handbook/parts/p04/complexity.tex` 416-436
(`def:p04-captures-complexity`, a variant encoding `1^k0b` on [n]) and 466-470 (Fagin pointer);
`handbook/parts/p09/presentations/n-c-004.tex` 21-33 and `n-c-004-01.tex` 69 (`thm:p09-fagin74-theorem6`,
Fagin's encoding and Theorem 6 already presented with locators); `handbook/parts/p04/decision-problems-and-arithmetical-hierarchy.tex`
38-42 (`thm:p04-trakhtenbrot`, not on the p04 route). The P3 edits link to these rather than duplicating them.

## Notes for the lead

- `thm:p03-fagin` was restated with the hypothesis that tau has at least one relation symbol and with the
  explicit encoding; Fagin's Theorem 6(2) handles empty S with NP_1, so the previous unqualified statement
  was wider than the source under the source's encoding.
- Symbol overlaps: `\(\mathsf{NP}_1\)` and `e(\cdot), E(\cdot)` are also used in `sec:p09-presentation-n-c-004`
  with the same meaning; `\rho_j` uses the globally registered formula-metavariable glyph rho with an index,
  same type (formula). The P03 chapter uses tau for a signature, which collides with the global sentence
  metavariable row; the new P2 text uses `\Lang` instead.
- The P2 body's references into P3/P4/P9 and the P3 references to `thm:p02-w02-p02-036-*` resolve only after
  the body and annex are input by the drivers.

## Continuation

State at return of block 2 (4 October 2026): the four gaps named by the assessment are written in the owned
body and annex (Def. 2.1.28, Ex. 2.1.29, H_1/H_2/H_infinity with an inseparability proof, refined reduction
property through prec_{K,M}, Thm. 2.1.30 for Sent(L) and FO; FMP decidability (p. 33); prec_K with the proof
of Ex. 2.1.26; Def. 2.1.35 and Ex. 2.1.36). The P3 host gained one pointer sentence. Unit compile ok (10 small
overfull boxes, largest about 20pt); fused-space check clean; check.py --tree shows no finding in these
files. Open: the G1 guard flags untracked files of packets w02-p02-044/045
(spec/research/edition-2026-p02-unit-accounting-w02-p02-04{4,5}{.md,-return.json}); they were written by those
packets (owned_files empty in their packets), not by this one, and this packet may not modify them; the lead
must re-snapshot or attribute them. The two earlier patch requests in work/waves/w02/patches/w02-p02-036.json
are unchanged and still apply.
