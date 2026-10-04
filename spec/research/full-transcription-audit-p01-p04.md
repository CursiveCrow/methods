# Full-transcription audit: front matter and Parts 1--4

**Snapshot audited:** 2026-08-12. The source controller is
`source/formal-logic-reference.tex`. The live destinations are the assembled
P1--P4 body, calculus-registry, and proof-annex files present in the worktree at
that snapshot. This note changes no handbook content.

## Controlling rule, scope, and verdict vocabulary

The controlling mandate requires a full and accurate compendium. Compression,
selection, normalization into house syntax, proof shortening, exercise
retirement, pointer substitution, and fusion of source text with later material
do not count as transcription. A handbook wrapper, page break, label, or index
entry may change; mathematical and explanatory content may not.

This ledger covers every printed-source line in the following disjoint spans:

- front matter and source Part I: lines 170--1648;
- source Parts II and III, now live Part 2: lines 1649--6048;
- source Part IV, now live Part 3: lines 6049--7493;
- source Part V, now live Part 4: lines 7494--9079; and
- source Part IX, rehomed into live Part 2: lines 12249--12969.

The TeX implementation preamble at lines 1--169 is not printed prose, but the
content-bearing metadata, environment standings, and notation declarations in
that span are separately inventoried below because they control the exact
meaning and visible syntax of the printed source.

The classifications are the contract's classifications:

- **full-and-accurate** -- the complete source unit is present, in order,
  without content or syntax change;
- **layout-only relocation** -- only wrapper, label, page placement, or
  typography changes and the complete source surface remains;
- **altered** -- wording, notation, hypotheses, conclusion, status, title, or
  attribution changes;
- **abridged** -- some of the source unit is summarized, compressed, or
  represented only by a shorter statement, proof, table, checklist, or pointer;
- **omitted** -- no live transcription of the source unit exists;
- **hybridized** -- inherited source and later/editorial material are fused in
  one presentation; and
- **unsupported addition** -- live material has no fixed source edition and
  page/section/text controller from which a full transcription can be checked.
  This is a provenance verdict, not a verdict on mathematical truth.

**Overall verdict:** no substantive P1--P4 inherited section is
full-and-accurate as a complete unit. Two short result bodies survive as raw
exact strings, identified below, but their surrounding result/proof units do
not. Every other inherited span is altered, abridged, omitted, or hybridized.
The old P1--P4 PASS notes are affirmative evidence of noncompliance: they
record a 3.7:1 P1 compression, 40--60% proof/sketch targets throughout P2--P4,
and deliberate exercise retirement.

## Exhaustiveness check

The covered spans contain the following named source units. Connective prose,
unnamed displays, headings, rule surfaces, status sentences, and citations are
also covered because the restoration rows partition every line, rather than
only the named environments.

| Source span | Named-unit counts |
|---|---|
| 170--1648 | 1 part; 6 chapters (including two unnumbered); 28 sections (including five unnumbered); 6 subsections; 44 definitions; 7 theorems; 4 lemmas; 3 corollaries; 10 proofs; 5 examples; 9 exercises; 5 warnings; 5 methods |
| 1649--6048 | 2 parts; 9 chapters; 35 sections; 48 definitions; 29 theorems; 29 lemmas; 4 corollaries; 60 proofs; 19 examples; 31 exercises; 3 warnings; 1 remark |
| 6049--7493 | 1 part; 3 chapters; 12 sections; 21 definitions; 14 theorems; 7 lemmas; 3 corollaries; 17 proofs; 1 proof plan; 10 examples; 11 exercises; 5 warnings; 2 methods; 3 remarks; 1 convention |
| 7494--9079 | 1 part; 3 chapters; 11 sections; 18 definitions; 18 theorems; 8 lemmas; 2 corollaries; 14 proofs; 8 proof plans; 4 examples; 5 exercises; 5 warnings; 2 remarks |
| 12249--12969 | 1 part; 2 chapters; 8 sections; 9 definitions; 6 theorems; 3 proofs; 3 examples; 6 exercises; 2 warnings |

The tables below are continuous partitions. Every named unit in a row inherits
that row's verdict unless the row expressly identifies a narrower exception.
Every restoration instruction means: restore the complete frozen span in its
original order, including prose, displays, titles, labels needed by the text,
citations, status sentences, proofs, examples, exercises, warnings, methods,
and remarks. Later material may occur only as a separately headed and separately
attributed addition.

## Content-bearing preamble inventory

| Frozen source | Controlling function | Live evidence | Class | Exact obligation |
|---|---|---|---|---|
| 1--38, 49--55, 158--169 | document class, packages, page geometry, color, running heads, and listing style | `handbook/main.tex:5--8`; `handbook/handbook.sty:37--58` | layout-only relocation | These are implementation/layout data. Preserve only when needed to render the frozen content; they do not license content changes. |
| 39--47 | PDF title, subject, and keywords | `handbook/main.tex:10--12`; `handbook/frontmatter.tex:5--16` | altered | Preserve the source metadata as edition provenance. The live title, campaign author, moving date, and phase wording are not its transcript. |
| 56--70 | exact standing and common numbering of definition, example, exercise, method, convention, theorem, lemma, corollary, remark, and warning environments | `handbook/handbook.sty:6--18,23--35,239--260` | altered, hybridized | Preserve each source environment's standing and title locally. Handbook status/index wrappers may surround but may not replace or rename the source unit. Exercises must remain exercises. |
| 72--89 | title-index wrappers; `solution`; `proofplan` explicitly displayed as “Proof sketch.” | `handbook/handbook.sty:23--35,98--212`; proof annex files | altered, hybridized | Preserve source titles and every source `proofplan` in place and in full. An annex summary or `\sketchnote` cannot substitute for it. |
| 90--96 | source delimiter macros | `handbook/handbook.sty:81--82` and dispersed live notation | altered, abridged | Preserve the source delimiter expansion wherever source text uses it; do not silently replace it by a house delimiter. |
| 97--151 | the complete source notation declaration from `\N` through `\coNP` | `handbook/handbook.sty:60--82`; `handbook/registry/symbols.csv` | altered, abridged, hybridized | Preserve every source macro's local expansion and role. A global registry may index the notation but may not normalize source syntax or suppress declarations. |
| 152--156 | exact rule, side-condition, tuple, and definition-sign macros | `handbook/handbook.sty:64--82`; calculus registry | altered, hybridized | Restore the source expansions. Decisively, source `\defeq` is `\mathrel{:=}` at line 155, while live `\defeq` is `\mathrel{:\equiv}` at `handbook/handbook.sty:67`; this is a syntax change, not layout. |

## Front matter and P1 inherited-source ledger

| Frozen source | Complete source surface | Current live destination and evidence | Class | Exact restoration |
|---|---|---|---|---|
| 170--197 | document opening; complete title page; edition/date; three-sentence source commitment; front-matter transition | `handbook/frontmatter.tex:5--26`; `handbook/main.tex:10--18` | altered, hybridized | Restore 170--197 in full. The live “Fourteen Parts with a Proof Annex,” Version 2.0, moving date, and rewritten commitment are additions, not a transcript. |
| 198--234 | `Preface`, its full dependency-order account, four purposes, citations, and scope boundary | `handbook/frontmatter.tex:28--63` | abridged, altered, hybridized | Restore 198--234 in full. The live text explicitly changes linear teaching into lookup organization. |
| 235--293 | complete terminology and notation policy, five naming conditions, `iff`, and every permanent distinction | `handbook/frontmatter.tex:130--197` | abridged, altered, hybridized | Restore 235--293 in full and in order. The handbook's naming/status policy may follow separately. |
| 294--320 | seven-level evidence hierarchy and the three exact result-status definitions | `handbook/frontmatter.tex:77--100,198--224`; `handbook/handbook.sty:98--212` | altered, hybridized | Restore 294--320 in full. The compile grammar may annotate it but cannot replace the source wording or distinctions. |
| 321--362 | `Graduate-Level Scope`, prerequisites, all twelve learning outcomes, contents transition | `handbook/frontmatter.tex:38--63,65--129`; `handbook/main.tex:18--20` | abridged, altered, hybridized | Restore 321--362 in full. `spec/verification/phase4-p01.md:33` expressly retires the linear-completion scope; that retirement is forbidden. |
| 363--372 | Part I and `Sets, Relations, Functions, and Cardinality` chapter opening | `handbook/parts/p01.tex:2--6`; `handbook/parts/p01/mathematical-preliminaries.tex:2--5` | altered, hybridized | Restore 363--372 in full before P1 additions. “Foundations of Formal Work” cannot be replaced by “Notation, Symbols, and Conventions.” |
| 373--405 | sets, subclasses, power sets, classes, and the set-builder warning | `handbook/parts/p01/mathematical-preliminaries.tex:6--18,54--56` | abridged, altered | Restore 373--405 in full, including explanatory prose and warning. |
| 406--443 | ordered pairs, identity lemma and complete proof, products | body `:19--24,61--67`; `handbook/annex/p01.tex:6--18` | abridged, altered | Restore 406--443 in full; the annex proof is a rewrite and cannot replace source proof 424--432. |
| 444--506 | relations, relation properties, functions, partial functions, injections/surjections/bijections, image and inverse image | `handbook/parts/p01/mathematical-preliminaries.tex:25--45` | abridged, altered | Restore 444--506 in full. |
| 507--532 | equivalence relations, classes, quotients, and the full quotient-definition method | body `:46--60` | abridged, altered | Restore 507--532 in full; a short method card is not the source unit. |
| 533--602 | finiteness/countability/cardinal comparison; Cantor--Schröder--Bernstein and Cantor with complete proofs | body `:68--108`; annex `:20--59` | abridged, altered | Restore 533--602 in full, replacing both shortened annex proofs with source proofs 561--583 and 588--602. |
| 603--647 | transitive sets, ordinals/cardinals, transfinite recursion and its exact evidence/citation prose | body `:68--116` | abridged, altered | Restore 603--647 in full. |
| 648--744 | Choice, well-ordering, cardinal assignment, finite coding, syntax counting, and complete syntax-counting proof | body `:117--171`; annex `:61--78` | abridged, altered, hybridized | Restore 648--744 in full. The later Ultrafilter entry must be separately attributed. |
| 745--772 | Ultrafilter Lemma definition and dependency/evidence discussion | body `:123--135` | altered, hybridized | Restore 745--772 in full; retain later evidence as a separate addition rather than replacing the source definition. |
| 773--789 | three source exercises | absent as exercises; `spec/verification/phase4-p01.md:43` | omitted | Insert 773--789 verbatim. |
| 790--797 | complete dependency summary | no source-shaped unit; P1 fragments disperse it | omitted, abridged | Restore 790--797 verbatim. |
| 798--852 | `Levels, Objects, and Consequence`; formal language, calculus, semantics, logical-system definitions; examples and standing prose | `handbook/parts/p01/formal-work-conventions.tex:4--75` | abridged, altered, hybridized | Restore 798--852 in full. |
| 853--906 | object language, metalanguage, use/mention example, and warning | body `:13--75` | abridged, altered | Restore 853--906 in full. |
| 907--984 | syntax, proof theory, semantic consequence, derivability, validity, theoremhood, soundness, completeness, and direction warning | body `:13--141` | abridged, altered, hybridized | Restore 907--984 in full and in source order. |
| 985--1023 | satisfaction, truth in a structure, model, and their exact qualifications | body `:76--141` | abridged, altered | Restore 985--1023 in full. |
| 1024--1084 | argument/countermodel definitions, complete formalization method, quantifier-order example | body `:76--157` | abridged, altered | Restore 1024--1084 in full. |
| 1085--1100 | two source exercises | absent as exercises; `spec/verification/phase4-p01.md:43` | omitted | Insert 1085--1100 verbatim. |
| 1101--1147 | finite-string chapter opening, finite sequence/string definitions, numerical pairing construction and proof | `handbook/parts/p01/mathematical-preliminaries.tex:172--209` | abridged, altered | Restore 1101--1147 in full. |
| 1148--1163 | countability-of-finite-strings lemma and complete proof | body `:210--212`; annex `:80--105` | abridged and altered | Source line 1149 is the only exact raw P1 result body found, but an exact statement fragment does not make the complete unit a layout-only relocation. Restore the entire lemma and proof 1148--1163; the live annex proof is not exact. |
| 1164--1223 | countability corollary/proof, concatenation lemma/proof, and remaining string prose | body `:213--218`; annex `:107--132` | abridged, altered | Restore 1164--1223 in full. |
| 1224--1263 | inductive generation, structural induction theorem/proof, and active-grammar warning | body `:219--224,239--241`; annex `:134--142` | abridged, altered | Restore 1224--1263 in full. |
| 1264--1308 | structural recursion theorem and complete proof | body `:225--233`; annex `:144--159` | abridged, altered | Restore 1264--1308 in full. |
| 1309--1319 | formula-complexity example | absent from P1; `spec/verification/phase4-p01.md:42` says deliberately retired/rehomed | omitted | Restore 1309--1319 verbatim at its source location. A later P2 complexity entry may coexist but cannot substitute. |
| 1320--1342 | induction-on-derivations section and complete method | body `:234--241` | abridged, altered | Restore 1320--1342 in full. |
| 1343--1397 | reflexive-transitive closure, path lemma/proof, equivalence closure | body `:242--246`; annex `:161--175` | abridged, altered | Restore 1343--1397 in full. |
| 1398--1410 | two closure exercises | absent as exercises | omitted | Insert 1398--1410 verbatim. |
| 1411--1504 | full formal-writing chapter opening; dependency order; definition audit, example, circularity warning; theorem-statement and proof-plan guidance | `handbook/parts/p01/formal-work-conventions.tex:158--226` | abridged, altered, hybridized | Restore 1411--1504 in full. |
| 1505--1553 | all six proof-method subsections: direct, contrapositive, contradiction, induction, construction, counterexample | body `:158--226` | abridged, altered | Restore 1505--1553 in full and retain each source subsection. |
| 1554--1579 | displayed formulas and prose | body `:227--244` | abridged, altered | Restore 1554--1579 in full. |
| 1580--1591 | exact illustrative inference-rule typography | replaced by registry-reference policy at body `:227--244`; `spec/verification/phase4-p01.md:41` says deliberately retired | omitted, altered | Restore 1580--1591 verbatim. Registry copies may follow; they cannot replace the source display. |
| 1592--1631 | complete nine-class error taxonomy and explanations | body `:245--284` | abridged, altered, hybridized | Restore 1592--1631 in full, not only the summary table. |
| 1632--1648 | two source exercises | absent as exercises | omitted | Insert 1632--1648 verbatim. |

### P1 decisive departures

1. `spec/verification/phase4-p01.md:19--20` records approximately 3.7:1
   compression; lines 32--43 record compressed front matter, retired scope,
   compressed levels/writing chapters, retired rule display, retired formula
   example, and unreproduced exercises.
2. `handbook/parts/p01/mathematical-preliminaries.tex:1` calls itself a
   “lookup compression”; `handbook/parts/p01/formal-work-conventions.tex:1--3`
   calls itself a compressed core.
3. Source syntax is not controlling: `\defeq` changes meaning at
   `handbook/handbook.sty:67`.
4. The full source proofs are rewritten into annex cards; preservation of a
   result's evidence class is not preservation of its proof text.

## P2 inherited source Part II: classical propositional logic

| Frozen source | Complete source surface | Current live destination and evidence | Class | Exact restoration |
|---|---|---|---|---|
| 1649--1660 | source Part II and chapter openings | `handbook/parts/p02.tex:2--7`; `handbook/parts/p02/propositional-syntax-semantics.tex:9--16` | altered, hybridized | Restore 1649--1660 in full. Live “Classical Logic” collapses three distinct source parts. |
| 1661--1816 | alphabet, grammar, defined connectives, parenthesis lemma/proof, unique readability/proof, complexity/subformula | body `:17--137`; annex `handbook/annex/p02/propositional-syntax-semantics.tex:3--26` | abridged, altered, hybridized | Restore 1661--1816 in full, including both complete proofs. |
| 1817--1898 | valuations, recursive clauses, coincidence lemma/proof, semantic notions, truth-table example | body `:138--272`; annex `:28--33` | abridged, altered, hybridized | Restore 1817--1898 in full. |
| 1899--1945 | controlled-prose translation and both worked examples | body `:273--312` | abridged, altered | Restore 1899--1945 in full. |
| 1946--2186 | literal/clause interpretation; NNF/CNF/DNF; clause, normal-form, and functional-basis results with all complete proofs | body `:313--628`; annex `:35--112` | abridged, altered, hybridized | Restore 1946--2186 in full. The annex proofs were deliberately reduced to 40--60% (`spec/verification/phase4-p02a.md:43--68,178--179`). |
| 2187--2192 | deduction chapter opening and classical-ND introduction | `handbook/parts/p02/propositional-calculi.tex:5--19` | altered, hybridized | Restore 2187--2192 in full. |
| 2193--2340 | exact natural-deduction derivation, all source rules, derivability, two derivation examples, substitution lemma/proof | body `:20--92`; calculus sheet `handbook/registry/calculi/nd-cpl.tex`; annex `handbook/annex/p02/propositional-calculi.tex:4--16` | altered, abridged, hybridized | Restore 2193--2340 verbatim as a source calculus and proof block. A normalized registry sheet cannot substitute for source syntax. |
| 2341--2450 | sequent definition, full rule surface, and worked derivation | body `:93--139`; `handbook/registry/calculi/lk.tex` | altered, abridged, hybridized | Restore 2341--2450 in full before separately identified registry variants. |
| 2451--2544 | metatheory chapter opening; ND and LK soundness theorems with complete proofs | `handbook/parts/p02/propositional-metatheory.tex:3--36`; annex `:3--41` | abridged, altered | Restore 2451--2544 in full. |
| 2545--2664 | consistency/maximal consistency; closure, Lindenbaum, and truth lemmas with complete proofs | body `:37--97`; annex `:43--85` | abridged, altered | Restore 2545--2664 in full. |
| 2665--2809 | strong completeness, compactness, and LK completeness, including complete proofs and source sketch | body `:98--159`; annex `:87--135` | abridged, altered, hybridized | Restore 2665--2809 in full. The source sketch's full omitted-case account must remain, not a shorter `\sketchnote`. |
| 2810--2914 | resolution definition, soundness/proof, completeness/proof, attribution/scope remark | body `:197--276`; registry sheet `resolution-cpl.tex`; annex `:158--191` | abridged, altered, hybridized | Restore 2810--2914 in full. |
| 2915--2932 | complete common-errors section and warning | body `:404--420` | abridged, altered | Restore 2915--2932 in full. |
| 2933--3021 | twelve propositional exercises | absent as exercises; `spec/verification/phase4-p02a.md:95--101` | omitted | Insert 2933--3021 verbatim. |

## P2 inherited source Part III: classical first-order logic

| Frozen source | Complete source surface | Current live destination and evidence | Class | Exact restoration |
|---|---|---|---|---|
| 3022--3037 | source Part III and first-order syntax chapter openings | `handbook/parts/p02.tex:2--7`; `handbook/parts/p02/first-order-syntax-semantics.tex:7--15` | altered, hybridized | Restore 3022--3037 in full. |
| 3038--3104 | signatures, terms, and term example | body `:16--91` | abridged, altered, hybridized | Restore 3038--3104 in full. |
| 3105--3165 | formulas, unique readability theorem, complete proof | body `:16--91`; annex `handbook/annex/p02/first-order-syntax-semantics.tex:5--16` | abridged, altered | Restore 3105--3165 in full. |
| 3166--3239 | occurring/free variables and formula complexity | body `:92--256` | abridged, altered | Restore 3166--3239 in full. |
| 3240--3428 | term/formula substitution, strong recursive renaming, alpha-equivalence, capture example, three lemmas and complete proofs | body `:92--256`; annex `:18--58` | abridged, altered, hybridized | Restore 3240--3428 in full. |
| 3429--3518 | structures/expansions/reducts, assignments, term values, term coincidence and substitution proofs | body `:257--400`; annex `:60--72` | abridged, altered | Restore 3429--3518 in full. |
| 3519--3680 | recursive satisfaction; formula coincidence, substitution, alpha-invariance, sentence independence with complete proofs; truth/validity/consequence | body `:257--400`; annex `:74--116` | abridged, altered | Restore 3519--3680 in full. |
| 3681--3728 | quantifier translation and both examples | body `:401--439` | abridged, altered | Restore 3681--3728 in full. |
| 3729--3907 | theories, axiomatization, all four examples, definitional-extension theorem and complete proof | body `:440--547`; annex `:118--148` | abridged, altered, hybridized | Restore 3729--3907 in full. |
| 3908--3926 | axiomatization errors warning and source prose | body `:440--547` | abridged, altered | Restore 3908--3926 in full. |
| 3927--4061 | deduction chapter; complete quantifier/equality ND rule surfaces; derivability; reduct lemma/proof; three examples | `handbook/parts/p02/first-order-calculi.tex:5--81`; `handbook/registry/calculi/nd-fol.tex`; annex `handbook/annex/p02/first-order-calculi.tex:3--10` | altered, abridged, hybridized | Restore 3927--4061 verbatim, including source rule syntax and examples. |
| 4062--4108 | complete first-order sequent-rule surface | body `:18--81`; registry `lk-eq.tex` | altered, abridged, hybridized | Restore 4062--4108 verbatim as the source calculus. |
| 4109--4213 | ND and LK soundness theorems with complete proofs | body `:18--81`; annex `:12--58` | abridged, altered | Restore 4109--4213 in full. |
| 4214--4234 | quantifier-rule error warning and complete explanation | body `:276--294` | abridged, altered | Restore 4214--4234 in full. |
| 4235--4305 | nine first-order deduction exercises | absent as exercises; `spec/verification/phase4-p02b.md:144--145` | omitted | Insert 4235--4305 verbatim. |
| 4306--4575 | Henkin chapter and syntactic preparation: consistency, closure, duality, fresh constants, witness property/extension, constant elimination, transfinite Lindenbaum, Henkin--Lindenbaum, with all proofs | `handbook/parts/p02/first-order-completeness.tex:5--116`; annex `handbook/annex/p02/first-order-completeness.tex:6--122` | abridged, altered, hybridized | Restore 4306--4575 in full. |
| 4576--4712 | term structure, equality congruence, term evaluation, quantifier membership, truth lemma, all complete proofs | body `:117--192`; annex `:124--168` | abridged, altered | Restore 4576--4712 in full. |
| 4713--4920 | strong completeness, countable choice-free corollary, LK completeness sketch, with the full source proofs/sketch | body `:193--247`; annex `:170--235` | abridged, altered, hybridized | Restore 4713--4920 in full. |
| 4921--4967 | first-order compactness and corollary with complete proofs | body `:193--247`; annex `:237--255` | abridged, altered | Restore 4921--4967 in full. |
| 4968--5042 | cardinality chapter opening; substructure/elementarity; Tarski--Vaught theorem and proof | body `:248--290`; annex `:257--272` | abridged, altered, hybridized | Restore 4968--5042 in full. |
| 5043--5131 | downward and upward Löwenheim--Skolem theorems and complete proofs | body `:291--370`; annex `:274--301` | abridged, altered, hybridized | Restore 5043--5131 in full. |
| 5132--5567 | literal/NNF/prenex/rectification/Skolemization pipeline, all definitions/examples, five results and complete proofs | `handbook/parts/p02/first-order-normal-forms.tex:4--357`; annex `handbook/annex/p02/first-order-normal-forms.tex:4--148` | abridged, altered, hybridized | Restore 5132--5567 in full. Old verification records proof bodies at 43.4--56.8% (`spec/verification/phase4-p02b.md:53--57`). |
| 5568--5923 | first-order clauses/substitutions, renaming, unification, resolution/factoring, Herbrand and lifting results, worked example, soundness proof and both full source sketches | `handbook/parts/p02/first-order-resolution.tex:4--253`; registry `resolution-fol.tex`; annex `handbook/annex/p02/first-order-resolution.tex:3--49` | abridged, altered, hybridized | Restore 5568--5923 in full. |
| 5924--5959 | full common-errors section | body fragments disperse it | abridged, altered | Restore 5924--5959 in full and contiguous. |
| 5960--6048 | ten first-order exercises | absent as exercises; `spec/verification/phase4-p02b.md:144--145` | omitted | Insert 5960--6048 verbatim. |

## P2 inherited source Part IX: second- and higher-order logic

| Frozen source | Complete source surface | Current live destination and evidence | Class | Exact restoration |
|---|---|---|---|---|
| 12249--12261 | source part and second-order chapter openings | `handbook/parts/p02.tex:2--7`; `handbook/parts/p02/second-and-higher-order-logic.tex:8--18` | altered, hybridized | Restore 12249--12261 in full. Rehoming may change a locator, not the source title or introduction. |
| 12262--12289 | second-order signatures, formulas, and sentences | body `:19--48` | abridged, altered, hybridized | Restore 12262--12289 in full. |
| 12290--12355 | full assignments/consequence/comprehension theorem and complete proof | body `:49--457`; annex `handbook/annex/p02/higher-order.tex:7--17` | abridged, altered, hybridized | Restore 12290--12355 in full. |
| 12356--12414 | full second-order arithmetic and categoricity theorem with complete proof | body `:49--457`; annex `:19--33` | abridged, altered, hybridized | Restore 12356--12414 in full. |
| 12415--12536 | noncompactness theorem/proof; no-effective-calculus theorem and source proof reasoning; full-real categoricity; Lindström theorem and qualifications | body `:49--457`; annex `:35--60`; P3 pointer/addition | abridged, altered, hybridized | Restore 12415--12536 in full and in source order. Relocation of Lindström may add a cross-reference but cannot remove this source unit. |
| 12537--12673 | Henkin structures/consequence, comprehension/choice standing, incidence translation/calculus, and all source explanatory material | body `:458--496` and earlier inserted calculus material; registry `sol.tex`; annex `:112--182` | abridged, altered, hybridized | Restore 12537--12673 in full. A translation-defined new sheet is a separately attributed addition, not the source presentation. |
| 12674--12720 | reachability example, semantic-parameter warning, and three exercises | example/warning dispersed in body; exercises explicitly retired at file `:5--6` and `spec/verification/phase4-p02c.md:85--86` | abridged, altered, omitted | Restore 12674--12720 in full, including all three exercises. |
| 12721--12783 | simple-type chapter opening; types, terms, formulas, binders, application, equality standing | body `:497--656`; registry `system-f.tex` is later material | abridged, altered, hybridized | Restore 12721--12783 in full. |
| 12784--12923 | standard/Henkin type structures, semantics, extensionality, substitution/beta result and source sketch, completeness/categoricity qualifications, two examples | body `:497--656`; annex `:184--199` | abridged, altered, hybridized | Restore 12784--12923 in full. The migrated sketch is only 58.1% of source (`spec/verification/phase4-p02c.md:39--49`). |
| 12924--12950 | type-discipline/foundational-scope section and proof-assistant warning | body `:621--656` | abridged, altered, hybridized | Restore 12924--12950 in full. |
| 12951--12969 | three higher-order exercises | absent as exercises; body header `:5--6` | omitted | Insert 12951--12969 verbatim. |

### P2 decisive departures

1. Every migrated P2 proof/sketch was deliberately targeted to 40--60% of its
   source word count: `spec/verification/phase4-p02a.md:43--68`,
   `phase4-p02b.md:38--67`, and `phase4-p02c.md:37--49`.
2. Every P2 source exercise layer was deliberately retired:
   `phase4-p02a.md:95--101`, `phase4-p02b.md:144--145`, and
   `phase4-p02c.md:82--86`.
3. Exact source calculus surfaces were replaced by separately authored registry
   sheets. Rule centralization is layout only if the source syntax remains;
   these sheets normalize, annotate, and combine systems and therefore are not
   transcriptions.
4. Source Parts II, III, and IX were fused under one live part, and later depth
   material was interleaved. That organization may remain only if each source
   presentation is still complete and independently attributable.

## P3 inherited-source ledger

| Frozen source | Complete source surface | Current live destination and evidence | Class | Exact restoration |
|---|---|---|---|---|
| 6049--6069 | `Model Theory`, chapter opening, and exact status convention | `handbook/parts/p03.tex:2--11`; `handbook/parts/p03/maps-elementarity.tex:12--24` | altered and hybridized | An exact part-title fragment does not make the complete unit a layout-only relocation. Restore 6049--6069 in full. The live wrapper may retain its label; the source convention may not be replaced by handbook status grammar. |
| 6070--6137 | homomorphism, embedding, isomorphism/automorphism, term-preservation lemma/proof, warning | `handbook/parts/p03/maps-elementarity.tex:25--78`; annex `handbook/annex/p03/maps-elementarity.tex:5--11` | abridged, altered | Restore 6070--6137 in full. |
| 6138--6242 | substructures, example, isomorphism-invariance and embedding-image lemmas with complete proofs | body `:79--135`; annex `:13--36` | abridged, altered | Restore 6138--6242 in full. |
| 6243--6331 | elementary maps/substructures, remark, Tarski--Vaught theorem/proof, worked example | body `:136--183`; annex `:38--53` | abridged, altered | Restore 6243--6331 in full. |
| 6332--6421 | parameter constants, atomic/elementary diagrams, embedding tests and complete proof, comparison example | body `:184--236`; annex `:55--71` | abridged, altered, hybridized | Restore 6332--6421 in full. |
| 6422--6431 | diagram exercise | body header `:5--10` says source exercises deliberately retired | omitted | Insert 6422--6431 verbatim. |
| 6432--6493 | elementary chains, theorem and complete proof, coherent-chain warning | body `:237--261`; annex `:73--87` | abridged, altered | Restore 6432--6493 in full. |
| 6494--6509 | two elementary-chain exercises | body header `:5--10` | omitted | Insert 6494--6509 verbatim. |
| 6510--6629 | types chapter; types/type spaces, compactness theorem and proof, finite-type-space example | `handbook/parts/p03/types-ultraproducts.tex:4--107`; annex `handbook/annex/p03/types-ultraproducts.tex:6--31` | abridged, altered, hybridized | Restore 6510--6629 in full. |
| 6630--6639 | type-space exercise | body `:329--335` says five exercises deliberately retired | omitted | Insert 6630--6639 verbatim. |
| 6640--6693 | realization example, saturation definition/remark, saturated-extension cited theorem | body `:13--107` | abridged, altered | Restore 6640--6693 in full. |
| 6694--6782 | homogeneity, saturation-to-homogeneity theorem/proof, explanatory example | body `:108--132`; annex `:33--64` | abridged, altered | Restore 6694--6782 in full. |
| 6783--6791 | homogeneity exercise | body `:329--335` | omitted | Insert 6783--6791 verbatim. |
| 6792--6845 | principal/nonprincipal types, omitting-types theorem, example | body `:133--170` | abridged, altered | Restore 6792--6845 in full. |
| 6846--6854 | omitting-types exercise | body `:329--335` | omitted | Insert 6846--6854 verbatim. |
| 6855--6941 | filters, nonprincipal-ultrafilter lemma and complete proof | body `:171--206`; annex `:66--89` | abridged, altered, hybridized | Restore 6855--6941 in full. |
| 6942--7134 | ultraproduct definition; well-definedness, term, Łoś, diagonal results with every complete proof; finite-ultraproduct example; first-order warning | body `:207--328`; annex `:91--152` | abridged, altered, hybridized | Restore 6942--7134 in full. |
| 7135--7149 | two ultraproduct exercises | body `:329--335` | omitted | Insert 7135--7149 verbatim. |
| 7150--7294 | QE chapter/section; one-quantifier method; DLO theorem/remark/example; completeness/model-completeness definitions; reduction lemma/proof; corollary/proof plan; ACF theorem | `handbook/parts/p03/qe-categoricity-games.tex:18--212`; annex `handbook/annex/p03/qe-categoricity-games.tex:4--23` | abridged, altered, hybridized | Restore 7150--7294 in full. |
| 7295--7468 | categoricity, warning, partial isomorphisms, back-and-forth method/theorem/proof, saturated corollary/proof, DLO categoricity/proof, ACF example, Ryll--Nardzewski, Morley, final warning | body `:213--450`; annex `:25--53` | abridged, altered, hybridized | Restore 7295--7468 in full. |
| 7469--7493 | three QE/categoricity exercises | body header `:7--11` says absorbed or retired | omitted | Insert 7469--7493 verbatim. |

### P3 decisive departures

1. Every migrated P3 proof or sketch was reduced to 40--60% of source
   (`spec/verification/phase4-p03.md:36--46`).
2. `handbook/parts/p03/maps-elementarity.tex:4--10` and
   `types-ultraproducts.tex:329--335` explicitly say examples/warnings are
   compressed and all source exercises are retired.
3. `handbook/annex/p03/maps-elementarity.tex:1--3`,
   `types-ultraproducts.tex:1--4`, and `qe-categoricity-games.tex:1--2`
   explicitly describe proof compressions.
4. The live text replaces source `\Th` syntax with a different printed form;
   `spec/verification/phase4-p03.md:98--99` records the normalization. The
   source preamble defines `\Th`, so this is not a repair authorized by the
   full-transcription mandate.

## P4 inherited-source ledger

| Frozen source | Complete source surface | Current live destination and evidence | Class | Exact restoration |
|---|---|---|---|---|
| 7494--7505 | source `Computability` part and machines chapter openings | `handbook/parts/p04.tex:2--11`; `handbook/parts/p04/machines-effective-procedures.tex:9--17` | altered, hybridized | Restore 7494--7505 in full. “and Complexity” is a later addition and cannot alter the source title. |
| 7506--7677 | exact deterministic one-tape machine, configuration/computation, partial computability, successor example, formalism/complexity warning | body `:18--168` | abridged, altered, hybridized | Restore 7506--7677 in full. |
| 7678--7752 | primitive-recursive functions/relations, theorem and full proof plan, example, remark | body `:169--401`; annex `handbook/annex/p04/machines-effective-procedures.tex:5--11` | abridged, altered, hybridized | Restore 7678--7752 in full. |
| 7753--7843 | decidable/c.e. definitions, machine decision/recognition, two result proofs and one complete proof plan | body `:402--462`; annex `:13--34` | abridged, altered | Restore 7753--7843 in full. |
| 7844--7850 | Turing-machine exercise | body `:463--468` says retired | omitted | Insert 7844--7850 verbatim. |
| 7851--8048 | universal-computation chapter; complete effective numbering; renaming lemma/proof; enumeration theorem/proof; universal theorem/proof plan; parameter theorem | `handbook/parts/p04/universal-reductions.tex:1--130`; annex `handbook/annex/p04/universal-reductions.tex:5--56` | abridged, altered, hybridized | Restore 7851--8048 in full. |
| 8049--8080 | many-one reduction, preservation lemma/proof, direction warning | body `:131--159`; annex `:58--63` | abridged, altered | Restore 8049--8080 in full. |
| 8081--8143 | self-application problem, undecidability theorem/proof, complement corollary/proof, binary-domain worked argument | body `:160--197`; annex `:65--80,132--141` | abridged, altered, hybridized | Restore 8081--8143 in full. Source line 8115 is an exact raw body match at live `:178`, but the live corollary adds a title and its proof is shortened; the complete unit is not layout-only. |
| 8144--8186 | recursion theorem, full proof plan, self-reference example | body `:198--215`; annex `:82--97` | abridged, altered | Restore 8144--8186 in full. |
| 8187--8238 | extensional-index-property definition; Rice theorem/complete proof; scope warning | body `:216--244`; annex `:99--119` | abridged, altered | Restore 8187--8238 in full. |
| 8239--8247 | Rice exercise | body `:245--249` says retired | omitted | Insert 8239--8247 verbatim. |
| 8248--8305 | decision-problem chapter/section; negative Entscheidungsproblem; enumerability corollary/proof; restricted-signature warning; Trakhtenbrot theorem | `handbook/parts/p04/decision-problems-and-arithmetical-hierarchy.tex:16--48`; annex `handbook/annex/p04/decision-problems-and-arithmetical-hierarchy.tex:6--13` | abridged, altered, hybridized | Restore 8248--8305 in full. |
| 8306--8438 | arithmetic language/order abbreviations; syntactic and semantic arithmetical-hierarchy definitions and qualifications | body `:49--164` | abridged, altered, hybridized | Restore 8306--8438 in full. |
| 8439--8709 | pairing graph, beta function, contraction, bounded exchange, prefix normal form, and every complete proof | body `:165--263`; annex `:15--110` | abridged, altered | Restore 8439--8709 in full. |
| 8710--8876 | history coding; bounded verification and level-one theorems with full proof plans; hardness/completeness; classification and strictness theorems; warning | body `:264--424`; annex `:112--140` | abridged, altered, hybridized | Restore 8710--8876 in full. |
| 8877--8897 | three arithmetical-hierarchy exercises | body `:425--430` says deliberately retired | omitted | Insert 8877--8897 verbatim. |
| 8898--9079 | relative computation/Post section; oracle machines, jump, relativized adequacy/proof plan, jump theorem/proof plan, Post theorem, full convention-bridge remark | `handbook/parts/p04/degrees-and-priority.tex:13--151,436--441`; annex `handbook/annex/p04/degrees-and-priority.tex:5--55` | abridged, altered, hybridized | Restore 8898--9079 in full. Later degree and finite-injury material must follow separately. |

### P4 decisive departures

1. `spec/verification/phase4-p04.md:63--121` records every source complete
   proof and proof plan at 40--60% of source size, including explicit
   “compliance compression.”
2. `phase4-p04.md:124--127` records deliberate retirement of all five source
   exercises. The body comments at
   `machines-effective-procedures.tex:463--468`,
   `universal-reductions.tex:245--249`, and
   `decision-problems-and-arithmetical-hierarchy.tex:425--430` confirm it.
3. The body/annex headers themselves say “compression”:
   `handbook/annex/p04/machines-effective-procedures.tex:1--3`,
   `universal-reductions.tex:1--3`, and
   `decision-problems-and-arithmetical-hierarchy.tex:1--4`.
4. The single exact raw corollary body at source 8115 does not make the
   source proof or surrounding worked example exact; those are separately
   shortened and reclassified.

## Live additions and hybridization ledger

The following live surfaces are not inherited transcriptions of the covered
source spans. They may be retained only as separate, attributed additions.
Where existing research notes cite sources but do not fix a controlling
edition/page/section/text presentation, the surface remains **unsupported
addition** for transcription auditing.

| Live surface | Evidence | Class |
|---|---|---|
| P1 generated symbol registry, Boolean-function table, historical-notation table, and letter-family policy | `handbook/parts/p01/symbol-registry.tex:1--299` | unsupported addition; hybridized wherever used to normalize inherited syntax |
| P1 handbook status grammar, proof-annex protocol, and calculus-only rule-display policy | `handbook/frontmatter.tex:65--129`; `handbook/handbook.sty:6--35,98--212` | unsupported addition; hybridized where substituted for source evidence prose/rules |
| P2 duality/Post material, Hilbert/tableau comparison, interpolation/complexity/tractability expansions | `handbook/parts/p02/propositional-syntax-semantics.tex:418--628`; `propositional-calculi.tex:140--326`; `propositional-metatheory.tex:160--403` | unsupported addition unless individually fixed to a controller; hybridized in the inherited chapters |
| P2 first-order tableaux/Hilbert/depth/reference expansions | `handbook/parts/p02/first-order-calculi.tex:82--275`; `first-order-depth.tex:1--417` | unsupported addition unless individually fixed; hybridized |
| P2 matched relational SOL calculus and all variant-logic cards | `handbook/registry/calculi/sol.tex`; `handbook/parts/p02/variants.tex:1--447` | unsupported addition unless individually fixed; hybridized |
| P3 classification theory, finite-model theory, preservation/abstract-logic chapters, and EF additions | `handbook/parts/p03/classification-theory.tex:1--247`; `finite-model-theory.tex:1--118`; `preservation-abstract-logic.tex:1--202`; `qe-categoricity-games.tex:331--451` | unsupported addition unless individually fixed; hybridized where inserted in inherited flow |
| P4 degree/priority material beyond source 8898--9079, frontiers of computability, and complexity | `handbook/parts/p04/degrees-and-priority.tex:152--441`; `frontiers-of-computability.tex:1--506`; `complexity.tex:1--454` | unsupported addition unless individually fixed; hybridized at the part-title and chapter-flow levels |
| Generated P1--P4 audit registers | `handbook/generated/audit-p01.tex` through `audit-p04.tex` | layout/navigation addition only if they index complete source units; presently unsupported as fidelity evidence because their indexed units are abridged |

## Exact restoration ledger

No editorial decision is required. Restoration is mechanical and ordered:

1. Preserve the content-bearing source metadata and local macro meanings from
   preamble lines 39--156; source-local notation controls every inherited
   transcription.
2. Insert source lines 170--1648, in order and without rewriting, as the
   complete front matter and Part-I presentation.
3. Insert source lines 1649--6048, in order and without rewriting, as the
   complete Part-II and Part-III presentations.
4. Insert source lines 6049--7493, in order and without rewriting, as the
   complete Part-IV presentation.
5. Insert source lines 7494--9079, in order and without rewriting, as the
   complete Part-V presentation.
6. Insert source lines 12249--12969, in order and without rewriting, as the
   complete Part-IX presentation at its chosen layout location. Rehoming may
   add locators but may not fuse or rewrite the source.
7. Keep every proof immediately identifiable as the proof belonging to its
   source result. A proof annex is permissible only as layout relocation when
   the proof itself is complete and unchanged; every current 40--60% rewrite
   must be replaced.
8. Restore all 62 source exercises in these spans as exercises, all examples
   as examples, all warnings as warnings, all methods as methods, all proof
   plans in full, and all exact calculus/rule displays in source syntax.
9. Place later material after the applicable inherited unit under a separate
   heading with fixed source attribution. Distinct source presentations remain
   distinct. Do not synthesize a house version.
10. Regenerate indices and audit tables only after every source line and named
    unit has a book locator and a full-and-accurate or layout-only verdict.

## Audit conclusion

The current P1--P4 manuscript fails the full-transcription mandate. This is
not an inference from page count or style: the live files and their own prior
verification notes explicitly identify compression, proof shortening,
exercise retirement, rule replacement, source-syntax normalization, rehoming,
and interleaving with later additions. The restoration spans above cover every
printed source line from 170 through 9079 plus the entire otherwise uncovered
Part-IX span 12249--12969, with no gaps inside those ranges.
