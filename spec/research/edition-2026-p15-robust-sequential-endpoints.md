# P15-U6: robust sequential endpoint closure

9 September 2026. First clock reading: 03:24:46 UTC.
Owned new files: handbook/parts/p15/robust-sequential-endpoints.tex,
handbook/annex/p15/robust-sequential-endpoints.tex, this note, and
handbook/registry/symbols-intake-p15-robust-sequential-endpoints.csv.
Root owns earlier files and shared integration.

## Source and actual reading

Peter J. Huber (1965), A Robust Version of the Probability Ratio Test,
The Annals of Mathematical Statistics 36(6), pp.1753--1758.
DOI 10.1214/aoms/1177699803. Key Huber1965RobustProbabilityRatio.
Held file: source/references/huber-robust-probability-ratio-1965/huber-1965.pdf.
Six journal pages, 578627 bytes.
SHA256: B3E9489F3CD1F7AB9E7F65AC205128DD31A14B1DF44DB620650A1CBD71D17970.

The entire original was read in the preceding author block. This block
reread the actual p.1757 image, including all of its expected-size
argument and drift qualification, and the actual preceding neighborhood
definitions, constructions, stochastic-order/quantile proofs and full
sequential error and bounded-score expected-size proofs.
The primary image is tmp/pdfs/p15-huber-robust-source/source-5.png.
Research/PDF skills guided reading. A source-extent research agent could
not start because the agent thread limit was reached.
No new primary acquisition or bibliography intake was needed.

## Complete result and quantifiers

The original arbitrary contamination and equal-radius variation classes
are unchanged, including singular H, zero radii, zero/infinite clipping
endpoints, arbitrary measurable spaces, and the source variation norm
equal to twice sup-event distance. Previously proved ordered composite
extensions also qualify. Each expectation uses one fixed law R and
independent observations; the supremum covers the whole neighborhood.

The full source conclusion is proved:
sup_R E_R N / E_Q N -> 1 whenever the corresponding actual
least-favorable wrong-exit probability tends to zero.
Hence both ratios hold when both errors vanish. Boundary divergence
is sufficient, not a replacement for the original premise.
This includes finite entropy, infinite entropy with finite scores,
and positive singular-score mass. No bounded-score, variance or
second-moment premise is inserted.

## Exact reciprocal map

Chapter: sec:p15-robust-sequential-endpoints.
Annex: sec:annex-p15-robust-sequential-endpoints.

| Body result | Full proof |
| --- | --- |
| thm:p15-directional-log-integrability | annex:p15.directional.log.integrability |
| thm:p15-one-sided-truncation | annex:p15.one.sided.truncation |
| thm:p15-hitting-restart | annex:p15.hitting.restart |
| thm:p15-two-boundary-passage-comparison | annex:p15.two.boundary.passage.comparison |
| thm:p15-robust-endpoint-closure | annex:p15.robust.endpoint.closure |
| thm:p15-stopped-binary-information | annex:p15.stopped.binary.information |
| thm:p15-sequential-leading-minimax | annex:p15.sequential.leading.minimax |
| thm:p15-infinite-entropy-finite-scores | annex:p15.infinite.entropy.finite.scores |
| thm:p15-singular-contamination-stopping | annex:p15.singular.contamination.stopping |

## Proof route and direct source corrections

The log likelihood's negative part is integrable with expectation at
most 1/e, and E exp(-Z)<=1 follows by density integration.
Upper truncation at finite M with positive d_M=E min(Z,M), finite
stopped summation and S_(tau wedge n)<=t+M prove
E tau_t<=(t+M)/d_M. Finite entropy then gives the untruncated Wald
identity through absolute expected summability.

The restart identity and subadditivity are proved by finite-history
product integration, with jointly measurable random hitting targets.
The stopped nonnegative exponential bounds the wrong-exit overshoot.
The relative error is at most exp(-u){1+(u+M)/d_M}, uniformly in t.
In terms of actual wrong-exit probability p, it is at most
p{1+2(log(1/p)+M)/d_M} for 0<p<=exp(-1), and zero for p=0.
This stronger form retains the exact source vanishing-error premise.
Coordinatewise coupling and membership of Q then squeeze the complete
neighborhood supremum.

Finite entropy gives the scale t/D. Infinite entropy gives a zero
normalized limit, not an equivalence to t/infinity. A positive
infinite-score atom of mass s gives the finite unnormalized limit 1/s.
Without such an atom the expectation diverges, possibly sublinearly.
The countable full-support example explicitly has infinite forward
entropy, finite reverse entropy and finite scores everywhere.

The nonzero-contamination example has two allowed alternative laws
with infinite score means but expected-size limits 5/2 and 2.
Thus the source's equal-mean coupling step requires finite means.
It also has zero null error at every upper boundary and alternative
error (3/5)^r, disproving the source's implication that vanishing
errors always requires both boundaries to diverge. The proof here
retains the full conclusion using actual errors instead.

Stopped entropy and binary decision information are derived on the
disjoint union of finite stopped histories, allowing a common independent
random seed. Finite entropy gives sharp leading logarithmic minimax cost.
Positive singular mass gives limiting minimax cost 1/s using a
finite-history absolute-continuity lower bound. Infinite entropy without
a singular atom yields divergent but sublinear minimax and robust-test
costs; a ratio-optimality claim between those two sublinear quantities
is not inferred from their zero linear-scale limits. This stronger
cross-procedure comparison is distinct from the fully closed Huber
least-favorable expected-size ratio.

## Exact integration change for root

Preserve the earlier bounded-score theorem and its proof. Replace only
the final boundary paragraph in handbook/parts/p15/robust-hypothesis-testing.tex:

> The expected-size asymptotic uses bounded clipping. Zero-radius cases
> with unbounded log ratios have the proved finite termination and error
> comparison, but need separate moment and overshoot arguments for
> that expected-size asymptotic.

Suggested replacement:

The unbounded and singular endpoints are completed in
\cref{thm:p15-robust-endpoint-closure}. That result proves the full
least-favorable expected-size ratio under vanishing errors, with
separate finite-entropy, infinite-entropy and singular-mass limits.
The corresponding leading minimax cost distinctions are in
\cref{thm:p15-sequential-leading-minimax}.

The preceding source note's remaining endpoint obligation should also
point to this completed pair. Earlier/shared files were not edited here.

## Handoff

The complete body, annex, source note and notation intake received
the whole author read-through. Final corrections specified the growth
premise for size classifications, clarified the random-target monotone
limit, and defined finite-history likelihoods piecewise on their support.
No independent review, scanner, test, build or manuscript render is run.
No Huber 1965 expected-size endpoint obligation remains.
Exact finite-boundary expected-cost optimality, shared contamination,
multi-decision procedures and robust estimation remain separate work.
