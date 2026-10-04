REJECT

# Part IX R3 adversarial-publication review

## Review basis and boundary

I independently re-established this verdict from the current reader graph and
did not use any earlier review transcript or conclusion.  The SHA-256 of
`handbook/parts/p09/logic-in-computer-science.tex` is
`D65CC5D77D14F6E897840B12367C983B4DFE842BA500A03B9A0A922F51ADD515`, exactly
the supplied frozen-snapshot hash.

The live route is `handbook/parts/p09.tex:1-3` to the Part IX body and
`handbook/annex/p09.tex:1-3` to `handbook/annex/p09/proofs.tex`.  I reviewed
that body and annex, all five Part IX calculus files, their one-time Part XIV
rendering, the relevant master-table rows, bibliography records, the generated
Part IX theorem/definition audit, the generated named-theorem index, and the
P9 symbol registrations and compact index links.  This was a source/content
review only.  I ran no test, TeX build, PDF build, or visual inspection, and no
mechanical-check result is treated as publication acceptance.

## Source/content blockers

### F1 — The description-logic table does not type its complexity problems

**Severity:** must-fix publication blocker.

**Live evidence:**

- `handbook/parts/p09/logic-in-computer-science.tex:376-424` is presented as
  the exact description-logic/profile, task, and complexity comparison.
- The OWL 2 EL cell at
  `handbook/parts/p09/logic-in-computer-science.tex:391-394` collectively says
  that ontology consistency, class satisfiability, subsumption, and instance
  checking are PTIME-complete “in taxonomic, data, and combined complexity.”
- The OWL 2 QL cell at
  `handbook/parts/p09/logic-in-computer-science.tex:399-402` uses “query
  complexity” as a third axis.
- “Taxonomic complexity” occurs nowhere else in the live handbook, and this
  location does not define what is input and what is fixed.  “Query
  complexity” is likewise not typed at this location.  This contradicts the
  chapter's promise at `handbook/parts/p09/logic-in-computer-science.tex:4-9`
  and the table's own no-transfer warning at lines 421-423.

**Concrete failure path:** a reader cannot form the decision language denoted
by the OWL 2 EL sentence.  In particular, the displayed class-subsumption task
has no varying ABox or data argument in the chapter's syntax, so calling it
PTIME-complete “in data complexity” is not a well-typed complexity assertion
unless a separate input convention is supplied.  The same sentence does not
say whether a taxonomy/TBox, an ABox, a queried class expression, or all of
them vary.  The resulting bound is therefore unreconstructible even if every
intended individual bound is true in its source convention.

**Exact correction:** before the table, define each retained axis by an input
tuple and fixed components: taxonomy/TBox complexity, data/ABox complexity,
query complexity, and combined complexity.  Then split the EL and QL cells by
reasoning task and print only the bound for the applicable, source-supported
axis.  Do not quantify the whole list of consistency, satisfiability,
subsumption, and instance tasks over all three axes in one sentence.  If the
intended source supports only a combined bound for a task, print only that
bound.  The correction must make each row answer: exact syntax/profile, exact
decision problem, varying input, fixed input, encoding, class, and source.

### F2 — The Part XIV monadic-FOL row contradicts the route Part IX tells the reader to use

**Severity:** must-fix apparatus and terminology blocker.

**Live evidence:**

- Part IX routes the exact fragment conventions to
  `tab:p02-decidable-fragments` and expressly says the monadic row is
  equality-free and function-free at
  `handbook/parts/p09/logic-in-computer-science.tex:178-185`.
- The routed row says that Lewis's language has neither identity nor function
  signs, imports no constants, and puts equality, constants, and functions
  outside the cited complexity claim at
  `handbook/parts/p02/first-order-depth.tex:199-210`.
- The master decision table instead prints “constants/equality declared” for
  the same unqualified name “monadic first-order logic” at
  `handbook/parts/p14/master-tables.tex:29`.
- This also conflicts with the master table's declared retrieval role at
  `handbook/parts/p14/master-tables.tex:5-9`.

**Concrete failure path:** the sentence `\(\forall x\,x=x\)` belongs to the
language described by the Part XIV row but is explicitly outside the language
of the Part II row to which Part IX sends the reader.  Thus a reader following
the public retrieval path reaches two different input languages under one
name, and cannot know which language the displayed decision status governs.

**Exact correction:** align the Part XIV row with the routed Part II result:
closed formulas over unary predicates, no identity, no constants, and no
function symbols; print satisfiability as `\(\mathsf{NEXPTIME}\)`-complete and
route the qualification to `Table~\ref{tab:p02-decidable-fragments}` with
`Lewis1980`.  If a broader monadic language with equality or constants is
independently intended, it needs a separately distinguished convention and an
exact theorem/source; it cannot silently replace the already routed row.

### F3 — The modal-\(\mu\) master row contains a placeholder instead of the live status and route

**Severity:** must-fix retrieval/completeness blocker.

**Live evidence:**

- Part IX explicitly routes the modal-\(\mu\) language, semantics, sheet, and
  system card at `handbook/parts/p09/logic-in-computer-science.tex:701-710` and
  records the strict alternation result at lines 713-717.
- The live card gives the actual decision information at
  `handbook/parts/p08/temporal-epistemic-supplement.tex:250-270`: satisfiability
  is EXPTIME-complete; finite-state model checking is polynomial-time
  equivalent to parity games, has a quasipolynomial algorithm, and is not
  known to be in P.  The adjacent live comparison table further records the
  P-hard and `\(\mathsf{UP}\cap\mathsf{coUP}\)` boundaries at
  `handbook/parts/p08/temporal-epistemic-supplement.tex:273-299`.
- The Part XIV decision table reduces all of that to “parity-game equivalent”
  in the status column and the reader-facing phrase “algorithm/bound declared”
  at `handbook/parts/p14/master-tables.tex:56`.  It supplies no destination and
  omits the current quasipolynomial source.

**Concrete failure path:** the reader consults the master *decision-problem*
table for the modal-\(\mu\) model-checking status and receives neither an
algorithmic bound nor a link to the place where the bound is declared.
“Algorithm/bound declared” is construction prose, not a decision status, and
cannot be used to compare the row with the exact CTL/CTL* rows immediately
above it.

**Exact correction:** replace line 56 with the live finite-explicit-input
classification: polynomial-time equivalent to parity games, P-hard, in
`\(\mathsf{UP}\cap\mathsf{coUP}\)`, quasipolynomial-time, with membership in P
open.  Hyperlink the row to `entry:p08-modal-mu` (and, if useful,
`tab:p08-temporal-comparison`) and include the source that controls the
quasipolynomial bound.  Keep satisfiability's EXPTIME-complete status separate
from model checking rather than merging the two problems.

### F4 — The TQBF prose denies a second public identity while the live generated apparatus publishes one

**Severity:** must-fix identity/standing ambiguity.

**Live evidence:**

- The public completeness result is `thm:p04-tqbf-pspace`, stated at
  `handbook/parts/p04/complexity.tex:237-241` and listed in the named-theorem
  index at `handbook/generated/named-theorem-index.tex:428`.
- Part IX then opens a second public theorem environment,
  `thm:p09-tqbf-proof`, at
  `handbook/parts/p09/logic-in-computer-science.tex:1768-1778`, while lines
  1775-1777 say that “the result is not assigned a second public identity
  here.”
- The annex targets the P9 identity at
  `handbook/annex/p09/proofs.tex:136-207`, but its conclusion points back to
  the P4 theorem at line 206.
- The generated Part IX audit publishes the P9 theorem at
  `handbook/generated/audit-p09.tex:84`, and the generated named-theorem index
  publishes it at `handbook/generated/named-theorem-index.tex:312`.  The P4
  and P9 destinations are therefore both reader-visible public theorem
  identities.

**Concrete failure path:** a reader following the sentence “not assigned a
second public identity” to the named-theorem index finds two destinations: the
P4 completeness theorem and the P9 theorem containing the membership and
hardness constructions.  The current text does not decide whether the P9 item
is merely the proof route for the P4 theorem or a nonredundant additional
theorem; the generated apparatus makes the former prose literally unsafe.

**Exact correction:** choose one standing.  For one public identity, retarget
the annex proof to `thm:p04-tqbf-pspace`, make the P9 body item an unnumbered
proof-route paragraph, and regenerate the P9 audit and named index without
`thm:p09-tqbf-proof`.  If a distinct construction theorem is required, narrow
its statement to the genuinely additional construction, explicitly explain
its nonredundancy with TQBF completeness, and replace the false no-second-
identity sentence with that standing before regenerating the indexes.

## Checked-clean source/content seams

- **Frozen route and reader debt:** the body hash matches; the Part IX and
  annex drivers each route one live file.  The current reader graph contains
  no noncomment OPEN, TODO, FIXME, stub, unadmitted, internal row ID,
  finalizer, or workflow instruction.  Ordinary uses such as an open tableau
  branch and an open interval endpoint are semantic, not workflow debt.

- **Finite-model and prefix material:** finite versus unrestricted validity,
  the single inherited Trakhtenbrot route, the Part III zero--one/Fagin routes,
  locality, and the equality-sensitive prefix table are internally coherent at
  `handbook/parts/p09/logic-in-computer-science.tex:47-258`.  No second
  Part-IX Trakhtenbrot theorem identity appears in the Part IX generated audit.
  F2 is the separate Part XIV convention collision.

- **ALC initialization and proof:** the body initializes every ABox individual,
  every declared ABox edge, the optional tested root, and a TBox-only anonymous
  root at `handbook/parts/p09/logic-in-computer-science.tex:296-343`.
  `handbook/registry/calculi/tableaux-alc.tex:2-25` prints the same data,
  blocking convention, re-evaluation rule, and root initialization.  The
  annex termination/model-guidance/model-extraction proof is reciprocal at
  `handbook/annex/p09/proofs.tex:3-67`; the former empty-initial-forest failure
  path is closed in the current source.

- **Temporal, automata, CTL, symbolic, and probability semantics:** the
  infinite-word acceptance conventions, product initialization, finite-tree
  run semantics, CTL least/greatest fixed points, and interpolation procedure
  all state their model and acceptance data at
  `handbook/parts/p09/logic-in-computer-science.tex:427-803`.  PCTL now prints
  all three path-formula clauses and types undecorated versus min/max modalities
  at lines 805-913.  CSL prints elapsed-time until, endpoint standing, and the
  long-run clause at lines 915-963.  The annex CTL proof matches the live
  fixed-point clauses at `handbook/annex/p09/proofs.tex:69-105`.  F3 concerns
  only the master retrieval row, not these live semantics.

- **Program and logic-programming calculi:**
  `handbook/registry/calculi/hilbert-pdl.tex:2-12`,
  `handbook/registry/calculi/hoare-while.tex:2-15`,
  `handbook/registry/calculi/separation-logic.tex:2-4`, and
  `handbook/registry/calculi/sld-resolution.tex:2-12` agree with their body
  languages and side conditions.  The total-while rule preserves a fresh old
  variant value; the separation frame rule requires both locality and the
  free-variable condition; SLD uses standardization apart, whole-resolvent
  substitution, and the occurs check.  The Prolog paragraph at
  `handbook/parts/p09/logic-in-computer-science.tex:1356-1367` now distinguishes
  leftmost/textual/depth-first execution from fair complete-tree enumeration
  and excludes omitted-occurs-check, cut, and other extra-logical behavior.

- **Stable, well-founded, database, and CSP boundaries:** the reduct, stable
  criterion, alternating fixed point, canonical-database homomorphism,
  fixed-query versus combined evaluation, Datalog saturation, and fixed-template
  CSP input are separated at
  `handbook/parts/p09/logic-in-computer-science.tex:1392-1656`.  The logic-
  programming comparison table and SLD figure each have one live label.

- **Proof-status reciprocity:** the four `proved=` body records map one-to-one
  to the four annex items: ALC, CTL, Hoare soundness, and the TQBF construction.
  The proof bodies contain the advertised termination/fixed-point/variant/QBF
  arguments.  F4 is an identity-standing defect, not a claim that the selector
  recurrence itself is malformed.

- **One-time sheet routing:** each of `tableaux-alc`, `hilbert-pdl`,
  `hoare-while`, `separation-logic`, and `sld-resolution` has one registry
  definition and exactly one `\showcalculus` route at
  `handbook/parts/p14/rule-sheets.tex:80-87`.

- **Generated audit and named retrieval:** direct source comparison gives 70
  Part IX public definition/theorem/method/example environments and 70 rows in
  `handbook/generated/audit-p09.tex:15-84`; the body's 38 named theorem-like
  results have 38 P9 destinations in
  `handbook/generated/named-theorem-index.tex`.  All generated P9 proof targets
  point to live annex or citation data.  These count/target checks do not cure
  F4's semantic identity claim.

- **Symbols:** the registry has 52 P9-scoped rows.  The same 52 distinct
  destinations appear at
  `handbook/generated/symbols-tables.tex:768-819`, and the compact
  `handbook/generated/symbol-index.tex` has exactly one link back to each of
  those 52 destinations.  The full registry is routed once at
  `handbook/parts/p01/symbol-registry.tex:31`; the compact projection is routed
  at `handbook/parts/p14/master-tables.tex:249-269`.

- **References and bibliography:** static label collection found no unresolved
  `\ref`, `\pageref`, or `\hyperref` target on the scoped body, annex, sheets,
  Part XIV routes, and generated surfaces.  Every citation key used on those
  scoped surfaces has a live entry in `handbook/bib/handbook.bib`; the added
  W3C and ISO records are present at lines 5834-5849.  This is source-level
  target/key existence only, not proof that TeX, hyperlinks, or bibliography
  rendering succeeds.

- **Registered artifacts:** the live route contains the prefix,
  description-logic, probabilistic/stochastic, Hoare/WP, logic-programming, and
  overall complexity tables and the worked SLD figure.  It also reaches the
  already public finite-model and temporal comparison artifacts rather than
  duplicating them.  The Buechi/model-checking, SLD/Prolog, stable/Datalog,
  Hoare/WP/separation, and quantitative-probability subject obligations all
  have substantive reader surfaces; the blockers above concern exact claim
  typing and retrieval, not absent chapter sections.

## Prioritized repair checklist

1. Type and split the OWL 2 EL/QL complexity assertions by exact varied and
   fixed inputs; remove every collective or inapplicable axis claim.
2. Repair the Part XIV monadic-FOL row to match the exact Part II/Part IX
   language convention.
3. Replace the modal-\(\mu\) placeholder row with the live finite-state status,
   destination, and source.
4. Resolve TQBF's one-identity versus separate-construction standing and
   regenerate the affected audit/named-theorem surfaces.
5. Re-run the existing mechanical source checks after those edits.  Only then
   run the still-external full TeX/reference/bibliography build, inspect the
   long tables and SLD figure visually, inspect generated page links and index
   ordering, and obtain the separate human/user gates.

Until F1-F4 are corrected, the frozen Part IX source/content graph is not safe
for final publication admission.
