# Büchi 1962 independent manuscript review record

## Admission scope

This record closes source acquisition, reader-facing reconstruction, and the
three independent manuscript-content review gates for exactly N-c-013.a,
J. Richard Büchi's 1962 presentation “On a Decision Method in Restricted
Second Order Arithmetic.” Its principal reader scope is
handbook/parts/p09/presentations/n-c-013.tex, lines 375--760. The shared Part IX
decision theorem, bibliography record, complete source/acquisition note, and
compact controlling presentation were reviewed with it.

Admission is topic-only. It does not admit N-c-013.b through N-c-013.e,
N-c-013 as a whole, Part IX, another handbook part, the final generated
handbook, rendered-page inspection, human review, final-book completion, or
user acceptance.

## Exact accepted snapshot

All three blind reviewers accepted the following unchanged six-object
snapshot:

| Artifact | SHA-256 |
|---|---|
| tmp/pdfs/p09-buchi-1962/logic-methodology-philosophy-science-pageplace-preview-includes-buchi-pp1-11.pdf | D37929230CD874D9B6E91CDDE50DD57EAF51D625BC7575878853E4018B64E089 |
| handbook/parts/p09/presentations/n-c-013.tex | F674BDB103A3B07DEE5925A1D7F3880D92DA31C6442196FB075B2FA85F4ADD24 |
| handbook/parts/p09/logic-in-computer-science.tex | 2778CAA3D0EB741A78B9D2EA44BD157E5FCCB4E2F3034ED539D52A9788287A1B |
| handbook/bib/handbook.bib | 748B159ED5CE40855878D3E8492DA98D0A465B73C68830E5BE11165EFF2ACA6A |
| spec/research/p09-buchi-1962-source-acquisition.md | 90C23E094604342726B02EC78FE1A4211D56233A063532E8EDA94537676C434B |
| spec/research/p09-source-presentations-lot2-3.md | EBC0E39AF016B22F1BA52D7DEEB620DE6B00F5B48AA1F3E0687BB10BBC316508 |

After all reports had been filed and read, the chair independently recomputed
all six identities. Every value remained exact.

## Primary authority, versions, and rights

The controlling primary text is:

- J. Richard Büchi, “On a Decision Method in Restricted Second Order
  Arithmetic,” in Ernest Nagel, Patrick Suppes, and Alfred Tarski, eds.,
  Logic, Methodology and Philosophy of Science: Proceedings of the 1960
  International Congress, Stanford University Press, Stanford, California,
  1962, pp. 1--11.

The acquired public commercial preview is a later Stanford printing. Printed
pp. 1--11 occupy file pp. 12--22; file p. 23 begins Julia Robinson's next
article on printed p. 12. Every relevant front-matter page, all eleven article
pages, and the boundary page were visually inspected at original detail.

No DOI appears in the 1962 original. DOI
10.1016/S0049-237X(09)70564-6 identifies the 1966 North-Holland/Elsevier
republication, and DOI 10.1007/978-1-4613-8928-6_23 identifies the 1990
collected-works reprint. Neither later identifier was attached to the original
bibliography record. The preview supplies a research copy but declares no
open-content licence; no redistribution right is inferred.

## Reviewer transcripts and independence

| Seat | Canonical reviewer | Model | Transcript | Transcript SHA-256 | Verdict |
|---|---|---|---|---|---|
| source fidelity and evidence | /root/buchi_r1_source_fidelity | gpt-5.5, xhigh | spec/research/boards/p09-buchi-1962/transcript/r1-source-fidelity.md | 4A5122B7C3EDD31C28A75958CEED6D23AA7CD71CBF97AF90AFA86FF87E190043 | ACCEPT |
| mathematical and proof correctness | /root/buchi_r1_mathematical_proof | gpt-5.6-sol, xhigh | spec/research/boards/p09-buchi-1962/transcript/r1-mathematical-proof.md | 3DFF1977C13C2991EBD4FBC0CF2E427F47A89F9A943D4DDF6391CA7F49F303AF | ACCEPT |
| adversarial publication and terminology | /root/buchi_r1_adversarial_publication | gpt-5.6-terra, xhigh | spec/research/boards/p09-buchi-1962/transcript/r1-adversarial-publication.md | 1953769C4DEFF4716FD975B3588C5E31C785FFA6F8E633069807ED29FA549041 | ACCEPT |

Each reviewer was a fresh direct child of the chair with no inherited turn
history. Each was instructed to read the complete charter; not to read the
ledger, chair record, any earlier or concurrent transcript, or another
verdict; not to contact another reviewer; and not to edit a frozen artifact.
Each wrote only its assigned transcript. The chair kept every transcript
sealed until all three reviewers had completed, then read every line of all
three reports.

Every reviewer independently recomputed all six frozen identities and visually
read every required source image. All M01--M25 coverage points were discharged.

This was manuscript scholarship, not software engineering. No reviewer or
chair operation used a test, test harness, automated checker, repository
script, TeX command, handbook-PDF inspection, or build. The evidence was direct
source and manuscript reading, primary-page visual inspection, mathematical
proof, citation/provenance inspection, and SHA-256 identity labels. These
reviews establish no compilation or rendered-page result.

## Mathematical and source determinations

The accepted presentation preserves Büchi's own \(SC\) standing: individuals
range over \(\mathbb N\), monadic predicates over all subsets of
\(\mathbb N\), and the language has \(0\), successor, propositional
connectives, and quantifiers of both sorts. A predicate assignment is encoded
as an infinite truth-value word before any auxiliary accepting sequence is
introduced.

The literal \(\Sigma_n,\Pi_n\) hierarchy, infinitely-often quantifier,
\(\Sigma_1^\omega\) recurrent form, finite-interval \(\Sigma^0\) formulas,
two-sided finite-rank congruences, and multiperiodic finite-word languages were
checked against the printed pages. Multiperiodicity is not confused with
ultimately periodic predicate assignments.

The handbook-owned finite-data comparison was independently proved in both
directions. For one \(\Sigma_1^\omega\)-formula, the eliminable objects
\(\Gamma,Q,Q_0,\Delta,F\) give exactly a permitted-initial-set
nondeterministic Büchi acceptor. Conversely, finite automaton states can be
encoded by predicate bits, with propositional matrices excluding unused codes
and enforcing initial, transition, and recurrence clauses. The article does
not print this modern tuple, use modern run terminology, or name Büchi
acceptance.

The Sequential Lemma and its Ramsey proof, Lemmas 2--6 and their cited proof
dependencies, the Lemmas 7--9 Boolean and complement constructions, the
\(2^{2m^2}\) congruence-rank bound, and Lemma 10's nonempty repeated-block
reading were all independently checked. No later determinization theorem was
imported.

Theorem 1's recurrent normal form, the \(\Sigma_1^\omega/\Sigma_2\)
definability collapse, the free-individual extension, and the finite-set
consequence remain at the source's exact proof strength. Lemma 12 was
rederived as the existence of an initial finite path to a recurrent state plus
a nonempty return cycle, with the common \(2^k\) edge bound and all empty and
one-state cases checked. The remaining effectivity argument supports Theorem
2's decidability conclusion but no modern complexity bound.

The five post-Theorem-2 comparisons, proposed axiom schema, ultimately
periodic assignment restriction, finite-semigroup outline for Theorem 3,
Theorem 4, the printed \(\mathrm{Nn}\) discrepancy, the Robinson- and
Gödel-attributed reports, and all three open problems were checked against
printed pp. 9--10. Verification of a supplied finite-state behavior remains
distinct from the open synthesis question.

## Finding disposition

The source-fidelity seat filed one non-blocking consider item, F-SF-01. Printed
p. 1 uses the word “fraction,” while the complete source note gives the
unquoted modern paraphrase “fragment” when describing \(SC\)'s relation to
restricted second-order arithmetic.

The observation is preserved here rather than erased or outvoted. It does not
require a snapshot repair: “fragment” is an accurate unquoted mathematical
paraphrase; the note does not present it as a quotation; the domains,
vocabulary, and formal standing are exact; the reader-facing section does not
use either word; and the reviewer itself classified the item as consider,
explicitly nonblocking. The finding is therefore closed as documented with no
content change.

No reviewer filed a blocker, must-fix, should-fix, uncertainty, unread page, or
identity mismatch. No majority vote was used to suppress a finding, and no
verdict from another snapshot was carried forward.

## Admission disposition

The exact six-object snapshot is admitted for source acquisition,
reader-facing reconstruction, and topic-level independent manuscript review of
N-c-013.a only. The admission preserves the historical formalism, exact
formula hierarchy, source-versus-handbook ownership, cited proof dependencies,
finite-congruence method, decidability strength, version and rights limits,
historical comparisons, printed discrepancy, and open-problem boundaries.

N-c-013.b through N-c-013.e, N-c-013 overall, later Part IX presentations,
Part IX admission, the other thirteen parts, the single final publication
build after all fourteen parts are text-frozen, rendered inspection, human
review, final-book completion, and user acceptance remain separate and open.
No test, test harness, automated checker, repository script, TeX command,
handbook-PDF inspection, or build was run for this admission.
