# Kamp Lemma 8 foundations and single-peaked majority: publication-text review

Date: 8 September 2026. Reviewer: `/root/kamp8_foundation_median_publication_review`.
Review began at 07:34 UTC; the bounded return deadline is 08:19 UTC.
This is a fresh independent publication-text review. No other current reviewer
report or conclusion was read. Only this report is owned by the reviewer.

## Final verdict

The four frozen LaTeX targets and all fourteen promised proofs have been read
completely. Final publication-text verdict: **PASS for both bounded
components** at the final identities recorded below. Their mathematical
statements, examples, source attribution, declared scope, integration and new
notation pass this reading. The sole finding, P17-N1, was corrected and
rechecked in the actual annex and both generated symbol views. No unresolved
publication-text finding remains in this assigned scope. No manuscript build,
render, test or admission was performed.

The Kamp component consists of seven completed supporting results. Its full
Lemma 8 elementary-representation induction remains open. Passing these
supporting results cannot close that induction or N-c-012. The median chapter
supplies its declared source exercise and seven stated deductions; it does
not close all of P17-D5 or the remaining social-choice problems.

## Frozen targets and governing instructions

The complete governing amendment and conventions were read directly:

- `spec/EDITION-2026-CONTRACT.md`: SHA256 `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3`.
- `handbook/CONVENTIONS.md`: SHA256 `4293F514072179A5AC95E64FA8D8F37E23FFE2693814A1980E5801BABA5B7242`.

| Target | Complete extent read | Initial SHA256 |
| --- | --- | --- |
| `handbook/parts/p09/presentations/kamp-iii2-lemma8.tex` | 493 lines; 20,892 bytes | `ECC3896B4F0C25C58914FFBB9D03A49447D89F5146FF8949EF2CF9B34AD6F61E` |
| `handbook/annex/p09/kamp-iii2-lemma8.tex` | 762 lines; 36,037 bytes | `8740AE1FCC283B7313511073AD8D05B167FD92C1E207C37A984D53D00870BF8F` |
| `handbook/parts/p17/single-peaked-majority.tex` | 309 lines; 15,554 bytes | `BA7EF43E3E28026890EE178439A32CF13614D6E430CF916350FEFC479D423063` |
| `handbook/annex/p17/single-peaked-majority.tex` | 404 lines; 21,295 bytes | `1AA78E18617B8DE56578E7DA915F5A02F276FEA09737A21811EB21705E3AC3E0` |

The complete author intakes were read as claims to check, not as independent
acceptance: `edition-2026-c7-kamp-iii2-lemma8.md` at
`1F4F79991AB23E61A20ACC5FAA9D2925ED29E85E056DBCFFA462C8FE7ECE59FC`, and
`edition-2026-p17-single-peaked-majority.md` at
`6FEE2C27D11C89679F1294151D1E5A2417B1A1112C4D98AC682DF78D0B840128`.

## Actual prerequisite and primary reading

The prerequisite interfaces were read in their actual LaTeX. For Kamp these
were the Lin/Com and language declarations in `n-c-012.tex`, the literal At
grammar in `kamp-iii1-normal-form.tex`, the strict limiting operators and
Lp/Lf definitions in Lemma 2, proper substitution and the finite E grammar
in Lemma 3, elementary labelled words, guarded realization, property I and
its substitution closure in Lemma 4, the Lemma 6 fixed-start statement, and
the complete Lemma 7 body including all cut words and both reductions.
The complete Lemma 4 interval-substitution proof was also read.

For the median chapter the actual strict-profile, weak-output, vote-count,
IIA, Pareto, dictatorship and Arrow statement interfaces were read in
`social-choice.tex`, together with the weak/strict/indifference conventions
in `finite-preferences.tex`. Infinite alternatives in the new result do
not inherit the older finite chapter's finiteness hypothesis; the social
chapter explicitly supplies the infinite-set extension of that interface.

The two existing bibliography records were read. The held primary hashes
were checked live:

- Kamp, *Tense Logic and the Theory of Linear Order* (1968),
  `tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf`,
  `C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA`.
- Rubinstein, *Lecture Notes in Microeconomic Theory*, second edition,
  author revision of 11 January 2015,
  `source/references/rubinstein-microeconomic-theory-2015/rubinstein-second-edition-revision-2015-01-11.pdf`,
  `F7CEA2C4F48C77D93DD25C30BBDA83E051C6562A589256AAC8CBA1B5084A33F8`.

Every complete Kamp source page 83 through 92 was independently read from
the retained source images, including the detailed images of pages 84 and
88. Rubinstein's complete printed pages 123 and 128 were read from source
images, and physical pages 1 through 3 were extracted and read to verify
the revision and edition. These are primary-source readings, not manuscript
layout inspections. The PDF skill guided this read-only source work; its
authoring marker was not applicable.

Kamp page 84 prints the tautology substitution for the fresh disjunct;
the manuscript directly uses falsehood and proves the necessary recovery.
Page 88 prints the weakened chi_6 shape tested by the six-point example;
page 89 claims its unconditional implication to the target. The supplied
counterexample refutes exactly that implication even on a complete finite
order. The new Gamma descriptors retain the original endpoints and are
identified as the corrected construction. Source pages 89 through 92
continue to the elementary-representation argument, whose unfinished
portion is accurately retained in the manuscript's final proof boundary.

Rubinstein page 123 supplies strict individual orderings and weak social
outputs. Problem 2 on page 128 uses the whole interval [0,1], the displayed
same-side peak condition and odd positive electorate size. Problem 1's
different weak-individual convention does not migrate to Problem 2.
The source poses an exercise, and the new chapter explicitly attributes
the full proofs, ordered-set extension and refinements to the handbook.

## All fourteen reciprocal proof promises

Each row below was checked against its entire body statement and annex
proof, not just its label or a scanner result.

| Kamp suffix, after `thm:p09-kamp-` | Evidence and result |
| --- | --- |
| `family-rank` | Body 58; annex 6. Exact source comparison is equivalent to lexicographic maximum/count decrease, including empty families. Maximal deletion and all permitted replacement unions decrease it; coincident outputs cannot increase counts. PASS. |
| `family-cut` | Body 121; annex 72. Every tuple of subsets is included. Both quantified orientations retain every fixed-side conjunct, arbitrary auxiliary formulas and unchanged free parameters. Fixed truth subsets precede universal variation. The residual-family rank application states its additional At/Bp and once-per-member hypotheses. PASS. |
| `family-normalization` | Body 168; annex 178. The empty and atomic base use an actual one-interval elementary word. Whole-At replacement preserves its grammar, fresh basic occurrences preserve lengths, and successive proper substitutions recover the original family. The added fresh disjunct is eliminated by falsehood. PASS. |
| `fixed-endpoint-limits` | Body 226; annex 275. Both directions of both endpoint constructions are supplied. The n=1 unary strict limit and n>1 whole suffix/prefix are distinct. Actual witnesses and the two-interval words give guarded Lin equivalences without density or completeness. PASS. |
| `eleven-boundaries` | Body 347; annex 388. Empty, singleton and all nine distinct-boundary pairs exhaust the Com case. Every lower/upper type has its exact first-order condition; attained and unattained boundary points are treated separately. The rational-cut example correctly limits exhaustion on Lin. PASS. |
| `hull-interpolation` | Body 374; annex 525. Existing infimum/supremum supply truth-set members strictly on either side. The left orientation invokes precisely Lemma 6's four points; the right orientation explicitly reverses word, order, realization and guarded closure. PASS. |
| `corrected-boundary-decomposition` | Body 443; annex 611. All eleven branches retain descriptors and original endpoint bindings. The proof checks both side intervals, the middle interval and every attained/unattained endpoint test, and verifies the finite counterexample. No elementary membership is inferred merely from being first order. PASS. |

| Median suffix, after `thm:p17-` | Evidence and result |
| --- | --- |
| `single-peaked-structure` | Body 57; annex 11. Unique greatest peak, all four allowable triple rankings, no-valley converse and finite greatest-element argument are supplied. The infinite-set greatest-element premise is retained. PASS. |
| `single-peaked-majority` | Body 103; annex 53. Odd pair counts remove ties, two voter-set inclusions exclude both possible three-cycle orientations, and failure of full transitivity would produce a three-cycle. Weak transitivity is checked separately. This proves the entire social relation on the whole interval. PASS. |
| `median-peak-winner` | Body 135; annex 107. Both majority coalitions give the unique strict and weak winner, then single-peakedness of the already proved social ordering. Repeated peaks, endpoints, one voter and singleton alternatives are covered. PASS. |
| `even-median-interval` | Body 152; annex 152. Every point between the central peaks is weakly unbeaten, and every outside point loses strictly to a central peak. Coincidence yields a strict winner; distinct central peaks preclude one. No even weak-transitivity assertion is made. PASS. |
| `single-peaked-algorithm` | Body 236; annex 188. Permutation validation, adjacent-comparison necessity/sufficiency, concrete failure witnesses, histogram order statistics and victory-count output are proved. Exactly nq(q-1)/2 rank comparisons supplies the matrix; the O(nq), O(n+q) and O(nq^2) bounds specify their finite random-access model. PASS. |
| `single-peaked-boundaries` | Body 254; annex 265. All ten unordered pair counts match the five-voter input. The majority ranking differs from the median voter's ranking on a/e. The three-voter cycle and four-voter nontransitive social ties have the stated counts. The full-interval realization uses strict individual tie-breaking. PASS after the notation correction below. |
| `single-peaked-arrow` | Body 282; initial annex 354. Pareto, anonymity and restricted-domain IIA are established directly. An admissible profile refutes each candidate dictator. A concrete strict interval ordering witnesses a proper domain restriction, so the unrestricted Arrow premise is absent. PASS. |

The remaining boundaries in Kamp body 478 and median body 298 are accurate:
the full I induction, weak individual ties, finding an axis, other domains
and strategy claims remain separate obligations. No empirical conclusion
or mechanism truthfulness theorem is asserted by these formal results.

## Finding and integration check

P17-N1, notation: the initial median annex at lines 330 through 345 uses
paired bars for real absolute distance in the handbook-added interval
counterexample. The conventions' cardinality ruling applies here; this is
not syntax quoted from the source exercise. The mathematics is correct,
but the additional role needs correction. Requested repair: define the
same real distance explicitly, for example `d_p(t)=max(t-p,p-t)`, and use
that typed symbol in the comparison and its proof, with matching canonical
notation. This affects the displayed counterexample notation only.

Text repair checked: the annex now defines `d_p(t)=max{t-p,p-t}` before use,
uses it throughout the distance/tie-break ordering, and explicitly proves
`d_p(t)=p-t` on the left of the peak and `d_p(t)=t-p` on the right. The entire
changed passage was read. The strict-order argument, same-side monotonicity
and all three interval vote comparisons remain valid. P17-N1 is closed in
the manuscript text. The revised annex has 408 lines, 21,482 bytes, and
SHA256 `5DDA4E25ADEF9987B45CE7050836D5BB2BEC11D9A55959FBDE460B8CEDE25E89`.
The exact saved predecessor at
`tmp/edition-2026-bounded-kamp4-probability-decision/kamp8-median/before/median-annex.tex`
was hash-checked against the initial annex identity in the table. A complete
file comparison shows only this distance-definition and replacement passage
changed; all other proof text is preserved.

## Final integration and notation snapshot

The root supplied the final candidate snapshot, and each following identity
was verified live. The Kamp pair and median body retain their initial hashes
in the first table. The median annex is the corrected `5DDA4E25...` version
described above.

| Artifact | Final SHA256 |
| --- | --- |
| `handbook/parts/p09/presentations/n-c-012.tex` | `BD1314D94F1C93B06E56FB173723068E7A4F004825AE9CA13AFD843A12354CBC` |
| `handbook/annex/p09.tex` | `24D9CD8BEF216C974AF5AE66C8127A64023D0A79F9BD8520C78FF582B9F81108` |
| `handbook/parts/p17.tex` | `50D19DD085E5AB253BFFBAEDBF26BAAE6118AB3E8F88C0E1B8DB000E665E4642` |
| `handbook/annex/p17.tex` | `0EE64A3F34A8501CF845D2971EF16AA8E7DBEAADA114ECC10CDDED9F58604380` |
| `handbook/parts/p17/social-choice.tex` | `83E82EB6AF1353725E3D48799390AD9F4F3CAFCF566E694514C0D1AC2E5CCDCB` |
| `handbook/registry/symbols.csv` | `264699412B6D3461A2B807DCAF41FD67772ADC8AC305D2AE2D88C70208DC27DD` |
| Candidate `symbols-tables.tex` | `7034EFF5131773D0F16B53DD4A3549D44E112B827022AC41F696719888EC895E` |
| Candidate `symbol-index.tex` | `650729321E98C9D535AC40DF9CF2FDE88AC249D3426B457D64A4E957AC71B1D4` |
| `handbook/bib/handbook.bib` | `46C6D1BEA7541A50E028422CC5BA0C305B3EAE7C64C57B803B611E49DE2A8F63` |

Both candidate generated files are in
`tmp/edition-2026-bounded-kamp4-probability-decision/kamp8-median/`.
They are candidate lookup views, not publication or admission artifacts.

The actual P9 body route at line 156 and annex route at line 14 place the
foundation immediately after Lemma 7. The actual P17 body route at line 9
and annex route at line 8 place the median chapter immediately after social
choice. The complete short drivers and the relevant P9 body route region
were read. Each new body/annex pair is routed once in its corresponding
driver. P9.4 and P17.6 are the appropriate local scopes.

The entire changed social-choice boundary was read, and a complete file
comparison against `before/social-body.tex` was inspected. That saved
predecessor has SHA256
`224340F36A0774478ED6CFD8713601190B23F97BE7950106DD4CD8F8B71E64FA`.
Only the final boundary changed: it now points to the completed single-peaked
Problem 2 and retains other preference domains, voting methods, strategy
questions and Problems 3 through 5 as owed. The new pointer is accurate;
all earlier theorem statements and proof dependencies are preserved.

The canonical registry has 1,212 data rows. Every cell of the 23 new rows at
physical lines 1191 through 1213 was read against the actual manuscript.
Every corresponding complete row in both actual generated views was then
read, including the table labels and index hyperlinks `01191` through
`01213`. All 23 identities, glyph families, roles, scopes, first-use values
and substantive notes agree across these surfaces.

The thirteen Kamp rows retain the finite-family grammar and counts, all
cut-choice orientations, adjacent-endpoint rather than remote-endpoint
limits, the original endpoint parameters in the truth set and remaining
disjunction, the three boundary types, all guarded branches, and the
explicit order reversal. No entry promotes boundary decomposition to the
unfinished elementary-representation conclusion.

The ten median rows retain the common axis, strict individual domain,
source peak alias, exact odd/even ranges, possible even social ties,
restricted-domain welfare map, repeated peak positions, finite rank-array
representation and candidate-winner role. The final distance row uses
`d_p(t)` and its explicit maximum definition in both generated views. Its
note correctly confines distance-based preferences to the interval
counterexample. P17-N1 is therefore closed in both text and notation.

Final review completed at 07:58 UTC, before the 30-minute checkpoint and
the 08:19 deadline. The full readings and final changed-passage rechecks
support the bounded PASS. Production, separate formal admission, full Kamp
Lemma 8 and the remaining edition obligations retain their own requirements.
