# Edition 2026 C2: CSL interval and jump-time correction

Date: 7 September 2026. Status: operative manuscript correction and subsequent
annex integration implemented; author read-back complete. Independent
mathematical/source review has not been represented as passed by this author.

## Ownership, input evidence and checkpoint

Owned manuscript surface: the CTMC/CSL definition, interval/algorithm treatment,
and directly dependent CSL boundary rows in
`handbook/parts/p09/logic-in-computer-science.tex`. No other source, bibliography,
style, register, or presentation file was edited. In particular, the concurrent
EL++ correction in `n-c-010.tex` is outside this task.

The manuscript before this task had SHA-256
`d4de787e1505bcb79f10f3257b88dbbed47edbafbfdba0ca739bcd47def10ddd`.
The existing dirty worktree was preserved.

Read before implementation: host lines 1265–1465, 2315–2340 and 2410–2440;
the CSL authority passage in `presentations/n-x-015.tex`, lines 147–181;
`spec/inventory/2026-09-06/additional-current-content-findings.md`, especially
INV-CSL-001; and `spec/research/p09-source-presentations-lot4.md`, lines
2210–2285. The operative insertion was subsequently read back in full.

The first manuscript patch was saved at 13:26 UTC, within the first fifteen
minutes of the block that began at 13:16 UTC. This note is the companion
checkpoint. Exact final line ranges and manuscript hash are recorded below
after the final read-back.

## 1. Confirmed defect INV-CSL-001: unrestricted closure

Original host lines 1365–1369 admitted nonempty flagged real-time intervals
and asserted that replacing any such interval by its closure preserves path
probability. That assertion is false for until because the witness time is
existential and may be zero; it is not simply a random residence time.

Let the chain have a single absorbing state s, with p true. The only path is
constant. For false U^(0,1] p, any witness t>0 requires false at u=0, so its
probability is 0. For false U^[0,1] p, t=0 is a witness with no earlier-time
obligation, so its probability is 1. The threshold at 1/2 changes truth value.
The manuscript now states and derives these probabilities directly.

## 2. Newly confirmed adjacent defect C2-JUMP-001

Original host lines 1342–1345 used the least i with
t <= sum_(j=0)^i tau_j. This selects the departing state at a jump time.
Combined with the strict earlier-time condition in the active strong-until
clause at lines 1377–1380, it invalidates ordinary first-entry reachability.

Take two states s,g, R(s,g)=r>0, all other rates zero, A={s}, B={g}.
For a path whose first jump is T>0, the old occupation map has s at T.
No t<T has B; t=T still has s; and every t>T has a prior u in (T,t) at g,
which violates A. Thus the old convention gives probability zero even for
A U^[0,b] B, whereas the stated transient/reachability procedure gives
1-exp(-r*b). This discrepancy is not a null-event modification: the witness
can be the random jump time itself.

The operative definition now uses T_0=0, T_i=sum_(j<i) tau_j and
pi@t=s_i for T_i <= t < T_(i+1); the final absorbing state is occupied for
all t >= T_k. The first entry into B can therefore witness strong until.
The note records the historical convention separately; the corrected reader
does not claim that its inequality is the source's identical printed wording.

The same edit makes path feasibility and finite prefixes explicit: every
prescribed step has positive rate, all prefix states through s_k are fixed,
the empty prefix has probability 1, and infeasible prefixes have probability
0. Infinite paths are restricted to the full-measure time-divergent set.

## 3. Exact retained endpoint law

Fix a finite CTMC and already interpreted state formulas Phi,Psi. Put
A=Sat(Phi), B=Sat(Psi), and u_I(s)=Pr_s(Phi U^I Psi). The finite lower
endpoint a is nonnegative, the upper bound b is finite or infinity, and
infinity is never a witness time.

For a nonempty, nondegenerate interval I with a<b, let J=[a,b] if b is finite,
and J=[a,infinity) otherwise. The proved normalization is

    u_I(s) = 1_A(s) u_J(s), if a=0 and 0 is excluded from I;
             u_J(s),       otherwise.

This is an equality of probabilities, not equality of all path sets. It does
not assert that arbitrary removal of a singleton has zero effect.

### Proof of the probability qualification

A Poisson clock of rate lambda >= max_s E(s), lambda>0, with acceptance
probability E(s)/lambda and successor distribution P(s,.) realizes the chain.
The survival probability before an accepted tick is

    sum_n exp(-lambda*t) (lambda*t)^n/n! (1-E(s)/lambda)^n
      = exp(-E(s)*t).

Rejected ticks are not actual path steps. At E(s)=0 there are no accepted
ticks. There are finitely many ticks on bounded intervals almost surely, and
no tick at a fixed positive time. Hence there is a full-measure set of paths
locally constant on both sides of the finitely many positive finite endpoints
under consideration.

On that set, a witness at an excluded positive upper endpoint can move
slightly earlier. A witness at an excluded positive lower endpoint can move
slightly later: the prior-time condition and local constancy force A at the
lower endpoint, and both A and B persist for a short time. At lower endpoint
zero, the later-witness argument requires the initial state to belong to A.
If it does not, all positive witnesses fail already at u=0. This proves the
displayed normalization for every endpoint-flag combination with a<b.

### Degenerate and absorbing cases

- u_[0,0](s)=1_B(s), with no requirement s in A.
- For a>0, u_[a,a](s) is the probability of B at a and A at all u<a.
  It can be positive or 1; it is not generally a first-entry atom.
- A flagged interval with equal endpoints and an excluded endpoint is empty.
  The grammar admits only nonempty intervals; if an algorithm produces an
  empty one, its until/next probabilities are 0 before any normalization.
- A constant absorbing path at a state in A intersect B has singleton-until
  probability 1 for every a>=0.
- A constant absorbing path at B minus A has until probability 1 precisely
  when time zero belongs to the interval; otherwise its probability is 0.
- Timed next has probability 0 at every absorbing state, because no next step
  exists, regardless of the label or interval.

## 4. Endpoint-aware computation and direct correctness argument

For C subset S, retain the original rate row at s in C and replace it by zero
otherwise. Call this R_C and put Q_C=R_C-diag(E_C). Thus states outside C
are absorbing. Let D_A=diag(1_A) and use probability columns

    v_t = exp(Q_(A minus B)*t) 1_B.

A and B are evaluated in the original chain and remain fixed; nested CSL
state formulas are not reevaluated after a rate transformation. Until vectors
are columns, whereas the initial distribution in the uniformization formula
is explicitly a row. Zero-time matrix evolution uses the identity exactly.

Then

    u_[0,b] = v_b                           (b>=0),
    u_[a,b] = exp(Q_A*a) D_A v_(b-a)         (0<a<=b<infinity).

For h, the ordinary unbounded-until vector, set h=1 on B and h=0 outside
A union B and at absorbing states outside B. On the remaining positive-rate
states take the least nonnegative solution h_s=sum_t P(s,t)h_t. Then

    u_[0,infinity) = h,
    u_[a,infinity) = exp(Q_A*a) D_A h        (a>0).

For nondegenerate intervals excluding zero, apply D_A on the left to the
corresponding closed-lower-bound vector. No unproved endpoint erasure is used.

The first modified chain follows the original until success in B or failure
outside A union B, then freezes. Its transient mass on B is the bounded-until
probability. For a>0, the first phase must preserve A until a; fixed-time
jumps at a are a null event, so multiplying exp(Q_A*a) by D_A removes exactly
the failed prefixes. States in A intersect B must remain active in this first
phase: an early visit to B is not yet a valid lower-bounded witness. The Markov
property at a gives the second phase. Replacing its bounded reachability by h
gives the infinite-upper-bound formula. These derivations are supplied in the
actual manuscript rather than imported as a claim of literal source identity.

For a=b>0 the matrix expression is exp(Q_A*a)1_(A intersect B). For a=b=0
it is 1_B. In the two-state example A={s}, B={g}, it gives
u_[a,b](s)=exp(-r*a)-exp(-r*b) for 0<a<=b, so u_[a,a](s)=0. With A=S,
the same positive-time singleton has probability 1-exp(-r*a), because earlier
entry into g is permitted while A continues to hold. The active text gives
both cases.

For timed next, when E(s)>0 the probability is

    (exp(-E(s)*a)-exp(-E(s)*b)) sum_(t in B) P(s,t),

with the second exponential zero at b=infinity. It is 0 when E(s)=0.
This follows by conditioning on the first successor and integrating its
exponential waiting-time density. Endpoint flags do not affect next's
probability, and every singleton gives 0.

## 5. Primary-source evidence and version limits

The registered journal article is Baier, Haverkort, Hermanns and Katoen,
*Model-Checking Algorithms for Continuous-Time Markov Chains*, IEEE TSE
29(6) (2003), 524–541, DOI
[10.1109/TSE.2003.1205180](https://doi.org/10.1109/TSE.2003.1205180).
The [author's institutional record](https://iccl.inf.tu-dresden.de/web/Article2484194115/en)
and the [Twente journal record](https://research.utwente.nl/en/publications/model-checking-algorithms-for-continuous-time-markov-chains/)
confirm that identity and 18-page extent.

The bibliography's linked
[37-page file](https://ris.utwente.nl/ws/files/268940692/Baier2002model_checking.pdf)
belongs to the separately identified
[April 2002 CTIT report 02-10](https://research.utwente.nl/en/publications/model-checking-algorithms-for-continuous-time-markov-chains-2/).
Its web extraction is garbled, screenshot requests timed out, and an ordinary
in-memory HTTP read returned 403 in this pass. No local source copy was
created and no body reading is inferred from this failed route.

A public [article-text rendering](https://www.researchgate.net/publication/3188342_Model-checking_algorithms_for_continuous-time_markov_chains)
was inspected at Definition 3 (path occupation), Definition 6 (until), the
opening of Section 4 (closure assertion), and Section 4.2 (transient reductions).
The rendering displays a journal-layout manuscript with a July/issue-7 running
header, while the authoritative publication is June/issue 6. It is therefore
not asserted byte-identical to the final journal file. Its path/closure
wording is historical evidence, not a substitute for the direct correctness
proof above and not a claim that a final-journal erratum was established.

The new endpoint theorem and jump-time correction are handbook derivations.
The reader retains attribution of the underlying CTMC/CSL framework and
transient algorithms to the registered source without calling the corrected
conventions its identical original wording. The existing source note at
`p09-source-presentations-lot4.md:2248–2262` records earlier source-locator
reconciliation; its report/journal comparison is not newly repeated here.

## 6. Remaining verification boundaries

Uniformization still supplies a Poisson truncation bound, and separate bounds
are required for the retained terms and floating-point error. Error intervals
must propagate through the nonnegative matrix operations and projections.
Numerical refinement alone is not claimed to decide exact equality with a
threshold. No new general CSL decidability proof or full source-paper audit
is claimed.

The dependent comparison row and complexity row retain endpoint flags and the
time-zero condition. The existing `n-x-015.tex` authority passage states only
closed bounds [0,t] and [a,b], and its top-until example remains correct; it
was read but not edited.

No manuscript builds, manuscript renders, software test suites or subagents
were used. No independent review pass is declared. The next step is a bounded
independent reading of the actual changed definitions, endpoint proof and
matrix decomposition, especially the positive singleton and absorbing cases.

## 7. Final author checkpoint, 13:36 UTC

Frozen author result for `handbook/parts/p09/logic-in-computer-science.tex`:

`96730f47c816df9800191700a280ebb6db0041f5415fe05c569225a62b9ad822`

Actual final locations:

| Surface | Lines / stable label |
| --- | --- |
| Corrected paths, prefixes and flagged CSL input | 1318–1405; `def:p09-ctmc-csl` |
| Restricted endpoint law, proof, absorbing counterexample | 1407–1479; `sec:p09-csl-endpoints` |
| Explicit matrix/embedded-chain computations, direct proof, singleton examples, timed next and numerical boundary | 1481–1609; `thm:p09-csl-model-checking` |
| Dependent comparison-table cell | 1622–1625; `tab:p09-probabilistic-model-checking` |
| Dependent CSL complexity/boundary row | 2497–2501 |

The complete changed section was read back, and every later mathematical/type
clarification and formatting change was reread in the actual LaTeX. The manual
case analysis covered: all four absorbing A/B membership combinations;
excluded zero versus included zero; positive open/closed endpoints;
empty intervals; zero and positive singletons; first entry into B minus A;
persistent B occupation when A includes B; positive rate self-loops; and
the first phase's requirement to keep A intersect B active.

Read-only evidence hashes at this checkpoint:

| Evidence | SHA-256 |
| --- | --- |
| `spec/inventory/2026-09-06/additional-current-content-findings.md` | `99e6cae1c50c694a02790fd6eda49df8f9b2a182ab6294209bb6413c80f0336f` |
| `spec/research/p09-source-presentations-lot4.md` | `75ebab01d35f3befc6b52afadfb03c6f663f13712f2ea0da5c92d4eab6061b56` |
| `handbook/parts/p09/presentations/n-x-015.tex` | `29c172d5ba714ea89e99f4272bd4b87aa2b72bc3d305447ba43ede5289c69e08` |
| `spec/EDITION-2026-CONTRACT.md` | `c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3` |

Own writes are confined to the listed CTMC/CSL surfaces and this new note.
The final-journal body comparison, general exact threshold-equality questions,
and independent review remain distinct boundaries. No mathematical defect is
retained in the active endpoint rule with an instruction to reinterpret it.

## 8. Separate annex-integration correction, 13:55 UTC

The initial mathematical patch placed two new editorial proof environments in
the host. The retained structural rule requires such proofs in an annex. This
follow-up changes their location and theorem packaging, not their mathematical
content. The 13:36 hash and ranges above remain the historical initial patch;
the following identities describe the integrated result.

### Statements, exact proof preservation and links

| Body statement | Status and annex destination | Exact annex back-reference |
| --- | --- | --- |
| `thm:p09-csl-endpoints` | `proved=annex:p9.csl.1` | `annexitem{annex:p9.csl.1}{thm:p09-csl-endpoints}` |
| `thm:p09-csl-interval-computations` | `proved=annex:p9.csl.2` | `annexitem{annex:p9.csl.2}{thm:p09-csl-interval-computations}` |

The existing `sec:p09-csl-endpoints`, `def:p09-ctmc-csl`, and
`thm:p09-csl-model-checking` labels are preserved. The last of these remains
`cited=BaierHaverkortHermannsKatoen2003`; its Volterra and steady-state source
results have not been promoted to locally proved results. The annex explicitly
identifies the embedded-chain characterization of h as a cited dependency.

Both complete proof blocks, including their begin/end commands and the second
block's optional proof title, were relocated verbatim. Exact UTF-8 hashes:

| Proof block | Lines | SHA-256 before and after relocation |
| --- | ---: | --- |
| Endpoint rule | 30 | `853846773f1a7998a139b98f3843a1bfa5dd21b477ccf31b496b2a0d9fa1bb3e` |
| Interval computations | 24 | `19a752949f13216cf34ca8f853c32387aa9030587ab46d24551727904bfd3c2d` |

The endpoint and two-state examples remain in the host outside the local
theorems. The timed-next formula remains a separately cited computation, with
its conditioning explanation preserved in the annex. Uniformization, numerical
error and exact-threshold boundaries likewise remain outside the local proved
theorems, with their original source qualifications. No proof was replaced by
a citation or shortened.

### Integrated files and hashes

| File | SHA-256 |
| --- | --- |
| `handbook/parts/p09/logic-in-computer-science.tex` | `1eaf705ced9c83e18edd1129f0f0996663840fdfd5b22bee411b871eb3d85dd3` |
| `handbook/annex/p09/csl-corrections.tex` | `92aeada76892a0dbf271b8002dca189d563ba39c389ebb478be3d438521c42f5` |
| `handbook/annex/p09.tex` | `47a28fa80f2cad42054c36628815326f9898036c58fafaff876e3703c154cb15` |

The body endpoint theorem is at lines 1410–1439; the original cited theorem is
at 1454–1470; the local computation theorem is at 1475–1508. The annex contains
the two items starting at lines 6 and 41, with the verbatim proof blocks at
9–38 and 49–72. The single new input is `annex/p09/csl-corrections` at driver
line 6.

The updated body and full annex were read. Both forward status targets and
reverse annex-item targets agree exactly. The host now contains zero proof
environments. Restoring the saved pre-relocation C2 section in memory recovers
the exact original host hash
`96730f47c816df9800191700a280ebb6db0041f5415fe05c569225a62b9ad822`, confirming
that the relocation did not alter other host material. Removing the one added
driver input in memory recovers its original hash
`6012fb0c7577081822c68790c7d293ecf409e5a085f5483ff8eca52338bc9cbd`.

This follow-up writes only the assigned C2 host surface, new annex fragment,
one driver input and this note. C1 is untouched. No full-book build, render,
test infrastructure or independent mathematical-review result is claimed.
