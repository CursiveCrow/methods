from __future__ import annotations

import copy
import csv
import hashlib
import importlib.util
import io
import json
import tempfile
import unittest
from pathlib import Path

import jsonschema


MODULE_PATH = Path(__file__).with_name("build_register_obligation_closure.py")
SPEC = importlib.util.spec_from_file_location("build_register_obligation_closure", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
target = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(target)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


SUPERSESSION_IDS = (
    "OBL::defects::S-002",
    "OBL::defects::S-003",
    "OBL::apparatus::A-167",
    "OBL::apparatus::A-168",
)
SUPERSESSION_ID = "notation-contract-2026-08-11"
SUPERSESSION_EXCLUDED_ID = "OBL::apparatus::A-172"
SUPERSESSION_STATEMENT = (
    "Only the four listed demands to rewrite inherited notation are displaced by "
    "the 2026-08-11 fidelity contract; source tokens, renderings, scoped roles, "
    "original register rows, and every unlisted obligation remain unchanged."
)
CLAUSE_SPANS = (
    ("spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md", 3, 7),
    ("spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md", 30, 55),
    ("spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md", 68, 69),
    ("spec/FULL-COMPENDIUM-TRANSCRIPTION-CONTRACT.md", 119, 134),
    ("spec/FULL-COMPENDIUM-ARCHITECTURE.md", 49, 60),
    ("spec/FULL-COMPENDIUM-ARCHITECTURE.md", 210, 225),
    ("handbook/CONVENTIONS.md", 3, 8),
    ("handbook/CONVENTIONS.md", 198, 208),
)
CURRENT_LOCATORS = (
    ("OBL::defects::S-002", 3439, 3447, r"\abs{\Meta}"),
    ("OBL::defects::S-002", 3472, 3472, r"\abs{\Meta}"),
    ("OBL::defects::S-003", 3668, 3675, r"\equiv"),
)
REVISION_PAIRS = (
    (
        "OBL::defects::S-002",
        4317,
        4317,
        "72cdf3383cb543f3e7273b1fe3ba3569bffa7aae316bf57a48983623b623f2f2",
        5053,
        5053,
    ),
    (
        "OBL::defects::S-002",
        4386,
        4386,
        "eff749f747dbe7f735653eac65df946e8b390ee23bc4cbb9b47d4f1b93a81026",
        5122,
        5122,
    ),
    (
        "OBL::defects::S-003",
        4371,
        4371,
        "6295142ce77d696fb81609888eef67e6eb3531e5cb0f5178c049b00cdb6b36ba",
        5107,
        5107,
    ),
)
PROVENANCE_INTERVALS = (
    ("SRC-03429-03518", 3429, 3518),
    ("SRC-03519-03680", 3519, 3680),
    ("SRC-05043-05131", 5043, 5131),
)
SCOPED_ROLES = [
    {
        "glyph": r"\abs",
        "scope": "editorial handbook outside inheritedrestorationscope",
        "standing": "editorial notation",
        "role": "cardinality",
    },
    {
        "glyph": r"\dom",
        "scope": "editorial handbook outside inheritedrestorationscope",
        "standing": "editorial notation",
        "role": "domain operator",
    },
    {
        "glyph": r"\equiv",
        "scope": "editorial handbook outside inheritedrestorationscope",
        "standing": "editorial notation",
        "role": "elementary equivalence",
    },
    {
        "glyph": r"\Leftrightarrow",
        "scope": "editorial handbook outside inheritedrestorationscope",
        "standing": "editorial notation",
        "role": "formula equivalence",
    },
    {
        "glyph": r"\defeq",
        "scope": "editorial handbook outside inheritedrestorationscope",
        "standing": "editorial notation",
        "role": r"definitional abbreviation rendered :\equiv",
    },
    {
        "glyph": r"\abs",
        "scope": "inheritedrestorationscope",
        "standing": "source-supplied notation",
        "role": "the source-supplied vertical-bar role at each exact presentation",
    },
    {
        "glyph": r"\equiv",
        "scope": "inheritedrestorationscope",
        "standing": "source-supplied notation",
        "role": "the source-supplied equivalence role at each exact presentation",
    },
    {
        "glyph": r"\defeq",
        "scope": "inheritedrestorationscope",
        "standing": "source-supplied notation",
        "role": "the source-supplied definitional sign rendered :=",
    },
]
PRESERVATION_TOKENS = {
    "handbook/handbook.sty": sorted(
        [
            r"\renewcommand\defeq{\mathrel{:=}}%",
            r"\renewcommand\abs[1]{\lvert##1\rvert}%",
            r"\renewcommand\Meta{\mathcal M}%",
        ]
    ),
    "tools/test_restoration_scope.py": sorted(
        [r"\ifx\abs\expectedabs", r"\ifx\equiv\expectedequiv", r"\abs{\Meta}" ]
    ),
    "tools/test_part2_reader_route.py": sorted(
        [
            r'surface.count(r"\abs{\Meta}")',
            r'surface.count(r"\equiv")',
            r'self.assertIn(r"\varphi\equiv\psi", surface)',
        ]
    ),
}


def line_excerpt(raw: bytes, start: int, end: int) -> bytes:
    return b"".join(raw.splitlines(keepends=True)[start - 1 : end])


def canonical_digest(value: object) -> str:
    return digest(
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode(
            "utf-8"
        )
    )


class RegisterObligationClosureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="register-closure-test-")
        self.root = Path(self.temporary.name)
        self.obligation_id = "OBL::depth-gaps::D-TEST-001"
        self.source_path = "spec/registers/depth-gaps.csv"
        self.source_line = 2
        self.source_bytes = b"id,item\nD-TEST-001,Test obligation\n"
        self._write(self.source_path, self.source_bytes)
        row_bytes = b"D-TEST-001,Test obligation\n"
        self.record_sha256 = digest(row_bytes)
        original_json = json.dumps(
            {"id": "D-TEST-001", "item": "Test obligation"},
            separators=(",", ":"),
        )
        manifest_output = io.StringIO(newline="")
        writer = csv.DictWriter(
            manifest_output,
            fieldnames=target.MANIFEST_FIELDS,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerow(
            {
                "obligation_id": self.obligation_id,
                "source_register": self.source_path,
                "source_line": str(self.source_line),
                "record_sha256": self.record_sha256,
                "binding_disposition": "open",
                "original_record_json": original_json,
            }
        )
        self.manifest_bytes = manifest_output.getvalue().encode("utf-8")
        self.expected_manifest_count = 1
        self.manifest_path = self._write(
            target.MANIFEST_PATH,
            self.manifest_bytes,
        )
        self.review_path = self.root / "spec/provenance/reviewed-register-obligation-records.json"
        self.unit_inventory = self.root / "spec/handbook-unit-inventory.csv"
        self.unit_reverse = self.root / "spec/handbook-unit-reverse-ledger.csv"
        self.packet_root = self.root / "spec/presentations"
        self.destination_path = "handbook/parts/p01/test.tex"
        self.destination_bytes = b"\\label{def:p01-test-obligation}\nTest content.\n"
        self._write(self.destination_path, self.destination_bytes)
        self.unit_id = "HBU-0123456789abcdef"
        self._write(
            "spec/handbook-unit-inventory.csv",
            f"unit_id\n{self.unit_id}\n".encode("utf-8"),
        )
        reverse_output = io.StringIO(newline="")
        reverse_writer = csv.DictWriter(
            reverse_output,
            fieldnames=(
                "unit_id",
                "mapping_status",
                "semantic_review_status",
                "stable_labels",
                "source_authority_ids",
                "presentation_packet_ids",
                "register_obligation_ids",
            ),
            lineterminator="\n",
        )
        reverse_writer.writeheader()
        reverse_writer.writerow(
            {
                "unit_id": self.unit_id,
                "mapping_status": "mapped/reviewed",
                "semantic_review_status": "pass",
                "stable_labels": '["def:p01-test-obligation"]',
                "source_authority_ids": '["SRC-TEST"]',
                "presentation_packet_ids": "[]",
                "register_obligation_ids": json.dumps(
                    [self.obligation_id], separators=(",", ":")
                ),
            }
        )
        self._write(
            "spec/handbook-unit-reverse-ledger.csv",
            reverse_output.getvalue().encode("utf-8"),
        )
        self.evidence: list[dict[str, object]] = []
        for index, category in enumerate(target.VERIFICATION_FIELDS):
            path = f"spec/evidence/{category}.txt"
            data = f"evidence for {category} and {self.obligation_id}\n".encode("utf-8")
            self._write(path, data)
            item: dict[str, object] = {
                "category": category,
                "recorded_result": "pass",
                "artifact_path": path,
                "sha256": digest(data),
                "producer_identity": f"Reviewer {index}",
                "recorded_scope": f"Review of {self.obligation_id} for {category}",
            }
            if category in target.AI_VERIFICATION_FIELDS:
                item.update(
                    {
                        "model": "self-test-model",
                        "model_version": f"self-test-version-{index}",
                        "instructions": "Check the exact obligation against the consulted authority.",
                        "consulted_authority_files": [
                            {
                                "path": self.source_path,
                                "sha256": digest(self.source_bytes),
                            }
                        ],
                        "consulted_authority_locators": [
                            f"{self.source_path}:{self.source_line}"
                        ],
                        "findings": [f"The {category} fixture passes."],
                        "evidence_digest": digest(data),
                    }
                )
            self.evidence.append(item)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _write(self, relative: str, data: bytes) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def _document(self, records: list[dict[str, object]]) -> dict[str, object]:
        return {
            "schema_version": target.SCHEMA_VERSION,
            "register_manifest_path": target.MANIFEST_PATH,
            "register_manifest_sha256": digest(self.manifest_bytes),
            "records": records,
            "contract_supersessions": [],
        }

    def _record(self) -> dict[str, object]:
        return {
            "obligation_id": self.obligation_id,
            "source_register": self.source_path,
            "source_line": self.source_line,
            "record_sha256": self.record_sha256,
            "completion_status": "complete",
            "handbook_unit_ids": [self.unit_id],
            "presentation_packet_ids": [],
            "destination_labels": ["def:p01-test-obligation"],
            "fulfillment_description": "The admitted handbook unit supplies the exact owed content.",
            "verification": {key: "pass" for key in target.VERIFICATION_FIELDS},
            "verification_evidence": copy.deepcopy(self.evidence),
        }

    def _apply_document(
        self,
        document: dict[str, object],
        *,
        write_unit_files: bool = True,
    ) -> list[dict[str, str]]:
        del write_unit_files
        self.review_path.parent.mkdir(parents=True, exist_ok=True)
        self.review_path.write_text(
            json.dumps(document, indent=2) + "\n",
            encoding="utf-8",
        )
        rows = target.load_manifest(
            self.manifest_path,
            self.root,
            expected_count=self.expected_manifest_count,
            expected_sha256=digest(self.manifest_bytes),
        )
        return target.apply_reviewed_records(
            rows,
            self.review_path,
            self.manifest_path,
            self.root,
            self.unit_inventory,
            self.unit_reverse,
            self.packet_root,
        )

    def _apply_records(self, *records: dict[str, object]) -> list[dict[str, str]]:
        return self._apply_document(self._document(list(records)))

    def _copy_live(self, relative: str) -> Path:
        return self._write(relative, (target.ROOT / relative).read_bytes())

    def _install_supersession_fixture(self) -> dict[str, object]:
        with target.DEFAULT_MANIFEST.open(encoding="utf-8", newline="") as handle:
            live_rows = {
                row["obligation_id"]: row for row in csv.DictReader(handle)
                if row["obligation_id"] in (*SUPERSESSION_IDS, SUPERSESSION_EXCLUDED_ID)
            }
        self.assertEqual(
            set(live_rows), {*SUPERSESSION_IDS, SUPERSESSION_EXCLUDED_ID}
        )
        for relative in {row["source_register"] for row in live_rows.values()}:
            self._copy_live(relative)
        manifest_output = io.StringIO(newline="")
        writer = csv.DictWriter(
            manifest_output, fieldnames=target.MANIFEST_FIELDS, lineterminator="\n"
        )
        writer.writeheader()
        for row in sorted(live_rows.values(), key=lambda item: int(item["source_line"])):
            writer.writerow(row)
        self.manifest_bytes = manifest_output.getvalue().encode("utf-8")
        self.expected_manifest_count = len(live_rows)
        self.manifest_path.write_bytes(self.manifest_bytes)

        for relative, _start, _end in CLAUSE_SPANS:
            if not (self.root / relative).is_file():
                self._copy_live(relative)
        for relative in PRESERVATION_TOKENS:
            if not (self.root / relative).is_file():
                self._copy_live(relative)
        source_path = self._copy_live("source/formal-logic-reference.tex")
        source_raw = source_path.read_bytes()
        source_hash = digest(source_raw)
        self._write("handbook/main.pdf", b"independent rendered fixture\n")

        provenance_records: list[dict[str, object]] = []
        provenance_by_id: dict[str, dict[str, object]] = {}
        artifact_by_id: dict[str, str] = {}
        for provenance_id, start, end in PROVENANCE_INTERVALS:
            fragment = line_excerpt(source_raw, start, end)
            artifact = f"handbook/restoration/inherited-{start:05d}-{end:05d}.tex"
            self._write(artifact, fragment)
            record = {
                "provenance_id": provenance_id,
                "source_locator": {
                    "start_line": start,
                    "end_line": end,
                    "line_count": end - start + 1,
                    "interval_sha256": digest(fragment),
                },
                "restoration_artifact": {
                    "path": artifact,
                    "sha256": digest(fragment),
                },
            }
            path = self._write(
                f"spec/provenance/{provenance_id}.json",
                (json.dumps(record, indent=2) + "\n").encode("utf-8"),
            )
            provenance_records.append(
                {
                    "provenance_id": provenance_id,
                    "path": path.relative_to(self.root).as_posix(),
                    "sha256": digest(path.read_bytes()),
                    "source_start": start,
                    "source_end": end,
                    "interval_sha256": digest(fragment),
                    "restoration_artifact_path": artifact,
                    "restoration_artifact_sha256": digest(fragment),
                }
            )
            provenance_by_id[provenance_id] = record
            artifact_by_id[provenance_id] = artifact

        affected_ranges = (
            ("SRC-03429-03518", 3439, 3447),
            ("SRC-03429-03518", 3472, 3472),
            ("SRC-03519-03680", 3668, 3675),
            ("SRC-05043-05131", 5053, 5053),
            ("SRC-05043-05131", 5107, 5107),
            ("SRC-05043-05131", 5122, 5122),
        )
        unit_fields = (
            "unit_id",
            "record_type",
            "path",
            "start_line",
            "end_line",
            "bytes",
            "sha256",
            "unit_kind",
        )
        unit_rows: list[dict[str, str]] = []
        affected_units: list[dict[str, object]] = []
        for index, (provenance_id, source_start, source_end) in enumerate(
            affected_ranges, start=1
        ):
            provenance = provenance_by_id[provenance_id]
            interval_start = provenance["source_locator"]["start_line"]  # type: ignore[index]
            local_start = source_start - interval_start + 1  # type: ignore[operator]
            local_end = source_end - interval_start + 1  # type: ignore[operator]
            artifact = artifact_by_id[provenance_id]
            artifact_raw = (self.root / artifact).read_bytes()
            unit_raw = line_excerpt(artifact_raw, local_start, local_end)
            identity = {
                "unit_id": f"HBU-{index:024x}",
                "record_type": "physical_interval",
                "path": artifact,
                "start_line": str(local_start),
                "end_line": str(local_end),
                "bytes": str(len(unit_raw)),
                "sha256": digest(unit_raw),
                "unit_kind": "source-preserved-interval",
            }
            unit_rows.append(identity)
            affected_units.append(
                {
                    **{
                        key: int(value) if key in {"start_line", "end_line", "bytes"} else value
                        for key, value in identity.items()
                    },
                    "identity_sha256": canonical_digest(identity),
                }
            )
        inventory_output = io.StringIO(newline="")
        inventory_writer = csv.DictWriter(
            inventory_output, fieldnames=unit_fields, lineterminator="\n"
        )
        inventory_writer.writeheader()
        inventory_writer.writerows(unit_rows)
        self.unit_inventory.write_bytes(inventory_output.getvalue().encode("utf-8"))

        clauses: list[dict[str, object]] = []
        for relative, start, end in CLAUSE_SPANS:
            raw = (self.root / relative).read_bytes()
            clauses.append(
                {
                    "path": relative,
                    "sha256": digest(raw),
                    "start_line": start,
                    "end_line": end,
                    "excerpt_sha256": digest(line_excerpt(raw, start, end)),
                }
            )
        current_locators: list[dict[str, object]] = []
        for obligation_id, start, end, token in CURRENT_LOCATORS:
            current_locators.append(
                {
                    "obligation_id": obligation_id,
                    "revision": "v1.1-verified",
                    "source_path": "source/formal-logic-reference.tex",
                    "source_sha256": source_hash,
                    "start_line": start,
                    "end_line": end,
                    "excerpt_sha256": digest(line_excerpt(source_raw, start, end)),
                    "required_tokens": [token],
                }
            )
        revision_pairs: list[dict[str, object]] = []
        for (
            obligation_id,
            old_start,
            old_end,
            old_excerpt_hash,
            current_start,
            current_end,
        ) in REVISION_PAIRS:
            revision_pairs.append(
                {
                    "obligation_id": obligation_id,
                    "historical_revision": "v1.0-audit",
                    "historical_source_sha256": "81bf3c0ab12863d7d89e1b44648ccc1d63832dc68ab8e32b84aa9a0700cd6de1",
                    "historical_start_line": old_start,
                    "historical_end_line": old_end,
                    "historical_excerpt_sha256": old_excerpt_hash,
                    "current_revision": "v1.1-verified",
                    "current_source_path": "source/formal-logic-reference.tex",
                    "current_source_sha256": source_hash,
                    "current_start_line": current_start,
                    "current_end_line": current_end,
                    "current_excerpt_sha256": digest(
                        line_excerpt(source_raw, current_start, current_end)
                    ),
                }
            )
        preservation_controls: list[dict[str, object]] = []
        for relative, tokens in PRESERVATION_TOKENS.items():
            raw = (self.root / relative).read_bytes()
            preservation_controls.append(
                {
                    "path": relative,
                    "sha256": digest(raw),
                    "required_tokens": tokens,
                }
            )

        obligation_records: list[dict[str, object]] = []
        superseded_fields = {
            "OBL::defects::S-002": ("required_fix", "acceptance"),
            "OBL::defects::S-003": ("required_fix", "acceptance"),
            "OBL::apparatus::A-167": ("spec", "status"),
            "OBL::apparatus::A-168": ("spec", "status"),
        }
        for obligation_id in SUPERSESSION_IDS:
            base = live_rows[obligation_id]
            original = json.loads(base["original_record_json"])
            fields = []
            for field_name in superseded_fields[obligation_id]:
                value = original[field_name]
                fields.append(
                    {
                        "field_name": field_name,
                        "original_value": value,
                        "original_value_sha256": digest(value.encode("utf-8")),
                    }
                )
            obligation_records.append(
                {
                    "obligation_id": obligation_id,
                    "source_register": base["source_register"],
                    "source_line": int(base["source_line"]),
                    "record_sha256": base["record_sha256"],
                    "original_record_json_sha256": digest(
                        base["original_record_json"].encode("utf-8")
                    ),
                    "superseded_fields": fields,
                }
            )

        rendered = self.root / "handbook/main.pdf"
        group: dict[str, object] = {
            "supersession_id": SUPERSESSION_ID,
            "obligations": obligation_records,
            "binding_contract_clauses": clauses,
            "revision_locator_pairs": revision_pairs,
            "current_source_locators": current_locators,
            "affected_handbook_units": affected_units,
            "affected_provenance_records": provenance_records,
            "surviving_scoped_roles": copy.deepcopy(SCOPED_ROLES),
            "preservation_controls": preservation_controls,
            "rendered_artifact": {
                "path": "handbook/main.pdf",
                "sha256": digest(rendered.read_bytes()),
                "bytes": rendered.stat().st_size,
            },
            "supersession_statement": SUPERSESSION_STATEMENT,
            "verification": {key: "pass" for key in target.VERIFICATION_FIELDS},
            "verification_evidence": [],
        }
        authority_paths = {
            item["path"] for item in clauses
        } | {"source/formal-logic-reference.tex"} | {
            item["path"] for item in provenance_records
        } | set(PRESERVATION_TOKENS) | {
            "spec/handbook-unit-inventory.csv",
            target.MANIFEST_PATH,
        } | {row["source_register"] for row in live_rows.values()}
        authority_files = [
            {
                "path": relative,
                "sha256": digest((self.root / relative).read_bytes()),
            }
            for relative in sorted(authority_paths)
        ]
        locators = sorted(
            [f"{path}:{start}-{end}" for path, start, end in CLAUSE_SPANS]
            + [
                f"v1.0-audit:{old_start}-{old_end}->v1.1-verified:{new_start}-{new_end}"
                for _obligation, old_start, old_end, _old_hash, new_start, new_end in REVISION_PAIRS
            ]
            + [
                f"source/formal-logic-reference.tex:{start}-{end}@v1.1-verified"
                for _obligation, start, end, _token in CURRENT_LOCATORS
            ]
            + [
                f"{live_rows[obligation_id]['source_register']}:"
                f"{live_rows[obligation_id]['source_line']}"
                for obligation_id in SUPERSESSION_IDS
            ]
        )
        evidence: list[dict[str, object]] = []
        for index, category in enumerate(target.VERIFICATION_FIELDS):
            relative = f"spec/evidence/supersession-{category}.txt"
            raw = f"independent evidence {category} for {SUPERSESSION_ID}\n".encode()
            self._write(relative, raw)
            item: dict[str, object] = {
                "category": category,
                "recorded_result": "pass",
                "artifact_path": relative,
                "sha256": digest(raw),
                "producer_identity": f"Supersession reviewer {index}",
                "recorded_scope": (
                    f"Atomic {SUPERSESSION_ID}: " + ", ".join(SUPERSESSION_IDS)
                ),
            }
            if category in target.AI_VERIFICATION_FIELDS:
                item.update(
                    {
                        "model": "self-test-model",
                        "model_version": f"supersession-version-{index}",
                        "instructions": "Check only the exact four-row contract conflict without waiving source fidelity.",
                        "consulted_authority_files": copy.deepcopy(authority_files),
                        "consulted_authority_locators": locators,
                        "findings": [f"The atomic {category} review passes without changing source tokens."],
                        "evidence_digest": digest(raw),
                    }
                )
            evidence.append(item)
        group["verification_evidence"] = evidence
        return group

    def test_empty_reviewed_input_yields_explicit_open_without_semantic_files(self) -> None:
        self.unit_inventory.unlink()
        self.unit_reverse.unlink()
        first = self._apply_records()
        second = self._apply_records()
        self.assertEqual(first, second)
        self.assertEqual(len(first), 1)
        self.assertEqual(first[0]["completion_status"], "OPEN")
        self.assertEqual(first[0]["visual_verification"], "pending")
        self.assertEqual(first[0]["handbook_unit_ids"], "[]")

    def test_contract_supersessions_is_a_separate_required_collection(self) -> None:
        document = self._document([])
        del document["contract_supersessions"]
        with self.assertRaisesRegex(ValueError, "contract_supersessions"):
            self._apply_document(document)

    def test_empty_live_collection_keeps_the_atomic_four_and_a172_open(self) -> None:
        rows, _csv_raw, _markdown_raw = target.build_outputs(
            target.DEFAULT_MANIFEST,
            target.DEFAULT_REVIEWED,
            target.ROOT,
        )
        by_id = {row["obligation_id"]: row for row in rows}
        for obligation_id in (*SUPERSESSION_IDS, SUPERSESSION_EXCLUDED_ID):
            with self.subTest(obligation_id=obligation_id):
                self.assertEqual(by_id[obligation_id]["completion_status"], "OPEN")
                self.assertEqual(by_id[obligation_id]["contract_supersession_id"], "")

    def test_exact_atomic_contract_supersession_projects_four_terminal_noncompletions(self) -> None:
        group = self._install_supersession_fixture()
        document = self._document([])
        document["contract_supersessions"] = [group]
        schema = json.loads(
            (
                target.ROOT
                / "spec/provenance/reviewed-register-obligation-records.schema.json"
            ).read_text(encoding="utf-8")
        )
        jsonschema.Draft202012Validator(
            {
                "$schema": schema["$schema"],
                "$defs": schema["$defs"],
                "$ref": "#/$defs/contractSupersession",
            }
        ).validate(group)
        first = self._apply_document(document)
        second = self._apply_document(copy.deepcopy(document))
        self.assertEqual(first, second)
        self.assertEqual(
            {row["obligation_id"] for row in first},
            {*SUPERSESSION_IDS, SUPERSESSION_EXCLUDED_ID},
        )
        by_id = {row["obligation_id"]: row for row in first}
        self.assertEqual(
            {
                by_id[obligation_id]["completion_status"]
                for obligation_id in SUPERSESSION_IDS
            },
            {"SUPERSEDED_BY_CONTRACT"},
        )
        self.assertEqual(by_id[SUPERSESSION_EXCLUDED_ID]["completion_status"], "OPEN")
        self.assertEqual(by_id[SUPERSESSION_EXCLUDED_ID]["contract_supersession_id"], "")
        self.assertNotIn("COMPLETE", {row["completion_status"] for row in first})

    def test_contract_supersession_rejects_nonatomic_duplicate_and_overlapping_records(self) -> None:
        group = self._install_supersession_fixture()

        partial = copy.deepcopy(group)
        partial["obligations"].pop()  # type: ignore[union-attr]
        document = self._document([])
        document["contract_supersessions"] = [partial]
        with self.assertRaisesRegex(ValueError, "exact atomic four-row group"):
            self._apply_document(document)

        arbitrary = copy.deepcopy(group)
        arbitrary["obligations"][3]["obligation_id"] = "OBL::defects::S-999"  # type: ignore[index]
        document["contract_supersessions"] = [arbitrary]
        with self.assertRaisesRegex(ValueError, "partial, arbitrary, duplicate"):
            self._apply_document(document)

        duplicate_obligation = copy.deepcopy(group)
        duplicate_obligation["obligations"][3] = copy.deepcopy(  # type: ignore[index]
            duplicate_obligation["obligations"][2]  # type: ignore[index]
        )
        document["contract_supersessions"] = [duplicate_obligation]
        with self.assertRaisesRegex(ValueError, "partial, arbitrary, duplicate"):
            self._apply_document(document)

        excluded = copy.deepcopy(group)
        excluded["obligations"][3]["obligation_id"] = SUPERSESSION_EXCLUDED_ID  # type: ignore[index]
        document["contract_supersessions"] = [excluded]
        with self.assertRaisesRegex(ValueError, "A-172 is outside"):
            self._apply_document(document)

        document["contract_supersessions"] = [group, copy.deepcopy(group)]
        with self.assertRaisesRegex(ValueError, "duplicate atomic record"):
            self._apply_document(document)

        document = self._document([{"obligation_id": SUPERSESSION_IDS[0]}])
        document["contract_supersessions"] = [group]
        with self.assertRaisesRegex(ValueError, "ordinary completion.*overlap"):
            self._apply_document(document)

        document = self._document([{"obligation_id": SUPERSESSION_IDS[0]}])
        with self.assertRaisesRegex(ValueError, "ordinary completion is forbidden"):
            self._apply_document(document)

    def test_contract_supersession_rejects_stale_contract_source_unit_and_rendering_pins(self) -> None:
        group = self._install_supersession_fixture()

        cases: list[tuple[str, tuple[object, ...], object, str]] = [
            (
                "immutable row identity",
                ("obligations", 0, "record_sha256"),
                "0" * 64,
                "stale immutable row identity",
            ),
            (
                "superseded field",
                ("obligations", 0, "superseded_fields", 0, "field_name"),
                "status",
                "wrong superseded field",
            ),
            (
                "contract clause",
                ("binding_contract_clauses", 0, "excerpt_sha256"),
                "0" * 64,
                "contract clause drift",
            ),
            (
                "source token locator",
                ("current_source_locators", 0, "required_tokens"),
                ["generic token"],
                "mixed or stale source coordinate",
            ),
            (
                "mixed coordinate revision",
                ("revision_locator_pairs", 0, "current_revision"),
                "v1.0-audit",
                "mixed coordinate revisions",
            ),
            (
                "provenance identity",
                ("affected_provenance_records", 0, "sha256"),
                "0" * 64,
                "provenance record drift",
            ),
            (
                "unit identity",
                ("affected_handbook_units", 0, "identity_sha256"),
                "0" * 64,
                "stale or incomplete unit set",
            ),
            (
                "preservation control",
                ("preservation_controls", 0, "sha256"),
                "0" * 64,
                "preservation control drift",
            ),
            (
                "rendered bytes",
                ("rendered_artifact", "bytes"),
                999999,
                "rendering changed",
            ),
        ]
        for label, path, replacement, pattern in cases:
            with self.subTest(label=label):
                changed = copy.deepcopy(group)
                cursor: object = changed
                for key in path[:-1]:
                    cursor = cursor[key]  # type: ignore[index]
                cursor[path[-1]] = replacement  # type: ignore[index]
                document = self._document([])
                document["contract_supersessions"] = [changed]
                with self.assertRaisesRegex(ValueError, pattern):
                    self._apply_document(document)

    def test_contract_supersession_rejects_generic_self_reused_and_ungoverned_evidence(self) -> None:
        group = self._install_supersession_fixture()

        generic = copy.deepcopy(group)
        generic["supersession_statement"] = "The notation obligations are waived."  # type: ignore[index]
        document = self._document([])
        document["contract_supersessions"] = [generic]
        with self.assertRaisesRegex(ValueError, "generic waivers are forbidden"):
            self._apply_document(document)

        generic_scope = copy.deepcopy(group)
        generic_scope["verification_evidence"][0]["recorded_scope"] = (  # type: ignore[index]
            f"Review mentioning {SUPERSESSION_ID} and " + ", ".join(SUPERSESSION_IDS)
        )
        document["contract_supersessions"] = [generic_scope]
        with self.assertRaisesRegex(ValueError, "exact atomic scope"):
            self._apply_document(document)

        reused = copy.deepcopy(group)
        reused["verification_evidence"][1]["artifact_path"] = (  # type: ignore[index]
            reused["verification_evidence"][0]["artifact_path"]  # type: ignore[index]
        )
        reused["verification_evidence"][1]["sha256"] = (  # type: ignore[index]
            reused["verification_evidence"][0]["sha256"]  # type: ignore[index]
        )
        document["contract_supersessions"] = [reused]
        with self.assertRaisesRegex(ValueError, "reused evidence file"):
            self._apply_document(document)

        copied = copy.deepcopy(group)
        original = copied["verification_evidence"][0]  # type: ignore[index]
        original_raw = (self.root / original["artifact_path"]).read_bytes()  # type: ignore[index]
        copied_path = "spec/evidence/copied-supersession-review.txt"
        self._write(copied_path, original_raw)
        copied["verification_evidence"][1]["artifact_path"] = copied_path  # type: ignore[index]
        copied["verification_evidence"][1]["sha256"] = digest(original_raw)  # type: ignore[index]
        document["contract_supersessions"] = [copied]
        with self.assertRaisesRegex(ValueError, "reused or copied evidence"):
            self._apply_document(document)

        self_evidence = copy.deepcopy(group)
        self_evidence["verification_evidence"][0]["artifact_path"] = target.MANIFEST_PATH  # type: ignore[index]
        self_evidence["verification_evidence"][0]["sha256"] = digest(self.manifest_bytes)  # type: ignore[index]
        document["contract_supersessions"] = [self_evidence]
        with self.assertRaisesRegex(ValueError, "self evidence is forbidden"):
            self._apply_document(document)

        same_producer = copy.deepcopy(group)
        same_producer["verification_evidence"][1]["producer_identity"] = (  # type: ignore[index]
            same_producer["verification_evidence"][0]["producer_identity"].upper()  # type: ignore[index]
        )
        document["contract_supersessions"] = [same_producer]
        with self.assertRaisesRegex(ValueError, "distinct producer"):
            self._apply_document(document)

        ungoverned = copy.deepcopy(group)
        ungoverned["verification_evidence"][0]["consulted_authority_files"] = (  # type: ignore[index]
            ungoverned["verification_evidence"][0]["consulted_authority_files"][:-1]  # type: ignore[index]
        )
        document["contract_supersessions"] = [ungoverned]
        with self.assertRaisesRegex(ValueError, "exact governed authorities"):
            self._apply_document(document)

    def test_valid_terminal_unit_record_is_complete_and_deterministic(self) -> None:
        first = self._apply_records(self._record())
        second = self._apply_records(self._record())
        self.assertEqual(first, second)
        self.assertEqual(first[0]["completion_status"], "COMPLETE")
        self.assertEqual(first[0]["visual_verification"], "pass")
        self.assertEqual(json.loads(first[0]["handbook_unit_ids"]), [self.unit_id])
        self.assertEqual(
            json.loads(first[0]["destination_labels"]),
            ["def:p01-test-obligation"],
        )

    def test_unknown_duplicate_and_stale_register_identities_fail_closed(self) -> None:
        duplicate = self._record()
        with self.assertRaisesRegex(ValueError, "duplicate obligation ID"):
            self._apply_records(duplicate, copy.deepcopy(duplicate))

        unknown = self._record()
        unknown["obligation_id"] = "OBL::depth-gaps::UNKNOWN"
        with self.assertRaisesRegex(ValueError, "unknown obligation ID"):
            self._apply_records(unknown)

        for field, value in (
            ("source_register", "spec/registers/new-content.csv"),
            ("source_line", 3),
            ("record_sha256", "0" * 64),
        ):
            with self.subTest(field=field):
                stale = self._record()
                stale[field] = value
                with self.assertRaisesRegex(ValueError, "stale or mismatched"):
                    self._apply_records(stale)

    def test_exact_shapes_and_types_are_required(self) -> None:
        document = self._document([])
        document["extra"] = True
        with self.assertRaisesRegex(ValueError, "unexpected"):
            self._apply_document(document)

        record = self._record()
        del record["fulfillment_description"]
        with self.assertRaisesRegex(ValueError, "missing"):
            self._apply_records(record)

        record = self._record()
        record["source_line"] = True
        with self.assertRaisesRegex(ValueError, "expected integer"):
            self._apply_records(record)

        raw = json.dumps(self._document([]))
        marker = f'"schema_version": {target.SCHEMA_VERSION},'
        raw = raw.replace(marker, f'{marker} {marker}')
        self.review_path.parent.mkdir(parents=True, exist_ok=True)
        self.review_path.write_text(raw, encoding="utf-8")
        rows = target.load_manifest(
            self.manifest_path,
            self.root,
            expected_count=1,
            expected_sha256=digest(self.manifest_bytes),
        )
        with self.assertRaisesRegex(ValueError, "duplicate JSON field"):
            target.apply_reviewed_records(
                rows,
                self.review_path,
                self.manifest_path,
                self.root,
                self.unit_inventory,
                self.unit_reverse,
                self.packet_root,
            )

    def test_manifest_and_live_source_drift_are_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "manifest SHA-256 drift"):
            target.load_manifest(
                self.manifest_path,
                self.root,
                expected_count=1,
                expected_sha256="0" * 64,
            )
        self._write(self.source_path, b"id,item\nD-TEST-001,Changed obligation\n")
        with self.assertRaisesRegex(ValueError, "source-record SHA-256 drift"):
            target.load_manifest(
                self.manifest_path,
                self.root,
                expected_count=1,
                expected_sha256=digest(self.manifest_bytes),
            )

    def test_unit_support_must_be_known_admitted_reviewed_and_reciprocal(self) -> None:
        record = self._record()
        record["handbook_unit_ids"] = ["HBU-deadbeef"]
        with self.assertRaisesRegex(ValueError, "unknown unit ID"):
            self._apply_records(record)

        reverse = self.unit_reverse.read_text(encoding="utf-8")
        self.unit_reverse.write_text(reverse.replace("mapped/reviewed", "open/unmapped"), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "unadmitted"):
            self._apply_records(self._record())

        self.unit_reverse.write_text(
            reverse.replace(self.obligation_id, self.obligation_id + "-OTHER"),
            encoding="utf-8",
        )
        with self.assertRaisesRegex(ValueError, "does not link this obligation"):
            self._apply_records(self._record())

    def test_completion_requires_support_exact_labels_and_live_unique_labels(self) -> None:
        record = self._record()
        record["handbook_unit_ids"] = []
        with self.assertRaisesRegex(ValueError, "requires a handbook unit or presentation packet"):
            self._apply_records(record)

        record = self._record()
        record["destination_labels"] = ["def:p01-other"]
        with self.assertRaisesRegex(ValueError, "exactly equal linked support labels"):
            self._apply_records(record)

        self._write(
            "handbook/parts/p02/duplicate.tex",
            b"\\label{def:p01-test-obligation}\n",
        )
        with self.assertRaisesRegex(ValueError, "occurs 2 times"):
            self._apply_records(self._record())

    def test_missing_and_unverified_packet_support_is_rejected(self) -> None:
        record = self._record()
        record["handbook_unit_ids"] = []
        record["presentation_packet_ids"] = ["missing.packet"]
        with self.assertRaisesRegex(ValueError, "unknown packet ID"):
            self._apply_records(record)

        self.packet_root.mkdir(parents=True, exist_ok=True)
        (self.packet_root / "open.json").write_text(
            json.dumps({"packet_id": "open.packet", "overall_status": "open"}),
            encoding="utf-8",
        )
        record["presentation_packet_ids"] = ["open.packet"]
        with self.assertRaisesRegex(ValueError, "packet is not verified"):
            self._apply_records(record)

    def test_all_verification_gates_and_evidence_categories_are_required(self) -> None:
        record = self._record()
        record["verification"]["visual"] = "pending"  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "completion requires pass"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"] = record["verification_evidence"][:-1]  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "exactly six"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][1]["category"] = "source_fidelity_ai"  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "duplicate evidence category"):
            self._apply_records(record)

    def test_evidence_paths_hashes_producers_and_scopes_fail_closed(self) -> None:
        record = self._record()
        record["verification_evidence"][0]["artifact_path"] = "../outside.txt"  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "inside the repository"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][0]["sha256"] = "0" * 64  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "evidence SHA-256 drift"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][1]["artifact_path"] = record["verification_evidence"][0]["artifact_path"]  # type: ignore[index]
        record["verification_evidence"][1]["sha256"] = record["verification_evidence"][0]["sha256"]  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "separate evidence files"):
            self._apply_records(record)

        record = self._record()
        original_path = record["verification_evidence"][0]["artifact_path"]  # type: ignore[index]
        copied_bytes = (self.root / original_path).read_bytes()
        copied_path = "spec/evidence/copied-independent-source.txt"
        self._write(copied_path, copied_bytes)
        record["verification_evidence"][1]["artifact_path"] = copied_path  # type: ignore[index]
        record["verification_evidence"][1]["sha256"] = digest(copied_bytes)  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "reuse identical artifact bytes"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][1]["producer_identity"] = "REVIEWER 0"  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "distinct recorded producer"):
            self._apply_records(record)

        record = self._record()
        record["verification_evidence"][0]["recorded_scope"] = "generic review"  # type: ignore[index]
        with self.assertRaisesRegex(ValueError, "exact obligation ID"):
            self._apply_records(record)

    def test_source_destination_support_and_input_cannot_self_evidence(self) -> None:
        cases = (
            self.source_path,
            self.destination_path,
            target.MANIFEST_PATH,
            "spec/handbook-unit-inventory.csv",
            "spec/handbook-unit-reverse-ledger.csv",
            "spec/provenance/reviewed-register-obligation-records.json",
        )
        for path in cases:
            with self.subTest(path=path):
                record = self._record()
                record["verification_evidence"][0]["artifact_path"] = path  # type: ignore[index]
                record["verification_evidence"][0]["sha256"] = digest((self.root / path).read_bytes())  # type: ignore[index]
                with self.assertRaisesRegex(ValueError, "cannot be its own evidence"):
                    self._apply_records(record)

    def test_committed_schema_and_empty_document_match_the_runtime_interface(self) -> None:
        schema = json.loads(
            (target.ROOT / "spec/provenance/reviewed-register-obligation-records.schema.json").read_text(encoding="utf-8")
        )
        document = json.loads(target.DEFAULT_REVIEWED.read_text(encoding="utf-8"))
        self.assertEqual(schema["properties"]["schema_version"]["const"], target.SCHEMA_VERSION)
        self.assertEqual(schema["properties"]["schema_version"]["type"], "integer")
        self.assertEqual(document["schema_version"], target.SCHEMA_VERSION)
        self.assertEqual(document["records"], [])
        self.assertEqual(document["contract_supersessions"], [])
        self.assertEqual(
            set(schema["required"]),
            {
                "schema_version",
                "register_manifest_path",
                "register_manifest_sha256",
                "records",
                "contract_supersessions",
            },
        )
        supersession_collection = schema["properties"]["contract_supersessions"]
        self.assertEqual(supersession_collection["maxItems"], 1)
        self.assertEqual(
            supersession_collection["items"]["$ref"],
            "#/$defs/contractSupersession",
        )
        contract = schema["$defs"]["contractSupersession"]
        self.assertEqual(set(contract["required"]), target.CONTRACT_SUPERSESSION_FIELDS)
        self.assertEqual(set(contract["properties"]), target.CONTRACT_SUPERSESSION_FIELDS)
        rationale = contract["$comment"]
        for heading in ("Necessity:", "Definition:", "Standing:", "Nonredundancy:", "Use:"):
            self.assertIn(heading, rationale)
        self.assertEqual(
            contract["properties"]["supersession_id"]["const"],
            SUPERSESSION_ID,
        )
        self.assertEqual(
            contract["properties"]["supersession_statement"]["const"],
            SUPERSESSION_STATEMENT,
        )
        obligation_items = contract["properties"]["obligations"]["prefixItems"]
        self.assertEqual(
            [item["properties"]["obligation_id"]["const"] for item in obligation_items],
            list(SUPERSESSION_IDS),
        )
        self.assertEqual(set(schema["$defs"]["record"]["required"]), target.RECORD_FIELDS)
        self.assertEqual(set(schema["$defs"]["record"]["properties"]), target.RECORD_FIELDS)
        self.assertEqual(
            set(schema["$defs"]["aiEvidence"]["required"]),
            target.AI_EVIDENCE_FIELDS,
        )
        self.assertEqual(
            set(schema["$defs"]["mechanicalEvidence"]["required"]),
            target.MECHANICAL_EVIDENCE_FIELDS,
        )


if __name__ == "__main__":
    unittest.main()
