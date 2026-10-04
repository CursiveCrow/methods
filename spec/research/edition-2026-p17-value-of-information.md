# Edition 2026 P17: finite value of information

Date: 8 September 2026. Author: /root. Scope: P17.7.

The chapter and full annex are written and connected to the P17 drivers.
The bibliography and canonical notation registry include the new source and
local notation. This is an authoring record; consolidated reviews follow
completion of the manuscript's full writing and integration phase under the
user's current instruction.

## Source acquired and read

David Blackwell, *Equivalent Comparisons of Experiments*, The Annals of
Mathematical Statistics 24(2), June 1953, 265–272.
DOI: 10.1214/aoms/1177729032.
[Publisher PDF](https://projecteuclid.org/download/pdf_1/euclid.aoms/1177729032).

The ordinary publisher download returned HTTP 200 and application/pdf.
Local source: source/references/blackwell-equivalent-experiments-1953/blackwell-1953-equivalent-comparisons.pdf.
SHA-256: F490B8395187EDC34AB46A3D45455F1F59CBBC9632964C63218A2F4C8BA8CD1D.
Size: 794,785 bytes. Eight pages, printed 265–272. The 2006 embedded creation
date describes digitization; the publication date is 1953. The PDF is
unencrypted. Its text extraction contains footer material, so the author
read every complete scanned source page, retained at
tmp/pdfs/blackwell-1953-source/page-1.png through page-8.png.
Research and PDF skill instructions guided this source reading.

The exact finite matrix definitions and Theorems 1–7 were read before
writing. The remaining pages were read to identify the source's general
observation-space, restricted-decision and binary testing constructions.
Blackwell's distinct 1951 paper was not acquired and is not counted as read.
The source attributes the converse comparison theorem to Sherman and Stein;
the chapter preserves that attribution.

The reader text is an independent mathematical exposition with complete
derivations. No source page or figure is reproduced in the manuscript.
Bibliography key: Blackwell1953EquivalentExperiments.

## Written artifacts

| Artifact under handbook/ | SHA-256 at this authoring handoff |
| --- | --- |
| parts/p17/value-of-information.tex | 69EE3B40084A78FB82671C4CF922D09AE47EA5F9A80E7D5E2C563C2BE99C612D |
| annex/p17/value-of-information.tex | 1913B9035ACFB7CD9907414E2C55FBE7B7301D8982EA6B4C4306115EDCFB95F0 |

Both saved LaTeX files were read completely by their author. The ten
statement/proof suffixes use thm:p17- and annex:p17. respectively:

| Suffix | Complete construction |
| --- | --- |
| information-policy-value | Signalwise optimization; deterministic attainment; zero-probability outputs without undefined posteriors. |
| information-value-bounds | Ignoring information; perfect-information upper bound; acquisition threshold for costs in payoff units. |
| garbling-simulation | Statewise randomized-policy simulation; composition; mutual equivalence; best and worst experiments. |
| finite-separation-minimax | Finite-dimensional compactness consequences, closest-point separation and a full finite zero-sum minimax proof. |
| finite-blackwell | Source loss-set comparison, all finite decision problems, and the single full-support prior converse via an explicit separating payoff problem. |
| blackwell-trace-route | Source diagonal/trace condition and its minimax quantifier change, with explicit vertices of both polytopes and the final coordinate equations. |
| posterior-splitting | Posterior barycenter and an implementing experiment, including arbitrary rows at zero-prior states. |
| finite-posterior-order | Conditional averaging, finite Jensen and the converse using maxima of linear payoffs. |
| finite-convex-transport | Full finite-vector reduction through an explicit injective simplex embedding; coupling; reverse matrix; every null input row. |
| information-example-checks | Binary signal degradation, service decision and net cost, incomparable experiments, finite transport, and failure of the converse at a prior with zero entries. |

The service example gives value -28/25, EVSI 22/25, EVPI 7/5 and net value
-81/50 at cost 1/2. The two partition experiments favor opposite decisions
and admit neither garbling. All numerical data are stipulated mathematical
examples. No empirical or algorithmic claim about unspecified real inputs
is made.

## Source details for subsequent writing

The finite source comparison uses non-strict named relations P > Q and
P superset Q; these are not strict inequalities between experiments.
The source's convex loss set is closed and bounded. Its finite-vector
Theorem 7 requires a mean-preserving row at every input point, including
zero-weight points; the written construction supplies them.

The general approximation proof on printed p. 268 states convergence of
the centroid approximations on every open set. That assertion cannot be
copied: for mu = (1/2) delta_0 + (1/2) Uniform(0,1) and O = (0,infinity),
the first dyadic cell's positive centroid moves the atom at zero into O.
Every centroid approximation has mass 1 on O, while mu(O) = 1/2. The
subsequent general proof needs a correct weak-convergence argument using
continuous test functions. The finite chapter does not use this claim.

On printed p. 270 the deterministic selection h has N partition coordinates
and values in {1,...,r}. Its mixture weight must multiply lambda_(j,h_j)
over j = 1,...,N. The displayed product ending at r cannot normalize these
weights in general: with N = 3, r = 2 and all coordinate weights 1/2,
the erroneous product assigns total weight 2. The later restricted-decision
construction must use the product over all N cells.

The remaining distinct writing comprises the source's general observation
space extension, restricted k-decision comparison and binary testing-error
formulation, followed by the approved decision chapter's further sequential
and strategic regimes. These require their complete constructions; none is
inferred solely from the finite theorem written here.
