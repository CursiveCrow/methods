ACCEPT

# Part VIII R3 source-fidelity admission review

## Verdict and reviewed snapshot

The current Part VIII reader surface is source/content admissible under the
board charter. I found no blocking defect in exact-source preservation,
editorial source standing, mathematical source support, proof-status/annex
reciprocity, calculus routing, bibliography roles, notation, or generated
retrieval.

This was a blind, read-only review of the current graph. I did not read another
seat's transcript or conclusion, edit a manuscript/spec/tool/generated file,
run a test, or run a TeX/PDF build. The reviewed root hashes are:

- `handbook/parts/p08.tex`:
  `8598376cdad4d96757b24a95dfd9106eb7fe02eeab0f882ee82fec46c840d95a`;
- `handbook/annex/p08.tex`:
  `9cb88c24e31f392659cbea2819f83fe4e08d23ee726d05f585e0703488d72e6e`;
- frozen authority `source/formal-logic-reference.tex`:
  `0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc`.

The charter's separation remains load-bearing: this is a source/content
acceptance, not a provenance-control mutation, build result, visual judgment,
human review, or user acceptance (`board-part8-admission-2026-08-21/charter.md:11-16`).

## 1. Exact-source preservation: checked clean

The public driver turns exact-source hooks on at
`handbook/parts/p08.tex:2`, routes forty provenance wrappers at
`handbook/parts/p08.tex:3-60`, and switches hooks off around every editorial
insertion at `handbook/parts/p08.tex:13-15`, `27-29`, `32-36`, `43-45`,
`53-55`, and `61-64`. The annex route is exactly the three declared annex
components at `handbook/annex/p08.tex:2-10`.

I independently compared every current restored artifact against its inclusive
authority slice and checked its wrapper and provenance locator/hash. The result
was:

`INTERVALS=40 FIRST=12970 LAST=14094 TOTAL=1125 PROBLEMS=0`

Thus the forty intervals are contiguous, ordered, nonoverlapping, and complete;
every one of the 1,125 normalized content lines is equal to the corresponding
authority line; every wrapper names the matching `SRC-start-end` record and
the matching `inherited-start-end` artifact; and every artifact and authority
hash agrees with its provenance record. The printed source map states the same
authority hash, line range, line count, and interval order at
`handbook/parts/p08/source-map.tex:5-12` and enumerates the exact intervals at
`handbook/parts/p08/source-map.tex:25-40`.

The exact intervals contain 35 theorem/definition-class units and 10 named
results. The live generated Part VIII register contains all 35 exact units as
32 synthetic `entry:p08-source-*` anchors plus the three inherited native
labels `thm:glivenko`, `thm:negative-translation`, and
`thm:disjunction-property` (`handbook/generated/audit-p08.tex:15-25`,
`44-53`, `112-119`, and `138-144`). All 10 exact results are present in the
named-result surface. The non-byte hook definitions and result anchors are
declared at `handbook/parts/p08/source-anchors.tex:1-101`, loaded before the
part at `handbook/main.tex:31-32`, and removed for editorial material at
`handbook/parts/p08/source-anchors.tex:103-114`.

I also traversed the body, annex, and source-anchor input graph: 98 files were
reachable, no input was missing, 341 explicit live IDs were unique, and none
was duplicated. Across the live route, all 242 distinct `ref`/`hyperref`
targets resolved to a handbook definition. There is therefore no duplicate or
altered inherited unit and no broken public source route in the reviewed
snapshot.

## 2. Source map and editorial standing: checked clean

The source map expressly distinguishes all interleaved material from exact
source. It classifies the intuitionistic derivative at
`handbook/parts/p08/source-map.tex:55-57`, the modal/temporal/group material at
`:58-64`, the new conditionals chapter at `:65-67`, the many-valued derivative
at `:68-70`, the IMLL erratum at `:71-73`, the relevance/linear derivative at
`:74-76`, the paraconsistent/further-reading material at `:77-78`, and the
generated audit navigation at `:79-81`. The nonreplacement rule is explicit at
`:85-86`, and public symbol, precedence, and rule-sheet navigation is explicit
at `:88-92`.

The body contains no reader-facing `OPEN`, `hbstub`, `owed`, `TODO`, `FIXME`,
or `TBD` construction debt. The remaining lexical matches are mathematical
uses: open sets, open tableau branches, no-open-premise derivations, and the
currently open complexity question for parity games. Those are not completion
notices.

### Editorial group convention

The exact authority says “finite group” and defines (E_G) and (C_G) at
`source/formal-logic-reference.tex:13538-13550`; it does not alter or duplicate
that presentation. The inserted note is visibly headed “Editorial group
convention” and fixes “group” to mean a nonempty finite subset at
`handbook/parts/p08/group-operator-convention.tex:1-4`. It also states the
coherent empty-group identities and explicitly excludes them from the fixed
language/calculus at `:4-8`. The common-knowledge sheet uses exactly the same
nonempty-finite domain and types every rule accordingly at
`handbook/registry/calculi/hilbert-common-knowledge.tex:2-6`.

This is an honest editorial restriction, not a retroactive claim about the
source bytes. Its necessity, definition, standing, nonredundancy, and later
use are all local and explicit, and the source map identifies it as non-exact
at `handbook/parts/p08/source-map.tex:58-64`.

## 3. Highlighted source-role repairs: checked clean

### A-093: AGM revision, contraction, Levi, and Harper

The live definition separately fixes belief-set revision and contraction at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:246-263`. The revision
table at `:265-283` contains exactly Closure, Success, Inclusion, Vacuity,
Consistency, Extensionality, Superexpansion, and Subexpansion, with the
consistency hypothesis correctly attached to Vacuity rather than Inclusion.
The contraction table at `:286-307` separately contains Closure, Inclusion,
Vacuity, non-tautological Success, Recovery, Extensionality, Conjunctive
Overlap, and Conjunctive Inclusion. Levi and Harper are correctly typed as
cross-operation identities at `:310-322`:

- (K*A=(K-\neg A)+A);
- (K-A=K\cap(K*\neg A)).

The finite-signature faithful-preorder theorem is explicitly scoped to
consistent belief sets and valuations at `:324-350`, distinguishes that
presentation from AGM partial-meet contraction at `:351-354`, and excludes
database update, iterated revision, and belief-base revision at `:354-356`.
That prevents an AGM-family overreach.

The controlling bibliography records have the correct source roles and
metadata: AGM's primary article is
`handbook/bib/handbook.bib:1995-2004`, and Katsuno--Mendelzon's finite
propositional faithful-preorder source is `:2006-2013`. The primary AGM article
is fetchable at <https://doi.org/10.2307/2274239>. I found no altered postulate,
reversed inclusion, missing side condition, or false identity. A-093 is
substantively closed on the reader surface.

### A-094: LP versus da Costa (C_1)

The repaired definition fixes one calculus, da Costa's propositional (C_1),
rather than transferring a statement to the entire hierarchy
(`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:72-90`). It types
(A^\circ=\neg(A\land\neg A)) as an eliminable formula-level
well-behavedness/consistency abbreviation, not a matrix value or a
metalinguistic consistency assertion (`:76-84`). The nonexplosion theorem
states both the unrestricted failure and the additional-premise controlled
explosion judgment at `:95-108`. The comparison table then keeps LP's
designated-value semantics separate from (C_1)'s proof-theoretic
formula-level mechanism at `:110-132`.

The active calculus sheet gives the exact primitive language, definition of
(A^\circ), uniform substitution, sole primitive rule, and controlling source
at `handbook/registry/calculi/hilbert-da-costa-c1.tex:1-3`. Its numbered rules
at `:4-18` reproduce da Costa's postulates (1)--(15): the positive implicative,
conjunctive, and disjunctive core; excluded middle; double-negation
elimination; the (B^\circ)-restricted reductio postulate; and the three
well-behavedness propagation postulates. The primary article prints that
language/abbreviation and those postulates on its pp. 498--499 and records the
failure of explosion immediately afterward; it is fetchable at
<https://doi.org/10.1305/ndjfl/1093891487>. The BibLaTeX record matches the
article at `handbook/bib/handbook.bib:752-760`.

The sheet is publicly rendered at `handbook/parts/p14/rule-sheets.tex:80-84`.
Its new notation is registered at `handbook/registry/symbols.csv:598-599`,
rendered at `handbook/generated/symbols-tables.tex:741-742`, and indexed at
`handbook/generated/symbol-index.tex:38` and `:302`. The conditional-logic
alias (mathsf{C1}) and da Costa calculus (mathsf C_1) remain separately
typed and sourced. A-094 is substantively closed on the reader surface.

### Corrected free-logic terminology

The selected negative free-logic model has total outer-domain denotation,
inner-domain existence, strict atoms/identity, and inner-domain quantifiers at
`handbook/parts/p08/conditionals-deontic-free.tex:7-17`. The text now correctly
calls an outer-domain value “denoting but nonexisting,” not “non-denoting”
(`:16-17`). It separates negative, positive, and neutral partial semantics at
`:19-25`; calls the instantiation condition an inner-domain existence premise
at `:29-32`; keeps undefined primitive descriptions distinct from total
ordinary terms at `:34-49`; and gives each variant its own denotation, atomic,
identity, quantifier, and description policy at `:51-84`. The claims are
confined to the declared presentations and supported by the cited Lambert,
Bencivenga, Russell, Lehmann, and Gratzl--Pavlović--Nolt sources. I found no
remaining denotation/existence terminology swap.

### Lewis 1971 and Wen 2019

The live sphere definition fixes nested sphere systems, the limit-free truth
clause, weak centering, centering, and the separate limit assumption at
`handbook/parts/p08/conditionals-deontic-free.tex:234-276`. The VC theorem now
has `cited=Lewis1971` at `:322`, and its statement is limited to Lewis's
centered system and the exact displayed limit-free semantics at `:323-329`.
The corresponding system card gives Lewis 1971 the adequacy and decidability
roles at `:349-363`.

Those roles match the primary sources. Lewis's 1971 article introduces the
limit-free variably-strict models, calls the centered system (C1), and proves
the completeness and decidability results; its metadata is correctly recorded
at `handbook/bib/handbook.bib:1711-1720` and the primary publication is
fetchable at
<https://doi.org/10.1111/j.1755-2567.1971.tb00061.x>. Lewis 1973 supplies the
later (V/VC) sphere presentation used by the definition.

Wen 2019 has the narrower, correct role: its introduction states that Lewis
1971 called (V) and (VC) by (C0) and (C1), and it proves that the popular
Nute presentation is not equivalent until CA replaces MOD. The paper is
fetchable at <https://arxiv.org/abs/1910.06202> (especially its introduction,
paragraphs 1--4). The active VC sheet says exactly that at
`handbook/registry/calculi/hilbert-counterfactual-vc.tex:1-5` and displays ID,
CA, CSO, CV, CMP, and CS at `:6-11`. Wen is not used as the source of the
limit-free semantic theorem; Lewis 1971 is the theorem's controlling status.
The Wen record is correctly typed as an online arXiv work at
`handbook/bib/handbook.bib:1748-1755`.

## 4. Proof standing and annex reciprocity: checked clean

The body has 16 live `proved=annex:*` or `sketched=annex:*` tokens, targeting
16 distinct annex items; all 16 targets exist and none is mismatched. The annex
root correctly distinguishes reciprocal navigation for five inherited sketches
from separately authored proofs at `handbook/annex/p08.tex:3-10`.

- The IPL, modal, LTL, multi-agent S5, and IMLL source-sketch records identify
  the exact omissions and route back without promotion at
  `handbook/annex/p08/source-sketch-map.tex:3-56`.
- The finite Łukasiewicz, Bochvar, Post, K3, LP, FDE, and K3/LP-duality proof
  bodies are present at
  `handbook/annex/p08/many-valued-supplement.tex:18-133`.
- The separately authored full canonical proof for (K,KT,S4,S5) states the
  deduction/Lindenbaum/existence/truth-lemma dependencies and frame-property
  cases at `handbook/annex/p08/modal-completeness-supplement.tex:3-65`.

The exact source sketches remain exact in the body, and no annex navigation
record silently upgrades `sketched` to `proved`. Conversely, every editorial
`proved` token has a nonempty proof body rather than a citation or pointer.

## 5. Calculus and citation source surfaces: checked clean

The live Part VIII body contains 48 distinct calculus-sheet references. Every
one resolves to a `calculussheet` definition, and every owning registry file is
rendered exactly once in the Part XIV catalog; there were zero missing sheet
definitions and zero missing Part XIV routes. The catalog routes the modal,
conditional, temporal/epistemic, many-valued/paraconsistent, and
relevance/linear/Lambek sheets at `handbook/parts/p14/rule-sheets.tex:41-94`
and states the nonreplacement and source-record contract at `:96-105`.

The highlighted C1 and VC sheets have explicit controlling citations. The
older extracted sheets retain their inherited lineage, while separately
authored sheets are tied to the matching body system card/source record; no
sheet is presented as an exact source replacement. I found no rule list used
under a different calculus name, no theorem-only rule used on open premises,
and no family claim transferred from one selected sheet.

Across the live body/annex graph, 134 distinct bibliography keys are used and
all 134 exist in `handbook/bib/handbook.bib`. Critical revised roles are
record-to-claim exact: da Costa 1974 controls (C_1); Priest 1979 controls LP;
Lewis 1971 controls (C1/VC) adequacy and decidability; Lewis 1973 controls
sphere semantics; Wen 2019 controls the alias/corrected Nute presentation; AGM
1985 controls belief-set revision/contraction and the Levi/Harper bridge; and
Katsuno--Mendelzon 1991 controls the finite faithful-preorder presentation.

## 6. Generated audit, named-result, symbol, and public navigation surfaces

The live generated Part VIII theorem/definition register has 166 unique rows:
35 exact-source units and all 131 live editorial theorem/definition-class
labels. No live class label is omitted (`handbook/generated/audit-p08.tex:1-181`).
The named-result index contains all 62 live Part VIII result labels (the 10
exact results plus 52 separately authored theorem/lemma/proposition/corollary
labels), including (C_1) nonexplosion at
`handbook/generated/named-theorem-index.tex:263`.

The symbol registry and both generated public symbol surfaces agree exactly at
632 rows each. Besides the (C_1) rows identified above, group epistemic
notation is present in the registry at `handbook/registry/symbols.csv:100-101`
and `:535-536`, in the generated tables at
`handbook/generated/symbols-tables.tex:606-607` and `:678-679`, and in the
symbol index at `handbook/generated/symbol-index.tex:80`, `:93`, `:109`, and
`:536`. The new convention therefore has typed notation and public retrieval;
it is not an unregistered editorial primitive.

## 7. P8 register ceilings and apparatus: source/content disposition

I checked the current reader treatment against all literal P8-targeted
new-content and depth rows and against the P8 rule-sheet/table/figure apparatus
ceilings. The route meets the declared treatment level without converting a
survey/statement ceiling into an unproved theorem or generalizing from one
calculus to a family:

- Lot 1: N-b-030--031 and D-P10-013--019 are realized, with the BHK and
  intuitionistic-mathematics principles explicitly kept at explanatory/source
  boundaries, at `handbook/parts/p08/intuitionistic-supplement.tex:246-579`.
- Lot 2: N-b-001--009 and D-P10-001--008 are realized with fixed frame/model
  hypotheses, explicit source statuses, and separate incompleteness/two-index
  boundaries at `handbook/parts/p08/modal-logics-supplement.tex:22-1028`.
- Lot 3: N-b-010--018, D-P3-008, D-P10-009, D-P10-011--012, and
  D-P10-037--038 are realized at
  `handbook/parts/p08/temporal-epistemic-supplement.tex:21-730` and
  `handbook/parts/p08/conditionals-deontic-free.tex:5-475`.
- Lot 4: N-b-025--033 and D-P10-020--030, D-P10-032--033, and
  D-P10-035--036 are realized at
  `handbook/parts/p08/many-valued-supplement.tex:21-545`,
  `handbook/parts/p08/relevance-linear-supplement.tex:1-708`, and
  `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:2-512`.
  The excluded quantum-logic, adaptive-logic, and formal-argumentation rows
  N-x-006, N-x-007, and N-x-009 remain honest scope exclusions, with sourced
  navigation rather than false completion at
  `handbook/parts/p08/relevance-linear-supplement.tex:693-708`.

The P8 table obligations A-076--A-094 are all reader-visible. In particular,
A-093 is now two exact tables plus the identities at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:265-322`, and A-094 is
the exact two-mechanism table at `:110-132`. The modal, intuitionistic,
temporal, epistemic, Barcan, many-valued, t-norm, relevance, linear,
substructural, conditional, deontic, free-logic, and nonmonotonic table labels
are present at the corresponding live locations:

- `handbook/parts/p08/modal-logics-supplement.tex:74`, `:418`, `:486`, and
  `:994`;
- `handbook/parts/p08/intuitionistic-supplement.tex:180` and `:543`;
- `handbook/parts/p08/temporal-epistemic-supplement.tex:299` and `:683`;
- `handbook/parts/p08/many-valued-supplement.tex:271` and `:441`;
- `handbook/parts/p08/relevance-linear-supplement.tex:224`, `:341`, and
  `:589`;
- `handbook/parts/p08/conditionals-deontic-free.tex:77`, `:203`, and `:389`;
- `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:132`, `:241`,
  `:283`, and `:307`.

The P8 figure obligations A-136--A-147 and A-153 are also live, including the
intuitionistic countermodels and intermediate lattice at
`handbook/parts/p08/intuitionistic-supplement.tex:80`, `:100`, and `:578`; the
modal lattice/countermodels and Barcan countermodel at
`handbook/parts/p08/modal-logics-supplement.tex:360`, `:624`, and `:1028`; the
LTL, CTL, and Büchi figures at
`handbook/parts/p08/temporal-epistemic-supplement.tex:324`, `:350`, and `:401`;
and the Routley--Meyer and substructural maps at
`handbook/parts/p08/relevance-linear-supplement.tex:40` and `:621`.

The literal control records nevertheless remain administratively open. For
example, A-093/A-094 are still `open` in
`spec/register-obligation-manifest.csv:420-421`; their corresponding
new-content/depth records are also still open at `:120`, `:122`, `:229`, and
`:245`. The exact-restoration records likewise retain pending independent,
build, visual, and compatibility fields. Those states require the separate
closure workflow. They are not reader-visible source/content debt and, under
the charter's explicit gate separation, do not reverse this admission verdict.

## Coverage and external gates

- Lot 1 (intuitionistic/intermediate): **checked clean** for exact source,
  editorial claims, source roles, proof standing, notation, and apparatus.
- Lot 2 (modal/QML): **checked clean** for exact source, fixed model/frame
  hypotheses, calculus variants, source roles, proof standing, and apparatus.
- Lot 3 (temporal/epistemic/conditional/deontic/free): **checked clean** for
  exact source, the nonempty-group editorial boundary, source roles, fixed
  semantics/calculi, and apparatus.
- Lot 4 (many-valued/fuzzy/relevance/linear/Lambek/paraconsistent/
  nonmonotonic plus public retrieval): **checked clean** for fixed systems,
  designated-value and proof-theoretic boundaries, citations, proofs,
  calculus sheets, symbols, audit/named indexes, and apparatus.
- TeX/PDF build, PDF visual inspection, control-record closure, provenance
  status mutation, human review, and user acceptance: **not checked and
  intentionally external**.

No source/content correction is required before Part VIII admission.

ACCEPT
