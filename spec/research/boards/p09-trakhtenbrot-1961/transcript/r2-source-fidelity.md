# Round 2 source-fidelity, language, and evidence review

## Scope, independence, and language competence

I audited the complete seven-object Frozen Round 2 snapshot identified in the
charter.  I did not read the board ledger, the chair transcript, a Round 1
report, or another Round 2 report, and I did not contact another reviewer.  I
did not inspect a handbook PDF or run a test, checker, repository script, TeX
command, or build.  SHA-256 was used only to confirm the seven frozen identity
labels.

I am not a native Russian speaker, a certified translator, a Slavicist, or a
Russian-language specialist.  I have working reading competence in
mathematical Russian sufficient to parse the printed definitions, theorem
statements, proof transitions, examples, qualifications, and historical
remarks in these two papers and to compare them with the bounded English
reconstruction.  I inspected the scan glyphs, formulae, theorem typography,
page layout, and bibliographic matter directly.  The searchable extractions
were treated, where useful, only as navigation aids; no OCR reading controlled
a word, symbol, formula, or translation judgment.  This evidence supports the
mandate at the reconstruction's stated strength, but it does not constitute or
imply Russian-language-specialist certification.

## Frozen identities and page control

All seven recomputed SHA-256 labels agree exactly with the charter:

| Frozen object | Recomputed SHA-256 |
|---|---|
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961.pdf` | `44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9` |
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded.pdf` | `EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D` |
| `handbook/parts/p09/presentations/n-c-014.tex` | `109A631EBAFAC28A7C84A946FE4E305E91BA1818B7E4E9F08FCF4E15E4B95B72` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD` |
| `handbook/bib/handbook.bib` | `75AB70009DF4AB8B2180CFFC6987EA244ADB2F978B1D889C87009EFF17066D5C` |
| `spec/research/p09-trakhtenbrot-1961-source-note.md` | `6D84E96A50414E10FE229536D3E8A4557BEB45D2D0024DF182E6AD75D3DD41DC` |
| `spec/research/p09-source-presentations-lot2-3.md` | `DFFF60FBB6E0C715A9B41D7000D670B374B0B62A86305AC2BAF92CA46726A687` |

I visually inspected all four announcement images and all twenty-nine
expansion images at original detail.  The physical-to-printed maps are
continuous:

- announcement physical page (i) is printed page (325+i), so pages 1--4
  are pp. 326--329;
- expansion physical page (i) is printed page (102+i), so pages 1--29 are
  pp. 103--131.

The announcement scan prints *Doklady Akademii Nauk SSSR*, volume 140, no. 2
(1961), the Russian title, presentation by P. S. Novikov on 16 May 1961,
receipt on 29 April 1961, and pp. 326--329.  The expansion scan prints
*Sibirskii Matematicheskii Zhurnal*, volume III, no. 1, January--February 1962,
the same Russian title, receipt on 15 May 1961, and pp. 103--131.  The official
Math-Net records independently confirm the respective English renderings
"Finite Automata and the Logic of Single-Place Predicates" and "Finite
Automata and the Logic of One-Place Predicates," the dates, volumes, issues,
page ranges, Russian language, and full-text access routes.  The cited AMS
volume record confirms the later 1966 English-translation route; its body is
not used.  Math-Net's terms reserve copyright and republication rights while
allowing individual noncommercial teaching/research printing.  The source
note's no-open-licence and no-redistribution qualification is therefore honest.

## Source/result crosswalk

The reader preserves the unequal source strengths and does not transfer
numbering between them:

| 1961 announcement | 1962 expansion | Reader treatment |
|---|---|---|
| Theorem 1, p. 327, after the lower/upper terminology on p. 326 | Section 1 normal-form theorem and proof, pp. 105--109 | `n-c-014.tex:512--525` states semantic fictitious occurrence, the two dependence directions, effective transformation, and the proof moves. |
| Theorem 2, p. 327 | Section 3, Theorem 1, pp. 116--118 | `n-c-014.tex:604--607` gives homogeneity plus effective internal transition. |
| Theorem 3, p. 328 | Section 3, Theorems 2 and (2'), p. 118 | `n-c-014.tex:607--631` keeps closedness, recurrence, closure operations, and the open Borel/projective question explicit. |
| Theorem 4, p. 328 | Section 4, Theorem 1, pp. 119--120 | `n-c-014.tex:642--650` requires an exactly defined continuous total graph, obtains bounded anticipation and finite memory, and preserves the weight bound. |
| Theorem (4'), p. 328 | Related Section 4 existence/general-solution development, pp. 119--124, without silently assigning the announcement number to it | `n-c-014.tex:654--663` distinguishes relation-solving from graph-definition and records the closed and open cases at their printed strengths. |
| Theorem 5, pp. 328--329 | Section 4, Theorem 3, pp. 121--124 | `n-c-014.tex:665--699` gives both general-solution quantifiers, stable deletion, the no-solution/surviving-family branches, parameter choice, closedness, weight, and conditionality. |
| No transferred announcement number | Section 4, Theorem 2, p. 120; Theorem \(3'\), p. 124; Section 5, pp. 124--131 | `n-c-014.tex:650--652,692--755` labels these as expansion-only additions and preserves finite memory versus finite operator, fixed \(p\), explicit synthesis, word sets, and \(\mathcal I'\). |

The typographical normalization of printed Cyrillic И to \(\mathcal I\)
is declared at `n-c-014.tex:499--510`.  Printed Cyrillic Л in the announcement
and Latin \(A\) in the expansion are separated and then deliberately normalized
to the expansion's \(A\) only in cross-version prose at `n-c-014.tex:563--570`.
No source silently lends the other its title, theorem number, or class letter.

## Independent mathematical/source checks within this mandate

The normal form supplies the asserted homogeneity mechanism.  Fixing a finite
prefix changes a lower (t)-formula only through one of finitely many Boolean
functions of its bounded window, while the upper component is shifted as a
tail formula.  Hence only finitely many residual formulae occur; appending a
letter updates one residual to another by the printed syntactic construction.
This independently verifies both homogeneity and effective internal
transition in `n-c-014.tex:604--607` against expanded pp. 116--118.

Conversely, a finite portion basis supplies a finite state index.  A choice bit
selects a permitted next symbol, and the internal portion transition updates
the state.  The one-hot initial state selects the original set rather than an
arbitrary portion.  Existentially quantifying the state and choice streams
gives the displayed current/next recurrence.  Closedness turns compatible
finite prefixes into membership; in the reverse direction the local recurrence
is a projection of a closed subset of a compact stream space and has only
finitely many state residuals.  Complement, finite union, and projection then
give exactly the recorded closure characterization.  This verifies
`n-c-014.tex:607--631` against expanded pp. 116--119 without importing modern
regular-language folklore.

The operator distinctions also survive direct checking.  Expanded pp. 109--112
allow the external and internal memory functions to inspect the whole future
suffix, so one state does not imply bounded or effective future dependence.
Adding one fixed lookahead window gives the finite-operator equations; setting
that bound to zero gives the expansion's (A)-operators.  Expanded pp. 119--120
use compact uniformity to obtain one lookahead bound for a continuous total
definable graph and use the finite portion basis for memory.  Dropping
continuity in expanded Theorem 2 leaves only the latter argument.  The reader
states exactly this nonimplication at `n-c-014.tex:538--572,642--652`.

For Section 5, the direct scan confirms the semantic anticipation criteria on
p. 125, the terminating shifted-formula construction on pp. 125--126, and the
two residual formulae and both printed tables on pp. 126--127.  The two
finite-word directions on pp. 127--128 use, respectively, existential input
reconstruction for recognition and a prefix/extendibility-guided output choice
for enumeration.  On pp. 130--131, formula (2) says exactly that the presented
prefix agrees with some eventually-zero satisfying predicate; this yields the
special-beginning language and is prefix-dependent.  Effectivity is asserted
only for \(\mathcal I'\)-formulae and is explicitly credited to Büchi.  The
reader's `n-c-014.tex:701--755` preserves all of these boundaries.

## Findings

No blocker, must-fix, should-fix, or source-critical consider finding remains
within this mandate.  In particular, I found no false compression, hidden
continuity or closedness assumption, finite-memory/finite-operator collapse,
graph/solution collapse, unbounded-lookahead inflation, title or numbering
transfer, OCR-controlled formula, modern-theorem laundering, specialist-
translation claim, rights overclaim, or premature admission claim.

## Mandatory coverage map

| Point | Status | Evidence |
|---|---|---|
| M01 | checked-clean | Seven exact identity matches are listed above; no content inference was made from a hash. |
| M02 | checked-clean | All 4+29 page images inspected at original detail; physical/printed maps are 1--4 to 326--329 and 1--29 to 103--131. |
| M03 | checked-clean | Scan title pages and colophons; official Math-Net records `dan25511` and `smj4799`; source note `24--76`; bibliography `5991--6013`; compact record `648`. |
| M04 | checked-clean | Precise non-native, non-specialist working-competence disclosure and controlling visual evidence stated above; source note `14--18,100--104,438--447` and reader `770--772` make the same bounded claim. |
| M05 | checked-clean | Expanded pp. 104--105 and 130--131; reader `499--510,746--755`; source note `80--98,106--124,377--386`. |
| M06 | checked-clean | Announcement pp. 326--327; expanded pp. 105--109; reader `512--525`; source note `126--142`.  Semantic fictitious occurrence and every reported normal-form proof move agree. |
| M07 | checked-clean | Expanded pp. 109--112; reader `527--572`; source note `144--182`.  Total stream map, anticipation/prefix equivalence, whole-suffix memory equations, weight, finite windows, (A)-standing, and all nonimplications agree. |
| M08 | checked-clean | Expanded pp. 111--112; reader `551--554,574--581`; source note `170--182`.  The one-state strict-future example and both primitive-recursive recognition/synthesis reductions agree. |
| M09 | checked-clean | Expanded pp. 113--116; reader `583--602`; source note `184--215`.  Portions, tuple extension, degree, basis, transition, graph/singleton examples, and uncountability argument agree. |
| M10 | checked-clean | Expanded pp. 116--118; reader `604--607,633--640`; source note `219--257`; independent residual derivation stated above. |
| M11 | checked-clean | Expanded pp. 116--119; reader `607--631`; source note `226--257`; independent finite-basis recurrence, compact closedness, converse, and closure derivation stated above. |
| M12 | checked-clean | Announcement pp. 326, 328--329; expanded pp. 118--119 and 124; reader `633--640,687--697`; source note `251--257,304--331`.  Internal transition is unconditional, emptiness/output choice is conditional, and Putnam is restricted to the recurrent fragment. |
| M19 | checked-clean | Expanded pp. 124--127; reader `701--714`; source note `333--346`.  Explicit standing, semantic criteria, termination, equations, and the exact two-formula example role agree. |
| M20 | checked-clean | Expanded pp. 127--128; reader `716--744`; source note `348--375`.  Both word-set definitions, both theorem directions, prefix closure, and proper extendibility agree. |
| M21 | checked-clean | Expanded pp. 130--131; reader `746--755`; source note `377--386`.  \(\mathcal I'\), special beginnings, existence/effectivity split, and Büchi attribution agree. |
| M22 | checked-clean | Announcement pp. 326--329 and expansion pp. 103--131 were compared theorem by theorem; the crosswalk above records every used announcement number and every expansion-only result. |
| M23 | checked-clean | Shared theorem `logic-in-computer-science.tex:811--825`, source navigation `2341--2347`, and reader `757--792` label the one-sentence equivalence as modern and keep Büchi, Elgot, Trakhtenbrot, and Thomas source packages distinct. |
| M24 | checked-clean | Reader `487--772`, source note `1--449`, compact record `646--658,911--913`, shared theorem/navigation, and bibliography entries agree on every Trakhtenbrot claim and admission status.  Noncontrolling reading-aid hashes were not recomputed, as required by the charter. |
| M25 | checked-clean | All reader locators at `524--525,630--631,698--699,755`, theorem numbers, displayed formulae, title forms, citations, and historical qualifications agree with the controlling printed pages. |
| M26 | checked-clean | Every technical distinction used in the Trakhtenbrot reconstruction is source-defined or exactly eliminated at first use, has explicit standing, differs from its neighbors, and is used later.  No hypothetical named artifact, definition-after-use, redundant name, or unused distinction occurs. |
| M27 | checked-clean | Adversarial checks found no hidden hypothesis, class collapse, source/translation/priority inflation, source laundering, or misleading completion status. |
| M28 | checked-clean | Review remained topic-only and source/manuscript-only; rights and no-redistribution limits remain explicit; no test, checker, script, TeX command, build, or handbook-PDF inspection was used. |

VERDICT: ACCEPT
