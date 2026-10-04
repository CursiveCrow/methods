# Round-three source fidelity and evidence report

Mandate: source fidelity and evidence seat for the frozen round-three seven-object snapshot in `spec/research/boards/p09-alpern-schneider-1985/charter.md`.

I read the complete charter first. I did not read `ledger.md`, `transcript/chair.md`, any `r1-*` or `r2-*` transcript, either other round-three transcript, or any earlier Part IX board record. I did not contact another reviewer. I used only file hashes for snapshot identity, direct visual reading of the existing source-page images, citation/access inspection, direct manuscript/source-record reading, and mathematical/source-fidelity reasoning. I did not run or create any test, checker, repository script, Python utility, TeX command, handbook build, or handbook-PDF render/inspection.

## Snapshot/hash confirmation

All seven round-three hashes were recomputed with `Get-FileHash -Algorithm SHA256` and matched the charter.

| Artifact | Round-three SHA-256 observed | Status |
|---|---|---|
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-defining-liveness.pdf` | `FB69B4E81FD14CAE073F6087CE724E70847FFF16EA560701525952908E48FE31` | match |
| `tmp/pdfs/p09-alpern-schneider-1985/alpern-schneider-1985-tr-85-650.pdf` | `CF02E04AF863E7325C59C6C4671E389C53DB7B7ADA7804A379B287C569C896AE` | match |
| `handbook/parts/p09/presentations/n-c-012.tex` | `0C72F461A83E421AAFF950E2CBA03FD386EEA088BAC70E9D8E30E86052E977D2` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F` | match |
| `handbook/bib/handbook.bib` | `E0AF3849EEB34AB9966EF971881D3D10307ED47A92593FBE0B91917E18A1318E` | match |
| `spec/research/p09-alpern-schneider-1985-source-note.md` | `75D66211C3520522D7530C609221AB20C0409EBBA6CBCD29BD9C3CD9B8D8DD27` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `C2526F8FF7FAFFE4DB2902799BB968E0B21491B57CCC40F6548EEB6BAA534031` | match |

## Sources and pages visually inspected

I visually read the five existing journal page images at original detail:

| Image | Printed page | Content checked |
|---|---:|---|
| `journal-page-1.png` | 181 | journal metadata, title/authors, communication/receipt/revision dates, abstract, keywords, support/copyright line, execution convention, property/program relation, safety examples |
| `journal-page-2.png` | 182 | \(S^\omega\), \(S^*\), execution/partial-execution notation, safety definition, stuttering footnote, liveness examples and liveness definition |
| `journal-page-3.png` | 183 | liveness maximality argument, uniform and absolute liveness, inclusion chain, leads-to, predictive example, until and total correctness |
| `journal-page-4.png` | 184 | prefix topology, Theorem 1 proof, Corollary 1.1, Plotkin temporal-logic claim, Theorem 2 proof, Corollary 2.1, Boolean closure |
| `journal-page-5.png` | 185 | conclusion, acknowledgments, references including Plotkin private communications |

I visually read the eleven existing Cornell technical-report page images at original detail:

| Image | Internal location | Content checked |
|---|---|---|
| `tr-page-01.png` | outer cover | title, authors, TR 85-650, October 1984, revised February 1985, Cornell affiliation, support footnote |
| `tr-page-02.png` | title/abstract leaf | title, authors, 30 October 1984, revised 20 February 1985, abstract, keywords |
| `tr-page-03.png` | body p. 1 | introduction and beginning of safety examples |
| `tr-page-04.png` | body p. 2 | safety universe, safety definition, stuttering footnote |
| `tr-page-05.png` | body p. 3 | liveness examples and liveness definition |
| `tr-page-06.png` | body p. 4 | maximality argument, uniform liveness, absolute liveness, inclusion chain beginning |
| `tr-page-07.png` | body p. 5 | inclusion chain, leads-to, predictive example, Section 4 beginning |
| `tr-page-08.png` | body p. 6 | until, total correctness, topology, Theorem 1 beginning |
| `tr-page-09.png` | body p. 7 | Theorem 1 proof, first corollary, temporal-logic/Plotkin claim, Theorem 2 and proof |
| `tr-page-10.png` | body p. 8 | second corollary with intersection wording, Boolean closure, conclusion, acknowledgments |
| `tr-page-11.png` | body p. 9 | complete references |

## Manuscript/source-record lines read

I directly read every in-scope line in the round-three snapshot:

| Artifact | Lines read |
|---|---:|
| `handbook/parts/p09/presentations/n-c-012.tex` | 2632--3011 |
| `handbook/parts/p09/logic-in-computer-science.tex` | 710--718 |
| `handbook/bib/handbook.bib` | 6056--6080 |
| `spec/research/p09-alpern-schneider-1985-source-note.md` | 1--681 |
| `spec/research/p09-source-presentations-lot2-3.md` | 395--552 |

## Round-three correction checks

| Required round-three correction | Checked result |
|---|---|
| Distinguish the source's conditional liveness claim for leads-to from its unqualified non-absolute-liveness claim. | checked-clean: `n-c-012.tex` lines 2773--2780, source note lines 283--291, and compact record lines 470--483 preserve the two source strengths and mark the repair as handbook-owned. |
| Type one-state finite words, constant executions, concatenated witnesses, and one-letter cylinders before use. | checked-clean: `n-c-012.tex` lines 2642--2657 and 2840--2845, source note lines 120--139 and 375--381, and compact record lines 423--430 define the needed typed objects before using them. |
| Use the source-exact name `until`, not `strong-until`. | checked-clean: journal p. 183 and TR body p. 6 print `Until`; manuscript lines 2830--2838, source note lines 355--371, and compact record lines 488--489 use `until` only. |
| Include the leads-to defect in the source-critical findings table. | checked-clean: source note line 641 includes AS-06 for the leads-to overbreadth and required treatment. |
| Report the Plotkin temporal-logic decomposition only as an independently unverified private-communication claim. | checked-clean: journal p. 184 attributes the temporal-logic liveness-factor claim to Plotkin [8], and journal p. 185 lists [8] as private communication, 1983. Manuscript lines 2905--2909, source note lines 468--472 and 594--599, and compact record lines 512--516 do not promote it to a proved article theorem or independent verification. |

The handbook-owned state-set assertion for leads-to is also checked-clean. Under the state-set rendering, the three conditions \(E_1\ne\varnothing\), \(E_2\ne\varnothing\), and \(S\setminus(E_1\cup E_2)\ne\varnothing\) are sufficient because \(e_2^\omega\) is a uniform suffix for \(e_2\in E_2\), while \(c^\omega\) with \(c\) neutral is a satisfying execution made non-satisfying by prefixing \(\langle e_1\rangle\). They are necessary for the stated uniform-but-not-absolute separation: if \(E_1=\varnothing\), the property is all of \(S^\omega\); if \(E_2=\varnothing\) with \(E_1\ne\varnothing\), a one-state \(E_1\)-prefix has no satisfying continuation; and, once \(E_1,E_2\) are nonempty, if no neutral state exists, every satisfying suffix contains an \(E_2\)-state and therefore answers all finitely prepended \(E_1\)-requests, so absolute liveness holds.

## Coverage table

| ID | Status | Evidence/check |
|---|---|---|
| M01 | checked-clean | Recomputed all seven SHA-256 identities with `Get-FileHash`; all matched the round-three charter. |
| M02 | checked-clean | Visually read journal pp. 181--185 and all eleven report file pages from existing PNG images at original detail. |
| M03 | checked-clean | Journal title, authors, venue, volume/issue/date/page range, receipt/revision dates, communication editor, ISSN/copyright line, and DOI/bibliographic access route were reconciled against visual pages and citation/access records; TR number/date/revision/access route were reconciled against TR cover/title pages and bibliography/source-note records. |
| M04 | checked-clean | Page maps in the source note match the visual page contents. Journal and revised report agree substantively while preserving journal control; Corollary 2.1 has the same intersection-closure wording in both sources. |
| M05 | checked-clean | \(S\ne\varnothing\), \(S^*\), \(S^\omega\), empty sequence membership, concatenation, prefix, one-state finite words, constant executions, property standing, membership notation, program satisfaction, and terminal-state padding are source-faithful or explicitly marked as handbook clarification/repair. |
| M06 | checked-clean | Safety quantifiers and finite bad-prefix reading match journal p. 182/TR body p. 2 and are not strengthened. |
| M07 | checked-clean | `live for P` is correctly kept as a prefix/property relation; liveness is its universal closure over \(S^*\), with nonemptiness and full-space boundary stated. |
| M08 | checked-clean | Proof-method motivation, maximality argument, examples, and stuttering qualification are reported at source strength without making proof-rule or uniqueness claims. |
| M09 | checked-clean | Uniform and absolute liveness definitions, standing, nonredundancy, use, and inclusion chain match journal p. 183/TR body pp. 4--5. |
| M10 | checked-clean | Leads-to example preserves printed conditional liveness, printed unqualified non-absolute claim, and handbook-owned fixed-hypothesis repair without laundering the repair as source text. |
| M11 | checked-clean | Predictive example is source-faithful; manuscript nondegeneracy hypotheses and \(P_{A,B}\) rendering are handbook-owned quantifier reconstruction, not printed wording. |
| M12 | checked-clean | Until and total-correctness examples match source terminology and block a safety/liveness dichotomy. |
| M13 | checked-clean | Cylinder basis and safety/closed and liveness/dense equivalences match journal p. 184/TR body p. 6; direction proofs are correctly identified as handbook-supplied. |
| M14 | checked-clean | Theorem 1 construction, set algebra, minimal-closed-superset density proof, and nonuniqueness/syntax/algorithm boundaries are source-faithful at exact strength. |
| M15 | checked-clean | Corollary 1.1 preserves complement, intersection, and topological-closure hypotheses and remains conditional. |
| M16 | checked-clean | Theorem 2, \(L_a,L_b\) to \(E_a,E_b\) alpha-renaming, density/disjointness, factorization, and materiality of \(|S|>1\) are correct and source-faithful. |
| M17 | checked-clean | Corollary 2.1 is preserved as printed; the intersection-closed denotation-family countermodel and union/Boolean-closure repairs are explicitly handbook-owned and mathematically sufficient. |
| M18 | checked-clean | Boolean-closure entries and the claim that only \(S^\omega\) is both safety and liveness match the source's Boolean-operation paragraph and are not overread. |
| M19 | checked-clean | Manuscript and source note correctly separate printed proofs of Theorems 1--2, stated topological equivalences, unnumbered inclusion-chain argument, handbook proofs, and private-communication claims. |
| M20 | checked-clean | Definition-before-use and AGENTS terminology rule are satisfied for `live for P`, uniform liveness, absolute liveness, \(P_{A,B}\), \(L_P\), \(E_a,E_b\), \(Q\), and \(\mathcal F\); all are either source terms, semantic property classes, or eliminable metalinguistic abbreviations with stated use. |
| M21 | checked-clean | Reader, shared definition, bibliography, source note, and compact presentation agree claim by claim within their intended granularity. |
| M22 | checked-clean | Unlettered register standing, rights boundary, topic-only status, and no-test/no-build boundary are explicit and source-faithful. |

## Findings

No R3-SF-* findings are filed. I found no blocker, must-fix, should-fix, or source-fidelity defect under this seat's mandate on the frozen round-three snapshot.

VERDICT: ACCEPT
