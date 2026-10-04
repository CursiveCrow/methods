# Intermediate logics and Heyting varieties: actual-text review

Date: 2026-09-06. Review began 2026-09-07 03:01:15 UTC.

## Result and scope

**Scoped pass: no concrete mathematical defect or necessary source correction found.**

Read the complete actual body `handbook/parts/p10/intermediate-algebras.tex` and all three proofs in `handbook/annex/p10/intermediate-algebras.tex`. Checked the relevant primary thesis pages directly in `tmp/pdfs/p10-priestley-heyting/bezhanishvili-2006-thesis.pdf`. No other review conclusions were consulted. Only this note was written; no manuscript edits, tests, builds, renders, or additional agents.

## Finite equations and the Boolean endpoint

The four equations in `thm:p10-heyting-equational` have exactly the required effect. Starting with residuation, the first follows from a∧1≤a; the second follows by proving both inequalities between a∧(a⇒b) and a∧b; the third is the residual form of a∧b≤b; the fourth follows by comparing all lower bounds.

Conversely, the fourth equation makes a⇒− monotone. The second gives d≤a⇒b ⇒ d∧a≤b. For the converse, the third gives d≤a⇒d, while the first and fourth identify a⇒d with a⇒(a∧d). Monotonicity then yields d≤a⇒b when a∧d≤b. Thus the finite equational claim is justified, with no appeal to residuation as though it were already an equation.

Within a Heyting algebra, a∧(a⇒0)=0. Adding a∨(a⇒0)=1 makes every element complemented, hence makes the bounded distributive lattice Boolean. Conversely the Boolean decomposition of d proves d∧a≤b iff d≤¬a∨b, so uniqueness of residuals identifies implication and gives the added identity. The trivial algebra is covered.

## Intermediate quotient and arbitrary valuations

The theorem-set definition correctly requires IPC⊆L⊆CPL together with modus ponens and uniform substitution. It does not apply substitution freely to local premise-dependent conclusions.

IPC theorem schemas supply reflexivity/transitivity of theorem implication, monotonicity of meet/join, and antitonicity/monotonicity of implication. The annex explains how to derive the implication schema and the meet/join schemas using the preceding propositional rules. Applying them within L proves congruence and a well-defined quotient partial order. The bounds, lattice operations, distributivity, and currying theorem establish a Heyting algebra without assuming any prime-filter representation.

The equivalence [λ]=1 iff λ∈L uses valid IPC schemas involving top and conjunction, followed by modus ponens. Since L⊆CPL and bottom is not a classical theorem, the quotient is nontrivial.

For an arbitrary quotient valuation and a selected λ∈L, the proof chooses representatives only for the finitely many variables in λ, extends by identity on all other variables, and applies simultaneous substitution. Structural induction gives the represented value of the substitution instance, and theorem-level substitution closure puts it in L. This proves H_L∈V(L) without an infinite choice of representatives. The canonical valuation refutes each non-theorem and proves all stated algebraic completeness equivalences.

## Equations, formulas, and inverse assignments

The translation replaces 0,1,⇒ by bottom, top, and object-language implication. Term/formula evaluation is preserved, including ground terms. Residuation yields a⇒b=1 iff a≤b, so s=t is equivalent at each valuation to (s⇒t)∧(t⇒s)=1. Universal identity validity therefore translates exactly into theorem-formula validity, in both directions.

Every defining identity can be moved into the fixed countably infinite variable alphabet: its finite set of occurring variables can be renamed in the order of first occurrence. This is a specified finite syntactic operation and does not require selecting injections separately for an arbitrary family.

The first inverse equality Log(V(L))=L is exactly quotient completeness. For the second, one defining identity set E of the selected subvariety suffices. Every E-identity translates to a formula of Log(V), so any algebra validating Log(V) satisfies E. The opposite inclusion follows directly from the definition of Log. Using one witnessing axiomatization in this argument is ordinary existential reasoning, not an invocation of choice for an infinite family.

## Endpoints and complete lattice operations

IPC completeness gives V(IPC)=HA and Log(HA)=IPC. For the Boolean endpoint, the finite-cell calculation proves validity of every classical tautology in every Boolean Heyting algebra, including zero-variable formulas. Classical propositional completeness supplies a two-element countervaluation for every formula outside CPL. Validating CPL forces excluded middle at each algebra element, giving V(CPL)=BA and Log(BA)=CPL.

Thus V(L) lies in the interval BA⊆V⊆HA, and Log sends that interval back into IPC⊆L⊆CPL. The trivial algebra belongs to each variety, while the trivial-only variety lies outside the interval. This is the correct boundary for the declared consistent intermediate logics.

Nonempty meets on either side are intersections. Logic joins are intersections of their intermediate upper bounds; CPL provides such an upper bound, and closure of IPC together with the union is therefore well defined. Variety joins are defined by the canonical identity theory of BA together with the union, whose Heyting models give the least upper bound. Every upper-bound subvariety has a defining identity set contained in that canonical theory, proving leastness.

Using each subvariety's complete identity theory for intersections avoids selecting an axiomatization for each member of an infinite family. These theories are subsets of the fixed set of identities, which also provides canonical set-sized codes for the subvarieties under discussion.

The empty endpoints are explicitly correct: on logics, the empty meet is CPL and the empty join IPC; on the variety interval, the empty meet is HA and the empty join BA. Adding BA to the variety-join generator handles the empty union correctly. The inverse order-reversing maps exchange all greatest lower bounds and least upper bounds, including these empty cases.

## Primary-source locators

The actual thesis pages verify all locators used in this section:

- Definition 2.1.4, printed p12: intermediate logics are MP/substitution-closed sets between IPC and CPC; the manuscript uses CPL as its declared classical alias.
- Theorem 2.2.6, pp21–22: the four residual equations. The source gives the converse proof and omits the forward details; the manuscript supplies both directions.
- Proposition 2.2.9, p23: the Boolean characterization by excluded middle.
- Theorem 2.2.18, p25: algebraic completeness of IPC extensions.
- Theorem 2.2.19, p26: the logic/variety anti-isomorphism. The immediately preceding paragraph explicitly discusses excluding the trivial variety and taking BA as the lower endpoint; the manuscript's interval formulation makes that convention precise.

The final warning against inferring ordinary Kripke completeness of every intermediate logic from algebraic completeness is correct. None of these proofs requires BPIT or a Kripke representation.
