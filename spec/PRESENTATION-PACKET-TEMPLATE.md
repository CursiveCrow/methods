# Presentation packet template

This is an administrative skeleton for one separately attributed presentation.
It contains no logical content and supplies no house-selected terminology. Replace
every angle-bracketed field from the identified authority before verification.

An `open` packet keeps every uncollected content array empty and records the
source-bound work still owed. Its presentation identity may remain `unresolved`;
do not turn a taxonomy heading into a name or description. A packet may be
recorded as `verified` only after each content array contains either the
complete sourced material or an explicit `not_applicable` record justified at
an exact source locator, at least one substantive item is actually present,
every completeness and verification dimension is `pass`, all required
independent evidence artifacts are hash-verified, and `owed_artifacts` is empty.

The administrative field `obligation_links` uses an exact per-obligation
assignment because a bare manifest-ID list cannot distinguish sourced
fulfilment from work merely asserted to be covered. An assignment is the
metalinguistic record consisting exactly of one manifest ID, one exact source
locator, one status, and either present content-item IDs when `fulfilled` or
owed-artifact IDs when `open`. It differs from a content item because it does
not contain logic, and from an owed artifact because it binds that content or
work to one existing manifest obligation. The checker uses the record to
reject unknown IDs, dangling references, attribution-only fulfilment, and any
`verified` packet whose assignments remain open.

Passing `tools/check_presentation_packet.py` establishes only packet shape,
manifest-assignment/reference integrity, and the byte integrity of referenced
local artifacts.
It does **not** establish that a locator is semantically correct, that a
reconstruction is complete or accurate, that non-applicability is justified,
or that recorded AI-review findings are correct. Those are separately scoped
AI-review judgments recorded in independently produced evidence; the checker cannot
confer them.

```json
{
  "schema_version": 2,
  "packet_id": "open.<source-slug>.<presentation-slug>",
  "overall_status": "open",
  "authority": {
    "work": "<identified authoritative work>",
    "edition": "<identified edition or official version>",
    "exact_locator": "<pages, sections, theorem or rule numbers, or versioned locator>",
    "local_path": "<local source path; replace with url when the authority is remote>"
  },
  "presentation_identity": {
    "identity_status": "unresolved",
    "house_selected": false,
    "synthesized": false,
    "hybrid": false
  },
  "reconstruction_mode": "open_missing",
  "content": {
    "notation_roles": [],
    "conventions": [],
    "syntax": [],
    "definitions": [],
    "axioms": [],
    "calculi": [],
    "rules": [],
    "side_conditions": [],
    "semantic_clauses": [],
    "statements": [],
    "hypotheses": [],
    "results": [],
    "proofs": [],
    "proof_boundaries": [],
    "examples": [],
    "counterexamples": [],
    "exercises": [],
    "exercise_solutions": [],
    "exercise_feedback": [],
    "warnings": [],
    "qualifications": [],
    "tables": [],
    "source_attributions": []
  },
  "technical_names": [],
  "variants": [],
  "obligation_links": {
    "coverage_assignments": [
      {
        "obligation_id": "<existing stable_id from spec/full-compendium-coverage-manifest.csv>",
        "assignment_status": "open",
        "source_locator": "<exact authority locator showing why this obligation belongs to this presentation>",
        "present_content_item_ids": [],
        "owed_artifact_ids": [
          "owed.content"
        ]
      }
    ],
    "register_assignments": []
  },
  "destination": {
    "file": "<required handbook destination file>",
    "stable_labels": [
      "<required stable destination label>"
    ]
  },
  "completeness": {
    "notation": "pending",
    "conventions": "pending",
    "syntax": "pending",
    "definitions": "pending",
    "axioms": "pending",
    "calculi": "pending",
    "rules": "pending",
    "side_conditions": "pending",
    "semantic_clauses": "pending",
    "hypotheses": "pending",
    "statements": "pending",
    "results": "pending",
    "proofs": "pending",
    "proof_boundaries": "pending",
    "examples": "pending",
    "counterexamples": "pending",
    "exercises": "pending",
    "exercise_solutions": "pending",
    "exercise_feedback": "pending",
    "warnings": "pending",
    "qualifications": "pending",
    "tables": "pending",
    "attribution": "pending"
  },
  "verification": {
    "source_fidelity_ai": "pending",
    "topic_specialist_ai": "pending",
    "adversarial_publication_ai": "pending",
    "static": "pending",
    "build": "pending",
    "visual": "pending"
  },
  "verification_evidence": [],
  "owed_artifacts": [
    {
      "artifact_id": "owed.identity",
      "artifact_kind": "presentation_identity",
      "description": "Establish the presentation identity from the identified authority without naming a hypothetical answer.",
      "source_obligation": "Record the source-given name, or an exact eliminable description only when the source supplies no name.",
      "completion_condition": "Set identity_status to identified only after the source-given name or exact source-bound description is recorded."
    },
    {
      "artifact_id": "owed.content",
      "artifact_kind": "content",
      "description": "Gather and reconstruct the identified presentation in full from the authority above.",
      "source_obligation": "Account for every applicable content category and every material source qualification at the exact locator.",
      "completion_condition": "Replace empty arrays with sourced records or source-justified not_applicable records, then independently verify every dimension."
    }
  ]
}
```

When an obligation is fulfilled, its assignment must instead name at least one
`present` content item outside `source_attributions`, name no owed artifact,
and use `"assignment_status": "fulfilled"`. Attribution is retained in full,
but attribution alone is not the logical content whose acquisition an
obligation records.

For a present content item, use exactly one of `text` or `artifact_path`:

```json
{
  "item_id": "<stable source-specific item id>",
  "status": "present",
  "source_locator": "<exact locator within the packet authority>",
  "artifact_path": "<path to the complete maintained transcription or reconstruction>",
  "content_digest": "<lowercase SHA-256 of the artifact bytes>"
}
```

A verified packet also needs one separately produced, hash-checked evidence
record for each verification dimension. This record links evidence; it does not
make the packet checker a reviewer. Each AI-review record additionally pins the
model and version, instructions, exact scope, consulted authority files and
locators, findings, and the digest of its evidence artifact.

```json
{
  "kind": "source_fidelity_ai",
  "artifact_path": "<path to independently produced source-comparison record>",
  "sha256": "<lowercase SHA-256 of that artifact's bytes>",
  "verifier_identity": "<identified AI review process>",
  "verification_scope": "<exact packet, authority locator, content categories, and checks covered>",
  "independently_produced": true,
  "model": "<model family>",
  "model_version": "<exact model version>",
  "instructions": "<exact review instructions>",
  "consulted_authority_files": [
    {
      "path": "<repository-relative authority snapshot>",
      "sha256": "<lowercase SHA-256 of that authority file>"
    }
  ],
  "consulted_authority_locators": [
    "<exact locator consulted>"
  ],
  "findings": [
    "<exact finding>"
  ],
  "evidence_digest": "<same lowercase SHA-256 as sha256 above>"
}
```

The `static`, `build`, and `visual` evidence objects use only the six common
fields from `kind` through `independently_produced`; they do not assert a model,
AI instructions, authority consultation, or AI findings.

Use `not_applicable` only when the source itself supports the absence:

```json
{
  "item_id": "<stable source-specific item id>",
  "status": "not_applicable",
  "source_locator": "<exact locator supporting non-applicability>",
  "source_justification": "<source-grounded reason this category does not apply>"
}
```

If a new technical name is actually required, its record must supply all six
fields below at the same location. Otherwise leave `technical_names` empty and
describe the missing source-bound artifact in `owed_artifacts`.

```json
{
  "name": "<new technical name>",
  "necessity": "<why existing terms cannot state the distinction unambiguously>",
  "definition_or_axiom": "<exact eliminable definition or explicit introducing axiom>",
  "standing": "<what kind of object, relation, statement family, or abbreviation it names>",
  "nonredundancy": "<exact difference from every existing defined term>",
  "use": "<later definition or theorem that requires the distinction>"
}
```

Validate an instantiated packet with:

```text
python tools/check_presentation_packet.py path/to/packet.json
```
