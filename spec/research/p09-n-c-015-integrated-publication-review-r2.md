# N-c-015 integrated publication and terminology review, round 2

VERDICT: ACCEPT

## Decision

The complete current presentation at `handbook/parts/p09/presentations/n-c-015.tex`,
lines 1--166, is acceptable as graduate-reference prose at the explicitly
bounded source strength. I found no line-specific must-fix in the presentation
or its integration at `handbook/parts/p09/logic-in-computer-science.tex`, lines
877--944.

This verdict does not close the source register. The technical body of
Thatcher--Wright 1968 remains unavailable, and the presentation correctly
treats its acquisition and source-controlled reconstruction as an open
obligation rather than silently filling the gap from TATA or modern notation.

## Definition, notation, and logical-order audit

1. **Finite objects and automata are defined before use.** Lines 12--16 define
   the finite ranked alphabet, `T(F)`, ground terms, and their finite ordered
   tree reading. Lines 17--28 then give the complete standing of the source
   tuple \(\mathcal A=(Q,F,Q_f,\Delta)\), its state set, final-state set,
   transition relation, runs, acceptance, and recognizability. The example at
   lines 34--39 therefore uses no undeclared automaton component.

2. **The source and host notations are kept distinct and mapped exactly.**
   Lines 29--32 explicitly identify TATA's alphabet \(F\) with the handbook's
   \(\Sigma\), TATA's \(T(F)\) with \(T_\Sigma\), and TATA's \(Q_f\) with the
   handbook's final-state set \(F\), while also recording the different tuple
   order. This is compatible with the host definition at lines 884--913,
   especially the host tuple \((Q,\Sigma,\Delta,F)\) at lines 895--901. The
   repetition is nonredundant: the host gives the handbook definition, whereas
   the presentation records and translates the source's literal notation.

3. **The operative automata results follow the automaton definition.** Lines
   41--49 state determinization, Boolean closure, and the upward reachability
   criterion for emptiness only after runs and acceptance have been fixed. The
   determinism gloss, reachable-subset statement, and final-state marking
   criterion have the required object and type standing.

4. **WSkS and its source syntax are introduced before the coding uses them.**
   Lines 51--64 fix \(k\), \(\epsilon\), the word domain, first-order and set
   variable ranges, successor behavior, the restricted atoms, and the meanings
   of \(\operatorname{Sing}(X)\), \(X=Yi\), and the eliminable source
   abbreviation \(X=\epsilon\). In particular, the visually type-mixed atom
   \(X=\epsilon\) is not left primitive or ambiguous: lines 62--63 eliminate it
   as \(X=\{\epsilon\}\).

5. **The finite-set encoding is ordered from data to logic.** Lines 66--75
   define the track alphabet, coordinate meanings, ranks, and the worked source
   example. Lines 77--89 then introduce the finite tree domain \(D\), the label
   sets \(X_f\subseteq D\), the translations of label and child atoms, and the
   restrictions on element and set quantifiers. Thus the ambient successor tree
   is not allowed to change standing from coding structure to automaton input.

6. **Both logical directions and the decision step have enough local
   information.** Lines 91--103 give the atomic inclusion automaton and the
   disjunction, negation, and projection operations. Lines 104--116 give the
   converse state-set partition, final-root condition, and local transition
   clause. Lines 118--124 preserve TATA's qualification of the slogan theorem
   and state the closed-sentence convention and final-transition test. This is
   sufficient for the constructive outline claimed at lines 160--166; the text
   does not claim to reproduce every source transition table or proof.

7. **The counterexample and the finite/infinite boundary occur after the
   positive theory.** Lines 126--135 state the exact ranked alphabet and supply
   a complete deterministic-state separation argument, including the otherwise
   easy-to-omit premise that every \(t\) must reach a state. Lines 137--145 then
   define full SkS by its arbitrary-set range and distinguish its root-down
   infinite-input automata from the finite bottom-up automata already defined.
   The host makes the same distinction at lines 915--934 and does not conflate
   it with Rabin's S2S theorem at lines 877--882.

## Terminology audit under `AGENTS.md`

No hypothetical primitive or newly coined construction is introduced. The
technical names used are source terms or standard descriptive names whose
standing is supplied where they enter:

- finite ranked alphabets, finite ordered ranked trees, automata, runs, and
  recognizable languages are defined at lines 12--28 and used throughout;
- WSkS is identified as a logic over a typed word domain with explicit variable
  ranges at lines 51--55, and its distinction from full SkS is used at lines
  137--145;
- the encoded domain \(D\), label sets \(X_f\), and state sets \(Y_q\) are
  introduced as sets of positions before their formulas use them at lines
  77--87 and 104--115;
- the host itself states the necessity and nonredundancy of the finite ranked
  tree and bottom-up-run definitions at lines 907--910 and immediately uses
  them in the theorem at lines 915--934.

The presentation therefore does not name a speculative answer in place of an
owed artifact. The only owed artifact is the Thatcher--Wright source visit, and
lines 147--158 describe that obligation without inventing a name, signature,
relation, or theorem for the missing construction.

## Reader sufficiency and sentence-level clarity

The exposition moves in a usable graduate-reference order: edition and domain
boundary (lines 6--10), objects and automata (12--39), constructions (41--49),
logic and coding (51--89), the two translations and decision consequence
(91--124), limitation and counterexample (126--145), then historical and
reconstruction boundaries (147--166). Sentences identify the subject of each
operation and keep source theorem numbers attached to their operative content.
The small run at lines 34--39 provides a concrete acceptance/non-run contrast;
the encoding at lines 66--75 and inclusion automaton at lines 91--102 prevent
the logical correspondence from remaining merely schematic.

I found no undefined symbol, unresolved pronoun, misleading tuple order, or
sentence-level ambiguity that changes the mathematical claim. In particular,
the local transition metavariable \(s\) at lines 111--112 is determined by the
arity of the displayed symbol \(f\), whose ranked standing was fixed at lines
12--16 and 77--82; it does not create a new untyped object.

## Citation, ownership, and source/version boundaries

- Lines 6--10 identify the actual controlling TATA release as 18 November 2008,
  explain the register's 2007 label, cite the finite-tree scope, and explicitly
  exclude infinite-tree automata. The `ComonEtAl2007` bibliography key remains a
  stable identifier, but its actual entry records year 2008, the 18 November
  release, and the HAL record.
- Source theorem, proposition, lemma, example, figure, exercise, and section
  numbers are used as source locators rather than recast as handbook theorem
  labels. The citations at lines 9, 27, 48, 89, and 116 bound the corresponding
  source-dependent passages.
- Lines 118--124 do not strengthen TATA's qualified Theorem 3.3.7 slogan beyond
  the two coded directions, and they state the source's empty-alphabet or
  nullary-\(\top\) convention rather than substituting an all-zero-track claim.
- Lines 147--158 attribute only abstract-level claims to Thatcher--Wright 1968,
  list the body-dependent material that is not reconstructed, separate TATA's
  modern presentation from the older paper, and keep the 1966 report at
  bibliographic-lead strength. The `ThatcherWright1968` bibliography entry has
  the matching authors, title, journal, volume, issue, corrected pages 57--81,
  year, and DOI.
- Lines 160--166 explicitly delimit the reconstruction and identify the small
  accepting run and Exercise 1.4 proof as handbook-owned. Those statements
  prevent the local proof and example from being misattributed to either cited
  source.

## Host compatibility

The host first distinguishes Rabin's full infinite binary tree at lines
877--882, then defines finite ranked trees and finite bottom-up automata at lines
884--913, states the finite-tree automata/MSO theorem at lines 915--934, and
only then inputs this source presentation at line 943. The source presentation
therefore elaborates already declared handbook objects without changing their
meaning. Its finite-domain weak/full coincidence agrees with host lines
920--925, and its repeated warning against identifying finite bottom-up runs
with Rabin runs agrees with host lines 932--933. No host symbol is silently
retyped.

## Remaining open source obligation

The Thatcher--Wright article body is still not acquired. The permitted
acquisition record supports only identity, metadata, abstract-level scope, and
the existence of the same-title 1966 report as a lead. The current manuscript
does not exceed that evidence. Acquisition of the complete journal body, or of
the report at explicitly precursor strength followed by reconciliation against
the journal article, remains required before adding any body-dependent
definition, theorem, proof, example, or technical name. This open register item
does not force rejection of the present text because lines 147--158 state the
boundary honestly and lines 160--166 keep the modern reconstruction separately
owned.

## Evidence and method record

Files and portions read:

1. `handbook/parts/p09/presentations/n-c-015.tex`, lines 1--166, from line 1
   through EOF.
2. `handbook/parts/p09/logic-in-computer-science.tex`, lines 877--944 only.
3. `spec/research/p09-tata-2008-source-note.md`, lines 1--203. Only its source
   identity, source-content, reconstruction-boundary, and acquisition-boundary
   evidence was used; its internal review/admission-history assertions were not
   used in reaching this blind verdict.
4. `spec/research/p09-thatcher-wright-1968-acquisition-note.md`, lines 1--96.
5. `spec/research/p09-source-presentations-lot2-3.md`, lines 751--775 only. A
   preliminary count exposed only the file's total line count; no text outside
   lines 751--775 was displayed or used.
6. `handbook/bib/handbook.bib`, the `ComonEtAl2007` entry at lines 5883--5889
   and the `ThatcherWright1968` entry at lines 6041--6050 only.

Prohibitions observed:

- no prior or parallel integrated N-c-015 report was opened or used;
- no independent review record, board material, decision ledger, or other
  review/admission history was opened or used;
- no other agent was asked, listed, messaged, or consulted;
- no manuscript PDF, source PDF, render, PNG, page image, or visual layout
  evidence was opened or used;
- no LaTeX build, test, test harness, checker, repository script, automated
  validator, or manuscript render was run;
- no hash was computed, compared, or used as evidence; pre-existing hash text
  incidentally present in the permitted notes was disregarded; and
- no original historical source page or web source was needed or consulted.

Layout is outside this verdict.

REGISTER STATUS: OPEN
