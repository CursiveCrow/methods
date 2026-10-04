# Comparison-indexed realization of the 2017 monotonicity term model

Date: 9 September 2026. Constructive authoring contribution for
ED26-P07-monotonicity-0001. The primary author owns all manuscript files.
No manuscript, canonical record, test, build or render was changed here.

Source read: Icard, Moss and Tune, 2017 ACL paper, particularly Definitions
3.5 and 6.5, Section 7, Proposition 9.3 and Section 9.3. Local PDF:
`source/references/p07-monotonicity/icard-moss-tune-2017.pdf`, SHA-256
`ce574675aed06937f7f11bc693344de1dae87e621d001ac39c52f303f5dc0186`.
The complete layout extraction is `tmp/p07-monotonicity/source-layout.txt`.
The current body and annex were read; they are concurrently maintained by
the primary author, so this note does not freeze their changing proofs.

A later primary source corroborates the need for a repair: Moss and Icard,
*A Completeness Result for Inequational Reasoning in a Full Higher-Order
Setting*, arXiv:2202.08725v1, 17 February 2022, Section 3 on printed p. 11,
explicitly acknowledges an error in reference [7]. The bibliography on
p. 23 identifies [7] as the exact 2017 Icard–Moss–Tune paper and [6] as an
unpublished 2021 manuscript. These passages were read at
https://arxiv.org/pdf/2202.08725v1. The 2022 paper's variable-free full-model
theorem is a different target and is not used as a replacement proof here.

## Result and boundary

The canonical realization and completeness direction can be proved with the
original type-changing beta/eta conversion. Neither raw typed normal-form
uniqueness nor injectivity of a raw-normal-form encoding is required.
The necessary correction is to retain every comparison-type index on the
realization, coercion and valuation maps. The construction below proves
application coherence rather than assuming it silently.

A separate issue concerns the source's polarity converse. Under the natural
application-coherence law, its criterion in terms of raw beta/eta normal
syntax has a concrete counterexample, given in the last section. It cannot
be copied unchanged into the corrected manuscript. Section 7 gives the
separate construction and proof for a comparison-normalized, coercion-aware
occurrence criterion.

## 1. Exact syntactic setting

Keep the original marked types, their contravariant/covariant order, intrinsic
term types and full conversion relation `≈`. In particular,
`lambda x:sigma.M(x) ≈ M` is allowed when `x` is fresh for `M` and has a
type **below** the intrinsic argument type of `M`; equality of argument types
is not imposed. Keep the original universally interpreted hypotheses and
the complete monotonicity rule system.

Write `[M]` for the global original conversion class. Define

\[
 T_\tau=\{[M]:\operatorname{tp}(M)\preceq\tau\}.
\]

Membership means that at least one representative has the indicated type.
Whenever a class in `T_tau` is used, choose a representative whose intrinsic
type is below `tau`; an arbitrary representative of the global class need
not do so. For `sigma <= tau`, let `i_sigma,tau` be the literal inclusion
of these class sets.

If `[M]` is in `T_(sigma -m-> tau)` and `[O]` is in `T_sigma`, choose
legal representatives. Structural subtyping gives

\[
 M:\delta\xrightarrow n\epsilon,
 \quad\sigma\preceq\delta,\quad\epsilon\preceq\tau,
 \quad n\sqsubseteq m,
 \qquad \operatorname{tp}(O)\preceq\sigma.
\]

Thus `M(O)` is well typed and its class is in `T_tau`. This action is
well defined. If `M',O'` are other legal representatives, application
congruence yields `M(O) ≈ M'(O')`. The mixed applications needed by
congruence are well typed because both arguments lie below `sigma` and
both functions' domains lie above it.

Assume the source term-structure conditions: preorders on the `T_tau`,
monotone/antitone action at signed arrows, and

\[
 a\sqsubseteq_{\sigma\xrightarrow m\tau}b
 \quad\Longleftrightarrow\quad
 a(c)\sqsubseteq_\tau b(c)\quad\hbox{for every }c\in T_\sigma.
 \tag{TS}
\]

The inclusions preserve order. At bases, comparable types coincide. For
arrows `sigma -m-> tau <= sigma' -m'-> tau'`, restrict (TS) from
`T_sigma` to its subset `T_sigma'`; the induction hypothesis promotes
each output inequality from `tau` to `tau'`; then apply (TS) at the
target arrow. This is the complete source Lemma 7.3 induction.

## 2. Indexed realization by actual functions

Construct sets `D_tau` and bijections `iota_tau:T_tau -> D_tau` by induction
on the height of the type. At a base type take a tagged copy of `T_b` and
transport its preorder. Tags are optional, but avoid accidental identification
of unrelated base carriers.

Suppose `D_sigma`, `D_tau` and their bijections have been constructed. For
`a=[M]` in `T_(sigma -m-> tau)`, define the **actual function**

\[
 F^{\sigma,\tau}_a:D_\sigma\longrightarrow D_\tau,
 \qquad
 F^{\sigma,\tau}_a(\iota_\sigma([O]))
   =\iota_\tau([M(O)]).
 \tag{1}
\]

The inverse of `iota_sigma` and the well-defined term action show that (1)
is well defined. Crucially, the function depends on the domain and codomain
indices; it is not an unindexed realization of a conversion class.
Set

\[
 D_{\sigma\xrightarrow m\tau}
 =\{F^{\sigma,\tau}_a:a\in T_{\sigma\xrightarrow m\tau}\},
 \qquad
 \iota_{\sigma\xrightarrow m\tau}(a)=F^{\sigma,\tau}_a.
 \tag{2}
\]

### Injectivity, with the strict-subtype case included

Suppose the two functions for legal representatives `M,N` are equal. Choose
a variable `x:sigma` fresh for both. Evaluate at `iota_sigma([x])`.
Injectivity at the smaller result type yields `[M(x)]=[N(x)]`. Hence
`M(x) ≈ N(x)`. Abstraction congruence gives
`lambda x:sigma.M(x) ≈ lambda x:sigma.N(x)`, and the **original** eta
rule gives `M ≈ N`. This remains valid when `sigma` is strictly below
one or both intrinsic argument types. It establishes equality of global
conversion classes, not equality of raw normal forms with differently typed
binders. Surjectivity in (2) is by definition.

Give every arrow carrier pointwise order. By induction, its comparison of
the two values in (1) is equivalent to the output comparison in `T_tau`.
Quantifying over `D_sigma`, using surjectivity of `iota_sigma`, and applying
(TS), shows that `iota_arrow` preserves **and reflects** order. In particular,
this is an order isomorphism of preorders; quotienting mutually comparable
elements is neither needed nor intended.

The function in (1) does not depend on the mark `m`. Since the corresponding
term-class sets for `+` and `-` are subsets of the `dot` set, their images
are literal subsets of the same actual function space. Signed action in
the term structure and the lower-type order isomorphisms make the `+`
functions monotone and the `-` functions antitone.

For every comparable pair define

\[
 \pi_{\alpha,\beta}
 =\iota_\beta\,i_{\alpha,\beta}\,\iota_\alpha^{-1}.
 \tag{3}
\]

These maps preserve order, have identity components, and compose. These
facts follow from the corresponding properties of the inclusions; every
intermediate realization and inverse cancels at its own indicated type.

### Application coherence

Let `alpha=delta -n-> epsilon <= beta=sigma -m-> tau`, let
`f=iota_alpha([M])`, and let `a=iota_sigma([O])`. Both sides of the
required arrow-coercion equation are defined. On the left,

\[
 \pi_{\alpha,\beta}(f)(a)
 =\iota_\beta([M])(\iota_\sigma([O]))
 =\iota_\tau([M(O)]).
\]

On the right,

\[
 \pi_{\epsilon,\tau}
 \bigl(f(\pi_{\sigma,\delta}(a))\bigr)
 =\pi_{\epsilon,\tau}
   \bigl(\iota_\epsilon([M(O)])\bigr)
 =\iota_\tau([M(O)]).
\]

Thus the constructed prestructure satisfies the natural application
coherence law exactly, including argument restriction, result promotion
and mark forgetting. No injectivity of coercions in arbitrary external
structures is assumed. The inclusions happen to yield injective maps in
this syntactic model.

## 3. Interpretation under every assignment

Use typed substitutions that send a variable of type `sigma` to a term of
intrinsic type below `sigma`. The already required type-refinement lemma
ensures `tp(M[s]) <= tp(M)`. Conversion is stable under these substitutions:
abstract both convertible terms over their finitely many free variables,
rename the binders fresh for the substitution images, apply both abstractions
to those images using application congruence, and beta-convert. This argument
uses the original congruence and does not demand a source eta instance survive
as one syntactically identical eta instance after substitution.

Every semantic assignment `phi` can be lifted to a typed substitution `s`:
for each `x:sigma`, take a class whose `iota_sigma` image is `phi(x)` and
choose a representative `s(x)` of type at most `sigma`. Define

\[
 \llbracket M\rrbracket_\varphi
 =\iota_\tau([M[s]])\quad\hbox{where }\tau=\operatorname{tp}(M).
 \tag{4}
\]

The index is the **original declared type of M**, even when substitution
refines its intrinsic result. To see independence of the lift, suppose `t`
also lifts `phi`. Injectivity of `iota_sigma` gives `s(x) ≈ t(x)` for
every variable. For the finitely many variables free in `M`, simultaneous
capture-avoiding substitution congruence gives `M[s] ≈ M[t]`. All mixed
replacements are well typed by the type-refinement lemma. Therefore (4)
does not depend on the selected representatives.

For variables, (4) is the assigned value; for a constant `c:tau`, choose
the fixed interpretation `iota_tau([c])`.

For application, suppose `M:delta -m-> epsilon` and `N:rho <= delta`.
Using (1) and (3), its recursively computed semantic value is

\[
 \iota_{\delta\xrightarrow m\epsilon}([M[s]])
    \bigl(\pi_{\rho,\delta}(\iota_\rho([N[s]]))\bigr)
 =\iota_\epsilon([M[s](N[s])])
 =\iota_\epsilon([(M(N))[s]]),
\]

which is (4) for the application. Both substituted terms may have refined
types; membership below the displayed comparison indices is sufficient.

For abstraction `lambda x:sigma.M`, where `M:tau`, choose a fresh
`y:sigma` avoiding `M`, the finitely many relevant substitution images,
and a representative `A` of the argument value
`a=iota_sigma([A])`. At this argument, (1), capture avoidance and beta give

\[
 \llbracket\lambda x.M\rrbracket_\varphi(a)
 =\iota_\tau([ (\lambda y.M[s_x^y])(A)])
 =\iota_\tau([ M[s_x^A]])
 =\llbracket M\rrbracket_{\varphi_x^a}.
\]

The substitution `s_x^A` lifts precisely the changed assignment, and lift
independence justifies using it. The lambda term's value belongs to the
correct signed carrier by (2) and type refinement. This proves closure
under all abstractions and every interpretation clause. The structure
is not merely a prestructure with unspecified interpretation.

## 4. The canonical preorder and completeness direction

For the unchanged original rule system and fixed universally interpreted
premise set `Gamma`, define

\[
 [M]\sqsubseteq_\tau[N]
 \quad\Longleftrightarrow\quad
 \Gamma\vdash M\precsim_\tau N.
 \tag{5}
\]

Choose legal representatives at `tau`. Equiv in both directions followed
by Trans makes (5) representative independent. Ref and Trans give a
preorder.

For signed action, a representative below `sigma +-> tau` has intrinsic
type `delta +-> epsilon` with `sigma <= delta` and `epsilon <= tau`.
Promote an input comparison by Pres to `delta`, apply Mono, and promote
the output by Pres to `tau`. Anti proves the negative case.

For the forward implication of (TS), Point gives every argument comparison.
For the converse, choose a fresh variable `x:sigma`. Its argument comparison
is among the hypotheses. Func abstracts over it at the specified common
arrow type. The actual abstraction types lie below that comparison arrow
because the representatives' domain/result/mark relations were assumed.
Full original eta, Equiv and Trans give the comparison of `M,N`. This is
Proposition 9.3 with unequal intrinsic function domains explicitly retained.

Consequently (5) is a term structure, and Sections 2–3 produce a genuine
application-coherent structure `S_Gamma`.

The original calculus is closed under substitution of the conclusion while
retaining `Gamma`: from an assertion abstract over all its free variables by
Func, freshen binders, apply the resulting two terms to substitution images
by Point, then beta-convert with Equiv. Replacing this starting assertion by
its proof from `Gamma` proves the derived substitution lemma. Its validity
depends on the hypotheses being universal rather than one fixed valuation.

Take any derivable assertion `Gamma |- G <=_tau H` and any assignment `phi`
in `S_Gamma`. Lift it to `s`. The substitution lemma gives
`Gamma |- G[s] <=_tau H[s]`, hence (5) and the order isomorphism give

\[
 \iota_\tau([G[s]])\leq_\tau\iota_\tau([H[s]]).
\]

By (3) and (4), these are exactly the promoted interpretations of `G,H`
under `phi`. Thus `S_Gamma` satisfies every member of `Gamma` under every
assignment.

Finally suppose `Gamma` semantically entails `M <=_tau N` in any class
of structures containing this canonical structure. Apply the entailment
to the identity-generated assignment
`phi_0(x)=iota_(tp(x))([x])`. Its substitution lift is the identity.
Equations (3)–(4) and order reflection give

\[
 [M]\sqsubseteq_\tau[N],
 \quad\hbox{hence}\quad
 \Gamma\vdash M\precsim_\tau N.
\]

This completes the original calculus's **completeness direction** for the
intended application-coherent structures. It does not require changing eta,
discarding strict subtype arguments, restricting premises to closed terms,
or replacing the target with full function-space completeness.

## 5. A route to conversion soundness without a new model axiom

Adding a global conversion-coherence axiom to the model class would make
Equiv sound by definition, but would leave a source-model-class change to
justify. There is a more informative route using comparison-type eta-long
normal forms. The following is a constructive lemma to incorporate after
binding the ordinary simply typed beta/eta long-normalization theorem already
needed by P7. It does not use raw marked beta/eta confluence.

Erase all markings recursively, leaving the base types and arrow tree.
Comparable marked types have identical erasures. Marked beta/eta conversion
therefore erases to ordinary simply typed beta/eta conversion.

For a marked context, a term `M` of intrinsic type below `tau`, and the
expected comparison type `tau`, form an eta-long representative `L_tau(M)`:

1. Beta-normalize with typed, capture-avoiding substitution.
2. At expected arrow type `sigma -m-> rho`, introduce a fresh binder
   `x:sigma`, form `M(x)`, and normalize that body at `rho`. If the
   beta-normal head was already an abstraction, substitute the fresh variable
   in its body. This uses the permitted subtype argument and retains the
   binder at the comparison type.
3. At a base type, the beta-normal term is a variable/constant head applied
   to a finite spine. Normalize each argument at the intrinsic argument type
   specified by that head's typed spine.

This is the ordinary eta-long normalization algorithm with uniquely
determined marked binder/argument annotations. Its termination follows by
the same recursive calls as the ordinary typed algorithm. No arbitrary
alternation of eta expansion and contraction is performed.

### Why the reconstructed term has the required type

Beta steps refine types. In the arrow case, if the original function has
type `delta -n-> epsilon <= sigma -m-> rho`, then `sigma <= delta`,
`epsilon <= rho` and `n <= m`. The fresh application is legal. Before
normalizing its body, the fresh binder occurs with sign `n` if `n` is signed.

The required strengthened occurrence observation is: a signed free occurrence
survives beta reduction and comparison-directed eta expansion, with the same
sign, possibly in several copies; unsigned occurrences may refine. For a beta
redex, an occurrence in the abstraction body outside its binder survives
capture-avoiding substitution. An occurrence in the argument with signed
total polarity has passed through a signed abstraction. That abstraction
has at least one free occurrence of its binder, all with its indicated sign,
so substitution produces at least one copy with the same product sign.
The surrounding context preserves that sign because a refinement of a signed
mark must be that same sign. Eta expansion keeps all previous free occurrences
in its function part and introduces only a fresh bound variable. The same
argument applies recursively in neutral-head arguments. In particular, a
nonvacuous signed binder cannot become vacuous in this normalization.

Thus the reconstructed arrow's intrinsic mark is below `m`, and its result
type is below `rho`. At a base head, every argument still lies below the
corresponding declared domain, so the whole application is well typed. This
proves type validity and the needed sign-refinement invariant together by
induction over the eta-long normalization construction.

### Why meaning is preserved at the comparison type

Beta normalization preserves promoted interpretation by the substitution
lemma and composition of coercions. For the fresh arrow abstraction,
application coherence gives, for every `a` in `D_sigma`,

\[
 (\pi_{\operatorname{tp}(M),\tau}\llbracket M\rrbracket)(a)
 =\pi_{\epsilon,\rho}
   (\llbracket M\rrbracket(\pi_{\sigma,\delta}(a))).
\]

The right-hand side is the promoted interpretation of `M(x)` when `x=a`.
The inductive hypothesis for the body therefore identifies it with the
normalized body's value. Actual function extensionality proves preservation
for the abstraction. At a neutral head, the inductive hypotheses say that
each normalized argument has the same value after promotion to that head's
declared domain; repeated application then preserves the result.

### Why the result is unique at this fixed comparison type

The erased eta-long normal form is unique up to ordinary alpha conversion.
Its marked decoration is uniquely determined by the comparison type and the
fixed typed free-variable/constant context: at a lambda, the binder takes the
expected arrow's domain type; at a neutral head, every argument takes the
domain type in that head's declared spine. The abstraction marking itself
is recomputed from the decorated body by the original occurrence rule.
Induction over this long normal form gives uniqueness of that decoration.

Consequently if `M ≈ N` and both intrinsic types are below `tau`, their
comparison-directed long forms are the same typed term up to typed alpha
conversion. Meaning preservation yields equal promoted interpretations at
`tau` in every application-coherent structure. This proves Equiv soundness
without asserting uniqueness of raw typed short normal forms or adding a
new conversion-coherence axiom. The primary author must check and bind this
eta-long normalization lemma as part of the proof, rather than cite the
false raw-normal-form uniqueness claim.

## 6. Exact counterexample to the raw-normal polarity converse

Let `b` be a base type, put

\[
 \rho=(b\xrightarrow+ b),\qquad
 \sigma=(b\xrightarrow\cdot b),\qquad \rho\prec\sigma,
\]

and take a free variable `c:b` and a constant or fixed-assignment variable

\[
 F:(\rho\xrightarrow+ b)\xrightarrow+ b.
\]

Consider

\[
 M=F(\lambda f:\sigma.\ f(c)).
 \tag{6}
\]

The inner abstraction has intrinsic type `sigma +-> b`: its bound `f`
occurs positively as the function in `f(c)`. Contravariance yields
`sigma +-> b <= rho +-> b`, so (6) is well typed and has intrinsic type `b`.
There is no beta redex. The lambda body is `f(c)`, not an expression of the
form `Q(f)` with `f` absent from `Q`, so there is no eta redex either.
Thus it is a raw normal term under the source definition.

The occurrence of `c` inside `f(c)` is unsigned because `f:sigma` has a
dot arrow. The outer F is monotone, but `+` composed with `dot` is `dot`.
Therefore the sole free occurrence of `c` in M is **not positive**.

Nevertheless its interpretation is monotone in c in every coherent structure.
For `a` in `D_b`, the abstraction denotes the evaluator `f |-> f(a)` on
`D_sigma`. Its coercion to `D_(rho +-> b)` restricts this evaluator to
`g` in `D_rho`, by application coherence and the mark-forgetting inclusion.
Every such `g` is monotone. If `a <= a'`, then `g(a) <= g(a')` for every
`g` in `D_rho`. Pointwise order therefore makes the restricted evaluator
at `a` below the one at `a'`. Finally, monotonicity of F yields
`[[M]]_(c=a) <= [[M]]_(c=a')`.

The monotonicity hypothesis of the original raw-normal converse is satisfied,
while its syntactic conclusion fails. This is not a test result or a numerical
approximation; it is a uniform proof over the intended coherent model class.

The example is nonvacuous. In the full hierarchy over the two-element chain,
let F evaluate its argument at the identity function `id_b`, which belongs
to `D_rho`. Evaluation at a fixed argument is monotone for pointwise order,
so F has the required type, and the denotation of M is simply c.
For the negative counterpart, replace rho by `b -→ b` and let F evaluate at
the order-reversing Boolean negation. The same raw occurrence is unsigned,
but the uniform argument gives antitonicity and the concrete value is the
negation of c.

Comparison-directed normalization repairs the *description* of this example:
the argument received at type `rho +-> b` becomes
`lambda g:rho.g(c)`, where c is positive. Section 7 proves the general
converse for these elaborated occurrences by constructing a compatible
indexed occurrence preorder, proving its signed action and extensionality,
and realizing a structure that separates a nonpositive elaborated occurrence.
This is the separate Lyndon-style theorem; it does not restore the original
raw criterion under application coherence.

## 7. Completed construction for the elaborated polarity converse

This section supplies the occurrence-preorder construction and converse for
the **comparison-directed eta-long** representative. The counterexample to
the original raw criterion is unchanged.

Assume the comparison-normalization lemma from Section 5 has been established
in the manuscript. Write `L_tau(M)` for its unique eta-long representative
at expected type `tau`, modulo typed alpha conversion. The ordinary
simply typed beta/eta long-normalization theorem is the explicit external
normalization input. The other required inputs are the original typed
substitution/type-refinement facts and the signed-residual argument stated
and proved below. No restriction on the original eta rule is introduced.

### 7.1 Statement of the corrected theorem

Let `M` have intrinsic type at most `tau`, and let `x:sigma0` be a variable.
For an assignment `phi`, define the value to be compared by

\[
 V_{M,\tau,\varphi}(a)
  =\pi_{\operatorname{tp}(M),\tau}
      (\llbracket M\rrbracket_{\varphi_x^a}),
 \qquad a\in D_{\sigma_0}.
 \tag{7}
\]

Then the following are equivalent:

- Every free occurrence of `x` in `L_tau(M)` is positive.
- In every application-coherent structure and for every assignment, (7) is
  monotone.

Replacing positive/monotone by negative/antitone gives the parallel theorem.
An absent variable satisfies either occurrence condition, and (7) is then
constant. The quantification is over the general structures realized in
Sections 2–3, not only full function hierarchies.

### 7.2 Typed colored trees

Fix three distinct variables `x,y,z` of the same type `sigma0`. Work modulo
typed alpha conversion, and always rename bound variables away from this
triple. For complete precision one may use de Bruijn indices for bound
occurrences while retaining names and assigned types for free variables.
This avoids making positions depend on a choice of fresh bound names.

For a typed term `P`, let `erase_color(P)` replace its **free** occurrences
of `y,z` by `x`. All other variable names, constants, binders, binder types,
application nodes and abstraction nodes remain. This is a capture-avoiding
same-type renaming. Consequently it preserves the intrinsic type and the
polarity of every corresponding position. In particular, it does not change
any binder's inferred marking: the free distinguished variables have the
same declared type and none is that binder.

Suppose `P,Q` have the same color-erased typed tree `S`. Every free `x`
position of `S` carries, in `P` and `Q`, a color in `{x,y,z}`. At a position
whose polarity in `S` is positive, order the colors by equality and `y < z`;
at a negative position use equality and `z < y`; at an unsigned position
use equality alone. The color `x` is comparable only with itself at every
position. Define `P <=color Q` when the corresponding colors are ordered
at every position. No change is permitted at a non-distinguished position.

For each comparison type define

\[
 [P]\sqsubseteq_\tau[Q]
 \quad\Longleftrightarrow\quad
 L_\tau(P)\leq_{\rm color}L_\tau(Q),
 \tag{8}
\]

using representatives with intrinsic types at most `tau`. The unique
comparison-normal form makes this independent of those representatives.

Reflexivity is pointwise color equality. For transitivity, if `P` and `Q`
have color-erased tree `S` and `Q` and `R` have color-erased tree `S'`,
then `S=S'` modulo the fixed typed alpha convention. The relevant color
order at each position is transitive, so the pair `P,R` satisfies it.
Thus (8) is a preorder on every `T_tau`.

### 7.3 Residual and substitution lemmas

The following facts concern typed syntax, not semantic monotonicity. This
distinction prevents a circular use of the theorem being proved.

**Normalization preserves the color order.** If well-typed `P,Q` have
types at most `tau` and `P <=color Q`, then
`L_tau(P) <=color L_tau(Q)`.

To prove this, follow the same deterministic comparison-normalization calls
on the two terms. Their color-erased typed trees agree. Renaming among the
three same-type free variables does not change whether a node is a beta
redex, its binder, the positions occupied by that binder, the intrinsic types
on its spine, or the choice of expected types in eta expansion. Therefore
beta contraction and expected-type eta expansion occur at matching nodes,
and their color-erased outputs still agree. The residuals of each changed
color position match in the two outputs.

A changed position was signed: a positive change was `y` to `z`, and a
negative change was `z` to `y`. For a beta contraction, a free occurrence
in the abstraction body outside its binder remains under capture-avoiding
substitution. An occurrence in the argument is copied into the binder's
free positions in the body. If that original occurrence had signed total
polarity, the abstraction's marking was signed, so its binder occurred at
least once and uniformly with that sign. Each residual then has the same
product sign. A refined type cannot change one sign into the other sign
or into an unsigned mark: both signs are minimal in the marking order.
In a surrounding context the same product argument preserves a previously
signed total polarity. Positions which disappear need impose no condition;
they create no new color change. Eta expansion retains every previous free
occurrence in its function part and adds only fresh bound occurrences.
When a fresh binder has a strict subtype, the resulting substitution is
exactly the type-refining case of the same residual argument. Thus all
surviving changed positions retain their permitted directions. Induction
over the normalizing calls proves the claim.

**A common substitution preserves color order.** Let `u` be distinct from
`x,y,z`. If `P <=color Q`, and the same well-typed term `A` is substituted
for `u` in both, then the resulting terms, and therefore their common-type
normalizations, remain color ordered.

Indeed, their free `u` positions agree, as do the types and polarities of
those positions. Every inserted copy of `A` is identical on the two sides;
colors introduced by it are therefore equal. An old changed distinguished
occurrence is not a substituted `u` and survives with its signed direction
under type refinement. The two substitutions have the same typed erased
shape. Alpha-renaming prevents a distinguished free variable in `A` from
being captured. Normalization preservation then applies. There is no
requirement that `A` itself omit `x,y,z`.

**A signed variable reverses or preserves a varying substitution.** Let `B`
be one term, let `u` be distinct from `x,y,z`, and suppose every free
occurrence of `u` in `B` has sign `epsilon`, where `epsilon` is `+` or `-`.
Let `N <=color O`, with both substituends legal at the type of `u`.
For `epsilon=+`,

\[
 B[N/u]\leq_{\rm color}B[O/u];
\]

for `epsilon=-`,

\[
 B[O/u]\leq_{\rm color}B[N/u].
\]

Both conclusions remain true after normalization at any common legal
comparison type. To see this, the substituends have the same typed
color-erased tree and therefore the same intrinsic type. The resulting
substitutions in `B` also have the same typed color-erased tree. Existing
distinguished occurrences in `B` have equal colors on both sides. A changed
position inside a substituend of sign `delta` appears at each substituted
`u` position with sign `epsilon * delta`, by the signed instance of the
type-refining substitution lemma. Multiplication by `+` preserves its
permitted direction. Multiplication by `-` reverses it, exactly compensated
by comparing `B[O/u]` with `B[N/u]`. This accounts for every possibly changed
position. Normalization preservation gives the final assertion.

These proofs use only shape agreement, original occurrence multiplication,
and the corrected bound for type-refining substitution. They do not assume
that all unsigned positions preserve their original marking.

### 7.4 Signed action

Let `[M]` belong to `T_(sigma +-> tau)` and let
`[N] <=_sigma [O]`. Take comparison-normal representatives

\[
 L_{\sigma\xrightarrow+\tau}(M)=\lambda u:\sigma.B,
 \quad L_\sigma(N)=N',\quad L_\sigma(O)=O'.
\]

Choose the bound `u` fresh for the distinguished variables and both
substituends. Type validity says that the intrinsic type of this long
abstraction is below `sigma +-> tau`. Its intrinsic marking must therefore
be `+`, so its body has a nonempty collection of free `u` occurrences and
all are positive. Definition (8) gives `N' <=color O'`. The positive
varying-substitution lemma gives the color comparison of `B[N'/u]` and
`B[O'/u]` after normalization at `tau`.

The original global conversion relates `M` to its displayed long abstraction
and `N,O` to `N',O'`. Application congruence and beta conversion identify the
two normalized outputs with `L_tau(M(N))` and `L_tau(M(O))`. All displayed
applications are well typed at the comparison domain `sigma`. Hence
`[M(N)] <=_tau [M(O)]`, as required by the term-structure positive-action
condition. The negative-action condition is the same argument with
`L_(sigma --> tau)(M)`; the variable `u` is then uniformly negative and
the varying-substitution comparison reverses.

This proof did not first assume order preservation of type inclusions.
The comparison-normal function has exactly the binder domain `sigma`, so
the input order is used at the type where it was given.

### 7.5 Extensionality of the occurrence preorder

Let `[M],[N]` be in `T_(sigma -m-> tau)`. Choose their long representatives
with the same fresh binder `u:sigma`, writing them as `lambda u.B` and
`lambda u.C`. By the definition of the long form, `B` and `C` are the
comparison-normal forms at `tau` of `M(u)` and `N(u)`.

If `[M] <=_(sigma -m-> tau) [N]`, adding or deleting this common outer
lambda does not change the polarity of a distinguished **free** occurrence.
Thus `B <=color C`. For any class `[O]` in `T_sigma`, take a legal
representative and normalize it at `sigma`. Apply the common-substitution
lemma to replace `u` by this same term in both bodies. Conversion and beta
identify the resulting normalized pair with `M(O),N(O)` at `tau`.
Therefore the pointwise comparison holds for every argument class.

Conversely, suppose the pointwise comparison holds for every argument class.
It holds in particular for a variable `u:sigma` fresh for `M,N,x,y,z`.
It says exactly that `L_tau(M(u)) <=color L_tau(N(u))`. Adding the same
outer binder preserves that relation and yields the comparison of
`L_(sigma -m-> tau)(M)` and `L_(sigma -m-> tau)(N)`. This is the required
arrow comparison. No comparison of raw short normal forms occurs.

We have proved (TS), both signed-action conditions and the preorder laws.
Thus (8) defines a term structure for the **full original type system**.
The already proved term-inclusion lemma now gives order preservation of
its inclusions, and Sections 2–3 realize it as an actual coherent structure
with the complete indexed interpretation.

### 7.6 Separation and the converse

First, `[y] <=_(sigma0) [z]` in this term structure. For a base type their
long forms are simply the two variables. At an arrow type, eta-long expansion
adds fresh binders and arguments; the distinguished free head variable remains
positive. Iterating this observation along the type proves that replacing
that free head `y` by `z` is permitted at all its occurrences.

Suppose (7) is monotone in every coherent structure. Choose the occurrence
term structure just constructed, its realization from Section 2, and the
identity-generated assignment on all other variables. Vary `x` between
`iota_sigma0([y])` and `iota_sigma0([z])`, which are ordered by the preceding
paragraph. The interpretation formula (4), followed by promotion to `tau`,
and the monotonicity hypothesis give

\[
 \iota_\tau([M[y/x]])\leq_\tau\iota_\tau([M[z/x]]).
\]

Order reflection gives `[M[y/x]] <=_tau [M[z/x]]`.
Choose `y,z` fresh for `M`. Same-type free-variable renaming commutes with
comparison-directed long normalization: the algorithm's types, redexes,
expected-type choices and binding structure are unchanged, and bound names
are freshened uniformly. Therefore this last comparison is

\[
 L_\tau(M)[y/x]\leq_{\rm color}L_\tau(M)[z/x].
 \tag{9}
\]

After color erasure the common skeleton is `L_tau(M)`. At **each** free
`x` position of this skeleton, (9) changes the color from `y` to `z`.
The color order permits that distinct change only at a positive position.
Thus every such occurrence is positive. If there are no such positions,
the conclusion is vacuous, as required.

For an antitone hypothesis, the same ordered pair of argument values gives
the reversed output comparison. At every free `x` position it changes `z`
to `y`, which the color order permits only at a negative position. This
proves the negative converse.

For the forward directions, comparison normalization preserves the promoted
denotation of `M` at `tau`. Apply the ordinary occurrence-polarity lemma to
`L_tau(M)`. If its intrinsic result type is strictly below `tau`, compose
the resulting monotone or antitone map with the order-preserving output
coercion. Its value is exactly (7). This proves both forward directions
and completes the corrected equivalences.

### 7.7 What was corrected, and what was preserved

The theorem is about the occurrences in a fully elaborated eta-long term
at the specified comparison type and at each head's receiving argument
types. It is **not** the disproved raw-short-normal-form theorem. Its model
class includes natural application coherence, which the corrected manuscript
states explicitly. The proof system, source type order, strict-subtype
applications and original type-changing eta are preserved throughout.

Every normalization input has been named: ordinary STLC long normalization,
typed substitution/refinement, and the signed-residual proof. The occurrence
model does not assume the desired converse or treat a color comparison as a
universally asserted hypothesis. It is one constructed structure in which
`[y] <= [z]` holds under the chosen identity-generated assignment, and
semantic monotonicity is tested there. This avoids replacing the source's
all-assignments semantics by local premises or by a different calculus.
