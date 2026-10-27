# P3 39.8 Existential pebble games and fixed-subgraph queries (packet w03a-p03-061, block 1)

## Files

- Body: `handbook/parts/p03/finite-models-definability-and-descriptive-complexity-w03-p03-061.tex`
- Annex: `handbook/annex/p03/finite-models-definability-and-descriptive-complexity-w03-p03-061.tex`
- Bib intake: `handbook/bib/intake-p03-finite-models-definability-and-descriptive-complexity-w03-p03-061.bib`
- Symbol intake: `handbook/registry/symbols-intake-p03-finite-models-definability-and-descriptive-complexity-w03-p03-061.csv`
- Placement: body after `parts/p03/preservation-abstract-logic` in `handbook/parts/p03.tex` (line 71); annex after `annex/p03/abstract-model-theory-and-lindstrom` in `handbook/annex/p03.tex` (line 9).

## Sources read this session

1. Kolaitis, *On the Expressive Power of Logics on Finite Models*, author manuscript dated 1 August 2003, 83 pp.
   URL https://dbai.tuwien.ac.at/staff/pichler/dbt/kolaitis.pdf, downloaded to
   `tmp/agent-scratch/w03a-w03a-p03-061-b1-author/dl/kolaitis.pdf`, SHA-256 digest
   2d34763a48e65afe56b26c16965812d6c6ee86a085527cbcdbe6d87608a71bed (identical to earlier scratch copies).
   Read as page images: contents pp. 1-2; Sect. 8 pp. 69-79 in full (Def. 8.1, Thms 8.2-8.3, Defs 8.4-8.6, Thm 8.7,
   Cor. 8.8, Method 8.9, Thm 8.10 with sketch, Prop. 8.11 with proof, Thm 8.12, Defs 8.13-8.14, Exs 8.15-8.16,
   Def. 8.17, Thms 8.18-8.19 with hint, closing remarks); p. 80 (start of references).
   Not the Springer 2007 printed chapter; the reader text says so once. Bib key `Kolaitis2003ExpressivePowerNotes`
   (identical entry to the one in the 055/056/058 intakes; duplicated here so the unit compiles).
2. Kolaitis and Vardi, *On the Expressive Power of Datalog: Tools and a Case Study*, undated author manuscript, 43 pp.,
   https://www.cs.rice.edu/~vardi/papers/pods90rj.pdf (SHA-256 digest ebc2e1b15b41ce78102f209397bba6961e2610bf2f37a3ae34d3fce68a5671b8).
   Full version of PODS 1990 paper; journal version JCSS 51 (1995) not read. Pages read as images: 1, 3, 4, 22
   (definition of homeomorphism, footnote 3 on node-disjointness, no-isolated-node convention); pages 20-43 seen only as
   a thumbnail grid to locate Section 6 (6.1 positive results pp. 23-27; 6.2 negative results pp. 27-40). Only p. 22 is
   cited. Bib key `KolaitisVardi1995DatalogManuscript`.

The PDF text layer of item 2 is not extractable (font encoding); pages must be rendered (pymupdf) to read.

## Source discrepancies recorded in reader text

- Ex. on p. 70: second rule of the non-2-colorability program printed with body atom O(z,y); taken as O(w,y).
- Thm 8.2 second bullet prints ∃FO^k for the fixed-point components; proved and used here as ∃L^k_∞ω.
- Proof of Prop. 8.11 (p. 76): relation list names N_3 twice; the second is P_3.
- Method 8.9 soundness: "on A and B" means A_k, B_k.
- Thm 8.19 literal second clause fails for edgeless patterns with two or more nodes; handled by the
  no-isolated-node convention (KV manuscript p. 22).
- Ex. on p. 70 speaks of "path"; the formula defines walks.

## Proof provenance

All annex proofs are written for this chapter (the source gives only hints or citations for Thms 8.2/8.3, 8.7, Cor 8.8).
The star-direction proof of the descriptive dichotomy (Spoiler strategy + directed Menger, giving
∃L^{m+1}_∞ω(≠)-definability) is original to this text, not KV's max-flow/Datalog(≠) proof. Menger (set-to-set,
directed) is proved in the annex by the edge-induction argument.

## Session 2 (this run) sources

- Kolaitis 2003 manuscript pp. 77-79 re-read this session (text layer): Defs 8.13-8.14, Exs 8.15-8.16, Def 8.17,
  Thms 8.18-8.19 with hint. Theorem 8.19 ranges over "all finite directed graphs".
- Kolaitis-Vardi manuscript pp. 23-30 read this session as page images rendered at 130 dpi: class C and the
  two dichotomies (p. 23), Thm 6.1 with proof (pp. 23-25: Q', Q_{k,l}, self-loop case), Thm 6.2 start (p. 25),
  Sect. 6.2 opening, H_1/H_2/H_3 (pp. 27-28), Lemma 6.3 with proof (pp. 28-29), switch paths and Lemma 6.4,
  start of the FHW reduction (p. 30). Pages 31-40 not read this session.

## Source discrepancy found this session

- KV p. 25: Q'_{k,l} (description and both printed rules) does not require the walk to avoid t_1..t_l, but the
  Menger step needs it. Counterexample written into reader text (def:p03-w03-p03-061-kv-program): edges
  (s,s_1),(s,t),(t,s_2) give Q'_{2,1}(s,s_1,s_2,t) but not Q_{2,1}. Fixed by inequalities x != t_i.
- Lemma 6.3 (KV pp. 28-29) defers the "B'_k fails F_2" step to an induction in FHW80; annex proves it directly
  (paths for F_1 edges meet no distinguished node other than their endpoints).

## Session 3 (block 2) sources

- Kolaitis 2003 manuscript pp. 69-77 re-read (text layer): Def 8.1, Thms 8.2-8.3 with hint, p. 71 proper-inclusion remark, Thm 8.10 with sketch (pp. 74-75), Prop 8.11 with proof (pp. 75-76), Thm 8.12 (p. 77).
- Kolaitis-Vardi manuscript pp. 30-39 and 43 read as page images (rendered earlier into tmp/agent-scratch/w03a-w03a-p03-061-b2-author/img/): switch paths and Lemma 6.4 (p. 30), construction steps (p. 31), FHW proof both directions (pp. 31-33), Def 6.5 (p. 33), phi_k and its Player II strategy (pp. 33-34), Thm 6.6 and proof (pp. 34-38), Thm 6.7 and proof (pp. 38-39). The PDF has no figure pages (no drawings on any page; p. 43 ends the references), so Figures 1-6 are not in this copy.
- Bang-Jensen and Gutin, Digraphs, corrected first edition dated 15 August 2007, free from the authors (https://www.cs.rhul.ac.uk/books/dbook/main.pdf; RHUL page checked this session). Local copy tmp/agent-scratch/w03a-w03a-p03-061-b2-author/dl2/bjg-main.pdf (772 PDF pages). Read pp. 477-480 and 482: Thm 9.2.3, Lemma 9.2.4 (p. 478, proof left as Exercise 9.4), Fig. 9.1 (p. 479), proof of Thm 9.2.3. The switch edge list in def:p03-w03-p03-061-switch was checked against Fig. 9.1 edge by edge this session.

## Source discrepancies found in session 3

- KV p. 30 lists p(b,d) as 6',2',7,9,12 and q(b,d) as 6,2,7',9',12'; in BJG Fig. 9.1 the edge leaving the head of 2' is 7' and the one leaving the head of 2 is 7. Recorded in reader text.
- KV p. 34 display of phi_2 repeats the clause not-x1 or not-x2 and omits x1 or not-x2. Recorded in reader text.

## Proof provenance (session 3)

- Switch lemma: proved via the observation that the twelve inner vertices form a directed 12-cycle (written here; the sources leave it to inspection or an exercise).
- FHW reduction, Duplicator family I_k, quotient lemma for H_2/H_3: written for this chapter following KV's plan; the family replaces KV's auxiliary formula game.
- Thm 8.10: full proof via the least fixed point W of the Spoiler-forcing operator; program pi_B extended to constants.
- Prop 8.11: Horn 3-SAT P-completeness used as an input (not proved); log-space computability and composition argued in the annex.

## Continuation

State after block 2 (session 3):

- Hard guard fixed: sec:p03-w03-p03-061-switches and thm:p03-w03-p03-061-dichotomy now exist; unit-compile ok.
- Written: walks (thm), system (def+thm, Kolaitis Thm 8.2 general), proper inclusion (thm), spoiler-lfp (thm, Thm 8.10) with def program-b, horn-complete (Prop 8.11), switches section (switch, fhw graph, templates, fhw, A_k/B_k, family, h1, quotient, h2h3, dichotomy, phi1 example, limit warning), refines lemma; all with annex proofs.
- Still open: patterns with loops (Kolaitis Thm 8.19 over all finite digraphs); Thm 8.12 reported only; Horn 3-SAT P-completeness used as cited input.
- Driver insertion still pending (lead).

## Author correction and boundary completion, 2026-10-26

The examples now describe m pairwise vertex-disjoint directed edges rather
than parallel edges: the declared graph vocabulary has a binary edge relation
and does not encode multiedges. Statements about the unrestricted infinitary
logic now identify the open status as the 2003 manuscript's report, not a
verified claim about later literature.

A new theorem and reciprocal annex item, suffix single-loop, settle one exact
boundary. If a loop edge is realized by a positive-length simple directed cycle
through its named vertex c (a self-loop counts as length one), the unary Datalog
rules R(x) :- E(c,x) and R(y) :- R(x),E(x,y), with output R(c), define the query.
Stage induction identifies positive walks; a shortest positive closed walk
through c has no repeated internal vertex. The explicit two-variable unfolding
proves existential infinitary two-variable definability. This is a direct
derivation, not an attributed source classification. It shows why the existing
loopless non-star dichotomy cannot simply be asserted for loop patterns under
that convention. It does not classify all patterns with loops or close the
broader original-source requirement.

The Horn encoding now normalizes empty clauses to a fixed contradiction and
adds an unused variable, preserving satisfiability and guaranteeing a nonempty
structure for an empty conjunction. The homomorphism proof and logspace
reduction explicitly cover these cases. The rules, template sequences and
quantifier-substitution chain have readable line breaks without changing their
mathematical content. In particular, formerly missing row breaks in the
Spoiler fixed-point displays were repaired.

The symbol intake has valid CSV quoting, a corrected stage-formula scope, and
local entries for R and rho_n in the new example. Related intake-only syntax
repairs were made in 056 and 074; 058 proof-local first-use anchors were corrected
and Phi/Phi_0/Theta separated by their actual origins. No new bibliography key
was introduced. The parent integrator owns canonical merging and citation alias
resolution.

Verification: all 11 assigned packet body/annex pairs have balanced environments
and all proved-status targets have reciprocal annex items; all 11 intakes parse
as seven-column CSV. These are structural checks, not mathematical acceptance.
The final 061 scoped TeX Live build completed pdflatex/biber/pdflatex/pdflatex and
produced 55 pages. Overfull warnings fell from 38 to 29; those remaining still
require the book-wide layout pass. Changed pages 11, 18, 22, 46 and 54 were visually
inspected. External references in a unit build do not establish integrated
cross-reference resolution. Packet 063 was checked and rebuilt successfully
(21 pages, 3 overfull warnings), but its final bytes match the pre-edit snapshot:
an initially suspected omitted proof was already present and is not credited
as new work. No independent review, full-source completion, admission, or book
completion is claimed.

