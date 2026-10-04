# Mac Lane--Moerdijk presheaf/internal semantics: source-specific authoring

Unit: ED26-REQ-N-d-023-03. Date: 2026-10-02.

## Scope and actual reading

The queue's bounded source-specific obligation is the elementary/presheaf
topos foundation, classifier/exponential/power-object interface and internal
intuitionistic higher-order semantics, together with all generalized-element,
site/sheaf and presheaf-stage Kripke--Joyal clauses. The original overview
ceiling excludes a sheafification or geometric-morphism development.

Read handbook/CONVENTIONS.md and spec/EDITION-2026-CONTRACT.md completely;
read the actual unit in completion-work-queue.jsonl, its five prerequisite
allocations, and current presheaf body and reciprocal annex files. The foundation
proofs are reused by precise interface and reciprocal link, not counted as
already proving the missing semantics.

Primary: Mac Lane and Moerdijk1992, institutional Pisa scan at
`tmp/pdfs/p10-topos/mac-lane-moerdijk-sheaves-in-geometry-and-logic-institutional.pdf`.
Current hash, independently recomputed in the separately allocated continuation:
`A30AE90087DF702F6E48A705FF313CEB7821FAE55AB3CF43E255D4DCD7B95825`.
The existing source qualification recorded 638 physical pages and physical
one-based PDF page = printed page +11 in the inspected extent.

Directly inspected existing source images here:

- I section4 pp35--38, image names mlm-classifier-046 through049;
- I section6 pp44--47, mlm-exponentials-055 through058;
- I sections8--9 pp50--61, mlm-logic1-061 through072;
- III section8 pp147--149, mlm-sheaf-quantifiers-158 through160;
- IV sections8--9 pp198--209, mlm-heyting-topos-209 through211,
  mlm-heyting-topos-tail-212 through214, mlm-base-change-215 through219,
  and mlm-base-change-tail-220;
- VI sections5--7 pp296--318, mlm-logic6-307 through318,
  mlm-forcing-319 through328, and mlm-presheaf-clauses-329.

VI pp313--314 are an additional read beyond the prior 2026-09-06 verification
note, to complete IAC through its last argument on p315. No whole-book reading
credit is taken; unrelated adjoining arguments on images remain outside this
presentation. The prior source note remains distinct historical evidence.

## Delivered components and source/proof boundaries

Body: `handbook/parts/p10/presentations/n-d-023-source-03.tex`.
Annex: `handbook/annex/p10/n-d-023-source-03.tex`.
No shared driver, host paragraph, calculus sheet, canonical registry,
generated consumer or admission record was edited by this author.

1. Foundation bridge links the actual five completed host constructions to
   the source's I section4 classifier and I section6 exponential formulas.
   Reused foundation interfaces preserve small base, fixed universe,
   canonical images, empty components and the degenerate empty-base case.
2. `thm:p10-mlm-presheaf-predicates` / `annex:p10.mlm.1`: complete
   restriction-stability and residuation proof, pullback preservation of
   Heyting operations, both all-arrow adjunctions, Frobenius and both
   Beck--Chevalley identities, with direct component proofs. Sources:
   I section8 Proposition5 (18)--(19)p56, III section8 (15)p148,
   IV section9 (2)p204, Proposition1p205, (13)p209.
   The source's further component verification on p56 is left to the reader;
   this annex supplies it rather than misdescribing the printed proof.
3. `thm:p10-mlm-internal-representation` / `annex:p10.mlm.2`: full
   representability proof for internal Heyting and power-object quantifier
   maps on every parameter object, including internal Frobenius and universal
   BC checks assigned to Exercise9 in IV section9. Sources pp201--209.
4. `def:p10-mlm-language` gives every semantic constructor in VI section5
   pp298--301, in explicit common typed contexts. The source's free-variable
   context merging is bridged by projections; arbitrary empty unused types
   are not silently deleted. `thm:p10-mlm-contextual-semantics` /
   `annex:p10.mlm.3` proves capture-avoiding substitution, quantifier BC,
   comprehension recovery, beta/eta identities, equality replacement,
   predicate/function extensionality, and validity/universal closure.
5. `thm:p10-mlm-generalized-clauses` / `annex:p10.mlm.4` supplies all
   generalized-element clauses, persistence, epimorphic descent, equality
   and membership, including the source's omitted negation and abbreviated
   membership checks. Sources VI section6 pp303--310. The full clause
   derivation explicitly imports the earlier generic elementary-topos
   structural package as `cited=MacLaneMoerdijk1992`: IV sections6--7,
   IV section8 Theorem1 and IV section9. This is a cited generic-topos
   prerequisite, not a new complete proof of the whole IV development.
   The needed presheaf ingredients have current concrete proofs.
6. `thm:p10-mlm-site-clauses` / `annex:p10.mlm.5` supplies all site clauses
   and the trivial-topology presheaf specialization. It expands the source's
   first proof route via explicit local closure of subsheaves and the
   all-arrow existential/universal adjunctions, including source reader
   verifications. Sources III section8 pp147--149 and VI section7pp315--318.
   The second source proof route imports generation and cover-detection by
   sheafified representables from III section6 and III section7Corollary7;
   those dependencies are identified separately, not treated as a new proof
   of sheafification. The associated-sheaf adjunction is an explicit
   established-site setup boundary, respecting the original overview ceiling.
7. `thm:p10-mlm-internal-epi-boolean-choice` / `annex:p10.mlm.6` supplies
   the complete internal epi, Boolean and IAC translation examples from
   VI sections5--6 pp301--315, including both Boolean directions and the
   IAC proof continuation. It distinguishes internal local right inverses
   from external global splitting.
8. Worked/failure cases: two-object arrow stage calculation; failed
   componentwise complement and forall; explicit sieve values; arbitrary
   generalized disjunction without a whole-object disjunct; an equivariant
   epi without a section; empty-context failure of deleting an unused empty
   type; empty-site-cover bottom; dense-topology refinement clauses.

## Source corrections retained

- III section8p147 prose introduces y as in E(c); the output is a subobject
  of F and y belongs in F(c). Correct formulas use target values.
- IV section8p201 prose gives i_A target E/B; its diagram requires E/A.
- IV section9p204 says V ranges over Sub(A); Frobenius uses V in Sub(B).
- VI section5p300(5) changes the parameter name Y to U; one parameter name
  is used consistently in the manuscript.
- Universal-image comparisons restrict the target along every u:d to c,
  avoiding the separate2007 source's printed mismatched-stage formula.
  No independent2007 presentation is credited to this1992 unit.

## Dependent typed-HOL continuation and exact remaining boundaries

N-d-023-S03-TASK02 states exactly: **"Give the full assigned typed higher-order
language, interpretation and intuitionistic soundness."**

The first block supplied the semantic language/interpretation but left the
formal rule specification and soundness owed. A separately allocated
continuation now supplies that dependency using **Lambek--Scott1980**, not
pretending that MLM1992 itself prints the rules or that LJ is typed HOL.
New sheet: `handbook/registry/calculi/p10-internal-hol-lambek-scott1980.tex`.
It preserves the source's product/power grammar, Leibniz-defined equality,
four structural rows, fourteen directions of the seven logical adjunction
clauses, six nonarithmetic nonlogical axioms, three optional Peano axioms,
and the independently optional Boolean axiom: 28 displayed rows.

Source: `source/references/internal-topos-hol-source/lambek-scott-1980-type-theory-free-topos-author-scan.pdf`,
first-party author-hosted journal-layout scan, *Journal of Pure and Applied
Algebra*19(1980),215--257. Its SHA256 was independently recomputed in this
continuation and matches `3ADB5D6B2BEE0DEDC18611FD1EC9FCDD6C097F1B5072EFBB6070E190A81ED55F`.
Read the actual existing images for §1pp216--218 and full extracted p219;
read §5's actual interpretation pp240--242 and printed p215 for identity and
its explicit NNO scope. Incidental pp243--246 were read
while locating that passage, but their free-topos proof is not adopted as
proved or comprehensively reviewed. No whole-paper reading credit is taken.

Added reciprocal pairs:

- `thm:p10-ls1980-leibniz-equality` / `annex:p10.mlm.7`: generic contextual
  interpretation/substitution and full diagonal-versus-Leibniz bridge. Its
  parameterized singleton is built categorically from the diagonal, avoiding
  a circular helper defined using the equality being established.
- `thm:p10-ls1980-hol-soundness` / `annex:p10.mlm.8`: validation of every
  source structural/logical/nonlogical row followed by induction over finite
  derivation trees. The full source uses variable-set indices; generalized
  assignment families interpret arbitrary indices without infinite products
  or deleting unused empty types. For finite declared contexts the test is
  proved equivalent to ordinary subobject inclusion. Quantifier side
  conditions make absence of the bound variable from p's free variables
  explicit; it need not be absent from a possibly infinite declared index.
  The source's printed adjunction clauses taken without that binding guard
  would be unsound, and the body supplies a two-element failure case.
  Arithmetic is explicitly optional: zero separation, successor injectivity
  and predicate induction are derived from the NNO recursion property,
  including parameterized/slice recursion. The actual constant presheaf NNO
  is constructed. Boolean extension is separately conditional on Booleanness.
- `thm:p10-ls1980-exponential-graph-bridge` / `annex:p10.mlm.9`: proof that
  source-definable total single-valued relations in P(A×B) represent B^A on
  every parameter object. It proves the evaluation/lambda graph and beta/eta
  bridge without introducing primitive function/lambda syntax into pure L1.
  Naming interpreted objects/arrows uses the source's explicitly applied
  extension on p242. Pure-language syntactic conservativity, normalization,
  completeness and free-topos metatheorems are not claimed.

The source-qualified dependent TASK02 grammar/interpretation/soundness
components are now written, subject to parent integration and independent
admission. This does **not** close the distinct Lambek--Scott1986 or
Boileau--Joyal1981 source facets; their exact technical bodies remain
unqualified in the source-prerequisite record. The 1983 equality-primitive
presentation is not mixed into the 1980 connective-primitive one.

The generic-topos structural package remains accurately cited, not locally
reproved. Any independently allocated full-proof obligation for those
generic prerequisites remains owed; the presheaf proof package does not
assert a proof for all elementary topoi merely by changing its title.

## Verification and execution boundary

Author read each generated mathematical proof against its matching statement
and source clauses while constructing the reciprocal pairs; this is author
reasoning, not independent admission. No reviews, builds, manuscript renders,
prose tests, payments, logins, contact or security bypass were performed.
The assigned scope prohibited those activities.

The initial body/annex apply_patch calls returned success. Subsequent default
exec_command calls repeatedly failed before process start with
`helper_unknown_error: setup refresh had errors`; a filesystem read tool also
returned Internal error. The approved `require_escalated` mechanism succeeded
in the separately allocated continuation, without bypassing access controls.
Current body/annex/sheet are reread and hashed at the end of that continuation;
their final hashes are returned to the parent rather than embedded in this
self-hashed note. No build, review, manuscript render, prose test or admission
is implied by those ordinary author checks. Shared integration remains parent-owned.

## Root reader/canonical integration

Root placed this source subsection inside the actual topoi host and routed
the matching nine-item annex plus the separately attributed1980 rule sheet.
The25 typed rows are now canonical with explicit roles for external adjoints,
internal power maps and object-versus-term comprehension. Published glyphs
were preserved; CSV math wrappers and allowed precedence tokens were repaired.
MacLaneMoerdijk1992 was enriched at its existing canonical identity and the
verified JPAA19(1980),215--257 LambekScott1980ITT identity added. The prior
TCS journal guess in a dispatch message is not the canonical source identity.
No1981/1986 facet or generic structural theorem is closed by that dependency.

The incoming affected-set reference/citation/route/schema checks passed,
without a manuscript build/render or independent review. Mathematical source
fidelity, publication rights, full-proof residuals and admission remain distinct.
