VERDICT: REJECT

# N-c-016 Round 5 mathematical/definedness review

The frozen current presentation is not yet mathematically admissible. The
exhaustive must-fix list for this review contains three defects, all in the
general Clarke--Emerson factorization. They are independent: repairing the
initial store does not repair the guards, and repairing the guards does not
make a merged transition's update well-defined.

## Line-specific must-fixes

1. **An initial duplicate-labelled node is left without an initialization
   whenever it also has an incoming arc**
   (handbook/parts/p09/presentations/n-c-016.tex:443-450, with the possibility
   of cycle-closing arcs at lines 401-406). The assignments on incoming arcs
   define what happens when execution *enters* \(v_r\); none of those
   assignments is executed when a run starts at an initial \(v_r\). The
   qualifier “and has no incoming arc” therefore leaves \(z_{\Lambda}\)
   undefined at an initial node that lies on a cycle or otherwise has an
   incoming edge, even though that node's label asserts \(z_{\Lambda}=r\). No
   invariant in the presentation says that every initial node is
   source-in-degree zero; indeed, the construction closes cycles through
   checked fragment roots.

   **Minimal repair:** replace the conditional sentence at lines 449-450 by
   an initialization for *every* initial \(v_r\), independently of whether it
   has incoming arcs: initialize \(z_{\Lambda}:=r\) when execution starts at
   \(v_r\), while retaining \(z_{\Lambda}:=r\) on every incoming arc for later
   entries. If the formalism permits several initial nodes, state the
   corresponding initial-store disjunction/correlation explicitly.

2. **The general local enabling guards erase the auxiliary values that were
   introduced to distinguish global nodes**
   (handbook/parts/p09/presentations/n-c-016.tex:451-476; compare the stated
   use at lines 409-415 and the concrete guard at lines 427-429). The general
   source and target tuples contain only the current region \(R_u/R_v\) and
   the other-process region components \(S_1,\ldots,S_p\). The generated guard
   is only \(S_1\land\cdots\land S_p\). It contains no source-state equality
   such as \(z_{\Lambda}=r\). Consequently two global nodes with the same
   process regions but distinct discriminator values induce indistinguishable
   local enabling conditions, so their different outgoing behavior is
   conflated. This contradicts the worked skeleton, where
   \(\mathsf{TURN}=1\) is an indispensable part of the
   \(\mathsf{TRY}_1\to\mathsf{CS}_1\) guard.

   **Minimal repair:** for every global \(i\)-arc \(e\), define its local
   source guard \(\gamma_e\) as the conjunction of all source-label conjuncts
   other than \(P_i\)'s own current-region atom. In particular, \(\gamma_e\)
   must include every applicable auxiliary equality \(z_{\Gamma}=q\), as well
   as the other-process components. Use \(\bigvee_e\gamma_e\), not merely
   \(\bigvee(S_1\land\cdots\land S_p)\), as the local guard. Preserve the
   \(k=1\) convention only for the empty *other-process* part; it must not erase
   an auxiliary equality.

3. **Disjoining all global arcs with the same local endpoints makes the local
   update undefined when those arcs carry different assignments**
   (handbook/parts/p09/presentations/n-c-016.tex:458-479; the concrete
   counterpattern already appears at lines 422-426). Lines 458-476 construct
   one \(R_u\to R_v\) arc whose guard is the disjunction over all corresponding
   global arcs. Line 478 then says to copy an assignment “if such a global arc”
   carries one, but there need not be one common assignment. In the worked
   \(P_1\) skeleton itself, the two
   \(\mathsf{NCS}_1\to\mathsf{TRY}_1\) branches differ precisely in that the
   \(\mathsf{TRY}_2\) branch assigns \(\mathsf{TURN}:=2\), whereas the
   \(\mathsf{NCS}_2\lor\mathsf{CS}_2\) branch does not. More generally, arcs
   to different copies of one duplicate label can require different
   \(z_{\Lambda}:=r\) updates. A single merged edge can neither choose the
   correct update nor omit it soundly.

   **Minimal repair:** retain one guarded-command branch per global arc, or
   group corresponding global arcs only when their complete update maps are
   identical. Formally, for each triple \((R_u,R_v,\sigma)\), where \(\sigma\)
   is the complete auxiliary update (with “no assignment” represented by the
   identity update), create a local transition with guard
   \[
     \bigvee\{\gamma_e:
       e\text{ has endpoints }R_u,R_v\text{ and update }\sigma\}
   \]
   and update exactly \(\sigma\). Never merge branches carrying different
   updates.

No other line-specific mathematical must-fix was found in the authorized text
scope.

## Bounded positive evidence outside the rejected factorization

### Definitions, types, quantifiers, arities, and nullary cases

- Clarke--Emerson binds \(k\geq1\) before process-indexed syntax and totality
  (n-c-016.tex:41-60), permits the strong-until witness at zero
  (lines 62-99), binds the Hamiltonian domain by \(n\geq1\)
  (lines 208-234), and separately binds duplicate multiplicity \(d\geq2\),
  region count \(m\geq1\), region indices \(u,v\), and the \(k=1\) empty
  other-process conjunction (lines 441-476). Those repairs are well-typed; the
  remaining failures are the three operational factorization clauses above.
- Queille--Sifakis separates the all-variable vector \(\mathbf X\) from the
  protocol's scalar data variable \(X\) and gives the action labels their
  program-event standing (lines 509-570). Its execution domain \(D_s\) makes
  every temporal quantifier range only over actual positions of a finite or
  infinite maximal execution (lines 600-635).
- The finite action-family notation now quantifies \(k\in\mathbb N\) and
  \((a_i)_{i=1}^k\), defines the process-set abbreviation by a set-indexed
  disjunction, and fixes
  \(\bigvee\varnothing=\mathsf{false}\) and
  \(\bigwedge\varnothing=\mathsf{true}\) (lines 645-681). Thus both nullary
  action abbreviations, empty-process enabledness, empty-family liveness, and
  empty-family deadlock behavior have determinate truth values.
- Emerson--Halpern explicitly requires nonempty state and path domains, types
  finite/infinite suffix operations, and gives a positive-arity base case for
  the Appendix segment recursion (lines 907-922, 977-1008, and 1192-1228).
- Baier--Katoen's Hamiltonian construction binds \(n\geq1\), gives the
  length-one base of \(\Psi\), and restricts the recursive clause to
  \(2\leq k\leq n\) (lines 1872-1919). Its \(S=\varnothing\) branch is
  separated from the nonempty host instantiation (lines 1581-1600).

### Paths, state/path ownership, and fixed-point directions

- Clarke--Emerson's paths are infinite because the union of the indexed step
  relations is total; \(A[U]\) and \(E[U]\) are state formulas with correctly
  scoped path quantifiers and current-inclusive strong until (lines 41-124).
  The increasing universal/existential until chains have the correct guards
  and finite stabilization argument (lines 126-183).
- Queille--Sifakis preserves finite maximal executions and sinks without ever
  asking the fictitious \(\omega\) state to satisfy a formula (lines 600-643).
  The predecessor maps, pointwise transformer union/intersection, iterate
  types, and four ascent/descent identities are explicit; image-finiteness and
  the delegated proof boundary are retained (lines 767-829).
- Emerson--Halpern keeps CTL* state formulas and path formulas mutually typed,
  restricts \(A/E\) to the state-forming bridge, and gives current-inclusive
  \(F/U\), proper next on finite paths, and infinitely-many-position semantics
  (lines 1019-1111). The MPL endpoint/next conflict is reported rather than
  silently repaired (lines 1370-1440).
- Baier--Katoen keeps CTL path operators immediately under path quantifiers
  (lines 1621-1668), states existential until as the least inclusion-closed
  set and existential always as the greatest post-fixed set
  (lines 1686-1734), and runs the increasing and decreasing chains in their
  correct directions (lines 1736-1803). The no-terminal-state and
  recursive-choice/cycle conditions needed by the greatest-set direction are
  not dropped.

### Graph/formula translations and witness systems

- The Clarke--Emerson Hamiltonian reduction explicitly gives \(V\), all added
  states, all added edges, labels, the infinite sink continuation, and both
  logical directions; it concludes only NP-hardness for the extended problem
  (lines 208-234).
- The Baier--Katoen-to-host bridge defines the action-forgetting relation
  \(R_0\), the correctly typed valuation
  \(V_0:AP\to\mathcal P(S)\), and the recursive constructor translation before
  using the host method (lines 1504-1606). Collapsing action-labelled triples
  is correctly reflected by \(|R_0|\leq K\), not by identifying the two
  representation parameters.
- The Baier--Katoen Hamiltonian transition system includes the fresh sink,
  all sink edges, singleton vertex labels, the permutation formula, and the
  system-level negation equivalence (lines 1872-1930). The proof explicitly
  distinguishes enumerated formula size from the linear model-checking bound
  and identifies the missing uniformity premise in the source's informal
  \(\mathsf P=\mathsf{NP}\) inference.
- The CTL/LTL witnesses give both base systems, the \(n>0\) recursive edge
  clauses, labels, the separating paths, and the exact proof omissions
  (lines 1932-1967). The CTL* grammar and the strictness formula are well-typed;
  the atom-substitution step is labelled as an omitted elementary
  reconstruction (lines 1969-2004).
- Emerson--Halpern's separating-family invariants and their cited/reader-left
  proof steps are not promoted to self-contained proofs (lines 1192-1332).
  Its PL translation is constructor-by-constructor, whereas the literal MPL
  clauses remain explicitly unresolved (lines 1347-1440).

### Proof strength, complexity, acquisition, and host consistency

- The Clarke--Emerson text separates the printed labelling argument and
  \(\operatorname{length}(f)|S|^2\) representation bound, the two proposition
  proofs, the abridged tableau, and the worked synthesis construction
  (lines 126-318 and 483-495). It does not substitute the later edge-linear
  host theorem for the 1981/1982 accounting convention.
- The Queille--Sifakis text preserves the external non-loss assumption, the
  image-finite hypotheses, the Sifakis-1979 proof delegation, the user-set
  iteration cap, and the absence of a general complexity or synthesis theorem
  (lines 572-577 and 807-894).
- The Emerson--Halpern text distinguishes printed proofs, cited results,
  reader-left inductions, proof-and-diagram-supported repairs, and unresolved
  literal clauses; it attributes no CTL/CTL* labelling or complexity theorem
  to that expressiveness article (lines 907-1468).
- The 1999 Clarke--Grumberg--Peled subsection stays at acquisition strength:
  bibliography and contents locators only, with no grammar, algorithm, proof,
  example, or complexity content attributed to the unacquired first-edition
  body (lines 1470-1491).
- The Baier--Katoen runtime retains finiteness, no terminal states, predecessor
  adjacency representation, the distinction between \(K\) labelled triples
  and \(|R_0|\) binary edges, and the prohibition on materializing an
  exponentially enlarged ENF formula (lines 1601-1606, 1670-1684, and
  1856-1930). No space theorem or CTL* model-checking result is inferred.
- The inherited host requires \(S\ne\varnothing\), total \(R\), and
  \(V:\mathsf{Prop}\to\mathcal P(S)\). The presentation instantiates it only
  for finite nonempty \(S\) and handles empty \(S\) by the source's vacuous
  system semantics, so the empty-state bridge is sound
  (temporal-epistemic-supplement.tex:46-56;
  logic-in-computer-science.tex:948-1015;
  n-c-016.tex:1530-1606).

### Supplied technical-name rule

No independent technical-name violation remains outside the rejected
factorization. “Synchronization skeleton,” “global system flowgraph,” “model
fragment,” “interpreted Petri net,” MPL “stage,” the proof-local segment forms,
\(D_s\), \(R_0/V_0\), \(\operatorname{tr}\), and the propositional comparison
abbreviations are each accompanied by necessity or source standing, an
eliminable definition (or an explicitly reported source definition), a type,
a nonredundancy explanation, and an actual later use. The auxiliary
\(z_{\Lambda}\) likewise has necessity, an exact finite value domain,
program-variable standing, and a nonredundancy explanation, but its promised
use is not operationally realized until must-fixes 1-3 are made; that is why
those are mathematical defects rather than a separate fourth naming-only
finding.

## Explicit non-claims

- This verdict applies only to the frozen 2,021-line source text read in this
  review. It is not a verdict on a rendered handbook, a historical publication
  file, or any other checkout or revision.
- No omitted source proof was independently completed. Reader-facing
  reconstruction was accepted only where the presentation labels it as such
  and supplies a determinate logical argument.
- No content-level claim is made for the unacquired Clarke--Grumberg--Peled
  first edition.
- No compilation, visual-layout, publication-readiness, source-fidelity, or
  human-review conclusion is implied by this mathematical/definedness verdict.

## Substantive text read

- handbook/parts/p09/presentations/n-c-016.tex: lines 1-2021, complete through
  EOF (with a focused reread of lines 401-482).
- handbook/parts/p09/logic-in-computer-science.tex: lines 930-1060 and
  1485-1525, including the host CTL method/theorem and the actual N-c-016
  insertion point.
- handbook/parts/p08/temporal-epistemic-supplement.tex: lines 42-190.
- spec/research/p09-clarke-emerson-1981-source-note.md: lines 1-884, complete
  through EOF.
- spec/research/p09-queille-sifakis-1982-source-note.md: lines 1-867, complete
  through EOF.
- spec/research/p09-emerson-halpern-1986-source-note.md: lines 1-729, complete
  through EOF.
- spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md: lines
  1-470, complete through EOF.
- spec/research/p09-baier-katoen-2008-ch6-source-note.md: lines 1-1120,
  complete through EOF.
- handbook/bib/handbook.bib: lines 2393-2407, 2409-2422, 2424-2436,
  2438-2447, 2449-2458, 4815-4824, 4826-4835, 4837-4846, and 4897-4906.

## Prohibitions observed

- No prior N-c-016 review/report (including an earlier mathematical report),
  source-fidelity/publication report, board/admission/history file, parent
  conclusion, or other agent output was opened or consulted.
- No agent was contacted, inspected, or delegated to.
- No PDF, render, screenshot, page image, historical publication file, or web
  source was opened or inspected.
- No TeX build, test, checker, validator, repository script, hash computation,
  or executable source tool was run. Shell use was limited to direct
  Get-Content reads of the authorized text and a non-content Test-Path for the
  designated output.
- No memory file was consulted, because prior-run memory would have violated
  the blind-review constraint.
- No manuscript or repository file other than this designated Round 5 report
  was created, modified, deleted, or reverted.

REGISTER STATUS: OPEN
