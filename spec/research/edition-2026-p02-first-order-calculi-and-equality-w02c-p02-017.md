# P2 17.4 supplement: Mendelson's first-order theories and deduction theorem (packet w02ca-p02-017)

## Duty

17.4 MP-0 (Mendelson part): complete separate presentation of Mendelson,
Introduction to Mathematical Logic, 4th ed. (1997), ch. 2: first-order
theories with logical axioms A1-A5 incl. the (A4) free-for and (A5) not-free
provisos; MP and Gen (Gen unrestricted in derivability); dependence of wfs in
a deduction; Prop. 2.4; Deduction Theorem Prop. 2.5 with its Gen hypothesis;
Cor. 2.6 and 2.7, each with proof written. Enderton 2001 sec. 2.4 part of
MP-0 remains blocked_source (not held).

## Source read this session

source/references/acq-r3-ACQ-2026-10-0618/mendelson-1997-intro-math-logic-4ed.pdf
(sha256 ea9949fd...; PDF page = printed page + 7). Read as text (pdftotext):
PDF 41-44 (book 34-37), 59-61 (book 52-54), 64-65 (book 57-58), 67 (book 60),
70 (book 63), 76-83 (book 69-76).

Verified locators used: p. 34-35 formal theory, proof/deduction from Gamma,
consequence, Gamma |- C, |- C; p. 35 system L axioms (A1)-(A3) and MP;
p. 36 Lemma 1.8 (|-_L B => B, five-step proof); p. 37 Proposition 1.9
(deduction theorem for L); p. 52 terms, wfs, scope, defined connectives,
(Ex) as abbreviation; p. 53 bound/free occurrence, free/bound variable;
p. 54 notation B(x_i), B(t), "free for", facts 1-4; p. 57 first-order
language; p. 58 closed wf; p. 60 satisfaction by sequences; p. 63 (X),
Lemma 1, Lemma 2, (XI); p. 69 sec 2.3, logical axioms A1-A5, remark that
(Ax_i)B => B are A4 instances, footnote pointing to sec 1.4 terminology;
p. 70 proper axioms, predicate calculus, MP, Gen, model, pseudo-instance (V)
for A4; pp. 70-71 pseudo-instance (VV) for A5; p. 71 sec 2.4 start,
subscript K dropped; p. 72 Prop 2.1, Prop 2.2, Cor 2.3; p. 73 failure of the
unmodified deduction theorem, definition of dependence, example; p. 74
Prop 2.4 with proof, Prop 2.5 with proof (cites Prop 2.1 for |- B => B),
"rather cumbersome" remark; p. 75 Cor 2.6, Cor 2.7 (no proofs), Extension of
Props 2.4-2.7, example, Exercise 2.27(a); p. 76 Exercise 2.29 (prove the
Extension).

## Files

- handbook/parts/p02/first-order-calculi-and-equality-w02c-p02-017.tex
  (sec:p02-w02c-p02-017-mendelson)
- handbook/annex/p02/first-order-calculi-and-equality-w02c-p02-017.tex
  (sec:annex-p02-w02c-p02-017-mendelson)
- handbook/registry/symbols-intake-p02-first-order-calculi-and-equality-w02c-p02-017.csv
- handbook/bib/intake-p02-first-order-calculi-and-equality-w02c-p02-017.bib
  (comment only; Mendelson1997 already in handbook.bib)
- work/waves/w02ca/patches/w02ca-p02-017.json (attribution fix request)

## Editorial decisions

- Source notation kept: \neg, \Rightarrow, (\forall x_i), script B, C, D, E,
  D_1..D_n, A^n_j, f^n_j, a_j, |-_K.
- |- B => B is derived directly from A1, A2, MP (Mendelson's Lemma 1.8 proof
  transferred to K) instead of citing Prop 2.1, so no dependency on the
  propositional completeness theorem.
- Prop 2.4 proved by the subsequence of non-dependent steps (the deduction
  Mendelson's length induction produces).
- Prop 2.5 proved by explicit blocks E_i with invariant (Q), so the
  Extension of Props 2.4-2.7 (which Mendelson counts as part of their
  statements and leaves as Exercise 2.29) is proved too. Extension stated
  existentially (there is a deduction with the property).
- Cor 2.6 and 2.7: proofs written (Mendelson gives none).
- Failure case: proved via a soundness lemma for theorems of K in the
  handbook's Tarskian semantics (def:p02-fol-satisfaction), with a free-for
  substitution lemma for Mendelson's replacement-substitution (proved from
  thm:p02-fol-term-substitution, thm:p02-fol-term-coincidence,
  thm:p02-fol-coincidence). Mendelson's own semantics uses sequences; the body
  says the lemmas are counterparts of his Lemma 2, (X), (XI) and Prop 2.2.
- Worked example: Exercise 2.27(a) via Cor 2.6, the Extension, and Prop 2.5.

## Existing treatment found

- sheet:hilbert-fol, def:p02-hilbert-fol-dependencies,
  thm:p02-hilbert-fol-deduction (first-order-calculi-supplement.tex):
  different system (restricted Gen, capture-avoiding A4, primitive exists).
  Linked and contrasted in sec:p02-w02c-p02-017-relations.
- Kleene presentation sec:p02-w02-p02-025-kleene: linked.
- Attribution defect (assessor observation, confirmed against the source):
  first-order-calculi-supplement.tex lines 99-100 say Mendelson supplies the
  dependency-sensitive generalization convention; in Mendelson Gen is
  unrestricted (p. 70). Patch request filed for the supplement (readonly
  host). The same claim in the registry comment
  handbook/registry/calculi/hilbert-fol.tex lines 1-3 is not in this
  packet's hosts; reported in the return for the lead.

## Continuation

- Written: all of MP-0 Mendelson part (body + annex). Remaining in MP-0:
  Enderton 2001 sec. 2.4 (blocked_source, not held).
- Checks (end of session): unit-compile ok (2 small overfull annex heading
  lines); check.py --tree handbook shows no findings in the new files;
  find_fused_spaces no hits. Cross-references use the on-route restored
  semantics sections (sec:fol-semantics-01/02, sec:fol-syntax-semantics-03/04,
  lem:term-substitution, lem:fol-coincidence), not the off-route
  first-order-syntax-semantics.tex labels.
- Lead actions: insert the two \input lines (placement in return file);
  apply patches/w02ca-p02-017.json after the body insertion.
