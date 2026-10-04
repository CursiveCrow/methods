# Additional current content findings

These findings arise from current LaTeX reading. They are kept separate from the 615 historical register rows so that the original register inventory remains exact. The manuscript is unchanged.

## INV-CSL-001: closing an until interval can change its probability

**Confirmed current mathematical defect.** At [logic-in-computer-science.tex:1365](C:/Dev/the-methods-of-reason/handbook/parts/p09/logic-in-computer-science.tex:1365), the host permits nonempty intervals with explicit endpoint flags, then claims that replacing an interval by its closure does not change path probability because residence times are continuous. Its own until clause at lines 1377–1380 contradicts that unrestricted statement.

Take the permitted one-state CTMC with state `s`, rate `R(s,s)=0`, and atomic proposition `p` true at `s`. The state is absorbing under lines 1329–1334. The unique path stays at `s`, including at time zero under lines 1336–1345. Let the left until operand be `not top` and the interval be `(0,1]`.

- For every possible witness `t > 0`, the until clause requires the false left operand at `u=0`, since `0 <= 0 < t`. No witness exists. The path-event probability is 0.
- Replacing the interval by `[0,1]` admits the witness `t=0`. The proposition `p` is true then, and the universal prior-time condition has an empty range. Every path satisfies the formula, giving probability 1.

The state formula `P_(>=1/2)[(not top) U^I p]` consequently changes truth value. This uses the actual mutually typed grammar and semantics in the same passage. Continuous positive residence times do not remove the time-zero witness of until.

The inventory reader found this counterexample during its complete remaining-P9 reading. The root independently read current host lines 1325–1385 and checked the counterexample against the displayed definitions. This finding concerns the current handbook's unrestricted claim; it does not attribute that claim or error to the cited Baier–Haverkort–Hermanns–Katoen paper.

**Remaining manuscript work:** correct the unrestricted endpoint-closure statement and preserve the endpoint flags wherever they affect timed-until semantics. Any restricted equivalence used by an algorithm needs its exact hypotheses and proof or source support. The current inventory does not implement that correction.

## INV-ELPP-001: the printed nominal saturation criterion misses a forced subsumption

**Confirmed current mathematical defect.** The [EL++ saturation state and reachability definition](C:/Dev/the-methods-of-reason/handbook/parts/p09/presentations/n-c-010.tex:125), CR1–CR11 at lines 165–200, and the decision criterion at lines 216–227 do not decide every normalized CBox claimed by the text. The shared-nominal label-agreement assertion at lines 264–266 fails on the same example.

Use distinct concept names `A,C,D,P,Q`, one individual name `a`, and roles `r,s`. The following seven GCIs already have the printed normal forms:

```text
A <= exists r.C
A <= exists s.D
C <= {a}
D <= {a}
C <= P
D <= Q
P and Q <= bottom
```

Every model has `A` empty. An element of `A` would require an `r`-successor in `C` and an `s`-successor in `D`; both successors must be the same named element `a`. That element would belong to both `P` and `Q`, contradicting the last GCI. The CBox itself is satisfiable: take a one-element domain interpreting `a`, with all five named concepts and both roles empty. Thus the CBox entails `A <= P` by emptiness of `A`.

Starting with the printed initialization, the rules reach:

```text
S(A)   = {A, top}
S(C)   = {C, top, {a}, P}
S(D)   = {D, top, {a}, Q}
S({a}) = {{a}, top}
S(P)   = {P, top}
S(Q)   = {Q, top}
R(r)   = {(A,C)}
R(s)   = {(A,D)}
```

Other basic labels remain at their initial values. CR1 and CR3 have been exhausted. No label contains both `P` and `Q`, so CR2 adds no bottom. There are no left-existential GCIs, concrete atoms or role inclusions, so CR4 and CR7–CR11 add nothing; CR5 has no bottom to propagate.

CR6 does allow its reachability sequence to start at **any nominal**, as the manuscript explicitly says. However, no nominal has an outgoing role edge here. Neither `C` reaches `D` nor `D` reaches `C`. A zero-length route to `{a}` can only copy `S({a})` into labels that already contain it. Therefore no additional nominal merge occurs and no bottom is derived. Both disjuncts of the printed decision criterion are false for `A <= P`, contradicting the semantic entailment above.

The quotient proof has the corresponding gap: `C`, `D`, and `{a}` share a nominal and belong to the domain reachable from the queried root, but their saturated label sets do not agree. Non-applicability of the printed CR6 does not imply the assertion at lines 264–266.

The inventory reader supplied the normalized counterexample. The root independently checked the actual rule list, the option to start at any nominal, the fixed-point state and the model argument. The held LTCS-05-01 report at SHA-256 `374d73eb848e556da759d89231385353996f44e6a6131f53d2794bb68d5aa3ba` repeats the R-path guard and the label-agreement claim in its printed pages 7–8 and 11–12. Those checked source passages do not supply a missing preprocessing step; the current manuscript presents the criterion as valid rather than explicitly qualifying it as an unresolved historical assertion.

**Remaining manuscript work:** repair the nominal/nonemptiness handling and its decision/canonical-model proof, or accurately restrict the asserted algorithm. A query-specific fresh-nominal assumption is a possible direction, not an implemented or verified correction. Preserve the distinction between the printed source procedure and any repaired procedure. The inventory does not implement the repair.

## INV-CTL-001: the computation-tree illustration leaves its root valuation implicit

The [CTL tree source](C:/Dev/the-methods-of-reason/handbook/parts/p08/temporal-epistemic-supplement.tex:329) labels both branches explicitly with `p` or `not p`, but labels the root only `w`. Its annotation at line 346 says `AF p` is false there. Under inclusive eventuality, that requires `p` to be false at `w`: if `p` is true there, every path already has a witness at its initial position.

The branch continuations are supplied and totality is explicit. The remaining issue is the root's omitted atomic valuation. This is an under-specified illustration, not a counterexample to CTL semantics. It is already included in the component-level disposition of original apparatus row A-146, so it must not be counted as an additional original requirement.

**Remaining manuscript work:** make the intended root valuation explicit in the figure's actual source or an unambiguous accompanying valuation definition.
