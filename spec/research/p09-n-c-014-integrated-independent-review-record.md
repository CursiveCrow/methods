# N-c-014 integrated independent direct-LaTeX review record

## Admission scope

This record admits the integrated reader-facing presentation in
`handbook/parts/p09/presentations/n-c-014.tex` at the explicitly bounded source
and mathematical strength stated in that file.  The admitted unit contains five
deliberately distinct presentations: B\"uchi's complete September 1959 report
precursor; Elgot's complete 1961 article, complete 1959 report precursor, and
published 1962 errata; Trakhtenbrot's complete 1961 announcement and complete
1962 expansion at their distinct strengths; Rabin's complete 1969 article with
the separately attributed Meyer complexity correction; and Thomas's complete
May 1996 report precursor.  The finite-word and `S2S` integration passages in
`handbook/parts/p09/logic-in-computer-science.tex` are included in the scope.

This is a narrow manuscript-content admission.  It does not claim that
B\"uchi's 1959 report has been reconciled with the registered 1960 journal
article, or that Thomas's 1996 report has been reconciled with the registered
1997 chapter.  It does not turn Rabin's cited McNaughton dependency into a
reconstruction of the still-separate McNaughton article body.  It also does not
admit Part IX as a whole, another presentation, another handbook part, final
typesetting or layout, human or user review, final-book completion, or
publication.

## Direct-LaTeX review protocol

Three fresh blind Round 7 seats independently read the complete actual
manuscript source, `n-c-014.tex` lines 1--1884, and the actual host-chapter
LaTeX at `logic-in-computer-science.tex` lines 836--944, including the
presentation input at host line 942.  Each seat also read the five authorized
source notes, the compact N-c-014 register material, and the relevant
bibliography entries.  No concrete ambiguity required a new visit to an
original historical publication page during the final round.

No seat opened a manuscript PDF, page image, PNG render, or other derivative
of the manuscript.  No seat ran a TeX build, test, checker, repository script,
hash, or automated validation.  Layout was outside the round and supplied no
evidence.  The target manuscript and host integration remained unchanged
throughout Round 7, and the three reports were kept separate until every seat
had filed:

| Seat | Report | Verdict | Register status |
|---|---|---|---|
| source fidelity and integration | `p09-n-c-014-integrated-source-review-r7.md` | **ACCEPT** | **OPEN** |
| mathematical correctness and definedness | `p09-n-c-014-integrated-mathematical-review-r7.md` | **ACCEPT** | **OPEN** |
| publication text and terminology | `p09-n-c-014-integrated-publication-review-r7.md` | **ACCEPT** | **OPEN** |

Each report was then read completely by the chair.  None contains an adverse
finding, a qualification disguised as acceptance, an unread manuscript
passage, or reliance on a rendered manuscript artifact.  The unanimous verdict
therefore admits the bounded manuscript content; it does not close the two
publication-version obligations recorded below.

## Integrated review history

The final acceptance was not carried forward from an earlier manuscript state.

1. Round 1 accepted source fidelity but rejected mathematical and publication
   definedness defects across the source presentations.  The actual LaTeX was
   repaired before the next complete read.
2. Round 2 again accepted source fidelity but rejected remaining typing and
   edge-case defects, including Elgot's stable-extension construction, unary
   relation promotion, Rabin's finite-run distinctions, and Thomas's empty-chain
   endpoint.  Those passages were repaired in the manuscript.
3. Round 3 accepted source fidelity and mathematics but rejected nine
   publication-text omissions: the finite-word signature and `WS1S` ranges,
   Rabin's recurring-state and principal-formula types, the deterministic
   Muller word automaton, the named one-letter valued tree, Thomas's direction
   stream, the game, the regular-tree generator, and the binary successor
   functions.  A would-be source seat that had accidentally seen prior-verdict
   text self-disqualified before reading and filed no report; a clean
   replacement seat supplied the actual source review.  All nine defects were
   repaired directly in LaTeX.
4. Round 4 rejected three remaining definedness failures: B\"uchi's empty-word
   string read, Elgot's unordered lexicographic selection, and the completed
   Thomas game's failure to rebind its enlarged state set.  The next snapshot
   supplied the uniform empty-word read, the ordered regular selection, and the
   exact completed game space.
5. Round 5 accepted the mathematics but rejected an undefined Trakhtenbrot
   shorthand, a missing letter-predicate signature in the host theorem, an
   unexpanded metalinguistic Elgot abbreviation, and a silently reused alphabet
   symbol.  The shorthand was eliminated, the host signature and abbreviation
   were made exact, and Rabin's track alphabet received separate notation.
6. Round 6 accepted source fidelity and publication text but rejected the
   finite-tree run domain on nonfrontiered trees and an unqualified prefix
   condition inside Trakhtenbrot's positive-word universe.  The automaton and
   lift were restricted to frontiered finite valued trees, and the converse was
   restated with quantified nonempty-prefix and strict-extension conditions.
7. Round 7 reread the complete repaired actual source.  All three fresh seats
   independently returned **ACCEPT** at the same explicit source-bounded
   strength and independently recorded **REGISTER STATUS: OPEN**.

## Controlling determinations

- B\"uchi's finite-set interpretation, propositional automaton, pointwise
  special-output identity, repaired analysis argument, terminal-marker word
  encoding including the empty word, guarded decision method, and false
  unary-powers claim are admitted at complete-1959-report strength.  The
  repair and later arithmetic correction are not projected into the report as
  original wording.
- Elgot's acceptor and transducer, canonical finite-set encoding, both
  directions of Theorem 5.3, arithmetic consequences, maximal strongly
  extendable sublanguage, ordered regular selection, causal infinite behavior,
  erratum-controlled finite-union construction, handbook-owned unary-window
  completion, and undecidability boundary form one coherent article-plus-errata
  presentation.  The precursor remains separately identified.
- Trakhtenbrot's primitive grammar, syntactic dependence classes, anticipation,
  whole-future finite memory, finite operators, portions, residual stream maps,
  homogeneity, source defect and counterexample, closed-set construction,
  conditional algorithms, solution and general-solution standings,
  fixed-lookahead results, and positive-word bridge retain the distinct 1961
  and 1962 source strengths.  No Russian-language-specialist certification is
  inferred from this admission.
- Rabin's successor structures, ordinary and dual acceptance, both logical
  translations, deterministic path product, marked and well-founded obligation
  architecture, positive-length pair induction, frontiered finite-tree lift,
  finite table-runs, source emptiness reduction, applications, and later Meyer
  complexity correction are admitted without substituting Thomas's later
  regular-tree basis route for Rabin's proof.
- Thomas's detailed finite-word and infinite-tree construction belongs to the
  May 1996 report precursor.  The finite-word structures, empty-word guard,
  game positions and moves, rejecting-state completion, empty chain,
  memoryless-strategy complement, regular-tree generator, basis theorem, and
  `S2S` route are coherent and do not close final-chapter reconciliation.
- The host's modern finite-word theorem now includes its letter predicates and
  explicitly distinguishes the modern package from the historical source
  encodings.  Its `S2S` theorem and neighboring finite-ranked-tree material do
  not conflate finite bottom-up runs with Rabin's infinite-tree automata.
- Every handbook-added technical abbreviation in the admitted range has a
  stated standing and an eliminable definition, is distinguished from nearby
  source terminology, and is used by a later construction or theorem.  Where
  existing language sufficed, unsupported shorthand was removed instead of
  naming a hypothetical object.

## Disposition

Integrated `N-c-014` manuscript content is admitted for source fidelity,
mathematical correctness and definedness, terminology, host integration, and
reader-facing exposition at the source-bounded strength above.  The source
register remains open for literal reconciliation of B\"uchi's 1960 journal
article with UMR1083 and Thomas's 1997 chapter with the May 1996 report.  The
separate McNaughton article-body obligation is unaffected.  Part IX remains
open.  The manuscript PDF will be built and inspected only once, after all
fourteen parts are text-frozen, solely for final publication layout.

