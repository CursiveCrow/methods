# CDCL/UIP/watched-literal authoring packet

Date: 2 October 2026 local; edition source cutoff 7 September 2026.
Standing: authored mathematical packet, unreviewed and not admitted. This
single note records scope, primary manifestations and remaining source duty;
it is not a coverage receipt, source ledger or completion percentage.

## Scope and preserved queue identities

The exact current-fulfillment rows 248.2, 248.3 and 248.4 were read by
stream-filtering `current-fulfillment/p11-p12.jsonl`. Their source facets were
then stream-filtered in the frozen `completion-work-queue.jsonl`; no rebaseline
or queue mutation occurred. The pertinent original allocations are:

- `ED26-REQ-N-c-032-01`: GRASP 1999, conflict graph, learning and
  nonchronological backtracking; `MarquesSilvaSakallah1999`, IEEE TC 48(5),
  506–521, DOI 10.1109/12.769433.
- `ED26-REQ-N-c-032-02`: Chaff 2001, watched-literal events/update invariants
  and branching; `MoskewiczEtAl2001`, DAC 2001, 530–535,
  DOI 10.1145/378239.379017.
- `ED26-REQ-N-c-032-03`: the SAT 2003 MiniSat contribution published in
  2004, 502–518, DOI 10.1007/978-3-540-24605-3_37. Its original publication
  is not equated to the retrieved extended version 1.2.
- `ED26-REQ-N-c-032-04`: final 2009 CDCL handbook chapter, 131–153,
  DOI 10.3233/978-1-58603-929-5-131. Its original final manifestation is
  not equated to the retrieved manuscript marked 2008, 127–149.
- `ED26-REQ-D-P11-001-01`: the composite goal, especially its exact
  GOAL-01/GOAL-02 state, analysis, propagation and heuristic obligations.
- `ED26-SRC-051-0004`: the distinct 2021 CDCL chapter, 133–182,
  DOI 10.3233/FAIA200987. Publisher metadata was read; its body was not
  acquired or reconstructed in this block.

Other facets of these rows remain separate: N-c-032-05 is the already frozen
DRAT packet; N-c-033-01/-02/-03 and the 2021 handbook chapters 3, 5, 6, 8,
9, 11, 12, 13, 14, 16 and 17 are not discharged by this CDCL core. The
inherited U00944–U00949 restoration facets are not replaced or counted as new
source credit. The inherited current SAT chapter was already read in the
preceding block; its CDCL vocabulary is the bounded interface this packet
expands, not an independent full algorithm proof.

## Actual primary captures and reading

Three intact PDF captures are preserved in `source/references/p12-cdcl-uip/`:

1. `cdcl-2009-course-hosted-author-manifestation.pdf`, SHA-256
   `500CE9CB7E8B0FE9015F64B65C3263DF088A7EE97132029D88483854A40B7B1F`.
   [Public university-hosted primary chapter](https://ics.uci.edu/~dechter/courses/ics-275a/winter-2016/readings/SATHandbook-CDCL.pdf).
   It explicitly displays IOS Press 2008, pages 127–149, and contains 23
   pages. All 23 were read: web extraction for the notation/introductory
   pages, then local text extraction of pages 6–16 and 12–23, with pages
   17–18 reread separately after output truncation. Controlling locators:
   §4.2 reasons/levels; Algorithm 1; §4.4 equations (4.16)–(4.18),
   Examples 4.2.4/4.4.1–4.4.3 and Tables 4.1–4.2; §4.5.1 lazy structures,
   §4.5.2 restarts, §4.5.3 activity, §4.5.4 deletion. This filename does
   not establish equivalence to final 2009 pages 131–153 or to 2021.
2. `chaff-dac2001-v56-author.pdf`, SHA-256
   `305124C23462E58AFD1826DC1403082F479DA78676465BC7CFD65A43613ADDF1`.
   [Chaff author PDF](https://www.princeton.edu/~chaff/publication/DAC2001v56.pdf),
   six pages, linked as v5.6/RC2 by the official developer page. All six
   were read: web-extracted §§1–4, then local pages 4–6 including the
   remainder, Figure 1 and tables/references. Invoked locators: §2 watch
   event cases and no-rollback claim, §3 literal-polarity VSIDS counters,
   §§4.1–4.2 scheduled deletion and restart qualifications. Its empirical
   speed comparisons are not promoted to general guarantees or reproduced
   as experiments by this packet.
3. `een-sorensson-extended-1-2.pdf`, SHA-256
   `53197DBD783C924A2627D75E305706297988494265BD5E5EC873840E5D797AC4`.
   [Official MiniSat author download](http://minisat.se/downloads/MiniSat.pdf),
   explicitly “extended version 1.2”, 23 pages. The HTTPS endpoints had
   certificate-name mismatches; the original public HTTP route supplied the
   PDF without disabling validation. All 23 pages were read in local ranges
   1–9, 10–16, 17–19 and 20–end. Some embedded-font extraction omits letters
   in prose/identifiers; the semantic algorithms and displayed figures were
   read with the official web extraction as a cross-interface aid, not a
   claimed pixel inspection. Controlling locators: §§3–4; Figures 7–9
   Clause.propagate/constructor/enqueue and interrupted-list restoration;
   Figures 10–11 reverse-trail analyze and assertion record; Figure 12
   cancellation; Figure 13 search; Figure 14 activity; Figure 15 locked
   deletion; Figure 16 top-level/incremental root-level handling. The final
   Satzoo appendix is a distinct strategy comparison, not MiniSat's own
   proved core or an adopted extra implementation.

No source bytes were edited. No source visual inspection, manuscript render,
solver execution, test suite, package installation or build is claimed.

The GRASP author-deposit route
[Southampton primary PDF](https://eprints.soton.ac.uk/262032/1/jpms-tcomp99.pdf)
returned a bot challenge/403 and no body capture; no challenge was bypassed.
Its institutional record and publication identity were read, not its full
paper. The 2021 publisher route
[IOS Press chapter](https://ebooks.iospress.nl/DOI/10.3233/FAIA200987)
returned guest metadata, abstract, authors and pages but not the body. Author
publication-list and legitimate public-route searches did not provide that
chapter body. No paid access or access-control circumvention was used.

## What was actually authored

Reader: `handbook/parts/p12/cdcl-uip-and-watched-literals.tex`, anchor
`sec:p12-cdcl-uip-and-watched-literals`. Annex: matching file under
`handbook/annex/p12/`. Six complete reciprocal result/proof pairs:

- `local-sound`: semantic unit propagation, ordered reasons and resolution
  entailment, including empty/tautological clauses.
- `analysis`: decreasing reverse-trail first-UIP construction, availability
  of every reason, false/non-tautological intermediates, domination and
  downstream-most UIP argument, unit assertion and minimal backjump level.
- `watch-correct`: exact forward event/update procedure, finite queue,
  units/binary clauses/tautologies, live lists and interruption restoration,
  fixed-point completeness and no-watch-restoration proof for whole-level
  backtracking. The event invariant includes in-progress list references.
- `search-correct`: SAT/UNSAT soundness and model preservation; actual
  learned-clause novelty derived from the watch invariant, not assumed;
  finite-clause termination/completeness for no forgetting/no voluntary
  restarting, plus conflict-charged retained-learning restarts. Arbitrary
  restart/forgetting remains outside that theorem.
- `activity-scale`: exact-real correspondence of eager decay, growing lazy
  increments and common positive rescaling. It proves no floating-point or
  performance claim.
- `lookahead-sound`: failed-literal and shared two-branch consequences,
  explicitly prefix-relative unless assumptions are kept in a global clause.

All pairs use `thm:p12-cdcl-uip-...` / `annex:p12-cdcl-uip-...`, with full
proof bodies only in reciprocal annex items. They concern general finite CNF,
not a bounded-width or small-instance substitute. The worked source trace
retains x_21/x_31 and source levels 2/3/5, works both selected-resolution
orders and the decision-boundary versus first-UIP clauses, and verifies the
backjump/assertion. A separate general-data-structure failure example derives
a three-literal learned clause and shows missed propagation after an
incorrect second watch; a restart-before-progress example gives an infinite
sound run on a satisfiable input.

The source reason-max level formula and MiniSat enqueue-current-level policy
are separately stated. Chaff's false-literal-indexed lists are explicitly
bridged to MiniSat's true-complement event indexing. The core retains learned
units as root facts and keeps original clauses; this is not a claim that the
extended MiniSat implementation's special unit storage, simplifyDB,
incremental root-level handling or arbitrary-constraint API is identical.
Chaff literal-polarity counters, MiniSat variable/clause activity and old
handbook restart/deletion policies retain their separate attribution.

Bibliography intake has three manifestation records:
`handbook/bib/intake-p12-cdcl-uip.bib`. Symbol intake:
`handbook/registry/symbols-intake-p12-cdcl-uip.csv`. Root must bind the genuine
local u-marker/u-variable and literal/variable roles, and local score roles,
without house renaming. No shared driver, canonical record, map or receipt
was edited. Suggested seam: the new chapter after SAT Search and Certificates
and before the frozen DRAT chapter; the matching annex after the DPLL fragment
and before the DRAT proofs.

## Remaining duty and verification standing

Author mathematical rereading and direct tracing of the worked conflicts are
not independent review. Static/build/render and the consolidated independent
source/topic/publication reviews remain pending. The general algorithm/proofs
are authored; the exact final GRASP 1999 body, original MiniSat 2004/version
relationship, final 2009/manuscript relationship, and 2021 CDCL chapter body
remain source-specific acquisition/reconstruction duties. The broad original
allocations and all additional 2021 chapter components are not marked
fulfilled merely from these related primaries or six new proofs. In particular
this packet does not close the whole 2021 CDCL chapter, the other SAT handbook
source facets, or the nineteen-part/289-chapter/2,475-section/615-requirement
manuscript goal.
