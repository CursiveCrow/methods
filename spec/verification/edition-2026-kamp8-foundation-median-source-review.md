# Independent source review: Kamp Lemma 8 foundation and single-peaked majority

Review opened 8 September 2026 at 07:19 UTC. The assigned block ends at
08:04 UTC. This report belongs to the independent source-fidelity reviewer.
Completed at 07:32 UTC after all four frozen manuscript hashes were rechecked.
The complete reading finished before the first 15-minute checkpoint; concrete
progress messages were sent during the block and no later checkpoint was needed.

## Retrieved Content

### Median manuscript: body lines 13–20

```tex
The source problem is Rubinstein's Lecture 9, Problem 2, in the author
revision dated 11 January 2015. Its alternative set is the whole interval
\([0,1]\), and it inherits Lecture 9's strict individual-order domain
\cite[pp.~123, 128]{Rubinstein2015LectureNotes}. We retain that regime.
The argument also gives the explicitly stated results for other ordered
sets. The median, finite procedure and parity refinements are deductions
supplied here; the source poses the odd-electorate aggregation result
as a problem, rather than printing its solution.
```

### Median manuscript: body lines 152–159

```tex
\begin{hbtheorem}{thm:p17-even-median-interval}{proved=annex:p17.even-median-interval}{Even electorates: the exact weak-winner interval}
Let \(n=2k\), \(k\geq1\), and keep strict single-peaked inputs
on the same nonempty linearly ordered \(X\). The set of weak Condorcet
winners is exactly \([l,u]_X\), where \(l,u\) are the two central
peaks. There is a strict Condorcet winner exactly when \(l=u\);
in that case it is their common value. This conclusion does not assert
transitivity of the weak majority relation for an even electorate.
\end{hbtheorem}
```

### Kamp foundation manuscript: body lines 478–493

```tex
\begin{proofboundary}{def:p09-kamp-lemma8-remaining}{The remaining elementary-representation induction}
The proved results above establish the comparison, normalization and
complete guarded boundary decomposition, and elementary representations
for accumulation adjacent to the fixed endpoint. To finish Lemma~8 one must
still construct finite \(\operatorname{Ep}(x,y)\) representations
for suitable boundary branches and supply every repeated cut-elimination
step, using only smaller-family instances and the preceding proved
closure lemmas. In particular the boundary descriptors are not asserted
to have property \(I\) merely because they are first-order formulas.
The finite-family cut theorem supplies all alternatives at a single
strict cut, with the correct residual bound and every fixed-side
conjunct. Their arrangement across the complete boundary branches
and the resulting elementary representations remain to be supplied.
The claimed \(I(x,y)\) conclusion of the
full Lemma~8 is not established by the boundary decomposition alone.
\end{proofboundary}
```

## Supplementary Notes

### Scope and independent reading

The median unit passes this source/text review at its assigned frozen
identities. The seven supporting Kamp foundation results also pass at their
assigned frozen identities. No source-scope or mathematical defect was found
in either bounded unit. The full Kamp Lemma 8 conclusion remains unproved
and is not accepted by this review. No unfinished author file was read.

| Median target | Full reading | SHA-256 |
| --- | --- | --- |
| `handbook/parts/p17/single-peaked-majority.tex` | Lines 1–309, complete | `BA7EF43E3E28026890EE178439A32CF13614D6E430CF916350FEFC479D423063` |
| `handbook/annex/p17/single-peaked-majority.tex` | Lines 1–404, complete, every proof | `1AA78E18617B8DE56578E7DA915F5A02F276FEA09737A21811EB21705E3AC3E0` |

Both target hashes were independently checked against the actual files.
The intake was read as a map, not as proof:
`spec/research/edition-2026-p17-single-peaked-majority.md`.
Its verified hash is
`6FEE2C27D11C89679F1294151D1E5A2417B1A1112C4D98AC682DF78D0B840128`.

The complete current `handbook/parts/p17/social-choice.tex` and its annex
were read directly. Their identities are respectively
`224340F36A0774478ED6CFD8713601190B23F97BE7950106DD4CD8F8B71E64FA`
and `C76738A8942F81BD5BF37E3701A30820AD24992E5B3805EC448CD9D883D69E6F`.
The complete finite-preferences body was also read, including the actual
weak/strict/indifference definitions. The finite-preferences annex was not
needed for an unproved dependency: the new majority proof explicitly
establishes the relation properties it uses. No other current reviewer
report was opened.

The governing edition contract and handbook conventions were read in full.
The Research and PDF skills were read before source work. This is a
delegated independent research task; no further agent was created.

### Rubinstein identity and full source extent

Held primary source:
`source/references/rubinstein-microeconomic-theory-2015/rubinstein-second-edition-revision-2015-01-11.pdf`.
Its SHA-256 was independently verified as
`F7CEA2C4F48C77D93DD25C30BBDA83E051C6562A589256AAC8CBA1B5084A33F8`.
Physical pages 1–3 were read as text to verify title, author, second edition,
and the 11 January 2015 author-revision date. All seven complete assigned
pages, printed 122–128 / physical 136–142, were personally read both as
extracted text and full page images. Retrieval occurred during this block.

Printed 123 declares strict individual orderings and weak social output.
Problem 1 on printed 128 explicitly changes its own binary input domain
to permit individual indifference. Problem 2 supplies the entire interval
[0,1], an attained individual peak, strict improvement toward that peak on
both sides, and an odd finite electorate. The new definition at body
25–55 preserves those conditions. Its proof does not add continuity,
symmetry, a numerical utility, a distance ordering, or a finite alternative
set to that source theorem.

Problem 2 asks for the aggregation result but prints no solution. The
manuscript correctly identifies its supplied proofs, ordered-set extension,
median and parity conclusions, finite procedure, and counterexamples as
handbook deductions. It does not attribute an unprinted source proof to
Rubinstein or import the source's separately discussed strategic results.

### Checks of every median pair

| Body / annex locations | Result of the direct reading |
| --- | --- |
| Body 57–73 / annex 11–51 | Unique greatest peak follows by using the peak as the comparison point. The four triple rankings and their converse retain an attained greatest element on infinite domains. |
| Body 103–117 / annex 53–105 | Odd counts compare every distinct pair. The two voter-set inclusions exclude both orientations of a three-cycle; failure of transitivity then produces such a cycle. This proves the entire relation on the full interval. |
| Body 135–150 / annex 107–150 | The two coalitions of at least k+1 voters prove the median beats every rival and prove the whole social ordering is single-peaked. Repeated peaks and endpoints are retained. |
| Body 152–159 / annex 152–186 | Every point between the central peaks has at least k votes against each rival; outside points lose by at least k+1. Distinct central peaks are two weak winners, excluding a strict winner; coincident peaks give a strict majority against every rival. |
| Body 201–252 / annex 188–263 | The supplied-axis permutation and adjacent-rank checks are necessary and sufficient. Histogram positions retain repeated peaks. The pair count and victory-count ordering are correct in the explicitly stated unit-cost finite representation. |
| Body 161–197 and 254–277 / annex 265–352 | All ten five-voter pair counts were recomputed directly from the given rankings. The cycle's excluded valley and the four-voter nontransitive social ties are real. The interval distance construction uses an explicit strict tie-break, so it remains in the source's strict-input domain. |
| Body 282–296 / annex 354–404 | Pareto, anonymity and restricted-domain IIA follow from counts. Each candidate dictator has an admissible refuting profile. The explicit interval order with its middle point below both endpoints proves the domain is proper. The missing unrestricted-domain premise is exactly the relevant Arrow distinction. |

### Kamp identity and complete source extent

| Kamp target | Full reading | SHA-256 |
| --- | --- | --- |
| `handbook/parts/p09/presentations/kamp-iii2-lemma8.tex` | Lines 1–493, complete | `ECC3896B4F0C25C58914FFBB9D03A49447D89F5146FF8949EF2CF9B34AD6F61E` |
| `handbook/annex/p09/kamp-iii2-lemma8.tex` | Lines 1–762, complete, every proof | `8740AE1FCC283B7313511073AD8D05B167FD92C1E207C37A984D53D00870BF8F` |

Both hashes were independently checked. The intake at
`spec/research/edition-2026-c7-kamp-iii2-lemma8.md` was read completely and
its hash verified as
`1F4F79991AB23E61A20ACC5FAA9D2925ED29E85E056DBCFFA462C8FE7ECE59FC`.
It was used to locate claims, not to establish their correctness.

The held thesis `tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf` was independently
hashed as `C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA`.
All ten complete assigned pages, printed 83–92 / physical 92–101, were
personally read as full source images. The embedded text extraction is
corrupt and was not used to resolve formulas. The higher-resolution source
images for printed 84 and 88 were additionally read. The source's full
Lemma 8 proof ends before Lemma 9 on printed 92; the new body does not
claim to complete all that source extent.

### Actual Kamp prerequisites read

The complete current bodies of Lemmas 1, 2, 3, 4, 6 and 7 were read.
The complete Lemma 1 realization proof and complete Lemma 6 and Lemma 7
annexes were read. In the Lemma 4 annex, lines 1–240 were read, covering
the entire elementary-word and substitution-interface proofs. Its later
fusion proof was not needed for a new proof claim here and was not reread.
The actual At grammar in `kamp-iii1-normal-form.tex`, lines 66–128, and
the four order-class definitions near the beginning of `n-c-012.tex` were
read directly. The complete Lemma 2 body supplies the exact limiting-class
quantifiers used by the new accumulation construction; the new proof
uses those definitions and does not depend on the old limiting translation
proof.

Relevant verified dependency identities:

| Prerequisite | SHA-256 |
| --- | --- |
| Lemma 1 body | `3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6` |
| Lemma 1 annex | `631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1` |
| Lemma 2 body | `49C59D4BDF9169590457F73F3841B35E9620F6C4A54083044DAD625598823677` |
| Lemma 3 body | `811AAA41E515F647CB6BC252A4AFEF59279B8338A0FBB43BE72DA3E572A29BA3` |
| Lemma 4 body | `1821FB12C4E77B1D531A3BB154581451A972745BAFFAE1FF0611E34152CF13EB` |
| Lemma 4 annex | `2C1DA5AE40BC16DD4533C64714DEF9868F93D2202202D30E6FFE10AA6DEB451E` |
| Lemma 6 body | `EBB6DEAE8B3C2538DDB8CF5AB9CF24C7C52AA0EB6202585A7E7B33B188AE99DB` |
| Lemma 6 annex | `9EA42EBBDFFE6A6A9071C581E2F10721CF2D2504B96EC1CE51FE15658469D171` |
| Lemma 7 body | `3411BB4A552755CAFEF4675851A764A8605CBE36D402C6CFE022E397DE9F9778` |
| Lemma 7 annex | `3E71146A7142A8A2BA26983A6A23634D9E7D3B52AA8A5F4FD2C9CC8793BD817F` |

### Checks of every Kamp supporting pair

| Body / annex locations | Independent conclusion |
| --- | --- |
| Body 58–78 / annex 6–70 | The exact source relation is equivalent to comparing maximum length and then its multiplicity. The empty family has no predecessor. Deleting a maximum and permitting at most one equal-length residual per remaining member gives the stated decrease; lower-length additions and coincident outputs do not invalidate it. |
| Body 80–166 / annex 72–176 | The product of all cut subsets is finite, including its sole empty tuple. Both implication directions in both orientations keep every fixed-side conjunct and select subsets before the universal endpoint varies. The rank application is explicitly conditional on actual At/Bp retained members and one enumeration of each replaced member. |
| Body 168–196 / annex 178–273 | Atomic and empty bases have an explicit one-interval elementary representative. Whole-At replacement resolves the special-tautology grammar issue. Fresh letters avoid every old letter and P_0; later restorations cannot change earlier inserted original formulas. Adding an atom leaves the rank unchanged only in the stated M>1 regime. Falsehood removes the fresh disjunct. |
| Body 198–253 / annex 275–386 | Both fixed-endpoint accumulation equivalences are proved by extracting and reinserting the first or last point of a full realization. The exact one-letter limit and positive-stage suffix/prefix cases agree with the actual Lp/Lf clauses. The witness chosen below the minimum, or above the maximum, of two given points preserves the needed end gap. Both representatives have two interval pieces and correct guarded Lin scope. |
| Body 297–372 / annex 388–523 | Complete orders supply the nonempty bounded truth set's infimum and supremum. Equality gives exactly the singleton; otherwise the nine pairs of three disjoint boundary types are exhaustive. All six first-order type descriptions, emptiness and singleton descriptions are proved exact without object-language equality. |
| Body 374–386 / annex 525–609 | Any point strictly between the bounds has genuine truth-set members on both sides. The left interpolation uses the exact four-point Lemma 6 hypothesis. The right proof reverses the order, occurrence word, realizing sequence and existential guard explicitly. The fixed remote endpoint is retained. |
| Body 388–475 / annex 611–762 | The eleven guarded branches cover the original open interval by the two exterior pieces, each applicable boundary point and the middle piece. Only unattained interior bounds need a D test. Interpolation justifies D OR P only between actual brackets. Every case is checked and the full disjunction uses Com solely for exhaustion. The six-point countermodel has the stated truth values. |

### Independent source-error findings and the corrections actually supplied

K8-Q is confirmed. Printed 84 visibly supplies a tautology as replacement
for a newly added disjunct. On the supplied three-point order, all original
pattern letters are false, so the original universal condition fails at
the middle point. The tautology replacement makes it true. The new
falsehood replacement and its substitution argument therefore correct an
actual source error. This finding was checked before reading the intake's
assessment.

K8-BRACKET is confirmed. The complete printed chi_6 formula on page 88 has
a first fixed-start witness, D below it, and D OR an unrestricted past
closure above it. The page 89 text claims the unconditional implication
from each chi_i back to the target. In the supplied six-point structure,
phi(0,1) holds, phi(0,4) fails because its open gap contains the B-false
point 2, and phi(3,4) holds across an empty gap. Q is false only at 4.
Thus chi_6 is true with first witness 1 while the target is false at 4.
The predicates are distinct and each occurs once in the input family,
so the source's fresh-occurrence reduction does not exclude this example.
The order is finite and complete. The source implication is therefore
false even in its intended order class. The corrected singleton branch
fails as required, and the purported cofinal case 6 is unavailable because
the actual supremum is 1, not 5.

The source's printed page 85 endpoint substitutions also visibly replace
the fixed x inside the pattern in several gamma formulas. The new Gamma
conditions are explicitly corrected descriptors keeping that endpoint
fixed; the report does not certify literal equivalence between them and
every printed gamma spelling. Their source case numbering tracks the
eleven intended boundary configurations, and their own exact equivalence
proofs justify the new decomposition. No further source case is silently
accepted from an omitted-case assertion.

The new fixed-terminal accumulation result is distinguished from the
source's remote-initial-endpoint beta_1 claim. The latter and the interior
descriptor representations are still required by the remaining induction.
Nothing in the seven passing supporting results converts a first-order
descriptor into an elementary interval representation merely by naming it.

### Boundaries

This verdict does not claim completion of P17-D5, the remaining social-choice
problems, the whole book, canonical notation, drivers, publication output,
formal admission or user acceptance. No manuscript build, manuscript render,
test or shared-file change was made by this reviewer. Only this report is
owned and edited. The remaining Kamp obligation is the complete elementary
representation and smaller-family induction for suitable corrected branches,
in both orientations, before the full Lemma 8 can be marked proved. This
review accepts the closed foundation only.

## Addendum: two changed passages and navigation, 8 September 2026

This separately assigned addendum began at 08:00 UTC and was completed at
08:04 UTC, within its ten-minute bound. The unchanged proofs were not
reopened. No other current reviewer report was read. The earlier source-page
reading remains the authority for this comparison; no new source or manuscript
PDF was generated or inspected.

### Retrieved Content

Current `handbook/annex/p17/single-peaked-majority.tex`, lines 328–338:

```tex
This parity failure also occurs on the source's whole interval.
For a specified \(p\in[0,1]\), define the real distance function
\[
 d_p(t)=\max\{t-p,p-t\}\qquad(t\in[0,1]).
\]
Order alternatives by smaller \(d_p(t)\), and when two distances agree,
prefer the larger value of \(t\). Formally, \(s\) is above \(t\) when
\[
 d_p(s)<d_p(t)\quad\hbox{or}\quad
       (d_p(s)=d_p(t)\ \hbox{and}\ s>t).
\]
```

Current `handbook/parts/p17/social-choice.tex`, lines 312–323:

```tex
\begin{proofboundary}{def:p17-social-choice-next}{Further collective-choice regimes}
All results asserted in this chapter have full annex proofs.
Chapter~\ref{sec:p17-single-peaked-majority} supplies the single-peaked
domain, full majority-order and median-winner results, including the
source's Problem~2. Further required treatments include other preference
domains, aggregation and voting methods, strategic misreporting and
the precise domain/range assumptions of social-choice impossibility
theorems. Arrow's theorem here concerns social rankings and IIA; it does
not by itself prove a theorem about strategic manipulation of a function
selecting one alternative. The source's other related-results discussion
and Problems 3--5 require their own statements and constructions.
\end{proofboundary}
```

### Supplementary Notes

**PASS for both changed passages and the 23 new navigation entries.**
The median source/text acceptance extends to the revised annex below.
The Kamp supporting-results acceptance is unchanged and still excludes
completion of the full Lemma 8 induction.

The two full `git diff --no-index` comparisons were read against the exact
saved predecessors in
`tmp/edition-2026-bounded-kamp4-probability-decision/kamp8-median/before/`.
Each comparison has one changed passage, with no further text differences.
The complete affected median counterexample context was reread, including
the four-voter computation, strictness and transitivity argument, same-side
formulas, and interval realization. The complete changed predecessor boundary
was reread against its previously accepted chapter context. The updated
median intake's root correction addendum was read as a change map.

| Passage | Saved predecessor SHA-256 | Current SHA-256 |
| --- | --- | --- |
| Median annex, 404 to 408 lines | `1AA78E18617B8DE56578E7DA915F5A02F276FEA09737A21811EB21705E3AC3E0` | `5DDA4E25ADEF9987B45CE7050836D5BB2BEC11D9A55959FBDE460B8CEDE25E89` |
| Social-choice body, 321 to 323 lines | `224340F36A0774478ED6CFD8713601190B23F97BE7950106DD4CD8F8B71E64FA` | `83E82EB6AF1353725E3D48799390AD9F4F3CAFCF566E694514C0D1AC2E5CCDCB` |

All four hashes were independently checked. For real t and p, the new
distance equals p-t on the left and t-p on the right, including equality.
It therefore preserves the old distance comparisons exactly. The descending
distance and descending-coordinate tie-break define the same strict ordering;
the transitivity proof and all three comparisons witnessing the interval
parity failure remain valid. The source's strict-input domain is preserved.
The added same-side formulas explicitly justify strict movement toward p.
The predecessor link accurately records the completed Problem 2 treatment
and retains the separate Problems 3–5 and strategic obligations.

All 23 new physical CSV rows 1191–1213 were read completely. All 23
corresponding entries were read completely in each candidate generated view:
the table entries occupy lines 1012–1024 and 1420–1429; the index entries
were located by each exact registry ID. Each view contains exactly one
entry for every ID from 01191 through 01213. The registry has 1,212 data rows.
Verified snapshot identities are:

| Artifact | SHA-256 |
| --- | --- |
| `handbook/registry/symbols.csv` | `264699412B6D3461A2B807DCAF41FD67772ADC8AC305D2AE2D88C70208DC27DD` |
| Candidate `symbols-tables.tex` | `7034EFF5131773D0F16B53DD4A3549D44E112B827022AC41F696719888EC895E` |
| Candidate `symbol-index.tex` | `650729321E98C9D535AC40DF9CF2FDE88AC249D3426B457D64A4E957AC71B1D4` |

The thirteen P9.4 rows preserve the reviewed family lengths and exact rank,
whole-At freshening, falsehood removal, one empty cut tuple, separate fixed-side
conjuncts, fixed-endpoint limits, actual truth-set bounds, guarded interpolation
and corrected branch conditions. Their notes do not grant property I to a
descriptor or imply that the full induction is finished. Both generated views
retain those qualifications and point to the matching table IDs.

The ten P17.6 rows preserve the common axis, strict individual domain,
source peak alias, electorate parity, vote conventions, restricted-domain IIA,
sorted peak multiplicities, finite procedure, Condorcet winner role and the
newly defined d_p. The distance remains a construction for one counterexample,
not a new hypothesis of the source theorem. The views preserve the distinction
between odd transitivity and even weak-winner conclusions. No source-meaning
change or omitted qualification was found in these entries.

The actual main driver reaches the P9 and P17 body and annex drivers.
P9 reaches `logic-in-computer-science.tex`, whose fourth numbered section is
Temporal logic and automata and whose line 950 inputs `n-c-012.tex`.
That presentation inputs Lemma 8 at line 156 immediately after Lemma 7;
the P9 annex inputs its matching proof at line 14 immediately after Lemma 7.
Thus the declared P9.4 placement matches the existing section convention.
The P17 driver has six chapter inputs; single-peaked-majority is sixth,
immediately after social-choice, with the same order in the annex. P17.6
therefore matches the actual new chapter route. Verified route hashes:

| Route | SHA-256 |
| --- | --- |
| `handbook/parts/p09/presentations/n-c-012.tex` | `BD1314D94F1C93B06E56FB173723068E7A4F004825AE9CA13AFD843A12354CBC` |
| `handbook/annex/p09.tex` | `24D9CD8BEF216C974AF5AE66C8127A64023D0A79F9BD8520C78FF582B9F81108` |
| `handbook/parts/p17.tex` | `50D19DD085E5AB253BFFBAEDBF26BAAE6118AB3E8F88C0E1B8DB000E665E4642` |
| `handbook/annex/p17.tex` | `0EE64A3F34A8501CF845D2971EF16AA8E7DBEAADA114ECC10CDDED9F58604380` |

The addendum changes only this report. It supplies bounded source/text and
navigation acceptance, without a build, manuscript rendering, full registry
audit, test, formal admission or publication claim.
