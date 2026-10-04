# C5 independent adversarial publication-text review

Date: 7 September 2026. Review context: `/root/c5_publication_review`.
Started at 09:37:47 PDT; findings filed within the first fifteen-minute work
block. Observed host: Codex desktop on Windows/PowerShell. The actual runtime
model identifier and version were not exposed to this reviewer; no model
version is asserted. The live checkout was `C:/Dev/the-methods-of-reason`,
branch `phase4-codex`, HEAD `35d537c692bb74b532dc4aa750da381a7fe4daf2`.

This reviewer did not author the frozen units, read another new C5 review,
contact another reviewer before filing, or delegate this assignment. Only
this report was written. No software test, checker execution, build, manuscript
PDF render, registry edit, manuscript edit, or generated-view promotion was
performed. Inspection of checker source below supplies evidence about a
documented naming rule; it is not an executed static-check result.

## Scoped verdicts

| Unit | Verdict | Exact scope and reason |
| --- | --- | --- |
| ACF / S-011 | PASS | Publication text at `handbook/restoration/inherited-07295-07468.tex:177-218`, with the necessary active categoricity/ACF definitions and cited-status route. The result states existence and uniqueness, fixed characteristic, Choice, and the countable exception. Its source-dependent explanation accurately declares its proof boundary. This is not independent source-fidelity or full ACF-theory acceptance. |
| Tseitin / D-P2-007 | FAIL | The complete 188-line body, complete 167-line annex, active routes and candidate notation projection were reviewed. Two editorial example labels violate the binding `hbexample` label taxonomy. Finding C5-PUB-01 must be corrected before this unit can pass publication-text review. |
| C5 candidate symbol projection | PASS | The nine new rows, their declared roles/scopes, candidate table labels and corresponding candidate index links agree at this frozen construction scope. This does not accept or promote active generated symbol views. |

There is one concrete failure. No mathematical counterexample, missing primitive
gate, missing root assertion, incompatible assignment domain, false example,
or unsupported linear bit-time claim was found in the Tseitin text. That
observation does not override C5-PUB-01 or substitute for the topic review.

## C5-PUB-01: editorial examples use an unsupported label prefix

Severity: blocking publication-text/navigation contract defect; bounded repair.

`handbook/parts/p02/tseitin-transformation.tex:149` declares
`\begin{hbexample}{ex:p02-tseitin-worked}{...}` and line 173 declares
`\begin{hbexample}{ex:p02-tseitin-root-boundary}{...}`.
`handbook/annex/p02/tseitin-transformation.tex:105` references the latter label.

`handbook/CONVENTIONS.md:63-67` lists the admitted label prefixes and excludes
`ex:`; its environment contract at line 103 explicitly gives
`\begin{hbexample}{def:<id>}{<Title>}`. The live implementation agrees:
`tools/check.py:181-189` gives `hbexample` the `def:` prefix, and lines 956-965
register a `label-prefix` finding when that environment's label fails its
required prefix. These are newly authored editorial examples outside an
inherited source scope, so the source-capture allowance for historical `ex:`
labels does not apply.

The reference currently names an existing declaration, so this is not a claim
that TeX already produces an undefined reference. It is a concrete mismatch
between the new reader/navigation identifiers and the handbook's binding
editorial-label contract, with a corresponding static-admission consequence.

Correction: use admissible part-owned `def:` identifiers for both example
declarations and update the annex reference consistently, retaining an
explicit disposition of the replaced construction identifiers if required
by the integration records. No weakening of the shared naming rule is needed.
Freeze the resulting body and annex hashes, recheck both declarations and all
their references, and obtain the affected independent review evidence. This
review does not itself authorize an identifier change or grant the later
static/build gate.

## ACF publication findings

The active categoricity definition at lines 4-8 requires model existence as
well as uniqueness. The reviewed theorem supplies both at every uncountable
cardinal. It fixes `p=0` or prime and makes Choice an ambient hypothesis before
using bases and cardinal calculations. The earlier active theorem at
`inherited-07150-07294.tex:137-144` already identifies `ACF_p` as the theory
of algebraically closed fields of characteristic `p` in the ring language.

The explanatory text introduces the prime field, transcendence basis and
absolute transcendence degree at lines 186-191 before invoking those terms
in the classification argument. Basic field-theory terms such as algebraic
independence and algebraic closure are treated as background; this review
does not certify a full field-theory prerequisite treatment elsewhere in the
book. The explanation consistently uses the absolute degree over the prime
field, supplies the existence construction, and gives degree-zero and degree-one
countable witnesses. Positive characteristic includes the finite prime field;
the algebraic closures in the countable examples are still countably infinite.

The result is explicitly `cited=Steinitz1910`, not `proved=...`. Lines 215-218
identify the classification, existence and closure results as cited dependencies
whose full proofs are not reproduced. The prose presents the modern categoricity
claim as an application of field classification and its cardinality calculation.
It does not attribute modern model-theoretic terminology or an independently
written complete proof to Steinitz.

The stable theorem identifier is active through `main.tex:26`, `parts/p03.tex:58`,
and the complete three-line `scope-SRC-07295-07468.tex` wrapper. The formerly
matching `parts/p03/qe-categoricity-games.tex` is not an input of the current P3
driver; a literal input search found no inclusion of that old path. The new
`hbtheorem` does not open an ordinary `theorem` environment: inspection of
`handbook.sty:461-495` confirms its own shared-result counter path. Therefore
it does not increment the P3 driver's ordinary-theorem ordinal hook used for
Ryll-Nardzewski and Morley. This is source-route evidence, not rendered anchor
validation.

The protected DLO slice, lines 108-176, was read and independently hashed as
UTF-8 with LF line endings. It is 3,539 bytes and has SHA256
`9AC556285A7ABB3F42E7652606A28BE92EE3C50102F5F045FB9805A20617A213`, matching
the frozen identity. No DLO correction or fresh DLO proof acceptance is claimed.

## Tseitin publication findings apart from C5-PUB-01

The active P2 order supplies the primitive grammar, total valuations,
coincidence lemma, occurrence definitions, and clause/CNF conventions before
the new section. The section itself explicitly introduces finite valuation
domains and explains their relation to total valuations. Its fresh labels are
ordinary indexed propositional variables, not a new alphabet, and the
occurrence policy separates equal subformula strings at different positions.

The table covers variables, bottom, negation, conjunction, disjunction and
implication. It defines child representatives before the clauses use them,
allows coincident binary inputs, reuses original variable leaves and labels
bottom occurrences. The root assertion includes atomic inputs. Clause-set
equality, duplicate list emissions, literal sorting and right association have
separate explicit roles, so the set and the exact formula-string output are
not silently identified.

The extension theorem fixes the input assignment on exactly `V`, asserts
uniqueness on exactly `V union Z_phi`, and leaves global outside assignments
unrestricted. It distinguishes metatheoretic existence from a CPL quantifier.
The annex proves both directions of every gate, existence, bottom-up forced
values, uniqueness, atomic and variable-free boundaries, root satisfaction,
the list/set/formula bridge and the total-valuation entailment. The enlarged
vocabulary countervaluation supports the stated failure of converse entailment.

The size theorem states structural counts separately from its encoding model.
Its conditional linear emission claim requires a parsed tree and supplied fresh
names under unit-cost references/comparisons. The bit bound accounts for original
names and fresh indices, proves indices below `N` are available, and states
polynomial effectiveness without claiming linear bit-time. The size measure
includes repeated occurrences and the expansion of defined connectives.

The worked conjunction/negation/implication example emits eight gate clauses
and one root clause. Both displayed assignments agree with the input's truth
value and the corresponding forced auxiliary values. The bottom example loses
equisatisfiability when its root is removed. The negated-atom example makes the
input true and the output false on the stated enlarged assignment.

The CNF section reaches the new section and theorem at
`inherited-01946-02186.tex:210-212`. `parts/p02.tex:10` includes the body once;
`annex/p02.tex:13` includes its annex once. Both proved-status destinations
match their annex back-references at annex lines 2 and 110. The annex scope
paragraph includes Tseitin. The Part 12 reference uses the stable `part:p12`
label, and the existing source section at `inherited-14351-14400.tex` contains
the stated conjunction shape and root qualification. The old P2
`propositional-syntax-semantics` path is not an input of the current driver;
a literal input search found no inclusion of it.

## Candidate notation: construction evidence and canonical roles

The complete candidate README was read. Its stated registry hash and both
projection hashes match the files inspected. Registry lines 862-870 have nine
rows; the row identifiers are physical CSV line identities, explaining why
869 data rows end with anchor `00870`.

| CSV row / candidate anchor suffix | Role checked | Candidate table line | Candidate index line |
| --- | --- | ---: | ---: |
| 862 / 00862 | `W,V`: finite valuation domain and exact input-variable set | 205 | 842 |
| 863 / 00863 | `G_phi`: nonvariable occurrence positions | 206 | 176 |
| 864 / 00864 | `z_a,Z_phi`: fresh indexed variable aliases and auxiliary set | 207 | 868 |
| 865 / 00865 | `r_a`: variable representative of an occurrence | 208 | 714 |
| 866 / 00866 | `D_phi` in calligraphic type: unrooted gate clauses | 209 | 346 |
| 867 / 00867 | `S_phi`: rooted clause set | 210 | 736 |
| 868 / 00868 | `C_1,...,C_m`: ordered emission list retaining repeated clauses | 211 | 93 |
| 869 / 00869 | `T_phi`: CNF formula determined by chosen labels and emission conventions | 212 | 770 |
| 870 / 00870 | `N,M,L;n_0,n_1,n_2`: tree, encoding and primitive-node counts | 213 | 559 |

Each index row names the matching `entry:symbol-registry-...` declaration
present in the candidate table. The new rows have P2.1 scope and metalinguistic
standing; none introduces a new CPL primitive. In particular, calligraphic
`D_phi` denotes the gate clause set, whereas the earlier ordinary `D_phi`
denotes a DNF formula; their glyphs and types remain distinct. The candidate
description of `T_phi` as deterministic is understood after the fresh-variable
choice, as in the body's explicit optional deterministic naming policy.

The candidate index links to the registry table; its page references and the
table's `thepage` fields have not been compiled or visually checked. Textual
`sec:`/`def:` locators in notes are identifiers rather than claimed compiled
hyperlinks to definitions. This bounded finding accepts the nine role mappings
and candidate anchor pairing, not completeness of the entire 869-row registry
or a full subject/task lookup surface.

The canonical CSV supplies the candidate input. The candidate files remain
isolated, pre-admission construction projections. Promotion of active generated
views is an explicit later gate after the applicable content admission path;
requiring that promotion to exist before this review would create the circular
dependency the approved plan excludes.

## Primary-source and attribution observations

The live [Harrison author PDF](https://www.cl.cam.ac.uk/~jrh13/slides/marktoberdorf-30jul03/slides1.pdf)
was read as extracted source text. The title page identifies John Harrison,
the propositional-logic lecture and 30 July 2003. Printed slide 12 (physical
page 13) displays biconditional subformula definitions and an asserted output,
followed by CNF clauses; neighboring slides 11 and 13 establish its normal-form
and clause-set context. This supports the bounded introductory attribution.
It does not establish that Harrison supplied this occurrence policy or annex
proof, and the manuscript makes no such assertion. The PDF skill was used for
this source inspection; no manuscript PDF was rendered or accepted. A source
screenshot call returned a reference, but this reviewer claims no completed
visual source-PDF inspection.

The [Steinitz printed-page-299 primary OCR](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0137/00000303?_format=xml)
was read completely, including the cardinal invariance and transcendence-degree
definition. The [printed-page-301 primary OCR](https://gdz.sub.uni-goettingen.de/fulltext/PPN243919689_0137/00000305?_format=xml)
was read completely, including the unique algebraically closed type within a
characteristic/degree class and the uncountable-cardinality calculation under
well-ordering. These passages directly support the publication text's described
source dependence and explicit Choice hypothesis.

Attempts to retrieve the cited printed pages 287, 289 and 300 did not produce
readable bodies in this review: the web tool refused those endpoints and the
shell requests ultimately failed authentication after network permission was
granted. Their claimed source contents were read only in the author note and
are not promoted here to independently verified source-body evidence. The
independent source-fidelity reviewer must resolve the exact locator coverage.
This access limit is outside the ACF publication-text PASS and prevents treating
this report as a full source-fidelity PASS.

The canonical bibliography records actually read are
`handbook/bib/handbook.bib:4000-4011` for Steinitz1910 and `5354-5361` for
Harrison2003PropositionalSlides. The cited keys and the stated identities are
present. The Steinitz bibliography's resolver URL was not accepted as a
verified-working current access route by this review.

## Exact frozen identities

All SHA256 identities below were computed from the actual local files and
matched the integration freeze.

| File | SHA256 |
| --- | --- |
| `handbook/parts/p02/tseitin-transformation.tex` | `9E09805F966C64DF13CFDC0471C40AE0E0DCC9B2DC187B68E915E5E5A334E0D5` |
| `handbook/annex/p02/tseitin-transformation.tex` | `975195E565E2AE77F128EDA22568BF728555380F03E360006D4A5D67C4D19561` |
| `handbook/restoration/inherited-01946-02186.tex` | `185C35156F2E1983B1BEF028888C3FF2A0DFFF333366CFF1A3D2769225E37468` |
| `handbook/restoration/inherited-07295-07468.tex` | `A133AD43A7AF91BEC6DC90B1AC5335F0524C1447869CB382B05175138A9C0505` |
| `handbook/parts/p02.tex` | `77811CDF11B5E6E2FBB3B56A45B229D973BA39815926DE29D49823D3F2FA7854` |
| `handbook/annex/p02.tex` | `CB924992058BF0846B4D83CB35E24165A2DB7BDC8B0BA1A974FC770F0ACF13D6` |
| `handbook/bib/handbook.bib` | `84FF6BDD200A86DB3D82B84B0405376C98F395C7E504DA6CC38F52EFF340B7CC` |
| `handbook/registry/symbols.csv` | `2B0A9C3C4740EC6CD28FDBEEC437329C8049991CDC0855B9F3AF07955D50F781` |
| `tmp/edition-2026-c5-candidate/symbols-tables.tex` | `76899033C8772705AB7592702208313CBD3DCB4A227D702D4B6AA8A88120253B` |
| `tmp/edition-2026-c5-candidate/symbol-index.tex` | `8C53E4771A7E9951098F5210C7B76E313523A197AB2F2C9EF722248D47E81073` |

Additional dependency identities observed:

| File | SHA256 |
| --- | --- |
| `handbook/parts/p02/propositional-substitution.tex` | `5B39B8DC52B60442850707C6D4DF2C7E853929FC52541F85D839986BFD8DC146` |
| `handbook/restoration/inherited-01661-01816.tex` | `FB12D36A183AC0FDF5C8B2F8A1BBC09238526FDB03F75364A6DC18239913EC3E` |
| `handbook/restoration/inherited-01817-01898.tex` | `499FEC700936D0625769D7C09AA2BC5FD1F6D976B9EAB1A9CBC8EDFE8CAFB9C4` |
| `handbook/parts/p03.tex` | `3694A5CDE0762B4CF489AA640AECA2F00B9216BF16FE4BFA2A43E0FD4583BA69` |
| `handbook/restoration/inherited-07150-07294.tex` | `CCB19227218A479328D04079082C149BBD9ACF4B587C45D13FFF49A07548EFF8` |
| `handbook/handbook.sty` | `1B5C089594010DD517389CDF510CDFBF741E014EAAC877CC5BB44F3991412288` |
| `handbook/CONVENTIONS.md` | `4293F514072179A5AC95E64FA8D8F37E23FFE2693814A1980E5801BABA5B7242` |
| `tmp/edition-2026-c5-candidate/README.md` | `340F8F58AE7188766688329C814FC9896C7BE30D629C413C21BD434DD1D36234` |

## Read intervals and limits

Complete reads: edition contract 1-168; C5 integration note 1-78; ACF author
note 1-85; Tseitin author note 1-148; handbook conventions 1-251; Tseitin body
1-188; Tseitin annex 1-167; ACF-containing restoration file 1-250; primitive
grammar 1-156; valuation file 1-82; CNF file 1-244 across successive reads;
substitution body 1-181; P2 body driver 1-67; P2 annex driver 1-18; P3 driver
1-68; candidate README 1-17; the three-line source wrappers for the grammar,
valuation, CNF and categoricity files; and the complete 50-line Part 12
equivalence/equisatisfiability source file.

Focused reads: ACF prerequisite theorem 130-145 in
`inherited-07150-07294.tex`; the two bibliography records above; symbol CSV
849-870 with findings restricted to 862-870; candidate table 176-219 with
findings restricted to 205-213; the nine complete candidate index rows listed
above; style 338-358, 457-496 and 1610-1622; checker 180-193 and 950-970;
main-driver body/annex/bibliography input lines; and SAT chapter 1-30.
Targeted literal searches checked the known inactive duplicate paths and
active label references. These searches do not constitute a whole-book label
or notation audit.

## Integration boundaries and next disposition

Correct C5-PUB-01 and freeze the affected Tseitin body and annex. The existing
ACF text result and candidate role mappings need not be treated as failed by
that identifier repair, although changed shared dependencies must be assessed.
The three independent review dimensions remain separately required; this
report gives no majority-vote or author-self-acceptance shortcut.

Correction-provenance migration and its independent terminal support remain
open. Existing v1 records do not describe these corrected active files.
Candidate generation, successful body/annex input tracing, and this scoped
publication review do not close those obligations. Required static, build,
rendered-page, visual, formal-admission, whole-book integration and final user
acceptance gates remain separate and unclaimed. Active generated lookup
promotion follows the applicable admission stage and must preserve the accepted
content and canonical symbol roles.

Historical memory was used only for the earlier handbook review discipline:
frozen-text acceptance must remain distinct from build, visual and formal
admission. No historical verdict supplied current C5 evidence.
