# Coquand–Huet1988 original-body qualification and corrective bridge

Date: 2 October 2026. Owner: `/root/lambda_hol_metatheory_author`.
This records source qualification, proof construction and the separately
authorized reader-ready reconstruction listed below. It is not independent
admission or a whole-paper completion claim. No legacy host, shared driver
or canonical record is edited by this worker.

## Original manifestation actually acquired

Thierry Coquand and Gérard Huet, “The Calculus of Constructions,”
*Information and Computation*76(2–3), pp95–120 (1988),
DOI10.1016/0890-5401(88)90005-3. The actual held PDF is the 26-page
publisher-layout original rehosted by University of Illinois CS522:
<https://courses.grainger.illinois.edu/cs522/sp2016/TheCalculusOfConstructions.pdf>.

Held path:
`source/references/p07-coquand1988-qualification/coquand-huet-1988-publisher-layout-illinois.pdf`.
Bytes: 1,407,838. SHA-256:
`8b43060165c38d8e438ed85bed8ccdf10eecab283130c059883ad12d629e290e`.
PDF metadata title: `PII: 0890-5401(88)90005-3`; capture metadata2003.
Printed first page shows journal/volume/pages/year, exact title/authors,
1988 Academic Press copyright and journal ISSN. Last printed page is120;
26 consecutive pages cover95–120. Physical page = printed page−94.
Publisher-file byte identity against a current publisher fetch is not claimed.
This is not the distinct INRIA report530 (May1986), the 1985 EUROCAL
paper, or the separate Geuvers1994 proof source.

Primary identity corroboration:
<https://pauillac.inria.fr/~huet/bib.html>, item33, explicitly separates
the 1986 report and final 1988 journal publication;
<https://rocq-prover.org/papers/the-calculus-of-constructions> supplies the
1988 journal identity and abstract. The article's received/accepted dates
in1985 do not alter its printed1988 publication identity.

## Prior records and route attempts

Read prior `spec/research/p07-new-content.md:1368` and its binding-key
discussion, the exact bib record `handbook/bib/handbook.bib:4645`, and
targeted DOI matches in acquisition-src035/src038. These established
bibliographic/reference evidence, not an actual original1988 body or
qualified rule comparison. No unchanged previously failed body route was
repeated from these records.

This block's ordinary access attempts:

- CORE publisher-connector PDF82038778: web reader and normal TLS curl
  returned403. Not retried with altered headers, tokens, proxy or CAPTCHA.
- Author bibliography's exact publisher link and DOI/publisher page: web
  reader errors; no publisher body acquired there.
- A targeted exact-title/PII search located the Illinois original publisher
  layout. Its normal TLS curl succeeded and its complete26-page PDF was
  retained and identified. No paid route, login, contact or security workaround.

## Actual source extent read

Sections1–3 pp95–105: the full base abstract syntax, one-based indices,
relocation/lookup, validity/typing rules, restricted versus full typed
conversion, and p104 logical reduction clauses. Sections4–5 pp105–110
were read for stripping, its candidate interpretation and normalization
standing; §§6–8 pp111–117 were read to distinguish normal-type/user-interface
variants and proposed recursive/universe extensions. The terminal printed
page120 was inspected for extent; full bibliography/whole-paper treatment
is not claimed.

Source pixels inspected: pp95–99,101–102,104–105 and110,112,120 in the
assigned capture directory. These are primary source renders, not manuscript
renders. The mathematical reconstruction does not rely on corrupted OCR for
the inference or relocation formulas.

## Exact original interface, not presumed two-sort notation

The article writes one literal `*`; it has no literal `Box`. Its raw logical
contexts Ao are products ending in*, and its objects Ai are indices,
applications, lambdas with object bodies and products with object bodies.
Both classes can annotate binders. An environment is a closed logical context
viewed as a list. It has separate Γ⊢Δ validity, Γ⊢M:P typing, and Γ⊢M≃N
typed equality. `*` itself is untypable. This is not a raw-sort bijection to
the PTS axiom `*:Box`; source validity must map to a target kind judgment.

The p102 full calculus replaces starred restricted rules by typed term
reflexivity, full lambda compatibility, simultaneous application compatibility
and arbitrary typed β equality. No primitive η or δ generator is present in
the read base rules. The p104 directed logical relation belongs to the
restricted presentation and has an explicit transitivity rule; it must not
be mistaken for exactly one ordinary full β contraction.

## Two literal printed defects, precisely separated

1. P98 relocation is described as replacing only free references k by k+1.
   The printed recurrence starts ξ0, increments the cutoff under a binder,
   but fixes k<i rather than k≤i for the one-based indices. Its literal image
   of the closed `(λx:*.1)` is `(λx:*.2)`. The bridge explicitly corrects
   this to k≤i (or equivalently starts at1 and retains k<i). It does not
   mutate or silently reinterpret the retained primary bytes.
2. P101's starred restricted “reflexivity” has literal conclusion M≃Δ from
   M:Δ. In `[A:*]`, it gives A≃*, whose images are distinct β-normal terms.
   It is not a β-sound equality rule. The same example also contradicts
   the paper's Lemma6: logical rank
   δ(A)=0 for its object variable, whereas δ(*)=1.
   P102's actual full replacement is M:N implying M≃M. The full bridge
   uses that printed replacement; it does
   not claim the unmodified restricted rule system embeds into CC.

These are visually inspected formulas, not deductions from OCR artifacts.
The immutable original is retained. Any corrected reader presentation and
the corresponding original-variant attribution remain lead-owned.

## Substantive bridge actually constructed

`spec/fragments/p12-har-lambda-hol-metatheory.tex`, W12a–d, supplies a faithful
normalization-preserving **forward** bridge for the full concrete/binding-
semantics presentation with explicitly corrected one-based relocation.
It does not claim a raw bijection or an inverse for the target's extraBox.

The construction sends source indices to the corresponding named variables,
bracket products to Π, annotated lambdas/applications homomorphically, and
source environments to ordered declaration contexts. It separately proves
relocation/lookup and substitution/removal commutation. Source validity Γ⊢Δ
becomes Γhat⊢TΔ:Box; source object typing becomes Γhat⊢TM:TP.

A complete joint derivation induction handles every validity/typing/equality
rule. Equality additionally transports either target-typed endpoint at the
same type, in both directions. This strengthened equality interface supplies
the separate sorted target type needed by conversion. Product/lambda cases
use actual target context conversion; application handles both replacements;
the root β reverse case uses typed source premises and uniqueness, not an
unsafe blanket expansion principle. The proof does not import unproved
original Lemmas3–4 from the 1985 thesis reference.

Every compatible source β contraction, including annotations, maps to one
target β contraction. Exact CC SN from W9 excludes an infinite source path.
Thus this authored corrective full-system argument proves the mathematical
annotated β normalization property required by a properly scoped legacy
consumer, while preserving the original source/version distinctions.

## Source-native proof standing and remaining integration boundary

P110 Corollary1 explicitly proves SN for the closed stripped image p(M), not by itself
for every annotation retained in M. P105 refers full constructed-term
normalization to reference15; p112 uses that result for a normal-type variant.
The independently reconstructed Geuvers1994 W9 argument and W12 bridge supply
the stronger annotated termination argument editorially. They must not be
misattributed as the literal complete proof printed in the1988 article.

Original1988 acquisition/readability for the needed interface is now supplied;
independent source admission and full-paper coverage remain separate.
An unchanged literal indexed system is **not** declared equivalent or closed:
the relocation defect and restricted reflexivity are explicit. Reader adoption
of the corrective full presentation, its appropriate original1988/1994 proof
attribution and exact P7 status/navigation reconciliation remain root-owned.
The qualification-only block made no P7, shared, canonical, bibliography,
registry, queue or driver edit. The subsequently authorized disjoint
reader-ready files are recorded below; that does not retrospectively
upgrade source admission or the literal misprinted calculus.

## Reader-ready standalone reconstruction, 14:45–15:25 UTC authoring block

Root authorized new disjoint files only:

- `handbook/parts/p07/presentations/coquand-huet-1988.tex` (starts with section;
  insertable before the legacy cited CoC result);
- `handbook/annex/p07/presentations/coquand-huet-1988.tex`;
- `handbook/registry/calculi/p07-coquand-huet-1988.tex`;
- `handbook/bib/intake-p07-coquand-huet-1988.bib`;
- `handbook/registry/symbols-intake-p07-coquand-huet-1988.csv`.

The intake shorthand is resolved under handbook/, as in the actual project
contract and other P7 intakes. The existing canonical CoquandHuet1988 key
is retained; its intake augments primary-capture metadata for lead
reconciliation. Geuvers1994Report9450 remains supplied by the separate
HAR intake, not duplicated under a new edition or a new key.

The body fully declares the one-star two-class indexed syntax, environment
versus logical-context roles, corrected cutoff/lookup and total object-argument
binder-removal substitution. It gives the actual core construction surface,
corrected restricted and full equality guards, and distinct raw compatible
beta and transitive directed-logical relations. Five typed sheets in the
owned registry contain every displayed rule. The named bridge imports only
the exactly identified CC structural results until the final use of its proved
normalization theorem.

Six body results have actual reciprocal annex proofs: index operations;
binding/substitution/one-step encoding; joint full validity/typing/equality
transport with both endpoint directions and a sorted conversion target;
corrected restricted-to-full rule inclusion; positive logical-path transport;
and full open annotated normalization. The inclusion supplies its source
application-generation lemma rather than assuming missing original metatheory.
All binder reverse endpoint cases transport the body back to the premise's
actual old context before applying equality induction.

The original closed stripped-image result is source-cited with its precise
proof-level/empty-environment domain. The original realization induction,
checking/rank sketch and later extensions are not promoted to proved local
results. The stronger annotated/open theorem is attributed to the editorial
binding bridge plus the separately proved Geuvers1994-source CC construction.
Active reader rules are mathematically corrected from their first occurrence;
the literal source defects and correction provenance remain in this note,
not reader instructions to repair a false displayed rule.

Reader scope delivered is the original base syntax and construction/equality
variants of §§1–3, the annotated normalization bridge, and the separate
stripping/source-proof/extension boundary. It is not a full reconstruction of
the original realization model, original checking proof, source development
examples or every §§6–8 extension. Those full-paper facets remain separate
obligations. This writer performs no legacy P7 status or consumer repair and
no driver/canonical integration. The owned annex parent directory was absent;
its exact scoped creation was granted before saving, with no unrelated move
or deletion. No child/review/build/manuscript render or prose test was run.

Author completion check: six proved body results have the six matching annex
items and back-references; one separately source-cited closed stripping result
has no invented local proof status. The final author read-through checked
source classes/scopes and object-argument substitution, both equality endpoint
directions, every common/restricted/full/directed rule guard, and the positive
path argument. The copied proof substitution notation was made consistent
with the reader's published-order `[N/x]Q`; the closed rho notation is
explicitly defined only in the empty proof-level interpretation. No build,
consolidated static suite, independent review or formal assistant execution
success is claimed. Files are released for lead routing/intake reconciliation
and the later consolidated gates; legacy P7/consumer repair remains lead-owned.

## Separate original-realization block

The released handbook body/annex/sheet/intakes were kept frozen. The proof
fragments were saved at the planned15:35–16:15UTC block boundary; final
metadata saving needed correction of a failed source-note patch context
and was completed later. No additional checking algorithm was authored.
New owned files: `spec/fragments/p07-ch88-realization-body.tex`,
`spec/fragments/p07-ch88-realization-annex.tex`, and
`handbook/registry/symbols-intake-p07-ch88-realization.csv`.

Original §§4–5 pp105–110 and the checking/normal-type boundaries pp104–105,
111–112 were reread. New source-only realization-12 through realization-17
PNGs preserve the old renders; pp107–109 were inspected as pixels. The
original PDF/hash is unchanged. No new bibliography key is needed.

Five actual reciprocal results are supplied: native saturated-set and
dependent-product closure/introduction; value/functionality/scoping/
substitution/equality compatibility; original proof-level realization
soundness; closed erased-imageSN; and consistency via the minimal saturated
marker-headed set. This is the original CLOSED-program/head-expansion
construction, not Geuvers reduction-closed candidates or annotation-retainingE.
The full functionality spaces require beta-invariant functions on proof
program domains; the restricted ones allow all such functions. Ambient
Cartesian environments and realized dependent D(Γ) are kept distinct.

The value interpretation is qualified by actual proof/constructor modes
and sort certificates from the previously proved structural source-image
transport. No annotatedSN or inverse adequacy is used. This expands the
original two-premise soundness statement and makes its implicit small-type
domain explicit for the closed image corollary. Constructor/type conversion
uses literal equality of sets; proof beta equality is proved on open
stripped syntax before closing, not inferred by an omega rule. It never
transports arbitrary saturated membership by beta equality.

Necessary domain clarification: a typed equality alone need not type all
raw product endpoints. In [A:*], full reflexivity of y:A under [y:A]
and product congruence derive [y:A]y equal to itself, although that product
is not a sorted type. The original interpretation was defined for derived
typed sequents; compatibility is therefore stated only where the endpoint
interpretations exist. Source conversion's actual sort certificates are
supplied by structural transport. This does not silently interpret an
untypable product as a candidate family.

The original rank/innermost and term-plus-environment-length checking
discussion retains its source method/outline standing and logical guards.
The normal-type variant depends on actual source generation, preservation
and conversion adequacy; no complete original full checking algorithm or
inverse source bridge is claimed. Those checking obligations remain open.
No frozen reader/shared/canonical edit, child/review/build/manuscript render
or prose test was performed.

## Original-checking block,17:40–18:20UTC

New owned working files: `spec/fragments/p07-ch88-checking-body.tex` and
`-annex.tex`, `handbook/registry/calculi/p07-ch88-checking.tex`, and
`handbook/registry/symbols-intake-p07-ch88-checking.csv`. Released reader,
legacy, P5 and shared/core files were frozen. No new bibliography key needed.

Reread full original pp104–105,111–112 as pixels in the existing
original-10,original-11,realization-17,original-18 captures. The qualified
original PDF and hash remain unchanged. Read current indexed grammar,
all5 existing rule sheets, actual forward transport/binding proofs, and
exactCC structural prerequisites in paragraph(a) of
`annex:p12.har.cc-normalization`, including the untyped top exception.

Eight reciprocal proofs now supply source context regularity/generation;
source thinning and dependent entire-suffix substitution in both ordinary
variants; rank/class invariance; the domain-rank countercase; raw beta-image
reflection/confluence; direct all-rule normal-variant CC transport; an
actual total sound/complete normal-variant checker, type correctness and
whole-normal-form preservation; and the normal-variant raw-step countercase.

Literal p105 domain-rank measure defect: Γ=A:*,a:A,C:* and
M=((λx:A.λB:*.B)a)C contracts innermost to (λB:*.B)C. Both source
logical guards hold, and the sole domain rank changes{0}→{1}.
This refutes that measure's decrease, not normalization itself.

The p112 no-conversion variant is separately specified by its exact8 rules
on the new sheet. Its checker validates contexts oldest-first, recurses on
proper original syntax, and normalizes only CC-certified typed results.
CC generation proves completeness on the annotation-normal source image,
including product-head recovery and equality of normal domains. This is
a constructed inverse on that declared domain, not an assumed inverse to
the earlier full bridge. It produces actual normal-variant derivations.
Its normalizer terminates by proved full annotatedCCSN, not erasedSN.

The normal variant is not raw-beta subject-preserving: in Γ=A:*,a:A,
K=λx:A.A and V=(λF:(Πx:A.*).λy:F a.y)K has typeΠy:A.A, but raw
contractumλy:K a.y has a nonnormal annotation and cannot be typed there.
Whole normal formλy:A.y is typed. Hence an unchanged ordinary-full raw
judgment cannot silently be called a normal-variant judgment.

Precise residual: full-source root-redex generation may expose argument
typeB while the literal lambda annotation isA, via converted function
product type. Target product injectivity gives raw beta equality of images,
but source conversion still needs an actual typed equalityA≅B. Source
substitution is supplied here; ordinary-full source type correctness,
compatibleSR and sorted
beta-conversion equality reflection, hence the checker for arbitrary
ordinary-full annotations, remain unsupplied. Restricted typed-equality
decidability is not inferred from raw normalization either. The complete
checker belongs to the explicitly declared p112 no-conversion variant,
not to a merely conditional full checker. A full-source annotation-normal
typing has the one-way normal-variant consequence through the proved
forward bridge and new completeness theorem; the converse ordinary-full
derivation is not assumed.

No children, independent review, build, manuscript render or prose test.
Only original source-page images were inspected. Root owns integration
and correction of earlier reader rank/method/status passages. Files are
released at the block boundary; SHA256 values are reported in the return.

## Reader adoption block,18:45UTC

The13 released proof pairs are now adopted, via apply_patch, in these
reader files:

- `handbook/parts/p07/presentations/coquand-huet-1988-realization.tex`
  and its matching annex path: five native realization pairs.
- `handbook/parts/p07/presentations/coquand-huet-1988-checking.tex`
  and its matching annex path: eight checking/rank pairs.

All four working originals in `spec/fragments/p07-ch88-*` are retained
unchanged at their release hashes. Proof labels, proof-status targets and
annex backreferences are preserved. The adopted native annex is unchanged
in substance; the checking annex changes only the source-historical word
“printed” in two already proved mathematical statements. No proof case is
deleted or promoted, and no conditional ordinary-full checker is adopted.

The owned core body now inputs the original rule sheet after all source
judgment/reduction definitions, then develops its binding/CC bridge and
annotated normalization. It inputs native realization immediately after
the stripping definition, and the checking section after the reconciled
realization/annotation/extension boundary. The checking body inputs the
exact8-rule normal-type sheet after defining that separate variant and
before transport and checking. Shared part/annex drivers, style,
canonical/baseline records and generators are root-owned and untouched.
The two new annex inputs still require root's shared-driver routing after
the original indexed-core annex.

The old cited duplicate `thm:p07-ch88-source-stripped-normalization` is
replaced by an alias on the actual proved
`thm:p07-ch88-native-closed-image` corollary, whose reciprocal target
remains `annex:p7.ch88.native-closed-image`. Thus that stable consumer
resolves to the closed proof-level image endpoint, not the annotated/open
normalization theorem. The original extra-premise realization statement
and article Corollary1's closed-image attribution remain qualified.
`def:p07-ch88-source-checking` is retained as the corrected logical
measure/checking-variants method in the checking section;
`def:p07-ch88-source-checking-boundary` aliases the current ordinary-full
dependency boundary. The existing annotated-normalization alias is unchanged.

Historical correction provenance: the article's p105 rank sketch asserts
an innermost multiset decrease for redex complexityδ(P). The independently
authored typed{0}→{1} countercase establishes that this precise assertion
fails. The reader now states the corrected measure boundary at the first
rank definition and supplies the countercase, rather than retaining an
active decrease assertion followed by a repair instruction. The obsolete
native checking outline and incomplete boundary are replaced coherently;
the source history is recorded here, not as a later contradictory apology.

Current reader proof scope: original closed-program/head-expansion
realization with its full native soundness/closed-image/consistency proofs;
ordinary-source context/generation/thinning/substitution and rank invariance;
raw source-image beta reflection; the complete p112 no-conversion
normal-type checker, actual type correctness and whole-normal-form
preservation; and the two typed countercases. Ordinary-full source type
correctness, sorted typed-beta equality reflection, compatibleSR and
checking for arbitrary full annotations remain explicit dependencies.
Restricted typed-equality decidability is not inferred from raw betaSN.

The actual latest core/fragments and adjacent reader passages were read
before and after adoption. Author read-through compared the13 statement
targets and reciprocal annex backreferences and checked the relocated
definitions/inputs and old aliases. No test, build, manuscript render,
independent review, child or generator was run. Original PDF/read extent
is unchanged. New source/bibliography intake is unnecessary; existing
unique realization/checking symbol intakes and checking sheet are retained.
Release paths and hashes are supplied in the return to root.

## Ordinary-full construction block,19:16–19:56UTC

New working artifacts only:
`spec/fragments/p07-ch88-ordinary-checking-body.tex` and
`spec/fragments/p07-ch88-ordinary-checking-annex.tex`. All adopted files,
earlier fragments/intakes and shared records stayed frozen. Existing
notation and CoquandHuet1988 key suffice, so no empty/duplicate intake was
created. Reread actual primary pp99,101,102 as complete held page images,
the current corrected ordinary sheets, source thinning/substitution and
the actual current ordinary-full boundary. The original p99 object
extension premise is M:*, not arbitrary typing or target validity.

Seven reciprocal proofs are supplied: raw literal-star rigidity and
small-type generation; source context conversion with actual certificates
for both changed annotations; equal-object substitution through typed or
valid templates and the entire dependent suffix; product-headed source
equality injection, automatically unrestricted for kind products; actual
ordinary constructor-valued root subject reduction and beta equality;
dependent codomain transport; and fully derived nonnormal declarations
and annotation contractions at the same old source type.

The substantive domain-cast construction does not assume an inverse to CC.
Flatten an actual product-headed source equality proof into its outer
product/reflexivity leaves with orientations retained. Project domain
equalities along the path. Each leaf has its actual first-domain
certificate, supplied by its body premise's context. Transport that leaf
body equality into the original actual first-domain context by the proved
source context-conversion theorem. Concatenate there. Intermediate right
domains need not be assumed well formed. For logical product endpoints,
class invariance and persistent product heads exclude every outer object
lambda/application/beta rule; headedness is therefore automatic. This
constructs the exact source A≅B cast and body equality P≅Q for an ordinary
constructor root redex, so substitution and the actual final conversion
chain give its contractum at the SAME given source logical type.

Concrete source witnesses: Γ=A:*,F:(Πu:A.*),a:A,f:(Πu:A.Fu),
n=(λv:A.v)a, B=Fn, B'=Fa. Actual full rules derive n:A,n≅a,
B:*,B':*,B≅B',fn:B and fa:B after a source conversion. Hence the
nonnormal object declaration h:B satisfies the exact M:* extension guard.
Changing it to h:B' preserves h:B. The annotation contraction of
t=λh:B.h to t'=λh:B'.h preserves the actual old typeΠh:B.B by an
explicit product equality and type conversion. The annex also gives the
fully indexed Γ/n/B/B' witnesses. This is not normal-variant inference;
that variant rejects the nonnormal annotation and old result type.

Remaining inference, not hidden closure: a proof-valued redex has an
object-product function type. An arbitrary equality proof of such products
can leave the product head through beta/application generators. The headed
path theorem does not yet eliminate those excursions. An actual example
of nonautomatic headedness is T=Πz:A.A and U=(λX:*.T)A in the valid
Γ above. Source product formation gives T:*, thinning gives T:* in ΓX:*,
abstraction/application give U:*, and full beta gives U≅T. Thus the
actual proof T≅U≅T has an application-headed intermediate, although this
particular endpoint equality also has a simpler reflexive proof. This
does NOT disprove the possibility of a general proved transformation;
it establishes why the proof condition cannot simply be dropped.

An attempted general sorting/endpoint induction exposes the mixed
application case: MN:* generates M:(Πx:A.*),N:A. From child equalities
M≅M',N≅N' one still needs actual same-type source typings of those
children, especially when A is a proof-domain object type. The new
equal-substitution construction supplies codomain equality once such
typings exist; it does not manufacture them. A naive induction on maximum
raw proof heights is also not justified through transitivity because the
first transported typing can have larger generated height. No purported
well-founded closure or an imported normal-type inverse is counted as a
solution to that gap. Ordinary-full global type correctness, general
sorted-beta reflection, arbitrary compatibleSR and the complete arbitrary-
annotation checker remain unsupplied. Constructor rootSR and the stated
headed proof-valued subclass are actual newly proved source results.

No children, independent review, tests, build or manuscript render. Only
held primary source pages were viewed. The original PDF/hash is unchanged.
The new fragments are released with hashes in the return; reader adoption
of these further results is a separate root decision.

## Object-head excursion block and explicit overrun

The first clock was20:18UTC, with a planned20:58 proof stop. Mathematical
files were saved20:47UTC. Further dependency investigation continued until
the21:08 clock audit, overrunning the planned stop; no theorem discovered
after that save is counted as supplied. Root directed an immediate stop
and release-record/hash saving only. This paragraph preserves that overrun
instead of reporting it as on-time work.

New artifacts: `spec/fragments/p07-ch88-object-product-body.tex` and
`-annex.tex`, with a genuinely new two-row measure intake
`handbook/registry/symbols-intake-p07-ch88-object-product.csv`.
All adopted and previously released mathematical files/intakes stayed
frozen. Current ordinary rules, source context conversion/equal substitution
and headed injection were read. No source reacquisition, new manuscript
render, test, build, independent review or child was used.

Six reciprocal proof pairs supply:

1. Product beta landings have actual source star typing: substitution
   gives a source contractum typing; source product generation gives its
   actual star typing; raw rigidity then forces the original body type
   literallystar. Raw substitution and persistent heads classify the two
   templates as both headed or both the selected variable.
2. Asymmetric equal substitution: only the LEFT argument needs actual
   typing; right argument equality/scopedness suffice. The full congruence
   guards all use the left substituted environment. A literal product or
   lambda template produces one outer congruence of that same head.
3. Actual beta–primitive-lambda-congruence/application–beta commutation
   using both landing guards. Their actual annotation certificates and
   domain equality permit the source right-argument cast and right-body
   context conversion; substituted body equality plus equal substitution
   produces equality of the contracta. The local redex-endpoint beta-height
   decrease is NOT advertised as a global equality-path measure.
4. A headed-proof normalizer for an EXPLICIT syntactic certificate family:
   headed bases, symmetry/transitivity with headed intermediates, cancelling
   beta pairs, and nested guarded diamonds. Recursive calls are only on
   ORIGINAL body/argument equality subproofs, strictly lower in original
   proof-tree height. Inflated generated proofs are never recursive inputs.
   No exhaustion of arbitrary source equality proofs is assumed.
5. Source product injection and actual rootSR extend from already-headed
   conversions to this genuinely unheaded certified family. Lambda-headed
   domain/body injection is also supplied with its actual first-context guard.
6. A fully typed countercase to naive endpoint/path beta-height measures.

The last example uses Γ=A:*,C:*,a:A, n3=I_A^3 a,
D(x)=(λp:A.C)x, M0=Πy:C.C and M1(x)=Πy:D(x).D(x).
Its original outer diamond path has heights0,4,3,2; the commuting middle
M1(n3) has height8 and the new path0,8,2. Maximum increases4→8 and
sum9→10. All source typing/beta/congruence guards are derived in the
annex. Its body equality is already product-headed, so the new normalizer
successfully handles it by original proof height. This refutes only the
naive proposed measure, not head elimination or a future full theorem.

Residual: a general middle function equality can have nonprimitive
lambda-head excursions, and product-to-product paths need not have the
specified certificate shape. No well-founded exhaustive transformation,
global ordinary-full type correctness, sorted beta reflection, arbitrary
compatibleSR or complete arbitrary-annotation checker is supplied.

After the saved proof stop, a constructor-only principal-kind and source
weak-head route was investigated but NOT written/proved in an annex.
The proposed principal recursion uses variable lookup, star for products,
products for constructor lambdas, and valid-kind body substitution after
kind-product injection for applications. A proposed weak-head recursion
would keep proof arguments opaque and use constructor-root preservation,
with lexicographic term beta-height/size for function and contractum calls.
These are pending construction routes, not adopted facts or imported
lemmas. They require a separate bounded assignment and full written cases.

The immediate release record and hashes accompany this return. No further
proof investigation followed root's stop direction.

## Ordinary/object reader adoption,21:31UTC

The frozen seven ordinary-checking pairs and six object-head pairs are
adopted via apply_patch in four new files:
`handbook/parts/p07/presentations/coquand-huet-1988-ordinary-checking.tex`,
`coquand-huet-1988-object-product.tex`, and their matching
`handbook/annex/p07/presentations/` paths. All13 statement labels,
proved-status targets and reciprocal annex backreferences are retained.
Both new annexes preserve the frozen proof contents. Working fragments,
the earlier realization/checking reader files and intakes remain unchanged;
the owned core changes only its inputs and adjacent scope reconciliation.

The owned core input sequence is now normal-variant checking, then
ordinary source casts/context/equal substitution, then object-head
certified transformation. Root still owns the shared annex driver and
must route the two new annex files in that order after the existing
checking annex. No shared driver, canonical/baseline record or generator
was changed in this block.

Core and ordinary scope passages now distinguish supplied constructor
domain casts/injection/root preservation and certified-family proof-valued
preservation from the remaining arbitrary object-product path problem.
The old blanket missing-cast language is not retained beside its supplied
constructor proof. The certified family is explicitly not exhaustive;
global ordinary-full type correctness/sorted reflection/compatibleSR and
arbitrary-annotation checking are not upgraded. The beta-height
countercase and the successful original-proof-height measure remain.
The object landing statement's general product-or-lambda shape clause is
phrased explicitly as a separate generalization of its product-only star
typing clause, matching the already supplied annex proof.

Only reader placement/scope reconciliation was performed. No new proof
investigation, independent review, test, build, render or source reread
beyond the required current-fragment/placement read was done. The prior
overrun and pending principal-kind/weak-head route stay in this research
record and are not copied into the book as results. The measure intake is
retained unchanged. Release hashes are supplied in the return to root.
