# Final poll — topic specialist

### F6 — accept

The post-r4 schema at `handbook/registry/calculi/mltt-intensional.tex:17-36` closes the exact defect recorded in Round 4.  `Eq_Delta` has one clause for a type-premise pair (`Delta |- A == A' type`) and a separate clause for a term-premise pair, which requires both equality of the two types and term equality after conversion to the common left-hand type.  Lines 29-36 apply that multi-sorted relation to every premise judgment in the exact dependent telescope of each displayed constructor rule, transport each later premise into the already established left-hand context, and require the corresponding multi-sorted equality for the conclusion.  Pi/Sigma/Id formation premises are therefore handled as type judgments rather than being forced into term-equality premises, while lambda, application, pairing, projections, refl, and J retain their term typing and dependent transports.  Together with the already typed computation rules and the structural, conversion, and universe rules, this satisfies the F6 correction without relying on the former term-only congruence schema.

### F8 — accept

The corrected identity clause at `handbook/registry/calculi/omega-arithmetic.tex:4` now states the syntax with the required separation: function symbols name primitive-recursive numerical functions and generate number terms together with variables, `0`, and `S`; relation symbols name primitive-recursive numerical relations and occur in literals.  It no longer places relation symbols in number terms.  The sole Round 4 residual is therefore removed.  The previously source-verified one-sided sequent domain, initials, inference rules, indexed derivability relation, cut-rank bound, `2_n(alpha)` recursion, and Jäger--Probst Theorem 2 instance are unchanged.

No blocking objection remains for F6 or F8.  This poll makes no build, rendering, visual-review, source-fidelity, or user-acceptance claim.
