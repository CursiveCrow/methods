# C6.0–C6.1: exact serialization and bounded extraction

Date: 7 September 2026. Root authoring record. This is actual manuscript
development; independent content review and formal admission remain pending.

The preparation note identified an unspecified serialization in the active
bespoke numbering. The present changes complete that convention while
retaining its designated slots, two-sided machine model, numerical input/output
semantics, length-prefixed right-nested Cantor tuple code and invalid-index
divergence convention. They are newly completed in-document conventions;
no external source is claimed to have already supplied these exact fields.

## Serialization now written

handbook/restoration/inherited-07851-08048.tex introduces
def:p04-program-serialization. Its description has state count n, tape-symbol
count b, a fixed-width input-alphabet bitmap A, and the complete ordered list
of five-field transition rows. States and symbols number from zero, with
the existing designated codes. Row direction 0 is left and 1 is right.
There are m=(n-2)b rows and k=3+m description entries. Every nonhalting
key occurs once in lexicographic order, with every field range checked.

The following paragraph gives unique decoding and finite validity checking,
including zero/one-length tuple conventions and why lengths below six are
invalid machine descriptions. The enumeration proof now constructs the
explicit metadata as well as the row list. The renaming proof, universal
simulation sketch and parameter-theorem boundary are retained.

Original whole-file hash:
436DE76199BCD67D4E55252CA92D47A3046701AC028E79484395E5C0EDE6B7B8.
Root-stage hash:
DE01687B7F524F49D6B3E90C9ACD038550F7BE1551A1AABC771B8BBB3B4B0177.

## Bounded extraction and history layout now written

handbook/restoration/inherited-08710-08876.tex introduces the eliminable
arithmetic formulas E and E2 for one- and two-dimensional tagged entries.
Their argument-bound variables are freshly renamed. The complete lemma
proves the numerical bound pair(a,b)<(a+b+1)^2, exact extraction, uniqueness,
value at most s, and finite packing from the existing beta lemma. Each family
has one fixed positional arity, preventing mixed-arity address collisions.
The proof explicitly does not require paired indices themselves to be <=s.

The history definition now has fourteen specified tags and an eleven-field
header. It fixes the alphabet bitmap's tail certificates, canonical binary
input/output, finite tape width W=L+2T+1 and origin H=T, per-configuration
state/head/symbol/prefix/code values, and output length/value fields. Clause
h2 refers to the actual serialized metadata and five-field rows.

Original whole-file hash:
2B00900E80D8D0A97CD6779A632E8821F2A51937164F72238CFEF179FE18934C.
Root-stage hash before C6.2 authoring:
F133F82DF48E6E4556FF07B637452151362770CA0DB4396B3772BD4468EF49C1.

The original pairing and beta proofs in inherited-08439-08709.tex are
unchanged, SHA256
95EB4270559303FEFC5DE2D9BC804A04768EAD87D68D9E5D9CBF65079714806A.

## Verification and exact continuation

Root read the original assigned files, the arithmetic language and P/B
definitions, then read back the new serialization and extraction/history
prefix. The table row terminator and the fixed-arity condition were corrected
during author read-back. No independent mathematical pass, software test,
build, render or provenance migration is claimed.

The new lemma is a lemma environment, preserving the P4 driver's ordinary
theorem-count hooks for the later hierarchy statements. The full Comp theorem
and c.e. characterization remain sketches at this stage. P5 representation
and internal proof-transformations are separate obligations.

C6.2 is the next authoring assignment: literal H1/H2 formulas and complete
canonical-input/exact-table correctness proofs. C6.3–C6.4 still owe every
initial/step/final clause, the complete bounded Comp formula and both
code-to-run/run-to-code directions. C6.5 must verify consumers and update
only proof statuses whose complete obligations have actually been met.
Canonical symbol intake and correction-provenance admission remain open.
