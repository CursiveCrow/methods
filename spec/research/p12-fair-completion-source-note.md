# Fair completion: exact procedures and persistent-rule proof

Authoring checkpoint: 1 October 2026. Author owns only
`handbook/parts/p12/fair-completion.tex`, the matching annex,
`handbook/bib/intake-p12-fair-completion.bib`,
`handbook/registry/symbols-intake-p12-fair-completion.csv`, and this note.
Shared routes, canonical bibliography and symbols remain the lead's files.

## Scope and source identity

The body distinguishes the restart/interreduction operations of
Knuth and Bendix 1970 from Huet's precisely labeled and marked
incremental algorithm published in 1981. It supplies the complete
persistent-rule correctness proof for the latter. It is not an admission
of the original Huet 1980 JACM presentation, later unfailing/ordered
completion, or completion modulo a further equational congruence.

The construction allocation identifies `ED26-REQ-N-c-037-02` with
Knuth--Bendix 1970 completion operations, critical pairs, outcomes and
the word problem. `ED26-REQ-N-c-037-03` separately allocates the exact
Huet 1980 critical-pair/confluence treatment; this 1981 paper cannot
replace that obligation. The allocation was read in
`spec/coverage/edition-2026/computational-requirements/source-allocations.jsonl`.
This chapter completes its assigned scheduling and fair-limit proof
component. It does not independently admit or rebaseline N-c-037.

Held source bodies:

- Knuth, Donald E., and Peter B. Bendix, *Simple Word Problems in Universal
  Algebras*, in John Leech (ed.), *Computational Problems in Abstract Algebra*,
  Pergamon, 1970, pp. 263--297. Held PDF:
  `tmp/pdfs/p12-reduction-orderings/knuth-bendix-1970.pdf`, 617156 bytes,
  18 physical pages, SHA-256
  `1B1F3ECAA6B4B3EE76131430A15F5AAB125DF557621755D11569DD5819738080`.
  It is a two-printed-page scan. The author's bounded reading covered
  physical pages 6--8, printed pp. 272--277, containing the local-peak
  criterion and all of sections 5--6. The independently authored KBO
  treatment is an explicit upstream dependency, not a replacement for
  the source procedure.
- Huet, Gerard, *A Complete Proof of Correctness of the Knuth--Bendix
  Completion Algorithm*, *Journal of Computer and System Sciences* 23(1),
  August 1981, pp. 11--21; received 2 June 1980, revised 12 January 1981.
  Held PDF: `tmp/pdfs/p12-fair-completion/huet-1981-correctness.pdf`,
  725589 bytes, 11 physical pages, SHA-256
  `C64C1D53A6BE57EF3B44E62EEE0AF12B6195948C6505CEFBA881E8EB5414831C`.
  All physical pages 1--11, including the introduction, algorithm,
  Lemmas 1--7 and corollaries, conclusion and references, were read.
  The [publisher record](https://www.sciencedirect.com/science/article/pii/0022000081900027)
  confirms DOI `10.1016/0022-0000(81)90002-7`, August 1981, volume 23(1)
  and pp. 11--21. The [author's publication list](https://pauillac.inria.fr/~huet/bib.html)
  independently identifies publication item 16. An initially guessed,
  unsuccessful DOI lookup was not used as evidence or saved in the intake.

The bounded source helper independently returned exact page locators and
the two algorithm distinctions below. It did not edit the manuscript or
perform an independent mathematical review. Source extraction used pypdf;
the host Poppler path was absent and the installed MiKTeX pdftotext attempt
could not create its local data directory. Those extraction failures did
not block reading the complete held Huet body with the bundled runtime.

## Source-to-manuscript bridge

Knuth--Bendix section 5, pp. 273--276, gives disjoint, substituted-variable
and nonvariable superposition cases, MGU construction, and its exhaustive
test. Equations (6.1)--(6.3), p. 276, justify adding consequences and mutually
derivable replacements. The two procedural paragraphs on p. 277 prescribe
restart after an oriented disagreement and all-rule interreduction using
the distinguished rule excluded. The body specifies repeated fixed-point
interreduction to make the scheduling operationally definite and explicitly
identifies that scheduling detail as an elaboration of the source's
all-rules instruction. It retains the original ordering name and does not
claim the source specified the elaboration's replacement order.

Huet p. 13, physical page 3, is the exact mathematical
macrostep specification. In particular:

- New rules use fresh increasing labels and start unmarked.
- A collapsed old left side deletes its label and generates an equation
  against its old right side.
- Retained records keep left sides, labels and marks; their right sides
  are normalized under the pre-insertion rules together with the new rule.
- A marked surviving rule need not be marked again merely because its
  right side changed.
- The pending-equation phase finishes before another critical-pair phase.
- Selecting label k computes every critical pair with current labels at
  most k, in both overlap directions and including self-overlaps.

Lemma 4, p. 15, also mentions a permitted implementation variant using
already-reduced right sides during normalization. The chapter fixes the
displayed algorithm's pre-insertion-plus-new rule set; it does not mix
that choice with a different unproved schedule.

Huet pp. 14--15, Lemmas 1--4, supply persistent reducibility, soundness,
equation-loop termination and interreduced states. The fairness hypothesis
on p. 15 applies to every allocated label, not to equation selection.
The chapter uses the least unmarked live label as its constructive
scheduler. Source Lemma 5, pp. 15--16, provides historical-version coverage;
Lemma 6, pp. 16--18, gives the nested induction transferring historical
reductions to persistent joins. The chapter proves both inductions and
every branch explicitly, including a concrete two-coordinate rank for
strict pattern containment. This avoids relying on a bare assertion that
two well-founded relations have a well-founded composition.

The source defines the persistent limit by eventual unchanged membership
on p. 14. The labeled reconstruction defines final right sides of
never-deleted labels, proves their finite stabilization, and only then
identifies this with eventual unchanged labeled membership. It records
the distinction between all historical versions and this limit.

Huet p. 19 supplies semidecision by progressive normalization, finite-limit
termination, and the infinite-antichain corollary. These are all written
and proved. The conclusion, pp. 19--20, says pair-at-a-time and
occurrence-at-a-time implementations need different bookkeeping and
revised fairness. Permutative and Peterson--Stickel incremental extensions
are conjectural there. The chapter preserves those boundaries; no
associative-commutative completion theorem is inferred from the ordinary
term-language antichain criterion.

## Complete written proofs and examples

The body and annex now have ten reciprocal statement/proof pairs:

1. Termination of a finite interreduction phase and correctness of a
   successful freshly scanned restart output.
2. Valid rule orientation, one common reduction ordering, interreduced
   states, finite equation phases, joining every pending equation,
   equational consequences, and stabilization of persistent right sides.
3. Well-founded strict pattern containment, strict collapse decrease,
   and persistence of reducibility.
4. Historical-version critical-pair coverage for every persistent peak,
   including disjoint, variable and nonvariable overlaps.
5. Full simultaneous well-founded proof of historical reduction transfer,
   persistent confluence, historical-union confluence and theory equality.
6. Finite success, finite limit implies termination, and equality
   semidecision during a fair infinite nonfailure run.
7. The infinite persistent left-side antichain and the conditional
   termination consequence for languages without infinite such antichains.
8. The least-label scheduler and the explicit three-label collapse run.
9. The 1970 associativity superposition example, its precise KBO data,
   every overlap and its canonical ordered leaf sequences.
10. The variable-swap obstruction to orienting commutativity and a
    separate direct decision of the pure-commutative word problem.

The associativity example explicitly uses a finite signature consisting
of one binary operation and at least one constant. It supplies the exact
nullary-symbol condition of the upstream historical KBO, any strict total
symbol precedence, all positive symbol weights, the variable weight, and
every reduction in the nontrivial critical peak. The failure example
proves both forbidden orientation directions by exchanging its two
variables. The common-order boundary also exhibits two individually
terminating singleton systems whose historical union cycles.

## Author checks, integration and outstanding work

The complete saved body and annex were read sequentially. Source matching
confirmed the insertion normalization set, old marks, increasing labels,
source failure exits and fairness conditions. The associativity signature
was made explicit during this read-through so that both its canonical
leaf-sequence argument and imported historical KBO hypotheses agree.
The actual collapse run, associativity peak and swap counterexample were
calculated directly. No software test was added to mirror manuscript prose.
The containment-rank proof was corrected during the final sequential
read: an equal-node-count substitution may map a variable to a constant,
not only to another variable. The proof now considers both single-node
images, and derives invertible variable renaming only when the distinct
variable counts are also equal. The displayed rank and theorem remain
unchanged, with the missing branch supplied.

The intake has one new bibliography key, `Huet1981CompletionCorrectness`,
and thirteen symbol rows. `KnuthBendix1970` already exists canonically.
Body and annex are ready for lead routing adjacent to the existing
rewriting/completion treatment. The lead owns all driver, shared-sheet,
canonical bibliography and canonical symbol changes. The source intakes
are preserved.

The source-specific original Huet 1980 full presentation and the other
N-c-037 source facets remain separate. This authoring completion does not
establish their completion, independent acceptance, manuscript compilation,
render quality, publication rights or reproduction gates. Consolidated
reviews and manuscript builds/renders remain after the complete writing
and correction batch under the user's instruction.
