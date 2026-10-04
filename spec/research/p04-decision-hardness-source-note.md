# P04 decision hardness: two stronger classifications

Assigned scope: new handbook/parts/p04/decision-problem-hardness.tex and
matching annex; unique p04-decision-hardness bibliography/symbol intakes,
this one source/working note, and disjoint source/references/p04-decision-hardness
captures. Prior LTL/Wald/locator/Chapter285 files and all shared files
were left unchanged. Root owns routing, canonical intake merging and
shared table/source-attribution updates.

## Completed mathematical content

Six reciprocal full proof pairs support the two requested classifications:

1. thm:p04-dh-stcon / annex:p04.dh.stcon: directed STCON NL-completeness.
   Explicit unary dimension/adjacency-matrix encoding, length-zero paths,
   malformed rejection, bounded nondeterministic membership and an actual
   always-valid polynomial-size configuration graph for each NL machine.
   Requested-bit reruns prove pullback/composition without storing output.
2. thm:p04-dh-complement / annex:p04.dh.complement: NONREACH in NL,
   NL=coNL and NONREACH NL-completeness. The census enumerates each vertex
   once, certifies only positive membership and requires the exact prior
   count; therefore no reachable vertex can be silently omitted. All
   counters, stage updates, N=1, and bounded branch termination are proved.
   Both graph languages reject malformed strings; whole binary-space
   complementation is derived using always-valid configuration outputs.
3. thm:p04-dh-two-sat / annex:p04.dh.two-sat: explicit 2-CNF SAT and
   valid-input UNSAT are NL-complete under logspace many-one reductions.
   The SCC iff criterion is independently proved with a topological-rank
   assignment. SAT upper membership uses the proved complementation result,
   not a linear SCC-time inference. Lower formulas have start/target units
   and edge implications. Malformed graph inputs map to constant valid
   instances of the needed polarity. Empty clauses/lists, r=0, s=t,
   edgeless graphs and very long atom-name normalization are handled.
4. lem:p04-dh-computation-validity / annex:p04.dh.computation: a valid
   deterministic machine accepts its input iff the emitted finite
   closed first-order sentence is unrestrictedly valid. Every left,
   stationary and right update, both missing tape-list ends and explicit
   blanks are supplied. A positive run gives a finite derivation in
   arbitrary models. A negative run gives an actual free ground-term
   model, total on unused signature symbols, with Reach exactly the
   represented run terms. All arbitrary variable assignments are covered.
5. thm:p04-dh-validity-complete / annex:p04.dh.validity: FO validity is
   c.e.-complete under total computable many-one reductions. The upper
   bound reuses the current complete proof-enumeration argument. The
   lower bound starts from every c.e. set's domain-machine definition
   and constructs its recognizer directly; it does not rely on the
   sketched arithmetic-history or c.e.-equivalent-forms theorems.
   A fixed countable effective signature, finite symbol use, exact
   prefix tags/self-delimiting fields and numerical code/inverse are
   given. Invalid/open input, zero code, empty word, empty transition
   table and empty/all-natural c.e. sets are treated.
6. thm:p04-dh-relational-validity / annex:p04.dh.relational:
   relational FO validity with identity is also c.e.-complete when the
   finite signature is encoded in the input. Total/unique graph axioms,
   constant parameter, term-value formulas, fresh-variable construction
   and both model directions are proved. Only unary Reach, binary and
   ternary graph relations and identity remain. No arbitrary individual
   fixed finite signature or identity-free monadic transfer is claimed.

The finite-validity example gives a separate explicit infinite model of
an injective self-map omitting a named element; its contradiction
implication is finite-valid but not unrestrictedly valid. This does not
alter the current relational Trakhtenbrot theorem.

## Current routed prerequisites actually read

- P02 propositional-metatheory-supplement.tex: explicit literal-reference
  definition, empty-clause case and cited thm:p02-two-sat SCC criterion.
  The new proof supplies the criterion afresh, not just its citation.
- P04 complexity.tex: current read-only-input/all-branches-halting class
  convention, resource classes and logspace reduction convention.
- restoration/inherited-07506-07677.tex: actual numerical input/output
  convention and def:partial-computable at line126. For an undefined
  function value its realizing machine must diverge, so a chosen domain
  machine is a valid recognizer without accepting malformed outputs.
- restoration/inherited-07753-07843.tex: c.e. set is a domain; the
  equivalent-forms theorem is a sketch and was not promoted into a proved
  premise. The needed domain-to-recognizer direction is supplied locally.
- restoration/inherited-08049-08080.tex: total computable many-one reduction.
- restoration/inherited-08248-08305.tex: cited general FO undecidability,
  complete proof-enumeration corollary, restricted-signature warning,
  and cited finite-validity distinction.
- Current parts/p04.tex driver hooks were read. thm:fol-validity-enumerable
  is attached to the ordinary source corollary, and thm:trakhtenbrot to
  the second ordinary source theorem, rather than to inactive legacy files.
- Current bounded-verification/c.e.-level-one arithmetic statements are
  sketched. Although external Q Sigma-one completeness is now proved,
  the reduction avoids the sketched Comp existence/effectivity dependency.

## Primary evidence and distinct versions

Immerman, Neil, “Nondeterministic Space Is Closed under Complementation”,
SIAM Journal on Computing17(5),935--938, October1988, DOI10.1137/0217058.
Author-hosted journal version:
https://people.cs.umass.edu/~immerman/pub/space.pdf
Capture immerman-1988-author-journal-version.pdf:
202548 bytes; SHA-256
c4c9cbffb1dd4022d7f0209a78917642f3539d13ecb35ffbe0a70a8c6e65ae85.
All seven reformatted pages were read, including Theorem1 and Lemmas1--2.
Proof pages2--3 were also inspected as actual page images to resolve
font-extraction damage. The proof here specializes and expands their
inductive-counting method to the explicit graph language; it does not
import the paper's historical open-question list as present status.
Bib key Immerman1988Complement is new. The separate conference/preprint
versions were located but are not falsely marked read.

Church, Alonzo, “A Note on the Entscheidungsproblem”, JSL1(1),40--41,
1936, DOI10.2307/2269326.
https://courses.fit.cvut.cz/MI-VYC/church-a-note-on-the-entscheidungsproblem.pdf
Capture church-1936-note.pdf:
85386 bytes; SHA-256
4d3e2951858d8645a2bacbfdf688a0154bcb49a39cbd6feb4fe0cd52dfbe8b3f.
All three PDF pages (cover plus printed40--41) were read. Its finite
axiom-conjunction/function-graph passage is historical context, not
the source of the new modern degree theorem. Canonical Church1936
denotes the distinct American Journal paper “An Unsolvable Problem...”;
the new correct key is Church1936DecisionNote, not a renamed old entry.
The publisher's opening extract and footnote3 of the separate
1936 correction, DOI10.2307/2269030, were read for the closure/scope issue.
A complete PDF was not acquired; no full correction reading is claimed.
The new graph axioms are explicitly closed and their model correspondence
is proved, so no historical suppressed-variable argument is a premise.

Turing, A.M., original “On Computable Numbers...”,
Proc.LondonMath.Soc.(2)42,230--265, existing bib key Turing1937.
https://www.astro.puc.cl/~rparra/tools/PAPERS/turing_1936.pdf
Capture turing-1936-1937-computable-numbers.pdf:
2369519 bytes; SHA-256
566cf0ddbf10807c2e6e303ea94cfd99d3a62514783a2d9262602b18bae44fc4.
Selected original Section11, printed259--263, was read in full from
page images, with the preceding printed258 boundary also inspected.
No claim of reading the entire36-page paper is made. The original
symbol-printing instance, configuration induction and reverse semantic
argument differ from the new accepting-state/two-list construction.

Turing, “...A Correction”, Proc.LondonMath.Soc.s2-43(1),544--546,
publisher volume year1938 (also historically cited1937),
DOI10.1112/plms/s2-43.6.544.
https://www.wolframscience.com/prizes/tm23/images/Turing2.pdf
Capture turing-correction-544-546.pdf:
293781 bytes; SHA-256
161f5befe23990fb38fd724bcd50b59bd358a4dd115121e36b95a8eccbb5d6ef.
All three actual pages were read. The changed preservation clauses,
added precedence relation, corrected induction and conjunction in place
of the original logical-sum wording were checked. Its remaining
real-number representation discussion is not imported into this unit.
Bib key Turing1938DecisionCorrection is new and keeps this source distinct
from the original Turing1937 entry. Publication year follows the actual
publisher record:
https://doi.org/10.1112/plms/s2-43.6.544

Aspvall--Plass--Tarjan1979 is the existing cited linear algorithm,
not the source of the new NL lower bound. The current routed statement
was read. Attempts to acquire the university-hosted PDF failed normal
TLS certificate verification; no verification bypass was used and no
abstract or metadata was represented as full-paper reading. The SCC
truth criterion is fully proved locally, and the stronger NL sources/
reduction chain are explicit. The older whole-source allocation remains
separate from the completed hardness proof.

## Integration destinations

Root can replace the shared master-table 2-CNF class attribution with
thm:p04-dh-two-sat, retaining thm:p02-two-sat for its distinct linear
literal-reference algorithm. The general unrestricted FO c.e.-complete
row can point to thm:p04-dh-validity-complete; the relational variant
has the narrower explicit statement thm:p04-dh-relational-validity.
Protected Chapter285's weaker lookup rows can likewise be strengthened
by root with these new proof links, not by worker edits to that chapter.

Scope-binding suggestions (all anchors are new actual source):

- P04 decision hardness resources: def:p04-dh-nl; keep disjoint from
  the machine-move-code meaning of the same mathsf-L glyph.
- P04 decision hardness graphs: sec:p04-dh-reachability.
- P04 decision hardness CNF: sec:p04-dh-two-cnf.
- P04 decision hardness validity: sec:p04-dh-first-order.
- P04 decision hardness SCC proof: annex:p04.dh.two-sat.
- P04 decision hardness computation proof: annex:p04.dh.computation.
- P04 decision hardness reduction proof: annex:p04.dh.validity.
- P04 decision hardness relational proof: annex:p04.dh.relational.

Where a symbol needs its body and annex lifetime combined, add the
corresponding annex region without merging conflicting local roles.
The intake has52 rows; first-use labels are real declarations, and
glyphs are actual mathematics TeX, not bare approximate text.

## Verification and remaining work

Six statement/proof pairs have full bodies. The author read-through
checks reduction polarity, positive-only census certification, countermodel
typing/freeness, blank-end updates, closure before implication, relational
freshness and both model directions. A scoped current-route plus
new-local-label check found no missing references or bibliography keys.
Driver hooks were traced to the actual source proofs, not treated as
proofs themselves. No whole-book build/render, review wave, child agent
or prose-mirroring test was run.

Remaining integration: root routing, bibliography/symbol merging and
master-table attribution updates. Whole-version readings not undertaken
above remain explicit source obligations; they are not necessary unproved
lemmas silently used by the new hardness arguments.
