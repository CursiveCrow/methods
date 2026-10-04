#!/usr/bin/env python3
"""Focused regression tests for historical/current handbook tree records."""

from __future__ import annotations

import hashlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))

import build_handbook_source_inventory as inventory  # noqa: E402
import check_full_compendium_controls as controls  # noqa: E402
import check_handbook_audit_snapshot as historical  # noqa: E402
import check_handbook_construction_snapshot as construction  # noqa: E402
import handbook_tree_manifest as tree_manifest  # noqa: E402


class TreeManifestTests(unittest.TestCase):
    def make_tree(self, root: Path, content: bytes = b"alpha\n") -> Path:
        handbook = root / "handbook"
        handbook.mkdir()
        (handbook / "source.tex").write_bytes(content)
        return handbook

    def test_unknown_suffix_is_included_but_exact_transient_is_excluded(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            handbook = self.make_tree(root)
            (handbook / "other.aux").write_bytes(b"source-like\n")
            (handbook / "main.aux").write_bytes(b"build output\n")
            (handbook / "opaque.newkind").write_bytes(b"opaque\x00input")
            paths = {
                row["path"] for row in tree_manifest.live_rows(handbook, root)
            }
        self.assertEqual(
            paths,
            {
                "handbook/opaque.newkind",
                "handbook/other.aux",
                "handbook/source.tex",
            },
        )

    def test_manifest_parser_rejects_noncanonical_or_unsafe_rows(self) -> None:
        unsafe = (
            b"path,bytes,sha256\n"
            + b"handbook/../escape,1,"
            + (b"0" * 64)
            + b"\n"
        )
        with self.assertRaisesRegex(ValueError, "unsafe path"):
            tree_manifest.parse(unsafe)

        noncanonical = (
            b"path,bytes,sha256\r\n"
            + b"handbook/a,01,"
            + (b"0" * 64)
            + b"\r\n"
        )
        with self.assertRaisesRegex(ValueError, "non-canonical byte count"):
            tree_manifest.parse(noncanonical)

    def test_candidate_creation_is_explicit_safe_and_non_overwriting(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            allowed = root / "spec"
            allowed.mkdir()
            candidate = allowed / "candidate.csv"
            tree_manifest.write_new_candidate(
                candidate, b"candidate\n", allowed_root=allowed
            )
            self.assertEqual(candidate.read_bytes(), b"candidate\n")
            with self.assertRaisesRegex(ValueError, "already exists"):
                tree_manifest.write_new_candidate(
                    candidate, b"replacement\n", allowed_root=allowed
                )
            with self.assertRaisesRegex(ValueError, "outside"):
                tree_manifest.write_new_candidate(
                    root / "outside.csv", b"bad\n", allowed_root=allowed
                )
            governed = allowed / "governed.csv"
            with self.assertRaisesRegex(ValueError, "governed canonical"):
                tree_manifest.write_new_candidate(
                    governed,
                    b"bad\n",
                    allowed_root=allowed,
                    forbidden_paths={governed},
                )


class SnapshotSeparationTests(unittest.TestCase):
    def test_historical_record_does_not_require_live_tree_equality(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            rows = [
                {
                    "path": "handbook/then.tex",
                    "bytes": "4",
                    "sha256": hashlib.sha256(b"then").hexdigest(),
                }
            ]
            manifest_raw = tree_manifest.render(rows)
            manifest = root / "historical.csv"
            manifest.write_bytes(manifest_raw)
            handbook = root / "handbook"
            handbook.mkdir()
            (handbook / "now.tex").write_bytes(b"different live tree")

            recorded = historical.verify_record(
                manifest, hashlib.sha256(manifest_raw).hexdigest()
            )

        self.assertEqual(recorded, rows)

    def test_current_record_requires_manifest_anchor_and_live_equality(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            handbook = root / "handbook"
            handbook.mkdir()
            source = handbook / "source.tex"
            source.write_bytes(b"current\n")
            manifest_raw = tree_manifest.render(
                tree_manifest.live_rows(handbook, root)
            )
            manifest = root / "current.csv"
            manifest.write_bytes(manifest_raw)
            expected_hash = hashlib.sha256(manifest_raw).hexdigest()

            rows = construction.verify_current(
                manifest, expected_hash, handbook, root
            )
            self.assertEqual(len(rows), 1)
            source.write_bytes(b"drifted\n")
            with self.assertRaisesRegex(ValueError, "source tree drifted"):
                construction.verify_current(
                    manifest, expected_hash, handbook, root
                )
            with self.assertRaisesRegex(ValueError, "authority is not frozen"):
                construction.verify_current(manifest, "PENDING", handbook, root)

    def test_historical_checker_has_no_write_option(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(TOOLS / "check_handbook_audit_snapshot.py"),
                "--write",
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("unrecognized arguments", result.stderr)

    def test_inventory_tool_has_no_implicit_historical_write_mode(self) -> None:
        governed = [
            ROOT / "spec/handbook-audit-snapshot.csv",
            ROOT / "spec/handbook-source-inventory.csv",
            ROOT / "spec/handbook-source-inventory.md",
        ]
        before = [hashlib.sha256(path.read_bytes()).hexdigest() for path in governed]
        result = subprocess.run(
            [sys.executable, str(TOOLS / "build_handbook_source_inventory.py")],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        after = [hashlib.sha256(path.read_bytes()).hexdigest() for path in governed]
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("one of the arguments", result.stderr)
        self.assertEqual(after, before)

    def test_existing_historical_snapshot_and_inventory_remain_anchored(self) -> None:
        rows = historical.verify_record()
        files, lines = inventory.verify_historical()
        self.assertEqual(len(rows), 214)
        self.assertEqual((files, lines), (214, 35669))

    def test_inventory_build_stays_open_and_matches_snapshot_file_rows(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            handbook = root / "handbook"
            handbook.mkdir()
            (handbook / "a.tex").write_bytes(b"one\ntwo\n")
            snapshot_rows = tree_manifest.live_rows(handbook, root)
            rows = inventory.build(snapshot_rows, root)
            files, lines = inventory.verify_inventory_structure(rows, snapshot_rows)
        self.assertEqual((files, lines), (1, 2))
        self.assertTrue(all(row["provenance_status"] == "open/unmapped" for row in rows))
        self.assertTrue(all(row["source_authority_ids"] == "[]" for row in rows))


class AggregateControlTests(unittest.TestCase):
    def test_current_tree_check_is_first_and_last(self) -> None:
        commands = controls.command_list("python-fixture")
        expected = ["python-fixture", "tools/check_handbook_construction_snapshot.py"]
        self.assertEqual(commands[0], expected)
        self.assertEqual(commands[-1], expected)
        self.assertIn(
            [
                "python-fixture",
                "tools/build_handbook_source_inventory.py",
                "--check-construction",
            ],
            commands,
        )

    def test_all_independent_controls_run_and_all_failures_are_returned(self) -> None:
        commands = [["python", f"control-{index}"] for index in range(4)]
        with mock.patch.object(controls, "run", side_effect=[1, 0, 7, 0]) as run:
            failures = controls.run_all(commands)
        self.assertEqual(run.call_count, 4)
        self.assertEqual(failures, [(commands[0], 1), (commands[2], 7)])


if __name__ == "__main__":
    unittest.main()
