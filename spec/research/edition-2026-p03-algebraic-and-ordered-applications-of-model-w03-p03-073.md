# Research note: P3 41.1 (packet w03a-p03-073), Hodges 1993 Appendix A and Eklof 1985 Ch. XI

Label tag: `p03-w03-p03-073`. The owned body and annex files are NOT written. Every component
is a source-specific reconstruction, and no legitimate copy of either source body could be read
in this session. Under A3 and A13 no placeholder, outline or stub is written for an unread source.

## Source access log (block 1, 2026-10-11)

### SRC-049 / ED26-SRC-049-0011: Eklof, "Applications to Algebra", Ch. XI of Barwise and Feferman (eds.), Model-Theoretic Logics
- Held: `tmp/edition-2026-catalog-src038/tail-039-068/SRC-049-pageplace-preview-2026-09-09.pdf`
  (2017 CUP publisher preview, 92 pages). It has the contents only for Ch. XI (reading.txt lines
  449-457: section 1 p. 424, 2 p. 426, 3 p. 428, 4 p. 431, 5 p. 434, 6 p. 437, 7 p. 441). The
  preview contains no Ch. XI body (grep for "locally finite" and "Lefschetz" hits only the contents).
- Project Euclid 1985 open-access version (chapter pl/1235417277): WebFetch of the chapter page
  returned an Incapsula bot-detection interstitial ("Pardon Our Interruption"). curl of
  `.../pl/1235417277.pdf`, `projecteuclid.org/download/pdf_1/euclid.pl/1235417277` and
  `projecteuclid.org/euclid.pl/1235417277` each returned the same 1.1 kB Incapsula JavaScript
  challenge page, not the PDF. The bot check was not circumvented.
- Cambridge Core 2017 chapter (doi 10.1017/9781316717158.016, pp. 423-442): "Get access" or
  purchase only; not open access.
- Internet Archive `isbn_0387909362` (1985 Springer): collections inlibrary and printdisabled,
  that is, login-gated lending; not used.
- Author page webapps.math.uci.edu/~peklof/peklofv.html: three lecture PDFs (Padua 2006,
  Barcelona 2006, Stanford 2009), not the chapter. WebSearch (standard and extended) and the
  OpenAlex API found no other legitimate copy of any version.
- Result: blocked_source for C001 to C007 in this session. Unblocking action for the lead: a
  human download of the open-access Project Euclid PDF (pl/1235417277, 1985 Springer pagination,
  pp. 423-441) into the held-sources registry. The chapter is then writable as the 1985 version.

### SRC-048 / ED26-SRC-048-0013: Hodges, Model Theory (CUP 1993, EMA 42), Appendix: Examples, pp. 653-715
- Held: the contents page (`SRC-048-gbv-contents-2026-09-09.pdf`) and the author corrigenda
  (`SRC-048-hodges-corrigmt-2026-09-09.pdf`) only; no appendix body.
- Cambridge Core chapter page (doi 10.1017/CBO9780511551574.015): paywalled ("Get access").
  WebSearch found no author preprint, open archive or other legitimate version.
- Result: blocked_source for C001 to C006.

## Source access log (block 1 rerun, 2026-10-12)
The task text states that Ch. XI is writable from the open-access 1985 Project Euclid version.
Re-checked in this session; no legitimate copy was reachable:
- held-sources.json: no Eklof / pl/1235417277 entry; SRC-049 is held only as the 2017 publisher
  preview (contents, no Ch. XI body). No file under source/references matches.
- WebFetch of the Project Euclid chapter page
  (projecteuclid.org/ebooks/perspectives-in-logic/Model-Theoretic-Logics/chapter/Applications-to-Algebra/pl/1235417277)
  and of its .pdf URL: both return the Incapsula "Pardon Our Interruption" bot-detection page.
  The bot check was not circumvented (no real-browser JS challenge pass, no mirrors of the PDF).
- Cambridge Core 2017 chapter page: "Book purchase", not open access.
- Internet Archive advancedsearch: only isbn_0387909362 (inlibrary/printdisabled lending, login-gated).
- WebSearch (extended) found a whole-book PDF self-hosted by freecomputerbooks.com and a
  vdoc.pub mirror. Neither is the publisher, an open archive, the author or an institution;
  vdoc.pub is a shadow library and the freecomputerbooks copy has no stated provenance or
  licence. Neither was opened.
- Hodges 1993 Appendix: WebSearch again found only the paywalled Cambridge Core chapter page.

Unblocking action for the lead (unchanged): a human download of the Project Euclid open-access PDF
of Eklof Ch. XI (pl/1235417277, 1985 Springer pagination, pp. 423-442 per the Project Euclid
listing) registered in held-sources.json; Hodges 1993 Appendix pp. 653-715 needs a licensed copy.

## Existing treatment search (A9)
The packet `existing` list is empty. A route search for Eklof Ch. XI and Hodges App. A material
found no treatment. Only unrelated nearby material exists: the Birkhoff subdirect representation
(handbook/parts/p10/subdirect-products.tex:101-141), ACF and RCF quantifier elimination and model
completions in P3, and DLO. None reconstructs the source sections.

## Source access log (block 2, 2026-10-12)
The block 2 task asked for the G10 unit-compile failure to be fixed first. That failure comes from the owned
body and annex files not existing. They do not exist because every component is a source-specific
reconstruction whose source body is not legitimately readable. Re-checked in this block:
- held-sources.json: no new entry for Eklof Ch. XI or Hodges 1993 Appendix A (grep for eklof,
  1235417277, hodges, model-theoretic). SRC-048 is still held only as the contents page and the corrigenda.
  SRC-049 is still held only as the 2017 publisher preview, which has contents and no Ch. XI body. No held
  general authority on the model theory of modules or abelian groups was found (no Prest, Ziegler, Baur,
  Szmielew, Marker or Tent-Ziegler file).
- WebFetch of the Project Euclid chapter page (pl/1235417277): the bot-detection page again ("flagged as a
  bot", enable cookies/JavaScript). curl of the chapter .pdf URL: HTTP 200 with 1162 bytes, which is the
  same challenge page and not a PDF. The check was not circumvented.
- WebSearch: only the Cambridge Core 2017 chapter landing pages (purchase access) and the author page
  (lecture PDFs, not the chapter). No legitimate copy of any version.
- Hodges 1993 Appendix A: still no legitimate copy. The Cambridge Core chapter is paywalled.

Decision for G10: the owned .tex files are again not created. Under A13, a file that contains only
the toc line and a section heading, or a general modules/abelian-groups treatment written from other
authorities in place of the sources, would be a stub or a substitute. The failure conditions of
both units say a different textbook substituting for the source counts as failure. The G10 guard cannot pass until a source body is held.

## Existing treatment search (A9, block 2 additions)
Two existing treatments that the packet's `existing` list does not include:
- handbook/parts/p03/resplendence-and-atomic-compactness.tex lines 160-178: pp formulas, atomic
  compactness, pure extensions (def:p03-resplendence-purity). This is relevant to Hodges A.1 (modules) and
  Eklof section 4 (abelian groups, pure-injectivity).
- handbook/parts/p02/propositional-languages-valuations-and-truth-functions-w02c-p02-003.tex line 2395:
  a proofboundary that records Szmielew's decidability of abelian groups as unproved there. This is relevant to Hodges
  A.2 and Eklof section 4. A later treatment should link to both.

## Block 2 rerun (2026-10-13): general section region written

Task: the assessment gap US-1 (no body/proof region for 41.1) and guard G10 (owned body file missing).
Source access re-checked first: curl of the Project Euclid PDF of Eklof Ch. XI (pl/1235417277.pdf)
again returned a 1154-byte HTML bot-check page (not circumvented). held-sources.json and
source/references still hold no body of Hodges 1993 App. A or Eklof Ch. XI, and no general
authority on the model theory of modules (searched citations/ and source/references/ file names
and SOURCE.md files for eklof, hodges, prest, ziegler, baur, szmielew, abelian, module).

Decision: the 13 source-specific components stay blocked_source. Section 41.1 itself
("Modules, abelian groups, and their definable structure") is a general topic, so a general
reference treatment was written from two legitimately accessible online authorities read in
this session (A3, general content). It does not present itself as, and is not, a
reconstruction of Hodges App. A.1-A.6 or Eklof XI.1-7; the reader text names neither.

Online sources read (2026-10-13):
- Prest, M., "Model Theory of Modules", survey dated 4 September 2020, author page
  https://personalpages.manchester.ac.uk/staff/mike.prest/ModThModsArticle.pdf (HTTP 200,
  application/pdf, 449150 bytes). Read: contents, Sections 1-7 and the start of Section 8.
  Locators used: Sec. 2 (language L_R, right modules, pure embeddings replace elementary
  ones), Sec. 3 (pp formulas, Lemma 3.1, invariants statements, |phi(M)/psi(M)|, pp formulas
  over Z of the form p^n | x p^m citing his 1988 book), Theorem 4.1 and the paragraph after it
  (definable sets), Theorem 5.1 (QE iff von Neumann regular; stated, not proved here),
  Sec. 6 and Theorem 6.1(i) (stability count |A|^kappa; Z superstable not t.t.), Sec. 7
  (axiomatization by invariants; pp commutes with direct sums and products; |phi/psi|).
- Kuber, A., "Grothendieck Rings of Theories of Modules", arXiv:1302.4229v1 (18 Feb 2013),
  https://arxiv.org/pdf/1302.4229. Read: Section 2.5 (Lemma 2.5.3, Definition 2.5.4,
  Theorem 2.5.5 attributed to Baur 1976, Theorem 2.5.6, Lemma 2.5.7, Lemma 2.5.8 Neumann's
  lemma citing Prest 1988 Thm 2.12), Section 3.1 start, reference list.
- Not read (not cited): Baur 1976, Prest 1988 book, Ziegler 1984, the Novak 2023 Charles
  University thesis (dspace.cuni.cz returned HTTP 429 to both WebFetch and curl).

All proofs in the annex were written for the handbook (no source supplies them in the pages
read): pp-subgroup lemma, invariant sentences, Neumann's lemma (two-claim proof), one-variable
extension step (Neumann plus inclusion-exclusion count of D-cosets), separation criterion by
compactness, pp-elimination via aleph_0-saturated extensions and back-and-forth, invariants
criterion for elementary equivalence, definable sets, direct sums/products, lambda-stability for
lambda^{|R|+aleph_0}=lambda, Q-vector spaces example, and the limits theorem (invariant
sentences needed; 2Z in Z not qf-definable).
Cross-references use active inherited anchors thm:fol-compactness, thm:saturated-extension,
thm:saturation-homogeneity (the p02/p03 editorial duplicates thm:p02-fol-compactness and
thm:p03-saturated-extension are outside the build closure and were reported dangling).
Existing treatments linked (A9): def:p03-resplendence-atomic, def:p03-resplendence-purity,
thm:p03-resplendence-positive-maps (used for homomorphism preservation instead of reproving),
def:p02-w02c-p02-003-theories-boundary (Szmielew, still unproved; the warning says so),
def:p03-stability-spectrum.

Symbol overlap known: Inv(M;phi,psi) follows Kuber; Prest's |phi/psi| is mentioned only in prose.
The sibling section 41.2 (w03-p03-074) says the Hodges appendix and Eklof chapter accounts
"belong to the preceding section"; 41.1 does not contain them (blocked_source). That sentence in
the sibling file may need adjusting by its owner or the lead.

## Continuation
- Block 1 (both runs, 2026-10-11 and 2026-10-12) and block 2 first run (2026-10-12): no reader text; all 13 components blocked_source.
- Block 2 rerun (2026-10-13): owned body handbook/parts/p03/algebraic-and-ordered-applications-of-model-w03-p03-073.tex
  (375 lines) and annex (572 lines), intake bib (2 keys) and symbol intake (7 rows) written. Unit compile ok;
  check.py shows only bib-key findings for the two intake keys. Insertion: body after
  parts/p03/qe-categoricity-games-supplement (p03.tex line 68), annex after annex/p03/feferman-vaught-composition
  (annex/p03.tex line 7).
- Still open: the 13 source-specific components (Hodges 1993 App. A.1-A.6; Eklof 1985 Ch. XI sections 1-7) need
  their source bodies. Unblock: human download of the Project Euclid open-access PDF of Eklof Ch. XI
  (pl/1235417277) into held sources; a licensed copy of Hodges 1993 pp. 653-715. When held, the A.1/A.2 and
  XI.4 reconstructions should extend this section (link its pp-elimination and invariants results) rather than
  duplicate them.

## Author correction, 2026-10-26

The arbitrary-product assertion explicitly assumes Choice, matching the witness
selection in its existing proof. The direct-sum assertion and finite product
index formula do not require it. The invariant comparison is now described as
a structural criterion, with its additional effectiveness requirements stated;
an infinite list of invariant comparisons is not a terminating algorithm. A
missing alignment row break in the pp-type extension proof was repaired.

The pp-subgroup, finite-coset-cover, Boolean separation, pp-elimination and
stability arguments were reviewed, including the use of saturated extensions.
The scoped TeX Live build succeeded through biber and three pdflatex passes,
producing 21 pages. Twelve overfull warnings remain, predominantly headings and
long inline expressions. The revised direct-product statement page was visually
inspected. This bounded author review is not an independent correctness verdict
for the complete source allocation and changes no acceptance or coverage ledger.

