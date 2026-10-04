# P15.17: strong-law rates and infinite-mean normalization

Written 8 September 2026 in the assigned 45-minute author block.
The first tool clock checkpoint was 12:45 UTC; the full body and annex
were saved before 13:00 UTC and read back with corrections afterward.
Only the three assigned new files were authored. All paths were unused
at dispatch. Root retains shared integration ownership and the preceding
martingale chapter's P15.16 reservation. Independent reviews remain
deferred under the current writing-first instruction.

| File | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| handbook/parts/p15/strong-law-rates-and-normalization.tex | 309 | 13200 | 3F4F7E859BA93ADADD8BEF6DB70B61CC0218EC2BA554A4D9DF5814FE82A2AEAA |
| handbook/annex/p15/strong-law-rates-and-normalization.tex | 590 | 24306 | F2EF8340F21C53F1D513BE1F27CAEB4C72B79242F2C9697473B903FD8F181E50 |

## Exact source and complete read extent

Durrett, Probability: Theory and Examples, author Version 5 dated
11 January 2019, held at
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf.
Verified SHA-256:
AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886.
Reuse DurrettPTEAuthor2019; no new bibliography key is needed.

The selected scope was fixed before writing as the complete statements
and proofs of Theorems 2.5.11--2.5.13, the source's later LIL comparison,
the full moment converse in Exercise 2.5.2, and the power-moment
prerequisite Lemma 2.2.13. Printed pages 87--90 and 63--64,
physical pages 95--98 and 71--72, were personally read as text and
primary-source page images. Images are under the task workspace's
tmp/pdfs/p15-rates-source/ directory. Additional theorem headings in
Sections 2.2 and 3.1--3.4 were located to identify the next obligations;
those sections were not treated as fully read or authored.

The source's MZ theorem has 1<p<2 and mean zero. Its full power-interval
decomposition, nonnegative sum/integral interchange, scaled-variance
summability and separate mean-tail estimate are retained. The finite-variance
proof retains its variance series and Kronecker argument. Feller retains
both scaled-tail and finite-tail arguments, including the exact interval
count identity, variance sum, proof that a_n/n diverges in the finite-tail
case, and the final truncated-mean calculation.

## Direct source-algebra corrections and parameter scope

The active MZ mean estimate has coefficient one:
|mu_m| <= m^(1/p-1) E[|X|^p; |X|>m^(1/p)].
The final p^(-1) factor printed in the source's p. 88 chain does not
follow from the preceding scaling step. The new annex gives the complete
correct chain; the extra factor is not copied into the active manuscript.
The first power interval and the singular endpoint y=0 of the general
tail-integral formula are treated explicitly. The quantified variance
constant 4/[p(2-p)] is an added bound, not claimed to be a printed source
constant.

In the source's p. 89 truncated-mean display, the first triangle bound
contains an extra factor n before a sum of n expectations. The active
proof uses the correct successive bounds
|sum E Y_m|/a_n <= (sum E[W;W<a_m])/a_n
<= (n/a_n)E[W;W<a_n],
then retains the source's fixed-head/interval-tail argument.
The measure in those nonnegative interval integrals is explicitly the
law of W=|X_1|, so it cannot be confused with a signed input distribution.

MZ now has complete separate cases: 0<p<1, p=1, and 1<p<2.
The subunit proof even needs only a common law, not independence, and
establishes absolute weighted-series convergence before Kronecker.
The moment converse holds for every p>0, with arbitrary finite center;
for p>=1 the center must equal the mean. The iid classification below
two is therefore an equivalence. The p=2 and p>2 failures use the
existing fourth-moment lower bound and tail zero-one law, without CLT.
The source's LIL comparison is explicitly recorded as a separate later
proof obligation; no optimal logarithmic-factor claim is made here.

Feller uses positive denominators with a_n/n nondecreasing, inclusive
removed events |X_n|>=a_n and strict retained events |X_n|<a_n.
Its interval identity includes the initial one from the threshold a_0=0.
The hypotheses imply that a_n itself is strictly increasing. The staircase
counterexample preserves positive nondecreasing denominators but drops
ratio monotonicity, and proves failure of the finite-tail conclusion.

## Ten complete statement/proof pairs

Each suffix has body label thm:p15-<suffix> and reciprocal annex label
annex:p15.<suffix>.

| Suffix | Completed content |
| --- | --- |
| power-tail-tools | General positive power-moment identity, both integer-tail bounds, decreasing series/integral comparisons and constant-shift moment equivalence. |
| finite-variance-log-rate | Full source logarithmic variance series, denominator domain, zero variance and centered nonzero means. |
| mz-source-rate | Full source 1<p<2 proof with every truncation, variance and mean step and an explicit constant. |
| mz-subunit-rate | The 0<p<1 absolute weighted-summability and normalized absolute-sum proof without independence. |
| power-rate-necessity | Correct normalized-increment identity, independent Borel--Cantelli, moment necessity and necessary centering. |
| mz-full-classification | All cases below two, including p=1, both directions and arbitrary centers where permitted. |
| feller-infinite-mean | Both full source branches, count identity, scale comparison, variance summability, ratio divergence and complete mean drift. |
| rate-calculated-examples | Fair signs, an infinite-mean finite-half-moment law, a centered Pareto-type 3/2-rate example and both Feller branches. |
| rate-hypothesis-boundaries | Order-two and higher failure without CLT, missing center, critical moments, finite-mean Feller failure and dependence failure. |
| feller-ratio-counterexample | Fully defined deterministic staircase, existence of its indices, summable single-term tails and divergent normalized partial sums. |

## Integration and current dependencies

Use planned scope P15.17. Body anchor:
sec:p15-strong-law-rates-and-normalization. Annex anchor:
sec:annex-p15-strong-law-rates-and-normalization.

The live prerequisite identities were checked:

| Predecessor | Body SHA-256 | Annex SHA-256 |
| --- | --- | --- |
| independent-random-series | 9E0C548249191087AB7F68F10868745C6C77AD0CD63ECBEBF6FA1C1D0780D107 | 831ED99DBD3929DEDDB5371311E3708686FC0F3F03C2E702FECD36480D27D509 |
| strong-laws-of-large-numbers | FF74422B72E9610D2153CC6319AE99D0F9285A09F3D6F159A30782CCD1AA6DDB | ACF700405F83D58521E4F18F7E51A7227BAC6D92ACB00C027CD6C8857BCB10DB |
| strong-law-applications | 98281F5718F019C1BBC8AE22688347F22E93762B9A3AA2E4DCBFD2EA04947C51 | FF5646A3BC68634EF199E806B080852C23BD55035F4C5441252DA294E4C8391B |

Notation intake: S_n,S_0 and centered S_n^(c); positive a_n and a_0;
nonnegative W, power p, summation exponent q, level y, cutoff Y_m,
truncated sum T_n, truncated mean mu_m, intervals I_j, tail moment d_m;
sigma>=0 and sigma^2, logarithmic tolerance epsilon; centered V_n,
partial sums Delta_n; Feller ratio b_n, tail probabilities q_n and sum Q,
absolute-value law nu, intervals A_m, fixed tail index N and bound B;
the fair-sign convergence event C, logarithmic exponent beta and d;
example scalar u=2^(1/4), density f; staircase indices N_k,N_0 and heights
A_k. All roles are locally declared. A_m denotes intervals in the Feller
proof and A_k denotes positive heights in the separate staircase proof.

The actual saved body and annex were read completely and the changed
qualifications reread. The existing scoped scanner reports ten reciprocal
pairs, no findings, no missing references and no duplicated new labels.
No independent review, manuscript build/render, new test or acceptance
report was run.

## Exact next weak-law and distributional obligations

Complete the remaining Section 2.2 presentations and applications,
printed pp. 58--66, especially triangular-array Theorem 2.2.11,
tail-truncation Theorem 2.2.12, integrable weak law 2.2.14 and the
St. Petersburg calculation 2.2.16. The general power-moment lemma 2.2.13
is supplied here. The necessity remark attached to 2.2.12 cites Feller,
Vol. II (1971), pp. 234--236; its exact source extent and proof remain
part of that full future presentation. The weak-law proof must retain
the inequality bounding the truncated second moment by the tail integral,
and its lower-moment implication uses the positive range 0<1-epsilon<1.

Then supply the separate de Moivre--Laplace route in Section 3.1,
pp. 113--115; complete weak convergence in Section 3.2, pp. 116--125,
including coupling, bounded-continuous tests, continuous mapping,
portmanteau, Helly/tightness and subsequence criteria; and the required
characteristic-function presentation in Section 3.3, pp. 126--143.
The continuity theorem is 3.3.17 and the relevant Taylor/moment results
include 3.3.19--3.3.20.

The full iid CLT is Theorem 3.4.1 with its continued proof, pp. 144--145.
Lindeberg--Feller is Theorem 3.4.10, pp. 148--149, with its stated
triangular-array hypotheses and the surrounding applications retained.
Its completion must discharge the separately recorded LF premise of
the random-series chapter's preserved source necessity route. These
distributional proofs and their examples are not replaced by the
almost-sure results just written.
