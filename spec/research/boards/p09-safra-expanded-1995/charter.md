# Board charter: Safra author-hosted expanded manuscript for `N-c-013.d`

- Artifact: the five-object frozen Round 1 snapshot below.
- Purpose: determine whether the handbook's reconstruction of Shmuel Safra's
  author-hosted expanded manuscript may be admitted at explicit expanded-
  manuscript strength.
- Mode: review.
- Requested by: the standing requirement that completed handbook topics
  receive three independent blind scholarly reviews before admission.
- Authorship disclosure: chair-authored reconstruction. No seated reviewer
  authored a frozen object.
- Severity taxonomy: blocker, must-fix, should-fix, consider, discard,
  unresolved-user.
- Source rule: reviewers must read the actual frozen manuscript LaTeX and the
  actual hash-pinned PostScript source. No manuscript PDF, PNG page render,
  derived source PDF, test, checker, script, TeX command, or build is a review
  object or carries independent evidence.
- Consensus rule: admission requires three `VERDICT: ACCEPT` reports on one
  unchanged frozen snapshot and no unresolved blocker or must-fix. A supported
  finding cannot be outvoted.
- Board type: live.
- Workspace: `spec/research/boards/p09-safra-expanded-1995/`.

## Frozen Round 1 snapshot

No frozen object may be edited while the round is open. Any content or status
edit invalidates every verdict and requires a new hash-pinned blind round.

| Artifact | Review scope | SHA-256 |
|---|---|---|
| `tmp/pdfs/p09-safra-1988/DBA-author-hosted.ps` | complete controlling twenty-page author-hosted expanded manuscript | `2D492FD28FBCC9FF85E5AA22A62A435D6CB6549DDC00EB5FE8DC7DD82DF6CCD8` |
| `handbook/parts/p09/presentations/n-c-013.tex` | whole-file identity; substantively lines 787--1000, the complete Safra proceedings/expansion boundary and expanded-manuscript reconstruction | `7F8B6D07C564D7312FFADC437228C60FC56B80C61A3A6AD7576766FE2E587A7B` |
| `handbook/bib/handbook.bib` | whole-file identity; especially `Safra1988` and `Safra1995Extended` | `05B96387DBE9774BF76B3E5E8B1D5C5D3590CA5B101ADA7CACAB66CE61B15208` |
| `spec/research/p09-safra-1988-source-note.md` | complete identity, access, version, mathematical, repair, rights, custody, and scope record | `A252D489A270D824C0F083B28685F7B17F981331523DB3EE3477AD1273A0F45F` |
| `spec/research/p09-source-presentations-lot2-3.md` | whole-file identity; especially `N-c-013.d` and the consolidated open-status ledger | `5A1340437E27BA9653747D69BC987C81D8B02D86B68528BCA1A26EEC9E3E7743` |

Every reviewer must independently recompute and report all five identities
before substantive judgment.

## Controlling source and version boundary

The source is the actual PostScript file above. Its header says `jcss.dvi`,
records generation on 21 March 1995, and declares twenty pages. The title-page
footnote says a preliminary version appeared as `[Saf88]`; the reference list
identifies that preliminary version as the 1988 FOCS paper. The registered
nine-page FOCS version of record remains unacquired. Detailed claims may be
accepted only as claims about the author-hosted expansion.

The PostScript itself controls wording, formulae, colors, transition order,
theorem numbering, proof status, and version evidence. Reviewers may use direct
text extraction to navigate its pages, but a derived file cannot replace the
actual `.ps` identity or be cited as independent evidence. The drawn examples
are summarized in the reader text only at the level stated in the prose; no
edge-by-edge reproduction is under review.

## Exact admission question

The board decides only whether the complete Safra subsubsection of
`handbook/parts/p09/presentations/n-c-013.tex` may be admitted as expanded-
manuscript content for `N-c-013.d`, together with its two bibliography entries
and two research records.  The semantic boundary begins with the Safra
subsubsection heading and ends with its final paragraph immediately before the
Thomas subsubsection heading.  The latest frozen-round table records the exact
current line interval.  This semantic boundary supersedes the historical
Round 1 endpoint at line 1000 and Round 2 endpoint at line 1031, both of which
were rejected because they cut the subsection before its end.

An ACCEPT does not acquire or reconcile the nine-page FOCS body; admit
McNaughton 1966, Thomas 1997, `N-c-013` overall, Part IX, another part, a
manuscript PDF, a build, human or user review, the book, or publication.

## Mandatory invariant checklist

The identifiers `S01`--`S16` are review labels, not mathematical terminology.
Every reviewer must dispose of every item expressly.

- **S01 -- identity and version.** The controlling source must be the
  247,788-byte PostScript with the frozen hash, twenty declared pages,
  `jcss.dvi` header, 21 March 1995 generation date, preliminary-version
  footnote, and FOCS reference. It must not be called the nine-page proceedings
  file or a published JCSS article.
- **S02 -- registered-work boundary.** The 1988 DOI, pages, abstract-level
  contribution, and continuing proceedings-body gap must remain separate from
  the expansion's detailed content and numbering.
- **S03 -- custody and rights.** Author/university hosting permits research
  access but must not be promoted to an open-content or republication licence.
  The handbook must use independent prose and must not treat derived renders as
  evidence.
- **S04 -- automaton, run, and infinity set.** The source tuple, transition
  type, initial state, run recurrence, infinity set, and Büchi condition must be
  typed and correct before use. Missing transitions must remain possible.
- **S05 -- Rabin and Streett pair order.** Safra's `(L_i,U_i)` convention must
  make `L_i` recurring/good and `U_i` eventually absent/bad. It must not be
  silently exchanged with Thomas's notation.
- **S06 -- tree state standing.** `T=(N,r,p,S)`, the `n`-element vocabulary,
  label map, total color map, proper child-union containment, disjointness of
  non-ancestral labels, left--right order, and specific-state abbreviation must
  be exact. Node identity, labels, and colors must remain distinct standings.
- **S07 -- initial representative.** The source's one-node `{q0}` tree and
  all-white colors must be present. Fixing one vocabulary element as root must
  be expressly handbook-owned and used only to make the deterministic state
  literal.
- **S08 -- six-stage update.** Label advancement, youngest accepting-subset
  child creation, leftmost horizontal duplicate retention, empty-label
  deletion, vertical collapse/green coloring, white/red coloring, and fresh
  renaming must appear in source order with the correct objects and types.
- **S09 -- deterministic allocation and name reservoir.** The source's “some
  unused name” must receive an explicit handbook-owned deterministic choice.
  The specific-state argument must justify at most `n` surviving nodes and the
  `n`-name reservoir. Creation-state red coloring and later name persistence
  must agree with the printed color map.
- **S10 -- empty-root completion.** Because `delta(q,a)` may be empty, the
  printed deletion sequence can remove the root. The handbook-owned absorbing
  rejecting state must have exact standing, transition, pair membership,
  language effect, and bound effect. It must not be attributed to the source.
- **S11 -- acceptance pairs.** For every vocabulary name, the green and red
  state sets, sink treatment, eventual-red/infinite-green condition, and exact
  `n`-pair conclusion must be correct.
- **S12 -- soundness.** Successive green positions, label-to-label accepting
  segments, the finitely branching predecessor tree, König's lemma, and
  concatenated Büchi run must form a valid proof without reversing an edge or
  quantifier.
- **S13 -- completeness.** Representation of an accepting run at the root,
  eventual settling under an older sibling, descent through non-green nodes,
  bounded depth, name persistence, and the final Rabin witness must form a
  valid proof.
- **S14 -- state count and optimality.** Tree-shape count, specific-node label
  encoding, colors, `2^(O(n log n))` state count, exact `n` pair count, `n!`
  lower-bound citation, and “up to a constant in the exponent” qualification
  must match the source. Lemma 2's appendix argument must remain a sketch.
- **S15 -- applications.** Corollaries 4, 6, and 7 must have the right source
  and target automaton classes, state bounds, pair count, and partial-
  determinization standing. Modal-logic consequences must not be inflated.
- **S16 -- cross-presentation and publication scope.** Safra's `n` vocabulary
  names/`n` pairs must remain separate from Thomas's later `2n` names/`2n`
  pairs. All five files must agree on source ownership, repair ownership,
  terminology, open proceedings reconciliation, review status, and the narrow
  admission boundary. No manuscript render, test, checker, script, TeX command,
  interim build, or final-publication claim may appear as evidence.

## Seat mandates

### Source fidelity and evidence

Audit the actual PostScript against every source-attributed statement in the
actual LaTeX, bibliography, detailed note, and compact record. Check identity,
version, page locators, tuple components, terminology, colors, update order,
pair convention, numbered results, proof-status labels, applications, rights,
and every source/handbook ownership boundary. A source mismatch, unread relied-
on passage, silent correction, proceedings/expansion conflation, or
attribution inflation is at least a must-fix.

### Mathematical and proof correctness

Independently reconstruct the determinization. Stress-test missing input
successors, empty labels, duplicate paths, simultaneous child creation,
collapse ordering, name reuse, creation-state colors, persistent names, the
soundness predecessor tree, completeness descent, exact pair orientation,
state count, lower-bound qualifier, and each application. A type error,
undefined transition, false invariant, invalid proof step, wrong class, or
wrong bound is at least a must-fix.

### Adversarial publication and terminology

Try to falsify the version boundary, source ownership, five-part terminology
rule, definition-before-use order, source/handbook repair distinction,
Safra/Thomas separation, proof/sketch distinction, rights statement, cross-file
status, and exact admission scope. A premature name, undefined standing,
hidden source substitution, stale completion claim, or cross-record
contradiction is at least a must-fix.

## Round 1 independence and filing rule

Round 1 uses three fresh agents with no inherited conversation or turn history.
Each reviewer may read only this charter and the five frozen objects. It may
not read `ledger.md`, `transcript/chair.md`, another report, another board,
conversation history, memory, staging material, or web results. Reviewers may
not contact one another.

The assigned files are:

- `transcript/r1-source-fidelity.md`;
- `transcript/r1-mathematical-proof.md`; and
- `transcript/r1-adversarial-publication.md`.

Each report must contain the independently recomputed five identities; an
explicit statement that the actual frozen `.tex` and actual `.ps` were read;
a disposition for every `S01`--`S16`; any findings with severity, identifier,
exact manuscript line, exact source page, and required repair; and a concise
seat-specific rationale. The reviewer may write only its assigned report. Its
final line must be exactly `VERDICT: ACCEPT` or `VERDICT: REJECT --` followed
by exact finding identifiers.

No test, test harness, automated checker, repository script, TeX command,
interim build, manuscript-PDF inspection, PNG inspection, or build is
authorized.

## Frozen Round 2 snapshot

For Round 2, this section supersedes the Round 1 artifact table and filing
rule.  The Round 1 table remains above only as history.  No object in the table
below may be edited while Round 2 is open.

| Artifact | Review scope | Bytes | SHA-256 |
|---|---|---:|---|
| `tmp/pdfs/p09-safra-1988/DBA-author-hosted.ps` | complete controlling twenty-page author-hosted expanded manuscript | 247,788 | `2D492FD28FBCC9FF85E5AA22A62A435D6CB6549DDC00EB5FE8DC7DD82DF6CCD8` |
| `handbook/parts/p09/presentations/n-c-013.tex` | whole-file identity; substantively lines 787--1031, the complete Safra proceedings/expansion boundary and expanded-manuscript reconstruction | 59,650 | `4DF89F9A17BC8CE2EF8D1F66C8990BD088BB1AB8BAD1219C926407FB3F9900F8` |
| `handbook/bib/handbook.bib` | whole-file identity; especially `Safra1988` and `Safra1995Extended` | 207,798 | `C085AB2ACA4DDBFF4FA7BBAAD7C01961007962424829C7537A93CFCA0F9201AC` |
| `spec/research/p09-safra-1988-source-note.md` | complete identity, access, version, mathematical, repair, rights, custody, and scope record | 17,649 | `40EAAF3B885CD7AB3DFAD3B2536FE3EB9EEC77077C3BB5849204E0EB598B92A5` |
| `spec/research/p09-source-presentations-lot2-3.md` | whole-file identity; especially `N-c-013.d` and the consolidated open-status ledger | 238,878 | `4BC69269B9E61BFCE47975F5BA097361F4A844EA3507B321FBFBB8F222DA0D6F` |

Each Round 2 reviewer must independently recompute and report all five byte
counts and identities before substantive judgment.

### Round 2 mandatory refinements

The standing admission question, source boundary, seat mandates, and
`S01`--`S16` checklist remain controlling.  For the repaired snapshot, the
following clauses are explicit parts of those same invariants:

- `S01` and `S16`: the source's reference prints the singular historical
  wording *Journal of Computer and System Science*.  Every source-attributed
  occurrence must preserve or expressly own any normalization.
- `S04`, `S10`, and `S16`: Safra's deterministic target convention is
  `|delta(q,a)|=1` for every state and letter, hence total and single-valued;
  the input may still have an empty successor set.  Muller acceptance must be
  defined as infinity-set membership in a family of state subsets before that
  family's size is discussed.
- `S06` and `S09`: reviewers must inspect the source's printed strict-ancestor
  inconsistency.  The inclusive-path specificity relation, first-divergence
  left-to-right relation, and ancestor-first total traversal must be exact,
  explicitly handbook-owned where corrective, and sufficient to make name
  allocation one function.
- `S12`: the finite factor used by the soundness proof must have an exact
  endpoint convention before use.
- `S14`: the source's printed `n^n` label encoding omits original states absent
  from all live labels.  The handbook-owned encoding must be a total typed map,
  its extra value must not be a node or automaton component, and its bound must
  still prove `2^(O(n log n))`.  Theorem 1 must be stated without undefined
  class abbreviations.  Lemma 2 must bound Muller-family cardinality and remain
  only an Appendix A sketch.
- `S15`: deterministic in the limit must be defined as an accepting-run
  condition involving only finitely many nondeterministic choices and must be
  distinguished from full determinism.
- `S16`: unnecessary undefined breakpoint terminology must not remain, and the
  exact result enumeration is Theorem 1; Lemmas 2, 3, and 5; Corollaries 4, 6,
  and 7.

### Round 2 independence and filing rule

Round 2 uses three fresh blind agents with no inherited conversation or turn
history.  Each reviewer may read only this charter and the five Round 2 frozen
objects.  It must read the actual frozen `.tex` file and the actual frozen `.ps`
file.  It may not inspect a manuscript PDF, PNG, derived source PDF, test,
checker, repository script, TeX command, build, `ledger.md`, chair text, a
Round 1 report, another Round 2 report, another board, conversation history,
memory, staging material, or web result.  Reviewers may not contact one another.

The assigned files are:

- `transcript/r2-source-fidelity.md`;
- `transcript/r2-mathematical-proof.md`; and
- `transcript/r2-adversarial-publication.md`.

Each report must contain the independently recomputed five byte counts and
identities; an explicit statement that the actual frozen `.tex` and actual
`.ps` were read; a disposition for every `S01`--`S16` including the Round 2
refinements; any findings with severity, identifier, exact manuscript line,
exact source page, and required repair; and a concise seat-specific rationale.
The reviewer may write only its assigned report.  Its final line must be
exactly `VERDICT: ACCEPT` or `VERDICT: REJECT --` followed by exact finding
identifiers.

No test, test harness, automated checker, repository script, TeX command,
interim build, manuscript-PDF inspection, PNG inspection, or build is
authorized.

## Frozen Round 3 snapshot

For Round 3, this section supersedes every earlier artifact table, numerical
scope endpoint, refinement section, and filing rule.  The controlling admission
unit is the complete semantic Safra subsubsection defined above, currently
lines 787--1038.  Earlier round material remains only as board history.  No
object below may be edited while Round 3 is open.

| Artifact | Review scope | Bytes | SHA-256 |
|---|---|---:|---|
| `tmp/pdfs/p09-safra-1988/DBA-author-hosted.ps` | complete controlling twenty-page author-hosted expanded manuscript | 247,788 | `2D492FD28FBCC9FF85E5AA22A62A435D6CB6549DDC00EB5FE8DC7DD82DF6CCD8` |
| `handbook/parts/p09/presentations/n-c-013.tex` | whole-file identity; substantively the complete Safra subsubsection at lines 787--1038 | 60,088 | `D8376280880E262F0D0FCE00C6FFBA229284428DB7BBDC7D43C707192C930E75` |
| `handbook/bib/handbook.bib` | whole-file identity; especially `Safra1988` and `Safra1995Extended` | 207,798 | `C085AB2ACA4DDBFF4FA7BBAAD7C01961007962424829C7537A93CFCA0F9201AC` |
| `spec/research/p09-safra-1988-source-note.md` | complete identity, access, version, mathematical, repair, rights, custody, and scope record | 17,866 | `BB9DB11D86A33F8A18BE1D8E5F175C76A2A7A015C36829F9F97EB652B8635F63` |
| `spec/research/p09-source-presentations-lot2-3.md` | whole-file identity; especially `N-c-013.d` and the consolidated open-status ledger | 239,351 | `75F59E5731805548ED37BD1CFC2DB555E1C8AB4C4D5D1BCF096343775DBC795D` |

Each Round 3 reviewer must independently recompute and report all five byte
counts and identities before substantive judgment.

### Round 3 mandatory refinements

The semantic admission question, controlling source boundary, seat mandates,
`S01`--`S16`, and every substantive Round 2 refinement remain mandatory.  In
addition:

- the source's strict-ancestor convention breaks both its printed
  left-to-right clause for siblings and its printed specificity clause at the
  node itself; the first-divergence and inclusive-path corrections must each be
  exact and expressly handbook-owned in the LaTeX and both research records;
- the ancestor-first total traversal and least-unused-name allocation must
  remain separately handbook-owned and yield one transition function;
- the source's printed tree-state tuple must be stated without classifying the
  later handbook-added state before that state's necessity and standing are
  supplied;
- the rejecting state must not be placed into informally named acceptance sets
  before the displayed `G_v` and `B_v` definitions; and
- the complete lines 787--1038 semantic unit must control every disposition,
  including Theorem 1, Lemma 2, Corollaries 4, 6, and 7, the Safra/Thomas
  separation, and the non-facsimile/nonpublication boundary.

### Round 3 independence and filing rule

Round 3 uses three fresh blind agents with no inherited conversation or turn
history.  Each reviewer may read only this charter and the five Round 3 frozen
objects.  It must read the actual frozen `.tex` file and the actual frozen `.ps`
file directly.  It may not inspect a manuscript PDF, PNG, derived source PDF,
test, checker, repository script, TeX command, build, `ledger.md`, chair text,
any Round 1 or Round 2 report, another Round 3 report, another board,
conversation history, memory, staging material, or web result.  Reviewers may
not contact one another.

The assigned files are:

- `transcript/r3-source-fidelity.md`;
- `transcript/r3-mathematical-proof.md`; and
- `transcript/r3-adversarial-publication.md`.

Each report must contain the independently recomputed five byte counts and
identities; an explicit statement that the actual frozen `.tex` and actual
`.ps` were read; a disposition for every `S01`--`S16` and all Round 2 and
Round 3 refinements; any findings with severity, identifier, exact manuscript
line, exact source page, and required repair; and a concise seat-specific
rationale.  The reviewer may write only its assigned report.  Its final line
must be exactly `VERDICT: ACCEPT` or `VERDICT: REJECT --` followed by exact
finding identifiers.

No test, test harness, automated checker, repository script, TeX command,
interim build, manuscript-PDF inspection, PNG inspection, or build is
authorized.
