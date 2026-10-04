# Fused-space repair review

Scope: the uncommitted `find_fused_spaces.py --fix --apply handbook` diff
(49 files), class D candidates, and a hand scan for fusions the detector cannot
see. Status: done, with one open item for the lead (the registry and bib sources
listed under "Forbidden-file hits"). No TeX build was run for this review.

## Counts

| Item | Count |
|---|---|
| Detector insertions reviewed (space or `~`) | 236 in 49 files |
| Accepted as-is | 234 |
| Reverted | 0 |
| Adjusted (space replaced by hyphen) | 1 |
| Converted to math | 1 |
| Tool side effect repaired (bare CR became LF) | 3 occurrences in 1 file |
| Class D candidates reviewed | 105 |
| Class D real fusions fixed | 1 |
| Word-word fusions fixed (step 3) | 4 |
| Further detector-missed fusions fixed in the step-3 scope files | 160 (1 of them converted to math) |
| Calculus-sheet rule display names fixed | 11 |

Files changed now: 52, which is the 49 from the detector plus
`parts/p19/explanatory-preferences.tex`, `parts/p19/neurocognitive-methods.tex`
and `registry/calculi/p13-medieval-latin.tex`. Every edit inserts a space or
`~`, except the six edits listed under "Step 1" below. I checked this by diffing
each changed line against HEAD.

## Step 1: detector insertions

All 236 insertions are a single space or `~`. None broke a system or rule name,
a citation key, a URL or a version string, so none were reverted. Some needed a
closer look, and all of these were kept:

- `parts/p13/presentations/medieval-latin-inference.tex:257,259,260`: `Rules 1 and 2`, `Rule 3o` and `Rule 3b` are kept. The formal labels are the keys `rule:p13-latin-neg-3o`/`-3b`, and the display text "Rule3o" was itself fused (see "Calculus sheet" below).
- `annex/p12/presentations/har2001-c18-polynomial-normalizer.tex:368`: `value 1A` is kept. `1A` is the ring unit in this file, as in `0A` and `chi k+1A`.
- `parts/p12/sources/src-027-501-marked-trees.tex:89` (line 92 before the CR repair): the `from 7*` and `and 7(8)` splits are correct. The other fusions on that line were fixed in step 3.

Changes that are not a plain space insertion:

- **Adjusted.** `handbook/parts/p13/presentations/medieval-latin-inference.tex:474`: the detector turned `pre1325` into `pre 1325`. I changed it to `pre-1325`.
- **Converted to math.** `handbook/parts/p12/presentations/har2001-c18-polynomial-normalizer.tex:283`: the detector turned `and2x` into `and 2x`. I changed it to `and \(2x\)`, which matches the neighbouring `\(x^2\)`.
- **Tool side effect.** `handbook/parts/p12/sources/src-027-501-marked-trees.tex:45,50,51`: HEAD held a bare CR byte where `\r` belonged, a JSON-escape corruption of `\rm`. Git therefore treated the file as binary (`i/-text`). `_read_text` uses universal newlines, so the `--apply` write split those lines at `\leq_{` / `m anc}`. I restored all three to the evident original, `\leq_{\rm anc}`. The book class defines `\rm`. No other handbook `.tex` file contains a stray control character.

## Step 2: class D

There were 105 candidates. One was a real fusion:
`handbook/parts/p13/presentations/abelard-and-contemporaries.tex:26`, where
`NotreDame` became `Notre Dame`.

The other candidates are legitimate and were left alone:

- Rule names: NameApp, RecEval, AbsValue, ZeroTest, PredEval, SuccEval and FalseBranch (annex/p10); AddFeet, SplitSpider, RemoveShading and IntroduceShadedZone (p12 rationality-13-1).
- Coq names: HasProper.
- Fluent and action constants: CurrentBoy, PastBoy, PastYoung, CurrentOld, FutureDie, HasBananas, HasPublications, StopPump, SetSwitch, EnableBackup, TankOxidizer and ReservoirOxidizer.
- Algorithm names in `\textsc`: PerfectRef, SplitPath, PolyRefine, SplitLoop and FiniteRun.
- Scheme names: ExpertOpinion--PositiveConsequences.
- Scenario labels: TrapDoor.
- Products and services: CompCert, PubMed, ScienceDirect, CrowdFlower, PowerPoint, OpenAlex, HathiTrust and ArguMed.
- Surnames: DerSimonian.
- The literal word "CamelCase".

Judgment calls left as written:

- `parts/p09/presentations/n-c-017.tex:3706` `PentiumPro`: an attested period spelling of the Pentium Pro.
- `parts/p11/rationality-12-3.tex` `TrapDoor`: used consistently as a case label.

Forbidden-file hits, all legitimate identifiers, so nothing to do:

- `handbook/main.tex:18-20` (LogicBlue)
- `handbook/restoration/inherited-00035-00037.tex:1-3` (LogicBlue, LogicGray, LogicRed)
- `handbook/restoration/inherited-00039-00047.tex:6-8` (LogicBlue)
- `handbook/restoration/inherited-00158-00169.tex:7` (LogicGray)
- `handbook/restoration/inherited-08710-08876.tex:797` (OutCells, OutNext)

## Step 3: word-word fusions without digits

I scanned the 49 touched files, all of `parts/p13/presentations/*.tex` and all
49 of `parts/p19/*.tex`. The scan split rare tokens against the handbook's own
vocabulary, looked for function words glued to other words, and looked for
lower-to-upper case joins. Fixed:

- `handbook/parts/p19/insight-impasse-and-restructuring.tex:366`: `CRAitems` became `CRA items`.
- `handbook/parts/p19/insight-impasse-and-restructuring.tex:457`: `EEGeffects` became `EEG effects`.
- `handbook/parts/p19/insight-impasse-and-restructuring.tex:377`: `10--50scale` became `10--50 scale`. This has a digit, but the detector's prefix guard hides it after `--`.
- `handbook/parts/p19/explanatory-preferences.tex:463`: `baserates` became `base rates`.

Candidates reviewed and kept:

- `steplock`: part of the source's invented jonks/grummond/steplock example.
- `forcefields`: an attested single word.
- `primediv`: a definition name.
- `Camenop`: a mnemonic.
- `Inconcludent`, `nonfair` and `nonaxiom`: technical coinages.

No `separatefromunheld`-type run remains in these files.

### Further detector-missed fusions fixed in the same scope

The same files held many word-plus-number fusions that the detector does not
see:

- The word is not in `LOWER_A_WORDS`, as in `selects8`, `payoff1` and `Coeff2 4`.
- A comma or colon has lost its following space, as in `students,12`, `groups:18` and `24,48,72,96`.
- A word is glued to inline math, as in `stage\(n+1\)`.
- The text is inside `tabular`/`longtable`, which `_mask_tex` masks as math, as in `Block1` and `All79`.

I fixed the clear prose cases. Each fix inserts a space, with three exceptions:

- `Notation3.2` became `Notation~3.2`.
- `pred0=0` became `\(\operatorname{pred}(0)=0\)`, matching `parts/p10/stable-domains-and-sequential-models.tex:139`. This is the second conversion to math.
- The `har2001` Coq-style text: a space is added before the numeral only where the bare function name is spaced elsewhere in the same file (`Coeff`, `Proper`, `HasProper`, `div`, `propdiv`, `prime`, `times`, `chi`, `plus`, `numeral`).

Fixes listed as line and original token:

- `handbook/annex/p09/negative-premises-and-stratification.tex`: 231 `label0`; 231 `stage\(n+1\)`; 232 `label\(n\)`
- `handbook/annex/p09/sos-congruence-and-conservative-extension.tex`: 206 `neither0 nor`
- `handbook/annex/p10/stable-domains-and-sequential-models.tex`: 303 `including pred0=0.` (converted to math)
- `handbook/annex/p12/n-c-035-05-narrowing.tex`: 320 `a's1.`
- `handbook/annex/p12/presentations/har2001-c18-autarkic.tex`: 274 `source0,`; 275 `source1,`
- `handbook/annex/p12/presentations/har2001-c18-frameworks.tex`: 261 `numerator0, denominator1`
- `handbook/annex/p12/presentations/har2001-c18-kprime.tex`: 248 `Coeff2 4`; 248 `tests1<2`; 249 `Proper2 4`; 252 `HasProper4`; 253 `coefficient2`; 253 `div2 4`; 254 `bounds1<2`; 255 `propdiv2 4`; 256 `prime4`; 357 `bound2<=61`; 358 `times8`; 358 `numeral64`; 375 `bounds62<=63`; 395 `propdiv e61`; 399 `prime61`; 447 `numeral61`; 451 `Coeff d61`; 452 `Proper d61`; 452 `all62`; 453 `all62`; 456 `HasProper61`; 457 `one61`
- `handbook/annex/p12/presentations/har2001-c18-polynomial-normalizer.tex`: 110 `chi0`; 115 `chi0`; 231 `chi0`; 234 `plus0A`; 331 `times1A`; 334 `times1A`; 361 `chi0`; 369 `times1A`; 377 `times1A`
- `handbook/annex/p12/sources/src-027-501-direct-sum.tex`: 178 `depth1`; 179 `depth0`; 299 `become0`; 304 `provide0`; 318 `constants0`; 319 `q-copy,1`; 333 `become7`; 336 `match4,5,6`; 344 `weights2`; 345 `1,2,3;1 to 4,5,6;0 to 7`; 371 `q-copy's1`; 372 `copy's1`; 372 `copy's2`; 373 `yield4,5,6`
- `handbook/annex/p12/sources/src-027-501-marked-trees.tex`: 301 `leaf0`; 302 `labels1,2,3`; 309 `root2`; 310 `marked3-copy`; 310 `its1-child`; 314 `root1`; 314 `marked2-children`; 317 `root1.`; 317 `marked2-copy`; 317 `its1-child`; 342 `leaf0.`
- `handbook/annex/p12/sources/src-027-501-pa.tex`: 9 `therefore4.`; 13 `index2.`; 129 `norm1.`; 289 `indices2 through`
- `handbook/annex/p13/abelard-and-contemporaries.tex`: 288 `Cold,Tepid`; 318 `Animal values0,1,1`; 318 `Well values0,1,0`; 319 `values0,0,1`
- `handbook/annex/p13/medieval-latin-inference.tex`: 310 `reply1.`; 311 `reply0.`; 320 `replies0,0`; 321 `reply1.`
- `handbook/annex/p15/hintikka-inductive-logic.tex`: 152 `target2`; 300 `weights21,7,7,3`; 304 `widths3 and`; 305 `weights7 and`
- `handbook/annex/p16/nonmonotonic-causal-theories.tex`: 234 `time1.`
- `handbook/parts/p07/hott-paths-and-equivalences.tex`: 9 `June19`
- `handbook/parts/p09/sos-congruence-and-conservative-extension.tex`: 203 `July2003`
- `handbook/parts/p10/hsp-varieties-and-equational-representation.tex`: 292 `equation10-1`
- `handbook/parts/p11/rationality-intro.tex`: 894 `solvers,54`; 911 `their50-minute`; 927 `was15/20`; 927 `against3/32`; 936 `the57`; 936 `students,12`; 939 `not57`
- `handbook/parts/p12/presentations/har2001-c18.tex`: 1814 `literal45`; 1832 `specification,0/1`
- `handbook/parts/p12/presentations/n-c-035-05-ac.tex`: 160 `Singleton2`; 160 `singleton3`; 184 `vector4`; 224 `Stickel1975`
- `handbook/parts/p12/presentations/n-c-035-05-combination.tex`: 186 `label1`; 252 `label1.`; 365 `colour1`; 366 `colour2.`; 377 `identity0,`; 385 `Here0`
- `handbook/parts/p12/presentations/n-c-035-05-narrowing.tex`: 36 `footnote11.`; 198 `constants0,a`
- `handbook/parts/p12/sources/src-027-501-direct-sum.tex`: 172 `glyphs1`
- `handbook/parts/p12/sources/src-027-501-marked-trees.tex`: 87 `selects6`; 87 `into7(8)`; 88 `under4.`; 89 `selects8`; 89 `then6`; 89 `marked5-copies`; 91 `marked5-subtree`; 99 `root2`; 99 `the3-node`; 99 `its9-child`; 99 `node's9-child`; 100 `its7-child`; 100 `the8-node`; 100 `the0- and`; 100 `the1- and`; 101 `that8-node`; 102 `the0-node`; 103 `image8`; 103 `parent7.`; 105 `an8`; 105 `internal0`
- `handbook/parts/p12/sources/src-027-501-ordered-markers.tex`: 28 `Notation3.2` (became `Notation~3.2`)
- `handbook/parts/p13/presentations/medieval-latin-inference.tex`: 122 `Dorp's1393`; 525 `footnote65.`
- `handbook/parts/p15/hintikka-inductive-logic.tex`: 309 `widths2,3,3,4`; 312 `cell1`; 320 `width3 and width4`; 321 `Cell1`; 590 `payoff1`
- `handbook/parts/p15/reichenbach-probability-logic.tex`: 579 `German1935`; 579 `English1949`
- `handbook/parts/p15/stochastic-satisfiability-and-inference.tex`: 652 `24,48,72,96`; 652 `32,64,96,128`; 673 `anomalous12-variable,24-clause,`
- `handbook/parts/p19/insight-impasse-and-restructuring.tex`: 186 `two A,two B,one C,one D each`; 187 `participants,17 men/21 women,ages`; 190 `undergraduates,45 women/33 men,ages 18--38,course`; 193 `undergraduates,18 women/16 men,ages`; 195 `groups:18`; 214 `Block1`; 215 `Block1`; 216 `Block1`; 217 `Block2`; 227 `43,126,300,104 seconds for A,B,C,D.`; 234 `same/same,20 same-numerals,19 same-order,`; 236 `67 to 96,64 to 99,64 to 95,71 to 95`; 316 `(10 men,8 women)`; 318 `leaving13.`; 318 `(9 men,10 women)`; 374 `study's30seconds.`; 385 `All79`
- `handbook/parts/p19/neurocognitive-methods.tex`: 232 `Vogel2005`; 398 `Morrison2004` (line 226 already writes "Vogel anchor")

### Calculus sheet

The detector masks all five `\hbrule` arguments, so it never sees these.

- `handbook/registry/calculi/p13-medieval-latin.tex`: 6 `{Rule1}`; 9 `{Rule2}`; 12 `Rule3o:`; 14 `Rule3b.`; 15 `Rule3b:`; 17 `Rule3o.`; 18 `Rule3o-prime`; 23 `Rule3b-prime`; 34 `Burley Rule2`; 36 `{Rule2-prime}`; 38 `{Rule2-double-prime}`. These now match the prose, which reads `Rules 1 and 2` and `Rule 3o`/`Rule 3b`. Rule keys are unchanged.

### Seen in scope and deliberately left

- `annex/p13/medieval-latin-inference.tex:88,91` `cut2-prime` / `cut2-double-prime`: the rule-name form is uncertain, so the lead should decide.
- Identifiers: `annex/p16/cplus-action-language.tex` `Turkey1`; `annex/.../har2001-c18-kprime.tex:46` `l0` and `:325` `n0n1lt`; `parts/p12/presentations/n-c-035-05-ac.tex:165` `h1`/`h2`/`h3`. Uppercase labels are also left: CR1--3, SR1--14, CSFR1, BQ7, CM1, DFA1/2, ACL2, SPM99, NIHMS681047.
- Coq-style comma and colon lists in the har2001 annexes (`n:nat`, `d=O,one,61`, `62<=64,62<=65`) and compact number lists inside formulas (`1,2,3`, `0,1,1`).
- Comma-joined page lists in `\cite[...]` postnotes, such as `pp.~1220,1223` and `pp.~481--483,487`. They occur in about 60 places, house usage is mixed, and the detector masks them.
- `parts/p15/stochastic-satisfiability-and-inference.tex:657,667`: `10,400` and `25,200` are thousands groups.
- `parts/p19/rationality-3-3.tex:77-84`: `\(a=\)designer` is deliberate formatting.
- `% Planned223.5` and `chapter8`: inside comments.

## Possible misses outside the step-3 scope (allowed files, not fixed)

These came from the same scan run over the rest of `parts/**` and `annex/**`.
Most other hits there are identifiers such as c1, k4, s4, Eq0 and v1.1. These
are the likely real ones:

- `annex/p10/hsp-varieties-and-equational-representation.tex:329` `equation10-1`: the twin of the fixed parts line.
- `annex/p11/kripke-truth-fixed-points.tex:23` `Delta11`: probably \(\Delta^1_1\).
- `annex/p12/sources/src-027-501-ordered-markers.tex:305-306` `label3`, `label1`, `label0`.
- `annex/p12/presentations/har2001-c18-lambda-star.tex:96,111,124` `label0`–`label3`: possibly proof-label identifiers.
- `parts/p06/proper-forcing-and-master-conditions.tex:247` `Shelah1982`, `Abraham2010`.
- `parts/p12/presentations/har2001-c18-primitive-recursive-compiler.tex:413,434` `Prime61`.

## Forbidden-file hits left for the lead

`tools/find_fused_spaces.py handbook` now reports only `handbook/generated/*`.
Those hits come from registry data, so regenerating alone will NOT clear them:

- `handbook/registry/symbols.csv:1633` `source1937`, `:1638` `original1933`, `:2052` `Source Section5`, `:2380` `has2 raised to p`.
- `handbook/registry/symbols-intake-p15-factorial-inference.csv:24` `has2`.
- `handbook/registry/symbols-intake-p18-question-evocation.csv:16` `Section5`.
- `handbook/bib/handbook.bib:12407` `Section5.8lines1066--1251 SHA25672c0e0`, in a note field.

## Step 5: final detector run

`python -B tools/find_fused_spaces.py handbook` reports 8 hits, all in generated
files:

- `handbook/generated/symbol-index.tex:44,143,1075,1498`
- `handbook/generated/symbols-tables.tex:1994,1999,2178,2692`

The tokens are `Section5`, `original1933`, `has2` and `source1937`. All of them
trace to the registry rows listed above.

## Detector blind spots (for whoever owns tools/)

1. Class A only fires after words in `LOWER_A_WORDS`/`STRUCTURAL_A_WORDS`, so `selects8`, `payoff1` and `Coeff2 4` are missed.
2. `tabular` is in `MATH_ENVS`, so prose in table cells is invisible (`Block1`, `All79`).
3. The `PREFIX_GUARD` lookbehind blocks `-`, so `10--50scale` is missed.
4. There is no comma or colon rule for `word,12` / `groups:18` or for 2-digit lists such as `24,48,72,96`.
5. A word glued to inline math (`stage\(n+1\)`) is missed.
6. All `\hbrule` arguments are masked, including the display name.
7. Class D needs `Xx..Xx..`, so an acronym followed by a word (`CRAitems`, `EEGeffects`) is missed.
8. `--apply` reads with universal newlines and writes with `newline="\n"`. A bare CR therefore becomes a line break, and any CRLF file it fixes would be converted to LF wholesale. The handbook has 5 CRLF files (`annex/p15/huber-{information-game,joint-endpoints,remaining-methods}.tex`, `annex/p19/mental-rotation-and-spatial-reasoning.tex`, `parts/p10.tex`) and 4 mixed-EOL drivers. None of them were touched in this run.

## Residual candidate pass

Input: `work/waves/tooling/fusion-candidates-filtered.json`, which lists 247
candidates in 160 files. I opened every candidate at its line and read the
lines within 10 above and below it, in all 141 non-driver files. All edits
are byte-level, and every touched file is LF both before and after. No TeX
build was run.

### Counts

| Item | Count |
|---|---|
| Candidates reviewed | 247 |
| Real fusions fixed by insertion (space or hyphen) | 9 |
| Converted to math | 3 |
| Real fusion not fixed (the fix would need a `.`) | 1 |
| Legitimate, left unchanged | 234 (19 of them are `\hbpartidentity{pNN}` in forbidden part drivers) |
| Other fusions fixed within the ±10-line windows (`~` inserted) | 2 |
| Lines changed | 13, in 9 files |

### Fixes (file:line before -> after)

All paths are under `handbook/`.

- `annex/p10/hsp-varieties-and-equational-representation.tex:329` `equation10-1` -> `equation 10-1`. This matches the twin line at `parts/p10/...:292`.
- `annex/p12/presentations/har2001-c18.tex:1775` `PREDomega` -> `PRED-omega` (hyphen). This matches the same file's prose `PRED-omega` at lines 551, 727 and 1136.
- `parts/p12/presentations/har2001-c18.tex:1360` `PREDomega` -> `PRED-omega` (hyphen), for the same reason.
- `annex/p13/medieval-latin-inference.tex:88` `cut2-prime` -> `cut 2-prime`.
- `annex/p13/medieval-latin-inference.tex:91` `cut2-double-prime` -> `cut 2-double-prime`.
- `parts/p06/proper-forcing-and-master-conditions.tex:247` `Shelah1982 and Abraham2010` -> `Shelah 1982 and Abraham 2010` (2 tokens).
- `parts/p12/presentations/har2001-c18-primitive-recursive-compiler.tex:413` `Prime61 computation` -> `Prime 61 computation`.
- `parts/p12/presentations/har2001-c18-primitive-recursive-compiler.tex:434` `printed Prime61 implementation` -> `printed Prime 61 implementation`.
- **Math.** `annex/p11/kripke-truth-fixed-points.tex:23` `Delta11` -> `\(\Delta^1_1\)`. This matches lines 8, 16, 262, 319 and 650 of the same file.
- **Math.** `annex/p16/cplus-action-language.tex:201` `Turkey1` -> `\(Turkey_1\)`. This matches `\(\neg Alive(Turkey_1)'\)` on line 202 and `parts/p16/cplus-action-language.tex:303-341`.
- **Math.** `annex/p16/cplus-action-language.tex:207` `Turkey1` -> `\(Turkey_1\)`, for the same reason.
- **Window fix.** `parts/p12/sources/src-027-501-pa.tex:18` `\parencite[p.21]` -> `\parencite[p.~21]`.
- **Window fix.** `parts/p12/sources/src-027-501-pa.tex:23` `\parencite[pp.30--34]` -> `\parencite[pp.~30--34]`.

### Judgment calls among the fixes

- `cut2-prime` and `cut2-double-prime` were left for the lead in the earlier pass. They are fixed now because the calculus sheet these annex lines prove (`registry/calculi/p13-medieval-latin.tex:36,38`) now displays `Rule 2-prime` and `Rule 2-double-prime`, with the number as its own token. Revert both if the lead prefers a fused rule label.
- `Prime61`: the house form is `Prime(61)` (`parts/p12/presentations/har2001-c18-kprime.tex:211`, "The printed Prime(61) example"). Adding parentheses is not an insertion of a space, `~` or hyphen, so I used the Coq application form `Prime 61`, which the annex also uses ("prove prime 61", `annex/.../har2001-c18-kprime.tex:399`). The lead may prefer `Prime(61)`.
- `Turkey1` was left as an identifier in the earlier pass. It is converted now because every other occurrence in both C+ files is math `\(Turkey_1\)`.

### Real fusion left for the lead

- `annex/p07/presentations/coquand-huet-1988-checking.tex:210`: the annexitem title reads `Direct transport of every p112 rule`. House usage in the same files is `p.~112` (for example `parts/p07/presentations/coquand-huet-1988-checking.tex:33,107,214` and line 281 of this annex). The repair needs a `.` inserted, which this pass is not allowed to do, so the title is unchanged. The same fusion is in `registry/calculi/p07-ch88-checking.tex:1` (`eight p112 construction rules`), outside the windows. That line also has `Coquand--Huet1988`.

### Legitimate (left unchanged)

- All 163 class W candidates:
  - Ordinary words and attested compounds, such as schoolbook, namespace, slowdown, straightedge, arctangent, nullspace, halfspaces, endformula, worklists, powerdomains, pointfree, roundoff, backjumps, lognormal, arcsecond, cutpoints, epicycles, obversion, ninefold, sevenfold, footbridge, switchman, forcefields, affector, timepoint, spacebar and loglinear.
  - Latin: generationem, obligationis, syllogismus, economicus and Martinus.
  - Surnames: Rowbottom, Portmore, Churchman and Greenspan.
  - Rule, action and algorithm names: ZeroTest, FalseBranch, CurrentOld, SetSwitch, SplitPath, SplitLoop and FiniteRun (all three in `\textsc`), ArraysEx, ExpertOpinion--PositiveConsequences and the Coq `Fixpoint`.
  - Products: PowerPoint and ScienceDirect.
- Class A: CCalc, a system name.
- Names with digits (class N, 37):
  - 2SAT, 2EXPTIME (8 sites), KAlt1, seL4, Isabelle2025-2 and NIHMS681047.
  - Report numbers RC1713, RC5587, UMR1083 and UMR1342. The two UMR numbers match the `number` fields in `handbook.bib`.
  - The source identifier `n0n1lt` in a har2001 annex.
  - `\hbpartidentity{pNN}` (19).
- Class P (9): arXiv identifiers (4), `post-1969`, `pre-1325`, `whole-1950-book`, the har2001 Coq list `d=O,one,61`, and `Appendix I,13` (see below).
- A name or word directly followed by math (class M, 24): `Bernoulli\((1/4)\)` and similar (11 sites), `DERIV\((f,g)\)` (3), `probability\(_1\)` and `\(_2\)`, `(ii\(^{\prime}\))` and `(iv\(^{\prime}\))`, `\(\mathsf{PTIME}\)-complete\({}^{\dagger}\)` (2), `Harpist\(\subseteq\)Human\(\subseteq\)FutureDie` (3), and `b\_eq\((S\overline w)O\)`, which is function application; the same file also writes `b\_eq a b` in prose.
- `parts/p12/sources/src-027-501-pa.tex:21` `Appendix I,13`: a locator of the classical-reference kind, and its meaning is uncertain, so it is left as written.
- `parts/pNN.tex:2` `\hbpartidentity{pNN}`: part keys in forbidden driver files.

The windows also contain comma-joined page lists in `\cite`/`\parencite` postnotes, such as `pp.~736,738`, `secs.~1,7` and `pp.~164,167--168`. These were left, as in the earlier pass.

### Possible misses outside the windows (allowed files, not fixed)

Locators with no space or `~` after `p.`/`pp.`, the same fusion as the two window fixes. House usage is otherwise `p.~N`:

- `parts/p09/negative-premises-and-stratification.tex:10,184`
- `parts/p09/sos-congruence-and-conservative-extension.tex:175`
- `parts/p12/sources/src-027-501-direct-sum.tex:8,11`
- `parts/p12/sources/src-027-501-marked-trees.tex:7`
- `parts/p12/sources/src-027-501-ordered-markers.tex:5,18`
- `parts/p12/sources/src-027-501-pa.tex:5`
- `parts/p12/sources/src-027-501.tex:83,100,253,260,307,384,410,451,476,757,772,779,881,893,920,943`
- `parts/p19/rationality-11-2.tex:389`
- `parts/p19/rationality-15-1.tex:401,402`
- `registry/calculi/p07-mll-proof-nets.tex:12`, `p09-sos-formats.tex:13`, `p12-har-types.tex:1,76,78`

A few of these may sit in comments or titles, so check each one before fixing it.

### Verification

`git diff -- handbook` shows 13 changed lines in 9 files. A script compared each `-` line with its `+` line, after substituting the three logged math conversions. Every remaining difference is an inserted space, `~` or `-`, and the result was 13/13 ok. CR byte counts are unchanged in every touched file: all are 0 at HEAD and 0 now.
