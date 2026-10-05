# w02b-p02-036 (P2, unit accounting): A-035, L-004, L-005, R-013

Packet: work/waves/w02b/packets/w02b-p02-036.json. Editable host: handbook/registry/calculi/nd-cpl.tex only. No owned body/annex files; label_tag p02-w02b-p02-036 (no new labels were needed).

Held sources opened this session: spec/decisions/edition-2026-coverage-policy-resolution.md sections 3 (lines 60-76) and 8 (lines 152-177); spec/inventory/2026-09-06/complete-requirement-ledger.json (A-035 row, via the packet's source_presentations extract).

## R-013 (sheet vs derivation definition)

Gap (r2 confirm assessment): the sheet required a fresh application label and total discharge of all open occurrences of the bracketed formula; the definition (restoration/inherited-02193-02340.tex 14-27) discharges exactly the open occurrences of the bracketed formula marked with the carried label (possibly a proper subset), requires every carried label to discharge at least one occurrence, and requires freshness only for graft copies (8-12) and merging relabeling (21-27).

Change: nd-cpl.tex preamble and the side conditions of or-E, imp-I, neg-I and RAA now state the definition's discipline: carried label need not be fresh; exactly the open occurrences of the bracketed formula marked with that label are discharged; at least one; unmarked open occurrences stay open, so in the contexted reading the instance requires that formula to be in the conclusion context whenever one is left; total discharge is obtained by first applying convention (ii) (merging relabeling with a fresh label). Freshness is stated as required only in conventions (i) and (ii). The completeness opening (inherited-02665-02809.tex 14-28: bot-E when no open occurrence of the negated goal remains, otherwise merging relabeling then RAA) and lem:prop-mcs clause 5 (inherited-02545-02664.tex 60-70: and-I then and-E2, then imp-I discharging the single occurrence marked i) are licensed under the revised sheet word for word. Scratch render of \showcalculus{nd-cpl} with handbook.sty: no overfull box, no error.

## A-035-C03 (Herbrand row)

The table host handbook/parts/p02/first-order-depth.tex is read-only for this packet. Patch request filed in work/waves/w02b/patches/w02b-p02-036.json (replace of the Herbrand row's last cell, lines 461-463). Choice analysis read in the book: existential-validity proof (annex/p02/herbrand-methods-unification-and-first-order-w02-p02-028.tex 94-141) restricts to finite L_sigma, Herbrand model lemma (58-91) uses thm:prop-compactness(2) (inherited-02665-02809.tex 44-66), proved from completeness (4-35) and Lindenbaum (inherited-02545-02664.tex 72-96) along an enumeration of countable Fm_CPL: no choice. The general-validity extension uses AC right to left via thm:skolem-equisatisfiable(1) (inherited-05132-05567.tex 316-330); standing convention item 4 (parts/p02/herbrand-...-w02-p02-028.tex 42-44) agrees.

## L-004 / L-005

Remaining items per the r2 first assessments are lead-owned (handbook.sty Rule/side macros, hash-checked restoration capture inherited-02193-02340.tex 48-56 overfull 8.69pt, final consolidated publication inspection). One concrete editorial item filed as a patch request: the cr-terminated array in natural-deduction-and-classical-sequent-calculi-w02b-p02-009.tex 631-651 (another packet's file) changed to double-backslash rows.

## Continuation

- R-013-C02/C04: sheet aligned (nd-cpl.tex lines 10-15 comment, 16 preamble, 23, 24, 26, 29). Next reader check: confirm match against inherited-02193-02340.tex 1-30.
- A-035-C03: awaiting lead application of patch request 1 in work/waves/w02b/patches/w02b-p02-036.json.
- L-004/L-005: lead-owned remainder; patch request 2 covers the p02-009 array.
- unit-compile cannot run for this packet (no owned body/annex .tex): it reports "packet lacks owned body and annex .tex files to compile".
