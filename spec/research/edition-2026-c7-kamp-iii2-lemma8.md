# Edition 2026 C7: Kamp III.2, Lemma 8 foundations

Date: 8 September 2026. Author: /root/kamp_lemma7_author.
Repository: C:\Dev\the-methods-of-reason. Requirement: C7 / N-c-012.
Block start: 06:51 UTC; 45-minute deadline: 07:36 UTC.
Standing: seven completed supporting results; the full Lemma 8 induction remains open.

## Frozen authored files

| Owned artifact | Extent | SHA256 |
| --- | --- | --- |
| handbook/parts/p09/presentations/kamp-iii2-lemma8.tex | 493 lines; 20,892 bytes | ECC3896B4F0C25C58914FFBB9D03A49447D89F5146FF8949EF2CF9B34AD6F61E |
| handbook/annex/p09/kamp-iii2-lemma8.tex | 762 lines; 36,037 bytes | 8740AE1FCC283B7313511073AD8D05B167FD92C1E207C37A984D53D00870BF8F |

The closed results are the exact well-founded family comparison, the complete
finite-family cut construction, the atomic base and normalization, explicit
elementary representations for accumulation adjacent to a fixed endpoint,
all eleven complete-order boundary configurations, fixed-endpoint interpolation
in both orientations, and the corrected full guarded boundary decomposition.
Each has a complete reciprocal proof. This is substantive partial completion
of Lemma 8; it is not completion of its required I(x,y) induction. The active
proof boundary identifies that remaining obligation and no full Lemma 8
theorem is marked proved.

Only these two new manuscript files and this note were edited. Shared routes,
registry, bibliography, admission and generated artifacts remain root-owned.

## Primary source and complete reading

J. A. W. Kamp, *Tense Logic and the Theory of Linear Order*, UCLA dissertation,
1968; existing key Kamp1968.
Held PDF: tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf, 128 pages.
[Institutional source](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf).
Verified before and after this block:
C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA.
Printed page n is physical page n + 9, counted from one.

The entire exact Lemma 8 extent was frozen and personally read before writing:
printed pp. 83-92, physical pp. 92-101. Its proof ends on p. 92 immediately
before Lemma 9. Every complete page was read from a fresh 180-dpi rendering
of the verified source. The two confirmed defective passages on printed
pp. 84 and 88 were also freshly rendered and read at original 300-dpi size.

| Printed page | Complete inspected content |
| --- | --- |
| 83 | Lemma 8 statement; exact At(z), Bp(x,z), Bp(z,y) family; occurrence length and length-one At convention; finite-family comparison; start of fresh-occurrence reduction. |
| 84 | Normalization, atomic base, added Q disjunct and printed tautology substitution; choice of maximal phi and remaining family. |
| 85 | All alpha and beta boundary conditions and gamma_1 through gamma_11; explicit Com exhaustion. |
| 86 | chi_1, chi_2 and the first bracketing proof using Lemma 6. |
| 87 | chi_3, its two claimed implication directions, and the beginning of chi_4. |
| 88 | Remaining chi_4 and chi_5 through chi_9; full chi_6 formula used in the finite countermodel. |
| 89 | chi_10, chi_11, omitted-case assertion; source's atomic substitution step and start of alpha_1 representation. |
| 90 | n=1 and n>1 limit clauses for alpha_1; remote beta_1 assertion; beginning of repeated Lemma 7 elimination. |
| 91 | Complete finite-cut residual bound and repeated-elimination claim. |
| 92 | Opposite-orientation argument, explicit end of Lemma 8 and start of Lemma 9. |

Printed p. 93 / physical 102 was also read only to locate subsequent source
boundaries. Pages after that were generated during the initial range search
but were not read or used as evidence. Source images are retained under
C:\Users\Crow\Documents\Codex\2026-08-10\phase-4-handover-migration-campaign-written\tmp\pdfs\kamp-lemma8-source\.
The actual target pages are page-092.png through page-101.png; detailed source
pages are detail-093.png and detail-097.png. No manuscript PDF was rendered.

## Completed constructions and source corrections

The source comparison is exactly lexicographic in (maximum length, number of
members at that maximum). The proof establishes this equivalence, well-foundedness,
deletion of a maximal member, and the decrease after replacing every other
basic member by its allowed cut residuals. Arbitrarily many shorter residuals,
empty residuals and output coincidences are included. The result does not
count fixed-side conjuncts as members of the reduced universal family.

The finite-family cut construction enumerates the product of all individual
cut power sets. For k input words with n_j intervals, it has
2^(sum_j(2 n_j - 1)) choices, with one empty-tuple choice at k=0. Both complete
quantified equivalences are proved for arbitrary auxiliary formulas. The
selected subsets are fixed before the universal endpoint varies; a residual
word or cut may vary with that endpoint. Every fixed-side conjunct is retained.
Every original word contributes at most one residual of its own length and
none longer. This supplies a closed finite-family version of the source's
repeated Lemma 7 step at one strict cut.

The normalization replaces each complete At formula by one fresh atom and
each basic predicate occurrence by its own fresh atom, then restores them
through actual proper substitutions. Whole-At replacement is necessary to
retain the declared grammar when the input is its particular tautology or
has repeated predicate letters. Family cardinality and all length counts
are preserved. The point-only and empty-family base cases have explicit
one-interval elementary representatives.

**Correction K8-Q, printed p. 84.** The source adds Q(z) as a disjunct and
prints substitution of P_0(z) OR NOT P_0(z) to recover the original formula.
That makes the whole universal disjunction true. On 0 < 1 < 2 with a single
basic input pattern whose unary predicates are all false, the original
universal formula is false at 1, while the substituted formula is true.
The active construction substitutes the source falsehood F^K instead.
The full restoration and I-substitution argument is supplied directly.

The fixed-endpoint limit result completes the source's alpha_1 construction:
the endpoint predicate and a first interval neighborhood are combined with
the exact limiting suffix. At n=1 the suffix is a unary strict limit; at
n>1 it is the original positive-stage Lf pattern. A two-interval elementary
word gives the full guarded Lin equivalence. Its opposite-endpoint version
uses a limiting prefix and the last interval predicate and is also proved
directly. This second version fixes the terminal endpoint; it is not the
different source beta_1 assertion that fixes a remote initial endpoint.

The boundary classification uses the actual truth set within (a,b). Empty
and singleton sets are separate, and the nine remaining configurations
combine endpoint, attained-interior and unattained-interior types with
strictly distinct infimum and supremum. All six type conditions are given
as first-order formulas and proved equivalent to their order meanings.
Completeness is used only to obtain the two extrema. The interpolation
proof obtains actual truth-set members on both sides of each middle point
and applies Lemma 6; the right orientation is proved by explicitly reversing
the word, realization, order and existential closure.

**Correction K8-BRACKET, printed pp. 88-89.** The source claims chi_i implies
the target for every i, but chi_6 omits the final bracketing condition.
Let T={0,1,2,3,4,5}, x=0, y=5, phi have word (A,B,C), and put
A={0,3}, B=T minus {2}, C={1,4}, Q=T minus {4}, F={phi(x,z),Q(z)}.
Every input predicate occurs once, and Q occurs in no basic input.
The fixed-start truth set is {1}. Printed chi_6 holds with u_1=1:
its lower universal interval is empty; Q holds at 2 and 3; its unrestricted
past closure holds at 4 via initial point 3. The target fails at 4 because
Q(4) is false and phi(0,4) crosses the B-false point 2. The order is finite
and belongs to Com, so completeness does not repair the claimed implication.
The complete predicate verification is in the annex.

The active corrected branch construction retains the actual boundary
descriptor, all outside-interval tests, and the missing-boundary point tests.
Each of its eleven branches is proved conditionally equivalent to the target
under its own descriptor over Lin; the full disjunction is equivalent over
Com. The descriptor formulas keep the original fixed endpoint in phi and
both original endpoints in every remaining disjunct. Their Gamma_i symbols
name the corrected precise configurations; this note does not assert literal
equivalence to every printed gamma_i spelling or certify every other omitted
source case. The full elementary-representation repair remains below.

## Exact proof pairs and root intake

| Body result | Reciprocal annex |
| --- | --- |
| thm:p09-kamp-family-rank | annex:p9.kamp.family.rank |
| thm:p09-kamp-family-cut | annex:p9.kamp.family.cut |
| thm:p09-kamp-family-normalization | annex:p9.kamp.family.normalization |
| thm:p09-kamp-fixed-endpoint-limits | annex:p9.kamp.fixed.endpoint.limits |
| thm:p09-kamp-eleven-boundaries | annex:p9.kamp.eleven.boundaries |
| thm:p09-kamp-hull-interpolation | annex:p9.kamp.hull.interpolation |
| thm:p09-kamp-corrected-boundary-decomposition | annex:p9.kamp.corrected.boundary.decomposition |

Root should input the body after Lemma 7 in
handbook/parts/p09/presentations/n-c-012.tex and its matching annex after
Lemma 7 in handbook/annex/p09.tex. Existing Kamp1968 supplies all citations.

Local P9.4 symbol roles to record: F,G,G^Q; D_F and U_F; ell, M(F), c(F)
and prec; rho_j,n_j and the indexed cut formulas; the finite product J,
tuples bold J and S_J/R_J aggregates in both orientations; C_W^+/C_W^-,
lambda_W^+/lambda_W^- and V_W^+/V_W^-; the fixed truth formula H(t),
guarded closure P(t), truth set R_(a,b), and interval abbreviations V_D;
lower/upper bounds l,h and type numbers lambda,mu; Gamma_i, endpoint tests
E_j, branch matrices K_i and branches Z_i; opposite order, reversed word
and reversed basic pattern in the right-interpolation proof. Each role
is declared locally in the actual LaTeX.

## Verification and precise remaining work

Both authored files were read back completely, including all later additions.
The existing tools/check.py scanner reports zero findings, seven reciprocal
proof pairs, 24 declared labels and valid citation keys against the current
bibliography. It was used only on the two new files. No software test was
added, and no manuscript build, render, generator, commit or admission action
was performed. All new references identify actual prerequisite definitions
or proof results. Source/error judgments here remain author findings for
fresh independent source, topic and publication review.

The exact accepted Lemma 7 body and annex were reread/checked against
3411BB4A552755CAFEF4675851A764A8605CBE36D402C6CFE022E397DE9F9778 and
3E71146A7142A8A2BA26983A6A23634D9E7D3B52AA8A5F4FD2C9CC8793BD817F.
Prior full readings of the unchanged Lemma 1 realization proof and Lemma 6
body/annex were reused after live hash checks. The actual limiting-class
definitions and complete interval-substitution proof were reread, as were
the exact At grammar and current Com definition. Relevant unchanged hashes:
Lemma 1 body 3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6;
annex 631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1;
Lemma 2 body 49C59D4BDF9169590457F73F3841B35E9620F6C4A54083044DAD625598823677;
annex 75BAE1D38B195849018E8F573741A7F04B8F0984C6804FECFF770D00602FA4F2;
Lemma 4 annex 2C1DA5AE40BC16DD4533C64714DEF9868F93D2202202D30E6FFE10AA6DEB451E;
Lemma 6 body EBB6DEAE8B3C2538DDB8CF5AB9CF24C7C52AA0EB6202585A7E7B33B188AE99DB;
annex 9EA42EBBDFFE6A6A9071C581E2F10721CF2D2504B96EC1CE51FE15658469D171.
The frozen original remains 0509750C13B88A4E18914BD52BDE171C725CBA14221CBFC2227D7693A2B421CC.
The research and PDF skills were reread completely for this block. Research
was performed as the parent's assigned background agent, with no further
agents permitted. PDF guided source reading only; no PDF-authoring marker
was applicable.

The next bounded assignment should complete the following substantive work:

1. Give valid elementary representations for the remote-endpoint and
   unattained-interior boundary conditions needed by suitable corrected
   branches. A first-order descriptor alone does not have property I by
   definition; retaining all Gamma_i proves correctness but not membership.
   The source's beta_1 step and omitted cases need their actual constructions.
2. Assemble the finite-family cut theorem at each strict interior boundary,
   preserving all fixed-side conjunctions and endpoint bindings. Every
   induction call must involve an actual smaller family in At/Bp form;
   any elementary one-variable replacement must enter through a justified
   proper-substitution step, not be silently reclassified as At.
3. Complete all eleven corrected branches and both orientations of the
   I(x,y) induction, using the atomic base and exact rank decrease proved
   here. Only then add a full Lemma 8 result with a complete reciprocal proof.

The whole source extent for this unfinished portion remains pp. 83-92.
Lemma 9 begins on printed p. 92, but it depends on the full Lemma 8 result
and cannot yet be treated as having that prerequisite. Independent review,
root integration, applicable production evidence and formal admission of
the closed supporting results are also still required.
