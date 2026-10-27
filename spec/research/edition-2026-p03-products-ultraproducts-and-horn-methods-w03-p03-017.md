# w03a-p03-017 research note (P3 ch. 27, sections 27.1-27.4)

Label tag: `p03-w03-p03-017`. Owned body: `handbook/parts/p03/products-ultraproducts-and-horn-methods-w03-p03-017.tex`; annex: `handbook/annex/p03/products-ultraproducts-and-horn-methods-w03-p03-017.tex`.

## Sources opened in this session

- Burris and Sankappanavar, *A Course in Universal Algebra*, Millennium Edition (2012 update), held file `citations/Burris and Sankappanavar - A Course in Universal Algebra (2012, Millennium Edition, 2012 update).pdf` (listed in held-sources.json). Read: Ch. V Def. 1.4 (p. 192), direct products and the Horn definition before Exercise 29, Exercises 29-32 (p. 204), section 2 Defs 2.1-2.5, Lemmas 2.2 and 2.6, Theorem 2.7 (pp. 205-210), Def. 2.8 (p. 210). Cited as `BurrisSankappanavar2012` (existing key; its bib note claims page alignment with 1981, but the pages seen here are the 2012 file's own; only 2012 locators are used).
- The held acquisition `source/references/acq-r1-ACQ-2026-10-0066/...burris-sankappanavar-1981...pdf` (author re-typeset edition, not the GTM printing) was also opened: same text, different pagination (Ch. V section 2 at pp. 234-239). Not cited, to avoid mixing versions.
- Shelah 1971, Israel J. Math. 10, pp. 224-233, held `source/references/acq-r1-ACQ-2026-10-0505/shelah-1971-elementarily-equivalent-isomorphic-ultrapowers.pdf` (scan of published pages). All ten pages read as images. Cited as `Shelah1971Ultrapowers` with page locators 224-232.
- Not used: Keisler 1961 Indag. Math. is now held (`source/references/acq-r1-ACQ-2026-10-0223/ACQ-2026-10-0223.pdf`, publisher version) but was not read in this block (time). Hodges 1993 body and Bell-Slomson 1969 are not held (only Hodges corrigenda and contents).

## Existing treatments found (A9)

- Statement of Shelah's theorem, mu lemma, converse (comparison item 2), index bound: sibling packet w03a-p03-018 file `handbook/parts/p03/products-ultraproducts-and-horn-methods-w03-p03-018.tex` (not in this packet's existing list; being written concurrently). This note's body links to its labels (`thm:p03-w03-p03-018-shelah`, `-mu`, `-notation`, `-comparison`, `-worked`, `sec:p03-w03-p03-018-shelah-ultrapowers`, annex `sec:p03-w03-p03-018-annex`) rather than restating them; dependency: those labels must stay.
- Reduced products over an ideal: `def:p03-fv-reduced-standing` (feferman-vaught-composition.tex); direct product `def:p03-fv-product`. Linked, not duplicated (the Horn section needs the filter form with equality congruence, so it gives Burris-Sankappanavar's definition and states the identification).
- Horn syntax in Part 2: `def:p02-w02b-p02-031-krom-horn`; linked in the conventions.

## Presentation decisions (reader-side remarks recorded in def:p03-w03-p03-017-shelah-reading)

- H^i_gamma read as a set of pairs: Shelah's Lemma 5 output in Case IV could already be in Dom H (and in Case III a new b could already be in Range), which would break "function". The induced class map is still a bijection by condition 3 for x1 = x2.
- Lemma 3: sequences of values indexed by a set Sigma of size (chi*)^(n+1) < mu instead of ordinals below chi* (source wording fails for finite chi*). Violations also fixed by their g-pattern (finite sequence from G_1) in the pigeonhole step.
- Lemma 5: hypothesis |F| > kappa made explicit (source: "Choose f in F_1").
- L^0 given lambda constants; nullary relation symbols handled in the language lemma.
- Bookkeeping lemma: explicit construction; needs |p| + lambda < cf(2^lambda), proved from Konig (thm:p06-konig-cardinal). Added clause: every gamma with R(gamma) = <i,p> has all parameter positions below gamma (needed for |p-hat| <= kappa in Case V).
- Saturation: handbook definition uses complete types in finitely many variables; proof reduces to one variable by induction.
- Lemma 2 (source: "Immediate"), Case II ("easy to see"), Case IV ("same as Case III") written out.

## Provenance for N-a-014-MAP-05 (outside the reader)

The active Los citation correction (FLRV1 line 7037 `\cite{Los1955}` -> `\cite{Los1955Ultraproducts}` at `handbook/restoration/inherited-06942-07134.tex` line 96) has stale provenance: `spec/provenance/SRC-06942-07134.json` still records a byte-exact artifact and `tools/check_inherited_restoration.py` fails (7814 != 7802). Fixing it needs edits to spec/provenance and restoration checks (lead-owned); the reader paragraph `def:p03-los-source-correction` lives in non-owned `handbook/parts/p03/ultrafilter-choice-and-source-boundary.tex`. Not touched here.

## Block 2 (2026-10-13)

### Sources opened in this block

- Shelah 1971 held scan: pp. 224, 225 re-read as page images (220 dpi); pp. 232 (references 1-6) and 233 (references 7-16) read as images.
- Keisler 1961, held publisher version `source/references/acq-r1-ACQ-2026-10-0223/ACQ-2026-10-0223.pdf` (19 pp., journal pp. 477-495; PDF metadata DOI 10.1016/S1385-7258(61)50048-0). Whole text layer read; images inspected for pp. 484-488, 491, 492.

### Verified locators used in block 2

- Shelah p. 224: Keisler [6] summary; decomposition by Keisler [8] into three stages (lambda^+-good existence under lambda^+ = 2^lambda; lambda^+-saturation of M^I/D for language <= lambda; uniqueness of elementarily equivalent mu-saturated models of cardinality mu, with mu arbitrary); references [8], [7], Morley-Vaught [15]; Kochen [11] / Keisler [10] section 5 begins.
- Shelah p. 225: ultralimits, beth_alpha -> beth_{alpha+omega}; Mansfield [13] Boolean ultrapowers; Kunen [12]; Silver and Rucker consistency with ZFC + aleph_1 < 2^aleph_0, follows from Martin's axiom; open question (M = N, ||M||,||N|| <= mu, |L(N)| <= mu, D over mu, maybe independent of ZFC; mu arbitrary here); GCH elimination for Keisler [6] elementary classes; Horn theorem Keisler [5], Galvin [3], Mansfield [14]; "Los [3]" (misnumbered: Los is item 4); Notation: "Notice that mu is a regular cardinal."
- Shelah p. 232: reference 6 is the Ph.D. thesis (Univ. of Calif. Berkeley 1961) with "See also" the Indag. Math. 23 article; reference 3 Galvin, Horn sentences, Ann. Math. Logic 1 (1970); reference 5 Keisler, Reduced products and Horn classes, TAMS 117 (1965).
- Keisler p. 477 footnote *: the paper is identical with the doctoral dissertation (spring 1961, University of California). p. 478: isomorphic limit ultrapowers [20], [27]. p. 481-482: EC, EC_Delta, EC_Sigma, EC_Delta_Sigma. p. 483: Prod, Pow; Theorems 1.1-1.6 without proof (proofs in [12] Frayne-Morel-Scott, [29] Kochen). p. 486: proof of 2.2 cites "Theorem 1.4" for reducts; the reduct statement is Theorem 1.5 (p. 484). p. 487: footnote 5 (Kochen). pp. 487-488: Theorem 2.5 with proof. p. 488: Theorem 2.6, Cor. 2.7, Theorem 2.8, Cor. 2.9, Cor. 2.10, Theorem 2.11 (proof via 2.6 and 1.4). pp. 488-490: separation principles 2.12-2.14, Craig. p. 490: open question. p. 491: Q(alpha). p. 492: Cor. A.6. p. 493: Horn sentence definition, HC, HC_Delta, RProd, Chang's result, A.10-A.12 under GCH.

### Existing treatment found during block 2 (A9)

- w03a-p03-018 (block 2, written concurrently, file dated 2026-10-13 08:22) now contains the full reconstruction of Keisler 1961 Lemma 2.1, Theorems 2.2-2.4, the appendix forms and the comparison, including GCH-free Theorem 2.4 and transitivity (item 3 of thm:p03-w03-p03-018-keisler-compare). A first draft of the same material in this file was removed in favour of \cref links to those labels; this file adds only what 018 does not have (Keisler classes convention, Theorems 1.2-1.4 and 2.5-2.14 account, GCH-free 2.6/2.7/2.11/2.12 with proofs, Shelah's p. 224-225 context, mu regular, saturated uniqueness, decomposition corollary).
- Countable saturated uniqueness: thm:p03-vaught-saturated-uniqueness (n-a-003-01.tex) linked.

### N-a-014-MAP-05 correction provenance (recorded here; the provenance JSON is lead-owned)

- Correction: FLRV1 `source/formal-logic-reference.tex` line 7037 reads `The original source is \cite{Los1955}.`; the active restoration `handbook/restoration/inherited-06942-07134.tex` line 96 reads `The original source is \cite{Los1955Ultraproducts}.` Kind: bibliographic key correction (authorized correction of a citation key, no mathematical change). Current artifact: 7814 bytes, sha256 c159e8ad1b3761c6674fd59324def89b6a392eed21416e8188d4165871ee3bf6.
- `spec/provenance/SRC-06942-07134.json` still records restoration_artifact bytes 7802, sha256 784404cf..., disposition "full transcription", and no correction. Change needed (lead): set restoration_artifact.bytes 7814, sha256 and content_token_sha256 to c159e8ad...; record the line-96 correction (source line 7037, from Los1955 to Los1955Ultraproducts, reason: key of the cited Los 1955 paper); set disposition to the schema's authorized-correction value; rerun tools/check_inherited_restoration.py.

## Continuation

Block 1 written: 27.2 Horn (definitions, conventions, direct/reduced products, congruence and atomic lemma, preservation theorem with annex proof, corollary, worked example, limits); 27.3/27.4 Shelah 1971 construction (notation, Definition 1, Lemmas 1-5, language reduction, bookkeeping R, induction with Cases I-VI, parts 1-2, Keisler-Shelah both directions, Lemma 1 example, reading remarks, proof boundary). Patch request work/waves/w03a/patches/w03a-p03-017.json (driver inputs; crosslink in types-ultraproducts-supplement.tex).

Block 2 written:
- G14: workflow word removed from the false-head convention item.
- thm:p03-w03-p03-017-mu-regular (body ~251; annex 'The bound, saturated models...' subsection).
- sec:p03-w03-p03-017-keisler1961 (body 549-643): thesis identity kept distinct; classes convention; Theorems 1.2-1.4, 2.4-2.14 and A.10 account; links to 018 for 2.1-2.4 and appendix.
- sec:p03-w03-p03-017-shelah-context (body 644-~805): Keisler decomposition (stages 1-2 reported, stage 3 proved as thm:...-saturated-unique, composition thm:...-decomposition), Kochen ultralimits, Mansfield, Kunen, Silver/Rucker + Martin's axiom remark, open question, GCH elimination statements; thm:...-gch-free-closed (2.6, 2.7, 2.11, 2.12) with annex proof; proof boundary.

Open, in order:
1. GCH-free versions of Keisler 2.5, 2.8, 2.9, 2.10, 2.13, 2.14 (need an ultraproduct form of Shelah part 1, or a proof that ultrapowers of ultraproducts are ultraproducts plus a model of K* being equivalent to an ultraproduct; the latter lemma is already in the 2.11 proof).
2. Stages 1-2 of the decomposition (good ultrafilters): Keisler 1964 [7], [8] not held; Kunen [12] not held.
3. Kochen 1961, Mansfield 1971, Silver/Rucker, Galvin 1970, Keisler 1965: not held; reported only.
4. MAP-05 provenance JSON: lead-owned (above).
5. Hodges 1993 ch. 9 (SRC-048-0009) and Bell-Slomson: not held.
