VERDICT: ACCEPT

# N-c-016 integrated source-fidelity review, Round 4

## Scope of this verdict

This is a fresh, text-only verdict on the frozen current LaTeX presentation in
`handbook/parts/p09/presentations/n-c-016.tex`.  The verdict is bounded by the
current manuscript source, its directly relevant host and inherited CTL/CTL*
definitions, the five named source/acquisition notes, and the five exact
bibliography entries.  Within that boundary, I found no remaining
source-fidelity must-fix.

Acceptance means that the current presentation keeps the five source states
separate, reproduces or reconstructs their mathematical content at the strength
supported by the authority notes, states the hypotheses and proof boundaries
needed by the displayed results, and distinguishes handbook-supplied typing or
proof completions from literal source text.  It also means that the current
technical names and abbreviations pass the supplied necessity/definition/
standing/nonredundancy/use rule at the points where they are introduced.

Acceptance does **not** establish a successful TeX build, a clean PDF, visual
layout, publication permission, a newly acquired 1999 book body, independent
revalidation of the source notes' external-access observations, mathematical
correctness beyond the source-and-handbook claims reviewed here, or final
register admission.  No such operation or determination formed part of this
review.

## Integrated source-state and hierarchy findings

The file has the right host hierarchy.  Its umbrella heading at lines 3--4 is a
`\subsection` within the host's existing model-checking `\section`; the five
individual presentations are `\subsubsection`s.  The host inputs N-c-016 at
`logic-in-computer-science.tex` line 1517, after the immediately preceding
presentation input and before the new `Program logics` section at lines
1521--1522.  The presentation therefore does not escape or duplicate its host
section.  Its labels and its references to the host CTL method and theorems are
consistent with the definitions and statements at host lines 948--1033.

The five source states remain noninterchangeable:

- Lines 9--18 distinguish the Clarke--Emerson 1981 workshop event, the 1982
  LNCS publication, the authorized 2008 reprint, and the separate longer author
  manuscript.  No result available only in the longer manuscript is presented
  as printed in the twenty-page chapter.
- Lines 492--499 distinguish the original Queille--Sifakis body, the 2008
  reprint, the page-authenticated institutional scan, the unresolved
  distribution authorization of that scan, and the uninspected
  subscription-only reprint pages.
- Lines 886--892 distinguish the 1986 JACM article from the 1983 preliminary
  paper and the two 1984 reports and preserve the archived ACM body's
  conditional-copying, non-open-licence status.
- Lines 1457--1478 are a genuine acquisition boundary, not a synthetic
  presentation of Clarke--Grumberg--Peled.  They make only route-bounded access
  and contents-locator claims, explicitly deny body-level support for formulas,
  algorithms, proofs, examples, and complexity assertions, and do not substitute
  the Clarke--Schlingloff chapter, the Clarke--Grumberg--Long survey, the 2018
  second edition, or Baier--Katoen for the unavailable first-edition body.
- Lines 1480--1489 identify the complete Baier--Katoen source, its
  all-rights-reserved status, and the corrected chapter/page boundaries.  They
  do not convert anonymous institutional availability into a republication
  licence.

The bibliography entries at `handbook/bib/handbook.bib` lines 2393--2458 agree
with those identities.  In particular, `ClarkeEmerson1981` records the 1982
LNCS publication while the prose preserves the 1981 event year;
`QueilleSifakis1982` has the correct title, LNCS 137, pages, year, and DOI;
`EmersonHalpern1986` has the correct JACM volume, issue, pages, year, and DOI;
`ClarkeGrumbergPeled1999` names Doron A. **Peled**, not the defective `Peleg`
publisher metadata, and records the 1999 MIT Press identity and correct ISBN;
and `BaierKatoen2008` records the 2008 MIT Press book and correct ISBN.  Each
entry's access note stays within the corresponding authority note.

## Clarke--Emerson fidelity

Lines 20--39 define the source's synchronization skeleton at its proper
standing as a per-process finite program abstraction, distinguish it from both
the computation tree and the later finite global system flowgraph, explain why
the distinction is necessary, and identify its use in factorization.  Lines
41--60 retain the countable source state space, a positive finite number of
processes, the process-indexed relations, their total union, infinite paths,
and process-labelled computation-tree arcs.  Lines 62--124 reproduce the
process-indexed primitive CTL grammar and strong, current-inclusive until
semantics, and keep the printed `V`, `AF`, `EF`, `AG`, `EG`, indexed-next, and
unindexed-next forms derived rather than primitive.  The possible vacuity of
`AX_i` when process `i` has no successor is both correct and used later.

The finite-state algorithm at lines 126--183 keeps finite model checking
distinct from tableau satisfiability.  The universal and existential
approximants include the required left-operand guard.  The existential
recurrence is explicitly identified as a reconstruction from the base case
and guarded loop, while the source's defective displayed universal recurrence
is recorded rather than copied or silently presented as literal text.  The
stabilization and quadratic source bound are not replaced by the later
edge-sensitive linear bound.  The worked `AFb \land EGa` calculation at lines
185--197 matches the source graph and the four stated snapshots.

Lines 199--234 preserve the two extension boundaries.  `E^\infty Fp` is not
put into the base grammar, Proposition 4.1 retains finiteness and the exact
self-loop/nontrivial-SCC condition, and Proposition 4.2 is limited to
NP-hardness for the arbitrary-linear-path-prefix extension.  Its graph
construction is complete: it retains `E`, adds fresh `u_1,u_2`, adds exactly
`u_1 -> v_i`, `v_i -> u_2`, and `u_2 -> u_2`, assigns only `p_i` to `v_i`,
and gives the exact visit-every-vertex/visit-no-vertex-twice formula.  Neither
NP-completeness nor a later full-CTL* result is inferred.

Lines 236--318 keep the tableau an outline.  `Blocks`, `Tiles`, alpha, beta,
elementary, nonelementary, and downward closure receive their source standings
and exact available definitions; the publication's single concrete `Tiles`
construction is not inflated into the fuller manuscript's process-indexed
rules.  The exponential label count is only a termination/size warning, and
the worked `EFp \land EF\neg p` tableau is not promoted to the omitted general
correctness proof.

Lines 320--487 reproduce all nine mutual-exclusion requirement groups with
their process indices and preserve the semantically redundant but literally
printed ninth group.  The model fragment is defined as a finite construction
artifact and explicitly distinguished from a complete model.  `TURN` has a
necessary source role, exact state-label standing, nonredundancy, and later use
in enabling conditions.  The displayed `P_1` skeleton and the general
factorization use arbitrary local indices `u,v`, handle the one-process empty
conjunction, preserve auxiliary assignments, and do not turn the worked
construction into a general synthesis-correctness theorem.  The concluding
algorithm, proposition, tableau-outline, and synthesis statuses remain
separate.

## Queille--Sifakis fidelity

Lines 501--527 define an interpreted Petri net exactly far enough to distinguish
it from an ordinary net: the all-variable vector, guards, assignments,
transition firing, and true/identity omitted inscription are typed and used.
The translator's asserted safety, missing translation grammar/proof, and the
undefined format of `diagnostics` are all retained as boundaries.

Lines 529--569 give the alternating-bit protocol only at the source-supported
level.  The bold all-variable vector and the sender's scalar `X` are explicitly
distinguished; `Y`, `Z`, `M`, `MM`, `AA`, the `.B` projection, `SENDER`, and
`RECEIVER` have stated program standings.  Every action name subsequently used
by `enable` or `after` is declared as the corresponding event: `send`,
`repeat`, `receive`, `accept`, `repeatack`, `sendack`, and `receiveack`.  The
last is correctly used as the repair of the source's two `receivack` typos,
which are recorded at lines 748--752.  The prose non-loss assumption is not
turned into a fairness clause or a property of the displayed line processes.

Lines 571--635 preserve the source's unary state-formula language and its
absence of next, until, and a separate path-formula type.  The handbook's
completion of the omitted execution start/adjacency clauses is declared as a
completion.  The new index-set abbreviation
`D_s={k in N : s(k) is an actual position}` is exact and eliminable; its
standing, finite/infinite cases, necessity relative to the fictitious
post-terminal `omega`, nonredundancy from the source's reachability guard, and
use in all four temporal clauses occur together.  Consequently no formula is
asked to hold at `omega`.  The missing printed Boolean interpretation clauses
are recorded rather than attributed to the display.

Lines 637--752 distinguish source predicates `Init`, `enable a`, and `after a`
from temporal operators; define the finite action-family and process-action-set
notation; supply explicit nullary conventions as reader-facing conventions;
and reproduce the invariant, liveness, deadlock, and response families with
the correct conjunction/disjunction and `POT`/`INEV` strengths.  Enablement is
never strengthened to eventual execution, and no fairness is smuggled into
the formulas.

Lines 754--816 give `pre`, its Boolean dual, identity, pointwise transformer
union/intersection, finite iterates, and the literal superscript-`x` operation
with their exact standings.  The four formulas retain image-finiteness, the
sink-sensitive existential-predecessor factor, and the fact that their proofs
are delegated to Sifakis's 1979 report.  Lines 818--881 preserve the missing
net-reduction and IPN-to-`pre` artifacts, reproduce the sole complete
calculation with all place predicates, one-token invariants, and the correct
`P_0`, `pre(P_0)`, and `P_1` values, and retain the implementation's iteration
cap and possible no-answer outcome.  No asymptotic theorem, total-answer
theorem, satisfiability calculus, or synthesis result is invented.

## Emerson--Halpern fidelity

Lines 894--1004 keep Lamport's shared syntax and its branching and linear
semantic types distinct, including the difference between primitive
`sometimes` and derived `not never`.  Whole-model strong equivalence is not
substituted for pointwise equivalence, and the source's suffix, fusion, limit,
`R`-generability, and state-completeness properties have structure/path
standings rather than object-language standings.  The compatible string
decompositions and the source's `states from X` type defect are made explicit.

Lines 1006--1152 preserve the mutually generated CTL* state/path syntax, the
finite-path next boundary, current-inclusive eventuality and strong until,
infinitely-often semantics, exact derived operators, all named language
fragments, formula-length convention, associated-language constructor, and
both equivalence relations.  `B(L)` is expressly metalinguistic and not falsely
closed under semantic negation or disjunction.  The fusion/state-completeness
hypotheses and their counterexamples are not dropped.

Lines 1154--1319 reproduce the expressiveness order at its source-supported
scope over `R`-generable structures and do not treat absent diagram edges as
mere layout.  Theorem 3's path-deletion proof, Theorem 4's normalization
boundary, and the cited rather than locally proved Theorems 8--9 are separated.
The self-defeating literal targets of Theorems 5--6 are printed before the
proof-and-diagram-supported targets without the extra `L( )`; the wrong
Theorem 9 dependency and later wrong Theorem 7 cross-reference are both
identified.  The witness formulas, bounded-formula invariants, omitted Boolean
or repeated induction cases, and Theorem 7's use of cited Boolean-path
elimination retain their proper proof status.

Lines 1321--1427 type `enabled` and `executed` as atomic state predicates and
keep strong-eventual fairness inside the specification formula rather than in
the path set.  The PL translation states the role of the atomic program,
initial-prefix test, and proper-suffix operation and preserves Proposition 5's
unprinted-induction boundary.  The MPL `stage` name meets the supplied naming
rule: its necessity, exact finite-prefix definition, standing, distinction
from states and connectives, and later use are stated together.  The literal
non-strict `U` and `X` defects are demonstrated by counterexamples; the
strict-before/proper-successor repair is described only as what would support
the announced translation and is not attributed to the printed clauses.
Closure hypotheses, the well-ordering qualification, omitted proof steps, and
the merely expected TC translation are all retained.  Lines 1429--1455 keep
the terminal-server example at application-argument strength and deny a CTL
labelling algorithm, general complexity result, or synthesis theorem in this
article.

## Clarke--Grumberg--Peled acquisition fidelity

Lines 1460--1470 match the acquisition note's exact negative and positive
claims: no anonymously readable complete first-edition body or public accepted
manuscript was obtained on the audited routes as of 22 August 2026; this is not
global unavailability; controlled lending and institution-only access exist;
Google Books is partial/searchable; the HathiTrust statement is limited to
standard-identifier queries; and MIT Press supplies a product record without a
body.  The four printed section-start locators come only from contents
metadata.  The text explicitly says those locators support no body-level
claim.  Lines 1472--1478 keep all lookalike or later works separate and retain
independent citations for the host's four complexity classifications.  This
section therefore does not create a hypothetical 1999 presentation under a
new name; it states the still-owed acquisition artifact and its exact limit.

## Baier--Katoen fidelity and host bridge

Lines 1491--1565 preserve the source's action-labelled transition-system tuple,
its definition of finiteness, possible empty initial set, successor and
terminal-state notions, and standing no-terminal-state hypothesis.  The
handbook-supplied `R_0` and `V_0` bridge satisfies the technical-name rule:
action forgetting is necessary to instantiate the host's binary relation;
both symbols have eliminable definitions and metalinguistic standings; their
difference from a new Baier--Katoen transition system is explicit; and they are
used immediately in `K_0`, the predecessor identity, the totality argument,
the satisfaction-preservation induction, and the `|R_0| <= K` parameter
distinction.  The empty-state edge case is not used to instantiate the host's
nonempty structure.  Maximal fragments, paths from arbitrary evaluation
states, and initial paths remain distinct.

Lines 1567--1630 reproduce the typed CTL grammar and semantics, derived
operators, non-strict until witness, satisfaction-set/system clauses, and ENF
grammar.  The potentially exponential universal-elimination rewrite is not
used as an intermediate in the later linear formula-size bound.  Lines
1632--1750 preserve Theorem 6.23's least/greatest set characterizations,
Algorithm 14's seven branches, the naive one-state loops, both simultaneous
approximation chains, Algorithms 15--16's worklist/count mechanisms, and the
count invariant.  The global structural induction assembled from Algorithm 13
and Theorem 6.23 is expressly labelled as a handbook-explicit argument rather
than a separately printed theorem proof.  The global no-terminal convention
is retained; the text correctly notes that the displayed post-fixed-set
condition itself supplies an in-set successor in the converse greatestness
argument.

Lines 1751--1800 reproduce the eight-state graph, labels, edges, and initial
state.  The Boolean equality/inequality signs are introduced as exact,
eliminable metalinguistic propositional abbreviations, distinguished from a new
state-variable sort or new atoms, and used immediately.  The eventuality and
existential-always satisfaction sets agree with the authority note.  Lines
1802--1816 retain the exact finite/no-terminal, adjacency-representation, and
direct-modality hypotheses of the `O((N+K)|Phi|)` time theorem and do not
invent a separate printed space theorem.

Lines 1818--1876 make Example 6.31 fully typed: the added `b` state totalizes
the graph; all graph vertices are initial and uniquely proposition-labelled;
`Psi` and `Phi_n` are exact eliminable formula abbreviations; and the
Hamiltonian equivalence uses system satisfaction correctly.  The exponential
formula size is kept separate from the model-checking theorem.  The source's
informal `P=NP` inference is not promoted: the manuscript correctly identifies
the missing uniform construction premise and labels the result a succinctness
warning.

Lines 1878--1913 give the actual `TS_n,TS'_n` families with separate base and
positive-index clauses, the correct new edges, and the exact proof omissions.
The `forall always exists eventually` trace separation retains its correct
modality.  Lines 1915--1950 preserve CTL* state/path typing, derived universal
quantification, semantic clauses, the LTL embedding, and the well-typed
strictness formula.  The atom-substitution explanation is presented as the
omitted elementary step, not as printed source prose.  Lines 1952--1967 record
all relevant printed defects and incomplete proof surfaces and limit the
source support for the host method/theorem accordingly.

## Technical-name rule

No current passage names a hypothetical answer where the text instead owes an
artifact.  Source terms such as synchronization skeleton, global system
flowgraph, interpreted Petri net, `Blocks`, `Tiles`, strong equivalence,
`R`-generability, stage, existential normal form, and satisfaction set are
defined at their source-supported standings and then used.  Handbook additions
such as `D_s`, `R_0`, `V_0`, `K_0`, the pointwise transformer operations, and
the propositional comparison abbreviations are eliminable, are identified as
reader-facing or metalinguistic where needed, state the distinction that
requires them, and have immediate downstream use.  Auxiliary symbols such as
`TURN`, `Theta`, `Psi`, and `Phi_n` name explicit source variables or exact
formula abbreviations rather than speculative new entities.  The inaccessible
1999 first-edition body is correctly left as an acquisition boundary rather
than assigned invented mathematical content.

## Substantive text read

The following text was read directly and completely over the recorded ranges:

- `handbook/parts/p09/presentations/n-c-016.tex`, lines 1--1967 (complete file
  through EOF).
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 925--1055 and
  1475--1535 (the host transition into the model-checking section; all CTL,
  labelling, boundary, and complexity declarations used by N-c-016; and the
  N-c-016 input/hierarchy span).
- `handbook/parts/p08/temporal-epistemic-supplement.tex`, lines 35--185 (the
  inherited total-transition, CTL, and CTL* definitions and cards).
- `spec/research/p09-clarke-emerson-1981-source-note.md`, lines 1--884
  (complete file through EOF).
- `spec/research/p09-queille-sifakis-1982-source-note.md`, lines 1--867
  (complete file through EOF).
- `spec/research/p09-emerson-halpern-1986-source-note.md`, lines 1--729
  (complete file through EOF).
- `spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md`, lines
  1--470 (complete file through EOF).
- `spec/research/p09-baier-katoen-2008-ch6-source-note.md`, lines 1--1120
  (complete file through EOF).
- `handbook/bib/handbook.bib`, lines 2393--2458, limited to the exact entries
  `ClarkeEmerson1981`, `QueilleSifakis1982`, `EmersonHalpern1986`,
  `ClarkeGrumbergPeled1999`, and `BaierKatoen2008`.

## Prohibitions observed and resulting non-claims

I did not open or inspect a PDF, render, screenshot, page image, or historical
publication file.  I did not run a TeX build, test, checker, validator, source
analysis script, hash operation, or executable manuscript tool.  I did not
browse the web.  I did not read any prior N-c-016 review report, including any
earlier report of my own; any mathematical/publication report; any admission,
board, register-history, or campaign-history file; any parent conclusion; or
any other agent output.  I did not contact, delegate to, or otherwise consult
another agent.  I modified no manuscript, host, prerequisite, authority note,
bibliography, or other project file.

Accordingly, this ACCEPT verdict is a source-text fidelity finding only.  It
does not certify compilation, cross-reference resolution in a build, visual
pagination, glyph rendering, accessibility, copyright clearance, permission to
distribute any underlying source object, completeness of any external search,
independent reproduction of an algorithm, independent proof verification,
human editorial approval, or final admission of N-c-016.

REGISTER STATUS: OPEN
