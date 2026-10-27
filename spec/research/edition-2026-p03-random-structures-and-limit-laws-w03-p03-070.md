# Research note: P3 40.7 Jump and complexity conditions (packet w03a-p03-070)

## Source read in this session

- Spencer, *Logic and Random Structures*, version hosted at
  https://cs.nyu.edu/faculty/spencer/papers/ircsallsubm.pdf (30 pp., PDF
  produced 6 July 2007 from ircsallsubm.dvi; SHA-256 digest
  b81de4d3a6126e08ab363f6438ab495c343b442a4b03beae7fb8295568bf545c).
  Downloaded to tmp/agent-scratch/w03a-w03a-p03-070-b1-author/dl/ by the
  first run of this block and re-read in the second run (pdftotext plus page
  images of pp. 9 and 18-21, which confirm the ceiling in
  t_{i+1} = max[t_i, ceil((u-i)/eps)] on p. 18 and K = ceil(r/eps) on p. 9).
  Pages read: 5-13 (sections 2-6), 14-16 (sections 7-9), 17-22 (sections
  9-12: Jump Condition pp. 18-19, Complexity Condition pp. 19-21, Tardos
  attribution p. 21), 29-30 (references; Spencer-Tardos is item [25] on p. 30,
  listed as submitted to Combinatorica).
  This is not the printed Springer chapter (2007, doi 10.1007/3-540-68804-8);
  bib key Spencer2007LogicRandomStructuresAuthor (entry copied byte-identically
  from the sibling intakes 067/069 so the finalizer dedupes it).
- The packet's held path source/references/acq-r1-ACQ-2026-10-0472/graedel-2007-fmt-descriptive-complexity-ch3.pdf
  is Graedel's chapter 3 of the same volume (106 pp.), not Spencer's chapter 4;
  it supplies none of sections 4.10-4.11.
- The held capture tmp/acquisition/src050/web-spencer-chapter-04-pdf-renderer.txt
  holds only fragments; its page tags (P18-P20) are offset by one from the
  printed folios of the PDF read here; locators in the handbook use the printed
  folios of the PDF.
- Spencer-Tardos, Ups and Downs of First Order Sentences on Random Graphs
  (Combinatorica 20 (2000) 263-280, doi 10.1007/s004930070025): web search in
  both runs found only the paywalled publisher record; not read; not cited.
  The search-result abstract says the paper proves two necessary conditions
  and hopes they characterize the functions; the handbook text reports only
  what Spencer's chapter says (sufficiency attributed to Tardos) and marks it
  as not proved.

## Source slips recorded in the reader text

- p. 18: numerator of 1/3 + 10^-6 given as 10^6+1; it is 10^6+3 (noted in
  def:p03-w03-p03-070-explosion).
- p. 19: T^-_alpha called the limit of T_{alpha+eps}; the side is alpha-eps
  (def:p03-w03-p03-070-side).
- p. 19: "the sequences t_0..t_u are the same inside each interval" fails
  (thm:p03-w03-p03-070-nonconstant: u=2, interval (2/5,3/7), t_2 = 5 or 4
  either side of 5/12).
- p. 9: K = ceil(r/eps) bound only valid for irrational parameters; for
  rational lambda the floor form is used (thm:p03-w03-p03-070-finite-closure).

## Existing treatment found (A9)

- Irrational-parameter closure, Nonexistence Lemma, Finite Closure Lemma and
  T_alpha axioms: handbook/parts/p03/random-structures-and-limit-laws-w03-p03-064.tex
  (def:p03-w03-p03-064-closure, thm:p03-w03-p03-064-finite-closure) and
  -068.tex (def:p03-w03-p03-068-closure, thm:p03-w03-p03-068-finite-closure,
  def:p03-w03-p03-068-axioms, thm:p03-w03-p03-068-continuity). Not in the
  packet's existing list. The 070 chapter now cross-references them and
  states that its versions extend them to rational parameters.
- f_A and spectra: def:p03-w03-p03-069-spectrum (used, not redefined).

## Continuation

Second run (this block):
- Re-read every annex proof of the first run step by step against the
  definitions; no change was made to the mathematics of those proofs.
- Replaced the Delta^p_k notation (defined as Sigma cap Pi, clashing with the
  oracle meaning) by explicit Sigma^p_k cap Pi^p_k in body and annex.
- Added the p. 18 numerator slip note, the cross-references to 064/068
  closure material and to thm:p03-w03-p03-068-continuity.
- Wrote the symbol intake CSV (it was missing).
- unit-compile ok; find_fused_spaces clean; check.py shows no finding in the
  070 files.

Open (not closable from the source read):
- Jump Condition for the source's own splitting set XPL_u: proved only for
  the refined set XPL*_u (contains XPL_u). At points of XPL*_u \ XPL_u (e.g.
  5/12 for u=2) the transfer argument fails (admissibility needs a density
  pair that changes sign); neither proof nor counterexample is known here.
  The Spencer-Tardos paper would settle the intended definition but is not
  freely reachable.
- The source's zero-one law for G(n, n^{-alpha}) at rational alpha outside
  XPL_u: needs probabilistic estimates the source does not give.
- All results on f_A, g_A and consistency of T^-_lambda assume (AS_gamma),
  i.e. the probabilistic Generic Extension schema, which the source only
  indicates (pp. 10-11) and the handbook cites in
  thm:p03-w03-p03-065-shelah-spencer.
- Printed Springer chapter sections 4.10-4.11: not read (paywalled, not held);
  no printed-version locators.

## Author correction 2026-10-26

The definition of weight previously required a finite base, whereas the
closure definition and its intersection proof quantify over arbitrary
vertex sets in infinite graphs. This was a gap in the manuscript, not an
additional assertion about the printed source.

- Extended the weight definition to arbitrary bases and finite nonempty
  extensions, assigning weight minus infinity when infinitely many edges
  meet the extension. This matches the convention already used in 064/068.
- Extended the calculus of weights to these bases. Additivity now treats
  infinite edge sets explicitly. The rigid-subextension proof first handles
  finite bases, then reduces a strict density inequality to a finite set of
  incident edges; it does not subtract two infinite weights.
- Consequently the enlarging-base lemma used in the closure intersection
  proof now has exactly the scope its applications require. Finite-closure
  estimates, zero-weight boundaries, and the distinction between the source
  XPL_u and the proved refinement XPL*_u are unchanged.

This is an author correction. It does not confer independent review or
acceptance, or discharge the distinct printed Springer-source obligation.
The earlier open-dependency note concerning the Generic Extension theorem
should be read with packet 064: its annex now contains a proof of that
probabilistic input. The exact rational Jump Condition and the source's
Tardos sufficiency claim remain outside the proved claims of this packet.
