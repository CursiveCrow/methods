# Finite probability and Kamp III.2 Lemma 1: blind publication-text and integration review

Date: 7 September 2026. Review context: `/root/probability_kamp_l1_publication_review`.
Review began at 20:35 UTC; findings filed before the 20:50 UTC checkpoint.
Repository: `C:\Dev\the-methods-of-reason`; branch `phase4-codex`;
HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`. The working tree contains
substantial existing work; HEAD alone does not identify the reviewed content.

## Verdict and limits

**The four frozen target texts PASS this publication-text review. Their active
body and proof routes, all eight result/proof target pairs, and the bounded
stable ownership/status/card/annex interfaces PASS source inspection. Present
P15 notation and validation compatibility FAIL on findings F1 and F2 below.**

The seventeen new symbol rows and their isolated table/index projections PASS
for the meanings, qualifications, scope identifiers, anchors and correspondence
actually supplied. That bounded result does not establish complete P15 notation
coverage: the existing numerical-order declarations leave P15 outside their
scope. The active publication apparatus also still consumes earlier generated
files, so publication of the candidate notation remains UNRESOLVED.

| Scope | Verdict | Meaning |
| --- | --- | --- |
| P15-U1 body, lines 1–461 | PASS | Definitions, statements, examples and finite/general boundary are coherent in the frozen text. |
| P15-U1 proof annex, lines 1–284 | PASS | The seven advertised finite proofs cover their stated components and cases. |
| Kamp III.2 Lemma 1 body, lines 1–202 | PASS | The exact-stage grammar, strict temporal convention, finite construction and remaining III.2 boundary are clear. |
| Kamp III.2 Lemma 1 annex, lines 1–212 | PASS | Both directions of the chain and temporal constructions are supplied, including endpoint cases. |
| New canonical notation rows 917–933 | PASS | All seventeen entries describe the supplied notation accurately at the text level. |
| Corresponding isolated table/index entries | PASS | All seventeen candidate registration anchors and index references correspond to their canonical rows. |
| P15 numerical-order notation coverage | FAIL | F2: the existing `<` and `\leq` declarations stop at P14. |
| Current handbook symbol-checker compatibility | FAIL | F1: the checker treats `global` and P15 scopes as disjoint. |
| Stable ownership/status/card/annex interfaces | PASS | Bounded source inspection supports P15 as owner and XI as its present printed ordinal. |
| Active body/annex routing and eight result/proof pairs | PASS | The supplied files are reachable and their forward/backward targets agree. |
| Publication of the candidate notation apparatus | UNRESOLVED | Active inputs still point to earlier files under `handbook/generated/`. |
| Full nineteen-part migration | UNRESOLVED | There are fifteen current body drivers; P16–P19 remain absent as disclosed in `main.tex`. |
| Primary-source fidelity, build, rendering, visual quality and admission | UNRESOLVED in this review | These require their separately assigned evidence and gates. |

This report was written before reading any other new review or author
conclusions. No source note, candidate README, new author completion report or
other review report was used. The primary source bodies were left to the
separately assigned source-fidelity reviewer. Source descriptions below refer
to what the manuscript expressly attributes; they are not a substitute for
verification against those bodies.

No manuscript, style, registry, generator, canonical output or admission record
was edited. No test suite, checker, build, renderer or publication command was
run. Evidence consists of complete target-text reading, bounded dependency
reading, source searches, direct reasoning about displayed mathematics and
source code, and SHA-256 inspection. This report is the sole file written by
this reviewer.

## Findings requiring correction

### F1 — The handbook checker's global symbol scope excludes P15

Severity: P2. Verdict: FAIL for the symbol-validation compatibility prerequisite.

`tools/check.py:1468–1505` parses registry scopes. At line 1480, it defines
`full = set(range(100, 1500))`, explicitly covering only P1–P14. Lines 1481–1482
return that set for `global`. The endpoint parser at lines 1484–1491 maps
`P15.1` to 1501. Consequently, the intersection of the returned `global` scope
with `P15.1` is empty. Lines 1538–1541 skip collision checking when this
intersection is empty.

This is a concrete false-negative path in the validator now that P15 is active:
a glyph registered globally and again in P15.1 would bypass the overlap gate.
It does not demonstrate that any of the seventeen supplied glyph strings
currently collide. It demonstrates that the existing validation gate cannot
support a P15 compatibility claim. The separate generator already covers
stable parts 1–19 in `tools/symbols2tex.py:40–44`, so the two tools disagree.

Correction: make the handbook checker's global domain cover the approved stable
part IDs and retain its chapter-level distinctions. Verify that `global`
overlaps P15.1 and the remaining approved new parts, and that existing disjoint
chapter scopes remain disjoint. This is a shared checker correction, outside
this reviewer's write ownership. The governing requirement is
`spec/EDITION-2026-CONTRACT.md:109–113`: compatibility work must precede new
driver insertion, including symbols and review/part validation.

### F2 — P15 uses numerical comparison notation outside its registered scopes

Severity: P2. Verdict: FAIL for P15 notation coverage at this frozen registry.

The numerical `\leq` declarations in `handbook/registry/symbols.csv:79–83`
cover earlier part/chapter scopes; the last canonical-order row, line 83,
ends at `P14`. The numerical `<` declarations at lines 85–87 also end at
`P14`. No P15 numerical-order row occurs among the new entries at lines
917–933, and a search of the registry finds no alternative declaration covering
these numerical roles in P15.

The new probability chapter substantively uses `\leq`, for example in
`handbook/parts/p15/finite-probability.tex:61–62` and `:374–375`, and `<`, for
example in `:147` and `:203–205`. Their mathematical readings are evident;
the failure concerns the handbook's explicit normative registry interface.
`handbook/parts/p01/symbol-registry.tex:6–12` and `:40–44` make scope part of the
declaration. `handbook/CONVENTIONS.md:216–222` likewise requires honest local
standing and scope. The addition of P15 therefore exposes an actual uncovered
use, even though the seventeen newly added composite entries themselves are
accurate.

Correction: supply the numerical-order role in the required P15 scope, either
through a justified extension of the corresponding canonical ranges or through
an explicit P15 declaration that preserves the existing object-language
exceptions. Audit later new parts before extending those same roles there.
Regenerate and review the affected candidate table/index after the registry
correction. No mathematical change to the four target files is indicated by
this finding.

## Open construction boundary: candidate apparatus is not yet the active apparatus

This is UNRESOLVED publication work, rather than a demand to bypass admission.
`handbook/parts/p01/symbol-registry.tex:46` inputs
`generated/symbols-tables`, and `handbook/parts/p14/master-tables.tex:275` inputs
`generated/symbol-index`. Their live files have 1,049 and 855 lines respectively
and lack all registration IDs `00917` through `00933`. The inspected candidate
files have 1,143 and 933 lines and contain those entries.

Thus the new body/proof content is reachable from `main.tex`, while these new
notation rows are currently available only in the isolated candidate outputs.
The edition contract at lines 155–161 requires lookup generation from admitted
content projections; this review grants no permission to substitute raw
candidate output for that admission process. After the appropriate admission
and corrected registry projection, the active apparatus needs generation and
its own validation. Its present state does not refute the candidate content
PASS, but it prevents a claim that the publication already includes those rows.

## P15-U1 publication-text assessment

The chapter identifies the CHANCE Project version dated 4 July 2006 and gives
its cited sections at lines 12–19. It explicitly selects the finite part of a
discrete treatment and fixes an outcome space separately from random-variable
values. Lines 51–55 distinguish the handbook's mass-function terminology from
the source's distribution-function terminology and distinguish uniform
counting from a general finite probability model. The bibliography key exists
at `handbook/bib/handbook.bib:6583–6594` with the same version identification.

The definition order is usable by the intended graduate audience:

- Lines 24–49 fix finite nonempty outcomes, all events, masses, measure,
  complements, support, null events and almost-sure language before their laws.
- Lines 77–97 define variables as functions, inverse-image events, laws, joint
  and marginal laws, and composition before the grouping theorem.
- Lines 116–135 define positive-event conditioning and its reweighted mass
  function before multiplication, chain rules, Bayes and conditional
  independence. Lines 158–167 supply an explicit nonempty null-event example.
- Lines 169–184 define the hypothesis partition, positive-prior index set,
  likelihood and posterior types before the total-probability and odds claims.
- Lines 217–238 define event, mutual, pairwise, variable and conditional
  independence before the examples using them.
- Lines 343–360 extend to real-valued variables with finite range, define
  expectation and indicators, and declare pointwise arithmetic before the
  expectation identities. Lines 395–415 distinguish a numerical conditional
  mean from a conditional-expectation random variable.

The positive-denominator restrictions cover the uses made of them. In
particular, the chain rule at lines 145–150 requires positivity only for earlier
prefixes; the final intersection can be null. Bayes omits null hypothesis
likelihoods rather than multiplying undefined values by zero. The odds formula
allows a zero numerator while requiring a positive denominator. The
conditional-expectation convention on null fibers is expressly a version
choice, not a definition of null-event conditioning.

The examples support the intended distinctions. The four-point example at
lines 255–274 has three pairwise-independent events with triple probability
1/4 rather than 1/8, and conditioning on equal coordinates destroys the first
two events' independence. In the stipulated inspection example, the four
weights sum to 10,000; `90/585 = 2/13`, the odds are `18/99 = 2/11`, and the
alternative prior produces `2/3`. The explicit three-coordinate conditional
product gives `0.0081/(0.0081 + 0.002475) = 36/47`; copied evidence leaves the
one-alert posterior. These calculations use different expressly specified
models. The indicator example separates linearity from product factorization,
and the final weighted conditional means recover `100/10000`.

All seven annex proofs cover what their corresponding statements promise:
atomic representation and uniqueness; empty fibers and marginals; normalized
conditioning and successive conditioning; null prior blocks and odds;
complement independence and coordinate product construction; finite grouping,
linearity, monotonicity and independent products; and conditional-mean
averaging with almost-sure uniqueness. The final uniqueness argument explicitly
uses singleton value sets and discards only a finite union of null fibers.

Lines 447–461 keep model calculation, population justification, causal claims,
prior selection, laws of large numbers, infinite constructions and general
conditional expectation outside this finite treatment. No empirical or
normative conclusion is smuggled into the stipulated example. This is a
bounded finite-probability unit; the text does not claim completion of N-x-008,
the complete P15 curriculum, or the remaining edition obligations.

## Kamp III.2 Lemma 1 publication-text assessment

The active host supplies the inherited definitions before this unit:
`n-c-012.tex:16–40` defines the order classes; `:42–72` defines the first-order
language and current-point assignment; `:74–131` supplies the strict temporal
semantics and the recursive map `D`. Its input at line 138 supplies the III.1
normal-form definitions and theorem before the new input at line 149. In that
preceding file, the regional classes and the III.1 theorem occur at lines
66–128 and 159–191 respectively.

The target's lines 11–28 define expression at a named current point and
capture-avoiding replacement. Lines 30–103 distinguish the exact binary stages
from their guarded one-variable closures and from the earlier regional classes.
The apparent `x != y` conditions in the displayed class descriptions are
explicitly conditions on variable names, which avoids importing equality into
the source's equality-free object language. The binary base's missing order
guard is explained; the existential closure supplies it.

Lines 105–132 retain repeated predicate occurrences, explain the renamed
sequence symbol, define realizations and make vacuous open intervals explicit.
The lemma's recurrences at lines 134–170 use the already declared strict
argument order. Their construction order is stated. The recurrence seeds are
expressly distinguished from a stage zero in the basic-pattern classes.

The annex supplies word length and free-variable checks, both directions of
the binary-chain equivalence, both guarded closures, and explicit past and
future induction arguments. Its same-word argument at lines 86–98 addresses
unordered endpoint assignments separately, preserving the source grammar.
Its auxiliary one-point semantic seed at lines 131–134 does not silently
extend the syntactic stage classes. Fresh-variable conditions are maintained
in the formulas at lines 142–145 and 170–173.

The two-piece example needs three strictly increasing witnesses, and its
two-point/endpoint consequences follow from the displayed strict semantics.
The prose does not treat an empty open interval as permission to omit a
witness. The target's lines 193–202 and annex lines 203–210 expressly leave
the limiting classes, remaining interval lemmas, all regional expressibility
and III.2 itself to further work. There is no promotion of this finite-pattern
lemma over `Lin` into the full expressive-completeness result over `Com`.

These observations support the publication-text PASS. The descriptions of
Kamp's printed pages, exact grammar and proof method still require the
separate primary-source review.

## All result and annex targets

Each row below occurs once as the matching body result and once as its annex
item in the searched body/annex trees. Every status is `proved=annex:...`, and
every proof item points back to the result in the same row. Each proof is
inside `annexitem`; no target body contains a `proof` environment.

| Body result label | Body line | Annex target | Annex line | Verdict |
| --- | ---: | --- | ---: | --- |
| `thm:p15-finite-probability-laws` | 57 | `annex:p15.finite-laws` | 12 | PASS |
| `thm:p15-finite-law-projection` | 99 | `annex:p15.finite-law-projection` | 58 | PASS |
| `thm:p15-finite-conditioning-laws` | 137 | `annex:p15.finite-conditioning` | 80 | PASS |
| `thm:p15-finite-bayes` | 186 | `annex:p15.finite-bayes` | 121 | PASS |
| `thm:p15-finite-independence-laws` | 240 | `annex:p15.finite-independence` | 151 | PASS |
| `thm:p15-finite-expectation-laws` | 362 | `annex:p15.finite-expectation` | 202 | PASS |
| `thm:p15-finite-total-expectation` | 417 | `annex:p15.finite-total-expectation` | 251 | PASS |
| `thm:p09-kamp-iii2-lemma1` | 134 | `annex:p9.kamp.iii2.lemma1` | 6 | PASS |

## Active routes and bounded shared-style compatibility

The probability body route is `main.tex:35` -> `parts/p15.tex:4` -> the full
finite-probability chapter. The proof route is `main.tex:54` ->
`annex/p15.tex:3` -> its full proof file. The Kamp body route is `main.tex:33`
-> `parts/p09.tex:4` -> `logic-in-computer-science.tex:950` ->
`n-c-012.tex:149` -> the new lemma. The Kamp proof route is `main.tex:52` ->
`annex/p09.tex:7` -> the new lemma proof.

The P15 driver declares `\hbpartidentity{p15}` before its sole public part
heading. The style's map at lines 397–418 assigns stable P15 the approved
ordinal 11 and its approved title. Lines 424–435 set `\hbcurrentpartid` to the
stable ID and record the next observed printed ordinal independently. Given
the ten body parts preceding P15 in the present driver, that ordinal is XI.
The result stream uses the stable owner at lines 472–473. The card stream uses
the same stable owner at lines 1134–1136. No new P15 system-entry card is
present, so this is interface evidence rather than an observed P15 card output.

The annex driver calls `\hbannexchapter{15}{...}`. Style lines 1697–1715 retain
the stable chapter/anchor number P15, while the heading uses the observed
printed ordinal and the mapped title. The two-argument driver interface is
preserved; the title map is authoritative. Lines 1818–1822 retain the separate
annex chapter and item hyperlink identity. The later P11 annex can reset to
its stable number without inheriting P15 as its owner.

The parser at style lines 260–335 accepts the supplied result statuses;
lines 340–347 display their annex links; lines 1610–1620 declare the annex
anchors and back references. These source interfaces are coherent for the
present P15 and P9 files. Their runtime behavior and rendered link appearance
were not exercised here.

`main.tex:23–39` has fifteen body drivers and expressly says P16–P19 await
substantive content. Its present printed ordinals for stable P11–P14 therefore
remain construction ordinals XII–XV; the approved final ordinals are XVI–XIX.
The observed-ordinal interface is consistent with that temporary physical
order. This report does not treat missing parts, remaining reference/lookup
migration, review-part validation, complete part-order validation or F1/F2 as
closed by the bounded style PASS.

## Complete new-notation correspondence

All rows below have precedence `meta`. The first six use scope/first-use
`P9.4`; the last eleven use `P15.1`. Those are stable scope codes. Candidate
table headers explicitly say "Stable part", including P15 at line 1117.
The index registration links resolve textually to the candidate table's
`entry:symbol-registry-00NNN` anchors. These are registration-page links,
as their column headings say; they do not claim to be definition-page links.

| CSV line / entry suffix | Meaning | Body definition/use lines | Candidate table line | Candidate index line | Verdict |
| --- | --- | --- | ---: | ---: | --- |
| 917 / `00917` | Predicate-to-proposition correspondence | Kamp 11–28 | 897 | 904 | PASS |
| 918 / `00918` | Binary basic-pattern exact stages | Kamp 30–77 | 898 | 633 | PASS |
| 919 / `00919` | Guarded one-variable basic patterns | Kamp 79–103 | 899 | 632 | PASS |
| 920 / `00920` | Predicate occurrence word | Kamp 105–116 | 900 | 803 | PASS |
| 921 / `00921` | Word realization | Kamp 118–131 | 901 | 35 | PASS |
| 922 / `00922` | Temporal recurrences | Kamp 138–169 | 902 | 253 | PASS |
| 923 / `00923` | Outcomes and all events | Probability 24–49 | 1130 | 615 | PASS |
| 924 / `00924` | Atom masses, measure and complement | Probability 24–55 | 1131 | 723 | PASS |
| 925 / `00925` | Variable, joint and marginal laws | Probability 77–97 | 1132 | 921 | PASS |
| 926 / `00926` | Inverse-image events and composition | Probability 79–95 | 1133 | 910 | PASS |
| 927 / `00927` | Positive-event conditional probabilities | Probability 116–135 | 1134 | 329 | PASS |
| 928 / `00928` | Hypotheses, evidence, priors and likelihoods | Probability 169–184 | 1135 | 213 | PASS |
| 929 / `00929` | Likelihood ratio and prior odds | Probability 181–182, 203–211 | 1136 | 755 | PASS |
| 930 / `00930` | Stipulated two-alert product model | Probability 311–337 | 1137 | 717 | PASS |
| 931 / `00931` | Finite expectation and indicators | Probability 343–360 | 1138 | 324 | PASS |
| 932 / `00932` | Conditional mean, numerical type | Probability 395–401 | 1139 | 322 | PASS |
| 933 / `00933` | Conditional expectation, variable type | Probability 402–415 | 1140 | 323 | PASS |

The rows preserve repeated letters and strict witnesses for Kamp; positive
conditioning, null-fiber qualifications and distinct mathematical types for
probability; and the stipulated rather than inferred independence of the
two-alert model. The spelling and notes in the isolated table and index agree
with the canonical entries. F2 concerns missing coverage in earlier rows,
not a contradiction within these seventeen rows.

## Read extents and frozen hashes

SHA-256 values identify whole files even where the read extent is bounded.
All four assigned target hashes, the canonical registry hash, both candidate
hashes and the bibliography hash matched the assignment. The contract was
read completely before substantive assessment. Truncated bulk output was
followed by targeted reads for the target's expectation-definition span and
the relied-upon Kamp host span. No unread remainder of a dependency is claimed
as reviewed.

| File | Total lines | Read extent used | SHA-256 |
| --- | ---: | --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | 168 | 1–168, complete | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `handbook/parts/p15/finite-probability.tex` | 461 | 1–461, complete | `BD14BAB29058D7235155D827A8F11793A1D07AF119AD1B34239835EF98805AC0` |
| `handbook/annex/p15/finite-probability.tex` | 284 | 1–284, complete | `D51A43CF5E2CD2DCE15CD558EF3A167AC084347BB471E2A44E657769399EAE58` |
| `handbook/parts/p09/presentations/kamp-iii2-lemma1.tex` | 202 | 1–202, complete | `3372E9B698C044DE21BE64C5F7FF81674A2EA3597B1EC1767A48C9CE89176BF6` |
| `handbook/annex/p09/kamp-iii2-lemma1.tex` | 212 | 1–212, complete | `631B7855D077D3FDDD4C6A7EDFD8A7A934B458F1844ABB5B2ECBFD40C5E0E3B1` |
| `handbook/main.tex` | 67 | 1–67, complete | `E4ED41CD71B429DC5113A1F75B381686C9D03574E20DCE6846426CDCB891B000` |
| `handbook/parts/p15.tex` | 4 | 1–4, complete | `086B941242042DFC0797B625E4707E41FFC71322EBFBAE9231439DAE58E41794` |
| `handbook/annex/p15.tex` | 3 | 1–3, complete | `0C2B7A83557C8F939ECFB69064D7A0731DACC96C79CA3B67F92F51603DEE2FFB` |
| `handbook/parts/p09.tex` | 4 | 1–4, complete | `625DF74E50F822162949AA0B6E2826353FF7A520BD95002A5714AE8885A960BF` |
| `handbook/annex/p09.tex` | 8 | 1–8, complete | `A73A387EA197B03B75ED7D2BF184EA0682957EDC3EC39BED4759E30E0A48010D` |
| `handbook/parts/p09/presentations/n-c-012.tex` | 3064 | 1–169 relied upon; 170–183 also read; remaining bulk output incomplete | `35F9137094A285A4847D351FF868CC206EBF3A6F8F7A75DAC767F0C0AFCE2590` |
| `handbook/parts/p09/presentations/kamp-iii1-normal-form.tex` | 231 | 1–231, complete, as preceding definitions/theorem dependency | `0D1EB5FC960B7F0F1EB216026AF2AAF953CD3D95F62E4ACF014345611D860B31` |
| `handbook/parts/p09/logic-in-computer-science.tex` | 2589 | Chapter/section headings; 942–955; exact input search | `61E3125B950AE194412C81BC6C5EEB3DFCEAC533541B26007F6DB7744E3DDC45` |
| `handbook/handbook.sty` | 1826 | 212–501; 1120–1167; 1600–1645; 1680–1728; 1807–1825; interface searches | `1B5C089594010DD517389CDF510CDFBF741E014EAAC877CC5BB44F3991412288` |
| `handbook/registry/symbols.csv` | 933 / 932 data rows | Header; 79–91; 917–933 complete; searches for ordering roles | `4C8E503AA79DE05E399514211087E8ACA0BDF4D0DDE8961B5AED39609C075CF9` |
| `handbook/bib/handbook.bib` | 6594 | 6576–6594; exact-key search | `A9CFDB177C40F50581B87F8626318FDEFEAA7C5C300D7971A09FFEA2F22C9A53` |
| `tmp/edition-2026-probability-kamp-l1-candidate/symbols-tables.tex` | 1143 | 1–24; 897–902; 1111–1143; all seventeen target entries | `31C7A631B7EE1CCA51F1C1B1B4DAC293EF604BDD81E3FC569B2C95DFB6A0645B` |
| `tmp/edition-2026-probability-kamp-l1-candidate/symbol-index.tex` | 933 | 1–23; 35, 213, 253, 322–324, 329, 615, 632–633, 717, 723, 755, 803, 904, 910, 921 | `AA2377EBB22285E065D55B4614FB51D8EC6D24D836E3ABB36B824FEEC3480921` |
| `handbook/parts/p01/symbol-registry.tex` | 313 | 1–46 and 274–313 relied upon; intervening bulk output not complete | `A95B36D13BA4C61ADEF116BE5E439E43CB21B210130F14BDFE55DA773A21C8DA` |
| `handbook/parts/p14/master-tables.tex` | 312 | 258–282 | `D7AC8DAC67FA6253A0020A27214AE80D5DA5FB36A2E8C7B69A3CC9C79A9BCA17` |
| `handbook/generated/symbols-tables.tex` | 1049 | 1–4; full-file exact search for target entry IDs, no matches | `C6B97C8D431D996110D8881EA6E74DA26278C20C0B5B9460A5948B133A650553` |
| `handbook/generated/symbol-index.tex` | 855 | 1–4; full-file exact search for target entry IDs, no matches | `C4E444976A9310E20A0E732651F760A6B20235CAD84E306D5A5F043DB0F3EDBD` |
| `tools/check.py` | 1740 | 1461–1551; symbol-scope and part-related searches | `5AC607FFB5138FB2202D199209B000EC82D699F4DF7975B68E4C7C84501D3F57` |
| `tools/symbols2tex.py` | 272 | 35–76; scope/header/generation-related searches | `1107FA18828213D26FC7221B3D51A384F27A8CF8C1B136FF6DD15A2076A614D5` |
| `handbook/CONVENTIONS.md` | 251 | 208–232; relevant symbol/edition searches | `4293F514072179A5AC95E64FA8D8F37E23FFE2693814A1980E5801BABA5B7242` |

The historical memory registry was consulted only for the prior review
discipline: frozen source/text evidence does not grant non-text admission.
Current contract and file evidence govern every verdict above. No prior unit's
acceptance was reused as evidence of acceptance here.

## Handoff

Retain the four text PASS verdicts against their exact hashes while correcting
F1 and F2 in the lead integrator's shared-file scope. A registry correction
reopens the affected notation/projection review; a checker correction needs
appropriate shared-tool verification. Any target or content-dependency change
requires the affected independent content review again. Obtain the remaining
independent source/topic evidence, scoped static/build/visual evidence and a
separate admission record before treating these units as admitted. P16–P19,
full N-x-008/III.2 obligations and the full edition migration remain open.
