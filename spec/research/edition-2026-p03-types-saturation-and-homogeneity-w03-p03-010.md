# w03a-p03-010 (P3, section 25.4): saturated elementary extensions of arbitrary structures

Packet: `work/waves/w03a/packets/w03a-p03-010.json`. label_tag `p03-w03-p03-010`, heading level `\section`, toc tag `%% toc: P3 25 25.4`.

## Duty addressed

MP-0(a): `thm:saturated-extension` (handbook/restoration/inherited-06640-06693.tex:40-53) carries "Status: cited theorem" with a Marker2002 pointer and a sketch. The owned body and annex files supply the complete proof for every structure and every infinite cardinal kappa:

- one-step compactness extension realizing every complete finitary type over every subset (`thm:p03-w03-p03-010-one-step`, with `thm:p03-w03-p03-010-type-facts` for consistency/completion/transfer and `thm:p03-w03-p03-010-copy` making the inclusion actual);
- transfinite elementary chain of length kappa^+ with unions at limits via `thm:elementary-chain`, the stage choices made inside a set (`annex:p03-w03-p03-010-saturated-extension`);
- regular-length bookkeeping: every parameter set of size at most kappa lies in an earlier stage (`thm:p03-w03-p03-010-bookkeeping`, proved from kappa*kappa = kappa only);
- consequences, worked example ((N,<) with kappa = aleph_0), limitations, relationships to Vaught's countable theorem and to `thm:saturation-homogeneity`.

## Provenance

Files `handbook/parts/p03/types-saturation-and-homogeneity-w03-p03-010.tex` and `handbook/annex/p03/types-saturation-and-homogeneity-w03-p03-010.tex` were first drafted by an earlier run of this packet (11 October 2026) that stopped before writing this note, the return, the intake bib and the symbol intake. This run (12 October 2026) re-checked every proof step, revised the text, re-opened both sources and wrote the remaining files.

Changes this run:
- `\Th` and `\set` are guarded restoration-only macros; replaced by `\operatorname{Th}` and `\{...\}` (unit compile failed before).
- The convention `def:p03-w03-p03-010-saturation-scope` now refers to the restoration definition of kappa-saturation instead of restating it as a new definition (A9).
- The relationships paragraph no longer cites `thm:p03-w03-p03-032-qf-test` (an unrouted file of another packet); it states the aleph_0 case (chain of length omega suffices for finite parameter sets) with its one-line reason.
- The annex justification that Seq_delta is a set now names Power Set, Separation and Replacement and the map r -> r u {(delta, U_r)}.
- Sources paragraph: identifies the van den Berg text as a course handout and adds the Definition 10.1 locator.
- Three overfull displays split.

Existing treatments checked (A9): `thm:saturated-extension` and the Saturation definition (inherited-06640-06693), `thm:saturation-homogeneity` (inherited-06694-06782), Vaught countable construction (n-a-003-01 body 380-393 and annex 621-680), `thm:p03-countable-saturated` (classification-theory.tex). Not in the packet's existing list: `handbook/annex/p03/stability-and-the-forking-calculus-w03-p03-032.tex` (annex of `thm:p03-w03-p03-032-qf-test`, around its line 748) builds an omega-saturated elementary extension by a chain of length omega (finite parameter sets only); it is a separate, unrouted file of packet w03-p03-032. Also unrouted: w03-p03-007 files (Vaught 1961 section 5).

## Sources read this session

- Morley, Vaught, "Homogeneous universal models", Math. Scand. 11 (1962) 37-57, publisher open access. URL https://journals.msp.org/mscand/article/download/2698/2697 (landing https://journals.msp.org/mscand/article/view/2698, DOI 10.7146/math.scand.a-10648). Downloaded this session; sha256 9710182d120a8b6f3f2798aabb3d316f26daa53d0ed099927acb69f6019fc431, identical to the earlier scratch copy. Pages read: 38 (preliminaries, kappa*), 39 (relational systems, S_kappa notation), 49 (Theorems 3.4 and 3.5). Version of record.
- van den Berg, Chapter 10 "kappa-saturated models and quantifier elimination", handout for 11 April 2016 in the Mastermath Model Theory 2015/2016 course; author page https://staff.fnwi.uva.nl/b.vandenberg3/Onderwijs/Model%20theory%202016/contents.html links `syllabus_week_8.pdf`. Downloaded this session; sha256 1e9957dadc5f3c6decaed92844686446bca22dcbfdb597513809cd264c5d86b0 (identical to the earlier scratch copy `w8.pdf`). Pages read: 1-3 (Definition 10.1, Lemma 10.2, Proposition 10.3, Theorem 10.4, Lemma 10.5 and the proof of 10.4). A lecture handout, not a published text; the reader text says so.

Locators used in reader text: MorleyVaught1962 p. 38 (kappa*), p. 39 (S_kappa), p. 49 Theorems 3.4, 3.5; vandenBerg2016ModelTheoryCh10 ch. 10 p. 1 Definition 10.1, pp. 2-3 Theorem 10.4, Lemma 10.5. All seen this session.

## Symbols

New local symbols in the symbol intake: s_M, mu_M, P_M, D_M, W(K), Seq_beta, N_alpha. Overlap: `\mathrm{Seq}_\beta` vs the registered P11 `\mathsf{Seq}_{\mathcal A}` (different font, role and scope; annex-local).

## Components

- FLRV1-U00457..U00461: the restoration capture `handbook/restoration/inherited-06694-06782.tex` lines 1-89 is line-identical to source lines 6694-6782 (diff run this session); assessed earlier with no open component. Not modified.
- N-a-003-*, ED26-SRC-048-0007-*, ED26-SRC-048-0010-*: readonly units owned by w03-p03-007 (A14).

## Continuation

State at return (12 October 2026): MP-0(a) proof written in owned body and annex; unit compile ok; check.py shows only bib-key findings for the two intake keys; find_fused_spaces clean. Remaining outside owned files: driver inputs and the restoration status change, filed as patch requests in `work/waves/w03a/patches/w03a-p03-010.json`. Until the inputs are applied, the route still shows the cited status. Small overfull boxes remain at long theorem titles (at most 17 pt).
