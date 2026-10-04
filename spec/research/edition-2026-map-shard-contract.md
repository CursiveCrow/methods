# Coverage-map construction contract

Authority: the user's 9 September 2026 direction to complete the coverage
map before further broad authoring. Existing chapter drafts and primary
captures remain preserved. New manuscript authoring is paused.

This is the finite edition-catalog projection authorized by CAT-01. It reuses
the original requirement ledgers, source-unit inventory, historical coverage
manifest, author/source notes and presentation-packet identities. It does not
replace historical records, manufacture admission evidence or rebind validators.

## Shared destinations and ownership

Root owns spec/edition-2026-coverage-map.json and its human-readable companion,
the shared unit conventions, reconciliation of overlapping mappings, the
new-reasoning/benchmark crosswalk and final complete-set accounting.

Workers write disjoint JSON/JSONL shards beneath
spec/coverage/edition-2026/ and one source/evidence note per assignment beneath
spec/research/. Large raw extraction evidence may remain in the established
tmp/edition-2026-catalog-*/ directories with explicit receipt links.
Do not overwrite the September inventory or the historical manifest.

## Content-unit records

Use JSONL, one object per identified intellectual treatment, with these fields:

- unit_id: stable and source-specific; use ED26-REQ-<original-id>-<local-number>
  for requirement-origin units, ED26-<source-id>-<local-number> for external
  source units, or ED26-<part>-<family>-<local-number> for new reasoning units.
- kind: definition_system, theorem_proof_group, algorithm_method,
  comparative_treatment, empirical_treatment, philosophical_argument,
  historical_treatment, or apparatus.
- title and reasoning_question: actual subject and purpose, not a raw filename.
- original_requirement_ids and inherited_source_ordinals: explicit arrays.
- source_presentations: actual source IDs/citation keys, title, version,
  precise extent, local artifacts/locators and evidence for the identification.
- required_components: explicit objects with component_id, description,
  success_condition, failure_condition and required_source_extent.
- prerequisites: identified unit IDs when available, otherwise exact named
  mathematical/content premises marked for root's identifier reconciliation.
- destination: body, annex and lookup fields, each with existing path/label or
  a precise proposed destination; do not create empty manuscript chapters.
- content_state: authored, partly_authored, missing, or mixed. This describes
  writing, not independent acceptance.
- source_state: identified_held, identified_missing, mixed, or identity_unresolved.
- scope_state: resolved or unresolved.
- evidence: current path/label/locator and dated reading or source records.
- remaining_work: concrete writing/source/mapping tasks.
- unresolved_questions: exact outstanding scope/identity questions, if any.

Keep materially different presentations separate. Multiple requirements can
point to one unit, and one requirement can point to several units. A common
topic title is not evidence that two source presentations are identical.

## Original-requirement and inherited-unit crosswalks

Preserve every original identity and wording in the crosswalk. Each row needs
its identity, unit_ids, exact required component mapping, present destinations,
remaining work, evidence and mapping_state (resolved or unresolved).
Missing writing is a valid mapped state when its obligation and destination
are specific; a generic heading or TODO is not a resolved component mapping.
The retired opening framing needs the explicit user-directed policy disposition,
without erasing the original identities or surviving substantive obligations.

## Historical-record reconciliation

Use exact IDs or verified consecutive ranges, retaining source/parent identity,
counts, original field/payload evidence and the applicable producer receipt.
Each range must give disposition, rationale, unit_ids where applicable,
evidence_paths and mapping_state.

Allowed dispositions are substantive_obligation, alias_or_repeated_capture,
non_content_metadata and unresolved_candidate. State the actual relation:
for example a source fragment belonging to a unit, or an artifact descriptor
which preserves acquisition evidence without becoming a new content unit.
Artifact role and raw-record role are separate: a PDF's font/byte descriptors
are not its theorem text. An OCR word, coordinate field or serialized response
does not become an independent intellectual treatment merely by being called
a topic in the old producer.

Classify complete producer families and exact membership, not title samples.
Do not classify a whole mixed source group as metadata. Preserve source text,
figures, variants, acquisition failures and uncertain candidates explicitly.
Substantive reference-list entries do not automatically create new whole-paper
transcription obligations; follow the edition's stated family/scope rule.

## Completion conditions

The construction map is incomplete until every one of the 615 original
requirements, all 1,055 inherited structural units, all 9,162,150 historical
records, the 26 initial new-reasoning assignments, mandatory cross-part
families and selected benchmark contents have accounted mappings.

Each actual required intellectual unit must have specific components,
prerequisites, source identity/extent, destination and success/failure cases.
Every duplicate or non-content classification needs evidence. Every unresolved
scope or identity candidate must be resolved before claiming map completion.
Missing manuscript content stays visible as missing work; it cannot be removed
to improve a completion count. Do not infer publication acceptance from this map.

No broad manuscript authoring, per-edit reviews, manuscript builds or renders
occur during this priority phase. Necessary source acquisition, source reading,
data extraction and complete-set mapping checks are part of the map task.
