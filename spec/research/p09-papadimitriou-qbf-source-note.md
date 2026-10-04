# Papadimitriou Theorem 19.1 on QSAT: source note

Retrieved 2026-08-22. Scope: acquisition gap `N-c-026` for Christos H.
Papadimitriou, *Computational Complexity* (Addison-Wesley, 1994), especially
the identity and printed location of Theorem 19.1, its exact QSAT input
language and reduction strength, the proof architecture actually present, and
the Stockmeyer--Meyer attribution in note 19.4.1. This note distinguishes
publicly exposed primary-text snippets from the complete body visible only in
the previously used nonpublisher scan.

## Result safe to state

The registered book is Christos H. Papadimitriou, *Computational Complexity*,
Reading, Massachusetts: Addison-Wesley, 1994, xv + 523 printed pages, ISBN
0-201-53082-1 (ISBN-13 978-0-201-53082-7), LCCN 93005662. The records inspected
do not supply a printed ordinal edition statement. Accordingly, **1994
Addison-Wesley edition** is safe; **first edition** and a particular printing or
impression should not be added without another source.

The exact locator is more precise than “pp. 455--458”:

- printed p. 455 starts Chapter 19 and Section 19.1, defines the book's QSAT
  language, and gives the QBF nomenclature footnote;
- printed p. 456 begins **Theorem 19.1** and its proof;
- printed p. 458 ends that proof;
- printed p. 487, note **19.4.1**, gives the historical attribution.

The theorem's exact short statement is: “Theorem 19.1: QSAT is
PSPACE-complete.” Its completeness is under the book's default
**deterministic logspace functional reduction**: a single output instance
`R(x)` is produced and satisfies `x in L1` iff `R(x) in L2`. In current
terminology this is a deterministic logspace many-one reduction, and is
strictly stronger than merely saying polynomial-time many-one.

The book calls the problem **QSAT**, not TQBF. Its p. 455 footnote says that the
problem is usually called QBF; `TQBF` does not occur at this locator. A modern
handbook may explain the relationship to TQBF, but it should not attribute the
name `TQBF` or an unrestricted input syntax to Theorem 19.1 itself.

One textual defect must remain visible. On p. 455 the displayed prefix, the
parity clause for `Q_n`, and the p. 456 circuit proof all specify the
existential-first language

`exists x_1 forall x_2 exists x_3 ... Q_n x_n phi`,

where `phi` is in conjunctive normal form, the quantifiers alternate strictly,
and `Q_n` is universal for even `n` and existential for odd `n`. But the prose
immediately before the display instead begins “for both truth values for the
variable x1,” thereby describing a universal-first prefix. Google Books
independently exposes both sides of this conflict. The author-titled errata
inspected below has no correction for p. 455. The most coherent identification
of the intended QSAT language is therefore the existential-first displayed
formula, supported by the parity sentence and proof, but a source-faithful
account must report the contradictory prose rather than silently repairing it.

## Edition identity and access

### Library of Congress record -- identity closed, body absent

The [Library of Congress record](https://www.loc.gov/item/93005662/) identifies
the author and title, “Reading, Mass. : Addison-Wesley, c1994,” the physical
extent “xv, 523 p. : ill. ; 25 cm,” call number `QA267.7 .P36 1994`, and LCCN
93005662. It exposes catalog data only, not Chapter 19.

### Google Books record and public primary-text snippets -- partial body

The [Google Books volume record](https://books.google.com/books/about/Computational_Complexity.html?id=JogZAQAAIAAJ)
records Addison-Wesley, 1994, 523 pages, and both ISBN forms. Its metadata field
“illustrated, reprint” is not a printed ordinal edition statement and should
not be converted into “first edition.” Google Books is also not itself the
publisher; the earlier description “Google Books publisher record” overstates
its provenance. It is a Google-managed bibliographic and scan record that names
Addison-Wesley as publisher.

Google's [public view-status response for ISBN 0-201-53082-1](https://books.google.com/books?jscmd=viewapi&bibkeys=ISBN:0201530821)
marks this volume `noview`, not embeddable, and not downloadable as PDF or
EPUB. Nevertheless, its public search-within-volume interface returns limited
primary-text snippets with printed page numbers. The following were directly
inspected:

- [Theorem-number search](https://books.google.com/books?jscmd=SearchWithinVolume2&vid=JogZAQAAIAAJ&q=%22Theorem%2019.1%22):
  p. 455 locates the end of the definition and p. 456 exposes the theorem
  statement and proof opening.
- [The p. 455 prose search](https://books.google.com/books?jscmd=SearchWithinVolume2&vid=JogZAQAAIAAJ&q=for%20both%20truth%20values%20for%20the%20variable%20x1)
  reproduces the universal-first wording.
- [The p. 455 parity/display search](https://books.google.com/books?jscmd=SearchWithinVolume2&vid=JogZAQAAIAAJ&q=nth%20quantifier%20is%20for%20all%20if%20n%20is%20even)
  returns the existential-first displayed prefix and the clause that the last
  quantifier is universal for even `n` and existential for odd `n`.
- [The p. 456 circuit search](https://books.google.com/books?jscmd=SearchWithinVolume2&vid=JogZAQAAIAAJ&q=AND%20gates%20if%20i%20is%20even)
  says even levels are AND levels because those variables are universally
  quantified, while odd levels are OR levels. This confirms the
  existential-first reading.
- [The p. 456 Savitch search](https://books.google.com/books?jscmd=SearchWithinVolume2&vid=JogZAQAAIAAJ&q=restatement%20of%20the%20proof%20of%20Savitch)
  exposes the configuration-reachability setup.
- [The p. 458 logspace search](https://books.google.com/books?jscmd=SearchWithinVolume2&vid=JogZAQAAIAAJ&q=construction%20can%20indeed%20be%20performed%20in%20logarithmic%20space)
  exposes the claimed construction bound.
- [The p. 458 complement search](https://books.google.com/books?jscmd=SearchWithinVolume2&vid=JogZAQAAIAAJ&q=precisely%20the%20complement%20of%20QSAT)
  exposes the DNF/complement and `PSPACE = coPSPACE` finish.

These snippets independently confirm the current nonpublisher scan at pp.
455, 456, and 458. They do not expose a continuous page body, the central p.
457 recursion, or the p. 487 attribution note.

### Library digitizations -- matching object found, readable body not acquired

The [Internet Archive metadata record](https://archive.org/metadata/computationalcom0000papa)
identifies a scanned 1994 Addison-Wesley object with ISBN 0201530821, LCCN
93005662, 554 scan images, and Open Library edition `OL1398106M`. It is in the
`internetarchivebooks` and `printdisabled` collections and is marked
`access-restricted-item: true`; its OCR, page images, and ordinary PDF are
private, while only encrypted lending derivatives are exposed. The
[item page](https://archive.org/details/computationalcom0000papa) therefore does
not provide an anonymously readable Chapter 19 body, and its public
search-inside request returned “Item not available.” An older Open Library
identifier, `computationalcom00papa`, now resolves at the metadata endpoint only
to a dark item shell and supplies no recoverable body.

The [HathiTrust Bibliographic API query by ISBN](https://catalog.hathitrust.org/api/volumes/full/isbn/0201530821.json)
returned no records and no items on 2026-08-22; the same was true for LCCN
93005662 and OCLC 28421912. The Library of Congress record has no page images.
No current Pearson/Addison-Wesley full-body page was located in this pass.

Consequently, **no publisher-issued or named-library-readable body was acquired
that can confirm every line of pp. 455--458 and 487**. Google Books provides
useful independent primary-scan snippets, but its record does not identify a
source library and its `noview` status prevents full inspection.

## Exact decision problem and reduction strength

### Input language

Subject to the p. 455 prose defect already recorded, the displayed and
proof-controlled problem is:

- input: a Boolean expression `phi(x_1,...,x_n)` in conjunctive normal form;
- prefix: one Boolean quantifier per variable, strictly alternating and
  beginning existentially;
- question: whether the resulting closed quantified Boolean expression is
  true.

The p. 455 dummy-variable observation says that consecutive like quantifiers
can be separated to enforce strict alternation. It does not state the modern
unrestricted-TQBF syntax. The theorem should therefore be cited for this
CNF, existential-first, strictly alternating QSAT language; a passage to a
different TQBF presentation requires a separately stated syntactic reduction.

### Reduction type

Section 8.1, printed p. 160, defines the book's reduction as a function from
strings to strings computed by a deterministic machine in `O(log n)` space,
preserving membership in both directions. The definition is exposed by the
[Google Books p. 160 reduction search](https://books.google.com/books?jscmd=SearchWithinVolume2&vid=JogZAQAAIAAJ&q=language%20L1%20is%20reducible%20to%20L2).
Section 8.2, printed p. 165, then defines `C`-complete for a language already
in `C` to mean that every language in `C` reduces to it; see the
[p. 165 completeness search](https://books.google.com/books?jscmd=SearchWithinVolume2&vid=JogZAQAAIAAJ&q=Let%20C%20be%20a%20complexity%20class).

Theorem 19.1's own proof reinforces that default. Printed p. 457 rejects the
naive duplicated reachability formula because it would not give a
logarithmic-space reduction, and p. 458 says the final layered formula can be
constructed in logarithmic space. Thus the safe strength is:

`QSAT is PSPACE-complete under deterministic logspace many-one reductions.`

The phrase “many-one” is a modern description of the book's functional map;
it is not a claim that the theorem title itself prints that phrase.

## Proof architecture actually present

The complete architecture below was directly inspected in the current
[nonpublisher primary-text scan](https://djvu.online/file/ugtJZIrmGbFU7),
printed pp. 456--458. The provenance labels in the right column delimit what an
independent lawful source presently confirms.

| Printed locator | Step actually present in Papadimitriou | Independent status |
|---|---|---|
| p. 456 | Membership: arrange all assignments as a depth-`n` binary tree, view alternating levels as OR/AND circuit levels, and evaluate the implicitly represented circuit in `O(n)` space using the earlier circuit-depth method. | **GOOGLE BOOKS SNIPPET-CONFIRMED.** |
| p. 456 | Hardness setup: for a polynomial-space decider `M`, use its configuration graph, encode a configuration by `n^k` bits, and recast Savitch reachability as formulas `psi_i(A,B)` for paths of length at most `2^i`. | **GOOGLE BOOKS SNIPPET-CONFIRMED.** |
| p. 457 | Base formula: `psi_0` says equality or one legal machine step. A naive midpoint conjunction duplicates `psi_i` and grows exponentially. | **NONPUBLISHER BOOK BODY ONLY; method corroborated by the 1973 author copy below.** |
| p. 457 | Single-copy recursion: quantify a midpoint block `Z` and universal endpoint blocks `X,Y`, then require `psi_i(X,Y)` whenever `(X,Y)` is either `(A,Z)` or `(Z,B)`. The book explicitly compares reusing that one subformula with Savitch's reuse of work space. | **NONPUBLISHER BOOK BODY ONLY; essentially the same displayed recursion occurs in Stockmeyer--Meyer Theorem 4.3.** |
| p. 457 | Normalize the nested formula to prenex form. Its CNF would be too large, but its DNF is small and can be extended layer by layer. | **NONPUBLISHER BOOK BODY ONLY.** |
| p. 458 | Emit `n^k` layers in logarithmic space. This first reduces every PSPACE language to the DNF-matrix version, which the text identifies as the complement of its displayed QSAT language with a CNF matrix; complement the reduction and use `PSPACE = coPSPACE` to obtain QSAT-hardness. | **GOOGLE BOOKS SNIPPET-CONFIRMED at the construction and final inference.** |

Two distinctions matter for a handbook reconstruction.

1. Papadimitriou's displayed reuse device quantifies whole endpoint blocks
   universally; it does **not** literally use the later-presented selector-bit
   formula with existentially chosen endpoint blocks. A selector-bit proof can
   be a valid modernization, but it must not be presented as Papadimitriou's
   exact displayed construction.
2. The proof does not simply end after constructing a reachability QBF. It
   explicitly encounters the CNF/DNF polarity issue and finishes through the
   complement language and `PSPACE = coPSPACE`.

Because Google Books does not expose p. 457 and the Internet Archive body is
restricted, exact page-specific wording and formula typography on p. 457 remain
unconfirmed by a publisher/library-readable copy even though the architecture
is independently consistent with the first-party 1973 source.

## Stockmeyer--Meyer attribution

### What Papadimitriou literally attributes

The current book scan's note **19.4.1**, printed p. 487, begins: “The
PSPACE-completeness of QSAT was established in” and then cites L. J. Stockmeyer
and A. R. Meyer, “Word problems requiring exponential time,” *Proceedings of
the Fifth ACM Symposium on Theory of Computing*, pp. 1--9 (1973).

This wording assigns establishment of the result to that paper. It does **not**
literally say “the first proof,” “independently,” or “first
PSPACE-completeness proof.” Those stronger historical formulations should not
be put in quotation marks or represented as Papadimitriou's exact wording.
The p. 487 sentence itself is still **NONPUBLISHER-BODY ONLY**: Google Books did
not return a p. 487 snippet, and no readable publisher/library copy of that page
was acquired.

### The cited primary source -- identity and mathematical match closed

The [official ACM record](https://doi.org/10.1145/800125.804029) gives the full
title “Word Problems Requiring Exponential Time: Preliminary Report,” authors
L. J. Stockmeyer and A. R. Meyer, STOC 1973, pp. 1--9, DOI
10.1145/800125.804029, published 30 April 1973. This confirms the book note's
authors, venue, year, and pages; Papadimitriou simply omits the subtitle
“Preliminary Report.”

Albert R. Meyer's [first-party publication list](https://people.csail.mit.edu/meyer/resume.html)
links an [author-hosted nine-page paper copy](https://people.csail.mit.edu/meyer/meyer-stockmeyer-word-probs.pdf).
In that copy:

- Section 2 defines the alternating Boolean languages `B_k`, beginning with an
  existential variable block, and `B_omega` as their union;
- the reduction definition is a logspace-computable function preserving
  membership, hence a logspace many-one reduction;
- Section 4, **Theorem 4.3** (fifth PDF page), states that `B_omega` is
  logspace-complete in polynomial space;
- the proof on the fifth and sixth PDF pages uses encoded instantaneous
  descriptions, bounded reachability, and the same single-copy quantified
  midpoint construction later presented by Papadimitriou.

The original paper's theorem is phrased for `B_omega`, with finite blocks of
Boolean variables and its own formula syntax, not under Papadimitriou's later
name `QSAT`. It confirms the historical source and proof lineage; it should not
be quoted as though it literally states Papadimitriou's CNF scalar-variable
problem.

### Errata checked

An [institutional Duke mirror of the author-titled errata](https://courses.cs.duke.edu/spring07/cps240/books/P/PapadimitriouErrata.pdf)
was text-inspected in full. Its heading identifies *Computational Complexity*,
Christos H. Papadimitriou, Addison-Wesley, 1994, and its corrections run through
p. 500. It contains no entry for p. 455 or Theorem 19.1. Helsinki University of
Technology's [supplementary errata page](http://www.tcs.hut.fi/Studies/T-79.240/errata.html)
explicitly labels itself unofficial and links the old publisher errata; it adds
a Chapter 19 correction for p. 461, but none for p. 455. Absence from these
lists does not resolve the literal p. 455 contradiction.

## Evidentiary disposition for Part IX

| Item | Disposition | Safe consequence |
|---|---|---|
| 1994 book identity | **CLOSED** by Library of Congress, Google Books, and matching Internet Archive metadata | Cite Papadimitriou, *Computational Complexity*, Addison-Wesley, 1994, xv + 523 pp., ISBN 0-201-53082-1. Do not add an ordinal edition or exact printing. |
| Theorem and printed locator | **CLOSED** for statement/pagination | QSAT is defined on p. 455; Theorem 19.1 begins p. 456 and its proof ends p. 458. Saying “Theorem 19.1, pp. 456--458” is exact; “pp. 455--458” names the whole definition-plus-proof presentation. |
| Exact input syntax | **CLOSED WITH A PRINTED CONTRADICTION** | State the existential-first, strict-alternation, CNF language as controlled by the display/parity/proof, and record that the preceding prose accidentally describes universal-first. Do not attribute unrestricted TQBF syntax to the theorem. |
| Reduction strength | **CLOSED** | State deterministic logspace many-one completeness, not merely polynomial-time completeness. |
| Proof architecture | **PARTIALLY CLOSED** | Membership, Savitch/configuration setup, logspace output, and complement/coPSPACE finish are independently snippet-confirmed. The exact p. 457 body is known only from the current nonpublisher scan, though the original author-hosted 1973 proof corroborates its construction. |
| Stockmeyer--Meyer source | **CLOSED** | Cite Stockmeyer--Meyer, STOC 1973, pp. 1--9, DOI 10.1145/800125.804029, and distinguish its `B_omega` theorem from Papadimitriou's later QSAT syntax. |
| Papadimitriou's exact priority sentence and p. 487 locator | **SOURCE LEAD, NOT AUTHORITATIVE-BODY CLOSED** | The current scan says the PSPACE-completeness “was established in” Stockmeyer--Meyer. Do not strengthen that to an exact “first proof” quotation until p. 487 is checked in a publisher/library-readable body. |
| Full publisher/library comparison | **OPEN** | Google Books snippets independently agree at pp. 455, 456, and 458, but the Google volume is `noview`, the Internet Archive item is restricted, HathiTrust has no item, and the Library of Congress exposes metadata only. Full comparison of pp. 457 and 487 remains required. |

The acquisition gap is therefore narrowed but not completely closed. The
edition identity, theorem statement, precise theorem pages, intended QSAT
syntax (with its printed contradiction), and logspace many-one strength are
source-secure. Exact quotation or typography from the central p. 457 proof and
the p. 487 priority note must remain provenance-qualified until a readable
publisher or library copy is inspected.
