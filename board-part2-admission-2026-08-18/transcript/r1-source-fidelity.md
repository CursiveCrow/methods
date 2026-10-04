# Source-fidelity opening position

- seat: source-fidelity
- round: 1 (blind opening)
- snapshot: current live Part II bytes after the chair's freeze notice on 2026-08-18
- scope discipline: I did not read another seat's transcript. I read the complete reachable graph rooted at `handbook/parts/p02.tex` and `handbook/annex/p02.tex`, including all 50 restoration wrappers and artifacts, every reachable editorial body/annex file, the corresponding provenance and closure records, the calculus sheets reached by those files, and the bibliography records used by their claims.

### F1 [blocker] [open] Seven routed notices expressly say that their reader content is OPEN or unadmitted

- author: source-fidelity r1
- location: `handbook/annex/p02.tex:4-12,27-34`; `handbook/parts/p02/first-order-calculi-supplement.tex:2-10`; `handbook/parts/p02/first-order-completeness-remainder.tex:2-7`; `handbook/parts/p02/first-order-normal-forms-supplement.tex:2-10`; `handbook/parts/p02/first-order-resolution-supplement.tex:2-8`; `handbook/annex/p02/first-order-calculi-supplement.tex:2-7`; `handbook/annex/p02/first-order-completeness-remainder.tex:2-7`; charter I4 and C5.
- claim: Part II cannot be admitted while these blocks remain on the reader route. They do not merely preserve internal workflow comments: they print `OPEN`, `unadmitted`, and `owes` to the reader, and several state that they close no content, review, register, or publication gate.
- evidence: `handbook/annex/p02.tex:4-12` says the historical propositional annex is off route, two old backreferences still lack an exact destination, duality is absent from the restored interval, and later use owes reviewed content. Lines 27-34 then say the routed first-order additions remain explicitly OPEN and unadmitted. Each of the six separately routed supplement notices cited above independently repeats that status. This directly triggers I4 rather than requiring an inference from a control file.
- correction: Review each retained editorial unit on its merits. For every unit accepted by the board, replace only its own OPEN notice with a precise editorial/source attribution and bind its reviewed record; remove any unit the board rejects from the driver. For the historical propositional-annex paragraph at `handbook/annex/p02.tex:4-12`, remove the reader notice if the off-route fragment is formally discarded; if its missing topics are required, first add genuinely reviewed body results and matching annex proofs rather than aliases to retired labels. Do not bulk-delete the notices before the substantive findings below are resolved.
- status: open.

### F2 [blocker] [open] The live Part II route has no admitted provenance or register record

- author: source-fidelity r1
- location: `spec/provenance/SRC-01649-01660.json:39-44,56-75,91-94`; `spec/provenance/SRC-04306-04575.json:53-57,71-90,106-109`; `spec/provenance/SRC-12951-12969.json:40-44,56-75,91-94`; `spec/provenance/reviewed-handbook-unit-records.json:2-5`; `spec/provenance/reviewed-register-obligation-records.json:2-6`; `handbook/parts/p02.tex:3-60`; `handbook/parts/p02.tex:55`; `spec/handbook-unit-inventory.csv:1`; `spec/handbook-construction-snapshot.csv:1`; charter I4-I5 and C1-C5.
- claim: Exact byte restoration has been established, but no current control record establishes independent source/content admission for any of the 50 inherited Part II intervals or for the reachable editorial additions. The current construction snapshot also does not describe the live reader tree.
- evidence: A read-only enumeration of the Part II source ranges found `part2_records=50 open_destinations=50 independent_source_pending=50 all_completeness_pending=50`. The three records cited above show the same schema at the beginning, middle, and end of the route: `handbook_destination.status` is `open/missing`; every completeness dimension is `pending`; independent-source, build, visual, and human-review fields remain pending. Both reviewed-record files contain an empty `records` array. `python tools/check_inherited_restoration.py` passes all 282 corpus records and explicitly limits the result to source/static evidence; all 50 Part II records are among those passes. By contrast, `python tools/check_handbook_construction_snapshot.py` currently fails with `handbook source tree drifted (added=34, changed=69)`. The reachable file `handbook/parts/p02/simple-type-logical-constants.tex`, input at `handbook/parts/p02.tex:55`, has no row in either cited inventory/snapshot CSV.
- correction: After the substantive Part II findings are dispositioned, regenerate the handbook construction snapshot and unit inventory from the final live bytes. Add one hash-bound reviewed-unit record for every reachable inherited/editorial unit and one reviewed-obligation record for every Part II obligation actually discharged, citing the relevant board transcript and its exact review scope. Update each inherited provenance record's destination, independent-source field, and applicable completeness dimensions individually; do not promote build, visual, or user acceptance from this source review, and do not bulk-close an obligation merely because its text exists.
- status: open.

### F3 [blocker] [open] The incidence translation is not defined for every inherited Henkin structure

- author: source-fidelity r1
- location: `handbook/restoration/inherited-12537-12673.tex:4-13`; `handbook/parts/p02/second-and-higher-order-logic-supplement.tex:101-160`; `handbook/annex/p02/higher-order-supplement.tex:63-82`; charter I2-I3 and C2.
- claim: The theorem `thm:p02-sol-incidence-satisfaction` quantifies over every relational Henkin structure, but its target structure can assign a relation-sort constant a value outside that sort's domain. The theorem and its annex proof are therefore undefined on permitted inherited structures.
- evidence: The inherited definition requires only nonempty `\mathcal R_n\subseteq\mathcal P(M^n)` and lets the remaining components interpret nonlogical symbols (`inherited-12537-12673.tex:4-13`); it never requires a predicate constant interpretation `P^\mathcal H` to belong to `\mathcal R_n`. The editorial construction sets the relation-sort domain to `\{S_n\}\times\mathcal R_n` but interprets `\widehat P` by `(S_n,P^\mathcal H)` (`second-and-higher-order-logic-supplement.tex:129-141`). Take a unary language, `M=\{0\}`, `\mathcal R_1=\{\varnothing\}`, and `P^\mathcal H=\{0\}`. This satisfies the inherited definition, while `(S_1,\{0\})` is not in the declared `S_1` domain, so `\mathcal H^\sharp` is not a well-sorted first-order structure. Nevertheless, lines 149-160 assert the satisfaction equivalence for every such `\mathcal H`, and the annex proof at lines 73-76 assumes the missing membership.
- correction: Restrict the construction and satisfaction theorem to relational Henkin structures satisfying `P^\mathcal H\in\mathcal R_n` for every `n`-ary predicate constant, state that hypothesis before `\mathcal H^\sharp` is formed, and use it in the predicate-constant case of the annex proof. Then separately show that every matched comprehension-choice model used downstream has this property (via the eligible comprehension instance defining each predicate constant), or add it explicitly to the matched-model definition. An alternative repair would translate predicate constants directly as object-sort relations rather than relation-sort constants, but the present theorem cannot remain universally quantified as written.
- status: open.

### F4 [must-fix] [open] `Skolem1934` is the wrong primary source for Skolem's paradox

- author: source-fidelity r1
- location: `handbook/parts/p02/first-order-completeness-remainder.tex:56-65`; `handbook/bib/handbook.bib:945-953`; `handbook/bib/handbook.bib:4063-4070`; charter I2 and C4.
- claim: The warning's mathematics is correctly calibrated, and `Hodges1993` is a suitable modern source, but the primary citation `Skolem1934` does not correspond to the historical result being attributed.
- evidence: The local bibliography identifies `Skolem1934` as *Über die Nicht-charakterisierbarkeit der Zahlenreihe mittels endlich oder abzählbar unendlich vieler Aussagen mit ausschliesslich Zahlenvariablen*, Fundamenta Mathematicae 23 (1934), 150-161. The publisher's authoritative record confirms that title, date, and locator: [IMPAN, volume 23 (1934), pp. 150-161](https://www.impan.pl/en/publishing-house/journals-and-series/fundamenta-mathematicae/all/23/0/93125/uber-die-nicht-charakterisierbarkeit-der-zahlenreihe-mittels-endlich-oder-abzahlbar-unendlich-vieler-aussagen-mit-ausschliesslich-zahlenvariablen). By contrast, the Stanford Encyclopedia's historical account says that Skolem obtained the paradox from his first-order set-theory treatment in the 1922 paper and gives the exact title *Einige Bemerkungen zur axiomatischen Begründung der Mengenlehre*: [SEP, “The Emergence of First-Order Logic,” section 9 and bibliography](https://plato.stanford.edu/entries/logic-firstorder-emergence/). Its dedicated entry likewise calls 1922 the paper in which the paradox was first presented: [SEP, “Skolem's Paradox,” sections 2 and 3.1](https://plato.stanford.edu/archives/spr2019/entries/paradox-skolem/). The existing key `Skolem1923` is a work on recursive arithmetic (`handbook.bib:4063-4070`) and is not a substitute.
- correction: Add a verified bibliography entry for Skolem's 1922 *Einige Bemerkungen zur axiomatischen Begründung der Mengenlehre* (or its identified translation in van Heijenoort), replace `Skolem1934` with that key at `first-order-completeness-remainder.tex:64`, and retain `Hodges1993` for the modern internal/external explanation. Keep `Skolem1934` only where the 1934 non-characterizability-of-the-number-sequence paper is actually intended.
- status: open.

### F5 [must-fix] [open] The Hilbert completeness attribution collapses a two-source calculus into Mendelson alone

- author: source-fidelity r1
- location: `handbook/parts/p02/first-order-calculi-supplement.tex:164-173`; `handbook/registry/calculi/hilbert-fol.tex:1-18`; `handbook/bib/handbook.bib:318-323,2866-2875`; charter I2-I3 and C4.
- claim: The comparison table calls soundness and strong completeness external facts from `Mendelson1997` “for this standard presentation,” but the registered presentation is an authored combination whose own source note assigns different components to Mendelson and Kleene.
- evidence: The table's system has primitive `\forall,\exists`, four quantifier schemas `\forall1,\forall2,\exists1,\exists2`, MP, and Gen (`first-order-calculi-supplement.tex:164-169`). The controlling sheet says explicitly that Mendelson supplies schemas A1-A5 and Gen, while the dual existential schemas are “as in Kleene” (`hilbert-fol.tex:1-5`); lines 14-18 then display that combined surface. Mendelson's fourth-edition record is [Google Books](https://books.google.com/books?id=ZO1p4QGspoYC), while the local bibliography separately identifies Kleene's *Introduction to Metamathematics*. Thus `Mendelson1997` alone is not exact authority for the sheet the table describes, even if the combined calculus is sound and complete.
- correction: At the comparison row, cite both `Mendelson1997` and `Kleene1952` and replace “for this standard presentation” with a precise split attribution. Before claiming strong completeness for the combined primitive-existential sheet, either cite a source proving that exact surface or add a short conservative/definitional-extension bridge from Mendelson's A1-A5+Gen presentation to the two displayed existential schemas. Do not treat the registry's source note as a proof of adequacy.
- status: open.

### F6 [must-fix] [open] The simple-type Boolean declaration prints stray symbols and leaves the existential abbreviation under-typed

- author: source-fidelity r1
- location: `handbook/parts/p02.tex:55`; `handbook/parts/p02/simple-type-logical-constants.tex:1-28`; charter I2-I3 and C4.
- claim: The newly routed typed-constant convention fails its own purpose of making every object-language constant and abbreviation well typed.
- evidence: Lines 11-12 contain literal `qquad` rather than the TeX spacing command `\qquad`; in math mode those letters are reader-visible mathematical tokens. Line 13 writes each binary constant as `o\to o\to o` without fixing arrow association at this location. Lines 20-21 introduce `\exists_\alpha(P)` and apply `P` to `x` without declaring `P:\alpha\to o`. This file is separately editorial, so none of these defects is inherited-source content that must be preserved.
- correction: Change the display to `\bottom:o,\qquad \neg:o\to o,\qquad \land,\lor,\to:o\to(o\to o)`, and introduce the abbreviation with the explicit binder “for `P:\alpha\to o`, put `\exists_\alpha(P)\defeq\neg\forall_\alpha(\lambda x{:}\alpha.\neg P x)`.” Preserve the stated left association of term application.
- status: open.

### F7 [must-fix] [open] Required Part II further reading is absent from the reader graph

- author: source-fidelity r1
- location: `spec/registers/apparatus.csv:187`; `spec/register-obligation-closure.csv:513`; `handbook/parts/p02.tex:1-62`; all 118 reachable files from the two Part II roots; charter I4 and C3-C4.
- claim: Apparatus obligation A-186 requires a further-reading section for every part, but the live Part II graph has none and the obligation remains OPEN.
- evidence: `apparatus.csv:187` defines A-186, priority `must`, as “Per-part further reading” drawn from the per-domain shopping lists. Its closure row at `register-obligation-closure.csv:513` is OPEN with all review fields pending. A case-insensitive search through the 118 reachable Part II files found no “Further reading” heading or text. A similarly named section in an unrouted historical/editorial file cannot satisfy a reader-surface requirement.
- correction: Add one separately attributed, source-bearing `Further Reading` section to the live Part II route, grouped at least by propositional logic, first-order logic/model theory, full versus Henkin higher-order semantics, and the variant logics actually presented. Bind A-186 to that exact unit and close it only after source and content review; do not count an off-route file.
- status: open.

### F8 [blocker] [open] The Robinson joint-consistency entry is expressly pointer-only

- author: source-fidelity r1
- location: `handbook/parts/p02/first-order-depth.tex:312-322`; `spec/registers/depth-gaps.csv:23`; `spec/register-obligation-closure.csv:23`; charter I4 and C3.
- claim: The reader text expressly says its Robinson joint-consistency sentence is “only a Part 2 pointer.” That is the exact pointer-only state I4 excludes from an admitted reader section, and the corresponding obligation remains OPEN.
- evidence: Lines 315-321 identify the Part III home, give only a prose synopsis, and say that the current sentence is only a pointer to the Part III theorem. The register defines D-P3-005 as “Robinson joint consistency theorem” with home P3, while the closure row remains OPEN with no evidence records.
- correction: Remove `first-order-depth.tex:315-322` from the admitted Part II depth section and leave D-P3-005 solely at its registered Part III home. If Part II is instead required to carry the result, replace the paragraph with a complete separately attributed theorem statement fixing both theories, their common signature, and the no-separating-sentence condition, plus an honest proof status; then review and bind that new Part II unit before closing any obligation.
- status: open.

## Coverage note

### Cross-cutting checks

- checked clean: The Part II driver routes 50 distinct restoration IDs exactly once, in increasing source order: 39 contiguous intervals cover source lines 1649-6048 and 11 contiguous intervals cover 12249-12969. I found no duplicate routed ID or overlap. `python tools/check_inherited_restoration.py` passed every one of those 50 records (and all 282 corpus records), establishing frozen-source digest, interval digest, and ordered content-token equality. This is source/static evidence only, as the checker itself reports.
- checked clean: Recursive reader-graph traversal reached 118 files. Custom-environment IDs plus ordinary labels had no duplicate and every route-local Part II `ref` consumer resolved. The union of citation commands and `cited=` proof-status authorities contained 59 unique bibliography keys; all 59 exist in `handbook/bib/handbook.bib`.
- checked clean: The accessible high-risk source checks other than F4-F5 supported their concrete claims: arbitrary propositional compactness versus the Boolean Prime Ideal Theorem/Ultrafilter Lemma; Karp's infinitary-completeness boundary and Scott sentences; the finite Herbrand-expansion form; and the cut-free first-order subformula-instance qualification. Variant families were kept distinct rather than presented as aliases.
- not checked: final TeX build, rendered-page inspection, and user/human acceptance. Charter I5 makes those separate gates, and this review did not run a command that writes generated/build output.
- not checked: page-by-page inspection of every closed-access monograph cited by the 59 keys. I checked all local authority roles and all fetchable clauses needed for the findings above, but a key's local existence is not independent confirmation of every page in a copyrighted book. Those remaining independent-source gates are accurately still pending under F2 and cannot be silently promoted by this transcript.

### Lot 1 — propositional syntax, semantics, calculi, metatheory, annex

- checked clean: every reachable inherited artifact and wrapper in source lines 1649-3021; source/artifact byte correspondence; one-route order; the separately routed Hilbert/tableau and compactness-choice supplements; cited-key existence; annex/body identity routing. No altered or duplicated inherited propositional unit was found.
- findings: F1 (reader-visible historical-annex debt), F2 (unadmitted records), and F7 (Part-wide reading apparatus).
- not checked: build/visual/user gates as above.

### Lot 2 — first-order syntax, semantics, calculi, completeness, normal forms, resolution, depth, annex

- checked clean: every reachable inherited artifact and wrapper in source lines 3022-6048; source/artifact byte correspondence and order; separation of inherited rules/proofs from editorial sheets and supplements; all reachable body/annex links and bibliography keys.
- findings: F1, F2, F4, F5, F7, and F8.
- not checked: build/visual/user gates and closed-monograph page-by-page verification as above.

### Lot 3 — second/higher-order logic, variants, translations, proofs, pointers

- checked clean: every reachable inherited artifact and wrapper in source lines 12249-12969; source/artifact byte correspondence and order; full/Henkin semantic separation; many-sorted, free, infinitary, generalized-quantifier, and analytical-hierarchy variant separation; route-local labels and bibliography keys.
- findings: F2, F3, F6, F7, and F8 where the pointer-only invariant crosses lots.
- not checked: build/visual/user gates and closed-monograph page-by-page verification as above.

### Lot 4 — every editorial supplement and every visible OPEN/unadmitted/owed/register claim

- checked clean: every separately routed editorial body and annex file was read in full; the seven reader-visible status blocks were enumerated rather than inferred; comment-only uses of “open” for tableau branches were excluded; the unrouted `generated/audit-p02` comment was not misclassified as reader content.
- findings: F1-F8 collectively. In particular F1 exhausts the explicit reader-visible OPEN/unadmitted/owed blocks found on the current route, while F2, F7, and F8 cover the unresolved admission/register/pointer states relevant to this lot.
- not checked: no build, visual, or user-acceptance status is claimed.
