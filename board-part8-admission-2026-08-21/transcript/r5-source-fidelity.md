ACCEPT

# Part VIII R5 source-fidelity verdict

Seat: source fidelity / evidence  
Snapshot: current frozen reader tree, 2026-08-21  
Scope: final source/content admission after the two R4 corrections

## Verdict

The two corrections are source-faithful and introduce no downstream drift.
Part VIII remains admissible for source/content.

I did not read any other seat's transcript or conclusion. I edited no
manuscript, specification, tool, generated source, calculus, registry, or test
file. I ran no test suite and no TeX/PDF build. The only file written for this
round is this transcript.

Current pinning digests:

- `handbook/parts/p08.tex`:
  `8598376cdad4d96757b24a95dfd9106eb7fe02eeab0f882ee82fec46c840d95a`;
- `handbook/annex/p08.tex`:
  `9cb88c24e31f392659cbea2819f83fe4e08d23ee726d05f585e0703488d72e6e`;
- `handbook/parts/p08/conditionals-deontic-free.tex`:
  `70c64fef9c8050c26b13ac3b6f01c29eac4e6c3ef4fa8b697bd150c60d2c6e24`;
- `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex`:
  `c53272339480dcd822eadccade5d0ca51adad8a71a4d51a764b4bb091ed89084`;
- `handbook/parts/p08/source-map.tex`:
  `af4d506ec623c5bb5b540b1fefce50ffb3a358865a0432d32da278f33cbf77bc`;
- `source/formal-logic-reference.tex`:
  `0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc`.

## 1. Exact source and editorial standing: accept

The frozen source authority and public source-map digest remain unchanged.
The map identifies the authority and its digest at
`handbook/parts/p08/source-map.tex:5-8`, and identifies the forty consecutive
intervals from lines 12970 through 14094 at
`handbook/parts/p08/source-map.tex:9-12,25-40`.

I independently compared the current forty restoration artifacts with those
forty authority slices, using only the repository's declared terminal
line-ending normalization and otherwise exact byte/order comparison
(`tools/check_inherited_restoration.py:27-35`). Result:

```text
INTERVALS=40 LINES=1125 FIRST=12970 LAST=14094 ERRORS=0
```

All forty artifact digests also equal their provenance-record digests; every
wrapper has the required three-line, single-input form; the intervals are
consecutive and occur once in the order printed by
`handbook/parts/p08.tex:2-64`. No inherited heading, formula, status, proof,
example, exercise, warning, label, citation, or source sentence changed.

Both corrected files are explicitly editorial. The public source map calls
`conditionals-deontic-free` a new sourced editorial chapter at
`handbook/parts/p08/source-map.tex:65-67`, and calls
`paraconsistent-and-nonmonotonic` new sourced editorial material at
`handbook/parts/p08/source-map.tex:77-78`. It also states that additions neither
replace an inherited unit nor promote an inherited sketch at
`handbook/parts/p08/source-map.tex:85-86`. The current route matches those
standings.

## 2. Removal of orphaned Part-IX terms: accept

The current Part VIII nonmonotonic comparison contains preferential and ranked
consequence, Reiter default logic, circumscription, autoepistemic logic, and AGM
revision at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:220-235`. Its caption
now describes only those live rows and attributes their printed complexity
bounds to Gottlob at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:236-239`.

There is no reader-visible occurrence of “stable model,” “answer-set
programming,” or “ASP” anywhere in the active Part VIII body/annex graph. There
is also no such occurrence in the exact authority interval
`source/formal-logic-reference.tex:12970-14094`. Their removal therefore changes
no inherited P8 claim, citation, theorem, calculus, or status.

The frozen content controls support the removal:

- N-b-033 asks Part VIII for default-logic and circumscription treatment and
  expressly says that the ASP computational side lives in Part IX
  (`spec/registers/new-content.csv:105`);
- D-P10-035 assigns default logic, circumscription, and autoepistemic logic to
  P8.7 and assigns ASP to the later computational row
  (`spec/registers/depth-gaps.csv:119`);
- Part IX supplies the actual finite-ground reduct, stable-model definition,
  and answer-set-programming use at
  `handbook/parts/p09/logic-in-computer-science.tex:379-391`, followed by its
  exact finite-propositional complexity boundary at
  `handbook/parts/p09/logic-in-computer-science.tex:393-396`.

The removal does **not** erase or confuse Moore's distinct autoepistemic
notion of a *stable expansion*. That P8 notion remains present in the comparison
at `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:232`, is defined by
its fixed-point equation and differentiated from Reiter extension at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:420-437`, and remains on
the autoepistemic card at
`handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:477-492`. Its Moore 1985
source role is unchanged (`handbook/bib/handbook.bib:2044-2053`), and the
generated audit still retrieves the definition at
`handbook/generated/audit-p08.tex:181`.

Literal global apparatus row A-092 still includes ASP and remains open at
`spec/registers/apparatus.csv:93` and
`spec/register-obligation-closure.csv:419`. Part VIII neither prints that
internal row nor claims it closed. This source/content verdict does not convert
the separate global-register disposition into acceptance.

Verdict on the correction: removing the P9-only terms is definition-before-use
and source-boundary repair, not loss of a required P8 source claim.

## 3. Lewis weak centering: accept

The current sphere definition fixes a nonempty nested family closed under the
stated unions and intersections, defines
\(U_w=\bigcup\mathcal S_w\), and gives the limit-free variably strict truth
clause at `handbook/parts/p08/conditionals-deontic-free.tex:268-288`.

It now defines weak centering by both

\[
 w\in U_w
 \quad\text{and}\quad
 \forall S\in\mathcal S_w\,(S\ne\varnothing\to w\in S),
\]

at `handbook/parts/p08/conditionals-deontic-free.tex:289-295`.

That is exactly Lewis's two-part condition in the manuscript's notation.
Lewis's *Counterfactuals* defines a sphere system as weakly centered at its
world when the world belongs to every nonempty sphere **and there is at least
one nonempty sphere**. Fetchable primary text:
<https://fitelson.org/piksi/piksi_18/lewis_counterfactuals.pdf>, chapter 1,
weak-centering clause W. The current bibliography correctly preserves author,
title, publisher, and date at `handbook/bib/handbook.bib:1722-1727`.

Here the existence component is precisely \(w\in U_w\): since
\(U_w=\bigcup\mathcal S_w\), this says that some sphere contains \(w\), hence
that a nonempty sphere exists. Conversely, if a nonempty sphere exists and
every nonempty sphere contains \(w\), then \(w\in U_w\). The previous
every-nonempty-sphere clause by itself would permit
\(\mathcal S_w=\{\varnothing\}\) vacuously; the added conjunct closes exactly
that gap.

The neighboring distinctions remain correct:

- centered means \(\{w\}\in\mathcal S_w\) at
  `handbook/parts/p08/conditionals-deontic-free.tex:296-297`;
- nesting makes centered imply the now-complete weak-centering condition
  (`handbook/parts/p08/conditionals-deontic-free.tex:297-298`);
- Lewis's \(\mathsf V\), \(\mathsf{VW}\), and \(\mathsf{VC}\) are assigned
  arbitrary, weakly centered, and centered sphere systems respectively at
  `handbook/parts/p08/conditionals-deontic-free.tex:298-300`;
- the limit assumption remains a separate least-permitting-sphere condition at
  `handbook/parts/p08/conditionals-deontic-free.tex:300-308` and is not inferred
  from either centering clause.

The semantic correction is consistent with the calculus. Weak centering makes
conditional modus ponens valid, and the VC sheet assigns exactly that condition
to conditional MP at
`handbook/registry/calculi/hilbert-counterfactual-vc.tex:10`; full centering
controls CS at `handbook/registry/calculi/hilbert-counterfactual-vc.tex:11`.
The centered VC completeness statement remains cited to Lewis 1971, with Wen
2019 controlling the corrected, limit-free presentation at
`handbook/parts/p08/conditionals-deontic-free.tex:358-366` and
`handbook/registry/calculi/hilbert-counterfactual-vc.tex:1-11`. The bibliography
keeps those roles separate at `handbook/bib/handbook.bib:1711-1719` and
`handbook/bib/handbook.bib:1748-1755`.

The notation was already registered; the correction invents no untyped symbol.
\(\mathcal S_w,U_w\) remains the typed Lewis sphere-family/accessible-union
row at `handbook/registry/symbols.csv:593`, publicly rendered at
`handbook/generated/symbols-tables.tex:736` and indexed at
`handbook/generated/symbol-index.tex:276`.

Verdict on the correction: exact Lewis source correspondence is restored, the
VC calculus and theorem roles agree with it, and no limit assumption is
smuggled in.

## 4. No-drift verification of previously accepted surfaces

### Reader route and construction-debt boundary

The recursively routed surface from the Part I symbol registry, Part VIII
source anchors, body, and annex contains 100 existing files and no missing
input. After comments are removed, it contains no reader-visible `\hbstub`,
`OPEN`, owed statement, `A-###`, `D-P...`, `N-...`, `R-...`, phase token,
“apparatus row,” or “register row.” The current live graph declares 344 unique
public labels with no duplicate. Its 245 distinct `\ref`, `\pageref`, and
`\hyperref` targets all resolve on the handbook route.

The Part I notation route remains live: `handbook/main.tex:24` loads Part I,
`handbook/parts/p01.tex:36` loads the registry, and
`handbook/parts/p01/symbol-registry.tex:6-12,22-31,82-128` preserves the
scope-sensitive symbol and precedence contract. Part VIII still links readers
to that registry and the rule-sheet catalog at
`handbook/parts/p08/source-map.tex:88-92`.

### Citations and source roles

The current P8 body/annex graph has 134 distinct keys across citation commands,
entry-source fields, and cited-status tokens; every key resolves in
`handbook/bib/handbook.bib`. No correction changed a citation key or changed an
author/editor/title/container/version/date/locator role.

The previously repaired source-role boundaries remain in place, including:

- intermediate-logics lattice and local-chain standing at
  `handbook/parts/p08/intuitionistic-supplement.tex:484-517,533-602`;
- variant-indexed free-logic consequence and guarded semantic rules at
  `handbook/parts/p08/conditionals-deontic-free.tex:75-118`;
- cited-only Lewis triviality at
  `handbook/parts/p08/conditionals-deontic-free.tex:473-496`;
- the explicitly editorial nonempty-group convention at
  `handbook/parts/p08/group-operator-convention.tex:1-8`;
- exact da Costa \(C_1\) scope and mechanism at
  `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:72-132` and
  `handbook/registry/calculi/hilbert-da-costa-c1.tex:1-18`;
- AGM revision/contraction, Levi/Harper, and finite propositional faithful-order
  scope at
  `handbook/parts/p08/paraconsistent-and-nonmonotonic.tex:244-355`.

### Calculi, statuses, symbols, and generated retrieval

All 48 distinct calculus-sheet identifiers used by the live Part VIII route
resolve to existing registered sheets. The R4 edits add no rule, delete no
rule, and alter no sheet identifier or side condition.

All sixteen `proved=` or `sketched=` body targets still have exactly matching
annex items, and all sixteen annex items retain their body back-reference. The
five inherited sketches remain sketches with reciprocal navigation in
`handbook/annex/p08/source-sketch-map.tex:3-55`; cited-only results still have
no annex proof item.

The generated Part VIII audit remains 168 rows: 35 exact-source rows and 133
editorial rows (`handbook/generated/audit-p08.tex`). The named-result index
still contains all 62 P8 named results, including cited VC at
`handbook/generated/named-theorem-index.tex:347` and cited Lewis triviality at
`handbook/generated/named-theorem-index.tex:4`.

Symbol parity remains exact: 633 CSV rows in
`handbook/registry/symbols.csv`, 633 public rows in
`handbook/generated/symbols-tables.tex`, and 633 rows in
`handbook/generated/symbol-index.tex`. The two corrections require no new
symbol row and leave every existing typed collision boundary intact.

## 5. Gate separation

This is an **ACCEPT** for Part VIII source/content only. It does not close:

- the literal global register rows, including A-092;
- provenance-record destination/completeness or pending independent-source
  fields;
- build or PDF/visual verification;
- human or final-user acceptance.

Those gates remain external exactly as required by
`board-part8-admission-2026-08-21/charter.md:14-16`. Within the current reader
tree, exact-source preservation, editorial standing, Lewis semantics, P8/P9
scope division, citations, calculi, symbols, statuses, and generated retrieval
are intact.
