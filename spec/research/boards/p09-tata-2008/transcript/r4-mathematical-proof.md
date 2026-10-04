# TATA Round 4 — mathematical and proof-correctness review

## Seat, independence, and exact scope

I reviewed the hash-pinned Round 4 snapshot independently in the mathematical
and proof-correctness seat. I read the charter and all seven frozen textual
objects completely, recomputed the nine native SHA-256 identities before
judgment, and visually inspected every one of the twenty-seven named TATA
renders and five named Thomas identity/page-map renders in original-detail
mode. I did not consult a prior-round report, the board ledger, the chair
transcript, another Round 4 report, another board or board transcript,
conversation history, memory, staging or layout material, a handbook PDF, or
web results, and I did not contact another reviewer.

This report decides only whether the frozen `N-c-015.b` TATA reconstruction may
be admitted at manuscript-content level. It does not review or admit
`N-c-015.a`, `N-c-015` as a whole, the Thomas reconstruction, the registered
Thomas 1997 chapter, Part IX as a whole, a build, a rendered handbook page,
human or user review, the book, or publication.

## Native identity recomputation

All values below were recomputed from the local native objects and agree
exactly with the Round 4 freeze.

| Frozen object | Recomputed SHA-256 | Result |
|---|---|---|
| `tmp/pdfs/p09-tata-2008/tata-2008.pdf` | `3EB9C3F9A1A9A3BD45EC1E50BD50A1C10010789B542A2818F030A7246F9B5B22` | match |
| `handbook/parts/p09/presentations/n-c-015.tex` | `69AC3973E247EF090D9C78E92991BCEEDB30C0145CC276DC2C45F85DE984B4AD` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `70CFEBC05E1F574703FA6F8B1367C2EBBA1A640A57B2DEEC8D144E88328A7117` | match |
| `handbook/bib/handbook.bib` | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` | match |
| `spec/research/p09-tata-2008-source-note.md` | `E8BB8448B3AAA119575EBC6EE16BD79A5F4F50A584875234513A61FC627FA948` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `0A1E5537F20DC16D6421FE6FC21B846180B6548F8AA9B5B6A2CC5942FC0524B3` | match |
| `spec/research/p09-thatcher-wright-1968-acquisition-note.md` | `547821EE7F3B8078C884C2145D4CE4857715F3E2B9775DC57B573098D96C7275` | match |
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` | match |
| `spec/research/p09-thomas-1996-report-source-note.md` | `9B06269638D97345123D23434BB9B299EDACF6B1373C9190E92190E3FBE45581` | match |

## Complete reading and visual evidence record

The seven frozen textual objects read in full were the 161-line reader, the
complete shared Part IX file, the complete bibliography, the complete TATA
custody/reconstruction note, the complete compact source-presentation record,
the complete Thatcher--Wright acquisition note, and the complete Thomas
precursor/version note.

The TATA visual inspection covered, individually:

- `core-rendered/page-001.png`, `page-002.png`;
- `core-rendered/page-012.png`, `page-013.png`, `page-014.png`;
- `core-rendered/page-020.png`, `page-021.png`, `page-022.png`,
  `page-023.png`, `page-024.png`, `page-025.png`, `page-026.png`,
  `page-027.png`, `page-028.png`;
- `core-rendered/page-031.png`, `page-041.png`, `page-044.png`; and
- `relevant-rendered/page-088.png`, `page-089.png`, `page-090.png`,
  `page-091.png`, `page-092.png`, `page-093.png`, `page-094.png`,
  `page-095.png`, `page-096.png`, `page-097.png`.

These images establish the HAL cover and internal title, printed introduction
pp. 11--13, printed pp. 19--27, 30, 40, and 43, and the complete controlling
Section 3.3 passage at printed pp. 87--96. The physical-to-printed map is exact:
physical page 1 is the added HAL cover, physical page 2 is the monograph title,
and physical page `n+1` is printed page `n` in the relevant numbered body.

The Thomas visual inspection covered, individually,
`inspect-title-01.png`, `inspect-title-02.png`, `inspect-title-03.png`,
`inspect-body-start-04.png`, and `inspect-body-end-75.png`. They show the May
1996 Kiel Bericht 9607 identity, the literal prospective phrase *Handbook of
Formal Language Theory*, the contents, printed p. 1, and printed p. 72. This was
identity, version, and page-map evidence only, not a review of Thomas's
mathematics.

No test, test harness, automated checker, repository script, TeX command,
build, or handbook-PDF inspection was run.

## Independent mathematical reconstruction and stress test

### Finite ranked terms, automata, and runs

For a finite ranked alphabet, the ground terms are the least set containing
each nullary symbol and closed under `f(t_1,...,t_n)` when `f` has arity `n`.
The position diagram is consequently a finite ordered tree. TATA's literal
automaton tuple is `A=(Q,F,Q_f,Delta)`: `F` is the ranked alphabet, `Q_f` is the
final-state set, and a rule for `f` of arity `n` has the form
`f(q_1,...,q_n) -> q`. The reader's map to the shared handbook tuple
`(Q,Sigma,Delta,F)` is explicit and type-correct (`F_TATA` maps to `Sigma`, and
`Q_f` maps to handbook `F`); see reader lines 12--30, shared definition lines
848--877, and TATA printed pp. 19--22.

A run is a map from every term position to a state satisfying one rule at each
node. For a nullary node, this condition is exactly a nullary rule `a -> q`.
Acceptance is existence of a run whose root is final. Thus a partial transition
table can leave a term with no run; no implicit dead state is assumed in the
nondeterministic definition. The small handbook example at reader lines 32--37
has its only licensed leaf states `q_a,q_b` and its licensed root state `q_f`,
so it accepts `f(a,b)`. Deleting `f(q_a,q_b) -> q_f` leaves no rule applicable
at that root and hence no run. The source supplies the general run semantics at
printed pp. 20--22; the reader correctly identifies the particular example as
handbook-owned at lines 154--160.

### Determinization, Boolean closure, and emptiness

Given child subsets `S_1,...,S_n`, the subset construction's uniquely
determined target is

`{q in Q : some q_i in S_i satisfy f(q_1,...,q_n) -> q in Delta}`.

Induction on the input term shows that this subset is exactly the set of all
states reachable at that term in the original automaton. A subset is final
exactly when it meets `Q_f`, so the accepted language is unchanged. This also
shows why “deterministic” means at most one target for a fixed symbol and fixed
child-state tuple, not one rule per symbol. Restricting the constructed state
set to subsets reached by ground terms preserves that induction and the
language. Reader lines 39--46 and compact-record lines 698--702 retain precisely
that strength; TATA Theorem 1.1.9 is visible at printed pp. 25--27.

Effective union and intersection use the standard disjoint-union/product
constructions, and complement is taken after determinization and completion;
the reader claims closure, not an invalid direct complement of an incomplete
nondeterministic machine. This agrees with Theorem 1.3.1 at printed p. 30.

For emptiness, initialize the marked set with every target of a nullary rule,
then repeatedly mark a target when all child states of one transition are
already marked. Induction on term height proves that the least fixed point is
exactly the accessible-state set. Therefore the language is nonempty exactly
when the marked set meets the final-state set. This handles nullary terms,
partial tables, and unreachable states without assuming completeness. Reader
lines 42--46 state the final-state criterion and limit linear time to the
automaton representation; TATA Theorem 1.7.4 and its least-fixed-point/Horn
proof are on printed p. 40. There is no theorem-strength inflation.

### WSkS semantics and the finite-set encoding

For fixed `k >= 1`, first-order WSkS variables denote words in
`{1,...,k}*`, successor appends a letter, and monadic variables denote finite
sets of such words. Replacing a first-order variable with a singleton-set
variable yields exactly the four restricted atoms `X subseteq Y`, `Sing(X)`,
`X=Yi`, and `X=epsilon`; the singleton side conditions give the asserted
standing of the last two atoms. Reader lines 49--60 agree with TATA printed
pp. 87--90.

For a finite tuple `(S_1,...,S_n)`, the encoded tree contains the root and the
prefixes of words occurring on some track. At position `p`, track `i` is `1`
when `p` belongs to `S_i`, `0` when `p` does not belong but is a prefix of a
word in `S_i`, and `bottom` otherwise. Any product symbol
with a `0` or `1` coordinate has arity `k`; the all-`bottom` symbol is nullary.
In particular, an all-empty tuple is represented by the one-node all-`bottom`
tree, not by a missing input.

For Example 3.3.3, direct calculation gives root `(1,bottom,0)`, position 1
`(0,bottom,0)`, position 2 `(bottom,bottom,0)`, position 11 `(1,bottom,1)`,
position 22 `(bottom,bottom,1)`, and all extra leaves introduced to complete
the `k` children of a non-nullary product symbol as all-`bottom`. This matches
reader lines 62--71 and the printed diagram and definition at pp. 90--91. It
does not replace nullary padding with an all-zero-track slogan.

### Formula to automaton

For the atomic inclusion `X subseteq Y`, the one-state final automaton has
exactly

`bottom bottom`, `00`, `01`, `11`, `bottom 0`, `bottom 1`

as its six product labels, with the binary labels looping on `(q,q)` and the
all-`bottom` label nullary. The absent labels are exactly the combinations that
would force an `X` member, or the prefix of an `X` member, without the required
`Y` track. This agrees symbol for symbol with Figure 3.9 on printed p. 92 and
reader lines 85--96.

In the structural induction, a disjunction first adds freely varying tracks for
variables absent from one disjunct and then unions the two languages; negation
uses effective complement; and existential set quantification projects away
the quantified track. On genuine finite-set encodings these operations have
the required assignment semantics. Missing variables and empty sets therefore
do not change the free-variable type of the resulting automaton. These are the
three source steps on printed p. 93, not an asserted reproduction of every
mechanical state table.

### Automaton to formula and the local clause

For each automaton state `q`, quantify a monadic set `Y_q` and require the
family to partition exactly the finite encoded position set. Require the root
to belong to some `Y_q` with `q` final. For every input symbol `f` and every
state `q`, require

`forall x ((x in X_f and x in Y_q) ->`
`  OR_{f(q_1,...,q_s)->q in Delta} AND_{i=1}^s xi in Y_{q_i})`.

The implication direction is correct: a node already assigned state `q` must
have one incoming transition to `q` whose ordered child states match. The
partition then makes those child assignments unambiguous at the level required
by a selected run, while nondeterminism remains existential through the choice
of the state partition. For `s=0`, an available nullary rule contributes the
true empty conjunction; if no matching nullary rule exists, the disjunction is
false. Thus the formula neither invents a run for a missing leaf transition nor
requires the automaton itself to be deterministic. Conversely, every accepting
run supplies the required partition. Reader lines 98--110 reproduce this
direction exactly from Lemma 3.3.6 at printed pp. 94--95.

### Finite-tree MSO bridge and closed sentences

A finite ranked tree has a finite prefix-closed position domain `D`, a partition
of `D` into symbol-label subsets, and arity conditions determining its children.
A label atom becomes membership in the corresponding label subset, and the
`i`-th-child atom becomes the successor equation `y=xi`. Restricting every
element quantifier to `D` and every monadic quantifier to subsets of `D` sends a
finite-tree MSO formula to WSkS. In the reverse construction, the state sets
partition that same `D`. Hence the surrounding infinite successor structure is
only the address space used to code a finite tree; it is not silently made the
automaton input. Reader lines 73--83 and 98--110 supply both sides needed by the
shared theorem, consistent with TATA printed pp. 89--95.

The reader also preserves TATA's warning that Theorem 3.3.7 is a convenient but
“not very precise” slogan and lets Lemmas 3.3.4 and 3.3.6 carry the exact two
directions. When there are no free tracks, the zero-fold product alphabet is
represented explicitly by the sole nullary constant `top`. There is only that
one ground input, so a closed sentence is true exactly when the constructed
automaton has `top -> q_f` for some final `q_f`. This handles the empty
free-variable alphabet without confusing it with an all-zero data track; see
reader lines 112--118 and TATA printed p. 95.

### Exercise 1.4

Assume a finite deterministic bottom-up automaton recognizes
`L={f(t,t):t in T(F)}` for `F={a^(0),f^(2)}`. Every ground term `t` must have a
run: otherwise the required term `f(t,t)` cannot have a run. If distinct terms
`t` and `u` reach the same state `q`, acceptance of `f(t,t)` supplies an
applicable transition `f(q,q) -> r` with final resulting state. The same rule
then gives `f(t,u)` the same root state, so it is accepted, although syntactic
freeness of the ground term algebra and `t != u` show that it is not of the form
`f(v,v)`. Hence distinct ground terms require distinct states. The sequence
`a`, `f(a,a)`, `f(f(a,a),f(a,a))`, and so on supplies infinitely many ground
terms, contradicting finiteness of the state set. The proof therefore remains
valid for a partial deterministic automaton and contains the previously easy
to miss reachability premise. It is correctly marked handbook-owned at reader
lines 120--129 and 154--160; TATA prints only the exercise at p. 43.

### Weak/full ranges, shared theorem, and source boundaries

Weak monadic quantification ranges over finite subsets. Full SkS permits every
subset, including infinite subsets, of the infinite successor tree. On an
actually finite position domain the two ranges coincide because every subset is
finite; on the infinite successor tree they do not. TATA accordingly points to
root-down automata over infinite inputs and a different complementation
argument for the full logic. Reader lines 131--139 and TATA printed pp. 95--96
state that boundary without converting a finite input into a Rabin input.

The shared theorem now types the weak and full ranges at their actual first use
at lines 879--898, and its finite-ranked-tree definition at lines 848--877
agrees with the reader on term formation, bottom-up runs, root acceptance, and
recognition. It also keeps the finite-tree construction explicitly distinct
from the S2S/Rabin theorem at lines 843--846. The shared source-role statement
at lines 30--33 gives Thatcher--Wright only abstract-level historical standing
and assigns the operative definitions, constructions, and theorem to the
inspected TATA release.

The reader's Thatcher--Wright paragraph at lines 141--152 and reconstruction
boundary at lines 154--161 do not infer a body-level signature, recognition
relation, weak logic, theorem, example, or proof from the unacquired article.
The acquisition note's owed artifact at lines 64--82 describes what must later
be established without naming a hypothetical mathematical answer, and RC-1713
remains only an acquisition lead. This preserves both proof ownership and the
historical/modern distinction.

## Mandatory invariant dispositions

- **T01 — PASS.** The eight title-page authors and their order, title, HAL
  custody, 2008 release footer, 2021 deposit-cover date, 263/262-page account,
  fixed-object hash, and evolving-work 2007 distinction agree. Evidence:
  reader lines 6--10; bibliography lines 5847--5853; detailed note lines 5--29
  and 157--159; compact record lines 694--698; TATA physical pp. 1--2 and
  printed pp. 11--13.
- **T02 — PASS.** Authorized HAL research access is not promoted to an open
  republication licence; the PDF/renders remain evidence rather than handbook
  assets. Evidence: detailed note lines 31--34 and TATA physical p. 1.
- **T03 — PASS.** The operative input is a finite ranked ground term, and the
  exclusion of infinite-tree automata is explicit. Evidence: reader lines
  6--10 and 131--139; shared lines 871--875 and 896--897; TATA printed
  pp. 11--13 and 95--96.
- **T04 — PASS.** Ranked arities, nullary/positive-arity recursion, finite
  ordered-tree standing, literal tuple order, and the source/handbook symbol
  map are exact. Evidence: reader lines 12--30; shared lines 848--865; TATA
  printed pp. 19--20.
- **T05 — PASS.** Rules, runs, nullary leaves, final-root acceptance, and
  recognizability are correctly typed. Evidence: reader lines 20--27; shared
  lines 859--870; TATA printed pp. 20--22.
- **T06 — PASS.** Determinism is target uniqueness per symbol/child-state
  tuple, the language is unchanged, and the constructed states are reachable
  subsets. Evidence: reader lines 39--41; compact record line 698; TATA printed
  pp. 23--27.
- **T07 — PASS.** Effective Boolean closure, accessible-state marking,
  final-marked nonemptiness, and the representation-qualified linear bound are
  exact. Evidence: reader lines 41--46; shared lines 890--895; TATA printed
  pp. 30 and 40.
- **T08 — PASS.** The `f(a,b)` run and missing-root-rule failure are correct,
  and ownership is handbook-only. Evidence: reader lines 32--37 and 154--160;
  source run semantics at TATA printed pp. 20--22.
- **T09 — PASS.** Word and finite-set ranges and all four restricted atoms are
  exact. Evidence: reader lines 49--60; TATA printed pp. 87--90.
- **T10 — PASS.** Product-symbol arities, all three coordinate meanings, every
  named Example 3.3.3 label, and nullary all-`bottom` padding agree with the
  source. Evidence: reader lines 62--71; TATA printed pp. 90--91.
- **T11 — PASS.** `D`, the symbol-label subsets, both atom translations, both
  quantifier restrictions, and the coding/input distinction are explicit.
  Evidence: reader lines 73--83; shared lines 879--889; TATA printed
  pp. 89--95.
- **T12 — PASS.** The inclusion automaton has the complete six-label list; the
  disjunction extension and union, negation complement, and existential
  projection are all present and correctly typed. Evidence: reader lines
  85--96; TATA printed pp. 91--93.
- **T13 — PASS.** One set per state, partition of exactly the finite encoded
  domain, final root, and the correctly directed local transition clause are
  present; the clause also handles arity zero. Evidence: reader lines 98--110;
  TATA printed pp. 94--95.
- **T14 — PASS.** The slogan qualification and exact two-lemma control are
  preserved, and the closed-sentence case uses empty tracks/the sole nullary
  `top`, not a zero track. Evidence: reader lines 112--118; TATA printed p. 95.
- **T15 — PASS.** The exact two-symbol ranked alphabet and copying language are
  retained; the handbook proof establishes subrun existence before the
  deterministic separation and is valid for partial tables. Evidence: reader
  lines 120--129 and 154--160; TATA printed p. 43.
- **T16 — PASS.** Finite-set WSkS, arbitrary-set full SkS, finite-domain
  coincidence, root-down infinite inputs, and the distinct complement argument
  are separated. Evidence: reader lines 131--139; shared lines 884--889;
  TATA printed pp. 95--96.
- **T17 — PASS.** The shared definition and theorem agree with the detailed
  presentation and expressly preserve the Rabin boundary. Evidence: shared
  lines 843--898; reader lines 12--139; TATA printed pp. 19--43 and 87--96.
- **T18 — PASS.** Operative construction, full-source proof, printed exercise,
  handbook example, and handbook proof have distinct and accurate ownership;
  no claim of reproducing every state table or proof is made. Evidence: reader
  lines 154--161; detailed note lines 161--176; TATA printed pp. 25--27, 30,
  40, 43, and 91--95.
- **T19 — PASS.** Thatcher--Wright remains abstract-level history, TATA is not
  substituted for its missing body, RC-1713 is only a lead, and the open owed
  artifact has no speculative name. Evidence: shared lines 30--33; reader lines
  141--152; acquisition note lines 27--48 and 64--82; compact record lines
  684--692; TATA printed p. 95 for TATA's `[TW68]` citation only.
- **T20 — PASS.** Bibliography, numbering, notation, page maps, attribution,
  proof ownership, and status agree across the frozen records. In particular,
  bibliography lines 2346--2367 separate the May 1996 report from the 1997
  chapter; Thomas-note lines 51--58 preserve the report's literal prospective
  *Handbook of Formal Language Theory* separately from the registered final
  *Handbook of Formal Languages*; and Thomas-note lines 79--92 and compact
  record lines 606--616 and 902--916 leave final-chapter reconciliation and
  independent precursor review open. Controlling Thomas evidence: physical
  pp. 1--4 and 75, especially the abstract on physical p. 2.
- **T21 — PASS.** The mathematical terms used in the reconstruction are defined
  and typed before reliance, have clear object/relation/property standing, and
  are used by the later constructions. The source boundaries have explicit
  metalinguistic standing. No redundant speculative name is assigned to the
  unacquired Thatcher--Wright construction; its note states an owed artifact.
  Evidence: reader lines 12--30, 49--60, 62--83, 131--152; acquisition note
  lines 64--82.
- **T22 — PASS.** The records distinguish acquired source, reconstruction,
  independent review, admission, and all broader completion states. The
  pre-review records correctly leave this review and admission open. Evidence:
  reader line 161; detailed note lines 178--185; compact record lines 694--706
  and 900--916. This verdict closes only the chartered `N-c-015.b`
  manuscript-content question on the nine listed hashes.

## Findings and conclusion

I found no blocker, must-fix, should-fix, consider, discard, or unresolved-user
finding. The finite ranked-term definitions, bottom-up run semantics,
determinization invariant, reachability/emptiness proof, WSkS encoding, both
formula/automaton directions, local transition clause, closed-sentence
reduction, Exercise 1.4 separation, finite-tree MSO bridge, weak/full boundary,
proof ownership, source-role distinctions, Thomas version correction,
cross-record status, terminology, and exact completion scope all survive the
required edge-case stress tests on the frozen Round 4 snapshot.

VERDICT: ACCEPT
