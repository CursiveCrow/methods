# P3 27.6-27.8: Shelah 1971 isomorphic-ultrapowers theorem (packet w03a-p03-018)

## Sources read in this session

- Held: `source/references/acq-r1-ACQ-2026-10-0505/shelah-1971-elementarily-equivalent-isomorphic-ultrapowers.pdf`
  (S. Shelah, Every two elementarily equivalent models have isomorphic ultrapowers,
  Israel J. Math. 10 (1971) 224-233; journal scan, 10 pages). Pages read: 224 (abstract,
  theorem, Keisler comparison), 225 (notation), 230 (proof remarks 1-3, language reduction,
  list of pairs, enumerations of |M_i|^lambda). Page images rendered at 200-250 dpi and
  inspected directly, because the OCR layer renders lambda as "2".
- Bib key: `Shelah1971Ultrapowers` (already in handbook.bib, pages 224--233). No new keys.

## Verified locators

- p. 224: THEOREM. "Let lambda be any cardinality, mu = min{mu : lambda^mu > lambda}." Parts 1)-3).
  Keisler [6] summary: lambda^+ = 2^lambda; ||M||, ||N|| <= lambda^+; language <= lambda.
- p. 225: NOTATION. lambda fixed (infinite) cardinal; mu = min{mu : lambda^mu > lambda};
  "Notice that mu is a regular cardinal" (not used, not proved here); |M| universe, ||M|| power.
- p. 230: Remark 2 omits proof of part (3); Remark 3: D is lambda^+-good via Keisler [8];
  language WLOG <= 2^{||M||} <= lambda^{||M||} = lambda; list of pairs {(M_i, N_i) : i < 2^lambda};
  enumerations |M_i|^lambda = {a^i_alpha : alpha < 2^lambda}.

## Discrepancy with the assessment text

The assessment wrote mu = min{mu : 2^mu > lambda}. The held page images of both p. 224 and
p. 225 read mu = min{mu : lambda^mu > lambda}. The two differ (e.g. lambda = aleph_omega under GCH).
Per the rule that mathematical statements follow the source exactly, the handbook uses
lambda^mu, and the body notes explicitly that the exponent base is lambda, not 2.

## Treatment written

- Body `handbook/parts/p03/products-ultraproducts-and-horn-methods-w03-p03-018.tex`
  (section sec:p03-w03-p03-018-shelah-ultrapowers): notation convention, lemma on mu,
  cited theorem as published (cited=, statement duty only), hypothesis analysis (index set,
  ultrafilter, cardinal bound, language), Keisler comparison (as summarized by Shelah),
  explicit-index corollary, comparison theorem of the three relations, separation corollary
  ((Q,<) vs 2^omega x Q lex), worked example, limitations warning, relationships, source.
- Annex `handbook/annex/p03/products-ultraproducts-and-horn-methods-w03-p03-018.tex`:
  full proofs of mu lemma, index-bound corollary, comparison theorem (incl. finite case for
  arbitrary signatures via minimal B_{L0}), separation corollary.
- Editable host `handbook/parts/p03/ultrafilter-choice-and-source-boundary.tex`: last item of
  the assumption map rewritten and a paragraph reconstructing the original hypotheses
  (lambda, mu, single D over lambda, power < mu, no GCH, Keisler's lambda^+ = 2^lambda version,
  Choice in the enumerations of p. 230).
- Patch requests `work/waves/w03a/patches/w03a-p03-018.json`: driver inputs for body and annex;
  replacement of the "No fixed index set ... is asserted." sentence in thm:p03-keisler-shelah
  (read-only host types-ultraproducts-supplement.tex).

## Existing treatments found not in the packet list

- `handbook/parts/p03/simple-nip-and-o-minimal-theories-w03-p03-035.tex` lines 376-381 cite
  Shelah1971Ultrapowers at p. 224 to disambiguate it from Shelah's other 1971 papers.

## Block 2: Keisler 1961 (sections 27.7 and 27.8 MP-0)

### Source read in this session

- Held: `source/references/acq-r1-ACQ-2026-10-0223/ACQ-2026-10-0223.pdf` (H. J. Keisler,
  Ultraproducts and elementary classes, Indag. Math. 23 (1961) 477-495; publisher version of
  record, 19 pages; PDF metadata gives DOI 10.1016/S1385-7258(61)50048-0). Whole text layer
  read; page images inspected for pp. 477, 480, 484, 485, 486, 487, 491, 492 (OCR garbles the
  mathematics). Shelah 1971 p. 232 (reference 6) read for the series A 64 / Indag. Math. 23
  identification.
- New bib key in the intake: `Keisler1961ElementaryClasses` (same entry, field for field, as in
  the w03-p03-017 intake; on merge they are one key).

### Verified locators (Keisler 1961)

- p. 479: AC assumed throughout; well-ordering principle and maximal principle.
- p. 480: (omega_xi)^+; GCH = omega_{xi+1} = kappa(2^{omega_xi}), equivalently alpha^+ = kappa(2^alpha);
  S(X), S_alpha(X), bar S_alpha(X); filter, ultrafilter; Ultrafilter Theorem (Tarski).
- pp. 480-481: similarity type mu, rho = D mu, relational systems; L(mu) predicates only;
  operations replaced by operational relations (p. 481).
- p. 482: mu (+) xi, unary predicates P_{rho+zeta}.
- p. 483: reduced product, ultrapower, Prod, Pow; Theorems 1.1-1.6 stated without proof (pp. 483-484).
- p. 484: Lemma 2.1 with proof; Theorem 2.2 statement: alpha >= omega, alpha >= kappa(rho),
  kappa(2^alpha) = alpha^+, kappa(I) = alpha, structures of cardinality <= kappa(2^alpha);
  (i) D, E on I containing bar S_alpha(I); (ii) no Phi with both sets in bar S_alpha(I).
- pp. 485-486: proof of 2.2 (F, conditions (1)-(3), maximal chain, E_0, E, D_0, D); remark that
  D_0 is already an ultrafilter when every A_i has more than one element (p. 486); footnote 3
  (Cantor's method); footnote 4 (no relations / finite structures known without hypothesis).
- p. 486: Theorem 2.3 (ultrafilters D, E on alpha; no uniformity in the statement).
- p. 487: remark that only kappa(alpha^+)=2^alpha (as printed) at one alpha is used; Assumption
  (GCH for rest of Section 2); Theorem 2.4 with proof; transitivity remark; footnote 5 (1959
  special case; Kochen; counterexample).
- p. 490: open question (2.4-2.14 without GCH); appendix omits proofs.
- p. 491: countably complete; Q(alpha) (with bar S_omega(beta), as printed); "Hereafter suppose
  alpha, beta >= omega"; Lemma A.3 (i)-(iv).
- p. 492: Theorem A.4, Corollaries A.5-A.8, Theorem A.9.
- p. 493: Assumption GCH (for A.10-A.12).

### Reading notes

- Shelah's summary of Keisler (p. 224: single D over lambda, lambda^+ = 2^lambda, power <= lambda^+,
  language <= lambda) matches Keisler's Corollary A.6 with D = E (existence via Lemma A.3 (iii)),
  which Keisler announces without proof. The proved Theorems 2.2/2.3 have two ultrafilters D, E
  chosen after the structures. The reader text states this.
- Corollary A.8 is printed with no hypothesis; the reader text says so without inferring one.
- The annex proof of Theorem 2.2 follows Keisler's construction, but checks the final isomorphism
  directly from the definition of the ultraproduct relations instead of Theorem 1.1 and the reduct
  theorem; this is said in the annex.
- Notation deviations recorded in the convention: Keisler's type letter mu and predicate index
  lambda are not used (they clash with Shelah's lambda, mu); 0 for the empty set is written
  varnothing; L(mu (+) xi) is written L_xi in the annex.

### Written in block 2

- Body: new subsections sec:p03-w03-p03-018-keisler and "Keisler's and Shelah's hypotheses
  compared" replacing the paragraph that relied on Shelah's summary; section title, intro and
  Sources paragraph updated; Shelah convention retitled and scoped.
- Annex: proofs of Lemma 2.1, Theorems 2.2, 2.3 (with uniformity), 2.4, and the comparison theorem.
- Editable host: Keisler's hypotheses rebuilt from the article in a new paragraph of
  def:p03-ultrafilter-choice-boundary; the sentence "as Shelah reports it" removed.

## Continuation

- D-P4-003-GOAL-01, GOAL-02, GOAL-03 and the 27.8 MP-0 Shelah part written (see return).
- Open: the driver inputs and the thm:p03-keisler-shelah sentence are patch requests for the lead.
- Not used: the source's remark that mu is regular (p. 225); not stated in reader text.
- Block 2: 27.7 MP-0 (Keisler's own conditions and the comparison) and 27.8 MP-0 (Keisler's
  hypotheses in the boundary) written from the held Keisler article; see the block 2 section.
- Open: Keisler's Corollaries A.6/A.8 and Lemma A.3 (iii) are cited only (the source gives no
  proof). The Keisler1961ElementaryClasses key is in both the -017 and -018 intakes.
