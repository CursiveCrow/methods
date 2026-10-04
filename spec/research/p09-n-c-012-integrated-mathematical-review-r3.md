# N-c-012 Round 3 blind mathematical and proof-coherence review

## Review basis and scope

I read the complete actual manuscript source
`handbook/parts/p09/presentations/n-c-012.tex` directly from line 1 through its
EOF at line 3010.  I also read the actual current parent source
`handbook/parts/p09/logic-in-computer-science.tex` at the portions governing the
reused LTL and past semantics, the strict/inclusive translations, the public
theorem statements, the semantic safety/liveness definition, the
infinite-word-automata and model-checking interface, and the input seam
(principally lines 604--811 and 899--906).

This was a blind review of the live `.tex` sources.  I did not read an
integrated N-c-012 review report, and I used no manuscript PDF, page image,
render, screenshot, test, checker, repository script, TeX command, build, or
hash.  The line references below are actual-LaTeX line references.

## Result

The five historical presentations are, in most respects, unusually careful
about semantic convention, theorem strength, and proof ownership.  The Kamp,
GPSS, and Alpern--Schneider reconstructions are mathematically coherent; the
Pnueli presentation correctly preserves rather than hides the source's
strict/inclusive tensions and several proof gaps; and the Sistla--Clarke
presentation correctly keeps the operator bases and path quantifiers apart.
The parent interfaces and final integration paragraph also agree with those
reconstructions.

Two blocking defects remain.  One changes the declared theorem-system standing
of `K_b` at its principal later use.  The other leaves the ETL grammar domain
wide enough to contain empty-word productions while giving a consistency rule
which cannot interpret them.

## Blocking findings

### R3-MATH-01 — `K_b` is declared to be the pure calculus but is later used as the system-relative calculus

At lines 847--898, the manuscript presents the pure future calculus.  It then
makes a particularly strong local declaration at lines 890--894:

- `K_b` denotes *exactly* the pure propositional future calculus;
- its axioms are G1--G3;
- its rules are RT, RG, and MP; and
- it is a theorem system, distinct from the later GPSS systems.

The domain-dependent principles are then explicitly kept separate from that
pure basis at lines 930--990.  In particular, E and N derive system-relative
eventualities from facts about `R` and the selected action relation.  This
separation is mathematically real: the pure calculus has no transition relation
in its formula language and no rule whose premise is a transition-system
validity.

Nevertheless, lines 1020--1025 say that Theorem 3 makes `K_b` at least as strong
as ER and that every ER axiom is a theorem of `K_b`.  Under the preceding exact
local definition this cannot be the asserted simulation.  ER's A1, displayed at
lines 560--565, obtains `p \leadsto q` from a condition on one-step
`R`-transitions.  Its tense representation `p \Rightarrow Fq` is not a theorem
of the pure calculus: on the inclusive semantics at lines 827--838, take an
infinite word on which `p` holds only now and `q` never holds.  Then
`p \Rightarrow Fq` is false now.  The transition premise can make the formula
valid *for a selected system*, and principle E can internalize that premise,
but neither fact turns it into an absolute theorem of the declared pure
calculus.

This is independent of the already recorded strict/inclusive conflict at lines
668--676.  Even if the eventuality convention is first repaired, the theorem
system still needs a system-relative proof interface.  It is also a direct
failure of the workspace technical-name rule: `K_b` has one explicit standing
at lines 890--894 and is used with a different standing at lines 1020--1025.

Required repair: keep the pure theorem system used in Theorem 2 distinct from
the system-relative proof system used in Theorem 3.  At the latter location,
define exactly which of I1, I2, E, N, quantified principles, and background
state reasoning are available; state whether derivability is relative to a
fixed transition system and its established premises; and then restate the ER
simulation at that exact standing.  If the source itself overloads its system
name, report that overload rather than resolving it by the handbook's earlier
exclusive definition.  Until this artifact is supplied, the theorem-system
claim is not well typed.

### R3-MATH-02 — ETL admits a zero-terminal production but its local consistency rule has no zero-terminal case

Lines 2429--2436 define a right-linear production as `N -> aM` or `N -> a`,
where `a` is a *finite word* of terminals, and then normalize to productions
emitting *at most* one terminal.  No nonemptiness condition is imposed.  Lines
2437--2446 make ETL the least formula class closed under the resulting
grammar-indexed constructors.  Lines 2454--2469 explicitly treat a finite
generated word of length `r`, with the formula obligations ranging over
`0 <= ell < r`; no condition states `r > 0`.

Consequently the stated grammar domain includes, or at minimum fails to exclude,
an empty emitted word.  Take a grammar with terminal alphabet `{a_1}` and the
production `N -> epsilon`.  Under the displayed finite-word semantics,
`N(P)` is true at every position: the generated word has length zero and its
universal family of argument obligations is empty.

The positive consistency biconditional at lines 2550--2560 cannot represent
that case.  Its right side recognizes only productions of the forms
`N_j -> a_k N_ell` and `N_j -> a_k`.  For the grammar above both disjuncts are
false, so the rule declares `N(P)` absent from the current truth set.  This
contradicts the constructor semantics.  The claim at lines 2579--2583 that the
displayed checks rule out all finite and infinite witnesses therefore does not
hold for the formula class as it was defined.

Required repair: make the grammar domain exact.  Either require every emitted
word to be nonempty and explain why the normalization used in the proof
preserves precisely that restricted constructor semantics, or retain empty-word
productions and add the necessary epsilon-closure and empty-witness cases to
the local consistency and continuation rules.  If this is an omission in the
source proof, it must be marked as a source gap or a handbook repair just as the
other source defects are; it cannot be resolved by silently reading “finite
word” as “nonempty finite word.”

## Reconstruction of the five presentations

### 1. Kamp

Lines 16--40 correctly separate `Lin`, `Den`, `Dis`, and order-theoretic `Com`.
The completeness condition permits discrete orders and endpoints; in
particular, the examples involving finite orders, the integers, the reals, and
the rationals are correctly classified.  Lines 42--72 give the one-current-
variable first-order standing and uniform operation semantics.  Lines 74--98
preserve Kamp's strict witnesses, open intervals, and witness-first operand
order for both S and U.

The temporal-to-first-order clauses at lines 100--131 are capture avoiding and
preserve all three of those features.  The converse at lines 133--155 is not
silently promoted from complete orders to arbitrary chains, and the rational
counterexample at lines 157--165 is kept distinct from the integer separation.
The literal Chapter IV Theorem 3 is correctly identified at lines 167--231.

The handbook-owned repair of the sparse-square induction is mathematically
coherent.  The atomic counterexample to the unrestricted printed second clause
is valid (lines 272--278); adding same parity gives the right bounded-window
invariant (lines 280--295); the enlargement argument supports conjunction
(lines 297--308); immediate-neighbour operators preserve the two repaired
uniformities (lines 310--317); and strict unbounded past/future become
eventually constant (lines 319--326).  The alternating central gaps then
separate both isolation operations (lines 334--341).  The repair is repeatedly
and correctly identified as handbook-owned rather than attributed to Kamp.

### 2. Pnueli

The transition-system and atomic-interleaving setting at lines 372--431 is
properly typed and does not impose finiteness on the state space.  Reachability,
invariance, and the source's strict `leadsto` relation are distinguished at
lines 433--478.  P1 at lines 481--489 is ordinary reachable-state induction.

The manuscript correctly exposes both defects in literal P2: the missing
zero-rank boundary (lines 490--531) and the independent mismatch between a
current-state discharge and strict futurity (lines 533--541).  The typed ER
relation and parameterized R4 are explicit at lines 543--616.  Its reported
completeness proof is not overstated: pointwise finite branching is distinguished
from a uniform branching bound, and the arbitrary-start and seriality gaps are
exhibited at lines 618--666.  The strict `leadsto` versus inclusive F/G tension
is then summarized accurately at lines 668--676.

The sequential and concurrent attachments and the producer--consumer invariant
calculation are coherent (lines 678--817).  The inclusive F/G semantics,
quantifier schemata, and source-sensitive status of the pure calculus are
otherwise carefully reconstructed (lines 819--928).  The domain-dependent
principles and fairness premise are correctly separated at lines 930--1018;
the defect is only their later unmarked reassimilation into `K_b` in
R3-MATH-01.

The finite-state specialization correctly distinguishes arbitrary-start
continuations from proper initial-state executions (lines 1030--1062).  The SCC
criterion at lines 1075--1094 includes the necessary cyclicity and every-action
condition.  P and MRG are nonredundant and correctly scoped (lines 1096--1117).
Appendix A separates imported T2/T3 from the locally printed lemma
(lines 1119--1148), while Appendix B correctly reports an automata/language
decision route without importing a later LTL-to-Buechi construction
(lines 1150--1197).

### 3. GPSS

Lines 1212--1247 retain the source's strict-future convention and explicitly
record the printed reversed inequality for F as a source conflict.  The local
strict-until notation at lines 1249--1290 has exact standing and operand order;
the strict past operator is clearly marked as a handbook-supplied order dual.
The discrete bridge at lines 1292--1313 is correct in both directions and
correctly keeps X and Y available.

The program formulas, the three response strengths, and their fairness examples
remain under the strict convention (lines 1315--1408).  The precedence
abbreviation is eliminable, defined, and used for the promised ordering
distinction (lines 1410--1455).  The four first-order result domains are not
collapsed (lines 1473--1539), and the proof-outline boundary—including the
unformalized event expressions, numbering conflict, and external referrals—is
accurately preserved (lines 1541--1645).

DX and DUX are presented as theorem systems at lines 1647--1687, and their
canonical construction is consistently reported as an outline rather than a
completed proof (lines 1690--1772).  The final `U^0` semantic/recursion conflict
is genuine and is correctly left unresolved rather than silently repaired
(lines 1774--1827).  The parent theorem uses the discrete bridge without
turning these source outlines into full proofs.

### 4. Sistla--Clarke

The journal version controls, and the conference/journal repair boundary is
kept explicit (lines 1838--1861).  The source languages and inclusive X, U, S,
F, and G semantics are correct at lines 1863--1930.  Satisfiability,
existential-path truth in an R-structure, and universal validity are not
conflated (lines 1932--1970).

The L(F) small-structure argument keeps the finite prefix, recurring valuation
types, acceptable-subsequence condition, and ambient-structure parameter
separate (lines 1972--2089).  The source's strict/non-strict size defect is
correctly exposed, and the proof-supported non-strict bound is used
(lines 2091--2112).  The NP certificate correctly adds the directed-cycle
condition missing from a merely reflexive singleton SCC (lines 2114--2205).

The three PSPACE bases in Theorem 4.1, the R-structure reduction, stuttering
step, computation-history hardness proof, truth-set count, deletion lemma,
periodic truth conditions, past boundary, and polynomial-space checker remain
operator sensitive (lines 2207--2426).  The ETL least-class standing is
otherwise clear, but its constructor/proof interface has the zero-terminal gap
in R3-MATH-02.  Apart from that gap, the grammar-tree obligations and the
journal's corrected periodic argument are cleanly separated from the ordinary
until obligations (lines 2485--2588).  The final table preserves all three
decision problems and the exact fragment bases (lines 2590--2620).

### 5. Alpern--Schneider

Lines 2624--2653 correctly place the theory in the full semantic universe
`P subseteq S^omega`, rather than paths of a fixed transition system or formula
syntax.  The nonempty state-set hypothesis is explicitly justified
(lines 2659--2664).  Safety and liveness have the correct bad-prefix and
continuation quantifiers (lines 2666--2719).

Uniform and absolute liveness are exactly distinguished at lines 2721--2761.
The repaired leads-to separation has the hypotheses required by its witnesses
(lines 2763--2795), and the predictive example correctly exhibits ordinary but
not uniform liveness (lines 2797--2818).  The prefix-topological equivalences
are correct (lines 2830--2849).

The closure factor `L_P` gives a valid safety/liveness decomposition
(lines 2851--2893), and the private-communication claim is not upgraded to a
proof (lines 2895--2899).  Theorem 2 and the singleton-state exception are
correct (lines 2901--2926).  The printed Corollary 2.1 really does require union
rather than mere intersection closure, and the denotation-family counterexample
at lines 2941--2961 establishes insufficiency of the printed hypothesis.  The
Boolean-closure table and final source boundary are coherent.

## Parent interfaces and integration

The parent definition at `logic-in-computer-science.tex` lines 604--625 reuses
the established inclusive future language and adds inclusive Y and S with the
right boundary clauses.  Lines 627--684 give mutually truth-preserving strict
and inclusive translations over discrete words; operand order is consistent
with N-c-012, and X/Y are not falsely eliminated.  The first-order and PSPACE
theorems at lines 686--710 have the exact language and order domains reconstructed
in the presentation.

The safety/liveness definition at lines 712--720 is semantic rather than
typographical and agrees with the full-word treatment in the fifth presentation.
The automata and model-checking interfaces at lines 722--811 correctly distinguish
Buechi, parity, and Rabin acceptance; consume the initial state label at the
product's initial vertices; require an accepting cyclic SCC; separate explicit
product size from formula translation; and pass from existential counterexample
search to universal model checking by complement.

The input seam at lines 903--906 places N-c-012 after those public temporal and
automata interfaces and before the later model-checking section.  The final
integration paragraph in N-c-012 at lines 2997--3010 correctly keeps the five
domains separate: complete-order first-order expressiveness, transition-system
proof rules, strict GPSS temporal syntax, inclusive fragment-sensitive
complexity, and full-space semantic properties.  Neither blocking finding
requires changing that paragraph once the two local interfaces are repaired.

## Five-part technical-name audit

Most locally introduced notation satisfies the workspace rule: it is motivated
by a real ambiguity, defined eliminably or explicitly typed, assigned a standing,
distinguished from adjacent terms, and used later.  Particularly good examples
include the tense-defining formulas, the strict GPSS warning subscripts, the
proper-execution validity relation, source truth sets versus guessed truth sets,
and the Alpern--Schneider property abbreviations.  Undefined source symbols such
as GPSS's gap operators and event expressions are correctly left as owed or
source-reported artifacts rather than promoted to handbook definitions.

`K_b` fails the standing-and-use clauses for the reason in R3-MATH-01.  ETL has
the right formula-class standing, but its grammar-indexed constructor fails the
exact-definition and later-use clauses until R3-MATH-02 is resolved.  I found no
other technical name whose use changes the mathematical result.

VERDICT: REJECT -- R3-MATH-01, R3-MATH-02
