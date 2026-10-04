# N-c-012.c independent manuscript review record

## Admission scope

This record closes the reader-facing body reconstruction and the three
independent manuscript-content review gates for exactly `N-c-012.c`: Dov
Gabbay, Amir Pnueli, Saharon Shelah, and Jonathan Stavi's 1980 presentation,
“On the Temporal Analysis of Fairness.” Its principal reader scope begins at
`\subsubsection{The GPSS presentation of fairness and expressive
completeness}` in `handbook/parts/p09/presentations/n-c-012.tex` and ends
immediately before the Sistla--Clarke presentation. The relevant shared Part IX
strict/inclusive convention bridge, discrete-word theorem, bibliography entry,
source note, and source-presentation record were reviewed with it.

Acceptance does not certify every formula, proof sketch, or bibliographic
detail printed by GPSS as correct. The accepted presentation expressly
preserves the p. 164 future-direction conflict, the one-sided next-time clause,
the p. 170 proof-numbering tension, the missing event-expression and gap-operator
definitions, the incomplete canonical-model account, the p. 172 path-condition
omission, the p. 173 `U^0` conflict, and the source's literal `19th`-FOCS
reference discrepancy. Acceptance means that the source statements, defects,
counterexamples, handbook-owned repairs, external-referral boundaries, and
proof-strength limits are themselves stated correctly.

This record does not admit `N-c-012.d`, `N-c-012` as a whole, Part IX, any
other handbook part, a generated handbook, rendered-page inspection, human
review, final-book completion, or user acceptance.

All three final reviewers accepted the following exact pre-admission snapshot:

| Artifact | SHA-256 |
|---|---|
| `tmp/pdfs/p09-gpss-1980/gabbay-pnueli-shelah-stavi-1980.pdf` | `2C8FF0E169D2D37B2B402907741AB8FCD67C2883395A4C1655775AB3723A4DA2` |
| `tmp/pdfs/p09-gpss-1980/page-08-quantifier-symbols.png` | `D74FF885AC1010EA703749F215D1E47DFB3649595F3F8C0A282E073DB714C0F9` |
| `tmp/pdfs/p09-gpss-1980/page-10-closure-crop.png` | `F49C546E4F07A005BA548AB594C6F63B01B37FC62FE3D8DD89A3FAE44EAEA434` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `DD9DF6D66A6632D98DBF88DD9968C299320B103F317932C836D624D21E76033F` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `DAE8982D6CAA548BEBCB916B197399B6499A7C6DB966E6972CC4E2C50AC163BA` |
| `handbook/bib/handbook.bib` | `BB4096F50E3359E2F07187E1B898F8A8E65CF4A3AC3C288E3FA58099A2A53380` |
| `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md` | `038BB890132E61EABB91540EA6CC8BAEC5BFF897FC749FD52CEBD69FCBE2B060` |
| `spec/research/p09-source-presentations-lot2-3.md` | `F0681E77E779236104BF4B490FFCBA9400068AF0026F360A7F1CF0B740EE40CD` |

The source-presentation-record hash is the pre-admission status surface read by
all three reviewers. Its subsequent status-only edit records their unanimous
verdict and links this review record; the resulting post-admission hash is
`B3DCC1380B76AA50BB9D3CC1D9F2263E2A306895DFD7F47596D65D4F7D85AA22`.
That edit changes no reader-facing mathematics, source claim, bibliography, or
source note. The accepted reader and source note remain byte-identical to the
reviewed snapshot.

## Primary authority surface

The controlling primary authority was the complete author-archive PDF linked
from Saharon Shelah's paper record:

- author record: `https://shelah.logic.at/papers/134/`;
- PDF: `https://shelah.logic.at/files/95957/134.pdf`;
- local object: `tmp/pdfs/p09-gpss-1980/gabbay-pnueli-shelah-stavi-1980.pdf`;
- controlling SHA-256:
  `2C8FF0E169D2D37B2B402907741AB8FCD67C2883395A4C1655775AB3723A4DA2`.

The PDF has eleven physical pages corresponding directly to printed pages
163--173. Every final reviewer visually read all eleven pages and both
controlling enlarged crops. The p. 170 crop established that both future
quantifier restrictions use the inclusive sign `>=`; the p. 172 crop
established the literal three `Gamma`-closure obligations, including the
easily misread `XA` to `X not-A` clause. Images controlled over OCR, notes, and
memory. The crops were reading derivatives, not substitute authorities.

The embedded `Author` metadata names Pnueli, Shelah, and Stavi but omits Dov
Gabbay. The printed four-author title page controls. The frozen hash identifies
the inspected author-archive object; it does not establish byte identity with
an ACM-hosted file. Printed p. 163 carries ACM's conditional copying notice,
not an open-content licence. The handbook therefore uses independently written
scholarly reconstruction rather than republishing protected source expression.

## Reviewer transcripts, runtime, and independence

| Seat | Canonical reviewer | Final transcript | Transcript SHA-256 | Verdict |
|---|---|---|---|---|
| source fidelity | `/root/schmidt_smolka_1991_research/gpss_primary_pass` | `spec/research/boards/p09-n-c-012c/transcript/r4-source-fidelity.md` | `44F3A34BC87DD4E0CE3145A8FE45EFA6CAC2BC9AAF4847E0220F3D7C88626777` | **ACCEPT** |
| mathematical/proof correctness | `/root/schmidt_smolka_1991_research` | `spec/research/boards/p09-n-c-012c/transcript/r4-mathematical-proof.md` | `C5E3B9B1F6DBA3E7344C5DF4D19DDE1940AA89F89B872450847C7E6F949A571E` | **ACCEPT** |
| adversarial publication/AGENTS | `/root/mcnaughton_1966_research` | `spec/research/boards/p09-n-c-012c/transcript/r4-adversarial-publication.md` | `266EE401DAB5E61312322689B36D6AFF8A049FBC664B2E308424564625ABF64D` | **ACCEPT** |

The runtime did not expose an exact serving model, deployment version, or build
identifier to any final seat; the unavailable information is recorded rather
than guessed.

Each reviewer was instructed to read the complete frozen topic scope and every
authority page, not to inspect the board ledger, chair record, a prior-round
transcript, or another reviewer's transcript or verdict, not to contact another
reviewer, and not to edit a frozen artifact. Each created only its assigned
round-four transcript. Each independently computed all eight frozen identities
before substantive review and again immediately before filing; every value
matched. After all three reports were complete, the chair read each transcript
in full and independently recomputed the eleven controlling hashes: all eight
frozen artifacts and all three final transcripts matched exactly.

This was manuscript scholarship, not software engineering. No reviewer and no
chair operation used a test, test harness, automated checker, repository
script, TeX command, handbook-PDF inspection, or build. Primary-source visual
reading, direct text inspection, mathematical reasoning, provenance inspection,
and SHA-256 identity labels were the review methods. These manuscript-content
reviews establish no compilation or rendered-page result.

## Source-fidelity review

- Canonical reviewer:
  `/root/schmidt_smolka_1991_research/gpss_primary_pass`.
- Role: primary-source identity, complete clause fidelity, attribution,
  locators, and acquisition boundaries.
- Final verdict on the common round-four snapshot: **ACCEPT**.

The source reviewer freshly read printed pp. 163--173 and both controlling
crops, then reread the complete reader presentation, shared convention bridge,
bibliography entry, 1,179-line source note, and source-presentation record. It
found no remaining source-fidelity defect, undisclosed ambiguity, unsupported
acquisition claim, reversed source mapping, silent source repair, proof
promotion, or cross-file inconsistency.

The review specifically confirmed the exact p. 169 respective mapping:
Pnueli's `[P2]` work is reported as the earlier proposal for `DX/L(X,F)`, and
the Myers--Pnueli `[MY]` technical note as the earlier proposal for
`DUX/L(X,F,U)`. It verified the source-note identities of `[FL]`, `[G1]`,
`[G2]`, `[MP]`, `[MY]`, `[P1]`, `[P2]`, and `[SS]`; the nonacquisition and
nonverification boundaries for referred external bodies; and the literal
`19th` in GPSS's `[P1]` entry against the separately acquired publisher record
identifying the 1977 paper with the Eighteenth FOCS.

It also confirmed the full initial grammar, strict semantics, source defects,
program examples, four distinct expressiveness questions, unequal theorem
domains, exact `DX/DUX` schemes and rules, canonical-model assertions, closure
obligations, transformed systems, `U^0` conflict, and the separation from later
LTL, automata, complexity, and model-checking results.

## Mathematical and proof review

- Canonical reviewer: `/root/schmidt_smolka_1991_research`.
- Role: mathematical correctness, typing, quantification, semantic convention,
  theorem strength, local derivation, and proof ownership.
- Final verdict on the common round-four snapshot: **ACCEPT**.

The mathematical reviewer independently reconstructed the complete proof
surface from a fresh visual read of all eleven authority pages. It found no
type error, quantifier error, invalid handbook calculation, unsupported theorem
strength, proof-ownership error, or unresolved mathematical uncertainty.

The review directly rechecked the strict/inclusive and operand-order bridges,
including both recursive translations and their `X/Y` dependence; every
theorem's exact order class and evaluation-point hypothesis; the complete
normal-form and event-expression omission boundary; system-relative maximal
consistency; the exact restricted canonical domain; all literal `Gamma`
closures; quotient and path standings; and the truth-lemma and decision-bound
omissions.

For the p. 173 defect, the reviewer recomputed the separating natural-number
model: at time zero, `A` is false; at every later point, `A` is true; and `B` is
false everywhere. Strict `GA` makes the printed defining equation true at zero,
whereas the right side of printed `U0.2` is false. Thus the two displays cannot
jointly define one coherent operation. The manuscript correctly leaves
substitution of `G^0A` for `GA` as a possible unprinted repair and qualifies the
`D^0UX` completeness report.

## Adversarial publication and AGENTS review

- Canonical reviewer: `/root/mcnaughton_1966_research`.
- Role: omissions, unsupported additions, source/handbook ownership,
  definition-before-use, terminology, integration, and publication readiness
  at the declared manuscript scope.
- Final verdict on the common round-four snapshot: **ACCEPT**.

The adversarial reviewer reread the full authority and all frozen topic
surfaces, inspected both adjacent topic boundaries, and tried to falsify source
identity, theorem domains, formula direction, proof ownership, reference-key
standing, status language, and cross-file consistency. It found no blocking or
must-fix defect.

The five-part technical-name rule was checked at each load-bearing handbook
addition. Local strict `U_s/S_s`, the temporal-to-first-order translation,
`Pr`, and the strict/inclusive translations have stated necessity, exact
eliminable definitions, standing, nonredundancy, and actual later use. Source
labels whose required definitions are absent---GPSS's past `S`, gap symbols
`S'/U'`, event expressions, and a coherent `U^0`---remain identified as missing
or conflicting source artifacts rather than being adopted as invented handbook
objects.

The review also confirmed that `Pr` is used in exactly three following
displays---general FIFO, the implementation-specific semaphore instance, and
the repeated-response refinement---and that the last formula is the source's
printed refinement, not a handbook repair. Its premortem found that the
accepted text directly blocks the plausible publication failures: silently
correcting pp. 164 or 173, collapsing four until conventions, promoting proof
outlines or external manuscripts into complete local proofs, leaving source
keys opaque, or retrojecting later automata and complexity results.

## Revision history and closure of admitted findings

Four blind review rounds were required. No majority vote was used, no supported
finding was discarded, and an acceptance from an earlier hash was never carried
forward to a changed snapshot.

1. Round one returned three `REVISE` verdicts and admitted F01--F10. The
   resulting repairs corrected provenance and metadata, restored the complete
   initial grammar, fixed the local-`G` explanation and busy-wait calibration,
   defined program-state symbols before use, corrected the semaphore-FIFO
   standing, restored Lemma 1's proof boundary, typed the canonical assertions,
   stated the transformed systems exactly, and exposed the p. 173 `U^0`
   contradiction with a countermodel rather than silently repairing it.
2. Round two returned mathematical/proof `ACCEPT` and two `REVISE` verdicts,
   admitting F11--F13. The repairs made maximal consistency system-relative,
   disclosed the source's unprinted selection of `Delta_0`, replaced an
   undefined descendant gloss with the exact restricted domain, stopped calling
   syntactic `Gamma` literally finite, and identified `[SS]` and its external
   proof-ownership boundary.
3. Round three returned source-fidelity and mathematical/proof `ACCEPT` and
   adversarial publication `REVISE`, admitting F14--F16. The repairs expanded
   `[G2]`, `[P2]`, and `[MY]` at first reader use, restored the exact
   `[P2]/[MY]` respective mapping, mapped every load-bearing source key and its
   acquisition standing, corrected the repeated-response description, and
   named all three actual uses of `Pr`.
4. In round four, all three reviewers independently reread the complete
   authority and artifact scope and returned **ACCEPT** on the exact common
   eight-artifact snapshot recorded above. The chair then read all three final
   transcripts in full and independently confirmed every hash.

F01--F16 are therefore incorporated and accepted for this exact snapshot.
Nothing in this admission asserts that GPSS supplied the handbook's repairs,
that an external manuscript body was acquired or independently proved, that
the conflicted `U^0` has one coherent source definition, or that the source
contains later LTL, automata, complexity, or model-checking results.

This closes body-level reader reconstruction and topic-level manuscript review
only for `N-c-012.c`. `N-c-012.d`, `N-c-012` overall, Part IX admission, the
single final publication build reserved until all fourteen parts are
text-frozen, rendered-page inspection, human review, final-book completion, and
user acceptance remain open.
