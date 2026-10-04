# P15.26 author return: characteristic functions through 3.3.21

Date: 8 September 2026. This bounded author block supplies seventeen
complete statement/proof pairs through Durrett Theorem 3.3.21.
It does not mark the full Section 3.3 target complete.

Files:

- handbook/parts/p15/characteristic-functions-and-inversion.tex
- handbook/annex/p15/characteristic-functions-and-inversion.tex
- This single source/notation note.

Root retains shared routes, symbols, bibliography and older boundary
updates. No other manuscript file was edited.

## Frozen full source target and supplied boundary

The exact held presentation is Durrett, author Version 5 dated
11 January 2019:
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf.
SHA-256:
AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886.
Reuse DurrettPTEAuthor2019; no new source key is needed.

Before authoring, the entire Section 3.3 was read and the full target
was communicated to root: numbered theorems/examples 3.3.1–3.3.26,
the three unnumbered moment-problem counterexamples and the section's
exercise boundaries. The section begins on printed p. 125, rather
than p. 126, and ends on p. 143. These are physical PDF pp. 133–151.
All of that exact text, including every continued proof, was read.
The beginning of Section 3.4 on p. 144 was context only; no CLT
was used as a premise.

The completed boundary for this block is the definitions, theorems,
lemmas, corollaries and examples numbered 3.3.1–3.3.21, printed
pp. 125–136. The remaining 3.3.22–3.3.26 chain is retained below.
The source calls its last two subsections optional reading; that
does not remove them from the manuscript's assigned target.

Complete source images were personally read for the Gaussian
two-route calculation, finite examples, inversion and density proof
on pp. 127–130, and the continuity continuation and all
moment/Taylor proofs on pp. 133–136.
Additional required passages read in full:

- Exercise 1.7.5, printed p. 42, physical p. 50, including its
  actual page image and both stated conclusions.
- Theorem A.5.1 and its complete continued proof and normal
  application, printed pp. 470–471, physical pp. 478–479.
- The actual Fubini exercise 1.7.1 and the differently concerned
  exercise 1.7.4 on printed p. 41, physical p. 49.
- The norm/Jensen referral, Exercise 1.6.2, printed p. 35,
  physical p. 43.
- The complete topological subsequence statement and proof,
  Theorem 2.3.3, printed p. 68, physical p. 76.

The relevant previously written prerequisites are real integration,
Tonelli/Fubini for sigma-finite products, expectation against a law,
finite/countable mixture integration, Gaussian normalization and
first absolute moment, Poisson normalization, and P15.23's
bounded-continuous, Helly, tightness and subsequence results.
The new complex and differentiation premises are proved here.

## Seventeen complete reciprocal proof pairs

Each suffix has body prefix thm:p15- and proof prefix
annex:p15. followed by the identical suffix.

| Suffix | Complete supplied scope |
| --- | --- |
| characteristic-complex-calculus | Complex conventions, modulus/Jensen special case, componentwise convergence/Fubini, exponential series and elementary derivative bounds. |
| characteristic-differentiation | Full Appendix A.5.1 integral-average proof, including joint measurability and reduction of an arbitrary measure to a sigma-finite derivative support. |
| characteristic-algebra | Theorems 3.3.1–3.3.2 and Lemma 3.3.9; source finite mixtures plus proved countable extension; real-part and squared-modulus transforms. |
| characteristic-elementary-examples | Examples 3.3.3–3.3.4, 3.3.6–3.3.8 and 3.3.10, retaining their direct, convolution and mixture proofs. |
| characteristic-normal-transform | Example 3.3.5, both differentiated and completed-square routes; all parameter bounds for the complex shift and the degenerate normal case. |
| characteristic-dirichlet-integral | Exact corrected strip identity, both error estimates, uniform bound, sign-scaled kernels and failure of absolute convergence. |
| characteristic-inversion-uniqueness | Theorem 3.3.11: finite-kernel Fubini, oscillatory limit, half-atoms and full uniqueness argument. |
| characteristic-inversion-corollaries | Corollaries 3.3.12–3.3.13 through the characteristic-function route. |
| characteristic-integrable-inversion | Theorem 3.3.14 with reality, nonnegativity, no atoms, continuity, normalization and equality of Borel measures. |
| characteristic-inverse-examples | Examples 3.3.15–3.3.16 through the source dual inversions; separate characteristic-function proof of Cauchy averages. |
| characteristic-atom-inversion | Source Exercises 3.3.2–3.3.3, shifted-lattice phase, averaged atoms and squared-atom sum. |
| characteristic-continuity-theorem | Theorem 3.3.17, exact real nonnegative tightness integral, existence/uniqueness and the source bounded-test subsequence route. |
| characteristic-moment-derivatives | Theorem 3.3.18, every order's integrability, derivative interchange and continuity. |
| characteristic-taylor-remainder | Lemma 3.3.19, exact oriented remainder, both bounds, n = 0 and negative arguments. |
| characteristic-moment-expansion | Full n-th order expansion and source (3.3.3), Theorem 3.3.20 without a third moment. |
| characteristic-second-moment | Theorem 3.3.21, complete Fatou/limsup argument, reverse implication and Exercise 3.3.16's zero-law consequence. |
| characteristic-boundaries | Loss of continuity at zero, density without integrable transform, independence failure and impossibility of exp(-abs(t)^alpha) for alpha > 2. |

Additional exercises actually supplied are 3.3.1, 3.3.2, 3.3.3,
3.3.4, 3.3.6 and 3.3.16. Other exercises retain their separate
obligations; the Cantor counterexample mentioned after 3.3.3
is not claimed written by its squared-atom identity.

## Corrections and qualifications applied directly

1. Exercise 1.7.5's stated strip is 0 < x < A, 0 < y < infinity.
   Performing the two integrals gives pi/2 as the leading term,
   not the printed arctan(A). The manuscript contains the correct
   exact identity. The source's original error bound centered at
   arctan(A) is nevertheless true and is separately proved:
   the complex combination of the two correction integrals has
   modulus at most 1/A, while pi/2 minus arctan(A) is at most 1/A.
2. The source's complex-mean Gaussian explanation is replaced
   directly by a valid shifted-integral proof. Parameter
   differentiation is dominated on every bounded parameter
   interval; its derivative becomes an integrable x-derivative
   with vanishing boundary terms. The source's separate real
   differentiation/integration-by-parts proof is retained.
3. Appendix A.5.1 cites Exercise 1.7.4 as Fubini, but that
   exercise is a CDF-shift identity in this version. The actual
   interchange is proved from the manuscript's Fubini theorem.
   No sigma-finiteness is silently added to A.5.1's domain:
   E = {s: integral_I abs(g(t,s)) dt > 0} is proved
   sigma-finite, and the derivative vanishes identically off E.
4. Finite inversion uses only the original bounded difference
   kernel for Fubini. The separate sine integrals are evaluated
   at each fixed x; no hidden first or logarithmic moment is
   required. The infinite inversion is a symmetric improper
   limit, with both endpoint half-masses retained.
5. The continuity theorem's symmetric integral is proved real
   and nonnegative before inequalities are applied. Its
   candidate limit is measurable, has value one at zero, and
   produces a probability law only after tightness and selection.
6. The source typo referring to Lemma 3.3.2 in the Taylor
   estimate is resolved to the actual remainder lemma 3.3.19.
   Both its factorial and denominator-free bounds are supplied.
7. The n = 0 remainder and oriented negative-argument cases
   are explicit. The second-moment converse chooses a
   decreasing positive sequence attaining the relevant liminf
   before applying Fatou. Its quotient is explicitly real.
8. Density inversion proves all density properties. Lattice
   inversion is restricted to the stated lattice, and an
   affine lattice has a phase factor rather than necessarily
   ordinary periodicity.

## Exact next required chain

- Theorem 3.3.22, pp. 137–138: convex right-derivative
  representation, Stieltjes measure, weighted measure,
  both integrated tail identities, normalization, and the
  source finite-support approximation/continuity proof.
- Examples 3.3.23–3.3.24, pp. 138–139: generalized binomial
  series and coefficient normalization; stable-function
  construction for 0 < alpha < 2; periodic Fourier
  coefficients and their normalized discrete law.
- Moment-problem presentation pp. 140–143: transfer of all
  moments under selected weak limits; compact-support
  determinacy; lognormal perturbation and discrete families;
  the complex-gamma counterexample; Theorems 3.3.25–3.3.26
  with the r = 0 case and analytic propagation; the
  nonnegative/symmetric correspondence and Counterexample 3.
- The outstanding section exercises, especially their
  independently required constructions and converse claims.

The already read source has a sign problem in Exercise
3.3.14(iii): a constant X = 1 gives the derivative i, not
the printed -i. That separate Pitman/weak-law proof remains
owed and must incorporate the direct correction when authored.
No false version of it was inserted in this chapter.

## Root integration and local notation

Drafting scope P15.26. Body root:
sec:p15-characteristic-functions-and-inversion.
Annex root: sec:annex-p15-characteristic-functions-and-inversion.
Root owns updates to the older Cauchy and weak-convergence
source-route boundaries now supplied here.

First definitions: def:p15-characteristic-complex-conventions
introduces complex components, conjugation, modulus, exponentials
and integrals; characteristic-function introduces varphi_X and
its probability law mu, keeping normal density phi distinct.
The derivative theorem locally defines I,f,g,u,v and its proof
defines q(s),E. Algebra locally defines mixture weights lambda_j.
The kernel definition introduces sinc, S(A), R(theta,T),
K_(a,b), T and the sign function. Inverse examples define f_P.
Atom inversion uses b+hZ and its phase. The continuity theorem
uses mu_n,varphi_n,u and its real averaging integral.
Moment results introduce derivative order n, remainder order,
the symmetric quotient Q(h), and the one-sided finite limit c.
All scopes are local; no new macro or bibliography key is needed.

## Author return

The entire written body and annex were read back once as
actual LaTeX, with direct revisions to the source identities,
parameter domains and definition order.
No independent reviews, review waits, scanners, tests, builds
or manuscript renders were run.
The research skill directed primary reading and this single
repo note; the PDF skill was used for the exact source equations
and continued proof pages. The full Section 3.3 target remains
open at the explicit theorem boundary above.
