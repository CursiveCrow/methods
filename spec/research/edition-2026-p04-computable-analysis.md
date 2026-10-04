# P4 computational analysis: authoring, source repair and fulfillment handover

Date: 3 October 2026. This is a bounded authoring record, not independent
review, source admission or a canonical fulfillment update. Root owns the
drivers, canonical bibliography and symbols, named scope bindings and ledger.

## Scope and actual current-state finding

The assigned planned sections were52.1–52.4, under original requirement
ED26-REQ-N-x-014-01. Current LaTeX already contains substantial treatments:

- handbook/parts/p04/represented-spaces-and-type-two-computation.tex:
  439 lines;9 full declared reader/annex pairs.
- handbook/annex/p04/represented-spaces-and-type-two-computation.tex:
  517 lines.
- handbook/parts/p04/computable-function-operators.tex:
  493 lines;11 full declared reader/annex pairs, not13.
- handbook/annex/p04/computable-function-operators.tex:562 lines.

Both readers and both annexes are already on the actual P4 routes:
parts/p04.tex lines79–80 and annex/p04.tex lines8–9. Those files were
preserved, not rewritten or duplicated. The new work supplies meaningful
strengthening rather than another generic names/realizers introduction.

## New saved reader and full proofs

Reader: handbook/parts/p04/computable-real-analysis.tex,239 lines,
section anchor sec:p04-computable-real-analysis. It is a section fragment,
not another chapter. Suggested seam: after computable-function-operators,
so all representation/operator prerequisites have already appeared.
Annex: handbook/annex/p04/computable-real-analysis.tex,263 lines.
Both remain unrouted pending root integration.

Six reciprocal declared result/proof pairs:

| Suffix under thm:p04-ca- / annex:p04-ca- | Reader line | Annex line | Actual content |
| --- | ---: | ---: | --- |
| sample-modulus |44 |3 | Both computable translations between uniform polygon names and rational sample tables plus a supplied modulus; rational grid recovery, finite termination and uniform interpolation error |
| sample-obstruction |58 |42 | Finite-prefix counterexample using a rational tent of area one; continuous integration and uniform-name translation fail for weak samples, even exact queried values |
| computable-c1 |137 |74 | Corrected full bump construction, disjoint supports, derivative continuity at0, nonexistence of second derivative at0, exact centre values, effective tail and actual polygon-output algorithm |
| noncomputable-derivative |156 |165 | Uniform centre evaluation would decide an undecidable enumerable set; explicit rational separated threshold; absence of a computable derivative modulus |
| derivative-modulus |179 |191 | Both directions of the computable-derivative/modulus equivalence; C2 fixed-function proof, supplied-bound uniform variant and higher-order individual/nonuniform distinction |
| root-certificate |214 |228 | Positive lower-slope uniqueness, residual-to-location bound, productive certified residual search and perturbation bound for every existing perturbed zero |

Definitions precede their uses. Names retain actual scalar versus function
types. The arbitrary-negative membership test needed to enumerate bumps is
not used. No real-equality decision is smuggled into endpoint handling or
the derivative gap argument. Small residuals are not called root existence
or location certificates without the stated additional premises.

The reader and annex were read back completely after writing. One wording
ambiguity was repaired so the Lipschitz constant four explicitly belongs
to f, not f'. This is author read-through, not independent review.

Intakes:12 raw grouped symbol-role records and one new bibliography entry.
Grouped records are not an atomic-glyph count; root performs typed expansion
and collision reconciliation. Existing Weihrauch1995IntroductionRS is reused
without creating a title-only duplicate. No calculus sheet is needed because
these are represented algorithms and analytic constructions, not a new
deductive-rule system.

Frozen content hashes:

| File | SHA-256 |
| --- | --- |
| parts/p04/computable-real-analysis.tex |84C5E74D5CE10FD59DF39363BB9736D5FF1B7965DD29DD151F8C78360D654FEC |
| annex/p04/computable-real-analysis.tex |507243EC4C826CAEE4AECCABD3758EE71C000CC19A79D569B06E9B4CEBF653C2 |
| registry/symbols-intake-p04-computable-analysis.csv |03632CCBBBFD11CFBE78F274E845695713CB14693EE56B5C2188BD97CAE3A4C4 |
| bib/intake-p04-computable-analysis.bib |D47211CE76032FB0C1C4A817A6FE080349916153A40607DB51BD718160C844A8 |

## Exact held source, reading extent and transport

Olivier Bournez, MPRI Course Complexity over the Reals, Part I, Computable
Analysis. Cover expressly identifies Version of November14,2024.
[Author's institutional PDF](https://www.lix.polytechnique.fr/~bournez/load/MPRI/Cours-2024-MPRI-partie-I-goodMPRI.pdf).
The92-page PDF's creation/modification metadata also dates14November2024;
this is not the earlier2021 lecture or a2025 version inferred from search.
Holding: source/references/p04-computable-analysis/bournez-2024-computable-analysis.pdf.
SHA-256:FB0384CC4130E29A48D2094FA960B0B714881E1FCF68F09203593325175E72A0.

Read: identity/contents, selected context on scalar computability and
finite-use continuity, and the complete section8.2, printed/physical50–53,
including all nine subsections, theorem8.6, corollaries8.1–8.2,
basic/scaled bumps, enumeration, support argument, continuity, positive
computability, derivative obstruction and final value-comparison remark.
Source pages52–53 were additionally inspected as pixels to confirm the
printed scale exponents and proof formulas; these are source inspections,
not manuscript renders. The source prints '(dessin)' in the bump account,
not an actual supplied diagram; no nonexistent image is credited.

Normal Invoke-WebRequest and system curl failed with native TLS credential
errors. Python standard-library urllib with its default certificate
verification successfully fetched the advertised institutional PDF:
HTTP200,application/pdf,831180bytes. No TLS bypass, account, anti-bot
circumvention, paid acquisition or dependency installation was used.

Myhill's1971 original, DOI10.1307/mmj/1029000631, was not acquired or read.
The Project Euclid route failed in the web tool; normal native transport
failed, and a default-verified urllib request returned1159bytes of HTML,
not PDF. The signature assertion rejected it and no false PDF was saved.
Bournez is authority for this author's2024 presentation and attribution,
not evidence of original1971 body reading.
The entire92-page course is held but not fully read or reconstructed.
Other selected fixed-point, differential-equation and resource-complexity
results in that source remain outside this unit's credited extent.

The already held Weihrauch corrected second version, July1995, remains
separate: source/references/p04-represented-spaces/weihrauch-simple-introduction.pdf,
SHA-256 CA29A4B6CCCA832DFFDCFAF70B4025A78D4A8C2884193BFE01A1DB507A1587FC.
Existing operator definitions and proofs and its recorded source-reading
extent were used, not relabeled as the complete2000book.

## Direct mathematical correction provenance

Bournez2024p52 prints alpha_n=2^(-k-2n-2),beta_n=2^(-k-n-2).
Those give beta_n/alpha_n=2^n, while its p52 continuity argument needs
that ratio to tend to0 and p53 states it is2^(-n). Pixel inspection
confirms the defect is in the source formula, not an extraction error.
The active reconstructed definition retains the published theta,lambda,
scaling map,alpha_n,width geometry,h,A,centre locations and partial-sum
indexing, and corrects beta_n to2^(-k-3n-2). Then the actual ratio is
2^(-n); all stated derivative limits, centre values and error bounds
are proved with those parameters. This corrected presentation is expressly
identified in the reader, not misattributed as the unmodified original.

Additional proof repairs:

- The source omits the1/lambda factor in its derivative bound. The active
  proof keeps it, computes lambda, and establishes1/lambda<4.
- The source's p53 proposed theta case computation does not return zero
  outside the negative support: min(0,x(x^2-1)^2) is negative for x<−1.
  The active formula uses a computable clamped argument and is exact on
  the whole real line, with no undecidable boundary comparison.
- The p50 mean-value expression refers to f' where the second derivative
  is required to bound changes of f'. The active C2 proof uses f'' and
  an explicit existing or supplied integer bound, with their distinct
  individual/uniform computational standings.
- The theorem8.6 modulus exercise is completed in both directions from
  the actual polygon-modulus and secant algorithms already supplied.
- The original finite-sum value argument is strengthened to an actual
  uniform polygon-name procedure, including every output error term.
  A computable scalar evaluation family alone is not substituted for
  a function-name proof.

The sample-table bridge/finite-prefix tent obstruction and the lower-slope
root certificate are explicitly derived reference extensions of the held
representation/operator framework, not attributed as unmodified numbered
Bournez or Weihrauch theorems. Their complete arguments are supplied.

## Proposed52.1–52.4 fulfillment correction for root

The stale observation 'missing' is contradicted by actual routed reader
and proof text for all four planned sections. Recommended record is
**partial, with the local drafted extent stated**, not entire-source
complete or independently accepted. Root alone changes the ledger.

| Planned section | Actual active supplied extent | Distinct residual |
| --- | --- | --- |
|52.1 Names, representations and Type-Two Effectivity | represented-spaces reader23–123; defs p04-rs-baire,representation,machine,realizer; theorem p04-rs-finite-use and annex3–37; rational/Cauchy clauses reader215–297 and bridge annex200–317 | Complete separately allocated Weihrauch2000 naming/TTE body remains unheld; finite/infinite source syntax is not identified without the supplied code bridges |
|52.2 Realizers, admissibility and representation invariance | represented-spaces reader124–213; reduction,invariance,admissible,neighbourhood definitions; results p04-rs-invariance,standard,topological with annex38–199; source-to-host Cauchy bridge separately proved | Admissibility claim is proved for the stated countably based T0 setup, not arbitrary nonsequential spaces or an effective universal lifting theorem; original2000whole-source duties remain |
|52.3 Computable versus continuous operations | finite-use reader115–122, topological descent/lifting198–213, obstruction/continuous-noncomputable391–425; annex447–517; already supplied arithmetic/reciprocal proofs; new sample/modulus and sample-obstruction results saved off-route | No promotion from continuous lifts to computable lifts; source-specific full2000characterization and unread alternative frameworks remain distinct |
|52.4 Differentiation, integration and zero finding | function-operators reader211–491: evaluation/modulus, scalar/global/primitive integration, uniform derivative failure, supplied derivative-modulus positive construction, zero relations/selectors, unique/local isolated roots, inverse, certified residual and no-computable-zero construction; corresponding full annex164–562; six new pairs strengthen these after routing | Complete2000operator source remains unheld. New corrected2024bump presentation is not originalMyhill1971, Pour-El–Richards1989, or a proof of arbitrary root computability. Existing1995evaluation universal characterization/set-image/composition boundaries are not silently upgraded |

Hashes of the preserved actual active units at this observation:

| File | SHA-256 |
| --- | --- |
| parts/p04/represented-spaces-and-type-two-computation.tex |7BD267AF5390B94525B77353CA34073FD7B8278EB1338303CB2CA523D27FE56B |
| annex/p04/represented-spaces-and-type-two-computation.tex |9F5159AE9780AA34084A58EC9BE8CE9EDD257DD64833DF3D21EC52A12532BDAB |
| parts/p04/computable-function-operators.tex |94046AF1B3BDBC1539C70D7577D7C869FAC2623785AEF99740C2202261B52542 |
| annex/p04/computable-function-operators.tex |E873F6DA199E16685BB8A7C54C91C9DFA05EF62119C45A566AC9FD4F4E2FFD64 |

The entire chapter52, including52.5–52.11, is not complete. Computability
structures, Banach/Hilbert constructions, physical-equation examples,
resource analysis, multivalued ordinary/strong Weihrauch reductions,
degree operations and exact framework comparisons remain separate duties.

No child, review, test suite, book build or manuscript render was run.
Research and source-only PDF skills were read and used. The assignment's
no-children instruction superseded Research's ordinary background delegation.
No shared or canonical manuscript file, existing intake/source, status map,
review record or generated artifact was edited. Root integration and the
later consolidated independent gates remain unperformed.
