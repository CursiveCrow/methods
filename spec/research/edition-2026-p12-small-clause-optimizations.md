# Small-clause optimizations: author checkpoint and source map

## Status and ownership

Current author: historical_first_half, resuming the product_measure_author
draft. Assignment HAR2001-C06-G02 through G05.
Authoring resumed under the lead's 9 September 2026 authoring contract after
the coverage-map phase. The assigned source treatment and the full author
read-through are now **complete as authored work**. Twelve body results have
their twelve corresponding complete annex proofs. This is not independent
acceptance, a build claim, or completion of separate original papers referred
to by the selected source.

## Completed resumption, 9 September 2026, 16:54 UTC

Read the entire saved body and annex, then the complete selected primary
Sections 4–8, bibliography and index (printed 347–367). The original title,
introduction and semantic preliminaries were also read, including the exact
multiset clause and substitution conventions. The lossy extraction was checked
against source images of printed 348–351 for the count/coefficient/threshold
tables. The retained 33-page PDF hash was reverified as
41EA6003E78E88D20EBE639EF7943F6A4BCC983D8F074D73F41B72C28AA32264.

The completed authoring changes are:

- Added a finite preorder naming schedule, def:p12-opt-schedule. Original
  occurrence markers move into the single retained definition copy, every visit
  removes one marker, and new syntax receives none. The annex now proves
  termination, polynomial representation size, whole-formula nonincrease and
  composition of the expansion/reduct maps for this precise schedule.
- Included the literal-root case in complete shallow naming.
- Restored the source condition that a conditional-definition guard has free
  variables only among the quantified head parameters.
- Required every BDD vertex to be reachable from its root and removed newly
  unreachable vertices after reduction. This excludes unrelated graph components
  from the canonicality claim and includes one-terminal constant diagrams.
- Corrected the two-atom clause bound for the retained multiset convention.
  Duplicate literals must first be removed by condensation. Without that
  condition, the r+1 multisets with i copies of P and r−i copies of Q are
  pairwise incomparable and nontautological for every r. The active text now
  contains the qualification and this counterexample.
- Declared the original binary relation R separately from auxiliary naming
  predicates; recorded that role and the conditional guard in the unique
  symbol intake.

The three shared G01 interfaces were confirmed with its current author:
thm:p12-small-context, thm:p12-small-sat-closure and
thm:p12-small-rectification. Their labels and all-assignment semantic scope
remain unchanged. G01 and its integration are not owned by this author.

The primary bibliography record is supplied in
handbook/bib/intake-p12-small-clause-optimizations.bib, key
NonnengartWeidenbach2001SmallClauses, DOI
10.1016/B978-044450813-3/50008-4, original pages 335–367.
Root owns canonical merging and driver routing. The body and annex remain
unrouted by this author.

The final modified passages were read again. A bounded count of the actual
files reports 12 theorem/status targets and 12 annex items; the reciprocal
labels were read directly. The mathematical cases above were derived in the
text and annex. No software test suite, manuscript build, manuscript render or
independent review was run.

Final authored artifact hashes:

- Body: D08A17B45220A31D4EAD03595E4F12C75B150C858C458ACD47CCCCBEA2333FA7.
- Annex: 8637685FA3773086C8066E1B6CA5B88F73D4BEFBBF787C7D3B35BD4B32B092F8.
- Symbol intake: 171D2F8AAD7FA0B65E490D9926843B6D2C88038CD43AB6C1B521DC9482249950.
- Bibliography intake: 7422C68175E1F2213A52DFC893B0C511B3D5A7C90E91914301DF583DDC8028C2.

Owned files:

- handbook/parts/p12/small-clause-optimizations.tex
- handbook/annex/p12/small-clause-optimizations.tex
- this note
- handbook/registry/symbols-intake-p12-small-clause-optimizations.csv
- handbook/bib/intake-p12-small-clause-optimizations.bib

Shared drivers, symbols and bibliography remain root-owned.
The unique bibliography intake now supplies key
NonnengartWeidenbach2001SmallClauses. Root integrates it and the companion
handbook/parts/p12/small-clause-standard.tex.

## Frozen primary presentation and read extent

Andreas Nonnengart and Christoph Weidenbach, “Computing Small Clause
Normal Forms,” Chapter 6 of *Handbook of Automated Reasoning* (2001).
The title page identifies that chapter, authors, editors Alan
Robinson and Andrei Voronkov, and Elsevier 2001.

Source: tmp/acquisition/src037/dfki-small-clause-retry-01.body.derived-decompressed.ps.derived-render.pdf.
33 physical pages. This is a retained PostScript-rendered presentation,
**not asserted byte-identical to a publisher PDF**.
SHA256 verified during this block:
41EA6003E78E88D20EBE639EF7943F6A4BCC983D8F074D73F41B72C28AA32264.
Printed numbered pages follow physical page + 334; the first physical
page is title/contents and the final physical page is printed 367.

The same-stem .pdf.derived-layout.txt is a lossy extraction aid.
Read the entire selected Section 4 through the end, printed 347–367,
including bibliography and index. Also read complete printed 338–341
for syntax, semantics, substitution, polarity, clauses and simplification.
The title/contents were read. Printed 337 was partially visible in an
output that truncated; do not credit it as a complete additional read.

Actual original-page PNGs inspected in visual-renders/pdf-008:
page-14.png through page-17.png (printed 348–351), and page-19.png
through page-29.png (printed 353–363). These establish table cells,
strong-step substitutions, selector proof, equality/definition
conditions and BDD edges. They are source images, not manuscript renders.

The research skill governed this one durable note. The PDF skill was
used for original-source reading. No PDF was authored or changed.
No reviewer, manuscript scanner, new test or build was run.

## Exact queue-to-host map

Queue: tmp/edition-2026-catalog-src037/chapter-component-queue-v3.json,
chapter 6, component_groups; all five rows read.

| Queue group | Assigned source extent | Saved host |
|---|---|---|
| HAR2001-C06-G02 | Section 4, pp. 347–352: renaming, expansion/reduct, count/coefficient recursions, thresholds, instances, size and search distinctions | def:p12-opt-renaming through thm:p12-opt-sharing; annex renaming/counts/coefficients/capped/sharing |
| HAR2001-C06-G03 | Section 5, pp. 352–359: Definition 5.1 inner/outer, Definition 5.2 and Lemma 5.3 optimized, Definition 5.4 splitting, Definition 5.5 strong, Definition 5.6 selectors, Lemmas 5.7–5.8, both comparisons | def:p12-opt-skolem-modes through def:p12-opt-skolem-failures; annex standard-skolem/optimized-skolem/selector/strong-skolem |
| HAR2001-C06-G04 | Section 6, pp. 359–363: equality substitutions, six cardinality cases, Lemma 6.1, atom definitions, BDD splitting/reduction/example | thm:p12-opt-equality through thm:p12-opt-bdd and matching annex entries |
| HAR2001-C06-G05 | Sections 7–8, pp. 363–365: historical variants, referred optimality/complexity, implementation and experience | sec:p12-opt-history and def:p12-opt-remaining-originals; no manufactured proof count for historical reports |

## Reciprocal statement/proof map

Twelve saved pairs. Prefix body labels by thm:p12-opt- and annex
labels by annex:p12.opt-:

1. renaming: positive/negative/zero definitions and model relation.
2. counts: all Table 3 cases and polynomial bit calculation.
3. coefficients: all Table 4 cases and exact saving inequalities.
4. capped: finite-value decision, terminating selected-position schedule,
   separately identified complete shallow-definition construction.
5. sharing: compatible shared instances and syntactic matching.
6. standard-skolem: arbitrary inner/outer single step, global outer
   witness construction and reversal, local/whole-formula distinction.
7. optimized-skolem: both witness cases and reduct.
8. selector: empty/nonempty fibers and uniform implication.
9. strong-skolem: full selector-composition route with uniform induction,
   and separate direct prefix-witness construction.
10. equality: both substitutions, six cardinality cases and termination.
11. atom-expansion: retained/guarded definitions and elimination.
12. bdd: splitting, reduction, uniqueness and path clauses.

The duplicated contextual pair was removed in the last patch.
Use root's thm:p12-small-context. Other direct root links are
thm:p12-small-sat-closure and thm:p12-small-rectification.
Root's whole companion body was personally read. Its proof annex was
being written concurrently and has not been read by this author;
no independent acceptance claim is made here.

## Corrections applied to reader mathematics

- Table 5 (350) misses p(A)=p(B)=2 in both sum-greater-than-three
  and product-greater-than-three tests. The reader supplies the
  complete threshold table and exact capped recurrence.
- Table 6 (351) needs the nonzero coefficient condition: a*p>1 does
  not follow from p>1 when a=0. Both zero and nonzero cases are supplied.
- Exponential magnitude does not prevent efficient exact counting.
  The actual tree recursion has counts at most 2^N and polynomial
  bit complexity. Printing all clauses can still be exponential.
- Freshness is outside the declared signature for fixed-structure
  expansion; merely unused old symbols can have fixed interpretations.
- Lemma 5.7's selectors need empty-fiber handling. Total functions are
  defined there, with universal truth asserted only on nonempty fibers.
- Lemma 5.8 uses a strengthened uniform implication and padded
  dependency-block containment. All composition steps are supplied;
  the separate direct proof also handles shared/empty dependency blocks.
- Definition 5.1's arbitrary outer step is retained with a full
  sentence-level witness construction. Local equivalence is asserted
  only for the inner step, with a two-element distinguishing example.
- Cardinality simplification retains the model class on both sides.
  A condition merely on models of the old whole formula can be
  vacuous; an inconsistent equality example shows the failure.
- Guarded definition expansion requires the stated intervening-binder
  condition, and all witness/definition substitutions avoid capture.
- Finite congruence axiomatization concerns a finite relevant signature;
  arbitrary infinite signatures require a scheme.
- BDD canonicality concerns a fixed propositional order. First-order
  Boolean abstraction remains sound but does not decide all
  first-order equivalences or allow arbitrary movement across binders.

The false running-example distribution on 346–347, closure interface
and raw-renaming injectivity are corrected by root's standard chapter;
this author did not modify those files.

## Historical and measured-evidence boundaries

The selected pages report favorable experience but supply no benchmark
count, timing table, hardware record, uncertainty interval or replication
data. None has been invented. The stated tree algorithms and explicit
output bound are proved constructions; the experience is reported history.

Separate original presentations remain owed if admitted as technical
obligations: Boy de la Tour's global optimality/strict-criterion proof;
Plaisted–Greenbaum's distinct quadratic size analysis; the cited
proof-length speedups; the 1998 experimental comparison; Goubault's
first-order BDD/Skolem algorithms; Goubault–Posegga comparisons; and
witness/predicate reuse. These are labeled referrals, not supplied
original proofs. No acquisition of those originals was attempted here.

## Earlier paused checkpoint, superseded by the completed resumption above

The first saved body was read completely. The first saved annex was
read from the start through the complete opt-sharing proof.
The in-flight final patch added standard-skolem, removed the duplicate
context proof, clarified the two-atom count, guard binding, variable-list
order and finite-signature scope after root relayed the user's priority.

**Still required before completing the author read-through:** read the
final patched body for those changes and the annex from
opt-standard-skolem through opt-bdd, then resolve any actual author
findings. This checkpoint does not claim integration, review, build,
rendering or acceptance. Root may now reassign the slot to coverage work.
