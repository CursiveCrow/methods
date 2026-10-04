# Edition 2026 C2: first independent-round source and reference repairs

Date: 7 September 2026. The independent mathematical review passed its scope.
The source and publication-text reviews identified a conflation of the journal
entry's metadata with the report's downloadable body. Source review additionally
identified the missing [0,1] threshold restriction. These are author repairs
pending independent recheck; exact final-journal fidelity is still open.

## Source identity and retained body

The [University of Twente report record](https://research.utwente.nl/en/publications/model-checking-algorithms-for-continuous-time-markov-chains-2/)
identifies the four authors, April 2002 publication, Enschede, the CTIT technical
report series and number 02-10. It separately links the June 2003 TSE article,
volume 29, issue 6, pages 524-541. The report's PDF is not the final body of that
journal article.

The independently inspected 37-page report was copied unchanged from the
reviewer's temporary acquisition to the retained project location
`source/references/baier-haverkort-hermanns-katoen-2002/ctit-02-10.pdf`.
Both copies have SHA256
`4fa36cb3a826a1a62721762063e4d02da02c87343873577053c014b6b5050d74`.
This custody copy changes neither the review's consulted bytes nor its exact
final-journal limitation. The reviewer inspected report pages 1, 4-11, 13-25
and 29-33; no root full-body reading or whole-paper acceptance is inferred.

## Actual repairs

- The 2003 journal bibliography entry now links its own DOI,
  `https://doi.org/10.1109/TSE.2003.1205180`.
- A separate `BaierHaverkortHermannsKatoen2002Report` entry identifies CTIT
  report 02-10 and its verified report URL. The original journal key, title,
  journal, volume, issue, pages, year and DOI remain unchanged.
- The host explicitly identifies the report as a distinct earlier version;
  report locators are not presented as journal locators.
- The CSL grammar now declares rational thresholds in [0,1], matching the
  inspected source signatures and leaving other probability languages intact.
- The introduction expands continuous stochastic logic (CSL), and the later
  summary row links the corrected interval-computation theorem as well as the
  broad cited source result.

The two proved theorem statements and complete annex proofs are unchanged by
these source/lookup repairs. Their structural relocation and mathematical
derivations remain documented in the author's C2 correction note.

## Remaining verification

SF-C2-01/C2-PUB-01 and SF-C2-04 require independent closure checks on the new
snapshot. SF-C2-02, the readable exact final-journal body with verified locators,
remains unresolved. The known report and typeset candidate cannot silently close
that requirement. The source unit and final release remain open while it is
unresolved. No full-book build, render, source-admission record or publication
acceptance was created by this repair.
