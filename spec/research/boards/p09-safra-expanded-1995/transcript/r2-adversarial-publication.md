# Round 2 adversarial publication and terminology review

## Independence and review objects

I performed a fresh blind review using only the charter and the five frozen
Round 2 objects. I did not inspect a manuscript PDF, PNG, derived source PDF,
test, checker, repository script, TeX command, build, ledger, chair text,
Round 1 report, another Round 2 report, another board, memory, conversation
history, staging material, or web result, and I did not contact another
reviewer.

I read the actual frozen
`handbook/parts/p09/presentations/n-c-013.tex` directly, including the complete
Safra passage through its actual closing line 1034. I also read the actual
frozen `tmp/pdfs/p09-safra-1988/DBA-author-hosted.ps` directly: its raw header
and the text of all twenty declared pages. Direct text extraction was used only
to navigate that same PostScript object; no derived review object was made or
cited.

## Independently recomputed Round 2 identities

| Frozen object | Bytes recomputed | SHA-256 recomputed | Disposition |
|---|---:|---|---|
| `tmp/pdfs/p09-safra-1988/DBA-author-hosted.ps` | 247,788 | `2D492FD28FBCC9FF85E5AA22A62A435D6CB6549DDC00EB5FE8DC7DD82DF6CCD8` | exact match |
| `handbook/parts/p09/presentations/n-c-013.tex` | 59,650 | `4DF89F9A17BC8CE2EF8D1F66C8990BD088BB1AB8BAD1219C926407FB3F9900F8` | exact match |
| `handbook/bib/handbook.bib` | 207,798 | `C085AB2ACA4DDBFF4FA7BBAAD7C01961007962424829C7537A93CFCA0F9201AC` | exact match |
| `spec/research/p09-safra-1988-source-note.md` | 17,649 | `40EAAF3B885CD7AB3DFAD3B2536FE3EB9EEC77077C3BB5849204E0EB598B92A5` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | 238,878 | `4BC69269B9E61BFCE47975F5BA097361F4A844EA3507B321FBFBB8F222DA0D6F` | exact match |

The identity precondition passes for all five objects.

## Findings

### AP-SCOPE-01 — blocker — the controlling admission boundary is contradictory and cuts the reconstruction twice

The charter's standing exact admission question still decides only manuscript
lines 787--1000, and the Round 2 clause expressly says that standing question
remains controlling. The Round 2 table instead calls lines 787--1031 the
complete reconstruction. Neither endpoint is complete in the actual frozen
manuscript:

- lines 999--1001 are one statement of Theorem 1, so the controlling line-1000
  endpoint omits the theorem's state bound completion and exact `n`-pair
  conclusion at line 1001;
- lines 1002--1008 give the lower-bound qualification and Lemma 2 proof-status
  boundary;
- lines 1010--1025 give Corollaries 4, 6, and 7, deterministic-in-the-limit
  standing, and the modal-logic scope limitation; and
- lines 1027--1034 are one cross-presentation and publication-scope paragraph,
  so the Round 2 line-1031 endpoint stops after “both” and omits lines
  1032--1034, including the anti-splicing, non-facsimile, and non-journal
  publication limitations.

The controlling PostScript supplies the affected material at p. 9 (Theorem 1),
pp. 12--13 (bound and lower-bound qualification), pp. 13--16 (applications),
pp. 17--18 (Appendix A's Lemma 2 sketch), pp. 10--11 (Safra's `n`-name and
`n`-pair construction), and p. 20 (the expansion's singular historical journal
wording). This is not a cosmetic locator error: the two charter endpoints
define different admitted propositions, and each excludes required `S14`--`S16`
material.

**Required repair:** replace the exact admission question and the Round 2 table
scope with one explicit complete range, presently manuscript lines 787--1034,
and state unambiguously that it supersedes the historical line-787--1000
question. Because the current seats were commissioned under contradictory
admission objects, begin a fresh blind round under that corrected scope; retain
the five hashes only if none of the five frozen objects changes.

### AP-TERM-01 — must-fix — `non-sink` classifies the target before the distinguished repaired state has standing

At manuscript lines 847--850, “A non-sink determinization state is exactly”
introduces the tree tuple. The distinguished handbook-owned state
`\bot_{\mathrm{dead}}` is not necessitated, defined, or distinguished from the
source's tree states until lines 916--925. Even though “sink” is standard
automata vocabulary, “non-sink” is ambiguous here: it can mean either “not the
distinguished added state” or “not any state with absorbing sink behaviour.” It
therefore fails the local definition-before-use and standing requirements of
the five-part terminology rule.

The source defines all of its printed target states as `(T,l,c)` on p. 10 and
prints empty-label deletion on p. 11; it supplies no sink case. The distinction
is a handbook repair and must be locally owned rather than projected backward
onto the source state definition.

**Required repair:** at lines 847--850 describe these as the source's printed
tree-form states without naming a complementary class, or move the
necessity, exact definition, automaton-state standing, nonredundancy from tree
nodes/source states, and later use of `\bot_{\mathrm{dead}}` to that first
classification location.

### AP-TERM-02 — must-fix — `bad-name set` and `good-name set` are used before their definitions

Manuscript lines 920--924 say that `\bot_{\mathrm{dead}}` belongs to every
“bad-name set below” and no “good-name set.” The formal sets `G_v` and `B_v`
are introduced only at lines 927--936, and those English compound names are
never themselves declared as defined terms. This is an explicit forward use,
not a definition at the same location, and therefore fails the five-part rule's
definition and standing requirements. The need and use are real, but they do
not cure the ordering defect.

The controlling source defines its green `L_v` and red `U_v` Rabin components
on p. 11. The dead-state membership is entirely handbook-owned because the
source has no such state.

**Required repair:** remove the premature set names from lines 923--924 and let
the immediately following displayed definitions establish sink membership, or
move the exact `G_v`/`B_v` definitions to the sink's first mention and state
there that they are target-state subsets, why the new letters are needed, how
they differ from source `L_v`/`U_v`, and how acceptance uses them.

## Five-part terminology audit

I applied the required five tests as: necessity for the distinction; exact
eliminable definition or explicit axiom; standing as a source object, set,
map, relation, state, state family, property, or metalinguistic abbreviation;
nonredundancy from existing terms; and actual later use.

| First-use term or notation | Five-part disposition |
|---|---|
| expanded manuscript, lines 787--802 | passes: needed to separate the unread nine-page proceedings body; identified as the twenty-page author-hosted PostScript; stands as a source object; expressly not the proceedings file or a published journal article; controls all detailed claims |
| ordered `V`-tree, left-to-right relation, and total traversal, lines 837--847 | passes: exact tuple and two relations are given; their distinct comparison domains are stated; the traversal is needed only for deterministic allocation |
| `specific`, lines 858--868 | passes: the source inconsistency necessitates the correction; the inclusive-path formula is exact; it is expressly a metalinguistic label abbreviation rather than a component; it is used for uniqueness and the `n`-node bound |
| `\widehat\delta`, lines 879--888 | passes: the union formula eliminates it, its subset-transition standing is clear, it differs from the point-state transition, and stage 1 uses it |
| `non-sink`, lines 847--850 | fails under AP-TERM-01 |
| `\bot_{\mathrm{dead}}`, lines 916--925 | its eventual definition otherwise passes necessity, state standing, nonredundancy, transition/acceptance effect, and bound use; the first classification order still fails under AP-TERM-01 |
| `bad-name set` / `good-name set`, lines 923--924 | fails under AP-TERM-02 |
| `G_v` and `B_v`, lines 927--940 | their displayed definitions otherwise pass: they are target-state subsets, avoid collision with language notation, correspond without being identical notation to source `L_v,U_v`, and are used in the exact Rabin clause |
| finite factor `\alpha[i,j)`, lines 960--976 | passes: the half-open endpoint convention and finite-word standing precede the soundness use |
| absence symbol `\star`, lines 990--1001 | passes: needed to totalize the source's incomplete label encoding; exactly typed in `f:Q\to N\cup\{\star\}`; expressly not a node or automaton component; differs from live-node values; used in the state bound |
| deterministic in the limit, lines 1014--1021 | passes: defined on accepting runs by finitely many multiple-successor positions; stands as an automaton property; is expressly weaker than full determinism; needed for Corollary 7 |

No hypothetical mathematical entity is named where the text should instead
state an owed artifact. The two failures are local premature classifications,
not pressure to add any new abstraction.

## Mandatory invariant dispositions

- **S01 — PASS on content, FAIL overall through AP-SCOPE-01.** The actual
  247,788-byte PostScript has the frozen hash, `jcss.dvi` header, 21 March 1995
  date, and twenty declared pages. Its p. 1 preliminary-version footnote and
  p. 20 FOCS reference are preserved. The manuscript does not call it the
  proceedings file or a published JCSS article. The exact admitted extent,
  however, remains contradictory.
- **S02 — PASS.** Manuscript lines 787--802, bibliography entries
  `Safra1988`/`Safra1995Extended`, source-note lines 13--62, and compact-record
  lines 596--604 keep DOI, pp. 319--327, abstract strength, and the open
  proceedings-body gap separate from the expansion.
- **S03 — PASS.** Source-note lines 291--305 state research access but no
  open-content or republication licence; the reconstruction is independent
  prose with bounded locators and no render treated as evidence.
- **S04 — PASS.** Manuscript lines 804--827 type the tuple, set-valued
  transition, initial state, run, infinity set, Buechi condition, Muller family
  membership, and total single-valued deterministic target convention. The
  input's possible empty successor set is explicit. Source pp. 2--4 and the
  empty transitions used on p. 18 support the dispositions.
- **S05 — PASS.** Lines 828--834 preserve source `(L_i,U_i)` as recurring-good
  then eventually-absent-bad and expressly bar exchange with Thomas. Source
  pp. 2 and 4 agree.
- **S06 — PASS.** Lines 836--871 give `T=(N,r,p,S)`, an `n`-element vocabulary,
  node labels, total colors, both label invariants, first-divergence
  left-to-right order, ancestor-first total traversal, inclusive-path
  specificity, and distinct node/label/color standings. The strict-ancestor
  correction is expressly handbook-owned against source pp. 9--10.
- **S07 — PASS.** Lines 873--877 give the one-node `{q_0}` all-white source
  state and own only the least-root representative. Source p. 10 agrees.
- **S08 — PASS.** Lines 879--903 preserve the source pp. 10--11 order: advance
  labels; create youngest accepting-subset children; retain the leftmost
  duplicate path; delete empty labels; collapse descendants and color green,
  white, or red; then rename surviving temporary nodes.
- **S09 — PASS.** Lines 837--847 and 900--914 use the fixed vocabulary order,
  one ancestor-first traversal, and least unused names to turn the source's
  “some” choice into one function. Specificity proves at most `n` survivors;
  creation-state red and persistent-name colors agree with source pp. 10--11.
- **S10 — FAIL under AP-TERM-01 and AP-TERM-02; mathematical repair otherwise
  exact.** Lines 916--925 correctly own the empty-root omission, give the
  absorbing target-state standing, total loop, rejecting pair membership,
  language effect, and unchanged asymptotic bound. The terminology order used
  to distinguish and classify that state is not admissible.
- **S11 — PASS on the displayed definitions.** Lines 927--941 define one
  green and one red target-state subset per vocabulary name, include the dead
  state only in every bad component, and obtain eventual-red/infinite-green
  acceptance with exactly `n` pairs, as on source p. 11. AP-TERM-02 concerns
  the two-line premature prose use, not these formulas.
- **S12 — PASS.** Lines 960--977 define the half-open finite factor before use,
  orient predecessor choices from successive green-label levels, apply
  finite-branching Koenig, and concatenate accepting segments consistently
  with source pp. 11--12.
- **S13 — PASS.** Lines 979--988 retain root representation, only finitely many
  moves to older siblings, descent through non-infinitely-green nodes, bounded
  depth, persistent names, and the eventual-red/infinite-green witness from
  source p. 12.
- **S14 — PASS on content, FAIL overall through AP-SCOPE-01.** Lines 990--1008
  totalize the source p. 12 label encoding with a typed outside value, preserve
  `2^(O(n log n))`, state Theorem 1 without class abbreviations, give exactly
  `n` pairs, qualify the `n!` lower bound, and identify Lemma 2 as a
  Muller-family-cardinality lower bound with only the pp. 17--18 Appendix A
  sketch. The controlling admission question cuts this material at line 1000.
- **S15 — PASS on content, FAIL overall through AP-SCOPE-01.** Lines 1010--1025
  give the correct Corollary 4 target and `n+1` pairs, Corollary 6 target,
  accepting-run definition and partial standing for Corollary 7 with `O(3^n)`,
  and bounded modal-logic consequences from source pp. 13--16. The standing
  admission question excludes the entire passage.
- **S16 — FAIL under AP-SCOPE-01.** Within the text, Safra's `n` names/`n`
  pairs remain distinct from Thomas's `2n`; source and handbook repairs,
  singular historical wording, rights, conditional review status, and
  nonpublication scope are consistent across the frozen records. But the
  Round 2 table cuts the final cross-presentation paragraph at manuscript line
  1031, and the controlling question cuts it earlier still, so the exact
  admission boundary is not defined.

## Round 2 refinement dispositions

- **Singular historical journal wording (`S01`,`S16`) — PASS.** Manuscript
  lines 795--799, bibliography lines 2352--2357, source-note lines 49--60, and
  compact-record line 598 preserve *Journal of Computer and System Science*,
  exactly as source p. 20 prints it, without normalizing it to the journal's
  usual plural title.
- **Total target, empty input successors, and Muller-family order
  (`S04`,`S10`,`S16`) — PASS on substance.** Lines 813--827 distinguish
  `|delta(q,a)|=1` from the input's empty-successor possibility and define
  Muller membership before the family-size statement at lines 1004--1007.
  The terminology defects in the handbook-owned sink remain AP-TERM-01 and
  AP-TERM-02.
- **Strict-ancestor inconsistency and deterministic allocation
  (`S06`,`S09`) — PASS.** Lines 841--868 and 900--907 give inclusive-path
  specificity, first-divergence left-to-right comparison, ancestor-first total
  traversal, corrective ownership, and a single least-free-name function.
- **Finite-factor endpoint (`S12`) — PASS.** Lines 960--971 define
  `alpha[i,j)` before the soundness segment is used; source pp. 11--12 agree.
- **Total label encoding and result strength (`S14`) — PASS on substance.**
  Lines 990--1008 give the total typed map with an extra value that is neither
  node nor component, the required asymptotic bound, an unabbreviated Theorem
  1, and Lemma 2's family-cardinality/Appendix-sketch boundary. AP-SCOPE-01
  prevents admission of the complete passage.
- **Deterministic in the limit (`S15`) — PASS on substance.** Lines 1014--1021
  give exactly the accepting-run/finitely-many-multiple-successor condition and
  distinguish it from full determinism. AP-SCOPE-01 excludes it from the
  controlling admission range.
- **Breakpoint terminology and exact result inventory (`S16`) — PASS on
  wording, FAIL on scope.** No unnecessary breakpoint term occurs in the Safra
  reconstruction or its detailed note/compact Safra record. Source-note lines
  64--65 correctly enumerate Theorem 1; Lemmas 2, 3, and 5; Corollaries 4, 6,
  and 7, matching source pp. 9 and 13--18. AP-SCOPE-01 nevertheless makes the
  actual admitted result inventory indeterminate.

## Seat-specific rationale

The frozen scholarly content is unusually careful about the proceedings versus
expansion boundary, source-versus-handbook repairs, Safra-versus-Thomas
notation, proof-versus-sketch status, rights, and conditional review status.
The five identities also match exactly. Publication admission still fails,
because the board names two different and both syntactically incomplete text
ranges, and the manuscript twice uses repaired-state terminology before the
required local standing and definitions. These are not mathematical requests
for new machinery; they require only one exact scope and local reordering or
deletion of premature names.

VERDICT: REJECT -- AP-SCOPE-01, AP-TERM-01, AP-TERM-02
