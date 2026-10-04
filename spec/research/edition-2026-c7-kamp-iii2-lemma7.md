# Edition 2026 C7: Kamp III.2, Lemma 7

Date: 7 September 2026 Pacific time / 8 September UTC.
Author: /root/kamp_lemma7_author. Repository: C:\Dev\the-methods-of-reason.
Assignment: C7 / N-c-012, complete the two orientations of Lemma 7.
Standing: completed author construction, awaiting independent review and integration.
Dispatch/start: approximately 06:13 UTC; 45-minute deadline 06:58 UTC.

## Frozen authored content

| Owned artifact | Extent | SHA256 |
| --- | --- | --- |
| handbook/parts/p09/presentations/kamp-iii2-lemma7.tex | 278 lines; 12,652 bytes | 3411BB4A552755CAFEF4675851A764A8605CBE36D402C6CFE022E397DE9F9778 |
| handbook/annex/p09/kamp-iii2-lemma7.tex | 489 lines; 23,301 bytes | 3E71146A7142A8A2BA26983A6A23634D9E7D3B52AA8A5F4FD2C9CC8793BD817F |

The body supplies the full finite cut construction, both quantified
equivalences, the exact original length restriction, all subset alternatives,
a worked two-interval example requiring different cuts at different universal
witnesses, and the empty/substage-one boundaries. The annex supplies every
point-cut and gap-cut direction, both full quantified proofs, their truth
patterns and removal of negative conjuncts, the exact length calculations,
and the worked examples. No component of the selected corrected aggregate
construction is left as a sketch or a future proof obligation.

The second source statement needs the explicit output-class correction below.
The manuscript gives a correct active statement and full proof, and identifies
it as the handbook's corrected aggregate formulation. It does not claim to
prove the false individual-Bp output assertion as printed.

Only these two new manuscript files and this note were edited. Root owns
routes, registry, bibliography, generated navigation and formal records.

## Exact primary source and reading extent

J. A. W. Kamp, *Tense Logic and the Theory of Linear Order*, UCLA dissertation,
1968. Existing bibliography key: Kamp1968.
Held source: tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf, 128 pages.
[Institutional locator](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf).
Verified SHA256: C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA.
Printed page n is physical PDF page n + 9, counted from one.

The complete selected extent was frozen before authoring: Lemma 7 starts on
printed p. 80, its two-part statement continues on p. 81, and its proof ends
on p. 83 immediately before Lemma 8. All four complete pages were personally
read, first through held complete page images and then through newly rendered
240-dpi complete pages of the verified source. The 7(a) class line was also
inspected as a 400-dpi source crop; the 7(b) endpoint and output-class line
was reread at original resolution. The endpoint in 7(b) is v, not y; no
endpoint-glyph error is claimed.

| Printed / physical extent | Personally read content |
| --- | --- |
| 63-66 / 72-75 | Complete pages: basic grammar, occurrence sequence S, point-occurrence subsequence Se, realization semantics, same-word and ordered-endpoint remarks. Repetitions are explicitly permitted by the occurrence definition and its example. |
| 80 / 89 | Complete page: end of Lemma 6 and opening of Lemma 7(a), including all four variable names, arbitrary psi_1 and psi_2, the left universal interval and finite output aggregates. |
| 81 / 90 | Complete page: both length restrictions, complete right-interior statement, start of proof, prefix/suffix split and point-occurrence test Z(i). |
| 82 / 91 | Complete page: both starred-word operations, every Boolean truth assignment, complete truth patterns, positive conjunctions, residual disjunctions and initial equivalence. |
| 83 / 92 | Complete page: distribution, forward implication to (23), reverse implication for every disjunct, explicit end of Lemma 7, next lemma and its source length convention. |
| 84 / 93 | Complete page inspected only for the next boundary; no Lemma 8 construction is claimed. |

The new complete source-page images are retained under
C:\Users\Crow\Documents\Codex\2026-08-10\phase-4-handover-migration-campaign-written\tmp\pdfs\kamp-lemma7-source\,
as source-089.png through source-092.png. The detail is class-detail-089.png.
Earlier prerequisite page images are in the held kamp-lemma4-source directory.
These are primary-source inspection aids, not rendered manuscript evidence.

## Source construction, completed details and correction provenance

There are n gap cuts and n-1 interior-point cuts, a total of 2n-1. The
construction lists all subsets, hence 2^(2n-1) indexed alternatives. In the
source's enumeration from zero this can be indexed 0 through p with
p = 2^(2n-1) - 1. No cut is lost and no choice of one cut is moved outside
the universal quantifier. A subset records fixed-side truths; its residual
disjunction allows different cuts at different values of the varying endpoint.

For a point cut at A_k, the source prefix ends immediately before that
occurrence, and its suffix begins there. Appending A_k to the prefix and
retaining the suffix yields the two words in the manuscript. For a gap cut
at B_k, append B_k twice to the prefix and prepend B_k to the suffix.
This is exactly the displayed R_i^*, S_i^* operation. The occurrence-based
definition of Se on p. 64 determines the point/gap case, including when a
letter is repeated in both roles.

The permitted cuts have nonempty prefix and suffix of at least two
occurrences. This makes both starred words genuine positive-stage basic
patterns. An empty prefix would represent the original initial endpoint,
not a strict interior cut; a one-occurrence suffix would represent the
original final endpoint. Both are excluded by the actual strict cut guard.
The manuscript spells out these ranges directly rather than relying on an
implicit convention about the word "sequence."

The source uses sigma_i and rho_i after forming the starred words without
separately displaying their word-to-formula assignments. The manuscript
defines L_c and R_c by the existing Bp recursion, proves their factorization
through every realization, and uses the correct side at each orientation:
left case sigma_i = R_c(u,y), rho_i = L_c(v,u); right case fixed-side
L_c(x,u), residual R_c(u,v). Its complete truth patterns Omega_alpha and
tilde-Omega_alpha implement the source's sigma'_alpha step. Their positive
parts and selected residuals are Sigma_J and rho_J. Negative truth tests
are dropped only in the complete existential/disjunctive construction,
with an independent converse, never as isolated equivalent formulas.

**Confirmed printed output-class defect in 7(b), p. 81.** The statement
calls each sigma_i an individual member of Bp(x,u) and each rho_i an
individual member of Bp(u,v), even though it refers the proof to the
aggregate construction of 7(a) and reuses the residual-disjunct condition.
The individual-Bp requirement for sigma_i makes the statement false.
Interpret every unary predicate by the empty set on 0 < 1 < 2 < 3, take
psi_1 = T^K_u and psi_2 = T^K_v, and evaluate x = 0, y = 3. The original
right-interior formula is true with u = 1; its tested interval contains 2
and psi_2 is true there. Every basic past pattern is false at every
endpoint pair because its initial unary atom is false. Thus every proposed
output disjunct with an individual Bp(x,u) conjunct is false, whatever the
finite list and whatever extra predicate letters it uses. This refutes the
printed target itself, not merely a particular proposed construction.

The active correction states finite conjunctions and disjunctions in 7(b),
with the empty conjunction true and empty disjunction false, exactly as the
two-sided cut construction requires. Both original quantified formulas,
the arbitrary psi inputs, Lin scope, and the at-most-one equal-length and
no-longer residual restrictions are retained. The empty alternative handles
the countermodel. No stronger individual-Bp assertion is left active or
reported proved. Independent reviewers should check both the source reading
and this countermodel before accepting the correction.

The residual bound is not enlarged: point cuts have lengths 2k+1 and
2(n-k)+1, both shorter than 2n+1; gap cuts have lengths 2k+1 and
2(n-k+1)+1. The unique full-length left candidate is the last gap and
the unique full-length right candidate is the first gap. A subset includes
each at most once, even if shorter cuts happen to yield equivalent formulas.

## Dependencies and author verification

The complete actual LaTeX bodies of Lemmas 1-6 were read. The actual
Lemma 1 annex was read through line 133, covering the full word/realization
induction and guarded closure semantics. The complete Lemma 6 annex was
read. Lemmas 2-6 supply chronological context and notation; their substantive
results are not mathematical premises of the cut proof. The mathematical
prerequisite is the already proved basic-word realization equivalence.

Verified unchanged dependencies:

- Lemma 1 body: 3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6.
- Lemma 1 annex: 631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1.
- Lemma 4 body, for the existing word recursion: 1821FB12C4E77B1D531A3BB154581451A972745BAFFAE1FF0611E34152CF13EB.
- Lemma 6 body: EBB6DEAE8B3C2538DDB8CF5AB9CF24C7C52AA0EB6202585A7E7B33B188AE99DB.
- Lemma 6 annex: 9EA42EBBDFFE6A6A9071C581E2F10721CF2D2504B96EC1CE51FE15658469D171.

The governing contract and complete conventions were read; their hashes were
C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3 and
4293F514072179A5AC95E64FA8D8F37E23FFE2693814A1980E5801BABA5B7242.
The execution-plan C7, ownership, timebox and source/content gates were read.
The complete research and PDF skills were personally read. This agent is
the parent's delegated researcher; the assignment prohibited further agents.
The PDF skill guided source scan reading only. No PDF was authored, so its
PDF-authoring marker was inapplicable.

Both authored files were read back completely; final wording changes were
reread. The existing tools/check.py scanner was used on these two files only:
zero findings; three reciprocal result/proof pairs; 13 declared labels;
all citation keys present in the existing bibliography. The five distinct
reference targets were checked against their actual declarations. The
scanner hash was 05F22DEE54E3F177EAD79DFAE16D88787E513A58441F443278679F8BC7443914.
The bibliography remained BD462E1E3BC9B6E6C1AA40B30E4E7C23A6B4533FA196EDD43B881F8C7757FA59,
and the frozen original remained 0509750C13B88A4E18914BD52BDE171C725CBA14221CBFC2227D7693A2B421CC.
The two-interval example and the all-false countermodel were checked directly
in the written proof. No new software test, manuscript build, manuscript
render, generator change, commit or admission action was performed.

## Root intake and next boundary

Input the new body after Lemma 6 in handbook/parts/p09/presentations/n-c-012.tex,
and its matching annex after Lemma 6 in handbook/annex/p09.tex. Kamp1968 already
supplies all bibliography references. The exact reciprocal pairs are:

| Body result | Annex proof |
| --- | --- |
| thm:p09-kamp-cut-factorization | annex:p9.kamp.cut.factorization |
| thm:p09-kamp-iii2-lemma7-left | annex:p9.kamp.iii2.lemma7.left |
| thm:p09-kamp-iii2-lemma7-right | annex:p9.kamp.iii2.lemma7.right |

Suggested local P9.4 symbol roles: ell(W), ell(phi) for occurrence length;
C_n, the p/g tags and c for the ordered cut index set; W_c^L/W_c^R and
L_c/R_c for cut words and their basic formulas; J and alpha for subsets
and their truth assignments; Sigma_J^L/Sigma_J^R and rho_J^L/rho_J^R for
fixed-side conjunctions and varying-side disjunctions; Omega_alpha and
tilde-Omega_alpha for complete truth-pattern formulas in the proof.
The scalar points a,d,b, sequence entries a_i,l_i,r_i and tested point z
retain the local realization-proof roles stated before use.

The next exact source result is Lemma 8, beginning printed p. 83 / physical
p. 92. It treats a finite family from At(z), Bp(x,z), Bp(z,y), its length
comparison, and the universal interior formula with property I(x,y).
Its full continuation, later lemmas and Theorem III.2 remain separate work.
This new Lemma 7 unit needs fresh independent source, topic and publication
reviews, root integration, relevant static/build/visual evidence, and its
separate formal admission. Author completion grants none of those gates.
