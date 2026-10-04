# Round 2 mathematical and proof-correctness review: TATA 2008

## Mandate and independence

I reviewed the complete Frozen Round 2 seven-object snapshot identified by the
charter, independently of the withdrawn Round 1 work and independently of the
other Round 2 seats. I used only the charter, those seven frozen objects, and
the twenty-seven chartered original-detail renders. I did not consult a board
ledger, chair transcript, another report, another board, conversation history,
memory, staging or layout material, or web results. I did not contact another
reviewer. I ran no test, test harness, automated checker, repository script,
TeX command, build, or handbook-PDF inspection.

## Native identity recomputation

I independently recomputed the SHA-256 digest of every Frozen Round 2 object.
The native values are:

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-tata-2008/tata-2008.pdf` | `3EB9C3F9A1A9A3BD45EC1E50BD50A1C10010789B542A2818F030A7246F9B5B22` | exact charter match |
| `handbook/parts/p09/presentations/n-c-015.tex` | `69AC3973E247EF090D9C78E92991BCEEDB30C0145CC276DC2C45F85DE984B4AD` | exact charter match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD` | exact charter match |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` | exact charter match |
| `spec/research/p09-tata-2008-source-note.md` | `5D31699B3219A9340435D41B0B8B74770EA405B70C3E58C1059CB95D09F434A9` | exact charter match |
| `spec/research/p09-source-presentations-lot2-3.md` | `0E693D15418B828B650FC4A9F8310484B8121E806C45AEA07701311727DCB93F` | exact Round 2 charter match |
| `spec/research/p09-thatcher-wright-1968-acquisition-note.md` | `547821EE7F3B8078C884C2145D4CE4857715F3E2B9775DC57B573098D96C7275` | exact charter match |

The compact record therefore has the Frozen Round 2 identity, not the
withdrawn Round 1 identity.

## Original-detail source inspection

I visually inspected every chartered render at original detail. The inspection
set was exactly:

- `core-rendered/page-001.png`, `page-002.png`;
- `core-rendered/page-012.png`, `page-013.png`, `page-014.png`;
- `core-rendered/page-020.png`, `page-021.png`, `page-022.png`,
  `page-023.png`, `page-024.png`, `page-025.png`, `page-026.png`,
  `page-027.png`, `page-028.png`;
- `core-rendered/page-031.png`, `page-041.png`, `page-044.png`; and
- `relevant-rendered/page-088.png`, `page-089.png`, `page-090.png`,
  `page-091.png`, `page-092.png`, `page-093.png`, `page-094.png`,
  `page-095.png`, `page-096.png`, `page-097.png`.

The physical-to-printed relation visible in the object is the chartered one:
physical page 1 is the HAL cover, physical page 2 is the internal title, and
physical page `n+1` is printed page `n` throughout the numbered material used
here. The title pages establish the eight-author order. The body footers show
`TATA — November 18, 2008 —`. Printed pp. 11--12 expressly limit the book to
finite-tree automata and exclude infinite-tree automata.

## Independent mathematical reconstruction and stress test

### Ranked terms, runs, and recognition

For a finite ranked alphabet, the least-term construction gives a leaf for
each nullary symbol and gives `f(t_1,...,t_n)` only when `f` has arity `n` and
the ordered children are already terms. Thus every input is a finite ordered
ranked tree. TATA's data are literally `A=(Q,F,Q_f,Delta)` (printed p. 20),
whereas the shared handbook definition uses `(Q,Sigma,Delta,F)`; the reader's
symbol map at `n-c-015.tex:12--30` prevents either occurrence of `F` from being
misread.

A run on a term `t` is a map from `Pos(t)` to `Q` satisfying, at every position
`p` labelled by an `n`-ary `f`, a rule
`f(r(p1),...,r(pn))->r(p)`. At `n=0`, this is exactly a nullary rule
`f->r(p)`; there is no hidden initial state. A run accepts exactly when
`r(epsilon)` is final. This reproduces printed pp. 20--22 and the reader at
`n-c-015.tex:12--30`.

This typing handles a partial transition table correctly: a term may have no
run at all. It also handles an empty final set, which accepts nothing, and an
alphabet with no nullary symbols, for which the least ground-term set is empty.
Unreachable states cannot manufacture a run because every state assigned at a
node must be justified recursively by an actual rule below that node.

### Determinization, closure, and emptiness

For each term `t`, let

`S(t)={q in Q : the original automaton has a run on t with root q}`.

The subset transition on an `n`-ary symbol is uniquely forced:

`f(S_1,...,S_n) -> {q : some q_i in S_i satisfy f(q_1,...,q_n)->q}`.

The nullary case is the set of all targets of rules `f->q`. Structural
induction gives the exact invariant that the deterministic state reached on
`t` is `S(t)`, so acceptance is equivalent to
`S(t) intersect Q_f` being nonempty. A missing original transition yields the
empty subset rather than a false accepting run. The algorithm on printed
pp. 25--27 retains only subsets realized by ground terms, including the empty
subset if it is realized. Original unreachable states never enter a realized
subset. This verifies the same-language and reachable-subset assertions at
`n-c-015.tex:39--41` without assuming that the original transition table was
complete.

For Boolean closure (printed p. 30), union may use the disjoint-state
construction, intersection may use the product construction, and complement
first uses deterministic completion before reversing final-state status. The
source expressly warns on p. 30 why completeness matters to a product, and
printed p. 24 gives the missing-transition state completion. The reader merely
states the effective closure theorem at `n-c-015.tex:41--47`; it does not omit
a premise from a displayed complement proof or claim that a partial table can
be complemented by reversing finals directly.

For emptiness, start with every target of a nullary rule and close upward under
rules whose child states are all already marked. Induction on term height proves
both directions of

`q is marked iff some ground term has a run ending in q`.

Therefore the language is nonempty exactly when a final state is marked. No
unreachable final state can cause a false positive, and no nullary rule is lost
in the base case. Printed p. 40 supplies the accessible-final characterization
and the linear least-fixed-point/Horn implementation; the bounded wording at
`n-c-015.tex:42--46` correctly makes linearity relative to the automaton
representation.

### The handbook-owned small run

With only `a->q_a`, `b->q_b`, and `f(q_a,q_b)->q_f`, the leaves of `f(a,b)`
force `q_a,q_b`, the root rule forces `q_f`, and finality accepts. Removing the
root rule leaves the root without any applicable transition, so the term has
no run rather than merely a nonfinal run. The calculation at
`n-c-015.tex:32--37` is correct and is explicitly identified as handbook-owned
at `n-c-015.tex:154--160`; it is not presented as a source-printed example.

### WSkS syntax, semantics, and the finite-set encoding

In the fixed WSkS structure, first-order variables range over words in
`{1,...,k}*`, while monadic variables range only over finite word sets
(printed pp. 87--90). Proposition 3.3.1 replaces an element variable by a
singleton-set variable and leaves the four restricted atoms
`X subseteq Y`, `Sing(X)`, `X=Yi`, and `X=epsilon`. The reader's meanings at
`n-c-015.tex:49--60` preserve the direction of the successor: the sole word of
`X` is obtained by appending `i` to the sole word of `Y`.

For a finite tuple `(S_1,...,S_n)`, the encoded domain contains the root and the
needed prefix positions. Coordinate `i` is `1` at membership, `0` at a proper
prefix leading to later membership, and `bottom` when neither membership nor a
later member exists. Every vector with a `0` or `1` is `k`-ary; only
`bottom^n` is nullary. Consequently:

- the all-empty tuple is the one-node term `bottom^n`, not an all-zero tree;
- an empty individual track remains `bottom` even at positions kept alive by
  another track;
- occupied leaves still have `k` nullary `bottom^n` padding children; and
- padding nodes cannot be confused with positions of the represented sets.

For Example 3.3.3, the reader's root, first-level, occupied second-level, and
padding labels at `n-c-015.tex:62--71` agree exactly with printed pp. 90--91 and
Figure 3.7. In particular the empty `S_2` track is `bottom` everywhere.

The six Figure 3.9 rules transcribed at `n-c-015.tex:85--96` are complete:
`bottom bottom`, `00`, `01`, `11`, `bottom 0`, and `bottom 1`. On a valid
encoding these are exactly the local coordinate pairs compatible with
`X subseteq Y`. The all-empty encoding is accepted by the nullary
`bottom bottom->q` rule. If `X` has a member not in `Y`, either `1 bottom`,
`10`, or an ancestor `0 bottom` appears and has no rule. The induction is
evaluated on the canonical encodings defined on printed pp. 90--91; arbitrary
over-padded alphabet terms are not silently treated as assignments.

### Restricted formula to automaton

Lemma 3.3.4 (printed pp. 91--93) is correctly reconstructed at
`n-c-015.tex:85--96`:

1. the atomic cases use the source automata, including the complete inclusion
   list above;
2. before union for a disjunction, both automata receive unconstrained tracks
   for variables free only in the other disjunct;
3. negation uses effective complement, which incorporates determinization and
   completion from Chapter 1; and
4. existential monadic quantification projects away its track.

Missing free-variable tracks therefore cannot accidentally constrain a
disjunct, an empty set remains a legitimate projected value, and a partial
atomic automaton is not complemented by a mere unqualified final-state flip.

### Automaton to restricted formula and the local clause

Lemma 3.3.6 (printed pp. 94--95) existentially supplies one set `Y_q` for each
state. `Partition(D,(Y_q))` makes their union exactly the encoded finite domain
and makes them pairwise disjoint; an unreachable state may simply receive the
empty set. The root clause selects a final state. For a position carrying
symbol `f` and state `q`, the reader correctly uses

`(x in X_f and x in Y_q) => OR_{f(q_1,...,q_s)->q} AND_i xi in Y_{q_i}`.

The implication is in the correct direction, the disjunction selects a rule
whose target is the parent state, and each conjunct points from the parent to
the corresponding child state. If the table has no matching transition, the
empty disjunction is false. If `f` is nullary, a matching nullary transition
contributes an empty conjunction, hence true; without such a transition the
clause is false. The source's ground-term condition ensures every required
child is in `D`, while the state partition labels every such child exactly
once. Thus a satisfying assignment is exactly an accepting bottom-up run, in
both directions. This verifies `n-c-015.tex:98--110` against printed p. 94 and
the continuation on p. 95.

### Finite-tree MSO bridge and both logical directions

For a finite ranked input tree, let `D` be its finite position set and let
`X_f` be the positions labelled by each ranked symbol. The source's `Term`
conditions on printed p. 89 require nonempty prefix closure, a partition by
labels, exactly the children prescribed by a symbol's arity, and no higher
children. A label atom translates to `x in X_f`; the `i`-child atom translates
to `y=xi`. Restricting element quantifiers to `D` and monadic quantifiers to
subsets of `D` prevents either kind of variable from ranging over the unused
remainder of the ambient successor tree.

In the formula-to-automaton direction, this domain-and-label coding followed by
Lemma 3.3.4 yields a finite bottom-up automaton for the coded finite inputs. In
the automaton-to-formula direction, the partition, final-root condition, and
local transition clauses from Lemma 3.3.6 give an MSO definition of precisely
the accepting runs. These are inverse at the level asserted by the main
theorem; the ambient prefix tree is only the coding structure. The bridge at
`n-c-015.tex:73--83` and the shared statement at
`logic-in-computer-science.tex:876--891` therefore do not substitute an
infinite input for a finite ranked tree.

### Theorem qualification and the closed-sentence reduction

Printed p. 95 calls Theorem 3.3.7 a slogan that is "not very precise" and
directs precision back to Lemmas 3.3.4 and 3.3.6. The reader preserves that
qualification at `n-c-015.tex:112--114`.

With no free variables there are no tracks. Under the source's explicit
convention, the unique encoded input is the nullary constant `top`. A
nondeterministic bottom-up automaton accepts that one term exactly when it has
a nullary transition `top->q_f` to some final state. This remains correct for
an empty final set and for a partial transition table. The reduction at
`n-c-015.tex:114--118` matches the proof of Theorem 3.3.8 on printed p. 95 and
does not revive the rejected all-zero-track description.

### Exercise 1.4

Printed p. 43 fixes exactly the alphabet with `a` nullary and `f` binary. Suppose
a deterministic bottom-up automaton recognized
`{f(t,t):t in T(F)}`. For every term `t`, acceptance of `f(t,t)` supplies a run
on each copy of `t`; hence even a partial deterministic automaton must reach a
state on every `t`. If distinct `t,u` reached the same state `q`, the accepting
run on `f(t,t)` would supply a transition `f(q,q)->r` with final root state
`r`. The same transition would accept `f(t,u)`, contrary to `t!=u`. Thus the
state reached distinguishes every ground term. Since the specified term
algebra is infinite and the state set is finite, this is impossible. The proof
at `n-c-015.tex:120--129` is complete, handles partiality, and is correctly
marked handbook-owned at lines 154--160.

### Weak/full and finite/infinite boundaries

WSkS quantifies only over finite subsets of the infinite successor structure;
full SkS permits arbitrary, hence possibly infinite, subsets. Printed
pp. 95--96 explains that infinite inputs require root-down devices and that
complement is no longer obtained by bottom-up determinization. On an actually
finite structure every subset is finite, so weak and full monadic
quantification have the same range. This fact does not change the automaton's
input from a finite ranked term into an entire infinite labelled tree. The
reader at `n-c-015.tex:131--139` and the shared theorem at
`logic-in-computer-science.tex:876--891` preserve all three distinctions.

## Mandatory invariant dispositions

| ID | Disposition | Basis |
|---|---|---|
| T01 | satisfied | HAL cover and title, internal footers, bibliography, `n-c-015.tex:6--10`, source note lines 14--34, compact record lines 694--696: one eight-author 18 November 2008 object, 263 physical/262 monograph pages, with the evolving-work 2007 label kept distinct. |
| T02 | satisfied | HAL custody cover; source note lines 31--34: authorized public research deposit, no asserted CC or blanket republication licence, renders retained only as evidence. |
| T03 | satisfied | TATA printed pp. 11--13; `n-c-015.tex:6--10,131--139`: operative inputs are finite terms, not Rabin inputs. |
| T04 | satisfied | TATA printed pp. 19--20; `n-c-015.tex:12--30`; shared definition lines 845--874: nullary and positive arities, ordered ground terms, exact TATA tuple, and explicit symbol map. |
| T05 | satisfied | TATA printed pp. 20--22; `n-c-015.tex:20--27`: correctly typed bottom-up rules, nullary base, final root, and recognition. |
| T06 | satisfied | TATA printed pp. 23--27; `n-c-015.tex:39--41`: target uniqueness, exact language invariant, reachable subsets, empty-subset/partial-table case retained. |
| T07 | satisfied | TATA printed pp. 24, 30, 40; `n-c-015.tex:41--47`: effective closure, required completion, exact marking criterion, and representation-bounded linearity. |
| T08 | satisfied | `n-c-015.tex:32--37,154--160`: valid finite run, missing root rule gives no run, handbook ownership explicit. |
| T09 | satisfied | TATA printed pp. 87--90; `n-c-015.tex:49--60`: correct word/finite-set ranges, singleton translation, four exact atoms. |
| T10 | satisfied | TATA printed pp. 90--91; `n-c-015.tex:62--71`: correct arities, coordinate meanings, empty track, named labels, and nullary bottom padding. |
| T11 | satisfied | TATA printed p. 89 and pp. 94--95; `n-c-015.tex:73--83`: `D`, label subsets, atom translations, both quantifier restrictions, and coding/input distinction are explicit. |
| T12 | satisfied | TATA printed pp. 91--93, especially Figure 3.9; `n-c-015.tex:85--96`: all six rules, missing-coordinate extension, union, complement, and projection. |
| T13 | satisfied | TATA printed pp. 94--95; `n-c-015.tex:98--110`: one set per state, exact-domain partition, final root, correct implication/disjunction/child direction, including nullary and missing-transition semantics. |
| T14 | satisfied | TATA printed p. 95; `n-c-015.tex:112--118`: slogan qualification, exact lemmas, no-track/`top` convention, and nullary final transition. |
| T15 | satisfied | TATA printed p. 43; `n-c-015.tex:120--129,158--160`: exact alphabet and language, reachability premise, crossed-pair separation, handbook proof ownership. |
| T16 | satisfied | TATA printed pp. 95--96; `n-c-015.tex:131--139`: finite/arbitrary set ranges and finite/infinite automaton boundary are not conflated. |
| T17 | satisfied | `logic-in-computer-science.tex:845--891` agrees with `n-c-015.tex:12--139` on finite ranked trees, bottom-up runs, MSO equivalence, effective operations, and Rabin nonconflation. |
| T18 | satisfied | `n-c-015.tex:154--160`, compact record lines 702--706, source note lines 173--176: operative outline and ownership are exact; no complete-proof or complete-state-table claim is made. |
| T19 | satisfied | `n-c-015.tex:141--152`, compact record lines 684--692, Thatcher--Wright note lines 3--34 and 64--82: only identity and abstract scope are reported; the body-dependent artifact remains owed and RC-1713 remains only a lead. |
| T20 | satisfied | Title pages, bibliography entries, reader, shared text, detailed note, compact record, and acquisition note agree on authors, date/version, theorem numbers, page locators, notation, ownership, and open statuses. The Round 2 compact hash contains the reconciled adjacent Thomas/Rabin administrative sentence. |
| T21 | satisfied | The reader defines and types each relied-on mathematical object at first material use; the historical open obligation does not assign TATA's modern definitions to Thatcher--Wright. No speculative term is used as a proved object. |
| T22 | satisfied | `n-c-015.tex:154--161`, source note lines 3--12 and 178--185, compact record line 706, Thatcher--Wright note lines 64--82: reconstruction and acquisition status are separated from independent admission, build, visual publication review, human/user review, and book completion. |

## Findings and scope of decision

No blocker, must-fix, should-fix, consider, discard, or unresolved-user finding
is filed. The acceptance below concerns only the manuscript content of
`N-c-015.b` on the seven exact Frozen Round 2 identities above. It does not
admit `N-c-015.a`, `N-c-015` overall, Part IX, a build, rendered handbook,
human or user review, the book, or publication.

VERDICT: ACCEPT
