# P15-U1: finite probability foundations

Date: 7 September 2026. Author: `/root/p5_kamp_source_review`.
Assignment: first bounded P15-U1 unit, serving the N-x-008 foundations.
Status: substantive body and complete finite-scope proofs supplied and read
back by the author. Independent source, topic and publication review,
integration, production and admission remain due.

## Saved result and exact scope

| Artifact | Supplied extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p15/finite-probability.tex` | 1-461, complete new chapter body | `BD14BAB29058D7235155D827A8F11793A1D07AF119AD1B34239835EF98805AC0` |
| `handbook/annex/p15/finite-probability.tex` | 1-284, all seven complete proof items | `D51A43CF5E2CD2DCE15CD558EF3A167AC084347BB471E2A44E657769399EAE58` |
| `source/references/grinstead-snell-chance-2006/prob-2006-07-04.pdf` | New, unchanged full primary-source capture; reading restricted below | `763EAB9894983DDFD6CD7F84685548D1515A9326A2D9FD015474534460551A5E` |

The chapter supplies finite outcome spaces and all-subset event spaces,
probability masses and measures, support/null/almost-sure distinctions,
finite random variables and joint/marginal laws, conditioning on a positive
event, multiplication and chain rules, successive conditioning, total
probability, Bayes' formula and odds, event and random-variable independence,
conditional independence, a two-factor product construction, finite real
expectations, linearity, independent-product expectation, conditional means,
and the averaging property and almost-sure uniqueness of E[X | Y] for finite Y.

This is one finite foundations unit. It is not all of P15-U1, N-x-008, the
source textbook, or the probability/statistics stream. General measurable
spaces, countably infinite probability, continuous densities, integration,
infinite products, convergence, laws of large numbers and other limiting
results, general conditional expectation and null-event conditional
distributions remain separate obligations. The body states these limits.

## Holdings check and primary-source acquisition

Before acquisition I checked existing source/reference and temporary PDF
filenames for Grinstead/Snell, probability-book, `prob.pdf`, and `amsbook`
holdings, and searched the canonical `handbook/bib/handbook.bib` for the
authors and probability-text titles. No matching held textbook PDF or
bibliography entry was found by those checks. Other probability-related
metadata and references did not supply this source body. No existing source
capture was replaced.

The verified new source is *Grinstead and Snell's Introduction to Probability*,
The CHANCE Project, version dated **4 July 2006**. Its title-page notice
identifies copyright 2006 Peter G. Doyle and describes this as a version of
Grinstead and Snell's *Introduction to Probability*, second edition,
published by the American Mathematical Society, copyright 2003 Charles M.
Grinstead and J. Laurie Snell. The notice states redistribution under the GNU
Free Documentation License. The chapter cites this precise CHANCE version;
the capture is not identified as an unchanged scan of a different AMS edition.

Primary locator:
[Dartmouth Mathematics CHANCE PDF](https://math.dartmouth.edu/~prob/prob/prob.pdf).
The [CHANCE book page](https://chance.dartmouth.edu/teaching_aids/books_articles/probability_book/pdf.html)
was also inspected for the author/institutional setting and chapter listing.
The actual mathematical reading used the saved PDF, not this landing page.

The request on 7 September 2026 returned HTTP 200, `application/pdf`, and
`Last-Modified: Mon, 10 Jul 2006 13:05:02 GMT`. The saved file is 2,993,135 bytes,
an unencrypted 518-page PDF 1.2 with letter-size pages. Its SHA256 is in the
artifact table. Acquisition required a scoped filesystem/network escalation;
it succeeded. No paid access or alternative edition was substituted.

## Actual source reading

The PDF title/version/license page was visually read. The following complete
printed-page text extents were read from the saved PDF using `pypdf`:

| Printed pages | Physical PDF pages | Extent actually read and used |
| --- | --- | --- |
| 18-24 | 26-32 | Section 1.2 opening, Definitions 1.1-1.2, examples and Theorems 1.1-1.4: outcomes/events, finite masses, finite additivity, partitions and the two-event union formula. |
| 133-149 | 141-157 | Section 4.1 through the beginning of its historical discussion: positive-event conditioning, Definitions 4.1-4.5, Theorem 4.1, joint/marginal and product laws, total probability/Bayes derivation, and examples including a small prior. |
| 225-240 | 233-248 | Section 6.1 through the conditional-expectation theorem/proof and following example: expectation, grouping, linearity, independent products, Definition 6.2 and Theorem 6.5. Intervening examples were read but are not reproduced or claimed as completed handbook treatments. |

The body pagination in this version has physical page = printed page + 8.
For mathematical glyph and layout confirmation, I additionally visually
inspected the complete title page and complete printed pages
19, 22, 23, 134, 139, 140, 141, 143, 146, 226, 230, 231, 233, 234, 239 and 240.
These were rendered directly from the saved PDF in memory at 100 dpi and
displayed for inspection; no new PNG files were written. The text extraction
has malformed glyphs in several mathematical fonts, so the visual reading
controlled the key definitions and displayed formulas. This is a record of
these actual read extents, not a claim to have read all 518 pages.

The `research` skill guided primary-source tracing and this single note;
the `pdf` skill guided source extraction and visual verification. The explicit
assignment prohibited subagents and controlled the research skill's delegation
suggestion. No manuscript PDF was built or rendered. The edition contract was
read completely before writing. Existing `handbook.sty` environment definitions
and a current editorial chapter were inspected to use the real theorem,
definition, example, warning and annex forms.

## Source relation and supplied proof components

The new exposition and proofs are independently written for a typed finite
model. They are not a transcription of the source's prose. In particular,
the source often calls a variable's value space its sample space and calls
atom weights a distribution function. The new chapter separates underlying
outcomes, variable values and their induced mass functions. It uses `mass
function` for atom weights and makes no density/point-mass identification.

| Body result | Exact source foundation | Supplied annex |
| --- | --- | --- |
| `thm:p15-finite-probability-laws` | Definition 1.2, pp. 19-20; Theorems 1.1-1.4, pp. 22-24 | `annex:p15.finite-laws`, lines 12-56: each stated finite identity and the converse unique atomic representation. The converse and support characterization are explicit finite deductions supplied here. |
| `thm:p15-finite-law-projection` | Joint and marginal construction, pp. 141-144; grouping principle, pp. 229-230 | `annex:p15.finite-law-projection`, lines 58-78: disjoint fibers, normalization, both marginals and function-of-variable law. |
| `thm:p15-finite-conditioning-laws` | Conditional reweighting and positive denominator, pp. 133-135 | `annex:p15.finite-conditioning`, lines 80-119: normalization, induced measure, multiplication, chain rule with every proper-prefix denominator guarded, and successive conditioning. |
| `thm:p15-finite-bayes` | Hypothesis partition and formulas (4.1)-(4.3), pp. 145-146 | `annex:p15.finite-bayes`, lines 121-149: total probability, posterior weights, null prior blocks, normalization and the derived odds identity. |
| `thm:p15-finite-independence-laws` | Definitions 4.1-4.4 and Theorem 4.1, pp. 139-143; product construction, p. 144 | `annex:p15.finite-independence`, lines 151-200: positive-event criterion, null events, complemented pairs, event-set/fiber equivalence and a normalized two-factor product model. |
| `thm:p15-finite-expectation-laws` | Definition 6.1, p. 226; Theorems 6.1-6.4 and explicit lack of a linearity independence hypothesis, pp. 230-234 | `annex:p15.finite-expectation`, lines 202-249: finite grouping, indicators, affine linearity including an empty sum, monotonicity and independent products. |
| `thm:p15-finite-total-expectation` | Definition 6.2 and Theorem 6.5, pp. 239-240 | `annex:p15.finite-total-expectation`, lines 251-284: partition averaging, the finite Y construction, its averaging property for all value events and almost-sure uniqueness. The last characterization is an explicit finite extension supplied here. |

The source's conditional formulas inherit the positive-event restriction
established on p. 134; the later compact conditional-expectation statement
does not repeat that guard. The chapter states it at every definition and
uses only the positive-mass index set J in total-probability and expectation
formulas. A null block contributes a zero unconditioned sum, never zero
multiplied by an undefined conditional quantity. A chosen value on a null
fiber in E[X | Y] is distinguished from a null-event conditional distribution.

The chapter defines mutual event independence by all nonempty subfamilies.
The source also displays an equivalent complemented-full-pattern formulation
on p. 141. That equivalent characterization is not asserted as an additional
theorem here. This finite unit uses the former definition, proves the stated
two-event complement facts, and supplies the pairwise/mutual counterexample.
The source's full collection of independence exercises and variants is not
claimed completed by this unit.

## Worked examples and author verification

The complete saved body and complete proof annex were read back; subsequent
definition clarifications, display adjustment and the expanded two-alert model
were also read back, producing the final 461-line body and 284-line annex. Every proof direction
was checked against its displayed hypotheses and the finite-sum definitions.
This is author reasoning and read-back, not independent acceptance or a test run.

The numerical example is a hypothetical inspection model, not an empirical
study. Its four weights 90, 10, 495 and 9405 sum to 10000. The checked exact
calculations are:

- Defect prior 100/10000 = 1/100; alert likelihoods 90/100 = 9/10 and
  495/9900 = 1/20; total alert probability 585/10000 = 117/2000.
- Posterior after one alert 90/585 = 2/13; posterior complement 495/585 =
  11/13. Prior odds 1/99 times likelihood ratio 18 give posterior odds 2/11.
- With prior 1/10 and unchanged likelihoods, the posterior is 2/3.
- The second model has explicit outcomes (h,u,v) in {0,1}^3 and masses
  pi_h r_h(u) r_h(v), normalized in the body. Conditional independence holds
  under each hypothesis by its product law. Two alerts then have joint
  defect mass 81/10000 = 324/40000 and joint nondefect mass 99/40000, giving
  324/423 = 36/47. Identical copied alerts retain posterior 2/13 instead.
- Conditional indicator means average to the prior:
  (585/10000)(90/585) + (9415/10000)(10/9415) = 1/100.

The other worked boundaries include a nonempty null event with an undefined
0/0 conditional ratio; three pairwise independent events on four equally
weighted points whose triple intersection is 1/4 rather than 1/8; loss of
independence upon conditioning on equal coordinates; and coincident indicator
variables whose expectations add but whose product expectation does not
factor. None uses an unstated independence premise.

## Root-owned bibliography intake

The new key `GrinsteadSnellChance2006` is used in both manuscript files and
is not yet in the canonical bibliography. Proposed entry, subject to the
root's existing intake/validation process:

```bibtex
@misc{GrinsteadSnellChance2006,
  author       = {Grinstead, Charles M. and Snell, J. Laurie},
  title        = {Grinstead and Snell's Introduction to Probability},
  howpublished = {The CHANCE Project},
  year         = {2006},
  note         = {Version dated 4 July 2006. This version is copyright
                  Peter G. Doyle and identifies its basis as the second
                  edition published by the American Mathematical Society,
                  copyright 2003 Charles M. Grinstead and J. Laurie Snell},
  url          = {https://math.dartmouth.edu/~prob/prob/prob.pdf},
  urldate      = {2026-09-07}
}
```

No unverified editor role, ISBN or publisher for the CHANCE revision has been
invented. The local capture is retained with its original notice. No source
figure or protected expository paragraph was copied into the chapter.

## Root-owned notation intake

All roles below are local to `ch:p15-finite-probability`; existing global
symbols should be reused or scoped through the canonical intake, preserving
other systems' meanings. No new macro or canonical symbol row was authored.

| Written role | Meaning and first anchor |
| --- | --- |
| Omega, omega, 2^Omega, p, P, A^c | Finite outcomes, outcome, all events, atom mass, event measure, relative complement; `def:p15-finite-probability-space` |
| X, S; p_X, p_{X,Y}; {X in D}, {X=x}; f(X) | Finite variable/value set, marginal and joint masses, inverse-image events and composition; `def:p15-finite-random-variable` |
| P(A given B), P_B, p_B | Conditional number, conditional event measure and conditional atom mass for P(B)>0; `def:p15-finite-conditioning` |
| H_i, E, pi_i, J, ell_i | Hypothesis partition, evidence, prior mass, positive-prior indices and likelihood; `def:p15-finite-hypothesis-partition` |
| q_1/q_0, prior/posterior odds | Likelihood ratio and ordinary real odds with stated denominator guards; `thm:p15-finite-bayes` |
| p_2(h,u,v), pi_h, r_h | Explicit two-alert model and local binary conditional laws; `def:p15-alert-bayes-case` |
| E[X], 1_A, {X=Y} | Finite real expectation, event indicator and equality event; `def:p15-finite-expectation` |
| E[X given B] versus E[X given Y], g(Y) | Conditional mean as number versus a finite random variable; zero-fiber representative convention; `def:p15-finite-conditional-expectation` |
| Q | Nonnegative normalized additive event function in the converse finite representation theorem; `thm:p15-finite-probability-laws` |

The table uses plain descriptions; the exact TeX spellings in the body are
authoritative. In particular probability is `\mathbb P`, expectation is
`\mathbb E`, and the indicator is `\mathbf1_A`. Distinguish the event measure
P from the variable's atom mass p_X, and distinguish the two conditional
expectation result types. Support, null event, almost surely, pairwise/mutual
independence and conditional independence have explicit definitions and
relevant index entries.

## Integration seam and remaining gates

The root owns the P15 part driver, P15 annex driver, main route, canonical
bibliography and symbols. After the required compatibility and intake work,
the intended body input is:

```tex
\input{parts/p15/finite-probability}
```

It belongs under stable part identity P15, printed XI, after P10 and before
the existing P11-P14 group. The corresponding annex input is:

```tex
\input{annex/p15/finite-probability}
```

The body opens a chapter and supplies four sections. The annex opens a
section and has seven `annexitem` records; their backreferences and the seven
`proved=annex:...` status targets match. The root must provide the owning
part/annex wrappers and stable identities. The new files themselves contain
no main/part-driver changes or independent style definitions.

Author result: supplied the complete assigned finite-scope content, definitions,
proofs, examples and boundary cases. No currently known mathematical gap is
left in these seven stated results. This author assessment is not a review
PASS. Next, the root can integrate the source/notation intake and drivers,
freeze the resulting dependency snapshot, and dispatch fresh independent
source, topic and publication reviewers. Static/build/visual and actual
admission gates remain to be performed at their required scope.

Only the two named manuscript files, this note, and the one named source
capture were created. The necessary empty P15 directories were created after
a scoped permission escalation. No tests, manuscript build/render, source
PDF edit, registry/provenance mutation, formal acceptance or subagent dispatch
was performed. Other agents' files were preserved.
