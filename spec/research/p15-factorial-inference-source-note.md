# Factorial inference and estimability: NIST 2012 source and authoring record

Date: 9 September 2026. Assigned unit: **ED26-SCI-NIST2012-001**.
The chapter supplies the four selected contrast, replication/blocking,
fractional-alias and causal-interpretation components. The existing P19
four-cell example is retained and extended. This is an authoring return,
not independent acceptance or publication readiness.

## Exact source and version

The selected source is the official compiled *NIST/SEMATECH e-Handbook of
Statistical Methods*. The [publisher's printing page](https://www.itl.nist.gov/div898/handbook/toolaids/pff/index.htm)
states that these PDF files were last updated on **28 June 2012** and are
maintained separately from the current HTML pages.

- [Official complete PDF](https://www.itl.nist.gov/div898/handbook/toolaids/pff/E-Handbook.pdf).
- Local copy: `source/references/nist-sematech-2012/E-Handbook.pdf`.
- Size: **12,811,958 bytes**; **2,333 physical pages**.
- SHA-256: `C0D71C6FC65EB0A44BBB11107799CD36CEAE1C4D81F0D143C439C3D1849EADDA`.
- Embedded creation timestamp: 27 June 2012, 14:00:17, UTC-04:00.
- Embedded modification timestamp: 28 June 2012, 11:06:11, UTC-04:00.
- Producer: Acrobat Web Capture 10.0. The first-chapter metadata title
  does not mean this complete eight-chapter file contains only EDA.

The publisher printing page is also captured locally as
`source/references/nist-sematech-2012/publisher-printing-page.html`, SHA-256
`B4796F8F0A77F726B242BBE4F57DDF584F459538A70D4A798B3DCD0AF50E9540`.
The HTTP resource modification date was in 2025; it was not substituted for
the embedded 2012 edition/capture evidence. An initial default-client request
returned 403; a normal browser-compatible Accept/User-Agent request downloaded
the public PDF. No access challenge or certificate verification was bypassed.

The research and PDF skills guided acquisition, exact version identification,
source-text reading and source-image inspection. No manuscript PDF was built
or rendered.

## Complete selected reading

I read all selected physical pages **1300-1352**, plus the design-selection
context at 1297-1299 and the next-section heading at 1353 to establish the
end boundary. The selected page footers preserve capture timestamps on
27 June 2012, from 14:23:40 through 14:24:00.

| Section | Physical pages | Retained source scope |
| --- | --- | --- |
| 5.3.3.1 | 1300-1302 | Completely randomized designs, balance, two randomization counts, twelve-run order, one-factor mean model and estimates. |
| 5.3.3.2 | 1303-1306 | Complete blocks, nuisance-factor treatment, all twelve wafer/dosage/furnace cells, crossed-factor counts and additive estimates. |
| 5.3.3.2.1 | 1307-1312 | Latin-square assumptions, information limits and all three displayed 3-, 4- and 5-level matrices. |
| 5.3.3.2.2 | 1313-1316 | All three Graeco-Latin matrices and their factor roles. |
| 5.3.3.2.3 | 1317-1319 | Both Hyper-Graeco-Latin matrices, the absent three-level case and all factor roles. |
| 5.3.3.3 and 5.3.3.3.1 | 1320-1323 | Full-factorial run counts, standard order, cube, product-column matrix and the complete replicated response table. |
| 5.3.3.3.2 | 1324-1328 | Polishing settings, sixteen replicated rows, randomized order and nineteen-run center schedule. |
| 5.3.3.3.3 | 1329-1331 | Alternate-corner blocks, interaction/block alias and within-block execution. |
| 5.3.3.4 through 5.3.3.4.3 | 1332-1341 | Both half fractions, the eight response values and their fractional contrasts, all generator/alias steps, resource example and thirteen-run schedule. |
| 5.3.3.4.4 | 1342-1347 | Three eight-factor specifications, defining words, complete two-factor alias patterns, relabeling, resolution and aberration distinctions. |
| 5.3.3.4.5-5.3.3.4.7 | 1348-1352 | Screening purposes and assumptions, notation correspondence and all 29 catalogue specifications. |

The 2012 PDF's source pages 1319 and 1345-1346 were also inspected as
images where the compact matrix, alias text and generator diagram needed
confirmation. Poppler reported unavailable source Symbol/ArialUnicode fonts;
the original embedded mathematical images and numerical tables supplied
the needed confirmation. The images in `tmp/pdfs/p15-factorial-nist/`
are source-reading evidence.

Compact row/column grids retain every run of all eight square examples:
the encoding from a cell to the original full run row is stated explicitly.
The polishing and fractional schedules likewise state all rows through a
standard-order formula and exact run-index sequence. The eight-factor
generator equations and standard-order formula specify each of the 32
rows without introducing an arbitrary sample of them. All 29 entries of
Table 3.17 are retained. The repeated cube figures are combined in one
explicitly labeled native diagram with the same vertex and parity data.

The compiled selected sections refer outward to chapter 7 ANOVA, Box-Hunter-
Hunter, individual Dataplot design files and John's nonregular 48-run design.
Those references remain identified as referrals. They are not additional
matrices embedded in the selected 53 pages and have not been falsely
identified as acquired 2012 bodies. No universal minimum-aberration
classification theorem is claimed from the catalogue: the chapter proves
the two explicit word-count comparisons and preserves the catalogue as an
attributed source selection.

## Corrections applied directly to the written mathematics

1. **Hyper-Graeco-Latin 5-by-5:** The compact source grid at physical page
   1319 prints E31 in row 3, column 4. The full numerical run table assigns
   blocking levels 1 and 3 and treatment 5 to that cell. The correct cell
   is **E13**. The written grid uses E13 and satisfies every required pairwise
   balance condition.
2. **Alternative eight-factor design:** Its defining word 2467 entails
   **27 = 46**. The source's page 1345 list of five supposedly clear
   interactions and count of 23 aliased interactions are incorrect.
   The complete calculation gives clear pairs **12, 14, 23, 34**, with
   **24** of the 28 two-factor interactions aliased. The body and proof
   contain these corrected counts and all eleven alias groups.
3. Source role/level slips in the Graeco-Latin and Hyper-Graeco-Latin
   explanatory lists are resolved against the full numerical tables:
   there is one treatment factor, with three or four nuisance factors,
   and the four-/five-level examples have four/five levels. The printed
   run matrices and their actual assignments determine the reconstruction.
4. Orthogonality gives uncorrelated estimators under the stated covariance
   model; it is not a guarantee under arbitrary heteroskedasticity or
   dependence. Fractional main-column contrasts estimate alias sums unless
   the competing coefficients are restricted. Resolution II can still
   estimate selected row-space functionals; it is not universally useless.

The source's polishing table labels the third setting “Depth” and reports
cm/sec for its unit. That physical-unit interpretation cannot be repaired
from the design table alone. The chapter retains its exact numerical
coordinate scale for the coding calculation; the original unit label is
preserved here and in the source PDF rather than silently changed to a
different physical quantity. No operational polishing prescription is made.

## Four component outcomes

**C01:** The original hypothetical cell means `(4,0,0,2)` and both opposite-
sign comparisons remain. The chapter derives the conditional effects,
equal-weight main effects, difference of differences 6, factorial interaction
effect 3 and coded coefficient 3/2. It supplies the full four-row matrix,
explicit contrast weights and a missing-cell nonestimability case.

**C02:** Full proofs supply the row-space criterion, least-variance linear
estimation, residual information, normal-model Student intervals and joint
F tests, pure error versus lack of fit, repeated-measurement clustering,
complete-block estimates, all square-design ranks and saturated cases.
Center rows are treated using the enlarged matrix: centers in both blocks
can separate an additive block effect from the corner triple interaction,
while centers alone do not separate individual square terms or the
`x3 = x1 x2` alias.

**C03:** The regular-fraction proof uses an affine binary system and proves
the character-average identity, signs, cosets, alias sums and run count.
Both half fractions, all original eight-factor examples and their full
two-factor alias lists are supplied. The resolution proof also gives the
37-column rank bound that requires at least 64 runs for an eight-factor
regular design with resolution at least V.

**C04:** The finite assignment estimator has an explicit unbiasedness and
variance derivation. It uses the actual assignment probabilities, rather
than treating blocking or randomization as random sampling. The finite
causal counterexample gives two mechanisms with the same complete
assignment surface but different interventions on reflection. Stable
versions, consistency, interference, missingness, compliance and transfer
remain distinct assumptions, matching the actual P19/P16 interfaces.

## Author checks and handoff

The actual P19 experiment, P15 finite-expectation and Student-inference
interfaces, and P16 intervention/identification definitions were read.
The complete newly written body and annex received an author read-through;
the subsequent local fixes were read in context. These are author checks,
not independent reviews.

`tmp/pdfs/p15-factorial-nist/nist-author-calculations.py` records finite
source-matrix and exact rational arithmetic. Its JSON output confirms all
eight square matrices have pairwise balance; their residual dimensions
are 2, 6, 12, 0, 3, 8, 0 and 4. It computes both eight-factor alias
patterns, verifies the relabeling group equality and reproduces both
response examples. The replicated table has pure-error sum of squares 5,
variance estimate 5/8 and factorial-effect variance estimate 5/32. This is
a calculation of actual mathematical examples, not a software test suite
mirroring manuscript prose.

Assigned manuscript artifacts are:

- `handbook/parts/p15/factorial-inference-and-estimability.tex`
- `handbook/annex/p15/factorial-inference-and-estimability.tex`
- `handbook/bib/intake-p15-factorial-inference.bib`
- `handbook/registry/symbols-intake-p15-factorial-inference.csv`

The result has thirteen reciprocal result/proof groups. The source intake
introduces `NISTSEMATECH2012DOE`; the symbol intake records local matrix,
factor, word and assignment roles. The lead owns driver routing and canonical
merging. No shared driver, canonical bibliography, symbol registry or
existing P19/P16 content was edited. No manuscript build, render or
independent review was run. All four selected authoring components are
supplied; independent source/mathematical/publication admission remains open.
