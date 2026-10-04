# Part VII round 2b — source-fidelity targeted recheck

Role: source fidelity/evidence. Snapshot: current live reader route after R2 repairs. I rechecked only R2 F1--F8 and the requested finite-set Cut proof/source boundary. The live route is the exact wrappers plus `calculi-and-derivability-supplement.tex` at `handbook/parts/p07.tex:86-118`; the dormant historical body files are not evidence for the current reader surface. No build or tests were run, and no handbook, source, registry, control, generated, or test file was edited.

## R2 F1 — `N-a-055`: honest source-relative treatment, but literal obligation still blocks admission

**Disposition: still open as an admission blocker; not a false completion claim.**

- The reader now distinguishes exactly what is locally proved from what is imported. `handbook/parts/p07/functional-interpretations.tex:328-338` proves only the cut-free LJ last-rule lemma and says that arbitrary-derivation extraction additionally needs complete cut elimination. The IPC, HA disjunction, and HA numerical-existence results are each explicitly `cited=TroelstraVanDalen1988` at `:340-361`.
- The source boundary at `:363-389` gives the concrete locator, *Constructivism in Mathematics*, Vol. I, Chapter 3, section 5.6, beginning at p. 139; identifies equality, induction, normalization, and erasure as source-side machinery; and expressly denies that the handbook reproduced that machinery or locally proved the three results. The annex likewise says it proves only the LJ last-rule lemma (`handbook/annex/p07/functional-interpretations.tex:1-4,6-37`). This is source-faithful and is not a printed assertion of local completion.
- Literal register completion is nevertheless absent. `spec/registers/new-content.csv:56` requires “disjunction and numerical existence properties for IPC and HA **with proofs**,” while `spec/register-obligation-closure.csv:197` remains `open,OPEN`. A citation to a proof and a description of its shape do not constitute the locally routed proofs named by that frozen row.
- Exact correction for admission: either route complete proofs for the fixed IPC/LJ and HA calculi, including the equality/induction normalization machinery on which the HA extraction depends, or obtain an authorized contract supersession that changes `N-a-055` from local “with proofs” completion to the present source-relative cited treatment. The present prose should otherwise remain because its status boundary is accurate.

## R2 F2 — `A-074`: honest local table and honest deferral, but literal master-table obligation still blocks admission

**Disposition: still open as an admission blocker; not a false completion claim.**

- The current live table defines its calibration convention at `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:251-271`, captions itself “Local citation-qualified” and “input to, not a substitute for, the separate master table” at `:273-278`, supplies only the six scoped rows at `:287-308`, and explicitly declines to guess the lower arithmetics or broader set-theory range at `:313-317`. This is an exact and honest source boundary.
- The frozen must-level row still requires one master table covering “Q-range fragments, PA, and stronger systems” (`spec/registers/apparatus.csv:75`), and its closure record remains `open,OPEN` (`spec/register-obligation-closure.csv:401`). The current six-row table begins at modern PRA and expressly says it does not discharge that range.
- Exact correction for admission: supply the separate master A-074 table with a fixed lower-fragment presentation and citation-qualified Q-range/PA/stronger rows, or obtain an authorized supersession/reassignment of A-074. Do not relabel the current local table as the master.

These two records therefore pass source honesty but fail the charter's separate requirement that Part VII be “complete for every Part VII register commitment.” Under the current charter, their deliberate research deferral does not convert them into completed obligations.

## R2 F3 — categorical and Cut notation

**Disposition: partially fixed; one exact registry residual remains open.**

- **Categorical family fixed.** The live definition now uses typed `\mathsf 1_{\mathrm{ty}}` and `\mathsf 0_{\mathrm{ty}}`, products/sums, constructors, eliminators, and the typed beta--eta relation at `handbook/parts/p07/normalization-and-curry-howard-supplement.tex:34-94`. Registry rows `handbook/registry/symbols.csv:432-435` cover those families, and both generated surfaces contain the corresponding entries (`handbook/generated/symbols-tables.tex:540-543`; `handbook/generated/symbol-index.tex:42,279,287,534`). The typed empty type no longer collides with the computable Turing degree `\mathbf0` at `handbook/registry/symbols.csv:263`.
- **Cut measures only partly fixed.** `r(A),h(c),o(D)` and Hessenberg natural sum `\#` are registered at `handbook/registry/symbols.csv:436-437` and appear in both generated surfaces (`handbook/generated/symbols-tables.tex:544-545`; `handbook/generated/symbol-index.tex:272,507`). But the same live definition introduces the Cut-node constructor/set `\operatorname{Cut}_A(D_0,D_1)` / `\operatorname{Cut}(D)` and the indexed cut formula `A_c` at `handbook/parts/p07/arithmetic-proof-theory-supplement.tex:133-141`. Neither token occurs in `handbook/registry/symbols.csv`, `handbook/generated/symbols-tables.tex`, or `handbook/generated/symbol-index.tex`; row 436's displayed symbols and key contain only `r,h,o`.
- Exact correction: expand the P7.5 metalinguistic row (or add a companion row) to register `\operatorname{Cut}_A(D_0,D_1)`, `\operatorname{Cut}(D)`, and `A_c` with their constructor/set/indexed-formula roles, then regenerate both symbol surfaces. This is direct fallout from F3, not a new topic.

## R2 F4 — Jäger--Probst identity

**Disposition: accept fixed.**

`handbook/bib/handbook.bib:3530-3538` now contains valid UTF-8 `Jäger, Gerhard` and *Variation on a Theme of Schütte*, with journal, volume, issue, pages, year, and DOI `10.1002/malq.200310097`. A strict UTF-8 decode of the current bibliography bytes succeeds. The names/title now match the authoritative [DOI record](https://doi.org/10.1002/malq.200310097); the malformed `J{"a}ger`-without-backslash analogue is gone.

## R2 F5 — A-071 status/source split

**Disposition: accept fixed for source/content.**

- The live guide now says the inherited propositions/first-order completeness entries retain their source sketch status while the new theorem supplies a separate complete local proof (`handbook/parts/p07/calculi-and-derivability-supplement.tex:97-118`). The theorem itself is `proved=annex:p7.calculi.4` at `:215-223`.
- The A-071 catalog row now states both facts rather than collapsing them: inherited completeness remains a sketch; `thm:p07-canonical-lk-completeness` supplies a separate local proof (`:243-248`).
- The structural comparison explains why the source-Part-VIII reduction does not establish canonical-LK cut admissibility: it belongs to `LK_d`, with different logical and identity rules (`:49-57`). Calling it “source Part VIII” is historical source provenance, not a stale present-day reader-route assignment.

## R2 F6 — exact Craig/Beth route standing

**Disposition: accept fixed.**

The hand route now says exactly “exact source entry with cited-theorem standing and no annex item” for Craig and Beth (`handbook/parts/p07/proof-complexity.tex:226-245`); it no longer imports dormant `cited=Craig1957` / `cited=Beth1953` tokens. That wording matches the live exact artifact, whose Craig statement says `Status: cited theorem` and routes its proof-theoretic/model-theoretic evidence to Troelstra--Schwichtenberg and Hodges (`handbook/restoration/inherited-11914-11960.tex:4-24`), and whose Beth statement has the same cited status and routes the consequence to Hodges (`:26-40`). The supplementary route also refuses a local status upgrade (`handbook/parts/p07/cut-elimination-and-interpolation-supplement.tex:166-193`).

## R2 F7 — Wansing fragment versus full source calculus

**Disposition: accept fixed.**

The sheet identifies itself as a “Worked-Derivation Fragment,” says it is not the complete rule surface, and limits its scope to the worked example (`handbook/registry/calculi/display-k-wansing.tex:1-5`). The worked cycle uses exactly the printed Identity, Box-L, Modal Display, and Box-R rows and denies being an adequacy proof (`handbook/parts/p07/structural-extensions.tex:178-197`). The cited theorem is now explicitly about Wansing's **full** display-K calculus and says the printed sheet does not inherit the full metatheorems (`:220-225`); the A-071 catalog repeats that distinction (`handbook/parts/p07/calculi-and-derivability-supplement.tex:283-288`). This matches the scope of [Wansing 1994](https://doi.org/10.1093/logcom/4.2.125).

## R2 F8 — MLTT composite and ACD theorem scope

**Disposition: accept fixed for source role and theorem scope.**

The sheet now says it is an editorial composite, not a verbatim calculus controlled by one metatheorem source; assigns the broad intensional/judgment/universe organization to Martin--Löf and later standard presentations; and assigns Abel--Coquand--Dybjer only to the dependent-function/one-universe normalization and typed-equality theorem, expressly excluding Sigma, identity types, and the cumulative hierarchy (`handbook/registry/calculi/mltt-intensional.tex:1-14`). Its rules at `:15-67` are therefore locally fixed components of the disclosed composite, not falsely attributed verbatim rows. The body makes the same whole-sheet/subcalculus distinction at `handbook/parts/p07/lambda-calculi-and-type-theories.tex:399-424,442-451`, and the route table repeats it at `handbook/parts/p07/proof-complexity.tex:254-279`. That narrow claim matches the [Abel--Coquand--Dybjer author-hosted paper](https://www.cse.chalmers.se/~peterd/papers/NbeMLTTEqualityJudgements.pdf).

## Requested finite-set Cut proof/source-standing check

**Disposition: accept the proof standing and source boundary; the F3 notation omission above remains separate.**

- The body identifies `arithmetic-proof-theory-supplement.tex` as separately authored editorial material, not inherited source or a local proof of Gentzen's full arithmetic theorem (`handbook/parts/p07/arithmetic-proof-theory-supplement.tex:1-14`). It then exactly defines the finite-set support calculus as the propositional support image of the registered, source-extracted `sheet:lk-defneg`, including identity, bottom-left, monotonicity, contraction/exchange, absence of Mix, clean/nonclean Cut, and the two support translations (`:94-124`). The source sheet itself records its Part-VIII extraction and exact multiset rules at `handbook/registry/calculi/lk-defneg.tex:1-19`.
- The theorem is explicitly local `proved=annex:p7.arithmetic.1` and limits itself to the fixed deterministic propositional strategy, denying both arbitrary-reduction strong normalization and an upgrade of the source-relative epsilon-zero arithmetic analysis (`handbook/parts/p07/arithmetic-proof-theory-supplement.tex:169-180`). The route table makes the same split (`handbook/parts/p07/proof-complexity.tex:281-292`).
- The annex labels itself an editorial proof and supplies the clean/nonclean initial cases, commuting cases, all three compound principal pairs, the ordinal decrease, termination, and both support translations (`handbook/annex/p07/arithmetic-proof-theory-supplement.tex:1-114`). Its source standing is therefore accurate: a complete local proof for the newly defined finite-set propositional presentation, derived from but not passed off as inherited `LK_d` source, and not evidence for full arithmetic cut elimination.

## Final source/content verdict

Six R2 source-role defects are fixed (F4--F8 and the categorical portion of F3), and the finite-set Cut proof has honest local editorial standing. Part VII still cannot be admitted under the literal charter: `N-a-055` lacks the required proofs, `A-074` lacks the required master table or supersession, and F3 still omits `\operatorname{Cut}(D)` / `A_c` from the registered and generated notation surfaces. The first two are honest deferred/open records rather than false completion claims, but honest deferral is not literal register completion.

REJECT
