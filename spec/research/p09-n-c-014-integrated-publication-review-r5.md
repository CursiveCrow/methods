# N-c-014 integrated publication-text review — Round 5

VERDICT: REJECT

## Review scope

This was a fresh, blind, text-only publication review of the current N-c-014
snapshot.  I reviewed the presentation as one integrated graduate-reference
unit, not as a collection of previously reviewed source visits.  The verdict
tests definition-before-use, notation stability, exact standing, logical
sequence, reference completeness, source/handbook ownership, citation support,
host consistency, and the local technical-name rule.

## Evidence read

- `handbook/parts/p09/presentations/n-c-014.tex`, line 1 through line 1859,
  including the complete final line and no omitted interval.
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 836--941.
- The complete permitted source notes:
  `spec/research/p09-buchi-1960-source-note.md`,
  `spec/research/p09-elgot-1961-source-note.md`,
  `spec/research/p09-trakhtenbrot-1961-source-note.md`,
  `spec/research/p09-rabin-1969-source-note.md`, and
  `spec/research/p09-thomas-1996-report-source-note.md`.
- The compact N-c-014 source and open-obligation bullets in
  `spec/research/p09-source-presentations-lot2-3.md`.
- The relevant bibliography entries in `handbook/bib/handbook.bib`:
  `Buchi1959WeakReport`, `Buchi1960`, `BruyereEtAl1994`, `Elgot1959Report`,
  `Elgot1961`, `Elgot1962Errata`, `Trakhtenbrot1961`,
  `Trakhtenbrot1962Expanded`, `Rabin1969`, `Meyer1975Complexity`,
  `McNaughton1966`, `Thomas1996Report`, and `Thomas1997`.

The permitted notes were used as text.  I did not open any source artifact or
render that they describe; no concrete ambiguity required a historical-page
visit.

## Prohibited actions not taken

- I did not open, inspect, render, build, or cite a manuscript PDF, PNG, page
  image, contact sheet, or other manuscript render.
- I did not run a test, harness, automated checker, repository script, hash,
  TeX command, PDF command, or manuscript build.
- I did not read an earlier N-c-014 review, admission record, board file,
  ledger, chair transcript, decision record, or review-history file.  I did
  not follow the review-history links contained in the permitted notes and
  compact record.
- I did not edit the presentation, host, ledger, bibliography, source notes,
  compact record, or any prior report, and I did not add an admission record.
- I did not call `list_agents`.
- I make no finding about pagination, rendered typography, visual placement,
  page breaks, or layout.

## Must-fix findings

### 1. The host theorem omits the letter predicates required for the stated finite-word equivalence

**Location:** `handbook/parts/p09/logic-in-computer-science.tex`, lines
837--840.  The controlling contrast is in
`handbook/parts/p09/presentations/n-c-014.tex`, lines 994--1007 and 1025--1041.

The host says that \(L\subseteq\Sigma^*\) is definable in monadic second-order
logic “over positions with order” exactly when it is regular.  As written, the
signature mentions order, or successor and endpoints, but no unary predicate
that records which letter occurs at a position.  The detailed presentation
correctly gives Thomas's word structure as

\[
 \mathfrak W_w=
 \bigl(\operatorname{Pos}(w),S^w,(P_a^w)_{a\in\Sigma}\bigr).
\]

The omission is substantive, not cosmetic.  Order-only structures cannot
distinguish two words of the same length with different letters, so they cannot
define regular languages such as the words whose first letter is a fixed
\(a\in\Sigma\).  Consequently the literal host statement is false or, at best,
depends on an unstated convention that the detailed presentation takes care to
make explicit.

**Required repair:** state the word signature in the theorem itself: positions,
one unary predicate \(P_a\) for every \(a\in\Sigma\), and order; then state the
equivalent successor presentation with the same letter predicates and the
definable endpoint/order apparatus.  The source-package qualification in lines
843--850 should remain unchanged.

### 2. A metalinguistic characteristic-column map is presented as though it were literal \(L_1\) syntax

**Location:** `handbook/parts/p09/presentations/n-c-014.tex`, lines 262--266,
268--275, 285--289, and 310--314.

Lines 262--266 give the literal atomic grammar of Elgot's \(L_1\).  Lines
268--275 then define \(c_F(n)\) as the characteristic column of an interpreted
finite-set assignment, and lines 285--289 expressly distinguish a formula, an
assignment, its columns, and the resulting language.  Despite that standing,
lines 310--314 call

\[
 \exists x\,[c_F(x)=a\land c_F(x')=b]
\]

a “local formula.”  The symbol \(c_F\) is not a function symbol in the stated
\(L_1\) grammar.  Without an announced eliminable abbreviation, the display
moves a semantic encoding map into object-language syntax and contradicts the
standing distinction made immediately above.

**Required repair:** either replace the display by the literal conjunction of
the atoms \(x\in F_j\), \(x\notin F_j\), \(x'\in F_j\), and
\(x'\notin F_j\) selected by the coordinates of \(a,b\in U_r\), or state before
the display that \(c_F(x)=a\) is exactly that metalinguistic, eliminable
abbreviation.  Its standing as an abbreviation rather than an added
object-language function symbol must be explicit at first syntactic use.

### 3. The same global alphabet notation is silently redefined across the Büchi and Rabin presentations

**Location:** `handbook/parts/p09/presentations/n-c-014.tex`, lines 145--169
and 1178--1190.

The Büchi presentation fixes

\[
 \Sigma_n=\{\bot,\top\}^n
\]

as its finite-word alphabet and uses that notation through the word-encoding
and regularity discussion.  The Rabin presentation later assigns the same
symbol anew by

\[
 \Sigma_n=\{0,1\}^n
\]

for formula-track labels.  No equality between the source-specific truth-value
alphabet and the bit alphabet is declared, and no source qualifier delimits the
second use.  This is especially undesirable in a presentation that otherwise
preserves source notation and repeatedly warns against silently identifying
different source objects.

**Required repair:** give the Rabin track alphabet a distinct notation, such as
\(\Gamma_n=\{0,1\}^n\), and update line 1190 and its immediately dependent
uses, or source-qualify both alphabet families and state any intended
identification explicitly.  A silent second definition of \(\Sigma_n\) does
not meet the stated stable-notation standard.

## Findings by audit dimension

- **Definition-before-use and exact standing:** REJECT because of Finding 2.
  Apart from that defect, the presentation carefully distinguishes formulas,
  assignments, runs, behaviors, relations, automata, finite witnesses, and
  handbook-owned corrections.
- **Stable and disambiguated notation:** REJECT because of Finding 3.  The
  explicit distinctions between \(A\)-operator and input alphabet, Rabin's
  \(\Lambda\) and Thomas's \(\epsilon\), ordinary and dual acceptance, and the
  two meanings of \(S_0\) are otherwise effective.
- **Graduate-reference completeness and logical sequence:** REJECT because the
  public host theorem lacks the letter-predicate signature required for its
  correctness.  The long presentation itself gives substantial definition,
  theorem, counterexample, proof-architecture, and boundary coverage.
- **Source versus handbook ownership:** no additional must-fix found.  The
  Büchi analysis repair, Elgot unary-window completion, Trakhtenbrot
  counterexamples and edge cases, Rabin zero-length and empty-witness repairs,
  and Thomas deadlock and empty-chain completions are identified as
  handbook-owned rather than projected into the historical texts.
- **Citations and version boundaries:** no additional must-fix found.  The
  1959 Büchi report and 1996 Thomas report remain explicitly precursor-only;
  Elgot's article, report, and errata are separated; the two Trakhtenbrot
  bodies retain distinct standings; Rabin's historical complexity claim and
  Meyer's later correction are separated; and the bibliography entries support
  the cited identities and locators.
- **Local technical-name rule:** no additional hypothetical technical object
  was found.  In particular, the presentation gives local definitions,
  standings, distinctions, and uses for the terms whose precision matters most,
  including portions, residual stream operators, general solutions,
  frontiered finite trees, dual types, finite table-runs, the order-vector with
  hit, and regular generated trees.  Finding 2 remains a standing failure even
  though it concerns notation rather than a newly named mathematical species.
- **Host consistency:** the S2S host statement agrees with the later Rabin and
  Thomas constructions.  The finite-word host statement does not become
  publication-ready until Finding 1 is repaired.

## Disposition

The three findings above are local text repairs; they do not require a source
revisit, a manuscript render, a build, a new abstraction, or a new technical
name.  They do, however, affect the literal correctness, standing, and notation
of the publication text.  Because ACCEPT requires no must-fix publication-text
defect, this snapshot is rejected and no admission record should be added.

REGISTER STATUS: OPEN
