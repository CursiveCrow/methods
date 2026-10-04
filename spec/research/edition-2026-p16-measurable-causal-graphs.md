# P16 authoring: measurable causal graphs

8 September 2026. Block began 17:14:31 UTC; deadline 17:59:31 UTC.
Owned outputs: the new body and annex `measurable-causal-graphs.tex`, this
note, `handbook/bib/intake-p16-measurable-causal-graphs.bib`, and the two
source directories below. The three manuscript/note paths were initially
absent. The frozen mediation pair and all shared files remain unchanged.
Root owns integration, canonical notation and bibliography merging.

## Verified primary

Steffen L. Lauritzen, **Lectures on Graphical Models**, third edition 2019,
second printing 2020, Department of Mathematical Sciences, University of
Copenhagen, ISBN 978-87-70787-53-6. The actual title, copyright and prefaces
were read. The second-edition preface expressly says the directed Markov
theory was extended to distributions without product densities.

- Author publication page: https://web.math.ku.dk/~lauritzen/publications.html
- Its verified download: https://web.math.ku.dk/~lauritzen/papers/gmnotes.pdf
- Local: `source/references/lauritzen-graphical-lectures-2019/lauritzen-graphical-models-third-edition.pdf`
- **160 pages; 899,245 bytes**.
- SHA-256: **965FC04BF07B2E8B960367D8F916E17D55F4277795DDD4EF71F220EEB43AA56B**.
- PDF creation/modification: 2 February 2021; this conversion date is
  separate from the edition and printing actually stated in the body.
- Citation key: `Lauritzen2019GraphicalLectures2020`.

Actual complete printed-page extents read, with PDF page = printed page + 5:

- **19–22:** Theorem 1.28 and complete jointly measurable quantile proof,
  update-function interpretation, and Theorems 1.29–1.30 on conditional
  coordinates and kernel reduction.
- **41–52:** conditional events and sigma-algebras; Theorems 2.9–2.10 and
  proofs; kernel combination and Propositions 2.15–2.17 with proofs;
  Theorem 2.18 and Corollary 2.20; the distinction between universally
  valid semigraphoid operations and stronger intersection/composition claims.
- **64–69:** the complete directed Markov section, Theorem 2.44 and proof,
  order independence 2.45–2.46, ancestral reduction 2.48, full recursive
  kernel equivalence 2.49, structural realization 2.50, and the distinct
  dominated-density special case 2.51–2.53. The start of Markov equivalence
  on p. 69 was read for context.
- Definition 1.1, the kernel definition, was also read in the author's
  web-extracted PDF opening. No whole-book reading claim is made.

Source-only images of PDF pp. 69–73 were generated; pp. 70–72 were read
visually to verify the exact central statements, graph notation and the
kernel/density distinction. Scratch images are in the old task's
`tmp/pdfs/p16-measurable-graphs-source/` directory.

An additional historical capture was obtained during source selection:
`source/references/dawid-conditional-independence-1979/dawid-1979-with-discussion.pdf`,
from https://people.csail.mit.edu/tdanford/discovering-causal-graphs-papers/dawid-79.pdf
It has **32 PDF pages, 4,863,971 bytes**, SHA-256
**0555A977497068AEDD643D8AB2ED4DF6600960371B380635C8E23ACDDF77B05A**.
The JSTOR cover and first article page verify A. P. Dawid, *Conditional
Independence in Statistical Theory*, JRSS B 41(1) (1979), listed extent
1–31. It is scanned, with no usable extracted text. Only those two identity
pages were read; it is retained for later reading and supplies no proof
premise or bibliography citation in this component.

The Lauritzen–Dawid–Larsen–Leimer 1990 publication record and Evans's
density-based teaching theorem were located, but unread paper content and
a density theorem were not used as the general-space premise. Acquisitions
were free and confined to the reported source directories.

## Nine complete theorem/proof pairs

Suffixes: `measurable-ci-calculus`, `measurable-kernel-construction`,
`measurable-kernel-randomization`, `measurable-global-markov`,
`measurable-interventions`, `measurable-response-component`,
`measurable-mediation-fields`, `measurable-mediation-corollary`, and
`measurable-graph-examples`. Body prefix `thm:p16-`; annex prefix `annex:p16.`.

The source's kernel route is retained: conditional-expectation calculus,
product-kernel combination and Fubini, legal adjacent topological swaps,
ancestral marginals, and ordered/local/global/recursive-kernel equivalence.
The global proof fills the ancestral moral separator into a complete
partition. Its terminal-vertex induction handles either response side and
the conditioning set; the last case explicitly uses contraction then weak
union. No intersection property, positivity or density is assumed.

The randomization proof retains the source's upper-quantile choice, proves
joint sublevel-set measurability, and transports through a Borel real coding.
A measurable default outside the Borel image gives a total map and preserves
every parameter's kernel. No unique cross-world coupling is inferred.
Intervention solutions are jointly measurable and their laws are actual
probability kernels even outside observational support.

The response-component lemma constructs one jointly measurable function for
all parameter values using the actual private-root tuple on the response
side of a moral separator. General global Markov gives one conditional
product measure for that entire tuple and the other side. This is stronger
than separate fixed-response statements and closes the diagonal problem.

The source mediation graph conditions yield three different fields: R_0 for
the natural cross-world step, R_1 for exposure adjustment, and R_2 for
mediator adjustment. Mediator ancestral edges are restored without connecting
the response and mediator sides, so mediator sets with internal paths retain
their full natural joint values. A fresh reference draw from eta_b(C) first
matches the natural target using R_0. Its conditional joint kernel with
(R_1,A) licenses exposure adjustment. The simultaneous identity
Y=F_2(M,T,R_2) supplies one observed response kernel. Absolute continuity
transfers that kernel's single exceptional set to the target integral.

## Direct corrections, examples and exact scope

The manuscript states all needed contractions, excludes a vertex from its
own predecessor/nondescendant set, and fills the moral-component partition.
Source Proposition 2.17's product-kernel construction gives Y independent
of Z given X; its printed final independence transposes these roles. The
new proof uses the correct product identity. The source's sigma-algebra
intersection/completion assertion is not imported into the proof.

A deterministic continuous chain is proved not dominated by any
sigma-finite product coordinate measure, yet all Markov/kernel claims apply.
A continuous-mediator example gives theta=(1/2,2/3,2,7/3), PNDE 3/2,
TNIE 1/3 and TE 11/6. A positive-density counterexample uses independent
uniform A,M and Bernoulli(1/4) E: Y=E XOR 1{A=1/2} versus Y=E. Observations
coincide, but natural direct effects from 1/4 to 1/2 are 1/2 and 0.
Therefore a point-density assertion cannot identify an isolated null
exposure value. Structural interventions still exist; observational
identification there requires additional regularity or experimental kernels.

The previously missing general-space graphical premise is discharged for
the finite DAG / standard-Borel / independent-disturbance model and the
source's intermediate-vertex mediation graph scope. The observational
corollary has explicit conditional exposure atoms and exact mediator
measure domination. Its proof does not require product densities or an
unproved uniform cross-world assumption. Arbitrary nonstandard targets,
infinite graphs, cyclic equations, and other graph variants with
nonintermediate mediator coordinates remain outside this statement.

## Dependencies and notation handoff

Read the actual regular-conditional-law interfaces through kernel joint
measure, the conditional tower/pullout statements, and the frozen mediation
four-set and full-parent proof interfaces. The earlier graph-theoretic
ancestral-moral bridge has no value-space cardinality premise. Root owns
the canonical merges and later consolidated reviews/admission.

Local roles: K_v,P_K and the topological kernel product; S_v; pr(v),nd(v);
kernel randomizer F and upper quantile q; intervention parameter t; response
component D and private-root tuple R; R_0,R_1,R_2 and F_0,F_1,F_2; C,
S=(C,W_1),T=(A,C,W_1,W_2); gamma_1,gamma_3,gamma_2^a; rho_a,Q_a^obs;
eta_b; domination MS; independent draw G^b; and target measure alpha.
Repeated covariate coordinates are removed without changing any source
conditioning set.

The actual body and all nine reordered full annex proofs were read as the
author's complete batch, with notation/domain corrections applied. No
independent reviews, scanners, tests, manuscript builds, manuscript renders
or acceptance checks were run. No proof remains missing within the stated
standard-Borel graph theorem and its exact observational support domain.
