# Immerman 1986 ordered-capture presentation

Assignment `ED26-REQ-N-c-004-03`, components `N-c-004-MAP-03` and
`N-c-004-MAP-05`. Read the exact completion queue row, current common
`handbook/parts/p09/presentations/n-c-004.tex`, and the source allocation in
`spec/research/p09-source-presentations-lot1.md:556-602`, plus the handbook
conventions and current edition contract. The separate Vardi1982, Fagin1974,
Fagin1976 and Immerman1999 treatments remain untouched.

## Actual held source and qualification

Neil Immerman, *Relational Queries Computable in Polynomial Time*,
*Information and Control* 68(1-3), 1986, pp.86-104,
DOI `10.1016/S0019-9958(86)80029-8`. The
[author's publication index](https://people.cs.umass.edu/~immerman/pub_immerman.html)
links [query.pdf](https://people.cs.umass.edu/~immerman/pub/query.pdf) under
that journal work and separately identifies the 1982 preliminary version.
The [publisher record](https://www.sciencedirect.com/science/article/pii/S0019995886800298)
confirms the journal metadata and open-archive designation in indexed text.
The publisher page/PDF fetch returned HTTP403; it was not repeatedly retried.

The author URL initially failed with HTTP503 through web retrieval. Direct
acquisition succeeded and the subsequent author-index link also rendered the
PDF. Local file `source/references/p09-immerman1986/query-author-copy.pdf`,
473987 bytes, SHA-256
`f47e9e244634e413b2e5eb5c0183fa1e06150184ce9f0a6eaae92ef5fd204a6c`.
The PDF is an author-typeset 18-page copy, labelled on its first page as the
1986 Information and Control article, with its own pp.1-18. It is **not**
described as an original journal facsimile. Identity is based on the author's
publication link, internal bibliographic header, section/theorem identities
and actual selected body, not a matching filename alone. A publisher
facsimile's byte identity and pagination have not been independently checked.

The complete selected sections 1-3 were read: author pp.2-8, including query
syntax, positivity, Constant Assumption, Facts2.1-2.2, the hierarchy notation,
Theorem1, Lemma3.1 and the transition/readout formula. Page images for author
pp.1,3,5,7,8 were inspected to recover corrupted mathematical text. Journal
pp.87-93 are the existing selected locator evidence, not falsely represented
as the local PDF's page numbers. Research skill was applied locally because
the assignment forbids children; PDF skill was applied only to source pages.

## Authored source-specific mechanism

Body: `handbook/parts/p09/presentations/n-c-004-03.tex`, label
`sec:p09-n-c-004-03`. Annex:
`handbook/annex/p09/n-c-004-03.tex`, label
`sec:annex-p09-n-c-004-03`. Disjoint intakes are
`handbook/bib/intake-p09-immerman1986.bib` and
`handbook/registry/symbols-intake-p09-immerman1986.csv`.

The construction retains the actual 1986 features: the language L_mu and
its source binder; the printed binary E initial row with n² bits followed
by n³-n² blanks and letter codes0..4; one (2k+1)-ary cell/time/letter
relation; the finite neighborhood quadruple set delta_M; its three
positive previous-row atoms; and the final first-position/last-time
accepting-letter readout. Footnote3's independent position, time and
alphabet recodings make c0 the appropriate argument in each coordinate.
The source's Boolean simplification is explicit, with a separately supplied
parameter-table extension back to fixed-output-arity queries.

Editorial proof completions are distinguished from printed details. They
include order-definable immediate tuple successors; absent endpoint-neighbor
letters; returning and padding halting machines; uniqueness and exactness of
all generated rows; an explicit fixed-type padded characteristic-table
decoder; constant singleton tables; a unary-size header for that completed
encoding; complete finite diagrams below the alphabet/tag cutoff; and
folding finite accepting exceptions into the same positive induction.
The source says the reader can generalize Lemma3.1 from its binary example;
that missing general-type construction is supplied rather than treated as
already printed. This is a transparent completion of its local-row mechanism,
not a substitution of a Vardi/1999/generic tableau presentation.

## Qualifications and direct corrections

- The source's ancestor formula contains x=y and therefore gives reflexive
  transitive closure, not strict positive-length ancestry. The reader text
  preserves the displayed operator and explains this actual convention.
- Monotonicity yields ascent from the empty relation; it does not imply that
  an operator is inflationary on every arbitrary relation. The evaluation
  proof establishes the correct induction and bound.
- Zero tape bits receive explicit positive relation facts with zero letter
  codes. Missing facts cannot be used to infer negative bits in a positive
  tableau operator.
- The source's expressions p-1, p+1 and t-1 need endpoint and predecessor
  meanings. These are explicitly supplied, with no wraparound, imported BIT
  predicate or undefined arithmetic function.
- The source has at least one constant in its normal-form setup. Constant-free
  Boolean closure uses the stated one final quantifier, not silent omission
  of the proviso. The binder's positive-arity convention underlying that
  proviso is explicit: admitting a modern nullary relation binder would
  provide another way to write a closed atom and is not silently substituted.
- The source reports Fact2.2 by attribution to Chandra-Harel. The supplied
  parity proof is an editorial equality-pattern argument for the exact
  all-female/empty-parent-and-husband subclass, with the constant retained.
- Fixed-query data complexity is separated in the task/input-axis table from
  expression and combined evaluation; no unproved hardness class is imported
  from Vardi's separately allocated presentation.
- The 1986 section4 hierarchy collapse is distinct from Theorem1. Neither
  section3 nor section4 supplies the missing original 1999 Chapter4 body.

## Completed author checks, 2026-10-02

The package has five reciprocal proof targets. The first-half author reread
was completed in the initial block. In the bounded finish block the whole
second half of both files was read, including the accepting-anchor recoding,
preserved input order, finite small-domain operator, singleton parameter
tables, and nested-LFP equality-pattern argument. Every repaired passage was
then reread in its current file. These are author checks, not independent
admission.

The reread produced four mathematical precision repairs:

- The eventual unordered constancy statement now explicitly concerns fixed
  **sentences**. Open formulas require matching assignment patterns.
- The nested monotonicity proof now proves positive and negative parameter
  cases together, including an outer-positive parameter occurring negatively
  inside an inner fixed point under a surrounding negation.
- The equality-pattern induction is explicitly strengthened to allow
  pattern-invariant free relation interpretations, so it can be applied to
  outer stages while proving the inner fixed-point constructor.
- Letter-code equalities are eliminated by first-order code predicates, not
  partial terms or invented input constants. The machine's origin flag is
  created in its first setup transition, preserving the printed M0 row, so
  later accepting cleanup can recognize the first cell.

Direct finite calculations were performed in the tool runtime without
creating a software test suite:

1. **Printed M0.** At n=5 all 125 position triples had exactly one letter.
   The clauses partitioned them as 1 initial head cell, 24 ordinary bit
   cells and 100 blanks. Two E tables exercised both E(0,0) cases: the first
   selected code4, with 8 ordinary ones and 16 zeros; its complement selected
   code3, with 16 ordinary ones and 8 zeros. No missing/multiple letter.
2. **Moving head and exact stages.** A finite 448-entry neighborhood table
   for a deterministic toy machine gave successive first-cell neighborhoods
   `S1,0,B,B`; `0,R0,B,B`; `L0,1,B,B`; `F,1,B,B`. Direct machine execution
   and the positive source-shaped operator agreed at every cell/time.
   On 20 positions and 20 times, relation sizes were 0,20,40,...,400,400.
   All older rows persisted without an inflationary union clause, every row
   had one letter per position, and the last cell remained blank. No extra,
   missing, wrong, or lost fact was found.
3. **Padded decoder and original order.** At n=20, k=4, r=2, all 160000
   addresses were classified. The unary-size header decoded n=20; the binary
   E table and the original-order table were recovered without discrepancy;
   the singleton constant decoded c0=7 and a tested output coordinate
   decoded 3. Counts were 494 zero letters, 365 one letters, one start
   letter and 159140 blanks. Sorting by the decoded original-order table
   recovered 0,...,19, not the altered position order.
4. **Accepting anchor and cleanup.** With c0=7 the separate coordinate
   orders and accepting code gave final readout (7,7,7). All 20 possible
   anchor choices had the required first-position and last-time value.
   A second direct moving-head example created and preserved the origin
   flag, moved 0,1,2,3,2,1,0, then wrote stationary F; its local transition
   update agreed with global execution and kept the opposite endpoint blank.
5. **Small and singleton domains.** With the large-machine branch disabled,
   the finite-diagram seed for query E(c0,c0) was checked on both one-point
   databases and all 64 two-point ordered databases (all E tables, constants
   and orders), with one-stage stabilization and correct truth. The parameter
   version E(x,c0) was checked in 2 one-point and 128 two-point assignments.
   These gates do not require nonexistent alphabet codes.
6. **Nested fixed points and parity boundary.** For n=1,...,8, an outer
   induction `S(x)=x=c0 or not(mu R(y))[not S(y) and y!=c0](x)` stabilized
   at {c0}; its universal readout was true only at n=1. Exhausting all
   S-subset-S' pairs through n=6 found no violation of outer monotonicity.
   A positive nested induction seeded by S and spreading from an R point
   to unequal points stabilized after outer stages empty,{c0},U,U for n>1.
   Three-variable equality patterns relative to c0 numbered 15 at both
   n=5 and n=6. These examples check the delicate polarity/orbit cases;
   the general nondefinability conclusion rests on the supplied structural
   and stage induction, not on the examples.

The earlier block ended with these checks pending after its clock boundary;
this finish block completes them. No manuscript build/render, consolidated
review, children or prose-mirroring suite was performed.

Root owns routing, common-file reconciliation, lookup/intake integration and
later independent checks. The held author copy is accurately qualified;
publisher-facsimile identity remains unverified rather than claimed.
Any requirement that specifically demands comparison with the printed
publisher original retains that acquisition/variant-check residual. No
unfilled allocated mathematical proof is identified by the completed author
checks; independent source-fidelity, specialist and publication review remain
separate unfinished work and may reveal errors.
