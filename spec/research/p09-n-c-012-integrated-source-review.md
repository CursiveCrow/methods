# Part IX `N-c-012` integrated source-boundary review

## Scope and method

I read the complete actual LaTeX file
`handbook/parts/p09/presentations/n-c-012.tex` directly from line 1 through
EOF at line 3020.  I also read the actual integration text needed for this
review in `handbook/parts/p09/logic-in-computer-science.tex`: the reused LTL
and past-operator definition (lines 605--626), the exact strict-order domain
boundary (lines 628--637), the strict/inclusive translations (lines
639--685), the discrete-word expressiveness and operator-sensitive PSPACE
theorems (lines 687--711), the shared safety/liveness definition (lines
713--721), the model-checking method and theorem (lines 764--812), and the
`\input` seam (lines 900--909).

As supporting records, I read completely the five requested source notes and
the five requested independent-review records:

- `spec/research/p09-kamp-1968-source-note.md` and
  `spec/research/p09-n-c-012a-independent-review-record.md`;
- `spec/research/p09-pnueli-1977-source-note.md` and
  `spec/research/p09-n-c-012b-independent-review-record.md`;
- `spec/research/p09-gabbay-pnueli-shelah-stavi-1980-source-note.md` and
  `spec/research/p09-n-c-012c-independent-review-record.md`;
- `spec/research/p09-sistla-clarke-1985-source-note.md` and
  `spec/research/p09-n-c-012d-independent-review-record.md`; and
- `spec/research/p09-alpern-schneider-1985-source-note.md` and
  `spec/research/p09-alpern-schneider-1985-independent-review-record.md`.

This was an actual-LaTeX source and integration review.  I did not inspect or
create a manuscript PDF, page render, image, or screenshot.  I ran no test,
checker, repository script, TeX command, or build, and I did not recompute any
hash.  I did not reopen or re-review any original historical-source body; the
ten named records were used only as supporting evidence for the integrated
LaTeX.

## Must-fix findings

### IS-01 -- The final boundary paragraph changes Pnueli's semantic relation into an object-language operator

`handbook/parts/p09/presentations/n-c-012.tex:3011--3014` says that Pnueli's
“printed leads-to operator is strict.”  That standing contradicts the same
actual presentation's exact local definition.  At lines 473--476,
`\varphi\leadsto\psi` is expressly a source-local temporal-implication
statement family and a relation between state assertions, “not a new primitive
in the handbook's LTL grammar”; lines 478--483 give its strict-future
quantifier clause.  Formula-level inclusive `F` and `G` are introduced only
later, with their recursive word-position clauses at lines 830--856, and the
source-internal strict/inclusive tensions are kept separate at lines 679--687.
The shared Part IX definition likewise identifies the actual temporal formula
constructors at `logic-in-computer-science.tex:605--624`.

This is not merely stylistic.  The review mandate requires the semantic and
formula levels to remain distinct, and the workspace technical-name rule
requires exact standing.  Calling `\leadsto` an “operator” invites the false
reading that it is an object-language connective comparable to `F` or `G`,
undoing the distinction established in the source-specific body and confirmed
by the Pnueli source/review records.

Required repair: describe it as Pnueli's printed temporal-implication relation
or statement family, whose consequent requires a strictly later witness.  Do
not call it an LTL operator.

### IS-02 -- The final paragraph misassigns and underspecifies the GPSS strict/inclusive bridge

`handbook/parts/p09/presentations/n-c-012.tex:3014--3016` grammatically assigns
to Gabbay, Pnueli, Shelah, and Stavi both the strict future language and “over
discrete time, a translation to inclusive word operators.”  The integrated
LaTeX establishes a more qualified ownership and a materially more exact
translation:

- GPSS's strict future convention and source `U` clause are reconstructed at
  lines 1227--1273.
- The past constructor `\mathsf S_s` used for the bridge is explicitly
  handbook-supplied, not transcribed from a GPSS grammar or truth clause, at
  lines 1274--1286.
- The exact discrete bridge is the handbook's metalinguistic equivalence at
  lines 1307--1328 and at
  `logic-in-computer-science.tex:639--685`.  It requires `\mathsf X` and
  `\mathsf Y` together with inclusive strong `\mathsf U` and `\mathsf S`;
  inclusive `U,S` alone are expressly not credited with next/previous
  expressiveness (`logic-in-computer-science.tex:680--685`).
- GPSS's own printed comparison with earlier present-inclusive notation is a
  different artifact, and its literal `U^0` equation conflicts with its
  recursion scheme; the presentation therefore refuses to adopt it as one
  coherent operator at lines 1789--1842.
- The proof/source boundary at lines 1844--1849 expressly says that the public
  discrete-word theorem uses the stated handbook bridge and does not upgrade a
  source outline into a complete proof.

Thus “inclusive word operators” is both ownership-ambiguous and technically
underspecified.  It can be read as GPSS's conflicted `F^0,G^0,U^0` comparison
or as the handbook's modern inclusive strong operators, and it suppresses the
load-bearing `X/Y` requirement.  It also fails the workspace naming rule:
existing exact terminology already states the distinction, while this new
one-off phrase has no local definition, nonredundancy explanation, or later
use.

Required repair: assign only the strict future language to GPSS, then say that
the handbook, on `\mathbb N`, relates GPSS's strict `\mathsf U_s` (and the
handbook-supplied past dual `\mathsf S_s`) to the already defined
`\mathsf X,\mathsf Y` plus inclusive strong `\mathsf U,\mathsf S` language.
Keep GPSS's separate and internally conflicted `U^0` comparison out of that
claim.

## Integration findings that pass

Apart from IS-01 and IS-02 in the new final paragraph, the five complete
presentations remain source-distinct in the actual LaTeX:

| Presentation | Actual-LaTeX scope | Convention, domain, and standing preserved |
|---|---:|---|
| Kamp 1968 | lines 6--369 | Strict witness/open-interval prefix `S,U`; temporal-to-first-order translation over every binary structure; converse only over complete strict linear orders; integer, rational, and real-order separations kept distinct; the sparse-square correction is explicitly handbook-owned. |
| Pnueli 1977 | lines 370--1205 | Transition systems, state assertions, a strict semantic temporal-implication relation, later inclusive `F/G`, system/proper-execution domains, proof rules, and source proof gaps are kept separate from modern LTL and automata results. |
| GPSS 1980 | lines 1206--1850 | Strict future `F,G,U_s`, source/handbook past-constructor ownership, four unequal first-order theorem domains, outline versus external-referral boundaries, `DX/DUX`, and the conflicted `U^0` material are separately stated. |
| Sistla--Clarke 1985 | lines 1851--2631 | Inclusive strong `U,S`, the existential `R`-path problem, reconstructed validity standing, operator-sensitive NP/PSPACE rows, journal/conference boundary, and handbook-owned corrections are not converted into GPSS or automata results. |
| Alpern--Schneider 1985 | lines 2632--3008 | Properties are arbitrary subsets of the full nonempty `S^\omega` execution space; safety/liveness are semantic classes rather than formula shapes; fixed-system relativization, topology, decompositions, source defects, and handbook repairs remain explicit. |

The shared Part IX LaTeX is otherwise coherent with those boundaries.  Its
past operators are defined inclusively (`logic-in-computer-science.tex:605--624`);
its strict/inclusive bridge states the correct operand order and the necessary
`X/Y` dependence (lines 639--685); its discrete-word theorem has the exact
`\mathbb N` pointed-word domain and two-direction language (lines 687--694);
its PSPACE theorem identifies the inclusive `L(U,X)` basis without promoting
another fragment (lines 696--711); and its safety/liveness definition classifies
word properties semantically rather than by typography (lines 713--721).
The model-checking theorem also preserves Sistla--Clarke's existential-path
problem as the complement-side source for universal checking (lines 799--811).

The `\input{parts/p09/presentations/n-c-012}` seam at
`logic-in-computer-science.tex:904` is correctly placed after every shared
definition and theorem referenced from the presentation, including the
infinite-word automaton definition and model-checking theorem, and before the
next Part IX section.  No undefined forward dependency or source-body
substitution is introduced by the seam.

The final boundary paragraph is necessary and otherwise chooses the right five
axes: order-theoretic expressiveness, transition-system proof reasoning,
strict temporal syntax, operator-sensitive decision problems, and semantic
execution properties.  It is not sufficient in its present wording because
its Pnueli and GPSS sentences contradict the exact standing and ownership that
the preceding 3008 lines carefully establish.  Both findings are local to
lines 3011--3016 and can be repaired without changing any of the five
source-specific bodies or the shared Part IX theorems.

VERDICT: REJECT -- IS-01, IS-02
