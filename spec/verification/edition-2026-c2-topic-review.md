# C2 topic-specialist mathematical review

Date: 2026-09-07. Reviewer task: `/root/edition_c2_topic_review`.

## Verdict

**PASS for the scoped mathematical correction.** The right-continuous path semantics, endpoint normalization theorem, interval-computation theorem, annex derivations, examples, and numerical qualifications agree on the reviewed snapshot. I found no counterexample to either local theorem and no mathematical defect requiring a correction within this scope.

The result is a mathematical text review of C2. It does not establish exact source identity, identical wording with the cited source, a total numerical procedure for deciding every equality case, whole N-x-015 acceptance, build success, rendered-page quality, or publication acceptance. The source identity qualification remains separate.

## Reviewer configuration and instructions

The assignment was an independent topic-specialist mathematical review in `C:/Dev/the-methods-of-reason`, limited to the actual CTMC/CSL definition, the two local correction theorems, examples, numerical boundaries, following comparison, dependent CSL complexity row, all of the correction annex, and the matching annex driver. The required challenges were right-continuous jump occupation; feasible and time-divergent paths; interval normalization including excluded zero, empty and singleton intervals; absorbing and rate-self-loop cases; the survival mask `D_A`; `Q_A` versus `Q_(A\B)`; finite and infinite bounds; timed next; nested formulas evaluated in the original chain; numerical error propagation; and threshold equality.

I was instructed to derive correctness from the actual semantics, treat the corrections as handbook derivations with source boundaries, avoid other reviewers' reports and author conclusions, run no software tests or manuscript build or render, create no subagents, and write only this report using `apply_patch`. I followed those restrictions. The time allowance was at most 45 minutes with a checkpoint at 15 minutes; this review was completed before that checkpoint became due. An interim mathematical finding was sent to the parent during the review.

The active task identity and assigned reviewer role are exposed. The actual inference model identifier/version, reasoning-effort setting, sampling parameters, and runtime configuration are **unavailable** to this reviewer. Tool metadata listing available models does not establish which model executed this review.

No `AGENTS.md` was found at the checked filesystem ancestors or at the root, `handbook`, `handbook/parts`, `handbook/parts/p09`, `handbook/annex`, `handbook/annex/p09`, `spec`, or `spec/verification` directories. The task's supplied instructions governed the review. Earlier memory was consulted only for the general distinction between a frozen text review and later acceptance gates; historical acceptance was not used as evidence for C2.

## Snapshot and complete read record

Repository root: `C:/Dev/the-methods-of-reason`. Branch: `phase4-codex`. HEAD: `35d537c692bb74b532dc4aa750da381a7fe4daf2`. The working tree contains extensive existing changes. The hashes below identify the actual reviewed files, independently of HEAD.

| File | SHA-256 | Complete contiguous ranges actually read |
| --- | --- | --- |
| `handbook/parts/p09/logic-in-computer-science.tex` | `1eaf705ced9c83e18edd1129f0f0996663840fdfd5b22bee411b871eb3d85dd3` | 1300–1620 and 2434–2464 |
| `handbook/annex/p09/csl-corrections.tex` | `92aeada76892a0dbf271b8002dca189d563ba39c389ebb478be3d438521c42f5` | 1–82, the entire file |
| `handbook/annex/p09.tex` | `47a28fa80f2cad42054c36628815326f9898036c58fafaff876e3703c154cb15` | 1–6, the entire file |

The main-file ranges include the complete CSL definition at 1318–1405, endpoint theorem and examples at 1407–1452, cited computational framework at 1454–1470, local computation theorem at 1472–1508, examples and timed next at 1510–1536, uniformization and threshold qualifications at 1538–1564, the complete following comparison table at 1566–1587, and the CSL complexity row at 2452–2456. Reading beyond the comparison into the next definition supplied context only; it is not a review of that separate presentation. Whole-file hashing does not imply a whole-file mathematical review.

The assignment's shorthand driver path `annex/p09.tex` is absent relative to the repository root. The actual file is `handbook/annex/p09.tex`; its hash exactly matches the supplied driver hash. Line 6 includes the reviewed correction annex. This path resolution was reported to the parent.

All three hashes matched the assignment at intake and were rechecked unchanged before report creation, at 2026-09-07 14:00:58 UTC. The methods used were source reading, searches, filesystem/hash checks, and explicit mathematical derivation. No test suite, simulation, symbolic package, compilation, manuscript build, or rendering was performed. No other review report or author verdict was read.

## Findings and adversarial checks

There are **no confirmed defect findings**. The following identifiers record the actual semantic challenges and their disposition. Counterexamples below are explicit probes that would refute common incorrect alternatives; the printed correction gives the correct value in each case.

### C2-TOP-01 — PASS: path space, occupation, and self-loops

Evidence: main file 1318–1362 and 1381–1390; annex 10–24.

The rate map and its generator are correctly distinguished. With `E(s) = sum_t R(s,t)`, a positive diagonal rate contributes to actual next-step timing, while `Q(s,s) = -sum_(t != s) R(s,t)` cancels that diagonal rate for state occupation. Positive-rate transitions are required on every path step, finite paths end only at a zero-rate state, and infinite paths are required to cover arbitrarily large times. Right-continuity places the reached state at the jump time. An absorbing terminal state is occupied for all remaining time, but contributes no next step.

The annex's rate-`lambda` Poisson construction treats accepted self-loops as actual path steps and rejected clock ticks as no step. Its finite number of ticks on bounded intervals supplies nonexplosion; the absence of ticks at a prescribed positive time supplies the null-event fact used later. This proof does not confuse uniformization's artificial self-loops with actual next-step events.

Explicit probe: take one state `s`, `R(s,s) = r > 0`, and let `p` hold. Then `Q = 0`, occupation of `p` is always 1, while `Pr_s(X^[a,b] p) = exp(-ra) - exp(-rb)` for finite endpoints. If instead all rates are zero, occupation is still 1 but every timed-next probability is 0. The definition and separate next formula return exactly these different answers.

Closure requirement: none.

### C2-TOP-02 — PASS: nondegenerate endpoint normalization and excluded zero

Evidence: main file 1410–1437 and 1441–1452; annex 26–37.

For any fixed positive endpoint, outside a null event the occupation path is constant on a neighborhood of that endpoint. An upper-endpoint witness can therefore move slightly earlier. At a positive lower-endpoint witness, the prior-time condition and local constancy imply membership in both `A` and `B` at the endpoint and immediately after it, so the witness can move slightly later. This is an equality of probabilities; the proof does not assert pathwise equivalence on trajectories that jump at the fixed endpoint.

At zero, there is no left neighborhood. A positive witness requires the initial state to lie in `A`. If it does, its strictly positive initial holding time, or absorbing continuation, permits a zero witness to move into the interval. This establishes exactly the factor `1_A(s)` for an excluded lower endpoint zero.

Explicit probe: the one-state absorbing chain with `p` true has `Pr(bot U^(0,1] p) = 0` and `Pr(bot U^[0,1] p) = 1`. This is the printed example and directly excludes unconditional removal of the zero endpoint. With `A = B = {s}`, either interval has probability 1. With `A` empty, every interval containing only positive times has probability 0.

Empty intervals have no witness and are explicitly kept distinct from nonempty closed singletons. Infinity is explicitly excluded as a witness time, so the infinite upper-bound notation introduces no endpoint atom.

Closure requirement: none.

### C2-TOP-03 — PASS: positive singleton occupation is not first entry

Evidence: main file 1427–1437, 1490–1494, and 1510–1520; annex 58–69.

For `a > 0`, the singleton event is survival in `A` on `[0,a)` together with occupation of `B` at `a`. Since there is almost surely no jump at this deterministic time, its probability is `exp(Q_A a) 1_(A intersect B)`. This agrees with the theorem at `b = a`, since `v_0 = 1_B` and `D_A 1_B = 1_(A intersect B)`. The event can have positive probability without any jump occurring exactly at `a`.

Explicit probe: let `s -> g` have rate `r > 0`, with `g` absorbing and `B = {g}`. If `A = {s}`, the singleton probability from `s` is 0: success requires the sole jump at exactly `a`. If `A = S`, it is `1 - exp(-ra)`: every earlier entry to `g` persists to the occupation time. These are the two printed cases, and both follow from the displayed matrix formula. At `a = 0`, the probability is `1_B` without a survival mask.

Closure requirement: none.

### C2-TOP-04 — PASS: the survival mask removes failures before the lower bound

Evidence: main file 1481–1506; annex 58–62.

`Q_A` retains the original dynamics while the path is in `A` and makes each state outside `A` absorbing. Multiplication by `D_A` at time `a` then removes all mass that exited `A` before `a`, including paths starting outside `A`. Thus the row of `exp(Q_A a) D_A` is the distribution at time `a` of precisely the surviving paths, up to the justified null event at `a`. Making outside states absorbing alone would retain failure mass; the mask is essential.

Explicit probe: in the two-state chain `s -> g` of rate `r`, take `A = {s}` and `B = {g}`. For `0 < a <= b`, the printed formula gives `exp(-ra) - exp(-rb)`. Omitting `D_A` would instead give `1 - exp(-rb)`, incorrectly counting paths that reached `g` before `a` and then violated `A` before the witness time. Starting at `g` would likewise yield an incorrect positive answer without the mask. For the excluded-zero interval `(0,b]`, the separate left factor `D_A` correctly rejects an initial state in `B \ A`.

Closure requirement: none.

### C2-TOP-05 — PASS: visits to A intersect B remain live before the lower bound

Evidence: main file 1490–1501; annex 50–70, especially 63–67.

The first phase uses `Q_A`, while the second phase uses `Q_(A\B)`. A visit to `B` before a positive lower bound does not discharge the formula; the original chain must continue during the first phase while it remains in `A`. Once the lower bound has been reached, the first subsequent visit to `B` is a witness, so success absorption is correct in the second phase. The annex states this distinction explicitly.

Explicit probe: use the three-state chain `s -> g -> f`, both rates 1, with `f` absorbing, `A = S`, and `B = {g}`. Let the independent residence times in `s` and `g` be `T_1,T_2`, each exponential of rate 1. Then

`Pr_s(A U^[a,a] B) = Pr(T_1 <= a < T_1 + T_2) = a exp(-a)`.

For `0 < a <= b < infinity`, splitting according to whether entry to `g` precedes `a` gives

`Pr_s(A U^[a,b] B) = integral_0^a exp(-t) exp(-(a-t)) dt + integral_a^b exp(-t) dt = (a+1) exp(-a) - exp(-b)`.

The printed product gives the same result: occupation of `g` at `a` contributes `a exp(-a)`, and occupation of `s` at `a` followed by entry during `b-a` contributes `exp(-a) (1-exp(-(b-a)))`. Freezing `g` in the first phase would instead give `1-exp(-b)`, and at a singleton would give `1-exp(-a)`, both wrong. This probe checks exactly the early visit followed by departure that an absorbing-target construction before `a` would lose.

Closure requirement: none.

### C2-TOP-06 — PASS: zero lower bound, infinite bounds, and least reachability solution

Evidence: main file 1458–1462 and 1490–1506; annex 50–56 and 69–71.

For `[0,b]`, `Q_(A\B)` follows the original chain until success in `B` or failure outside `A union B`, then holds the resulting state. Its `B` occupancy at `b` is the desired probability, including the immediate time-zero witness from `B`. The column-vector orientation `exp(Q t) 1_B` and the first-phase/second-phase multiplication order are correct.

For `h`, the boundary prescriptions leave the embedded-chain equations only on nonabsorbing states of `A \ B`, where `P` is defined. The least nonnegative solution is necessary: a closed non-target class, including a state with only a positive rate self-loop, otherwise permits spurious positive fixed points. Iterating the one-step reachability operator from the target indicator counts success within finitely many transitions; the increasing limit counts eventual success. The time-divergence restriction prevents infinitely many transitions before a finite witness time. If a positive witness occurs during a holding interval, its entry state supplies the corresponding discrete success state.

Explicit probes: a self-loop-only non-target state has equation `h_s = h_s` and correct least solution 0; an absorbing target has value 1; an absorbing non-target has value 0. In the three-state probe from C2-TOP-05, `h = (1,1,0)` and the printed infinite-upper-bound formula gives `(a+1) exp(-a)`, exactly the probability that the visit to `g` has not ended before `a`. In the two-state probe with `A = {s}`, `[a,infinity)` has probability `exp(-ra)` for `a > 0`. All are consistent.

The long-run clause and the finite-state bottom-component computation are also compatible with self-loops: the occupation generator cancels diagonal rates, zero-rate singleton components remain stationary, and each finite irreducible nontrivial continuous-time component has a unique limiting occupation distribution. No transient series is applied at infinite time; the text uses reachability and stationary computations for the infinite-time cases.

Closure requirement: none.

### C2-TOP-07 — PASS: timed next and nested truth sets

Evidence: main file 1477–1480 and 1522–1536; annex 74–82.

Conditioning on the first actual successor yields the printed factorization into an exponential waiting-time probability and `sum_(t in B) P(s,t)`. Every singleton interval has probability zero because the first residence time has a continuous law when `E(s) > 0`; when `E(s) = 0`, there is no first successor. Finite endpoint flags do not affect this law, including at zero, unlike the until operator's immediate witness. The self-loop probe in C2-TOP-01 checks that `E(s)`, rather than the off-diagonal escape rate, is required here.

The text explicitly evaluates `A,B` in the original chain and fixes them during every transformation. This is necessary for nested state formulas. For example, in a one-state chain with a positive rate self-loop, the state formula `P_>0[X^(0,1) top]` is true in the original chain but false after the state's rate row is zeroed. Its truth set must be fixed before an outer until calculation makes it absorbing. The printed instructions preserve that truth set.

Closure requirement: none.

### C2-TOP-08 — PASS: uniformization bounds and threshold limitations

Evidence: main file 1538–1564, comparison row 1577–1580, and complexity row 2452–2456.

The stated choice `lambda > 0` with `lambda >= max E(s)` makes `U = I + Q/lambda` nonnegative with row sums 1, including chains having only zero rates. The same lambda also works for the row-zeroed transformed chains. The Poisson series is therefore a positive mixture of stochastic matrices. Omitting a tail of total mass at most epsilon gives a componentwise lower bound and an upper bound obtained by adding epsilon. The text correctly reserves a separate allowance for retained-term evaluation and arithmetic error and instructs propagation through the two-phase sums and products. At time zero it expressly uses the exact identity, avoiding an unnecessary numerical boundary there.

An explicit bound verifies that this propagation is available for the actual local formula. Let `P = exp(Q_A a)` and `W = exp(Q_(A\B) (b-a))`. Suppose exact truncated series give `P_hat <= P` and `W_hat <= W` entrywise, with omitted row masses at most `epsilon_a` and `epsilon_d`. Then

`l = P_hat D_A W_hat 1_B <= u_[a,b] <= l + (epsilon_a + epsilon_d) 1`.

Indeed, write the difference as `(P-P_hat) D_A W 1_B + P_hat D_A (W-W_hat) 1_B`. Each reward vector lies between 0 and 1; the first term is at most `epsilon_a`, and the second at most `epsilon_d`. This derivation is a review check of the printed instruction to propagate bounds, not a claim that the manuscript prints this particular bound. Additional arithmetic errors require corresponding rigorous bounds, as the text says. Fixed input indicators and exact reachability values cause no extra uncertainty; any computed uncertain input vector must carry its own bound.

For an interval `[L,U]` enclosing a probability, the sufficient true-comparison tests are `U < q`, `U <= q`, `L > q`, and `L >= q` for `<`, `<=`, `>`, and `>=`, respectively. Thus a weak inequality can sometimes be certified with `q` at an enclosure endpoint. The text's requirement that the whole enclosure be on the required side is compatible with these cases. Determining equality itself needs separate exact or analytic evidence; refinement of numerical enclosures alone does not supply it.

Explicit equality probe: in a one-state chain with `A = B = {s}`, the until probability is exactly 1. With positive uniformization time and lambda, every finite Poisson partial sum is less than 1, so an enclosure based only on the tail may retain the threshold 1 indefinitely. The exact occupation argument proves the probability is 1. The manuscript explicitly preserves this boundary. The complexity row's phrase “effective with certified numerical boundary” is supported as effective probability approximation and conditional comparison, read with its immediately printed equality qualification; this review does not interpret it as a proved terminating threshold-equality algorithm for every nested CSL input.

Closure requirement: none for the scoped qualification. A future claim of total exact model checking would require an additional decision argument that is not supplied by tail bounds alone.

## Remaining qualified boundaries

**C2-TOP-U01 — UNRESOLVED outside this mathematical scope: exact source identity and source-specific theorem attribution.** The live text labels the two correction theorems as handbook results proved in the annex and distinguishes their derivation from the cited Volterra and steady-state results at main lines 1472–1474 and annex lines 45–48. This review establishes mathematical consistency from the printed semantics. I did not obtain or compare the exact Baier–Haverkort–Hermanns–Katoen 2003 source artifact, so I do not close the separately qualified source-identity or exact-attribution question. Closure would require the identified source artifact and direct source-location comparison; no change to the two local formulas follows from that unperformed check.

**C2-TOP-U02 — UNRESOLVED outside this mathematical scope: final artifact and publication gates.** Software tests, manuscript compilation, rendered-page inspection, reference resolution after compilation, editorial acceptance, and publication acceptance were excluded from the assignment. Their closure requires their own evidence on the relevant final artifact. The annex driver's source inclusion at line 6 is verified, but source inclusion is not compilation evidence.

The disposition is therefore PASS for the specified C2 mathematical text, with the two explicitly separate unresolved boundaries above. No source edits are requested by this review.
