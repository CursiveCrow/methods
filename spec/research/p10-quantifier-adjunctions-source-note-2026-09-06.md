# Quantifiers as adjoints: primary sources and proof packet

Date: 2026-09-06. Bounded source research for `N-d-022`, `spec/registers/new-content.csv:169`: quantifiers as adjoints and the hyperdoctrine view of first-order logic. The register excludes a development of fibrations. Used the research skill, checked held acquisitions first, and read the relevant primary bodies. Only this note and narrowly named acquisition files were written. No manuscript edits, tests, builds, or manuscript renders; no other reviewers' conclusions were consulted.

## Source acquisition and exact versions

**Pitts, held and read:** Andrew M. Pitts, *Categorical Logic*, author manuscript **18 May 1995**, UCAM-CL-TR-367, DOI `10.48456/tr-367`. Existing key `Pitts1995Draft`. Local file `tmp/acquisition/src030/cambridge-categorical-logic-author.pdf`, with `.layout.txt` extraction. Printed p is physical PDF p+1. [Author PDF](https://www.cl.cam.ac.uk/~amp12/papers/catl/catl.pdf), [official report](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-367.html). This is distinct from the published `Pitts2000` chapter. The needed predicate material is chiefly **§§5.2–5.6, pp40–59**, supported by term semantics in §2.2; it is not chiefly §§3–4.

**Lawvere, original metadata and public access checked:** F. William Lawvere, *Adjointness in Foundations*, *Dialectica* **23(3–4) (1969), 281–296**, DOI `10.1111/j.1746-8361.1969.tb01194.x`, matching the existing `Lawvere1969` bibliography entry. The DOI now resolves to the [journal's Philosophie.ch record](https://www.philosophie.ch/lawvere-1969), which links `https://assets.philosophie.ch/dialectica/lawvere-1969.pdf`. That original-layout PDF returned HTTP 403 both to the web reader and the direct download. [JSTOR's record](https://www.jstor.org/stable/42969800) identifies the original article as openly available under CC BY 4.0; its direct PDF download nevertheless returned an HTML client challenge. The latter is preserved as `tmp/pdfs/p10-quantifiers/lawvere-1969-jstor-access-response.html`, not misidentified as an article PDF. No challenge or access restriction was bypassed.

**Lawvere, complete authorized reprint acquired and read:** *Adjointness in Foundations*, **Reprints in Theory and Applications of Categories 16 (2006), 1–16**, republished May 21, 2006 and revised October 30, 2006. Source: `https://tac.mta.ca/tac/reprints/articles/16/tr16.pdf`, also linked by the [Lawvere Archives](https://lawverearchives.com/work/). Local file: `tmp/pdfs/p10-quantifiers/lawvere-adjointness-foundations-2006-reprint.pdf`; 231,071 bytes; 17 physical PDF pages (numbered pp1–16 and a final editorial page). SHA256 `E1F0AB8479A46D0C39395E9E999D999BDC955A3D8D5BF5FB9E5872B095A721F9`. Printed page numbers agree with physical page numbers. Suggested separate key **`Lawvere2006AdjointnessReprint`**. The title page explicitly authorizes the reprint; pp1–2 are 2006 commentary, and the original article begins at p3. The author says the section subtitles were inserted for this reprinting. A candidate collected-works file named `1969-adjointness-in-foundations.pdf` was also inspected and proved byte-identical to this 2006 reprint; the redundant copy was removed, retaining the verified publisher copy.

The original article's exact historical text is therefore available through an authorized retypeset reprint, but the original 1969 layout was not acquired. Cite the inspected reprint's pagination explicitly rather than assigning its page numbers to *Dialectica*.

## What Lawvere actually supplies

**Reprint §3, pp10–14**, develops cartesian closed categories and hyperdoctrines. The hyperdoctrine definition itself is **pp11–12**: a cartesian closed base T; a cartesian closed category P(X) of attributes for each type; substitution functors contravariant in terms, coherently functorial; and left and right adjoints to substitution along every term. This is a category-valued definition, not just posets of predicates. The author explicitly notes on p12 that substitution need not preserve implication in this generality.

**Reprint p12** describes the graph of f and equality as existential quantification of truth along the graph/diagonal. **Reprint p13** gives the powerset hyperdoctrine: sets and maps as the base, subsets as attributes, inverse image as substitution, and direct image as existential quantification. The other example on pp13–14 uses categories of sets over a set; this is not the same as the powerset example and should not be merged with it.

The inspected reprint does not give the explicit modern posetal package of Heyting-preserving reindexing, parameterized equality, product-square Beck–Chevalley and Frobenius as numbered axioms. Searches for the names Beck and Frobenius in its complete text produced no occurrences. Pitts supplies those definitions and stability requirements directly. Thus use Lawvere for the foundational adjunction idea and cited historical construction, and Pitts for the exact first-order semantics developed below.

## Exact Pitts locators

| Needed item | Verified primary locator |
| --- | --- |
| Base and indexed order | **Definition 5.2.1, pp41–42**: finite-product category C with a contravariant functor `Prop:C^op→Pos`; each f gives monotone, functorial reindexing. Pitts calls this a prop-category and explicitly warns that the terminology is not standard and general Lawvere hyperdoctrines are category-valued. |
| Powersets | **Example 5.2.2, p42**: ordinary subsets, ordered by inclusion; reindexing is inverse image. |
| Subobject variant | **Example 5.2.5, pp42–43**: finite limits and well-poweredness give a set of subobjects in each fibre; reindexing is categorical pullback. Finite limits alone do not supply the full logical structure below. |
| Atomic predicates and substitution | **§5.2, pp43–44**, **Lemma 5.2.6, p44**: atomic relations are reindexed along tuples of term interpretations; simultaneous substitution is reindexing and context extension is projection reindexing. Terms use **Lemma 2.2.1, p8**. |
| Finite hypotheses and structural soundness | **Definition 5.3.1 and Theorem 5.3.2, p45**: fibres have finite meets preserved by reindexing; a sequent is satisfied when the meet of its finitely many antecedents is below its conclusion. |
| Propositional operations | **Definition 5.4.1, p46**: finite joins and Heyting implications, each preserved by reindexing. **Theorem 5.4.2, p47**, and Figs3–4 pp48–49: intuitionistic propositional soundness. **Remark 5.4.7, p51**: Boolean fibres yield classical propositional logic. Having Heyting algebras as fibres without implication-preserving reindexing is insufficient. |
| Quantifier adjunctions and substitution | **§5.5, pp51–53**, **Definition 5.5.1, p53**. Projection reindexing has a right adjoint for forall and a left adjoint for exists; both are natural in the parameter object. Equations **(5.6)–(5.7), p52**, are the product-square Beck–Chevalley identities; **(5.8)–(5.9), pp52–53**, are the two adjunctions. |
| Frobenius | Equation **(5.10), p53**, and **Remark 5.5.2, p53**. It is an explicit stability requirement with finite meets, and follows from a left adjoint when reindexing preserves Heyting implication. |
| Quantifier Set formulas | **Example 5.5.3, pp53–54**: existential and universal fibre conditions, naturality in parameters, and agreement with Tarskian semantics. |
| Adjoint existence is insufficient | **Example 5.5.5, p54**: inclusive subsets of cpos have left adjoints to projection reindexing but these fail the needed Beck–Chevalley condition. |
| Equality with parameters | **§5.6, pp55–56**, equation **(5.12)** and **Definition 5.6.1, p56**: the diagonal equality predicate satisfies the parameterized adjoint rule. Equation **(5.13), p56**, is its necessary unparameterized top case. **Remark 5.6.2** supplies an additional implication-plus-universal-quantification hypothesis under which that top case suffices; do not assert it with only finite meets. |
| Set and subobject equality | **Example 5.6.3, p56**: diagonal relation in Set. **Example 5.6.5, p57**: diagonal monomorphism; reindexing equality along a term pair gives its equalizer subobject. |
| General substitution squares | **Remark 5.6.6, pp57–59**: generalized quantifiers and the two Beck–Chevalley equations for a square. The implication/equality/quantifier structure is needed for the displayed generalized-quantifier formulas; in particular the formulas explicitly use Eq. The first-order development may require only the product substitution squares, whose pullbacks exist from finite products. |

Minor source display cautions: Definition 5.5.1 prints the projection codomain as X although its surrounding equations require `I×X→I`; use the typed projection. Its parenthetical equation references also contain a slip for the right-adjoint law. The formulas themselves, (5.6)–(5.10), determine the intended statements. The introductory sentence of Remark 5.6.6 does not explicitly repeat equality among its assumptions although its construction uses Eq; include equality if using that construction.

## A fully explicit powerset construction

All arguments in this section work in ZF; they require no simultaneous selection of witnesses. For every set X let `P(X)` be its powerset, ordered by inclusion, with top X, bottom empty set, intersection, union, and Boolean implication `U⇒V=(X\U)∪V`. For a function `f:X→Y`, define `f^*(B)=f^{-1}(B)`. Inverse image is monotone, preserves all the Boolean operations, and satisfies `id^*=id` and `(gf)^*=f^*g^*`.

For `A⊆X` define

`∃_f A = { y∈Y : there is x∈A with f(x)=y }`,

`∀_f A = { y∈Y : for every x∈X, f(x)=y implies x∈A }`.

Then

`∃_f A ⊆ B ⇔ A ⊆ f^*B`,

because the left assertion says exactly that f(x) belongs to B whenever x belongs to A; and

`f^*B ⊆ A ⇔ B ⊆ ∀_f A`,

because both assert that every x with f(x) in B lies in A. Thus `∃_f ⊣ f^* ⊣ ∀_f` as monotone maps. These equivalences also prove monotonicity and uniqueness of the adjoints: two left adjoints have the same upper bounds at each input, and two right adjoints the same lower bounds.

For `π:I×A→I` the formulas reduce to the usual existential and universal quantifiers over the second coordinate. If A is empty, `∃_π U=∅` and `∀_π U=I`; this case must be retained. In particular the empty parameter context is interpreted by a singleton, not by the empty set.

### Beck–Chevalley in Set, including both directions

Consider a pullback square

```
X' --g'--> X
 |          |
 f'         f
 |          |
 v          v
Y' ---g---> Y .
```

For any `y'∈Y'`, the function g' gives a bijection from the fibre of f' over y' onto the fibre of f over g(y'). Surjectivity and injectivity here are exactly the pullback property applied to pairs `(y',x)` with `g(y')=f(x)`.

For `U⊆X`, membership in `g^*(∃_f U)` means there exists x in U with `f(x)=g(y')`; by the fibre bijection this is equivalent to membership in `∃_(f')((g')^*U)`. Membership in `g^*(∀_f U)` means every x in the latter fibre belongs to U; by the same bijection it is equivalent to membership in `∀_(f')((g')^*U)`. Hence

`g^*∃_f = ∃_(f')(g')^*`, and `g^*∀_f = ∀_(f')(g')^*`.

This is a fibrewise argument, not an application of Choice. For ordinary capture-safe substitution beneath a quantifier, take `g=f_0:I'→I`, `X=I×A`, `X'=I'×A`, and `g'=f_0×id_A`.

For a merely commutative square, adjunction gives only the automatic comparisons

`∃_(f')(g')^* ≤ g^*∃_f`, and `g^*∀_f ≤ ∀_(f')(g')^*`.

Do not replace the pullback/stability hypothesis with commutativity. For example take `X'=∅`, `X=Y=Y'={*}`, and f,g the identities. With U=X the existential equality fails; with U empty the universal equality fails.

### Frobenius and equality in Set

For `U⊆X`, `V⊆Y`,

`∃_f(U∩f^*V) = (∃_f U)∩V`.

An element y belongs to either side exactly when y belongs to V and some x in U satisfies f(x)=y. This proves both inclusions, including empty fibres.

Let `Δ_A:A→A×A`, `a↦(a,a)`. Then

`δ_A = ∃_(Δ_A)(A) = { (a,a):a∈A }`.

For any `t,u:I→A`, reindexing gives `⟨t,u⟩^*δ_A={i:t(i)=u(i)}`. To verify equality with parameters, put `e=id_I×Δ_A`, `p(i,a,b)=(i,a)`, and `r(i,a,b)=(a,b)`. For `U⊆I×A`,

`∃_e U = p^*U ∩ r^*δ_A`.

Both sides consist exactly of triples `(i,a,a)` with `(i,a)∈U`. Combining this with `∃_e ⊣ e^*` proves the full parameterized equality adjunction used below, rather than just reflexivity.

## A precise first-order posetal hyperdoctrine convention

Define the convention used in the manuscript before invoking its consequences. Let C be a category with chosen finite products. Let `P:C^op→Heyt` be a contravariant functor to Heyting algebras and homomorphisms preserving top, bottom, finite meets, finite joins, and Heyting implication. Write f* for P(f). For each product projection `π:I×A→I`, require monotone maps `∃_π,∀_π:P(I×A)→P(I)` with

`∃_π ⊣ π^* ⊣ ∀_π`,

and require both Beck–Chevalley identities for every parameter substitution square `f×id_A` over `f:I'→I`. These squares are pullbacks in any finite-product category. No other pullbacks, and no adjoints to every arbitrary arrow, are required for this definition.

For equality, require `δ_A∈P(A×A)` for each object A, satisfying the following parameterized axiom for every I. With e,p,r as above, the monotone map

`L_e(α)=p^*α ∧ r^*δ_A`

is left adjoint to `e^*:P(I×A×A)→P(I×A)`. This states exactly

`p^*α ∧ r^*δ_A ≤ β ⇔ α ≤ e^*β`.

The top, parameter-free case says `δ_A` is the value at top of a left adjoint to diagonal reindexing. This follows from the full axiom; the converse is not being asserted without further hypotheses. In a general doctrine δ_A is a predicate, not automatically a selected subobject or a literal diagonal subset. The powerset construction satisfies the complete definition by the preceding proofs. Boolean fibres strengthen the propositional logic to classical logic.

This is a specified first-order posetal convention based on Pitts. It should not be called literally identical to Lawvere's category-valued CCC definition: neither the base requirements nor the substitution requirements are the same.

### Frobenius is a proved consequence under these hypotheses

More generally suppose `L⊣R` between Heyting algebras and R preserves implication. For any α in the domain of L and β,γ in its codomain,

`L(α∧Rβ)≤γ`

`⇔ α∧Rβ≤Rγ`

`⇔ α≤(Rβ⇒Rγ)`

`⇔ α≤R(β⇒γ)`

`⇔ Lα≤(β⇒γ)`

`⇔ Lα∧β≤γ`.

The two elements have the same upper bounds, so `L(α∧Rβ)=Lα∧β`. Applying this to `L=∃_π`, `R=π^*` proves Frobenius. No Beck–Chevalley hypothesis is used in this calculation. With only meet-semilattice fibres, however, the implication step is unavailable and Frobenius must be assumed or separately proved, as Pitts does in his more modular definition.

## Formula interpretation, substitution, and soundness

For a many-sorted first-order signature, interpret each sort by an object of C, each operation by an arrow between the corresponding finite products, and each relation by a predicate in the corresponding fibre. A nullary operation is an arrow from the terminal object; a nullary relation is a predicate in its fibre. Interpret a finite variable context by its product, terms by projections and composition/pairing, and atomic predicates by reindexing the designated relation along the tuple of term arrows. Interpret equality by `⟨t,u⟩^*δ_A`, connectives by fibre operations, and quantifiers by the adjoints for context projections.

**Substitution lemma.** For any capture-safe term substitution represented by `s:J→I`, prove `⟦φ[s]⟧=s^*⟦φ⟧` by induction on φ. Atomic cases use term substitution and functoriality. The connective cases use preservation of the corresponding Heyting operations. For a quantified formula, rename its bound variable fresh before substitution; the new substitution map is `s×id_A`, and the appropriate Beck–Chevalley equality is exactly the induction step. For equality, the equality predicate is fixed and the tuple of substituted terms is the old tuple composed with s, so functoriality proves the result. Context weakening is the special case of projection reindexing.

**Sequent meaning.** A finite-hypothesis sequent `φ_1,...,φ_n ⊢ ψ` in context I means `α≤⟦ψ⟧`, where `α=∧_i⟦φ_i⟧`; for n=0 the meet is top. Identity, exchange, contraction, weakening, and Cut follow respectively from reflexivity, the meet laws, monotonicity, and transitivity. Substitution preserves the inequality by its lemma. Propositional rules follow from the defining meet/join/residuation laws of Heyting algebras.

**Universal rules.** For an antecedent α independent of the new variable, `π^*α≤β ⇔ α≤∀_πβ` proves universal introduction and its eigenvariable condition. For a term t of type A in context I, the map `s=⟨id_I,t⟩` is a section of π. Reindex the counit `π^*∀_πβ≤β` along s to obtain `∀_πβ≤s^*β`, which proves universal elimination. The term must be well typed in the retained context.

**Existential rules.** Reindex the unit `β≤π^*∃_πβ` along a term section s to obtain `s^*β≤∃_πβ`, proving existential introduction. For elimination, suppose `π^*α∧β≤π^*γ`, where α and γ do not depend on the bound variable. Apply the left adjunction and Frobenius to obtain `α∧∃_πβ≤γ`. Together with a premise `α'≤∃_πβ` this gives `α∧α'≤γ`, the rule with two finite antecedent lists. The parameter conditions are precisely the usual freshness conditions.

**Equality rules.** The unit for `L_Δ⊣Δ^*` at top gives reflexivity; reindexing gives `top≤⟦t=t⟧`. The parameterized equality adjunction says that if a predicate β holds on the diagonal under assumptions α, then `p^*α∧r^*δ_A≤β`; reindexing along `(id_I,t,u)` gives replacement of equals in arbitrary predicates under parameters. This is the equality elimination rule. Thus induction on a derivation proves soundness for Pitts's contextual first-order calculus, including arbitrary sets of theory axioms because a derivation uses only finitely many.

### Nonempty-domain first-order logic requires an explicit bridge

The powerset doctrine above includes empty sort interpretations. It validates the contextual rules just proved, but it must not silently be identified with the handbook's ordinary nonempty-domain FOL semantics or its context-erasing conventions. For example a closed `∃x(x=x)` fails when the sort is empty. A context containing an element of that sort instead has empty interpretation and all its sequents hold vacuously; dropping such a context is not harmless.

To recover ordinary nonempty-domain Set semantics, restrict the interpretations of the quantified sorts to nonempty sets. More abstractly, for any rule or theorem that requires inhabited sorts, impose explicitly `∃_(I×A→I)(top)=top` for each interpreted sort A and parameter context I. In Set the condition at I=1 is exactly `A≠∅`, and nonemptiness gives it for every I. Frobenius then yields `∃_ππ^*α=α`, so projection reindexing reflects order: `π^*α≤π^*β` implies α≤β. This justifies removal of an unused variable context in that strengthened semantics. No such inhabitance condition is part of the bare powerset construction over all sets or follows merely from the two adjoints.

## Incorporation conclusion

The held Pitts1995Draft supports a complete sound first-order development with all requested stability and equality conditions explicitly typed. The authorized Lawvere2006AdjointnessReprint supports the historical adjunction and powerset constructions while retaining the original definition's different scope. The only source-access gap in this bounded packet is the original 1969 printed layout; the accessible reprint is a complete primary text with verified variant identity. No claim that all abstract doctrines automatically satisfy Beck–Chevalley, that all diagonal-top predicates suffice for parameterized equality, or that all Set sort interpretations are nonempty is justified by these sources.
