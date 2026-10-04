# Kripke 1975: partial-truth authoring record

Updated 1 October 2026. This is the working source and integration record for
the owned treatment, not an independent review or an admission record.

## Actual source and extent

- Saul Kripke, *Outline of a Theory of Truth*, *The Journal of Philosophy*
  72(19), 6 November 1975, 690–716, DOI 10.2307/2024634.
- Local original: `source/references/kripke-1975-truth/kripke-1975-outline.pdf`.
- SHA256: `C63A44C5D0C3386679C5B01ECAB9F6F6889B8E3E908188D92226EF785317939F`.
- The scan has 28 physical pages: page 1 is a JSTOR wrapper, page 2 begins
  with the previous article's ending before Kripke's title, and page 28
  ends with the following article's opening. Kripke's complete article and
  its footnotes on printed 690–716 were read; adjacent articles were excluded.
- Public source locator preserved in the bibliography enrichment:
  <https://www.impan.pl/~kz/truthseminar/Kripke_Outline.pdf>.
- Printed 711 was also inspected as an image to disambiguate formula (14)
  and the two different consistency restrictions. It is
  `forall x not (T(x) and T(neg(x)))`, with the outer negation present.
- Martin's 1984 reprint and Halbach's 2011 first edition were not used as
  interchangeable copies. Their separately allocated presentations remain owed.
- On resumption, printed 697–699 and 709–711 were reread directly from
  the held original, including the transfinite discussion at 697 and
  the intrinsic-level/equivalence passage and finite-hierarchy footnote
  at 710. The selected allocation in
  `spec/coverage/edition-2026/requirements-units.jsonl`, unit
  `ED26-REQ-N-b-020-01`, was also read. The 1975 source omits the
  transfinite definition and explicitly requires proper definitions for
  its converse; it does not supply a canonical full-general theorem
  that can be attributed to the construction below.
- In the semantic-order continuation, the original 1974 coding discussion
  and 5A.1 at printed 65–66 were reread directly. Its elementary tuple
  constructors and finite numerical histories are the actual resources
  used below; no algorithm on arbitrary opaque domain objects or primitive
  truth-stage predicate is imported from that source.

### Bounded computational dependencies acquired in the continuation

- Speranski's author-hosted preprint,
  `source/references/kripke-computational-dependencies/speranski-2017-author-preprint.pdf`:
  18 numbered pages, 491074 bytes,
  SHA256 `E8A118CF2E6BA8281BF1C5940C99997C0C0E362E65FCF4109F0BD4070947CE12`.
  All eighteen pages were read. Source URL:
  <https://homepage.mi-ras.ru/~speranski/files/preprints/speranski-2017-sl.pdf>.
  The held preprint has no separate draft date. The
  [publisher identity](https://link.springer.com/article/10.1007/s11225-016-9694-8)
  verifies online publication 5 November 2016 and Studia Logica 105,
  407–429, April 2017. Its original V_VB constrains both coordinates;
  its V_SV constrains only the positive coordinate. The former is the
  unrestricted extension family used in the original Kripke treatment here.
  Its optional non-code atomic convention is not substituted for our stage 0.
- Moschovakis's 2009 author copy of *Descriptive Set Theory*,
  `source/references/kripke-computational-dependencies/moschovakis-2009-dst-author-copy.pdf`:
  516 physical pages, 3014970 bytes,
  SHA256 `7E213EA8198B070977E34A04CE78210A0E74F38BD5270C0E17BB079DEFAFA07F`.
  Source URL: <https://www.math.ucla.edu/~ynm/lectures/dst2009/dst2009.pdf>.
  The title date is 8 April 2009. The front matter and the bounded
  positive-induction discussion on printed 311–319 were read. This is
  **not** the 1974 *Elementary Induction on Abstract Structures* and is
  not credited as acquisition of that book's acceptable-structure definitions.
- Harel and Kozen's original 1984 journal article, acquired from Kozen's
  institutional author page:
  `source/references/kripke-computational-dependencies/harel-kozen-1984-ind-author-copy.pdf`,
  22 physical pages, 947881 bytes,
  SHA256 `AFA78AC0BC62A965818A546A0F5E0ABFB235F919549DB9EAA9EE589817E17D63`.
  Public source: <https://www.cs.cornell.edu/~kozen/Papers/IND.pdf>.
  Selected extent read: §§1–5, printed 118–132, plus the resource
  description at the opening of §6, 133. This significantly revised
  journal version is not the 1982 conference preliminary report. It
  supplies finite-program, parameter-section, inductive/coinductive and
  halting conventions for the generic construction; it does not replace
  the original 1974 book.
- Exact original Moschovakis 1974 *Elementary Induction on Abstract Structures*,
  `source/references/kripke-computational-dependencies/moschovakis-1974-eias-repository.pdf`:
  222 physical pages, 8832996 bytes,
  SHA256 `8C4343281193094AF3F1E983224DFC714CE63BC4AC3419647CE5053E072F6BBA`.
  Public institutional repository:
  <https://ndl.ethernet.edu.et/bitstream/123456789/37633/1/32.pdf>.
  The original title, 1974 copyright and North-Holland ISBN 0-7204-2280-9
  were inspected. Four captured preliminary pages precede numerical body
  pages 1–218; this is not a claim that every originally paginated
  preliminary leaf is present. Selected reading: title/copyright/preface,
  introduction and 1A opening; 1B–1D (printed 8–23), and 5A–5C with 5D
  opening (printed 65–74). Printed 65–66 coding definitions were also
  inspected as images. The numerical body extent and index ending were
  checked. This is a bounded computational dependency, not a claim of
  read-through of all 218 numerical pages or completion of a separate
  original-book allocation.

## Owned outputs and integration interfaces

- Body: `handbook/parts/p11/kripke-truth-fixed-points.tex`, chapter label
  `sec:p11-kripke-fixed-points`.
- Proofs: `handbook/annex/p11/kripke-truth-fixed-points.tex`, section label
  `sec:p11-ktf-proofs`.
- Symbols: `handbook/registry/symbols-intake-p11-kripke-truth-fixed-points.csv`,
  157 rows: the already merged 93 rows, the protected previous 32-row
  return in scope `P11 recursive truth hierarchies`, and a new 32-row
  append in scope `P11 semantic-order truth hierarchies`. The present
  return boundary is rows **126–157**. Rows 94–125 remain the lead's
  protected prior append boundary, not a second copy of this return.
- Bibliography: `handbook/bib/intake-p11-kripke-truth-fixed-points.bib`,
  **one existing key** `Kripke1975`, offered for enrichment, not duplication,
  and new keys `Speranski2017TruthAuthorPreprint` and
  `Moschovakis2009DSTAuthor`, `Moschovakis1974EIASOriginal`, and
  `HarelKozen1984IND`. The original key
  enrichment adds the publication date, source URL and scan-boundary note.
- No shared driver, canonical bibliography, canonical symbol file, style,
  generated apparatus or frozen coverage catalog was changed by this author.
- The lead confirmed routing and integration of the prior 30-pair package,
  its arithmetic extension rows and Moschovakis2009 key. The generic finite
  arithmetic graph proof now precedes the P11 use in P4 under
  `thm:p04-doh-arithmetic-graphs`; P11 retains its compatibility statement
  and the lead's reciprocal compatibility proof. The old beta intake row
  was relocated, not duplicated. The P4 native Delta11/HYP construction
  and annex are now routed, as confirmed by the lead. The current generic
  append added 10 reciprocal pairs, 31 symbol rows, and two bibliography
  keys. The lead has now canonically merged that append and all earlier
  rows through 93. This resumption adds no bibliography key or enrichment.

## Completed proof statements

There are fifty-two reciprocal body result / annex proof pairs. Their proofs
are written; this count does not certify mathematical or publication acceptance.

| Result suffix `thm:p11-ktf-...` | Annex suffix `annex:p11.ktf....` | Content |
| --- | --- | --- |
| evaluation | evaluation | Unique recursive evaluation, coincidence, capture-free substitution and information persistence, including every quantifier case |
| order | order | Partial order, compatible union, monotone/disjoint jump and failure of the full state-space lattice property |
| construction | construction | Actual ordinal recursion, increasing consistent stages, stabilization below omega1 from countable sentence codes, leastness and seed extension |
| examples | examples | Rank/code-entry offset, truth-free rank zero, actual coded liar, both truth-teller seeds, fixed-point value transparency versus material biconditional |
| limit-example | limit-example | Unbounded finite chain, omega-rank universal, next-stage code entry and failure of omega-union preservation |
| maximal | maximal | Zorn maximal extensions, every maximal point deciding the truth-teller, no greatest point, liar gaps and a sentence defined in some but not all maximal points |
| intrinsic | intrinsic | Closure preserving compatibility with every fixed point, arbitrary joins, greatest intrinsic point and meets as joins of lower bounds |
| intrinsic-example | intrinsic-example | Ungrounded intrinsically true rho and the never-false truth-teller excluded middle with no intrinsic value |
| boundaries | boundaries | Nonempty unrestricted completion family, supertrue liar excluded middle, classical successor oscillation and the metalanguage/object-language gap distinction |
| empirical | empirical | One held syntax made grounded true, grounded false or paradoxical by a base predicate; a mutually dependent pair settled at ranks 1 and 2 |
| tarski | tarski | Finite noncumulative Tarski predicates as internal formulas under the **explicit syntactic-adequacy premise**, all bivalent and fixed-point independent |
| satisfaction | satisfaction | Extra sequence-code premise, full satisfaction jump and least fixed point, with Hartogs bound on the actual argument space |
| signed | signed | The note-24 signed-closure alternative, including equal-denotation atom replacement, equivalent to the least point's defined values |
| schemes | schemes | Distinct weak-Kleene and unrestricted-supervaluation jumps, least points, ordinal-stage inclusion and classical theorem-code universal |
| restricted | restricted | Original negation-consistency restriction and separate maximal-consistent-theory restriction, eligible states, nonempty families, monotone jumps, union limits and least points |
| closed | closed | Closing off, persistence of old defined values, the conditional T-biconditional and failure to obtain a truth fixed point after classical reevaluation |
| arithmetic-graphs | arithmetic-graphs | Compatibility invocation of the full earlier P4 finite-sequence/CRT and machine-history graph construction, with the P11 statement label preserved |
| tree-normal-form | tree-normal-form | Effective tree normal form, including the relative version and a numerical canonical branch selection for arithmetical witness families |
| pi-upper | pi-upper | Full SK signed-closure upper bound and original two-coordinate SV upper bound using arithmetically packed countermodel/valuation witnesses |
| tree-ranks | tree-ranks | Actual uniform diagonal sentence family for recursive forests; identical SK/SV height ranks, no false values, and branch gaps |
| pi-representation | pi-representation | Both directions of the positive monadic Pi11 characterization for SK and SV, plus computable many-one completeness |
| ck-lower | ck-lower | Recursive decreasing-order trees yielding every recursive ordinal as a sentence rank and the cofinal CK lower bound |
| total-upper | total-upper | Every total monadic extension and its complement are Pi11, hence the extension is Delta11 |
| finite-equivalence | finite-equivalence | Computable translations between the noncumulative and cumulative finite classical Tarski hierarchies over the arithmetic base, preserving every assignment and treating non-code inputs explicitly |
| pi-operations | pi-operations | Effective Pi11 positive operations, including both number quantifiers; the existential case is justified by packed arithmetical counterexample witnesses |
| pi-comparison | pi-comparison | Actual universal Pi11 index, recursive KB order and initial-segment non-embedding comparator with the required outside-domain behaviour |
| effective-induction | effective-induction | Coded diagonal self-index for a verified Pi11-preserving monotone operator, recursive-ordinal entry bounds and CK stabilization |
| ck-exact | ck-exact | Concrete SK signed-rule and original two-coordinate SV compiler hypotheses, SK stage comparison and exact CK upper plus lower for both |
| total-converse | total-converse | Actual alternating product-tree sentences, bivalence by well-founded induction and both cases distinguishing a Delta11 set and its complement |
| effective | effective | Exact total-HYP classification for SK and original unrestricted SV, using the independently supplied native P4 characterization and the local total-Delta results |
| internal-syntax | internal-syntax | Exact original acceptable coding scheme; elementary finite histories, postorder parsing, free-index lists, assignment updates, capture-free constant substitution and total closing |
| internal-induction | internal-induction | Uniform finite elementary positive signed interpreter, actual tag packing, and equality of its least closure with the least SK point |
| acceptable-ind | acceptable-ind | Both directions of generic SK Ind(A) definability through actual internally closed diagonal sentence families and parameter sections |
| elementary-games | elementary-games | Constructive positive-formula-to-control-game compilation, replacement of rejection by divergence, and actual game-to-truth-template stage correspondence |
| selective-shuffle | selective-shuffle | Both active/inactive winner claims proved by proper successor resolution ranks; no unproved running-time equality or Boolean combination |
| hyperelementary | hyperelementary | Full Harrington totality converse using a never-rejecting inductive game, dual complementary game and elementary alternating shuffle |
| general-classical-valuation | general-classical-valuation | First-order matrix in relation arguments and actual unique classical valuation for all internally coded formulas and assignments |
| general-tellers | general-tellers | Injective elementary truth-teller family remains gap-valued through every SV stage and permits every selected subset in total completions |
| general-sv | general-sv | Both directions of generic Pi11(A) definability; typed ambient pre-fixed operator, explicit choice-based packed countermodels, and truth-teller coding of arbitrary finite-arity relations |
| general-finite-hierarchy | general-finite-hierarchy | Actual elementary finite guard formation and noncumulative/cumulative code translations over acceptable structures; default variable-term noncode rather than an assumed numerical noncode |
| recursive-hierarchy | recursive-hierarchy | Unique classical well-order recursion with computable finite-word syntax over arithmetic and varying empirical predicates, including a new truth predicate at each nonzero limit index |
| limit-separation | limit-separation | Actual finite-word diagonalization showing that the added full truth set is not already definable in its prior union language |
| transfinite-embedding | transfinite-embedding | One self-template word translation, all assignments and empirical interpretations, with successor/limit stage bounds proved rather than an assumed stage predicate |
| stage-compiler | stage-compiler | Actual total self-indexed signed finite-word compiler using the separately proved P4 program self-reference lemma |
| transfinite-stages | transfinite-stages | Exact positive/negative coordinate formulas for every index of a recursive well-order, including actual union stages and negative noncodes |
| uniform-converse | uniform-converse | Both expressive directions at every represented bound; safety, supremum intrinsic evaluation bound and semantic equivalence are precisely defined, and represented-bound membership is proved equivalent to the supremum criterion |
| intrinsic-scope | intrinsic-scope | One safe fixed tree sentence with empirical ranks cofinal in omega1, failure of safety after admitting branch models, and safe finite examples separating rank constancy and semantic rank invariance |
| semantic-order-syntax | semantic-order-syntax | Actual elementary finite parse/legality certificates with opaque indexed atoms; total prospective embedding and signed compilers copy finite template codes without deciding the semantic order |
| semantic-order-embedding | semantic-order-embedding | Unique completed hierarchy for any codable set well-order, original-truth embedding with all successor/limit bounds, and actual opaque-name diagonal proof of prior-language truth undefinability |
| semantic-order-stages | semantic-order-stages | A named actual graph formula supplies the self-template compiler without a numerical program-index import; exact signed coordinates follow by well-order induction |
| semantic-order-converse | semantic-order-converse | Uniform held-family equivalence in both directions; stabilization below the code-domain successor cardinal; represented-rank criterion, all countable/nonrecursive numerical instances and every separately codable rank below that successor |
| expansion-transport | expansion-transport | Actual prospective code recoding into a finite ordinary expansion, with equality at every original truth stage, nonsentence preservation, identical grounding and first ranks; no assumption of unchanged-string conservativity |

## Source distinctions and repairs

The source at 702–703 starts with both coordinates empty, leaving **T on
all of D** undefined. Non-sentence objects become negative at jump 1. The
draft and proofs retain this staging. The initial truth-free base atoms
are already classically evaluated. Countable closure counts sentence-code
additions after the first jump, not all domain elements; D may be uncountable.
No complete-lattice Knaster–Tarski theorem is applied to consistent partial
states. The complete-lattice claim is proved for intrinsic fixed points only.

The source's first supervaluation consistency restriction (711) means absence
of a sentence together with its negation in the positive extension. It is
**weaker** than finite-theory consistency. The original family is retained;
the stronger maximal-consistent-theory family remains separate. Negative
non-code membership is imposed by each jump, not by a hidden initial change.
With arbitrary non-code assignments permitted in the first completion family,
the unguarded formula (14) is established at stage 1; the guarded version is
already supertrue at stage 0. Under maximal-consistent completions both are
supertrue at stage 0 because their positive coordinate is a sentence theory.
All these formulas hold at their respective least fixed points as the source
asserts. Empty completion families are excluded through an explicit eligibility
domain; they cannot vacuously make every sentence both true and false.

The finite Tarski embedding requires internally definable syntax guards.
The generic fixed-point existence theorem assumed only an external code
injection, which is insufficient for that stronger conclusion. The finite
embedding now states its actual additional syntactic-adequacy hypothesis;
adjoining primitive guard predicates is identified as a different expansion,
and is not credited as a proof of definability in the old base.

Invalid saved label prefixes `lem:`, `meth:` and `ex:` were replaced inside
this owned treatment by the required `thm:` and `def:` prefixes.
The signed-closure definition explicitly includes equal-denotation replacement;
it does not silently identify strings when a closed term has the same numerical
denotation as a numeral.

## Exact remaining obligations

**Do not close ED26-REQ-N-b-020-01 / N-b-020-C01 from this return.**
The complete original article was read. Its main semantic, arithmetic and
acceptable-structure constructions now have written proofs in the chapter.
The eight terminal clauses have the following exact standing:

1. **Completed at written-proof standing:** exact arithmetic CK closure for
   SK and unrestricted two-coordinate SV. The new effective induction proof
   supplies the upper bound independently of admissibility and combines
   it with the already proved cofinal lower bound. The concrete operator
   compiler hypotheses and the SK signed-rule comparison are proved.
2. **Completed at written-proof standing:** positive monadic extensions are
   exactly lightface Pi11, with both directions, for SK and unrestricted SV.
   The arithmetic graph, tree normal-form and actual syntax-translation
   dependencies are supplied rather than assumed.
3. **Arithmetic total-HYP characterization completed at written-proof standing:** the upper and converse
   constructions are now supplied. The converse uses an alternating
   product-tree formula, not a Boolean combination of weak formulas.
   The independently constructed P4 `thm:p04-doh-characterization`
   supplies the native Delta11/HYP connection with proofs of both
   inclusions. Its actual body and characterization proof were inspected.
   `annex:p11.ktf.effective` invokes it; root reader routing is the
   lead's integration action. This is a supplied prerequisite, not the
   desired equivalence introduced as a definition or assumption.
4. **Completed at written-proof standing:** the full positive Pi11 classification for
   unrestricted supervaluation is proved. Its total/HYP converse and
   characterization has the full total-Delta11 construction and the actual
   native HYP bridge. The SV scheme remains precisely unrestricted total
   extensions of both coordinates.
5. **Completed at written-proof standing:** exact original 1974 acceptable
   structure and Ind(A) definitions, including finite parameters, finite
   primitive signature, every-object names, elementary internal interpreter
   and both directions of Strong-Kleene Ind(A) classification.
6. **Completed at written-proof standing:** full Harrington HE(A) totality
   upper and lower directions in that same regime. The lower direction has
   an actual elementary-control compilation, self-coded truth embedding,
   and selective alternating-shuffle rank proof.
7. **Completed at written-proof standing in the stated ZFC metatheory:**
   generic unrestricted two-coordinate SV Pi11(A) classification, both
   directions. The general upper packing explicitly uses choice, not the
   numerical canonical-selection lemma. Its independent truth-teller lower
   construction is supplied without that selection premise.
8. **Finite translations and a specified recursive-transfinite converse are written:** actual code graphs and
   formula translations implement the noncumulative/cumulative equivalence
   over the specified arithmetic base. The acceptable-structure finite result
   supplies actual internal formation/translation graphs and guards in the
   original name-rich regime; it is no longer a citation-only or arithmetic
   substitute. Separately, the six saved recursive-transfinite pairs construct
   the completed limit convention, its original-truth embedding, an actual
   signed word compiler and exact stage coordinates. The present repair
   defines safety over a specified empirical family, its supremum intrinsic
   evaluation bound and all-interpretations semantic equivalence. It proves
   the converse exactly at represented recursive bounds, without assuming
   primitive stage predicates. The new scope theorem shows that safety over
   an arbitrary empirical family need not supply such a bound. A comparison
   over nonrecursive ordinal presentations and name-rich acceptable bases
   with codable semantic orders is now additionally supplied by the four
   semantic-order pairs and the expansion-transport pair. Its index predicates must be elementary or
   explicitly added as ordinary resources; this is not a theorem making
   arbitrary orders definable in every unexpanded old base. A fixed code
   domain cannot represent orders beyond its cardinal capacity. Other
   limit conventions and a justified identification with any stronger
   intended historical intrinsic-level criterion are not asserted.

The mapped component descriptions MAP-01 through MAP-05 are substantially
advanced by the fifty-two proofs, but MAP-05 and the complete C01 article
obligation are not closed by treating a chosen completed-hierarchy convention
as the unspecified historical full-general intrinsic-level theorem. The
nonrecursive and opaque-index mechanism is now supplied, with the source's
precise omission and the unexpanded-base/cardinal boundaries preserved;
these results are substantive constructions, not a shrinking of the
whole obligation. Separate Martin1984 and Halbach2011
allocations are not completed by reading the 1975 article.

### Attempts at the still-open dependencies

- The naive proposal to combine weak formulas for a Delta11 set and its
  complement into a total SK formula fails. Their values can be (true,gap)
  and (gap,true). A monotone Boolean connective cannot output opposite
  defined signs on these compatible information inputs, since their common
  extension (true,true) would force both signs. Thus two weak representations
  do not prove the required totality converse.
- The initially attempted exact-upper route used a transitive admissible set at the CK
  ordinal, definable ordinal recursion and Sigma1 collection to bound the
  stages of all numerical instances of a quantified formula. The crucial
  dependencies are **admissibility of the CK level**, internal existence and
  definability of the stage sequence, and the actual collection bound. These
  were not proved by that attempt. The later successful norm-index route
  resolves the exact upper bound without importing those missing premises.
- The successful replacement uses the 2009 normed-induction idea with the
  actual numerical prerequisites supplied here: universal Pi11 index,
  recursive KB order, a Pi11 strict comparator with correct outside-domain
  behaviour, an explicit diagonal index, and an effective compiler for
  each concrete operator. Induction on the recursive norm bounds entry
  stages. Pointclass membership alone is not used as a closure bound.
  The coded self-index matrix explicitly retains its two designated
  numerical variables with tautological conjuncts, covering constant
  operator outputs. The SK signed operator discards malformed codes,
  so its fixed sets are precisely the typed closed sets being characterized.
- The original arithmetic upper definability proof did not need that
  closure bound: the ambient signed-powerset pre-fixed-set argument now
  establishes it directly. Its valuation relation is arithmetical **in two
  set arguments**; no uniform first-order arithmetic truth predicate is assumed.
- The successful totality repair uses the synchronized product of two
  recursive trees, one well founded at every input. The equation has an
  outer universal over first-tree children and an inner existential over
  second-tree children. Well-founded induction yields actual bivalent
  values, and inductions on the well-founded coordinate establish the two
  opposite classifications. This resolves the failed Boolean-combination route.
- The prior bounded acquisition pass for the exact 1974 book found its original
  identity in the publisher-hosted contemporary review, later Dover records
  and limited previews, but no readable full original body. An exact
  filename pass in the existing OneDrive Library also found no matching
  book. A later successful public-repository acquisition resolved that source
  obstacle; see the held original and its exact selected extent above.
- The original 1B–1D and 5A–5B definitions resolved the generic regime:
  finite primitive signature, finite parameters, elementary sequence resources
  and names for every domain object. The new finite-history/parse proof and
  positive signed interpreter supply the internal adequacy mechanism. A
  nonuniform infinite primitive vocabulary, or an unnamed uncountable
  parameter domain, is not silently treated as the same language.

## Prior generic-block checks and hashes

At the prior generic-block checkpoint, a bounded own-file integration check established forty reciprocal pairs,
zero duplicate own labels, zero dangling own references, all ninety-three
symbol first-use labels present, zero body proof environments and forty
annex proof environments. All body/annex brace counts were balanced. The
external mathematical cross-references include the existing
`def:p04-kleene-ordinal-notations` and the actually constructed
`thm:p04-doh-characterization` and `thm:p04-doh-arithmetic-graphs`.
The older cited P4 characterization
has not been silently promoted by this author. Author content reasoning was conducted
against the actual LaTeX and original paper. These are not independent reviews.
No manuscript build, manuscript render or prose-mirroring test was run.
The inactive `thm:p02-transfinite-lindenbaum` pointer was removed:
the needed countable extension argument is actually supplied in
`annex:p11.ktf.restricted`, now the cited local pointer.

At that superseded checkpoint:

This is the coherent generic-block snapshot after the lead's completed
relocation of the full graph proof to P4 and after preserving its P11
compatibility interface. The 10 new pairs and 31-row append are stable
for canonical intake; no earlier symbol rows were changed in this block.

| Artifact | Lines | Bytes | SHA256 |
| --- | ---: | ---: | --- |
| Body | 1347 | 69818 | `DEC2451550E49B5EE7833EEB55253460D88CC1509D0844C650349A660AF98DE5` |
| Annex | 2142 | 116027 | `A57E58DD8DAF2C6D0385F6694976A7B5D26D898367CEECFDF5BB068F045690E9` |
| Symbols intake | 94 | 22994 | `D4285DFC34537C578CEE03F3DD4AF8EC018F1143F589C2A4793BB9C45BBDD419` |
| Bibliography enrichment | 81 | 3863 | `32C0BB39FF1ED4012BB8DDEEE9E30A8AE2DC0ED4C172BC8C4E542831A5555B12` |

## Completed generic construction and current intrinsic-level interface

The source read at Harel–Kozen 130–132 defines inductive relations
as parameter sections of a least fixed point of a positive first-order
formula and hyperelementary as inductive/coinductive. Its totality proof
uses a real program shuffle after turning rejections into divergence;
it does not combine two gap-valued formulas by a Boolean connective.
The induced information ordering and ordinary truth ordering are different,
and the program's first resolved label is always a successor-stage event.

The original 1974 source supplies the missing resources. The completed
lower construction replaces each positive recursive predicate by truth
of the actual closed self-template instance carrying its argument tuple.
Projection of the original truth stages reproduces the positive operator's
stages exactly. Upper containment uses a genuinely finite positive
elementary interpreter with fixed ordinary primitive cases, and tag packing
to one relation. The proof identifies its closure with the least SK truth
point, not merely with a proposed evaluation relation.

The HE converse is now resolved by actual control diagrams, with ordinary
literal false terminals replaced by divergence, a dual complementary game,
and the selective shuffle. The proof uses two mutually supported winner
claims at proper successor ranks, and does not assume a theorem identifying
HE with total games. The general SV upper supplies an actual first-order
classical valuation matrix and packed countermodels with choice explicitly
stated. Its lower direction uses the elementary injective all-domain
truth-teller family and tagged tuples for arbitrary relation arities.

The 1975 passage at printed 710 explicitly omits a transfinite Tarski
definition and says that intrinsic level, equivalence and related notions
need proper definitions. Its intrinsic fixed points at 709 are a different
notion. The saved extra block was resumed at body 1533 lines,
SHA256 `CA11C3508DD20CDB7FFB4EB436E2FACDFE0C9E7E83DB7BCC15B9EA3B50275343`,
and annex 2509 lines,
SHA256 `2EF904E6A00F12A21972979E97100485871F5E567A3B4A940AD98BF63162D115`.
It already contained six actual reciprocal proofs, not only a possible
construction. Those proofs were read and preserved, not restarted from
the obsolete forty-pair note.

The current convention fixes standard arithmetic with a finite empirical
predicate signature and one recursive well-order. Each nonzero index,
including a limit, adds ordinary classical truth for the finite-word
language of strictly earlier indexed predicates. This completed hierarchy
differs from an ordinary-union convention; an actual diagonal proof shows
the new limit truth set is not definable in that union. The original-truth
embedding closes an actual finite template at its own code. At a limit,
each input sentence has finitely many lower predicate tokens, so its code
enters below the limit even though the whole family has no one smaller
bound. The proof does not assert preservation of unions by the truth jump.

The signed word compiler is constructed by the separately proved P4 program
self-reference lemma. Its prospective-index factory only inserts a finite
arithmetic computation-graph formula; it does not execute the prospective
program or query a truth stage. The resulting program is total by finite
parse recursion. Classical truth of the actual lower-index compiler outputs
then defines the exact original positive/negative stage coordinates.
Successor indices take the largest preceding jump output; limit indices
take the actual union of lower successor outputs. Negative noncodes enter
at jump one as in the original construction. This supplies the previously
missing variable access to lower stages through an actual code graph and
ordinary truth, rather than a primitive stage predicate.

The repaired intrinsic convention has three distinct objects. Safety means
definedness at every least point over the specified empirical family.
Its intrinsic evaluation bound is the supremum of first defined ranks
over all those interpretations and numerical assignments. Semantic
equivalence compares their least-point values with each other or with
classical hierarchy values, universally over the same family. A safe
formula is defined by its supremum, whether or not one instance attains it.
It has a represented bound b exactly when that supremum is at most the
rank of b. The signed compiler and the original-truth embedding give both
directions of expressive equivalence at every such index. This does not
decide safety or claim minimal syntactic complexity.

Every recursive ordinal has some suitable recursive presentation, but
one fixed presentation has recursive order type below the Church–Kleene
ordinal. The construction is not an index at CK, not a nonrecursive ordinal
compiler, and not a transfinite result over every general acceptable base.
The empirical family is consequential: one fixed self-template tree sentence
is safe across all well-founded empirical trees and has ranks cofinal in
omega1, so it has no recursive uniform bound. Admitting a branch model
makes it unsafe. That safe sentence is nevertheless equivalent to a base
tautology in its restricted family. A separate full-family unary example
has actual ranks zero or one and is equivalent to a bound-zero tautology.
These are counterexamples to silently replacing safety by a recursive
bound, constancy of ranks, or a rank invariant of semantic equivalence.

The subsequent semantic-order construction now resolves the specific
nonrecursive and opaque-index interface left by that recursive block.
It retains the completed-at-limits convention while separating raw syntax
from semantic order-dependent legality. For an acceptable code domain A,
an indexed prime is one tagged tuple constructor with an opaque payload
b in A. A finite parse certificate verifies it without treating b as a
child; a legality certificate checks the ordinary order predicates at
its finitely many indexed records. Those predicates must be elementary
in the base or explicitly supplied as a finite ordinary expansion. No
compiler executes their nonrecursive extensions.

The new self-template mechanism supplies the actual general compiler,
without transferring numerical program self-reference to opaque domains.
An elementary prospective graph C_I(k,selector,index,input,output) verifies
finite syntax transformations for any admissible five-slot ordinary
template code k. At a truth prime its factory copies that template,
putting the name of k in its first slot. After the graph formula has
actually been constructed, take its code h. Its copied instance at h
is then the real C_I(h,...) graph. The graph was built from finite parse,
copying and substitution certificates before h was chosen, and neither
interprets nor recursively recompiles the formula it copies. This is the
new mechanism, not the desired stage predicate disguised as a premise.

Well-order recursion gives the unique hierarchy on any specified index
subset I of A, and an actual named-template embedding has the same
successor/limit bounds as in the recursive proof. The signed compiler
queries classical truth of its actual lower-index outputs. Well-order
induction proves exact stage-coordinate equality: successors select the
largest preceding jump output, and limits take the actual union of lower
successor outputs. Nonsentences receive their negative sign at jump one.
The construction works for all assignments and for a held interpretation
family with the same coding scheme and index order. If the order varies,
the construction still applies separately, but a shared index can have
different ordinal ranks; no common ordinal is inferred from its name.

Choice and the fixed infinite code cardinal kappa give the exact available
scope. Each truth iteration stabilizes below kappa^+ by selecting a fresh
signed domain object at every strict successor. Every separately supplied
ordinal rank below kappa^+ fits an order of type alpha+1 on a subset of A;
none of rank kappa^+ fits that domain. A fixed supplied order only covers
its own initial segments. On the numerical domain this includes every
countable ordinal, even nonrecursive ones. The direct earlier finite-word
arithmetic syntax with function terms is treated explicitly: its raw
compilers remain computable and have arithmetic graphs, while language
legality uses the supplied ordinary order predicates. It is not silently
identified with the distinct relational opaque coding.

The expansion interface also required repair. Adding ordinary order tokens
enlarges the truth language, so an unchanged old T(code) can change value
if an old nonsentence object becomes a new sentence code. The new transport
compiler therefore recodes old formulas. Its named actual graph maps a
source sentence to its translated target sentence code, a source open
formula to an open target formula, and malformed inputs to a genuine
target variable-term noncode. Ordinal induction proves equality of the
old and translated values at every successor and union limit, with the
negative noncode appearing at jump one. Groundedness and first ranks are
identical. Thus old formulas can be transported into the order expansion
before applying the hierarchy converse; expansion conservativity is not
assumed. No inverse translation of arbitrary new ordinary order predicates
to the old base is claimed without their old-base definitions.

The historical boundary is still distinct from these proved constructions.
The original source does not select a canonical intrinsic criterion or
alternative limit convention. The chapter states its relative safety,
supremum-bound and semantic equivalence convention as editorial, not as
Kripke's omitted definition. It does not supply a proper-class all-ordinal
hierarchy on a fixed set code domain, nor show arbitrary added orders are
definable in an unexpanded old base. The concrete previously missing
nonrecursive/codable-acceptable mechanism is supplied; any claim beyond
these resources or identifying them with an unspecified historical
full-general theorem remains unestablished. Do not close the whole original
unit or independent admission merely from these written proofs.

## Protected previous 47-pair return

At the protected previous return, the own-file structural check found **47 reciprocal body/annex pairs**,
zero missing reciprocal mappings, zero duplicate owned labels, zero body
proof environments and 47 annex proof environments. Brace totals balance
in each owned manuscript file. All 32 appended symbol rows have actual
owned first-use labels. The first 22994 bytes of the intake have SHA256
`D4285DFC34537C578CEE03F3DD4AF8EC018F1143F589C2A4793BB9C45BBDD419`,
equal to the prior complete 93-row intake hash: that merged prefix was
preserved byte-for-byte. These are bounded author structural observations,
not independent mathematical, source-fidelity or publication reviews.
No manuscript build, manuscript render or prose-mirroring test was run.

That prior intake boundary is **symbol rows 94–125 only**. No new
bibliography row was returned. The six saved recursive-transfinite pairs
and the new scope pair are all in the same already owned body and annex;
no new driver, canonical file or reader route was changed.

| Artifact | Lines | Bytes | SHA256 |
| --- | ---: | ---: | --- |
| Body | 1610 | 83753 | `DA7DD853E322798543674B2528CCD613A870A19D37518FC4859124A332CBD07C` |
| Annex | 2643 | 141836 | `8BEF2BE202A0A7A715DAEC9B869174449022357C3030F9B48999E86BAA60F459` |
| Symbols intake | 126 | 32311 | `87CFA731195799A88AE92FE48D099443D2932CA469C88286D93C4C5CEE5CCC2C` |
| Bibliography enrichment, unchanged | 81 | 3863 | `32C0BB39FF1ED4012BB8DDEEE9E30A8AE2DC0ED4C172BC8C4E542831A5555B12` |

## Current 52-pair semantic-order return

The actual broad extension adds **five reciprocal pairs** beyond the
protected 47: semantic-order syntax, hierarchy/embedding, exact stages,
uniform converse/ordinal capacity, and expansion transport. The present
symbol intake is **rows 126–157 only**, 32 new typed-role rows. No new
bibliography material, shared route or canonical file was changed.

The protected prior prefix is unchanged in all three artifacts: the first
83753 body bytes hash to `DA7DD853E322798543674B2528CCD613A870A19D37518FC4859124A332CBD07C`,
the first 141836 annex bytes hash to `8BEF2BE202A0A7A715DAEC9B869174449022357C3030F9B48999E86BAA60F459`,
and the first 32311 intake bytes hash to `87CFA731195799A88AE92FE48D099443D2932CA469C88286D93C4C5CEE5CCC2C`.
These reproduce the complete protected return hashes exactly, not only
the counts of its pairs and rows.

Own-file structural observations: 52 body and 52 annex pairs, no missing
mapping in either direction, no duplicate owned labels or dangling own
references, zero body proof environments and 52 annex proof environments.
The brace totals balance. All 32 new symbol rows parse with nonempty
required fields and have actual owned first-use labels. Author reasoning
was checked against the current written proofs and the actual coding
resources. These observations are not independent admission or a
consolidated review. No build, render or prose-mirroring test was run.

The concrete new mechanism removes the recursive-order restriction and
supplies the opaque-domain compiler and the source-expansion bridge.
Remaining boundaries are the explicit ordinary order resource, the
set-sized fixed code/name capacity, the fixed-versus-varying order family,
and the source's unspecified historical intrinsic convention. No result
about an unexpanded base is inferred from an added order predicate, and
no assertion of all ordinals is inferred from every separately codable
rank below the domain's successor cardinal.

| Artifact | Lines | Bytes | SHA256 |
| --- | ---: | ---: | --- |
| Body | 1858 | 97107 | `03ADE57E96E2287D6AA3333C5D219D831374C13A216988EF481B9CC66DC3807B` |
| Annex | 3135 | 169333 | `16413530DA3A6C2B82DDEF78222300D332D165055E0B64CF3B8579B05EA97C46` |
| Symbols intake | 158 | 42265 | `03B8E2B235BA7FC1587185B5B6F5280CE36B142846AC7F7463F6AA0D230B85CC` |
| Bibliography enrichment, unchanged | 81 | 3863 | `32C0BB39FF1ED4012BB8DDEEE9E30A8AE2DC0ED4C172BC8C4E542831A5555B12` |
