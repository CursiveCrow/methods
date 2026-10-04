# P15.18: direct weak laws, triangular arrays and the exact tail criterion

Root integration: the unchanged staged Feller scan is now held at
source/references/feller-probability-volume2-second-edition/feller-volume2-second-edition.pdf.
Its imported SHA-256 matches the staged original:
CB87C933D4175234F5F5958A74F3A466ECF13C29BE4E0DFEDF9C9B739F717486.
The canonical bibliography key is Feller1971ProbabilityII. The edition
year and unspecified physical printing date retain the distinctions below.
Both weak-law files are connected before the P15.19 conditional-limit unit.

Written 8 September 2026 in the assigned 45-minute author block.
The complete body and proof annex are saved. Only these three assigned
manuscript/intake files were edited; all paths were unused at dispatch.
Root retains shared routes, bibliography, source import and symbol ownership.
The downloaded source scan is staged in the task scratch directory for
root to import unchanged into the manuscript's source collection.

| File | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| handbook/parts/p15/weak-laws-and-triangular-arrays.tex | 339 | 15221 | 0A066DDDEF4D6C4BB012C2412C462CBFF55162952B2E3A3A1DD0C0F04ADF4E3D |
| handbook/annex/p15/weak-laws-and-triangular-arrays.tex | 576 | 25276 | 41B932BBE4E485376FB6F430B25B87BEF693E8EC3E2DD0E1974FB569A1D50FB2 |

## Complete primary reading and mathematical scope

Durrett, Probability: Theory and Examples, author Version 5 dated
11 January 2019, held at
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf,
SHA-256 AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886.
Reuse DurrettPTEAuthor2019.

Complete printed pp. 56--64, physical pp. 64--72, were personally read
as text and source page images. This includes the definitions, direct
variance results 2.2.1--2.2.3 and 2.2.6, all direct applications
2.2.4--2.2.10, triangular-array Theorem 2.2.11, the whole continued
Theorem 2.2.12 and its remarks, prerequisite 2.2.13, and the immediate
integrable corollary 2.2.14. Geometric Example 1.6.14 on printed p. 35,
physical p. 43, was also read in full as text and image.
Source images are in the task workspace's tmp/pdfs/p15-weak-law-source/.

All direct variance, polynomial, cube, coupon, permutation, occupancy
and truncation proof routes are retained. The first result revisits
the already written variance/L2 foundations in the context of this
complete source presentation; it does not create another original
requirement identity. No weak-law proof is replaced by a strong law.

The exact weak-law criterion now has a complete independent necessity
proof. A finite product constructs unbounded independent copies. Their
differences are independent, identically distributed and symmetric.
A full first-crossing proof of Levy's maximal inequality turns
concentration of the symmetrized sums into n times their n-scale tail
probabilities tending to zero. Independence of the two copies transfers
this to the original tail. A final deterministic-center argument proves
that every admissible center differs from the truncated mean by o(1).
The original and copied probability measures are explicitly distinguished.

## Acquired Feller second-edition source

The title page of the downloaded scan explicitly says Volume II and
SECOND EDITION, with John Wiley & Sons and Mei Ya Publications, Taipei,
imprints. Its introduction is dated January 1970 and Clara Feller's
note is dated May 1970. The second edition's bibliographic year is
1971, verified against the authoritative
[Wiley edition record](https://www.wiley-vch.de/de/fachgebiete/mathematik-und-statistik/an-introduction-to-probability-theory-and-its-applications-volume-2-978-0-471-25709-7),
which identifies the second edition as January 1971, ISBN
978-0-471-25709-7. This identifies the required edition, not an exact
physical printing year of the Mei Ya copy.

The public [Zenodo record](https://zenodo.org/records/7108309) labels its
English Volume II file as 1970 and supplies an MD5 checksum. The exact
[download payload](https://zenodo.org/records/7108309/files/%28Wiley%20series%20in%20probability%20and%20statistics%29An%20introduction%20to%20probability%20theory%20and%20its%20applications.%20Vol2%20%282nd%20edtion%29-William%20Feller%281970%29.pdf?download=1)
was obtained with ordinary Python TLS after the web fetch and Windows
TLS clients failed. No certificate verification was disabled.

Staged original file:
C:/Users/Crow/Documents/Codex/2026-08-10/phase-4-handover-migration-campaign-written/tmp/pdfs/p15-weak-law-source/feller-vol2-candidate.pdf

Size: 44,136,265 bytes; PDF pages: 683.
SHA-256: CB87C933D4175234F5F5958A74F3A466ECF13C29BE4E0DFEDF9C9B739F717486.
MD5: b364d1c1aed6b145c3167f16918a02d8, matching the public record.
The file was not edited or re-exported.

The title page and complete printed pp. 234--236, physical pp. 249--251,
were read as text and images. These pages contain the exact generalized
weak-law argument referred to by Durrett, including its necessity proof.
The scan has no copyright/date leaf between its title and first-edition
preface, and its title has library markings, including a handwritten
1971. The physical printing year remains unspecified; that annotation
was not used as a publisher date. Whole-book page completeness is not
claimed from this bounded reading.

The distinct Feller reconstruction remains next writing, as directed by
root. Its median-based chain invokes Chapter V inequalities (5.6), (5.10)
and (5.7); those complete prerequisite presentations were not read or
reconstructed in this block. The footnote also points to XVII,2a for a
different proof. The current manuscript therefore keeps the separate
historical presentation boundary while establishing the mathematical
criterion fully by an independent proof now.

## Eleven complete statement/proof pairs

Each suffix has body label thm:p15-<suffix> and reciprocal annex label
annex:p15.<suffix>.

| Suffix | Completed content |
| --- | --- |
| direct-variance-weak-laws | Full square expansion, moment-to-probability bound, common-mean L2 law and arbitrary-sequence variance criterion. |
| bernstein-approximation | Compact-interval continuity prerequisites, binomial representation including endpoint probabilities, uniform estimate and exact x-squared example. |
| cube-shell-concentration | Product-volume model, exact moments 1/3 and 1/5, radial conversion and explicit annulus error bound. |
| coupon-collector-law | Finite hitting times and real versions, independent durations from finite histories, geometric differentiation with finite-remainder justification, moments and normalization. |
| permutation-cycle-law | Complete uniform-permutation algorithm, its open-chain invariant, mutual independence of closing indicators, full cycle law and endpoint failure without CLT. |
| occupancy-weak-law | Complete diagonal/off-diagonal covariance formula, logarithmic limits, negative covariance bound and the additional infinite-loading case. |
| triangular-array-weak-law | Both source truncation conditions and the complete union/Chebyshev error bound with row-only independence. |
| levy-symmetric-maximal | Full first-crossing/sign-of-future proof, strict and non-strict thresholds, and increment-maximal consequence without moments. |
| iid-weak-tail-criterion | Direct source sufficiency, complete independent necessity, all deterministic centers and the exact lower-moment range. |
| direct-integrable-weak-law | Source Theorem 2.2.14's two dominated-convergence steps and truncation argument. |
| weak-law-counterexamples | Failure of each sufficient array condition, row dependence, cancellation, an infinite-absolute-mean weak law and a law admitting no deterministic center. |

The coupon example distinguishes its leading asymptotic scale
365 log(365)=2153.462534... from the actual mean
365 H_365=2364.646023.... The source's truncated-second-moment display
on p. 64 is supplied with its correct inequality and the exact
subtracted-tail identity. The lower-moment implication is restricted
to 0<r<1. Geometric p=1, empty occupancy products, initial logarithmic
denominators and null exceptional coupon paths are explicit.

## Root integration, notation and next obligations

Use drafting-unit P15.18. Body anchor:
sec:p15-weak-laws-and-triangular-arrays; annex anchor:
sec:annex-p15-weak-laws-and-triangular-arrays.
The body continues to cite the held Durrett key. Root should import the
unchanged Feller scan and its actual provenance before adding the
separate historical presentation and its bibliography/source routes.

Notation intake: probability and mean-square convergence; row X_(n,k),
S_n, means mu_i,mu_n, scales b_n and variances sigma_n^2; Bernstein f_n,
M_f, omega_f and binomial coefficients; product volume lambda_n, norm,
annulus A_(n,epsilon), squared-coordinate mean M_n and radius R_n;
coupon hitting times tau_k^n, finite durations D_(n,k), T_n and p_(n,k),
geometric G and q; permutation pi, adaptive domain/image labels i_k,j_k,
closing indicators I_(n,k), cycle count K_n, harmonic H_n and variance v_n;
occupancy events A_i, count N_n, ball count r_n, probabilities q_n,s_n;
truncated rows bar X, bar S, center a_n and error terms u_n,w_n;
Levy sums T_k, crossing events A_k,A_k^+,A_k^- and future R_k;
copies hat X, tilde X, hat S, tilde S on product probability Q;
symmetrized Y_i, tail scale eta, original tail W, truncated means mu_n,
arbitrary centers c_n, function g and lower-moment exponent r.
Each reused letter is locally typed in its own statement or proof.

The complete saved LaTeX was read and the local mathematical corrections
reread. As instructed, no scoped scanner, tests, build, manuscript render,
independent review or acceptance checks were run. File hashes and sizes
are inventory metadata, not an acceptance claim.

Next: reconstruct the separately sourced Feller second-edition argument
with its cited Chapter V prerequisites; finish Examples 2.2.15--2.2.16,
especially the St. Petersburg normalization; then continue the distinct
de Moivre--Laplace, weak-convergence, characteristic-function and CLT
presentations. The later CLT cycle-count proof in Example 3.4.11 remains
separate from the fourth-moment endpoint proof supplied here.
