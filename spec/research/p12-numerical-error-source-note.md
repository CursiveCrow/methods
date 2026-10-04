# Numerical error and inference: author/source record

Date: 9 September 2026. Unit: `ED26-SCI-GoldbergOracle-001`.
Status: selected body and eighteen proofs authored; full author read-through, integrated mathematical examples and reciprocal proof-label accounting completed. Ready for lead integration and the later consolidated reviews. No independent acceptance or publication claim.

## Exact acquired presentation

The [Oracle-hosted HTML](https://docs.oracle.com/cd/E19422-01/819-3693/ncg_goldberg.html) identifies Appendix D as an edited reprint of David Goldberg's March 1991 Computing Surveys article. The [PDF of this same guide](https://docs.oracle.com/cd/E19422-01/819-3693/819-3693.pdf) identifies the book on its actual first page as *Numerical Computation Guide*, Sun Studio 11, part 819-3693-10, November 2005, Revision A. The copyright page says 2005 Sun Microsystems. This 2005 edited presentation is the selected source, not a substituted original article or a claim about current IEEE compliance.

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| `source/references/p12-numerical-error/oracle-819-3693-goldberg.html` | 510096 | B61F55461B984EA1CAC3D9445BE84DC11787F6F101F1A2F2AC0FE8F327866026 |
| `source/references/p12-numerical-error/oracle-819-3693.pdf` | 2036560 | 352F4A6CCD78C8A458872981668F53B7270CD182AC4E7C77684FA73CC2119304 |

The PDF has 294 physical pages; physical page 183 is printed D-1. D.3 begins at physical page 185 / printed D-3. D.6.1 occupies physical pages 228–237 / D-46–D-55; only its actually invoked proof material is selected. D.10.1–D.10.2 is physical pages 243–245 / D-61–D-63. D.11's explicit notice says that its additions were not written by Goldberg; it is not part of this selected proof package.

The complete selected D.3 text and theorem statements were inspected through the primary HTML and the PDF; mathematical expressions obscured by HTML image placeholders were checked in the actual PDF text. D.6.1 and D.10.1–D.10.2 were read for the dependent proofs. Read-only PDF extraction is source reading, not a manuscript render or review.

## Owned output

- `handbook/parts/p12/numerical-error-and-inference.tex`
- `handbook/annex/p12/numerical-error-and-inference.tex`
- `handbook/bib/intake-p12-numerical-error.bib`
- `handbook/registry/symbols-intake-p12-numerical-error.csv`
- This source note and the uniquely owned source directory.

The lead owns routing, style, canonical bibliography and symbols. No driver or shared canonical record was edited.

## Source-to-treatment allocation

| Selected source component | Manuscript result/interface |
| --- | --- |
| D.3.1–D.3.2 formats, ulps, relative error | `def:p12-numerical-format`, `def:p12-numerical-rounding`, `thm:p12-numerical-nearest` |
| D.3 Theorem 1 | `thm:p12-numerical-no-guard` |
| D.3 Theorem 2; D.6 Theorems 9–10 | `thm:p12-numerical-guard-bound` |
| D.6 Theorem 11 | `thm:p12-numerical-close-subtraction` |
| D.3 cancellation; D.6 product-error calculation | `thm:p12-numerical-product-errors`, `thm:p12-numerical-cancellation` |
| D.3 quadratic identity/examples and D.6 sensitivity discussion | `thm:p12-numerical-quadratic`, its traces, `thm:p12-numerical-root-sensitivity` |
| D.6 Theorem 12; D.3 Theorem 3 | `thm:p12-numerical-triangle-radicand`, `thm:p12-numerical-triangle-area` |
| D.6 Theorem 13; D.3 Theorem 4 | `thm:p12-numerical-mu`, `thm:p12-numerical-log-increment` |
| D.3 Theorem 5 | `thm:p12-numerical-no-drift`; complete rounding-cell proof, including the asymmetric boundary case |
| D.6 Theorem 14 and D.10 carry proof | `thm:p12-numerical-split-rounding` |
| D.3 Theorem 6 | `thm:p12-numerical-split` and exact partial-product example |
| D.3 Theorem 7 | `thm:p12-numerical-round-trip` |
| Edition's sign/order and uncertain-data inference obligation | `thm:p12-numerical-certification`, `thm:p12-numerical-data-budget`, final reference procedure |

The binary-to-decimal conversion theorem, Kahan summation, hardware survey and D.11 implementation survey are not invoked by this selected D.3 proof package. Their presence in the complete acquired PDF does not make them new whole-section obligations here. The source's companion sum formula at the end of D.6.1 is not used to prove any selected result.

## Direct mathematical corrections and proof choices

The active text defines an unrestricted-exponent interior model and explicitly states sufficient finite-range transfer conditions: executed operations implement the declared rounding procedure, nonzero stored inputs/outputs are normal, and the magnitudes of nonzero exact real operation results stay within the normal magnitude range. The exact real result need not be exactly representable; proof-only rescalings are not executed operations. Nonzero relative errors do not cover exact-zero targets or results lost through underflow. Guard-digit arithmetic and exact rounding are different procedures throughout.

The difference-of-squares error product retains its cubic term: `(1+2u)^2(1+u)-1 = 5u+8u^2+4u^3`. The active derivation does not silently discard a higher-order term from a bound.

The logarithm proof handles one-guard addition directly. The source's mean-value argument uses an absolute increment displacement bound and a restricted interval for its ratio lemma. The authored integral lemma supplies `|(log mu)'| <= 1/2` on the entire nonnegative axis; the proof uses `|xhat-x| <= 2u`, includes rounded values above 3/4, and derives the same 5u result without upgrading addition to exact rounding. The zero branch is explicit. The proof of `ln(1+x) >= 2x/(2+x)` supplies the needed relative bound in that branch.

The area derivation includes degenerate triangles as a zero absolute-error case, all three multiplication errors, square-root perturbation, and any rounded division by four. Exact rational comparisons certify its constants at u=1/200 and monotonicity covers the remaining interval. The square-root and logarithm interfaces preserve the source's half-ulp assumptions without adding an unnecessary even-midpoint rule for those library results; round-to-even remains mandatory in the separate exact-rounding identities.

The source's D.10 editorial footnotes 31 and 32 explicitly state a missing additional carry argument in the splitting proof. The authored proof uses integer grids and covers the extra carry: if the second subtraction crosses the upper binade, its rounded value is the boundary BP and the final high part is exactly the correctly rounded coarse value. Midpoint parity and the smallest binary parameter case are handled explicitly. No reader-facing passage asks the reader to repair the source proof.

The round-trip theorem explicitly requires representable integer operands and no range loss. Its normalized midpoint-separation proof handles every even radix and separately treats the equal-exponent denominator by exact division by two. It thus proves both the source's binary theorem and its subsequent even-radix remark as a mathematical statement, without a hardware-compliance claim.

## No-drift proof construction and source lead

Oracle's Theorem 5 is stated without a proof. Root assigned `historical_first_half` a bounded proof-construction task. Its complete derivation is preserved in `spec/research/numerical-no-drift-proof-construction.md` (SHA-256 2B4403055492BC21F6C242CFC83AD1993DF13D029362ED19F2DF5ABDACA09C4A), read in full and integrated by this chapter's author. The active theorem now points to the complete annex proof. It distinguishes symmetric cells from an asymmetric radix-power boundary; the exceptional branch can change the rounded intermediate subtraction while its following addition still fixes the output. This is author construction, not an independent review or claimed reproduction of the unread original proof.

The reference is Reiser and Knuth, *Evading the drift in floating-point addition*, Information Processing Letters 3(3), 84–87 (1975), DOI [10.1016/0020-0190(75)90022-8](https://doi.org/10.1016/0020-0190(75)90022-8). A separate erratum is recorded at 3(5), 164 (1975). The source body and erratum have not been acquired in this assignment; their metadata are leads, not read proofs.

## Author calculations and remaining work

`source/references/p12-numerical-error/author-arithmetic-calculations.py` performs exact rational exploratory calculations. It checked split examples across small bases/precisions and the two constant comparisons. It is not a proof of the general results, a manuscript test suite or an independent review. The manuscript proofs carry the universal claims.

The final author pass read the body and annex, the complete assisting no-drift derivation, and every subsequent integrated change. It corrected the geometric-sum approximation to 37614.0473, checked the exact discriminant ratio 177/73, the Heron product sequence 0.452, 2.04, 9.22, the stable product sequence 1.09, 9.81, 88.3, the split difference 34799/1000000, and the certified relative root bound 4/39597. The area proof explicitly allows zero radicand perturbation in its intermediate inequality. The general even-radix round-trip proof was read through with its midpoint parity, equal-exponent denominator and scaled-integer cases.

Construction accounting finds eighteen body results with proved targets, eighteen reciprocal annex items, no cited-only result, no hbproof wrapper, and no unmatched reciprocal pair in these owned files. The bibliography intake has one identified entry; the symbol intake has twenty-three rows. These observations are author/integration evidence, not independent acceptance.

Remaining work belongs to lead integration and the later batch gates: merge the uniquely named intakes, route the body and annex, retain the source and proof-construction evidence, and perform the consolidated source/topic/publication reviews and required final build/output checks. No build, render, independent review or new test suite has been run in this assignment.
