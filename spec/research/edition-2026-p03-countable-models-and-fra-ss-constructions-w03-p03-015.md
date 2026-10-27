# w03a-p03-015 (P3, 26.4): finite-signature application and random-graph types

## Scope taken from the packet

Packet work/waves/w03a/packets/w03a-p03-015.json, block 1. Gaps addressed in the given order:
N-a-001-MAP-05 (random-graph finite-type example as an instance of the corrected application),
ED26-SRC-048-0017-C061 (corrected p. 352 application at its stated scope, constants allowed), then
the source-specific duties (N-a-001-C01, MAP-03, MAP-06, the other ED26-SRC-048-0017 corrections).
Unit ED26-SRC-048-0007 is read-only (owner w03-p03-007).

## Sources read in this session

- Hodges corrigenda, held PDF tmp/edition-2026-catalog-src038/tail-039-068/SRC-048-hodges-corrigmt-2026-09-09.pdf,
  all six pages via pdftotext. Locators used in the reader text: corrigenda p. 3, correction to book p. 352
  l. -16 (add "with no function symbols" after "finite signature"); corrigenda p. 1, correction to
  Corollary 2.7.6 on book p. 72 (separate clauses for constant symbols and for function symbols).
- Online, 2026-10-11: Cambridge Core landing page for Hodges 1993 chapter 7 (doi 10.1017/CBO9780511551574.009,
  pp. 323-359): purchase/subscription only; no body read. Web searches for Ryll-Nardzewski 1959, Svenonius 1959
  and Engeler 1959 found only bibliographic records, a JSL review and PhilPapers metadata; no legitimate copy.
  Earlier attempts are recorded in spec/research/p03-ryll-nardzewski-source-note.md (RCIN closed access,
  AMS 403, Wiley paywall).

No statement or proof is attributed to the Hodges book body. The reader text says the application is stated
in its own formulation and is not a reading of the textbook page.

## Existing treatment found

- n-a-001-01.tex: general criterion (MAP-01, MAP-02), DLO calculation (MAP-04), relational application
  without constants (thm:p03-rn-relational-application), (Z,s,t) boundary (thm:p03-rn-function-boundary).
- fraisse-1954.tex: extension axioms, graph limit and its categoricity (no type calculation);
  relational categoricity boundary with the countable-signature counterexample.
- classification-theory.tex thm:p03-random-graph (cited statement).
- Not in the packet's list: restoration/inherited-06138-06242.tex lem:iso-invariance (used for automorphism
  invariance; the P3 thm:p03-isomorphism-invariance label is not on the current input route).

## Notes on the mathematics

- Application theorem: finite L, relation and constant symbols, no function symbols; M countably infinite and
  ultrahomogeneous for finitely generated substructures. Equal atomic patterns give a substructure isomorphism
  (term-value map, constants fixed), hence an automorphism; QE by pattern disjunctions; patterns isolate and
  biject with S_n(T); categoricity via thm:p03-rn-characterization. Empty generated set handled explicitly.
- (Z,s,t) is ultrahomogeneous in the finitely-generated sense and not omega-categorical: the "no function
  symbols" correction is necessary.
- Random graph: graph patterns (equality partition + simple graph on classes); realization by the extension
  axioms in every model; finite partial isomorphisms preserve all formulas (one-point extension by the
  extension axioms); counts sum_k S(n,k) 2^{k(k-1)/2} = 1,1,3,15,127 for n = 0..4; orbits; instance of the
  application by matching atomic patterns with graph patterns; named vertex (one constant) gives
  |S_n| = |Gamma_{n+1}|.

## Open items

- N-a-001-C01, MAP-03, MAP-06: original bodies not held (blocked_source).
- ED26-SRC-048-0017-C061: application inside a reader treatment of Hodges p. 352 (body not held; unit 0007
  owned by w03-p03-007).
- Other ED26-SRC-048-0017 corrections: the corrected Hodges pages are not held; target units owned elsewhere
  or unallocated.
- Existence of Fraisse limits with constant symbols is not proved in the handbook; the application is stated
  for any countably infinite ultrahomogeneous structure, which covers every infinite limit.

## Continuation

Block 1 wrote the chapter body and annex, symbol intake (8 rows), an empty bib intake (no new keys) and the
return JSON. Checks: unit-compile ok with 0 overfull; check.py filtered to these files shows no findings;
find_fused_spaces no hits. Next block: nothing further is writable without the source bodies; if the
Hodges 1993 chapter 7 or the 1959 originals become held, write the source-specific presentations and the
MAP-06 comparison.
