REJECT

# N-c-013 integrated mathematical/proof review — Round 1

## Review basis

I read `handbook/parts/p09/presentations/n-c-013.tex` directly from line 1
through line 1222 and `handbook/parts/p09/logic-in-computer-science.tex`
directly from line 723 through line 915.  I used the five N-c-013 source
records to check mathematical and version boundaries.  I did not inspect a
manuscript PDF, PNG, rendered page, or other manuscript rendering, and I did
not run a build, test, checker, repository script, hash, or automated
validation.  I did not read a prior integrated N-c-013 report or a prior
Safra/Thomas review report.

The snapshot is not mathematically admissible yet.  One construction is not
closed on its declared state space, two pieces of the Vardi--Wolper product
are undefined, and the source-set/start-state convention needed by two host
claims is not supplied.  The McNaughton citation in the host also exceeds the
explicitly preserved evidence boundary.

## Findings

### M1 — Blocker: Thomas's horizontal deletion can destroy the Safra-tree invariant

**Locations:**

- `handbook/parts/p09/presentations/n-c-013.tex:1122-1128`
- `handbook/parts/p09/presentations/n-c-013.tex:1142-1150`

The declared tree-state invariant says that the union of the children labels
is a proper subset of the parent label.  In the update, however, line 1147
says only to delete a duplicated original state from a younger sibling when
it occurs in an older sibling.  It does not delete that state from descendants
of the younger sibling.  Consequently the update need not map a valid tree
state to another valid tree state.

A finite counterexample uses a valid current tree with root label
`{a,b,c,d}`, older-child label `{a}`, younger-child label `{b,c}`, and a child
of that younger child labelled `{c}`.  The two root children are disjoint;
their union `{a,b,c}` is a proper subset of the root; and `{c}` is a proper
subset of `{b,c}`.  Let the Büchi set be empty, so the first update stage adds
no child, and on one letter let

\[
 \delta(a)=\{q\},\qquad
 \delta(b)=\{q,s\},\qquad
 \delta(c)=\{q\},\qquad
 \delta(d)=\{t\}.
\]

After advancement the older child is labelled `{q}`, the younger child
`{q,s}`, and its child `{q}`.  Applying the printed manuscript instruction
removes `q` from the younger sibling, leaving it labelled `{s}`, but leaves
its descendant labelled `{q}`.  The descendant label is then not a subset of
its parent label.  No node is empty and neither of the stated collapse tests
repairs the violation.

**Required correction:** when a state is retained in an older sibling, delete
it from the entire subtree rooted at every younger sibling in which it occurs,
then remove empty nodes before testing the collapse condition.  The manuscript
must state the descendant deletion explicitly; "delete from the younger
sibling" is not a closed transition on the state space defined at lines
1122--1128.

### M2 — Must-fix: the Appendix B product uses two undefined state sets and an unstated counting premise

**Location:** `handbook/parts/p09/presentations/n-c-013.tex:74-124`

Lines 78--96 describe which subsets are local states and which pairs of local
states are consecutive, but lines 107--112 then use `N_L` and `N_\varphi`
without defining either symbol.  In particular, the manuscript never states
that `N_\varphi` is the set of local states containing `\varphi`, even though
that fact is the initial-formula obligation in the construction.  The final
inequality at lines 115--117 also uses
`|e(\varphi)|\le |\varphi|` without stating it.

**Required correction:** define

\[
 N_L=\{u\subseteq cl(\varphi):u\text{ satisfies the displayed local
 conditions}\},\qquad
 N_\varphi=\{u\in N_L:\varphi\in u\},
\]

and state that the until subformulas give
`|e(\varphi)|\le |\varphi|`.  Then the displayed initial set and the
`2^{3|\varphi|}` count follow from named, typed data rather than from symbols
the reader must reconstruct.

### M3 — Must-fix: the source's multiple-start automata are used as one-start automata without the normalization

**Locations:**

- `handbook/parts/p09/presentations/n-c-013.tex:42-60`
- `handbook/parts/p09/presentations/n-c-013.tex:101-124`
- `handbook/parts/p09/presentations/n-c-013.tex:469-498`
- `handbook/parts/p09/presentations/n-c-013.tex:622-632`
- `handbook/parts/p09/logic-in-computer-science.tex:723-756`
- `handbook/parts/p09/logic-in-computer-science.tex:764-790`
- `handbook/parts/p09/logic-in-computer-science.tex:830-840`

Vardi--Wolper's source automaton has a start set `S_0`; its Appendix B product
starts in `N_\varphi\times\{\varnothing\}`.  The handbook's Büchi convention,
reused by the host at line 725, has one initial state, and the model-checking
product at lines 777--784 presupposes a single `q_0`.  The Büchi 1962
translation has the same mismatch: its exact extracted finite data have a
permitted initial set `Q_0`, explicitly contrasted with the handbook's
single-initial-state definition at lines 492--494, but the host theorem calls
the result a Büchi-recognizable language under that handbook definition.

The equivalence is true, but the manuscript does not supply the conversion it
uses.  Add a fresh nonaccepting initial state `q_*`, with no transitions into
it, and put

\[
 \delta_*(q_*,a)=\bigcup_{q\in Q_0}\delta(q,a),
\]

while retaining the old transitions on old states.  On an infinite word the
fresh state occurs only at time zero, so it cannot change the recurrence
condition; the construction adds one state and preserves the language.  The
same clause applies with `S_0` or `N_\varphi` in place of `Q_0`.  This leaves
all asymptotic bounds unchanged and explains exactly why the host's initial
product vertices consume the label of `s_0` before the later edge rule consumes
the label of each successor.  If the exact Appendix B count is mentioned, it
must remain identified as the multiple-start product count before this
one-state normalization, as the host currently says at lines 752--755.

### M4 — Must-fix source boundary: the host citation retrojects unsupported automaton data to McNaughton 1966

**Locations:**

- `handbook/parts/p09/logic-in-computer-science.tex:723-745`
- `handbook/parts/p09/presentations/n-c-013.tex:757-781`

The citation at host line 744 attaches `McNaughton1966` to the paragraph that
defines the handbook's deterministic parity and Rabin tuples and exact
acceptance clauses.  The integrated presentation correctly says that the
McNaughton article body is unavailable and that its alphabet, tuple,
acceptance clause, constructions, examples, proof, and size bounds therefore
remain unestablished.  The contemporary Project MAC report supports only the
narrow omega-event/regular/finite-state equivalence reported at lines
765--773.  A reader cannot tell from the host citation that McNaughton is not
evidence for the displayed tuple and acceptance data.

**Required correction:** remove `McNaughton1966` from the definitional citation
at line 744, which is already supportable from the acquired Thomas precursor,
or move it to a separate historical sentence limited to the narrow registered
result and the explicit unread-body boundary.  Do not leave it attached to
data that the presentation itself says cannot yet be attributed to that
article.

## Coverage found clean apart from M1--M4

### Vardi--Wolper, lines 6--374

- The computation semantics use non-strict until correctly; the run indexing
  and source tuple are internally consistent.
- Local Boolean/next/until consistency is correctly separated from eventuality
  discharge.  Once M2 supplies the missing names and inequality, recurrence of
  the empty obligation set and the `2^{3|\varphi|}` bound are correct.
- The program automaton consumes the label of its current program state.  The
  language-inclusion/negated-formula emptiness equivalence is correct, and the
  worked `Fp` counterexample respects that timing.
- The intersection size, Vardi--Wolper time and space upper bounds, and
  fixed-formula linear structure bound are not conflated with the lower bound.
  The PSPACE lower bound is correctly assigned to Sistla--Clarke's existential
  path problem and transferred to universal satisfaction by negation and
  closure of deterministic polynomial space under complement.
- `ETL_f`, `ETL_l`, and `ETL_r` retain different acceptance standings.  The
  Markov semantics is measure-one rather than universal-path satisfaction;
  probabilistic fairness is a path condition; the Streett implication and the
  `(S,F)` Büchi representation are correct; and the printed opposite-direction
  conversion defect is not promoted to a theorem.
- The restricted probabilistic time bounds and every deferred-proof boundary
  remain qualified at source strength.

### Büchi 1962, lines 375--756

- `SC`, `\Sigma_n`, `\Pi_n`, and `\Sigma_1^\omega` have the correct standings.
  The modern finite-data comparison is explicitly handbook-owned.
- The Sequential Lemma retains the load-bearing quantifier `p<q`; its Ramsey
  argument supports every concatenation between selected cut points.
- The finite-word congruence is two-sided, and the `2^{2m^2}` complement rank
  follows from two binary reachability distinctions for each ordered state
  pair.
- Lemma 10's repeated blocks are correctly required to be nonempty.
- Theorem 1 is stated as the collapse to recurrent existential form without an
  invented modern state-complexity bound.  The converse automaton-to-formula
  coding is mathematically correct once M3 states the harmless start-set
  normalization.
- Lemma 12 correctly requires a finite stem and a nonempty cycle through an
  `L`-state; the finite-state bound supports decidability but no modern
  complexity claim.
- `SC_{\mathrm{fin}}` and `SC_{\mathrm{per}}` remain distinct restricted
  interpreted formalisms.  The source's `Nn` discrepancy, proof referrals,
  proposed axiom schema, and synthesis open problem remain explicit.

### McNaughton, lines 757--781

Apart from the host citation in M4, the presentation does not retroject a
modern tuple, acceptance family, construction, determinacy theorem, or size
bound.  The distinct fallacious game memo is correctly kept separate.

### Safra expanded manuscript, lines 783--1035

- The registered 1988 proceedings paper and the 1995 author-hosted expansion
  remain different source objects.
- Safra's good/bad Rabin-pair order is correct.  The corrected tree order,
  inclusive-path specificity, deterministic name allocation, and rejecting
  sink are eliminable handbook repairs with stated standing.
- The `n`-element persistent vocabulary gives exactly `n` Rabin pairs; the
  absent-state encoding symbol completes the label count without becoming a
  node or automaton component.
- The soundness argument uses recurrent green events and König's lemma; the
  completeness descent uses finitely many left moves and bounded tree depth.
  The `2^{O(n\log n)}` bound and its factorial lower-bound qualification are
  stated at expanded-manuscript strength only.

### Thomas 1996 report and host integration, lines 1036--1222 and 723--915

- Thomas's total deterministic transition premise makes Muller complementation
  sound.  His Rabin and Streett pair order is kept distinct from Safra's.
- The finite-union characterization rules out a finite result from infinitely
  many empty factors by requiring unbounded concatenated length.
- The `2n`-name reservoir, persistent-name condition, current-update mark
  clearing, empty absorbing state, and `2n` Rabin pairs are mutually
  consistent.  The one-mark `ab^\omega` example correctly shows why old marks
  cannot persist.  M1 is the sole defect found in the update itself.
- The repaired input-free Büchi emptiness criterion correctly requires a
  reachable nonempty cycle meeting the Büchi set.
- The host product consumes the initial structure label once, then each target
  structure label once.  Its accepting cyclic-SCC criterion is exact, its
  counterexample lasso is nonempty, and its universal-path theorem has the
  stated PSPACE and fixed-formula strengths.  M3 is required only to connect
  that correct product to the source's multiple-start construction.
- The host `SC` theorem preserves full-set monadic semantics, effective
  recurrent normal form, the modern automata corollary, finite stem--cycle
  decidability, and the absence of a modern complexity bound.

## Disposition

Repair M1--M4 in the actual LaTeX and subject the repaired snapshot to a fresh
mathematical/proof pass.  No change to the historical source files is needed
to resolve these findings.
