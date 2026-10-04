# N-c-014 integrated source review — blind Round 5

VERDICT: REJECT

## Review scope

This was a fresh, direct-source-LaTeX source-fidelity review of the current
N-c-014 presentation.  The verdict concerns historical/source fidelity,
attribution, locators, source-versus-handbook ownership, bounded register
language, and the local rule governing new technical names.  It is not a
typesetting, build, rendered-page, or general mathematical-proof verdict.

## Evidence read

The following permitted text evidence was read directly:

- `handbook/parts/p09/presentations/n-c-014.tex`, lines 1--1859, from the first
  line through EOF;
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 836--941;
- `spec/research/p09-buchi-1960-source-note.md`, in full;
- `spec/research/p09-elgot-1961-source-note.md`, in full;
- `spec/research/p09-trakhtenbrot-1961-source-note.md`, in full;
- `spec/research/p09-rabin-1969-source-note.md`, in full;
- `spec/research/p09-thomas-1996-report-source-note.md`, in full;
- the N-c-014 source-status section of
  `spec/research/p09-source-presentations-lot2-3.md`, lines 681--745, and the
  relevant open-register statements at lines 967, 974--975, and 980; and
- the relevant entries in `handbook/bib/handbook.bib` for
  `Buchi1959WeakReport`, `Buchi1960`, `BruyereEtAl1994`, `Elgot1959Report`,
  `Elgot1961`, `Elgot1962Errata`, `Trakhtenbrot1961`,
  `Trakhtenbrot1962Expanded`, `Rabin1969`, `Meyer1975Complexity`,
  `McNaughton1966`, `Thomas1996Report`, and `Thomas1997`.

No historical publication page was needed to resolve an ambiguity other than
the blocking terminology ambiguity identified below; the permitted notes do
not resolve that ambiguity, so no additional publication page was treated as
evidence.

## Prohibited actions not taken

- I did not open, inspect, render, build, or cite a manuscript PDF, historical
  PDF, PNG, page image, or any other render.
- I did not run a TeX/PDF build, test, test harness, automated checker,
  repository script, hash, or other automated validation.
- I did not read an earlier N-c-014 integrated review, admission record,
  board file, decision ledger, chair transcript, or review-history file.  I did
  not follow the review-record links appearing inside the permitted notes and
  compact record.
- I did not call `list_agents`.
- I did not edit the presentation, host, source notes, compact record,
  bibliography, ledger, or any prior report, and I did not add an admission
  record.  This Round 5 report is the only file created by this review.

## Must-fix finding

### F1 — `one-homogeneous` is an undefined and genuinely ambiguous technical name

**Location:** `handbook/parts/p09/presentations/n-c-014.tex:788`.

The presentation defines a set to be “homogeneous of degree at most \(k\)” at
lines 714--716 and separately works with one-coordinate and tuple stream spaces
at lines 695--713.  It then says at line 788 that there are “uncountably many
one-homogeneous sets.”  The text never says whether `one` means:

1. homogeneity degree at most \(1\); or
2. a homogeneous subset of a one-coordinate stream space, as opposed to the
   tuple spaces just defined.

Those readings concern different parameters and therefore different statement
families.  The phrase is not an exact eliminable definition, its standing is
not fixed, its nonredundancy is not explained, and no later definition or
theorem requires the shorthand.  An existing defined phrase can state the
claim without ambiguity.  The permitted Trakhtenbrot note repeats
“one-homogeneous” but does not eliminate this two-way reading, so that note
cannot cure the manuscript's first-use defect.

This violates the local AGENTS rule and blocks source-fidelity acceptance:
the review cannot tell which exact source-backed cardinality claim the
manuscript is asserting.

**Required repair:** replace the shorthand at line 788 by the exact intended
statement.  If `one` denotes degree, the minimal repair is:

> there are uncountably many homogeneous sets of degree at most \(1\), but
> only countably many \(\mathcal I\)-formulae.

If `one` instead denotes coordinate arity, say that explicitly and retain the
already defined degree terminology separately.  Do not introduce another name
for the distinction.  The repaired sentence must be reconciled with the
controlling Russian-source reconstruction before a fresh verdict.

## Detailed source-fidelity findings

Apart from F1, I found no must-fix source-fidelity defect in the inspected
snapshot.

| Component | Evidence basis represented in the manuscript | Boundary found in the actual LaTeX | Result |
|---|---|---|---|
| Büchi | Complete September 1959 UMR1083 precursor plus later correction evidence; registered 1960 identity kept separately | Lines 8--16 and 977--979 expressly deny journal wording, numbering, example, proof-detail, and page identity; all mathematical locators are to `Buchi1959WeakReport` | Bounded honestly; 1960 reconciliation remains open |
| Elgot | Complete 1961 article, 1959 precursor, and controlling 1962 errata | Lines 234--239 and 565--575 give the authority order; lines 530--543 mark the unary-window completion as handbook-owned rather than erratum text | Source and correction ownership are explicit |
| Trakhtenbrot | Distinct complete 1961 announcement and 1962 expansion | Lines 577--587 preserve publication, title, pagination, and theorem-number boundaries; lines 676--684 preserve the Cyrillic/Latin operator-name distinction; lines 977--983 deny a complete line-by-line translation | Sound except for F1 |
| Rabin | Complete 1969 article, with Meyer's later lower-bound correction kept separate | Lines 1059--1114 distinguish Rabin's definitions/decidability from the later complexity correction; lines 1508--1632 reconstruct Rabin's actual emptiness route rather than a later basis proof | Source route and later correction are not conflated |
| Thomas | Complete May 1996 Kiel report precursor; registered 1997 chapter identity separate | Lines 985--1057 and 1664--1859 consistently use report locators; lines 1854--1859 state expressly that the 1997 chapter is not in the source basis | Bounded honestly; 1997 reconciliation remains open |

### Büchi finite-word presentation

- Lines 18--29 give the finite-set interpretation of `W.2.A.` and distinguish
  it from full-set infinite-word logic.
- Lines 31--71 keep propositional automaton data, induced time predicates, and
  behavior sets at separate standings.  The special-output identity agrees
  with the permitted source reconstruction.
- Lines 73--142 distinguish the printed Theorem 2 defect from the
  handbook-owned corrected finite witness and prove the ownership boundary
  rather than silently attributing the repair to Büchi.
- Lines 144--171 retain the terminal marker and the empty-word convention in
  the source's finite-word encoding.
- Lines 173--232 preserve the false-tail condition and inclusive search bound,
  identify the printed arithmetic counterexamples, and attribute the
  `in_2`/`V_2` correction to later scholarship.  No journal page locator is
  used for a claim verified only in the report.

The host theorem at lines 836--850 labels its displayed finite-word sentence as
a modern formulation, says that the original source packages differ, and does
not claim verbatim occurrence in each source.  Its citation list keeps
`Buchi1959WeakReport` and `Buchi1960` separate.  In the context of the explicit
presentation boundary, this is a bounded historical citation rather than a
claim that the unread journal body supplied the report locators.

### Elgot presentation

- Lines 241--259 give the correctly typed source acceptor and exact empty-word
  convention.
- Lines 261--346 reconstruct the canonical admissible encoding and both
  effective directions of Theorem 5.3 rather than collapsing them into a
  modern compound-name attribution.
- Lines 348--447 distinguish acceptor, synchronous transducer, finite behavior,
  source-specific prefix openness, and causal infinite behavior.  The maximal
  strongly extendable sublanguage is explicitly defined before use.
- Lines 449--548 state the literal restricted syntax, the published
  finite-union correction, the tagged construction, and the separately owned
  handbook completion for unary windows.
- Lines 550--575 preserve the negative decision boundary and the exact
  article/report/errata authority order.

The bibliography entries reproduce the inspected identities and keep the
article, precursor, and errata as three distinct objects.

### Trakhtenbrot presentation

- Lines 589--638 define the normalized name `\mathcal I`, its standing, its
  primitive grammar and interpretation, the controlled formula classes, and
  their semantic consequences.
- Lines 640--693 distinguish anticipation, broad finite memory, finite
  operator, and the source's 1961/1962 names for the automaton-realizable
  zero-anticipation class.
- Lines 695--747 define portions, tuple portions, homogeneity, graph portions,
  and the handbook-owned residual maps with their standings and later use.
- Lines 749--785 expressly identify the source's false degree bound and the
  handbook-owned counterexample rather than silently repairing the source.
- Lines 790--966 distinguish definability, conditional effectivity, graph
  definition versus solution, general solutions, fixed-lookahead results,
  automaton-enumerability, automaton-decidability, and the handbook-owned
  empty-language repair.

The normalized/source technical names otherwise satisfy the local rule: they
are defined, assigned a standing, distinguished from nearby terms, and used in
the later construction.  F1 is the one exception found.

### Rabin presentation

- Lines 1065--1165 preserve Rabin's root symbol, two order relations,
  arbitrary-root valued trees, transition-table/automaton distinction,
  ordinary Muller-family acceptance, and the `exists run / every path`
  quantifier order.
- Lines 1176--1269 reconstruct both logical directions and explicitly label
  the worked two-track instance as handbook-worked rather than source-printed.
- Lines 1271--1323 state the external McNaughton dependency and the exact
  deterministic product used in Rabin's Theorem 3.1.
- Lines 1325--1506 keep ordinary and dual acceptance separate.  The
  zero-length normalization is defined and labelled handbook-owned;
  `frontiered` and Rabin's well-foundedness condition receive exact definitions,
  standings, nonredundancy explanations, and later proof uses.
- Lines 1508--1632 give the one-letter reduction, restricted-table semantics,
  finite table-run standing, two empty-witness repairs, and external weak-tree
  decision dependency.  They do not substitute Thomas's regular-tree basis
  route for Rabin's source proof.
- Lines 1634--1662 bound the applications and the omitted transition-level
  detail without claiming complete reproduction of the article.

The host S2S theorem at lines 874--879 is a concise modern successor-structure
statement supported by the fully bounded Rabin presentation; it does not import
the host's later finite-ranked-tree automaton definition into Rabin's proof.

### Thomas report-precursor presentation

- Lines 985--1057 use `Thomas1996Report` for Section 3.1, distinguish finite
  word structures from `WS1S`, and keep the modern survey proof separate from
  the three historical finite-word presentations.
- Lines 1664--1728 identify the later game-theoretic route, define the chain and
  its handbook-owned empty endpoint, and give the exact standing and use of the
  order-vector-with-hit memory.
- Lines 1730--1759 expose and repair the report's partial-transition/game
  premise, prove language preservation, and state that the completion is
  handbook-owned.
- Lines 1761--1852 keep the game, strategies, instruction-labelled trees,
  regular generated trees, automata, runs, and successor structure distinct.
- Lines 1854--1859 state the decisive publication boundary: no locator is
  attributed to the registered 1997 chapter.

The bibliography has distinct `Thomas1996Report` and `Thomas1997` entries, and
the compact register keeps final-chapter reconciliation open.  The manuscript
therefore does not overstate the acquired source strength.

## Register disposition

Even after F1 is repaired and independently re-reviewed, this review cannot
close the source register.  Two publication-version obligations remain exactly
open:

1. acquire and reconcile the registered Büchi 1960 journal article (or the
   authorized 1990 reprint) against UMR1083; and
2. acquire and reconcile Thomas's registered 1997 handbook chapter against the
   May 1996 report precursor.

Elgot's controlling article/errata body, the two distinct Trakhtenbrot bodies,
and Rabin's controlling article are represented at the bounded strengths
recorded in the permitted evidence.  This report makes no admission decision
for N-c-014 overall, Part IX, a rendered handbook, a build, the book, or
publication.

REGISTER STATUS: OPEN
