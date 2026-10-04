# P16 three-rule do-calculus soundness: author return

Date: 8 September 2026 UTC. Author block began 09:45:16 UTC;
deadline 10:30:16 UTC. All independent reviews remain deferred under
the user's all-changes-before-reviews instruction. The three manuscript
output paths and the new source-capture directory were verified unused.

## Complete authored component

| File | Extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p16/do-calculus-soundness.tex` | 237 lines; four definitions and seven results | `2FDEBFB8DA5C299510F8913B8C10366CF96B7439636B6D45FC49164463C0F13B` |
| `handbook/annex/p16/do-calculus-soundness.tex` | 388 lines; seven complete proofs | `8EA690E058C93016EEC9CC51231A8A7CD65E8310C441C5857D4C7E6EAB68833C` |

Both actual LaTeX files were read back completely, including every proof
and each subsequent author correction. Only these files, this note, and
the authorized primary capture were added to the manuscript directory.
No old boundary, shared route, registry, bibliography, or review file was edited.

The reciprocal suffixes have body prefix `thm:p16-` and annex prefix
`annex:p16.`:

| Suffix | Complete proof content |
| --- | --- |
| `regime-law` | Finite product outcome space, explicit disturbance-tuple independence, acyclic evaluation, every regime assignment, and exact conditional identification with its simultaneous equation replacements. |
| `regime-graph-bridges` | Full ancestral-moral arguments for action-observation exchange and action deletion. The latter proves the nonancestors of W among Z cannot be ancestors of Y, by taking the last such vertex on a hypothetical directed path. |
| `do-rule-one` | Global Markov in the post-X model, the constant X tuple, positive event inclusion, and division of the conditional product identity. |
| `do-rule-two` | Simultaneous pointwise consistency proves intervention-side support; the two positive regime strata and the first graph bridge prove exchange for arbitrary Z sets, including ancestor-related members. |
| `do-rule-three` | The second graph bridge gives independence from all regime selectors conditional on X and W; the two stated positive regime strata prove action insertion/deletion with the exact ancestor exception. |
| `do-rule-sequence` | Rule 1, Rule 2, Rule 3, Rule 2 sequence on a noisy chain with an independent observation; every graph modification, support event and final probability is calculated. |
| `do-failed-conditions` | All eight masses in a positive-support ancestor-exception countermodel, plus separate undefined-observation and undefined-intervention conditional examples. |

No nondescendant restriction on W is added to Rule 2. Rule 3 uses exactly
`Z(W)=Z\setminus\operatorname{an}_{G_{\overline X}}(W)` and requires both `p_x(w) > 0` and
`p_{x,z}(w) > 0`. Rule 2 requires `p_x(z,w) > 0`; its other denominator
is then positive by consistency. No observational positivity for the
baseline intervention X=x is assumed. All four vertex sets are pairwise
disjoint and may be empty. The original source's check-mark notation is
explicitly related to the handbook's intervention subscripts in the body.

## Primary acquisition and actual reading

The held R-350 overview was searched for the three rule statements; it
does not supply that presentation. The author therefore acquired the
original paper from the verified UCLA author link:
[R-218-B PDF](https://bayes.cs.ucla.edu/R218-B.pdf), listed on
[Pearl's UCLA publications page](https://bayes.cs.ucla.edu/csl_papers.html).
The journal identity and article DOI are also supported by the
[Biometrika article page](https://doi.org/10.1093/biomet/82.4.669).

- Capture: `source/references/pearl-causal-diagrams-1995/pearl-1995-ucla-r218-b.pdf`.
- Identity: Judea Pearl, *Causal diagrams for empirical research*,
  Biometrika 82(4), December 1995. The author-hosted R-218-B file is
  explicitly marked “With Discussions” and spans printed pp. 669-710;
  the journal's main-article DOI record gives pp. 669-688.
- Extent: 42 pages; 3,612,866 bytes; SHA256
  `0A9DD3218E541ACBF26AEFF5865E3C70CB662CD7DE50E1234D016F1AF5DA8927`.
- PDF metadata dates are 2003 creation and 2004 modification. These are
  capture metadata, not the article publication date.
- Complete pages read visually and as text: title p. 669, model and
  separation pp. 671-673, rule context/statements pp. 676-678, and the
  full appendix proof on pp. 686-687. Additional returned text, including
  the source example on p. 679, was read for context. No whole-42-page
  transcription or completeness claim is made.

The page 677 scan clearly prints Rules 1, 2 and 3, and the bar/underline
graph operations were read from the actual images. OCR's second “Rule 1”
is a recognition error, not a source error. The ancestor exception is
printed relative to the incoming-X-deleted graph. The source's 1995 remark
about completeness being open is not presented as current knowledge.

The research and PDF skills guided primary-source reading. Source PNGs
are retained in the old task's `tmp/pdfs/p16-do-calculus-source` directory.
Poppler reported missing display-font aliases on the title render, but the
actual inspected title and mathematical pages were readable. No manuscript
PDF was generated or rendered. The finite fair-bit regime model, both full
moral-graph proofs, support qualifications and examples are handbook
derivations from the stated primary rules and existing foundations.

## Bibliography intake

The key is new and must be merged by root; the author did not alter the
canonical bibliography.

```bibtex
@article{Pearl1995CausalDiagrams,
  author = {Pearl, Judea},
  title = {Causal diagrams for empirical research},
  journaltitle = {Biometrika},
  volume = {82},
  number = {4},
  date = {1995-12},
  pages = {669--688},
  doi = {10.1093/biomet/82.4.669},
  url = {https://bayes.cs.ucla.edu/R218-B.pdf},
  urldate = {2026-09-08},
  note = {Author-hosted R-218-B capture includes discussions through page 710}
}
```

## Integration, dependencies, and notation

Input both files after their matching `front-door-identification`
predecessors, in the existing finite causal chapter, expected scope P16.2.
Root owns the earlier paragraphs that still point forward to do-calculus.

The actual intervention, moral-separation, and global-Markov definitions
and proofs were used; their complete proofs had been read in the preceding
author blocks and the moral bridge was reread here. Root's current boundary
updates were read while preserving those mathematical prerequisites. The
current prerequisite hashes checked in this block are:

- Causal body: `489A65462DC4A3ADD88BE885F10142FC5E3F620044B9AE0E36B7DD464463E3E4`.
- Causal annex: `1393539308C2668996B75AED30D47025F337944E0FC0270E863A153A00794096`.
- Separation body: `B841B541AB248DBBCC2E189B6C4EE6E439A80C83B29A2CB1E6DEE44900D3E7BD`.
- Separation annex: `9B97C4938F35761CA336AE783562B6E02C7F194DCE44056880A33380FAE9FC2A`.

| New or extended glyph family | Typed role |
| --- | --- |
| `\mathcal M`, `X,Y,Z,W`, `x,y,z,w`, `C=X\cup W` | Finite model, four pairwise disjoint vertex sets, their indexed assignments, and the retained graphical conditioning set. |
| `G_{\overline A}`, `G_{\underline B}`, combined subscripts, `K,L,H`, `Z(W)`, local `A,B` | Incoming/outgoing edge deletion, graph and ancestral-set names, exact source ancestor exception, and its partition used in the proof. |
| `p_x`, `p_{x,z}`, `p_x(D)`, `p_x(y\mid z,w)`, `\operatorname{pr}(y\mid\check x,z,w)` | Full and marginal intervention laws, event sums, positive conditional ratios and the source's intervention-marker notation. |
| `F_i`, `\mathcal F_Z`, `F,e,T_e`, `\widetilde K`, `\widetilde V`, `\widetilde\Omega`, `\widetilde{\mathbb P}` | Fresh regime roots, graph vertex set versus random/realized tuples, switched coordinate set, augmented graph, solutions and finite probability space. |
| `2^{-|Z|}`, `r_i(u_i)`, `D\subseteq S_N` | Uniform regime probability using cardinality, old disturbance marginals, and an assignment event. |
| named `A,B,C,D` and `U,Z,W,Y`, `\alpha,\beta`, `a,b,c,d,u` | Locally declared binary vertices, probability functions and outcome values in the worked sequence and countermodels. |

## Author checks and next requirement

The existing file scanner reports no findings, 20 labels, seven statuses,
seven annex items, and seven reciprocal pairs. All four external references
resolve in the actual causal/separation bodies, with no label collisions
there. The new citation remains an integration intake until root merges it.
No tests, independent reviews, admission records or manuscript renders were
created. All assigned finite soundness content is written.

Next, supply a distinct identification algorithm and its termination,
soundness and completeness treatment from acquired primary sources; do not
equate these three sound transformation rules with that further result.
Continuous conditional-kernel and latent-projection presentations likewise
retain their own definitions and obligations.
