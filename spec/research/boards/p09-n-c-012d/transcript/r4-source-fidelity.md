ACCEPT

# Round-four source-fidelity transcript: N-c-012.d

## Reviewer, verdict, and independence

- Stable agent identifier / canonical task name: /root/r4_source_fidelity.
- Runtime model/version exposure: no exact runtime model name or version identifier was exposed to this seat.
- Verdict: ACCEPT. The corrected frozen round-four reconstruction is source-faithful and checked clean under C1--C9, I1--I15, and M01--M37. I found no must-fix item and retain no unresolved uncertainty.
- This review was restarted from scratch after withdrawal of the first freeze. The corrected source-presentation object, including its local definition of the tuple abbreviation, was reviewed as part of the controlling snapshot.
- I did not inspect ledger.md, transcript/chair.md, any round-one, round-two, or round-three transcript, or any sibling round-four transcript or verdict. I did not contact another seat or use another seat's completion status.
- I performed no tests, test harnesses, automated checkers, repository scripts, TeX runs, handbook-PDF inspection, or builds. The work consisted only of direct visual source reading, targeted text inspection, mathematical/source comparison, and the expressly permitted SHA-256 verification.

## Frozen snapshot verification

I recomputed and matched all ten controlling round-four SHA-256 values:

1. tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf  
   F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5
2. tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf  
   1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283
3. tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png  
   D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114
4. tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png  
   27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1
5. tmp/pdfs/p09-sistla-clarke-1985/journal-page-04-acceptable-crop.png  
   C267D4B4DF785F9A7E82123B068662E45D7E2C87CB18C24D7B8EB0B875AF413B
6. handbook/parts/p09/presentations/n-c-012.tex  
   45E2B1F4A97B1049247FD198CDF69C67794D129AEB28582FE595DC34EDF7ABD8
7. handbook/parts/p09/logic-in-computer-science.tex  
   961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F
8. handbook/bib/handbook.bib  
   F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B
9. spec/research/p09-sistla-clarke-1985-source-note.md  
   1E734EF089EEA077DE90229411726D85708A102D914EFE4F7956B7DDE9EE9094
10. spec/research/p09-source-presentations-lot2-3.md  
    40F0AE94BB9B763F941B421F63854B17A426C1989084F6262ACD59071C0A7E8D

## Direct visual source-reading record

I freshly opened with the image viewer and visually read all twenty-seven source-page images:

- Journal images 01--17, corresponding one-for-one to printed pp. 733--749.
- Conference images 01--10, corresponding one-for-one to printed pp. 159--168.

I also visually inspected the enlarged journal p. 742 exponent crop, the full enlarged journal p. 745 image, and the enlarged journal p. 736 acceptable-union crop. The visual reading covered the front matter, every definition and numbered result, both reductions and figures, the algorithms, Table I, conclusion/correction notice, and references. In particular, the images directly establish:

- journal p. 742 prints the realized-source-truth-set count as 2^length(f);
- journal p. 736 prints the strict acceptable-union inequality and strict Lemma 3.3 bound, while the p. 737 proof uses non-strict bounds;
- journal p. 741 prints 2S(n), whereas conference p. 164 prints S(n);
- journal p. 745 prints both the unrestricted finite/infinite-word index clause and the even-state sentence that conflicts with the displayed zero-based constructor semantics;
- conference p. 160, unlike journal pp. 734--735, prints a formal validity clause;
- journal p. 748 reports only that an unidentified theorem used in the conference proof contained an error and does not identify a precise inference or unique repairing lemma.

The page images, not OCR, notes, memory, or any prior verdict, were the evidentiary basis for source claims.

## Criteria C1--C9

- C1 — PASS. The reader gives the exact author order, plural title, JACM volume 32, issue 3, July 1985, pp. 733--749, DOI, source provenance, journal file hash, rights limit, receipt/revision/acceptance history, and distinct 1982 STOC object at reader lines 1853--1881. ISSN 0004-5411 and the separate conference identity are exact in handbook.bib lines 2245--2274. These agree with journal pp. 733 and 749 and conference p. 159. The source note's identity, acquisition, file, and rights record is at lines 35--117. No public-access/republication inference is made.

- C2 — PASS. Reader lines 1883--1973 exactly separate the primitive grammar, F/G abbreviations, L(O_1,...,O_k), the atomic-negation-only restricted fragment, inclusive U/S, infinite structures, total R-structures, existential path truth, universal-program counterexample use, and the reconstructed validity clause. This agrees with journal pp. 734--735 and 748 and conference p. 160. The clause is expressly reconstruction relative to the journal, not falsely attributed to journal p. 735.

- C3 — PASS. Reader lines 1975--2193 accurately reconstruct the unique maximal final suffix; exact init/final/range/size decomposition; ambient-relative acceptable-subsequence operations; Lemmas 3.1--3.3 and 3.6; both strict/non-strict source conflicts; Theorems 3.4--3.7; Figure 1's chain-of-diamonds reduction; every Theorem 3.5 labelling rule; the literal strong-connectivity/entry-edge certificate; its loopless-singleton false acceptance; and the separately owned directed-cycle correction. Formula length, size, and mu are not conflated, and proof-sketch/induction qualifications agree with journal pp. 735--739.

- C4 — PASS. Reader lines 2195--2420 preserve the exact Section 4 reduction chain, all Lemma 4.3 auxiliary formulas, the two self-loop-sensitive pure-U replacements, Lemma 4.2's stuttering scope, the Figure 2 encoding unit, journal p. 741's 2S(n) versus conference p. 164's S(n), closure versus realized-source-truth-set count, inclusive fulfilled-before definition, exact Lemmas 4.5--4.6, full Theorem 4.7 bounds and every-position obligations, the Ff move for past S, and all five direction-sensitive Theorem 4.1 recurrences, initial-since condition, loop closure, storage, and Savitch step. These agree with journal pp. 739--745.

- C5 — PASS. Reader lines 2422--2556 give the exact disjoint-grammar convention, right-linear grammar and normalization, grammar-indexed constructor, finite/infinite printed typing defect and handbook-owned represented-index restriction, parity conflict without invented repair, ETL closure, exact labelled tree Gamma, terminal/continuation separation, Lemmas 5.1--5.2 with both inherited conclusions, distinct finite-tree and U obligations, Theorem 5.3 bounds, and Theorem 5.4's exact positive rule and negative frontier update. Grammars are part of the encoded input, the continuation set must empty within the period, and the correction notice is calibrated exactly to journal pp. 745--748.

- C6 — PASS. Reader lines 2558--2588 preserve every Table I language/classification, distinguish Theorem 4.1's displayed list from Table I's L(U,X) row, and state the exact containment argument. Shared Part IX lines 693--708 use L(U) subseteq L(U,X) subseteq L(U,S,X) for lower and upper bounds. Reader lines 1950--1959 and shared Part IX lines 796--808 pass from existential truth of the negated formula to universal model checking by polynomial-space closure under complement, without changing the source problem's quantifier.

- C7 — PASS. The full journal/conference comparison in source-note lines 907--946 agrees with my visual reading of all twenty-seven pages. It accurately separates front matter, grammar/validity wording, closure, restricted fragment, Section 3 numbering/bounds/proof detail, Section 4 numbering and machinery, S(n)/2S(n), halting/persistence, periodic hypotheses, Section 5 proof replacement, summaries, and references. Reader lines 1873--1881, 2251--2266, and 2550--2556 never import conference theorem language into the journal or claim a uniquely identified repair.

- C8 — PASS. The two bibliography entries at handbook.bib lines 2245--2274 are source-accurate and distinct. Direct conference and journal citations in the reader resolve to their respective records. Source-note lines 119--145 give the accurate page map; lines 880--905 give the source-exact proof-status table; lines 907--946 give the version reconciliation; and lines 997--1022 state the evidentiary and downstream-gate limits. Source-presentation lines 185--345 agree with the reader, source note, bibliography, and rights boundary.

- C9 — PASS. The reader subsection at lines 1851--2589 is independently worded, definition-before-use, typed, quantified, and candid about source defects versus handbook correction. All introduced names receive adequate local standing and use. In the corrected source presentation, lines 284--306 locally define the temporary tuple abbreviation bar f, state why it is needed, classify it as eliminable metalinguistic notation, distinguish it from formulas and guessed sets, and restrict its use to the two displayed rules. No unsupported theorem, Büchi attribution, unmarked authorial repair, omitted controlling qualification, or terminology-rule violation remains.

## Invariants I1--I15

- I1 — PASS. This was exclusively a source-reading, mathematical-reconstruction, and prose-inspection review. None of the prohibited computational or publication operations was performed.
- I2 — PASS. All ten objects match the corrected round-four hashes listed above.
- I3 — PASS. Every journal page 733--749 and every conference page 159--168 was freshly visually read; page-level claims and differences were checked against those images.
- I4 — PASS. The p. 742 crop confirms 2^length(f). The p. 745 image confirms both ETL defects. Reader lines 2275--2289 and 2431--2460 preserve them exactly.
- I5 — PASS. The journal controls throughout. Reader lines 1873--1881 and 2550--2556 and source-note lines 907--946 preserve distinct numbering, proof machinery, and the correction notice's limited force.
- I6 — PASS. Reader lines 1883--1973 and 2558--2588 distinguish all named fragments, inclusive U/S, satisfiability, existential R-truth, and reconstructed validity.
- I7 — PASS. Reader lines 1975--2105 preserve the unique maximal suffix, the finite description measure of an infinite structure, ambient-relative subsequence measures, both printed strict inequalities, their null failures, and the proof-supported non-strict correction.
- I8 — PASS. Reader lines 2251--2297 preserve journal 2S(n), conference S(n), closure cardinality, the 2^length(f) realized-type count, and the j >= i inclusive fulfillment witness.
- I9 — PASS. Reader lines 2340--2412 preserve valuation periodicity, every-position type equality and U discharge, exact bounds, the Ff move, initial-since check, storage statement, and Savitch step.
- I10 — PASS. Reader lines 2422--2556 preserve all listed ETL conventions, the exact tree and frontier machinery, the two Theorem 5.3 bounds, the Theorem 5.4 rules, handbook-owned finite-index typing, and unrepaired parity conflict.
- I11 — PASS. Reader lines 2107--2115, 2311--2312, 2414--2420, and 2501--2502 and source-note lines 880--905 preserve the source's unequal proof granularity. Reader lines 2418--2420 and 2550--2556 expressly avoid attributing a Büchi/automata proof to Sistla--Clarke.
- I12 — PASS. Acceptable subsequence, ambient subscripts, label, source truth set, fulfilled-before, auxiliary reduction formulas, A/B, the ETL constructor, Gamma, varphi, and the corrected bar-f abbreviation each have a local necessity/use, exact eliminable definition or source definition, standing, nonredundancy, and actual later use. Relevant reader locators are 2019--2050, 2135--2163, 2201--2230, 2268--2297, 2376--2412, and 2422--2550; source-presentation locator 284--306.
- I13 — PASS. I maintained the required isolation and inspected none of the prohibited review records.
- I14 — PASS. There was no unread page, hash mismatch, uncertainty, or must-fix item. This ACCEPT is an independent judgment, not a vote or inference from another seat.
- I15 — PASS. This verdict closes at most the N-c-012.d topic-level scholarly-review seat. It does not close Alpern--Schneider, N-c-012 as a whole, Part IX, a publication build, rendered inspection, human review, final-book completion, or user acceptance. The same limit is stated in source-note lines 1019--1022 and source-presentation lines 326--345.

## Mandatory checks M01--M37

- M01 — PASS. The enlarged p. 742 crop reads 2^length(f). Reader lines 2275--2289 and source-note lines 579--593 preserve that count and reject attribution of 2^(2 length(f)).

- M02 — PASS. Visual inspection confirms no formal validity clause on journal pp. 734--735. Conference p. 160 contains it. Reader lines 1960--1973 expressly mark the identical universal clause as reconstruction relative to the journal.

- M03 — PASS. Journal p. 742 defines fulfillment for j >= i with the right operand witnessed at an index from i through j inclusive. Reader lines 2290--2297 reproduce exactly that endpoint-inclusive condition.

- M04 — PASS. Journal p. 736 literally prints strict less-than both in the preparatory acceptable-union sentence and Lemma 3.3. Empty/null cases refute the strict forms; the p. 737 proof and Theorem 3.4 use non-strict bounds. Reader lines 2051--2066 and 2094--2115 preserve every side of the conflict and do not silently rewrite the source.

- M05 — PASS. Direct image comparison confirms journal p. 741 says 2S(n) and conference p. 164 says S(n). Reader lines 2253--2266 give those exact pinpoints.

- M06 — PASS. Reader lines 2354--2374 state Theorem 4.7 with i in N, p positive, i <= 2^(1+length(f)), p <= 4^(1+length(f)), truth-set equality for every k >= i, and every pending U obligation fulfilled before the next copy. Reader lines 2502--2511 state Theorem 5.3 with l <= 2^(1+card(SF(f))), p <= c^card(SF(f)), and both obligations at every periodic position.

- M07 — PASS. Journal p. 745 says finite or infinite generated string and then quantifies over unrestricted nonnegative indices. Reader lines 2431--2446 explicitly identify the represented-position restriction for a finite word as handbook-supplied typing, not printed text.

- M08 — PASS. Journal p. 745 and conference p. 166 print N_0 -> a_1 a_2 N_0 and the even-state sentence. Reader lines 2451--2460 correctly calculates that the displayed zero-based clause places the second argument at odd offsets, lists possible repairs without selecting one, and notes that the theorem chain does not depend on the sentence.

- M09 — PASS. Reader lines 2462--2479 give the exact ETL closure and Gamma(S,j,N_i): root label, depth-indexed argument position, continuation-production edge, selected-argument truth test, and child nonterminal. Terminal productions are kept outside continuation edges and handled by the separate finite-witness condition.

- M10 — PASS. Reader lines 2481--2490 define negated-grammar fulfillment from maximum finite-tree depth and distinguish it from U fulfillment. Reader lines 2530--2549 give singleton frontier initialization, exact layer update, and emptiness somewhere within the guessed period.

- M11 — PASS. Journal p. 748 identifies only an error in a theorem used by the conference proof. Reader lines 1874--1881 and 2550--2556 and source-note lines 939--946 do not assert a precise bad inference or unique repairing lemma.

- M12 — PASS. Source-note lines 880--905 accurately classify each proof as printed proof, proof sketch, asserted induction, abbreviated cases, or brief replacement. Reader lines 2414--2420 preserve those distinctions and expressly state that the source proof is not automata-theoretic. No Sistla--Clarke Büchi construction is asserted.

- M13 — PASS. Shared Part IX lines 693--708 use exactly L(U) subseteq L(U,X) subseteq L(U,S,X), with the left language supplying PSPACE-hardness and the right language the PSPACE upper bound.

- M14 — PASS. Reader lines 1950--1959 retain existential R-truth. Shared Part IX lines 796--808 obtain universal model checking by searching for a path satisfying the negation and invoking deterministic-polynomial-space closure under complement.

- M15 — PASS. The five-part terminology rule is satisfied locally for acceptable subsequence and ambient subscripts at reader lines 2019--2050, source truth set and U fulfillment at 2268--2297, the grammar-indexed constructor at 2422--2449, and Gamma at 2468--2479. Each is exactly defined, typed, distinguished from nearby notions, and used.

- M16 — PASS. Source-note lines 119--145 place structure-level init/final/range/size on printed p. 735, the conclusion only on p. 748, and references on pp. 748--749. This matches the visual images.

- M17 — PASS. Conference p. 160's formal validity definition is recorded at reader lines 1960--1972 and source-note lines 256--265; the journal-relative status remains reconstruction. Reader lines 1874--1881 limit the correction notice to an unidentified theorem used in the conference regular-operator proof.

- M18 — PASS. Reader lines 2000--2017 reproduce Lemma 3.2's equal initial lengths, pointwise prefix valuation equality, zero-prefix first-valuation condition, equal recurring range, and start truth equivalence. Lines 2071--2105 reproduce Lemma 3.3's acceptable input/output, all-represented-position hypothesis, every-intermediate-supersequence quantifier, surviving-position scope, and strict/non-strict conflict. Lines 2183--2190 reproduce Lemma 3.6's finite subsequence containing the current state, length bound, every-intermediate-supersequence quantifier, and preservation at that state.

- M19 — PASS. Reader lines 2251--2266 state that each Figure 2 diamond is one tape-cell position, a complete BI-to-EI traversal is one instantaneous description, repeated traversals form a computation, and journal terminal configurations persist forever without tape changes. Source-note lines 926--927 separately record conference p. 164's halting language.

- M20 — PASS. Reader lines 2340--2352 define source model periodicity exactly for i in N and positive p by equality of complete valuations for every k >= i and distinguish it from source-truth-set equality, U discharge, and negated-grammar discharge.

- M21 — PASS. Shared Part IX lines 761--808 return a finite product path plus a nonempty product cycle, whose infinite unfolding is the counterexample. No undefined periodicity term is used.

- M22 — PASS. Reader lines 2468--2479, source-note lines 755--766, and source-presentation lines 303--305 call Gamma only the source's labelled tree or tree. No proof-tree, derivation-tree, or continuation-tree synonym is introduced.

- M23 — PASS. Against the current charter's retained M01--M15 and round-two M16--M22 obligations, every specified repair is present on the frozen round-four objects and none weakens C1--C9 or I1--I15. This disposition is based on the current charter, primary pages, and current artifacts; no prohibited earlier transcript or ledger was consulted.

- M24 — PASS. Reader lines 1975--1996 give p. 735's unique maximal final suffix, exact sequence decomposition, and structure-level init, final, range, and size before their use in Lemmas 3.1--3.2.

- M25 — PASS. Reader lines 2019--2050 define p. 736's acceptable-subsequence init, final, range, and size relative to ambient S. Lines 2025--2033 explicitly make the S-subscript eliminable and metalinguistic, explain its necessity and nonredundancy, and lines 2042--2050 and 2079--2092 use it.

- M26 — PASS. Reader lines 2051--2066 preserve the literally strict preparatory acceptable-union inequality, its null/null failure, and proof-supported non-strict subadditivity. Lines 2068--2071 define mu(f) before Lemma 3.3 as the number of F occurrences.

- M27 — PASS. Reader lines 2126--2159 give length(p') <= length(f) card(N), C subseteq N, restricted strong connectivity, the connecting edge, initially empty labels at every node in p' or C, increasing-subformula-length processing, all four exact iff rules, and acceptance iff f is in the start label.

- M28 — PASS. handbook.bib lines 2245--2258 give the separate and accurate SistlaClarke1982 record; lines 2260--2274 give SistlaClarke1985. Reader conference claims cite SistlaClarke1982 at lines 1873--1880, 1960--1962, 2260--2261, and 2555--2556; journal claims cite SistlaClarke1985 separately.

- M29 — PASS. Every current-charter round-two repair obligation M16--M23 remains present; the preparatory strict-sign conflict is exact at reader lines 2051--2066 and source-note lines 310--331 and 386--406; no retained criterion, invariant, or mandatory check was weakened.

- M30 — PASS. Reader lines 2258--2266 pinpoint the journal sentence to printed p. 741, the conference sentence to p. 164, and the broader journal reduction to pp. 741--742. Source-note lines 570--577 preserve the same distinction.

- M31 — PASS. Reader lines 2135--2159 exactly give empty initialization, increasing-length processing, atomic/negation/conjunction/F iff rules, and start-label acceptance. Lines 2165--2182 preserve the paper's literal strong-connectivity and entry-edge checks, give the concrete q_0,c,d false-acceptance instance, and own the positive directed-cycle condition solely as a handbook correction. Source-presentation lines 235--251 agree.

- M32 — PASS. Reader lines 2201--2230 give exact P_1/P_2, g_1/g_2/g_3, f_x, h_1/h_2/h_3, f-prime, and f-double-prime definitions and L(F,X) preservation. Lines 2232--2247 give both self-loop-sensitive pure-U replacements and Lemma 4.2's exact finite-stuttering use.

- M33 — PASS. Reader lines 2298--2312 make Lemma 4.5 delete s_i through s_(j-1), retain s_j, restrict the valuation to retained state tokens, and preserve the truth set of every common token. Lines 2314--2338 give every Lemma 4.6 hypothesis and both conclusions (a) and (b), with their exact index ranges.

- M34 — PASS. Reader lines 2376--2412 give the Boolean, X, U, and direction-sensitive S recurrences, initial-since equivalence, saved loop-entry equality, within-period U discharge, present/next/loop-entry storage plus counters, nondeterministic linear-space claim, and Savitch conversion.

- M35 — PASS. Reader lines 2481--2511 give Lemma 5.2's added negated-grammar fulfillment hypothesis, both inherited Lemma 4.6 conclusions, and the distinct obligations in Theorem 5.3. Lines 2512--2549 give Theorem 5.4's exact continuation-or-terminal iff rule, singleton frontier initialization, exact present-to-next nonterminal update, and emptiness within the period.

- M36 — PASS. The label sets are locally defined, typed, distinguished from semantic truth sets, and used at reader lines 2135--2163. Lemma 4.3's auxiliary formula names receive definition, standing, nonredundancy, and assembly use at lines 2201--2230. A/B receive exact guessed-set standing and use at lines 2376--2412. Varphi receives exact finite-set definition, standing, distinction from valuation and Gamma, and finite-tree use at lines 2530--2549.

- M37 — PASS. All supported repair obligations encoded by M24--M36 are present on the common corrected round-four hashes. The reader and source records distinguish printed defects from handbook corrections, preserve all source qualifications, and introduce no unsupported strengthening or silent authorial repair. The corrected source-presentation tuple abbreviation at lines 287--303 is now locally defined and satisfies the terminology rule. No earlier criterion, invariant, or mandatory check is weakened.

## Final disposition

No discrepancy remains between the visually read journal/conference pages and the frozen reader subsection, shared Part IX claims, bibliography, source note, or corrected source-presentation ledger within the chartered scope. There is no source-fidelity blocker, uncertainty, unread source page, or hash mismatch. The source-fidelity seat therefore ACCEPTS the corrected round-four N-c-012.d snapshot, subject only to the explicit I15 downstream-gate limitation.
