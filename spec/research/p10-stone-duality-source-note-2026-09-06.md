# Stone duality: primary-source locators and incorporation details

Date: 2026-09-06. Bounded source reading of Burris and Sankappanavar, *A Course in Universal Algebra*, Millennium Edition, 2012 Update, Chapter IV §§3–4. The electronic text preserves the 1981 main-page pagination. Source descriptions below are paraphrases; mathematical formulations and naturality calculations are supplied explicitly for manuscript use.

Source: <https://www.math.uwaterloo.ca/~snburris/htdocs/UALG/univ-algebra2012.pdf>. Held copy: `tmp/pdfs/p10-burris-sankappanavar-1981/univ-algebra2012.pdf`. Main printed page p is one-based physical PDF page p+14. Sections IV§3–4 occupy printed pp127–141; the principal duality theorem is on pp136–138. Read the complete relevant section pages, including the exercise list. No other agents' outputs were consulted. No manuscript edits, tests, builds, or manuscript renders were performed.

## Exact locators and hypotheses

| Claim | Source locator | Exact mathematical scope |
| --- | --- | --- |
| Filter and ideal definitions | IV Definition 3.1, p127 | Filters contain 1, are closed under binary meets, and are upward closed. Ideals are the dual notion. Neither definition by itself requires properness. |
| Generated filters and ideals | IV Definition 3.8 and Lemma 3.9, p131 | The generated filter consists of elements above a finite meet of generators, also including 1. Dually for ideals and finite joins, including 0. |
| Ultrafilters | IV Definition 3.11, p132 | A filter maximal among filters omitting 0. Maximal ideals are maximal among ideals omitting 1. The text explicitly observes that only nontrivial Boolean algebras have these objects. |
| Complement criterion | **IV Theorem 3.12, pp132–133** | For a filter F of B, F is an ultrafilter iff exactly one of a and its complement belongs to F for every a∈B. The analogous criterion holds for an ideal being maximal. |
| Finite-join primeness | IV Corollary 3.13(a), p133 | A filter F is an ultrafilter iff 0∉F and a∨b∈F exactly when a∈F or b∈F. Part (b) gives the dual ideal statement. |
| Prime ideals | IV Definition 3.14, p133 | A proper ideal is prime when a∧b in it implies that at least one factor is in it. The preceding result identifies prime and maximal ideals in Boolean algebras. |
| Separation | IV Theorem 3.15, pp133–134 | If a≠0 there is a prime ideal omitting a; if a≠1 there is an ultrafilter omitting a. |
| Inverse image of ultrafilters | **IV Lemma 3.16, p134** | For any Boolean homomorphism h:B→C and any ultrafilter U of C, h⁻¹[U] is an ultrafilter of B. No injectivity or surjectivity assumption on h is needed. |
| Extension with exclusion | **IV Theorem 3.17, p134** | If F is a filter and a∉F, some ultrafilter U contains F and omits a. The ideal version extends I while omitting an element outside I. Setting a=0 gives extension of every proper filter. |
| Boolean/Stone spaces | **IV Definition 4.1, p135** | A Boolean space is Hausdorff, compact, and has a basis of clopen sets. No nonemptiness condition is imposed. |
| Ultrafilter topology | IV Definition 4.2, p135 | B* has the ultrafilters of B as points, with the sets N_a={U:a∈U} as a subbasis. |
| Basic-set identities | IV Lemma 4.3, pp135–136 | N_(a∨b)=N_a∪N_b, N_(a∧b)=N_a∩N_b, and N_(¬a)=B*\N_a. Consequently these sets already form a basis. |
| Clopen algebra | IV Lemma 4.4 and Definition 4.5, p136 | For every topological space X, its clopen subsets form a Boolean subalgebra of its powerset algebra; no compactness or separation assumption is needed for this claim. |
| Algebra representation and compactness | **IV Theorem 4.6(a), pp136–137** | For every Boolean algebra B, B* is a Boolean space and a↦N_a is an isomorphism B→Clop(B*). |
| Space reconstruction | **IV Theorem 4.6(b), pp136–138** | For every Boolean space X, x↦{C∈Clop(X):x∈C} is a homeomorphism X→Ult(Clop(X)). |
| Homomorphism-to-continuous map | **IV §4 Exercise 9, p140** | h:B→C induces h*:C*→B*, U↦h⁻¹[U]. It is continuous; surjective h gives injective h*, and injective h gives surjective h*. |
| Continuous-map-to-homomorphism | **IV §4 Exercise 10, p140** | f:X→Y between Boolean spaces induces f*:Clop(Y)→Clop(X), D↦f⁻¹[D]. It is a Boolean homomorphism; surjective f gives injective f*, and injective f gives surjective f*. |

The source proves the object-level maps in Theorem 4.6. It expressly leaves the homomorphism/continuous-map relationship to exercises on p140. It does **not** state the functor laws and natural isomorphisms there as an additional numbered theorem. Cite Exercises 9–10 for the morphism constructions and provide the naturality calculations below as part of the manuscript's proof.

## Ultrafilter separation and the choice dependency

Theorem 3.17(a), with a=0, is the precise source form of proper-filter extension. It supplies every ultrafilter existence used below. An elementary proof of the complement criterion from maximality proceeds as follows: if a∉U, adjoining a must generate the improper filter, so u∧a=0 for some u∈U; hence u≤¬a and ¬a∈U. Conversely, if a proper filter decides each complement pair, adding any outside element makes it improper. This direct proof avoids the source's detour through simple quotient algebras.

For a≰b, a∧¬b is nonzero. Its principal filter is proper, so an ultrafilter extending it contains a and omits b. In particular distinct a,b are separated by an ultrafilter, applying this to one of the two failed order relations. Alternatively, source Theorem 3.15(a) gives a prime ideal omitting the nonzero difference and its corresponding ultrafilter.

The book does not isolate the Boolean prime ideal theorem as a minimal set-theoretic hypothesis in IV§3. Its proof of Theorem 3.15 uses the subdirect representation IV Corollary 1.12, p121, which invokes Birkhoff's II Theorem 8.6, pp58–59; that proof uses a maximality argument with Zorn's lemma. A manuscript that wants the sharper dependency should explicitly assume the Boolean prime ideal theorem in its proper-filter-extension form and derive the representation from it. It should not describe arbitrary ultrafilter existence as a consequence of the Boolean identities alone in ZF.

No additional simultaneous selection of witnesses is needed by the proofs below: their pointwise existential arguments and finite subcovers suffice once proper filters can be extended.

## The compactness and representation proof supported by IV4.6

Write S(B)=Ult(B) and [a]={U∈S(B):a∈U}. The complement and finite-join criteria give

\[
[0]=\varnothing,\quad [1]=S(B),\quad
[a\wedge b]=[a]\cap[b],\quad
[a\vee b]=[a]\cup[b],\quad
[\neg a]=S(B)\setminus[a].
\]

Different ultrafilters differ on some a and are separated by the disjoint clopen sets [a] and [¬a]. Thus the topology is Hausdorff with a clopen basis.

For a basic cover {[a]:a∈J}, failure of any finite subcover means that the complements ¬a have all finite meets nonzero. Their generated filter is proper; extend it to an ultrafilter U, which lies in none of the [a], a contradiction. Equivalently, the source extends the ideal generated by the a's to a maximal ideal when no finite join is 1. Refining an arbitrary cover by all basic opens contained in a member of the cover reduces general compactness to this basic-cover argument; choosing cover members for a finite subcover requires only finitely many choices.

The map η_B:a↦[a] is a homomorphism by the displayed equations and injective by ultrafilter separation. For a clopen C⊆S(B), all basic sets contained in C cover C. Since C is closed in a compact space, a finite subfamily covers it. Its finite union is [a_1∨⋯∨a_n], proving surjectivity. For C=∅ use the empty join 0. This proves the clopen inverse without asserting that every open set is represented by one algebra element.

For a Boolean space X define ε_X(x)={C∈Clop(X):x∈C}. This is a proper ultrafilter, and clopens separate distinct points because X is Hausdorff and has a clopen basis. If U is any ultrafilter on Clop(X), its members are closed and all finite intersections are nonempty. Compactness gives a point x in their intersection. Then U⊆ε_X(x), so equality follows from maximality. The point is unique by clopen separation. Finally,

\[
\varepsilon_X^{-1}([C])=C
\]

for every clopen C. This gives continuity; bijectivity plus compact-domain/Hausdorff-codomain yields a homeomorphism, or the same formula and the clopen bases prove openness directly. These are exactly the two sides of IV Theorem 4.6.

## Morphisms, contravariance, and naturality

All Boolean homomorphisms here preserve 0,1, complement, finite meets, and finite joins. For h:B→C put

\[
S(h):S(C)\to S(B),\qquad U\mapsto h^{-1}[U].
\]

Lemma 3.16 gives its codomain. For a∈B,

\[
S(h)^{-1}([a])=[h(a)],
\]

so S(h) is continuous. For a continuous f:X→Y put

\[
C(f):\operatorname{Clop}(Y)\to\operatorname{Clop}(X),
\qquad D\mapsto f^{-1}[D].
\]

Inverse images preserve complements relative to the full spaces, both constants, and finite unions/intersections, so C(f) is a Boolean homomorphism. The identities (g∘f)⁻¹=f⁻¹∘g⁻¹ and id⁻¹=id prove both contravariant functor laws.

The source's object maps are natural. For h:B→C,

\[
C(S(h))\circ\eta_B=\eta_C\circ h,
\]

because both sides send a to [h(a)]. For f:X→Y,

\[
S(C(f))\circ\varepsilon_X=\varepsilon_Y\circ f.
\]

Indeed, a clopen D⊆Y belongs to the ultrafilter on the left at x exactly when f⁻¹[D] contains x, equivalently when D contains f(x). Since all η_B are isomorphisms and all ε_X are homeomorphisms, these equations give the natural isomorphisms between each double-dual functor and the relevant identity functor. This is the categorical dual equivalence; no extra representation assumption is needed.

The optional injective/surjective conclusions in Exercises 9–10 require attention to the directions. For example, injective h gives surjective S(h) by extending the proper filter generated by the image of an ultrafilter. For injective continuous f between Boolean spaces, f identifies X with a closed subspace of Y, and each clopen subset of that subspace extends to a clopen of Y using compactness and the clopen basis; this yields surjectivity of C(f). The compact Hausdorff hypotheses matter for that latter extension statement.

## Trivial algebra and empty space

IV Definition 1.1, pp116–117, imposes Boolean equations but not 0≠1, so the one-element Boolean algebra is allowed. IV Definition 3.11, p132, explicitly says it has no ultrafilters. IV Definition 4.1 imposes no nonemptiness condition, so the empty topological space is a Boolean space.

Accordingly S(1)=∅ and Clop(∅)={∅}, the one-element algebra in which 0=1. Both reconstruction maps remain isomorphisms. Treat the empty space separately in an intersection-of-ultrafilter-members argument: its clopen algebra has no proper ultrafilter, so there is no U for which a point must be produced. In compact-cover arguments the empty cover has a finite subcover, namely itself; algebraically the empty join 0 equals 1 in the trivial algebra.

The morphisms also fit these conventions. There is a unique Boolean homomorphism from any Boolean algebra to the trivial algebra, dual to the unique map from the empty space. There is no Boolean homomorphism from the trivial algebra to a nontrivial algebra, because both constants must be preserved, matching the absence of a map from a nonempty space to the empty space. Thus no restriction to nontrivial algebras or nonempty spaces is necessary, provided the conventions are retained on both sides.
