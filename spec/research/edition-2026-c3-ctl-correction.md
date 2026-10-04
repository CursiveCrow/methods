# Edition 2026, C3: explicit CTL root valuation

Initial correction recorded 7 September 2026, 13:17 UTC. Scope: INV-CTL-001 and the root-valuation component of original apparatus requirement A-146. The initial snapshot below is followed by a separately recorded review-driven notation repair. This is author evidence, not independent acceptance or formal admission.

## Actual correction

In [temporal-epistemic-supplement.tex:332](C:/Dev/the-methods-of-reason/handbook/parts/p08/temporal-epistemic-supplement.tex:332), the CTL computation-tree root label changed from \(w\) to \(w:\neg p\). The node identifier, edges, two infinite branch continuations, four annotations, caption and stable label fig:p08-ctl-tree remain unchanged.

The before/after whole-file text comparison equals exactly this one-line replacement; no other text or line endings changed. The file remains 756 lines.

| Snapshot | SHA256 of the complete manuscript file |
|---|---|
| Before C3 | 637FA1588D8E7EF2412142562847733A2CA0C271BD294576BBF0879217C30B70 |
| After C3 | 3028F3196A8F8FC064A06E5E7AEC3366FAD90AA042FCEAF0645825AA70EDDB56 |

The correction addresses an unspecified valuation rather than changing CTL semantics. With the old bare root label, assigning \(p\) true at \(w\) would make AFp true immediately under inclusive eventuality, despite the entirely negative right branch. The new node label states the intended value in the figure itself.

## Semantic evidence

The actual [total-transition definition, lines 46–55](C:/Dev/the-methods-of-reason/handbook/parts/p08/temporal-epistemic-supplement.tex:46) requires a nonempty state set, a successor at every state, and paths indexed from zero. The [CTL clauses, lines 69–99](C:/Dev/the-methods-of-reason/handbook/parts/p08/temporal-epistemic-supplement.tex:69) make EX/AX existential/universal over immediate successors and permit a strong-until witness at index zero. The [registered EF/AF equations, lines 5–6](C:/Dev/the-methods-of-reason/handbook/registry/calculi/hilbert-ctl.tex:5) identify eventuality with until having the always-true left operand. These current passages were read; no new primary-paper fidelity claim is made.

Write the displayed left branch as \(u_0=u,u_1,u_2,\ldots\) and the right branch as \(v_0=v,v_1,v_2,\ldots\). The full displayed model for the relevant atom has
\[
 S=\{w\}\cup\{u_n,v_n:n\in\mathbb N\},\qquad
 V(p)=\{u_n:n\in\mathbb N\},
\]
with edges \(wRu_0,wRv_0,u_nRu_{n+1},v_nRv_{n+1}\), and no other edges. Each state has a successor. The caption at lines 349–351 expressly gives the dots infinite continuations, so they are not terminal leaves.

Every annotation at [lines 346–347](C:/Dev/the-methods-of-reason/handbook/parts/p08/temporal-epistemic-supplement.tex:346) follows:

| Annotation at \(w\) | Exact reason |
|---|---|
| EFp true | The path \(w,u_0,u_1,\ldots\) has a \(p\)-witness at position 1. |
| AFp false | The path \(w,v_0,v_1,\ldots\) has no \(p\)-witness at any position, including position 0 because the root is explicitly negative. |
| EXp true | The immediate successor \(u_0\) satisfies \(p\). |
| AXp false | The immediate successor \(v_0\) satisfies \(\neg p\). |

All four displayed claims are therefore consistent with the specified total model and inclusive semantics.

## Verification boundary

The initial figure source at lines 329–353 was read back after the label edit. No build, manuscript render, software test, registry change, inventory update or independent acceptance record was produced. The enlarged root label has not received a rendered-layout check.

## Subsequent definition-before-use repair

The independent publication-text reviewer confirmed that the earlier CTL
definition did not state the EF/AF abbreviations used by the figure. Their
equations existed only in the later calculus sheet. The lead added both
expansions directly after the strong-until clauses in `def:p08-ctl-semantics`,
before the CTL card and figure, and stated that the until witnesses allow zero.
The figure and its truth claims are unchanged by this second edit.

Current whole-file SHA256 after the notation repair:
`3f9533cfaec9de0da6f3729105571656999122b2813d199d5326c91c6e03d7a0`.
The equations were read against `registry/calculi/hilbert-ctl.tex:5-6` and the
actual preceding semantic clauses. Independent closure of the publication
finding and remaining production gates are still required.
