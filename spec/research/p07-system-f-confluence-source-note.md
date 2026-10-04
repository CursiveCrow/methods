# System F confluence and Church-style checking: author proof record

Date: 9 September 2026. Exact existing targets:

- `thm:p07-system-f-confluence`: raw Church-style terms, combined compatible
  term-beta and type-beta reduction, arbitrary finite forks.
- `thm:p07-system-f-church-checking`: the supplied finite explicit judgment
  over the exact contexts and rules of `sheet:system-f`.

This is authoring evidence. Independent admission and final manuscript
verification remain separate.

## Current calculus and existing obligations

Read the current target statements in
`handbook/parts/p07/lambda-calculi-and-type-theories.tex`, the complete
`handbook/registry/calculi/system-f.tex`, and the current substitution
interfaces in the completed `system-f-normalization.tex` body/annex.
The exact calculus has five term constructors, two beta contractions,
no eta rule and no reductions inside types. The distinction between
explicit Church-style checking and erased Curry-style assignment is
preserved. The associated `N-c-029` source allocations were checked;
the original Girard 1989/source-version obligation remains distinct.

The new raw confluence proof uses the earlier **syntactic substitution
identities only**, whose proofs precede the candidate normalization
argument and contain no confluence assumption. It does not invoke the
strong-normalization theorem, even to join a local fork. The checking
proof uses finite syntax, formation and typing inversion; it also does
not invoke term normalization or confluence.

## Primary sources read

**Peter Selinger, Lecture Notes on the Lambda Calculus, arXiv
0804.3434v2, 26 December 2013.** Held file:
`source/references/p07-monotonicity/selinger-2013-v2-lambda-notes.pdf`.
Its first page identifies the exact v2 date. The PDF has 120 pages;
SHA256 is
`9C4AD820D6A48E7D926996F04100830B86F4131BCA0CAB4BF1D6349A2182481F`.
The canonical key `Selinger2013LambdaNotesV2` already exists, with
[the exact arXiv locator](https://arxiv.org/pdf/0804.3434v2).

Read Sections 4.3–4.4 completely, printed/physical pages 30–36, including
the parallel relation, substitution proof, complete-development lemma,
diamond and finite-closure argument. Page 31's joining and counterexample
diagrams were also read visually from the source PDF. The manuscript
supplies its own explicit indexed finite-grid argument instead of leaving
the passage from the diamond to finite confluence to a diagram.

Read the surrounding original source pages 72–79, including complete
Sections 8.1–8.4: explicit polymorphic syntax, Table 6's rules, both beta
contractions and the separate eta conversions, examples, and the
System F confluence/normalization statements. The source explicitly
leaves the System F confluence extension as an exercise. The new manuscript
proof supplies that extension for the **two beta rules actually requested**.
The source's eta rules are not silently added to the book's calculus.

Reading extracts:

- `tmp/pdfs/p07-system-f-confluence/selinger-parallel.txt`, SHA256
  `CAE7D54B801AB5131DA82E5D17283232F55E0DDADF46788AFB6F7B3CC45B14A8`.
  It includes pages 30–37, with the subsequent exercise page retained.
- `tmp/pdfs/p07-system-f-confluence/selinger-system-f.txt`, SHA256
  `168365A575059F7AE995B7E4E0C496318933848ADD5DF5CA92B66DD33F39F413`.
  It includes pages 72–79; material outside the selected syntax and
  reduction portion is not thereby claimed as newly authored coverage.

**Girard, Proofs and Types, 2003 web reprint**, translated and with
appendices by Taylor and Lafont. Held file:
`source/references/p07-stlc-normalization/girard-lafont-taylor-prot-online.pdf`,
183 pages, SHA256
`909424159082D3F31D190C20B1A9B4DD39355B527BC1C680FB0AA763913F56DC`.
The canonical key is `GirardLafontTaylor2003Web`, with
[the author-hosted locator](https://www.paultaylor.eu/stable/prot.pdf).

Read Section 4.1, printed pages 22–23 / physical pages 30–31, in this
block. It states Church–Rosser and explicitly omits its proof. The exact
Sections 11.1–11.2, printed 81–82, were read completely in the preceding
System F proof block, and the same PDF bytes were reverified here. They
supply the source syntax and binding restrictions. A later web presentation
does not establish identity with the exact original 1989 manifestation.

A search also identified the Takahashi 1995 parallel-reduction paper, but
its body was not used or claimed read; no new citation or source-completion
credit is assigned to it. The complete available Selinger derivation is
the explicit methodological source for this host proof.

## Complete written proof components

1. Define the seven-clause auxiliary parallel relation directly on raw
   annotated terms modulo alpha-renaming. Its constructor congruences
   and two parallel root contractions are distinct; transitivity is not
   built into a single parallel step.
2. Prove reflexivity and both inclusions between ordinary and parallel
   reduction, including every congruence position and both root rules.
3. Prove type-substitution stability and the parallel term-substitution
   lemma by every parallel-derivation case. The two composition identities
   explicitly include the mixed type/term case and the freshness needed
   for inserted term images.
4. Define complete development by the **original** function constructor.
   It is well defined modulo alpha-renaming and retains newly created
   head redexes where the original head was not an abstraction.
5. Prove every parallel reduct reaches that development. Each term/type
   application is split into a retained original root, a contracted
   original root, or absence of such an original root. The premise
   inductions and substitution lemmas cover all nested, duplicated,
   erased, disjoint and mixed reductions.
6. Give the finite rectangular diamond argument, including zero-length
   paths, to prove the exact raw confluence theorem. Derive uniqueness
   of a normal form when one exists without assuming normalization.
7. Specify finite variable encodings, context validation, formation,
   capture-avoiding type substitution and a bound-index/free-name alpha
   comparison; prove termination and correctness of these operations.
8. Specify all five syntax-directed synthesis cases, explicit rejection
   conditions and freshening of bound names without altering free context
   declarations. Prove termination, soundness, completeness, output
   formation and uniqueness of the synthesized type by every constructor.
9. Decide the exact proposed judgment by synthesis followed by alpha
   comparison with its supplied result type. No implicit instantiation,
   missing-annotation search or Curry-style inference is introduced.

The examples display both mixed nesting orders and the precise substitution
identities that join them. The checker examples distinguish `f[b] z` from
`f z` and distinguish a free type name from a bound quantifier index.

The complete new body, annex and symbol intake received an author
read-through. The relation inclusions, fresh binder conditions, both
root-overlap branches and every synthesis case were checked directly
against the current syntax. No proof case is left as an exercise, sketch
or external citation. The source-reading PDF workflow was used for
the source's diagram, not for manuscript output review.

## Integration handoff

The new body is
`handbook/parts/p07/system-f-confluence-and-checking.tex` (254 lines).
Its annex is
`handbook/annex/p07/system-f-confluence-and-checking.tex` (355 lines).
The six-row unique symbol intake is
`handbook/registry/symbols-intake-p07-system-f-confluence.csv`.
Every glyph is in inline math, each display-code cell is populated, and
all scopes are actual section or annex labels. Existing canonical
bibliography keys suffice; no bibliography intake is needed.

The five new support results have reciprocal proof items. Two additional
annex items point to the existing targets, whose old status/driver files
remain owned by the lead. Required updates after integration are:

- Existing confluence status:
  `proved=annex:p7.system-f.confluence`.
- Existing Church-style checking status:
  `proved=annex:p7.system-f.church-checking`.
- Route this body and annex once; merge the six-row symbol intake.
- Keep the separately allocated exact historical presentations visible
  when replacing the old cited-only status.

No mathematical branch of these two host theorems remains unfinished.
Historical source-version acceptance, other System F coverage components,
consolidated independent review and final manuscript build/output checks
remain separate. No independent review, manuscript build, manuscript
render or prose-mirroring test suite was run in this block.

## Artifact hashes

| Artifact | SHA256 |
| --- | --- |
| Body | `51445CA6D5DAECA0DE53E003089635825BC15B4ACD99DE6259516B1ECBC573A8` |
| Annex | `707AF69B9A45B4C3E95E6EE32A0960CE5995DB46E70EEE30879AB8D913E2E4CA` |
| Symbol intake | `1E768FCFE47DEDE3FA575B7D3A362352CA13CC159E83D09FF89554E218E8E4FB` |
