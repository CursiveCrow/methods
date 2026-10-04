# ED26-P07-monotonicity-0001: source reading and authoring checkpoint

Date: 9 September 2026. This is an authoring record, not an independent
review or acceptance.

## Current standing after the second authoring block

The complete corrected source treatment has now been written in the body,
annex and rule sheet. The original general eta rule, strict subtype
applications, all eight inequality rules and universally interpreted
premises are preserved. The indexed functional realization and canonical
completeness proof are integrated. Conversion coherence is proved by
comparison-directed long elaboration; it is not an additional model axiom.
The corrected polarity theorem uses the elaborated occurrences at a
specified comparison type, with both signed cases and the absent-variable
case proved by the complete occurrence-preorder construction.

There are 13 reciprocal body/annex result pairs, with no source-wide
sketch or conditional soundness status remaining. The body has 648 lines,
the annex 859 lines, the registry 26 rules and the symbol intake 29 rows
at this checkpoint. The five extra registry rules are the explicitly
unmarked auxiliary parallel beta-eta reduction used to prove the ordinary
long-form input. A bounded identity check found all 13 reciprocal pairs
matched. The final author read-through covered the actual new LaTeX,
including the common-substitution case in which an argument contains
distinguished occurrence colors.

The current state is **authored and ready for lead integration**, with
independent source/topic/adversarial review, the whole-book build and output
checks still belonging to the later consolidated batch. The source note's
first-block statements below are retained as construction history and
superseded only as to their incomplete proof standing.

### Integrated construction contribution

Read the complete source-model contribution and its completed Section 7:
spec/research/monotonicity-term-model-construction.md, 35927 bytes,
SHA-256 D83AF28AC0AFE4E64EB25861E2C9E26EE1581FE818735FA7A5F500250153BD21.
The primary author transcribed the full mathematical argument into the
owned LaTeX and checked its indexing and proof interfaces.
This was constructive coauthoring, not independent review.

### Exact additional ordinary normalization source

Peter Selinger, *Lecture Notes on the Lambda Calculus*,
arXiv:0804.3434v2, 26 December 2013:
https://arxiv.org/pdf/0804.3434v2.

- Local:
  source/references/p07-monotonicity/selinger-2013-v2-lambda-notes.pdf
- SHA-256:
  9C4AD820D6A48E7D926996F04100830B86F4131BCA0CAB4BF1D6349A2182481F.
- The v2 history, full title, 120-page extent and exact passages were
  checked. Only Sections 4.2–4.4, printed pp. 28–36, and Sections 8.7–8.8,
  printed pp. 80–84, are selected as this bounded supporting source.
- The complete beta-eta parallel proof in Section 4.4 was read, including
  every application/abstraction overlap and the substitution lemma.
  The long-form definitions and Proposition 8.7 were read.
- The source leaves long-form uniqueness as an exercise. The annex
  supplies it: ordinary beta-eta confluence gives a common short normal
  form; finite eta-long expansion is invariant under eta contraction
  of beta-normal terms and fixes long terms.
- The manuscript specializes to the ordinary arrow-only fragment with
  inert constants; it does not import System F's polymorphic syntax.
  The full source book is not newly selected.

The existing P7 strong-normalization result is explicitly beta-only.
It is used only for that beta normalization input. The beta-eta
Church-Rosser argument and the long-form uniqueness argument are now
actually supplied in annex:p7.monotonicity.ordinary-long. No beta-only
theorem is credited with proving eta confluence.

### Component completion

- LR002-C1: marked types/orders, coherent semantic domains, occurrence
  syntax, all interpretation clauses and signed substitution completed.
- LR002-C2: complete intrinsic typing grammar, conversion and inequality
  rules with type/freshness conditions and universal-premise semantics
  completed; the finite substitution and strict-subtype extensionality
  arguments are in the annex.
- LR002-C3: automatic conversion coherence, indexed actual-function model,
  all-valuation canonical completeness, soundness, and the corrected
  comparison-normalized polarity converse completed.
- LR002-C4: the source's mathematical and language examples, lexical
  replacement, exact-count failure, local-premise failure and explicit
  coercion counterexample completed.

Ordinary beta strong normalization remains the existing upstream P7
obligation; this chapter neither changes its earlier proof status nor
confers independent acceptance on it. The benchmark Natural Logic
presentation remains a separate source treatment and is not merged into
this 2017 presentation.

## Authority and files

Read before authoring:

- spec/research/edition-2026-authoring-resumption-2026-09-09.md
- handbook/CONVENTIONS.md
- spec/EDITION-2026-CONTRACT.md
- spec/coverage/edition-2026/added-reasoning-units.jsonl:
  ED26-P07-monotonicity-0001
- the research skill and the PDF skill.

Owned files:

- handbook/parts/p07/monotonicity-inference.tex
- handbook/annex/p07/monotonicity-inference.tex
- handbook/registry/calculi/p07-monotonicity.tex
- handbook/bib/intake-p07-monotonicity.bib
- handbook/registry/symbols-intake-p07-monotonicity.csv
- this source note.

The lead owns the drivers, style and canonical bibliography/symbol registry.
No owned files were routed or merged into canonical shared records.

## Primary source acquisition and complete read

Thomas F. Icard, Lawrence S. Moss and William Tune, *A Monotonicity Calculus
and Its Completeness*, Proceedings of the 15th Meeting on the Mathematics
of Language, London, 13–14 July 2017, pp. 75–87.

- Publisher metadata: https://aclanthology.org/W17-3408/
- DOI: 10.18653/v1/W17-3408
- Free publisher PDF: https://aclanthology.org/W17-3408.pdf
- Local: source/references/p07-monotonicity/icard-moss-tune-2017.pdf
- Bytes: 343916.
- SHA-256: CE574675AED06937F7F11BC693344DE1DAE87E621D001AC39C52F303F5DC0186.
- PDF information: 13 pages; PDF 1.5; no encryption; title and authors
  match the paper. The title page spells the first author's name Thomas F.
  Icard; ACL's metadata shortens it to Thomas Icard.
- Complete layout extraction:
  tmp/p07-monotonicity/source-layout.txt.
- All thirteen pages, Sections 1–10 and References, were read through the
  complete extraction. Source Figures 1–4 were also inspected visually at
  physical pages 2, 5, 10 and 11; images are in tmp/p07-monotonicity/.
  This was source reading, not manuscript rendering.

The selected entire-paper extent remains fixed. The original eight
inequality rules are Ref, Trans, Point, Mono, Anti, Pres, Equiv and Func.
The current rule sheet also explicitly displays premise leaves, the four
term-formation rules, and the reflexive/symmetric/transitive closure of the
alpha/beta/eta/Xi/Cong conversion relation. No source rule is retired by
the partial status of the adequacy proof.

The source's premises are universal over assignments. The source's
Remark 9.4 changes the quantifier order in a proposed alternative relation;
that alternative does not justify Func. The chapter states the original
universal interpretation and supplies a concrete local-premise failure.

## A later primary error notice

A related paper by Moss and Icard supplies independent bibliographic
confirmation that the 2017 source needs correction:

- *A Completeness Result for Inequational Reasoning in a Full Higher-Order
  Setting*, arXiv:2202.08725v1, 17 February 2022.
- https://arxiv.org/pdf/2202.08725v1
- Local:
  source/references/p07-monotonicity/moss-icard-2022-v1-error-notice.pdf
- SHA-256:
  BCCCC044B6666A50DA0E8C289FBD65A956D1A934629E8BFBFBC02CC779AB6B5C.
- This 23-page related source was consulted only for its first-page
  scope, Section 3 p. 11, and references p. 23. A complete reading of the
  related paper is not claimed.

The exact relevant statement in Section 3, p. 11 is:

> (We should mention that [7] has an error
> that will be fixed in a follow-up publication.)

Reference [7] is the exact Icard–Moss–Tune 2017 proceedings paper.
Reference [6] is Icard–Moss, *Reasoning about monotonicity in a higher-order
setting*, unpublished manuscript, 2021. Its full body has not been acquired
or used here.

The 2022 paper's principal target is variable-free applicative terms and
full weakly complete structures. It is a different target and has not
replaced the selected 2017 calculus.

## Corrections made in active text

1. **Type-order recursion.** Source Proposition 3.4 defines R0 as identity
   and its following stage using only arrow pairs. A literal iteration
   loses base identities needed by later mixed-height arrows.
   The active structural characterization is proved directly by induction.
   Its optional staged description retains identities at every stage.

2. **Auxiliary join is partial.** Source Definition 3.3 compares arrow types
   with literally identical argument types. Arbitrary permitted
   type-refining substitutions need not have a join under this particular
   auxiliary operation. The active comparisons name an actual common
   upper type rather than applying an undefined join.

3. **Substitution refines occurrence polarity.** Source Lemma 6.2's exact
   product assertion is too strong for substitutions that refine head
   types. For f:b dot->b, x:b, and substitution f |-> g:b +->b, x |-> x,
   the old occurrence in f(x) has polarity dot and the occurrence in g(x)
   has polarity +. The proved active bound is new polarity <= old
   composed polarity in the marking order. When the old product is a
   sign, refinement retains that sign. This suffices for the signed
   subject-reduction statement.

4. **Semantic coercions.** The active prestructure definition explicitly
   supplies application coherence:
   pi_(sigma->tau,sigma'->tau')(F)(a)
   = pi_(tau,tau')(F(pi_(sigma',sigma)(a))).
   Fixed interpretations of constants and the variable clause are explicit.
   These are conditions used by the intended interpretation, not silently
   inferred from arbitrary functorial maps.

5. **Figure 2 example.** Following the source's occurrence grammar,
   lambda f.lambda x.-(0)(f(x)) has a negative outer marking:
   (r dot->r) --> (r dot->r).
   The free f occurrence passes through the negative second argument of
   subtraction. The x occurrence remains unspecified because the input f
   has unspecified variance. The active example states these computed
   markings directly.

6. **No marked-normal-form uniqueness claim.** An attempted proof using
   raw typed beta/eta normal forms was withdrawn before the checkpoint.
   Merely requiring exact-domain eta does not restore the argument when
   beta substitution can refine types. The active text retains the original
   general type-changing conversion relation and proves substitution
   stability by abstraction, congruence, applying the finite substitution
   images, and beta conversion. It claims termination by ordinary typed
   erasure, not uniqueness of the remaining marked binders.

7. **The raw normal-form converse has an actual counterexample.**
   The source model-construction worker supplied the following example,
   now proved directly in the active body/annex:
   rho=(b +->b), sigma=(b dot->b), x:b, and
   F:((rho +->b) +->b).
   M=F(lambda f:sigma.f(x)) is raw beta/eta normal with raw x-polarity dot.
   Its argument coercion restricts f to the monotone domain D_rho.
   Consequently M is monotone in x in every application-coherent structure.
   The active result thm:p07-monotonicity-coercion-polarity gives the full
   calculation and a nonvacuous full-model instance over {0,1}.
   This corrects the proposed raw converse by requiring the later criterion
   to expose coercions/expected types; it does not announce the whole
   completeness theorem false.

Correction provenance stays here; the reader is not told to repair an
earlier active formula.

## Exact obstruction to the discarded confluence strategy

Take rho < sigma, let Q(a) not eta-contract, and consider
E=lambda v:rho.(lambda a:sigma.Q(a))(v).
Unrestricted well-typed eta contracts E to lambda a:sigma.Q(a), whereas
contracting the inner beta redex gives lambda v:rho.Q(v).
For rho=(b +->b), sigma=(b dot->b), Q(a)=a(c) with c:b, these are
distinct typed normal forms.

Even exact-domain eta is insufficient as a raw confluence repair.
In
(lambda f:(rho +->b).lambda x:rho.f(x))(N)
with N:(sigma +->b) and rho<sigma, an inner exact-domain eta step followed
by beta produces N. An outer beta step first gives lambda x:rho.N(x),
where the eta binder is now strictly below N's actual domain.

These critical pairs defeat that strategy. They do not by themselves
refute the full consequence/completeness theorem.

## First-block proved prefix and then-remaining work

At the first-block checkpoint the body/annex contained eight reciprocal
result/proof pairs:

- structural type-order characterization and the partial-join upper bound;
- positive/negative occurrence implications, including all application
  marking cases and vacuous occurrences;
- type-refining substitution, polarity-refinement and semantic substitution;
- conversion stability under substitution and termination by typed erasure;
- universally valid premise instantiation and extensional comparison;
- order preservation of term-domain inclusions, conditional on the
  stated term-structure axioms;
- conditional soundness: the explicit conversion-coherence property (E)
  is a hypothesis, not a proved automatic property of all intended models;
- the concrete coercion/polarity counterexample.

The original type-changing rules remain in the rule sheet. Conditions are
not silently replaced by an exact-domain-only calculus.

The chapter also contains every main running source example: duration
thresholds, the complete real-term table, the mammals/marsupials/few/deftly
derivation, the real subtraction derivation, and the improper-integral
variance application. Lexical poodle/dog replacements, a neutral exact-count
case, and the local-premise failure supply reader lookup cases.
The analytical comparison theorem in the integral example is explicitly
an external premise. Ordinary simply typed strong normalization is linked
to its existing handbook theorem, whose separate proof completion/admission
is not conferred by this chapter.

Original scope remaining at that earlier checkpoint, now discharged by
the second-block constructions above:

- Prove conversion coherence (E) from the correctly specified intended
  structure conditions for arbitrary models. The proposed route is
  comparison-type eta-long elaboration; raw typed eta contraction is
  not an adequate justification.
- Integrate the complete comparison-indexed functional term realization,
  valuation lifting and canonical completeness proof from
  spec/research/monotonicity-term-model-construction.md when the model
  worker publishes it. Its iota_tau must retain the comparison type.
- Supply the corrected coercion-aware polarity converse, with its exact
  normalization/representation hypotheses and full countermodel argument.
  The false raw-normal formulation is not to be restored.
- Complete the final author read-through after those proofs are integrated.
- Preserve the complete full-space completeness boundary of Section 10;
  the 2022 variable-free result is not a replacement.

At that earlier checkpoint LR002-C1 and C4 had substantive written
treatments, C2 had the displayed grammar/rules and universal-premise
interpretation, and C3 was partial. The unit was then partly authored.
The current completion standing is the second-block statement above.

## Checks and handoff

The actual LaTeX body, annex and rule sheet were read through during this
block, with corrections applied directly. The finite coercion and
exact-count cases were reasoned through explicitly; no prose-mirroring
software tests were created. The final identifier/intake check is a bounded
structural construction check, not independent acceptance.

No manuscript build, render, independent review, driver edit or canonical
intake merge was performed. Source PDF image inspection is recorded above.

The final bounded structural check found 8 proved body targets, 8 matching
annex items, zero unmatched reciprocal targets, 21 rule-sheet entries and
24 parsed symbol-intake rows. The body has 539 lines and the annex 301 lines
at this checkpoint. These counts include the explicitly conditional
soundness result and do not imply completion of the source-wide adequacy
or corrected polarity-converse obligations.
