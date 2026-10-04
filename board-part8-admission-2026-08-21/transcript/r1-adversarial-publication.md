# Part VIII admission board — round 1 adversarial-publication review

## Verdict and evidence boundary

Part VIII is **not source/content-admissible on the current bytes**.  The exact
restoration route is substantially better disciplined than the retained
historical combined files, and many local mathematical/status surfaces are
sound.  Nevertheless, the live reader still encounters explicit construction
debt, several must/should register promises have no reconstructible treatment,
and the generated retrieval apparatus makes claims broader than its actual
coverage.

This was a source-only review of the reader graph rooted at
`handbook/parts/p08.tex:2-49` and `handbook/annex/p08.tex:2-9`, including the
restoration wrappers, routed supplements, active calculus sheets, generated
audit/theorem/symbol surfaces, Part VIII register rows, and bibliography and
navigation consumers.  I did not treat the retained but unrouted combined
Part VIII bodies or historical annexes as live reader content.  No TeX/PDF
build, test, visual inspection, provenance adjudication, human review, or user
acceptance was performed.

## Findings

### F1 — P1 — Reader-visible OPEN and internal-workflow debt remains

**Status:** still-open-source; admission blocker.

**Evidence.** The reader notes call routed material “OPEN additions” in
`handbook/parts/p08/intuitionistic-supplement.tex:15-17`,
`handbook/parts/p08/modal-logics-supplement.tex:16-17`,
`handbook/parts/p08/temporal-epistemic-supplement.tex:16-18`,
`handbook/parts/p08/many-valued-supplement.tex:16-18`, and
`handbook/parts/p08/relevance-linear-supplement.tex:15-18`.  The many-valued
chapter then prints the internal identifiers `D-P10-020`, `N-b-028`, and
`N-b-029` and says they “remain OPEN inclusion obligations” at
`handbook/parts/p08/many-valued-supplement.tex:187-198`; it repeats “OPEN annex
targets” at `handbook/parts/p08/many-valued-supplement.tex:484-490`.  The only
live Part VIII annex likewise tells the reader that its items are OPEN at
`handbook/annex/p08/many-valued-supplement.tex:13-16`.

**Concrete failure path.** A reader following the normal Part VIII route is
shown campaign workflow status and opaque register identifiers instead of a
finished source/editorial standing.  This directly violates the charter's
no-reader-OPEN/no-internal-row invariant at `board-part8-admission-2026-08-21/charter.md:11-16`.

**Exact correction.** Complete or explicitly rescope the substantive
obligations in their governing registers, then replace every printed OPEN/internal-ID
notice with ordinary reader-facing provenance: identify the exact inherited
source, identify the separately sourced editorial addition, and state only its
mathematical proof status.  Merely deleting the word OPEN while leaving the
owed calculus or theorem absent would not close this finding.

### F2 — P1 — A-113 has no live Part VIII audit register, and the candidate is malformed

**Status:** still-open-source; admission blocker.

**Evidence.** A-113 requires one generated audit table per part at
`spec/registers/apparatus.csv:114`.  The Part VIII driver explicitly leaves
`generated/audit-p08` unrouted because it scans retained historical files
rather than the reachable graph (`handbook/parts/p08.tex:50-52`).  The generated
candidate does have a nominal Part VIII caption and label at
`handbook/generated/audit-p08.tex:1-6`, but exact-source results lack IDs and
targets, for example `handbook/generated/audit-p08.tex:15-20`, and the hybrid
logic title is corrupted to `)\)` at `handbook/generated/audit-p08.tex:96`.

**Concrete failure path.** The reader has no Part VIII theorem/definition
register to navigate.  Routing the present candidate would instead expose a
hybrid historical/live scan, missing destinations, and a visibly broken title.

**Exact correction.** Make the audit-table generator consume the reachable
Part VIII route, give every exact-source unit a stable source-preserving
destination, correct parsing of braced titles containing `@`, regenerate the
table, and route that one generated table exactly once from Part VIII.

### F3 — P1 — A-159's “every live named theorem and lemma” claim is false for exact restorations

**Status:** still-open-source; admission blocker.

**Evidence.** The master table says the generated index covers every live
named theorem and lemma destination at
`handbook/parts/p14/master-tables.tex:239-241`, and the generated file repeats
that claim at `handbook/generated/named-theorem-index.tex:1`.  Several reachable
exact-source named results have no label/destination and are omitted from that
index:

- Persistence — `handbook/restoration/inherited-13046-13057.tex:1-4`;
- Soundness and strong completeness of IPL —
  `handbook/restoration/inherited-13058-13099.tex:11-21`;
- Frame correspondence and completeness —
  `handbook/restoration/inherited-13285-13316.tex:1-21`;
- Soundness and completeness of LTL —
  `handbook/restoration/inherited-13440-13471.tex:1-13`;
- Multi-agent S5 — `handbook/restoration/inherited-13519-13551.tex:1-6`;
- Finite-matrix tableau soundness and completeness —
  `handbook/restoration/inherited-13641-13699.tex:1-6`;
- Soundness, completeness, and cut elimination for the displayed IMLL
  calculus — `handbook/restoration/inherited-14001-14015.tex:1-6`.

The separate generated audit exposes the same defect by rendering these named
results with `--` rather than a target at
`handbook/generated/audit-p08.tex:17-19`, `:47-51`, `:107`, and `:132`.
A-159 requires all named theorems and lemmas to point to statement and proof
detail (`spec/registers/apparatus.csv:160`).

**Concrete failure path.** A reader who knows one of the exact inherited
theorem names cannot retrieve it through the advertised named-theorem index;
the index silently favors labelled editorial environments over unlabelled
exact-source theorem environments.

**Exact correction.** Add source-preserving wrapper destinations for every
reachable restored named result, teach the generator to harvest those
destinations and their inline proof/sketch status, regenerate the index, and
retain the “every live” claim only after the generated coverage is complete.

### F4 — P2 — The public symbol registry and symbol index leak internal audit language

**Status:** still-open-source; publication blocker under the no-internal-workflow
invariant.

**Evidence.** Part VIII symbol rows print “Ruling 3,” “audit D3/E3,” “promised
... but never registered,” and “Audit C3 finding 10” at
`handbook/generated/symbols-tables.tex:598`, `:600-607`, `:622`, and `:625`.
Those notes are copied into the compact public symbol index, including
`handbook/generated/symbol-index.tex:27`, `:76`, `:100`, `:104`, `:132`,
`:152`, `:258`, `:309`, `:313`, `:397`, `:530`, `:558`, and `:588`.  The
master-table prose presents the projection as a reader retrieval surface at
`handbook/parts/p14/master-tables.tex:219-240`.

**Concrete failure path.** A reader looking up a nonclassical symbol encounters
undefined audit phases and internal rulings in the “principal uses / notes”
column.  These strings neither define the symbol nor supply a usable source
route.

**Exact correction.** Keep audit/ruling lineage in machine-readable control
metadata only.  Generate public notes from semantic role, scope, precedence,
and source/use information, with no audit labels, finding numbers, promises, or
campaign history.

### F5 — P1 — A-189 navigation is incomplete and one annex direction is false

**Status:** still-open-source; admission blocker.

**Evidence.** The intuitionistic navigation paragraph tells the reader that
complete and sketched evidence is reached through status links to Annex P8 at
`handbook/parts/p08/intuitionistic-supplement.tex:550-555`.  The live annex,
however, routes only the many-valued supplement and explicitly excludes the
historical intuitionistic/modal/temporal annexes at
`handbook/annex/p08.tex:2-9`; the IPL proof and sketch are inline at
`handbook/restoration/inherited-13046-13057.tex:1-12` and
`handbook/restoration/inherited-13058-13099.tex:11-41`.

A-189 also requires body links to the precedence table and notation registry
(`spec/registers/apparatus.csv:190`).  The actual targets are
`handbook/parts/p01/symbol-registry.tex:2-4` and `:83-97`, but the live Part
VIII body supplies no `sec:p01-symbol-registry` or `tab:p01-precedence`
consumer.  Its navigation paragraphs instead concentrate on sheets and local
source citations, for example
`handbook/parts/p08/modal-logics-supplement.tex:996-1003` and
`handbook/parts/p08/many-valued-supplement.tex:482-498`.

**Concrete failure path.** The annex link lands at unrelated many-valued
material, while a reader trying to resolve overloaded Part VIII glyphs has no
body-to-registry/precedence route even though the handbook promises one.

**Exact correction.** Replace the false annex statement with direct links to
the inline IPL result/status destinations (after F3 supplies them), and add one
Part VIII navigation paragraph linking the normative symbol registry and
precedence table as well as the rule-sheet catalog.

### F6 — P1 — D_G has no Part VIII semantic entry and A-080 does not include its promised surface

**Status:** still-open-source; admission blocker.

**Evidence.** The common-knowledge card first invokes distributed knowledge
by saying that `D_G` uses relation intersection at
`handbook/parts/p08/temporal-epistemic-supplement.tex:509-527`, but neither the
exact source's E/C definitions
(`handbook/restoration/inherited-13519-13551.tex:20-32`) nor the supplement
defines a relation and satisfaction clause for `D_G`.  The epistemic table
then claims “semantic entry above” at
`handbook/parts/p08/temporal-epistemic-supplement.tex:626-650`, specifically
`:642-643`, although no such entry exists.  A remote generated registry note
does describe the intended reading at
`handbook/generated/symbols-tables.tex:678`, but F5 shows that Part VIII does
not link the reader to that registry.

A-080 requires the S5n/E/C/D/PAL table with the common-knowledge induction rule
included (`spec/registers/apparatus.csv:81`).  The current table expressly
points to, rather than includes, the induction and PAL surfaces at
`handbook/parts/p08/temporal-epistemic-supplement.tex:637-650`.

**Concrete failure path.** Following “semantic entry above” yields no truth
condition for a formula `D_G A`; following the table alone also does not show
the induction rule its governed apparatus row says is included.

**Exact correction.** Before the card/table use, define
`R_G^D = \bigcap_{i\in G}\sim_i` and the exact satisfaction clause for
`D_G A`, state its standing versus E and C, and link the registered symbol row.
Then put the exact fixed-point/induction and PAL axiom surfaces in A-080 or
revise the governed apparatus contract through an explicit board decision; an
unqualified “semantic entry above” must not remain.

### F7 — P1 — The conditionals/deontic/free chapter does not deliver its must/should content or apparatus

**Status:** still-open-source; admission blocker.

**Evidence.** The governing rows require a free-logic family treatment
(`spec/registers/new-content.csv:82`), SDL with Ross, Good Samaritan, Chisholm,
and dyadic semantics (`:85`), C1/VC counterfactual completeness (`:88`), an
indicative-conditional treatment including a theorem-level triviality result
(`:89`), and CK/neighbors with selection-function and premise semantics and a
correspondence table (`:90`).  A-089--A-091 independently require governed
conditional, deontic, and free-logic tables at
`spec/registers/apparatus.csv:90-92`.

The live chapter supplies only:

- one “negative” definition that leaves term denotation as the disjunction
  “partial or outer-domain” and gives only prose rules, while its anonymous
  three-row variant table has no caption/label or fixed calculi
  (`handbook/parts/p08/conditionals-deontic-free.tex:7-43`);
- SDL and Chisholm prose, but no Ross or Good Samaritan/gentle-murder case and
  no formal dyadic truth clause, calculus, or adequacy statement (`:45-73`);
- a partial Stalnaker clause that is undefined when no A-world is available,
  a non-formal Lewis phrase “relevant closest region,” and no C1/VC calculus or
  completeness statement (`:75-105`);
- an Adams definition and a name-level Lewis-triviality summary without the
  theorem's hypotheses, plus no CK, neighboring systems, premise semantics, or
  correspondence table (`:107-134`).

**Concrete failure path.** A reader cannot decide atomic truth in the mixed
free-logic presentation, evaluate all counterfactual cases, reconstruct a
dyadic obligation, identify the C1/VC derivability relation, or test the
promised conditional/deontic comparison tables.  Citations cannot substitute
for the missing local definitions and system identities.

**Exact correction.** Split and type the free-logic variants, fixing term,
atomic, identity, quantifier, existence, and description clauses and their
matched calculi.  Add the missing deontic paradox cases and one explicitly
sourced dyadic semantics.  Add separately named C1 and VC presentations with
total semantic clauses, calculus/adequacy status, and the A-089 comparison
table.  State Lewis triviality with its exact hypotheses, and add the
CK-neighbor/premise-semantics map.  Give A-089--A-091 captions, stable labels,
and source/status columns.

### F8 — P1 — The quantified-modal section promises a designation policy but omits designators

**Status:** still-open-source; admission blocker for N-b-009.

**Evidence.** N-b-009 expressly requires rigid designators together with
domain regimes, existence, and actualism/possibilism at
`spec/registers/new-content.csv:81`.  The section correctly warns that a
quantified-modal presentation must fix designation policy at
`handbook/parts/p08/modal-logics-supplement.tex:850-859`, but the model that
follows supplies only world-relative predicate extensions and a
world-independent variable valuation at `:862-895`.  The theorem later calls
that valuation convention a “rigid-assignment convention” at `:936-941`; a
fixed assignment to variables is not a semantics for constants/designators.

**Concrete failure path.** The reader cannot interpret a modal formula
containing a name, determine whether a name denotes across worlds, or compare
rigid designation with domain membership, despite the governing row and the
section's own parameter warning.

**Exact correction.** Add the chosen constant/name syntax, a typed
world-relative or world-invariant designation map, denotation/existence
conditions, and an explicit definition of rigidity.  Distinguish that map
from the fixed variable assignment used in the Barcan proof.  If the source
example intentionally has no names, state that limitation and leave N-b-009
honestly unclosed rather than calling variable assignment rigid designation.

### F9 — P1 — The mandatory canonical-completeness package remains only a sketch

**Status:** still-open-source; admission blocker for D-P10-001/N-b-001, but not
a proof-status inflation finding.

**Evidence.** D-P10-001 requires canonical models constructed with
completeness proofs for K, T, S4, and S5 at
`spec/registers/depth-gaps.csv:85`; N-b-001 requires the Lindenbaum
construction and canonicity treatment at `spec/registers/new-content.csv:73`.
The exact inherited theorem is explicitly only a proof sketch and delegates
the detailed canonical argument to a citation at
`handbook/restoration/inherited-13285-13316.tex:23-31`.  The supplement defines
the worlds/relation and lists the existence lemma, truth lemma, and frame
checks that are needed, but does not prove them
(`handbook/parts/p08/modal-logics-supplement.tex:285-304`).

**Concrete failure path.** A reader attempting the advertised construction
cannot recover the Lindenbaum extension, modal existence lemma, full truth
lemma, or the separate T/4/5 canonical-frame checks from the live book.  The
existing “sketch” label is honest, but honesty does not discharge a register
row requiring the proofs.

**Exact correction.** Preserve the inherited sketch and add a separately
attributed proof package, preferably in a reciprocal annex route: Lindenbaum
extension, existence lemma, truth lemma including the box case, and explicit
canonical relation checks for K/T/S4/S5.  Link each body theorem/card to that
proof and index it.

### F10 — P1 — The many-valued/fuzzy syntactic claims are not reconstructible and are expressly unadmitted

**Status:** still-open-source; admission blocker.

**Evidence.** D-P10-020 and N-b-028 require finite/infinite Lukasiewicz
matrices, axiomatization, and completeness (`spec/registers/depth-gaps.csv:104`
and `spec/registers/new-content.csv:100`); N-b-029 requires the t-norm family at
must priority (`spec/registers/new-content.csv:101`), and A-085 requires the
table to include axiomatizations (`spec/registers/apparatus.csv:86`).  The
chapter itself says those rows remain OPEN and that its content does not close
them at `handbook/parts/p08/many-valued-supplement.tex:187-198`.

The semantic matrices are defined at `:202-224`, but the syntactic theorem
then refers to “its standard Hilbert calculus” without defining or routing
that calculus at `:325-338`.  The t-norm theorem delegates to calculi “named in
the table” at `:376-384`, while the table caption admits that it only names
cited Hilbert extensions and does not redisplay their rules at `:386-390`;
its rows give semantic scopes and completeness labels rather than the promised
axiomatizations (`:400-429`).

**Concrete failure path.** The reader can calculate truth values but cannot
form the derivability relation on the left side of the Lukasiewicz
completeness biconditional or reconstruct the BL/MTL/Godel/Product proof
systems.  A source citation and a system name are not a definition of a
calculus.

**Exact correction.** Supply exact sourced Hilbert axiom/rule surfaces (and
stable calculus identifiers) for the infinite Lukasiewicz logic and each
t-norm system whose syntactic completeness is asserted; state precisely which
finite/infinite consequence notion each theorem covers.  Populate A-085 with
those surfaces or exact links, then remove the OPEN notices only after the
governed rows are actually discharged.

### F11 — P1 — Paraconsistent/nonmonotonic must/should rows and comparison tables are incomplete

**Status:** still-open-source; admission blocker.

**Evidence.** N-b-026 requires the inclosure schema and replies in the
dialetheism treatment (`spec/registers/new-content.csv:98`).  The live chapter
distinguishes dialetheism from paraconsistency and gives an LP countervaluation
but supplies neither the schema nor replies
(`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:10-42`).

N-b-032 requires System P/KLM, rational monotony, AGM, Levi and Harper at must
priority (`spec/registers/new-content.csv:104`).  The chapter names the System
P principles in prose at `:58-64`, compresses AGM postulates into prose, gives
Levi but not Harper, and does not state the promised representation theorem at
`:84-105`.  D-P10-036 and A-093 require an AGM postulates table with both
identities (`spec/registers/depth-gaps.csv:120` and
`spec/registers/apparatus.csv:94`), but no such table appears.

D-P10-035 requires default, circumscription, and autoepistemic logic
(`spec/registers/depth-gaps.csv:119`), N-b-033 requires default/circumscription
entry cards (`spec/registers/new-content.csv:105`), and A-092 requires a table
including default, circumscription, autoepistemic logic, and ASP with
consequence and complexity (`spec/registers/apparatus.csv:93`).  The current
table has only semantic/operational object and characteristic step columns,
omits autoepistemic logic and all complexity data
(`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:66-81`); the later
default and circumscription material is definition-level prose rather than
complete entry cards (`:107-143`).

**Concrete failure path.** A reader cannot reconstruct System P's rule surface,
derive the KLM/AGM representation claims, apply Harper, locate an
autoepistemic consequence definition, or make the promised complexity
comparison.

**Exact correction.** Add the inclosure schema with explicitly sourced reply
families; display System P and rational monotony with exact rule conditions and
state the representation results at their governed ceiling; add the complete
AGM revision/contraction table with Levi and Harper; add a typed
autoepistemic-logic treatment and structured default/circumscription cards;
and regenerate/replace A-092 with consequence and complexity columns.

Adaptive logic is **not** separately charged as a missing technical chapter:
the governing exclusion row N-x-007 at `spec/registers/new-content.csv:178`
places it outside the admitted program, and the explicit boundary at
`handbook/parts/p08/relevance-linear-supplement.tex:683-691` is coherent with
that decision.  Inventing an unregistered adaptive system would violate the
frozen contract rather than repair it.

### F12 — P2 — The .2 and .3 “first-order conditions” are open formulas

**Status:** still-open-source; localized correctness/publication defect.

**Evidence.** The correspondence theorem says every displayed row is an exact
first-order frame condition at
`handbook/parts/p08/modal-logics-supplement.tex:367-373`.  Rows D through 5 are
explicitly closed, but the .2 and .3 rows omit all universal quantifiers at
`:382-388`.

**Concrete failure path.** As printed, `Rxy \land Rxz -> ...` has free
variables and is not a frame sentence; the table gives no convention saying
that free variables are universally closed.  This is especially misleading
because adjacent rows spell out their quantifiers.

**Exact correction.** Prefix the .2 and .3 formulas with the appropriate
universal quantifiers (including the existential witness for .2), or state in
the table heading/caption that every displayed free variable is universally
closed.  Using explicit closed formulas is preferable here because the other
rows already do so.

## Checked-clean source/content surfaces

- **Route and identity.** `handbook/parts/p08.tex:2-49` interleaves the exact
  restoration scopes with each live supplement once.  The retained combined
  files under `handbook/parts/p08/` are not on that route.  The annex driver
  explains and excludes the shortened historical duplicate annexes at
  `handbook/annex/p08.tex:3-9`.  Source-level inspection found no duplicate
  reachable label/identity.
- **Lot 1.** The current excluded-middle and Peirce figures are semantically
  correct, including the crucial `w_1 \nVdash p\to q` annotation at
  `handbook/parts/p08/intuitionistic-supplement.tex:61-97`.  Negative
  translations, Heyting/topological semantics, IQC, and KC/LC apparatus were
  checked; no additional local mathematical blocker was established beyond
  F1/F3/F5.
- **Lot 2.** The normal/non-normal modal catalog keeps systems distinct; its
  lattice caption explicitly refuses unproved inclusions at
  `handbook/parts/p08/modal-logics-supplement.tex:309-340`.  Filtration,
  bisimulation, neighborhood, two-dimensional, Barcan, and incompleteness
  claims generally retain source-specific scopes and honest cited/sketched
  status.  The outstanding issues are F8, F9, and F12 rather than a blanket
  family-wide transfer.
- **Lot 3.** LTL/CTL/CTL*/mu-calculus, multi-agent S5/KD45, common knowledge,
  PAL, and hybrid-logic sheets all have live rule-sheet destinations through
  `handbook/parts/p14/rule-sheets.tex:65-76`.  The temporal, branching-time,
  automata, epistemic, and PAL figures/tables were source-level checked; the
  concrete residuals are F6 and F7.
- **Lot 4.** K3, LP, and FDE keep their designated sets distinct, the generic
  finite-matrix theorem has a complete inline proof at
  `handbook/restoration/inherited-13641-13699.tex:1-58`, and the specialized
  K3/LP/FDE proofs have reciprocal annex targets at
  `handbook/annex/p08/many-valued-supplement.tex:19-96`.  Relevance, IMLL,
  CLL, affine, and Lambek contexts/rules are not silently identified, and all
  referenced calculus sheets are routed once through
  `handbook/parts/p14/rule-sheets.tex:75-86`.  The adaptive-logic exclusion is
  explicit rather than a hidden omission.  Residual blockers are F10 and F11.
- **References and bibliography.** Static source inspection found that the
  citation keys used by the live Part VIII supplements, annex, and annotated
  further-reading route resolve in `handbook/bib/handbook.bib`.  The
  further-reading section states that it is navigation, not an authority
  transfer, at `handbook/parts/p08/further-reading.tex:7-37`.
- **Labels and reciprocal links.** Apart from the missing destinations and
  misleading navigation specifically recorded in F2/F3/F5, the reachable
  supplement/annex `ref` and `hyperref` consumers inspected at source level
  have matching live labels.  This is not a compiled-reference finding.

## Not checked / gates deliberately external

- TeX compilation, bibliography backend execution, makeindex output, and the
  final resolved-reference log;
- PDF hyperlink destinations, page-number accuracy, longtable continuation,
  landscape rotation, TikZ placement, float order, overfull boxes, glyph/font
  rendering, and other visual/page failures;
- final exact-byte provenance adjudication, human mathematical review, user
  acceptance, and the administrative disposition of register rows.

Those gates cannot cure the source/content blockers above, and static source
inspection must not be inflated into render acceptance.

REJECT
