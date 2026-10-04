# P5 syntax arithmetization and Kamp III.1: independent source review

Date: 7 September 2026. Reviewer: `/root/p5_kamp_source_review`.
Assignment: source fidelity, compatibility with the actual governing handbook
definitions, and preservation of source and internal-proof boundaries.

## Verdicts

| Frozen unit | Verdict | Scope |
| --- | --- | --- |
| P5 `handbook/restoration/inherited-09328-09438.tex` | PASS | The complete supplied numbering and checker construction agrees with the actual arithmetic syntax, ND rules, finite/c.e. axiom conventions, and accepted P4 computation interface. Its Q representability and internal derivability boundaries remain explicit. |
| C7 reader `handbook/parts/p09/presentations/kamp-iii1-normal-form.tex` and complete annex `handbook/annex/p09/kamp-iii1-normal-form.tex` | PASS | The supplied result realizes Kamp's III.1 normal form and sentence corollary over Lin, with justified, documented corrections and an explicit conversion from the separate starred grammar to the source grammar. |

No source-compatibility failure or unresolved source finding was identified in
these assigned units. These are independent source-review verdicts. They do
not record topic or publication approval, a build, manuscript page inspection,
formal source/register admission, completion of P5 or N-c-012, or release.
The new topic/publication reports were not read, and findings were not
exchanged before this report was filed.

## Actual reading and frozen identities

All paths below are relative to `C:/Dev/the-methods-of-reason`. The read extent
is the actual newly inspected extent, not an extent inferred from an author
note or from a whole-file hash. SHA256 values were computed in this review.

| File | Actual read extent | SHA256 |
| --- | --- | --- |
| `spec/EDITION-2026-CONTRACT.md` | 1-168, complete | `C9B101AD6BF6BFEA5A3E1FBEC25CDBA81B47667146474861EB1AA00B5DFA1BF3` |
| `spec/research/edition-2026-p5-syntax-arithmetization.md` | 1-78, complete | `D518FC87200C34B0FBBFDCF1EFF0EE488A77A29067E60D77A0B5AB17069F7D45` |
| `spec/research/edition-2026-c7-kamp-iii1.md` | 1-193, complete | `D576C1FA5FF57E20FDD28BE2B5CAD44D1A5C41F4402A99CDF8022F2E5F094B4D` |
| `spec/verification/edition-2026-c6-text-acceptance.md` | 1-73, complete accepted dependency scope | `AEEFFB41C4D21CAF2EA0F6145FE07CDC1A26E9C7DC6B06AA10C9E8BAEC9FFC17` |
| `handbook/restoration/inherited-09328-09438.tex` | 1-519, complete target | `87C2203AE4F94D78B973B592C9CA88013E7EF0641410E512B45C79A680AB9903` |
| `handbook/parts/p09/presentations/kamp-iii1-normal-form.tex` | 1-231, complete target | `0D1EB5FC960B7F0F1EB216026AF2AAF953CD3D95F62E4ACF014345611D860B31` |
| `handbook/annex/p09/kamp-iii1-normal-form.tex` | 1-380, complete target | `A46BFF4D11C868E8A865F2F9CC89690FCB4D03A550EB6CCB755B4C067A3B7F8B` |
| `handbook/parts/p05.tex` | 1-52, complete active route and theorem hook | `068B90E56BFCF4538AFF14F0DBBF428A228A34B12736CA55484B1E3D5E64B326` |
| `handbook/restoration/inherited-02193-02340.tex` | 1-148, complete ND_CPL body and discharge definition | `5BA27894EDF744D288008B613ADF93EAC3D65385F745135DE776D5B6011316A3` |
| `handbook/restoration/inherited-03038-03104.tex` | 1-67, complete signature and term grammar | `8531B8FC91A659AB7C5B131A77FCA7AFF9C97F0A052E3B78FE0459ADEC25FFAB` |
| `handbook/restoration/inherited-03105-03165.tex` | 1-61, complete formula grammar/readability | `5C062C8A2584C841ED74EC9B546FA502EF0FF4D667A5A702EC56B7C8A49463C9` |
| `handbook/restoration/inherited-03166-03239.tex` | 1-74, complete occurrence/FV definitions | `D7D08869229F450D219BCB06FFA8E990B60DB10F195B76D53E9ECCBBC480AC3C` |
| `handbook/restoration/inherited-03240-03428.tex` | 1-90, actual substitution, complexity, alpha definition, first example | `36D7779D6B9BB3CAF0C4EF514A79A1C7D8AA10BD4A72290256EA1D09D5DB58CC` |
| `handbook/restoration/inherited-03927-04061.tex` | 1-135, complete ND_FOL body | `2AD2846970D4976177B0FBB8AC59FF8106253F5D155A5E4861956F7F651BF480` |
| `handbook/registry/calculi/nd-fol.tex` | 1-29, complete twenty-rule sheet | `F25549BC18FC4AAE212EEA32CADC9FFFD08E03D712F5DF10E9DA62F660BE5370` |
| `handbook/restoration/inherited-07678-07752.tex` | 1-75, complete PR definitions and stated proof boundaries | `1B3A7277D05F42CD5E568CC12B851F2E460BDBAB4244D11F91F30EFF78AA02DD` |
| `handbook/restoration/inherited-07753-07843.tex` | 1-23, c.e. domain and relation definitions | `E2B7284BEABCA82F440BB921D779243F1615F8D7077ABA73DFF6CBDE28458B00` |
| `handbook/restoration/inherited-07851-08048.tex` | 1-261, complete numbering/enumeration body and later boundaries | `DE01687B7F524F49D6B3E90C9ACD038550F7BE1551A1AABC771B8BBB3B4B0177` |
| `handbook/restoration/inherited-08306-08438.tex` | 1-42, arithmetic language, numerals, comparison and marked bounds | `0B020970BE72999CD771566BA0D6CDB4E4668728362CBD3C0D1606059EE9D2B8` |
| `handbook/restoration/inherited-08710-08876.tex` | 1-72, 650-707, 800-855, 952-1015: tagged extraction, Comp assembly/boundedness, theorem interface and evaluator | `4D131A6631A148354F31066316E3B73977DF71AF66C06FC98158D6C402DBC102` |
| `handbook/restoration/inherited-09099-09111.tex` | 1-13, complete Q definition | `38534E090C35DB78D99D045D19B3C7F34F1F1AAA8999CF118C7A416CD41D9D2B` |
| `handbook/restoration/inherited-09262-09327.tex` | 1-66, complete unchanged representability fragment | `75A27E87080116A235A904DAEDABE2A70DFF472BA27CA8A454C448DFD4B58BB6` |
| `handbook/parts/p09/presentations/n-c-012.tex` | 1-170, local language/order context, insertion and following III.2 boundary | `A12201D510F6FE514BC4300F65A34AAA10B0DE0429979ABD10D8BE8F07AE4E5E` |
| `spec/research/p09-kamp-1968-source-note.md` | 29-79, acquisition identity/pagination; locating search hits only elsewhere | `75B83F9C5C5874F670A18F72D0FC4C151312364F53D10EC9D002DF68DE588218` |

The governing external source is Johan Anthony Willem Kamp, *Tense Logic and
the Theory of Linear Order*, UCLA dissertation, 1968, held at
`tmp/pdfs/p09-kamp-1968/1968.kamp.thesis.pdf`, SHA256
`C39AF4D431BA7CEDBC93472A790C806AD6469574EA238750A7A688EE9A52A8CA`.
The actual PDF is an unencrypted 128-page PDF 1.3 of 11,617,255 bytes, with
letter-size pages. Its title leaf was visually read. Its recorded institutional
locator is the [Stuttgart thesis file](https://www.ims.uni-stuttgart.de/archiv/kamp/files/1968.kamp.thesis.pdf);
this review used the held file and makes no new claim about live HTTP access.

Actual visual source reading covered all of printed pages 43-56 (physical
PDF pages 52-65), all of printed pages 21-22 (physical 30-31), and printed
page 39 (physical 48). This includes every line of Definitions 4-9, Theorem
III.1, its proof, and Corollary 1. The sixteen page images for printed 21-22
and 43-56 were additionally compared pixel-for-pixel to fresh 140-dpi PNG
rendering of the corresponding pages of the held PDF, performed entirely
in memory. Every comparison was equal at 1190 by 1540 pixels. Thus the scans
read here are verified representations of the hashed PDF. OCR did not control
any formula reading. This operation rendered source pages, never manuscript
pages, and wrote no new images.

## P5 findings

### P5-SRC-01: actual syntax and the declared numbering - PASS

P5 lines 11-83 specialize the live P2 grammar to precisely the arithmetic
signature defined at `inherited-08306-08438.tex:4-16`. Equality is logical;
there is no primitive order predicate in this arithmetic language. The
thirteen tree tags cover its five term constructors and eight formula
constructors, including bottom and all three primitive binary connectives.
P2's different illustrative signature containing a relation `<` is not
silently used as this language. Numerals, infix functions, comparisons and
marked quantifiers are expanded under their existing conventions.

Positive cons uses the established Cantor pairing but adds its own terminal
and tag discipline. The empty raw list, zero term, symbol code, string code,
and formula tree code have distinct declared roles. Decoding recurses through
strictly smaller components; exact arities and type checks reject malformed
trees. P5 lines 85-139 give bounded inverses, accumulated course-of-values
rows and an explicit bounded string-to-tree search. This is a new local
construction built from the actual PR class, not a claim that decidability
alone establishes primitive recursiveness. The illustrative prime-power
code at lines 372-389 is explicitly separate from the governing codes.

### P5-SRC-02: substitution and alpha match the governing operations - PASS

The arbitrary-term routine at P5 lines 153-201 follows the exact three
quantifier clauses in `inherited-03240-03428.tex:25-46`. In its third clause,
the forbidden names are all occurrences in the current matrix, all names in
the replacement term, and the two substitution/binder variables. The chosen
name is the least available name. It preserves the source's renaming even
when the substituted variable happens not to occur freely. Preliminary
renaming stops at a repeated binder and its globally fresh target prevents
another renaming inside that pass. Closed numeral substitution therefore
has the simpler source-preserving traversal.

The alpha comparison record at P5 lines 203-222 distinguishes free indices
from nearest-binder positions. Its correctness argument is tied to the actual
syntactic congruence and fresh-renaming generators in the P2 definition:
generators preserve records, and corresponding globally fresh binder names
make equal records yield identical renamed formulas. No semantic-equivalence
test or replacement rule is substituted for alpha conversion.

### P5-SRC-03: all twenty actual rule forms and the order bridge - PASS

The tags in P5 lines 237-248 correspond to all twenty entries in the live
ND_FOL sheet. The following table records the complete coverage, with tag
numbers in P5's stated order.

| Tags | Source rule forms | Actual correspondence |
| --- | --- | --- |
| 0 | assumption | A leaf occurrence, optionally labelled; its own singleton open list |
| 1-5 | conjunction introduction, its two eliminations, two disjunction introductions | The actual child formulas, conclusion constructors and premise arities |
| 6 | disjunction elimination | Major premise and two separate minor branches; each designated formula/label must have a discharged occurrence in its own branch |
| 7-8 | implication introduction and elimination | Nonvacuous labelled discharge for introduction; the two elimination premise positions explicitly exchange between body and sheet |
| 9-12 | negation introduction/elimination, bottom elimination, RAA | Actual bottom/conclusion forms and nonvacuous discharge of the displayed assumption for negation introduction and RAA |
| 13-14 | universal elimination, existential introduction | Supplied variable, matrix and term determine the exact capture-avoiding substitution instance |
| 15 | universal introduction | Generalized variable is free in no surviving premise assumption |
| 16 | existential elimination | Supplied matrix/eigenvariable/discharge label; the eigenvariable is absent in all occurrences from conclusion, major existential formula and every surviving open assumption |
| 17 | alpha | The source's syntactic alpha relation |
| 18-19 | equality introduction and elimination | Premise-free reflexivity and the actual matrix substitution rule; zero occurrences of the matrix variable are permitted |

The body implication elimination in `inherited-02193-02340.tex` places the
antecedent before the implication. Sheet line 18 reverses those two premise
positions. P5 lines 271-276 states that exact exchange. It preserves each
subderivation and its open leaves, so the bridge does not change inference
strength. The other displayed premise orders agree.

Open assumptions are leaf occurrences, not a set used to discard multiplicity.
The postorder row conditions encode a connected finite tree. Its branch-local
filters preserve the actual formula-specific, nonvacuous discharge rules in
the body and sheet. In particular the stronger all-occurrence existential
freshness condition is preserved, while universal introduction retains its
different free-variable condition. The contexted sheet is read with its
explicit tree/discharge explanation. It supplies no extra weakening,
repetition, arbitrary substitution or logical-axiom record form.

### P5-SRC-04: finite and c.e. axiom conventions and Comp - PASS

P5 lines 308-370 select a fixed set of axiom sentences rather than its
deductive closure. Finite membership is the actual finite disjunction of
sentence-code equalities; universal instantiation uses the actual universal
elimination rule with its supplied term. Q's seven universal closures remain
its seven axiom sentences. Empty finite theories and empty root open lists
are explicitly handled.

For c.e. theories, the domain convention agrees directly with
`inherited-07753-07843.tex:9-12`. The actual enumeration theorem supplies a
domain index in the accepted P4 numbering. P5's `V(e,a,s)` evaluates the one
fixed accepted marked-bounded Comp formula by PR term/Boolean operations and
bounded sums/products. The unchanged arithmetic bound convention explains
why this value equals truth of the expanded formula. This is neither a
uniform unbounded truth predicate nor a replacement historical T-predicate.

The Comp interface in the actual P4 theorem requires valid accepting
computation with valid numerical output, and says such a history exists
exactly when the indexed function is defined. Those are precisely the two
directions used by P5 lines 445-469. One witness is attached to each surviving
open axiom leaf. Discharged temporary assumptions require no membership
certificate. There is no claimed computable bound on a successful witness.
The list/derivation numbering, machine serialization, and beta histories
remain distinct. Both P4 dependency hashes match the accepted C6 record.
This review newly checked the specified interface extents; it does not claim
a fresh complete review of all 1104 lines of the Comp file.

### P5-SRC-05: external attribution and Q/internal proof boundary - PASS

The manuscript provides its own arithmetic numbering and ND checker.
The author note accurately identifies the active handbook specifications as
its direct authorities and makes no claim to reproduce an external author's
particular coding proof. P5 lines 391-470 state and prove a standard-model
coding equivalence for this checker. The separate definition at lines
472-494 then invokes exactly the Sigma1 numeralwise relation clause of the
unchanged cited representability theorem at
`inherited-09262-09327.tex:33-42`.

The existing Shoenfield citation remains an external proof dependency for
representability. No Shoenfield body was read in this assignment and no
external source-completion finding is made for it. Numeralwise relation
representation, the stronger separately defined functional representation,
standard-model c.e. definability and internal derivability conditions retain
their different standing. The target explicitly says its checker does not
establish Q's universal statements about all codes or internal derivability
conditions for the chosen representing formula. It therefore does not
promote the local construction into completion of those later obligations.

## Kamp III.1 findings

### C7-SRC-01: exact theorem, language and source grammar - PASS

The theorem on printed page 48 quantifies over formulas with a positive
number of free variables and asserts equivalence over Lin to a standard
formula in those variables. Printed page 56 explicitly distinguishes this
Lin normal form from the later Com result, then states the Boolean-combination
sentence corollary. The target theorem at reader lines 159-190 and its
closing scope paragraph at lines 225-231 preserve that extent. The host
paragraph immediately following the insertion still assigns the additional
reduction to III.2 and Lemmas 1-10. No completion of those proofs follows
from this report.

The actual language display on printed page 21 supplies unary predicates and
the binary order predicate without a primitive equality symbol. The target
represents the equality displayed in Chapter III by the coincidence
abbreviation justified by linearity. This is a declared interpretation of
the source display, not an unnoticed addition to L. Source precedence in
Definitions 5-6 is reflected in variable-name order, essential representatives
and point order. The adjacent-chain prefix, singleton self-coincidence,
orientation of block equalities and separation of name order from point order
match printed pages 43-46. Fixing same-block equality order and parentheses
chooses a definite written representative permitted by the source conditions.

The local classes preserve the source's literal At base: unary-literal
conjunctions and its designated P0 tautology. The two regional constructors,
their three guards, their permitted inner classes, retained earlier stages
and union over stages agree with Definition 7 on printed pages 47-48.
The local nonempty operand-list convention writes empty Boolean cases with
explicit permitted P0 constants. It chooses actual source formulas for those
cases instead of claiming raw empty lists are new object-language constants.
The standard-clause component set and sentence form agree with Definitions
8-9 on printed pages 48 and 56.

### C7-SRC-02: starred rendition has an actual source conversion - PASS

Reader lines 116-127 identify starred At and regional classes as a distinct
syntactic presentation. The theorem separates their unary-support property
from source-standard membership. Annex lines 13-22 declare that the proof
temporarily suppresses stars, so order-based truth/falsehood slots during the
construction are not falsely counted as literal source At formulas.

Annex lines 342-360 restore the stars and prove the epsilon bridge. It sends
each distinguished constant slot to the source's permitted P0 tautology or
contradictory unary conjunction, preserving the displayed variable. The
induction over finite stages preserves regional guards, endpoints,
constituent-class membership and truth under every unary interpretation.
The resulting source-standard formula therefore exists with the original
free-variable set. The optional no-new-unary-predicate claim is made only for
the starred output; the final conversion may add the inessential P0 slots.
This supplies the literal source theorem rather than relying on a grammar
that merely has similar semantic behavior.

### C7-SRC-03: full source proof structure and both documented corrections - PASS

| Printed source extent | Newly read construction and source correspondence |
| --- | --- |
| 43-46, Definitions 4-6 and prefix remarks | Reader lines 11-64; annex lines 24-47 supply the finite ordered-partition argument establishing consistency, coverage and mutual incompatibility. |
| 49-50, quantifier-free basis | Annex lines 49-77 supplies prenex preparation, finite Boolean conversions, every complete order type, unary representative substitution and empty/false cases. |
| 50-51, existential equality cases | Annex lines 79-122 treats a nonessential quantified variable and an essential variable whose block has a surviving member, with forced witnesses and recursive endpoint substitution. |
| 51-52, existential strict positions | Annex lines 124-171 treats first, last and interior singleton blocks separately and proves membership at a finite successor stage. |
| 52-53, universal restrictions and grouping | Annex lines 173-242 keeps both equality orientations and all strict positions, groups by residual prefix, and explicitly covers all 2s+1 positions. |
| 54-55, equations (7)-(10) | Annex lines 218-257 includes missing positions using false consequents, then uses finite conjunctive normal form without negating component atoms. |
| 55-56, equation (11) cases and completion | Annex lines 258-324 treats equality and strict regions with all, none or some dependent disjuncts; distributes the results back to standard form. |
| 56, Definition 9 and Corollary 1 | Annex lines 362-378 gives the structural sentence argument, including vacuous quantifiers and nonempty-domain constants. |

I verified the first documented correction directly in the printed page 49
scan: the source uses a conjunction of the two strict directions in its
negated-equality replacement. Distinct assigned points in a two-point chain
refute that replacement. The disjunction in annex lines 61-64 is the correct
linear-order replacement and preserves the source theorem's intended scope.
The author note records this correction outside the reader derivation.

I also verified the second correction directly at the top of printed page 52:
the source drops witness existence in the leftmost-position case when the
local conjuncts omit the quantified variable. A one-point order with its
unary condition true refutes that step. Annex lines 145-169 retains the
existential region condition even with a true dependent component. Its
separate rightmost and interior cases preserve the same required existence.
The reader's endpoint and consecutive-integer examples expose the relevant
boundaries; no density or absence of endpoints is used.

The universal construction agrees with the source's missing-position and
empty-region precautions. A missing equality position is impossible because
the named point realizes it. A missing strict position requires an empty
region. When every disjunct is independent of the quantified variable,
the empty-region alternative is still present. The source's universal
argument already contains these precautions on printed pages 54-56; the
reconstruction supplies their full finite-position organization rather than
attributing them to a new source theorem.

### C7-SRC-04: attribution and completion boundary - PASS

The proof uses independent exposition and traces the actual source case
structure. The author note identifies the two corrections and the separate
starred support property. The proof's effectivity argument concerns finite
syntactic operations and the exhausted original quantifier prefix; it asserts
no efficiency or output-size bound. Neither the source theorem statement nor
the reconstructed one identifies these first-order regional components with
temporal operators. III.2, Lemmas 1-10, the subsequent passage to the image of
D over Com, and the other Kamp presentations retain their separate obligations.

## Review conduct and handoff

The PDF skill guided inspection of the actual scanned source, including the
direct PDF-to-image correspondence check. The research skill guided primary
authority tracing and this single evidence file. The assignment's explicit
no-delegation instruction controlled its background-agent suggestion. A
lightweight prior-memory lookup supplied only the frozen-snapshot review
discipline; all current manuscript and source facts above were newly checked.

Only this report was authored. No manuscript, code, registry, source PDF,
provenance record or author note was edited. No test, manuscript build,
manuscript rendering, source acquisition, delegation or admission operation
was performed. All three target hashes matched the assigned frozen hashes.
The root integrator retains the notation/catalog/provenance seam and the
remaining independent review and production gates.
