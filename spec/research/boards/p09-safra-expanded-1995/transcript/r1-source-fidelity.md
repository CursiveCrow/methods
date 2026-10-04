# Round 1 source-fidelity review

## Scope, independence, and source use

I read the charter first and then read only the five frozen objects authorized
by it. I read the actual frozen LaTeX admission passage at
`handbook/parts/p09/presentations/n-c-013.tex:787--1000` directly. I also read
the actual hash-pinned `DBA-author-hosted.ps` through all twenty declared pages;
direct text extraction was used only to navigate that PostScript and was not
treated as another evidence object. I inspected no manuscript PDF, PNG,
derived source PDF, test, checker, repository script, TeX command, or build. I
did not read the chair, ledger, another report or board, conversation history,
memory, staging material, or web results.

## Independently recomputed frozen identities

The five identities were recomputed before substantive judgment.

| Frozen object | Bytes | Independently recomputed SHA-256 | Result |
|---|---:|---|---|
| `tmp/pdfs/p09-safra-1988/DBA-author-hosted.ps` | 247,788 | `2D492FD28FBCC9FF85E5AA22A62A435D6CB6549DDC00EB5FE8DC7DD82DF6CCD8` | matches |
| `handbook/parts/p09/presentations/n-c-013.tex` | 57,179 | `7F8B6D07C564D7312FFADC437228C60FC56B80C61A3A6AD7576766FE2E587A7B` | matches |
| `handbook/bib/handbook.bib` | 207,736 | `05B96387DBE9774BF76B3E5E8B1D5C5D3590CA5B101ADA7CACAB66CE61B15208` | matches |
| `spec/research/p09-safra-1988-source-note.md` | 15,511 | `A252D489A270D824C0F083B28685F7B17F981331523DB3EE3477AD1273A0F45F` | matches |
| `spec/research/p09-source-presentations-lot2-3.md` | 237,009 | `5A1340437E27BA9653747D69BC987C81D8B02D86B68528BCA1A26EEC9E3E7743` | matches |

The controlling PostScript is therefore the stipulated 247,788-byte object.
Its actual header is `%!PS-Adobe-2.0`, gives `%%Title: jcss.dvi`, records
`%%CreationDate: Tue Mar 21 15:47:45 1995`, and declares `%%Pages: 20`. Its
title-page footnote identifies `[Saf88]` as a preliminary version, and its
reference list identifies `[Saf88]` as the 1988 FOCS paper on pp. 319--327.

## Findings

### SF-R1-01 — must-fix — the printed journal title is silently normalized

- **Exact manuscript line:**
  `handbook/parts/p09/presentations/n-c-013.tex:797` says that the source's own
  bibliography names the *Journal of Computer and System Sciences*.
- **Other frozen line:** `handbook/bib/handbook.bib:2355--2356` repeats that
  plural title while describing what the manuscript says. By contrast,
  `spec/research/p09-safra-1988-source-note.md:51--53` preserves the singular
  wording.
- **Exact source page:** actual PostScript p. 19, reference `[Saf88]`, prints
  “An extended version to appear in Journal of Computer and System Science.”
- **Defect:** the LaTeX and bibliography silently correct `Science` to
  `Sciences` while expressly reporting the source's statement. This is a
  source-wording mismatch and a contradiction among frozen records, regardless
  of what the journal's normalized title may be elsewhere.
- **Required repair:** report the singular printed wording exactly, or state
  explicitly that the source prints the singular form and that any plural
  normalization is handbook-owned. Make the LaTeX, bibliography, detailed
  note, and compact record agree.

### SF-R1-02 — must-fix — the source's strict-ancestor defect is repaired without ownership, and the relied-on order is not exact

- **Exact manuscript lines:**
  `handbook/parts/p09/presentations/n-c-013.tex:834--835` invokes the “usual”
  left--right order; lines `845--848` give a corrected path-based definition of
  “specific”; and lines `881--882` then allocate names in undefined “tree
  order.”
- **Other frozen lines:**
  `spec/research/p09-safra-1988-source-note.md:117--130` likewise presents the
  corrected order and specificity clauses as though they were literal source
  definitions. The compact record uses “specific-node label assignments” at
  `spec/research/p09-source-presentations-lot2-3.md:602` without giving the
  relation locally.
- **Exact source pages:** actual PostScript pp. 9--10. Page 9 defines an
  ancestor by `p^k(d_2)=d_1` for `k>0`, so the relation is strict. It then
  defines left-of using ancestors. Page 10 says that `q` is specific to `d` if
  `q` belongs to `d` and does not belong to any node which is not an ancestor
  of `d`. Read with the printed strict definition, `d` itself is not its own
  ancestor, so the literal specificity clause requires both membership and
  nonmembership at `d`. The following parenthetical supplies the evident
  intended root-to-`d` path reading.
- **Defect:** the handbook uses the intended corrected relation, but does not
  disclose or own the correction. It also relies on “tree order” for the
  deterministic allocation repair without identifying it exactly with a
  defined total order on the simultaneously created temporary leaves.
- **Required repair:** record the printed strict-ancestor inconsistency and
  explicitly mark the path-based correction as handbook-owned. Define the
  intended root-to-node path relation including the node itself, define
  left--right order by the first divergent ordered children, and make the
  allocation step use that exact defined order. Align both research records.

### SF-R1-03 — must-fix — the detailed note invents a contiguous lemma range

- **Exact frozen-record line:**
  `spec/research/p09-safra-1988-source-note.md:64--65` says that “Lemmas 2--5”
  were read.
- **Exact source pages:** actual PostScript pp. 13--15 contains Lemma 2,
  Lemma 3, Corollary 4, Lemma 5, Corollary 6, and Corollary 7. There is no
  Lemma 4.
- **Defect:** “Lemmas 2--5” falsely presents the source's mixed result numbering
  as a contiguous lemma sequence and thereby mislabels Corollary 4.
- **Required repair:** replace the range with the exact enumeration “Lemmas 2,
  3, and 5” while retaining Corollaries 4, 6, and 7 separately.

### SF-R1-04 — must-fix — “deterministic in the limit” is used without the source's definition

- **Exact manuscript line:**
  `handbook/parts/p09/presentations/n-c-013.tex:986` first and only uses
  “deterministic in the limit” without defining it. The same omission occurs at
  `spec/research/p09-safra-1988-source-note.md:226--227` and
  `spec/research/p09-source-presentations-lot2-3.md:602`.
- **Exact source page:** actual PostScript p. 15, immediately before
  Corollary 7, defines an automaton to be deterministic in the limit when every
  accepting run makes only finitely many nondeterministic choices.
- **Defect:** the omitted definition loses the exact standing and the
  distinction from full determinism that makes Corollary 7 a partial, rather
  than complete, determinization result.
- **Required repair:** before the term is used, give the source's exact
  accepting-run/finitely-many-nondeterministic-choices definition, state that it
  is a property of an automaton, distinguish it from full determinism, and then
  state Corollary 7. Align both research records.

### SF-R1-05 — must-fix — Theorem 1's source class notation is undefined in the LaTeX

- **Exact manuscript lines:**
  `handbook/parts/p09/presentations/n-c-013.tex:969--973` displays
  `NB(n) -> DR(2^(O(n log n)),n)` without defining `NB` or the two arguments of
  `DR`. These abbreviations occur nowhere else in the frozen LaTeX file. The
  compact record repeats them at
  `spec/research/p09-source-presentations-lot2-3.md:602` without a local
  definition. The detailed note does define them at lines `106--107`, which
  makes the cross-file omission especially clear.
- **Exact source page:** actual PostScript p. 4 defines `N`/`D` for
  nondeterministic/deterministic and `B`/`M`/`R`/`S` for the four acceptance
  classes, explains that automaton size records states and acceptance-condition
  size (with Büchi's condition neglected), and uses `DR(state count, pair
  count)`.
- **Defect:** the displayed theorem introduces technical class notation without
  its source standing or parameter meanings. Nearby prose does not eliminate
  the ambiguity between a state count and a pair count.
- **Required repair:** define `NB(n)` locally as the class of `n`-state
  nondeterministic Büchi automata and `DR(m,h)` locally as the class of
  deterministic Rabin automata with `m` states and `h` accepting pairs, then use
  the display. Give the compact record an eliminable local expansion or avoid
  the unexplained abbreviations there.

## Mandatory invariant dispositions

| Item | Disposition | Source-fidelity rationale |
|---|---|---|
| **S01** | **Not satisfied — SF-R1-01** | All byte, hash, header, page-count, date, footnote, and FOCS-reference facts match, but the source's printed journal-title wording is silently changed in two frozen objects. |
| **S02** | Satisfied | The DOI, pp. 319--327 proceedings identity, abstract-level contribution, unread nine-page body, and twenty-page expansion are kept separate. Detailed numbering and construction claims are assigned only to the expansion. |
| **S03** | Satisfied | The records claim research access, not an open-content licence; the LaTeX is independent exposition; and no render or derived file is offered as evidence. |
| **S04** | Satisfied | The actual p. 4 tuple, set-valued transition, initial state, run recurrence, infinity-set meaning, and Büchi clause are faithfully typed. Empty successor sets remain possible and motivate the separately owned sink. |
| **S05** | Satisfied | The LaTeX preserves Safra's actual `L_i` recurring/good and `U_i` eventually absent/bad order from pp. 2 and 4 and warns against importing Thomas's notation. |
| **S06** | **Not satisfied — SF-R1-02** | The tuple, labels, colors, containment, disjointness, and standing distinctions otherwise match pp. 9--10, but the source's strict-ancestor/specificity inconsistency is silently repaired and the relied-on left--right order is not exactly defined. |
| **S07** | Satisfied | The one-node `{q0}` tree and all-white colors match p. 10. Choosing the least root name is expressly handbook-owned and confined to making the deterministic state literal. |
| **S08** | Satisfied | Lines 867--883 preserve pp. 10--11's six stages, including simultaneous accepting-child creation, leftmost duplicate retention, empty-node deletion, old-node collapse/coloring, and final renaming. |
| **S09** | **Not satisfied — SF-R1-02** | The `n`-node argument, color timing, persistent old names, and source/handbook allocation boundary match p. 11, but “tree order” is not an exact defined deterministic enumeration until SF-R1-02 is repaired. |
| **S10** | Satisfied | The one rejecting absorbing automaton state is clearly handbook-owned, is reached exactly on an empty advanced root, loops, lies in every bad set and no good set, preserves rejection, and adds only one state without changing the asymptotic bound. |
| **S11** | Satisfied | Green/good and red/bad sets, sink membership, eventual-red/infinite-green semantics, and exactly `n` pairs match p. 11 after the explicit sink completion. |
| **S12** | Satisfied | Lines 937--952 faithfully track pp. 11--12's successive green positions, accepting finite segments, predecessor tree, König step, and concatenated Büchi run. No source-attributed proof step is reversed. |
| **S13** | Satisfied | Lines 954--963 faithfully track p. 12's root representation, finite moves to older siblings, descent, bounded depth, persistence, and final infinitely-green/eventually-nonred witness. |
| **S14** | **Not satisfied — SF-R1-03, SF-R1-05** | The p. 12 count, exact `n` pairs, p. 13 `n!` qualifier, and Appendix A sketch status otherwise match, but Theorem 1's class notation is undefined and the detailed note misstates the numbered lemma sequence. |
| **S15** | **Not satisfied — SF-R1-03, SF-R1-04** | Corollaries 4 and 6 have the correct classes and bounds, and Corollary 7 has the correct `O(3^n)` target, but its defining partial-determinization property is omitted; the detailed note also misstates the surrounding result numbering. |
| **S16** | **Not satisfied — SF-R1-01 through SF-R1-05** | The Safra `n`-name/`n`-pair presentation is kept separate from Thomas's later `2n` presentation, and review/publication scope remains narrow, but the five frozen files do not yet agree exactly on source wording, source-owned versus handbook-owned repair, result numbering, or local terminology standing. |

## Seat-specific rationale

The automaton tuple, Rabin orientation, six-stage update, color map, sink
ownership, correctness-proof synopsis, asymptotic result, lower-bound qualifier,
applications, rights boundary, and Safra/Thomas split are substantially faithful
to the actual PostScript. Admission nevertheless fails on this unchanged
snapshot because the charter makes a silent source correction, a source
mismatch, an incorrect result number, and an undefined relied-on technical term
at least must-fix. The five findings above require a changed snapshot and a new
blind round.

VERDICT: REJECT -- SF-R1-01, SF-R1-02, SF-R1-03, SF-R1-04, SF-R1-05
