# Edition 2026 P15: signed measures and Radon–Nikodym

Date: 8 September 2026. Author: /root. Scope: P15.9.
This is substantive writing and integration under the user's instruction
to complete all changes before consolidated reviews.

## Primary source read

Durrett, Probability: Theory and Examples, author version 5 dated
11 January 2019, existing key DurrettPTEAuthor2019.
Held PDF: source/references/durrett-probability-2019-01-11/PTE5_011119.pdf.
Verified SHA-256:
AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886.

Root read complete extracted printed pp. 466–470 for Appendix A.4,
including its definition, both sign conventions, all source lemmas and
theorems, remarks and Exercises A.4.1–9. Complete images of printed
pp. 467, 469 and 470 were also read to resolve the displayed formulas.
Source image files are retained under tmp/pdfs/p15-radon-nikodym-source.
The complete extracted pp. 13–14 were read for the source's Cantor example
and its neighboring definitions. The manuscript supplies its own full
fair-digit construction and identifies its CDF with the source's specified
plateaus. No source figure is reproduced.

The existing integration, Stieltjes, CDF and countable-product statements
and required proof interfaces were read before writing. Research and PDF
skills guided primary-source reading. No manuscript PDF was built or rendered.

## Complete new LaTeX

| File under handbook/ | SHA-256 at authoring completion |
| --- | --- |
| parts/p15/radon-nikodym.tex | 1DFE698D74883B9CE2AE2D3A5A2DE31552C07838DFB505EA953A1ECE26E95E66 |
| annex/p15/radon-nikodym.tex | D3E282F6672E636E838F229D6D419523696045C0181AA6EA1D1D80EAD3EA23A7 |

Both complete saved files were read back by their author. Thirteen
statement/proof suffixes have body prefix thm:p15- and annex:p15.:

- signed-measure-examples: differences with finite negative measure;
  integral construction; the full positive/negative subset criterion.
- signed-set-closure: hereditary and countable-union closure in both signs.
- negative-subset: the source's minimal reciprocal-threshold removal,
  terminating case and complete infinite-remainder contradiction.
- hahn-decomposition: attainment of the negative infimum, exclusion of
  a negative-infinite infimum and exact signed-null partition uniqueness.
- jordan-decomposition: existence, uniqueness, negative-part finiteness,
  extrema over subsets and the full finite-partition variation formula.
- signed-cdf-variation: normalized right-continuous CDF differences,
  uniqueness and the reverse interval-variation inequality by explicit
  finite-measure approximation with interval unions.
- lebesgue-decomposition: maximal dominated density, Hahn residual,
  common finite partition for both sigma-finite measures and uniqueness
  without cancellation of infinite totals.
- radon-nikodym: removal of the singular part, finiteness on a target
  finite-measure cover and full density uniqueness on all relevant sets.
- density-calculus: simple/monotone change of measure, signed parts,
  sums, scalar multiples, chains, reciprocal null sets and singularity transfer.
- finite-signed-density: representation of both Jordan parts, their
  disjoint density supports, signed uniqueness and total-variation density.
- finite-uniform-absolute-continuity: complete epsilon-delta equivalence
  for a finite target measure and any base measure.
- cantor-singular-law: actual independent-digit random variable, every
  cylinder mass, every middle-third plateau, absence of atoms and density.
- radon-nikodym-examples: mixed density/atom measures, signed cancellation,
  counting-measure failure and failure of uniform continuity for an infinite target.

The source's positive-infinite signed-measure convention is preserved;
the other one-sided convention is identified separately. The converse
CDF statement includes the needed right continuity and zero left limits.
The sigma-finite assembly is explicit, and the singularity proof uses
the actual reciprocal sequence of Hahn partitions. The density uniqueness
argument treats infinite-valued representatives on their measurable null
sets before comparing finite integrals. These are direct completed arguments
in the reader text, with no instruction to repair a preceding statement.

## Integration and subsequent writing

Root owns the body/annex input after countable-product-measures, canonical
notation and the earlier forward references. The existing bibliography key
supplies every citation. This authoring note does not claim independent
content acceptance or a current manuscript build.

Conditional expectation is the next local writing component. Its exact
source Section 4.1, printed pp. 205–217, has now been read completely as
text in preparation, including the regular conditional-law construction
and Exercises 4.1.1–10. Its local-equality proof must conclude zero measure
on A intersect B, not on all A. Its joint-density formulas must explicitly
handle zero/infinite marginal densities and nonintegrable exceptional
sections. Regular kernels need one common full-measure domain and a
measurable Borel-image concentration argument; those will use the complete
real coding already supplied in the preceding chapter.
