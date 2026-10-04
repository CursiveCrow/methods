# P9 short-production grammar normalization

Separate authoring record. Owned reader, annex and notation intake are new
files. Frozen earlier recombination packets, shared routes, canonical records,
coverage and bibliography remain untouched.

## Objective and result

Closed the exact host proof dependency previously left cited: a finite
effective compiler from an arbitrary finite type-0 grammar to one whose every
production has nonempty left side of length at most two and right side of
length at most two, preserving the exact terminal language including the
empty word. The construction is new handbook mathematics, not credited as an
unchanged reconstruction of the original Kuroda-normal-form argument.

Two reciprocal authoring proof pairs:

- `thm:p09-short-grammar-normalization` /
  `annex:p09.short-grammar-normalization`: ten explicit finite production
  groups; initialization; one active control; cursor motion; consuming
  left-side matching; ordered right-side emission; complete macrostep
  invariant; mismatched/stuck derivations; cleanup; both language inclusions;
  finite effective generation; nonempty-lhs and length bounds; no identities.
- `thm:p09-consuming-universality-short-compiler` /
  `annex:p09.consuming-universality-short-compiler`: exact composition with the
  existing repaired bounded consuming simulation, including fresh alphabets,
  finite rules/support, infinite helper multiplicities, radius-five bound,
  literal terminal filter and empty word.

Normalizing productions does not remove the molecular supply or observation
conditions. The reader states this before universality: genuinely finite
count/weight populations can produce only finitely many words; the universal
representation uses infinite helper multiplicities and accepts through T*.

## Authority and new-construction identity

The bounded-production need is source-grounded in Head, Paun, Pixton,
*Language Theory and Molecular Genetics: Generative Mechanisms Suggested by
DNA Recombination*, Handbook of Formal Languages 2, Theorem 3.6, printed 320,
DOI 10.1007/978-3-662-07675-0_7. Held manifestation is
`source/references/p09-recombination-models/hfl-volume2-institutional.pdf`,
SHA256 CF68AD2A00723DFFA55E8B7D2751B98070AADC240E6A49AE2F91BD49D40242BD.
It identifies a softcover reprint of the hardcover first edition 1997.
The source specifies 1<=|u|<=2, 0<=|v|<=2, u!=v and refers to Kuroda normal
form, but does not supply that normalization proof at this passage. Its
printed 313 Lemma 3.15 begins directly from a type-0 grammar for an RE
language. Printed 298 supplies source family terminology and explicitly uses
equality modulo the empty word; the host compiler instead proves literal
equality. These three passages were re-read as OCR in this block; their
313/320 source pixels had been read in the previous authoring block.

The proof here is a distinct host compiler using fresh coded data letters and
one movable control. Its source-native application target is preserved, but
its Q/E/D compiler symbols are explicitly new, not passed off as the chapter's
notation or original proof. The existing bibliography intake key
`HeadPaunPixton1997RecombinationIntake` is reused; no duplicate bibliography
record is added. No unrelated draft/final source version is substituted.

## Decisive boundary checks in the actual proof

- Q does not appear until the last initialization production, so simulation
  cannot interleave with unfinished initialization.
- All original grammar symbols, including original terminals, are coded as
  nonterminals; only final cleanup emits actual terminal letters.
- Commitment removes Q and no matching state has an exit except matching
  its next actual letter; a wrong match or premature boundary is globally
  stuck, retains a nonterminal, and cannot count as terminal output.
- Emission restores Q only after the complete right side, including the
  zero-length emission case, has been processed.
- Cleanup starts only at the actual left boundary. Encountering a coded
  original nonterminal is permanently stuck; nothing can skip or erase it.
- DR deletion is available only when the entire remaining coded word is
  empty. LQR therefore produces lambda exactly, with no empty-word quotient.
- Movement preserves decoded concatenation; every completed match/emission
  macrostep is one actual original production at its actual selected context.
- Each listed production has lhs length one/two, rhs length zero/one/two,
  and no identity. All names and indices are from finite effective ranges.

These are authoring deductions embodied in the complete proof, not executable
tests or independent reviewer endorsements.

## Integration and residuals

Place this continuation after the computational-expressiveness packet; its
consequence references the existing repaired consuming definition/theorem and
finite-population theorem. The older cited universal statement is historical
source standing; root may add a link to the new host proof without collapsing
the two construction identities. No frozen source proof status was edited.

The exact bounded-production host dependency is now supplied. This does not
close whole chapter ED26-SRC-046-0007 or prove omitted source classification,
consuming obstruction/incomparability, trajectories, later splicing-system
variants or appendix. It does not prove the separate global equivalence of
type-0 grammars and machine-recognizable languages: its RE-language consequence
uses that explicit grammar characterization, already used by the source.

No children, tests, reviews, builds, manuscript renders, canonical merges or
coverage mutations. Files were read back after writing. Root owns final route
and bibliography/notation admission; both reader and annex are off-route here.
