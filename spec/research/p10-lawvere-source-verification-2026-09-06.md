# Source verification of the Lawvere extensions

Date: 2026-09-06. Bounded source-only check, using the research skill and the held primary-source packet `spec/research/p10-lawvere-theories-source-note-2026-09-06.md`. Read the complete actual bodies and annexes:

- `handbook/parts/p10/lawvere-presentations.tex`, lines 1–151;
- `handbook/annex/p10/lawvere-presentations.tex`, lines 1–277;
- `handbook/parts/p10/lawvere-free-algebras.tex`, lines 1–180;
- `handbook/annex/p10/lawvere-free-algebras.tex`, lines 1–282.

Also checked the three cited bibliography entries in `handbook/bib/handbook.bib`. No other mathematical review conclusions were consulted. This is a source-support and attribution result, not an independent full mathematical acceptance of the five new proofs. No manuscript/shared files were edited and no tests, builds, or renders were performed.

## Result

**Source-scope pass. No necessary source-version, locator, or attribution correction was found.** The actual wording distinguishes the results present in the sources from the explicit equation basis, quotient arguments, comparison maps, and boundary examples proved locally.

## Named presentations

At body lines 100–112, the named signature and evaluation quotient are attributed to **Adámek–Rosický–Vitale, Definition 13.5 and Proposition 13.7 p123; Remark 13.8 p124**, in the **February 1, 2010 author draft**. These exact source passages name arrows `n→1` as operation symbols, provide the free-theory universal property, and recover an abstract theory as the quotient by the evaluation kernel.

The actual body then says that the present proof identifies that kernel using its **two explicit equation families**. This accurately marks the projection/substitution basis in body lines 16–60 and its reduction proof in annex lines 78–103 as a local elaboration. It does not claim that ARV prints this exact two-family basis or these same calculations. The explicit nullary family, the inverse on tuple arrows, and the treatment of nonfaithful structural maps likewise appear as supplied proof details.

The supporting Lawvere references at body lines 106–112 are accurate: **1963 thesis Chapter II §2, reprint pp69–73**, for presentations/substitution, and **Chapter II §1, reprint pp61–63**, for the coproduct orientation. The sentence naming the opposite-category translation prevents the source's `1→n` operations from being silently cited as its literal product-oriented definition.

The morphism definition at body lines 114–127 is supported by **ARV Definition 11.3 and Remark 11.4 p98**: identity on objects, commutation with the structural finite-set functor, and the consequent preservation of selected products. The model-restriction theorem and its annex proof then work out precomposition, all natural-transformation components, contravariant composition, and naturality of the named translation directly. No claim that this entire expanded proof is verbatim from the cited definition is made. Lawvere's III§1 pp75 onward also supports restriction of models along theory morphisms in the opposite orientation already explained by the core.

## Representable and arbitrary free models

The finite-free source paragraph at body lines 57–63 uses correct locators:

- **Lawvere's 1963 thesis, Chapter III §1, reprint pp74–75**, and the separate **1968 article §1 p110**;
- **ARV Remark 11.21 and Corollary 11.22, draft pp102–103**;
- **Pitts1995Draft, Remark 4.2.3 p33**.

These passages support representables as finite free models, their free generators, and the opposite-theory description. The new theorem's isomorphism with a category of *indexed chosen* representables is transparently more explicit than a statement of equivalence with the full category of all finite free models. The annex supplies the elementary Yoneda calculation establishing this indexed version and fixes the correspondence of generators before asserting uniqueness. This is an accurately presented local elaboration, not an unsupported attribution of a stronger unqualified uniqueness claim.

For arbitrary generators, body lines 130–134 cite **ARV §13 pp121–125** for terms/presentations and **Remark 11.21 pp102–103** for free models on every set. These are the inspected draft's actual locators. The construction using the common semantic kernel on the term set, the proof that its quotient satisfies E by choosing only finite representative families, and the separate empty-term case are developed in annex `annex:p10.lawvere-free.2`. The source paragraph expressly announces those local verifications. It does not attribute that exact proof organization to ARV. The subsequent explicit singleton-power comparisons, naturality in generators and models, and triangle checks are also supplied as local proof details.

## Carrier conventions and examples

Body lines 68–89 explicitly switch to all-carrier algebras for this construction while retaining the earlier section's nonempty hypotheses. This matches the source packet: ARV and Pitts permit empty carriers in these Set-model constructions. The declared finite equation contexts and zero powers are retained.

The exact empty-model criterion, uniqueness statement, and zero-generator boundary in body lines 139–163 are proved locally in `annex:p10.lawvere-free.3`; no incorrect claim that these exact theorem statements were copied from a numbered source theorem appears. They are consistent with the source conventions and their representable-initial-object construction.

At body lines 174–176, Lawvere **1963 thesis Chapter II §1, reprint p64**, is cited for the distinction between expressible zero-ary operations and definable constants. This is precisely the distinction in that source. The empty-set, left-zero-semigroup, and unary-d examples are separately explained and proved in the manuscript. The wording uses them to illustrate the source distinction; it does not claim that Lawvere gives these three exact examples on p64.

## Bibliography and version consistency

The live bibliography entries retain the correct manifestations:

- `Lawvere2004FunctorialReprint`, `handbook/bib/handbook.bib:6513`: Reprints in Theory and Applications of Categories 5 (2004), pp1–121; note identifies the 1963 thesis, 1968 article, and commentary; publisher PDF URL is the acquired source.
- `AdamekRosickyVitale2010Draft`, `handbook/bib/handbook.bib:6527`: February 1, 2010 unpublished author draft; direct Vitale institutional PDF URL; note identifies draft pp1–238 and distinguishes the 2011 book.
- `Pitts1995Draft`, `handbook/bib/handbook.bib:6493`: May 18, 1995 Cambridge report UCAM-CL-TR-367, DOI `10.48456/tr-367`; author-manuscript pagination pp1–94. It is not presented as the final Pitts2000 chapter.

No source acquisition was required for this recheck; the verified bodies are already held. No new unsupported source claim was identified in either extension.
