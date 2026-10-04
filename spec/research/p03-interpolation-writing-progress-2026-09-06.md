# Model-theoretic interpolation and definability

The live Part III already contained short Robinson and Beth proofs.
This pass expands the model construction, supplies the exact
Craig--Robinson equivalence, and corrects the unsupported ordinary
Beth-to-Craig reduction. It completes the model-theoretic proof writing
requested by N-a-013.

## Actual mathematical content

- The new elementary-reduct extension lemma is proved from the union of
  two elementary diagrams with shared parameter constants. Finite
  satisfiability reflects existential statements through an elementary
  reduct inclusion. Compatible elementary embeddings are transported to
  literal inclusions.
- Robinson's proof constructs a complete common theory from the union
  of the two sets of common-language consequences. It then embeds one
  model's reduct inside a model of the other theory and alternates
  elementary extensions. The two elementary unions share a domain and
  every common interpretation, producing a joint model.
- A fixed cardinal and fresh domain blocks make the recursive choices
  set-sized. The ambient Choice assumption is explicit. Constants,
  functions, nullary predicates, equality, and arbitrary signatures are
  covered.
- The earlier Stone-space common-completion argument and the
  Keisler--Shelah ultrapower route are retained as alternative arguments,
  with their logical steps and theorem references made explicit.
- The direct Robinson-to-Beth proof now includes arbitrary theories,
  arity zero, inconsistent-side cases, capture-avoiding parameter
  elimination inside terms, repeated parameter values, and one uniform
  finite supporting subtheory.
- The equivalence proof supplies Craig-to-Robinson by compactness and
  Robinson-to-Craig by the separator theorem. It handles the bottom/top
  cases before applying joint consistency to consistent component
  theories, and recovers the common-free-variable condition.

The correct relationship in the book is Craig iff Robinson, with either
implying ordinary Beth. The former purported reverse construction allowed
private vocabulary in the explicit definition. The precise diagnosis and
primary-source evidence are in p03-craig-robinson-beth-source-note.md.
The book now gives the valid theorem and a worked vocabulary example.

## Files and proof links

The body remains handbook/parts/p03/preservation-abstract-logic.tex.
The actual proofs are in handbook/annex/p03/editorial-proofs.tex:

- annex:p3.abstract.4: elementary-reduct extension;
- annex:p3.abstract.1: Robinson joint consistency;
- annex:p3.abstract.2: Beth definability;
- annex:p3.abstract.5: Craig--Robinson equivalence and the Beth consequence.

Part VII now links to this independent model-theoretic route.
The named-theorem index has been updated for these results and the
interpolation and modal-completeness results written in the preceding pass.
The inactive Part III lookup table has been corrected locally, but remains
unrouted as before; its broader navigation issue is a separate obligation.

## Verification

Independent bounded readers checked the actual diagram-extension and
Robinson proofs, the common-completion step, the revised Beth proof,
the equivalence proof, and the paired theorem statements. They found no
concrete mathematical defect in those scopes. The cardinal-bound
paragraph explicitly transports the initial pair of models together,
preserving their inclusion.

The supporting independent derivations are
p03-robinson-elementary-chain-proof-note.md and
p03-robinson-separation-proof-note.md.
This records completion of this proof-writing obligation, not publication
readiness of the entire manuscript.
