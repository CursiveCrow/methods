# Round 3 mathematical and proof-correctness review: Rabin 1969

## Scope, independence, and evidence boundary

I reviewed the complete frozen Round 3 snapshot under the mathematical and
proof-correctness mandate in the board charter.  I did not use any Round 1 or
Round 2 report, any other Round 3 report, the ledger, the chair transcript, any
other board or transcript, the staging draft, the layout extraction as
controlling evidence, or conversation/history as evidence.  I did not contact
another reviewer.  I wrote no frozen object and wrote only this assigned
report.

The controlling mathematical evidence was limited to the frozen manuscript,
the two frozen source records, the frozen bibliography, and direct visual
inspection of the permitted original-detail Rabin and Meyer renders.  I used
the PDFs only for the mandated identity calculation and the renders for page
content.  I ran no test, automated checker, repository script, TeX command,
interim build, handbook-PDF inspection, or build.

This is a manuscript-content review of `N-c-014.d`, not an acceptance of any
other presentation, Part IX, a rendered page, a build, or the book.

## Frozen identity

I independently recomputed SHA-256 for all six objects before substantive
review.  Every value matched the charter exactly.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | exact match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `530EB0B226A239B260938F6BD1A9B247B60A19870F99050D32B879F22639AB23` | exact match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | exact match |
| `spec/research/p09-rabin-1969-source-note.md` | `4F5E6D98191DEA62094B88C81DD116809D05B970351CE99C8CE8ECF9C435D215` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `DC8B5386F57C829DBAFFDB2CF78575682448762E30880AEAC5D1FD19CA492C93` | exact match |

## Printed pages inspected

I visually inspected every page at original-detail input:

- Rabin render `page-01.jpg`, the custody page;
- Rabin renders `page-02.jpg` through `page-36.jpg`, corresponding to every
  printed article page 1 through 35; and
- Meyer renders `page-485.png` through `page-490.png`, physical PDF pages
  485--490 and printed article pages 477--482.

The visual pass included all displayed formulae used here: Rabin's Definitions
1.1--1.7, Theorems 1.1 and 1.3--1.12, formulae (1.1)--(1.3), the Chapter III
word and tree automata, Theorem 3.1, Definitions 3.1--3.7, Lemmas 3.2--3.15,
formulae (3.1)--(3.6), the finite-tree definitions, the Section 3.12 reduction,
and the printed references.  For Meyer it included the tower lower-bound
statement spanning printed pp. 478--479, the list item for the theory of two
successors and prefix on printed p. 479, the surrounding model-of-computation
qualification, and the article bibliography.

## Independent mathematical derivations

### 1. Ordinary semantics and the formula translations

At manuscript lines 965--1014, a run on a valued subtree `(v,T_x)` is a map
from all of `T_x` to the finite state set satisfying the binary move relation
at every node.  Ordinary acceptance at lines 996--1005 is therefore exactly

\[
  \exists r\,[r(x)\in S_0\ \land\ \forall\pi\,
  (\operatorname{In}(r|\pi)\in F)],
  \qquad F\subseteq\mathcal P(S),
\]

with the path predicate supplying the displayed restriction on `pi`.  This is
the definition on Rabin printed p. 6.  It also confirms that an empty move set
may leave no run and that ordinary acceptance is then false.  The frozen text
keeps the transition table `(S,M)` distinct from the automaton
`(S,M,S_0,F)` and does not import the later pair sequence into `F`.

For Definition 1.7, each tuple of node sets has exactly one pointwise bit
label, and every full-root bit-labelled tree recovers exactly one tuple by
taking inverse images of the `1` bits.  Thus the map at lines 1026--1038 is a
genuine bijection, not merely an encoding into a larger class.  The principal
formula construction at lines 1047--1064 is also sound: its truth is witnessed
on finitely many successor iterates of one node, a finite full binary initial
subtree can make every required node an interior labelled node, and Lemma 3.12
then lifts the finite witness language.  In the handbook-owned example at
lines 1066--1076, choosing the witness node and its `0`-child as labelled
interior nodes records exactly
`exists x (x in A and r_0(x) in B)`.  The text correctly does not attribute a
printed transition table for that example to Rabin.

Conversely, after coding the finite state set by `m` bits, the run tracks are
existentially quantified.  A single initial state fixes the root code;
transition clauses force the codes of both children to be legal states, and
induction from the root consequently forces a legal state code everywhere.
The universally quantified path track then checks the Muller family.  This
derives the exact `exists B_1 ... exists B_m forall C` set-quantifier prefix at
lines 1078--1090 and on Rabin printed p. 10.  The matrix is free of set
quantifiers, although it may of course contain individual quantification.

For a closed sentence `G`, introducing a dummy monadic variable if necessary
makes `G` equivalent over the nonempty binary tree to `exists A_1 G`.
Theorem 1.7 supplies an automaton for the matrix, so the sentence is true if
and only if that automaton has a nonempty language.  This proves the frozen
reduction at lines 1092--1097 directly from Rabin printed p. 9; no regular-tree
basis premise is needed or silently used.

### 2. Theorem 3.1 product

Let a branch carry tree-table states `s_0,s_1,...`, and let the deterministic
Muller word run be

\[
  u_0,\quad u_{n+1}=K(u_n,s_n).
\]

The frozen product at lines 1113--1134 starts the root in `(u_0,s_0)` and sends
both children of `(u_n,s_n)` to first coordinate `K(u_n,s_n)=u_{n+1}` while
preserving exactly a permitted tree-table successor pair.  Induction on depth
therefore gives precisely the word run on every branch.  Determinism ensures
that two branches with a common prefix receive the same first-coordinate
history before they split.

The designated family is correctly

\[
 \{C\subseteq U\times S:p_1(C)\in H\}.
\]

Indeed, for an infinite sequence of pairs over finite `U x S`,
`p_1(In(pair sequence))` equals `In(first-coordinate sequence)`: one direction
is immediate, and in the other direction an infinitely recurring first
coordinate must occur infinitely often with at least one second coordinate
because `S` is finite.  The source indexing convention already matches the
displayed product.  Even under the alternative convention that records the
post-letter state, only one endpoint is shifted, which cannot change an
infinite-occurrence set.  The product is therefore exactly typed and proves
the stated path-language absorption on Rabin printed pp. 17--18.

### 3. Dual semantics and the zero-length case

At lines 1142--1187, `phi in [Omega]` has the exact disjunctive pair condition
from Rabin Definition 3.5, while `phi in [Omega,e]` adds avoidance of a lower
set by the whole range.  Definition 3.6 reverses the ordinary prefix to

\[
  \forall r\,[r(x)=s\ \Longrightarrow\ \exists\pi\;(r|\pi\in[\Omega])].
\]

This is the formula on printed p. 25.  In particular, if there is no rooted
run, the implication is true; the frozen text explicitly preserves this
vacuity.

Lemma 3.6 enumerates the nonempty subsets of `S` that are not designated by
`F`.  The enumeration can have length zero.  For the empty sequence,
`[< >]` is empty, so dual acceptance is equivalent to the absence of a rooted
run.  The normalization at lines 1189--1212 is exact.  Because the named root
state makes finite `S` nonempty, every map from an infinite path to `S` has a
nonempty infinitely recurring set.  With
`Omega^dagger=((S,S))`, its only pair would require that set both meet and
avoid `S`, which is impossible.  Hence `[Omega^dagger]` is empty and its dual
language is identical to the zero-length dual language.  This introduces no
new acceptance semantics; it merely supplies a positive-length representation
to the source induction beginning on printed p. 32.

### 4. Marked obligations and well-founded stratification

The complementation outline at lines 1217--1255 retains all finite-state
components visible on Rabin printed pp. 19--32.  A finite marker alphabet
records local obligations.  Simultaneous runs need retain only one active copy
of a given local automaton in a given state at a node; copies in the same state
have identical possible futures, so merging them loses no acceptance choice.
Theorem 3.1 then converts the remaining condition on every branch into an
ordinary tree-automaton condition.

For a mapping `h -> H_h`, define strata by putting into the first stratum the
members with no successors and, at each later ordinal, the as-yet unassigned
members whose entire successor set lies in earlier strata.  Every edge then
strictly decreases stratum.  Conversely, if a residual set remained after the
construction stabilized, repeatedly selecting a successor still in the
residual set would produce an infinite descent.  Thus absence of infinite
descent is equivalent to the ordinal decomposition stated at lines 1226--1232
and on printed p. 19.  This also verifies the second transfinite locus: the
converse direction of Lemma 3.11 forms its obligation stages by transfinite
induction on printed p. 29.  Neither use replaces the finite marker alphabet,
the simultaneous finite-state construction, or the later induction on the
finite pair-sequence length.

The two positive-length half-steps remain separate.  When the last lower set
is empty, Lemmas 3.9--3.10 express local questions through the sequence with
that last pair deleted; Lemma 3.2 combines the resulting ordinary local
automata.  For an arbitrary sequence of the same positive length, Lemma 3.11
uses well-founded deferrals, while Lemma 3.8 converts each local condition to a
sequence of the same length whose last lower set is empty; Lemma 3.4 combines
those obligations.  This is exactly the dependency order summarized at lines
1234--1255 and printed pp. 25--32.  The arbitrary case, last-lower-set-empty
case, and induction on shorter positive length have not been collapsed.

### 5. Finite trees and the root-state boundary

At lines 1258--1282, predecessor closure and being frontiered are correctly
distinct.  Predecessor closure alone allows one child; the displayed
frontiered condition requires both children at every nonterminal node.  The
valuation domain excludes the frontier, exactly as on Rabin printed p. 30.
The transition codomain permits either a pair of genuine states or the pair
`(f,f)`, and `f` is explicitly outside `S`.  It is therefore a distinguished
frontier value, not an automaton state.  The first-use definition gives the
term's standing, its difference from predecessor closure, and the later uses
that require the distinction.

The roles of Lemmas 3.12--3.14 are not conflated.  Lemma 3.12 lifts an accepted
finite initial subtree, Corollary 3.13 supplies principal-formula automata,
Lemma 3.14 is the finite compactness statement for a universal hitting
condition, and Corollary 3.15 supplies the length-one complementation base.
Nothing in these steps changes the infinite input tree or replaces full
monadic quantification by weak quantification.

Definition 3.7 at lines 1342--1350 also has the exact root boundary from
printed p. 33.  The restricted table retains formal state set `R` but replaces
each move set by its intersection with `R' x R'`.  Consequently every state
strictly below the root lies in `R'`; the root itself may be outside `R'`
because it is the source, rather than a target, of the root transition.  The
later reductions use this precise semantics.

### 6. Emptiness and both repaired empty branches

The one-letter erasure at lines 1306--1321 is exact.  A run on a labelled tree
is a run of the union table.  Conversely, at each node of a union-table run,
one may select a letter witnessing its transition, producing a valuation for
which the same map is a run.  Re-rooting invariance then reduces nonemptiness
to acceptance of the unique one-letter full tree.  Complementing that
one-letter language and applying Lemma 3.6 produces the displayed dual
membership question.  This is Rabin's printed pp. 32--33 construction and not
a regular-tree basis argument.

For the finite-state calculation, the arbitrary-sequence stage terminates:
the transfinite stages are disjoint subsets of the current finite state set,
so at most `|R|` stages are nonempty.  Each membership test needed to compute a
stage is converted by Lemma 3.8 to a same-length question with empty last
lower set.

When `L_k` is empty and `k>1`, the exhaustive choice must include
`H=emptyset`.  If `H` is empty, the clause is exactly the current direct dual
question for `Omega_(k-1)` at `s_0`; if it holds, the longer sequence also
holds.  If it does not hold but the length-`k` dual question does, the
`U_k`-recurrence alternative supplies a nonempty `H`, and restricting states
strictly below the root to `R-H` gives the source's shorter questions.  The
frozen branch split at lines 1360--1370 is therefore exhaustive.

The counterexample recorded in the frozen source note also checks directly.
From `s`, the unique run is eventually constantly `a`, so it already has an
`Omega_1`-type path.  The only nonempty proposed `H={u}` fails at `u`, whose
unique run is eventually constantly `b`.  The direct `H=emptyset` branch is
therefore necessary; it is not optional prose.

In the base `Omega=((emptyset,U_1))`, dual acceptance says that every rooted
infinite run has some branch on which a state of `U_1` recurs infinitely.  The
source's nonempty finite set `U_0={s_1,...,s_m}` and finite trees
`E_0,...,E_m` handle the nonvacuous recurrence case.  The repaired allowance
`m=0` at lines 1372--1388 leaves only `E_0`, and the universal requirement to
hit the empty set is then true exactly when no finite run on `E_0` begins at
`s_0`.  If finite compatible runs existed at every depth, their finitely
branching tree of restrictions would have an infinite branch by Koenig's
Infinity Lemma, yielding an infinite run.  Conversely, any infinite run
restricts to every finite initial tree.  Thus a finite no-run obstruction
exists exactly when there is no infinite rooted run, which is exactly the
vacuous dual-acceptance case.

The second frozen counterexample confirms necessity: there is no run from
`s`, so dual acceptance is vacuous; the only nonempty candidate `{u}` fails
because the run from `u` immediately remains in `a` and never hits `u` below
the root.  The empty `U_0` choice and finite no-run tree are the missing case.
The repair preserves the printed nonempty case and changes only the false
exhaustiveness of the printed word “nonempty.”  Its finite-tree existence
condition remains a weak-monadic finite-tree question, leaving the cited
Doner/Thatcher--Wright theorem as an external dependency rather than silently
turning the original full `S2S` input into weak logic.

### 7. Meyer consequence

Meyer printed pp. 478--479 state a lower bound with a tower whose height grows
with input length and apply it, for infinitely many sentences, to each theory
in the list on p. 479.  Item 5 is the theory of two successors and prefix and
credits Meyer and Stockmeyer.  Meyer also states that the lower bound applies
to nondeterministic as well as deterministic Turing machines.

The transfer used at manuscript lines 952--960 is immediate: every sentence
using only the two successors and prefix is already a sentence in Rabin's
displayed binary language, which additionally has the lexicographic order.
An elementary-recursive worst-case decision bound for the latter would, by
restriction to that sublanguage, give one for Meyer's listed theory, contrary
to the growing-height tower lower bound.  This consequence withdraws Rabin's
historical elementary-recursive qualification while leaving the existence and
effectiveness of the decision procedure untouched.

## Mandatory-invariant audit

| Invariant | Frozen manuscript location | Controlling printed source | Mathematical result |
|---|---|---|---|
| R01 | lines 914--917 | Rabin p. 5 | `Lambda` is retained as the empty word/root; no epsilon substitution. |
| R02 | lines 914--963 | Rabin pp. 5, 10--11; Meyer pp. 478--479 | All `0<n<=omega`, both orders and successors, finite definability qualification, omega exception, and later complexity correction are exact. |
| R03 | lines 965--1014 | Rabin p. 6 | Arbitrary roots, table/automaton tuple distinction, `F` type, and ordinary quantifiers are exact. |
| R04 | lines 1142--1187 | Rabin pp. 24--25 | The pair sequence is dual, the prefix is `forall r exists pi`, and no-run vacuity is explicit. |
| R05 | lines 1016--1022, 1092--1097 | Rabin pp. 6--9 | Union/intersection, projection/cylindrification, complement, and emptiness have their exact separate roles. |
| R06 | lines 1026--1064 | Rabin pp. 7--9, 30--31 | The full-root bit map is bijective and the principal, finite-lift, Boolean, projection, and complement stages are distinct. |
| R07 | lines 1066--1076 | Rabin pp. 8, 30--31 | The worked formula is a correct handbook-owned instance and is not misattributed as a printed table. |
| R08 | lines 1078--1097 | Rabin pp. 9--10 | Run coding, one initial state, the exact set-quantifier prefix, and direct sentence-to-nonemptiness reduction are correct. |
| R09 | lines 1099--1138 | Rabin pp. 17--18 | The deterministic Muller product, update, initial set, and designated family are exactly typed; infinite-occurrence acceptance absorbs any endpoint shift. |
| R10 | lines 1142--1187 | Rabin pp. 24--25 | Type, type-empty, quantifier reversal, and complement role are exact. |
| R11 | lines 1217--1224 | Rabin pp. 19--24 | Marking, simultaneous activation, same-state merging, and Theorem 3.1's path check are retained. |
| R12 | lines 1226--1232, 1295--1302 | Rabin pp. 19, 23--30 | No-infinite-descent semantics, lower ordinal strata, and both exact transfinite loci are correct. |
| R13 | lines 1234--1255 | Rabin pp. 25--32 | Sequence lengths and both positive-length half-steps remain distinct after the explicit zero-length normalization. |
| R14 | lines 1258--1282 | Rabin p. 30 | Predecessor closure, frontieredness, valuation domain, transition codomain, and external `f` are exact and definition-before-use compliant. |
| R15 | lines 1283--1293 | Rabin pp. 30--31 | The finite lift, principal-formula use, and compactness use remain distinct; no weak/full or finite/infinite conflation occurs. |
| R16 | lines 1304--1332 | Rabin pp. 32--33 | Alphabet erasure, complement, dual conversion, and one-tree membership are Rabin's actual emptiness reduction. |
| R17 | lines 1334--1350 | Rabin pp. 33--34 | Current finite data are restated and Definition 3.7 preserves the formal state set and root-outside-subset possibility. |
| R18 | lines 1352--1370 | Rabin pp. 33--34 | All `H` choices are covered; the empty choice is the exact direct shorter question and the nonempty choices use the restricted table. |
| R19 | lines 1372--1388 | Rabin pp. 31, 34 | `m=0`, empty `U_0`, the sole finite no-run obstruction, Koenig equivalence, and the external weak-theory dependency are correct. |
| R20 | lines 952--960, 1391--1395 | Rabin pp. 1, 4; Meyer pp. 478--479 | The historical claim is reported but not retained; the lower-bound sublanguage consequence is valid. |
| R21 | lines 1403--1420 | Rabin pp. 11--17 | Linear-order, unary-function, Cantor-space, Boolean-algebra, and game applications retain their stated class-level strength. |
| R22 | lines 1422--1436 | Rabin pp. 1--35 | The reconstruction boundary is explicit; omitted internal tables remain in Rabin, and later Thomas/McNaughton roles are not projected backward. |
| R23 | lines 908--1436 | Rabin pp. 1--35; Meyer pp. 477--482 | Numbering, mathematical locators, symbols, theorem strength, and attributions used in the proof reconstruction agree with the printed pages. |
| R26 | especially lines 918--927, 1047--1064, 1189--1212, 1258--1282 | Rabin pp. 5, 8, 24--25, 30 | New or editorial terminology has a definition and standing where needed; `frontiered` and external `f` have explicit nonredundancy and later use. No hypothetical technical object is named. |
| R27 | lines 965--1436 | Rabin pp. 5--34; Meyer pp. 478--479 | Ordinary/dual, finite/infinite, weak/full, existence/effectivity, source/later route, and decidability/complexity remain separate. |
| R28 | compact record lines 660--672; source note lines 1--24 and 629--637 | governance record, not a printed mathematical claim | Status remains pending Round 3 and any verdict is limited to `N-c-014.d` manuscript content. |
| R29 | lines 1189--1212, 1339--1341 | Rabin pp. 25, 32--34 | A zero-length list denotes no path type; `((S,S))` has the same empty path language and exactly the same no-rooted-run dual semantics. |

I also checked the parallel statements in
`spec/research/p09-rabin-1969-source-note.md` and the compact `N-c-014.d`
record at `spec/research/p09-source-presentations-lot2-3.md` lines 660--672.
Their mathematical claims agree with the frozen manuscript.  The frozen
bibliography supplies the cited Rabin, Meyer, Thatcher--Wright, McNaughton, and
Thomas identities without changing any proof claim.

## Findings

No blocker, must-fix, should-fix, consider, discard, or unresolved-user finding
arose under the mathematical and proof-correctness mandate.  In particular, I
found no incorrect formula, mistyped construction, invalid quantifier
reversal, omitted mathematical edge case, false lower-bound transfer, or
definition-before-use defect in the frozen reconstruction.

VERDICT: ACCEPT
