# P16 conditional interventional identification: author return

Root integration: both manuscript files are connected after the zero-support
treatment. Both primary bibliography entries were copied into handbook.bib
and verified there; the now-redundant intake-p16-idc-uai2006.bib was removed.
All of its entry data remain in the canonical bibliography. The handoff
hash below identifies that historical intake, not a missing primary paper.

Date: 8 September 2026 UTC. Block began 14:23:09 UTC; deadline
15:08:09 UTC. The owned manuscript and intake paths were absent at intake.
All writing preceded independent review; no review, scanner, test, build
or manuscript render was run. The complete actual body and annex, including
the final general necessity construction, were read back mathematically.

## Outputs

| File | Extent | SHA256 |
| --- | --- | --- |
| `handbook/parts/p16/conditional-interventional-identification.tex` | 291 lines; conditional semantics, IDC, fourteen results and source boundary | `AFC42F7E491BC5BCC3C7935140043DF425DA1F20EE16FFD8D80E2651F1747FF6` |
| `handbook/annex/p16/conditional-interventional-identification.tex` | 593 lines; fourteen complete proofs | `8E842F1D26044D00E1147021F858D78146EB2E356E702F92A53050A775876C3A` |
| `handbook/bib/intake-p16-idc-uai2006.bib` | 25 lines; two distinct primary entries | `67138CD51381406C03E7B24E443086D0ADC6CE88EBDC79AEDD8EB89548462321` |

The fourteen reciprocal suffixes use body prefix `thm:p16-` and annex
prefix `annex:p16.`: `idc-positive-context`, `idc-root-graph-bridge`,
`idc-rule-two-step`, `idc-exchange-closure`, `idc-termination-soundness`,
`idc-known-denominator`, `idc-response-rooted-failure`,
`idc-parent-root-gadget`, `idc-hedge-scope-counterexample`,
`idc-positive-path-gadget`, `idc-unused-conditioning-bit`,
`idc-terminal-reduction`, `idc-completeness`, and `idc-worked`.

## Verified primary acquisition

Capture folder:
`source/references/shpitser-pearl-conditional-identification-uai2006/`.

The author publication list at <https://bayes.cs.ucla.edu/csl_papers.html>
links the UAI version and the separate addendum. Both PDFs were downloaded
from those actual author links. A default scoped write/TLS attempt failed;
a narrowly scoped escalated download to these exact paths succeeded.

| Primary | Exact readable extent | SHA256 |
| --- | --- | --- |
| `r329-uai-2006.pdf` | 8 pages; 240,945 bytes; complete UAI article and Appendix | `098B12E5792305495533B9B037CED23B87B429223A993EE9F6FD992213BF9CAA` |
| `r329-appendum-2007.pdf` | 2 pages; 47,507 bytes; complete correction and argument | `16149F70F492FF7292F4E916B781112B1D2BBF621F053B6B17658CE2AB4EE8BC` |

Verified URLs:
<https://ftp.cs.ucla.edu/pub/stat_ser/r329-uai.pdf> and
<https://ftp.cs.ucla.edu/pub/stat_ser/r329-appendum.pdf>.

The actual UAI first page names Ilya Shpitser and Judea Pearl, the exact
title, R-329, May 2006, the UAI proceedings edited by R. Dechter and
T. S. Richardson, AUAI Press, Corvallis, and pages 437-444. It is the
author-hosted UAI version with its report header, not asserted to be a
publisher facsimile. Its PDF metadata says created 21 May 2006 and modified
29 May 2007; the latter is not substituted for the publication year.
The separate addendum's actual header names Ilya Shpitser, R-329-APPENDUM,
May 2007. Its metadata creation is 27 May 2007, modification 29 May 2007.

All eight UAI pages and both addendum pages were read as complete extracted
text and primary page images. Primary images are in the old task's
`tmp/pdfs/p16-idc-source/`; they are source-reading intermediates, not
manuscript renders. Research and PDF skills guided this reading and note.
The earlier February 2006 submission and the later 2012 arXiv deposit
were located as distinct records, not substituted for this capture.
A later JMLR appendix was consulted on the web as a proof lead; it was
not acquired or used as an additional theorem premise in this component.

## Complete mathematical scope

The main domain explicitly quantifies over every finite nonempty observed
alphabet family, every possible common strictly positive observed law,
every two compatible models on that family, and all action/conditioning/
response values. All intervention contexts are positive by the proved
indicator-removal argument. A canonical pair-root DAG is used solely for
graph tests; active-walk conversion proves its separation equivalence to
actual latent-root expansions, without replacing their probability models.

The unique maximal exchange set is proved through the ancestral moral
graph. Eligibility is equivalent to absence of a parent in the response
components after deleting the conditioning set. Exchanging an eligible
vertex leaves those components unchanged, proving persistence, order
independence and the simultaneous maximal Rule 2 criterion.

All IDC branches, fixed assignments, termination, successful normalization
and do-calculus derivations are supplied. The original joint can be
unidentified while the conditional is identified; the full positive chain
example proves this. A collider example has an identified marginal response
but different conditional effects, with both conditioning masses 1/2.

The general terminal necessity proof is COMPLETE in the stated positive
graph-uniform domain. It retains the source's two-case split:

- If the conditioning marginal is identified, equality of that marginal
  and conditional would identify the joint, giving the required contradiction.
- Otherwise the existing positive core/relay hedge construction supplies
  a discrepancy in the joint terminal relay bits conditional on the other
  evidence coordinates. Positive product laws are determined by their
  one-coordinate full conditionals, so an unused relay bit has a differing
  conditional probability given all other evidence fields.
- Noneligibility supplies an active path from that evidence vertex, made
  a sink by the Rule 2 graph test, to a response. Separate finite coordinate
  channels copy independent segment bits, use collider exclusive-or signals,
  and transmit those signals to the conditioning set. Conditioning the
  signals to zero produces a nonzero two-by-two determinant. Independent
  private noise, with an explicit determinant bound, makes all observations
  positive while preserving dependence.
- Take this gadget independently in both old models, mask the unused
  evidence bit by exclusive-or with the gadget's sink bit, and omit the mask
  bit itself. Neither omitted coordinate is used elsewhere, so these are
  legal equations on the same graph. Equal full observed laws and full
  positivity survive the common coordinate map. The conditional response
  difference is an explicit fractional-linear expression whose numerator
  is `(t1-t2) times the nonzero gadget determinant`. Rule 2 restores the
  original query and gives its positive conditional countermodels.

Thus IDC, the exact terminal-query hedge criterion, and conditional
do-calculus completeness are proved here. The finite coordinate expansion
is allowed by the graph-uniform quantifier; it does not claim the stronger
unchanged-small-alphabet theorem.

## Corrections and distinct source arguments

The source Appendix Lemma 5 states F is contained in F-prime union X.
The explicit hedge L -> X -> W with X <-> L <-> W and F-prime={W}
disproves that as a general inclusion. The body gives its positive models
and does not use it in the completed necessity proof. The general proof
instead preserves the source's marginal case division and active-path
transmission with the full independent-coordinate construction above.

The 2007 addendum expressly retracts the UAI paper's assertion that Tian's
conditional `cond-identify` algorithm is unsound, attributing it to a
notation misunderstanding. That original assertion is not repeated as
current mathematics. The addendum's distinct conditional-Tian procedure
and proof remain a separate presentation; they are not replaced by IDC
or by the unconditional modified Tian component already written.

## Integration and remaining boundaries

Input these files after their `identification-with-zero-support.tex`
counterparts. Merge both bibliography intake keys. Root owns shared routes,
canonical notation and later consolidated review. New notation includes
the conditional kernel, canonical root DAG, eligibility set E, IDC and its
terminal A/W sets, moral response components, unused relay coordinates,
active-path channel bits and noise, and the two-by-two masking table.

No required positive graph-uniform IDC completeness lemma remains pending.
Additional nonpositive IDC support/completeness, unchanged fixed-small-domain
refinements, sequential-policy identification and the distinct corrected
Tian conditional presentation are not claimed by this component. Existing
zero-support sound joint answers can be normalized only after the actual
post-action conditioning denominator and every exchange context are justified.
