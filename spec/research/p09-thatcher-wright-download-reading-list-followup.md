# Thatcher--Wright downloadable-PDF reading-list follow-up

Date: 2026-09-06, America/Los_Angeles.
The fresh bounded pass began at 2026-09-07 01:02:49 UTC and stopped on
the root's instruction within its five-minute window.

## Result

No exact Thatcher--Wright 1968 article was verified. No target PDF was
saved. The exact title, authors, and printed pp. 57–81 therefore remain
unverified for this pass.

Follow-up identification at 2026-09-07 01:10:51 UTC closed the fourteen
additional generic candidates specified by the root: all are nonmatches.
The root independently identified the four earlier candidates as
nonmatches as well. Details are appended below.

The target remains DOI [10.1007/BF01691346](https://doi.org/10.1007/BF01691346),
Mathematical Systems Theory 2(1), 1968, pp. 57–81.

## Fresh repository checks

Web searches used ThatcherW68, ThatcherWright, generalizedfinite, the
exact DOI, and the full title, restricted where useful to GitHub,
raw.githubusercontent.com, and github.io. Public GitHub repository
searches for the exact DOI and exact phrase “generalized finite
automata” in README files returned zero repositories.

Actual recursive file-tree responses were read for:

- [orlarey/algebra2](https://github.com/orlarey/algebra2): 28 entries,
  no PDFs; its Thatcher/Wright reference is the different 1977
  initial-algebra paper.
- [yuezato/automata_papers](https://github.com/yuezato/automata_papers):
  2 entries, including rewbl.pdf.
- [xamgore/automata-coursework](https://github.com/xamgore/automata-coursework):
  33 entries, including goga.pdf.
- [REMath/literature_review](https://github.com/REMath/literature_review):
  2 entries, no PDFs.
- [realizeme/Seminal-Papers-in-Computing](https://github.com/realizeme/Seminal-Papers-in-Computing):
  README only; its Thatcher mention is the editor attribution for
  Karp's 1972 paper.
- [wcjordan/forester](https://github.com/wcjordan/forester): 119 entries,
  no PDF or target filename match in the checked tree.
- [lancejpollard/computer-science](https://github.com/lancejpollard/computer-science):
  3,057 entries, untruncated. It contains many generic PDF filenames
  under automaton/tree-automaton/tree-language. Neither its tree nor
  the inspected README supplied the target title, DOI, or requested
  filename variants.

Some initial PowerShell JSON-serialization calls failed; those three
tree reads were repeated successfully using plain output. The counts
above come from the successful reads.

## Four downloadable but unverified payloads

The following actual repository paths were found in the last tree.
Their raw.githubusercontent.com URLs returned Git LFS pointer text.
Following the corresponding ordinary public media URLs returned HTTP
200 with the listed lengths:

| Candidate URL | Bytes |
|---|---:|
| [article2 (1).pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-automaton/article2%20%281%29.pdf) | 324,532 |
| [13.pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-automaton/13.pdf) | 5,819,168 |
| [82451792.pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-automaton/82451792.pdf) | 298,337 |
| [82535884.pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-automaton/82535884.pdf) | 1,135,109 |

Their reported content type was application/octet-stream. The search
was stopped before document parsing. Their titles, authors, page counts,
and distribution provenance have not been established. These URLs are
not claimed to be the target, nor are they claimed to be verified
nonmatches. No copy was retained locally.

The preceding paragraph records the state at the first stop. The root
subsequently parsed those four candidates and supplied these identities:

| Earlier candidate | Root-verified identity | PDF pages |
|---|---|---:|
| article2 (1).pdf | Algorithms for Guided Tree Automata | 26 |
| 13.pdf | Efficient Algorithms for Tree Automata, 2019 | 7 |
| 82451792.pdf | Query automata over finite trees, 2002 | 42 |
| 82535884.pdf | Tree Pushdown Automata, 1985 | 16 |

They are now classified as nonmatches on that independently supplied
evidence, rather than on filename inference.

## Identification of the fourteen remaining specified candidates

This was a new, three-minute-bounded identification task, with no
expansion to other repositories or searches. The fourteen specified
media URLs were read directly into memory using Python with UTF-8
output and pypdf. Their page counts and first two pages' extracted
text, supplemented by document metadata, supplied the identities
below. No candidate was written to disk and no page was rendered.

All paths below are relative to the same
[repository branch](https://github.com/lancejpollard/computer-science/tree/make).
Each linked file is its actual public Git LFS media URL.

| Observed candidate | Identified document and authors | PDF pages | Bytes |
|---|---|---:|---:|
| [tree-automaton/10.1.1.164.8383.pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-automaton/10.1.1.164.8383.pdf) | MONA Version 1.2: User Manual — Nils Klarlund and Anders Møller; BRICS NS-98-3, June 1998 | 63 | 615,094 |
| [tree-automaton/10.1.1.61.3611.pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-automaton/10.1.1.61.3611.pdf) | Deterministic Automata on Unranked Trees — Julien Cristau, Christof Löding, Wolfgang Thomas | 12 | 174,722 |
| [tree-automaton/10.1.1.710.9167.pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-automaton/10.1.1.710.9167.pdf) | Tree Search and Quantum Computation — Luís Tarrataca and Andreas Wichert | 25 | 1,179,236 |
| [tree-automaton/10.1.1.757.3530.pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-automaton/10.1.1.757.3530.pdf) | Deterministic Automata for Unordered Trees — Adrien Boiret, Vincent Hugot, Joachim Niehren, Ralf Treinen; GandALF 2014 | 14 | 282,690 |
| [tree-automaton/3133906.pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-automaton/3133906.pdf) | Restricting Grammars with Tree Automata — Michael D. Adams and Matthew Might | 25 | 559,510 |
| [tree-automaton/680-692.pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-automaton/680-692.pdf) | Some Hypergroups Induced By Tree Automata — M. Ghorani and M. M. Zahedi; 2012 | 13 | 192,250 |
| [tree-automaton/mini.pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-automaton/mini.pdf) | HAL cover: Minimizing Tree Automata for Unranked Trees; body: On the Minimization of XML Schemas and Tree Automata for Unranked Trees — Wim Martens and Joachim Niehren | 55 | 613,713 |
| [tree-language/10.1.1.160.7069.pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-language/10.1.1.160.7069.pdf) | A new algorithm for linear regular tree pattern matching — Priti Shankar, Amitranjan Gantait, A. R. Yuvaraj, Maya Madhavan; TCS 242 (2000) | 18 | 132,158 |
| [tree-language/10.1.1.302.4102.pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-language/10.1.1.302.4102.pdf) | The Complexity of Text-Preserving XML Transformations — Timos Antonopoulos, Wim Martens, Frank Neven | 12 | 430,566 |
| [tree-language/10.1.1.44.1393.pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-language/10.1.1.44.1393.pdf) | Locating Matches of Tree Patterns in Forests — Andreas Neumann and Helmut Seidl | 12 | 224,418 |
| [tree-language/10.1.1.91.929.pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-language/10.1.1.91.929.pdf) | An Improvement to Bottom-up Tree Pattern Matching — David R. Chase; title occurs on the second PDF page | 14 | 259,701 |
| [tree-language/82588933.pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-language/82588933.pdf) | Tree algebras and varieties of tree languages — Saeed Salehi and Magnus Steinby; TCS 377 (2007) | 24 | 514,934 |
| [tree-language/Volltext (PDF).pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-language/Volltext%20%28PDF%29.pdf) | New Results on Context-Free Tree Languages — Johannes Osterholzer; Dresden dissertation submitted December 2017 | 240 | 1,675,817 |
| [tree-language/reg.pdf](https://media.githubusercontent.com/media/lancejpollard/computer-science/make/paper/tree-language/reg.pdf) | Regular tree language recognition with static information — Alain Frisch | 12 | 143,682 |

All fourteen have different titles and authors from the target. The
two 25-page files demonstrate why page count alone was insufficient.
Some PDF parsing emitted recoverable object-offset warnings; all
fourteen nevertheless returned page counts and identifying page text.
This was identity inspection, not a claim of complete PDF validation.

The specified repository-candidate list is now exhausted: eighteen
identified nonmatches, counting the four independently parsed by the
root. No exact target was found and no acquisition is claimed.

## Boundary

This was a fresh repository/attachment pass, not a repeat of the earlier
university or archive search. No purchases, accounts, third-party
messages, manuscript changes, tests, builds, or renders were used.
The research skill's note-and-primary-link discipline was used; the
explicit no-new-agents instruction controlled delegation. PDF identity
verification remains necessary before any candidate can be called the
requested article.
