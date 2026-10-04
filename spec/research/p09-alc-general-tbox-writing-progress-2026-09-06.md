# General-TBox ALC manuscript writing

Date: 2026-09-06.

## Work incorporated

The active body is handbook/parts/p09/alc-general-tboxes.tex, included
by logic-in-computer-science.tex before entry:p09-alc. The active proof
fragment is handbook/annex/p09/alc-general-tboxes.tex, included by
handbook/annex/p09.tex.

- def:p09-alc-complete-type defines the finite NNF closure types,
  Boolean completeness, internalized global inclusions, and role
  compatibility.
- def:p09-alc-type-elimination gives every deletion and acceptance
  condition, including ABox name assignments, asserted role edges,
  nonempty domains, and an optional tested concept.
- thm:p09-alc-type-elimination / annex:p9.alc.2 proves preservation of
  realized types, the full canonical-model truth lemma, the finite
  model bound 2^m, and deterministic time 2^{O(N^2)}. With no ABox
  names, the displayed procedure takes 2^{O(N)} time.
- thm:p09-alc-general-exptime / annex:p9.alc.3 proves EXPTIME
  completeness for concept/TBox satisfiability, relative subsumption,
  finite knowledge-base satisfiability, and instance checking.
  The lower bound explicitly supplies configuration partitions,
  branching, scanned-cell updates, unchanged-cell constraints,
  binary countdown, polynomial output size, and both directions.

The body includes a two-stage deletion example, an inconsistent
asserted role edge, and a satisfiable cyclic inclusion with a
singleton self-loop model.

The system card and both host complexity tables now state the proved
classification. N-c-009 connects the later treatment to its exact
sources and retains the separate acquisition standing of the
2003 first edition and 2017 textbook.

## Sources and independent reading

The classification is supported by Baader--Horrocks--Sattler's
2008 chapter, Theorem 6 on p. 26 of the acquired 47-page author draft.
Donini--Massacci 2000, Theorem 3.13 p. 98 and Theorem 6.17 p. 123,
supplies a separate optimal concept/TBox tableau procedure subject
to its prescribed search techniques. The manuscript does not transfer
that bound to arbitrary blocking strategies.

Chandra--Kozen--Stockmeyer 1981, Corollary 3.6 p. 122, is the cited
APSPACE = EXPTIME dependency. Theorems 2.5 and 2.6(b), pp. 120-122,
are explicitly invoked to select a machine without negating states
whose reachable configurations obey a constructible polynomial space
bound. The tape/branching simulation and the ALC encoding are proved
in the manuscript.

An independent upper-bound review read the actual body, host semantics,
closure, annex:p9.alc.2, and all three examples; it found no mathematical
defect. The separate lower-bound review and source review are recorded in:

- p09-alc-general-tbox-lower-bound-review-2026-09-06.md;
- p09-alc-general-tbox-source-verification-2026-09-06.md.

The requested CKS citation clarification was incorporated and read back
by the lower-bound reviewer. These are bounded mathematical and source
reviews, not whole-book publication acceptance.

## Direct correction and navigation

N-c-009's earlier Proposition 4.2 canonical-model display now includes
the singleton case and a total individual assignment directly.
Its proof checks all constraint forms and both clash patterns.
The same independent reviewer checked this correction.
Historical source defects remain in the Schmidt--Schauss--Smolka
source note.

The four new definition/theorem rows and two named-theorem entries
were serialized using the existing navigation generators and applied
as a scoped generated patch. A proposed whole-register regeneration
would also change unrelated historical rows and proof links, so it
was not applied. That broader navigation discrepancy remains separate
work; this update makes no global freshness claim.

Nine notation rows were added to handbook/registry/symbols.csv, and
the existing symbols formatter regenerated its two reader tables
successfully with 701 rows.

## Remaining work

The exact 2003 and 2017 book bodies are still missing. Their separate
presentations remain owed. No tests, manuscript build, or page render
was used in this writing pass. Final build, layout, full content
coverage, and publication acceptance remain unverified. The complete
manuscript goal remains active.
