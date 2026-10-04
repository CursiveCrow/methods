# Independent contextual first-order semantics review

Date: 2026-09-06. Read the complete actual body `handbook/parts/p10/first-order-categorical-semantics.tex`, annex `handbook/annex/p10/first-order-categorical-semantics.tex`, and calculus sheet `handbook/registry/calculi/contextual-first-order.tex`. Scope: all three `quant-fol` proof pairs, the syntax and interpretation definitions, all 27 registered rules, theory axioms, and the Tarskian/nonempty-domain comparison. No other mathematical review conclusions were consulted. Only this owned note was written; no manuscript/shared edits, tests, builds, or renders were performed.

## Finding reported and resolved

The first read found an overbroad context-removal sentence in `thm:p10-doctrine-tarski`. After discussing both term equations and predicate sequents, it said that removal was valid in arbitrary doctrines for inhabited sorts without limiting this to predicates. Internal inhabitance reflects predicate order, not equality of base arrows.

A counterexample is the constant one-element doctrine on Set. Every object, including the empty set, is internally inhabited. Two distinct constant functions `1→{0,1}` become equal after precomposition with `empty set→1`, although they remain distinct before precomposition. Thus an equational judgment cannot in general discard that internally inhabited variable.

The author repaired the actual theorem and proof during this review. Read-back confirmed the following:

- Body `thm:p10-doctrine-tarski`, then lines 159–165, explicitly permits both judgment kinds in nonempty Set, limits the general doctrine statement to predicate sequents, and disclaims base-arrow equality reflection.
- Annex `annex:p10.quant-fol.3`, then lines 216–229, explicitly uses surjectivity of Set context projections to reflect equality of term functions as well as inclusion. It separates this from the abstract predicate-order consequence and notes that an internally inhabited projection need not be epic in the base.

The reported issue is resolved. No additional concrete mathematical defect was found in the full rule and interpretation check described below. The subsequent quantifier-notation incorporation was also read back and confirmed, as recorded at the end of this note.

## Syntax, products, and substitution

The syntax distinguishes a finite list of variable declarations from a finite hypothesis list. Formula formation retains unused declarations, including under nullary relation formation. Function and relation arities may be zero. A countably infinite supply of variable names is now explicitly declared, with sorts assigned by declarations, so freshness outside each finite substitution instance is available without an unstated supply condition. Bound alpha-renaming and capture-safe simultaneous substitution are specified.

The interpretation uses `I_empty=1` and `I_(Γ,x)=I_Γ×A`, so a unary context really is `1×A`. The argument product of a symbol also starts with a terminal component. Tuple arrows include that unique leading component, and a nullary tuple is the map to 1. The target of the equality pair is separately the actual binary product `A×A`, as required by the equality predicate. The variable, operation, and predicate formulas are correctly typed with these conventions.

In `annex:p10.quant-fol.1`, the term induction uses tuple precomposition and terminal uniqueness. The atomic-relation step uses reindexing along the argument tuple; the equality step uses the fixed equality predicate and composition of its term pair. Each propositional step requires, and has, preservation of the corresponding Heyting operation.

For both quantifiers, the lifted substitution is the correctly typed `s×id_A:J×A→I×A`. Its old variable components are weakened along the first projection and its final component is the new variable. The two separate calculations use respectively existential and universal Beck–Chevalley. They do not obtain one quantifier's stability from the other's by an unproved duality. The induction also covers vacuous binders and empty contexts. Renaming/permutation maps are interpreted by their product-tuple isomorphisms; reindexing need not reflect order merely to establish the substitution and weakening laws.

## Every registered rule

The sheet contains 27 rules, including both explicit theory-axiom rules. Its rule conditions agree with the cases checked in `annex:p10.quant-fol.2`:

| Registered rules | Checked semantic argument |
| --- | --- |
| Eq-Ax and Seq-Ax | The fixed interpretation satisfies every theory axiom by hypothesis. The axiom contexts are retained. |
| Eq-Refl, Eq-Sym, Eq-Trans | Reflexivity, symmetry, and transitivity of actual equality of interpreted arrows. |
| Eq-Subst | The prefix-context term equation makes the two inserting tuple arrows equal after weakening into the retained context. Composing the other equal pair of term arrows with that common insertion gives the conclusion. |
| Id, Cut, Contract, Exchange | Reflexivity/meet projection, transitivity with the two antecedent meets, idempotence, and commutativity. |
| Context Weaken | Pullback along the projection forgetting added declarations preserves both the inequality and its finite antecedent meet. It does not require that the projection reflect order. |
| Subst | Its equational premise is an external term equation, so both inserting maps are equal. Formula substitution identifies the reindexed antecedent and conclusion even though the sheet uses M in one and M' in the other. |
| false-Elim | Bottom lies below every predicate. |
| Conjunction introduction and both eliminations | Meet monotonicity and the two meet projections, respecting separate assumption lists for introduction. |
| Both disjunction introductions and elimination | Join inclusions; for elimination, intersect all three antecedent meets and use Heyting distributivity to split beneath the two disjuncts. The actual rule's three lists are all retained. |
| Implication introduction and elimination | Heyting residuation and evaluation `(b⇒c)∧b≤c`. |
| Universal introduction | The assumption list is well formed in the shorter context, so its value is a projection pullback. The right adjunction then discharges the last variable. |
| Universal elimination | The supplied well-sorted term gives a section `<id_I,M>` of the projection. Reindexing the counit along that section proves the instance. No arbitrary global inhabitance assumption is used. |
| Existential introduction | The supplied term section reindexes the left-adjoint unit, proving the instance implies its existential quantification. Witness typing remains necessary even when the bound variable is absent from the body. |
| Existential elimination | The explicit freshness conditions make the undischarged assumptions and conclusion projection pullbacks. The left adjunction and Frobenius yield `a'∧∃b≤c`; the first premise then supplies the concatenated antecedent. |
| Equality introduction | Pull back `Δ_A^*δ_A=top_A` along the interpreted term. This is an internal equality formula, not an external equation inferred from a predicate. |
| Equality elimination | The full parameterized equality adjunction, with the maps and parameter assumptions detailed below. |

Adding hypotheses is indeed admissible through the displayed Id and Cut rules, as the proof says. The checking of all primitive rules suffices for induction on a finite derivation tree. Any set of theory axioms is permitted, because the tree has only finitely many axiom leaves; no extra compactness or model-existence assertion is being assumed.

## The full equality-elimination step

Let `b=⟦ψ(x,y)⟧` in `P((I×A)×A)` and let a' be the meet of the second premise's assumptions in P(I). The registry requires every member of that assumption list to be well formed in Γ, so its value in Γ,x is exactly `π^*a'`. Substitution by the diagonal gives the premise `π^*a'≤e^*b`.

The parameterized equality adjunction yields `p^*π^*a'∧r^*δ_A≤b`. Its domain is the left-associated triple product. Pulling back along `h=<<id_I,M>,N>:I→(I×A)×A` gives the displayed inequality because `π p h=id_I` and `r h=<M,N>`. Combining with the first premise gives the conclusion under both hypothesis lists. This uses every parameter in the actual equality rule and does not collapse formula equality to arrow equality.

The final degenerate-doctrine example is valid: take Set as base and a one-element Heyting algebra in every fibre. All reindexings, quantifiers, and equality data are unique and satisfy the requirements. Every equality formula is true while distinct constant term arrows remain distinct. The sheet has no forbidden reflection rule. This matches the distinction in Pitts's Remark 5.6.7 p59, whose actual source text was read during this review.

## Tarskian and nonempty-domain comparison

`annex:p10.quant-fol.3` gives an actual bijection between a leading-terminal context product and finite sorted assignments, with a specified inverse. The function/relation argument interpretations are transported through the analogous bijections. Nullary operations and relations use the singleton empty assignment set. Term induction and the Boolean powerset operations give exactly the Tarskian atomic and connective clauses; the projection fibre gives precisely the possible values of a quantified variable, including an empty fibre.

For the powerset interpretation, equality of term functions is equality at every finite assignment, and the sequent inequality is universal implication from all finitely many hypotheses. No assignment of values simultaneously to every variable or sort of an infinite language is required. When a sort is nonempty, every shorter assignment extends across one unused declaration. Its projection is therefore surjective, reflecting both predicate inclusion and equality of Set term functions. Finite unused contexts can be removed one variable at a time; moving a variable to a final position uses the already established permutation isomorphisms.

The repaired abstract comparison is appropriately weaker: internal inhabitance supplies order reflection for predicates only. Empty-sort examples correctly distinguish false in an empty variable context (a singleton parameter set) from false under an added empty sort (an empty parameter set). The closed existential equality formula fails for an empty Set sort, while the corresponding universally quantified formula is vacuously true. No completeness or deductive equivalence with the handbook's different LJ presentation is claimed.

## Source check

Pitts1995Draft §§5.2–5.6 pp40–59, Lemma 5.2.6, Theorems 5.3.2 and 5.4.2, and the cited Figures 1–3, 5, and 7 support the modular contextual interpretation and its rules. The live statement deliberately does not add the equivalent adjoint rule presentations as extra primitive rules. The two equality judgments and failure of unrestricted equality reflection are expressly discussed in the actual source's Remark 5.6.7 p59. Examples 5.5.3 pp53–54 and 5.6.3 p56 support the powerset quantifier/equality comparison. The claims are attached to the inspected May 18, 1995 draft and not to unverified Pitts2000 pagination. The present annex supplies its own detailed proof for the displayed sheet.

## Final incorporation read-back and result

Read the saved notation changes across the body, annex substitution proof, quantifier rules, and final sheet header. Current source dimensions in that read-back were body lines 1–188, annex lines 1–251, and registry lines 1–29. The body now defines a unary formula abstraction `φ=(x)e` and application `φ(M)=e[M/x]` at lines 26–35. It expressly makes this metalevel binding notation, not a new sort or object-language connective. The new locator, Pitts §3 p13, was checked against the actual source passage headed *Meta-linguistic conventions*, which defines `(x)e` and its substitution application.

Body lines 111–116 now interpret `∀_σ(φ)` and `∃_σ(φ)` by applying the appropriate projection adjoint to the body `φ(x)` in the extended context. Annex lines 34–55 use that same body and the same lifted substitution `s×id_A`; both Beck–Chevalley calculations remain correctly typed. Registry lines 24–27 use the corresponding abstractions and preserve the original rule premises and eigenvariable restrictions. The explicit witness typing in existential introduction is identified as clarification of implicit source well-sortedness, at body lines 53–59 and registry line 26. This is accurate, and it prevents vacuous bodies from licensing a witness of an uninhabited sort.

The final registry header at line 2 now agrees with the body on `φ(M)=e[M/x]`, and distinguishes two-variable simultaneous substitution in `ψ(M,N)`. The closed empty-sort example is now `∃_σ((x)(x=_σ x))` at body line 178 and annex line 236; its binding and false interpretation in the terminal Set context are unchanged and correct.

The repaired context-removal statement remains present at current body lines 170–176 and annex lines 217–230: both term equations and sequents in nonempty Set; predicate sequents only for abstract internal inhabitance. No new mathematical issue was introduced by the notation or qualification changes.

**Final scoped result: pass after the recorded correction.** No unresolved concrete defect remains in the three actual first-order interpretation/soundness/Tarskian proofs and all 27 registered rules reviewed here. This is not a build, render, routing, or whole-manuscript acceptance result.
