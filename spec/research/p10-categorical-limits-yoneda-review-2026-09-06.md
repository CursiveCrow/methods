# Categorical limits and Yoneda: independent actual-text review

Review date: 2026-09-06 (local date).

## Final outcome and scope

**Scoped mathematical pass after the integrating author applied the reported size and hypothesis repairs.** I read back the actual repairs. No remaining necessary mathematical correction was found in the assigned first half.

Read the category and equivalence definitions, limits/colimits and product/equalizer definitions, and the complete statements and proofs of:

- thm:p10-limits-unique / annex:p10.cat.1;
- thm:p10-limits-products-equalizers / annex:p10.cat.2;
- thm:p10-yoneda / annex:p10.cat.3.

Files: handbook/parts/p10/categorical-toolkit.tex and handbook/annex/p10/categorical-toolkit.tex. Final line anchors below refer to the saved text read after the corrections, at approximately 03:49 UTC on 7 September 2026. The first-half body statements now end at line 231 and the three annex items at line 193.

No other review conclusions were consulted. Only this note was written by this reviewer. No manuscript edit, test, build, or render was performed. Source-attribution and the adjunction/exponential half are outside this review's conclusion.

## Reported repairs, now verified in the manuscript

### 1. Small diagrams refer to their indexing categories

The original opening equated a small diagram with diagram data belonging to the fixed universe. This would incorrectly restrict diagrams into a large category: a finite indexing category can select an object outside the fixed universe, so the functor data need not themselves be small.

The corrected body, lines 6–13, states separately that a small set belongs to the fixed universe, a small category has small object and arrow sets, and a small diagram has a small indexing category. Its values may lie in a large category. This is the condition actually used by the products/equalizers construction.

### 2. Yoneda gives a small parameter set, not fixed-universe membership of whole component families

The original theorem concluded that the actual ambient family of natural transformations is small, solely from its bijection with \(F(A)\). That does not follow when “small” means belonging to a fixed universe \(U\).

For example, let \(\mathcal C=\mathsf{Set}_U\) and \(H=\mathcal C(-,1)\). There is exactly one transformation \(H\Rightarrow H\): every component maps a singleton set to itself. The transformation, as the complete family of components indexed by all objects of \(\mathsf{Set}_U\), has domain \(U\), so it does not itself belong to \(U\). Its singleton collection need not belong to \(U\), even though the parameter set \(H(1)\) does. All these families may be formed in the containing ambient universe.

Corrected body lines 217–222 now assert canonical parametrization by the small set \(F(A)\), while distinguishing the size of each entire component family. Corrected annex lines 160–164 explicitly give a bijection between the ambient transformation family and the small parameter set. Both are accurate. The original Yoneda maps and proof remain valid.

### 3. The poset example needs the smallness hypothesis

Corrected body lines 57–61 say that a **small** partially ordered set yields a small category. A general ambient poset need not have its object set in the fixed universe. The order-category construction itself is unchanged and correct.

### 4. The universal properties are explicit hypotheses

Corrected annex line 27 specifies that \(e:E\to A\) **is an equalizer** of \(f,g\), rather than merely an arrow that equalizes them. This supplies the unique factorization used to prove monicity.

Corrected annex line 91 says to **take a coequalizer** \(q:S\to K\) of \(s,t\), rather than only to choose an arrow coequalizing them. This supplies the factorization property used to construct the colimit.

## Definitions and uniqueness proof

Body lines 15–77 give correctly typed composition, functor, opposite-category, natural-transformation, fullness, faithfulness, and equivalence data. The naturality equation for \(\alpha:F\Rightarrow G\) has both sides \(FA\to GB\). Componentwise inverses satisfy the naturality equation in the reverse direction. The equivalence definition requires quasi-inverse functors and natural isomorphisms; it does not incorrectly assert triangle identities for arbitrary chosen isomorphisms.

The cone and cocone definitions at body lines 88–111 use the right directions:
\[
D(u)p_j=p_k,\qquad q_kD(u)=q_j.
\]
Their mediating arrows have types \(X\to L\) and \(K\to X\), respectively. Empty diagrams correctly give terminal and initial objects.

The product, coproduct, equalizer, coequalizer, pullback, pushout, mono, and epi definitions at body lines 113–144 have the correct universal-property and cancellation directions.

Annex cat.1, lines 7–25, constructs inverse mediators between two universal cones/cocones and applies uniqueness to their composites. It proves uniqueness of the leg-preserving isomorphism, rather than uniqueness of every isomorphism of the underlying objects. The empty diagram is explicitly included.

Annex lines 27–33 prove equalizers monic and coequalizers epic from their now explicit universal hypotheses. Lines 35–42 prove pairing precomposition and the identity/composition laws for product arrows by comparing projections. All compositions are correctly typed.

## General limit and colimit constructions

For a small diagram, annex lines 48–76 form
\[
P=\prod_{j\in\operatorname{Ob}J}Dj,\qquad
Q=\prod_{u:j\to k}Dk.
\]
Both products have small indexing sets because \(J\) has small object and arrow sets. The parallel maps \(s,t:P\to Q\) have components \(D(u)\pi_j\) and \(\pi_k\). Their equalizer gives the required compatible cone. Existence and uniqueness of a mediator use the product and equalizer properties in the correct order.

The explicit dual construction at annex lines 80–106 uses
\[
R=\coprod_{u:j\to k}Dj,\qquad
S=\coprod_jDj,
\]
with \(s\rho_u=\iota_kD(u)\) and \(t\rho_u=\iota_j\). Their coequalizer produces the cocone. The proof checks its commutativity, factors every cocone, and proves uniqueness using the coproduct and coequalizer properties. It does not rely solely on an unstated duality instruction.

The arrow index includes identities; their redundant compatibility equations are harmless. The empty index makes the two products terminal and the two coproducts initial, and the constructions retain the correct universal property even if different terminal/initial representatives were chosen.

Annex lines 108–115 correctly restrict the finite construction to categories with finitely many objects **and arrows**. Binary products plus a terminal object build every finite product; the coproduct statement is dual. The proof does not confuse finite object sets with finite diagrams having an unrestricted arrow set. Local smallness in the theorem is a sufficient hypothesis; no stronger size assumption is silently used.

## Set constructions and absence of hidden representative choices

Annex lines 117–121 prove the compatible-tuples subset is a limit by the coordinate function \(x\mapsto(a_j(x))_j\). Every coordinate is prescribed, proving uniqueness. This does not assume that an arbitrary Cartesian product is nonempty.

The colimit relation at lines 122–124 exists as the intersection of all equivalence relations containing the generating pairs. The universal relation is one such relation, so the family being intersected is available.

At lines 125–132 the cocone equations put all generating pairs in the kernel of the induced function on the disjoint union. Consequently that function is constant on every generated equivalence class, and the displayed quotient function is well-defined. Existence of a representative in each equivalence class proves pointwise uniqueness; no simultaneous selection of representatives is needed.

Lines 133–135 cover the empty diagram: the product is the singleton containing the empty tuple, and the disjoint union and quotient are empty.

## Yoneda maps, both naturalities, and representable isomorphisms

Local smallness makes every representable value \(\mathcal C(X,A)\) an object of \(\mathsf{Set}\). For \(x\in F(A)\), annex lines 141–151 define
\[
\alpha^x_X(f)=F(f)(x)
\]
and verify naturality for \(u:Y\to X\) through
\[
F(u)F(f)(x)=F(fu)(x).
\]
Evaluation at \(1_A\) recovers \(x\).

Lines 153–164 use the naturality square of a given transformation at \(f:X\to A\) to obtain
\[
\alpha_X(f)=F(f)(\alpha_A(1_A)).
\]
This proves the inverse direction and the corrected ambient-family/small-parameter conclusion.

Naturality in \(F\), annex lines 166–169, is covariant: postcomposition with \(\theta:F\Rightarrow H\) corresponds to \(\theta_A:F(A)\to H(A)\).

Naturality in \(A\), annex lines 170–179, is contravariant in the displayed parameter: for \(h:A\to B\), precomposition with \(\mathcal C(-,h)\) corresponds to \(F(h):F(B)\to F(A)\). The equation \(\alpha_A(h)=F(h)(\alpha_B(1_B))\) has the correct direction.

Finally, annex lines 181–191 identify transformations between representables with postcomposition by a unique arrow. Identity and composition are preserved. Fullness represents the inverse transformation, and faithfulness turns its two identity composites into inverse equations for the representing arrows. Thus the claimed full faithfulness and reflection of representing-object isomorphisms follow.
