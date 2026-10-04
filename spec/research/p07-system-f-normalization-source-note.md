# System F strong normalization: complete author proof

Date: 9 September 2026. Target:
`thm:p07-system-f-strong-normalization`, for `sheet:system-f`.
This is an authoring record, not independent admission.

## Exact source and required extent

The source used is the author-hosted **2003 web reprint** of Jean-Yves
Girard's *Proofs and Types*, translated and with appendices by Paul Taylor
and Yves Lafont. The held title and copyright pages were read directly.
They identify first publication in 1989, a reprint with minor corrections
in 1990, and the 2003 web reprint. The host locator is
[Paul Taylor's stable PDF](https://www.paultaylor.eu/stable/prot.pdf).

Held file:
`source/references/p07-stlc-normalization/girard-lafont-taylor-prot-online.pdf`.
It has 183 physical pages and SHA256
`909424159082D3F31D190C20B1A9B4DD39355B527BC1C680FB0AA763913F56DC`.
The existing canonical bibliography key `GirardLafontTaylor2003Web` is
used; no new bibliography entry or shared-record change was necessary.

The following required portions were read completely:

| Source portion | Physical pages | Printed pages | Use |
| --- | --- | --- | --- |
| Title and copyright |1–2 |Unnumbered title / ii |Exact manifestation identity |
| Chapter 6 |49–53 |41–45 |CR1–CR3, finite normalization height, arrow candidates, guarded abstraction, substitution fundamental lemma |
| Sections 11.1–11.2 |89–90 |81–82 |Five Church-style term constructors, type abstraction's restriction, type-beta contraction, impredicative instantiation |
| Complete Chapter 14 |121–126 |113–118 |Candidates, quantified interpretation, semantic substitution, universal introduction/elimination, full reducibility statement |

The extracted reading files are under
`tmp/pdfs/p07-system-f-normalization/`:

- `chapter6.txt`: SHA256
  `0212F37147E1BF6CF363E2EA12C2189B8F6A1133E98ED812625DFD58D7650CDD`.
- `chapter11-definitions.txt`: SHA256
  `73398B2BB2030489BC53CCF436FCCB6136D873EAC3B48D504E0F16119D6423E9`.
- `chapter14.txt`: SHA256
  `B35D53F958B6FB10E8F6C2566F741040D658ECDAE955235315CB9E43F0F0236F`.

The source has no diagram or table essential to these proof portions that
requires a separate visual reconstruction. The exact PDF and its formulas
remain the source; extracted text is reading evidence. No manuscript render
was performed.

## Actual manuscript and catalog checked

Read the exact current `handbook/registry/calculi/system-f.tex`, the
System F syntax/reduction/normalization section in
`handbook/parts/p07/lambda-calculi-and-type-theories.tex`, and the lead's
new arrow-only proof in `parts/p07/stlc-metatheory.tex` and its annex.

The covered mathematical declaration is the existing open-term statement
for the combined compatible term-beta/type-beta relation. The relevant
coverage records are `D-P9-004` and `N-c-029`, including
`N-c-029-MAP-01` and `N-c-029-MAP-04`. The four separate source
allocations in `N-c-029` remain distinct. In particular:

- This later presentation does not discharge the separately allocated
  original Girard 1972 presentation.
- The 2003 web reprint does not silently become the exact 1989 edition.
- Reynolds 1974 and Reynolds 1983, relational parametricity, the full
  encoding obligations, and the Curry-style decision problem are not
  declared complete by this normalization proof.

## Proof construction and its explicit adaptation

The source defines candidates among terms of a specified type. The new host
proof defines CR1–CR3 on all raw Church-style terms under the **combined**
reduction relation. This adaptation is identified in the reader text and
matches the raw-term auxiliary convention of the lead's STLC proof.
Candidate membership does not assert typability. The fundamental lemma
relates it to an actual derivation on the existing System F sheet.

The proof retains annotated lambda abstraction, type abstraction and type
application throughout. It neither erases type-beta steps nor replaces the
target by Curry-style, monomorphic or closed-term normalization. Every
syntactic type and every candidate is quantified over in the universal
interpretation. The interpretation recurses on the proper type body with
a changed candidate parameter, rather than recursively interpreting all
potentially larger type instances.

The complete written argument supplies:

1. Capture-avoiding simultaneous type and term substitution, all annotation
   and type-argument actions, and preservation of genuine contractions for
   both beta rules at every position.
2. The finite-copy argument for substitution into a reduced term image,
   including the zero-copy case; finite normalization height from finite
   branching.
3. Type formation substitution, typing type substitution, typing term
   substitution and subject reduction, with every typing constructor and
   both root-redex cases covered.
4. All three candidate properties for SN, the arrow constructor and the
   universal constructor. Variables enter every candidate through the
   neutral-normal case.
5. Candidate-valued interpretation, free-variable independence, bound-type
   renaming and the full semantic type-substitution lemma, including its
   universal case and commuting valuation updates.
6. Both guarded beta-expansion lemmas, enumerating every immediate reduct.
   In particular the normalization of an abstraction body is established
   before induction on its height, rather than presumed.
7. Arrow and universal introduction. Universal introduction obtains body
   normalization by the identity syntactic type instance and the SN
   candidate, then handles every type and candidate.
8. All five typing cases of the simultaneous-substitution fundamental
   lemma. Universal introduction explicitly uses the absence of its
   eigenvariable from **every context type**, together with freshness for
   all inserted images. Universal elimination instantiates at the actual
   substituted syntactic type and the candidate interpreting the original
   instance type.
9. The identity-substitution closing argument for the existing theorem,
   retaining all free term and type variables. Every maximal combined
   reduction ends in a normal term with its original type and contexts.

The worked examples include identity instantiated at its own universal
type, an open reduction at a free type variable, the forbidden
eigenvariable-context example from the source's restriction, and a raw
diverging argument showing why unguarded beta expansion fails. The raw
divergent terms are explicitly not asserted typable in System F.

## Written outputs and integration action

The new body is `handbook/parts/p07/system-f-normalization.tex` (287 lines).
The annex is `handbook/annex/p07/system-f-normalization.tex` (424 lines).
The symbol intake is
`handbook/registry/symbols-intake-p07-system-f-normalization.csv` (20 rows).
All glyphs have inline math wrappers, all display-code cells are nonempty,
and scopes use actual section or annex labels.

There are seven new proved support results and an eighth annex item
closing the **existing** target theorem. The lead still owns its status
and the drivers. Required integration is:

- Route the new body and matching annex once.
- Change the existing target's status to
  `proved=annex:p7.system-f.strong-normalization`; that annex item's
  back-reference is exactly `thm:p07-system-f-strong-normalization`.
- Merge the 20-row unique symbol intake.
- Preserve the separate historical Girard 1972 citation/source obligation
  when changing the old status; the later host proof is not source-version
  acceptance for that original presentation.

The full written body, annex and intake received an author read-through.
The proof cases were checked against the actual constructors and both
reduction rules, including fresh type names in inserted term images and
the identity instance needed to justify universal-abstraction height.
No mathematical branch of the stated host normalization theorem is left
as a sketch or external citation. Confluence remains a separately cited
result and is not used to prove termination.

No independent review, manuscript build, manuscript render or software
test suite was run. Consolidated verification and independent admission
remain with the complete manuscript batch. The exact historical source
obligations described above remain open independently of this host proof.

## Artifact hashes

| Artifact | SHA256 |
| --- | --- |
| Body | `0F5DE52D00A50B020C1E77A8C18F7E53B1CE54338BFFB519AD2E65D01D2B1A33` |
| Annex | `6C7480778F3E00769FA0D4B8368CB81382C1137AFF0E08C951F44EC14FEC24D4` |
| Symbol intake | `11E1DDD5D6798168A24A08667C183AC2A4996D331D18D729445412CBA949ED45` |
