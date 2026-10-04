# N-c-015 integrated source-fidelity review R2

VERDICT: ACCEPT

## Decision

The complete presentation at `handbook/parts/p09/presentations/n-c-015.tex`
is acceptable at its expressly bounded source strength.  I found no
line-specific must-fix in the presentation or in its integration with
`handbook/parts/p09/logic-in-computer-science.tex` lines 877--944.  The
presentation accurately separates the acquired 18 November 2008 TATA release
from the register's evolving-work date, finite bottom-up tree automata from
Rabin's infinite-tree construction, TATA's detailed reconstruction from the
unavailable Thatcher--Wright body, and source material from the two identified
handbook-owned arguments.

The Thatcher--Wright article body remains an open source-register obligation.
That obligation does not require rejection here because lines 147--158 make no
body-dependent technical claim and lines 160--166 expressly preserve the
boundary.

## Materials actually read

1. `handbook/parts/p09/presentations/n-c-015.tex`, lines 1--166, read
   consecutively from line 1 through EOF.
2. `handbook/parts/p09/logic-in-computer-science.tex`, lines 877--944.
3. `spec/research/p09-tata-2008-source-note.md`, lines 1--203.
4. `spec/research/p09-thatcher-wright-1968-acquisition-note.md`, lines 1--96.
5. `spec/research/p09-source-presentations-lot2-3.md`, only lines 751--775.
6. `handbook/bib/handbook.bib`, only the relevant entries
   `ComonEtAl2007` at lines 5883--5889 and `ThatcherWright1968` at lines
   6041--6050.
7. The repository technical-name rule supplied in the task-scoped AGENTS
   instructions.  No additional AGENTS file supplied substantive evidence.

The admission/review-history statements embedded in the otherwise permitted
TATA note and compact record were not used as evidence for this verdict.

## Presentation review, line by line of substantive content

### Identity, edition, and finite-input boundary (lines 6--10)

- The fixed object is correctly identified as the online monograph release of
  18 November 2008.  The explanation that the register's 2007 date concerns
  the evolving work prevents a false claim of a distinct fixed 2007 edition.
  The `ComonEtAl2007` bibliography key is therefore only a stable key; its
  entry correctly records year 2008 and the release date.
- The finite-tree scope and exclusion of infinite-tree automata are supported
  by the permitted TATA note's account of printed pp. 11--13.  The concluding
  contrast with an entire infinite labelled tree is an accurate scope
  consequence, not an attribution of Rabin's construction to TATA.
- The locator `pp. 11--13` and source key are fit for the claim made.

### Ranked terms, automata, runs, and notation map (lines 12--32)

- The ranked-alphabet and ground-term clauses correctly describe finite
  ordered ranked trees.  Nullary symbols supply leaves, and the recursive
  constructor respects the symbol's arity.
- The source tuple is given in the literal TATA order
  `\(\mathcal A=(Q,F,Q_f,\Delta)\)`.  The ranked alphabet, state set, final
  states, transition rules, nondeterministic multiplicity, bottom-up run, and
  accepting-root condition agree with the permitted source record.
- `recognizable` is given an eliminable definition: a language has that
  property exactly when some such automaton accepts precisely its members.
  Its standing is therefore a property of tree languages, not a new kind of
  motive or an unexplained object.
- Lines 29--32 explicitly and correctly map TATA's `F`, `T(F)`, `Q_f`, and
  tuple order to the host's `\Sigma`, `T_\Sigma`, `F`, and tuple order.  This
  disarms the otherwise serious collision between TATA's alphabet symbol `F`
  and the handbook's final-state symbol `F`.
- The `\S1.1` locator covers the definitions actually invoked.

### Handbook-owned accepting run (lines 34--39)

- With exactly the displayed rules, the stated assignment to `a`, `b`, and
  `f(a,b)` is licensed and accepting.  Removing the only displayed binary
  rule leaves the term without a run.  The example therefore demonstrates the
  finite-root acceptance condition without importing infinite-path behaviour.
- Line 164 later identifies the small run as handbook-owned, so it is not
  passed off as a source example.

### Determinization, closure, and emptiness (lines 41--49)

- Theorem 1.1.9 is reported at the supported strength: same recognized
  language, reachable subset states, and uniqueness of a target for each
  symbol/child-state tuple.
- Theorem 1.3.1 is accurately limited to effective union, complement, and
  intersection closure.
- The upward marking account includes both essential halves of the emptiness
  criterion: seed states come from nullary rules, and a language is nonempty
  exactly when a final state is marked.  Theorem 1.7.4 is accurately described
  as supplying a linear-time implementation in the automaton representation.
- The chapter-level locator is adequate because each numbered theorem is also
  named.  Lines 160--166 later prevent these summaries from being mistaken for
  reproductions of every printed construction or proof.

### WSkS domain, variables, and restricted atoms (lines 51--64)

- The word domain, empty word, successor action, first-order range, and finite
  set-variable range agree with the source record for WSkS.
- Proposition 3.3.1 is reported with the exact four supported atomic forms.
  `\operatorname{Sing}(X)`, `X=Yi`, and the eliminable abbreviation
  `X=\{\epsilon\}` are all defined where introduced; no undefined primitive is
  silently created.
- The statement that the translation removes first-order variables without
  changing the represented assignments is exactly the role of the singleton
  translation and does not strengthen it into a new decision theorem.

### Tuple encoding and the worked source example (lines 66--75)

- The three coordinate values have the correct meanings: membership,
  strict-prefix continuation without membership, and absence from that track's
  remaining support.  The arity convention distinguishes every vector with a
  `0` or `1` coordinate from the all-bottom nullary vector.
- Every listed label in Example 3.3.3 follows from the three displayed sets:
  the root, positions `1` and `2`, positions `11` and `22`, and remaining
  nullary padding are all accounted for.  The manuscript neither changes the
  example nor attributes invented labels to it.
- This is source-controlled example material, distinct from the handbook-owned
  run at lines 34--39.

### Bridge from the WSkS coding to finite-tree MSO (lines 77--89)

- The choice of a branching bound at least the maximum source-symbol arity is
  sufficient for the position coding.
- The finite domain `D`, its label subsets `X_f`, the source arity clauses, the
  translations of label and child atoms, and the restrictions of element and
  set quantifiers together state the needed finite-tree interpretation rather
  than merely asserting an unexplained equivalence.
- The converse state-position sets are restricted to and partition the same
  represented finite domain.  Accordingly, the ambient successor tree is
  correctly identified as a coding domain for a finite input, not as the
  automaton's infinite input.
- The `pp. 89--95` locator is consistent with the permitted source note's
  account of the controlling Section 3.3 passage.

### Formula-to-automaton direction (lines 91--102)

- The six displayed transitions are exactly the one-state binary-track cases
  compatible with `X\subseteq Y`: `\bot\bot`, `00`, `01`, `11`, `\bot0`, and
  `\bot1`.  The nullary/binary arities are consistent with the encoding
  convention already stated.
- The disjunction construction does not silently unite mismatched alphabets:
  it first adds unconstrained tracks for variables absent from the opposite
  disjunct.  Negation and existential set quantification are then correctly
  tied to complement and projection.
- The claim is limited to the construction of Lemma 3.3.4 and does not claim
  that every source transition table has been copied.

### Automaton-to-formula direction (lines 104--116)

- The state sets `Y_q`, their partition requirement, and the final-state root
  disjunction are the supported ingredients of Lemma 3.3.6.
- The displayed local clause has the correct direction: a node bearing symbol
  `f` and state `q` must have child-state labels matching at least one
  transition into `q`.  Its conjunction over every symbol and state, together
  with the partition and final-root conditions, describes an accepting
  bottom-up run.
- The `\S3.3` locator and explicit lemma number make the ownership and source
  location clear.

### Exact slogan boundary and closed-sentence decision (lines 118--124)

- The manuscript preserves TATA's qualification that Theorem 3.3.7 is a
  convenient but “not very precise” slogan and identifies Lemmas 3.3.4 and
  3.3.6 as the precise directions.  It therefore does not cite the slogan as a
  stronger theorem than the source supports.
- Theorem 3.3.8's closed-sentence reduction uses the supported empty-track
  alphabet convention, including the source's optional sole nullary symbol
  `\top`.  The final transition criterion `\top\to q_f` is stated, and the
  manuscript avoids the unsupported all-zero-track reconstruction.
- The link to the host theorem is therefore constructive and explicitly
  bounded.

### Copying-language counterexample (lines 126--135)

- The exact alphabet hypothesis `F=\{a^{(0)},f^{(2)}\}` and the exact exercise
  language are retained.
- The supplied proof is valid.  Determinization permits a deterministic
  recognizer; acceptance of every `f(t,t)` forces every ground term `t` to
  reach a state; two distinct terms sharing a state would make `f(t,t)` and
  `f(t,u)` reach the same root state; infinitely many terms therefore require
  infinitely many states.
- Lines 164--166 explicitly call this proof handbook-owned and distinguish it
  from the source's exercise statement.  There is no false proof attribution.

### Weak/full and finite/infinite boundary (lines 137--145)

- Full SkS is introduced only with the supported distinction that set
  variables may denote arbitrary, possibly infinite subsets of the infinite
  successor tree.
- The root-down infinite-input automata and different complementation argument
  are attributed only at the level stated in the permitted TATA record.
- The equality of weak and full ranges on an actually finite domain is an
  elementary finite-set consequence.  The next sentence correctly prevents
  that observation from being used to identify finite bottom-up automata with
  Rabin automata on an entire infinite tree.

### Thatcher--Wright boundary (lines 147--158)

- The article identity and bounded abstract-level scope agree with the
  acquisition note and the `ThatcherWright1968` bibliography entry.
- The paragraph reports “finite algebras” only as language of the authoritative
  abstract.  It does not define the paper's algebra, recognizability relation,
  signature, logic, examples, theorem statements, or proof from later TATA
  notation.
- The same-title 1966 report is labelled only a bibliographic lead.  No
  precursor-strength technical inference is made from its unavailable body.
- This is the correct treatment of the open source-register obligation under
  the technical-name rule: the owed artifact is described, but no hypothetical
  construction is named in advance.

### Reconstruction and ownership boundary (lines 160--166)

- The positive scope exactly matches what the presentation actually provides:
  finite-tree objects and operative determinization, closure, emptiness,
  coding, and accepting-run descriptions.
- The negative scope prevents “operative reconstruction” from being read as a
  claim to reproduce every transition table or complete proof of Theorems
  1.1.9, 1.3.1, and 1.7.4.
- The small accepting run and copying-language proof are expressly assigned to
  the handbook; TATA's printed material and the unavailable Thatcher--Wright
  body remain separately attributed.

## Host integration review, lines 877--944

### Rabin context and separation (lines 877--882)

The S2S theorem is host context rather than a claim sourced to either N-c-015
source.  Within the permitted evidence, the relevant integration fact is that
it is explicitly about the full infinite binary successor tree and Rabin's
construction.  The N-c-015 definition and theorem repeatedly distinguish
their finite inputs from this object.  No TATA or Thatcher--Wright ownership is
improperly attached to lines 877--882.

### Finite ranked-tree definition (lines 884--913)

- The host's `\Sigma_n`, `T_\Sigma`, nullary-leaf, transition, run, root-final,
  and recognized-language clauses agree with the presentation's source
  reconstruction.
- The subject is explicitly a finite ranked alphabet.  The disjoint
  arity-indexed presentation gives the standing of `\Sigma` and every
  `\Sigma_n`; the recursive least-set clause gives the standing of
  `T_\Sigma`.
- The host tuple order `(Q,\Sigma,\Delta,F)` differs from TATA's order, but
  presentation lines 29--32 state the exact symbol and order conversion.  No
  source notation is silently rewritten.
- Lines 907--911 supply the necessity and nonredundancy of the introduced
  finite-tree notions: they are not word automata or infinite Rabin runs, and
  the distinction is used immediately in the next theorem.

### Finite-tree MSO theorem and algorithms (lines 915--934)

- The signature is fully stated with unary label predicates and indexed child
  relations.  The equivalence between recognizable finite-tree languages and
  MSO-definable languages is exactly the correspondence reconstructed in
  presentation lines 77--124.
- Weak/full set-variable ranges are correctly separated before the
  finite-domain coincidence is taken.  The host explicitly refuses to export
  that coincidence to the infinite successor tree.
- Effective subset determinization, Boolean closure, and upward reachable-state
  emptiness match presentation lines 41--49.  Membership decidability also
  follows directly from the finite input, finite states, and local transition
  definition: the possible states at each node can be computed bottom-up.
- The consequence at lines 929--931 is expressly conditional on an effective
  reduction to the listed operations and emptiness; it does not claim that
  every finite-tree property is thereby decidable.
- Line 932's TATA citation supports the finite-tree clauses, while line 933
  again excludes Rabin's infinite-tree construction.

### Placement (lines 936--944)

The two earlier-figure references make no N-c-015 source attribution.  The
presentation is included after the finite-tree definition and theorem, so its
notation map and detailed source route have the definitions they reference and
do not precede the host concepts they explain.

## Attribution, locator, bibliography, and ownership result

- `ComonEtAl2007` names the correct eight authors, title, 2008 release year,
  18 November release note, and authoritative HAL record.  The stable key's
  apparent year mismatch is explained in presentation lines 6--8.
- `ThatcherWright1968` gives the correct authors, title, journal, volume, issue,
  pages 57--81, year, and DOI.
- The presentation uses section, chapter, page, theorem, lemma, proposition,
  example, figure, and exercise locators at the strength needed to distinguish
  definitions, constructions, examples, and boundaries.
- Source ownership is never transferred between TATA and Thatcher--Wright.
  Handbook ownership is explicit for the small run and the Exercise 1.4 proof.
- The missing Thatcher--Wright body is neither concealed nor treated as an
  automatic failure of the bounded TATA presentation.

## Technical-name rule

No technical name in the reviewed passage violates the repository rule.

- `finite ranked alphabet`, `finite tree`, and `bottom-up tree automaton` are
  needed to distinguish these objects from words and infinite Rabin runs; they
  receive exact host definitions, clear mathematical standing, and immediate
  theorem use.
- `recognizable` is eliminably defined as existential acceptance by such an
  automaton and is later used in the correspondence and counterexample.
- `WSkS`, `Sing`, and `full SkS` are source terms or eliminable notation whose
  domains and semantic distinctions are stated where they enter the argument.
- The unavailable Thatcher--Wright construction receives no invented name.
  The manuscript instead records exactly which source-controlled artifacts
  remain owed.

## Prohibitions observed

- I did not open or use any earlier or parallel integrated N-c-015 report,
  including any R1 or R2 report.
- I did not open or use
  `spec/research/p09-tata-2008-independent-review-record.md`, anything under
  `spec/research/boards/p09-tata-2008/`, or any other review/admission history.
- I did not ask, list, or message any other agent.
- I did not inspect a manuscript PDF, manuscript render, PDF page, PNG, page
  image, or other rendered manuscript evidence.
- I did not run a LaTeX build, test, test harness, checker, repository script,
  automated validator, or hash operation.
- I did not consult an original historical source page because the permitted
  textual source records resolved the source questions needed for this review.
- I made no manuscript, host, note, ledger, bibliography, or collateral edit.
  The only created file is this review report.

REGISTER STATUS: OPEN
