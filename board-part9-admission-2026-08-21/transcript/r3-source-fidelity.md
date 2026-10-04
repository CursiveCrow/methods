REJECT

# Part IX R3 source-fidelity admission review

## Independence, snapshot, and gate

I reviewed the current reader graph from the live files and did not read or use
any Part IX R1, R2, or R3 reviewer transcript or conclusion. The reviewed Part
IX body is
`handbook/parts/p09/logic-in-computer-science.tex`, 1,815 physical lines, with
SHA-256
`D65CC5D77D14F6E897840B12367C983B4DFE842BA500A03B9A0A922F51ADD515`.
That is exactly the frozen hash supplied for this round.

The source/content gate is not publication-ready. The decisive defects are
source-presentation completeness, two exact authority mismatches, one
underdefined source variant, one citation-role/metadata mismatch, one
unsupported definition, and one duplicate public result identity. Mechanical
checks were not treated as evidence for source acceptance. I ran no tests and
no TeX/PDF build. Provenance-record disposition, build, visual, human, and
final-user gates remain separate.

## Blocking findings

### SF9-R3-01 — blocker — the live chapter is an editorial synthesis, not the separately reconstructed source presentations required by the binding contract

**Locations.**

- `spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md:3-7,14-21,45-55,62-84,88-97,169-185`
- `spec/research/full-transcription-audit-p09-p14.md:94-131`
- `spec/registers/new-content.csv:108-135,186`
- `spec/registers/depth-gaps.csv:94,133-135`
- `handbook/parts/p09/logic-in-computer-science.tex:11-37,1787-1807`

**Claim.** The live source-standing notice expressly calls Part IX a “newly
sourced editorial synthesis” (`:15`) and assigns whole fields to grouped
secondary/primary source lists (`:22-35`). The binding amendment expressly
supersedes instructions permitting synthesis (`FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md:3-7`),
makes register rows inclusion requirements rather than ceilings (`:45-47`),
requires each source presentation to retain its own notation, hypotheses,
scope, result strength, and proof status (`:48-55`), and prohibits replacement
by capsules, tables, or composites (`:62-84`). The Part IX source ledger makes
the consequence literal: every semicolon-delimited authority is a separate,
fully attributed presentation (`full-transcription-audit-p09-p14.md:98-129`).
Topical coverage, even when mathematically correct, therefore cannot discharge
these source units.

**Concrete current evidence.** This is not merely a missing ledger label.

- `N-c-020` requires the 2001, 2002, 2011, and 2019 presentations, but the live
  route substitutes a 2009 bi-abduction paper and O'Hearn 2007 at
  `logic-in-computer-science.tex:1258-1275`; the 2011 and 2019 registered
  presentations are not routed.
- `N-c-021` requires Pratt 1976, Fischer--Ladner 1979, Kozen--Parikh 1981, and
  Harel--Kozen--Tiuryn 2000. The live PDL sheet cites only Fischer--Ladner and
  Kozen--Parikh (`handbook/registry/calculi/hilbert-pdl.tex:2-12`), and the
  Harel--Kozen--Tiuryn source has no bibliography record.
- `N-c-022` requires a distinct Apt--van Emden 1982 presentation. Its
  bibliography record exists at `handbook/bib/handbook.bib:2479-2488`, but the
  Part IX body and SLD sheet never assign it a presentation role.
- `N-c-023` requires Brewka--Eiter--Truszczyński 2011 in addition to the
  Gelfond--Lifschitz and Marek--Truszczyński presentations. The current stable-
  model route at `logic-in-computer-science.tex:1485-1529` has no such source
  route or record.
- `N-c-025` requires the Feder--Vardi 1998, Bulatov 2017, and Zhuk 2017
  presentations. The live CSP unit supplies only the final Zhuk journal
  presentation (`logic-in-computer-science.tex:1641-1657`;
  `handbook/bib/handbook.bib:5307-5315`).

The same defect affects the authorities that are mentioned but collapsed into
one house presentation: a grouped citation is not a presentation-by-
presentation reconstruction. Cross-part reuse is legitimate only when it
points to an already complete source presentation; it cannot turn a theorem
pointer or comparison-table row into the full source unit demanded at
`FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md:62-65`.

**Exact correction.** For every authority listed at
`full-transcription-audit-p09-p14.md:102-129`, route a separately attributed
presentation packet with an exact source locator and complete checks for the
source's notation, definitions, hypotheses, system/model class, theorem
strength, proof status and proof boundary, examples, and qualifications.
Record nonidentical variants separately. Existing editorial comparison prose
may follow those packets as navigation, but cannot stand in for them. Recheck
the four depth crosswalks only after their source presentations are present.

**Status:** open and independently sufficient for rejection.

### SF9-R3-02 — must-fix — the finite bounded-degree threshold theorem is not a Hanf-1965 theorem

**Locations.**

- `handbook/parts/p09/logic-in-computer-science.tex:106-145`
- `handbook/generated/audit-p09.tex:17-20`
- `handbook/generated/named-theorem-index.tex:208`
- `handbook/bib/handbook.bib:5701-5709`

**Claim.** `thm:p09-hanf-bounded-degree` states the finite, bounded-degree,
radius-and-threshold equivalence theorem but assigns status
`cited=Hanf1965`. That role is historically and mathematically too narrow.
Hanf's original method concerns infinite structures. Fagin, Stockmeyer, and
Vardi explicitly describe their result as a version better suited to finite
structures and prove the threshold form used here. Libkin's authoritative
treatment likewise distinguishes Hanf 1965 from the finite version and says
that the finite threshold theorem is due to Fagin--Stockmeyer--Vardi.

**Authority.** The primary article is Ronald Fagin, Larry Stockmeyer, and Moshe
Vardi, “On Monadic NP vs. Monadic co-NP,” *Information and Computation*
120(1):78-92 (1995), DOI 10.1006/inco.1995.1100; its abstract identifies the
old Hanf technique and the new finite-suited version
([publisher record](https://www.sciencedirect.com/science/article/pii/S0890540185711005),
[author-hosted paper](https://s3.us.cloud-object-storage.appdomain.cloud/res-files/500-infcom95.pdf)).

**Exact correction.** Add an exact `FaginStockmeyerVardi1995` bibliography
record and change the theorem's controlling status to that primary source (or
to a proved local reconstruction with the primary source cited). Keep
`Hanf1965` only for the original historical/infinite theorem. `Libkin2004` may
be cited for its direct finite proof, but must not erase the primary finite
source role. Regenerate the audit and named-result surfaces after the status
change.

**Status:** open.

### SF9-R3-03 — must-fix — Kozen--Parikh does not prove completeness for the exact test-containing sheet printed here

**Locations.**

- `handbook/parts/p09/logic-in-computer-science.tex:1044-1070`
- `handbook/registry/calculi/hilbert-pdl.tex:2-12`
- `handbook/bib/handbook.bib:5228-5248`
- `handbook/generated/audit-p09.tex:55-57`
- `handbook/generated/named-theorem-index.tex:377`

**Claim.** The Part IX grammar contains tests (A?) (`:1048-1054`), the sheet
contains the test axiom `[B?]A\leftrightarrow(B\to A)` (`hilbert-pdl.tex:10`),
and `thm:p09-pdl-adequacy` cites only `KozenParikh1981` for completeness of
that exact registered calculus. Kozen and Parikh's primary paper explicitly
omits the test operator from its language for simplicity and says only that
the proof can be extended with restructuring. Its displayed Segerberg system
also uses the source induction axiom, whereas the registered sheet prints an
editorial theorem-only invariant rule. These may be extensionally related, but
the present route supplies neither an exact source for the test extension nor
an interderivability proof for the altered rule presentation.

**Authority.** Kozen and Parikh, “An Elementary Proof of the Completeness of
PDL,” pp. 113-118: syntax and the explicit omission appear on p. 114; the
source axioms and completeness theorem appear on pp. 114-115
([author-hosted primary PDF](https://www.cs.cornell.edu/~kozen/Papers/ElemPDL.pdf)).
The registered `N-c-021` authority Harel--Kozen--Tiuryn 2000 has dedicated
chapters for PDL, filtration/decidability, deductive completeness, and
complexity ([MIT Press record and chapter list](https://direct.mit.edu/books/monograph/1973/Dynamic-Logic)).

**Exact correction.** Either (a) restrict the theorem and sheet to the exact
test-free Kozen--Parikh language and record the test extension separately, or
(b) add and cite an authoritative source proving completeness for the exact
language with tests, reproduce its exact axiom/rule presentation, and give a
local interderivability proof for every editorially changed rule. Add the
missing Harel--Kozen--Tiuryn bibliography record if that is the controlling
source. Fischer--Ladner may continue to control closure and decision bounds;
that role does not by itself repair the adequacy citation.

**Status:** open.

### SF9-R3-04 — must-fix — “alternation depth” is underdefined and collapses distinct source variants

**Locations.**

- `handbook/parts/p09/logic-in-computer-science.tex:701-717`
- `handbook/bib/handbook.bib:5645-5655`
- `handbook/generated/audit-p09.tex:43-44`
- `handbook/generated/named-theorem-index.tex:392`

**Claim.** The definition says only that alternation depth “counts switches”
along a “dependency chain,” without defining the dependency relation, the
base/index convention, capture treatment, or which source notion is meant.
Bradfield--Stirling §7 expressly separates (i) simple syntactic alternation,
(ii) Emerson--Lei alternation, which ignores closed subformulae, and (iii) the
stronger Niwiński dependency-sensitive classes. The source gives different
depths for the same example under those notions. It then defines symmetric
depth by membership in explicit \(\Sigma^\mu_n/\Pi^\mu_n\) classes. The live
two-line gloss silently identifies these nonidentical presentations and does
not determine the index used by the strictness theorem.

**Authority.** Bradfield and Stirling, “Modal Mu-Calculi,” §7, pp. 741-743 of
the published chapter: the three notions and symmetric-depth definition are
set out before Theorem 7.1, and the theorem's exact hierarchy convention is
then stated
([University of Edinburgh author preprint](https://www.pure.ed.ac.uk/ws/files/16483207/Modal_Mu_Calculi.pdf)).

**Exact correction.** Reconstruct the source definitions separately, or state
one selected notion with its exact \(\Sigma^\mu_n,\Pi^\mu_n\) inductive
classes, substitution/capture clause, base case, and symmetric-depth index;
then state the strictness theorem with the matching indices and source role.
If Part IX wants the switch count as a separate metalinguistic abbreviation,
name and define it separately rather than calling it the source's alternation
depth.

**Status:** open.

### SF9-R3-05 — must-fix — the conjunctive-query theorem conflates Vardi's measure taxonomy with the modern uniform-AC0 result, and the Vardi title is incomplete

**Locations.**

- `handbook/parts/p09/logic-in-computer-science.tex:1531-1579`
- `handbook/parts/p14/master-tables.tex:66-71`
- `handbook/generated/audit-p09.tex:74-76`
- `handbook/generated/named-theorem-index.tex:78-79`
- `handbook/bib/handbook.bib:2159-2166`

**Claim.** `thm:p09-cq-evaluation` assigns one status,
`cited=Vardi1982`, to two different results: fixed-query uniform
\(\mathsf{AC}^0\) data complexity and combined NP-completeness. The prose cites
Chandra--Merlin only for the latter. Vardi's primary extended abstract is the
source for separating data, expression, and combined measures; the current
route does not identify an exact source/proof for the stronger modern
*uniform* circuit formulation. The register itself names
Abiteboul--Hull--Vianu 1995, whose Theorem 17.1.2 gives the AC0 evaluation
result. In addition, the live BibLaTeX title omits the source's printed
“(Extended Abstract)” designation.

**Authority.** Vardi's primary paper defines the measures in its abstract and
introduction ([ACM DOI record](https://doi.org/10.1145/800070.802186)).
Abiteboul, Hull, and Vianu, *Foundations of Databases*, Theorem 17.1.2, states
that every relational-calculus/first-order query is in AC0 and sketches the
constant-depth evaluation construction
([author-distributed book PDF, pp. 431-432](https://wiki.epfl.ch/provenance2011/documents/foundations%2Bof%2Bdatabases-abiteboul-1995.pdf)).

**Exact correction.** Split the source roles: cite Vardi for the complexity-
measure distinction, Chandra--Merlin for combined CQ evaluation, and an exact
modern source or complete local circuit construction for the uniform
\(\mathsf{AC}^0\) bound. If only the Abiteboul--Hull--Vianu theorem is used,
state precisely the AC0 convention it proves; retain “uniform” only with an
authority/argument that fixes the uniformity notion. Correct the BibLaTeX title
to `The Complexity of Relational Query Languages (Extended Abstract)`.

**Status:** open.

### SF9-R3-06 — must-fix — the exact safety/liveness definitions have no claim-local authority

**Locations.**

- `handbook/parts/p09/logic-in-computer-science.tex:30-32,473-481,1798-1801`
- `handbook/bib/handbook.bib` (no Alpern--Schneider record)

**Claim.** `def:p09-safety-liveness` prints the exact bad-prefix definition of
safety and the every-finite-prefix extension definition of liveness, but it
has no local citation. The broad temporal/automata survey role assigned to
`Thomas1997` does not identify the authority for these exact semantic
definitions.

**Authority.** Bowen Alpern and Fred B. Schneider, “Defining Liveness,”
*Information Processing Letters* 21(4):181-185 (1985), DOI
10.1016/0020-0190(85)90056-0, gives the formal liveness definition and the
safety/liveness topological characterization
([publisher record](https://www.sciencedirect.com/science/article/pii/0020019085900560),
[Cornell author bibliography and technical-report route](https://www.cs.cornell.edu/fbs/fullist.html)).

**Exact correction.** Add the exact Alpern--Schneider bibliography record and
cite it at the definition, retaining Thomas only for the automata/language
survey role. If another primary source is intended for safety, name its exact
clause separately rather than leaving both definitions under one broad survey
umbrella.

**Status:** open.

### SF9-R3-07 — must-fix — the route creates a second public TQBF identity while claiming that it does not

**Locations.**

- `handbook/parts/p04/complexity.tex:237-241`
- `handbook/parts/p09/logic-in-computer-science.tex:1762-1778`
- `handbook/annex/p09/proofs.tex:136-207`
- `handbook/generated/audit-p04.tex:135`
- `handbook/generated/audit-p09.tex:84`
- `handbook/generated/named-theorem-index.tex:312,428`

**Claim.** Part IV already assigns TQBF completeness the public identity
`thm:p04-tqbf-pspace`. Part IX says its membership and hardness construction
belongs to that public theorem and “is not assigned a second public identity”
(`logic-in-computer-science.tex:1774-1777`). Nevertheless it wraps the same two
directions in a public `hbtheorem` named `thm:p09-tqbf-proof`, gives it its own
`proved=` status, and publishes both identities in the audit and named-theorem
index. The annex itself closes by saying that its two directions complete
`thm:p04-tqbf-pspace` (`proofs.tex:204-206`). The prose claim is therefore
false, and result identity/status is duplicated.

**Exact correction.** Keep one public theorem identity. The cleanest repair is
to retain `thm:p04-tqbf-pspace`, retarget `annex:p9.tqbf.1` to that theorem,
record its complete local proof status there while preserving the
Stockmeyer--Meyer citation inline, and turn the Part IX block into an unnumbered
proof-navigation paragraph. Remove `thm:p09-tqbf-proof` from the audit and
named index. Alternatively, if the simulation lemma is intentionally a
distinct result, narrow its statement to the genuinely nonredundant lemma and
delete the false “no second identity” claim; the current two-direction theorem
cannot support both assertions.

**Status:** open.

## Register and apparatus disposition

The following records were all checked for a live topical destination; “live”
here is deliberately not “source-complete.” Every `N-c`/`N-x` group remains
blocked by SF9-R3-01 until its separate source presentations exist.

| Register records | Current topical route | Source/content disposition |
|---|---|---|
| `N-c-001`, `002`, `003`, `004` | `logic-in-computer-science.tex:44-173` plus the single P3/P4 public identities it cites | Topic present; `003` also blocked by SF9-R3-02; all source packets open under SF9-R3-01. |
| `N-c-005`, `006`, `007`, `008` | `:175-258` and `tab:p02-decidable-fragments` | Topic/prefix boundaries present; separate Lewis, Mortimer, Grädel, Löwenheim, Behmann, and BGG presentations remain open under SF9-R3-01. |
| `N-c-009`, `010`, `011` | `:261-424`, ALC sheet, ALC annex proof, and DL family table | Topic present; tableau mathematics and OWL-profile role checked clean; source packets remain open under SF9-R3-01. |
| `N-c-012`, `013`, `014`, `015`, `016`, `017`, `018` | `:428-803` plus the explicit P8 ROBDD/LTL/CTL/μ and Büchi-figure reuses | Topic present; SF9-R3-04 and SF9-R3-06 apply; remaining source packets open under SF9-R3-01. |
| `N-c-019`, `020`, `021` | `:1041-1276` and the Hoare, separation, and PDL sheets | Hoare/separation content checked clean; PDL blocked by SF9-R3-03; source packets open under SF9-R3-01. |
| `N-c-022`, `023`, `024`, `025` | `:1278-1657`, SLD sheet, SLD tree, semantics table | Topic present; CQ source role blocked by SF9-R3-05; source packets open under SF9-R3-01. |
| `N-c-026`, `N-c-028` | `:731-803,1659-1778` and `annex:p9.tqbf.1` | Interpolant method and TQBF proof bodies present; TQBF public identity blocked by SF9-R3-07; source packets open under SF9-R3-01. |
| `N-x-015` (live under the amendment) | `:805-1039`: DTMC/MDP/PCTL, CTMC/CSL, atemporal likelihood logic, exact scheduler and numerical-certification boundaries | Substantive topic is live rather than falsely excluded; distinct Halpern and Baier--Katoen presentations remain open under SF9-R3-01. |
| `D-P10-010` | `:483-550` plus the reused P8 Büchi figure | Live topical treatment; source-presentation completion still open. |
| `D-P11-006` | `:1280-1479` plus `sheet:sld-resolution` | Live and operational boundaries checked clean; source-presentation completion still open. |
| `D-P11-007` | `:1485-1638` | ASP and Datalog are kept distinct; source-presentation completion and SF9-R3-05 remain open. |
| `D-P11-008` | `:1098-1276` plus Hoare/separation sheets and `tab:p09-hoare-wp` | Live content checked clean; source-presentation completion still open. |

The Part IX apparatus obligations are physically present: `A-022` and `A-023`
are routed at `handbook/parts/p14/rule-sheets.tex:83-87`; `A-036` is routed by
`logic-in-computer-science.tex:178-234`; `A-051`, `A-079`, and the Part IX
decision rows occur at `handbook/parts/p14/master-tables.tex:11-83`; `A-052` is
reused at `logic-in-computer-science.tex:153-173`; `A-095` is
`tab:p09-description-logic-family`; `A-096` is `tab:p09-hoare-wp` plus the
Hoare sheet; `A-097` is `tab:p09-logic-programming`; `A-147` is the single
reused `fig:p08-buchi-gfp`; `A-148` is `fig:p09-sld-tree`; `A-157` and `A-159`
are routed at `master-tables.tex:245,262`. Their literal `open` values in
`spec/registers/apparatus.csv` are global administrative-control states, not a
substitute for this source review and not an additional reason for this
source/content rejection.

## Checked-clean areas

- **Exact-source route and relocation claim.** Part IX does not duplicate an
  inherited source interval. Its statement at
  `logic-in-computer-science.tex:15-20` resolves to the exact Part II wrapper
  sequence in `handbook/parts/p02.tex`; the public labels
  `ch:second-order-logic` and `ch:simple-type-theory` occur in
  `handbook/restoration/inherited-12249-12261.tex:5` and
  `handbook/restoration/inherited-12721-12783.tex:2`. The two checked artifacts
  have current hashes
  `4009C0CD10412D59613A2DAD30F19DC93493D70B19A588743E7AB512D5078C43`
  and
  `BDD6AFB53913EE0013604E51DBD6EC58A8076C18A50D9DDFCE250313369918F4`,
  matching their provenance records. The still-open
  provenance/build/visual fields in
  those records are external gates.
- **Annex reciprocity and proof bodies.** The ALC proof
  (`handbook/annex/p09/proofs.tex:3-66`), CTL proof (`:69-104`), Hoare proof
  (`:107-134`), and TQBF construction (`:136-207`) are complete at the level
  claimed by their bodies and have reciprocal body links. Only the TQBF public
  identity/status routing in SF9-R3-07 is defective.
- **Calculus routing.** All five Part IX sheets are routed exactly once at
  `handbook/parts/p14/rule-sheets.tex:80-87`. The ALC, Hoare, separation, and
  SLD sheets state their languages, judgement shapes, source roles, and side
  conditions accurately. The PDL sheet is excluded from this clean result by
  SF9-R3-03.
- **Description-logic standards.** The OWL 2 EL/QL/direct-semantics rows at
  `logic-in-computer-science.tex:378-418` preserve the profile/underlying-logic
  distinction and the separate taxonomic, data, query, and combined measures.
  They agree with the official W3C profile definitions and complexity table
  ([OWL 2 Profiles Recommendation, §§2-4 and Appendix](https://www.w3.org/TR/2012/REC-owl2-profiles-20121211/)).
- **Model-checking boundaries.** The LTL/CTL state-versus-path typing, Büchi
  product emptiness test, CTL least/greatest fixed-point labelling, ROBDD
  single-identity reuse, interpolation abort/fixed-point distinction,
  DTMC-versus-MDP scheduler scope, PCTL bounded-step encoding, CTMC/CSL timing,
  and numerical-certification caveats are internally coherent. The
  source-definition exceptions are SF9-R3-04 and SF9-R3-06.
- **Program/database boundaries.** Partial versus total Hoare correctness,
  Apt versus Cook roles, weakest versus weakest-liberal preconditions, frame-
  rule locality, SLD computed answers, ground finite failure, floundering,
  Clark completion, stable versus well-founded semantics, Datalog data versus
  combined complexity, CQ containment versus evaluation, and fixed-template
  CSP are not silently transferred across problem classes. SF9-R3-03 and
  SF9-R3-05 are the exceptions.
- **Technical-name rule.** The new metalinguistic name “reverse depth” at
  `logic-in-computer-science.tex:779-792` has an eliminable definition, a graph-
  parameter standing, an explicit distinction from diameter, and an actual
  use in `thm:p09-interpolant-model-checking`; it satisfies the supplied
  technical-name rule. “Alternation depth” does not yet meet the corresponding
  exact-definition requirement, as recorded in SF9-R3-04.
- **Generated retrieval.** The body has 70 public theorem/definition/method/
  example environments and `handbook/generated/audit-p09.tex:15-84` has 70
  matching rows. It has 38 theorem identities and the generated named-result
  index has 38 matching Part IX rows. The 52 Part IX-local symbol records at
  `handbook/registry/symbols.csv:635-686` appear one-for-one in both
  `handbook/generated/symbols-tables.tex:768-819` and the symbol index. This
  generated agreement correctly exposes, rather than cures, the duplicate
  TQBF identity.
- **Reader debt.** No reader-visible `OPEN`, stub, owed-artifact, placeholder,
  internal register ID, or retired-content notice occurs in the live Part IX
  body, annex, or five sheets. The `Phase-3 skeleton` text in the driver is a
  TeX comment and is not reader-visible.

## Four-lot coverage

1. **Finite-model theory, descriptive complexity, decidable fragments, prefix
   classes:** checked. Not clean because of SF9-R3-01 and SF9-R3-02; the other
   displayed finite/unrestricted, zero--one, Gaifman, capture, and prefix
   boundaries are clean.
2. **Description logics and ontology/query boundaries:** checked clean at the
   current mathematical/editorial layer, including ALC tableau/annex and W3C
   roles; source-presentation completion remains blocked globally by
   SF9-R3-01.
3. **Temporal logics, automata, model checking, and modal μ-calculus:** checked.
   Not clean because of SF9-R3-01, SF9-R3-04, and SF9-R3-06; the remaining
   status, acceptance, scheduler, and algorithm boundaries are clean.
4. **Program logics, logic programming, databases, CSP, complexity, symbols,
   and navigation:** checked. Not clean because of SF9-R3-01, SF9-R3-03,
   SF9-R3-05, and SF9-R3-07; the remaining calculi, annex routes, tables, and
   generated retrieval surfaces are clean.

Final source/content verdict: **REJECT** until SF9-R3-01 through SF9-R3-07 are
repaired against the frozen snapshot and independently re-reviewed. This
verdict neither promotes nor resolves the separate provenance, build, visual,
human, or final-user gates.
