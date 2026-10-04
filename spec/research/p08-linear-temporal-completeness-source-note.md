# Linear temporal completeness and decision: authoring record

Date: 1 October 2026. The author owns the assigned body, annex and unique
intakes; root owns the drivers, canonical records, cards and coverage overlay.

## Output and exact claim

- Body: `handbook/parts/p08/linear-temporal-completeness.tex`.
- Annex: `handbook/annex/p08/linear-temporal-completeness.tex`.
- Bibliography intake: `handbook/bib/intake-p08-linear-temporal-completeness.bib`.
- Symbol intake: `handbook/registry/symbols-intake-p08-linear-temporal-completeness.csv`.
- Exact governing calculus: `handbook/registry/calculi/hilbert-ltl.tex`,
  unchanged by this author.

The treatment proves weak theoremhood completeness and finite-premise local
completeness of that seven-rule classical X/non-strict strong-U calculus over
infinite natural-number words. It also proves the failure of compactness for
arbitrary local premise sets. No arbitrary-premise strong-completeness claim
is made. There are 21 reciprocal statement/proof pairs in the completed text.
The author read the actual body and annex, including the saved draft and the
new generalized-acceptance constructions. This is completed authoring, not
independent acceptance, source-unit admission or publication.

## Primary objects and passages actually used

| Version | Exact preserved object | Bytes | SHA-256 |
| --- | --- | ---: | --- |
| Gabbay, Pnueli, Shelah and Stavi, POPL 1980, pp. 163–173 | `tmp/pdfs/p09-gpss-1980/gabbay-pnueli-shelah-stavi-1980.pdf` | 778981 | `2C8FF0E169D2D37B2B402907741AB8FCD67C2883395A4C1655775AB3723A4DA2` |
| Vardi and Wolper, author preprint dated 15 August 1985, associated with LICS 1986 | `tmp/pdfs/p09-vardi-wolper-1986/lics86-ieee-ceda.pdf` | 856275 | `28AC190CA9C03AAC2B045195241DC9D1944669A36A55E5E2E2EBCE68267D64A3` |
| Sistla and Clarke, JACM 32(3), July 1985, pp. 733–749 | `tmp/pdfs/p09-sistla-clarke-1985/sistla-clarke-1985-jacm.pdf` | 6661126 | `F6811D5F3F39A99DC410CE50345BA9DFDE4D433982B09D14BD41270437538CF5` |

The live source sizes and hashes were checked in this block. Primary locators:
[GPSS author archive](https://shelah.logic.at/files/95957/134.pdf),
[IEEE CEDA preprint](https://ieee-ceda.org/files/ieeeceda/2024-03/lics86.pdf), and
[Clarke's CMU journal facsimile](https://www.cs.cmu.edu/~emc/papers/Papers%20In%20Refereed%20Journals/TheComplexityOfPropositionalLinearTemporalLogics.pdf).
The existing full source records remain separate:
`p09-gabbay-pnueli-shelah-stavi-1980-source-note.md`,
`p09-vardi-wolper-1986-source-note.md`, and
`p09-sistla-clarke-1985-source-note.md`.

The author read GPSS's introductory operator clauses and printed pp. 171–172
on DX/DUX, weak completeness, the finite quotient and threading. Saved source
images controlled the mathematics. A bounded source helper checked the strict
endpoints and theoremhood boundary, returned its evidence and stopped without
editing. Its additional check of printed p. 170 confirms that the source's
first-order future quantifiers are inclusive, despite corrupted OCR. That
expressive-completeness theorem is a separate treatment and is not reproved
by this chapter.

The author read the Vardi–Wolper cover, the body introduction to PTL, Appendix
A's future clauses at physical page 16, and Appendix B's complete local,
eventuality, product and projection construction at physical pages 17–18,
printed appendix pp. 2–3. The text derivative contains only form feeds, so
the saved PDF images supplied the source text. The longer author preprint is
not asserted to be the printed ten-page proceedings facsimile. The new
`VardiWolper1985LTLPreprint` intake key identifies the actual body version.

The author read Sistla–Clarke Section 4, printed pp. 740–745: the reduction,
Lemma 4.4's stationary-halting machine encoding, periodic-model preparation,
Theorem 4.7 and the space procedure. The source uses subformula records and
periodic witnesses, not a Büchi translation. Its earlier STOC 1982 version
and regular-operator Section 5 remain separate source obligations.

## Construction and source distinctions

1. GPSS until has a strictly later witness and requires its left operand only
   strictly between endpoints. On natural-number time it becomes next of the
   chapter's non-strict until. The inverse decomposition includes the current
   right-operand case and the current left-operand requirement. The original
   DUX schemas are not renamed into the registered U-unfold/UInd calculus.
2. GPSS Section 3 concerns valid formulas over omega-models and no-premise
   theoremhood. The chapter proves the registered calculus by finite
   characteristic formulas and theorem-only UInd. Finite-premise completeness
   follows by the proved finite conjunction reduction; arbitrary-premise
   compactness is explicitly refuted.
3. Vardi–Wolper Appendix B collects currently true, unwitnessed untils when
   the pending set is empty. A nonempty pending set can lose an obligation
   only when its right operand is currently true. The subset conditions allow
   extra obligations, as in the source; the existence proof chooses the
   minimal allowed batches.
4. Source signed closure types are encoded by subformula truth bits, then
   projected to true atoms in the letter test. The current state describes
   the outgoing transition's current letter, including the first letter.
5. Generalized Büchi acceptance and its counter conversion are additional
   explicitly defined and fully proved finite constructions. They are not
   attributed as the source's printed pending-batch representation. The
   empty accepting list, empty required sets and single-set case are included.
   Reaching the last counter value without last-set membership is insufficient.
6. The deterministic bounded-reachability recursion proves quadratic workspace
   in the state-encoding length. It supplies the polynomial-space upper bound
   directly without invoking an unproved nondeterministic-space conversion.
   It does not promise the explicit graph traversal's time bound.
7. The hardness proof fills the journal's stationary-halting configuration
   idea with a complete clock/cell formula and local update table. It is an
   X/non-strict-U reconstruction, not the literal diamond graph of Figure 2
   or the source's pure-U sketch.
8. Universal checking hardness uses the fully proved valuation-bit block
   translation, including the single fresh start and both until directions.
   The verification product uses syntactic negation of the specification,
   not assumed nondeterministic Büchi complementation.

## Complete statement/proof matrix

| Component | Body label | Annex target |
| --- | --- | --- |
| Strict endpoints | `thm:p08-ltl-strict-bridge` | `annex:p08.ltl.strict-bridge` |
| Registered soundness and suffix validity | `thm:p08-ltl-soundness` | `annex:p08.ltl.soundness` |
| Noncompactness | `thm:p08-ltl-noncompactness` | `annex:p08.ltl.noncompactness` |
| Next Boolean laws | `thm:p08-ltl-next-boolean` | `annex:p08.ltl.next-boolean` |
| Consistent-type partition | `thm:p08-ltl-type-partition` | `annex:p08.ltl.type-partition` |
| Successors and one-step equations | `thm:p08-ltl-successor` | `annex:p08.ltl.successor` |
| UInd finite witness paths | `thm:p08-ltl-eventuality-reach` | `annex:p08.ltl.eventuality-reach` |
| Fair scheduling with positive progress | `thm:p08-ltl-fair-path` | `annex:p08.ltl.fair-path` |
| Full truth lemma | `thm:p08-ltl-fair-truth` | `annex:p08.ltl.fair-truth` |
| Weak and finite-premise completeness | `thm:p08-linear-temporal-completeness` | `annex:p08.ltl.completeness` |
| Both pending-batch directions | `thm:p08-ltl-batch-realization` | `annex:p08.ltl.batch-realization` |
| Both language inclusions and size | `thm:p08-ltl-automaton-language` | `annex:p08.ltl.automaton-language` |
| Generalized acceptance iff realization | `thm:p08-ltl-generalized-realization` | `annex:p08.ltl.generalized-realization` |
| Counter conversion | `thm:p08-ltl-generalized-conversion` | `annex:p08.ltl.generalized-conversion` |
| Single-start conversion | `thm:p08-ltl-single-start` | `annex:p08.ltl.single-start` |
| Positive-cycle/SCC/finite lasso | `thm:p08-ltl-accepting-cycle` | `annex:p08.ltl.accepting-cycle` |
| Counterexample product | `thm:p08-ltl-product-correctness` | `annex:p08.ltl.product-correctness` |
| SCC algorithm and time | `thm:p08-ltl-finite-graph-decision` | `annex:p08.ltl.finite-graph-decision` |
| Deterministic space procedure | `thm:p08-ltl-polynomial-space` | `annex:p08.ltl.polynomial-space` |
| Machine reduction and PSPACE | `thm:p08-ltl-pspace-hardness` | `annex:p08.ltl.pspace-hardness` |
| Block translation and checking PSPACE | `thm:p08-ltl-model-checking-complete` | `annex:p08.ltl.model-checking-complete` |

The proofs include current-point witnesses, zero untils, empty starts, empty
and singleton accepting families, empty required accepting sets, positive
return length and the first encoded valuation. Examples distinguish an
unfulfilled local until loop and an accepting state visited only initially.

## Direct repairs and integration

The body and annex now follow dependency order, with lower bounds after their
upper bounds. The final lookup instructions explicitly negate the formula
for validity and the specification for universal checking. Formula and word
length uses `len`; cardinality bars keep their set-cardinality meaning. The
complete model input length is declared before resource claims. The machine
cell alphabet has separate notation from the automaton transition function.
No editing log was inserted into the reader's derivation.

The intake contains one new bibliography key and 40 symbol rows with math TeX,
`n/a` precedence and actual first-use anchors. Root can bind the named scope
`P8 linear temporal completeness` to the exact body file and
`P8 linear temporal completeness annex` to the exact annex file. Root still
owns routing, merging and the earlier sketched adequacy/card link update.
Use `proved=annex:p08.ltl.completeness` for exact theoremhood adequacy,
`proved=annex:p08.ltl.polynomial-space` for the decision upper bound, and the
separate hardness and model-checking labels above for full classifications.
No change to the seven-rule calculus is required.

No writing component assigned to this future-LTL treatment remains open.
The complete GPSS expressive presentation and original DX/DUX proofs,
past-operator completeness, published-LICS/preprint comparison, regular
operators, determinization/complementation, probabilistic verification and
branching-time treatments remain their respective separate obligations.
This chapter does not discharge them. No manuscript build, render,
independent review, admission or release was performed or claimed here.
