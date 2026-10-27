# w03a-p03-053 (P3 38.7) research note: differences from ordinary first-order and probabilistic semantics

Label tag: `p03-w03-p03-053`. Files:
- body `handbook/parts/p03/topological-borel-measure-and-category-model-w03-p03-053.tex` (766 lines)
- annex `handbook/annex/p03/topological-borel-measure-and-category-model-w03-p03-053.tex` (718 lines)
- bib intake `handbook/bib/intake-p03-topological-borel-measure-and-category-model-w03-p03-053.bib`
- symbol intake `handbook/registry/symbols-intake-p03-topological-borel-measure-and-category-model-w03-p03-053.csv`

## Duty addressed

MP-0 (and US-1, same gap): explicit comparison naming the logical languages (FO, L_{omega_1 omega}, L_2/L_t on topological
structures, L(Q_c)/L(Q_m) on Polish-carrier (Borel) structures, L_{omega P} probability quantifiers, FO under the uniform finite
random-model probability), their semantic parameters and where each lives, and the nontransfer cases, with full annex proofs.
Explicit statements that neither the X_L code-space topology (sec:p03-morley-borel-truth) nor the finite random-model probability
(sec:p03-zero-one-law) is a measure/category logic: def:p03-w03-p03-053-no-substitution, backed by
thm:p03-w03-p03-053-code-carrier, thm:p03-w03-p03-053-almost-sure, thm:p03-w03-p03-053-finite-collapse.

Results written (all proved in the annex): code-carrier; almost-sure theory (complete, satisfiable, no finite model);
finite collapse of Q_c/Q_m to forall; Baire category lemma; comeager null set and the uniform/mixed laws; failure of ordinary
isomorphism invariance plus preservation under homeomorphisms / measure-preserving Borel isomorphisms; no countable carrier for
sigma_c, sigma_m (downward LS fails); L_2 noncompact on topological structures (and no finite-character strongly complete calculus);
L_t consequence = two-sorted FO consequence from Ext/Union/Empty/Bas (compactness, completeness, r.e. validities).

## Sources

Held (read this session): SRC-049 publisher preview `tmp/edition-2026-catalog-src038/tail-039-068/SRC-049-pageplace-preview-2026-09-09.pdf`
(reading derivative): Barwise ch. I, sec. 1.3 pp. 6--7 (completeness problem), sec. 1.6 p. 10 (Karp completeness; Lopez-Escobar Craig/Beth
for L_{omega_1 omega}), sec. 2.8 p. 21 (Part E: topological models; Friedman measure/category; Keisler probability spaces);
contents: ch. XV begins p. 557, sec. 2 p. 560; ch. XVI begins p. 579, sec. 2 p. 586, sec. 3 p. 591. No chapter bodies of XV/XVI.

Read online (legitimate open copies):
- https://arxiv.org/pdf/1702.04769 (arXiv v4, 9 April 2018 = published LMCS 14(2:2) 2018 layout, CC licence): sec. 1 pp. 1--2,
  sec. 2.2 p. 5 (meager/comeager), sec. 2.3 p. 6 (Borel probability measure, null sets, coin-flipping measure), sec. 2.4 pp. 7--8
  (large-section category and measure quantifiers; Remark 2.7; Theorem 2.8).
- https://cs.auckland.ac.nz/~nies/papersnew/BorelEMU.pdf (Montalban--Nies, author-hosted copy, "submitted Jan 28 2010, compiled
  April 7 2013"; page numbers of this copy): Def. 1.1 p. 1; history and Friedman's quantifiers p. 2; Thm 2.1 p. 3; Def 2.4,
  Thm 2.5 p. 5; Thm 2.6 p. 6. Only Def 1.1 (p. 1) and p. 2 are cited in reader text.
- https://arxiv.org/pdf/2104.12124v1 (Antonelli--Dal Lago--Pistone): read sec. 6 only for orientation; not cited.

Tried and blocked (bot check, not bypassed): Project Euclid pl/1235417282 (Steinhorn ch. XVI) and its .pdf URL; pl/1235417281 not
retried after the identical interstitial. The 1985 Ziegler and Steinhorn chapter bodies were therefore not read; no claim, locator
or notation in the reader text is taken from them beyond the contents-page locations.

## Open items (not supplied)

- Compactness, completeness and interpolation status of Friedman's/Steinhorn's L(Q_m), L(Q_c) over their own Borel model classes
  (Steinhorn ch. XVI secs. 2--3): not asserted; the summary table says "not established here". Needs the chapter body
  (Project Euclid copy blocked by bot check) -- owner packet w03-p03-052 holds ED26-SRC-049-0016.
- Interpolation for L_t (Ziegler ch. XV sec. 2): stated as a dependency sentence only; owner packet w03-p03-051 holds ED26-SRC-049-0015.
- Downward LS for L_{omega_1 omega} and for unrestricted L_2: table entries "not established here". A proved fragment LS exists in
  `handbook/parts/p03/comparison-games-and-infinitary-languages-w03-p03-039.tex` (thm:p03-w03-p03-039-downward-ls), not yet on the
  main.tex route, so not cross-referenced; once inserted, the L_{omega_1 omega} cell can cref it.
- Keisler's 1985 probability-quantifier chapter (ch. XIV, pp. 509ff, probability structures with a measure on the carrier, L_AP):
  not read (same Project Euclid block); the comparison uses the handbook's L_{omega P} finite-model presentation only.

## Existing treatments found

Listed: finite-model-theory.tex (sec:p03-zero-one-law), presentations/n-a-004-02.tex (sec:p03-morley-borel-truth).
Not listed in packet but found and linked: handbook/parts/p03/topological-model-theory.tex (L_2, L_t, compactness, basis axioms,
reduced ideal-products), handbook/parts/p15/probability-quantifiers.tex and probability-quantifier-elimination.tex (L_{omega P}),
handbook/parts/p02/variants.tex (L_{omega_1 omega} calibration, Karp boundary), restoration labels thm:fol-compactness,
thm:fol-completeness, thm:downward-ls; P1 thm:p01-csb.

## Continuation

Block 1 (earlier session) wrote the MP-0 comparison chapter and annex. Block 1 rerun (2026-10-12), after an assessment
that no 38.7 comparison is on the main.tex route:
- The route gap is a placement matter: the files are not yet \input in handbook/parts/p03.tex / handbook/annex/p03.tex
  (drivers are read-only; placement is in the return JSON for the lead).
- Added thm:p03-w03-p03-053-l2-uncountable (L_2 sentence theta_R with only uncountable carriers; R is a model) with annex
  proof; the L_2 'countable models' cell now says fails.
- Added sec:p03-w03-p03-053-finite: lemma thm:p03-w03-p03-053-pure-equality and thm:p03-w03-p03-053-finite-row
  (compactness, completeness/enumerability and Craig interpolation fail over finite structures; FO and L_omegaP with
  rational thresholds) with annex proofs; uses def:p03-finite-compactness-failure and thm:trakhtenbrot (both on route).
- Summary table rebuilt with an Interpolation column and a finite-structure row; L_omega1omega countable-model cell now
  cross-references tab:p02-fol-extensions (on route) instead of 'not established here'.
- Project Euclid retried: landing page for pl/1235417282 loads, PDF download returns an Incapsula bot check; not bypassed.

Still open (reported in the return): L(Q_c)/L(Q_m) compactness, completeness, interpolation over Steinhorn's model
classes (dependency sentence only; source body unread; unit owned by w03-p03-052); L_t interpolation (dependency
sentence; unit owned by w03-p03-051); interpolation for unrestricted L_2 (no proof written).

Block 2 (2026-10-13), after the assessment gap MP-0 (c) (L_2 interpolation cell 'not decided in this chapter'):
- Searched handbook for an existing L_2 interpolation treatment: none (topological-model-theory.tex, w03-p03-051 file,
  interpolation files of P3 checked).
- Added sec:p03-w03-p03-053-l2-interpolation (body lines 554-655): def:p03-w03-p03-053-l2-craig (Craig interpolation
  over topological structures, models_top), lemma thm:p03-w03-p03-053-discrete-rank (finite discrete spaces of size
  >= 2^q agree on L_2(empty) sentences of rank <= q; proof by cells/counts back-and-forth incl. open equality atoms),
  thm:p03-w03-p03-053-l2-interpolation (psi_i = Discrete & Fin & varphi_i; psi_1 |=top not psi_2, no L_2(empty)
  interpolant), example def:p03-w03-p03-053-l2-interpolation-example, limitation paragraph. Annex proofs
  annex:p03-w03-p03-053-discrete-rank (annex lines 547-655) and annex:p03-w03-p03-053-l2-interpolation (657-718).
  Proof is editorial (no source claim); reuses varphi_1, varphi_2 of finite-row and Fin of l2-noncompact.
- Table cell now 'Craig fails'; intro conclusions and summary prose updated; 'not decided' sentence now refers to the
  (R5) row only.
- Stated limitation in reader text: the counterexample needs a binary point relation; for point signatures of unary
  predicates only (correspondence signature) no proof is given.

Still open: (R5) L(Q_c)/L(Q_m) interpolation, compactness and completeness over Steinhorn's classes (source body
unread, unit of w03-p03-052); L_t interpolation (unit of w03-p03-051); L_2 interpolation restricted to unary point
signatures (not proved either way).
Bib key Barwise1985BackgroundAims duplicates the identical entry in intake-p03-comparison-games-and-infinitary-languages-w03-p03-041.bib.
