# Board charter: manuscript completion batch

- Artifact: the current reader-facing manuscript additions and replacements listed below in `work/formal-logic-handbook`.
- Purpose: determine whether the newly written material is accurate, source-supported, complete enough for its stated scope, internally coherent, and publication-safe before any final build.
- Mode: audit.
- Requested by: the governing objective requires independent source-fidelity, topic-specialist, and adversarial-publication AI reviews for every reader-facing topic.
- Authorship disclosure: chair-authored in this thread; no seated reviewer may treat the chair's static checks as substantive approval.
- Invariants:
  - I1: The public product is one book titled *The Methods of Reason*, with the fixed fourteen-part organization. (stated by user)
  - I2: Exact inherited artifacts remain byte-faithful; editorial additions remain separately identified and do not replace, alias, or upgrade inherited claims. (stated by user)
  - I3: Definitions precede use; theorem statements include all types, quantifiers, hypotheses, side conditions, and exact proof status. (stated by user)
  - I4: A new technical name has colocated necessity, exact definition or axiom, standing, nonredundancy, and later use. (stated by user/AGENTS.md)
  - I5: Source fidelity, mathematical correctness, static validation, compilation, visual review, AI review, and user acceptance remain separate claims. (stated by user)
  - I6: No reader-facing stub, unsupported addition, collapsed variant, undefined reference, or uncited external claim may remain. (stated by user)
  - I7: A proof annex may provide navigation or additional proof detail but may not be the sole reader-facing location of an inherited proof. (stated by user)
- Criteria:
  - C1: claims and definitions match their cited authorities or explicitly stay at a cited/sketch boundary;
  - C2: mathematical statements and locally supplied arguments are correct as written;
  - C3: the requested register topics represented by each former stub are substantively present, not merely renamed;
  - C4: notation, terminology, labels, cross-references, proof statuses, and variants are coherent with the live handbook;
  - C5: the prose is graduate-reference quality, definition-before-use, and does not hide an open obligation behind a new name;
  - C6: publication/navigation risks and likely rendered-layout failures are identified without treating a static pass as a visual pass.
- Severity taxonomy: blocker, must-fix, should-fix, consider, discard, unresolved-user.
- Source rule: artifact claims cite exact file:line locations; external claims cite a fetchable primary or authoritative source; unverified claims cannot block consensus.
- Consensus rule: rough consensus per rule 8; opening round plus at most two deliberation rounds.
- Roster:
  - source-fidelity: independent reviewer of exact authority, bibliography, citations, variant separation, and claim/source correspondence;
  - topic-specialist: independent formal-logic reviewer of definitions, theorems, proofs, types, quantifiers, side conditions, and complexity claims;
  - adversarial-publication: independent reviewer for omissions, unsupported additions, terminology conflicts, labels, references, index/bibliography coverage, trust boundaries, and likely page defects.
- Board type: live.
- Workspace: `board-manuscript-completion-2026-08-18/`.

## Artifact lots

1. Part V: `handbook/parts/p05/{provability-logic-gl,decidable-arithmetics,independence-catalog,reverse-mathematics}.tex`.
2. Parts IX--XI: `handbook/parts/p09/logic-in-computer-science.tex`, `handbook/parts/p10/algebraic-and-categorical-logic.tex`, `handbook/parts/p11/philosophy-of-logic.tex`, and `handbook/annex/p09.tex` through `p11.tex`.
3. Parts XIII--XIV: `handbook/parts/p13/chronology-and-biography.tex`, `handbook/parts/p14/{rule-sheets,master-tables}.tex`.
4. Closed former stubs and new sheets in Parts II, III, VI, VII, VIII, and XII: changed files under `handbook/parts/p02`, `p03`, `p06`, `p07`, `p08`, `p12`, plus the newly added files under `handbook/registry/calculi/`.
5. Backmatter/source accounting: `handbook/bib/handbook.bib`, `spec/provenance/inherited-bibliography-field-ledger.csv`, and restoration/provenance records from `SRC-16743-16801` through `CTL-17206-17206` plus the eight preamble/control records.

Opening-round cap: at most 12 findings per seat; every seat must report checked-clean coverage for every lot it actually inspected and explicitly list anything not checked.
