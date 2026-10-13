# Packet w02ca-p01-018: equivalence and colon-equals role records (section 8.4)

Provenance note for packet w02ca-p01-018 (part P1, chapter 8, section 8.4),
block 1. Units ED26-REQ-A-168-01 and ED26-REQ-S-003-01; governing text is
policy section 7 of spec/decisions/edition-2026-coverage-policy-resolution.md
(lines 137-151, read this session).

## What was changed

No new body or annex file was written: the duties are completions of the
existing records in the editable hosts.

Host handbook/parts/p01/notation-binding-and-comparison-of-formal-w02b-p01-013.tex:

- def:p01-w02b-p01-013-identically-equal (lines 62-113): region list extended
  with f\equiv1/K (thm and annex of p15-030 Kemeny-Carnap) and every other
  routed function-identically-constant occurrence found by the sweep below
  (p15-064, p15-065, p15-057, p15-061, p15-073, p15-043, p15-008, p15-012,
  p15-022, p15-042, and this chapter's own lemma and annex); real-valued
  functions read through the inclusion of R in C.
- def:p01-w02b-p01-013-mention (lines 132-161): adds the registry extracts
  sec:p01-w02b-p01-012-extracts, the front-matter section "Calculi, notation,
  and source conventions" (frontmatter.tex line 94, no label), the Mahajan
  display in def:p15-approximation-relations, and this chapter outside the
  lemmas of sec:p01-w02b-p01-013-facts.
- def:p01-w02b-p01-013-role-reading: step 7 (line 337 ff.) names a declared
  metalinguistic relation between objects that are neither structures nor
  formulas (def:p15-w02b-p15-045-pair); side conditions (line 356-358) route
  displayed occurrences to the mention convention.
- tab:p01-w02b-p01-013-roles (lines 615-976):
  - role (a) row: sec:p09-elpp-query-correctness replaced by
    sec:p09-presentation-n-c-010 (the paragraph label did not contain the
    DL-Lite lines 1075, 1103, 1185); added sec:p09-kamp-present-progressive and
    sec:p09-stavi-completeness (in print, the later N-c-012 subsubsections
    fall under these two input subsections), part 1 of
    thm:p01-w02b-p01-013-colon-equals, annex:p15-w02b-p15-065-outer-fubini.
  - role (b) row: annex:p02-w02b-p02-008-lem, annex:p02-w02b-p02-026-eq-resolution,
    annex:p15-w02b-p15-027-absolute-equalities.
  - role (c) row: parts 2 and 3 of thm:p01-w02b-p01-013-colon-equals and
    annex:p01-w02b-p01-013-colon-equals.
  - role (e) row: the command x:=x+1 of part 3 of the same lemma.
  - role (f) row: sec:p09-elpp-query-correctness replaced by
    sec:p09-presentation-n-c-010 (PR:=\{q\}, PR':=PR at lines 1277-1278);
    now agrees with intake rows 102 and 204 of the w02b-p01-013 intake CSV.
  - role (g) row: sec:p09-kamp-present-progressive, sec:p09-stavi-completeness
    (n-c-012 lines 1260, 1926).
  - U\equiv V row: sec:p15-w02b-p15-025-annex.
  - F\equiv G row: sec:p15-w02b-p15-030-eg; def:p15-w02b-p15-029-almost,
    thm:p15-w02b-p15-029-regular-c, annex:p15-w02b-p15-029-regular-c;
    sec:p15-w02b-p15-030-nn, annex:p15-w02b-p15-030-truthlikeness.
  - t\equiv a (mod n) row: sec:p15-w02b-p15-027-bernoulli and three p15-027
    annex items.
  - new rows: \mu_1\equiv\mu_2 (same null sets; p15-045 and its annex),
    and the displayed Mahajan sign (def:p15-approximation-relations); both
    were already in registry/symbols.csv but absent from the table.
- Sources paragraph: one sentence on the two new rows.

Owned intake CSV handbook/registry/symbols-intake-p01-notation-binding-and-comparison-of-formal-w02c-p01-018.csv:
56 rows, one per newly registered region.

Patch request work/waves/w02ca/patches/w02ca-p01-018.json: S-003-C03,
symbol-registry.tex lines 138-142 (read-only host), scoping the sentence
that says \Leftrightarrow is not an object-language operator.

## Sweep method

A script walked the \input route from handbook/main.tex (1810 files), tracked
the sectioning and environment labels around every occurrence of `:=`,
`::=` and `\equiv`/`\not\equiv`, and compared them with the labels cited in
the matching table rows and in the identically-equal and mention
conventions. After the edits: `:=` 1092 occurrences, the only one outside a
cited label is frontmatter.tex line 94 (named in words in the mention
convention); `::=` 140 occurrences, none outside; `\equiv` 1486 occurrences,
82 outside a cited label, each checked by hand as covered by a row phrase the
script does not parse ("everywhere" for structures, "with its annex proofs",
"X to Y" annex ranges, editorial `:\equiv`). Restoration files were not
swept for regions (the table assigns them wholesale).
`\Leftrightarrow` rows are "everywhere" except two source-local rows; not
re-swept beyond the assessment.

## Continuation

- All listed MP-0 and MP-1 items written in the hosts and the intake CSV.
- S-003-C03 waits on the lead applying the patch request.
- unit-compile cannot run for this packet: its owned body and annex .tex
  files do not exist, because no new body text was needed. A scratch build of
  the edited host chapter and its annex with the same unit template compiled
  without errors.
- r2 (2026-10-10): Emerson-Jutla := gap closed in the host. Role-(a) row and
  update row (c) of tab:p01-w02b-p01-013-roles list
  sec:p09-presentation-n-c-018-emerson-jutla (Succ(d,i):= at n-c-018.tex
  line 2879; 'under X:=S' at lines 3261, 3268, all in paragraph
  sec:p09-streett-response-record). Item (c) prose names the two n-c-018
  subregions. Two intake CSV rows added. Scratch build of host chapter and
  annex: no LaTeX errors. S-003-C03 still waits on the lead's registry patch.
- block 2 (2026-10-10): motive-letter gap in annex:p12.har.prime-equality closed.
  - New owned chapter parts/p01/notation-binding-and-comparison-of-formal-w02c-p01-018.tex
    (lines 1-337) and annex (lines 1-125): def:p01-w02c-p01-018-motive,
    def:p01-w02c-p01-018-motive-reading (rule letter -> role (b), new name -> role (a)),
    thm:p01-w02c-p01-018-motive-readings (one value: readings agree; two lines can
    never both be role (a); role (a) + later different value -> two meanings),
    thm:p01-w02c-p01-018-equality-instances (types y=x, f x=f y, x=w; the two
    region-wide role-(a) readings change a conclusion or need x=y convertible
    with y=x), worked example over every predicate := line of the Harper Part 12
    proofs, warning, relationships. Citation: Barendregt1992 Lemma 5.2.13 item 2,
    p. 221 (generation lemma for PTSs), read in the held publisher's scan
    source/references/acq-r1-ACQ-2026-10-0030/barendregt-1992-lambda-calculi-with-types.pdf
    (PDF page 106, running head 221). The Barendregt-Geuvers 2001 held PDF has no
    extractable text (Type 3 fonts), so no locator from it was used.
  - Host tab:p01-w02b-p01-013-roles: role-(a) row (lines 682-694) now names the
    role-(a) lines of prime-equality (no_conf n), prime-divisor (B_n),
    autarkic-square-root (M, q), autarkic-interpreter (nu_x, X) and
    autarkic-substitution (nu_sigma); role-(b) row (lines 716-726) adds the motive
    lines of those five proofs. Item (b) of def:p01-w02b-p01-013-colon-equals
    (lines 222-229) names the three P(z):= lines.
  - Sweep of every := in the Harper annex files: P_0 (leibniz), Q n (prime-order),
    P(p) (prcompiler-ok, form induction has no displayed bound letter) stay role (a).
  - Intake CSV: five p:=s rows appended (one per region).
  - unit-compile ok; scratch build of host + new chapter: no errors, new labels
    resolve from the host.
  - G1 (spec/research/...p02-002...md modified): not touched by this packet in this
    session; it belongs to packet w02ca-p02-002. No action taken.
- r3 block 1 (2026-10-10): := registration for the motive chapter and annex:p10.adjoint.2.
  - def:p01-w02b-p01-013-mention (host lines 162-182) now covers
    sec:p01-w02c-p01-018-motives and sec:annex-p01-w02c-p01-018-motives: sign named,
    table-row forms named, schematic forms (role from def:p01-w02c-p01-018-motive-reading),
    quoted Part 12 lines (role of their region); items 1-3 of
    thm:p01-w02c-p01-018-equality-instances excepted as role (b) and listed in the
    role-(b) row (host lines 770-773).
  - annex:p10.adjoint.2: all five := (adjoint annex lines 109, 215, 263, 280, 291) apply
    rule Subst (def:p10-contextual-first-order; sheet rule Subst) to a sequent with a
    displayed context. Item (d) and step 1 of the procedure now give them role (d),
    item (b) excludes them, the role-(d) row names the five phrases, the role-(a) row
    no longer lists the region (no role-(a) occurrence there).
  - Intake CSV: four rows (two mention scopes, role (b) for the lemma, role (d) for
    annex:p10.adjoint.2). Patch request: delete symbols.csv row 8262 (role (a) for
    annex:p10.adjoint.2) and row 144 of the w02b-p01-013 intake CSV.
  - unit-compile ok; scratch build of host + chapter + annexes ok; check.py clean for
    these files; find_fused_spaces clean.
- r3 block 2 (2026-10-10): hard-guard items.
  - G10: rerun of `python -B tools/waves.py unit-compile` on the unchanged files reported
    ok with Barendregt1992 resolved (unit.bbl has the entry; unit.bcf present). The earlier
    "Cannot find unit.bcf" failure did not reproduce; the build directory
    tmp/unit-builds/w02ca-p01-018 is shared by every run for this packet, so a concurrent
    run is the likely cause. The one overfull box (lemma title of
    thm:p01-w02c-p01-018-equality-instances, then the annex heading, whose long annex id
    cannot break) was removed: body title now "Three uses of the equality eliminator in
    the Harper development"; annex title "Equality-eliminator uses in Harper's
    development". unit-compile: ok, overfull 0.
  - G1: spec/research/edition-2026-p02-categorical-syllogistic-and-existential-import-w02-p02-002.md
    was last written 2026-10-10 06:41, before this packet's first file of the round; the
    diff rewrites every line with the same text (line endings). Not this packet's file;
    not touched or reverted (A8).
  - find_fused_spaces clean on the four .tex files; check.py --tree handbook shows no
    finding located in this packet's files.
  - S-003-C03 still waits on the lead applying work/waves/w02ca/patches/w02ca-p01-018.json
    (symbol-registry.tex lines 138-142); the symbols.csv row-8262 deletion in the same
    file is also unapplied.
- r4 block 1 (2026-10-10): assessor gaps on := / ::= / equiv_n registration.
  - Role (g): the p09 n-c-009/010/011, n-c-016 (four subsubsections), n-c-017
    biere-ectl-certificates, n-c-018 kozen / bradfield-stirling (with
    modal-parity-automata) and n-c-021 productions were already inside
    sec:p09-description-logics, sec:p09-model-checking and sec:p09-program-logics
    (subsection rule of the table); the row now names each subsection and line.
  - Role (f): sec:p09-model-checking names the Baier-Katoen steps T:=Sat(...)
    (n-c-016.tex lines 1897, 1904).
  - Role (b): five HIT motive lines (annex/p07/higher-inductive-types.tex lines 31,
    44, 71, 145, 209), the hub data lines H(r,r'):=u, S(r,r',x):=v(x) (lines
    265-266) and the witness P:=Reach (annex p01-023 line 28) moved from role (a)
    to role (b). def:p01-w02c-p01-018-motive now allows K = Prop or a universe;
    new example def:p01-w02c-p01-018-hit-example. Binding definitions:
    def:p07-hit-circle (parts line 93), -interval (138), -pushout (220),
    -set-quotient (306). The assessor's "line 179" is the suspension, not used.
  - equiv_n row: names sec:p09-gpss-complete-order-complement (lines 56, 73) and
    annex:p9.hr.ordinal.game (annex line 119); role text matches the definition.
  - Sweep of every ::= in routed files: all now lie in a named region of row (g).
    Found outside: w02c-p01-017 chapter lines 62, 64 (not routed; reported).
    parts/p02/propositional-syntax-semantics.tex and second-and-higher-order-logic.tex
    contain ::= but are not routed.
  - Patch request: delete six role-(a) rows in symbols.csv and six in the
    w02b-p01-013 intake CSV.
  - unit-compile ok; scratch build of host + chapter ok (2 overfull boxes in
    unchanged host text); check.py clean for these files; fused spaces clean.
