# λHOL proof-authoring block: exact β-only global metatheory

Owner: `/root/lambda_hol_metatheory_author`. Date: 2 October 2026.
These are distinguishable working artifacts, not adopted manuscript text or
an admission/review record. This note,
`spec/fragments/p12-har-lambda-hol-metatheory.tex`, and the separately assigned
`source/references/p12-har-cc-normalization/` capture directory are owned by
this worker. The capture directory was authorized only in the second block.
The source author owns reader body/annex/rule-sheet/source-note; root owns
shared integration files. No unrelated files were edited.

## Exact source and scope

Barendregt–Geuvers, *Proof-Assistants Using Dependent Type Systems* (2001),
author-hosted 90-page chapter pp.1149–1238, retained PDF in
`citations/Barendregt and Geuvers - Proof-Assistants Using Dependent Type Systems (2001, Handbook of Automated Reasoning, author-hosted chapter).pdf`.
Recorded citation-copy SHA-256:
`48268d36690e8006aa0f6e78b67f553c7a2a17f44b4f394a442241be002b4b2e`.
Readable exact retained extraction:
`tmp/acquisition/src037/geuvers-proof-assistants-retry-01.body.derived-layout.txt`.
Read in the first block: §§3.2–3.4, pp.1185–1202; source rule sheets and current
body/annex/source note. Visually inspected held source p1190 in
`source/references/p12-har-types/lambda-hol-42.png` and p1202 in
`source/references/p12-har-types/pts-bridge-54.png`. Broader chapter reading
is not claimed. Project contracts and research/PDF skill instructions read.

Formal §3 expressly omits definitions/δ; the target is β only. Sorts:
Prop, Type, Type'; axioms Prop:Type, Type:Type'; triples:
(Type,Type,Type), (Prop,Prop,Prop), (Type,Prop,Prop). The earlier request's
βδ regime was corrected by parent/source author; no extended calculus
was invented. The informal §2 βιδ discussion stays separate.

## Constructed results and dependencies

The fragment contains substantive independent constructions, not prose-only
restatements:

- W1: valid-context/source-occurrence equivalence, projection, and thinning
  into any valid context containing the literal declarations.
- W2: every constructor's generation witnesses, plus product injectivity
  from raw confluence. No normalization used.
- W3: type correctness, with the application's type obtained by product
  generation and the actual-argument substitution theorem.
- W4: context conversion preserving later raw annotations and derivations;
  selected variable converts from the new annotation back to the old one.
- W5: direct domain/object syntax stratification, β-stable separation,
  full rule-case classification, proof-declaration deletion by reconstruction,
  and the actual three-stratum well-formed permutation/disambiguation.
- W6: uniqueness of types by structural subject induction, generation, and
  product injectivity; no checker completeness or normalization premise.
- W7: β subject reduction by structural subject induction, including
  reduction in lambda/product annotations and actual root-redex argument
  conversion/substitution. Every finite path then preserves the type.
- W8: a full judgment-dependent λHOL→exact-CC translation and all typing
  rule cases, preserving each designated β contraction. It is not falsely
  represented as an ordinary PTS sort morphism.
- W9a–h, constructed in the second block: exact CC structural/level
  prerequisites; reduction-closed candidates and controlled β expansion;
  finite kind-shape semantic domains; semantic evaluation definedness,
  membership, substitution and typed-conversion invariance; annotation-retaining
  positive-step simulation; the complete fundamental lemma and open-context
  realization; full compatible annotated β strong normalization.
- W10: a concrete failure of the printed inverse λHOL→PREDω derivation map.

W1–W7 and the all-rule transport in W8 are supplied derivational arguments.
They use the main source author's separately authored raw β confluence
and whole-later-context substitution proof. They do not duplicate those
proofs, assume strong normalization, use checker completeness, or introduce
arbitrary PTS generalizations.

## Normalization bridge and now-supplied CC construction

Define h(Prop)=h(Type)=*, h(Type')=Box, extend on syntax homomorphically.
Domain types D are simple arrows over declared domain variables and Prop.
Set σ(D)=* when its rightmost atom is a domain variable, Box when Prop.
Translate Type:Type' to *:Box; D:Type to hD:σ(D); object M:D to hM:hD;
proof p:F to hp:hF; a:Type context declarations become a:*.
All four CC product pairs are needed: notably a mixed
(a→Prop)→a domain maps to (a→*)→a:* through (Box,*,*).
The fragment supplies all rule cases and contraction simulation.

The first block stopped with exact CC SN as an exposed interface. Root's
second proof-construction block targeted that precise gap. W9 has now been
replaced by a substantive direct construction for exact source CC (sorts
*,Box; axiom *:Box; all four triples; full compatible annotated β).
It does not use the chapter's Theorem3.33 statement as a proof or premise.
Combined with W8, the authored argument establishes strong normalization
for the exact β-only λHOL. No separately assumed normalization lemma remains
inside this construction. Independent mathematical/source admission and
reader integration are still pending; this is an author-supplied proof,
not a formal-assistant execution or independent acceptance.

In the first block, a direct λHOL candidate-semantics route was considered
but not adopted:
object terms are simply typed, yet proof quantification over Prop/predicate
domains is impredicative. Assigning a formula candidate without maintaining
the matching denotation/substitution interface would merely assume the hard
step. The second block instead uses the maintained two-interpretation CC
interface from a primary proof source, with all required closure and
substitution details reconstructed; the abandoned direct sketch is not
promoted or relied on.

## Second block: primary proof source and actual W9 dependencies

Existing P7 was inspected before construction:
`handbook/parts/p07/lambda-calculi-and-type-theories.tex:465` has only
`cited=CoquandHuet1988`, and its CoC row remains a citation. No full CC annex
proof was found. The complete existing System F candidate proof has
irreducible types and cannot silently cover constructor/type/annotation
reduction in CC.

Acquired primary source: Herman Geuvers, *A short and flexible proof of
Strong Normalization for the Calculus of Constructions*, Computing Science
Report94/50, Eindhoven, December1994, institutional PDF:
<https://pure.tue.nl/ws/files/2181809/9511424.pdf>.
Identity page:
<https://research.tue.nl/en/publications/a-short-and-flexible-proof-of-strong-normalization-for-the-calcul-2/>.
Retained file:
`source/references/p12-har-cc-normalization/geuvers-1994-report-94-50.pdf`,
1,181,796 bytes, 38 physical pages, SHA-256
`1e5a515c38beb8b91e8c3bc1a0f8705bfc4be96517423e7bd33e0f40efa6edb3`.
Physical page = printed page +2. The repository cover and download-dated
metadata are retained; no hash identity with the 1995 LNCS publication is
inferred. Author's 1995 publication link was found but its web reader failed;
the 1994 report was selected/read as a distinct primary manifestation.

Read: sections1–3, printed pp1–10, with exact definition2.2, classification2.4,
definitions/lemmas3.1–3.15, and section4's opening typed-conversion warning.
Visual inspection: retained source renders printed pp7–10, covering all
interpretation/substitution/fundamental/canonical-valuation formulas.
The whole source is held; later extension proofs/apparatus are not claimed read.

W9 explicitly adapts the report's key-redex saturated sets to ordinary
reduction-closed neutral-expansion candidates, proving the properties used.
The model defines finite kind-shape sets of candidates/functions in ordinary
set theory, not a self-member impredicative universe or inaccessible hierarchy.
It separately proves exact CC level/classification, typed common reducts,
kind-shape invariance, and evaluation definedness before using semantic values.

The raw interpretation is E(*)=d, E(v)=v, E(MN)=EM EN,
E(λv:A.M)=K(λv.EM)EA, E(Πv:A.B)=d EA(λv.EB), with K=λp.λq.p and
inert d. Annotation retention is justified by the proved K candidate lemma.
A root source β step maps to three target β steps; proper-subterm steps,
including annotations and types, lift through their retained target contexts.
No source β step is erased. The fundamental lemma covers both argument
levels and all four product triples. Canonical semantic values plus identity
raw variable valuation realize every finite well-formed open context.

Dependencies remain only the main author's supplied raw annotated β
confluence proof and whole-context Figure3 substitution proof, along with the
structural results already constructed here. CC SN itself, checker completeness,
closed-term SN, weak-head SN and a universe hierarchy are not premises.

## Source correction: the inverse comparison's mixed-domain countercase

In a:Type, D=(a→Prop)→a is formed twice by source Type/Type and has Type.
Printed inverse g maps a:Set and a→Prop:Type. Since D ends in a, the
printed override assigns D:Set; its formation requires missing
(Type,Set,Set), absent from PREDω's exact six triples. Conversion cannot
change those rigid sorts. This disproves that displayed map's claimed
all-derivation preservation/equivalence; it does not refute λHOL SN and
does not affect the forward PREDω→HOL morphism. Source author was informed
and is integrating the concrete countercase separately.

## Boundaries and next action

No child agents, review seats, builds, manuscript renders, prose tests,
contacts, purchases, login, CAPTCHA or security bypass were performed.
Scoped permissions/escalations covered only the two assigned working files
and the new assigned primary source capture directory. Initial sandbox directory
creation and ordinary web-request attempts failed; a scoped directory creation
and normal TLS curl retrieval succeeded. No security workaround was used.
No δ theorem or reader/manuscript normalization-integration claim is supplied.
Full author read-through of both saved artifacts was performed; the root-redex
preservation argument was tightened to retain explicit domain-sort typing,
including the literal Prop case not delivered by type correctness alone.
The second block's W9a–h received a full author read-through and dependency
check. It corrected the top-sort wording to distinguish a typable subject
from Box merely counted as well typed on the right of an axiom. It checked
finite shape-domain nonemptiness, the controlled-expansion side conditions,
every product/binder/app case, and positive annotation-step simulation.
No build, static suite, formal proof-assistant execution, or independent
proof-review success is claimed. The next action is authorized reader
integration of the supplied W1–W9 arguments and the main author's corrected
checker/decoder dependencies, followed by the project's later consolidated
independent gates. W10's source inverse failure remains separately attributed.

## Third bounded block: live P7 consumer and exact formal-draft bridge

Task: trace the current reader route and construct an actual bridge when
its interface exists; do not infer coverage from retained off-route files
or change reader/shared/canonical files. This is construction, not admission.
Inspection checkpoint: 2 October 2026, 12:25–12:34 UTC.

Actual current P7 path:

- `handbook/main.tex:35` inputs `parts/p07`.
- `handbook/parts/p07.tex:119` inputs the actual
  `parts/p07/lambda-calculi-and-type-theories` chapter.
- Its `thm:p07-coc-strong-normalization` begins at line465 and still carries
  `cited=CoquandHuet1988`: exact Coquand–Huet calculus, not a later inductive
  extension.
- Its comparison row at lines567–569 consumes that cited theorem; the live
  `parts/p07/proof-complexity.tex:300–301` likewise prints its cited standing.
- `handbook/annex/p07.tex:8–24` selects the actual P7 annex inputs and has no
  CoC normalization proof input.

The relevant P7 chapter has no explicit CoC grammar, sort/axiom/product
specification, CoC inference sheet, context validity or compatible-reduction
surface. The `lambda-untyped` sheet is unannotated and untyped, not CoC.
Nearby `mltt-intensional` is a different Pi/Sigma/Id/cumulative-universe,
typed-equality calculus. Its Pi beta rule excludes extra Pi eta, while the
separate Abel–Coquand–Dybjer source comparison has typed beta-eta equality.
Neither defines the cited original1988 CoC.

Current P7 snapshots (read-only):

- `parts/p07/lambda-calculi-and-type-theories.tex` SHA256
  `38bda4faaf2189fe47aec71d5c1944e0f3e5bf85153ea4516d2d3c97b649ab4e`.
- `parts/p07.tex` SHA256
  `8fd441c87db6ba9ec9bfaff64dc6637b5a8652c11915ca678379ea936fc8226b`.
- `annex/p07.tex` SHA256
  `a5b49fbbf79f994956fa07a70ffc849fcbdf4609f63ef4da4e8950b017682e06`.

W11a supplies the genuine bijective notation/context/typing/reduction bridge
between W9 and the CURRENT source-author P12 formal CC draft:
`def:p12-har-pts-specifications`, `sheet:p12-har-pts` (registrylines50–57),
and `thm:p12-har-cc-normalization` (bodyline1331 at this checkpoint).
Both have sorts*,Box; axiom*:Box; all four triples; the seven Figure3 rules;
ordered fresh contexts; capture-avoiding substitution; and full compatible
annotated beta. The structural identity map and its inverse preserve all
annotations and binders. The fragment proves substitution commutation,
one-step preservation/reflection at root and every compatible position,
both typing inductions with all seven cases, context validity and both
subject/type well-typedness, and infinite-path/SN equivalence.
This proof is not a claim that an identity map exists to an unspecified
1988 source presentation. Read-only route inspection also established that
the current P12 body/annex drivers do not yet input the `har2001-c18` pair;
there was no `input`/`include` to that pair anywhere in the TeX tree at the
checkpoint. The explicit CC proof is an authored draft, not an already
reader-routed result. W11 identifies that integration dependency rather
than upgrading the draft to a live reader through wording.

Precise residual: obtain/read the original Coquand–Huet1988 mathematical body,
identified only bibliographically here by *Information and Computation*
76(2–3), pp95–120, DOI10.1016/0890-5401(88)90005-3. Its actual notation,
rules, equality/conversion, compatible normalization relation and context
conditions must be matched; eta/delta/universe differences are not guessed.
No such original-source body or exact rule comparison is supplied by this
block. The 1994 proof facet is established separately in W9, and the current
explicit two-sort beta core is bridged by W11a. After routing the source-author
pair, root may connect a P7 consumer explicitly scoped to that core to the
proved P12 result, but must
not silently relabel the original1988 historical source facet as supplied.

All W1–W10 content remains unchanged. Only W11 and this working-record
section were appended. No broad source search, acquisition, child/review,
build, manuscript render, prose test, or reader/shared/canonical edit was
performed in this bounded block.

## Fourth bounded block: actual original1988 qualification and corrective bridge

Root separately authorized35minutes beginning12:35UTC to repair the
underlying original-source dependency, with two new owned paths:
`source/references/p07-coquand1988-qualification/` and
`spec/research/p07-coquand1988-source-qualification.md`. No P7/shared edit.

The actual1988 journal-layout article was acquired from the Illinois CS522
academic rehost,26 pages95–120,1,407,838 bytes, SHA256
`8b43060165c38d8e438ed85bed8ccdf10eecab283130c059883ad12d629e290e`.
Its printed first/last pages,1988copyright, author/title/journal/PII identity,
and needed rules were inspected. Metadata-only priorP7/source035/038 records
were checked first. CORE returned403 and publisher-reader links errored;
neither was bypassed or repeatedly probed. The newly found university route
worked normally. Original qualification is recorded in the assigned note;
it is not a substituted1985/1986 report or the1994 proof source.

Read the needed base/interface extent §§1–3 pp95–105, stripping/proof standing
§§4–5 pp105–110, and variant/extension boundaries §§6–8 pp111–117. Inspected
source pixels pp95–99,101–102,104–105,110,112,120. Full-paper reconstruction or
full bibliography reading is not claimed.

The source interface differs genuinely: one written*, one-based indices,
logical-context product terms Ao, object terms Ai, separate validity/typing
judgments, and restricted/full typed equality variants. Box is not an original
constant; validity maps to target typing atBox. Sourcep110's own Corollary1
is closed stripped-imageSN; full constructed-term normalization is referred
to[15] atp105 andp112. W9's annotated/open proof remains separately supplied.

Two source defects are explicit, visually pinned, and countercased:

- P98's cutoff startsξ0 and increments under binders but fixesk<i, inconsistent
  with one-based indices. Closed(λx:*.1) becomes(λx:*.2). The bridge explicitly
  uses correctedk≤i, not the literal erroneous recurrence.
- P101's starred restricted reflexivity concludesM≃Δ fromM:Δ. `[A:*]` gives
  A≃*, not β-sound and contrary to its own rankLemma6 (ranks0versus1). The
  p102 full replacement actually printsM≃M fromM:N; the full bridge uses it.

W12a–d was appended to the existing proof fragment. It supplies indexed/named
binding, corrected relocation/lookup and binder-removal substitution identities;
a complete joint validity/typing/full-equality induction; strengthened
two-direction endpoint typing transport to make source conversion's target
sort explicit; and positive one-step full compatible β transport including
annotations. Combining withW9 proves annotated open-contextSN for the full
concrete/binding-semantics presentation under the stated relocation correction.
It does not assert a raw bijection toBox, unmodified restricted/full equivalence,
or normalization of the uncorrected literal indexed rule surface.

The original acquisition/readability gap for this interface is repaired.
The remaining adoption boundary is real: root must choose/declare and route
the corrective full source presentation, preserve original1988 and1994-proof
attribution, and reconcile the legacyP7 theorem/consumers. The literal source
defects are not erased, and no source-admission or full-paper status is granted.
AllW1–W11 content is preserved. Author read-through checked the actual W12
joint induction and source formulas; no child/review/build/manuscript-render/
prose-test/security-bypass action was performed.
