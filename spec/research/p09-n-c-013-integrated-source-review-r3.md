ACCEPT

# N-c-013 integrated source-fidelity audit, Round 3

## Audit scope and verdict basis

I read the current actual `handbook/parts/p09/presentations/n-c-013.tex`
from line 1 through its end at line 1409 and the current host
`handbook/parts/p09/logic-in-computer-science.tex` from lines 723--945,
including the input of N-c-013 at host line 935.  I also checked the explicitly
cross-sourced parity convention in
`handbook/parts/p09/presentations/n-c-018.tex:615--647`, the five permitted
N-c-013 source notes, the compact register-obligation ledger, and the relevant
bibliography entries.  I did not consult an earlier review, admission record,
transcript, board file, charter, manuscript PDF, PNG, render, or page image.  I
did not run a build, test, checker, repository script, hash, or automated
validation.

At the strength the manuscript expressly claims, the current LaTeX is
source-faithful and publication-admissible.  The account consistently separates
historical-source statements from handbook translations, repairs, notation,
examples, and representative choices.  It also keeps the four unresolved
source-body/provenance obligations open rather than treating their absence as
negative evidence.  I found no source-fidelity defect.

## Exact-line findings

### 1. Host integration, parity provenance, and theorem citations

- `logic-in-computer-science.tex:723--745` gives the deterministic parity word
  convention as handbook-owned specialization, not as an N-c-013 historical
  source claim.  Its least-priority-recurring-even clause at lines 737--740 is
  externally seated in Bradfield--Stirling at lines 741--745.  The permitted
  cross-source passage `n-c-018.tex:634--647` uses the same least-recurring-even
  convention and cites Bradfield--Stirling Sections 4--5.  The bibliography
  entry `handbook.bib:5857--5868` identifies that chapter correctly.  Parity is
  therefore neither unattributed nor silently assigned to Vardi--Wolper,
  Buechi, McNaughton, Safra, or Thomas.

- `logic-in-computer-science.tex:747--765` states a total deterministic Rabin
  word automaton and Thomas's pair semantics: some `E_i` is eventually absent
  while some `F_i` recurs.  This agrees with Thomas's 1996 report convention as
  reconstructed in the Thomas note at lines 114--134 and with the report
  presentation in `n-c-013.tex:1204--1266`.  It is expressly a word automaton,
  not a tree automaton.

- `logic-in-computer-science.tex:767--779` attributes the exponential LTL-to-
  Buechi theorem jointly and accurately: Vardi--Wolper state it, credit the
  earlier Wolper--Vardi--Sistla paper, and provide the compact Appendix B
  construction.  The host preserves the explicit `2^{3|A|}` permitted-start
  product bound and identifies the extra single-start state as handbook-owned.
  This matches `n-c-013.tex:87--100` and `102--222` and the Vardi--Wolper note at
  lines 114--200.

- `logic-in-computer-science.tex:781--784` supports effective complementation
  with the acquired Safra expanded manuscript and Thomas report, not with the
  unread Safra 1988 proceedings body.  That is the correct source seat.

- `logic-in-computer-science.tex:786--819` gives the zero-based product exactly:
  the automaton consumes the initial structure label in the initial product
  vertices at lines 800--803, then consumes each successor label on the edge at
  lines 804--806.  The accepting cyclic-SCC criterion at lines 807--812 is the
  finite graph form of an ultimately periodic counterexample.  The linear
  explicit-product claim and separately stated formula-translation contribution
  at lines 814--818 do not collapse the parameters.

- `logic-in-computer-science.tex:821--834` states both directions of product
  correctness and sources the combined-input PSPACE lower bound to
  Sistla--Clarke while using closure of deterministic polynomial space under
  complement for the universal-path formulation.  It does not misattribute
  that lower bound to Vardi--Wolper's upper-bound theorem.  The supporting
  bibliography entries are accurate at `handbook.bib:2260--2274` and
  `2323--2344`.

- `logic-in-computer-science.tex:852--871` carefully splits Buechi's literal
  Theorem 1 and Theorem 2 from the handbook-owned modern automaton packaging and
  converse.  It restricts the normal-form statement to formulas with no free
  individual variables, retains the later effectivity step, gives no modern
  complexity bound, and uses the finite stem--cycle search only after effective
  normalization.  This agrees with `n-c-013.tex:762--820` and the Buechi note at
  lines 338--399.

- `logic-in-computer-science.tex:934--936` inputs N-c-013 once, between N-c-012
  and N-c-014.  No host line in the audited range assigns N-c-013 material to a
  different source or bypasses the bounded presentation.

### 2. Vardi--Wolper 1986 author-preprint presentation

- `n-c-013.tex:6--15` states the source object and locators exactly: the
  eighteen-page file is linked from IEEE CEDA, identified by Wolper's
  institutional repository as an author preprint, dated 15 August 1985 on its
  abstract cover, and distinguished from the ten-page 1986 proceedings record
  at pp. 322--331.  It does not call the file a proceedings facsimile.  This
  matches the Vardi--Wolper note at lines 3--33 and bibliography entry
  `handbook.bib:2323--2334`.

- `n-c-013.tex:17--62` reproduces the source's finite propositional alphabet,
  computation type, non-strict `X` and `U` semantics, permitted-start-set
  Buechi tuple, run indexing, recurrence condition, semi-determinism, and the
  source's exact distinction between semi-determinism and determinism.  The
  locators to preprint pp. 4 and 10 and Appendix A agree with the source note's
  page map and extraction (`p09-vardi-wolper-1986-source-note.md:35--54,
  56--128`).

- `n-c-013.tex:64--85` visibly owns and proves the one-state conversion from a
  permitted start set to the handbook's single-start, zero-based convention.
  The fresh state consumes the first letter while choosing and advancing from
  an old permitted start, has no incoming transition, is nonaccepting, handles
  the empty start set, preserves recurrence, and adds exactly one state.  No
  part of this conversion is falsely quoted as Vardi--Wolper's tuple.

- `n-c-013.tex:87--100` preserves the source theorem's literal
  `2^{O(|varphi|)}` bound, its attribution to Wolper--Vardi--Sistla 1983, and
  the cited rather than reproduced status of the emptiness algorithms.  The
  bibliography does not claim independent acquisition of the 1983 body
  (`handbook.bib:2336--2344`).

- `n-c-013.tex:102--222` gives a fully typed and correctly scoped account of
  Appendix B: closure and eventuality sets; the complete local types; the
  local transition's Boolean, next, and until conditions; batch collection and
  discharge by recurrence of the empty obligation set; the product's states,
  permitted starts, designated set, transition, and `2^{3|varphi|}` bound; and
  the projection from closure types to propositional valuations.  Lines
  219--222 expressly preserve the proof boundary: the appendix gives the
  construction and invariant but no worked input or line-by-line proof of both
  language inclusions.  The construction agrees with the source note at lines
  130--217.

- `n-c-013.tex:224--279` accurately reconstructs the finite-state program,
  identifies the source's tuple-order inconsistency without inventing a second
  convention, derives counterexamples by intersection with the automaton for
  `not varphi` rather than automata-theoretic complementation, and separates
  the source's two-parameter upper bounds from Sistla--Clarke's combined-input
  lower bound.  This agrees with the source note at lines 219--296.

- `n-c-013.tex:281--301` labels its three-state product calculation as a
  handbook example because the source has none.  The accepting branch
  `s_0 b^omega` witnesses `G not p`, the other branch enters the rejecting
  sink after seeing `p`, and the calculation respects the surrounding
  zero-based convention.

- `n-c-013.tex:303--328` keeps the past-operator extension and the three
  automata-connective languages separate, defines each acceptance standing,
  retains the source's `O(exp(|varphi|^2))` bound for `ETL_r`, and says the
  cited proof is not reproduced.  This matches the note at lines 202--217 and
  298--319.

- `n-c-013.tex:330--400` distinguishes almost-sure satisfaction from
  universal-path satisfaction.  Its cylinder, Borel-field, formula-event, and
  support-size notation is explicitly handbook notation replacing the source's
  overload; every abbreviation is defined and used.  The Streett clause is
  exact, and lines 395--400 record the source's internally inconsistent
  conversion sentence as a printed defect rather than promote it to a theorem.
  This matches the source note at lines 321--376.

- `n-c-013.tex:402--505` defines every restricted temporal fragment before use,
  gives exact limit and `k`-limit equivalence, correctly states
  probabilistic fairness as a computation condition, preserves each displayed
  time/space bound, and marks every sketch, deferral, open improvement, and
  concurrent-model omission.  This agrees with the source note at lines
  378--479.

- `n-c-013.tex:507--512` closes the Vardi--Wolper presentation with an accurate
  proof-ownership ledger.  It does not upgrade cited prior results, proof
  sketches, or promised full-paper details.

### 3. Buechi 1962 presentation

- `n-c-013.tex:514--528` identifies the complete article in the later Stanford
  printing, maps printed pp. 1--11 to file pp. 12--22, identifies the next
  article at file p. 23, gives the original editors and publisher, and keeps the
  1966 Elsevier and 1990 Springer DOI-bearing republications separate.  This
  matches the Buechi source note at lines 1--37 and the bibliography entry at
  `handbook.bib:2276--2288`.

- `n-c-013.tex:530--606` preserves Buechi's source name `SC`, its interpreted
  natural-number/full-monadic-set standing, its predicate-assignment word
  encoding, the exact `Sigma_n`/`Pi_n` schemes, the infinitely-often
  quantifier, and `Sigma_1^omega` formula/denotation overload.  It neither
  retrojects the modern name S1S as Buechi's presentation nor treats
  “sequential calculus” as another formal system.  This agrees with the note at
  lines 67--156.

- `n-c-013.tex:608--640` labels the modern finite automaton data as a handbook
  translation of one recurrent existential formula.  The alphabet, state set,
  allowed starts, transition, and recurrent set are eliminably defined; the
  existential predicate sequence supplies the nondeterministic run; and the
  text explicitly says the article does not print the modern tuple or term
  “Buechi acceptance.”  The single-start conversion is again owned by the
  handbook.  This matches the note at lines 158--189.

- `n-c-013.tex:642--680` gives the exact bounded regular formula, its finite-word
  dependence, the source-declared `Sigma^0` overload, congruence, rank, and
  multiperiodic finite-word language.  “Multiperiodic” is not confused with an
  ultimately periodic infinite assignment.  This agrees with the note at lines
  191--224.

- `n-c-013.tex:682--750` states the Sequential Lemma with the essential
  `p<q` quantification, records the printed Ramsey proof, separates the
  finite-state recursion from an infinite-word acceptor, and preserves the
  Myhill/Buechi-1960 and Rabin--Scott proof dependencies.  Its complement
  construction uses the source's `2m^2` distinctions and finite congruence,
  not a later determinization theorem.  This agrees with the note at lines
  226--336.

- `n-c-013.tex:752--789` accurately states the finite-union stem/repeated-block
  form, Theorem 1's collapse to one recurrent existential form, and the
  hierarchy collapse.  The two-way modern Buechi-language comparison is
  explicitly a handbook corollary, with unused state codes excluded, and is not
  put into Buechi's mouth.  This matches the note at lines 326--355 and
  501--508.

- `n-c-013.tex:791--820` gives the exact finite stem--nonempty-cycle argument,
  retains the subsequent effectivity check, and concludes only decidability.
  It expressly refuses elementary, PSPACE, or optimal complexity and does not
  invent a worked circuit.  This matches the note at lines 357--399.

- `n-c-013.tex:822--844` presents the five post-Theorem-2 comparisons as
  source-reported consequences, preserves the undefined source label
  `Sigma_2^0`, distinguishes it from `Sigma^0`, and does not claim the cited
  historical results were reproved in the eleven-page article.  This matches
  the note at lines 401--423.

- `n-c-013.tex:846--908` does not promote Buechi's proposed axiom schema to a
  soundness/completeness theorem.  The handbook abbreviation `SC_per` is given
  an exact eliminable definition, explicit standing, necessity, and immediate
  use in Theorem 3.  The text preserves the source's `Nn` discrepancy and
  unresolved phrase “arithmetically equivalent,” extracting only the separately
  usable decidability conclusion.  It also keeps the three printed open
  problems distinct, especially verification of a supplied recursion versus
  synthesis of some recursion.  This agrees with the note at lines 425--482.

- `n-c-013.tex:910--920` accurately inventories what is printed, cited,
  outlined, and handbook-owned.  It asserts no modern determinization,
  complementation theorem name, translation-state bound, or circuit case study
  as Buechi's own.

### 4. McNaughton 1966 access-bounded presentation

- `n-c-013.tex:921--927` gives only registered identity and access status for
  the ten-page article.  It correctly says the publisher marks a version of
  record as open archive while the body was not delivered through the lawful
  routes tried; it does not infer nonexistence from access failure.  This
  matches the McNaughton note at lines 3--6, 12--62, and 96--116 and the
  bibliography entry at `handbook.bib:2290--2299`.

- `n-c-013.tex:929--938` limits positive mathematical content to McNaughton's
  contemporary Project MAC summary: an omega-event is a set of infinite
  sequences, regularity is described through state graphs, and the reported
  Kleene--Myhill analogue is finite-state iff regular.  It explicitly leaves
  the article definitions, tuple, acceptance, constructions, examples, and
  proof open.  This matches the source note at lines 118--144 and 184--221; the
  report bibliography entry is accurate at `handbook.bib:2311--2321`.

- `n-c-013.tex:940--946` keeps the separately lettered 1965 finite-game memo
  apart from the journal article and preserves McNaughton's warning that the
  memo's proof had a deep, then-unpatched fallacy.  No determinacy or
  finite-state-strategy claim is imported.  This matches the source note at
  lines 146--182.

### 5. Safra 1988 proceedings identity and 1995 expanded manuscript

- `n-c-013.tex:948--963` correctly limits the unread nine-page proceedings
  object to its authoritative abstract and metadata, while separately
  identifying the complete twenty-page author-hosted expanded manuscript, its
  preliminary-version note, its historically prospective singular journal
  wording, and its 21 March 1995 PostScript generation date.  It does not call
  the expansion a FOCS facsimile or published journal article.  This agrees
  with the Safra note at lines 1--88 and bibliography entries
  `handbook.bib:2346--2368`.

- `n-c-013.tex:965--995` gives the expanded manuscript's exact automaton data,
  total deterministic convention, run and infinity set, and Buechi, Muller,
  and Rabin semantics.  It preserves Safra's `(L_i,U_i)` order—good recurring
  first, bad eventually absent second—and explicitly prevents its exchange
  with Thomas's later `(E_i,F_i)` notation.  This matches the Safra note at
  lines 90--115.

- `n-c-013.tex:997--1036` faithfully separates the source's ordered
  vocabulary-tree data and invariants from two clearly labelled handbook
  corrections: the left-to-right relation and the inclusive-path reading of
  “specific.”  The total traversal order is defined only for deterministic name
  allocation.  Node identity, colors, labels, and specificity are not
  conflated; “specific” is eliminable and used to prove the node bound.  This
  matches the Safra note at lines 117--155.

- `n-c-013.tex:1038--1079` owns the fixed initial vocabulary name and unique
  allocation representative, then gives the expanded manuscript's six updates
  in their actual order: advance; create accepting children; horizontal
  deletion; empty deletion; collapse/color; rename.  It correctly records a
  new name as red in its creation state and derives the `n`-node bound.  This
  matches the Safra note at lines 157--184.

- `n-c-013.tex:1081--1107` identifies the source's empty-root definedness gap
  and adds exactly one rejecting total sink as a handbook completion.  The sink
  is a determinized automaton state, not a tree node; it is in every bad set and
  no good set.  The resulting acceptance is eventually-not-red and
  infinitely-green for one persistent name, with exactly `n` pairs.  This
  matches the Safra note at lines 186--202.

- `n-c-013.tex:1109--1157` gives the tree/lineage explanation and both
  correctness directions at the expanded manuscript's strength.  Soundness
  uses finite run segments visiting the Buechi set and Koenig's lemma;
  completeness follows an accepting original run through boundedly many
  leftward moves and bounded tree depth.  The examples are described as worked
  overviews, not definitions.  This matches the Safra note at lines 204--219.

- `n-c-013.tex:1159--1176` visibly repairs the source's incomplete `n^n` label
  encoding with the external absence symbol `star`, expressly an encoding
  value rather than a node or component.  It preserves the
  `2^{O(n log n)}` bound, `n` pairs, the factorial lower-bound qualification,
  and Appendix A's sketch status.  This matches the Safra note at lines
  221--241.

- `n-c-013.tex:1178--1202` keeps each application in its actual target class,
  defines “deterministic in the limit” on accepting runs, and assigns all
  detailed claims only to the expanded manuscript.  Lines 1195--1202 expressly
  prevent splicing Safra's `n` pairs into Thomas's `2n`-name presentation.  This
  matches the Safra note at lines 243--274 and 293--307.

### 6. Thomas 1996 report precursor and 1997 chapter boundary

- `n-c-013.tex:1204--1266` attributes every locator to the complete May 1996
  Kiel report, gives the exact run and infinity-set definitions, restores the
  source's total deterministic premise, and keeps Buechi, Muller, Rabin, and
  Streett conditions distinct.  Thomas's Streett pair order is stated exactly:
  recurrence in `F_i` requires recurrence in `E_i`.  This matches the Thomas
  note at lines 3--88 and 114--138.

- `n-c-013.tex:1268--1289` gives Thomas's finite-union characterization with a
  defined infinite-concatenation condition, distinguishes deterministic
  Buechi from deterministic Muller complement closure, and calls Theorem 5.4 a
  later proof of McNaughton's result rather than evidence for McNaughton's unread
  article.  This matches the Thomas note at lines 136--150.

- `n-c-013.tex:1291--1313` defines the report presentation's Safra-tree state
  completely: rooted ordered tree, changing labels, injective persistent names
  in `{1,...,2n}`, and current-update marks.  It labels the fixed initial name
  and clearing of old marks as handbook normalizations/clarifications and
  explains why name, label, and mark have different standings.  This matches
  the Thomas note at lines 150--167 and 280--304.

- `n-c-013.tex:1314--1339` preserves Thomas's create-then-advance update order,
  gives the subtree-wide horizontal deletion required for label containment,
  and supplies the empty absorbing state only when the advanced root is empty.
  The empty state is precisely defined, rejects, has no node/name/mark, and
  changes neither the pair count nor asymptotic bound.  All additions are
  labelled handbook-owned.  This matches the Thomas note at lines 168--181 and
  291--304.

- `n-c-013.tex:1340--1374` makes new-name allocation deterministic while
  withholding every predecessor name, proves the `2n` reservoir sufficient,
  and translates permanence/current collapse into Thomas's Rabin pairs.  The
  empty state is in every excluding set and no recurring set.  The `ab^omega`
  check demonstrates why marks must not persist.  The text keeps Thomas's
  `2^{O(n log n)}`/`2n` presentation and qualified lower bound separate from
  Safra's expanded-manuscript `n`-pair construction.  This matches the Thomas
  note at lines 176--196.

- `n-c-013.tex:1376--1396` states the report's Buechi/MSO equivalence and weak-
  MSO consequence while explicitly repairing Corollary 5.10's printed omission:
  a reachable nonempty cycle must contain a Buechi state.  It labels that
  accepting-cycle criterion handbook-owned rather than silently altering the
  source.  This matches the Thomas note at lines 198--204 and 280--289.

- `n-c-013.tex:1398--1409` is an exact version boundary.  The May 1996 report is
  used only as a precursor proof source; the registered 1997 chapter is not
  claimed to have been read; and the report is not allowed to close the
  McNaughton 1966, Safra 1988, or Vardi--Wolper proceedings-facsimile gaps.
  The registered chapter's bibliography identity is correct at
  `handbook.bib:2382--2391`, while all relied-on report claims cite the separate
  `Thomas1996Report` entry at `handbook.bib:2370--2380`.

### 7. Terminology and ownership discipline

- Every manuscript-added technical abbreviation is eliminable and locally
  typed: the closure/product names at `n-c-013.tex:102--218`; the cylinder,
  formula-event, and support-size names at lines 345--389; Buechi's finite-data
  translation at lines 608--640; `SC_per` at lines 854--870; Safra specificity,
  traversal, sink, good/bad sets, and absence code at lines 997--1107 and
  1159--1168; and Thomas's empty state and deterministic allocation at lines
  1329--1359.  Each distinction has stated necessity or nonredundancy and is
  used by a later construction or theorem.  The text does not name a
  hypothetical primitive where only an owed artifact is known.

- Source terms retain their original standing: Vardi--Wolper's
  semi-determinism and temporal-fragment names; Buechi's `SC`, formula classes,
  and multiperiodic finite-word languages; McNaughton's report-level quoted
  phrases; Safra's expanded-manuscript colors and pair order; and Thomas's
  report-level names and current marks.  No source-specific term is silently
  universalized across presentations.

## Open source-body and provenance obligations

The following are accurately disclosed open obligations and are not findings
against this bounded presentation:

1. **Vardi--Wolper proceedings-facsimile comparison:** open.  The mathematical
   body used is the complete author preprint, and `n-c-013.tex:9--15,
   1408--1409` expressly bars a proceedings-page identity claim.
2. **McNaughton 1966 article body:** open.  Only registered metadata and the
   narrow Project MAC first-person summary are used (`n-c-013.tex:921--946`).
3. **Safra 1988 proceedings body:** open.  Abstract-level claims remain with
   the 1988 entry; all construction detail belongs to the separately cited 1995
   expanded manuscript (`n-c-013.tex:948--963, 1195--1202`).
4. **Thomas 1997 chapter body/reconciliation:** open.  The complete May 1996
   report is cited only at explicit precursor strength
   (`n-c-013.tex:1204--1409`).

The compact ledger states that historical status fields do not themselves
close an obligation (`spec/register-obligation-closure.md:1--10`) and lists
`OBL::new-content::N-c-013` as `OPEN` with no admitted support projection at
line 308.  This Round 3 source-fidelity verdict neither edits nor purports to
close that administrative row.

REGISTER STATUS: OPEN
