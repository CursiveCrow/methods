# w02b-p15-032: P15 164.10, Dubois--Prade 4.7 completion and the Galavotti blocker

Provenance note for packet w02b-p15-032 (label_tag p15-w02b-p15-032).
Reader files: handbook/parts/p15/inductive-logic-and-confirmation-w02b-p15-032.tex
(chapter sec:p15-w02b-p15-032) and handbook/annex/p15/inductive-logic-and-confirmation-w02b-p15-032.tex
(sec:annex-p15-w02b-p15-032). The read-only host handbook/parts/p15/rationality-4-7.tex
(SHA-256 hash 5c359a89..., the version assessed) was not edited; the new chapter extends it.

## Sources opened in this session

- source/references/p15-rationality-4-7/dubois-prade-2021-publisher.pdf (14 pages; printed 305-316).
  Full text extracted; page images of printed 306-313 inspected for glyphs. Locators used:
  pp. 305, 306, 307, 308, 309, 310, 311, 312, 313, 314. Verified readings:
  p. 308 adjunction display P(A|C)>P(A^c|C) and P(B|C)>P(B^c|C) imply P(A cap B|C)>P(A^c cup B^c|C);
  p. 309 K gives box(p and q) iff box p and box q; D as N(A)=1 implies Pi(A)=1; GPL D as box^lambda p => diamond^1 p;
  p. 310 Cox (i)-(iii), Paris strict monotonicity + density, Halpern 1999a,b, (i) presupposes Bayes conditioning, (ii) self-duality;
  p. 313 the second rule is printed LP(f-g) >= 0 (weak), while desirability is stated as positive lower expectation.
- source/references/acq-r1-ACQ-2026-10-0485/milton-2011-induction-before-hume.pdf: Milton, "Induction before Hume",
  HHL vol. 10 (author version, (c) 2009 line) -- a different chapter, not Galavotti.
- tmp/acquisition/src063/web-open-fordham-volume2-chapter-pdf-renderer.txt: HHL vol. 2 contents listing -- not Galavotti.
- Handbook interfaces read: rationality-4-7 body/annex, rationality-4-1 (selected sections), rationality-8-4 (selected),
  ambiguity-and-robust-choice (acts, sure-thing, Ellsberg three colours, robust dominance, maxmin urns),
  finite-subjective-probability (price coherence), imprecise-probability (representation, dual, possibility bridge),
  reasoning-methods-and-evidence (measure separation), paraconsistent-and-nonmonotonic (AGM), conditionals-deontic-free.

## Existing treatments found (A9)

- thm:p14-evidence-measure-separation already gives a lower envelope violating the order-two inequality; it is
  cited, not duplicated. Not in the packet's "existing" list.
- thm:p17-maxmin-urns already computes the three-colour maxmin values; cited and re-derived only for the credal
  set P_E inside the decision theorem. Not in the packet's list.
- def:p17-robust-dominance / thm:p17-robust-dominance (robust dominance) = the survey's LP(f-g)>=0 rule; identified.
- thm:p15-ip-representation already gives uniqueness of the closed convex representing set on all bounded gambles;
  the new finite theorem gives the closure characterization and the nonclosed counterexample.

## Corrections recorded

1. Survey p. 308 prints big-stepped masses as a strict chain p1>...>pn with p_i > sum_{j>i} p_j for all i<n.
   The exact finite class at threshold 1/2 (thm:p15-w02b-p15-032-big-stepped) is: positive masses ordered
   decreasingly satisfy p_i > sum_{j>i} p_j for i <= k-2; the last two may tie; null states free.
   Uniform on two states obeys the rule.
2. Survey p. 312 "any convex set" is true for closed convex sets only (thm:p15-w02b-p15-032-convex).

## Cited-only boundaries (works not held; no locators claimed)

Cox 1946; Paris 1994; Halpern 1999a,b; Dubois-Prade-Sabbadin 2001; Fargier-Sabbadin 2005; Benferhat-Dubois-Prade
1998, 1999; Snow 1999 (other thresholds); Dubois-Fargier-Prade 2004 (links to counterfactuals and revision);
Ciucci-Dubois 2013; Dubois-Prade-Schockaert 2017 (GPL completeness and encodings); Shafer 1976 and Smets 1995
(separable decomposition); Jaffray 1989; Kerkvliet-Meester 2018; Giles 1982; Dubois-Prade-Smets 2008; Spohn 1990;
Dubois-Moral-Prade 1997 and Dubois 2006. Each is listed per claim in tab:p15-w02b-p15-032-claims.

## Blocked: SRC-063 (Galavotti)

Not held: Maria Carla Galavotti, "The Modern Epistemic Interpretations of Probability: Logicism and Subjectivism",
Handbook of the History of Logic vol. 10, Inductive Logic (Elsevier 2011), chapter 5, pp. 153-203; and the author
presentation HHL10_Galavotti.pdf (stephanhartmann.org upload). The held paths are a different chapter (Milton) and a
vol. 2 contents listing. Nothing was written for these components (no placeholder).

## Continuation

State after this session (2026-10-04):
- Written: body chapter (730 lines) and annex (292 lines), eight annex proofs with reciprocal proved= links;
  intake bib (no new keys) and symbol intake (9 rows).
- unit-compile ok (overfull boxes 18, from the two longtables); check.py --tree shows no finding in these files.
- Remaining for this packet: SRC-063 components blocked on acquisition of the Galavotti chapter and author PDF.
  RAT2021-4-1 components belong to w02b-p15-022.
- Possible next steps if allocated: acquire Benferhat-Dubois-Prade 1999 and Snow 1999 to prove or bound the
  any-threshold claim; acquire Paris 1994 / Halpern 1999 to present Cox's theorem with its exact hypotheses.
- Lead-owned: insert \input of the body after parts/p15/goodman-entrenchment-and-projectibility in handbook/parts/p15.tex
  (after line 93) and the annex after annex/p15/goodman-entrenchment-and-projectibility in handbook/annex/p15.tex (after line 91).

Update 2026-10-04 (second session):
- ED26-BM-RAT2021-4-7-C05: claims table tab:p15-w02b-p15-032-claims gained two rows, both read in the held
  publisher PDF this session: p.307 Savage (1954) justification (Savage's derivation cited only; handbook route
  def:p17-sa-postulates / thm:p17-sa-general-converse proved / thm:p17-sa-general-source cited) and p.313
  "avoiding sure loss means UP(f) >= LP(f)" (necessary direction proved at thm:p15-ip-dual; as a sufficient test for
  separately quoted prices refuted at thm:p15-r47-price-boundaries). unit-compile ok; no check.py finding in owned files.
- G1 guard files (p01-014 and p02-036 research notes and returns) were not touched by this packet.

Update 2026-10-04 (third session, gap list for ED26-BM-RAT2021-4-1 C01-C05):
- Not written here. The packet's readonly_units assigns ED26-BM-RAT2021-4-1 to w02b-p15-022, and the five
  gaps sit in the read-only host handbook/parts/p15/rationality-4-1.tex. The owner's note
  (spec/research/edition-2026-p15-exchangeability-and-predictive-induction-w02b-p15-022.md, block r3) records
  C01 (sec:p15-w02b-p15-022-alternatives), C04 (comparison section) and C05
  (sec:p15-w02b-p15-022-dependent-sources) as written in its own files and C02, C03 as remaining.
  Writing them here as well would give a second treatment in a file the owner does not control.
- Exact changes still owed (lead or owner): C02 add to the disagreement passage of rationality-4-1.tex the
  source's prescription for each scenario (defer to a better-informed disputant, not to a less-informed one;
  both may hold their positions under different permissible priors; independent agreement may warrant raised
  confidence, Lasonen-Aarnio), the Christensen and Kelly attributions, and the source's classification of the
  Principal Principle as an expert/deference principle; C03 state the source's KL values (0.438, 0.572) next
  to thm:p15-rat41-graded and record that they differ from (3/7, 4/7) and do not sum to one; C04 replace
  "another chapter" (line 214) with \cref{sec:p15-rationality-4-7} and cross-reference rationality-4-5 (P19)
  and rationality-8-3 (P17).
- SRC-063 (Galavotti): still not in held-sources.json; no change.
- Checks: unit-compile ok (overfull 18); find_fused_spaces no hits; check.py no finding in owned files.

Update 2026-10-04 (fourth session):
- G1 guard: the four flagged files are untracked files of packets w02b-p01-014 (mtime 22:34) and
  w02b-p02-036 (mtime 18:23); this packet never wrote them and cannot revert another packet's files.
  Lead attribution of the guard is needed; no action possible here.
- SRC-063: held-sources.json still lists only Milton 2011 and the vol. 2 contents listing; the
  HHL10_Galavotti.pdf fetch in tmp/acquisition/src063 records a 502 failure. Still blocked_source.
- ED26-BM-RAT2021-4-1: still owned by w02b-p15-022 (readonly_units). No change.
- Checks rerun: unit-compile ok (overfull 18); find_fused_spaces no hits; check.py no finding in owned files.
