# P18: original evocation and implication pattern completion

Assigned bounded authoring continuation on 2026-10-03. The first recorded
clock checkpoint was 17:55:04 UTC. Parent owns shared drivers, canonical
registries, bibliography, manifests and coverage decisions. This child owns
only the new reader, matching annex, source rule sheet, notation/bibliography
intakes and this note. Existing implication/search packets and their raw
intakes were not edited. No children, reviews, software tests, builds or
manuscript renders were run.

Research skill was used for primary reading and this single source note;
the parent assigned the background research/authoring task. PDF skill caused
read-only inspection of the original source pages for mathematical glyphs,
not rendering of the manuscript or creation/editing of a PDF deliverable.

## Source identity and actual reading

Held original, not reacquired:
`source/references/p18-erotetic-implication/wisniewski-2001-questions-inferences.pdf`.
SHA256 `accf78facefd12d5256db5b08c752ebd99e74cf0f264ee51b7528eef96e6e131`;
252,997 bytes, 39 physical pages. Andrzej Wisniewski, *Questions and
Inferences*, literal issue imprint *Logique & Analyse* 173--174--175
(2001), printed 5--43. The running production stamp is 2003/6/9; it is
not identified here as a distinct journal edition or as the separate
2003 *Synthese* paper.

Original archive URL:
https://logiqueetanalyse.be/archive/issues87-220/LA173-174-175/01wisniewski.pdf.
The local bytes, not a current remote metadata assumption, were consulted.
Actual text reading covers physical1--39 / printed5--43. Any truncated
combined output at printed39--40 was repaired by a separate bounded reread.
Pixel inspection covers printed20,22,23,27,28,29 and38,39,40. Source-only
PNG cache is `tmp/p18-erotetic-patterns-source-pages/`; no manuscript pages
were rendered. The immutable source PDF was not edited.

Read the existing `question-to-question-implication.tex` reader/annex,
`erotetic-search-scenarios.tex` reader/annex and search sheet before selecting
the new seam; narrow rereads repaired earlier truncated output. The PMCE
chapter's actual language/evocation/calculus definitions were also inspected
to preserve the distinction between semantic warrants and PMCE proof
judgments. The full book was not reviewed.

## Delivered scope and exact source-to-result map

New reader is `handbook/parts/p18/erotetic-patterns-and-composition.tex`.
New proof annex has the same basename under `handbook/annex/p18/`.
The source numbering is retained in the literal sheet
`handbook/registry/calculi/p18-erotetic-patterns.tex`, included by the reader
after the syntax/family/analytic definitions. Fourteen reciprocal
result/proof pairs are saved, and the sheet contains forty entries:
twenty-one E examples plus nineteen Im examples.

The common label stem is `thm:p18-ep-` for results and `annex:p18.ep.`
for their full proofs. The following suffixes identify exact units:

| Source locator | Result/proof suffix | Supplied extent |
|---|---|---|
| (6.5)--(6.15), printed20 | propositional-evocation | All eleven cases; coverage and a countervaluation for each individual answer; original parentheses and native CPC signs |
| (6.16)--(6.19), printed22 | firstorder-polar | Every finite observation list, both models for each polar answer, equality aliasing/distinct-denotation cases |
| (6.20)--(6.24), printed22 | named-evocation | Named-or-residual witness, both finite lists and whole S-answer sets; non-entailment for every constant, including unlisted names |
| (6.25), printed23 | complete-list | Explicit finite disjunct family; every arbitrary finite candidate U-answer, not merely the displayed extension lists |
| Conditions in (6.16)--(6.25) | evocation-boundaries | Domain closure, unique names, singleton restriction, single extension disjunct and unnamed witness countermodels |
| (8.1)--(8.3),(8.7),(8.10)--(8.11), printed27--28 | pure-patterns | Both negation directions, permutation, four reverse binary truth functions, each forward polar-to-binary direction; actual singleton/proper-subset witnesses |
| (8.4)--(8.5), printed27 | general-refinement | Arbitrary well-formed formula instances, not only frozen distinct-atom examples; both directions and analytic status, with dependent-instance regularity boundary |
| Definition11 and note14; tags at (8.1)--(8.3),(8.7),(8.10)--(8.11) | analytic-profile | Exact subformula condition; independent-atom failures and distinct compound-formula analytic instances |
| (8.12)--(8.13), printed28 | signed-cofactors | Every connective and both signs; full truth-function cases, no informativeness promotion |
| (8.14)--(8.15), printed28 | polar-refinements | Three-answer pattern and every n/index; proper complementary witnesses, n=2 regularity, independent n>2 countercases |
| (8.16), printed28 | denial | Every negative target answer; both indispensable premises and regularity limits |
| (8.18)--(8.21), printed29 | partition-patterns | Every nonempty finite block split and both responses; exact premises, singleton n=2 and larger-block countercases |
| (8.22), printed29 | arbitrary-formulas | Full arbitrary Ax,Bx,Cx extent; structural closed-substitution proof including bound variables/quantifiers, and all four target conjunction answers |
| (8.26), printed29 | wh-polar | Every listed index, both responses, properness in the entire wh-answer set, n=2 regularity and n>2 failure in general; both lost-premise models |

The new general-refinement pair was necessary because the frozen first
packet states only distinct-atom examples for source (8.4)/(8.5).
Its valid instance proofs remain untouched. The new rule sheet fully
expands the original source premises rather than substituting the proof's
editorial D/K/N/H abbreviations into those displayed rules. Complete-list
first/last lists retain the source's c/c-prime notation; the finite
intermediate family is explicitly typed in the reader.

## Syntax, conditions and correction provenance

1. Native implication is `\supset`, native Boolean biconditional `\equiv`,
   binary question `?\pm|A,B|`, connective parameter `\otimes`, sign choices
   `\alpha A`/`\alpha B`, and closed substitution `A(x/c)`. The original
   paper's images confirm these signs. Their local types are declared before
   use and recorded honestly, rather than rewritten to house glyphs. The
   existing canonical elementary-equivalence and linear-tensor roles are
   not identified with these roles.
2. Distinct constant symbols do not imply distinct denotations. Countermodels
   are permitted to interpret finitely many symbols distinctly; no such
   axiom is added to the source model class. Complete-list (6.25) uses the
   source's distinct-metavariable convention for its alternative name lists.
   If the alternatives are instead collapsed to one extension constraint,
   a listed complete answer is entailed and evocation fails. Every arbitrary
   candidate list is covered by the proof, including outside names.
3. Printed (8.21) literally has a stray comma between the initial disjunction
   and its conditional sign. The coherent premise is
   `(A_1 or ... or A_i) \supset B`, followed by the other conditional and
   the separate full coverage disjunction. The reconstruction supplies this
   single conditional directly, not an extra standalone block premise.
   Source printed29 pixels retain positive evidence of the literal surface.
4. The generic non-analytic tags at (8.10)/(8.11) cannot be asserted as
   non-analyticity of every formula instance. Under the source's exact
   Definition11, A=p-and-q,B=p is analytic in (8.10), although the two
   formulas are distinct. Its reversal is analytic in (8.11). The active
   theorem gives the exact syntactic condition; independent atoms recover
   the non-analytic examples. No Boolean-equivalence subformula closure is
   introduced.
5. Source (8.14) has no auxiliary premise although it is placed in the
   subsection headed nonempty bases. The new sheet and proof keep its empty
   basis. For n>2, source annotations saying regular *if n=2* are not changed
   into an assertion that every larger dependent formula instance is
   nonregular; explicit independent-atom countercases prove only the correct
   general limitation.
6. The arbitrary-formula (8.22) proof is not replaced by the atomic predicate
   search example. It proves substitution for Boolean, equality and bound
   quantifier cases. The wh-polar witness for a negative response comes from
   both existence and finite restriction; neither is treated as an implicit
   global naming assumption.

All known issues in this new writing were corrected directly before freezing;
the reader does not carry task logs or an instruction to repair a false
earlier claim. These independently supplied proofs are not represented as
printed proofs in the original expository paper.

## Bounded source-native transformation proposal for the saved search packet

Parent requested a mapping only; this child did not edit the frozen files.
The exact target set is the saved search reader, its matching annex and
`handbook/registry/calculi/p18-erotetic-search.tex`.

| Inventoried target expression | Native replacement | Boundaries |
|---|---|---|
| `\mathcal B(A,B)` | `?\pm|A,B|` | Search reader declaration/binary warrants/procedure premises, annex binary warrants/scenario prefix, sheet identity |
| `\mathcal B(P_2a,P_3a)` | `?\pm|P_2a,P_3a|` | Predicate reader R-definition only |
| `\mathcal B(Rc,Tc)` | `?\pm|Rc,Tc|` | Predicate procedure sheet side condition only |
| `\to` | `\supset` | All inventoried occurrences in exactly these three files are object-language material conditionals: departure bases/endpoints, connective range, Figure10 and its proof |
| `\leftrightarrow` | `\equiv` | All inventoried occurrences are object-language Boolean biconditionals: umbrella/predicate bases, connective range, Figure12 and its proof |
| `\circ` | `\otimes` | Confined binary-warrants and search-procedures metavariable occurrences; declare the same finite connective range |

Leave every `\mapsto` response-action arrow, semantic Im/E judgment,
entailment sign, set relation and other manuscript file untouched. This
proposal is based on the actual inventoried saved text and printed27--29,
38--40 images; it is not a request for a book-wide blind replacement.
The binary declaration should say the native expression abbreviates the
explicit four-answer question, not introduce a second semantic object.

Proposed native-search supplement, to be integrated only by the parent:

- `?\pm|A,B|`: binary conjunctive question, declaration at
  `sec:p18-erotetic-search-scenarios`, four literal conjunction answers.
- `\supset`: local source-native material conditional, same declaration;
  usages in departure/predicate/scenario/procedure owners and their proofs.
- `\equiv`: local source-native Boolean biconditional, same declaration;
  distinct from the global elementary-equivalence role.
- `\otimes`: metalinguistic connective parameter, binary-warrants declaration
  at `thm:p18-es-binary-warrants`; all four Boolean connectives, not tensor.

If parent has already applied part of this mapping, use the current files
and do not replay it blindly. The historical raw intake remains preserved.

## Integration seam, frozen identities and residuals

Insert this reader after the existing implication fragment and before the
search-scenario continuation; add the matching annex in the same conceptual
order. All prerequisites referenced in this reader are in the existing
implication fragment. The source's definitions precede the literal sheet.
No new macro or style change is required. Parent owns input routes and
canonical/scoped glyph integration.

Frozen authored files, with hashes read before this note was saved:

| File | Lines | SHA256 |
|---|---:|---|
| parts/p18/erotetic-patterns-and-composition.tex | 331 | f9d77175de6dfa4af83817a8412eb465ca218b170b4907d68c69027d2d249000 |
| annex/p18/erotetic-patterns-and-composition.tex | 553 | 5ab2cddfcdcdc1eb27d3f4b2b4c6d1713bac69eaaa571712791c835b5c65adc9 |
| registry/calculi/p18-erotetic-patterns.tex | 122 | 181ba8ec0217f39131c36ffd060be65a6ef4d8f3c4692d37355aa89b684fbaad |
| registry/symbols-intake-p18-erotetic-patterns.csv | 30 | 65fdb97b7cdc619856d0b60f7fafd9c9ae16d623184e59272bbcbd23441d30f9 |
| bib/intake-p18-erotetic-patterns.bib | 5 | ca61a94f7214d6bead34ba98543991ab2e840925736ef27526de15c946969c59 |

The symbol intake has 29 raw seven-field records. Explicitly grouped families
are not atomic-glyph counts. Local C_j/T denotation sets and numeric truth-cell
labels are declared in their actual annex proofs. Local object-predicate and
model-extension P/R roles are declared explicitly in the annex introduction
and recorded separately; the question R is not renamed to hide that typed
source role. Bibliography intake contains
five provenance comments and no duplicate/new key: reuse
`Wisniewski2001QuestionsInferences`. Root's existing bibliography reading note
for its first block is historical, not automatically a record of this later
full-paper reading.

Reader, annex and sheet were read back, including repaired superscript
formatting and the correct conditional cofactor table. Matching result/proof
labels were inspected, forty rule entries enumerated, and the actual CSV
parsed as seven fields. This is author self-checking, not an independent
source-fidelity/correctness/adversarial review, a proof-assistant check, a
successful build or a rendered-page inspection. None of those is claimed.

New source units are reconstructed at the stated scopes; the full 2001 paper
is not admitted as complete solely from these files. The already saved
(8.6),(8.8),(8.9),(8.17),(8.23)--(8.25) still require exact integration
with their own bodies/proofs and native source syntax. Source introductory
arguments, generation and its qualifications, the compactness/direct-or-partial
answer observation in section7, and every other source component require their
own existing or new actual coverage evidence; no whole-paper credit is inferred
from reading all its pages.

The separate Wisniewski2003 *Erotetic search scenarios*, *Synthese*134,
389--427, remains a distinct unheld/unread source body in this work block.
The independent generalized proofs in the earlier packet do not waive its
source acquisition/presentation obligations. Harrah/Ginzburg/Hintikka and
the application/reducibility originals remain separate authorities. Public
access to this original is not publication-rights clearance. Whole-book
coverage, final reviews and publication completion remain the parent's full
objective, not the completion status of this bounded packet.
