# Round 2 adversarial publication and terminology audit

Seat: adversarial publication and terminology.  Snapshot: the seven frozen
Round 2 objects identified in the charter.  Scope: `N-c-014.c` at manuscript-
content level only.

## Disposition

The reconstruction is mathematically and historically careful, and the Round 2
snapshot closes the large hostile-reader risks: it separates the 1961
announcement from the 1962 expansion, declares both title and operator-letter
normalizations, exposes every continuity/closedness/effectivity hypothesis,
keeps finite memory distinct from bounded anticipation, limits the modern
finite-word sentence to a modern formulation, and does not inflate rights or
admission status.  One mandatory definition-before-use defect nevertheless
remains.  It is small to repair but blocking under I16, I26, and the repository
AGENTS terminology rule.

## Independence, competence, and evidence boundary

- I read the charter, the seven permitted frozen objects, the four announcement
  scans, and the twenty-nine expansion scans.  I did not read the ledger, chair
  transcript, any Round 1 report, or another Round 2 report, and I did not
  contact another reviewer.
- I have non-specialist working reading competence in mathematical Russian.  It
  is sufficient here to follow headings, definitions, theorem statements,
  proof order, formulae, operator letters, qualifications, receipts, and
  bibliographic matter, and to compare the bounded English reconstruction with
  the controlling pages.  I am not a Russian-language specialist and do not
  certify idiomatic translation, fine stylistic nuance, or historical priority.
  The snapshot expressly makes none of those stronger claims.  Specialist-level
  line-by-line translation certification is therefore not checked and is not a
  represented deliverable.
- Formulae, symbols, pagination, Cyrillic/Latin letter identity, and source
  wording were checked from the rendered scan pages at original detail.  OCR
  was treated only as a navigation aid and never as controlling evidence.
- I also inspected the live official Math-Net records for both papers and its
  Terms of Use.  They confirm the two official English renderings, journal
  identities, dates, volume/issue/page data, receipt dates, Russian-language
  status, public full-text routes, copyright reservation, permission to print
  individual noncommercial teaching/research copies, prohibition on systematic
  downloading, and the requirement of permission for reproduction or
  republication.  The AMS volume route confirms the later volume-59 (1966)
  English item; its body was not used as evidence.
- I ran no test, automated checker, repository script, TeX command, build, or
  handbook-PDF inspection.  SHA-256 was used only to identify the frozen
  objects, as the charter permits.

## Frozen identity labels

All seven recomputed labels matched the charter before substantive review.

| Frozen object | Recomputed SHA-256 |
|---|---|
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961.pdf` | `44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9` |
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded.pdf` | `EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D` |
| `handbook/parts/p09/presentations/n-c-014.tex` | `109A631EBAFAC28A7C84A946FE4E305E91BA1818B7E4E9F08FCF4E15E4B95B72` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD` |
| `handbook/bib/handbook.bib` | `75AB70009DF4AB8B2180CFFC6987EA244ADB2F978B1D889C87009EFF17066D5C` |
| `spec/research/p09-trakhtenbrot-1961-source-note.md` | `6D84E96A50414E10FE229536D3E8A4557BEB45D2D0024DF182E6AD75D3DD41DC` |
| `spec/research/p09-source-presentations-lot2-3.md` | `DFFF60FBB6E0C715A9B41D7000D670B374B0B62A86305AC2BAF92CA46726A687` |

The PDF byte sizes also match the custody record: 566,358 bytes for the
announcement and 1,884,181 bytes for the expansion.  These are identity and
custody observations only, not content validation.

## Complete visual source inspection

The physical-to-printed maps are continuous and complete.

| Physical pages | Printed pages | Material visually checked |
|---|---|---|
| Announcement 1--4 | 326--329 | title and presentation line; system/normal-form summary; Theorems 1--5 and (4'); the source definition of solution before (4'); Cyrillic Л terminology and both generality clauses; conditionality; receipt, references, and the correction concerning the earlier item |
| Expansion 1--7 | 103--109 | title/header, introduction, system И, full syntax and eliminable extensions, semantic fictitious occurrence, lower/upper (t)-formulae, and the normal-form construction |
| Expansion 8--10 | 110--112 | operator map, anticipation and prefix behavior, finite-memory equations with whole future suffixes, weight, finite-operator equations, Latin (A), the one-state nonrecursive example, periodicity, and the recognition/synthesis negative boundary |
| Expansion 11--16 | 113--118 | Cantor-space portions, coordinatewise extension, homogeneous degree, basis, internal/external transition data, examples, covering construction, definability, recurrence formula, closure characterization, and topological qualifications |
| Expansion 17--22 | 119--124 | conditional И-algorithm boundary, Putnam qualification, graph-versus-solution definition, continuous and noncontinuous operator theorems, general (A)- and zero-anticipation solutions, stable deletion, Theorem 3, fixed-(p) Theorem (3'), and all weight/closedness clauses |
| Expansion 23--29 | 125--131 | explicit definitions, anticipation criteria, synthesis procedures, the two-formula/two-table example, word enumeration and decision, both directions of the word theorem, И', special beginnings, Theorem 3, Büchi attribution, receipt, and references |

The first announcement page is printed p. 326 and the fourth p. 329.  The first
expansion page begins the article on printed p. 103, the second is p. 104, and
the twenty-ninth is p. 131.  No page is duplicated or absent.

## Blocking finding

### AP-R2-01 — must-fix — the source-specific solution vocabulary is named and used before definition

- **Manuscript location:**
  `handbook/parts/p09/presentations/n-c-014.tex:563-566,642,654-679`.
  Lines 565--566 first name “general Л-solution” and “general (A)-solution”;
  the paragraph title at line 642 again names general solutions; and lines
  654--660 use “continuous operator solution,” “finite solution,”
  “zero-anticipation solution,” and the open-relation “solution.”  Only lines
  661--663 state that (T) solves (arphi(X,Y)) when
  (arphi(X,T(X))) holds for every input, a claim strictly weaker than saying
  that (arphi) defines exactly the graph of (T); only lines 665--679 give
  the two-quantifier definition of a general solution.
- **Controlling printed source:** announcement p. 328 defines “solution” before
  stating Theorem (4'), then defines the general Л-solution before Theorem 5;
  expansion p. 119 opens §4 by distinguishing graph containment
  (satisfaction/solution) from exact graph definition before any of the §4
  theorems, and p. 120 defines the general (A)-solution before Theorem 3.  The
  frozen source note preserves both definitions and their order at lines
  261--263 and 288--302.
- **Violated requirements:** I16 and I26; M15, M26, and M27; the AGENTS
  definition-before-use, standing, and nonredundancy conditions.
- **Concrete reader harm:** “solution” and “general solution” are not harmless
  ordinary prose here.  The exact graph/contained-graph distinction changes
  the hypothesis and conclusion of Theorem (4'), while “general” means the
  all-and-only parameterization expressed by two separate quantifiers.  A
  hostile expert encounters both names first as unexplained labels, can read
  the later theorem uses with the stronger exact-graph standing established in
  the preceding paragraph, and only afterward learns that the source means the
  weaker containment relation and a precise bidirectional parameterization.
  This creates exactly the standing ambiguity the reconstruction otherwise
  works to prevent.
- **Smallest exact correction:** defer the sentence at lines 565--566 that names
  the general solutions (the version distinction is already stated with the
  definition at lines 668--669); shorten the line-642 paragraph title to
  “Finite realization”; and move the existing sentence at lines 661--663
  immediately before line 654, changing only its deictic opening if needed.
  The first remaining occurrence of “general (A)-solution” will then be its
  definition at lines 665--679.  No new term, proof, or abstraction is required.

No other blocker or must-fix was found.

## Independent hostile derivation checks

### Normal form, portions, and effective internal transition

The lower/upper normal form on announcement pp. 326--327 and expansion
pp. 103--109 leaves only finitely many prefix Boolean functions at a fixed
shift and finitely many residual upper formulae.  Prefix substitution therefore
produces finitely many residual sets.  Appending one input letter sends a
residual to another residual by syntactic substitution, so the internal
transition is effectively obtained without deciding whether a residual is
empty.  This supports `n-c-014.tex:512-525,583-607`.  It also explains why the
external output choice at `:633-640` is different: selecting an allowed output
requires a nonemptiness/truth decision.

### Closed-homogeneous converse and topology

For a finite portion basis, the internal transition follows the next portion
and a choice bit selects a permitted next output.  The induced covering
operator has as image the closure of the original homogeneous set.  Hence
closedness in the Cantor product topology is exactly what turns coverage into
equality.  The one-hot initial state selects the original portion, while the
bound state and choice predicates plus a local current/next matrix give the
displayed recurrent formula.  Conversely, a local finite-state constraint is
closed before projection, its quantified predicate space is compact, and its
projection is closed; only finitely many state residuals occur.  This verifies
both directions and the closure characterization in
`n-c-014.tex:583-631` against expansion pp. 113--119.  The manuscript does not
hide the topological hypothesis or infer definability from bare homogeneity.

### Continuous finite realization and the noncontinuous boundary

A continuous total operator on compact Cantor input has a uniform finite
lookahead for its next output on every nonempty graph portion.  There are only
finitely many portions, so the maximum is one global anticipation bound; the
portion index is finite memory and yields the advertised weight bound.  Without
continuity, the portion state can still use a whole future suffix, giving
finite memory but no bounded anticipation.  This confirms
`n-c-014.tex:642-652` against announcement p. 328 and expansion pp. 119--120.
The manuscript never promotes expanded §4, Theorem 2, to finite-operator
standing.

### Generality, deletion, and fixed lookahead

The two clauses at `n-c-014.tex:665-679` are respectively completeness (every
solution of the named class arises by parameter substitution) and soundness
(every allowed substitution is a solution).  Stable deletion removes empty
portions and predecessors lacking a permitted output for some input.  Deletion
of the initial portion yields the no-solution branch; survival supplies a
finite transition system in which parameter bits select surviving outputs.
Every selected finite prefix remains compatible, and closedness supplies the
limit pair in the relation.  The same parameter trace represents any original
zero-anticipation solution.  This verifies the weight bound, both generality
quantifiers, and conditional emptiness boundary at `:681-699` against
announcement pp. 328--329 and expansion pp. 120--124.  Shifting the first
(p) output places reduces each fixed-(p) class separately to the
zero-anticipation case; it does not produce one solution across unbounded
lookahead.

### Explicit synthesis and the word bridge

Semantic independence outside ([1,t+p]) is exactly anticipation at most
(p); the case ([1,t]) is zero anticipation.  Repeated first-column
substitution yields finitely many residual (t)-formulae and hence the output
and transition tables shown on pp. 126--127.  For words, zero anticipation
makes (T_t) independent of the infinite extension and prefix compatible.
An enumerator can be converted to a terminal recognizer by existentially
testing an input preimage.  Conversely, from a recognizer for a prefix-closed,
extendible language, the construction preserves an accepted prefix and chooses
a compatible longer accepted word, giving an enumerator.  The empty-word issue
is avoided because the source and manuscript expressly use positive lengths.
The И' special-beginning clause then requires an actually all-zero tail, not
an arbitrary finite prefix.  These checks support `n-c-014.tex:701-755`
against expansion pp. 124--131.

## Terminology-rule audit

The following first-use audit applies necessity, definition, standing,
nonredundancy, and later use rather than mere typographic presence.

| Term or distinction | First-use result |
|---|---|
| (mathcal I) | Clean at `n-c-014.tex:499-510`: the Cyrillic source name is normalized, its interpreted-language standing and domains are fixed, eliminable extensions are separated from primitives, and it is distinguished from Büchi's weak system before later use. |
| fictitious occurrence; lower/upper (t)-formula | Clean at `:512-525`: semantic independence is distinguished from written occurrence, prefix and tail standings differ, and the normal-form theorem immediately uses them. |
| operator; anticipation; prefix preservation | Clean at `:527-536`: a typed total stream map and the exact agreement condition are supplied before use. |
| finite memory; weight | Clean at `:538-554`: the finite state, fixed initial state, whole-suffix transition types, and least-cardinality meaning are explicit; the nonrecursive one-state example proves nonredundancy from anticipation. |
| finite operator; Л-operator; (A)-operator | Clean at `:556-572`: conjunction versus zero-anticipation specialization, 1961/1962 letter standing, normalization, alphabet-letter ambiguity, and later theorem use are all explicit. |
| periodic/ultimately periodic | Clean at `:574-581`: the source convention is eliminated into preperiod/period data and used in the negative boundary and singleton example. |
| portion; homogeneous degree; basis; internal transition | Clean at `:583-595`: all are defined as a stream-set residual, property, or finite data and expressly denied invented-automaton standing before theorem use. |
| closed | Clean at `:597`: the Cantor product topology is named before any closed-converse or closed-relation theorem. |
| conditional (mathcal I)-algorithm | Clean at `:633-640`: its metalinguistic procedural standing and truth-oracle condition are stated and later used to qualify deletion. |
| solution | **Finding-linked: AP-R2-01.** It occurs inside the unexplained general-solution label at `:565`, is used theoremically at `:655`, and is only defined at `:661-663`, despite its nonredundant weaker-than-graph meaning. |
| general (A)-solution; general zero-anticipation solution | **Finding-linked: AP-R2-01.** The two all-and-only quantifiers, parameter standing, and class replacement at `:665-679` are exact, but the source names at `:565-566` and the line-642 heading precede them. |
| explicit definition | Clean at `:701-709`: the defining equation, finite-memory standing, and anticipation criteria are supplied before synthesis. |
| (T_t); automaton-enumerable; automaton-decidable | Clean at `:716-744`: types, extension independence, terminal-output standing, and both theorem directions are supplied. |
| (mathcal I'); special beginning | Clean at `:746-755`: the eventually-zero quantifier domain and exact tail condition are stated before the existence/effectivity theorem. |

No redundant invented automaton kind, unused hypothetical distinction, or
unexplained new symbol was found.  In particular, “portion,” “basis,” and
“internal transition” remain data/properties of a stream set; (mathcal I)
remains an interpreted language; and (A) is explicitly insulated from the
input-alphabet metavariable.

## Source, translation, rights, and publication-fitness audit

- `n-c-014.tex:487-497`, the two bibliography entries at
  `handbook.bib:5991-6013`, source-note lines 5--104, and compact-record lines
  646--658 consistently distinguish the registered four-page 1961 announcement
  from the complete twenty-nine-page 1962 expansion.  The scans have the same
  Russian title; the current Math-Net records supply “single-place” for 1961
  and “one-place” for 1962.  No title, pagination, theorem number, or proof
  detail is silently moved under the other source's locator.
- The announcement visibly prints Cyrillic И and Л; the expansion visibly
  prints И and Latin (A).  `n-c-014.tex:499-510,563-570` states both
  normalizations and standings.  This is declared normalization, not
  transliteration laundering.
- The announcement's Theorems 1--5 and (4'), the expansion's five sections
  and distinct theorem numbering, the pp. 126--127 example, the source-time
  conditionality, and the Church/Büchi/Elgot/Putnam/Robinson remarks all have
  the correct source-page homes.  The priority language at `n-c-014.tex:757-764`
  is explicitly historical report, not independent adjudication.
- `logic-in-computer-science.tex:811-825` labels the displayed regular/MSO
  equivalence as a modern formulation, lists the original packages' different
  encodings, and says the compound name does not make the sentence verbatim in
  each source.  `n-c-014.tex:774-792` gives Thomas §3.1 the exact modern proof
  role while refusing to substitute it for either Russian body.  The source-
  navigation paragraph at `logic-in-computer-science.tex:2341-2347` preserves
  the same source order.  No compound-name folklore is laundered into
  Trakhtenbrot's announcement.
- Source-note lines 71--76 and compact-record line 648 preserve the controlling
  rights boundary: public inspection is not open-content licensing, the local
  PDFs are research objects, and no redistribution permission is inferred.
- Source-note lines 14--18 and 438--449, compact-record line 658 and consolidated
  status lines 911--913 all keep independent review pending.  “Body sufficient”
  is expressly limited to acquisition.  Nothing claims rendered-handbook,
  human, final-book, Part IX, or user acceptance.

## Mandatory coverage map

| Point | Disposition | Evidence/result |
|---|---|---|
| M01 | checked-clean | All seven labels recomputed before substantive review and matched exactly. |
| M02 | checked-clean | All 4+29 pages inspected at original detail; physical maps 1--4 = 326--329 and 1--29 = 103--131 confirmed. |
| M03 | checked-clean | Identities, journals, dates, volumes/issues, pagination, official title renderings, live Math-Net routes, source order, later-translation boundary, and rights qualification agree. |
| M04 | checked-clean | Non-specialist mathematical-Russian competence and exact evidence limits disclosed above; no specialist or line-by-line certification is claimed. |
| M05 | checked-clean | (mathcal I) syntax/domain/successor/eliminable extensions and (mathcal I') eventually-zero standing agree with expansion pp. 103--105 and 130--131. |
| M06 | checked-clean | Semantic fictitious occurrence, unequal lower/upper dependence, announcement Theorem 1, expanded normal form, and reported proof moves agree with pp. 326--327 and 103--109. |
| M07 | checked-clean | Typed stream map, anticipation/prefix equivalence, whole-suffix memory equations, weight, finite-window equations, (A)/Л standing, and nonimplications agree with pp. 327 and 109--112. |
| M08 | checked-clean | The one-state future-existence operator and primitive-recursive recognition/synthesis negative boundary are preserved at `n-c-014.tex:551-581`. |
| M09 | checked-clean | Portions, tuple extension, degree, basis, transition, graph/singleton examples, and uncountability counterexample agree with pp. 113--116. |
| M10 | checked-clean | Finite residual derivation and unconditional internal-transition construction independently checked above. |
| M11 | checked-clean | Closed converse, recurrence, projection/compactness argument, full closure characterization, and topological hypotheses independently checked above. |
| M12 | checked-clean | Internal transition is unconditional; external output/nonemptiness is conditional; Putnam is limited to the recurrent fragment. |
| M13 | checked-clean | Compact uniformity, one global bound, portion memory, and weight bound independently derived. |
| M14 | checked-clean | Expanded Theorem 2 is kept at finite-memory strength only. |
| M15 | finding-linked | The mathematical graph/solution distinction and every (4') clause are correct, but AP-R2-01 violates definition-before-use. |
| M16 | finding-linked | Both generality quantifiers and parameter/class standing are mathematically exact, but AP-R2-01 records that the technical names precede them. |
| M17 | checked-clean | No-solution/survival branches, deletion, parameters, closedness, weight, and conditionality independently reconstructed. |
| M18 | checked-clean | Theorem (3') remains separately quantified at each fixed (p); no unbounded generalization appears. |
| M19 | checked-clean | Explicit definition, semantic anticipation, finite residual termination, canonical tables, and the pp. 126--127 example retain exact scope. |
| M20 | checked-clean | Both word-set definitions and both theorem directions, including prefix closure and proper extension, independently checked. |
| M21 | checked-clean | (mathcal I'), special beginnings, existence/effectivity split, and Büchi attribution agree with pp. 130--131. |
| M22 | checked-clean | Announcement Theorems 1--5/(4') and expanded section results are compared without transferring numbering, title, or source strength. |
| M23 | checked-clean | Modern theorem and Thomas paragraph explicitly prevent compound-name/verbatim-source laundering. |
| M24 | checked-clean | Reader, source note, compact record, shared theorem, bibliography, and consolidated status agree on every substantive claim. |
| M25 | checked-clean | Locators, theorem numbers, formula roles, citations, title renderings, attributions, and bounded-translation qualifiers reconcile with the scans and official records. |
| M26 | finding-linked | AP-R2-01 is the sole definition-after-use/standing failure found; all other introduced technical names pass the five-part rule. |
| M27 | finding-linked | AP-R2-01 creates a local graph-versus-solution ambiguity; no other hidden continuity/closedness assumption, class collapse, source/translation/priority laundering, false compression, or status inflation remains. |
| M28 | checked-clean | Topic-only scope, rights boundary, and no-test/no-build/no-handbook-PDF boundary were observed and are accurately stated. |

VERDICT: REJECT — AP-R2-01
