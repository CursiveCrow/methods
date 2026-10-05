# Research note: P15 160.9, Feller continuations (packet w02b-p15-012)

Owned files:

- handbook/parts/p15/distributions-transforms-and-moment-problems-w02b-p15-012.tex
- handbook/annex/p15/distributions-transforms-and-moment-problems-w02b-p15-012.tex
- handbook/registry/symbols-intake-p15-distributions-transforms-and-moment-problems-w02b-p15-012.csv

Label tag: `p15-w02b-p15-012`. No new bibliography keys: every citation uses
`Feller1971ProbabilityII` from handbook/bib/handbook.bib, so no intake bib was created.

## Source and locators

Held file: source/references/feller-probability-volume2-second-edition/feller-volume2-second-edition.pdf
(Feller, An Introduction to Probability Theory and Its Applications, vol. II, 2nd ed.).
PDF page index = printed page + 14 in chapters VII-XV. Every page and equation
number below was read in this session, from the text layer and, for formulas,
from rendered page images (pp. 353-355, 431, 433, 462-463, 507-509).

| Presentation | Feller locator | Handbook labels |
|---|---|---|
| Uniqueness thm 1, translation principle (1.9), thm 1a, corollary | XIII.1 pp. 430-433 | thm:p15-w02b-p15-012-laplace-uniqueness |
| Continuity theorem (thm 2) | XIII.1 p. 431 | thm:p15-w02b-p15-012-laplace-continuity |
| Extended continuity theorem (thm 2a), example (g) | XIII.1 pp. 433-434 | thm:p15-w02b-p15-012-laplace-extended-continuity, -laplace-continuity-examples |
| Convergence of measures (recalled from VIII.1, VIII.6) | XIII.1 p. 433 | def:p15-w02b-p15-012-vague, thm:p15-w02b-p15-012-vague-tools |
| Parseval (3.1)-(3.4), thm 1, lemma, thm 2, corollary | XV.3 pp. 507-509 | thm:p15-w02b-p15-012-parseval, -cf-uniqueness, -cf-lemma, -cf-continuity, -cf-examples |
| Space, contractions, semigroups, (8.7) | X.8 pp. 350-352 | def:p15-w02b-p15-012-semigroup, thm:p15-w02b-p15-012-semigroup-continuity |
| Thm 1 (9.1)-(9.2), thm 2 (9.3)-(9.6), variant (9.7)-(9.11) | X.9 pp. 353-355 | thm:p15-w02b-p15-012-pseudo-poisson, -semigroup-exponential, -subordinated-variant, -semigroup-examples |
| Integral (9.1)-(9.5), resolvent (9.6), lemma, thm 2 (9.13)-(9.14) | XIII.9 pp. 454-457 | def:p15-w02b-p15-012-resolvent, thm:p15-w02b-p15-012-semigroup-integral, -resolvent-limit |
| (10.25), thm 3 (10.24) | XIII.10 pp. 462-463 | thm:p15-w02b-p15-012-resolvent-derivatives, -abstract-inversion, -resolvent-examples |

Source observations recorded in reader text:

- XV.3 (3.4) is printed with constant 1/sqrt(2 pi); dividing (3.3) by a sqrt(2 pi) gives 1/(2 pi).
  Feller's "G = N_a" with density a n(a x) has variance a^{-2}; the text avoids the clash by
  naming N_a only for variance a^2.
- X.9 (9.6) prints the good range as |nh - t| < eta t; the proof needs |nh - t| < delta.
- X.9 (9.11) is printed without the factor t and asserted "formally"; the handbook proves it
  with the factor t, taking (9.7) as the definition of the weights and assuming m_1 > 0, m_2 < infinity.
- VII.6 p. 233 says the abstract version of (6.6) appears in XIII.9. The formula itself is
  XIII.10 Theorem 3, (10.24), p. 462, built on the XIII.9 resolvent; Feller identifies it with VII,(1.6).
  The statement of (10.24) is written "as lambda -> infinity"; the limit variable is n.
- XIII.9 Lemma uses the XIII.1 corollary (stated for measures, hence nonnegative u) on a function
  that may change sign; the annex uses (6.6) instead, as Feller's bracket on p. 433 suggests.
- XV.3 Theorem 2 sufficiency uses only continuity of the limit at the origin.

Proof substitutions (Feller cites results not otherwise presented here):

- Feller's selection theorem of VIII.6 is replaced by Durrett's selection construction
  (thm:p15-helly-selection) plus the non-atom partition lemma (thm:p15-w02b-p15-012-vague-tools).
- Feller's corollary of VIII.1 (uniform convergence of characteristic functions) is proved
  directly from tightness (thm:p15-weak-tightness-selection) and equicontinuity.
- Bochner integrals in XIII.9 are replaced by pointwise integrals shown to be norm limits of
  Riemann sums.

Existing treatments found: Durrett's continuity theorem thm:p15-characteristic-continuity-theorem
(linked, not duplicated); Durrett's Helly selection and tightness (used). No prior handbook
treatment of a Laplace-transform continuity theorem, of semigroups or of resolvents was found
(searched parts/ and annex/ for "semi-group", "semigroup", "resolvent", "Hille", "Laplace transform").

Block 2 additions (read this session from the held Feller II PDF, text layer and rendered
pages 444-446 and 524-526 of the PDF = printed pp. 429-431 and 509-511; text layer for
XV.1-XV.2 pp. 500-505 and XV.3 pp. 507-511):

| Presentation | Feller locator | Handbook labels |
|---|---|---|
| Theorem 1 second proof, (1.4) | XIII.1 p. 430 | thm:p15-w02b-p15-012-laplace-integer-values |
| Examples (a)-(f), (1.3), (1.6), (1.7) | XIII.1 pp. 430-431 | thm:p15-w02b-p15-012-laplace-xiii1-examples |
| Example (a), convolution powers | XV.3 p. 508 | thm:p15-w02b-p15-012-convolution-powers |
| Example (b), Polya criterion; polygon case | XV.3 p. 509; XV.2 example (b) pp. 504-505 | thm:p15-w02b-p15-012-polya-feller |
| Theorem 3 (3.5), corollary (3.7) | XV.3 pp. 509-510 | thm:p15-w02b-p15-012-fourier-inversion |
| Examples (c)-(e), (3.8)-(3.12) | XV.3 pp. 510-511 | thm:p15-w02b-p15-012-xv3-inversion-examples |
| Theorem 4 (3.13)-(3.14) | XV.3 p. 511 | thm:p15-w02b-p15-012-lattice-inversion |

Block 2 source observations recorded in reader text:

- XIII.1 example (c) prints the exponent as alpha+1 with parameter a; the computation gives a+1.
- XV.3 example (b) prints only "real even, omega(0)=1, convex graph on [0,inf)". XV.2 example (b)
  adds omega >= 0 and a last side on the axis. Counterexamples 1+zeta^2, -1/2+3/2 e^{-|zeta|}
  and 1_{0} show nonnegativity, monotonicity and continuity at 0 are needed.

Block 2 proof substitutions:

- XV.3 example (a): Feller's lemma 4 of XV.1 (p. 501) is replaced by a Tonelli argument showing
  {omega=1} is Lebesgue-null; the symmetrization step is written out with the bound
  G^{n*}{I}^2 <= (0G)^{n*}{[-l,l]}.
- XV.3 example (c): Feller's "left side equals 0f(0)" is made rigorous by normal smoothing,
  L^1 convergence of the smoothed densities (approximation from thm:p15-criteria-real-integration),
  Fatou along an a.e. subsequence, and the Cauchy-Schwarz bound 0f <= int f^2.
- XV.3 example (b): the polygon case is taken from thm:p15-criteria-polya (finite-piece case);
  Feller's inscribed-polygon limit and his corollary are written out.
- XIII.1 second proof: Riemann-sum matching replaced by the image-measure rule
  (thm:p15-expectation-law-integral); extension to defective F added and proved.

Existing treatments linked, not duplicated: thm:p15-characteristic-integrable-inversion (Durrett 3.3.14,
same statement as Feller Theorem 3, different proof), thm:p15-characteristic-atom-inversion (lattice
formula, same as (3.14)), thm:p15-criteria-polya (Durrett 3.3.22), thm:p15-characteristic-inversion-uniqueness.
Also fixed four aligned-environment line breaks written as a single backslash in the annex.

## Continuation

State after block 2 (C020 is still the only open component; it remains partial):

- Written in block 1: VII.5-VII.6, XV.4, XIII.1 Theorems 1, 1a, corollary, 2, 2a, example (g);
  XV.3 Parseval (3.1)-(3.4), Theorem 1, lemma, Theorem 2 and corollary; X.8-X.9; XIII.9 (9.1)-(9.6),
  lemma, Theorem 2; XIII.10 (10.25) and Theorem 3.
- Written in block 2 (body 612-683, 808-962, warning 1247-1275; annex 793-886, 1039-1321):
  XIII.1 Theorem 1 second proof and examples (a)-(f); XV.3 examples (a)-(e), Theorem 3 and its
  corollary, the note (3.12), and Theorem 4.
- Still open under C020:
  1. Original Hausdorff papers (Math. Z. 9 (1921) 74-109 and 280-299; Math. Z. 16 (1923) 220-248),
     Heyde (J. Roy. Statist. Soc. Ser. B 25 (1963) 392-393), and the Feller XIII.1 footnote 1 source
     (W. Feller, On Muntz' theorem and completely monotone functions, Amer. Math. Monthly 75 (1968)
     342-350): not held; blocked_source.
  2. Not yet supplied from held Feller pages: XIII.9 Theorem 1 (9.8)-(9.12), Corollaries 1-3 and
     examples (a)-(b) (pp. 456-458), which need the generator of X.10 (not yet read); XIII.10
     Hille-Yosida material other than Theorem 3 (pp. 458-462).
- Next step: read X.10 (generators) in the held file, then XIII.9 Theorem 1 with corollaries, then
  XIII.10 pp. 458-462.
- Checks run in block 2: unit-compile ok (0 errors, 58 overfull); find_fused_spaces clean;
  check.py --tree handbook shows no finding in the owned files.
