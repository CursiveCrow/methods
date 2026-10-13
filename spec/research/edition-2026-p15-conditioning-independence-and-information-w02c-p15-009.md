# Packet w02ca-p15-009 (P15, section 159.8): authoring note

10 October 2026. Hosts edited in place (editable_hosts):
`handbook/parts/p16/measurable-causal-graphs.tex`,
`handbook/annex/p16/measurable-causal-graphs.tex`,
`handbook/parts/p16/finite-causal-models.tex`,
`handbook/annex/p16/finite-causal-models.tex`.
No new chapter file is needed: every duty is a completion of an existing
treatment in those hosts, so the owned new body/annex files are not created
(no driver insertion is requested).

## Continuation

- Started: MP-0..MP-3 (measurable-causal-graphs C002, C005, C010, C012).
- MP-0 (C002) written: body thm:p16-measurable-ci-calculus now states the
  transformed-tuple clause precisely; annex paragraph "Measurable
  transformations" in annex:p16.measurable-ci-calculus (kernel pi, image
  kernel rho via thm:p15-kernel-joint-measure, product at z outside one null
  set N, return to the product-test definition).
- MP-1 (C005) written: annex paragraph "The whole kernel model" in
  annex:p16.measurable-kernel-randomization (three-part topological induction).
- MP-2 (C010) written: new body lemma thm:p15-w02c-p15-009-root-exposure with
  annex:p15-w02c-p15-009-root-exposure; response-component proof now cites it
  and the moral bridge at the separation step, proves R d-separated from B in
  the exposed graph, and has a full "random parameter" paragraph; body
  statement made precise (kappa, lambda, theta displays).
- MP-3 (C012) written: cross-world field rewritten with Facts 1-6 (Fact 1 puts
  every exposure descendant that is a mediator ancestor in D_M; Fact 6 proves
  every vertex needed for Y is in D_Y with inputs a,m).
- Finite-causal-models disputes C003, C005, C008, C009, C010, C012 written in
  handbook/parts/p16/finite-causal-models.tex with two new results
  (thm:p15-w02c-p15-009-five-variable, thm:p15-w02c-p15-009-chain-weak) and
  their annex proofs appended to handbook/annex/p16/finite-causal-models.tex.
- Self-check: owned body/annex .tex files intentionally not created (all
  duties complete existing host treatments; a P15 chapter here would be a
  stub or a duplicate), so `waves.py unit-compile` fails on the missing
  owned files, as for w02b-p15-009. Scoped scratch build of the four hosts
  (tmp/unit-builds/w02ca-p15-009-hosts/unit.tex) exits 0 with no TeX error;
  only cross-part refs/cites are undefined in that scoped unit. No hard
  check.py finding in the hosts; find_fused_spaces clean.
- Status (first run): all then-listed duties had text.

- Continuation run (10 October 2026, after the usage-limit reset), closing
  the independent assessment's remaining gaps:
  - measurable C009: annex:p16.measurable-interventions rewritten
    (annex measurable-causal-graphs.tex 653-832): general claim for any
    acyclic system with independent disturbances (kernel measurability via
    thm:p15-kernel-joint-measure; independence of the current disturbance
    from the constructed predecessors; regular conditional law; rectangle
    uniqueness induction with thm:p15-kernel-joint-measure); constant
    interventions as the case g_v = t_v (kernel delta_{t_v}); history-based
    kernels: fresh uniform noise on the product space, augmented model is
    a measurable SCM on G^Q with kernels K_w and Q_v, global Markov via
    thm:p16-measurable-global-markov. Body statement (parts 284-301)
    sharpened accordingly.
  - finite C003 (parts 89-197): Wright eqs (1)-(2), fn. 6, Fig. 1(a)/(b),
    dashed double arrow, structural reading ('to be determined from the
    data'; external/internal increase), disturbances responsible for the
    observed variation and assessed qualitatively, missing-link encoding,
    'causal, not associational', experimental/other-assumption uncovering,
    p. 107 central idea. Eqs (3)-(4) via the new linear-effect theorem.
  - finite C005 (parts 303-326 and 792-860 with annex 487-551): SEM as
    main vehicle (Goldberger 1972; Duncan 1975; Bollen 1989), 'until
    recently', new ways of defining and estimating effects in nonlinear and
    nonparametric models, invariance for causal effects and
    counterfactuals; eq. (14) and its four claims; new theorem
    thm:p15-w02c-p15-009-linear-effect.
  - finite C009 (parts 549-563): p. 113 G-computation coincidence and
    adjustment for treatment-affected covariates, tied to item 3.
  - finite C010 (parts 586-605): p. 108 framing quotation related to the
    exact-law criterion and the estimation distinction.
  - finite C011 (parts 655-690): p. 110 unqualified Markovian claim,
    non-Markovian conditions (sec. 3.3), end of sec. 3.2.2 graph claim;
    full observation and positivity as the finite qualification, linked to
    items 1-2 of thm:p16-causal-nonidentification.
  - finite C012 (parts 722-770): p. 107 illustration as pointwise fact,
    p. 111 conclusions, normative orthogonality sentence, attribution of the
    two assumptions to (13) only, P(y|do(x)) variant marked as the
    handbook's own.
  - Locators added this run were read in the held PDF this session
    (pdftotext of PDF pp. 8-18; page images of printed pp. 104, 105, 110
    to verify beta in eqs (1), (2), (14) and Fig. 1).
  - unit-compile still fails only because the owned P15 files do not exist
    (all duties complete host treatments); scoped scratch build of the four
    hosts exits 0 with no TeX error. check.py: only soft notation-scope
    findings in the hosts (\mathcal W new, scoped in the intake CSV).

- Run r4 (10 October 2026), closing finite C001, C003, C012 disputes
  (Pearl 2009 printed pp. 104-106, PDF pp. 9-11, read this session as
  pdftotext layout text):
  - C001: def:p16-causal-dag now defines child, descendant, ancestor.
    New def:p15-w02c-p15-009-causal-diagram (disturbance vertices, solid,
    dashed, dashed double arrows E^<->, kinship over all arrows, path over
    edges of any kind with distinct vertices) and
    thm:p15-w02c-p15-009-diagram-paths (U_i parentless, only child i,
    descendants {i} u de_G(i), acyclic, agreement with G; Fig. 1(b) has
    exactly the two paths (X,Y) and (X,U_X,U_Y,Y), Fig. 1(a) one), with
    annex:p15-w02c-p15-009-diagram-paths. Source paragraph pp. 104-105
    paraphrased before the definition. Distinct-vertex requirement marked
    as the handbook's precision.
  - C003: paragraph after the theorem gives (i) Wright's contribution as
    the source's claim, (3)-(4) as instances; (ii) algebra obscures origin
    for large models, with the path-by-path reading of (4) marked as the
    handbook's observation; (iii) the solving claim with its proviso quoted
    (one marked quotation). New thm:p15-w02c-p15-009-path-solve (after
    linear-effect): beta = Cov/Var under the two assumptions, effects
    fixed by the observational law; M_1, M_2, M_3 share one law, contrast
    2, 0, 0. Annex annex:p15-w02c-p15-009-path-solve.
  - C012: paragraph after def:p16-causal-chain with the p. 106 claims;
    seven-link enumeration (9 possible links minus 2) marked as the
    handbook's reading since the source does not list them. New
    thm:p15-w02c-p15-009-chain-testable: CI of Z,Y given X from the
    factorization; a violating law; each single assumption compatible
    with every law (M_a shared disturbance on the chain graph; M_b
    independent function-valued disturbances on the complete DAG);
    pairwise independence insufficient (XOR). Annex
    annex:p15-w02c-p15-009-chain-testable.
  - Checks: scoped host build (copy of the hosts unit in the scratch
    folder) exits 0, no TeX error; new overfull boxes only in the two annex
    headers (label length, as for the existing five-variable and
    linear-effect headers); find_fused_spaces clean; unit-compile fails
    only on the absent owned P15 files, as before.

- Run r5 (11 October 2026), closing the assessment disputes on finite C012,
  Pearl extent claims, and measurable C003, C005, C007:
  - finite C012 (parts finite-causal-models.tex 945-1072): Definition 1
    (p. 106) related to def:p16-active-path; the p. 106 illustration with
    disturbance vertices, including the misprint (printed U_X _||_ Y | Z;
    the named path gives U_Z _||_ Y | Z); collider path and "may or may
    not hold"; Berkson (1946) and two coins (source attribution only);
    "main opening"/"almost all tests" claim and note 7 (Shpitser and Pearl
    2008, dormant independence) reported as the source's claims. New
    thm:p15-w02c-p15-009-chain-diagram (items 1-5: diagram factorization
    and global Markov on the 6-vertex DAG; the d-separations; counterexample
    to the printed statement; Berkson coins in the chain and the variant
    where independence holds; completeness of the chain's CI test) with
    annex:p15-w02c-p15-009-chain-diagram (annex finite 771-935).
  - Pearl extent: p. 110 "endless confusions in the literature" with note 15
    (read on p. 124, sec. 3.5.2, page image checked for beta and delta/delta
    x) at parts 1150-1168; p. 112 purpose of the truncated factorization
    at parts 648-660.
  - measurable C003 (parts 81-114): Lauritzen's adapted kernels,
    recursive combination (circledast), Prop. 2.46 and Def. 2.47 (p. 66,
    page image checked for notation); the departure (kernels kept in the
    model) stated with a two-model example.
  - measurable C005 (annex 209-222): the source's reason for the upper
    quantile (non-unique quantiles; separate choices may destroy joint
    measurability; operationally defined largest p-quantile), pp. 19-20.
  - measurable C007 (parts 305-411; annex 667-750): p. 65 contrast claim;
    undirected (P), (L), (G) (Def. 2.35 p. 59; p. 60), Prop. 2.37 (p. 60),
    Theorem 2.38 Pearl-Paz (pp. 60-61), (S5) (p. 52); new
    def:p15-w02c-p15-009-undirected-markov and
    thm:p15-w02c-p15-009-undirected-gap (G=>L=>P proved; three equal coins
    on the edgeless graph: P holds, L and G fail, intersection fails;
    directed equivalence restated). p. 68 density strengthening (F),
    Prop. 2.51, Lemma 2.52, Thm. 2.53 reported (page image checked).
  - Checks: scoped scratch build of the four hosts
    (tmp/agent-scratch/w02ca-r5-w02ca-p15-009-b1-author/unit.tex) exits 0,
    no TeX error; undefined refs only cross-file; no new overfull box over
    5pt in the new text after reflowing; find_fused_spaces clean; check.py
    hard failures none in these files; soft notation-scope for \mathcal D,
    \mathcal X, \mathcal G recorded in the intake CSV. waves.py
    unit-compile still fails only because the owned P15 files are absent.

- Run r5 block 2 (11 October 2026), hard guards G13 and G10:
  - G13: the 13 runs of 12 or more words shared with Pearl 2009 in
    parts/p16/finite-causal-models.tex paraphrased (lines near 122, 136,
    244, 271, 436, 546, 722, 762, 790, 872, 1079, 1080, 1102 of the old
    numbering); remaining quotations are at most 6 words. Recomputed with
    the waves.py copy index: no run of 12 or more words in any of the four
    hosts or the new P15 files.
  - G10: owned P15 files now written as a real chapter for 159.8,
    "Conditional Independence of Sigma-Algebras and Its Inference Rules"
    (sec:p15-w02c-p15-009-sigma-ci), from Lauritzen ch. 2, printed
    pp. 39-52 (PDF pp. 44-57), read this session as extracted text:
    Defs 2.1 (p. 40), 2.5 (p. 42); Examples 2.2 (p. 40), 2.3 (p. 41),
    2.7 (p. 43), 2.13 (p. 46); Lemma 2.6 (pp. 42-43); Thm 2.9 (p. 44);
    Thm 2.10 (pp. 44-45); Cors 2.11, 2.12 (p. 45); Thm 2.18 (p. 48);
    Example 2.19 and Cor 2.20 (p. 49); (S1)-(S4), Pearl 1988 conjecture,
    Studeny 1992 (p. 52, source attributions only, no key added). Three
    theorems with full annex proofs; the A5 intersection with null-set
    augmentation is reported as the source's statement only, not proved.
    One cross-link paragraph added after def:p16-measurable-ci.
  - Checks: waves.py unit-compile ok; waves.py verify hard list empty;
    find_fused_spaces clean; check.py shows only pre-existing soft
    notation-scope findings in the P16 hosts. Driver inserts for the new
    P15 files are requested in the return (lead).

## Source provenance, run r5 (read this session)

- Pearl 2009 R-350 held PDF: printed p. 106 (PDF p. 11) as pdftotext
  layout text; pp. 110-112 (PDF 15-17) as text; p. 124 (PDF 29) as text
  and page image (note 15). Berkson (1946), Shpitser and Pearl (2008),
  Holland (1988), Whittaker (1990), Wermuth (1992), Wermuth and Cox (1993),
  Sobel (2008) appear only as the source's attributions; no key added.
- Lauritzen 2019/2020 held PDF: printed pp. 19-20 (Theorem 1.28 proof),
  52 ((S1)-(S5)), 59-61 (Def. 2.35, (P), (L), (G), Prop. 2.37, Theorem
  2.38), 65-68 (Theorem 2.44, Prop. 2.46, Def. 2.47, Prop. 2.48, Theorem
  2.49, Example 2.50, (F), Prop. 2.51, Lemma 2.52, Theorem 2.53) as text;
  pp. 66 and 68 also as page images (PDF pp. 71, 73).

## Source provenance (read this session)

Pearl, J., "Causal inference in statistics: An overview", Statistics Surveys
3 (2009) 96-146, author-hosted R-350:
`source/references/pearl-causal-overview-2009/pearl-2009-ucla-r350.pdf`.
Printed pp. 103-113 (PDF pp. 8-18) were read as extracted text; p. 108 was
also read as the page image `source-13.png` to verify the primes in
equations (8) and (9). Locators used: sec. 3.1 pp. 103-104 (Wright 1921;
directionality and missing arrows; disturbances vs regression residuals
p. 104); sec. 3.2 p. 107 (extension beyond linear SEM; Haavelmo 1943,
Strotz and Wold 1960, Spirtes et al. 1993, Pearl 1993a and 2000a, Lindley
2002; autonomy, Simon 1953 and Koopmans 1953); sec. 3.2.1 p. 108 (eqs.
(6)-(9), variance, controlled distribution called "causal effect" in Pearl
2000a, 1995a; controlled/experimental reading); pp. 108-109 (identification
contrast: Hurwicz 1950, Marschak 1950, Koopmans 1953, Duncan 1975, Bollen
1989; Definition 2 attributed to Pearl 2000a p. 77 and its gloss); sec.
3.2.2 p. 109 (eqs. (11)-(13), the two assumptions); sec. 3.2.3 pp. 110-111
(Theorem 1, Corollary 1, eq. (16), the P(z|do(x0)) display, n. 8); p. 112
(Fig. 3, eqs. (18)-(22), Robins 1986, Arjas and Parner 2004). The Fig. 3
edge set was read from the factors of eq. (18). The cited secondary works
are reported only as the source's attributions; none is cited directly, so
no bibliography key was added.

Measurable-graph duties use only handbook results
(thm:p15-kernel-joint-measure, thm:p15-value-conditional-law,
thm:p16-moral-separation-bridge, thm:p16-measurable-global-markov,
thm:p16-measurable-ci-calculus); no new source locator was written there.
