ACCEPT

# Round-five mathematical/proof review — N-c-012.b

## Opening position

No blocker, must-fix, should-fix, consider-level mathematical defect, or unresolved mathematical uncertainty remains in the frozen round-five scope. The repaired presentation is well typed, its local reconstructions are valid at their stated strength, its counterexamples compute correctly, and its source-proof gaps and external-proof boundaries are disclosed rather than silently repaired. My verdict on this exact snapshot is **ACCEPT**.

Stable reviewing seat: `/root/p09_math_proof_review`.

The runtime model/version was not exposed by the review harness.

## Independence, method, and authority reading

I read `spec/research/boards/p09-n-c-012b/charter.md` first and used its appended round-five snapshot as the controlling scope. I did not inspect `spec/research/boards/p09-n-c-012b/ledger.md`, `transcript/chair.md`, any round-one through round-four transcript (including my own earlier transcript), or either other round-five transcript. I did not contact another reviewer and did not use another reviewer's conclusion.

I made no manuscript, shared-surface, source-note, ledger, bibliography, or authority edit. I ran no test, test harness, automated checker, repository script, TeX command, handbook-PDF inspection, or build. The only file created is this assigned transcript.

For source scholarship I visually read the author-hosted render's archival wrapper and every printed body page 46--57. Specifically, I opened `tmp/pdfs/p09-pnueli-1977/page-01.png` for provenance and `page-02.png` through `page-13.png` for printed pp. 46--57; the source images controlled over OCR and memory. I also read the complete frozen reader scope, shared scope, source note, ledger scope, three bibliography entries, and adjacent presentation/version boundaries specified in the charter.

## Frozen identities

The following SHA-256 identities were independently checked before substantive review and checked again after the complete review, immediately before filing. Both passes matched the charter exactly:

- `tmp/pdfs/p09-pnueli-1977/focs77.ps.gz`: `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB`
- `tmp/pdfs/p09-pnueli-1977/focs77.ps`: `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F`
- `tmp/pdfs/p09-pnueli-1977/focs77.pdf`: `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972`
- `handbook/parts/p09/presentations/n-c-012.tex`: `1FABE2120A026468AE21DD2BC116A92DE9AAE048D84655032DA4F7048B82620E`
- `handbook/parts/p09/logic-in-computer-science.tex`: `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394`
- `handbook/bib/handbook.bib`: `74F102209EEFB17C63FB5B41B6D257184064BFCFF52CF625BC7A1A61C443B3D9`
- `spec/research/p09-pnueli-1977-source-note.md`: `B27AAA9E6C69403998671A924B7F1883DBC2122048D7CF47124464CA63B65803`
- `spec/research/p09-source-presentations-lot2-3.md`: `3065E52284FF29AAD53121398C3307D691955C13358AE9E314819285A3534203`

The PDF is a local scholarly render, not a substituted bibliographic authority. Its physical page 1 is the May 1981 archival wrapper, while physical pages 2--13 map in order to printed pp. 46--57. The substantive authority is the complete author-hosted printed body preserved by the hash-pinned PostScript objects.

## Findings

There are no findings to assign an `MP-F...` identifier. In particular, there is no remaining defect for which an exact correction is owed.

## Complete mathematical and proof audit

### Program model, executions, reachability, and specifications

At `n-c-012.tex:384-443`, checked against printed pp. 46--47, the dynamic system, sequential specialization, and concurrent interleaving are all typed correctly. The sequential maps have domains and codomains `N:L x D -> L` and `T:L x D -> D`; the concurrent maps use the selected processor's old local location and shared datum, update exactly that local coordinate and the datum, and leave every other location coordinate fixed. The existential processor index is correctly quantified. The deterministic-notation qualification and atomic-granularity qualification agree with the source.

At `n-c-012.tex:445-490`, checked against printed pp. 48--49, the recursive powers give `R^0` as identity and hence make `R*` reflexive-transitive. Consequently `s_0` belongs to the accessible set `X`, as the source's use requires despite its informal phrase “transitive closure.” A state assertion has the declared type `S -> {false,true}` before the subsequent principles use it. Invariance, partial correctness, clean execution, mutual exclusion/deadlock standing, and the strict temporal implication are kept distinct. The displayed temporal implication quantifies every initial execution and every position and requires a target at `j>i`; it is not conflated with the later inclusive `F` connective.

The early enabled-processor scheduling prose at `n-c-012.tex:440-443` and the later all-actions-infinitely-often condition at `n-c-012.tex:910-926` are explicitly kept as different source standings. No equivalence is asserted without proof.

### P1, literal P2, both counterexamples, and the zero boundary

P1 at `n-c-012.tex:492-500` is the ordinary forward induction on finite `R`-paths: the base is at `s_0`, the preservation premise is universally closed over both state variables, and the conclusion ranges over exactly the reflexively reachable set `X`.

The literal P2 package at `n-c-012.tex:501-552`, checked against printed p. 49, is correctly separated into typing, soundness, and strictness questions:

1. Extending the predicate to `A:S x N_0 -> {false,true}` makes the source's `n=1` occurrence `A(s',n-1)` typed, while the rule itself still quantifies `n>0`. The reader correctly identifies that extension and the universal closures as handbook repairs and leaves the current-state disjunct `psi(s)` literal.
2. The zero-rank counterexample at `n-c-012.tex:528-535` works. In `S={a,b}` with transitions `aRb` and `bRb`, only `A(a,1)` and `A(b,0)` hold. The first P2 premise is witnessed by rank 1 at `a`. The only transition instance whose positive-rank antecedent is true is `(a,b,1)`, and its conclusion is true through `A(b,0)`. Nevertheless `psi` is false everywhere, so even inclusive eventuality fails.
3. The unprinted premise `forall s not A(s,0)` at `n-c-012.tex:536-542` is sufficient for the inclusive conclusion and is not claimed to repair the printed strict conclusion. Indeed, from `A(s_i,n)` and the supposition that `psi` is false at the successive current states, the transition premise inductively yields `A(s_{i+k},n-k)` through `k=n`, contradicting the zero prohibition. Thus some `psi` occurs at a position at or after the starting position; nothing in this argument forces it to be strictly later when `psi(s_i)` already holds.
4. The independent strict-future counterexample at `n-c-012.tex:544-552` also works. With `phi` and `psi` true only at `a` and `A` true only at `(a,1)`, the ranked transition obligation is discharged by the current-state disjunct `psi(a)`, but the unique execution's later states are all `b`, so the `j>i` conclusion fails.

The manuscript therefore neither mistakes totalization for soundness nor presents the false-at-zero condition as a complete repair of literal P2.

### ER, R4 hygiene, metarule I, and Theorem 1

At `n-c-012.tex:554-606`, checked against printed pp. 49--50, A1--A2 and R1--R3 have state-assertion types and the required universal closures. R1's preserved assertion is propagated in the correct direction, R2 composes the target of the first implication with the antecedent of the second, and R3 joins antecedent cases.

R4 now uses exactly one parameterized family `p-hat:S x U -> {false,true}`. For each `u`, `p-hat_u` is a state assertion, and the pointwise existential `(exists_U p-hat)(s)` is also a state assertion. It is not treated as a tense constructor. The premise means one derivation uniform in an arbitrary parameter: the consequent `q` and every undischarged assumption are independent of `u`. These are the sufficient eigenparameter conditions. Semantically, when the existential antecedent holds at a state, one selects its witness and applies that uniform instance, so the rule has the stated force. The text accurately marks the family type and hygiene statement as handbook-supplied typing of the source display.

Metarule I at `n-c-012.tex:608-627` consistently specializes that same family to `U=N_0`. Its base is a theorem, its step is a derivation from the displayed temporary hypothesis for an arbitrary `n`, and its conclusion is the theorem family for every `n`. Only after metalevel induction does R4 form the already defined pointwise existential state assertion. There is no free-index/quantifier type collision.

Theorem 1's proof chain at `n-c-012.tex:629-670`, checked against printed p. 50, has exactly the warranted standing. The asserted predicate `P:S x N_0 -> {false,true}` is expressly conditional on assertion-language expressiveness. “Bounded nondeterminism” is correctly rendered as pointwise finite branching, not a global degree bound. From a fixed state, the tree of finite target-avoiding prefixes is finitely branching; unbounded depth would yield an infinite target-avoiding branch by Koenig's infinity lemma. I supplies each `P_n leadsto q`, R4 supplies the pointwise existential family member, and A2/R2 connect the antecedent to that family.

The reader also correctly refuses to certify more than the printed sketch proves. With `S={d}`, empty `R`, and false `q(d)`, there is no infinite execution from `d`, so the source's universal English definition makes `P(d,0)` vacuously true while its base implication to `q(d)` is false. The stated alternatives—serial/execution existence or a nonvacuous recursive/prefix definition—are genuine repairs, and neither is silently added to the theorem. The separate strict/inclusive conflict among temporal implication, P2/A2, inclusive `F`, and Theorem 3 is restated at `n-c-012.tex:662-670` rather than normalized away.

### Sequential and concurrent attachments; producer--consumer proof

At `n-c-012.tex:672-705`, checked against printed p. 50, the sequential attachment is indexed by actual locations. The verification obligations use `q_{N(ell,u)}` rather than treating a location as an integer, and they are correctly presented as premises whose proof allows P1 to yield invariance. The finite-path ER description has the correct A1-then-R2 direction.

At `n-c-012.tex:707-762`, checked against printed p. 51, both concurrent attachment forms are exact and typed. Full attachment has one `D -> Prop` component per location pair and a conjunction whose guards select the current pair. Partial attachment has families `p_i:L_2 x D -> Prop` and `q_j:L_1 x D -> Prop`; each family may depend on the other process's location. Both are metalinguistic representations of one global assertion, not new transition semantics. The manuscript accurately distinguishes the two-process sum-sized top level from product-sized case expansion and reserves exponential growth for a varying number of processes through `prod_h |L_h|`. It also retains the initial and per-transition obligations for global invariants.

The producer--consumer derivation at `n-c-012.tex:764-811`, checked against printed pp. 51--52, is complete at the strength of the printed calculation and does not invent a support set for the location indicators. The types make the three semaphore quantities nonnegative and the location indicators Boolean-valued. Every used implication is stated, including the repaired direction `m_i=1` implies critical-section membership and hence nonwaiting.

The calculations are valid:

- `m_1=m_2=1` and `m_1+m_2+mu=1` force `mu=-1`, contradicting nonnegativity.
- `b=s_1+s_2+e >= 0`, and `s_i<=r_i` gives `b<=r_1+r_2+e=C-f<=C`.
- If process `i` waits on the mutex, `m_i=mu=0`, so the first invariant gives `m_{3-i}=1`; the stated indicator meaning makes the other process critical and nonwaiting.
- In the remaining simultaneous producer/consumer semaphore wait, `r_1=r_2=e=f=0`, so the second invariant forces `C=0`, contradicting the explicit `C>0` hypothesis.

Thus the claimed mutual exclusion, load bound, and deadlock exclusion follow, and the positive-capacity premise is used exactly where needed.

### Inclusive F/G semantics, proof systems, fairness, and Theorems 2--3

At `n-c-012.tex:813-879`, checked against printed pp. 52--53, `H(t,p)` is correctly kept metalinguistic and limited to atemporal state assertions. The recursive clauses type arbitrary nesting of Boolean connectives and unary `F,G`; both use `t>=n`, so the present is included. The absolute present is `s_0`. G1--G3, RT, RG, MP, F2--F3, and Q1--Q4 have the printed directions: Q1--Q2 are biconditionals, Q3--Q4 are one-way implications. The unprovided object-domain semantics and unresolved range of the quantified schemata are disclosed; an atemporal-use policy is not attributed to the source.

Theorem 2's repaired qualification at `n-c-012.tex:881-908` is mathematically necessary and exact. The displayed formula

`(Fp and Fq) -> (F(p and Fq) or F(q and Fp))`

is valid on every inclusive linear future: choose witnesses `i,j` for `p,q` and use the earlier of them, with equality covered by either disjunct. It fails at the root of the stated reflexive-transitive branching frame: the two incomparable reflexive terminal successors separately satisfy only `p` and only `q`; therefore the root satisfies both diamonds but no accessible world satisfies either nested conjunct. This is an S4 frame. The countermodel proves exactly that an arbitrary-S4 referral does not establish completeness for the preceding linear-execution semantics. The manuscript consequently leaves the source theorem's model class unresolved and does not invent a complexity bound.

At `n-c-012.tex:910-970`, checked against printed p. 53, the finite family `mathcal A` is a disjoint relational partition of `R`, and the tail condition `forall a forall i exists j>=i a(s_j,s_{j+1})` is exactly the infinitely-often action condition. I1, I2, E, and N have correct state-variable quantification and successor direction. N's proof uses the first future occurrence of the designated action and preservation across all preceding non-action steps. Its raw-path counterexample is well typed: `a={(t,t)}` and `c={(s,s)}` are relations, `a` is nonempty, the path at `s` takes only `c`, both local premises hold, and `p -> Fq` fails without the action condition.

DI and DN at `n-c-012.tex:972-998`, checked against printed p. 54, reproduce the exact strengthened premise directions and are correctly described as derived from I2 and N. Theorem 3 at `n-c-012.tex:1000-1008` is not overproved: the source's encoding instruction and relative-completeness claim are reported, while the absent individual ER derivations remain absent and the strict/inclusive representation tension remains disclosed.

### Finite systems, proper executions, SCC equivalence, P/MRG, and Theorems 4--5

At `n-c-012.tex:1010-1042`, checked against printed p. 55, finiteness and seriality are distinct hypotheses. Arbitrary-start infinite `R`-paths satisfying the action condition are defined for the continuation test; a proper execution is the initial-state instance beginning at `s_0`; and `Sigma |=_prop A` quantifies exactly those proper executions. These three standings are not conflated.

Theorem 4's route at `n-c-012.tex:1044-1074` is correct. Checking every `p`-state is identified as the source's sufficient route. Restricting first to `X` makes it exact for initial-state validity: any finite path from `s_0` to a reachable offending state can be prefixed to an action-fair target-avoiding tail without changing the infinitely-often condition, while every counterexample proper execution supplies such a reachable state and tail.

The handbook-supplied SCC criterion is an exact equivalence. In the graph with all `q`-states deleted, a reachable cyclic strongly connected component containing an internal edge of every action yields a closed walk that traverses chosen representatives of all actions; strong connectivity joins those representatives, and repeating the walk is an infinite fair target-avoiding path. Conversely, a fair infinite path in a finite graph eventually remains in one component of the acyclic condensation graph; that component is cyclic and its tail contains an internal edge of every action. The formula `a intersect (C x C) != empty` therefore has the correct internal-edge type and quantifier.

P and restricted MRG at `n-c-012.tex:1076-1090` match printed p. 55. The counterexample to unrestricted generalization correctly separates an initially true assertion from one true at all later positions. Theorem 5 at `n-c-012.tex:1092-1097` retains both source clauses—semantic decidability and derivability of every valid propositional tense formula in the extended system—while expressly noting that the paper prints no general adequacy construction and that Appendix B addresses only decidability.

### Appendices A and B

At `n-c-012.tex:1099-1128`, checked against printed p. 57, T2, its corollary, T3, and its corollary have the exact displayed directions and remain externally owned by reference 23. The separate local lemma is proved in six valid steps: excluded middle plus `Fq := not G not q` gives `Fq or G not q`; the assumed `p and G not q` case and the tautological `p and Fq` case both yield `Fq`; propositional case combination and modus ponens give `p -> Fq`. The manuscript does not transfer that local proof to T2 or T3.

At `n-c-012.tex:1130-1177`, checked against printed pp. 55--57, Appendix B's two routes remain semantic decision routes and no later LTL-to-Buchi theorem or complexity class is retrojected. The proper-execution language is a subset of `S^omega`. The repaired atomic clause is now fully typed: a state is identified with its singleton word `(s) in S^1 subset S*`, so `[[p]] subset S*` and `[[p]]S^omega subset S^omega` under the declared finite-prefix/infinite-suffix concatenation. Allowing the empty prefix in `S*` makes `L(FW)=S*L(W)` inclusive, consistent with the earlier semantics. All Boolean and G clauses have the expected language types.

The proof ownership is also exact: Pnueli locally asserts a finite-state infinite-word acceptor for proper executions without giving its tuple, acceptance condition, construction, or proof; reference 32 supplies imported omega-regular/closure machinery; and reference 33 supplies the inclusion decision. The eliminable meaning of “omega-regular” is tied to the already defined nondeterministic Buchi word-automaton language class and does not name an unconstructed automaton.

## Fresh F27--F40 repair audit

All charter-mandated earlier repair obligations were rechecked rather than presumed:

- The F27--F35 package is clean: the raw-path action is one binary relation and does not collide with the load variable; full attachment has an exact formula, standing, distinction, and use; every producer indicator implication used is stated; state assertions precede use; arbitrary-start paths, proper executions, and system validity are distinct; attachment size has the correct varying parameters; the SCC formula and both directions are handbook-owned; Theorem 5's adequacy proof remains unprinted; and the three Appendix B ownership layers remain separate.
- The F36--F40 package is clean: P2 typing is separated from soundness and both independent counterexamples work; the false-at-zero premise has only the claimed inclusive sufficiency; R4 and I share one typed parameter family with the right eigenparameter hygiene; the producer proof includes the `m_i=1` nonwaiting implication; the linear-valid formula and branching S4 countermodel establish exactly the claimed model-class warning; and the one-letter-word embedding repairs the Appendix B type without changing the source recursion.

## Criterion-by-criterion coverage

- **C1 — checked clean.** `n-c-012.tex:372-382`, source-note lines 7--52, ledger lines 151--153, and the `Pnueli1977` bibliography entry agree on identity, DOI, first-party route, wrapper/body page map, hashes, rights boundary, and the still-open IEEE comparison.
- **C2 — checked clean.** `n-c-012.tex:384-490` and `910-926`, against printed pp. 46--49 and 53, give exact system/execution types, atomicity, both fairness standings, reachability, and the specification hierarchy.
- **C3 — checked clean.** `n-c-012.tex:492-670`, against printed pp. 49--50, gives P1/P2, the two P2 defects, ER and its side conditions, typed I, exact Theorem 1 assumptions, the Koenig step, and the deadlock-vacuity proof gap.
- **C4 — checked clean.** `n-c-012.tex:672-811`, against printed pp. 50--52, gives the correctly directed sequential obligations, both typed attachment forms, parameterized size claims, and the complete source-supported producer calculation.
- **C5 — checked clean.** `n-c-012.tex:813-1008`, against printed pp. 52--55, gives recursive inclusive semantics, exact pure/quantified/system rules, the RG boundary, action fairness, DI/DN, and Theorems 2--3 at their warranted source/referral strength.
- **C6 — checked clean.** `n-c-012.tex:1010-1177`, against printed pp. 55--57, gives serial finite systems, proper executions, Theorems 4--5, exact SCC semantics, P/MRG, Appendix proof ownership, and both decision routes with correct language types.
- **C7 — checked clean.** The source note (all 696 lines), ledger lines 151--167, the three bibliography entries, shared Part IX lines 599--823, reader lines 370--1178 and 1583--1590, and adjacent GPSS text agree. The shared LTL/Buchi material is available for explicit cross-reference but is not attributed to Pnueli's 1977 result.
- **C8 — checked clean.** The exposition is independently worded; definitions and local types precede use; source defects are labelled; handbook reconstructions are labelled; and the open-status/version boundary is explicit.

## Invariant-by-invariant coverage

- **I1:** obeyed; this was source reading and mathematical/prose reasoning only, with no prohibited verification or build activity.
- **I2:** obeyed; both hash passes matched every round-five identity.
- **I3:** obeyed; the wrapper was read for provenance and every printed page 46--57 was visually read from the source images.
- **I4:** checked clean; types, quantifiers, premises, side conditions, theorem strength, proof status, and external ownership are explicit and mathematically coherent.
- **I5:** checked clean; strict temporal implication, A2/current-state discharge, inclusive F, and Theorem 3's representation remain visibly separate at `n-c-012.tex:473-483`, `554-606`, `813-839`, `1000-1008`, and especially `662-670`.
- **I6:** checked clean; no X/U grammar, later LTL-to-Buchi translation, safety/liveness syntax, or PSPACE classification is assigned to Pnueli 1977.
- **I7:** checked clean under the user's technical-name rule. State assertion, temporal implication, full/partial attachment, proper execution, restricted validity, `L_prop`, and omega-regular language each have a local necessity or source-specific role, exact eliminable definition/type, standing, distinction from nearby notions, and actual downstream use. No hypothetical construction is given a technical name.
- **I8:** checked clean; `n-c-012.tex:1583-1590`, source-note lines 689--696, and ledger line 167 keep the IEEE-direct comparison open.
- **I9:** obeyed; this is one independent seat's verdict, not a majority or a claim that unanimity has already been obtained.
- **I10:** checked clean; acceptance here can close only this review seat on this N-c-012.b snapshot. The rest of N-c-012, Part IX admission, builds, handbook visual review, human review, final publication, and user acceptance remain open.

## Narrow closure statement

This **ACCEPT** applies only to the round-five mathematical/proof correctness of N-c-012.b on the eight hash-pinned identities above. It does not certify an IEEE-file comparison, another review seat, unanimous board admission, any other N-c-012 presentation, Part IX, a TeX or handbook build, handbook-PDF appearance, human review, final-book completion, or user acceptance.

ACCEPT
