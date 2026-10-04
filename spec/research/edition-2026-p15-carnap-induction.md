# P15 Carnap logical probability and induction: original-source intake

Authoring block: 2026-10-02 local / 2026-10-03 UTC. Authoring assessment only; no independent correctness review, build, tests, or manuscript rendering. The source-page PNGs below are reading artifacts of acquired source pages, not handbook output.

## Allocations kept separate

- Section 164.6, ED26-REQ-N-x-008-01: Carnap's **1950 first edition**, *Logical Foundations of Probability*, University of Chicago Press, xvii + 607 pages. The selected presentation includes explication/two probabilities, language/state/structure descriptions, regular and symmetric confirmation, methods and calculations, and philosophical conditions and limitations. N-x-008-C01, N-x-008-S01-PRESENTATION, N-x-008-S01-PROOF, N-x-008-S01-BRIDGE remain distinct content/presentation/proof/bridge duties. Neither 1952 *The Continuum of Inductive Methods* nor 1962's second edition is a substitute.
- ED26-SRC-063-1008: S. L. (Sandy L.) Zabell, *Carnap and the Logic of Inductive Inference*, HHL10 *Inductive Logic*, chapter 8, pp.265–309, publisher allocation Elsevier 2011, DOI 10.1016/B978-0-444-52936-7.50008-2. Its full historical argument and formal dependencies are a separate source duty, not closed by the original-source treatment.

## Acquisition and identity

Carnap legitimate institutional archive route:

- [Archive item](https://archive.org/details/logicalfoundatio00carn_0).
- [Direct exposed PDF download](https://archive.org/download/logicalfoundatio00carn_0/logicalfoundatio00carn_0.pdf).
- Archive OCR, scandata and metadata downloaded from the same item to `source/references/p15-carnap-induction/`.
- The title/copyright body identifies publication and copyright 1950, Chicago; the printed contents end with bibliography pp.583–598 and index pp.599–607. Native PDF metadata identifies 634 physical PDF pages. For printed Arabic page p, the acquired PDF page number is p+22 in the regions checked; the archive scandata leaf numbers agree with this physical numbering. No 1962 introduction was substituted.
- Archive metadata reports contributor Princeton Theological Seminary Library and a HathiTrust public-domain copyright review. This is the archive's rights statement, not an independent legal finding by the authoring agent.

Historical chapter legitimate scholar route:

- Intended free scholar-hosted copy: [HHL10_Zabell.pdf](https://www.stephanhartmann.org/wp-content/uploads/2016/02/HHL10_Zabell.pdf).
- Both `www` and bare-host HTTPS attempts failed certificate-name validation. Validation was not weakened.
- Public Wayback availability endpoint returned status200/availabletrue for timestamp20240917060514. Acquired using certificate-valid HTTPS: [public captured PDF](https://web.archive.org/web/20240917060514id_/http://www.stephanhartmann.org/wp-content/uploads/2016/02/HHL10_Zabell.pdf).
- Saved as `zabell-2011-published.pdf` (477537 bytes; this filename denotes the intended allocation, **not verified final-version equality**) and extracted as `zabell-2011-published.txt`.
- The copy contains the exact allocated title, author S.L.Zabell, pagination265–309 and complete sections1–14 plus bibliography. Its first-page footer says copyright2009. Publisher/DOI allocation is2011. Final publisher-version identity therefore remains an explicit dependency; no byte comparison with a final publisher PDF was performed.

## Actual bounded reading

Carnap original reading was source-body reading, not a title/citation search. Read title/copyright, preface discussions of the program and deferred second volume, actual contents, early explication material, and these relevant regions:

- §18 pp.70–79: state descriptions, logical independence, qualitative completeness (including the author's uncertainty about its necessity), related-property families, ranges. The saved nominal `pages-70-78.txt` extraction begins at printed71 and ends79; it must not be mistaken for a complete read of page70 solely from its filename.
- §§26–27 pp.109–118: name correlations, individual versus statistical distributions, and structure descriptions as disjunctions of individual-renaming orbits. A combined output clipped a small middle interval of the individual-distribution discussion; no claim of full deductive-chapter reading is made.
- §§31–32, archive OCR lines8269–8628, printed122–129: monadic restriction, Q-profiles, widths and primitive-property conjunctions.
- §45 pp.208–218: abstraction, total evidence, idealized examples, omitted evidence and approximation, usefulness and dangers of abstraction. Saved extraction read in two contiguous chunks.
- §55 pp.295–301: positive normalized state weights, extension to sentence ranges, conditional ratios, contradictory evidence, distinction between logic and application, and probability1/probability2. No claim of complete §§55–58 reading.
- §59, archive OCR lines18746–18975, pp.315–318: finite/infinite side conditions, confirmation bounds, equivalence, addition and multiplication statements and their actual finite proofs. Remaining §59 results and full §60 were not read in this block.
- §§90–94, saved `pages-483-497.txt`, actual printed484–498: symmetry definitions, renaming-invariance proof, individual/statistical evidence cancellation, direct inference and its finite-population qualifications. The beginning of §95 was read; its entire binomial/Bernoulli development was not.
- §110A–J, printed562–577, archive OCR lines32885–33970, read in successive chunks: actual c* definition, explicit distinction from equal-state weights, deferred justifications, monadic formula, predictive/direct/inverse/analogy/universal inferences, instance and qualified-instance confirmation, law use, variety and rational reconstruction. Formulas(6)–(8) on printed568–569 were checked visually against source page pixels saved as `carnap-source-formula-590.png` and `...591.png`; OCR of these formulas is corrupt. The mathematical derivations in the annex do not rely on accepting corrupted OCR equations.

Zabell copy: extracted text lines1–EOF (complete45-page chapter pp.265–309), read in sequential chunks including bibliography. The first combined output clipped part of §5; the entire clipped region was reread separately in lines469–777. Read extent is full **scholar copy**, not proven identity with final2011 publisher bytes. Source notation and chronology are retained as historical claims; mathematical results proved locally are bounded below.

Reader overlap inspected: finite-probability definitions and conditioning/Bayes/independence regions, plus its annex proof conventions; the final systematic-power discussion explicitly distinguishes its latent weights from a Carnap measure. Hume's source boundary was inspected. No shared induction host, Hempel or Popper file was edited.

## Authored mathematical scope

New reader `handbook/parts/p15/carnap-logical-probability-and-induction.tex` and reciprocal annex of the same basename establish ten pairs:

1. `carnap-language-counts`: Q-partition, widths, state/orbit cardinalities.
2. `carnap-regular-laws`: regular conditional identities and simultaneous name-renaming invariance.
3. `carnap-star-construction`: equal-orbit uniqueness, actual monadic masses, fitting finite systems, equal-state no-learning contrast.
4. `carnap-predictive`: refined-to-coarse aggregation, actual width-sensitive block/singular formulas, inverse distribution and finite mean estimates.
5. `carnap-direct`: arbitrary-symmetric known-count hypergeometric inference and fixed-sample multinomial limit.
6. `carnap-analogy`: 1950 equation(8), widths and explicit confirmation increase.
7. `carnap-universal`: finite law product, zero large-domain limit, instance and qualified-instance calculations.
8. `carnap-history-family`: independently justified later-family construction, not its sufficientness characterization; category-symmetric die obstruction.
9. `carnap-history-finite`: finite orbit-mixture representation, nonextendable binary pair law and variance/instantial-relevance bound.
10. `carnap-history-universal`: changed-prior universal-law example and first induction theorem, with its positive-hypothesis assumption.

Mathematical claims in examples are supported explicitly in these annex proofs. Philosophical reconstruction, objections and interpretation are presented as attributed arguments, not fake mathematical theorems.

## Exact remaining dependencies: no whole-source closure

The original selected allocation still requires systematic transcription of original comparative confirmation (especially §§79–88), relevance/irrelevance (§§65–76), general c-mean estimation and reliability (§§98–106), associated qualifications and actual proofs; full internal deductive dependencies not read here; arbitrary quantified infinite-language existence/effective computation of §110A; the variety-of-instances assertion §110I with its referenced prior-paper dependency; and any source-based comparative justification deferred by the author rather than actually contained in1950. The full 607-page book has not been read. Absence of an authored component is not evidence of absence from the book.

The historical allocation still requires final2011-copy identity resolution and full transcription of its advanced mathematical claims/dependencies: coherence converse, Johnson–Carnap sufficientness characterization (including binary/asymmetric qualifications), infinite de Finetti/Dirichlet and moment-characterization arguments, Hintikka–Niiniluoto extensions, quantitative finite approximation, Markov/normal mixture characterizations, species-sampling three-parameter characterization/Ewens law, and referenced merging/convergence-of-opinion results. The reader explains the author's chronology and major philosophical objections but does not claim complete proof treatment of this full chapter.

Status: **substantive authored, unreviewed, bounded treatment; allocations remain partial**. Acquisition succeeds for exact1950 and for a complete historical scholar copy; exact final2011 version remains unresolved. No source receipt, canonical bibliography/symbol registry, fulfillment map, queue, driver, baseline or manuscript host was edited.

## Root integration seam

Root should include the new reader with the philosophical induction cluster, after the relevant finite-probability prerequisites and alongside the current Hume/Whewell–Mill/Goodman treatments, before the systematic-power/confirmation comparisons that need its actual measure. Include its annex in the reciprocal P15 annex cluster, merge the two bib intake records after duplicate-key checks, and merge the scoped symbol intake. This subagent does not edit those shared integration files. The chapter's Hempel and Popper discussion deliberately does not duplicate or supersede their separately owned source treatments.

## Hash and delivery record

SHA256 delivery hashes obtained from the saved bytes:

| Artifact | SHA256 |
|---|---|
| reader | `6835EFB14B66E039011EF81762AA622AEDBD1545052E6C8370820D2EC686E058` |
| reciprocal annex | `D08931EC100735823CD4266A386ACDC7E085958234DE4A2761347A2C790FDC03` |
| bibliography intake | `71422390C882EDD58E3221D047DA680569F36415251F02FF18210BA38D079789` |
| symbol intake | `A73D366C873D683DEBD9AE6E6FF86E2470F0B1979D58254D933BF92AFD709810` |
| exact1950 PDF | `03536F3FEFE1419C1F233D66ED0BFDA31EBCA047DC175E9F5727878B1136E27E` |
| archive OCR | `E950532A494B9EA1D6A5CD1BBCE325B7E0F9539C6196F034E420A5EF86D71743` |
| archive scandata | `F79D3BF57AD713F342302D157DF85E44EB1576084CF6203A67AF51B6A0EA346C` |
| archive metadata | `DC381C297BB63A0717AD129A3175AC9CBF5D23C520D82FA5E2931AA6B2256441` |
| historical scholar PDF | `DEAC14BEC7F8E5291ABCF6F7D571BE52A603D38C8CE60DD493DBFFEF430255A2` |
| historical extracted text | `98B3503F7F1457799D7A1AF3CDAF2E682598825106DEEF6B1F1FBCC1716C85AC` |

The research note's own hash is supplied externally after its final save, avoiding a self-referential hash field. Source/authoring paths above are authoritative; filenames of bounded text extractions are not substitutes for the actual read extents recorded above.

## Distinct continuation block: 1950 comparison, relevance and reliability

2026-10-03 UTC, block began04:54:16; reading deadline05:24:16, save deadline05:29:16. First reader/annex and their intakes were frozen and were not edited. This block writes only the new `carnap-confirmation-relevance-and-reliability.tex` reader and matching annex, new relevance symbol/bib intakes, source reading extracts/images, and this appended record. No reviews, tests, build, or handbook rendering were performed.

Original source remains the exact1950 PDF SHA256 `03536F3FEFE1419C1F233D66ED0BFDA31EBCA047DC175E9F5727878B1136E27E`. Complete extraction and reading extents:

- `carnap-1950-relevance-346-427.txt`, lines1–3633, §§65–76 pp.346–427: sequential text chunks cover definitions, full side conditions and infinite exceptions, quotient/cumulative method, signed relevance, both two-observation and two-hypothesis analyses, all75 signs, state/content methods, extreme/complete relevance and their transformations. SHA256 `59FFCA53FE3ACB0E537B3CF3BDBDE0064EB10FA3041359B183D1B13B6E6832CA`.
- `carnap-1950-comparative-428-482.txt`, lines1–2322, §§79–88 pp.428–482: actual adequacy requirements, D81-1 and proof, finite/infinite T81 distinction, Eq/Gr/comparability, composition/Koopman and predictable-observation comparisons, C-prime and Carnap's Hempel assessment. SHA256 `2D343897F09396C217339CD19EBA297ADC0949F079DBE1EF553E62382674FE50`. Combined-output clips were repaired by separate reads of the beginning, lines76–150, and lines2071–2135.
- `carnap-1950-estimation-511-554.txt`, lines1–1959, §§98–106 pp.511–554: full original discussion of alternative statistical methods; general function/argument definition; continuous density/Stieltjes qualification; linearity and nonlinear paradox; three reliability candidates; signed/absolute/square error; internal-versus-external error warning; truth frequency; direct and predictive estimation. SHA256 `7BCA945C9E23E8A5773615B8FEEDA12493D9E622A0BF25AE91AAAA43B1BD65CD`.
- `carnap-1950-predictive-dependencies-555-561.txt`, lines1–292: §106C continuation and §107, including general-hypothesis renamed-class reliability proposal, null evidence argument, qualified straight-rule criticism and inverse estimates. SHA256 `D80052762D0142404B4FD9D0EE7BA99FE43E7DE891C7241EF29E487E457B6ECC`. Its clipped last passage was reread from the final45 lines.

Source-pixel readings: original T69-1 on printed378–379 (PDF400–401), T72-8 on printed403 (PDF425, sideways source layout), and T105-1 on printed547 (PDF569). Their OCR is corrupt; source pixels were inspected directly. The reader supplies an equivalent zero-sum generating classification and complete construction/count proof for all75 sign tuples, not a claim that corrupt OCR faithfully reproduced the source table. The current integral-reader definitions/results and full relevant monotone/nonnegative/signed-integral annex proofs were read before relying on them.

Authored scope has ten reciprocal pairs: full finite unanimous comparative criterion and nongeneral fitting extension; comparison calculus; determinant and signed additivity; multiple quotient accumulation; full75 signs and source chess countercases; state/content and extreme/complete criteria; actual quantified infinite-limit countercases; general conditional-distribution/integral means; error identities/minimum-square-loss and boundary examples; general dependent truth counts and direct/predictive reliability. General means have integrability and chosen-law conditions; no strict-positive mass on every point of an uncountable domain is assumed. New bibliography intake introduces no duplicate source key; it explicitly reuses `Carnap1950Probability`. Fifteen scoped symbol rows are supplied.

Source qualifications: the source states Gr using universal weak ordering plus strictness for at least one function. The continuation preserves that quantifier form and does not manufacture a finite equality countercase under the stronger logical criterion proved here. The density representation is conditional on an actual density, not merely on vanishing singleton probabilities. The source's historical estimation-method assessments are attributed to1950, not asserted as a description of2026 statistics. Monetary valuation, utility choice, adequacy of the chosen confirmation function and tentative reliability of a confirmation value are arguments/proposals, not deduced mathematical vindications.

Precise continuation still open: arbitrary general-sentence infinite-language logical transfer used by T81-2a; universal existence and effective computation of all relevant m/c limits; the construction of a confirmation function for the full quantitative language of science rather than assuming its probability representation; source-exact reproduction/proof attribution for the remaining fine-grained comparative catalogue beyond the reconstructed calculus (notably the full printed Koopman axiom mapping and every T83/T85 subitem); full original variety-of-instances and deferred comparative vindication dependencies; and the separate historical advanced proofs/final2011-copy identity. The history's2009 footer is unchanged and does not become2011 version closure through this original-source work. This continuation is authored and unreviewed, not whole1950-book closure.

Integration seam: root should place the new reader immediately after the frozen Carnap logical-probability chapter and its annex immediately after that reciprocal annex, using the already integrated first-edition bib key and merging this new symbol intake. Root retains exclusive ownership of canonical registries, drivers, queues, maps and receipts. Final saved hashes and physical line counts are reported externally after this append.
