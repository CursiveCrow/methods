REVISE

# Round-three blind source-fidelity review: N-c-012.d

## Seat, runtime, and independence

- Stable agent identifier: `/root/schmidt_smolka_1991_research/gpss_primary_pass`.
- Seat: source fidelity.
- Runtime model/version: the exact deployed runtime model and version were not exposed to this seat.
- Independence: I did not inspect `ledger.md`, `transcript/chair.md`, either earlier-round transcript (including my own), or another reviewer's transcript or verdict. I did not contact another reviewer. Earlier verdicts were not used as authority.
- Method: direct visual reading of the two complete frozen facsimiles and three controlling journal derivatives, followed by line-by-line inspection of the frozen reader, shared integration, bibliography, source note, and source-presentation entry. I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or builds.

## Frozen round-three identity verification

All ten identities matched the charter before substantive review, again immediately before filing, and again unchanged immediately after filing:

| Frozen object | Verified SHA-256 | Disposition |
|---|---|---|
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf` | `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5` | MATCH |
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf` | `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283` | MATCH |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png` | `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114` | MATCH |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png` | `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1` | MATCH |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-04-acceptable-crop.png` | `C267D4B4DF785F9A7E82123B068662E45D7E2C87CB18C24D7B8EB0B875AF413B` | MATCH |
| `handbook/parts/p09/presentations/n-c-012.tex` | `1F5792A97766A695A58EF5FAA259F97D8CD6E50B720FB14BEDEA358E3505E7F8` | MATCH |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` | MATCH |
| `handbook/bib/handbook.bib` | `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B` | MATCH |
| `spec/research/p09-sistla-clarke-1985-source-note.md` | `3C1F2DEB6D3224D61E1008B59DF353F56BE096A951E936B0060C583497E37565` | MATCH |
| `spec/research/p09-source-presentations-lot2-3.md` | `414CFAEF19DB8F53B76E6A4805EA20F3D2DABFCA245FC0DD6F537FE32F8253DE` | MATCH |

No identity mismatch affected the review.

## Complete visual authority record

I freshly read every frozen page image at original detail. The PDF/page correspondence was checked through the printed folios; images were used only as page renderings of the controlling PDFs.

### JACM 1985, all seventeen printed pages

- `journal-page-01.png`, printed p. 733: title, Sistla--Clarke author order, affiliations, abstract, introduction, JACM issue/footer, and ACM rights notice.
- `journal-page-02.png`, printed p. 734: introduction completed; notation, fragment notation, primitive formula syntax, and Boolean/`F`/`G` abbreviations.
- `journal-page-03.png`, printed p. 735: `\widetilde L(F,X)`, structures and interpretations, inclusive `X/U/S` clauses, closure bound, total `R`-structures, existential truth problem, and the unique-maximal-suffix `init/final/range/size` definitions.
- `journal-page-04.png`, printed p. 736: Lemmas 3.1--3.3, exact Lemma 3.2 hypotheses, acceptable subsequences, ambient-relative measures, literal strict union inequality, definition of `mu(f)`, literal strict Lemma 3.3 bound, and the atomic basis.
- `journal-page-05.png`, printed p. 737: the non-strict inequalities used throughout the Lemma 3.3 induction, Theorem 3.4's non-strict conclusion and explicit `PROOF SKETCH`, and Theorem 3.5's statement.
- `journal-page-06.png`, printed p. 738: Figure 1 and the 3-SAT reduction; the bounded prefix/strongly connected set/connecting-edge certificate; the subformula-labelling rules on nodes in `p'` or `C`.
- `journal-page-07.png`, printed p. 739: acceptance at the start label, Theorem 3.5 completion, Lemma 3.6, Theorem 3.7, and Theorem 4.1.
- `journal-page-08.png`, printed p. 740: stuttering Lemma 4.2 and the exact `R`-truth-to-satisfiability reduction of Lemma 4.3.
- `journal-page-09.png`, printed p. 741: Figure 2, persistent terminal configurations, the chain of `S(n)` cell diamonds, complete instantaneous-description traversals, and the literal journal sentence using `2S(n)` next operators.
- `journal-page-10.png`, printed p. 742: completion of the pure-`U` sketch, source truth sets, the literal `2^length(f)` count, Lemma 4.5, inclusive fulfilled-before definition, valuation periodicity, and Lemma 4.6.
- `journal-page-11.png`, printed p. 743: Lemma 4.6 completion and Theorem 4.7's exact statement, bounds, every-periodic-position obligation, and `Ff` proof move.
- `journal-page-12.png`, printed p. 744: Theorem 4.7 completion and the on-the-fly proof of Theorem 4.1, including local consistency, initial-since, period, and until-discharge checks.
- `journal-page-13.png`, printed p. 745: Savitch step; ETL grammar and constructor semantics; finite/infinite index conflict; disjoint nonterminals; `N_0 -> a_1 a_2 N_0` parity conflict; normalization; exact closure; `Gamma`; and Lemma 5.1.
- `journal-page-14.png`, printed p. 746: Lemma 5.1 completion, maximum-depth fulfillment, Lemma 5.2, and the beginning of Theorem 5.3 with its exact bounds.
- `journal-page-15.png`, printed p. 747: Theorem 5.3 completion and Theorem 5.4's grammar-as-input, `card(SF(f)) <= 2n`, local grammar consistency, and continuation-nonterminal search.
- `journal-page-16.png`, printed p. 748: Theorem 5.4 completion, Table I, conclusion, unidentified conference-theorem error notice, rights-neutral prose, and the beginning of the references.
- `journal-page-17.png`, printed p. 749: references, the distinct STOC citation, and receipt/revision/acceptance history.

### STOC 1982, all ten printed pages

- `conference-page-01.png`, printed p. 159: title, author order, Harvard affiliation, abstract, introduction, 1982 ACM notice and identifier.
- `conference-page-02.png`, printed p. 160: conference syntax/semantics, satisfiability, and the literal universal validity clause.
- `conference-page-03.png`, printed p. 161: existential `R`-truth, structure measures, conference Theorem 3.1 and Lemmas 3.2--3.3, and the conference acceptable-subsequence presentation.
- `conference-page-04.png`, printed p. 162: conference Lemma 3.4 proof sketch, `2 length(f)` small-model statement/proof tension, and Theorem 3.5.
- `conference-page-05.png`, printed p. 163: Figure 1 and the conference NP certificate/labelling procedure.
- `conference-page-06.png`, printed p. 164: Theorem 4.1, reduction/hardness machinery, halting terminal-state convention, Figure 2, and the literal `S(n)` next-distance sentence.
- `conference-page-07.png`, printed p. 165: conference Lemmas 4.4--4.5, recurring-type set `M_{S,f}`, and conference Theorem 4.6 without the journal's every-position until obligations.
- `conference-page-08.png`, printed p. 166: proof outline, uncorrected regular-operator extension, `n^2` closure estimate, and the same parity sentence.
- `conference-page-09.png`, printed p. 167: conclusion, Figure 3 classification, and bibliography beginning.
- `conference-page-10.png`, printed p. 168: bibliography completion.

### Controlling journal derivatives

- `journal-page-04-acceptable-crop.png`: visually confirms that the preparatory acceptable-union sentence literally prints `<`, that the measures are relative to ambient `S`, and that `mu(f)` is defined immediately thereafter.
- `journal-page-10-bound-crop.png`: visually confirms the faint count as `2^length(f)`, with no additional factor in the exponent.
- `journal-page-13.png`: visually confirms the unrestricted finite/infinite index wording and the even/zero-based-odd parity conflict.

## Complete frozen artifact record

- Reader: `handbook/parts/p09/presentations/n-c-012.tex`, lines 1851--2387, read in full.
- Necessary shared context: `handbook/parts/p09/logic-in-computer-science.tex`, lines 602--708 and 720--809, including both shared theorems and the complete intervening model-checking construction, read in full.
- Bibliography: `handbook/bib/handbook.bib`, lines 2245--2274, both `SistlaClarke1982` and `SistlaClarke1985`, read in full.
- Source note: `spec/research/p09-sistla-clarke-1985-source-note.md`, lines 1--867, read in full.
- Source-presentation entry: `spec/research/p09-source-presentations-lot2-3.md`, lines 185--257, read in full.

## Criterion dispositions

### C1 — PASS

The frozen artifacts preserve the journal's plural title, Sistla--Clarke order, JACM 32(3), July 1985, pp. 733--749, DOI, ISSN, and receipt history; the distinct STOC 1982 venue/date/pages/DOI and file identity; CMU acquisition/file-boundary facts; and the non-republication rights boundary. Source: journal pp. 733, 748--749; conference pp. 159, 167--168. Artifact: reader lines 1853--1881; bibliography lines 2245--2274; source note lines 1--145 and 757--796; source-presentation lines 185--189.

### C2 — PASS

The reader keeps `L(O_1,...,O_k)`, `\widetilde L(F,X)`, the full syntax, inclusive `U/S`, structures, interpretations, existential `R`-truth, satisfiability, program-counterexample use, validity, and the reconstructed journal validity boundary distinct. Source: journal pp. 734--735 and 748; conference p. 160. Artifact: reader lines 1883--1973; source note lines 147--265; source-presentation lines 191--192; shared definition lines 602--623.

### C3 — PASS

The Section 3 reconstruction now gives the unique maximal suffix and exact decomposition before use; defines structure and acceptable-subsequence measures relative to ambient `S`; states Lemmas 3.1--3.3 and Lemma 3.6 with the needed zero-prefix, acceptability, intermediate-supersequence, surviving-position, finite-subsequence, and current-state quantifiers; discloses both strict/non-strict conflicts; states Theorems 3.4--3.7; reconstructs Figure 1; and gives the printed polynomial NP certificate exactly. Source: journal pp. 735--739 and the p. 736 crop. Artifact: reader lines 1975--2149; source note lines 267--457; source-presentation lines 193--241.

### C4 — PASS on mathematical content; see F01 for its citation locator

The stuttering boundary, Lemmas 4.2--4.6, Figure 2 encoding unit, persistent terminal configurations, journal/conference distance distinction, source truth-set definition and count, inclusive fulfillment, exact periodicity, Theorem 4.7 bounds and every-position obligations, `Ff` move, initial-since check, and Savitch step are mathematically source-exact. Source: journal pp. 740--745 and p. 742 exponent crop; conference pp. 164--166. Artifact: reader lines 2151--2267; source note lines 459--595. The one blocking defect is not the value `2S(n)` but the reader's attached journal page locator, recorded as F01.

### C5 — PASS

The ETL reconstruction preserves disjoint nonterminals, the grammar-indexed formula constructor, normalization, represented-position typing reconstruction, the unresolved parity defect, closure, exact `Gamma` continuation edges, separation of terminal productions, finite-tree depth, distinct fulfillment obligations, Theorems 5.3--5.4, grammar input encoding, and continuation-set termination. It does not choose an authorial repair or identify a unique corrected inference. Source: journal pp. 745--748, especially full p. 745; conference pp. 166--167. Artifact: reader lines 2269--2354; source note lines 597--689; source-presentation line 241.

### C6 — PASS

Table I is exact; Theorem 4.1 and the table's `L(U,X)` row remain distinct; the shared theorem derives the row through `L(U) subset L(U,X) subset L(U,S,X)`; and universal model checking is obtained through existential truth of the negation plus deterministic-space complement closure. Source: journal pp. 739, 744--745, 748. Artifact: reader lines 2356--2386; shared lines 693--708 and 761--809.

### C7 — PASS

Conference and journal syntax, validity, small-model, theorem numbering, terminal-machine behavior, next distance, periodic obligations, proof labels, ETL closure/machinery, correction notice, summary display, and references are not interchanged. Direct conference claims resolve to `SistlaClarke1982`; journal claims resolve to `SistlaClarke1985`. Source: complete STOC pp. 159--168 and JACM pp. 733--749. Artifact: reader lines 1853--1881, 1960--1973, 2164--2181, 2349--2354; source note lines 757--796; bibliography lines 2245--2274.

### C8 — REVISE

The bibliography, page map, proof-status table, source-presentation entry, acquisition record, and rights boundary are otherwise consistent, but the reader's direct journal locator for the `2S(n)` sentence is wrong by one printed page. The sentence is on printed p. 741, while reader line 2175 cites p. 742. See F01.

### C9 — PASS apart from the C8 locator defect

The prose defines before use and supplies the required standing/distinction/use material for acceptable subsequences, ambient-subscript notation, source truth sets, fulfilled-before obligations, the ETL constructor, and `Gamma`. No unsupported automata proof, finite-model claim, unlabelled validity attribution, or unprinted ETL repair was found. Artifact: reader lines 1896--1903, 2019--2050, 2068--2071, 2192--2214, 2271--2326, and 2328--2354.

## Invariant dispositions

- I1 — PASS. Scholarship-only review; no tests, scripts, TeX, handbook PDF, or build.
- I2 — PASS. All ten frozen identities matched at every required verification point.
- I3 — PASS. All 17 journal and all 10 conference pages were freshly read visually.
- I4 — PASS. The p. 742 crop fixes `2^length(f)`; full p. 745 fixes the two ETL conflicts.
- I5 — PASS. Journal controls; conference numbering and proof language are separated; the correction notice is calibrated.
- I6 — PASS. Language notation, inclusive semantics, existential truth, satisfiability, validity column, and reconstructed journal validity clause remain distinct.
- I7 — PASS. Infinite-structure size, unique maximal suffix, ambient-relative acceptable measures, and both strict/non-strict defects are exact.
- I8 — PASS on mathematical statements. Journal `2S(n)`, conference `S(n)`, closure bound, truth-set count, and inclusive fulfillment are correct; F01 concerns the reader's journal page citation.
- I9 — PASS. Theorem 4.7's three separate periodic conditions, exact bounds, `Ff`, initial since, and Savitch remain visible.
- I10 — PASS. ETL naming, semantics, conflicts, closure, `Gamma`, termination obligation, bounds, and continuation search are exact.
- I11 — PASS. Sketches, asserted inductions, abbreviated cases, and brief replacements remain unequal; no Sistla--Clarke Büchi proof is claimed.
- I12 — PASS. The locally introduced technical vocabulary satisfies necessity, definition, standing, nonredundancy, and use.
- I13 — PASS. Independence restrictions were obeyed.
- I14 — PASS by returning REVISE. The locator defect is not outvoted or waived.
- I15 — PASS. This review makes no topic-closure, Part IX, publication-build, rendered-review, human-review, book-completion, or user-acceptance claim.

## Mandatory-check dispositions

- M01 — PASS. Printed p. 742 and the bound crop say `2^length(f)`, not `2^(2 length(f))`; reader lines 2190--2204 and source note lines 511--525 are exact.
- M02 — PASS. No standalone validity clause occurs on journal pp. 734--735; conference p. 160 has one; reader lines 1960--1973 label the journal-relative clause as reconstruction.
- M03 — PASS. Journal p. 742 has `j >= i` and an `i <= l <= j` witness; reader lines 2205--2212 preserve both inclusive endpoints.
- M04 — PASS. The p. 736 union sentence and Lemma 3.3 both literally print `<`; null cases fail; p. 737 uses `<=`; Theorem 3.4 concludes non-strictly. Reader lines 2050--2066 and 2094--2115 disclose all parts.
- M05 — REVISE at the locator surface. Visual source content is exact: journal p. 741 says `2S(n)` and conference p. 164 says `S(n)`. Reader lines 2173--2176 state the correct values and use the correct version keys, but the journal citation incorrectly says p. 742. See F01.
- M06 — PASS. Theorem 4.7's bounds and every-`k` obligation are at reader lines 2230--2249; Theorem 5.3's exact bounds and every-`k` obligations are at lines 2332--2341.
- M07 — PASS. Journal p. 745 says finite or infinite and then uses the unrestricted index; reader lines 2282--2293 explicitly mark represented-position typing as handbook-supplied.
- M08 — PASS. Journal p. 745 prints `N_0 -> a_1 a_2 N_0` and the even-state sentence; reader lines 2298--2307 preserves its conflict with zero-based odd offsets and chooses no repair.
- M09 — PASS. Reader lines 2309--2326 give the same-grammar closure and every `Gamma` continuation edge, and separate terminal productions from continuation children.
- M10 — PASS. Reader lines 2328--2349 distinguish maximum finite-tree depth from until fulfillment and require the continuation set to become empty within the period.
- M11 — PASS. Journal p. 748 identifies neither the bad conference inference nor a uniquely repairing lemma; reader lines 2349--2354 and source note lines 789--796 preserve that limit.
- M12 — PASS. Reader lines 2261--2267 and source note lines 730--751 preserve every proof-status qualification and exclude a Sistla--Clarke Büchi construction.
- M13 — PASS. Shared lines 693--708 explicitly use `L(U) subset L(U,X) subset L(U,S,X)` for the exact hardness/upper-bound classification.
- M14 — PASS. Shared lines 796--808 obtain universal model checking from an existential path satisfying the negation and deterministic-space closure under complement.
- M15 — PASS. Reader lines 2019--2050, 2192--2214, and 2278--2349 locally define, type, distinguish, and use every named construction listed in the charter.
- M16 — PASS. Source-note map lines 119--145 places the four structure measures on p. 735, conclusion on p. 748, and references on pp. 748--749.
- M17 — PASS. Conference p. 160's validity clause and the journal-relative reconstruction are both recorded; the p. 748 correction notice remains unidentified. Reader lines 1960--1973 and 1874--1881.
- M18 — PASS. Reader lines 1998--2017, 2071--2092, and 2141--2148 preserve the exact Lemma 3.2, 3.3, and 3.6 hypotheses, conclusions, and quantifier scopes.
- M19 — PASS. Reader lines 2164--2181 and source-note lines 498--510 distinguish cell diamonds, full instantaneous-description traversals, repeated computations, persistent journal terminal configurations, and conference halting.
- M20 — PASS. Reader lines 2216--2228 define valuation periodicity for `i in N`, positive `p`, and every `k >= i`, and separate it from truth-set equality and obligation discharge.
- M21 — PASS. Shared lines 761--809 return a finite product path plus a nonempty product cycle whose infinite unfolding is the counterexample; no unsupported periodicity name is used.
- M22 — PASS. Reader lines 2315--2326 and source-note lines 644--656 use only the source's labelled tree/`Gamma`; no proof-tree, derivation-tree, or continuation-tree synonym appears in the frozen scope.
- M23 — PASS for the retained repair surfaces. The current frozen artifacts independently satisfy C1--C9, I1--I15, and M01--M15 except for the newly recorded independent citation-locator defect F01; no prior transcript was consulted.
- M24 — PASS. Reader lines 1975--1996 give unique maximal `final(S)`, exact `s = init(S) . final(S)`, and structure-level `range/size` before use.
- M25 — PASS. Reader lines 2019--2050 define all four acceptable-subsequence measures relative to ambient `S`; lines 2025--2033 give eliminability, metalinguistic standing, necessity, and nonredundancy; later bounds use them.
- M26 — PASS. Reader lines 2050--2066 preserve the literal strict union statement, null/null counterexample, and proof-supported non-strict inequality; lines 2068--2071 define `mu(f)` before Lemma 3.3.
- M27 — PASS. Reader lines 2126--2138 give `length(p') <= length(f) card(N)`, `C subset N`, the restricted strongly connected graph, connecting edge, labelling on every node of `p'` or `C`, and acceptance exactly at the start label.
- M28 — PASS. Bibliography lines 2245--2258 give a distinct accurate `SistlaClarke1982` record; reader direct conference claims use that key, and journal claims use `SistlaClarke1985`.
- M29 — PASS for the enumerated round-three repairs. The ambient definitions, strict-sign disclosure, NP certificate, and version-separated citations are repaired without weakening earlier criteria. F01 is an additional direct-locator defect and independently prevents acceptance under C8 and the verdict rule.

## Finding

### F01 — Blocking wrong printed-page locator for the journal's `2S(n)` sentence

Source evidence: on JACM printed p. 741 (`journal-page-09.png`), immediately after Figure 2's computation-history description, the article prints the sentence beginning “Using `2S(n)` `X` operators”; the following printed p. 742 begins with continuation formulae and does not contain that distance sentence. The source-note page map likewise places Figure 2/Lemma 4.4 on p. 741 and its completion on p. 742 (`spec/research/p09-sistla-clarke-1985-source-note.md`, lines 131--132).

Artifact evidence: `handbook/parts/p09/presentations/n-c-012.tex`, lines 2173--2176, correctly states the journal value `2S(n)` and the conference value `S(n)`, and correctly separates `SistlaClarke1985` from `SistlaClarke1982`, but attaches `\cite[p.~742]{SistlaClarke1985}` to the journal sentence. The journal locator must be p. 741. The adjacent conference locator p. 164 is correct.

Required narrow repair: change only that journal pinpoint from `p.~742` to `p.~741`, retain the journal citation key and the mathematical statement, refreeze all affected identities, and subject the new common snapshot to the charter's required fresh independent review. This is a source-locator failure under C8 and the verdict rule; it cannot be waived merely because the mathematical factor and version identity are correct.

## Narrow closure boundary

This verdict reports one blocking direct-citation defect and no other source-fidelity defect in the frozen scope. It does not close N-c-012.d, N-c-012, Part IX, any publication build, rendered inspection, human review, final-book completion, or user acceptance. No manuscript or record was edited by this seat.

REVISE
