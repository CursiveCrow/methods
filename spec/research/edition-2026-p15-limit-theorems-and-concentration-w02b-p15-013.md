# w02b-p15-013 — Limit Theorems and Concentration (P15 161; sections 161.1, 161.2, 161.4, 161.5)

Label tag: `p15-w02b-p15-013`. Heading level: `\chapter`. toc tag:
`%% toc: P15 161 161.1,161.2,161.4,161.5`.

## Files

- Body: `handbook/parts/p15/limit-theorems-and-concentration-w02b-p15-013.tex`
- Annex: `handbook/annex/p15/limit-theorems-and-concentration-w02b-p15-013.tex`
- Symbol intake: `handbook/registry/symbols-intake-p15-limit-theorems-and-concentration-w02b-p15-013.csv`
- Editable host changed: `handbook/annex/p15/weak-convergence-exercises.tex`
  (the step "almost-sure convergence implies convergence in probability",
  formerly unstated, now cites `thm:p15-w02b-p15-013-as-probability` (1)
  and `thm:p15-weak-metric-premises`).
- No intake bib: only `DurrettPTEAuthor2019`, already in `handbook/bib/handbook.bib`.

## Source reading (this session)

Held file opened: `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`
(Durrett, *Probability: Theory and Examples*, author version 5, dated
11 January 2019), extracted with pdftotext; printed page numbers read
from the running heads.

| Locator written | Content checked |
|---|---|
| p. 56 | Section 2.2 opening: definition of convergence in probability, with strict inequality |
| Lemma 2.2.2, p. 57 | p > 0 and E|Z_n|^p -> 0 give Z_n -> 0 in probability (Chebyshev, Theorem 1.6.4) |
| Theorem 1.6.3, p. 29 | Hölder for p, q in [1, infinity] |
| Theorems 2.3.2-2.3.4, pp. 68-69 | subsequence criterion; topological subsequence lemma; continuous mapping in probability |
| remark, p. 69 | a.s. convergence comes from no topology; points to Exercises 2.3.14 and 2.3.11 |
| Exercise 2.3.11, p. 75 | independent Bernoulli(p_n): in probability iff p_n -> 0; a.s. iff sum p_n < infinity |
| Exercise 2.3.12, p. 75 | countable Omega with all subsets: in probability implies a.s. |
| Exercise 3.2.12, p. 124 | probability implies distribution; distribution to a constant implies probability |
| Theorem 4.4.6, p. 237 | martingale L^p convergence for p > 1 |
| Theorems 4.6.2-4.6.3, pp. 245-246 | superlinear moment criterion; UI <=> L^1 convergence <=> convergence of E|X_n| (given convergence in probability) |

Durrett states the UI criterion only at p = 1 and has no exercise in
Section 4.6 for general p (Exercises 4.6.1-4.6.7 checked). The general-p
criterion (`thm:p15-w02b-p15-013-vitali`), the inclusion L^p in L^q for
0 < q < p, the metric d_p for 0 < p < 1, and the five-model assembly are
written here as handbook results with complete proofs, attributed as
extensions.

Notation: Durrett's Exercise 2.3.11 writes X_n for the Bernoulli
variables; the handbook writes B_n because X_n is the chapter's generic
sequence (recorded in the symbol intake). Durrett's p_n is kept.

## Existing treatments found and linked (not duplicated)

- `def:p15-lp-convergence`, `def:p15-lp-conditional-spaces`,
  `def:p15-w02b-p15-001-lp-space`, `thm:p15-w02b-p15-001-lp-results`,
  `def:p15-w02b-p15-001-lp-limits` (p < 1 triangle failure): extended to
  every p > 0 by `def:p15-w02b-p15-013-modes` and `thm:p15-w02b-p15-013-power`.
- `thm:p15-direct-variance-weak-laws` (2): Lemma 2.2.2; reused in the
  comparison proof.
- `thm:p15-probability-l1-tools` (2): one direction of Durrett 2.3.2; reused.
- `thm:p15-weak-metric-premises`: Exercise 3.2.12; reused.
- `thm:p15-vitali-convergence`, `thm:p15-ui-small-sets`,
  `thm:p15-ui-moment-criteria`: p = 1 base of the general-p theorem.
- `thm:p15-ui-counterexamples` (1), `def:p15-convergence-failures`,
  `thm:p15-maximal-convergence-boundaries` (1),
  `thm:p15-weak-convergence-boundaries` (3), martingales-and-convergence
  lines 228-238: isolated separating cases, now cited as instances of
  models (1) and (4) and of the probability-not-a.s. phenomenon.
- Not listed in the packet's "existing" list and found here:
  `thm:p15-event-limit-calculus`, `thm:p15-borel-cantelli-first`,
  `thm:p15-borel-cantelli-second` (limsup-events-and-zero-one-laws.tex),
  `thm:p15-independent-sequence-existence` (countable-product-measures.tex),
  `thm:p15-expectation-bounds` (integration-expectation.tex),
  `thm:p15-lebesgue-unit-interval` (measure-extension.tex),
  `thm:p15-martingale-lp-convergence` (martingale-maximal-inequalities.tex),
  `def:p15-w02b-p15-001-lp-space` and `thm:p15-w02b-p15-001-lp-results`
  (probability-spaces-and-random-variables-w02b-p15-001.tex).

## Placement

Packet proposal followed: body `\input{parts/p15/limit-theorems-and-concentration-w02b-p15-013}`
after `parts/p15/variance-and-dependent-concentration` in
`handbook/parts/p15.tex`; annex
`\input{annex/p15/limit-theorems-and-concentration-w02b-p15-013}` after
`annex/p15/variance-and-dependent-concentration` in `handbook/annex/p15.tex`.
The lead may prefer placing it directly after
`uniform-integrability-and-conditional-limits`, whose p = 1 theorem it
extends; the edited exercise annex refers forward to it in either placement.

## Continuation

Status at return (block 1):

- 161.1 US-0 duty: the named comparison is written in the owned body and
  annex files: definitions for every 0 < p < infinity, power inequalities
  and metrics, L^p in L^q, a.s. => probability with Durrett 2.3.2-2.3.4,
  the no-topology remark and Exercise 2.3.12, the comparison theorem with
  the twelve failing ordered pairs enumerated in the annex, the general-p
  UI criterion, five separating models parameterized by p (with the
  p = 1, 2, 1/2 instances named), the finite-mass limitation, method,
  worked example, warning and relationships. Defects (a)-(e) of the
  assessment are each addressed by a named label (see return JSON).
- No new work started on 161.2, 161.4, 161.5 in this block; their
  components map to existing environments listed in the return JSON.
- Checks run: unit-compile ok with 0 overfull boxes; find_fused_spaces
  clean; check.py --tree handbook shows no finding in the owned files or
  the edited host.
- Open items: none known for the US-0 duty. The lead must add the two
  `\input` lines (blocked_policy: drivers are read-only here) and merge
  the symbol intake.
