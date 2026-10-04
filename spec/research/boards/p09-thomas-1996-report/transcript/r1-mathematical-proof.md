# Round 1 mathematical and proof-correctness report

Seat: mathematical and proof correctness  
Admission question: only the frozen May 1996 report-precursor presentations
`N-c-013.e` and `N-c-014.e`

## Frozen native identities

I independently recomputed SHA-256 on the seven native frozen files before
making a substantive judgment. The results are:

| Frozen object | Independently recomputed SHA-256 | Match |
|---|---|---|
| `tmp/pdfs/p09-thomas-1997/thomas-1997.pdf` | `C8326967AA56B685EC8ED98B0E211EA36773E2644B1BC3B5E368E6F50F28E8AA` | yes |
| `handbook/parts/p09/presentations/n-c-013.tex` | `76480DE7C2620521835DD1301B5D8B5698C60E14AA0B2EFA467D852F81BB36CA` | yes |
| `handbook/parts/p09/presentations/n-c-014.tex` | `F12CD5EDD8D160D91E9A2BC7B68056EF77AB8F2F6FFF5AD4EC474669059CF31B` | yes |
| `handbook/parts/p09/logic-in-computer-science.tex` | `70CFEBC05E1F574703FA6F8B1367C2EBBA1A640A57B2DEEC8D144E88328A7117` | yes |
| `handbook/bib/handbook.bib` | `07233B0722E6DAE89AEE6B34F699BC980D54F4367C2672B4D3B92131F6D680AD` | yes |
| `spec/research/p09-thomas-1996-report-source-note.md` | `B33BF77916C06C57F4896394B4A5569678D75B0B14A940FF451D68D4BD915FB8` | yes |
| `spec/research/p09-source-presentations-lot2-3.md` | `45F8EB339A139C24251616F03A77715337F8E8B8F735956D35B05407D92637C7` | yes |

The controlling PDF was also confirmed as a 478,293-byte, 75-physical-page
object.

## Controlling-source and page-inspection attestation

The hash-pinned PDF itself was the controlling source and was read and judged
directly. Its title, abstract, contents, physical/printed page map, and every
relied-on substantive page were checked in the native object. Searchable text
obtained from that PDF was used only for navigation. No formula, symbol,
wording, pagination claim, or finding was accepted from searchable extraction
alone.

I individually opened and inspected all forty-four chartered renders at
original detail:

- the five identity/page-map displays `inspect-title-01.png`,
  `inspect-title-02.png`, `inspect-title-03.png`,
  `inspect-body-start-04.png`, and `inspect-body-end-75.png`;
- all five substantive displays `page-11.png` through `page-15.png`; and
- all thirty-four substantive displays `page-31.png` through `page-64.png`.

Those PNGs were viewer/display aids derived from the pinned PDF. They did not
substitute for the PDF and carry no independent evidentiary weight. The observed
map is physical page 4 = printed page 1 and physical page 75 = printed page 72;
accordingly, the substantive ranges are physical 11--15 = printed 8--12 and
physical 31--64 = printed 28--61.

I did not run or create a test, test harness, automated checker, repository
script, TeX command, build, interim build, or handbook-PDF inspection.

## Must-fix findings

### TH96-MP-01 — the regular-omega finite-union characterization is absent

- **Severity:** MUST-FIX.
- **Manuscript location:**
  `handbook/parts/p09/presentations/n-c-013.tex`, lines 843--848.
- **Controlling source:** printed p. 30 (physical p. 33), especially the
  paragraph following Proposition 5.3.
- **Defect:** the report states the two-way characterization that an
  omega-language is Buechi-recognizable exactly when it is a finite union of
  sets (U\cdot V^\omega), with (U) and (V) regular finite-word
  languages. The manuscript ends the nondeterministic comparison at
  Proposition 5.3 and moves immediately to the deterministic boundary. Thus
  the H10 statement is not merely compressed: it is missing. The detailed
  record itself notes the source result at
  `spec/research/p09-thomas-1996-report-source-note.md`, lines 131--134, and the
  compact record notes it at
  `spec/research/p09-source-presentations-lot2-3.md`, line 610, so the omission
  is visible across the frozen objects.
- **Required repair:** insert the exact iff characterization between the
  Proposition 5.3 comparison and the deterministic boundary; define the
  (V^\omega) convention so that an infinite concatenation has unbounded total
  length (equivalently, uses nonempty factors after harmless removal of
  epsilon); identify Thomas's report as the source of this survey statement;
  and do not promote it into original-priority evidence.

### TH96-MP-02 — the Safra update has no state for an empty successor image

- **Severity:** MUST-FIX.
- **Manuscript location:**
  `handbook/parts/p09/presentations/n-c-013.tex`, lines 859--875, especially
  lines 870--874.
- **Controlling source:** printed p. 28 for the partial transition relation and
  printed p. 34 for the staged Safra transition (physical pp. 31 and 37).
- **Defect:** Definition 5.1 permits a partial relation
  \(\Delta\subseteq Q\times\Sigma\times Q\). Consequently, advancing the root
  label can produce the empty set. For the one-state automaton with no
  (a)-transition, for example, (a^\omega) has no run and must be rejected,
  but the update from the initial root \(\{q_0\}\) has empty root image. The
  manuscript says to remove empty nodes. Removing the root leaves no object of
  the stated class of finite ordered rooted trees. Retaining an empty root does
  not help: the empty union of its children is not a proper subset of its empty
  label, and a vacuous reading of the collapse test can even mark it. Hence the
  prose does not define a total transition function for the alleged
  deterministic automaton, nor does it prove rejection when the original
  automaton has no continuing run.
- **Required repair:** define the result of an update with empty advanced root
  explicitly. One exact repair is to admit the empty ordered tree as a single
  unmarked absorbing rejecting determinization state, with no live node name
  and membership in no marked-presence component. State and prove that this
  clause preserves rejection of words having no infinite original run and does
  not alter the live-node, name-reservoir, asymptotic state, or pair bounds.

### TH96-MP-03 — breakpoint marks have no specified one-step lifetime

- **Severity:** MUST-FIX.
- **Manuscript location:**
  `handbook/parts/p09/presentations/n-c-013.tex`, line 862 and lines 865--883.
- **Controlling source:** printed pp. 34--35 (physical pp. 37--38), where the
  transition marks a vertical-collapse event and Rabin acceptance requires
  marked presence infinitely often.
- **Defect:** a breakpoint mark is part of a determinization state, but the
  update never says that marks arriving from the preceding state are erased.
  The distinction is proof-critical. Let the original Buechi automaton have
  states (q_0,f,s), final set \(\{f\}\), transitions
  (q_0\mathrel{\xrightarrow a}f),
  (f\mathrel{\xrightarrow b}s), and
  (s\mathrel{\xrightarrow b}s). On (ab^\omega), the state (f) is visited
  only once, so the word is rejected. The Safra root receives a child at that
  visit; on the next update the child and parent both advance to \(\{s\}\), so
  vertical collapse marks the persistent root once. If that incoming mark is
  retained by later updates, the persistent root is marked in every later
  determinization state and the Rabin condition falsely accepts. The intended
  event interpretation is plausible, but it is not an exact state-transition
  definition and cannot be supplied silently.
- **Required repair:** state in the ordered update that all old breakpoint
  marks are cleared while node names persist, and that only vertical collapses
  occurring during the current letter update set marks in the successor state.
  Recheck both acceptance directions using current-step marking, including the
  one-breakpoint counterexample above. Identify the clarification as
  handbook-owned if the report's wording is retained as the source boundary.

### TH96-MP-04 — partial tree transitions invalidate the stated game reduction

- **Severity:** MUST-FIX.
- **Manuscript location:**
  `handbook/parts/p09/presentations/n-c-014.tex`, lines 1454--1465 and
  1500--1524; the downstream uses are at lines 1526--1545.
- **Controlling source:** printed p. 44 for Definition 6.1, printed pp. 47--49
  for the automaton game, and printed pp. 50--51 for Definition 6.10 and
  Example 6.11 (physical pp. 47, 50--52, and 53--54).
- **Defect:** Definition 6.1 permits an arbitrary, hence possibly partial,
  four-place transition relation. If no transition is available at an
  Automaton position, the position has no outgoing edge. But the abstract game
  graph used by Theorem 6.13 expressly requires a nonempty finite outgoing-edge
  set at every vertex, and the strategies and winning conditions are defined
  only through infinite plays. For the chain automaton with initial state
  (q_0) and no transition on the root letter, no global run exists and the
  input tree is rejected; nevertheless, the initial position of
  \(\Gamma_{\mathcal A,t}\) is not a game position to which Theorem 6.8 applies.
  Thus Remark 6.7, the inference from failure of acceptance to a Pathfinder
  winning strategy, and the complement and basis constructions are not proved
  for the tuple actually defined.
- **Required repair:** before forming the game, totalize the chain tree
  automaton in a language-preserving way. Add one fresh state outside every
  displayed (F_i); for each state/letter pair having no transition, add a
  transition sending both children to that state, and add its self-transitions
  for every letter. Prove that every path entering it rejects, so a successful
  run cannot use an added transition, while every game position now has
  nonempty finite outdegree. Then propagate that normalization explicitly
  through Remarks/Theorems 6.7--6.9, the application of Theorem 6.13, the
  finite game in Theorem 6.18, and the S2S decision route. An alternative repair
  would have to define finite-play losses and prove a matching determinacy
  theorem; merely relying on that convention implicitly is insufficient.

## Mandatory invariant dispositions

| Item | Disposition | Mathematical/proof reason |
|---|---|---|
| H01 | PASS | The native object is Thomas's complete May 1996 Kiel Bericht 9607 precursor, not a verified copy of the 1997 chapter; its byte count, extent, and identity agree. |
| H02 | PASS | The abstract's prospective *Handbook of Formal Language Theory* wording and the eventual *Handbook of Formal Languages* identity remain expressly distinct. |
| H03 | PASS | The physical/printed map and every relied-on Section 3.1, 5.1--5.3, and 6.1--6.3 locator agree with the controlling PDF. No final-chapter page is inferred. |
| H04 | PASS | University-course availability is recorded as custody/access only; no Creative Commons or blanket republication right is claimed, and source displays remain research evidence. |
| H05 | PASS | The finite-word tuple, three-place transition relation, length-(n+1) run, initial/final conditions, and effective two-way Theorem 3.1 strength are correct at lines 888--901 of `n-c-014.tex`. |
| H06 | PASS | Disjoint tracks, the separately tested last-letter transition, the rejecting-empty-word guard, the four `MSO0` atomic forms, complement, union, and projection reconstruct printed pp. 8--9 correctly. Direct evaluation at (n=0) confirms why the guard is required. |
| H07 | PASS | `WS1S` uses finite-set-valued monadic variables and input-free successful-run existence; the reversed-binary, finite-carry Presburger paragraph does not exceed printed pp. 10--12. |
| H08 | PASS | The omega tuple, partial three-place transition type, infinite run, and typed recurrence set are stated before the acceptance modes and remain distinct from finite-word and tree automata. An omega-word with no run has no accepting run; TH96-MP-02 concerns the later deterministic-state transition. |
| H09 | PASS | All four conditions are correct, including the source-specific Streett direction: recurrence in (F_i) implies recurrence in (E_i). Empty pair sequences give false Rabin and vacuously true Streett acceptance, as the displayed quantifiers require. |
| H10 | **FAIL — TH96-MP-01** | Example 5.2, Proposition 5.3, and the two deterministic facts are correct, but the required finite-union (U\cdot V^\omega) iff is absent. |
| H11 | PASS | The Safra object has a local necessity argument, a finite ordered state-subset-tree definition, sibling and proper-child-union invariants, determinization-state standing, nonredundancy against subset states, and immediate later use. It is not confused with an input tree or tree-automaton run. |
| H12 | **FAIL — TH96-MP-02, TH96-MP-03** | The listed update order, sibling deletion, name persistence/freshness, live-node bound, and reservoir are otherwise faithful, but the update is not total on an empty root image and does not specify that marks are current-step events. |
| H13 | **FAIL — TH96-MP-02, TH96-MP-03** | Eventual name persistence, infinitely many breakpoint events, the absence/marked-presence Rabin pairs, both proof directions, (2^{O(n\log n)}), (2n) pairs, and the non-(2^{O(n)}) lower-bound qualifier are correctly reported only after the transition and mark-lifetime gaps are repaired. As written, the counterexamples invalidate the claimed acceptance correspondence. |
| H14 | PASS | Theorem 5.9 retains effective two-way strength. The printed Corollary 5.10 defect is visible, and the reachable nonempty cycle meeting (F) is correctly identified as a handbook-owned correction rather than source text. |
| H15 | PASS | The two outer recurrence patterns in Proposition 5.11 and the below-(y) bounds on all inner quantifiers are preserved; weak monadic quantification is correctly finite-set quantification. |
| H16 | PASS | The four-place tree transition relation, global root/child run equations, and \(\exists r\,\forall\pi\) Muller condition are exact. Missing transitions correctly mean that no global run exists. Examples 6.2--6.3 support only the stated Buechi/Muller separation. |
| H17 | PASS | The strict chain and existential path condition are exact. The order-vector with hit is defined as permutation plus former position, has finite-state-memory standing, and is justified by Remark 6.6. A state outside the displayed chain cannot by itself witness any (F_i), so the displayed chain formula rejects a path recurring only outside the chain; no contrary inference is made from the parity gloss. |
| H18 | **FAIL — TH96-MP-04** | Move order, current-position-only standing, and Remark 6.7 are correct when moves exist, but Theorem 6.8 is applied to positions with no guaranteed outgoing edge. |
| H19 | **FAIL — TH96-MP-04** | The local direction functions, transition-sequence universalization, all-path deterministic Muller check, nondeterministic instruction-label guess, and input-tree independence have the right architecture, but the decisive nonacceptance-to-Pathfinder-strategy implication is unavailable at a deadlock. |
| H20 | **FAIL — TH96-MP-04** | The attractor/complementary-subgame induction, finite-game effectivity, regular-tree generator, and empty-language/nonempty-regular-member alternatives are otherwise correctly separated; their applications require a game graph with nonempty outdegree, which has not been established from Definition 6.1. |
| H21 | **FAIL — TH96-MP-04** | The atomic/disjunction/existential/complement translation, existential-run/universal-path converse, input-free decision shape, and later Thomas-versus-Rabin boundary are accurately stated. The proof route is nevertheless incomplete because its complement and basis dependencies invoke the invalid unnormalized game reduction. |
| H22 | **FAIL — TH96-MP-01, TH96-MP-02, TH96-MP-03, TH96-MP-04** | Bibliography, identity, rights, page locators, precursor/final boundary, Thomas/Rabin boundary, and open-review status agree. The frozen records' claims that the operative reconstruction has been supplied cannot support admission while one required source theorem is absent and two determinization updates and the game reduction remain formally incomplete. No prohibited build or test evidence was used. |

## Seat-specific rationale

I reconstructed the finite-word proof in both directions and evaluated the
empty-word case directly. I separately evaluated all four omega acceptance
conditions, including empty accepting sets and empty pair lists, verified the
Streett pair orientation, and reconstructed the nondeterministic comparison and
deterministic complement boundary. That pass exposed TH96-MP-01.

For Safra determinization I tracked label containment, sibling duplicate
removal, node deletion, the predecessor-relative fresh-name rule, persistent
and transient names, current breakpoint events, the Rabin pairs, and both
acceptance directions. Concrete missing-run and one-breakpoint automata expose
TH96-MP-02 and TH96-MP-03; these are definedness and false-acceptance defects,
not stylistic requests. The corrected accepting-cycle criterion for the
input-free Buechi automaton is sound: reachability of a nonempty cycle alone is
insufficient, while a reachable cyclic component meeting (F) is necessary and
sufficient.

For infinite trees I reconstructed the global-run/all-path quantifier order,
the chain condition, the order-vector memory, the Automaton/Pathfinder game,
the finite local-instruction encoding, the determinacy induction, finite-game
effectivity, the regular-tree basis argument, and the MSO/S2S route. Paths whose
recurring states lie outside the displayed chain reject under the actual chain
formula, and the empty tree language causes no false basis witness. The
no-available-transition case, however, prevents the source game from satisfying
the hypothesis of the very determinacy theorem used downstream, yielding
TH96-MP-04.

Because each finding is at least a type/transition-definition failure, a false
acceptance under a literal update, an invalid proof application, or an expressly
required missing theorem-strength statement, the frozen precursor
presentations are not admissible on this round.

VERDICT: REJECT -- TH96-MP-01, TH96-MP-02, TH96-MP-03, TH96-MP-04
