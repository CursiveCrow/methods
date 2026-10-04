ACCEPT

# Part VIII round-four source-fidelity admission review

Seat: source fidelity / evidence  
Snapshot reviewed: current frozen Part VIII reader route on 2026-08-21  
Review boundary: source and mathematical-content admission only

## Decision

I find no blocking source-preservation, source-role, mathematical-source,
proof-standing, citation, notation, or reader-route defect in the current live
Part VIII snapshot. The current route is admissible for source/content.

This verdict does **not** close provenance-control fields, literal global
register rows, build, PDF/visual, human, or final-user gates. Those boundaries
are required by `board-part8-admission-2026-08-21/charter.md:11-16` and remain
separate below.

The frozen files I used for the final recheck have these SHA-256 digests:

- `handbook/parts/p08.tex`:
  `8598376cdad4d96757b24a95dfd9106eb7fe02eeab0f882ee82fec46c840d95a`;
- `handbook/annex/p08.tex`:
  `9cb88c24e31f392659cbea2819f83fe4e08d23ee726d05f585e0703488d72e6e`;
- `handbook/parts/p01.tex`:
  `f9e914c3582f835e0a3066dbf7d6003ac435c1bb07f7a0ce847c797aee0f44ef`;
- `handbook/parts/p08/source-map.tex`:
  `af4d506ec623c5bb5b540b1fefce50ffb3a358865a0432d32da278f33cbf77bc`;
- `source/formal-logic-reference.tex`:
  `0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc`.

I did not read another reviewer's Part VIII transcript or conclusion. I made
no manuscript, specification, tool, generated-source, or test edit. I ran no
test suite and no TeX/PDF build.

## 1. Exact inherited-source preservation: checked clean

### Authority, interval coverage, and order

The public source map identifies the frozen authority, edition, and full digest
at `handbook/parts/p08/source-map.tex:5-8`. It states the Part VIII authority
span as forty intervals covering lines 12970--14094, 1,125 lines with no gap,
overlap, duplication, or reordering at
`handbook/parts/p08/source-map.tex:9-12`; the complete ordered interval list is
printed at `handbook/parts/p08/source-map.tex:25-40`.

I independently rechecked the forty live restoration artifacts against those
forty authority slices. After applying only the repository's stated
physical-line-ending comparison rule---terminal CRLF, LF, or CR becomes one LF
while every other byte and line order is preserved
(`tools/check_inherited_restoration.py:27-35`)---all 1,125 lines compare equal.
Every interval is consecutive, every wrapper occurs once and in authority
order, and every artifact digest agrees with its provenance record. I found no
changed formula, heading, status word, proof sentence, example, exercise,
warning, citation, label, or ordering unit.

The first record illustrates the closed correspondence used for every interval:

- authority, edition, physical size, and digest:
  `spec/provenance/SRC-12970-12988.json:3-10`;
- exact inclusive locator and interval digest:
  `spec/provenance/SRC-12970-12988.json:12-16`;
- artifact path, byte/line count, digest, and comparison rule:
  `spec/provenance/SRC-12970-12988.json:32-38`;
- full-transcription standing:
  `spec/provenance/SRC-12970-12988.json:46`;
- public wrapper/destination route:
  `spec/provenance/SRC-12970-12988.json:97-111`.

The corresponding wrapper is exactly the three-line provenance envelope at
`handbook/restoration/scope-SRC-12970-12988.tex:1-3`. The remaining thirty-nine
wrappers have the same one-input shape.

### Live route and non-byte anchors

`handbook/parts/p08.tex:2-64` routes all forty wrappers in authority order and
interleaves editorial additions only while the source hooks are off. The source
map is inserted after the first exact framing interval at
`handbook/parts/p08.tex:3-5`; it neither replaces nor interrupts an inherited
unit. `handbook/main.tex:31-32` loads the non-byte source-anchor hook definitions
before Part VIII. Those hooks add navigation labels around exact environments
without changing any restoration artifact
(`handbook/parts/p08/source-anchors.tex:1-114`).

The source map honestly distinguishes exact material from every editorial
route at `handbook/parts/p08/source-map.tex:44-81`, and expressly says that the
additions neither replace an inherited unit nor promote an inherited sketch at
`handbook/parts/p08/source-map.tex:85-86`. That description matches the live
bytes. There is no duplicate exact unit and no inactive historical P8 body file
is reachable from the current driver.

## 2. Part I symbol registry and reader-surface cleanup: checked clean

The master notation surface is now genuinely reader-routed. `handbook/main.tex:24`
loads Part I before Part VIII; `handbook/parts/p01.tex:36` loads
`handbook/parts/p01/symbol-registry.tex`. The registry declares its normative,
scope-sensitive role at `handbook/parts/p01/symbol-registry.tex:2-12`, routes the
generated master table at `handbook/parts/p01/symbol-registry.tex:22-31`, and
states the binding/precedence policy at
`handbook/parts/p01/symbol-registry.tex:82-128`. Part VIII's public source map
links readers to that registry, the precedence table, and the rule-sheet
catalog at `handbook/parts/p08/source-map.tex:88-92`.

The live CSV and both generated public surfaces agree exactly: 633 rows in
`handbook/registry/symbols.csv`, 633 labeled rows in
`handbook/generated/symbols-tables.tex`, and 633 entries in
`handbook/generated/symbol-index.tex`. Representative repaired P8 rows include
the intermediate-logic identifiers at `handbook/registry/symbols.csv:484`, the
group common-knowledge operator at `handbook/registry/symbols.csv:101`, the
three free-logic consequence relations at `handbook/registry/symbols.csv:586`,
da Costa derivability and consistency notation at
`handbook/registry/symbols.csv:599-600`, and the typed AGM operations at
`handbook/registry/symbols.csv:603-604`. The public free-logic row is present at
`handbook/generated/symbols-tables.tex:729`.

I recursively traversed the current reader graph from the Part I registry,
Part VIII source anchors, `handbook/parts/p08.tex`, and
`handbook/annex/p08.tex`, stripping TeX comments before checking reader text.
The graph contains 100 existing routed files and no missing input. It contains
no reader-visible `\hbstub`, `OPEN`, owed statement, `A-###`, `D-P...`,
`N-...`, `R-...`, `apparatus row`, `register row`, or phase-control token.
Thus the former reader-internal apparatus identifiers and construction notices
are absent from the live surface. Public theorem/definition labels in the
generated lookup remain intentionally visible as navigation, not as internal
campaign obligations.

Inactive historical P8 files still contain comments or old debt prose, but
they are not inputs of `handbook/parts/p08.tex`; they do not form part of the
current reader graph and are not represented as live by the source map.

## 3. Editorial standing and derivative boundaries: checked clean

The editorial/source boundary is explicit and accurate:

- `handbook/parts/p08/source-map.tex:55-57` identifies the intuitionistic file
  as a separately authored derivative rather than exact source;
- `handbook/parts/p08/source-map.tex:58-64` does the same for modal, temporal,
  epistemic, and the group convention;
- `handbook/parts/p08/source-map.tex:65-78` separately identifies the new
  conditionals/deontic/free chapter, many-valued derivative, IMLL semantic
  erratum, relevance/linear derivative, paraconsistent/nonmonotonic chapter,
  and further-reading navigation;
- `handbook/parts/p08/source-map.tex:79-81` correctly assigns the generated
  audit table navigation rather than mathematical-source standing.

The exact source continues to carry its own definitions, theorem language,
examples, exercises, warnings, and proof status. The editorial chapters do not
claim to be literal slices, do not silently replace the exact units, and do not
transfer a source theorem's standing to a wider family, calculus, domain
regime, matrix, or structural-rule package.

The nonempty-group convention is especially clear. The inherited language at
authority lines 13538--13550 says “finite group” and supplies the finite
conjunction and reachability clauses. The immediately routed addition is headed
“Editorial group convention,” selects a nonempty finite subset of the agent
index set, and explains rather than suppresses the coherent empty-group
identities at `handbook/parts/p08/group-operator-convention.tex:1-8`. The active
common-knowledge sheet carries the same nonempty finite hypothesis in its
language, both axioms, and theorem-only induction rule at
`handbook/registry/calculi/hilbert-common-knowledge.tex:2-6`. This is an honest
editorial choice for the selected calculus, not a false claim that the frozen
source explicitly imposed nonemptiness.

## 4. Proof status and annex reciprocity: checked clean

The annex route accurately says that inherited sketches remain beside their
theorems and that the opening annex items are reciprocal navigation rather than
replacement proofs (`handbook/annex/p08.tex:2-10`). The five exact inherited
sketch routes---IPL, four-system modal, LTL, multi-agent S5, and IMLL---identify
the precise omitted lemmas/cases and point back to the exact source at
`handbook/annex/p08/source-sketch-map.tex:3-55`.

Across the live body I found sixteen status-bearing `proved=` or `sketched=`
annex routes and sixteen matching annex items, with no missing target or missing
body back-reference. Cited-only theorems have no annex proof item. Separately
authored proofs remain identified as editorial annex work; for example the
many-valued annex expressly distinguishes its specializations from the exact
generic source proof at `handbook/annex/p08/many-valued-supplement.tex:1-16`,
and its individual proofs are routed at
`handbook/annex/p08/many-valued-supplement.tex:18-133`. The complete new
four-system canonical proof is separately authored and fully stated at
`handbook/annex/p08/modal-completeness-supplement.tex:4-65`; it does not promote
the inherited modal sketch.

No cited result is presented as a local proof, and no inherited sketch is
promoted by a later restatement.

## 5. R4-specific authority and source-role checks

### 5.1 Intermediate-logics lattice: source role accepted

The reader first defines an intermediate logic as a theorem set between IPL and
CPC, closed under uniform substitution and modus ponens
(`handbook/parts/p08/intuitionistic-supplement.tex:484-494`). It then defines the
order by inclusion, arbitrary meets by intersection, joins by generated closure,
and the empty-family bottom/top conventions, obtaining the complete lattice at
`handbook/parts/p08/intuitionistic-supplement.tex:496-507`. The next paragraph
states exactly what the term denotes, why it is needed, and why the displayed
chain is not the whole lattice at
`handbook/parts/p08/intuitionistic-supplement.tex:509-517`. This passes the
technical-name gate: the definition is eliminable, its metalinguistic standing
is stated, nonlinearity explains nonredundancy, and the KC/LC comparison uses
it immediately.

The source role is proportionate. Chagrov and Zakharyaschev's *Modal Logic*,
Oxford Logic Guides 35 (Oxford University Press, 1997), is an authoritative
monograph whose publisher description includes the theory of
superintuitionistic logics; the current bibliography preserves authors, title,
series/number, publisher, and year at
`handbook/bib/handbook.bib:1554-1561`. Fetchable publisher record:
<https://academic.oup.com/book/52910>. The citation supports the broader lattice
context; the displayed meet/join construction is justified directly from the
local definition and is not falsely attributed as a verbatim theorem from that
book.

KC and LC remain separate source claims. KC is cited to Jankov with its weak
excluded-middle schema, finite rooted greatest-world presentation, FMP, and
failure of theorem-level disjunction at
`handbook/parts/p08/intuitionistic-supplement.tex:519-524`; LC is cited to
Dummett with prelinearity, linear frames, FMP, and the same disjunction boundary
at `handbook/parts/p08/intuitionistic-supplement.tex:526-531`. Their bibliography
records are exact at `handbook/bib/handbook.bib:4526-4545` (primary locators:
<https://doi.org/10.2307/2964753> and
<https://doi.org/10.1070/IM1968v002n05ABEH000690>).

The strict chain is not merely asserted: the LC-to-KC derivation and three
strictness countermodels are printed at
`handbook/parts/p08/intuitionistic-supplement.tex:533-560`. The table keeps KC
and LC separate at `handbook/parts/p08/intuitionistic-supplement.tex:563-586`,
and the figure caption says it is only a strict local chain inside the complete
lattice at `handbook/parts/p08/intuitionistic-supplement.tex:588-602`. The
generated audit retrieves the lattice definition and both cited profiles at
`handbook/generated/audit-p08.tex:42-44`.

Verdict: the intermediate-lattice source does exactly the work assigned to it;
the local chain is neither inflated into a classification of the entire lattice
nor misattributed to the background monograph.

### 5.2 Lewis triviality: cited-only standing accepted

The local Adams definition assigns conditional probability an
assertability/uncertainty role rather than a truth-functional truth value at
`handbook/parts/p08/conditionals-deontic-free.tex:460-469`. The Lewis result is
then explicitly `cited=Lewis1976`, restricted to the finite Boolean algebra
generated by two logically independent events, a fixed event in that same
algebra, and every strictly positive probability at
`handbook/parts/p08/conditionals-deontic-free.tex:471-482`. The text expressly
says that no internal proof is claimed. The following boundary confines the
conclusion to fixed-event probability representation and does not infer that
indicatives lack semantics
(`handbook/parts/p08/conditionals-deontic-free.tex:485-494`).

The primary paper is David Lewis, “Probabilities of Conditionals and
Conditional Probabilities,” *The Philosophical Review* 85(3), 297--315 (1976),
DOI <https://doi.org/10.2307/2184045>. The current record preserves all those
roles and locators at `handbook/bib/handbook.bib:1765-1774`. A fetchable copy of
the primary text is
<https://joelvelasco.net/teaching/4310/lewis76-prob_cond_cond_prob.pdf>.
Lewis's source rejects a single proposition whose probability equals the
corresponding conditional probability uniformly over the relevant probability
functions. The handbook's four-atom formulation is a strictly narrower finite
consequence, not a stronger restatement.

The finite consequence also checks independently. If the four atom
probabilities are (x,y,z,w>0), then (P(B\mid A)=x/(x+y)). A fixed event is a
fixed 0/1 selection of those atoms. Varying (z,w) while holding (x,y) fixed
forces the same selection coefficient on both outside-(A) atoms. Setting
(x=y=t) would then require a 0/1-coefficient affine function of (t) to equal
(1/2) for every (0<t<1/2), which is impossible. Thus the exact local
statement follows under the printed hypotheses.

The generated audit and named-result index preserve cited-only status at
`handbook/generated/audit-p08.tex:112` and
`handbook/generated/named-theorem-index.tex:4`; there is no annex item. Verdict:
source scope and proof standing are exact.

### 5.3 Free-logic consequence and quantifier rules: source standing accepted

The selected negative semantics fixes outer and existing domains, total
ordinary-term denotation, strict atomic/equality behavior, and inner-domain
quantification at `handbook/parts/p08/conditionals-deontic-free.tex:7-17`. It
then states why “negative” is necessary and separates positive and neutral
variants at `handbook/parts/p08/conditionals-deontic-free.tex:19-27`. Russellian
elimination and primitive partial descriptions are kept as different formal
presentations at `handbook/parts/p08/conditionals-deontic-free.tex:29-44`; the
three fully typed semantic rows are printed at
`handbook/parts/p08/conditionals-deontic-free.tex:46-73`.

The new consequence notation is defined, rather than merely named, at
`handbook/parts/p08/conditionals-deontic-free.tex:75-85`: negative and positive
consequence preserve ordinary truth, neutral consequence preserves the sole
designated value (mathsf t), and the text explicitly denies that these three
relations constitute one family-wide proof calculus. The guarded universal
instantiation and existential generalization claims at
`handbook/parts/p08/conditionals-deontic-free.tex:87-113` are semantic-validity
claims for the three just-defined model classes. Their exact (E!(t)) guard is
printed in every row; the caption disclaims interderivability of proof calculi.
The guarded existence consequence at
`handbook/parts/p08/conditionals-deontic-free.tex:116-118` has the same scope.

The official Stanford Encyclopedia of Philosophy entry “Free Logic” distinguishes
positive, negative, and neutral treatments, explains quantifier restriction to
existing objects and the corresponding guarded rules, and separates weak and
strong Kleene choices for neutral free logic:
<https://plato.stanford.edu/archives/sum2025/entries/logic-free/>. The local
bibliography records this authoritative reference with all contributor,
container, edition, publisher, date, and URL roles at
`handbook/bib/handbook.bib:3510-3519`. Historical/source roles are also correctly
split among Lambert's negative/free-existence treatment
(`handbook/bib/handbook.bib:3471-3480`), Bencivenga's handbook survey
(`handbook/bib/handbook.bib:3482-3493`), and Lehmann's description treatment
(`handbook/bib/handbook.bib:3496-3507`).

The rule table is therefore a direct semantic consequence of the declared
variant models, not an unsourced Hilbert or natural-deduction calculus. The
three consequence glyphs are registered with precisely that standing at
`handbook/registry/symbols.csv:586` and publicly rendered at
`handbook/generated/symbols-tables.tex:729`. The audit retrieves the definition
at `handbook/generated/audit-p08.tex:103`. Verdict: terminology, consequence,
guards, and source roles are exact at the chosen scope.

### 5.4 P8 ASP removal: accepted, with the global row kept external

The live Part VIII comparison table contains preferential and ranked
consequence, Reiter default logic, circumscription, autoepistemic logic, and AGM
revision at `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:220-235`.
It does not present an ASP row, stable-model semantics, ASP consequence, or ASP
complexity before those notions are defined. Its caption explicitly routes
stable-model semantics and ASP to Part IX at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:236-240`.

That routing matches the frozen P8 content contract: N-b-033 is “default logic
and circumscription entry cards,” and its note says “ASP computational side
lives in P9” (`spec/registers/new-content.csv:105`). The related depth row also
places ASP under the later computational treatment
(`spec/registers/depth-gaps.csv:119`). Part IX then defines the exact finite
ground normal-program reduct, stable model, and answer-set-programming use at
`handbook/parts/p09/logic-in-computer-science.tex:379-391`, with the scoped
finite-propositional complexity statement at
`handbook/parts/p09/logic-in-computer-science.tex:393-396`.

Literal global apparatus row A-092 still asks for an ASP comparison and remains
`open` at `spec/registers/apparatus.csv:93`; its generated closure record also
remains `OPEN` at `spec/register-obligation-closure.csv:419`. The Part VIII
reader neither prints that internal row nor claims it is complete. I therefore
do **not** treat this source/content acceptance as closure of A-092. On the
current source-relative P8 route, removing the substantive ASP cell is the
faithful choice: it obeys definition-before-use and the explicit N-b-033/P9
boundary. Any later global disposition of A-092 is an administrative/register
decision outside this verdict.

## 6. Previously repaired source roles remain intact

### AGM revision and contraction

The current body fixes revision, expansion, and contraction as distinct
operations on deductively closed belief sets and states the source role at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:245-262`. All eight
revision postulates, with unconditional Inclusion and consistency-conditioned
Vacuity, are printed at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:264-283`. All eight
contraction postulates, including the supplementary conjunctive conditions, are
printed at `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:285-307`.
Levi and Harper are distinct identities at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:309-321`. The later
faithful-preorder definition and theorem explicitly restrict the representation
to finite propositional belief sets at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:323-355`. The AGM and
Katsuno--Mendelzon bibliography roles remain correct at
`handbook/bib/handbook.bib:1995-2013`.

### LP versus da Costa (C_1)

The reader fixes one exact (C_1) rather than making a hierarchy-wide claim,
defines (A^\circ), states its formula-level standing, and contrasts it with
LP's designated-value mechanism at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:72-93`. Nonexplosion and
controlled explosion are cited only for that calculus at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:95-108`; the comparison
table preserves the two different mechanisms at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:110-132`. The active
sheet prints da Costa's exact fifteen-postulate presentation and assigns the
controlling role to da Costa 1974 at
`handbook/registry/calculi/hilbert-da-costa-c1.tex:1-18`. The bibliography has
the correct author, article, journal, volume/issue, pages, date, and DOI at
`handbook/bib/handbook.bib:752-761`.

### Lewis VC and Wen's correction role

The body assigns soundness, completeness, and decidability to Lewis 1971, while
Wen 2019 controls the limit-free/corrected-presentation qualification at
`handbook/parts/p08/conditionals-deontic-free.tex:356-364` and
`handbook/parts/p08/conditionals-deontic-free.tex:383-398`. The live calculus
sheet likewise says that Lewis's sources control VC while Wen controls the
corrected Nute-style presentation in which CA replaces non-equivalent MOD
(`handbook/registry/calculi/hilbert-counterfactual-vc.tex:1-11`). The
bibliography keeps Lewis's journal-theorem role separate from Wen's arXiv
correction role at `handbook/bib/handbook.bib:1711-1719` and
`handbook/bib/handbook.bib:1748-1755`.

These repairs have not drifted.

## 7. Citations, calculi, retrieval, and navigation: checked clean

The recursively routed graph has 133 distinct live citation keys, all present
in `handbook/bib/handbook.bib`. I found no unresolved cited key and no changed
author/editor/title/container/version/date/locator role in the repaired records
reviewed above. Source claims are kept at their cited scope; statements derived
locally from definitions are not falsely represented as quotations or local
proofs from those sources.

The graph references 48 distinct Part VIII calculus sheets; every identifier
resolves to an existing sheet under `handbook/registry/calculi/`. Cards do not
substitute prose names for missing rule surfaces, and no theorem for one exact
calculus is generalized to a family. The source map gives readers the public
rule-sheet route at `handbook/parts/p08/source-map.tex:91-92`.

The generated Part VIII audit has 168 entries: 35 exact-source theorem- or
definition-class rows and 133 editorial rows. It preserves the source's
proved/sketched/cited distinctions; representative rows are visible at
`handbook/generated/audit-p08.tex:15-25`, and the repaired intermediate,
free-logic, Lewis-VC, Lewis-triviality, da Costa, and AGM entries are at
`handbook/generated/audit-p08.tex:42-44`, `:103`, `:110-112`, and `:170-178`.

There are 62 live named results in Part VIII (52 editorial results plus ten
inherited named results), and all 62 occur in
`handbook/generated/named-theorem-index.tex`; none is missing from public
retrieval. Together with the 633/633/633 symbol parity above and the source-map
and annex back-links, the public navigation surface is source-complete at the
declared P8 scope.

## 8. Four-lot coverage

| Charter lot | Source-fidelity disposition | Evidence boundary checked |
|---|---|---|
| 1. Intuitionistic/intermediate, translations, algebraic/topological semantics, realizability and IQC | checked clean | Nine exact intervals at `handbook/parts/p08.tex:3-12`; routed derivative at `:14`; exact/editable standing at `handbook/parts/p08/source-map.tex:25-28,55-57`; intermediate-lattice/source checks above |
| 2. Normal/non-normal and quantified modal logic | checked clean | Thirteen exact intervals at `handbook/parts/p08.tex:16-31`; modal derivative at `:33`; source standing at `handbook/parts/p08/source-map.tex:29-33,58-64`; exact sketch and distinct complete annex proof checked |
| 3. Temporal, epistemic, dynamic, hybrid, conditional, deontic, and free logic | checked clean | temporal/epistemic and conditionals routes at `handbook/parts/p08.tex:34-35`; nonempty-group convention at `:28`; Lewis/free-logic/source-role and symbol checks above |
| 4. Many-valued, fuzzy, relevance, linear, Lambek, paraconsistent, adaptive/nonmonotonic, and apparatus | checked clean at the declared P8 source/content scope | Eighteen exact intervals at `handbook/parts/p08.tex:37-60`; editorial routes at `:44,54,62-64`; annex at `handbook/annex/p08.tex:8-10`; AGM/C1/ASP, calculi, citations, generated audit/index/symbol checks above |

No charter lot is unreviewed.

## 9. External gates and exact residual boundary

The source/content verdict is **ACCEPT**. The following are deliberately not
converted into acceptance claims:

- provenance records continue to carry open destination/completeness and
  pending independent-source/build/visual/human fields, exemplified at
  `spec/provenance/SRC-12970-12988.json:40-44,57-76`;
- the literal global register closure remains administrative, including the
  open A-092 record described above;
- no test or TeX/PDF build was run;
- no PDF page was visually inspected in this round;
- no human or final-user acceptance is inferred.

Those are external to the source/content admission requested here, not hidden
Part VIII completion claims. Within the current frozen reader graph, exact
preservation, editorial standing, proof status, citations, definitions,
calculus surfaces, symbols, and generated retrieval are source-faithful.
