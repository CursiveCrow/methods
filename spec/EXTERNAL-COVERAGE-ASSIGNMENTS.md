# External-coverage assignment sidecars

The exact sidecar header is:

```text
coverage_id,packet_id,source_locator,present_content_item_ids
```

Each file is UTF-8, LF-only CSV. `present_content_item_ids` is a compact JSON
array whose strings are nonempty, unique, and lexically sorted. Sidecars are
listed in `spec/external-coverage-assignment-index.json` in lexically sorted
path order. Concatenating their data rows must reproduce coverage-manifest
order. This lets the checker compare all 9,162,150 baseline rows while keeping
only one manifest row and one sidecar row in the streaming comparison. Exact
global coverage-ID uniqueness is proved with a disposable disk-backed SQLite
index whose RAM cache is explicitly bounded; this catches nonadjacent duplicate
IDs without allocating the ID set in memory. Memory for the compatibility join
scales with admitted packet records and the assignments those packet files
repeat; it does not scale with sidecar-only assignments.

The sidecar is the sole fulfillment source of truth. Every assignment names
exactly one independently admitted packet and one or more of that packet's
admitted present content items. Every coverage assignment repeated inside an
admitted packet must occur identically in the sidecar stream. A packet may
repeat only a strict subset of its sidecar assignments; packet-local data
cannot create fulfillment absent from the sidecar.

## Why this administrative record exists

- **Necessity:** packet-local arrays cannot prove unique, exhaustive assignment
  of a multi-million-row manifest without duplicating the entire assignment
  corpus into packet files.
- **Definition:** an external-coverage assignment sidecar is one indexed,
  immutable CSV shard whose ordered rows bind exact coverage IDs to exact
  admitted packets, source locators, and admitted present content-item IDs.
- **Standing:** it is a metalinguistic administrative record, not a logical
  term, source presentation, or handbook claim.
- **Nonredundancy:** packet admission proves that maintained packet content may
  be used; the sidecar separately proves which exact external baseline IDs that
  content fulfills, exactly once and in manifest order.
- **Use:** terminal readiness requires the streaming checker with
  `--require-complete`, which rejects every missing, duplicate, unknown, stale,
  conflicting, or packet-only assignment.
