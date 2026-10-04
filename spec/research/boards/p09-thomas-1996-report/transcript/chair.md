# Chair transcript -- Thomas 1996 report precursor

## Round 1 opened -- 2026-08-23

The seven objects are frozen under the Round 1 table in `../charter.md`. Three
fresh blind seats must independently recompute all identities, inspect all five
identity/page-map renders and all thirty-nine substantive source-page renders,
read the chartered textual scope, and dispose of `H01`--`H22`.

The exact question is whether the May 1996 report-precursor reconstructions for
`N-c-013.e` and `N-c-014.e` may be admitted at manuscript-content level. The
registered 1997 chapter body and reconciliation remain open. Rabin's 1969
presentation, either containing presentation file overall, Part IX, a build,
rendered-handbook inspection, human or user review, the book, and publication
are outside the question.

This is manuscript scholarship. No test, test harness, automated checker,
repository script, TeX command, interim handbook build, handbook-PDF
inspection, or build is authorized.

Status: ROUND 1 OPEN.

## Round 1 reconciliation -- 2026-08-23

All three reports were physically filed before the chair read any report. Each
seat independently matched the seven frozen native identities. The filed report
identities are:

| Seat | Report SHA-256 | Verdict |
|---|---|---|
| Source fidelity | `2EF56BD42CA090393A2631D0CC358B9D85572BF37387F8AA884D3157587C02AE` | `REJECT -- SF-01, SF-02` |
| Mathematical and proof correctness | `40C53864D10863B7140FB4BA8ADCD000A7812CAC41027EDF52317039E6366AC1` | `REJECT -- TH96-MP-01, TH96-MP-02, TH96-MP-03, TH96-MP-04` |
| Adversarial publication and terminology | `1F171521C7C2B7E3FE8F13FFB46EAEF024B8784926ED019FEA5FFE5C322133F7` | `REJECT -- AP-01, AP-02, AP-03` |

The findings reconcile into four substantive repairs and one local terminology
repair:

1. Add Thomas's printed-page-30 finite-union characterization
   \(\bigcup_{j=1}^{k}U_jV_j^\omega\), with regular finite-word factors and an
   explicit infinite-concatenation convention (`SF-01`, `TH96-MP-01`, `AP-01`).
2. Define the empty-successor case of the Safra update as an absorbing rejecting
   determinization state, and prove that it preserves rejection and the stated
   bounds (`TH96-MP-02`).
3. State that predecessor breakpoint marks are cleared and only collapses in
   the current letter update mark the successor state (`TH96-MP-03`).
4. Totalize the partial chain tree automaton with one rejecting sink before the
   game reduction, prove language preservation, and propagate the premise
   through complementation, basis, and S2S (`SF-02`, `TH96-MP-04`, `AP-03`).
5. Remove the premature occurrence of the technical name later introduced with
   its necessity, definition, standing, nonredundancy, and use (`AP-02`).

Round 1 reviewed the actual frozen manuscript LaTeX against Thomas's actual
source PDF. The additional PNG-by-PNG inspection was redundant: those files are
only display derivatives of the source PDF and contributed no independent
evidence. No later round will require them. Later reviewers must read the
actual `.tex` files and consult only the source-PDF pages needed to verify the
claims under review.

No test, harness, checker, repository script, TeX command, build, manuscript
PDF, or rendered-handbook inspection was used.

Status: ROUND 1 CLOSED -- REJECTED; NO ADMISSION.

## Round 2 opened -- 2026-08-23

The five reconciled repairs are frozen under the Round 2 table in
`../charter.md`. Round 2 asks the same narrow admission question on the revised
seven-object snapshot. Three new blind seats must read the actual manuscript
LaTeX, independently recompute all seven identities, consult the actual source
PDF pages supporting their judgments, and dispose of `H01`--`H22` plus
`R2-01`--`R2-05`.

Derived PNG page images are not Round 2 objects, are not required to be
inspected, and have no independent evidentiary standing. No test, harness,
checker, repository script, TeX command, build, manuscript PDF, or
rendered-handbook inspection is authorized.

Status: ROUND 2 OPEN.

## Round 2 reconciliation -- 2026-08-24

All three reports were filed before the chair opened any report. Each seat
independently matched the seven frozen native identities and read the actual
frozen manuscript LaTeX. The filed report identities are:

| Seat | Report SHA-256 | Verdict |
|---|---|---|
| Source fidelity | `DA6C38F518C09F7874265A39A23B8481E2643ED5561A24FC7A3187F4F59AA2F1` | `ACCEPT` |
| Mathematical and proof correctness | `A71665D3F7972DDDD8D33C3CE03F021FB714700ED72FBF0BA611F01168F1CC1B` | `REJECT -- R2-MP-01` |
| Adversarial publication and terminology | `BD99B13B2A78084C8446769E1350EA11ECDDF4E2AB0D0B90A83440A4BB8A05CD` | `REJECT -- R2-AP-01` |

The two must-fix findings are distinct and both are sustained:

1. The deterministic Muller complementation sentence omits Thomas's total
   transition-function premise. With a merely partial functional transition
   relation, a word with no run is rejected both before and after the Muller
   family is flipped (`R2-MP-01`).
2. The determinization-state definition later uses persistent node names and
   one Rabin pair per name without first making injective live-node naming part
   of the state. New siblings created in one update must receive pairwise
   distinct names, not merely names absent from the predecessor tree
   (`R2-AP-01`).

The source-fidelity seat found no independent defect. All five repairs frozen
for Round 2 otherwise passed. The two bounded Thomas report-precursor
presentations remain unadmitted pending repair and a fresh unchanged-hash
review round.

No retained source render, test, harness, checker, repository script, TeX
command, build, manuscript PDF, or rendered-handbook inspection was used.

Status: ROUND 2 CLOSED -- REJECTED; NO ADMISSION.

## Round 3 opened -- 2026-08-24

The two Round 2 repairs are frozen under the Round 3 table in
`../charter.md`. Three fresh blind seats must read the actual manuscript LaTeX,
independently recompute all seven identities, consult the controlling source
PDF only at the pages needed for their source judgments, and dispose of
`H01`--`H22`, `R2-01`--`R2-04`, and `R3-01`--`R3-03`.

Derived PNG page images are inert viewer aids. They are not source or manuscript
review objects, are not to be inspected, and carry no independent evidence. No
test, harness, checker, repository script, TeX command, build, manuscript PDF,
or rendered-handbook inspection is authorized.

Status: ROUND 3 OPEN.

Before any reviewer was assigned, the chair made the frozen records state the
already-open Round 3 status literally rather than by the generic phrase “fresh
round.” This changed only the two record identities. The final pre-dispatch
hashes are the Round 3 table values
`F169CB0936EAA8CB650102A974FEE01F05C3E9D58774F7A198E2CEE35E2A7150`
and
`C45908A389BB22FBB584672F9F78F1C0E45E7DDF274BC37039AEA9BC81ED281F`.
No reviewer saw or reviewed the superseded pre-dispatch identities.

## Round 3 reconciliation -- 2026-08-24

All three reports were filed before the chair opened any report. Each seat
independently matched all seven Round 3 identities, read the actual frozen
manuscript LaTeX, consulted the controlling source PDF itself, inspected no PNG
or derived page render, disposed of every mandated invariant, and reported no
finding.

| Seat | Report SHA-256 | Verdict |
|---|---|---|
| Source fidelity | `5F028511108664941B33E4BDBB1FB5A6CCA1B43FFC33616F7B976A1B7034A53A` | `ACCEPT` |
| Mathematical and proof correctness | `789E9DF877545B81D1D8FB0D0480E622EBF005C0C45EF8814C84F7D59EC96EE9` | `ACCEPT` |
| Adversarial publication and terminology | `3B253D567F9A64B98136B2C936050BEF1B18FA1CFDFFAA451D4D9547804B21F6` | `ACCEPT` |

The unanimous decision admits only the frozen May 1996 report-precursor
manuscript content proposed for `N-c-013.e` and `N-c-014.e`. It does not admit
the registered 1997 chapter, either presentation file overall, `N-c-013` or
`N-c-014` overall, Part IX, another part, a build, rendered-handbook
inspection, human or user review, the final book, or publication.

No test, harness, checker, repository script, TeX command, build, manuscript
PDF, rendered-handbook inspection, or derived page render was used.

Status: ROUND 3 CLOSED -- ACCEPTED AT BOUNDED REPORT-PRECURSOR MANUSCRIPT-CONTENT SCOPE.
