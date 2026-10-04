# Round 3 mathematical-and-proof review

## Independence and evidence declaration

I conducted this as a fresh blind Round 3 mathematical-and-proof review.  I
read the charter first and thereafter read only the five frozen Round 3
objects.  In particular, I read the actual frozen LaTeX directly, including
the complete semantic Safra subsubsection at lines 787--1038, and I read the
actual hash-pinned PostScript directly, page by page through all twenty
declared pages.  The PostScript page programs, not a render or derivative,
were the controlling source; direct text extraction was used only to navigate
that same object.  I did not inspect a manuscript PDF, PNG, derived source
PDF, test, checker, repository script, TeX command, build, ledger, chair text,
prior-round report, another Round 3 report, another board, memory, staging
material, or web result, and I did not contact another reviewer.

## Independently recomputed frozen identities

I independently recomputed both byte length and SHA-256 for every frozen
object.  All five results agree with the Round 3 table.

| Frozen object | Bytes | Independently recomputed SHA-256 | Result |
|---|---:|---|---|
| `tmp/pdfs/p09-safra-1988/DBA-author-hosted.ps` | 247,788 | `2D492FD28FBCC9FF85E5AA22A62A435D6CB6549DDC00EB5FE8DC7DD82DF6CCD8` | exact match |
| `handbook/parts/p09/presentations/n-c-013.tex` | 60,088 | `D8376280880E262F0D0FCE00C6FFBA229284428DB7BBDC7D43C707192C930E75` | exact match |
| `handbook/bib/handbook.bib` | 207,798 | `C085AB2ACA4DDBFF4FA7BBAAD7C01961007962424829C7537A93CFCA0F9201AC` | exact match |
| `spec/research/p09-safra-1988-source-note.md` | 17,866 | `BB9DB11D86A33F8A18BE1D8E5F175C76A2A7A015C36829F9F97EB652B8635F63` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | 239,351 | `75F59E5731805548ED37BD1CFC2DB555E1C8AB4C4D5D1BCF096343775DBC795D` | exact match |

## Independent mathematical reconstruction and stress test

The source automaton is the typed tuple
`(Sigma,Q,q0,delta,C)` with `delta:Q x Sigma -> P(Q)`.  Its use of a
set-valued transition permits an empty input successor set.  Its deterministic
target convention is stronger than mere partial single-valuedness: every
state-letter pair has exactly one successor.  The manuscript preserves both
facts at lines 804--834, before using runs, infinity sets, Büchi acceptance,
Muller families, or Rabin pairs.  Safra's Rabin order is also preserved: the
`L` component recurs and the `U` component is eventually absent (PostScript
pp. 2 and 4; manuscript lines 827--834).

For a live tree state, proper child-union containment gives every live node a
state not present in any child, while branch disjointness makes the deepest
node carrying that state unique.  With the manuscript's explicitly
handbook-owned inclusive-path correction, that state is specific to the node.
Thus, after duplicate pruning, empty deletion, and collapse, distinct live
nodes have distinct specific original states.  There can be at most `n` live
nodes.  This proves both the node bound and the sufficiency of the `n`-name
reservoir; it does not confuse names, node labels, or colors (PostScript pp.
9--11; manuscript lines 836--918).

The six update stages are type-correct and in the printed order.  Creation is
simultaneous over the nodes present after label advancement, so a newly made
child is not recursively processed again in the same creation stage.  Each
old node creates at most one temporary child, so the disjoint `n`-element
temporary reservoir suffices before pruning.  Horizontal pruning removes a
duplicate only from branches to the right and never from a shared ancestor.
Empty deletion then removes exactly the empty subtrees.  Collapse is evaluated
only for old nodes, preserves the collapsing node, and removes its descendants.
The surviving temporary nodes are finally assigned the least unused names in
the fixed ancestor-first/first-divergence traversal.  Temporary identities do
not affect the output, and the fixed final allocation makes the displayed
transition one function (PostScript pp. 10--11; manuscript lines 883--918).

The color chronology is also coherent.  A name assigned to a new temporary
node was absent during the coloring stage and is therefore red in its creation
state.  If that node survives, its name is not changed; it is white on an
ordinary later update and green precisely on a later collapse.  If it is
deleted, the name is red and may be reused only through another red creation
state.  Consequently, a name that is eventually never red denotes one
persistent lineage, exactly what both correctness directions require.

The only failure of the printed six-stage transition is the empty advanced
root.  That case is possible because input transitions may be empty.  The
handbook introduces the absorbing rejecting automaton state only after
identifying this necessity and expressly says that it is neither a tree node
nor a source component.  The tree-to-sink transition occurs exactly when no
original run extends the prefix; the sink loops on every letter.  After the
displayed definitions, it is placed in every `B_v` and no `G_v`.  It therefore
rejects every continuation, restores target totality, changes no accepted
word, adds only one state, and adds no Rabin pair (manuscript lines 920--946).

For soundness, after the chosen name's last red position, successive green
positions leave the same named node present.  At each green position its
descendants are cleared.  Before the next green collapse, equality with the
union of its child labels means that every endpoint state in the next green
label descends from a child created at an intervening Büchi visit.  Hence each
next-level state has a predecessor in the prior green label connected by a run
over the explicitly half-open factor `alpha[i_j,i_{j+1})` that visits `F`.
Giving each next-level state one such predecessor creates a rooted,
finitely-branching tree with a nonempty level at every height.  Koenig's lemma
selects a forward branch; its edge segments run from the earlier label to the
later label, so concatenation has the correct orientation and visits `F`
between every two successive green positions.  The result is one infinite
Buechi run, not a changing sequence of finite witnesses (PostScript pp. 11--12;
manuscript lines 965--982).

For completeness, an accepting original run remains represented at the root.
If the root is green infinitely often, its persistent root name is the Rabin
witness.  Otherwise, after the root's last green collapse, the run's next
visit to `F` places it below the root.  Propagation keeps it below that child
unless horizontal pruning transfers responsibility to a strictly older
sibling.  New siblings are youngest, so there are only finitely many such
leftward transfers; after settling, the child cannot be empty while it carries
the run and cannot be removed by a parent collapse after the parent's last
green event.  If that persistent child is not green infinitely often, the same
argument descends below it.  Proper label containment strictly decreases
labels down a branch and bounds simultaneous depth by `n`, so indefinite
descent is impossible.  Some persistent node is therefore green infinitely
often; its persistent name is red only finitely often (PostScript p. 12;
manuscript lines 984--993).

Finally, the shape count, the total label encoding, and the colors multiply to
`2^(O(n log n))`.  The manuscript correctly repairs the source's incomplete
`Q -> V` encoding: an absent original state maps to an external encoding value,
while a present state maps to its unique specific live node.  The value is not
a node or automaton component, and `(n+1)^n` preserves the asymptotic bound.
The absorbing state adds one state only.  The source's `n!` lower bound supports
optimality only up to a constant in the exponent.  Appendix A is only a sketch
and supports the sharper reading of Lemma 2 as requiring doubly exponentially
many members in a deterministic Muller acceptance family.  The three stated
corollaries retain their respective source and target classes and bounds
(PostScript pp. 12--18; manuscript lines 995--1029).

## Mandatory invariant dispositions

### S01 -- identity and version: satisfied

The recomputation above fixes the controlling PostScript at 247,788 bytes and
the stated hash.  Its literal header is `jcss.dvi`, records generation on 21
March 1995, and declares twenty pages.  PostScript p. 1 identifies `[Saf88]` as
the preliminary version; p. 19 identifies that item as FOCS 1988, pp. 319--327,
and prints the singular historical journal wording.  Manuscript lines 787--802
call this a twenty-page author-hosted expansion and do not call it the
nine-page proceedings file or a published article.

### S02 -- registered-work boundary: satisfied

Manuscript lines 788--802 confine DOI/proceedings pages and abstract-level
claims to the registered work and assign the detailed construction and
numbering only to the expanded manuscript.  The bibliography entries and both
research records keep that split.  The continuing proceedings-body gap remains
open and is not used to support expansion details.

### S03 -- custody and rights: satisfied

The detailed note records author/university hosting as research access, not an
open-content or republication licence, and states that the handbook uses
independent prose.  The manuscript claims neither facsimile nor journal
publication at lines 1031--1038.  No derived render is cited as evidence in the
semantic unit or records.

### S04 -- automaton, run, and infinity set: satisfied

Manuscript lines 804--827 type the tuple, set-valued transition, initial state,
run recurrence, infinity set, Buechi condition, and Muller family before use.
They preserve possible empty input transitions and the source's total,
single-valued deterministic convention (PostScript pp. 1--4).

### S05 -- Rabin and Streett pair order: satisfied

Manuscript lines 827--834 give Safra's `(L_i,U_i)` order with recurring/good
first and eventually-absent/bad second, matching PostScript pp. 2 and 4.  They
expressly bar exchange with Thomas's later convention.

### S06 -- tree-state standing: satisfied

Manuscript lines 836--875 give `T=(N,r,p,S)`, the `n`-element vocabulary,
parent and sibling order, label and total color maps, proper child-union
containment, branch disjointness, and the exact inclusive-path specificity
abbreviation.  Node identities come from `V`; labels and colors retain their
separate standings.  Both printed strict-ancestor defects are identified and
corrected without attributing the corrections to Safra (PostScript pp. 9--10).

### S07 -- initial representative: satisfied

The one-node `{q0}` label and all-white source coloring are stated at manuscript
lines 877--881, matching PostScript p. 10.  Choosing the least `v0` is expressly
handbook-owned and is used only to make the target initial state literal.

### S08 -- six-stage update: satisfied

Manuscript lines 883--907 give, in order, label advancement, simultaneous
youngest accepting-child creation, leftmost duplicate retention, empty-node
deletion, collapse/green plus white/red coloring, and fresh renaming.  The
objects and update order agree with PostScript pp. 10--11.

### S09 -- deterministic allocation and reservoir: satisfied

The corrected first-divergence order and the separate ancestor-first total
traversal appear at manuscript lines 841--851; least-unused allocation and its
handbook ownership appear at lines 904--917.  Specific states inject live nodes
into `Q`, proving at most `n` survivors.  Creation-state red, later persistence,
and collapse green agree with the source color map (PostScript pp. 10--11).

### S10 -- empty-root completion: satisfied

Manuscript lines 920--946 give the missing case, the absorbing state's exact
automaton-state standing, entry condition, self-loops, rejecting behavior,
membership in all displayed bad components and no good component, unchanged
language, and unchanged asymptotic bound.  Nothing attributes this repair to
the PostScript.

### S11 -- acceptance pairs: satisfied

The displayed definitions at manuscript lines 931--946 put tree states with a
green `v` in `G_v`, tree states with a red `v` and the sink in `B_v`, and the
sink in no `G_v`.  Eventual non-red plus infinite green is exactly Safra's Rabin
orientation and yields exactly one pair for each of the `n` vocabulary names
(PostScript p. 11).

### S12 -- soundness: satisfied

The half-open finite factor is defined before use at manuscript lines 965--966.
Lines 967--982 correctly pass from successive persistent green labels to
accepting finite segments, orient the predecessor edges from earlier to later
levels, apply Koenig's lemma to a finitely branching tree with arbitrarily deep
levels, and concatenate one Buechi-accepting run (PostScript pp. 11--12).

### S13 -- completeness: satisfied

Manuscript lines 984--993 track one accepting run at the root, use youngest
creation and strictly leftward duplicate transfers to obtain an eventually
stable child, repeat only when the current persistent node is not infinitely
green, and stop by strict containment/bounded depth.  The terminal node's name
persists and is the required Rabin witness (PostScript p. 12).

### S14 -- state count and optimality: satisfied

Manuscript lines 995--1012 give the source tree-shape bound, the
handbook-completed total typed label encoding with a non-node absence value,
the `3^n` color factor, `2^(O(n log n))` states, and exactly `n` pairs.  Theorem
1 is stated without class abbreviations.  The `n!` lower bound receives only
the justified constant-in-the-exponent qualification.  Lemma 2 is accurately
about Muller-family cardinality and remains an Appendix A sketch (PostScript
pp. 12--13 and 17--18).

### S15 -- applications: satisfied

Manuscript lines 1014--1029 preserve Corollary 4 as complementary deterministic
Rabin with `2^(O(n log n))` states and `n+1` pairs, Corollary 6 as complementary
nondeterministic Buechi with the same asymptotic state bound, and Corollary 7 as
equivalent Buechi deterministic in the limit with `O(3^n)` states.  The
accepting-run definition of determinism in the limit is exact and weaker than
full determinism.  The modal-logic sentence reports only the source's upper
bounds and does not inflate them (PostScript pp. 13--16).

### S16 -- cross-presentation and publication scope: satisfied

Manuscript lines 1031--1038 keep Safra's `n` persistent names and `n` pairs
separate from Thomas's `2n` names and `2n` pairs.  The LaTeX, two bibliography
entries, detailed note, and compact record agree on source ownership, repair
ownership, terminology, the open proceedings reconciliation, conditional
review status, and the complete lines 787--1038 admission boundary.  None
claims a render, build, whole topic, whole part, handbook, book, or publication
as admitted evidence.

## Round 2 refinement dispositions

1. **Singular historical journal wording: satisfied.**  PostScript p. 19
   literally prints *Journal of Computer and System Science*.  Manuscript
   lines 795--799, the bibliography note, and both research records preserve
   that wording and do not silently normalize it.
2. **Total target, possible empty input, and Muller family standing:
   satisfied.**  Manuscript lines 804--827 distinguish all three points before
   any family-size claim.  The sink repair at lines 920--946 then makes the
   constructed transition total.
3. **Both strict-ancestor corrections and deterministic traversal:
   satisfied.**  Manuscript lines 841--871 give the first-divergence and
   inclusive-path corrections; lines 847--851 separately define the
   ancestor-first traversal.  Both records state the same corrections and
   identify them as handbook-owned.
4. **Finite-factor endpoint convention: satisfied.**  Manuscript lines
   965--966 define `alpha[i,j)` as the letters at positions `i` through `j-1`
   before the soundness segments use it.
5. **Total label encoding, theorem statement, and Lemma 2 boundary:
   satisfied.**  Manuscript lines 995--1012 make the encoding a total map,
   keep the external value outside the tree and automaton, state Theorem 1 in
   full class names, and identify the Muller-family lower bound as only an
   Appendix A sketch.
6. **Deterministic in the limit: satisfied.**  Manuscript lines 1018--1025
   quantify over accepting runs and finitely many positions with more than one
   successor, while expressly distinguishing full determinism.
7. **Terminology and numbered-result inventory: satisfied.**  No undefined
   breakpoint terminology remains in the Safra semantic unit.  Across the
   complete source record the exact numbered inventory is Theorem 1; Lemmas 2,
   3, and 5; and Corollaries 4, 6, and 7 (PostScript pp. 9 and 13--17).  The
   manuscript reconstructs Theorem 1, Lemma 2, and the three corollaries it
   substantively invokes without renumbering or inventing a result.

## Round 3 refinement dispositions

1. **First-divergence and inclusive-path repairs in all three prose objects:
   satisfied.**  The LaTeX at lines 841--871, detailed note at lines 125--150,
   and compact record at line 600 each describe both defects exactly, give both
   corrected relations, and assign both corrections to the handbook.
2. **Traversal and allocation remain separately owned: satisfied.**  The
   ancestor-first/first-divergence traversal is introduced for enumeration;
   the fixed linear order and least-unused assignment separately resolve the
   source's “some unused name” instruction.  Together they determine one
   output state, while neither is attributed to Safra.
3. **Printed tuple before later repair: satisfied.**  Manuscript lines
   852--875 classify exactly the states printed by the source as `(T,l,c)` and
   do not mention or pre-classify an added state.  Only after lines 920--923
   prove necessity do lines 924--929 introduce the added automaton state and
   give its standing.
4. **Acceptance-set definition order: satisfied.**  The sink is not put into
   an informally named acceptance set before the displayed `G_v` and `B_v`
   definitions at lines 931--937.  Lines 938--945 then state notation,
   membership, semantics, and the exact pair count.
5. **Complete semantic admission unit: satisfied.**  The Safra heading is at
   line 787, its final paragraph ends at line 1038, and the Thomas heading is
   at line 1040.  The complete unit includes the source boundary, Theorem 1,
   Lemma 2, Corollaries 4, 6, and 7, the Safra/Thomas separation, and the
   non-facsimile/nonpublication boundary.  No earlier numerical endpoint was
   used in this review.

## Findings and seat-specific rationale

No blocker, must-fix, should-fix, consider, discard, or unresolved-user finding
arose.  The repaired reconstruction supplies a total deterministic target,
maintains the ordered-tree and name invariants under every update stage,
handles missing successors without changing the language, orients both proof
directions correctly, and preserves the exact asymptotic and application
claims at author-hosted expanded-manuscript strength.  This conclusion is
narrowly limited to the five frozen objects and the complete Safra semantic
unit at lines 787--1038.

VERDICT: ACCEPT
