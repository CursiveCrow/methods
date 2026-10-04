# Review of the adjunction and exponential toolkit

Date: 2026-09-06 Pacific time. Actual-file inspection began at
2026-09-07 03:46 UTC and concluded approximately 03:51 UTC.

## Result and inspected scope

**Scoped pass: no concrete mathematical defect found.** Read the actual
second half of `handbook/parts/p10/categorical-toolkit.tex`, lines
231–352, and the complete corresponding proofs in
`handbook/annex/p10/categorical-toolkit.tex`, lines 193–405. Also read
the preceding category, equivalence, cone, product, and product-arrow
definitions at body lines 6–169 and the product identities proved at
annex lines 5–44.

The six lambda/internal-language proof interfaces were cross-checked
against their actual evaluation, transposition, product, and unit/counit
formulas. This is a review of the toolkit and that compatibility; it
does not expand the assigned scope to the earlier limit-construction
or Yoneda proofs. No other review conclusions were consulted. Only
this note was written; no manuscript edits, tests, builds, or renders.

## 1. Hom-set naturality, units, counits, and recovery

`def:p10-adjunction`, body lines 231–247, has the correct types:

`Phi_(A,B):D(F(A),B) -> C(A,G(B))`,

and for `u:A'->A`, `f:F(A)->B`, `v:B->B'`,

`Phi_(A',B')(v f F(u)) = G(v) Phi_(A,B)(f) u`.

The assignments at body lines 257–258 produce
`eta_A:A->GF(A)` and `epsilon_B:FG(B)->B`.
Annex lines 197–211 derive both reconstruction formulas from the
appropriate naturality variable:

`Phi(f)=G(f) eta_A`,
`Phi^(-1)(g)=epsilon_B F(g)` for `g:A->G(B)`.

Annex lines 214–234 correctly prove both natural transformations.
The unit equation is `GF(u) eta_A=eta_(A') u` for `u:A->A'`.
The inverse-bijection naturality formula at lines 223–224 uses
`u:A'->A`, `g:A->G(B)`, and `v:B->B'`; its two applications to
identity arrows give
`v epsilon_B=epsilon_(B') FG(v)`.

The two triangle calculations at lines 236–240 are correctly indexed:
apply the inverse formula at B=F(A) to eta_A, and the forward formula
at A=G(B) to epsilon_B.

For the converse, lines 242–260 use counit naturality at
`f:F(A)->B` and the first triangle to show `Psi(Phi(f))=f`.
They use unit naturality at `g:A->G(B)` and the second triangle
to show `Phi(Psi(g))=g`. All composites have the required domains
and codomains. The calculation at lines 261–270 verifies simultaneous
naturality in both variables, not merely bijectivity of unrelated
hom-sets. Evaluating at identities recovers the original unit and
counit, and the earlier formulas recover the original bijections.

## 2. Preservation of limits and colimits

`thm:p10-adjoint-preservation`, body lines 278–289, correctly claims
preservation of existing small universal cones and cocones, rather
than existence of every limit or literal equality with independently
chosen representatives.

For a colimit in C, annex lines 281–300 transpose a cocone on F(D)
to one on D. Naturality in the first variable changes
`b_k F(D(u))=b_j` into `a_k D(u)=a_j`. Colimit uniqueness gives
the mediating map to G(B), and inverse transposition gives the
mediating map from F(L). The leg equation at line 295 and the
uniqueness argument use exactly the same first-variable naturality.

For a limit in D, lines 302–318 inverse-transpose the given cone
on G(D). Naturality in the second variable translates its cone
equations. The limiting mediating arrow transposes to the desired
arrow into G(L), and the second-variable equation at line 314
verifies every leg. Uniqueness follows by inverse transposition.

For an empty shape J, the same arguments assert that the relevant
hom-set is a singleton and transfer that assertion through the
adjunction. Thus initial objects are preserved by the left adjoint
and terminal objects by the right adjoint, without assuming a leg
exists to test. The coproduct/product, coequalizer/equalizer, and
pushout/pullback instances match the preceding shape definitions.

## 3. Exponentials and the two-variable adjunction

`def:p10-ccc`, body lines 297–325, supplies evaluation
`ev_(A,B):B^A × A -> B` and the unique transpose for arrows
`X×A->B`. Its inverse maps and beta/eta identities are oriented
consistently with both lambda sections. It distinguishes existence
of the universal constructions from the specified choices used
to interpret syntax.

Annex lines 332–339 prove parameter naturality by checking the
evaluation of `Lambda(f) s` and using uniqueness. The product
identities already proved in the toolkit make `(-)×A` a functor.
The definition

`v^A=Lambda(v ev_(A,B)):B^A -> (B')^A`

at lines 343–350 is correctly typed. Identity and composition are
verified by their untransposes at lines 352–356. Lines 358–363
then prove codomain naturality `Lambda(v f)=v^A Lambda(f)`.
Together with parameter naturality this yields exactly the
two-variable naturality required for `(-)×A` left adjoint to
`(-)^A`. Evaluation is the counit obtained from the generic
unit/counit formulas; the unit is the transpose of the appropriate
product identity.

## 4. Set and Heyting-order examples

The Set construction, annex lines 368–382, defines the transpose
pointwise from a given function and proves uniqueness by equality
of functions. For A empty, both adjunction hom-sets are singletons,
including B empty. For A nonempty and B empty, both hom-sets are
empty when X is nonempty and singleton when X is empty. The
argument therefore assumes no nonexistent map into the empty set.
All function sets are small relative to the stated universe.

The Heyting-order example, lines 384–403, uses the terminal element
1, meet as product, and the residual as exponential. Its hom-sets
are empty or singleton, and residuation says exactly when both
adjunction sides are inhabited. The evaluation inequality and
uniqueness are valid, including the one-element Heyting algebra.

## 5. Compatibility with the lambda and internal-language proofs

- `annex:p10.lambda.1` uses typed substitution and needs no extra
  categorical premise. Its proof interface supplies the tuples used
  by the later categorical arguments.
- `annex:p10.lambda.2` uses concatenation products and the curried-list
  exponential; these satisfy the current definition of a CCC.
  The syntactic category is small because its types, contexts, terms,
  and equivalence classes form sets, so local smallness is satisfied.
- `annex:p10.lambda.3:172–182` uses the exact parameter-naturality
  equation now proved in `annex:p10.cat.6`. Its beta and eta arguments
  use the current evaluation orientation `B^A×A->B`. Generic contexts
  retain their leading terminal factor.
- `annex:p10.internal.1` interprets closed arrow constants by
  transposing `a pi_2:1×A->B`. Its type comparisons use the parameterized
  eta identity. Packing terms denote identities, while packing context
  arrows denote `<!,id>`; the toolkit does not identify these two types.
- `annex:p10.internal.2` has unit `eta:Id->JE` and counit
  `epsilon:EJ->Id`, with `epsilon_A=pi_2:1×A->A`. Its two triangles
  have exactly the types of `thm:p10-adjunction-data` for F=E, G=J.
- `annex:p10.internal.3` uses the established product-arrow laws to
  construct the natural product comparison j. Its exponential
  comparison is the transpose of `E(ev_syn) j^(-1)`, whose domain is
  `P_Omega×P_Gamma`. This matches the toolkit's exponential definition;
  no strict equality between differently bracketed products is used.

No incorporation repair is required within the assigned mathematical scope.
