# w02-p01-025 (P1 chapter 8: 8.3, 8.4, 8.7) -- research note

## Provenance

- Body: handbook/parts/p01/notation-binding-and-comparison-of-formal-w02-p01-025.tex
  (\chapter, label_tag p01-w02-p01-025; insertion after parts/p01/symbol-registry in handbook/parts/p01.tex,
  after the sibling w02-p01-024 chapter if both are placed there).
- Annex: handbook/annex/p01/notation-binding-and-comparison-of-formal-w02-p01-025.tex
  (insertion after annex/p01/equivalence-closure-and-quotients in handbook/annex/p01-route.tex).
- Symbol intake: handbook/registry/symbols-intake-p01-notation-binding-and-comparison-of-formal-w02-p01-025.csv (7 rows).
- No intake .bib: the only citation is Kleene1952, already in handbook.bib.
- Patch requests: work/waves/w02/patches/w02-p01-025.json (3 ops: first-order-calculi-supplement.tex replace;
  propositional-substitution.tex insert_after thm:p02-replacement; frontmatter.tex insert_after the notation paragraph).

## Sources opened in this session

- Kleene 1952, held PDF source/references/acq-r1-ACQ-2026-10-0230/kleene-1952-introduction-to-metamathematics-1974-reprint.pdf
  (text layer extracted with pdftotext). Seen: section 73 "The predicate calculus with equality", page header 399:
  axiom 22 (a = a), schema 23 (a = b implies (A(a) implies A(b))), (A) equality axioms for = and the n open equality
  axioms of an n-place predicate letter; terms are variables in the pure predicate calculus with equality. Cited as
  \cite[\S 73, p.~399]{Kleene1952}. Pages 400-401 (Theorem 39/40 proofs, quotient by the equivalence relation Q)
  were seen but not cited.
- Handbook text read and used: restoration/inherited-03240-03428.tex (substitution, complexity, alpha, fv lemma),
  inherited-03519-03680.tex (satisfaction, cor:alpha-invariance, first-order equiv definition lines 150-160),
  inherited-03927-04061.tex and inherited-04062-04108.tex (ND_FOL rules incl. exact Exists-E wording "absent from",
  source symmetry example, LK =L and source symmetric-replacement paragraph), inherited-04576-04712.tex
  (lem:equality-congruence), inherited-03166-03239.tex (complexity c), inherited-01661-01816.tex (defined
  biconditional with \defeq), inherited-01554-01579.tex (P1 metalinguistic equiv), inherited-05043-05131.tex
  (thm:upward-ls elementary equivalence wording), inherited-05132-05567.tex (lem:rectified-variant),
  inherited-02933-03021.tex (ex:prop-metatheory-09), inherited-15638-16742.tex (feedback for ex 9),
  parts/p02/propositional-substitution.tex + annex, parts/p02/first-order-calculi-supplement.tex + annex,
  parts/p07/equality-lk-metatheory.tex + annex item p7.eqlk.replacement, registry/calculi/nd-fol.tex, lk-eq.tex,
  handbook.sty lines 216 and 1539-1543, symbols.csv rows 30, 32, 129, 160, 3717.

## Existing treatments found (A9)

- Listed and linked: inherited-03240-03428.tex (FLRV1 U00236-U00246, on route), inherited-03519-03680.tex,
  first-order-calculi-supplement.tex (thm:p02-equality-laws), symbol-registry.tex (tab:p01-notation-variants for A-025),
  inherited-02933-03021.tex, inherited-15638-16742.tex, propositional-syntax-semantics.tex (off route; its
  cited=Kleene1952 thm:p02-replacement duplicate label was not counted or referenced).
- Not listed: parts/p07/equality-lk-metatheory.tex -- thm:p07-eqlk-replacement (LK_eq symmetry and the opposite-oriented
  replacement, proved at annex:p7.eqlk.replacement), thm:p07-eqlk-congruence, thm:p07-eqlk-cut-failure,
  thm:p07-eqlk-nd. The chapter links these instead of re-deriving the kernels; the new corollary
  thm:p01-w02-p01-025-lk-symmetric only states the rule form.
- Not listed: parts/p02/propositional-substitution.tex is the active home of thm:p02-replacement.
- The source paragraph at inherited-04062-04108.tex:36-46 already derives the LK symmetric replacement in prose.

## Decisions and open items

- Exists-E "absent from" read as "does not occur" (the source contrasts it with "free in no" at
  inherited-04306-04575.tex:45); all eigenvariable choices in the annex respect that reading, and Eq is defined to
  contain every choice of distinct bound variables so that axioms can be renamed away from an eigenvariable.
- The replacement-from-axioms proof uses substitution sequences to avoid needing a separate
  "substitution respects alpha-equivalence" lemma, which the source does not state.
- Sheet labels (sheet:nd-fol, sheet:lk-eq) are printed as \texttt names without \hyperref, because unit-compile's label
  index does not know \calculussheet labels and fails on them.
- Overfull boxes: 13 in the unit build, mostly annexitem headings with long labels and the substitution-sequence
  paragraph (cosmetic).
- symbols.csv:160 note and nd-fol.tex comment still say equiv is "reserved globally for elementary equivalence"; that
  is superseded by policy section 7 but lies in canonical files this packet cannot edit.

## Block 2 additions

- Source uses of the triple bar surveyed with a script over every handbook/restoration/inherited-*.tex file, mapped to
  source/formal-logic-reference.tex lines and source section labels (opened this session). Bare or subscripted uses
  outside the earlier-recorded scopes: inherited-08439-08709.tex:78 (source 8516, sec:decision-hierarchy-02, proof of
  lem:goedel-beta, t equiv a_i pmod 1+(i+1)m); inherited-15638-16742.tex:334-335 and 994 (source 15971-15972 and 16631,
  app:exercise-feedback, solutions for ex:fol-cardinality-normalforms-05 and ex:automated-reasoning-03);
  inherited-14729-14778.tex:42 (sec:latex-style-01); inherited-15093-15206.tex:79 (app:notation table);
  inherited-15240-15488.tex:110 (sec:rule-sheets-01, equiv_alpha side condition); inherited-08898-09079.tex:155-164
  (sec:decision-hierarchy-03, rem:jump-convention, equiv_m; registered row 264 scope 'P4 frontiers-computability'
  starts at handbook/parts/p04.tex:78, after this restoration input at p04.tex:74).
- Convention def:p01-w02-p01-025-equivalence-roles: item 1 scope extended to the two feedback solutions; item 4 scope
  extended to the rule sheet; new items 5 (schematic register entry), 6 (number-theoretic congruence), 7 (many-one
  equivalence). Bridge lemma part 5 (remainder) with annex proof (5). Six intake rows added (rows 9-14 of the CSV).
- Patch op 2 rewritten so it cites only labels already on the route (no dependence on the P1 chapter 8 insertion).
- Guard: the four spec/research/edition-2026-p02-unit-accounting-w02-p02-042/044 files are untracked files of other
  packets; this packet did not write them and cannot modify them.
- source/formal-logic-reference.tex is not an entry of spec/coverage/edition-2026/held-sources.json, although the
  packet declares it in units[].held_paths and its sha256 matches the packet record; the lead may add it.

## Continuation

Block 2 written: 8.4 role/scope records (convention items 1, 4-7, bridge part 5, intake rows 9-14) and the standalone
patch op 2. Remaining items need the lead: (1) insert the body input after parts/p01/symbol-registry in
handbook/parts/p01.tex (line 39) and the annex input after annex/p01/equivalence-closure-and-quotients in
handbook/annex/p01-route.tex (line 4); until then D-P2-010-GOAL-03 (forward link) and all D-P3-011 goals are
off-route; (2) apply patch ops 1-3 (op 1 needs the insertion, op 2 does not); (3) merge the symbol intake; named
scopes in rows 1, 3 and 4 may need symbol-scopes.json entries; (4) optionally add source/formal-logic-reference.tex
to held-sources.json.
