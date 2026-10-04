# Edition 2026: finite probability and Kamp III.2 Lemma 1 source review

Date: 7 September 2026. Reviewer: fresh independent context
/root/probability_kamp_l1_source_review. Assignment: source fidelity of the
two frozen body/annex units, plus a bounded recheck of C7-SRC-03.
Repository: C:\Dev\the-methods-of-reason, branch phase4-codex,
HEAD 35d537c692bb74b532dc4aa750da381a7fe4daf2.

## Verdicts

| Reviewed unit | Verdict | Finding |
| --- | --- | --- |
| Finite probability body and annex | PASS | The cited version and source results support the stated finite treatment. The additional finite deductions have explicit proofs, and the boundaries on null conditioning, independence and infinite probability are preserved. |
| Kamp III.2, Lemma 1 body and annex | PASS | The statement, basic-pattern grammar, occurrence sequence, expressibility convention and strict temporal construction agree with the source after the documented p. 64 class-name correction. Both directions of the finite-chain and temporal constructions are supplied. |
| C7-SRC-03, p. 47 stage-index disposition | PASS | The scan has the reported unindexed occurrence. The stage regularization is supported by the source's recursion and subsequent induction, and the note correctly distinguishes it from a literal transcription. |

No actionable source-fidelity defect or unresolved source reading remains in
these three bounded scopes. These verdicts do not establish whole-unit
admission, production quality, full P15 coverage, completion of Kamp III.2,
or a fresh review of the unchanged III.1 mathematics.

## Method and actual read extent

The reviewer read the complete spec/EDITION-2026-CONTRACT.md and the
applicable PDF skill before inspecting source content. The PDF workflow
caused direct visual inspection of source pages. Source pages were rendered
from the hashed PDFs into separate task-local scratch; no manuscript was
rendered. Existing repository changes were preserved. The only repository
file written by this reviewer is this report. No tests, build, source edit,
manuscript edit, delegation, canonical-record mutation or admission occurred.

All four frozen manuscript files were read completely: finite probability
body lines 1-461 and annex lines 1-284; Kamp Lemma 1 body lines 1-202 and
annex lines 1-212. The active Kamp host was additionally read at
handbook/parts/p09/presentations/n-c-012.tex:1-160, including its language,
order classes, exact temporal semantics and all clauses of D. For the
bounded C7 check, the component grammar at
handbook/parts/p09/presentations/kamp-iii1-normal-form.tex:66-115 and the
complete C7 author note were read. The III.1 annex was hashed, not rereviewed.

The Grinstead-Snell source was read through extraction over the complete
title/dedication and printed pp. 18-24, 133-149 and 225-240. Physical body
page = printed page + 8. Extraction loses or corrupts several mathematical
glyphs; the following complete source pages were also inspected visually,
and those images controlled the relevant formulas: title page; printed
pp. 18, 19, 22, 23, 24, 134, 139, 140, 141, 142, 143, 144, 145, 146,
226, 228, 230, 231, 232, 233, 234, 239 and 240.
This is a bounded reading, not a claim to have read the entire book.

The Kamp scans were inspected visually throughout physical pp. 1-2,
48-51, 56 and 68-79: title/approval pages and complete printed pp. 39-42,
47 and 59-70. Physical body page = printed page + 9. These include all of
Lemma 1, its preceding definitions and the opening of Lemma 2; the latter
was read only to verify the continuation boundary. Extracted Kamp glyphs
were not used as formula authority.

The canonical bibliography entries GrinsteadSnellChance2006 and Kamp1968
were read and compared with the held title pages. Relevant source-relation
and correction passages in the two author notes were consulted as claims
to check and as provenance locations. Their judgments were not evidence.
No new independent review report was opened before filing these findings.
References to an earlier reviewer inside the assigned C7 author-note target
were treated as historical metadata.

## A. Finite probability: source correspondence

The title page identifies *Grinstead and Snell's Introduction to Probability*,
the CHANCE Project, version dated 4 July 2006. Its footnote identifies
copyright 2006 Peter G. Doyle and the 2003 second edition by Charles M.
Grinstead and J. Laurie Snell as its basis. The canonical entry at
handbook/bib/handbook.bib:6583-6594 preserves these distinctions. The body
at lines 12-19 cites this actual version.

| Manuscript claim and proof | Direct source support and review finding |
| --- | --- |
| Body 24-75; annex 12-56: masses, event probabilities and finite identities | Definition 1.2 on pp. 19-20 and Theorems 1.1-1.4 on pp. 22-24 give nonnegative normalized atom weights, event sums, monotonicity, finite additivity, complements and the two-event union identity. The separation of underlying outcomes from variable values is announced at body 16-17; replacing the source's term distribution function by mass function is explicit at 51-55. |
| Body 77-111; annex 58-78: laws, joint laws, marginals and grouping | The joint-variable and joint-distribution discussion on pp. 141-144, together with the grouping principle on pp. 229-230, supports the reconstruction. The annex proves normalization and both marginals by disjoint fibers, including empty and unattainable fibers. |
| Body 116-167; annex 80-119: conditioning, multiplication, chain rule and successive conditioning | Conditional reweighting on p. 134 explicitly requires positive conditioning probability. Every proper prefix used as a chain-rule denominator is positive; the last intersection may be null. Successive conditioning has the sufficient guard P(B intersect C) > 0. |
| Body 169-212; annex 121-149: total probability, Bayes and odds | The source's partition and equations (4.1)-(4.3), pp. 145-146, supply the Bayes construction. The manuscript excludes null prior blocks from likelihood sums, supplies their zero posterior branch, proves normalization and states the denominators needed for ordinary real odds. |
| Body 217-253; annex 151-200: independence and product models | Definition 4.1 and Theorem 4.1, pp. 139-140, support the equivalent product definition, including null events. Definition 4.2 on p. 141 supports the all-subfamily definition. Definition 4.4 on p. 143 supplies random-variable factorization, and p. 144 supplies a product law. Complemented pairs and event-set/fiber equivalence are separately proved. |
| Body 343-393; annex 202-249: expectation, grouping, linearity and independent products | Definition 6.1 on p. 226 and Theorems 6.1-6.4 on pp. 230-234 support these claims. The source removes an independence requirement from linearity on p. 232 and requires independence for its product theorem. The finite restriction makes the manuscript's sums defined without convergence assumptions. |
| Body 395-445; annex 251-284: conditional means and averaging | Definition 6.2 and Theorem 6.5 on pp. 239-240 give event conditioning and partition averaging. Their compact statements inherit the positive-event restriction from p. 134. The manuscript states that guard and proves the finite-valued conditioning-variable extension. |

The following additions were checked as supplied deductions, rather than
treated as individually numbered results in the source: the unique atomic
representation of an additive finite event measure; support/null/almost-sure
characterizations; projection by an arbitrary finite function; guarded chain
and successive conditioning identities; preservation of prior-null
hypotheses; the odds identity; complemented-event independence; equivalence
between joint factorization and independence of all value events; arbitrary
two-factor product laws; expectation monotonicity; and the averaging
characterization and almost-sure uniqueness of E[X | Y]. Their annex proofs
use finite partitions, nonnegative sums, distributivity or cancellation by
a stated positive number. No proof depends on a concealed infinite theorem.
The author provenance also identifies the atomic converse and E[X | Y]
characterization as supplied finite additions.

The null-fiber convention at body 404-413 assigns a representative value to
a random variable; it does not define conditioning on a null event.
Annex 277-282 divides only on positive fibers and takes a finite union of
null remaining fibers. Body 158-167 correctly distinguishes nonemptiness
from positive probability and almost-sure truth from truth at every outcome.

The source's alternative complemented-full-pattern characterization on
p. 141 is not asserted as an additional theorem in this unit. The adopted
all-subfamily definition is the source's other definition. The additional
characterization, exercises, named distributions and source applications
are not claimed completed by this finite foundations unit.

The examples were checked against their stipulated masses. The four alert
weights total 10000; the single-alert posterior is 90/585 = 2/13; the
changed-prior posterior is 2/3; the conditional product model gives 36/47
after two alerts. Copying one alert leaves 2/13 and is presented as a
different dependence model. The pairwise/mutual example and the dependent
indicator product have their stated intersections and expectations.
These are hypothetical finite constructions, not empirical claims imported
from the source's medical examples.

The source defers the long-run interpretation of expectations on pp. 228-229.
Body 447-461 preserves the need for separate sampling/model justification
and a law of large numbers, and excludes continuous, infinite and
null-conditioning extensions from this chapter.

## B. Kamp III.2, Lemma 1: source correspondence

The held title/approval pages identify Johan Anthony Willem Kamp,
*Tense Logic and the Theory of Linear Order*, UCLA dissertation, 1968.
The canonical Kamp1968 entry agrees.

Definition 11 on source p. 59 uses an alphabetic variant followed by proper
substitution of the named point for t_0. Body 11-28 preserves that convention
with capture avoidance. The first-order S and U clauses and D on pp. 39-42
put the first argument at a strictly earlier/later witness and the second
throughout the intervening open interval. Both active host clauses and the
new body/annex use that exact argument order.

Source p. 63 has identical binary bases, then different past and future
associations. Body 30-103 preserves the base without an x < y conjunct, the
fresh strict interior witness at every later stage, the constituent classes
Bp_n(z,y) and Bf_n(x,z), and the later unions over stages. There is no
retention clause within these exact stages. The unary closures provide the
strict endpoint guard. The syntactic x != y condition is explained as
distinctness of variable names.

Source p. 64 counts all predicate occurrences in textual order, including
repeats. Body 105-132 does the same using sigma, and its n intervals /
n+1 points convention consistently reindexes source p. 65. Annex 18-31
proves the occurrence count and free-variable claim. Annex 33-98 proves
both binary associations equivalent to the same realized chain, including
unordered endpoints: stage-one formulas coincide and higher stages are
both false. This supplies the four remarks on source pp. 65-66, including
existence of both associations and same-word equivalence.

Lemma 1 on source pp. 69-70 states expressibility of the unary basic past
and future union over Lin. Its past proof introduces an auxiliary starred
family, rearranges witnesses and composes expressible links by proper
predicate substitution; it abbreviates the future companion. The new annex
describes that procedure at 203-207 and supplies its own explicit chain
rearrangement and two temporal recurrences. It does not claim that L_i/R_i
are Kamp's literal auxiliary notation.

The recurrences at body 144-149 have the correct directions: L_i uses
A_i and S(L_(i-1), B_i) upwards; R_i uses A_i and U(R_(i+1), B_(i+1))
downwards, with hats understood on predicate letters. Annex 126-185 proves
both implication directions using the penultimate or second witness.
Repeated letters create no substitution collision because the construction
tracks occurrences and forms temporal formulas directly. Single-letter
recurrence seeds do not add a stage-zero basic class.

The strictness examples at body 172-191 follow: two interval pieces require
three distinct ordered points; one piece requires two, while its open
interval may be empty. No density, endpointlessness or completeness enters
the proof. Body 193-202 agrees with source pp. 60-62 and 66-70:
the limiting classes and later interval work remain necessary for all
regional formulas and the complete III.2 theorem over Com.

### Confirmed source-name correction

On printed p. 64 the future-closure line repeats Bp_n(y) on its left,
although its right is the strict future closure of Bf_n(y,t_i).
The p. 63 definitions, p. 66 unary satisfaction remark and p. 69 lemma
statement determine the future name. Active Bf_n(x) at body 85-87 corrects
that label and consistently renames the endpoint. Its guard and binary
constructor are unchanged. The correction is recorded outside the
derivation in spec/research/edition-2026-c7-kamp-iii2-lemma1.md:151-166.

The source proof paragraph on p. 69 also repeats Bp when announcing the
same-way companion. The actual lemma union resolves that companion as the
future class; the active annex proves it. This is documented at author-note
168-177. The frozen PDF is unchanged; neither typo becomes an active claim.

## C. Bounded C7-SRC-03 recheck

The target is spec/research/edition-2026-c7-kamp-iii1.md:119-144.
Printed p. 47 has unindexed Bef(z) in the constituent union for
Bef_(n+1)(x), beside indexed Bet_n(z,x). The mirror Aft and Bet clauses
display the stage indices. Active body 96-98 uses Bef_n(z), as the note says.

Printed p. 60 organizes the next argument from Bef_n and Aft_n to stage
n+1; p. 61 invokes stage-n membership of proper regional subformulas.
Together with p. 47's announced recursion, these passages support the
staged reading. The corrected occurrence chooses an earlier-stage
constituent where the literal unindexed reading allows the eventual union.
It therefore cannot enlarge the source's unindexed language.

The note correctly labels the regularization, preserves the discrepancy as
provenance and gives the inclusion needed for active output membership.
This PASS concerns that disposition. It does not assert literal equality
of the printed stage inscriptions, settle arbitrary readings of the
circular unindexed occurrence, or rerun the whole III.1 proof.
The unchanged III.1 body and annex hashes were independently rechecked.

## Frozen identities and dependencies

All assigned manuscript and source-PDF hashes matched on initial inspection
and were rechecked at filing.

| Artifact | Lines | SHA256 |
| --- | --- | --- |
| handbook/parts/p15/finite-probability.tex | 461 | BD14BAB29058D7235155D827A8F11793A1D07AF119AD1B34239835EF98805AC0 |
| handbook/annex/p15/finite-probability.tex | 284 | D51A43CF5E2CD2DCE15CD558EF3A167AC084347BB471E2A44E657769399EAE58 |
| handbook/parts/p09/presentations/kamp-iii2-lemma1.tex | 202 | 3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6 |
| handbook/annex/p09/kamp-iii2-lemma1.tex | 212 | 631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1 |
| source/references/grinstead-snell-chance-2006/prob-2006-07-04.pdf | -- | 763EAB9894983DDFD6CD7F84685548D1515A9326A2D9FD015474534460551A5E |
| tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf | -- | C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA |

Additional identities recorded during review:

| Dependency | SHA256 |
| --- | --- |
| spec/EDITION-2026-CONTRACT.md | C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3 |
| handbook/bib/handbook.bib | A9CFDB177C40F50581B87F8626318FDEFEAA7C5C300D7971A09FFEA2F22C9A53 |
| handbook/parts/p09/presentations/n-c-012.tex | 35F9137094A285A4847D351FF868CC206EBF3A6F8F7A75DAC767F0C0AFCE2590 |
| handbook/parts/p09/presentations/kamp-iii1-normal-form.tex | 0D1EB5FC960B7F0F1EB216026AF2AAF953CD3D95F62E4ACF014345611D860B31 |
| handbook/annex/p09/kamp-iii1-normal-form.tex | A46BFF4D11C868E8A865F2F9CC89690FCB4D03A550EB6CCB755B4C067A3B7F8B |
| spec/research/edition-2026-c7-kamp-iii1.md | E7EDB297952B265B3EDD954868A0D9F3D73745811B9964B1455045D1D6D3154B |
| spec/research/edition-2026-c7-kamp-iii2-lemma1.md | F3254DA85D895833F625D5E5998A1F874917AC4FBB67D89CE4DFDF54B1E217D2 |
| spec/research/edition-2026-p15-u1-finite-probability.md | 4B172BAC317CBADA8CF1C388FFB46F8E18CC250F9C5D8161E3A276F6A48DE432 |

This report's hash is supplied in the handoff after saving and read-back.
