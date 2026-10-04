# Topological model theory: authoring and source record

This record concerns planned **38.1–38.3**. It is an authoring/provenance note, not an independent review or admission record. No coverage ledger, original source allocation, driver, canonical bibliography or canonical symbol registry was changed. The saved body supplies two identified topological-language presentations and actual proofs; it does not substitute continuous metric model theory for the required topological structures.

## Exact original duties and current-reader context

Read the complete finite allocation `ED26-SRC-049-0015` from `spec/coverage/edition-2026/sources-037-068/src049-content-units.jsonl`, and its matching completion-queue record. Its original source is M. Ziegler, Chapter XV, *Topological Model Theory*, in Barwise–Feferman, *Model-Theoretic Logics*, first edition1985; the recorded publisher presentation is the Cambridge/ASL reissue copyright2016/release2017, DOI `10.1017/9781316717158.022`. Its components remain:

- C001, §1 Topological Structures, pp.557–560.
- C002, §2 The Interpolation Theorem, pp.560–565.
- C003, §3 Preservation and Definability, pp.565–568.
- C004, §4 infinitary topological logic, pp.568–570 (the preview's extracted title is typographically damaged; no reconstructed glyph is invented).
- C005, §5 Some Applications, pp.570–575.
- C006, §6 Other Structures, pp.575–578.

The allocation and source-version conditions were preserved, not narrowed to the work below. [The Cambridge chapter index](https://www.cambridge.org/core/books/abs/modeltheoretic-logics/topological-model-theory/A8E5C2117D74C1D454BFF81C15CB1B9D) supplies metadata/access controls, not a held full chapter. The exact original Project Euclid chapter locator `https://projecteuclid.org/euclid.pl/1235417281` returned an Incapsula challenge in the normal HTTPS response. No challenge, login, TLS or access-control bypass was attempted. ResearchGate's chapter page has no full text, so its abstract is not credited as reading §1–§3. Flum–Ziegler's1980 LNM769 publisher page is a subscription preview. Both observed normal AMS paths for Sgro's1980 interior-operator article returned403 and supplied no readable body. No original interpolation proof was obtained.

Read actual current `preservation-abstract-logic.tex` lines179–369, its `annex:p3.abstract.5` proof interval, the complete272-line body `presentations/n-a-004-02.tex`, and the indicated first106lines of its annex. These supply ordinary first-order preservation/Craig/Beth and topology on codes, not the topological-language interpolation proof. Read the actual compact-topological atomic-solution treatment in `resplendence-and-atomic-compactness.tex` lines176–242: its compact carrier and closed basic relations are a different genuine use of topological structures. That existing result was not overwritten or misreported as absent. The new languages and quantification over opens are not supplied by its atomic-compactness argument.

## Primary bodies acquired and read

1. **Milan Z. Grulović and Miloš S. Kurilić, “The Feferman–Vaught theorem for reduced ideal-products,” Novi Sad J. Math.31(2) (2001),1–8.** Acquired the full8-page journal PDF from its institutional [journal body](https://sites.dmi.uns.ac.rs/nsjom/Papers/31_2/nsjom_31_2_001_008.pdf). Held at `source/references/p03-topological-models/grulovic-kurilic-2001-journal.pdf`,194,723bytes, SHA-256 `a80b7b1b3c958c7952ea7f3b511ba71a3948e9c9066c9c2fe7392369356943a2`. Read every page, including received25November1995 on p.8; publication year and received date are not conflated. The construction uses an idealLambda for topology support and filterPsi for point equivalence, a Boolean quotient with distinguished support ideal, and a monotone/polarity-preserving local reduction. The complete guard proof is pp.3–6; the article omits atomic, negation, conjunction and individual-existential cases. The new annex supplies these. Its externally cited separation-axiom criterion `(LambdaPsi)` and cited1992/1994 results are not reconstructed or newly credited.
2. **Balder ten Cate, David Gabelaia and Dmitry Sustretov, “Modal Languages for Topology: Expressivity and Definability,” institutional author draft dated10October2006,48pages.** Acquired via the University of Hamburg seminar [actual draft](https://www.math.uni-hamburg.de/home/loewe/2006-07-II/files/tengasus.pdf). Held at `source/references/p03-topological-models/ten-cate-gabelaia-sustretov-2006-institutional.pdf`,386,120bytes, SHA-256 `ae254264ed5198f40a3608bfe3ce2a04fe20af9d8ab8bcf2919e2aeadd32ced9`. Read pp.1–12 completely: topological/basoid definitions, unrestrictedL2 and restrictedLt, Ext/Union/Empty/Bas, basis invariance, compactness/countable-basis claims, separation formulas, and standard translation. The remaining36pages were not read or reconstructed. The2009 APAL article (DOI `10.1016/j.apal.2008.11.001`,159(1–2),146–170) is metadata-identified only, not equated with this draft. An arXivv1 PDF request returned406; no v1 body was captured or title-matched to the institutional draft.

Standard HTTPS downloads with default certificate verification were used. No request to contact authors, spend money, change accounts, or publish was made.

## Mathematical content saved

Owned body: `handbook/parts/p03/topological-model-theory.tex`.
Reciprocal proofs: `handbook/annex/p03/topological-model-theory.tex`.
Raw notation intake: `handbook/registry/symbols-intake-p03-topological-models.csv`.
Bibliography intake: `handbook/bib/intake-p03-topological-models.bib`.

Nine pairs use `thm:p03-topological-` / `annex:p03-topological-`:

1. `polarity`: actual membership-polarity induction under changing free subset parameters.
2. `basis`: topology generation and both guarded-quantifier directions of basis invariance, with an explicit fullL2 separating model.
3. `compactness-ls`: basoid reconstruction from the four first-order axioms, ordinary first-order compactness/LS transfer, and countable basis versus countable full topology.
4. `property-formulas`: T0,T1,T2,discrete,least-neighborhood/Alexandroff formulas and full semantic proofs; connectedness in unrestrictedL2 is distinct from the guarded fragment.
5. `translation-homeomorphism`: full standard-translation induction and two-sorted homeomorphism satisfaction induction, with an ordinary-isomorphism/topology counterexample.
6. `rip-structure`: point/function/relation quotient well-definedness, open quotient map, actual box basis, canonical coordinate membership, product-versus-box example, and Boolean quotient/image ideal well-definedness.
7. `carrier-substitution`: whole-carrier substitution for free memberships, including binding and quantifier cases.
8. `fv`: all recursive clauses of increasing Boolean reduction, simultaneous free-variable/polarity invariants, individual witnesses on a common large agreement set, and open witnesses supported inLambda; native+,dot,prime,lambda and whole-carrier eta_j roles retained.
9. `transfer`: factorwiseLt-equivalence preservation, full ultrafilter induction including the guarded open step, generated topological ultraproducts, and diagonal formula transfer.

The source2006 correspondence signature has one predicate per propositional letter; source2001 has an arbitrary finitary point signature and guards by point terms. These are separate sections with explicit generalization of the same membership proofs. No continuity of operations/relations, interior-operator n-ary product language, strongL2 interpolation, or arbitrary continuous-map preservation is silently imported.

## Direct corrections and exact boundaries

The new active definitions/formulas are correct themselves. These notes record evidence and preserve source bytes; readers are not told to repair an earlier false book claim.

- **Open equality/polarity:** Draft2006 Definition10 includes all atomicL2 formulas and tests positivity by negation parity. Literal primitiveU=V would make `forall U(a in U -> U=V)` positive-guarded. WithV={a}, it is true on the two-point basis `{empty,{a},{b}}` but false in its generated discrete topology (U={a,b}). This contradicts basis invariance. The new membership presentation expands open equality extensionally before polarity testing; it then has mixed membership polarity, so that guard is excluded. The annex proves the corrected fragment, not the literal erroneous syntax or the unheld full fragment-characterization theorem.
- **Alexandroff direction:** Draft2006 Table1 p.12 has `y in V -> y in U` after existentialU/universalV. The whole carrier witnessesU in every space. The new formula has `y in U -> y in V`, asserting a least neighborhood. The annex proves equivalence to arbitrary-intersection closure; the usual real line separates it from the reverse implication.
- **Empty box parameters:** Source2001 states its theorem for actual basic setsU and local coordinatesU_i while omitting the atomic case. The new semantics explicitly uses coordinate projections of the actual box; an empty box has all empty projections. Noncanonical written factors can give a false atomic parameter: empty coordinate-zero/full others modulo a cofinite filter yields a large local membership set despite an empty image. The new atomic proof removes this ambiguity; nonempty witness boxes retain the supported-coordinate construction.
- **Predicate ultraproduct notation:** Draft2006 Definition11 p.9 writes predicate extensions as quotient images of Cartesian products. Such a product is empty if one factor extension is empty, even when its local truth set is ultrafilter-large. The new active interpretation uses filter-large local relation truth, with the actual atomic proof. It is not a source-exact literal claim for that shorthand.
- **Empty basis convention:** Draft2006 basoids includeempty; the2001 ideal-box basis need not (Lambda={empty}). The reader explicitly adjoinsempty when using the former convention and proves guarded quantification unchanged. Those variants are not silently identified.

These repairs do not close all source2006 content. UnrestrictedL2 model-theoretic failures/hardness use its unread AppendixA; the full base-invariant-fragment characterization, saturation result, connectedness nondefinability, and later modal preservation/definability theorems were not reconstructed. No completion credit for these omitted components is claimed.

## Integration and remaining duties

Root should route the chapter after P3 structure/ordinary-preservation prerequisites and before later Borel/measure/category material, with its matching annex. Root owns canonical integration and source/fulfillment updates. The bibliography has two new version-specific records. Notation records distinguish topology sigma/tau from Boolean sigma/tau, point/Boolean brackets, support idealLambda/filterPsi, and source congruenceequiv/elementary equivalence. No shared macro or calculus sheet was added.

**38.1:** substantive topological carriers, sorts, restricted syntax, satisfaction conventions, basis presentations and constructed model-theory results are supplied. This supports partial authoring when routed, not discharge of unheld ZieglerC001.

**38.2:** required topological interpolation and its full source proof remain unsupplied. Exact dependency is Ziegler§2 pp.560–565 and/or a separately identified fully held original interpolation treatment with its language, consistency/amalgamation construction and proof. Ordinary Craig/Beth and this basis-invariance argument are not credited as topological interpolation. Sgro1980's weak-model axioms and Robinson joint-consistency proof are not held; its abstract is insufficient.

**38.3:** source-specific composition and theory-preservation supply a genuine topological preservation application. Original Ziegler§3 pp.565–568 and its exact definability/preservation operations remain owed. No general syntactic preservation characterization or full definability theorem is claimed.

C004–C006 and whole-source apparatus remain untouched/open. Held primary bodies do not waive first-edition/reissue identities, source examples/exercises, original proof dependencies or independent admission.

The45-minute block began approximately18:19UTC; the15-minute checkpoint followed saving the first five pairs. Saved reader/annex text was read and concrete polarity/inclusion/empty-box/ultraproduct cases checked by direct mathematical reasoning. No reviewer, software test, checker, build, manuscript render, driver/canonical merge or ledger edit was performed.
