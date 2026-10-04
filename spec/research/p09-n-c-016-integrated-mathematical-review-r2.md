VERDICT: REJECT

# N-c-016 Round 2 mathematical and definedness review

## Scope and decision rule

This is a fresh, independent, text-only review of the frozen 1,849-line
presentation and its authorized host, prerequisite, and supporting evidence.
The review is mathematical/definedness only.  It tests definition before use,
types, quantifiers, truth and nullary cases, path conventions, fixed-point
typing and iteration, image-finiteness, CTL/CTL* typing, logical direction,
source-versus-reader proof boundaries, representation-sensitive complexity,
the Clarke--Grumberg--Peled acquisition limit, host consistency, and the
supplied `AGENTS.md` technical-name rule.

The verdict is `REJECT` because the following line-specific must-fix items
remain.  Each repair below is deliberately minimal; no wider redesign is
needed.

## Must-fix findings

### M1. The host predecessor and fixed-point variables have no declared set type

**Location:** `handbook/parts/p09/logic-in-computer-science.tex`, lines
954--961 and 980--994.

The host defines `Pre_exists(X)` and `Pre_forall(X)` without first saying that
`X` ranges over subsets of `S`, and then binds `X` with `mu` and `nu` without
stating the complete lattice or the type of the bound variable.  The prose at
lines 991--994 gives an iteration strategy, but it does not repair the missing
definition of the displayed fixed-point notation.  This matters to the
Baier--Katoen bridge, which says that the source set characterizations are
represented by exactly this notation.

**Minimal repair:** at line 954 declare

\[
 \operatorname{Pre}_{\exists},\operatorname{Pre}_{\forall}:
 \mathcal P(S)\longrightarrow\mathcal P(S),
 \qquad X\in\mathcal P(S),
\]

and, before the equations containing `mu X` and `nu X`, state that these denote
the least and greatest fixed points in
`(mathcal P(S), subseteq)` and that their bound `X` is a state set.  The
existing monotonicity and finite-iteration prose can then remain unchanged.

### M2. The host mis-types LTL as a state-formula language

**Location:** `handbook/parts/p09/logic-in-computer-science.tex`, lines
1008--1014; compare
`handbook/parts/p08/temporal-epistemic-supplement.tex`, lines 129--163, and
`spec/research/p08-new-content.md`, lines 813--822.

The phrase “an LTL state formula read universally over paths” conflicts with
the inherited state/path distinction.  LTL supplies a path formula; its
state-level comparison is obtained only after universal path closure.  In
particular, the object compared with CTL is the state interpretation
`A(F G p)`, not the untyped path string `F G p` standing alone.

**Minimal repair:** rewrite the theorem opening to quantify an LTL path formula
`varphi` and explicitly define its state lift as `A varphi` (universal truth on
all paths from the current state).  State the two separations as: no
universally lifted LTL formula defines `AG EF p`, and no CTL formula defines
the universal state lift of `F G p`.  The CTL* containment sentence can then
refer to “state-lifted LTL,” matching the prerequisite and comparison table.

### M3. The Clarke--Emerson tableau calls elementary formulas “both types” without components

**Location:** `handbook/parts/p09/presentations/n-c-016.tex`, lines 251--269.

Lines 251--252 define an alpha formula by two required components and a beta
formula by two alternative components.  Lines 261--263 then say that an
elementary formula is treated as “both types” but is not expanded.  No alpha
or beta components are supplied for an elementary formula, yet the
downward-closure definition immediately quantifies over the components of
every alpha and beta formula.  On the permitted supporting text, the source
distinguishes elementary from nonelementary formulas and expands only the
latter; it does not supply the missing component assignment needed by the
reader-facing “both types” sentence.

**Minimal repair:** delete “the source treats it as both types” and retain the
exact usable distinction: elementary formulas are not expanded, while the
stated alpha/beta component rules govern the nonelementary expansions.  If
“both types” is intended in some other precise source sense, supply that sense
and its components at this location instead.

### M4. The ninth Clarke--Emerson requirement is valid under the already assumed totality condition

**Location:** `handbook/parts/p09/presentations/n-c-016.tex`, lines 46--49,
110--113, and 368--371.

The source structure assumes that
`A=A_1 union ... union A_k` is total.  Since
`EX true := bigvee_i EX_i true`, every state therefore satisfies `EX true`.
Consequently `AG(EX true)` is valid on every stated source structure and adds
no constraint to the conjunction.  Presenting it only as the substantive
requirement “Some process can always move” conceals that logical redundancy.

**Minimal repair:** immediately after line 370 add that, under the standing
totality hypothesis, group 9 is semantically redundant (and is retained only
because it is one of the source's printed requirement groups).  Do not delete
the source formula.

### M5. The Clarke--Emerson factorization leaves the one-process conjunction undefined

**Location:** `handbook/parts/p09/presentations/n-c-016.tex`, lines 427--446.

The general rule labels a local arc by conjunctions
`S_1 land ... land S_p` of all other-process components, but `p` is not tied
to `k-1` and the nullary case is not defined.  For `k=1`, there are no other
process components.  The displayed rule then uses an empty conjunction
without saying that it is `true`.

**Minimal repair:** say that `p=k-1` after the process-`i` component is removed
and adopt the convention that the empty conjunction is `true`.  Alternatively,
state a sourced standing hypothesis `k>=2`; the empty-conjunction convention
is the smaller and more general repair.  The outer disjunction needs no empty
case because the local arc is drawn only when at least one matching global arc
exists.

### M6. CESAR's finite action-family abbreviations omit all nullary truth values

**Location:** `handbook/parts/p09/presentations/n-c-016.tex`, lines 597--609
and 635--645.

The text quantifies over a finite action family, not a nonempty one.  It then
uses disjunction for `enable(a_1,...,a_k)` and `after(a_1,...,a_k)`, uses
`enable A(P)` for an arbitrary process action set, and later uses a conjunction
for liveness of every family member.  If `k=0` or `A(P)=emptyset`, these
expressions have no declared value.

**Minimal repair:** add the standard conventions

\[
 \bigvee\varnothing=\mathsf{false},\qquad
 \bigwedge\varnothing=\mathsf{true}.
\]

Then `enable(emptyset)` and `after(emptyset)` are false, absence of deadlock
for an empty family is false, and “every member is live” for an empty family
is true.  If the source intends only nonempty families and processes with at
least one action, state those quantifiers instead.

### M7. CESAR's transformer power is under-typed and incorrectly called descending

**Location:** `handbook/parts/p09/presentations/n-c-016.tex`, lines 692--715.

The text defines powers for “a transformer `h`” but never gives the exact type
`h : mathcal P(Q) -> mathcal P(Q)`.  More importantly, line 714 calls `h^x`
“descending finite iteration.”  What the source defines is the pointwise
intersection of all finite powers.  For an arbitrary transformer, even an
order-preserving one, the powers need not form a descending chain: the
constant transformer `h(P)=Q` gives `P,Q,Q,...` whenever `P` is a proper
subset of `Q`.

**Minimal repair:** type the construction and evaluate it pointwise:

\[
 h:\mathcal P(Q)\to\mathcal P(Q),\qquad
 h^*(P)=\bigcup_{i\in\mathbb N}h^i(P),\qquad
 h^x(P)=\bigcap_{i\in\mathbb N}h^i(P).
\]

Replace “descending finite iteration” by “the pointwise intersection of all
finite iterates.”  The following four source identities, their
image-finiteness hypothesis, and the delegated-proof warning are otherwise
typed and stated in the correct direction.

### M8. Emerson--Halpern's closure conditions use untyped, undefined concatenation notation

**Location:** `handbook/parts/p09/presentations/n-c-016.tex`, lines 871--893.

The displayed definitions use `x_1 s y_1`, `x_2 s y_2`,
`x_1 x_2 y_2`, and `x_1 x_2 x_3 ...` without defining concatenation, saying
which symbols are finite blocks or tails, specifying whether empty blocks are
allowed, or making the universal quantifiers explicit.  Earlier lines define
only first state, successor suffix, and finite iteration of suffix.  Thus the
three named closure properties are not eliminable definitions at their point
of introduction.

**Minimal repair:** immediately before the array define the state-string
concatenation notation and the types of the prefix blocks, shared state, and
tails, including the permitted empty cases; then universally quantify the
displayed compatible decompositions.  In the limit-closure clause, explicitly
say that every finite approximation shown belongs to `X` and that the infinite
concatenation is the asserted limit path.  No new closure name is needed.

### M9. The new proof-family symbols `B` and `B+` fail the exact-definition prong of `AGENTS.md`

**Location:** `handbook/parts/p09/presentations/n-c-016.tex`, lines 1086--1106.

This paragraph carefully supplies standing, nonredundancy, and later use for
the Appendix's `B` and `B+`, and distinguishes them from `B(L)`.  It does not,
however, give an exact definition of `B`: one constituent is only “a specified
family of nested `F`-forms.”  Consequently neither `B` nor its
conjunction/disjunction closure `B+` is eliminable from the reader-facing text.
That is precisely the supplied technical-name rule's missing Definition
condition.

**Minimal repair:** either reproduce the complete source grammar for `B` and
then define `B+` exactly, or remove the two symbols from the reader-facing
proof synopsis and say directly that the Appendix normalizes into the listed
segment, recurring-eventuality, and nested-eventuality forms before translating
their Boolean combinations.  The latter is the smaller repair and preserves
the stated proof boundary.

### M10. The Baier--Katoen bridge does not discharge the host's nonempty-state hypothesis

**Location:** `handbook/parts/p09/presentations/n-c-016.tex`, lines 1357--1408;
compare `handbook/parts/p08/temporal-epistemic-supplement.tex`, lines 46--55,
and `handbook/parts/p09/logic-in-computer-science.tex`, lines 948--967.

The inherited host definition requires `S != emptyset`.  The Baier--Katoen
tuple presented here states finiteness and permits an empty initial set, while
the displayed no-terminal condition is universal and hence does not by itself
exclude `S=emptyset`.  Thus it makes `R_0` serial on whatever states exist, but
the text has not yet shown that `K_0=(S,R_0,V_0)` is a host total transition
structure.  The satisfaction equivalence at lines 1403--1408 is still a valid
structural induction on any source state; the claimed instantiation of the
host method needs the missing nonemptiness case.

**Minimal repair:** either add a sourced `S != emptyset` hypothesis before
calling `K_0` a host total transition structure, or state the bridge for
`S != emptyset` and handle `S=emptyset` separately (all satisfaction sets are
empty and system satisfaction is vacuous because `I=emptyset`).  Do not infer
nonemptiness merely from the no-terminal formula.

### M11. The Hamiltonian-path construction has no `n>=1` base-domain hypothesis

**Location:** `handbook/parts/p09/presentations/n-c-016.tex`, lines 1681--1712.

The construction writes `V={v_1,...,v_n}` and defines the recursion by the
base expression `Psi(v_{i_1})`.  For `n=0`, that base expression is undefined,
while the set of permutations has a nullary member under the usual convention.
The later equivalence therefore has no determined empty-graph case.

**Minimal repair:** state `n>=1` when introducing `V`.  Nothing in the
succinctness argument needs the empty graph, so no separate nullary formula is
required.

## Results of the remaining requested checks

The following checks produced no additional must-fix beyond M1--M11.

| Surface | Verified mathematical/source boundary | Outstanding items |
|---|---|---|
| Clarke--Emerson | The indexed `EX_i` grammar, total-union path semantics, inclusive strong until, guarded universal/existential predecessor growth, finite SCC qualification for infinitely-often, NP-hardness-only direction for the LTL-prefix extension, and abridged tableau/synthesis proof status are preserved.  The global-flowgraph, model-fragment, and `TURN` distinctions have stated standing and actual later use. | M3--M5. |
| Queille--Sifakis | Maximal finite/infinite executions, the inaccessible-`omega` convention, current-inclusive unary modalities, the source's missing execution/Boolean clauses, the external non-loss assumption, all four transformer identities, image-finiteness, delegated proofs, and possible analyzer non-answer are separated correctly. | M6--M7. |
| Emerson--Halpern | The Lamport state/path readings, finite-path suffix convention, typed CTL* grammar, direct path semantics, pointwise-versus-model equivalence distinction, expressiveness direction, proof-supported repairs to Theorems 5--6, literal MPL `U/X` defects, and reader/source proof boundaries are stated consistently. | M8--M9. |
| Clarke--Grumberg--Peled | No grammar, algorithm, proof, example, or complexity theorem is attributed to the unavailable first-edition body.  Contents-page locators are kept as acquisition targets; the 1996 survey, 2001 chapter, 2008 textbook, and 2018 second edition are not substituted. | None.  Source-content reconstruction correctly remains open. |
| Baier--Katoen | Action-erasure preserves the state sequences used by CTL; `|R_0|<=K` correctly distinguishes binary edges from action-labelled triples.  CTL and CTL* formulas are typed, until is current-inclusive, the least/greatest set directions and worklists agree, `I=emptyset` is explicitly vacuous, ENF expansion is not charged to the linear bound, the time bound retains its representation hypotheses, and the Hamiltonian succinctness argument correctly records its missing uniformity premise. | M10--M11. |
| Host | Once M1 is supplied, the `EU`, `AU`, `EG`, and `AG` operators are the correct least/greatest fixed points on a finite total frame, and the adjacency-list/worklist time bound has the correct representation-sensitive form.  The four CTL/CTL* decision problems remain distinct. | M1--M2. |

## `AGENTS.md` technical-name audit

The source-derived names “synchronization skeleton,” “global system
flowgraph,” “model fragment,” “interpreted Petri net,” `Blocks`, `Tiles`,
“strongly equivalent,” the path-set closure properties, “stage,” existential
normal form, and the Boolean comparison abbreviations are each accompanied by
enough standing, distinction, and subsequent use for this review.  M8 records
the missing eliminable definitions inside the named closure conditions, and
M9 records the one new pair of proof-family symbols whose exact definition is
not supplied.  M1 and M7 are corresponding type/standing failures for bound
set variables and transformers rather than requests for new terminology.

## Complete text-evidence ledger

The following files and only these substantive text ranges were read:

1. `handbook/parts/p09/presentations/n-c-016.tex`, lines 1--1849, complete.
2. `handbook/parts/p09/logic-in-computer-science.tex`, lines 945--1023 and
   1505--1507.
3. `handbook/parts/p08/temporal-epistemic-supplement.tex`, lines 42--190.
4. `spec/research/p09-clarke-emerson-1981-source-note.md`, lines 1--884,
   complete.
5. `spec/research/p09-queille-sifakis-1982-source-note.md`, lines 1--867,
   complete.
6. `spec/research/p09-emerson-halpern-1986-source-note.md`, lines 1--729,
   complete.
7. `spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md`, lines
   1--470, complete.
8. `spec/research/p09-baier-katoen-2008-ch6-source-note.md`, lines 1--1120,
   complete.
9. `spec/research/p09-source-presentations-lot2-3.md`, lines 781--847.
10. `handbook/bib/handbook.bib`, lines 2393--2407, 2409--2422, 2424--2436,
    2438--2447, 2449--2458, 4815--4824, 4826--4835, 4837--4846, and
    4897--4906.
11. `spec/research/p08-new-content.md`, lines 810--830.

The supplied `AGENTS.md` instruction was used as task text; no additional
`AGENTS.md` file content was opened.  A filename-only repository search was
used to resolve the supplied relative path under `work/formal-logic-handbook`;
it exposed no additional substantive file content.

## Prohibitions observed

- No N-c-016 Round 1 report was read.
- No existing source Round 2 report was read.
- No other N-c-016 review, board, admission, handoff, or history file was read.
- No agent was inspected, contacted, or delegated to; no subagent was used.
- No manuscript PDF, source PDF, render, screenshot, page image, or manuscript
  visual evidence was opened or inspected.
- No TeX or handbook build was run.
- No tests, test infrastructure, checkers, repository scripts, validators, or
  executable source tools were run.
- No hash was computed.  Hash strings appearing in the authorized notes and
  bibliography were read only as permitted text evidence.
- No historical publication file was consulted; the permitted text evidence
  was sufficient to identify every reported issue without that exception.
- No web source or unlisted supporting source was consulted.
- No project file other than this assigned report was edited.
- No memory or prior-run review material was consulted, preserving the blind
  independence requirement.

REGISTER STATUS: OPEN
