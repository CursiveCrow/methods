# Round 2 — independent source-fidelity verification

- seat: source-fidelity
- independence: I reread only the charter, my own r1 transcript, and the current live Part III graph. I did not read another seat transcript or a chair/ledger digest.
- scope: r1 F1-F6; every newly changed reader unit in `classification-theory.tex`, `finite-model-theory.tex`, `preservation-abstract-logic.tex`, `further-reading.tex`; route/supplement changes; new bibliography records and their authority roles
- boundary: read-only source/content verification; no build, test construction, manuscript/control/generated edit, human review, or user acceptance

### F1 — still-open

- repaired portions: `handbook/parts/p03/maps-elementarity-supplement.tex:2-50` now presents the model-symbol table as an ordinary separately authored lookup and removes the printed A-162/OPEN language. `handbook/annex/p03.tex:1-3` no longer routes the old QE/R-030 annex file, so that off-route file's OPEN text is not reader-visible.
- residual evidence: The live types body still prints `D-P4-003`, `D-P4-004`, `OPEN`, and `unadmitted` at `handbook/parts/p03/types-ultraproducts-supplement.tex:4-8`; its routed proof still prints `D-P4-004` and “does not admit or close” at `handbook/annex/p03/types-ultraproducts-supplement.tex:2-4`. The QE body still prints a bold OPEN notice and `unadmitted` at `handbook/parts/p03/qe-categoricity-games-supplement.tex:3-8`. These are active reader lines. The remaining OPEN text in `handbook/parts/p03.tex:10-13,60-62` is comment-only and is not part of this residual.
- exact correction: After F6-F7 are resolved, replace the types body/annex and QE body notices with ordinary source/nonreplacement/proof-status attribution, removing D-P/internal gate language. Do not infer register admission, build, visual, human, or user acceptance from that notice replacement.
- disposition: still-open.

### F2 — still-open

- current evidence: The 21 exact Part III provenance records still yield `open_destinations=21`, `independent_source_pending=21`, and all completeness dimensions pending. `spec/provenance/reviewed-handbook-unit-records.json:5` and `spec/provenance/reviewed-register-obligation-records.json:6` still contain zero records. No current control binds the newly expanded body units, the new source-boundary file, or `handbook/parts/p03/further-reading.tex` to an admission decision.
- exact correction: Keep the r1 correction unchanged: after the final source bytes freeze, regenerate the construction snapshot/unit inventory, add hash-bound reviewed-unit and reviewed-obligation records with this board's exact scope, and update each provenance/source-completeness field individually. Build, visual, human, and user gates remain separate.
- disposition: still-open.

### F3 — accept-fixed

- evidence changing r1: The reader annex root now inputs only `annex/p03/types-ultraproducts-supplement` (`handbook/annex/p03.tex:1-3`). `annex/p03/qe-categoricity-games-supplement.tex`, including `annex:p3.qe.5`, is unreachable. The current 53-file graph therefore has only the exact inherited `thm:dlo-countable-categorical` and its inline complete proof at `handbook/restoration/inherited-07295-07468.tex:108-131`; it no longer publishes an unmatched second annex proof or a second proof-standing claim.
- boundary: R-030's administrative closure remains part of F2, but the duplicate/orphan reader route identified by F3 is gone.
- disposition: accept-fixed.

### F4 — accept-fixed

- evidence changing r1: The exact inherited artifact remains byte-unchanged, but the immediately following reader unit now gives an explicit source erratum at `handbook/parts/p03/ultrafilter-choice-and-source-boundary.tex:32-40`: it distinguishes the retained *On the Extending of Models I* key from the actual ultraproduct source and cites `Los1955Ultraproducts`. The new bibliography record at `handbook/bib/handbook.bib:403-414` has the correct author, French article title, container *Mathematical Interpretation of Formal Systems*, series/volume 16, pages 98-113, North-Holland, Amsterdam, 1955, and DOI `10.1016/S0049-237X(09)70306-4`. `handbook/parts/p03/further-reading.tex:12-14` uses that corrected key.
- authority: Those fields agree with the [primary publisher record](https://www.sciencedirect.com/science/article/pii/S0049237X09703064/pdf) and the [Polish Academy historical account](https://www.impan.pl/images/schinzel.pdf). Keeping the old `Los1955` record as inherited bibliography evidence no longer makes it the controlling source for the theorem.
- disposition: accept-fixed.

### F5 — accept-fixed

- evidence changing r1: `handbook/parts/p03/qe-categoricity-games-supplement.tex:128-143` now uses `cited=Vaught1965CardinalsFarApart`. The new `@incollection` record at `handbook/bib/handbook.bib:741-750` gives Vaught as author; *A Löwenheim--Skolem Theorem for Cardinals Far Apart* as title; *The Theory of Models* as container; Addison, Henkin, and Tarski as editors; pages 390-401; North-Holland, Amsterdam; 1965. Those roles match the [Cambridge/JSL bibliographic record](https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/r-l-vaught-a-lowenheimskolem-theorem-for-cardinals-far-apart-the-theory-of-models-proceedings-of-the-1963-international-symposium-at-berkeley-edited-by-j-w-addison-leon-henkin-and-alfred-tarski-studies-in-logic-and-the-foundations-of-mathematics-northholland-publishing-company-amsterdam1965-pp-390401/B772C31774DF696C8B1A9C7E280AE402) and [publisher contents](https://www.sciencedirect.com/book/9780720422337/the-theory-of-models). `Vaught1961` remains separately available for the never-two theorem and conjecture history.
- disposition: accept-fixed.

### F6 — still-open

- substantial repairs accepted: The new classification chapter now supplies the Fraisse HP/JEP/AP package, limit theorem, and random-graph extension/omega-categoricity entry (`classification-theory.tex:17-90`); countable saturated models plus never-two/conjecture status (`135-191`); EM blueprints/applications (`228-265`); cardinal stability, omega-stability, superstability, and nonforking laws (`349-397`); Morley rank, total transcendence, strongly minimal sets, and Baldwin--Lachlan/Morley outline (`399-469`); and o-minimal monotonicity/cell decomposition (`492-540`). The preservation chapter now supplies existential closure/model companions (`21-92`), a model-theoretic joint-consistency proof (`94-141`), Beth/Craig/Robinson material (`267-336`), the Q1 landmark (`338-384`), and a long Lindstrom argument (`386-518`). The finite-model chapter adds a substantive computable-model entry (`120-172`). The new further-reading unit groups sources for every charter lot (`further-reading.tex:1-26`). These changes resolve most absence claims from r1.
- residual definition defect: `classification-theory.tex:351-371` defines cardinal stability with `S_1(A)`, and `374-391` states symmetry with `\operatorname{tp}(a/Ab)`, but neither notation is defined anywhere in the live handbook. The inherited chapter defines complete types over a parameter set semantically, but introduces neither `S_n(A)` nor `\operatorname{tp}(a/A)`. The new stability and nonforking statements are therefore not eliminable at first use.
- exact correction for notation: Before `def:p03-stability-spectrum`, define `S_n(A)` as the set of complete `n`-types over `A` consistent with the fixed complete theory/ambient model, and define `\operatorname{tp}(a/A)` as the complete type consisting of the parameter formulas satisfied by `a`; state independence from the chosen sufficiently saturated ambient model. Then use those exact definitions in the spectrum and symmetry statements.
- residual source-role defect: `thm:p03-em-models` combines the EM blueprint/functorial construction with the claim that every unstable complete theory has `2^\kappa` nonisomorphic models in every `\kappa>|T|`, but its status is only `cited=EhrenfeuchtMostowski1956` (`classification-theory.tex:248-256`). The unstable-spectrum clause is Shelah's separate theorem, not a theorem printed by the 1956 EM paper. The prose cites `Shelah1971Stability`, which is itself a different Annals of Mathematical Logic article. The exact primary source is Shelah, *The Number of Non-Isomorphic Models of an Unstable First-Order Theory*, Israel Journal of Mathematics 9 (1971), 473-487, DOI `10.1007/BF02771463`; its [publisher abstract states the same bound and conclusion](https://link.springer.com/article/10.1007/BF02771463).
- exact correction for source role: Split `thm:p03-em-models` into an EM construction theorem controlled by `EhrenfeuchtMostowski1956` and an unstable-spectrum theorem controlled by a new exact Shelah 1971 record, or assign each clause an independently visible source status. Do not let a prose citation to a different Shelah paper stand in for the theorem-bearing source.
- disposition: still-open.

### F7 [new blocker] — editorial proof text contradicts the mandatory cited-only status

- location: `handbook/CONVENTIONS.md:60-72`; `handbook/parts/p03/preservation-abstract-logic.tex:3-4,107-141,288-316,421-518`; `handbook/parts/p03/finite-model-theory.tex:148-167`; charter exact-proof-status invariant and registered treatment ceilings N-a-013/N-a-061.
- claim: The mandatory status grammar says `cited=<bibkey>` means “statement only; source carries the proof,” and new editorial proof material lives under `annex/`. The changed reader files now put explicit local proofs immediately after four theorems still marked `cited=`: Robinson joint consistency, Beth definability, Lindstrom's theorem, and computable categoricity of the rational order. The preservation file's own header still says every status-bearing result is citation-only and no proof is claimed. Thus theorem metadata, reader proof text, annex placement, and the claimed full-proof register ceilings disagree.
- evidence: `thm:p03-robinson-joint-consistency` is `cited=RobinsonJointConsistency1956` at line 107 and receives “Model-theoretic proof” at lines 124-141. `thm:p03-beth-definability` is `cited=Beth1953` at line 288 and receives a proof ending in `\square` at lines 293-316. `thm:p03-lindstrom` is `cited=Lindstrom1969` at line 421 and receives a multi-lemma proof ending in `\square` at lines 434-512. `thm:p03-q-computably-categorical` is `cited=AshKnight2000` at `finite-model-theory.tex:148` and receives a proof ending in `\square` at lines 154-167. The current annex graph contains only the compactness-via-ultraproduct proof, so none of these local proof claims has a reciprocal annex status.
- correction: For every proof intended to count as local evidence, move the complete proof into a uniquely labelled Part III annex item and change the body status to `proved=annex:<id>`. This is required for the N-a-013 model-theoretic proofs and the N-a-061 full Lindstrom proof; expand any suppressed coding step there before calling it complete. For a result intended to remain citation-only, replace the body proof by an explicitly bounded proof idea/sketch that does not claim completion and enumerate what the source still carries. Recheck reciprocal body/annex status before closing the register rows.
- disposition: still-open, blocking source/content admission.

## New-authority verification

- checked: Fraisse's limit theorem and Rado's graph roles match the cited primary works; the live construction distinguishes the Fraisse class, ultrahomogeneity, extension property, and omega-categoricity rather than treating them as aliases.
- checked: Vaught's 1961 never-two theorem and the current open-conjecture statement are correctly separated from the repaired 1965 two-cardinal source. Current 2025-2026 literature continues to describe the general conjecture as open; recent work discusses restrictions and necessary features of counterexamples rather than a verified solution.
- checked: The Baldwin--Lachlan record and theorem scope agree with the primary paper's strongly-minimal analysis and its one-or-countably-many countable-model conclusion ([Cambridge primary record](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/393A3AEC617C29FC6AB9C6BCF3C21ABE/S002248120008395Xa.pdf/on-strongly-minimal-sets.pdf)). The o-minimal monotonicity and cell-decomposition variants agree with Pillay--Steinhorn and van den Dries ([cell-decomposition chapter](https://www.cambridge.org/core/books/abs/tame-topology-and-ominimal-structures/cell-decomposition/04F570063CE5D7F34AE6152836529552)).
- checked: Robinson model completeness, ACF/RCF model completions, Beth definability, Craig/Robinson/Beth equivalence, and Keisler's `L(Q_1)` completeness/countable-compactness roles match their cited sources; the [Keisler primary publication](https://www.sciencedirect.com/science/article/pii/S0003484370800055) is the correct work for the Q1 claims.
- checked: All 57 reachable citation/status keys exist. The new `Los1955Ultraproducts` and `Vaught1965CardinalsFarApart` field roles are correct. The further-reading groups introduce no theorem-status promotion.

## Structural and not-checked boundaries

- current graph: 53 reachable files; no duplicate identifier; no unresolved scoped Part III reference; 57 citation/status keys with no missing bibliography key; one genuine `proved=annex:p3.types.8` pair and one reciprocal annex target. The three route-hook anchors at `handbook/parts/p03.tex:27-58` attach navigation labels to the intended second theorem of `SRC-07150` and third/fourth theorem of `SRC-07295` without changing inherited artifact bytes or order.
- exact inherited source: not rerun in this round; r1's 21 interval/hash/content-token passes remain the latest source/static evidence available to this seat, and no exact artifact edit was observed in the live graph.
- not checked: TeX build, generated index/reference/bibliography refresh, PDF rendering, layout/overflow, visual inspection, F2 admission regeneration, human review, or user acceptance. I did not treat source checking as evidence for any of those gates.
- not checked: I did not inspect every page of every closed-access monograph. Where exact theorem/source roles were disputed or newly load-bearing, I used fetchable primary/authoritative records and identified the one unresolved theorem-source mismatch under F6.

## Round-2 disposition summary

- accept-fixed: F3, F4, F5.
- still-open: F1, F2, F6.
- new blocker: F7.
- no other-seat transcript read; no manuscript/control/test/generated edit; no build or test construction.
