# Section-local review shards

Section-local shards preserve provisional construction evidence without changing
the terminal handbook-unit reverse ledger while the handbook tree is still
moving. The governing schema is
`spec/provenance/section-review-shard.schema.json`; the fail-closed merger is
`tools/merge_section_review_shards.py`.

The state order is exact:

`queued` → `source restored` → `external content integrated` →
`provenance mapped` → `topics AI-approved` → `section AI-approved` →
`build-approved` → `visual-approved` → `internally locked`.

The source-fidelity, topic-specialist, and adversarial-publication reviews are
separate at topic and section scope. A passing AI evidence record identifies
the model and version, retains the exact instructions, pins every consulted
authority path and locator, records findings, and states that no other review
output was consulted. No vote or aggregate score is accepted. A state advances
only when every gate required for that state passes; a later file-hash change
makes the shard stale rather than silently reopening or promoting it.

The phrase “section-local review shard” is an administrative description, not
a new content term. It is needed because the terminal semantic ledger must stay
unpopulated while construction changes; it means exactly one schema-valid JSON
document for one section; it stands only for review administration; it differs
from source-unit, handbook-unit, packet, and register records by pinning the
section’s local files and state; and the merger and final freeze workflow
consume it to decide whether a section may be internally locked.

The merger rejects unknown handbook-unit IDs, duplicate sections, stale hashes,
skipped construction gates, non-isolated AI evidence, unresolved dependencies,
and non-deterministic ordering. It does not by itself establish packet,
register, source-unit, build, or visual truth; terminal readiness must validate
those owning records independently.
