# Categorical section: exact primary-source packet

Date: 2026-09-06. Bounded source research using the research skill. Reused the held Pitts manuscript and its acquisition record before looking for an additional author-hosted source. No manuscript changes, tests, builds, renders, or new agents.

## Pitts: held author manuscript and version

The held files are `tmp/acquisition/src030/cambridge-categorical-logic-author.pdf` and its `.layout.txt` extraction. Existing record: `spec/research/acquisition-src-030.md`, especially its source-identity table and the file record at line 474. This is **Andrew M. Pitts, Categorical Logic, 18 May 1995**, not an unidentified chapter or the final published chapter pagination.

- Author PDF URL: <https://www.cl.cam.ac.uk/~amp12/papers/catl/catl.pdf>.
- Official report record: <https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-367.html>.
- Report metadata: University of Cambridge, Computer Laboratory, **UCAM-CL-TR-367**, May 1995, DOI `10.48456/tr-367`; the report record says 94 pages.
- Held PDF: **95 physical pages**, including the unnumbered title cover, followed by local pages 1–94; 1,816,311 bytes; SHA256 `3520D326EABA40B2679583E80AEFA06EB8B98822B511DE313C3DDAC574F038BB`.
- Printed page p is physical PDF page p+1. PDF conversion metadata dates from 26 April 2012; the author manuscript's printed date is 18 May 1995.
- Its cover refers to a forthcoming Volume VI of the *Handbook of Logic in Computer Science*. The later publication is in Volume 5. Keep the manuscript/report identification and its local pagination separate from the final chapter.

Suggested key: **`Pitts1995CategoricalLogic`**, type `techreport`, author `Pitts, Andrew M.`, title `Categorical Logic`, institution `University of Cambridge, Computer Laboratory`, number `UCAM-CL-TR-367`, year 1995, month May, date `1995-05-18`, DOI above, and author PDF URL.

### Exact Pitts locators

| Topic | Source locator and scope |
| --- | --- |
| Background category notions | Introduction, p2, explicitly assumes familiarity with functors, natural transformations, limits, and adjunctions. This chapter is not a self-contained primary proof source for their elementary definitions or Yoneda. |
| Categorical term semantics | §2.2, pp7–10. Variables are product projections, terms-in-context are arrows from the context product, and weakening uses projections. |
| Substitution | **Lemma 2.2.1**, in §2.2: substitution is interpreted by composition with the corresponding tuple/pairing map. |
| Soundness of equational semantics | **Theorem 2.2.3**, §2.2: a model of a theory in a category with finite products satisfies its equational consequences. |
| Internal signatures | **§2.3, pp10–11**, and Proposition 2.3.1: sorts name objects, operation symbols name morphisms from finite products, and equations express equality, identity, composition, and universal constructions. |
| Function-type semantics | **§3.3, pp22–24**: abstraction is currying, application is evaluation after pairing, β/η are the two inverse laws for the hom-set correspondence. Rules/equations (3.19)–(3.22) give the exact β/η correspondence. |
| Context category | **§4.2, pp30–32**: objects are contexts modulo consistent renaming, equivalently finite lists of sorts; arrows are tuples of terms modulo componentwise provable equality; composition is simultaneous substitution; identities are tuples of context variables. |
| Finite products from contexts | **Proposition 4.2.1, p32**: empty context is terminal; concatenation of contexts is a product, with subtuple projections and tuple concatenation as pairing. |
| Choice of context representatives | **Remark 4.2.2, pp32–33**: using canonical representatives from an enumerated variable supply gives strictly associative and unital context products. |
| Generic model and completeness | **Lemma 4.2.4, pp33–34**: the generic model identifies an interpreted term with its syntactic arrow and satisfies exactly the provable equations. |
| Universal property | **Theorem 4.2.5, pp34–35**, and Corollary 4.2.6, p35: models correspond to finite-product-preserving functors out of the classifying category; uniqueness is up to the compatible natural isomorphism. |
| Recovering a category | **§4.3, pp35–36**: name all objects and morphisms and take all equations true in the category. The interpretation functor from the resulting classifying category is full, faithful, and essentially surjective. |
| Size boundary | **§2.3 p10 and §4.3 p36**: the internal signature and axiom collection are sets only for a small category. Otherwise a universe or class-sized-language convention is required. |
| Arrow-only CCC construction | **§4.4, p38, “Function types”**: exponentials for arbitrary finite contexts are built from iterated arrow types. The source expressly says product types are unnecessary for this conclusion. |
| Datatype theory extensions | **Remark 4.4.1, pp38–39**: the generic-model/completeness and universal-property discussion extends to theories with product, disjoint-union, and function types; this displayed version is bicartesian closed. Use the preceding function-type construction for the present arrow-only case. |

## Application to the live arrow-only sheet

The actual `handbook/registry/calculi/stlc.tex` has base types and the arrow type former only; terms are variables, typed abstractions, and applications. Contexts are finite lists of distinct typed variables. The sheet has compatible β reduction, but no product/unit type constructors and no η rule.

The category construction can preserve this typing calculus exactly. Declare, separately, the **typed αβη equational congruence** used to identify arrows. For η, the term equation is λx.(M x)=M when x is fresh for M and the context. This does not assert that η contraction is already one of the sheet's β-reduction rules. Substitution must respect the congruence, with bound variables renamed to avoid capture.

Objects should be finite type lists Γ=(A_1,…,A_n), not only individual types. A morphism Γ→Δ=(B_1,…,B_m) is an m-tuple of Γ-typed terms, modulo componentwise αβη equality. The empty tuple is the unique arrow Γ→(), and concatenation gives products. Pairing is an operation on arrow tuples; it is not an additional term constructor.

Pitts p38 gives exactly the needed exponential:

\[
\Delta^\Gamma=
(A_1\to\cdots\to A_n\to B_1,\ldots,
 A_1\to\cdots\to A_n\to B_m),
\]

with right-associated arrows. Its evaluation tuple is (f_j x_1⋯x_n)_j, and currying abstracts the n new variables in each component. Repeated β proves evaluation after currying; repeated η proves currying after evaluation. If Γ is empty, the curried target type is B_j itself; if Δ is empty, the exponential is the empty context and the hom-set correspondence is between singleton sets. These cases need no nonexistent unit type.

For semantic interpretation in a chosen CCC, interpret a context by its finite product, a variable by its projection, application by evaluation after pairing, and abstraction by the transpose of the body arrow. State the given product/exponential choices or preservation up to their canonical comparison isomorphisms. The correctly typed bijection is

\[
\mathcal C(I\times A,B)\cong\mathcal C(I,B^A),
\quad h\mapsto\Lambda(h),
\quad k\mapsto\operatorname{ev}\circ(k\times1_A).
\]

The forward and inverse formulas should be typed explicitly: OCR of the held Pitts display around p24 is poor.

### Internal-language boundary

The free context category of the unextended arrow-only calculus does not recover every arbitrary CCC from an arbitrary interpretation of its base types. Many arrows of the target need not be definable in that language.

For the full internal-language reconstruction, follow Pitts §§2.3 and 4.3: use a **separate named internal theory** with symbols for all relevant objects and arrows and all equations valid in the target. For a CCC, extend that internal theory with the function-type structure, as in §4.4. Faithfulness then comes from the chosen true-equation theory; fullness comes from naming the arrows; essential surjectivity comes from naming the objects. With a small category and specified structural choices this is a set-sized construction.

If expressing the internal theory using only curried typed constants, name each relevant arrow from a finite context product to an interpreted target type by a constant of the corresponding curried type, including closed constants for arrows from the terminal object. This is an explicitly expanded internal signature, not a silent addition to the original STLC sheet. Equivalence, rather than literal identity of categories or syntaxes, is the justified conclusion. The uniqueness in Pitts Theorem 4.2.5 is relative to the specified agreement with the interpreted generic model; it does not rule out arbitrary unrelated automorphisms.

## Riehl: live author-hosted elementary toolkit

Downloaded <https://emilyriehl.github.io/files/context.pdf> to `tmp/pdfs/p10-categorical/riehl-category-theory-in-context.pdf`.

**Version caution:** although the [author's books page](https://emilyriehl.github.io/books/) still describes the 2016 Dover first edition, the actual current PDF explicitly identifies itself as a **second edition** and its preface describes changed content and numbering. It has 299 physical pages, 1,948,866 bytes, SHA256 `E4779F34FF0432508F1105912F39A84AF3C64799B969507325C80E27C2D994DD`. PDF creation/modification metadata is **31 August 2026, 07:39 UTC−04:00**. This is a file-production date, not proof of a printed second-edition publication date. Printed page p is physical PDF page p+20.

Suggested separate key **`Riehl2026ContextOnline`**: Emily Riehl, *Category Theory in Context*, author-hosted second-edition text, online version retrieved 6 September 2026, with a note recording the PDF metadata date and exact URL. Do not describe these local page numbers as verified 2016 edition locators.

Verified toolkit locators in this exact version:

- **Definition 1.1.1, p3**: category, identities, and associative composition.
- **Definition 1.3.1, p14**: functor and both preservation laws.
- **Definitions 1.4.1 and 1.4.3, p25**: natural transformation and natural isomorphism.
- **Theorem 2.2.4, pp61–63**: Yoneda for a set-valued covariant functor on a locally small category, with naturality. The contravariant version used by the handbook is its dual, explicitly **Exercise 2.2.i, p66**. Local smallness suffices; the particular natural-transformation collection is shown to be a set by the bijection.
- **Definitions 3.1.1–3.1.2, p82**: constant diagrams, cones, and cocones.
- **Definition 3.1.5, p83**: limits/colimits as representations of the cone functors. Its footnote specifies that a small indexing category and locally small target ensure sets of cones.
- **Definition 3.1.6, p84**: limit as terminal cone and colimit as initial cocone. **Proposition 3.1.7, p84**: uniqueness up to the unique isomorphism respecting the selected cones, not uniqueness among all possible object isomorphisms.
- **Definition 4.1.1, p132**: an adjunction is a hom-set bijection natural in both variables.
- **Definition 4.2.5, p140**: unit η:id_C⇒GF and counit ε:FG⇒id_D with Gε∘ηG=id_G and εF∘Fη=id_F.
- **Theorem 4.2.7, pp140–142**: equivalence of the hom-bijection data, unit/counit triangle data, and universal-arrow forms. Its proof gives the transposition maps f↦Gf∘η and g↦ε∘Fg and verifies that these recover the original data.

## Registered-source boundary

The registry identifies Mac Lane's *Categories for the Working Mathematician*, second edition (1998), Awodey's *Category Theory*, second edition (2010), Lambek's *From λ-calculus to Cartesian Closed Categories* (1980), pp375–402, and Lambek–Scott's *Introduction to Higher Order Categorical Logic* (1986). In the held acquisition/source directories inspected, no identifiable complete body of these exact editions was found. Their bibliography records were not used as substitutes for proof content. Pitts supplies the exact context/function-type construction, and the newly identified Riehl second-edition file supplies the elementary proofs; both should be cited under their own source identities.
