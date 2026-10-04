# Biere 1999: specialized finite bounds and complete supplied proofs

## Scope and source standing

Research date: 2026-09-06. The current Biere subsection of `handbook/parts/p09/presentations/n-c-017.tex` was read in full before this investigation. It already contains the no-loop and selected-loop LTL translations, their satisfiability correspondence, corrected recurrence diameter, safety and state-predicate persistence bounds, and an ordinary-Buchi-product bound. This note does not duplicate those proofs unnecessarily. No manuscript, build, render, software test, or other research file was changed.

Primary source: [Biere, Cimatti, Clarke, and Zhu, *Symbolic Model Checking without BDDs*, CMU-CS-99-101, 4 January 1999](https://www.cs.cmu.edu/~emc/15-820A/reading/biere99symbolic.pdf). This is the nineteen-page report, not a silently substituted TACAS edition. Section 4 is on physical PDF pages 11-13; Section 5 is on physical pages 13-15. Use definition/theorem numbers as the principal locators.

Three kinds of content are deliberately separated below:

1. Source definitions and statements actually present in the report.
2. Independently supplied complete proofs and precise sufficient constants for its lasso and F/G-fragment results.
3. An explicitly identified handbook ECTL certificate construction. The report does not print its bounded ECTL semantics, so this construction is not attributed to the report as a recovered definition.

## 1. What the report actually supplies

Sections 3-4 define bounded **LTL path** semantics and its SAT encoding (Definitions 4-6, 10-15; Theorem 16). Section 5.1 describes ECTL syntactically by existential quantification before every temporal operator, but explicitly defers its bounded ECTL semantics and translation elsewhere. Theorems 18 and 23 assert state-count and recurrence-diameter ECTL bounds without printing those definitions or proofs here.

Section 5.2 states a linear-size bound for the F/G-only fragment without an explicit constant. Definition 26 uses uniformly bounded stem and period lengths for every initial path; Theorem 27 gives the sufficient bound u+v. These are source statements, not additional printed proof passages. [Report, Section 5](https://www.cs.cmu.edu/~emc/15-820A/reading/biere99symbolic.pdf#page=13).

The report's fixed-loop convention is exact: a prefix `s_0,...,s_k` together with `T(s_k,s_l)`, `0 <= l <= k`, represents

\[
s_0\cdots s_{l-1}(s_l\cdots s_k)^\omega.
\]

It contains k unfolded transitions and one separately checked closing transition. The loop has `k-l+1` states and the stem has l states. For that selected lasso, temporal truth is ordinary infinite-path LTL truth. [Definitions 4-5, 12-15](https://www.cs.cmu.edu/~emc/15-820A/reading/biere99symbolic.pdf#page=8).

## 2. Standing notation for the supplied arguments

Let `M=(S,I,T,L)` have finite nonempty S, initial set `I subseteq S`, total `T subseteq S x S`, and `L:S -> 2^AP`, with AP finite. Write `N=|S|` and `d=recdiam(S,T)` in the manuscript's corrected convention: d is the largest number of edges in a simple directed path. Thus `0 <= d <= N-1`.

An LTL formula in this note has grammar

\[
h ::= \top\mid\bot\mid p\mid\neg p\mid h\land h\mid h\lor h
\mid Xh\mid Fh\mid Gh\mid h\,U\,h\mid h\,R\,h.
\]

Only atoms are negated. Ordinary path semantics uses infinite paths. Until requires a right-operand witness with the left operand before it; release means either the right operand holds forever, or a left-operand witness occurs with the right operand holding through that witness. The existing selected-loop translation implements these semantics exactly, including nested operators and the closing-edge successor.

Every state vector in a symbolic formula is constrained to S if S is not literally the whole Boolean cube. Empty conjunctions are true; empty disjunctions are false. A finite word's length below is its **number of states**, not its number of transitions.

## 3. A fixed selected-loop formula

For fixed `k >= 0` and `0 <= l <= k`, define

\[
\begin{split}
D_{k,l}(h)={}&I(s_0)
\land\bigwedge_{i=0}^{k-1}T(s_i,s_{i+1})\\
&\land T(s_k,s_l)
\land {}_l\llbracket h\rrbracket_k^0.
\end{split}
\]

Then `D_(k,l)(h)` is satisfiable exactly when an initial `(k,l)`-lasso satisfies h. A satisfying assignment supplies its finite representation and closing edge; induction on the selected-loop translation supplies its LTL truth. Conversely, an initial lasso supplies the state assignment and the same induction supplies the temporal conjunct. No simplicity or minimal-period condition is needed.

At `k=l=0`, the transition conjunct is `T(s_0,s_0)`. This is an infinite self-loop, not a zero-transition finite execution. Next returns to position 0. Arbitrarily nested next operators remain meaningful there.

This is the fixed-disjunct consequence of [Definitions 13-15 and Theorem 16](https://www.cs.cmu.edu/~emc/15-820A/reading/biere99symbolic.pdf#page=12), with the proof supplied here.

## 4. Uniform lasso bounds, padding, and one sufficient SAT bound

### 4.1 Padding a lasso to any larger bound

Suppose an initial path pi has the representation `u v^omega`, where `a=|u| >= 0` and `b=|v| >= 1`. Its natural bounded representation has `k_0=a+b-1` and loop entry a.

For every `K >= k_0`, define

\[
l_K=a+((K+1-a)\bmod b).
\]

Then `a <= l_K <= a+b-1 <= K`, and periodicity gives

\[
\pi(K+1)=\pi(l_K).
\]

The transition from pi(K) to pi(K+1) therefore closes the prefix at l_K. Also `K-l_K+1` is a positive multiple of b. Repeating that segment reproduces the same infinite path pi, rather than a different continuation. Thus pi is a `(K,l_K)`-loop for every such K.

Consequently, if pi satisfies any LTL formula h, `D_(K,l_K)(h)` and the existing general encoding `[[M,h]]_K` are satisfiable for every `K >= a+b-1`.

### 4.2 Uniformly bounded path shapes

Suppose integers `U >= 0`, `V >= 1` satisfy:

\[
\forall\pi\text{ starting in }I\quad
\exists u,v:\quad
\pi=uv^\omega,\quad |u|\le U,\quad 1\le |v|\le V.
\tag{L}
\]

Put `K=U+V-1`. For every LTL h,

\[
M\models_E h
\iff
\llbracket M,h\rrbracket_K\text{ is satisfiable}.
\tag{2}
\]

Proof: an ordinary witness has some a<=U and b<=V, so its natural bound is at most K; the padding argument realizes that very witness at K. Conversely, satisfiability implies an ordinary witness by the existing encoding-correctness theorem. This proves both implications. For a universal property phi, apply (2) to the negation-normal form of `not phi` and use unsatisfiability.

The pair U,V need not be unique or optimal. If I is empty, the existential claim and SAT encoding are both false and universal validity is vacuous. Condition (L), with state-counted word lengths, proves a bound one smaller than the report's conservative u+v statement; the complete proof is supplied here from [Definition 26 and Theorem 27](https://www.cs.cmu.edu/~emc/15-820A/reading/biere99symbolic.pdf#page=15).

More generally, if every relevant witness can be chosen with `|u|+|v| <= B`, then K=B-1 suffices by the same proof. This version can be sharper than adding separate maxima U and V.

### 4.3 Deterministic total systems

If every state has exactly one T-successor, every initial execution repeats a state within its first N+1 positions. Choose its first repetition `s_j=s_i`, with `0<=i<j<=N`. Determinism makes the suffix after j identical to the suffix after i, giving stem length i and period length j-i. Hence the combined representation length is j<=N.

Therefore, for **every** LTL h on a finite deterministic total system,

\[
M\models_E h
\iff
\llbracket M,h\rrbracket_{N-1}\text{ is satisfiable}.
\]

The bound does not depend on h's length or nesting depth, because the loop translation evaluates the infinite repeated path. It also permits multiple initial states. A one-state system has K=0, and total determinism supplies the required self-loop.

### 4.4 Mere eventual periodicity is not a uniform shape bound

Take initial state a, transitions `a->a`, `a->b`, `b->b`, and p true only at b. Every path is ultimately periodic, but it can delay its first visit to b arbitrarily.

For each integer m>=1, the formula

\[
h_m=X^m p\land X^{m-1}\neg p
\]

requires first entry to b precisely at time m. A no-loop witness with k<m fails the nested-next clause. A k-loop with k<m would have only a-states in its prefix and hence remain at a forever, also failing h_m. Bound m has the witness `a^m b^omega`.

Thus no bound depending only on this two-state model works for all LTL formulas. Condition (L) is a genuine uniform hypothesis; finiteness or individual eventual periodicity alone does not supply it.

## 5. An explicit linear bound for the F/G-only fragment

The report states that such a bound exists but does not give a constant or proof in Section 5.2. The following is an independently supplied sufficient result, not an asserted optimal constant or a transcription of an unprinted theorem.

Let h use only literals, constants, conjunction, disjunction, F, and G. Let m count its distinct temporal subformulas of the form `F theta` or `G theta`. Then, with N>=1,

\[
M\models_E h
\iff
\llbracket M,h\rrbracket_K\text{ is satisfiable},
\qquad K=2(m+1)N-2.
\tag{FG}
\]

### 5.1 Divide an ordinary witness into constant temporal-value intervals

Assume an initial path pi satisfies h. Along any fixed infinite path, the truth of `F theta` can change only from true to false, and the truth of `G theta` only from false to true. Each therefore changes at most once. Record the m temporal truth values at every position. The path has at most m+1 successive intervals on which this whole record is constant; the last interval is infinite.

In each finite interval, erase cycles from its state sequence while retaining its first and last states (as states, even if they coincide). This leaves a simple path with at most N vertices. Consecutive intervals remain connected by their original boundary edge. All retained positions keep the same atom labels and the same temporal record as their original occurrences.

### 5.2 Construct a short recurring suffix with all required witnesses

Let Z be the nonempty set of states occurring infinitely often in the last interval. After a sufficiently late point, no other states occur. The graph induced by Z is strongly connected: sufficiently late occurrences of any two such states are connected by the intervening original path in Z. Every vertex of Z also lies on a positive closed walk.

For each temporal subformula whose final value is `F theta=true`, theta holds infinitely often; otherwise that eventuality would eventually become false. Choose a recurring state witnessing theta. For every final `G theta=false`, choose a recurring state witnessing `not theta`, which likewise occurs infinitely often. There are at most m such obligations.

Truth of any proper subformula at a state with the final temporal record is determined by that record and the state's atom labels. Thus the selected witness states have well-defined required subformula truth values at every late occurrence.

Within Z, connect these witness states cyclically by shortest paths. If there are r>=1 selected witnesses, the concatenated closed walk has length at most r(N-1), unless that length is zero because the witnesses coincide. In that case use a shortest positive cycle through their common state, of length at most N. If r=0, choose any simple positive cycle in Z. In all cases a nonempty closed walk of length

\[
b\le\max(1,m)N
\]

visits every required witness. Let its first vertex be w. Connect the start of the last interval to an occurrence of w using its original path and erase cycles. This adds at most N vertices in the last interval, just as for each finite interval.

The total stem, excluding its final cycle-entry vertex, therefore has length

\[
a\le(m+1)N-1.
\]

Repeat the closed walk forever. It gives a valid initial lasso.

### 5.3 Prove preservation of all subformula truth values

Assign each retained stem state its original temporal record, and each cycle state the constant final record. Prove by structural induction that every subformula has its recorded original value along the new path. Literals and Boolean cases follow directly.

For `F theta` recorded false, every later original occurrence satisfies `not theta`; this includes every retained later stem state and every chosen recurring state. The induction hypothesis makes it false on the new path too.

For `F theta` recorded true, either its final value is true, in which case the new cycle visits its theta-witness, or it eventually changes to false. At its last true position before that change, theta itself must hold. That position is an interval endpoint and its state and temporal record were retained by cycle erasure. The induction hypothesis again supplies a future theta-witness.

For `G theta` recorded true, theta holds at every later original occurrence; all retained stem and recurring cycle states therefore satisfy theta by induction. For `G theta` recorded false, either its final value remains false and the cycle supplies a `not theta` witness, or it changes to true. In the latter case theta is false at the last position before the change; that interval endpoint was retained. Thus the required counterexample to always-theta survives.

This proves the temporal cases, including arbitrary nesting of F and G. In particular h remains true at the initial state. No next operator is allowed: deleting intermediate states would not in general preserve it.

The natural lasso bound is

\[
k=a+b-1
\le (m+1+\max(1,m))N-2
\le 2(m+1)N-2=K.
\]

Pad this lasso to K by Section 4.1. This proves the forward implication of (FG); encoding soundness proves the reverse. When m=0 and N=1, K=0, which is valid. No witness exists when h is false or I is empty, and both sides are false.

The result supplies a concrete O(N(m+1)) bound corresponding to the qualitative statement in [Section 5.2](https://www.cs.cmu.edu/~emc/15-820A/reading/biere99symbolic.pdf#page=14).

## 6. Optional handbook construction: bounded ECTL certificates

### 6.1 Attribution boundary

This section defines a **handbook construction**, not the report's unprinted bounded ECTL semantics. It gives an exact, independently proved sufficient result for the existential CTL language discussed in Section 5.1. In particular it must not be denoted by the existing bounded LTL path-satisfaction notation without an explicit distinction.

The certificate horizon is local to each temporal operator. Its subformula certificates can branch independently. Every EX certificate consumes one edge and is forbidden at horizon zero. The resulting sufficient uniform horizon is `max(1,d)`, not an artificially retained d when d=0.

### 6.2 Syntax and ordinary semantics

Use the state-formula grammar

\[
\theta ::= \top\mid\bot\mid p\mid\neg p\mid
\theta\land\theta\mid\theta\lor\theta\mid EX\theta
\mid E[\theta U\theta]\mid EG\theta.
\]

Ordinary truth `M,s |= theta` has the usual literal and Boolean clauses and:

- `EX alpha`: some t with T(s,t) satisfies alpha.
- `E[alpha U beta]`: some finite path from s reaches a beta-state, with alpha true at every earlier position. A zero-length witness is allowed. Totality extends it to an infinite path.
- `EG alpha`: some infinite path from s consists entirely of alpha-states.

Define `EF alpha := E[top U alpha]`. Existential release can be included without a new primitive:

\[
E[\alpha R\beta]
\equiv EG\beta\ \lor\ E[\beta U(\alpha\land\beta)].
\]

Indeed, on a release witness either beta holds forever, or an alpha-position is reached while beta holds through that position. Conversely either disjunct supplies a release witness. This identity includes beta at the release endpoint.

### 6.3 Local bounded semantics

Write `M,s ||-_k theta`, k in N, for the following finite-certificate relation. Literals and constants have their ordinary meanings; conjunction and disjunction use this same bounded relation for their children. Define:

\[
M,s\Vdash_k EX\alpha
\iff k\ge1\ \land\ \exists t\,[T(s,t)\land M,t\Vdash_k\alpha].
\]

\[
\begin{split}
M,s\Vdash_k E[\alpha U\beta]
\iff{}&\exists r\in\{0,\ldots,k\}\ \exists s_0,\ldots,s_r:\\
&s_0=s\ \land\ \bigwedge_{j=0}^{r-1}T(s_j,s_{j+1})\\
&\land\ M,s_r\Vdash_k\beta
\ \land\ \bigwedge_{j=0}^{r-1}M,s_j\Vdash_k\alpha.
\end{split}
\]

\[
\begin{split}
M,s\Vdash_k EG\alpha
\iff{}&\exists r\in\{0,\ldots,k\}\ \exists l\in\{0,\ldots,r\}
\ \exists s_0,\ldots,s_r:\\
&s_0=s\ \land\ \bigwedge_{j=0}^{r-1}T(s_j,s_{j+1})
\ \land\ T(s_r,s_l)\\
&\land\ \bigwedge_{j=0}^{r}M,s_j\Vdash_k\alpha.
\end{split}
\]

Every recursive call concerns a proper syntactic subformula, so these clauses are well-founded even though k is not decreased. Different conjuncts, and different occurrences of a child along a witness, may have different witness paths.

At k=0, until reduces to the bounded beta-clause; EG requires a self-loop and the bounded alpha-clause; EX is false. These conventions are explicit parts of this construction, not recovered source conventions.

### 6.4 Soundness and completeness

For every k and state s,

\[
M,s\Vdash_k\theta\ \Longrightarrow\ M,s\models\theta.
\]

Proof is structural induction. The EX clause supplies a real edge and a true child. The until clause supplies a finite witness whose required children are true; totality provides an infinite continuation. The EG clause supplies a lasso, and each repeated state satisfies alpha by induction. Boolean clauses preserve the implication because negation occurs only at atoms.

For every `k >= max(1,d)`, every state s, and every formula theta in this grammar,

\[
M,s\models\theta\ \Longleftrightarrow\ M,s\Vdash_k\theta.
\tag{ECTL}
\]

For completeness, use structural induction simultaneously at all states. EX has a one-edge witness and k>=1. For until, choose a shortest path satisfying its state-formula constraints; a repeated state could be removed without losing any constraint, so its length is at most d. For EG, take a simple cycle in the subgraph of alpha-states and a shortest path from s to its vertex set within that subgraph. The stem and cycle are disjoint before entry, so their sequence before the closing vertex is a simple path of length at most d. In both cases the induction hypothesis supplies all bounded child certificates at the same k. This proves every temporal case and hence (ECTL).

Increasing k preserves bounded truth by another structural induction, since it only enlarges the permitted finite witness families. The certificate is therefore an underapproximation that becomes exact by the stated bound.

### 6.5 Propositional compilation and the branching distinction

For a Boolean state vector s, compile the preceding clauses directly. Literals become their state predicates; Boolean connectives remain Boolean connectives. EX introduces one fresh vector t. Until introduces fresh vectors for each possible witness length r and conjoins its transition and child-certificate formulas. EG additionally disjoins over the loop entry l and adds the closing edge.

Every recursive occurrence must receive fresh private witness variables. All witness quantifiers are existential and occur positively; after renaming, they can be moved to the front and omitted for a SAT query. Structural induction gives exact correspondence between satisfiability of the compiled certificate at a fixed state and bounded ECTL truth there. This assertion is about correctness, not an unproved polynomial-size bound for naive expansion.

For existential initial-state satisfaction, add `I(s)` and existentially choose s. With k>=max(1,d), that SAT query is exact. To check a universally initialized ACTL property, negate it into ECTL negation normal form and search for an initial counterexample by this query.

The construction cannot be replaced by one LTL path formula. For example, a state with one successor satisfying p and another satisfying q can satisfy `EX p and EX q` while no successor satisfies `p and q`. Independent existential witnesses are necessary.

## 7. Ordinary diameter: a narrower reachability bound

Define the all-state diameter

\[
D=\max\{\operatorname{dist}(u,v):u,v\in S, v\text{ reachable from }u\}.
\]

Zero-length paths are admitted, so the set is nonempty. Shortest paths are simple; hence `0<=D<=d<=N-1`. Every ordinary EF state-predicate witness can be shortened to length at most D. This is the reachability specialization of [Definition 19 and Theorem 20](https://www.cs.cmu.edu/~emc/15-820A/reading/biere99symbolic.pdf#page=13).

For r in N, a precise all-state certificate for `D<=r` is

\[
\begin{split}
\forall s_0,\ldots,s_{r+1}\in S\ \exists t_0,\ldots,t_r\in S:\quad
&\bigwedge_{i=0}^{r}T(s_i,s_{i+1})\ \Longrightarrow\\
&t_0=s_0\land\bigwedge_{i=0}^{r-1}T(t_i,t_{i+1})
\land\bigvee_{i=0}^{r}t_i=s_{r+1}.
\end{split}
\]

If D<=r, use a shortest same-endpoint path of length at most r and extend it to r transitions by totality. Conversely, if a shortest u-to-v path had more than r edges, the certificate would shorten its first r+1 edges to at most r; appending the remaining suffix would contradict shortestness. Thus the certificate is exact. This supplies the proof behind the form in Theorem 21.

This unrestricted diameter must not replace d for constrained until: a shortest unrestricted route can pass through states where its left operand is false. The ECTL proof above uses shortest paths satisfying the relevant state predicates, bounded by the longest-simple-path quantity d.

## 8. Authoring disposition

- The fixed-lasso padding theorem and deterministic corollary fit directly after the current general-product bound. They use the existing LTL syntax and encoding without modification.
- The F/G-only bound supplies the missing explicit constant and complete proof for the fragment mentioned in Section 5.2. Its restriction excludes X, U, and R.
- The ECTL section is optional new handbook machinery with its own notation, local witness horizon, and full proof. It must be introduced as such, not passed off as the report's unavailable bounded ECTL definition.
- The diameter certificate is a separate, narrower reachability result. The existing recurrence-diameter and product results remain unchanged.

## 9. Internal evidence boundary

The report's missing bounded ECTL clauses prevent verification of whether its horizon is inherited, reset, or interpreted through loop positions at nested operators. In particular, its stated small-k ECTL results do not authorize inventing an exception for EX at k=0. Section 6 explicitly chooses EX=false at k=0 and proves the safe bound max(1,d).

The source's recurrence-diameter final-state repetition defect has already been corrected in the manuscript. No source-error narrative is proposed for the reader-facing theorem. Every supplied proof here uses the corrected simple-path definition.

No unproved exact automaton-size estimate, fixed coefficient for an unprinted source proof, or finite-state-only lasso assumption is silently substituted for a stated hypothesis.

## 10. Principal-source coverage check, 2026-09-06

Compared the full current Biere subsection (`n-c-017.tex:1641-2462` at this reading) with the nineteen-page primary report. The principal mathematical development is now represented: finite Boolean model and NNF LTL, loop/no-loop distinction, all temporal translation clauses, bounded soundness and witness existence, SAT correspondence, recurrence and ordinary diameter, safety and persistence, ordinary-Buchi product completeness, uniform lassos, and the F/G fragment. The new bounds were not re-audited here. No further missing principal mathematical theorem was identified at this bounded coverage level. Three presentation gaps and one attribution clarification remain actionable:

1. **The source's main worked example is absent.** [Section 2 and Figure 1, physical pages 6-7](https://www.cs.cmu.edu/~emc/15-820A/reading/biere99symbolic.pdf#page=6) use an initially arbitrary three-bit register with `x'[0]=x[1]`, `x'[1]=x[2]`, `x'[2]=1`, where the last 1 is the erroneous replacement for zero-fill. The universal eventual-zero property is refuted by a nonzero lasso. Add this original example alongside the existing handbook `p U q` calculation. At the source's chosen k=2, its formula is `T(x_0,x_1) and T(x_1,x_2) and (OR_(j=0)^2 T(x_2,x_j)) and (AND_(j=0)^2 (x_j != 0))`; all nine state bits equal to 1 satisfy it. Do not call k=2 minimal: with I=true, `111` already gives a self-loop witness at k=0.

2. **The increasing-bound SAT driver and its precise minimality guarantee are not explicit.** [Section 1 and the opening of Section 5, physical pages 5 and 13](https://www.cs.cmu.edu/~emc/15-820A/reading/biere99symbolic.pdf#page=13) describe checking k=0,1,2,..., returning and decoding the first satisfying assignment. Add this operational connection after the encoding correspondence: the first successful horizon is the least satisfiable bounded horizon when all smaller horizons were actually checked; this does not separately minimize the period or number of distinct states. An unsatisfiable prefix of this search proves only absence at the searched bounds unless a completeness bound is established. Also state that fixed-k SAT construction uses the direct temporal clauses without a tableau; the automaton product supplies a completeness proof/bound and is not a prerequisite for bounded bug finding.

3. **The implementation and positive verification experiments are omitted.** The current final paragraph covers only distributed-mutual-exclusion liveness and its missing bound. [Section 6, Tables 1-2, physical pages 15-17](https://www.cs.cmu.edu/~emc/15-820A/reading/biere99symbolic.pdf#page=15) additionally supplies BMC's SMV-subset input, DIMACS/SATO and PROVE backends, a 16-by-16 sequential multiplier checked against a combinational multiplier for the selected output bits and overflow, and a barrel-shifter invariant with a separately checked finite bound. Add a compact description of these complete-verification uses and their benchmark-specific status; every timing row is unnecessary for this principal-coverage task. Do not import the source's defective recurrence-diameter formula or treat a benchmark observation as a worst-case complexity improvement.

4. **Make the ECTL attribution explicit in one sentence.** The current paragraph says that it gives a separate state-certificate construction and correctly distinguishes it from bounded LTL, but its final Section 5.1 citation and the subsection's opening source-for-definitions wording can still suggest that these are recovered source clauses. Add a concise attribution such as: `The following state-certificate construction is supplied here for the existential CTL fragment; it is not the report's unprinted bounded ECTL definition.` The report's deferral is explicit in [Section 5.1, physical page 13](https://www.cs.cmu.edu/~emc/15-820A/reading/biere99symbolic.pdf#page=13). Retain the existing independently proved local-horizon semantics and its max(1,d) bound.

This is a principal-source coverage record, not topic acceptance, publication approval, or a requirement to reproduce all empirical tables or source prose. Only this section was appended; the manuscript was not edited.

## 11. Disposition of the four bounded coverage findings, 2026-09-06

Implemented the four findings in the Biere subsection only, preserving its prior content. The manuscript now has the paragraph anchors `sec:p09-n-c-017-biere-horizon-search`, `sec:p09-n-c-017-biere-shift-register`, `sec:p09-n-c-017-biere-ectl-certificates`, and `sec:p09-n-c-017-biere-positive-experiments`.

- The horizon-search paragraph gives the increasing-k procedure, assignment decoding, certified stopping condition, unknown-result handling, and the exact least-satisfiable-horizon guarantee. It distinguishes direct fixed-k SAT construction from the automaton argument for a completeness bound.
- The shift-register paragraph defines the original three state bits, unrestricted initial predicate, all transition equalities, nonzero property, k=2 unfolding and closing-edge formula, and the all-ones satisfying assignment. It separately derives the k=0 self-loop witness instead of calling the illustrative horizon minimal.
- The ECTL paragraph now explicitly identifies its clauses as a handbook construction separate from the report's unprinted bounded semantics. No certificate equation or proved bound was changed.
- The implementation/experiment paragraph records BMC's SMV-subset input and output formats, SATO/PROVE backends, multiplier comparison, and barrel-shifter invariant/finite-bound experiment. The existing qualified DME liveness account remains intact.

Read before editing: the current Biere subsection and this note's coverage section; the [primary report's Section 2 and Figure 1/Equation (1)](https://www.cs.cmu.edu/~emc/15-820A/reading/biere99symbolic.pdf#page=6), [Section 1 and opening of Section 5](https://www.cs.cmu.edu/~emc/15-820A/reading/biere99symbolic.pdf#page=13), and [Section 6](https://www.cs.cmu.edu/~emc/15-820A/reading/biere99symbolic.pdf#page=15). The written changes were read back directly as LaTeX and Markdown. No manuscript outside the Biere subsection, no new file, no build, render, software test, or additional agent was used. This records bounded authoring work, not full-topic acceptance.
