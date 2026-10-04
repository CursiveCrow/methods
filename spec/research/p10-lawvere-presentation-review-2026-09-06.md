# Independent review of the named Lawvere presentation

Date: 2026-09-06 Pacific time. The actual-file review began at
2026-09-07 04:15 UTC.

## Result and scope

**Scoped pass: no concrete mathematical defect found.** Read both
actual files in full:

- `handbook/parts/p10/lawvere-presentations.tex`, lines 1–151;
- `handbook/annex/p10/lawvere-presentations.tex`, lines 1–277.

Also checked the dependency interfaces in
`handbook/parts/p10/lawvere-theories.tex`: structural finite-set functor,
selected projections and `p_0^1=1_1` at lines 24–57; explicitly contextual
equations and the least substitution-compatible congruence family at
lines 64–113; tuple-valued term-theory hom-sets and evaluation at lines
115–143; models and all natural transformations at lines 154–213.
The proof labels reviewed are `annex:p10.lawvere-present.1` and `.2`.

The author's manuscript and shared files were not edited. No other
review conclusions were consulted, and no tests, builds, or renders
were used. This note records mathematical incorporation, not a new
source-edition audit.

## 1. Signature and explicit equation families

Body lines 16–45 correctly assign an n-ary operation name to each
actual arrow `f:n->1`. Domains distinguish the arities. The projection
equations and the composition/substitution equations are well typed
in their specified finite contexts.

The k=0 equation

`sigma_f() ≈ sigma_(f o !_n)(x_0,...,x_(n-1))`

is essential and is present. It identifies a closed term used in a
larger context with the named operation of that declared arity. No
projection equation is required in context zero. The families are
set-indexed by the small arrow set and finite tuples, so no class of
new symbols or choice of representatives is introduced.

## 2. Substitution and the evaluation kernel

Annex lines 7–47 verify tuple projections, the identity tuple, tuple
precomposition, and the full substitution equation. The nullary
operation case uses `!_k o a = !_n`; the k=0 source-context case is
explicitly retained.

Lines 49–76 show that the defined equations have equal interpretations,
and that semantic equality forms a family of congruences stable under
substitution across all finite contexts. Replacing equal substitution
components also preserves evaluation because their tuple arrows are
equal. The least-family definition therefore proves the soundness
inclusion. If a term set is empty, its relation is empty; the proof
does not need a ground term to serve as a default representative.

Lines 78–103 give a complete structural induction reducing each term
to its named interpretation. A variable uses the projection equation
in reverse. A compound uses congruence on its immediate subterms and
then exactly one composition equation. A nullary term uses the k=0
instance with no induction hypotheses. Thus equal interpretations give
the same named term and hence equational equality. This supplies the
reverse kernel inclusion; the theorem does not merely assume a full
semantic diagram as an axiom set.

## 3. The evaluation isomorphism and zero contexts

The functor at annex lines 105–139 is well defined on component
classes. Identity preservation uses the projection tuple, while
composition is the proved substitution equation. Faithfulness follows
by projecting equal target tuples, and fullness is given by the exact
inverse

`h:n->m |-> ([sigma_(p_j^m o h)(x_n)])_(j<m)`.

Evaluating this tuple recovers h. Applying it after evaluation
recovers the original term classes by the normalization already
proved. Thus this is an identity-on-objects isomorphism, not just
an unspecified equivalence. Lines 141–153 additionally verify the
inverse functor's composition and identity laws directly.

The singleton tuple convention is respected: at a target 1, the
identity `p_0^1=1_1` makes the interpretation of a one-component
tuple equal to that component arrow. For target 0, the tuple is
empty and unique.

Lines 167–184 cover both zero-source possibilities. If `0->m`
exists for m>0, each projected component has a nullary operation
name and therefore a ground term. If `T(0,1)` is empty, there are
neither nullary symbols nor ground terms, and no arrow `0->m`
for positive m can exist. In a composite `n->0->m`, the special
nullary substitution equation proves the required equality in
context n. No zero-context case is omitted.

Lines 186–191 explicitly accommodate coincident projections:
when `p_i^n=p_j^n`, the shared operation name and the two projection
equations identify the corresponding variables. The proof requires
the structural finite-set functor to preserve products, not to be
faithful.

## 4. Theory morphisms and restriction on all homomorphisms

Body lines 114–127 and annex lines 197–226 correctly characterize
theory morphisms as identity-on-objects functors preserving the
selected projections. Projection comparison proves preservation of
all tuples. Block projections then prove preservation of selected
finite products, and compatible product isomorphisms handle other
representatives. Terminal uniqueness covers the empty product.
The same tuple calculation proves equivalence with commuting with
the structural finite-set functors, including empty target tuples.

For `H:T->U`, restriction has direction
`H^*:Mod(U)->Mod(T)`. Annex lines 228–245 check naturality of every
restricted transformation at H(a). No invertibility or additional
condition on a model homomorphism is imposed. Underlying carriers
remain literally M(1), because H fixes object 1. This is compatible
with a model originally having carrier A^1; it does not identify
A^1 with A. Nonempty-carrier full subcategories are therefore
preserved. Reversed composition of restriction functors has the
correct order.

Finally, lines 247–275 define an arity-preserving translation by
`sigma_f -> sigma_(H(f))`. Each projection equation maps to a
projection equation; each composition equation maps to one because
H preserves tuples and composition. This includes k=0. Translation
commutes with simultaneous substitution, so it descends through the
least congruence families. Term induction proves the commuting
evaluation square on components, hence on all tuple arrows and
objects.

The presentation-recovery proof does not invoke the later free-model
theorem. Its use by that theorem is therefore acyclic. No repair is
required within the assigned mathematical scope.
