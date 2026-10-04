# Priestley and Heyting developments: primary-source packet

Date: 2026-09-06. Bounded research pass using held-source discovery followed by official, institutional, and author-hosted sources. No manuscript changes, tests, builds, renders, or additional agents. Source statements below are paraphrased. Exact original bodies and later expositions are distinguished.

## Original-source standing

**Priestley 1970.** The official Wiley/LMS page verifies H. A. Priestley, *Representation of Distributive Lattices by Means of Ordered Stone Spaces*, Bulletin of the London Mathematical Society 2(2) (1970), 186–190, DOI `10.1112/blms/2.2.186`. Opening its PDF link returned the abstract/metadata page, not the five-page article. No original-body theorem numbers are claimed. Official page: <https://londmathsoc.onlinelibrary.wiley.com/doi/abs/10.1112/blms/2.2.186>.

**Rasiowa–Sikorski 1963.** The registered book is *The Mathematics of Metamathematics*, Helena Rasiowa and Roman Sikorski, PWN, Warsaw, 1963. No legitimate original book body was acquired in this pass. A publisher-hosted contemporary review confirms the publication but is not used as mathematical-body evidence. The later sources below supply actual mathematical content.

**Esakia 1974: original acquired.** L. L. Esakia, *Topological Kripke models*, Doklady Akademii Nauk SSSR 214(2) (1974), 298–301, in Russian, MathNet `dan38051`. Official article page <https://www.mathnet.ru/eng/dan38051>; exact PDF <https://www.mathnet.ru/php/getFT.phtml?jrnid=dan&option_lang=eng&paperid=38051&what=fullt>. Local `tmp/pdfs/p10-priestley-heyting/esakia-1974-topological-kripke-models-ru.pdf`: 4 pages, 593,392 bytes, SHA256 `BEBB9EF67F3824D786FF907BF91A477A834D5B9DEFDDCBD74E4D9272797D0866`.

The original uses perfect topological Kripke models, initially with preorders on nonempty Stone spaces. Definition 1, p298, introduces these models; Definition 2, p298, introduces strongly isotone maps, the order-theoretic lifting condition underlying the modern p-morphism. The full subcategory with partial orders is K_1. Definition 3, p299, gives the residuation definition of a Brouwerian algebra with least element, corresponding to the present bounded Heyting convention. Theorem 3, p300, states dual equivalence for categories K_α and L_α, α=0,1,2; α=1 is the Heyting case. On p301 the clopen upper cones are given implication

\[
a\to b=\{x:R(x)\cap a\subseteq b\},
\]

and an unnumbered representation theorem states that every Brouwerian algebra is represented by such a cone algebra. The four-page original is not the modern prime-filter construction written with Priestley separation. Cite the later thesis for that presentation. Its nonempty-space conventions also require an explicit empty-space extension if the manuscript retains trivial algebras.

Proposed key `Esakia1974`: author `Esakia, L. L.`; title `Topological Kripke Models`; journal `Doklady Akademii Nauk SSSR`; volume 214; number 2; year 1974; pages 298--301; language Russian; URL the MathNet article page. Do not replace these verified Russian publication data with an unverified English-translation page range.

## Acquired later body sources

### Nick Bezhanishvili's 2006 thesis

Proposed key **`Bezhanishvili2006Thesis`**: Nick (title-page full name Nikoloz) Bezhanishvili, *Lattices of intermediate and cylindric modal logics*, doctoral thesis, Universiteit van Amsterdam, ILLC Dissertation Series DS-2006-02, 2006, ISBN 90-5776-147-5. Repository identifies it as the final published version. Defense date 17 March 2006. PDF <https://pure.uva.nl/ws/files/3836071/40465_Bezhanishvili.pdf>.

Local `bezhanishvili-2006-thesis.pdf` in the task source directory: 241 pages, 1,366,379 bytes, SHA256 `B55108F80048B56188160D8108CC271FF747B878CF83AD2B502A4D6E9AC70D4A`. Printed page p corresponds to physical PDF page p+15 (one-based).

Verified locators:

- Definition 2.2.4, p21: Heyting implication satisfies c≤a→b iff a∧c≤b.
- Theorem 2.2.16, p25: IPC theoremhood iff validity in all Heyting algebras. Theorem 2.2.18, p25: each intermediate logic has its corresponding algebraic completeness result. These statements refer to established proofs elsewhere; they are not full proofs in the thesis.
- §2.2.3, p26: the upset algebra of a poset has implication U→V = W\↓(U\V).
- Definition 2.2.20 and following construction, pp26–27: proper prime filters, ordered by inclusion, form the associated intuitionistic frame. Keep `1∈F` explicit in the manuscript's filter definition: the abbreviated printed definition here omits an explicit nonemptiness/1 clause.
- Definition 2.3.1, p28: general intuitionistic frames have an admissible collection of upsets containing ∅,W and closed under finite meets/joins and the relational implication.
- Definition 2.3.2, p28: refined means order separation by admissible upsets; compactness is the finite-intersection property for admissible upsets and their complements; descriptive means refined and compact.
- Theorem 2.3.3, p28: every Heyting algebra is isomorphic to the admissible algebra of its descriptive prime-filter frame. The proof is explicitly a sketch.
- Definition 2.3.20, p34: Priestley separation is x≰y ⇒ some clopen upset contains x and omits y. A Priestley space is a Stone space with a partial order satisfying this axiom. An Esakia space additionally has ↓C clopen for every clopen C, not merely every clopen upset.
- Proposition 2.3.21, p35: closed principal upsets/downsets for Priestley spaces, and an equivalent characterization of Esakia spaces.
- Theorem 2.3.22, p35: a Heyting algebra is represented by all clopen upsets of an Esakia space. The following paragraph identifies Esakia morphisms as continuous p-morphisms of the underlying orders.
- Theorem 2.3.25, p37: Heyting algebras are dually equivalent to descriptive intuitionistic frames and to Esakia spaces; its proof specifies inverse-image maps on prime filters and on admissible upsets.

The thesis explicitly takes topological spaces nonempty (Definition 2.3.17, p33). Do not silently transfer this convention to a manuscript allowing the trivial Heyting algebra. The latter has no proper prime filters and corresponds to the empty Esakia space, whose clopen-upset algebra has one element.

### Tommaso Moraschini's author notes

Proposed key **`Moraschini2023AlgebraLogicNotes`**: Tommaso Moraschini, *The Algebra of Logic*, author lecture notes dated **31 May 2023**, <https://moraschini.github.io/files/teaching/AL.pdf>.

Local `moraschini-algebraic-logic-notes.pdf`: 130 pages, 724,404 bytes, SHA256 `6DD24DD4F56AA028DAF94B0A77EE6B76B88D89F4487BD337BE1DB4C05B526547`. Printed page p corresponds to physical page p+4.

The **Prime Filter Theorem on p41** states that each filter of a bounded distributive lattice is an intersection of prime filters and supplies a proof via the algebraic lattice of filters. **Corollary 2.14, p41**, states a≰b ⇒ there is a prime filter containing a and omitting b. This is actual body evidence for separation, independently of unavailable Rasiowa–Sikorski pages. The PDF extraction sometimes loses the stroke of ≰; the proof and web rendering establish the negative order hypothesis.

**Example 2.25, p47**, proves the upset-algebra implication formula and its residuation law. **Theorem 2.26, pp47–48**, proves the prime-filter representation of a Heyting algebra as a subalgebra of the full upset algebra. It includes the exact implication-witness step:

\[
a\to b\notin F\quad\Longleftrightarrow\quad
\exists G\supseteq F\ (G\text{ prime},\ a\in G,\ b\notin G).
\]

For the nontrivial direction, the filter generated by F∪{a} cannot contain b: otherwise some c∈F has c∧a≤b, giving c≤a→b and hence a→b∈F. The Prime Filter Theorem extends this generated filter to a prime filter omitting b. The converse is filter closure and a∧(a→b)≤b. This proof supplies the precise clause required by the intuitionistic Kripke truth induction.

### Further explicit modern functors

Gianluca Grilletti and Davide Emilio Quadrellaro, *Esakia duals of regular Heyting algebras*, **arXiv:2303.11246v2, 25 August 2023**, <https://arxiv.org/pdf/2303.11246v2>. This is the inspected arXiv version, not an assertion that its numbering equals the final Springer publication with DOI10.1007/s00012-023-00833-5.

Local `grilletti-quadrellaro-2023-esakia-v2.pdf`: 27 pages, 377,666 bytes, SHA256 `4612FE9554DA564BC30F5A60AF6407853CE5CE56F45164682134D7F9708D21CD`.

Definitions 1–2, p3, give Esakia spaces and continuous order-preserving maps satisfying the back condition

\[
f(x)\leq y\ \Longrightarrow\ \exists z\geq x\ f(z)=y.
\]

The prime-filter topology, order by inclusion, and subbasis â and its complements are on p3. Page 4 defines clopen-upset implication as the complement of ↓(U\V); Theorem 3 gives both object reconstructions; the following paragraphs give both inverse-image arrow maps. Use their displayed maps rather than the final functor-letter labels, which appear interchanged: prime filters send algebras to spaces, while clopen upsets send spaces to algebras.

### Priestley's own later account

Proposed key **`Priestley2019Slides`**: Hilary Priestley, *Snapshots of Duality Theory*, Mathematical Institute, University of Oxford, talk dated **21 June 2019**, **web version 5 July 2019**, as explicitly printed on slide 1. Author-hosted <https://people.maths.ox.ac.uk/hap/TACLslides-web0507.pdf>. Local `priestley-2019-duality-slides.pdf`: 58 pages, 1,296,040 bytes, SHA256 `E47BED7C8C9D5F1D1D64C8F6D8B71B3E8E12C7438E254B58D9FBDB4321DD48B2`.

Physical slides 17–20 describe hom-functors, evaluation maps, and the full duality between bounded distributive lattices and Priestley spaces. Slide 53 explicitly warns that merely equipping a Stone space with a closed partial order does not suffice: Priestley separation is essential. This is an author exposition, not the original 1970 article or a full replacement proof of it.

## Exact constructions for the manuscript

For a bounded distributive lattice D, take its proper prime filters ordered by inclusion, with the topology generated by â={F:a∈F} and their complements. The representation is a↦â into the lattice of all clopen upsets. The inverse space reconstruction sends a point x to the prime filter of clopen upsets containing x. For morphisms, bounded lattice homomorphisms act by inverse image on prime filters, and continuous monotone Priestley maps act by inverse image on clopen upsets. The source-grounded modern definitions above fix the directions and topology; the manuscript should supply the full compactness and surjectivity proofs if those are being claimed as proved.

For a Heyting algebra H, the implication-witness lemma gives

\[
\widehat{a\to b}=X_H\setminus\downarrow(\widehat a\setminus\widehat b).
\]

Thus the prime-filter representation preserves implication. On an Esakia space, down-closure of every clopen makes this expression clopen, while its complement-of-downset form makes it an upset. The residuation law identifies it as the Heyting implication. Heyting homomorphisms dualize to continuous p-morphisms, rather than merely continuous monotone maps; their back condition is what preserves the universal quantification over future points in implication.

IPC algebraic completeness plus the implication-preserving prime-filter embedding gives Kripke completeness of IPC by the usual structural truth induction. This does not assert that every intermediate logic is complete for its underlying ordinary Kripke frames: the thesis expressly distinguishes algebraic/descriptive completeness from possible ordinary-frame incompleteness. General descriptive valuations range over clopen upsets; unrestricted Kripke valuations range over all upsets.

## The Rasiowa–Sikorski naming issue

**Prime-filter separation should not simply be named the Rasiowa–Sikorski lemma.** Add the actual countable dense-set result separately if N-d-008 requires that named lemma.

An author-hosted primary exposition states it explicitly: Krzysztof Ciesielski, *Set Theory for the Working Mathematician*, **Theorem 8.1.2, printed p132**, <https://community.wvu.edu/~kciesiel/ProfessionalStuff/Other/ElectronicReprints/B2IntSetThe.pdf>. It states: given a poset P, a point p∈P, and a countable family of dense subsets of P, there is a filter containing p and meeting every member of that family. Dense means every condition has a stronger condition in the set; a forcing filter is upward closed and downward directed. This page was checked through the author's public PDF rendering; that book was not downloaded in this pass.

For an arbitrary poset, the usual descending-sequence construction invokes dependent choices; in ZFC this is immediate. For an explicitly enumerated countable poset one can choose the least available witness at each step and obtain the corresponding result in ZF. Keep this separate from a global distributive prime-filter theorem.

Bibliography metadata for **`Ciesielski1997`** is verified both on the [author's book page](https://community.wvu.edu/~kciesiel/ProfessionalStuff/STbook.html) and the [Cambridge book page](https://www.cambridge.org/core/books/set-theory-for-the-working-mathematician/265BF1E67363492A762DF85B136DA8B7): Krzysztof Ciesielski, *Set Theory for the Working Mathematician*, London Mathematical Society Student Texts **39**, Cambridge University Press, **1997**. Hardback ISBN 978-0-521-59441-7; paperback ISBN 978-0-521-59465-3. DOI `10.1017/CBO9781139173131` identifies the electronic book, whose Cambridge online publication date is 5 June 2012; the print year remains 1997. The public author PDF has 243 physical pages and begins at printed preliminary page v, omitting the title/copyright leaves; metadata therefore comes from those separately identified author/publisher pages, not an invented front-matter reading.

There is also a named Boolean formulation: Kozen, Mardare, and Panangaden, *Strong Completeness for Markovian Logics*, Theorem 3, p4, <https://www.macs.hw.ac.uk/~rm4023/papers/StrongCompleteness-MFCS.pdf>, gives an ultrafilter containing a specified nonzero element and respecting a countable family of subsets whose meets exist. This is an additional infinitary preservation condition, not ordinary prime-filter separation. It corroborates the need to avoid the current conflated attribution.
