# C7 author handoff: Kamp Chapter IV, Theorem 1

Date: 8 September 2026. Assignment: `/root/kamp_lemma7_author`, resumed at
10:34 UTC. This is an author completion record for the exact real-order
theorem, its three source lemmas, and the source corollary. Consolidated
independent reviews remain deferred under the current user instruction.

## Saved manuscript and scope

| File | Lines | Bytes | SHA256 |
| --- | ---: | ---: | --- |
| `handbook/parts/p09/presentations/kamp-iv1-unary-separation.tex` | 249 | 10595 | `8D6F6618ADC5F8D9F79702BBCFBD777737C6B53347BD9EDB157E14CB59417D9C` |
| `handbook/annex/p09/kamp-iv1-unary-separation.tex` | 435 | 19450 | `1350D472A3307C9E88C82FA41B96A19F78E7A66F31A11D29DB0691F167FED732` |

All assigned paths were unused before this block. Only the two new manuscript
files and this note were written. The new text supplies the complete theorem
for the usual strict real order: neither strict SINCE nor strict UNTIL is
definable by a finite formula from sentential connectives and the entire
alphabet of source-definable unary real-order tenses. It quantifies over every
input pair and uses the actual even/odd-integer interpretation. It does not
restrict the unary alphabet to a selected finite temporal basis.

## Primary source and exact extent

Held primary: Johan Anthony Willem Kamp, *Tense Logic and the Theory of Linear
Order*, UCLA dissertation, 1968,
`tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf`, SHA256
`C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA`.
The hash was rechecked during this block. The institutional locator is
[the held Stuttgart thesis](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf).

Before authoring, personally read all source scans at printed pp. 95–99
(physical pp. 104–108), and the next transition and definition on printed
p. 100 (physical p. 109). The complete Theorem IV.1 proof ends on p. 99:

| Source component | Printed extent | Authored content |
| --- | --- | --- |
| Theorem IV.1 and setup | 95–96 | Exact real-order target, unary operation alphabet, two-letter interpretation scope |
| Definition 1 | 96 | Discreteness at every real point, both unbounded directions, explicit empty-set convention, DU |
| Lemma 1 | 96–97 | Four-set closure, both complement orientations, every Boolean/S/U constructor, separate empty case |
| Corollary | 97 | Every source-definable unary tense, via one-letter expressive completeness |
| Lemma 2 | 97–98 | Finite field normal form, all four intersection cases, finite-union discreteness and unboundedness |
| Lemma 3 | 98 | Complete finite-formula induction, including arbitrary unary operation and all finite truth functions |
| Final witnesses and contradictions | 98–99 | Even/odd sets, both signs of one half, the complemented second operand, both substitution contradictions |

The governing contract, conventions, C7 plan scope, and research/PDF skill
instructions were personally read. Source scans were read as primary evidence;
actual LaTeX supplied manuscript content and dependencies. No manuscript PDF
was built or rendered.

## Proof and correction details

The nearest earlier/later member of a nonempty discrete unbounded real set is
proved using the real supremum/infimum and the source's gaps at *every* point.
Thus the full constant output for a complemented interval condition follows,
including when the current point belongs to the discrete set. The proof
separates the empty discrete set instead of pretending the four choices are
distinct in that case.

The source's valuation ellipses in Lemmas 1 and 3 are made explicit in the
actual new statements. Every occurring atomic interpretation must be the
single stated proposition for the source case of Lemma 1, and a generator
(or an already generated field member in the proved extension) for Lemma 3.
Unrestricted additional letters cannot be admitted: with even/odd generators,
an extra letter interpreted by `{0}` already violates field closure at the
atomic step. The source theorem's setup on p. 95 expressly restricts its
formula to `q0,q1`; the new statements preserve that intended scope.

The final proof uses `S(q0, not q1)` and `U(q0, not q1)`, as on p. 99, rather
than removing the negation from the second operand. A complete structural
substitution proof takes an alleged binary definition at inputs `(E,H^c)`
back to a formula evaluated at the fixed discrete pair `(E,H)`. It checks
atoms, negation, conjunction and the application of any unary set operation.
The final exact truth sets are
`S(E,H^c) = union_k (2k,2k+1]` and
`U(E,H^c) = union_k [2k-1,2k)`; both endpoint descriptions are proved.

The operation class retains the source's exact positive unary syntax: a
defining formula contains `P0`, has only `t0` free, and has no other predicate
or real parameters. An inessential occurrence of `P0` is permitted and
explicitly explained. The real-order operation need not be given as a
preselected uniform family over other orders; its defining formula is
translated over Com and then restricted to the reals.

The source's symmetric and immediate steps are fully supplied. No source
error is left as a reader repair instruction. The only strengthened results
are identified explicitly: Lemma 1 permits atomic inputs already in its four
choices, Lemma 3 permits extra atoms already in the field, and the worked
example gives the entire two binary truth sets. Each strengthening is proved.

## Reciprocal result and proof links

| Body result | Annex item |
| --- | --- |
| `thm:p09-kamp-iv1-lemma1` | `annex:p9.kamp.iv1.lemma1` |
| `thm:p09-kamp-iv1-unary-corollary` | `annex:p9.kamp.iv1.unary.corollary` |
| `thm:p09-kamp-iv1-lemma2` | `annex:p9.kamp.iv1.lemma2` |
| `thm:p09-kamp-iv1-lemma3` | `annex:p9.kamp.iv1.lemma3` |
| `thm:p09-kamp-iv1` | `annex:p9.kamp.iv1` |

The only external theorem link is `thm:p09-kamp-iii2`. Its statement and
one-letter support argument were reread at the needed extents in the actual
LaTeX; this author's earlier complete reading remains applicable to the
unchanged pair. Body SHA256:
`3B9955A076F3116157212A4B492E7F193C5AA815683B4899BBDC0727472C0470`;
annex SHA256:
`F8D99C95A5620C6C8728D8C13B5C850A384D24EE2AE1BE0F6CB75C3616BDC407`.
The standing definitions and existing IV.1 statement were read from
`n-c-012.tex`, snapshot SHA256
`2734611F8F77D62408E3902B17E97B3077298F09840BE3EE905313A483705FBF`.

## Root integration and notation intake

Root owns all shared routes and records. Add the body input to the Kamp
presentation in `handbook/parts/p09/presentations/n-c-012.tex`, after the
Chapter III/primitive-recursive development and before the later Chapter IV
results. Add the matching annex input after the existing primitive-recursive
input in `handbook/annex/p09.tex`. The existing adjacent-separations paragraph
around `n-c-012.tex:365` can then point to `thm:p09-kamp-iv1`. Bibliography key
`Kamp1968` already exists; no new entry is needed.

New local typed notation, scoped to this section and its annex:

| Notation | Role and first definition |
| --- | --- |
| `\mathcal R` | Usual strict real order, `def:p09-kamp-real-unary-language` |
| `A^c` | Complement relative to the fixed real domain, same definition |
| `\mathfrak M_{\mathcal R}` | All parameter-free source-definable unary real-order operations, same definition |
| `\mathsf{TM}_{\mathcal R}` | Finite sentential language for that alphabet, same definition |
| `\llbracket\eta\rrbracket_V` | Truth set under proposition valuation V, same definition |
| `\operatorname{DU}(A)` | A or its complement is discrete and unbounded in the source sense, `def:p09-kamp-du` |
| `\mathcal F(A)` | Four-choice family, same definition |
| `\mathcal B(A_1,\ldots,A_n)` | Generated finite field of real subsets, `def:p09-kamp-discrete-generated-field` |
| `A_I` | Union of the generators indexed by I, same definition |
| `E,H` | Even and odd integers as real propositions, `thm:p09-kamp-iv1` |
| `d_-,d_+` | Greatest earlier/least later D-point, introduced by supremum/infimum inside `annex:p9.kamp.iv1.lemma1` |
| `N,\mathcal G` | Finite index set and candidate field family, local to `annex:p9.kamp.iv1.lemma2` |

S/U retain their established strict witness-first typed roles. D as a local
discrete proposition in Lemma 1 is distinct from the already established
first-order translation D cited in the following corollary; their local
types and extents are declared in the text. No shared notation file was edited.

## Author checks and next boundary

Read the entire saved body and annex, including the final edits. The existing
`tools/check.py` scanner and bibliography check, scoped to these two files,
reported no grammar/citation findings, no duplicate labels, 17 labels, five
reciprocal result/proof pairs, and only the verified external theorem link
`thm:p09-kamp-iii2`. The checker itself was unchanged, SHA256
`05F22DEE54E3F177EAD79DFAE16D88787E513A58441F443278679F8BC7443914`.
These are author and structural checks, not independent acceptance. No new
tests were written and no review was launched.

No proof obligation inside the assigned real-order Theorem IV.1 remains
unfinished in these files. The next source material is the dense-order
extension observation across pp. 99–100, followed by Definition 2 and Theorem
IV.2 on the integer order beginning p. 100. The complete continuation of IV.2
has not been read or written in this block, and neither that result nor the
following dense-order observation is claimed by this real-order theorem.
