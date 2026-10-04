REJECT

# Round 1 mathematical and proof-correctness review

VERDICT: REJECT — F1, F2, F3, F4, F5.

## Independence, competence, and evidence boundary

This is a blind opening review.  I did not read the ledger, the chair
transcript, or either other reviewer's report.  I am not a credentialed
Russian-language specialist and do not certify literary translation.  I can
read the mathematical Russian in these two papers at a working level.  For
this mandate I used the complete page images at original detail, the printed
formulae and theorem displays, the surrounding Russian mathematical prose,
and independent mathematical derivation.  The supplied OCR extractions were
used only to locate passages; no symbol or source-language conclusion rests on
OCR.

I visually read all four physical pages of the announcement.  They are printed
pp. 326--329 in that order.  I also visually read all twenty-nine physical
pages of the expansion.  They are printed pp. 103--131 in that order.  I did
not inspect a handbook PDF and ran no test, checker, repository script, TeX
command, or build.

## Frozen identity check

I recomputed the seven SHA-256 identities before substantive review.  Every
value matched the charter:

| Frozen object | Recomputed SHA-256 |
|---|---|
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1961.pdf` | `44213AEBE4DB2F1C389B812A7401138799C3DB4749C3605BA7211BBB4BAF96F9` |
| `tmp/pdfs/p09-trakhtenbrot-1961/trakhtenbrot-1962-expanded.pdf` | `EAB4438A7BBA2B6009374826A98A3A61FB6465C493F57B03D2C6C7385824096D` |
| `handbook/parts/p09/presentations/n-c-014.tex` | `6D780FB5E14B34DB56C1B65A1040C4A194C57B5FDD012B7CD0BABD66341CB2D1` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `A09D35C6EFDF1DF575D47F549A7270B60B1A5569EC33845EB51CDA28CEF5DCDD` |
| `handbook/bib/handbook.bib` | `75AB70009DF4AB8B2180CFFC6987EA244ADB2F978B1D889C87009EFF17066D5C` |
| `spec/research/p09-trakhtenbrot-1961-source-note.md` | `3028B89EE4B8CE8104416E57096B9015291E766BFA4660E1A85B85F3913C3B4C` |
| `spec/research/p09-source-presentations-lot2-3.md` | `E34436FBDAF4CA90A8A93A02AA305E65F5F7197027A545E6B5DEC94FAB9B4631` |

## Findings

### F1 [must-fix] The finite-realization and general-solution hypotheses are not stated at theorem strength

- **Reader location:**
  `handbook/parts/p09/presentations/n-c-014.tex:623-631` and
  `:656-668`.
- **Controlling source:** announcement p. 328, Theorems 4, \(4'\), and 5;
  expansion pp. 119--120, Section 4 Theorems 1--2, and pp. 121--124,
  Section 4 Theorems 3 and \(3'\).  The exact hypothesis is also recorded in
  `spec/research/p09-trakhtenbrot-1961-source-note.md:233-246` and
  `:269-293`.
- **Claim:** line 623 begins merely, “Suppose \(\varphi(X,Y)\) defines the
  graph of a total operator,” and line 656 says the general-solution
  alternative holds “for a closed relation.”  The source is not making these
  assertions for an arbitrary defining formalism or an arbitrary closed
  relation.  The formula is an \(\mathcal I\)-formula; consequently its graph
  or relation is \(\mathcal I\)-definable and has the finite homogeneous basis
  used in the proof.  Without that hypothesis the first statement is false:
  for example, a causal operator whose output at time \(t\) records whether
  the input prefix contains a prime number of ones is total, zero-anticipating,
  and continuous, but it has infinitely many residuals and is not finite-state
  (restricting to unary words gives the nonregular prime-length language).
- **Harm:** the reader has to infer a hypothesis on which both the theorem and
  the weight bound depend.  Taken literally, it promotes a source theorem
  about \(\mathcal I\)-definable relations into a false theorem about all
  continuous operators or all closed relations.
- **Required correction:** at line 623 say explicitly that an
  \(\mathcal I\)-formula defines the graph.  At line 656 say explicitly that
  the relation is the closed relation defined by an \(\mathcal I\)-formula
  (hence is homogeneous of finite degree).  Carry that same subject through
  Theorem \(3'\).  Do not leave the hypothesis to paragraph context.

### F2 [must-fix] The displayed recurrence form omits the free input and the initial basis state

- **Reader location:**
  `handbook/parts/p09/presentations/n-c-014.tex:594-606`.
- **Record location:**
  `spec/research/p09-trakhtenbrot-1961-source-note.md:198-215` is likewise
  schematic enough to leave the free input and initialization invisible.
- **Controlling source:** expansion p. 118, display (5), Theorem 2, and
  Theorem \(2'\); announcement p. 328, Theorem 3 and its displayed recurrent
  form.
- **Claim:** the reader displays only
  \((\exists Z_1\cdots\exists Z_k\exists U)(\forall t)\theta(t)\), then names
  only the bound predicate variables and says that \(\theta\) relates their
  current and next values.  As printed, this is a sentence independent of the
  stream \(X\) whose set is supposedly being defined.  It also suppresses the
  fixed initial basis-state clause.  Trakhtenbrot's expansion uses the free
  value \(X(t)\), current auxiliary values, the next state values, and fixed
  initial values such as \(q_1(1)=1\), \(q_2(1)=\cdots=q_k(1)=0\).
- **Harm:** the displayed formula does not itself define the claimed subset of
  streams, and without the initial-state clause it can select a union of basis
  portions rather than the designated original set.  This fails the exact
  recurrence, standing, and definition-before-use requirements.
- **Required correction:** display the formula as a formula in the free stream
  variable, for example
  \(\varphi(X)\equiv(\exists q_1\cdots\exists q_k\exists U)
  [\operatorname{Init}(q(1))\land(\forall t)
  \theta(X(t),q(t),U(t),q(t+1))]\), and immediately expand
  \(\operatorname{Init}\) or write the fixed initial bits literally.  State
  the standing of \(X\), the auxiliary state predicates, and the choice
  predicate.  Apply the same precision to the source note; no new technical
  name is needed.

### F3 [must-fix] “Range of an \(A\)-operator” is ill-typed for a finite-word language

- **Reader location:** the only typed operator is the stream map at
  `handbook/parts/p09/presentations/n-c-014.tex:527-550`; the finite-word
  definitions occur at `:687-692`.
- **Controlling source:** expansion p. 110 defines the word maps induced by a
  zero-anticipation operator and their heredity property; pp. 127--128 define
  automaton-enumerability, automaton-decidability, and prove Theorem 2.
- **Claim:** under the reader's displayed type,
  \(T:A^{\mathbb N_+}\to B^{\mathbb N_+}\), the range of \(T\) is a set of
  infinite streams, not a language of finite words.  The source first uses
  zero anticipation to induce, for every length \(t\), a well-defined map from
  input words of length \(t\) to output words of length \(t\); the maps commute
  with taking prefixes.  Only that induced finite-word action makes the later
  source definitions well-typed.  The recognizing convention also needs the
  source's designated output result on the presented finite word.
- **Harm:** “automaton-enumerable” is introduced without an object of the right
  type, violating the repository terminology rule's Definition and Standing
  clauses.  The subsequent two directions of Theorem 2 therefore lack exact
  domains and codomains even though their informal content is right.
- **Required correction:** before the two source terms, define the induced
  length-\(t\) word map from any infinite extension and prove its
  extension-independence from zero anticipation.  Then state the source's
  across-all-lengths range convention and terminal recognition convention
  exactly.  Restate both directions of Theorem 2 against those typed maps.

### F4 [must-fix] Theorem 3 recognizes special beginnings, not all finite initial words, and its Büchi attribution is missing

- **Reader location:**
  `handbook/parts/p09/presentations/n-c-014.tex:693-698`.
- **Compact-record location:**
  `spec/research/p09-source-presentations-lot2-3.md:656` repeats “finite initial
  words.”
- **Source-note location:**
  `spec/research/p09-trakhtenbrot-1961-source-note.md:318-325` correctly uses
  “special beginnings” but does not state the source's explicit Büchi
  attribution at the theorem locator.
- **Controlling source:** expansion pp. 130--131, Section 5.3, definition 3 and
  Theorem 3.
- **Claim:** for an eventually-zero predicate \(X\), the source calls
  \(X(1)\cdots X(t)\) a *special beginning* only when
  \(X(\tau)=0\) for every \(\tau>t\).  The theorem recognizes precisely these
  complete-support beginnings for satisfying predicates.  It does not
  recognize every finite prefix.  For instance, if \(X(2)=1\), its length-one
  prefix is a finite initial word but is not a special beginning.  The printed
  theorem also explicitly attributes effective construction in the
  \(\mathcal I'\) case to Büchi.
- **Harm:** the present wording strictly enlarges the recognized language and
  drops a source attribution expressly required by M21.  It also replaces a
  needed source term by an undefined informal phrase.
- **Required correction:** define *special beginning* exactly before use;
  replace “finite initial words” by that term in the reader and compact record;
  preserve the distinction “existence for an arbitrary \(\mathcal I\)-formula,
  effective construction for an \(\mathcal I'\)-formula”; and attach the
  source's Büchi attribution to the effective half in the reader and source
  note.

### F5 [must-fix] The open-relation qualification following Theorem \(4'\) is omitted from the reader

- **Reader location:**
  `handbook/parts/p09/presentations/n-c-014.tex:633-639`.
- **Controlling source:** announcement p. 328, the remark immediately after
  Theorem \(4'\); the qualification is already recorded at
  `spec/research/p09-trakhtenbrot-1961-source-note.md:248-253`.
- **Claim:** after the closed-homogeneous existence theorem, the announcement
  separately states the analogous result for an open relation but without the
  weight estimate.  The reader gives only the closed case.
- **Harm:** this drops the source's explicit topology/strength qualification at
  the exact place where the presentation claims to distinguish graph,
  solution, topology, and bound strength.  The source note and reader are not
  reconciled on this clause.
- **Required correction:** add one sentence after the closed-case clauses:
  the source separately records the analogous open-relation assertion, but
  without a bound on solution weight.  Do not merge it into the closed theorem
  or transfer the closed-case bound.

## Independent derivations and checked-clean mathematical content

The findings above are localized.  The following substantive chains were
independently rederived and are correct on the frozen snapshot once the stated
hypotheses are read as the source intends.

1. **Normal form.**  Predicate quantifiers can be moved ahead of individual
   quantifiers; the individual quantifiers can be pushed into the matrix and
   split at the free time variable.  A predicate assignment on the bounded
   prefix can be spliced with one on the tail, which justifies distributing a
   predicate quantifier over the separated lower/upper factors.  The bounded
   lower window has finitely many Boolean valuations.  This supports reader
   lines 512--525 and source-note lines 113--128.
2. **Operator classes.**  The stream type, anticipation condition, whole-suffix
   finite-memory equations, least-state weight, bounded-window finite
   equations, and zero-anticipation \(A\)-operator specialization at reader
   lines 527--571 agree with expansion pp. 109--113.  A one-state machine may
   still ask whether a \(1\) occurs strictly later in the suffix, so finite
   memory alone supplies neither continuity nor effectiveness.  Conversely,
   finite memory plus a fixed anticipation bound gives the displayed finite
   window equations.
3. **Homogeneity from definability.**  Put a defining formula in lower/upper
   normal form.  Prefix substitution changes only one of finitely many Boolean
   lower-window functions and leaves one of finitely many upper contexts.
   Hence only finitely many semantic portions occur.  Appending a bit performs
   the corresponding residual update, so the internal transition is obtained
   effectively before any nonemptiness choice.  This validates the positive
   direction and the effectiveness boundary in reader lines 594--620.
4. **Closed homogeneous converse.**  A finite basis supplies finitely many
   one-hot state predicates and an internal transition.  A choice predicate
   selects an allowed next letter; the fixed initial basis state selects the
   original set.  Every generated stream lies in the closure, and every point
   of the closure has a compatible choice stream.  Local finite-state
   recurrence gives homogeneity; projection of the compact witness space gives
   closedness.  This validates the converse only after F2 makes the free input
   and initial state explicit.
5. **Continuous finite realization.**  The graph of an
   \(\mathcal I\)-definable operator has a finite portion basis.  Each nonempty
   portion is compact.  Continuity of its first output coordinate is therefore
   uniformly determined by a finite input prefix; taking the maximum over the
   finite basis gives one anticipation bound.  The basis index is a memory
   state, so the weight is at most the homogeneity degree.  Dropping continuity
   leaves the finite basis/state update but permits the output selector to be
   an arbitrary whole-suffix function.  Thus expanded Theorem 2 proves finite
   memory only, exactly as reader lines 622--631 say once F1 is repaired.
6. **General solutions.**  Stable deletion removes empty basis portions and
   then portions with no surviving output continuation.  Deletion of the
   initial portion is exactly the no-zero-anticipation-solution branch.  In the
   surviving branch, a parameter bit selects every surviving output and only
   such an output; induction proves every parameter substitution is a
   solution, while a parameter selector extracted from any given solution
   proves completeness.  Closedness converts compatible prefixes into
   membership.  Padding/shifting the first \(p\) output places reduces each
   fixed-\(p\) class to this zero-anticipation construction; it does not produce
   one solution uniform over unbounded \(p\).  Reader lines 641--670 preserve
   both general-solution quantifiers and the fixed-\(p\) boundary, subject to
   F1.
7. **Explicit synthesis.**  Semantic fictitiousness outside
   \([1,t+p]\) is exactly the anticipation-\(p\) criterion.  In the zero-shift
   prefix-controlled case, substituting the first input column and shifting
   produces only finitely many residual formulae by normal form.  Their output
   values and residual indices are precisely the canonical tables.  Expansion
   pp. 126--127 does produce two residual formulae and the two tables described
   at reader lines 672--685.

The announcement/expansion distinction, the unequal official English title
renderings,
\(\mathcal I\) versus \(\mathcal I'\), the semantic fictitious-occurrence
definition, the finite-memory/finite-operator nonimplication, graph versus
solution, both quantifiers in a general solution, fixed versus unbounded
anticipation, source-time conditionality, and the modern-versus-literal
finite-word boundary are otherwise kept separate.  The bibliography entries at
`handbook/bib/handbook.bib:5991-6013`, the shared modern theorem at
`handbook/parts/p09/logic-in-computer-science.tex:811-825`, and its navigation
paragraph at `:2341-2347` are mathematically consistent with those boundaries.

## Mandatory coverage map for this seat

| Point | Disposition |
|---|---|
| M01 | checked-clean: all seven hashes recomputed and matched |
| M02 | checked-clean: all 4 + 29 source pages visually read; page maps confirmed |
| M05 | checked-clean: syntax, domains, primitive successor, eliminable conveniences, and \(\mathcal I'\) range checked |
| M06 | checked-clean: semantic fictitiousness, lower/upper forms, effective normal form, and reported proof moves checked |
| M07 | checked-clean: typed stream operator, anticipation, prefix preservation, whole-suffix memory, weight, finite equations, and \(A\)-operator distinction checked |
| M08 | checked-clean: both primitive-recursive negative reductions and strict-future one-state example checked |
| M09 | checked-clean: portions, tuple extension, degree, basis, transition, graph/singleton examples, and uncountability counterexample checked |
| M10 | checked-clean: homogeneity and effective internal-transition derivation given above |
| M11 | F2: recurrence display/initialization; remaining closed-homogeneous and closure arguments checked-clean |
| M12 | checked-clean: internal transition unconditional; external nonemptiness choice conditional; Putnam fragment separated |
| M13 | F1: missing explicit \(\mathcal I\)-definability hypothesis; proof and bound otherwise checked-clean |
| M14 | checked-clean: no continuity, finite memory only; no lookahead collapse |
| M15 | F5: omitted open-relation qualification; graph/solution distinction and closed clauses otherwise checked-clean |
| M16 | checked-clean: parameter standing, completeness, and soundness quantifiers checked |
| M17 | F1: closed \(\mathcal I\)-definable-relation hypothesis; deletion, branches, parameter selection, closedness, bound, and conditionality otherwise checked-clean |
| M18 | checked-clean: theorem is separately fixed at each \(p\); no unbounded generalization |
| M19 | checked-clean: explicit definition, anticipation tests, shifted residual termination, tables, and pp. 126--127 example checked |
| M20 | F3: induced word maps and recognition convention missing; theorem directions and prefix/extension conditions otherwise checked |
| M21 | F4: special-beginning language and Büchi attribution; existence/effectivity distinction otherwise checked |
| M22 | checked-clean: announcement numbering is not transferred to expansion |
| M23 | checked-clean: modern regular/MSO sentence and Thomas route are expressly nonliteral and non-substitutive |
| M26 | F2, F3, F4: recurrence standing, finite-word operator standing, and missing exact source term; all other introduced names satisfy necessity, definition, standing, nonredundancy, and use |
| M27 | F1--F5; no additional continuity, closedness, operator-class, source-laundering, translation, priority, or status defect found |
| M28 | checked-clean: review remains topic-only; rights and no-test/no-build boundaries are explicit and were obeyed |

No additional blocker or must-fix is being withheld.  Acceptance requires all
five findings to be corrected on one new frozen snapshot and the affected
mathematical review rerun blind.

VERDICT: REJECT — F1, F2, F3, F4, F5.
