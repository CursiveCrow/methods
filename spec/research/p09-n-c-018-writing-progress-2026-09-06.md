# N-c-018 writing progress, 6 September 2026

## Current manuscript and editorial direction

The authoritative presentation is
handbook/parts/p09/presentations/n-c-018.tex.
The reader-facing text is being developed into corrected definitions,
arguments, and worked mathematics. Source defects and the provenance of
repairs belong in research notes, not in place of those arguments.
Earlier dated reconstruction-closure statements do not establish
completion of the expanded mathematical treatment.

## Additions in this pass

- Typed model interpretations and variable environments, complete Boolean
  and modal denotations, and the behavior of boxes and diamonds at dead ends.
- Proofs of the least-pre-fixed and greatest-post-fixed characterizations,
  fixed-point complement duality, comparison under operator inclusion,
  polarity through nested binders, and capture-avoiding substitution.
- Transfinite approximants with a stabilization argument, finite-state
  change bound, and an explicit treatment of the apparent all-ordinal union.
- A fully specified countable chain model, the exact finite approximants,
  closure ordinal omega+1, and failure of omega-continuity. The
  well-foundedness interpretation states the dependent-choice use.
- Proofs of the PDL star identities and the filtration argument separating
  well-foundedness from PDL.
- An explicit all-false-proposition realization of Figure 2, with both
  edge families and the full calculation that the second fixed-point
  formula denotes exactly the even states. The separate PDL finite/cofinite
  argument remains to be expanded.
- A complete semantic soundness proof for the equational calculus, including
  the distinction between whole-predicate induction and a local implication.
- All six Proposition 5.7 laws, with derivations, fresh-binder conventions,
  the independent invariant parameter, and the proof-theoretic consistency
  consequence used by the tableau construction.

## Corrections to existing passages

The Kozen tableau labels are raw subformulas of the original input with
their unique binder links. They are not all members of the separately
closed unfolding family CL(p0). The latter choice would prevent the
binder/body and bound-variable rules from operating as stated.
The raw-label definition and body-exposure rule have been corrected.
The terminal rejection condition now explicitly includes the false
constant 0, with negated Boolean constants normalized before expansion.
Without that case the previously stated procedure accepted the input 0.
The source's zero-flag applicability guard for a nu-variable expansion
is also explicit, with minimal mu X.X and nu X.X executions showing
rejection versus acceptance.

The polarity and substitution arguments now include the ordinal-stage
constructor as well as least and greatest fixed points. Pointwise
operator comparisons extend to approximants by transfinite induction.

The model-to-consistency direction of Theorem 6.3.1 now points to the
soundness proof actually supplied in the manuscript.

In the Emerson--Jutla presentation, the fixed-point and modal-closure
clauses already use the corrected symbols. Their descriptions no longer
interrupt the reader with the duplicated-nu and mismatched-variable
printing errors. The original defect evidence remains in
p09-emerson-jutla-1991-source-note.md.

## Sources and evidence

The existing Kozen source record is p09-kozen-1983-source-note.md.
A fresh source reading checked Proposition 5.7 and rule 5.6 directly
against printed pages 341--342 of the primary Cornell scan:
https://www.cs.cornell.edu/kozen/Papers/mu.pdf
The exact formulas, side conditions, full printed algebraic route,
and a shorter derived proof of strengthened induction are appended there.
The manuscript uses the shorter argument after proving unfolding.

The semantic arguments are written for arbitrary state sets where stated,
not merely imported from the finite BDD evaluator in N-c-017.
No manuscript build, render inspection, or software tests were used.

A bounded mathematical reading found the missing false-constant rejection
case and omitted ordinal-stage semantic induction case; both were repaired.
It reported no other defects in the reviewed fixed-point, substitution,
stabilization, continuity, filtration, derived-law, and consistency
arguments. Figure 2's frame and raw tableau labels were separately
confirmed against the primary source, and its fixed-point calculation
has a complete supplied proof. The PDL finite/cofinite proof remains open.

A final bounded recheck confirmed the repaired ordinal-stage induction,
constant normalization/rejection, nu-flag guard, minimal tableau runs,
and Figure 2 fixed-point calculation, with no concrete mathematical
defect reported. It did not treat the PDL finite/cofinite assertion
as proved and did not grant topic acceptance.

The Bradfield--Stirling accessible document is now identified in both
the presentation and bibliography as the preprint dated 15 November 2005.
The published 2007 chapter metadata is retained, while internal section
and theorem locators are explicitly attributed to the accessible text.

## Further completed writing

The PDL finite/cofinite argument is now fully supplied and incorporated.
Its separate development is p09-kozen-figure2-proof-note.md. An independent
mathematical challenge checked the complete proof, and a later read-back
checked its actual LaTeX incorporation. The argument includes arbitrary
finite nesting of program tests, iteration, and converse; it is not a
finite-modal-depth substitute. The intermediate bi-infinite word lemma
has an explicit lower-bound estimate, so the final witnesses remain in
the stated half-line model.

The closure and activity treatment now gives the exact sequential
inner-to-outer substitutions, all seven closure conditions, the closure
and leastness proof, activity's transitivity and prefix property, and
the variable-order conventions. The source's variable/replacement slash
order is converted explicitly to the book's replacement/variable order.

The counter treatment now supplies all eight update clauses. Counter
identities, their mutable values, shared nu-flags, local order, global
shuffle, collisions, and dependent resets are distinguished. It proves
finite increment/reset counts for each individual mu-identity using
radix N+1, and finite nonmodal saturation through an outermost infinitely
unfolded variable. A finite-configuration greatest-fixed-point
construction then decides nonrejection and gives the exponential-time
simulation.

The primary source explicitly allows infinite computations across modal
steps. The book no longer treats the nonmodal saturation lemma as global
halting. A nu X.<a>X execution demonstrates the difference. An erroneous
auxiliary source claim about a collision chain of nu-counter identities
is documented in the source note; the supplied saturation proof does
not use it. No unsupported exact numeric constant is inferred from
the source's compressed counter-counting argument.

Bradfield--Stirling now has explicit syntax/system/environment data,
bisimulation invariance proved by matching transfinite approximants,
the image-finite converse proved by finite distinguishing conjunctions,
and the full labelled-path unravelling construction. The open-formula
case uses a pulled-back environment. A bounded reader checked these
arguments and prompted the explicit HML scope, root-index convention,
and open-environment additions.

## Final bounded check

The final bounded review of closure, counter updates, event bounds,
nonmodal saturation, and configuration-graph nonrejection found two
repair items: the event bound must not be called a finite identity
lifetime, and shared nu-flags require a deterministic collision
convention for the one-successor administrative simulation.
Both are corrected, with origin-based, identity-renaming-invariant
collision ordering. A follow-up mathematical reading found those
repairs and the exponential nonmodal-segment bound sound.
Primary-source rechecking also confirmed that immediate pre-collision
overflow rejection was not stated; the book explicitly checks live
counters in the completed successor configuration.

The separate truth/model-construction implication is still outstanding;
the simulation result does not stand in for that proof.

## Game and model-construction continuation

The model-checking game now has every move, terminal outcome, free-variable
exit, and priority assignment explicitly defined. Its truth theorem is
proved in all four least/greatest, true/false binder cases using ordinal
entry/exclusion ranks. A bounded mathematical check found only that a
strategy's domain must exclude terminal owned positions; that was fixed.

The separate positional-determinacy proof applies to arbitrary set-sized
total arenas with finite priority range, including infinite branching.
It supplies uniform positional dominions, closes removed unions again
at limit stages, and proves termination of strategy switching by ordinal
entry stages and attractor ranks. The proof is in
p09-parity-determinacy-proof-note.md and has been independently checked.
It is now incorporated with the priority reversal, model-checking
corollary, and bounded-branching tree-model proof.

The nonrejection-to-model direction is now written in full: uniform
mu-collision-chain ranks, the selected tree and first saturated root,
ordinal-closed labels, all six saturation conditions, the complete
parameterized truth lemma, and a finite model obtained from the positional
configuration strategy. Its ordinary ancestor-or-self backedge
representation has a proved exponential underlying-tree-depth bound.
An independent reader checked that direction and its actual incorporation.
The local counter lookup was made explicit because the enclosing-variable
list is longer than the active-counter sublist. Boolean constants keep
their fixed interpretations, independently of raw-label membership.

The consistency-to-nonrejection direction is not complete. A separate
review found that inherited provisional lists must be used before the
incoming-body collision in the annotation step; that local proof has
been repaired in the source note. The global overflow argument still
does not establish the needed comparison across modal edges.
Equal raw labels and unchanged higher annotations do not suffice.
No unproved version of that argument was incorporated into the book.

## Automata and context-counting continuation

The actual LaTeX now defines modal alternating parity automata with
depth-one guarded transitions, their acceptance games, and their
set-indexed runs. It proves game/run equivalence on arbitrary set-sized
models, complementation, union and intersection, and works out both
well-founded universal safety and infinitely-often/finitely-often examples.
Finite branches and both modal dead-end cases are explicit.

The formula-to-automaton direction now has a complete construction for
closed formulas that may be unguarded. Finite local syntax games produce
monotone winning functions on colored modal exits. Their positive truth-table
summaries become guarded transitions. The proof distinguishes actual
control parity on infinite local episodes from minimum-priority summaries
of completed finite episodes, resets the summary at every model move,
and proves the block-minimum lemma. Both strategy directions are supplied,
including exact realizable supports in the forward direction and a
noncircular virtual-history construction in the reverse direction.
The section includes a finite effectiveness argument and a crude explicit
transition-table bound. The complete proof note is
p09-mu-epsilon-elimination-proof-note.md.

A bounded independent reader checked that note and then the actual new
LaTeX in full. The two incorporation clarifications were made: Boolean
constants are explicitly covered in the forward terminal argument, and
the two component proposition alphabets are defined before their use.
This is mathematical source-text review, not a build or PDF inspection.

The consistency investigation now supplies a complete alternative proof,
not merely a report of the unresolved original-bound recurrence.
The reader-facing text explicitly parameterizes the tableau by its finite
cap and distinguishes the source cap N = 2^m from the context-counted cap
M = 2^m (m^2+1)^(m^2). The latter is now incorporated as a separate,
fully stated procedure with exactly the same input class and structural
rules. It records closed annotation values, inherited-old contexts before
incoming-body collision, weakening on disposal and reset, and fixed
higher-identity signatures. Equal signatures at two unreset surviving
increments contradict consistency, even across modal intervals.
The finite signature count excludes overflow at M.

The model proof is explicitly parameterized by a finite cap T. Its
identity and continuation bounds transfer to M, giving consistency,
nonrejection at M, and finite directed satisfiability as equivalent,
with 2^(O(m^4 log(m+1))) configuration, model, and decision-time bounds.
The annotations are proof objects, not additional algorithmic state.
The supporting investigation is p09-kozen-consistency-investigation.md.
A separate bounded mathematical reader checked the investigation against
the actual local rules and model proof and validated that threshold transfer.
The actual incorporation was then read independently. Its definition
bridge now explicitly quotients raw occurrences into tableau formula keys,
with representative-independent active lists and ordered translations.
The final theorem repeats the positive-normal and renaming conventions,
and the encoding count explicitly distinguishes counter entries from
the number of values in each entry's range.

The original N = 2^m global recurrence is still not established by this
reconstruction. The sufficient M bound is not a recovery of that sharper
claim. The old source-theorem proof summary was replaced by the supplied
context-counted proof; source-specific limitations stay in these notes.
No manuscript build, render, software test, commit, or push was performed.

## Completed reverse automaton translation

The actual presentation now supplies the other direction of
Bradfield--Stirling Theorem 5.2 at sec:p09-mu-automaton-to-formula.
It constructs an ordinary scalar parity formula on a tagged finite
control product, including exact proposition-letter guards, all finite
terminal cases, source-priority recording after model moves, and both
history-dependent strategy translations. The least-recurring priority
comparison is explicit and does not assume positionality.

The binary Bekić identity is proved for both least and greatest fixed
points on complete lattices. Finite induction produces scalar syntax
for every component, with capture avoidance and external parameters
preserved. A componentwise structural induction then removes control
tags and tagged action symbols through the complete-lattice isomorphism
P(S x Q) = P(S)^Q. Each product binder becomes a simultaneous same-sign
block before it is scalarized; unlike fixed-point signs are never
silently commuted. A direct nested equation-system expression makes
the resulting construction explicit in the original vocabulary.

The section includes a two-control all-even elimination calculation
with distinct box/diamond dead-end behavior, and a two-state calculation
showing that exchanging the least/greatest binder order changes the
denotation from the full state set to the empty set.

Primary locations and supplementary elimination sources are recorded in
p09-mu-automaton-to-formula-source-note.md. The separate supplied algebraic
derivation is p09-mu-bekic-elimination-proof-note.md. The primary preprint
states the expressive-equivalence theorem and ordered block semantics;
the detailed product-game and elimination proofs are supplied here.

A bounded independent reader checked the actual new LaTeX in full and
found no mathematical defect in the construction, elimination proofs,
semantic induction, or examples. Three wording repairs were made:
the component translation is explicitly restricted to its positive-normal
tagged-action vocabulary; the cross-reference names the earlier
formula-to-automaton direction; and true constant guard terminals are
included alongside true literals. No manuscript build, render, software
test, commit, or push was performed.

## Full semantic automaton normal-form construction

The actual N-c-018 LaTeX now contains the full effective semantic route
from an arbitrary closed formula to guarded, well-named ANF, with all
three transformations written as constructions and supplied proofs.

The cover section defines its witness and covering requirements, finite
and empty targets, omitted action labels, and the successor-first box
choice. Cover transitions are explicitly a different one-step constructor
language from the earlier grammar of Boolean combinations of modal state
atoms. No equation identifying [a](q or r) with [a]q or [a]r is used.

The all-traces monitor begins with an explicit nondeterministic Büchi
recognizer for a bad relation-word trace. It reuses the existing proved
Safra expanded-manuscript construction in N-c-013, now given the precise
label sec:p09-safra-determinization. Complementation uses the unique total
deterministic run. A full least-recent-first record proof then converts
the complementary Muller condition to least-recurring parity, with the
pre-move suffix, emitted successor-state color, initial composite state,
finite-prefix convention and finite size bound explicit.

The general cover simulation uses simultaneous obligation sets and
relation-valued successor profiles, not bare subsets without trace history.
Universal box pairs occur in every profile; every diamond pair has a
profile witness. The relation itself remains in the target control so
distinct profiles cannot be silently identified. The two strategy proofs
preserve acceptance in the same pointed model, including arbitrary
branching, empty obligations, empty profile families and modal dead ends.
The forward proof treats pairs in B_a first, even if they also occur in
I_a; only profiles outside B_a require the canonical diamond witness.

The final cover-to-ANF construction uses separate real model moves and
deterministic control switches in its proof product, preserving the box's
choice order. Component semantics removes both auxiliary actions.
The base component bodies are ANF clauses with every coordinate variable
guarded. Substitution closure, the guarded same-sign Bekić invariant,
and downward simultaneous-block elimination yield a closed, guarded,
well-named formula in the original vocabulary. The final composition is
semantic equivalence, not a claim of derivability in Kozen's calculus.

Primary-source conventions and the exact later cut/equisatisfiability
statement are in p09-mu-automaton-normal-form-source-note.md. The new
supporting proof notes are p09-mu-parity-trace-monitor-proof-note.md and
p09-mu-cover-anf-proof-note.md. The bibliography now records the original
Janin--Walukiewicz paper, with internal locators assigned to the acquired
author-hosted version.

Bounded independent actual-LaTeX readers checked the monitor and the
cover-to-ANF section. The monitor's initial composite state and the ANF
grammar's finite action-index set were made explicit. The distinct
general simulation received its own actual-text mathematical reading.
That reader found the box/diamond overlap wording issue and confirmed
the actual disjoint-case repair; no remaining mathematical defect was
found in the simulation's reviewed scope. The normal-form composition
now has independently checked component proofs in the actual LaTeX.
No manuscript build, render, software test, commit, or push was performed.

## Completed ANF cut theorem and finite-model restoration

The actual LaTeX now proves the exact cut/equisatisfiability theorem for
closed, guarded, well-named ANF. Each variable occurrence is classified by
its original binder kind before erasure; whole fixed-point subformulas are
not replaced by constants. Nested outer-variable references retain their
original classification.

The fixed-point-free Boolean calculation is proved by structural induction,
with disjoint target-model witnesses and a fresh root for each consistent
literal/distinct-action cover clause. The necessity proof constructs a
finite model-free game on original primitive occurrences, transports a
satisfying-model evaluation strategy through mandatory diamond witnesses,
and then uses positional determinacy. A first selected mu-variable leaf
would give a repeatable odd binder-to-variable cycle, so the selected cut
tree has only true variable leaves. Cover-expansion copies and original
binder links are explicit.

For sufficiency, true cut values select a finite syntax tree with no
mu-variable leaves. Restoring nu-variable ancestor returns creates a graph
whose administrative subgraph is acyclic by guardedness. The endpoint map
h defines finite model states, valuations and real action edges. Its
same-state invariant handles variable returns; after a box successor is
chosen, a corresponding target occurrence supplies the existential cover
choice even when duplicate edges have collapsed. All recurring variable
priorities are nu-priorities. This proves truth of the original ANF.

The supplied finite model has at most n states and at most one labelled
edge per original cover-target occurrence, where n is the original ANF
size in cover notation. The Boolean decision is O(n) with integer
proposition identifiers and supplied original binder links or binder-kind
tags; arbitrary string symbol-table costs are separate. Composing with
the already proved effective same-model normal-form transformation gives
decidable satisfiability and the finite-model property for the full modal
mu-calculus, without transferring the ANF-linear bound to its shorter
pre-normalization input.

Worked examples distinguish cut equisatisfiability from same-model truth,
mu-variable regeneration from reopening a mu-binder, and the independent
necessity of excluding bound-variable literal conjunctions and repeated
cover actions. Their original formulas are not mislabeled as ANF.

The supporting notes are p09-mu-anf-cut-source-note.md,
p09-mu-anf-cut-necessity-proof-note.md, and
p09-mu-anf-cut-model-proof-note.md. Separate bounded readers checked the
actual necessity and sufficiency passages, with no mathematical defects
reported in their scopes. A third source/representation check prompted
the explicit binder-link assumption in the linear-time paragraph.
No code, software tests, manuscript builds or renders, commits, or pushes
were performed.

## Completed contextual pre-model and ordinal-signature treatment

The actual presentation now defines the canonical binding environment for
raw subformula occurrences, with binders assigned outer-before-inner and
genuinely free variables retaining their external valuation. A full
binder-depth/first-external-exit proof identifies canonical truth with the
original linked evaluation game's winner at every original occurrence.
This avoids treating variables bound elsewhere in the input as arbitrary
free terminals, or making the later inner assignments change an outer
binder's denotation.

The pre-model definition now has actual literal, constant and genuinely
free-variable terminal checks; both Boolean annotation equivalences;
the correct modal obligations; original binder links; and one positional
choice function on state/occurrence pairs. Every infinite trail from every
label is subject to the global parity condition. The full truth theorem
and its converse use the linked-game lemma and a uniform winning strategy
on the whole winning region. The source's direct variable/body dependency
is explicitly subdivided through the binding occurrence. No guardedness
restriction is introduced into this general pre-model theorem.

The ordinal-signature characterization is proved in both directions for
arbitrary set-sized dependency graphs and finite priority ranges. Its
comparison uses the source-priority prefix. For each odd j, finite paths
whose edge-source priorities stay at least j and visit j define a
well-founded relation; its ordinary ordinal rank gives a stronger
coordinatewise-prefix certificate. The converse uses the weaker stated
lexicographic condition. Dependent choice, terminal outcomes, the common
ordinal bound, root-only reachability, and finite N-1 ranks are explicit.
The examples include accepting resets, an infinitely branching graph
requiring omega, and unguarded nu/least loops. The ranks are not identified
with least semantic-approximant entry stages.

The source note is p09-mu-premodel-source-note.md and the separate graph
proof is p09-mu-premodel-rank-proof-note.md. One independent reader checked
the contextual valuation and original linked-game proof, then the actual
pre-model insertion. Another independently derived the rank construction
and checked its actual incorporation. The sole incorporation precision
was changing compatible evaluation plays to maximal compatible plays,
matching the defined notion of trail; it was fixed in the LaTeX.
No code, software tests, manuscript builds or renders, commits, or pushes
were performed.

## Completed alternation definitions and strictness proof

The actual presentation now proves the class inclusions, syntactic duality
with its open-environment qualification, level-one characterization,
and exact symmetric-depth convention. It gives exact simple-class indices,
the closed-fragment characterization for Emerson--Lei, and a substitution-
stable Niwinski dependency lower bound sufficient for the examples.
Each example has both membership and nonmembership derivations, with its
two minimum indices and symmetric depth displayed. The finite action
alphabet contains the displayed action, and the EL proof handles level zero
separately. A two-state model distinguishes the first two formulas' meanings.

The semantic strictness proof now replaces the former arithmetic-route
summary. The first level uses the closed tree languages of nu-only formulas
and a least-fixed-point reachability language with a missing limit tree.
For every n >= 2, finite open recursion graphs realize the actual Niwinski
generation rules inside the required priority interval, including capture-
safe substitution, arbitrary body-graph binding and interval-preserving
elimination of internal moves. Open graph letters include the truth values
of their free-variable exits. On full binary trees, terminal outcomes are
replaced by absorbing controls within the same interval.

The simple alternating-prefix game formula W_n is a witness in Sigma_n^S.
Padding each competing automaton transition gives a productive game-tree
map with one extra level of prefix agreement. Its fixed tree is constructed
directly by stabilized-prefix iteration. The complement diagonal excludes
all Pi_n^N competitors. Extra vocabulary is restricted by class-preserving
constant instantiation, and uniformly equivalent open competitors reduce
to the closed case. The full finite-model property supplies a finite
distinguishing model for each competitor.

The public theorem thm:p09-mu-alternation now states the simple-class
witness and finite-system conclusion and links to the supplied proof.
Arnold's primary article is recorded in the bibliography.
The supporting notes are p09-mu-alternation-classes-proof-note.md,
p09-mu-alternation-strictness-source-note.md,
p09-mu-binary-diagonal-proof-note.md, and
p09-mu-niwinski-index-proof-note.md.

Separate readers checked the actual class calculations, the fixed-index
construction and the diagonal proof. The incorporation repairs specify
the EL zero case, fragment-word bounds, the nonempty action alphabet,
open-exit truth values, extra vocabulary and the final equivalence chain.
The reviewed proof components now establish the displayed strictness result.

## Completed Emerson--Jutla constructions and determinacy arguments

The actual N-c-018 LaTeX now supplies the layered formula automaton,
including directional EX/AX expansion, transition disjunctive normal form,
accepting and rejecting sinks, every-letter totality, both strategy
translations, and the conversion from least-even parity to the source's
Streett acceptance. The history-free conclusion follows from positional
parity determinacy before acceptance is presented as Streett. The ambient
alphabet includes unused letters, and an explicit empty-alphabet case
covers the otherwise vacuous input class.

The reverse construction for general ordered binary-tree automata uses
the separate directions 0 and 1. A finite permutation record converts
Rabin acceptance to parity, and the existing reverse modal construction
gives a directional formula. Singleton letter observations and the full
ambient alphabet are retained through complementation. The root-child
separator proves why unindexed EX/AX cannot express arbitrary ordered
tree languages.

The parity fixed-point formulas are proved for total set-sized bipartite
arenas with paired colors. The I and II binder prefixes, n = 0 case,
OR-round predecessors, general reach-target versus avoidance duality,
restricted safety regions, and targets on intermediate vertices are
explicit. The residual-game quotient transports named moves and yields
the source's history-free strategies.

The F-sigma treatment supplies both constrained fixed-point games, the
dual nested regions, ordinal descent for I's phases, and II's successive
closed-component violations. Prefix trees are formed from complete play
histories, so leaving one is permanent. The bounded-color specialization
proves I's global finite bound and II's unbounded-color strategy.

The general alternating-to-nondeterministic construction now has a full
all-thread proof and parameter counts. Original Streett controls receive
a finite full-state permutation record before positional choices are
merged into obligation sets. A bad-trace word automaton and Safra
determinization yield a deterministic good-trace monitor. The new
pair-response record operates on the monitor's pair names, avoiding a
factorial in its much larger state set. The record's full product,
current-state update, simultaneous response order, zero-pair case and
Rabin acceptance conversion are explicit.

Partial inputs are normalized with n <= n0 + 2,
m <= m0 + (n0 + 2)|Sigma|, and k = max(k0, 1). All displayed asymptotic
counts use normalized n, m, k. With S = n n! (2n + 2), B <= S(n + 2)
and M the deterministic bad-trace monitor size, the constructed automaton
has at most (2^S - 1) M B! (2B + 3) OR controls, at most that count times
m^S AND choices, and B + 1 Rabin pairs. Both acceptance directions
preserve every compatible thread through the exact endpoint invariant.

Supporting notes are p09-emerson-jutla-formula-automaton-proof-note.md,
p09-emerson-jutla-layered-game-proof-note.md,
p09-emerson-jutla-parity-formulas-proof-note.md,
p09-emerson-jutla-fsigma-proof-note.md,
p09-streett-response-record-proof-note.md, and
p09-emerson-jutla-nondeterminization-proof-note.md.
Bounded independent readers checked the actual LaTeX constructions.
Their incorporation corrections were applied to the product declaration,
ambient alphabet and singleton coding, strategy scope, and edge cases.

## Completed full-calculus axiomatization treatment

The section now states Walukiewicz's weak completeness theorem for the
entire finitary modal mu-calculus, with the paper carrying the cited proof.
The source's meet-based order notation is identified with the book's
join-based abbreviation, and its K1--K6 rules are matched to the existing
equational calculus.

The theorem is stated for all models, environments and states, and gives
both validity/theoremhood and unsatisfiability/refutability. The text derives
the equation and inequality consequences and the exact finite-premise
local-consequence statement.

The source's Fact 17 and Theorem 26 identify the required provable
normalization and the implication from the input formula to its
semantically equivalent disjunctive form. This is the cited deductive
bridge; the independently supplied semantic ANF construction is not
silently used as a proof of derivable equivalence.

A complete noncompactness example uses finite reachability to p together
with the demand that every finite a-depth satisfies not p. Each finite
subset has a finite chain model; the whole set has none. This proves why
weak completeness cannot become arbitrary-premise strong completeness
for a sound finitary consequence calculus.

The Part VIII system card now states weak completeness explicitly and
links to this treatment. The source alignment is recorded in
p09-walukiewicz-completeness-source-note.md.
An independent reader checked the actual insertion against the primary
theorem and rules, and checked the finite-premise and noncompactness
arguments. Its requested author-version locator qualification is now
explicit in the text.

## Remaining substantive writing

- The book now has the complete context-counted consistency-to-nonrejection
  proof. Recovering the original source threshold is a separately open
  sharpening, not something proved by the larger-cap argument.
- Reconcile the exact imported tree-like convention in Kozen's cited
  sources. The proved ordinary ancestor-backedge representation does
  not assert a no-nesting/no-crossing restriction.
- Complete independent mathematical/source review and the separate
  publication requirements. No whole-topic acceptance is claimed.

REGISTER STATUS: OPEN
