# N-c-015 integrated publication and terminology review — Round 1

VERDICT: REJECT

The integrated publication text has two line-specific must-fix notation and
definition-before-use defects.  Both are narrow, but each occurs in an
operative formula or theorem example and therefore prevents acceptance under
the repository's exact standing and technical-name requirements.  I found no
other publication or terminology defect at the source-bounded strength claimed.

## Review scope and evidence

This is a fresh blind review of the actual reader source.  I read:

- `handbook/parts/p09/presentations/n-c-015.tex`, lines 1--160, completely;
- `handbook/parts/p09/logic-in-computer-science.tex`, lines 877--944,
  completely;
- `spec/research/p09-tata-2008-source-note.md`, completely;
- `spec/research/p09-thatcher-wright-1968-acquisition-note.md`, completely;
- the compact `N-c-015` portion of
  `spec/research/p09-source-presentations-lot2-3.md`, lines 751--775; and
- the `ComonEtAl2007` and `ThatcherWright1968` entries in
  `handbook/bib/handbook.bib`, lines 5883--5889 and 6041--6050.

The audit covers definition-before-use, notation and type standing,
nonredundancy and later use of technical names under `AGENTS.md`, logical
order, graduate-reader sufficiency, sentence-level clarity, ownership and
citation boundaries, source/version boundaries, and compatibility with the
host theorem and definition.

## Prohibitions observed

No manuscript PDF, historical-source PDF, PNG, page image, render, or other
visual artifact was opened or used as manuscript evidence.  No LaTeX or PDF
build, test, harness, checker, repository script, automated validator, or hash
operation was run.  No prior or parallel integrated `N-c-015` report,
independent-review record, board file, admission ledger, or review-history
artifact was opened or used.  Status prose incidentally present in the two
mandated supporting records was not used as verdict evidence.  Layout is
outside this review.

## Must-fix findings

### 1. Lines 49--60: `X=\epsilon` has no defined or type-correct standing

After Proposition 3.3.1 is said to replace every first-order variable by a
singleton **set** variable, line 55 lists

\[
X\subseteq Y,\qquad \operatorname{Sing}(X),\qquad X=Yi,\qquad X=\epsilon.
\]

Lines 57--59 define `Sing(X)` and explain `X=Yi` in terms of the unique words
belonging to the two singleton sets.  They do not define `\epsilon`, and they do
not state what `X=\epsilon` means.  Read as ordinary equality, the display is
ill-typed: `X` has just been declared a set variable, whereas `\epsilon` is
presumably a word.  The later uses of `\epsilon` as the root in the worked
encoding (line 67) and final-root condition (line 101) depend on the omitted
meaning.

Must-fix: at this first occurrence, state that `\epsilon` denotes the empty
word and give the exact semantics and standing of the source atom
`X=\epsilon` in the singleton-set presentation—for example, if that is the
source's intended reading, that the unique member of `X` is `\epsilon`,
equivalently `X=\{\epsilon\}`.  Make clear that this is a well-typed atomic
formula or an explicitly eliminable abbreviation, not ordinary equality
between a set and a word.  This supplies definition, standing, nonambiguity,
and the meaning required by the later root uses without inventing a new
technical object.

### 2. Lines 120--129: `T(F)` is used without being introduced

The copying-language example defines

\[
L=\{f(t,t):t\in T(F)\}
\]

and later appeals to the infinitely many terms in `T(F)`.  Lines 12--16 have
defined ground terms over the ranked alphabet `F` in prose, but they never
assign those terms the notation `T(F)`.  The host instead introduced
`T_\Sigma` for finite `\Sigma`-trees (host lines 884--893), and the source-to-host
map at manuscript lines 28--30 maps the alphabet and final-state symbols but
does not map this term-set notation.  Consequently `T(F)` first appears as an
undefined object precisely where membership in it carries the example and its
proof.

Must-fix: before or at line 122, define `T(F)` exactly as the set of ground
terms, equivalently finite ordered ranked `F`-trees, generated at lines 12--16;
also relate it to the host's `T_\Sigma` notation or simply reuse the already
defined host notation.  The repair must give the notation's standing as a set
of finite terms and preserve its two later uses in the language definition and
infinite-state contradiction.

## Findings that do not require repair

### Source and version boundaries

The manuscript identifies the controlling TATA object as the fixed 18 November
2008 release and explains that the register's 2007 date belongs to the evolving
work, not a second fixed edition (lines 6--10).  The `ComonEtAl2007` bibliography
key preserves the stable key while its entry records 2008 and the exact release
date.  This is internally consistent.

The Thatcher--Wright paragraph reports only the authoritative abstract's
finite-algebra, closure, generalized-Kleene, and positive-second-order scope
(lines 141--152).  It expressly refuses to assign TATA's modern ranked-tree
tuple, logical language, theorem statements, examples, or proof to the
unavailable 1968 body.  The same-title 1966 report is correctly described as a
bibliographic lead rather than technical evidence.  That is exactly the
source-bounded treatment required by the acquisition note and by the
`AGENTS.md` rule: the text describes the owed artifact instead of naming a
hypothetical reconstruction.  The missing Thatcher--Wright body therefore
keeps the register open but is not itself a manuscript rejection reason.

### Standing, nonredundancy, and operative use of the defined terms

Apart from the two defects above, the technical vocabulary is introduced with
adequate standing and then used.  Lines 12--30 distinguish ranked symbols,
ground terms, finite ordered trees, automaton states, final states, transition
rules, runs, accepted terms, and recognizable languages.  They also resolve
the potentially serious `F` collision explicitly: TATA's `F` is the host's
alphabet `\Sigma`, while TATA's `Q_f` is the host's final-state set `F`, and the
tuple orders differ.

Lines 49--60 define WSkS as weak monadic second-order logic on the `k`-successor
word tree, distinguish word-valued first-order variables from finite-set-valued
monadic variables, and explain the singleton-set reduction.  Lines 62--83 then
give the finite membership-track encoding and distinguish the ambient prefix
tree used for coding from the finite input tree represented by the code.
Lines 85--110 preserve the separate standings of a logical assignment, an
encoding tree, an automaton, a state partition, a local transition clause, and
an accepting run.  Lines 131--139 define full SkS by changing the set-variable
range and explain exactly why its root-down infinite-input automata are not the
finite bottom-up automata under review.

The manuscript's new or source-specific terms are nonredundant where they need
to be.  `Recognizable` names the accepted-language property, not an automaton;
WSkS and full SkS differ by the finite versus arbitrary set range; the coded
ambient successor tree is not the finite input; and the TATA tuple is mapped to
rather than silently identified with the host tuple.

### Logical order and reader sufficiency

The exposition moves in a sound graduate-reference order: finite ranked terms
and bottom-up automata; a concrete finite run; determinization, Boolean
closure, and emptiness; the WSkS singleton syntax; finite-track coding; the
finite-tree MSO bridge; formula-to-automaton and automaton-to-formula
directions; the closed-sentence decision; a nonrecognizable copying language;
the finite/full boundary; then the unavailable historical-source and
reconstruction boundaries.

The operative proof architecture is present.  The manuscript records
reachable-subset determinization, the final-state criterion in the emptiness
marking construction, coordinate completion before disjunctive union,
complement for negation, track projection for existential quantification, and
the state-set partition plus local transition formula for the converse.  It
also preserves TATA's warning that Theorem 3.3.7 is only a convenient slogan
and assigns exact content to Lemmas 3.3.4 and 3.3.6.  The final paragraph
honestly identifies the constructive outline's limits and owns the small run
and copying-language proof as handbook additions (lines 154--160).

### Host compatibility

The host first distinguishes Rabin's full infinite binary tree and `S2S`
(host lines 877--882), then defines finite ranked terms and nondeterministic
bottom-up automata (884--913), and only then states the finite-tree
automata/MSO equivalence and weak/full finite-domain coincidence (915--934).
The `N-c-015` input occurs afterward (943).  The manuscript uses that order:
it maps TATA's tuple to the host tuple at lines 28--30, supplies the
constructive details promised by the host theorem, and repeatedly distinguishes
finite bottom-up runs from Rabin's root-down infinite-tree runs (manuscript
lines 6--10, 32--37, 73--83, and 131--139).  No host theorem is strengthened or
silently redefined.

### Citations and ownership

The nearby `ComonEtAl2007` citations support the fixed release identity,
finite-tree scope, tuple and run, constructive operations, WSkS coding and
logical translations, and the finite/full boundary.  The final reconstruction
boundary correctly says that the worked finite run and the proof of Exercise
1.4 are handbook-owned.  `ThatcherWright1968` is used only for the verified
bibliographic identity and abstract-level provenance.  The two relevant
bibliography entries agree with the permitted source and acquisition notes.

## Acceptance condition

Acceptance requires both must-fixes above in the actual manuscript source:
give a locally typed definition of `\epsilon` and the atom `X=\epsilon`, and
define or eliminate `T(F)` before its first use.  No broader rewriting or new
technical apparatus is warranted.

REGISTER STATUS: OPEN
