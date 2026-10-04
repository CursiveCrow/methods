# C2 independent source-fidelity review

Date: 7 September 2026. Reviewer role: independent primary-source researcher.
Reviewer task: `/root/edition_c2_source_review`. Actual model identifier and
reasoning-effort configuration: unavailable to this reviewer; no claim is made
about a requested or inferred configuration.

## Verdict and scope

**Verdict: FAIL for the source linkage and threshold signature identified below;
UNRESOLVED for fidelity to the exact final 2003 journal manifestation.** The
bounded comparisons that pass remain useful. This is not full source-paper
reconstruction, formal admission, manuscript build acceptance, visual admission,
or publication acceptance.

The review read the actual current LaTeX, the complete new correction annex,
the edition contract, a downloaded primary report body, and selected passages
of a separate author-uploaded typeset body. Other reviewers' outputs and author
verdicts were not consulted. No manuscript was edited, compiled, rendered, or
tested. The only repository output owned and written by this reviewer is this
file. Source PDF pages were rendered for reading because the report's extracted
text was malformed; these are source-body checks, not manuscript rendering.

## Frozen inputs and reading record

Paths below are relative to `C:/Dev/the-methods-of-reason`.

| Input | Actual reading | SHA256 |
| --- | --- | --- |
| `handbook/parts/p09/logic-in-computer-science.tex` | Lines 1318-1587, including the full CTMC/CSL definition, endpoint theorem, model-checking summary, interval computations, timed next, uniformization and comparison table; complexity row 2452-2456. Adjacent context 1181-1235 and the threshold search at 1255 were checked for a possible inherited threshold declaration. | `1eaf705ced9c83e18edd1129f0f0996663840fdfd5b22bee411b871eb3d85dd3` |
| `handbook/annex/p09/csl-corrections.tex` | Entire file, lines 1-82. | `92aeada76892a0dbf271b8002dca189d563ba39c389ebb478be3d438521c42f5` |
| `handbook/parts/p09/presentations/n-x-015.tex` | Lines 141-181, especially the assigned source boundary 147-181. | `29c172d5ba714ea89e99f4272bd4b87aa2b72bc3d305447ba43ede5289c69e08` |
| `handbook/bib/handbook.bib` | Entry `BaierHaverkortHermannsKatoen2003`, lines 2508-2519. | `d5bab1c74ab2b378eaacafe2ce1b313209e71e46a28dd2748ef7c539c5cb7094` |
| `spec/EDITION-2026-CONTRACT.md` | Entire file. | `c9b101ad6bf6bfea5a3e1fbec25cdba81b47667146474861eb1aa00b5dfa1bf3` |

The two assigned content hashes were rechecked near completion and still
matched. The bibliography reconciliation was used only as a candidate-location
index. Its assessment was not used as primary-body evidence.

## Manifestations actually available

**R2002: CTIT technical report 02-10, April 2002.** The University of Twente
has a [separate report record](https://research.utwente.nl/en/publications/model-checking-algorithms-for-continuous-time-markov-chains-2/)
and a [37-page downloadable body](https://ris.utwente.nl/ws/files/268940692/Baier2002model_checking.pdf).
The downloaded PDF is 584,762 bytes, SHA256
`4fa36cb3a826a1a62721762063e4d02da02c87343873577053c014b6b5050d74`.
Its title page and author list were inspected. The temporary local source is
`C:/Users/Crow/AppData/Local/Temp/c2-source-review-4676747b7ba14ec9abbab24a55877523/Baier2002model_checking.pdf`.
The report has readable rendered pages despite a malformed text layer.
Pages actually inspected visually: 1, 4-11, 13-25, and 29-33. Printed and PDF
page numbers coincide. The uninspected pages are not claimed as read.

**J2003-final: required journal manifestation.** Its identity is
Baier, Haverkort, Hermanns and Katoen, *IEEE Transactions on Software
Engineering* 29(6), 524-541, June 2003,
[DOI 10.1109/TSE.2003.1205180](https://doi.org/10.1109/TSE.2003.1205180).
The [separate University of Twente journal record](https://research.utwente.nl/en/publications/model-checking-algorithms-for-continuous-time-markov-chains/)
and Crossref publisher metadata agree on this bibliographic identity. They
were used only for identity, not as substitutes for the body. No exact final
journal PDF was acquired, and no final-journal local hash is available.
DOI/IEEE web access did not expose that body; a direct IEEE PDF-shaped URL
returned HTML. A CiteSeer candidate download timed out. The lead confirmed
that no additional exact-final artifact location was known beyond the
inventoried holdings. No purchase or authenticated acquisition was attempted.

**J2003-candidate: author-uploaded typeset body, exact version unresolved.**
The [public ResearchGate full text](https://www.researchgate.net/publication/3188342_Model-checking_algorithms_for_continuous-time_markov_chains)
identifies author uploads by Joost-Pieter Katoen. Its displayed body has a
masthead of volume 29, number 7, July 2003, and internal pages 1-18. This is
not the bibliographic identity of J2003-final. The public body extraction,
rather than merely its abstract, was read at Definitions 1, 3-6; section 2.3;
Propositions 2-3; the section 3.4 endpoint-closure passage; Theorem 1's
statement; Corollary 1; Theorems 2-3; section 4.3 equations (7)-(8); and
section 6's operator-cost discussion and Theorem 6. These correspond to
internal pages 3-13 and 15, with the title/masthead separately checked.
The underlying PDF downloads failed, so a local PDF hash and a comparison
with J2003-final are unavailable. These passages corroborate a candidate's
claims and numbering; they do not establish final-journal fidelity.

## Findings

### SF-C2-01 - FAIL - Journal bibliography resolves to a distinct report

Location: `handbook/bib/handbook.bib:2508-2519`; all C2 citations using this key.

The entry combines the J2003-final journal identity with R2002's PDF URL.
The two institutional records distinguish these outputs. Their result
numbering also differs, as the locator table below shows. The report URL is
therefore not evidence that the cited journal body has been obtained.

Closure requires separate manifestation records, or an equally explicit
source record that identifies the report as a separate available version and
provides verified correspondence to the journal passages. A corrected URL or
source record must not imply identity by title alone. Updating shared
bibliography belongs to the integrator, not this reviewer.

### SF-C2-02 - UNRESOLVED - Exact final-journal body and locators

Locations: host lines 1334, 1362, 1403, 1454-1469, 1533 and 1558;
`n-x-015.tex:149-158,171-181`.

The current single-number locators agree with J2003-candidate, whereas R2002
uses section-based numbering. The exact final journal was not available for
comparison. The following are actual body locators, not an assertion that the
two versions are identical:

| Subject | R2002, visually read | J2003-candidate, public body read |
| --- | --- | --- |
| CTMC tuple, rates and self-loops | Definition 2.1, pp. 4-5 | Definition 1, section 2.1, internal p. 3 |
| Paths, occupation, cylinder measure | Definition 2.3, pp. 6-7; section 2.3, pp. 7-8 | Definition 3 and section 2.3, internal pp. 4-5 |
| CSL signature and semantics | Definitions 3.1-3.3, pp. 10-11 | Definitions 4-6, internal pp. 5-6 |
| Steady state | Proposition 3.1, p. 14 | Proposition 2, internal p. 7 |
| Unbounded until | Corollary 3.1 and following equations, pp. 18-19 | Corollary 1 and following equations, internal p. 9 |
| Volterra characterization | Theorem 3.1, pp. 16-17 | Theorem 1, internal pp. 8-9 |
| Closed bounded intervals | Theorems 4.1-4.2, pp. 22-23 | Theorems 2-3, internal pp. 11-12 |
| Timed next | Proposition 3.2, p. 15 | Proposition 3, internal p. 8 |
| Uniformization and truncation | Section 4.3, equations (8)-(9), p. 25 | Section 4.3, equations (7)-(8), internal pp. 12-13 |
| Operator costs | Section 6 and Table 2, pp. 29-32 | Section 6 and Theorem 6, internal pp. 14-15 |

Closure requires readable free access to, or a held copy of, J2003-final with
identity, complete required extent, locator and local hash verified, followed
by passage comparison against the frozen manuscript. Alternatively, an
authorized change of the cited manifestation needs separate review; it cannot
silently discharge the original journal obligation.

### SF-C2-03 - PASS - Core CTMC conventions are faithfully distinguished

Location: host lines 1318-1362, subject to SF-C2-02 for final-journal identity.

The rate-map treatment, positive diagonal entries, exit-rate sum, absorbing
zero rows and cylinder-product construction agree with the inspected primary
bodies. Rational rates are expressly identified as the handbook's effective
input convention. The time-divergence restriction is accompanied by its
full-measure qualification. R2002 section 2.3 instead includes convergent
paths and assigns their set probability zero. The handbook's annex supplies
its own Poisson-clock reasoning.

Closure: no change required for this bounded comparison; preserve the
effective-input and full-measure qualifications when resolving SF-C2-02.

### SF-C2-04 - FAIL - CSL threshold signature has an unmarked extension

Location: host lines 1364-1365.

The declaration permits arbitrary rational `q`. R2002 Definition 3.1 and
J2003-candidate Definition 4 restrict the threshold to `[0,1]`. The earlier
PCTL declaration at host line 1255 has that restriction, but the new CSL
definition does not explicitly inherit it. Thus formulas such as
`S_{>=2}[top]` enter the printed CSL grammar without an editorial-extension
marker. Their comparisons are mathematically meaningful, so this is a small
signature/fidelity defect, not a counterexample to the endpoint calculations.

Closure: state `q` rational and in `[0,1]`, or explicitly designate and justify
the broader threshold grammar as a handbook extension. Recheck this narrow
definition and its source convention after correction.

### SF-C2-05 - PASS - Active correction results are separated from source claims

Locations: host 1346-1350, 1407-1452, 1472-1506;
annex 6-38 and 41-81.

The inspected bodies use the prior state at a jump: choose the smallest index
whose cumulative residence time is at least the observation time. The active
handbook expressly chooses right-continuous occupation. Its new endpoint
normalization and interval computations carry their own `proved` links.
The paragraph at 1472-1474 separates their derivation from the cited Volterra
and steady-state results. The annex repeats the proof boundary.

The unconditional endpoint-closure assertion is present in R2002 p. 15 and
J2003-candidate section 3.4, internal p. 8. The handbook's time-zero test,
singleton clauses, and absorbing-state examples directly replace that
assertion in the active mathematics. They are not presented as identical
original wording. This check concerns the active attribution boundary;
the author's separate correction record was not used to prejudge the review.

Closure: no change required to these active distinctions for the bounded
source check. Retain the exact version-specific historical reading and
correction provenance when resolving SF-C2-01 and SF-C2-02. This pass does not
certify every proof obligation in the original paper.

### SF-C2-06 - PASS - Retained computation summaries match available bodies

Locations: host 1454-1536; `n-x-015.tex:149-169`.

The four retained source computations correspond to the available-body
locators above. The active interval formulas retain the required two-stage
restriction for positive lower bounds, evaluate state sets in the original
chain, and give timed next its own calculation. The one-transition example
uses an exponential waiting time and identifies its numerical threshold
boundary. The annex expressly relies on the cited unbounded-until result
rather than claiming to reprove it, and disclaims reproving the Volterra and
steady-state results.

Closure: no change required for this bounded algorithm-attribution comparison;
final-journal correspondence remains SF-C2-02. Neither this pass nor the
annex supplies a full reconstruction of all source proofs and examples.

### SF-C2-07 - PASS - Approximation and complexity boundaries remain explicit

Locations: host 1538-1564, 1577-1580, 2452-2456;
`n-x-015.tex:171-181`.

The uniformization expansion and Poisson-tail criterion agree with the
inspected equations. The manuscript explicitly adds separate error control
for retained-term evaluation and floating-point arithmetic, propagates bounds
through the transient computations, and keeps equality separate. The
comparison and later row preserve these conditions. They do not assert a
polynomial bound in the bit length of all rational inputs or a terminating
equality procedure proved by the displayed numerical method.

The source-cost discussion is sensitive to manifestation: R2002's linear
system term is `N^{2.81}`; J2003-candidate uses `N^3`. Neither figure is
silently inserted into the current row. This difference is another reason
to retain version identity.

Closure: no change required for this bounded boundary check. Preserve the
numerical and equality qualifications. Any later claim of exact decision or
specific bit complexity requires its own supporting theorem and review.

## Handoff

Resolve SF-C2-01 and SF-C2-04 and obtain the source evidence required by
SF-C2-02 before recording a source-fidelity pass for this frozen unit.
The current positive findings concern only the checked correction and
attribution surfaces. Full source acquisition, complete paper treatment,
other reviewers' gates, manuscript output verification and formal admission
remain outside this bounded review.
