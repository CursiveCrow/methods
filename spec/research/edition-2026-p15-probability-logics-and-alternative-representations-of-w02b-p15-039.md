# w02b-p15-039: RAT2021 5.3 Ranking Theory (section 165.5), block 1

Packet `work/waves/w02b/packets/w02b-p15-039.json`; unit `ED26-BM-RAT2021-5-3`.
Label tag `p15-w02b-p15-039`. Date 4 October 2026.

## Source held and read this session

- `source/references/p15-rationality-5-3/ranking-2021-institutional.txt`
  (held; SHA256 2bf5eaeb...c9043), text of the KOPS publisher-layout PDF
  `ranking-2021-institutional.pdf` (held; SHA256 f8d025f6...b94c), printed
  pp. 337-346 of Knauff and Spohn (eds.), *The Handbook of Rationality*, MIT
  Press 2021, chapter 5.3. Whole chapter, notes 1-9 and references read.
- Provenance of the earlier treatment: `spec/research/p15-rationality-5-3-source-note.md`.

Locators used and seen in the held text this session: p. 337 (section 1:
belief simpliciter, truth vs action, doxastic logic static, belief revision
iterated-revision problem, ranking promises both); p. 338 (qualitative belief
sets cannot model change; entrenchment); p. 339 (law of conjunction
justification; cardinality presupposition; material vs conditional belief
"precisely ... non-vacuously"; reason explanation; Carnap incremental
confirmation); p. 340 (Definition 3; Bayes nets restatable, Spohn 1988,
Goldszmidt and Pearl 1996); p. 341 (ordinal AGM, no clear solution; Shackle,
Rescher, Cohen lack conditional ranks); p. 342 (Darwiche-Pearl etc.;
psychological belief revision extension; Da Silva Neves et al. System P plus
rational monotonicity; no direct ranking test); p. 344 n. 4 (Merin sections 1-4
transfer), n. 9 (|~ default entailment).

## Gaps closed in this block (host edits, not new files)

Per A9 the existing treatment in the editable hosts was extended instead of
writing a second chapter. Owned body/annex files were not created; temporary
wrappers that \input the hosts were created only to run the packet's
unit-compile and then removed. No driver insertion is needed.

- C02 (i) `sec:p15-w02b-p15-039-motivation` + example
  `def:p15-w02b-p15-039-same-order` (editorial; same order, different
  cardinal ranks, different iterated outcome).
- C02 (ii) law-of-conjunction paragraph at the head of "Conditionals and reasons".
- C02 (iii) + C04 (4-3) `sec:p15-w02b-p15-039-reasons`,
  `thm:p15-w02b-p15-039-reason-laws` (cross-sum criterion a+d<b+c, symmetry,
  negation, irrelevance, Delta_P = p1p4-p2p3, weak betweenness of tau(B) and
  failure of strict prior comparison, nontransitivity).
- C05 `thm:p15-w02b-p15-039-material` (kappa(A)=0 hypothesis; vacuous case).
- C04 (4-4) `thm:p15-w02b-p15-039-rational-monotony` + comparison paragraph.
- C04 (p16 4-2) `thm:p15-w02b-p15-039-chain` + comparison paragraph.
- C04 (p19 5-4) paragraph realizing `thm:p19-r54-two-revisions` orders as ranks.

Author arithmetic check (scratch, not a test suite): brute force over cell
ranks in {0,1,2,3,inf} confirmed the cross-sum criterion, symmetry and weak
betweenness; rational monotonicity confirmed over all rankings 0-2 of eight
worlds.

## Open items

- Hild and Spohn 2008, *Artificial Intelligence* 172, 1195-1218 (measurement
  axioms and ratio-scale uniqueness theorem) is not held; the cardinality
  justification remains reported by citation through the chapter (p. 340, n. 7).
- Da Silva Neves, Bonnefon and Raufaste 2002 not held: no task, sample or
  uncertainty reported beyond the chapter's description.
- Ranking analogues of the parental Markov condition and semigraphoid
  operations (Spohn 1988; Goldszmidt and Pearl 1996) are not held and not derived.

## Second pass (r2): C05 accounting for pp. 341-343

Held text reread this session: `source/references/p15-rationality-5-3/ranking-2021-institutional.txt`
lines 291-656 (printed pp. 341-345, notes and reference list). Locators used and
seen: p. 341 (Leitgeb 2017, Raidl and Skovgaard-Olsen 2017; P(A)=1-eps claim;
DS generality, Shafer 1976 ch. 10 consonant functions, Spohn 2012 sec. 11.9;
probability translation); p. 342 (Darwiche-Pearl 1997; Jin-Thielscher 2007;
Delgrande-Jin 2012; Spohn 2012 ch. 7; Kern-Isberner-Huvermann 2017; Levi/Harper;
contraction as ranking conditionalization; Kern-Isberner, Bock, Sauerwald,
Beierle 2017; Kern-Isberner 2004; Baratgin-Politzer, Oaksford-Chater, Wolf et al.;
Colombo, Elkin, Hartmann 2018; Da Silva Neves et al. 2002; Benferhat et al. 2005;
Isberner and Kern-Isberner 2017; Eichhorn et al. 2018 begins); p. 343 (Eichhorn
et al. ends; Ragni et al. 2017; Byrne 1989; Spohn 2013, 2015; Skovgaard-Olsen
2014, 2016, 2017, 2019; Henrion et al. 1994; Juslin et al. 2011); pp. 344-345
reference list (48 entries, counted by hand; page-of-first-citation grouping
taken from the page headers at text lines 65, 132, 196, 291, 351, 411, 483).

None of the pp. 341-343 dependent works named in the gap is in
held-sources.json (searched by author name); all are reported only as the
chapter's attribution. Titles used in reader text (Henrion et al. 1994,
Benferhat et al. 2005, Kern-Isberner et al. 2017) are from the printed
reference list p. 344.

Written (host extension, end of body and annex):
- body `sec:p15-w02b-p15-039-dependents` (lines 736-1090):
  `def:p15-w02b-p15-039-dependent-set` (finite set D, 48 entries by page),
  `sec:p15-w02b-p15-039-attributions` (one paragraph per gap claim: kind,
  dependent works, treatment, A11 limits), `def:p15-w02b-p15-039-contraction`,
  `thm:p15-w02b-p15-039-levi-harper`, `def:p15-w02b-p15-039-levi-example`,
  `thm:p15-w02b-p15-039-consonant`.
- annex `annex:p15-w02b-p15-039-levi`, `annex:p15-w02b-p15-039-consonant`
  (lines 349-525).
- Editorial results (not in the chapter): contraction case split; Levi/Harper
  at belief-set level and Levi at ranking level; consonant representation with
  base-2 masses, Dempster conditioning agreement, non-closure under Dempster
  combination (3-world counterexample). Checked by hand in the annex.

Open (blocked_source; not written): Leitgeb 2017; Raidl and Skovgaard-Olsen 2017;
Spohn 2012 ch. 7 and sec. 11.9; Jin-Thielscher 2007; Delgrande-Jin 2012;
Kern-Isberner-Huvermann 2017; Kern-Isberner, Bock, Sauerwald, Beierle 2017;
Colombo et al. 2018; Benferhat et al. 2005; Eichhorn et al. 2018; Henrion et
al. 1994; Hild-Spohn 2008 (carried over). Their own definitions, theorems, and
study designs are not stated.

## Third pass (r3): guard fixes and relocation into owned files

Held text reread this session: `source/references/p15-rationality-5-3/ranking-2021-institutional.txt`
lines 280-500 (printed pp. 341-344). No new locators were introduced; the
relocated text keeps the locators recorded for r1 and r2 above.

- G14: host body lines 628 and 657 used the verb "reviewed"; now "presented"
  and "described" (`handbook/parts/p15/rationality-5-3.tex`).
- G10: the packet's owned body/annex files did not exist, so the unit compile
  failed.  The r2 material that this packet appended to the hosts (body
  section "Attributed claims and the works they depend on" with its
  subsections, old host lines 736-1090; annexitems levi and consonant, old
  host annex lines 349-525) was moved verbatim into the owned files, with
  only cross-reference wording changed ("above", "previous section", "this
  chapter" now point to Chapter sec:p15-rationality-5-3), the two former
  subsections promoted to sections, and a new chapter opening
  (`sec:p15-w02b-p15-039`) plus annex section heading (`sec:p15-w02b-p15-039-annex`).
  No label changed.  No label in the moved block is referenced from outside it.
- The hosts now end at the hbmethod `def:p15-rat53-task-interface` (body) and
  the annexitem `annex:p15-w02b-p15-039-rational-monotony` (annex).
- The owned files must be inserted into the drivers by the lead (packet
  insertion proposal: `\input{parts/p15/probability-logics-and-alternative-representations-of-w02b-p15-039}`
  after `\input{parts/p15/rationality-5-3}` in handbook/parts/p15.tex, and the
  matching annex input after `\input{annex/p15/rationality-5-3}` in
  handbook/annex/p15.tex).  Until then the moved content is absent from main.tex.

## Fourth pass (r4): assessment gaps C02, C04, C05

Held text reread this session: `source/references/p15-rationality-5-3/ranking-2021-institutional.txt`
lines 196-250 (printed p. 340) and 291-400 (pp. 341-342).  Locators used and
seen: p. 340 ("four significant forms" by sign of tau(B|A), tau(B|not A);
sufficient reason defined; independence = neither A nor not A a reason;
independence theory in analogy to probability); p. 341 (DS three claims,
Shafer 1976 ch. 10, Spohn 2012 sec. 11.9; product/quotient to sum/difference
translation); p. 342 (independence postulates related to ranking
independence, Spohn 2012 ch. 7, Kern-Isberner and Huvermann 2017).

Correction: the r2 attribution paragraph said the chapter does not print the
ranking notion of independence; it does (p. 340).  Paragraph corrected.

Written:
- host body `handbook/parts/p15/rationality-5-3.tex` 311-355: four-forms
  paragraph, `thm:p15-w02b-p15-039-reason-forms` (five sign cases of a reason,
  sufficient = (+,0),(+,-), realizing quadruples, Tweety B->F (+,0) and
  not-P->F (0,-)).  The other three forms' names are not printed in the
  chapter and are not named (A12).
- host body 540-562: DS paragraph states the three p. 341 claims, marks the
  divergence as a material objection, contrasts thm:p15-r47-ranking (static
  only) and points to thm:p15-w02b-p15-039-consonant.
- host annex `handbook/annex/p15/rationality-5-3.tex` 265-315:
  `annex:p15-w02b-p15-039-reason-forms`.
- owned body 334-418: `sec:p15-w02b-p15-039-independence`,
  `thm:p15-w02b-p15-039-independence` (cross-sum, product-to-sum form,
  invariance of ranks of B under every update on A iff independent, symmetry,
  update on A preserves tau(B|A), tau(B|not A)),
  `def:p15-w02b-p15-039-independence-example` (preservation under update on
  not A; loss under update on A<->B with firmness 2; Tweety bird/penguin).
- owned annex 113-202: `annex:p15-w02b-p15-039-independence`.
- patch request `work/waves/w02b/patches/w02b-p15-039.json`: driver insertion
  of the owned body and annex (the assessment read only the host; the owned
  chapter carrying Levi/Harper, Leitgeb, Raidl and Skovgaard-Olsen, Colombo et
  al., Benferhat et al., Eichhorn et al., Henrion et al., Kern-Isberner and
  Huvermann, Spohn 2012 sec. 11.9 and the dependent-source set D is off the
  main.tex route until inserted).

Checks: unit-compile ok (2 overfull, bibliography); scratch build with hosts
plus owned files: no error, no undefined reference to any rat53 or
w02b-p15-039 label; find_fused_spaces no hits; check.py --tree no finding
for the four files.

## Continuation

r4: gaps of the assessment closed as far as the held chapter allows (above).
Remaining blocked_source unchanged from r2 (Leitgeb 2017; Raidl and
Skovgaard-Olsen 2017; Spohn 2012 ch. 7 and sec. 11.9; Jin and Thielscher 2007;
Delgrande and Jin 2012; Kern-Isberner and Huvermann 2017; Kern-Isberner, Bock,
Sauerwald and Beierle 2017; Colombo et al. 2018; Benferhat et al. 2005; Da Silva
Neves et al. 2002; Eichhorn et al. 2018; Henrion et al. 1994; Hild and Spohn
2008), plus the names and boundaries of the other three of the four forms of
reasons (not printed in the chapter).  Driver insertion is blocked_policy
(patch request filed).
