# Packet w03a-p03-032 (P3 ch. 32, sections 32.5-32.7): research note

## Sources opened in this session
- Shelah1971Stability, held: source/references/acq-r1-ACQ-2026-10-0504/shelah-1971-stability-fcp-superstability.pdf
  (published Ann. Math. Logic 3 (1971) 271-362 scan; text extracted with pdftotext). Read: Sec. 0 p.273
  (definitions of stable in lambda, superstable = stable in every lambda >= 2^|T|), Sec. 2 pp.296-305
  (Definitions 2.1-2.6, Lemmas 2.1-2.12, Theorems 2.9 and 2.13). Page numbers taken from running heads.
- ErdosMakkai1966, read online: https://users.renyi.hu/~p_erdos/1966-19.pdf (Erdős archive, Rényi Institute;
  scan of Studia Sci. Math. Hungar. 1 (1966)). Read all three pages: theorem, proof cases (i) and (ii),
  problems. Printed page numbers seen: 158 and 159 only (first page number not visible), so no page
  locators and no pages field in the intake bib entry (open item).

## What was written
- Body: handbook/parts/p03/stability-and-the-forking-calculus-w03-p03-032.tex
- Annex: handbook/annex/p03/stability-and-the-forking-calculus-w03-p03-032.tex
- Spectrum: tree rank, local character of a stable formula, product bound, S_1 -> S_m, tree count,
  Erdős-Makkai (full proof), many types -> OP, OP -> trees (dyadic construction, own), formula theorem,
  theory spectrum theorem (stable iff lambda-stable for all lambda = lambda^|T|; unstable => no lambda).
- Separating theories: QE-type lemma via back-and-forth in omega-saturated models; T_P (superstable in both
  senses, not omega-stable); T_E (stable, lambda-stable iff lambda^aleph0 = lambda, not superstable in both
  senses); Koenig-type lemma. Random graph: cross-referenced to w03-p03-031's proved theorem
  (thm:p03-w03-p03-031-random-graph) and its order-property example; not duplicated.

## Not written (remaining)
- "superstable iff stable in every lambda >= 2^|T|" for the handbook's forking definition of
  superstability (def:p03-stability-spectrum) is NOT proved. Shelah 1971 takes the cardinal condition as
  the definition (p.273); the equivalence with finite local character of forking needs the stable forking
  calculus (forking = dividing, nonforking extensions/definability) and a type-counting argument along
  dividing trees. Only the two example theories are verified in both senses.
- Source-specific presentations of Shelah 1978 (Classification Theory, 1st ed.) and Pillay 1996 are not held;
  nothing was written from them. Tent-Ziegler 2012 not held.

## Existing treatments found
- classification-theory.tex sec:p03-stability (defs; thm:p03-nonforking-calculus cited).
- w03-p03-031 chapter (concurrent): random graph forking, order property of the edge relation.
- countable-models-and-fra-ss-constructions-w03-p03-015.tex: random graph types/QE.


## Block 1 additions (12 October 2026)
- Shelah 1971 section 6 read in this session (held PDF, pdftotext): pp.346-359, Definitions 6.1-6.5,
  Lemmas 6.1-6.3 and the Remark after 6.3, Theorems 6.4-6.9, Corollaries 6.8, 6.10.
- New body section sec:p03-w03-p03-032-superstable: Shelah's degree (families of |T|^+ members),
  basic lemma (monotone, well defined, invariance, max for disjunction, alpha_0 bound), dividing lowers
  the degree, infinite degree gives level-uniform inconsistency trees of every width (own pruning proof
  replacing Shelah's 6.4 A->B induction), tree count (k_n-inconsistent siblings, needs lambda >= 2^aleph0),
  and thm:p03-w03-p03-032-superstable: (1) lambda-stable all lambda >= 2^|T| => (2) one lambda with
  lambda^aleph0 > lambda >= 2^aleph0 => (3) stable and Deg_m(x=x) < infinity => (4) forking-superstable.
- Warning def:p03-w03-p03-032-superstable-definitions updated: one direction proved, converse open.
- Annex proofs for all five new results. Dangling ref thm:p02-fol-compactness replaced by thm:fol-compactness.

## Continuation
- Remaining for the spectrum duty: forking-superstable => lambda-stable for every lambda >= 2^|T|.
  Route options: (a) Shelah 6.6, 6.7, 6.9 with 5.8 (Delta-indiscernible subsequence of length |T|^+ in a
  stable theory) to bound same-degree extensions by 2^|T|, plus (4) => (3) [infinite degree => a type
  forking over every finite subset]; (b) counting via stationarity over models using the stable calculus of
  thm:p03-w03-p03-031-stable-calculus (forking = dividing proved there). A sketch tried here: Erdos-Rado
  gives |T|^+ types pairwise differing on one phi with the same local-rank shape; Ramsey on an omega-subset
  yields an omega-family k-inconsistent or the order property, but the degree needs |T|^+-families, so the
  argument does not close without 5.8.
- Erdos-Makkai first page number: verify from a copy showing it, then add pages to bib.


## Author correction, 26 October 2026

The current manuscript now supplies the four annex items previously absent
despite their `proved` status: weak pressing down, finite uniformity on a
regular uncountable sequence, the bound on same-degree extensions, and the
forking-chain construction. The superstability proof now includes (4) to (3),
(3) to (5), and (5) to (1), and the promised |A| + 2^|T| type bound. This
supersedes the earlier statement in this research history that the converse
was not written; it does not erase that history or confer independent admission.

The original Shelah 1971 PDF held at
`source/references/acq-r1-ACQ-2026-10-0504/shelah-1971-stability-fcp-superstability.pdf`
was read at printed pp. 340 and 354–359. The same-degree proof makes explicit
the finite-pattern obstruction and regular-cardinal thinning behind Theorem
6.7 (pp. 355–356); the final count follows Theorem 6.9 (p. 357). The weak
pressing-down and uniformity arguments are written out rather than attributing
a proof to the paper, which does not supply its Theorem 5.8 proof. The
forking-chain proof is an editorial compactness/Ramsey argument, not a claim
that Shelah's 1971 paper defines modern forking.

The nonzero-limit hypothesis is explicit in the weak pressing-down statement.
The CSV intake's comma in h(x,y) is now quoted. The saved source-specific
obligations for unavailable books remain open. These changes are author
corrections; the main build and independent admission remain integration duties.
