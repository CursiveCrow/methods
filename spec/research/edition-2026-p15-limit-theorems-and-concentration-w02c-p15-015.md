# Edition 2026, P15 chapter 161 (sections 161.2, 161.4, 161.5, 161.9): packet w02ca-p15-015

Label tag: `p15-w02c-p15-015`. Owned body/annex:
`handbook/parts/p15/limit-theorems-and-concentration-w02c-p15-015.tex`,
`handbook/annex/p15/limit-theorems-and-concentration-w02c-p15-015.tex`.

## Sources opened in this session

- Durrett, *Probability: Theory and Examples*, author Version 5 dated
  11 January 2019 (`source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`,
  key `DurrettPTEAuthor2019`). Read PDF pp. 152-165 (book pp. 144-157),
  PDF p. 131 (book p. 123), contents (Section 3.8 Stable Laws at book
  p. 182; Section 3.6 is Poisson Convergence), PDF pp. 83-84 (Theorem 2.4.1,
  book p. 76).
- Feller, *An Introduction to Probability Theory and Its Applications*,
  vol. 2, 2nd ed. (`source/references/feller-probability-volume2-second-edition/feller-volume2-second-edition.pdf`,
  key `Feller1971ProbabilityII`). Read ch. XVI sec. 5, printed p. 542,
  footnote 7 (the sentence Durrett quotes on book p. 157).

- Feller vol. 2, 2nd ed. (same file), opened again in block 1 of the
  continuation run: printed p. 2 footnote 3 and p. 4 (I.2: barred
  interval a,b denotes the open interval {a<x<b}), p. 137 (V.2 median
  paragraph), p. 148 (V.5 symmetry with the bracketed density form,
  (5.1)-(5.3)), pp. 234-235 (VII.7: (7.1)-(7.5), the remark that (7.4)
  holds for dependent variables with varying distributions, the "oldest
  version" and "Khintchine's law" statements). PDF page = printed page + 16.

## Provenance and corrections

- Durrett's Remark after Example 3.4.13 (book p. 152) sends the reader to
  "Section 3.6" for power tails with exponent below two. In Version 5 the
  stable laws are Section 3.8 (contents, book p. 182); Section 3.6 is
  Poisson convergence. The handbook states the corrected pointer and proves
  the remark directly by characteristic functions.
- Durrett's Berry-Esseen remark that the third-moment hypothesis is
  "needed" for the n^{-1/2} rate (book p. 157) is given in the reader text
  in the precise form supported by the theorem he cites (Heyde 1967 as
  reported): an O(n^{-1/2}) rate forces finite moments of every order
  2+delta with 0<delta<1. Open item: finiteness of the third moment itself
  is not necessary for an O(n^{-1/2}) rate (Ibragimov's 1966 criterion);
  that source is not held, so the reader text says only that the source
  does not prove necessity of the third moment and makes no further claim.
- Heyde (1967), van Beek (1972), Hall (1982), Gnedenko (1943), Resnick
  (1987), Gnedenko-Kolmogorov (1954) are cited only through Durrett's own
  remarks; none of these works was opened, and no new bibliography key is
  introduced.

- Feller's Lemma (7.5) (VII.7, p. 235) prints the coefficient
  1/(n^2 x^2) in front of E(X_1'^2); his own sufficiency proof uses
  1/(n x^2) (the bound eps^{-2} sigma(n) + tau(n)). The reader text states
  the n^{-1} coefficient and points to item 5 of
  thm:p15-feller-proof-boundaries, which shows the printed one fails.
- Feller's median remark (V.2, p. 137) is for his barred, i.e. open,
  interval (I.2, p. 4); the reader text proves it and adds that the two
  endpoints are medians too.

## Continuation

State at return of block 1 (2026-10-10):

- Written in owned chapter (body + annex, not yet on the input route;
  insertion proposal in the return JSON): CLT C001 (chi notation, chi-square
  lemma), C005 (roulette model, histogram rule, exact consistency theorem,
  sixteen-toss example with 0.1974 vs 0.1964 and the 11.5 reading), C006
  (pairwise contrast corollary), C019 (truncation window lemma, power-tail
  nonnormal limit theorem, corrected Section 3.6 -> 3.8 pointer), C025
  (exp(e^4) arithmetic), C029 (Berry-Esseen remarks, rate-series lemma,
  reported-results proofboundary), C030 (Levy attribution and
  Gnedenko-Kolmogorov remark); weak-laws C011 (non-strict maximal
  inequality, full first-crossing proof).
- Edited editable hosts: Feller annex (non-strict largest-term comparison
  and q_>= / V.(5.10) chain written out, C005); weak-convergence-exercises
  body (Exercise 3.2.2 closing remark, boundary rewritten; C003, C013).
- Patch requests (work/waves/w02ca/patches/w02ca-p15-015.json): replace
  the CLT host boundary def:p15-clt-current-boundary (C030); insert chi
  pointer in def:p15-clt-notation (C001); weak-laws host body pointer to
  the non-strict lemma (C011); weak-laws host body Section 3.3 exercise
  locations including thm:p15-w02c-p15-012-bound-gives-growth (C015);
  weak-laws host annex sketch replaced by pointer (C011).
- Open: weak-laws C015 clears only when the lead applies the patch and
  places the w02c-p15-012 file on the route. The owned chapter cites
  thm:p15-w02c-p15-012-bound-gives-growth, so that file must precede it
  on the route. Readonly units (criteria-and-moments, owner w02c-p15-012;
  weak-convergence-of-laws, owner w02c-p15-004) are not written here.
- Checks run: find_fused_spaces (no hits), waves.py unit-compile (ok),
  check.py --tree handbook (no finding in the owned or edited files).

Continuation run, block 1 (2026-10-10):

- Written in the editable Feller host (body
  handbook/parts/p15/feller-weak-law-presentation.tex, annex
  handbook/annex/p15/feller-weak-law-presentation.tex):
  feller C002 median set (body 67-96, annex 64-116,
  thm:p15-w02c-p15-015-median-set); feller C001 density form of symmetry
  (body 98-120, annex 118-166, thm:p15-w02c-p15-015-density-symmetry);
  feller C009 general (7.4) lemma and complete-dependence example (body
  256-314, annex 447-486), the i.i.d. bound now derived from it (body
  332-339, annex 488-509); feller C011 historical remarks (body 382-399).
- Central-limit-theorems C001, C005, C019, C025, C029, C030: content is in
  the owned chapter; the only remaining step is the lead's \input of the
  owned body and annex files (reported blocked_policy with the exact
  driver change).
- Checks: find_fused_spaces no hits; waves.py unit-compile ok;
  check.py --tree handbook has no hard finding in the edited files (the
  host's notation-scope notes for \mathbb P and \mathbb E are soft and
  predate this block).

Run r4, block 1 (2026-10-10):

- Sources opened: Feller vol. 2, 2nd ed., printed pp. 149 (V.5: (5.4),
  (5.5), the "messy arguments" sentence before Lemma 1, the sentence
  before Lemma 2), 234 (VII.7 heading footnote), 235, 236 (remarks after
  Theorem 1), 237-238 (VII.8 opening), 241 (VII.8 Theorem 4, (8.19)),
  58 (II.7, (7.1) Bessel I_p). PDF index offset is 15 up to about p. 150
  and 14 from about p. 234 (0-based index = printed + 15 or + 14).
  Theorem 4 sits on p. 241 under the VII.9 running head; Feller's p. 236
  text places it in section 8.
- Written in the editable Feller host: C003 (body 124-135), C005 (body
  176-185), C010 (body 408-418), C011 (body 436-486; annex 623-750,
  thm:p15-w02c-p15-015-mean-versus-tau and
  thm:p15-w02c-p15-015-strong-law-converse), C012 (body 515-551, annex
  801-852, thm:p15-w02c-p15-015-atomic-symmetrization; boundary
  def:p15-feller-next-boundary rewritten, no longer defers (5.5)).
- Provenance: the strong-law converse proof follows Feller's route
  (second Borel-Cantelli, then symmetrization) but replaces his appeal
  to a zero-one property by the product-space argument
  P(B)^2 = Q(B x B') = 0. The geometric case of (5.4) is a handbook
  worked example, not a Feller formula.
- CLT C001, C005, C006, C019, C025, C029, C030: unchanged; content in
  the owned chapter, waiting for the lead's \input and the CLT host patch.
- Checks: find_fused_spaces no hits; waves.py unit-compile ok; check.py
  shows only the pre-existing soft notation-scope notes for \mathbb P
  and \mathbb E in the Feller host.

Run r5, block 1 (2026-10-11):

- Source opened: Feller vol. 2, 2nd ed., printed p. 236 (PDF index 250):
  the remark after the proof of Theorem 1 is stated for symmetric F with
  t[1-F(t)] -> 0, conclusion P{|n^{-1}S_n| > eps} -> 0.
- Feller C011 closed in the editable host: thm:p15-w02c-p15-015-mean-versus-tau
  (body 448-474, new sentence 458-463) now states that for symmetric F,
  P(|X|>t) = 2[1-F(t)], so t[1-F(t)] -> 0 iff tau(t) -> 0, and then the
  weak law holds; annex 649-668 proves it from 1-F(t) = F((-t)-),
  thm:p15-feller-tail-moment-equivalence and the symmetric clause of
  thm:p15-feller-centering-corollaries.
- Patch file: added insert_after records for the two driver \input lines
  (parts/p15.tex after the w02b-p15-063 input; annex/p15.tex likewise).
- CLT C001, C005, C006, C019, C025, C029, C030 and weak-laws C011: content
  unchanged in the owned chapter; still waiting for the lead's \input.
- Checks: find_fused_spaces no hits; waves.py unit-compile ok; check.py
  shows only the pre-existing soft notation-scope notes in the Feller host.
