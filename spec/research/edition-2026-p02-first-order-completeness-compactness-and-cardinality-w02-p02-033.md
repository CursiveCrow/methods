# w02-p02-033: P2 sections 20.7 and 20.8 (D-P3-013 compactness applications suite)

Packet: work/waves/w02/packets/w02-p02-033.json; label_tag p02-w02-p02-033.

## Gaps addressed (from the independent assessment handed to this packet)

- D-P3-013-GOAL-03: the passage from the elementary embedding of
  thm:p02-upward-ls-elementary-extension (annex:p2.2.20) to a proper
  elementary extension M <= N' of cardinality kappa, with the copy over
  j[M] constructed, proved in general, and the two forms compared.
- D-P3-013-GOAL-02: the Skolem-paradox explanation must say that the model
  satisfies the existence of an uncountable set because the theory proves it
  (Cantor for P(omega)), and that the external extension
  {b in dom M : M |= b in a} is a subset of the countable domain while no
  enumeration of it is an element of the model.
- D-P3-013-C01: composite, depends on the two above; GOAL-01 (nonstandard
  model with finite satisfiability) was assessed as present and is not
  rewritten here.

## Sources and provenance

- No external source for these results is held (spec/coverage/edition-2026/
  held-sources.json has no Hodges1993, Marker2002 or Skolem1923SetTheory
  file; Skolem1923 is the arithmetic paper, a different work). No
  source-specific presentation was written; nothing is attributed to Skolem,
  Hodges or Marker.
- Every argument is an editorial completion built from inherited handbook
  results, cited by label and by frozen-source line interval through the new
  intake key FrozenFormalLogicCompactnessApplications. Line intervals were
  checked in source/formal-logic-reference.tex in this session: 533 (Finite,
  countable, and uncountable sets; Cantor at 584), 4109 (Soundness), 4713
  (Completeness), 4921 (Compactness), 5043 (L-S theorems; downward 5046,
  upward 5097), 6070, 6138, 6243, 6332 (maps, substructures, elementary maps,
  diagrams; iso invariance 6181), 10089 (ZF axioms). 3519-3680 (substitution
  lemma) and 3927-4061 (reduct invariance) match restoration captures
  inherited-03519-03680.tex and inherited-03927-04061.tex read here.
- Design choices: the fresh index r for the copy is Russell's set over the
  first coordinates of pairs in dom M, so neither Foundation nor Choice is
  used. Internal countability is the internal reading of the inherited
  definition (injection into omega). The Cantor argument is run semantically
  in an arbitrary model (only extensionality, power set, separation,
  infinity), then completeness gives the derivation and soundness the
  "because T proves it" direction. The infinity axiom's abbreviations are
  read through Emp and Suc (stated in the reader text, since the inherited
  text does not fix that elimination).
- Hypothesis counterexample for kappa >= |L|: constants c_n and functions
  f_x (x in 2^N) on N; any element outside the image is separated from every
  c_n and the f_x give 2^aleph_0 distinct values. Own construction.

## Existing treatments found (A9)

- Listed: handbook/parts/p02/first-order-completeness-remainder.tex
  (def:p02-elementary-diagram, thm:p02-upward-ls-elementary-extension,
  thm:p02-nonstandard-arithmetic-model, def:p02-skolem-paradox) and its annex;
  the off-route duplicates in first-order-completeness.tex.
- Not listed but relevant: thm:upward-ls and thm:downward-ls
  (restoration/inherited-05043-05131.tex), thm:diagram-tests and
  def:diagrams (inherited-06332-06421.tex, part p03), lem:embedding-image
  (inherited-06138-06242.tex). annex/p03/n-a-003-01.tex lines 604-608 also
  use a one-sentence isomorphic-copy step inside a Vaught-theorem proof; it
  could cite thm:p02-w02-p02-033-copy-over-image. The inherited Cantor
  theorem (inherited-00533-00602.tex) is unlabelled, so it is referenced by
  sec:set-prerequisites-05.

## Patch requests (read-only hosts)

work/waves/w02/patches/w02-p02-033.json: (1) replace the def:p02-skolem-paradox
explanation ('can satisfy') with the because-proved / external-extension
account pointing to the new theorems; (2) insert a pointer after
thm:p02-upward-ls-elementary-extension to the inclusion form and comparison;
(3) replace the unproved copy sentence in annex:p2.2.21 by a reference to the
written construction. Driver insertion lines per the packet proposal are for
the lead.

## Second pass: nonstandard-model suite (D-P3-013-GOAL-01)

The second independent assessment found GOAL-01 partial: only the single
arithmetic corollary (thm:p02-nonstandard-arithmetic-model, via upward LS)
existed on the P2.2 route; no example's own theory had its finite
satisfiability made explicit; the Part 5 direct construction
(handbook/restoration/inherited-09188-09261.tex, thm:nonstandard-model,
def:nonstandard-model, ex:nonstandard-true-arithmetic) was unlinked.

Added subsection sec:p02-w02-p02-033-nonstandard (body), proofs in the annex:
- hbmethod def:p02-w02-p02-033-compactness-method (procedure, side conditions).
- def/lemma numeral map (num_M): elementary embedding, order facts, iso test,
  no least nonstandard element / descending sequence, standard part not
  definable (induction-instance argument).
- thm ...-nonstandard-direct: T_1 = Th(N_ar) + {c != n-bar}, witness
  m_Delta = 1 + max; countable via downward LS; inclusion form via
  copy-over-image (reproves the corollary with one constant); answers the
  Part 5 exercise for T = Th(N_ar).
- thm ...-divisible: T_2 = Th(N_ar) + {c != 0} + {p | c}, witness = product
  of the primes mentioned; Euclid argument (n!+1) written out.
- example ...-fragment-witnesses (42 -> 210; 9 -> 10).
- thm ...-infinitesimal: T_3 = ElDiag(R_of) + {c_a < c}, witness 1 + max;
  elementary embedding proved directly from ElDiag; infinitesimal via
  delta_a sentences; non-Archimedean; inclusion form.
- lemma ...-fs-fails: finite structures refute the analogous theory by one
  finite fragment; no expansion of the witnessing structure satisfies T_i.
- corollary ...-not-axiomatizable: isomorphism type of N_ar, well-ordering of
  <, Archimedean property.
- warning ...-nonstandard-limits.
All content is general mathematics built from inherited results; nothing is
attributed to an external source. New frozen-source intervals cited and
checked in source/formal-logic-reference.tex this session: 8306 (sec
decision-hierarchy-02, def:language-arithmetic) and 9188 (sec
arithmetic-coding-02, def:nonstandard-model, thm:nonstandard-model); bib
intake note updated. The \R macro is restricted to inherited scopes, so the
reals are written \mathbb R.

Patch request 4 added to work/waves/w02/patches/w02-p02-033.json: insert
after thm:p02-nonstandard-arithmetic-model in the parts remainder a pointer
to the direct construction, the further examples, the failure lemma and
(through the new theorem) thm:nonstandard-model.

## Continuation

- All four components have text in the owned files; unit-compile ok
  (12 overfull boxes, all under 16pt except unit-only annex headers);
  check.py shows only the expected bib-key finding for the own intake key;
  find_fused_spaces clean.
- Remaining outside this packet's write scope: apply the four patch
  requests and the two driver input lines (parts/p02.tex after
  parts/p02/first-order-completeness-remainder; annex/p02.tex after
  annex/p02/first-order-completeness-remainder). Until patch (1) is applied,
  the warning def:p02-skolem-paradox itself still says "can satisfy"; until
  patch (4) is applied, the corollary thm:p02-nonstandard-arithmetic-model
  does not itself point to the example suite (the new section does point
  back to it and to thm:nonstandard-model).
