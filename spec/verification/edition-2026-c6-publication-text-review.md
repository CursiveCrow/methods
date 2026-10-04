# C6 / R-002: independent publication-text review

Date: 7 September 2026. Reviewer context: `/root/c6_publication_review`.
Repository: `C:/Dev/the-methods-of-reason`; observed HEAD:
`35d537c692bb74b532dc4aa750da381a7fe4daf2`. This assessment concerns the live
frozen inputs identified below, including uncommitted text. The runtime did
not expose an independently verifiable model identifier or version to this
reviewer; no particular model/version is certified here.

## Decision

**Overall publication text/candidate verdict: FAIL, with one bounded correction
required in the new notation row.** The two manuscript targets pass this
publication-text review. The C6 notation meanings and candidate anchors pass;
one new registry note emits an unescaped underscore into both candidate LaTeX
surfaces. Those candidate texts require correction before acceptance.

The construction gets the central publication problem right: it gives the
reader the actual serialization, formula abbreviations, and proofs for this
numbering. It states the raw-program and canonical-output conventions before
using them, and its standard-model result has an explicit boundary against the
later internal arithmetic claims. These features make the argument independently
traceable at the supplied text level.

| Component | Verdict at the reviewed scope | Reason |
| --- | --- | --- |
| Frozen target identity | PASS | Both manuscript and all three canonical/candidate notation hashes match the freeze. |
| Manuscript definition, statement, proof and example interfaces | PASS | The complete files were read; each new named helper is defined before its mathematical use, and its conditions are carried into its consumers. |
| Bespoke-numbering attribution and source boundary in the text | PASS | The numbering and literal formulas identify their local authorship; external readings are not presented as owners of these exact codes. |
| Mathematical interfaces challenged for publication | PASS | No false implication or missing local interface was found in the supplied serialization, extraction, H1–H4, Comp and P4 c.e./Delta-1 chain. This is the publication reviewer's assessment, not the separate specialist's verdict. |
| Canonical C6 notation meanings, scopes and argument descriptions | PASS | Existing row 259 and all 17 new rows 871–887 agree with their declared local roles. |
| Candidate table/index semantic projection and anchor correspondence | PASS | All 18 affected rows preserve their glyph, role, scope, first-use description and notes, and every affected index target has its matching table anchor. |
| Candidate LaTeX text | FAIL | Finding C6-PUB-01: raw `code_5` occurs in a prose note in both outputs. |
| Primary-source body fidelity, rights and source acquisition | UNRESOLVED | No external paper/book body was read in this publication-review assignment. The text's attribution boundary is assessed; external fidelity is a separate review. |
| Static/build/render/visual quality, correction provenance, admission, active-view promotion and release | UNRESOLVED | These later gates were not executed or granted by this text review. |

## C6-PUB-01: escape the tuple-code notation in the new registry note

Severity: High for candidate publication; blocking the candidate-text pass.
Framework: inversion and failure-case inspection.

What I see: `handbook/registry/symbols.csv:873` describes the serialized row
with the prose fragment `The right-nested code_5 of source state`. Its `notes`
field contains the underscore outside any math or verbatim delimiter. The
same fragment appears in
`tmp/edition-2026-c6-candidate/symbols-tables.tex:359` and
`tmp/edition-2026-c6-candidate/symbol-index.tex:739`.

Why it matters: these are LaTeX-valued prose cells. The generator explicitly
says the registry escapes its own special characters
(`tools/symbols2tex.py:10–12`), passes `notes` through unchanged in the table
(`213–217`), and passes it through unchanged in the index (`237–242`). Only
the separate macro column is protected by `detokenize`. The shown handbook
package dependencies and main preamble provide no text-underscore handling.
Consequently this character is a mathematical subscript token in prose, making
the supplied candidate invalid for the intended LaTeX use. This conclusion
comes from the actual source tokens; no compiler failure or rendered defect
is claimed to have been observed.

Required correction: in canonical row 873, use the actual mathematical name
`\(\operatorname{code}_5\)` in the note, or an explicitly escaped text spelling
if that is the editorial choice. Regenerate the two isolated candidate
projections, verify this row's glyph/meaning/anchor in both, and record their
new hashes. Preserve the existing row identity. The manuscript proof does
not need to change for this finding. Candidate correction and review may take
place before admission; promotion to the active views remains a later gate.

## Complete interface audit

The following locators in this section refer to
`handbook/restoration/inherited-08710-08876.tex`, unless another file is named.

### Program identity and prior definitions

The complete numbering file `inherited-07851-08048.tex:1–261` uses the
machine tuple and step relation already supplied at
`inherited-07506-07677.tex:4–79`. Its alphabet and state slots, direction codes,
metadata, number of rows, lexicographic row keys, five-field row order,
description length and outer pairing are all fixed at `07851–08048:7–63`.
Its right-nested tuple convention is exactly the one at
`07506–07677:81–109`, including the identity code at arity one and zero at
arity zero. The preceding pairing bijection and effective inverse are supplied
at `01101–01147:25–46` and `07506–07677:139–147`.

The decoder at `07851–08048:65–80` checks exact length and metadata, terminal
identity tail, bitmap width, each row's field ranges and its actual ordered
key. The lower bound of six description entries follows from the specified
minimum state and alphabet counts. It does not silently accept omitted,
additional, unordered, or halting-source rows. Invalid indices denote the
everywhere-undefined function; rejection and malformed accepting output also
leave the indexed value undefined (`82–101`). The wrapper is described as a
machine computing that partial function; it does not replace the raw machine
whose trace Comp later checks.

The enumeration proof preserves this identity. Its normalization handles a
halting start state by a fresh start and one tape-preserving move
(`181–189`), which respects the prior output convention's independence from
final head position. It serializes the actual normalized metadata and full
table (`191–209`). The `code_k` input convention is not applied twice
(`104–109`). Kleene is identified as parallel reading for this bespoke
numbering (`212–216`). Universal computation remains a proof sketch
(`218–238`); the parameter theorem remains a cited theorem with the omitted
compiler verification stated (`240–261`). Those statuses are not upgraded by
the C6 text.

### Formula and argument inventory

The arithmetic language, numerals, marked strict/non-strict bounds,
freshness condition and syntactic/semantic hierarchy distinction occur earlier
in the active order at `inherited-08306-08438.tex:4–124`. The actual P graph,
B formula, extraction uniqueness, value bound and finite packing proof occur
at `inherited-08439-08709.tex:1–87`.

| New abbreviation and argument order | Definition | Interface checked |
| --- | --- | --- |
| `E(s,t,j,v)`; `E2(s,t,a,b,v)` | 1–26 | Tag first, then one position or the ordered pair of positions; fresh expansion of both levels and B. |
| `Lt(u,v)`; `Le(u,v)`; `Bit(d)` | 160–180 | Marked comparison witnesses; the zero upper-bound cases have the correct meanings. |
| `I(x,s,L)`; `J(s,lambda)`; `H1(x,s)` | 182–214 | Input bit and prefix ranges, last-position witness, canonical zero and positive leading bit. |
| `P5(q,a,q',a',d,rho)`; `R5(s,i,q,a,q',a',d)` | 216–240 | Four pairing equations, three internal tails, identity final component, description position `3+i`; R5 alone makes no table-membership claim. |
| `D(s,lambda)`; `M(s,b,A)`; `K(s,n,b,nu)`; `H2(e,s)` | 242–321 | Complete decoding chain, bitmap tails and terminal zero, every ordered nonhalting key, exact header/outer code. |
| `Cfg(s,t,n,b,W,mu)` | 533–559 | State/head/symbol ranges, first and successive tape prefixes, final fixed-width code. |
| `Init(s,L,H,W)` | 560–573 | Correct normalized bit-to-symbol conversion by successor and blanks in every other window cell. |
| `Step(s,t,m,W)` | 574–600 | Actual row index `i<m`, source/target/read/write alignment, both head moves, overwritten cell and every unchanged cell. |
| `H3(s)` | 601–618 | Unique common header; `H=T`, `W=L+2T+1`, `W=S mu`, row count from `k=3+m`; all times and transitions. |
| `OutCells(s,T,H,ell,y)`; `OutNext(s,lambda)`; `H4(s)` | 620–664 | Canonical output prefix, every bit and recurrence, output value, first following blank, accepting state, independent final head. |
| `Comp(e,x,s)` | 665–676 | Exactly H1(x,s), H2(e,s), H3(s), H4(s), expanded with fresh bound variables. |

The fourteen family tags and their fixed arities are explicit at `76–158`.
The three different last-position uses of lambda are separate local bindings;
mu is the last tape column and nu the number of nonhalting states. Numerical
bracket access remains in the metatheory. The formulas use relational
extraction instead of introducing array access, subtraction, division,
exponentiation or a tuple constructor into the arithmetic language.

### Statements, proofs and boundary cases

The E/E2 extraction proof at `28–74` supplies the polynomial term bound on
each pairing index, including zero, and distinguishes those indices from
stored values bounded by s. Fixed positional arity prevents address collisions.
Its finite-packing construction determines all indices before choosing s;
empty assignments are included. The earlier beta proof's Chinese remainder
theorem dependency remains explicit at `08439–08709:71–82`.

The input lemma and proof (`323–377`) show both directions for precisely the
input families, including the single zero digit, a positive first bit of one,
one-digit inputs and the empty successor range. Binary quotient/remainder
uniqueness establishes the actual word and length. The table lemma and proof
(`379–498`) supply every metadata and row condition, explain the final identity
tail, bound internal row projections by the stored row code, and show that
Euclidean division enumerates every row exactly once. The minimal `n=b=3`
case is included. The simultaneous-packing lemma (`500–531`) requires
agreement at overlapping positions; it makes no claim that input/table
certificates imply an accepting run.

The configuration/output lemma (`678–803`) explicitly assumes H1 and H2.
It proves a full-tape converse by extending the represented window with blanks
and checks the original transition relation on the scanned cell, all other
window cells and all outside cells. Both heads remain in range. The final
check identifies the first nonnegative blank and a canonical binary output;
negative cells, later scratch cells and final head position impose no extra
output restriction.

The Comp theorem and proof (`805–907`) give both the code/history equivalence
and the existential convergence equivalence. The actual-run direction proves
the head bound, chooses the fixed window `[-T,L+T]`, establishes an untouched
rightmost blank, bounds the output end, and packs the complete finite
assignment before invoking the formula lemmas. The stored datum, row
projection, derived-length and paired-index bounds are separately justified.
The zero-transition range is meaningful for H3 but cannot satisfy H4 because
the normalized start and accepting states differ. Invalid programs, rejecting
halts, empty output, nonbinary output and noncanonical binary output cannot
produce a successful Comp certificate.

The worked example at `917–956` supplies the exact three-row machine and
six-entry description expression, complete header, input and output bits and
prefixes, bitmap tails, both tapes, tape prefixes/codes, state/head sequences,
the actual selected row and first-blank position. Each number agrees with the
displayed recurrences and location conventions. The unique decoder and packing
lemma determine the remaining large codes; printing their enormous decimal
expansions is not required to make this example definite. The leading-zero
input and blank-bit bitmap examples genuinely fail the named conjuncts.

### c.e. proof, attribution and P5 limits

The forward c.e. direction (`966–980`) uses the domain definition at
`inherited-07753-07843.tex:9–12`, the exact enumeration theorem, and Comp.
It does not invoke the four-way c.e. equivalence sketch at `07753–07843:56–76`
or the conclusion it is proving. The converse (`982–1033`) gives a terminating
bounded-formula evaluator for the actual syntax, including bottom and empty
quantifier ranges, explains its finite tape-block implementation and valid
truth-value output, and then searches finite boxes of witness tuples. The
prefix-form dependency was read in full at `08439–08709:153–270`. The resulting
machine returns zero on a witness and runs forever otherwise, including for
the empty set. The decidable/Delta-1 argument (`1035–1044`) uses negation of
defining formulas and the earlier supplied complement characterization at
`07753–07843:78–90`.

The local authorship/source boundary at `909–915` is accurate as a statement
of what the manuscript proves. Shoenfield and Boolos–Burgess–Jeffrey are
pointed to for other standard constructions. Neither their general results
nor the generic T-predicate substitutes for the literal formulas here.
Hierarchy completeness and strictness (`1047–1104`) retain their cited status
and are outside this acceptance scope.

The later actual P5 text distinguishes numeralwise representation in Q
(`inherited-09262-09327.tex:4–48`), the selected syntax/proof numbering and
arithmetization sketch (`inherited-09328-09438.tex:4–84`), and internal
derivability conditions (`inherited-09750-09816.tex:7–47`). C6 claims a truth
equivalence in N. It supplies none of those additional Q/PA proof obligations,
and its proof does not use them circularly. The shared beta machinery does not
identify the program, history and syntax/proof codes as the same numbering.

## Routing and candidate anchor evidence

The active source route is `handbook/main.tex:27` to `parts/p04.tex`, then
`parts/p04.tex:36` and `65` to the respective three-line restoration wrappers,
whose line 2 reaches each frozen file. Arithmetic language and P/B/prefix
prerequisites precede the history target at `parts/p04.tex:54–55`.

The history file has exactly four ordinary theorem openings in this order:
bounded verification at 805; c.e./Sigma-1 at 958; hierarchy classifications at
1059; hierarchy strictness at 1080. The counter is reset at
`parts/p04.tex:56`, and its theorem hook attaches the classification and
strictness labels at counts three and four (`57–64`). The hook is removed at
66. The new definitions and lemmas do not increment that ordinary-theorem
hook. The source environment definitions at `handbook.sty:655–673` preserve
that distinction. This is a source-route check, not a compiled-link claim.

Canonical physical CSV row 259 projects to candidate table line 293 and index
line 427, with anchor `entry:symbol-registry-00259`. The 17 new rows 871–887
project in order to table lines 357–373, with anchors
`entry:symbol-registry-00871` through `entry:symbol-registry-00887`. Their index
lines, in canonical row order, are:

`570, 43, 739, 822, 440, 750, 476, 457, 496, 464, 434, 422, 491, 247, 721, 115, 256`.

Each index reference matches its table anchor and its canonical row contents.
The meaning of row 873 is correct; its unescaped prose spelling causes the
separate candidate-text failure above. C5 rows 862–870 were read only as
adjacent preserved-row context, not reviewed or reaccepted here.

The candidate README accurately names these files as isolated pre-admission
outputs, states the canonical input hash and count, and leaves semantic and
layout review open. Active routes still name `generated/symbols-tables`
(`parts/p01/symbol-registry.tex:46`) and `generated/symbol-index`
(`parts/p14/master-tables.tex:275`). This review does not require promotion
before candidate assessment; it does not grant promotion or attest the current
contents of those active generated files.

## Exact input identities and actual read intervals

All intervals are inclusive physical file lines. SHA256 values identify entire
files, even where only a stated interval was read. No other C6 independent
review was read, and no findings were exchanged before filing this report.

| Artifact | Actual reading | SHA256 |
| --- | --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | Complete 1–168 | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `spec/research/edition-2026-c6-review-freeze.md` | Complete 1–85 | `04E1075E9EF200726F36C781C463380F7701B82C7C5FB8FB1DFE1E7F656D4732` |
| `handbook/restoration/inherited-07851-08048.tex` | Complete 1–261 | `DE01687B7F524F49D6B3E90C9ACD038550F7BE1551A1AABC771B8BBB3B4B0177` |
| `handbook/restoration/inherited-08710-08876.tex` | Complete 1–1104, in consecutive 1–290, 291–590, 591–900 and 901–1104 reads | `4D131A6631A148354F31066316E3B73977DF71AF66C06FC98158D6C402DBC102` |
| `handbook/registry/symbols.csv` | Header, row 259, rows 862–887; targeted collision/role searches also returned existing context rows | `54F108553D5B719EB06BC3B85808656D4AF5BF56397ADF4643EB10C57D8B0D79` |
| `tmp/edition-2026-c6-candidate/symbols-tables.tex` | 1–20, 254–260, 293, 348–381; other search-returned existing rows were context only | `79E2C62BAF9D5E566AFA251ABF6A2F3E4BAE2F83C1481F1BCF25821D28328712` |
| `tmp/edition-2026-c6-candidate/symbol-index.tex` | 1–12 and the 18 exact affected lines listed above; other search-returned existing rows were context only | `03231E48997471D9EF625A7584CB54AD85ED7F5F822338125BF39AA78B0CBCD5` |
| `tmp/edition-2026-c6-candidate/README.md` | Complete 1–17 | `8E43AACC3F8C685C778BA71492265451A308DB1DA4D88AFFB6636FBAAB59B230` |
| `handbook/restoration/inherited-01101-01147.tex` | Complete 1–47 | `A5683457BDF59EA170FA60151B8ADD87790A4E3BA0A5D4739753B9B676C65663` |
| `handbook/restoration/inherited-07506-07677.tex` | Complete 1–172 | `EB27FE6DE9A8FFBBE3EC6F317DFF66D97DDE72F22B1FA3FCB48A4304D85F3C7D` |
| `handbook/restoration/inherited-07678-07752.tex` | Complete 1–75 | `1B3A7277D05F42CD5E568CC12B851F2E460BDBAB4244D11F91F30EFF78AA02DD` |
| `handbook/restoration/inherited-07753-07843.tex` | Complete 1–91 | `E2B7284BEABCA82F440BB921D779243F1615F8D7077ABA73DFF6CBDE28458B00` |
| `handbook/restoration/inherited-08306-08438.tex` | Complete 1–133 | `0B020970BE72999CD771566BA0D6CDB4E4668728362CBD3C0D1606059EE9D2B8` |
| `handbook/restoration/inherited-08439-08709.tex` | Complete 1–271 | `95EB4270559303FEFC5DE2D9BC804A04768EAD87D68D9E5D9CBF65079714806A` |
| `handbook/restoration/inherited-08877-08897.tex` | Complete 1–21 | `AA6B105B9031A8D67D75B67D3C7F228C448FAFA1764882536D62CB784762017C` |
| `handbook/restoration/inherited-09262-09327.tex` | Complete 1–66 | `75A27E87080116A235A904DAEDABE2A70DFF472BA27CA8A454C448DFD4B58BB6` |
| `handbook/restoration/inherited-09328-09438.tex` | Complete 1–111 | `F5A14F098311611F5942A7E0F9F5B348B52C1AADFCA2E1FF129E5F63A977F6A0` |
| `handbook/restoration/inherited-09750-09816.tex` | Complete 1–67 | `EFA16565DC4206D722BA62585AA452A86394B5827C84B6201C6340815062D2DE` |
| `handbook/main.tex` | Complete 1–65 | `511E6B538B89E6BF9541AC7DC564EBBAA7499D5991E18327C313453087C24761` |
| `handbook/parts/p04.tex` | Complete 1–84 | `19C6CB01DE3F19F24430EDBFE623F466C55DDEA50AF006864B6B1B8EC964A509` |
| `handbook/restoration/scope-SRC-07851-08048.tex` | Complete 1–3 | `7FD00B6A8140B749C94538B9055F2E6F4CDB82FCFB4647AA863AB8DEB38AA61B` |
| `handbook/restoration/scope-SRC-08710-08876.tex` | Complete 1–3 | `874744040E6B3C1A1FEE5C71ECA68548315678D9FDAC856A561FDAA813C91462` |
| `handbook/parts/p01/symbol-registry.tex` | Complete 1–313 | `A95B36D13BA4C61ADEF116BE5E439E43CB21B210130F14BDFE55DA773A21C8DA` |
| `handbook/parts/p14/master-tables.tex` | 257–280 | `D7AC8DAC67FA6253A0020A27214AE80D5DA5FB36A2E8C7B69A3CC9C79A9BCA17` |
| `handbook/handbook.sty` | 1–150, 650–687, 1380–1435; targeted searches for theorem routing, packages and catcodes | `1B5C089594010DD517389CDF510CDFBF741E014EAAC877CC5BB44F3991412288` |
| `tools/symbols2tex.py` | 1–17, 185–269; read only for candidate emission | `1107FA18828213D26FC7221B3D51A384F27A8CF8C1B136FF6DD15A2076A614D5` |
| `spec/research/edition-2026-c6-arithmetic-preparation.md` | Complete 1–198; historical author/preparation context only | `4AFF64BB834FCEB5425AF53F08D811EE41C6EFA59C63931F42798C884BE5DA42` |
| `spec/research/edition-2026-c6-protocol-and-extraction.md` | Complete 1–77; author context only | `0662246175206E086C052CD7353151923CCCC7D26AF9E841D91F885A22B58964` |
| `spec/research/edition-2026-c6-input-table-formulas.md` | Complete 1–93; author context only | `8D236534FE3A88A11C3A2985B159D34D7A4E37DAD041DC9DB147E54B34E2DA29` |
| `spec/research/edition-2026-c6-computation-verification.md` | Complete 1–104; author context only | `950B7FD7B5F1300C84FA294773D62E0854D0048BC027A710642768D1E12AA3F9` |

## Later gates and review method

The required local repair is confined to the canonical notation note and its
isolated outputs. It should receive an affected-scope review at new hashes.
Unchanged manuscript content retains the evidence recorded here, subject to
the independent source and specialist reviews and any errors they find.

Source acquisition/fidelity, independent mathematical acceptance, correction
provenance and restoration preservation, scoped static/build/visual evidence,
the separate admission record, active notation projection, and final integrated
publication remain their own gates under the edition contract. P5 internal
representation and proof transformations, the separate universal-machine and
parameter/compiler arguments, and later hierarchy completeness/strictness are
not closed by this report.

The Devil's Advocate skill supplied the steel-man, inversion and failure-case
method used here. Prior handbook memory was used only for review discipline;
all factual manuscript, dependency, notation and routing claims above were
checked against current local inputs. No manuscript, source, registry,
provenance or tooling file was changed; this assigned report is the sole write.
No tests, generator execution, build, manuscript render, source acquisition or
delegation was performed. No compiled pagination, PDF appearance, runtime
model version or user acceptance is inferred from source inspection.

Verdict: ship with the specified candidate-text correction at this review scope;
overall publication text/candidate status remains FAIL until that correction
is reviewed. This wording grants neither admission nor release.
