# Round 1 mathematical-and-proof review

## Independence and review objects

I reviewed only the board charter and the five frozen Round 1 objects. I read
the actual frozen LaTeX file directly, including the complete Safra passage at
lines 787--1000, and read the actual hash-pinned PostScript source itself. Direct
text extraction was used only to navigate the PostScript's own twenty pages. I
did not inspect a manuscript PDF, PNG, derived source PDF, test, checker,
repository script, TeX command, build, ledger, chair text, another report or
board, staging material, memory, conversation history, or web result.

## Independently recomputed identities

| Frozen object | Bytes | Independently recomputed SHA-256 | Disposition |
|---|---:|---|---|
| `tmp/pdfs/p09-safra-1988/DBA-author-hosted.ps` | 247,788 | `2D492FD28FBCC9FF85E5AA22A62A435D6CB6549DDC00EB5FE8DC7DD82DF6CCD8` | exact match |
| `handbook/parts/p09/presentations/n-c-013.tex` | 57,179 | `7F8B6D07C564D7312FFADC437228C60FC56B80C61A3A6AD7576766FE2E587A7B` | exact match |
| `handbook/bib/handbook.bib` | 207,736 | `05B96387DBE9774BF76B3E5E8B1D5C5D3590CA5B101ADA7CACAB66CE61B15208` | exact match |
| `spec/research/p09-safra-1988-source-note.md` | 15,511 | `A252D489A270D824C0F083B28685F7B17F981331523DB3EE3477AD1273A0F45F` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | 237,009 | `5A1340437E27BA9653747D69BC987C81D8B02D86B68528BCA1A26EEC9E3E7743` | exact match |

The controlling PostScript begins with `%!PS-Adobe-2.0`, has title
`jcss.dvi`, records creation at `Tue Mar 21 15:47:45 1995`, declares
`%%Pages: 20`, and contains twenty ascending `%%Page` comments. Its title-page
footnote identifies `[Saf88]` as a preliminary version, and its page-20
reference identifies `[Saf88]` as the 1988 FOCS paper on pp. 319--327 while
recording the intended extended version.

## Findings

### MP-01 — must-fix — undefined theorem-class notation

- **Invariant:** S14; also the charter's definition-before-use rule.
- **Exact manuscript line:** `handbook/parts/p09/presentations/n-c-013.tex:971--972`.
- **Exact source page:** PostScript p. 4 defines the `N`/`D` and
  `B`/`M`/`R`/`S` class abbreviations and the two-parameter size convention;
  PostScript p. 9 then states Theorem 1 in that notation.
- **Defect:** The frozen reader first uses `NB(n)` and
  `DR(2^{O(n\log n)},n)` in the theorem display but never defines either
  expression in the actual LaTeX file. The surrounding prose lets an expert
  infer the intended theorem, but inference does not give the abbreviations an
  exact standing or define which parameter counts states and which counts
  Rabin pairs.
- **Required repair:** Prefer the existing prose vocabulary and replace the
  display by the fully expanded statement: every nondeterministic Buechi
  automaton with `n` states has an equivalent deterministic Rabin automaton
  with `2^{O(n\log n)}` states and exactly `n` Rabin pairs. Alternatively,
  define both abbreviations and both parameters immediately before the display.

### MP-02 — must-fix — the printed label encoding is not typed for absent states

- **Invariant:** S14.
- **Exact manuscript line:** `handbook/parts/p09/presentations/n-c-013.tex:966--969`.
- **Exact source page:** PostScript p. 12.
- **Defect:** The reader says that the labels are encoded by a function sending
  **each** original state to the node to which it is specific and then counts
  `n^n` functions. An ordinary non-sink tree need not contain every original
  state: the set-valued transition may lose some states while leaving the root
  nonempty. An absent state is specific to no live node, so the displayed total
  function is undefined on it. The PostScript's p. 12 count has the same silent
  omission; repeating it does not supply the missing value.
- **Required repair:** Make the encoding total and label the completion as
  handbook-owned. One exact repair preserves the source's `n^n` bound: when
  `N` is a proper subset of `V`, use the fixed least element of `V\setminus N`
  as the absence code and use live specific nodes for present states; when
  `N=V`, every one of the `n` live nodes has a specific state, so no original
  state can be absent. The simpler alternative is an explicit absence value
  and the bound `(n+1)^n=2^{O(n\log n)}`. Either repair leaves Theorem 1's
  asymptotic state bound unchanged.

### MP-03 — must-fix — partial-determinization standing is omitted

- **Invariant:** S15; also the charter's definition-before-use rule.
- **Exact manuscript line:** `handbook/parts/p09/presentations/n-c-013.tex:985--987`.
- **Exact source page:** PostScript p. 15.
- **Defect:** `deterministic in the limit` is used as the target class of
  Corollary 7 without definition anywhere in the actual LaTeX file. It is not
  ordinary determinism: the PostScript expressly defines it by a condition on
  accepting runs.
- **Required repair:** Before the Corollary 7 statement, say that a Buechi
  automaton is deterministic in the limit exactly when every accepting run
  makes only finitely many nondeterministic transition choices. Then retain the
  equivalent `O(3^n)`-state conclusion and its expanded-manuscript attribution.

## Mandatory invariant dispositions

- **S01 — PASS.** The independently checked source is exactly the 247,788-byte,
  twenty-page `jcss.dvi` PostScript generated on 21 March 1995. The preliminary
  version footnote and `[Saf88]` reference are present. None of the frozen
  objects calls it the nine-page proceedings file or a published JCSS article.
- **S02 — PASS.** The DOI, FOCS pp. 319--327, abstract-level proceedings
  contribution, and still-unread proceedings body remain separate from the
  expanded manuscript's detailed construction, numbering, proofs, and
  applications.
- **S03 — PASS.** The source note treats author/university hosting as research
  access only, records no open-content or republication licence, and limits the
  handbook to independent prose and bounded attribution. No derived render is
  offered as evidence.
- **S04 — PASS.** Lines 803--820 type the finite alphabet, finite state set,
  initial state, set-valued transition, run recurrence, infinity set, and
  Buechi condition before use. Empty successor sets remain possible, which is
  exactly the case later completed by the rejecting sink.
- **S05 — PASS.** Lines 821--827 preserve Safra's order: `L_i` is the
  infinitely recurring good component and `U_i` the eventually absent bad
  component. Lines 993--1000 expressly prevent substitution of Thomas's later
  convention.
- **S06 — PASS.** Lines 829--852 give `T=(N,r,p,S)`, node identities from the
  `n`-element vocabulary, the parent and sibling orders, the label map, total
  color map, proper child-union containment, and non-ancestral disjointness.
  `specific` is given an eliminable label-theoretic standing and is later used
  in the node bound. Nodes, labels, and colors are not conflated.
- **S07 — PASS.** Lines 854--858 preserve the source's one-node `{q_0}` tree
  and all-white colors. Choosing the least vocabulary element is explicitly a
  handbook-owned representative choice and has no acceptance content.
- **S08 — PASS.** Lines 860--883 preserve the six source stages in order:
  advancement; simultaneous youngest accepting-subset creation; leftmost
  horizontal retention; empty deletion; vertical collapse with final
  green/white/red coloring; and fresh renaming. I stress-tested nested collapse
  eligibility: final retention makes eligible old nodes that survive ancestor
  deletion green, retained noneligible old nodes white, and every deleted old
  name red, so a deleted descendant cannot remain green. Temporary children are
  created simultaneously and are pairwise non-ancestral leaves, so the already
  induced left--right order supplies their deterministic enumeration.
- **S09 — PASS.** Lines 885--894 make the source's unused-name choice
  deterministic, preserve old names, make every newly allocated name red in
  its creation state, and justify the `n`-name reservoir from one specific
  original state per surviving node. Immediate reuse of a deleted old name is
  safe because that name is red in the successor state; persistence begins
  only on the next update if its new node survives.
- **S10 — PASS.** Lines 896--905 correctly identify the source omission when
  advancement empties the root and add one explicitly handbook-owned absorbing
  rejecting automaton state. It is neither a node nor a tree, loops on every
  letter, lies in every bad set and no good set, accepts no continuation, adds
  no pair, and changes only the state count by one.
- **S11 — PASS.** Lines 907--921 define one good and one bad set for each of the
  `n` vocabulary names, put the sink in every bad set and no good set, and use
  the exact eventually-nonred/infinitely-green Rabin condition. The conclusion
  is exactly `n` pairs.
- **S12 — PASS.** Lines 937--952 have the correct quantifier direction. At
  successive green positions every next label state has a predecessor in the
  preceding label connected by an input-compatible segment visiting `F`.
  Choosing one predecessor per next-level node gives a rooted, finitely
  branching, infinite predecessor tree; Koenig's lemma gives compatible
  endpoints, and concatenation gives one Buechi run with infinitely many
  accepting visits. Taking `{q_0}` at level zero remains valid even when the
  witness name was allocated later, because its creation label consists of
  accepting states reachable from the root lineage.
- **S13 — PASS.** Lines 954--963 correctly track an accepting run at the root.
  After an ancestor's last green event, the run enters a child at its next
  accepting visit. Horizontal responsibility can move only left among finitely
  many older siblings, after which the carrier survives and its name persists.
  If that carrier is not green infinitely often, the argument repeats below
  it. Strict label containment bounds the depth by `n`, forcing an eventually
  nonred, infinitely green witness.
- **S14 — FAIL (MP-01, MP-02).** The tree-shape and color factors, final
  `2^{O(n\log n)}` state asymptotic, exact `n` pairs, modified-Michel `n!`
  lower bound, constant-in-the-exponent qualification, and Appendix A sketch
  status all match source pp. 12--13 and 17--18. Admission nevertheless fails
  because the theorem notation is undefined and the label-count encoding is
  not total on absent original states.
- **S15 — FAIL (MP-03).** Corollaries 4 and 6 have the right complementary
  targets and `2^{O(n\log n)}` state bounds; Corollary 4 has exactly `n+1`
  pairs. Corollary 7's equivalent Buechi target and `O(3^n)` bound match source
  p. 15, and the modal-logic consequences are not inflated. Its target-class
  standing is nevertheless undefined in the reader.
- **S16 — PASS.** All five objects keep Safra's persistent `n`-name vocabulary
  and `n` pairs separate from Thomas's later `2n` names and `2n` pairs. Source
  ownership, the handbook-owned root/allocation/sink repairs, expanded-
  manuscript terminology, open proceedings reconciliation, pending review
  status, rights boundary, and narrow admission scope agree. No render, test,
  checker, script, command, build, or publication claim is used as evidence.

## Seat-specific rationale

The core determinization is mathematically sound after the explicitly bounded
empty-root completion. Empty successor sets enter the rejecting sink; horizontal
pruning gives merged states to the oldest branch; collapse events and red events
have the right temporal meaning; the fixed allocation rule does not change the
language; and the source's soundness and completeness arguments survive direct
quantifier and edge-orientation checks. The three findings are local and do not
refute Safra's theorem, but each violates a mandatory admission invariant on the
frozen reader: two operative class expressions have no definition, and one
counting map is undefined on a possible kind of input state. All three require a
new frozen snapshot and fresh review.

VERDICT: REJECT -- MP-01, MP-02, MP-03
