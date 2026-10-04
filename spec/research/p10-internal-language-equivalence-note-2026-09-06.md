# An exact internal language for a small cartesian closed category

Independent proof plan, 2026-09-06 Pacific time; no manuscript edits.

## Source and exact claim

Read the held Andrew M. Pitts, *Categorical Logic*, 18 May 1995 draft,
`tmp/acquisition/src030/cambridge-categorical-logic-author.pdf`, through
the accompanying author-layout extraction. Relevant passages are Section
2.3, pp. 10–11 (named objects/arrows and equations for identity,
composition, terminal objects, and products); Sections 3.2–3.3, pp. 19–24
(unit/product and exponential beta/eta laws); Section 4.2, pp. 30–35
(context category and evaluation); Section 4.3, pp. 35–36 (the full
semantic diagram and category equivalence); and Section 4.4, pp. 37–38
(type structure in the classifying category). Use `Pitts1995Draft`.

Pitts Section 4.3 explicitly takes as axioms ALL equations-in-context
true in the canonical named structure, then derives full faithfulness
and essential surjectivity. This is an exact, source-supported strategy.
It does not assert that pure beta/eta conversion, or merely adding names
for arrows, presents every CCC. No effective axiomatization is claimed.

## Size and chosen structure

Fix a small category C, meaning its objects and arrows form sets in the
chosen universe. Give it a specified terminal object 1, specified binary
products, and specified exponentials B^A with evaluation
`ev_(A,B):B^A × A -> B`. These choices are data; no simultaneous choice
of representatives or of CCC structure is hidden in the construction.
For a merely existentially specified CCC, choosing such structure is an
additional preliminary step under the ambient choice convention.

Use selected finite products P_Gamma for finite object lists: P_empty=1,
P_(A)=A, and a fixed bracketing for longer lists, with their canonical
projections. The singleton convention makes evaluation onto objects
literal rather than merely essentially onto. A large locally small C
does not in general yield a set-sized language; either enlarge the
universe or state a different size policy.

## An arrow-only language compatible with the context-category route

Take one base type `[A]` for every object A of C. Form types using only
the function-type constructor S→T, in addition to these base types.
Contexts are finite lists of typed variables; arrows between contexts
are tuples of terms, modulo typed equations. Interpret

`|[A]|=A`, `|S→T|=|T|^(|S|)`, and `|Gamma|=P_(|T_1|,...,|T_m|)`.

Use ordinary simply typed abstraction/application, alpha-conversion,
beta and eta equality, and the usual typed equality/substitution rules.
Include these closed constants:

1. `c_f:[A]→[B]` for every actual arrow f:A→B. Interpret c_f by the
   transpose of `f o pi_2:1×A->B`, so `x:[A] |- c_f x:[B]` denotes f.
2. `u:[1]`, denoting `id_1:1->1`.
3. `pair_(A,B):[A]→[B]→[A×B]`, denoting the curried pairing map.
4. `E_(A,B):[B^A]→([A]→[B])` and
   `L_(A,B):([A]→[B])→[B^A]`, both denoting the identity of B^A
   in their displayed unary-arrow interpretations.

The final three families are explicit structural constants. They can
also be viewed as differently typed presentations of the identity arrows
on the chosen unit, products, and exponentials. They are necessary here
because base `[B^A]` is not syntactically the arrow type `[A]→[B]`, and
there are no primitive product or unit type constructors. The family is
still a set. Pitts's alternative many-sorted signature names an arrow
from a finite product both by an n-ary and a unary symbol; these added
structural constants perform the same context-packing role.

## The equational theory must be stated explicitly

Define Th_C to consist of all well-typed equations-in-context
`Gamma |- s=t:T` whose interpretations are equal arrows
`|Gamma| -> |T|` in C. This is a set of axioms, since the syntax is a set.
Use the least typed equational theory containing these axioms and the
STLC beta/eta laws. Its soundness follows because semantic equality is
preserved by congruence, abstraction, and simultaneous substitution; the
substitution lemma identifies the last operation with composition.
Conversely, every semantically equal parallel term pair is an axiom.

In particular, the diagram contains these explicit structural equations:

`c_id x=x`, `c_g(c_f x)=c_(g o f) x`, and `c_!A x=u`;

`c_pi1(pair x y)=x`, `c_pi2(pair x y)=y`,
`pair(c_pi1 z)(c_pi2 z)=z`;

`E(L h)=h`, `L(E z)=z`;

`E_(A,B) z a = c_ev(pair_(B^A,A) z a)`;

for each f:D×A->B and its categorical transpose lambda(f):D->B^A,

`E_(A,B)(c_(lambda(f)) d) a = c_f(pair_(D,A) d a)`.

Terminal uniqueness is `z:[1] |- z=u`. The source's identity,
composition, terminal, and product criteria are Proposition 2.3.1;
function beta/eta correspond to the exponential identities in Section
3.3. Do not claim that the displayed subfamily alone generates the whole
diagram unless a separate normalization theorem is supplied. The proof
below deliberately uses the stated full semantic diagram.

## Comparison of compound types with named objects

Define terms `k_T:T→[|T|]` and `l_T:[|T|]→T` recursively.
For T=[A], both are identity terms. If |S|=A and |T|=B, put

`k_(S→T)(h)=L_(A,B)(lambda a:[A]. k_T(h(l_S(a))))`,

`l_(S→T)(z)=lambda s:S. l_T((E_(A,B)(z))(k_S(s)))`.

Induction shows that both denote `id_(|T|)` at their respective types.
Their two inverse equations therefore belong to Th_C. They can also be
derived directly from the E/L inverse equations and beta/eta. These
comparisons prevent any implicit identification of a formal type with
its named semantic object.

## Comparison of contexts with named products

For `Gamma=(x_1:T_1,...,x_m:T_m)`, define

`pack_Gamma:Gamma -> [|Gamma|]`.

For the empty context it is u. For a singleton it is `k_(T_1)(x_1)`.
For a longer context, combine the preceding packer and `k_(T_m)(x_m)`
using the selected curried pair constant with the fixed product bracketing.
Its interpretation is `id_(|Gamma|)`.

Define `unpack_Gamma:[|Gamma|] -> Gamma` by the tuple

`(l_(T_i)(c_(pi_i) z))_(1<=i<=m)`.

For an empty target this is the empty tuple. Its interpretation is also
the identity under the chosen finite-product convention. Thus
`unpack_Gamma o pack_Gamma=id_Gamma` and
`pack_Gamma o unpack_Gamma=id_[|Gamma|]` are provable componentwise
diagram equations. For Gamma empty, the second equality is precisely
the terminal equation z=u; it must not be silently omitted.

## Full faithfulness and essential surjectivity

Let Syn(Th_C) be the category of finite contexts and equivalence classes
of term tuples, with composition by capture-avoiding simultaneous
substitution. Define evaluation

`Eval:Syn(Th_C) -> C`

by the chosen context product on objects and the tuple of component
denotations on arrows. Soundness makes it well-defined; the substitution
lemma gives composition and identity preservation.

**Fullness.** Given any `f:|Gamma| -> |Delta|`, represent it by

`unpack_Delta o c_f o pack_Gamma`.

Here c_f has type `[|Gamma|]→[|Delta|]`. Evaluation is f because the
pack/unpack comparisons evaluate to identities. This includes empty
source contexts, using u, and empty targets, whose unique tuple evaluates
to the unique map to 1.

**Faithfulness.** If two tuple arrows have equal evaluations, projecting
their equal target-product arrows gives equal component denotations.
Every corresponding component equation is therefore an axiom of Th_C.
The tuples are equal in Syn(Th_C). With an empty target both tuples are
already the unique empty tuple.

**Essential surjectivity.** For each A in C, the singleton context [A]
evaluates to A. In fact evaluation is onto the object set with the chosen
singleton product convention.

An explicit quasi-inverse J sends A to [A] and f to `x |- c_f x`.
The displayed identity/composition equations make J a functor, and
`Eval o J=id_C`. The pack_Gamma maps form a natural isomorphism
`id_Syn -> J o Eval`: the naturality square evaluates to one equality
in C, so faithfulness proves it commutes syntactically. The inverse is
unpack_Gamma. This proves an actual category equivalence.

## Unit, product, and exponential preservation

The empty context evaluates to the specified terminal object 1.
The comparison

`j_(Gamma,Delta):|Gamma,Delta| -> |Gamma| × |Delta|`

is induced by the two tuples of finite-product projections. It is an
isomorphism by the two product universal properties; its inverse is the
tuple collecting all component projections. Thus evaluation preserves
context products through specified comparison isomorphisms, not through
an unsupported equality of differently bracketed products.

For Gamma=(S_1,...,S_m) and Delta=(T_1,...,T_n), the arrow-only context
category has exponential context

`Omega=(S_1→...→S_m→T_j)_(1<=j<=n)`.

For m=0 these component types are T_j; for n=0 the context is empty.
Its evaluation term is iterated application; lambda abstraction gives
currying. The beta/eta rules verify the exponential universal property.

The comparison

`chi:|Omega| -> |Delta|^(|Gamma|)`

is the categorical transpose of

`|Omega|×|Gamma| --j^(-1)--> |Omega,Gamma| --Eval(ev)--> |Delta|`.

It is an isomorphism: full faithfulness identifies arrows into |Omega|
with syntactic arrows into Omega, the syntactic exponential property
identifies those with arrows into Delta after a product with Gamma, and
the product comparison identifies these with arrows to |Delta| after a
product with |Gamma|. This correspondence is natural; every C-object is
the evaluation of a singleton context and every C-arrow has a syntactic
representative. Hence |Omega| has the same exponential universal property
as the specified target, and chi is its unique comparison isomorphism.

This is a CCC equivalence with explicit structural comparisons. The
assertion does not identify an arbitrary CCC with the bare free STLC
category, and does not assert an isomorphism of the concrete object sets
or an effective presentation of the given category.
