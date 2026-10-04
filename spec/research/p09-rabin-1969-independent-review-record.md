# Rabin 1969 independent manuscript review record

## Admission scope

This record closes source acquisition, reader-facing reconstruction, and the
three independent manuscript-content review gates for exactly `N-c-014.d`:
Michael O. Rabin's 1969 article, “Decidability of Second-Order Theories and
Automata on Infinite Trees,” together with Albert R. Meyer's later correction
to Rabin's elementary-recursive complexity claim. The reviewed reader scope is
the Rabin presentation beginning at line 908 of
`handbook/parts/p09/presentations/n-c-014.tex`, together with the relevant
bibliography records, complete Rabin source note, and compact Part IX
source-presentation record.

Acceptance means that the frozen presentation accurately reconstructs the
source definitions, numbered-result roles, proof architecture, applications,
later complexity correction, explicit handbook-owned repairs, terminology
standing, provenance, rights limits, and reconstruction boundary described
below. It does not certify every statement printed by Rabin as correct, and it
does not silently attribute a handbook repair or Meyer's later result to Rabin.

This admission does not admit `N-c-014.a`, `N-c-014.b`, `N-c-014.c`,
`N-c-014.e`, `N-c-014` as a whole, Part IX, another handbook part, a rendered
handbook page, a TeX or repository build, human review, user acceptance,
final-book completion, or publication. It does not authorize redistribution of
either source PDF or its page images.

## Exact accepted snapshot

All three Round 8 reviewers accepted the following unchanged six-object
pre-admission snapshot:

| Artifact | SHA-256 |
|---|---|
| `tmp/pdfs/p09-rabin-1969/rabin-1969.pdf` | `CF86AFCBE897931FD0BA5E119CFB8F1C56DC5010581E2DC0DE9C3E41D5AB45E3` |
| `tmp/pdfs/p09-rabin-1969/icm1974-volume2-meyer.pdf` | `9AF43A2A01E32F02649DA845D256A9A26F73D668091FFDB1BBEC34D67BF3355D` |
| `handbook/parts/p09/presentations/n-c-014.tex` | `BD9574662C1CC025F9AF8B6657EFC5535795C55F1E32162188E0C2007E443695` |
| `handbook/bib/handbook.bib` | `408B1020F85D15599820FD91E1E604384A761A38CCC52BAD470E5AEF0A652BE0` |
| `spec/research/p09-rabin-1969-source-note.md` | `4C7FA2AFDCED52E1076F5604A826F5AC148707EE0A4AE1772B31F704259F104A` |
| `spec/research/p09-source-presentations-lot2-3.md` | `9B679F27B410F8FC65F0193AD0E85B4653C32B306002B9C0F19E2EFBACDC8DB2` |

Each reviewer independently recomputed all six identities before judgment. The
chair kept the three reports sealed until all had been filed, then read every
report in full and independently recomputed the six frozen identities and the
three report identities. Every value matched.

The compact source-presentation record then received only two administrative
status changes: the `N-c-014.d` paragraph now records the unanimous Round 8
decision and links this record, and the consolidated ledger now says that the
reconciled Rabin reconstruction is independently accepted. Its resulting
post-admission SHA-256 is
`EAA1CDBC5C3D388CFC7E5915F099F0FBDEE43243D80131EF5ECED0F185FBE6B8`.
Those edits change no reader mathematics, source claim, bibliography entry, or
detailed source note. The accepted reader, bibliography, source note, and two
source PDFs remain byte-identical to the reviewed snapshot.

## Primary authorities, page coverage, and rights

The controlling source is Michael O. Rabin, “Decidability of Second-Order
Theories and Automata on Infinite Trees,” *Transactions of the American
Mathematical Society* 141 (1969), pp. 1--35, DOI
`10.1090/S0002-9947-1969-0246760-1`. The frozen local file contains one
custody-and-use cover followed by all thirty-five printed article pages.
Physical PDF page 1 is the cover; physical pages 2--36 are printed pp. 1--35.

The later complexity authority is Albert R. Meyer, “The Inherent Computational
Complexity of Theories of Ordered Sets,” in *Proceedings of the International
Congress of Mathematicians, Vancouver, 1974*, vol. 2 (published 1975), printed
pp. 477--482. The frozen local file is the complete official proceedings
volume; the authorized article scope is physical PDF pp. 485--490, corresponding
to printed pp. 477--482.

Every Round 8 reviewer visually inspected all thirty-six Rabin physical pages
and all six Meyer article pages at original detail. The Rabin inspection
covered the custody statement, every definition and numbered result, the whole
complementation and emptiness development, all applications, and the
references. The Meyer inspection covered the tower lower bound, the exact
two-successors-and-prefix entry, the Meyer--Stockmeyer attribution, the Rabin
comparison, and the references. Searchable extraction was not controlling for
formulae, symbols, wording, or pagination.

Rabin's custody cover restricts the archived copy to personal, noncommercial
use absent permission. Meyer's article bears the proceedings copyright.
Research access to either object is not treated as an open-content or
republication licence. The handbook supplies independent scholarly prose and
does not claim a right to reproduce the source PDFs or protected expression.

## Reviewer transcripts and independence

| Seat | Canonical reviewer | Final transcript | Transcript SHA-256 | Verdict |
|---|---|---|---|---|
| source fidelity and evidence | `/root/rabin_r8_source_fidelity` | `spec/research/boards/p09-rabin-1969/transcript/r8-source-fidelity.md` | `D79C7A3D91A8664647C968432B645A2EED8BCE23230109DACEB597382B0B47B5` | **ACCEPT** |
| mathematical and proof correctness | `/root/rabin_r8_mathematical_proof` | `spec/research/boards/p09-rabin-1969/transcript/r8-mathematical-proof.md` | `C6CFA5E0E5C180B1F1D25D498220DEF4CD1623B52F20E3C9089BEF6FED16F3D2` | **ACCEPT** |
| adversarial publication and terminology | `/root/rabin_r8_adversarial_publication` | `spec/research/boards/p09-rabin-1969/transcript/r8-adversarial-publication.md` | `9C93AB0649A19A8635E8031E5079A4F5DBF2EA4A14C9E02B17051F1CCDF3ED24` | **ACCEPT** |

The Round 8 seats were fresh agents who had not sat in an earlier Rabin round
and received no inherited conversation history. Each could use only the board
charter, the six frozen objects, and the two chartered original-detail render
sets. Earlier reports, the ledger, chair transcript, other board records,
staging material, layout extraction, memory, conversation history, web
browsing, and contact with another reviewer were forbidden. Each reviewer
wrote only its assigned report.

The source-fidelity report was filed first and the mathematical report second.
The chair did not open either report while the adversarial seat was still
working. After the adversarial report was physically filed, the chair read the
three reports completely in separate line-numbered passes. The final reports
contain 198, 473, and 227 lines respectively, and each ends exactly with
`VERDICT: ACCEPT`.

This was manuscript scholarship, not software engineering. No reviewer and no
chair operation used a test, test harness, automated checker, repository
script, TeX command, interim handbook build, handbook-PDF inspection, or build.
The review methods were direct source and manuscript reading, original-detail
source-page inspection, mathematical reconstruction, provenance and rights
inspection, and native SHA-256 identity labels. These reviews establish no
compilation or rendered-handbook result.

## Eight-round revision and review history

No supported finding was outvoted, and no acceptance on an earlier hash was
carried forward to a changed snapshot.

1. **Round 1 — rejected.** Source fidelity accepted; mathematical correctness
   rejected `MP-R1-01`; adversarial publication rejected `AP-R1-01` and
   `AP-R1-02`. The supported repairs supplied an exact normalization for the
   possible zero-length pair sequence, added the necessary empty-
   \(H\) and \(m=0,\ U_0=\varnothing\) branches while preserving Rabin's
   printed nonempty clauses, and removed the undefined redundant modifier
   `full-frontiered`.
2. **Round 2 — rejected.** Source fidelity and mathematical correctness
   accepted. The adversarial seat rejected `R2-AP-01` and `R2-AP-02`: the
   source term `frontiered` lacked its complete first-use standing and
   nonredundancy, and \(f\notin S\) was wrongly called a state. The repair
   defined `frontiered` as the both-children property of the finite
   predecessor-closed node set, distinguished it from predecessor closure, and
   identified \(f\) as an external frontier value.
3. **Round 3 — rejected.** Source fidelity and mathematical correctness again
   accepted. The adversarial seat rejected `AP-01` because an opening history
   paragraph named the two repaired finite-tree objects before their complete
   first-use introductions. The history was made generic; the accepted later
   definitions were retained.
4. **Round 4 — withdrawn before filing.** Before any report was filed, the
   chair found another first-use defect: two passages used a source-defined
   operation name without its definition. All three agents were interrupted,
   and no partial work was treated as a verdict. The repair replaced the name
   with direct prose stating the two coordinate operations required by
   Theorem 1.4.
5. **Round 5 — rejected.** Mathematical correctness and adversarial
   publication accepted; source fidelity rejected `SF-R5-01`. The compact
   record had assigned Lemma 3.14 a frontiered-tree role. The repair restored
   the exact division: Lemma 3.12 supplies the finite-tree lift, Corollary 3.13
   applies it to principal formulas, Lemma 3.14 is the intervening compactness
   result, and Corollary 3.15 returns to the frontiered-tree complementation
   construction. A source-report filing failure was recorded transparently;
   the already-completed blind reviewer restored only its missing report, and
   the rejected decision did not depend on that procedural judgment.
6. **Round 6 — rejected.** Source fidelity and mathematical correctness
   accepted; adversarial publication rejected `AP6-01`. The detailed and
   compact records used Rabin's well-foundedness notion without locally giving
   the exact no-infinite-dependency-chain definition. The repair stated the
   mapping, chain condition, standing, distinction from path acceptance and
   simultaneous-run merging, ordinal characterization, and uses in Lemmas 3.4
   and 3.11.
7. **Round 7 — rejected.** All three seats independently found the same stale
   status contradiction, consolidated as `R7-STATUS-01`. The detailed source
   note's opening required Round 7, but its closing still described an earlier
   review state and directed a fresh Round 6. The history was reconciled
   through Round 7 and made round-neutral where possible. Every seat found the
   mathematics, source roles, terminology, Meyer correction, rights boundary,
   and limited scope otherwise correct.
8. **Round 8 — accepted.** Three entirely fresh seats independently read the
   complete textual snapshot, recomputed the six identities, visually
   inspected every mandated source page, audited all invariants `R01`--`R29`,
   and returned `ACCEPT` on one unchanged snapshot. No blocker, must-fix,
   should-fix, consider, advisory, unread page, identity mismatch, or other
   actionable defect remained.

## Mathematical and source determinations

The three final reviews independently established the following bounded
determinations.

- **Structures and ordinary acceptance.** The presentation retains Rabin's
  root symbol \(\Lambda\), all structures \(T_n=n^*\) for
  \(0<n\leq\omega\), both displayed orders, arbitrary rooted valued trees,
  the distinct transition-table and automaton tuples, and the literal
  one-run/all-paths ordinary acceptance condition with
  \(F\subseteq\mathcal P(S)\).
- **Logical translations.** The full-root bit-track map is a typed bijection.
  Principal recognition, finite-tree lifting, Boolean closure, projection, and
  complement remain separate. The worked formula is labelled handbook-owned.
  The converse uses finite state tracks and the exact
  \(\exists\bar B\,\forall C\) prefix. Closed-sentence truth reduces directly
  to nonemptiness; no later basis theorem is inserted into Rabin's proof.
- **Theorem 3.1 product.** The deterministic word machine, product state set
  \(U\times S\), common first-coordinate update, projected recurring-state
  family, and harmless one-position convention shift are all correctly typed
  and justified. McNaughton's word theorem remains an external dependency.
- **Dual semantics and zero-length case.** The presentation preserves the
  exact type and type-empty clauses and the universal-run/existential-path
  dual prefix, including no-run vacuity. When Lemma 3.6 returns no pairs, the
  handbook-owned \(\Omega^\dagger=((S,S))\) has empty path type and exactly the
  same no-run dual language, so positive-length induction begins without
  inventing a new acceptance condition.
- **Marked obligations and well-founded dependency.** Marked activation,
  simultaneous finite-state copies, same-state merging, path checking, and the
  separate no-infinite-deferral condition all retain their distinct roles. The
  mapping's standing, exact chain definition, ordinal equivalent, and uses are
  supplied before reliance on the name.
- **Finite trees.** The terminal frontier, the both-children property named
  `frontiered`, its nonredundancy from predecessor closure, valuation off the
  frontier, exact transition codomain, and \(f\notin S\) as an external value
  are explicit. Lemma 3.12, Corollary 3.13, Lemma 3.14, and Corollary 3.15 have
  their separate lift, application, compactness, and complementation roles.
- **Emptiness recursion.** The one-letter reduction, complement, dual
  conversion, current-table binding, strict-descendant restriction, finite
  stratum termination, and weak finite-tree base are retained. The
  handbook-owned empty-\(H\) and empty-\(U_0\) branches are necessary,
  mathematically correct, and not attributed to Rabin. The finite weak base is
  not confused with the infinite input theory.
- **Applications and complexity.** The Chapter II application families remain
  at their source-stated class strength. Meyer supplies a growing-tower lower
  bound and the Meyer--Stockmeyer credit for the two-successors-and-prefix
  sublanguage. The resulting correction withdraws Rabin's elementary-recursive
  worst-case claim while preserving decidability and effectiveness.
- **Proof, terminology, and provenance boundaries.** The reader states what it
  reconstructs and what remains in the complete article. Source statements,
  handbook calculations, later results, rights, and completion status are not
  collapsed. The adversarial review found every actual technical name either
  exactly introduced with necessity, definition, standing, nonredundancy, and
  later use, or clearly marked as established source or literature language.

## Admission disposition

The exact Round 8 snapshot is admitted for source acquisition,
reader-facing reconstruction, and topic-level independent manuscript review of
`N-c-014.d` only. The accepted presentation includes the later Meyer complexity
correction and the three explicitly handbook-owned edge-case completions; it
does not convert those additions into claims about what Rabin printed.

The remaining `N-c-014` presentations, `N-c-014` overall, the open
Thatcher--Wright source acquisition, TATA's separate review, Part IX, the other
thirteen parts, the single final publication build reserved until all fourteen
parts are text-frozen, rendered inspection, human review, final-book
completion, and user acceptance remain separate and open.
