# R1 source-fidelity and evidence report: Elgot 1961, N-c-014.b

Seat: blind source-fidelity and evidence reviewer.

Scope observed: I read the charter completely before judgment, remained within the authorized frozen artifacts and source renders, did not read the ledger, chair transcript, any other board transcript, any Büchi board/transcript, or another Elgot transcript/verdict, and did not contact another reviewer. I edited only this owned transcript. I did not run tests, automated checkers, repository scripts, TeX, builds, or handbook-PDF inspection. OCR/text extractions were not used to control any mathematical symbol, formula, pagination, or wording.

## Frozen identity check

I recomputed the SHA-256 identity of every frozen round-one object. All eight matched the charter:

| Artifact | Recomputed SHA-256 | Status |
|---|---:|---|
| `tmp/pdfs/p09-elgot-1961/elgot-1961-trans-ams.pdf` | `DE2F9587F72075C94C7071A00002D1129AA8148C498F9A4D6F75968EB46ACD74` | checked-clean |
| `tmp/pdfs/p09-elgot-1961/elgot-1959-umr1342.pdf` | `596A599A7DF12F122BB2D875255B050695EC84A5A22F3488844D5876F3211D74` | checked-clean |
| `tmp/pdfs/p09-elgot-1961/elgot-1962-errata.pdf` | `B13E422FC03DDA61B93A1B782F40882AE90DBC8886945B26A42376A96ED34EC1` | checked-clean |
| `handbook/parts/p09/presentations/n-c-014.tex` | `C37C4F9F7D093D75DD33E90FBD6050C55F147B3C7A71933D8891D4DDF46AF20A` | checked-clean |
| `handbook/parts/p09/logic-in-computer-science.tex` | `1690DED84FC257B50BC5B44E094E382D8A79B176E7BB9C21D0845DAEC59629B8` | checked-clean |
| `handbook/bib/handbook.bib` | `6F98B6EB38B2B935DACC0C7E8373E1B12A5BB70FCAAC172D11BAFCDACA8C502F` | checked-clean |
| `spec/research/p09-elgot-1961-source-note.md` | `292B5EFD5972B27DC5043AF39FE20B1AB3ABE487290C3699031A79ED18472DA7` | checked-clean |
| `spec/research/p09-source-presentations-lot2-3.md` | `12CAA5ADB48E78D809F3EE6C8EA6FFBF98C504E0F7920A555DD9C378824ACAC7` | checked-clean |

## Visual source inspection

I visually inspected at original detail all required source renders.

Journal article, `rendered/page-01.jpg` through `rendered/page-31.jpg`, printed pp. 21--51:

- Printed p. 21: title, author, introductory Chapter I.
- Printed p. 22: §2 definition of the \(I\)-automaton, including \(I\), \(S\), \(f:I\times S\to S\), \(d\in S\), \(D\subseteq S\), run recursion, and null-sequence case.
- Printed pp. 23--24: §§3.2--3.6, projection material, and the displayed ordered-pair error later corrected by errata.
- Printed pp. 25--27: truncation lemma, \(L_1\), \(L_1^1\), finite-set semantics, admissible encodings, \(U_r\), \(U_r^0\), \(0_r\), and Theorem 5.3 statement.
- Printed pp. 28--31: Lemmas 5.4--5.5, proof of Theorem 5.3(a), proof of Theorem 5.3(b), state-coordinate encoding, and \(\Lambda\) handling.
- Printed pp. 31--37: Corollary 5.8, \(\tau(F)=\sum_{x\in F}2^x\), finite-carry addition, Presburger consequence, power-of-two extension, and finite/cofinite or quasi-finite variants.
- Printed pp. 37--43: Chapter III, \(A\)-extendability, strong \(A\)-extendability, Lemma 6.1, Lemmas 6.3--6.5, \(A/B\)-automata, finite behavior, Theorem 7.1, and Theorem 7.3.
- Printed pp. 44--47: Theorem 8.1, Corollary 8.2 including the vacuous \(\gamma_A=\varnothing\) case, §8.3 formula encoding, §8.4--§8.5, and §8.6.1--§8.6.4 including the printed false §8.6.2 sentence.
- Printed pp. 47--50: Chapter IV, Lemma 10.1, Theorem 10.2, §§10.3--10.5, and Corollary 10.6.
- Printed p. 51: bibliography endpoint.

Report, `report-rendered/page-01.jpg` through `report-rendered/page-60.jpg`:

- PDF pp. 1--5: cover, grant/funding leaf, acknowledgments p. iii, contents p. v, abstract p. vi.
- PDF pp. 6--55: report numbered pp. 1--50, complete body.
- PDF pp. 56--59: distribution list leaves.
- PDF p. 60: University of Michigan barcode endpoint.
- Version-specific checks: report p. 4 already prints \(\widehat p\) in the projection passage where the journal erratum corrects \(\widehat f\); report p. 6 shares the \((a,b)\) ordered-pair error; report p. 41 shares the false §8.6.2 one-relation assertion; the report otherwise has the same mathematical divisions and theorem numbering used by the manuscript/source note.

Errata, `elgot-1962-errata-page-1.jpg` and `elgot-1962-errata-page-2.jpg`, printed pp. 558--559:

- Printed p. 558 begins the Elgot errata after the preceding article endpoint. It verifies all six listed corrections: p. 23 lines 10--11 \(\widehat f\mapsto\widehat p\); p. 23 §3.6(b) line-break correction; p. 24 line 9 second display \((a,b)\mapsto(b,a)\); p. 46 §8.6.2 line 5 \(n\) one more than the maximum; p. 46 §8.6.2 line 7 "for some \(R\) which is \(n\)-ary"; and replacement of the third sentence of §8.6.2 by the finite-union correction.
- Printed p. 558 also verifies the explicit \(k=2\) counterexample and begins the repair by adding a third coordinate/tagged formula \(Q\).
- Printed p. 559 verifies the disjoint tagged field construction, tagged relations \(R'_j\), tagged prefix sets \(E'_j\), relation/prefix-set union, projection \(p(\langle a,j\rangle)=a\), and projection equality \(\widehat p(S)=S_1\cup\cdots\cup S_k\).

## Source-fidelity judgment

I found no blocker, must-fix, or finding-worthy source-fidelity defect in the frozen N-c-014.b reconstruction.

The manuscript line 231--236 authority statement is source-faithful: the 1961 journal article controls the body, the 1959 UMR1342 report is a complete primary precursor with same section/theorem architecture, and the 1962 errata controls corrections. This matches the source note's authority discussion and visual page identities.

The §2 acceptor presentation at manuscript lines 238--256 is faithful to journal printed pp. 21--22: \(I\) is the finite nonempty input alphabet, \(S\) is the finite nonempty internal-state set, the automaton is \((S,f,d,D)\), \(f:I\times S\to S\), \(d\in S\), \(D\subseteq S\), the run begins at \(s_0=d\), transitions by \(s_{k+1}=f(i_k,s_k)\), and the empty word is accepted exactly when \(d\in D\). The manuscript also correctly keeps alphabet, state set, transition, run, and accepted language distinct.

The finite-set encoding at manuscript lines 258--286 is faithful to journal printed pp. 26--27. \(L_1^1\) has individuals over \(\mathbb N\) and monadic variables over finite subsets of \(\mathbb N\). \(U_r=\{0,1\}^r\), \(0_r=(0,\ldots,0)\), \(U_r^0=U_r\setminus\{0_r\}\), the all-empty assignment is \(\Lambda\), nonempty encodings stop at the last nonzero column, and the admissible words are exactly \(U_r^*U_r^0\cup\{\Lambda\}\). The manuscript distinguishes formulas, assignments, characteristic columns, and \(T_r(A)\).

The Theorem 5.3 summary at manuscript lines 288--329 is source-faithful to journal printed pp. 27--31. It states both effective directions and attributes proof ownership correctly: formula-to-language uses Lemmas 5.4--5.5, Boolean operations, existential-set projection plus right truncation, and local principal-pattern regular expressions; language-to-formula encodes automaton states in extra coordinates, defines start/terminal/local-adjacency sets, existentially removes state coordinates, and handles \(\Lambda\) separately. I did not identify source laundering into a generic modern MSO/regular theorem.

The arithmetic consequences at manuscript lines 331--343 are faithful to journal printed pp. 31--37: Corollary 5.8 is stated as a truth decision for \(L_1^1\), \(\tau(F)=\sum_{k\in F}2^k\) and a finite carry relation support addition/Presburger consequences, and the power-of-two and finite/quasi-finite variants are presented as consequences at their exact strength, not as alternative automaton definitions or blanket arithmetic-design decidability.

The \(A/B\)-automaton and finite-behavior synthesis material at manuscript lines 345--393 is source-faithful to journal printed pp. 37--46. The tuple is \((S,f,d,g)\), \(f:A\times S\to S\), \(d\in S\), \(g:S\to B\), with synchronous finite input/output pairing and the empty paired word. Theorem 7.1's regularity, openness/prefix-closure, functionality, and input-totality clauses are all present. \(A\)-extendability, strong \(A\)-extendability, \(\gamma_A\), Theorem 8.1, Corollary 8.2, and §8.3 are presented with distinct standings and source order.

The infinite-behavior boundary at manuscript lines 395--401 is source-faithful to journal printed pp. 43--44. The text describes Elgot's transducer behavior via finite prefixes, prefix functionality, and input totality, and explicitly prevents a Büchi-acceptance conflation.

The §8.6 correction at manuscript lines 403--438 is source-faithful to journal printed p. 46 and errata printed pp. 558--559. The manuscript correctly says the printed §8.6.2 third sentence is false, does not use it as true, gives the finite-union replacement \(S_1\cup\cdots\cup S_k\), states that \(n\) is one more than the greatest successor offset, notes \(k\) need not be one and the erratum's \(k=2\) example, and describes the disjoint tagged-copy repair, relation/prefix-set union, and projection step.

The negative boundary at manuscript lines 440--453 is faithful to journal/report printed pp. 47--50: Chapter IV uses Post-system encoding, Theorem 10.2 gives recursively enumerable but undecidable satisfiable formulas at maximal r.e. degree under the stated finite-predicate setting, §§10.3--10.5 transfer the result to the stated variants, and Corollary 10.6 distinguishes decidable satisfaction for a fixed input-free automaton from undecidable existence of some satisfying automaton.

The report/article comparison at manuscript lines 455--462 is source-faithful. The visual report confirms same divisions and theorem numbering; the report already has \(\widehat p\) at report p. 4, but shares the \((a,b)\) error at report p. 6 and the false §8.6.2 one-relation assertion at report p. 41. The manuscript correctly treats this as version evidence and assigns all corrections to the published errata, not to silent choice among versions.

The bibliography entries at `handbook/bib/handbook.bib` lines 5843--5873 match the article/report/errata identities used in the manuscript: Elgot 1961, Transactions AMS 98(1), pp. 21--51, DOI `10.1090/S0002-9947-1961-0139530-9`; Elgot 1959 UMR1342 report; and Elgot 1962 errata, Transactions AMS 103(3), pp. 558--559, DOI `10.1090/S0002-9947-62-99982-8`. The shared theorem line in `logic-in-computer-science.tex` lines 811--816 cites the finite-word correspondence context without adding an unsupported Elgot-specific claim. The source note and compact record are consistent with the reader on authority order, correction ownership, source sufficiency, and the "review pending" admission boundary.

## Mandatory item ledger

Assigned to this source-fidelity seat: M01--M07, M10--M11, and M17--M26.

| Item | Status | Evidence and judgment |
|---|---|---|
| M01 | checked-clean | All eight frozen hashes recomputed and matched before verdict; no frozen artifact was edited. |
| M02 | checked-clean | Visually read all 31 journal pages, all 60 report pages, and both errata pages at original detail; physical/printed maps confirmed as described above. |
| M03 | checked-clean | Article/report/errata identities, dates, series, DOI/handle-style bibliography data, access/rights qualifications, and authority order checked against source note, bibliography, manuscript lines 231--236 and 455--462, and visual source title/end pages. |
| M04 | checked-clean | §2 acceptor tuple, types, run recursion, final-state convention, and empty-word case checked against journal printed p. 22 and manuscript lines 238--256. |
| M05 | checked-clean | §§3--4 regularity/right truncation checked at source-fidelity depth against journal printed pp. 23--26 and report pp. 4--9; errata p. 558 verifies \(\widehat f\mapsto\widehat p\) and \((a,b)\mapsto(b,a)\). |
| M06 | checked-clean | \(L_1^1\) syntax/interpretation checked against journal printed pp. 26--27 and manuscript lines 258--263; formula/assignment standing remains distinct. |
| M07 | checked-clean | \(U_r\), \(U_r^0\), \(0_r\), admissible words, \(T_r(A)\), all-empty \(\Lambda\), and terminal-zero removal/projection distinction checked against journal printed pp. 26--30 and manuscript lines 265--286, 301--307. |
| M08 | not-checked with reason | Not assigned to this source-fidelity seat as an independent mathematical rederivation item; only source attribution and statement fidelity were checked. |
| M09 | not-checked with reason | Not assigned to this source-fidelity seat as an independent mathematical rederivation item; only source attribution and statement fidelity were checked. |
| M10 | checked-clean | Corollary 5.8, \(\tau\), finite carry, Presburger consequence, power-of-two extension, and finite/quasi-finite variants checked against journal printed pp. 31--37 and manuscript lines 331--343. |
| M11 | checked-clean | \(A/B\)-automaton tuple, synchronous finite behavior, and distinction from §2 acceptor checked against journal printed pp. 40--41 and manuscript lines 345--358. |
| M12 | not-checked with reason | Not assigned to this source-fidelity seat as an independent proof-verification item; source statement/order and later use were inspected. |
| M13 | not-checked with reason | Not assigned to this source-fidelity seat as an independent proof-verification item; source statement/order and locator fidelity were inspected. |
| M14 | not-checked with reason | Not assigned to this source-fidelity seat as an independent proof-verification item; the non-Büchi source boundary was checked. |
| M15 | not-checked with reason | Not assigned to this source-fidelity seat as an independent proof-verification item; source statement/order, empty case, and attribution were inspected. |
| M16 | not-checked with reason | Not assigned to this source-fidelity seat as an independent proof-verification item; source nonconflation of formula, automaton, and behavior was inspected. |
| M17 | checked-clean | §8.6 arbitrary-set interpretation, restricted form \(\exists\mathbf s\,\forall x\,M\), absence of equality/order in the local matrix, allowed numerals, and successor-offset convention checked against journal printed p. 46, errata pp. 558--559, and manuscript lines 403--423. |
| M18 | checked-clean | All six errata corrections, \(k=2\) counterexample, finite-union statement, tagged fields, tagged prefix sets, relation union, and projection equality directly verified on errata printed pp. 558--559 and reflected at manuscript lines 411--438. |
| M19 | checked-clean | Corrected §8.6.2 plus §8.5 reduction source chain checked at source-fidelity/source-reasoning depth: manuscript lines 425--437 do not use the false single-relation sentence and match errata pp. 558--559 and journal printed pp. 45--47. |
| M20 | checked-clean | Lemma 10.1, Theorem 10.2, §§10.3--10.5, and Corollary 10.6 positive/negative boundary checked against journal printed pp. 47--50, report pp. 43--47, and manuscript lines 440--453. |
| M21 | checked-clean | Complete report/article comparison at every used claim checked; report p. 4 \(\widehat p\), report p. 6 \((a,b)\), report p. 41 §8.6.2, same architecture, and pagination distinction are correctly attributed at manuscript lines 455--462. |
| M22 | checked-clean | Reader claims reconciled with the source note, compact record, shared theorem, bibliography, and status/open-ledger excerpt authorized by charter; no conflict found. |
| M23 | checked-clean | Locators, theorem numbers, cross-references, citations, historical attribution, and source-versus-modern qualifications inspected; no mislocator or unsupported attribution found. |
| M24 | checked-clean | AGENTS terminology rule applied. New or potentially technical names are introduced with source-backed need, eliminable definition or immediate source description, clear standing, distinction from neighboring terms, and actual use: \(I\)-automaton, admissible, \(T_r(A)\), \(A/B\)-automaton, \(A\)-extendable, strongly \(A\)-extendable, \(\gamma_A\), arbitrary-set interpretation, and the correction vocabulary all pass. Descriptive exclusions such as "not a Büchi acceptance theorem" do not introduce a new object. No definition-after-use, redundant name, standing ambiguity, or unused distinction found. |
| M25 | checked-clean | Adversarial source-fidelity inspection found no false compression, hidden hypothesis, source laundering, correction laundering, misleading singular/plural, empty-case omission, or completion inflation. The most dangerous singular/plural trap, the §8.6.2 one-relation claim, is explicitly corrected to finite union/tagging. |
| M26 | checked-clean | Topic-only scope, rights boundary, and no-test/no-build boundary were observed. Acceptance, if granted, is limited to N-c-014.b at the frozen article-plus-errata manuscript-content level. |

## Findings

No findings. No blocker or must-fix remains under the source-fidelity and evidence mandate.

VERDICT: ACCEPT
