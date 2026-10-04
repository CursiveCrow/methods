REVISE

# Round-four adversarial publication and AGENTS review

Stable reviewer identifier: /root/r4_adversarial_publication

Runtime model/version disclosure: no exact runtime model or version identifier was exposed to this seat. The instructions exposed only the generic Codex/GPT-5 identity.

Review scope: the corrected, controlling round-four snapshot in the charter, including handbook/parts/p09/presentations/n-c-012.tex lines 1851--2589; the necessary local LTL context and the two named theorems in handbook/parts/p09/logic-in-computer-science.tex; the two Sistla--Clarke bibliography records; the complete source note; and the N-c-012.d source-presentation record. I did not inspect ledger.md, transcript/chair.md, any round-one, round-two, or round-three transcript, or any other round-four transcript or verdict. I did not contact another seat. I ran no test, test harness, automated checker, repository script, TeX command, build, handbook rendering, or handbook-PDF inspection.

## Frozen-object verification

All ten corrected round-four hashes were freshly recomputed and matched the charter:

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

## Direct source reading

After the corrected freeze was issued, I freshly and visually read all seventeen journal images, journal-page-01.png through journal-page-17.png, corresponding one-for-one to printed pp. 733--749, and all ten conference images, conference-page-01.png through conference-page-10.png, corresponding one-for-one to printed pp. 159--168. Thus all twenty-seven source pages were visually read. I also inspected the enlarged acceptable-subsequence crop, the enlarged p. 742 exponent crop, and the full p. 745 image. The page images, not OCR or the source note, supplied the evidence for the source claims below.

## Must-fix findings

### F1. The reader uses the source closure \(\operatorname{SF}(f)\) before defining it

The newly supplied Theorem 3.5 certificate tells the reader to process
\(g\in\operatorname{SF}(f)\) at handbook/parts/p09/presentations/n-c-012.tex:2135--2138. The reader does not define \(\operatorname{SF}(f)\), its single-negation closure, or double-negation convention until lines 2268--2276, in the later Section 4 discussion.

This is not the source order. Printed journal p. 735, visible in journal-page-03.png, defines \(SF(f)\) and its negation closure before Section 3 and before Theorem 3.5; the source note likewise records the definition at spec/research/p09-sistla-clarke-1985-source-note.md:216--226. The round-four reader therefore leaves a load-bearing input set undefined at the point where the certificate first uses it. This violates definition-before-use and the exact-type requirement in C9/I12, and prevents a clean M27/M31 disposition even though the four displayed labelling rules themselves match printed pp. 738--739.

Required repair: move or restate the source closure definition before the Theorem 3.5 certificate, or introduce an exact forward-local definition there. It must retain the source's subformula-plus-single-negation content, double-negation elimination, and the distinction between the closure bound and the later realized-truth-set count.

### F2. The certificate's start symbol \(q_0\) is not bound to the reader's supplied start state

The reader defines the input start state as \(\delta\in N\) at handbook/parts/p09/presentations/n-c-012.tex:1945--1954. In the Theorem 3.5 paragraph it then says only that \(p'\) starts at “the supplied start state” at lines 2126--2134, but acceptance is suddenly written
\(f\in\operatorname{label}(q_0)\) at lines 2158--2159. No clause defines \(q_0:=\delta\) or otherwise binds \(q_0\) before this use. The later counterexample's set \(N=\{q_0,c,d\}\) at lines 2167--2174 is a new, example-local binding and cannot retrospectively type the general certificate.

Printed journal pp. 738--739, visible in journal-page-06.png and journal-page-07.png, use \(q_0\) for the certificate's supplied starting node and accept when \(f\in label(q_0)\). A source-faithful reader can therefore fix this simply by naming the supplied start node \(q_0\) when the certificate is introduced, or by using the already-defined \(\delta\) consistently.

The same unbound transition appears in the supporting records: spec/research/p09-sistla-clarke-1985-source-note.md:423--448 moves from an unnamed start node to \(q_0\), and spec/research/p09-source-presentations-lot2-3.md:235--243 does the same. This is consequently a cross-file definedness defect, not an isolated typography complaint. It bears directly on the exact “start label” required by M27/M31.

### F3. The ETL argument-tuple arity changes from \(n\) to an unintroduced \(q\)

The reader fixes terminals \(a_1,\ldots,a_n\) and defines the constructor
\(N_j(f_1,\ldots,f_n)\) at handbook/parts/p09/presentations/n-c-012.tex:2423--2439. It continues to use the \(n\)-tuple in the \(\Gamma\) definition at lines 2468--2479. Lemma 5.2 and Theorem 5.4 then change without a binder to
\(N_u(f_1,\ldots,f_q)\) and \(N_j(f_1,\ldots,f_q)\) at lines 2484--2492 and 2519--2540. No ETL arity \(q\) is introduced. Worse, \(q\) was most recently used as the graph start node in the Lemma 4.3 reduction at lines 2223--2226, so the later formula index is ill-typed if that binding is carried forward.

Printed journal p. 745 first presents an \(n\)-terminal grammar and later locally says “let \(N_i(f_1,\ldots,f_q)\) be a formula” before defining \(\Gamma(S,j,N_i)\). Thus the source itself supplies a local generic \(q\)-ary formula at the point where it changes letters. The handbook omitted that binding. The source note has the same unsupported switch from \(n\) at spec/research/p09-sistla-clarke-1985-source-note.md:710--718 to \(q\) at lines 755--759 and thereafter.

The corrected compact source-presentation object does now define
\(\bar f:=(f_1,\ldots,f_q)\) locally at spec/research/p09-source-presentations-lot2-3.md:284--303; that withdrawn-freeze defect is repaired in that object. It does not define the reader's or source note's free \(q\).

Required repair: use \(n\) consistently, or explicitly introduce \(q\) as the number of arguments/terminals of the grammar and bind \(N_i(f_1,\ldots,f_q)\) before its first use. If a new tuple abbreviation is added to the reader or source note, it must receive the same local eliminable/metalinguistic standing, nonredundancy, necessity, and actual use already supplied in the corrected compact presentation.

These three findings are reader-visible formal publication defects. Because this board's acceptance rule treats any must-fix definedness failure as dispositive, the verdict is REVISE even though the substantive source reconstruction is otherwise unusually complete.

## C1--C9 disposition

- C1 — PASS. Journal p. 733 and p. 749, conference p. 159, reader lines 1853--1881, bibliography lines 2245--2274, and source-note lines 35--117 agree on author order, plural title, JACM 32(3), July 1985, pp. 733--749, DOI, ISSN, receipt history, distinct STOC object, hashes/provenance, and the limited rights inference.

- C2 — PASS. Journal pp. 734--735 and conference p. 160 support reader lines 1883--1973. The fragments, inclusive \(U/S\), satisfiability, existential \(R\)-truth, universal counterexample relation, and the journal-relative reconstruction of validity are kept distinct.

- C3 — REVISE. The Section 3 definitions, bounds, strict/non-strict conflicts, Lemmas 3.1--3.6, Theorems 3.4--3.7, diamond reduction, literal labels, singleton counterexample, and handbook-owned cycle repair are substantively source-exact at reader lines 1975--2193. F1 and F2 nevertheless leave the certificate's closure and start label undefined at first use.

- C4 — PASS. Journal pp. 740--745 and reader lines 2195--2420 agree on the complete Lemma 4.3 construction, both pure-\(U\) cases, stuttering boundary, p. 741 journal \(2S(n)\) versus conference p. 164 \(S(n)\), source truth sets, the p. 742 count, fulfillment, Lemmas 4.5--4.6, Theorem 4.7, and all five direction-sensitive search checks.

- C5 — REVISE. Apart from F3, journal pp. 745--748 and reader lines 2422--2556 agree on finite/infinite ETL semantics, handbook-supplied finite-word typing, the parity conflict, closure, \(\Gamma\), Lemmas 5.1--5.2, Theorems 5.3--5.4, the positive rule, negative frontier, and correction boundary. The unbound \(q\) prevents the constructor and the two exact rules from being fully typed.

- C6 — PASS. Journal p. 748, reader lines 2558--2588, and shared Part IX lines 693--708 and 796--808 preserve all Table I classes, the Theorem 4.1/\(L(U,X)\) distinction, the two containments, and complement-based universal model checking.

- C7 — PASS. The full conference/journal comparison at source-note lines 907--946 agrees with the twenty-seven pages. Reader lines 1872--1881, 2249--2266, and 2551--2556 do not import conference numbering, \(S(n)\), halting language, or the uncorrected Section 5 proof, and do not claim that a unique journal lemma was the identified repair.

- C8 — REVISE. Bibliography, locators, page map, proof-status table, rights boundary, and corrected compact \(\bar f\) definition pass. F2 is repeated in the source note and compact source record, and F3 is repeated in the source note, so the source records and reader are not yet fully publication-consistent.

- C9 — REVISE. The prose is independently worded and most terms are well typed, but F1--F3 are definition-before-use/type failures. They are not cured by mathematical inferability from later prose.

## I1--I15 disposition

- I1 — PASS. This review used only direct visual source reading, mathematical reasoning, prose inspection, targeted text reads, and permitted SHA-256 verification.
- I2 — PASS. Every frozen object matches the corrected round-four hash.
- I3 — PASS. All seventeen journal and ten conference pages were freshly visually read.
- I4 — PASS. The p. 742 crop reads \(2^{\operatorname{length}(f)}\); p. 745 visibly contains both ETL source defects.
- I5 — PASS. Journal and conference versions remain distinct, and no unique bad inference or unique repairing lemma is invented.
- I6 — PASS. All language, semantic, problem-quantifier, and validity boundaries remain distinct.
- I7 — PASS. Structure size, maximal final suffix, ambient-relative acceptable measures, and both strict-sign conflicts are exact.
- I8 — PASS. The next distance, closure/type count, and inclusive fulfillment endpoint are exact.
- I9 — PASS. Theorem 4.7's bounds, every-position obligations, \(Ff\) move, initial-since rule, and Savitch step are visible.
- I10 — REVISE. The ETL mathematics is otherwise exact, but F3 prevents the grammar constructor and later rules from having one consistently bound argument arity.
- I11 — PASS. The source's heterogeneous proof strengths remain calibrated, and no Sistla--Clarke Büchi construction is asserted.
- I12 — REVISE. F1--F3 violate local definition-before-use/exact-standing requirements. The specifically audited technical names otherwise satisfy the five-part rule.
- I13 — PASS. Independence restrictions were observed.
- I14 — PASS. This transcript returns REVISE because the snapshot is not clean.
- I15 — PASS. The source-presentation status at lines 326--345 keeps topic admission, Part IX, build, rendered inspection, human review, book completion, and user acceptance open.

## M01--M37 disposition

- M01 — PASS. Journal p. 742 and journal-page-10-bound-crop.png print \(2^{\operatorname{length}(f)}\); reader lines 2282--2288 preserve it and reject the doubled exponent.

- M02 — PASS. No validity clause appears on journal pp. 734--735. Reader lines 1960--1973 explicitly identify the universal clause as a reconstruction and cite conference p. 160 separately.

- M03 — PASS. Journal p. 742 and reader lines 2289--2297 require \(j\ge i\) and an inclusive witness \(i\le\ell\le j\).

- M04 — PASS. Journal pp. 736--737 and reader lines 2050--2066 and 2094--2114 preserve both printed strict signs, the null failures, the proof-supported non-strict uses, and Theorem 3.4's non-strict conclusion.

- M05 — PASS. Journal p. 741 says \(2S(n)\); conference p. 164 says \(S(n)\). Reader lines 2258--2266 cite both separately.

- M06 — PASS. Reader lines 2354--2374 and 2503--2511 preserve the exact Theorems 4.7 and 5.3 bounds, positive-period standing inherited from lines 2340--2352, equal truth sets, and both every-periodic-position fulfillment obligations.

- M07 — PASS. Journal p. 745 prints finite or infinite and then an unrestricted nonnegative index. Reader lines 2435--2446 labels the finite represented-index restriction as handbook-supplied typing.

- M08 — PASS. Journal p. 745 and reader lines 2451--2460 preserve the exact grammar example, the printed even-state sentence, the zero-based odd-offset consequence, and the absence of an authorial repair.

- M09 — PASS. Reader lines 2462--2479 give the exact grammar closure and every continuation edge of \(\Gamma(S,j,N_i)\), while terminal productions remain in the separate finite-witness condition.

- M10 — PASS. Reader lines 2481--2490 and 2530--2549 distinguish finite-tree maximum-depth fulfillment from until fulfillment and require the continuation set to become empty within the period.

- M11 — PASS. Journal p. 748, reader lines 1874--1881 and 2551--2556, and source-note lines 939--946 do not identify a precise bad inference or unique repairing lemma.

- M12 — PASS. The proof-status table at source-note lines 880--901 and reader lines 2107--2108, 2311--2312, 2414--2420, and 2501--2502 preserve the source's unequal proof granularity. Reader lines 2418--2420 and 2550--2552 do not attribute a Büchi construction to the article.

- M13 — PASS. Shared Part IX lines 693--708 gives
\(L(U)\subseteq L(U,X)\subseteq L(U,S,X)\), using the left inclusion for hardness and the right for the upper bound.

- M14 — PASS. Reader lines 1950--1959 and shared Part IX lines 796--808 keep source truth existential and derive universal model checking by searching \(\neg A\) and using polynomial-space closure under complement.

- M15 — PASS as to its named terms. Reader lines 2019--2050, 2277--2297, 2431--2449, and 2468--2479 define and distinguish acceptable subsequences, the eliminable ambient subscript, source truth sets, both fulfillment notions, the grammar constructor, and \(\Gamma\), and later use each. F1/F3 are separate binding failures and are recorded under C9/I12.

- M16 — PASS. Source-note page-map lines 119--145 place the structure measures on p. 735, the conclusion only on p. 748, and references on pp. 748--749.

- M17 — PASS. Conference p. 160's validity clause, journal pp. 734--735's omission, and the limited p. 748 correction notice are all now visible without conflation.

- M18 — PASS. Reader lines 1998--2017, 2071--2092, and 2185--2193 preserve the zero-prefix clause, acceptable input/output subsequences, every-intermediate-supersequence quantifiers, surviving-position scope, and the finite subsequence containing the current state, with the Lemma 3.3 sign conflict separately disclosed.

- M19 — PASS. Reader lines 2249--2266 preserves the tape-cell unit, complete BI-to-EI instantaneous-description traversal, repeated computation traversals, journal persistence convention, conference halting language in the source comparison, and the exact journal/conference distance.

- M20 — PASS. Reader lines 2340--2352 types \(i\in\mathbb N\), \(p>0\), and complete-valuation periodicity for every \(k\ge i\), distinct from truth-set equality and both fulfillment obligations.

- M21 — PASS. Shared Part IX lines 761--808 returns a finite product path and nonempty product cycle whose infinite unfolding is the counterexample and introduces no undefined periodicity name.

- M22 — PASS. The reader, source note, compact presentation, and charter use only the source's “labelled tree” or \(\Gamma\); no proof-tree, derivation-tree, or continuation-tree synonym occurs in the audited objects.

- M23 — PASS on the blind evidence permitted by the charter. Every repair obligation encoded by M16--M22 is visible and does not weaken M01--M15. I did not inspect the forbidden historical transcripts or ledger.

- M24 — PASS. Reader lines 1975--1996 gives the unique maximal suffix, exact decomposition, range, and structure size before Section 3 uses them.

- M25 — PASS. Reader lines 2019--2050 defines all acceptable-subsequence measures relative to \(S\) and gives the subscript's eliminability, metalinguistic standing, necessity, nonredundancy, and later use.

- M26 — PASS. Reader lines 2050--2071 gives the literal preparatory strict sign, null/null counterexample, proof-supported subadditivity, and defines \(\mu(f)\) as the \(F\)-occurrence count before Lemma 3.3.

- M27 — REVISE. The path bound, \(C\), restricted strong connectivity, entry edge, label domain/rules, and printed acceptance test are present at reader lines 2126--2159, but F1 and F2 leave \(SF(f)\) defined only later and \(q_0\) unbound to the supplied start. The requirement for an exact start label is therefore not met as publication prose.

- M28 — PASS. Bibliography lines 2245--2274 give separate, accurate conference and journal records. Direct conference claims cite SistlaClarke1982 and journal claims cite SistlaClarke1985.

- M29 — PASS on the blind evidence permitted by the charter. The explicitly encoded round-two repairs M24--M28 and all prior checks are materially present; no historical transcript or ledger was consulted.

- M30 — PASS. Reader lines 2258--2266 pin the journal sentence to p. 741, conference sentence to p. 164, and broader journal construction to pp. 741--742.

- M31 — REVISE. Reader lines 2135--2159 correctly starts labels empty, orders \(SF(f)\) by length, prints all four iff rules, and writes the source acceptance condition; lines 2165--2182 correctly preserve the literal graph checks, concrete false acceptance, and handbook-owned directed-cycle condition. F1/F2 nonetheless leave the processed closure and start symbol undefined at their first use.

- M32 — PASS. Reader lines 2201--2247 supplies \(\mathcal P_1/\mathcal P_2\), every \(g_i^x,f_x,h_i,f',f''\), the \(L(F,X)\) preservation, both self-loop-sensitive pure-\(U\) replacements, and the exact Lemma 4.2 role.

- M33 — PASS. Reader lines 2298--2338 deletes \(s_i,\ldots,s_{j-1}\), retains \(s_j\), preserves every common token's truth set, and gives every Lemma 4.6 hypothesis and both conclusions.

- M34 — PASS. Reader lines 2376--2412 gives the exact \(X,U,S,\land,\neg\) recurrences, direction-sensitive since rule, initial-since check, loop-entry equality, within-period discharge, three-set/two-counter storage, and Savitch step.

- M35 — REVISE. The negated-grammar hypothesis, inherited conclusions, positive continuation/terminal iff rule, singleton initialization, frontier update, and emptiness check are mathematically present at reader lines 2481--2549. F3 leaves their argument tuple \(f_1,\ldots,f_q\) without a local arity binder, so they are not exactly typed.

- M36 — PASS as to the four named technical devices. Reader lines 2135--2163 defines label and its eliminable certificate standing; lines 2201--2230 defines and distinguishes the Lemma 4.3 auxiliaries; lines 2376--2382 defines successive guesses \(A,B\); and lines 2530--2549 defines, distinguishes, and uses \(\varphi\). F2 concerns the unbound start argument supplied to label, not label's finite-set standing itself.

- M37 — REVISE. Every substantive round-three repair listed in the current compact presentation is reader-visible: labels at 2135--2159, the singleton gap/correction at 2165--2182, Lemma 4.3 at 2201--2247, Lemmas 4.5--4.6 at 2298--2338, Theorem 4.1 recurrences at 2376--2412, Lemma 5.2 at 2481--2502, Theorem 5.4 at 2512--2549, and the p. 741 pinpoint at 2258--2266. The corrected compact \(\bar f\) definition is also visible at source-presentation lines 284--303. But F1--F3 mean those repairs did not yield a clean common snapshot and weakened C3/C5/C8/C9, I10/I12, and M27/M31/M35 at the level of reader-visible binding and exact types.

## Final disposition

The source identity, page reconciliation, mathematical bounds, source defects, source-versus-handbook ownership, proof calibration, citations, and all substantive round-three repairs are present. The snapshot is nevertheless not publication-ready because three load-bearing symbols/arity transitions remain undefined where used, two of them repeated across the source records. Under the charter's no-uncertainty/no-must-fix acceptance rule, N-c-012.d remains open and requires a newly frozen review after F1--F3 are repaired consistently.
