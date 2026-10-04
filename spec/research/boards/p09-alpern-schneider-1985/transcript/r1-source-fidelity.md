# Round 1 opening report: source fidelity and evidence

Seat: Source fidelity and evidence  
Board: `p09-alpern-schneider-1985`  
Scope: frozen seven-object snapshot in `charter.md`  

## Evidence boundary followed

- I recomputed all seven frozen SHA-256 hashes before substantive review.
- I visually read the five journal page images (`journal-page-1.png` through `journal-page-5.png`) and the eleven technical-report page images (`tr-page-01.png` through `tr-page-11.png`).
- I read the frozen manuscript/source surfaces in the charter's exact line scope:
  - `handbook/parts/p09/presentations/n-c-012.tex:2632-2975`
  - `handbook/parts/p09/logic-in-computer-science.tex:710-718`
  - `handbook/bib/handbook.bib:6056-6080`
  - `spec/research/p09-alpern-schneider-1985-source-note.md:1-634`
  - `spec/research/p09-source-presentations-lot2-3.md:395-528`
- I did not read `ledger.md`, `transcript/chair.md`, another current transcript, or any prior Part IX board transcript/review record.
- I did not contact another agent.
- I did not run tests, checkers, repository scripts, TeX, builds, or inspect the handbook PDF.

## Hash verification

All hashes matched the charter.

| Artifact | Recomputed SHA-256 | Status |
|---|---|---|
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-defining-liveness.pdf` | `FB69B4E81FD14CAE073F6087CE724E70847FFF16EA560701525952908E48FE31` | checked-clean |
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-tr-85-650.pdf` | `CF02E04AF863E7325C59C6C4671E389C53DB7B7ADA7804A379B287C569C896AE` | checked-clean |
| `handbook/parts/p09/presentations/n-c-012.tex` | `D1844530FA4BA9EC2E8F702763966F8AA3C57BE3A3E3DD5163EEA24E2905033D` | checked-clean |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` | checked-clean |
| `handbook/bib/handbook.bib` | `E0AF3849EEB34AB9966EF971881D3D10307ED47A92593FBE0B91917E18A1318E` | checked-clean |
| `spec/research/p09-alpern-schneider-1985-source-note.md` | `B99757CEAADE0045D4663493403112892AC4A199176D7B4A0D244AF23168532F` | checked-clean |
| `spec/research/p09-source-presentations-lot2-3.md` | `35D27BCC4AE25DE83260CB9356D854F64E99FAAFC6B824A34B85366B553CE872` | checked-clean |

## Source-page reading record

Journal article:

- Journal p. 181: publication metadata, title/authors, received/revised dates, abstract, keywords, execution convention, property/program relation, start of safety examples, copyright line.
- Journal p. 182: formal \(S^\omega\), \(S^*\), execution/partial-execution terminology, \(x\models P\) membership notation, safety clause, stuttering footnote, liveness examples, liveness clause.
- Journal p. 183: maximality argument, uniform liveness, absolute liveness, inclusion chain, leads-to example, predictive example, until example.
- Journal p. 184: total-correctness continuation, prefix topology, Theorem 1 proof, Corollary 1.1, Theorem 2 proof, Corollary 2.1, Boolean-closure paragraph.
- Journal p. 185: conclusion, acknowledgments, references.

Technical report:

- TR file p. 1 outer cover: `TR 85-650`, October 1984, revised February 1985, Cornell affiliation, support footnote.
- TR file p. 2 title/abstract leaf: title/authors, 30 October 1984, revised 20 February 1985, abstract, keywords.
- TR body p. 1 through p. 9: same substantive definitions, examples, topology, theorem proofs, corollaries, Boolean-closure paragraph, conclusion, acknowledgments, and references as the journal, with report pagination/citation style and unnumbered corollary labels.

The journal p. 184 and TR body p. 8 both print the Corollary 2.1 hypothesis with the defective closure word `intersection`; the journal labels it Corollary 2.1, while the TR prints the corresponding second corollary without decimal numbering.

## Citation and access-route check

- The Cornell journal route in `handbook/bib/handbook.bib:6066` and `spec/research/p09-alpern-schneider-1985-source-note.md:20-21` returned a live PDF route during citation inspection.
- The Cornell TR route in `handbook/bib/handbook.bib:6078` and `spec/research/p09-alpern-schneider-1985-source-note.md:30-31` returned a live PDF route during citation inspection.
- The DOI is not printed on the journal page image. Crossref metadata for `10.1016/0020-0190(85)90056-0` confirms the DOI, title, journal, volume 21, issue 4, pages 181-185, and Elsevier publisher; the printed journal page supplies the exact 7 October 1985 issue date.

## Findings

No board findings are filed by this seat. The source-critical defects already recorded in the source note, especially the implicit \(S\ne\varnothing\) hypothesis and the Corollary 2.1 closure-word defect, are visibly preserved and repaired as handbook-owned material in the frozen N-c-012 presentation rather than hidden or misattributed.

## Coverage map

| ID | Status | Evidence and disposition |
|---|---|---|
| M01 | checked-clean | All seven hashes recomputed and matched the charter values before substantive review. |
| M02 | checked-clean | Visually read journal pp. 181-185 and all eleven TR file pages. The source-note page map at `spec/research/p09-alpern-schneider-1985-source-note.md:51-80` matches the visual page reading. |
| M03 | checked-clean | Journal p. 181 supports title, authors, journal, volume/issue, date, page range, receipt/revision dates, and copyright; TR file p. 1 and p. 2 support report number/date/revision. Bibliography lines `handbook/bib/handbook.bib:6056-6080` match these, with DOI confirmed by citation metadata rather than printed page text. |
| M04 | checked-clean | Journal/report page maps and substantive agreement are supported by visual reading and by `spec/research/p09-alpern-schneider-1985-source-note.md:82-95`. Corollary 2.1 has the same substantive closure-word defect in journal p. 184 and TR body p. 8, with numbering/style differences disclosed at source-note lines 88-91 and reader lines `handbook/parts/p09/presentations/n-c-012.tex:2959-2964`. |
| M05 | checked-clean | `handbook/parts/p09/presentations/n-c-012.tex:2634-2670` defines \(S\ne\varnothing\), \(S^*\), \(S^\omega\), concatenation, prefix, property standing, membership notation, program satisfaction, and terminal-state padding; these are supported by journal pp. 181-182 and TR body pp. 1-2, with the \(S\ne\varnothing\) hypothesis correctly labelled as a handbook repair. Shared definition lines `handbook/parts/p09/logic-in-computer-science.tex:710-718` are consistent at compact strength. |
| M06 | checked-clean | The safety quantifiers and finite bad-prefix reading in `handbook/parts/p09/presentations/n-c-012.tex:2672-2685` match journal p. 182 and TR body p. 2. |
| M07 | checked-clean | `live for \(P\)` is correctly presented as a finite-prefix/property relation, and liveness as universal closure over \(S^*\), at `handbook/parts/p09/presentations/n-c-012.tex:2685-2700`; this matches journal pp. 182-183 and TR body pp. 3-4. Full-space, not fixed-system, scope is stated at `handbook/parts/p09/presentations/n-c-012.tex:2722-2725`. |
| M08 | checked-clean | Proof-method motivation, maximality argument, examples, and stuttering qualification appear at `handbook/parts/p09/presentations/n-c-012.tex:2660-2663`, `2702-2720`; these are faithful to journal pp. 181-182 and TR body pp. 1-2 and do not promote the prose into a decision procedure or uniqueness theorem. |
| M09 | checked-clean | Uniform and absolute liveness definitions, standing, nonredundancy, and inclusion chain are at `handbook/parts/p09/presentations/n-c-012.tex:2727-2767`; journal p. 183 and TR body pp. 4-5 support the definitions and inclusion chain. |
| M10 | checked-clean | Leads-to source claims and the handbook-supplied fixed-suffix check are separated at `handbook/parts/p09/presentations/n-c-012.tex:2769-2778`; journal p. 183 and TR body p. 5 support the printed example and non-absolute-liveness argument. |
| M11 | checked-clean | Predictive property prose, nondegeneracy hypotheses, liveness proof, and non-uniform proof are at `handbook/parts/p09/presentations/n-c-012.tex:2780-2800`; the source prose is on journal p. 183 and TR body p. 5, while the exact \(P_{A,B}\) rendering is correctly handbook-owned. |
| M12 | checked-clean | Until and total-correctness examples, and rejection of a safety/liveness dichotomy, are at `handbook/parts/p09/presentations/n-c-012.tex:2802-2810`; supported by journal pp. 183-184 and TR body pp. 6. |
| M13 | checked-clean | Cylinder basis and both topological equivalences are stated at `handbook/parts/p09/presentations/n-c-012.tex:2812-2831`; journal p. 184 and TR body p. 6 state the topology/equivalences, and the direction proofs are correctly labelled as handbook-supplied. |
| M14 | checked-clean | Theorem 1 construction, set algebra, density proof, and boundary claims are at `handbook/parts/p09/presentations/n-c-012.tex:2833-2867`; journal p. 184 and TR body pp. 6-7 print the theorem proof, while nonuniqueness/syntax/algorithm cautions are appropriate handbook boundary statements. |
| M15 | checked-clean | Corollary 1.1 and its complement/intersection/topological-closure hypotheses are at `handbook/parts/p09/presentations/n-c-012.tex:2868-2875`; journal p. 184 and TR body p. 7 support the statement. |
| M16 | checked-clean | Theorem 2, alpha-renamings from source \(L_a,L_b\) to handbook \(E_a,E_b\), density/disjointness, factorization, and materiality of \(|S|>1\) are at `handbook/parts/p09/presentations/n-c-012.tex:2877-2902`; journal p. 184 and TR body p. 7 support the theorem proof. |
| M17 | checked-clean | Corollary 2.1 is printed with `intersection` in journal p. 184 and TR body p. 8. The N-c-012 reader preserves the printed defect, countermodel, and union/Boolean repair at `handbook/parts/p09/presentations/n-c-012.tex:2904-2936`; source note lines `467-516` give the fuller source-critical record. |
| M18 | checked-clean | Boolean-closure entries and the claim that only \(S^\omega\) is both safety and liveness are at `handbook/parts/p09/presentations/n-c-012.tex:2938-2956`; journal p. 184 and TR body p. 8 support the closure paragraph. |
| M19 | checked-clean | Proof granularity is separated at `handbook/parts/p09/presentations/n-c-012.tex:2830-2831`, `2964-2968` and `spec/research/p09-alpern-schneider-1985-source-note.md:537-557`: Theorems 1-2 are printed with proofs; the topological equivalence direction proofs and quantifier expansions are handbook-supplied. |
| M20 | checked-clean | Definition-before-use and the AGENTS terminology rule are satisfied for `live for P`, uniform liveness, absolute liveness, \(P_{A,B}\), \(L_P\), \(E_a,E_b\), \(Q\), and \(\mathcal F\) at `handbook/parts/p09/presentations/n-c-012.tex:2685-2694`, `2727-2767`, `2780-2800`, `2833-2845`, `2877-2888`, `2917-2935`. Each name has local necessity, eliminable definition/standing, nonredundancy, and actual use. |
| M21 | checked-clean | Reader, shared definition, bibliography, source note, and compact presentation reconcile claim-by-claim: N-c-012 lines `2632-2975`, shared definition lines `710-718`, bib lines `6056-6080`, source note lines `1-634`, and compact presentation lines `395-528` agree on authority, definitions, source defects, proof ownership, rights, and status. |
| M22 | checked-clean | Unlettered register standing, rights boundary, topic-only status, and no-test/no-build boundary are explicit at `spec/research/p09-alpern-schneider-1985-source-note.md:36-49`, `626-634`, compact lines `411-415`, `523-527`, and N-c-012 lines `2958-2975`; these match the visual source pages and the charter's manuscript-content gate. |

VERDICT: ACCEPT
