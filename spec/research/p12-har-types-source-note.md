# Barendregt--Geuvers 2001: source-specific proof/type-system intake

Unit: `ED26-SRC-037-0018`; allocated components C001--C004. This is a
bounded authoring record, not independent source admission or publication
acceptance. The entire selected 90-page chapter remains allocated.

## Identity, extent and manifestation

Henk Barendregt and Herman Geuvers, "Proof-Assistants Using Dependent Type
Systems," chapter 18 of *Handbook of Automated Reasoning*, volume 2, edited
by Alan Robinson and Andrei Voronkov, Elsevier/MIT Press, 2001,
pp.1149--1238; DOI `10.1016/B978-044450813-3/50020-5`.

First-party host: <https://www.cs.ru.nl/~herman/PUBS/HBKassistants.pdf>.
The author's publications page is <https://www.cs.ru.nl/~herman/pubs.html>.
The chapter URL was opened successfully through the web PDF reader on
2 October 2026; its reader reports 90 pages and the same printed title,
authors, contents and 2001 copyright. Web screenshot requests subsequently
failed with a cache-miss error; held-source Poppler renders were used instead.

The retained original is
`tmp/acquisition/src037/geuvers-proof-assistants-retry-01.body`, 633910 bytes,
SHA-256 `ce13485bfec08df559c838db13e53dcc9e75050daa7e67fe806bb04c25f4adcf`.
The citation copy is
`citations/Barendregt and Geuvers - Proof-Assistants Using Dependent Type Systems (2001, Handbook of Automated Reasoning, author-hosted chapter).pdf`,
636349 bytes, SHA-256
`48268d36690e8006aa0f6e78b67f553c7a2a17f44b4f394a442241be002b4b2e`.
The citation manifest records unchanged page objects/streams and preserved
original bytes as a prefix. Neither this transformation nor matching
pagination proves publisher-file byte identity. The retained readable layout
is `tmp/acquisition/src037/geuvers-proof-assistants-retry-01.body.derived-layout.txt`.
Physical PDF page = printed page -1148 (one-based), including the blank
second physical page. Printed pp.1230--1234 contain bibliography,
1235--1237 subject index, and 1238 name index.

## Ownership and route

The lead corrected the initial assignment to the exact queue-proposed files:
`handbook/parts/p12/presentations/har2001-c18.tex` and
`handbook/annex/p12/presentations/har2001-c18.tex`. No file was created at
the earlier erroneous paths. Intakes remain
`handbook/bib/intake-p12-har-types.bib`,
`handbook/registry/symbols-intake-p12-har-types.csv`; source rules use only
`handbook/registry/calculi/p12-har-types.tex`. The lead owns routing and
canonical integration. Existing `interactive-proof.tex` is an interface,
not a discharge of this chapter.

## Reading and correction provenance

Read across the authoring blocks: the complete retained readable layout,
including sections1--5 pp.1151--1230 and bibliography/subject/name indices
through p.1238, plus title/contents and the blank opening page. Thus the
actual ninety-physical-page layout reading is complete; full reconstruction,
proof completion and image inspection of every page are not claimed.
Inspected source pixels:1159,1169,1179--1183,1186--1188,1190,
1192--1196,1201--1202,1204--1205,1207--1211,1215,1217--1219,1227.
Other generated PNGs are not credited as inspected.

1. Source p.1159 application synthesis: after finding argument type A and
   function type C reducing to `Pi x:D.B`, the printed domain test compares
   D with C. This is ill-typed as an application criterion. The active
   reconstruction compares D with A, as the displayed example itself does.
2. Source p.1169 `abs-comp`: premise `Gamma |- A=C:D` accompanies a
   conclusion with the second lambda annotated D. The active rule uses
   annotation C, the equal domain, not D, its sort/type. Both slips are
   confirmed visually rather than guessed from corrupted extraction.
3. Source `AntiSym` in pp.1157--1159 names the formula
   `forall x,y. Rxy -> Ryx -> bottom`, which is asymmetry, not ordinary
   antisymmetry (`Rxy and Ryx -> x=y`). Retain the published identifier and
   explicitly distinguish its meaning; ordinary antisymmetry does not imply
   irreflexivity (equality is a counterexample).
4. Corrupted layout extraction drops minus signs in pp.1179--1180; the
   actual page images show the negative absolute-value branch `-x` and the
   overlap assertion `x=_F -x`. Retain these exact signs.
5. Source p.1171's comparison of equality elimination and historical Coq is
   not generalized to modern CIC/Rocq. The mathematically usable condition
   is permission to eliminate into the sort of `Fin`; the exact historical
   implementation claim remains a version-specific source claim, not a
   theorem about every inductive equality.
6. Actual page1194 confirms that Lemma3.19/Definition3.20 admit only a
   Prop-sorted domain in the formula-body branch. Figure2 also admits
   Type/Prop. The concrete valid term `lambda x:A.hx` in
   `A:Type,P:A->Prop,h:Pi x:A.Px` is rejected by that printed guard.
   The active guard admits both Prop and Type in that branch; its complete
   conditional correctness argument and the counterexample are reciprocal
   annex results. The correction is not attributed as the unmodified
   published algorithm. Source3.16's full-product check is retained as
   the earlier algorithm, with its real termination-measure obstruction.
7. Proposition3.23(2) prints the ordinary turnstile in the consequent of
   its modified-rule completeness assertion. The active assertion uses
   the modified `tc` turnstile, as required by the statement's subject.
8. Noninjective PTS sort maps preserve contractions at their redex positions,
   but do not reflect the reduction relation between arbitrary chosen
   preimages. The source p.1200 unrestricted pairwise `iff` is stronger
   than this valid property. The active morphism proof uses only the
   valid forward contraction preservation needed for normalization
   transfer; it does not assume an injective inverse sort map.
9. The reverse map on pp.1201--1202 is from lambdaHOL to PREDomega and is
   judgment dependent at result sort Type; the printed preceding wording
   calls it a morphism in the opposite direction. The reader treatment
   retains the actual clauses without that erroneous designation.
10. Formal section3, p.1181, explicitly excludes definitions and delta
    reduction. Its lambdaHOL and PTS checking/metatheory use beta alone;
    the earlier beta/iota/delta informal regime is a distinct interface.
11. The source's printed reverse HOL/PREDomega comparison fails, not just
    its designation as a morphism: lambdaHOL forms
    `(A->Prop)->A:Type` in `A:Type`; the proposed reverse requires
    missing PREDomega pair `(Type,Set,Set)`. This concrete countercase
    was supplied by the disjoint metatheory-construction worker and
    integrated with its full local derivation/rejection proof. It repairs
    the active equivalence claim and leaves the source normalization
    transfer in need of a valid replacement, not an added missing rule
    silently attributed to the original PREDomega.
12. Source p.1208's map term has an unused outer list binder and omits
    application of the recursor to that binder, yielding an extra
    List-to-List function relative to its claimed type. The active term
    applies the recursor to l; both constructor computations and its
    exact corrected type are proved, and this correction is not
    attributed as the unmodified printed term.
13. Source p.1204 lists three group axiom formulas but its tuple supplies
    four proof fields. The active right-nested proof package has exactly
    three. Figure6's Type/Prop strong sum also does not form the outer
    data-valued sums of the displayed Group(A); those additional formation
    requirements are explicit, not inferred from that figure.
14. Source p.1210 declares Q:A->Prop but the dependent constructor binds
    z:B. The active declaration Q:B->Prop is necessary to type Qz and
    the subsequent actual projection construction. The separately added
    Prop/Type regime remains separate from the base disambiguation.
15. Source p.1205's displayed lower-result Sigma-prime rule and its
    following higher-universe warning are retained as distinct surfaces.
    The lower candidate and the Prop-result strong-existential variant
    are not silently adopted as consistent rules. Their full paradox/
    consistency and exact universe-extension arguments remain owed.

## Component standing and residual dependencies

C001 remains **partial**. Exact beta-only lambdaHOL structural metatheory,
direct HOL decoding, strong normalization and the corrected full checker
are now proved with the incorporated CC argument. The three framework
inverse-faithfulness directions, full setoid/extensional interpretations,
other source-cited completeness/equality arguments and remaining historical
exposition/qualification obligations remain owed.

C002 **partial**: full pp.1181--1202 read; the actual HOL/lambdaHOL
languages, rules, direct embedding, checker and corrected guard, modified
judgments, distinct PTS specifications and genuine maps are supplied.
Contexts/projection/thinning, generation/product injectivity, correctness,
context conversion, disambiguation, uniqueness, beta subject reduction,
exact CC strong normalization and the judgment-dependent lambdaHOL transfer
have reciprocal proofs. The decoder and checker no longer retain those
premises as unresolved assumptions. Remaining arbitrary-PTS metatheory,
lambda-star paradox and other selected source obligations remain open.
The refuted printed inverse is not used to justify normalization.

C003 **partial**: full pp.1202--1211 read and reconstructed rule/definition
surfaces include Figures4--6, fixed nat/List/Tree, the exact positive
argument scheme and generated recursive families, primitive conjunction/Eq,
parametric List and separate dependent-mu extension. Local typing/
constructor computation proofs, even-double induction, corrected map,
Tree task terms and actual dependent projection construction are supplied.
The general extension's complete beta/iota metatheory, universe/strong-sum
paradox or consistency arguments, full admitted record-formation regime
and parametric-family extension obligations remain open.

C004 **partial**: full pp.1211--1230 read; historical tactic-to-term
workflow, core theory definitions, both printed proof objects, autarkic
interfaces and the complete dated comparison table are reconstructed.
Most listed logical/arithmetic lemma proofs, the prime-divisor end proof,
actual F/KPrime/G/interpreter constructions and universal adequacy/soundness
proofs with free-variable valuations remain owed. Modern assistant tables
are not substituted for this source version.

The whole source extent pp.1149--1238, bibliography/index provenance and
all four component obligations survive this partial block. No queue state,
canonical record, generated lookup, driver, shared host or style was edited.
No child agent, reviewer, manuscript build/render or prose-test was run.
Source PNGs are evidence only, not manuscript publication checks.

## Delivered local constructions and exact continuation

The body contains the source-specific checking/problem distinction;
constructive type interpretation; Rel/AntiSym/Irrefl definitions and the
whole five-binder term check; all three section2.4 signatures; fully
instantiated predicate and beta examples; primitive-recursion clauses and
the four-step addition/conversion example; the two-level reflection term;
definitional/book/Leibniz/inductive/identity distinctions; setoid functions,
quotients, subsetoids and rational representatives; coercion insertion;
semantic/derivability and strong-completeness distinctions; reciprocal and
absolute-value proof-dependence examples. Source rules are shown through
the disjoint registered sheet, not new body inference schemata.

The initial eight body results have reciprocal annex items and supplied arguments:
asymmetry term check; conditional normal-form conversion decision; all
forward PROP/PRED/lambda framework rule cases; dependent-sum projections;
reflection; Leibniz equivalence/transport; function/subset/quotient setoids;
reciprocal and all four absolute-value branch cases. These local results
are not source-unit admission or formal proof-assistant executions.

C001/C002 continuation, before any full-component credit:

- The corrected checker's exact normalization dependency is now discharged
  by the incorporated CC proof and separate lambdaHOL transport. Preserve
  beta-only scope and corrected algorithm provenance; no added-inductive
  or strong-sum theorem is thereby supplied.

- Establish each inverse framework faithfulness direction for its precise
  host/signature, with normal-form/canonical-form restrictions ruling out
  unintended inhabitants; forward rule induction does not do this.
- Supply the remaining selected global normalization/equality results and
  general PTS properties at exact regimes. Raw pseudo-term confluence,
  whole-context substitution and specific lambdaHOL structural/typed
  preservation results are now proved; no beta/iota extension theorem or
  arbitrary-PTS strengthening theorem follows automatically from them.
- Supply or preserve as unresolved the source-cited equality,
  extensional/setoid interpretation and weak/strong completeness proofs.
  Full setoid interpretation needs other type constructors, not just the
  proved arrow fragment.
- Reconstruct section1's remaining historical motivation/application and
  reliability qualifications (complexity versus depth, research-tool and
  computer-mathematics/library discussion), the section2 opening contributor
  account, and source2.9 philosophical alternatives/quantifier choices
  at their attributed status. Current local treatment is not a claim to
  reproduce every source exposition paragraph.
- Add the rational example's complete representative existence/uniqueness
  argument if treated as a proved result rather than its current example;
  retain the positive denominator and non-invariant subset predicate.

The lead assigned a disjoint metatheory-construction worker on the exact
lambdaHOL dependencies. W1--W8 were read completely, checked against the
exact triples and noncircular dependency chain, and integrated into the
reader annex with reciprocal statements. It does not own these reader
files. The separately authorized normalization block began12:12UTC.
W9a--h was read completely, compared with the exact primary report rules
and checked for its actual structural/semantic dependency chain before
adoption. It is incorporated as a reciprocal exact CC theorem followed by
lambdaHOL transfer and closed corrected-checker links. This is author
integration, not independent admission.
Full C001/C002 dependencies stay allocated. C003 has the actual local
treatment above and its explicit global residuals. C004 and the
remaining source extent survive unchanged. The finished writing batch
still needs later consolidated independent source-fidelity/topic/adversarial,
static, build and visual evidence.

## Second-block new proof and rule surfaces

Additional reciprocal annex results supply:

- The direct HOL domain/term/formula translation and every natural-deduction
  rule, including the eigenvariable and beta-conversion cases.
- All local impredicative connective typing/computation cases and the
  source's predicate-valued Leibniz symmetry construction, separate from
  the first block's equality-valued construction.
- The inverse direct HOL decoder with every proof constructor/typing-rule
  case; its formerly conditional structural premises are now integrated
  full lemmas, not assumptions stating the desired completeness.
- The source-guard counterexample and corrected mutual checker proof
  (guard equivalence, soundness, a concrete decreasing weight, total
  termination on all inputs, completeness and final TCP comparison),
  now using the separately proved exact normalization.
- PTS morphism judgment preservation, all seven Figure3 rule cases,
  source PREDomega/HOL and PREDomega/CC map checks, and conditional
  target-to-source normalization transfer.
- Unconditional raw pseudo-term beta confluence by parallel substitution,
  complete development/absorption, diamond joining, and the two closure
  inclusions; annotations and Pi bodies are included.
- Unconditional general Figure3 PTS substitution including the entire
  later context, all seven typing-rule cases and free-variable discipline.
- The concrete failure of the printed inverse PREDomega comparison;
  both the valid HOL formation and impossible target formation are shown,
  including why beta conversion does not restore the missing pair.

The shared source-rule file now contains the earlier section2 surfaces,
complete Figure1 HOL, Figure2 lambdaHOL, Definition3.22 modified judgments,
and Figure3 PTS surfaces. Its multiple sheet labels remain disjoint and
are reached through the body's existing `showcalculus{p12-har-types}`.
No source component is admitted by the number of labels or proof items.

Current proof-construction interface: the separate worker was informed
that the exact formal source is beta-only, and received the corrected
checker guard and its counterexample. Its returned reverse-map countercase
is integrated, and its complete W1--W8 structural/CC-transport fragment is
integrated. The W9 normalization construction is now read, source-qualified and incorporated;
other unresolved source/extension obligations receive no proved credit.

## Third-block extension constructions and residuals

Eight W1--W8 reciprocal items were integrated, preserving the original
assumptions and discharging the direct decoder's structural conditions.
Subject reduction includes annotated and product-body contractions and
gives a typed common reduct using raw confluence. The valid normalization
bridge is judgment dependent, not a false ordinary sort morphism.

Three further C003 reciprocal items give both encoded sum computations,
all fixed/general constructor-root type checks and recursive-family
construction, the complete even-double proof and corrected map equations,
and the actual dependent-mu projection sequence plus conjunction/Eq
proposition-only constructor cases. A well-founded input-tree fold argument
is given explicitly; it does not assert universe closure or existence of
every proposed inductive formal extension.

New exact residuals: full formal beta/iota subject reduction/confluence/SN
for admitted inductive signatures; the universe and strong-sum warned
variants' complete paradox/consistency proofs; formation of the nested
group record beyond Figure6; the parametric family kind/constructor
quantification extension. C004 now has the partial treatment above, with its
remaining proof/algorithm obligations explicit. Bibliography/index pages
have been read; their full destination/citation reconciliation still remains.
Full readable-layout reading is actual; full-source completion is not.

## Exact CC normalization qualification and integration

Primary: Herman Geuvers, Computing Science Report94/50, Eindhoven,
December1994, *A short and flexible proof of Strong Normalization for the
Calculus of Constructions*. Primary PDF:
<https://pure.tue.nl/ws/files/2181809/9511424.pdf>; identity page:
<https://research.tue.nl/en/publications/a-short-and-flexible-proof-of-strong-normalization-for-the-calcul-2/>.
Retained worker-owned capture:
`source/references/p12-har-cc-normalization/geuvers-1994-report-94-50.pdf`,
SHA-256 `1e5a515c38beb8b91e8c3bc1a0f8705bfc4be96517423e7bd33e0f40efa6edb3`.
The PDF's38physical pages contain repository/report covers, printed
report1--27, then a trailing series catalog; physical=printed+2 within
its report. No identity with the1995LNCS publication pp14--38 is inferred.
The separate key Geuvers1994Report9450 records the actual version.

Read here: complete primary sections1--3, printed pp1--10, including
section4's opening typed-conversion warning; actual renders pp7--10
inspected. Definition2.2 has exactly the target two sorts, one axiom,
four product triples and compatible annotated beta. Whole later report
extensions are not credited as read or imported. The delivered proof
fragment's hash at qualification was
`ae4c33d8819d6532c409c7966359e595d6b2a23f019c5333c8d68cdd85902d58`.

The complete W9a--h chain was read: CC top-sort structural/SR exception;
classification and beta-stable finite kind shapes; candidates and
controlled expansion; finite nonempty semantic domains; evaluator
definedness/membership/substitution/typed-conversion invariance;
annotation-retaining positive-step simulation; every binder/argument and
all four product cases; identity raw valuation for arbitrary open valid
contexts. The reduction-closed neutral-expansion candidate version is an
explicit adaptation, not an identification with the report's key-redex
SAT definition. No circular normalization/checker premise or missing
closure step was found in this author integration; independent gates
remain required.

Exact CC SN, lambdaHOL transfer and the corrected full checker now have
reciprocal reader proofs and actual links. No normalization premise
remains in that chain. Delta/iota, strong sums, inductive and warned
universe extensions remain outside it.

## C004 exact continuation

## Disjoint framework-faithfulness and concrete setoid block

The lead locked the released core body/annex/sheets/intakes during its
integration. This block edits only NEW
`spec/fragments/p12-har-framework-faithfulness-body.tex` and
`spec/fragments/p12-har-framework-faithfulness-annex.tex`, uniquely suffixed
framework bibliography/symbol intakes, and this note/source packet.
These are reader-ready constructions awaiting root insertion/adoption;
their existence is not independent admission or full C001 completion.

Reread source2.4 pp1160--1163. Primary LF support was read at
<https://homepages.inf.ed.ac.uk/gdp/publications/Framework_Def_Log.pdf>,
selected section2.1 Tables1--2 and section2.4, author pages3--10,
with its explicit beta-only choice and canonical-form caveat. Retained
author file has37physical pages, SHA-256
`4bd5b57ace8616b7e71d43df985f80686776220a178f30f9835a735d3fb81947`,
at `source/references/p12-har-types/harper-honsell-plotkin-author-framework.pdf`.
Its whole37pages and exact final JACM layout are not claimed read/identified.
The source chapter itself supplies the1993 JACM40(1),143--184 reference.

Six reciprocal items now supply exact beta-only weak LF normal-head
inversion and typed normal representatives; exhaustive normal-name
reification/substitution; every inverse proof-head case for PROP/PRED/
untyped beta equality; an explicit no-object-eta boundary; the rational
gcd/Bezout reduced-representative construction and proof-sensitive
subsetoid isomorphism; and the full quotient-setoid mapping property.
The three formerly open framework converse tasks are constructed here
at their source host/signature/open-context standing, pending adoption.

The proof does not assume every beta-normal LF term is beta-convertible
to an eta-long canonical term: the primary paper expressly denies that.
Partial forall(R c) and abs(app u) arguments use explicit pointwise
reification. Function-valued proof inputs are decoded by applying a
fresh variable; a concrete size decrease proves recursive termination.
All introduction/elimination/refl/sym/trans/mon/xi/beta cases are present.
The first-order converse includes open term substitutions and the actual
eigenvariable condition. The lambda converse admits arbitrary free D
variables but not extra equality hypotheses, which would assert extra
equations rather than pure beta conversion. LF kind entries remain fixed
signature declarations, not additional kind-typed object variables.

Remaining C001 gaps are not disguised as consequences of these proofs:
the full source-cited extensional/setoid interpretation beyond the arrow
fragment requires actual dependent fiber transports coherent under
reflexivity/composition and proof choice, followed by all Pi/Sigma and
universe/elimination cases. That construction is not supplied here.
The source-attributed Martin-Lof weak-completeness theorem still needs
the exact selected system/first-order fragment and its Swaen-style proof;
the chapter's family description does not fix those clauses sufficiently
to infer it from the framework result. No generic nonderivability claim
about Leibniz versus Fin transport is promoted without the actual sort
and elimination regime. Core source files and all shared/canonical files
were left untouched; no children, reviews, builds, manuscript renders or
prose tests were run.

## C004 exact continuation after the arithmetic construction block

The formerly open listed logical/equality/order/addition/multiplication
library proofs and numbers_gt1_have_primediv/Euclid continuation now have
actual constructions in the manuscript prime-development child and its
reciprocal annex. Their original working fragments are retained; the
author-side adoption block below records placement. Independent gates
and root's shared-annex routing/typed-data merge remain pending.
They are no longer merely the chapter's omitted-object declarations.
Autarkic continuation
must actually construct F/KPrime/G/interpreter procedures and prove their
universal adequacy/soundness, including free-variable valuations; their
current interfaces are not implementations presented as complete.
Source p1215's printed impredicative disjunction definition self-refers;
the valid non-self-referential encoding already supplied from p1188 is
used in the released core, not that malformed display. The new historical
arithmetic treatment uses the source's primitive inductive or instead.
Repeated n,m,k binders in plus_ass/distr now have the single-triple proof
and an explicit unused-outer-triple witness for a literal shadowing reading.
The footnote's
variadic Euclid display is not literally one first-order PA formula,
but this does not imply that its finite-sequence coded counterpart
requires second-order arithmetic; the explicit coding bridge remains owed.

## Disjoint historical arithmetic / prime-divisor / Euclid block

This separated block began 2026-10-02 17:50:45 UTC, with checkpoints at
18:00 and 18:10 UTC. Its ownership is only the NEW files
`spec/fragments/p12-har-prime-development-body.tex`,
`spec/fragments/p12-har-prime-development-annex.tex`,
`handbook/bib/intake-p12-har-prime-development.bib`,
`handbook/registry/symbols-intake-p12-har-prime-development.csv`, and this
single existing source note/source packet. Previously released core,
framework and lambda-star files stayed frozen for lead adoption.

Actual rereading in this block: complete printed pp1214--1220 in the held
layout, with pp1215--1220 also visually read from the retained source
page images `development-67.png` through `development-72.png`.
Source locators: p1214 nat_ind/nat_rec and constructor computation;
p1215 primitive or and note4's two Euclid forms; p1216 Coq6.3 qualification
and the explicit omitted-proof notice; p1217 logic/ex declarations;
p1218 DN, ex_c proof and Set-indexed equality; p1219 nat:Set, Is_suc,
leseq/lthan/cv_ind/plus; p1220 times/div/propdiv/prime/primediv/HPD,
the named prime-divisor theorem and cutoff-subtraction requirement.
The chapter's original author host is
<https://www.cs.ru.nl/~herman/PUBS/HBKassistants.pdf>.
The held original ninety-page file remains
`tmp/acquisition/src037/geuvers-proof-assistants-retry-01.body`, SHA256
`ce13485bfec08df559c838db13e53dcc9e75050daa7e67fe806bb04c25f4adcf`;
no new manifestation or modern Coq-library identity was inferred.
The current registered fixed-Type nat data/proof Rec schemas were read
at `handbook/registry/calculi/p12-har-types.tex`, rules nat-data/nat-proof
and the two nat constructor computations. The historical Set spelling,
its generated Prop-only equality/leseq/ex eliminations, and data/predicate
case analyses are kept explicitly separate from the beta-only base.

Seven reciprocal reader items supply: (1) every selected logical helper,
including introduction/elimination aliases and actual DN instances;
(2) primitive equality transport, symmetry, f_equal, eq_ind_r, no_conf
and successor injectivity; (3) all source order lemmas, direct Prop
leseq induction, trichotomy/cancellation and cv_ind derived from nat_ind;
(4) all source plus/times identities, both cancellations, additive order
characterization and a full positive-factor strict-preservation/weak-
reflection argument; (5) reflexive/transitive divisibility and the actual
difference coefficient s dotminus r, with d=O separately discharged;
(6) the complete source prime-divisor proof via cv_ind and DN-derived
tnd on existence of a proper divisor; (7) factorial positivity and
factorial divisibility, the full unbounded-prime Euclid proof, and a
typed finite-family avoidance corollary using a constructed nat-rec sum
bound. Each proof states its induction motives and branches; definitions
of numerical functions are not substituted for their theorems.

All ex/or/leseq/eq eliminations in these proofs target Prop. Natural-number
recursions returning data are instantiated separately at nat or
nat-to-nat, and never consume proof evidence to return an extracted
witness. No classical prime-producing algorithm is claimed: DN enters
the source's proper-divisor disjunction and hence the output Prop
existential. A current Coq execution, kernel replay, general inductive
extension normalization/consistency theorem, or beta-only lambdaHOL
retargeting is not claimed. The arithmetic dependency chain itself has
no retained omitted lemma at its explicitly stated historical generated
principles and DN assumption; its standing is author-supplied proof
construction, not independent admission or full C004 completion.

Precise remaining scope: actual autarkic F/KPrime/G/interpreter procedures
and universal adequacy/soundness with open valuations; the formal
first-order arithmetic sequence-coding bridge (the typed finite-family
fold is not that bridge); and the separately allocated global extension
consistency/metatheory and C001 extensional/weak-completeness obligations.
Root owns insertion/adoption, reconciliation with prior declarations and
all canonical/shared consumer changes. No children, independent reviews,
builds, manuscript renders, prose tests, payments, account access or
external contact were performed.

The entire chapter is read in retained layout, but all C001--C004 and the
full source extent remain allocated at these partial standings. No
queue/canonical/shared host/style/driver/generated edits, child agents,
reviews, manuscript build/render or prose tests were performed.

## Author-side adoption of lambda-star and arithmetic reader units

This separated adoption block began 2026-10-02 18:44:29 UTC. The lead
delegated the existing core body and only the four NEW manuscript child
files, with the two existing disjoint intakes and this single source note.
The current whole core and all four released working fragments were read
before placement. No new source acquisition or broader reading/completion
claim is made by this block.

Four lambda-star reciprocal pairs are now in
`handbook/parts/p12/presentations/har2001-c18-lambda-star.tex` and
`handbook/annex/p12/presentations/har2001-c18-lambda-star.tex`:
hurkens-beta, hurkens-bottom, star-inconsistency, star-no-normal-form.
These manuscript files preserve their corresponding working copies
byte-for-byte. The parent core input is after the exact CC and lambdaHOL
normalization results and before products/sums/inductive extensions.
The earlier PTS-table assertion now links the actual witness and normal-
head obstruction rather than treating the paradox as an absent proof.
The old reverse-map boundary also points to the already constructed direct
CC replacement instead of retaining that normalization dependency as open.

Seven arithmetic reciprocal pairs are now in
`handbook/parts/p12/presentations/har2001-c18-prime-development.tex` and
`handbook/annex/p12/presentations/har2001-c18-prime-development.tex`:
prime-logical, prime-equality, prime-order, prime-semiring,
prime-divisibility, prime-divisor, prime-euclid.
The parent input follows the historical arithmetic entry and precedes the
existing two-printed-source-object theorem. The stable
`def:p12-har-prime-development` consumer label is retained as that entry;
its source-native detailed constructor/case/order/arithmetic/divisor/
primality/HPD clauses are preserved in the richer child definitions, not
discarded for a bare pointer. The parent still explicitly supplies
not/iff/ex/DN and the historical nat:Set standing. The child contains all
old numeric definitions and the full cv_ind/prime target statements plus
the actual recursor instances and arithmetic proofs.

The existing `thm:p12-har-development-objects` and its original reciprocal
core-annex link remain unchanged in identity: non_or and ex_c are the two
objects actually printed in the chapter. Their distinct printed-source
attribution is explicitly contrasted with the reconstructed omitted
library derivations, with links to the historical regime and new library
result. Source omission is retained as a fact about the source, not an
active claim that the manuscript still lacks these selected proofs.

The arithmetic manuscript copies differ from the frozen working copies
only by a reader heading, explicit quantification of P:nat-to-Prop in
cv_ind, clearer wording that Is_suc(O) computes to FF, and LaTeX escaping
of bare historical identifier underscores in prose. The parent preserves
its other actors' framework/CC/extension/assistant content. All four
original `spec/fragments/p12-har-{lambda-star,prime-development}-{body,annex}.tex`
working files remain untouched at their released hashes.

No shared driver, existing core annex, canonical registry/bibliography,
baseline, generated file or style was edited. Root still must input the
two new annex files from its shared route and merge the existing typed
intakes. Eleven reciprocal status/backreference pairs exist in manuscript
files; this is author-side adoption, not an independent review, admission,
build or rendered-publication result. No reviews, tests, builds, manuscript
renders or Coq replay were performed.

Residuals remain explicit in the adjacent manuscript: actual autarkic
F/KPrime/G/interpreter definitions with universal and open-valuation
correctness; the arithmetic finite-sequence coding bridge; and the global
formation/beta-iota metatheory and warned universe/strong-sum/parametric
extension arguments. The one-sort lambda-star witness is not a proof for
every such extension, and the historical nat:Set/DN development is not
beta-only HOL or the abstract nat:Type rule regime. The separately
allocated C001 extensional/weak-completeness obligations and all independent
gates/full-source allocation remain open.

## Disjoint autarkic F and interpreter construction block

Block start:2026-10-02 19:06:46 UTC. Only new
`spec/fragments/p12-har-autarkic-body.tex` and `-annex.tex`, unique
`intake-p12-har-autarkic.bib`/`symbols-intake-p12-har-autarkic.csv`, this
note and owned source evidence were edited. Adopted manuscript and old
intakes were frozen and untouched while root merges them.

Read full source section4.3 pp1220--1223 in retained layout and visually
from development-72/73 and newly retained source-only
autarkic-source-74/75.png. These contain F's bound, KPrime's two obligations,
term(Nat)'s Nat/+/*/0/1 signature, E's quotation equation, G's universal
preservation obligation and the omitted free-variable bookkeeping.
The generic compiler, Pocklington/Fermat variant, large certificate and
continuity language remain distinct source claims; no additional paper
body is claimed acquired/read. Current core/prime regime/order/semiring
and registered data/proof Rec interfaces were reread. The held original
90page source identity/hash stay unchanged. Source PNG creation reported
Type3 glyph bounding-box warnings; their relevant source formulas/text
were legible and visually read. These are not manuscript renders.

Six reciprocal items now supply: actual eqb/choose and all total/range/iff
branches; square growth/monotonicity/unique bounds; concrete F with full
ordinary-nat-induction adequacy and literal 45-to-6 reduction; actual
five-constructor arithmetic syntax and E_nu fold with quote/pointwise/
finite-context valuation proofs; all five semantic-substitution branches;
and the coefficient bound/finite proper-divisor characterization needed
by the next primality search. An explicit nested eqb/data-selector
valuation extends any finite assignment at distinct literal indices,
using default zero_A, and its assigned-index contractions are proved.

F is defined before its proof. Boolean equations are used through
f_equal and Prop equality transport, never equality reflection or proof-
to-data elimination. None of these six proofs uses DN. Fixed-carrier
A:Set interpretation needs only typed zero/unit/two operations; its Nat
instance is the source arithmetic interpretation, not beta-only HOL or
an identified nat:Type system. Syntax is first-order arithmetic, not all
lambda terms. Generated nat/syntax induction motives and every branch
are explicit; no parametricity/extensionality assumption supplies the
desired conclusion. The F45 path is a mathematical constructor reduction
derivation, not executed Coq or kernel replay.

At that block boundary KPrime's computed order code, boolean operations,
bounded folds and composition were still open. The following separate
KPrime block now supplies those actual constructions, pending adoption.
G's
actual polynomial transformer/normal-form convention and every universal
E_nu preservation branch remain required; interpreting the two source
example quotations does not construct G. Generic primitive-recursive
compiler, Pocklington/Fermat certificates, differentiation/simplification/
continuity extensions, arithmetic coding and global extension/C001
metatheory remain owed. Six pairs are reader-ready working constructions
awaiting root adoption and independent gates, not full C004/90page
completion. No independent reviews/tests/builds/manuscript renders or
Coq execution were performed.

## Disjoint actual KPrime construction and printed61 block

Start:2026-10-02 20:04:21 UTC. Ownership is only new
`spec/fragments/p12-har-kprime-body.tex` and `-annex.tex`, unique
`intake-p12-har-kprime.bib`/`symbols-intake-p12-har-kprime.csv`, and this
single note. Adopted/released prior files and old intakes stayed frozen;
no shared/canonical/driver/baseline edits were made.

Source pp1221/1223 were reread visually for the two KPrime obligations,
generic compiler, Pocklington/Fermat and exact large-example standing.
The held full section4.3 and pp1218--1220 definitions remain the source
basis; frozen eqb/bounded-coefficient code/proofs and historical order/
semiring interfaces were reread. No new acquisition or additional-paper
body reading is claimed. The held90page source hash remains unchanged.

Eight reciprocal items now construct: boolean operations with exact
range premises and all four cases; actual leb/ltb terms with range and
both positive/negative source-order iff proofs; inclusive Any with full
base/step range/existential/universal/negative proofs; Coeff/Proper/
HasProper with both bounded searches and all semantic directions; the
complete KPrime composition with range, prime iff one, neg prime iff O,
constructive decision, literal0/1 reductions and a composite4 search-hit
reduction; ordinary divisor characterization including zero/coefficient
cases; weak-product/no-multiple/small-factor lemmas; and the printed61
proof plus complete finite reduction argument.

The61 object proof uses one<61,61<8*8, the actual small-factor argument,
all six2..7 product-interval certificates and the full bounded nat case
enumeration. Its reduction argument is independent of inferring truth
from object-theory consistency: a separate meta-level literal-integer
interval table covers every d=2..60 and excludes61 for every coefficient,
then actual literal times/eqb/leb and inclusive-loop constructor contractions
give KPrime61 to one. No executed computation or certificate is reported.

All programs use fixed-target nat_rec and computed nat0/1 codes in the
historical nat:Set regime. All witnesses are eliminated only into Prop
code equations/specifications, never extracted to define program data.
DN, equality reflection, parametricity and functional extensionality are
unused. The source capitalized Prime obligation is instantiated at its
explicit historical prime definition and the ordinary divisor bridge is
proved, not inferred from names. Neither nat:Type nor beta-only HOL nor
a current kernel is silently identified with this regime.

The selected direct KPrime program/proof chain has no retained missing
lemma under its existing hypotheses. These eight pairs are reader-ready
working constructions awaiting root adoption and independent gates.
Still owed separately: generic primitive-recursive compiler/universal
compilation proof, Pocklington/Fermat algorithm and the printed
1223334444555554444333221/other large certificates, G and its universal
open-valuation polynomial-correctness/normal-form proof, differentiation/
simplification/continuity extensions, arithmetic coding and global
extension/C001 metatheory. No full C004/90page completion or independent
admission is claimed. No reviews/tests/builds/manuscript renders/kernel
execution or children were performed.

## Disjoint actual polynomial G construction block

Start:2026-10-02 21:02:51 UTC. Only new
`spec/fragments/p12-har-polynomial-normalizer-body.tex`/`-annex.tex`,
unique polynomial-normalizer bibliography/symbol intakes and this note
were edited. Every prior adopted/released file and intake stayed frozen.
Primary pp1221--1222 were visually reread for the exact arithmetic
signature, G example and universal E preservation/free-variable gap.
Frozen five-constructor T/E_nu/open-valuation clauses, computed nat
boolean/order code and actual historical semiring proofs were reread.
No new acquisition or additional-paper/full-reading claim is made.

The actual program uses three explicitly positive Set data declarations:
finite variable words, coefficient/word rows and finite row sequences.
All recursor signatures/constructor computations are supplied; no list,
map, ordering, interpreter or polynomial library is postulated. Weq/wlt
are actual nested word recursions; primitive word equality is justified
with length/head/tail functions and nat separation. Lex totality,
irreflexivity/transitivity and both code directions are proved. Word
merge has a typed outer W-to-W recursion and inner W recursion supplying
its same-first/smaller-second call, not an unproved well-founded search.

Ten reciprocal items now supply word code/order; coefficient homomorphism;
sorted merge/occurrence/value; every zero/combine/prepend/recurse insertion
case and key invariant; all sum/scale/product branches and zero cases;
all five actual N constructor cases; literal/word/row/polynomial quotation;
full universal open-valuation G preservation; the data N(Qp)=p retraction
and primitive-book-equality idempotence; and the actual source-pattern
computation. Coefficients combine in Nat, zero coefficients are discarded,
monomials retain repeated indices in nondecreasing words, rows have strict
descending lex keys. Every output is proved Good under that precise
sparse normal-form convention.

Interpretation functions chi/V/B/L are actual fixed-target recursions.
For each fixed A:Set the proof assumes the explicit commutative-semiring
equation families: additive/multiplicative association and commutativity,
identities, both distributions and zero annihilation. It does not silently
give those laws to an uninterpreted carrier. The Nat instance discharges
them with the existing arithmetic library, without DN. Every valid open
valuation nu:nat-to-A is quantified; no functional extensionality,
parametricity, choice, equality reflection or proof-to-data extraction is
used. Canonical data are not asserted semantically complete for models
with additional equations.

The literal X=Var O example computes to sparse rows (1,[0,0]),(2,[0]),
(1,[]), then to the right-associated AST x^2+(2x+1), with literal2
represented by Add U U and coefficient-one/trailing-unit omissions.
The source's alternate left-associated reading (x^2+2x)+1 has an explicit
addition-association interpretation bridge; parser-dependent AST identity
is not asserted. The example is a finite mathematical constructor
reduction trace, not an executed evaluator/kernel certificate. Retraction
and idempotence on opaque open inputs are likewise stated as primitive
book equalities, not definitional contraction claims.

This selected G program and its declared normal-form/correctness chain
have no retained missing helper under their explicit source-generated
recursion and semiring hypotheses. Ten pairs are reader-ready working
constructions awaiting root adoption and independent gates. Generic
compiler/universal compilation, Pocklington/Fermat/large certificates,
differentiation/simplification beyond this polynomial normalization,
continuity languages, arithmetic coding and global extension/C001
metatheory remain separately allocated. No full C004/90page completion,
independent admission, reviews/tests/builds/manuscript renders/kernel
replay or children are claimed/performed.

## Author-side adoption of all three autarkic packets

Separated adoption block start:2026-10-02 21:52:40 UTC. Latest parent
arithmetic/autarkic seams were read; its pre-edit hash matched the frozen
parent state. All six released working-file hashes matched their release
manifests before copying and remain unchanged after adoption. No new
research/source acquisition, review, test, build, render or replay occurred.

All24 reciprocal pairs now have manuscript body/annex files:
`handbook/parts/p12/presentations/har2001-c18-autarkic.tex` and matching
`handbook/annex/p12/presentations/har2001-c18-autarkic.tex` contain6;
the corresponding `har2001-c18-kprime.tex` files contain8; and the
corresponding `har2001-c18-polynomial-normalizer.tex` files contain10.
Their actual parent input sequence follows the historical prime-development
and two printed-source-object material: autarkic, then kprime, then
polynomial-normalizer, all before the dated assistant comparison.
Thus arithmetic/equality/order precede F/eqb and T/E_nu; those precede
KPrime's flags/folds; both precede G's word/order/semiring interpretation.

The parent retains stable `def:p12-har-autarkic` and source attributions,
but now links the actual F universal/45 proof, direct KPrime specification
and61 proof, T/E_nu valuation/substitution results, and actual G normal-
form/preservation/retraction/example. It no longer says those programs
are missing. Adopted autarkic body/annex pending-KPrime/G seams likewise
point to the actual supplied results. The frozen working copies retain
their original temporal boundaries, not new edits. KPrime and polynomial
manuscript copies preserve their released mathematical content. Before
freeze, the lead identified two further local stale phrases: KPrime's
closing boundary still listed G as remaining, and the word-merge result
said its already preceding interpretation was defined below. Those two
manuscript-body seams were corrected to the actual G proof pointers and
defined-above locator. Thus these bodies differ only at those local seams;
their annexes are byte-identical. Autarkic body/annex copies differ only
at the adjacent pending-KPrime/G seams described above. All frozen working
copies and intakes remain unchanged.

Every hypothesis/proof and the historical nat:Set versus abstract nat:Type
and beta-only HOL distinctions are retained. Generic fixed carriers still
require the explicit commutative-semiring equations for G; its right-
associated output and the alternate-source-parse association bridge stay
explicit, with no AST-identity or arbitrary-model completeness upgrade.
No generic compiler, large Pocklington/Fermat certificate, C001 result,
arithmetic coding or global-extension standing is promoted by adoption.

Intake stems remain p12-har-autarkic, p12-har-kprime and
p12-har-polynomial-normalizer. No frozen intake or canonical data was
modified; root owns their merge and all shared annex-driver routing.
The three new annex paths exist but their shared inputs are still root's
integration responsibility. This is author-side manuscript adoption,
not independent mathematical/source acceptance or full C004/90page
completion. Remaining compiler/Pocklington/large-certificate,
differentiation/continuity/coding/global-extension/C001 obligations and
all independent gates stay open.

## Generic primitive-recursive compiler and internal formula interpretation

Separated writing block start: 2026-10-02 22:18:55 UTC; new reading/proof
cutoff 22:48:55, save boundary 22:53:55. The current block owns only the
new primitive-recursive-compiler body/annex, its uniquely suffixed intakes,
this note and the HAR source directory. All previously released/adopted
body, annex and intake files remained frozen. The lead owns parent inputs,
shared annex routing, canonical merge and any adjacent old consumer seams.

The chapter's actual generic-program promise was reread in held printed
pp1222--1223, with its provisional Oostdijk--Geuvers2001 bibliography
identity. The cited author-hosted primary body was acquired completely:
`source/references/p12-har-types/oostdijk-geuvers-proofbycomp-author-2000.pdf`,
26 physical/printed pages, headed Elsevier preprint 14 April 2000, from
https://www.cs.ru.nl/~herman/PUBS/TCS.ProofbyComp.pdf linked by the author's
publication list https://cs.ru.nl/H.Geuvers/pubs.html. Its SHA256 is
606da0168c72c2630655dfd3b973c45df746b4a08ca37f0c74c6b1a7bd8102ef.
Publisher bibliographic metadata identifies the eventual TCS272(1--2),
293--314 article, 6 February2002, DOI10.1016/S0304-3975(00)00354-6.
The dated26-page preprint, chapter's provisional2001 reference and
22-page2002 journal manifestation are kept distinct. Journal bytes/body
were not acquired or read; the journal key records bibliographic identity
only. No publisher-file byte identity is inferred.

PowerShell/Schannel acquisition failed authentication/credential
initialization; bundled Python's default-verifying urllib client acquired
the author PDF. No certificate/TLS/security bypass, login, payment or
restricted-route repetition was used. The pypdf text attempt was not
relied upon because font extraction/console encoding failed. Primary
web text and actual source-only Poppler PNG inspection supplied reading.
Actual selected reading: introduction pp1--2 and system pp5--6 via
primary web text; datatype/recursion passages pp12--15 via primary web
text; computational interpretation and discussion pp17--25 via web text
and full source-page images; p16 was additionally fully image-read.
Exact definition/induction interfaces on p6 and p14 were additionally
image-inspected. Definition7 and the generated family induction are
on pp18--19, interpreters Definitions10/11 on pp20--21, comparisons
Definitions12/13 p21, connectives/bounded folds/istrue Definitions14--17
p22, universal ok/conversion and inverse caveat p23, extension/algorithm
limitations and external-Lego distinction pp24--25. This is selected
reading, not a claim that all26 pages or the whole HAR90page allocation
was newly fully read. Source images are derived evidence only, not
manuscript renders.

The decisive source-scope finding is that the present method is internal:
form:Set with eleven constructors, Prop interpretation and bool
interpretation, and a single ok proof generalized over every form.
Atomic fields are already typed Coq nat terms, not a syntactic PR-function
AST; quantified fields are nat-to-form families. The paper calls this
an extension of PRA. Its p23 inverse Prop-to-form translation is expressly
not an internal object-language function and is not implemented there.
Its p25 external string/Lego generator is a different earlier method.
The manuscript therefore does not substitute external representability
for the promised internal program. A separately labelled editorial finite
ranked PR-prescription language fixes arities, zeroary conventions and
last recursion argument, and provides actual zero/successor/projection,
composition and nat_rec templates with universal numerical representation.
No internal PR-prescription datatype is falsely attributed to this paper.

Nine reciprocal pairs are supplied in
`handbook/parts/p12/presentations/har2001-c18-primitive-recursive-compiler.tex`
and the matching `handbook/annex/p12/presentations/` file: complete ranked
compiler typing; independent-denotation/numerical representation;
actual source bool operations and computed nat-code bridge; all five
atomic comparison iff proofs; both exclusive bounded-fold iff proofs;
all eleven interpreter branches/induction typing; full internal universal
ok including negative/implication/family cases; characteristic instances
and conversion-to-proof; arbitrary prescribed-PR-predicate construction
with finite zero/one/at-least-two output calculation. The source bool:Set,
historical nat:Set, source proposition-code target Prop:Type and proof
target Prop remain separate. The exact source PRED-omega sorts/axioms/
six product pairs are stated. The source higher-order form recursor and
generated Prop induction are the licensed premises; no arbitrary fixpoint,
parametricity, functional extensionality, choice, DN or existential-proof
elimination to Set is assumed. The source's p23 lowercase boolean-looking
result in the istrue reduction is reconstructed at its actual Prop type:
istrue true reduces to True, identified here with historical TT.

The universal numerical representation covers every standard-natural
valuation, not arbitrary uninterpreted carriers. The internal ok proof
covers every valid open typed parameter context and arbitrary well-typed
quantifier family, independent of a closed normalization claim. Data
selector code explicitly converts source bool to nat O/one, with both
positive and negative proofs. Every ranked prescription yields the form
equality of its compiled value with one; comp then supplies an actual
zero/one characteristic program and an internally proved open-tuple iff.
This is not a classifier of arbitrary host nat functions or an inverse
on arbitrary Prop. Closed proof extraction is conditional on its actual
finite comp-to-true reduction, not on the input merely being described
as true. No global normalization of arbitrary axiomatic nat fields is
assumed. The direct earlier KPrime and the source generic Prime61 search
remain different algorithmic constructions.

Under these explicitly licensed selected-inductive interfaces, the generic
internal computation/adequacy dependency and external ranked-representation
bridge have no retained unproved helper. Automatic arbitrary Prop reification
remains source-unimplemented and is not claimed. Extension by a new atomic
relation still requires its actual boolean function and universal iff proof.
Pocklington/Fermat/large certificates, differentiation/continuity languages,
arithmetic coding, and global extension/C001 obligations remain separately
allocated. All full-source/whole-HAR scope and independent source/math/
admission gates remain owed where not separately satisfied. No children,
independent reviews, tests, builds, manuscript renders or kernel replay were
performed. Intake stem is p12-har-primitive-recursive-compiler, with source
preprint and journal-metadata keys kept separate; source mathematical
acceptance, root routing and canonical merge are not implied by this release.
The primary's exact Example9 f_Divides/f_Prime formula-valued terms are
also retained, with coefficient k<S m and strict divisor d<n bounds,
their actual Prop interpretations and generic characteristic-instance
links. Their source bounded-division convention is not silently identified
with the earlier historical unbounded div/proper-divisor prime definition.
The source's historical Prime61 performance report is attributed, not a
new finite trace or executed computation for this generic algorithm.
