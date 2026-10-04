# Part VI admission board, round 1: adversarial-publication review

Reviewer: adversarial-publication seat  
Mode: blind source/content review of the live reader graph; no other Part VI seat transcript was read.  
Disposition: **not source/content admissible in the current bytes**.

I read the charter, both roots, all 23 exact-source wrappers and their inherited
artifacts, every routed editorial body and annex addition, and the Part VI
portions of the generated theorem and symbol lookup surfaces. I performed no
build, test, render, or manuscript/control/generated-file edit. A read-only
route traversal found 62 reachable files, no missing `\input` target, and no
second live inclusion of a reachable child. A read-only lexical lookup found no
unresolved Part VI `\ref`/`\hyperref` target and no missing bibliography key;
those observations are source-level only and are not a claim that links,
citations, pagination, or floats render correctly.

## Findings

### F1 — blocker — reader-visible admission debt remains the title of required apparatus A-058

- **Location:** `handbook/parts/p06/zfc-axiom-table-supplement.tex:15-18`.
- **Evidence:** the live route prints `OPEN ZFC axiom-table apparatus`, then
  prints **OPEN and unadmitted**, and says that the apparatus closes no source,
  content, AI, build, visual, register, or acceptance gate. The file is live at
  `handbook/parts/p06.tex:5`.
- **Failure path:** a reader entering Part VI reaches a required ZFC reference
  table through a section whose own heading and first sentence deny admission.
  This directly violates the charter's prohibition on reader
  OPEN/unadmitted/internal-workflow prose (`charter.md:10-16`) and prevents any
  claim that Part VI is reader-ready.
- **Exact correction:** replace the printed OPEN heading and gate disclaimer
  with an ordinary descriptive heading and a truthful reader source note. Keep
  administrative gate state outside the manuscript. Preserve
  `tab:p06-zfc-axioms` and the table's actual side conditions.
- **Status:** **open, source/content**.

### F2 — blocker — cardinal trichotomy uses an undefined comparison relation

- **Location:** `handbook/restoration/inherited-10559-10674.tex:4-14` and
  `handbook/parts/p06/cardinals-choice-supplement.tex:218-225`.
- **Evidence:** the exact source defines equipotence and explains when
  `\lvert A\rvert` is licensed, but it does not define “the size of (A) is
  strictly smaller than the size of (B).” The supplemental trichotomy theorem
  nevertheless uses that phrase twice and says comparison is understood in
  Section `sec:cumulative-hierarchy-04`, the exact section that lacks the
  promised injection/no-reverse-injection clause.
- **Failure path:** the reader cannot eliminate either strict-size alternative
  to a formula over sets, so “exactly one” has no fixed meaning at the theorem's
  point of use. In particular, it is unclear whether strict comparison means an
  injection without a reverse injection, an injection without a bijection, or
  an ordinal-cardinal inequality that would already presuppose
  well-orderability. This also violates the supplied technical-name rule:
  standing and exact definition are owed at the use site.
- **Exact correction:** before `thm:p06-cardinal-trichotomy`, define “size at
  most” by existence of an injection (A\to B) and “strictly smaller” by an
  injection (A\to B) together with nonexistence of an injection (B\to A).
  State that these are relations among arbitrary sets and do not presuppose
  ordinal-cardinal assignment; then make the theorem refer to that definition.
  Do not duplicate the already exact equipotence definition.
- **Status:** **open, source/content**.

### F3 — blocker — the ccc/nice-name package is outside its declared model scope and uses an undefined bare forcing relation

- **Location:**
  `handbook/restoration/inherited-10770-10825.tex:4-19`,
  `handbook/restoration/inherited-11012-11052.tex:31-40`,
  `handbook/parts/p06/constructibility-forcing-supplement.tex:93-140`, and
  `handbook/annex/p06/constructibility-forcing-supplement.tex:13-99`.
- **Evidence:** the exact convention fixes the externally countable transitive
  (M\models\mathsf{ZFC}), (mathbb P), its order, and names only “for the
  remainder of this section.” The live ccc supplement is a later section,
  after the exact relative-consistency section. Its nice-name theorem uses
  (M), (mathbb P), (G), (M[G]), and (p\forces\nu\subseteq\check\omega)
  without renewing that scope. The exact source's forcing boundary explicitly
  says that the manuscript has defined only the external semantic relation and
  has **not** introduced a local recursive relation. The annex then repeatedly
  uses bare `\forces` while saying only “Work in (M), using Choice.”
- **Failure path:** the theorem and proof have no live declaration fixing what
  (M), (mathbb P), (G), or bare (p\Vdash\varphi) denote. A reader cannot
  tell whether bare forcing is the defined semantic relation, the cited
  recursive assertion, or an unintroduced third relation, and therefore cannot
  type-check either the nice-name reduction or its truth-lemma steps. The
  preservation theorem also does not inherit the expired countability/
  transitivity/background convention merely by proximity.
- **Exact correction:** begin the supplemental section with a live convention
  that explicitly fixes the required transitive (M\models\mathsf{ZFC}),
  (mathbb P\in M), order orientation, external (M)-generic (G), and the
  location of internal versus external cardinal computations. Define bare
  (p\forces\varphi(\bar\nu)) as the recursively defined assertion imported by
  the cited forcing theorem, or replace every use by the already defined
  semantic notation and cite its equivalence. Repeat the minimum standing at
  the annex entry or make an explicit reciprocal reference to the renewed
  convention. Then restate the body hypotheses at the exact strength each
  theorem consumes.
- **Status:** **open, source/content**.

### F4 — major — the reader is given two identities for poset filters and dense sets

- **Location:**
  `handbook/restoration/inherited-10770-10825.tex:4-18`,
  `handbook/restoration/inherited-10826-10881.tex:1-55`, and
  `handbook/parts/p06/forcing-vocabulary.tex:50-82`; route order is fixed by
  `handbook/parts/p06.tex:13-29`.
- **Evidence:** the exact forcing chapter first fixes the stronger-is-smaller
  orientation and gives the full definition of poset filter and dense set. The
  later “Forcing-order vocabulary” section repeats the orientation and prints a
  second labelled definition `def:p06-poset-filter`. It appears only after all
  exact forcing and CH/non-CH material, so it is not definition-before-first-
  forcing-use; later editorial references select only the second identity.
- **Failure path:** the reader encounters one unlabelled exact definition and
  later a new labelled definition of the same technical object with no explicit
  alias or controlling-identity statement. Retrieval goes to the duplicate,
  while the exact proof route was written under the first. This obscures which
  identity controls the supplemental theorems and compounds F3's bare-forcing
  ambiguity.
- **Exact correction:** retain the exact source definition as the sole
  controlling identity. Supply a governed destination/hook for it, and make the
  later lookup section refer to that destination while defining only genuinely
  new vocabulary such as ccc and `\operatorname{Add}`. If a compact restatement
  is retained for usability, mark it explicitly as a non-normative repetition
  of the exact definition rather than declaring a second definition identity.
- **Status:** **open, source/content**.

### F5 — major — the source/editorial boundary is hidden in comments, and the few printed source notices use a stale part identity

- **Location:** representative derivative headers are
  `handbook/parts/p06/ordinal-rank-supplement.tex:1-14`,
  `handbook/parts/p06/cardinals-choice-supplement.tex:1-13`,
  `handbook/parts/p06/constructibility-forcing-supplement.tex:1-13`,
  `handbook/parts/p06/forcing-variants-supplement.tex:1-12`, and
  `handbook/annex/p06/cardinals-choice-supplement.tex:1-11`; the printed stale
  wording is at `handbook/parts/p06/infinitary-combinatorics.tex:395-403` and
  `handbook/parts/p06/determinacy.tex:107-127`. The exact-scope environment is
  explicitly nonprinting control syntax at `handbook/handbook.sty:1153-1162`.
- **Evidence:** necessity/definition/standing/nonredundancy/source-disposition
  material for the routed historical derivatives exists only in `%%` comments.
  The restoration wrapper itself emits no reader label. Where the reader does
  receive source prose, it refers without qualification to “the inherited Part
  VII” and “migrated Part VII” while the live book calls this reader unit Part
  VI.
- **Failure path:** a reader cannot distinguish exact inherited bytes from
  historical derivatives and newly sourced additions by inspecting the
  artifact. The unexplained “Part VII” wording appears to be a broken internal
  part reference rather than a historical source-version designation. That
  makes nonreplacement and proof-status claims unverifiable from the reader
  surface.
- **Exact correction:** add one visible Part VI source map, supplemented where
  necessary by short chapter/annex reader notes, identifying the 23 exact
  source intervals and each distinct editorial/historical addition and stating
  that the latter do not replace or promote the exact source. Change printed
  “Part VII” phrases to “historical v1.1 Part VII source” (or another explicitly
  defined historical designation). Keep administrative admission state out of
  those notes.
- **Status:** **open, source/content**.

### F6 — blocker — required A-113 is deliberately absent, and its generated candidate cannot safely be routed

- **Location:** `handbook/parts/p06.tex:37-38` and
  `handbook/generated/audit-p06.tex:1-43,61-73`.
- **Evidence:** the root says `generated/audit-p06` is intentionally OPEN and
  unrouted because it scans retained overlapping history. The current generated
  table would print `--` as the ID for exact results and bold **unclassified**
  proof statuses for Set recursion, ordinal trichotomy, transfinite recursion,
  the hierarchy theorem, Mostowski collapse, Hartogs, AC equivalence, and the
  constructible-class theorem.
- **Failure path:** A-113 (“per-part audit registers,” must) has no reader route.
  Merely adding the existing file would introduce precisely the unclassified
  status/internal-construction debt forbidden by the charter and would not
  give stable retrieval destinations for the exact results.
- **Exact correction:** regenerate the Part VI register strictly from the live
  62-file reader graph; give every exact and editorial row a stable reader
  destination; classify inline proof, proof sketch, cited theorem, annex proof,
  and annex sketch from the actual reader prose; remove all `--`/unclassified
  output; then route the table exactly once at the governed Part VI location.
- **Status:** **open, source/content**.

### F7 — blocker — A-159's completeness claim omits unlabelled exact-source theorems and its printed count is stale

- **Location:** `tools/build_named_theorem_index.py:1-3,99-143`,
  `handbook/generated/named-theorem-index.tex:1`,
  `handbook/parts/p14/master-tables.tex:250-260`, and the missing-identity
  evidence in `handbook/generated/audit-p06.tex:27-43,61-69`.
- **Evidence:** the generator describes a “complete live theorem/lemma index,”
  and the generated header claims coverage of every restored theorem/lemma.
  But the collector silently `continue`s whenever a restored `theorem` or
  `lemma` environment has no `\label`. Part VI's exact Ordered-pair identity,
  Set recursion, hierarchy theorem, Mostowski collapse, Hartogs, equivalent AC
  forms, constructible-class theorem, generic-filter lemma, and semantic-
  forcing monotonicity are among the resulting inaccessible names. The master
  prose still says “all 335 live theorem and lemma labels,” while the current
  generated file contains 369 data rows (370 physical lines including its
  header).
- **Failure path:** a reader who uses the advertised named-theorem index to find
  Hartogs or Mostowski collapse gets no row, despite both being live named
  results in Part VI. The fixed numeric completion claim also visibly
  disagrees with the current generated artifact.
- **Exact correction:** create governed, non-byte-altering destinations for all
  live exact Part VI theorem/lemma environments and teach the generator to emit
  them; fail generation on any live named result without a destination rather
  than silently skipping it. Replace the hard-coded `335` prose with a
  generator-owned count or count-free claim, and regenerate the index.
- **Status:** **open, source/content**.

### F8 — major — A-164's forcing-symbol row contradicts the live exact notation and F3's proof boundary

- **Location:**
  `handbook/restoration/inherited-10900-10988.tex:50-88`,
  `handbook/restoration/inherited-11012-11052.tex:26-40`, and
  `handbook/generated/symbols-tables.tex:402-411`, especially line 407.
- **Evidence:** the exact source defines
  (p\Vdash^{\mathrm{sem}}_{M,\mathbb P}\varphi), explicitly distinguishes it
  from the cited recursive assertion, and says no local recursive relation was
  defined. The generated Part VI registry instead displays only
  (p\Vdash_{M,\mathbb P}\varphi) and says its ruling “absorbs” the source's
  semantic qualifier, even though the live exact bytes still print that
  qualifier and later supplemental bytes use bare `\Vdash`.
- **Failure path:** the symbol lookup tells the reader that two intentionally
  distinguished relations were normalized into one glyph, while the actual
  theorem route relies on the distinction. It therefore cannot repair the
  undefined bare relation in F3 and instead publishes a false source-normality
  claim.
- **Exact correction:** register the exact semantic form and the later bare
  recursive/imported form as two scoped entries (or first perform the explicit
  alias correction required by F3), with standing, scope, and the forcing-
  theorem equivalence stated accurately. Regenerate both the full registry and
  compact symbol index.
- **Status:** **open, source/content**.

### F9 — blocker — required figure A-134 is expressly absent

- **Location:** `handbook/parts/p06/large-cardinals-absoluteness.tex:4-6` and
  `handbook/parts/p06/large-cardinals-absoluteness.tex:391-442`.
- **Evidence:** the live owner comment says A-134 is a Phase-6 artifact and “is
  not built here,” and the closing disposition confirms that no A-134 content
  is present. The chapter contains the distinct required table A-065 at lines
  391-422; a table does not silently satisfy the separately registered must
  figure “consistency-strength ladder.”
- **Failure path:** the Part VI apparatus set is incomplete. A reader receives
  a dense longtable but not the registered visual relationship among the
  consistency-strength rungs, while the source comment expressly defers that
  must commitment beyond this admission board.
- **Exact correction:** add and label the A-134 consistency-strength figure at
  the large-cardinal calibration, with conditional existence, implication
  direction, and the no-strict-separation/no-exhaustiveness boundary in its
  caption. Keep A-065 as the detailed table; do not relabel one artifact as
  both commitments. Its float placement and legibility remain build/visual
  gates after the source exists.
- **Status:** **open, source/content**.

### F10 — moderate — the Gale–Stewart theorem omits its set-theory base at the theorem site

- **Location:** `handbook/parts/p06/determinacy.tex:12-16,38-48`.
- **Evidence:** the chapter introduction generically says it distinguishes ZFC
  theorems from additional assertions. The Borel-determinacy theorem explicitly
  says “in (\mathsf{ZFC}),” but `thm:p06-gale-stewart` merely says that open or
  closed payoff sets are determined, with no base theory in the theorem.
- **Failure path:** Part VI is specifically responsible for choice/background
  calibration. At the first determinacy theorem, the reader cannot tell whether
  the result is claimed over ZF, ZFC, DC, or the chapter's ambient metatheory;
  the next theorem's explicit ZFC phrase makes the omission salient rather than
  supplying it.
- **Exact correction:** state the exact base theory in
  `thm:p06-gale-stewart` itself and ensure that the cited formulation supports
  that strength. If the intended statement is the standard ZF theorem, say
  “(\mathsf{ZF}) proves …”; otherwise name the genuinely consumed principle.
- **Status:** **open, source/content**.

## Checked-clean coverage

### Lot 1 — axioms, hierarchy/rank, ordinals, cardinals, Hartogs, and Choice

- **Checked:** all seven exact wrappers through source line 10674; ZF/ZFC axiom
  formulas and schema side conditions; object-language versus metatheoretic
  Choice; omega, ordered pairs, set/transfinite recursion, ordinal trichotomy,
  hierarchy/rank, Mostowski collapse, equipotence, Hartogs, aleph/CH/GCH;
  ordinal arithmetic/CNF/rank figures; system/Choice tables; weaker-Choice
  dependencies; binary-tree and fan results; all three Choice annex items.
- **Clean apart from F1, F2, F4, F5, F6, and F7:** the A-058 table body, A-059,
  A-060, A-062, A-063, A-129, A-130, and A-133 are present; the binary-tree and
  fan body statuses reciprocate `annex:p6.choice.2/.3`; the broader AC theorem
  honestly says `sketched=annex:p6.choice.1`; historical overlapping body and
  annex files are not on the live route.

### Lot 2 — constructibility, forcing, CH and non-CH, vocabulary, and variants

- **Checked:** all sixteen exact wrappers from 10675 through 11353; (L),
  relativization, CTM strength, generic-filter construction, names/evaluation,
  semantic forcing, cited forcing theorem and its internal boundary, Cohen
  forcing, CH and non-CH relative consistency/nonderivability; forcing
  vocabulary; condensation, ccc preservation, nice names, continuum forcing;
  Boolean-valued, collapse, permutation/symmetric-model, and independence
  catalogs; all three forcing annex items.
- **Clean apart from F3-F8:** A-066, A-067, A-131, and A-132 are present; the
  ccc, nice-name, and many-Cohen body statuses point to reciprocal
  `annex:p6.force.9/.10/.11`; the Fraenkel theorem explicitly stops at ZFA and
  cites the transfer to pure ZF; the CH catalog keeps positive/negative
  relative consistency separate from truth and absolute consistency.

### Lot 3 — combinatorics, cardinal arithmetic, large cardinals, reflection, and absoluteness

- **Checked:** clubs/stationarity/diagonal intersection/Fodor; Delta-system and
  Cohen-ccc proofs; partition notation, Ramsey and Erdos–Rado; trees, Suslin,
  diamond, square, and Martin's axiom; cardinal arithmetic, cofinality, Konig,
  Hausdorff, Easton, and Silver/PCF boundary; Levy hierarchy, reflection,
  Shoenfield, constructibility interface, and the inaccessible-to-supercompact
  ladder.
- **Clean apart from F5-F9:** A-061, A-064, and A-065 are present; the Delta
  and Cohen-ccc body labels reciprocate the two combinatorics annex proofs;
  regularity/uncountability and Choice hypotheses are generally explicit;
  Easton is stated as a relative forcing result and stops at regular cardinals;
  Silver stops before PCF; Martin's-axiom iteration is an honest proof boundary;
  every large-cardinal row is conditional and does not claim ZFC existence or
  strict adjacent consistency separation. A-134 alone is absent.

### Lot 4 — descriptive set theory, determinacy, and publication apparatus

- **Checked:** Polish/Baire spaces; Borel, analytic/coanalytic, and projective
  definitions; Suslin theorem; regularity and the coanalytic perfect-set
  boundary; A-068 and A-135; Gale–Stewart/Borel determinacy, AD/PD, AD versus
  Choice, Woodin/Martin–Steel calibration; further reading; named-theorem and
  symbol retrieval surfaces.
- **Clean apart from F5-F10:** A-068, A-135, and A-186 are present; the
  Borel/projective table isolates ZFC regularity from game/large-cardinal
  hypotheses; the determinacy chapter separates Borel determinacy, PD, and AD;
  Martin–Steel is presented as a sufficient conditional hypothesis, not an
  equivalence or existence theorem. All citation keys used by the live graph
  exist lexically. A-113 is unrouted, A-134 is absent, and A-159/A-164 have the
  concrete defects above.

## Explicit non-build / non-visual boundary

I did **not** compile the book, resolve TeX counters, inspect a PDF, or validate
actual hyperlink, citation, index, float, page-break, or landscape behavior.
Source-level labels and bibliography keys are present, but that is not render
acceptance. In particular, the wide set-theory-system, forcing-catalog,
independence, Borel/projective, and large-cardinal longtables; the
epsilon-zero, hierarchy, forcing-extension, Choice, and Borel/projective
figures; blank-verso/page-style controls; named/symbol index pagination; and
the still-missing A-134 figure all require the later full build and visual
inspection after F1-F10 are repaired. Human mathematical review and final user
acceptance also remain external gates.
