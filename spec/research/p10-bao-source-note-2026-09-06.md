# Boolean algebras with operators: Venema source packet

Date: 2026-09-06. Bounded primary-source reading for the Part 10 general finitary representation. Used the research skill, located the existing acquisition record first, and reused the held source. No acquisition, manuscript edits, tests, builds, renders, or additional agents.

## Version and existing holdings

Existing record: `spec/research/acquisition-src-025.md`, particularly lines 278, 316–323, and source locator 236 at line 793. It records the complete STOQ-hosted Venema file, not merely the editor's three-page chapter introduction.

- Held PDF: `tmp/src025/venema-chapter6.pdf`.
- Held extraction: `tmp/src025/venema-chapter6.txt`.
- Recorded source URL: <https://www.stoqatpul.org/lat/materials/ontformale/modal_logic_coalgebra.pdf>.
- Author/title: Yde Venema, *Algebras and Coalgebras*.
- Verified extent: 86 PDF pages; 834,619 bytes.
- SHA-256: `7DED040A23C0AAA632C29F8166101FE309C01C0E29A01F01D90281C01690B49A`.
- The body explicitly identifies itself as a preprint dated **19 October 2005**. Its footnote says it was written for the forthcoming *Handbook of Modal Logic*, and unresolved `HBML` cross-references remain.
- The held copy also contains a first-page bibliographic header identifying the 2007 published chapter, pp331–426. That does not turn its 86-page preprint body into the 96-page published manifestation.
- PDF creation metadata: `D:20051019121600Z`; modification metadata: `D:20121122132644+01'00'`; creator TeX; producer pdfTeX-0.13d. The modification timestamp is not evidence of a revised 2012 mathematical edition.
- Published-chapter metadata recorded in the acquisition note: *Handbook of Modal Logic*, Studies in Logic and Practical Reasoning 3, editors Blackburn, van Benthem, Wolter, 2007, pp331–426; DOI `10.1016/S1570-2464(07)80009-7`.

**All page locators below refer to the held 2005 preprint.** Its printed local page numbers agree with one-based PDF pages. Do not add 330 to obtain supposed verified published locators; that correspondence has not been checked. Cite the theorem numbers with the preprint qualification when using this held text as the exact source.

## Exact definitions and theorem scope

| Item | Held-source locator | Mathematical content |
| --- | --- | --- |
| Finitary modal signature | §2, p4 | An arbitrary fixed similarity type τ has an arity function into ω. The chapter normally uses a fixed countably infinite variable set. It explicitly warns that proofs will often be given only for one unary diamond. |
| Frames | Definition 2.1, p4 | A τ-frame has a nonempty carrier and one (n+1)-ary relation for each n-ary modal symbol. |
| Complex operators | Definition 3.5, p8; Proposition 3.7, p8 | For R⊆S^(n+1), the operator sends (A_1,…,A_n) to the states with an R-successor tuple in their Cartesian product. Formula interpretation is the homomorphic term evaluation in this powerset expansion. |
| Algebraization | Definition 3.8, p8 | Theoremhood corresponds to validity of φ≈1; validity of φ≈ψ corresponds to theoremhood of φ↔ψ. The source separately distinguishes this theorem-level presentation from general consequence relations. |
| Operators/BAOs | **Definition 3.11, p9** | An n-ary operator is normal and additive in each coordinate. A τ-BAO is a Boolean algebra expanded with such operators; a modal algebra is the single-unary-operator case. |
| Algebraic completeness | **Theorem 3.13, p10** | BAOτ(Γ), the BAOs validating γ≈1 for γ∈Γ, algebraizes the normal modal logic Kτ.Γ. It also states the analogous expanded-algebra and monotone-algebra results. |
| Lindenbaum algebra | Definitions 3.14/3.16 and Proposition 3.15, p10; Theorem 3.17, pp10–11; Theorem 3.18, p11 | Provable equivalence is a congruence; its quotient validates an identity exactly when the corresponding equivalence is provable and is the relevant free algebra. |
| Perfect BAOs | Definition 5.1, p17 | Complete and atomic Boolean reduct, with operators preserving all joins in each coordinate. Finite additivity alone is not complete additivity. |
| Atom structure | Definition 5.2, p17 | For an atomic BAO, Q_f(p_0,p_1,…,p_n) iff p_0≤f(p_1,…,p_n). |
| Exact atomic representation | Proposition 5.3, pp17–18 | The canonical atom map embeds the atomic BAO into the complex algebra of its atom structure when the operators are complete; it is onto in the perfect case. The proposition states A≅Cm(At(A)) iff A is perfect. |
| Ultrafilter extension | Theorem 5.11, p19 | Every proper Boolean filter extends to an ultrafilter; the source proves this with Zorn's lemma. |
| General n-ary canonical relation | **Definition 5.12, p19** | R_f(u,u_1,…,u_n) iff f(a_1,…,a_n)∈u for every tuple with a_i∈u_i. The frame on all ultrafilters with these relations is the canonical structure A•. |
| Jónsson–Tarski representation | **Theorem 5.15, p20** | For an arbitrary τ-BAO A, a↦â={u:a∈u} embeds A into Cm(A•). **The stated theorem is general finitary; the displayed proof of preservation of the extra operations treats only one unary diamond.** |
| Canonical extension | **Definition 5.16, p21** | Aσ=(A•)+=Cm(A•), also called the canonical embedding algebra or perfect extension. |
| General frames | **Definition 5.24, p22** | A relational frame together with a Boolean algebra of admissible subsets closed under all complex operators. Its associated algebra has precisely the admissible subsets as carrier. |
| Descriptive frames | **Definition 5.25, p22** | Tightness plus differentiation gives refinement; refinement plus compactness gives descriptiveness. Compactness and differentiation of the underlying field are defined in Definition 5.20, p21. |
| General-frame duality | Definition 5.27 and **Theorem 5.28, p23** | τ-BAOs and descriptive general τ-frames are dually equivalent, with continuous bounded morphisms on the frame side. The proof is a sketch and leaves details to the reader. |
| Logics and varieties | Theorem 6.3, p28 | The logic/BAO constructions give the dual correspondence between normal modal logics and varieties of τ-BAOs. |
| Kripke completeness boundary | **Theorem 6.4, p29** | A normal modal logic is Kripke complete iff its BAO variety is generated by its perfect members. |
| Canonicity | **Definitions 6.9–6.10 and Theorem 6.11, p31** | A class is canonical when closed under A↦Aσ. An equation is canonical when its validity is preserved by this operation. Logical/algebraic canonicity are identified using logical canonicity quantified over **all variable sets X**. |
| Canonicity implies completeness | **Theorem 6.12, p31** | A canonical BAO variety is Kripke complete. |

Two short source excerpts pin down the operator and proof scopes:

> “normal and additive in each of its coordinates” — Definition 3.11, p9.

> “we restrict ourselves to the basic modal similarity type” — proof of Theorem 5.15, p20.

The remaining source content here is paraphrased or expressed mathematically.

## Clauses for the general finitary manuscript theorem

For every n>0 and coordinate i, the required laws are

\[
f(a_1,\ldots,0,\ldots,a_n)=0,
\]
\[
f(a_1,\ldots,b\vee c,\ldots,a_n)
=f(a_1,\ldots,b,\ldots,a_n)\vee f(a_1,\ldots,c,\ldots,a_n).
\]

They imply monotonicity in each coordinate. The canonical relation of Definition 5.12 gives immediately

\[
\langle R_f\rangle(\widehat a_1,\ldots,\widehat a_n)
\subseteq\widehat{f(a_1,\ldots,a_n)}.
\]

The reverse inclusion is the n-ary witness lemma: if f(a_1,…,a_n)∈u, find ultrafilters u_i containing a_i such that every tuple chosen from the u_i has its f-value in u. The source states the general representation but does not supply that general witness proof. The manuscript should provide it explicitly.

At arity zero, coordinate normality/additivity imposes no condition: f() is an arbitrary designated Boolean element, not necessarily 0. The definition reduces to R_f(u) iff f()∈u. The complex nullary operator is the subset defined by that unary relation, so representation of the constant is immediate. No ultrafilter successor tuple must be chosen in this case.

For a trivial BAO, there are no ultrafilters. The source's frame definition requires nonempty carriers, leaving this boundary implicit in the unqualified representation statement. To retain the manuscript's trivial-algebra convention, explicitly allow the empty canonical frame and its one-element powerset algebra. Every relation on it is empty; every operator on the one-element algebra has the sole possible value. The representation remains correct with that convention.

The atom structure and ultrafilter structure must not be conflated: arbitrary BAOs may have no atoms, and atomicity alone does not make their operators completely additive. The perfect-algebra result and the general ultrafilter representation have different hypotheses.

## A BPIT proof route for the missing n-ary witness detail

This paragraph supplies a derivation, not a claim that it is printed in Venema's unary proof. Start with the principal filters F_i above a_i. Normality makes each a_i nonzero, and monotonicity gives f(b_1,…,b_n)∈u for every b_i∈F_i. Maintain this property while extending one filter at a time.

With all filters except the ith fixed, put

\[
I_i=\{b:\exists(b_j\in F_j)_{j\ne i}\;
 f(b_1,\ldots,b_{i-1},b,b_{i+1},\ldots,b_n)\notin u\}.
\]

This is an ideal. Normality gives 0∈I_i; monotonicity gives downward closure. If b,c have witnessing tuples, replace their other coordinates by the componentwise meets of those tuples. Monotonicity keeps both values outside u; additivity and ultrafilter primeness keep the value at b∨c outside u. The maintained property gives F_i∩I_i=∅.

The filter generated by F_i and {¬d:d∈I_i} is proper: otherwise some f∈F_i is below a finite join of elements of I_i, placing f in that ideal. BPIT extends this proper filter to an ultrafilter u_i containing F_i and disjoint from I_i. By the definition of I_i, replacing F_i by u_i preserves the maintained property. After the finite number n of coordinates, the desired ultrafilter tuple exists. This proof uses BPIT and finite choices; a Zorn argument on whole filter tuples is unnecessary.

## General frames and the canonicity boundary

The representing general frame has carrier Uf(A), relations R_f, and admissible algebra {â:a∈A}. Representation proves closure of this admissible algebra under every complex operator. General-frame valuations range over these admissible subsets; structural induction therefore evaluates formulas in that algebra. This is distinct from allowing every subset of Uf(A) as a valuation, which evaluates in Aσ. Definition 5.24 and the paragraph after Theorem 5.28 support this account; the source leaves the full semantic algebraization details there to the reader.

Differentiation means admissible subsets separate points. Compactness means every admissible family with the finite-intersection property has nonempty intersection. Tightness means that any tuple outside R_f can be witnessed by admissible neighborhoods A_i of its successor coordinates such that the first point is outside the complex image of (A_1,…,A_n). For unary operators, Remark 5.26, pp22–23, reformulates tightness as closed successor sets. Use the tuple formulation for general n-ary operators; do not replace it by an unexplained unary condition.

Theorem 3.13 establishes algebraic completeness for every normal logic through its Lindenbaum algebra. It does **not** infer Kripke completeness from the representation embedding. An identity true in A need not be true throughout a superalgebra Aσ: the latter contains more possible valuations. Canonical axioms or closure of the variety under canonical extensions are additional hypotheses. Theorem 6.12 then supplies the completeness implication.

The source's Theorem 6.11 uses Definition 6.10 with all variable sets, not merely the fixed countably infinite variable alphabet used elsewhere in the chapter. If citing that equivalence, retain this qualification. The preprint additionally comments on the then-open countable-variable issue; this note makes no claim about that problem's present status.

For an intrinsic alternative to Definition 5.16, §7.2, pp38–39, defines a canonical extension of a Boolean algebra as a dense and compact completion (Definition 7.1) and states existence/uniqueness up to an isomorphism fixing the embedded algebra (Theorem 7.2). Section 7.1, p37, explains how extending operators recovers the earlier double-dual construction. This is not an assertion that canonical extension preserves all pre-existing infinite joins or is the MacNeille completion; the source explicitly distinguishes regular completions and later discusses the MacNeille construction separately.

## Small preprint slips to avoid copying

The first inclusion label in the proof of Theorem 5.15, p20, is reversed relative to the immediately preceding argument: that argument starts in the relational complex image and concludes membership in the represented f-value. Use the correct inclusion displayed above. Also the inverse-image definitions around Definition 5.17 and the morphism paragraph before Theorem 5.28 occasionally print u where the input is u′; the correctly typed map is η⁻¹[u′]. These do not affect the theorem statements but should not be propagated into the manuscript.
