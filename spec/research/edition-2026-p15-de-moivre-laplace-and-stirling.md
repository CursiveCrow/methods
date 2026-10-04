# P15.24 author return: the distinct Stirling route

Date: 8 September 2026. The assigned body and annex are saved with
eleven complete reciprocal statement/proof pairs. All writing and
corrections precede consolidated reviews.

Files:

- handbook/parts/p15/de-moivre-laplace-and-stirling.tex
- handbook/annex/p15/de-moivre-laplace-and-stirling.tex
- This single source/notation note.

Root retains shared routes, notation, progress and older boundaries.
The additional source acquisition and preservation were expressly
authorized by root during this block.

## Verified and preserved Feller referral

Canonical file:
source/references/feller-probability-volume1-third-edition/feller-volume1-third-edition.pdf.
SHA-256:
5779C397AC16CA0E7E5C37E2B84D4C29CBA081F7F6E31D03FEDF27DA80678F58.
Size: 36,816,618 bytes. PDF pages: 524.
MD5: 3EDB18869B6F4EBFDA4E3FDA340C2952, matching the
[Zenodo download record](https://zenodo.org/records/7108309).

The actual title page says Volume I, Third Edition, Revised Printing,
John Wiley & Sons. The copyright page includes 1968 and catalog
number 68-11708. Both complete page images were read.
The [publisher edition record](https://www.wiley-vch.de/en/areas-interest/mathematics-statistics/statistics-16st/probability-mathematical-statistics-16st1/introduction-to-probability-theory-and-its-applications-978-0-471-25708-0)
confirms third edition, January 1968, ISBN 978-0-471-25708-0.
That is the edition's bibliographic year; the precise physical
revised-printing year is not asserted.

The unchanged staged copy remains at:
C:/Users/Crow/Documents/Codex/2026-08-10/phase-4-handover-migration-campaign-written/tmp/pdfs/p15-stirling-source/feller-volume1-candidate.pdf.
The narrow permission grant did not permit creation of the missing
canonical directory; the exact authorized import succeeded with
an escalated command. Canonical and staged SHA-256 values match.
Root added Feller1968ProbabilityI; the actual entry was personally read.
The full required source extent is present. Whole-book leaf completeness
is not claimed merely from the page count.

## Complete reading

Durrett: author Version 5, 11 January 2019, at
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf.
SHA-256:
AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886.
Reuse DurrettPTEAuthor2019.

Read the entire exact Section 3.1, printed pp. 113–115,
physical pp. 121–123: complete factorial factorization,
Lemma 3.1.1 and proof, Theorems 3.1.2–3.1.3, every continued
Riemann-sum/parity step, all four exercises and their leads.
All three whole source page images were read.

Feller: read the logarithmic-series premise on printed p. 51
and the full II.9 proof/refinements on pp. 52–54, physical
pp. 66–69. All three Stirling proof-page images were read.
Followed the p. 53 constant referral to the full VII.2 argument
on pp. 179–181, physical pp. 194–196, especially footnote 3
on p. 180; read pp. 180–181 as full source images.
The continued p. 182 discussion was read to delimit the separate
later error estimates.

Read the actual VI.(3.5) binomial-tail premise and its complete
ratio/central-term proof on pp. 150–151, physical pp. 165–166;
read the whole p. 151 image. Adjacent binomial-law/context
pp. 148–149 were read.
Read the Gaussian normalization/tail discussion on pp. 174–179,
physical pp. 189–194, including the continued proof of VII.(1.8).
The normal table/figure pages were context; their transcription
is not claimed.

Both required source tail proofs are supplied here. Gaussian
normalization is the already written independent Gaussian integral.
The optional second constant determination uses the independent
cosine-integral central-coefficient proof from P15.23. Neither
prerequisite uses Stirling or a normal-limit theorem.

## Eleven complete statement/proof pairs

Each suffix uses body prefix thm:p15- and reciprocal proof
prefix annex:p15. followed by the same suffix.

| Suffix | Complete scope |
| --- | --- |
| stirling-log-tools | Finite logarithmic remainders; source scalar Lemma 3.1.1 and triangular Exercise 3.1.1. |
| stirling-tail-premises | Binomial law/moments, both Feller tail bounds and full Gaussian tail-bound proof. |
| stirling-with-remainder | II.9 logarithmic proof, Robbins bounds, Feller VII.2 constant argument, independent constant determination and quantified refinement. |
| stirling-local-rademacher | Exact source factorial factors, all three factor limits, explicit uniform logarithmic error, both lattice parities and extreme points. |
| stirling-de-moivre-laplace | Full Theorem 3.1.3, finite rounding, controlled Riemann sums, source odd-index step, strict/singleton/infinite endpoints and CDF limits. |
| stirling-poisson-premises | Probability normalization, all used moments and exact independent summed law. |
| stirling-poisson-normal | Full Exercise 3.1.2, uniform local error and the complete indicated interval/CDF consequence. |
| stirling-rademacher-tail-rate | Exercise 3.1.3: point-mass asymptotic and geometric-tail comparison, ceilings and all endpoint regimes. |
| stirling-poisson-tail-rate | Exercise 3.1.4: first-term/geometric-tail proof and separate boundary regimes. |
| stirling-general-binomial | Explicit fixed-p extension through a separate factorial/Taylor calculation and concrete interior derivative bound. |
| stirling-worked-boundaries | Relative/absolute factorial error, calculations, independence failure, global relative-approximation failure and a changing-p countermodel. |

The even-binomial logarithmic relative error is bounded by
(A^4/18 + A^2/3 + 3/8)/n on scaled windows of radius A,
for n at least max(1,2A^2).
The Poisson logarithmic error is at most
(2A^3/3 + A)/sqrt(n) + 1/(6n) eventually.
Both probability-limit arguments therefore use proved uniform
estimates, not unqualified pointwise approximations.

## Direct qualifications and corrections

- Feller's constant is initially unknown, A = exp(C). The
  source central-ratio, interval-mass and tail comparison
  forces A = sqrt(2 pi). The cosine-integral determination
  is a separate route, not a substitute for the source argument.
- Zero factorial indices and wrong-parity points use their
  exact combinatorial values; r_0 is never introduced.
  Real thresholds use explicit ceilings/floors and empty sums.
- The source illustrative equality of a lattice displacement
  with a scaled real position is expressed through the actual
  integer-sequence limit. Negative and zero displacements
  do not rely on an inapplicable positive-exponent assumption.
- Feller's refinement is proved with the explicit stronger
  remainder 6/(5 n^5), after both Robbins inequalities.
  Every finite Taylor remainder used for it is bounded.
- At n = 5 the leading value is 118.01916795759; the actual
  improved upper bound is 120.002637086197. These are
  calculated from the formula instead of copying rough decimals.
- The binomial extension fixes 0 < p < 1. The p = 0,1
  zero-variance cases are separate. The p_N = 1/N example
  prevents an unrestricted moving-parameter interpretation.

## Root integration and notation

Drafting scope P15.24. Body root:
sec:p15-de-moivre-laplace-and-stirling.
Annex root: sec:annex-p15-de-moivre-laplace-and-stirling.
Root may now update P15.23's previously separate Stirling-route
boundary and owns all shared imports.

At def:p15-stirling-models: factorials/binomial coefficients,
natural logarithms, asymptotic equivalence; fair signs epsilon_i,
sum S_N and lattice L_N; separate binomial B_N, p,q;
normal phi,Phi and rounding.
At stirling-log-tools: scalar and row parameters, finite limit
ell and logarithmic-series y.
At stirling-tail-premises: b(k;N,p) and integer tail threshold r.
At stirling-with-remainder: factorial remainder r_n.
Annex-local d_n, Delta_n, C, A = exp(C) and the dimensionless
normal-density multiple c are defined in the constant argument.
At stirling-local-rademacher: u, H(u), R_(n,k), scaled x_(n,k),
window A and K_A. At stirling-de-moivre-laplace: L_N,U_N.
At def:p15-stirling-poisson-laws: lambda and the separate
Poisson sum T_n. At def:p15-stirling-rate-functions: gamma(a),
I(a), and zero-log conventions.
At stirling-general-binomial: sigma_N; its proof defines
D(t||p), the interior interval and derivative bound M_p.
At stirling-worked-boundaries: A_n and changing p_N.
No new macro is required. Root integrated the new Feller key.

## Authoring extent and next work

The complete body and annex were read back as one authoring
batch, with direct revisions for explicit index domains,
finite-interval qualifiers and definition order.
No independent reviews, review waits, scanners, tests, builds
or manuscript renders were run. Primary images were read;
the manuscript was read as actual LaTeX.

The requested Durrett Section 3.1 and its necessary Stirling
chain are written. Next are the remaining Section 3.2 exercises
and Section 3.3 characteristic functions, followed by the general
CLT and its refinements.
Feller's broader Chapter VII, beyond the exact constant
premises used here, is not claimed completed merely because
it was read.

The research skill directed primary investigation and this
single note. The PDF skill supplied the source identity and
complete proof-page reading. The frozen PDFs were preserved.
