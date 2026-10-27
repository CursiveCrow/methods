# w03a-p03-044 — P3 36.6 Partially ordered prefixes (research note)

Packet: work/waves/w03a/packets/w03a-p03-044.json. Label tag p03-w03-p03-044.
Files: handbook/parts/p03/generalized-game-and-dependence-quantification-w03-p03-044.tex (body),
handbook/annex/p03/generalized-game-and-dependence-quantification-w03-p03-044.tex (annex),
intake bib and symbol CSV under the packet's owned paths.

## Sources opened in this session

- SRC-049 held preview, tmp/edition-2026-catalog-src038/tail-039-068/SRC-049-pageplace-preview-2026-09-09.pdf
  (SHA-256 digest 1597918d...). PDF pages 58-59 = printed pp. 38-39 (Ch. II, H.-D. Ebbinghaus,
  "Extended Logics: The General Framework", Section 2.5), rendered and read as images.
  PDF page 51 = printed p. 31 (Definition 1.2.4, kappa-compactness, "of power <= kappa"),
  read as an image. Chapter II spans pp. 25-76 by the contents (Ch. III begins p. 77).
  Bib key Ebbinghaus1985ExtendedLogics (intake). Ch. II is by Ebbinghaus, not Mundici.
- Online: Konrad Zdanowski, "One Henkin Quantifier in the empty vocabulary suffices for
  undecidability", arXiv:1612.07154v1 (21 Dec 2016), https://arxiv.org/pdf/1612.07154v1,
  Section 2, pp. 2-3 read (rendered page images). No journal version identified; the reader
  text says that it follows arXiv v1. Bib key Zdanowski2016HenkinArxiv (intake).
- Also read but not cited: Barwise 1974, Annals of Math. Logic 7, scratch text at
  tmp/agent-scratch/w03a-w03a-p03-048-b0-first/barwise1974.txt around pp. 240-241 (Henkin
  quantifier as a Lindstrom quantifier). No locators are used from it.
- Tried: the Project Euclid table of contents for Model-Theoretic Logics (Ch. VI, Mundici) on
  2026-10-11. It returns an Incapsula bot-check page, which was not bypassed.

## Notation decisions

- Ebbinghaus writes Q^H (superscript H) and L_{omega omega}(Q^H) with a script L. Both are kept
  as \mathscr L and Q^{\mathrm H}. The gap text's "Q_H" is not the source's glyph.
- Zdanowski's triple Q=(A,E,D) uses A for the set of universal variables, while Ebbinghaus uses
  A for the universe of \mathfrak A. Both are kept, and the reader text states where the meaning
  switches (from def:p03-w03-p03-044-qh on). This is recorded in the symbol intake.
- The name \varphi_\infty is introduced for Ebbinghaus's unnamed sentence on p. 39.
- \mathcal H (Zdanowski's family of all Henkin prefixes) overlaps the P2 prop-metatheory row
  "relational Henkin structure", which has a different scope and role. The proposed decision
  is recorded in the return file.

## Existing treatment found

- sec:p03-dependence-logics (preservation-abstract-logic.tex 480ff.) covers team semantics and
  the IF slashed quantifier. This chapter links to it and does not duplicate it. The IF
  convention is marked as distinct (def:p03-w03-p03-044-if-distinct). The team bridge is proved
  for dependence atoms only.
- Not listed in the packet: thm:fol-compactness (restoration) and
  thm:p02-w02c-p02-023-finite-structures. Both are reused for the non-first-order corollary.
  thm:p02-fol-compactness and thm:p02-finite-structures-not-axiomatizable exist in
  parts/p02/first-order-completeness.tex, but that file is not on the main.tex route.
- A grep of parts/ and annex/ found no other treatment of Henkin or branching quantifiers.
  handbook/annex/p08/n-b-009-02.tex matched the pattern "Q_H", but its content is unrelated.

## What is written (MP-0(a))

- General dependency-prefix syntax and its function and strategy semantics (Zdanowski pp. 2-3),
  with the observation that the dependency relation is a partial order.
- The dependency triple of a linear prefix and its Skolem equivalence (Ebbinghaus's p. 38
  illustration), with a full annex proof by induction.
- The definition of Q^H, its two-row notation and its triple form.
- Q^H compared with the linear prefix, with a counterexample.
- The infinity sentence in three parts, with choice used in part (3).
- Failure of aleph_0-compactness, and the absence of a first-order equivalent.
- The flatness lemma and the team-semantics bridge.
- A warning that the IF convention is distinct, and a warning on limitations.
- Worked examples on N and on a three-element set.

## Block 1 of 2026-10-12: regularity of the Henkin logic

- Re-opened the held preview this session: PDF pages 47-51 (printed pp. 27-31: structures,
  tau-closed sets, renamings, Definition 1.1.1, Definitions 1.2.1-1.2.3, regular logics) and
  58-59 (printed pp. 38-39), rendered as images under tmp/agent-scratch/w03a-w03a-p03-044-b1-author/.
  The earlier items (prefix syntax, strategy semantics, Q^H, infinity, non-compactness) were
  checked against pp. 38-39 again; they were already in the body.
- Written: sec:p03-w03-p03-044-regular (convention def:p03-w03-p03-044-henkin-syntax; lemmas
  thm:p03-w03-p03-044-basic and thm:p03-w03-p03-044-unnesting; theorem
  thm:p03-w03-p03-044-regular) with annex proofs. The definitions of logic, closure,
  relativization and substitution are not repeated; they are \cref'd from the w03-p03-047
  chapter (def:p03-w03-p03-047-vocabularies, -ebbinghaus-logic, -closure, -relativization).
- Decisions: one-sorted vocabularies only. Ebbinghaus's Q^H clause has f_0,f_1:A->A on one
  universe, and Definitions 1.2.2-1.2.3 are stated for the one-sorted case (p. 30). A many-sorted
  version of Q^H is not defined in the pages read, so none is invented.
- Substitution property reading: 047's definition imposes the graph condition on every symbol
  of tau' minus tau. For finitely many symbols this is proved. For infinitely many symbols not
  occurring in phi, a single sentence would have to express infinitely many graph conditions;
  the theorem proves the version for the symbols occurring in phi and, separately, the full
  version when tau' minus tau is finite. Whether the full version holds for infinite tau' minus tau
  is open here (crosslink note for the 047 owner).

## Block 2 of 2026-10-12: substitution limit and links

- Guard G8 fixed in this note (line 11: the digest label is now written SHA-256).
- Re-opened the held preview: PDF pages 50-51 (printed pp. 30-31), rendered under
  tmp/agent-scratch/w03a-w03a-p03-044-b2-author/. Read: p. 30 "For technical convenience we
  formulate the following properties only in the one-sorted case" (before Def. 1.2.2); the
  displayed single-replacement meanings (relation, function, constant) on p. 30; Def. 1.2.3
  (pp. 30-31) quantifies over all tau subset tau' and all symbols of tau' minus tau; p. 31
  says the many-sorted version needs a careful treatment of sort symbols.
- Written: thm:p03-w03-p03-044-substitution-limit (body, after the regularity theorem) with
  annex proof annex:p03-w03-p03-044-substitution-limit. Result: with countably many variables,
  tau={e} and infinitely many new constants c_n with psi_{c_n}(d) = (d=e and not eps_n), there
  is X (Cantor counting) for which no sentence of L(Q^H)[tau], hence no first-order sentence,
  meets the substitution requirement for all symbols. Theorem regular part (4) is strengthened
  from "tau' minus tau finite" to "only finitely many function symbols and constants in
  tau' minus tau" (annex paragraph updated). This closes open item (3) of block 1: the
  all-symbols version for infinitely many replaced constants is false, also for L_omega omega.
- Linked to w03-p03-042 (owner of unit ED26-SRC-049-0006): the intro now states that
  Mundici's comparison and Robinson-equivalence quantifiers belong with
  sec:p03-w03-p03-042-mundici-po, and the p. 39 second-order remark cites
  thm:p03-w03-p03-042-mundici-pc-ec. The section titles were checked against the held
  contents listing (reading.txt lines 403-406). Q_pi is NOT used in that sentence because this
  chapter's Q_pi (linear-prefix triple) differs from 042's Q_pi (Mundici's pattern quantifier).

## Remaining source items on pp. 38-39 not written

- Ebbinghaus p. 39 also says that adjoining quantifiers from partially ordered prefixes gives the
  full expressive power of second-order logic, and defers the details to Section VI.1. This is
  not written. The details are in Ch. VI (Mundici), whose body is not held: the preview lacks
  it and Project Euclid is behind a bot check. Zdanowski p. 3 states
  Sigma^1_1 <= L(H) <= Delta^1_2 and cites Enderton and Walkoe, which are not held; this is not
  written either.
- The rest of duty MP-0 for 36.6 covers the comparison quantifiers and the Robinson-equivalence
  quantifiers (Ch. VI Sections 2 and 4). The source body is not held, so nothing is written.

## Continuation

- 2026-10-11 block 1: the MP-0(a) material is written (body lines 1-372, annex lines 1-285).
  unit-compile reports ok, with 5 small overfull boxes, each under 4pt. check.py reports only
  bib-key findings for the two intake keys. find_fused_spaces reports no hits.
- 2026-10-12 block 1: regularity section written (body 296-444, annex 210-574). Body is now
  lines 1-531, annex 1-650. unit-compile ok (6 overfull boxes, each under 4pt); check.py shows
  only the bib-key finding for Zdanowski2016HenkinArxiv (intake key); find_fused_spaces clean.
  The second-order remark of p. 39 is reported in reader text as Ebbinghaus's remark and is
  not stated as a theorem.
- Next: (i) the second-order expressive-power claim needs Ch. VI.1 (not held); (ii) a many-sorted
  form of Q^H would need a source that defines it; (iii) the Ch. VI components stay with the
  owner packet w03-p03-042 (readonly_units).
- 2026-10-12 block 2: body now lines 1-583 (new theorem at 455, remark 445-485, intro 28-32,
  second-order link 488-493), annex 1-724 (new item 578-649). unit-compile ok (6 overfull);
  find_fused_spaces clean; check.py shows only the bib-key finding for the intake key
  Zdanowski2016HenkinArxiv.
- Remaining: (i) the p. 39 second-order remark stays a reported remark (its precise form is
  042's theorem); (ii) many-sorted Q^H: Ebbinghaus formulates Defs. 1.2.2-1.2.3 only for the
  one-sorted case (p. 30), and no many-sorted Q^H clause is in the pages read; (iii) Ch. VI
  Sections 2-4 are owned by w03-p03-042 (readonly_units).

## Author correction, 26 October 2026

The non-first-order-definability proof now contains the direct first-order compactness argument, including the finite-size sentences and finite satisfiability check. It no longer depends on the off-route Part 2 finite-structures packet. This is an author correction; no source allocation or independent-review status is promoted.
