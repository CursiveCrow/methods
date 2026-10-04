# Presheaf topoi: primary-source packet and typed constructions

Date: 2026-09-06. Bounded research for `N-d-023`, `spec/registers/new-content.csv:170`: elementary topoi, intuitionistic internal logic, presheaf examples, and Kripke–Joyal semantics. Used the research skill, beginning with held acquisitions. No manuscript/shared record was edited, and no software tests, builds, or manuscript renders were performed. Source-page images were inspected where a downloaded primary scan lacked text. No other mathematical reviews were consulted.

## Acquired sources and exact identities

### 1. Mac Lane–Moerdijk 1992: registered source acquired

**Saunders Mac Lane and Ieke Moerdijk, *Sheaves in Geometry and Logic: A First Introduction to Topos Theory*, Springer-Verlag, 1992, Universitext.** An institutional copy was obtained from [University of Pisa mathematics hosting](https://poisson.phc.dm.unipi.it/~ciuffreda/Libri/Sheaves_in_geometry_and_logic_a_first_introduction_to_topos_theory.pdf).

Saved file: `tmp/pdfs/p10-topos/mac-lane-moerdijk-sheaves-in-geometry-and-logic-institutional.pdf`; 638 physical PDF pages; 24,603,140 bytes; SHA256 `A30AE90087DF702F6E48A705FF313CEB7821FAE55AB3CF43E255D4DCD7B95825`.

The scan has no useful embedded text in the inspected pages. Its copyright page at physical p3 was visually read: **©1992 Springer-Verlag New York Inc.**, ISBN **0-387-97710-4** and **3-540-97710-4**, printing line **9 8 7 6 5 4 3 2 1**. Thus the title/search-file metadata mentioning a later year is not the edition evidence. The registered `MacLaneMoerdijk1992` key is appropriate. The inspected main-text pages have physical page = printed page +11; this mapping was checked at printed pp1–2, 35–38, and 44–47. It should be checked again before assuming it across the entire scan.

The complete contents and actual primary passages **I§4 pp35–38** and **I§6 pp44–47** were read visually. The contents also locate I§8 *Heyting Algebras* at p50, I§9 *Quantifiers as Adjoints* at p57, VI§5 *The Mitchell–Bénabou Language* at p296, VI§6 *Kripke–Joyal Semantics* at p302, and VI§7 *Sheaf Semantics* at p315. Those latter are **contents locators only in this pass**; the actual body support for the logical clauses below was read in the author-hosted 2007 notes instead.

### 2. Moerdijk–van Oosten 2007: additional author-hosted primary presentation

**Ieke Moerdijk and Jaap van Oosten, *Topos Theory*, Department of Mathematics, Utrecht University, 2007.** [Author-hosted full PDF](https://webspace.science.uu.nl/~ooste110/syllabi/toposmoeder.pdf), linked from [van Oosten's teaching page](https://webspace.science.uu.nl/~ooste110/onderwijs.html), and identified by his author CV as joint 2007 lecture notes. Suggested key **`MoerdijkVanOosten2007Topos`**, type `unpublished` or `misc`, institution Utrecht University, year 2007, author PDF URL, note identifying lecture notes.

Saved file: `tmp/pdfs/p10-topos/moerdijk-van-oosten-topos-theory-2007.pdf`; **73 physical pages**, cover and contents followed by printed pp1–71; physical page = printed page +2; 402,372 bytes; SHA256 `C040B58ECCD6B2B095F20BE56B8F2C825C2E3036D8EC31C67E9D2CEA4A74ACAB`. The title page expressly says 2007. This is a separate work, not a draft of Mac Lane–Moerdijk 1992 or of Johnstone 2002.

Read the actual relevant portions of **§1 pp1–14**, **§2.2 pp29–32**, and **§3.3 pp53–59**, including the complete formulas for exponentials, classifier, implication, quantifiers, and forcing. Some verification steps in these lecture notes are exercises; the typed checks below fill the needed elementary details without claiming that every line is printed as a source proof.

### 3. Lawvere: exact six-page article acquired

**F. William Lawvere, *Quantifiers and Sheaves*, Actes du Congrès international des mathématiciens, Nice 1970, Tome 1, pp329–334.** Acquired the six-page original-layout article from the [Lawvere Archives PDF](https://lawverearchives.com/wp-content/uploads/2024/12/1970-quantifiers-and-sheaves.pdf), linked by the [archive's chronological list](https://lawverearchives.com/work/). Saved as `tmp/pdfs/p10-topos/lawvere-quantifiers-and-sheaves-icm1970.pdf`; 640,947 bytes; six PDF pages = printed pp329–334; SHA256 `25BD24945DBD216B384AB4B094FF1BB4315682D0D90817C0CAD77CB15DA74DE4`. All six pages were read. This is not a later TAC reprint.

**Publication-year correction for root consideration:** the conference and running heading say 1970, but the proceedings were published by Gauthier-Villars in **1971**. This is stated by the author's archive, and the title page of the [official IMU volume](https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1970.1/ICM1970.1.ocr.pdf) gives 1971. Existing key `Lawvere1970` may remain stable, but `handbook/bib/handbook.bib:3328–3334` currently uses 1970 as the publication year. Use publication year 1971 and retain Nice 1970 as the event/title year. No shared bibliography edit was made here.

### 4. Held-source identity clarification: no false SRC-041 record found

The generic filename `tmp/acquisition/src041/jhu-sheaves-full-volume-retry-01.body` is **Francis Borceux, *Handbook of Categorical Algebra 3: Categories of Sheaves***, not Mac Lane–Moerdijk. Its held layout extraction identifies that title and author, with first publication 1994 and transfer to digital printing 2004. This was initially encountered in the search for held sheaf/topos sources.

The acquisition record itself is **correctly identified**: `spec/research/acquisition-src-041.md:1` names *Handbook of Categorical Algebra, Volume 3*; lines **16–18** give JHU URLs explicitly named `Borceux1995HandbookOfCategoricalAlgebra3.CategoriesOfSheaves.pdf`. The generic local filename must not be used as evidence of an existing MLM1992 copy, but no mistaken source identity in the inspected acquisition-record header was found. No existing source was renamed, deleted, or relabeled.

### Other registered sources

The bounded held-file search did not locate exact Lambek–Scott1986 or Johnstone2002 full bodies. [Scott's author bibliography](https://www.site.uottawa.ca/~phil/papers/) links the book to Cambridge, rather than providing a full author download; its listing uses 1988, whereas the registered first edition is 1986. The public [Oxford Johnstone record](https://academic.oup.com/book/52926) verifies the 2002 publication but does not provide an acquired open full text in this pass. Neither metadata nor secondary reproductions were substituted for inspection of those book bodies. The acquired sources above suffice for the requested concrete presheaf development.

## Exact body locators and supported scope

| Item | Primary passage actually inspected |
| --- | --- |
| Presheaves, small base, variance | Moerdijk–van Oosten **§1 p1**: C small throughout; presheaves are `C^op→Set`; Yoneda representable `yc=C(-,c)` with postcomposition action on c. |
| Pointwise limits and colimits | Moerdijk–van Oosten **§1 p3**, paragraph following Proposition 1.1. It gives the pointwise construction and lists componentwise mono/epi criteria, empty initial presheaf, singleton terminal presheaf, and preservation of colimits by product with a presheaf. |
| Exponentials | Mac Lane–Moerdijk **I§6, Proposition 1, pp46–47**, formulas **(5)–(8)**: the natural-transformation formula, evaluation, and explicit transpose, with the full proof. Moerdijk–van Oosten **§1 pp4–5** gives the same object/action and proves the universal property using colimits of representables; evaluation naturality is Exercise 1 p5. |
| Classifier definition | Moerdijk–van Oosten **§1 pp5–6** defines the classifier's unique pullback property and proves its domain terminal. |
| Sieves, action, characteristic map | Mac Lane–Moerdijk **I§4 pp37–38**, formulas **(2)–(8)**. Moerdijk–van Oosten **§1 pp6–7** gives the complete proof, including naturality, recovery of the subpresheaf, and uniqueness. |
| Elementary topos definition | Moerdijk–van Oosten **Definition 1.2 p8**: finite limits, cartesian closedness, subobject classifier. Lawvere **p329, §1** uses a definition additionally listing finite colimits. Do not silently call these identical lists of primitive assumptions. Presheaves have the finite colimits pointwise as well. |
| Power objects and membership | Moerdijk–van Oosten **pp7–8, Exercise 4**: `P(X)=Ω^X`, `P(X)(c)=Sub(yc×X)`, restriction by pullback, membership detected at `(id_c,x)`. |
| Heyting subobject algebra and quantifier adjoints | Moerdijk–van Oosten **Theorem 1.8, pp10–11**: componentwise meets/joins, implication using every restriction arrow, reindexing preservation, direct-image existential and all-restrictions universal. **Exercise 8 p11** asks for Frobenius. |
| Presheaf first-order semantics and forcing | Moerdijk–van Oosten **§1.2.1 pp11–13**, **Definition 1.9 p12**, full clause list **p13**, and **Theorem 1.10 p13** for global truth of a sentence. **Theorem 1.11 p14** is a soundness/completeness statement explicitly given without proof; do not count it as a supplied completeness proof. |
| General higher-order semantics | Moerdijk–van Oosten **§3.3 pp53–58**, particularly exponential/power sorts, evaluation, lambda abstraction and comprehension pp57–58. Their arithmetic extension assumes a natural numbers object; it is not part of Definition 1.2. |
| Generalized-element Kripke–Joyal semantics | Moerdijk–van Oosten **§3.3 pp58–59**: factoring through the interpretation subobject; epimorphic locality for exists/disjunction; all generalized refinements for implication/forall. This is broader than forcing solely at base-category objects. |
| Sheaf-local differences | Moerdijk–van Oosten **§2.2 p32**, after defining sites/topologies: disjunction and existence hold on a covering sieve; the same atomic, conjunction, implication and universal clauses are retained. The earlier site and sheaf setup is necessary. |
| Historical topos/internal logic connection | Lawvere **pp329–330**: topos definition, truth-value object, intuitionistic/Heyting structure, quantifiers, and sieves (cribles) for a small-category presheaf topos. This is a concise announcement/overview, not the full pointwise construction proof. |

The existing Pitts1995Draft is useful for the logic interface, not as the sole source of the complete presheaf construction: **Definition 5.2.1 pp41–42**, **Example 5.2.5 pp42–43**, **Definition 5.4.1 p46**, and **§§5.5–5.6 pp51–59** give the indexed predicate/quantifier/equality framework. The preceding packet `p10-quantifier-adjunctions-source-note-2026-09-06.md` identifies that 1995 source separately from Pitts2000.

## Typed construction and proof details for the new text

### Sizes, pointwise limits, and monomorphisms

Fix a universe, a category C whose object and arrow sets belong to it, and presheaves taking values in that universe's Set. Natural transformations between fixed presheaves form a set: they are a subset of the product over objects c of function sets between the component values, subject to naturality equations. All the exponential and sieve values below are therefore sets in that universe. The entire presheaf category need not itself be small. For a larger base, change universes or state a separate size arrangement; mere local smallness of a large base does not suffice for these set bounds.

For a finite diagram `D:J→PSh(C)`, define `L(c)=lim_j D(j)(c)` in Set. Restrictions are the unique maps induced by the restricted component cones. Uniqueness proves their identity/composition laws; coordinatewise mediating maps prove the limit universal property in PSh(C). Empty J gives the constant singleton presheaf. Products are componentwise products and equalizers are componentwise equalizer subsets. If needed, the same argument gives all small limits and the dual construction all small colimits.

A componentwise injection is monic by cancellation at each component. Conversely, if `m:A→B` is monic, elements a,a' in A(c) with the same image give maps `yc→A` by Yoneda; their composites with m are equal, hence so are the maps and a=a'. Thus any mono can be represented by its componentwise image subpresheaf. This justifies using inclusions when proving the classifier.

### Exponential, action, evaluation, and currying

Put `E=Y^X`, with

`E(c)=Nat(yc×X,Y)`.

For `u:d→c`, set `E(u)(α)=α∘(yu×id_X)`, where `(yu)_e(v)=u∘v` for `v:e→d`. Thus

`[E(u)(α)]_e(v,x)=α_e(u∘v,x)`.

The identity and composition laws follow from composition; naturality in e follows from that of α. Define

`ev_c(α,x)=α_c(id_c,x)`.

For `u:d→c`, naturality of α gives

`Y(u) ev_c(α,x)=α_d(u,X(u)x)=ev_d(E(u)α,X(u)x)`.

For a natural map `h:Z×X→Y`, define its transpose by

`[λh_c(z)]_d(u,x)=h_d(Z(u)z,x)` for `u:d→c`.

Naturality of h proves that `λh_c(z)` is a natural transformation in d; functoriality of Z proves `λh` natural in c. Evaluation at the identity gives `ev∘(λh×id_X)=h`. Conversely, for `k:Z→E`, naturality of k gives `k_d(Z(u)z)=E(u)(k_c(z))`; evaluating this at `(id_d,x)` proves `λ(ev∘(k×id_X))=k`. These prove both inverse identities and the exponential universal property, including X or Y empty. The value is not in general the plain function set `Set(X(c),Y(c))`.

### Sieve classifier and characteristic maps

A sieve S on c is a set of arrows into c closed under precomposition. Let Ω(c) be all such sieves and

`Ω(u)(S)={v:e→d : u∘v∈S}` for `u:d→c`.

This is a sieve, with identity/composition laws inherited from composition. The truth map `true:1→Ω` selects the maximal sieve at each c. For a subpresheaf `A⊆X`, define

`χ_A,c(x)={u:d→c : X(u)x∈A(d)}`.

Closure of A under restrictions proves this is a sieve. Naturality follows from `X(v)X(u)=X(u∘v)`. It is maximal exactly when x belongs to A(c): one direction uses `id_c`, the other uses closure. Thus A is the pointwise pullback of true along χ_A.

For uniqueness, if χ has that pullback, then `u∈χ_c(x)` iff `id_d∈Ω(u)(χ_c(x))` iff `id_d∈χ_d(X(u)x)` iff `X(u)x∈A(d)`. Consequently χ=χ_A. Arbitrary monos are handled by their isomorphic image subpresheaves. The empty base C is harmless: its presheaf category has one object and one arrow, and the construction gives the degenerate elementary topos.

### Heyting implication, quantifiers, and a non-Boolean example

For subpresheaves `A,B⊆X`, joins/intersections and top/bottom are pointwise. Define

`(A⇒B)(c)={x∈X(c): for every u:d→c, X(u)x∈A(d) implies X(u)x∈B(d)}`.

Restriction stability follows by composing arrows. If `D⊆A⇒B`, use u=id to obtain `D∩A⊆B`. Conversely, if `D∩A⊆B`, restrict x∈D(c) along any u and apply the inclusion at d. This proves residuation. Pullback along a natural map preserves implication by substituting the naturality identity inside the displayed condition. The complement-like operation is `¬A=A⇒0`, not pointwise set complement in general.

For a projection `π:X×Y→X` and `R⊆X×Y`,

`(∃_π R)(c)={x∈X(c): ∃y∈Y(c), (x,y)∈R(c)}`,

`(∀_π R)(c)={x∈X(c): ∀u:d→c ∀y∈Y(d), (X(u)x,y)∈R(d)}`.

These are subpresheaves. The existential adjunction is the componentwise image property. For the universal one, any subpresheaf D with `π^*D⊆R` satisfies the displayed condition after restricting its elements; conversely u=id shows `π^*∀_πR⊆R`. This proves `∃_π⊣π^*⊣∀_π` and explains why the universal quantifier cannot be computed solely at c.

For a concrete non-Boolean presheaf topos take C with objects 0,1 and a single nonidentity arrow `a:0→1`. Presheaves have a restriction `X(1)→X(0)`. Let U be the subterminal with `U(0)={*}`, `U(1)=∅`. At stage 0, its negation is empty because U already holds; at stage 1, its negation is empty because restriction along a reaches U(0). Thus `¬U=0` and `U∨¬U=U≠1`. Equivalently Ω(1) is the three-element chain of sieves `∅`, `{a}`, `{a,id_1}`. At stage 1 neither U nor ¬U is forced. This is a local explicit example of the source's all-restrictions implication, not a claim of a separately numbered source example.

### Power objects and higher-order interpretation

Set `P(X)=Ω^X`. The exponential/classifier bijections give

`Nat(Z,P(X)) ≅ Nat(Z×X,Ω) ≅ Sub(Z×X)`, naturally in Z.

Hence `P(X)(c)≅Sub(yc×X)`. Its restriction along u is pullback along `yu×id_X`. Its membership subobject at c consists of `(S,x)` with `(id_c,x)∈S(c)`. In particular this is not simply the family of full external powersets `P(X(c))`.

Products and exponentials interpret product and function types, with beta/eta following from evaluation/transposition. Power objects interpret predicate types and comprehension: the classifying transpose of a subobject of `Z×X` is its predicate-valued term `Z→P(X)`, and pulling membership back gives the original formula subobject. These are the ingredients for intuitionistic higher-order logic. A natural numbers object is additional structure for arithmetic; presheaves possess the constant-N example, but an arbitrary elementary topos need not be assumed to have one merely from the topos definition.

## Presheaf forcing: exact clauses and the sheaf boundary

Keep an explicit finite variable context with interpretation Γ. For `γ∈Γ(c)`, define `c⊩φ(γ)` to mean `γ∈⟦φ⟧(c)`, equivalently that its characteristic sieve contains `id_c` (and hence is maximal). For `u:d→c`, write `γu=Γ(u)γ`. The clauses obtained from the constructions above are:

| Formula | Presheaf stage condition |
| --- | --- |
| Atomic relation | The tuple of interpreted terms belongs to the designated relation subset at c. |
| `t=s` | Their values at γ in the component at c are equal. |
| top / bottom | Top always holds; bottom never holds at a base object c. |
| `φ∧ψ` | Both hold at c. |
| `φ∨ψ` | At least one holds at c. |
| `φ⇒ψ` | For every `u:d→c`, forcing φ at γu entails forcing ψ there. |
| `¬φ` | No `u:d→c` forces φ at γu. |
| `∃x:Y φ` | There is `y∈Y(c)` such that φ holds at `(γ,y)` at c. |
| `∀x:Y φ` | For every `u:d→c` and every `y∈Y(d)`, φ holds at `(γu,y)` at d. |

Induction gives persistence under every restriction arrow. The membership interpretation and these clauses agree by the explicit operations; a sequent is valid when its pointwise antecedent meet is included in its conclusion subpresheaf, for every stage and assignment. This supplies soundness through the preceding quantifier-adjunction framework without importing the source's unproved completeness theorem. A sentence is globally true iff it is forced at every c. If C is empty, there are no stages and the presheaf topos is degenerate, so global truth is vacuous.

At an arbitrary generalized object E of a topos, the more general Kripke–Joyal forcing relation means the parameter arrow factors through the formula subobject. Here disjunction can require an epimorphic two-piece cover, existence an epimorphism `E'→E` carrying a witness, implication and forall all arrows `E'→E`, and bottom means E is initial. At representables in a presheaf category these specialize to the stage clauses above. Do not insert cover-local disjunction/existence into the elementary presheaf stage definition without explaining this change of test objects.

For **sheaves on an explicitly specified site `(C,J)`**, the stage clauses for disjunction and exists change: the arrows on which a disjunct holds, respectively on which a witness exists, must form a J-covering sieve. Bottom holds when the empty sieve covers c; in particular negation then needs its proper implication-to-bottom reading. These clauses presuppose the Grothendieck topology and sheaf semantics. No sheafification theorem, site construction, or geometric-morphism result is asserted by this packet.

## Source slips and scope checks to retain

The 2007 notes are useful but should not be copied mechanically. Their Theorem 1.8 universal-image display on p11 writes an equality between an element at D and x at C; the correctly typed condition is `φ_D(y)=X(u)(x)`. The naturality calculation for the sieve classifier on p7 also contains a composition-order slip in one intermediate line; the typed formula uses `u∘v`, as above. These do not affect the intended constructions when written with their domains.

The notes' Exercise 56 p57 suggests truth is unchanged by dropping unused variables. With possibly empty sort interpretations this requires an inhabitance qualification: a false closed formula becomes vacuously true in an added empty context. Retain explicit contexts, or impose the nonempty/inhabited-sort convention already documented in the quantifier packet. Do not use that exercise to erase this distinction.

The source chapter's higher-order type list on p57 calls `Y^X` a sort of functions in the opposite direction in one phrase; evaluation `Y^X×X→Y` and the correct p58 interpretation fix the intended direction `X→Y`. NNO and arithmetic are optional additional scope. No choice of witnesses is required for the displayed presheaf constructions or the stagewise existential clause.

This packet establishes actual primary support for the concrete presheaf topos construction and its logical interpretation. Unread sections of acquired books, mere catalogue entries, and the broader source statements given without proof remain distinguished from the passages and elementary arguments checked here.
