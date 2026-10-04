# P15.19: uniform integrability and forward/backward conditional limits

Written and integrated 8 September 2026. The body and annex contain seventeen
complete statement/proof pairs. Root read both saved LaTeX files completely,
including the continuation of the truncated tool output, and applied the
final domain and definition corrections together. No independent review,
scoped scan, test, build or manuscript render ran.

Body at authoring: handbook/parts/p15/uniform-integrability-and-conditional-limits.tex,
15950 bytes, SHA-256
2AE9B93D4DB648575670B0D80E97A41EAA3B7F0A926C47546A5202C624A8E295.
Annex: handbook/annex/p15/uniform-integrability-and-conditional-limits.tex,
29094 bytes, SHA-256
7E269CF710F0B0902D2B1D766B97D76AF65AB5EBA1D677DD22B9F305DCAFA231.

## Exact source and complete extent

Durrett, Probability: Theory and Examples, author Version 5 dated
11 January 2019, held at
source/references/durrett-probability-2019-01-11/PTE5_011119.pdf.
SHA-256 AEAC36CBF5E44C53D69FA60A2D29A393E2D0E8C955EE103BD845D925FD910886.
The existing bibliography key DurrettPTEAuthor2019 is used.

The complete printed pp. 244–250, physical pp. 252–258, were read directly
from the held source. This covers all of Section 4.6: definition,
Theorems 4.6.1–4, Lemmas 4.6.5–6, Theorems 4.6.7–10, Example 4.6.11,
and Exercises 4.6.1–7. It also covers the backward-martingale definition
and the full Theorems 4.7.1–3. The adjoining Example 4.5.8 and the
exchangeability setup at the end of p. 250 were read as context; they
are not claimed as complete additional presentations.

The source's clipped and continuous-cutoff routes in Theorem 4.6.3
are both retained. So are the closing-variable event identities,
pi-lambda identification, separate conditional proof of the tail
zero-one law, oscillation-envelope conditional dominated convergence,
the full Bernoulli counterexample, every Section 4.6 exercise, and the
finite reversed-string upcrossing proof. The source's negative indices
are translated explicitly to the new nonnegative reverse-time indices.

## The seventeen reciprocal proof suffixes

Body prefix thm:p15-; annex prefix annex:p15.:

ui-small-sets; ui-moment-criteria; ui-conditional-family;
probability-l1-tools; vitali-convergence; submartingale-ui;
closed-martingale; levy-upward; levy-information-law;
changing-conditional-limits; ui-counterexamples; dyadic-martingales;
posterior-mean-consistency; extinction-or-escape; bounded-polarization;
backward-martingale-convergence; levy-backward.

The uniform small-event equivalence, explicit convex superlinear converse,
terminal sub/supermartingale inequality, completed-measure Borel-version
construction and finite-vector limit extension are proved additions.
They are not described as unmodified source statements.

## Direct qualifications and corrections

The source's first sentence of the Theorem 4.6.1 proof invokes dominated
convergence from P(A_n)->0, which does not itself give pointwise convergence
of the indicators. The active proof uses the complete tail-splitting
small-event bound. For the superlinear criterion, the moment function is
explicitly Borel measurable; the convex converse is a locally finite
sum of positive parts with controlled expected tails.

The source's dyadic Lipschitz exercise uses f(1) while initially defining f
only on [0,1). The active statement and proof first construct the unique
continuous extension to 1. Every dyadic atom, average, child identity,
telescoping integral and arbitrary-endpoint limit is supplied. The Borel
sigma-algebra generation and the separate completion extension are proved.

The posterior exercise retains integrable noise and prior and identifies
the parameter from the actual infinite observed averages. The limit is an
information-measurable version; no uncompleted sigma-algebra is assumed
to contain arbitrary modifications on null sets.

The extinction result uses a countable family of integer thresholds and
one common probability-one event. Its branching application defines the
offspring recursion, finite nonnegative integer initial population,
generation information and conditional zero probability. No offspring
mean or initial-population mean is required. The polarization exercise
has a full conditional-mean calculation, a closed two-point limit
argument and a realizable uniform-input construction.

The backward proof explicitly proves monotonicity of maximum upcrossing
counts when a new left observation is added. It excludes infinite limits
by Fatou and constructs the limit measurably in the actual intersection
of the decreasing sigma-algebras.

## Integration and continuation

Both files are connected in the P15 drivers; scope P15.19 is reserved
after the direct weak-law block P15.18. Canonical symbols contain all
new local roles. The preceding martingale boundary links these results.
The body and seventeen proofs are author-complete; independent admission
remains part of the later consolidated process.

These theorems provide the remaining conditional-limit premises for
Blackwell's general comparison-of-experiments construction. The remaining
Durrett work includes the Section 4.3–4.5 applications and maximal/Lp
results, the rest of Section 4.7 and optional sampling, and the distributional
and statistical presentations being developed in their separate units.
