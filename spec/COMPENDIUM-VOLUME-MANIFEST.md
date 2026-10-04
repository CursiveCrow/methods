# Single-publication handbook manifest

The machine-readable authority is `spec/compendium-volume-manifest.json`.
Despite the historical filename, it no longer describes a volume set. It binds
exactly one possible public artifact:

- title: *The Methods of Reason*;
- path: `handbook/main.pdf`;
- format: PDF;
- current status: construction draft;
- current release status: not release-ready.

No companion book, inherited volume, external-presentation volume, integrated
layout edition, facsimile, or volume set is part of the publication. The final
book has no page-count ceiling and no compression target.

## Internal authority evidence

`spec/inherited-corpus-manifest.json` continues to hash-lock the frozen source
and PDF. Those files are immutable internal authority evidence. They are not a
public volume, are not bundled with the final book, and cannot become a second
publication artifact by changing a manifest flag. Historical audits that once
described a staged or multi-volume publication remain historical evidence; this
current governing manifest does not rewrite their observations or imply that
they were final.

## Draft and release states

While construction is underway, `publication_status` is
`construction-draft`, `release_ready` is false, and `final_release_evidence` is
null. The checker still requires the draft's byte count, page count, digest, and
PDF metadata title to match the manifest exactly. A source or PDF rebuild must
therefore repin the observation rather than silently leaving a stale record.

The manifest may change to `publication_status: release` only when all of the
following are true together:

1. `release_ready` is true;
2. the public artifact remains exactly `handbook/main.pdf` titled *The Methods
   of Reason*;
3. `final_release_evidence` names and hash-locks the all-zero-residual readiness
   record;
4. `final_release_evidence` names and hash-locks the user's final-acceptance
   record; and
5. the recorded public-PDF digest equals the digest checked by both records.

The publication-manifest checker verifies those file identities. It does not
manufacture readiness or user acceptance. The terminal readiness checker owns
the residual proof; only the user can supply final editorial acceptance.

## Administrative field labels

The labels `publication_status`, `internal_authority_evidence`, and
`final_release_evidence` are machine fields, not logical terminology used in
the handbook.

**Necessity.** A path and digest alone cannot distinguish a mutable
construction observation, immutable internal evidence, and the two records
required to authorize release without ambiguity.

**Definition.** `publication_status` is exactly `construction-draft` or
`release`; `internal_authority_evidence` is exactly the frozen-corpus manifest
path plus the false `published_with_book` flag; `final_release_evidence` is
null for a draft and otherwise is the exact five-field object containing the
readiness path/digest, user-acceptance path/digest, and public-PDF digest.

**Standing.** These are metalinguistic administrative JSON labels. They do not
name motives, logical relations, statement families, mathematical objects, or
content classifications.

**Nonredundancy.** The publication status states the permitted lifecycle
state; the authority-evidence object prevents the frozen corpus from being
misclassified as a public artifact; the release-evidence object binds two
independent terminal records to the exact PDF. None can be recovered from the
other two fields.

**Use.** `tools/check_compendium_volume_manifest.py` uses the three labels to
reject a second public artifact, reject publishing the inherited evidence,
verify the current draft, and fail closed on a release claim lacking readiness
or user-acceptance evidence.

## Machine check

From the repository root, run:

```text
python tools/check_compendium_volume_manifest.py
```

The checker requires:

- the exact schema and single-artifact shape;
- the exact title *The Methods of Reason* in the manifest and PDF metadata;
- the exact public path `handbook/main.pdf`;
- exactly fourteen transitive reader-facing `\part` surfaces in the pinned
  order, including a source-exact inherited part heading reached through its
  validated wrapper instead of a duplicate driver heading;
- current PDF bytes, pages, and SHA-256;
- the frozen source and PDF to match `spec/inherited-corpus-manifest.json`;
- `published_with_book` to remain false; and
- a terminal readiness and user-acceptance record before any release-ready
  state.

`--require-release-ready` fails while the artifact is a construction draft.
The deprecated `--require-expansions-ready` spelling is retained as the same
fail-closed alias so older automation cannot accidentally pass under weaker
multi-volume semantics.
