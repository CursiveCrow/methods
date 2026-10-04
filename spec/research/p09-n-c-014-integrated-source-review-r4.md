# N-c-014 integrated source-fidelity review — blind Round 4

VERDICT: REJECT

## Review identity and scope

This is a fresh, direct review of the current LaTeX source.  The review covers:

- `handbook/parts/p09/presentations/n-c-014.tex`, line 1 through EOF (lines
  1--1852);
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 836--941, as the
  host context for the shared finite-word theorem, the S2S statement, the
  finite-tree nonconflation boundary, and the `n-c-014` input;
- all five permitted source notes, read completely:
  - `spec/research/p09-buchi-1960-source-note.md`;
  - `spec/research/p09-elgot-1961-source-note.md`;
  - `spec/research/p09-trakhtenbrot-1961-source-note.md`;
  - `spec/research/p09-rabin-1969-source-note.md`;
  - `spec/research/p09-thomas-1996-report-source-note.md`;
- the compact `N-c-014` source presentations in
  `spec/research/p09-source-presentations-lot2-3.md`, lines 681--745, and the
  relevant open-register statements at lines 967--980; and
- the relevant entries in `handbook/bib/handbook.bib`:
  `Buchi1959WeakReport`, `Buchi1960`, `BruyereEtAl1994`, `Elgot1959Report`,
  `Elgot1961`, `Elgot1962Errata`, `Trakhtenbrot1961`,
  `Trakhtenbrot1962Expanded`, `Rabin1969`, `Meyer1975Complexity`,
  `McNaughton1966`, `Thomas1996Report`, and `Thomas1997`.

The substantive audit asks whether the actual reader source accurately states
the historical identities, source objects, theorem and definition
attributions, proof roles, locators, source-versus-handbook ownership, and
bounded source-register standing supplied by that permitted evidence.  The
adjacent host material was used to test integration and nonconflation; this
review does not enlarge `N-c-014` into an audit of the neighboring `N-c-013`
or `N-c-015` presentations.

## Prohibited actions not taken

- No manuscript PDF, PNG, page image, rendered page, or other manuscript
  render was opened, inspected, produced, or cited.
- No historical-source PDF or historical page image was opened; the permitted
  notes resolved the source questions without a new publication-page visit.
- No TeX or PDF build was run.
- No test, test harness, automated checker, repository script, or hash command
  was run.
- `list_agents` was not called.
- No earlier standalone `N-c-014` review, admission record, board record,
  review-history file, decision ledger, or chair transcript was opened.  Review
  history appearing incidentally inside the expressly permitted source notes
  or compact source bullets was not used as evidence for this verdict.
- No manuscript, host, ledger, bibliography, source note, compact record, or
  prior report was edited.  This report is the only file created.

## Detailed source-fidelity findings

### 1. Büchi: correct precursor strength and explicit journal boundary

The Büchi presentation at `n-c-014.tex:8--230` consistently attributes its
technical reconstruction and page locators to the complete September 1959
UMR1083 report.  It does not use report locators as if they were locators in the
unreconciled 1960 journal article.  Lines 8--16 state the same-title precursor
relationship and expressly leave wording, numbering, examples, proof detail,
and page-by-page journal reconciliation open.  Lines 971--973 repeat the
precursor-strength boundary.

The technical claims agree with the permitted note: the finite-set meaning of
weak monadic quantification (`n-c-014.tex:18--29`); the propositional
formula-tuple automaton and transit recursion (`n-c-014.tex:31--46`); the exact
pointwise special-output identity and eventual-truth behavior
(`n-c-014.tex:47--71`); the synthesis and analysis roles
(`n-c-014.tex:73--142`); the terminal-marker finite-word encoding and Theorems
6--8 (`n-c-014.tex:144--169`); and the guarded finite decision argument
(`n-c-014.tex:171--190`).

The reader also preserves the source defects rather than laundering them into
source theorems.  The finite-witness repair of printed formula (2) is proved
and called handbook-owned (`n-c-014.tex:108--142`); the free-individual
off-by-one prose is bounded by the displayed source convention
(`n-c-014.tex:171--178`); and the false unary-powers-of-two equivalence is
separated from the later `\in_2`/`V_2` correction
(`n-c-014.tex:192--230`).  The bibliography entries preserve the distinct 1959
report, 1960 article identity, and 1994 correction source.

### 2. Elgot: controlling article, precursor, errata, and handbook completions remain distinct

The Elgot presentation at `n-c-014.tex:232--569` uses the complete 1961 article
as the controlling publication, the 1959 UMR1342 report as a separately named
precursor, and the 1962 errata as the owner of the published corrections.  The
bibliography identities and the article's corrected pp. 21--51 range agree with
the permitted source note.

The source objects and proof roles are accurately separated: the
`I`-automaton tuple and empty-word convention (`n-c-014.tex:239--257`); the
canonical finite-set encoding and both directions of Theorem 5.3
(`n-c-014.tex:259--330`); the arithmetic consequences
(`n-c-014.tex:332--344`); the distinct `A/B` transducer, Theorems 7.1 and 7.3,
Lemma 6.1, Theorem 8.1, and Corollary 8.2 (`n-c-014.tex:346--441`); and the
Chapter IV negative boundary (`n-c-014.tex:544--557`).

The corrected Section 8.6 route states the erratum's finite union and tagged
projection rather than the false printed single-relation claim
(`n-c-014.tex:443--542`).  The arity-one promotion is explicitly identified as
a handbook completion, not as text printed by the erratum
(`n-c-014.tex:524--537`).  The local version-comparison paragraph at lines
559--569 concerns the three article/report corrections listed in that
paragraph and does not erase the separately stated ownership of the unary
completion.

### 3. Trakhtenbrot: the two Russian bodies, terminology, and repairs are bounded correctly

The Trakhtenbrot presentation at `n-c-014.tex:571--977` preserves the distinct
1961 announcement and 1962 expanded-article strengths, their different official
English title renderings, and their separate page and theorem locators.  It
does not claim a complete English translation.  The typographical rendering
of Cyrillic И as `\mathcal I`, the announcement's Л terminology, and the
expansion's Latin `A` terminology are all announced rather than silently
normalized (`n-c-014.tex:571--603`, `663--678`).

The primitive grammar, controlled-formula classes, operator types, whole-future
finite-memory equations, anticipation, weight, portions, homogeneity,
definability, conditional algorithms, finite realization, general solutions,
and fixed-lookahead result match the bounded source-note reconstruction
(`n-c-014.tex:583--687`, `689--896`).  The reader keeps source terms and
handbook exactifications apart: the typed residual maps are explicitly
handbook-owned (`n-c-014.tex:715--741`); the counterexample to the printed
weight/degree inference is proved and owned by the handbook
(`n-c-014.tex:743--779`); and the nonempty covering restriction and empty-set
case are likewise identified as handbook additions (`n-c-014.tex:784--827`).

The positive-length word maps, automaton-enumerability and
automaton-decidability definitions, nonempty-language correction, weak system
`\mathcal I'`, and special-beginning bridge preserve the source's literal
finite-word route rather than retroactively attributing the modern one-line
regular/MSO theorem to the four-page announcement
(`n-c-014.tex:898--969`).

### 4. Rabin: source acceptance, dual construction, and actual emptiness proof are not conflated

The Rabin presentation at `n-c-014.tex:1053--1656` accurately distinguishes
the successor structures, ordinary infinite-tree automaton, and later dual
construction.  In particular, Definition 1.5's acceptance datum is
`F \subseteq \mathcal P(S)` and has the prefix `\exists r\,\forall\pi`;
the finite pair sequence belongs to dual acceptance with prefix
`\forall r\,\exists\pi` (`n-c-014.tex:1059--1168`, `1319--1367`).  The
formula-track construction, both definability directions, and direct
sentence-to-emptiness reduction have their proper theorem roles
(`n-c-014.tex:1170--1263`).  Theorem 3.1's deterministic-word product and its
McNaughton dependency are separately stated (`n-c-014.tex:1265--1317`).

The reader gives exact definitions, standings, distinctions, and later uses
for the finite-tree frontier, `frontiered`, the external frontier value, the
dual zero-length normalization, well-founded obligation mapping, and finite
table-run (`n-c-014.tex:1216--1242`, `1369--1491`, `1538--1616`).  The
zero-pair, empty-`H`, and empty-`U_0` cases are explicitly handbook-owned rather
than attributed to Rabin.  Section 3.12 is reconstructed as Rabin's actual
one-letter/dual-language/weak-finite-tree decision route, not as Thomas's later
regular-tree basis argument (`n-c-014.tex:1502--1626`).  The Chapter II map and
the proof-boundary paragraph keep the applications visible without pretending
to reproduce every source induction (`n-c-014.tex:1628--1656`).

Rabin's printed elementary-recursive qualification is reported as a historical
claim and withdrawn as a handbook complexity conclusion in light of the later
Meyer lower bound (`n-c-014.tex:1097--1108`, `1618--1626`).  The Rabin and Meyer
bibliography entries match the permitted identities.

### 5. Thomas: finite-word precursor boundary passes; the tree-game typing does not

The finite-word Thomas passage at `n-c-014.tex:979--1051` consistently cites
the May 1996 report and reconstructs report Section 3.1 at precursor strength.
Its automaton tuple, `n+1`-state run, finite-word structure, both directions of
Theorem 3.1, empty-word guard, `MSO_0` atomic automata, `WS1S` distinction, and
Presburger route agree with the permitted note.  It is explicitly kept separate
from the three original presentations.

The later tree passage correctly says that Thomas's Sections 6.1--6.2 are a
post-1969 game-theoretic route, not Rabin's original proof
(`n-c-014.tex:1658--1695`).  The Muller tuple, global-run/all-path acceptance,
strict chain, empty-chain handbook completion, and order-vector-with-hit memory
are stated with their proper standings (`n-c-014.tex:1660--1722`).  The
registered 1997 chapter is not used for a report locator, and lines 1847--1852
expressly leave every Thomas locator at May 1996 report-precursor strength.

There is, however, one operative type break in the rejecting-state completion.
It is detailed under the must-fix finding below.

### 6. Host theorem, citations, and source-register boundary

The host theorem at `logic-in-computer-science.tex:836--851` labels its displayed
finite-word equivalence as a modern formulation and immediately explains that
Büchi, Elgot, and Trakhtenbrot use different encodings and result packages.  It
does not claim that the displayed sentence occurs verbatim in each source.  The
host's separate S2S theorem (`logic-in-computer-science.tex:874--879`) and
finite-ranked-tree discussion (`logic-in-computer-science.tex:881--931`) keep
Rabin's infinite-tree automata distinct from bottom-up finite-tree automata.
The `n-c-014` input occurs at line 939.

The technical locators in the presentation use the source actually supporting
them: UMR1083 rather than an unread 1960 journal page; Elgot's article and
errata for publication claims; the two Trakhtenbrot bodies at their distinct
strengths; Rabin 1969 for Rabin's construction; Meyer 1975 only for the later
complexity correction; and `Thomas1996Report` rather than `Thomas1997` for the
report sections.  No citation in the reader purports to close the missing
1960-journal or 1997-chapter comparison.

The compact open register still owes (i) acquisition and page-by-page
reconciliation of Büchi's 1960 journal article or 1990 reprint against UMR1083,
and (ii) acquisition and reconciliation of Thomas's registered 1997 chapter
against the May 1996 report.  The manuscript properly bounds both obligations;
they are not themselves defects in a precursor-strength presentation, but they
prevent the source register from closing.

### 7. Local technical-name rule

The reader generally satisfies the local rule.  Source terms are introduced
with exact definitions and standings, and the editorial terms that carry real
work also state their necessity and nonredundancy before later use.  Salient
examples are the residual stream operators (`n-c-014.tex:720--741`),
`frontiered` (`n-c-014.tex:1216--1230`), the one-pair dual normalization
(`n-c-014.tex:1369--1392`), the finite table-run (`n-c-014.tex:1556--1571`),
and the completed chain automaton (`n-c-014.tex:1724--1753`).  I found no
merely speculative technical name that should instead have remained an owed
artifact.  The defect below is not a failure to justify the completion's name;
it is a failure to carry its newly defined state set into the game that uses it.

## Must-fix source-fidelity defect

### MF-1 — The completed Thomas game excludes the newly added state from its displayed position set

At `n-c-014.tex:1732--1739`, the handbook correctly defines the completed state
set

\[
Q^\bot=Q\cup\{\bot\}
\]

and adds transitions whose two successor states are `\bot`, together with the
`\bot` self-loops.  Lines 1741--1753 correctly explain why this completed
automaton preserves the recognized language and supplies the nonempty-outdegree
premise required by the game theorem.

The renaming at `n-c-014.tex:1755--1757`, however, says only that the completed
automaton and transition relation are again written `\mathcal A` and `\Delta`.
It never rebinds `Q` to `Q^\bot`.  The game is then defined at
`n-c-014.tex:1759--1766` with Automaton positions

\[
(u,q)\in T\times Q.
\]

For a formerly missing state/letter case, the now-renamed `\Delta` permits
`\tau=(q,t(u),\bot,\bot)`.  After Pathfinder chooses either direction, the
displayed next position is `(ud,\bot)`, which is not in `T\times Q` because
`\bot\notin Q` was fixed at line 1732.  Thus the displayed game is not closed
under its own moves, and the statement at line 1766 that completion makes every
play infinite is not established for the game as typed.  The same mismatch
undercuts the claimed placement inside the game theorem's hypothesis at
`n-c-014.tex:1789--1797` and therefore the later complementation, regular-basis,
and S2S route that invokes that game (`n-c-014.tex:1799--1845`).

The minimal repair is to rebind the state-set notation explicitly when the
completed automaton is renamed—for example, say that `Q^\bot`,
`\mathcal A^\bot`, and `\Delta^\bot` are henceforth written `Q`, `\mathcal A`,
and `\Delta`—or to retain `Q^\bot` in the game position set and every ensuing
state type.  The transition and instruction types must then use the same
completed state set.  This is a must-fix definedness/source-presentation defect,
not an open-source-body obligation.

## Disposition

The Büchi, Elgot, Trakhtenbrot, Rabin, finite-word Thomas, host, bibliography,
ownership, locator, and bounded-register checks otherwise pass at the exact
strengths stated above.  The single Thomas completion defect prevents approval
of this unchanged source snapshot.  The independently open Büchi-journal and
Thomas-chapter reconciliations remain open regardless of that manuscript fix.

REGISTER STATUS: OPEN
