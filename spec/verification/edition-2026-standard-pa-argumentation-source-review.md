# Standard PA and finite argumentation: independent source review

Date: 7 September 2026. Reviewer: `/root/standard_pa_argumentation_source_review`.
Review began at 22:14 UTC and was filed before the 15-minute checkpoint.
Repository: `C:\Dev\the-methods-of-reason`, branch `phase4-codex`, HEAD
`35d537c692bb74b532dc4aa750da381a7fe4daf2`. The targets are the live,
uncommitted files identified below. HEAD is context, not their content snapshot.

## Verdict

**PASS for the assigned source-fidelity and local-compatibility scope.** No
blocking discrepancy was found in the four frozen manuscript files. The PA
construction is a new numerical deduction from the actual local syntax,
axioms and ND rules. The argumentation chapter accurately gives finite
instances of the identified Dung results and labels its additional examples
and guarded acceptance queries as handbook choices.

| Component | Verdict | Extent of the conclusion |
| --- | --- | --- |
| PA literal seven axioms and induction recognizer | PASS | Exact decoding, local Q/PA compatibility, canonical closure, literal rejection boundaries and primitive-recursive bounds. |
| PA derivation transport | PASS | The displayed closing conventions, including the stated source variants, preserve the actual rule conditions by the all-variable subset argument. |
| PA direct numerical checker and certificate bridge | PASS | All twenty inherited row checks, direct tag 19, certified tag 16, sentence roots, open axiom leaves and empty contexts are handled consistently. |
| PA numerical/internal boundary | PASS | The text accurately leaves arithmetic-formula selection and the internal D2/D3 construction open. Their completion is UNRESOLVED by this unit. |
| Dung identity, source mapping and bibliography preservation | PASS | Actual printed journal leaves identify the retained source; the current bibliography agrees with that identity, and an in-memory inverse verifies preservation of the pre-locator entry. |
| Finite argumentation definitions, results, examples and queries | PASS | The finite deductions and six complete example calculations support the stated source relationships and additional handbook conventions. |
| Broader argumentation boundaries | PASS | The text retains the finite scope and does not claim the remaining infinite, structural, game, dialogue or empirical treatments. Their completion is UNRESOLVED by this unit. |

These verdicts concern this review scope. Manuscript build, rendering,
publication quality, source rights, three-review admission and final editorial
acceptance were not performed or supplied by this review.

## PA findings and evidence

1. **The seven constructor expressions decode to the actual Q axioms.**
   The expressions in `handbook/parts/p05/standard-pa-proof-predicate.tex:24-34`
   use exactly the constructor grammar in
   `handbook/restoration/inherited-09328-09438.tex:24-64`. Their respective
   matrices are `not(Sx0 = 0)`, `Sx0 = Sx1 -> x0 = x1`,
   `not(x0 = 0) -> exists x1 (x0 = Sx1)`, `x0 + 0 = x0`,
   `x0 + Sx1 = S(x0 + x1)`, `x0 * 0 = 0`, and
   `x0 * Sx1 = (x0 * x1) + x0`, with the displayed outer universal closures.
   These match all seven clauses of
   `handbook/restoration/inherited-09099-09111.tex:1-13`. In particular, q3
   has its predecessor witness under the distinct binder x1. The two-variable
   closure cases are q2, q5 and q7. The choice x = x0, y = x1 is expressly
   made before serialization; neither term instances nor arbitrary alpha
   variants become additional literal constants. Annex lines 8-43 preserve
   this boundary. The separate prime-power illustration in inherited syntax
   lines 372-388 is correctly excluded from these governing codes.

2. **The induction matrix and its parameter closure match the active PA
   definition.** The source is
   `handbook/restoration/inherited-09175-09187.tex:2-12`: the conjunction of
   the zero instance and the universally quantified successor step implies
   the universally quantified matrix, with parameters closed universally.
   Body lines 45-82 instantiate exactly this shape using the specified
   substitution, an increasing list of distinct free parameter indices, and
   an explicit invalid-matrix default. The definition does not require the
   induction variable to occur freely. The shadowing example at body lines
   164-171 follows the source substitution's stopping clause, rather than
   changing bound occurrences.

3. **The literal identities needed by closure transport are valid for the
   local deterministic substitution.** The source clauses are
   `handbook/restoration/inherited-03240-03428.tex:20-46`, implemented by
   inherited syntax lines 153-201. Substitution of xi for xi is literally the
   identity: its own binder stops the substitution and every other binder
   avoids the replacement term. Neither substitution of 0 nor of Sxi invokes
   fresh renaming. Consequently the free-variable equalities and
   `Var(I(theta,i)) = Var(theta) union {xi}` in the PA annex, lines 45-90,
   follow by structural induction. Canonical closure introduces only names
   already in that all-occurrence set.

4. **The recognizer has a bounded inverse for each induction axiom.** Body
   lines 84-109 first type-check a sentence, handle the seven constants,
   strip the maximal universal prefix, recover i and m from the implication's
   quantified consequent, and reconstruct the complete axiom for literal
   comparison. An induction core starts with implication, so prefix stripping
   cannot consume part of the core. The constructor/list inequalities give
   the stated bounds on variable-index scanning, matrix recovery and prefix
   stripping. Annex lines 92-139 prove both acceptance directions and the
   primitive-recursive closure from the already specified list/substitution
   operations. The rejection statements cover changed matrix copies,
   mismatched binders, shadowing violations and noncanonical prefixes;
   derivability is not used as an axiom test.

5. **The transport verifies the stronger existential-elimination condition.**
   Annex lines 141-169 supply actual forall-E steps using each removed
   binder's own variable, followed by forall-I in reverse target-prefix
   order. The sole open assumption is a sentence. Whole-tree insertion in
   annex lines 171-195 replaces only surviving open axiom occurrences and
   uses unmarked new leaves. For source-to-canonical induction transport,
   the new leaf's all-variable set is contained in the replaced source
   closure's set; extra vacuous source binders only enlarge the latter. In
   the reverse direction the permitted source closure of exactly the free
   parameters has the same all-variable set. The q-axiom closing-order
   cases also preserve this set. Thus the eigenvariable remains absent from
   each affected remaining open assumption, as required by inherited syntax
   lines 293-300, the actual quantifier rule at
   `handbook/restoration/inherited-03927-04061.tex:21-34`, and
   `handbook/registry/calculi/nd-fol.tex:26`. Closedness alone would only
   suffice for forall-I. The proof also preserves exact old formulas,
   branch-specific discharge and its existing nonvacuity witnesses. Its
   bounded postorder rebuilding argument at annex lines 197-215 supplies
   the claimed effective transport without proof search.

6. **The direct checker retains the complete inherited calculus.** Body
   lines 174-207 incorporate the row grammar, earlier references, parent
   counts, open-occurrence lists, exact substitutions, alpha test and
   variable side conditions of inherited syntax lines 224-319. I checked
   all twenty rule tags against both annex arrays at lines 228-237. The
   premise arities are
   `0,2,1,1,1,1,3,1,2,1,2,1,1,1,1,1,2,1,0,2`; parameter-list lengths are
   `0,0,0,0,0,0,2,1,0,1,0,0,1,3,3,1,4,0,1,4`.
   These agree with the full tests, including body-order implication
   elimination and premise-free equality introduction. Final axiom checks
   apply exactly to surviving open leaves. The one-row q examples and the
   empty-open-list proof of 0 = 0 at body lines 209-222 follow these rules;
   the latter makes no assertion that 0 = 0 is a nonlogical axiom.

7. **The new code sort and the internal arithmetic boundary are explicit.**
   Direct records require `N19(N15(R),0)`; the earlier certified convention
   requires tag 16 and a history list ordered by its final open leaves
   (inherited syntax lines 338-370). The PA annex, lines 254-302, proves
   both standard-model proof-meaning directions and a bridge of proof
   existence. The arbitrary c.e. domain-index direction uses existence of
   finitely many accepting histories and does not claim a primitive-recursive
   bound on finding them. Distinct injective outer tags give disjoint
   positive code sorts. Body lines 243-252 and annex lines 304-314 accurately
   leave selection of the graph description and formula, internal modus
   ponens and evidence-to-proof work subsequent. This agrees with the
   graph-description interface at
   `handbook/restoration/inherited-09262-09327.tex:67-148` and the existing
   numeralwise-representation boundary at inherited syntax lines 472-520.

## Dung findings and evidence

The retained PDF's physical page 1 is printed page 321 and identifies Phan
Minh Dung, the article title, *Artificial Intelligence* 77 (1995), 321-357,
the AIT affiliation, receipt in June 1993 and revision in April 1994. Its
opening footnote distinguishes the earlier condensed presentation. Physical
page 37 carries the final printed page 357 and the final references. The
file has 37 pages. The generic digital metadata and unrelated digital-author
field do not replace this printed article identity.

| Printed source evidence actually inspected | Corresponding manuscript evidence and finding |
| --- | --- |
| p. 325, start of Section 2.1; p. 326, Definition 2 and Remark 4 | Body lines 20-40 preserve directed attack orientation and the abstract status of argument identifiers. Finite A, including empty A, is an explicit restriction. Self-attacks are allowed by the relation definition. |
| p. 326, Definitions 5-6; pp. 328-329, Definition 16 | Body lines 35-64 preserve conflict-freeness, acceptability relative to S, admissibility and the characteristic function. The handbook's term defense is explicitly mapped to Dung's acceptability. It does not require a defended argument to belong to S. |
| p. 327, Lemma 10; p. 329, Lemmas 18-19 | Body lines 66-77 and annex lines 9-40 give valid monotonicity, preservation of conflict-freeness, admissible-image and enlargement deductions. The conflict proof explicitly includes the self-attack case. |
| p. 327, Definition 7, Theorem 11(2), Corollary 12; p. 328, Definition 13 and Lemmas 14-15 | Body lines 82-108 and 139-157 retain inclusion-maximal preferred semantics and stable semantics. Annex lines 81-118 give full finite maximal-extension existence, stable-implies-preferred, and the stable complement-of-attacked-set equivalence. The cardinality choice in the finite proof selects a maximal admissible superset; it does not redefine preferred to mean maximum cardinality. |
| p. 329, Definitions 20 and 23; p. 330, Lemma 24 and Theorem 25(1)-(2) | Body lines 110-137 and annex lines 42-79 give a finite proof of grounded existence, admissibility, leastness among all fixed points, completeness and intersection of all complete extensions. The n+1 evaluation bound counts the final equality comparison; it includes empty A. Conflict-freeness remains necessary for an arbitrary fixed point to be complete. |
| p. 327, Example 9; p. 328, Lemma 15 counterexample; p. 329, Example 22 | Body lines 170-193 accurately identify the mutual-pair attack pattern and one-argument self-attack as source patterns. It explicitly calls the other cases additional finite illustrations. |
| p. 330, Remark 26 | Body lines 232-244 and 268-274 and annex lines 180-199 provide an additional explicit witness: every preferred extension contains d, but the grounded extension is empty. This supports the source's stated distinction. |
| pp. 330-331, Definition 27, Lemma 28, the non-finitary pointer and beginning of Section 2.3 | Body lines 284-288 preserve the need for separate infinite/finitary, transfinite and further-semantics treatments. No finite stopping bound is asserted for arbitrary infinite frameworks. |

I independently followed all six finite calculations in annex lines 120-201.
The chain has sole complete/preferred/stable extension {a,c}; the mutual pair
has complete extensions empty, {a}, {b} and preferred/stable singletons; the
self-attacker has the sole complete/preferred extension empty and no stable
extension; the empty framework has one empty extension in each family; the
unequal-size framework has preferred/stable extensions {a} and {b,c}; and the
shared-argument framework has preferred/stable extensions {a,d} and {b,d},
with empty grounded extension. The lists and counterexamples are supported
by the stated attack sets and exhaustive admissible-candidate arguments.

Body lines 251-266 explicitly introduce the handbook's nonemptiness guard for
skeptical queries. They correctly distinguish an empty family from a family
containing the empty extension and describe the unguarded universal's vacuity.
This convention is not attributed to Dung as a change to stable semantics.
The historical skeptical/credulous names for grounded/preferred semantics
remain distinct from membership queries over a selected extension family.
The interpretation statements at lines 12-15 and 276-288 correctly refrain
from inferring premise truth, attack correctness or empirical adequacy from
the abstract input relation.

The broader order-structure results in Theorem 11(1) and Theorem 25(3),
continuity, Section 2.3 coincidence results and the rest of Dung's article
are not supplied in this unit. This review establishes the stated finite
foundation and does not treat the whole article or N-x-009 as completed.

## Bibliography comparison

The current `Dung1995` record is at `handbook/bib/handbook.bib:2155-2166`.
Its printed author/title/journal/volume/year/page identity agrees with the
actual source leaves. The existing issue 2 and DOI
`10.1016/0004-3702(94)00041-X` are preserved. The added institutional URL is
`https://cse-robotics.engr.tamu.edu/dshell/cs631/papers/dung95acceptability.pdf`,
with access date 2026-09-07. No additional bibliographic identity was created.

The pre-locator whole-file hash recorded at
`spec/research/edition-2026-probability-kamp-l1-integration.md:72` is
`A9CFDB177C40F50581B87F8626318FDEFEAA7C5C300D7971A09FFEA2F22C9A53`.
I read the current bibliography bytes and removed only the exact URL and
access-date lines inside the Dung1995 record in memory. Hashing that inverse
recovered the recorded pre-locator digest exactly. The current digest is
`417399F8D66B5D7285B6B98DA4C2C6AF38EE1D1510E3C56273226FC936F708B7`.
This is direct evidence of preservation relative to that snapshot. HEAD
predates the entry and was not used as the pre-locator content baseline.
The institutional URL was not re-fetched in this review; no new acquisition
or assertion of byte equality with a different online copy was needed.

## Actual reading, source inspection and independence

- Read the complete edition contract, `spec/EDITION-2026-CONTRACT.md:1-168`,
  and the complete PDF skill before inspecting source pages.
- Read all four target files completely: PA body 1-252, PA annex 1-315,
  argumentation body 1-289, argumentation annex 1-201.
- Read the complete local Q definition 1-13, PA definition 1-13, governing
  syntax/checker file 1-546, substitution file 1-189, first-order-deduction
  file 1-135, and ND-FOL sheet 1-29. A truncated output segment in the
  twenty-rule list was separately retrieved at lines 260-307. Read only
  lines 67-148 of the graph-construction file, for its referenced interface
  and stated boundary.
- Rendered and visually read the nine complete selected Dung source pages:
  printed 321, 325-331 and 357, corresponding to physical pages 1, 5-11
  and 37. The page bodies, displayed mathematics, headings, footnotes and
  relevant diagrams were inspected at 120 dpi. The remaining 28 pages were
  not read. No manuscript pages were rendered.
- The author handoff `spec/research/edition-2026-p18-a1-finite-argumentation.md`
  was read after the direct manuscript and source-page inspection as a
  locator/scope note. Its verification and acceptance statements were not
  used as independent evidence. Only the specific old-hash row was read
  from the earlier integration note. No other new target-review conclusions
  were read before this filing.
- No manuscript edits, tests, builds, manuscript rendering, source acquisition
  or subdelegation were performed. The only repository write is this report.
  Source-page rasterization used temporary files outside the repository.

## Frozen hashes

SHA256 values below were checked against the actual local files. The four
target digests and the retained source digest match the assignment.

| File | SHA256 |
| --- | --- |
| `handbook/parts/p05/standard-pa-proof-predicate.tex` | `71D3E5569BFB7BAE907CA818BE65DBBCE5E48DBA86D9D8942819DCC5110331E2` |
| `handbook/annex/p05/standard-pa-proof-predicate.tex` | `7F3E3F751832ACACFFC8F2383E2AC14A8D8DC7A9DEA2DA4B837F3A9DF648DFDF` |
| `handbook/parts/p18/finite-argumentation.tex` | `685A2D6BF0125A07A5C85AEC0DA22CA9866B9799202750C758CA8BC1062C85AC` |
| `handbook/annex/p18/finite-argumentation.tex` | `1B70FD5FA52B42BBCBA76976D484A0E2DFD1A67EDEEDDD1BB5D88713F9509BAA` |
| `source/references/dung-1995/dung-1995-ai77-n-games.pdf` | `C78EE6D0864CA18A882E6CF79BB1356EFD86F1D32B38B55570FB572E4651FBA3` |
| `spec/EDITION-2026-CONTRACT.md` | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `handbook/restoration/inherited-09099-09111.tex` | `38534E090C35DB78D99D045D19B3C7F34F1F1AAA8999CF118C7A416CD41D9D2B` |
| `handbook/restoration/inherited-09175-09187.tex` | `0DB98B87928AA115C82883993E2E25B18286779E7DED0399C7148633C0178430` |
| `handbook/restoration/inherited-09328-09438.tex` | `A6E37FA592E81B888C14A2DA97CC70F1A05EC69BAE0CE4D36E2E60C59F09C541` |
| `handbook/restoration/inherited-03240-03428.tex` | `36D7779D6B9BB3CAF0C4EF514A79A1C7D8AA10BD4A72290256EA1D09D5DB58CC` |
| `handbook/restoration/inherited-03927-04061.tex` | `2AD2846970D4976177B0FBB8AC59FF8106253F5D155A5E4861956F7F651BF480` |
| `handbook/registry/calculi/nd-fol.tex` | `F25549BC18FC4AAE212EEA32CADC9FFFD08E03D712F5DF10E9DA62F660BE5370` |
| `handbook/restoration/inherited-09262-09327.tex` | `B49A3B30AFF36050841D4F384A6BA80FCF36F4661B3C4085E58D2371B4E003CB` |
| `handbook/bib/handbook.bib` | `417399F8D66B5D7285B6B98DA4C2C6AF38EE1D1510E3C56273226FC936F708B7` |

The report's own digest is returned after final write/readback, rather than
embedded in the bytes it hashes.
