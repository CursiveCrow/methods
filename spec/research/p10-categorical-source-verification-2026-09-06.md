# Categorical sources: verification of the six drafts and toolkit locators

Date: 2026-09-06. Source check began 2026-09-07 03:39:31 UTC. Used the research skill and inspected the held primary sources. No mathematical reviewers' conclusions were read. No manuscript/shared source edits, tests, builds, or manuscript renders were performed; only this note was written.

## Result

**The current six drafted proof items have appropriate Pitts 1995 source grounding. No unsupported attribution was found in their actual wording.** The drafts supply their own proofs and correctly distinguish their explicit constructions from literal source formulas. One optional locator improvement is to cite Pitts §4.4, p38, immediately after the curried-context exponential in the Cartesian-lambda body, because that is the most direct source for the arrow-only case.

This is a source-scope verification, not a replacement for the independent mathematical reviews or an integration/build result.

## Exact source identities

### `Pitts1995Draft`

Andrew M. Pitts, *Categorical Logic*, author manuscript dated **18 May 1995**, associated with University of Cambridge Computer Laboratory technical report **UCAM-CL-TR-367**, May 1995, DOI `10.48456/tr-367`.

- Held PDF: `tmp/acquisition/src030/cambridge-categorical-logic-author.pdf`.
- Held extraction: the corresponding `.layout.txt` file.
- Author URL: <https://www.cl.cam.ac.uk/~amp12/papers/catl/catl.pdf>.
- Official report record: <https://www.cl.cam.ac.uk/techreports/UCAM-CL-TR-367.html>.
- Extent: **95 physical PDF pages**, the title cover plus local pages 1–94. Local printed page p is physical PDF page p+1.
- SHA256: `3520D326EABA40B2679583E80AEFA06EB8B98822B511DE313C3DDAC574F038BB`.

The source cover refers to a forthcoming Volume VI. The later published chapter associated with `Pitts2000` is a different manifestation, in the eventual handbook volume. The checked statements below use the **1995 manuscript's local page numbers**. This pass makes no claim that those numbers or exact wording match the later published body. The PDF's 2012 conversion metadata is not a new author-manuscript date.

### `Riehl2026ContextOnline`

Emily Riehl, *Category Theory in Context*, **author-hosted second-edition text**, <https://emilyriehl.github.io/files/context.pdf>.

- Held PDF: `tmp/pdfs/p10-categorical/riehl-category-theory-in-context.pdf`.
- Extent: **299 physical pages**, 1,948,866 bytes.
- SHA256, rechecked: `E4779F34FF0432508F1105912F39A84AF3C64799B969507325C80E27C2D994DD`.
- File metadata gives 31 August 2026, 07:39 UTC−04:00 for creation/modification. This is a **PDF-production timestamp**, not a verified printed publication date.
- The front matter expressly identifies a second edition; pp xvi–xvii describe changed content and numbering. It must not be identified as the 2016 Dover first-edition file.
- Printed page p is physical PDF page p+20.

Use the required key `Riehl2026ContextOnline`, with an online-version note and retrieval date. No printed second-edition publisher/date is established by this evidence.

## Pitts support for each drafted proof

Read the actual two body files and six annex items in `cartesian-lambda.tex` and `internal-cartesian-language.tex`.

| Actual proof item | Exact primary support | What the manuscript supplies itself |
| --- | --- | --- |
| `annex:p10.lambda.1`, typed substitution and equality | Pitts §2.1 supplies equations-in-context and substitution rules; §4.2, pp30–32, uses simultaneous substitution to compose context morphisms. Lemma 2.2.1 in §2.2 gives the corresponding **semantic** substitution law. | The detailed capture-avoiding typed induction, freshness bookkeeping, substitution associativity, and preservation of typed βη equality are explicit manuscript proofs. They are not falsely identified as the statement of Pitts's semantic lemma. |
| `annex:p10.lambda.2`, Cartesian closure of contexts | §4.2, pp30–32, defines finite lists of sorts and tuple arrows; **Proposition 4.2.1, p32**, proves terminal empty context and concatenation products. **§4.4, p38**, gives the curried-list exponential and expressly says product types are unnecessary. | Repeated β and η, parameter naturality, and the separate empty-source/empty-target cases are spelled out in the manuscript. |
| `annex:p10.lambda.3`, categorical soundness and completeness | **Lemma 2.2.1**, §2.2, substitution as composition; **Theorem 2.2.3**, §2.2, equational soundness. **§3.3, pp22–24**, especially (3.19)–(3.22), gives β/η as the exponential inverse laws. **Lemma 4.2.4, pp33–34**, identifies generic-model equality with provable equality; §4.4 extends the function-type construction. | The separating context-category model is fully worked out for the exact arrow-only syntax, including the interpretation of singleton contexts as 1×A in general and the literal singleton interpretation in the syntactic model. |
| `annex:p10.internal.1`, named type and context comparisons | **§2.3, pp10–11, Proposition 2.3.1**, names category objects/morphisms and expresses identity, composition, terminal objects, and products by equations. §3.3 provides the function-type interpretation. | The specific constants c_f,u,pair,e,l, the κ/ι recursion, and pack/unpack tuples are the manuscript's chosen arrow-only encoding. Pitts does not print those exact named formulas. The body accurately says they follow his method rather than claiming to quote them. |
| `annex:p10.internal.2`, evaluation equivalence | **§4.3, pp35–36**, takes all equations true in the named category and obtains a full, faithful, essentially surjective interpretation functor. It expressly restricts a set-sized internal language to a small category. **Theorem 4.2.5, pp34–35**, gives the generic model's universal property. | The explicit quasi-inverse, packing unit, projection counit, naturality, and triangle calculations remove a need to choose object representatives. The exact 1×A comparisons are author-supplied details. |
| `annex:p10.internal.3`, preservation of CCC structure | **§4.4, p38**, makes the function-type context category Cartesian closed; the generic-model discussion through **p39** states preservation of products and exponentials, within its broader datatype setting. | The explicit product comparison j and exponential comparison χ, with their universal-property proofs and empty-context cases, specialize and elaborate this construction. |

### Source boundaries correctly retained by the drafts

The original STLC sheet remains arrow-only and gives β reduction. The draft adds **typed βη equational metatheory** for its categorical quotient, rather than claiming η was already a reduction rule on that sheet. Tuple pairing is a construction of context arrows, not a new product-term constructor.

Pitts's p38 object for contexts Γ=(A_1,…,A_m) and Δ=(B_1,…,B_n) is precisely the list of right-curried types (A_1→⋯→A_m→B_j)_j. Thus the arrow-only CCC assertion has direct source support; it does not depend on borrowing the richer product/unit syntax from another source section.

The named internal-language draft explicitly adds constants and the **full true equational diagram**, assumes the category small, and does not assert that its displayed finite list of structural equations axiomatizes all of that diagram. These are the essential hypotheses behind Pitts's §4.3 reconstruction. The source's theory-category equivalence is not an equivalence between an arbitrary interpreted CCC and the unextended free βη category. The final paragraph of the current draft correctly makes that distinction.

Pitts's Theorem 4.2.5 uniqueness is relative to a specified isomorphism of interpreted models. It is not a statement that objects or functors have no unrelated automorphisms. The current explicit comparison construction does not make that stronger claim.

## Riehl locators: exact second-edition statements

| Toolkit item | Verified locator | Scope and formulas |
| --- | --- | --- |
| Category | **Definition 1.1.1, p3** | Objects and arrows with specified domains/codomains, identities, associative and unital composition. |
| Functor | **Definition 1.3.1, p14** | Preserves domains/codomains, identities, and composition. |
| Naturality | **Definition 1.4.1, p25** | For α:F⇒G and f:c→c′, α_(c′)∘Ff=Gf∘α_c. **Definition 1.4.3, p25**, makes a natural isomorphism componentwise invertible. |
| Cones/cocones | **Definitions 3.1.1–3.1.2, p82** | A cone over K:J→C is Δc⇒K; a cocone is K⇒Δc. |
| Universal limits/colimits | **Definition 3.1.5, p83**, and **Definition 3.1.6, p84** | Represented cone functors, equivalently terminal objects in cone categories and initial objects in cocone categories. The p83 footnote uses small J and locally small C to ensure sets of cones. |
| Uniqueness | **Proposition 3.1.7, p84** | Two limits have a unique isomorphism commuting with the selected cone legs; dually for colimits. This does not prohibit automorphisms of the underlying object that change the cone. |
| Limits from products and equalizers, dual colimits | **Theorem 3.5.11, pp112–113** | Any small diagram's colimit is a coequalizer between coproducts, when those objects exist; dually its limit is an equalizer between products. Small coproducts plus coequalizers imply cocompleteness; small products plus equalizers imply completeness. The displayed proof assumes local smallness or a larger universe. **Remark 3.5.14, p113**, describes direct verification of the universal property as an alternative proof. |
| Yoneda | **Theorem 2.2.4, pp61–63** | For F:C→Set and locally small C, Nat(C(c,−),F)≅F(c), by evaluation at id_c, natural in c and F. |
| Contravariant Yoneda | **Exercise 2.2.i, p66**, explicitly the dual of Theorem 2.2.4 | For F:C^op→Set, Nat(C(−,c),F)≅F(c). The inverse sends x∈F(c) to the transformation with component f:d→c ↦ F(f)(x). This dual follows by applying the proved theorem to C^op; it is not separately printed as Theorem 2.2.4's covariant statement. |
| Hom-adjunction | **Definition 4.1.1, p132** | F:C→D and G:D→C with D(Fc,d)≅C(c,Gd), natural in both variables. |
| Unit/counit and triangles | **Definition 4.2.5, p140** | η:id_C⇒GF, ε:FG⇒id_D, with Gε∘ηG=id_G and εF∘Fη=id_F. |
| Equivalence of adjunction data | **Theorem 4.2.7, pp140–142** | Natural hom-bijections, unit/counit triangle data, and the corresponding universal-arrow forms determine each other. Transposition is f↦Gf∘η; its inverse is g↦ε∘Fg. The proof checks recovery of the original data, not only existence of some correspondence. |
| Preservation by adjoints | **Theorem 4.5.2, pp158–159** | Right adjoints preserve existing limits; left adjoints preserve existing colimits. The proof transposes cone legs and uses uniqueness. It does not assume the categories complete/cocomplete, and it does not say arbitrary adjoints create or reflect these (co)limits. |

### The product/equalizer construction with correct directions

For K:J→C, take

\[
P=\prod_{j\in\operatorname{Ob}J}Kj,
\qquad Q=\prod_{u:j\to k}Kk.
\]

The two arrows P⇉Q have u-components π_k and K(u)∘π_j. Their equalizer, with its induced projections to Kj, is the limit. The dual construction has two arrows

\[
\coprod_{u:j\to k}Kj\ \rightrightarrows\
\coprod_jKj,
\]

whose u-components are the injection at j and the injection at k composed with K(u). Its coequalizer is the colimit. All identities of J may be included; their constraints are redundant but harmless. Empty J requires the empty product/terminal object or empty coproduct/initial object. For finite diagrams the proof uses only finite products/coproducts and an equalizer/coequalizer. Finite means the required object and arrow index sets are finite, not merely finitely many objects with arbitrarily many arrows.

### Yoneda size and variance limits

Local smallness suffices for the represented natural-transformation collection in Yoneda to be identified with a set. It does not imply that every natural-transformation collection in Set^(C^op) is small when C is large; **Remark 2.2.7, pp63–64**, explicitly distinguishes these issues. If the toolkit introduces the whole functor category as locally small, it should use a small domain or a suitable universe convention. Dualizing Yoneda changes C to C^op, not Set to Set^op, and does not turn the theorem into a claim about transformations from arbitrary functors into representables.

## Incorporation conclusion

The existing exact Pitts references in the two drafted bodies are supported. Adding §4.4 p38 beside the arrow-only exponential would improve the local source pointer but is not needed to repair an unsupported claim. Retain the separate source identities `Pitts1995Draft`, `Pitts2000`, and `Riehl2026ContextOnline`; the checked PDF pages provide no license to identify their manifestations or assign an unverified printed second-edition date to Riehl.

## Read-back of the newly saved categorical toolkit

Read the complete actual body `handbook/parts/p10/categorical-toolkit.tex` and annex `handbook/annex/p10/categorical-toolkit.tex` after they were saved. This added scope covers all six theorem/proof pairs. Source support and attribution pass within the following scope; no mathematical reviewers' conclusions were consulted.

| Actual toolkit proof | Primary support and checked boundary |
| --- | --- |
| `annex:p10.cat.1`: universal-property uniqueness and elementary product/equalizer facts | Riehl Definition 3.1.6 and Proposition 3.1.7, p84, support the unique cone-compatible isomorphism. The additional equalizer monicity, dual epimorphism, and product-arrow calculations are explicitly proved elementary consequences in the annex. The body does not exclude unrelated object automorphisms. |
| `annex:p10.cat.2`: products/equalizers and coproducts/coequalizers | Riehl Theorem 3.5.11, pp112–113, supports exactly these constructions; Remark 3.5.14, p113, supports direct universal-property verification. The actual index objects and arrows have the correct variances. Smallness is stated, the finite-diagram clause requires finitely many objects and arrows, and empty diagrams are included. The Set tuple/quotient descriptions are supplied explicitly. |
| `annex:p10.cat.3`: contravariant Yoneda | Riehl Theorem 2.2.4, pp61–63, applied to the opposite category, and explicit Exercise 2.2.i, p66. The actual body correctly calls its form contravariant and cites both. Its universe convention and represented-family smallness do not assert that every natural-transformation family between arbitrary large-domain functors is small. |
| `annex:p10.cat.4`: hom-bijections and unit/counit triangles | Riehl Definition 4.1.1, p132; Definition 4.2.5 and Theorem 4.2.7, pp140–142. The actual formulas have matching domains/codomains and the proof recovers the original data in both directions. |
| `annex:p10.cat.5`: preservation by adjoints | Riehl Theorem 4.5.2, pp158–159. The actual theorem states preservation of every existing small (co)limit; this is a permissible restriction of the source statement. Neither category is assumed complete or cocomplete, and creation/reflection is not claimed. The proof gives both the cocone and cone arguments. |
| `annex:p10.cat.6`: exponential adjunction and examples | Pitts §3.3, pp22–24, gives evaluation, transposition, and β/η as the exponential universal property used for function types. The source attribution is attached specifically to this function-type semantics. Functoriality, parameter naturality, and the Set/Heyting-poset examples are independently written out in the annex; their detailed presentation is not claimed to be a verbatim Pitts theorem. |

The read-back also confirms that the body distinguishes the author-hosted Riehl second-edition text from the separately cited classical books. The additional source locators requested during integration are now present in the actual body: Theorem 3.5.11, pp112–113, at lines 195–196, and Theorem 4.5.2, pp158–159, at lines 302–303 in the final read-back. No remaining source-identity or locator correction was found in this added toolkit scope. This is a primary-source support check, not a build, render, or whole-manuscript acceptance result.
