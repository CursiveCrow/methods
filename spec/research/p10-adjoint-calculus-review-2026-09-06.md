# Adjoint first-order presentations: independent mathematical and source review

Date: 2026-09-06, local date.

## Verdict and scope

**Scoped pass. No necessary mathematical or rule-incorporation repair found.**

Read the complete actual body and annex:

- handbook/parts/p10/adjoint-first-order-calculus.tex, lines 1–136;
- handbook/annex/p10/adjoint-first-order-calculus.tex, lines 1–410.

Read both complete sheets:

- handbook/registry/calculi/contextual-adjoint-first-order.tex, lines 1–17;
- handbook/registry/calculi/contextual-parameter-free-equality.tex, lines 1–4.

Compared the sheets directly with the held Pitts1995Draft, visually inspecting the complete printed pages 48, 52, 55, and 56: Figures 4, 6, 8, and Remark 5.6.2. Source: Andrew M. Pitts, *Categorical Logic*, draft 18 May 1995, held at tmp/acquisition/src030/cambridge-categorical-logic-author.pdf; [author PDF](https://www.cl.cam.ac.uk/~amp12/papers/catl/catl.pdf).

No other reviewers' conclusions were consulted. Only this note was written. Source-page inspection used in-memory images; there were no manuscript edits, tests, builds, or manuscript renders.

## 1. All source directions are present

The count of fifteen directed ADJ inferences is correct:

| Source bi-rule | Directions | Registry lines | Source locator |
| --- | ---: | --- | --- |
| Conjunction | 3 | 3–5 | Fig. 4, p. 48 |
| Disjunction | 3 | 6–8 | Fig. 4, p. 48 |
| Implication | 2 | 9–10 | Fig. 4, p. 48 |
| false | 1 | 11 | Fig. 4, p. 48 |
| Universal | 2 | 12–13 | Fig. 6, p. 52 |
| Existential | 2 | 14–15 | Fig. 6, p. 52 |
| Equality | 2 | 16–17 | Fig. 8, p. 55 |

The source explains below Figure 4 that all upper sequents are derivable iff the lower sequent is derivable. Accordingly, two upper sequents give one downward rule and two individual upward rules. The empty upper side of false-Adj gives a zero-premise lower inference, not an additional assertion with an empty conclusion.

The identical retained hypothesis list in conjunction and disjunction is preserved. The retained list in disjunction and existential adjunction is not dropped. Universal and existential eigenvariable conditions are correct.

Full equality permits \(\Phi\) to depend on the first variable \(x\), but not the added \(x'\). The sheet explicitly preserves this possibility. It matches the source's full parameterized equality condition (5.12), whose antecedent is an arbitrary predicate over the parameter object times the first copy of the sort.

The Eq0 sheet contains both directions of the completely parameter-free form: no retained hypotheses and exactly the displayed equality variables. This is the explicit form associated with Remark 5.6.2 and its parameter-free diagonal-top condition (5.13). The body's local Eq0 definition makes this scope explicit; additional bound variables inside the formula are permitted.

Source unary abstraction notation \(\forall_\sigma(\psi)\), \(\exists_\sigma(\psi)\), and metalevel \((x)e\) notation are preserved. ND and ADJ are locally declared names of derivability presentations, not new object-language connectives.

## 2. Predicate transport is genuinely syntactic

Body theorem lines 55–75; annex:p10.adjoint.1, lines 7–83.

Implication introduction discharges the finite hypothesis list from last to first, producing the right-nested formula
\[
D=\phi_1\Rightarrow(\phi_2\Rightarrow\cdots(\phi_m\Rightarrow\psi)\cdots)
\]
with no hypotheses. This preserves multiplicities in a list with repeated formulas.

Universal introduction then closes the variable context from its last declaration to its first. Every introduction satisfies the eigenvariable condition because there are no remaining hypotheses, and the declaration being removed is last. The resulting sequent is in the empty variable context.

After bound alpha-renaming outside the target context and all substituting terms, context Weaken appends the target context. Successive universal eliminations use the supplied well-sorted terms in that exact retained context. Freshening prevents an earlier instantiation from changing or capturing a later inserted term, so the result is simultaneous substitution.

Implication eliminations with the separate Id sequents reinstate the substituted hypotheses in their original order. Empty hypothesis lists omit these steps; empty source contexts omit universal closure. An empty target context requires closed terms for every source declaration, as the theorem states.

The crucial same-theory property is justified at annex lines 70–75: the original derivation remains a subtree. No axiom leaf is renamed, permuted, or substituted. Only its derived conclusion is discharged, closed, and instantiated. Thus arbitrary theories need not be closed under free-variable renaming.

The proof applies only to predicate sequents. It does not infer an external term equation by universal closure or equality-formula reflection. It gives the specific context permutations used later without treating semantic product isomorphisms as proof rules.

## 3. Every ND–ADJ translation

Annex:p10.adjoint.2, lines 89–308.

### Structural preparation and prefix discipline

Lines 93–111 derive assumption weakening from Id and Cut, and use only hypothesis Exchange and Contract to rearrange or merge finite lists. These are distinct from variable-context permutations.

Every direct use of Subst has its exact source prefix. A term \(M\) in \(\Gamma\) is inserted into \(\Gamma,x:\sigma,\Delta\) while retaining the suffix \(\Delta\). For two appended variables, the proof first substitutes the first while retaining the second, then substitutes the second. Eq-Refl supplies the required external equation premises. No unsupported general transport of external equations is used.

### Propositional rules in both directions

Lines 113–143 derive the four ADJ bi-rules from ND. Conjunction introduction initially duplicates the retained list and then contracts it. Disjunction-down uses the two branch premises and Id for the disjunction, followed by contraction. Each disjunction-up uses the corresponding injection and Cut. Implication-up applies implication elimination to an Id premise, and false-Adj follows from Id plus false elimination.

Lines 145–176 derive all ND propositional rules from ADJ. Separate premise lists are enlarged and exchanged to the same retained list when needed. Disjunction introductions arise from the upward directions applied to Id for the disjunction. ND disjunction elimination then follows from its two branches by ADJ-down and a Cut with the third premise. Implication and false elimination are likewise obtained with the stated Cuts.

All antecedent orders and multiplicities can be restored by the listed finite structural steps. Empty lists cause no exception.

### Quantifier rules in both directions

Lines 178–201 derive the quantifier bi-rules from ND. Universal-up first extends the context and then instantiates with its newly declared variable, freshening the quantifier binder. Existential-down uses Id for the existential formula and ND elimination. Existential-up uses its declared variable as a typed witness, weakens the lower sequent, and Cuts.

Lines 203–222 derive the four ND rules from ADJ. Universal elimination is ADJ-up followed by literal-prefix Subst. Existential introduction first obtains \(\psi(x)\vdash\exists_\sigma(\psi)\), instantiates with the supplied well-sorted witness, then Cuts. Elimination uses ADJ-down on the second premise and Cuts with the existential premise.

The retained hypotheses, and the existential conclusion, satisfy the correct eigenvariable exclusions. No witness is manufactured without a well-sorted term, and no inhabitance of a sort is assumed.

### Full equality from ND, including \(\Phi(x)\)

Lines 224–270 correctly avoid imposing independence of \(\Phi\) from the first equality variable.

First, for a fresh variable \(z\) after a retained context \(K\), Id and implication introduction give the empty-hypothesis diagonal tautology
\[
\vdash\rho(z)\Rightarrow\rho(z)\,[K,z:\sigma].
\]
ND equality elimination, applied to the binary abstraction
\(\rho(u)\Rightarrow\rho(v)\), yields
\[
(M=_\sigma N)\vdash\rho(M)\Rightarrow\rho(N)\,[K].
\]
Its diagonal hypothesis list is empty, satisfying the actual ND equality rule.

For full ADJ-down, take \(K=\Gamma,x:\sigma,x':\sigma\), \(M=x\), \(N=x'\), and \(\rho(v)=\psi(x,v)\), retaining the first \(x\) as a parameter. Implication elimination combines the resulting replacement implication with the weakened original premise. The entire original \(\Phi(x)\) is retained.

For ADJ-up, literal-prefix substitution \(x':=x\) leaves \(x\) declared. Equality introduction and Cut then remove only the diagonal equality assumption.

### ND equality from full ADJ

Lines 272–298 obtain reflexivity by applying ADJ-up to Id for the equality formula. Substitution of an arbitrary supplied \(M\), followed by assumption weakening, gives exactly ND equality introduction.

For elimination, ADJ-down is applied to the ND rule's second premise. The two equality variables are then instantiated in the permitted prefix order, yielding \(\Phi',(M=_\sigma N)\vdash\psi(M,N)\). Cut with the first premise gives the registered conclusion.

These arguments use implication where it is available in the full ND package; the theorem does not assert that the isolated equality fragment alone proves every direction.

Lines 300–308 validly extend the rule translations by induction over finite proof trees. Both calculi have the same external-equation subsystem and no predicate-to-external-equation rule, so agreement of external equation derivability follows separately. Cut is explicitly retained.

## 4. Eq0 recovers full parameterized equality

Annex:p10.adjoint.3, lines 314–408.

Full equality immediately supplies Eq0 by the stated special cases. For the converse, the only additional logical rules used are implication and universal quantification.

For the downward direction, the retained list is discharged into
\[
D(u,v)=\phi_1(u)\Rightarrow
(\phi_2(u)\Rightarrow\cdots(\phi_m(u)\Rightarrow\psi(u,v))\cdots).
\]
The first argument \(u\), not \(v\), is used in every retained assumption. This is what preserves arbitrary dependence of \(\Phi\) on \(x\).

The already proved predicate-transport theorem moves the parameter context behind \(x\). Universal introduction closes those parameter declarations from right to left. The resulting binary abstraction \(\chi\) has no free parameter context, so Eq0-down applies to \(\vdash\chi(x,x)\,[x:\sigma]\).

Before reinstating the old parameter declarations, their now-bound names are freshened. Weaken appends the parameter context, universal elimination inserts its well-sorted variables, and implication elimination reinstates every assumption. Hypothesis Exchange and predicate-context transport restore exactly the original lower full-equality sequent.

For the upward direction, Eq0-up first gives the reflexivity formula in the single-variable context. Predicate transport supplies it in \(\Gamma,x:\sigma\). Literal-prefix substitution \(x':=x\) in the given lower full-equality premise, followed by Cut with this reflexivity formula, gives the upper premise.

The transport theorem used here assumes only the common basis plus the same implication/universal rules already present. Thus there is no circular use of full equality to obtain Eq0's parameter restoration.

Both empty-list cases are explicitly handled. There is no semantic-completeness argument, context erasure, external term-equation transport, equality reflection, conjunction/disjunction/existential dependency, or cut-elimination claim in this reduction.
