# P3 40.4 Constant-probability regimes and their countable models (packet w03a-p03-067)

## Provenance

- Source followed: Joel Spencer, "Logic and Random Structures", author's version,
  https://cs.nyu.edu/faculty/spencer/papers/ircsallsubm.pdf (30 pages, dvips 2007-07-06,
  SHA-256 digest b81de4d3a6126e08ab363f6438ab495c343b442a4b03beae7fb8295568bf545c), fetched and read
  2026-10-11 in block 1. Its own section numbers 1-14 (no chapter prefix) and its own printed
  page numbers are used. The Springer 2007 printing (Finite Model Theory and Its Applications,
  doi 10.1007/3-540-68804-8) was not read; no locator is attributed to it.
- Pages read: 1-15 (sections 1-8), 26-30 (section 14, About the references, reference list).
- Re-fetched 2026-10-12 (block 1 rerun) from the same URL; same SHA-256 digest; pp. 10-16 re-read
  (Generic Extension, large deviation, completeness sketch, sections 6-7, start of 8).
- Locators used: SU(n,p) p. 1; almost surely / almost never p. 2; unary zero-one theorem and
  its theory p. 3; countable models of the unary theory aleph_0-categorical p. 4; G(n,p) p. 4;
  K4 threshold p. 4; sparse zero-one theorem pp. 5-6; rooted graphs, dense/sparse/rigid/safe
  p. 6; three vertices with no common neighbour pp. 7-8; t-closure p. 8; large deviation omitted
  pp. 10-11; section 6 pp. 12-13; section 7 pp. 13-15; section 14 game, theorem, corollary
  pp. 26-27; Glebskii et al. and Fagin attribution p. 27.

## Ownership note

The queue unit ED26-SRC-050-0004 lists packet w03-p03-064 as its writer (readonly_units).
Section 40.4's own duty MP-0 asks for the constant-probability regimes, the almost-sure-model
classification and the asymptotic proof, which is the material of the source's sections 6 and 7
(with the unary constant-p regime of section 1 as the second constant-probability regime).
This packet writes that section text; the owner packet should cross-reference these labels
rather than write a second treatment of sections 6-7.

## Existing treatments (linked, not duplicated)

- handbook/parts/p03/finite-model-theory.tex sec:p03-zero-one-law (uniform relational, G(n,1/2)).
- handbook/parts/p09/presentations/n-c-002-02.tex thm:p09-fagin1976-graph (fixed-p graph law,
  Fagin route, back-and-forth plus elementary substructures) and its annex.
- handbook/parts/p03/classification-theory.tex thm:p03-random-graph (cited Rado graph).
- handbook/parts/p03/presentations/rado-1964.tex thm:p03-rado64-extension (found, not listed in
  the packet's existing list).
- handbook/parts/p03/qe-categoricity-games-supplement.tex def:p03-ef-game, thm:p03-ef (cited).

## Continuation

- Block 1 (2026-10-11): body handbook/parts/p03/random-structures-and-limit-laws-w03-p03-067.tex
  (1-378) and annex handbook/annex/p03/random-structures-and-limit-laws-w03-p03-067.tex (1-323)
  written; unit-compile ok; fused-space check clean; check.py shows only the own-intake bib-key.
- Open for a later block: complete proofs of the irrational-alpha countable-model claims
  (thm:p03-w03-p03-067-sparse-models is sketched): rigid one-root sequence with almost sure
  glued copies, infinite closure of c, witness-demand graph models T_alpha and is unique, finite
  closures in it, completeness of T_alpha. Candidate source: Spencer, Countable Sparse Random
  Graphs, Random Structures and Algorithms 1 (1990) 205-214 (reference [20] of the author
  version); not yet searched for a legitimate free copy.
- Block 1 rerun (2026-10-12): def:p03-w03-p03-067-sparse-notions is now an hbconvention that
  cross-references 065 (rooted graph, dense/sparse/rigid/safe, safe criterion) and 068 (e_G(N;S),
  rigid over a set, cl_t, axioms of T_alpha, cited axiomatization); only cl(X) = union of cl_t(X)
  and k, c are defined locally. The sketched sparse-models item is replaced by full annex proofs:
  thm:...-diophantine (pigeonhole), def/thm:...-circulant (editorial construction H(v): 2k-regular
  circulant on v nonroots plus root joined to the Beatty set Q_v; rigid, excess alpha*g(v), glued
  H^s safe), thm:...-infinite-closure (compactness + downward LS), def:...-demands (run; demands
  postponed until roots are present, a detail the source leaves open), thm:...-demand-model (sparse
  over every stage set; Nonexistence, Generic Extension with t-genericity for all t; finite
  closures), thm:...-demand-unique (back-and-forth over finite sets A with every outside finite Y
  sparse over A), cor thm:...-sparse-models, example def:...-pi-seven (K5 vs H(13) at pi/7;
  brute-force check script tmp/agent-scratch/w03a-w03a-p03-067-b1-author/check_hv.py).
- Remaining open (C007): thm:...-demand-model item 4 (G* models T_alpha) uses the cited
  thm:p03-w03-p03-068-axiomatized: that the Nonexistence and Generic Extension axioms hold almost
  surely and generate T_alpha (large-deviation estimate and completeness game) is not proved in the
  handbook; the source omits the large-deviation proof (pp. 10-11) and sketches completeness
  (pp. 11-12). That is source section 5 material (component C005, unit owner w03-p03-064).
- Bib key overlap: siblings cite the same PDF as SpencerLRS2007Preprint (065 intake);
  this file uses Spencer2007LogicRandomStructuresAuthor. Lead may merge.
- Block 2 (2026-10-13): closed the cited step. New lemma thm:p03-w03-p03-067-axioms-generate
  (body 323-376; annex 279-372): (1) the 068 axioms (def:p03-w03-p03-068-axioms, with "copy"
  read as injective edge-preserving map) and the 070 axioms (def:p03-w03-p03-070-theory) agree
  datum by datum in every graph (rigid-over in 068 = alpha-rigid in 070 via S <-> X' cup Z_0;
  safe = alpha-safe by thm:p03-w03-p03-070-same-theory(2)); (2) each 068 axiom holds a.s. via
  thm:p03-w03-p03-070-as-holds; (3) a.s. sentences = logical consequences of graph axioms + 068
  axioms, consistent and complete, via thm:p03-w03-p03-070-complete(2) and FOL
  soundness/completeness. demand-model item 4 and the body/relationships text now use this
  lemma; thm:p03-w03-p03-068-axiomatized is referenced only as the source's statement.
  Symbol intake: added Sigma_alpha, T^-_alpha; quoted the comma-containing macro fields of three
  existing rows. unit-compile ok; fused-space clean; check.py has no finding naming -067 files.
