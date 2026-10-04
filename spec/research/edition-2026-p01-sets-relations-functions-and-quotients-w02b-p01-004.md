# P1 2.1: separation instances for relative complement and intersection (w02b-p01-004)

## Provenance

- Packet: work/waves/w02b/packets/w02b-p01-004.json; section 2.1; duty MP-0 (X-1). Components FLRV1-U00009..U00013 are closed in the packet (open=false) and carry no duty here.
- Gap closed: two "same argument" deferrals in handbook/annex/p01/sets-relations-functions-and-quotients-w02-p01-005.tex: membership clause 3 (lines 74-76) and the G_cap step of the subset-algebra proof (lines 296-297).
- Held source opened this session: source/formal-logic-reference.tex lines 365-372 (chapter "Sets, Relations, Functions, and Cardinality"), 405-440 (sec. "Ordered pairs and products": definition "Ordered pair", lemma "Ordered-pair identity", definition "Cartesian product"), 444 (sec. "Relations and functions"), 466-476 (definition "Function"), 10063-10170 (chapter "The Axioms of ZF and ZFC": language, classes, extensionality, empty set, pairing/union/power set, infinity, separation schema). Every locator in the body is one of these.
- Bib: existing key FrozenFormalLogicSetOperations (handbook.bib 13107). No new keys; no bib intake file.

## Mathematical design

- Named L_in formulas theta_pair, theta_op, theta_cap, gamma_cap (def:p01-w02b-p01-004-formulas); lemma that each defines its intended set (pairing/membership(2) + extensionality).
- Relative complement: one explicit application of thm:p01-w02-p01-005-separated-set to neg x in B (parameter B, formed variable d distinct from x, B).
- Graph G^Q_cap = {w in (QxQ)xQ : gamma_cap(w,Q)} for arbitrary Q: membership condition (carries X cap Y in Q), single-valuedness via ordered-pair identity twice, totality iff Q closed under cap. Corollary for Q = P(S) with closure X cap Y subseteq S, and identification with G_cap of the 005 subset-algebra proof by extensionality.
- Example: P({emptyset}) = {e0, e1}, four triples, complements. Failure: Q = {e1, e2}, e1 cap e2 = emptyset not in Q, no value at <e1,e2>.

## Existing treatment found

- Listed: restoration/inherited-00373-00405.tex (sec:set-prerequisites-01), w02-p01-005 body and annex. Extended, not duplicated; patch requests replace the two deferrals with pointers.
- Not listed but relevant: sec:set-prerequisites-02 (restoration/inherited-00406-00443.tex: ordered pair, ordered-pair identity, product) and sec:set-prerequisites-03 (restoration/inherited-00444-00506.tex: relation, function). Used, unchanged.
- Adjacent observation (not in the MP-0 duty text): in the same 005 subset-algebra proof the complement graph G_c is formed from the condition exists X (X in Q and w = <X, S minus X>) without writing it as an L_in formula; and the G_cup step unfolds pairs only by reference to the product-bound proof. Lead may route these if the same standard is applied there.

## Continuation

- Written: body handbook/parts/p01/sets-relations-functions-and-quotients-w02b-p01-004.tex (266 lines); annex handbook/annex/p01/sets-relations-functions-and-quotients-w02b-p01-004.tex (229 lines); symbol intake handbook/registry/symbols-intake-p01-sets-relations-functions-and-quotients-w02b-p01-004.csv (5 rows).
- Patch requests: work/waves/w02b/patches/w02b-p01-004.json (2 replace ops on the 005 annex; anchors verified unique). Not applied (read-only host).
- Driver inputs needed (lead): p01.tex after parts/p01/sets-relations-functions-and-quotients-w02-p01-005 (line 10); annex/p01-route.tex after annex/p01/sets-relations-functions-and-quotients-w02-p01-005 (line 6). The packet proposed the body before the 005 file (after line 9); placement after it is proposed because every result here cites 005.
- Self-checks: find_fused_spaces no hits; unit-compile ok (4 overfull boxes: two annex headers from long labels, 1.5pt and 5.1pt; two in the shared bib entry); check.py --tree handbook shows no finding on these files.
