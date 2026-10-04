# Vardi 1982 exact extended abstract: qualification and authoring record

Unit: `ED26-REQ-N-c-004-02`; allocated components `N-c-004-MAP-02` and
`N-c-004-MAP-05`. Authoring date: 1 October 2026 PDT / 2 October UTC.
This is an evidence and correction note, not reader exposition or independent
admission. The Fagin 1974 files are protected and remained unchanged.

## Scope and ownership

Read the exact structured queue row, lot1 lines 501-556, the latest shared
`n-c-004.tex`, relevant actual reader counterparts, and the previously read
handbook/edition/resumed-authoring contracts. The allocated source-specific
treatment is data/expression/combined complexity, Theorem 5, the exact
ordered fixed-point query-capture mechanism and its source syntax, the
input-axis interface and unordered boundary. It is not a wholesale unrelated
book expansion or a substitute Immerman 1986 presentation.

Exclusively owned artifacts:

- `handbook/parts/p09/presentations/n-c-004-02.tex`;
- `handbook/annex/p09/n-c-004-02.tex`;
- `handbook/bib/intake-p09-vardi1982.bib`;
- `handbook/registry/symbols-intake-p09-vardi1982.csv`;
- this note and `source/references/p09-vardi1982/`.

Root owns shared drivers, common text, canonical bibliography/registry and
lookup integration. No children, review wave, manuscript build/render or
prose test suite were run.

## Source identity and direct acquisition

Moshe Y. Vardi, *The Complexity of Relational Query Languages (Extended
Abstract)*, Proceedings of the Fourteenth Annual ACM Symposium on Theory of
Computing, 1982, pp. 137-146, DOI
[10.1145/800070.802186](https://doi.org/10.1145/800070.802186).

The [author publication list](https://www.cs.rice.edu/~vardi/papers/) supplies
the [direct readable PDF](https://www.cs.rice.edu/~vardi/papers/stoc82.pdf).
The page's general boilerplate warns that posted works may be preliminary;
the selected file itself is a ten-page scan with the exact extended-abstract
title, original two-column conference layout, the eleven-theorem text and
original references. Its first page has a handwritten STOC 82 annotation.
It is retained as the identified author-hosted scan of this proceedings
treatment, not asserted byte-identical to an inaccessible publisher download.
No later full version or differently dated article is substituted.

`source/references/p09-vardi1982/stoc82-author.pdf`: 590,025 bytes,
10 physical pages, SHA-256
`cf01452d82dc760a8363361dca3481493c1d72b02b868b5e9828ee26d78a0a89`.
Metadata gives HP 9100C Digital Sender and scan creation 16 September 2001;
that is a digitization date, not a second publication year.

The earlier lot1 claim that the author's Rice URL was dead is stale: direct
download succeeded during this block. The
[author-uploaded ResearchGate record](https://www.researchgate.net/publication/221590198_The_Complexity_of_Relational_Query_Languages_Extended_Abstract)
provided searchable transcription context; no byte identity between its file
and the direct author scan is presumed. The DOI/publisher fetch returned a
403 to this reader, so it is not claimed as the readable body acquired here.

`pdftotext -layout` produced only form feeds and a stray character from this
image-only scan. Its `stoc82-author.layout.txt` is retained as an unusable
extraction attempt and earns no reading credit. All ten physical pages were
rendered for source inspection as `original-page-01.png` through
`original-page-10.png`; these are source inspection images, not manuscript
renders. The rendered scan, not OCR, controlled formula glyphs and grammar.

## Reading extent and source-native content

The complete ten-page scan was visually inspected. The selected dependencies
and allocated treatment are concentrated in the following original locators:

| Original pages | Content read and used |
| --- | --- |
| 137-138, section 1 | Three complexity axes; their different purposes; explicit notice that this version only sketches proofs |
| 138-139, section 2 | Partial query type; standard explicit database encoding; consistency criterion; meaning function; query and expression graphs; D/E completeness with logspace reductions; graph-complexity query classes |
| 139-140, section 3 | F/F-minus, outer binary TF, positive outer YF, existential-relation SF; flight examples and the source's parameter-preserving recursion |
| 141-142, Theorem 5 | Increasing approximation bound; Path System Accessibility data hardness; high-arity binary tableau expression-hardness sketch on fixed B0 |
| 142-143, Remark 2 | SF/NP and ordered YF-plus/P capture; equality conjunction and existential projection qualification; supplied order; EVEN and unordered failure |
| 145, concluding section | TF/YF/SF are not initially logically closed; closed Y is a distinct language; C(Y)=C(YF-plus) attributed to Immerman [Im2] |
| 145-146, references | CH1/CH2 identities; Jones-Laaser and Hartmanis-Stearns external sources; [Im2] is the same-volume 1982 Immerman work, not the later 1986 article |

The algebraic-language sections and remaining results were read for context
and dependencies, but this unit does not claim a newly authored complete
presentation of every algebraic-language theorem in the paper.

## Source standing, reconstructions and corrections

1. **The two Theorem 5 lower bounds are different.** Data hardness cites
   Path System Accessibility. The machine paragraph with rank `2n+m` and
   Boolean time/tape coordinates is expression hardness on the fixed database
   `B0=({0,1},{<1>})`. The common text/lot1's description of that paragraph as
   the data lower-bound tableau must not be reused. The new source-specific
   presentation makes the distinction explicit.
2. **Actual order glyph.** The printed remark displays
   `C(YF-plus,<=)=QPTIME(<=)`, using weak order, not the inherited strict-order
   glyph. The construction defines strict order from this relation as needed.
3. **Actual language boundary.** The initial TF and YF definitions add
   particular outer operators to first-order expressions. The concluding
   section itself explains their lack of logical closure. The draft does not
   substitute full modern nested FO(TC)/FO(LFP) syntax. It retains Y, YF and
   YF-plus separately and reports the p. 145 normal-form identity at its
   actual external-citation standing.
4. **Partial functions versus recognition graphs.** The original query
   definition permits partial functions, and the original class `QC` tests
   `Gr(Q)` alone. The source nevertheless prints `C(SF)=QNPTIME` and
   `C(YF-plus,<=)=QPTIME(<=)`, while its logical expressions define total
   queries. Under literal partial-function equality this cannot hold for
   every partial query: the nowhere-defined partial query has the same empty
   graph as the total constant-empty query, but only the latter is a total
   query definable by such an expression. The active capture statement is
   corrected at its point of use to the total consistent query classes
   `QPTIME_tot` and `QNPTIME_tot`. Equivalently it is graph-recognition capture
   after identifying queries with the same graph. The original unqualified
   printed formula is preserved here as provenance, not left as a false
   theorem followed by reader repair instructions.
5. **Positive tableau reconstruction.** One relation carries all candidate
   query prefixes, time/cell addresses, complete finite cell tokens and flags.
   Minimum/maximum tuples code a finite alphabet even on a two-element
   domain. The input word is explicitly first-order definable from ordered
   relation tables, unary domain markers and candidate-marker blocks.
   Canonical ordered relabeling handles arbitrary long numerical names while
   respecting consistency. A deterministic radius-one local map uses only
   positive predecessor facts. Distinct flags select computation; equality
   selects answer signals, which are existentially projected using the
   literal YF-plus extension. Singleton diagrams are handled directly without
   alphabet-code collisions. Both row soundness and derivability are supplied.
6. **Empty Boolean case.** The paper does not explicitly exclude empty D.
   A true empty-domain Boolean answer cannot be produced by an existential
   projection of a positive-rank tableau. The draft supplies that finite
   case in the closed language Y and uses the paper's explicit p. 145
   `C(Y)=C(YF-plus)` bridge to obtain YF-plus expressibility. This preserves
   the source's cited normal-form dependency; it does not pretend that the
   short YF-plus grammar already contains unrestricted Boolean closure.
7. **EVEN proof attribution.** Vardi cites CH2 for unordered nondefinability.
   The new explanation also supplies the precise embedding into the stronger
   order-free FO(LFP) language and reuses the completed equality-pattern proof
   at `thm:p09-fagin74-unordered-boundary`. No protected Fagin file was edited
   or recredited as Vardi's original proof.

## Proof status and checks

`thm:p09-vardi82-theorem5` is `sketched=`: its annex supplies the actual two
source routes and an explicit path-system operator, but leaves the cited
external PTIME-completeness result and full logspace expression-generation
reduction at their source standing. The source's normal-form dependency
`C(Y)=C(YF-plus)` is also cited, not locally proved. There is no separately
invented full-proof promise for these source-sketched/external results.

`thm:p09-vardi82-iteration` is `proved=`: its annex proves monotonicity, leastness,
the finite stage bound and the changing-exponent upper bounds.
`thm:p09-vardi82-remark2` is `sketched=`: its annex retains the published sketch
status while supplying the detailed positive deterministic construction and
the correctly typed graph/total-query scope.

The author reread both written files. Ephemeral mathematical calculations
confirmed the flight example's second-stage `(a,p,r)` addition without
`(b,p,r)`, and the path-system stages `s`, `s,u`, `s,u,v`, `s,u,v,t`, then
stability for rules `(s,s,u)`, `(s,u,v)`, `(v,u,t)`. These are author checks,
not independent admission or a software test suite. Protected Fagin body and
annex hashes remained respectively
`0fffc5c92dbce59b9c7ef780daa5e2c634f427efc222f64e0e48b7440dc9c662` and
`b0509f1316022c311dcf44308b614c418962a136eef7adca9acfaccdcedd6dab`.

The assigned presentation is written at the accurately declared proof/sketch
scope. Unreproduced external completeness and normal-form proofs remain
explicit dependencies, not mathematical results claimed independently proved.
Root integration, unique intake merging, lookup binding and later consolidated
independent/source/publication/build/render checks remain due. The shared
Vardi paragraph should be updated for Path System data hardness, its weak-order
glyph and the total-query or graph-recognition capture qualification.

## Handoff snapshot

The bibliography intake enriches the existing `Vardi1982` identity rather
than introducing a different version. The symbol intake contains 25 parsed
records with the required CSV header. Reciprocal result/annex pairs are:
`theorem5` (sketched), `iteration` (proved), and `remark2`/`ordered` (sketched),
all under the `p09-vardi82` and `annex:p9.n-c-004.2` prefixes.

| Artifact | SHA-256 |
| --- | --- |
| `handbook/parts/p09/presentations/n-c-004-02.tex` | `4e49b368297e25eaa3e9f6b156f385c0dc628b19fe3694be839971ffc4917f01` |
| `handbook/annex/p09/n-c-004-02.tex` | `bea7944f01adf92eccc511c6c4399f229114faa5a841a49e993e4081fe9713f8` |
| `handbook/bib/intake-p09-vardi1982.bib` | `f159cfe3a1448248c663c0d9ead0a5ec82de8e213682599aa288a5980a4320fd` |
| `handbook/registry/symbols-intake-p09-vardi1982.csv` | `cc9f0eb29d627bc3c29c254b134197df92e55323d36af98afcfad42f0947ccb3` |
