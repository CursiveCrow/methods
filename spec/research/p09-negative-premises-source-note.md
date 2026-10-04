# P9 negative-premise transition specifications: authoring handoff

2 October 2026. This is an author-side source/proof record for planned
section 133.2, not independent review, source-unit admission or publication
acceptance. Proof/source exploration stopped at the bounded 30-minute
point; the following files were saved within the 35-minute block.

## Exact allocation and existing interfaces

Read the exact P9 row in
`spec/coverage/edition-2026/current-fulfillment/p08-p09.jsonl`, section
`133.2`, title **Transition-system specifications, negative premises and
stratification**, and its evidence note. Its source-facet joins are bounded
locator candidates, not complete-source credit. The linked queue units are:

- `ED26-SRC-058-0003`: the 2001 first-edition *Handbook of Process Algebra*
  chapter3, *Structural Operational Semantics*, publisher pp.197--292;
  its whole chapter and all three required components remain allocated.
- `ED26-SRC-058-0101`: the separate 133-page author manifestation
  `WEB-PDF-001-SOS-AUTHOR`; selected C007--C017 cover TSS definitions,
  process examples, model/proof/stratification meanings and applications;
  C064 is the general meanings facet. The whole133-page presentation,
  remaining conservative-extension/congruence/higher-order/denotational
  components and the publisher/author variant comparison remain allocated.

Read the current P9 host/source-standing interface, the finite strong/weak
LTS interval of `presentations/n-c-017.tex:1344--1436`, and the general
action-relation/proposition-valued modal interface of
`presentations/n-c-018.tex:4701--4760`. The new relation is on closed process
terms, with action triples and unary predicates. It does not assume total
transitions, a finite state set or image-finiteness. Predicate judgements
yield proposition valuations; no congruence theorem is inferred from
semantic existence. Read the exact calculus-registry convention and
existing rule-sheet examples before authoring the unique sheet.

## Actual primary bodies and read extent

1. [Exact author SOS PDF](https://www.cs.vu.nl/~wanf/pubs/sos.pdf), Luca
   Aceto, Wan Fokkink and Chris Verhoef, *Structural Operational Semantics*.
   Held `source/references/p09-negative-premises/aceto-fokkink-verhoef-sos-author.pdf`;
   actual physical count133; SHA256
   `FEE86B46154D4ACE6DC265D7BD5F91B140435916F6B8A0FD099A64AA612D5D85`.
   The inspected title material is undated. Read physical/printed pages
   1--3 and15--27, including full selected §§2.5--3.5 and the start of §4.
   Rendered all selected pages as source-only PNGs; visually inspected
   pages17,20,23,24,25,27 for rule shapes, semantic definitions and actual
   stratifications. This is not a full133-page reading or a publisher-body
   equivalence claim. The publisher chapter itself was not acquired/read.
2. [Groote's 1993 article](https://ir.cwi.nl/pub/194/0194D.pdf), *Transition
   System Specifications with Negative Premises*, TCS118, pp.263--299.
   Held `groote1993.pdf`; actual37-page body; SHA256
   `08FCFD4E1711E43D7E24A865F895ADC80B45C63EA379B08F8191CCF4F1835E29`.
   Read physical5--11, printed267--273: exact arbitrary-premise TSS
   definitions, agreement counterexamples, ordinal/regular-cardinal
   construction and complete Theorem2.15 proof. Lemma2.16's statement
   and initial proof were read; no claim is made to have read its remaining
   proof pages or the complete37-page article. Independence is proved
   directly in the new annex through stable uniqueness.
3. `bol-groote1996.pdf` was acquired from the freely served CWI URL
   https://ir.cwi.nl/pub/1339/1339D.pdf ; SHA256
   `57EDA689223AB18A243CBACAF4156F2B2A8E6FE049E016DC1A6109666216CEF0`.
   Its body was **not read** in this block and is not cited as a proof
   dependency or used to close any allocation. Acquiring a file is not
   a source-reading qualification.

The owned helper `read-primary.py` extracts and renders primary pages only.
No manuscript PDF, source export or new publication artifact was generated.
The research/PDF skills guided primary identity and visual source reading;
the no-child instruction was retained rather than spawning another agent.

## Delivered construction and seven reciprocal proofs

- Body `handbook/parts/p09/negative-premises-and-stratification.tex`,
  SHA256 `FF932E93019E00875CEC71B0B009167B322639954B54508F932FED60CD1010A8`.
- Annex `handbook/annex/p09/negative-premises-and-stratification.tex`,
  SHA256 `8B7E5B176982C4B01D26F8A522EA975B78E61716934D61BEA217B1EA5FCC25FC`.
- Unique sheet `handbook/registry/calculi/p09-negative-premises.tex`,
  SHA256 `58CC6F54CC2A27BED6E2B3A288BE92F4524FE900610DF19FEF90E7A7F2F2CB7A`.
- Bibliography intake, SHA256
  `870ED24EA77470C9A56E434595D1ADD0E50816A177E02969BF371ED0050688B5`.
- Eight-row symbol intake, SHA256
  `F2C6C981618E8BCE4DB4574AC302949A6529143D85D9542428880CD93A39F8D7`.

Body/annex prefixes `thm:p09-np-` / `annex:p09-np-` have seven pairs:

- `positive`: arbitrary-premise monotone closure below an infinite regular
  cardinal strictly bounding every positive premise set; full least-model,
  support and well-founded-tree equivalence arguments.
- `stable`: reduct proof restoration/pruning and exact equivalence of
  stable and well-supported models, separate from ordinary circular support.
- `well-founded`: antitone candidate operator, full least squared fixed
  point construction, consistent true/possible bounds and information order.
- `proof-meanings`: universal negative blocking, supported-model soundness,
  three-valued soundness/consistency and constructive ordinal converse for
  both true and false well-founded judgements; totality equals ws-completeness.
- `stratified`: ordinal strata, all potential negative targets below the
  head, actual same-rank least closure and regular bounds, support/modelhood,
  stable uniqueness, choice independence and total well-founded semantics.
  The positive-reduct localization argument is supplied explicitly.
  Strict stratification is separately needed for unique supported modelhood.
- `countermodels`: all six actual source predicate TSSs with explicit
  model/support/reduct calculations; editorial unique-stable-but-unknown
  and infinitary-premise/omega-truncation failures are identified separately.
- `processes`: all nine BPA base rules, both priority rules and six timed
  rules checked against the source's actual occurrence-count ranks; a
  separately proved strict source-size rank and exact process endpoints.

The registry sheet explicitly distinguishes the separate T_i/E/J families,
BPA, priority and time extensions; it does not combine them into one TSS.
It retains standard negative action absence over **every** target and
unary predicate negatives. Target-specific negatives extend only the proof
comparison, as the author source's §3.2 specifies. Predicates are not
silently dropped. No TRS variable-condition or finite-premise hypothesis
was imposed on a general TSS. Choice contains separate both-delay and
one-delay branches, and priority tests every larger action under the stated
strict partial action order. All rule displays are on the assigned unique
registry sheet, not unregistered fractions in the body.

Correction provenance outside exposition: the source's phrase ``two least
models'' for its incomparable examples is mathematically ``two incomparable
minimal models, with no least model''. The new body directly uses the
correct distinction. T6's pair {h,k} is a model but cannot support k;
the active statement and calculation list only its two supported singletons.
No source correction was left as a contradictory reader-facing afterthought.

## Qualification and exact residuals

This supplies the newly authored selected TSS/negative/stratified inference
contribution, not either full SRC058 source unit. Publisher-body acquisition,
the full133-page remainder/variant comparison, supported-proof-to-ws-proof
inclusion and the source's wider answer hierarchy, Groote's dependency-graph
equivalence/remaining article, recursive-priority/abstraction examples,
conservative/congruence formats and higher-order/many-sorted/denotational
contributions remain separate source/proof obligations. No stable uniqueness
claim is substituted for well-founded totality, and no negation-as-failure
search implementation is claimed. The new files are not routed by this writer.
Root owns host/annex drivers, canonical bibliography/symbols and baselines.

The new authoring was inspected directly, with seven reciprocal labels and
the process/rank calculations preserved. No independent review, tests,
build, manuscript render, shared/canonical/driver/baseline edit, paid/login/
contact action or access-control bypass was performed. Earlier Klop packets
and their source notes/intakes remained untouched throughout this P9 block.

## Separate SOS-formats and conservative-extension continuation

New owned body/annex basename `sos-congruence-and-conservative-extension.tex`,
unique sheet `p09-sos-formats` and matching bib/symbol intakes are prepared
for root routing. Frozen NP seven pairs/sheet/intakes and all prior Klop
files stayed unchanged. Host/driver/canonical/baseline work is root-owned.
Final proof-scope clarification was saved at23:03UTC, beyond the intended
30-minute proof stop; no further proof/source exploration followed.

Additional exact author-source reading: physical/printed29--32,40--46,
54--55, and bibliography records112/115. Visually inspected30,31,43,54.
The held133-page source hash is unchanged. Publisher96-page chapter remains
unread and not identified with it. Read literal source Theorem4.4 including
both fresh-source and fresh-positive-premise alternatives; Props4.5--4.6;
panth/ntree definitions and the GSOS finite-language conditions.

Additional primary bodies:

- Fokkink/Verhoef report95/28, *A Conservative Look at Term Deduction
  Systems with Variable Binding*, institutional file
  https://pure.tue.nl/ws/files/2438211/9610579.pdf ;36physicalpages including
  portal/series pages; printed cover October1995. Read physical1--8 and
  16--20, including the actual Theorem3.21/source-distance proof. SHA256
  `7279E3CD2AD9C8C05AD09D1D76EC04120F4FA971CFBC6270DAC4400844098EC1`.
  Not silently substituted for the distinct1998 journal article or its
  many-sorted/binding extensions.
- Bloom/Istrail/Meyer, *Bisimulation Can't Be Traced*, dated July21,2003,
  https://people.csail.mit.edu/meyer/BCBT.pdf ;actual38physicalpages.
  Read1,16--21: exact GSOS conditions, semantic witnessing and congruence
  theorem/sketch, source pattern failure. SHA256
  `5F5D5C4AA8A5E9D3CFE441C38C026AB8926D9C933A97BB7A13464E39BC5B5658`.
  Its cross-reference placeholders are a variant limitation. The separate
  institutional1995 article URL returned404 and was not retried; this
  author file is not relabelled as the1995 JACM final. No guarded-recursion
  or full-abstraction theorem is imported. Rendered dependency source
  pages only; no manuscript render.

Eight reciprocal `thm:p09-sos-` / `annex:p09-sos-` pairs are supplied:
`local-semantics`, `congruence`, `old-proof`, `conservative`, `models`,
`failures`, `applications`, `panth-example`. They include explicit
compatible-closure/substitution/bisimulation induction; full proof-height
and finite source-dependency-distance induction for both freshness cases;
general proof-conservativity reduct projection, interval lifting and least-
pair projection; all nine BPA, two priority, six timed and five new silent
rule types; four condition-failure examples; and the exact source p.44
unique-stable but incomplete panth example with four unknown Q-judgements.

Scope remains explicit: native nonrecursive finitary GSOS is covered.
The predicate-bearing local-input class is a declared subclass, not all
panth. The general complete-panth Theorem5.3 and panth-to-ntree Theorem5.6
remain owed; their older premise-well-foundedness restriction is not
reimposed to manufacture a full theorem. Recursion binders, binding/
many-sorted versions, other equivalences and both whole-source remainders
remain allocated. The semantic projection/lifting theorem assumes general
proof-level operational conservativity itself, not just its sufficient
syntactic criterion. Table-specific timed conservativity is not attributed
to every similarly named later timed language.

Final hashes: body
`4D144370FD22386CAA3D91407470A4C3D369231BAD39F751494FE7F5728871ED`;
annex `DB5F18861674520C612A4942AD2CE1A22AA99F236BCDF726DB4EB041B342B1F3`;
sheet `2FD59543D672374AE8046780F6E78CE97C4C1C93D5071155529D076A3B9FB259`;
bib `E7239A9CB9BD9F8B685498C3FC65CD68BF9EF29F584F9FC0CC05669430F716DB`;
symbols `E5E3915D58CD039D68CFBED796EFCBEA91870C8A056D21C538EECB4CBEA60291`.
The same canonical `AcetoFokkinkVerhoefSOSAuthorNP` manifestation is reused.
No independent review/tests/builds/manuscript renders/shared/canonical/
driver/generated edits, paid/login/contact or bypass actions occurred.
The source-note continuation records actual partial source/proof standing,
not full-unit admission or acceptance.
