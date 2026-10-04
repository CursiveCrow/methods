# Independent review of the arrow-only STLC context category

Date: 2026-09-06 Pacific time. Actual-file reading began 2026-09-07
03:39 UTC and concluded approximately 03:44 UTC.

## Disposition and scope

**Scoped pass: no concrete mathematical defect found.** The review read
the complete actual files:

- `handbook/parts/p10/cartesian-lambda.tex`, lines 1–198;
- `handbook/annex/p10/cartesian-lambda.tex`, lines 1–273;
- `handbook/registry/calculi/stlc.tex`, including every registered rule;
- `handbook/parts/p07/lambda-calculi-and-type-theories.tex:24–71`, the
  variable, alpha-equivalence, and capture-avoiding substitution definitions;
- `handbook/parts/p07/normalization-and-curry-howard.tex:100–118`, the
  registered arrow-only type and term grammar.

Line references describe this inspected snapshot. The review concerns
the supplied mathematics and its compatibility with the registered
syntax; it is not an independent audit of the Pitts edition or source
locators. No other review conclusions were consulted. Only this review
note was written; no manuscript edits, tests, builds, or renders were used.

## 1. Typed equality and substitution

Body lines 14–49 define a typed congruence containing bound
alpha-renaming and the beta/eta equations. Its beta instance requires
the body in the extended context and the argument in the original
context; its eta instance requires the binder fresh for the context
and function term. Abstraction congruence changes the context in the
required direction. This is an equational metatheory of the sheet's
beta-reduction calculus, not a claim that the sheet already has an
eta-reduction rule.

The simultaneous substitution at body lines 39–48 replaces only the
free target-context variables and does not substitute into inserted
terms again. This permits source and target context names to overlap
without making substitution iterative. The inherited untyped
substitution convention is extended with binder annotations retained.

Annex lines 7–45 justify freshening, weakening, renaming, and the
lifted substitution `sigma^+=(sigma_1,...,sigma_n,z)`. The fresh z
is outside all involved finite terms and contexts, and the old
components are weakened to the new source context. This is exactly
what the abstraction typing rule requires.

Annex lines 47–86 prove identity and associativity up to bound
alpha-equivalence, substitution into equations, and replacement of
equal substitution components. In particular, the substituted beta
body `M[sigma^+][N[sigma]/x]` has the same composite substitution
as `(M[N/x])[sigma]`. The eta substitution proof preserves freshness
by choosing its binder outside the substitution components. These
arguments do not use subject reduction or strong normalization as
unproved dependencies.

## 2. Category laws, products, and exponentials

Body lines 70–92 use finite type lists as objects and equivalence
classes of term tuples as arrows. The distinction between renaming
declared free variables by position and alpha-renaming bound variables
is explicit. Substitution associativity and component congruence give
well-defined composition, identities, and associativity, as checked
in annex lines 92–102.

Annex lines 104–113 prove that the empty tuple is the unique arrow
to the empty context. Concatenation, block projections, and tuple
pairing satisfy both product equations, including an empty block.
Thus a terminal object and products are provided at context level;
the arrow-only term/type grammar is preserved.

Body lines 100–128 and annex lines 115–158 use the correct
right-associated curried-list types. Iterated application types
evaluation, and iterated abstraction types transposition. Successive
beta steps recover the original tuple; successive eta steps, from
the innermost abstraction outward, recover the original function
tuple. The fresh argument variables are absent from the parameter
context, and typing makes them absent from the free variables of
its tuple components. Bound renaming is available for any further
freshening of the finite term presentation.

The empty-source exponential is Delta itself, while an empty target
gives the empty context and singleton hom-sets on both sides of the
exponential bijection. Both empty contexts are explicitly covered.
The displayed naturality calculation follows from capture-avoiding
substitution under the fresh abstraction variables. These establish
the universal property, not merely one beta equation.

## 3. Generic CCC semantics and leading terminal factors

Body lines 133–167 fix chosen CCC structure and interpret contexts
recursively from 1. The explicit singleton value is `1 × [[alpha]]`.
The abstraction body therefore has domain `[[Gamma]] × [[alpha]]`,
matching transposition exactly; no unitor equality is silently assumed.
The interpretation of a tuple into a context has its unique leading
terminal component in addition to its stated variable components.

Annex lines 172–182 derive transposition naturality from evaluation
and uniqueness. Lines 184–195 first establish the semantic formula
for variable-selection substitutions, including weakening. This
preliminary step justifies, without circularity, the identification
of the general lifted substitution with `[[sigma]] × id` at
lines 205–210. The induction at lines 197–221 then proves the full
semantic substitution law, including substitution into closed terms.

The beta calculation at lines 223–231 has the correct maps:
`f:X×A->B`, `n:X->A`, and
`ev o <Lambda(f),n> = f o <id_X,n>`.
The right side is the substitution interpretation. The eta
calculation at lines 232–238 is the transpose uniqueness identity
for an arbitrary parameter map `m:X->B^A`; it does not assume
that the CCC is well-pointed. All equality rules preserve equality
of the resulting arrows.

## 4. Semantic equality completeness

Annex lines 243–271 choose the already constructed context category
as the separating CCC, with its explicit products and curried-list
exponentials. Each base type is interpreted by its singleton context.
Induction makes every type alpha interpret as `(alpha)`.

The generic leading-terminal convention remains valid: the terminal
object in this particular category is the empty list, and its product
is concatenation. Therefore the recursive context product is literally
the original type list, as stated at lines 254–257. This is a fact
about this model's chosen products, not an assertion that `1×A=A`
in an arbitrary CCC.

Term induction at lines 259–266 identifies the interpretation of each
term with the singleton-target arrow represented by that term.
Application is substitution into the evaluation term; abstraction
is the chosen syntactic transpose. Equality of these arrows is
precisely typed beta/eta equality by the definition of hom-sets.
Consequently equality in every CCC entails equality in this one,
which proves the converse. No normal-form or normalization theorem
is needed.

The registered base-type collection is a set. Even if it is empty,
the construction has the empty context and its unique arrow, hence
the terminal one-object CCC; the assertions about typed terms are
then vacuous. No additional nonemptiness hypothesis on the base-type
set is required for the stated category construction.
