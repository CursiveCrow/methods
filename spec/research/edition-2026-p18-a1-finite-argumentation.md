# P18-A1: finite abstract argumentation

Date: 7 September 2026. Author: `/root/p5_kamp_source_review`.
Assignment: bounded finite-framework foundations for P18-A1, serving N-x-009.
Status: substantive reader body and complete proofs supplied and read back.
Independent source/topic/publication review, integration, production and
admission remain due. This note is an author handoff, not an acceptance record.

## Frozen files and supplied components

| Artifact | Extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p18/finite-argumentation.tex` | 1-289, complete new body | `685A2D6BF0125A07A5C85AEC0DA22CA9866B9799202750C758CA8BC1062C85AC` |
| `handbook/annex/p18/finite-argumentation.tex` | 1-201, all four complete proof items | `1B70FD5FA52B42BBCBA76976D484A0E2DFD1A67EDEEDDD1BB5D88713F9509BAA` |
| `source/references/dung-1995/dung-1995-ai77-n-games.pdf` | New unchanged capture of the 37 journal pages; reading extents below | `C78EE6D0864CA18A882E6CF79BB1356EFD86F1D32B38B55570FB572E4651FBA3` |

The unit supplies arguments and directed attack, empty frameworks and
self-attacks, attacked sets and attacker sets, conflict-freeness, defense,
the characteristic operator, admissibility, complete/grounded/preferred/stable
extensions, finite existence and inclusion results, and a terminating grounded
iteration. All four advertised results have complete proofs inside matching
`annexitem` environments. The six examples are stated as one theorem so their
full calculations also belong to an annex item rather than an untracked body
proof.

The grounded iteration is proved to reach an equality G_k = G_{k+1} for
k <= |A| and to identify the least fixed point among all fixed points. The
direct procedure therefore takes at most |A| + 1 operator evaluations,
including its terminating comparison. No constant-time operator evaluation,
polynomial bit complexity, or bound for enumerating all preferred extensions
is claimed.

## Existing holdings and bibliography

Before acquisition I searched source/reference and temporary filenames for
Dung, argumentation and semantic-PDF holdings, checked current author/source
notes, and inspected the canonical bibliography. No matching local article
capture was found by those checks. The existing `Dung1995` entry at
`handbook/bib/handbook.bib:2155-2164` already supplies Phan Minh Dung, the
correct article title, *Artificial Intelligence* 77(2), 321-357, 1995, and
DOI `10.1016/0004-3702(94)00041-X`.

The existing P8 reference at
`handbook/parts/p08/relevance-linear-supplement.tex:699-705` is expressly a
navigation pointer outside that chapter's technical scope. It is not a
previously completed Dung framework treatment. The new P18 files reuse
`Dung1995`; no duplicate bibliography entry was added or proposed.

## Verified primary-source identity and acquisition

The source is Phan Minh Dung, "On the acceptability of arguments and its
fundamental role in nonmonotonic reasoning, logic programming and n-person
games," *Artificial Intelligence* 77 (1995), 321-357. The captured pages have
the journal's typeset header, article title, author's AIT affiliation,
received June 1993/revised April 1994 line, numbered definitions/results,
and final printed page 357. This is a copy of the published journal-page
treatment, not the earlier condensed conference presentation mentioned in
the article's opening footnote.

The author's institutional publication lead is
[AIT's article PDF](https://www.cs.ait.ac.th/~dung/Site/Publications_files/n-games.pdf).
Its web-accessible article text and publication listing identified the exact
journal treatment. The local capture attempt at that host failed DNS
resolution. The successful source capture instead came from the
[Texas A&M institutional course copy](https://cse-robotics.engr.tamu.edu/dshell/cs631/papers/dung95acceptability.pdf).
The [publisher record](https://www.sciencedirect.com/science/article/pii/000437029400041X)
also identifies the same title and author in the 1995 journal issue. The
actual proof reading and visual verification used the saved Texas A&M copy.
No claim of byte equality with the AIT file is made.

The successful request on 7 September 2026 returned HTTP 200,
`application/pdf`, and `Last-Modified: Wed, 19 Aug 2026 21:04:10 GMT`.
The saved file is 6,384,273 bytes, unencrypted, with 37 letter-size pages,
PDF version 1.3. Its metadata records a 2013 Chrome/Quartz repackaging and
an unrelated digital-document author name; that metadata is not the article's
authorship or publication date. The printed journal leaves control identity.
The capture hash is recorded above. No source PDF was edited or re-exported.

## Actual reading

Read from the saved PDF, both as complete extracted page text and visually:

- Printed p. 321, physical p. 1: journal/title/author/version identity,
  abstract and conference-version footnote.
- Printed pp. 325-331, physical pp. 5-11, every page in full: the Section 2
  introduction, Definitions 2, 5, 6, 7, 13, 16, 20, 23 and the relevant
  lemmas/theorems; also the source's broader results and beginning of Section
  2.3, inspected to preserve their separate scope.
- Printed p. 357, physical p. 37: final journal header and references,
  confirming the last leaf of the held article.

The pagination is physical page = printed page - 320. All nine selected
source pages were rendered directly from the saved file in memory at 115 dpi
and visually inspected. No source-page image files were written. The PDF's
text extraction has several distorted glyphs and reports four invalid object
offsets while recovering its page tree. The actual required pages extracted
and rendered successfully; the visible mathematical source controlled the
definitions and formulas. The capture was preserved unchanged. The remaining
article pages were not read in this block, and no full-article proof-completion
claim is made.

The edition contract was read completely. The research and PDF skills guided
primary-source tracing and actual-page inspection. The explicit assignment
prohibited subagents and controlled the research skill's delegation suggestion.
Current `handbook.sty` environment interfaces and an editorial chapter were
inspected before writing. No new style definitions were introduced.

## Source-to-unit correspondence

| Source, printed location | New treatment |
| --- | --- |
| Definition 2 and Remark 4, p. 326 | `def:p18-finite-framework`: finite A, relation R, exact attack orientation, attacked-set and attacker-set notation. Source AR/attacks are mapped to A/R. |
| Definitions 5-6, p. 326; Definition 16, pp. 328-329 | Conflict-freeness, defense/acceptability, admissibility and the characteristic operator in the two opening definitions. Self-attacks and vacuous defense are explicit. |
| Lemma 10, p. 327; Lemmas 18-19, p. 329 | `thm:p18-defense-properties`, proved in `annex:p18.defense-properties`, lines 9-40. The proof first establishes monotonicity and preservation of conflict-freeness, then admissible images and both enlargement claims. It explicitly includes a=b in the conflict argument. |
| Definition 20 and Lemma 24, pp. 329-330; Theorem 25(2), p. 330 | `thm:p18-grounded-iteration`, proved in `annex:p18.grounded-iteration`, lines 42-79. Finite ascending iteration supplies existence, termination, leastness, uniqueness, complete fixed-point characterization and intersection of all complete extensions. |
| Definition 7, Theorem 11(2), Corollary 12, p. 327; Definitions/Lemmas 13-15, p. 328; Theorem 25(1), p. 330 | `thm:p18-extension-relations`, proved in `annex:p18.extension-relations`, lines 81-118. Finite maximal-admissible existence, stable-implies-preferred, preferred-implies-complete and the stable complement-of-attacked-set characterization are fully proved. |
| Example 9, p. 327; Lemma 15 counterexample, p. 328; Remark 26, p. 330 | `thm:p18-example-extensions`, proved in `annex:p18.example-extensions`, lines 120-201. Exact mutual-pair/self-attack patterns and additional finite constructions establish the claimed distinctions. |

The proofs are independently written for the finite scope. The general
existence assertion in the source is instantiated here by a finite-family
argument: choose a largest-cardinality member among admissible supersets of
a specified admissible set, then prove it is maximal under inclusion. This
does not define preferred extensions by largest cardinality; the unequal-size
example verifies the distinction concretely. No infinite maximality principle
or unproved fixed-point theorem is used in these finite proofs.

The source's broader Theorem 11(1) order-structure result, Theorem 25(3)
semilattice result, Lemma 28 continuity, Section 2.3 coincidence conditions,
and the logic-programming/game embeddings remain separate treatments. Reading
their boundary passages did not complete those obligations.

## Complete finite examples and acceptance convention

The annex establishes each full extension list by identifying all admissible
candidates and checking characteristic values or outsider attacks:

| Framework | Grounded | Complete family | Preferred family | Stable family |
| --- | --- | --- | --- | --- |
| Chain a attacks b, b attacks c | {a,c} | {{a,c}} | {{a,c}} | {{a,c}} |
| Mutual pair a/b | empty set | {empty set,{a},{b}} | {{a},{b}} | {{a},{b}} |
| Self-attacker a | empty set | {empty set} | {empty set} | empty family |
| Empty framework | empty set | {empty set} | {empty set} | {empty set} |
| a mutually attacks each of b,c | empty set | {empty set,{a},{b,c}} | {{a},{b,c}} | {{a},{b,c}} |
| Mutual a/b, both attack c, c attacks d | empty set | {empty set,{a,d},{b,d}} | {{a,d},{b,d}} | {{a,d},{b,d}} |

The chain's stages are empty set, {a}, {a,c}, {a,c}. The self-attacker also
has the conflicting fixed point {a}, showing why the complete-extension
definition must retain conflict-freeness. The unequal-size framework has
preferred extensions of sizes one and two. In the final framework, d occurs
in every preferred extension but not in the grounded extension; this supplies
a concrete witness for the distinction in Dung's Remark 26.

The final query definition is explicitly a handbook interface convention:
credulous acceptance uses existence of a containing extension; skeptical
acceptance uses a nonempty extension family and membership in every member.
For an empty family the report is "no extensions," and neither acceptance
label is assigned. The text also states what an unguarded universal would
do by vacuity and distinguishes the family {empty set}. This guard is not
misattributed as an alteration of Dung's stable semantics. Dung's historical
names for grounded/preferred semantics are also kept distinct from queries
over an arbitrary selected extension family.

No interpretation assigning premises, conclusions, speaker reliability or
truth values to the argument identifiers has been added. The chapter explicitly
states that its extension results cannot establish those external properties.

## Root intake and integration seam

Reuse the existing `Dung1995` bibliography entry. The root may add the verified
Texas A&M URL and access date through the current source-intake process, while
preserving the article identity and DOI. No new bibliography key is needed.

Proposed notation roles, scoped to `ch:p18-finite-argumentation`:

| Exact notation | Role / first anchor |
| --- | --- |
| `\mathcal F=(A,R)` | Finite framework, arguments and directed attack relation; `def:p18-finite-framework` |
| `\operatorname{Att}_{\mathcal F}(a)` | Set of attackers of a; same anchor |
| `S^+_{\mathcal F}` and local `S^+` | Arguments attacked by S; same anchor |
| `\mathsf F_{\mathcal F}` and local `\mathsf F` | Characteristic operator on subsets; `def:p18-defense-operator` |
| `G_{\mathcal F}`, `G_i` | Grounded extension and finite iteration stages; `def:p18-extension-semantics` / `thm:p18-grounded-iteration` |
| `\operatorname{Comp}`, `\operatorname{Pref}`, `\operatorname{Stab}` | Extension families of the supplied framework; `def:p18-extension-semantics` |
| `\mathcal F_{\rm chain}`, pair, self, empty, size, shared | Six local framework constants; `def:p18-example-frameworks` |
| `\mathcal E` | The selected extension family for the explicit acceptance queries; `def:p18-acceptance-queries` |

These names need their proper typed scopes in the root-owned symbol registry;
for example `\operatorname{Comp}` is an extension family here, not the P4
arithmetic computation formula. Existing subset, power-set, finite-cardinality
and numerical-order roles should be reconciled through the same intake.

The body opens a chapter with four sections. It belongs under stable P18,
printed XIV in the approved nineteen-part order. Root-owned inputs are:

```tex
\input{parts/p18/finite-argumentation}
\input{annex/p18/finite-argumentation}
```

The second line belongs in the P18 annex route under its owning wrapper.
The annex contains four `annexitem` records with backreferences to the four
body theorem labels; all `proved=annex:...` targets have those exact items.
No body proof environment or proof outside an annex item was introduced.
The author did not change main, part/annex drivers, style, bibliography,
symbols, provenance or acceptance records.

## Author verification and remainder

The complete initial 285-line body and complete 201-line annex were read back.
The small definition/display/title refinements were then read back, producing
the frozen 289-line body. The source correspondence, every proof direction,
the n+1 evaluation bound, all six extension lists and the empty-family cases
were checked by direct author reasoning. No mathematical gap is currently
known in the stated finite results. This is author verification, not an
independent review PASS.

The next step is root integration/intake followed by fresh independent source,
topic and publication reviews and the required output/admission gates. The
remaining A1/N-x-009 work includes the other abstract semantics/results and
infinite variants, structured argumentation, dialogue and informal-reasoning
methods, and their source-specific treatments. This chapter does not claim
completion of that broader requirement.

Only the two named manuscript files, this note and the one named source
capture were created. No tests, code changes, manuscript build/render, source
PDF edit, formal acceptance or subagent dispatch was performed. Other agents'
work and all existing source holdings were preserved.
