# Part IV local interpreter, specialization and recursion completion — 26 October 2026

## Reader delivery

Extended the already-routed body and annex `universal-reductions-supplement.tex` with four new reciprocal proof pairs: counter-compilation, local-universal, local-parameter and local-recursion (body prefix `thm:p04-`; annex prefix `annex:p04.local.`). This fills the actual omissions in the active inherited `thm:universal-computation`, `thm:parameter` and `thm:recursion-theorem`. The retained unreachable combined drafts and every restoration artifact remain byte-identical. Inherited historical status strings were not promoted; the native completion statements have their own complete proofs.

The counter compiler supplies finite-state scan/shift templates, L/R-only moves, a single-tape representation, binary I/O, full-row completion, designated-slot renaming and exact local serialization. The interpreter validates the supplied code, stores variable finite lists in fixed counters, simulates arbitrary two-sided finite-support tapes, and implements invalid/reject/invalid-output divergence. The specialization compiler is total even for invalid target indices; it preserves the right-nested arity coding. The recursion proof supplies the general index-self-reference result, the total index-transformation corollary, and the exact intermediate transformation omitted by the inherited sketch.

## Held source and attribution

Read Kleene, *Introduction to Metamathematics*, 1952 text in held 1974 reprint, `source/references/acq-r1-ACQ-2026-10-0230/kleene-1952-introduction-to-metamathematics-1974-reprint.pdf`. Relevant printed pages 340–342 (physical 350–352), §65 Theorems XXII–XXIII, state the equation-code enumeration and parameter operations. Printed pages 348–354 (physical 358–364), §66, distinguish Theorem XXVI's least functional fixed point from Theorem XXVII's index self-reference. Read the relevant text, including the latter proof at printed353; nearby source context through printed355 was also checked. The local single-tape compiler is an authored construction, not attributed to Kleene's equation coding. Existing canonical key `Kleene1952` is used; no new bibliography record or source-version conflation is needed.

## Verification standing

Authored and locally checked, not independently admitted. Proof reciprocity, source locators and a scoped LaTeX fixture are checked separately; final results are recorded in task artifacts. No statement that the entire Part IV source obligation is complete follows from this addition. Native proof manifests and canonical notation intake still require the root integration pass.

## Final local build and inspection

The `p04-proof-check` fixture compiles with pdflatex and Biber to 23 pages, including the actual machine and partial-recursion prerequisites. All three cited keys resolve and all references resolve. The newly authored body and annex pages were rendered and inspected; a page-space guard keeps the counter-compilation lemma together, and the interpreter's new overfull line was corrected. Three remaining overfull boxes belong to the included pre-existing normal-form/renaming/enumeration text, not these additions. The fixture's standalone annex counter presentation is not the final book's numbering.

All four new theorem/annex pairs and the retained range bridge are reciprocal and environment-balanced. The 12-row dedicated intake passes local CSV/math-span/label checks; canonical hierarchy and collision checks remain the integration step. The source and proof checks are author verification, not independent acceptance. No executable implementation of the entire compiler is claimed: the complete construction is given by finite transition templates and invariants in the proof.
