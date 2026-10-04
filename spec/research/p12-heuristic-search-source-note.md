# Heuristic search source and authoring record

## Final authoring standing: ready for integration

Recorded 9 September 2026, 18:50 UTC. The entire selected treatment for
`ED26-P12-PRACT-002` is authored. Components C01–C05 include the exact search
objects and procedures, least-cost and termination guarantees, computational
comparisons, generalized best-first development, and worked relaxation and
failure cases. The author read the actual body and annex LaTeX in full and
completed the generalized and saturated-search notation intake. No selected
authoring component or source-acquisition blocker remains. The root owns
routing, the authoring projection and canonical bibliography/symbol merges.

The current files contain **29 reciprocal statement/proof pairs**, **29 full
proof environments** and **72 symbol rows**. Direct identity and reference
checks found zero unpaired statements, unpaired annex items, duplicate labels,
unresolved local references, missing symbol first-use anchors, missing symbol
scope anchors, or empty symbol fields. The body contains no proof environment.
Both citations use the sole bibliography intake key
`DechterPearl1985BestFirst`. These are authoring and intake checks; no independent
review, test suite, manuscript build or render has been run for this handoff.

The exact selected source remains Dechter–Pearl (1985), §§1–4 including the
actual concluding §4.4, and the relevant Appendix B cases. The printed article
has no numbered §5. Appendix A's random-tree probability claim remains outside
the selected scope. The source SHA-256 remains
`261A75AD83CC3BEEDB438E9058DE215F2840D21BE55897A5C898CDE7EBB11487`.
The treatment preserves the original targets and explicitly distinguishes
proved corrections and strengthened procedures from reproduction of historical
claims. The full Figure 9 matrix is not imported as an unchanged theorem.

### Frozen authoring files

| File | Extent | SHA-256 |
| --- | --- | --- |
| `handbook/parts/p12/heuristic-search.tex` | 796 lines | `EF6D5B7B86E1A347254F9B4123DD055F8277A007F2C1B2D6717112E0DBE85076` |
| `handbook/annex/p12/heuristic-search.tex` | 1153 lines | `E4D279FA9D0BA2499CAB22DE22D0F3807D47930471E4D27D63B8DC637F209269` |
| `handbook/registry/symbols-intake-p12-heuristic-search.csv` | 72 data rows | `BADEA8C972D16B9B743A255EB0D465B42B1BBF1434BD08651B87E09841974457` |
| `handbook/bib/intake-p12-heuristic-search.bib` | One entry, `DechterPearl1985BestFirst` | `BBB28F6E58A65A41FFDEF8F96B78503DC41BD4E0BE4E73BF5CF2DFD754B3C2BA` |

The actual body path is `handbook/parts/p12/heuristic-search.tex`, whose chapter
label is `sec:p12-best-first-search-and-heuristic-guarantees`. The corresponding
annex path is `handbook/annex/p12/heuristic-search.tex`, whose chapter label is
`annex:p12-heuristic-search`. These actual paths supersede the provisional
filename for this unit only through the root's authoring projection.

### Complete statement/proof inventory

Every suffix below identifies a body statement `thm:p12-hsearch-SUFFIX` and its
full reciprocal proof `annex:p12.hsearch-SUFFIX`.

| Number | Suffix | Treatment |
| --- | --- | --- |
| 1 | `consistency-bound` | Consistency, admissibility and monotone prefix scores |
| 2 | `frontier` | Maintained optimal-path frontier witness |
| 3 | `finite` | Finite nonnegative-cost graph termination |
| 4 | `optimal` | Least-cost goal selection |
| 5 | `infinite` | Solvable locally finite graphs with a positive uniform edge bound |
| 6 | `no-reopen` | Consistency and final expanded labels |
| 7 | `relaxation` | Edge-preserving relaxation lower bound |
| 8 | `sure-set` | Strict-contour expansion and nonpathological equality |
| 9 | `consistent-efficiency` | Consistent equal-information expansion forcing |
| 10 | `tradeoff` | Nonpathological information trade |
| 11 | `cost-compatibility` | Explicitly stronger costwise comparison class |
| 12 | `pathmax` | Admissibility of the specified persistent-record A** |
| 13 | `pathmax-containment` | Matched ties and strict-containment example |
| 14 | `bestfirst-forcing` | Normalized path-only competitor forcing |
| 15 | `two-input-score` | Necessary restriction on two-input scores |
| 16 | `weak-compatibility` | Counterexample to forcing under the original weak premise |
| 17 | `pending-domination` | Strict uniform domination of the stated pending-update procedure |
| 18 | `saturated-invariant` | Revealed-edge closure and barrier invariant for A-dagger |
| 19 | `saturated-type-three` | Type 3 comparison for the explicitly strengthened procedure |
| 20 | `no-type-two` | No type 2 optimum under the declared comparison quantifiers |
| 21 | `positive-type-three` | Strictly positive-cost extension with the stated tie premise |
| 22 | `general-barrier` | Generalized path barriers and the post-root threshold |
| 23 | `general-complete` | Generalized completeness from bounded-prefix finiteness |
| 24 | `general-closure` | Exact generated-path labels after a relaxation fixed point |
| 25 | `weighted` | Weighted and nonlinear sufficient conditions and bounds |
| 26 | `returned-path` | Necessary and sufficient branch-barrier implications |
| 27 | `tree-criterion` | Exact ordered-tree criterion under pure leftmost ties |
| 28 | `no-type-zero` | No universal expansion containment in the specified classes |
| 29 | `positive-domain-extension` | Applicable comparison arguments on the source's positive-cost domain |

### Original source targets and their authored disposition

| Source target | Current treatment and exact qualification |
| --- | --- |
| Definitions and A* properties in §§1–2 | Explicit path records, successor revelation, duplicates, reopening, stale entries, tie rules and goal selection; pairs 1–7 give full basic proofs with finite and infinite hypotheses separated. |
| General BF* Lemma 1 | Pair 24 states the exact relaxation-fixed-point premise. A generated-edge counterexample shows why merely revealing edges does not complete label propagation. |
| Minmax Lemmas 2–4, Theorems 1–5 and Corollary 1 | Pairs 22–25 provide barriers, completeness, full-root versus effective post-root threshold, and weighted/nonlinear consequences. The compulsory-root boundary is retained explicitly. |
| Theorem 6 | Pair 26 gives the returned-path branch implications using operational frontier inequalities and complete start-rooted path records. |
| Lemma 5 and Theorem 7 | Pair 27 proves the ordered-tree criterion in both directions, using the source's half-open strict-ancestor interval and pure leftmost ties. Goal-first ties have a separate counterexample. |
| Theorems 8–9 and Corollary 2 | Pairs 8–10 give strict-contour forcing, consistent-domain comparison and the nonpathological information trade with full hypotheses. |
| Theorem 10 and Corollaries 3–4 | Pair 17 proves an actual counterexample for the chapter's specified pending-update A** model. Pairs 18–21 prove the repaired invariant and type 3/no-type 2 comparisons for the separately named fully saturated A-dagger procedure, including positive-cost flat groups. They do not assert that the historical procedure already performs full revealed-edge closure. |
| Theorem 11 and Corollaries 5–6 under weak global compatibility | Pair 16 supplies a proved hybrid-competitor counterexample to the original weak forcing claim in the declared model. Pair 11 proves a separate stronger costwise theorem; it does not discharge or reproduce the weaker-premise historical claim. Competitor-dependent tie choices are written explicitly. |
| Lemma 6, Theorem 12 and Corollary 7 | Pairs 14–15 give normalized path-only forcing and two-input restrictions; pair 29 supplies the strictly positive terminal-edge adjustments and states the proper score domain. |
| Appendix B cases | Pairs 12–13 give A** admissibility, matched-tie containment and a strict-containment case with persistent witnesses and g-based duplicate improvements. The source's broader comparative claims retain the distinct corrected treatment above. |
| §4.4 conclusion | The reader receives the proved relaxation certificate, precise comparison distinctions and limitations of empirical heuristic claims. No nonexistent §5 is fabricated. |
| Appendix A | Random-tree probability theorem unselected and unclaimed. |

The selected source has therefore been treated with its original claims
identified, proved where the exact hypotheses support them, and corrected by
explicit counterexamples and separately stated results where required. This
standing is authoring completion, not independent mathematical acceptance.

### Corrections and model boundaries retained in the final text

The four computational comparisons retain their actual quantifiers. A tie
policy selected for a particular competitor is not one policy simultaneously
contained in every competitor's expansion set. Equal-cost two-branch examples
prove the distinction. Distinct-state expansion sets and repeated expansion
operations remain separate quantities.

The weak-compatibility counterexample uses the fully observed root lists
`s->a:3,s->b:1,s->c:1`, `b->a:1`, `c->t:10` and heuristic values
`h(s)=h(t)=0,h(a)=1,h(b)=20,h(c)=9`. A* never expands b; any A* return through
a can be shortened by replacing its cost-3 prefix with the revealed cost-2
prefix. A hybrid competitor recognizes this finite pattern and returns the
known cost 11, falling back to uniform-cost search otherwise. Thus it is
optimal whenever A* is optimal but can omit the strictly forced state a.
This proves failure of the weak forcing assertion rather than merely
identifying a gap in one proof strategy.

The pending-update counterexample fixes legal goals-first, fresh-before-reopened
ties and uses `s->w:3,s->x:5,s->z:1,s->k:1,w->j:2,x->j:1,z->x:1,j->t:7`,
with k a dead end and `h(s)=h(j)=h(t)=0,h(w)=7,h(x)=5,h(z)=h(k)=9`.
After j is expanded on its old cost-5 record, the revealed graph already has
a cost-10 solution, while the pending procedure still expands k before
propagating that solution. A wrapper following exactly the same query prefix
can return when its exact revealed-graph solution cost meets the minimum OPEN
barrier. The frontier certificate proves it correct on the entire stated
class, so the saving is strict uniform domination. The rejected non-parent
edge x->j makes the witness survive current-pointer-tree propagation.

A-dagger saturates all revealed edges after each strict improvement before
another state query. The resulting invariant controls every exposed alternative
path. Its positive-cost theorem additionally gives priority to minimum-barrier
states with g below that barrier, then handles the finite flat group with
g equal to the barrier as a group. The proof preserves prior observations,
uses a strictly positive fresh goal edge, and includes outside-group
interleavings. These extra rules are explicit strengthened-procedure premises.

The generalized threshold excludes the compulsory initial selection. The
source's full-root minmax is retained as `max(initial score,effective threshold)`.
A root-score counterexample explains why it cannot force all below-root-score
states. Generalized graph search requires continuation-safe score order and
reopening; generalized tree search retains path records. Completeness requires
bounded-prefix finiteness or the stated pathwise growth condition. Positive
edge costs alone do not force an arbitrary generalized score to grow.

The original Figure 6(b) scan displays direct `s->J1:1`, `s->J2:1`,
`J2->J1:1`, `J2->goal:10`, with `h(J1)=1,h(J2)=10`. Those displayed values
alone, under the chapter's `h(s)=0`, imply a lower bound of 10 through J1,
not 11. A hidden J1 goal edge of cost 9 exhibits the difference. The valid
proper-subset example in this chapter instead has direct `s->a:3`, making
the cheapest known prefix to a cost 2 through b and the bound `2+9=11`.
The body example `def:p12-hsearch-subset-cost-boundary` explicitly proves
that changing the direct edge back to 1 invalidates that pruning certificate.
An additional exact root estimate of 11 would be a different premise and
certificate. The chapter does not silently reproduce the displayed source
numbers as if they proved the altered bound. Its information-trade example
also uses `h(c)=9`, whereas source Figure 6(a) displays 6; both are explicitly
specified examples, not claimed literal figure reproductions.

Pair 29 extends the applicable finite-run comparisons to solvable locally
finite graphs with strictly positive uniformly bounded-below edge costs.
It uses positive perturbations when a terminal zero edge would leave that
domain, and restricts the positive-domain two-input statement to `x>0,y>=0`.
No numerical lower bound common to every instance is supplied as extra
oracle information. The no-universal-containment example for admissible and
normalized path-only classes uses strictly positive edges. The analogous
costwise-class conclusion in pair 28 remains explicitly scoped to the finite
nonnegative domain of its zero-terminal-edge construction.

### Symbol scope inventory for root integration

All 72 rows use the following 18 existing anchors. The scope bindings are
intended as stated here; this author has not edited shared scope bindings.

| Scope | Rows | Intended body or annex region |
| --- | --- | --- |
| `sec:p12-best-first-search-and-heuristic-guarantees` | 31 | Entire body chapter |
| `sec:p12-hsearch-cost-closure` | 6 | Body section on global guarantees and propagation of known costs, through the saturated and positive-cost comparisons |
| `sec:p12-hsearch-generalized` | 6 | Body generalized-best-first section through the returned-path result, ending before the ordered-tree section |
| `sec:p12-hsearch-ordered-tree` | 5 | Body ordered-tree section and its local criterion/tie boundary |
| `def:p12-hsearch-algorithm` | 1 | A* procedure's local tentative scalar q |
| `def:p12-hsearch-relaxation` | 2 | Relaxation definition's unary relaxed goal distance and heuristic |
| `thm:p12-hsearch-returned-path` | 1 | Returned-path statement's local suffix barrier |
| `thm:p12-hsearch-weighted` | 5 | Weighted/nonlinear theorem and its p, epsilon, beta, w and phi roles |
| `annex:p12-heuristic-search` | 2 | Entire annex chapter's exposed-graph and distance roles |
| `annex:p12.hsearch-bestfirst-forcing` | 2 | Complete best-first-forcing proof item, local Q and Q_b |
| `annex:p12.hsearch-consistent-efficiency` | 1 | Complete consistent-efficiency proof item, positive edge slack |
| `annex:p12.hsearch-cost-compatibility` | 1 | Complete cost-compatibility proof item, positive perturbation |
| `annex:p12.hsearch-infinite` | 1 | Complete infinite-graph proof item, fixed-path bound |
| `annex:p12.hsearch-pending-domination` | 1 | Complete pending-domination proof item, known solution cost |
| `annex:p12.hsearch-positive-domain-extension` | 1 | Complete positive-domain-extension proof item, domain-preserving perturbation |
| `annex:p12.hsearch-positive-type-three` | 3 | Complete positive-type-three proof item, flat group and two positive perturbations |
| `annex:p12.hsearch-tradeoff` | 2 | Complete tradeoff proof item, scalar distance bound and perturbation |
| `annex:p12.hsearch-weighted` | 1 | Complete weighted proof item, local inverse function |

The intake distinguishes scalar tentative `q` from path score `q(P)`, unary
relaxed distance `d_R(x)` from binary revealed-graph distance `d_R(u,v)`,
expanded-set D from the trade proof's scalar D, and the local inverse function
r from subtree-root and right-side-bound uses. The optimum `C*` is interpreted
under the currently declared cost functional, which may be nonadditive in
the generalized section. All scope and first-use anchors resolve to the owned
body or annex. There are 57 body-scoped and 15 annex-scoped rows.

## Historical authoring checkpoints

Everything below records earlier source reading and intermediate authoring
states. The incomplete standings and continuation lists below are superseded
by the final 29-pair, 72-row handoff above; they are retained as provenance.

### Second authoring block, 9 September 2026, 18:16 UTC (superseded)

The next block added the generalized best-first minmax, completeness,
fixed-point, returned-path branch and exact ordered-tree developments, with
their proofs, and the weighted/nonlinear score examples. It also added a
proved negative result for the original weak global-compatibility premise,
so the stronger costwise theorem is not being counted as its discharge.

There is now a concrete strict-uniform-domination counterexample for the
chapter's pending-reopening A** procedure. A wrapper follows the same queries
and stops early only when an exact solution in the revealed graph meets the
minimum OPEN barrier. The seven-state witness shows a proper saving. It
survives pointer-tree descendant updates because the improved route uses an
already revealed non-parent edge. This is a proved failure for that explicit
operational model, not just the failure of the published proof strategy.

The new, separately named A-dagger procedure fully relaxes every revealed
edge before selecting a new state. Its cost-closure/barrier invariant checks
all revealed alternative paths, and supplies a complete first-divergence
proof of type3 and the no-type2 conclusion on finite nonnegative graphs.
The positive-cost version supplies the missing zero-residual case separately:
ties first prefer g below the common barrier; a finite flat group with
g equal to the barrier is handled as a group before the comparison advances.
The construction uses a small strictly positive goal edge, preserves the
other group lists and leaves outside frontiers terminal. These proofs are
explicit corrections/qualified replacements, not claims that the historical
pending-update procedure already performs full closure.

The generalized expansion threshold excludes the forced root selection;
the full source minmax is retained as max(initial score, effective threshold).
An explicit root-score counterexample explains the needed distinction.
The ordered-tree theorem uses pure leftmost ties, including goals, and side
subtrees branching at strict ancestors. Goal-first ties have a separate
counterexample. Original embedded scan strips were decoded losslessly to PNG
for source reading: the source really states c >= delta > 0 on p.508, and the
tree formula on p.518 uses the half-open root-to-node interval. These are
source-image reads, not manuscript renders. Figure6's source graph strips
were also inspected; the numerical examples in the chapter remain explicitly
independent examples rather than literal redraws.

The prior mathematical continuation list below is superseded by these added
proof drafts. The unit remains unrouted. Before calling authoring complete,
finish one full author read-through of the new actual LaTeX, update the symbol
intake for the newly introduced generalized/saturated notation, and check the
new reciprocal identities. No independent review, build, manuscript render
or prose-test run has occurred. The next continuation starts with those final
authoring tasks, not another source search or a review wave.

Date: 9 September 2026. Unit: `ED26-P12-PRACT-002`.
Authoring ownership: `handbook/parts/p12/heuristic-search.tex`, matching annex,
and the bibliography/symbol intakes carrying the `p12-heuristic-search` slug.
The root owns all drivers and canonical records. Other writers' files and the
older SRC-036/SRC-057 search presentations were preserved.

## Source acquired and read

Dechter and Pearl, *Generalized Best-First Search Strategies and the Optimality
of A\**, Journal of the ACM 32(3), July 1985, 505–536,
DOI [10.1145/3828.3830](https://doi.org/10.1145/3828.3830).
The complete free [author-hosted PDF](https://ics.uci.edu/~dechter/publications/r0.pdf)
was downloaded to `tmp/pdfs/p12-heuristic-search/dechter-pearl-1985.pdf`.

- Bytes: 2,542,517.
- SHA-256: `261a75ad83cc3beedb438e9058de215f2840d21be55897a5c898cde7ebb11487`.
- Actual pages: 32, printed 505–536.
- No encryption, form or embedded JavaScript was reported by PDF metadata.
- The PDF's 1999 scan creation/modification dates are not publication dates.

All 32 pages were extracted for source reading, with separate per-page text
files, and the entire selected main text and Appendix B were read. Appendix A
was encountered and kept outside the selected probability-result scope. The
paper ends its main discussion at §4.4 on pp.531–533; it has no numbered §5.
The allocation's reference to section5 therefore cannot identify a nonexistent
section. The relevant conclusion is the actual §4.4 discussion.

The read-only PDF and research skills supported primary-source reading and this
durable note. No manuscript PDF was created, built or rendered. The web source
figure-screenshot route failed. Original embedded scan strips were extracted as
source evidence, but were not used to claim a completed visual comparison of
the original figures. The worked numerical graphs in the new chapter are
independently specified mathematical examples, not purported facsimiles of
Figures6 or10.

## First-block authored material (historical, superseded)

The body and annex contain **15 reciprocal statement/proof pairs**, covering:

1. consistency implies admissibility and nondecreasing prefix scores;
2. the maintained frontier witness;
3. finite-graph termination with nonnegative costs, including zero-cost cycles;
4. least-cost return at goal selection;
5. locally finite solvable infinite graphs with a positive uniform edge bound;
6. no reopening under consistency;
7. an edge-preserving relaxation certificate;
8. strict-contour expansion and equality on nonpathological instances;
9. the consistent equal-information expansion lower bound and its tie qualification;
10. the nonpathological expansion trade and absence of a single uniformly best algorithm;
11. an explicitly stronger costwise-compatible competitor theorem;
12. admissibility of the precisely specified persistent-record A** procedure;
13. both matched-tie containment and a strict-containment A** case;
14. normalized path-only best-first competitor forcing and boundary choices;
15. the restriction on two-input scores with normalized goal values.

Every stated proved result has an ordinary proof inside its reciprocal
`annexitem`. The author read the actual written LaTeX; the final simple
identity check found15 statements,15 annex items,15 proof environments and
zero unpaired statement/proof identities. This is authoring evidence, not
independent acceptance. No prose test suite, independent review or build ran.

The procedures explicitly define graph states versus path records, successor
revelation, finite heuristic values, normalized goal estimates, persistent
cost witnesses, strict duplicate improvement, reopening, stale heap entries,
goal-prioritized ties, and the distinction between distinct-state expansion
sets and repeated expansion operations. The efficiency oracle does not reveal
the entire graph, its size or a complete goal list in advance.

## Mathematical calculations made during authoring

| Case | Correct conclusion |
| --- | --- |
| Allocated four-edge trace | A* returns4; the unused branch has score11 |
| Same graph with h(a)=20 | A* returns11 instead of4 |
| Goal accepted on generation | Direct cost10 can hide the two-edge optimum2 |
| Admissible inconsistent estimate | Reopening changes the returned cost from5 to4 |
| Geometrically shrinking positive edge costs | An infinite chain stays below1 and starves a goal of cost2 |
| Infinite unsolvable unit-cost chain | OPEN need never empty |
| Nonpathological information trade | A* expands a and skips b; a sound competitor expands b and skips a |
| Pathological information trade | Competitor expansion set is a proper subset of A*'s |
| Inherited barrier and goal preference | A** skips a dead-end state that A* must inspect, both returning10 |
| Incorrect barrier-based duplicate pruning | Rejecting a better g-label because its barrier is larger returns12 instead of10 |

The relaxation used for the allocated trace is explicit: add a zero-cost
edge from s to the goal while retaining the original edges. Its exact relaxed
distances are h(s)=0,h(a)=2,h(b)=10,h(t)=0. This supplies a complete lower-bound
derivation instead of calling selected useful scores a relaxation without proof.

## Source interpretation and corrections kept outside the reader's derivation

### Tie quantifiers

The prose definitions on p.521 must be expanded into explicit quantifiers.
The actual proof of Corollary6 on p.529 chooses a tie rule depending on the
competitor's returned optimal path. It does not produce one tie rule whose
expansion set is contained in all competitors' sets simultaneously.

Two equal-cost branches with perfect estimates demonstrate the distinction:
one competitor expands the left branch, another the right, and no successful
run can have an expansion set contained in both. Further, a goal-preferring
policy may first inspect a tied dead-end sibling before following a solution
branch; a different policy can omit that sibling. A competitor-dependent
type1 condition therefore cannot imply a type2 condition simultaneously
quantified over every bad tie policy merely by rearranging the paper's prose.
The chapter states four explicit comparison tests and does not assert that
these differently quantified relations form an automatic hierarchy.

### Persistent witnesses and graph relaxation

The frontier proof uses accepted labels and immutable path records. It does
not assume that merely generating every edge of a cheaper graph path has
already propagated its improvement through every descendant. Such propagation
is required before a shortest-distance statement about an exposed graph can
be used. The nonpathological trade proof explicitly proves the needed final
relaxation closure before using shortest distances in the exposed graph.

The A** procedure ranks by the maximum prefix g+h value but retains duplicates
by strict g improvement. A better g record can have a larger barrier. Replacing
the record replaces both values; taking the lesser barrier or keeping only a
barrier-minimal duplicate is a different procedure. The chapter's cost12 versus
cost10 example exhibits the failure of that substitution.

### Weak global compatibility versus costwise compatibility

The source describes global compatibility as returning an optimum whenever
A* returns an optimum. Its Theorem11 proof appends a cheap goal to an unexpanded
state and obtains a smaller A* return value, then treats that return as an
optimum of the modified graph. On a graph with a different cheaper route to
that state, the smaller return value alone does not justify that assertion.

The active chapter proves a distinct, explicitly stronger **costwise
compatibility** theorem: B must return a path no more expensive than every
A* tie policy on all finite solvable instances, including inadmissible advice.
Its proof needs only the smaller returned value and makes no claim that A* is
optimal on the modified instance. This is not attributed as the exact unchanged
weak premise of the historical theorem.

A concrete reason the distinction matters is the following finite pattern.
Let the root's complete successor list be s->a:3,s->b:1,s->c:1;
b's complete list is b->a:1; c's complete list is c->t:10, with t a goal.
Use h(s)=0,h(a)=1,h(b)=20,h(c)=9,h(t)=0. Keep a's outgoing list unknown.
A* never expands b, because the fixed path through c keeps a frontier score
at most11, while b has score21. Any new goal reached through a by A* has a
prefix costing3; replacing that prefix with s,b,a lowers its true cost by1.
Thus an A* return through the unknown a-region cannot be globally optimal.
If A* is globally optimal on a completion of this observed pattern, its
return must instead have the known cost11.

A comparison algorithm may inspect b and c, recognize this exact pattern,
and return11 without inspecting a; on all other observations it can fall
back to uniform-cost search. It satisfies the weak implication that it is
optimal whenever A* is optimal. On the original admissible instance with a
a dead end, however, it skips a although A* must expand a. This is why the
stronger active theorem does not silently stand in for the historical weak
class. The mathematical argument is retained here for continuation and later
independent assessment; it is not a reader-facing instruction to repair an
earlier statement.

### Other explicit qualifications

The source's informal remark that human-created admissible heuristics are
usually consistent is not promoted to an empirical theorem. The proved
relaxation result states the actual goal/edge simulation hypotheses.
Finite nonnegative-cost termination and infinite positive-uniform-bound
termination have separate proofs. Positive edge costs alone do not suffice
on an infinite graph. The source's random-tree probability assertion from
Appendix A is not selected or claimed.

## First-block component standing and continuation (historical, superseded)

C01, C02, C03 and C05 have substantive drafts with the stated proofs and
worked boundaries. C04 has the four comparison distinctions, consistent-domain
containment, the nonpathological trade, proper-subset counterexample, A** B1/B2
cases, and the restricted normalized path-score results. **The entire unit
remains partly authored against the broad dispatch scope.** Do not mark a
complete transcription of source §§1–4 or the entire Figure9 matrix from
these15 results.

The next authoring block must finish the precise standing of the historical
weak globally-compatible class and its corrected comparative treatment, and
reconstruct or correct the general type3/A** and no-type2 claims in source
Theorem10 and Corollaries3–4. The published proof's first-divergence construction
needs explicit treatment of already revealed alternative paths and duplicate
label propagation before it can be asserted for the specified graph algorithm.
Generalized BF* minmax results and the full left/right tree criterion of §§2–3
have been read but are not reconstructed in this body. If those full source
presentations are required by the broad section allocation, they remain writing
work; they have not been retired by the narrower proofs supplied here.

Drivers, canonical bibliography and canonical symbol registry are untouched.
The body/annex pair is not routed by this author. A subsequent integration
decision must retain these open source-scope and mathematical items. All
independent review, build, output inspection and admission follow the completed
writing/correction batch.
