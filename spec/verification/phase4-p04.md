# Phase 4 verification: Part 4

> **PASS VERDICT INVALIDATED (2026-08-12).** This note verified the revoked
> compressed-migration policy, not the binding full-transcription standard.
> Retain it only as audit evidence; see `FULL-TRANSCRIPTION-READINESS.md`.

Date: 2026-08-11
Visit: P4, Computability and Complexity
Verified source: `v1.1-verified`, Part V, lines 7494--9079.

## Delivered scope

- Body: machines and effective procedures; universal computation, reductions,
  and fixed points; logical decision problems and the arithmetical hierarchy;
  relative computation, degrees, and priority; frontiers of computability; and
  complexity theory.
- Annex: twenty-seven items in exact one-to-one correspondence with seventeen
  `proved` and ten `sketched` body results.
- Result inventory: sixty-one statused results -- seventeen `proved`, ten
  `sketched`, and thirty-four `cited`.
- Tier-1 method: the finite-injury priority construction, with a body method,
  a construction table, the Friedberg--Muchnik theorem, and an annex sketch
  that states the omitted coding and compiler obligations.
- Apparatus: A-045, A-046, A-047, A-048, A-049, A-050, A-052, A-124, A-125,
  A-126, A-127, A-163, A-182, A-186, and A-189.
- Integration: the Part-4 body driver inputs all six body fragments and ends
  with the generated P4 audit register; the annex driver inputs all four P4
  annex fragments.

## Source and evidence accounting

All twenty-nine theorem, lemma, or corollary results carrying a source status
or complete proof were checked against the repaired source.  Fourteen complete
source proofs remain proved, all nine source sketches remain sketched with
named omissions, and all six cited source theorems remain citation-only.  The
complete-proof count includes the complement-of-`K` corollary at source lines
8114--8121, whose complete proof is present even though the source omitted a
printed `Status:` line.

| Source fragment | Complete proofs | Proof sketches | Cited theorems |
|---|---:|---:|---:|
| Machines and effective procedures, 7497--7849 | 2 | 2 | 0 |
| Universal computation and reductions, 7851--8247 | 6 | 2 | 1 |
| Decision problems and arithmetical hierarchy, 8248--8897 | 6 | 2 | 4 |
| Relative computation and jump, 8898--9079 | 0 | 3 | 1 |
| **Total** | **14** | **9** | **6** |

That twenty-nine-result table deliberately excludes the source example at
8123--8142.  Its lines 8129--8141 contain a complete binary-domain argument;
the no-body-proofs rule therefore required a proved corollary and annex item
rather than leaving the reasoning inside an example.

The additional annex-backed local-numbering bridge and many-one-versus-Turing
lemma are complete derivations supplied during the migration and have no
source-compression ratio.  The binary-domain corollary extracts and statuses a
complete argument formerly printed inside a source example; its separate
ratio appears below.  The Friedberg--Muchnik theorem is the one new `sketched`
result.  All other new statused results stay at the citation ceilings
supported by the research ledger.  No source evidence class was upgraded.
Thus the seventeen final proved results comprise fourteen source-result proof
migrations, the extracted binary-domain proof, and two new complete
derivations; the ten sketches comprise nine source sketches and the new
Friedberg--Muchnik sketch; and the thirty-four citations comprise six source
citations and twenty-eight new source-backed entries.

The established `detex` alphabetic-word method was applied to all fourteen
complete source-result proofs and all nine source sketches.  Complete-proof
counts exclude result statements and `proof` delimiters.  Sketch source counts
use the `proofplan` interior, except that the final convention bridge uses its
substantive remark and embedded omission note at 9055--9077; sketch annex
counts include the full `annexitem` interior and its `sketchnote`, matching the
P3 precedent.  Each ratio is annex words divided by source words.

| Result | Source proof lines | Target annex item | Source to annex words | Ratio |
|---|---:|---|---:|---:|
| Machine form of decidability | 7801--7805 | `annex:p04-machines.2` | 47 to 27 | 57.4% |
| Complement criterion for decidability | 7837--7841 | `annex:p04-machines.4` | 46 to 21 | 45.7% |
| Renaming invariance | 7922--7932 | `annex:p04-universal.1` | 94 to 52 | 55.3% |
| Enumeration theorem | 7948--7995 | `annex:p04-universal.2` | 415 to 239 | 57.6% |
| Preservation under many-one reduction | 8070--8072 | `annex:p04-universal.4` | 32 to 17 | 53.1% |
| Undecidability of the self-application domain set | 8096--8111 | `annex:p04-universal.5` | 81 to 46 | 56.8% |
| Complementary domain set | 8119--8120 | `annex:p04-universal.6` | 14 to 6 | 42.9% |
| Rice's theorem | 8209--8230 | `annex:p04-universal.8` | 160 to 94 | 58.8% |
| Enumerability without decidability | 8274--8280 | `annex:p04-hierarchy.1` | 74 to 35 | 47.3% |
| Pairing graph | 8454--8462 | `annex:p04-hierarchy.2` | 87 to 51 | 58.6% |
| G\"odel beta function | 8495--8520 | `annex:p04-hierarchy.3` | 241 to 124 | 51.5% |
| Pairing contraction | 8547--8555 | `annex:p04-hierarchy.4` | 88 to 48 | 54.5% |
| Bounded-quantifier exchange | 8579--8588 | `annex:p04-hierarchy.5` | 100 to 58 | 58.0% |
| Prefix normal form | 8624--8707 | `annex:p04-hierarchy.6` | 615 to 270 | 43.9% |
| **Total** | -- | -- | **2094 to 1088** | **52.0%** |

All fourteen complete source-result proofs lie in the required 40--60% band.
The first eight entries were already compliant when independently audited and
were not shortened, expanded, or otherwise edited in response to their
measured ratios.  The pairing proof received one two-word compliance
adjustment before its final 58.6% measurement.

The newly annexed binary-domain corollary was checked separately because its
source evidence was an argument-bearing example rather than a statused result:

| Result | Source argument lines | Target annex item | Source to annex words | Ratio |
|---|---:|---|---:|---:|
| Binary and self-application domain problems | 8129--8141 | `annex:p04-universal.10` | 93 to 52 | 55.9% |

This extracted proof lies in the required band after its single compliance
pass.  No already compliant migrated proof was repeatedly shortened.

The nine source-sketch migrations give:

| Result | Source sketch lines | Target annex item | Source to annex words | Ratio |
|---|---:|---|---:|---:|
| Primitive recursive functions are computable | 7723--7731 | `annex:p04-machines.1` | 91 to 49 | 53.8% |
| Equivalent forms of computable enumerability | 7822--7827 | `annex:p04-machines.3` | 59 to 35 | 59.3% |
| Universal computation | 8015--8023 | `annex:p04-universal.3` | 83 to 48 | 57.8% |
| Kleene recursion theorem | 8157--8176 | `annex:p04-universal.7` | 108 to 64 | 59.3% |
| Bounded verification of computations | 8766--8789 | `annex:p04-hierarchy.7` | 258 to 144 | 55.8% |
| Computable enumerability and level one | 8806--8815 | `annex:p04-hierarchy.8` | 73 to 42 | 57.5% |
| Relativized adequacy | 8969--8979 | `annex:p4.degrees.1` | 100 to 54 | 54.0% |
| Jump theorem | 8996--9020 | `annex:p4.degrees.2` | 170 to 89 | 52.4% |
| Convention bridge for the jump | 9055--9077 | `annex:p4.degrees.3` | 209 to 111 | 53.1% |
| **Total** | -- | -- | **1151 to 636** | **55.3%** |

Every source sketch lies in the required band.  The bounded-verification,
level-one, relativized-adequacy, and jump-bridge items each received one
compliance compression after the exhaustive audit exposed their overlength;
their omission notes and source evidence classes were retained.

Five source exercises, beginning at source lines 7844, 8239, 8877, 8884, and
8891, are explicitly accounted for in body-file comments and deliberately
retired because the handbook has no exercise layer.  No source result is
retired; the first two exercises' substantive cautions survive in the
complement criterion and the exact scope of Rice's theorem.

## Repaired-source fidelity

- R-002: one fixed machine and history coding is retained.  The pairing and
  beta lemmas supply bounded extraction, history certificates include the
  program table, input, configuration sequence, and valid-output check, and
  the bounded-verification and level-one consequences retain source-sketch
  status.
- R-003: object-language \(<\) and \(\leq\) are defined as eliminable
  arithmetic abbreviations with fresh witnesses, with the witness on the
  registered side of addition.  Metalinguistic \(<_{\N}\) and
  \(\leq_{\N}\) remain separate, and the already statused Part-5 bounded-case
  and dichotomy lemmas carry the Robinson-arithmetic obligations.
- R-004: the ordinary and relativized jumps use accepting-with-valid-output
  definedness rather than arbitrary halting.  Relativized adequacy, the jump
  theorem, and the convention bridge remain sketches; Post's theorem remains
  cited.
- R-005: the bespoke numbering fixes designated state and symbol slots, full
  row order, invalid-code divergence, tuple application, and the output
  wrapper.  Its enumeration theorem retains a complete proof, every
  numbering-dependent index choice cites it, and the annex-backed range
  corollary ties that numbering to the partial-recursive class without
  identifying it with Kleene's separate normal-form coding.
- R-006: the proved pairing, beta, contraction, and bounded-exchange lemmas
  support the proved closure-to-prefix-normal-form theorem.  Formula classes
  and boldface relation classes remain distinct throughout A-047 and A-124.
- R-035: partial computability is stated by one definiendum--definiens
  biconditional followed by the defined and undefined cases; divergence is not
  treated as a third output.

## Depth rows and apparatus ceilings

Filled at their registered ceilings: D-P5-001, D-P5-002, D-P5-003, D-P5-004,
D-P5-005, D-P5-006, D-P5-007, and D-P9-002; N-a-016 through N-a-024; and
N-a-063 and N-a-064.  The `could` rows receive their registered treatment
rather than being silently promoted: word problems and Busy Beaver are table
or short-entry treatments, and computable presentations remain an explicit
pointer that does not discharge the P3 model-theory row.  N-x-014's Type-2
effectivity, represented spaces, and Weihrauch degrees remain deliberately
outside P4.

A-045 fixes each machine model, function convention, equivalence edge, and
evidence source.  A-046 gives encoded instance sets and sources for the seven
undecidability rows.  A-047 and A-124 share the repaired arithmetical-hierarchy
conventions; A-048 and A-125 are visibly lightface and record
\(\Delta^1_1=\mathsf{HYP}\); and A-049 and A-126 separate Kleene--Post degrees
from the c.e. degrees supplied by Friedberg--Muchnik.  A-050 and A-127 mark
known strict inclusions, inclusions only, and open equalities rather than
presenting an unproved Hasse diagram.  A-052 states the finite-vocabulary and
order hypotheses for descriptive complexity.

A-163 assigns the P4 glyph-role pairs, including the separate object-language
and metalinguistic orders, tuple arrows, convergence symbols, degree notation,
and complexity classes.  A-182 supplies the verified P4 bibliography records,
including the dedicated `Myhill1955`, `Johnson1977Rice`, `Berger1966`, and
`Rado1962BusyBeaver` keys.  A-186 separates historical primaries from modern
systematic reading, and A-189 gives every `proved` or `sketched` target one
annex item, with every sketch naming its omissions.  Final global
bibliography, symbol, and cross-reference closure is reserved for the release
checks below.

## Adversarial correction log

The independent source, fidelity, standards, bibliography, and symbol reviews
corrected:

- the standing of Kleene's normal-form index, which is now explicitly separate
  from the later bespoke program index, and the missing R-005 bridge from that
  bespoke numbering to partial recursion;
- proof reasoning that had remained in body prose, moving the local-numbering
  bridge and the binary-domain equivalence into statused annex-backed results,
  and relocating finite-injury and reduction arguments without upgrading their
  evidence;
- the exhaustive ratio audit's newly exposed overruns: a two-word pairing-proof
  adjustment, one compliance pass for the extracted binary-domain proof, and
  one compliance compression each for bounded verification, the level-one
  characterization, relativized adequacy, and the jump-convention bridge;
- the Turing-machine definition's literal `(Q)`, restoring the mathematical
  \(Q\); the degree-annex target namespace was separately audited and retained
  as `annex:p4.degrees.*` under the annex-specific precedent;
- the jump's convergence convention and the distinction between the
  non-c.e. Kleene--Post incomparable degrees and the c.e. incomparable degrees
  supplied by Friedberg--Muchnik;
- the finite-injury construction's empty-restraint case, live-numbering and
  compiler dependencies, finite-stage coding obligations, and honest sketch
  omissions;
- claims about simple, creative, and complete sets: simple is not asserted to
  mean intermediate, acceptable-numbering hypotheses are explicit, one-one and
  many-one reducibility remain distinct, and Rice--Shapiro includes the empty
  class convention;
- the R-002 blank-tape case and bounded decoding certificates, the R-003
  witness order, and the R-006 separation between syntactic and boldface
  hierarchy levels;
- L-012/L-013 retypesetting of tall set-builders and prose inside mathematical
  delimiters, together with tuple-arrow versus numeral-bar and universal-
  evaluator symbol collisions;
- the lightface analytical-hierarchy scope, plain versus prefix-free
  Kolmogorov complexity, the fixed-machine dependence of Busy Beaver, and the
  plane rather than finite-board scope of the domino problem;
- complexity-diagram semantics, the order hypothesis for FO(LFP), and the
  exact primary citations for TQBF, fixed-alternation QBF, Myhill,
  Rice--Shapiro, tiling, and Busy Beaver; and
- explicit retirement records for all five source exercises instead of
  silently dropping them.

The original eight-proof migration audit caused no ratio-driven edits to those
already compliant proofs.  The pairing and binary adjustments and the four
sketch compressions above were the single compliance passes required by the
later exhaustive audit.  No proof or sketch was repeatedly shortened after
entering the band.

## Mechanical evidence

- Integrated TeX Live 2025 build with biber and makeindex: pass, 463 pages;
  biber resolved 143 cited keys.
- `python tools/check.py --tree handbook --strict`: pass; 301 symbol rows,
  286 distinct glyphs, 360 bibliography entries, 123 proved / 20 sketched /
  89 cited statuses globally, zero malformed statuses, and 32 remaining
  tracked stubs, none in P4.
- `python tools/check.py --tree source`: pass; the frozen source tree is
  unchanged.
- `python tools/symbols2tex.py`: pass; 301 rows in ten scope groups.
- `python tools/audit_tables.py`: pass; 128 generated P4 audit rows and 499
  rows across all fourteen generated part tables.
- Text-tree `git diff --check`, excluding the tracked binary `main.pdf`,
  passes; `git diff --exit-code -- source` is empty.
- The integrated log contains no undefined citation, reference, or control
  sequence and no biber warning or error.

## Visual evidence

The integrated PDF was rendered and inspected across the generated symbol
registry (physical pages 37--45), the entire P4 body (219--278), the adjacent
P5 notation pages affected by reconciliation (279--294), the P4 annex
(407--418), and the P5 annex opening (419--421).  This covers A-045 through
A-050, A-052, A-124 through A-127, A-186, all ten P4 tables, all four P4
figures, and every P4 annex item.

After the final proof-compliance edits and integrated rebuild, physical pages
413, 415--419 were rerendered at full page scale.  The pairing and binary
proofs, bounded-verification and level-one sketches, relativized and jump
sketches, finite-injury proof, and many-one/Turing proof are legible and
complete.  A four-baseline page enlargement keeps the final proof together on
printed page 399; printed page 400 is the intended blank spacer and the P5
annex begins on printed page 401.

No clipped text, collision, unreadable table, malformed figure, missing glyph,
running-head collision, or broken page flow was found.  Compilation and visual
inspection establish integration and presentation, not mathematical
correctness.  Source fidelity, new-content evidence, status preservation,
standards, and rendering were checked separately above.
