# N-c-015 integrated source review — blind Round 1

## Verdict

VERDICT: REJECT

The integrated presentation is source-bounded correctly in almost every respect, including its refusal to reconstruct the unavailable Thatcher--Wright body.  One line-specific must-fix remains in the TATA construction: the manuscript defines WSkS for arbitrary branching degree (k\geq1), says that every active track symbol has arity (k), and then prints a two-child inclusion automaton without stating that this display is the (k=2) instance.  The displayed rules are not typed for arbitrary (k).  Acceptance therefore requires one local qualification or arity-generalization.

This rejection is limited to that exact manuscript defect.  It does not treat the honestly bounded Thatcher--Wright acquisition obligation as a manuscript error, and it does not reject the remaining TATA reconstruction.

## Evidence examined

I read the following permitted evidence directly:

- `handbook/parts/p09/presentations/n-c-015.tex`, lines 1--160, completely from line 1 through EOF;
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 877--944;
- `spec/research/p09-tata-2008-source-note.md`, completely;
- `spec/research/p09-thatcher-wright-1968-acquisition-note.md`, completely;
- the compact `N-c-015` portion of `spec/research/p09-source-presentations-lot2-3.md`, lines 751--775; and
- the `ComonEtAl2007` and `ThatcherWright1968` entries in `handbook/bib/handbook.bib`.

The actual LaTeX, rather than a record summary, controlled the verdict.  Review or admission-history prose embedded in the permitted notes and compact record was outside the evidentiary basis for this decision.

## Prohibitions observed

- I did not open or use the TATA independent-review record, anything under the TATA board directory, or any earlier or parallel integrated `N-c-015` report.
- I did not ask, list, or message another agent.
- I did not open, inspect, render, or use a manuscript PDF, a PDF page, a PNG, a page image, or a render as manuscript evidence.
- I did not run LaTeX, a build, a test, a test harness, a checker, a repository script, an automated validator, or a hash operation.
- The must-fix is visible from the internal types in the actual LaTeX and the permitted notes; no original historical-source page was needed.
- I changed no manuscript, host, note, ledger, bibliography, prior report, or other repository file.

## Must-fix finding

### 1. `n-c-015.tex:85--91` silently specializes the inclusion automaton to (k=2)

The manuscript establishes the general setting at lines 49--52:

- (k\geq1);
- the underlying successor domain is \(\{1,\ldots,k\}^{*}\); and
- the construction is presented as WSkS for that arbitrary (k).

It then fixes the rank of every encoding symbol at lines 62--66: a symbol containing a (0) or (1) has arity (k), while the all-(\bot) symbol is nullary.  Consequently, for the two-track alphabet used by the atomic formula (X\subseteq Y), a transition on `00`, `01`, `11`, `\bot0`, or `\bot1` must have (k) child-state arguments.

Lines 85--91 instead say, without a local specialization, that the atomic construction for (X\subseteq Y) has the rules

\[
 \bot\bot\to q,\quad 00(q,q)\to q,\quad 01(q,q)\to q,\quad
 11(q,q)\to q,\quad \bot0(q,q)\to q,\quad \bot1(q,q)\to q.
\]

Those active-symbol rules have exactly two child arguments and hence are well-typed only when (k=2).  The phrase “with (k=2)” at lines 66--67 modifies the preceding source Example 3.3.3; it does not declare that the later Lemma 3.3.4 paragraph has abandoned the general (k\geq1) scope, especially after lines 73--83 return to the general finite-tree/MSO bridge.

The permitted TATA note identifies this display as Figure 3.9's exact one-state transition list, so the list itself need not be changed if the intended role is a binary illustration.  The minimum source-faithful repair is either:

1. state at line 85 that the displayed atomic automaton is the (k=2) instance; or
2. retain arbitrary (k) and replace each pair `(q,q)` by a (k)-tuple of copies of (q).

The missing qualification is substantive rather than typographical because the ranked arity determines whether a transition is even a rule over the stated alphabet.  It is therefore a must-fix under the repository's definition-before-use and exact-standing discipline.

## Claims that pass at the bounded source strength

### TATA identity and finite/infinite boundary

`n-c-015.tex:6--10` correctly identifies the controlling object as the 18 November 2008 online-monograph release, explains the stable 2007 register label without treating it as the inspected fixed edition's date, and confines TATA to finite trees.  The `ComonEtAl2007` bibliography key retains 2008 as the bibliographic year and identifies the release date in its note.  No TATA construction is projected onto Rabin's infinite-tree automata.

### Ranked trees, automata, and algorithms

Lines 12--30 correctly define ranked ground terms, TATA's bottom-up automaton tuple, nondeterministic transitions, runs, root acceptance, recognizability, and the literal map from TATA's symbols and tuple order to the host definition.  Lines 32--37 give a small finite run and contrast it with infinite-path recurrence; lines 154--160 explicitly own that run as a handbook example.

Lines 39--47 accurately bound determinization, Boolean closure, the bottom-up accessible-state emptiness procedure, and the linear implementation to the cited Chapter 1 results.  The host at `logic-in-computer-science.tex:884--934` gives compatible finite-term and bottom-up-run definitions, states the same effective consequences, and expressly distinguishes them from the `S2S` construction at lines 877--882.

### WSkS encoding and both logical directions

Apart from the missing (k=2) qualification in the displayed atomic example, lines 49--60 correctly state WSkS's word domain, successor operations, finite-set range, singleton-set elimination, and restricted atomic syntax.  Lines 62--83 accurately describe the finite tuple-of-sets encoding, work the source's (k=2) example, and type the bridge between finite-tree label/child predicates and the ambient successor-tree coding without replacing the finite input by an infinite tree.

Lines 93--110 correctly assign disjunction, negation, and existential projection to their automata operations and give the converse state-partition/final-root/local-transition description.  Lines 112--118 preserve TATA's warning that Theorem 3.3.7 is an imprecise slogan, locate the precise directions in Lemmas 3.3.4 and 3.3.6, and give the source's empty-track/single-nullary-`\top` closed-sentence reduction.  These details support the host's exact finite-tree MSO correspondence rather than merely repeating the slogan.

### Nonrecognizable copying language

Lines 120--129 retain the exact ranked alphabet from Exercise 1.4 and supply a valid handbook-owned deterministic-state separation proof.  The proof includes the otherwise necessary reachability premise: every (t) must acquire a state because (f(t,t)) must be accepted.  It does not attribute the proof to the exercise text.

### Full SkS and Thatcher--Wright boundaries

Lines 131--139 distinguish full SkS's arbitrary subsets and root-down infinite-input method from WSkS and from finite bottom-up automata.  They also state correctly that weak and full monadic quantification coincide on an actually finite domain without collapsing the different ambient infinite-tree theories.

Lines 141--152 stay within the authoritative Thatcher--Wright abstract and metadata.  They report “finite algebras” only as source language, deny it the standing of a handbook definition, enumerate the unavailable body-dependent objects that are not reconstructed, and keep RC-1713 at bibliographic-lead strength.  This satisfies the repository technical-name rule: the presentation describes the owed artifacts instead of inventing an algebraic signature, recognition relation, logical fragment, or modern ranked-tree identification.  The bibliography's authors, title, journal, volume, issue, pages 57--81, year, and DOI agree with the acquisition note.

### Remaining technical names

The presentation's other technical terms satisfy the local rule.  “Finite ranked alphabet,” “ground term,” bottom-up automaton, run, and “recognizable” receive definitions, standings, finite/infinite distinctions, and later uses at lines 12--47.  WSkS receives its domain and variable ranges before its syntax and constructions at lines 49--60.  Full SkS is introduced only with its altered set range, different automaton direction, nonredundancy from WSkS, and boundary use at lines 131--139.  The host's finite-ranked-tree definition likewise states necessity, definition, standing, nonredundancy, and use together at `logic-in-computer-science.tex:884--934`.

## Open source-register obligation

The complete Thatcher--Wright 1968 body, or an authoritative copy of the 1966 RC-1713 precursor followed by final-article reconciliation, remains to be acquired.  Until then, its finite-algebra signature, recognizability relation, input domain and coding, closure and generalized Kleene theorems, exact second-order language and variable ranges, examples, and proofs remain open.  The actual manuscript states this boundary honestly, so the missing body is not an additional must-fix and is not the reason for the rejection.

REGISTER STATUS: OPEN
