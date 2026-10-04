# P16 authoring: causal mediation

8 September 2026. Block began 16:29:52 UTC; maximum deadline 17:14:52 UTC.
Owned outputs are the new body and annex `causal-mediation.tex`, this note,
`handbook/bib/intake-p16-mediation-pearl2001.bib`, and the two new source
capture directories listed below. The assigned manuscript/note/intake paths
were absent before writing. No earlier or shared file was edited. Root owns
drivers, canonical bibliography, notation and subsequent admission.

## Verified primary sources

Pearl, Judea. **Direct and Indirect Effects**. The complete body identifies
itself as R-273-UAI, June 2001, in *Proceedings of the Seventeenth Conference
on Uncertainty in Artificial Intelligence*, Morgan Kaufmann, pp. 411–420.
This is the original UAI presentation, not the separately discovered 2005
JSM version and not the later 2013 arXiv record.

- Verified author URL: https://ftp.cs.ucla.edu/pub/stat_ser/R273.pdf
- Local: `source/references/pearl-direct-indirect-uai2001/pearl-r273-uai2001.pdf`
- Extent: **10 complete pages, 228,623 bytes**.
- SHA-256: **6260C553812B3550AD9C96BAF51E1359C77CF72890D0183AB2726CDFCAAF3A8F**.
- Metadata title `r273-uai.dvi`; PDF creation/modification 14 June 2004.
  The actual first-page UAI 2001 citation and R-273-UAI heading establish
  presentation identity; the conversion timestamp is not its publication date.
- All ten pages read in extracted text and as source images. OCR mangles
  letters, subscripts and graph bars, so the actual images supplied the
  exact formulas and graph operations. Poppler reported missing Symbol and
  ArialUnicode display fonts; all required equations remained readable.
- Key: `Pearl2001DirectIndirectEffects`.

Vansteelandt, Stijn, and Rhian M. Daniel. **Interventional effects for
mediation analysis with multiple mediators**. The actual body identifies
the held version as a Europe PMC author manuscript, available 1 June 2017;
final edited publication: *Epidemiology* 28(2), March 2017, 258–265,
DOI 10.1097/EDE.0000000000000596.

- Verified institutional record: https://biblio.ugent.be/publication/8545462
- Download: https://backoffice.biblio.ugent.be/download/8545462/8545463
- Local: `source/references/vansteelandt-daniel-interventional-mediation-2017/vansteelandt-daniel-2017-author-manuscript.pdf`
- Extent: **19 complete PDF pages, 1,068,605 bytes**.
- SHA-256: **A0A42B1615A790DB76515EEE845882436CA7769095EA78945A21627B390A7BC5**.
- Actual metadata authors/title agree with the body; creation/modification
  2 February 2017. The author manuscript remains distinct from the journal
  pagination and its separately referenced eAppendix.
- Text read in full for PDF pp. 1–6. The required single-mediator section
  is pp. 2–4; its displayed formulas were read in the pp. 2–4 images.
  The multiple-mediator continuation beyond p. 6 and the eAppendix have
  not been read or claimed as completed treatments.
- Key: `VansteelandtDaniel2017InterventionalEffects`.

Both captures used scoped free downloads. No purchase or paid source was
used. Images are source-reading scratch files in the old task's
`tmp/pdfs/p16-mediation-source/`; no manuscript PDF was rendered.

## Written mathematical extent

Fourteen full body/annex proof pairs: `mediation-measurability`,
`mediation-decompositions`, `mediation-countable-formula`,
`mediation-kernel-formula`, `mediation-finite-observed`,
`mediation-general-observed`, `mediation-four-set-criterion`,
`mediation-parent-scope`, `mediation-policy-identities`,
`mediation-nonlinear-example`, `mediation-crossworld-countermodels`,
`mediation-induced-confounding`, `mediation-diagonal`, and
`mediation-path-semantics`. Body prefix `thm:p16-`; annex prefix `annex:p16.`.

The original Pearl routes are retained separately: experimental
cross-world factorization; observational identification of its factors by
any justified method; the four-set graphical adjustment route for finite
intermediate mediator vertices; the independent-error full-parent
specialization; reverse-transition decompositions; and edge-subgraph
reference-input semantics with the Figure 3 nonidentification witness.

The graph proof supplies its actual cross-world bridge. In the cut graph's
ancestral moral graph, remove baseline and distinguish the response
component from every mediator component. Restore outgoing mediator edges
needed for mediator-to-mediator ancestor routes; a route stopped at its
first mediator shows all restored endpoints and new moral edges remain
on the mediator side. Assign exposure inputs a on the response side and
b on the mediator side, preserving unchanged baseline. The resulting
same-background auxiliary model has response Y_(a,m), mediator tuple M_b,
and the required separation. The other three graph conditions give the
two sequential response adjustments and the reference-mediator adjustment.

For standard Borel spaces the jointly measurable response family
f(a,m,C,R) is defined before evaluation at random M_b. A single product
conditional law of (M_b,R) given C licenses the nested integral. The proof
uses actual joint-measure equality and the kernel section-integral theorem;
it does not infer diagonal substitution from fixed-m versions. The observed
general-space theorem uses uniform response-background exchangeability and
absolute-continuity transfer from the observed (C,L,M) measure to the target
measure. Exposure atoms are explicitly required for that observational
corollary; experimentally supplied intervention kernels have no such
observational atom requirement. Signed means have explicit absolute
integrability hypotheses. These sufficient general-space premises are
stronger than pointwise fixed-response independence and are not claimed
to be necessary or automatic from observed data.

## Calculated examples and direct corrections

- Nonlinear response A+2M+3AM gives all four nested means, both decompositions,
  controlled effect 1+3m, and interaction remainder 3/2.
- Two finite models have identical positive observations and every ordinary
  observed-coordinate intervention law, but natural direct effects 1/2 and
  0. Their common identified independent-draw effect is 1/4. Ordinary
  exposure/mediator exchangeability and overlap remain intact.
- The fully observed independent-error graph A→L→M→Y, L→Y has two latent
  couplings of (L_0,L_1) with the same positive observed and intervention
  laws. PNDE is -1/32 or 1/32; TE is 3/32. Correct independent-draw values
  give total contrast 5/64, rather than natural TE 6/64. Including (L,M)
  as the full response-parent mediator tuple changes the target and gives
  direct effect zero. The same pair proves the source Figure 3 path effect
  nonidentified, with values -1/16 and 0.
- A continuous diagonal model has independent uniform U,V, M_0=U,M_1=V,
  Y_(1,m)=1{m=U}, Y_(0,m)=0. Every fixed controlled response is zero almost
  surely, so all four pointwise independence conditions hold, but
  Y_(1,M_0)=1 pointwise. It shares observations and controlled-intervention
  laws with the zero-response model. This disproves an unqualified
  uncountable extension of the source's summation proof. Measurability and
  mediator absolute continuity alone do not fix it; the new uniform
  product-kernel premise is the stated general-space completion.
- A finite M=A example proves missing mediator overlap cannot be repaired
  by assigning an arbitrary conditional value to the absent cell.

The active statements correct the source's scope directly. Pearl's
Corollary 2 uses all response parents, not an arbitrary selected mediator;
the independent response disturbance is independent of its nondescendant
inputs, not literally of every downstream variable. His Eq. (10)'s
stray outcome-event notation inside an expectation is not copied.
The 2017 manuscript's written consistency line `M_a=Y` is represented
correctly as M_a=M. Its displayed Eq. (1) omits L in the reference-arm
conditional mean; the proved formula keeps L in both arm-specific means.
The limited equality of diagonal interventional and natural means states
the single-world response exchangeability Y_a independent of A given C
actually used in its proof. That independence is not inferred from
separate fixed-controlled-response and mediator marginal conditions.

## Dependencies, notation and remaining scope

The actual existing finite-counterfactual body was read first. Its common
worlds, composition and twin semantics are reused, not rewritten. General
proofs use the actual `regular-conditional-laws.tex` body and the complete
used annex proofs through `kernel-joint-measure`, including standard Borel
existence, common-null-set uniqueness, observation-space kernels and jointly
measurable kernel section integration. The finite graphical proof uses the
existing ancestral moral bridge and finite global Markov results. The
governing all-changes-before-reviews contract remains active.

Local notation: A,M,C,R; a_0,a_1; M_a,Y_(a,m),Y_(a,M_b); theta_ij;
CDE, TE, PNDE, TNDE, PNIE, TNIE, I; baseline law nu; mediator kernel eta_b;
response-background kernel kappa; controlled-response kernel Q_a and mean
q_a; intermediate confounder L and L_a; e_a, lambda_a, rho_a, mu_a;
policy kernel k, independent draw G^k, J(a,k), J_ij; absolute continuity
and OV; W_0,...,W_3; and edge subgraph g with model M_g^0. Root owns the
canonical notation and bibliography merge.

The finite and countable mediation formulas and the stated standard-Borel
kernel versions are fully proved. The source's graphical corollary here
covers finite intermediate mediator vertices; extending its graph theorem
to arbitrary standard-Borel DAGs requires a corresponding general global
Markov theorem, not the existing finite one. Graph sets containing arbitrary
nonintermediate vertices require their own checked nondescendant premises;
the full-parent specialization is supplied separately. No blanket completion
of those stronger graph variants is claimed. General path-specific
identification algorithms, the 2017 multiple-mediator refinement/eAppendix,
and estimation/asymptotic guarantees remain distinct writing obligations.

The author read the complete actual body and all fourteen reordered annex
proofs, corrected the definition and graph-set details found, and read the
source note and bibliography intake. Independent reviews, scanners, tests, manuscript builds,
manuscript renders and acceptance checks are deferred to the completed
manuscript change set.
