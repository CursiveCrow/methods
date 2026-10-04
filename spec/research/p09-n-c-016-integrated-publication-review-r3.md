VERDICT: REJECT

# N-c-016 Round 3 adversarial publication and terminology review

The frozen LaTeX is unusually careful about source state, proof strength, and
the difference between source notation and handbook-supplied bridges.  It is
not yet publication-ready, however, because the following line-specific
definition, hierarchy, and citation defects remain.  Every item below is a
must-fix; no page-layout conclusion is included.

## Must-fix findings

1. **The integrated row label is owned by the Clarke--Emerson subsection, not
   by the five-source N-c-016 presentation.**  In
   `handbook/parts/p09/presentations/n-c-016.tex:3-4`, the source-specific
   heading `Clarke--Emerson's branching-time synthesis presentation` is a
   `\subsection`, and the generic row label
   `sec:p09-presentation-n-c-016` is attached to it.  The Queille--Sifakis,
   Emerson--Halpern, acquisition-boundary, and Baier--Katoen headings at
   lines 474, 813, 1386, and 1409 are peer `\subsection`s with source-specific
   labels.  A reference to the generic N-c-016 anchor therefore denotes and
   displays the Clarke--Emerson subsection rather than an integrated section
   owning all five presentations.  This is a hierarchy and subsection-
   ownership error even though the file is physically contiguous.  **Minimal
   repair:** insert one umbrella `\subsection{CTL, CTL*, and state-labelling
   model checking presentations}` with
   `\label{sec:p09-presentation-n-c-016}` before current line 3; demote the
   five source headings to `\subsubsection`; and replace the current line-4
   label with the symmetric source label
   `sec:p09-presentation-n-c-016-clarke-emerson`.

2. **The alternating-bit notation is used without a reader-facing symbol and
   action declaration, and the glyph `X` changes standing without notice.**
   Lines 489-493 use `X` for the complete IPN vector of program variables.
   Lines 514-525 then use `(X,Y)` for the sender's data/bit pair without
   identifying this second `X` as one program variable rather than that whole
   vector.  The formulas at lines 638-645 and 686-702 additionally use
   `M`, `MM`, `AA`, `B`, `Y`, and the action identifiers `send`, `repeat`,
   `receive`, `sendack`, `repeatack`, `accept`, and `receiveack`; none receives
   an exact standing or definition in the LaTeX before use.  The prose summary
   of four processes does not determine which identifier names which program
   event, and the external Figure 2 is not reproduced.  This fails
   definition-before-use and the technical-name requirements of exact
   definition, standing, nonredundancy, and actual use.  The source note gives
   the missing inventory at
   `spec/research/p09-queille-sifakis-1982-source-note.md:235-267` and
   `:410-428`.  **Minimal repair:** use a distinct metavariable such as
   `\mathbf X` for the IPN's complete variable vector at lines 489-493, and
   insert before the property formulas a compact declaration that `M` is the
   sender's message `(X,Y)`, `MM` its receiver-side copy, `AA` the outgoing
   acknowledgement, `B` the bit projection, and `Y,Z` the sender/receiver
   control bits; declare the uppercase process identifiers and define the
   seven action labels by their displayed-program events (initial send,
   retransmission, message reception, initial/repeated acknowledgement,
   accepted message, and acknowledgement reception).  State there that the
   distinct labels are necessary because `after` and `enable` formulas below
   distinguish those events.

3. **The fourth Queille--Sifakis response formula has been collapsed into a
   table row plus a detached implication, losing its exact Boolean and
   temporal scope.**  Lines 686-698 provide a three-column decomposition;
   lines 700-703 then say that the last source formula “conjoins”
   `after sendack => AA.B=MM.B` without saying whether the conjunction is
   inside `ALL`, inside the consequent of `Init`, or outside either.  The
   source formula recorded at
   `spec/research/p09-queille-sifakis-1982-source-note.md:511-526` is exact and
   has only one correct scope.  **Minimal repair:** replace lines 696-703, or
   immediately supplement them, with the complete formula
   
   \[
   \operatorname{Init}\Rightarrow
   \operatorname{ALL}\Bigl(
     (\operatorname{after}accept\Rightarrow
       \operatorname{INEV}(\operatorname{enable}sendack))
     \land
     (\operatorname{after}sendack\Rightarrow AA.B=MM.B)
   \Bigr).
   \]
   
   Keep the existing `receivack`/`receiveack` defect notice for the second and
   third source formulas; that notice is correct and independent of this scope
   repair.

4. **Union and intersection of predicate transformers are applied before
   they are defined.**  Lines 710-738 type
   `pre`, its Boolean dual, `Id`, composition, and the two finite-iterate
   operators.  The identities at lines 746-755 then form
   `Id \cap (pre \cup \widetilde{pre})` and
   `Id \cup (pre \cap \widetilde{pre})`.  Set union/intersection is already
   defined for transformer *values*, but the LaTeX never defines these
   operations on maps
   `\mathcal P(Q)\to\mathcal P(Q)`.  Calling the iterate definitions
   “Pointwise” at line 729 does not define the two binary transformer
   operations.  The controlling source note explicitly records their
   pointwise standing at
   `spec/research/p09-queille-sifakis-1982-source-note.md:535-552`.
   **Minimal repair:** before the iterate notation, add, for transformers
   `g,h:\mathcal P(Q)\to\mathcal P(Q)`,
   
   \[
     (g\cup h)(P):=g(P)\cup h(P),\qquad
     (g\cap h)(P):=g(P)\cap h(P).
   \]
   
   Then say explicitly that the unions/intersections inside Propositions 1--2
   have this metalinguistic pointwise standing.

5. **The claimed worked CESAR calculation suppresses both the standing of its
   place symbols and the premises used for its final simplification.**  At
   lines 779-789, `s_i`, `r_i`, `m_i`, and `a_i` appear as Boolean factors,
   but the text does not say that each is the characteristic predicate of the
   like-named Figure-2 place; in particular, `a_i` can be mistaken for the
   action-family metavariables used at lines 607-618 and 654-664.  Lines
   791-794 then infer `P_1=true` by “the one-token invariant for each safe
   component” without stating any of the four invariants, so the displayed
   calculation is not checkable from the presentation.  The missing standing
   and exact premises are recorded at
   `spec/research/p09-queille-sifakis-1982-source-note.md:677-719`.
   **Minimal repair:** before current line 779, define each lower-case place
   identifier as the Boolean predicate that its like-named IPN place is
   marked, explicitly distinguish place `a_i` from an action metavariable, and
   display the four source invariants
   
   \[
   \begin{aligned}
   s_1\bar s_2\bar s_3\cup\bar s_1s_2\bar s_3
      \cup\bar s_1\bar s_2s_3&=\mathsf{true},\\
   r_1\bar r_2\bar r_3\cup\bar r_1r_2\bar r_3
      \cup\bar r_1\bar r_2r_3&=\mathsf{true},\\
   m_1\bar m_2\cup\bar m_1m_2&=\mathsf{true},\\
   a_1\bar a_2\cup\bar a_1a_2&=\mathsf{true}.
   \end{aligned}
   \]
   
   These are the premises that make the stated simplification reproducible;
   they are not a new proof-strength claim.

6. **The bibliography drops the suffix in the controlling 1999 book's author
   identity.**  `handbook/bib/handbook.bib:2438-2447` identifies the requested
   first edition, but line 2439 records `Clarke, Edmund M.` rather than
   `Edmund M. Clarke, Jr.`.  The controlling acquisition note gives the
   responsibility statement and formal citation with the suffix at
   `spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md:3-5` and
   `:27-43`.  **Minimal repair:** add `Jr.` to Clarke's BibLaTeX author name
   using the repository's suffix syntax; do not change the edition, year,
   ISBN, or acquisition-only note.

## Bounded positive evidence

- The main locally emphasized technical names do satisfy the supplied rule:
  `synchronization skeleton` and `global system flowgraph` are distinguished
  by object standing and later factorization use at lines 17-36 and 427-458;
  `interpreted Petri net` has a typed eliminable definition, necessity,
  standing, nonredundancy, and later predecessor use at lines 486-502;
  `Init`, `enable`, and `after` receive distinct state-predicate standings and
  later uses at lines 597-605; MPL `stage` is defined and distinguished from a
  state and connective at lines 1285-1291; the handbook bridge `R_0,V_0` is
  explicitly metalinguistic and necessary at lines 1446-1458; and the
  propositional comparison abbreviations are eliminable and scoped at lines
  1703-1715.  Findings 2, 4, and 5 are the remaining local exceptions, not a
  generic demand to add terminology.
- Clarke--Emerson's indexed next operators, strong inclusive until, finite
  model checker, defective printed universal recurrence, tableau outline,
  model fragments, nine mutual-exclusion groups, redundant group 9 under
  totality, `TURN`, and global-to-local factorization are kept distinct and in
  definition-before-use order.  The four proof-status categories at lines
  460-472 do not collapse a printed algorithm, propositions, an abridged
  tableau, and a worked synthesis example into one theorem.
- Queille--Sifakis's incomplete printed execution definition is completed only
  with an explicit handbook/source distinction at lines 555-595; the external
  non-loss assumption is not promoted to fairness; image-finiteness and the
  delegated proofs of Propositions 1--2 remain attached to the result; the
  analyzer's iteration cap is not represented as a proof or total decision
  procedure.
- Emerson--Halpern's state/path types, closure classes, pointwise versus
  model-validity equivalences, fragment hierarchy, printed Theorem 5--6 target
  defects, proof dependencies, MPL `U/X` defects, and theorem-level proof
  omissions are explicitly separated.  The terminal-server example is kept
  as an application argument rather than a dominance theorem.
- The 1999 acquisition-only subsection makes no source-content claim about an
  exact grammar, algorithm, proof, example, or complexity theorem.  Its
  contents-page locations remain locator metadata, and the host theorem's four
  complexity classifications retain independent citations.  No substantive
  claim is carried by acquisition evidence alone.
- Baier--Katoen's action-labelled source tuple is bridged explicitly to the
  host's binary relation; the empty-state boundary, edge-count distinction,
  ENF expansion risk, least/greatest set characterizations, source versus
  handbook proof voice, exact graph computations, time-only complexity claim,
  uniformity gap, CTL/LTL proof omissions, and CTL* typing are all stated with
  the necessary hypotheses and source locators.
- Apart from finding 6, the five presentation bibliography records and the
  four independent host complexity records match the source-note identities
  and do not silently substitute the 2001 chapter, 2018 edition, or another
  source state.

## Explicit non-claims

- This is not a source-fidelity verdict on the inaccessible 1999 book body and
  does not close that acquisition.
- This is not a new mathematical-correctness proof of every stated theorem or
  reconstruction.  It assesses the publication wording, terminology,
  hierarchy, local notation, citations, source boundaries, and proof-status
  voice against the permitted text evidence.
- No claim is made about TeX compilation, generated cross-reference output,
  typography, page breaks, figures, or any other rendered-page property.
- Public or institutional access is not treated as an open licence or as a
  right to redistribute any source body.

## Substantive text read

- `handbook/parts/p09/presentations/n-c-016.tex`: lines 1-1884, directly as
  LaTeX text through EOF.
- `handbook/parts/p09/logic-in-computer-science.tex`: lines 945-1048,
  1505-1507, and 1513-1519 (host definitions/theorems and the actual input
  position).
- `handbook/parts/p08/temporal-epistemic-supplement.tex`: lines 42-190.
- `spec/research/p09-clarke-emerson-1981-source-note.md`: lines 1-884.
- `spec/research/p09-queille-sifakis-1982-source-note.md`: lines 1-867.
- `spec/research/p09-emerson-halpern-1986-source-note.md`: lines 1-729.
- `spec/research/p09-clarke-grumberg-peled-1999-acquisition-note.md`: lines
  1-470.
- `spec/research/p09-baier-katoen-2008-ch6-source-note.md`: lines 1-1120.
- `spec/research/p09-source-presentations-lot2-3.md`: lines 781-847, used only
  for compact source-state and presentation-registration evidence.  Its final
  administrative sentence mentions prior review statuses; that sentence was
  excluded from the verdict and findings, which were derived independently
  from the LaTeX and source notes.
- `handbook/bib/handbook.bib`: lines 2393-2407, 2409-2422, 2424-2436,
  2438-2447, 2449-2458, 4815-4824, 4826-4835, 4837-4846, and 4897-4906.
- `spec/research/p08-new-content.md`: lines 810-830.

## Prohibitions and work boundary observed

- No N-c-016 review report, source-fidelity report, mathematical report,
  board/admission/handoff/history file, parent conclusion, or agent
  communication was opened.  No agent was contacted and no work was
  delegated.  The embedded administrative sentence disclosed in the read-log
  item above was not used as evidence.
- No PDF, manuscript render, screenshot, page image, historical publication
  file, or generated artifact was opened or inspected.
- No TeX build, test, checker, validator, repository/project script, hash, or
  executable source analyzer was run.  Only literal text reads and literal
  text searches were used.
- No web access or external lookup was used.
- No manuscript, bibliography, source note, host file, prerequisite file, or
  other repository work was modified or reverted.  This review file is the
  sole output.
- No page-layout issue or visual-publication conclusion is reported; those
  remain reserved for the final publication gate.

REGISTER STATUS: OPEN
