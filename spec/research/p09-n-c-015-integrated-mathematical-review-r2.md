# N-c-015 integrated mathematical and definedness review, round 2

VERDICT: ACCEPT

## Review scope and standard

This is a fresh, blind, text-only review of the complete current presentation
`handbook/parts/p09/presentations/n-c-015.tex`, lines 1--166, together with its
actual host at `handbook/parts/p09/logic-in-computer-science.tex`, lines
877--944. The verdict concerns the integrated manuscript at its expressly
bounded source strength. It does not close the source-register obligation to
acquire and inspect the Thatcher--Wright body.

ACCEPT means that I found no line-specific mathematical, logical, typedness,
definedness, source-strength, host-consistency, or technical-name must-fix in
the reviewed text. In particular, the presentation gives an operative
construction outline; it does not purport to reproduce every transition table
or every printed proof from TATA.

## Findings

### 1. Finite ranked trees and bottom-up automata are defined before use

- Presentation lines 12--16 define the ranked alphabet, ground-term set
  `T(F)`, the recursive constructor, and the nullary base case before any run
  or language is discussed. The constructor is arity-correct: an `n`-ary
  symbol receives exactly `n` already formed terms.
- Lines 17--32 give the complete source tuple `A=(Q,F,Q_f,Delta)`, type `Q_f`
  as a subset of the finite state set, type transitions by the arity of their
  ranked symbol, define a bottom-up run and root acceptance, define
  recognizability existentially over automata, and explicitly map every
  overloaded TATA symbol to the host notation. The tuple-order difference from
  the host is stated rather than silently normalized.
- Lines 34--39 form a well-typed nullary/binary example. The transitions on
  `a` and `b` provide the two leaf states, the binary transition provides the
  root state, and removing that last transition removes the only run on
  `f(a,b)`. Nothing in the example invokes an infinite path or a Rabin run.
- Host lines 884--913 independently define the same objects in handbook
  notation. Its least-set clause includes the `n=0` case, its automaton tuple
  places `Delta` before the final set `F`, and its run and accepted-language
  definitions agree exactly with the presentation's symbol map.

### 2. Determinization, Boolean closure, membership, and emptiness have the stated strength

- Presentation lines 41--43 state language-preserving effective subset
  determinization and the correct determinism condition: at most one target
  for a fixed ranked symbol and child-state tuple. Restricting the powerset
  carrier to reachable subsets does not weaken language equivalence.
- Lines 43--49 state effective union, complement, and intersection at theorem
  strength. They do not claim that merely flipping final states in an
  arbitrary partial nondeterministic automaton performs complementation; the
  cited closure construction follows determinization and is stated only at the
  strength used later.
- Lines 45--48 give the correct least-reachability emptiness test. Targets of
  nullary transitions form the base marks; a transition target is marked after
  all child states are marked; nonemptiness is equivalent to eventually
  marking a final state. This also handles the case of no usable nullary rule:
  no state is initially marked and the language is empty.
- Host lines 926--932 agree with this account. Membership is a direct finite
  bottom-up computation on the already defined run relation, while emptiness
  is the upward reachability computation. The host does not overidentify these
  effective finite-tree constructions with Rabin's infinite-tree method.

### 3. The WSkS universe, variable sorts, successors, and restricted atoms are bound

- Presentation lines 51--55 bind `k>=1`, define the root word `epsilon`, fix
  the first-order universe `{1,...,k}*`, type the successor operation as
  appending one letter, and distinguish word-valued first-order variables from
  finite-set-valued weak monadic variables.
- Lines 55--64 state the singleton-set replacement before using its restricted
  atom forms. `Sing(X)` is defined, `X=Yi` is explained as the successor
  relation between the unique represented words, and the superficially
  heterogeneous source atom `X=epsilon` is explicitly eliminated as
  `X={epsilon}`. The translation therefore does not leave an untyped equality
  between a set and a word.

### 4. Track coding binds both successor degree and ranked arity

- Lines 66--70 type the encoded object as a finite tree over
  `{0,1,bottom}^n`. At each represented position, coordinate `i` records
  membership, proper-prefix continuation, or absence for `S_i`. Every tuple
  containing `0` or `1` has rank exactly `k`, while the all-bottom tuple is
  nullary. Thus the `k` successors of the WSkS structure and the rank of each
  nonpadding code symbol are the same previously bound `k`; no successor
  degree is left implicit.
- Lines 71--75 correctly instantiate the binary code. The stated root,
  first-level, and occupied second-level labels follow coordinatewise from the
  three sets. Non-bottom member labels at `11` and `22` are binary and hence
  receive all-bottom nullary children, while unused siblings are likewise
  all-bottom leaves. The phrase "every remaining nullary padding position"
  therefore includes all and only the forced unused children.
- The zero-track situation is not smuggled into the positive-track example.
  Lines 121--123 separately give the source's closed-sentence convention: the
  empty track alphabet is represented, under the explicit working convention,
  by the sole nullary symbol `top`.

### 5. The bridge to finite ranked-tree MSO is sorted and arity-safe

- Lines 77--79 choose `k` only after the ranked alphabet `F` is fixed and
  require it to dominate every arity of `F`. Finiteness of `F` makes such a
  bound available; allowing a larger `k` is harmless because the ground-term
  arity clauses select only the child indices licensed by each symbol.
- Lines 79--86 bind the finite position set `D` and each symbol-label set
  `X_f subseteq D`. The source arity clauses ensure that these data describe
  one ground term. Label atoms become `x in X_f`, the `i`-child atom becomes
  `y=xi`, element quantifiers are relativized to `D`, and monadic quantifiers
  are relativized to subsets of `D`. Consequently neither elements nor sets
  leak into the unused portion of the ambient infinite prefix tree.
- Lines 87--89 and 104--116 give the reverse direction on the actual finite
  input domain: the existential state sets partition the encoded finite input,
  not the whole successor universe. This is consistent with the all-bottom
  padding used by the separate tuple code. The ambient prefix tree supplies a
  coding arena; it is not substituted for the finite tree accepted by the
  bottom-up automaton.

### 6. Both logic-to-automaton and automaton-to-logic directions are present

- Lines 91--102 give the formula-to-automaton direction at the promised
  constructive-outline strength. In the displayed `X subseteq Y` automaton,
  the single state is final, `bottom bottom -> q` is the nullary padding rule,
  and the five binary nonpadding rules are exactly the coordinate pairs
  compatible with inclusion: `00`, `01`, `11`, `bottom 0`, and `bottom 1`.
  Together with the nullary rule, the display contains every listed rule and
  omits the violating track combinations. The induction then identifies the
  necessary variable-alphabet extension for disjunction, language union,
  complement for negation, and track projection for existential set
  quantification.
- Lines 104--116 give the automaton-to-formula direction. One finite set
  variable `Y_q` is assigned per state, the sets partition the input positions,
  and a final state must contain the root. For each symbol `f` of arity `s` and
  each proposed parent state `q`, the displayed disjunction ranges precisely
  over transitions `f(q_1,...,q_s)->q`; its conjunction requires child `i` to
  lie in `Y_{q_i}`. The clause is oriented correctly for a bottom-up run.
- The local display is also correct for nullary symbols. When `s=0`, the inner
  conjunction is the true empty conjunction; the outer disjunction is true
  exactly when a nullary transition `f->q` exists, and is false when there is
  none. Thus the display neither assumes children of a leaf nor accepts a leaf
  state unsupported by `Delta`.
- Lines 118--124 explicitly resist promoting TATA's imprecise slogan beyond
  the two coded lemmas. For a closed sentence there is one conventional
  nullary input `top`; it is accepted exactly when some rule `top->q_f` reaches
  a final state. Hence the final validity test is a well-defined finite
  nullary acceptance question, not an all-zero-track surrogate.

### 7. The nonrecognizable copying language proof is complete at its stated scope

- Lines 126--135 fix the exact alphabet before defining the language. The
  language contains `f(t,t)` for every ground term and rejects `f(t,u)` when
  `t` and `u` are distinct.
- Language-preserving determinization justifies considering a deterministic
  recognizer. Every term `t` must acquire a state because an accepting run on
  `f(t,t)` contains a run on each occurrence of `t`. If distinct `t,u` reached
  one state, the same binary transition used at the root of `f(t,t)` would be
  used at the root of `f(t,u)`, giving both the same final root state. This
  contradicts the definition of the language. Since `T(F)` is infinite but
  `Q` is finite, the injectivity forced by recognition is impossible.
- Lines 164--166 correctly identify this proof as handbook-owned rather than
  attributing a printed proof to an exercise source.

### 8. Weak/full and finite/infinite boundaries are not conflated

- Lines 137--145 define full SkS by changing the range of monadic variables to
  arbitrary subsets of the infinite successor tree. They then state the
  corresponding source boundary: root-down runs on infinite inputs and a
  different complementation argument are required there.
- The finite-domain observation is exact: every subset of a finite position
  domain is finite, so weak and full monadic quantification have the same
  assignments on that finite structure. The manuscript immediately denies the
  invalid converse inference that this coincidence turns a finite bottom-up
  automaton into a Rabin automaton on an entire infinite labeled tree.
- Host lines 877--881, 915--934 preserve the same separation. The S2S theorem
  concerns the full infinite binary tree; the finite-tree theorem concerns
  finite ranked terms. The host's weak/full coincidence is asserted only over
  the finite position domain.

### 9. Thatcher--Wright is honestly bounded and remains an open source obligation

- Presentation lines 147--158 use only the authoritative abstract-level
  description available in the permitted acquisition record. "Finite
  algebras" is reported as source language and expressly withheld as a
  handbook definition. The missing algebraic signature, recognition relation,
  logical language, theorem statements, examples, and proofs are not filled in
  from TATA's later tuple or WSkS construction.
- The 1966 same-title report is marked only as an acquisition lead. No claim in
  the finite-tree theorem depends on that uninspected body.
- Lines 160--166 accurately delimit the reconstruction: the operative finite
  constructions are stated, the three cited chapter-one results are not
  represented as fully reprinted proofs, and handbook-owned arguments are
  distinguished from source-owned material.
- The missing Thatcher--Wright body therefore keeps the register open, but it
  is not a mathematical rejection of a manuscript that states that limitation
  explicitly and does not use the missing body to support its theorem.

### 10. Host consistency and technical-name discipline

- The presentation's `F`, `Q_f`, and tuple order are mapped to the host's
  `Sigma`, `F`, and tuple order at lines 29--32. The two texts agree on finite
  terms, root acceptance, recognizable/recognized languages, effective
  determinization, Boolean closure, and nullary-upward emptiness.
- The host theorem's signature description at lines 915--925 is exactly the
  finite structure used by the presentation's `D`, `X_f`, and child-successor
  translation. Its strength is neither weaker nor stronger than the two
  directions reconstructed in the presentation.
- The text introduces no hypothetical technical answer. Source-standard names
  are either already defined in the host or introduced with an eliminable
  definition and a stated standing: ranked alphabet and ground term, automaton
  and run, recognizable language, WSkS restricted atom, track code, and full
  SkS. Their distinctions are used later in the theorem, constructions,
  counterexample, or finite/infinite boundary. The Thatcher--Wright passage
  follows the AGENTS rule especially closely: it describes the owed artifacts
  instead of naming an unverified construction.

## Display-by-display definedness conclusion

Every mathematical display in the presentation and reviewed host excerpt is
well formed under definitions available before the display:

1. presentation lines 18--20: the four-component source automaton tuple;
2. presentation lines 57--59: the four restricted WSkS atomic forms;
3. presentation lines 94--97: one nullary and five binary inclusion rules;
4. presentation lines 109--113: the arity-indexed local run clause, including
   the empty-conjunction nullary case;
5. host lines 889--892: the arity-indexed least ground-term constructor;
6. host lines 898--901: the arity-indexed bottom-up transition form.

No displayed expression has an unbound index, an untyped variable, an
unavailable domain, or an illicit empty/nullary interpretation.

## Files and portions actually read

Only the following repository text was opened for this review:

1. `handbook/parts/p09/presentations/n-c-015.tex`, lines 1--166, read directly
   from line 1 through EOF;
2. `handbook/parts/p09/logic-in-computer-science.tex`, lines 877--944;
3. `spec/research/p09-tata-2008-source-note.md`, lines 1--203, through EOF;
4. `spec/research/p09-thatcher-wright-1968-acquisition-note.md`, lines 1--96,
   through EOF;
5. `spec/research/p09-source-presentations-lot2-3.md`, lines 751--775 only;
6. `handbook/bib/handbook.bib`, the `ComonEtAl2007` entry at lines 5883--5889
   and the `ThatcherWright1968` entry at lines 6041--6050.

The admission/review-history statements embedded in a permitted source note or
compact record were not treated as evidence for this fresh verdict. The
verdict rests on the reviewed LaTeX and the permitted substantive source and
acquisition records.

## Prohibitions observed

- I did not open or use any earlier or parallel integrated N-c-015 report,
  including any round-1 or round-2 report.
- I did not open or use
  `spec/research/p09-tata-2008-independent-review-record.md` or anything under
  `spec/research/boards/p09-tata-2008/`.
- I did not ask, list, message, or otherwise consult another agent.
- I did not open a manuscript PDF, render the manuscript, inspect a PDF/PNG/page
  image as manuscript evidence, or use an original historical source page.
- I did not run a LaTeX build, test, test harness, checker, repository script,
  automated validator, or hash operation.
- I did not edit the manuscript, host, source notes, register, ledger,
  bibliography, or any file other than this review record.

REGISTER STATUS: OPEN
