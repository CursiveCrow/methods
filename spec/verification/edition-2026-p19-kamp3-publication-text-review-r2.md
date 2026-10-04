# Focused R2 publication-text recheck: P19 and Kamp III.2 Lemma 3

Date: 7 September 2026 Pacific time; review began 8 September at 02:32:49 UTC.
Reviewer: `/root/p19_kamp3_publication_review`.
Repository: `C:\Dev\the-methods-of-reason`.
Owned output: this report only.

## Verdict

**PT-P19-01: PASS, closed at the publication-text scope.** The actual Study 1 predictors now have a source-attributed response-model specification, score identity and units, with unavailable estimation details stated explicitly. The two other assigned reporting changes also pass: the aid-present primary question agrees with its contrast, and the selected Study 2 adjustments are named.

**Kamp Lemma 3 preservation: PASS.** The body is byte-identical to R1. Reversing the annex's single opening-heading command change in memory yields the exact R1 annex hash, confirming that all mathematical content and proof cases remain unchanged.

**Routes, bibliography, canonical notation and generated notation source: PASS at the inspected source-integration scope.** All twenty-one new/updated notation records agree with the reviewed manuscript. PT-PROJ-01, found during this recheck, is now closed after the lead corrected five notes and regenerated both projections; the exact final repair and preservation checks are recorded below. No required repair remains in this assigned publication-text scope.

This is a focused R2 recheck by the R1 publication reviewer, independent of the repair author. No other R2 conclusions were consulted. The named repair note was read as an author/source locator and change-scope record, not accepted as independent verification. The full repaired P19 LaTeX was read directly. No primary PDF was re-read in this publication recheck; exact new source fidelity remains the source reviewer's separate remit. No builds, renders, tests, generators or admission operations were run, and only this report was written.

## Exact reading and identities

| File | Actual R2 reading/check | SHA256 |
| --- | --- | --- |
| `handbook/parts/p19/evidence-methods.tex` | Complete 1–704, including the full new definition and all changed surrounding paragraphs | `F9884A1A9267F1A8940C3C574874C6702B257B359BEC21AD137F642104B9CD12` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma3.tex` | Hash revalidation against the complete R1 reading, 234 lines | `811AAA41E515F647CB6BC252A4AFEF59279B8338A0FBB43BE72DA3E572A29BA3` |
| `handbook/annex/p09/kamp-iii2-lemma3.tex` | Changed heading and proof context 261–288; complete in-memory inverse identity check, 410 lines | `91E5182F2545CDA968E8B13FAB320988CEA3B24FC1E6572271A4EC4B66E53C0E` |
| `handbook/main.tex` | Complete 1–74 | `E9CB5F4EC7A0F0A5A24DAC385B7FC796AE88C2153FD47FD9FD93FA66996D94C7` |
| `handbook/parts/p19.tex` | Complete 1–4 | `A496651705405F4543AABEC440C795E50E310B5B50A6BB1A3BECC68387CBA2D9` |
| `handbook/parts/p09/presentations/n-c-012.tex` | Integrated seam 133–162; prior definitions read in R1 | `016A8D505BB2656F0B67DF72CC54AA9A8F700C22EA84915C9B1DCDBDC1317D87` |
| `handbook/annex/p09.tex` | Complete 1–10 | `9902C575579427D56034D39FB1F7DC8E39ADF979F2CBBF46D0DCC089FC36640E` |
| `handbook/bib/handbook.bib` | Complete relevant entries at 2271–2280 and 6622–6661; exact key search | `716394DAA6C90F1DD84DF53902A8E5A200E8D48870E45CE0382119E0AB32BD8B` |
| `handbook/registry/symbols.csv` | All new/updated records at physical CSV lines 1004–1024, then five encoding repairs reread and exact inverse checked; 1,023 total data rows | `85C3BFB6C05CDF4D4989F2F02FF4AD435791217118AB93715FE2C64EA2521E90` |
| `tmp/edition-2026-p19-kamp3/symbols-tables.tex` | All 21 affected rows, then repaired five rows reread and exact inverse checked; 1,298 lines | `DA50C974E8DA32147726ABBDEFFAD79AFBA457187EFD0283F606639CEEF2FD15` |
| `tmp/edition-2026-p19-kamp3/symbol-index.tex` | All 21 affected rows, then repaired five rows reread and exact inverse checked; 1,024 lines | `67B666B6D1EF07B354AD70CD51ECD22F7FBC3CE9FDF820915985848D98400616` |
| `spec/research/edition-2026-p19-e1-review-repairs.md` | Complete 1–108, as author/source/change lead | `14FEBF7BA473454D89B13172F1DD5325AAEC712E5E7FFCDD827D62B6D7631064` |

The complete contract and conventions previously read in this review context remain unchanged: `spec/EDITION-2026-CONTRACT.md` is `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3`; `handbook/CONVENTIONS.md` is `4293F514072179A5AC95E64FA8D8F37E23FFE2693814A1980E5801BABA5B7242`. The inspected typed-reference style also remains `2411A09B48D5C0A4ADBF583B350D5606CBD1A60C504681F67D52EEC444406C44`.

The previously read P15 and P17 interfaces were rehashed unchanged: finite probability `934D75E81BB2A465B43C5B4F04F3819167A957A692D7E46FE453D3504AE3FAA1`; finite preferences `58CFD946F16A9D068D0D81AF3262E26BBE926F87FFEF45C01CADD72E0DD0927C`. R1's located prerequisite-interface assessment remains applicable to their uses here.

## P19 repair assessment

| Assigned component | Result | Direct manuscript evidence |
| --- | --- | --- |
| Actual response coding and variables | PASS | 368–377 identifies participant/item indices, the five items, the three classified response categories and both binary steps. An intuitive error records zero at the first step and a missing second step; it is not represented as two observed failures. |
| Item/person model and probability structure | PASS | 379–407 defines real person effects, item intercepts, the logistic function and separate step probabilities, followed by the three response probabilities. Calculation is explicitly conditional on reaching the second step. The shared person effect across items, ten item-by-step intercepts, Model 1/Model 2 distinction and reported latent-effect scales/correlation are stated. |
| Actual regression-score identity | PASS | 409–416 identifies conditional modes of the fitted person-effect distributions and gives separate symbols `\widehat r_i` and `\widehat c_i^{\rm mod}`. These are explicitly distinct from raw response proportions, response probabilities and correct-answer counts. The coefficient-table introduction at 466–471 maps its rows to those exact symbols. |
| Units and standardization | PASS | 418–428 states the log-odds deviation scale and the odds multiplier `exp(1)` for a one-unit effect increase at fixed item. The observed modal-score means/SDs are reported separately from the model's latent-effect scales. Numeracy alone is identified as centered and standardized; the text does not silently assign unit empirical SD to the two modal predictors. |
| Unavailable estimation detail and reproduction boundary | PASS | 430–441 lists the unprinted fitting/score-extraction calls, numerical settings, score vectors, density and identification details. The joint-versus-marginal modal-extraction choice remains explicitly unspecified. The text identifies the reported measure without inventing a reproducible estimator or claiming the equations are a rerun fit. |
| Aid-present primary question and contrast | PASS | 604–610 names adding checking when aid is already supplied as the primary question. 629–636 defines `Delta_aid = Ybar_11 - Ybar_01`, with only its two constituent means required. This matches that question. |
| Secondary contrast and separating example | PASS | 637–653 retains the four-cell equal-weight contrast as secondary. With the declared hypothetical means `(4,0,0,2)`, the primary difference is `2` and the secondary average is `-1`. The example therefore demonstrates the distinction and uses means within the stated 0–4 outcome range. |
| Study 2 conditional comparison | PASS | 556–566 explicitly lists Calculation, numeracy, age, income, education and gender, and distinguishes the intelligence composite used in later composite-outcome models. The raw-versus-modal score warning remains. |
| Empirical, normative and theoretical limits | PASS | The new definition retains the interpretation of processing stages as model assumptions. The surrounding text preserves source-reported estimates, sample/denominator distinctions, no-causal-inference qualifications and no-effect versus nondetection distinctions. 658–673 retains the assignment, compliance, missingness and transfer boundaries. 697–704 expressly leaves broader statistical and measurement theory separate. |

The probability display is internally coherent. For finite real logits, both stage probabilities lie strictly between zero and one; the three category probabilities are nonnegative and sum to `(1-piR) + piR*piC + piR*(1-piC) = 1`. The odds interpretation follows directly from `L(s)/(1-L(s)) = exp(s)`. These checks explain the displayed descriptive model's units; they do not verify its empirical truth or supply the source's missing estimation implementation.

PT-P19-01 required both identification of the actual measures and explicit recognition of unavailable source details. Both are now present. A fully specified likelihood, numerical fitting recipe or participant score reconstruction is not silently supplied by this PASS. Those remain separate if future work claims numerical reproduction. No new annex obligation has been introduced by these definitions and direct arithmetic.

## Kamp preservation and integration

At annex line 268, `\paragraph{The staged grammar is exactly the stated least closure.}` has become `\textbf{The staged grammar is exactly the stated least closure.}\enspace`. The words are identical. Reversing just that exact replacement in memory and hashing the resulting UTF-8 string gives `1193D892D2BA1A16EBDCBC10CA3FDF2AF161CFBE7084BE8C78AA6A9A84FCAE7A`, the complete R1 annex identity. Thus the proof text, both annex items and their body backreferences are unchanged. This source-preservation result does not independently verify the rendering workaround; no manuscript was built or rendered here.

The main driver now explicitly inputs P19 after P18 and before P11. The P19 driver sets stable identity `p19`, supplies exactly one direct part heading and inputs the reviewed evidence-method chapter. There is no new P19 theorem status requiring an annex route. The Kamp body input is immediately after Lemma 2 at `n-c-012.tex:151`; the matching annex input is after its Lemma 2 counterpart at `annex/p09.tex:9`. The prerequisites therefore precede the new body treatment, and the two reviewed proof items are reachable through the corresponding annex route.

The three P19 citation keys each have one complete matching bibliography entry at 6622, 6636 and 6649. Their authors, titles, publication metadata and exact source locators are present and agree with the cited identities and named intake. `Kamp1968` remains present at 2271. This is a source-text bibliography/navigation check, not a renewed acquisition, primary-source-fidelity or rights decision.

## Canonical notation and final checkpoint

The initial R2 registry snapshot had 1,016 data rows and SHA256 `BA12ECC55D3901C6AEA85A4743BC33F1A4F3A08D03CAC6FF4E80CFFB100ED531`. All fourteen appended R1-integration rows, data rows 1003–1016 (physical CSV lines 1004–1017), were read in full. They correctly distinguish first-order predicate substitution from temporal substitution and assignment update; the five-generator class/stages from semantic-equivalence closure; replacement truth sets from example predicate letters; P19 probabilities/counts/raw scores from process claims; and hypothetical assignment labels/cell means from participant scores.

The final registry was then read at all physical lines 1004–1024, with SHA256 `4C175DC0B3A3736272EA50C623CC698320EE2DC1B28927F0D681D48189EF37E2` and 1,023 data rows. The revised row at physical line 1016 explicitly identifies the equal-weight comparison as secondary, requires all four means, and records that its sign may differ from the primary contrast. The seven new rows at 1018–1024 supply participant/item/response symbols; upright response-category codes; real person effects; item intercepts and the logistic function; conditional stage and response probabilities; modal predictors with the source's extraction ambiguity retained; and the aid-present primary contrast with its two-mean domain. These match the manuscript's roles, domains and limits. The local P9.4/P19.1 scopes preserve their distinctions from similarly named symbols elsewhere.

**Notation-meaning verdict: PASS for these twenty-one records at the stated registry identity.** The generated-source check below found a separate TeX-encoding defect.

### PT-PROJ-01 — Put mathematical subscripts in math mode in generated prose notes

**Initial finding: FAIL; final disposition: PASS after the repair below.** After the lead supplied generated projections, all twenty-one affected rows were read in each output. The initial `tmp/edition-2026-p19-kamp3/symbols-tables.tex` had SHA256 `C22EE2FBE0B2E70898B7D57060FFA8340DEEA25FA1AA461A0DF24BE5AB995CB6` (1,298 lines); the corresponding `symbol-index.tex` had SHA256 `91C62921102875B7DDB7D7D5A5305B476C69B4121B38D7EC72D3E7E9BD978AAF` (1,024 lines). Their glyphs, roles, scope fields and reciprocal `entry:symbol-registry-01004` through `01024` links agreed. However, their notes were TeX source prose, and five canonical notes passed raw underscores through without math delimiters:

| Registry physical line | Raw prose token | Symbol table line | Symbol index line |
| --- | --- | --- | --- |
| 1008 | `P_i` | 948 | 47 |
| 1011 | `k_g/n_g` | 1282 | 990 |
| 1014 | `n_C+n_O` | 1285 | 988 |
| 1018 | `X_ij` | 1289 | 254 |
| 1024 | `Ybar_11`, `Ybar_01` | 1295 | 986 |

These underscores are outside the preceding closed glyph math and outside any literal-text wrapper. They cannot serve as ordinary prose characters in these TeX table cells. **Required repair:** put the intended mathematical expressions inside math delimiters in the canonical notes, using the correctly braced symbols, or replace them with ordinary prose; regenerate and inspect both projections. Do not hand-edit the generated outputs. No build or render was run to discover this source-encoding defect.

Actual generated-table reading comprised lines 944–948 and 1280–1295. Actual index reading comprised all matching rows at 42, 47–48, 72, 174, 206, 209, 254, 346, 406, 457, 460, 755, 784, 819, 846, 986–988, 990 and 992. A first overly broad search was truncated; these complete bounded rows were reread before the finding was issued.

### Focused repair closure

The lead corrected the five canonical notes and regenerated both outputs. At 02:46:02 UTC, this reviewer read all five corrected registry rows and their five projections in each output, and verified the final hashes recorded in the identity table. The notes now use `\(P_i\)`, `\(k_g/n_g\)`, `\(n_C+n_O\)`, `\(X_{ij}\)` and `\(\overline Y_{11}-\overline Y_{01}\)`. Their intended mathematical meanings and stable anchor identities are preserved.

As an additional read-only identity check, reversing only those five prose replacements in memory reproduced the exact earlier hashes for all three files: registry `4C175DC0...`, symbol table `C22EE2FB...`, and symbol index `91C62921...` (full identities above). This proves that the previously read remaining projection content was unchanged. No generated file was edited by this reviewer, and no build, generator or render was run here. **PT-PROJ-01 is closed at the generated-source text scope.** Rendered output quality remains separate.

The target/manuscript and route/bibliography hashes were revalidated at the return checkpoint before the generated-source check; the corrected registry and both projections were then independently rehashed as described above. No other R2 verdict was consulted. P19's repaired publication-text component passes, Kamp's unchanged content verdict is preserved, and the assigned canonical/generated notation scope passes. No production, admission, full P19/E1, full Kamp III.2 or final-acceptance claim is made.
