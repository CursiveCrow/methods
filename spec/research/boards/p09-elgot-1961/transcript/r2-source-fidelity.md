# Elgot 1961 N-c-014.b Round 2 source-fidelity report

Seat: source fidelity and evidence.

Scope observed: I read the updated charter, the frozen Round 2 artifacts, and the authorized source renders for journal p. 46, report pp. 4 and 41, and errata pp. 558--559. I did not read the ledger, chair transcript, another seat transcript, any Büchi board material, or any other current Round 2 report. I did not edit frozen artifacts. I ran no test, checker, repository script, TeX command, build, or handbook-PDF inspection.

## Frozen identity check

All eight Round 2 frozen identities recomputed cleanly before substantive review.

| Frozen object | Expected SHA-256 | Recomputed result |
| --- | --- | --- |
| `tmp/pdfs/p09-elgot-1961/elgot-1961-trans-ams.pdf` | `DE2F9587F72075C94C7071A00002D1129AA8148C498F9A4D6F75968EB46ACD74` | match |
| `tmp/pdfs/p09-elgot-1961/elgot-1959-umr1342.pdf` | `596A599A7DF12F122BB2D875255B050695EC84A5A22F3488844D5876F3211D74` | match |
| `tmp/pdfs/p09-elgot-1961/elgot-1962-errata.pdf` | `B13E422FC03DDA61B93A1B782F40882AE90DBC8886945B26A42376A96ED34EC1` | match |
| `handbook/parts/p09/presentations/n-c-014.tex` | `33A2CD747DBDFA356F5505E88CBF798D426C5B5971003E0449805BCDF93F86FA` | match |
| `handbook/parts/p09/logic-in-computer-science.tex` | `1690DED84FC257B50BC5B44E094E382D8A79B176E7BB9C21D0845DAEC59629B8` | match |
| `handbook/bib/handbook.bib` | `6F98B6EB38B2B935DACC0C7E8373E1B12A5BB70FCAAC172D11BAFCDACA8C502F` | match |
| `spec/research/p09-elgot-1961-source-note.md` | `1A34AC4E992C00A0E917256CF5DB58A7C48A971FBF47F7F217B25D0DDAF18331` | match |
| `spec/research/p09-source-presentations-lot2-3.md` | `34D4B1AC65B78EAD14AB60335C94C8FFEA2F00778B963956038485DFB50EC438` | match |

## Source-page reinspection

I visually reinspected the required pages at original detail.

- Journal p. 46 (`rendered/page-26.jpg`) controls the corrected article §8.6.2. It states the restricted formula form, the quantifier-free condition on `M`, the displayed free variables, numerals allowed, equality and order excluded, and successor-offset terms. It also contains the published false singular one-relation assertion and the printed `n` wording corrected by the 1962 errata.
- Report p. 4 (`report-rendered/page-09.jpg`) controls the projection-symbol comparison. Both corresponding occurrences already print `\widehat p`, not `\widehat f`.
- Report p. 41 (`report-rendered/page-46.jpg`) shares the same §8.6.2 defect as the journal article, including the single-relation wording and the printed `n` as maximum rather than one more than maximum.
- Errata p. 558 (`elgot-1962-errata-page-1.jpg`) gives all six corrections: the two p. 23 projection-symbol corrections, the p. 23 line-break correction, the p. 24 ordered-pair correction, the p. 46 `n` correction, the grammatical `n`-ary wording correction, and the replacement of the false third sentence of §8.6.2 by the finite-union statement with `k` not necessarily one and a `k=2` example.
- Errata p. 559 (`elgot-1962-errata-page-2.jpg`) continues the repair by defining tagged disjoint fields, tagged prefix sets, relation union, the projection `p(<a,j>)=a`, and the equality `\widehat p(S)=S_1 \cup \cdots \cup S_k`. Its displayed relation notation is binary, while its stated assumption is arity at least two.

## Round 2 correction checks

### R2-C01: literal §8.6 syntax

Checked-clean.

The revised reader passage at `handbook/parts/p09/presentations/n-c-014.tex` lines 410--425 now states the controlling syntactic restrictions rather than replacing them by an undefined locality condition: `M` is quantifier-free; its only free variables are the displayed variables; numerals may occur; equality and order do not occur; and successor iterates `x^{(h)}` and `0^{(h)}` determine the window length with `n` one more than the relevant maximum. This matches journal p. 46 as corrected by errata p. 558. The source note lines 286--303 and 309--318 carry the same source attribution and do not promote the paraphrase to Elgot's uncorrected wording.

No blocker remains for R2-C01.

### R2-C02: general arity, projection equality, and the `n=1` case

Checked-clean.

The revised reader passage at lines 434--463 no longer gives only a binary-looking tag relation as though that exhausted the erratum. For `n >= 2`, it defines `R'_j` componentwise on tagged `n`-tuples, tags the words in `E_j`, takes the union of the tagged relations and prefix sets, and uses the projection `(a,j) \mapsto a`. This is the arity-explicit expansion of the errata pp. 558--559 repair: the errata says the `R'_j` are `r`-ary for `r >= 2`, defines disjoint tagged fields and tagged prefix sets, and concludes `\widehat p(S)=S_1 \cup \cdots \cup S_k`.

Independent projection check for `n >= 2`: each accepted length-`n` window in the tagged union has all entries with one tag. Consecutive windows overlap in `n-1` tagged entries, so the tag on every admitted infinite sequence is constant. Projection therefore sends a tagged sequence with tag `j` to a sequence in `S_j`. Conversely, every sequence in `S_j` lifts by tagging every entry with `j`; the tagged prefix condition and tagged relation condition are then immediate. Thus projection gives exactly the finite union, not a superset and not a single untagged relation.

The revised reader also handles `n=1` explicitly at lines 450--456 and labels that move as handbook-supplied, not as wording found in the erratum. Replacing a unary constraint `R_j` by the binary relation `R_j \times R_j` with the same one-letter prefix condition defines the same infinite sequences: if every term lies in `R_j`, then every adjacent pair lies in `R_j \times R_j`; conversely, if every adjacent pair lies in `R_j \times R_j`, the first coordinate of the first pair gives the initial term in `R_j` and the second coordinate of each adjacent pair gives every later term in `R_j`. After this promotion, the same tagged-binary overlap argument forces a constant tag and the projection equality remains exact. The source note lines 320--356 agrees and preserves the correction-ownership boundary.

No blocker remains for R2-C02.

### R2-C03: report projection-symbol attribution

Checked-clean.

The revised report comparison at `handbook/parts/p09/presentations/n-c-014.tex` line 480 now says the report already prints the correct `\widehat p` at both corresponding occurrences. Report p. 4 confirms both occurrences: the induced mapping on sequence-sets is printed as `\widehat p`, and the subsequent projection statement also prints `\widehat p`. This agrees with errata p. 558, where the two corresponding article occurrences on p. 23 are corrected from `\widehat f` to `\widehat p`. The reader no longer implies that only one report occurrence was already correct.

No blocker remains for R2-C03.

## Collateral source-fidelity and terminology inspection

The revised reader passage, source note, compact record, shared theorem, and bibliography remain mutually consistent on the Round 2 points:

- The bibliography keeps the controlling 1961 article, 1959 report, and 1962 errata identities and locators distinct.
- The source note attributes the finite-union and tagging correction to the errata, while explicitly identifying the unary-window treatment as a handbook completion.
- The compact record now reports the exact §8.6 syntax, componentwise general-arity tagged relation, unary-window handling, and the two report `\widehat p` occurrences.
- The shared theorem file is unchanged and does not absorb the disputed §8.6 correction.
- The AGENTS terminology rule is satisfied for the revised passage. The revision uses source terms or local metalinguistic descriptions whose standing is clear. The tag construction is defined where used; the unary-window completion is explained as an owed edge-case repair rather than smuggled in as Elgot's wording; no new named technical object is introduced without necessity, definition, standing, nonredundancy, and later use.

I found no collateral false compression, hidden hypothesis, correction laundering, misleading singular/plural, or completion inflation introduced by the revision.

## Assigned item ledger

- M01: checked-clean; all eight frozen hashes recomputed and matched before substantive review.
- M02: checked-clean for Round 2; I relied on my own complete Round 1 source pass as authorized and reinspected the required Round 2 pages at original detail.
- M03: checked-clean for Round 2 identities and authority order; the article, report, errata, bibliography, and source note remain distinct.
- M04--M07: checked-clean by authorized reliance on my own Round 1 source pass; no Round 2 revision touched these claims.
- M10--M11: checked-clean by authorized reliance on my own Round 1 source pass; no Round 2 revision touched these claims.
- M17: checked-clean; R2-C01 restores the literal §8.6 syntactic restrictions and successor-offset convention.
- M18: checked-clean; errata pp. 558--559 were read directly and the six corrections, `k=2` example, finite-union statement, tagged fields, tagged prefix sets, relation union, and projection equality are represented honestly.
- M19: checked-clean; corrected §8.6.2 plus the stated §8.5 route supports the reduction once the finite-union/tagged-projection repair and `n=1` completion are included.
- M20: checked-clean by authorized reliance on my own Round 1 source pass; no Round 2 revision touched the §10 material.
- M21: checked-clean; report pp. 4 and 41 confirm the report comparison, including both `\widehat p` occurrences and the shared §8.6.2 defect.
- M22: checked-clean for the authorized frozen records; the ledger component was not checked because the Round 2 charter expressly forbids reading the ledger.
- M23: checked-clean for the revised locators, theorem/section references, historical attribution, and source-versus-handbook correction ownership.
- M24: checked-clean; no definition-after-use, redundant name, standing ambiguity, or unused distinction appears in the Round 2 revision.
- M25: checked-clean; the revision does not leave a graduate-reader exposure on the three Round 1 source-fidelity defects.
- M26: checked-clean; topic-only scope, source authority, rights boundary, and no-test/no-build boundary were preserved.

## Findings

None.

VERDICT: ACCEPT
