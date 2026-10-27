# Research note: P3 39.3 finite-variable languages and pebble games (packet w03a-p03-056)

Owned files:

- handbook/parts/p03/finite-models-definability-and-descriptive-complexity-w03-p03-056.tex (body, `\chapter`, toc tag `%% toc: P3 39 39.3`)
- handbook/annex/p03/finite-models-definability-and-descriptive-complexity-w03-p03-056.tex (annex)
- handbook/bib/intake-p03-finite-models-definability-and-descriptive-complexity-w03-p03-056.bib
- handbook/registry/symbols-intake-p03-finite-models-definability-and-descriptive-complexity-w03-p03-056.csv

Label tag: `p03-w03-p03-056`.

## Duty

MP-0 (writable part): full L^k grammar (first-order k-variable and infinitary
L^k_{infty omega} with variable reuse), the k-pebble game (placement, reuse,
removal, Duplicator wins iff partial isomorphism after every move), and the
finite-variable equivalence theorem in finite-round and eternal versions with
every proof step written.

The units ED26-SRC-050-0001 and ED26-SRC-050-0002 are readonly here (owner
w03-p03-054). Their components are not written in this packet.

## Sources read in this session

Held:

- source/references/acq-r1-ACQ-2026-10-0472/graedel-2007-fmt-descriptive-complexity-ch3.pdf
  (Graedel, chapter 3, author-hosted 2007-04-25 PDF, running pp. 126-230).
  Read: p. 133 (Lemma 3.1.4, width and renaming of bound variables);
  p. 190 (definition of C^k_{infty omega}, Proposition 3.4.8 statement).
  The chapter has no pebble-game definition and no proof of the
  finite-variable equivalence theorem.
- source/references/acq-r1-ACQ-2026-10-0204/immerman-1999-descriptive-complexity-ch7.pdf:
  chapter 7 (second-order logic, Fagin); not relevant to pebble games.

Online (legitimate, freely accessible):

- Kolaitis, "On the Expressive Power of Logics on Finite Models", manuscript
  dated 1 August 2003, 83 pp., https://dbai.tuwien.ac.at/staff/pichler/dbt/kolaitis.pdf
  (university course page, TU Wien). This is a manuscript version, not the
  version of record (chapter 2 of Graedel et al., Finite Model Theory and Its
  Applications, Springer 2007). Read: pp. 3-4 (vocabularies, structures,
  partial isomorphisms), pp. 52-61 (Sect. 7: Def. 7.1, path formulas and
  three-variable reuse, Thm. 7.2 statement, Def. 7.3, Def. 7.4, Examples
  7.5-7.7, Def. 7.8, Thm. 7.9 with outline proof, Cor. 7.10, Method 7.11,
  Prop. 7.12).
- "Logical Methods in Combinatorics, 236605-2009/10", Technion CS course slides,
  Lecture 4, https://janos.cs.technion.ac.il/COURSES/236605-09/lec04.pdf
  (pp. 10, 11, 13: games PG^n_k and PG^infty_k, pebbles moved without removal
  moves, Theorem 2 finite-round and infinite versions stated, proof deferred),
  and Lecture 5, https://janos.cs.technion.ac.il/COURSES/236605-09/lec05.pdf
  (p. 2: Theorem 1 restated). No author is named on the slides.
- arXiv:math/9411235v1 (Gurevich, Immerman, Shelah, McColm's conjecture),
  read p. 2 description of the k-pebble game; not cited.

## Provenance decisions

- The finite-round theorem is stated in the Technion slides without proof; the
  eternal theorem is stated with an outline proof by Kolaitis (Thm. 7.9, which
  attributes it to Barwise 1977 and Immerman 1982). The annex proofs are
  written in full here; they are not transcriptions of either source.
- Positions are pairs of partial assignments on a common label set D, so two
  labels may sit on the same element. This handles variable reuse uniformly
  and avoids the distinctness side conditions in Kolaitis's outline.
- The game definition allows re-placement of a pebble in use (as in the
  slides) and removal moves (as in Kolaitis). The eternal theorem proves the
  three variants (both moves; slides' no-removal; Kolaitis's unused-pebble
  placement plus removal) have the same winner. The finite-round theorem
  proves the variants with and without removal moves agree.
- Kolaitis's vocabularies (finite: relation and constant symbols) are kept,
  so constants enter the win condition.
- Quantifier rank for infinitary formulas uses suprema; this extension is
  editorial and is said so in the text.
- Limitation example (N with successor versus N disjoint-union Z) is
  editorial, with full proof; it shows the finiteness hypothesis in the
  FO^k clause cannot be dropped.
- Barwise 1977 and Immerman 1982 were not read; they are mentioned only as
  Kolaitis's attribution, cited to Kolaitis's page.

## Existing treatments found (A9)

- handbook/parts/p09/presentations/n-c-002.tex 101-111: names L^omega and
  Libkin Thm 12.2 (linked from the relationships section).
- handbook/parts/p02/definitions-interpolation-and-decidable-fragments-w02-p02-035.tex:
  def:p02-w02-p02-035-fo2 (FO^2 sentences; linked).
- handbook/parts/p03/qe-categoricity-games-supplement.tex: def:p03-ef-game,
  thm:p03-ef (EF game, cited); linked and bridged by a proved lemma.
- handbook/parts/p03/qe-categoricity-games.tex: def:p03-finite-partial-isomorphism (linked).
- handbook/parts/p03/comparison-games-and-infinitary-languages-w03-p03-039.tex:
  def:p03-w03-p03-039-language (L_{infty,omega}) and thm:p03-w03-p03-039-karp
  (linked). These were not listed in the packet's "existing" list.

## Continuation

Block 1 state (2026-10-11):

- MP-0 writable part written: body chapter (565 lines) and annex (718 lines).
  Grammar and semantics (def -grammar, -semantics, -equivalence), lemmas
  -coincidence, -renaming, -walks, -finitely-many, -atomic; game definition
  with placement/reuse/removal and the two source variants; theorems
  -finite-round and -eternal with full annex proofs; examples -cliques,
  -even, -orders; limitation -successor (proved) and warning -limits;
  relationship lemma -ef-bridge (proved).
- unit-compile ok (8 minor overfull boxes, all in environment titles);
  check.py shows only bib-key findings for the four intake keys.
- Components of ED26-SRC-050-0001/0002 are readonly (owner w03-p03-054);
  not written here.
- Open: Barwise 1977 and Immerman 1982 not read (attribution via Kolaitis
  p. 58 only). Completeness half of Kolaitis Method 7.11 quoted, not proved.

Block 1, second pass (2026-10-12):

- Assessment said MP-0 material is not on the handbook route. The material
  is in the owned files; the route gap is the missing driver inputs.
  Patch request work/waves/w03a/patches/w03a-p03-056.json: inputs in
  handbook/parts/p03.tex and handbook/annex/p03.tex (packet insertion
  proposal) and a cross-reference sentence in the readonly host
  handbook/parts/p09/presentations/n-c-002.tex after the "finite-pebble
  strategy" sentence (route lines 101-111).
- Added, with annex proofs: thm:p03-w03-p03-056-monotone (Kolaitis p. 56
  remarks: monotonicity in k, equivalence relation), thm:p03-w03-p03-056-definability
  (Kolaitis Cor. 7.10, p. 59; both directions, plus completeness of
  Method 7.11 on finite classes; disjunction over the set of complete FO^k
  theories instead of iso-type representatives), thm:p03-w03-p03-056-clique-query
  (Kolaitis Prop. 7.12 second item, p. 60). The earlier open item
  "completeness half of Method 7.11 quoted, not proved" is now closed.
- Locators re-verified this session against the saved page images/text of
  the Kolaitis manuscript (pp. 52-60), Technion Lecture 4 (pp. 10, 11, 13)
  and Lecture 5 (p. 2), and the held Graedel PDF (running pp. 133, 190).
- unit-compile ok; check.py shows only bib-key findings for the four intake keys;
  find_fused_spaces clean.
- Still open: Barwise 1977 and Immerman 1982 not read (attribution via Kolaitis
  p. 58 only).

## Author proof audit and correction, 2026-10-26

The warning after the monotonicity result incorrectly denied the equivalence
between failure of a Duplicator strategy and a Spoiler strategy forcing a
finite loss on every play. The actual distinction is a uniform bound on the
number of rounds. The warning now states this, and the annex derives the
Spoiler strategy directly from a distinguishing infinitary formula. Boolean
choices and quantifier witnesses maintain opposite truth values; each step
descends through its well-founded syntax, so each play reaches atomic
disagreement, although the finite length may depend on the responses.

The finite-rank and finite-vocabulary hypotheses and the successor example
were also reread. This bounded author audit does not claim a fresh reading
of the original Barwise or Immerman sources cited through Kolaitis. The
scoped four-pass TeX Live build succeeded: 31 pages, seven overfull warnings,
and three external references unresolved because this is an isolated unit.

These are author corrections and bounded verification, not independent
review, source admission, complete-source coverage, or book completion.
