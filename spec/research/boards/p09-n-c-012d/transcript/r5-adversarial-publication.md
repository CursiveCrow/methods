REVISE

# Round-five adversarial publication / AGENTS-compliance review

## Reviewer identity, independence, and method

- Stable agent identifier: `/root/r5_adversarial_publication`.
- Runtime model/version: not exposed to this agent.
- Review object: only the ten-object frozen round-five snapshot specified in
  `spec/research/boards/p09-n-c-012d/charter.md`.
- Independence: I read the charter completely. I did not read `ledger.md`,
  `transcript/chair.md`, this board's round-one through round-four transcripts,
  or either other round-five transcript. I did not contact another reviewer or
  disclose this verdict to another seat.
- Method: fresh visual source reading, mathematical checking, and prose
  inspection only. I ran no test, test harness, checker, repository script, TeX
  command, build, handbook-PDF inspection, or rendered-handbook inspection.
  Hash calculation and ordinary read-only source inspection were the only
  command-line operations.

## Frozen identity verification

I computed SHA-256 for all ten frozen objects at the start of review and again
immediately before filing. Every value matched the charter exactly:

| Frozen object | Verified SHA-256 |
|---|---|
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf` | `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5` |
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf` | `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png` | `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png` | `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-04-acceptable-crop.png` | `C267D4B4DF785F9A7E82123B068662E45D7E2C87CB18C24D7B8EB0B875AF413B` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `C760B8B413937A9002F017704956EBFFB2AF7ED44AD8AD8FF0EC4366E526EC79` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` |
| `handbook/bib/handbook.bib` | `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B` |
| `spec/research/p09-sistla-clarke-1985-source-note.md` | `79E0677D27769153BC5C078242CDD77916350B926C87B25F91F78A9C943F0F19` |
| `spec/research/p09-source-presentations-lot2-3.md` | `9739EBEE2BBE5F24857B9C900F831B7F9783F5BAA00652E02E3F5DD755E08D22` |

There was no identity mismatch.

## Complete primary-source reading

I freshly and visually read every journal image
`journal-page-01.png` through `journal-page-17.png`, corresponding one-for-one
to printed pp. 733--749, and every conference image
`conference-page-01.png` through `conference-page-10.png`, corresponding
one-for-one to printed pp. 159--168. I also visually read the three frozen
enlarged aids required by the charter:

- `journal-page-04-acceptable-crop.png`, confirming the literal strict
  acceptable-union inequality on printed p. 736;
- `journal-page-10-bound-crop.png`, confirming the faint bound
  (2^{\operatorname{length}(f)}) on printed p. 742; and
- the enlarged `journal-page-13.png`, confirming the printed finite/infinite
  indexing defect and the (N_0\to a_1a_2N_0) even/odd conflict on printed
  p. 745.

The PDFs were treated as the authorities and the images only as visual reading
aids. No source page was unread or uncertain.

I then read the complete frozen reader subsection
`handbook/parts/p09/presentations/n-c-012.tex:1851--2622`, the shared Part IX
definition/theorem/method context at
`handbook/parts/p09/logic-in-computer-science.tex:599--809` and the summary row
at lines 2219--2222, both bibliography records at
`handbook/bib/handbook.bib:2245--2274`, the complete source note
`spec/research/p09-sistla-clarke-1985-source-note.md:1--1052`, and the complete
compact `N-c-012.d` presentation at
`spec/research/p09-source-presentations-lot2-3.md:185--375`.

## Must-fix finding

### F1 — The round-five ETL arity repair reuses one bound symbol for two incompatible quantities

This is a publication-blocking exact-typing and cross-file-consistency defect.
It fails C5, C8, C9, I10, M41, and M42.

The primary source keeps the quantities distinct at the point where the
distinction is necessary. Printed p. 745 first uses (n) for the number of
grammar terminals and hence for the constructor arity
(N_j(f_1,\ldots,f_n)); its later generic tree and Lemma 5.2 passages use a
local (q) for that same arity (printed pp. 745--746). In Theorem 5.4,
printed p. 747 instead uses (n) for the **total encoded input length**, while
the formula constructor there remains (N_j(f_1,\ldots,f_q)). Thus the source
does not identify encoded input length with grammar-terminal count.

The reader says that it alpha-renames the source's arity (q) to (n)
“throughout,” and explicitly binds (n) as both grammar-terminal count and
formula-constructor arity at
`handbook/parts/p09/presentations/n-c-012.tex:2457--2464`. That renaming could
be harmless only if the source's separate input-length variable were renamed
away. Instead the reader says at lines 2545--2548:

> If the total encoded input length is (n), the paper uses
> \(\operatorname{card}(\operatorname{SF}(f))\le2n\).

It then immediately writes (N_j(f_1,\ldots,f_n)) in the positive rule at
lines 2553--2560 and again in the continuation-set rule at lines 2563--2573.
Consequently the same (n), in one local Theorem 5.4 presentation, denotes
both total input length and constructor arity. On the rebinding reading, the
display silently forces the constructor to have one argument per encoded input
symbol, which the source never requires. On the no-rebinding reading, the
(\operatorname{card}(\operatorname{SF}(f))\le2n) estimate is incorrectly
stated in terms of terminal/argument count rather than total encoded input
length. The text supplies no third reading that preserves both claims.

The complete source note repeats the same collision. It binds (n) as
terminal count and constructor arity, and announces the (q\mapsto n)
alpha-renaming, at
`spec/research/p09-sistla-clarke-1985-source-note.md:730--744`; it then binds
total input length as (n) at lines 826--830 while retaining
(N_j(f_1,\ldots,f_n)) throughout the two Theorem 5.4 rules at lines
833--851.

The compact presentation makes the inconsistency visible rather than curing
it. At `spec/research/p09-source-presentations-lot2-3.md:306--317`, (n)
remains the terminal/argument count and
(\bar f:=(f_1,\ldots,f_n)) is locally and correctly defined; lines 318--331
then use that tuple in the two search rules. But lines 368--372 claim that the
formerly unbound ETL arity has now been repaired consistently in the reader and
source records. That completion claim is false on the frozen reader and source
note just cited.

The minimal repair is to preserve one symbol for terminal count / constructor
arity and use a different, explicitly bound symbol for total encoded input
length in both the reader and source note. For example, if (n) remains the
arity, bind a fresh local (L) as the total input length and write
(\operatorname{card}(\operatorname{SF}(f))\le2L). Equally, the source's own
(q)-for-arity and (n)-for-input-length distinction may be retained. The
same choice must be used through the constructor, (Gamma), Lemma 5.2,
Theorem 5.4, the source note, and the compact presentation before the compact
status claim can say the repair is consistent.

## Criterion-by-criterion disposition

| Criterion | Disposition | Evidence and reason |
|---|---|---|
| C1 | **CHECKED CLEAN** | Printed pp. 733 and 749, conference pp. 159--168, reader 1853--1881, bibliography 2245--2274, and source note 35--117 preserve exact work/version identity, author order, plural title, issue/date/pages, DOI/ISSN, receipt history, separate conference object, hashes, archive provenance, and the non-republication rights boundary. |
| C2 | **CHECKED CLEAN** | Journal pp. 734--735 and reader 1883--1990 preserve syntax, fragment standing, inclusive (U/S/F), structure and interpretation types, existential (R)-truth, its universal-counterexample relation, and the explicitly reconstructed journal-relative validity clause. |
| C3 | **CHECKED CLEAN** | Journal pp. 735--739 and reader 1992--2225 preserve the unique maximal suffix, ambient-relative acceptable subsequences, Lemmas 3.1--3.3 and both strict-sign conflicts, Theorems 3.4--3.7, the 3-SAT diamonds, pre-certificate (SF(f)), bound (q_0:=\delta), every label rule including current-position (F), the literal singleton gap, the handbook-owned cycle correction, and proof granularity. |
| C4 | **CHECKED CLEAN** | Journal pp. 740--745 and reader 2227--2446 preserve Lemma 4.3's full (\mathcal P_1/\mathcal P_2), (g_i^x,f_x,h_i,f',f'') construction, both pure-(U) cases, stuttering, journal (2S(n)), truth-set count, fulfilled-before clause, exact Lemmas 4.5--4.6, Theorem 4.7, all five one-step recurrences, initial since, loop equality, obligation discharge, storage, and Savitch. |
| C5 | **REVISE** | The ETL mathematical chain, finite-word typing disclosure, parity disclosure, closure, (Gamma), Lemmas 5.1--5.2, Theorems 5.3--5.4, and continuation rule are otherwise source-exact, but F1 leaves the terminal/constructor arity inconsistent with encoded input length in the reader and source note. |
| C6 | **CHECKED CLEAN** | Journal p. 748, reader 2591--2621, and shared theorem lines 693--708 give the exact Table I rows and the (L(U)\subseteq L(U,X)\subseteq L(U,S,X)) classification. Shared lines 761--808 preserve the finite product-path/nonempty-cycle witness and the complement passage to universal model checking. |
| C7 | **CHECKED CLEAN** | All ten conference pages were compared with all seventeen journal pages. Reader 1853--1881 and 2281--2295 and source note 933--972 preserve numbering, bounds, (S(n))/(2S(n)), terminal behavior, periodic invariants, and the unidentified correction boundary without importing a unique repair. |
| C8 | **REVISE** | Bibliography, locators, page map, proof-status table, provenance, and rights are clean, but F1 makes the reader/source-note/compact ETL bindings inconsistent and makes the compact round-five “repaired consistently” claim at lines 368--372 unsupported. |
| C9 | **REVISE** | The prose is independently worded and the named technical items otherwise meet the five-part terminology rule, but F1 violates exact binding and definition-before-use at the Theorem 5.4 rule location. Publication-quality notation cannot leave constructor arity dependent on an ambiguous rebinding. |

## Invariant disposition

| Invariant | Disposition |
|---|---|
| I1 | **PASS** — source reading, mathematics, and prose inspection only; no prohibited test/build activity. |
| I2 | **PASS** — all ten hashes matched twice. |
| I3 | **PASS** — all 17 journal and all 10 conference pages were freshly read visually. |
| I4 | **PASS** — the p. 742 exponent and both p. 745 defects were checked in the frozen enlarged aids and are reported exactly. |
| I5 | **PASS** — the journal controls and the conference is kept separate; the correction notice is not overinterpreted. |
| I6 | **PASS** — fragments, ETL constructor, inclusive semantics, existential truth, satisfiability, validity, and reconstruction are distinguished. |
| I7 | **PASS** — structure size, unique maximal suffix, ambient measures, and both strict/non-strict conflicts are exact. |
| I8 | **PASS** — journal (2S(n)), closure bound, (2^{\operatorname{length}(f)}), and inclusive fulfillment are distinct and exact. |
| I9 | **PASS** — Theorem 4.7's equality, every-position discharge, bounds, (Ff), initial since, and Savitch step remain visible. |
| I10 | **REVISE** — F1 violates the required consistently bound ETL terminal/argument arity through Theorem 5.4, despite the remaining grammar/tree/search material being exact. |
| I11 | **PASS** — proof sketches, asserted inductions, abbreviated cases, and brief replacements are not upgraded; no Sistla--Clarke Büchi proof is claimed. |
| I12 | **PASS** — acceptable subsequence, the ambient subscript, source truth set, both fulfillment uses, label, reduction auxiliaries, (A/B), (Gamma), (arphi), and the compact tuple abbreviation each have local necessity, exact definition/standing, nonredundancy, and use. F1 is a bound-variable typing collision, not licence for a new technical name. |
| I13 | **PASS** — independence restrictions were obeyed. |
| I14 | **PASS** — this uncertainty-free must-fix defect produces REVISE; no majority inference is made. |
| I15 | **PASS** — no topic-level verdict is represented as closing broader manuscript, build, visual, human, or user gates. |

## Mandatory-check disposition

| Check | Disposition and precise locator |
|---|---|
| M01 | **PASS** — journal p. 742 and `journal-page-10-bound-crop.png`; reader 2303--2315 prints (2^{\operatorname{length}(f)}), not (2^{2\operatorname{length}(f)}). |
| M02 | **PASS** — journal pp. 734--735 have no formal validity clause; conference p. 160 does; reader 1977--1990 labels the universal clause as reconstruction. |
| M03 | **PASS** — journal p. 742; reader 2316--2323 has (j\ge i) and (i\le\ell\le j). |
| M04 | **PASS** — journal pp. 736--737 and enlarged p. 736 crop; reader 2067--2083 and 2111--2122 preserves both literal `<` signs, null failures, proof `\le`, and Theorem 3.4's non-strict result. |
| M05 | **PASS** — journal p. 741 says (2S(n)), conference p. 164 says (S(n)); reader 2290--2295. |
| M06 | **PASS** — journal pp. 743--744 and 746--747; reader 2380--2400 and 2535--2544 preserves all bounds/quantifiers and every-periodic-position obligations. |
| M07 | **PASS** — journal p. 745; reader 2468--2479 distinguishes the untyped unrestricted index from the handbook's finite represented-index restriction. |
| M08 | **PASS** — journal p. 745 and enlarged page; reader 2484--2493 preserves (N_0\to a_1a_2N_0) and the even/zero-based-odd conflict without choosing a repair. |
| M09 | **PASS** — journal p. 745; reader 2495--2512 gives exact closure and (Gamma(S,j,N_i)), with continuation edges separated from terminal witnesses. |
| M10 | **PASS** — journal pp. 746--747; reader 2514--2517 and 2563--2583 separates finite-tree depth from until fulfillment and requires continuation-set emptiness within the period. |
| M11 | **PASS** — journal p. 748; reader 1874--1881 and 2583--2589 does not identify a precise bad inference or unique repairing lemma. |
| M12 | **PASS** — reader 2440--2446 and source note 906--927 preserve every proof-status qualification; reader 2583--2589 and source note 862--865 attribute no Büchi construction to Sistla--Clarke. |
| M13 | **PASS** — journal Table I and shared Part IX 693--708 use (L(U)\subseteq L(U,X)\subseteq L(U,S,X)) for the exact hardness/upper-bound classification. |
| M14 | **PASS** — journal p. 735 and shared Part IX 796--808 derive universal model checking from existential truth of the negated formula plus polynomial-space complement closure. |
| M15 | **PASS** — reader 2036--2067, 2303--2323, and 2464--2512 supplies the five-part local standing for acceptable subsequence, ambient subscripts, source truth sets, fulfillment, the ETL constructor, and (Gamma). |
| M16 | **PASS** — source-note page map 119--145 places `init/final/range/size` on p. 735, conclusion on p. 748, and references on pp. 748--749. |
| M17 | **PASS** — conference p. 160 validity is recorded while journal-relative reconstruction remains explicit; correction notice remains unidentified (reader 1977--1990, 2583--2589). |
| M18 | **PASS** — reader 2015--2034, 2085--2122, and 2217--2225 preserves the exact Lemmas 3.2, 3.3, and 3.6 hypotheses, every-intermediate-supersequence quantifiers, surviving-position scope, current-state inclusion, and strict-sign disclosure. |
| M19 | **PASS** — journal p. 741 and reader 2281--2295 preserve one cell per diamond, one ID per BI-to-EI traversal, repeated traversals, and persistent terminal configurations; source note 940--960 records the conference halting statement. |
| M20 | **PASS** — journal p. 742 and reader 2366--2378 gives (i\in\mathbb N), (p>0), and complete-valuation equality for every (k\ge i), distinct from truth-set equality and obligations. |
| M21 | **PASS** — shared Part IX 761--808 returns a finite product path plus a nonempty product cycle whose unfolding is the counterexample, without an undefined periodicity name. |
| M22 | **PASS** — reader, source note, and compact record call (Gamma(S,j,N_i)) only the source labelled tree / (Gamma); no proof-tree, derivation-tree, or continuation-tree synonym is introduced. |
| M23 | **PASS** — the round-one substantive defects represented by M01--M15 remain repaired/disclosed on this snapshot; F1 is the later round-five arity repair defect. |
| M24 | **PASS** — reader 1992--2013 defines the unique maximal suffix, exact decomposition, structure-level range, and size before use. |
| M25 | **PASS** — reader 2036--2067 gives the ambient-relative subsequence operations and the subscript's eliminable, necessary, nonredundant, used standing. |
| M26 | **PASS** — reader 2067--2085 and 2111--2122 gives the preparatory strict sentence, null counterexample, non-strict subadditivity, and (mu(f)) before Lemma 3.3. |
| M27 | **PASS** — reader 2143--2195 preserves prefix bound, (C), strong connectivity, entry edge, all initialized/increasing-length label rules, and acceptance at (q_0). |
| M28 | **PASS** — bibliography 2245--2274 has distinct accurate 1982/1985 records, and direct conference/journal claims use their respective keys. |
| M29 | **PASS** — all round-two substantive checks remain repaired/disclosed without weakening M01--M23. |
| M30 | **PASS** — reader 2290--2295 pinpoints journal (2S(n)) to p. 741, conference (S(n)) to p. 164, and the broader journal reduction to pp. 741--742. |
| M31 | **PASS** — reader 2153--2195 gives empty initialization, increasing-length atom/negation/conjunction/current-inclusive-(F) rules and start acceptance; 2197--2214 preserves the literal strong-connectivity check, concrete false acceptance, and handbook-only cycle correction. |
| M32 | **PASS** — reader 2233--2279 gives exact (\mathcal P_1/\mathcal P_2), (g_1/g_2/g_3), (f_x), (h_1/h_2/h_3), (f'), (f''), (L(F,X)), both pure-(U) cases, and Lemma 4.2's role. |
| M33 | **PASS** — reader 2324--2364 gives the exact Lemma 4.5 deletion/common-token result and all Lemma 4.6 hypotheses and both conclusions. |
| M34 | **PASS** — reader 2402--2438 gives Boolean, (X), (U), direction-sensitive (S), initial since, loop-entry equality, within-period discharge, storage, and Savitch. |
| M35 | **PASS** — reader 2514--2544 gives Lemma 5.2's additional negated-grammar hypothesis and both inherited conclusions; 2545--2583 gives the positive rule, singleton initialization, exact frontier update, and within-period emptiness. F1 concerns the bound symbol used in those otherwise exact rules. |
| M36 | **PASS** — reader 2156--2195, 2233--2262, 2402--2407, and 2563--2580 locally types and distinguishes `label`, all Lemma 4.3 auxiliaries, (A/B), and (arphi), and uses each. |
| M37 | **PASS** — all round-three substantive findings remain repaired/disclosed; no M01--M36 mathematical condition other than the later, separately tested arity binding is weakened. |
| M38 | **PASS** — reader 1905--1920 defines (SF(f)) before Theorem 3.5, with ordinary subformulas, single-negation mates, double-negation elimination, the (2\operatorname{length}(f)) bound, and distinction from (2^{\operatorname{length}(f)}). |
| M39 | **PASS** — reader 2143--2191, source note 428--468, and compact presentation 249--261 explicitly bind (q_0:=\delta) before prefix and acceptance use. |
| M40 | **PASS** — reader 2169--2189, source note 448--466, and compact 257--266 preserve “after,” explain the necessary non-strict reading from pp. 735/737, label the at-or-after form handbook-owned, and keep it distinct from the cycle correction. |
| M41 | **REVISE** — F1. Reader 2457--2464 and 2545--2573 and source note 730--744 and 826--851 reuse (n) for both terminal/constructor arity and total encoded input length. The compact tuple abbreviation at 313--331 is locally compliant but cannot make the other two records consistent. |
| M42 | **REVISE** — the supported round-four finding that the ETL arity was unbound has not been fully repaired: the round-five binding is now explicit at the constructor but becomes inconsistent at Theorem 5.4. The compact completion claim at 368--372 is therefore premature. |

## Final publication disposition

All source pages were read, all hashes matched, and no uncertainty remains.
The reconstruction is checked clean on the mathematical and source-fidelity
issues represented by M01--M40, but the single symbol collision in F1 prevents
exact typing and makes the cross-file completion claim false. Under the
charter's unanimity and uncertainty rules, the frozen round-five snapshot must
be revised and rereviewed.
