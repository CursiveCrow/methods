# N-c-015 integrated independent direct-LaTeX review record

## Admission scope

This record admits the integrated reader-facing presentation in
`handbook/parts/p09/presentations/n-c-015.tex` at the explicitly bounded source
and mathematical strength stated in that file.  The admitted content gives the
complete operative finite-tree presentation from the 18 November 2008 release
of *Tree Automata Techniques and Applications* and an abstract-only historical
boundary for Thatcher--Wright 1968.  The finite-ranked-tree definition and
theorem in `handbook/parts/p09/logic-in-computer-science.tex` lines 877--944
are included in the integration scope.

This is a narrow manuscript-content admission.  It does not claim that the
technical body of Thatcher--Wright 1968 or the same-title 1966 IBM report has
been acquired, reconstructed, or reconciled.  It does not admit Part IX as a
whole, another presentation, another handbook part, final typesetting or
layout, human or user review, final-book completion, or publication.

## Direct-LaTeX review protocol

Three fresh blind Round 2 seats independently read the complete actual
manuscript source, `n-c-015.tex` lines 1--166, and the actual host-chapter
LaTeX at `logic-in-computer-science.tex` lines 877--944, including the
presentation input at host line 943.  Each seat also read the two authorized
source/acquisition notes, the compact N-c-015 register material, and the two
relevant bibliography entries.  No concrete ambiguity required a visit to an
original historical publication page during the final round.

No seat opened a manuscript PDF, page image, PNG render, or other derivative
of the manuscript.  No seat ran a TeX build, test, checker, repository script,
hash, or automated validation.  Layout was outside the round and supplied no
evidence.  The target manuscript and host integration remained unchanged
throughout Round 2, and the three reports were kept separate until every seat
had filed:

| Seat | Report | Verdict | Register status |
|---|---|---|---|
| source fidelity and integration | `p09-n-c-015-integrated-source-review-r2.md` | **ACCEPT** | **OPEN** |
| mathematical correctness and definedness | `p09-n-c-015-integrated-mathematical-review-r2.md` | **ACCEPT** | **OPEN** |
| publication text and terminology | `p09-n-c-015-integrated-publication-review-r2.md` | **ACCEPT** | **OPEN** |

Each report was then read completely by the chair.  None contains an adverse
finding, a qualification disguised as acceptance, an unread manuscript
passage, or reliance on a rendered manuscript artifact.  The unanimous
verdict therefore admits the bounded manuscript content; it does not close the
Thatcher--Wright acquisition obligation.

## Integrated review history

The final acceptance was not carried forward from the earlier manuscript
state.

1. Three independent Round 1 seats read the complete 160-line actual LaTeX and
   all returned **REJECT**.  Publication review found that `\epsilon` and the
   set-level source atom `X=\epsilon` lacked an exact local definition, and
   that `T(F)` was used without being introduced or mapped to the host's
   `T_\Sigma`.  Source and mathematical review independently found that the
   general WSkS successor degree was not bound to the ranked alphabet and that
   the displayed two-child inclusion automaton silently specialized the
   arbitrary parameter `k` to two.
2. The actual LaTeX was repaired directly.  It now defines `T(F)` before use
   and maps it to `T_\Sigma`; defines `\epsilon` as the empty word and
   eliminates `X=\epsilon` as `X=\{\epsilon\}`; chooses a successor degree at
   least every arity in the ranked alphabet for the finite-tree bridge; and
   identifies the displayed inclusion automaton as the binary instance
   `k=2`.
3. Three entirely new Round 2 seats, blind to the Round 1 reports and to one
   another, reread the complete repaired 166-line source and the host.  All
   independently returned **ACCEPT** and recorded **REGISTER STATUS: OPEN**.

## Controlling determinations

- The presentation fixes the controlling TATA object as the 18 November 2008
  release while explaining the register's 2007 label, and it keeps finite
  bottom-up tree automata distinct from Rabin's infinite-tree automata.
- TATA's ranked alphabet, ground-term set, tuple order, state and final-state
  sets, transition rules, bottom-up runs, root acceptance, and recognizability
  are defined and mapped exactly to the host notation before use.
- Reachable-subset determinization, effective Boolean closure, and the upward
  final-state reachability test for emptiness are stated at the source's
  operative strength.  The small accepting run is explicitly handbook-owned.
- WSkS receives its word domain, empty word, successor degree, variable sorts,
  restricted atomic syntax, singleton-set semantics, and finite track coding.
  The worked binary encoding and inclusion automaton are typed as binary
  instances rather than silently generalized.
- The finite-tree MSO bridge binds the successor degree to the ranked alphabet,
  identifies the finite position and label sets, and restricts both element
  and set quantifiers to the represented finite domain.  The ambient successor
  tree remains a coding structure, not an infinite automaton input.
- Both logical directions are present at constructive-outline strength: the
  formula induction uses alphabet completion, union, complement, and
  projection; the converse quantifies a state-set partition, a final root, and
  the arity-indexed local transition clause.  The nullary case is well formed
  under the ordinary empty-conjunction and empty-disjunction conventions.
- The closed-sentence rule preserves TATA's explicit nullary `\top`
  convention, and the copying-language counterexample includes its exact
  alphabet hypothesis, necessary reachability premise, and handbook-owned
  deterministic-state separation proof.
- Weak and full monadic quantification are equated only on an actually finite
  domain.  Full SkS over the infinite successor tree remains separate from the
  finite bottom-up construction.
- Thatcher--Wright's phrase “finite algebras” is reported only at authoritative
  abstract strength.  The manuscript assigns no hypothetical signature,
  recognizability relation, logical language, theorem, example, or proof to
  the missing body and describes the owed artifacts without inventing a new
  technical name.

## Disposition

Integrated `N-c-015` manuscript content is admitted for source fidelity,
mathematical correctness and definedness, terminology, host integration, and
reader-facing exposition at the source-bounded strength above.  The source
register remains open for lawful acquisition and reconstruction of the
Thatcher--Wright 1968 technical body, or acquisition of the 1966 report at
precursor strength followed by reconciliation against the journal article.
Part IX remains open.  The manuscript PDF will be built and inspected only
once, after all fourteen parts are text-frozen, solely for final publication
layout.
