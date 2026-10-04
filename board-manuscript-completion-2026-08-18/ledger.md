# Board ledger

Opening citations were verified against the live files. Overlapping opening
records are merged below with every originating seat retained.

### F1 [must-fix] [accepted] General-TBox tableau omits successor propagation
- author: topic-specialist r1
- location: Part IX, ALC tableau
- claim: internalized GCIs are placed only at the root; `top <= A` with `exists r.not A` is a counterexample.
- correction: add every internalized GCI to every existing/new node and restate blocking.
- disposition: fixed; R2 topic verification accepted the propagated TBox rules and blocking boundary.

### F2 [must-fix] [accepted] HSP convention leaves the empty class ambiguous
- author: topic-specialist r1
- location: Part X, HSP theorem and glossary
- claim: the theorem needs either a nonempty-class hypothesis or an explicit empty-product convention.
- correction: state the empty-product/trivial-algebra convention explicitly.
- disposition: fixed; the theorem now states the nonempty-class/empty-product convention explicitly.

### F3 [must-fix] [accepted] Logic-program grounding is ill typed
- author: topic-specialist r1
- location: Part IX, definite and stable programs
- claim: substitutions need not ground all variables, and stable-model grounding is unstated.
- correction: quantify over ground instances and fix the finite propositional/ground representation.
- disposition: fixed; grounding is total on clause variables and stable models are defined on the declared ground representation.

### F4 [must-fix] [accepted] MV-algebra lacks an exact equational basis
- author: topic-specialist r1; adversarial-publication r1
- location: Part X, MV-algebra definition
- claim: “standard Chang equations” is not an eliminable definition.
- correction: display a complete universally quantified equational basis.
- disposition: fixed; the complete MV-equational basis is displayed.

### F5 [should-fix] [accepted] Monadic decidability lacks its function-symbol boundary
- author: topic-specialist r1
- location: Part IX decidable fragments and Part XIV decision table
- claim: “unary predicate fragment” does not say whether positive-arity functions are allowed.
- correction: fix the relational signature, constants, equality, and no-positive-arity-function convention.
- disposition: fixed; the monadic signature now permits constants and excludes positive-arity function symbols.

### F6 [must-fix] [accepted] MLTT sheet cannot derive its universe judgments
- author: topic-specialist r1
- location: `handbook/registry/calculi/mltt-intensional.tex`
- claim: the Universe rule assumes the judgment it is meant to introduce; context, conversion, cumulativity, and closure are missing.
- correction: add exact context/conversion/universe rules or withdraw the completion claim.
- discussion: topic-specialist r4 accepted the typed computation rules but found the congruence schema term-sorted only; the post-r4 repair defines equality premises separately for type and term judgments and transports dependent telescopes explicitly.
- disposition: fixed at source; final topic-specialist poll accepted the post-r4 multi-sorted congruence repair.

### F7 [must-fix] [accepted] DPLL(T) loses negative literals and overclaims model reconstruction
- author: topic-specialist r1
- location: Part XII, DPLL(T) state/proof
- claim: the abstraction map covers only true proxies; equisatisfiability alone gives no model projection.
- correction: map signed literals and state a definitional-extension/model-reconstruction invariant.
- disposition: fixed; the abstraction is polarity-preserving and clausification carries explicit extension/projection invariants.

### F8 [must-fix] [accepted] Selected omega calculus has no exact base calculus
- author: topic-specialist r1; adversarial-publication r1
- location: Part VII omega section and `omega-arithmetic.tex`
- claim: the text names PA-omega but leaves finitary rules, induction embedding, and ordinal data to an unnamed source.
- correction: bind an exact base calculus/embedding or restore an explicit owed-artifact boundary.
- discussion: topic-specialist r4 verified the live rules, indexed derivability relation, cut-rank bound, and `2_n(alpha)` theorem against Jäger--Probst Definition 1/Theorem 2; the post-r4 repair corrected the sole remaining term/relation-symbol sentence.
- disposition: fixed at source; final topic-specialist poll accepted the exact calculus and corrected language grammar.

### F9 [blocker] [accepted] Inherited bibliography semantic review is pending
- author: source-fidelity r1; topic-specialist r1; adversarial-publication r1
- location: `spec/provenance/inherited-bibliography-field-ledger.csv`
- claim: 64 static passes do not establish author/editor, container, edition, or date semantics.
- correction: independent row-by-row semantic comparison and exact corrections.
- disposition: fixed; all 64 ordered semantic decisions are now generated into the ledger with the independent transcript path and SHA-256 pinned per row.

### F10 [must-fix] [accepted] Skolem arithmetic cites the wrong paper
- author: source-fidelity r1
- location: Part V decidable arithmetics; `Skolem1934`
- claim: the 1934 noncharacterizability paper is not the multiplication-theory source.
- correction: add/cite the verified 1930 paper and a later decision-proof source as needed.
- discussion: source-fidelity r4 verified Rackoff's primary fixed-height space bound; the current theorem cites that article and states the elementary-recursive bound exactly.
- disposition: fixed.

### F11 [must-fix] [accepted] Consistency-presentation prose cites the wrong Feferman paper
- author: source-fidelity r1
- location: Part V independence catalog; `Feferman1964`
- claim: Systems of Predicative Analysis is not the general-arithmetization source.
- correction: cite Feferman’s 1960 arithmetization paper.
- disposition: fixed; the Feferman 1960 arithmetization paper is now cited.

### F12 [must-fix] [accepted] Equational completeness cites Birkhoff 1944
- author: source-fidelity r1
- location: Part X equational completeness
- claim: the 1944 subdirect-union paper is not the completeness source.
- correction: use `Birkhoff1935`.
- disposition: fixed; equational completeness now cites Birkhoff 1935.

### F13 [must-fix] [accepted] Biography capsules have no source apparatus
- author: source-fidelity r1; adversarial-publication r1
- location: Part XIII capsule section
- claim: forty date/attribution clusters have no citations or exact source links.
- correction: cite each capsule or tightly delimited group, using authoritative histories for ancient/fragmentary evidence.
- discussion: source-fidelity r4 accepted the capsule claim scopes but found two bibliography-role errors; the post-r4 repair records Girard as author, Taylor as translator, Taylor/Lafont as appendix contributors, and the 1972 work as a doctorat d'Etat thesis.
- disposition: fixed; final source-fidelity poll accepted the capsule sources and corrected contributor/thesis roles.

### F14 [must-fix] [accepted] Master-table rows lack promised destinations
- author: source-fidelity r1
- location: Part XIV decision, strength, and expressive tables
- claim: most rows have neither a citation nor a destination despite the chapter’s promise.
- correction: add one exact source-bearing link/citation to every substantive row.
- disposition: fixed; every substantive master-table row now carries a source-bearing citation or destination.

### F15 [blocker] [accepted] Named-theorem index is only an eighteen-row selection
- author: adversarial-publication r1
- location: Part XIV named-theorem table; apparatus A-159
- claim: it omits most live theorem/lemma labels and annex destinations.
- correction: generate it from every live named theorem/lemma with statement and proof/detail destinations.
- disposition: fixed; the generated index contains all 335 live theorem/lemma rows and their proof/detail status destinations.

### F16 [must-fix] [accepted] Symbol/person index descriptions are false or incomplete
- author: adversarial-publication r1
- location: Part XIV index-surfaces section
- claim: symbol registry points to the wrong chapter and lacks page/principal-use links; capsules are not alphabetized.
- correction: point to Part I, generate page-linked symbol/person surfaces, or accurately describe the remaining open work.
- discussion: adversarial-publication r4 verified 569 one-to-one registry anchors and compact-index links.
- disposition: source-fixed; final person/symbol sorting, pagination, target, and layout approval requires the single final build and visual audit.

### F17 [must-fix] [accepted] New calculus sheets do not carry controlling sources/dependencies
- author: source-fidelity r1; adversarial-publication r1
- location: new registry calculus sheets and Part XIV rendering
- claim: source names are comments/remote prose; affine and omega dependencies are raw or unnamed.
- correction: put reader-facing exact citations and linked dependency names on every affected sheet.
- disposition: fixed at source; all eleven agenda sheets carry controlling citations and named dependencies. Citation rendering remains a final-build check.

### F18 [must-fix] [accepted] Page-furniture mapping is adaptation, not exact reconstruction
- author: source-fidelity r1
- location: `PRE-00049-00055.json`, source lines 49--55, `handbook.sty`
- claim: fancyhdr source furniture differs from the integrated alternating headings.
- correction: explicitly classify/document the authorized layout adaptation or reproduce it exactly.
- discussion: adversarial-publication r4 withdrew the demand for a new undefined classification: the mapping fields retain historical audit standing while the live destination explicitly records non-identical adaptation and `open/missing` disposition.
- disposition: source-fixed; running heads, folios, scaling, navigation, and legibility require the single final build and visual audit.

### F19 [must-fix] [accepted] Unified bibliography hides inherited/editorial provenance
- author: source-fidelity r1
- location: `handbook/main.tex` bibliography printing
- claim: comments divide the database but the rendered bibliography does not.
- correction: use one Bibliography chapter with labeled inherited/editorial subbibliographies.
- disposition: fixed at source; one Bibliography chapter prints separately labeled inherited-source and editorial sections.

### F20 [must-fix] [accepted] TB, CT, KF, and FS are underdefined
- author: adversarial-publication r1
- location: Part XI axiomatic truth section
- claim: base theory, language, truth axioms/rules, and induction packages are unspecified.
- correction: fix exact variants or replace the abbreviations by a nontechnical survey boundary.
- disposition: fixed; the text now treats the four acronyms only as variant-indexed survey families and states the parameters required before any formal theorem.

### F21 [must-fix] [accepted] Ordered-superposition factoring hides side conditions
- author: adversarial-publication r1
- location: `ordered-superposition.tex`, Equality Factoring
- claim: “standard ordering side conditions” collapses distinct calculi.
- correction: state every unifier, eligibility, maximality, and ordering condition explicitly.
- disposition: fixed; the sheet states the unifier, eligibility, maximality, and ordering conditions explicitly.

### F22 [must-fix] [accepted] S1S and S2S are undefined one-use acronyms
- author: adversarial-publication r1
- location: Part IX automata section
- claim: neither structure/language is defined before the decidability claim.
- correction: define monadic second-order theories of one and two successors, or remove the acronyms.
- disposition: fixed; S1S and S2S are defined before the decidability claims.
