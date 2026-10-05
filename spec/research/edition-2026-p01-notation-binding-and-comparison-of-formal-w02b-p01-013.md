# Packet w02b-p01-013 (P1 chapter 8; sections 8.3, 8.4, 8.6, 8.7), block 1

Provenance note for the equivalence-glyph audit (S-003-C04 / A-168-C02). Not reader text.

## Scope of this block

The assessment named one remaining gap: section 8.4, components S-003-C04 and A-168-C02.
Live uses of the triple bar had no covering registry row at
handbook/parts/p05/decidable-arithmetics.tex:17 (Presburger congruence predicate),
handbook/parts/p15/conditional-expectation.tex:355 (h identically 1/2) and
handbook/parts/p15/characteristic-functions-and-inversion.tex:399 (phi identically 1),
and nothing on the route audited every live use of the triple bar, the double arrow and the
definitional sign against the registry. The superseded sole-elementary-equivalence rule is not
implemented (policy section 7 of spec/decisions/edition-2026-coverage-policy-resolution.md).

Existing treatments found and extended rather than duplicated:
handbook/parts/p01/symbol-registry.tex (editorial defaults, lines 15-25),
handbook/parts/p01/notation-binding-and-comparison-of-formal-w02-p01-025.tex
(sec:p01-w02-p01-025-signs, def:p01-w02-p01-025-equivalence-roles, thm:p01-w02-p01-025-equiv-bridges),
handbook/parts/p14/symbols-terminology-and-glossary.tex (glossary rows for the glyphs). The last
one was not in the packet's existing list.

## Audit method

1. Reader route: tools/symbol_registry.py ReaderIndex over handbook/main.tex (1689 live files),
   with each regex hit placed at the reader position of the last preceding command, so that a
   registry scope (numeric, label, label range or named binding) can be tested for containment.
2. Occurrences: every `\equiv` (with any attached subscript or superscript), `\Leftrightarrow`
   and `\defeq` after comment and verbatim stripping: 1925 occurrences (989 definitional-sign
   macro, 622 bare triple bar, 64 double arrow, 250 subscripted or superscripted triple bars).
3. Coverage: an occurrence is covered when a row of handbook/registry/symbols.csv or an intake
   CSV with the same glyph form lies in scope; for bare forms only rows whose glyph has the bare
   sign count. Occurrences covered only by the global rows (30 editorial formula equivalence,
   32 definitional sign, 42 elementary equivalence, 6555 source definitional sign) were read and
   accepted only when the operands match that row's type (structures for row 42, formulas for
   row 30, a colon prefix for row 32).
4. Literal `\mathrel{:\equiv}` is the definitional sign (row 32). The `\defeq` macro prints
   `:\equiv` (row 32) and inside the restoration provenance scopes `:=` (row 6555, handbook.sty
   around line 1539); both roles are global, so every macro use maps to one of them by its
   printing region.
5. Family instances: subscripted forms whose index is a declared metavariable of a registered
   family in scope were mapped to that family row (rows 3717 Morley approximants, 807 Lawvere
   equational congruence, 2258 rewriting congruence, 1928 small-clause equivalence with its
   bare-chain note).

Result after adding the 77 intake rows: every occurrence is mapped to a row, except the three
first-order equivalence chains in handbook/restoration/inherited-15638-16742.tex (exercise
feedback, lines 334-335 and 994). That file carries only `ch:` and `app:` labels, which a
registry scope cannot name (tools/symbol_registry.py LABEL_RE), so a named scope binding in
handbook/registry/symbol-scopes.json is needed (blocked_policy; lead change). The same blocker
affects the earlier intake rows 9 and 12 of
handbook/registry/symbols-intake-p01-notation-binding-and-comparison-of-formal-w02-p01-025.csv
(scopes `app:exercise-feedback`, `app:notation` do not resolve).

Validation: the intake resolves with no errors through symbol_registry.read_rows, and
collision_check over symbols.csv plus the intake reports no collision involving the intake.

## Role assignments by region (intake rows)

- Presburger congruence predicate: def:p05-presburger through def:p05-presburger-example.
- Identically equal: thm:p15-conditional-examples, thm:p15-characteristic-second-moment,
  sec:p15-characteristic-function-criteria-and-moments and its annex section,
  sec:annex-p15-bayes-factor-computation.
- Metalinguistic number congruence: sec:p09-presentation-n-c-012 (n congruent n' mod 2).
- Double arrow between assertions: global (first use def:p01-w02-p01-022-setting); regions
  read: P4 complexity, Turing degrees, frontiers; P6 finite character, Suslin, absoluteness;
  P2 second-order chapters and annex.
- CPL semantic equivalence outside the named CPL scope: ten P2 body and annex sections.
- First-order equivalence and alpha-equivalence extensions: P1 annexes, P2 Craig-Beth annex,
  P7 cut-elimination and equality chapters.
- Displayed register entries: sec:p01-symbol-registry, sec:p01-w02-p01-024-notation,
  sec:p01-w02-p01-025-overview, sec:p14-symbols-terminology-and-glossary; Principia column in
  sec:p01-notation-variants.
- Object-language connectives: Church type theory (P2 040 body and annex), Lambek-Scott
  internal language (P10 n-d-023 body and annex; the calculus sheet lies inside the body
  section region), Reichenbach (P15), erotetic languages (P18 body and proofs).
- Equivalence of a declared semantics, also introducing defined operators: P9 logic in computer
  science, presentations n-c-012 to n-c-021, Stavi body and annex, finite-tree annex.
- Named relations: filter agreement (P3 Feferman-Vaught), rank agreement (P3 abstract annex),
  Morley approximants annex, equality pattern (P2 035 annex), Weihrauch (P4 body and annex),
  judgmental equality (P7 HIT, circle, identity systems and their annexes), provable
  equivalence (P10), rewriting congruence instances (P12 fair completion, rewriting annex),
  small-clause bare chains (P12 annex), Emerson-Halpern, CEGAR, tree-depth and filtration
  relations (P9 presentations), predicate definition (P15 PR learning), sentence equivalence
  (P15 systematic power), classical equivalence (P16 deductive-nomological).

## Reader text written

- handbook/parts/p01/notation-binding-and-comparison-of-formal-w02b-p01-013.tex: chapter
  sec:p01-w02b-p01-013-equivalence-audit with def:...-congruence-predicate,
  def:...-identically-equal, def:...-statement-iff, def:...-mention, def:...-role-reading,
  thm:...-congruence-definable, thm:...-identically-equal, def:...-example, def:...-failure,
  tab:...-roles.
- handbook/annex/p01/notation-binding-and-comparison-of-formal-w02b-p01-013.tex: the two
  annex proofs.
- work/waves/w02b/patches/w02b-p01-013.json: glosses at the three named sites (anchors
  verified unique).

Sources: no source-specific presentation is written. The congruence lemma is proved from the
division algorithm and the satisfaction clauses; Presburger1929 is cited only as the source of
the elimination theorem already cited by def:p05-presburger. No page locator is given.

## Pass 2 of block 1 (8.4 gaps: S-003-C02, S-003-C04, A-168-C03)

Gaps named by the assessment and what was changed.

- CPL semantic formula equivalence (symbols.csv line 129, scope `P2 prop-syntax-semantics` =
  ch:prop-syntax-semantics plus annex/p02/propositional-substitution.tex and
  annex/p02/tseitin-transformation.tex in symbol-scopes.json). The table row now names the whole
  chapter and each of its sections in reading order (sec:prop-syntax-semantics-01, -02 where the
  relation is defined at inherited-01817-01898.tex line 57, sec:p02-propositional-substitution,
  -03, sec:p02-w02-p02-003-exercise-link, sec:p02-w02-p02-004-equivalent-substitutions,
  sec:p02-w02-p02-005-idioms, -04 with inherited-01946-02186.tex lines 103-109,
  sec:p02-tseitin-transformation) and the four annex items of the two bound annex files, then the
  extension regions (intake rows 10-19), annex:p2.1.8 (propositional-metatheory-supplement.tex
  lines 97-102 lie inside it), sec:p01-w02-p01-025-substitution and item 4 of
  thm:p01-w02-p01-025-equiv-bridges. Driver order checked in handbook/parts/p02.tex lines 4-13;
  the next chapter (ch:prop-deduction) starts at inherited-02187-02192.tex line 1. No intake row
  restates the canonical chapter scope: a row with the same glyph, role and an overlapping scope
  is a `duplicate glyph-role` error of tools/symbol_registry.py collision_check.
- P8 Scott Advice whole-concept equality (symbols.csv line 3596): table row and intake row
  `\(\tau\equiv\sigma\)` (scope `P8 Scott Advice`, first use def:p08-sa-concepts); read
  parts/p08/presentations/n-b-006-01.tex lines 86-145, 280-292, 326-334 and annex lines 80-95.
  Procedure step 7 now names defined relation symbols between terms; example item 4.
- P13 Street contradictory pairing (symbols.csv line 5768): table row and intake row
  `\(\Phi\not\equiv\Psi\) (modal tables)` (scope `p13-street-2004-modal-tables`); read
  the Street 2004 presentation file under parts/p13/presentations (file stem: the source
  number, the item 0107 and original-2004) lines 325-352. New convention def:p01-w02b-p01-013-slashed (slashed
  signs), step 0 of the procedure, lemma thm:p01-w02b-p01-013-contradictory with annex proof
  annex:p01-w02b-p01-013-contradictory. No locator into Street 2004 is written here (not opened);
  the section cited carries its own citation.

Further omissions found by a fresh coverage pass and closed in the same edit:
- slashed forms (`\not\equiv`, `\not\equiv_X`) had no reading: CPL denials in P2 003/004/005/019,
  `f(b)\not\equiv_{E_0} b` in thm:p12-completion-worked and annex:p12.rewriting.example (line 320,
  outside every row; intake row added for annex:p12.rewriting.example), `d\not\equiv F` in the
  C+ annex, and registered row 5181 (negated object biconditional, causal theories).
- sec:p01-w02-p01-025-signs and -substitution use first-order equivalence, CPL equivalence,
  alpha-equivalence, number congruence and many-one equivalence in role (lemma
  thm:p01-w02-p01-025-equiv-bridges); intake rows added; the mention convention now also names
  def:p01-w02-p01-025-equivalence-roles (a separate register-entry row there would duplicate intake
  row 31, whose scope sec:p01-w02-p01-025-overview is the whole chapter).
- Vague regions replaced by the regions of their registry scopes (symbol-scopes.json): Koppelberg,
  filter agreement and its quotient, Delhomme identity atom, HoTT and HIT judgmental equality,
  preferential and ranked satisfaction, native Gold predicates, native search procedures,
  Weihrauch realizer section, Morley approximants (sec:p03-n-a-004-02 with subscripts beta and
  delta_M), many-one (frontiers annexes), provable equivalence (nonclassical algebras),
  tree-language congruence, Lawvere family, game equivalence (temporal automata), inquisitive.
  Rows for first-order equivalence, alpha-equivalence and the schematic entry now give the exact
  `through` ranges of rows 6553, 6556 and 6561, and the exercise-feedback and notation appendices.

Method of the pass: a ReaderIndex subclass (scratch, not committed) recorded every glyph
occurrence on the main.tex route with its reader position and tested it against every
registry and intake row whose glyph contains the same sign. Bare `\equiv` is always "covered"
by the global elementary-equivalence row in such a test, so bare occurrences still rest on the
operand reading of the first pass; the pass reread the bare occurrences of the CPL chapter,
P8 Scott Advice, P13 Street and P16 causal theories and the 025 chapter only.

Validation: read_rows on the intake reports no errors; collision_check over symbols.csv plus the
intake reports no collision involving the intake; every \cref target in the body and annex
exists in the tree; unit-compile ok (two overfull boxes: a convention title line and an annex
heading in the unit build).

## Block 2 (8.4 gap: S-003-C02 / A-168-C03, colon-equals printings)

Gap named by the assessment: routed source presentations print a bare `:=` as their definitional
sign outside the restoration scopes (parts/p04/weihrauch-choice-and-degrees.tex line 44 inside
def:p04-wc-tupling; parts/p08/inquisitive-propositional.tex lines 132-135 inside
def:p08-inq-language), while the role table, step 1 of the procedure and symbols.csv row 6555
confined `:=` to the restoration scopes; non-definitional `:=` roles were not distinguished.

Survey method (scratch scripts, not committed): tools/symbol_registry.ReaderIndex over
handbook/main.tex gives the reader route (1165 files); for every route file outside
restoration/ and generated/ the comment-stripped text was scanned for `:=` (616 occurrences)
and `::=` (65 occurrences). Each occurrence was classified by position: inside a bracket after
an expression (update or substitution, decided by the kind of the expression), heap form
`[e]:=`, program text (while/heap/guarded-command languages), algorithm prose (set, initialize,
update, procedure rules), instantiation of a stated letter (with/taking/instantiate, derivation
justification columns), otherwise definitional. Contexts were read for every non-definitional
hit and for every file's definitional hits (first four per file, all hits of the uncertain
files p02-002 annex, n-c-012, n-c-016, n-c-018, p07 higher-inductive-types annex, p16 remedy).
Regions are the innermost labelled heading or annex item before each occurrence, with fixes
for unlabelled inputs (the Barendregt-Geuvers subfiles -> sec:p12-har-types; kamp-iii1 -> the n-c-012
section; temporal-epistemic supplement -> the section of def:p08-ctl-semantics; the
rational-closure sheet -> sec:p08-ranked-models-rational-closure; Curry-Howard supplement ->
the section of def:p07-curry-howard). Nested regions of one role were dropped in favour of the
containing region (so n-c-019 and n-c-020 program text is covered by sec:p09-program-logics).
Counts: definitional 388 occurrences in 72 regions, instantiation 58 in 8, update 67 in 18,
substitution 18 in 6, program 61 in 4, algorithm 22 in 7, grammar production 64 in 20, plus two
register displays in def:p01-w02-p01-025-equivalence-roles.

Written: convention def:p01-w02b-p01-013-colon-equals (roles (a)-(g) and their differences);
step 1 of def:p01-w02b-p01-013-role-reading rewritten with a side condition; lemma
thm:p01-w02b-p01-013-colon-equals (eliminability of c:=t, update identities, assignment
x:=x+1 changes every state and n=n+1 has no solution) with annex proof
annex:p01-w02b-p01-013-colon-equals; example items 6-9; warning sentences; table rows for
every printing and role with regions; intake rows 89-223; two patch requests for row 6555.

Hard guard notes: G8 fixed (line 128 rewritten; escape damage on lines 122-140 repaired). G1 lists
four files of packets w02b-p01-014 and w02b-p02-036; not written by this packet in this session.

## Block 1 of r3 (8.4 gap: S-003-C02/C03/C04, A-168-C01, colon-equals inside the restoration scopes)

Gap named by the assessment: the ::= productions inside the restoration scopes and the
algorithm step `r := DPLL(...)` (restoration/inherited-14271-14350.tex line 53, inside an
lstlisting) were not recorded; step 1 and the table rows read every := in those scopes as the
definitional sign, contradicting the completeness sentence of the table section.

Survey (this pass): grep over every file in handbook/restoration/ for `::=`, literal `:=`, and
the source macro `\defeq` (160 uses); alternative spellings (`\coloneqq`, `:\!=`, `{:}=`,
`\colon=`) have no hits. Findings:
- `::=` (7 occurrences in 6 files, all on the route): inherited-01661-01816.tex:38
  (sec:prop-syntax-semantics-01; not named by the assessment, found here), 12721-12783:25
  (sec:simple-type-theory-01), 12030-12100:12,17 (sec:normalization-curry-howard-02),
  13340-13409:7 (sec:modal-temporal-epistemic-02), 13807-13861:6 (sec:relevance-linear-02),
  13939-13971:6 (sec:relevance-linear-03).
- literal `:=`: only 14271-14350:53 (sec:automated-reasoning-01, DPLL listing) and the macro
  definition in 00152-00156:4 (not reader text).
- `\defeq` uses that are not definitions (found here, not named by the assessment):
  07295-07468:103 `f_0 \defeq f` after "applied with" (sec:qe-categoricity-02; letter of
  thm:back-and-forth-test); 09150-09174:15,19 witnesses `z \defeq y`, `z \defeq Sar n` in the
  proof of lem:q-dichotomy (section sec:arithmetic-coding-01; checked: no \section between
  09080-09098 line 12 and that file); 09620-09728:65 witness `z \defeq ar q` in the proofplan
  of thm:rosser (sec:first-incompleteness-04); 15093-15206:83 register row `a \defeq b` in
  app:notation (mention). Every other `\defeq` use has a new name on its left (read in the
  grep listing; `v(p)\defeq a` in 13641-13699:43 defines the valuation v pointwise).
- verbatim/lstlisting blocks outside restoration/: scanned all parts/ and annex/ files, no `:=`
  inside them, so the block 2 survey of non-restoration text is unaffected.

Written: convention role (b) extended to witnesses with the two restoration examples; role (f)
and role (g) name their restoration-scope instances; the "only role (a)" sentence includes the
restoration printing; step 1 of the procedure now applies the position test inside and
outside the restoration scopes, with the definitional sign as the remaining case (printed :=
inside, role (a) outside); mention convention names app:notation; example items 10 (DPLL step)
and 11 (simple types grammar); warning sentences for the DPLL step and the witness; table
paragraph states that position plays the part of operand kind for colon-equals and how the
restoration rows interact; table rows: restoration definitional row now excepts the role
(b)/(f)/(g) occurrences and the register display, instantiation row + 3 restoration regions,
algorithm-step row + sec:automated-reasoning-01, grammar row + 6 restoration regions;
Sources sentence. Stray word "The" before "Reading the assignment" in the warning removed.
Intake rows 224-233 (6 grammar, 1 algorithm step, 3 instantiation). read_rows: no errors;
collision_check over symbols.csv plus intake: no collision involving the intake. Patch 5 (row
6555 notes) extended to name the restoration-scope non-definitional occurrences.
The register display in app:notation has no intake row: LABEL_RE admits no app:/ch: scope
(same open blocker as rows 9 and 12 of the w02-p01-025 intake).

## Continuation

- Lead (placement): body after `parts/p01/notation-binding-and-comparison-of-formal-w02-p01-025`
  in handbook/parts/p01.tex and annex after
  `annex/p01/notation-binding-and-comparison-of-formal-w02-p01-025` in
  handbook/annex/p01-route.tex; the three patch requests in work/waves/w02b/patches/w02b-p01-013.json.
- Lead (blocked_policy, still open): named scope binding in symbol-scopes.json for
  `restoration/inherited-15638-16742.tex` (exercise feedback, lines 334-335 and 994) and for the
  `app:notation` region, then a first-order equivalence row scoped to it; rows 9 and 12 of the
  w02-p01-025 intake use the unresolvable scopes `app:exercise-feedback` and `app:notation`.
  The reader table already names both appendices.
- Open: bare `\equiv` occurrences outside the regions reread in pass 2 were not reread one by
  one in this pass; the individual `\defeq` uses are mapped by printing region only.
- Lead (patch, block 2): two replace requests on symbols.csv row 6555 in
  work/waves/w02b/patches/w02b-p01-013.json; if applied, the 72 intake rows with glyph \(a:=b\)
  may stay as region records or be dropped in favour of the widened row (return JSON decision).
- Open (block 2): `\equiv` used to name an assertion (`\mathcal I\equiv ...` and `C\equiv[y]:=1`
  in sec:p09-presentation-n-c-020, `P\equiv ...` in sec:p09-presentation-n-c-019) is read only
  through the "also introducing defined operators" clause of the declared-semantics row; it was
  not reread one by one in this block.
- r3 block 1: restoration-scope colon-equals roles recorded (see section above). Open for the
  lead: a named scope for app:notation if the register display row `a\mathrel{:=}b` there should
  also get a registry row (blocked_policy, same binding as the earlier app:notation request).
