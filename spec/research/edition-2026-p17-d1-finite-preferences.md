# P17-D1: finite preferences and ordinal representation

Date: 7 September 2026, Pacific time. Author:
`/root/standard_pa_argumentation_source_review`. Assignment: NOW-07/09,
bounded finite P17-D1 foundation. The block began at approximately 23:46 UTC
on 7 September; the source/body/proof checkpoint was sent before 00:01 UTC
on 8 September. This return is within the assigned 45-minute block.

Status: **WRITTEN**, with complete author readback. Fresh independent source,
topic and publication reviews, root integration, production evidence and
formal admission remain due. This author note does not supply acceptance or
claim completion of the full P17-D1 subject.

## Frozen outputs

Repository: `C:\Dev\the-methods-of-reason`, branch `phase4-codex`, HEAD
`35d537c692bb74b532dc4aa750da381a7fe4daf2`. These artifacts are new live
files; HEAD does not contain their manuscript text.

| Artifact | Complete extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p17/finite-preferences.tex` | 1-330, complete new chapter | `7C70F6C3428EFD358BDFDD99BA03911699DD7A4A16179033B408B9F9BE2AD988` |
| `handbook/annex/p17/finite-preferences.tex` | 1-324, seven complete annex items | `30FAEDDD5023D3F64A565FA669C47980DE325A2BFECB6F96ACAED9398E204FE1` |
| `source/references/rubinstein-microeconomic-theory-2015/rubinstein-second-edition-revision-2015-01-11.pdf` | 172 physical pages; selected reading below | `F7CEA2C4F48C77D93DD25C30BBDA83E051C6562A589256AAC8CBA1B5084A33F8` |

The note's own digest is returned after final write/readback.

The unit supplies complete and transitive weak preference with the diagonal
included in completeness; strict preference and indifference; the equivalence
classes and their total order; finite ordinal representation with a canonical
class rank; precise uniqueness on attained values and a proved extension to
the real line; maximal choice on finite menus; and explicit empty, singleton,
tied, cyclic and ordinal-interpretation boundaries.

## Holdings and primary-source identification

Before acquisition I searched source/reference and temporary holdings by
Rubinstein/preference/microeconomics names and inspected the canonical
bibliography for the author and relevant titles. The name search produced
unrelated Microsoft records from the broad micro substring, but no matching
Rubinstein book capture. The bibliography contained no matching Rubinstein
preference or microeconomics entry in those checks. No preexisting source
body or source-specific acceptance was assumed.

Rubinstein's [author books page](https://arielrubinstein.tau.ac.il/books.html)
identifies *Lecture Notes in Microeconomic Theory: The Economic Agent* and
its second edition, and describes the books as freely downloadable. The
general current download route leads to a registration page. I did not
register, submit personal information or obtain a newer version through
that route. An indexed public author-hosted PDF locator was available
directly: [Rubinstein2007.pdf](https://arielrubinstein.tau.ac.il/Rubinstein2007.pdf).

The actual saved PDF establishes its identity and version:

- Physical page 2 explicitly dates the revision to **11 January 2015** and
  names Ariel Rubinstein.
- Physical page 3 gives the full title, subtitle *The Economic Agent*,
  **Second Edition**, author, and Princeton University Press imprint.
- Physical page 4 carries copyright 2012, the publisher details and
  ISBN **978-0-691-15413-8**.
- The final physical page 172 is printed page **158**, ending the references.

Thus the held source is the **11 January 2015 author-hosted revision of the
2012 second edition**. The URL's 2007 filename is not its version date. This
is not claimed to be the latest revision, or byte-identical to the originally
printed second edition. The chapter uses a version-specific citation key.

The authorized free download completed from the public author URL using
`curl --fail --location`. The retained file has 1,431,428 bytes, 172 A4 pages,
PDF version 1.4, and is unencrypted. Its metadata records PDFCreator/Ghostscript
and January 2015 timestamps, with a generic digital-author field Benjamin.
The printed title/revision leaves establish the literary author and version;
the digital-author field does not replace them. The source PDF was preserved
without editing, filling, flattening or re-exporting.

## Actual source reading

All thirteen selected pages below were read visually in full from the saved
PDF after rendering at 110 dpi. Text extraction was an additional reading aid;
the visible source controlled the weak-preference glyph and mathematical
formulas. A truncated combined text output was followed by a separate
retrieval of the identity pages and printed page 5.

| Physical pages | Printed location | Actual scope read |
| --- | --- | --- |
| 2-4 | Revision, title and copyright leaves | Author/title/subtitle, explicit second-edition designation, dated 2015 revision, imprint and ISBN. |
| 19-22 | pp. 5-8 | Questionnaire R including diagonal pairs; Definition 2 completeness/transitivity; Table 1.1; source translation discussion/proof and the strict/indifference definitions in the summary. |
| 26-28 | pp. 12-14 | Utility-representation definition; ordinal interpretation; increasing-transform claim and proof; finite-extrema argument; finite elimination construction and proof; beginning of the separate countable-domain result. |
| 44-45 | pp. 30-31 | Stable interpretation of alternatives across menus; motivation for correspondences under ties; nonempty-menu choice-correspondence definition and exact induced-choice formula; neighboring revealed-preference scope. |
| 172 | p. 158 | Final reference leaf and manifestation endpoint. |

The remaining 159 PDF pages were not read. In the inspected body locations,
physical page equals printed page plus 14. These passages cover the complete
source definitions and finite construction used by this unit. The source's
other lectures, exercises, infinite-domain proofs and full choice-rationalization
presentation have not been supplied or accepted by this reading.

Temporary source-page PNGs were created outside the repository and removed
after inspection. No manuscript pages were built or rendered.

## Source conventions, corrections and justified additions

| Source location | Current manuscript treatment |
| --- | --- |
| pp. 5-6, Questionnaire R and Definition 2 | `def:p17-weak-preference` uses the same completeness and transitivity conditions. Completeness includes x = y, so reflexivity is derived. The source's weak-comparison glyph is mapped to the chapter's `\succeq`; its direction is unchanged. |
| pp. 7-8, Table 1.1 and summary | Strict preference means one weak comparison and failure of its reverse; indifference means both weak comparisons. The manuscript retains these meanings and proves their properties. |
| p. 12, utility definition | Ordinal representation is the biconditional x R y iff u(x) >= u(y), including ties. The chapter explicitly identifies this with the source's utility-representation usage. |
| pp. 13-14, finite existence argument | The chapter supplies the class quotient and proves finite least-class elimination. Its zero-based class rank counts strictly lower classes. The annex proves that the source's one-based successive elimination values are exactly u_0 + 1 on nonempty X. |
| p. 13, increasing-transform claim | The source's sufficiency of a strictly increasing real transformation is preserved. The manuscript adds and proves the exact converse on attained values, uniqueness there, and a piecewise-affine extension for finite attained domains. |
| p. 31, induced choice correspondence | On nonempty finite menus, the manuscript uses the exact set of alternatives weakly above every menu member and proves it is nonempty. It proves equivalence with strict undomination, representation maxima, comparison recovery and the selected menu-restriction identity. |

### Nonempty extrema and empty inputs

The source's printed lemma on page 13 says that any finite subset has a
minimal element, while the proof on page 14 begins at a singleton. Taken
literally the displayed wording lacks the necessary nonemptiness hypothesis.
The new treatment states and proves the lemma only for **nonempty** finite
sets of classes. It separately proves the empty-domain representation case
and performs no elimination or extremum choice when no class remains.
This is a direct correction of the missing edge hypothesis in the supplied
finite treatment; the retained source bytes are unchanged.

The source defines a choice correspondence on nonempty menus with nonempty
values. The new chapter proves that condition for finite weak preferences
and explicitly extends the operator to the empty menu by C(empty) = empty.
Its generic C_R formula is also defined for arbitrary binary relations so
that the cyclic counterexample is well typed; the nonempty-choice theorem
continues to require a weak preference. A tied choice set is a set of
retained alternatives, not a specified single selection.

### Ordinal uniqueness

For fixed representations u and v, the unique map on attained values is
f(u(x)) = v(x). Its well-definedness follows from the equivalence between
equal representing values and indifference. Its strict increase and
bijection properties are proved in both directions. The domain of this
unique map is exactly u(X), not all real numbers.

For finite attained domains, the annex proves that f extends to a strictly
increasing F on the real line: translation for a singleton; linear
interpolation with positive slopes between successive attained values and
positive-slope exterior rays for larger domains; and a separately specified
empty-domain case. Altering the left exterior slope proves nonuniqueness
outside a nonempty attained domain. Empty-domain extensions are also
nonunique. These are handbook deductions at the declared finite scope;
they are not misattributed as the source's exact converse theorem.

No infinite-domain extension assertion is inferred from this finite proof.
No expected-utility theorem, cardinal uniqueness theorem, probability model
or empirical claim about actual comparisons has been added.

## Complete results and annex links

| Body result / start | Reciprocal annex / start | Complete supplied content |
| --- | --- | --- |
| `thm:p17-preference-structure`, 76 | `annex:p17.preference-structure`, 12 | Reflexivity; strict irreflexivity/asymmetry/transitivity; comparison trichotomy; indifference equivalence and partition; well-defined total quotient order. |
| `thm:p17-finite-representation`, 121 | `annex:p17.finite-representation`, 67 | Necessity of completeness/transitivity; finite nonempty least-class induction; rank enumeration and bijection; exact ordinal representation; termination/source-rank bridge; empty/singleton/all-tied cases. |
| `thm:p17-ordinal-uniqueness`, 171 | `annex:p17.ordinal-uniqueness`, 147 | Both directions of the attained-value scale characterization; its uniqueness; explicit finite extension; nonuniqueness outside the image; preserved comparisons. |
| `thm:p17-maximal-choice`, 214 | `annex:p17.maximal-choice`, 212 | Strict undomination equals weak maxima; numerical representation; nonempty finite choices; highest met class; representation invariance; singleton/empty menus; pairwise recovery and menu restriction. |
| `thm:p17-tied-preference-example`, 259 | `annex:p17.tied-preference-example`, 255 | Complete tied classes, both numerical representations and all specified menu choices. |
| `thm:p17-preference-cycle`, 290 | `annex:p17.preference-cycle`, 280 | Complete/reflexive cyclic relation, failed transitivity, impossibility of ordinal representation and empty maximal set. |
| `thm:p17-ordinal-boundary`, 300 | `annex:p17.ordinal-boundary`, 303 | No affine relation between the two example scales; different gaps and average comparisons; identical original preferences/choices. |

All seven body `proved=annex:...` fields have exact reciprocal annex items.
All proofs are inside their `annexitem` environments. The tied example's
second representation is verified directly from its table, so the
non-affine boundary example introduces no circular dependence on the
uniqueness theorem.

## Explicit examples and boundaries

The tied example has X = {a,b,c,d,e}, with class order
{a,b} below {c} below {d,e}. The two complete numerical tables are:

| Alternative | a | b | c | d | e |
| --- | --- | --- | --- | --- | --- |
| Canonical t = u_0 | 0 | 0 | 1 | 2 | 2 |
| Second representation v | 0 | 0 | 1 | 10 | 10 |

The choices from X and {a,c,d,e} are {d,e}; from {a,b,c} the choice is
{c}; from {a,b} it is {a,b}. Every singleton retains its member, while
the empty menu has empty output. All original comparisons and all menu
choices are the same for t and v.

The affine equation v = alpha t + beta would force beta = 0 at a and
alpha = 1 at c, then fail at d. The two adjacent t gaps are both one;
the corresponding v gaps are one and nine. The endpoint arithmetic average
equals the middle value for t, but is five, strictly above the middle value
one, for v. These exact calculations show that an ordinal ordering does not
fix such gap or average comparisons. They do not assign preferences to
lotteries or claim an expected-utility representation.

The cyclic input contains exactly the three diagonal pairs and (a,b),
(b,c), (c,a). It is complete and reflexive, but fails transitivity at
(a,b),(b,c). A representation would require u(a) > u(b) > u(c) > u(a).
Each alternative also fails to be weakly above one other alternative, so
its full-menu maximal set is empty. This input fails the weak-preference
hypothesis; it is not mislabeled as a represented preference.

For empty X the relation, quotient, rank and representing function are all
empty, with the corresponding vacuous statements proved. For a singleton,
the unique weak preference is reflexive and any assigned real value
represents it. On a nonempty all-tied set the quotient has one class and
exactly the constant functions are representations.

## Exact root intake

The new bibliography key is `Rubinstein2015LectureNotes`. The proposed
record preserves the 2012 edition identity and explicitly names the held
2015 revision:

```bibtex
@book{Rubinstein2015LectureNotes,
  author    = {Rubinstein, Ariel},
  title     = {Lecture Notes in Microeconomic Theory},
  subtitle  = {The Economic Agent},
  edition   = {2},
  publisher = {Princeton University Press},
  location  = {Princeton and Oxford},
  year      = {2012},
  isbn      = {978-0-691-15413-8},
  note      = {Author-hosted revision dated 11 January 2015},
  url       = {https://arielrubinstein.tau.ac.il/Rubinstein2007.pdf},
  urldate   = {2026-09-07},
}
```

The reader citations identify the 2015 revision and use its actual printed
pages. The filename is not a claim that the unit uses a 2007 edition.
Root owns addition of this key and the canonical source records.

Stable placement is **P17**, printed **XIII** in the approved nineteen-part
order. Required root-owned driver seams are:

```tex
\input{parts/p17/finite-preferences}
\input{annex/p17/finite-preferences}
```

The chapter anchor is `sec:p17-finite-preferences`, followed by five section
anchors. The annex anchor is `sec:annex-p17-finite-preferences`, with seven
proof items. Root owns the part/annex wrappers, main driver and acceptance
records. None were edited by this author.

Typed symbol intake, scoped to `sec:p17-finite-preferences`:

| Symbol | Role / first declaration |
| --- | --- |
| X; x,y,z | Finite alternative set and its members; `def:p17-weak-preference`. |
| `\succeq`, `\succ`, `\sim` | Weak preference, its strict part and its indifference part; same definition. |
| `[x]`, `\mathcal Q`, `X/{\sim}` | Indifference class, class set and quotient; `def:p17-preference-quotient`. |
| `\unrhd` | Total comparison of indifference classes; same definition. |
| R | Generic binary relation on X, used in representation and choice definitions. |
| u, v | Real-valued ordinal representations; `def:p17-ordinal-representation` and its theorem. |
| k, I_k, r, u_0 | Number of classes, zero-based rank set, class rank and canonical representation; `def:p17-ordinal-representation`. |
| D, f, F, u(X) | Attained-value domain, its increasing change of scale, real-line extension and attained image; `def:p17-increasing-scale-change` and `thm:p17-ordinal-uniqueness`. |
| A,B as menus; `C_R(B)` | Menus and the weak-maximum operator; `def:p17-maximal-choice`. A,B used as classes in the quotient definition have that separate local role. |
| `\succeq_{\rm tie}`, t, v | The tied-example relation and its two complete score tables; `def:p17-tied-preference-example`. |
| `X_{\rm cyc}`, `R_{\rm cyc}` | Explicit three-element cyclic comparison input; `def:p17-preference-cycle`. |

The unit reuses existing finite-set, function, equivalence-relation, order,
natural-number and real-number vocabulary and the standard `\N`, `\R`
and `\defeq` interfaces. No new macros or shared style rules were added.

## Author verification and precise remainder

Read the entire edition contract and the research and PDF skills. The
research skill guided the holdings search, primary-source identity/version
verification and this single note. The assignment explicitly prohibited
subagents, so research and authoring were performed directly. The PDF skill
guided the thirteen actual source-page inspections.

Both manuscript files were read completely after writing. The direct table
verification of the second tied-example representation was kept independent
of the uniqueness theorem's non-affine observation. Every selected proof
direction, finite construction step, empty/tied case and numerical example
was checked by author reasoning. This does not constitute independent review.

No prose tests, executable mathematical test program, manuscript build or
render, formal admission, shared driver change, canonical bibliography or
symbol edit, or subagent dispatch occurred. The only repository creations
are the two owned manuscript files, this note and the one named primary
source PDF. Other agents' edits were preserved.

The next concrete tasks are root bibliography/symbol/placement intake; three
fresh independent reviews of the frozen source, mathematical and publication
scopes; then the required scoped static/build/visual checks and exact-snapshot
admission. A failure or unresolved finding in any required scope remains open
and reopens the affected review after correction.

The broader remaining P17-D1 work includes the required source's other
preference formalizations and presentations, infinite/countable representation
and its qualifications, continuity and other additional structures,
choice-rationalization and revealed-preference results, cardinal and expected-
utility models with their own primitives/axioms/proofs, and any empirical or
normative claims. No full D1 completion is asserted by this finite unit.
