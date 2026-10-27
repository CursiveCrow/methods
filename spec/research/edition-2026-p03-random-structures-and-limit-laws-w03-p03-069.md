# Edition 2026, P3 chapter 40 section 40.6 (packet w03a-p03-069): almost-sure encoding and infinite spectra

## Source intake

- Work: Joel Spencer, *Logic and Random Structures*.
- Version read: the 30-page version hosted at
  https://cs.nyu.edu/faculty/spencer/papers/ircsallsubm.pdf (PDF metadata: title
  `ircsallsubm.dvi`, created 6 July 2007, 30 pages; sections numbered 1-14 without a
  chapter prefix). Fetched in this session with WebFetch on 11 October 2026; the
  bytes (SHA 256 digest b81de4d3a6126e08ab363f6438ab495c343b442a4b03beae7fb8295568bf545c)
  were rendered page by page (pdftoppm) in
  `tmp/agent-scratch/w03a-w03a-p03-069-b1-author/` and read visually.
- Pages read: 4-12 (Sections 2-6: G(n,p), threshold examples, extension statements,
  sparse/safe/rigid, closure, T_alpha, t-generic, generic extension, completeness
  outline), 15-18 (end of Section 7, Section 8 A Dynamic View with f_A and Sp(A),
  Section 9 Infinite Spectra via Almost Sure Encoding, start of Section 10). Page 1
  header for title and author; section-start pages from the text extraction
  (Section 12 starts p. 22, Section 13 p. 25).
- Not read: the printed chapter in the 2007 Springer volume (doi 10.1007/3-540-68804-8),
  where the packet places this material as section 4.9. No printed-version locator is
  used. The reader text states once that it follows the hosted version.
- Bib key: `Spencer2007LogicRandomStructuresAuthor`, copied verbatim from the w03a-p03-067
  intake so the merge deduplicates it. Packet w03a-p03-065 cites the same version under
  `SpencerLRS2007Preprint`; the lead should pick one key at merge.

## What the source gives and what the text does

- Source section 9 (pp. 16-18) is an outline. It derives the Representation Lemma from
  T_alpha (1-Generic Extension plus rigidity of a common neighbour of three vertices) and
  gives a second witness-counting outline that it says needs fleshing out.
- The chapter proves everything directly: K_{3,k} threshold by first/second moment (using
  065's moment lemma), max |N| = k on I_k, EVEN/BIGGER semantics, A* limit values and
  Sp(A*) on [1/3,1), A* not first-order (EF game on complete bipartite B_{3,m}, using
  038's game criterion), a.s. Representation Lemma under l(3 alpha - 1) < 1 with
  1/3 < alpha < 1/2 (conditioning on root edges, binomial tail bounds proved inline,
  independence of witnesses outside N(roots)), the configurations (sparse/safe, rigid),
  the encoding (deterministic direction in every graph, converse a.s.), and the spectrum
  of A on [1/3,1/2).
- Bookkeeping correction recorded in the reader text (def:p03-w03-p03-069-bookkeeping):
  parts have at most ceil(k/4) pairs, which is <= k/3 only for k >= 6 (fails for
  k = 1, 2, 5), and the probabilistic proof needs alpha < 1/2. So f_A is determined only
  on I_k, k >= 6; Sp(A) is determined on [1/3, 1/2) and contains {1/3} and 1/3+1/k for
  k >= 7. Whether 1/2 and 1/3+1/k for k <= 5 are spectral points of A is not decided.
- Source Representation Lemma checked across all I_k: proved a.s. for k >= 6
  (thm:p03-w03-p03-069-representation); for k <= 3 only l = 0 is admissible and it holds
  a.s.; for k = 4, 5 the admissible case l = 1 fails a.s. because some pair has no common
  neighbour when alpha > 1/2 (thm:p03-w03-p03-069-representation-fails, using 065's
  common-neighbour threshold). This is a correction to the source's statement, recorded in
  reader text.
- Distinctness of x1,x2,x3 is not explicit in the source; made explicit with a proved
  warning (repeated triples give unbounded neighbourhoods).
- The source's T_alpha phrasing of the lemma is bridged in prose: an a.s. sentence lies in
  T_alpha given completeness and soundness of T_alpha as asserted at pp. 10-12 (owned by the
  T_alpha packets, not proved here).
- Hella-Kolaitis-Luosto notion and their question are reported as the source reports them,
  explicitly as an open question.

## Existing treatments checked

- finite-model-theory.tex L1-62 (constant-p zero-one law, Rado graph) and
  p09 presentations/n-c-002.tex L100-125 (Libkin limiting theory): countable limiting
  models, not this construction; linked in the Relationships section.
- New concurrent chapters found in the tree but not in the packet's existing list:
  handbook/parts/p03/random-structures-and-limit-laws-w03-p03-065.tex (G(n,p), thresholds,
  moments, dense/sparse/safe, Janson, safe criterion) and -067.tex (constant p, T_alpha
  notions). This chapter links their labels instead of redefining. Neither defines f_A,
  Sp(A), K_{3,k} thresholds, or the encoding.
- Game criterion: thm:p03-w03-p03-038-criterion; game definition def:p03-ef-game.

## Continuation

- Rerun of block 1 (12 October 2026): the online copy was fetched again with WebFetch
  in this session; its bytes have the same SHA 256 digest (b81de4d3...545c) as the scratch copy,
  and pp. 7, 10-12, 15-18 (rendered pages and text extraction) were re-read to check every
  locator in the body. Section start pages confirmed from the text extraction: 2 p. 4,
  3 p. 6, 5 p. 9 (genericity and Generic Extension on p. 10), 8 p. 15, 9 p. 16,
  12 p. 22, 13 p. 25.
- Proofs re-checked line by line (K_{3,k} threshold, max-common, EVEN/BIGGER, A* limits
  and spectrum, EF game, configurations, representation lemma, failure above 1/2,
  encoding, spectrum of A). Changes made: the configurations lemma now cites the
  dense/sparse/rigid/safe definition of 065; the rigidity proof uses Z for the root set
  (R was overloaded with the relation); the B_{3,m} symbol row scope is now the annex
  section label.
- State: body 526 lines, annex 574 lines; unit-compile ok; fused-space check clean;
  check.py --tree shows no finding in this packet's files.
- Open items: (1) the printed Springer 2007 chapter (section 4.9) is neither held nor read,
  so no printed-version locator or content bridge exists; acquisition needed.
  (2) f_A on I_k for k <= 5 (alpha > 1/2) and whether 1/2 and 1/3+1/k (k <= 5) are spectral
  points of A are not decided by the argument.
- Components C001-C008, C010-C015 of ED26-SRC-050-0004 belong to other sections; the unit
  is listed under readonly_units with owner w03-p03-064.
- Block 2 (12 October 2026): the two fused-token guard hits in this note (lines 10 and 73,
  the hash name) were rewritten as "SHA 256 digest"; the same token was removed from the
  return file. All content guards (G8, G9, G11, G12, G14, G15) rerun on the six owned files
  with no hit; fused-space check clean; unit-compile ok; check.py --tree shows no finding in
  this packet's files. The representation-lemma, failure-above-1/2 and encoding proofs were
  re-read (matching split ceil(s/4)+floor(s/4)=s/2 for even s checked; injection split into
  four parts of at most ceil(k/4) pairs checked). No reader-text change was needed.
- Printed version search, this session: one web search for a free copy of the printed
  Springer chapter (section 4.9, front matter shows it starting at printed p. 244, from
  tmp/acquisition/src050/web-springer-frontmatter-renderer.txt) found only catalogue and
  announcement pages; the earlier acquisition run recorded the Springer chapter 4 PDF
  behind access control. The held SRC-050 file
  (source/references/acq-r1-ACQ-2026-10-0472/graedel-2007-fmt-descriptive-complexity-ch3.pdf)
  is Graedel's chapter 3, not Spencer's chapter. Open item (1) above stands: acquisition
  of the printed chapter 4 (pp. 244 onward for 4.9) is needed for a printed-version
  presentation or a proved content bridge.
