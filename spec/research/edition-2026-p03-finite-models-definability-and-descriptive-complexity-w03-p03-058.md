# Research note: P3 39.5 games for existential second-order expressibility (packet w03a-p03-058)

Owned files:

- handbook/parts/p03/finite-models-definability-and-descriptive-complexity-w03-p03-058.tex (body, `\chapter`, toc tag `%% toc: P3 39 39.5`)
- handbook/annex/p03/finite-models-definability-and-descriptive-complexity-w03-p03-058.tex (annex)
- handbook/bib/intake-p03-finite-models-definability-and-descriptive-complexity-w03-p03-058.bib
- handbook/registry/symbols-intake-p03-finite-models-definability-and-descriptive-complexity-w03-p03-058.csv

Label tag: `p03-w03-p03-058`.

## Duty

MP-0: ESO comparison-game rules (relation-selection stage before the r-round FO
game), the Ajtai-Fagin variant with the query as parameter, the correspondence
theorems between Duplicator wins and ESO / monadic ESO inexpressibility with
complete proofs, and inexpressibility cases with full strategies; the IF
semantic-evaluation game kept distinct.

Units ED26-SRC-050-0001 and ED26-SRC-050-0002 are readonly here (owner
w03-p03-054); this packet writes the section-39.5 duty only. The writing
corresponds to Kolaitis manuscript Section 5 (= chapter 2 Section 2.5 of the
2007 volume, component ED26-SRC-050-0002-C007).

## Sources read in this session

Held:

- source/references/acq-r1-ACQ-2026-10-0472/graedel-2007-fmt-descriptive-complexity-ch3.pdf
  (Graedel ch. 3): text-searched for Ajtai, monadic NP, connectivity games; no
  treatment of ESO games. Not cited.

Online (legitimate, freely accessible):

- Kolaitis, "On the Expressive Power of Logics on Finite Models", manuscript
  dated 1 August 2003, 83 pp., https://dbai.tuwien.ac.at/staff/pichler/dbt/kolaitis.pdf
  (TU Wien course page). Downloaded 2026-10-11 to
  tmp/agent-scratch/w03a-w03a-p03-058-b1-author/dl/kolaitis.pdf and read as page
  images. Not the version of record (Springer 2007 chapter 2). Read:
  pp. 3-7 (vocabularies, partial isomorphisms, Def. 2.1 queries, Ex. 2.2 queries
  incl. Connectivity, Def. 2.3 definability, ESO/USO/MSO definitions p. 6,
  Ex. 2.5 disconnectivity and 2-colorability sentences p. 7); pp. 9-14
  (Def. 3.1 FO game with constants, Def. 3.4, Def. 3.5, Def. 3.6, Thm. 3.8,
  Thm. 3.10, Def. 3.11, Lemma 3.12, Def. 3.13, Thm. 3.14, Thm. 3.15);
  pp. 18-20 (Def. 3.22 Gaifman graph and N(a,d), Ex. 3.23, Def. 3.24 d-type,
  Def. 3.25 d-equivalence, Thm. 3.26 with hint, Method 3.27, Prop. 3.28);
  p. 25 (Prop. 4.6, Thm. 4.7 Fagin, Cor. 4.8); pp. 26-30 (Section 5 in full:
  Def. 5.1, Prop. 5.2, Method 5.3, Cor. 5.4, Def. 5.5, Method 5.6, Thm. 5.7
  with sketch, Cor. 5.8, Problem 5.9, Thms. 5.10-5.11 stated without proof).
  Bib key Kolaitis2003ExpressivePowerNotes, entry identical to the w03-p03-055
  intake (same document); duplicate to be deduped at merge.

## Handbook dependencies used

- thm:p03-w03-p03-038-pointed-ef, def:p03-w03-p03-038-positions,
  def:p03-w03-p03-038-records, def:p03-w03-p03-038-characteristic,
  thm:p03-w03-p03-038-characteristic, thm:p03-w03-p03-038-finite-records
  (proved pointed EF theorem); thm:p03-w03-p03-038-connectivity.
  The 055 file was rewritten during this block (its own W_m/Hintikka labels
  were removed in favour of 038); this packet was rebased onto 038.
- thm:p03-fagin (cited) and thm:p03-w03-p03-055-rank-definability.
- thm:p09-fagin74-theorem6 (proved Fagin), def:p02-complexity-standing,
  def:p02-w02-p02-036-fagin-encoding.
- def:p03-if-logic, thm:p03-dependence-eso (IF/dependence relationship).

## Provenance and departures

- Kolaitis's vocabularies include constants; kept, via Lemma
  thm:p03-w03-p03-058-ef-constants (reduction of the game with constants to
  the pointed game on the relational reduct).
- Completeness halves of Methods 5.3 and 5.6 are stated by Kolaitis without
  proof; full proofs written (finite sets Phi, Theta, Phi_0 of describing
  sentences; no global choice needed).
- Def. 5.5 is monadic; Kolaitis says the full-ESO version needs notation
  only. The general (<s_1..s_k>, r) Ajtai-Fagin game is defined and proved.
- Cor. 5.4 is proved in the general form "E(Q) NP-complete" as hypothesis
  (thm:p03-w03-p03-058-np-conp) and, since block b2, for Q = 3-colorability
  exactly as Kolaitis states it (thm:p03-w03-p03-058-np-conp-3col), with
  NP-completeness of 3-colorability proved (thm:p03-w03-p03-058-three-col-np).
- Thm. 3.26 (Hanf-type, FSV) is proved only for finite k-coloured graphs
  (symmetric irreflexive E plus unary colours), the case Theorem 5.7 needs;
  general form not proved (it belongs to the section-2.3 component owned by
  w03-p03-054).
- Thm. 5.7: Kolaitis's sketch pinches at two far-apart vertices with the same
  d-type. Same d-type on an undirected cycle allows a reflected pattern, for
  which the pinch need not preserve d-types; the proof uses equal oriented
  windows of radius d instead, found by pigeonhole among M+1 vertices spaced
  2d+1 apart, n = (M+1)(2d+1), M = 2^{k(2d+1)}, d = 3^{r-1}.
- Connectivity on Kolaitis's graphs (arbitrary binary E): his disconnectivity
  sentence defines "not strongly connected" on non-symmetric graphs; the
  corollary states both the strong and the weak (symmetric-closure) versions
  and the undirected case.

## Open items (not written)

- Kolaitis Theorems 5.10 (connectivity not monadic ESO on finite structures
  (V,E,Suc) with built-in successor, attributed to de Rougemont 1987) and 5.11
  (on finite ordered graphs, attributed to Schwentick 1994): stated without
  proof in the manuscript (p. 29). Block b2 tried to reach a legitimate copy
  of a proof: Fagin-Stockmeyer-Vardi, On monadic NP vs monadic co-NP,
  Information and Computation 120 (1995), ScienceDirect returned HTTP 403 to
  the fetcher; no author-hosted copy found by search. de Rougemont 1987 and
  Schwentick 1994 not reached. The pinch-and-Hanf argument of Theorem 5.7
  does not transfer: with Suc in the Gaifman graph the pinched edges create
  chords whose neighbourhood types differ (checked in b2). Not written.

## Block b2 (2026-10-12)

- Re-opened the Kolaitis manuscript copy (tmp/agent-scratch/.../dl/kolaitis.pdf,
  downloaded 2026-10-11 from https://dbai.tuwien.ac.at/staff/pichler/dbt/kolaitis.pdf)
  and its text dump; re-read pp. 3-4, 6-7, 25-30 and page 27 as an image
  (Cor. 5.4 reads NP != coNP). All locators in the body re-checked against
  these pages.
- Body intro: removed the unverified claim that the printed 2007 chapter has
  this material as Section 2.5; the text now says the presentation follows the
  manuscript, not the printed chapter (Springer chapter page redirected to a
  login, not followed).
- Closed the former open item "NP-completeness of 3-colorability": new
  def:p03-w03-p03-058-three-col, thm:p03-w03-p03-058-three-col-np (membership
  by certificate; hardness SAT -> Tseitin clause set S_phi
  (thm:p02-tseitin, thm:p02-tseitin-size) -> graph H_S with a six-edge
  disjunction gadget, two gadgets per clause), and
  thm:p03-w03-p03-058-np-conp-3col (Kolaitis Cor. 5.4 exactly), all proved in
  the annex. Gadget and reduction are my own write-up, not taken from a
  source; no attribution given.
- New symbols added to the intake CSV (the 3-colorability query symbol, palette vertices, Gamma, H_S).

## Continuation

Block b1 (2026-10-11): body and annex written for MP-0 (sections setting,
ESO game, Ajtai-Fagin games, connectivity, limits). Block b2 (2026-10-12):
3-colorability NP-completeness and Cor. 5.4 instance added; version statement
corrected; unit-compile ok. Block b2, second pass (2026-10-12): Kolaitis Theorems 5.10 and 5.11
stated with exact hypotheses (cited= de Rougemont 1987, Schwentick 1994),
the p. 29 built-in-predicate remark added next to the limits warning,
failure boundaries proved (thm:p03-w03-p03-058-reduct,
thm:p03-w03-p03-058-binary-conn); G8 fixed at line 126. Remaining: proofs of
Theorems 5.10 and 5.11 (open item above). The chapter is not yet input by handbook/parts/p03.tex or
handbook/annex/p03.tex (placement in the return file).

## Block b2, second pass (2026-10-12)

- Re-opened the manuscript copy (tmp/agent-scratch/w03a-w03a-p03-058-b1-author/dl/kolaitis.pdf)
  with pdftotext and as a page image of p. 29 (rendered to
  tmp/agent-scratch/w03a-w03a-p03-058-b2-author/p-29.png). Verified: p. 29
  Problem 5.9, built-in-predicate paragraph, Thm 5.10 (G = (V,E,Suc)), Thm
  5.11 (G = (V,E,<=)); p. 4 ordered graph definition and Example 2.2 start;
  p. 5 CN; p. 18 Def. 3.22 Gaifman graph, Example 3.23 (N(a,d) = L_n for
  d >= 2 on linear orders); p. 20 remark that d-equivalence of finite linear
  orders is equality of size.
- Body (after the limits warning): remark (Kolaitis p. 29, own words),
  def:p03-w03-p03-058-builtin, thm:p03-w03-p03-058-successor
  (cited=deRougemont1987), thm:p03-w03-p03-058-ordered (cited=Schwentick1994),
  failure-boundary list, thm:p03-w03-p03-058-reduct and
  thm:p03-w03-p03-058-binary-conn with annex proofs. The binary-ESO sentences
  gamma (one binary variable) and gamma_s (two) are my own construction.
- Proof sources tried again: Schwentick APAL 79 (1996) at ScienceDirect HTTP
  403; web search found no free full text (PhilPapers record has abstract
  only). Proofs of 5.10/5.11 remain unwritten.
- Bib entries deRougemont1987, Schwentick1994: data from Kolaitis's reference
  list (dR87, Sch94); the works were not read and no locator into them is used.

## Author proof audit and correction, 2026-10-26

The limitation prose now accurately reports the constructions already
proved: connectivity has a one-binary-relation ESO witness, while the
displayed strong-connectivity witness uses two binary relations. The old
claim that both displayed results use a single relation was unsupported.
Problem 5.9 is explicitly attributed to the status reported in the 2003
Kolaitis manuscript, without asserting its present status.

The ESO and Ajtai--Fagin game completeness arguments, the NP/coNP reduction,
the three-colouring gadget, the bounded-neighbourhood argument, the coloured
cycle construction and the binary connectivity witnesses were reread. No
claim of independent acceptance follows. The successor and ordered
connectivity statements remain cited only: the exact original proofs of
de Rougemont and Schwentick are still absent. The scoped four-pass TeX Live
build succeeded: 33 pages, 20 overfull warnings, and ten external references
unresolved in the isolated unit.

These are author corrections and bounded verification, not independent
review, source admission, complete-source coverage, or book completion.
