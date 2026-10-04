VERDICT: REJECT

# Round 8 adversarial publication/terminology review

The frozen LaTeX is not yet publication-admissible. Three line-specific
must-fixes remain. They are independent: repairing the notation order does
not repair the factorization's domain, and neither repair restores the omitted
proof-status qualification.

## Line-specific must-fixes

1. **handbook/parts/p09/presentations/n-c-016.tex:441-488, especially
   lines 461-487 — the “general factorization” omits the locality hypothesis
   needed for its local transitions to realize the global arcs.**

   The rule takes a global \(i\)-arc, retains the other processes' region
   components only in the source guard \(\gamma_e\), and creates a local
   transition that changes \(P_i\)'s region and the auxiliary variables. It
   contains no operation capable of changing a \(P_j\)-region component for
   \(j\ne i\). Consequently, if a global \(i\)-arc changes any such component,
   the constructed local \(P_i\) transition reaches a different joint state
   from the global arc's target. Requirement group 8 at lines 375-381 supplies
   the needed preservation condition for the worked mutual-exclusion model,
   but lines 441-488 call the rule general and line 487 says that it turns a
   finite global model into executable per-process enabling conditions without
   carrying that condition into the rule's stated domain.

   **Minimal repair:** immediately before the quantification over global
   \(i\)-arcs, state the locality premise
   \[
     \forall j\ne i,\quad
     \text{the \(P_j\)-region component at the target equals its component at
     the source},
   \]
   say explicitly that group 8 establishes it for the displayed construction,
   and restrict the claimed factorization to models satisfying that premise.
   If the authors intend arbitrary synthesized models instead, lines 461-488
   must define how a nonlocal global arc is rejected or represented; the
   present local transition cannot represent it.

2. **handbook/parts/p09/presentations/n-c-016.tex:547-564, especially
   lines 549-552 versus 560-564 — the protocol's scalar \(X,Y,Z\) symbols are
   used before their standings are declared.**

   The preceding IPN definition has already assigned the visually related
   \(\mathbf X\) the standing of the vector of retained IPN variables
   (lines 520-527). The next paragraph then uses \(X\) in \((X,Y)\), calls
   \(Y\) a current bit, and uses \(Z\) before the following paragraph finally
   says that \(X\) is the sender's data value rather than \(\mathbf X\), and
   that \(Y,Z\) are the two control bits. The eventual clarification is
   correct, but it occurs after the first substantive uses and therefore does
   not satisfy the requested definition-before-use discipline in the exact
   place where the scalar/vector collision matters.

   **Minimal repair:** move the declarations now at lines 560-564 before the
   sentence beginning “The sender transmits,” or revise that first sentence to
   introduce “the sender's data value \(X\), its control bit \(Y\), and the
   receiver's control bit \(Z\)” before any formula using them. Retain the
   explicit statement that scalar \(X\) is not the IPN vector \(\mathbf X\).

3. **handbook/parts/p09/presentations/n-c-016.tex:1290-1294 — the
   Theorem 5 account does not preserve the source's reader-delegated Boolean
   cases.**

   Line 1290 says that invariant (3) “is proved by induction through”
   \(EXq\), \(E[qUr]\), and \(A[qUr]\). The controlling source note records
   that the Appendix prints those modal cases but leaves the atomic,
   conjunction, and negation cases to the reader. The paragraph correctly
   records the separate cited dependency and its bad theorem number, yet
   omits this local proof boundary. Elsewhere the presentation explicitly
   distinguishes printed modal cases from reader-left Boolean cases
   (lines 1349-1352), so the current wording also creates an internal
   proof-status asymmetry between the Theorem 5 and Theorem 7 accounts.

   **Minimal repair:** replace the opening sentence at line 1290 with wording
   such as: “For invariant (3), the Appendix prints the
   \(EXq,E[qUr],A[qUr]\) induction cases and leaves the atomic, conjunction,
   and negation cases to the reader.” Keep the following Theorem 8(a)
   dependency and wrong-cross-reference correction unchanged.

## Bounded evidence that does not require repair

- The hierarchy and ownership are coherent: the registered subsection and its
  five source-specific subsubsections have definitions before their substantive
  uses, source-specific labels, and a separate acquisition-boundary subsection.
  The host includes this file at
  handbook/parts/p09/logic-in-computer-science.tex:1519, within the model-
  checking section and before the program-logics section.
- Apart from the missing locality premise above, the current factorization
  gives the fresh discriminator \(z_\Lambda\) a finite total value domain,
  defines its value at every global node and designated initial node, updates
  it on every global arc, separates the state guard \(\gamma_e\) from the
  complete transition update \(\sigma_e\), and merges only transitions with
  identical endpoints and complete updates (n-c-016.tex:441-488). Those
  names have exact eliminable definitions, explicit standings, stated
  nonredundancy, and immediate later use.
- The IPN vector itself is now correctly scoped to variables retained in the
  translated IPN, and deleted internal variables of non-specified type are
  explicitly excluded (n-c-016.tex:516-535). Finding 2 concerns only the
  later reader-facing declaration order of the protocol's scalar symbols.
- The Emerson--Halpern structure initially permits finite or infinite
  sequences, while the definition and equivalence involving
  \(R\)-generability are now explicitly restricted to
  \(X\subseteq S^\omega\). The reader-facing equivalence also adds state
  completeness because the chosen definition requires a total relation on all
  of \(S\), and it labels this as a handbook qualification rather than
  silently attributing it to the source
  (n-c-016.tex:917-924, 996-1049).
- The Baier--Katoen bridge has the right source and host types. It defines
  \(R_0\), \(V_0\), the host proposition alphabet, and the recursive formula
  translation; separates action-labelled transition count \(K\) from
  \(|R_0|\); does not instantiate the nonempty host structure when
  \(S=\varnothing\); states source semantics before asserting semantic
  preservation; and invokes the host method only for finite nonempty source
  systems (n-c-016.tex:1536-1705). The referenced host method and theorem
  are present at
  handbook/parts/p09/logic-in-computer-science.tex:974-1017.
- The source-state and rights boundaries are publication-safe in the text
  reviewed: the Clarke--Emerson reprint is separated from the fuller
  manuscript; the Queille--Sifakis institutional scan is not called
  authorized; ACM's conditional terms are not called an open licence; the
  1999 acquisition-only record supports no body-level claim; and the
  Baier--Katoen all-rights-reserved body is paraphrased rather than presented
  as reusable page content. The relevant bibliography records preserve those
  same boundaries.
- The Clarke--Grumberg--Peled acquisition subsection uses the unacquired book
  only for identity, access state, and contents-page locators. Its sentence
  about the four decision bounds points to
  thm:p09-ctl-star-complexity, whose independent citations are present at
  handbook/parts/p09/logic-in-computer-science.tex:1029-1035; no substantive
  theorem, algorithm, notation, or proof is inferred from acquisition-only
  evidence.

These positive observations are bounded to the exact LaTeX and controlling
text read below. They do not cancel the three must-fixes.

## Text read

Every substantive text range consulted in this round was read directly as
text:

- handbook/parts/p09/presentations/n-c-016.tex:1-2059 (complete file through
  EOF);
- handbook/parts/p09/logic-in-computer-science.tex:930-1060 and
  1485-1525 (including the exact host definitions/theorems, complexity
  theorem, and inclusion site);
- handbook/parts/p08/temporal-epistemic-supplement.tex:42-190;
- spec/research/p09-clarke-emerson-1981-source-note.md:1-884 (complete
  through EOF);
- spec/research/p09-queille-sifakis-1982-source-note.md:1-867 (complete
  through EOF);
- spec/research/p09-emerson-halpern-1986-source-note.md:1-729 (complete
  through EOF);
- spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md:1-470
  (complete through EOF);
- spec/research/p09-baier-katoen-2008-ch6-source-note.md:1-1120 (complete
  through EOF);
- handbook/bib/handbook.bib:2393-2458, 4815-4846, and 4897-4906,
  thereby including every requested relevant bibliography entry and the
  intervening blank separators.

## Prohibitions and non-claims

- No earlier N-c-016 review or report of any round, including this reviewer's
  earlier work, was opened.
- No source-fidelity or mathematical report, admission/board/history file,
  parent conclusion, or other agent output was opened.
- No agent was contacted, inspected, or delegated to.
- No PDF, manuscript render, screenshot, page image, or historical publication
  file was opened or inspected.
- No web source was browsed.
- No TeX or handbook build, test, checker, validator, repository script, hash,
  or executable source tool was run. The evidence collection consisted only
  of direct literal text reads.
- No conclusion about page layout, typography after compilation,
  cross-reference rendering, or PDF appearance is made.
- No claim is made that the unacquired 1999 first-edition body supports any
  mathematical or historical-body assertion.
- No manuscript or repository file other than this Round 8 report was modified
  or reverted.

REGISTER STATUS: OPEN
