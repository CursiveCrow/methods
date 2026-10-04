# Next manuscript writing obligations: live bounded census

Date: 2026-09-06.

## Result

**Update after this census:** the N15 canonical-code and pruning
construction has now been supplied, together with full finite-automaton
proofs and a finite-domain MSO equivalence proof. See
p09-n-c-015-writing-progress-2026-09-06.md. Item 1 below records the
gap as it stood when identified.

**Further update:** the general-TBox ALC mathematical treatment is now
supplied, including complete type elimination, a finite-model proof,
an alternating-machine hardness reduction, and the combined EXPTIME
classification for concept/TBox and finite knowledge-base reasoning.
See p09-alc-general-tbox-writing-progress-2026-09-06.md and item 4 below.
The distinct 2017 book presentation still requires its body.

Four concrete source presentations retain body-dependent gaps:
Thatcher--Wright 1968, McMillan 1993, the 2017 textbook's own
general-TBox treatment, and McNaughton 1966. The originally identified
N15 pruning and general-TBox mathematical gaps must not be inferred to
remain open from the historical locations retained below.

No newly supplied McMillan 1993 body was identified in the checked local
holdings. Its author-linked thesis remains a different source.

These are five bounded obligations, not a finding that everything else
in the manuscript is complete. A merely cited theorem is not counted
as missing authoring.

## Scope and live routing

All fourteen actual part drivers, handbook/parts/p01.tex through p14.tex,
were read. Relevant active source maps, chapter introductions, the Part IX
source-standing paragraph, and the actual source-gap passages below were
also read. A read-only traversal of literal input/include commands from
the fourteen drivers reached 651 existing files and found no missing
literal input target. Commented inputs were excluded.

This routing census is not a TeX build or an evaluation of every dynamic
macro. In particular, the generated rule-sheet mechanism is not inferred
from literal input traversal alone. No unreachable hbstub was promoted
to an authoring obligation.

The live drivers deliberately leave some historical generated audit tables
unrouted; those are apparatus/generator matters, not missing mathematical
presentations in this writing list. The new P3 Robinson/Beth material,
P6 PCF material, P7 Craig/Beth material, N14/N16 corrections, and N18
expansions were not replaced by the older statuses in acquisition or
review records. The same-day manuscript-direct-corrections note records
the user's authority to correct the active reader text; old frozen-copy
prohibitions are not a reason to defer authorized writing.

The general external-presentation requirement is
spec/FULL-COMPENDIUM-ARCHITECTURE.md:79–100: each presentation carries its
own definitions, conditions, supplied proofs, examples, and completeness
check; one source does not supply another's omitted clauses. Source notes
below are used for exact source targets, while the current reader text
establishes that the gap is still present.

## 1. N15: define and prove the ranked-tree projection operation

**Live location.** handbook/parts/p09/presentations/n-c-015.tex:177–181
defines the canonical assignment encoding: a remaining all-bottom symbol
is nullary, while a symbol containing 0 or 1 has arity \(k\). At line 213,
the existential case is still the single sentence that quantification
“projects away the quantified track.”

**Concrete authoring obligation.** Give the actual map on the ranked
encodings and the effective automaton construction for its image. Merely
deleting one coordinate from every node label need not preserve the
declared ranks. For example, with \(k=2\), \(X=\{\epsilon\}\), and
\(Y=\varnothing\), the two-track encoding has an internal
\((1,\bot)\) root with bottom leaves. After forgetting \(X\), the
canonical encoding of \(Y\) is the single nullary \(\bot\) tree.
The projection must collapse the now-all-bottom subtree.

This is a missing definition/construction for an operation already used
in the proof, not a claim that the finite-tree correspondence theorem
is false, and not a demand to reproduce the entire TATA monograph.

**Requirement pointer.** The same paragraph invokes the constructive
formula-to-automaton direction of Lemma 3.3.4. Its exact source target is
TATA printed pp. 91–93, recorded at
spec/research/p09-tata-2008-source-note.md:112–117. The presentation
contract's definition-before-use and complete operative-content
requirements apply to that named quantifier operation.

**Next feasible writing action.** Using the already present
tmp/pdfs/p09-tata-2008/tata-2008.pdf, define track deletion together with
all-bottom pruning, then give the finite automaton image construction
and prove that it recognizes exactly the canonical encodings of
existential witnesses. Include the zero-remaining-track sentence case
and preserve the distinction between canonical encodings and arbitrary
trees over the ranked alphabet. A deleting tree homomorphism/image
construction is a possible route, provided its domain, collapsing
clauses, and automaton implementation are stated.

N15 was being edited during this census: new finite-automaton material
appeared before this passage. The line numbers above are from the last
actual read; the projection sentence and encoding clauses remain the
stable text locators.

## 2. N15: supply the separate Thatcher--Wright 1968 presentation

**Live location.** handbook/parts/p09/presentations/n-c-015.tex:258–269,
especially line 263, explicitly says that the technical article body is
not part of the source basis. The host repeats its abstract-only
standing at handbook/parts/p09/logic-in-computer-science.tex:30–33.

**Concrete authoring obligation.** The article's finite-algebra objects,
recognition relation, generalized Kleene constructions, exact
second-order language, theorem hypotheses, and supplied examples/proofs
are still absent. TATA supplies a different modern presentation.

**Requirement pointer.** The explicit separate source obligation is
spec/research/p09-source-presentations-lot2-3.md:984 and
spec/research/p09-tata-2008-source-note.md:196–206, under the general
one-source/one-presentation requirement above. The older N-c-015
register row at spec/registers/new-content.csv:122 says “pointer only”;
that row alone is not being read as a requirement to write all of
finite-tree automata theory. The obligation here is the separately
identified missing source presentation.

**Next feasible writing action.** Inspect an authorized complete article
or the exact same-title RC-1713 report if supplied, establish its own
version, and reconstruct its objects and two directions under its own
attribution. The local filename search found
tmp/pdfs/p09-thatcher-1965/6511049.pdf, but no identified 1968 article or
RC-1713 body. That differently identified file is not evidence that the
registered body has arrived. Until the exact body is available, this is
a source-dependent writing obligation.

## 3. N17: reconstruct the revised McMillan 1993 book

**Live location.** handbook/parts/p09/presentations/n-c-017.tex:1627–1639.
Lines 1630–1633 identify the registered full SMV, symbolic-algorithm,
hardware/cache, induction, equivalence, and partial-order presentation,
and state that the revised body needed for its content is absent.

**Requirement pointer.** N-c-017 is a mandatory row at
spec/registers/new-content.csv:124. The exact book scope and chapter
targets are in spec/research/p09-source-presentations-lot2-3.md:875–883.
The current day's remaining-writing statement is
spec/research/p09-n-c-017-writing-progress-2026-09-06.md, under
“Remaining writing”; the same-day acquisition result is
spec/research/p09-n-c-017-mcmillan-acquisition-note.md.

**Next feasible writing action.** Use the already requested authorized
1993 book or complete publisher chapters when supplied. Verify the
internal title/version and reconstruct the book's SMV semantics,
transition partitioning, algorithms, examples, and arguments at the
recorded chapter ranges. Reconcile the thesis only after that body is
available. This census supplies no reason to repeat the exhausted
same-day external acquisition attempts.

**Local finding.** No new 1993 body was identified. Details and limits
of the local check appear below.

## 4. N9: complete the stated general-TBox ALC treatment

**Current disposition.** The former withheld classification has been
replaced in the ALC system card and both comparison tables.
handbook/parts/p09/alc-general-tboxes.tex supplies the definitions,
algorithm, examples, and theorems. The active annex fragment
handbook/annex/p09/alc-general-tboxes.tex supplies the two complete proofs.
Stable results are thm:p09-alc-type-elimination / annex:p9.alc.2 and
thm:p09-alc-general-exptime / annex:p9.alc.3.

**Mathematical work supplied.** The full finite TBox/ABox input, with an
optional tested concept, has a type-elimination decision algorithm and
a model of at most two to the closure-size elements when satisfiable.
The explicit deterministic upper bound is exponential; a polynomial
alternating-machine reduction proves EXPTIME hardness already for a
concept and TBox. Polynomial reductions cover subsumption and instance
checking. The earlier blocking tableau retains its distinct correctness
and termination proof in annex:p9.alc.1.

**Requirement pointer.** spec/registers/new-content.csv:116 marks N-c-009
mandatory and explicitly requires TBox/ABox treatment, blocking, and an
ExpTime complexity statement. Exact 2017 targets are recorded at
spec/research/p09-source-presentations-lot2-3.md:63–71: chapters 2, 4,
and 5, especially general knowledge bases from p. 83 and general
TBoxes from p. 117. Those exact textbook chapters remain a separate
source-reconstruction obligation.

**Remaining source action.** Obtain and inspect the exact 2017 chapters,
then reconstruct their own rule tables, blocking conditions, examples,
and proof organization. The acquired Donini--Massacci 2000 paper and
Baader--Horrocks--Sattler 2008 author draft support the classification
and have their own attribution. They do not constitute the 2017 body.

## 5. N13: replace the McNaughton report capsule with the article's mathematics

**Live location.** handbook/parts/p09/presentations/n-c-013.tex:921–938.
The current passage says that the article body was not obtained and
that its definitions, theorem wording, automaton data, constructions,
examples, and proof remain owed. Its current technical substitute is
explicitly only the contemporary Project MAC summary.

**Requirement pointer.** N-c-013 is a mandatory source row at
spec/registers/new-content.csv:120. The separate McNaughton obligation
and exact next visit are recorded at
spec/research/p09-source-presentations-lot2-3.md:629–637 and :979,
and spec/research/p09-mcnaughton-1966-source-note.md:205 onward.

**Next feasible writing action.** When the complete publisher article
is supplied through an available authorized route, inspect printed
pp. 521–530, define its original “testing,” “generating,” and
acceptance objects, and reconstruct its two equivalence constructions.
The later Safra and N18 constructions establish their own results;
they do not fill this source-specific gap. The local dedicated
directory still contains the Project MAC report and acquisition
metadata, not an identified complete journal body.

## McMillan local holdings check

The local search covered names and document inventories under source/,
tmp/, work/, and _campaign-root/, together with manuscript/source-note
references. The document inventory included 435 PDF, EPUB, DjVu, and
PostScript files. None had a modification date on or after 2026-09-06.
This is an inventory fact, not a content classification by date.

The McMillan-named PDF is still
tmp/pdfs/p09-mcmillan-1993/thesis.pdf:

- 1,712,433 bytes;
- SHA-256
  A458477801CBC806D9290F6F5FAF367A6860956FA52258EDDDF83A9DD4CDDFBF.

That hash matches the body already identified by its own title page
as the May 1992 CMU thesis, CMU-CS-92-131. Its title-page identity was
not newly inferred from the filename. The 69 relevant McMillan,
Springer-PDF, and book-DOI acquisition .body files in
tmp/acquisition/src057 were all empty. No newly identified book body
was found through the filename/identifier searches.

This does not rule out an unindexed copy under an unrelated name
outside the checked holdings. It does establish that no new 1993
body was identified on the authoritative local routes checked here.
No network acquisition, rendering, or source-version substitution
was attempted.

## Deliberate exclusions and practical order

Start with item 1, because its controlling body is already present and
its missing operation is concrete. The four source-dependent items
need their identified bodies before their source-specific writing can
be completed.

The census did not count every cited theorem, source-supplied proof
sketch, genuine open mathematical problem, survey scope limit,
historical source-version reconciliation, or generated-table repair
as missing mathematical authoring. The explanatory openings of
Parts X, XI, XIII, and XIV provide real chapter scope; “Phase-3
skeleton” comments in their drivers are not evidence that their
reader bodies are empty.

This is a bounded next-writing list. It is not whole-book mathematical,
source, publication, or admission acceptance. No handbook file,
test, build, or rendered output was changed.
