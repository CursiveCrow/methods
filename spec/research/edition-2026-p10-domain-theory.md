# P10 domain theory: bounded authoring provenance and continuation

## Source and scope

Current writing addresses TOC151.1--151.4 and bounded components of ED26-SRC-028-501. It does not discharge the full167-page author source or printed SRC028-001, separate PostScript SRC028-503, Gunter/Scott/Mosses or other retained variants. The catalog is unchanged.

Primary `tmp/acquisition/src028/handy1.pdf`: 1,147,740 bytes,167 pages, SHA-256 `74adfbb57ae86a8b24e5afae312ffa77138480962186136d6823098a2c9c8991`. Title-page identity: corrected/expanded Abramsky--Jung author manifestation based on1994 printed chapter; retained numbering does not imply unchanged proofs. Physical/internal page positions match in the read intervals. Author locators and existing-image hashes are in `source/references/p10-domain-theory/SOURCE.md`.

Actually read primary text: p1; pp5--7,10--57,68--79. This includes section2, sections3.1--3.3, lattice-like discussion through the opening of4.2, and recursive equations through the opening of5.4. Existing page18/page47 pixels were inspected; no new render or network acquisition was performed. Remaining pages are unread, not silently credited.

## Authored results

Reader: `handbook/parts/p10/domain-theory-and-recursive-models.tex`.
Annex: `handbook/annex/p10/domain-theory-and-recursive-models.tex`.
There are14 reader proved results and14 reciprocal annex arguments. They are written editorial proofs, not independent acceptance.

- `domain-basis`: exact way-below properties, directedness of whole basis approximants, compact inclusion, intrinsic continuous/algebraic conditions and finite interpolation. Source Props2.2.2,2.2.4,2.2.7, Lem2.2.15, Cor2.2.16, pp18--25.
- `domain-basic-examples`: powerset finite compacts/non-chain directed family with no cofinal chain, partial-function graph unions/compacts, unit interval's exact approximation and a pointed noncontinuous two-leg dcpo. Source pp13,18--21, Ex2.3.9(6),(19), pp31--32.
- `domain-ideal-completion`: round ideal object, exact approximation witnesses, compact principal ideals and actual inverse basis-recovery maps. Source Def2.2.20--21, Props2.2.22,2.2.25, Cor2.2.26, pp26--28.
- `domain-scott-topology`: topology/order recovery, exact continuity equivalence and basis opens. Source Def2.3.1, Props2.3.2,2.3.4--6, pp29--31.
- `domain-function-space`: directed pointwise function dcpo, strict map closure, product approximation/bases, actual evaluation/currying/composition. Source Prop2.1.18 and sec3.2.1--2, pp16,42--44. No blanket CONT/ALG cartesian closure.
- `domain-least-fixpoint`: complete omega-iteration and least pre-fixed bound; continuous fix operator/parameterization; editorial partial-graph factorial calculation. Source Thm2.1.19, Ex2.3.9(17), pp16,32.
- `domain-fixpoint-principles`: admissible induction and strict uniformity, source Lem2.1.20--21, p17.
- `domain-failed-premises`: explicit missing-bottom, missing-continuity, inadmissibility and non-strict-map failures. Source pp15--17 and Ex2.3.9(13), p32; the monotone example does not deny separate monotone fixed-point existence.
- `domain-constructors`: lifting/new-old bottom distinction, exact sum/smash directed objects and bases, strict-only sum coproduct, lifting adjunction, smash strict-currying/unit/coherence. Source sec3.2.3--5, pp44--45.
- `domain-algebraic-functions`: exact finite-step compact function basis in the algebraic bounded-complete case, bounded completeness and countable bases. Source pp54--57, Prop4.1.5; not the unrestricted function-domain claim.
- `domain-bilimit`: explicit commuting tuples/e-p maps, both mediators and uniqueness, identity-supremum cocone criterion, continuous/algebraic bases and compacts for expanding sequences. Source Def3.1.15, Def3.3.6, Thm3.3.7, Lem3.3.8, Thm3.3.11, Ex3.3.12(15), pp39,48--53.
- `domain-mixed-embedding`: actual typed variance passage/functor laws, synchronized chain-bilimit preservation and checked function-space local continuity. Source Def5.2.5/Prop5.2.6, pp72--73.
- `domain-recursive-solution`: seed-dependent expanding sequence and actual inverse fold/unfold suprema with both leg equations. Source Def5.2.1/Lem5.2.2, pp70--71.
- `domain-recursive-examples`: editorial prefix-stream isomorphism/truncation bilimit and flat-natural seeded nontrivial omega-algebraic reflexive solution; separate one-point solution, and semantic beta/eta. Source constructors/bilimits/genuine-equation example, pp20,43,48--53,68--72. No operational adequacy/full abstraction inferred.

## Intakes and seams

`handbook/bib/intake-p10-domain-theory.bib` has separate corrected-author and printed-identity keys; all current theorem citations use the author manifestation actually read. `handbook/registry/symbols-intake-p10-domain-theory.csv` uses the seven-column header and local typed symbol roles.

Root owns shared routing/maps/intake merge. Reader seam: immediately before the host's final theorem/definition register, after source03, insert `input{parts/p10/domain-theory-and-recursive-models}`; the block opens its own section and does not reparent the earlier Topoi subsection. Annex seam: after the existing final P10 annex input, insert `input{annex/p10/domain-theory-and-recursive-models}`. No shared route or generated register was edited by this writer.

## Exact continuation

1. Source2 still owes the full closure-system group, abstract-basis universal extension and approximable-relation equivalences, countable alternative conventions, and remaining exercises. Reading all section2 is not reconstructing all its units.
2. Source3 still owes general retract/adjunction/quotient groups and exercises; directed-index expanding systems and general-adjunction bilimits; source cocompleteness proofs and all infinitary distinctions. The chain e-p bilimit here is complete at its stated scope, not that broader group.
3. Source4 still owes general L-domain/BC/lattice cases, bifinite/FS/coherence and the full category hierarchy. The algebraic bounded-complete function theorem is a bounded completed case.
4. Source5 still owes parameterized/simultaneous/Bekic constructions, invariance/minimality, initial/final universal properties, free mixed-variant algebra, and structural/admissible induction/coinduction. The written5.2 variance passage and seed-based fold/unfold construction do not discharge those stronger obligations.
5. Read and reconstruct still-unread pages8--9,58--67,80--167, including remaining chapters4/5, equational theories/powerdomains, domain logic/topological equivalences, further directions, literature and apparatus. Full ED26-SRC-028-501 stays open.
6. Acquire/read/reconstruct/compare printed SRC028-001 and separate PostScript, and all allocated Gunter, Gunter--Scott, Mosses, Tennent and Wagner sources. Preserve their operational adequacy/full-abstraction and effectivity assumptions instead of inferring them from domain equations.

No children, independent reviews, tests, builds or manuscript renders were used. Source fidelity, mathematical/publication reviews, static integration, bibliography/symbol merge, build, visual inspection and admission are later unfinished gates. This authoring provenance is outside the reader derivation, not manuscript progress commentary.

## Continuation block: canonical recursion and invariance

This block narrows the earlier block's source5 residual through actual new writing, not through reclassification. Files: `handbook/parts/p10/domain-recursion-and-invariance.tex` and `handbook/annex/p10/domain-recursion-and-invariance.tex`. They depend on the frozen first packet without changing it. Its hashes at continuation start were reader `c78de54784452a1df9233f2fd173493635ad7587973da1b8d20ccef0fd156cd1` and annex `cea1f2e1debb6d82bae02440e5ae6bb9f6761cd5af9c6626692b4ca016207dda`.

New primary text actually read: corrected/expanded author PDF pp68--85, including the full section5 text and exercises; p85 is the next section's boundary/context, not a reading of chapter6. Exact source bytes remain SHA `74adfbb57ae86a8b24e5afae312ffa77138480962186136d6823098a2c9c8991`. Existing pixels inspected without new rendering: page78 SHA `17ff809c9d51dc4749531840c59a3f9c0f67148484f25b486939a67f0653bb11`, page83 SHA `3263ee20d4163245801212ac134428e03cd7c34274136fa4450cae9aee6efa34`.

There are14 new reader proved groups and14 reciprocal annex arguments, all with new `thm:p10-domain-invariance-*` identities:

| Suffix | Source scope and exact new construction/proof |
|---|---|
| `least-hom` | Lem5.3.1, pp74--75: actual least hom functional, strict-on-hom-dcpo precomposition comparison, exact composition and least kernel |
| `covariant` | Thms5.3.2--3, pp75--76: iterates equal e_n p_n; identity is least canonical endomap; actual minimal embedding/projection; all invariance implications with solution structures retained |
| `initial-final` | Thms5.3.4--5, p77: strict initiality, unrestricted finality including non-strict coalgebras, and the separate strict-only final regime; existence/uniqueness proved via typed functionals and strict hom-dcpo comparison maps |
| `least-pairs` | Lem5.3.6 and corrected comment, pp77--78: least paired functional; every finite composition approximation checked before diagonal directed-supremum passage; mixed idempotent kernel |
| `mixed` | Thms5.3.7--8, pp78--79: mixed canonical identity and actual comparison pair; conjugation, minimality and strict-endomorphism uniqueness, including the extra least-identity order step after h squared equals identity |
| `free-mixed` | Thm5.3.9, p79: actual strict paired universal functional and unique comparisons; its nth iterate is (q_n h,k q_n), proving uniqueness rather than asserting it from fold/unfold inverses |
| `parameters` | Prop5.2.7, pp73--74: all stage objects/maps, cocone equations, increasing mediator family, identity/composition/local continuity, both natural structure equations |
| `mixed-parameters` | pp72--74 and four-slot extension from Ex5.4.11(9), p84: paired parameter/recursive diagrams, correctly signed maps r_n/s_n, all four embedding/projection compatibilities, mixed functor laws/local continuity/structure naturality; this is a supplied extension argument, not an unprinted source quotation |
| `bekic` | p74 and Ex5.4.11(4), p83: least value pair for non-strict continuous f/g and general strict domain nested/simultaneous equivalence by an actual initial-algebra construction and uniqueness proof |
| `resumptions` | Source5.1.2, pp68--69: exact S -> (S sum S times R) object and strict functor action, local continuity, canonical strict universal properties, returned/continuation observations and infinite iterative resumption; no operational adequacy inferred |
| `relational` | Prop5.4.2 and Thm5.4.5, pp80--81: map predicate actually admissible; typed action variance; full arbitrary finite-arity comparison argument through least identity |
| `actions` | pp81--83: actual unary logical and binary extensional actions for lift/product/sum/smash/function/strict-function constructors; all admissibility/compatibility and variance-signed composition clauses proved |
| `induction-coinduction` | Thms5.4.7,5.4.9/Cor5.4.10 and source5.4.1, pp79--83: logical structural induction and simulation characterization; finite-expression basis induction with explicit countability premise; concrete two-point admissible stream simulation |
| `failures` | Ex5.4.11(5)--(7), p83 and earlier compact-basis conventions: equation isomorphism without initiality, non-strict uniqueness failures, uncountable compact-basis counterexample, actual distinct initial set algebra/final set coalgebra constructions |

The source5.2.3 parameter assertion is not represented by an object-level FIX name alone. The source5.3 universal-property group is not inferred from a seed-dependent isomorphism. The default unrestricted and strict hom regimes are explicitly different; in particular the resumption coalesced-sum functor is defined on strict morphisms and is not silently extended to arbitrary maps.

### Correction and proof expansion provenance

The author PDF's p83 displayed binary lifting formula uses carrier `D^2` despite describing lifting. The active new reader/annex use the well-typed carrier `(D_bot)^2`, a new-bottom-first clause and explicit old-element injections. Source bytes are preserved. The logical/extensional action definition is kept distinct from applying F to a relation as a domain object.

The p78 mixed uniqueness outline with H(u)=h u h first yields h squared equals identity. The new proof additionally uses that identity is the least fixed point to obtain identity below h, then h below h squared, so h is identity. The corrected-author least-pair composition comment is supplied as a complete finite-approximation induction and directed-limit argument. These are source-grounded editorial proof expansions, not claims that the short source prints every step.

### Integration and exact residual after this block

Root reader seam: immediately after `input{parts/p10/domain-theory-and-recursive-models}` and before the final register, insert `input{parts/p10/domain-recursion-and-invariance}`. Root annex seam: immediately after the corresponding first-packet annex input, add the new annex input. No shared route, style, canonical/map or receipt file was edited here.

Bibliography intake `intake-p10-domain-invariance.bib` intentionally introduces zero duplicate source entries and points to the already supplied author key. Symbols intake `symbols-intake-p10-domain-invariance.csv` records the new local roles for root merge.

The named source5 main-text parameter/Bekić, covariant/mixed invariance/minimality, initial/final/free mixed universal-property and admissible relation induction/coinduction dependencies now have actual written arguments at the explicit scopes above. Remaining source5 obligations include exact normal-form/conversion developments referred to chapter7.3, source exercises not supplied here (ideal-completion local-continuity failure, natural-number equation variants, monotone-function reflexivity, lazy Y-combinator interpretation), and the logical/extensional **relation-action** lift for the four-parameter fixed-point functor in Ex5.4.11(9); the paired object/map functor extension here is not that relation-action proof.

All other residuals from the preceding block remain: full section2/3 reconstruction/exercises, general directed-index/adjunction bilimits, full hierarchy/L-domain/bifinite/FS/coherence, equational theories/powerdomains/domain logic/further directions/literature/apparatus, original printed/PostScript and Gunter/Scott/Mosses/Tennent/Wagner variants, and their operational adequacy/full-abstraction assumptions. Current combined technical primary reading is p1; pp5--7,10--57,68--85; still-unread technical ranges include8--9,58--67,86--167. No complete167-page source or catalog scope is discharged by these two packets.

No new children, source edits, reviewers, tests, builds or renders were used. Independent admission and all later integration/static/build/visual gates remain unfinished.
