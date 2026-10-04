#!/usr/bin/env python3
"""Focused CLI tests for corpus-level packet-admission reporting."""

from __future__ import annotations

import contextlib
import hashlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parent
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import build_presentation_packet_admission as admission  # noqa: E402
import check_presentation_packet as packet_checker  # noqa: E402
import check_presentation_packet_corpus as corpus  # noqa: E402


EMPTY_ADMISSION_CSV = (
    "packet_id,packet_path,packet_sha256,admission_status,"
    "authority_projection_sha256,presentation_identity_projection_sha256,"
    "content_projection_sha256,present_content_item_ids,destination_file,"
    "destination_sha256,destination_labels,source_fidelity_ai_verification,"
    "topic_specialist_ai_verification,adversarial_publication_ai_verification,"
    "static_verification,build_verification,visual_verification,"
    "verification_evidence\n"
).encode("utf-8")


class PresentationPacketCorpusAdmissionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(prefix="packet-corpus-admission-")
        self.root = Path(self.temporary.name)
        (self.root / "spec/presentations").mkdir(parents=True)
        self.coverage = self.write("spec/coverage.csv", b"stable_id\nSRC-001\n")
        self.register = self.write("spec/register.csv", b"obligation_id\n")
        self.reviewed = self.root / "spec/reviewed-admissions.json"
        self.reviewed.write_text(
            json.dumps(
                {
                    "schema_version": admission.SCHEMA_VERSION,
                    "packet_root": "spec/presentations",
                    "records": [],
                }
            )
            + "\n",
            encoding="utf-8",
        )
        self.projection = self.write("spec/admission.csv", EMPTY_ADMISSION_CSV)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write(self, relative: str, raw: bytes) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        return path

    def arguments(self, *extra: str) -> list[str]:
        return [
            "--repository-root",
            str(self.root),
            "--packet-root",
            "spec/presentations",
            "--coverage-manifest",
            "spec/coverage.csv",
            "--register-manifest",
            "spec/register.csv",
            "--reviewed-admissions",
            "spec/reviewed-admissions.json",
            "--admission-projection",
            "spec/admission.csv",
            *extra,
        ]

    def invoke(self, *extra: str) -> tuple[int, str, str]:
        stdout = io.StringIO()
        stderr = io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            result = corpus.main(self.arguments(*extra))
        return result, stdout.getvalue(), stderr.getvalue()

    def install_verified_packet_without_admission(self) -> None:
        packet_root = self.root / "spec/presentations"
        packet = packet_checker._verified_fixture(packet_root)
        (self.root / "handbook").mkdir()
        self.write(
            "handbook/self-test.tex",
            b"\\section{Self-test}\\label{packet:self-test}\n",
        )
        (packet_root / "verified.json").write_text(
            json.dumps(packet, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        rows = admission.build_rows(
            self.root,
            packet_root,
            self.reviewed,
            self.coverage,
            self.register,
        )
        self.projection.write_bytes(admission.csv_bytes(rows))

    def test_exact_empty_projection_is_verified_without_claiming_book_readiness(self) -> None:
        result, stdout, stderr = self.invoke()

        self.assertEqual(result, 0, stderr)
        self.assertIn("PRESENTATION PACKET CORPUS STRUCTURAL CHECK OK", stdout)
        self.assertIn("CONTENT-ADMISSION PROJECTION CHECK OK", stdout)
        self.assertIn("independently admitted 0/0; open 0", stdout)
        self.assertIn(hashlib.sha256(EMPTY_ADMISSION_CSV).hexdigest(), stdout)
        self.assertIn("COMPENDIUM CONTENT/RESTORATION/READINESS: OPEN", stdout)
        self.assertNotIn("NOT IMPLEMENTED", stdout)

    def test_verified_packet_is_not_independently_admitted_by_self_attestation(self) -> None:
        self.install_verified_packet_without_admission()

        result, stdout, stderr = self.invoke()

        self.assertEqual(result, 0, stderr)
        self.assertIn("open: 0; verified: 1", stdout)
        self.assertIn("fulfilled by verified packets 1/1", stdout)
        self.assertIn("independently admitted 0/1; open 1", stdout)

    def test_forged_or_stale_projection_fails_closed(self) -> None:
        self.install_verified_packet_without_admission()
        forged = self.projection.read_bytes().replace(b",OPEN,", b",ADMITTED,", 1)
        self.assertNotEqual(forged, self.projection.read_bytes())
        self.projection.write_bytes(forged)

        result, stdout, stderr = self.invoke()

        self.assertEqual(result, 1)
        self.assertIn("PRESENTATION PACKET CORPUS STRUCTURAL CHECK OK", stdout)
        self.assertIn("content-admission control: FAIL-CLOSED", stdout)
        self.assertIn("CONTENT-ADMISSION PROJECTION CHECK FAILED", stderr)
        self.assertIn("stale or malformed generated projection", stderr)
        self.assertNotIn("independently admitted 1/1", stdout)

    def test_malformed_reviewed_evidence_fails_closed(self) -> None:
        self.reviewed.write_text(
            json.dumps(
                {
                    "schema_version": admission.SCHEMA_VERSION,
                    "packet_root": "spec/presentations",
                    "records": [{}],
                }
            )
            + "\n",
            encoding="utf-8",
        )

        result, stdout, stderr = self.invoke()

        self.assertEqual(result, 1)
        self.assertIn("PRESENTATION PACKET CORPUS STRUCTURAL CHECK OK", stdout)
        self.assertIn("content-admission control: FAIL-CLOSED", stdout)
        self.assertIn("CONTENT-ADMISSION PROJECTION CHECK FAILED", stderr)
        self.assertIn("exact field set required", stderr)

    def test_require_ready_never_treats_zero_packets_as_book_readiness(self) -> None:
        result, stdout, stderr = self.invoke("--require-ready")

        self.assertEqual(result, 1)
        self.assertIn("CONTENT-ADMISSION PROJECTION CHECK OK", stdout)
        self.assertIn("independently admitted 0/0; open 0", stdout)
        self.assertIn("COMPENDIUM CONTENT/RESTORATION/READINESS: OPEN", stdout)
        self.assertIn("do not establish book-level terminal readiness", stderr)


if __name__ == "__main__":
    unittest.main()
