# Posterior predictive model criticism: authoring and source record

Date: 9 September 2026. Unit: `ED26-SCI-GelmanMengStern1996-001`.
This is the author's source and progress record, not independent admission.

## Source identity and reading

The complete original main article is Andrew Gelman, Xiao-Li Meng and Hal
Stern, *Posterior Predictive Assessment of Model Fitness via Realized
Discrepancies*, **Statistica Sinica 6 (1996), 733–760**, ending on printed
page 760 after the references, three institutional addresses and received/
accepted dates, immediately before David Draper's comment. The publisher's
[landing page](https://www3.stat.sinica.edu.tw/statistica/j6n4/j6n41/j6n41.htm)
and [PDF](https://www3.stat.sinica.edu.tw/statistica/oldpdf/A6n41.pdf)
use the wider article-with-discussion pagination. The PDF is 76 physical
pages and ends on printed page 808. Neither the comments nor rejoinder
are silently merged into this unit's main-article presentation.

Held source: `source/references/gelman-meng-stern-1996/A6n41.pdf`.
Size: **1,056,743 bytes**. SHA256:
`B375989DB18AB5E693B5FD7907C84470FF9DD4917EEE8A1E64F0C845BE684D72`.
Downloaded directly from the publisher with Python's ordinary HTTPS
verification after Windows Schannel requests failed with no available
credentials. TLS verification was not disabled. No paid access was used.

Read the complete original main-article text, sections 1.1–4.3,
acknowledgements, all references and author addresses, on physical pages
1–28 / printed pages 733–760. Two extraction outputs preserve the reading:

- `main-article-plain.txt`, SHA256
  `F261CA361463D8A7C5253350BC553C8B421377D79FD6F82DA4B6D07AED608B41`.
- `main-article-pages.txt`, layout extraction, SHA256
  `40010E23D36A2C374A1E04A519CF9665B1C095FD1A7243496A5A68E6061D9D09`.

Both extraction files include the beginning of Draper's comment because
the boundary is within page 760; this is retained boundary evidence, not
allocated main-article content. The layout extractor misses rotated text
and produces diagram artifacts. The source figures were therefore also
read visually: Figures 1a–1c, 2–10 and Tables 1–3, with a separate larger
view of printed page 751. Source-only images are under
`tmp/pdfs/p15-posterior-predictive-source/`. The table cell for motor=2,
cry=1, fear=1 is **15**, not the separated digits suggested by extraction.
No manuscript was rendered for this assignment.

The research skill was fulfilled by this delegated source investigation
and this one durable note. The PDF skill was used for source extraction
and source-figure reading; no PDF was authored or edited.

## Written files and component allocation

The body is `handbook/parts/p15/posterior-predictive-model-criticism.tex`;
its matching annex is `handbook/annex/p15/posterior-predictive-model-criticism.tex`.
At the initial authoring checkpoint they contained 624 and 311 lines, respectively, with
nine reciprocal theorem/annex proof pairs. The unique intakes are
`handbook/bib/intake-p15-posterior-predictive.bib` (one source record) and
`handbook/registry/symbols-intake-p15-posterior-predictive.csv` (26 rows).
All drivers, shared style and canonical registries remain the lead's property.

| Required component | Actual authored treatment |
| --- | --- |
| C01: prediction, comparison and criticism | Opening reference description; explicit links to the existing posterior and model-odds results; application and interpretation sections |
| C02: joint discrepancy construction and computation | `def:p15-ppc-model`, `def:p15-ppc-discrepancy`, `thm:p15-ppc-joint`, reduced-discrepancy definition, simulation method and theorem, pivot and normal-calibration theorems |
| C03: prior, posterior and mixed replication | `sec:p15-ppc-replication-choices`; auxiliary conditioning, hierarchy kernel, exact normal-maximum theorem and proof |
| C04: informative and uninformative discrepancies | Exact normal mean check equal to one half; exact Gaussian fitted-residual comparison; gamma–Poisson totals and multinomial conditional dispersion; full data and reported checks in the mortality and infant applications |

The Gaussian difference-of-chi-squares proof, truncated-normal formulas,
gamma–Poisson calculation, constrained-posterior normalization and generic
Dirichlet augmentation are full editorial derivations. They are not
presented as literal proofs printed by the 1996 authors. The source's
non-Gaussian chi-square calculations retain their explicit approximate
status and do not acquire an invented uniform-error theorem.

## Complete main-article coverage reading ledger

| Source extent | Material retained in the authored treatment |
| --- | --- |
| 1.1–1.3, pp.733–737 | Fitness versus truth; sensitivity and substantive plausibility alongside predictive fit; constrained-Poisson tomography with all quoted count and discrepancy scales, named failure mechanisms and its motivational-only role |
| 2.1, pp.737–739, Figure 1 | Auxiliary statistics; same-parameter predictive kernel; statistic tails; pivotal special case; three different replication structures |
| 2.2, pp.740–741 | Realized discrepancy, shared parameter in the pair, minimum and posterior-average statistics and the refitting difference |
| 2.3, pp.741–742 | Posterior draws followed by replication, paired scatter and diagonal, reuse for multiple discrepancies, conditional averaging, and the extra work required by optimization or posterior refitting |
| 2.4, pp.742–744 | Pearson discrepancy; conditional chi-square approximation; average shift; difference of independent chi-squares; 250/200/80 example; dependence on a nonuniform prior |
| 3.1–3.2, pp.744–750, Table 1, Figures 2–7 | All 30 age/exposure/death records, constraint and rate model, Poisson approximation, likelihood and Pearson optimizations, source simulation procedure, posterior curves versus noisy replications, 23.0/43.4 and 21.1/39.6 references, tails 0.16/0.10/0.063, later-age localization, screening and prior-geometry explanations |
| 3.3–3.4, pp.750–754, Tables 2–3, Figures 8–9 | All 36 count cells, 93 infants and measured ages, mixture and within-class independence, four source deviance/dimension rows, Dirichlet blocks, augmentation and label roles, multimodality, two-class and independence-model checks and their limits |
| 4.1, pp.754–756, Figure 10 | New parameters versus shared parameters versus shared hyperparameters; proper-prior requirement; n=100, mean 5.1, maximum 8.1, uniform half-width 10^5 example and 149/1000 reported exceedances |
| 4.2–4.3, pp.756–758 | Prior centers and concentration; weak/strong sensitivity distinction; no established identification of prior versus likelihood defects; discrepancy choice tied to the intended inference; total/median contrast; descriptive multiple checks versus error-controlled decisions; defects without a replacement model |
| pp.758–760 | All references and article boundary read; referrals remain referrals, with no claim that their full bodies were acquired |

## Corrections and source-specific qualifications

1. On p.743, a sentence infers that the realized-discrepancy tail is
   larger from its larger reference variance. That is not a universal
   tail order. The body states the correct absence of a universal order;
   the annex proves a strict counterexample at residual zero and, by
   continuity, at some positive residuals. Both reference formulas and
   the article's intended large-residual illustration are preserved.
2. On p.755, the normal posterior is written without the truncation from
   the finite uniform prior. The active theorem gives the exact truncated
   law and proves the large-width limit. The source's simulation is
   reported as the effectively untruncated approximation.
3. On p.736, large exposure is said to force exact interpolation. The
   body does not generalize this to every nonnegative inverse problem;
   suitable interior geometry is needed, and boundary true means do not
   earn that conclusion merely from nonnegativity.
4. Fractional insurance exposures are not fractional binomial trial
   counts. The active construction uses the source's Poisson exposure
   approximation. The unbounded nonnegative rate region and its bounded
   probability-rate variant are stated separately; their posteriors are
   not asserted identical. The main article supplies no numerical upper
   truncation bound for the fitted prior.
5. The minimum-discrepancy mixture histogram has conflicting sample
   counts: p.752 prose says 500; Figure 8 on p.753 says 1,000. The body does
   not choose an unverified count for that histogram. Its mean, variance
   and tail remain attributed source results. The realized tail 0.74 is
   explicitly reported with 500 Monte Carlo draws on p.754.
6. Comparing 0.10 with 0.063, or 0.024 with 0.058, does not prove which model
   component failed. The original authors themselves call for further
   validation; the active manuscript preserves that uncertainty.
7. The source's descriptive multiple-check practice does not establish
   familywise error control for a selection or decision rule. The body
   gives that qualification directly.

## Author checks and remaining work

The author read through the complete written body, annex and intakes,
checking the mathematical transitions and source numbers. Direct arithmetic
from the transcribed infant table gives total 93 and independence deviance
**48.760804525066106**, matching the reported 48.761. The conditional
dispersion tail is exactly **4^-19 = 3.637978807091713e-12**. The PET
comparison n+2sqrt(2n) is **22887.924521583736**. These are targeted
mathematical calculations, not an independent review or a prose test suite.

The body preserves all selected source examples and their numerical results
as source-reported evidence. It does **not** claim to have reproduced the
original posterior simulations or reconstructed their unprinted random draws.
Exact numerical re-execution of the latent-class study still requires the
specific prior vectors referred to in **Rubin and Stern (1994), Testing in
latent class models using a posterior predictive check distribution,
in Latent Variables Analysis: Applications for Developmental Research,
pp.420–438**. Bounded searches found references and an author CV, not that
chapter's free full body. No substitute hyperparameters were invented.
Any full reconstruction of the source's graphical simulation outputs also
needs the relevant numerical setup and should distinguish newly generated
draws from the original source draws.

The original article's main mathematical constructions and the four selected
component treatments are drafted with complete proofs of the stated results.
The numerical reproduction dependency above remains open. Lead integration,
canonical intake merger, the consolidated independent reviews and final
manuscript build/output checks remain. No publication or full-unit admission
is claimed, and the original task has not been reduced to the finite count
illustration.

## Written artifact hashes at the initial authoring checkpoint

| Artifact | SHA256 |
| --- | --- |
| Body | `604D56DE9FBDCE47BFB793446DC9AE3B62E0C9D8B3C5D988A77157703166CEED` |
| Annex | `B5E519340E562EFBFA566EC5906A9F10CDDEF9FB7D020F418685DB90088C4BFF` |
| Bibliography intake | `826D34FED5E72078AA9BF4D289588F3493C24C66A3E36B623A892732D05D9550` |
| Symbol intake | `C509236670C349A06669C75B54384C176C2F1D203F11AA705C14FF1E8EDC95E8` |

## Symbol-intake integration repair

At the lead's request, all 26 mathematical glyph cells now use explicit
inline math delimiters, and every macro/display-code cell contains the
actual TeX spelling. The precedence value is `n/a` throughout. Each scope
now names its actual `sec:p15-...` chapter or section label, verified in
the current body. Roles, notes, typed distinctions and first-use labels
are preserved. This repair changes only the symbol intake and this note.
It does not change manuscript mathematics or claim a build result.
The intake was parsed as CSV: 26 records, zero empty macro cells, eight
distinct existing scope labels and one precedence value, `n/a`.

## Reproduction continuation: bounded source checks

The lead resumed the exact Rubin–Stern acquisition and remaining calculation
work later on 9 September 2026. The selected work remains **Rubin and
Stern (1994), chapter 17, pp.420–438**, not the related 1998 sample-size
paper or the separate 1994/1995 infant-temperament articles.

The following current checks did not supply the chapter body:

| Route | Actual evidence and outcome |
| --- | --- |
| Stern's [author page](https://ics.uci.edu/~sternh/) | Current HTML captured; links to the author's CV and book site, with no chapter PDF link |
| Stern's [November 2025 CV](https://ics.uci.edu/~sternh/hscv_full.pdf) | Full 27-page PDF acquired; publication item 11 on printed page 7 identifies the exact 1994 title, editors, publisher and 420–438 extent; the 1998 article is separately listed as item 25 |
| Rubin's Harvard-hosted CV | Indexed primary record identifies chapter 17; direct file request returned HTTP 403 |
| [OpenLibrary edition OL1084246M](https://openlibrary.org/books/OL1084246M) | Edition JSON acquired: Sage 1994, xii+458 pages, ISBN 0803953305/0803953313, OCLC 30033715 and InternetArchive identifier `latentvariablesa0000unse` |
| [InternetArchive item metadata](https://archive.org/metadata/latentvariablesa0000unse) | Metadata acquired. PDF, ordinary EPUB and OCR text/XML are explicitly marked `private=true`. Public listed alternatives are encrypted loan formats and catalog/scanning metadata. No restricted body was retrieved |
| [Google Books ISBN record](https://books.google.com/books?vid=ISBN0803953305) | HTML acquired; resolves its catalog identity to `mNMPAQAAMAAJ`, says `No eBook available`, and offers print sellers/library routes. No readable chapter supplied. The Books API ISBN query separately returned HTTP 429 |
| Publisher and repository searches | Exact-title and ISBN searches found the official Sage book-review/catalog records, author citations and later methodological papers; none returned the selected chapter body |
| Local literature library | Filename inventory under `C:/Users/Crow/OneDrive/Library` and manuscript source/acquisition directories found no matching latent-variables volume or Rubin–Stern chapter |

The full acquisition responses and their hashes are in
`tmp/pdfs/p15-posterior-predictive-source/rubin-stern-acquisition/receipt.json`
and `receipt-secondary.json`. The public InternetArchive metadata hash is
`dd512466b8262b699b3ead6fdff378e4ff4bf1faa1e568601ee9943de1f66095`.
The acquired Stern CV is 362,736 bytes, SHA256
`a3be1f8b213e9d115b1013da435179f281d71321f86e3fc963effbe4c4ac60b6`.
An inspected DOI landing page for the separate Behaviormetrika article,
`10.2333/bhmk.21.1`, is not the requested book chapter and was not used
to replace its prior specification. No author was contacted or new loan
initiated. These are bounded failures to acquire, not a claim that no
accessible copy exists anywhere.

## Reproduction continuation: actual mathematics and calculations

The body and annex now add `thm:p15-ppc-mortality-fit` and its complete
reciprocal proof. It supplies a nonnegative-increment parameterization of
all positive increasing convex rates, proves strict convexity and unique
attainment for the printed strictly positive death counts, and proves the
first-order optimality conditions. Likelihood and Pearson minimization
remain distinct. The active worked calculation now uses the exact printed
Poisson objective and data, with its independently obtained values:

| Calculation | Result |
| --- | --- |
| Pearson discrepancy at the Poisson likelihood optimum |30.685450871874796 |
| Minimum Pearson discrepancy |29.343902008431236 |
| Gaussian minimum-discrepancy tail, n=250/k=200/residual 80 |0.00448265656557319 |
| Gaussian realized-discrepancy tail for those inputs |0.1581311101463389 |
| Normal maximum upper tail, n=100/mean 5.1/maximum 8.1 |0.13129402617890526 |

The mortality minima were computed from four feasible starting coefficient
vectors, with all runs returning the same objective to displayed precision.
For the selected fits, maximum projected-gradient residuals were about
5.29e-7 for likelihood and 1.72e-9 for Pearson. These are floating-point
optimization diagnostics, not interval certificates. The source's stated
30.0 at its likelihood estimate on p.745 does not match this recomputation;
that historical figure remains recorded here, while the active worked
calculation states the result for its explicitly specified objective.
The source's 29.3 minimum agrees after rounding. Its simulated reference
summaries remain explicitly source-reported results.

The Gaussian difference tail was integrated in separate ranges around the
chi-square density's mass; an unsplit infinite-interval quadrature can miss
that mass and is not reliable evidence. The final quadrature error estimate
is about 2.03e-14. The normal-maximum integral was taken over standardized
posterior coordinates from -12 to 12, with omitted normal-tail bound
3.553e-33 and quadrature error estimate 1.23e-13. The solver estimates are
not rigorous floating-point error bounds. The finite uniform-prior
truncation is negligible at the stated width; numerical underflow of its
tail to zero is not interpreted as exact zero. The source's 149/1000
exceedance fraction is about 1.66 independent-draw Monte Carlo standard
deviations above the computed probability.

The reproducible calculation is
`tmp/pdfs/p15-posterior-predictive-source/recompute-printed-examples.py`,
using NumPy 2.3.5 and a task-local SciPy 1.18.1 installation. Its complete
inputs, optimizer outputs, formulas, numerical results and script hash are
preserved in `printed-example-calculations.json`, SHA256
`50A1E4E3CA616FA04B240395080233307300C5FD1D9696B6DFC0AFAF18011C6F`.
This is numerical manuscript authoring; no independent review, manuscript
build/render or prose-mirroring software tests were run.

**Remaining:** the original mixture posterior-predictive simulation is still
open because the selected Rubin–Stern Dirichlet vectors have not been
obtained. Neither the printed-input calculations nor the generic conjugate
derivation retires that obligation. The 500/1000 source inconsistency remains
as recorded above. The already-merged 26 symbol rows are untouched; four
new rows are isolated in
`handbook/registry/symbols-intake-p15-posterior-predictive-followup.csv`.
Only that delta needs another canonical merge.

Current body: 675 lines and 10 theorem/proof pairs, SHA256
`16019E6F2E5731A713D0E93B3D16E8DA835DEE39266C175CF833A3B69E798367`.
Current annex: 360 lines, SHA256
`25C781751619515DFE2691E7D20679DB16818F0984425734CFBE4345A8425173`.
New symbol delta SHA256:
`2F63A9F7C3E5D9AFD7CE3BBDDB2D55546CE5A79067438BDAB3FBB8D19FC9E216`.

## Public-source continuation, 1 October 2026

This bounded continuation read the complete existing acquisition record and
both earlier receipts before selecting new routes. It checked alternate
Internet Archive catalog records and a newly identified Harvard technical-report
lead. It did not repeat the unchanged author-CV, publisher, Google Books or
restricted-file requests from the earlier block.

The [Internet Archive title search](https://archive.org/advancedsearch.php?q=title%3A%22Latent+Variables+Analysis%22&output=json&rows=25)
returned HTTP 200, 2,041 bytes and exactly one record: the already recorded
`latentvariablesa0000unse`, dated 1994 with xii+458 pages. It supplied no
alternate scan. A separate title/creator catalog query returned zero records.
The earlier item-level metadata still controls the recorded access distinction;
this search result was not treated as a grant to retrieve its private files.

A new indexed reference in the author-hosted
[Gelman–Rubin simulation rejoinder](https://sites.stat.columbia.edu/gelman/research/published/itsim_rejoinder2.pdf)
identifies a Rubin–Stern **1992 Harvard Statistics technical report** under the
same title. The nine-page rejoinder was retrieved into memory: 4,739,298 bytes,
SHA256 `187402b8d65680b7a4c233e19e0004b7b0ab874af5b729c3a0c0a14e499750fc`.
Its scanned pages yielded no machine-readable text with the local extractor,
and the web screenshot request failed. Thus the citation is retained as an
**indexed acquisition lead**, not a claimed reading of the report or verified
equivalence of its contents with the 1994 chapter. A Berkeley-hosted citing
report's download response was empty and supplied no further body evidence.

The public [HOLLIS exact-title search](https://hollis.harvard.edu/discovery/search?query=any,contains,%22Testing%20in%20latent%20class%20models%20using%20a%20posterior%20predictive%20check%20distribution%22&tab=Everything&search_scope=MyInst_and_CI&vid=01HVD_INST:HVD2&lang=en&offset=0)
was read in its browser interface after the ordinary request returned only the
application shell. All twelve displayed result titles were read; they were
citing or related works, with no matching report or chapter. No login or library
request was initiated. The [DASH repository exact-phrase search](https://dash.harvard.edu/search?spc.page=1&query=%22Testing%20in%20latent%20class%20models%22)
was then executed through the repository's own search control. Its final visible
result was **“Your search returned no results.”** That observation is bounded to
the given query and public interface, not a claim about every Harvard holding.

**Outcome:** no qualified complete Rubin–Stern body and no source-verified
Dirichlet vectors were obtained. The exact mixture reproduction dependency
remains open. No prior values, source versions, manuscript claims or canonical
completion records were changed. The source-dependent search ends at this
checkpoint; its useful new lead is the possible 1992 report, whose actual body
and relation to the selected chapter remain unverified.
