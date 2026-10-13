# Packet w02ca-p15-017 (P15, sections 161.3 and 161.12): provenance note

Label tag: `p15-w02c-p15-017`. Owned body/annex files are new; edited hosts are
`handbook/parts/p15/variance-and-dependent-concentration.tex` and its annex.

## Sources opened in this session

- Hoeffding 1963, held file `source/references/hoeffding-bounded-sums-1963/hoeffding-1963.pdf`
  (JSTOR scan, journal pp. 13-30; PDF page k = journal page k + 11). Scanned images,
  no text layer. Read PDF pages 2-9 and 12-19 (journal pp. 13-20, 23-30), with
  zoomed crops of p. 17 (Doob citation line) and p. 20 (small bt/sigma^2 sentence).
  Locators used: p. 13 (1.6); p. 15 n. 4; p. 16 (Bennett (8b), |X_i|<=b vs X_i<=b,
  pp. 42-43 of Bennett); p. 17 (Bennett: (2.12) better than (2.13); Doob [7, p. 314]);
  p. 18 (Kolmogorov analogy via Feller [5, p. 220]; Section 3 ratio criterion);
  p. 20 ((3.15); approximation exp(-nt^3/(6b sigma^2)) when bt/sigma^2 small);
  p. 24 (alternative direct proof of (2.9); (5.2); "rather crude but may be useful");
  pp. 25-26 ((5.8) two-sample U statistic); p. 26 ((5.13) Cramer-von Mises);
  p. 28 ((6.2); Var Xbar <= Var Ybar special case); p. 29 (n = 2 symmetrized kernel;
  reference list items [2] Bennett 1962, [4] Doob 1953, [7] Hardy-Littlewood-Polya).
- Durrett, held file `source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`,
  text layer pp. 81-82: definition of F'_n and T (p. 81); Theorem 2.5.3 proof steps
  (a), (b) and the inclusion T in sigma(X_1, X_2, ...) (pp. 81-82).

## Source observations recorded for the reader text

- p. 17 prints "a theorem of Doob, [7, p. 314]"; item [7] of the reference list is
  Hardy, Littlewood and Polya, and Doob's Stochastic Processes is [4]. The body
  states both facts rather than silently correcting the bracket.
- p. 20: the approximation of B_1/B_2 by exp(-nt^3/(6b sigma^2)) holds to leading
  order in the exponent only when t/b is also small. With t/b fixed and
  bt/sigma^2 -> 0 the exponent factor tends to 6 rho(w)/w > 1 + w/2
  (18 - 24 log 2 at w = 1/2). Smallness of bt/sigma^2 suffices when sigma^2 <= b^2.
  The body states the precise two-sided bound and the qualification.
- p. 15 n. 4, Theorem-3 sentence: proved as a sharp supremum over the class without
  X_i <= b, with a one-summand two-point witness; also shows (1.6) remains the
  least uniform bound under X_i <= b whenever b >= nt.

## Mathematical content written here (no source)

- The coin enlargement Omega' x {0,1}: H_infinity is inside the rectangle field
  G, {Y = 1} is not in G, P(A sym-diff B) = 1/2 and independence for every A in
  H_infinity; canonical-product equality H_infinity = F.
- Kolmogorov's maximal inequality proved by first crossing (to make the source's
  analogy precise).

## Round 2 (2026-10-10, after the session limit reset): sources reread

- Hoeffding 1963 held PDF re-rendered at 300 dpi (pdftoppm) in this session: PDF pp. 2-5
  (journal pp. 13-16, with footnote crops of pp. 13, 14, 15), PDF pp. 7-9 and 11 (journal
  pp. 18-20, 22), PDF pp. 18-19 (journal pp. 29-30, reference list).
- Locators verified and used: p. 13 (names of (1.5) Bienayme-Chebyshev and (1.6)
  Chebyshev; t>0 assumed since no nontrivial bound for t<=0); p. 13 n. 2 (attribution
  history of (1.6), Chebyshev [14]); p. 14 (Bernstein attribution of the exponential
  method; surveys Godwin [6], Savage [13], Bennett [2]; Bennett's (2.12) and comparisons);
  p. 14 n. 3 second half (approximations via the minimized bound, Bahadur and Rao [1];
  exact bounds not approximations); p. 15 n. 4 (referee provenance; improvement over
  Markov when n and t not too small); pp. 15-16 (Okamoto [11] binomial case except (2.2)
  with mu<1/2; (2.1) implicit in Chernoff [3, Thm 1 and Example 5]); p. 18 (Section 3
  purpose and ratio criterion); p. 19 (reading of (3.6)-(3.7)); p. 20 ((2.8) increasing
  in sigma^2); pp. 29-30 (reference list items [1], [2], [3], [6], [11], [13], [14]).
- No new bibliography keys: the cited works are described through Hoeffding's list and
  cited to Hoeffding with page locators; none of them is held or was read.

## Mathematical content written in round 2 (no source)

- t<=0: constant witnesses (Theorems 1-2 classes); two-point witnesses with
  q <= b^2/(b^2+n sigma^2) giving Pr >= 1-q (Theorem 3 class).
- Markov comparison: n=1 strict A_1 > p/(p+t) via (1-q) ln(q(1-p)/(p(1-q))) > 0;
  chi-square bound D(q||p) < (q-p)^2/(p(1-p)) and ln(1+x) > x/(1+x) give
  A_1 > p/(p+t) when nt(p+t) <= p(1-p); ln(1+x) < x gives A_3 < p/(p+t) when 2npt > 1;
  example p=1/2, t=1/4: improvement exactly for n >= 4.
- Reading corollary for (3.6)-(3.7) with example p=3/4, t=1/8 (U=e^{-n/216}, L=e^{-n/48}).
- Strict increase of B_1 in sigma^2 from f_c' > 0 and the attained minimizer h_*.

## Continuation

State at return (2026-10-10, round 2):
- 161.3 C006: written in owned files (round 1); needs driver insertion (lead) and the
  cross-reference patch in work/waves/w02ca/patches/w02ca-p15-017.json.
- 161.12 bounded C002, C004 (1)-(3), C005, C008 (1)-(3): written in the variance host,
  new section sec:p15-w02c-p15-017-hoeffding-scope (body) with annex items
  annex:p15-w02c-p15-017-nonpositive-deviation, -markov-comparison,
  -section-three-reading. Cross-reference patches for the read-only bounded host and
  the sequential-evidence host filed in the patch file (5 entries in total).
- Variance C006: strict increase written (body line 230, annex proof in
  annex:p15.variance-bound-comparison).
- unit-compile ok (owned files, 0 overfull); scratch unit build of the variance host ok
  (36 overfull, the new ones at theorem heads with long labels); fused-space check
  clean; check.py: no hard finding in edited or owned files.
Nothing further is queued for this packet.
