# P19-E3: calibration, extreme confidence and the original Brier score

8 September 2026. Block began 19:41:39 UTC; deadline 20:26:39 UTC.
Owned: `handbook/parts/p19/calibration-and-extreme-confidence.tex`, matching
annex, this note, `handbook/bib/intake-p19-calibration.bib`, and the two new
source directories below. Root owns shared integration, bibliography and
symbols. Earlier chapters and earlier source-gap records were not edited.

## Primary identities, capture provenance and complete reading

**Baruch Fischhoff, Paul Slovic and Sarah Lichtenstein (1977), Knowing with
Certainty: The Appropriateness of Extreme Confidence.** Journal of Experimental
Psychology: Human Perception and Performance 3(4), 552-564.
DOI: **10.1037/0096-1523.3.4.552**.

- Local: `source/references/fischhoff-slovic-lichtenstein-extreme-confidence-1977/fischhoff-slovic-lichtenstein-1977-primary.pdf`
- Download: https://nuovoeutile.it/wp-content/uploads/2014/10/Knowing-with-certainty.pdf
- **13 pages; 1,017,889 bytes.**
- SHA-256: **4660B7325A70E0CE79E9D29079F9A0BEA6C17DD0D92C55533217D2B0D7352B83**.
- Actual first page gives the original journal, year, volume, issue, pages,
  title, authors and Decision Research/Perceptronics affiliation. The final
  page records receipt on 14 December 1976, not a data-collection date.
- Identity independently verified against the author's institutional list:
  https://epp.engineering.cmu.edu/directory/bios/fischhoff-baruch.html
  (1977 entry with matching title, authors, pages and DOI).
- Its linked CMU `jep-hpp-knowing-with-certainty-1977.pdf` endpoint redirects
  to a login, which was not pursued. The acquired freely hosted file is an
  original-journal scan, not a claimed byte-identical copy of the unavailable
  author-linked file or the later book-chapter reprint.
- Read **all 13 pages, printed 552-564**, including all five experiments,
  tables, discussion, notes and references. Additionally read source page
  images for printed 554-557, 560-562, verifying the table cells and
  numerical conflicts rather than relying on OCR. Other game pages were
  read completely in text. Source images of printed 558-559 were generated
  but not used as visual evidence. No manuscript page was rendered.

**Glenn W. Brier (1950), Verification of Forecasts Expressed in Terms of
Probability.** Monthly Weather Review 78(1), 1-3.
DOI: **10.1175/1520-0493(1950)078<0001:VOFEIT>2.0.CO;2**.

- Local: `source/references/brier-probability-forecasts-1950/brier-1950-primary.pdf`
- Publisher download:
  https://journals.ametsoc.org/downloadpdf/journals/mwre/78/1/1520-0493_1950_078_0001_vofeit_2_0_co_2.pdf
- **3 pages; 272,336 bytes.**
- SHA-256: **3778C4D3C8BDE70AF34D1B15A16517428537447E740B6F379CDD9B5268570754**.
- Read **all three pages** in text and page images, including both tables,
  equations, discussion, conclusion and references. The actual issue header
  says January 1950, closed March 5, issued April 15, with manuscript received
  February 10. The January issue label is not an assertion that publication
  preceded manuscript receipt. The currently delivered publisher PDF includes
  its retrieval footer; no claim of original 1950 byte identity is made.
- Original formula sums category squared errors and divides by occasions,
  not categories. For binary outcomes its range is 0-2 and it equals twice
  the one-coordinate squared score. The ten actual forecast records and
  five bins from the 85-forecast table were read and retained.

## Scope frozen before drafting

All **five** actually numbered 1977 experiments are included. Experiment 1:
four probability/question formats. Experiment 2: 106 mortality-pair questions
with odds. Experiment 3: the same task with a twenty-minute explanation and
calibration lecture. Experiment 4: difficulty-matched general knowledge,
the lecture, and hypothetical graduated chip-game offers. Experiment 5:
the announced real game, followed after willingness decisions by protection
of promised participation payment. The introductory calibration figure is
earlier literature, not a sixth new experiment.

Brier contributes his full original score, constant-forecast argument,
ten-record calculation, 85-record binned illustration and forecast context.
The finite conditional-mean/decomposition and binning proofs are handbook
deductions; they are not attributed as equations printed in Brier 1950.

## Evidence retained and checked against actual tables

Experiment 1: method N=361 paid Oregon student-newspaper advertisement
respondents; assignment according to preferred session times/dates, with
different items across formats. Table 1 prints item/N/response triples
43/30/1290, 75/86/6450, 75/120/9000, 50/131/6500. All certainty-report
frequencies and percent-true figures are retained. On report 1, table accuracies
83.1/71.7/81.8/80.7; on report 0, truth rates 29.5/20.5. For report zero,
truth is an error of certainty in the negation, not a correct zero forecast.

Experiment 2: N=66, 106 pairs, 6,996 judgments; task odds >=1:1, flexible
unbounded high end, glossary, all 41 historical cause-of-death rates, source
pair-construction criteria and historical rate-source description retained.
3,560 reports above 50:1, about 51%; all Table 3 major-category counts and
percent-correct figures, including the highest category's textual >=1,000,000:1
interpretation, are preserved. Experiment 3: N=40, same questions, groups
about 20, complete described instruction intervention; comparison remains
between cohorts rather than a randomized lecture-only causal estimate.

Experiment 4: N=42, 106 general-knowledge pairs, individually matched item
difficulty; same instructional route. All major-category results and overall
reported accuracy (71.0/72.5/73.1 for E2/E3/E4) are retained. Chip bag
100 white/2 red, replacement, wrong-answer cost $1, red-chip payments
$1/$1.50/$2/$2.50. Original $2.50 participation pay and hypothetical status
are explicit. Source acceptance sequence 27/6/3/2 and three refusals are
preserved with the conflicting subsequent 39-person analysis separately.
All reported simulated outcomes are retained: 1,495 selected answers,
mean 38.3, 36 expected losers/3 winners, range -25.63 to +1.84, mean
-3.64, median -2.35, ten losses above $5, total -142.13, 9.5 cents per
selected answer, and -33.38 for the two people asking particularly to play.

Experiment 5: N=19, acceptance sequence 6/3/1/3, six refusals. Real-game
announcement precedes willingness decisions; loss protection follows those
decisions. Thirteen players, 387 selected answers, 46 wrong (11.9%), no red
chips, unprotected balances -1 to -11, simulated mean -2.64 and four below
-6. The manuscript does not claim that these protected participants had
their promised payments confiscated, or that all 19 supplied the reported
player-only calibration subset.

Complete Table 4 person distributions and item distributions are retained,
including the 32/27-error outliers, the 5/3 people with no extreme error,
and 33/41 zero-error items. All Table 5 difficulty/threshold rates, all six
Table 6 example rates/counts, and all seven Table 7 keys/rates/counts are
retained. Deceptive means <50% correct, defined from these samples, not an
independent manipulation. The source's Poisson resemblance is a descriptive
claim with no reported fit test; one-third-of-easiest-items finding has no
published exact denominator. Outlier deletion is attributed without inventing
replacement data. Historical keys are not certified as universal current
facts for abbreviated cultural questions.

## Source discrepancies and direct manuscript corrections

These conflicts were read in page images and are not merely OCR artifacts:

- E1 prose N=361, but its table N values sum to 367; the final table row
  prints N=131, 50 items and 6,500 responses, although their product is
  6,550. No unreported exclusion is invented, and no single corrected N is
  asserted without further original evidence.
- The prose says probability-one answers were right 20-30% of the time.
  Table 1 instead supports 71.7-83.1% right, 16.9-28.3% wrong. The active
  manuscript directly uses the table-supported direction, not the reversed
  sentence. Report-zero truth rates are retained in their correct direction.
- Table 3 listed counts 6,098/2,981/3,855 correspond to about
  87.2/70.3/86.6% of full or nominal totals 6,996/4,240/4,452, whereas
  printed total shares are 88/70/75%. The E4 2:1 row also prints 1%
  beside 455 responses. The body retains counts and accuracy columns and
  distinguishes computed shares from inconsistent printed ones.
- E3's prose refers to a remaining 32% despite about 70% in major bins.
  2,981/4,240 gives an omitted nominal share about 29.7%; no 32% denominator
  is used. Its reference to 27% low-odds responses in Experiment 1 is read
  as a comparison to the preceding odds experiment, E2; E1 elicited probabilities.
- E4 incremental acceptances total 38, while three refusals from 42 and the
  following simulation use 39 acceptors. Both records remain visible.
- The mortality table includes a zero smallpox rate, so the stated finite
  ratio range cannot be an upper bound for every possible pairing with it.
  Equal-rate causes also appear. The full 106-pair list is not printed, so
  unreported pair choices are not manufactured.
- Exact calibrated expected error bounds at odds >=50, >=100 and >=1000
  are 1/51, 1/101 and 1/1001. Rounded decimal percentages must not become
  strict upper bounds that are slightly smaller than the exact fractions.
- Brier's category-sum scale and the later binary one-coordinate scale differ
  by exactly two. His concluding claim about increased extremes/correlation
  is not imported as a necessary condition for improved score; the body and
  proof give a concrete counterexample via calibration improvement.

## Five complete mathematical statement/proof pairs

1. `thm:p19-calibration-decomposition` / `annex:p19.calibration-decomposition`:
   finite conditional-mean minimization; calibration error/uncertainty/resolution
   decomposition; recalibration is calibrated under the same law; uniqueness,
   range and mean-bias distinctions. Null judgment values receive an explicit
   arbitrary version value instead of a fictitious conditional probability.
2. `thm:p19-binned-calibration` / `annex:p19.binned-calibration`:
   exact within-bin variance/covariance terms, their disappearance for exact
   judgment classes and explicit concealment of opposing errors by coarse bins.
3. `thm:p19-brier-propriety` / `annex:p19.brier-propriety`:
   original range and strict propriety; empirical constant optimum; binary
   normalization; proper reporting under a wrong belief can be miscalibrated.
4. `thm:p19-score-calculations` / `annex:p19.score-calculations`:
   Brier's actual ten rows, all constructed calibration/resolution examples,
   odds conversion, exact extreme-threshold expectations and endpoint identities.
5. `thm:p19-certainty-game` / `annex:p19.certainty-game`:
   expected unprotected money by linearity, subjective belief premises, strict
   versus weak advantage, seventeen-answer and fair-bag arithmetic, realized
   versus simulated balances. The subjective calculation explicitly requires
   believing the chip probability as well as one's answer probabilities.

Dependencies read in actual manuscript: `def:p15-finite-conditional-expectation`,
`thm:p15-finite-total-expectation`, `thm:p15-finite-expectation-laws`, their
finite proof interfaces, and P19's actual empirical-evidence standards. No
independent-trial premise is used for the descriptive or expectation identities.
Finite empirical improvement from fitting observed outcomes does not establish
new-sample calibration or forecasting improvement.

## Remaining source/evidence boundary and integration

Both full original primaries are acquired and read; no PDF-access gap remains.
The 1977 sample/denominator/acceptance conflicts remain exact unresolved source
fields. Resolving them needs an original correction, report or underlying
records. The paper does not print full item lists, glossary, lecture text,
participant-level data, principal-contrast confidence intervals/tests or
complete outlier-deletion reanalyses. It reports deleting ambiguous answer-key
items before study without giving their count. No further exclusion rule is
invented. Brier's 85-case table lacks bin counts and individual probabilities.
None of these missing quantities is reconstructed as observed evidence.

Root integration: chapter and five-item annex in P19, plus bibliography keys
`FischhoffSlovicLichtenstein1977Certainty` and `Brier1950Verification` from the
unique intake. Local notation C/Y/w_c/m/mu, Rel/Res/L, empirical n_c/m-hat,
g/Q, bin B=h(C), a_B/b_B/v_B/gamma_B, Brier f_ij/E_ij/P_B, odds t and
threshold event A_t, game k/w/b/Z_i/G/q_i. Text E2/E3/E4 denotes experiments,
not the outcome indicators E_ij. No shared registry or bibliography was edited.

The research skill guided primary provenance; a bounded source-delegation
attempt was refused by the thread limit, so no child ran. The PDF skill was
used only to acquire/read primary pages and their source tables. After the
full batch, the author read the actual LaTeX, complete proofs, source note
and bibliography, applying the definition, denominator and interpretation
corrections directly. No review agent, scanner, test, build, manuscript render
or admission check was run.
