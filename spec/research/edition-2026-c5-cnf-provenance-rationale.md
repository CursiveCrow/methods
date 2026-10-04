# C5 CNF interval: precise correction provenance

Date: 7 September 2026. Affected identities: SRC-01946-02186 and D-P2-007.

## Required reader correction

D-P2-007 requires an explicit active route from the P2 normal-form treatment
to the general Tseitin transformation. The active CNF artifact now supplies
that section/theorem link immediately after thm:prop-normal-forms and its proof.
The new reference identifies the satisfiability-preserving fresh-variable
treatment; it does not change the original truth-preserving CNF theorem.

The edition contract authorizes complete reader treatments and direct
correction while preserving the frozen source as evidence. The original
version-1 record is preserved byte for byte under
spec/provenance/history/SRC-01946-02186.v1-e457571c.json, SHA256
e457571c6c4aa33473b0c949e44d496749bb353edcc377c9ff7bd4ac0c5b1d2f.

## Complete observed transformation

The canonical frozen source has 241 lines. The current reader has 244 lines,
SHA256 185c35156f2e1983b1bef028888c3ff2a0dfff333366cff1a3d2769225e37468.
Direct complete comparison finds exactly two operations under the existing
line-ending normalization:

1. Insert four lines at source offset 209. Reader offsets 209–213, half-open,
   contain the three-line forward pointer and its following blank line.
2. Remove the original final blank line: source offsets 240–241, half-open,
   correspond to empty reader offsets 244–244.

Every other line is equal and in order. The second operation is an observed
trailing-blank normalization during the edit and is explicitly recorded;
the transformation is not claimed to preserve every original newline byte.
All original nonblank definitions, statements, proofs and qualifications
remain unchanged. The frozen authority itself was not edited.

The inserted reader lines 210–213 have no original source-line locator.
The following reader line 214 resumes at absolute original source line 2155.
The deleted final blank carries no substantive source unit. The same twelve
source-unit identities 155–166 remain bound by the original evidence.

## Standing

This rationale supports a version-4 candidate corrected-reader record with
full-reconstruction disposition. It does not assert unchanged transcription,
formal source-unit admission or satisfaction of every source-unit review.
All candidate completeness, independent-source, build, visual and human
fields remain pending. Only the prescribed mechanical source/static checks
may pass after the exact record has been validated. C5's separate scoped
text review does not grant the remaining formal or production gates.
