# Pnueli 1977, *The Temporal Logic of Programs*: source note

**Disposition:** AUTHOR-HOSTED PRINTED BODY ACQUIRED AND VISUALLY READ;
REPAIRED READER RECONSTRUCTION AWAITS FRESH UNANIMOUS TOPIC REVIEW;
IEEE-DIRECT FILE COMPARISON OPEN.

## Exact source object, render identity, and rights boundary

- Registered work: Amir Pnueli, “The Temporal Logic of Programs,” *18th
  Annual Symposium on Foundations of Computer Science* (FOCS 1977),
  pp. 46--57, DOI
  [10.1109/SFCS.1977.32](https://doi.org/10.1109/SFCS.1977.32).
- First-party access route: Pnueli's NYU memorial
  [publication list](https://cs.nyu.edu/home/people/in_memoriam/pnueli/c-and-j.html)
  identifies the 1977 FOCS paper and links
  [focs77.ps.gz](https://cs.nyu.edu/home/people/in_memoriam/pnueli/focs77.ps.gz).
- Retrieved 2026-08-22.
- SHA-256 of the author-hosted compressed PostScript:
  `BF0CA7C7DAFEFC3380CBABBC0008217E86232CDFC3B4397581D62C57E4B081FB`.
- SHA-256 after lossless gzip decompression:
  `F2AA3E13C855F117D02B3A9870D2B3B8260FA61C1598CB75858BBBE40E96552F`.
- SHA-256 of the local scholarly-inspection PDF render:
  `484CDCB482267B9671273D5F2920633AFFAE02210D5C0C398DA6533C8F9B3972`.

The PostScript is image-only. It was converted locally to a 13-page PDF and
rendered solely for visual source inspection; the derived PDF and PNG pages
are not bibliographic authorities. Physical page 1 is an archival wrapper
headed with the paper title, author, and “May 1981.” Physical pages 2--13 are
the twelve printed FOCS pages 46--57, so physical page `n` for `2 <= n <= 13`
maps to printed page `n + 44`. The printed body carries the conference title,
author, affiliations, pagination, footnote, figures, references, and
appendices. The wrapper is later archival packaging, not a second edition.

Neither the wrapper nor the printed body displays an open-content,
public-domain, or republication licence. Public first-party hosting supports
scholarly inspection; it does not by itself grant or establish a right to
republish or redistribute the scanned pages. The handbook therefore uses
independently written prose and does not infer a reproduction right from the
access route. The author-hosted scan has not been independently byte- or
image-compared with an IEEE-supplied file.

## Visual locator audit

| Printed pages | Inspected content |
|---|---|
| 46--47 | Summary; invariance/eventuality motivation; dynamic discrete system; exact sequential and concurrent transition equations; atomic interleaving; enabled-processor fairness motivation |
| 48--49 | Time-variable hierarchy; reflexive reachability intended by `R*`; invariance; clean execution; strict temporal implication; P1 and literal P2; beginning of ER |
| 50 | ER axioms and rules; induction metarule `(I)`; Theorem 1 and completeness sketch; sequential attachment and Floyd verification conditions; finite-path intermittent assertions |
| 51--52 | Full and partial concurrent attachments; interaction caveat; positive-capacity producer--consumer calculation; recursive future-tense semantics; pure `F/G` axioms and rules; `F2--F3` on p. 52 |
| 53--54 | `Q1--Q4`; RG restriction; finite action partition and formal fairness restriction; system-dependent rules `I1`, `I2`, `E`, `N`, `DI`, and `DN`; Theorem 3's skeletal proof and relative-completeness corollary; accessibility example |
| 55 | Finite serial action-labelled graph; proper executions; exact SCC route; `(P)` and `(MRG)`; both clauses of Theorems 4--5 |
| 56--57 | Discussion and references; Appendix A's externally owned T2/T3 package and locally proved lemma; Appendix B's monadic-second-order and omega-regular decision routes |

## Exact program and execution model

Printed p. 47 defines a dynamic discrete system

\[
\Sigma=\langle S,R,s_0\rangle,
\qquad R\subseteq S\times S,
\]

where `S` may be infinite and `s_0` is the initial state. An execution is an
infinite sequence `sigma = s_0,s_1,...` satisfying `R(s_i,s_{i+1})` for every
`i >= 0`. The relation may be nondeterministic.

For the deterministic sequential notation, let `L` be the finite location set
and `D` the data domain. The source uses maps

\[
N:L\times D\to L,
\qquad T:L\times D\to D,
\]

and the transition equation

\[
R(\langle\pi,u\rangle,\langle\pi',u'\rangle)
\Longleftrightarrow
\pi'=N(\pi,u)\land u'=T(\pi,u).
\]

Pnueli says explicitly that determinism is used only to simplify notation and
is not essential. For concurrent processors with finite location sets `L_i`,
the state space is `L_1 x ... x L_n x D`; maps
`N_i:L_i x D -> L_i` and `T_i:L_i x D -> D` determine the step selected for
processor `i`, while every other location coordinate remains fixed. Thus one
processor is selected nondeterministically and completes one atomic statement.
The source treats that granularity as a modelling choice and permits a
statement to be split when interference inside it matters.

The early scheduling prose requires that a processor which remains enabled not
be postponed indefinitely. That enabled-processor condition is motivation,
not the later formal action-occurrence restriction, and the source does not
prove the two formulations equivalent.

Define

\[
R^0(s,t)\Longleftrightarrow s=t,
\qquad
R^{m+1}(s,t)\Longleftrightarrow
\exists v\,(R^m(s,v)\land R(v,t)),
\qquad
R^*=\bigcup_{m\ge0}R^m.
\]

Then `X={s in S : R*(s_0,s)}` includes the initial state. This makes explicit
the reflexive reading needed by the source's accessible-state definition even
though the paper calls `R*` the “transitive closure.” A state assertion is a
map `p:S -> {false,true}`; it describes one state rather than a tense formula.
It is invariant exactly when it holds at every state in `X`.

Partial correctness constrains the output only if an exit is reached. The
source's separate clean-execution requirement is an invariant prohibition on
specified illegal intermediate operations or states, including division by
zero, numerical overflow, and out-of-range subscripts. It is needed because a
satisfactory exit value does not show that the intervening execution was
legal. Mutual exclusion and absence of deadlock are further invariant
examples; the later producer--consumer calculation uses this standing.

## Strict temporal implication and literal P2

The paper's temporal implication is the statement family

\[
\varphi\leadsto\psi
\quad\Longleftrightarrow\quad
\forall\sigma\ \forall i\ge0\,
\bigl(\varphi(s_i)\Rightarrow
      \exists j>i\,\psi(s_j)\bigr).
\]

It relates state assertions and is not the later handbook LTL connective.
Total correctness, process accessibility, and responsiveness are instances.
The paper expressly leaves specifications requiring three or more ordered
events and quantitative response bounds beyond its two basic cases.

After ordinary reachable-state induction `(P1)`, printed p. 49 says that the
rank argument is a positive natural number but then uses `A(s',n-1)`. The
`n=1` instance therefore requires `A(s',0)`. The handbook types the formula by
taking

\[
A:S\times\{0,1,2,\ldots\}\to\mathsf{Prop}
\]

while rule instances quantify `n>0`. Allowing the zero-rank argument and
supplying the implicit universal closures are disclosed handbook typing
repairs. The current-state target and the rest of the printed rule remain
literal:

\[
\frac{
 \forall s\bigl(\varphi(s)\Rightarrow\exists n>0\,A(s,n)\bigr)
 \qquad
 \forall s,s'\ \forall n>0\,
 \bigl(A(s,n)\land R(s,s')\Rightarrow
       A(s',n-1)\lor\psi(s)\bigr)}
 {\varphi\leadsto\psi}\;(P2).
\]

The target occurrence is the current-state formula `psi(s)`, not
`psi(s')`. The paper prints only the natural-number version and refers to the
literature for extension to other well-founded sets.

Totalizing `A` at zero makes the display well typed but does not make it sound.
Even under inclusive eventuality, take `S={a,b}`, `s_0=a`,
`R={(a,b),(b,b)}`, let `varphi` hold only at `a`, let `psi` be false
everywhere, and let `A` hold exactly at `(a,1)` and `(b,0)`. The first premise
holds, and the only true positive-rank transition premise is discharged by
`A(b,0)`, although no execution state satisfies `psi`. This is a handbook
counterexample to the zero-rank totalization. One sufficient handbook repair
for inclusive eventuality would add

\[
\forall s\in S\;\neg A(s,0).
\]

Without a `psi`-state, ranks would then decrease until the transition premise
demanded the forbidden rank zero. Printed p. 49 supplies no such boundary
premise, and the handbook does not add it to P2.

Independently, literal P2 conflicts with the paper's own strict `j>i` meaning.
Take `S={a,b}`, `s_0=a`, `R={(a,b),(b,b)}`, let both `varphi` and `psi` hold
only at `a`, and let `A` hold only at `(a,1)`. Both P2 premises hold because the ranked
transition can use `psi(a)`, but no later state satisfies `psi`. This is a
handbook counterexample to the literal conjunction of the printed clauses,
not a correction attributed to Pnueli.

The same source-internal tension also appears because ER axiom A2 treats
ordinary pointwise implication as temporal implication, the later `F` includes
the present, and Theorem 3 represents temporal implication by `p => Fq`. The
author copy gives no reconciliation. A faithful reconstruction records each
clause at its printed standing rather than silently normalizing them to a
modern non-strict LTL convention.

## ER, completeness hypotheses, and program attachments

ER contains the one-step axiom A1, pointwise-implication axiom A2, invariant
frame rule R1, transitivity R2, antecedent disjunction R3, and existential
generalization R4, together with all first-order predicate-calculus theorems as
axioms. A1--R3 use ordinary state assertions. R4 needs a parameter suppressed
by the source display. Fix a nonempty set \(U\), take
\(\widehat p:S\times U\to\{\mathsf{false},\mathsf{true}\}\) and
\(q:S\to\{\mathsf{false},\mathsf{true}\}\). The hat keeps this parameterized
family distinct from the ordinary state assertion \(p\). Define

\[
\widehat p_u(s)=\widehat p(s,u),
\qquad
(\exists_U\widehat p)(s)\Longleftrightarrow
\exists u\in U\;\widehat p(s,u).
\]

The typed rule is

\[
\frac{\widehat p_u\leadsto q\quad(u\in U\text{ arbitrary})}
     {(\exists_U\widehat p)\leadsto q}\;(R4).
\]

Its premise means a derivation uniform in arbitrary `u`; `q` and every open
assumption are independent of `u`. These are parameterized state assertions,
not new tense formulas. The source prints neither their types nor the
variable-hygiene condition, so the handbook discloses both as reconstruction.

Printed p. 50 also invokes ordinary integer induction. To type it, specialize
the parameter domain to \(\mathbb N_0=\{0,1,2,\ldots\}\), put
\(\widehat p_n(s)=\widehat p(s,n)\), and require \(q\) to be independent of
\(n\). The metarule is

\[
\frac{
 \vdash \widehat p_0\leadsto q
 \qquad
 \widehat p_n\leadsto q\ \vdash\ \widehat p_{n+1}\leadsto q}
 {\vdash \widehat p_n\leadsto q\quad\text{for every }n\in\mathbb N_0}\;(I).
\]

The second premise is a derivation under the displayed temporary hypothesis for
arbitrary \(n\); `(I)` is a proof metarule, not a temporal connective. The
already defined pointwise state assertion
\((\exists_{\mathbb N_0}\widehat p)(s)\) is equivalent to
\(\exists n\in\mathbb N_0\,\widehat p(s,n)\), and the typed R4 instance yields
\((\exists_{\mathbb N_0}\widehat p)\leadsto q\).

Theorem 1 calls ER sound and complete for temporal implications. Its
completeness argument is explicitly a proof sketch. It assumes an assertion
language expressive enough to define
`P:S x N_0 -> {false,true}`, where `P_n(s)=P(s,n)` means that every execution
from `s` reaches the target within at most `n` steps. Its “bounded
nondeterminism” is pointwise finite branching:

\[
\forall s\in S\quad\{s'\in S:R(s,s')\}\text{ is finite}.
\]

No uniform numerical bound over all states is asserted. If no finite target
bound existed, Koenig's infinity lemma would yield an infinite target-avoiding
execution. The sketch uses `(I)` to derive `P_n leadsto q` for every `n`, R4
to form the pointwise assertion `s |-> exists n, P(s,n)`, and then R2 and A2.
The expressiveness and finite-branching hypotheses and the sketch boundary are
part of the theorem.

The sketch contains two independent unspoken gaps. First, the paper defines
system executions only from `s_0`, but the proof's step from `p leadsto q` to
the pointwise assertion `p(s) => exists n, P(s,n)` ranges over arbitrary
states. Let

\[
S=\{s_0,u\},\qquad R=\{(s_0,s_0),(u,u)\},
\]

let `p` hold only at `u`, and let `q` be false everywhere. The unique system
execution from `s_0` never satisfies `p`, so `p leadsto q` holds vacuously.
But the infinite path `u,u,...` avoids `q`, so `P(u,n)` is false for every
`n`; the claimed pointwise assertion fails at `u`. This system is serial and
finitely branching. The printed step therefore needs either `S=X`, a
consistent restriction of assertion and rule semantics to `X`, or a theorem
semantics quantifying over executions from every start state; none is printed.

Second, the paper defines executions to be infinite but has not assumed
seriality at this point. For `S={d}`, `R` empty, and false `q(d)`, no infinite
execution begins at `d`. The universal English definition of `P(d,0)` is
therefore vacuously true, whereas the printed base step `P(d,0) => q(d)` is
false. Seriality appears only in the later finite-state specialization. Even
after the first gap is repaired, this base step needs either an infinite
execution from every state or a nonvacuous finite-prefix or recursive
definition of `P`; neither is printed. Both defects are recorded as
source-proof gaps, not silently repaired by strengthening Theorem 1.

For a sequential program, let
`L={ell_0,...,ell_m}`, let `s_0=<ell_0,u_0>`, and assign a predicate
`q_ell:D -> Prop` to every location `ell in L`. The integer notation `q_i`
is only an abbreviation for `q_{ell_i}`; location indexing is required because
`N(ell,u)` returns an element of `L`. Substituting the control-point attachment
into P1 *reduces the desired invariant proof to* the premises

\[
q_{\ell_0}(u_0),
\qquad
\forall\ell\in L\ \forall u\in D\,
\bigl(q_\ell(u)\Rightarrow
q_{N(\ell,u)}(T(\ell,u))\bigr).
\]

P1 yields invariance only after they have been proved. The finite-path
intermittent-assertion presentation similarly decomposes a path into finitely
many A1 instances and composes them with R2.

For two concurrent programs, choose finite index sets `I,J` and enumerate
`L_1={ell_i:i in I}` and `L_2={m_j:j in J}`. For every pair, take
`h_ij:D -> Prop`. The full attachment is the metalinguistic representation

\[
q_{\rm full}(\pi_1,\pi_2;u)=
\bigwedge_{i\in I}\bigwedge_{j\in J}
(((\pi_1=\ell_i)\land(\pi_2=m_j))\Rightarrow h_{ij}(u)).
\]

It represents one global assertion rather than a different program semantics
and contains `|I||J|` pair-indexed components. The partial attachment instead
takes typed families `p_i:L_2 x D -> Prop` and
`q_j:L_1 x D -> Prop` and has the representation

\[
q(\pi_1,\pi_2;u)=
\bigwedge_{i\in I}((\pi_1=\ell_i)\Rightarrow p_i(\pi_2,u))
\land
\bigwedge_{j\in J}((\pi_2=m_j)\Rightarrow q_j(\pi_1,u)).
\]

It reorganizes the global assertion into two location-indexed families, each
of which may still mention the other process's location. Loose interaction can
give `|I|+|J|` top-level assertions. Strong interaction can recover
`|I||J|` cases, the full two-process product; this is product or quadratic in
the two displayed location-set sizes, not by itself exponential. For a varying
number of processes, the analogous product `prod_h |L_h|` can grow
exponentially in the process-count parameter. That is the precise
parameterization of the source's informal exponential-complexity sentence.
Global arithmetic invariants can avoid materializing the full cross-product
attachment, but their initial truth and preservation under every relevant
processor transition must still be proved.

For the producer--consumer calculation, take a positive integer `C` for the
source's capacity `N`, `b:S -> Z` for its load `n`, and `mu,e,f:S -> N` for the
source semaphore values `MUTEX`, `IS_EMPTY`, and `IS_FULL`. This renaming
prevents collision with the next-location map `N`. Let
`m_i,r_i,s_i:S -> {0,1}` be the source's three location indicators for process
`i`. The printed calculation says they are one on some control locations and
zero elsewhere but does not enumerate those support sets. It uses only these
indicator consequences: simultaneous critical-region membership gives
`m_1=m_2=1`; conversely, `m_i=1` means process `i` is at its critical-section
location and therefore is not waiting on a semaphore operation; a process `i`
blocked on `MUTEX` gives `m_i=0` and `mu=0`; and simultaneous
producer/consumer waits on `IS_EMPTY`/`IS_FULL` give
`r_1=r_2=e=f=0`. Together with `0<=s_i<=r_i<=1`, these are all the support
facts used by the reconstruction; no unprinted location set is inferred.
Pointwise on reachable states, the printed invariants are

\[
\begin{aligned}
m_1+m_2+\mu&=1,\\
r_1+r_2+e+f&=C,\\
s_1+s_2+e&=b,
\end{aligned}
\qquad 0\le s_i\le r_i\le1.
\]

If both processes occupy their critical regions, the first equation forces
`mu=-1`, contradicting semaphore nonnegativity. The third equation gives
`b>=0`, while
`b=s_1+s_2+e <= r_1+r_2+e = C-f <= C`. A processor blocked on the mutex has
its corresponding `m_i=0` and `mu=0`; the first invariant gives
`m_{3-i}=1`, whose stated meaning puts the other process in its critical region
and shows it is not blocked. In the remaining
simultaneous-wait case the producer waits on `IS_EMPTY` and the consumer on
`IS_FULL`, giving `r_1=r_2=e=f=0`; the second invariant forces `C=0`, contrary
to positive capacity. The printed calculation therefore proves mutual
exclusion, `0<=b<=C`, and absence of deadlock under `C>0`.

## Future-only tense calculus and quantified schemata

For an execution `sigma=s_0s_1...`, `H(t,p)=p(s_t)` is the source's
metalinguistic evaluation abbreviation for an atemporal state assertion. It is
not an object-language operator. For nested propositional tense formulas, the
typed recursive clauses are

\[
\begin{aligned}
(\sigma,n)\models p &\Longleftrightarrow p(s_n),\\
(\sigma,n)\models FA &\Longleftrightarrow
  \exists t\ge n\,(\sigma,t)\models A,\\
(\sigma,n)\models GA &\Longleftrightarrow
  \forall t\ge n\,(\sigma,t)\models A,
\end{aligned}
\]

with the ordinary recursive Boolean clauses. Both `F` and `G` include the
present; no next or until operator occurs. The source defines
`FA := not G not A`. For a system formula, the source identifies the absolute
present with the initial state `s_0`; the recursion also evaluates formulas at
later positions.

The pure propositional basis contains G1--G3, the rule RT admitting classical
tautologies, modus ponens (MP), and generalization
`vdash A / vdash GA` (RG). In the handbook, `K_b` denotes exactly this theorem
system together with the derived abbreviation `FA := not G not A`. It is a
theorem system, not a formula class or model class, and it does not include the
later system-dependent rules E, I1, I2, N, P, or MRG. This exact standing is
needed to assess Theorems 2, 3, and 5 and distinguishes `K_b` from both ER and
the later GPSS systems DX and DUX. The dual definition gives
the displayed derived formulas

\[
A\Rightarrow FA\;(F2),
\qquad
FFA\Rightarrow FA\;(F3).
\]

For the source's formula metavariable `p`, with object variable `x` free,
printed p. 53 adds the exact source schemata

\[
\begin{aligned}
G(\forall x\,p)&\Longleftrightarrow\forall x\,Gp &(Q1),\\
F(\exists x\,p)&\Longleftrightarrow\exists x\,Fp &(Q2),\\
F(\forall x\,p)&\Rightarrow\forall x\,Fp &(Q3),\\
\exists x\,Gp&\Rightarrow G(\exists x\,p) &(Q4).
\end{aligned}
\]

These are proof schemata. The paper does not state whether `p` must be
atemporal or may contain `F/G`, and it supplies no separate domain-semantics
discussion. The source's schema range is therefore left unresolved. Any later
handbook use is conservatively limited to atemporal instances; that is a
handbook policy, not a restriction attributed to the source. Theorem 2 is
expressly limited to the pure propositional future-restricted `K_b` fragment.
It calls that fragment complete in the absolute sense and decidable, but points
outward for the complete proof and invokes S4 correspondence for decidability.

The completeness assertion is model-class-sensitive. The preceding recursion
evaluates formulas on a single linearly ordered execution, while S4 permits
arbitrary reflexive-transitive branching frames. The handbook formula

\[
(Fp\land Fq)\Rightarrow
\bigl(F(p\land Fq)\lor F(q\land Fp)\bigr)
\]

is valid on every linear future by comparing a future `p`-position with a
future `q`-position. Under the S4 accessibility reading of `F`, it fails in the
Kripke model

\[
M=(W,\rho,V),\qquad
W=\{r,u,v\},
\]

with

\[
\rho=\{(r,r),(u,u),(v,v),(r,u),(r,v)\},
\qquad V(p)=\{u\},\quad V(q)=\{v\}.
\]

The relation is reflexive and transitive; `u` and `v` are incomparable and
have no successors other than themselves. The root `r` satisfies neither atom
but satisfies `Fp and Fq`; no accessible world satisfies either `p and Fq` or
`q and Fp`. Thus the S4 referral does not establish completeness for the
displayed linear-execution semantics. The paper does not reconcile the two
readings, so the handbook records Theorem 2 as a model-class-unresolved source
assertion. Reference [29] is said to contain complexity results, but this paper
states no bound or complexity class.

RG is unrestricted only in the pure propositional basis just listed. The
source warns that when other means introduce facts true only at the present,
generalization must be restricted. The finite-state MRG rule below makes that
warning exact.

## Action fairness and system-dependent rules

Printed p. 53 partitions the transition relation into finitely many action
relations. Writing that partition as

\[
\mathcal A=\{a_1,\ldots,a_k\},
\qquad R=\bigcup_{h=1}^k a_h,
\qquad a_h\cap a_\ell=\varnothing\quad(h\ne\ell),
\]

the added restriction on the execution class is

\[
\forall a\in\mathcal A\ \forall i\ge0\
\exists j\ge i\ a(s_j,s_{j+1}).
\]

This is the literal negation of the source's “some action is indefinitely
delayed” tail condition, so every action occurs infinitely often. It is
distinct from the earlier enabled-processor prose.

The system-dependent rules I1 and I2 internalize invariance, E internalizes a
one-step eventuality, and N internalizes an inevitability step for a designated
\(a\in\mathcal A\). N's conclusion ranges only over executions satisfying the
displayed action-occurrence restriction. Without that restriction, its local
premises are not sound for `p => Fq`: a raw path can perpetually take another
action.
The proof method therefore has a system-specific phase establishing transition
and fairness premises and a pure tense-logical phase.

Printed p. 54 adds two derived strengthenings used in Example 2. With all state
variables universally closed, their typed forms are

\[
\frac{
 \forall s\,(p_1(s)\Rightarrow q(s))
 \qquad
 \forall s,s'\,
 (q(s)\land p_2(s')\land R(s,s')\Rightarrow q(s'))}
 {\vdash(p_1\land Gp_2)\Rightarrow Gq}\;(DI),
\]

\[
\frac{
 \begin{gathered}
 \forall s,s'\,
 (p_1(s)\land R(s,s')\land\neg a(s,s')\land p_2(s')
   \Rightarrow p_1(s'))\\
 \forall s,s'\,
 (p_1(s)\land a(s,s')\land p_2(s')\Rightarrow q(s'))
 \end{gathered}}
 {\vdash(p_1\land Gp_2)\Rightarrow Fq}\;(DN).
\]

DI and DN are derived from I2 and N, respectively, rather than primitive
axioms. Their `Gp_2` side condition is used in Example 2: DI preserves the
displayed future condition through the accessibility argument, and DN turns
the designated action into the target eventuality.

Theorem 3 says `K_b` is at least as strong as ER. Its complete printed proof is
only a skeletal instruction: represent `p leadsto q` as `p => Fq`, then assert
that every ER axiom can be shown to be a theorem of `K_b`. Under the exact pure
system just defined, that assertion is under-specified: translated A1 requires
the system-dependent rule E, which is not a rule of bare `K_b`, and the paper
does not say whether Theorem 3 tacitly adds E or any of I1, I2, and N. No
individual ER derivation is printed. The following relative-completeness
corollary is therefore recorded as an unresolved source assertion, not as a
verified embedding theorem for bare `K_b`.

## Finite-state decision package

Printed p. 55 assumes `S` finite and, for simplicity, excludes halting states
and deadlocks:

\[
\forall s\in S\ \exists t\in S\,R(s,t).
\]

Thus no state is terminal, and every finite `R`-path can be extended to an
infinite execution. For any `s in S`, an infinite `R`-path from `s` is a
sequence `rho=t_0t_1...` with `t_0=s` and `R(t_i,t_{i+1})` at every index. It
satisfies the action condition exactly when

\[
\forall a\in\mathcal A\ \forall i\ge0\
\exists j\ge i\ a(t_j,t_{j+1}).
\]

This arbitrary-start path property is needed for the continuation test in
Theorem 4. A proper execution of `Sigma` is such a path beginning at `s_0`.
Because finite-system validity is restricted to those initial-state paths,
the handbook defines

\[
\Sigma\models_{\rm prop}A
\Longleftrightarrow
\forall\sigma\in S^\omega
(\sigma\text{ proper for }\Sigma\Rightarrow(\sigma,0)\models A).
\]

This is a semantic system/formula relation, not a formula connective, and is
used to state both finite-system theorems.

Theorem 4 decides `Sigma |=_prop G(p => Fq)` for arbitrary state assertions
`p,q`. The
source's sufficient route checks every `p`-state. Restricting the graph first to
states reachable from `s_0` gives the exact initial-state version, but that
pruning is a disclosed handbook observation rather than source wording.

After deleting all `q`-states, the source says to label a strongly connected
component by actions occurring on edges among its constituent states, but it
prints neither a set formula nor the two-direction proof. The handbook
formalizes that sentence as follows: an infinite `q`-avoiding path from a
relevant `p and not q` state `s` which satisfies the action condition exists
exactly when a reachable cyclic strongly connected component `C` satisfies

\[
a\cap(C\times C)\ne\varnothing
\qquad\text{for every }a\in\mathcal A.
\]

The equivalence proof is handbook-supplied. Choose one internal edge of every
action relation. Strong connectivity supplies finite paths joining the head of
each chosen edge to the tail of the next and the last back to the first; repeat
that closed walk. Conversely, an infinite path through the finite acyclic
condensation graph eventually remains in one component, and its
action-satisfying tail supplies every required internal action edge. This is
the explicit formalization of the source's component-label sentence, not a
literal source display.

The finite-system proof calculus adds the initial-state rule

\[
\frac{p(s_0)}{\vdash p}\;(P)
\]

and replaces unrestricted RG by

\[
\frac{\vdash A}{\vdash GA}\;(MRG),
\qquad
\text{only when the proof of }\vdash A\text{ used no instance of }(P).
\]

P admits system-specific initial truth. MRG is necessary: on
`s_0 -> s_1 -> s_1`, with `p` true only at `s_0`, P yields `p`, while
unrestricted generalization would yield the false `Gp`. Theorem 5 has two
clauses: for every propositional tense formula `A`, whether
`Sigma |=_prop A` holds is decidable; and whenever it holds, `A` is derivable
in the `K_b` calculus extended by the system-dependent axioms, P, and MRG. The
paper asserts the adequacy clause but prints no general derivation construction.
Appendix B addresses only the decidability clause.

## Appendix proof ownership and decision boundary

Appendix A says that the following T2 and T3 formulas are proved in reference
[23] and prints their adjacent corollaries:

\[
\begin{aligned}
Gp\land Fq&\Rightarrow F(p\land q) &(T2),\\
Gp\land Fq&\Rightarrow F(Gp\land q) &(corollary),\\
F(p\lor q)&\Rightarrow Fp\lor Fq &(T3),\\
Gp\land Gq&\Rightarrow G(p\land q) &(corollary).
\end{aligned}
\]

Pnueli does not reprove T2 or T3. The appendix separately prints a local
six-step proof of

\[
\frac{\vdash(p\land G\neg q)\Rightarrow Fq}
     {\vdash p\Rightarrow Fq}.
\]

Its steps are the assumption; excluded middle for `Fq`; replacement of
`not Fq` by `G not q`; the tautology `(p and Fq) => Fq`; combination of the
two cases with the assumption; and the final consequence. The local proof is
not transferred to the externally owned T2/T3 results.

Appendix B discusses two semantic decision routes for Theorem 5's decidability
clause: reintroduce explicit time and reduce to monadic second-order theory of
successor, or use languages of infinite state words. Define

\[
L_{\rm prop}(\Sigma)
=\{\sigma\in S^\omega:\sigma\text{ is a proper execution of }\Sigma\}.
\]

This defined language states the source's inclusion question without supplying
an automaton tuple that the paper does not print, and it avoids collision with
the action partition. Pnueli locally asserts that a finite-state infinite-word
acceptor for exactly this language can be constructed, but prints no tuple,
acceptance condition, construction, or proof. That assertion is not assigned
to reference [32].

For an atemporal assertion `p`, identify each state `s in S` with the
one-letter word `(s) in S^1 subseteq S*`, and put
`[[p]]={(s) in S^1:p(s)}`. For `U subseteq S*` and `V subseteq S^omega`, prefix
concatenation is `UV={uv:u in U, v in V}`. The exact printed recursion is

\[
\begin{aligned}
L(p)&=\llbracket p\rrbracket S^\omega,\\
L(\neg W)&=S^\omega\setminus L(W),\\
L(W_1\land W_2)&=L(W_1)\cap L(W_2),\\
L(W_1\lor W_2)&=L(W_1)\cup L(W_2),\\
L(FW)&=S^*L(W),\\
L(GW)&=L(\neg F\neg W).
\end{aligned}
\]

The source's imported label “omega-regular” is used in the handbook only as
the eliminable metalinguistic abbreviation “accepted by some nondeterministic
Büchi word automaton under Definition `def:p09-omega-automata`.” It names a
class of infinite-word languages, not a new automaton, and is needed only for
the cited closure and inclusion route. Reference [32] accompanies the imported
omega-regular language machinery used for the recursion and effective closure
step. Reference [33] supports the decision of

\[
L_{\rm prop}(\Sigma)\subseteq L(W).
\]

The local acceptor assertion is unproved here; the imported language/closure
machinery and inclusion decision are likewise not proved in this paper. Pnueli
prints the recursion and route, not a later LTL-to-Büchi translation or a
complexity classification.

## Reader-facing disposition

The former metadata-only boundary is obsolete because the full author-hosted
body has been read. The repaired N-c-012.b presentation now covers the exact
program and execution model; P2's disclosed zero-rank typing repair, its
independent zero-boundary and strict-future counterexamples, and the unprinted
false-at-zero repair premise; P1/P2, typed ER parameter families, and the
induction metarule;
Theorem 1's proof gaps and completeness hypotheses; exact typed full and partial
attachments with parameterized size claims; the positive-capacity
producer--consumer calculation and its explicit indicator facts; future-tense
calculus; unresolved Q1--Q4 schema range and Theorem 2 model class; I1/I2/E/N
and derived DI/DN;
Theorem 3's skeletal proof; arbitrary-start action-condition paths,
initial-state proper executions, and restricted system validity; the
handbook-supplied SCC formalization; Theorem 5's unproved adequacy assertion;
Appendix B's one-letter-word typing; and Appendix A/B proof ownership.

The individual `N-c-012.b` review later reached unanimous acceptance after a
sixth repair round. A subsequent integrated review exposed one further
presentation boundary: bare \(K_b\) had to be defined as the pure G1--G3 and
RT/RG/MP theorem system, and the claimed ER comparison had to remain
under-specified because translated A1 requires system rule E. That correction
is now present in the actual manuscript and this note. In integrated Round 5,
three fresh blind seats read the complete actual `n-c-012.tex` and the relevant
host-chapter LaTeX; all returned **ACCEPT**. The
[integrated review record](p09-n-c-012-integrated-independent-review-record.md)
preserves the scope and determination. No manuscript PDF or page image supplied
evidence. The IEEE-direct comparison, Part IX, the final post-freeze layout
pass, human review, final-book completion, and user acceptance remain open.
