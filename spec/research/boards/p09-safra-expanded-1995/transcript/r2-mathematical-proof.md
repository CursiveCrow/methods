# Round 2 mathematical-and-proof review: Safra expanded manuscript

## Scope, identity, and independence

I read the actual frozen `handbook/parts/p09/presentations/n-c-013.tex`
directly, including the complete Safra passage at lines 787--1034 (the charter's
substantive range ends at line 1031, while its closing sentence continues
through line 1034). I also read the actual frozen
`tmp/pdfs/p09-safra-1988/DBA-author-hosted.ps` directly: its native PostScript
header, all twenty native `%%Page` bodies, and its trailer. I did not substitute
a manuscript PDF, page image, or derived source document for either object.

I also read the two Safra bibliography entries in the actual frozen
`handbook/bib/handbook.bib`, the complete frozen
`spec/research/p09-safra-1988-source-note.md`, and the `N-c-013.d` and
consolidated-status passages in the actual frozen
`spec/research/p09-source-presentations-lot2-3.md`. I did not inspect a PDF,
PNG, derived source PDF, test, checker, repository script, TeX command, build,
ledger, chair text, Round 1 report, another Round 2 report, another board,
memory, staging material, conversation history, or web result, and I did not
contact another reviewer.

I independently recomputed the byte count and SHA-256 identity of every Round 2
object before the substantive review:

| Frozen object | Recomputed bytes | Recomputed SHA-256 | Identity disposition |
|---|---:|---|---|
| `tmp/pdfs/p09-safra-1988/DBA-author-hosted.ps` | 247,788 | `2D492FD28FBCC9FF85E5AA22A62A435D6CB6549DDC00EB5FE8DC7DD82DF6CCD8` | exact match |
| `handbook/parts/p09/presentations/n-c-013.tex` | 59,650 | `4DF89F9A17BC8CE2EF8D1F66C8990BD088BB1AB8BAD1219C926407FB3F9900F8` | exact match |
| `handbook/bib/handbook.bib` | 207,798 | `C085AB2ACA4DDBFF4FA7BBAAD7C01961007962424829C7537A93CFCA0F9201AC` | exact match |
| `spec/research/p09-safra-1988-source-note.md` | 17,649 | `40EAAF3B885CD7AB3DFAD3B2536FE3EB9EEC77077C3BB5849204E0EB598B92A5` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | 238,878 | `4BC69269B9E61BFCE47975F5BA097361F4A844EA3507B321FBFBB8F222DA0D6F` | exact match |

## Finding

### MP-R2-01 — must-fix — the first-divergence order is a necessary but silently owned correction

**Exact manuscript location:** `n-c-013.tex` lines 841--847, especially the
first-divergence definition at lines 841--843. The nearby defect disclosure at
lines 858--867 owns only the correction to the specificity clause. Lines
905--907 own the deterministic allocation choice, but they do not own the
underlying correction to the source's left-to-right relation.

**Exact source location:** native PostScript p. 9. The source first defines
`d_1` to be an ancestor of `d_2` only when `p^k(d_2)=d_1` for some `k>0`, so
ancestor is strict. On that same page it says that two non-ancestral nodes are
left-to-right when some ancestor of one is an older brother of some ancestor of
the other. Native p. 11 then relies on this left relation in update step 3.

**Concrete falsification:** let `x` and `y` be distinct sibling nodes with `x`
older than `y`. They are non-ancestral. Under the source's printed strict
ancestor definition, neither `x` nor `y` is its own ancestor. Their proper
ancestors coincide, beginning with their common parent, so no proper ancestor
of `x` is an older brother of a proper ancestor of `y`. The printed clause
therefore declares neither sibling left of the other. The same failure occurs
when one or both endpoints are themselves first-divergence children. This is a
separate strict-ancestor inconsistency from the p. 10 specificity clause.

The handbook's rule at lines 841--843 is the mathematically correct repair: use
the first distinct children on the inclusive root paths and compare those
children by their sibling order. Together with the ancestor-first extension at
lines 843--847, it yields the total traversal needed at lines 900--902. But the
passage presents the first-divergence rule as if it merely restated the source.
The detailed record repeats that silent correction at
`p09-safra-1988-source-note.md` lines 125--130 while expressly owning only the
specificity correction at lines 140--148. The compact record does the same at
`p09-source-presentations-lot2-3.md` line 600, and line 604 consequently
overstates that the strict-ancestor ownership defect has been repaired.

This is mathematically operative, not cosmetic. Without the correction, update
step 3 does not determine the leftmost survivor when a duplicated original
state occurs in sibling branches. The handbook's deterministic name-allocation
traversal also cannot be justified from the printed relation. The actual
handbook construction works because it already uses the corrected relation;
the defect is the missing source/repair ownership boundary. Under the charter,
a silent correction is at least a must-fix.

**Required repair:** at lines 841--847, state directly that Safra's strict
ancestor convention also makes the printed left/right clause fail for siblings,
and that the handbook therefore replaces that clause by the displayed
first-divergence rule. Preserve the existing exact definition and the separate
ancestor-first traversal extension. Make the same ownership statement in the
detailed note and compact `N-c-013.d` record, and remove or revise the repaired-
status assertion at compact-record line 604 until the same frozen snapshot
contains all three changes. No additional primitive, tree component, or new
technical name is needed.

## Independent reconstruction and stress tests

Except for MP-R2-01's ownership defect, the displayed construction and proofs
survive the mathematical stress tests required by the charter.

1. **Types, partial input, and total target.** The input transition has type
   `Q x Sigma -> P(Q)` and can return the empty set. A run is correctly indexed
   from `q_0`, and Büchi, Muller, and Safra-order Rabin acceptance are defined
   from the infinity set. The target convention `|delta(q,a)|=1` is both total
   and single-valued. If root advancement is empty, child labels are also empty
   by containment, and printed step 4 removes the root. The handbook-owned
   `bot_dead` state is therefore reached exactly when no input run extends the
   prefix. Its all-letter loop, membership in every bad set, and absence from
   every good set make it rejecting and total; adding one state changes neither
   the language nor the asymptotic state bound.

2. **Tree invariant and simultaneous creation.** Proper child-union
   containment implies each child label is a proper subset of its parent's
   label. Branch disjointness separates non-ancestral responsibility. After
   label advancement, one new youngest child is simultaneously created for
   each current node whose new label meets `F`; there are at most `n` current
   nodes, so the temporary `n`-name set suffices. Temporary identity does not
   affect the final state because surviving temporary nodes are subsequently
   enumerated by tree position and renamed.

3. **Duplicate paths and empty labels.** The handbook's first-divergence rule
   gives a unique leftmost branch, so horizontal deletion retains an original
   state on that branch and removes it from all branches to its right. Common
   ancestors remain labelled, as they should. If an internal label is empty,
   every descendant label is empty by containment, so deleting all empty nodes
   preserves a rooted tree whenever the root itself remains nonempty.

4. **Collapse and colors.** Collapse is tested only after duplicate and empty-
   label deletion. An old node whose label is covered by its children survives,
   loses its descendants, and is green. Other surviving old names are white;
   old names not retained are red. Nested collapse does not change the labels
   of surviving ancestors or their immediate surviving child labels, so it
   creates no order-dependent acceptance event. New nodes are excluded from
   the old-node collapse test. Because unused vocabulary elements were colored
   red before final renaming, a newly allocated name is red in its creation
   state. A later surviving node keeps that name and is white except when its
   own collapse makes it green.

5. **Name reservoir.** Under the corrected inclusive specificity relation,
   proper child-union containment gives every nonempty node a state that lies
   in that node but in none of its children. Descendant containment and branch
   disjointness make that original state specific to exactly that node. Thus
   distinct live nodes have distinct specific original states, so at most `n`
   nodes survive. If `k` old nodes and `t` temporary nodes survive, then
   `k+t<=n`; hence at least `n-k>=t` vocabulary names are unused. The fixed
   order on `V` and corrected total traversal therefore make final allocation
   one function.

6. **Acceptance orientation.** For each vocabulary name, `G_v` is precisely
   the green-state set and `B_v` precisely the red-state set plus the rejecting
   sink. The Rabin condition is eventually no `B_v` and infinitely many
   `G_v`, matching Safra's `(L_v,U_v)` order with the recurring/good component
   first. There are exactly `n` pairs. Nothing exchanges this order with the
   later Thomas presentation.

7. **Soundness.** If `v` is eventually never red and is green at
   `i_1<i_2<...`, it is present throughout the tail. The manuscript defines
   the consumed factor exactly as `alpha[i,j)=alpha(i)...alpha(j-1)`. Between
   consecutive green events, the child created from an `F`-intersection and
   later absorbed at collapse supplies, for every endpoint in `S_{j+1}`, a
   predecessor in `S_j` and a finite run segment consuming exactly
   `alpha[i_j,i_{j+1})`, beginning at that predecessor and ending at that
   endpoint, with an `F` visit. Taking `S_0={q_0}` also covers a name created
   after the initial state, because every live label remains root-reachable and
   creation itself records an `F` visit. Give each next-level vertex one such
   predecessor and one witnessing segment. The resulting tree is rooted,
   infinite, and finitely branching (each level has at most `n` vertices), so
   Koenig's lemma gives an infinite branch. Consecutive segments agree at their
   selected endpoints; their concatenation is one input run, not a sequence of
   unrelated runs, and its infinitely many disjoint factors yield infinitely
   many `F` visits.

8. **Completeness.** Fix an accepting input run `rho`. Its state after every
   prefix lies in the root label, so the root persists. If the root is green
   infinitely often, its persistent name witnesses acceptance. Otherwise, on
   the next `F` visit after its last green event, `rho` is represented in a
   child. Horizontal merging can transfer responsibility only to an older
   sibling. There are finitely many older siblings, while every later-created
   child is youngest, so such transfers cannot occur infinitely often. Once
   responsibility settles in a child, that child cannot be deleted as empty;
   its parent no longer collapses. If it is not itself green infinitely often,
   the same argument applies after its last green event. Along a child chain,
   nonempty labels strictly decrease, so no current chain has more than `n`
   nodes. The nested persistent descent must stop at a node green infinitely
   often. Its creation-state red event is finite and the node thereafter
   persists, giving the required Rabin witness.

9. **State count and lower-bound strength.** For a fixed ordered tree, every
   original state present in some live label has a unique deepest/specific
   node; a state absent from all live labels needs a distinct encoding outcome.
   The handbook's total map `f:Q -> N union {star}` is therefore sufficient to
   reconstruct every label, and `star` is correctly excluded from the tree and
   automaton data. There are at most `(n+1)^n` maps and `3^n` colorings. With
   the source's `2^(n log n+O(n))` tree-shape count and the one sink, this remains
   `2^(O(n log n))`. Theorem 1 is stated without the source's class
   abbreviations and retains exactly `n` Rabin pairs. Native p. 13 gives only a
   modified-Michel `n!` lower-bound observation and qualifies optimality as up
   to a constant in the exponent. Native pp. 17--18 label the Lemma 2 argument
   a sketch; it specifically forces doubly exponentially many members in a
   deterministic Muller acceptance family. The manuscript preserves both
   limitations.

10. **Applications.** Native pp. 13--15 support the exact result sequence
    Theorem 1; Lemmas 2, 3, and 5; Corollaries 4, 6, and 7. Corollary 4 targets a
    complementary deterministic Rabin automaton with
    `2^(O(n log n))` states and `n+1` pairs. Corollary 6 targets a complementary
    nondeterministic Buchi automaton with the same asymptotic state bound.
    Immediately before Corollary 7, native p. 15 defines deterministic in the
    limit by quantifying over accepting runs and allowing only finitely many
    positions having more than one available successor. This is not full
    determinism, and the `O(3^n)` Corollary 7 target is correctly kept as a
    different partial determinization. Native p. 16 supports the stated
    exponential and doubly exponential modal-logic upper-bound consequences;
    the manuscript does not turn them into stronger lower bounds or proceedings
    claims.

## Mandatory invariant dispositions

- **S01 — PASS.** The independently measured source is exactly 247,788 bytes
  with the frozen hash. Its header says `jcss.dvi`, 21 March 1995, and twenty
  pages. Native p. 1 identifies `[Saf88]` as preliminary; native p. 19 identifies
  that item as FOCS 1988. The manuscript, bibliography, and both research
  records preserve the source's singular historical wording *Journal of
  Computer and System Science* and do not call the expansion a published JCSS
  article or the nine-page proceedings file.

- **S02 — PASS.** The DOI, pp. 319--327, and abstract-level proceedings claims
  remain separate from detailed expanded-manuscript content and numbering. The
  proceedings body remains expressly open.

- **S03 — PASS.** The detailed note distinguishes research access from an
  open-content or republication licence, and the manuscript is independent
  prose. No render or derived document is made evidence.

- **S04 — PASS.** The tuple, finite types, initial state, set-valued transition,
  run recurrence, infinity set, and Buchi condition precede use. Empty input
  successors remain possible. Safra's target determinism is correctly total
  and single-valued. Muller acceptance is infinity-set membership in a family
  of subsets before Lemma 2 discusses that family's cardinality.

- **S05 — PASS.** Safra's `(L_i,U_i)` order is recurring/good first and
  eventually absent/bad second, and it is expressly separated from Thomas's
  later convention.

- **S06 — FAIL (MP-R2-01).** The tuple, maps, color standing, label invariants,
  inclusive specificity correction, and node/label/color distinctions are
  mathematically correct. The separate first-divergence correction forced by
  the same printed strict-ancestor convention is not explicitly handbook-owned.

- **S07 — PASS.** The source's one-node `{q_0}` initial tree and all-white color
  map are present. Choosing the least `v_0` under the already fixed order is
  expressly handbook-owned and only makes the deterministic state literal.

- **S08 — PASS.** The six stages occur in source order with the correct old,
  temporary, label, node, and color standings. Child creation is simultaneous;
  duplicate deletion precedes empty deletion, which precedes collapse and
  coloring, which precedes renaming.

- **S09 — FAIL (MP-R2-01).** The `n`-node argument, reservoir inequality,
  creation-state red color, persistent-name behavior, and least-free final
  allocation are correct once the displayed first-divergence relation is used.
  But that operative correction is not owned, so the account does not yet give
  a fully honest source/handbook derivation of the one transition function.

- **S10 — PASS.** The absorbing rejecting state has exact automaton-state
  standing, all-letter transition, membership in every bad component and no
  good component, rejecting language effect, and constant bound effect. It is
  expressly not attributed to Safra.

- **S11 — PASS.** Every vocabulary name supplies one green/good and one
  red-or-sink/bad set; eventual-red/infinite-green orientation is correct and
  yields exactly `n` pairs.

- **S12 — PASS.** The finite factor has an exact half-open endpoint convention
  before use. The label-to-label predecessor assertion, finite branching,
  Koenig branch, endpoint-compatible concatenation, and infinitely many Buchi
  visits have the right directions and quantifiers.

- **S13 — PASS.** Root representation, finite movement to older siblings,
  eventual stable-child responsibility, proper-containment depth bound,
  persistent name, and the final infinitely-green witness form a valid
  completeness argument.

- **S14 — PASS.** Tree shapes, the total typed `Q -> N union {star}` encoding,
  the non-node status of `star`, colors, sink, `2^(O(n log n))` states, exactly
  `n` pairs, the `n!` qualifier, Theorem 1's expanded class names, Muller-family
  cardinality, and Appendix A sketch status are all correct.

- **S15 — PASS.** Corollaries 4, 6, and 7 preserve their source and target
  classes, bounds, and pair count. Deterministic in the limit is defined by the
  accepting-run condition and distinguished from full determinism. The modal-
  logic consequences are not inflated.

- **S16 — FAIL (MP-R2-01).** The five files otherwise preserve the expanded-
  manuscript/proceedings boundary, singular journal wording, exact result
  sequence, Safra's `n` names and pairs versus Thomas's `2n`, rights boundary,
  open proceedings reconciliation, conditional review status, and narrow
  admission scope; no unnecessary undefined Safra-breakpoint term remains.
  They do not agree on honest repair ownership because all three substantive
  prose objects silently use the corrected first-divergence relation, while the
  compact record claims the strict-ancestor ownership defect has been repaired.

## Seat-specific rationale

The determinization itself is mathematically correct in the repaired form
actually displayed: the dead-root completion is language preserving, the
specific-node encoding completion gives the claimed asymptotic bound, the
Rabin orientation and exact pair count are right, and the soundness and
completeness arguments survive adversarial reconstruction. MP-R2-01 is
nevertheless a mandatory rejection because a relation used by horizontal
duplicate deletion and deterministic allocation is not the relation literally
defined by the source. The handbook supplies the right correction but silently
assigns it source standing. One explicit ownership sentence in each substantive
record is sufficient; no mathematical redesign is required.

VERDICT: REJECT -- MP-R2-01
