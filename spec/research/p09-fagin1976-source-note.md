# Fagin 1976: original finite-model probabilities presentation

Assignment: `ED26-REQ-N-c-002-02`, allocated components
`N-c-002-MAP-02` and `N-c-002-MAP-04`. The exact queue row and
`spec/research/p09-source-presentations-lot1.md:176-242` control the extent.
The source's section 4 continues through printed p.58, so the full selected
sections were read through that page rather than stopping at the prior
note's p.57 counterexample locator.

## Source identity and actual reading

Ronald Fagin, *Probabilities on Finite Models*, *Journal of Symbolic Logic*
41(1), March 1976, pp.50-58, DOI `10.2307/2272945`. The freely available
[author-hosted scan](https://s3.us.cloud-object-storage.appdomain.cloud/res-files/500-jsl76.pdf)
is linked from the [author's publication index](https://ronfagin.com/papers/).
It was acquired on 2026-10-01 as
`source/references/p09-fagin1976/500-jsl76-author-scan.pdf`, 545111 bytes,
nine PDF pages, SHA-256
`e6aa930904068c12790728ec9409ac950577ef20467602bfb4003e38060e4fa8`.
This is the original journal article, with printed header, year, volume,
pagination and original references; no later enumeration paper is treated
as the same version.

The full extracted body of all nine pages was read. The extraction loses
the displayed axiom and some cases. Original page images for printed
pp.51,52,53,56,57,58 were inspected to confirm the extension guards, the two
spectrum proofs, the conditional parity formulas, the graph/tournament
conditioning formulas and the final-page weights. The local readable
body and receipt remain in the exclusively assigned reference directory.
PDF skill was used for source-page inspection only, not manuscript rendering.
Research skill called for a background researcher, but the explicit batch
ownership instruction forbids children; source research was performed in
this assigned agent without spawning another context.

## Prior manuscript state and distinctions

Read current `handbook/parts/p09/presentations/n-c-002.tex` in full and
`handbook/parts/p03/finite-model-theory.tex` through its finite-model results.
The common P9 presentation had a binary/general-arity summary, no full
back-and-forth or general-arity derivation, and no worked unlabelled proof.
It also folded equality into its open-description definition, contrary to
the original p.51. The dedicated assigned entry does not alter this shared
file; root must replace or reconcile its overlapping Fagin subsection.
The P3 theorem remains a separately cited survey counterpart. The separate
1974 complexity theorem is not duplicated here.

## Authored destinations and mathematical standing

- Body: `handbook/parts/p09/presentations/n-c-002-02.tex`, label
  `sec:p09-n-c-002-02`.
- Proof annex: `handbook/annex/p09/n-c-002-02.tex`, label
  `sec:annex-p09-n-c-002-02`; reciprocal targets under
  `annex:p9.n-c-002.2.*`.
- Disjoint bibliography/symbol intakes:
  `handbook/bib/intake-p09-fagin1976.bib` and
  `handbook/registry/symbols-intake-p09-fagin1976.csv`.
  Existing canonical `Fagin1976` was verified, not duplicated.

The reader text supplies both finite probability spaces, auxiliary counting
constants, exact relational open descriptions and distinctness guards,
all finite positive arities, extension theory, labelled law and geometric
rate, finite fragments, the actual disjunctive spectrum assertion, both
unlabelled proof cases, graph and tournament conditioning, constant/function
and second-order counterexamples, parity-conditioned failure, the unary
conditioning with limit 1/2, and the final-page nonuniform weights.

The annex fully derives the fresh-atom count
`sum_i k_i((m+1)^i-m^i)`, proves independence by disjoint inspected ground
atoms for distinct fresh candidates, and uses a union bound only across
parameter tuples. It completes both back-and-forth directions, consistency,
no finite models, and completeness relative to standard first-order
compactness and downward Lowenheim-Skolem. The source explicitly sketches
Theorem 1; the expanded argument is editorial, not falsely attributed as
printed source proof. It also proves the monadic normal-form premise using
a quantifier-rank threshold induction, and proves stars and bars directly,
so the monadic result has neither a hidden game lemma nor a missing Feller
proof dependency.

## Corrections and non-promotions

1. Original p.51 excludes equality from complete open descriptions. Distinct
   parameter and witness conditions were restored in their actual guards.
2. Corollary 6 is **either sigma or not-sigma has a cofinite spectrum**.
   The historical source note's stronger finite-or-cofinite assertion for
   each spectrum is not copied. Functions/constants belong to this spectrum
   corollary, not to the uniform zero-one theorem.
3. The source's first spectrum proof says relationalization preserves the
   positive spectrum. Negating the relational sentence permits failure of
   the total/single-valued coding conditions, so that premise alone does not
   justify transferring its negated spectrum to the original not-sigma.
   The annex uses and expands the source's independent second proof, with
   full predicates, projection functions and coincident constants. This
   proves the actual source result without silently assuming preservation
   under negation.
4. Nonmonadic unlabelled transfer imports Theorem 8 and the geometric rate
   from original reference [3], *The number of finite relational structures*,
   IBM report RC5587, August 1975 (identity visible on printed p.58).
   The exact separate report body/proof is not supplied. The body explicitly
   labels the imported estimate `cited=Fagin1976`; the completed transfer
   proof invokes it as a stated mathematical premise. No independent proof
   of that enumeration result or replacement by a later variant is claimed.
5. Section 4(7) states its mixed-measure convergence without proof. That
   statement retains cited status. Its actual weights, mixture identity and
   full-relation probability are supplied, without promoting the brief
   arbitrary-vocabulary remark into an unspecified measure theorem.
6. Source open questions are reported as questions in the 1976 article, not
   as current unsolved-status claims. The graph result fixes `0<p<1` and
   specifies no loops, symmetry, independent unordered edges and fixed
   vocabulary. It does not assert all functions, all orders, arbitrary
   conditioning, varying edge probabilities, or second-order zero-one laws.
7. The source's monadic rational-function remark is stated here as eventual
   rationality. Finite exceptional cardinalities must be allowed: the
   equality-only sentence saying there is exactly one point has probability
   one at n=1 and zero at every n>1, and no everywhere-defined nonzero
   rational function can have those infinitely many zeros and that isolated
   nonzero value. The supplied threshold proof establishes the correctly
   qualified eventual claim.

## Author checks and remaining integration

The full authored body, annex, receipt and intakes were reread before
handoff. The mathematical edge-case audit covers the empty relation
vocabulary (`q=1`), zero parameter sets, no unary predicates (`s=1`),
rank zero, one-element pairing/conditioning, unequal labelled/type weights,
and finite union rather than infinite intersection.

Direct finite calculations in the tool runtime (no saved test suite) gave:

- For one ternary relation, one parameter and two candidate points, each
  candidate uses seven distinct atoms and the two candidate atom sets have
  no overlap. Exhaustion of the 16384 assignments to those fourteen atoms
  gave 16129 assignments with neither all-positive extension, exactly
  `(127/128)^2`; each candidate succeeded 128 times and both once.
- For one binary, one ternary, and a mixed unary/binary/ternary vocabulary
  at m=2, fresh-atom counts were respectively 5, 19, and 25, agreeing with
  the stated general-arity formula.
- The four-type monadic composition counts at n=1,...,5 were 4,10,20,35,56;
  fixing one count to one gave 1,3,6,10,15, agreeing with both binomial
  formulas. In particular the unused-unary-vocabulary example gives 1/3
  versus 3/10 at n=2.
- Exhausting all unrestricted binary structures at n=1,...,4 gave
  sigma_1 counts 0,4,0,3888 and sigma_2 counts 2,0,296,0, with positive
  union counts and conditional sigma_1 probabilities 0,1,0,1. This checks
  the one-point edge case and the parity construction; it supplements,
  not substitutes for, the general pairing proof.

Inspection of the result/annex declarations found eight reciprocal proved
targets and two explicitly cited source-boundary results. No body proof
environment or undefined hbproof wrapper is used. These are mathematical
and structural author checks, not independent admission. No manuscript
build/render, consolidated
review, or prose-mirroring software suite is performed by this assignment.

Root owns routing, shared-file reconciliation, lookup integration and later
consolidated independent review/build/render. The original imported
enumeration proof and statement-only mixed-measure result remain exactly
qualified source boundaries; no additional independent full proof of those
steps is claimed. If a separate full-proof obligation is allocated to them,
it must remain open rather than be closed by these cited statuses.
