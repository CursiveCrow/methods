# LPO and historical KBO: definitions and complete selected metatheory

Date: 9 September 2026. This batch supplies complete mathematical treatments
for the existing reduction-ordering entries without editing their shared
host chapter. It preserves the original Knuth-Bendix zero-weight cases and
distinguishes that source's open-term comparison from later variants.

## Delivered artifacts

- Body: `handbook/parts/p12/reduction-orderings.tex`.
  SHA-256 `8F4B9B86FCA13279946743163A3C43FDE5E4E4E1C67B5F0B10340549A494A894`.
- Annex: `handbook/annex/p12/reduction-orderings.tex`.
  SHA-256 `A190C8D39136D98E4FB27956855A1209DFD6D306353C85274C61C2D924A630CD`.
- Bibliography intake: `handbook/bib/intake-p12-reduction-orderings.bib`.
  SHA-256 `DF90178190A92F8794457F04F2595302B82325EE37F9F84046A370E51B63AE30`.
- Twelve-row symbol intake:
  `handbook/registry/symbols-intake-p12-reduction-orderings.csv`.
  SHA-256 `6763C459C2EF399249E9910167D51A98B04EED64EA6D2CE7B6BE52AA8EF809A4`.

Eight body results have eight complete reciprocal proof annexes. The lead
can replace the two descriptive paragraphs in `parts/p12/rewriting.tex`
with precise links to `def:p12-ro-lpo`, `thm:p12-ro-lpo-termination`,
`def:p12-ro-kbo` and `thm:p12-ro-kbo-termination`, and route this section
and its proof file once. No new inference sheet is needed: the recursive
comparison clauses define metatheoretic relations, and the displayed
rewrite rules are worked inputs whose orientations are proved.

## Source identities and actual reading

### Dershowitz 1982

Nachum Dershowitz, *Orderings for Term-Rewriting Systems*, Theoretical
Computer Science 17(3), pp. 279-301, DOI
[10.1016/0304-3975(82)90026-3](https://doi.org/10.1016/0304-3975(82)90026-3).
The author-hosted complete 23-page article was acquired from
[Orderings4TRS.pdf](https://www.math.tau.ac.il/~nachumd/papers/Orderings4TRS.pdf)
as `tmp/pdfs/p12-reduction-orderings/dershowitz-1982.pdf`.
It has 948,954 bytes and SHA-256
`46C6E1565D32C9D66350BABD27E7B7EE8771CAEC237EC85AD9D823E8B52D0523`.
The actual first page gives the journal, pagination, author and article title.

The selected readings cover the introductory termination distinction,
Section 2's finite-rule/operator argument, embedding and simplification
conditions, and the later ordering comparisons on printed pp. 298-300.
The 1982 paper permits variable arity and includes a deletion condition;
our handbook's fixed-ranked setting makes that deletion operation
inapplicable. Its main recursive path order is not silently called LPO.
The selected finite-ranked tree lemma is proved completely in the new annex,
rather than importing an unexpanded appeal to Kruskal.

### Knuth-Bendix 1970

Donald E. Knuth and Peter B. Bendix, *Simple Word Problems in Universal
Algebras*, in *Computational Problems in Abstract Algebra*, pp. 263-297.
The publisher identifies the 1970 contribution at DOI
[10.1016/B978-0-08-012975-4.50028-X](https://doi.org/10.1016/B978-0-08-012975-4.50028-X).
The complete article scan was acquired from the
[Tufts course archive](https://www.cs.tufts.edu/~nr/cs257/archive/don-knuth/knuth-bendix.pdf)
as `tmp/pdfs/p12-reduction-orderings/knuth-bendix-1970.pdf`.
It has 617,156 bytes, 18 physical PDF pages covering printed pp. 263-297,
and SHA-256
`1B1F3ECAA6B4B3EE76131430A15F5AAB125DF557621755D11569DD5819738080`.
The selected controlling text in Sections 1-2, printed pp. 265-268, was
read directly from physical pages 2-4. The initial title/introduction and
group-ordering examples were also consulted. No full reading or
reconstruction of all completion experiments is claimed.

The finite operator sequence and strict total precedence, fixed arities,
positive nullary weights, possible greatest zero-weight unary symbol,
nonnegative higher-arity weights and minimum nullary variable weight are
all retained. The original equal-weight branch requires **equal variable
occurrence counts**, whereas the strictly greater-weight branch requires
dominance. This matters: the body and proof explicitly distinguish an
open pair that the original ordering leaves incomparable although every
ground instance decreases. No later dominance-based tie clause is
misattributed to the 1970 definition.

The original well-foundedness route is also supplied: fixed weight bounds
leaf/branching/positive-unary counts; erase the exceptional zero unary
symbol; select one of the finitely many cores; compare the finite tuple
of insertion counts lexicographically. The proof includes the omitted
strict-order cases and passes from open terms to ground terms using a
finite-support substitution on the variables of the first chain term.

### Kamin-Lévy note

The actual acquired title is *Attempts for Generalising the Recursive
Path Orderings*, by Sam Kamin and Jean-Jacques Lévy. The source is a
handwritten, undated scan conventionally attributed to 1980. Dershowitz's
1982 bibliography gives the related title *Two Generalizations of the
Recursive Path Orderings*; the citation records that distinction rather
than claiming the unprinted date or title is present in the scan.
The exact source file is
[kamin-levy80spo.pdf](https://www.cs.tau.ac.il/~nachumd/term/kamin-levy80spo.pdf),
saved as `tmp/pdfs/p12-reduction-orderings/kamin-levy-1980.pdf`:
2,871,004 bytes, 13 physical PDF pages, SHA-256
`3D4DF5964AA4860BA6A04FCD5F81516B18ABD426C7A4C77943B89C25F05B440A`.

The first four physical pages contain handwritten pages 1-8. These were
read as the actual embedded scanned images after text extraction returned
no text. The image files are preserved in the same evidence folder.
The selected pages give bounded lexicographic comparison, the three
general path clauses, the ordering-functional conditions, the structural
proof discussion and Ackermann examples. Their broader functional and
multiset possibilities remain distinct; the supplied theorem treats the
lexicographic member with declared fixed permutations of argument positions.
The rest of the handwritten note was not claimed read or reconstructed.

A PDF rendering library was unavailable; source reading used the original
embedded page images instead. No manuscript PDF was produced or inspected.

## Complete mathematical content

The LPO proof supplies recursive well-definedness, all transitivity cases,
irreflexivity, every proper-subterm case, context and substitution closure,
variable containment and ground totality under total precedence. The
finite-ranked embedding lemma contains the finite-product argument and the
minimal-bad-sequence proof in full, including why proper subterms form a
well-quasi-order and how to splice a smaller bad continuation. The
embedding/order comparison then proves well-foundedness. The finite-TRS
extension over a possibly infinite signature explicitly restricts each
derivation to the operators of its initial term and finite rules.

The KBO proof supplies the weight lower bound, both exact substitution
identities, irreflexivity and all transitivity cases, including comparisons
ending at a variable of minimum weight. It handles positive unary,
zero unary and zero-weight branching symbols in the subterm argument,
proves context closure and ground totality, proves substitution stability
case by case, and gives the full zero-chain well-foundedness argument.

Worked calculations cover all three Ackermann rules and their target
argument obligations, the falsely permitted expanding variant if that
obligation is dropped, four admissible zero-weight KBO orientations,
infinite descents for inadmissible unary and nullary zero-weight choices,
failure of substitution stability without variable dominance, reversal of
associativity direction when LPO status changes, and the substitution
obstruction to unrestricted commutativity. The final equal-weight
variable example documents a genuine limitation of the exact historical
ordering instead of changing its definition.

## Author checks and integration boundary

The complete new body and complete annex were read sequentially after
writing. The open-term KBO well-foundedness argument was sharpened to use
only the finite set of variables from the initial chain term, retaining
finite-support substitutions. The status-dependent associativity and
historical equal-count examples were checked as direct mathematical
comparisons. No software or prose test suite, independent review, build
or manuscript rendering was run.

This completes the selected LPO and original KBO entry definitions and
metatheory. It does not certify the complete 1982 paper, the complete
1970 completion presentation, the Baader-Nipkow book, a later KBO variant,
or every multiset/quasi-precedence/infinite-signature path-ordering theorem.
Those identified source presentations remain separate obligations.
The parent retains routing, canonical intake integration and the later
consolidated independent checks. Existing rewriting text, calculus sheets,
drivers and canonical records were not edited in this block.

The research and PDF skills guided the bounded primary-source readings
and this evidence record. Source-page images were a way to read an
image-only primary note, not manuscript layout inspection.
