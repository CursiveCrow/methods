REVISE

# Round-one adversarial publication/AGENTS review: N-c-012.d

## Identity, independence, and method

- Stable reviewer identifier: `/root/mcnaughton_1966_research`.
- Runtime model/version: not exposed by the runtime.
- Seat: adversarial publication and AGENTS compliance.
- Independence: I did not inspect `spec/research/boards/p09-n-c-012d/ledger.md`, `transcript/chair.md`, any other transcript, or any other reviewer's verdict, and I did not contact another reviewer.
- Method boundary: direct visual source reading, mathematical reconstruction, frozen-prose inspection, and SHA-256 identity checks only. I ran no tests, test harnesses, automated checkers, repository scripts, TeX, handbook-PDF inspection, or builds. I edited only this assigned transcript.

## Frozen identities verified before substantive review and immediately before filing

Every charter identity matched both times:

| Frozen object | Verified SHA-256 |
|---|---|
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf` | `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5` |
| `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1982-stoc.pdf` | `1DC63181577204AF299760C0C6B43E8224C7D45F68CB5694148AAF795B851283` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-10-bound-crop.png` | `D12214CC597D9C00AE1F42F0226FA7E99775B6DD0247D17311F906E0A2EE8114` |
| `tmp/pdfs/p09-sistla-clarke-1985/journal-page-13.png` | `27CBA35E2990C37FC867E814E3428DB8CC6A77F1FA4E5F1566E213BE3F7C75E1` |
| `handbook/parts/p09/presentations/n-c-012.tex` | `A4E1059FB5AE5BB577C76B443D05A26BF31F711449C7537B71027F7E72A958CC` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `5F3903C0793116D497B86FB8DC06CE6AF2DE6B8FA71C727D74F10054F8905A14` |
| `handbook/bib/handbook.bib` | `1BD6B33A12449449671505A5EEEAB64C99D0E8A74F3E968C9951FF932B778E95` |
| `spec/research/p09-sistla-clarke-1985-source-note.md` | `CF865B89EA3C6C5DF44E9D900D203441B015AF2977F1F383246C52431FCAB533` |
| `spec/research/p09-source-presentations-lot2-3.md` | `E2012A854194277F8C4CC964872428454B2ADEA3624DEE97536833868E37CCE9` |

## Source-page reading record

I visually read the complete journal facsimile at original image resolution: all seventeen physical pages, printed pp. 733--749, in order. I separately read the enlarged p. 742 exponent crop and the controlling full p. 745 derivative. I visually read the complete conference facsimile at original image resolution: all ten physical pages, printed pp. 159--168, in order. The page images, not OCR or the source note, controlled every source judgment below.

I also read the complete frozen Sistla--Clarke reader subsection (`n-c-012.tex:1851--2247`) with both adjacent presentation boundaries, the relevant shared temporal definitions/method/theorems and complexity-atlas row (`logic-in-computer-science.tex:599--806, 2216--2219`), the complete 758-line source note, the `N-c-012.d` source-presentation record (`p09-source-presentations-lot2-3.md:185--197`), and the complete `SistlaClarke1985` bibliography entry (`handbook.bib:2245--2259`).

## Steel-man of the frozen snapshot

The snapshot already gets most of the difficult scholarship right. It fixes the plural title and author order, preserves journal/conference identity and rights boundaries, gives the journal's inclusive `U`/`S` semantics and existential `R`-truth quantifier, labels the validity clause as handbook reconstruction, separates `L(F,X)` from the atomic-negation-only restricted fragment, preserves the strict/non-strict Lemma 3.3 defect, reads p. 742 as `2^length(f)`, keeps journal `2S(n)` separate from conference `S(n)`, states every-position `U` discharge in Theorem 4.7, preserves the finite/infinite ETL typing and parity conflicts, reconstructs the `Gamma` edges and continuation-set termination mechanism, calibrates proof granularity, and explicitly denies a Sistla--Clarke Buechi construction. The ledger also honestly leaves independent review and larger publication gates open. The findings below are therefore focused source-critical defects, not a rejection of that substantial correct work.

## Findings

### AP-F1 — HIGH — “Ultimately periodic” is used repeatedly without the source's defining clause

- **Locations:** `handbook/parts/p09/presentations/n-c-012.tex:2093--2112, 2192--2201`; `handbook/parts/p09/logic-in-computer-science.tex:781--785, 794--800`; `spec/research/p09-sistla-clarke-1985-source-note.md:442--491, 561--580`.
- **Claim:** The reader, shared method/theorem, and source note all use the technical name “ultimately periodic” before any frozen handbook surface gives its eliminable definition. Bounds on a “starting index” and “period,” equality of source truth sets, and eventuality discharge do not themselves define the underlying periodic structure.
- **Primary evidence:** Immediately before Lemma 4.6, journal p. 742 defines a structure `S=(s,xi)` to be ultimately periodic with starting index `i` and period `m` exactly when `xi(s_k)=xi(s_{k+m})` for every `k>=i`; Lemma 4.6 additionally takes a positive period. Theorem 4.7 then adds the stronger source-truth-set equality and every-position `U`-fulfilment obligations (journal pp. 742--744). The frozen prose starts with the name and the extra theorem obligations but never states the valuation-periodicity clause. A repository-wide search of the frozen handbook surfaces found uses, not a prior definition.
- **Publication harm:** A first-time reader cannot distinguish (i) periodicity of the valuation word, (ii) equality of the formula-relative sets `[s_k]_{S,f}`, and (iii) the stronger obligation-discharge condition. The omission also violates definition-before-use and the five-part name rule, and it leaves “ultimately periodic counterexample” in the automata method formally untyped.
- **Exact correction:** Before the first source theorem use, state: for `p>0`, `S=(s,xi)` is ultimately periodic with starting index `i` and period `p` iff `forall k>=i, xi(s_k)=xi(s_{k+p})`; identify it as a property of an infinite temporal structure, explain that Theorem 4.7 additionally requires formula-relative type equality and pending-until discharge, and use the definition later. In the shared product method, separately define an ultimately periodic counterexample path as a finite prefix followed by infinite repetition of a nonempty product cycle, or explicitly cross-reference an already adequate word-level definition.

### AP-F2 — HIGH — The reader-facing Section 3 proof architecture omits the exact robustness clauses of its load-bearing extraction lemmas

- **Locations:** `handbook/parts/p09/presentations/n-c-012.tex:1985--2007, 2028--2034`; compare `spec/research/p09-sistla-clarke-1985-source-note.md:282--326, 352--364`.
- **Claim:** The prose says Lemma 3.3 selects an acceptable subsequence “preserving all required eventualities,” and says Lemma 3.6 preserves a linear number of next-sensitive positions, but it never gives the quantified preservation properties actually used by Theorems 3.4, 3.5, and 3.7. It also reduces Lemma 3.2 to “once finite prefixes agree” without its exact recurring-range and zero-length hypotheses.
- **Primary evidence:** Journal p. 736 states Lemma 3.2 with equal initial-prefix lengths, pointwise equality along that prefix, an explicit equality of the first valuations for the zero-prefix case, and equality of `range(S)` and `range(T)`. Journal pp. 736--737 state Lemma 3.3 for a negation-normal `L(F,G)` formula true at every point of an acceptable `t`: the output acceptable `u` must work uniformly for every intermediate `W=(w,phi)` with `u` below `w` below `s` and `phi` the restriction of `xi`, at every point of `w` that was present in `t`. The printed `<mu(f)` is defective, while the proof supports `<=mu(f)`. Journal p. 739 gives the analogous uniform-intermediate-supersequence conclusion in Lemma 3.6, with `u` finite, containing the current state, and `length(u)<=length(f)`.
- **Publication harm:** “Preserves eventualities” is not equivalent to preservation of the whole formula at all relevant retained positions under every allowed intermediate supersequence. Without those quantifiers, a reader cannot verify why the pruning step is stable or how the linear witness yields the stated NP upper bounds. This fails the charter's exact Section 3 and first-time-reader criteria even though the strict/non-strict defect itself is well reported.
- **Exact correction:** Add compact displayed statements of Lemmas 3.2, 3.3, and 3.6 with their types, all hypotheses, the intermediate-supersequence quantifiers, restriction of the valuation map, and the points at which satisfaction is preserved. For Lemma 3.3, show the literal printed `<` and the separately labelled proof-supported `<=` repair; do not substitute the corrected bound silently.

### AP-F3 — MEDIUM — The claimed complete conference/journal reconciliation omits the predecessor's printed validity clause

- **Locations:** `handbook/parts/p09/presentations/n-c-012.tex:1959--1968`; `spec/research/p09-sistla-clarke-1985-source-note.md:255--261, 653--690`; the comparison table is specifically `:660--681`.
- **Claim:** The journal-side statement is correct: no standalone formal validity clause is printed on journal pp. 734--735, and the handbook labels its universal clause as reconstruction. But the supposedly complete version reconciliation never records that conference p. 160 *does* print formal satisfiability and validity clauses.
- **Primary evidence:** Conference p. 160 explicitly says that `f` is satisfiable iff some structure and position satisfy it and valid iff every structure and every position satisfy it. Journal pp. 734--735 omit that standalone validity definition. The source-note comparison table claims to list all material mathematical and presentation differences but has no row for this deletion/version boundary.
- **Publication harm:** A reader checking the predecessor can reasonably conclude that the handbook silently imported a conference definition into the journal presentation, despite the current prose's journal-only reconstruction label. The omission weakens both version provenance and the “complete reconciliation” status claim.
- **Exact correction:** Add a conference/journal comparison row: STOC p. 160 prints the existential satisfiability and universal validity clauses; JACM pp. 734--735 do not print a standalone validity clause; the handbook adopts the standard universal interpretation only as an explicit journal-presentation reconstruction. Add one short reader-facing sentence if needed to prevent the predecessor clause from being mistaken for journal text.

### AP-F4 — MEDIUM — A load-bearing journal convention that makes the infinite computation path legal is omitted, and its conference difference is unrecorded

- **Locations:** `handbook/parts/p09/presentations/n-c-012.tex:2049--2058`; `spec/research/p09-sistla-clarke-1985-source-note.md:389--418, 653--690`; `spec/research/p09-source-presentations-lot2-3.md:193--195`.
- **Claim:** The journal reduction assumes that after the deterministic machine enters its accepting or rejecting state, it stays in that state without updating the tape. The current reconstruction describes an infinite cyclic chain of instantaneous descriptions and requires a final description to appear, but omits this totalizing convention. The conference/journal reconciliation also omits the fact that conference p. 164 merely says the machine halts in an accepting or rejecting state, whereas journal p. 741 adds the persistence convention.
- **Primary evidence:** Journal p. 741 expressly states that after entering `V_A` or `V_R`, the machine remains in that state without updating the tape. Conference p. 164 instead says the machine halts on all inputs in `V_A` or `V_R`. The reduction uses an infinite path whose successive descriptions must remain legal after a final description has appeared.
- **Publication harm:** Without the journal convention, the handbook leaves a real gap in how a halting computation extends to the infinite path required by the `R`-structure semantics. Omitting the changed convention also contradicts the source note's claim to complete material reconciliation.
- **Exact correction:** State the journal persistence assumption in the reader's Lemma 4.4 paragraph and explain its role in continuing a legal infinite computation history. Add a comparison-table row distinguishing conference “halts” from journal “remains in the terminal state without tape update”; do not claim that the journal identifies this change as the precise conference error.

### AP-F5 — MEDIUM — “Proof tree”/“derivation tree” is an unnecessary, source-inaccurate technical renaming of `Gamma`

- **Locations:** `handbook/parts/p09/presentations/n-c-012.tex:2177--2186`; `spec/research/p09-sistla-clarke-1985-source-note.md:535--552`; `spec/research/p09-source-presentations-lot2-3.md:195`.
- **Claim:** The reader calls `Gamma(S,j,N_i)` the “source proof tree” and a “labelled proof tree”; the source note and ledger call it a derivation tree. Journal p. 745 calls it simply a “labeled tree.” The added proof/derivation terminology is not needed, is not the source's original term, and is not distinguished from proof-system derivation trees.
- **Primary evidence:** Journal p. 745 defines the root and continuation-production children of the labeled tree `Gamma(S,j,N_i)` and uses its finiteness in Lemma 5.1. It does not call the object a proof tree. Terminal productions are handled by the distinct finite-string condition.
- **Publication harm:** The new name can suggest that `Gamma` is a proof-calculus object rather than the grammar-continuation tree defined by the article. Because “labeled tree” already states the required distinction, the synonym fails the user's necessity and nonredundancy conditions and overstates source terminology.
- **Exact correction:** Use the source's “labelled tree `Gamma(S,j,N_i)`” consistently on the reader, source-note, and ledger surfaces. Retain the exact root/edge definition and the explicit separation from finite terminal productions, but delete “proof tree” and “derivation tree” unless a genuinely necessary new name is introduced with all five required conditions.

### AP-F6 — LOW — The source note's page map assigns the Section 3 structure measures to the wrong printed page

- **Location:** `spec/research/p09-sistla-clarke-1985-source-note.md:119--139`, especially rows `:125--127`.
- **Claim:** The page-map row for printed p. 736 lists `init`, `final`, `range`, and `size`, while those definitions are printed at the bottom of p. 735. Printed p. 736 starts with the lemmas.
- **Primary evidence:** Visual journal p. 735 contains the maximal recurring suffix and all four definitions; p. 736 begins “The following lemmas...” and contains Lemmas 3.1--3.3 through the atomic basis.
- **Publication harm:** The “complete journal page map” is an exact locator artifact used to audit the reconstruction. The one-page displacement frustrates direct verification and violates C8's exact-locator requirement.
- **Exact correction:** Change the p. 735 row to include the Section 3 `final/init/range/size` definitions and remove those definitions from the p. 736 row; leave p. 736 as Lemmas 3.1--3.3 begin.

## Criterion-by-criterion disposition

- **C1 — checked clean.** Journal title, author order, volume/issue/date/pages, DOI, ISSN, receipt history, affiliations, two file objects, separate STOC identity, archive provenance, and conditional rights boundaries all agree with the visually read authorities and frozen records.
- **C2 — checked clean.** Syntax, restricted-fragment standing, inclusive `U`/`S`, distinct state tokens and valuations, total finite `R`-structures, existential path truth, universal counterexample relation, and the explicitly reconstructed journal validity clause are correct.
- **C3 — REVISE (AP-F2).** The measure, acceptable-subsequence definition, printed inequality defect, main theorem bounds/classifications, diamond reduction, and proof-status labels are correct; the reader does not state the load-bearing Lemma 3.2/3.3/3.6 preservation clauses exactly enough for first-time-reader proof audit.
- **C4 — REVISE (AP-F1, AP-F4).** Stuttering boundary, `2S(n)`, closure/count separation, `j>=i` fulfilment, Theorems 4.5--4.7 bounds/obligations, `Ff`, initial-since check, and Savitch are correct; the underlying periodic-structure definition and the terminal-state persistence convention are missing.
- **C5 — REVISE (AP-F5).** ETL grammar typing, disjoint heads, normalization, closure, exact `Gamma` continuation edges, terminal-production separation, Lemmas 5.1--5.2, both fulfilment notions, Theorems 5.3--5.4 bounds/input convention, parity conflict, and continuation-set emptiness are mathematically present; the unnecessary “proof/derivation tree” renaming violates source terminology and the five-part rule.
- **C6 — checked clean.** Every Table I row is preserved; Theorem 4.1 is not misquoted as listing `L(U,X)`; the containment classification and complement passage to universal model checking are valid.
- **C7 — REVISE (AP-F3, AP-F4).** The controlling journal/error boundary, theorem renumbering, `S(n)`/`2S(n)`, and lack of a uniquely identified repair are correct, but two material conference/journal differences are absent from the supposedly complete reconciliation.
- **C8 — REVISE (AP-F3, AP-F6).** Bibliography, hashes, access state, rights boundary, proof-status table, ledger openness, and most locators are correct; the comparison inventory is incomplete and one page-map row is wrong.
- **C9 — REVISE (AP-F1, AP-F2, AP-F5).** Prose is independently worded and generally source-candid, but definition-before-use, first-time-reader proof sufficiency, and strict technical-name compliance are not yet publication-ready.

## Invariant-by-invariant disposition

- **I1:** obeyed; scholarship/prose review only.
- **I2:** obeyed; all nine frozen hashes matched before reading and immediately before filing.
- **I3:** obeyed; every printed journal and conference page was visually read; images controlled.
- **I4:** checked clean; enlarged p. 742 reads `2^length(f)`, and p. 745 controls both ETL defects.
- **I5:** REVISE only for the incomplete reconciliation in AP-F3/AP-F4; no conference theorem or unique repair was otherwise imported.
- **I6:** checked clean; language classes, restricted fragment, inclusive operators, existential truth, table validity, and reconstruction boundary remain distinct.
- **I7:** checked clean; finite measure, acceptable condition, literal strict display, zero/zero basis, proof-supported non-strict bound, and unknown cause are all preserved.
- **I8:** checked clean; journal `2S(n)`, conference `S(n)`, closure versus realized-type count, and inclusive fulfilment endpoint are exact.
- **I9:** REVISE for AP-F1/AP-F4; the bounds, every-periodic-position obligation, `Ff`, initial since, and Savitch are correct, but the base periodicity definition and terminal-history convention are owed.
- **I10:** REVISE for AP-F5 only; all mathematical ETL conditions and printed conflicts are otherwise correct.
- **I11:** checked clean; no proof sketch is inflated and no Buechi proof is attributed to Sistla--Clarke.
- **I12:** REVISE for AP-F1/AP-F5. The mandatory named objects themselves are mostly well typed, but “ultimately periodic” is undefined and “proof/derivation tree” is an unnecessary alias.
- **I13:** obeyed; blind independence preserved.
- **I14:** applied; substantive defects require REVISE without majority reasoning.
- **I15:** checked clean; ledger/source-note status leaves N-c-012.d review and every larger gate open.

## Mandatory round-one dispositions

- **M01 — PASS:** p. 742 and the enlarged crop print `2^length(f)`, not `2^(2 length(f))`; the manuscript and records agree.
- **M02 — PASS on the journal clause, with AP-F3 owed for version reconciliation:** no standalone formal validity clause appears on journal pp. 734--735, and the handbook labels its universal clause as reconstruction. Conference p. 160's contrasting printed clause must be added to the reconciliation.
- **M03 — PASS:** p. 742 requires `j>=i` and a witness in the inclusive interval `i<=l<=j`.
- **M04 — PASS:** the literal `<`, atomic zero/zero basis, proof uses of `<=`, and Theorem 3.4 non-strict result are all correctly disclosed.
- **M05 — PASS:** conference p. 164 prints `S(n)` `X` operators; journal p. 741 prints `2S(n)`.
- **M06 — PASS:** Theorem 4.7 has both exact exponential bounds and every-periodic-position `U` discharge; Theorem 5.3 has exact closure-cardinality bounds and both obligation families at every periodic position.
- **M07 — PASS:** journal p. 745 literally combines finite/infinite strings with unrestricted `l>=0`; the represented-index restriction is explicitly handbook supplied.
- **M08 — PASS:** the exact `N_0 -> a_1 a_2 N_0` example and even/zero-based-odd mismatch are preserved without repair.
- **M09 — PASS mathematically, REVISE terminologically under AP-F5:** the root and every continuation edge of `Gamma` are exact and terminal productions are separated; the source-inaccurate tree synonym must be removed.
- **M10 — PASS:** tree maximum depth/finite termination is distinct from until fulfilment, and continuation sets must become empty within the period.
- **M11 — PASS:** the conclusion identifies neither a precise inference nor one uniquely repairing lemma.
- **M12 — PASS:** proof-status qualifications are accurate and no Sistla--Clarke Buechi construction appears.
- **M13 — PASS:** `L(U) subseteq L(U,X) subseteq L(U,S,X)` gives the stated hardness/upper-bound classification.
- **M14 — PASS:** universal model checking is derived by searching existential truth of the negation and using deterministic polynomial-space closure under complement.
- **M15 — REVISE only for AP-F5:** acceptable subsequence, source truth set, both fulfilled-before obligations, and the grammar-indexed constructor each have necessity, exact definition, standing, nonredundancy, and later use; `Gamma` itself is exactly defined and used, but its added “proof/derivation tree” alias is unnecessary and unsupported.

## Premortem

Assume the topic shipped and later failed scholarly review. The likely failure report would say that the handbook advertised exact source reconstruction while leaving “ultimately periodic” undefined, reducing the decisive Section 3 preservation lemmas to slogans, calling the source's neutral labeled tree a proof tree, and claiming complete conference/journal reconciliation while omitting both the predecessor's explicit validity definition and the journal's persistence convention for terminal machine states. A source checker would then find the page-map displacement immediately. The ordinary checklist would have caught most numerical and theorem defects but could have missed these because each surrounding paragraph is locally polished; the premortem's definition-before-use and version-difference inversion exposed them.

## Narrow closure boundary

This verdict concerns only the frozen round-one N-c-012.d integrated unit. It does not decide Alpern--Schneider, N-c-012 as a whole, Part IX admission, any final publication build, rendered-page inspection, human review, final-book completion, or user acceptance.

REVISE
