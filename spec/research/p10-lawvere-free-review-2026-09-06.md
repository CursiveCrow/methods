# Free Lawvere algebras: independent actual-text review

Date: 2026-09-06, local date.

## Outcome and scope

**Scoped mathematical pass after read-back of the universe and incorporation repairs.** No remaining necessary mathematical correction was found.

Read in full:

- handbook/parts/p10/lawvere-free-algebras.tex;
- handbook/annex/p10/lawvere-free-algebras.tex.

Also read the live Lawvere core/model body and annex, the relevant named-presentation recovery interface, and the Yoneda proof used by the finite representables. No other review conclusions were read. This note is the only file written by this reviewer. No manuscript edits, tests, builds, or renders were performed.

Final anchors below refer to the actual corrected text read at approximately 04:17 UTC on 7 September 2026. Source-attribution verification, host integration, and typeset quality are outside this mathematical review.

## Repairs reported and verified

The original arbitrary-set wording needed alignment with the toolkit's fixed-universe category of sets. The new paragraph at handbook/parts/p10/lawvere-theories.tex:6–10 now places signatures, equations, algebra carriers, and generators in that universe, and explicitly treats larger instances in a suitably larger universe. The opening of lawvere-free-algebras.tex:6–7 invokes that convention. Thus the terms and quotient of an allowed generator set are again small sets, and the resulting evaluation model has the stated codomain.

The live annex at lines 237–238 now uses the core symbol \(T_{\Sigma,E}\), and correctly describes an arrow \(0\to1\) as a singleton tuple of a ground-term class. The body gives the corresponding canonical-bijection wording at lines 149–151. The live annex at lines 242–243 now uses absence of nullaries, rather than an empty-signature argument, for arbitrary positive-arity signatures. These incorporation issues are resolved.

## 1. Finite representables and opposite variance

Body lines 14–22 and theorem lines 24–55; annex lines 7–74.

For \(R_n=\mathbb T(n,-)\), postcomposition is covariant in the theory argument. The product universal property gives the comparison
\[
\mathbb T(n,k)\longrightarrow\mathbb T(n,1)^k,\qquad
a\longmapsto(p_i^k a)_{i<k}.
\]
It is bijective, including the terminal object \(k=0\), and establishes that \(R_n\) is a finite-product-preserving model.

Yoneda is applied to \(\mathbb T^{\mathrm{op}}\), so its presheaves are the covariant functors on \(\mathbb T\). The inverse transformation
\[
\alpha^z_k(a)=M(a)(z)
\]
has the required types, and naturality follows from \(M(ta)=M(t)M(a)\). The forward map evaluates at \(1_n\). Naturality at \(p_i^n\) makes the composite with \(c_n^M\) exactly restriction to the generator map \(i\mapsto p_i^n\).

The proof includes all natural transformations, not only isomorphisms: annex lines 44–50 use
\[
c_n^N b_n=(b_1)^n c_n^M
\]
for arbitrary \(b:M\Rightarrow N\). At \(n=0\), the parameter set \(M(0)\) is a singleton, so \(R_0\) is initial.

For an arrow \(f:m\to n\), precomposition gives \(R_n\to R_m\); hence the fully faithful functor has source \(\mathbb T^{\mathrm{op}}\), and
\[
\operatorname{Nat}(R_n,R_m)\cong\mathbb T(m,n).
\]
The indexed-object formulation \((n,R_n)\) makes the claimed category isomorphism precise even if different chosen representables are isomorphic. Comparison with a free model on a finite set fixes one bijection \(n\to X\); its universal property then gives the unique generator-preserving isomorphism. No simultaneous choice of free bases is made, and generator injectivity is never assumed.

## 2. Arbitrary generators and the semantic quotient

Body lines 76–99; annex lines 80–147.

Tagged variables keep the generator set disjoint from the signature. The semantic relation \(\theta_X\) is a relation on the fixed term-set square, definable by quantified evaluation conditions. It does not require a product of all models. Every evaluation kernel is an equivalence relation and operation congruence, so the common condition is a congruence and defines quotient operations.

The argument proving \(Q_X\models E\), annex lines 97–117, is sound. For one equation in one finite declared context \(Y\), an assignment into the nonempty quotient has finitely many values; choose representative terms only for these values. The term recursion identifies the two quotient evaluations with \([sr]\) and \([tr]\). Every existing assignment \(v:X\to A\) into an \(E\)-model makes these substituted terms equal by the original equation, so they are \(\theta_X\)-equivalent. Empty \(Y\) is explicitly covered by the empty substitution.

This proof does not select representatives for all quotient elements or all generators. Finite choices suffice and require no global choice principle. It also does not assume that a map from \(X\) to every target carrier exists; the semantic condition quantifies only over assignments that do exist.

The separate empty case, annex lines 119–126, is correct. An empty quotient implies an empty term set, since every term would otherwise have a class. Thus \(X\) is empty and the signature has no nullaries. Every well-formed term then contains a variable, so every well-formed equation has a nonempty declared context and has no valuation in the empty carrier. The empty quotient satisfies all equations.

The extension \(\bar v([t])=t^A(v)\) is independent of representatives by the definition of \(\theta_X\), preserves all operations by term recursion, and is unique by induction on terms. This includes nullaries and the entirely empty term set.

For \(u:X\to Y\), the unique map extending \(x\mapsto[u(x)]\) defines \(Q(u)\). Its formula \([t]\mapsto[t[u]]\) is justified by evaluation in the already established algebra \(Q_Y\). Uniqueness proves identity and composition laws, without a section of either quotient map.

## 3. Transport to the theory and the full adjunction

Body lines 101–127; annex lines 149–205.

The named-presentation isomorphism \(\rho\) fixes objects and selected projections. Therefore
\[
\mathcal F_{\mathbb T}(X)=M_{Q_X}\rho^{-1}
\]
has actual value \(Q_X^n\) at \(n\), and pulling a target model back along \(\rho\) retains the same comparison maps \(c_n^M\).

For \(v:X\to M(1)\), the proposed components
\[
\alpha_n=(c_n^M)^{-1}(\bar v)^n:Q_X^n\to M(n)
\]
are the evaluation transformation of the algebra homomorphism \(\bar v\), followed by the inverse comparison isomorphism on the model. Their naturality follows from the fully proved core model/algebra correspondence.

The reverse construction \(q\mapsto\alpha_1((q))\) is essential and correct: the source model's underlying carrier is \(Q_X^1\), not literally \(Q_X\). The core algebra isomorphism \(q\mapsto(q)\) makes this an algebra homomorphism. Independently, naturality at the projections gives
\[
c_n^M\alpha_n=
\bigl((q_i)_{i<n}\mapsto(\alpha_1((q_i)))_{i<n}\bigr),
\]
which verifies the inverse component formula directly. At \(n=1\), \(c_1^M(a)=(a)\), so the generator map is exactly \(x\mapsto([x])\), and restriction yields \(v(x)\). At \(n=0\), both component domain and codomain are singletons, irrespective of whether \(M(1)\) is empty.

The maps on generator-set functions have components \(Q(u)^n\). The equation
\[
U\mathcal F(u)\eta_X=\eta_Yu
\]
proves naturality of the generator family. Restriction to generators commutes with precomposition in \(X\) and postcomposition by every model transformation in \(M\), establishing the full two-variable adjunction bijection.

The counit is the extension of the identity assignment on \(M(1)\). Its generator equation proves the first triangle. For the second, combine naturality of \(\eta\) at \(\eta_X\) with that first triangle at \(M=\mathcal F(X)\): the composite \(\varepsilon_{\mathcal F(X)}\mathcal F(\eta_X)\) agrees with the identity on every generator. Freeness then proves equality. No triangle identity is assumed in obtaining the bijection.

The comparison \(\mathcal F_{\mathbb T}(n)\cong R_n\) follows from their common free universal property, including \(n=0\).

## 4. The exact empty-carrier criterion

Body lines 139–163; annex lines 211–251.

Product preservation forces \(M(0)\) to be a singleton. An arrow \(0\to1\) therefore excludes an empty carrier.

Conversely, if \(\mathbb T(0,1)\) is empty, there can be no arrow \(0\to n\) for \(n>0\), since a target projection would produce \(0\to1\). Assigning a singleton to \(0\) and the empty set to every positive object consequently provides every required arrow map uniquely. Identities and compositions follow by uniqueness.

For a finite product of objects \(n_j\), the selected product is their sum. If one is positive, both the comparison's source and target are empty; if all are zero, both are singletons. This includes the empty product and proves preservation. Every other empty-carrier model has exactly these empty/singleton values up to their unique component bijections, which are automatically natural.

The ground-term discussion now respects the term theory's singleton-tuple convention. Nullaries produce ground terms; in their absence no ground term exists, and quotienting cannot create one. Positive-arity operations on the empty set exist uniquely, and all well-formed equations are satisfied there.

The representable initial model has carrier \(\mathbb T(0,1)\). Nonempty generator sets supply terms and thus nonempty quotients and free-model carriers, regardless of any identifications of generators. Their free property restricts to nonempty target models. At zero generators, the all-carrier initial model may be excluded, and the text correctly leaves open whether the nonempty subcategory has another initial object.

## 5. Nonempty-category examples

Body lines 165–178; annex lines 253–280.

Every proposed initial nonempty set has two distinct constant maps into a two-element set. For semigroups the left-zero multiplication \(ab=a\) is associative, each element is idempotent, and both constant maps from a nonempty semigroup preserve multiplication. These give the claimed failures of initiality.

For the unary equation \(d(x)=d(y)\), a nonempty model has a uniquely determined value \(a_*\) of \(d\), and \(d(a_*)=a_*\). Sending the singleton algebra's element to \(a_*\) is a homomorphism; preservation of \(d\) forces this value for every homomorphism. Hence the singleton algebra is initial in the nonempty subcategory, without a nullary term. The empty algebra remains initial in the all-carrier category. The two initiality assertions refer to different categories and are compatible.
