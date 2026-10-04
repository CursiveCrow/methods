# Pitts's adjoint presentations: source and syntactic equivalence packet

Date: 2026-09-06. Scope: actual Figures 4, 6, and 8 of `Pitts1995Draft`, their surrounding explanations, and complete syntactic translations between their rules and the registered contextual natural-deduction package. Only this research note is written. No manuscript tests, builds, or renders were performed. The research skill was used for primary-source checking; the PDF skill was used to inspect the three source pages visually.

## Primary source and live interfaces

Andrew M. Pitts, *Categorical Logic*, author draft dated 18 May 1995, UCAM-CL-TR-367, DOI `10.48456/tr-367`, bibliography key `Pitts1995Draft`. [Author PDF](https://www.cl.cam.ac.uk/~amp12/papers/catl/catl.pdf), [official report record](https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-367.html).

Held body: `tmp/acquisition/src030/cambridge-categorical-logic-author.pdf`; extraction: `tmp/acquisition/src030/cambridge-categorical-logic-author.layout.txt`. Printed page 48 is physical PDF page 49; printed 52 is physical 53; printed 55 is physical 56. These complete source pages were inspected visually, and the surrounding text in §§5.4–5.6 was read. No manuscript image was used as mathematical evidence.

Live package read: `handbook/registry/calculi/contextual-first-order.tex`, `sheet:contextual-first-order`; definitions `def:p10-contextual-first-order` and `def:p10-contextual-doctrine-interpretation` in the paired body file. The sheet retains the term-equation rules of Figure 1, sequent structural rules of Figure 2, natural-deduction rules of Figures 3, 5, and 7, and two explicit theory-axiom rows. The source's formula equality is distinct from its external term-equation judgment.

The source itself calls Figure 4 an alternative formulation (§5.4, pp.47–49), and says Figures 5/6 and 7/8 are interderivable (§5.5, p.51; §5.6, p.55). A compendium should therefore display the alternative presentation and its equivalence theorem. It need not make both presentations additional primitive rules of the same calculus.

## Meaning of the double rule line

Pitts explains the double line immediately under Figure 4, printed p.48: closure under a bi-rule means that all sequents above belong to the closed collection exactly when the sequent below belongs to it. Thus a two-premise bi-rule expands into one downward two-premise inference and two separate upward one-premise inferences. This is a metalevel equivalence of derivability, not an object-language implication or bi-implication formula. The empty upper side of `false-Adj` gives one zero-premise inference; its upward direction requires no conclusion.

The four Figure 4 schemata expand into nine ordinary rules; Figure 6 adds four, and Figure 8 adds two: **seven displayed bi-rules, fifteen substantive inference directions**. A derived-rule sheet may display seven double fractions, explaining their expansion, or register fifteen ordinary `hbrule` rows so that each direction has its own identifier.

All rules below restore the common finite variable context Γ suppressed by Pitts. Φ denotes a finite hypothesis list, not Γ. Source formula symbols are retained: `false`, `&`, `∨`, `⇒`, `∀_σ(ψ)`, `∃_σ(ψ)`, and `=_σ`. A unary formula abstraction ψ=(x)e has body ψ(x) and application ψ(M)=e[M/x], using Pitts's metalevel convention from §3, printed p.13. Every displayed judgment is well formed, substitutions avoid capture, and displayed extra variables are fresh declarations of the indicated sorts.

## Exact Figure 4 schemata, printed p.48

With every displayed sequent in the same variable context Γ:

\[
\frac{\Phi\vdash\psi\qquad\Phi\vdash\psi'}
     {\Phi\vdash\psi\mathbin{\&}\psi'}
\quad(\&\text{-Adj}),
\]

\[
\frac{\Phi,\psi\vdash\theta\qquad\Phi,\psi'\vdash\theta}
     {\Phi,\psi\vee\psi'\vdash\theta}
\quad(\vee\text{-Adj}),
\]

\[
\frac{\Phi,\psi\vdash\psi'}
     {\Phi\vdash\psi\Rightarrow\psi'}
\quad(\Rightarrow\text{-Adj}),
\qquad
\frac{}{\Phi,\mathsf{false}\vdash\psi}
\quad(\mathsf{false}\text{-Adj}).
\]

**All fractions in this section are double-line bi-rules in the source.** The single `\frac` is only portable note typography; a manuscript sheet must render the double line or register the individual directions. There are no extra eigenvariable conditions in Figure 4 beyond well-formedness in the common Γ.

The same Φ is essential in both premises of `&-Adj` and both premises of `∨-Adj`. The latter also retains Φ below the line. The surrounding pp.48–49 explain that this parameter stability expresses distributivity of finite meets over finite joins; the stable `false-Adj` requires no extra semantic condition. In the presence of implication the stability follows automatically, but **the source presentation actually displayed has Φ**. Page 49 explicitly retains Cut as part of the structural basis for equivalence and warns that proof structures can differ. Do not infer cut elimination for this adjoint presentation.

## Exact Figure 6 schemata, printed p.52

\[
\frac{\Phi\vdash\psi(x)\,[\Gamma,x:\sigma]}
     {\Phi\vdash\forall_\sigma(\psi)\,[\Gamma]}
\quad(\forall\text{-Adj}),
\]

\[
\frac{\Phi,\psi(x)\vdash\theta\,[\Gamma,x:\sigma]}
     {\Phi,\exists_\sigma(\psi)\vdash\theta\,[\Gamma]}
\quad(\exists\text{-Adj}).
\]

Again these are double-line bi-rules. Here x is fresh for Γ; ψ(x) is well formed in Γ,x:σ. For `∀-Adj`, every member of Φ is well formed in Γ, so x is not free in Φ. For `∃-Adj`, every member of Φ and θ is well formed in Γ, so x is free in none of them. These restrictions are explicitly identified in §5.5, printed p.51, as implicit consequences of well-formedness in the source's sequent convention. No witness term and no inhabitance hypothesis belongs to either bi-rule.

The surrounding equations are the two parameter-substitution identities (5.6)–(5.7), printed p.52, universal adjunction (5.8), p.52, existential adjunction (5.9), p.53, and Frobenius (5.10), p.53. With π:I×X→I, parameter map f:I'→I, A,C∈Prop(I), B∈Prop(I×X), and Q∈Prop(I×X), they state:

\[
 f^*\forall_{I,X}Q=\forall_{I',X}(f\times1_X)^*Q,
 \qquad
 f^*\exists_{I,X}Q=\exists_{I',X}(f\times1_X)^*Q;
\]
\[
 A\leq\forall_{I,X}B\iff\pi^*A\leq B,
 \qquad
 \exists_{I,X}B\leq C\iff B\leq\pi^*C;
\]
\[
 A\wedge\exists_{I,X}B
 =\exists_{I,X}(\pi^*A\wedge B).
\]

The source writes the quantifier operators as big meet/join symbols with subscripts I,X. The displayed `∃-Adj` corresponds to the stable equivalence
`A∧∃B≤C iff π*A∧B≤π*C`, not merely the parameter-free left-adjoint equivalence. Remark 5.5.2 identifies the first two identities as Beck–Chevalley and the last as Frobenius, and states that implication-preserving reindexing makes Frobenius automatic. These facts explain the source presentation but are not used as substitutes for the syntactic derivations below.

## Exact Figure 8 schema, printed p.55

\[
\frac{\Phi\vdash\psi(x,x)\,[\Gamma,x:\sigma]}
 {\Phi,(x=_\sigma x')\vdash\psi(x,x')\,[\Gamma,x:\sigma,x':\sigma]}
\quad(=\text{-Adj}).
\]

This is also a double-line bi-rule. The names x,x′ are distinct and fresh for Γ. The binary formula abstraction ψ has body ψ(x,x′) in Γ,x:σ,x′:σ. **Φ may depend on x**: it is a finite list of formulas in Γ,x:σ. Only x′ must be absent from its free variables. Requiring Φ to be independent of x would give only a special case of the source rule.

The next source display interprets equality by pulling back Eq_X along the pair of term arrows, equation (5.11). Equation (5.12), pp.55–56, confirms the full parameter dependence: its antecedent A belongs to Prop(I×X), not merely Prop(I). With the source's right-associated products it is

\[
 A\leq(1_I\times\Delta_X)^*B
 \iff
 (1_I\times\pi_1)^*A\wedge\pi_2^*\mathrm{Eq}_X\leq B,
\]

where B∈Prop(I×(X×X)), π₁:X×X→X, and π₂:I×(X×X)→X×X. The live manuscript uses canonically associated left products; its equality definition is exactly this after transport. Equation (5.13), p.56, is the special case
`top_X≤Δ_X*B iff Eq_X≤B`. It does not replace the full parameterized condition without additional hypotheses.

## Common structural derivation tools

These are finite syntactic manipulations in the actual sheet; no semantic completeness theorem is used.

1. **Add assumptions.** From Φ⊢χ and Id `Σ,χ⊢χ`, Cut gives Φ,Σ⊢χ. Exchange permits insertion at any location. This works when either list is empty.
2. **Contract repeated lists.** Exchange brings the two occurrences of each entry adjacent; repeated Contract removes duplicate occurrences. Finite lists require only finitely many applications. Formulas already repeated inside a list cause no difficulty.
3. **Instantiate the last fresh declaration.** Given a derivation in Γ,x:σ and a term M:σ[Γ], combine Eq-Refl `M=M:σ[Γ]` with the sheet's Subst to obtain simultaneous substitution of M for x in the entire sequent, in Γ. For a context Γ,x:σ,y:τ and terms M,N in Γ, eliminate x first by Subst with suffix y:τ and then eliminate y. No unused-variable deletion is being invoked.
4. **Extend a variable context.** Use the registered Weaken and freshen bound variables first. In particular, when introducing an extra variable with the same displayed name as a quantifier's argument variable, alpha-rename that binder before extension. This preserves the abstraction represented by the quantifier.

Use the same term-equation rules, structural sequent rules, and arbitrary theory-axiom rows on both sides of the comparison. Let ND denote that common basis plus Figures 3,5,7, and ADJ the common basis plus the fifteen directions of Figures 4,6,8. Every derivation below is relative to any fixed theory; no closure of its axioms under arbitrary renaming or substitution is assumed.

## Figure 4 from ND, every direction

**Conjunction downward.** Given Φ⊢ψ and Φ⊢ψ′, the registered `&-Intr` gives Φ,Φ⊢ψ&ψ′; contract the duplicate list. **Upward:** apply `&-Elim1` or `&-Elim2` to the conclusion sequent.

**Disjunction downward.** Given the two upper sequents, combine them by `∨-Elim` with Id `ψ∨ψ′⊢ψ∨ψ′`. This gives Φ,Φ,ψ∨ψ′⊢θ. Contract Φ and exchange if necessary. **Upward to the first premise:** derive ψ⊢ψ∨ψ′ from Id and `∨-Intr1`, then Cut against Φ,ψ∨ψ′⊢θ. Exchange yields Φ,ψ⊢θ. Use `∨-Intr2` in the same way for Φ,ψ′⊢θ.

**Implication downward.** This is precisely `⇒-Intr`. **Upward:** combine Φ⊢ψ⇒ψ′ with Id ψ⊢ψ by `⇒-Elim`, obtaining Φ,ψ⊢ψ′.

**False downward.** Id gives Φ,false⊢false; `false-Elim` gives Φ,false⊢ψ. There is no upward conclusion to prove.

## Figure 3 from ADJ, every included rule

**Conjunction introduction.** For premises Φ⊢ψ and Φ′⊢ψ′, add assumptions to put both in the common list Φ,Φ′, and use downward `&-Adj`. Both conjunction eliminations are upward directions of `&-Adj`.

**Disjunction introductions.** Id gives `ψ∨ψ′⊢ψ∨ψ′`. Read this as the lower sequent of `∨-Adj` with empty Φ and θ=ψ∨ψ′. Its upward directions give ψ⊢ψ∨ψ′ and ψ′⊢ψ∨ψ′. Cut either with the corresponding arbitrary premise Φ⊢ψ or Φ⊢ψ′.

**Disjunction elimination.** Given Φ,ψ⊢θ and Φ′,ψ′⊢θ, add assumptions and exchange so both have the common retained list Σ=Φ,Φ′. Downward `∨-Adj` gives Σ,ψ∨ψ′⊢θ. Cut with the third premise Φ″⊢ψ∨ψ′ and exchange to obtain Φ,Φ′,Φ″⊢θ.

**Implication introduction.** Use downward `⇒-Adj`. **Implication elimination:** from Φ⊢ψ⇒ψ′, its upward direction gives Φ,ψ⊢ψ′. Cut with Φ′⊢ψ and exchange to get Φ,Φ′⊢ψ′.

**False elimination.** The zero-premise `false-Adj` with empty Φ gives false⊢ψ. Cut with the given Φ⊢false.

These proofs establish the propositional package first, so subsequent ADJ derivations may use the just-derived ND propositional rules without circularity.

## Figure 6 from ND, every direction

**Universal downward.** Exactly `∀-Intr`, with its displayed freshness restriction. **Universal upward:** weaken Φ⊢∀_σ(ψ)[Γ] to Γ,x:σ, freshening the binder as described above, and apply `∀-Elim` to the well-sorted term x. The result is Φ⊢ψ(x)[Γ,x:σ].

**Existential downward.** Given Φ,ψ(x)⊢θ[Γ,x:σ], use Id `∃_σ(ψ)⊢∃_σ(ψ)[Γ]` as the first premise of `∃-Elim`; the given upper sequent is its second premise. The result is ∃_σ(ψ),Φ⊢θ[Γ], which Exchange puts in source order.

**Existential upward.** Id followed by `∃-Intr` with the term x gives ψ(x)⊢∃_σ(ψ)[Γ,x:σ]. Weaken the given lower sequent Φ,∃_σ(ψ)⊢θ[Γ] to the same extended context, then Cut and exchange. This yields Φ,ψ(x)⊢θ[Γ,x:σ].

## Figure 5 from ADJ, every included rule

**Universal introduction.** Downward `∀-Adj`. **Universal elimination:** upward `∀-Adj` turns the premise into Φ⊢ψ(x)[Γ,x:σ]. Instantiate x with the supplied well-sorted M by Eq-Refl and Subst. This yields Φ⊢ψ(M)[Γ]. A term is required; there is no implicit inhabitance assumption.

**Existential introduction.** Id gives ∃_σ(ψ)⊢∃_σ(ψ)[Γ]. Apply upward `∃-Adj` with empty retained hypothesis list and θ=∃_σ(ψ), obtaining ψ(x)⊢∃_σ(ψ)[Γ,x:σ]. Instantiate x with M, then Cut with the given Φ⊢ψ(M). This proves the live explicitly typed rule; Pitts's printed Figure 5 leaves the well-sorted witness condition implicit.

**Existential elimination.** Turn the second premise Φ′,ψ(x)⊢θ[Γ,x:σ] into Φ′,∃_σ(ψ)⊢θ[Γ] by downward `∃-Adj`. Cut with the first premise Φ⊢∃_σ(ψ) and exchange. The freshness of x for Φ′ and θ is exactly the bi-rule's well-formedness restriction.

## Figure 8 from ND, preserving the full antecedent

The forward derivation below uses implication from the full registered package. It is therefore a complete proof of the requested full-calculus interderivability, without asserting a stronger minimal-fragment result.

**First derive parameterized replacement.** Fix any parameter context K, terms a,b:σ[K], and a unary formula abstraction ρ with body ρ(z) in K,z:σ. Id and implication introduction give

`∅ ⊢ ρ(z)⇒ρ(z) [K,z:σ]`.

Use the binary abstraction χ(u,v)=ρ(u)⇒ρ(v). With first premise Id `a=_σb ⊢ a=_σb [K]`, the registered `=-Elim` and the preceding diagonal theorem give

`a=_σb ⊢ ρ(a)⇒ρ(b) [K]`.

The auxiliary variable z is fresh for K; the second premise has an empty hypothesis list, so it meets the actual rule's independence condition. Cut/implication elimination now gives replacement under arbitrary hypotheses whenever ρ(a) has been derived.

**Equality downward.** Suppose Φ(x)⊢ψ(x,x)[Γ,x:σ]. Extend to K=Γ,x:σ,x′:σ. In the replacement result set a=x, b=x′, and ρ(v)=ψ(x,v), with the first x a retained parameter. Thus

`x=_σx′ ⊢ ψ(x,x)⇒ψ(x,x′) [K]`.

Combine this with the weakened given sequent by implication elimination and exchange. The result is exactly Φ(x),x=_σx′⊢ψ(x,x′)[K]. This construction allows Φ to depend on x, as required by Figure 8; it does not attempt to use Φ(x) as an eigenvariable-independent premise of `=-Elim`.

**Equality upward.** From the lower sequent use Eq-Refl x=x:σ[Γ,x:σ] and Subst to replace x′ by x. This produces Φ(x),x=_σx⊢ψ(x,x)[Γ,x:σ]. Equality introduction gives ∅⊢x=_σx in that same context. Cut removes this equality assumption, leaving the upper sequent. The declaration x is retained throughout.

## Figure 7 from ADJ, every included rule

**Equality introduction.** Id gives

`x=_σx′ ⊢ x=_σx′ [Γ,x:σ,x′:σ]`.

Apply upward `=-Adj` with empty Φ and ψ(u,v)=(u=_σv). Obtain ∅⊢x=_σx[Γ,x:σ]. For any M:σ[Γ], instantiate x with M using Eq-Refl and Subst, obtaining ∅⊢M=_σM[Γ]. Add the arbitrary hypothesis list Φ to obtain the registered `=-Intr` conclusion.

**Equality elimination.** Start with its second premise

`Φ′ ⊢ ψ(z,z) [Γ,z:σ]`,

where Φ′ is well formed in Γ. Downward `=-Adj` yields

`Φ′,z=_σw ⊢ ψ(z,w) [Γ,z:σ,w:σ]`.

For M,N:σ[Γ], substitute z:=M first and w:=N second, each by Eq-Refl and the registered Subst. This gives Φ′,M=_σN⊢ψ(M,N)[Γ]. Cut with the first premise Φ⊢M=_σN and exchange gives Φ,Φ′⊢ψ(M,N)[Γ]. No object equality is converted into an external term equation.

## Equivalence theorem and presentation recommendation

Every inference direction of ADJ has now been replaced by a finite ND derivation, and every included logical rule of ND has been replaced by a finite ADJ derivation. The common rules and theory-axiom leaves are unchanged. Induction on a finite proof tree therefore gives, for every fixed theory T and every well-formed contextual sequent S,

\[
 T\vdash_{\mathrm{ND}}S\quad\Longleftrightarrow\quad
 T\vdash_{\mathrm{ADJ}}S.
\]

External term-equation derivability also agrees, since neither package adds a rule deriving term equations from sequents and their equational bases are identical. This equivalence includes empty hypothesis lists, empty ambient Γ, arbitrary sets of theory axioms, nullary signature symbols, and uninhabited sort interpretations. No rule of unused-variable deletion is used: declarations are discharged only by the displayed quantifier rules or by substitution of available well-sorted terms.

Recommended next insertion: one separately attributed **derived-rule sheet for Pitts's adjoint presentation**, displaying all seven bi-rules (or the fifteen explicitly directed `hbrule` rows), followed by a theorem that the alternate primitive presentation ADJ has the same derivable judgments when it replaces the ND logical rules over the common structural/equational basis. Supply the preceding syntactic proof in its paired annex. This both exhibits the source presentation in full and explains its exact relationship to the already registered sheet. Keep Cut in the common basis; do not call the double line an object bi-implication or identify proof trees between presentations.

The current body sentence saying that Figures 4,6,8 are not additional primitive rules can remain true, but should point to this separately displayed alternative presentation. It cannot serve as the sole coverage of those figures.

## Nearby source variant to keep distinct

Remark 5.6.2, printed p.56, displays the parameter-free equality bi-rule

\[
\frac{\varnothing\vdash\psi(x,x)\,[x:\sigma]}
 {(x=_\sigma x')\vdash\psi(x,x')\,[x:\sigma,x':\sigma]}.
\]

The surrounding sentence explicitly assumes implication and universal quantification to recover the full parameterized equality principle from this special case. This is a further source variant, not the Figure 8 schema; do not silently replace Figure 8 by it. Its syntactic parameter-abstraction proof is supplied below after the necessary context-transport lemma.

## Follow-up: exact source contexts and syntactic context transport

The source rules were checked again visually on printed pp.7 and 41, together with the **explicit unsuppressed formula on printed p.40**. There is no omitted-prefix discrepancy in the current sheet:

\[
\frac{M=M':\sigma\,[\Gamma]\qquad
 N=N':\tau\,[\Gamma,x:\sigma,\Gamma']}
 {N[M/x]=N'[M'/x]:\tau\,[\Gamma,\Gamma']}
\tag{Pitts 2.9}
\]

and the unsuppressed Figure 2 rule on p.40 is

\[
\frac{M=M':\sigma\,[\Gamma']\qquad
 \Phi(x)\vdash\psi(x)\,[\Gamma',x:\sigma,\Gamma]}
 {\Phi(M)\vdash\psi(M')\,[\Gamma',\Gamma]}.
\]

The different Γ/Γ′ lettering does not change the shared-prefix structure. In both cases the context interpreting M,M′ also occurs as the initial segment of the second premise. A rule with second premise only `[x:σ,Δ]` and a new unrelated Γ imported from the first premise would be a different rule.

Definition 2.1.1, printed p.6, explicitly defines contexts as finite **lists** of distinct variable/sort pairs. Remark 3.0.2, printed p.14, says only that a common left-hand part of the context is suppressed in displays. It does not identify context lists up to permutation or declare theory axioms invariant under renaming. Figure 2 Exchange permutes hypotheses, while Weaken appends variable declarations. Semantic product isomorphisms do not by themselves supply an inference rule.

**The Figure 8 proof above requires no variable-context permutation:** the original Γ,x context is extended at the right by x′ and then by the fresh equality-rule variable z. Its reverse direction substitutes x′:=x, using the prefix Γ,x. The ADJ-to-ND direction substitutes z:=M with remaining suffix w, and then w:=N. All these are literal instances of the printed shared-prefix rules.

Nevertheless the full predicate calculus proves the needed more general transport as follows. Let Γ=(x₁:σ₁,...,xₙ:σₙ), let Φ=(φ₁,...,φₘ), and suppose T proves Φ⊢ψ[Γ]. Let Δ be any finite variable context and let tᵢ:σᵢ[Δ] be a term for every variable of Γ. Define the nested formula

`D = φ₁ ⇒ (φ₂ ⇒ ... (φₘ ⇒ ψ)...)`,

with D=ψ when m=0. Apply implication introduction successively, discharging the last hypothesis first. This gives `∅⊢D[Γ]`. Apply universal introduction successively to xₙ,...,x₁, obtaining the closed sequent

`∅ ⊢ ∀_{σ₁}((x₁)∀_{σ₂}((x₂)...∀_{σₙ}((xₙ)D)...)) [()]`.

All eigenvariable restrictions hold because there are no undischarged hypotheses, and each eliminated declaration is last in the current context. For n=0 this is simply the same closed D. Alpha-rename these bound variables outside Δ and all tᵢ, then use context Weaken to append Δ. Apply universal elimination n times with t₁,...,tₙ. Capture-safe substitution gives `∅⊢D[t₁/x₁,...,tₙ/xₙ][Δ]`. Finally, eliminate its m nested implications successively against Id for each φᵢ[t], accumulating precisely the list Φ[t]. The result is

`T proves the sequent Φ[t] ⊢ ψ[t] [Δ]`.

Every original axiom leaf occurs in its original context inside the starting proof. No renamed axiom is inserted. Thus this is a finite syntactic admissibility proof relative to the same arbitrary T. Taking tᵢ to be suitably named variables yields renaming; taking Δ to be a permutation of Γ and tᵢ=xᵢ yields variable-context permutation. It applies to **predicate sequents**, using implication and universal quantification. It makes no claim that external term-equation transport is admissible, since internal equality cannot be reflected into external equality in the given calculus. The earlier semantic term-substitution theorem is not a replacement for such an external syntactic proof.

This lemma is available in both ND and ADJ: it uses ND implication and universal rules, already derived from ADJ before the equality comparison. It does not depend on any equality rule or on the target Figure 8 equivalence.

### Full proof for the nearby parameter-free equality variant

Call the p.56 parameter-free bi-rule `Eq0`. The full `=-Adj` immediately gives Eq0 by taking Γ and Φ empty. Conversely assume the common structural/equational basis, implication, universal quantification, and Eq0.

Given the upper sequent Φ(x)⊢ψ(x,x)[Γ,x:σ] of full `=-Adj`, discharge its finite list Φ into nested implications as above. Write

`D(u,v) = φ₁(u) ⇒ (... ⇒ (φₘ(u) ⇒ ψ(u,v))...)`,

where the members of Γ remain parameters. Then `∅⊢D(x,x)[Γ,x:σ]`. By the proved predicate-context transport put this in context x:σ,Γ; universally close the Γ declarations in reverse order. If Γ=(y₁:τ₁,...,yₖ:τₖ), define the binary abstraction

`χ(u,v) = ∀_{τ₁}((y₁)...∀_{τₖ}((yₖ)D(u,v))...)`.

The resulting sequent is `∅⊢χ(x,x)[x:σ]`. Downward Eq0 gives `x=_σx′⊢χ(x,x′)[x:σ,x′:σ]`. Append the fresh Γ declarations, instantiate these k universal quantifiers with y₁,...,yₖ, and eliminate the m implications against the assumptions Φ(x). Predicate-context transport then restores the source order Γ,x:σ,x′:σ. This yields the lower sequent of the full `=-Adj`.

For the reverse direction of full `=-Adj`, Eq0 applied upward to Id `x=_σx′⊢x=_σx′[x:σ,x′:σ]` proves `∅⊢x=_σx[x:σ]`. The predicate substitution lemma transports this reflexivity theorem to any needed context and any well-sorted term. From the given lower sequent, use the literal shared-prefix Subst to put x′:=x, then Cut with the resulting contextual reflexivity theorem. This recovers the upper sequent. The case of empty Γ or empty Φ simply omits the corresponding universal introductions or implication introductions. This completes the source's reduced-presentation equivalence under its stated extra logical hypotheses.

No other source body or reviewer conclusion was used for the mathematical derivations in this packet.
