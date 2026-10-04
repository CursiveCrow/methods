# Round 8 mathematical-and-proof-correctness report: Rabin 1969

## Result and exact scope

I find no blocker, must-fix, should-fix, consider, or unresolved mathematical
finding in the frozen Round 8 snapshot.  The reconstruction is source-faithful
at the mathematical level, its handbook-owned repairs are necessary and
correct, and its stated proof boundary is honest.

This verdict is limited to the manuscript content of presentation
`N-c-014.d` on the six unchanged objects identified below.  It does not admit
all of `N-c-014`, Part IX, any rendered handbook page, a build, another part,
or the book; it is not human review, user acceptance, typesetting approval, or
a judgement about redistributing either source PDF.

## Independence, evidence boundary, and methods

I read the Round 8 charter completely before substantive review.  I used only:

1. `spec/research/boards/p09-rabin-1969/charter.md`;
2. the six objects in the charter's Frozen Round 8 table; and
3. the two original-detail render sets named by the charter.

I did not read any earlier-round report, any other Round 8 report,
`ledger.md`, `transcript/chair.md`, another board, a staging draft, or a layout
extraction.  I did not contact another reviewer, browse the web, inspect a
handbook PDF, run a test or automated checker, invoke a repository script, run
TeX, or perform a build.  The only computation used on the frozen objects was
native SHA-256 hashing for identity.  Formulae, symbols, pagination, and source
wording were checked visually against the original-detail page renders, with
the hash-pinned PDFs controlling.

I read the textual frozen objects in full: all 1--1,437 lines of
`handbook/parts/p09/presentations/n-c-014.tex`; all 1--6,272 lines of
`handbook/bib/handbook.bib`; all 1--665 lines of
`spec/research/p09-rabin-1969-source-note.md`; and all 1--915 lines of
`spec/research/p09-source-presentations-lot2-3.md`.  The histories contained
inside the latter two frozen authored objects were checked for internal and
cross-record status consistency, but were not treated as evidence that any
mathematical claim was true.

## Frozen identity

Each identity below was independently recomputed from the native file, not
copied from the charter.  Every recomputed value equals the Round 8 value.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` | exact match |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` | exact match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695` | exact match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | exact match |
| `spec/research/p09-rabin-1969-source-note.md` | `4C7FA2AFDCED52E1076F5604A826F5AC148707EE0A4AE1772B31F704259F104A` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `9B679F27B410F8FC65F0193AD0E85B4653C32B306002B9C0F19E2EFBACDC8DB2` | exact match |

## Original-detail page inspection ledger

I visually inspected every mandated page at original detail.

For Rabin, I inspected physical PDF pages **1, 2, 3, 4, 5, 6, 7, 8, 9,
10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
27, 28, 29, 30, 31, 32, 33, 34, 35, and 36** in
`rendered/page-01.jpg` through `page-36.jpg`.  Physical p. 1 is the
custody-and-use cover.  Physical pp. 2--36 are, respectively, printed article
pp. **1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, and 35**.

For Meyer, I inspected physical PDF pp. **485, 486, 487, 488, 489, and
490** in `meyer1975-rendered/page-485.png` through `page-490.png`.  The exact
physical-to-printed map is 485/477, 486/478, 487/479, 488/480, 489/481, and
490/482.

The Rabin inspection covered the complete article rather than only the cited
proof pages: introduction and historical complexity claim (printed p. 1),
Definition 1.1 and the finite/omega distinction (pp. 3--5), tree automata and
ordinary acceptance (pp. 5--7), both formula translations (pp. 7--10), all
Chapter II applications (pp. 10--17), the word dependency and Theorem 3.1
(pp. 17--19), marked obligations and simultaneous runs (pp. 19--24), dual
acceptance and both half-steps (pp. 24--30), finite trees and Lemmas
3.12--3.15 (pp. 30--32), the complete source emptiness recursion (pp. 32--34),
and all references (pp. 34--35).  The Meyer inspection covered the theorem's
tower display on printed p. 478, the enumerated theory list and exact
Meyer--Stockmeyer credit on p. 479, and the remaining article and references
through p. 482.

## Independent mathematical reconstruction

### 1. Successor structures, runs, and ordinary acceptance

The manuscript's `n-c-014.tex:914--963` agrees with Rabin printed pp. 3--5.
The root remains `\Lambda`.  For every `0<n<=omega`, the carrier is
`T_n=n^*={i:i<n}^*`, `r_i(x)=xi`, and the displayed structure contains both
the initial-segment and induced lexicographic orders.  The finite-`n`
definability statement and the failure of that elimination at `T_omega` are
not collapsed.  The editorial order subscripts are explicitly eliminable
disambiguations, and the predecessor map is defined before its first use.

At `n-c-014.tex:965--1014`, in agreement with printed pp. 5--7, a valued tree
may be rooted at any `x`, not just at `\Lambda`.  The transition table and
ordinary automaton have the different types

`<S,M>` with `M:S x Sigma -> P(S x S)`, and

`<S,M,S_0,F>` with `S_0 subseteq S` and `F subseteq P(S)`.

For a run `r:T_x->S`, the local condition is
`(r(y0),r(y1)) in M(r(y),v(y))`.  On an infinite path `pi`, finiteness of `S`
ensures that `In(r|pi)` is a nonempty subset of `S`.  Ordinary acceptance is
therefore exactly

`exists r [r(x) in S_0 and for every path pi, In(r|pi) in F]`.

This is one global branching run and a universal condition over all its paths.
It is neither a separate run for each path nor a pair-list acceptance
condition.  The manuscript correctly keeps the later pair list out of
Definition 1.5.  Its account of Lemma 1.2 and Theorems 1.3--1.6 at lines
1016--1023 also has the right dependency structure: union/intersection;
projection away from one label coordinate and the converse addition of an
unconstrained coordinate; complement; and emptiness.

### 2. Bit tracks, the worked principal formula, the converse, and sentences

At `n-c-014.tex:1027--1065` (Rabin printed pp. 7--9), the track map is fully
typed:

`tau(A_1,...,A_n)=(v_A,T)` with `v_A(x)=(chi_A1(x),...,chi_An(x))` and
alphabet `{0,1}^n`.

Injectivity follows by recovering each `A_i` from the nodes whose `i`th bit is
one; surjectivity follows by defining that set from any full-root bit-labelled
tree.  Thus the stated bijection is literal.  The principal-formula normal
form has the correct finite successor suffixes `xw_j`, and the proof keeps
principal recognition, Boolean closure, existential projection, and universal
quantification by complement-plus-projection as separate steps.

The handbook example at lines 1067--1077 is mathematically valid.  For
`P(A,B)=exists x(x in A and r_0(x) in B)`, choose a finite predecessor-closed
full binary prefix deep enough that both `x` and `x0` are outside its frontier.
Those two labelled nodes record exactly the two required bits.  The
finite-tree language is weak-monadically definable, and Lemma 3.12 lifts the
existence of such an accepted finite initial subtree.  The text correctly
labels this calculation as handbook-owned rather than as Rabin's printed
transition table.

Theorem 1.10 is also correctly reconstructed at lines 1079--1091 (printed
pp. 9--10).  After one-start-state normalization, finitely many monadic tracks
encode the unique state value at each node, local first-order conditions encode
the transition table, and a universally quantified set `C` ranges over paths
for the Muller condition.  The displayed monadic prefix
`exists B_1...exists B_m forall C` is therefore right; the remaining matrix
needs only first-order quantification.  For a closed sentence, adjoining a
dummy outer existential set quantifier if necessary justifies Rabin's
`exists A_1 F(A_1)` form.  Truth is exactly nonemptiness of the automaton for
`F`, so Theorem 1.6 closes the decision.  No basis theorem is needed or
silently inserted (`n-c-014.tex:1093--1098`; printed pp. 9--10).

### 3. Theorem 3.1 product and the harmless index position

The product at `n-c-014.tex:1102--1139` matches Rabin printed pp. 17--19.
Let the second-coordinate sequence on a branch be `s_0,s_1,...`, and let the
product states be `(u_n,s_n)`.  The displayed transition gives

`u_(n+1)=K(u_n,s_n)`.

Thus `u_0,u_1,...` is precisely the deterministic word-machine run under the
source's initial-before-first-symbol convention.  Under a post-transition
convention it differs only by its first finite position, which cannot change
an infinitely-recurring-state condition.  The same `K(u_n,s_n)` is placed on
both children, so the unique word history is shared up to a branch and then
continues coherently on each child path; this is exactly where determinism is
needed.

The acceptance family is also correctly typed.  For the pair-state run,

`p_1(In((u_n,s_n))) = In((u_n))`.

The forward inclusion is immediate.  For the reverse inclusion, if `u`
occurs infinitely often, finiteness of `S` forces some pair `(u,s)` to occur
infinitely often.  Hence testing `p_1(C) in H` on the product's recurring pair
set is exactly the deterministic Muller test.  Initial set `{u_0} x S`, state
set `U x S`, update, and designated family are all correct.

### 4. Dual acceptance, vacuity, and the zero-length normalization

The type and type-empty clauses at `n-c-014.tex:1143--1165` agree with Rabin
Definition 3.5 on printed p. 24.  A path is of type `Omega` if some pair has an
infinitely recurring state in `U_i` and none in `L_i`; it is type-empty if,
additionally, its entire range avoids some `L_j`.  The latter is stronger than
merely having no infinitely recurring `L_j` state, and the manuscript retains
that distinction.

Definition 3.6 at lines 1167--1188 has the literal dual prefix
`for every rooted run, there exists a path of type Omega`.  Because this is a
universal implication over runs rooted in the named state, it is true when no
such run exists.  This vacuity is essential in both repaired empty branches
below.

The zero-pair argument at lines 1190--1213 is exact.  Lemma 3.6 enumerates
`P(S) \ (F union {emptyset})`, which can have length zero.  With an empty
sequence, no path is of any listed type, so the dual statement holds iff there
is no rooted run.  For the replacement `Omega^dagger=((S,S))`, every infinite
map into finite nonempty `S` has nonempty `In(phi)`.  It therefore cannot
satisfy both `In(phi) cap S != emptyset` and `In(phi) cap S = emptyset`.
Consequently `[Omega^dagger]=emptyset`, and its dual language again consists
exactly of inputs with no rooted run.  The named state itself guarantees that
the relevant state set is nonempty.  This proves semantic equality, not merely
equisatisfiability, and legitimately feeds the source's positive-length
induction.

### 5. Marked obligations, well-founded dependency, and both half-steps

The local architecture at `n-c-014.tex:1215--1257` agrees with Rabin printed
pp. 19--32.  A marked-tree obligation starts a local run at a marked
node/state.  Running activated copies together and merging copies of the same
local automaton in the same state leaves only finitely many representatives at
each node; Theorem 3.1 then absorbs the remaining path-language check.  This is
a finite-state construction, not an ordinal argument.

The separate endless-deferral condition is correctly typed.  For nonempty
`H`, it is a mapping `h |-> H_h subseteq H`; it is well founded exactly when
there is no infinite chain with `h_(m+1) in H_(h_m)`.  This is a dependency
condition among obligations, distinct by both domain and role from ordinary
run/path acceptance and from the same-state merge.  The surrounding numbered
construction supplies its necessity: a local obligation may defer to a later
marked obligation, and an infinite deferral chain would evade discharge.

The ordinal characterization in Lemma 3.3 is exact.  If each dependency of
`h` lies in a strictly lower ordinal stratum, an infinite dependency chain
would produce an impossible infinite strictly descending ordinal sequence.
Conversely, a well-founded dependency relation admits the rank recursion

`rho(h)=sup {rho(h')+1 : h' in H_h}`,

so every `h' in H_h` has lower rank.  Lemma 3.4 uses this condition to recover
ordinary automaton definability; Lemma 3.11 uses it in the arbitrary-sequence
half-step.  The transfinite step is therefore real but local.

The sequence lengths are not collapsed.  Lemma 3.7 preserves the current
length.  Lemma 3.8 also preserves it while making the last lower set empty.
For `L_k=emptyset`, Lemmas 3.9--3.10 generate local questions for the genuinely
shorter `Omega_(k-1)`.  The first half-step proves the last-lower-empty case
from the induction hypothesis at length `k-1`; the second handles arbitrary
length `k` by Lemmas 3.11, 3.8, and 3.4.  After the explicit zero-list
normalization, induction starts at positive `k=1`.  Transfinite construction
does not replace marked trees, simultaneous runs, either half-step, or this
finite length induction (`n-c-014.tex:1240--1256,1296--1303`; printed
pp. 27--32).

### 6. Finite trees and the exact Lemma 3.12--Corollary 3.15 roles

The finite-tree block at `n-c-014.tex:1259--1294` agrees with printed
pp. 30--32.  The source first permits a finite predecessor-closed binary tree
and calls it *frontiered* precisely when every nonterminal node has both
children; thereafter its unqualified finite trees are frontiered.  The
manuscript gives the exact terminal frontier

`Ft(E)={x in E:x0 notin E and x1 notin E}`

and the two-child condition.  It also explains why this is not redundant with
predecessor closure, which allows a one-child node.  A finite valuation labels
only `E \ Ft(E)`.

The finite-tree automaton has the exact codomain

`M:S x Sigma -> P((S x S) union {(f,f)})`, with `f notin S`.

Thus `f` is an external frontier value, not an ordinary state.  The proof
roles remain separate:

* Lemma 3.12 lifts an automaton-definable collection of finite trees to
  infinite trees having some accepted finite initial subtree.
* Corollary 3.13 applies that lift to the principal-formula gap in Theorem 1.7.
* Lemma 3.14 is compactness, not a principal-formula or frontier construction.
  If no finite subfamily of node--state obligations hit all runs, then for
  every depth there is a finite run prefix avoiding all obligations at that
  depth.  The tree of such prefixes is finitely branching because `S` is
  finite.  Koenig's Infinity Lemma gives a coherent infinite avoiding run,
  contradicting the hypothesis.
* Corollary 3.15 combines that finite hitting result with frontiered finite
  trees and Lemma 3.12 to obtain the ordinary automaton needed for the `k=1`
  complementation base.

These results support automata on infinite input trees.  Their weak-monadic
finite-tree definability does not turn the full input or `S2S` into a weak
theory.

### 7. Section 3.12 emptiness recursion and the two empty-witness repairs

The one-letter reduction at `n-c-014.tex:1307--1333` is correct.  Given a run
of `M^bullet` on the unique one-letter tree, each node transition lies in the
union of the original label transitions, so one may choose at that node a
letter witnessing it and thereby recover a `Sigma`-valuation supporting the
same run.  Conversely, forgetting the labels of any original run gives an
`M^bullet` run.  Thus original nonemptiness is exactly acceptance of the one
full one-letter tree.  Complementing that one-tree language and applying
Lemma 3.6 to the complement returns the original language as a dual language;
no basis theorem occurs.

The recursive questions at lines 1335--1351 always state their current finite
state set, table, pair sequence, and root state.  Definition 3.7 is typed as
`N_R'(s)=N(s) cap (R' x R')` while retaining formal state set `R`.  Since the
restriction applies to child pairs, precisely the states strictly below the
root must lie in `R'`; the root may be outside it.  This root exception is
needed when a queried root state belongs to the removed set.

For arbitrary `Omega`, the source's ordinal stages specialize to disjoint
state strata in the finite one-letter table.  Each nonempty stratum consumes
at least one previously unused state, so there are at most `|R|` nonempty
stages.  Each stage question is converted by Lemma 3.8 to a length-`k`
last-lower-empty question.  This proves effective termination of the arbitrary
half-step (`n-c-014.tex:1353--1359`; Rabin printed p. 33).

For `L_k=emptyset` and `k>1`, the exhaustive reduction must range over every
`H subseteq U_k`, including `H=emptyset`.  The empty choice removes all
hit-a-later-`H` alternatives and is exactly the direct shorter question at the
current root.  For nonempty `H`, restricting strict descendants to `R\H`
turns each condition for a root in `H union {s_0}` into a length-`k-1` dual
question.  The manuscript correctly labels inclusion of the empty choice as a
handbook-owned completion of Rabin's printed nonempty clause
(`n-c-014.tex:1361--1371`; printed p. 34).

I independently checked necessity of this completion using the frozen note's
finite table, not by trusting its conclusion.  Let

`R={s,a,u,b}`, `N(s)={(a,a)}`, `N(a)={(a,a)}`,
`N(u)={(b,b)}`, `N(b)={(b,b)}`,

and `Omega=((emptyset,{a}),(emptyset,{u}))`.  The unique run from `s` has
`In={a}` on every path and hence already supplies an `Omega_1` path.  The only
nonempty candidate is `H={u}`.  From `u`, the unique run has only `b` strictly
below the root, so it has neither an `Omega_1` path nor a later `u`; that
candidate fails.  The empty `H` branch is therefore both sufficient and
necessary here.

The `k=1`, `L_1=emptyset` base must likewise allow `m=0` and
`U_0=emptyset`.  In that case the universal condition on `E_0` says exactly
that no finite run starts in `s_0`.  If an infinite run does not exist, the
finitely branching tree of compatible finite run prefixes cannot have nodes at
every depth; hence some finite full prefix is an obstruction.  Conversely, an
infinite run restricts to a run on every finite prefix.  This is precisely the
Koenig equivalence asserted at `n-c-014.tex:1373--1389` and controlled by
Rabin printed p. 34.

The second frozen counterexample also checks.  Let

`R={s,u,a}`, `N(s)=emptyset`, `N(u)={(a,a)}`, `N(a)={(a,a)}`, and
`Omega=((emptyset,{u}))`.

Dual acceptance from `s` is vacuous.  The sole nonempty candidate
`U_0={u}` fails: a run rooted in `u` has only `a` below the root and therefore
cannot hit `U_0` below it on any finite frontiered prefix.  With
`U_0=emptyset`, a finite nontrivial prefix on which `s` has no run is the
required `E_0`.  Thus the empty base branch is not optional.  The manuscript
preserves the printed nonempty branch, identifies both omissions as
handbook-owned, and does not attribute either repair to Rabin.

The final weak-monadic existence question is finite-tree data and is exactly
where Rabin invokes the external Doner/Thatcher--Wright result.  It does not
alter the infinite-tree input or the full-set semantics of the main theory.

### 8. Applications and proof boundary

The class-level application map at `n-c-014.tex:1404--1421` matches Rabin
printed pp. 10--17:

* Theorem 2.1: the monadic second-order theory of countable linear orders;
  Corollary 2.2: the weak theory of all linear orders; Corollary 2.3: the
  monadic second-order theory of countable well-orders.
* Theorem 2.4: countable unary-function structures; Corollary 2.5: the weak
  theory of arbitrary unary-function structures.
* Theorems 2.6--2.9: the stated closed and `F_sigma` representations and the
  associated Cantor-space, lattice, and unit-interval decision results.
* Theorems 2.10--2.11: the stated Boolean-algebra/ideal classes, with
  countable and arbitrary domains kept distinct.
* Section 2.5: the `S2S` encoding of a strategy and of determinacy for
  `F_sigma` payoff sets, reported as putting Wolfe's theorem within the
  decision procedure rather than as a new proof of a stronger determinacy
  result.

The closing scope at lines 1423--1437 accurately says which constructions are
reconstructed and which detailed tables and inductions remain in the complete
article.  Thomas's later Sections 6.1--6.3 basis route is separately
attributed and is not projected backward.  McNaughton's word result is
identified as an external dependency at Theorem 3.1, not as a Rabin theorem.

### 9. Meyer lower-bound consequence

Rabin's elementary-recursive assertion is visibly present on printed pp. 1
and 4.  Meyer printed p. 478 states a tower lower-bound theorem whose height
grows with input length, and printed p. 479 explicitly lists “the theory of
two successors and prefix,” credited there to Meyer and Stockmeyer.  A formula
in that signature embeds without translation overhead into Rabin's displayed
binary signature: use the same two successors and prefix relation and simply
do not use the extra lexicographic relation.  Therefore an elementary-recursive
worst-case procedure for the displayed theory would yield one for Meyer's
listed sublanguage, contradicting the growing-tower lower bound.  This
withdraws the complexity bound only.  It does not affect the existence or
effectiveness of Rabin's decision construction (`n-c-014.tex:949--960`;
Meyer printed pp. 478--479).

## Mandatory-invariant disposition

The following table records an independent disposition of every R01--R29
invariant, including the two seats not uniquely mathematical because the task
requires the whole charter.

| Invariant | Disposition and controlling locator |
|---|---|
| R01 | Satisfied: `\Lambda` is retained and the non-substitution is explicit (`n-c-014.tex:914--917`; Rabin pp. 3--4). |
| R02 | Satisfied: all `0<n<=omega`, `T_n`, successors, both orders, finite definability, and the `T_omega` exception are exact (`941--963`; Rabin pp. 3--5). |
| R03 | Satisfied: arbitrary roots, distinct table/automaton types, and `exists run / forall paths` with `F subseteq P(S)` are exact (`965--1014`; Rabin pp. 5--7). |
| R04 | Satisfied: the pair sequence is confined to the dual construction, the prefix is `forall run / exists path`, and no-run vacuity is explicit (`1143--1188`; Rabin pp. 24--26). |
| R05 | Satisfied: Theorems 1.3--1.6 and both directions of the one-coordinate operation are stated directly (`1016--1023`; Rabin pp. 6--7). |
| R06 | Satisfied: the track map is typed and bijective, and principal recognition, finite lift, Boolean closure, projection, and complement remain separate (`1027--1065`; Rabin pp. 7--9, 30--31). |
| R07 | Satisfied: the worked `P(A,B)` instance is correct and expressly handbook-owned (`1067--1077`; Rabin pp. 8, 30--31). |
| R08 | Satisfied: one-start normalization, state-track run coding, `exists B-bar forall C`, and direct sentence-to-nonemptiness are exact; no basis step is inserted (`1079--1098`; Rabin pp. 9--10). |
| R09 | Satisfied: every product type, initial state, update, designated family, and finite-shift qualification is correct (`1102--1139`; Rabin pp. 17--19). |
| R10 | Satisfied: type, type-empty, dual quantifiers, and complement role match Definitions 3.5--3.6 (`1143--1188`; Rabin pp. 24--26). |
| R11 | Satisfied: marked local obligations, simultaneous copies, same-state merging, and Theorem 3.1 path checking all appear as necessary finite-state components (`1218--1225`; Rabin pp. 19--24). |
| R12 | Satisfied: within the local architecture block, the deferral need, mapping standing, no-infinite-chain definition, distinction from merging/path acceptance, ordinal equivalence, and Lemma 3.4/3.11 uses are all supplied (`1215--1247,1296--1303`; Rabin pp. 19--32).  The source note supplies the same complete first-use package at lines 418--452, and the compact record at lines 668--672. |
| R13 | Satisfied: Lemmas 3.7--3.8 retain length, the last-lower-empty and arbitrary cases are separate, and induction begins at positive length only after normalization (`1235--1256`; Rabin pp. 25--32). |
| R14 | Satisfied: predecessor closure and frontieredness are distinguished, valuation excludes the frontier, and `f notin S` is external under the exact transition codomain (`1259--1283`; Rabin p. 30). |
| R15 | Satisfied: the four results have their exact lift, principal-formula, compactness, and frontiered-complement roles, with no weak/full conflation (`1284--1294`; Rabin pp. 30--32). |
| R16 | Satisfied: alphabet erasure, complement, conversion to dual membership, and recursive decision reproduce Section 3.12 with no basis theorem (`1307--1333`; Rabin pp. 32--33). |
| R17 | Satisfied: every recursive question states its current table and pair sequence; Definition 3.7 retains `R` and restricts only strict descendants (`1335--1351`; Rabin p. 33). |
| R18 | Satisfied: every `H subseteq U_k` is included, empty `H` is the direct shorter question, nonempty `H` uses the restricted table, and finite-stratum termination is explicit (`1353--1371`; Rabin pp. 33--34). |
| R19 | Satisfied: `m>=0`, possibly empty `U_0`, `E_0,...,E_m`, the no-run obstruction, Koenig equivalence, handbook ownership, and the external weak-theory dependency are all exact (`1373--1400`; Rabin p. 34). |
| R20 | Satisfied: Rabin's claim is historical, Meyer gives the growing-tower lower bound and exact Meyer--Stockmeyer credit, and the sublanguage argument preserves decidability/effectivity (`949--960`; Rabin pp. 1, 4; Meyer pp. 478--479). |
| R21 | Satisfied: all five Chapter II application families are present at the source's class strength (`1404--1421`; Rabin pp. 10--17). |
| R22 | Satisfied: the reconstruction boundary, retained source detail, Thomas basis route, and McNaughton dependency are explicitly separated (`1114--1139,1423--1437`; Rabin pp. 17--19, 32--34). |
| R23 | Satisfied: source numbering, notation, locators, strength, and attribution agree throughout the four frozen textual records and the inspected pages. |
| R24 | Satisfied: reader, detailed note, compact record, and bibliography agree.  Relevant bibliography entries are `McNaughton1966` at lines 2290--2299, `Thomas1997` at 2346--2355, `Meyer1975Complexity` at 5938--5947, `Rabin1969` at 5973--5982, and `ThatcherWright1968` at 5993--6002.  The Rabin URL, Thatcher--Wright pp. 57--81 and DOI, Meyer correction, and pending Round 8 status are consistent. |
| R25 | Satisfied: the source note distinguishes scholarly access from an open-content or republication licence and calls the PDFs/renders research objects (`source-note:48--102`).  No other frozen record inflates those rights. |
| R26 | Satisfied: source technical names are introduced with exact type/standing and use.  In particular, well-foundedness has its mapping/no-chain/ordinal/use package, and `frontiered` has necessity, exact definition, property standing, nonredundancy from predecessor closure, and later uses.  Editorial names are explicitly eliminable disambiguations. |
| R27 | Satisfied: finite/infinite tree, weak/full logic, ordinary/dual acceptance, existence/effectivity, source/later route, and decidability/complexity remain separate. |
| R28 | Satisfied: the frozen records retain pending-review language and make no broader admission.  This report likewise accepts only `N-c-014.d` manuscript content on these hashes. |
| R29 | Satisfied: the list may have length zero, the empty list denotes no rooted run under dual semantics, and `((S,S))` has empty path language and exactly the same dual language (`1190--1213,1340--1342`; Rabin pp. 25--32 for the surrounding source induction). |

## Cross-record status, bibliography, and rights check

The detailed note's opening status (`source-note:3--46`), closing status
(`622--665`), and compact record (`lot2-3:660--672,913--915`) agree: the body
and reconstruction exist; prior rounds are historical; Round 8 review is
required; and no terminal admission, build, visual handbook approval, human
review, or user acceptance is claimed.  The reader's final proof boundary at
`n-c-014.tex:1423--1437` is consistent with those records.

The bibliography identities agree with the inspected source title pages and
references: Rabin 1969, volume 141, pp. 1--35 and AMS DOI; Meyer in ICM 1974
proceedings volume 2, published 1975, pp. 477--482; Thatcher--Wright 1968,
volume 2(1), pp. 57--81 and DOI; McNaughton 1966, volume 9(5), pp. 521--530;
and Thomas 1997, pp. 389--455 and DOI.  No bibliography entry is used to
upgrade an uninspected theorem beyond the claim attributed to it.

The custody cover and note support reading and ordinary scholarly
reconstruction only.  Public availability of the Rabin scan and official
Meyer proceedings does not establish permission to redistribute either PDF or
its page images.  Nothing in the reader or compact record says otherwise.

## Findings

No findings.  In particular, I found no unresolved blocker or must-fix and no
advisory defect that would improve correctness without changing the verdict.

## Verdict limitation

Acceptance means only that the frozen `N-c-014.d` manuscript content is
mathematically and proof-architecturally fit for the board's manuscript gate.
It is not evidence of compilation, typesetting, rendered-page quality, a
general correctness theorem for the entire handbook, human verification, or
permission to redistribute source material.

VERDICT: ACCEPT
