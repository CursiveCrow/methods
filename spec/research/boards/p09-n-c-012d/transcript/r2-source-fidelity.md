ACCEPT

# Round-two source-fidelity review: N-c-012.d

## Seat, runtime, governing scope, and independence

- Stable agent identifier: `/root/schmidt_smolka_1991_research/gpss_primary_pass`.
- Review seat: source fidelity.
- Runtime model/version exposure: no exact model name, version, or build identifier was exposed to this seat. The surrounding role identifies the runtime only generically as Codex/GPT-5-family; I do not treat that as an exact version string.
- Governing charter: `spec/research/boards/p09-n-c-012d/charter.md`, read completely before hash verification and substantive review.
- Review basis: a fresh visual reading of the complete controlling JACM facsimile and the complete distinct STOC predecessor, followed by a complete reading of the frozen round-two artifact scope and direct mathematical/prose comparison. Page images and PDFs controlled over OCR, the source note, memory, and round one.
- Independence: I did not inspect `ledger.md`, `transcript/chair.md`, any round-one transcript, either other reviewer's round-two transcript or verdict, or any other reviewer transcript. I did not contact another reviewer.
- Mutation boundary: I created only this assigned transcript. I did not edit the charter, reader, shared Part IX text, bibliography, source note, source-presentation ledger, authority files, images, or any other file.
- Prohibited activity: I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or builds.

## Frozen round-two hash verification

All nine round-two hashes were computed and compared with the charter before any substantive source or artifact review. Every value matched exactly.

| Frozen object | Verified round-two SHA-256 | Disposition |
|---|---|---|
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf` | `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5` | exact match |
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf` | `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283` | exact match |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png` | `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114` | exact match |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png` | `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1` | exact match |
| `handbook/parts/p09/presentations/n-c-012.tex` | `48D2F8F946AFFC394613D7895E89175099CC9FA73800BDA36A3C5F63353C6AD5` | exact match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` | exact match |
| `handbook/bib/handbook.bib` | `1BD6B33A12449449671505A5EEEAB64C99D0E8A74F3E968C9951FF932B778E95` | exact match |
| `spec/research/p09-sistla-clarke-1985-source-note.md` | `D7E85E5AC951C56F607099A5756C1AA5CEEC02DB8D0CC3EC359E17EBE2450FCD` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | `D5BD9F8BA7A12AFD7A8A08CDAAFB2E0E4C0E0B48E0BD83D5BDC06AA08D2E8353` | exact match |

The same nine objects were recomputed immediately before filing this transcript; the final recomputation is recorded below.

## Complete authority-page visual-read record

I opened each page image at original detail and visually read the complete printed content. The journal PDF contains seventeen pages corresponding one-for-one to printed pp. 733--749. The conference PDF is a distinct ten-page object corresponding one-for-one to printed pp. 159--168. OCR was not used as controlling evidence.

### JACM 1985: all seventeen pages

| Image | Printed page | Fresh visual coverage |
|---|---:|---|
| `journal-page-01.png` | 733 | plural title, Sistla-before-Clarke author order, affiliations, abstract, descriptors, introduction, addresses, JACM issue/page line, and the conditional ACM rights notice |
| `journal-page-02.png` | 734 | completion of the introduction, operator-sensitive claims, Section 2 notation, language notation, and beginning of the formation clauses |
| `journal-page-03.png` | 735 | restricted `F,X` fragment, distinct-state structures, inclusive `X/U/S` clauses, closure bound, total `R`-structures, existential path-truth problem, and Section 3 definitions of `init`, `final`, `range`, and `size` at the bottom of the page |
| `journal-page-04.png` | 736 | Lemmas 3.1--3.2, the zero-prefix clause, ordinary and acceptable subsequences, Lemma 3.3's exact acceptable-input/output and intermediate-supersequence quantifiers, literal strict bound, and zero/zero basis |
| `journal-page-05.png` | 737 | every non-strict induction use in Lemma 3.3, Theorem 3.4's non-strict conclusion and explicit `PROOF SKETCH` label, and Theorem 3.5 statement |
| `journal-page-06.png` | 738 | Figure 1, the chain-of-diamonds 3-SAT reduction, exact labels/formula, and the NP membership construction |
| `journal-page-07.png` | 739 | completion of Theorem 3.5, exact Lemma 3.6 finite subsequence/intermediate-supersequence statement, Theorem 3.7, and Theorem 4.1 |
| `journal-page-08.png` | 740 | stuttering Lemma 4.2, its `L(U,X)` exclusion, Lemma 4.3, and the structure-truth-to-satisfiability reductions |
| `journal-page-09.png` | 741 | Figure 2, terminal-state persistence without tape updates, the tape-cell/instantaneous-description encoding, and the journal's literal `2S(n)` next-distance statement |
| `journal-page-10.png` | 742 | completion of Lemma 4.4, source truth sets and their count, Lemma 4.5, exact `j >= i` fulfillment with inclusive witness endpoint, valuation periodicity, and beginning of Lemma 4.6 |
| `journal-page-11.png` | 743 | completion of Lemma 4.6 and exact Theorem 4.7 statement, including bounds, source-truth-set equality, and every-periodic-position pending-`U` discharge |
| `journal-page-12.png` | 744 | completion of Theorem 4.7, the `Ff` move, and Theorem 4.1's on-the-fly Boolean/`X/U/S`, initial-since, loop, and fulfillment checks |
| `journal-page-13.png` | 745 | Savitch conclusion; ETL grammar semantics; finite/infinite string with unrestricted index; `N_0 -> a_1 a_2 N_0` parity conflict; normalization; closure; the labelled tree `Gamma(S,j,N_i)`; and beginning of Lemma 5.1 |
| `journal-page-14.png` | 746 | completion of Lemma 5.1, finite-tree maximum-depth fulfillment, exact Lemma 5.2 extension, and beginning of Theorem 5.3 |
| `journal-page-15.png` | 747 | completion of Theorem 5.3 with both obligation families, Theorem 5.4's encoded-grammar input, exact `card(SF(f)) <= 2n`, continuation-set update, and within-period empty-set requirement |
| `journal-page-16.png` | 748 | completion of Theorem 5.4, complete Table I, conclusion confined to this page, the non-isolating conference-error notice, and beginning of references |
| `journal-page-17.png` | 749 | completion of references and the exact April 1982/October 1984/January 1985 receipt history |

Controlling derivatives also read visually:

- `journal-page-10-bound-crop.png`: the faint exponent on printed p. 742 visibly reads `2^length(f)`, not `2^(2 length(f))`.
- `journal-page-13.png`: the complete enlarged printed p. 745 visibly preserves both the finite/infinite index defect and the zero-based odd-offset/even-state sentence conflict.

### STOC 1982: all ten pages

| Image | Printed page | Fresh visual coverage |
|---|---:|---|
| `conference-page-01.png` | 159 | separate conference title/authors/Harvard affiliation, abstract/introduction, support note, and conference rights/identifier line |
| `conference-page-02.png` | 160 | conference grammar with `F,G` among inductive forms, inclusive temporal clauses, satisfiability, the explicit universal all-structures/all-positions validity definition, and beginning of the `R`-structure definition |
| `conference-page-03.png` | 161 | completion of existential `R`-truth, Section 3 definitions, conference Theorem 3.1 and Lemmas 3.2--3.3, and acceptable-subsequence distinction |
| `conference-page-04.png` | 162 | conference Lemma 3.4 and proof sketch, its `c * length(f)` formulation, Theorem 3.1 proof sketch, and beginning of Theorem 3.5 |
| `conference-page-05.png` | 163 | Figure 1, completion of the 3-SAT reduction, NP membership procedure, and the conference witness-bound inconsistency |
| `conference-page-06.png` | 164 | Section 4 theorem/reduction, conference Lemma 4.3 and Figure 2, machine-halting convention, and the literal conference `S(n)` next-distance statement |
| `conference-page-07.png` | 165 | final-ID language, source types, recurring-type invariant, conference Lemmas 4.4--4.5, Theorem 4.6 without journal every-position `U` discharge, and beginning of the proof outline |
| `conference-page-08.png` | 166 | completion of the proof outline, abbreviated regular-operator semantics/proof, same parity sentence, `n^2` closure estimate, and beginning of the conclusion |
| `conference-page-09.png` | 167 | completion of conclusion, Figure 3 classification table, fragment footnote, and beginning of the coded bibliography |
| `conference-page-10.png` | 168 | completion of conference bibliography |

## Complete frozen-artifact read record

The following complete charter-defined scope was read after the authority pass:

- `handbook/parts/p09/presentations/n-c-012.tex:1851-2314`: the complete repaired Sistla--Clarke subsection, ending immediately before Alpern--Schneider at line 2315.
- `handbook/parts/p09/logic-in-computer-science.tex:602-809`: the complete necessary local context for `thm:p09-ltl-pspace` at lines 693--708 and `thm:p09-ltl-model-checking` at lines 796--809, including the automata method at lines 720--794 needed to audit attribution and witness form.
- `handbook/bib/handbook.bib:2245-2259`: the complete `SistlaClarke1985` entry.
- `spec/research/p09-sistla-clarke-1985-source-note.md:1-810`: the entire repaired source note.
- `spec/research/p09-source-presentations-lot2-3.md:185-232`: the entire repaired N-c-012.d source-presentation ledger entry.

For acquisition provenance, the current Carnegie Mellon publication index was independently inspected at `https://www.cs.cmu.edu/~emc/papers.htm`. Its journal row still displays the singular catalogue title and Clarke-before-Sistla order while linking the journal PDF; its conference row separately lists the STOC paper and targets the misdirected conference-path URL recorded in the source note. The frozen facsimile title pages, printed pagination, and hashes control version identity.

## Admitted-repair closure

Every repair family made mandatory by the updated charter is present and source-faithful on the round-two hashes.

| Repair family | Round-two evidence | Disposition |
|---|---|---|
| p. 735/p. 736 page-map correction | Source note lines 123--139 puts `init`, `final`, `range`, and `size` on p. 735 and starts p. 736 with the lemmas; lines 141--145 confine the conclusion to p. 748 and references to pp. 748--749 | repaired cleanly |
| conference/journal validity distinction | Reader lines 1959--1972; note lines 256--265 and reconciliation row 712; source-presentation line 191 | repaired cleanly |
| unidentified conference-error boundary | Reader lines 1873--1879 and 2276--2280; note lines 24--33, 728, 733--740, and 765--769; source-presentation line 189 | repaired cleanly |
| Lemmas 3.2, 3.3, and 3.6 exact hypotheses/conclusions | Reader lines 1989--2045 and 2070--2077; note lines 286--354 and 380--395 | repaired cleanly |
| Figure 2 encoding unit and terminal-machine boundary | Reader lines 2093--2107; note lines 442--454 and reconciliation row 721; source-presentation line 217 | repaired cleanly |
| valuation-period definition and three-way distinction | Reader lines 2143--2155 and 2168--2175; note lines 478--489 and 506--539; source-presentation lines 203--215 | repaired cleanly |
| finite counterexample witness in shared model checking | Shared lines 761--809, especially 781--787 and 796--808 | repaired cleanly |
| exact source tree name/standing | Reader lines 2242--2253; note lines 583--608 and reconciliation row 727; source-presentation line 217; charter I10/M09/M22 | repaired cleanly |

No repair weakened any retained criterion, invariant, or mandatory check.

## Criteria C1--C9

- **C1 — PASS.** The frozen package gives the exact work identity: A. Prasad Sistla before Edmund M. Clarke; plural *Logics*; *Journal of the ACM* 32(3), July 1985, pp. 733--749; DOI `10.1145/3828.3837`; ISSN `0004-5411`; and the printed receipt/revision/acceptance history. It separately identifies STOC 1982, pp. 159--168, DOI `10.1145/800070.802189`, records both file identities and the CMU conference-link defect, and makes no rights overclaim. Source: journal pp. 733, 749; conference p. 159. Artifact: reader lines 1853--1880; note lines 35--117; bibliography lines 2245--2259; source-presentation lines 185--189.
- **C2 — PASS.** Syntax, `L(O_1,...,O_k)` standing, `L-tilde(F,X)`, inclusive `X/U/S`, distinct-state valuation structures, total finite `R`-structures, existential path truth, and the universal-program counterexample relation are exact. Conference p. 160's explicit validity clause and the journal's omission are now separated, and the reader labels its journal-relative universal clause reconstruction. Source: journal pp. 734--735, 748; conference p. 160. Artifact: reader lines 1882--1972; note lines 147--265; source-presentation line 191.
- **C3 — PASS.** The Section 3 definitions and finite measure are exact. Lemma 3.2 includes its zero-prefix boundary; Lemma 3.3 includes acceptable input/output, every intermediate supersequence, surviving-position scope, literal `<`, proof-supported `<=`, and unknown editorial cause; Lemma 3.6 includes a finite subsequence containing the current state and the universal intermediate-supersequence clause. Theorems 3.4--3.7, Figure 1, witness measures, and proof granularity are accurate. Source: journal pp. 735--739. Artifact: reader lines 1974--2078; note lines 267--401 and 674--695.
- **C4 — PASS.** The reduction chain, stuttering boundary, exact Figure 2 representation, journal `2S(n)` versus conference `S(n)`, closure/truth-set distinction, p. 742 count, fulfillment definition, Lemmas 4.5--4.6, valuation periodicity, Theorem 4.7 bounds/three conditions, `Ff`, initial-since check, and Savitch step are exact. Source: journal pp. 739--745; conference pp. 164--165. Artifact: reader lines 2080--2194; note lines 403--539 and reconciliation lines 718--724.
- **C5 — PASS.** ETL grammar semantics, disjoint nonterminals, normalization, finite/infinite typing defect, parity conflict, closure, labelled `Gamma`, terminal/continuation separation, Lemmas 5.1--5.2, two fulfillment notions, Theorem 5.3 bounds/obligations, Theorem 5.4 input encoding/continuation sets, and non-isolating correction boundary are all exact. Source: journal pp. 745--748; conference p. 166. Artifact: reader lines 2196--2281; note lines 541--633, 683--695, and 725--728; source-presentation lines 217--229.
- **C6 — PASS.** The reader's Table I rows are exact, including the distinction between Theorem 4.1's displayed bases and the table's `L(U,X)` row. Shared lines 693--708 use `L(U) subset L(U,X) subset L(U,S,X)` for the exact hardness/upper-bound transfer. Shared lines 796--808 obtain universal path checking from existential truth of the negated formula and deterministic-space complement closure, while returning the exact finite product path/cycle witness. Source: journal pp. 739, 748. Artifact: reader lines 2283--2313; shared lines 693--708 and 761--809.
- **C7 — PASS.** The reconciliation at note lines 701--740 accurately distinguishes grammar, validity, closure, fragment proof, result numbering/bounds, stuttering, next distance, terminal-machine convention, loop invariant, theorem obligations, proof status, ETL semantics/machinery/error status, displays, branching comparison, and references. It imports no conference theorem number into the journal and identifies no unique repair. Direct comparison: all conference pp. 159--168 against all journal pp. 733--749.
- **C8 — PASS.** Bibliography, author/title/order, DOI/ISSN, page locators, page map, proof-status table, source-presentation entry, access/file identities, and rights qualification are accurate. The repaired map places the Section 3 definitions on p. 735, the conclusion on p. 748 only, and references on pp. 748--749. Artifact: bibliography lines 2245--2259; note lines 35--145 and 674--695; source-presentation lines 185--232.
- **C9 — PASS.** The prose is independently worded, definition-before-use, explicitly typed and quantified, and candid about reconstruction and printed defects. Each introduced technical name has standing, eliminable content, nonredundancy, necessity, and later use. I found no unsupported addition, missing material qualification, or terminology-rule failure in the complete frozen scope.

## Invariants I1--I15

- **I1 — PASS.** Review was limited to complete source reading, mathematical comparison, provenance inspection, and prose inspection. No prohibited test/build activity occurred.
- **I2 — PASS.** Only the exact nine round-two hashes were reviewed; all matched before review and at final recomputation.
- **I3 — PASS.** Every journal page 733--749 and every conference page 159--168 was freshly read visually; images/PDFs controlled.
- **I4 — PASS.** The p. 742 crop reads `2^length(f)`. The complete p. 745 image preserves both specified ETL defects.
- **I5 — PASS.** Journal and conference numbering, bounds, hypotheses, proof language, and Section 5 machinery remain distinct. The p. 748 notice is not made more specific than its text permits.
- **I6 — PASS.** The language notation, restricted fragment, inclusive operators, existential `R`-truth, satisfiability, and validity remain distinct. The repaired artifacts explicitly say that conference p. 160 prints validity while journal pp. 734--735 do not, and label the journal-relative clause reconstruction.
- **I7 — PASS.** `size(S)` is a finite measure of an infinite structure; acceptable subsequence is exact; the Lemma 3.3 strict/non-strict defect and unknown cause are explicit.
- **I8 — PASS.** Journal `2S(n)`, conference `S(n)`, `card(SF(f)) <= 2 length(f)`, `2^length(f)`, `j >= i`, and the inclusive fulfillment witness are all distinct and exact.
- **I9 — PASS.** Theorem 4.7 contains valuation periodicity, source-truth-set equality, and every-position `U` discharge with exact bounds; `Ff`, initial since, and Savitch remain visible at printed proof strength.
- **I10 — PASS.** ETL's nonterminal convention, constructor, normalization, closure, labelled `Gamma`, finite-depth termination, bounds, continuation search, reconstructed finite-domain typing, and unresolved parity conflict are exact.
- **I11 — PASS.** Proof sketches, asserted inductions, abbreviated cases, and brief replacements remain unequal. The Büchi construction is attributed to Vardi--Wolper, not Sistla--Clarke.
- **I12 — PASS.** The five-part terminology rule is met locally for every introduced name audited under M15 and M22; no hypothetical answer is prematurely named.
- **I13 — PASS.** The independence and assigned-file boundaries were obeyed.
- **I14 — PASS.** This verdict rests on exhaustive clean review of this one frozen snapshot, not a vote or another seat's conclusion.
- **I15 — PASS.** The acceptance boundary below is confined to round-two N-c-012.d topic-level scholarly review and claims no broader closure.

## Mandatory checks M01--M23

- **M01 — PASS.** The controlling crop of journal p. 742 visibly prints `2^length(f)`. Reader lines 2123--2131 and note lines 455--469 preserve that literal count and reject `2^(2 length(f))`.
- **M02 — PASS.** No standalone validity clause appears on journal pp. 734--735. Conference p. 160 does print the universal clause. Reader lines 1959--1972 and note lines 256--265 explicitly label the identical journal-relative handbook clause reconstruction; reconciliation row 712 records the version difference.
- **M03 — PASS.** Journal p. 742 defines fulfillment only for `j >= i` and permits the right-hand witness at every `l` with `i <= l <= j`. Reader lines 2132--2139; note lines 474--477.
- **M04 — PASS.** Journal p. 736 literally displays `<`; its atomic basis is zero/zero; every printed induction estimate on pp. 736--737 is non-strict; Theorem 3.4 concludes non-strictly. Reader lines 2035--2045; note lines 338--354.
- **M05 — PASS.** Journal p. 741 prints `2S(n)` next operators; conference p. 164 prints `S(n)`. Reader lines 2102--2105; note lines 451--454 and reconciliation row 720.
- **M06 — PASS.** Theorem 4.7's bounds, domains, type equality, and every-periodic-position `U` fulfillment are exact at reader lines 2157--2177. Theorem 5.3's `card(SF(f))` bounds and both obligation families are exact at lines 2259--2268. Note lines 495--535 and 609--621 independently preserve the same statements.
- **M07 — PASS.** Journal p. 745 pairs “finite or infinite string” with unrestricted `l >= 0`. Reader lines 2215--2220 and note lines 553--562 label the finite represented-position restriction handbook-supplied typing.
- **M08 — PASS.** Journal p. 745 prints `N_0 -> a_1 a_2 N_0` and says even states, while its zero-based constructor checks `P` at odd offsets. Reader lines 2225--2234 and note lines 564--581 preserve the conflict and choose no repair; conference p. 166 prints the same parity sentence.
- **M09 — PASS.** Reader lines 2236--2253 and note lines 583--600 give the exact ETL closure, root, depth-indexed continuation edges, selected-argument condition, and terminal-production separation for `Gamma(S,j,N_i)`.
- **M10 — PASS.** Journal p. 746 defines finite-tree fulfillment by maximum depth and separates it from until fulfillment. Reader lines 2255--2268 and 2273--2276 and note lines 601--628 preserve that distinction and the requirement that each tracked continuation set become empty within the guessed period.
- **M11 — PASS.** Journal p. 748 says only that “one of the theorems used in [9]” contained an error. It does not isolate the theorem, inference, or unique repair. Reader lines 1873--1879 and 2276--2280; note lines 24--33, 728, 733--740, and 765--769; source-presentation line 189.
- **M12 — PASS.** Reader lines 2047--2048 and 2188--2194 and note lines 630--633 and 674--695 preserve every material proof-status qualification. Shared lines 745--754 attribute the Büchi translation to Vardi--Wolper; no Sistla--Clarke automata proof is asserted.
- **M13 — PASS.** Shared lines 693--708 explicitly use `L(U) subset L(U,X) subset L(U,S,X)` so the left fragment supplies PSPACE-hardness and the right fragment the PSPACE upper bound.
- **M14 — PASS.** Reader lines 1949--1958 keep Sistla--Clarke's problem existential. Shared lines 796--808 universalize by existential truth of `not A` and deterministic polynomial-space complement closure, not by silently changing the source input quantifier.
- **M15 — PASS.** Local five-part terminology audit:
  - acceptable subsequence is source-defined, typed as a condition on subsequences, distinguished from ordinary subsequence, and used in Lemma 3.3/Theorem 3.4 (`n-c-012.tex:2010-2045`);
  - source truth set is exactly defined as a finite subset of `SF(f)`, distinguished from closure, valuation, and arbitrary power set, and used in Lemmas 4.5--4.6/Theorem 4.7 (`n-c-012.tex:2110-2141`);
  - fulfilled before has exact, separate `U`-witness and finite-tree-depth definitions and is used in the two periodic reductions (`n-c-012.tex:2132-2141, 2255-2268`);
  - the ETL constructor has grammar-indexed standing, exact finite/infinite reconstructed typing, nonredundancy from ordinary `U`, and later closure/tree use (`n-c-012.tex:2196-2240`);
  - `Gamma` is exactly the source's labelled, finitely branching tree, is neither a model nor proof-calculus object, and is used by Lemmas 5.1--5.2 and Theorems 5.3--5.4 (`n-c-012.tex:2242-2276`).
- **M16 — PASS.** Note lines 123--139 place all four Section 3 definitions on p. 735 and start p. 736 with Lemmas 3.1--3.3; lines 141--145 place the conclusion only on p. 748 and references on pp. 748--749. Direct visual inspection agrees.
- **M17 — PASS.** Conference p. 160's formal validity definition is now recorded while the identical clause remains explicitly reconstructed relative to journal pp. 734--735 (reader 1959--1972; note 256--265/712; source-presentation 191). The correction notice is confined to an unidentified theorem used in the conference proof (reader 1873--1879/2276--2280; note 728/733--740/765--769).
- **M18 — PASS.** Lemma 3.2's common initial length, pointwise prefix equality, zero-prefix first valuation, equal recurring range, universal `f in L(F)`, and truth equivalence are exact at reader lines 1989--2008. Lemma 3.3's acceptable `t` and `u`, NNF/every-represented-position hypothesis, every intermediate `w`, restriction valuation, surviving-position scope, and separately disclosed inequality conflict are exact at lines 2010--2045. Lemma 3.6's `f in L-tilde(F,X)`, current state, finite `u` containing that state, length bound, every intermediate `v`, restricted valuation, and preserved truth at the surviving state are exact at lines 2070--2077. Note lines 286--354 and 380--395 corroborate the reconstruction.
- **M19 — PASS.** Reader lines 2093--2107 identify each Figure 2 diamond with one tape-cell position, a complete BI-to-EI traversal with one instantaneous description, repeated traversals with a computation, and journal terminal configurations with persistent state/tape contents. Note reconciliation row 721 records the conference's halting-on-every-input language against the journal's infinite persistence convention. Source-presentation line 217 is consistent.
- **M20 — PASS.** Reader lines 2143--2155 define periodicity for `i in N`, positive `p`, and every `k >= i` by equality of complete valuations. Lines 2149--2153, 2168--2175, and 2259--2268 keep that equality distinct from source-truth-set equality, pending-`U` discharge, and ETL finite-tree discharge. Note lines 478--489/506--539 and source-presentation lines 203--215 agree.
- **M21 — PASS.** Shared lines 781--787 return satisfaction or a counterexample represented by a finite product path to a nonempty product cycle whose infinite repetition is the counterexample. The theorem repeats the exact witness at lines 796--808. No undefined periodicity name is used.
- **M22 — PASS.** Across the reader, source note, source-presentation ledger, and charter, `Gamma(S,j,N_i)` is called only the source's labelled tree or `Gamma`. No “proof tree,” “derivation tree,” or “continuation tree” synonym appears in the frozen N-c-012.d scope. Exact locators: reader 2242--2253; note 588--621/727; source-presentation 217; charter I10/M09/M22.
- **M23 — PASS.** The admitted-repair table above verifies every mandatory round-one repair family directly on the round-two hashes. The full C1--C9, I1--I15, and retained M01--M15 audit found no regression or weakened qualification.

## Final hash recomputation and narrow closure boundary

Immediately before filing, all nine frozen objects were recomputed again and retained exactly the values recorded in the opening hash table. No source or frozen artifact changed during review.

This `ACCEPT` closes only this source-fidelity seat's blind round-two scholarly review of the exact frozen N-c-012.d snapshot. It does not close another seat, Alpern--Schneider, N-c-012 as a whole, Part IX, another part, the final post-freeze publication build, rendered-page inspection, human review, final-book completion, or user acceptance.

ACCEPT
