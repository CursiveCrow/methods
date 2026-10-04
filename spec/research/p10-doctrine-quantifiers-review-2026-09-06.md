# First-order doctrine quantifiers: independent mathematical review

Date: 2026-09-06, local date.

## Outcome and scope

**Scoped mathematical pass. No necessary mathematical repair found.**

Read the complete actual files:

- handbook/parts/p10/doctrine-quantifiers.tex, lines 1–267;
- handbook/annex/p10/doctrine-quantifiers.tex, lines 1–280.

The review covers all four body/annex pairs: quantifier order laws, Frobenius, parameterized equality laws, and inhabitance/order reflection. Also checked the historical comparison directly against the held primary Lawvere reprint, pp. 11–12, and Pitts draft, pp. 46, 52–53, and 56, together with the already read predicate/equality pages. No other review conclusions were consulted.

Only this note was written. No manuscript edits, tests, builds, or renders were performed. The verdict does not establish host/driver integration, registry admission, typeset quality, or the subsequent formula-soundness theorem.

## 1. Definition, types, and source scope

Body lines 25–81 explicitly specify a locally small base with chosen finite products, small Heyting fibres, and reindexing preserving all five indicated Heyting operations. The contravariant direction
\[
f:J\to I,\qquad f^*:P(I)\to P(J)
\]
and the composite law \((fg)^*=g^*f^*\) agree.

For \(\pi:I\times A\to I\), the types of both quantifier maps are \(P(I\times A)\to P(I)\). The two adjunctions at body lines 53–62 have the correct directions. Both Beck–Chevalley equations at lines 63–74 have common type \(P(I\times A)\to P(J)\), and require only the indicated product substitution squares. The definition does not silently assume arbitrary base pullbacks or adjoints along all arrows.

The historical paragraph at body lines 13–23 is accurate. Lawvere's 2006 reprint pp. 11–12 defines category-valued fibres, a cartesian closed base and cartesian closed attribute categories, and both adjoints along every base arrow; p. 12 explicitly says substitution need not preserve implication. The manuscript does not identify that package with its more specific posetal convention.

Pitts Definition 5.4.1, p. 46, requires the stated propositional structure to be preserved by reindexing. Equations (5.6)–(5.9), pp. 52–53, provide parameter naturality and the two projection adjunctions. The manuscript's projection codomain is the correctly typed parameter object \(I\), rather than reproducing the source definition's codomain slip. Pitts treats Frobenius separately in the finite-meet presentation and explains its consequence under implication-preserving reindexing in Remark 5.5.2, p. 53. The local proof accurately supplies that consequence.

## 2. Product squares and quantifier order laws

Annex:p10.quant.1, lines 7–21, proves the product square is a pullback from its full universal property. Given \(a:K\to J\) and \(b:K\to I\times A\) with \(fa=\pi_{I,A}b\), the mediator
\[
h=\langle a,\pi_A b\rangle:K\to J\times A
\]
has the correct two composites. Any other mediator has the same two projections. This argument requires only finite products.

The uniqueness argument at lines 23–33 characterizes a left-adjoint value by all its upper bounds and a right-adjoint value by all its lower bounds. Antisymmetry supplies uniqueness without any selection principle.

The four unit/counit inequalities at lines 35–41 are correctly obtained by instantiating the two adjunctions. The proofs at lines 43–74 establish preservation of binary joins and bottom by \(\exists_\pi\), and binary meets and top by \(\forall_\pi\). They do not require unasserted arbitrary meets or joins in the fibres.

For Boolean fibres, lines 76–94 correctly use preservation of negation, which follows from preservation of implication and bottom, and Boolean double-negation laws in both fibres. The chain
\[
\beta\leq\neg\exists_\pi\neg\alpha
\iff \exists_\pi\neg\alpha\leq\neg\beta
\iff \neg\alpha\leq\neg\pi^*\beta
\iff \pi^*\beta\leq\alpha
\iff \beta\leq\forall_\pi\alpha
\]
has the right directions and types. No Beck–Chevalley identity enters these order calculations. The one-element Heyting or Boolean fibre causes no exception.

## 3. Frobenius

Annex:p10.quant.2, lines 102–128, correctly keeps \(a\in H\) and \(b,c\in K\). Every step of
\[
L(a\wedge Rb)\leq c
\iff a\wedge Rb\leq Rc
\iff a\leq(Rb\Rightarrow Rc)
\iff a\leq R(b\Rightarrow c)
\iff La\leq b\Rightarrow c
\iff La\wedge b\leq c
\]
is justified by the stated adjunction, residuation in the appropriate fibre, or the explicit implication-preservation hypothesis. Testing the two values themselves as upper bounds proves equality.

The doctrine instantiation has \(H=P(I\times A)\), \(K=P(I)\), \(L=\exists_\pi\), and \(R=\pi^*\), exactly as required. The proof does not replace implication preservation with finite-meet preservation, and does not use Beck–Chevalley.

## 4. Equality with the left-associated product

Body lines 147–188 correctly type all four maps:

- \(e(i,a)=((i,a),a)\);
- \(p((i,a),b)=(i,a)\);
- \(q((i,a),b)=(i,b)\);
- \(r((i,a),b)=(a,b)\).

The product is \((I\times A)\times A\). Thus
\[
L_e(\alpha)=p^*\alpha\wedge r^*\delta_A
\]
has domain \(P(I\times A)\) and codomain \(P((I\times A)\times A)\); it is correctly left adjoint to \(e^*\). Pitts's right-associated source formula is explicitly related by canonical rebracketing in body lines 190–194.

### Reflexivity

Annex lines 134–152 apply the adjunction unit at top, giving
\(\top_{I\times A}\leq e^*r^*\delta_A\).
At \(I=1\), \(re=\Delta_A\pi_A\). Pulling back along
\[
s_A=\langle!_A,1_A\rangle:A\to1\times A
\]
uses \(\pi_A s_A=1_A\), yielding \(\top_A\leq\Delta_A^*\delta_A\). The reverse inequality is the top bound. This retains the actual \(1\times A\); \(s_A\) is the canonical terminal-product map, not a global element \(1\to A\), so no inhabitance is assumed.

### Parameterized replacement

Annex lines 154–166 use \(qe=1_{I\times A}\). Thus
\(\gamma\leq e^*q^*\gamma=\gamma\), and the left adjunction gives precisely
\[
p^*\gamma\wedge r^*\delta_A\leq q^*\gamma.
\]
Parameters are retained throughout.

### Symmetry and transitivity

For symmetry, annex lines 168–191 take \(I=A\), \(\gamma=\tau_A^*\delta_A\), and
\[
m=\langle\Delta_A\pi_1,\pi_2\rangle:
A\times A\to(A\times A)\times A.
\]
The three composites are \(pm=\Delta_A\pi_1\), \(rm=1\), and \(qm=1\). The first reindexed conjunct is top by reflexivity and \(\tau_A\Delta_A=\Delta_A\); the resulting inequality is \(\delta_A\leq\tau_A^*\delta_A\). Reindexing by the involution gives the other direction.

For transitivity, lines 193–197 specialize replacement to \(I=A,\gamma=\delta_A\). The pairs selected by \(p,r,q\) are exactly the first/second, second/third, and first/third coordinates. The statement's inequality is therefore the usual transitivity relation.

### Congruence and limits of the conclusion

For \(f:A\to B\), annex lines 199–212 put \(\gamma=(f\times f)^*\delta_B\). The equation \((f\times f)\Delta_A=\Delta_Bf\) and reflexivity in \(B\) give \(\Delta_A^*\gamma=\top_A\). Applying the same replacement map \(m\) yields \(\delta_A\leq\gamma\), exactly the claimed arrow preservation.

For completeness of the parameter interpretation, the full equality axiom also applies directly to a term arrow \(f:I\times A\to B\): put \(\beta=\langle fp,fq\rangle^*\delta_B\). Since \(pe=qe=1\), reflexivity gives \(e^*\beta=\top_{I\times A}\). The adjunction at top then gives \(r^*\delta_A\leq\beta\). Thus the available axiom supports term congruence with parameters as well.

The manuscript correctly stops at internal equality preservation. It does not infer equality of base arrows from equality of their predicates, or require a subobject representation.

## 5. Inhabitance and unused variables

Body lines 227–261 and annex:p10.quant.4, lines 224–278, are correctly scoped.

Existential Beck–Chevalley along \(!_I:I\to1\), together with top preservation, carries inhabitance at the terminal parameter to
\[
\exists_{\pi_{I,A}}\top_{I\times A}=\top_I
\]
for every \(I\). The converse simply chooses \(I=1\).

A given global element \(a:1\to A\) supplies the section
\(s=\langle1_1,a\rangle:1\to1\times A\). Reindexing the existential unit at top along this section proves inhabitance. The theorem asserts sufficiency of a global element, not its equivalence with internal inhabitance.

For an inhabited \(A\), Frobenius gives
\[
\exists_\pi\pi^*\beta
=(\exists_\pi\top)\wedge\beta=\beta.
\]
Applying the monotone existential adjoint to
\(\pi^*\alpha\leq\pi^*\beta\) now proves \(\alpha\leq\beta\). The converse is monotonicity. This establishes order reflection before it is used in the universal calculation.

The universal unit gives \(\beta\leq\forall_\pi\pi^*\beta\). Its counit gives
\(\pi^*\forall_\pi\pi^*\beta\leq\pi^*\beta\), and the already proved order reflection supplies the reverse inequality. Thus both unused-quantifier identities are established without a Boolean-fibre assumption.

Finally, reindexing a finite-antecedent sequent preserves the conjunction of assumptions and its conclusion. Removing an unused variable is therefore exactly the proved order-reflection equivalence. For several extensions, inhabitance is available at every intermediate parameter context by the first part of the proof. No removal from an uninhabited sort is inferred.
