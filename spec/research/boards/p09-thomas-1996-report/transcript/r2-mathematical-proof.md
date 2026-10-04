# Round 2 mathematical and proof-correctness report

## Independence, scope, and evidence

I conducted this seat as a fresh blind review. I read the charter completely
before substantive judgment. I did not read `ledger.md`, `transcript/chair.md`,
any Round 1 report, another Round 2 report, another board or transcript,
conversation history, memory, staging material, retained PNG/source renders, or
web results, and I did not contact another reviewer.

I read the actual frozen manuscript LaTeX passages in full:

- `handbook/parts/p09/presentations/n-c-013.tex`, lines 800--956;
- `handbook/parts/p09/presentations/n-c-014.tex`, lines 888--927 and
  1451--1596; and
- the controlling cross-file passages of
  `handbook/parts/p09/logic-in-computer-science.tex`, especially lines 25--42,
  721--762, 814--828, 843--846, and 2348--2356.

I also read the Thomas bibliography entries, the complete detailed Thomas
source note, and the compact record's scope rule, both Thomas entries, and
consolidated open-status ledger. The actual hash-pinned source PDF controlled
every source judgment. I inspected physical pages 1--4 and 75 for identity,
version, abstract/title distinction, contents, and page mapping, and printed
pp. 8--12 and 28--61 for the mathematics. The mandatory Round 2 repair pages
were therefore all included: printed pp. 30; 28 and 34--35; and 44 and 47--51.
The physical/printed map was confirmed as physical page 4 = printed p. 1 and
physical page 75 = printed p. 72. Page views were made directly from the pinned
PDF without retaining a derived source-render file; no retained render carried
evidentiary weight.

No test, test harness, automated checker, repository script, TeX command,
interim build, handbook-PDF inspection, rendered-handbook inspection, or build
was used.

## Independently recomputed native SHA-256 identities

| Frozen Round 2 object | Recomputed SHA-256 | Disposition |
|---|---|---|
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` | matches |
| `handbook/parts/p09/presentations/n-c-013.tex` | `F3473BB8C2D77A56D82C7086888CD9087AE887847ED3FDA021DC6826868C25E3` | matches |
| `handbook/parts/p09/presentations/n-c-014.tex` | `F9576BB10063037CDFD9018E6DC7DFB553651590FB74FC77D2D33EEBBF4D5915` | matches |
| `handbook/parts/p09/logic-in-computer-science.tex` | `70CFEBC05E1F574703FA6F8B1367C2EBBA1A640A57B2DEEC8D144E88328A7117` | matches |
| `handbook/bib/handbook.bib` | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` | matches |
| `spec/research/p09-thomas-1996-report-source-note.md` | `3F63E37FE1E7C72140080302E3BDFA716D617A8E73BA157F0D12977041093681` | matches |
| `spec/research/p09-source-presentations-lot2-3.md` | `B43F11B230E9CFF763CAE106A91CDA29122305B02F4CA621E60BD4E63D253208` | matches |

## Finding

### R2-MP-01 — must-fix — deterministic Muller complementation lacks the source's total-transition premise

- **Frozen manuscript lines:**
  `handbook/parts/p09/presentations/n-c-013.tex:803-815` and `:863-867`.
- **Frozen record lines:**
  `spec/research/p09-thomas-1996-report-source-note.md:118-143` and
  `spec/research/p09-source-presentations-lot2-3.md:610`.
- **Controlling source pages:** printed pp. 28 and 31.

Printed p. 28 does more than give the nondeterministic transition relation: it
states that a deterministic automaton replaces that relation by a transition
function
\(
  \delta:Q\times\Sigma\to Q
\)
and hence has the corresponding unique infinite run. That totality premise is
what makes the printed p. 31 Muller-complement step valid by replacing
\(\mathcal F\) with \(\mathcal P(Q)\setminus\mathcal F\).

The frozen Thomas passage types only
\(\Delta\subseteq Q\times\Sigma\times Q\) and a run of that relation at lines
803--815, then at lines 863--867 asserts deterministic Muller closure under
complement solely by replacing the Muller family. It never states the source's
total deterministic transition function or otherwise excludes a missing run.
This is not harmless under the expressly required missing-run stress test. Let
\(Q=\{q_0\}\), \(\Sigma=\{a\}\), and let the transition relation be empty. On
the partial-functional reading, \(a^\omega\) has no run, so it is rejected both
before and after the Muller family is complemented. The second automaton
therefore does not recognize the complement of the first language.

**Required repair:** immediately after the general run definition, add Thomas's
printed deterministic clause with the total type
\(\delta:Q\times\Sigma\to Q\) and the unique-run equation
\(r(i+1)=\delta(r(i),\alpha(i))\). Reconcile the detailed and compact records so
that their account of the deterministic boundary carries the same premise.
This is the smallest source-faithful repair; no new construction is needed.

## Mandatory invariant dispositions

- **H01 — PASS.** The pinned object is Wolfgang Thomas, *Languages, Automata,
  and Logic*, Bericht 9607, Kiel, May 1996, 478,293 bytes and 75 physical pages,
  at the required hash. It is identified as a complete report precursor, not a
  verified 1997-chapter facsimile.
- **H02 — PASS.** The report abstract's prospective *Handbook of Formal
  Language Theory* is kept distinct from the final *Handbook of Formal
  Languages* identity.
- **H03 — PASS.** The physical-to-printed map, section boundaries, and relied-on
  locators agree with the PDF. No final-chapter locator is inferred.
- **H04 — PASS.** Public course access is not promoted to a licence. The
  detailed note ultimately states that the PDF is research evidence and derived
  page images are disposable viewer aids with no independent evidentiary
  weight or asset standing.
- **H05 — PASS.** The finite-word tuple, three-place transition relation,
  length-\(n+1\) run, start, final state, and effective two-way Theorem 3.1
  strength match printed p. 8.
- **H06 — PASS.** The state tracks are disjoint, the final-letter transition is
  separated, the empty-word guard has the correct polarity, the four
  \(\operatorname{MSO}_0\) atom families are exact, and complement, union, and
  projection have the right logical roles on printed pp. 8--9.
- **H07 — PASS.** Weak monadic variables range over finite sets; the input-free
  finite automaton is used by successful-run existence; and the reversed-binary
  finite-carry Presburger account does not exceed printed pp. 10--12.
- **H08 — PASS, subject to H10.** The nondeterministic omega tuple, relation,
  run, and \(\operatorname{In}(r)\) are correctly typed and kept distinct from
  finite-word and tree automata. The omitted deterministic totality premise is
  disposed under H10 because it first becomes theorem-critical there.
- **H09 — PASS.** All four acceptance conditions are correct. In Thomas's
  Streett ordering, recurrence in \(F_i\) implies recurrence in \(E_i\). Empty
  designated sets and empty pair sequences receive the expected displayed
  existential/universal semantics.
- **H10 — FAIL (R2-MP-01).** Example 5.2, Proposition 5.3, the
  \(UV^\omega\) characterization, and the deterministic-Buechi separation have
  the right strength, but deterministic-Muller complementation lacks the
  source's total-transition premise and is false under a missing-run reading.
- **H11 — PASS.** The need beyond reachable subsets is explained before the
  five-part introduction of the Safra tree. Its exact ordered-tree invariants,
  determinization-state standing, difference from input trees and runs, and
  immediate update/acceptance use are supplied.
- **H12 — PASS.** The initial root, youngest accepting children, advancement of
  old and new labels, horizontal deletion, vertical collapse, event marking,
  persistent surviving names, predecessor-relative fresh names, \(n\)-live-node
  bound, and \(1,\ldots,2n\) reservoir are in source order. Horizontal deletion
  resolves duplicate sibling states; the fresh-name rule prevents deletion and
  reuse from joining unrelated lineages.
- **H13 — PASS.** Eventual name persistence, infinitely many current collapse
  marks, the \((E_k,F_k)\) pairs, both acceptance directions, the
  \(2^{O(n\log n)}\) bound, exactly \(2n\) displayed pairs, and the qualified
  Theorems 5.7--5.8 lower bound are correct. Transient names cannot satisfy the
  Rabin pair.
- **H14 — PASS.** Theorem 5.9 is effective in both directions. The printed
  Corollary 5.10 defect is visible, and the reachable nonempty cycle meeting
  \(F\) is correctly owned by the handbook. Empty \(F\), a missing infinite run,
  and reachable nonaccepting cycles all reject.
- **H15 — PASS.** Proposition 5.11 has the correct finite disjunction of
  eventual-absence and recurring-presence tests, with inner quantifiers bounded
  below \(y\); weak monadic quantifiers are explicitly finite-set quantifiers.
- **H16 — PASS.** The tree tuple has the correct four-place relation. One global
  run obeys the root and both-child equations, and acceptance has the essential
  \(\exists r\,\forall\pi\) order. Examples 6.2--6.3 are used only for the stated
  Buechi/Muller separation.
- **H17 — PASS.** The chain is strict and its path formula is exact. The
  order-vector with hit is defined as a last-appearance permutation plus the
  prior position of the newly visited state, stands as finite automaton memory,
  and is made nonredundant by Remark 6.6's recovery of the recurrence set.
- **H18 — PASS.** After the rejecting-state completion, Automaton always chooses
  a transition and Pathfinder then chooses a branch. Acceptance/winning
  equivalence is correct, and memoryless means dependence only on the current
  game position.
- **H19 — PASS.** Local direction functions, universal transition-sequence
  checking along a path, deterministic Muller checking on all paths, and the
  single nondeterministic guess of local instruction labels have the right
  quantifier architecture. The complement automaton is independent of the
  particular input tree.
- **H20 — PASS.** The forced-finite-visit/attractor induction and complementary
  subgames accurately summarize Theorem 6.13; finite-game effectivity is kept
  separate. Regular trees are finite direction generators with output. Input
  guessing, the completed finite game, a memoryless strategy, effective
  emptiness, and the conditional regular-member conclusion are correct. If the
  tree language is empty, no regular member is asserted.
- **H21 — PASS.** The atomic, disjunction, existential, and complemented
  formula-to-automaton steps are correct; the converse has existential run
  tracks followed by a universal path set; and the input-free completed
  emptiness route proves S2S decidability. Thomas's later route is not projected
  onto Rabin's 1969 proof or `N-c-014.d`.
- **H22 — FAIL (R2-MP-01 only).** Bibliography, version, rights, page locators,
  proof ownership, Round 2 status, and narrow completion scope otherwise agree.
  The manuscript and both Thomas records nevertheless omit the theorem-critical
  total deterministic word-transition premise.

## Round 2 repair-invariant dispositions

- **R2-01 — PASS.** The reader gives an exact finite union of
  \(U_jV_j^\omega\), requires regular finite-word factors, and defines infinite
  concatenation by unbounded accumulated length. Empty factors cannot create a
  finite result. Report-precursor rather than priority standing is explicit.
- **R2-02 — PASS.** An empty advanced root enters one precisely defined empty,
  unmarked, absorbing state with no node or name. No original run extends the
  prefix; absorption preserves rejection. It contributes zero live nodes, no
  names, no marked presence, no pair, and only one state, so the live-node,
  reservoir, exact-pair, and asymptotic-state bounds survive.
- **R2-03 — PASS.** Old marks are cleared before each letter update; only a
  collapse in that update marks the successor. The proof now requires
  infinitely many distinct collapse events. Direct reconstruction of the
  \(ab^\omega\) example gives exactly one collapse and rejection.
- **R2-04 — PASS.** The fresh state lies outside every chain set; every missing
  state-letter case goes to it on both children; and it loops on all letters.
  Any run using an added transition has a path eventually constant at that
  state and therefore fails every chain pair. The language and strict chain are
  preserved, all game positions have nonempty finite outdegree, and completion
  is propagated through complement, finite games, the regular-tree basis route,
  and S2S. States outside the displayed chain, including the fresh state, do not
  become accepting merely by recurring.
- **R2-05 — PASS.** The first manuscript use of `Safra tree` has necessity,
  definition, determinization-state standing, nonredundancy, and immediate use.
  Both records say Round 1 rejected, the repaired unchanged-snapshot round is
  open, the final 1997 chapter remains unreconciled, and neither presentation nor
  any broader manuscript unit has been admitted.

## Seat-specific rationale

The finite-word translations, all four omega conditions, Safra invariants and
event semantics, corrected accepting-cycle test, tree completion, game
complement, determinacy induction, regular-tree basis, and S2S route survive the
chartered edge cases. The one remaining defect is logically prior to Muller
complementation: without Thomas's printed total deterministic transition
function, a missing run is rejected by both an automaton and the result of merely
flipping its Muller family. Because that makes an advertised proof step false
under an admitted reading, it is a must-fix and prevents Round 2 admission.

VERDICT: REJECT -- R2-MP-01
