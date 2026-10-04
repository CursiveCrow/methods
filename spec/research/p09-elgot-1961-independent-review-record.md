# Elgot 1961 independent manuscript review record

## Admission scope

This record closes source acquisition, reader-facing reconstruction, and the
three independent manuscript-content review gates for exactly `N-c-014.b`:
Calvin C. Elgot's 1961 journal article, its complete June 1959 University of
Michigan report precursor UMR1342, and the controlling 1962 published errata.
The reviewed reader scope is the Elgot presentation in
`handbook/parts/p09/presentations/n-c-014.tex`, together with the shared Part IX
finite-word theorem, bibliography records, complete source note, and compact
source-presentation record.

Admission is explicitly at **article-plus-published-errata strength**, with the
report used as a separately identified complete precursor.  It does not admit
`N-c-014.a` at literal 1960-journal strength, `N-c-014.c`, `N-c-014` as a
whole, Part IX, another handbook part, a generated handbook, rendered-page
inspection, human review, final-book completion, or user acceptance.

Acceptance does not certify every printed article sentence as correct.  The
accepted presentation preserves the false singular-relation claim in printed
Section 8.6.2 as a defect, applies the published finite-union and tagged-field
repair, and labels the remaining unary-window completion as handbook-owned.
Article, report, errata, source paraphrase, handbook proof, and modern
comparison remain distinct.

## Exact accepted snapshot

All three Round 2 reviewers accepted the following unchanged eight-object
snapshot:

| Artifact | SHA-256 |
|---|---|
| `tmp/pdfs/p09-elgot-1961/elgot-1961-trans-ams.pdf` | `DE2F9587F72075C94C7071A00002D1129AA8148C498F9A4D6F75968EB46ACD74` |
| `tmp/pdfs/p09-elgot-1961/elgot-1959-umr1342.pdf` | `596A599A7DF12F122BB2D875255B050695EC84A5A22F3488844D5876F3211D74` |
| `tmp/pdfs/p09-elgot-1961/elgot-1962-errata.pdf` | `B13E422FC03DDA61B93A1B782F40882AE90DBC8886945B26A42376A96ED34EC1` |
| `handbook/parts/p09/presentations/n-c-014.tex` | `33A2CD747DBDFA356F5505E88CBF798D426C5B5971003E0449805BCDF93F86FA` |
| `handbook/parts/p09/logic-in-computer-science.tex` | `1690DED84FC257B50BC5B44E094E382D8A79B176E7BB9C21D0845DAEC59629B8` |
| `handbook/bib/handbook.bib` | `6F98B6EB38B2B935DACC0C7E8373E1B12A5BB70FCAAC172D11BAFCDACA8C502F` |
| `spec/research/p09-elgot-1961-source-note.md` | `1A34AC4E992C00A0E917256CF5DB58A7C48A971FBF47F7F217B25D0DDAF18331` |
| `spec/research/p09-source-presentations-lot2-3.md` | `34D4B1AC65B78EAD14AB60335C94C8FFEA2F00778B963956038485DFB50EC438` |

Each reviewer independently recomputed all eight identities before judgment.
The chair kept the three reports sealed until all had been filed, then read
them together.  The source note and compact record may receive administrative
closure links after this decision; such status-only edits do not replace or
alter the accepted mathematical snapshot.

## Primary authorities, version order, and rights

The controlling publication is Calvin C. Elgot, “Decision Problems of Finite
Automata Design and Related Arithmetics,” *Transactions of the American
Mathematical Society* 98(1) (1961), 21--51, DOI
`10.1090/S0002-9947-1961-0139530-9`.  The complete thirty-one-page official AMS
facsimile is the first frozen object above.

The complete precursor is Calvin C. Elgot, *Decision Problems of Finite
Automata Design and Related Arithmetics*, University of Michigan report
UMR1342, June 1959, permanent repository record
<https://hdl.handle.net/2027.42/4758>.  Its sixty physical pages contain the
complete report and surrounding institutional matter.  Report agreement is
version evidence, not permission to overwrite the journal silently.

The controlling corrections are Calvin C. Elgot, “Errata to ‘Decision
Problems of Finite Automata Design and Related Arithmetics,’” *Transactions of
the American Mathematical Society* 104(3) (1962), 558--559, DOI
`10.1090/S0002-9947-62-99982-8`.  The errata, rather than the precursor, owns
the published corrections to the article.

The reviewers' Round 1 passes visually covered all thirty-one article pages,
all sixty report pages, and both errata pages.  Round 2 required renewed
original-detail inspection of journal p. 46, report pp. 4 and 41, and errata
pp. 558--559; the mathematical reviewer also reinspected journal p. 45 as the
immediate dependency.  OCR extractions were searchable aids only and did not
control a formula or symbol.

Public archival access is not treated as a redistribution licence.  The local
source files are research copies.  The handbook supplies independent
scholarly prose and does not claim a right to republish the source PDFs or
protected expression.

## Reviewer transcripts and independence

| Seat | Canonical reviewer | Final transcript | Transcript SHA-256 | Verdict |
|---|---|---|---|---|
| source fidelity and evidence | `/root/buchi_r1_source_fidelity` | `spec/research/boards/p09-elgot-1961/transcript/r2-source-fidelity.md` | `1EA196ACA218A1AAD1FD7450472407F521B76B7E7219A490E0FA9DBED6C6DF61` | **ACCEPT** |
| mathematical and proof correctness | `/root/buchi_r1_mathematical_proof` | `spec/research/boards/p09-elgot-1961/transcript/r2-mathematical-proof.md` | `D815A9FF2F702E821A32C6749C98BC8AA4C864A7DB2CE39FAD1F6FF4A7145C84` | **ACCEPT** |
| adversarial publication and terminology | `/root/buchi_r1_adversarial_publication` | `spec/research/boards/p09-elgot-1961/transcript/r2-adversarial-publication.md` | `9690395816271A5A7FF15B2E385FFA8642ADEEEF04CD81232D9E0CEF0219B0D5` | **ACCEPT** |

The same three canonical seats were reseated after Round 1.  A reviewer could
rely on that reviewer's own complete first-round source pass but could not read
another seat's report or verdict, the ledger, the chair transcript, or another
board.  Reviewers did not contact one another and edited only their assigned
transcripts.  Every reviewer checked the revised text and its immediate source
dependencies on the same unchanged snapshot.

This was manuscript scholarship, not software engineering.  No reviewer or
chair operation used a test, test harness, automated checker, repository
script, TeX command, interim handbook build, handbook-PDF inspection, or
build.  The evidence was direct source and manuscript reading, source-page
visual inspection, mathematical derivation, citation and provenance
inspection, and SHA-256 identity labels.  These reviews establish no
compilation or rendered-handbook result.

## Two-round revision history

Round 1 returned two `ACCEPT` verdicts and one `REJECT` verdict.  Supported
findings were not outvoted.  The mathematical seat identified three must-fix
defects:

- `MP-01`: the reader hid Section 8.6's literal syntactic restrictions behind
  the undefined adjective “local”;
- `MP-02`: the reader wrote only a binary tagged relation, without treating
  general arity or the possible unary case; and
- `MP-03`: the report comparison said one already-correct projection
  occurrence although report p. 4 contains two.

The revised reader states the exact quantifier-free syntax, permitted numerals,
forbidden equality and order, successor-offset terms, and corrected window
length.  It defines the tag construction componentwise for every arity at
least two.  For the unary case it explicitly replaces each unary relation
\(R_j\) by \(R_j\times R_j\), retains the one-letter prefix condition, proves
equivalence of admitted infinite sequences, and then applies the binary tag
construction.  This edge-case completion is attributed to the handbook, not
to Elgot's errata.  The report comparison now records both occurrences of
\(\widehat p\).

Round 2 returned three independent `ACCEPT` verdicts on the unchanged snapshot
above.  No verdict on a rejected snapshot was carried forward, and no blocker,
must-fix, should-fix, unread required page, identity mismatch, terminology
defect, or collateral source defect remained.

## Mathematical and source determinations

Elgot's Section 2 acceptor, the finite-set interpretation of \(L_1^1\), the
characteristic-column encoding, right truncation, Theorem 5.3's two effective
directions, its arithmetic consequences, the later \(A/B\)-transducer, strong
extendability, causal infinite behavior, realizability criterion, specification
encoding, and Chapter IV undecidability boundary were independently checked at
their stated source strength during Round 1.

The printed third sentence of Section 8.6.2 is false: a finite union of local
infinite-sequence languages need not be one such relation language.  The 1962
errata replaces it by \(S_1\cup\cdots\cup S_k\), with \(k\) not necessarily
one, and uses disjoint tags so that the projection of one tagged relation
language is exactly that union.

For arity \(n\geq2\), consecutive length-\(n\) tagged windows overlap, so their
component tags agree and hence are constant along an admitted infinite
sequence.  Every component sequence has a constant-tag lift, giving both
inclusions in the projection equality.  For \(n=1\), an infinite sequence has
every letter in \(R_j\) exactly when every adjacent pair belongs to
\(R_j\times R_j\).  Retaining the original one-letter prefix condition
therefore preserves the component language before tagging.  The same overlap
argument then applies, including empty-relation and ineffective-prefix cases.

The correction remains effective and retains a regular finite-prefix
language.  Thus the repaired Section 8.6.2 route can soundly invoke Theorem
8.1.  Nothing in this result turns Elgot's finite-transducer specification
calculus into a B\"uchi infinite-word acceptance theorem.

The report already prints \(\widehat p\) at both locations corresponding to
the journal's two corrected \(\widehat f\) occurrences.  It still shares the
reversed ordered-pair display and the false Section 8.6.2 singular-relation
sentence.  Those agreements and differences are reported only as precursor
evidence; the published errata owns the journal correction.

## Admission disposition

The exact Round 2 snapshot is admitted for source acquisition, reader-facing
reconstruction, and topic-level independent manuscript review of `N-c-014.b`
at the controlling 1961-article-plus-1962-errata strength, with the complete
1959 report kept as a separate precursor.

`N-c-014.a` still lacks literal 1960-journal reconciliation.  `N-c-014.c`,
`N-c-014` overall, Part IX admission, later Part IX work, the other thirteen
parts, the single final publication build after all fourteen parts are
text-frozen, rendered inspection, human review, final-book completion, and
user acceptance remain separate and open.  No test, test harness, automated
checker, repository script, TeX command, handbook-PDF inspection, or build was
run for this admission.
