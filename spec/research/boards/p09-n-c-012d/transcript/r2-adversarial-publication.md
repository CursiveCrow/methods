REVISE

# Round-two adversarial publication/AGENTS review: N-c-012.d

## Identity, independence, and method

- Stable agent identifier: `/root/mcnaughton_1966_research`.
- Runtime model/version: not exposed to this seat.
- Role: adversarial publication and AGENTS-compliance seat.
- Independence: I read no `ledger.md`, no `transcript/chair.md`, no round-one transcript, no other round-two transcript or verdict, and I contacted no reviewer.
- Mutation boundary: I edited only this assigned transcript. I made no manuscript, shared-surface, bibliography, source-note, source-presentation-ledger, authority, image, or board-record change.
- Method boundary: direct visual primary-source reading, mathematical comparison, and prose inspection only. I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or builds. SHA-256 identity hashing was the only mechanical verification.

## Frozen identities

I recomputed all nine round-two identities before substantive review and again immediately before filing. Both computations matched the charter exactly:

| Frozen object | Verified SHA-256 |
|---|---|
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf` | `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5` |
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf` | `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png` | `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png` | `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `48D2F8F946AFFC394613D7895E89175099CC9FA73800BDA36A3C5F63353C6AD5` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` |
| `handbook/bib/handbook.bib` | `1BD6B33A12449449671505A5EEEAB64C99D0E8A74F3E968C9951FF932B778E95` |
| `spec/research/p09-sistla-clarke-1985-source-note.md` | `D7E85E5AC951C56F607099A5756C1AA5CEEC02DB8D0CC3EC359E17EBE2450FCD` |
| `spec/research/p09-source-presentations-lot2-3.md` | `D5BD9F8BA7A12AFD7A8A08CDAAFB2E0E4C0E0B48E0BD83D5BDC06AA08D2E8353` |

## Primary-source reading record

I visually read the complete JACM authority, all seventeen physical pages corresponding one-for-one to printed pp. 733--749, from `journal-page-01.png` through `journal-page-17.png`. I separately inspected the controlling enlarged p. 742 exponent crop and the complete enlarged p. 745 image. I visually read the complete STOC authority, all ten physical pages corresponding one-for-one to printed pp. 159--168, from `conference-page-01.png` through `conference-page-10.png`. Images controlled over OCR, memory, the source note, and all earlier work.

I then read the complete frozen Sistla--Clarke reader subsection, `n-c-012.tex:1851-2314`, its GPSS and Alpern--Schneider boundaries, the relevant shared temporal-language, PSPACE, automata-model-checking, comparison, and atlas surfaces in `logic-in-computer-science.tex`, the complete source note, the complete `N-c-012.d` source-presentation-ledger entry, and the complete `SistlaClarke1985` bibliography entry.

## Findings

### AP-R2-F1 — BLOCKER — Section 3's source-defined objects are undefined or defined after use

- **Artifact locations:** `handbook/parts/p09/presentations/n-c-012.tex:1975-1987`, `:1989-2020`, and `:2035-2042`; `spec/research/p09-sistla-clarke-1985-source-note.md:269-280` and `:308-318`.
- **Source locations:** journal p. 735, bottom of §3; journal p. 736, the prose immediately before Lemma 3.3.
- **Claim:** The reader says that the source “splits off” `init(S)` and uses `final(S)` at lines 2011--2012, but never defines `final(S)` as the source's unique maximal suffix. It defines `size(S)` only for a structure and later writes `size(u)` for an acceptable subsequence without giving the source's context-relative definitions of `init(t)`, `final(t)`, `range(t)`, and `size(t)`. It first uses `mu(f)` in the displayed Lemma 3.3 bound at line 2020 and defines it only at lines 2037--2038. The source note likewise defines the four structure-level objects and then uses `size(u)` without recording the p. 736 extension to acceptable subsequences.
- **Evidence:** Printed p. 735 defines `final(S)` as the unique maximal suffix in which every valuation appearing there occurs infinitely often, writes `s=init(S) . final(S)`, and only then defines `range(S)` and `size(S)`. Printed p. 736 expressly extends the notation relative to the ambient structure: `init(t)` is the longest prefix of `t` that is a subsequence of `init(S)`; `final(t)` is the remaining suffix; and `range(t)` and `size(t)` are defined analogously, all relative to `S`. The same page defines `mu(f)` as the number of occurrences of `F` before stating Lemma 3.3.
- **Publication harm:** Without maximality, `init(S)` is not visibly canonical and the displayed size measure can vary with an arbitrary split. `final(S)` is a definition-before-use failure. More seriously, `size(u)<mu(f)` is not locally typed: the left side has only been defined for structures, and the right side is introduced after the theorem display. This defeats first-reader verification of the extraction lemma and violates I7, I12, C3, C8, C9, M15, and M18. It also makes the note's claim to an exact Section 3 chain incomplete.
- **Exact correction:** At the start of the small-structure paragraph, define `final(S)` with the source's unique-maximal-suffix condition, write the exact `s=init(S) . final(S)` decomposition, and derive `range(S)` and `size(S)` from it. Immediately after defining acceptable subsequence, reproduce the p. 736 relative definitions of `init(t)`, `final(t)`, `range(t)`, and `size(t)`. Before the Lemma 3.3 statement, define `mu(f)` as a natural-number occurrence count, state that it counts only `F` occurrences rather than all formula symbols, and explain that this distinct measure is required by the extraction bound. Add the same acceptable-subsequence measure definitions to the source note before its first `size(u)` use.

### AP-R2-F2 — MAJOR / MUST FIX — Theorem 3.5's NP-membership certificate loses its load-bearing polynomial bound

- **Artifact location:** `handbook/parts/p09/presentations/n-c-012.tex:2057-2069`.
- **Source locations:** journal pp. 738--739, Theorem 3.5 proof; the exact bound is already recorded at `spec/research/p09-sistla-clarke-1985-source-note.md:371-378`.
- **Claim:** The reader says only that the nondeterministic algorithm guesses a “bounded prefix and a strongly connected recurring set.” It neither gives the bound nor defines “recurring set.”
- **Evidence:** The printed proof bounds the finite path prefix by `length(f) card(N)`, then uses a guessed strongly connected subset for the infinite suffix and checks the prefix, the connection into that subset, strong connectivity, and the relevant formula conditions. That numerical bound is the step showing that the existential-path witness can be guessed in nondeterministic polynomial time.
- **Publication harm:** “Bounded” alone does not establish a polynomial certificate; it could conceal an exponential bound. “Recurring set” is also an unnecessary, undefined handbook synonym where the source's ordinary graph-theoretic “strongly connected subset” suffices. A skeptical reader therefore cannot recover the NP-membership argument from the reader-facing theorem presentation. This fails C3, C9, and I12 even though the source note preserves the missing fact.
- **Exact correction:** Replace the vague sentence with the source-exact certificate architecture: a prefix of length at most `length(f) card(N)`, followed by a suffix confined to a guessed strongly connected subset of `N`; name the connecting-edge, strong-connectivity, and formula-label checks. Delete “recurring set” unless it is independently justified under all five terminology conditions.

### AP-R2-F3 — MAJOR / MUST FIX — Direct STOC claims have no resolvable STOC bibliography citation

- **Artifact locations:** `handbook/parts/p09/presentations/n-c-012.tex:1872-1880`, `:1959-1972`, and `:2102-2108`; `handbook/bib/handbook.bib:2245-2259`.
- **Source-record location:** `spec/research/p09-sistla-clarke-1985-source-note.md:51-56` gives the distinct conference work's complete identity.
- **Claim:** The reader makes direct, page-specific claims about STOC p. 160's validity definition and the conference's `S(n)` distance, and it compares conference Theorem 4.6 with journal Theorem 4.7. Yet the bibliography contains only `SistlaClarke1985`, and every citation in the subsection points to journal pages. In particular, the citation at line 1972 points to journal pp. 735 and 748 even though the immediately preceding positive source claim is about conference p. 160; the citation at line 2108 points to journal pp. 739--742 and cannot establish what the conference printed.
- **Evidence:** The two authorities are distinct publications with distinct pagination, DOI, file identity, and proof status. The note correctly identifies the STOC paper as the same-titled work in the *Proceedings of the Fourteenth Annual ACM Symposium on Theory of Computing*, pp. 159--168, DOI `10.1145/800070.802189`. The journal citation can establish the journal's omission, its table, its correction notice, and its `2S(n)` text, but not the literal wording on conference pp. 160 or 164.
- **Publication harm:** A handbook reader cannot resolve the direct conference locators from the bibliography, and the adjacent journal citations visually imply support that those journal pages do not provide. That weakens the very version separation the subsection is trying to enforce and fails C7--C9.
- **Exact correction:** Add a separate `SistlaClarke1982` conference bibliography record with the identity already established in the source note. Cite it at each direct conference claim, while retaining `SistlaClarke1985` only for the corresponding journal statement or omission. Keep the two sources in separate citation commands where a sentence contrasts them.

## Criterion-by-criterion disposition

- **C1 — CLEAN.** Journal identity, author order, plural title, issue/date/pages/DOI/ISSN, receipt history, CMU provenance, file identity, distinct conference object, and rights boundary agree with printed pp. 733, 748--749 and the archive files. C8 nevertheless fails because the distinct conference object is not bibliographically citable in the reader (AP-R2-F3).
- **C2 — CLEAN.** The operator-indexed language classes, restricted tilde fragment, inclusive `U/S`, distinct-state temporal structures, total finite `R`-structures, existential path problem, universal counterexample relation, and journal-relative reconstruction of validity are exact. The conference clause is not misattributed to journal pp. 734--735.
- **C3 — REVISE.** Lemmas 3.2, 3.3, and 3.6 now have their repaired quantifiers and the strict/non-strict defect is candid, but the foundational `final/size/mu` definitions and the polynomial NP certificate are still defective (AP-R2-F1 and AP-R2-F2).
- **C4 — CLEAN.** The stuttering boundary, graph-to-satisfiability reduction, Figure 2 unit, terminal persistence, journal `2S(n)`, exact truth-set count, fulfilled-before endpoint, periodicity, every-position obligations, bounds, `Ff` move, initial-since condition, and Savitch passage agree with pp. 739--745.
- **C5 — CLEAN.** ETL grammar standing, disjoint nonterminals, normalization, finite/infinite typing disclosure, parity conflict, closure, exact `Gamma` edges, finite-terminal separation, two fulfillment obligations, Theorems 5.3--5.4, continuation sets, and correction-notice calibration agree with pp. 745--748.
- **C6 — CLEAN.** All Table I rows are present; `L(U,X)` is separated from the literal Theorem 4.1 list; the containment argument is valid; and the shared universal model-checking result passes through negated existential path search plus PSPACE closure under complement without changing the source quantifier.
- **C7 — REVISE.** The mathematical conference/journal reconciliation is accurate, including validity, terminal behavior, `S(n)`/`2S(n)`, periodic theorem strengthening, and the unidentified-error boundary, but the conference side is not independently citable in the handbook (AP-R2-F3).
- **C8 — REVISE.** Page map, proof-status table, rights statement, journal bibliography, source note, and pre-review ledger status are otherwise accurate. The source note omits the p. 736 subsequence-size definitions (AP-R2-F1), and the reader/bibliography lacks the conference citation surface (AP-R2-F3).
- **C9 — REVISE.** Prose is independently reconstructed and the major types/quantifiers are clean, but the definition-before-use and unnecessary-name failures in AP-R2-F1/F2 prevent publication readiness.

## Invariant disposition

- **I1:** satisfied by this review method.
- **I2:** satisfied; both complete hash passes matched.
- **I3:** satisfied; all 17 journal and 10 conference pages were visually read.
- **I4:** satisfied; p. 742 prints `2^length(f)`, and p. 745 controls both stated defects.
- **I5:** satisfied mathematically; the journal controls and no unique repairing inference is invented.
- **I6:** satisfied; all language/problem/quantifier distinctions remain explicit.
- **I7:** **not satisfied** because the reader does not give the exact source definition infrastructure for `final(S)` and acceptable-subsequence `size(u)` (AP-R2-F1); the inequality defect itself is correctly disclosed.
- **I8:** satisfied; `2S(n)`, `2^length(f)`, and inclusive `j>=i` fulfillment are exact.
- **I9:** satisfied; all three periodic conditions, bounds, `Ff`, initial-since, and Savitch are visible.
- **I10:** satisfied.
- **I11:** satisfied; proof granularities remain differentiated in the source note and no Büchi construction is attributed to this article.
- **I12:** **not satisfied** by `final(S)`, `size(u)`, definition-after-use `mu(f)`, and the undefined/unnecessary “recurring set” (AP-R2-F1/F2).
- **I13:** satisfied; independence was preserved.
- **I14:** applied; these supported defects force `REVISE` without majority inference.
- **I15:** preserved; no closure beyond this exact topic is claimed.

## Mandatory-check disposition

- **M01 PASS:** the p. 742 crop and full page print `2^length(f)`; no scoped artifact attributes `2^(2 length(f))` to the article.
- **M02 PASS:** pp. 734--735 contain no formal validity clause; the reader labels the universal journal-relative clause as reconstruction.
- **M03 PASS:** fulfillment uses `j>=i` and an inclusive witness `i<=ell<=j`.
- **M04 PASS:** the literal `<`, null-sequence `0<0` failure, proof uses of `<=`, and Theorem 3.4's `<=` conclusion are all preserved.
- **M05 PASS:** conference p. 164 prints `S(n)` and journal p. 742 prints `2S(n)`; the manuscript uses the journal count. Bibliographic support still requires AP-R2-F3.
- **M06 PASS:** Theorems 4.7 and 5.3 retain their exact prefix/period bounds and every-periodic-position obligations.
- **M07 PASS:** the finite/infinite word sentence and unrestricted printed index are disclosed, and the represented-index restriction is owned by the handbook.
- **M08 PASS:** the grammar word, printed even-state sentence, zero-based odd-offset consequence, and nonrepair boundary are exact.
- **M09 PASS:** closure and every continuation-edge condition in `Gamma` are exact, with terminal productions kept outside the continuation edges.
- **M10 PASS:** maximum finite-tree depth, distinct ETL fulfillment standing, and continuation-set emptiness within the period are exact.
- **M11 PASS:** no precise conference inference or unique new repairing lemma is identified.
- **M12 PASS:** all reduced proof statuses are preserved in the source-note table and no Sistla--Clarke automata translation appears.
- **M13 PASS:** `L(U) subseteq L(U,X) subseteq L(U,S,X)` supplies the exact lower/upper sandwich.
- **M14 PASS:** universal-path model checking is derived through the negated existential problem and complement closure.
- **M15 REVISE:** acceptable subsequence itself is distinguished, but its required `final/size` infrastructure and `mu` measure fail the local five-part rule; source truth set, both fulfilled-before obligations, the ETL constructor, and `Gamma` are otherwise clean.
- **M16 PASS:** the note maps `init/final/range/size` to p. 735, conclusion to p. 748 only, and references to pp. 748--749.
- **M17 PASS:** conference p. 160 validity is recorded, the journal-relative clause remains reconstructed, and the correction notice remains limited to an unidentified theorem. The direct conference claim still needs AP-R2-F3's bibliography repair.
- **M18 REVISE:** all repaired lemma hypotheses/conclusions and the inequality conflict are present, but the source's p. 736 acceptable-subsequence measure definitions required to type Lemma 3.3 remain omitted (AP-R2-F1).
- **M19 PASS:** tape-cell diamond, BI-to-EI description, repeated-history, journal persistence, and conference halting wording are all exact.
- **M20 PASS:** `i in N`, positive `p`, equality of complete valuations for every `k>=i`, source-truth-set equality, and obligation discharge remain distinct.
- **M21 PASS:** the shared method returns a finite product path plus a nonempty product cycle and explicitly unfolds it; no undefined periodicity label remains.
- **M22 PASS:** the scoped artifacts use only the source's “labelled tree” or `Gamma`; no proof-tree, derivation-tree, or continuation-tree synonym is introduced.
- **M23 REVISE:** the enumerated round-two repairs are mostly present, but the frozen snapshot still fails C3/C7/C8/C9 and I7/I12 through AP-R2-F1--F3; it is therefore not a clean repaired snapshot.

## Premortem

If this snapshot shipped, a source-critical reader would first fail while trying to instantiate Lemma 3.3: `final(S)` is not defined, `size(u)` has the wrong visible domain, and `mu(f)` arrives only after its theorem use. A complexity reader would then ask where the polynomial NP certificate is proved and find only the word “bounded.” Finally, a version auditor following p. 160 or the conference `S(n)` claim would find no conference bibliography record and only journal citations. An ordinary checklist focused on the already prominent exponent, parity, periodicity, and correction-notice defects could miss all three because the source note contains nearby correct prose; the adversarial definition-before-use and citation-resolution passes did not.

## Narrow closure boundary and verdict

The round-two source/version repairs concerning M01--M14, M16--M17, and M19--M22 are substantively clean, but AP-R2-F1--F3 are publication-level must-fix defects. This verdict concerns only the frozen N-c-012.d integrated unit. It does not close Alpern--Schneider, N-c-012 as a whole, Part IX, another handbook part, any final build or rendered inspection, human review, final-book completion, or user acceptance.

REVISE
