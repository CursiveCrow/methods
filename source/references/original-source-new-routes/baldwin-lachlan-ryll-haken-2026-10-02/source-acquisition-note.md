# New institutional/selected-paper routes: Baldwin--Lachlan, Ryll-Nardzewski, Haken

Date checked: 2 October 2026 UTC. This is a source-only follow-up to the existing acquisition notes, not a manuscript revision or proof reconstruction. No target original body was qualified in this block. No original-body hash, original-page reading, or source-completion credit is claimed.

The preceding notes read before new work were `spec/research/p03-baldwin-lachlan-source-note.md`, `spec/research/p03-ryll-nardzewski-source-note.md`, and `spec/research/p07-haken-source-note.md`. Their Cambridge/JSTOR/closed-RCIN/publisher-challenge failures were not retried. All manuscript files, the protected six-pair geometry bridge, intakes, shared records, drivers, and statuses were left untouched. The research workflow was used by the already delegated researcher; no child, contact, purchase, credential/login, CAPTCHA action, or restriction bypass occurred.

## Required originals, unchanged

| Canonical identity | Required original extent | New original body acquired | Body hash |
| --- | --- | --- | --- |
| `BaldwinLachlan1971`: J. T. Baldwin and A. H. Lachlan, *On Strongly Minimal Sets*, JSL 36(1), 1971, DOI `10.2307/2271517` | Printed 79--96; eighteen pages | No | None |
| `RyllNardzewski1959`: Czeslaw Ryll-Nardzewski, *On the Categoricity in Power* \(\leq\aleph_0\), *Bulletin de l'Academie Polonaise des Sciences, Serie des sciences mathematiques, astronomiques et physiques* 7, 1959 | Printed 545--548; four pages | No | None |
| `Haken1985`: Armin Haken, *The Intractability of Resolution*, TCS 39, 1985, DOI `10.1016/0304-3975(85)90144-6` | Printed 297--308; twelve pages | No | None |

These identities were checked against the preserved canonical bibliography. No later exposition, original author's differently dated thesis, journal review, or revised version was substituted.

## Concrete new routes and their results

1. **Berkeley's institutional Logic Library collection.** The [collection page](https://logic-library.berkeley.edu/) explicitly describes a physical collection in the Alfred Tarski Room, 727 Evans Hall. It lists Baldwin--Lachlan's *On Strongly Minimal Sets* with the year **1969**, but the entry is plain table text with no article download link. It also lists a Ryll-Nardzewski publication list, not the target four-page paper. Thus this is a genuine new institutional holding lead, but neither a downloadable body nor evidence that the listed 1969 item is the exact 1971 publication. Its date/version must not be silently collapsed into the target. Full HTML retained as `berkeley-physical-logic-library.html`.

2. **CMU-HoTT's selected-paper archive.** The actual [Scott repository](https://github.com/CMU-HoTT/scott), described by its public repository metadata as *Selected Papers of Dana S. Scott*, was inspected through its observed `main` branch [recursive tree API](https://api.github.com/repos/CMU-HoTT/scott/git/trees/main?recursive=1). Its enumerated PDF assets are Scott papers; none is one of these three target originals. The API JSON is retained as `cmu-hott-scott-tree.json`. This finding is scoped to the inspected tree, not a claim about every institutional GitHub archive. Scott's already acquired paper was not downloaded again or reassigned as a substitute.

3. **Wroclaw's Ryll-Nardzewski Center.** The [institutional legacy page](https://crn.pwr.edu.pl/en/ryll-nardzewski-center/legacy) provides biographical material and references, including a linked memorial item. Its observed links did not supply the 1959 categoricity paper. No memorial or other Ryll-Nardzewski paper was substituted. Full HTML retained as `wroclaw-ryll-center-legacy.html`.

4. **A distinct South Carolina course archive.** The [MATH 762 archive](https://people.math.sc.edu/mcnulty/762/), distinct from the previously checked `modeltheory/` course page, was reached from an observed institutional lecture-note URL. Its actual page lists the course's model-theory text plus Hodges, Henson, Simpson, Weiss--D'Mello, Pillay, Bledin, and Bell notes. It does not link the Ryll-Nardzewski unbound insert as a separate original scan. The complete page is retained as `south-carolina-762-course.html`. No course-note proof was promoted to 1959 original-body credit.

5. **RWTH Aachen proof-complexity seminar.** The [public WS 2022/23 page](https://logic.rwth-aachen.de/Teaching/SeminarProofComplexity-WS22/index.html.en) assigns the Haken topic but its actual Haken citation hyperlink points to the same ScienceDirect article route already known. The public page also directs current materials to Moodle; no login or restricted course area was entered. The publisher link was **not retried**. Full HTML retained as `rwth-proof-complexity-course.html`.

6. **Jakob Nordstrom's Copenhagen course archive.** The [CoCo 2023 course page](https://jakobnordstrom.se/teaching/CoCo23/) provides lecture notes and a Haken reference, but that article hyperlink again points to the previously known ScienceDirect route. The page explicitly distinguishes lectures from the original papers' proofs. The modern notes were not treated as an original scan, and the publisher link was **not retried**. Full HTML retained as `nordstrom-coco23-course.html`.

7. **University of Toronto reading-group archive.** The [group's page](https://www.cs.toronto.edu/~ozan/cpgroup/) identifies the exact Haken paper for the 17 October discussion, but its observed hyperlink is an old `pdn.sciencedirect.com` MiamiImageURL publisher link, not a Toronto-hosted PDF. That publisher endpoint was **not followed or retried**. The course folders reached from observed Pitassi lecture PDFs at `https://www.cs.toronto.edu/~toni/Courses/Proofcomplexity/` and `https://www.cs.toronto.edu/~toni/Courses/PvsNP/` both returned HTTP 403; no guessed article filename or restricted directory request followed. Reading-group HTML retained as `toronto-reading-group.html`.

8. **A promising-looking institutional `hak85.pdf` is not Haken1985.** Search returned the actual [IIT Kanpur PDF](https://www.cse.iitk.ac.in/users/prsingh/misc/hak85.pdf). It downloads without restriction and is a readable **six-page** PDF. The first page, inspected as both extracted text and a rendered image, identifies speaker/scribe **Pranjal Singh**, date **27 June 2022**, and a reading-group lecture titled *PHP requires exponential-size Resolution proofs*. The first page says it covers the first two sections of the publication; it does not bear original printed pages 297--308. It is therefore **rejected as a target body**, not an acquisition success. The file is deliberately named `iit-kanpur-2022-summary-not-haken1985.pdf`, with identity-inspection image `iit-kanpur-summary-page-1.png`. Its PDF metadata reports creation/modification in 2023, consistent with a later compilation, not the original 1985 typesetting. Only source-identity inspection was done; its mathematics was not adopted or used to edit the manuscript.

9. **Other bounded discovery failures.** The Harvard Boney course folder reached from the observed `spring16/144-modeltheory-notes_02_05_2016.pdf` URL returned HTTP 403, not a listing. A PhilPapers search listing's advertised download alternatives could not be resolved into a verified article/body locator in normal access; no download-alternative count was credited as a body. An Internet Archive advanced-search API request for the Polish bulletin title ended with a remote transport closure, so it supplied neither a result inventory nor a body; this is not reported as zero catalogue matches. Narrow primary/institutional searches and repository searches otherwise returned bibliographies, later papers, lecture notes, or irrelevant filename matches. Those results were not downloaded as supposed originals. No unchanged challenge route was retried.

## Retained captures and SHA-256

All files below are in this same disjoint source directory. **Except for the explicitly rejected 2022 lecture, they are catalogue/course/metadata captures, not PDF article bodies.** A hash authenticates the retained object; it does not change that object's standing.

| File | Bytes | SHA-256 | Standing |
| --- | ---: | --- | --- |
| `berkeley-physical-logic-library.html` | 606505 | `5fa52b755d67e5c798b3cfcf6b6c5e1484160805c1aeb8964b7630bec74df171` | Physical holdings list; 1969 Baldwin--Lachlan entry has no PDF link |
| `cmu-hott-scott-tree.json` | 9693 | `b4be0d0ac08f5f8b28cf935ec5faa87d333feae6ca6391c02fb30cd6d76a58ee` | Actual Scott repository asset inventory; target originals absent |
| `wroclaw-ryll-center-legacy.html` | 147173 | `d2a51faa697763204511468692f8d1ac376d18facfa0c11759bea218062cb986` | Institutional legacy page; no target scan link |
| `south-carolina-762-course.html` | 3535 | `b5bc56dad653337ddd70c778f64fb1b586ba8b36366e3f0de78f68ad13963c64` | New course archive listing, not original insert |
| `rwth-proof-complexity-course.html` | 25019 | `b400340cf4596726ba4789a00db6ed69e08128c0b92dcef2e1b5a0575fd50306` | Public course citation, same publisher destination |
| `nordstrom-coco23-course.html` | 29732 | `f65bec614890279ebedf7fc943d9dec02231a2c298b7e2583d764ee7a74c4317` | Course page; notes and original paper explicitly distinct |
| `toronto-reading-group.html` | 23907 | `fcb001cec049fe1a5c44e6c4afb437d888b9124dd3110161c0e55754d8f427db` | Reading list; link is old publisher endpoint |
| `iit-kanpur-2022-summary-not-haken1985.pdf` | 185471 | `f2f4d9a07e3a9e04ef86c97c1389ddaedefd9de1ba576e4053132c6de6f81ee8` | Six-page 2022 lecture; rejected as original twelve-page Haken1985 |

## Result and next useful dependency

This block adds concrete new-route evidence and one visually qualified **negative candidate**, but zero original bodies. The exact source gaps remain: Baldwin--Lachlan1971 79--96, Ryll-Nardzewski1959 545--548, Haken1985 297--308. No claim of universal unavailability or impossibility follows from these bounded checks.

A future acquisition attempt should begin only from a genuinely new observed original-scan link, a qualified author/institutional deposit, or an authorized source copy provided by the user. The physical Berkeley listing is a possible lead if the user independently has authorized access, but this block does not authorize contacting the institution or convert the 1969 holding into the 1971 published version. Repeating the inspected course pages, unchanged publisher challenges, or the rejected `hak85.pdf` would not address the missing-body dependency.
