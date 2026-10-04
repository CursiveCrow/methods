# Independent review of the presheaf topos construction

Date: 2026-09-06. Read the complete actual body `handbook/parts/p10/presheaf-topos.tex` (initial review snapshot lines 1–212) and annex `handbook/annex/p10/presheaf-topos.tex` (lines 1–336). Scope: all three proof pairs `psh.3–.5`, the definitions and source paragraphs, and both calculations in the two-stage example.

Also read the full live `handbook/parts/p10/presheaf-categories.tex` interface, the host's `def:p10-topos`, and the newly saved `def:p10-categorical-size` in `handbook/parts/p10/categorical-toolkit.tex`. The preceding pointwise-limit and componentwise-morphism theorems were used through their live statements; their other reviewers' conclusions were not read. Source attribution was compared with the actual held MLM1992/MVO2007 passages previously inspected in the source packets. Only this owned note was written; no manuscript/shared edits, tests, builds, or manuscript renders were performed.

## Review result and incorporation items

No proof-level mathematical defect was found in the exponential, sieve-classifier, or power-object constructions. The detailed checks below validate the requested interfaces and empty cases.

Two small incorporation points were reported to root: the exponential theorem initially used k in its second inverse law without declaring its type `k:Z→Y^X` (the annex already declares it correctly), and the new MVO2007 citation key was not yet present in the live bibliography. Final read-back status is recorded at the end of this note.

## Interface and size assumptions

The presheaf interface uses `u:d→c` to define `X(u):X(c)→X(d)`, with `X(u∘v)=X(v)X(u)`. Its Yoneda assignment on representing objects is covariant, so `yu:yd→yc`. This matches every action used in the new exponential and classifier formulas.

The updated size convention was read in full at `categorical-toolkit.tex:6` onward. It explicitly states transitivity, inclusion of N, pairing, powersets, and closure under unions indexed by small sets. These imply closure under subsets, function sets, quotient sets, and small-indexed products. The ambient collection of all sets is a permitted default; set-sized relativizing universes must have the indicated Grothendieck closure, with their existence an additional hypothesis rather than a theorem of the categorical development.

Those exact closures justify the subsets of products used for natural transformations (annex lines 8–16), sets of sieves (lines 127–128), and subpresheaf families (lines 229–239). The small object and arrow sets of C bound the indices and hom-sets. The proofs do not assert that the whole presheaf category is small or choose a representative from a large collection of monomorphism domains.

The host's elementary-topos definition requires finite limits, exponentials, and a classifier for every mono, with no nondegeneracy or NNO requirement. These are exactly the properties established here together with the preceding interface.

## Exponential: `annex:p10.psh.3`

**Body lines 15–51; annex lines 7–27.** The value `Nat(yc×X,Y)` has the displayed set bound. For `u:d→c`, precomposition with `yu×id_X` has the correct source and target and produces a natural transformation. Testing its component on `v:e→d` gives `α_e(u∘v,x)`, with x at the unchanged stage e. Successive precompositions give the correct contravariant restriction order. No global element or representative is selected.

**Evaluation — annex lines 29–40.** Naturality of α at u gives `Y(u)α_c(id_c,x)=α_d(u,X(u)x)`. The restriction formula at the identity of d identifies the latter with the restricted evaluation. Both input coordinates have the correct stage, including the X-restriction in the second coordinate.

**Both transpose naturalities — annex lines 42–65.** For fixed c,z the component `h_d(Z(u)z,x)` is a natural transformation `yc×X→Y`: naturality of h at `v:e→d` and `Z(v)Z(u)=Z(u∘v)` prove the square. The second check, varying c along u, agrees componentwise at every `v:e→d`. Thus the transpose is a map of presheaves, not just a family of functions at stages.

**Both inverse laws — annex lines 67–89.** Evaluation at `id_c` gives h back. Conversely, with `k:Z→Y^X` and `h=ev∘(k×id_X)`, naturality of k turns evaluation at d of its restricted c-value into `[k_c(z)]_d(u,x)`. Equality holds for every component and argument, proving the second inverse identity and uniqueness. The proof supplies exactly the typing needed by the theorem's initially undeclared k.

**Naturality of the hom-set bijection — annex lines 91–109.** Precomposition in Z is handled using the naturality of `a:Z'→Z`. For `b:Y→Y'`, postcomposition `α↦b∘α` defines `b^X`, commutes with restriction, and preserves identities/composition in b. The two transpose equations therefore prove naturality in the two variables actually claimed. No extra unproved naturality in a varying exponent X is needed for this statement.

**Empty cases — annex lines 111–120.** When X=0, every domain `yc×X` is initial, so every exponential component is a singleton. For Y=0 a natural map exists precisely when every domain component is empty, and is then unique; if any component is nonempty there is no map. Arbitrary empty components create no exceptional step in the elementwise proofs. If C is empty, there is one empty functor and one transformation, so all universal-property hom-sets are singletons.

## Sieve classifier: `annex:p10.psh.4`

**Sieves and truth — body lines 65–84; annex lines 126–147.** Restricting S along u gives precisely the arrows v for which u∘v belongs to S. Closure under further precomposition follows from sieve closure. The identity and composite actions have the correct order. A sieve containing `id_c` contains every arrow into c, so truth selects the unique maximal sieve and is preserved by restriction. Each singleton-domain truth component is injective; the live componentwise mono theorem makes the transformation monic. The correspondence with subpresheaves of yc has both directions immediately from precomposition.

**Characteristic map — annex lines 149–174.** Restriction stability of A makes the indicated set of arrows a sieve. Naturality is checked with the correct composite `u∘v`, avoiding the printed MVO source's intermediate composition typo. Its value is maximal exactly at the elements of A(c). The proof establishes the pullback universal property for the actual displayed subset A(c), rather than identifying it literally with a separately chosen set of pullback pairs. Pointwise limits give the required square in the presheaf category.

**Uniqueness and arbitrary monos — annex lines 176–203.** For any competing characteristic map, membership of u in its sieve is detected by identity membership after restriction; naturality and the pullback identify that with `X(u)x∈A(d)`. This determines every value of the map. For a mono `m:B→X`, the canonical image A has `B→A` componentwise bijective and hence naturally isomorphic by the interface. Transporting the inclusion square across that isomorphism proves the classifier property for m itself. Conversely, any characteristic square for m has that same image subpresheaf, so the uniqueness argument applies. Thus classification is independent of the chosen mono representing a subobject.

**Naturality and empty base — annex lines 205–223.** The component formula proves `χ_(a^*A)=χ_A∘a` for every presheaf map a, using the naturality of a. Empty components make this a vacuous equality where appropriate. For an empty base, the unique identity map is the truth map and classifies the sole subobject; this is allowed by the live elementary-topos definition.

## Power objects: `annex:p10.psh.5`

**Classification — body lines 128–158; annex lines 229–265.** Canonical image subpresheaves give a small set of actual subset families representing Sub(W), without choosing mono-domain representatives. For `P(X)=Ω^X`, uncurrying and classifier pullback are two bijections. The composite sends k to `(k×id_X)^*(∈_X)` because membership was defined as the inverse image of truth along evaluation. Transposing χ_S is the inverse. Naturality in Z follows either by composing the two proven naturalities or by the displayed equality of iterated inverse images.

**Stage identification and action — body lines 161–171; annex lines 267–282.** The actual exponential component is `Nat(yc×X,Ω)`. Applying the classifier bijection gives the canonical identification with `Sub(yc×X)`. Its restriction is precomposition and hence pullback along `yu×id_X`; at stage e the map sends `(v,x)` to `(u∘v,x)`. In particular x remains an element of X(e), so no restriction of x is needed inside that fixed-stage inverse-image formula.

**Membership — body lines 173–179; annex lines 284–302.** Before identification, a membership pair is `(α,x)` and is accepted exactly when `α_c(id_c,x)` is maximal. Under the classifier identification this is precisely `(id_c,x)∈S(c)`. Restriction stability is also checked directly: the S-restriction takes `(id_c,x)` to `(u,X(u)x)`, which becomes `(id_d,X(u)x)` in S restricted along u. The product order `P(X)×X` is consistent throughout the definition and its component formula.

**Classifying a relation — body lines 180–185; annex lines 304–324.** The map `bar z:yc→Z`, with component `u↦Z(u)z`, is natural. Pulling S back along `bar z×id_X` yields exactly S_z. Classifier naturality and the exponential transpose identify this subpresheaf with the value of the unique power-object classifying map at z. Pulling membership back then recovers S componentwise by testing `(id_c,x)∈S_z(c)`. This is equality of canonical subobject representatives, and the image convention extends it to arbitrary monos.

**Empty cases — annex lines 326–334.** P(0) is terminal and its membership has initial domain. Every `Z×0` is initial and has one subpresheaf, so the power-object bijections are between singleton sets. The empty-base case again has one presheaf and one subobject. All intermediate formulas are defined on their actual domains, including empty sets, and none selects a family of witnesses.

## Two-stage counterexamples

Body lines 196–211 use C with one nonidentity arrow `a:0→1` and `X(0)={*}`, `X(1)=empty set`. There is one arrow from either base object to 1, so y1 is terminal (not necessarily literally the selected constant-singleton representative).

The presheaf `y1×X` has a singleton component at 0 and an empty component at 1. A map from it to the initial presheaf cannot have its 0-component, so `(0^X)(1)` is empty. In contrast the external function set from X(1)=empty set to the empty set has its unique empty function.

That same product has exactly two subpresheaves: the stage-1 subset is forced empty, while the singleton stage-0 subset can be empty or full; both choices respect the sole restriction. Consequently P(X)(1) has two elements, whereas the external powerset of X(1) has one. Both examples correctly witness the asserted failures of componentwise exponential/powerset formulas.

## Source fidelity

The actual body citations match the inspected sources:

- Body lines 54–57: **Mac Lane–Moerdijk 1992, I§6 Proposition 1 pp46–47, formulas (5)–(8)** supplies the exponential, evaluation and explicit transpose; **MVO2007 §1 pp4–5** supplies the same component and restriction formulas. The present proof additionally writes out both naturalities and inverse laws explicitly.
- Body lines 118–123: **MLM1992 I§4 pp37–38, formulas (2)–(8)** gives sieves, restriction and characteristic map. **MVO2007 §1 pp6–7** gives the characteristic-map uniqueness argument. The actual new proof uses correctly typed composition, including where MVO has a printed typo.
- Body lines 190–194: **MVO2007 §1 pp7–8, Exercise 4** describes power objects, their component identification and membership. The body accurately says its own annex supplies the restriction, membership and classification proofs; it does not promote the source exercise into a fully written source proof.

The held MLM scan was verified as the 1992 edition, and MVO is the separate Utrecht 2007 lecture-note source. No claim conflates these sources with each other, with Pitts, or with an unread book manifestation. The two-stage calculations are locally supplied examples and are not falsely assigned a numbered source result.

## Read-back before incorporation

At the final read-back, 2026-09-07 05:48 UTC, the explicit size convention was saved and had been read in full; its closure requirements support all size arguments in this scope. The exponential theorem still used k at body line 42 without the local declaration `k:Z→Y^X`, and the key `MoerdijkVanOosten2007Topos` still had no entry in `handbook/bib/handbook.bib`. Both incorporation items had been reported to root; the theorem's annex already gives k the correct type, and the primary source metadata and citations themselves are verified.

At that snapshot, the three proofs and both example calculations passed the scoped mathematical review, with those two statement/bibliography incorporation items still open. No proof-level defect remained.

## Incorporation confirmed: final scoped pass

Read back the saved updates at 2026-09-07 05:49 UTC. Both reported incorporation items are resolved:

- `handbook/parts/p10/presheaf-topos.tex:39–43` now explicitly quantifies `k:Z→Y^X` before the two inverse identities. This agrees with the already checked annex and does not change either proof.
- `handbook/bib/handbook.bib:6552–6559` now contains `MoerdijkVanOosten2007Topos`, correctly identifying Ieke Moerdijk and Jaap van Oosten, *Topos Theory*, Utrecht University lecture notes (2007), and the verified author-hosted `toposmoeder.pdf` URL.

The expanded `def:p10-topos` at `handbook/parts/p10/algebraic-and-categorical-logic.tex:235–259` was read in full. It states local smallness, finite limits, exponentials, and the exact unique-characteristic-map pullback property for every monomorphism. Its element-free factorization expansion is equivalent to that pullback because the other cone leg is the unique map to the terminal object. The checked presheaf construction satisfies the added local-smallness condition through the live preceding theorem and supplies the entire classifier property for arbitrary monos through `.psh.4`.

The cited MVO Definition 1.2 p8 is the verified finite-limit/exponential/classifier definition; the local-smallness convention is compatible with this manuscript's scope. The host places the definition before the presheaf imports at lines 267–268. Its adjacent distinction between the 1970 congress, the 1971 publication, and Lawvere's additional listed finite-colimit requirement is consistent with the inspected source. No new proof obligation is introduced for presheaves, whose small colimits are already supplied by the preceding interface.

**Final result: scoped pass, with no unresolved mathematical, statement-typing, or source-incorporation finding in the reviewed `.psh.3–.psh.5` material.** This does not establish build, render, or whole-Part-X acceptance, nor does it count the separate pointwise foundations proofs as independently reviewed here.
