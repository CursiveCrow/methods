# Thomas 1996 report precursor and 1997 chapter boundary

## Current source standing

The registered `N-c-013.e` and `N-c-014.e` authority is Wolfgang Thomas,
“Languages, Automata, and Logic,” in *Handbook of Formal Languages*, volume 3
(Springer, 1997), pp. 389--455, DOI
<https://doi.org/10.1007/978-3-642-59126-6_7>. The author publication list
independently records that final chapter as `[Tho97d]` with the same title,
volume, pages, publisher, and year:
<https://www.lics.rwth-aachen.de/cms/lics/der-lehrstuhl/team/dozierende/wolfgang-thomas/~okhh/publikationen/?lidx=1>.

The locally acquired body is not a verified facsimile of that chapter. It is a
complete earlier report by the same author and with the same title:

- Wolfgang Thomas, *Languages, Automata, and Logic*;
- Bericht 9607, Institut für Informatik und Praktische Mathematik der
  Christian-Albrechts-Universität zu Kiel;
- May 1996.

The report is therefore usable only at explicit precursor strength until its
text is reconciled against the registered 1997 chapter.

## Local custody and identity

The controlling local source object is:

- path: `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf`;
- public route:
  <https://www.cs.cornell.edu/courses/cs6860/2019sp/Handouts/thomas.pdf>;
- byte length: 478,293;
- SHA-256:
  `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA`;
- physical extent: 75 PDF pages.

The physical page map is direct and complete: physical page 1 is the report
title page, physical page 2 is the abstract, physical page 3 is the contents
page numbered `i`, physical page 4 is printed page 1, and physical page 75 is
printed page 72. The title, author, May 1996 date, report number, institution,
abstract, contents, first numbered page, and final numbered page were read in
the controlling PDF itself; no derivative controls any identity or page claim.

An alternate EPFL-hosted file is also preserved at
`tmp/pdfs/p09-thomas-1997/thomas-1997-epfl.pdf`, 584,885 bytes, SHA-256
`D700728FC5D5C282FDF7D23BCD7614F8720A276C5032D5D2F435A1CF1842132C`.
It is not the controlling object, and no byte-level or page-by-page equivalence
with the Cornell file is asserted.

## Relevant-page source-reading record

The following report pages control the two manuscript presentations and were
read from the controlling PDF itself:

- Section 3.1, printed pp. 8--12, physical PDF pages 11--15;
- Section 5.1, printed pp. 28--30, physical pages 31--33;
- Section 5.2, printed pp. 31--36, physical pages 34--39;
- Section 5.3, printed pp. 37--42, physical pages 40--45;
- the Chapter 6 introduction, printed p. 43, physical page 46; and
- Sections 6.1--6.3, printed pp. 44--61, physical pages 47--64. Section 6.1
  ends and Section 6.2 begins on printed p. 47; Section 6.3 begins on printed
  p. 57.

Initial acquisition created disposable page images. They are retired, are not
source or manuscript review objects, carry no independent evidentiary weight,
and are not handbook or publication assets. Review reads the actual frozen
LaTeX and consults the controlling historical-source PDF itself at the exact
pages required; it does not inspect those images.

## Printed version evidence

The report itself fixes the version boundary. Its title page says “May 1996”
and “Bericht 9607.” Its abstract says that Sections 5 and 6 contain material
from February 1996 lectures and that a modified version of the paper would
become a chapter of the *Handbook of Formal Language Theory*. That prospective
title is the report's literal wording; the eventual registered chapter appeared
in the differently titled *Handbook of Formal Languages*. The acquired object
therefore predates, and expressly anticipates modification for, that 1997
publication.

The report contents give the section locators used by the manuscript:

- Section 3.1, “MSO-Logic on Words”;
- Sections 5.1--5.3, the infinite-word automata presentation; and
- Sections 6.1--6.3, automata and MSO logic on infinite trees.

Those locators may be attributed to the 1996 report. They must not be described
as locators read in the final 1997 chapter unless that chapter body is later
acquired, read, and reconciled.

## Mathematical reconstruction controlled by the report

### Section 3.1: finite words

The source's nondeterministic finite-word automaton has the data
`(Q,A,q0,Delta,F)`, with a transition relation contained in `Q x A x Q`. On a
word of length `n`, a run has `n+1` states, starts at `q0`, follows one
transition per letter, and accepts when its last state lies in `F`. Theorem 3.1
states the effective equivalence between finite-automaton recognizability and
`MSO[S]` definability.

For automaton-to-formula translation, pairwise disjoint monadic tracks encode
the run states through the last input position, while the transition on the
last letter is checked separately against `F`. The report expressly observes
that the displayed formula is satisfied by the empty word when all tracks are
empty, so an existence clause is needed when the automaton rejects the empty
word. For formula-to-automaton translation, the source uses the singleton-set
presentation `MSO0`, supplies atomic automata for subset, singleton, successor,
and letter-predicate forms, and interprets negation, disjunction, and
existential set quantification by complement, union, and bit-track projection.
The same construction decides `WS1S` by successful-run existence for an
input-free finite automaton. Reversed binary encodings and a finite carry set
give the recorded Presburger reduction.

### Sections 5.1--5.3: infinite words

Definition 5.1 uses a finite omega-automaton `(Q,A,q0,Delta,Acc)` and the set
`In(r)` of states occurring infinitely often in a run. Its four acceptance
modes are distinct source objects:

- Buchi: `In(r)` meets a designated set `F`;
- Muller: `In(r)` belongs to a designated family of subsets of `Q`;
- Rabin: for some pair `(Ei,Fi)`, `In(r) intersect Ei` is empty and
  `In(r) intersect Fi` is nonempty; and
- Streett, in Thomas's pair ordering: for every pair `(Ei,Fi)`,
  `In(r) intersect Ei` is nonempty or `In(r) intersect Fi` is empty,
  equivalently recurrence of an `Fi` state requires recurrence of an `Ei`
  state.

For a deterministic automaton, the source replaces the transition relation by
the total function `delta: Q x A -> Q`, so every input has a unique run with
`r(i+1)=delta(r(i),alpha(i))`. This totality premise, not merely an
at-most-one-successor condition, is what makes deterministic Muller
complementation valid by replacing the designated family `F` with
`P(Q) \ F`.

Example 5.2 realizes “if `a` occurs infinitely often, then `b` does” in all
four modes. Proposition 5.3 proves that their nondeterministic versions
recognize the same omega-language class. The source also records the exact
characterization that such a language is a finite union of sets
`U V^omega`, where `U` and `V` are regular finite-word languages. In the
reader, `V^omega` means an infinite sequence of `V`-factors whose concatenated
lengths are unbounded; equivalently, epsilon factors may be deleted. This
prevents a nominally infinite factor sequence from denoting a finite word.

Deterministic Buchi automata are not closed under complement; the report uses
the language with infinitely many `a` occurrences as its separating example.
Theorem 5.4 states McNaughton's effective conversion to deterministic Muller
acceptance and proves it by Safra's construction. A reachable-state subset is
insufficient because successive accepting states need not lie on one infinite
run. Put `n=|Q|`. In the reader's exact reconstruction, a `Safra tree` is the
tuple `(T,l,nu,M)`: `T` is a finite rooted ordered tree with live-node set
`N(T)`; `l:N(T)->P(Q)` is the macrostate label; `nu:N(T)->{1,...,2n}` is
injective; and `M` is the subset of currently marked live nodes. It is a
determinized word-automaton state, not an input tree or original run. Its name
map is distinct from the changing macrostate labels and the current-update
marks and is required later to identify one persistent lineage in the Rabin
pairs. More exactly:

- its nodes carry `Q`-macrostates;
- sibling labels are disjoint, and their union is a proper subset of the
  parent label;
- the initial tree is the single root `{q0}`, named `1` and unmarked; choosing
  `1` is a handbook-owned normalization, since another single initial name
  differs only by renaming;
- marks are successor-state records of collapses in the current letter update;
  the reader clears predecessor marks before the next update, a handbook-owned
  clarification needed to prevent one old breakpoint from persisting forever;
- the update first creates youngest `R intersect F` children, then advances
  every macrostate over the current input letter, then performs horizontal
  duplicate deletion followed by vertical collapse and marking;
- if advancement makes the root empty, the reader uses one empty, unmarked,
  absorbing determinization state with no node or name instead of deleting the
  root; this handbook-owned completion preserves rejection because no original
  run extends the prefix, adds no Rabin pair, and leaves the asymptotic bound
  unchanged;
- surviving node names persist, while all nodes created in one update receive
  pairwise distinct names, each absent from the entire predecessor name set;
  explicit injectivity and same-update distinctness are handbook-owned
  definedness clauses making the source's named-node encoding literal; and
- at most `n` nodes are live for an `n`-state input automaton, while names
  `1,...,2n` suffice.

The Muller condition detects a name that is eventually permanent and marked
infinitely often. Equivalently, for the injective name map `nu`, the Rabin pair
for name `k` has as its excluding set the states with `k` outside `im(nu)` and
as its recurring set the states having a currently marked node `v` with
`nu(v)=k`. The absorbing empty state is in every
excluding component and no marked-presence component, so it rejects. Clearing
old marks is proof-critical: on the rejected word `a b^omega` for the chain
`q0 -a-> f -b-> s -b-> s` with Buchi set `{f}`, the root has one breakpoint;
a persistent mark would falsely accept, while current-update marking does not.
Proposition 5.6 gives `2^{O(n log n)}` determinization states and
`2n` pairs in the displayed construction. Theorem 5.7 rules out a general
`2^{O(n)}`-state, `O(n)`-pair conversion, using Theorem 5.8's factorial Buchi
complementation lower-bound family. This is a later proof of the McNaughton
result, not evidence for the unread 1966 or 1988 original bodies.

Theorem 5.9 gives the effective Buchi/MSO equivalence on omega-words.
Corollary 5.10 reduces `S1S` truth to existence of a successful run of an
input-free Buchi automaton. Proposition 5.11 writes the result explicitly as a
finite disjunction of an eventually permanent absence
test and an infinitely recurring presence test, with every inner quantifier
bounded below the current position. Corollary 5.12 concludes that every MSO
formula over omega-words is equivalent to one in weak MSO.

### Sections 6.1--6.3: infinite trees

The Chapter 6 introduction says that its first two sections give a fairly
self-contained game-theoretic proof drawing on work later than Rabin 1969. The
report is therefore not used as evidence for Rabin's original complementation
or emptiness proof.

Definition 6.1 has a Muller tree automaton `(Q,A,q0,Delta,F)`, with
`Delta` contained in `Q x A x Q x Q`. A run labels the full binary tree by
states, starts in `q0`, and obeys one four-place transition at every node. It is
successful when every path has its infinitely recurring state set in `F`; an
input tree is accepted when there exists such a global run. The resulting
quantifier structure is existence of one run followed by the requirement on
all paths. Examples 6.2 and 6.3 give complementary tree languages and prove
that Buchi tree automata are strictly weaker than Muller tree automata.

Definition 6.4 replaces an arbitrary Muller family by a strictly increasing
chain `E1 subset F1 subset ... subset En subset Fn`. A path accepts when, for
some `k`, every `Ek` state occurs only finitely often and some `Fk` state occurs
infinitely often; the source also gives the successive odd/even priority
reading. Theorem 6.5 converts Muller to chain acceptance. Its “order-vector
with hit” is exactly
a permutation of the finite state set together with the prior position from
which the newly visited state was moved. It is finite memory attached to the
automaton state, not an input tree or run. Remark 6.6 explains how eventual hit
positions recover the infinitely recurring state set.

Section 6.2 forms the game in which Automaton chooses a transition and
Pathfinder chooses a branch. Remark 6.7 identifies automaton acceptance with a
winning strategy for Automaton. Theorem 6.8 gives memoryless determinacy for
the chain condition, where a memoryless strategy depends only on the current
game position rather than the earlier play. Definition 6.1 permits a partial
transition relation, but the abstract game theorem requires nonempty finite
outdegree. Before using the game, the reader therefore adds a fresh state
`bottom` outside every chain set, sends each missing state/letter case to
`(bottom,bottom)`, and loops `bottom` on every letter. Every original run
remains. Any run using an added transition has a path eventually constant at
`bottom`, which meets no accepting `F_i`; hence no successful run uses an added
transition. This handbook-owned completion preserves the strict chain and the
recognized tree language while making every game position live. Theorem 6.9
then constructs a complement automaton:
Pathfinder's local instruction at a node is a function from an input
letter/transition pair to a direction; a finitely labelled tree records all
local instructions; closure under negation and projection produces a
sequential deterministic Muller automaton that checks all transition sequences
consistent with those instructions along one path; a deterministic Muller tree
automaton performs the universal check over paths; and nondeterminism guesses
the instruction labels.
The constructed automaton depends on the source automaton, not on the
particular input tree. Theorem 6.13 proves the determinacy result by induction
by collecting positions from which one player can force a finite visit to a
target set and recursing on the induced complementary subgame. Theorem 6.16
makes winning regions and memoryless strategies effective for finite games.

Definition 6.17 calls an input tree regular when it is generated by a
deterministic finite word automaton over the two directions, equipped with an
output map. Theorem 6.18 removes the input by guessing labels and solves the
resulting finite game; the reader applies the same completion before that game.
A memoryless winning strategy fixes a finite
deterministic generator, proving both effective emptiness and the existence of
a regular member in every nonempty recognized tree language.

Section 6.3 works in the full binary successor structure. Theorem 6.19 builds
a Muller tree automaton from an MSO formula by atomic cases, disjunction,
existential projection, and the complementation theorem after the same
language-preserving completion. In the reverse
direction, existential state tracks encode a run and a universal path set
enforces its acceptance, giving the stated `Sigma^1_2` form. For a sentence,
the forward construction is input-free; the reader completes it before
Theorem 6.18 decides whether it has a successful run, and Theorem 6.20 concludes
that `S2S` is decidable. The regular
tree conclusion is then used for the report's regular-model consequence for
translated modal and branching-time logics.

## Source gaps and handbook-owned corrections

Corollary 5.10's printed proof says that a successful input-free Buchi run
exists exactly when some state is reachable from the initial state and lies on
a nonempty cycle. As printed, that condition omits the Buchi acceptance set and
accepts any reachable cycle. The sound finite criterion is: a reachable
nonempty cycle must contain a state in `F` (equivalently, a reachable cyclic
strongly connected component must meet `F`). The corollary's decidability
conclusion is unaffected.

**Direct manuscript update, 2026-09-06.** The live N13 paragraph now states
the accepting-state positive-return criterion and its proof directly; the
erroneous historical reading is retained in this source note. Printed p. 38
(physical PDF page 41) was read back from the held report for this edit.
The criterion requires a reachable `q in F` and a positive-length path
from `q` to itself. The reaching path may be empty. An accepting run
repeats some accepting state infinitely often, giving the required
paths; repeating a positive return after a reaching prefix gives the
converse. The paragraph also records finite reachability decidability
and excludes an isolated accepting state without a positive return.

The printed Safra update does not state what happens when the advanced root is
empty and does not explicitly clear an earlier breakpoint mark. The reader's
empty absorbing determinization state and current-update-only marks fill those
two definedness requirements without attributing them to the report.

The report names nodes, preserves surviving names, allocates names outside the
predecessor tree to new nodes, and later represents trees by functions on those
names, but it does not separately spell out injectivity or same-update
distinctness. The reader states those two requirements as handbook-owned
definedness clauses. They prevent newly created siblings from sharing one name
and make persistence, the `1,...,2n` reservoir, and the sets `E_k,F_k`
unambiguous. By contrast, the total deterministic transition function is
stated by the report itself and is restored as a source premise rather than a
handbook correction.

Definition 6.1 permits partial tree-automaton transitions, while Definition
6.10 requires every game vertex to have a nonempty finite outgoing-edge set.
The rejecting-state completion above supplies and proves the missing premise
before Remarks and Theorems 6.7--6.9, the finite-game use, the regular-tree
basis argument, and the `S2S` route.

## Rights and use boundary

The Cornell file is publicly readable from a university course route. No
Creative Commons licence or blanket republication permission was observed in
the report. The PDF is research evidence. Any derived page images are only
disposable viewer aids, carry no independent evidentiary weight, and are not
handbook assets.

## Manuscript disposition

Exact section claims based on the acquired file must cite a separate
`Thomas1996Report` bibliography entry. The `Thomas1997` entry remains the
registered final-publication identity and is not evidence that the final
chapter wording, numbering, corrections, examples, or proofs were read.

The 1996 report now supports bounded precursor reconstructions of `N-c-013.e`
and `N-c-014.e`. Their exact definitions, constructions, numbered results,
proof architecture, source gaps, and ownership boundaries have been inserted
in the reader. Blind Round 1 rejected the first snapshot for the omitted
finite-union theorem, two underspecified Safra-update cases, a partial-transition
gap in the game proof, and one premature technical name. Those passages are now
repaired. Blind Round 2 accepted source fidelity but rejected the snapshot for
two further manuscript-definedness omissions: the deterministic Muller
complement step lacked the source's total-transition premise, and the Safra
state lacked an injective live-node naming component. Both passages and the
records were repaired. Three fresh Round 3 seats then independently accepted
one unchanged seven-object snapshot with no finding. The exact hashes, reports,
and three-round history are preserved in
`p09-thomas-1996-report-independent-review-record.md`. This admits only the
May 1996 report-precursor manuscript content proposed for `N-c-013.e` and
`N-c-014.e`; no presentation file overall or broader manuscript unit is
admitted.

A later visit must acquire the registered 1997 chapter, compare every relied-on
definition, theorem, example, proof, section locator, and pagination claim,
record all modifications, and decide whether the precursor reconstructions
survive unchanged. Neither precursor acquisition nor later synthesis closes an
unread original source such as McNaughton 1966 or Safra 1988, and neither
substitutes for or reopens the separately admitted Rabin 1969 reconstruction.

No test, test harness, automated checker, repository script, TeX command,
interim handbook build, handbook-PDF inspection, or build was used.
