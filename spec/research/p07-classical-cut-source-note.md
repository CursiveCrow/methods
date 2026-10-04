# Classical cut elimination: held sources and authoring boundary

Source identification during authoring, 1 October 2026, 23:20 UTC. This
note is not an independent acceptance review of the completed construction.

## Retrieved content

### Gallier, section 6.1, printed p.246 (PDF page 270)

The following is verbatim PDF-extracted text, including its line breaks and
typographical extraction artifacts:

```text
The main result about LK is Gentzen’s cut elimination theorem. An entirely proof-
theoretic argument (involving only algorithmic proof transformation steps) of the cut
elimination can be given, but it is technically rather involved. Rather than giving such a
proof (which can be found in Szabo, 1969, or Kleene, 1952), we will adopt the follow-
ing compromise: We give a rather simple semantic proof of Gentzen’s cut elimination
theorem (using the completeness theorem) for LK, and we give a constructive proof of
the cut elimination for a Gentzen system G1
nnf simpler than LK (by constructive, we
mean that an algorithm for converting a proof into a cut-free proof is actually given).
The sequents of the system G1
nnf are pairs of sets of formulae in negation normal form.
This system is inspired from Schwichtenberg (see Barwise, 1977). The cut elimination
theorem for the system G1nnf
= which includes axioms for equality is also given.
```

### Gallier, section 6.2.2, printed p.250 (PDF page 274), algorithm sentence

```text
Note that the search procedure together with the method indicated in theorem 6.2.1
actually provides an algorithm to construct a cut-free LK-proof from an LK-proof with
cuts.
```

### Zach, section 6, Theorem 10, p.15 (PDF page 15), proof opening

```text
Proof. For a detailed proof, see Theorem 4.1 of Baaz, Ferm¨ uller, and Zach
[1994]. We give a sketch only. As in Gentzen [1934], we observe that th e cut
rule is equivalent to the mix rule,
```

## Supplementary notes

### Held manifestations and extent actually read

- **Gallier:** `source/references/p07-classical-cut-elimination/gallier-logic-for-cs-2015.pdf`,
  2,581,792 bytes, 520 PDF pages. SHA-256:
  `19E1F5F66B7EE973DB1F35A87B4036B063ED60A38894CD321C7EBB06FC53571C`.
  Title and copyright pages identify Jean H. Gallier, *Logic for Computer
  Science: Foundations of Automatic Theorem Proving*, Second Edition,
  Dover Publications, 2015. The copyright page identifies this as the
  unabridged republication of the revised 2003 online edition, originally
  published in 1986, with a new Dover preface. This agrees with the existing
  `Gallier2015` record at `handbook/bib/handbook.bib:1544`, whose author-held
  URL is <https://www.seas.upenn.edu/~jean/Logic-for-CS-2015.pdf>.
  Read: title/copyright (PDF pp.1-2); all of sections 6.1-6.2,
  printed pp.246-251 (PDF pp.270-275); section 6.4 setup and rules,
  printed pp.258-262 (PDF pp.282-286); all of section 6.4.4,
  printed pp.262-269 (PDF pp.286-293). Complete rendered source pages
  246, 250, 259 and 268 were also visually inspected.
- **Zach:** `tmp/pdfs/p07-classical-cut-construction/zach-2021-v2.pdf`,
  381,620 bytes, 42 PDF pages. SHA-256:
  `6BBF2EAADB4EE1232246F4508911FBCF5B9CE3F5D6E9B1F30963DD7A15FC82F1`.
  The first-page version stamp identifies Richard Zach, *Cut Elimination
  and Normalization for Generalized Single and Multi-Conclusion Sequent
  and Natural Deduction Calculi*, `arXiv:2001.00662v2 [math.LO] 31 May 2021`:
  <https://arxiv.org/abs/2001.00662v2>. Read: first page; section 6 through
  Theorem 10 and its conjunction example, pp.15-17; all of section 13,
  pp.38-40. Rendered source pp.15 and 40 were also visually inspected.
  The source-boundary portion of
  `spec/research/p07-classical-cut-construction.md`, lines 1-64, was read;
  its held-PDF hash, version and limited source status agree with this
  inspection. The rest of that construction was not reviewed here.

### Supported attribution and its limits

Gallier supports the statement that he gives a semantic cut-elimination
route for **his LK**, and a constructive treatment for a **separate
set-context NNF calculus**, `G1nnf`. The two treatments must not be
identified. Section 6.2.1, Definition 6.2.1, pp.247-249, has explicit
structural rules, primitive negation, sequence contexts (viewable as
multisets), and `A -> A` axioms. Theorem 6.2.1 and its corollary,
pp.249-250, route an LK proof through soundness, completeness/the procedure
`search`, and conversion of a G proof to LK without cut. Its semantic
dependence does **not** mean it is ineffective or nonalgorithmic: p.250
expressly gives the algorithmic qualification quoted above.

For the separate calculus, Definition 6.4.2, pp.259-260, uses finite sets
of NNF formulas; section 6.4.4 explicitly attributes the simpler induction
to the absence of structural rules. Its constructive locators are the
renaming/substitution lemmas 6.4.3-6.4.4 (pp.263-265), weakening and
inversion lemmas 6.4.5-6.4.6 (pp.265-266), reduction lemma 6.4.7
(pp.266-268), and Theorem 6.4.1 with its proof and depth bound
(pp.268-269). Several subsidiary cases are left as exercises. This
source supports the stated route and its separate calculus, not a claim
that Gallier prints a fully explicit proof for `sheet:lk-defneg` or its
selected-occurrence Mix. No exact-sheet depth bound is imported here.

Zach's Theorem 10 is expressly a sketch for `LX`. Its Mix removes every
occurrence of the mix formula on the designated sides; its left/right
rank counts consecutive branch sequents (p.15), not the construction
note's original-input-height sum. Section 13 gives the generalized
quantifier/clause/resolution mechanism and an eigenvariable-substitution
example (pp.38-40), not a complete case-by-case proof for the exact
defined-negation sheet. Neither passage supplies the full selected-token,
contraction-sensitive, literal-syntax construction by citation alone.
The existing construction note already states this boundary; this note
does not independently certify that construction.

Both version identifications are established by the held source pages;
no network acquisition or byte-for-byte comparison to a currently served
remote copy was needed or performed. No manuscript PDF was inspected, and
no manuscript build, render, test, bibliography edit or rule-sheet edit
was run.

## Completed authoring and integration handoff

The assigned classical author finished the saved draft on 1 October 2026.
The source-reading statements above describe that separate reading pass.
The author changed only the classical body and annex, their dedicated
bibliography/symbol intakes, and this source note. Shared drivers, canonical
records and the rule sheet were not edited.

The exact target is `sheet:lk-defneg`, whose current SHA-256 is
`EABDAA9FC4BAFB3E65CABA406E65E25DAF1FAF9EA916FF42039E2C0BA445267B`.
Its finite multisets, uncontexted identity, contextual bottom-left,
explicit weakening and contraction, shared conjunction-right and
disjunction-left, split implication-left, total capture-avoiding
substitution, and eigenvariable conditions all remain intact. The proof
uses no equality rules or primitive-negation presentation.

The current files supply seven reciprocal body/annex results:

1. Cut-free exact identity between alpha-equivalent representatives.
2. Height-preserving parameter freshening and substitution on auxiliary
   alpha-class proof trees.
3. Cut-free realization with any prescribed literal endsequent
   representatives, without a physical-height preservation claim.
4. Erasure of selected succedent bottom occurrences, with every initial,
   structural, propositional and quantifier case supplied.
5. Full selected-occurrence Mix admissibility, including zero multiplicity,
   unselected equal formulas, selected contraction ancestors, all logical
   commutations and all five principal pairs.
6. Elimination of every Cut and Mix in an arbitrary finite exact proof by
   outer structural recursion and the proved inner Mix construction.
7. Propositional analyticity, the first-order instance/alpha closure, and
   empty-sequent underivability.

The saved substantive construction was retained. The author expanded its
syntax argument: the nearest-binder encoding now proves characterization
of alpha-equivalence, substitution on classes, substitution interchange,
and the exact principal-instance identity constructor by constructor.
The quantified principal cases explicitly choose the new eigenparameter
outside both the matrix variables and its displayed binder. Parameter
substitution now precedes realization in the body as it already did in
the proof dependency order. No same-rank recursive call is made on a
structurally padded or previously constructed proof of uncontrolled
height; all such constructed inputs are used only at smaller formula rank.

The author read the full current body and annex, the saved construction
note, the rule sheet, and the first-order syntax definitions. The focused
format check found seven body results and seven matching annex items,
zero reciprocal failures, seven ordinary annex proof environments,
zero body proof environments, and no sketch statuses. The 13 symbol rows
have no blank required cells and every declared first-use label occurs
in the assigned files. These are authoring and format observations,
not independent mathematical acceptance. No source gap or proof gap
remains in this assigned exact-sheet treatment. Consolidated independent
reviews, reader-route integration, canonical intake merge, build and
publication checks remain with the parent campaign.

### Current artifact hashes

| File | Lines or rows | SHA-256 |
| --- | ---: | --- |
| `handbook/parts/p07/classical-cut-elimination.tex` | 229 lines | `BBF70F36866A3BF1A02B0D9CA68EF3BCA361CEEB4815C338017F8BC6262AF7A3` |
| `handbook/annex/p07/classical-cut-elimination.tex` | 583 lines | `D5C9461045731C2E51B4593F1D507BF38A23EF65863FF66C8DB85CA7B79688FA` |
| `handbook/bib/intake-p07-classical-cut-elimination.bib` | 1 entry | `C27BD9C85716F60BDDC9A13B4EDD8ED61E8DB3C6DA6776E88416D95657576C05` |
| `handbook/registry/symbols-intake-p07-classical-cut-elimination.csv` | 13 data rows | `A6976613BB56B591C543282EF7F7CA7EAB3664FF335399FAE8D5BC75E45DA41A` |

The dedicated bibliography intake adds only `Zach2021GeneralizedV2`.
`Gallier2015` is already canonical and agrees with the held source.
The symbol scope is an explicit body/annex union; the lead can add this
binding to `handbook/registry/symbol-scopes.json` after routing the files:

```json
"P7 classical cut elimination": {
  "presentation": "Exact defined-negation LK selected-occurrence Mix and literal-syntax realization construction",
  "regions": [
    {"anchor": "sec:p07-classical-cut-elimination"},
    {"file": "annex/p07/classical-cut-elimination.tex"}
  ]
}
```

No role override is requested. Formula rank and derivation height retain
their existing typed meanings; the named scope declares their local
parameters and the new occurrence bookkeeping. The complete exact-sheet
construction is authored here; this does not settle distinct source
presentations, quantitative bounds, arbitrary proof-rewrite strong
normalization, equality extensions, or primitive-negation variants.
