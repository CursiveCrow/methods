# Simulation evidence: selected source and authoring record

Date: 9 September 2026. Unit: `ED26-SCI-NASA7009B2024-001`.
Status: all four selected components authored; complete author read-through, arithmetic examples and reciprocal-label accounting finished. Ready for lead integration and later consolidated gates. No independent acceptance, NASA compliance assessment, or publication claim.

## Exact source and selected extent

The acquired [NASA-STD-7009B PDF](https://standards.nasa.gov/sites/default/files/standards/NASA/B/1/NASA-STD-7009B-Final-3-5-2024.pdf) is the exact selected standard, approved 2024-03-05 and superseding NASA-STD-7009A with Change 1. The cover, history and foreword were read from the actual document. Revision A's 2016 approval/change dates are not substituted for revision B. PDF creation/modification metadata say 2024-03-06; they are not its approval date.

Local artifact: `source/references/p12-simulation-evidence/NASA-STD-7009B-2024-03-05.pdf`.
Bytes: 1417365. Physical pages: 88.
SHA-256: `7B95A2065325DC3035C35CE110557D817555D3F22210CE5F6CE0BB2FB4CCD8B4`.

Read in full: section 3.2's definitions; 4.2.1.3–4.2.1.7; 4.2.3–4.2.8; 4.3.1–4.3.9; and the selected Appendix E factor discussions and full level tables. Sections 1.1–1.3 were read to determine applicability and the force of shall/should. E.1–E.3.1 and E.4.1 supplied the capability/results distinction and ordinal-label context. The five selected factor families are development/runtime pedigree (E.3.2 and E.4.3, Tables 7 and 16), verification (E.3.3/Table 8), validation (E.3.4/Table 9), uncertainty characterization (E.4.4/Table 17), and results robustness (E.4.5/Table 18). E.4.2's use-assessment comparison was read as context for 4.3.1.

Useful physical locators: definitions pages 11–17; selected development record clauses pages 25–26; verification/validation/uncertainty pages 28–30; use/reporting pages 31–38; Appendix E introduction pages 62–64; full pedigree/verification/validation tables pages 66–69; runtime input/uncertainty/robustness pages 75–79. The document's contents/table list is not consistently identical to physical-page numbering; citations use actual clause/table identities.

This is a reasoning-method comparison, not a reproduction of every administrative definition or a complete NASA compliance manual. The selected clauses are all read and their relevant requirements, recommendations and inferential distinctions are represented. Administrative terms are retained where they affect the scope/force of those clauses. The technical-review and process-management factors are acknowledged as part of NASA's complete assessments; their unselected full level tables are not silently replaced by the five selected families.

## Bounded reference-data example

The [NIST BoxBOD ASCII record](https://www.itl.nist.gov/div898/strd/nls/data/LINKS/DATA/BoxBOD.dat) was acquired and read completely. It identifies six observed responses, their units, the exponential model, starting values and certified fitting outputs; it attributes the observations to Box, Hunter and Hunter (1978), pages 483–487. That book was not acquired or represented as read. The [NIST certification-method page](https://www.itl.nist.gov/div898/strd/nls/data/LINKS/c-boxbod.shtml) was acquired; its methodology and definition text were read to bound the meaning of certified reference values.

| Local artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `source/references/p12-simulation-evidence/NIST-BoxBOD.dat` | 1784 | FC44FBED04E3BE16DF6498E722D4C8AEDFD0AF210110BC396D9F99ACECD77E21 |
| `source/references/p12-simulation-evidence/NIST-BoxBOD-certification.html` | 8097 | 3BB235265C6AAE49FC3A2C85AF3D78CA8D808E3530378A98D59719715120B8D7 |

These NIST endpoints are not independently versioned; no invented publication date is assigned. The retained finite records and hashes identify this use. No post-cutoff scientific finding is introduced: the example uses the documented historical dataset and its established numerical reference values.

The chapter does not claim a new fit, a new experiment, an independent validation sample, or a deterministic measurement-error bound for these data. NIST's 128-bit and multiple-algorithm certification pertains to the numerical regression reference. Six tabulated fit residuals show the difference between computational reproduction of that reference and meeting a separately declared response criterion. The criterion of 10 mg/l is an illustrative handbook choice, not a NASA/NIST standard. A complete proof establishes the day-three discrepancy exceeds 22.04 mg/l, without relying on displayed decimal exponential approximations.

## Owned files and source-to-component allocation

- `handbook/parts/p12/simulation-results-as-evidence.tex`
- `handbook/annex/p12/simulation-results-as-evidence.tex`
- `handbook/bib/intake-p12-simulation-evidence.bib`
- `handbook/registry/symbols-intake-p12-simulation-evidence.csv`
- This note and the unique source directory.

| Map component | Completed authored treatment |
| --- | --- |
| SCI-007-C01: model proof versus target evidence | Objects/use definitions; explicit error chain; conditional error-budget proof; exact decay/Euler model and computation. |
| SCI-007-C02: verification/validation and domains | Selected development/use/verification/validation clauses; precise referent-comparison bounds; NIST calibration-versus-validation example. |
| SCI-007-C03: numerical and empirical uncertainty | Separate step and arithmetic-error derivations; joint input-sensitivity bound; NASA uncertainty/pedigree factors; reporting unavailability without inventing a bound. |
| SCI-007-C04: transfer beyond validated domain | Finite-point nonidentifiability proof; continuous monotone regime-change counterexample; output-specific validation and explicit transfer premises. |

The chapter also proves that averaging ordinal factor labels is not invariant under increasing relabeling. It applies NASA's own warning against comparing/combining levels across different factors while retaining comparison of each factor against its own threshold.

## Source-force and inference decisions

Revision B's separate capability and results assessments are retained. Requirements using shall are distinguished from recommendations using should; no clause is adopted as a handbook production instruction. Section 4.3.6 leaves sufficiency thresholds to the program/project. M&S 26's warning alternative does not validate out-of-domain use. M&S 33 explicitly permits reporting that no uncertainty estimate is available; such disclosure provides no numerical inference certificate.

Full factor-table conditions govern the presentation, not abbreviated overview rows. Level 0 means insufficient evidence, levels are ordinal, and multi-condition levels require every condition unless an explicit alternative is given. Data pedigree and runtime input pedigree remain separate despite their similar ladders. Robustness assessment concerns the extent of knowledge about sensitivities; a high assessment is not a mathematical claim that the system is insensitive. Model agreement with a higher-fidelity referent still needs evidence connecting that referent to the target.

The source's definition of a validation domain as a region enclosing favorable points is preserved as operational terminology. The mathematical counterexample establishes that this terminology alone provides no uniform interpolation theorem. Likewise interval overlap, a fitted residual statistic, a margin or an experience-based factor is not automatically a decision-relevant worst-case error bound or a probability of truth.

## Author calculations and remaining work

Author calculations used exact rationals for the exponential lower polynomial and high-precision decimal evaluation for the displayed examples. NIST reported-parameter predictions at days 1,2,3,5,7,10 are approximately 90.1109, 142.2441, 172.4056, 199.9509, 209.1708 and 212.9111 mg/l. Their residual sum of squares is 1168.00887655555 and residual standard deviation sqrt(RSS/4) is 17.08807242315, agreeing with the reference at its displayed precision. These calculations check arithmetic; they do not establish empirical adequacy.

The Euler example at N=4,10,20 gives exact-real iterates 0.31640625, 0.3486784401 and 0.35848592240854. Its proved error bounds are approximately 0.06131324, 0.02043775 and 0.00968104. The exact degree-five lower bound for exp(1.62) is 62759338217/12500000000, greater than five. Universal mathematical claims are proved in the annex rather than inferred from these numerical examples.

The author read the complete body and annex after the writing batch, and checked the final integrated changes and intakes. All nine formal results have complete reciprocal annex proofs; there are thirty unique defining labels, no cited-only formal result and no hbproof wrapper. The sixteen symbol-intake first-use labels resolve to actual definitions/results. Both external reader interfaces were read in the actual LaTeX: `thm:p12-numerical-certification` and `def:p19-evidence-record`. The bibliography intake contains three identified primary records.

Remaining work belongs to lead integration and the later full-batch gates: merge the unique bibliography/symbol intakes, route the body and annex, and preserve the source evidence. The broader sensitivity chapter in the coverage map remains a related reader interface; the joint decay sensitivity bound used here is self-contained and imports no unproved result from that future treatment. No independent review, build, manuscript render or prose-mirroring software test was run.
