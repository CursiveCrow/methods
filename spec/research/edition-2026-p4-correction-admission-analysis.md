# Edition 2026 P4: correction provenance and admission compatibility

Read-only investigation, 7 September 2026, 15:21 UTC. No manuscript, code,
schema, canonical registry, generated view or existing provenance record was
changed. This note proposes a bounded compatibility change; it is not an
implemented or reviewed admission mechanism.

## Finding: no existing supported record does this truthfully

The current correction policy permits and requires direct repairs in the
active reader text while preserving the frozen source artifact.
The exact-capture machinery still implements the older, narrower contract.

- [check_inherited_restoration.py:1272–1325](C:/Dev/the-methods-of-reason/tools/check_inherited_restoration.py:1272) accepts record versions 1, 2 and 3. Versions 2 and 3 are reserved for closed reader-part and appendix-layout cases. All three unconditionally call validate_restoration_artifact.
- [validate_restoration_artifact:904–965](C:/Dev/the-methods-of-reason/tools/check_inherited_restoration.py:904) requires the live artifact's recorded bytes/hash, a physical line count equal to the frozen interval length, one shared canonical-content digest, and equality of every non-line-ending byte. Choosing the already listed disposition “full reconstruction” does not bypass these equalities.
- [validate_statuses:1002–1035](C:/Dev/the-methods-of-reason/tools/check_inherited_restoration.py:1002) is explicitly construction-stage validation: completeness stays pending; source/static record this mechanical check; independent/build/visual fields stay pending. It does not grant final admission.
- [check.py:729–769](C:/Dev/the-methods-of-reason/tools/check.py:729) catches any record-validation failure and withholds authorization for that wrapper's artifact. Its later scan at lines 1623–1634 then treats the source-only syntax/results as unauthorized. This describes the static checker's scope classification; it does not mean the TeX wrapper itself has disappeared.
- The alternative branch at check.py:771–816 retains an **exact** non-executed source artifact and names a different reconstructed destination. It still calls the exact validator and cannot legalize changed reader bytes at the same path.

The two latest records still declare “full transcription”: SRC-07295-07468
pins a 174-line artifact but the corrected reader file has 217 lines;
SRC-11711-11740 pins 30 lines but its reader file has 57. Even corrections
preserving line count fail the token comparison. Updating hashes or counts
alone is therefore neither sufficient nor an acceptable repair.

Final source-unit admission is another independent barrier:

- [reviewed-source-unit-records.schema.json:286–301](C:/Dev/the-methods-of-reason/spec/provenance/reviewed-source-unit-records.schema.json:286) permits only open/missing or full transcription, with pending/unclassified, full-and-accurate or layout-only relocation results.
- [build_source_unit_audit_crosswalk.py:663–680](C:/Dev/the-methods-of-reason/tools/build_source_unit_audit_crosswalk.py:663) revalidates the restoration record and demands its full-transcription disposition. Its terminal checks at lines 1233–1242 require all completeness/review evidence.
- [check_terminal_readiness.py:554–560](C:/Dev/the-methods-of-reason/tools/check_terminal_readiness.py:554) again counts only full transcription paired with one of the two exact/layout passing results.

A separately admitted new-proof packet can document that proof, but it does
not by itself close the original inherited-unit gate. Nor can semantic edits
be called layout-only relocation.

## Minimum explicit change

Add one closed corrected-reader case to the existing restoration checker,
for example record version 4 with a required reader_correction object.
Do not alter the exact-token or line-count invariants for versions 1–3.

Reuse the existing source authority, source locator, source-unit IDs,
destination, live-artifact digest and wrapper identity fields. The additional
object should contain only what distinguishes an authorized correction:

1. A stable correction ID and exact affected requirement/source-unit identities.
2. The controlling correction-policy path, hash and clause, plus the concrete correction-reason/proof note and its hash. Preserve the previous provenance record as historical evidence instead of pretending it already described the new bytes.
3. The frozen interval's canonical-content hash, separate from the current reader artifact's hash.
4. An ordered edit map between the frozen interval and current reader lines. Each edit has exact old/new ranges, old/new slice hashes, a reason and its affected identities. Use explicit half-open ranges or an equally precise insertion convention.
5. Existing scoped review-evidence links where available, with their actual status and scope. Their presence is not an automatic six-gate pass.

The checker must replay the complete transformation from the frozen interval:
all unchanged spans match exactly; each changed span matches its recorded
replacement; edits do not overlap or escape the interval; and there are no
unexplained insertions, deletions or reorderings. The current artifact's raw
bytes, UTF-8 standing and hash must also match. Its physical length can differ
from the source only in this explicit correction case.

The existing “full reconstruction” disposition can be reused **only when
paired with this validated correction case**, with an explicit corrected-source
presentation identity and comparison rule. It must not claim the old equality
rule succeeded. This needs a distinct terminal audit result, such as
“corrected-and-verified”, in the source-unit record schema and generator.
The exact spelling is an implementation choice; its meaning must be different
from unchanged transcription or layout-only relocation.

The existing restoration-record path/hash can bind the entire correction
record, so a parallel correction-admission framework is unnecessary.
Extend the generator's permitted-disposition/result pairing and the terminal
predicate to recognize that exact validated pair, under the **same complete
six-gate requirements**. A generic “full reconstruction” string without the
correction record must remain insufficient.

The scope checker can keep its existing one-wrapper/one-input interface.
After the new branch validates, it may authorize that exact corrected artifact
for retained source syntax. Record the authorization kind so downstream
consumers do not call it an exact capture. Retain wrapper identity, one-time
reachability, duplicate rejection and all ordinary reference/rule checks.

## Construction validation comes before formal admission

This separation is essential and already exists for exact captures.

1. Prepare the corrected-reader provenance record with truthful pending review/publication standing.
2. Validate its authority, artifact, edit map, identities and wrapper mechanically. This gives **candidate construction/syntax authorization**, not mathematical or source-fidelity acceptance.
3. Run scoped static checks, builds, source/text reviews and output inspection on that now well-defined candidate. Independent findings and any repairs retain their exact hashes and scopes.
4. Admit the corrected source unit only after every required completeness dimension, exact correction review and all six gates pass.

The correction record must not require final build/visual acceptance before
it can grant construction-time syntax scope. That would create a cycle.
Conversely, granting syntax scope must not set independent review, source-unit
admission, register closure or publication readiness to pass.

The current corrected content stays OPEN until those later gates pass.
Unknown reviewer metadata or a missing current output review does not justify
undoing the correction or falsely labelling it exact.

## Other consumers that require the correction distinction

The minimum change is not confined to the first stale-hash error.

- The source-unit generator's full-transcription-only checks and schema conditionals must agree with the terminal predicate. Otherwise strict syntax can pass while final admission remains impossible.
- Original source ordinals and ranges stay frozen. Corrected reader coordinates are separate; added proof lines are not assigned invented original-source line numbers.
- [audit_tables.source_line:88–93](C:/Dev/the-methods-of-reason/tools/audit_tables.py:88) currently assumes source_start + local_line - 1. Its use at lines 236–249 is wrong after inserted/deleted reader lines. For corrected files, use the validated edit/source map for unchanged spans and explicit current correction metadata for changed units. Do not generate source locators from the old offset arithmetic.
- The deferred inherited-reference rule at [check.py:1364–1379](C:/Dev/the-methods-of-reason/tools/check.py:1364) should remain available only for genuinely retained original reference occurrences. Newly authored correction references must resolve or receive their own explicit obligation, rather than inherit an automatic source-future exception.
- The volume checker and terminal interval checker already call validate_record. They should consume the new validated case without weakening their independent route and frozen-authority checks.

## Canonical notation and generated views: sequencing without a cycle

The current canonical symbols file is data, while the active generated views
are downstream presentation artifacts. In particular, symbols2tex.py
read_rows/collision_check validate field grammar and overlap, but do not prove
the roles semantically correct or check packet admission. Its main function
renders every input row; a successful invocation is not an admission decision.

Use the existing workflow in this order:

1. Prepare the narrowly scoped notation correction and source-role justification in the permitted intake/authoring workflow. Preserve genuine local roles, including propositional formula equivalence, instead of rewriting source notation to satisfy an obsolete global reservation.
2. Merge the intended canonical data as a **construction edit**, with its formal standing still OPEN. Freeze the actual canonical rows/file and the maintained explanatory entry text that the packet covers. Preserve existing symbol anchors; the renderer currently derives them from CSV line numbers, so arbitrary mid-file insertions would change later anchors.
3. Obtain packet-local source/text/static/build/visual evidence using the frozen data and real dependencies. Internal construction previews may use the existing explicit CSV/output-path interface; they are not promoted active lookup surfaces or final publication evidence. Pending full-book view freshness is not misreported as passing.
4. After admission, generate active symbol views from the same frozen admitted input projection. Do not mutate the upstream canonical data while generating. If some rows to be emitted remain unadmitted, the existing unrestricted renderer is not authority to promote them: complete their admission first, or keep the default-output promotion blocked. Do not silently delete owed notation to make the projection look complete.
5. Validate the regenerated lookup presentation and finally the integrated book. Final pagination, link or display repairs have their own affected output checks; an underlying notation/content change reopens its affected admission and dependent views.

Neither canonical content nor its packet/admission record should embed the
final generated-book PDF or terminal-readiness hash as a prerequisite for
lookup generation. The final record binds those downstream artifacts after
they exist. This uses the existing packet-local then whole-book sequencing,
not a waived build/visual gate.

## Required acceptance and rejection cases

| Case | Required outcome |
|---|---|
| An unchanged version-1/2/3 capture | Existing byte/token and line-count checks remain unchanged. |
| A modified capture with only refreshed bytes/hash fields | Reject; no correction map or authorization exists. |
| Same-line-count mathematical correction | Exact capture rejects it; the explicit correction case may validate only after complete edit replay. |
| A valid changed-length correction | Candidate source syntax may be authorized while all independent/admission/output gates remain pending. |
| A one-byte later edit to the corrected reader file | Reject stale artifact/map/evidence bindings. |
| An unexplained additional edit, overlapping ranges or wrong source interval | Reject. |
| A correction described as layout-only or full transcription | Reject the false disposition. |
| A second wrapper, wrong artifact path, or unscoped source syntax | Preserve the current rejection. |
| Three scoped text reviews but missing build/visual or model-version evidence | Preserve source/text evidence; keep full formal admission OPEN. |
| Generated symbols from a stale or unadmitted input projection | Do not grant active-view or publication acceptance. |
| Unchanged admitted input, regenerated views, then current final output checks | No digest cycle; final acceptance proceeds through the existing gates. |

These are cases for small changes to the existing restoration/scope/source-unit
tests if implementation is authorized, not a request for a new audit or test
framework.

## Actual model/version visibility

The existing [source review](C:/Dev/the-methods-of-reason/spec/verification/edition-2026-c3-c4-c5-source-review.md:4)
records that its actual model identifier and reasoning configuration were not
exposed. The [publication-text review](C:/Dev/the-methods-of-reason/spec/verification/edition-2026-c3-c4-c5-publication-text-review.md:25)
also records the runtime version and deployment configuration as unavailable.

The source-unit schema requires actual model/model_version fields, exact
instructions, consulted authorities, findings and a declaration of review
independence. A model catalog, alias, inferred parent model or the word
“unavailable” must not be substituted as an attested backend version merely
because a string validator would accept it.

Keep the present reviews as their honest scoped evidence. If the execution
system can supply the actual logged identifiers, attach that verifiable
metadata. Otherwise the formal metadata condition remains OPEN pending an
observable review configuration or an explicit user decision about the required
recording standard. Construction can continue without fabricating acceptance.

## Current affected-file snapshot

All eight currently use version-1 provenance and claim the exact-transcription
construction mode. Their current reader lengths and hashes are:

| Reader file | Recorded lines | Actual lines | Current SHA256 |
|---|---:|---:|---|
| handbook/restoration/inherited-07295-07468.tex | 174 | 217 | 1958B3363DCAC80B5C7AF56F446E74591B4249D23C1C8543CC9EC7DE7BB93A89 |
| handbook/restoration/inherited-11711-11740.tex | 30 | 57 | 35225299698968B229674BDF96987D1FBDE59DCECB15659C4615F18B27679C08 |
| handbook/restoration/inherited-10675-10769.tex | 95 | 104 | B745B19A1B07592A4CD59FEC1791B3102E88B3C53E30F276C06CA168EBC1D57A |
| handbook/restoration/inherited-11104-11126.tex | 23 | 23 | FC5C0DFCA658CA116D180DB210EA02AD12445A628B6F1E805386E2C461464956 |
| handbook/restoration/inherited-11127-11199.tex | 73 | 73 | 410062CE1D18F96FF5A58E317052FBBBF64FBA1D7A145A44159A4D1A0DF60052 |
| handbook/restoration/inherited-11914-11960.tex | 47 | 65 | 2D8EB98F583C9DEB327252DF70B2DBBFD36F949D6237E1817873FDF9AEAC4302 |
| handbook/restoration/inherited-13519-13551.tex | 33 | 32 | F2142F552BDA2969628D21F60AD90BAAF70163E8C478C31021E4D2F95D77E3C3 |
| handbook/restoration/inherited-13972-14000.tex | 29 | 34 | 79AC085C09DD1F0CEDA5A1E34A3D46ECA61C5786FCAB0926CFFE5BF82DDECC88 |

No proposed record or code change was implemented, and no strict check, build,
render, source acquisition or test suite was run during this investigation.

