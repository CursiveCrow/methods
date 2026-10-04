# Mac Lane–Moerdijk 1992: verified logic and forcing passages

Date: 2026-09-06. Bounded primary-source check using the research skill. This note upgrades only the **specific body passages actually read** from the earlier contents-only locator list in `p10-presheaf-topos-source-note-2026-09-06.md`. No manuscript/shared file was edited, and no software tests, builds, or manuscript renders were performed. Necessary source-page images were generated and inspected because the acquired book scan lacks useful text extraction.

## Sources and inspected scope

Primary scan: `tmp/pdfs/p10-topos/mac-lane-moerdijk-sheaves-in-geometry-and-logic-institutional.pdf`, **Saunders Mac Lane and Ieke Moerdijk, Sheaves in Geometry and Logic, Springer-Verlag 1992**. Its copyright/ISBN identity was verified in the acquisition packet. The current scan's printed page p occurs at physical PDF p+11 in every passage inspected here, including pp50, 147, 198, 296, and 318. Retain key **`MacLaneMoerdijk1992`**. Source URL: [institutional Pisa copy](https://poisson.phc.dm.unipi.it/~ciuffreda/Libri/Sheaves_in_geometry_and_logic_a_first_introduction_to_topos_theory.pdf).

Actually read: **I§8–9 pp50–61; III§8 pp147–149; IV§8–9 pp198–209; VI§5–6 pp296–312; VI§7 pp315–318**. The III/IV passages were selected because the initially requested I§9 and VI sections refer to them for the full all-arrow quantifier and Beck–Chevalley statements. Unrelated adjoining arguments on some page images are not adopted as reviewed theorem content. VI§6 pp313–314 were not read, and are not needed for its forcing Theorem 1, whose proof ends on p309.

Comparison source: `tmp/pdfs/p10-topos/moerdijk-van-oosten-topos-theory-2007.pdf`, **Ieke Moerdijk and Jaap van Oosten, Topos Theory, Utrecht University 2007**, [author PDF](https://webspace.science.uu.nl/~ooste110/syllabi/toposmoeder.pdf). Retain separate key **`MoerdijkVanOosten2007Topos`**. The already-read pp10–14 and pp53–59 were compared with the 1992 statements. The p11 universal-quantifier and p7 classifier displays were additionally inspected as source images to distinguish actual printed slips from text-extraction problems.

## Verified locators and proof status

| Needed claim | Exact 1992 body support | Proof status in the source |
| --- | --- | --- |
| Heyting implication as residual | **I§8 p50, equation (1)**: `z≤(x⇒y)` iff `z∧x≤y`. **Proposition 3 pp54–55** gives the finite equational characterization. | Definitions and explicit proof of the equivalence with the equations. |
| Subpresheaf Heyting implication | **I§8 Proposition 5 p56**, formula **(18)**; negation formula **(19)**. | The proof uses the complete pointwise lattice and infinite distributivity to obtain a Heyting algebra, prints the explicit restriction-arrow formulas, and expressly leaves further verification to the reader. It is not a fully written componentwise residuation proof. |
| Powerset projection quantifiers | **I§9 Theorem 1 p57**. | Short explicit order-adjunction proof. |
| Powerset arbitrary-function quantifiers | **I§9 Theorem 2 p58**. | Explicit direct-image and fibre-containment formulas; the adjunction verification is described as immediate. These are ordinary sets, not the component formula for arbitrary presheaf morphisms. |
| Slice quantifiers | **I§9 Theorems 3–4 pp58–61**: pullback on slice categories; left adjoint always, right adjoint under the stated cartesian-closed slice hypothesis. | Explicit constructions and reduction to exponentials/pullbacks. Keep the slice-category functors distinct from subobject-poset quantifiers. |
| All-arrow quantifiers for sheaves, hence presheaves under the trivial topology | **III§8 pp147–148, equations (13) and (15), Proposition 2 p148**. | Both formulas and adjunction arguments are supplied. Some subfunctor/sheaf checks for the existential image are left to the reader, with stability/transitivity of the topology identified; universal restriction stability and the sheaf check are written out. The converse universal-adjunction implication is called easier rather than expanded. |
| Reindexing preserves Heyting structure in a topos | **IV§8 Theorem 1 (External) p201**; corresponding **Internal** theorem pp201–202. | The external proof reduces to slice-topos structure and preservation of exponentials, sums, and epis from the earlier Theorem IV.7.2. The internal proof constructs operations by Yoneda and the power-object correspondence. These paragraphs are actual proofs with explicit prior dependencies, not standalone proofs of every earlier topos fact. |
| Frobenius | **IV§9 p204, equation (2)**. | Full chain of order equivalences using implication preservation and the existential adjunction. |
| Existential Beck–Chevalley | **IV§9 Proposition 1 p205**, equation **(4)**, and the symmetric identity immediately after it. | Explicit proof by pulling back an epi–mono image factorization, using previously established pullback stability of epis and monos. |
| Subobject right adjoint in a topos | **IV§9 Proposition 3 p208**. | Restricts the right adjoint on slice categories to subobjects of their terminal objects. Its existence depends on the earlier slice right-adjoint theorem, explicitly cited. |
| Universal Beck–Chevalley | **IV§9 p209, equation (13)**. | Derived by taking adjoints of the symmetric existential square. This is the external subobject-poset identity needed for the manuscript. The internal power-object version is described analogously and its proof is left as Exercise 9. |
| Internal existential quantifier on power objects | **IV§9 Theorem 2 pp206–208**. | Representability/Yoneda construction and internal BC proof supplied; the internal projection/Frobenius formula is left as Exercise 9. |
| Internal universal quantifier on power objects | **IV§9 Proposition 4 p209**. | Constructed from the natural external right adjoints by the same Yoneda argument; the further internal BC verification is left as Exercise 9. |
| Mitchell–Bénabou language | **VI§5 pp298–300**: types are objects, terms arrows from variable products, formulas terms of type Ω; application, equality, membership, and lambda transposition on pp298–299; quantifiers p300. | Definitions and explicit interpretation formulas. This does not supply a complete formal proof system or a proof of soundness for every rule of one. |
| Comprehension and predicate-valued terms | **VI§5 pp299–301**, application/membership and lambda on p299, set-builder pullback **(4)** p300; quantifiers **(3)–(6)** pp300–301. | Explicit definitional construction through the classifier, power objects, and transposition. Arithmetic constructions are qualified by the presence of an NNO, p298. |
| Generalized-element forcing definition | **VI§6 p303, equations (1)–(2)**; equality and persistence/local character p304. | Definition by image inclusion, equivalently factorization through the interpretation subobject; local-character proof supplied. |
| Generalized-element forcing clauses | **VI§6 Theorem 1 pp304–305**, proof **pp305–309**; atomic equality/membership **Propositions 2–3 p310**. | Detailed proofs for conjunction, disjunction, implication, existence, and universal quantification. Negation is expressly left to the reader on p307. Membership proof p310 is indicated by the classifier/evaluation relation rather than fully expanded. |
| Site/sheaf forcing | **VI§7 pp315–318**, especially **Theorem 1 p316** and proof p317. | Stated for an established site `(C,J)` and sheaf category, using sheafified representables. The first proof on p317 reduces each clause to the explicit formulas in III§8; a second proof outlines reduction from generalized-element forcing and cites the generating/covering properties established earlier. |
| Presheaf stage specialization | **VI§7 end of p317 and top of p318**, clauses **(ii′), (iv′), (v′)** together with retained clauses (i), (iii), (vi) from p316. | Explicit specialization to the trivial topology, with current-stage disjunction/existence and all-restrictions implication/universal quantification. This is now body evidence, not merely an inferred contents locator. |

VI§5 **p302** explicitly refers the specification of a formal intuitionistic calculus and its rule details to Boileau–Joyal and Lambek–Scott. Therefore this part of the 1992 book is a semantics source, not a substitute for the handbook's own registered-calculus soundness proof. Likewise the 2007 notes' Theorem 1.11 p14 is explicitly stated **without proof**, and should not be described as an inspected completeness proof.

## Correctly typed formulas and comparison with the 2007 notes

Let C be a small category, and let `f:X→Y` be a natural transformation between presheaves. If A is a subpresheaf of X, the formulas for its existential and universal images are

`(∃_f A)(c)={y∈Y(c): there exists x∈A(c) with f_c(x)=y}`,

`(∀_f A)(c)={y∈Y(c): for every u:d→c and x∈X(d), f_d(x)=Y(u)(y) implies x∈A(d)}`.

The second condition compares elements of **Y(d)** on both sides. One cannot compare `f_d(x)` directly with the unrestricted y in Y(c). **MLM III§8 (15), p148**, gives exactly this restriction as `y·u`; it is independently compatible with the presheaf stage forall clause in **VI§7 Theorem 1 p316**. MVO2007 Theorem 1.8 p11 intends this condition but omits the restriction in its printed display; see the defect ledger below.

For A,B subpresheaves of X, **MLM I§8 (18), p56**, is

`(A⇒B)(c)={x∈X(c): for every u:d→c, X(u)(x)∈A(d) implies X(u)(x)∈B(d)}`.

MVO2007 Theorem 1.8 p10 agrees and actually spells out preservation of this operation under pullback by a natural transformation. Meets and joins are componentwise, but implication is not the stagewise material implication. Its residuation check is left brief in both sources, so a self-contained manuscript should retain the explicit two-inclusion proof already prepared in the earlier source packet. MVO2007 gives ∃ as the pointwise image on p10, verifies its adjunction on p11, and asks the reader to check the universal adjunction there. Its Frobenius calculation is Exercise 8 p11.

For a **sheaf** morphism on `(C,J)`, the existential formula changes: the arrows `u:d→c` on which the restricted y has a witness form a **covering sieve**. This is **MLM III§8 (13), p147**. The universal formula remains the all-arrow condition in (15). The sheaf check uses the topology and the target being a subsheaf; this cannot be asserted before introducing the site. For the trivial topology the covering condition contains an identity witness and reduces to the current-stage presheaf image formula.

### Exact use of the two Beck–Chevalley equations

Use the pullback notation from MLM IV§9:

```
P = C ×_A B  --p--> B
      |             |
      q             f
      |             |
      v             v
      C -----g----> A .
```

Proposition 1 p205 proves `g^*∃_f=∃_q p^*`, and by symmetry also `f^*∃_g=∃_p q^*`. Taking right adjoints of the **symmetric** identity gives

`g^*∀_f=∀_q p^*`.

The other orientation, `f^*∀_g=∀_p q^*`, is the displayed square (13) on p209. This distinction matters: taking right adjoints of one composite reverses its order and changes which sides are quantified. Do not assert the desired same-orientation universal identity without the symmetric existential square or an independent argument. MVO2007 p56 gives this same symmetry-and-adjoints reasoning in compressed form.

These are statements about actual categorical pullback squares. For a merely commuting square only the usual mate comparison is automatic, as already addressed by Pitts and the preceding powerset packet; neither source licenses deleting the pullback/stability requirement.

## Power objects, comprehension, and three meanings of forcing

**Power-object comprehension.** In the Mitchell–Bénabou language, formulas are Ω-valued terms. A formula with variables of types X and Z determines a characteristic map `Z×X→Ω`; its exponential transpose is a term `Z→Ω^X=P(X)`. Evaluation/membership reconstructs the original predicate as a pullback. These steps are printed as lambda, membership and set-builder interpretations in **VI§5 pp299–300**. In a presheaf topos `P(X)(c)=Sub(yc×X)`, not generally the external powerset of X(c); this is explicit in **MVO2007 pp7–8**, with the detailed membership formula assigned as Exercise 4. The 1992 internal-language passage uses the categorical power object, not arbitrary independent component subsets.

**Base-object stages of a presheaf category.** For `γ∈Γ(c)`, stage forcing is membership in the component of the formula subpresheaf. **MLM VI§7 pp317–318** and **MVO2007 p13** agree:

- conjunction means both at c;
- disjunction means one disjunct at c;
- existence means a witness in the quantified presheaf's component at c;
- implication tests every restriction `u:d→c`;
- universal quantification tests every such u and every value of the quantified type at d;
- negation means no restriction forces the positive formula.

The initial presheaf is empty at every base object, so bottom is never forced at a base stage. If the base category is empty there are no stages, and validity is vacuous in the resulting degenerate topos. Neither source's use of base stages requires C to have products; the products needed for variable contexts live in the presheaf topos.

**Arbitrary generalized elements.** For `α:U→Γ` in an elementary topos, forcing means factorization through the interpretation subobject, **MLM VI§6 p303**. Disjunction may be witnessed by maps `V→U`, `W→U` whose copairing is epi; existence may require an epi `V→U` and a witness defined on V. Implication and universal quantification range over all arrows into U. Bottom holds exactly when U is initial; thus negation allows a positive-forcing refinement only when that refinement is initial. These are **Theorem 1 pp304–305**, proved pp305–309, and match **MVO2007 pp58–59**. Replacing arbitrary U by representables in a presheaf category explains the simpler current-stage clauses, rather than making the two formulations literally the same definitions on the same test objects.

**Site/sheaf stages.** The site version tests `c∈C` and sections of sheaves at c, equivalently generalized elements from **a(yc)**, where a is the already constructed associated-sheaf functor. **MLM VI§7 pp315–316** spells out these equivalences and Theorem 1. Disjunction and existence hold over a J-cover; implication and forall retain all arrows into c. Negation must account for objects with an empty covering family. In particular bottom at c means the empty sieve covers c, not that c is absent or literally an initial object of C. **III§8 p149, equation (18)** describes the least subsheaf at such objects, and (19) gives negation. The 2007 notes' p32 cover-local clauses agree.

MLM **VI§7 Remark 2 p317** explicitly warns that the generalized-object generic-element test `U×Y` does not automatically become a single base-stage test. An analogous simplification requires C to have products and the quantified sheaf to be representable as `a(yB)`. No sheafification, enough-points, site comparison, or geometric-morphism theorem was reconstructed in this bounded task; the site-level statements retain their source setup and dependencies.

## Relevant source defects and safeguards

The following were pinned to actual page images, rather than inferred from OCR:

1. **MVO2007 p11, Theorem 1.8 universal-image display:** it prints `φ_D(y)=x` for x at stage C. It must read `φ_D(y)=X(f)(x)` (or `x·f`) when `f:D→C`. The uncorrected equality compares different component sets and can define the wrong subset when component carriers overlap accidentally. MLM **III§8 (15), p148**, provides the correct positively verified version.
2. **MVO2007 p7, sieve-classifier naturality calculation:** with `f:C'→C` and `g:D→C'`, one intermediate expression prints `X(gf)(x)`. The correctly typed composite is `X(fg)(x)`, meaning `X(f∘g)(x)`. The next line already uses fg. This is a local order typo, not a different convention.
3. **MLM III§8 p147, sentence introducing (13):** it says y belongs to E(C), although the output is a subobject of F and y must belong to **F(C)** for `φ:E→F`. Formula (13) itself and the subsequent proof correctly use the restricted target value in F(D).
4. **MLM IV§8 p201, prose below diagram (10):** the inclusion `i_A` is printed with target `E/B`; diagram (10) and the construction require **`E/A`**.
5. **MLM IV§9 p204, sentence before Frobenius (2):** V is printed as ranging over Sub(A), but in that calculation U,V are subobjects of B. Use **V∈Sub(B)**; all the preceding adjunction steps type that way.
6. **MLM VI§5 p300, display (5):** the parameter letter changes from Y in the surrounding projection to U in its displayed adjoint domains. Use one parameter object consistently when reproducing the formula.

The first three bear directly on the new componentwise presheaf mathematics and must not be copied without correction. The other three are straightforward type/letter slips in the cited exposition.

Retain the prior substantive safeguard from **MVO2007 Exercise 56 p57**: dropping unused variable declarations cannot preserve truth in arbitrary empty-sort interpretations. Keep explicit contexts or an inhabitance hypothesis. The source's p57 function-sort phrase also reverses the direction in words once; its displayed evaluation and p58 interpretation correctly give functions `X→Y` for `Y^X`. Its addition of natural-number and recursion sorts presupposes an NNO. None of these points warrants treating an unrestricted generic doctrine as reflecting equality of base arrows.

## Conclusion

The previously contents-only MLM1992 logic and forcing pointers now have actual body support with the exact locators above. For the new presheaf section, the most compact source chain is **I§8 Proposition 5 p56** (implication), **III§8 Proposition 2 pp147–148** (correctly typed all-arrow formulas), **IV§8 Theorem 1 p201 and IV§9 pp204–209** (Heyting reindexing, Frobenius, and both BC identities), and **VI§5 pp298–301 / VI§6 Theorem 1 pp304–309 / VI§7 Theorem 1 pp316–318** (internal language and the three forcing scopes). The distinctions between printed proofs, reader verifications, exercises, and cited prerequisites remain explicit. This is source verification, not a manuscript, build, or rendered-output acceptance result.
