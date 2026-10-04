# Round 3 source-fidelity focused verification

### F9 — accept-fixed

- current locations: `spec/provenance/inherited-bibliography-field-ledger.csv:1-65`; `handbook/bib/handbook.bib:8-591`; `spec/provenance/SRC-16803-17196.json:36-71`
- evidence changing the position: I compared every current `source_literal_json` value with its current `bib_fields_json` value, treating author/editor standing, title and container standing, edition/version, publication versus access date, and locator standing as distinct roles. All 64 mappings preserve the roles asserted by the retained manual entries. The seven round-2 discrepancies are repaired at `handbook/bib/handbook.bib:16-20,294-298,355-369,461-466,531-537,587-591`: `AMSMathGuide` now has two institutional authors, and `Isabelle2025`, `LeanManual2026`, `LeanTPIL`, `RocqManual2026`, `TPTP`, and `Unicode2025` no longer manufacture publication years from release names, access dates, keys, or current context.
- control boundary: all 64 generated rows still contain `semantic_field_review=pending`, while `SRC-16803-17196.json:63-70` still says attribution and independent-source review are pending. The 64 individual decisions below are the independent semantic-review evidence produced by this read-only seat; those control fields should be synchronized from the board disposition rather than treated as evidence that the role comparison failed.

### F10 — still-open

- current locations: `handbook/parts/p05/decidable-arithmetics.tex:42-65`; `handbook/bib/handbook.bib:955-962,3053-3062,3298-3306`
- accepted portion: the wrong-work defect is repaired. The historical sentence now cites `Skolem1930Arithmetic`, and the status-bearing theorem now cites the later Ferrante--Rackoff treatment. Springer's record identifies the cited book and its chapter “Direct products of theories,” pp. 128--147: <https://link.springer.com/chapter/10.1007/BFb0062842>.
- remaining defect: `decidable-arithmetics.tex:63-65` says the known procedures have “nonelementary” worst-case behaviour and that no elementary bound is implied. Rackoff's primary JSL abstract expressly says the weak-direct-power method gives elementary-recursive decision procedures and that the same upper bound applies to the positive integers under multiplication: <https://doi.org/10.2307/2272034>. The adjacent `Oppen1978` record is, by its title at `handbook.bib:3053-3062`, about Presburger arithmetic, not a source that repairs this Skolem-complexity sentence. Replace “nonelementary” by the exact verified fixed-height bound and attach its exact source before closing F10.

### F13 — still-open

- current locations: `handbook/parts/p13/chronology-and-biography.tex:94-311`; `handbook/bib/handbook.bib:211-219,252-272,5002-5010,5120-5130`
- accepted portion: the two round-2 mismatches are repaired. `chronology-and-biography.tex:203-206` now cites `Kripke1963`, `Kripke1965`, and `Kripke1975` for the three distinct Kripke contributions at lines 228-231, and lines 274-277 now use `Scott1972Domains` rather than the unrelated `Scott1965` for the Scott capsule at lines 303-306.
- remaining defects after rechecking the grouped notices against their capsule ranges:
  - `chronology-and-biography.tex:203-216` cites only `Henkin1949` for Henkin, although the capsule expressly extends the claim to type-theoretic completeness under general semantics. The live database already distinguishes the directly relevant `Henkin1950`, *Completeness in the Theory of Types*, at `handbook.bib:263-272`; the group omits it.
  - `chronology-and-biography.tex:242-267` supplies only `Girard1987` for Girard, while the capsule also attributes System F and proof-theoretic semantics. The cited record at `handbook.bib:211-219` is *Linear Logic* and does not identify a source for those additional attributions.
  - `chronology-and-biography.tex:274-311` assigns `Quine1948` to the Quine capsule, but that single source pin does not identify support for the capsule's separate set-theory, logical-syntax, and translation attributions. Supply exact sources or narrow those claims.
- required disposition: finish claim/source correspondence for every claim in each grouped capsule range; adding one source per person is insufficient when the capsule bundles historically distinct contributions.

### F18 — needs-build/visual

- current locations: `spec/provenance/PRE-00049-00055.json:23-42,65-90`; `source/formal-logic-reference.tex:49-55`; `handbook/handbook.sty:148-193`
- source-fidelity position: the documentary defect is fixed. `PRE-00049-00055.json:40-42` now says exactly that the integrated one-book design intentionally replaces the source's fixed “Formal Logic” right head and centered footer folio with alternating chapter/section heads and header folios, calls this a layout-only adaptation rather than presentation identity, and leaves the disposition `open/missing`. That classification matches the still-different source and integrated declarations line for line.
- remaining gate: `PRE-00049-00055.json:69-70,89-90` correctly leaves build and visual review pending. Static source comparison cannot establish that the alternating marks, conditional scaling, folio gaps, legibility, or navigation render acceptably. No further source-classification correction is open, but final acceptance requires the build and visual checks named by the record.

## F9 row-by-row semantic decisions

BIBSEM AMSAuthorHandbook pass
BIBSEM AMSMathGuide pass
BIBSEM Avigad2018 pass
BIBSEM BaazEglyLeitsch2001 pass
BIBSEM BachmairGanzinger2001 pass
BIBSEM Barwise1977 pass
BIBSEM BarwiseFeferman1985 pass
BIBSEM BlackburnDeRijkeVenema2001 pass
BIBSEM BoolosBurgessJeffrey2007 pass
BIBSEM Buss1998 pass
BIBSEM ChangKeisler1990 pass
BIBSEM ChiswellHodges2007 pass
BIBSEM Church1936 pass
BIBSEM Cook1971 pass
BIBSEM DavisLogemannLoveland1962 pass
BIBSEM DavisPutnam1960 pass
BIBSEM DeMouraUllrich2021 pass
BIBSEM EbbinghausFlumThomas1994 pass
BIBSEM Enderton2001 pass
BIBSEM GabbayPnueliShelahStavi1980 pass
BIBSEM Gentzen1934a pass
BIBSEM Gentzen1935b pass
BIBSEM Girard1987 pass
BIBSEM Godel1930 pass
BIBSEM Godel1931 pass
BIBSEM Halmos1970 pass
BIBSEM Henkin1949 pass
BIBSEM Henkin1950 pass
BIBSEM HilbertBernays1939 pass
BIBSEM Hodges1993 pass
BIBSEM Isabelle2025 pass
BIBSEM ISO80000 pass
BIBSEM Jech2003 pass
BIBSEM Kleene1952 pass
BIBSEM KnuthLarrabeeRoberts1989 pass
BIBSEM Kripke1963 pass
BIBSEM Kripke1965 pass
BIBSEM LeanManual2026 pass
BIBSEM LeanTPIL pass
BIBSEM Lindstrom1969 pass
BIBSEM Lob1955 pass
BIBSEM Los1955 pass
BIBSEM Manzano1996 pass
BIBSEM Marker2002 pass
BIBSEM Marker2024 pass
BIBSEM NegriVonPlato2001 pass
BIBSEM OpenLogic2026 pass
BIBSEM Prawitz1965 pass
BIBSEM Robinson1965 pass
BIBSEM RocqManual2026 pass
BIBSEM RobinsonVoronkov2001 pass
BIBSEM Rosser1936 pass
BIBSEM RoutleyMeyer1972 pass
BIBSEM Shapiro1991 pass
BIBSEM Shoenfield1967 pass
BIBSEM SMTLIB2025 pass
BIBSEM Tarski1983 pass
BIBSEM TPTP pass
BIBSEM Trakhtenbrot1950 pass
BIBSEM TroelstraSchwichtenberg2000 pass
BIBSEM TroelstraVanDalen1988 pass
BIBSEM Tseitin1968 pass
BIBSEM Turing1937 pass
BIBSEM Unicode2025 pass
