# Original GRASP/MiniSat source presentation packet

Date: 3 October 2026 local. Edition source cutoff: 7 September 2026.
Standing: authored, not independently reviewed, admitted, built or manuscript-
rendered. This is a source/correction note, not a coverage ledger or receipt.

## Exact allocated scope

The frozen queue was stream-filtered only for `ED26-REQ-N-c-032-01` and
`ED26-REQ-N-c-032-03`, including their actual required components and source
presentations. The former allocates GRASP 1999 conflict graph, learning,
nonchronological backtracking and derivation; the latter allocates the final
SAT 2003 contribution published in 2004, propagation/conflict/extensibility
architecture. Their MAP-01/MAP-03 and the relevant composite D-P11-001
facets remain the intellectual identities; no rebaseline or source-credit
summation was performed. The current general CDCL chapter and its source note
were reread. It and the DRAT packet were left frozen; no new source-original
credit is assigned to their old wording merely because it treats related ideas.

## Newly held actual original bodies

1. `source/references/p12-grasp-minisat-originals/marques-silva-sakallah-1999-published.pdf`.
   SHA-256 `CE48CD433DD8FD1BC296C6E4B1E87C571FAAE0F1C42451736B1D5703E8AD05BB`.
   [Public Berkeley primary-paper route](https://people.eecs.berkeley.edu/~alanmi/courses/2005_290A/papers/grasp.pdf).
   Publication-form article, sixteen pages with journal pagination 506–521,
   IEEE Transactions on Computers 48(5), May 1999; title/authors/journal
   headers/native figures and appendix verified in the actual bytes. The
   separately identified DOI is 10.1109/12.769433. This successful alternative
   route was not a replay of the unchanged blocked Southampton route, and no
   bot challenge or access control was bypassed.
2. `source/references/p12-grasp-minisat-originals/een-sorensson-sat2003-published2004.pdf`.
   SHA-256 `58E68ED539B209BEFDCEC4AAC580C44D497EC7A18E860004501C9F6C7DC72C43`.
   [Public EPFL primary-paper route](https://lara.epfl.ch/w/_media/projects/minisat-anextensiblesatsolver.pdf).
   Publication-form contribution, seventeen printed pages 502–518, LNCS 2919,
   SAT 2003 selected revised papers, copyright Springer-Verlag Berlin
   Heidelberg 2004. Actual first-page footer/title/authors and last-page
   pagination verified. DOI 10.1007/978-3-540-24605-3_37 matches the publisher
   bibliographic identity. The first-page footnote explicitly directs the
   reader to an extended version; it is not the captured 23-page extended
   version 1.2 from the previous packet.

All sixteen GRASP pages and all seventeen published MiniSat pages were read
from actual source text. GRASP ranges were read in overlapping 1–8, 3–8,
9–16 and 13–16 passes; overlap repaired truncated display output. MiniSat
1–8 and 9–17 text passes were supplemented by actual page pixels because
the code font extracts as control characters. Existing bundled Poppler rendered
only these source PDFs, not the manuscript. Pixels inspected: GRASP PDF pages
5–9 and 15 (printed 510–514 and 520); published MiniSat PDF pages 1–16
(printed 502–517), including every native code figure. The last references
page 518 was read as text. The primary PDF bytes were not edited.

Source page PNGs are retained in the same owned source directory; they are
inspection derivatives, not source editions or manuscript render evidence.
Poppler emitted font warnings; the inspected native equations and code were
readable. An attempted existing Python renderer was unavailable (`fitz`
missing); nothing was installed. Source rendering then used the already
bundled Poppler runtime.

The held extended-v1.2 PDF was reread only at its relevant constraints and
enqueue pages (8 and 14) and visually inspected from two additional source
derivatives in this packet's folder. Its unchanged SHA-256 remains
`53197DBD783C924A2627D75E305706297988494265BD5E5EC873840E5D797AC4`.
No whole-program version equivalence was inferred from those comparisons.

## Verified source distinctions and corrections

GRASP §§2–3 use antecedent assignment sets, Lambda/Sigma cause expansion,
same-frame FDA and highest-cause-level CDB. These are not the later generic
first-UIP second-highest-level backjump algorithm. The original Figure 1
nine-clause example and its FDA/second-conflict Figure 4 are worked in full,
retaining x_9/x_10/x_11/x_12/x_13 and source levels 1/2/3/6.

The original source has consequential mathematical/interface discrepancies,
which are stated rather than silently “preserved” as proved:

- GRASP Eq. (1) is a reason-max level formula, whereas Figure 3 explicitly
  sets delta(x)=d; its FDA Appendix Definition 4 needs antecedents below
  the assertion level. The operational original-engine reconstruction uses
  the current-frame annotation, preserving reason-max as a separate source
  convention. Figure 2's zero-start frame token and the prose's first-level-one
  convention are not declared identical. The full Search proof states checked
  root deduction, fixed assumptions and positive decision-frame convention;
  it is not a theorem about an unspecified compiled zero-based wrapper.
- GRASP Eq. (9), interpreted with Eq. (8)'s two-argument operation, swaps
  the support/output roles. The corrected forward UIP construction explains
  a downstream node from an upstream stopping UIP, negates the support and
  appends the downstream true literal. Appending the stopping UIP's own
  literal instead is tautological. The terminal support starts at the
  conflict and stops at the final UIP. Both actual source example clauses
  are proved. No universal size-superiority claim is asserted without its
  own proof.
- GRASP Appendix Theorem 3 says the false function has no prime implicates
  while using its empty clause in the complete product. Under the explicitly
  stated literal-subset definition the empty clause is its unique prime
  implicate. In the satisfiable case the printed direction “psi implies
  prime omega” is reversed: an entailed prime subclause omega implies psi.
  The new complete-product theorem supplies the complete corrected argument,
  including false/true/zero-variable/compatible-prefix cases.
- Published MiniSat p. 508 Simplify prose reverses True/False relative to
  Figure 4 (p. 510) and Figure 9 (p. 517). The operative protocol follows
  the actual caller: True means satisfied/remove, False means keep after
  in-place simplification. Extended 1.2 p. 8 uses this latter prose convention.
- Published MiniSat Figure 6 clears propQ inside opposite enqueue before
  returning False. Extended 1.2 Figure 9 lacks that local clear; its outer
  propagation clears on callback failure. This is an actual local code
  difference even if common caller paths eventually have the same effect.
- Published Figure 5 moves ps to c.lits and then still indexes ps. Its
  abstract Vec transfer semantics are not supplied. For a clearing transfer,
  subsequent watch selection/bumping must use c.lits; otherwise a valid
  non-clearing ownership convention must be specified. This is kept as an
  implementation dependency, not mislabeled a verified original binary.

Original MiniSat has nine grouped code figures and no Satzoo appendix; the
23-page extended version has additional ADT exposition, exercises and that
appendix. The published callback semantics, absolute-root/query-root
distinction, original queue clearing and grouped Figures 7–9 are independently
written here. The general CDCL theorem supplies only the bounded reason/watch
bridge under its actual hypotheses, not source-version equality.

## Authored reader/proof/interface artifacts

Reader: `handbook/parts/p12/grasp-and-minisat-originals.tex`, anchor
`sec:p12-grasp-and-minisat-originals`. Annex: matching filename under
`handbook/annex/p12/`. Six complete reciprocal pairs:

1. `grasp-causes-sound`: finite graph recursion, cause sufficiency and learned
   implicates, with induction through earlier FDA reasons.
2. `grasp-standard-search`: root-relative standard Search soundness,
   FDA/CDB pruning, at-most-two-attempt frame progress, termination and
   model-extension completeness at the explicitly declared initialization.
3. `grasp-uip-links`: endpoint-correct UIP support/output clauses and native
   two-clause example, with domination and reason induction.
4. `grasp-complete-product`: blocking-assignment prime-subclause construction,
   unit-saturated compatibility and the empty/true cases.
5. `minisat-original-reason-bridge`: Boolean predicate callback explanations
   yield input-entailed clauses; chronological/undo/event-coverage premises
   establish sound learned clauses and total/query-root conclusions.
6. `minisat-original-query`: G and the relatively simplified F' preserve F;
   temporary H gives only F-and-H SAT/UNSAT, and a budget exit is undefined.

All use full annex proofs, no body proof environments. The original MiniSat
reason-expansion example from p. 513 and a concrete assumption-query misuse
boundary are worked. Native API/state/callback names, flags, locked-clause
deletion, search budgets and original strategy constants are supplied without
claiming the source experiments as new measurements.

Intakes: `handbook/bib/intake-p12-grasp-minisat.bib` contains two captured-
manifestation records, leaving existing canonical keys untouched;
`handbook/registry/symbols-intake-p12-grasp-minisat.csv` preserves all local
typed source roles including GRASP X as an unassigned marker, source plus/sum
as disjunction, and MiniSat bottom as undefined. Root owns canonical merges,
scope bindings, drivers, maps and receipts. Suggested seam: after the general
CDCL chapter and before the DRAT chapter, with annex in the corresponding
order. No shared or frozen-packet files were edited.

## Exact remaining duties

The previously unheld original bodies are now held and read. Source and
mathematical corrections are authored but not independently accepted. The
source's red/green space-bounded engine has its native policy stated; its
full variant correctness/space theorem is not inferred from the standard
retained-engine proof. Literal compiled-implementation correctness, precise
ownership semantics, floating-point execution and default heuristic liveness
are not established by this packet. Original empirical tables/experiments are
not reconstructed as an independent benchmark study. The full 2009/2008
handbook-version bridge, 2021 CDCL chapter, and other allocated whole handbook
chapters remain separate duties. No full original-source/whole-book closure
is claimed from related algorithm coverage, titles or the six new proof pairs.

Author rereading and direct mathematical source/example checks are not a
consolidated source/topic/publication review. No children, reviewers, tests,
solver run, build, manuscript render, installation, generated navigation,
ledger or receipt edit was performed. Root integration and later independent
static/build/visual admission remain pending. The nineteen-part, 289-chapter,
2,475-section, 615-original-requirement manuscript goal remains owed.
