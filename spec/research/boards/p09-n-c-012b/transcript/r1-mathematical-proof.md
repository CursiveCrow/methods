# Blind opening audit — mathematical and proof correctness

**Seat:** `/root/p09_math_proof_review`  
**Opening verdict:** **REVISE**

I read the board charter before substantive review, verified the frozen hashes,
and visually read every printed source page 46--57 from the scholarly render of
the author-hosted scan. I then read the complete Pnueli source note, the frozen
manuscript scope (`n-c-012.tex` lines 370--618 and 1023--1027), ledger lines
151--161, the `Pnueli1977` bibliography entry, and the temporal-logic shared
surface in `logic-in-computer-science.tex` lines 599--823. I read no board
ledger or chair record and no other seat's transcript or output, and I did not
contact another reviewer.

## Findings

### MP-F1 — must-fix — the sequential and concurrent transition models are under-typed

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:380-400`.
- **Claim:** The passage says that next-location and data-transformation
  functions determine sequential steps and that a concurrent step updates one
  processor, but it supplies neither the functions' types nor the equations
  defining `R`.
- **Evidence:** Printed p. 47 gives the literal sequential equation
  `R(<pi,u>,<pi',u'>)` iff `pi'=N(pi,u)` and `u'=T(pi,u)`, and the concurrent
  equation which chooses an index `i`, replaces only `pi_i` by
  `N_i(pi_i,u)`, leaves every other control coordinate fixed, and sets
  `u'=T_i(pi_i,u)`.
- **Mathematical harm:** The reader cannot check determinism, the domain and
  codomain of the two functions, or the claim that one atomic concurrent step
  changes exactly one control coordinate. Criterion C2 asks for the complete
  program model, not only a prose paraphrase.
- **Exact correction:** Introduce a data domain `D`. For the sequential case,
  state that `S=L x D`, with finite control set `L`,
  `N:L x D -> L`, `T:L x D -> D`, and
  `R((pi,u),(pi',u'))` iff
  `pi'=N(pi,u)` and `u'=T(pi,u)`. For the concurrent case, give finite
  `L_i`, maps `N_i:L_i x D -> L_i` and `T_i:L_i x D -> D`, and the displayed
  existential-index update equation from p. 47. This defines the data-domain
  name, its standing, and its actual use at the point of introduction.

### MP-F2 — must-fix — `R^*` is used without fixing the zero-step case

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:402-408`.
- **Claim:** `X={s in S:R^*(s_0,s)}` is called the set of reachable states,
  but `R^*` is not defined before use.
- **Evidence:** Printed p. 48 calls `R^*` a closure and immediately equates
  invariance on `X` with truth at all execution times, including time zero.
- **Mathematical harm:** If “transitive closure” is read as positive-length
  reachability, `s_0` can be absent from `X`; that conflicts with the source's
  time-zero reading and with P1's initial premise. This is not a harmless
  notation choice at the invariant boundary.
- **Exact correction:** Define
  `R^0=Id_S`, `R^(m+1)=R^m circ R`, and
  `R^*=union_{m>=0} R^m`, then define `X`. Explicitly call this the
  reflexive-transitive closure, while noting that p. 48 informally says
  “transitive closure.”

### MP-F3 — must-fix — P2 is replaced by a high-level paraphrase, and that paraphrase silently hides another strictness defect

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:439-442` and
  `:493-500`.
- **Claim:** The passage says only that every state has a rank and a transition
  either decreases it or “reaches the target.” It does not state P2's typed
  predicate, quantifiers, premises, conclusion, or the state at which the
  target is tested.
- **Evidence:** Printed p. 49 states, for positive natural `n`, the two
  premises
  `phi(s) => exists n A(s,n)` and
  `A(s,n) and R(s,s') => A(s',n-1) or psi(s)`, followed by
  `phi leadsto psi`. The printed disjunct is `psi(s)`, not `psi(s')`.
- **Mathematical harm:** “Reaches the target” naturally reads as a successor
  target and therefore silently repairs the source. More importantly, printed
  P2 is not sound for the strict `j>i` semantics. A minimal counterexample has
  states `a,b`, transitions `aRb` and `bRb`, initial state `a`, `phi(a)` and
  `psi(a)` true, `psi(b)` false, and only `A(a,1)` true (with `A(b,0)` false).
  Both printed premises hold, but no later state satisfies `psi`. The existing
  strictness paragraph names A2, inclusive `F`, and Theorem 3, yet omits this
  printed P2 conflict.
- **Exact correction:** Display P2 literally with
  `A:S x N_0 -> Prop`, quantification over `n>0`, and the pre-state disjunct
  `psi(s)`. Record explicitly that it supplies a second source-internal clash
  with strict temporal implication. Do not replace it silently. If the
  handbook also wants a valid strict ranking lemma, label it as a
  handbook-supplied repair and use, for example,
  `A(s,n) and R(s,s') => psi(s') or (n>1 and A(s',n-1))`, then prove the
  strict conclusion by induction on the positive rank.

### MP-F4 — must-fix — Theorem 1's branching hypothesis is not stated mathematically

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:482-491`.
- **Claim:** “Bounded nondeterminism” is named but not defined.
- **Evidence:** Printed p. 50 explains the intended hypothesis parenthetically:
  for each state `s`, there are at most finitely many distinct successors
  `s'` with `R(s,s')`. This is finite branching; the source does not require a
  single uniform numerical branching bound.
- **Mathematical harm:** Koenig's infinity-lemma step depends on finite
  branching. The present phrase is compatible with a stronger uniform bound or
  an undefined informal restriction, so the exact completeness-sketch
  hypothesis cannot be recovered from the manuscript.
- **Exact correction:** Replace the bare phrase by
  `for every s in S, {s' in S:R(s,s')} is finite`, and say explicitly that no
  uniform bound over all states is asserted. Retain the expressive-assertion
  hypothesis and proof-sketch status already stated.

### MP-F5 — must-fix — the Floyd reduction reverses premise and conclusion

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:503-515`.
- **Claim:** The text says invariant induction “yields” the initial condition
  and per-instruction verification conditions.
- **Evidence:** Printed p. 50 substitutes the attached assertion into P1 and
  obtains `q_0(u_0)` and each local preservation condition as the verification
  conditions which must be discharged; from them P1 yields invariance of the
  global attached assertion and hence partial correctness.
- **Mathematical harm:** The inference direction is reversed. Induction cannot
  derive its own base and step premises. In particular, a false `q_0(u_0)` is
  not made true by invoking P1.
- **Exact correction:** Say that substitution reduces the invariant proof to
  the premises `q_0(u_0)` and, for every location and datum,
  `q_i(u) => q_{N(ell_i,u)}(T(ell_i,u))`; after those premises are proved, P1
  yields invariance and the exit assertion. Keep the path argument's source
  boundary: p. 50 says the convenient finite-path form is formally decomposed
  into finitely many one-step A1 instances plus R2.

### MP-F6 — must-fix — the displayed `F/G` clauses do not define nested tense formulas

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:527-541`.
- **Claim:** `H(t,p)` is defined as the atemporal assertion `p(s_t)`, and the
  same metavariable is then used in the `F` and `G` clauses even though the
  prose permits arbitrary nesting of tense operators.
- **Evidence:** Printed p. 52 first explains `H(t,p)` as assertion evaluation,
  then says `F` and `G` are unary operators usable in arbitrary tense wffs and
  interprets such formulas relative to a present time.
- **Mathematical harm:** `H(t,Fp)` is ill-typed under the manuscript's own
  equation `H(t,p)=p(s_t)`, so formulas such as `FFp`, `G(p=>Fq)`, and the
  axioms G1--G3 lack a recursive semantics. These are formulas actually used
  later.
- **Exact correction:** Reserve `H(t,p)=p(s_t)` for atemporal state assertions.
  Give the recursive clauses
  `(sigma,n) |= F A` iff `exists t>=n (sigma,t)|=A` and
  `(sigma,n) |= G A` iff `forall t>=n (sigma,t)|=A`, together with the base
  clause `(sigma,n)|=p` iff `p(s_n)` and the ordinary Boolean clauses. State
  that `A` ranges over tense formulas. This retains the inclusive present and
  makes nesting typed.

### MP-F7 — must-fix — all four printed quantifier principles are omitted

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:539-555`.
- **Claim:** The passage says formulas may contain quantifiers but gives only
  the propositional G1--G3 basis and Theorem 2.
- **Evidence:** Printed p. 53 separately displays Q1--Q4:
  `G(forall x p) <=> forall x Gp`,
  `F(exists x p) <=> exists x Fp`,
  `F(forall x p) => forall x Fp`, and
  `exists x Gp => G(exists x p)`.
- **Mathematical harm:** The source's quantified extension and the
  universal/existential asymmetry disappear, although criterion C5 expressly
  requires the quantifier treatment. The reader also cannot tell whether a
  claimed commutation is an equivalence or only one direction.
- **Exact correction:** Reproduce Q1--Q4 with their exact directions after
  defining the quantified formula standing. Keep Theorem 2 explicitly scoped
  to the pure propositional future-restricted fragment and display
  necessitation at proof level as `vdash A / vdash G A`.

### MP-F8 — must-fix — N's fairness premise is only informal, and its displayed action type is too weak

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:557-592`, with
  interaction at `:398-400`, `:411-421`, and `:600-605`.
- **Claim:** The display allows an arbitrary designated relation `A subseteq R`
  and says merely that it “cannot be delayed forever.” It does not give the
  finite action family or state which execution class the conclusion ranges
  over. The earlier strict `leadsto` definition quantifies all raw `R`-paths.
- **Evidence:** Printed p. 53 partitions `R` into a finite action family
  `Q={A_i}` and adds to the execution definition the restriction equivalent to
  `for every A in Q and every i, some j>i has A(s_j,s_{j+1})`. Printed p. 47's
  enabled-processor fairness is an earlier informal scheduling statement; it
  is not a substitute for the p. 53 action quantifier.
- **Mathematical harm:** As a displayed inference rule, N is unsound without
  the missing premise. Let `S={s}`, let `R` be the self-loop, take `A` empty,
  `p` true and `q` false. Preservation while not executing A holds and the
  A-step premise is vacuous, but `p=>Fq` is false. It is also unclear whether
  Theorem 3 and later system proofs quantify raw executions or the fair subset.
- **Exact correction:** Before N, define a finite action partition
  `Q={A_1,...,A_k}` of `R`, take the designated action as `A in Q`, and state
  the admitted-execution condition
  `forall A in Q forall i exists j>i A(s_j,s_{j+1})`. State explicitly that N's
  conclusion is sound only over that restricted class. Keep the earlier
  enabled-processor wording as a distinct informal motivation rather than an
  implicit definition.

### MP-F9 — must-fix — Theorem 4 is under-hypothesized, reuses `A` at the wrong type, and does not state the exact SCC test

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:599-612`.
- **Claim:** The finite system is not stated to exclude halting/deadlock states;
  the action relations are only a union, not the source's finite partition;
  `A` is reused in `G(A=>FB)` immediately after standing for a binary action
  relation; and “can support every required action forever” is not an
  eliminable SCC condition.
- **Evidence:** Printed p. 55 expressly assumes no halting states or deadlocks,
  uses a finite action partition, declares the theorem's `A,B` to be arbitrary
  propositional expressions, and gives the component test: after deleting
  target states, a reachable strongly connected component must carry all
  action labels on edges internal to that component.
- **Mathematical harm:** The displayed formula is ill-typed under the local
  standing `A subseteq R`; finite maximal runs have no declared semantics; and
  the prose does not let a reader decide whether a label on an outgoing edge,
  rather than an internally repeatable edge, suffices. The latter would be a
  false criterion.
- **Exact correction:** State `S` finite and `R` serial (the source's
  no-halting/no-deadlock assumption), and let `Q={A_1,...,A_k}` be the finite
  action partition. Rename the state propositions to `p,q:S->Prop` and state
  Theorem 4 for `G(p=>Fq)`. In the graph induced by
  `S \ [[q]]`, a violating proper path exists exactly when some SCC `C`
  reachable from a relevant reachable `p and not q` state satisfies
  `A_i intersect (C x C) != empty` for every `i` (and is cyclic; this is
  automatic when `k>=1` under the displayed condition). Add the two-line proof:
  strong connectivity lets one connect and repeat one internal edge of every
  label, while any fair infinite path eventually remains in one SCC of the
  finite condensation graph and supplies every such internal label.

### MP-F10 — must-fix — Theorem 5 loses both its proof-system extension and half of its conclusion

- **Location:** `handbook/parts/p09/presentations/n-c-012.tex:612-617`.
- **Claim:** The manuscript reports only decidability for arbitrary
  propositional tense formulas.
- **Evidence:** Printed p. 55 first extends the calculus by the initial-state
  axiom `p(s_0) / vdash p` (P) and modifies generalization to MRG: from
  `vdash A` infer `vdash G A` only if the proof of `A` used no instance of P.
  Theorem 5 then has two clauses: finite-state validity is decidable, and the
  extended system is adequate for proving every valid propositional tense
  formula. Appendix B on printed p. 57 discusses the MSO-successor and
  omega-regular routes; it is not a full local proof.
- **Mathematical harm:** The theorem is materially weakened and its calculus
  cannot even admit arbitrary initially true facts as presented. Omitting MRG's
  side condition also hides the central soundness issue: in a two-state path
  `s_0 -> s_1 -> s_1` with `p` true only at `s_0`, P yields `p`, but unrestricted
  RG would yield the false `Gp`.
- **Exact correction:** Display P and MRG with the exact “no P in the proof”
  side condition, explain that P is needed for initial truth and MRG is
  nonredundant because it prevents the counterexample above, and state both
  Theorem 5 clauses. Preserve the present Appendix B wording as cited proof
  routes/discussion, not as a complete proof reproduced in the paper.

### MP-F11 — must-fix — the ledger's closure statement is inconsistent with the frozen mathematics

- **Location:** `spec/research/p09-source-presentations-lot2-3.md:161`, against
  `handbook/parts/p09/presentations/n-c-012.tex:370-618`.
- **Claim:** The ledger says the reader presentation now defines the exact
  ranking principle, proof systems, Theorems 2--5, and finite-state routes and
  closes the body-level reconstruction.
- **Evidence:** MP-F1--MP-F10 identify omitted or incorrect material on printed
  pp. 47--55, including P2, Q1--Q4, exact fairness, and the P/MRG extension and
  adequacy clause of Theorem 5.
- **Mathematical harm:** The integration surface records closure of a snapshot
  that does not meet its own C2--C6 claims. That can be mistaken for admission
  evidence even though this board requires a fresh unanimous review after
  repair.
- **Exact correction:** Return N-c-012.b's reader-facing status to pending (or
  append a precise repair-pending qualification), repair and re-freeze the
  manuscript, then update the ledger only after all three independent seats
  accept the same new hashes. Do not alter the still-open IEEE comparison.

## Criterion-by-criterion coverage

- **C1 — checked clean.** Identity, FOCS pagination, DOI, author-hosted route,
  1981 wrapper status, local-render standing, bibliography entry, and the
  author-copy/IEEE-direct boundary at manuscript lines 1023--1027 agree with
  printed pp. 46--57 and the source note.
- **C2 — not clean:** MP-F1 and MP-F8. The state tuple, infinite raw paths,
  atomic one-processor interleaving, enabled-processor motivation, and the
  invariance/eventuality examples are otherwise source-exact.
- **C3 — not clean:** MP-F2--MP-F4. P1 and ER A1--A2/R1--R4 are otherwise
  accurately transcribed; the handbook-supplied R4 hygiene condition is
  correctly disclosed; Theorem 1's expressive-assertion and proof-sketch
  boundaries are otherwise preserved.
- **C4 — not clean:** MP-F5. The product-versus-sum attachment comparison,
  global-invariant method, producer--consumer conclusions, and the later
  accessibility-example scope agree with printed pp. 51--55 and import no
  later model-checking machinery.
- **C5 — not clean:** MP-F6--MP-F8. Inclusive present, G1--G3, the pure
  tautology/MP/RG basis, Theorem 2's external-proof boundary, I1/I2/E/N
  transition premises, and Theorem 3's stated ER representation are otherwise
  source-exact. The strict/A2/inclusive-F/Theorem-3 tension is visibly recorded,
  but P2 adds the unrecorded tension in MP-F3.
- **C6 — not clean:** MP-F9--MP-F10. The high-level MSO-successor and
  omega-regular language-inclusion routes and their referral boundary agree
  with Appendix B; no later Buchi construction or complexity class is imported.
- **C7 — not clean:** MP-F11. The source note is a faithful high-level evidence
  map, the bibliography is correct, and the shared Part IX surface keeps modern
  inclusive LTL, GPSS's later strict/X/U language, safety/liveness, Buchi, and
  PSPACE results source-separated. The frozen ledger closure claim is not
  supported by the frozen manuscript.
- **C8 — not clean:** the definition-before-use/type defects in MP-F1, MP-F2,
  MP-F6, MP-F8, and MP-F9 prevent acceptance. The local `leadsto` name and `H`
  abbreviation otherwise give necessity, definition/standing,
  nonredundancy, and use; the prose is independently worded; no I6
  retrojection occurs; and the I8--I10 scope boundaries are preserved.

## Hash recheck and constraints

The following hashes matched the charter both before substantive review and
again after the review:

- `focs77.ps.gz` — `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB`
- `focs77.ps` — `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F`
- `focs77.pdf` — `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972`
- `n-c-012.tex` — `0DADDC029C1ED7574B14BA6A48ACEBE712F93A125AD7641747E336FAE2788C19`
- `logic-in-computer-science.tex` — `99D1DE3EC86F07ECC5CCF5C58A9850D66C8DC7754E4474D8E06AE59A13BDD394`
- `handbook.bib` — `AC811C3E21F76830822D4A78B3786AC2D36660BB919F6C5FEC16217BD663D8E2`
- `p09-pnueli-1977-source-note.md` — `539E0CEBE721A1F75D87223C41E6DEA2F139543E86EEF016750E56D169DE2D16`
- `p09-source-presentations-lot2-3.md` — `C3ACAF3670EF0BCDB58C67138FBA68565817814F19307DF5E25F329D093D2A35`

The harness did not expose a runtime model/version. I made no manuscript,
source-note, ledger, bibliography, or shared-surface edit; ran no tests,
automated checkers, repository scripts, TeX, handbook-PDF inspection, or build;
and created only this owned transcript.

**Verdict: REVISE.**
