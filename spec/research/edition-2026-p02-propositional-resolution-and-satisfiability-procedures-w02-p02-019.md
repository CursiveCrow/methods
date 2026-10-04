# w02-p02-019: Horn-SAT, 2-SAT and propositional decision complexity (P2 15.5-15.7)

## Provenance

- Packet: work/waves/w02/packets/w02-p02-019.json (label_tag p02-w02-p02-019).
- New body file: handbook/parts/p02/propositional-resolution-and-satisfiability-procedures-w02-p02-019.tex
- New annex file: handbook/annex/p02/propositional-resolution-and-satisfiability-procedures-w02-p02-019.tex
- Patch requests for the read-only host and drivers: work/waves/w02/patches/w02-p02-019.json
- All procedures and proofs are written from the inherited definitions
  (sec:prop-syntax-semantics-01, -02, -04; lem:prop-coincidence;
  lem:prop-clause-satisfaction) and the complexity convention
  def:p02-complexity-standing / def:p02-sat-taut. They are not presented as
  reconstructions of a named source's algorithm.

## Held sources opened in this session

- AspvallPlassTarjan1979: source/references/acq-r1-ACQ-2026-10-0014/aspvall-plass-tarjan-1979-linear-time-2sat.pdf
  (IPL 8(3), printed pp. 121-123). Locators used and seen: graph G(F) with
  2n vertices and 2|C| edges, unit clause u read as u v u, random access
  machine (p. 121); Theorem 1 (SCC criterion) and the satisfiability marking
  of components in reverse topological order (p. 122); O(n+m) bound with m the
  number of edges (p. 123).
- AroraBarak2009: source/references/acq-r1-ACQ-2026-10-0012/arora-barak-2009-computational-complexity.pdf.
  The held file is the web draft dated 2007-01-08, not the 2009 printing.
  Numbered items seen: Theorem 2.10 (Cook-Levin; SAT there is satisfiable CNF
  formulae, 3SAT also NP-complete), Definition 2.21 (coNP), Definition 2.22
  (coNP, certificate form), Example 2.23 (TAUTOLOGY coNP-complete via the
  negated Cook-Levin formula). Only these numbers are used as locators.
- DowlingGallier1984 (cited at thm:p02-horn-sat) is not held; no
  source-specific content of it is written. The Horn procedure is derived
  from the definitions.

## Existing treatments found (A9)

Listed in packet and read: supplement 198-323 (sec:p02-prop-decision-complexity,
def:p02-tractable-classes, thm:p02-horn-sat, thm:p02-dual-horn-sat,
thm:p02-two-sat, thm:p02-xor-sat, tab:p02-tractable-sat); annex:p2.3.12;
annex:p04.dh.two-sat (criterion and rank extraction); annex:p14.dc.horn (least
closure for the circuit instance); annex:p14.dc.finite-cpl;
parts/p12/sat-and-certificates.tex; parts/p09/presentations/n-c-026.tex 6-157
(complete Cook-Levin reconstruction, on route via
parts/p09/logic-in-computer-science.tex line 2529); parts/p04/complexity.tex
227-238 (thm:p04-cook-levin, cited).

Found and not listed in the packet's existing list:
- handbook/parts/p04/decision-problem-hardness.tex line 119
  (thm:p04-dh-two-sat, NL-completeness of 2SAT) - linked, not duplicated.
- handbook/parts/p02/herbrand-methods-unification-and-first-order-w02-p02-028.tex
  line 277 (thm:p02-w02-p02-028-resolution, a statused proved refutational
  completeness theorem written by another packet, not yet on route) - relevant
  to S-019-C03.
- handbook/restoration/inherited-08248-08305.tex lines 9-14
  (thm:fol-validity-undecidable, Status: cited theorem, Church1936/Turing1937)
  and the unlabelled corollary at lines 20-23 (c.e. but undecidable,
  Status: complete proof) - S-019-C02.
- handbook/parts/p02/tseitin-transformation.tex (thm:p02-tseitin,
  equisatisfiability) - linked in the SAT/equivalence warning.

## Decisions

- Cost model for the linear bounds: unit-cost random-access machine on
  normalized variable indices 1..n, as APT p. 121 state for their bound. The
  renaming from arbitrary variable names is stated as an input convention and
  its cost is named in the limitation warning.
- SCC algorithm: two-pass depth-first search (finishing order on G, then trees
  of the reverse graph in decreasing finishing order). Chosen because its
  correctness proof is short and complete; APT use Tarjan's one-pass
  algorithm, which is not held, so it is mentioned only through APT p. 122.
- Extraction rule: p true iff idx(p) > idx(not p), where idx is the order in
  which pass 2 outputs components (a topological order of the condensation).
  This is the rank argument of annex:p04.dh.two-sat specialized to that rank.
- TAUT: coNP-completeness is derived from SAT NP-hardness by the
  negation maps and complementation of reductions.

## Continuation

State at return (block 1):
- Body and annex written for 15.5, 15.6, 15.7 (Horn, 2-SAT, truth tables,
  SAT in NP, TAUT coNP-complete, SAT/validity/equivalence warning).
- Patch requests 1-9 in work/waves/w02/patches/w02-p02-019.json.

State at return (block 2):
- 15.7 / S-019-C03, C04: new subsection sec:p02-w02-p02-019-first-order-boundary
  (body 677-737) with thm:p02-w02-p02-019-fol-resolution, status
  cited=Robinson1965, cited in text as \cite{Robinson1965,BachmairGanzinger2001}.
  Its statement has the hypotheses and conclusion of thm:fol-resolution
  (restoration/inherited-05568-05923.tex 329-334); the prose identifies it with
  that theorem, names its proof-sketch dependencies (soundness theorem,
  thm:herbrand-clauses [cited], thm:prop-resolution-complete,
  thm:resolution-lifting [cited]) and gives the one-sided-search contrast with
  thm:fol-validity-undecidable and thm:fol-validity-enumerable.
  Robinson1965 is not held (acquisition ACQ-2026-10-0421 failed, HTTP 403);
  BachmairGanzinger2001 is not held (only the 1991 MPI report,
  BachmairGanzinger1994, is). So no locator is given on either citation; the
  locators remain open (Robinson 1965 pp. 23-41, the completeness theorem;
  Bachmair-Ganzinger 2001 handbook chapter, its refutational-completeness
  theorem).
  Status chosen: cited, because the in-book argument rests on two cited
  theorems. A complete proof (unification, lifting, Herbrand) exists in
  handbook/parts/p02/herbrand-methods-unification-and-first-order-w02-p02-028.tex
  (thm:p02-w02-p02-028-resolution, another packet, not on the driver route at
  this time); it is not referenced from reader text, to avoid an unresolved
  reference. If the lead routes it, the cited status here can be re-pointed.
- Patch request 10: status line inside thm:fol-resolution in the restoration
  capture (lead-only host), referring to the new statused theorem.
- 15.6 / A-030-C02 (XOR): new subsection sec:p02-w02-p02-019-xor (body
  434-517): convention def:p02-w02-p02-019-parity-input (dense m x (n+1)
  presentation), method def:p02-w02-p02-019-gauss-method (Gauss-Jordan over
  the two-element field), theorem thm:p02-w02-p02-019-xor (correctness,
  t <= min{m,n} pivots, at most t(m-1)(n+1) field operations, O(mn+m+n) other
  steps, m=0 and n=0 cases), example def:p02-w02-p02-019-xor-example; proof
  annex:p02-w02-p02-019-xor (annex 332-417). Written from the definition of
  def:p02-tractable-classes only; Schaefer1978 (cited at thm:p02-xor-sat) is
  not held and nothing source-specific is attributed to it.
- Patch request 11: pointer from thm:p02-xor-sat to the new method, theorem
  and annex.
- Checks: unit compile ok (4 overfull, all in the typeset bibliography);
  find_fused_spaces clean; check.py --tree shows no finding on these files.
- Guard G1 list (spec/research/edition-2026-p02-unit-accounting-w02-p02-042*,
  -044*, -045*, completeness-choice-scope-w02-p02-054*): these files belong to
  packets w02-p02-042, 044, 045 and 054 and were not written or modified in
  this packet's sessions; they were left untouched.
- Next block, if any: after the lead applies the driver inputs and patch
  requests, re-check that all external references resolve in the full build.
