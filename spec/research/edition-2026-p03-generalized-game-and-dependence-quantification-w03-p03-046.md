# P3 ch. 36 sections 36.8, 36.9 (packet w03a-p03-046): research note

## Files

- Body: `handbook/parts/p03/generalized-game-and-dependence-quantification-w03-p03-046.tex`
  (chapter "Definable Second-Order Quantifiers and the Comparison of Theories", label tag `p03-w03-p03-046`).
- Annex: `handbook/annex/p03/generalized-game-and-dependence-quantification-w03-p03-046.tex`.
- Bib intake: `handbook/bib/intake-p03-generalized-game-and-dependence-quantification-w03-p03-046.bib` (new key `BaldwinShelah1985`).
- Symbol intake: `handbook/registry/symbols-intake-p03-generalized-game-and-dependence-quantification-w03-p03-046.csv`.
- Insertion (from packet): body after `parts/p03/preservation-abstract-logic` in `handbook/parts/p03.tex` (line 71); annex after `annex/p03/abstract-model-theory-and-lindstrom` in `handbook/annex/p03.tex` (line 9). The lead must add both `\input` lines.

## Source access (2026-10-11)

### Baldwin, ch. XII "Definable Second-Order Quantifiers", Model-Theoretic Logics (ED26-SRC-049-0012)

- Held: only `tmp/edition-2026-catalog-src038/tail-039-068/SRC-049-pageplace-preview-2026-09-09.pdf` (CUP 2017 contents-only preview). No chapter body.
- Tried, Project Euclid (1985 Springer version, listed as open access):
  - `https://projecteuclid.org/ebooks/perspectives-in-logic/Model-Theoretic-Logics/Chapter/Chapter-XII-Definable-Second-Order-Quantifiers/pl/1235417278` -> bot-check page ("Pardon Our Interruption").
  - `https://projecteuclid.org/download/pdf_1/euclid.pl/1235417278` -> bot-check page.
  - same chapter URL with `.pdf` suffix -> bot-check page.
  - `https://projecteuclid.org/euclid.pl/1235417278` -> bot-check page.
  No challenge was attempted or solved. No other legitimate copy was found by web search (publisher sales pages, library catalogues, Perlego only).
- Result on 2026-10-11 (superseded 2026-10-12, see below): the chapter body was not read in any version. Nothing in the reader text presents or paraphrases the chapter.

### Baldwin and Shelah, "Second-Order Quantifiers and the Complexity of Theories", NDJFL 26 (1985) 229-303 (read online)

- URL: `https://shelah.logic.at/files/95815/156.pdf` (Shelah's archive, paper 156 page `https://shelah.logic.at/papers/156/`, labelled "published version (75p)"). Scanned published version, 75 pages, sha 256 `8e37dcc2d1dbf1534cc7bb6d0d60fdf32fac000e784fa160a127eae90af0ae44` (copy served to the WebFetch tool; page images rendered under `tmp/agent-scratch/w03a-w03a-p03-046-b1-author/img/`).
- Pages read: 229-244 (Introduction, Sections 1.1-1.4, 2.1, 2.2, start of 3.1).
- This is a different work from the Baldwin chapter (the research paper the chapter surveys; its p. 232 says an exposition of the four-quantifier argument "occurs in [2]"). It is used as general authority for duty MP-0 only, cited with its own locators, and the reader text says which work is followed and that the chapter is not.

### Hintikka-Sandu 1989 and Vaananen 2007 (N-a-062)

- Searched 2026-10-11: no free legitimate copy of Hintikka and Sandu, LMPS VIII (North-Holland 1989) pp. 571-589 (also reprinted in Hintikka, Paradigms for Language Theory, Springer 1998, paywalled); none of Vaananen, Dependence Logic (CUP 2007): only sales pages, CUP abstracts and the author homepage listing. Not held. Blocked_source; nothing written.


### Baldwin ch. XII, 1985 printing (read 2026-10-12)

- Obtained from Project Euclid open access via the chapter download link
  `https://projecteuclid.org/ebook/Download?urlId=pl%2F1235417278&isFullBook=false`
  (WebFetch returned the PDF; no bot check was met or bypassed). 36-page scan
  (Adobe Paper Capture text layer), sha 256
  `294c67e716604979056228ae0d1eff8e9297d87af5cac677a8e82b76f0a5f93a`, saved under
  `tmp/agent-scratch/w03a-w03a-p03-046-b1-author/euclid/`. PDF page k = printed page 442+k
  (pdf 1 = Part D introduction p. 443, pdf 3 = p. 445).
- Version: 1985 Springer-Verlag printing (Perspectives in Mathematical Logic), as reproduced
  by Project Euclid; the 2017 CUP reissue was not read. New bib key `Baldwin1985DSOQ`; the reader
  text says which version is followed.
- Read: text layer pp. 443-461; page images pp. 445-451 for formulas and locators.

Locators used: p. 445 (Isbell, McKenzie, Shelah Hanf number aleph_{Omega^omega} with
Omega=(2^omega)^+, three-involution device); p. 446 (1.1, notation, exists^{<k});
p. 447 (1.2.1, 1.2.2, T_psi, Q_I/Q_II, monadic and permutational, automorphisms, 1.2.3,
convention); p. 448 (1.2.4, WLOG remark, extended notion, transfer observation, pairing
coalescence); p. 449 (1.2.5, 1.2.6, 1.2.7, 1.2.8, strongly minimal remark); pp. 449-450
(uniform bound); p. 450 (1.2.9, remark on main result, 1.3.1, 1.3.2); p. 451 (1.3.3).

Editorial decisions (block 2):
- Definition 1.2.4 read with theta carrying the guard parameters (as for BS); full-domain
  interpretations named.
- Transfer observation (p. 448) proved for full-domain interpretations only, plus a
  relativized transfer; general case left open (reported).
- Q_mon not<= Q_I proved by counting in a countable elementary substructure instead of the
  source's well-order route (which needs the general transfer).
- Q_1-1 not<= Q_mon: source route (MSO of pure sets constant + Q_1-1 sentence with only
  uncountable models), but the sentence is "no permutation has a single orbit" (via monadic
  quantification inside Q_1-1), not Isbell's group-theoretic sentence.
- Q_II not<= Q_1-1: proofboundary only (Shelah's Hanf computation).
- Three-involution device shown to fail on odd finite orbits of length >= 3; proof uses
  factorization into two involutions.
- Proposition 1.2.7 stated with the hypothesis that psi has an infinite model; the degenerate
  case is shown not interpretable under Definition 1.2.4 (reported as a limitation).
- Codable (1.3.1) read with n >= 2 (n=1 trivializes); 1.3.2 and 1.3.3 reduced to the BS
  coding and equivalence lemmas, noting those proofs do not use absence of finite models.
- Downward LS cited as thm:p03-w03-p03-039-downward-ls (first-order fragment) because
  thm:p02-downward-ls is not on the static route.

## Locators used for BS 1985 (all seen on the page images)

- p. 231: Section 1.1 notation; T_infty; Th(<) (or LO).
- p. 232: classification programme; Shelah's four-quantifier result announced; exposition in [2].
- p. 234: Notation 1.3.1 (spec, Spec_T, bounded).
- p. 235: Definition 1.3.2 (Hanf numbers (i)-(vi), Lowenheim numbers).
- p. 237: Definition 1.4.1, Definition 1.4.2, Lemma 1.4.3, Example 1.4.4 (statement).
- p. 239: Definition 2.1.1.
- p. 240: Notation 2.1.2 (R_phi(A), the four cases, (T,1-1) by permutations of order two).
- p. 241: Definition 2.1.3 (a)-(d).
- p. 242: Definition 2.1.4, Theorem 2.1.5, Theorem 2.1.6 (Shelah), Section 2.2 opening, Definition 2.2.1, Lemma 2.2.2.
- pp. 242-243: Definition 2.2.3.
- p. 243: Lemma 2.2.4 and proof, Corollary 2.2.5, Lachlan remark.
- p. 244: Lemma 2.2.6 and proof, Corollary 2.2.7 and sketch.

## Editorial decisions

- Definition 2.1.3(1) is read with the coding formulas carrying both the fixed parameters and the varying primed parameters (convention def:p03-w03-p03-046-reading). Every proof verifies both inclusions of clause (1) directly, so the source's remark that one inclusion suffices is not used.
- Lemma 1.4.3: proved with the qualifier "whenever the numbers on the right exist"; the proof shows existence of the left-hand numbers from that of the right-hand ones.
- Lemma 2.2.4: proved with compactness (thm:p03-compactness-ultraproduct) plus choice of subsets, not Lowenheim-Skolem; no countability of L is needed. A coded non-surjective injection forces the domain to be infinite, which first-order pi cannot otherwise say.
- Lemma 2.2.2 is derived from Lemma 2.2.4 (pairing => coding with B0=B1=C=M).
- Lemma 2.2.6 and Corollary 2.2.7: proved via a new intermediate lemma (thm:p03-w03-p03-046-equiv-uniform) that builds the involution parameters directly; the source instead appeals to its Corollary 2.2.5. The body states the difference of route.
- Theorem 2.1.6 (four quantifiers): stated only inside a proofboundary attributed to BS p. 242; no proof supplied (the proof lives in Shelah 1973 and the Baldwin chapter, neither read).
- Not presented: Definition 1.3.2 parts other than h^T and ls^T; Examples 1.3.4, 1.3.5, 1.4.4; Definition 2.1.3(b) and (d) beyond a one-paragraph description; Theorem 2.1.5; Corollary 2.2.5; Sections 3-9 of the paper.

## Existing treatments

- Listed in packet: finite-model-theory.tex def:p03-existential-second-order (ESO sentences, not this theory); preservation-abstract-logic.tex sec:p03-dependence-logics etc. (36.9 material; not touched).
- Search of handbook/**/*.tex for second-order quantifier / permutational logic / admits coding / Baldwin-Shelah found no further treatment (pairing-function hits are set-theoretic or recursion-theoretic).

## Continuation

- Block 2 (2026-10-12): Baldwin ch. XII is now read online (1985 printing); section 1 written
  (C001 partial; remainder listed in the return file). C002-C006 not started.
- Next block: read pp. 451-464 (images for formulas) and write section 2 (four-quantifier
  theorem: 2.1 combinatorial lemmas, 2.2, 2.3, 2.4 with decomposition, 2.5/2.6 alternate routes).
  Then sections 3-6 (pp. 465-477). Remaining C001 items: general transfer, Feferman-Vaught claim
  of p. 446, well-order route, extended interpretation notion.
- N-a-062-* (Hintikka-Sandu 1989, Vaananen 2007) remain blocked_source from the 2026-10-11
  search; not re-searched in block 2.

- Block 3 (2026-10-12): fixed the two G8 guard hits (sha 256). Re-opened the local copy of the
  Project Euclid download (same sha 256 as above) and read the text layer pp. 443-477.
  C001 items closed or narrowed:
  - (d) theta_0-modification remark (p. 448): thm:p03-w03-p03-046-b-normal; the construction adds
    a test conjunct to theta_0 and changes guard and coding formula with it (stated in body).
  - (e) well-order claim (p. 449): thm:p03-w03-p03-046-b-wellorder; source-route proof of
    Q_mon not<= Q_I added to annex b-distinct, via thm:...-b-qi-normal (every interpretation in
    Q_I can be made full-domain: finite list of pattern formulas + default trick) and the transfer.
  - (b) transfer: extended to L_{kappa lambda} and to the extended (T1,Q)<=(T2,Q) notion (read as:
    guard, domain, coding, one formula per relation symbol; models of T1 obtained up to isomorphism);
    proved for full-domain interpretations and for every interpretation into Q_I. General case open.
  - (c) Hanf preservation: thm:...-b-hanf for the same two cases; general case open. Reason recorded
    in the body: the domain can be small in large models; Baldwin's section 4 (pp. 470-471)
    addresses this with strong semantic interpretation (|M*| computable from |M|).
  Locator added: pp. 470-471 (section 4, Definition 4.2 condition on |M*|), seen in the text layer.
- Next block: C004 and C003 are the shortest (pp. 465-472); C004 Lemma 4.5 needs the free-union
  (Def 3.7) and preservation theorem 3.5, so write section 3 first, then 4. Then C005, C006, and
  section 2 (longest, pp. 451-464). Check page images for formulas before writing each.

- Block 4 (2026-10-13, b2 author run): re-opened the local Project Euclid copy (sha 256
  294c67e7...93a, unchanged); rendered and read page images pp. 465-477 (pdf 23-35) and p. 446.
  Written:
  - C001(b): new thm:...-b-full-domain (part 1: guard parameters with |domain| = |A| exist for
    every interpretation, via downward LS and (F1); part 2: if Q_1-1 <= Q_phi full-domain, every
    interpretation into Q_phi can be made full-domain, via three coded involutions giving a
    bijection A -> domain) and thm:...-b-transfer-general (transfer + Hanf for targets Q_1-1,
    Q_inv, Q_perm, Q_II, and Lemma 1.2.9 targets). Composition of full-domain interpretations
    proved inside annex b-full-domain. Still open: targets that interpret neither Q_1-1 with
    full domain nor are Q_I (by the unproved classification, those bi-interpretable with Q_I
    or Q_mon); the argument breaks because subsets give no bijection A -> domain.
  - C001(c): thm:...-b-fv (disjoint unions and direct products of unary structures; explicit
    reduction sets; uses the n-similarity Claim of annex b-mso-sets).
  - C004 (partial): new section sec:...-b-comparison: Def 4.1 (def:...-b-syntactic) with the
    Turing-degree remark proved (thm:...-b-turing), Def 4.2 (def:...-b-semantic; printed
    "models of T_2 onto the models of T_2" read as models of T_1), Def 4.3 + Notation 4.4
    (def:...-b-bounded), Gurevich-Shelah boundary reported. Not written: Lemma 4.5 proof,
    Theorem 4.6, transitivity of B, the H_II-not-second-order-bounded argument. Note for the
    next block: "second-order definable function" is not defined in the chapter; transitivity
    of B needs f monotone (replace f by its running sup); the H_II argument as printed needs
    HW (or the bound) second-order characterizable, which the chapter does not show.
  - C006 (writable part): extension list, Def 6.2 (def:...-b-expressible), proofboundary
    def:...-b-shelah-results with Theorems 6.1 and 6.3 statements, many-models remark.
    Baldwin's locators into Shelah [1983c] (p. 53, pp. 48-57) deliberately not copied.
  Locators added: pp. 446, 466, 468, 470, 471, 472, 476, 477.
- Next block: C003 (Section 3, pp. 465-470: Def 3.1, Lemma 3.2, Def 3.4, Thm 3.5, Cor 3.6,
  Def 3.7). Def 3.4(ii) quantifies over sequences of length < |A*| and kappa(alpha,|W|) of 3.5
  is unspecified: fix exact readings before proving. Then C004 Lemma 4.5 / Thm 4.6 (need 3.5 and
  free unions), then C005 (pp. 472-476; Lemma 5.1.1 and Thm 5.1.6 proofs are in BS 1985 Ch.
  VIII/VII, available on Shelah's archive, pages beyond 244 not yet read), then C002
  (pp. 451-465).
