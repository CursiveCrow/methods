# Equational logic: independent actual-text review

Date: 2026-09-06. Review performed on the live files beginning 2026-09-07 01:37:50 UTC, including the contextual-replacement paragraph added during this pass.

## Result and scope

**Scoped mathematical pass.** No defect was found in the definitions, deduction system, or three annex proofs in the requested files. One minor theorem-statement clarification is recommended below; the annex proves the correct assertion already.

Read in full:

- `handbook/parts/p10/equational-logic.tex`;
- `handbook/annex/p10/equational-logic.tex`;
- `handbook/registry/calculi/equational-logic.tex`.

For conventions, also read the host's algebra definition and HSP/variety paragraph. Compared the citations with `spec/research/p10-equational-logic-source-note-2026-09-06.md` and independently checked the acquired primary PDF at II Theorem 11.4 and II Definitions 14.14–14.18/Theorems 14.17/14.19. No other review was consulted. No manuscript files were edited, and no tests, builds, or renders were run.

## One statement clarification

**Incorporated after review:** the actual theorem now says that for each
consequence s≈t, some finite Γ0⊆Γ already implies s≈t. The root read back
this wording after the patch. The finite premise set is allowed to
depend on the selected conclusion.

In `thm:p10-equational-completeness`, currently part-file lines 131–132, the wording “a finite Γ0 ... already implies each consequence” can be read as a single finite premise set that supports every consequence. Replace it by an explicit per-conclusion formulation:

> For every equation s≈t with Γ ⊨alg s≈t, there is a finite Γ0⊆Γ such that Γ0 ⊨alg s≈t.

This is a quantifier clarification, not a flaw in the proof: the last paragraph of `annex:p10.eq.2` takes the finitely many premises of the deduction of the selected equation. The stronger single-finite-basis reading would be false. For example, in a signature with independent nullary symbols c_i,d_i for natural numbers i, the identity set {c_i≈d_i : i∈N} has no finite subset implying every member: interpret a missing pair differently in a two-element algebra and all the selected pairs equally.

## Verification of terms, semantics, and deduction

`def:p10-term-algebra` correctly gives a nonempty term algebra exactly when the variable set is nonempty or there is a nullary symbol. The recursive operations cover arity zero. The universal extension, substitution law, and homomorphism/evaluation law in `annex:p10.eq.1` follow by the stated structural inductions, including the constants case.

The variable alphabet V in `def:p10-equational-logic` need not be infinite. Every claimed deduction and identity is over that same V, and the sole needed hypothesis is Tτ(V)≠∅. In particular, V=∅ with a nullary symbol is permitted: there is one empty valuation, substitutions on V are unique, the endomorphism of the ground-term algebra is the identity, and all the later arguments still apply. The proof does not require a fresh variable to simulate a context.

The corrected semantic implication is at the algebra level: every premise must hold under every valuation in A. The substitution proof correctly uses the original identity at the new assignment w(x)=σ(x)^A(v); there is no remaining use of the invalid rule for fixed local premises. The local-versus-identity example is mathematically correct: x≈y forces a one-element algebra in the empty signature, whereas the supplied valuation in a two-element set distinguishes the local relation. Its four named variables specify the alphabet needed for that example.

The registry's premise, reflexivity, symmetry, transitivity, operation compatibility, and simultaneous substitution rules match the body. Nullary compatibility has no premises and yields the reflexive constant equation, as required.

The newly supplied comparison between contextual replacement and operation compatibility is valid. For a selected occurrence, induction on its distance to the root combines the changed argument with reflexivity on unchanged arguments. In the converse direction, replacement at the selected argument positions followed by transitivity changes all arguments. Repeated equal subterms cause no difficulty because the occurrence, rather than only the term value, is selected. Arity zero is reflexivity. This is the same deductive closure as the source's II Definitions 14.14–14.16.

## Verification of completeness and finite choices

Reflexivity, symmetry, transitivity, and compatibility make θΓ a congruence; every term-algebra endomorphism is induced by a substitution, so the substitution rule makes it fully invariant. Conversely, induction over a finite deduction puts every derivable pair into any fully invariant congruence containing Γ. This proves the claimed leastness without an unstated closure step.

The quotient B is nonempty by the explicit term-algebra hypothesis, and operation compatibility makes every induced operation well defined. For any selected premise p≈q and valuation v:V→B, only the finitely many variables occurring in those two terms require representatives. A fixed term supplies every other substitution value. Therefore evaluation of p and q agrees with the quotient classes of their substituted terms. Substitution of the premise gives equality of those classes. This proves B⊨Γ at arbitrary quotient valuations and does not require a section of the quotient map or any axiom of choice for an infinite family.

If V is empty, the finite representative family and the substitution domain are empty, while p and q are ground terms; the same proof applies. If Γ is empty, the premise argument is vacuous. The canonical valuation x↦[x] evaluates each term to its own class in all these cases. It therefore falsifies exactly a conclusion whose pair is absent from θΓ, giving the stated contrapositive completeness argument.

The last paragraph establishes finite support for an arbitrary premise set by collecting the finite number of actual premise occurrences in the chosen derivation. No assumption that Γ itself is finite is used.

## Verification of free algebras

The relation θ(V,X) is the intersection condition on evaluation kernels, hence is a congruence. Defining it as a predicate on the set of term pairs is legitimate even if the model class is proper. The class of models of a set of identities contains the trivial algebra, so no empty-model-class exception has been hidden here.

Membership of the quotient F in the variety is proved directly, without assuming what must be shown. For each defining identity over V and each V-valuation into F, representatives are selected only for the finite set of occurring variables. This yields a substitution V→Tτ(X), even when X and V differ. Every algebra in the variety validates the substituted identity at every X-valuation by the substitution law, so its term pair lies in θ(V,X). The quotient consequently satisfies every defining identity.

For a target algebra A in the variety, the map [t]↦t^A(v) is well defined by the defining kernel condition, preserves operations, and extends the generator map. Term induction proves uniqueness. The usual two universal extensions give mutually inverse isomorphisms, and uniqueness also fixes the isomorphism commuting with the generator maps.

The generator map is correctly not required to be injective: the trivial variety collapses all generators. The construction requires Tτ(X)≠∅, so X=∅ is supported when constants exist. Without constants the manuscript correctly refrains from a general existence claim; the two constant maps from any nonempty set to {0,1} refute initiality in the empty signature. The caveat allowing special varieties with an initial algebra is also correct.

The free-monoid example verifies the universal property directly. Finite words form a monoid under concatenation, with the empty word as unit; assignment of letters extends by finite multiplication and unit preservation. Associativity proves preservation of concatenation, and generation by letters plus the unit proves uniqueness. X=∅ gives exactly the one-element monoid.

## Citation compatibility

The body correctly distinguishes the 2012 update from the original 1981 edition and uses its aligned main pagination. II Definitions 10.1–10.4 support the term presentation; II Definition 11.1 and II Definition 14.11 support universal identity semantics and algebra-level consequence. II Theorems 14.12/14.17 support the fully invariant closure account, and II Theorem 14.19 is indeed the equational completeness theorem on printed p95.

The free-algebra citation to II Theorems 10.7, 10.10, 10.12 and II Theorem 11.4 is appropriate. The latter, on printed pp73–74, identifies identity validity, validity in the relative free algebra, equality of the term classes there, and membership in the defining congruence. The manuscript gives its own direct quotient-membership proof, so it does not silently import the source's different presentation using generator images.
