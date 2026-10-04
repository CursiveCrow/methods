# P15-U1: event limits, Borel–Cantelli and zero-one laws

Written 8 September 2026 in the author block beginning 10:38 UTC,
deadline 11:23 UTC. The assigned writing is complete and returned for
integration. All independent reviews remain deferred under the user's
current instruction. No review task or review wait was created.

| File | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `handbook/parts/p15/limsup-events-and-zero-one-laws.tex` | 319 | 15805 | `490D8490C5EF661BEA1F2B6BE7CABAC3B5D6E30A4E5E154EF3FB5534B813F9B2` |
| `handbook/annex/p15/limsup-events-and-zero-one-laws.tex` | 535 | 25050 | `040449200D02CE95D195973B024E34935EA4552176476A6B29AA6796F4297CBE` |

The output paths were unused before writing. Only the assigned new LaTeX
files and this note were authored. The complete saved body and annex were
read, and the changed shrinking-interval and index qualifications checked.

## Source and full completed extent

Durrett, *Probability: Theory and Examples*, author Version 5 dated
11 January 2019, held at
`source/references/durrett-probability-2019-01-11/PTE5_011119.pdf`.
Verified SHA-256:
`AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886`.
Reuse `DurrettPTEAuthor2019`; no bibliography addition is needed.

Before authoring, the selected scope was frozen as the event-limit
definitions and Exercise 2.3.1, Theorems 2.3.1 and 2.3.7, the shrinking
interval Example 2.3.6, and the entire pairwise-independent counting
Theorem 2.3.9; plus the tail/permutation definitions, Examples 2.5.1--2.5.2,
and the complete Kolmogorov/Hewitt–Savage proofs, Theorems 2.5.3--2.5.4.
Complete printed pages 67--72 and 81--83, physical pages 75--80 and
89--91, were personally read as text and source page images. The images
are in the task workspace's `tmp/pdfs/p15-zero-one-source/`.
The approximation reference, Lemma A.2.1(ii) on printed p. 461 / physical
p. 469, was also read as text. Its needed finite-information consequence
is proved directly here, including a full sequence indexed by the actual
number of observed coordinates.

The source's mutually independent second Borel–Cantelli proof and its
separate pairwise-independent counting refinement are both retained.
The event `limsup S_n > 0` is shown not to be tail on the canonical real
sequence space; no false universal nonmembership claim about every
degenerate process is carried into the body. Likewise the source's
probability-triviality conclusion for both tail and exchangeable fields
is preserved without asserting literal equality of those sigma-algebras.

## Eleven complete statement/proof pairs

Each suffix has body label `thm:p15-<suffix>` and reciprocal annex label
`annex:p15.<suffix>`.

| Suffix | Supplied proof content |
| --- | --- |
| `event-limit-calculus` | Full limsup/liminf membership, complements, indicator identities, probability inequalities, and countably quantified a.s.-convergence criterion. |
| `borel-cantelli-first` | Source total-occurrence expectation proof, finite-integral conclusion, tail-union bound and summable-deviation corollary. |
| `borel-cantelli-second` | Mutual independence of complements, finite exponential product bound, both countable limiting steps, including zero/one event probabilities. |
| `pairwise-event-count-law` | Indicator variance bound, deterministic k-squared subsequence, positive denominators, summable errors at countably many thresholds and full interpolation. |
| `finite-coordinate-approximation` | Approximation class is a sigma-algebra, finite-union truncation, exact-index full sequence via decreasing infimal errors, symmetric-difference bounds and prefix-event representation. |
| `tail-event-structure` | Tail sigma-algebra, infinitely often indicators, finite/infinite series-limit events, normalized limsup conditions, canonical finite-change equivalence and explicit non-tail source example. |
| `kolmogorov-tail-zero-one` | Both source pi-system extensions, past/future independence, independence of the full observation field and tail field, then self-independence. |
| `permutation-structure` | Measurable finite-permutation actions and inverses, exchangeable sigma-algebra, tail inclusion, i.i.d. law invariance and all source partial-sum invariance examples. |
| `hewitt-savage-zero-one` | Finite-coordinate approximation, exact block-swap formula, law/event invariance, independent disjoint blocks, both error limits, and the pullback form on another probability space. |
| `zero-one-measurable-values` | Rational-cut proof that an extended real variable measurable for a probability-trivial field is a.s. constant, including both infinite constants. |
| `zero-one-countermodels` | Rare independent probabilities, full shrinking-interval family, pairwise-independent latent-bit tail countermodel, independent nonidentical Hewitt–Savage failure, and an exchangeable dependent-law failure. |

The pairwise countermodel uses independent fair bits Y,B_j and outputs
`X_(2j-1)=B_j`, `X_(2j)=Y xor B_j`. Every output pair is independent
and has fair marginals, but every sufficiently late pair reveals Y,
so the tail event `Y=1` has probability 1/2. The exact finite four-bit
failure of mutual independence is also exhibited. For the distinction
between the two sigma-algebras, the canonical event that at least one
coordinate is one is permutable but not tail, even under the i.i.d.
fair-bit law where it has probability one.

## Current dependencies, routes and notation

The statements use already written measure continuity, nonnegative
integration, variance/Chebyshev, generated independence, disjoint groups,
measurable products and countable probability constructions. No
Radon–Nikodym or conditional-expectation result is used. Key current
identities, body / annex:

| Predecessor | Body SHA-256 | Annex SHA-256 |
| --- | --- | --- |
| `measurable-probability` | `C249F33E0E0FC88084B05A7D44098DB87B3E4814083B34709D6DBE2B562340D9` | `FBB9E6C733A1F286F7E56FC31B7E76D4412D781E03711ED02D8D4B3AAEF8C8FC` |
| `integration-expectation` | `A29C887386C298112FC4E9820C6A37B3E934112EF32D704A9CC5EE77F5D909D5` | `F5F1AE8A99F95BE08E1C4A448EF1DF865D9B49E6D238A6DECED46BEF82EBC7FE` |
| `independent-random-variables` | `D70EA961C66F2298CCB449E503BEE16BC9AD15BC547003E3BC700C2F737DCCD1` | `016D354887C6A6B65D7EE42DBE53F859F158BBD34BC2A839C1CCE21BAE09A79B` |
| `countable-product-measures` | `E4875962ECA8AA842C61AB7B933F16231BBFF6FB42CECEBCAC4C744ED68C321A` | `2C93B7BB7D3F3C04930DBBB1DB05ABD73B30B2425ED53BF3044E5D38DD827C56` |

Root owns insertion of the body/annex routes after the required probability
foundations and reconciliation with its separately written RN/conditioning
chapters. The return-time driver now has nine chapters ending in
`radon-nikodym`; appending this unit next would make it P15.10. Root
determines the final chapter scope alongside its conditioning chapter.

Notation intake: event `limsup`, `liminf`, `i.o.`, counts `N_n,N_\infty`,
means `p_j,t_n`, deterministic indices `n_k`, subsequence counts `T_k`;
fields `\mathcal H_n,\mathcal H_\infty,\mathcal F'_n,\mathcal T,\mathcal E`;
`A\triangle B`, approximation errors `d_n,\varepsilon_n`, canonical
prefix map `\pi_n`, prefix replacement `r_m`, tail sums `R_n^{(m)}`;
finite permutations `\pi,\pi^{(n)}` and measurable actions `T_\pi`;
prefix value sets `B_n`, swapped events `A_n'`, rational-cut probabilities
`p(q)` and set `U`; binary `\oplus`, latent bit Y, and harmonic scalar
`H_n` (distinct from calligraphic finite-information field `\mathcal H_n`).
The source's tail-prime and exchangeable-field notation is retained.

The existing scanner reports eleven reciprocal pairs and no scoped
findings; the existing bibliography key resolves. All new references were
checked against the actual measure/extension/integration/product/independence/
countable-product files: none is missing and no new label is duplicated
there. No manuscript render, new test, review or acceptance report was made.

## Exact next writing

The next random-series component starts with source Theorem 2.5.5,
Kolmogorov's maximal inequality, then Theorem 2.5.6 (variance-summable
convergence), Theorem 2.5.7 and the full three-series Theorem 2.5.8 with
their continued proof extent. Separately complete source results
2.3.2--2.3.5 and 2.3.8, plus the record-value and longest-run applications
beginning at Example 2.3.10. The present zero-one laws do not substitute
for those convergence and quantitative constructions.
