# Edition 2026, P15 packet w02ca-p15-004 (sections 158.6, 158.7)

Label tag: `p15-w02c-p15-004`. New chapter files:
`handbook/parts/p15/measure-integration-and-product-constructions-w02c-p15-004.tex`
and the matching annex file. Placement: body after
`parts/p15/measure-integration-and-product-constructions-w02b-p15-005`
(handbook/parts/p15.tex line 41); annex after the matching annex input
(handbook/annex/p15.tex line 40). The lead adds both `\input` lines.

## Sources opened in this session

- `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`
  (Durrett, Probability: Theory and Examples, author Version 5, 2019-01-11):
  printed pp. 53-54 (PDF 61-62: Theorem 2.1.21, nice spaces, Theorem 2.1.22,
  the Dudley 13.1 pointer and the cardinality consequence on p. 54);
  printed pp. 119-122 (PDF 127-130: remark before Theorem 3.2.9 on p. 119,
  Theorems 3.2.10-3.2.11 and the remark after 3.2.11 on p. 120, rendered as
  an image to confirm the symbols x_n in G, x_n -> x_inf in boundary of G,
  K = G^c).
- `source/references/kripke-computational-dependencies/moschovakis-2009-dst-author-copy.pdf`
  (Moschovakis, Descriptive Set Theory, 2nd ed., 2009 author copy; bib key
  Moschovakis2009DSTAuthor): Section 2C, Perfect Set Theorem 2C.2 (statement
  p. 59, proof pp. 59-61) and Corollary 2C.3 (p. 61). Cited as a compare
  reference for the perfect-set step; the handbook proof uses a one-step
  condensation argument instead of the transfinite tree derivative.
- Dudley, Real Analysis and Probability (1989), Section 13.1: not held, not used.

## Gap closures

- weak-convergence-of-laws-C005: the p. 119 claim that the bounded-continuous
  characterization is a definition meaningful in any topological space.
  Written as def:p15-w02c-p15-004-topological-weak,
  thm:p15-w02c-p15-004-topological-weak (meaningfulness, agreement with the CDF
  definition on R, continuous images, metric uniqueness),
  thm:p15-w02c-p15-004-nonunique (Sierpinski two-point space: limits not
  unique), warning def:p15-w02c-p15-004-what-transfers.
- weak-convergence-of-laws-C008: the p. 120 remark in its general form.
  thm:p15-w02c-p15-004-point-masses (delta_{x_n} => delta_{x_inf} iff
  x_n -> x_inf), thm:p15-w02c-p15-004-boundary-approach (existence of the
  approach, strict (ii) for G, strict (iii) for K = G^c, boundary of K equals
  boundary of G and carries the limit mass, interior contrast), example
  def:p15-w02c-p15-004-two-sided.
- countable-product-measures-C015: the p. 54 cardinality consequence.
  Proved through the existing real coding thm:p15-metric-borel-representation,
  lemmas reals-continuum, borel-suslin, condensation, theorem
  thm:p15-w02c-p15-004-borel-cardinality, example
  def:p15-w02c-p15-004-irrationals. The earlier blocker (Dudley not held) does
  not apply to this route: the proof is self-contained and the held
  Moschovakis text is cited only for comparison. The ACQ-2026-10-0316 blocker
  ref in the packet resolves to an unrelated record.
- Patch request work/waves/w02ca/patches/w02ca-p15-004.json asks the lead to
  repoint the boundary def:p15-countable-product-next (read-only host) to the
  new theorem.

- Continuation round (w02ca resume): Durrett pp. 53-54 (PDF 61-62) reopened
  in this session. countable-product-measures-C009: Durrett's nice definition
  (p. 53), naming remark (short marked quotation, 9 words), applications
  claim, Theorem 2.1.22 in the source's terms (p. 54) written as
  def:p15-w02c-p15-004-nice, thm:p15-w02c-p15-004-nice-coding,
  thm:p15-w02c-p15-004-durrett-2122, example def:p15-w02c-p15-004-nice-cases.
  countable-product-measures-C013: failure claim and attributions (Andersen
  and Jessen 1948; Halmos 1950 p. 214; Neveu 1965 p. 84; Wegner 1973), all as
  Durrett reports them on p. 53 (those works are not held and not used), in
  def:p15-w02c-p15-004-extension-failure; the nice-space generalization stated
  and set against the handbook's Borel-image form in
  thm:p15-w02c-p15-004-nice-extension (uniqueness for arbitrary factors;
  existence with Borel images; under AC a Vitali-type decreasing family
  A_n of full outer measure with empty intersection gives nice factors with a
  consistent family and no extension). The counterexample is the handbook's
  own; it is not attributed to Andersen-Jessen.
  countable-product-measures-C015: thm:p01-csb / thm:p01-cantor citations
  replaced by the routed statements of sec:set-prerequisites-05
  (handbook/restoration/inherited-00533-00602.tex via parts/p01.tex); the
  Axiom of Choice is cited as sec:set-prerequisites-06.
- Patch file work/waves/w02ca/patches/w02ca-p15-004.json now has three
  entries (boundary repoint; pointer after def:p15-measurable-real-coding;
  pointer in thm:p15-coded-space-extension).
- Overlap noted for the lead: w02c-p15-002's unrouted nice-space text.

## Extensions beyond the source (marked in reader text)

Metric uniqueness of test-function limits; the two-point non-uniqueness
example; the converse half of the point-mass characterization; the whole
proof of the p. 54 cardinality statement; the nice-map / Borel-coding
relation; the uniqueness-for-arbitrary-factors statement; the counterexample
showing the Borel-image clause is needed.

## Continuation

State at return (resume round): the three assessed gaps C009, C013, C015
have reader text and annex proofs in the owned files; unit-compile ok with
no overfull boxes; find_fused_spaces clean; check.py shows no finding in the
owned files. Remaining for the lead: add the two `\input` lines at the
insertion points, apply the three patch entries, and decide the overlap with
w02c-p15-002's nice-space entries. Symbol rows added for the nice map and the
counterexample's local notation.

Resume round 2 (after the usage-limit halt): the assessment's G1 names
spec/research/edition-2026-p02-categorical-syllogistic-and-existential-import-w02-p02-002.md.
This packet did not write it: it belongs to the owned sets of w02ca-p02-001
and w02ca-p02-002, was modified at 15:55 (after this packet's last write at
15:23), and shows no diff against HEAD. Left untouched; recorded in the
return file under guard_notes. Re-ran unit-compile (ok, 0 overfull),
find_fused_spaces (clean) and check.py filtered to the owned files (no
finding). Rechecked the C015 annex proofs (reals, borel-suslin, cond,
borel-cardinality) line by line; no change needed.

Resume round 3 (w02ca r4, block 1): the assessment's remaining items
weak-convergence-of-laws-C005 and -C008 are route disputes only (the
treatments in sec:p15-w02c-p15-004-topological and
sec:p15-w02c-p15-004-boundary, annex lines 21-157 and 159-238, are not
input by any driver). No reader text changed. Driver lines rechecked:
handbook/parts/p15.tex line 41 and handbook/annex/p15.tex line 40 still hold
the w02b-p15-005 inputs. Two insert_after entries for the drivers were added
to work/waves/w02ca/patches/w02ca-p15-004.json (five entries now). C005 and
C008 are returned as blocked_policy pending the lead's driver inputs; C009,
C013 and C015 live in the same unrouted file and need the same inputs.
unit-compile ok (0 overfull), find_fused_spaces clean, check.py shows no
finding for the owned files.

Resume round 4 (w02ca r4, block 2): the assessment repeats C005 and C008 as
route disputes (lead-owned driver inputs). Rechecked: handbook/parts/p15.tex
line 41 and handbook/annex/p15.tex line 40 still hold the w02b-p15-005 inputs
and neither driver inputs the w02c-p15-004 files. Body lines 6-12 (p. 119
remark, quoted and located), 69-165 (sec:p15-w02c-p15-004-topological) and
167-233 (sec:p15-w02c-p15-004-boundary), annex lines 21-157 and 159-238
unchanged. Patch entries 4-5 in work/waves/w02ca/patches/w02ca-p15-004.json
still carry the two insert_after lines. No reader text changed. unit-compile
ok (0 overfull), find_fused_spaces clean, check.py shows no finding for the
owned files.

Resume round 5 (w02ca r5, block 1): the assessment adds two writable items.
Durrett PTE v5 pp. 117-118 (PDF 125-126) reread in this session.
- weak-convergence-of-laws-C021 (Example 3.2.5): new section
  sec:p15-w02c-p15-004-examples. def:p15-w02c-p15-004-birthday-reading gives
  the source's model and product (m from 2 to n), the j = m-1 match with
  thm:p15-weak-first-examples, the N = 365 reading under the source's
  equal-likelihood assumption (stated as "no two share"; the source's wording
  is paraphrased and the intended event made explicit), the source's
  arithmetic (1.1515, 0.6630, 0.515) and its comparison (2% smaller than
  0.524). thm:p15-w02c-p15-004-birthday-error proves a < p and
  0.0171 < (p-a)/p < 0.0174, also for the rounded exponent 0.6630
  (484/730 - 0.6630 = 1/73000); annex:p15-w02c-p15-004-birthday-error uses
  the series bounds x + x^2/2 + x^3/3 < -log(1-x) < x + x^2/2 + x^3/(3(1-x)),
  power sums 231, 3311, 53361, and t - t^2/2 < 1 - e^-t < t. Numbers were
  checked with exact rational arithmetic in a scratch script (relative
  shortfall 0.017182...).
- weak-convergence-of-laws-C022 (Example 3.2.6): def:p15-w02c-p15-004-density-notation
  quotes the convention sentence (one sentence, marked, p. 118), identifies
  it with f_{Y_n}(y), records non-adoption, and notes that the display's
  first factor P(S_2n = 0) is a genuine probability equal to C_n.
  thm:p15-w02c-p15-004-density-reading (annex:p15-w02c-p15-004-dens): the
  event {Y_n = y} has probability zero, f_{Y_n}(0) > 0, P(S_2n = 0) = C_n.
- Patch entries 6-7 added for the read-only host
  handbook/parts/p15/weak-convergence-of-laws.tex (route sentences pointing to
  the new labels); they need entries 4-5 (driver inputs) to resolve.
- Intro (purpose, inputs, conclusions) extended; owned-body lines after 34
  shifted by +8, return file updated accordingly.
- Symbol intake: P(Y_n=y) (source density notation), p,a,a', Lambda/kappa,
  s_k.
Checks: unit-compile ok, 0 overfull; find_fused_spaces clean; check.py
--tree handbook shows no finding in the owned files.
State: C021 and C022 have reader text and annex proofs in the owned files;
like C005 and C008 they reach the route only after the lead applies patch
entries 4-7.
