# P3 chapter 32: Stability and the forking calculus (packet w03a-p03-031)

## Provenance

- Body: handbook/parts/p03/stability-and-the-forking-calculus-w03-p03-031.tex (lines 1-776).
- Annex: handbook/annex/p03/stability-and-the-forking-calculus-w03-p03-031.tex (lines 1-1005).
- label_tag p03-w03-p03-031; toc_tag `%% toc: P3 32 32.1,32.2,32.3,32.4`.
- Existing treatment extended, not duplicated: handbook/parts/p03/classification-theory.tex
  sec:p03-stability (def:p03-stability, def:p03-dividing-forking, def:p03-simple-theory,
  def:p03-stability-spectrum, thm:p03-nonforking-calculus). The new chapter cross-references
  these definitions and proves the laws thm:p03-nonforking-calculus states, under simplicity.
- Further existing material used: thm:p06-erdos-rado, thm:p06-infinite-ramsey (P6, cited
  theorems), thm:saturated-extension (restoration/inherited-06640-06693.tex, cited),
  thm:p03-w03-p03-006-elementary-amalgamation (proved), thm:p03-w03-p03-015-graph-types
  (proved, random graph patterns/QE).
- Note: def:p03-saturation and thm:p03-saturated-extension live in parts/p03/types-ultraproducts.tex,
  which is not in the active driver; the active saturation definition (unlabelled) and
  thm:saturated-extension are in restoration/inherited-06640-06693.tex. Not listed in the packet's
  existing list.

## Sources read online this session

- Casanovas, "Simplicity simplified", Revista Colombiana de Matematicas 41 (2007) 263-277,
  published version, EMIS mirror https://emis.dsd.sztaki.hu/journals/RCM/Articulos/828.pdf,
  read in full (pp. 263-277). Locators used: Lemma 1.1 p. 264; Defs 3.1-3.3 p. 266;
  Remark 3.3, Lemma 3.1, Props 3.4, 3.5 p. 267; Section 4 opening p. 268; Cor 4.1, Def 5.1 p. 271;
  Def 5.2, Remark 5.2, Lemma 5.1, Props 5.3, 5.4 p. 272; Props 5.5, 5.6 p. 273.
- Shelah's archive page https://shelah.logic.at/papers/a/ : states no downloadable version of Sh:a.
- Tent-Ziegler 2012: no free copy found (web search, CUP pages only).

## Held sources read this session (block 2)

- Morley 1965, Categoricity in Power, Trans. AMS 114 (1965) 514-538, held PDF
  source/references/p03-morley1965/morley1965-categoricity-in-power.pdf (and its extracted text).
  Read pp. 514-522. Locators used: Section 2 standing convention (complete theory, countable language,
  infinite model) p. 518; Definition 2.2 p. 520; Theorems 2.7 and 2.8 p. 522 (page image checked).
  Introduction p. 514 (Cantor-Bendixson analogue) read, not cited.

## Deviations from the source, recorded

- Casanovas Lemma 1.1 (input length (2^lambda)^+, proof referred to Kim's thesis) is replaced
  by thm:p03-w03-p03-031-extraction with input length beth_{(2^lambda)^+}(lambda), proved from
  Erdos-Rado; applications only need some small length.
- Simplicity is the handbook's local-character definition (def:p03-simple-theory), which
  Casanovas explicitly allows (p. 268), so his Section 4 (tree property, D-rank) is not needed.
- No homogeneity of the ambient model is assumed; conjugation is done by realizing copied
  types (thm:p03-w03-p03-031-saturation (2)).
- Parameter-presentation independence (saturation lemma item 4) and the "adding base
  parameters" step in symmetry are made explicit; Casanovas leaves them tacit.
- Prop 3.4 (left by Casanovas as an easy application) and Prop 5.6 are written out in full.
- The random graph forking characterization is my own derivation from the handbook's graph
  pattern theorem; it gives a direct proof that T_RG is simple and unstable.

## Continuation

Block 0 (earlier): GOAL-02 laws invariance, monotonicity (left, right, base), finite character,
extension (any T), existence and extension from the domain (simple), local character (simple,
definitional), forking = dividing, Kim's lemma, symmetry, transitivity (both forms), all with
annex proofs; random graph example, base-monotonicity failure warning, law/hypothesis table.

Block 1 (this block): the open item "stable implies local character of nonforking" is closed by
linking, not re-proving. The handbook already contains a full annex proof that stable theories
are simple: thm:p03-w03-p03-035-stable-simple (packet w03-p03-035, chapter 34, annex
annex:p03-w03-p03-035-stable-simple, via the local dividing rank def:p03-w03-p03-035-drank,
thm:p03-w03-p03-035-drank-calculus and thm:p03-w03-p03-035-tree-order). Checked: that proof uses
from this chapter only def:p03-w03-p03-031-monster and thm:p03-w03-p03-031-saturation (3), (4),
so no circularity. Added thm:p03-w03-p03-031-stable-calculus (body lines 392-431) stating all
seven laws under the stable hypothesis with base conditions (local character with |A_0| <= |T|,
finite when superstable; invariance; monotonicity; existence/extension; symmetry; transitivity;
forking = dividing), with annex proof annex:p03-w03-p03-031-stable (annex lines 632-676).
Rewrote the classes paragraph (body 33-51) that had said the inclusion was not proved; the
omega-stable -> stable step is linked to thm:p03-w03-p03-032-spectrum (2)=>(1). Table row for
local character and the Relationships paragraph updated.

The independent assessment of block 0 read only classification-theory.tex (this chapter is not
yet in the driver), which is why it reported invariance, monotonicity and simple-theory
extension/symmetry/transitivity as absent; they are in this chapter at
thm:p03-w03-p03-031-basic-calculus, thm:p03-w03-p03-031-simple-extension,
thm:p03-w03-p03-031-symmetry, thm:p03-w03-p03-031-transitivity.

Remaining dependency for the lead: the chapter must be inserted into the drivers (insertion
proposal in the packet) and chapter 34 (w03-p03-035) must be in the same build for the
\cref to thm:p03-w03-p03-035-stable-simple to resolve.

N-a-007 units: Shelah 1978 (Sh:a), Pillay 1996 and Tent-Ziegler 2012 are neither held nor
freely available; their source-specific presentations are not written.

Block 2: closed the two gaps named by the assessment of block 1.
- N-a-007-MAP-05 (omega-stable => superstable): new section 32.2 "Counting types and the stability
  spectrum" (body 138-343). def:p03-w03-p03-031-cb-rank (ordinary Cantor-Bendixson derivative of
  S_m(A) over one set), lemma thm:p03-w03-p03-031-cb (annex:p03-w03-p03-031-cb, annex 18-145:
  stabilization, isolating formula, countable => no rank-infinity types via a binary splitting tree,
  greatest rank under a formula attained by finitely many types), theorem
  thm:p03-w03-p03-031-omega-superstable (annex:p03-w03-p03-031-omega-ss, annex 147-234). Proof for a
  language of ANY cardinality: omega-stable => stable (032 spectrum (2)=>(1)); countable sets have
  countably many m-types (032 one-to-many, lambda = aleph_0); infinite degree gives a countable
  k-inconsistent tree (032 degree-tree, lambda = aleph_0) along which the greatest CB rank strictly
  drops, contradiction; so Deg finite; 032-superstable (3)=>(4) gives superstability in the sense of
  def:p03-stability-spectrum. Second proof for countable languages via Morley Theorems 2.7/2.8
  (thm:p03-morley-countability, already proved in the n-a-006-01 presentation) and 032-superstable
  (1)=>(4), recorded in the same annex item and in body text with Morley locators.
  Worked example def:p03-w03-p03-031-cb-example (pure set); limitation (T_P) in body text.
- N-a-007-MAP-06: spectrum lookup table tab:p03-w03-p03-031-spectrum (body ~281-337) with rows for
  lambda-stable, stable, unstable, lambda^{|T|}>lambda, Shelah cardinal superstability, superstable,
  omega-stable, simple. Paragraph "Simple theories: what is proved here and what is proved
  separately" (body ~734-776) names the results requiring chapter 34 (sec:p03-w03-p03-035-chapter):
  stable => simple and local character of dividing; SOP/NIP/IP placement (sop-not-simple,
  simple-nip-stable, random-graph, dlo); tree property => order property; and states that the
  tree-property equivalence and stationarity/definability/independence theorem are proved in neither.
- Classes paragraph (body 39-68) rewritten: all four inclusions omega-stable < superstable < stable
  < simple now point to proved results, with T_P, T_E, T_RG as strictness witnesses.
- Restructure to match the toc (32.1-32.4): section 2 is the new spectrum section; the former
  "Indiscernibles and dividing" section is now subsection 32.3.1, and the laws are subsection
  32.3.2 (new label sec:p03-w03-p03-031-laws); no external references to the moved labels existed.
- Not re-checked: whether thm:p03-morley-countability's body file (parts/p03/presentations/n-a-006-01.tex)
  is on the body driver; its annex is. The lead must ensure the label resolves in the full build.


## Author correction, 26 October 2026

Repaired a gap between the statement and proof of nondividing and
indiscernible sequences: the statement allowed arbitrary small tuples and
infinite index orders, while the proof began by assuming a finite parameter
tuple and an omega-indexed sequence. The revised finite-satisfiability
argument works on finitely many coordinates and indices, uses finite Ramsey
thinning, and copies those finite configurations. It establishes the original
broader statement without shrinking it.

The parameter-padding proof now handles infinite small padding directly by
compactness and Ramsey thinning, rather than applying a finite-tuple extraction
lemma to an unrestricted tuple. The ambient convention explicitly chooses a
sufficient saturation level for each application; it does not require a single
cardinal to be closed under every beth bound below itself. The spectrum table
now records all directions actually proved in packet 032's superstability
theorem and its type bound. These are author corrections, not independent
admission or a claim to have closed the unavailable exact-source obligations.
