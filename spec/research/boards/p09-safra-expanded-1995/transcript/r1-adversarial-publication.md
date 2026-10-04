# Round 1 adversarial publication and terminology review

## Review declaration

I independently recomputed all five frozen SHA-256 identities before making a
substantive judgment. I read the actual frozen LaTeX file directly, including
the complete substantive scope at lines 787--1000, and read the actual frozen,
hash-pinned PostScript source page by page. The PostScript itself, rather than
the navigation text extracted directly from it, controlled every source
comparison below.

I read only the charter and the five frozen objects. I did not inspect a
manuscript PDF, PNG, derived source PDF, test, checker, repository script, TeX
command, build, ledger, chair report, other report or board, staging material,
memory, conversation history, or non-frozen web result.

## Independently recomputed identities

| Frozen object | Bytes | Recomputed SHA-256 | Identity disposition |
|---|---:|---|---|
| `tmp/pdfs/p09-safra-1988/DBA-author-hosted.ps` | 247,788 | `2D492FD28FBCC9FF85E5AA22A62A435D6CB6549DDC00EB5FE8DC7DD82DF6CCD8` | exact match |
| `handbook/parts/p09/presentations/n-c-013.tex` | 57,179 | `7F8B6D07C564D7312FFADC437228C60FC56B80C61A3A6AD7576766FE2E587A7B` | exact match |
| `handbook/bib/handbook.bib` | 207,736 | `05B96387DBE9774BF76B3E5E8B1D5C5D3590CA5B101ADA7CACAB66CE61B15208` | exact match |
| `spec/research/p09-safra-1988-source-note.md` | 15,511 | `A252D489A270D824C0F083B28685F7B17F981331523DB3EE3477AD1273A0F45F` | exact match |
| `spec/research/p09-source-presentations-lot2-3.md` | 237,009 | `5A1340437E27BA9653747D69BC987C81D8B02D86B68528BCA1A26EEC9E3E7743` | exact match |

The actual PostScript also has the declared identity facts: 247,788 bytes,
`%%Title: jcss.dvi`, `%%CreationDate: Tue Mar 21 15:47:45 1995`, twenty
declared pages, the title-page preliminary-version footnote, and the `[Saf88]`
FOCS reference.

## Findings

### R1-APT-01 — silent alteration of the source's historical journal wording

- **Severity:** must-fix
- **Checklist:** S01, S16
- **Exact manuscript line:** `n-c-013.tex:797`
- **Other frozen lines:** `handbook.bib:2355--2356` and
  `p09-safra-1988-source-note.md:53`
- **Exact source page:** PostScript p. 19, reference `[Saf88]`

The actual source prints the singular historical wording “Journal of Computer
and System Science.” The detailed source note preserves that singular wording,
but manuscript line 797 and the `Safra1995Extended` bibliography note silently
change it to “Journal of Computer and System Sciences” while expressly saying
what the manuscript itself says. This is a source-wording mismatch and a
cross-file contradiction at the publication boundary. It does not establish a
journal publication, but exactness still matters because the source's “to
appear” statement is the evidence being reported.

**Required repair:** make the manuscript and bibliography note report the
singular wording actually printed by the source, or expressly distinguish the
printed wording from an editorial normalization. Keep the existing statement
that no journal publication record was established.

### R1-APT-02 — Safra's meaning of “deterministic” is omitted

- **Severity:** must-fix
- **Checklist:** S09, S10, S16
- **Exact manuscript line:** `n-c-013.tex:804` (the source-automata definition
  begins here; the missing clause is owed before line 819)
- **Exact source page:** PostScript p. 4

Safra explicitly calls an automaton deterministic when
`|delta(q,a)| = 1` for every state and letter, so the condition is total as
well as single-valued. The Safra passage defines the set-valued transition and
run but never states this source convention before asserting a deterministic
output, a deterministic run, deterministic allocation, and a totalizing sink.
The omission is material because the same frozen LaTeX previously reports a
different source convention at lines 52--59 under which missing transitions
remain possible. The sink repair is substantively correct, but its necessity
is not definition-before-use exact while Safra's target standing is unstated.

**Required repair:** in the source-automata paragraph, state Safra's exact
`|delta(q,a)| = 1` deterministic condition, identify it as the target
condition, and distinguish it from the input's possible empty successor set
and from the earlier presentation's partial convention. Then the later sink
paragraph can point back to that definition.

### R1-APT-03 — “tree order” does not specify the promised deterministic allocation

- **Severity:** must-fix
- **Checklist:** S09, S16
- **Exact manuscript line:** `n-c-013.tex:881`
- **Exact source pages:** PostScript pp. 9 and 11

Line 881 orders temporary nodes “in tree order,” but no relation with that name
or exact traversal is defined. The state definition supplies sibling orders
and their induced left--right relation on non-ancestral nodes; it does not say
that “tree order” means that relation or fix ancestor/descendant traversal.
Safra's p. 11 instruction is only to choose “some” unused name, so the
handbook-owned choice must itself be exact before it can turn the update into a
literal deterministic function.

**Required repair:** replace “tree order” by one already defined exact order,
and explain why it is total on the surviving temporary nodes, or define a
specific total traversal (for example, the preorder induced by the sibling
orders) immediately before use. Continue assigning distinct least unused
elements of the linearly ordered vocabulary in that order.

### R1-APT-04 — “breakpoint” terminology is introduced without the five required facts

- **Severity:** must-fix
- **Checklist:** S16
- **Exact manuscript lines:** `n-c-013.tex:925--929`
- **Exact source page:** PostScript p. 6

The phrases “global breakpoint test,” “breakpoint discipline,” and
“breakpoint obligation” appear without an eliminable definition or an exact
standing. The source defines a breakpoint as a stage condition on the subset
simulation: since the previous breakpoint, every currently reachable state
has a represented run that has visited an accepting state. The manuscript does
not supply that definition, distinguish the global test from a node's local
collapse event, or use the new terminology in a later definition or theorem.
Consequently the terms fail the definition, standing, nonredundancy, and use
parts of the required terminology rule.

**Required repair:** either remove the three technical names and describe the
already defined child/collapse operations directly, or define the source's
breakpoint stage condition exactly, state its standing and its difference from
a local green collapse, and use that distinction where it is genuinely needed.

### R1-APT-05 — the proof uses an undefined finite-word factor notation

- **Severity:** must-fix
- **Checklist:** S12, S16
- **Exact manuscript line:** `n-c-013.tex:946`
- **Exact source page:** PostScript p. 11

The soundness proof first uses `alpha[i_j,i_{j+1})` at line 946 without
defining it. The source explicitly defines its corresponding notation as the
finite word consisting of positions `i` through `j-1` before using it in the
predecessor argument. Without that clause, the type and endpoint convention of
the run segment are implicit precisely where edge orientation and
concatenation are being checked.

**Required repair:** immediately before the soundness argument, define
`alpha[i,j)` as the finite factor
`alpha(i) alpha(i+1) ... alpha(j-1)` for `i <= j`, or replace the notation by
that description at line 946.

### R1-APT-06 — `NB` and `DR` are used without definition

- **Severity:** must-fix
- **Checklist:** S14, S16
- **Exact manuscript lines:** `n-c-013.tex:969--973`
- **Exact source pages:** PostScript pp. 4 and 9

The display uses `NB(n)` and `DR(2^{O(n log n)},n)`, their first and only
occurrence in the frozen LaTeX file, without defining either source-specific
class abbreviation or the two parameters of `DR`. Safra's p. 4 notation
distinguishes nondeterministic/deterministic mode and Büchi/Rabin acceptance
and makes the Rabin size record carry both the state count and the acceptance-
pair count; p. 9 then states Theorem 1 in that notation. The manuscript's prose
contains enough information to eliminate the abbreviations, but does not do
so at their point of use.

**Required repair:** either define `NB(n)` as the class of `n`-state
nondeterministic Büchi automata and `DR(m,h)` as the relevant deterministic
Rabin class with state bound `m` and `h` pairs immediately before the display,
or replace the display with the already available fully spelled-out theorem.

### R1-APT-07 — Muller acceptance lacks standing and semantics before Lemma 2

- **Severity:** must-fix
- **Checklist:** S14, S16
- **Exact manuscript lines:** `n-c-013.tex:976--978`
- **Exact source pages:** PostScript pp. 4, 13, and 17--18

The passage says that conversion to deterministic Muller acceptance can
require a doubly exponential “acceptance family,” but it has not defined a
Muller family or its semantics. The first actual definition in this frozen
LaTeX occurs only later, outside the admitted Safra passage, at lines
1038--1039. Safra's p. 4 gives the eliminable definition: a family of subsets
of the state set accepts exactly when the run's infinity set is one of its
members. That standing is necessary to understand what quantity Lemma 2 says
must be doubly exponential; pp. 13 and 17--18 state and sketch the lower bound.

**Required repair:** add the typed Muller family and infinity-set membership
condition to the source-automata paragraph before its use, then state that
Lemma 2 bounds the size of that family. Retain the existing Appendix A
“sketch” qualification.

### R1-APT-08 — “deterministic in the limit” is undefined in all three places that use it

- **Severity:** must-fix
- **Checklist:** S15, S16
- **Exact manuscript lines:** `n-c-013.tex:985--987`
- **Other frozen lines:** `p09-safra-1988-source-note.md:226--227` and
  `p09-source-presentations-lot2-3.md:602`
- **Exact source page:** PostScript p. 15

The manuscript and both research records name Corollary 7's target as a Büchi
automaton “deterministic in the limit” but never define that source term.
Safra defines it immediately before the corollary: every accepting run makes
only finitely many nondeterministic choices. Its standing is a condition on
the automaton's accepting runs, and it is weaker than full determinism because
nonaccepting runs need not eventually stop making nondeterministic choices.
Without those facts, the partial-determinization target is not exact and the
five-part terminology rule is not met at any occurrence.

**Required repair:** at each occurrence, replace the name by its eliminable
run condition, or define the term there with its standing, its distinction
from full determinism, and its role as Corollary 7's target.

## Mandatory invariant checklist

- **S01 -- NOT SATISFIED.** The five-object identity, byte count, twenty-page
  header, generation date, preliminary-version footnote, FOCS reference, and
  unpublished expansion boundary are verified; R1-APT-01 leaves one exact
  source-attributed publication wording inconsistent.
- **S02 -- SATISFIED.** DOI `10.1109/SFCS.1988.21948`, pp. 319--327,
  abstract-level proceedings contribution, and the continuing nine-page body
  gap remain separate from expanded-manuscript detail and numbering.
- **S03 -- SATISFIED.** The source note denies an open-content or
  republication licence, the manuscript is independent prose, and no derived
  render is presented as evidence.
- **S04 -- SATISFIED AS TO THE LISTED INPUT DATA.** The tuple, set-valued
  transition, initial state, run recurrence, infinity set, and Büchi condition
  are typed before use, and empty successor sets remain possible. Safra's
  separate target meaning of “deterministic” fails under S09/S10/S16 in
  R1-APT-02.
- **S05 -- SATISFIED.** Safra's `(L_i,U_i)` order is good/recurring then
  bad/eventually absent and is expressly separated from Thomas's notation.
- **S06 -- SATISFIED.** Tree, node identities, label map, total color map,
  proper containment, branch disjointness, sibling/left--right order, and the
  eliminable specific-state abbreviation have distinct standings.
- **S07 -- SATISFIED.** The one-node `{q0}` all-white source state is present;
  the least root name is expressly handbook-owned and representational.
- **S08 -- SATISFIED.** The six stages preserve source order and the required
  objects, including simultaneous child creation, horizontal retention,
  deletion, collapse/coloring, and renaming.
- **S09 -- NOT SATISFIED.** The `n`-node argument, reservoir size,
  creation-state red color, and persistence are correct, but R1-APT-02 and
  R1-APT-03 leave the target convention and allocation function incompletely
  specified.
- **S10 -- NOT SATISFIED.** The sink's standing, loop, pair membership,
  language effect, bound effect, and handbook ownership are correct; however,
  R1-APT-02 omits the exact Safra determinism condition that the totalizing
  repair is meant to satisfy.
- **S11 -- SATISFIED.** Every vocabulary name has the right green/good and
  red/bad state sets, the sink is in every bad set and no good set, the
  eventual-red/infinite-green condition is correct, and the pair count is
  exactly `n`.
- **S12 -- NOT SATISFIED.** The predecessor orientation, finite branching,
  König argument, and accepting concatenation are substantively valid, but
  R1-APT-05 leaves the finite segment and its endpoint convention undefined.
- **S13 -- SATISFIED.** Root representation, eventual movement to older
  siblings, descent, bounded depth, persistent name, and final Rabin witness
  match the source proof without a quantifier reversal.
- **S14 -- NOT SATISFIED.** Counts, exact `n` pairs, `n!` lower bound,
  constant-in-the-exponent qualifier, and Appendix A sketch status match the
  source; R1-APT-06 and R1-APT-07 leave the theorem's class notation and Muller
  acceptance-family standing undefined.
- **S15 -- NOT SATISFIED.** Corollaries 4 and 6 have the correct classes and
  bounds, and Corollary 7 has the correct numerical bound, but R1-APT-08 leaves
  its partial-determinization target undefined. Modal-logic consequences are
  not inflated.
- **S16 -- NOT SATISFIED.** Safra's `n` names/`n` pairs remain separate from
  Thomas's `2n` names/`2n` pairs, proceedings reconciliation remains open,
  repair ownership and review status are not inflated, and no forbidden
  derived object or publication claim is evidence. R1-APT-01 through
  R1-APT-08 nevertheless leave an exact cross-file wording contradiction and
  multiple terminology/definition-before-use failures.

## Seat-specific rationale

The frozen snapshot succeeds at the large publication boundary: it does not
substitute the expansion for the unread proceedings body, claim a JCSS
publication, convert hosting into a licence, splice Thomas's presentation into
Safra's, disguise the two handbook-owned repairs as source text, or promote an
Appendix sketch into a proof. The rejection is narrower and independently
fatal under this seat's mandate. One source-attributed publication phrase is
silently altered, and the text relies on seven undefined or incompletely
defined source terms, conventions, or notations exactly where determinism,
proof typing, class bounds, and partial-determinization standing are asserted.
Each repair can be local, but no unresolved must-fix is admissible in Round 1.

VERDICT: REJECT -- R1-APT-01, R1-APT-02, R1-APT-03, R1-APT-04, R1-APT-05, R1-APT-06, R1-APT-07, R1-APT-08
