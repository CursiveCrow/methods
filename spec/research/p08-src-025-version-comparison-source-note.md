# SRC-025 source-version qualification and comparison

Assignment: qualify the public Areces chapter candidate for the separately
catalogued published Blackburn--van Benthem chapter ED26-SRC-025-001 (2007,
printed pp1--84), and compare it with the exact institutional PP-2006-30
manuscript ED26-SRC-025-501. Acquisition and comparison are not source-specific
authoring, independent review, admission or shared catalog edits.

## Verified captures and current qualification

1. Original institutional manuscript: `tmp/src025/illc-chapter1.pdf`,
   587,542 bytes, 82 physical/printed pages, SHA-256
   `268f88669c8a609377d3aec348ca642a29d201ada542a10b6e9ccaae55461e35`.
   Actual first-page footer has the 2006 Elsevier manuscript notice and an
   unfinished editor line. The institutional record is PP-2006-30; the current
   source author's note records its MODS date 2006-04-27.
   References end on printed/physicalp79, physicalp80 is blank, and the
   standalone index occupies printed/physicalpp81--82. This blank page is
   retained in the exact82-page identity rather than silently removed.
2. Public candidate:
   <https://carlosareces.github.io/rio24/downloads/hb.pdf>, ordinary HTTPS
   response 200, application/pdf. Captured unchanged as
   `source/references/modal-src-025-publisher-comparison/areces-rio24-handbook-of-modal-logic.pdf`.
   641,367 bytes, **87** physical pages, SHA-256
   `f44e9415ee1a6085ff7064b8d416d850fe9d30486066579a3cf524e92a684f06`.
   It is a standalone chapter, not the full handbook. Title/author page is
   physical/printed p1. Section8 starts p79; references end p84; a standalone
   index follows on pp85--87. Metadata creation date is 2006-07-24 16:43:00.
   Metadata date alone does not establish publication version.
3. Fallback <https://carlosareces.github.io/ml18/downloads/hb.pdf> returns
   exactly the same 641,367 bytes/hash. Separate provenance capture is
   `areces-ml18-hb.pdf` in the owned source directory. There is no second
   source version merely because the hosting course directory differs.
4. Editor-hosted <https://cgi.csc.liv.ac.uk/~frank/MLHandbook/1.pdf> is only a
   **three-page introduction/contents** PDF, 36,778 bytes, SHA-256
   `a74ae1f9fee08025803cc4b80f5dac1f1a8f253f1c1a5d801796f772283e0650`.
   It is captured as `wolter-editor-chapter1.pdf`; it does not supply the
   full selected published chapter.
5. One additional normal public academic lead,
   <https://ai.stanford.edu/~epacuit/classes/lori-spr09/hml.pdf>, is also a
   standalone **87-page** chapter, not the full handbook or a qualified84-page
   publisher copy. Captured as `pacuit-stanford-hml.pdf`, 638,571 bytes,
   SHA-256 `7fa21e69769e75a20cdc25c261bf9b68ed5dc3d3a16b3201c7ff5b076dce9b62`.
   Its metadata creation date is 2006-05-09 17:56:00. It differs from the
   Areces July-metadata version in actual contents-page locators and wording
   (e.g. standard-translation start p9 vs p10; introduction still points to
   Section8 for alternative semantics). It is a third manifestation, not
   another filename for either exact82-page original or exact Areces bytes.

The 87-page candidate is a genuine more-developed standalone manifestation
of the same chapter, with substantive revisions, but **is not yet qualified
as the exact 2007 printed pp1--84 publisher body**. Dropping its three index
pages would manufacture an 84-page derivative, not prove publisher identity.
The original82-page identity remains separate and unchanged.

## Publication evidence and bounded unsuccessful routes

- The author's institutional [Roskilde publication record](https://forskning.ruc.dk/en/publications/modal-logic-a-semantic-perspective/)
  explicitly identifies 2007, pp1--84, ISBN9780444516909 and
  DOI10.1016/S1570-2464(07)80004-8. This is identity metadata, not the missing body.
- The [Elsevier book record](https://shop.elsevier.com/books/handbook-of-modal-logic/blackburn/978-0-444-51690-9)
  names the editors and chapter, but gives book release November3,2006.
  Book release and chapter copyright/citation year are distinct evidence.
- Ordinary publisher chapter access at
  `https://www.sciencedirect.com/science/article/pii/S1570246407800048`
  returned403 through the available web reader. No bypass was attempted.
- A Charles University repository lead explicitly says its full-book PDF
  requires university authentication for students with special needs:
  <https://dspace.cuni.cz/handle/20.500.11956/179850?locale-attribute=en>.
  It was not downloaded or accessed through a different interface.

## Actual comparison method and standing

All pages of the original82 and Areces87 PDFs were extracted with pypdf into
`original82-extracted.txt` and `candidate87-extracted.txt` inside the owned
capture directory. These are labelled mechanical derivatives, not source
identities or reader-facing manuscript content. A word-alignment pass with
Unicode compatibility normalization, running-head removal and citation-number
normalization was used only to locate changed passages. It cannot establish
mathematical equality, picture equality or publisher-version identity.

The comparison read the actual changed passages and the full source passages
containing the writer's priority items. Primary-page images were inspected
for originalpp6,9,34 and candidatepp1,6,9,26,27,29,35,36,42,43,87. These include
the changed acceptance proposition, game captions, exact filtration clause,
TMEQ formula, identity correspondence, Id/Un prose and cyclic-return formulas.
Poppler warned about substitute display fonts, but the material symbols and
caption locations in these inspected pages were visible and agreed with the
corresponding source text. The captures are not a repaired or republished PDF.

This is a bounded concrete comparison of the identified82/87 manifestations,
not an exhaustive page-by-page adjudication of every comma, diagram or proof,
and not a full2007 comparison: that selected published body has not been
qualified. No equivalence of versions follows from a shared title or similar
extracted text.

## Priority mathematical and figure comparison

Physical page numbers equal the displayed Arabic page numbers in both
standalone PDFs. The following are actual observations, with mathematical
implications separately stated where needed.

| Item | Exact82-page source | Areces87-page source | Version consequence |
| --- | --- | --- | --- |
| Process/automaton endpoint, Fig2 | p6: modal word ends in top | p6: it ends in proposition t, explicitly interpreted only at the terminal state | A genuine semantics-sensitive revision distinguishing path existence from endpoint acceptance; source figure graph itself is unchanged |
| Game Fig6 | p9: winning captions occur at 2p and 1p; none at 4p | p9: the same three terminal labels and the same two winning captions | No printed false winning caption at4p in either source. The source writer checked and corrected its working provenance note after receiving this pixel evidence |
| Modal Until, section4.1 | p25: displayed endpoint plus all interval-u condition; R is described as irrefl.existing accessibility relation | p26: same displayed condition, but preceding/following text explicitly discusses trees of computational runs and an immediate-successor relation | The semantic display is not replaced by an arbitrary-graph existential-path clause. The new tree context is real and must be retained; it is not license to assert interval/path equivalence on every graph |
| Until worklist figure | Fig15,p26 | Fig16,p27 | Variables v/w are consistently interchanged and a missing closing brace is repaired; the predecessor-propagation procedure is materially the same. A new diamond-checking procedure now occupies Fig15,p25 |
| Filtration, Definition19 | p28 clauses1--4; its upper constraint quantifies diamond formulas only | p29 same diamond-only constraint and same truth theorem | No added primitive-box condition or dual-negation closure appears in this revision. A source-specific corrected primitive-box treatment still needs its actual closure hypothesis; citation to this revision does not remove that dependency |
| Makinson, Theorem25 | p33 states containment for every normal modal logic | p34 explicitly adds consistency | A substantive repaired hypothesis; candidate also adds a later purported semantic sketch,p37. This acquisition/comparison does not validate that sketch |
| Id/Un frame assignment | p33: prose assigns Un to isolated reflexive frames and Id to isolated irreflexive frames | p35: same assignment | This reversal is not corrected here, despite the source's preceding Id/Un definitions. Do not credit the revised manifestation with a repair it does not contain |
| TMEQ, Theorem26 E schema | p34: antecedent contains box-psi; consequent ends with box-phi | p35: same formula | The independent-variable mismatch is retained. The cited1978 paper is renumbered117 to129, not replaced by a new proof; this comparison does not establish the cited theorem under the printed schema |
| Identity correspondence, Proposition27(3) | p34 actually prints `forall x,y [Rxx and (Rxy and Ryx implies x=y)]` | p36 prints `forall x,y [Rxy iff x=y]` | A genuine mathematical correction, visually confirmed. The original condition is reflexivity plus antisymmetry, not merely a one-way identity implication. A reflexive strict two-point chain meets that original condition but is not an identity frame |
| Cyclic-return correspondence, section5.5 | p41 gives its verbal reach-back condition | pp42--43 additionally gives a least-fixed-point definition of transitive closure and `forall x,y [Rxy implies R+yx]` | A real new formula/quantifier specification; original and revised source scopes are not interchangeable by a page-offset rule |
| K4.1/ultrapower citations | p39: van Benthem125/119 | p41: van Benthem137/131 | Actual cited works remain Correspondence Theory2001 and Modal Logic and Classical Logic1983; only source bibliography numbers change |

## Other substantive additions and changed conventions

The actual changed source passages also establish the following differences;
the claims are records of what this version adds, not independent theorem
acceptance or completion of their cited dependencies.

- At basic-syntax introduction,p3, the87-page version explicitly assumes PROP
  denumerably infinite; the originalpp3--4 setup did not fix that cardinal.
  Its p4 polarity convention now expands implication and bottom when counting
  negations. That is new setup, not merely a typography adjustment.
- Its p10 K aside explicitly restricts the illustration to a one-modality
  language with diamond defined by box, and explains propositional substitution
  instances, unlike the shorter original axiom list.
- It clarifies the maximal autobisimulation quotient,p14, and supplies the
  intended valuations and finite-vs-infinite branch comparison for Fig14,p20.
- It adds diamond-checking pseudocode at Fig15,p25, an explanation of the
  three factors in the model-checking bound, and a computational comparison
  table at Fig17,p33 (absent from the original).
- The GL finite-tree completeness account,p34, now explicitly interprets the
  modal relation by the transitive closure of the one-step tree relation.
- Section5.6,pp43--45, adds a tree/grid/Rabin/tiling discussion and Fig18, and
  adds a Sigma-one-one completeness claim for global frame consequence. The
  originalp42 only asserted non-enumerability at that point. The added claim
  is not silently imported as a proved original statement.
- Section6.2,pp51--52, adds a substantial downarrow-binder discussion, with
  irreflexivity, distinct-successor and grid-square formulas, an undecidability
  discussion and the bounded-fragment/generated-submodel connection. The
  originalp48 goes straight from basic hybrid satisfiability to further reading.
- Section6.3,p53, adds a simple unrestricted Until countermodel as Fig19;
  the original transitive countermodel Fig16,p49 becomes Fig20,p54. New Fig21,
  p58, compares the first-order fragments; the original had no such diagram.
- The packed-fragment guard description changes materially (originalp53,
  candidatep57): the original list explicitly allowed universally quantified
  relational guards; the revised list instead states equality, atomic
  relational and existentially quantified relational guards and gives its
  packed-quantification construction. Do not collapse these syntactic versions.
- PDL,p60, gains a compactness-failure construction absent from the original
  p56 passage. Neighborhood semantics gains the concrete concert/movie
  disjunctive-strategy example,p75.
- The topological-definability discussion changes its language qualification:
  candidatep79 explicitly attributes the extended result to the basic hybrid
  language enriched with the universal modality, whereas the originalp74
  attribution was less qualified.

Figure identities must be mapped by content, not by their printed ordinal.
The original has18 actual numbered figures; the candidate has23. Textual
cross-references beginning with a figure number were excluded from that count.
Important mappings are original15(Until)->candidate16,
original16(transitive Until countermodel)->candidate20,
original17(neighborhood countermodel)->candidate22, and
original18(topological zig/zag)->candidate23. New candidate figures are15,
17,18,19 and21. No all-diagram visual-equivalence claim is made.

## Citations, references and qualification boundary

Original references are numbered1--133; candidate references1--145. Specific
confirmed mappings include original83(Makinson)->candidate92,
original117(van Benthem1978)->candidate129,
original119(van Benthem1983)->candidate131,
original125(van Benthem2001)->candidate137. Reusing bracket numbers without
the actual source bibliography would point to different works.

Candidate title, complete eight-section body, references through145, and
standalone index are readable and present. There is no full-handbook cover,
copyright page, ISBN page, chapter DOI imprint or publisher-provided version
designation in this captured standalone file. It has no first-page2007
copyright/footer establishing that manifestation. The publisher's84-page
identity remains an external record, not an established identity of these
bytes. Even if a later comparison finds its first84 pages mathematically
identical to the publisher chapter, that is a relation to prove and record,
not an acquisition result inferred from matching page count after truncation.

Qualified result of this block: a complete, readable, separately hashed
87-page revised standalone source and concrete82/87 version differences.
Exact gap: a readable and version-qualified published2007 pp1--84 body,
followed by its actual comparison against both selected82 and candidate87.
ED26-SRC-025-001 acquisition/comparison is therefore still open; the82-page
writer may use this evidence for version distinctions without changing its
assigned original extent. No manuscript, intake, shared driver, canonical
registry or admission/coverage record was changed by this work.
