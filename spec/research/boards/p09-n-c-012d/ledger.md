# N-c-012.d review ledger

## Round-one status

The exact round-one source and manuscript snapshot is frozen in `charter.md`.
All three independent scholarly reviews are complete on that same snapshot:

- source fidelity: `REVISE`, transcript SHA-256
  `E8663895D6C83386791A9787337C6D9A866925226BC58E661338B969FA33FB07`;
- mathematical/proof: `REVISE`, transcript SHA-256
  `F7AF2686F50692E8A139A68E9927377B810A9A95F1817F434AE5B5DE3412FB5F`;
- adversarial publication/AGENTS: `REVISE`, transcript SHA-256
  `18005B767EEA69476F7BA8550C78742151FC8694115DEC9D59C74995202699AF`.

Every supported finding is admitted; no majority rule applies. The consolidated
round-one repair obligations are:

1. correct the journal page map for the p. 735 sequence definitions and the
   p. 748 conclusion;
2. record that conference p. 160 prints the universal validity clause which
   journal pp. 734--735 omit, while keeping the handbook clause reconstructed
   relative to the journal;
3. say only that an unidentified theorem used in the conference proof contained
   an error;
4. state that each Figure 2 diamond represents one tape-cell position and that
   a complete BI-to-EI traversal represents one instantaneous description;
5. define the source's model-level valuation periodicity, including the natural
   starting index and positive period, and keep it distinct from source-truth-set
   equality and obligation discharge;
6. restore the exact hypotheses and intermediate-supersequence quantifiers of
   Lemmas 3.2, 3.3, and 3.6;
7. restore the journal convention that accepting and rejecting configurations
   persist forever without tape changes, and record its difference from the
   conference's halting language; and
8. replace unsupported proof-tree and derivation-tree synonyms with the source's
   labelled tree `Gamma(S,j,N_i)`.

The round-one snapshot is rejected and remains open pending repair and a new
three-seat review of one common round-two snapshot.

## Round-two status

All eight admitted obligations were repaired by direct source comparison and
prose editing. The repaired reader subsection now spans lines 1851--2314. The
exact nine-object round-two snapshot is frozen in `charter.md`; its changed
reader-facing hashes are:

- reader: `48D2F8F946AFFC394613D7895E89175099CC9FA73800BDA36A3C5F63353C6AD5`;
- shared Part IX text: `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F`;
- source note: `D7E85E5AC951C56F607099A5756C1AA5CEEC02DB8D0CC3EC359E17EBE2450FCD`;
- source-presentation ledger: `D5BD9F8BA7A12AFD7A8A08CDAAFB2E0E4C0E0B48E0BD83D5BDC06AA08D2E8353`.

The sources and bibliography remain byte-identical. Three fresh blind
round-two reviews are assigned. No round-two verdict has been admitted, and
the topic remains open.

## Round-two outcome

All three reviews were filed on the unchanged round-two snapshot:

- source fidelity: `ACCEPT`, transcript SHA-256
  `1EACCB52B178F880243903AEF9BFAC78DC2D6DF37CA3D44E51ED9C8666AFD60B`;
- mathematical/proof: `REVISE`, transcript SHA-256
  `9791C65A53B0DCC35CBF0D7073C4834F157E70D580B1304D3AEAE8D964E1A718`;
- adversarial publication/AGENTS: `REVISE`, transcript SHA-256
  `FAA83BA518CA7D1C3DA7D2A3AE9E00A321BDE46A20719C3BCC4761B00EF26C64`.

The acceptance does not override either supported rejection. The round-two
snapshot is rejected. The admitted round-three repair obligations are:

1. define the unique maximal suffix `final(S)` and the exact decomposition and
   structure-level measures before use;
2. define the ambient-structure-relative `init`, `final`, `range`, and `size`
   operations on acceptable subsequences, and record the acceptable-union
   subadditivity fact used by the conjunction induction;
3. define `mu(f)` before the Lemma 3.3 bound;
4. replace the vague Theorem 3.5 membership certificate with the explicit
   `length(f) card(N)` prefix bound, strongly connected subset, connecting-edge,
   connectivity, and subformula-label checks; and
5. add a distinct `SistlaClarke1982` bibliography record and use version-
   separated conference and journal citations for every direct STOC claim.

The topic remains open pending repair and a common frozen round-three review.

## Round-three status

All five admitted round-two obligations were repaired by direct comparison
with printed pp. 735--739 and by prose editing. During that comparison, an
enlarged reread of p. 736 established that the preparatory acceptable-union
sentence itself literally prints a strict `<`, while the following conjunction
proof uses `<=`. The strict sentence fails for two null subsequences. This
additional source-visible conflict is admitted rather than hidden: the reader,
source note, source-presentation ledger, I7, C3, M04, and new M26 all
distinguish the literal sign from the proof-supported non-strict
subadditivity fact.

The repaired reader subsection now spans lines 1851--2387. The ten-object
round-three snapshot is frozen in `charter.md`. Its newly generated p. 736
reading crop and reader-facing hashes are:

- p. 736 acceptable-subsequence crop:
  `C267D4B4DF785F9A7E82123B068662E45D7E2C87CB18C24D7B8EB0B875AF413B`;
- reader:
  `1F5792A97766A695A58EF5FAA259F97D8CD6E50B720FB14BEDEA358E3505E7F8`;
- shared Part IX text, unchanged:
  `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F`;
- bibliography:
  `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B`;
- source note:
  `3C1F2DEB6D3224D61E1008B59DF353F56BE096A951E936B0060C583497E37565`;
- source-presentation ledger:
  `414CFAEF19DB8F53B76E6A4805EA20F3D2DABFCA245FC0DD6F537FE32F8253DE`.

Three fresh blind round-three reviews were assigned on that common snapshot.

## Round-three outcome

All three reviews were filed on the unchanged round-three snapshot:

- source fidelity: `REVISE`, transcript SHA-256
  `654A0FE0D6A6E48CACE30E44790D95D60016FB50CD1111267D8C2BD202D0F194`;
- mathematical/proof: `REVISE`, transcript SHA-256
  `95C1207C5916C68D7953426CBD629966807F0B864AC0ED00E303E0A56F7AC535`;
- adversarial publication/AGENTS: `REVISE`, transcript SHA-256
  `7A439DF17BCB7649DC9FCE807B05C8E4CFBE7D172C22851FCF314B3F75394BCD`.

The chair read all three transcripts completely and admitted every supported
finding without voting. The round-three snapshot is rejected. The consolidated
round-four repair obligations are:

1. change the journal `2S(n)` pinpoint from printed p. 742 to printed p. 741,
   retaining conference p. 164 and the broader journal pp. 741--742 locator;
2. reconstruct Theorem 3.5's exact bottom-up labelling procedure: empty
   initialization, increasing-length order, the atomic, negation, conjunction,
   and `F` iff clauses, and acceptance exactly when `f` occurs in the start
   label;
3. preserve the literal p. 738 strong-connectivity/entry-edge check, disclose
   that it does not exclude a loopless singleton under ordinary reflexive
   strong connectivity, give the concrete soundness problem, and clearly own
   the added directed-cycle requirement as a handbook correction;
4. state Lemma 4.3's exact `X`-based graph reduction and its distinct
   self-loop-sensitive two-case pure-`U` replacement, including the precise use
   of Lemma 4.2;
5. state the exact deletion map and common-state conclusion of Lemma 4.5, and
   both exact conclusions of Lemma 4.6;
6. state the five directional Boolean/`X`/`U`/`S` recurrence checks used by
   Theorem 4.1, retaining the initial-since, loop, fulfilment, space, and
   Savitch conditions;
7. state Lemma 5.2's added negated-grammar hypothesis and its inheritance of
   both Lemma 4.6 conclusions; and
8. state Theorem 5.4's positive continuation/terminal production iff rule,
   negative-tracker singleton initialization, exact frontier update, and
   within-period emptiness condition.

The mathematical seat also disclosed that the orchestration layer delivered
an unsolicited completion notification from another seat after its own source
audit. It did not open or use the other transcript, but literal blind
non-exposure was no longer perfect. After substantive repair, every seat must
therefore be rerun on one new snapshot without cross-seat completion
notifications being delivered before filing.

## Round-four status

All eight admitted round-three obligations were repaired by direct reading of
printed pp. 738--748 and prose editing. The reader now gives the complete
Theorem 3.5 labelling algorithm; preserves the literal strong-connectivity and
entry-edge test; supplies the loopless-singleton counterexample; and owns the
directed-cycle condition as a handbook correction. It gives the exact Lemma
4.3 reduction, Lemma 4.5 deletion, both Lemma 4.6 conclusions, all five
Theorem 4.1 recurrences, the full Lemma 5.2 inheritance, and both the positive
and negative Theorem 5.4 rules. The journal `2S(n)` pinpoint is now p. 741.
Every new auxiliary name is defined locally as eliminable metalinguistic
bookkeeping and distinguished from the nearby semantic objects.

The repaired reader subsection spans lines 1851--2589. The common ten-object
round-four snapshot is frozen in `charter.md`. Its reader-facing hashes are:

- reader: `45E2B1F4A97B1049247FD198CDF69C67794D129AEB28582FE595DC34EDF7ABD8`;
- shared Part IX text, unchanged:
  `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F`;
- bibliography, unchanged:
  `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B`;
- source note:
  `1E734EF089EEA077DE90229411726D85708A102D914EFE4F7956B7DDE9EE9094`;
- source-presentation ledger:
  `40F0AE94BB9B763F941B421F63854B17A426C1989084F6262ACD59071C0A7E8D`.

Before any verdict was admitted, the chair noticed that the compact source
presentation used `bar f` without defining the tuple abbreviation. The first
round-four freeze was withdrawn, all three running seats were interrupted,
and the abbreviation was given an exact eliminable metalinguistic definition,
standing, distinction, and local use. The hash above is the controlling
corrected round-four freeze. Round four is open for three fresh isolated
scholarly reviews. The repair and freeze used no test, test harness, automated
checker, repository script, TeX, handbook-PDF inspection, or build.

## Round-four outcome

All three transcripts were filed independently on the unchanged corrected
round-four snapshot:

- source fidelity: `ACCEPT`, transcript SHA-256
  `061B66571802596C38CC5D003FF21EFC7FF8F11804FF429F5C53DDC3F3A59E14`;
- mathematical/proof: `REVISE`, transcript SHA-256
  `16D5A0017A558868D10D95F62BB4161F34C2124897358462BEB24D9618FCDE73`;
- adversarial publication/AGENTS: `REVISE`, transcript SHA-256
  `A4647E76D2F62C7CF25F8193111B5A1D500CA177C150DAA0211AC9ECDADAD6B4`.

The chair read every transcript completely. No vote was taken: both supported
rejections keep the topic open. The admitted round-five obligations are:

1. define `SF(f)`, its single-negation closure and double-negation convention
   before the Theorem 3.5 certificate first uses it, while preserving the
   distinction between closure cardinality and the later realized-type count;
2. bind the certificate's `q_0` explicitly to the supplied `R`-structure start
   state in the reader and both supporting source records;
3. replace the strict handbook phrase “later than” in the prefix `F` rule with
   a current-position-inclusive relation. Preserve the source's word “after,”
   explain its necessarily non-strict contextual reading from inclusive `F`
   semantics and the p. 737 proof use, and keep this repair separate from the
   directed-cycle correction; and
4. bind one consistent ETL terminal/argument arity through the constructor,
   `Gamma`, Lemma 5.2, Theorem 5.4, and the source records.

The acceptance confirms that the remaining identity, attribution, and source
surface is clean; it cannot outvote these proof and publication defects. The
round-four snapshot is rejected.

## Round-five status

All four admitted round-four obligations were repaired by direct source
reading and prose editing. The reader and both source records now define
`SF(f)` exactly before the reviewed certificate uses it, including the
single-negation mates, double-negation elimination, closure bound, standing,
and distinction from the realized-truth-set count. Every surface binds
`q_0 := δ` before the prefix and acceptance clauses. The prefix `F` rule
now permits a witness at the current occurrence, preserves the paper's word
“after,” explains its non-strict contextual reading from inclusive semantics,
and keeps that issue separate from the directed-cycle correction. The ETL
constructor, `Gamma`, Lemma 5.2, and Theorem 5.4 use the one bound arity `n`;
the only remaining bare `q` discloses the source variable being alpha-renamed.

The repaired reader subsection spans lines 1851--2622. The exact ten-object
round-five snapshot is frozen in `charter.md`. Its reader-facing hashes are:

- reader:
  `C760B8B413937A9002F017704956EBFFB2AF7ED44AD8AD8FF0EC4366E526EC79`;
- shared Part IX text, unchanged:
  `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F`;
- bibliography, unchanged:
  `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B`;
- source note:
  `79E0677D27769153BC5C078242CDD77916350B926C87B25F91F78A9C943F0F19`;
- compact source presentation:
  `9739EBEE2BBE5F24857B9C900F831B7F9783F5BAA00652E02E3F5DD755E08D22`.

Round five is open for three fresh isolated scholarly reviews on that common
snapshot. No test, test harness, automated checker, repository script, TeX,
handbook-PDF inspection, or build was used.

## Round-five outcome

All three transcripts were filed independently on the unchanged round-five
snapshot:

- source fidelity: `REVISE`, transcript SHA-256
  `B657B256C1A13125341BB7F45F00F09F01D152B43A02C88E124D5B33BFEFA6AB`;
- mathematical/proof: `REVISE`, transcript SHA-256
  `A58167217B11596CFADD945109B71B4EC327FC1DAB84DF21197BAEA9B87E3C17`;
- adversarial publication/AGENTS: `REVISE`, transcript SHA-256
  `E87CEF5BEF71921FA64C5C8F2F65C23039D9E29ACFA5B8C173CA21BFB28AD5FB`.

The chair read every transcript completely. All three seats independently
found the same exact-typing defect. The round-five text reserved `n` for
grammar terminal count and constructor arity, then rebound `n` as total
encoded input length immediately before reusing `N_j(f_1,...,f_n)` in the
Theorem 5.4 positive and continuation rules. Those quantities are independent.
The compact presentation's local tuple was well bound, but its consistency
claim was therefore premature. No vote was taken; the round-five snapshot is
rejected.

The single admitted round-six obligation is to keep `n` as terminal count and
constructor arity, give total encoded input length a distinct exact binding on
all three surfaces, use that distinct variable in the `card(SF(f))` input-size
bound, and preserve every earlier repair.

## Round-six status

The admitted collision was repaired by direct source reading and prose
editing. The constructor, `Gamma`, Lemma 5.2, and both Theorem 5.4 rules keep
arity `n`. The source's independent Theorem 5.4 input-length variable is now
alpha-renamed to `ell_in` on the reader, source-note, and compact surfaces.
Each location defines it as the complete encoded formula-and-grammar length,
states its eliminable metalinguistic standing, distinguishes it from arity
`n` and fragment notation `L(O_1,...,O_k)`, and uses it in
`card(SF(f)) <= 2 ell_in`.

The repaired reader subsection spans lines 1851--2631. The exact ten-object
round-six snapshot is frozen in `charter.md`. Its reader-facing hashes are:

- reader:
  `C25353424D7DF38678F8AAC7BB421DD1DCCF2E1289643E114425D0F2BEA31DEA`;
- shared Part IX text, unchanged:
  `961D7BEDF28236024505EB96E89269D19FA7C3E0EE8A3E427C9D71263493F18F`;
- bibliography, unchanged:
  `F258FB9BF2AFE158F69C30DEAFE1CF499E181836C138FFEB260B3C39E0F9573B`;
- source note:
  `9390C6A525C88E247BC5C892B4522EDF1CCECA466DA577DDAC1230E3A350FA4B`;
- compact source presentation:
  `1F36F2BCAFE8E1BB8599610EA1ECAAC7E204CC7847674696E9A50D0F3F8918B5`.

Round six is open for three fresh isolated scholarly reviews on that common
snapshot. No test, test harness, automated checker, repository script, TeX,
handbook-PDF inspection, or build was used.

## Round-six outcome and topic admission

All three transcripts were filed independently on the unchanged round-six
snapshot:

- source fidelity: `ACCEPT`, transcript SHA-256
  `30C808BE930AE34892BA0B2D27A6A4B850E87D9F1D0ADF47E5F575B2450C39E3`;
- mathematical/proof: `ACCEPT`, transcript SHA-256
  `39B341A10610CDB93D68ED7E3C1C97192BDED250A5D80F22000466A2C830A0F9`;
- adversarial publication/AGENTS: `ACCEPT`, transcript SHA-256
  `7220F7C25BA966668D0C02E8C74FC5CF5B4389A744DC7D639B59B5C941AC7CF3`.

The chair read every transcript completely and independently recomputed the
ten frozen identities after filing; all remained exact. Every seat freshly
read all seventeen journal and ten conference pages and reports exhaustive
checked-clean coverage of C1--C9, I1--I15, and M01--M44. No seat reports a
blocker, must-fix item, uncertainty, unread page, or identity mismatch. No
vote was taken and no earlier acceptance was carried forward.

The exact round-six snapshot is therefore admitted for reader-facing body
reconstruction and topic-level manuscript review of `N-c-012.d` only. The
admission preserves the disclosed source defects, source-context
reconstructions, handbook-owned corrections, proof-strength qualifications,
conference/journal separation, and rights limits; it does not certify the
source's defective printed statements as correct mathematics.

The durable admission record is
`spec/research/p09-n-c-012d-independent-review-record.md`, SHA-256
`B993116E4FCA3AEE34AACD0CC47433C0C40F2B695DF45B93857233C1009882DB`.
The compact source-presentation file was then changed only to record the
unanimous verdict and link that admission record. Its accepted pre-admission
hash remains `1F36F2BCAFE8E1BB8599610EA1ECAAC7E204CC7847674696E9A50D0F3F8918B5`;
its post-admission status-only hash is
`FD3644BBDC3F70ADAB402D13913A80255B5E14033B4ACD4355694704EB88E61D`.
No reader mathematics, source claim, bibliography entry, or source note
changed after review.

## Current disposition

`N-c-012.d` acquisition, reader reconstruction, and three-seat topic-level
manuscript review are accepted on the exact round-six snapshot. `N-c-012`
overall, Alpern--Schneider and the later Part IX presentations, Part IX
admission, the other
thirteen parts, the one final post-freeze publication build, rendered
inspection, human review, final-book completion, and user acceptance remain
separate and open. No tests, test harnesses, automated checkers, repository
scripts, TeX, handbook-PDF inspection, or builds were run for this review.
