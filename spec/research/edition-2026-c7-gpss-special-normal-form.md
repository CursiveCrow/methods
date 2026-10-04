# C7 author handoff: GPSS special normal form and positive decompositions

Date: 8 September 2026. Assignment `/root/kamp_lemma7_author`, begun
12:22 UTC. The assigned normal-form and positive construction stages are
fully written. Proposition 2.4 remains an explicit mathematical/source
boundary. Independent reviews remain deferred.

## Files and exact primary

| File | Lines | Bytes | SHA256 |
| --- | ---: | ---: | --- |
| `handbook/parts/p09/presentations/gpss-special-normal-form.tex` | 303 | 14998 | `FC8A0651DB37E774DF630821F9AF07AB9C9C545A6A0DAEBC9089E9A0AD341F72` |
| `handbook/annex/p09/gpss-special-normal-form.tex` | 643 | 27510 | `C722ACBC9C74C6CB26DB66EB77EF624D40E06D77C35309D5E69D120FBAF7707B` |

All three owned paths were unused at dispatch. Only these two new files and
this note were written. Root's shared files and other author work were preserved.

Primary: Dov Gabbay, Amir Pnueli, Saharon Shelah and Jonathan Stavi,
*On the Temporal Analysis of Fairness*, POPL 1980, printed pp. 163–173.
Held PDF: `tmp/pdfs/p09-gpss-1980/gabbay-pnueli-shelah-stavi-1980.pdf`;
SHA256 rechecked: `2C8FF0E169D2D37B2B402907741AB8FCD67C2883395A4C1655775AB3723A4DA2`.
The exact author-archive copy is [Sh:134](https://shelah.logic.at/files/95957/134.pdf),
identified by the [author's archive record](https://shelah.logic.at/papers/134/).

Personally read the source model and strict operator clauses on printed p. 164,
the entire expressive-completeness passage on pp. 169–171, and the exact
external references on p. 173. PDF page = printed page minus 162. The
higher-resolution quantifier crop on p. 170 was personally inspected:
the source future quantifiers are inclusive, `y >= x`. The actual definitions
and relevant proof-boundary paragraphs of `n-c-012.tex` were read. The existing
source note was consulted for the held object and source-local referral map;
its historical inspection claims were not substituted for this source reading.

Research/PDF skills supplied primary reading and this research note. There
was no manuscript render, new test, independent review, or review wait.

## Complete authored results

| Result | Reciprocal annex |
| --- | --- |
| `thm:p09-gpss-kamp-normal-form-bridge` | `annex:p9.gpss.kamp.normal.form.bridge` |
| `thm:p09-gpss-special-normal-form` | `annex:p9.gpss.special.normal.form` |
| `thm:p09-gpss-future-special-form` | `annex:p9.gpss.future.special.form` |
| `thm:p09-gpss-future-label-closure` | `annex:p9.gpss.future.label.closure` |
| `thm:p09-gpss-positive-decomposition` | `annex:p9.gpss.positive.decomposition` |
| `thm:p09-gpss-suffix-translation` | `annex:p9.gpss.suffix.translation` |

The staged proof retains the exact GPSS grammar: At contains signed unary
literals; Bet_0 is empty; the next stage consists of signed guarded
existentials whose finite child list may be empty. Stage inclusion is proved
from this grammar, rather than added as an unprinted clause. Before/after
regions use omitted formal-endpoint guards. A whole-order extension with
both formal endpoints supplies the zero-free-variable sentence case explicitly.

The Kamp bridge reads the actual earlier starred point/regional grammar and
maps it by finite constructor translations. GPSS signed existentials become
Kamp existential/universal components, inserting starred truth/falsehood for
empty lists. Conversely Kamp components become finite GPSS component DNFs;
point conjunctions flatten to literal lists. Equality is replaced by the
strict-order coincidence formula. Constants introduce no new unary predicate.
This is an explicit semantic bridge, not an identification of the syntax or
an import of arbitrary Kamp elementary labels.

The direct GPSS normal-form proof includes all weak order types, both
equality-block eliminations, singleton quantified points in both rays and
every gap, universal quantification through fully constructed complements,
missing positions, empty regions, empty Boolean folds, and sentences.
It preserves unary support. The future specialization works in the induced
tail at and after x, evaluates its empty before region by sign, and returns
only At(x) and Aft(x) components in the original model.

The decomposition class keeps only actual L(U)-translated unary labels,
with no extra individual parameter. Their whole-model future semantics and
capture-free copying are explicit. All finite conjunctions preserve that
class. General past-dependent one-point formulas do not: the proved
counterexample at zero compares Q0 = {-1} with the empty interpretation.

Positive closure enumerates every weak interleaving of two finite witness
chains using steps (1,0), (0,1), (1,1), including coincident witnesses. It
transfers covering gap labels onto inserted points as well as new gaps.
Concatenation inserts the quantified point with its admissible point label.
The proof covers both rays, whole-order formal endpoints, empty child lists,
empty disjunctions, adjacency, and both signs of every stage-one component.
The worked three-point examples verify why fusion and transferred point
labels cannot be omitted.

The complete suffix translation uses nested strict until plus the last
gap's strict G condition. Each global cofinal clause translates as
`F psi AND G F psi`, not G F psi alone. Its nonempty first factor is needed
at a last point, where strict G would otherwise be vacuous. The proof gives
both directions over the whole domain. Every result in this block is proved
on arbitrary nonempty strict linear orders; no unproved negation closure is
used to claim a later completeness theorem.

## Precise next obligation

For the future-completeness route, the next required complement instances are
bounded intervals with an actual lower endpoint and suffixes `(x,+infinity)`.
For finite endpoints the target is `x < y AND NOT delta(x,y)`. An unguarded
complement cannot be a disjunction of guarded decompositions at x = y.
The full first-order normal form also retains before regions; the proved
positive operations on prefix-shaped decompositions do not assert that every
past-dependent component can be replaced by a future-only label.

The event-expression proof still needs all of the following actual mathematics:

1. A finite syntax and semantics for the first/last occurrence operations used
   by the source, including missing occurrences and unbounded/no-last cases.
2. A construction of the finite event list associated with each input
   decomposition, with every label still in the stated future class.
3. A proof that the list's values, undefined statuses and relative order
   determine the decomposition's truth.
4. A complete finite, mutually exclusive and exhaustive classification of
   those statuses and orders.
5. A translation of every relevant class back to a finite disjunction of
   the exact GPSS decompositions, retaining endpoint guards and cofinal
   conditions and avoiding past-dependent point labels.
6. The resulting relative complement construction, then the full induction
   on Bet_n and the claimed discrete-complete future theorem.

Finite enumeration of possible orders alone proves none of items 1–5.
The block does not count Proposition 2.4, the unrestricted Main Lemma,
Theorem 2.2, the separate separation Theorem 2.3, or the gap theorem as
completed. The staged/positive results provide the exact prerequisites.

## Bounded search for the missing primary proofs

The paper's [SS] is Shelah and Stavi, *Expressive Completeness for Temporal
Logic*, listed as forthcoming; [G2] is Gabbay, *The Separation Property of
Tense Logics*, manuscript, September 1979. Exact-title and author searches
were performed, including the author archive and publisher records. No
free full body of either exact referred manuscript was located or acquired
in this block. This is a search outcome, not a claim that no copy exists.

The [Shelah–Stavi coauthor index](https://shelah.logic.at/coauthors/jonathan_stavi/)
lists Sh:47, Sh:121, Sh:134 and Sh:144; it did not supply the separately named
[SS] manuscript. Sh:134 is the held GPSS paper, not the missing full proof.

A concrete later primary lead is Gabbay's
[1981 *Expressive Functional Completeness in Tense Logic*](https://link.springer.com/chapter/10.1007/978-94-009-8384-7_4),
pp. 91–117, DOI 10.1007/978-94-009-8384-7_4. Its publisher reference list
identifies a 1979 separation paper as Part 2 of that chapter. The accessible
page expressly presents subscription content and a preview PDF; a free
complete chapter was not verified. The later chapter has not been silently
identified with GPSS's manuscript or used as mathematical proof evidence.

Hodkinson's [author publication page](https://www.doc.ic.ac.uk/~imh/frames_website/hdim.html)
identifies a 1995 games proof of Kamp's theorem based on GPSS and a separate
1993 Gabbay–Hodkinson–Reynolds proof for gaps. The author-hosted
[2005 Hodkinson–Reynolds separation survey](https://www.doc.ic.ac.uk/~imh/papers/sep.pdf)
is freely accessible and points to later Gabbay proofs. These are distinct
later presentations. They were located as acquisition leads, not substituted
for the exact [SS]/[G2] bodies or for the missing GPSS event-expression proof.

## Root integration and source corrections

The new body belongs in the GPSS expressiveness presentation near the
current normal-form/decomposition passage; add its matching annex input.
Keep the later negation boundary explicit while updating the paragraph
headed `What the proof outline actually contains` so it links the now-written
Lemma 1, bridge and positive results. The current paragraph around line 1628
should not continue to imply that the handbook has no normal-form induction.

The comparison is with Kamp's actual Chapter III normal-form theorem, supplied
by `thm:p09-kamp-iii1`, rather than silently treating GPSS's printed Chapter II
referral as that proof. The old unqualified negation sentence near line 1660
needs its admissible-interval guard. The original source-model paragraph also
still displays the backward inequality in the reader-facing F clause; root
should write the coherent strict-future clause there and retain the historical
reading in the existing source note. The new label formulas use strict future
throughout, with the GPSS infix operand order.

The compared `n-c-012.tex` snapshot hash is
`9BEAD1D2370649EB62DF4C2AA1A830C18DF4F6CF57F79301F0F08919DA3C8DA2`.
The exact Kamp dependency was read in the actual LaTeX: body SHA256
`0D1EB5FC960B7F0F1EB216026AF2AAF953CD3D95F62E4ACF014345611D860B31`;
annex SHA256 `A46BFF4D11C868E8A865F2F9CC89690FCB4D03A550EB6CCB755B4C067A3B7F8B`.
Existing bibliography keys `Kamp1968` and `GabbayPnueliShelahStavi1980` suffice.

Local notation intake: At_G, Bet_(G,n), Bef_(G,n), Aft_(G,n), g_ab and the
whole-order endpoint convention in `def:p09-gpss-regional-stages`; weak
partition blocks B_j, representatives y_j and prefix pi in
`def:p09-gpss-special-form`; future-label translation star and strict U_s,
F/G in `def:p09-gpss-future-labels`; decomposition delta, actual interior
points z_i, point/gap labels theta_i/phi_i and global Inf in
`def:p09-gpss-decomposition`; suffix histories H_i in
`thm:p09-gpss-suffix-translation`; D_p in the worked merge example. The
source's original names are retained with G added to distinguish their
different syntactic types from the Kamp classes. No shared symbol file or
macro was edited.

## Author checks

Read the entire saved body and annex, including the worked examples and
final scope clarifications. Existing scanner/bibliography checks reported
zero findings, 20 owned labels and six owned proof pairs. Joined reference
and reciprocal-proof checks with the exact Kamp dependency also reported
zero findings. The two external references are
`def:p09-kamp-iii1-components` and `thm:p09-kamp-iii1`.
These checks do not grant independent acceptance. The exact next writing
boundary is the negation/event-expression construction described above.
