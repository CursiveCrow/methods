# Research note: 19.8 Equality boundaries and the connection to superposition (w02b-p02-026)

## Duty

Section 19.8 (`sec:fol-cardinality-normalforms-04`, closing paragraph of
`handbook/restoration/inherited-05568-05923.tex`, lines 351-355) only names an
equality-complete extension of resolution.  Duty MP-0: select one
equality-complete connection and supply its actual rules and guarantees
(soundness and refutational completeness under identity semantics) with
written proofs, linked to `thm:fol-resolution` and the equality boundary.

## Selected connection

Clausal equality axioms (reflexivity, symmetry, transitivity, function
congruence for every non-constant function symbol, relation congruence for
every relation symbol occurring in the clause set) added to the input, then
the unchanged Resolution and Factoring rules of the inherited section (whose
unification procedure already treats `=` as an atomic symbol).

Proof route (all in the annex file of this packet):

1. Translation lemma: replacing `=` by a fresh binary relation symbol
   `\mathsf{eq}` commutes with substitution, unification, Resolution and
   Factoring, and is truth-preserving when `eq` is read as identity.
2. Quotient lemma: a clause set has a model (identity semantics) iff its
   translation together with the translated equality axioms has a model
   (`eq` arbitrary).  Proof by quotient structure; finite choice only.
3. Main theorem: (1) unsatisfiable <-> (2) translated set unsatisfiable <->
   (3) finite propositionally unsatisfiable set of ground instances <->
   (4) Resolution with Factoring derives the empty clause from S + Eq_S.
   Uses the proved equality-free theorems `thm:p02-w02-p02-028-clause-form`
   and `thm:p02-w02-p02-028-resolution` on the translated set.
4. Bare resolution theorem: Resolution with Factoring refutes S iff S^eq is
   unsatisfiable (exact characterisation of what bare resolution decides).
5. Failure cases (proved): {a=b, P(f(a)), not P(f(b))} has no bare
   refutation; omitting the P-congruence clause from Eq loses completeness
   for {a=b, P(a), not P(b)}.
6. Soundness of the three ordered-superposition rules of
   `sheet:ordered-superposition` (ordering and selection conditions unused).
   The refutational completeness of superposition remains the cited
   `thm:p12-superposition-completeness`; it is not proved here.  The
   duty's success condition is met through route 1-4 (the duty offers the
   equality-axiom route as an alternative to superposition).

## Sources opened in this session

- `source/references/acq-r1-ACQ-2026-10-0379/nieuwenhuis-rubio-2001-paramodulation-based-theorem-proving.pdf`
  (author typescript, dvips build "TeX output 2000.09.21", 75 pp numbered
  1-75; PDF page = typescript page).  Read pp. 3-4 (section 1.1):
  congruence axioms E (reflexivity, symmetry, transitivity,
  monotonicity-I for each non-constant function symbol, monotonicity-II for
  each predicate symbol) on p. 3; the satisfiability equivalence of S with
  equality and S together with E without equality, the remark that resolution
  and factoring with E generate too many mostly unnecessary clauses, and the
  move to paramodulation (Robinson and Wos 1969, Brand 1975) on p. 4;
  footnote 1 on p. 4 (expressiveness of equality).  Source notation: equality
  written `\simeq`, axioms as implications.
- The existing key `NieuwenhuisRubio2001` in handbook.bib describes the
  printed chapter (pp. 371-443).  Typescript page numbers do not match it, so
  a new intake key `NieuwenhuisRubio2001Typescript` carries the held version.

## Existing treatment found

- Listed: inherited section (restoration file) with resolution rules,
  soundness theorem, `thm:fol-resolution`; `thm:p02-w02-p02-028-resolution`,
  `thm:p02-w02-p02-028-st-herbrand-eq` (quotient construction for the
  validity form inside a proof), `def:p02-w02-p02-028-equality-limit`.
- Not listed: `def:p01-w02-p01-025-eq-axioms` and
  `thm:p01-w02-p01-025-axiom-metatheorem` (equality axioms as sentences in
  natural deduction); `sheet:ordered-superposition`,
  `def:p12-ordered-superposition`, `thm:p12-superposition-completeness`
  (cited); `handbook/parts/p02/first-order-resolution.tex:242` (off-route
  sentence naming equality axioms, paramodulation, superposition);
  `handbook/parts/p12/small-clause-optimizations.tex:470-486` (congruence
  axioms simplified away; unrelated use).

## Symbol decisions

- `\mathsf{eq}` chosen for the fresh relation symbol because `\approx`
  is the equality symbol of `sheet:ordered-superposition` (identity
  semantics) and also the fresh relation symbol of the w02-p02-028 annex;
  using `\approx` here would give it two roles in one section.
- `\mathrm{Eq}(\Sigma)`, `\mathrm{Eq}_S`: clausal equality axioms; same glyph
  family as `\mathrm{Eq}_{\mathcal L}` (p01, sentences) and `\mathrm{Eq}`
  (w02-p02-028 annex, quantifier-free formulas).  Declared overlap.

## Continuation

- 2026-10-04: duty MP-0 drafted.  Body (359 lines) and annex (379 lines),
  bib intake (NieuwenhuisRubio2001Typescript), symbol intake and return
  written.  unit-compile ok; check.py shows only the own-intake bib-key
  finding; find_fused_spaces no hits.
- All FLRV1 and SRC components in the packet are read-only units owned by
  w02b-p02-025 / w02b-p02-001 and are reported not_started with that owner.
- Open: refutational completeness of ordered superposition stays the cited
  thm:p12-superposition-completeness (not part of the selected route).  A
  forward reference from the restoration paragraph (lines 351-355) to
  thm:p02-w02b-p02-026-eq-resolution is suggested to the lead in the return.
