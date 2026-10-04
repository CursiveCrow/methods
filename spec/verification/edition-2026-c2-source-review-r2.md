# C2 independent source-fidelity repair recheck, round 2

Date: 7 September 2026. Reviewer: `/root/edition_c2_source_review`, the
independent source reviewer returning to recheck the repairs to its own
findings. Actual model identifier and reasoning-effort configuration remain
unavailable to the reviewer.

## Result

**SF-C2-01 and SF-C2-04 now PASS and are closed for this snapshot.
SF-C2-02 remains UNRESOLVED.** The relevant previously passing semantics,
attribution and numerical-boundary scopes remain intact. This is a repair
recheck, not a new full source-paper reconstruction or a source-admission
record. An exact-final-journal obligation still remains open.

The first review is preserved unchanged at
`spec/verification/edition-2026-c2-source-review.md`, SHA256
`9a71f5808255b647425755d01058960942cb1c5c7ba78ec4098a0ae3202ad071`.
No other reviewers' outputs or author verdicts were read. Only this new
round-2 review file was written. No manuscript edits, builds, renders or
software tests were performed.

## Current evidence

All repository paths below are relative to `C:/Dev/the-methods-of-reason`.
The hashes were calculated from the actual current files and matched the
repair assignment.

| Artifact | Current SHA256 | Recheck extent |
| --- | --- | --- |
| `handbook/parts/p09/logic-in-computer-science.tex` | `61e3125b950ae194412c81bc6c5eeb3dfceac533541b26007f6db7744e3ddc45` | Read lines 1318-1590 and 2455-2460. |
| `handbook/bib/handbook.bib` | `8c4ae5fcd93092eb676ec04878a6ee09406e987464a5cebf2e9db9c139b7105f` | Read the two complete source entries, lines 2508-2532. |
| `handbook/annex/p09/csl-corrections.tex` | `92aeada76892a0dbf271b8002dca189d563ba39c389ebb478be3d438521c42f5` | Reread entire file, lines 1-82; byte identity with first-review annex verified. |
| `handbook/parts/p09/presentations/n-x-015.tex` | `29c172d5ba714ea89e99f4272bd4b87aa2b72bc3d305447ba43ede5289c69e08` | Byte identity with first-review source boundary verified; prior reading of lines 141-181 retained. |
| `spec/EDITION-2026-CONTRACT.md` | `c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3` | Entire contract reread. |
| `source/references/baier-haverkort-hermanns-katoen-2002/ctit-02-10.pdf` | `4fa36cb3a826a1a62721762063e4d02da02c87343873577053c014b6b5050d74` | Byte identity with the first review's downloaded primary report verified; PDF metadata confirms 37 pages and 584,762 bytes. |

The report PDF has a malformed text layer. For this recheck, its already
rendered pages 1, 6, 10 and 15 were reinspected: title/authors, occupation
convention, threshold signature, and endpoint-closure passage respectively.
These images were produced during the first review from the identical PDF
hash; no new rendering was performed. The first review's explicitly recorded
reading of report pages 1, 4-11, 13-25 and 29-33 remains the wider body evidence.

The institutional [CTIT report record](https://research.utwente.nl/en/publications/model-checking-algorithms-for-continuous-time-markov-chains-2/)
and [journal article record](https://research.utwente.nl/en/publications/model-checking-algorithms-for-continuous-time-markov-chains/)
were reopened. They confirm distinct publication identities: report 02-10,
April 2002, Enschede, CTIT; and the June 2003 journal article in volume 29,
issue 6, pages 524-541, DOI `10.1109/TSE.2003.1205180`. These records supply
identity evidence. They do not supply the missing final-journal body.

## Per-finding disposition

### SF-C2-01 - PASS - Separate report and journal identities

Current locations: `handbook/bib/handbook.bib:2508-2532` and host
`logic-in-computer-science.tex:1470-1472`.

The 2003 journal entry retains the article identity and now sets its URL to
`https://doi.org/10.1109/TSE.2003.1205180`. It no longer uses the report PDF
URL. The new `BaierHaverkortHermannsKatoen2002Report` entry has report type,
the correct four authors and title, CTIT/University of Twente as institution,
Enschede as location, number `02-10`, date `2002-04`, and the verified report
URL. Its associated local PDF has the known report hash.

The host explicitly identifies the April 2002 report as an earlier
presentation and says report and journal locators identify separate versions.
This resolves the linkage and manifestation-conflation defect recorded in
the first review.

Closure: **closed for the stated current hashes**. This closure does not
assert that the journal body has been acquired or that report theorem
numbers can be substituted for journal theorem numbers.

### SF-C2-04 - PASS - Threshold range restored

Current location: host `logic-in-computer-science.tex:1364-1365`.

The CSL declaration now requires rational `q` in `[0,1]`. The report's
Definition 3.1, page 10, has thresholds in `[0,1]`; the handbook retains its
effective rational-input restriction. The previously unmarked permission
for thresholds outside the probability interval has been removed.

Closure: **closed for the stated current host hash**. No further repair is
required for this finding.

### SF-C2-02 - UNRESOLVED - Exact final-journal body

The required final journal article remains *IEEE Transactions on Software
Engineering* 29(6), 524-541 (June 2003), DOI
`10.1109/TSE.2003.1205180`. No new exact-final-journal body or final-journal
local hash was obtained in this recheck.

The retained 37-page report has its own established identity. The separately
inspected author-uploaded typeset candidate from the first review has a
different masthead and pagination; it remains a candidate. Neither becomes
the final journal manifestation through the repaired bibliography or the
new source-storage path. The first review's version-specific locator table
and exact-journal limitation continue to apply.

Closure requires a readable freely available or held exact-final-journal
body with verified identity, required extent, locator and local hash, followed
by comparison of the required passages against the frozen unit. A new
authorized source-version disposition would need its own review and would
not silently complete the original obligation. **This finding is open.**

### SF-C2-03 - PASS retained - Core semantic conventions

Current locations: host 1318-1362 and annex 10-24.

The rational-rate qualification, rate self-loops, zero-row absorbing states,
positive residence times, cylinder products and full-measure
time-divergence qualification remain. The annex's independent Poisson-clock
argument is unchanged. The broadened definition title spells out continuous
stochastic logic without altering these clauses.

Closure: the bounded first-review pass is retained; exact-journal
correspondence is still governed by SF-C2-02.

### SF-C2-05 - PASS retained - Source and correction boundaries

Current locations: host 1346-1350, 1407-1452 and 1475-1478; annex 6-81.

The active handbook still explicitly chooses right-continuous occupation.
The endpoint theorem and interval-computation theorem retain separate
`proved` annex links. Their derivation remains expressly separate from the
cited Volterra and steady-state results. The annex states what it proves
and where it relies on the source's embedded-chain result.

The report's prior-state occupation rule and unrestricted endpoint-closure
passage remain historical body evidence. The repaired text does not identify
the corrected clauses as identical original source wording.

Closure: the bounded pass is retained. Preserve this distinction in any
later source reconciliation or restoration.

### SF-C2-06 - PASS retained - Retained computations and attribution

Current locations: host 1454-1539; unchanged annex 41-81 and unchanged
`n-x-015.tex:149-169`.

The four source-computation summaries remain. The added version statement
keeps the report separate. The active matrix formulas still hold the
original state sets fixed, retain the positive-lower-bound first phase and
its state restriction, handle infinite upper bounds through `h`, and give
timed next its own calculation. The proof boundary is unchanged.

Closure: the bounded available-body comparison is retained. This is not
renewed acceptance of the absent final-journal body or a claim that all
original paper proofs have been reconstructed.

### SF-C2-07 - PASS retained - Numerical and complexity qualifications

Current locations: host 1541-1567, 1580-1583 and 2455-2460; unchanged
`n-x-015.tex:171-181`.

The Poisson-tail bound, separate retained-term/roundoff error, bound
propagation and separate equality analysis remain explicit. The later CSL
row now refers to both the interval-computation theorem and the retained
source model-checking summary. Its conditions remain present; it introduces
no unsupported exact equality procedure or bit-complexity claim.

Closure: the bounded pass is retained. Any later stronger decision or
complexity assertion needs separate evidence and review.

## Handoff

The two actionable repairs from the first source review are verified. The
remaining source finding is **SF-C2-02, exact-final-journal fidelity**. The
unit must not be marked fully source-admitted while that obligation is
unresolved. Other independent reviews, manuscript output checks and formal
admission are separate gates and are not decided by this report.
