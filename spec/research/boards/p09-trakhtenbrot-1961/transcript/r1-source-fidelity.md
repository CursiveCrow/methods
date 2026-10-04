# REJECT

## Round 1 source-fidelity, language, and evidence review

- **Seat:** source fidelity, language, and evidence.
- **Round:** 1.
- **Artifact:** frozen Trakhtenbrot 1961/1962 snapshot for `N-c-014.c`.
- **Independence:** I read the charter, the seven frozen artifacts, the two
  primary scans, the two noncontrolling text extractions, and the official
  Math-Net identity and terms pages.  I did not read the board ledger, chair
  verdict, another current transcript, or another reviewer's conclusions.  I
  made no change to a frozen artifact.
- **Boundary observed:** no test, test harness, automated checker, repository
  script, TeX command, handbook build, rendered-handbook inspection, or
  handbook-PDF inspection was used.  SHA-256 recomputation and direct visual
  inspection of the two source scans were used because the charter expressly
  requires them.

## Source-language competence and evidence boundary

I can independently read technical Russian at the functional level required
to parse these definitions, theorem statements, proof transitions,
bibliographic notes, and historical qualifications.  I directly read the
Russian text on every source page and checked formulae and letterforms against
the scans.  I am not a native speaker or a credentialed human
Russian-language specialist, and this report is not a certification of a
complete literary translation.  The two scans control Russian wording,
symbols, pagination, and formulae; OCR was used only as a navigation aid.
Official English title renderings, journal metadata, access routes, and receipt
dates were checked against Math-Net rather than inferred by translation.

That evidence is sufficient for the source-fidelity determinations below.
None of the four rejecting findings depends on idiom or a disputed translation:
one is a directly visible Cyrillic/Latin letter distinction, one is a printed
page locator, one is the source's displayed definition of periodicity, and one
is an explicit repository-rights statement.

## Frozen identity check

I independently recomputed all seven required SHA-256 identities.  Every value
matches the charter.

| Frozen artifact | Recomputed SHA-256 |
|---|---|
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961.pdf` | `44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9` |
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded.pdf` | `EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D` |
| `handbook/parts/p09/presentations/n-c-014.tex` | `6D780FB5E14B34DB56C1B65A1040C4A194C57B5FDD012B7CD0BABD66341CB2D1` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD` |
| `handbook/bib/handbook.bib` | `75AB70009DF4AB8B2180CFFC6987EA244ADB2F978B1D889C87009EFF17066D5C` |
| `spec/research/p09-trakhtenbrot-1961-source-note.md` | `3028B89EE4B8CE8104416E57096B9015291E766BFA4660E1A85B85F3913C3B4C` |
| `spec/research/p09-source-presentations-lot2-3.md` | `E34436FBDAF4CA90A8A93A02AA305E65F5F7197027A545E6B5DEC94FAB9B4631` |

The two reading aids also match their declared identities:

- announcement extraction, 23,018 bytes:
  `18584E21CF79D98F863C6192DDBADF752D15FBD287A7E40BD4A4496F00665F4D`;
- expansion extraction, 160,210 bytes:
  `611661C9DB24DD9438F2DE18736372D18700A29FA539D7B5C4D7AC5E4AFE558B`.

## Complete visual source inspection and page maps

I inspected all thirty-three source pages at original detail.

- **1961 announcement:** physical pages 1--4 are printed pp. 326--329,
  respectively.  Physical p. 1 begins with the journal/volume header, Russian
  title, author, presentation date, and printed p. 326; physical p. 4 ends with
  the receipt, references, correction to the earlier reference (2), and printed
  p. 329.  No page is missing, duplicated, or out of order.
- **1962 expansion:** physical page \(n\), for \(1\leq n\leq29\), is printed
  page \(102+n\).  Physical p. 1 is printed p. 103 with the journal header,
  Russian title, author, and introduction; physical p. 29 is printed p. 131
  with the end of Theorem 3, the receipt date, and references.  The run
  pp. 103--131 is continuous, with no missing, duplicated, or reordered page.

Math-Net independently confirms the identities and metadata used in the
frozen records: 1961, volume 140, issue 2, pp. 326--329, English rendering
“Finite automata and the logic of single-place predicates”; and 1962, volume 3,
issue 1, pp. 103--131, English rendering “Finite automata and the logic of
one-place predicates.”  The scans confirm the same Russian title.  The 1961
scan prints presentation by P. S. Novikov on 16 May 1961 and receipt on
29 April 1961; the 1962 scan prints receipt on 15 May 1961.  The local file
sizes, 566,358 and 1,884,181 bytes, also match the source note.

## Rejecting findings and complete must-fix list

### SF-R1-01 — must-fix — the 1961 operator letter is silently replaced by the 1962 letter

**Controlling source evidence.**  The 1961 announcement visibly prints the
Cyrillic capital letter **Л**: p. 327 contrasts a finite operator with a
`Л-оператор`; p. 328 uses `Л-оператор` in Theorem \(4'\), defines an
`общее Л-решение`, and states Theorem 5 with an `общее Л-решение`; p. 329
again refers to Church's `общее Л-решение`.  The 1962 expansion instead
prints the Latin capital **A**: p. 104 frames the recognition and synthesis
tasks for `A-операторы`; p. 111 defines an `A-оператор` as the finite,
zero-anticipation case; p. 120 defines an `общее A-решение`; and pp. 121--124
use that terminology in Theorems 3 and \(3'\).  The class described is the
same automaton-realizable zero-anticipation finite class, but the two printed
names are not the same source notation.

**Frozen-artifact conflict.**  Reader lines 563--566 call the class simply
“the source's \(A\)-operators”; lines 633--668 summarize announcement
Theorems \(4'\) and 5 using \(A\)-operator/general \(A\)-solution language
without disclosing the announcement's **Л** notation.  Source-note lines
78--85 say without version restriction that “the source prints the Latin
letter `A`”; lines 248--285 likewise narrate the announcement with the later
\(A\) terminology.  Compact-record lines 652--654 transfer the same
terminology to announcement Theorem 5.

**Why this rejects.**  This is a directly checkable version boundary, not a
mere transliteration preference.  The frozen presentation expressly promises
not to transfer source notation silently between the 1961 announcement and the
1962 expansion.  It currently does so at the central operator/general-solution
name.

**Smallest exact correction.**  State at first operator use that the 1961
announcement calls the automaton-realizable class **Л-operators** and its
parametrizing object a **general Л-solution**, whereas the 1962 expansion uses
Latin **A-operator/general A-solution** for the same class.  Thereafter either
preserve the name belonging to each cited theorem or declare explicitly that
the reader adopts the 1962 \(A\) name as normalized terminology when restating
the 1961 results.  Scope source-note line 78 to the expansion and make the same
boundary explicit in the compact record.

### SF-R1-02 — must-fix — announcement Theorem 1 is cited to p. 326, but is printed on p. 327

**Controlling source evidence.**  Announcement p. 326 introduces lower and
upper \(t\)-formula terminology and ends during the definition of finite
operators.  Theorem 1 begins on printed p. 327 under “3°. Normal form.”

**Frozen-artifact conflict.**  Reader lines 517--523 expressly identify
announcement Theorem 1 and its effective normal-form conclusion, but line 524
cites only announcement p. 326.  Compact-record line 650 likewise attaches
the announcement normal-form claim to “announcement p. 326.”  Expanded
pp. 103--109 are correctly broad, but they do not repair the wrong locator in
the distinct announcement.

**Smallest exact correction.**  Split the authority precisely: p. 326 for the
lower/upper terminology and p. 327 for announcement Theorem 1, or cite
pp. 326--327 for the paragraph.  Correct the compact locator in the same way;
adding p. 327 to source-note lines 120--128 would keep all three records exact.

### SF-R1-03 — must-fix — “periodic” is used without the source's finite-preperiod semantics

**Controlling source evidence.**  Expanded p. 111 defines the paper's
`периодическая` function by the existence of a preperiod \(\alpha\) and a
period \(\beta\), with
\(f(\alpha+t)=f(\alpha+\beta+t)\) thereafter.  In current English terminology
this is **ultimately/eventually periodic**, not necessarily periodic from the
first position.  That definition controls the primitive-recursive negative
argument on p. 112 and the singleton-homogeneity example on p. 115 (with the
definability corollary on p. 118).

**Frozen-artifact conflict.**  Reader lines 568--571 say “periodic output” and
lines 589--590 say a singleton is homogeneous exactly when its stream is
“periodic,” without defining the source-specific wider use.  Source-note lines
154--162 and 182--189 repeat the same unqualified English term.  Elsewhere in
the same reader file, “ultimately periodic” is already used as the distinct
modern term, so a graduate reader can reasonably read these Trakhtenbrot
sentences too narrowly.

**Smallest exact correction.**  At the first Trakhtenbrot occurrence define
the source's use as “ultimately periodic (called periodic in the source, with a
finite preperiod),” then use `ultimately periodic` in the negative-boundary and
singleton statements.  Apply the same definition or wording in the source
note.

### SF-R1-04 — must-fix — the frozen provenance records omit the required rights qualification

**Controlling authority.**  This point is governed by the access repository,
not by a printed article page.  Math-Net's official Terms of Use page
<https://www.mathnet.ru/php/agreement.phtml?option_lang=eng> states that the
materials are copyrighted/all rights reserved, that reproduction or
republication requires permission, and that individual researchers may make
noncommercial research/teaching copies.  Anonymous public PDF access is
therefore not an open-content licence.

**Frozen-artifact conflict.**  Source-note lines 20--69 record identity,
custody, routes, hashes, and inspection, but no rights or redistribution
boundary.  Compact-record line 648 records the two access copies and the
unacquired AMS translation, again without that boundary.  No other
Trakhtenbrot-specific frozen reader or record line supplies it.  This leaves
charter invariant I27 and mandatory points M03/M28 unfulfilled.

**Smallest exact correction.**  Add one source-note and compact-record sentence
stating that Math-Net's public access supports scholarly inspection, that its
terms permit individual noncommercial research/teaching printing but do not
confer an open-content or republication licence, and that the local PDFs are
research objects not authorized for redistribution.  The reader's independent
prose remains unaffected.

There are **no additional blocker or must-fix findings** in this seat's
mandate.  I found no source support for weakening any of these four findings.

## Checked-clean source-to-reader trace

Subject to the four findings above, the substantive reconstruction is unusually
careful and tracks the Russian sources at the claimed strength.

| Surface checked | Controlling source locator | Frozen reader/record locator | Result |
|---|---|---|---|
| Two publication identities, same Russian title, distinct official English renderings, journals, years, volume/issue, pagination, receipt/presentation data, and unacquired-translation boundary | announcement pp. 326, 329; expansion pp. 103, 131; official Math-Net records | reader 487--497; source note 20--69; compact 646--648; bibliography 5991--6013 | Checked clean except SF-R1-04 rights omission. |
| Standing and interpretation of И/\(\mathcal I\), individual and predicate domains, primitive successor, and eliminable equality/order/bounded quantifiers/constants/offsets | expansion pp. 104--105 | reader 499--510; source note 71--118; compact 650 | Checked clean.  The typographic \(\mathcal I\) normalization is explicit and eliminable. |
| Semantic fictitious occurrence, lower/upper dependence, and normal-form transformation/proof moves | announcement pp. 326--327; expansion pp. 105--109 | reader 512--525; source note 113--128; compact 650 | Mathematical and linguistic content checked clean; locator rejected only under SF-R1-02. |
| Operator map, anticipation, prefix preservation, finite memory with whole future suffixes, weight, finite-window equations, and zero-anticipation automaton class | expansion pp. 109--113; announcement pp. 326--327 | reader 527--571; source note 130--162; compact 652 | Checked clean except the 1961/1962 letter boundary SF-R1-01 and periodicity wording SF-R1-03.  The one-state future-dependence example and the primitive-recursive recognition/synthesis boundary are not collapsed. |
| Cantor representation, portions (including tuples), degree, basis, internal/external transition data, graph and singleton examples, and nondefinable homogeneous sets | expansion pp. 113--118; announcement pp. 327--328 | reader 573--611; source note 164--217; compact 652 | Checked clean except the singleton wording in SF-R1-03.  `closed` is correctly scoped to the Cantor product topology. |
| Effective definable-to-homogeneous direction and closed-homogeneous converse | expansion pp. 116--119; announcement pp. 327--328 | reader 594--620; source note 191--225; compact 652 | Checked clean.  The finite residual-formula family gives homogeneity/internal transition; the finite basis and covering recurrence define the closure, which equals the set under closedness.  Complement, finite union, and projection recover the stated full class; intersection is derivable. |
| Conditional \(\mathcal I\)-algorithm boundary and Putnam qualification | announcement pp. 326--329; expansion pp. 104, 118--119, 124 | reader 613--620, 656--670; source note 219--225, 269--285; compact 654 | Checked clean.  Internal transition is effective; external output/deletion requires nonemptiness decisions; the stated existential-predicate fragment is the source's unconditional case. |
| Continuous graph theorem, compact finite anticipation, finite memory, weight bound, and weaker noncontinuous theorem | announcement p. 328, Theorem 4; expansion pp. 119--120, Theorems 1--2 | reader 622--631; source note 227--246; compact 654 | Checked clean.  Continuity is not imported into expanded Theorem 2, and finite memory is not inflated to bounded anticipation. |
| Graph versus solution, announcement Theorem \(4'\), generality in both directions, parameter standing, Theorem 5/expanded Theorem 3, stable deletion, fixed-\(p\) Theorem \(3'\), and conditionality | announcement pp. 328--329; expansion pp. 119--124 | reader 633--670; source note 248--293; compact 654 | Semantic statements and proof architecture checked clean; terminology rejected only under SF-R1-01.  The finite-tuple packaging is disclosed and eliminable.  Fixed \(p\) is not widened to unbounded lookahead. |
| Explicit definition, finite-memory conclusion, semantic anticipation tests, residual/shift synthesis, and two-formula/two-table example | expansion pp. 124--127 | reader 672--685; source note 295--308; compact 656 | Checked clean. |
| Automaton-enumerable and automaton-decidable word sets, both directions of Theorem 2, prefix closure, proper extendibility, weak system \(\mathcal I'\), special beginnings, Theorem 3, and effective/non-effective distinction | expansion pp. 127--131 | reader 687--700; source note 310--325; compact 656 | Checked clean. |
| Modern finite-word theorem and nonconflation with Büchi, Elgot, Trakhtenbrot, or Thomas | expansion pp. 112--113, 127--131; announcement pp. 326--329 | reader 700--735; shared theorem 811--825; navigation 2341--2347; source note 327--352; compact 22, 656--658 | Checked clean.  The displayed regular/MSO sentence is explicitly modern and is not represented as a verbatim theorem in either Russian source. |

The announcement/expansion numbering was otherwise kept separate: announcement
Theorem 1 corresponds to expanded §1.4; announcement Theorems 2--3 to the
expanded §3 chain; announcement Theorem 4 to expanded §4 Theorem 1;
announcement Theorem 5 to expanded §4 Theorem 3; expanded §4 Theorem 2 and
Theorem \(3'\) retain their separate, later strengths.  No proof detail was
silently attributed to the four-page announcement.

The AGENTS terminology rule is satisfied by the new reader-facing names other
than the source-version notation defect already isolated in SF-R1-01.  Each
technical term needed by the reconstruction has stated standing, a definition,
a nonredundant distinction, and later use.  I found no invented automaton kind,
hidden continuity/closedness hypothesis, operator-class collapse, modern-theorem
laundering, or independent priority adjudication.

## Mandatory coverage disposition

The source-fidelity seat's mandatory points are disposed as follows.

| Point | Disposition |
|---|---|
| M01 | **Checked clean:** all seven hashes recomputed and matched. |
| M02 | **Checked clean:** all 4 + 29 pages read visually at original detail; page maps confirmed. |
| M03 | **Finding-linked:** identity, date, journal, pages, titles, routes, and order checked clean; rights qualification fails SF-R1-04. |
| M04 | **Checked clean:** competence and evidence limits disclosed above. |
| M05 | **Checked clean:** \(\mathcal I\), \(\mathcal I'\), domains, successor, and eliminable extensions verified. |
| M06 | **Finding-linked:** semantics and proof moves checked clean; announcement Theorem 1 locator fails SF-R1-02. |
| M07 | **Finding-linked:** all operator distinctions and nonimplications checked clean; source-letter/version attribution fails SF-R1-01. |
| M08 | **Finding-linked:** one-state and primitive-recursive negative boundaries verified; the source's finite-preperiod meaning fails SF-R1-03 in English. |
| M09 | **Finding-linked:** portions, tuple extension, degree, basis, transitions, graph/singleton examples, and uncountability argument verified; singleton wording fails SF-R1-03. |
| M10 | **Checked clean:** finite normal-form residuals establish homogeneity and effective internal transition. |
| M11 | **Checked clean:** basis-cover construction, closedness, recurrence, and closure characterization verified. |
| M12 | **Checked clean:** unconditional internal construction, conditional nonemptiness/output step, and Putnam scope separated. |
| M19 | **Checked clean:** explicit semantics, residual synthesis, termination, equations, and pp. 126--127 example verified. |
| M20 | **Checked clean:** both word-set definitions and both Theorem 2 directions, including both converse hypotheses, verified. |
| M21 | **Checked clean:** \(\mathcal I'\), special beginnings, Theorem 3, Büchi attribution, and effectiveness distinction verified. |
| M22 | **Finding-linked:** theorem-strength and numbering comparison otherwise clean; the 1961/1962 operator-letter change fails SF-R1-01. |
| M23 | **Checked clean:** modern theorem and Thomas paragraph do not launder the modern sentence into either source. |
| M24 | **Finding-linked:** reader, source note, compact record, shared theorem, and bibliography agree except SF-R1-01 through SF-R1-04. |
| M25 | **Finding-linked:** formulae, titles, dates, and historical attributions checked clean; notation, locator, and periodicity failures are SF-R1-01 through SF-R1-03. |
| M26 | **Checked clean:** no additional AGENTS terminology defect found. |
| M27 | **Finding-linked:** no hidden continuity, closedness, finite-memory, translation, or priority inflation found beyond SF-R1-01 and SF-R1-03. |
| M28 | **Finding-linked:** topic and no-test/no-build boundaries were respected; the frozen rights record fails SF-R1-04. |

For M13--M18, which are assigned principally to the mathematical/proof seat, I
checked the printed source statements and their reader attribution while
performing M22--M25.  I do not substitute this source-fidelity report for that
seat's independent derivations.

## Verdict

The substantive mathematics is source-aligned, but the frozen snapshot cannot
receive source-fidelity acceptance while four mandatory, exact, and readily
repairable source/provenance defects remain.

VERDICT: REJECT — SF-R1-01, SF-R1-02, SF-R1-03, SF-R1-04
