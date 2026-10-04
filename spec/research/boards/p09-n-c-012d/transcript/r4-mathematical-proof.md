REVISE

# Round-four mathematical/proof review: `N-c-012.d`

## Reviewer, isolation, and method

- Stable agent identifier and canonical task name: `/root/r4-mathematical_proof`.
- Runtime model/version: not exposed to this seat.
- This is an independent mathematical/proof verdict on the corrected controlling round-four snapshot. I did not inspect `ledger.md`, `transcript/chair.md`, any round-one, round-two, or round-three transcript, or any sibling round-four transcript or verdict. I did not contact another seat and did not delegate any work.
- I used only direct visual source reading, mathematical reconstruction, prose inspection, targeted read-only text access, and SHA-256 verification. I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or builds.

## Frozen-object identity

All ten controlling SHA-256 hashes were reverified after the corrected freeze and match the charter exactly:

| Frozen object | Verified SHA-256 |
|---|---|
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf` | `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5` |
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf` | `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png` | `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png` | `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-04-acceptable-crop.png` | `C267D4B4DF785F9A7E82123B068662E45D7E2C87CB18C24D7B8EB0B875AF413B` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `45E2B1F4A97B1049247FD198CDF69C67794D129AEB28582FE595DC34EDF7ABD8` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` |
| `handbook/bib/handbook.bib` | `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B` |
| `spec/research/p09-sistla-clarke-1985-source-note.md` | `1E734EF089EEA077DE90229411726D85708A102D914EFE4F7956B7DDE9EE9094` |
| `spec/research/p09-source-presentations-lot2-3.md` | `40F0AE94BB9B763F941B421F63854B17A426C1989084F6262ACD59071C0A7E8D` |

The corrected last object now defines `\bar f:=(f_1,\ldots,f_q)` locally at `spec/research/p09-source-presentations-lot2-3.md:284-305`; the withdrawn-freeze undefined-abbreviation defect is repaired.

## Complete visual source reading

I visually read with `view_image` every one of the seventeen journal page images `journal-page-01.png` through `journal-page-17.png`, corresponding to printed pp. 733--749, and every one of the ten conference page images `conference-page-01.png` through `conference-page-10.png`, corresponding to printed pp. 159--168. Thus all 27 source pages were freshly visually read on this corrected snapshot. I also inspected the enlarged p. 736 acceptable-subsequence derivative, the enlarged p. 742 exponent derivative, and the enlarged p. 745 page. The page images, not OCR or a prior note, supplied the source judgments below.

## Must-fix mathematical/source-reconstruction defect

### F1. The Theorem 3.5 prefix rule incorrectly makes inclusive `F` strict

The reader correctly states that the journal defines

\[
Ff:=\top U f
\]

and that `U`, hence `F`, permits its right-hand witness at the current point (`handbook/parts/p09/presentations/n-c-012.tex:1891-1926`). This is exactly the journal clause on printed pp. 734--735: the `U` witness satisfies (k\ge i).

The journal's printed Theorem 3.5 rule on p. 738 then says, in its own prose, that for a prefix node (x), a node (y) in (p') is “after (x).” The source itself supplies strong contextual evidence that this wording is non-strict: in the `F` case of the Lemma 3.3 proof on p. 737, it infers from (S,t_n\models Ff_1) that there is an (s_j) “appearing after (t_n)” satisfying (f_1). Under the p. 735 semantics that inference includes the case (s_j=t_n). At minimum, therefore, the source's word “after” cannot safely be strengthened to the unambiguously strict word “later” without a disclosed reconstruction or correction.

The frozen artifacts nevertheless make precisely that strict strengthening:

- reader: the `F` rule requires “(y) later than (x) in (p')” at `handbook/parts/p09/presentations/n-c-012.tex:2148-2155`;
- source note: the rule requires a node “later in (p')” at `spec/research/p09-sistla-clarke-1985-source-note.md:423-452`, especially lines 443--444;
- source-presentation record: it says “at a later prefix node” at `spec/research/p09-source-presentations-lot2-3.md:235-244`, especially lines 241--242.

That strict rule is mathematically incomplete for the exact inclusive semantics. Consider the total (R)-structure

\[
N=\{q_0,d\},\qquad
R=\{(q_0,d),(d,d)\},\qquad
\eta(q_0)=\{A\},\quad \eta(d)=\varnothing,
\]

with start state (q_0), and let

\[
f=A\land FA.
\]

The unique infinite path is (q_0,d,d,\ldots). It satisfies (f) at (q_0): (A) is true there and (FA) has the permitted current-point witness (k=0). Under the frozen strict rule, however, the only recurrent directed-cycle choice is (C=\{d\}); every guessed prefix begins with (q_0) and subsequently contains only (d). No node of (C), and no prefix node strictly later than (q_0), has (A) in its label. Hence (FA\notin\operatorname{label}(q_0)), so (f\notin\operatorname{label}(q_0)), and the stated verifier rejects this true instance.

This defect is independent of, and not repaired by, the correctly identified loopless-singleton defect at `handbook/parts/p09/presentations/n-c-012.tex:2165-2182`. Requiring a directed cycle in (C) repairs the existence of the recurrent infinite suffix; it does not restore a current-position witness omitted by the prefix `F` rule.

Required repair: the reader, source note, and source-presentation record must preserve the printed wording and explicitly reconcile it with inclusive `F`. The mathematically sound prefix clause must allow the current occurrence---equivalently, it must include (g_1\in\operatorname{label}(x)) or quantify over a prefix occurrence at or after the occurrence of (x). Because the paper prints only “after,” the artifact must state whether this is a source-context reading supported by pp. 735 and 737 or a separately owned handbook correction. It must not silently call the relation strict. The directed-cycle correction must remain separately owned and unchanged.

This is a must-fix failure of C3, C8, C9, I6, M31, and M37. It prevents `ACCEPT` even though the remaining audited material is clean.

## Criterion-by-criterion disposition

- **C1 — PASS.** The journal identity, plural title, Sistla-before-Clarke order, JACM 32(3), July 1985, pp. 733--749, DOI, ISSN, affiliations, receipt/revision/acceptance history, CMU provenance, distinct ten-page STOC object, hashes, and rights boundary agree with journal pp. 733 and 749, conference pp. 159--168, reader lines 1853--1874, source-note lines 1--145, and bibliography lines 2245--2274. No republication licence is inferred from public access.
- **C2 — PASS as to the stated definitions and problem quantifiers.** Reader lines 1883--1973 preserve the primitive/derived syntax, fragment standing, inclusive `U/S`, structures, interpretations, existential (R)-truth, universal-program counterexample relation, and the journal-relative reconstructed validity clause. The strict prefix-label defect is recorded separately under C3/I6 because it is a misuse of the otherwise correctly stated inclusive semantics.
- **C3 — REVISE.** Reader lines 1975--2193 otherwise accurately reconstruct `init/final/range/size`, ambient-relative acceptable subsequences, Lemmas 3.1--3.3, both strict-sign defects and the proof-supported non-strict forms, Theorems 3.4--3.7, Figure 1, the complete certificate, the loopless-singleton false acceptance, and the handbook-owned directed-cycle condition. But lines 2148--2155 incorrectly replace the source's contextually non-strict “after” by strict “later than,” making the displayed verifier incomplete; see F1.
- **C4 — PASS.** Reader lines 2195--2412 contain the exact Lemma 4.3 construction, both pure-`U` replacements and Lemma 4.2 boundary, Figure 2 unit and terminal convention, journal p. 741 `2S(n)` versus conference p. 164 `S(n)`, the p. 742 truth-set count, fulfillment, exact Lemmas 4.5--4.6, Theorem 4.7 bounds and all-position obligations, all five directional Theorem 4.1 recurrences, loop closure, storage, and Savitch transfer.
- **C5 — PASS.** Reader lines 2422--2556 preserve the ETL grammar and disjoint nonterminals, normalization, exact finite/infinite typing qualification, parity conflict, closure, labelled tree `Gamma`, terminal/continuation separation, Lemmas 5.1--5.2, distinct fulfillment obligations, Theorem 5.3 bounds, Theorem 5.4 positive and negative update rules, singleton frontier initialization, within-period emptiness, input encoding, and the correction-notice boundary.
- **C6 — PASS.** Reader lines 2558--2588 reproduce every Table I class, distinguish Theorem 4.1 from the `L(U,X)` table row, and support the exact containment argument in shared Part IX lines 693--708. Shared Part IX lines 761--809 correctly pass from an existential path satisfying `not A` to universal satisfaction by complement, return a finite product path plus a nonempty cycle, and state combined/fixed-formula resources at the proper strength.
- **C7 — PASS.** The reader, source note lines 907--946, and source-presentation lines 187--215 keep the journal controlling, distinguish the p. 164/p. 741 distance, numbering, periodic hypotheses, terminal behavior, and replacement Section 5 machinery, and do not identify a precise erroneous inference or one unique repairing lemma.
- **C8 — REVISE only for F1.** The bibliography, citation locators, page map (`spec/research/p09-sistla-clarke-1985-source-note.md:119-145`), proof-status table (lines 880--902), version comparison (lines 907--946), corrected tuple abbreviation, and rights statements are otherwise source-accurate and mutually consistent. The source note and source-presentation record repeat the unjustified strict “later” rendering at the locators given in F1.
- **C9 — REVISE only for F1.** Definitions otherwise precede use, types and quantifiers are explicit, the terminology rule is met locally, and the prose is independently reconstructed. The strict prefix quantifier is an unsupported strengthening that contradicts the stated inclusive semantics and produces the concrete false rejection above.

## Invariant disposition

- **I1 — PASS.** Review mode remained source reading, reasoning, and prose inspection only; no prohibited execution or rendering occurred.
- **I2 — PASS.** All ten corrected round-four hashes match.
- **I3 — PASS.** All seventeen journal and all ten conference pages were freshly visually read.
- **I4 — PASS.** The enlarged p. 742 image confirms (2^{\operatorname{length}(f)}); the p. 745 image confirms both the finite/infinite index defect and the even/odd conflict.
- **I5 — PASS.** The journal controls; numbering and proof machinery are not interchanged; the correction notice is not overidentified.
- **I6 — REVISE.** The language, fragment, decision-problem, and validity distinctions are explicit, but the strict “later than” prefix rule is incompatible with the same artifact's inclusive `F` semantics. See F1.
- **I7 — PASS.** `size`, unique maximal suffix, ambient-relative measures, and both strict/non-strict conflicts are exact.
- **I8 — PASS.** The `2S(n)`/`S(n)` difference, closure/type-count distinction, and inclusive fulfillment endpoint are exact.
- **I9 — PASS.** Theorem 4.7 has all three distinct conditions, exact bounds, every-position discharge, the `Ff` move for past `S`, the initial-since rule, and Savitch.
- **I10 — PASS.** All listed ETL conventions, machinery, bounds, typing ownership, and parity uncertainty are exact.
- **I11 — PASS.** Sketches, asserted inductions, abbreviated cases, and brief replacements remain distinguished; no Sistla--Clarke Buchi construction is claimed.
- **I12 — PASS.** Every audited handbook-introduced technical name has a local eliminable definition/standing, necessity, distinction, and later use; detailed checks appear under M15 and M36.
- **I13 — PASS.** Independence and file-ownership restrictions were observed.
- **I14 — PASS as a decision rule.** The single must-fix defect causes this `REVISE`; it is not outvoted by the otherwise clean material.
- **I15 — PASS.** Neither the artifacts nor this verdict claim closure beyond the `N-c-012.d` topic-level gate; broader publication, build, rendered, human, and user gates remain separate.

## Mandatory-check disposition, M01--M37

- **M01 — PASS.** Journal p. 742 and the enlarged derivative print (2^{\operatorname{length}(f)}), never (2^{2\operatorname{length}(f)}); reader lines 2281--2288 are exact.
- **M02 — PASS.** Journal pp. 734--735 have no standalone validity definition; reader lines 1960--1973 label the universal clause reconstruction, with conference p. 160 separately cited.
- **M03 — PASS.** Reader lines 2290--2297 use (j\ge i) and a witness (i\le\ell\le j).
- **M04 — PASS.** Journal p. 736 prints `<` in both places; the null/null and atomic null counterexamples, following `<=` uses, and Theorem 3.4's `<=` conclusion appear at reader lines 2050--2115.
- **M05 — PASS.** Journal p. 741 prints `2S(n)` and conference p. 164 prints `S(n)`; reader lines 2258--2266 keep both locators distinct.
- **M06 — PASS.** Reader lines 2354--2374 and 2502--2511 preserve every bound, quantifier, and every-periodic-position obligation in Theorems 4.7 and 5.3.
- **M07 — PASS.** Reader lines 2431--2446 identify the printed finite/infinite string plus unrestricted index and own the represented-position restriction as handbook typing.
- **M08 — PASS.** Reader lines 2451--2460 preserve `N_0 -> a_1 a_2 N_0`, the printed even-state sentence, the zero-based odd-offset consequence, and the absence of an authorial repair.
- **M09 — PASS.** Reader lines 2462--2479 give the exact closure and each `Gamma(S,j,N_i)` continuation edge, with terminal productions handled outside the tree.
- **M10 — PASS.** Reader lines 2481--2511 distinguish finite-tree depth from until fulfillment; lines 2530--2549 give singleton initialization, the exact frontier update, and within-period emptiness.
- **M11 — PASS.** Reader lines 1874--1881 and 2551--2556 and source-note lines 939--946 do not name the bad inference or a unique repair.
- **M12 — PASS.** Reader lines 2107--2108, 2311--2312, 2414--2420, and 2501--2502 agree with the source-note proof-status table; no Buchi proof is attributed to Sistla--Clarke.
- **M13 — PASS.** Shared theorem lines 693--708 uses exactly (L(U)\subseteq L(U,X)\subseteq L(U,S,X)) for hardness and membership.
- **M14 — PASS.** Reader lines 1950--1959 and shared lines 796--809 retain existential source truth and derive universal model checking using `not A` and deterministic-PSPACE complement closure.
- **M15 — PASS.** `Acceptable subsequence` is source-defined and distinguished from ordinary subsequence at reader lines 2019--2023; the subscripted ambient operations satisfy all five terminology conditions at lines 2025--2050; source truth sets are exactly defined and distinguished at lines 2268--2289; the two fulfillment obligations are defined and distinguished at lines 2290--2297 and 2481--2491; the ETL constructor is typed, defined, distinguished from `U`, and used at lines 2422--2466; `Gamma` is exactly the source's labelled tree, distinguished from models/automata/proof objects, and used at lines 2468--2502.
- **M16 — PASS.** The source-note map puts `init/final/range/size` on p. 735, conclusion on p. 748, and references on pp. 748--749 (`spec/research/p09-sistla-clarke-1985-source-note.md:119-145`).
- **M17 — PASS.** Conference p. 160 validity is recorded; journal reconstruction and the unidentified conference-proof error boundary remain explicit.
- **M18 — PASS.** Reader lines 1998--2017, 2071--2105, and 2183--2192 preserve the zero-prefix clause, acceptable inputs/outputs, every-intermediate-supersequence quantifiers, surviving positions, current-state containment, and strict/non-strict defect.
- **M19 — PASS.** Reader lines 2249--2266 give one cell per diamond, one BI--EI traversal per instantaneous description, repeated traversals, and journal persistence. The source-note comparison at lines 914--937 separately records the conference halting convention.
- **M20 — PASS.** Reader lines 2340--2352 types (i\in\mathbb N), (p>0), and exact complete-valuation periodicity, separately from truth-set equality and both discharge notions.
- **M21 — PASS.** Shared Part IX lines 781--787 and 796--802 return a finite product path plus a nonempty product cycle and explain its infinite unfolding without inventing an undefined periodicity term.
- **M22 — PASS.** The reader, source note, corrected source-presentation subsection, and charter use only “labelled tree” or `Gamma`; none introduces `proof tree`, `derivation tree`, or `continuation tree` as a synonym.
- **M23 — PASS for every carried-forward requirement testable from the charter.** M01--M22's repaired objects are present without weakening. No forbidden earlier transcript or ledger was consulted.
- **M24 — PASS.** Reader lines 1975--1996 define the unique maximal suffix, exact decomposition, range, and size before later use.
- **M25 — PASS.** Reader lines 2019--2050 define all acceptable-subsequence operations relative to (S) and explicitly supply eliminability, metalinguistic standing, necessity, nonredundancy, and use.
- **M26 — PASS.** Reader lines 2050--2071 give the literal preparatory `<`, null/null failure, proof-supported `<=`, and define `mu` as the number of `F` occurrences before Lemma 3.3.
- **M27 — PASS.** Reader lines 2126--2159 contain the exact prefix bound, subset, induced strong-connectivity check, entry edge, empty initialization, increasing-length processing, all four printed forms, and acceptance in the start label. M31 records the separate strict-prefix defect in the handbook's rendering of “after.”
- **M28 — PASS.** Bibliography lines 2245--2258 contain the distinct accurate `SistlaClarke1982` record; direct conference statements use that record, while journal statements use `SistlaClarke1985` at lines 2260--2274.
- **M29 — PASS for the charter-enumerated round-two repairs.** M16--M28 remain present, and the preparatory strict-sign conflict is source-exact; no earlier mandatory item is weakened by those repairs.
- **M30 — PASS.** Reader lines 2258--2266 pinpoint journal `2S(n)` to p. 741, conference `S(n)` to p. 164, and the broader journal reduction to pp. 741--742.
- **M31 — REVISE.** Empty labels, increasing length, atomic/negation/conjunction rules, acceptance, literal strong connectivity and entry edge, the concrete singleton false acceptance, and the separately owned directed-cycle condition are all present at reader lines 2135--2182. The `F` prefix clause, however, is not mathematically exact: “later than” excludes the current witness permitted by pp. 734--735 and evidenced by the p. 737 use of “after.” See F1.
- **M32 — PASS.** Reader lines 2201--2247 preserve exact `P_1/P_2`, `g_1/g_2/g_3`, `f_x`, `h_1/h_2/h_3`, `f'`, `f''`, `L(F,X)` preservation, both self-loop cases, and Lemma 4.2's precise stuttering role.
- **M33 — PASS.** Reader lines 2298--2338 delete (s_i,\ldots,s_{j-1}), retain (s_j), preserve each common token, and state every Lemma 4.6 hypothesis and both conclusions with exact index ranges.
- **M34 — PASS.** Reader lines 2376--2412 preserve Boolean, `X`, `U`, direction-sensitive `S`, the initial-since rule, loop-entry equality, within-period discharge, three sets plus two counters, and Savitch.
- **M35 — PASS.** Reader lines 2481--2511 state Lemma 5.2's added hypothesis and both inherited conclusions; lines 2512--2549 contain the exact positive iff rule, singleton initialization, present-to-next frontier update, and within-period emptiness.
- **M36 — PASS.** `label` satisfies the five-part rule at reader lines 2135--2163; Lemma 4.3 auxiliaries at lines 2201--2230; successive guesses `A,B` at lines 2376--2382; and `varphi` at lines 2530--2549. The corrected source-presentation record also defines the tuple abbreviation `bar f` exactly, declares its metalinguistic standing and distinctions, and uses it only in the two stated rules (`spec/research/p09-source-presentations-lot2-3.md:284-305`).
- **M37 — REVISE.** The charter-enumerated round-three omissions are otherwise repaired on the common hashes, including the corrected p. 741 locator and the local `bar f` definition. But the strict “later” substitution is an unsupported strengthening and leaves the displayed Theorem 3.5 proof incomplete, so the no-unsupported-repair/no-weakened-criterion condition is not met.

## Final mathematical disposition

The Section 4 periodic-model chain, ETL replacement chain, complexity transfers, shared universal-model-checking theorem, source proof-strength calibrations, bibliography, rights boundary, and terminology standing are clean on the frozen hashes. The single Theorem 3.5 current-witness defect is nevertheless proof-critical and appears consistently in three frozen artifacts. Under the charter's unanimity and uncertainty rules, the corrected round-four snapshot must be revised and rereviewed.
