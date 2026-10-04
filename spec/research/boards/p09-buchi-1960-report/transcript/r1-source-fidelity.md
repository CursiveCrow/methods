# R1 source-fidelity and evidence report: Büchi 1959 UMR1083 precursor

Seat: source fidelity and evidence.

Owned file: `spec/research/boards/p09-buchi-1960-report/transcript/r1-source-fidelity.md`.

I remained blind: I read the board charter and the six frozen artifacts in their scoped ranges, visually inspected the 48 rendered report pages at original detail, and did not read any ledger, chair file, other transcript, other board, or other reviewer verdict. I did not contact another reviewer. I did not edit any frozen artifact. I did not run a test, test harness, automated checker, repository script, TeX command, handbook build, or handbook-PDF inspection. The OCR was not used as controlling evidence.

## Frozen identity check

All six frozen SHA-256 identities were recomputed before judgment and matched the charter values.

| Frozen artifact | Charter SHA-256 | Recomputed result |
|---|---:|---|
| `tmp/pdfs/p09-buchi-1960/buchi-1959-umr1083.pdf` | `18D1BF4C44E9581932239B500DA8E220876AD7F9B602451BF6B9B22795F840FD` | matched |
| `handbook/parts/p09/presentations/n-c-014.tex` | `1D4E34CE6B2602BEF520146ECC6F78C492A969CE6C8FE884912DC0959AFF6713` | matched |
| `handbook/parts/p09/logic-in-computer-science.tex` | `1690DED84FC257B50BC5B44E094E382D8A79B176E7BB9C21D0845DAEC59629B8` | matched |
| `handbook/bib/handbook.bib` | `FAACDA885C9671FD41509F0FCB24934CBA0B4AFD8BC1E6368C2DE355E8B03DFA` | matched |
| `spec/research/p09-buchi-1960-source-note.md` | `15165056F88D051DB0A5CB33B3C55A79F39AF2EEE62C507C756226CF851B411E` | matched |
| `spec/research/p09-source-presentations-lot2-3.md` | `E7DD8167EA70A32F72F09C12A478637F8C5ECCB3C7AA6E98BCC7918ECFB00285` | matched |

## Source-page inspection record

I visually inspected `page-01.jpg` through `page-48.jpg` under `tmp/pdfs/p09-buchi-1960/rendered/` at original detail. The map is confirmed: cover, funding leaf, printed pages 1--45, endpoint leaf.

| Rendered page | Printed page | Source evidence inspected |
|---:|---:|---|
| page-01 | cover | University of Michigan, College of Literature, Science, and Arts; Logic of Computers Group technical report; title `WEAK SECOND-ORDER ARITHMETIC AND FINITE AUTOMATA`; J. Richard Büchi; University of Michigan Research Institute, Ann Arbor; September 1959. |
| page-02 | funding leaf | Technical-report funding and contract page; handwritten UMR1083; NSF, ONR, Army Ordnance, and Army Signal Supply Agency sponsorship statements. |
| page-03 | 1 | Introduction; Kleene synthesis/analysis framing; Theorems 1 and 2 announced as Section 4 equivalents; 1958 Notices AMS footnote. |
| page-04 | 2 | Variable sorts: individual, propositional, monadic predicate, propositional formula variables; notation for formulas; restricted/monadic second-order predicate-calculus setup. |
| page-05 | 3 | Tuple/vector notation and notation overload; interpreted formulas; no deductive calculus supplied. |
| page-06 | 4 | Truth values; predicate as function from natural numbers to truth values; special predicate as ultimately false finite set; \(n\)-predicate; \(W.2.A.\) interpretation with zero and successor. |
| page-07 | 5 | \(W.2.A.\) named; Lemma 1 local normal form statement and proof begins. |
| page-08 | 6 | Lemma 1 proof continues/completes; Section 3 begins; Definition 1 starts: automaton data \(E^m,H^m[Y^m,X^n]\) and binary output \(U[Y^m]\). |
| page-09 | 7 | Definition 1 transition recursion and output predicate; Definition 2 special output; Definition 3 behavior begins. This page controls finding R1-SF-01. |
| page-10 | 8 | Definition 3 behavior completed; length of special input; property (*) using \(U[r(l+1)]\); Lemma 2 complement; Definition 4 expanded form; Lemma 3. |
| page-11 | 9 | Expanded-form construction details. |
| page-12 | 10 | Expanded-form specialness preservation; Lemma 4 guessed input track begins. |
| page-13 | 11 | Lemma 4 continues. |
| page-14 | 12 | Lemma 5 finite look-ahead output; condition `(c)` uses stability through false-input transition, corroborating R1-SF-01. |
| page-15 | 13 | Lemma 5 concludes; Lemma 6 statement/proof; line `(4)` again uses state-variable stability under false input, corroborating R1-SF-01. |
| page-16 | 14 | Lemma 6 concludes; Section 4; Lemma 7 local base statement. |
| page-17 | 15 | Lemma 7 construction details. |
| page-18 | 16 | Theorem 1 synthesis statement and construction roles: Lemma 1, Lemma 7, expanded form, projection, complement. |
| page-19 | 17 | Theorem 2 analysis statement and proof; transit predicates made special using cutoff construction because unrestricted \(r\) need not be special. |
| page-20 | 18 | Theorem 2 proof completed; Section 5; Definition 5 normal form begins; interpreted system notation and comparison with stronger systems. |
| page-21 | 19 | Theorem 3 free-individual normal form; free individuals represented by special initial-segment predicates. |
| page-22 | 20 | Corollary 1 finite decision proof by finite path and loop deletion; Corollary 2 begins. |
| page-23 | 21 | Corollary 2 proof: ultimately periodic sets; phase and period effectively obtainable. |
| page-24 | 22 | Corollary 2 ends; relations and Corollary 3. |
| page-25 | 23 | Corollary 4; binary expansion map \(f(i)=\sum i(x)2^x\); \(\operatorname{Pw}_2\); Theorem 4 begins. |
| page-26 | 24 | Theorem 4 proof with addition/carry predicate and \(\operatorname{Pw}_2\) bit test; translations in both directions. |
| page-27 | 25 | Corollary 5 decidability of \([=,+,\operatorname{Pw}_2]\); relation adjunction; Theorem 5 comparison. |
| page-28 | 26 | Section 6 comparison with other finite-automata concepts; explicit distinction between source automaton and transition system. |
| page-29 | 27 | Many-input extension and Definition 1′ begins. |
| page-30 | 28 | Definition 3′; Theorems 1′ and 2′ for many-input form. |
| page-31 | 29 | Many-input proof sketch; special predicates versus finite input strings; generalized calculus mentioned but not supplied. |
| page-32 | 30 | Section 7 exact finite-string encoding with terminal \(\top^n\) marker and all-false tail. |
| page-33 | 31 | Empty-string convention; finite \(n\)-string length convention; Definition 6 string behavior; Theorem 6 begins. |
| page-34 | 32 | Theorem 6 both directions; behavior and string behavior distinguished. |
| page-35 | 33 | Theorem 7; Theorem 8 four equivalent conditions: string behavior, special-output behavior, \(W.2.A.\) sg-formula definability, regularity. |
| page-36 | 34 | Definition 7 regular relation; Theorem 8′ for relations; equi-response relation. |
| page-37 | 35 | Binary-expansion regularity discussion and modified binary expansion; empty string represents 0. |
| page-38 | 36 | Theorem 9: \([=,+,\operatorname{Pw}_2]\)-definable relations exactly 2-regular; base-\(k\) setup. |
| page-39 | 37 | Base-\(k\) qualifications; initial segment, terminal segment, and concatenation distinctions. |
| page-40 | 38 | Base-\(k\) consequences; ultimately periodic/1-regular sets are \(k\)-regular; power-predicate equivalences. |
| page-41 | 39 | Proof skeleton for base-\(k\)/base-\(n\) regularity noncoincidence. |
| page-42 | 40 | Base-equivalence results and simple representatives. |
| page-43 | 41 | Binary-to-ternary nonexistence consequence; Section 8 feedback comparison begins. |
| page-44 | 42 | Union, concatenation, and star formulas; finite-set quantifier corresponds to feedback/Kleene star; Section 9 unsolved problem begins. |
| page-45 | 43 | Problem 1; Theorem 10; end of mathematical text. |
| page-46 | 44 | Bibliography entries [1]--[12]. |
| page-47 | 45 | Bibliography entries [13]--[15]; numbered report endpoint. |
| page-48 | endpoint leaf | University of Michigan barcode/end leaf; physical endpoint. |

## Frozen manuscript and record material read

- `handbook/parts/p09/presentations/n-c-014.tex` lines 1--213, especially the report reconstruction at lines 8--166 and the report/journal boundary at lines 8--16.
- `handbook/parts/p09/logic-in-computer-science.tex` lines 811--816.
- `handbook/bib/handbook.bib` lines 6099--6120.
- `spec/research/p09-buchi-1960-source-note.md` lines 1--318.
- `spec/research/p09-source-presentations-lot2-3.md` lines 620--630 and the scoped open/source-sufficiency entries at lines 898 and 905.

## Finding

### R1-SF-01 — Blocker — Definition 2's special-output identity is transcribed with the wrong left side

Affected frozen manuscript/source-record lines:

- `handbook/parts/p09/presentations/n-c-014.tex:47-56`
- `spec/research/p09-buchi-1960-source-note.md:152-158`
- `spec/research/p09-source-presentations-lot2-3.md:624`

Exact source page:

- Printed report p. 7, Definition 2, visually inspected at `tmp/pdfs/p09-buchi-1960/rendered/page-09.jpg`. Corroborating uses appear on printed pp. 12--13 (`page-14.jpg`, `page-15.jpg`) in Lemmas 5--6.

Invariant violated:

- I6, because the special-output identity is not the exact printed stability identity.
- I15, because the frozen reader, source note, and compact source record all present the same altered formula as source statement.
- I24, because the altered formula is a mathematically material ambiguity/error for a graduate reader.

Evidence:

The report's Definition 2 says a binary output \(U[Y]\) is special for the automaton when the propositional output is stable under the all-false input transition as a function of the transit/state variables:

\[
U[Y]\equiv U[H[Y,\Lambda^n]].
\]

The frozen reader instead states:

\[
U[\bot^m]\equiv U[H(Y^m,\bot^n)]
\]

at `n-c-014.tex:51-53`. The same wrong left side appears in the source note at `p09-buchi-1960-source-note.md:155` and the compact record at `p09-source-presentations-lot2-3.md:624`.

Harm:

The source condition is statewise invariance of the output formula after one false-input transition. It says that, for every current transit value \(Y^m\), \(U\) has the same value before and after applying \(H(Y^m,\Lambda^n)\). The frozen formula instead compares \(U\) at the all-false transit value with \(U\) after the false-input transition from arbitrary \(Y^m\). That is a different and generally stronger/incorrect condition: it can exclude source-special outputs whose value is invariant along the false-input transition but not equal to \(U[\bot^m]\). It also misstates the mechanism by which special input makes the output predicate eventually constant, and it contaminates downstream references to special output in Definition 3, Lemmas 3/5/6, and Theorems 1--2.

Minimum repair:

Replace the special-output identity everywhere it appears as source wording with the state-variable identity

\[
U[Y^m]\equiv U[H(Y^m,\bot^n)]
\]

or an explicit universally quantified equivalent over \(Y^m\). Then adjust the explanatory sentence to say that the output is invariant under the all-false input transition, not that it is forced to equal the all-false-state output value. Recheck all downstream uses of “special output” after that correction, especially the eventual-constancy explanation and the proofs or summaries of Lemmas 3, 5, 6 and Theorems 1--2.

## Source-fidelity determinations

Apart from R1-SF-01, the frozen reconstruction is source-honest at this seat's mandate:

- Report identity, institutional series, date, and UMR1083 precursor status match the visually inspected cover/funding leaves and the bibliography/source records.
- The 1959 report and registered 1960 journal article are kept separate. The frozen record does not claim the report is a page-for-page verified copy of the journal article; `p09-source-presentations-lot2-3.md:898` and `:905` keep literal journal reconciliation open.
- The language is correctly presented as \(W.2.A.\), with natural-number individuals, zero/successor vocabulary, monadic predicate variables over special predicates, and no supplied deductive calculus.
- Definition 1's source automaton is correctly treated as propositional-formula data \(E^m,H^m[Y^m,X^n]\) inducing deterministic bit-state recursion, not as a modern nondeterministic tuple.
- Definition 3's behavior is correctly located as eventual permanent truth over special inputs; Section 7's string behavior is separately tied to the terminal marker and arbitrary output.
- Lemma 1, Lemmas 2--7, Theorems 1--4, Theorems 6--9, Corollaries 1--5, and Section 8 are summarized at source-level strength and with no detected source-laundering into later journal wording, except where the special-output formula error affects the local definition and its downstream explanation.
- The shared finite-word theorem and bibliography preserve the report/article/Elgot/Trakhtenbrot separation at the scoped lines inspected.
- Rights and scope are qualified: public repository access is not treated as an open-content license, and acceptance would be limited to the 1959-report-strength precursor presentation only.

## Mandatory coverage ledger

| Item | Status | Seat-specific determination |
|---|---|---|
| M01 | checked-clean | All six frozen hashes were recomputed and matched before judgment. |
| M02 | checked-clean | All 48 rendered report pages were visually read; cover/funding/printed pp. 1--45/endpoint map confirmed. |
| M03 | checked-clean | Report identity, institutional series, September 1959 date, UMR1083/Deep Blue route, registered 1960 article identity/DOI, report/article/reprint boundary, access route, and rights qualification are source-supported. |
| M04 | checked-clean | Variable sorts, natural-number domain, zero/successor vocabulary, predicate domain, special-predicate definition, \(n\)-predicate standing, and absence of a deductive calculus match printed pp. 2--5 and frozen lines. |
| M05 | checked-clean | Definition 1's automaton data \(E^m,H^m[Y^m,X^n]\), transition recursion, binary output, and deterministic bit-state standing are source-supported. |
| M06 | finding-linked | R1-SF-01: Definition 2's special-output identity is not copied faithfully. |
| M07 | finding-linked | Definition 3's behavior quantifiers and special-input/output/behavior-set distinctions are otherwise source-supported, but the special-output premise feeding eventual constancy is affected by R1-SF-01. |
| M08 | checked-clean | Lemma 1's local normal form and the recorded proof architecture are source-supported. |
| M09 | finding-linked | Lemmas 2--7 and their differentiated roles are source-supported, but the special-output identity used in Lemmas 3/5/6 is affected by R1-SF-01. |
| M10 | not-checked with reason | Independent rederivation of Theorem 1 through arbitrary finite-set quantifier prefixes is outside this source-fidelity seat's charter coverage; I checked source support and dependency attribution only. |
| M11 | not-checked with reason | Independent rederivation of Theorem 2's analysis formula is outside this source-fidelity seat's charter coverage; I checked source support for the cutoff-special-witness argument and note that its special-output premise is affected by R1-SF-01. |
| M12 | checked-clean | Definition 5, Theorem 3, and Corollary 1's finite path/loop-deletion decision argument are source-supported at printed pp. 18--20. |
| M13 | checked-clean | Corollary 2's ultimately periodic characterization and effective phase/period extraction are source-supported at printed pp. 20--22. |
| M14 | checked-clean | Binary-expansion bijection, Theorem 4 translations, carry predicate, \(\operatorname{Pw}_2\) bit test, and Corollary 5 are source-supported at printed pp. 23--25. |
| M15 | checked-clean | Finite-word encoding, empty word, data positions, terminal \(\top^n\) marker, false tail, and length convention are source-supported at printed pp. 30--31. |
| M16 | checked-clean | Definition 6 and both directions of Theorem 6 are source-supported, with behavior and string behavior kept distinct. |
| M17 | checked-clean | Theorems 7--8, the four equivalent conditions, effective direction claims, and dependence on the regular-language theorem are source-supported at printed p. 33. |
| M18 | checked-clean | Theorem 8′, regular relations, binary-expansion regularity, and base-\(k\)/base-\(n\) consequences are source-supported at printed pp. 34--41. |
| M19 | checked-clean | Section 8's union, concatenation, star, feedback, and finite-set-quantifier comparison are source-supported at printed pp. 41--42. |
| M20 | finding-linked | Cross-record reconciliation found the same special-output formula error in the reader, source note, and compact record. Shared theorem, bibliography, open ledger entry, and source-sufficiency statement are otherwise clean. |
| M21 | finding-linked | Page locators, theorem numbers, cross-references, and source-versus-modern attribution are otherwise clean, but the Definition 2 formula locator points to a source page whose formula is miscopied; see R1-SF-01. |
| M22 | finding-linked | AGENTS terminology rule checked. Source-defined terms have standing and use; however, “special output” lacks the exact eliminable source definition in the frozen text until R1-SF-01 is repaired. No additional coined-term violation found. |
| M23 | checked-clean | Report/journal boundary is honest: the report-controlled material is not laundered into a verified 1960-journal claim, and literal journal reconciliation remains open. |
| M24 | finding-linked | R1-SF-01 is a mathematically material false compression of the source stability condition that a graduate reader could misread. No separate material ambiguity found. |
| M25 | checked-clean | Topic-only scope, rights boundary, and explicit no-test/no-build boundary are enforced in the frozen record and in this review. |

VERDICT: REJECT R1-SF-01
