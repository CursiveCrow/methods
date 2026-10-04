# Sequential collection and stopping of evidence: source and authoring record

Date: 1 October 2026. Unit: `ED26-METHOD-sequential-evidence`, selected from
`spec/coverage/edition-2026/additional-method-units.jsonl`. The source version
is Abraham Wald, “Sequential Tests of Statistical Hypotheses,” *The Annals
of Mathematical Statistics* 16(2), June 1945, 117–186,
DOI [10.1214/aoms/1177731118](https://doi.org/10.1214/aoms/1177731118).

## Actual primary acquisition

The supplied legacy download URL and the publisher's current `.pdf` URL
returned HTTP 200 HTML bot-block pages through shell/web retrieval. Those
responses were not saved or counted as the paper. Crossref's publisher record
confirmed the exact title, publication and legacy source URL; OpenAlex returned
only the same publisher locations, not an alternate readable body. The local
Calibre filename search found no Wald copy. The accessible SciSpace record
conflated the later 1992 reprint with the original; it was not used as evidence
for the original body.

Normal Edge browser access to the
[publisher article page](https://projecteuclid.org/journals/annals-of-mathematical-statistics/volume-16/issue-2/Sequential-Tests-of-Statistical-Hypotheses/10.1214/aoms/1177731118.full)
showed “Open Access,” June 1945, volume 16(2), 117–186 and “70 PAGES.” Its
visible **DOWNLOAD PDF** link was
`https://projecteuclid.org/journalArticle/Download?urlId=10.1214%2Faoms%2F1177731118`.
That ordinary browser download succeeded without sign-in, payment, CAPTCHA
handling or security changes. The file was copied into the authorized
manuscript source folder, retaining the browser download.

| Property | Verified live evidence |
| --- | --- |
| Preserved PDF | `source/references/wald-1945-sequential/wald-1945-sequential-tests.pdf` |
| File size | 5793822 bytes |
| SHA-256 | `3E837AC2348B81AF1F29634897967364E614B426767BD2C272C55001C8B5538B` |
| PDF pages | 70; physical page 1 is printed 117, physical 70 is printed 186 |
| Source identity | Title, A. Wald, Columbia University and original contents on printed 117; references on printed 186 |
| PDF format | 1.3; not encrypted; no forms or JavaScript |
| Readability | Original image-only facsimile; extraction has only the digitization footer on the first page |
| Derivatives | `source/references/wald-1945-sequential/pages/page-01.png` through `page-70.png`, rendered at 120 dpi |

All source pages were rendered. The author read the complete selected original
extent **Part I §§1–4, printed pp. 122–157**, including every displayed
equation and Tables 1–3, plus printed pp. 117–119 for identity/introduction,
the Part II boundary at 158, and references at 186. This does not claim that
the remaining Part II body was read or transcribed. Later reprints, the
1947 book and the 1948 Wald–Wolfowitz optimality paper are separate versions.
Public reading access to the facsimile is not represented as republication
permission; the chapter uses independently worded mathematics and proofs.

## Actual output and ownership

- Body: `handbook/parts/p15/sequential-evidence.tex`.
- Annex: `handbook/annex/p15/sequential-evidence.tex`.
- Bibliography intake: `handbook/bib/intake-p15-sequential-evidence.bib`.
- Symbol intake: `handbook/registry/symbols-intake-p15-sequential-evidence.csv`.

The author owns only those files and this source capture/record. Root owns
part routing, canonical bibliography and symbols, named-scope bindings,
coverage projection and final integration. No existing Huber or Durrett
chapter was edited, and the author spawned no children for this assignment.

The actual prerequisite passages were read in
`optional-stopping-and-random-walks.tex`, including the integrable-time
condition, first and second Wald identities and restarting; and in
`robust-hypothesis-testing.tex` and its annex, including the affinity stopping
proof, robust error comparison, bounded-excess argument and asymptotic.
The distinct unbounded/singular endpoint setting and original information
lower bound were read in `robust-sequential-endpoints.tex`. Those are
substantial existing proofs and are not credited as new 1945 source writing.

## Five requested components

| Component | Actual authored evidence |
| --- | --- |
| C01: continuation/terminal decisions and information | `def:p15-se-model`, `def:p15-se-procedure`, `def:p15-se-sprt`: observed history, measurable decision regions, first terminal stage, nontermination and actual versus target errors; an independent seed extension is explicit |
| C02: likelihood ratio and boundaries | Original upper `A`, lower `B`, equality-stops convention, their distinct logarithms, posterior-odds motivation, nominal and conservative choices |
| C03: stopping/error guarantees | Full affinity proof under distinct simple laws; block exit proof for any nonzero finite i.i.d. score; stopped-history density inequalities; the actual joint-density extension; explicit nominal-threshold counterexample |
| C04: finite/unbounded sampling and approximation | Wald identity with absolute integrability; zero-drift second moments; mean/exponential excess bounds; binomial and normal extrema; exact lattice/root and absorption calculations; complex stopped transform; consistently normalized boundary approximation; continuous density normalization; deadline and forced-cap errors; original information/zero-overshoot efficiency |
| C05: repeated fixed threshold versus sequential design | `thm:p15-se-repeated-fixed`: exact `1-(1-alpha)^M`, calculated `0.6415140776` at twenty independent five-percent inspections, unbounded value one, contrasted with the proved entire upper-exit error of a calibrated SPRT |

## Source distinctions and direct repairs

1. Original §3.1 uses `A` as upper likelihood ratio and `B` as lower likelihood
   ratio. Their logarithms are separately declared. The prior/posterior
   motivating thresholds are not substituted for frequentist error calibration.
   The initial general construction `0 < B < A` is retained. The termination
   and dependent-history statements cover those general boundaries; the
   subsequent calibration/operating calculations explicitly use the source's
   practical `B < 1 < A` regime. Degenerate zero scores are handled correctly
   on both types of boundary interval.
2. Original §3.2 proves `A alpha' <= 1-beta'` and
   `beta' <= B(1-alpha')`. The source's Figure 1 error quadrilateral is
   preserved mathematically by its four vertices and derivation.
3. Original §3.3 gives practical approximate thresholds
   `(1-beta)/alpha` and `beta/(1-alpha)`. Its actual guarantees are the coupled
   ratios, separate inflated bounds and `alpha'+beta' <= alpha+beta`.
   A one-step Bernoulli example proves individual nominal failure:
   null success mass `0.11`, alternative success mass `0.99`, boundaries
   `9` and `1/9`, actual errors `0.11` and `0.01`.
4. The stopped-sum proof states `E|z| < infinity` and `ET < infinity` before
   interchanging the infinite sum. The source's `EZ_T / Ez` division is not
   applied at zero mean. The zero-mean finite-variance case has its full
   second-moment derivation using the existing proved Durrett identity.
5. Source §3.4's nonzero exponential root is assumed where needed and proved
   for the particular binomial/normal families. A zero-drift finite score may
   have only the root zero; no nonexistent root is introduced. Conditioning
   extrema omit zero-probability conditioning events. One-sided inactive
   directions are treated explicitly.
6. The finite lattice determinant retains its nonzero-determinant condition.
   A separately proved absorption-matrix procedure handles singular root
   matrices and gives a finite-prefix remainder certificate. Finite approximating
   grids are not claimed to converge automatically across boundary atoms.
7. Original §3.5 and §4.2 normal extrema are proved using conditional normal
   variance and tail-ratio derivatives. No unread Birnbaum proof is imported.
8. Source §4.4's stopped transform is proved for bounded and unbounded finite
   scores. The proof establishes terminal absolute integrability from the
   one-step exponential moment and finite expected exit, rather than adding
   it as an unexplained assumption. The smaller-modulus local extension has
   its explicit surviving-tail condition.
9. `E exp(tau T)` is an exponential transform; imaginary arguments give the
   characteristic function, and derivatives then introduce powers of `i`.
   The boundary approximation consistently uses its own approximated decision
   weight, ensuring that its conditional transforms are normalized at zero.
   The normal square-root branches and vanishing determinant conditions are
   explicit. The continuous one-sided density is normalized and its moments
   proved; no discrete-to-continuous convergence/error bound is fabricated.
10. The full two-boundary continuous series is **cited to the separate 1944
    cumulative-sum paper by the 1945 source**, not printed there. Its historical
    derivation is not claimed as read or reproved. The present selected method
    gives the original citation boundary, transform mechanism and one-sided
    approximation, with exact finite-horizon calculations available independently.
11. Source §§4.5–4.6 give exact marginal-score inclusions and cap-error additions.
    Their normal expressions are exact for normal scores. The table passages
    reuse `A,B` for logarithmic quantities; the chapter retains distinct ratio
    and log notation. Nominal substitution in the truncation base error is
    explicitly approximate. The calculated symmetric 1000-observation example
    distinguishes nominal `0.094456` from the conservative CDF-expression
    upper bound approximately `0.097088`.
12. Original §4.7 proves the information bound and exact attainment when
    overshoot vanishes. The unbounded competitor argument is supplied by
    actual finite-horizon truncation and convergence of its errors. The original
    general exact-optimality conjecture remains distinct; no 1948 result is
    attributed as a 1945 proof. A bounded-excess comparison to the information
    lower bound is fully proved as an additional explicit result.

## Statement/proof matrix

Every result below has its matching `annex:p15.se.<suffix>` proof and body
back-reference. Actual suffixes are listed to keep the record directly usable.

| Body result | Annex suffix | Content |
| --- | --- | --- |
| `thm:p15-se-posterior` | `posterior` | Odds and posterior terminal boundaries |
| `thm:p15-se-termination` | `termination` | Simple-law and third-law stopping |
| `thm:p15-se-errors` | `errors` | Exact coupled errors and safe thresholds |
| `thm:p15-se-dependent` | `dependent` | Correct dependent-history density extension |
| `thm:p15-se-nominal` | `nominal` | Nominal bounds and explicit failure |
| `thm:p15-se-mean` | `mean` | Stopped mean and conditional excess bounds |
| `thm:p15-se-zero-drift` | `zero-drift` | Centered second-moment case |
| `thm:p15-se-oc` | `oc` | Exact exponential mean and operating bounds |
| `thm:p15-se-lattice` | `lattice` | Root equations and conditional determinant formula |
| `thm:p15-se-finite-recursion` | `finite-recursion` | Exact finite-state absorption and moments |
| `thm:p15-se-binomial` | `binomial` | Bernoulli root/excess formulas |
| `thm:p15-se-normal` | `normal` | Normal root/excess/tail-ratio calculations and fixed-size comparison |
| `thm:p15-se-transform` | `transform` | Full stopped transform and approximation-system algebra |
| `thm:p15-se-continuous-density` | `continuous-density` | Approximation density normalization, transform and moments |
| `thm:p15-se-deadline` | `deadline` | Exact endpoint inclusion and normal CDF bounds |
| `thm:p15-se-truncation` | `truncation` | Error additions at a forced cap |
| `thm:p15-se-repeated-fixed` | `repeated-fixed` | Exact repeated-inspection failure |
| `thm:p15-se-information` | `information` | Original finite/unbounded information lower bounds |
| `thm:p15-se-no-overshoot` | `no-overshoot` | Original ideal attainment and bounded cost slack |

## Verification and integration standing

The original source pages and actual new LaTeX were read by the author.
The arithmetic for the nominal failure, repeated-inspection error, normal
sample saving and all three original normal-table parameter pairs was
recomputed directly. The independent-inspection example does not assume
independence of overlapping cumulative looks. No prose software tests were
written or run. No manuscript build, render, independent review or admission
was performed in this authoring block.

The unique intake has one bibliography key and 66 symbol rows with math glyphs,
nonempty macros and actual first-use anchors. Named scopes are
`P15 sequential evidence` and `P15 sequential evidence annex`. Root must bind
them to the exact body and annex, route those two files, merge the intakes and
update the authoring projection. The new unit does not replace or claim the
separate Huber 1965 robust or Durrett 2019 stopping presentations.
