# Lawvere's original Quantifiers and Sheaves: source-specific authoring record

Date: 2 October 2026. Unit `ED26-REQ-N-d-023-01`; parent `N-d-023-C01`;
allocated components `N-d-023-S01-PRESENTATION`, `-PROOF`, `-BRIDGE`,
`-TASK01`. This is an authoring/provenance record, not source admission,
independent review, queue closure, or publication evidence.

## Authority and ownership

Read in full: `handbook/CONVENTIONS.md`, `spec/EDITION-2026-CONTRACT.md`,
`spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md`,
`spec/research/edition-2026-authoring-resumption-2026-09-09.md`, and
`work/next-formal-authoring-units.md` (especially candidate 6). Parsed the
actual queue record with exact `unit_id=ED26-REQ-N-d-023-01`, not a stale
capsule. Read the actual common host's topos section and the full presheaf
body/annex pairs before reusing their mathematical interfaces.

Owned new files only:

- `handbook/parts/p10/presentations/n-d-023-source-01.tex`
- `handbook/annex/p10/n-d-023-source-01.tex`
- `handbook/bib/intake-p10-lawvere-sheaves.bib`
- `handbook/registry/symbols-intake-p10-lawvere-sheaves.csv`
- `source/references/p10-lawvere-sheaves/`
- this note.

The lead owns the common host, part/annex drivers, style, canonical
bibliography/symbol registry, queue/canonical/generated records and final
integration. The parallel Mac Lane--Moerdijk writer owns source-03. No
shared file was modified by this author. Scoped permission was requested;
source rendering required a scoped escalated command after a normal
directory-create attempt was denied. Source renders are not manuscript
renders.

## Exact manifestation and reading qualification

F. W. Lawvere, *Quantifiers and Sheaves*, *Actes du Congres international des
mathematiciens*, Nice 1970, Tome 1, Gauthier-Villars, published **1971**,
printed pp.329-334. Stable citation key: `Lawvere1970`.

Held original-layout PDF:
`tmp/pdfs/p10-topos/lawvere-quantifiers-and-sheaves-icm1970.pdf`.
SHA-256: `25BD24945DBD216B384AB4B094FF1BB4315682D0D90817C0CAD77CB15DA74DE4`.
Six physical pages; physical page n = printed page 328+n. The hash was
recomputed in this block and matches the dispatch and retained source record.

Primary original [archive PDF](https://lawverearchives.com/wp-content/uploads/2024/12/1970-quantifiers-and-sheaves.pdf).
The [family-maintained chronological bibliography](https://lawverearchives.com/work/),
entry 11, was inspected in this block: it explicitly lists Nice 1970,
Gauthier-Villars **1971**, pp.329-334, and links this PDF. Thus the event date
does not supply the publication date. No later TAC reprint is used as the
authority or asserted byte-identical to this original.

All six source pages were read visually in full from the locally rendered
`source/references/p10-lawvere-sheaves/original-page-1.png` through
`original-page-6.png`. The primary web PDF extraction was also read, but it
was not trusted for damaged formulas. Visual reading checked especially:

- p.330: the support/dependent-product square; `(Pi)` versus `(exists)`;
  the covariant `P Set`/`2 Set` examples and their variance;
- p.331: recursion's `E^Omega` (endomap category, not classifier); geometric
  factorization directions; all three topology axioms and all four
  associated-sheaf observations;
- p.332: the generalized-ultraproduct inversion formula
  `h(u_*(sigma_1(Pi_(X->1)(X'))))=true_0` and its types;
- p.333: `omega < u^*(2^omega) < 2^omega`; the direction of `2^omega<I`;
  the exact `Y times omega isomorphic Y` condition and the source's still
  unspecified suitable chain condition;
- p.334: all four prime-subobject clauses, particularly the product
  equivalence and the direction of the additive implication.

The archive's six-page extent and title agree with the held PDF. This
reading does not qualify all the works in the source's bibliography, prove
unprinted source claims, or compare publisher volume typography independently.

## Source-to-manuscript map

| Exact source interval | New body content and standing | Annex/result route |
| --- | --- | --- |
| p.329 opening paragraphs | Joint work with Tierney; geometry/logic and modal-locality program; no external infinite-limit reliance; BVM/CH and intrinsic-spectrum applications; varying sets, choice, global-point qualifications | Introductory independently worded account; no invented formal theorem for the motivation |
| pp.329-330, section 1 opening | Original finite limits **and finite colimits**, exponentials, `true:1->T`, unique characteristic pullback, `{X/phi}` | `def:p10-lawvere-sheaves-topos`; concrete matched host bridge |
| p.330 first paragraphs | Heyting object T, internal predicate adjoints along every map; topological opens and presheaf cribles; formula/subobject correspondence | General internal Heyting/predicate construction now proved editorially in `annex:p10.lawvere-sheaves.predicate-adjoints`; concrete bridge remains distinct |
| p.330 slice/internal-category paragraphs | `Pi_f` right adjoint on slices, support, internal action category topos, `f_0` and `f_*` | Full editorial functional-graph, internal-action and both-extension constructions now supply `thm:p10-lawvere-sheaves-internal-adjoints`; the original's historical announcement standing is unchanged |
| pp.330-331 support square and conditions | Exact `(Pi)` and `(exists)`; conjunction equivalent to every epi splitting; group and well-ordered/covariant-diagram distinction; Skolem/local-existence interpretation | `thm:p10-lawvere-sheaves-choice`, full editorial annex proof and complete worked examples |
| p.331 recursion paragraph | Additional `(omega)` via free endomap adjoint, not part of initial definition; free group/ring and coequalizer uses; announced lifting over a base | Source attribution and explicit unprovided proof boundary; no assumption that every elementary topos has NNO |
| p.331 morphism/factorization theorem | Exact left-adjoint/direct-image directions; logical preservation; historical local-homeomorphism usage; conservative/full-faithful factorization | Full editorial factorization proof via the actual subobject adjunction L_X/G_X and constructed sheaf reflector; original announcement standing preserved |
| p.331 topology/associated sheaves | Idempotence, truth and meet preservation; universal closure; separated/closed characterization; four observations; singleton-first finite route; exactness via inverted maps | Full editorial closure, associated-sheaf, left-exactness and sheaf-classifier proofs now supplied; original printed route remains historically a sketch |
| pp.331-332 Godement example | Internal topology basis, comparison relation, realization/sections adjunction, image sheaves and cotriple alternative | Intrinsic cover/local-refinement criterion is derived as necessary and sufficient for the displayed adjunction; finite Godement/filtering dependencies separately qualified; no claim that 1970 prints the formula |
| p.332 double-negation paragraph | Double-negation topology/cofinal reading, classical sheaf logic, Boolean classifier/complemented-summand comparison | Full internal Heyting/nucleus, closed-predicate, complementary-summand and canonical 1+1 classifier proof supplied editorially |
| p.332 generalized-ultraproduct theorem | Finite-limit base functor plus Heyting homomorphism; exact monos inverted; logical vs geometric standing; two-valued collapse role | Ordinary localization/logical preservation and separately released full-datum partial-element closed functor plus nondegenerate BVM collapse; stronger normal-relative scope distinguished and degenerate exception retained |
| pp.332-333 section 2 opening | Base `(Pi),(exists),(omega),(not),(or)`; irreducibility; two-subterminal vs monoid counterexample; source Boolean package includes Skolem; BVM/S definition | `def:p10-lawvere-sheaves-bvm`; four-condition distinction kept historical |
| p.333 generation and classification | Subterminal generation under Skolem/classicality; BVM choice and CBA equivalence announcements | Full editorial generation and separately released BVM matrix/choice/cell-regime proofs; original cells unprinted and historical announcement standing preserved |
| p.333 poset and CH paragraphs | Double-negation BVM construction; source stage/cofinal forcing; finite partial maps; distinct ground/new powers; local injection; exact no-epi lemma with suitable ccc wording | `thm:p10-lawvere-sheaves-ch`, all displayed source hypotheses and sketch dependencies preserved; no unproved ZFC-transfer claim |
| pp.333-334 section 3 | Multiplicative monoid pairing, order/incidence submonoids, two fraction objects, sheaf reflection; prime-subobject four clauses; local units; finite-limit prime object; global spectrum/universal local ring | `def:p10-lawvere-sheaves-prime`, `thm:p10-lawvere-sheaves-spectrum`; source sketch retained; elementary classical complement/localization comparison justified in annex |
| p.334 section 4 and bibliography | Rousseau/Kock historical attributions; Lauchli; actual-time proposal; real-object/analysis historical question; all bibliography dependency identities and forthcoming standing | Closing attributed account; no present-day open-problem claim or source-proof substitution |

The source uses `T` throughout for truth values and `Omega` only in the
endomap-recursion category. Source-local reuse of `P` (forcing poset versus
spectrum membership), `u_*` (geometric direct image versus merely finite-limit
base functor), and predicate/family quantification is declared, not renamed to
hide typed roles. The notation intake now includes the additional
general-construction roles. The bibliography intake
retains the existing key and existing correct 1971/event1970 fields, offering
only optional archive URL/provenance enrichment; it is not a second identity.

## Concrete source-to-host bridge and editorial proofs

The concrete example uses these actually read and matching host results:
`def:p10-presheaf-category`, `thm:p10-presheaf-limits`,
`thm:p10-presheaf-mono-epi`, `thm:p10-presheaf-exponentials`,
`def:p10-presheaf-sieves`, `thm:p10-presheaf-topos`, and
`thm:p10-presheaf-power-objects`, with annex `p10.psh.1` through `p10.psh.5`.
Their complete source-specific formulas, restrictions, naturality, two inverse
transpose identities, classifier uniqueness, power membership and empty-base
case were read. Lawvere's crible object is identified as `T=Omega` under these
exact hypotheses. Their later Mac Lane--Moerdijk/Moerdijk--van Oosten proof
attributions remain separate. This is matched reuse with a proved bridge,
not title-based credit for every general internal category.

The following four original bounded proved results remain preserved,
with their reciprocal proofs:

1. `thm:p10-lawvere-sheaves-presheaf-bridge` ->
   `annex:p10.lawvere-sheaves.presheaf`: original finite-colimit package and
   exact `T=Omega` classifier/exponential/power-object match.
2. `thm:p10-lawvere-sheaves-choice` -> `annex:p10.lawvere-sheaves.choice`:
   both directions of the conjunction/choice equivalence, including the
   support of dependent product of a mono and adjoint transposition of a
   global section; group and ordered/arrow cases are checked explicitly.
3. `thm:p10-lawvere-sheaves-closure` -> `annex:p10.lawvere-sheaves.closure`:
   extensivity from the classifier square, monotonicity from meet preservation,
   idempotence, intersection preservation, and pullback stability.
4. `thm:p10-lawvere-sheaves-generators` ->
   `annex:p10.lawvere-sheaves.generators`: complement of an unequal-map
   equalizer, nonzero support, Skolem section, and separating subterminal.

The ordinary prime-ideal complement and `Z_(ell)` calculations are editorial
worked comparisons inside the spectrum annex, not proofs attributed to the
original source or to the general ringed-topos universal construction.

## General internal construction now supplied

Five further explicit proved results, plus the proved dependency summary
at `thm:p10-lawvere-sheaves-internal-adjoints`, now supply the previously
missing general construction chain:

1. `thm:p10-lawvere-sheaves-dependent-product`: define power-object relation
   parameters, impose supportedness and single-valuedness by transposed
   finite equalizers, prove that graph projection is monic, then impose
   exact domain equality by its classifier. This gives counit/evaluation
   without assumed images, unique choice, Boolean negation or exactness.
   Both inverse transpositions, naturality, functor laws, triangles,
   arbitrary generalized pullback Beck--Chevalley, identity/pasting and
   composition coherence, and the complete slice topos package are proved.
2. `thm:p10-lawvere-sheaves-predicate-adjoints`: derive universal quantification
   by applying the constructed Pi to monos. Construct a map's image as the
   universal intersection of all power-object predicates containing it;
   prove its epi cancellation and minimality, then stable epis/images by
   the actual pullback adjoints. Construct implication from the meet-order
   equalizer, prove residuation, joins and the internal Heyting structure,
   and represent existential/universal adjoints as actual power-object maps
   in every parameter context. Full pullback/Frobenius laws are included.
3. `thm:p10-lawvere-sheaves-effective-quotients`: prove every epi coequalizes
   its kernel pair through the image of its paired graph and epi descent;
   then transpose an internal equivalence relation to its row map. Equality
   of rows has exactly that relation as kernel pair, and the constructed
   image gives its effective quotient. Regularity/effectiveness are
   conclusions, never premises used for Pi or images.
4. `thm:p10-lawvere-sheaves-internal-presheaf-topos`: define full internal
   action data; construct free/cofree adjoints to underlying families;
   create finite limits and finite colimits using established preservation
   by family pullback; construct compatible-function exponentials and
   internal sieve classifier with unique characteristic pullbacks. Every
   compatibility predicate is built using the now-proved general Pi/forall,
   not by assuming external infinite products or global-point sufficiency.
5. `thm:p10-lawvere-sheaves-internal-kan`: restriction along an internal
   functor has a right extension formed from dependent assignments indexed
   by `b:F(c)->d`, with all C-action compatibilities. The left extension is
   a finite coequalizer of the two explicit generator/relation D-presheaves
   indexed by `b:d->F(c)`. Inverse adjunction correspondences, naturality,
   actual units/counits, triangle identities and functoriality are supplied.

All five have individual reciprocal `annex:p10.lawvere-sheaves.*` proofs.
The original internal-completeness sketch target is coherently replaced by
a full dependency-summary proof only after those constructions were supplied
and read through. Its historical p.330 source-announcement attribution is
still explicit. This is not replacement of the original article by another
source version or acceptance of the full Lawvere unit.

For a limited primary comparison, the author-hosted 2007 Moerdijk--van Oosten
notes' section 4 slice paragraph on p.67 and adjacent examples were
inspected: they state the fundamental slice
topos/adjoint theorem and distinguish logical inverse image from general
geometric behavior. This comparison statement was not used as a proof or
as a substituted 1970 presentation. The new general constructions above
are separately identified editorial deductions from the original package.

## General associated-sheaf construction now supplied

The actual p.331 source page was reinspected during the sheafification
continuation. Three complete editorial proof units now give its missing
construction chain without assuming reflectivity or a sheaf topos:

1. `thm:p10-lawvere-sheaves-associated-sheaf` ->
   `annex:p10.lawvere-sheaves.associated-sheaf`: identify image T_j with
   Eq(j,id), classify closed predicates, and extend them uniquely across
   dense monos by closure. Prove sheaf exponentials by dense product
   pullback; prove separatedness iff uniqueness across dense monos; prove
   closed subobjects of sheaves are sheaves and sheaves are closed in
   separated superobjects. The closed diagonal is explicitly proved an
   equivalence relation using j's meet/monotonicity equations. Its closed
   row map has exactly that kernel pair, and the previously constructed
   effective quotient gives S_X. Closing S_X in T_j^X gives a_jX and the
   actual natural extension bijection for every sheaf target. This proves
   all four source observations and the full separated/closed characterization.
2. `thm:p10-lawvere-sheaves-sheaf-topos` ->
   `annex:p10.lawvere-sheaves.sheaf-topos`: prove a_j inverts exactly maps
   with dense image and dense relative diagonal, equivalently exactly the
   maps inducing hom bijections into every sheaf. Prove their pullback
   stability, then left exactness by the actual pullback comparison
   P=X times_Z Y -> Q=a_jX times_(a_jZ) a_jY: its intermediate relation is
   closure of P and its kernel pair is closure of Delta_P. Construct finite
   limits, reflected finite colimits, ambient exponentials and classifier
   true_j:1->T_j in the full sheaf category. Monos between sheaves are proved
   underlying closed monos; characteristic uniqueness and its converse are
   supplied. In every slice E/B, the relative reflector is explicitly
   B times_(a_jB) a_jX -> B, and it commutes canonically with all pullbacks
   B'->B. Its sheaf property and universal property over B are proved, not
   inferred from global-point semantics. Identity and chaotic topology
   boundary cases are retained.
3. `thm:p10-lawvere-sheaves-factorization` -> existing reciprocal
   `annex:p10.lawvere-sheaves.sheaves`: for the given geometric L left adjoint
   R, derive the actual subobject adjunction L_X left adjoint G_X, with
   G_X(B)=X times_(RLX) RB. Its composite constructs a universal closure and
   hence j_u. Prove dense monos iff L-inverted monos and j_u-bijective maps
   iff L-isomorphisms. R lands in j_u-sheaves; restricted L/R give the
   conservative factor, and a_j/i_j give the full-and-faithful factor.
   For initially full-and-faithful R, the restricted adjunction is proved
   an equivalence. Recover closure/topology from inverted monos. The
   original factorization sketch target is upgraded only after these full
   deductions are supplied; the historical printed announcement/sketch
   standing is still explicit.

Images, effective quotients, and pullback stability used in these proofs
refer to the preceding actual constructions, not added assumptions. The
closure/singleton route uses finite/internal constructions at arbitrary
generalized bases, not global-point sufficiency, Boolean negation, chosen
class representatives, an external infinite product, or transfinite plus
iteration. The following two separate proof units now supply the
double-negation and Godement applications, rather than crediting them merely
by the general reflector theorem.

## Double negation and the qualified Godement reconstruction

`thm:p10-lawvere-sheaves-double-negation` has a reciprocal full proof:
triple-negation, idempotence, truth/bottom and meet identities are derived
intuitionistically; fixed predicates have closed complements and closed joins
giving excluded middle. A disjoint-cover kernel-pair argument proves genuine
coproduct summands without assuming extensivity. The three source classicality
conditions, including canonical 1+1->T, are proved equivalent. No Skolem or
choice claim follows from classicality alone.

`thm:p10-lawvere-sheaves-godement` reconstructs L/Gamma by finite generators,
relations and dependent sections; proves germ equality by a local common
refinement; proves cover/refinement both necessary and sufficient for left
exactness, with universal generalized-index tests; identifies the exact
covering-sieve topology and its full image sheaves; and proves comparison
with coalgebras of the left-exact cotriple by explicit finite equalizers and
the previously proved conservative image factor. The source's word poset
is qualified: arbitrary duplicate basis labels produce a thin preorder,
which the reconstruction retains rather than silently identifying labels.
This is a derivation of the criterion equivalent to the displayed geometric
adjunction, not an invented extra premise or an unprinted formula quoted as
Lawvere's text.

Finite primary dependency qualification:

- Godement, *Topologie algebrique et theorie des faisceaux*, Hermann:
  held 295-page scan at `source/references/p10-lawvere-sheaves/godement-topologie-algebrique-held-scan.pdf`,
  5,589,977 bytes, SHA-256 `B391C13011740C11BBF22747C8FCD6516A37FC7E91576616E742995C4DBDAB9B`.
  Physical p4 explicitly says new printing 1998 and copyright 1958.
  It is not asserted byte-identical to a 1958 first edition. Printed
  pp.109-113 were visually inspected; selected II section 1.2 pp.110-112
  gives the downward-filtered neighborhood/germ construction, etale topology,
  theorem 1.2.1 and generated-sheaf comparison. Physical = printed+12.
  The extra intake key is `Godement1998Printing`, with this exact standing.
- Held MLM1992, unchanged SHA-256 `A30AE90087DF702F6E48A705FF313CEB7821FAE55AB3CF43E255D4DCD7B95825`:
  VII section 8 pp.394-398 visually read. Definition 1 and Lemma 3
  pp.394-397 state epimorphic-local filtering, including generalized
  parameter objects. The proof on p398 continues beyond the reading;
  no full general filtering/flatness theorem is credited. Its external
  small-category/cocomplete discussion is not imported as an assumption
  on Lawvere's arbitrary elementary base. The finite/internal basis
  special-case proof is supplied separately here.

All new source-page renders are in the owned evidence directory. No full
book reading, first-edition typography match, or whole-book source credit is
claimed for these finite dependencies.

## Component disposition and exact still-owed work

### Released ordinary-localization continuation

The lead froze the prior reader files/intakes. This continuation edits only
new `spec/fragments/p10-lawvere-localization-body.tex`, matching
`-annex.tex`, uniquely suffixed `symbols-intake-p10-lawvere-localization.csv`,
and this note/evidence directory. The frozen body/annex/intakes, drivers,
canonical and queue files were not changed by this author.

MLM1992 V section 9 pp.256-263 was visually read through Theorem 2's final
classifier proof and Lemma 3; the following exercises are not credited.
Source images `mlm-filter-quotient-1992-267.png` through `-274.png` use
printed+11. PDF SHA-256 remains A30AE90087DF702F6E48A705FF313CEB7821FAE55AB3CF43E255D4DCD7B95825;
the exact original Lawvere PDF remains 25BD24945DBD216B384AB4B094FF1BB4315682D0D90817C0CAD77CB15DA74DE4.
The later book's proper-filter convention is distinguished from the
explicit degenerate-base extension. No new bibliography key is needed.

Three new reciprocal complete proofs supply the full u_*/h-induced arbitrary
truth filter and cofinal denominator equivalence; actual fractions,
coherence and functor-category universal property; and all localized
finite limits/colimits, exponentials, eventual strict monos, unique
classifier and logical preservation including internal quantifiers.
The arbitrary filter is proved to have exactly the original localization
property, not substituted by a finite/principal/Boolean/prime filter.

At this ordinary-localization release the closed-category base construction
and collapse were still owed; the separately released closed-base continuation
below now supplies its explicitly qualified construction and collapse.
The given u_* need not descend: product Set times Set to Set,
with h the first projection, inverts (1,0)->(1,1) but u_* sends it to 0->1.
The h-total partial-element/effective-quotient route in E_0 has now been
carried through in the disjoint closed-base fragments; its exact closed
versus normal-relative scope and countercases are recorded below.
The finite needed 1966 Eilenberg--Kelly definitions have now been acquired
and qualified there. Lead integration should supersede the corresponding
old sketch omissions only with the actual released theorems and their
scope qualifications, preserving the historical source announcement and
the remaining full-source obligations.

`N-d-023-S01-PRESENTATION`: source-specific account authored across the full
six-page extent, with exact source hypotheses and historical proof standing.
It still awaits integration and independent fidelity/admission checks; this
record does not mark it accepted.

`N-d-023-S01-TASK01`: concrete presheaf limits/finite colimits, exponentials,
classifier uniqueness, power-object membership/naturality are supplied by the
matched existing complete proofs plus the explicit new proved bridge. No new
claim of source-native detailed proof or independent acceptance is made.

`N-d-023-S01-BRIDGE`: concrete `T=Omega`, covariant-vs-presheaf variance,
support-vs-dependent-product, historical Boolean-vs-modern-classical,
ordinary-vs-generalized ultraproduct, ground-vs-new power object, and
prime-subobject-vs-classical-prime-ideal comparisons are authored. Their
general proof dependencies below remain open rather than being counted away.

`N-d-023-S01-PROOF`: **partial; not closed**. The source's announcement or
sketch standing does not waive a separately promised complete proof.
Exact residuals:

1. Any specified set-theoretic transfer/model interpretation and CH's
   positive consistency direction remain owed. The separately released
   CH-chain fragments now supply an explicit sufficient internal ccc,
   its finite-partial-map verification, the complete no-epi predicate
   lemma, local sequence-injection descent and both conditional strict
   internal comparisons. These are not an unspecified full ZFC theorem.
2. Internal multiplicative-basis directness, both fraction-object universal
   constructions and their reflected comparison, locality of the sheaf ring,
   and global-spectrum universal property.
3. The additional recursion condition's lifting and the invoked general
   free group/ring constructions, if required as independent full proof
   dependencies rather than source announcements, remain owed.

The frozen core retains source-result sketch targets `ultraproduct`,
`ch`, and `spectrum` under `annex:p10.lawvere-sheaves.*`. The released
localization and closed-base continuations now supply the ultraproduct
construction at the explicit closed-functor/nondegenerate-collapse scope;
lead integration must repair that old reciprocal sketch/boundary with
these actual dependencies and qualifications. The new CH-chain continuation
supplies its internal chain/no-epi/descent/comparison proof dependencies;
specified set-theoretic transfer/positive consistency and spectrum remain
owed. Historical source announcement standing is not silently
changed into source-native detailed proof credit.

## Author-only checks and verification limits

### Author-side adoption of the six CH-chain proof pairs

The latest root-corrected source-01 was read before editing, including its
at-most-two truth/false subobjects and exactly-two-under-nondegeneracy
qualification. That correction, source-03, prior constructions and shared
work were preserved. Both frozen CH fragments were read completely;
their working originals remain unchanged.

New adopted files are handbook/parts/p10/presentations/n-d-023-ch-chain.tex
and handbook/annex/p10/n-d-023-ch-chain.tex. Six reciprocal full-proof
pairs, all existing thm: identifiers, parameter branches and the actual
internal-site bridge are preserved. The parent body inputs the child
immediately after the source's finite-partial-map CH datum and no-epi
display, before the spectrum subsection. Only directly affected CH sketch
and final-boundary prose in source-01 body/annex was repaired.

The original reciprocal CH sketch status and historical article boundary
remain. Stale ccc/no-epi/descent/strict-comparison omissions now point to
the actual six proofs, keeping the explicit sufficient-condition/editorial
qualification rather than inventing an original definition of suitable.
Specified set-theoretic transfer/model interpretation, positive consistency,
spectrum, independent recursion/free-algebra and arbitrary stronger-base
obligations remain explicit. Released CH intakes needed no identifier or
notation changes. Shared annex driver/canonical/baseline routing remains
root-owned. No test, review, build or manuscript render was performed.

### Released CH-chain continuation

Owned new files only: spec/fragments/p10-lawvere-ch-chain-body.tex and
its matching annex, uniquely suffixed CH-chain intakes, this note and the
existing source directory. No adopted reader/annex, previous intake,
driver, canonical, generated or baseline file was edited.

Original p.333 was visually re-read in full from original-page-5.png:
the actual finite partial maps on omega times I; ground power object;
new power object; constant-sheaf adjunction; suitable ccc wording;
Y times omega isomorphic Y; and the entire internal Epi-object display.
The held six-page manifestation and 1971/event1970 distinction remain
unchanged. Current adopted BVM/base statements and current source-03
stage-forcing/internal-epi dependency bodies were inspected. The latter's
external-small-site scope is only a comparison: the new proof derives the
internal cofinal-witness/all-refinement clauses from actual closed
presheaf predicates, stable images and quantifier adjunctions.
No new primary manifestation or whole-book reading is claimed.

Six reciprocal full editorial proof units now supply:

- bounded greedy maximalization, finite-domain cardinal maps, countable
  families/images, an actual omega-squared pairing bijection, and
  X times omega isomorphic X for infinite X by countable-block partition;
- an internal delta-system induction and finite root coloring, proving
  ccc for the actual finite-partial-map object at every parameter base;
- dense separated constant units, internal forcing/image/quantifier
  clauses, transported NNO, and actual subconstant free-action covers
  giving the source's stronger Boolean/choice package;
- maximal deciding antichains and countable output fibers, constructing
  a ground epi from a supposed local one, with the necessary finite-X
  branch handled separately and all internally parametrized epi objects;
- actual dense partial evaluation and sheafification/transposition,
  followed by fresh-coordinate kernel separation for the injection;
- both displayed strict comparisons, including all epi predicates
  rather than only the canonical comparison map, using a concrete
  complement retraction. A permissible ground I is explicitly 2^C.

The exact chosen sufficient hypothesis is internally quantified ccc
(antichains embed into omega), not merely an external assertion about
global antichains. The original does not print a unique formal meaning
of suitable; no reconstructed formula is quoted as original wording.
Classical base logic, choice, power objects and actual NNO recursion
remain explicit. Maximal histories are bounded in power objects; no
external ordinal recursion, Zorn theorem, Replacement or ZFC universe
was imported. The source's Y times omega hypothesis is retained; the
stronger declared base tools make the no-epi argument valid even without
that extra restriction. The concrete X=1,Y=omega example disproves the
naive X times omega epi inference and explains the finite-X repair.

All six results are newly supplied editorial deductions. Their scope is
the internal source construction, not a transfer to an independently
selected set-theoretic axiom system/model or positive consistency proof.
General spectrum/locality/universality and independently owed general
recursion/free-algebra work remain separate. The new NNO preservation
is proved for the forcing construction and is not called a completed
free-algebra or unrestricted source-recursion package.
No child, review, test, build, manuscript render or restricted-acquisition
retry was performed.
The complete new body and annex were read back. All six reciprocal
targets were manually matched; the finite-X and internally parametrized
branches were inspected separately. Six complete proof environments and
the 16-row disjoint notation intake are authored. These are author-only
observations, not independent review, admission or a consolidated gate.

### Author-side adoption of BVM and closed-base continuations

Root initially allocated source-03, but actual reading showed that file is
the Mac Lane--Moerdijk semantics presentation. Root corrected the assignment
to localized integration in source-01. Source-03 and its annex were not
edited by this author. The four working originals under spec/fragments/
p10-lawvere-bvm-* and p10-lawvere-closed-base-* remain preserved.

Adopted reader files are handbook/parts/p10/presentations/n-d-023-bvm.tex
and n-d-023-closed-base.tex; their matching complete annexes are
handbook/annex/p10/n-d-023-bvm.tex and n-d-023-closed-base.tex.
All eight reciprocal proof pairs are retained. Active annex copies use
proper begin/end annexitem environments. CONVENTIONS permits no lem:
prefix: the adopted BVM base result is now thm:p10-lawvere-bvm-base,
with its annex backref, closed-base dependency reference and two intake
first-use cells repaired. The adopted closed-base countercase lemma is
likewise thm:p10-lawvere-closed-base-countercases; its backref matches.
These are identifier/environment repairs, not mathematical notation changes.
Legacy working originals retain their release text and hashes separately.

The source-01 input order is: existing ordinary-localization input;
abstract-set/BVM definition and subterminal-generator theorem; historical
BVM announcement; new BVM input; new closed-base input; separate restored
double-negation/CH subsection. This puts each construction after its
mathematical prerequisites. Superseded parent final-boundary and
ultraproduct-missing assertions now link the actual qualified constructions.
The old ultraproduct reciprocal sketch status and historical article
boundary are retained, with arbitrary strong/normal convention kept distinct.
Root separately authorized only the core annex's directly affected
ultraproduct/CH omission prose and the localization reader's obsolete
remaining-work paragraph; those were repaired, leaving unrelated proofs
and all mathematical CH/spectrum/recursion obligations unchanged.

The nondegenerate collapse guard, unrestricted u_*/h construction,
improper/degenerate boundary and general nonnormal/nonstrong distinction
remain in the adopted reader. Existing BVM/collapse proofs are no longer
listed as missing CH dependencies. This correction does not prove the
suitable ccc, no-epi lemma, injection descent, strict cardinal comparisons
or transfer. Shared annex drivers, canonical bibliography and symbols,
generated/baseline records and all admission/review/build gates remain root
work. No review, test, build, manuscript render or generator was run.

### Released full-datum closed-base and collapse continuation

New owned files: `spec/fragments/p10-lawvere-closed-base-body.tex`, matching
`-annex.tex`, and uniquely suffixed closed-base symbol/bibliography intakes.
Frozen core, ordinary-localization and BVM fragments/intakes were not edited.
Four reciprocal editorial full proofs construct h-total partial members,
their actual effective equality quotient H_h(X), forward-image map functors,
the natural singleton comparison and truth map extending h; terminal,
product and equalizer comparisons; inversion of every exact original mono
using its universal truth (without commuting h/u_* with quantification);
the unique fraction extension and finite limits of arbitrary germ diagrams;
actual base hom objects, identities/composition, evaluation transpose and
all three closed-functor compatibilities; and injective ordinary fraction
names in those hom objects. These use the full internal h datum, not only
the induced global filter.

Product/first-truth-projection gives H_h first projection and repairs the
explicit failed descent of original u_*. Diagonal Set to Set times Set
gives diagonal H_h and an invertible closed comparison, but pairs of
global function values versus only equal pairs of ordinary localized maps.
Thus the general ordinary closed-functor construction is supplied, while
neither normality nor identification of the enriched global underlying
category with E_h is inserted into the full original datum. Eilenberg--Kelly
p.549 has a stronger normal relative-base convention; Lawvere p.332 does
not print the corresponding additional requirement. A universal stronger
claim for this fixed ordinary E_h is contradicted, not renamed as a missing
construction or silently waived.

For nondegenerate BVM over S, bounded proper-filter histories in power
objects construct an actual Boolean/Heyting homomorphism p_*T to 2;
completeness of that homomorphism is not claimed. The exact localization
is proved nondegenerate, classical, two-valued and choice-preserving.
In this particular geometric-original/choice-base case the naming maps
are also proved surjective, giving the normal element identification up
to canonical isomorphism. The quotient target is not claimed geometrically
over S. Degenerate BVM cannot map its one-element Boolean algebra to
nondegenerate 2; this necessary qualification of the original word always
is explicit. The unrestricted degenerate-base/improper-filter construction
is retained separately and not called a nondegenerate two-valued collapse.

Finite historical primary acquired and visually read: Eilenberg--Kelly,
Closed Categories, proceedings of La Jolla 1965, publication 1966,
pp.421--562. Institutional original-folio PDF in the owned source directory:
`eilenberg-kelly-closed-categories-1966.pdf`, 142 pages, 8,576,440 bytes,
SHA256 `2C47935A55B94529437056E8BE83C7C3B8CA8CA5B643E6A37F206420039E1BA0`.
Physical n = printed 420+n. Selected complete visual readings only:
pp.428--429 (closed-category data/axioms), pp.433--434 (closed-functor
data/CF1--3; following composition proof continues beyond selected page),
p.439 (normality definition and local discussion), p.549 (relative-base
paragraph's stronger normal convention and promised later comparison).
No full 142-page reading, whole composition theorem proof, or later-paper
relative-base equivalence proof is credited. New key EilenbergKelly1966.
Primary URL: https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/EilenbergKelly.pdf.
Original Lawvere p.332 was visually re-read; its 1971/event1970 standing
and held SHA256 remain unchanged. The research skill's background-agent
step is fulfilled by this already delegated author; no additional child
was created under the parent's prohibition. PDF workflow was source reading
and source-page rendering only, not PDF/manuscript authoring.

These four proof units supply the general closed-functor construction and
the nondegenerate collapse with its actual existence hypotheses. Full
CH/ccc/transfer, spectrum/locality/universality and recursion/free-object
dependencies remain owed, as does any newly specified stronger target
not following from the printed datum. This is a release, not source
admission, an independent review, a build/render/prose test or a gate.
The complete new reader and annex were read back; all four result/annex
targets were manually matched. The 18-row notation intake parses and the
single new bibliography identity was inspected. These are author-only
observations, not an independent strict gate or compilation check.

### Released BVM continuation

New disjoint files: `spec/fragments/p10-lawvere-bvm-body.tex`, matching
`-annex.tex`, and uniquely suffixed BVM symbol/bibliography intakes.
All frozen core/localization reader and intake files were preserved.
Four reciprocal full editorial proofs provide bounded base well-ordering
from power objects and actual choice; internally S-complete `p_*T`;
partial-element epi covers and effective matrix quotients; actual map
functors and inverse comparisons/triangles; internal join-coverage sheaf
realization and classifier; explicit epi sections by Boolean
disjointification; entrywise complete homomorphism transport and actual
sheaf right adjoint; adjunction bijections/units/counits/triangles;
reconstruction from geometric inverse images; universal-index 2-cell
tests and composition/unit coherence by equality of quotient values.

Conventional geometric direction yields CBA(S)^op. The explicitly
inverse-image-directed regime yields CBA(S). Source p.333 prints neither
1-cell nor 2-cell definitions, so this qualification is in the reader.
No general geometric inverse image is claimed logical or power-preserving.

Finite primary qualification: MLM1992 VI section 1 pp.268--276 and VI
section 4 pp.291--295 were visually read in full from the held PDF,
physical=printed+11. Renders `mlm-bvm-base-1992-279.png` through `-287.png`
and `mlm-bvm-choice-1992-302.png` through `-306.png` are in the owned
source directory. Proposition 8's proof on p.276 continues to unread
p.277; the choice-independence proof on p.295 continues to unread p.296.
Neither complete later proof nor its set-theoretic transfer is credited.
Their distinctions of Boolean logic, two-valuedness and choice are a
comparison, not the basis for an original ZFC independence proof.
Held hashes and the 1971/event1970 distinction remain unchanged.
No new citation key was required.

This release supplies the stated editorial BVM/choice dependency at the
specified cell scope. The source unit remains partial: closed-category
base localization/collapse, CH/ccc/transfer, spectrum/locality/universality,
and recursion/free-object dependencies remain fully owed. This is not
admission, independent review, a build or a consolidated gate.

Read back the complete new body and annex. Inspected their mathematical
types and dependencies against all six rendered source pages. Author-only
structural inspection originally found nine reciprocal items; after the
general, sheaf and Godement constructions, all current result/annex pairs were
inspected again and have exact reciprocal targets.
There are fifteen full `proof` environments in the annex and three
omission-specific sketch notices, and no body `proof` environment. CSV
parsing reads the extended notation intake, including Godement and cotriple roles.
A local lexical inspection also found
balanced unescaped braces and matching begin/end environment nesting in
both new TeX files. These are
author-only structural observations, not the consolidated strict gate.

Finite mathematical checks, not software tests of book prose:

- Enumerated the arrow-example section choices: at stage 0 the forced
  images of `a,b` require both different final choices, giving zero natural
  sections; at stage 1 there are two. All three component fibers are
  nonempty, so this concretely separates support from dependent-product
  support.
- Enumerated all natural truth-object endomorphisms for the two-stage sieve
  classifier (`Omega(0)=2`, `Omega(1)=3`) satisfying the source's topology
  identities. Exactly four survive; all are extensive. The rejected
  nonextensive abstract-chain maps fail classifier naturality, in agreement
  with the general classifier-square proof.
- Enumerated all 64 relation subsets for a finite family with two-element,
  one-element, and empty fibers of f. The graph equalizers give respectively
  2, 1, and 1 total functional graphs, preserving the empty-fiber case.
- Checked the internal-functor collapse of a two-object arrow category on
  a presheaf with two elements at its lower object and one at the upper:
  the right-extension compatibility gives one assignment and the
  left-extension relations give two classes, as limit/colimit require.
- Computed the actual closed-singleton image and closure construction in
  the two-stage presheaf category for all four natural topologies. A test
  family with component sizes (2,3) reflects to (2,3), (2,2), (1,3), and
  (1,1), respectively. The initial family reflects to (0,0), (0,0), (1,0),
  and (1,1). This checks both an empty-cover topology and the chaotic
  degenerate case, including that the reflected initial object need not
  be ambient zero. These finite calculations are checks, not the general proof.

No children, reviews, manuscript builds/renders, software/prose tests,
queue/canonical edits, paid acquisition, login, contact, CAPTCHA, or security
bypass was performed. No independent acceptance is asserted. The permitted
next mathematical continuation is specified CH transfer/positive-consistency,
spectrum and independent general recursion/free-algebra dependencies.
Ordinary localization, the explicitly scoped editorial BVM construction
and the qualified full-datum closed-functor/nondegenerate collapse
are released separately above. The source-03 concrete
internal-logic treatment must stay separate.
Shared routing and later consolidated gates are lead work.
