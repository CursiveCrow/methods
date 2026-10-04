# Round 2 source-fidelity deliberation

### F9 — still-open

- current location: `spec/provenance/inherited-bibliography-field-ledger.csv:1-65`; `spec/provenance/SRC-16803-17196.json:37-71`
- position: The requested row-by-row semantic comparison is now complete, but the generated control is not: all 64 rows still say `static_field_status=pass, semantic_field_review=pending`. Seven rows also contain concrete role-level discrepancies. A token/year match is not enough to clear those rows.
- concrete discrepancies:
  - D1, row 2 `AMSMathGuide` (`csv:3`; `handbook/bib/handbook.bib:16-20`): the source names two institutional authors, “American Mathematical Society and the LaTeX Project”; the BibLaTeX field braces the whole phrase as one literal corporate author. Preserve two institutional names, for example `{American Mathematical Society} and {The LaTeX Project}`.
  - D2, row 31 `Isabelle2025` (`csv:32`; `handbook/bib/handbook.bib:294-299`): `year=2025` promotes digits embedded in the release/title `Isabelle2025-2` to a publication-year field. The source item states no standalone publication date. Supply authoritative release metadata or omit the year field rather than infer its role from the title/key.
  - D3, row 38 `LeanManual2026` (`csv:39`; `handbook/bib/handbook.bib:356-363`): the source states version 4.32.1 and an access date, 9 August 2026. BibLaTeX correctly records `urldate`, but also converts the access year into `year=2026`, thereby asserting an unstated publication/release year.
  - D4, row 39 `LeanTPIL` (`csv:40`; `handbook/bib/handbook.bib:365-372`): the source supplies only “official online tutorial, retrieved 9 August 2026.” The conversion again duplicates the access year as a publication `year`.
  - D5, row 50 `RocqManual2026` (`csv:51`; `handbook/bib/handbook.bib:464-470`): the source supplies version 9.1.1 and a URL but no date at all. `year=2026` is inferred solely from the citation key/current context.
  - D6, row 58 `TPTP` (`csv:59`; `handbook/bib/handbook.bib:535-542`): the source supplies BNF revision 9.3.0.3, content hash, and retrieval date. `year=2026` converts the retrieval year into a publication year in addition to the correct `urldate`.
  - D7, row 64 `Unicode2025` (`csv:65`; `handbook/bib/handbook.bib:592-597`): the reader-facing source says Version 17.0, Chapter 22 and gives a URL; 2025 occurs only in the citation key, not as a stated publication date. The conversion manufactures `year=2025` from that identifier.
- row-by-row dispositions: `match` below means only that the converted fields preserve every bibliographic role explicitly asserted by the retained `\bibitem`; it is not a claim that external metadata was independently refreshed.
  - 1 `AMSAuthorHandbook` match; 2 `AMSMathGuide` D1; 3 `Avigad2018` match; 4 `BaazEglyLeitsch2001` match; 5 `BachmairGanzinger2001` match; 6 `Barwise1977` match; 7 `BarwiseFeferman1985` match; 8 `BlackburnDeRijkeVenema2001` match.
  - 9 `BoolosBurgessJeffrey2007` match; 10 `Buss1998` match; 11 `ChangKeisler1990` match; 12 `ChiswellHodges2007` match; 13 `Church1936` match; 14 `Cook1971` match; 15 `DavisLogemannLoveland1962` match; 16 `DavisPutnam1960` match.
  - 17 `DeMouraUllrich2021` match; 18 `EbbinghausFlumThomas1994` match; 19 `Enderton2001` match; 20 `GabbayPnueliShelahStavi1980` match; 21 `Gentzen1934a` match; 22 `Gentzen1935b` match; 23 `Girard1987` match; 24 `Godel1930` match.
  - 25 `Godel1931` match; 26 `Halmos1970` match; 27 `Henkin1949` match; 28 `Henkin1950` match; 29 `HilbertBernays1939` match; 30 `Hodges1993` match; 31 `Isabelle2025` D2; 32 `ISO80000` match.
  - 33 `Jech2003` match; 34 `Kleene1952` match; 35 `KnuthLarrabeeRoberts1989` match; 36 `Kripke1963` match; 37 `Kripke1965` match; 38 `LeanManual2026` D3; 39 `LeanTPIL` D4; 40 `Lindstrom1969` match.
  - 41 `Lob1955` match; 42 `Los1955` match; 43 `Manzano1996` match; 44 `Marker2002` match; 45 `Marker2024` match; 46 `NegriVonPlato2001` match; 47 `OpenLogic2026` match; 48 `Prawitz1965` match.
  - 49 `Robinson1965` match; 50 `RocqManual2026` D5; 51 `RobinsonVoronkov2001` match; 52 `Rosser1936` match; 53 `RoutleyMeyer1972` match; 54 `Shapiro1991` match; 55 `Shoenfield1967` match; 56 `SMTLIB2025` match.
  - 57 `Tarski1983` match; 58 `TPTP` D6; 59 `Trakhtenbrot1950` match; 60 `TroelstraSchwichtenberg2000` match; 61 `TroelstraVanDalen1988` match; 62 `Tseitin1968` match; 63 `Turing1937` match; 64 `Unicode2025` D7.
- required disposition: Correct D1-D7, regenerate the ledger, and record each of the 64 semantic decisions individually. F9 cannot close while the control itself still says all 64 are pending.

### F10 — needs-evidence

- current location: `handbook/parts/p05/decidable-arithmetics.tex:42-65`; `handbook/bib/handbook.bib:961-968`
- evidence: The specific wrong-work defect is repaired: both uses now name `Skolem1930Arithmetic`, and that record is *Uber einige Satzfunktionen in der Arithmetik* (1930), not the unrelated 1934 noncharacterizability paper.
- remaining evidence need: line 61 uses `cited=Skolem1930Arithmetic`, which means the cited item carries the theorem at the handbook's claimed status. This round verified bibliographic identity, not the completeness/validity of the decision proof in that historical paper. Pin a source inspection or an exact later complete-proof source before closing the status-bearing theorem.

### F11 — accept-fixed

- current location: `handbook/parts/p05/independence-catalog.tex:78-99`; `handbook/bib/handbook.bib:3943-3952`
- evidence changing the position: Both affected claims now cite `Feferman1960`, whose record is *Arithmetization of Metamathematics in a General Setting*, Fundamenta Mathematicae 49 (1960), 35-92, DOI 10.4064/fm-49-1-35-92. `Feferman1964` remains separately identified as *Systems of Predicative Analysis* and is no longer used for these claims.

### F12 — accept-fixed

- current location: `handbook/parts/p10/algebraic-and-categorical-logic.tex:39-60`; `handbook/bib/handbook.bib:2517-2536`
- evidence changing the position: Equational completeness now uses `cited=Birkhoff1935` at line 52 and retains the modern Burris-Sankappanavar pointer at line 60. `Birkhoff1944` remains a distinct bibliography record for *Subdirect Unions in Universal Algebra* and is no longer assigned the completeness theorem.

### F13 — still-open

- current location: `handbook/parts/p13/chronology-and-biography.tex:94-311`; `handbook/bib/handbook.bib:334-354,1582-1591,3083-3092`
- evidence: Grouped source notices are a material improvement, but two groups still fail exact claim/source correspondence. Lines 203-206 cite only `Kripke1963` for the Kripke capsule at 228-231, although that capsule also attributes intuitionistic semantics and fixed-point truth; the live bibliography has the directly relevant `Kripke1965` and `Kripke1975`, but the group does not cite them. Lines 274-277 say the remaining citations correspond “respectively” and assign `Scott1965` to the Dana Scott capsule at 303-306; `Scott1965` is *Logic with Denumerably Long Formulas and Finite Strings of Quantifiers*, not a source for the capsule's domain-theory and denotational-semantics claims.
- required disposition: Add `Kripke1965,Kripke1975` to the mid-century group and replace/supplement `Scott1965` with an exact domain-theory/denotational-semantics authority. Then recheck each grouped citation against every claim in its stated capsule range.

### F14 — accept-fixed

- current location: `handbook/parts/p14/master-tables.tex:23-43,63-77,97-118`
- evidence changing the position: Every decision-problem row now carries an exact citation or cited destination; every strength row now carries a source; every expressive-power row carries a source; and the modal correspondence table has an explicit two-source governing sentence at lines 117-118. The original absence of the promised destinations is removed.

### F15 — accept-fixed

- current location: `handbook/parts/p14/master-tables.tex:217-231,241-242`; `handbook/generated/named-theorem-index.tex:1-336`; `tools/build_named_theorem_index.py:1-136`
- evidence changing the position: The selected eighteen-row table has been replaced by a generated four-column index. `python tools/build_named_theorem_index.py --check` reports `335 live theorem/lemma rows`, and the generated file has one header plus 335 entries. The generator traverses the reader route from `main.tex`, indexes live editorial `hbtheorem`/`hblemma` entries and labelled restored theorem/lemma environments, rejects duplicate live labels, and supplies statement plus citation/annex/source-proof detail.

### F16 — needs-evidence

- current location: `handbook/parts/p14/master-tables.tex:233-245`; `handbook/parts/p01/symbol-registry.tex:22-32`; `handbook/generated/symbols-tables.tex:6-17`
- evidence: The source defects are repaired: Part XIV now points to `sec:p01-symbol-registry`, no longer calls the capsule order alphabetical, and the generated symbol table now contains `Reg. page` and `Principal uses / notes` columns.
- remaining evidence need: lines 239-240 newly assert that surname-sorted person entries in the final unified index point to the capsule section. That is a generated/rendered-index claim; close F16 only after inspecting the built index for complete capsule-name coverage, accent-aware surname order, and working page destinations.

### F17 — needs-evidence

- current location: `handbook/parts/p14/rule-sheets.tex:4-100`; affected files under `handbook/registry/calculi/`
- position: The opening defect requires each rendered sheet to carry its exact controlling citation and each inherited dependency to be human-readable and linked. The round was frozen after the bibliography evidence check before a complete post-fix, sheet-by-sheet rendering/source pass could be recorded. Do not close F17 from citation-key presence or comments alone; the required evidence is a current table covering every affected sheet, its reader-facing citation, and every linked base-sheet dependency.

### F18 — needs-evidence

- current location: `spec/provenance/PRE-00049-00055.json:23-42,87-90`; `source/formal-logic-reference.tex:49-55`; `handbook/handbook.sty:148-193`
- position: The acceptable fix is documentary classification as an authorized non-identical one-book layout adaptation, not a claim of exact reconstruction. The round was frozen before the amended `reason` and disposition were compared line-for-line with the still-different source and integrated page styles. Retain F18 pending that exact record check; byte identity of the retained interval is not evidence that the rendered furniture matches.

### F19 — accept-fixed

- current location: `handbook/main.tex:10,58-61`; `handbook/bib/handbook.bib:8-597`
- evidence changing the position: The single backmatter Bibliography now prints two reader-facing sections: one filtered by `category=inheritedsource` and one by `notcategory=inheritedsource`, under an explicit bibliography-section heading. This preserves one book and one Bibliography chapter while making the 64 inherited records visibly distinct from editorial additions, which is the correction F19 required.

## Round-2 disposition summary

- accept-fixed: F11, F12, F14, F15, F19.
- still-open: F9, F13.
- needs-evidence: F10, F16, F17, F18.
- no manuscript, bibliography, provenance, control, or generated artifact was edited by this seat; only this verbatim deliberation record was added.
