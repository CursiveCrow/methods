#!/usr/bin/env python3
"""Fail if either frozen inherited-corpus artifact has drifted."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FROZEN = {
    "tex": {
        "path": "source/formal-logic-reference.tex",
        "bytes": 762835,
        "lines": 17206,
        "sha256": "0509750c13b88a4e18914bd52bde171c725cba14221cbfc2227d7693a2b421cc",
    },
    "pdf": {
        "path": "source/formal-logic-reference.pdf",
        "bytes": 2042303,
        "pages": 251,
        "sha256": "0a8fb84042175343e5ba8bbcf65d4804d8a4019367edb3d22473927a3399bb3f",
    },
}

TOP_LEVEL_FIELDS = {"schema_version", "tex", "pdf"}
RECORD_FIELDS = {
    "tex": {"path", "bytes", "lines", "sha256"},
    "pdf": {"path", "bytes", "pages", "sha256"},
}


def sha256(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def is_exact_int(value: object) -> bool:
    """Return true for an int but not for bool, which subclasses int."""

    return isinstance(value, int) and not isinstance(value, bool)


def validate_manifest(value: object) -> list[str]:
    """Validate the editable record against the exact frozen schema and values."""

    failures: list[str] = []
    if not isinstance(value, dict):
        return ["manifest: top-level JSON value must be an object"]
    if set(value) != TOP_LEVEL_FIELDS:
        failures.append(
            "manifest: fields differ from exact schema: "
            f"{sorted(set(value) ^ TOP_LEVEL_FIELDS)}"
        )
    schema_version = value.get("schema_version")
    if not is_exact_int(schema_version) or schema_version != 1:
        failures.append("manifest: schema_version must be the integer 1")

    for role in ("tex", "pdf"):
        record = value.get(role)
        if not isinstance(record, dict):
            failures.append(f"{role}: record must be an object")
            continue
        expected_fields = RECORD_FIELDS[role]
        if set(record) != expected_fields:
            failures.append(
                f"{role}: fields differ from exact schema: "
                f"{sorted(set(record) ^ expected_fields)}"
            )
        if not isinstance(record.get("path"), str):
            failures.append(f"{role}: path must be a string")
        for field in ("bytes", "lines" if role == "tex" else "pages"):
            if not is_exact_int(record.get(field)):
                failures.append(f"{role}: {field} must be an integer")
        if not isinstance(record.get("sha256"), str):
            failures.append(f"{role}: sha256 must be a string")
        if record != FROZEN[role]:
            failures.append(
                f"{role}: editable manifest disagrees with exact frozen authority"
            )
    return failures


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("spec/inherited-corpus-manifest.json"),
    )
    args = parser.parse_args()

    try:
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print("inherited corpus: FAIL")
        print(f"  manifest: {error}")
        return 1
    failures = validate_manifest(manifest)

    for role in ("tex", "pdf"):
        expected = FROZEN[role]
        path = (ROOT / expected["path"]).resolve()
        if path.parent != (ROOT / "source").resolve():
            failures.append(f"{role}: frozen artifact path leaves source directory")
        if not path.is_file():
            failures.append(f"{role}: missing {path}")
            continue
        actual_bytes = path.stat().st_size
        if actual_bytes != expected["bytes"]:
            failures.append(
                f"{role}: byte size {actual_bytes}, expected {expected['bytes']}"
            )
        actual_hash = sha256(path)
        if actual_hash != expected["sha256"]:
            failures.append(
                f"{role}: SHA-256 {actual_hash}, expected {expected['sha256']}"
            )

    tex_record = FROZEN["tex"]
    tex_path = ROOT / tex_record["path"]
    if tex_path.is_file():
        actual_lines = len(tex_path.read_text(encoding="utf-8").splitlines())
        if actual_lines != tex_record["lines"]:
            failures.append(
                f"tex: line count {actual_lines}, expected {tex_record['lines']}"
            )

    if failures:
        print("inherited corpus: FAIL")
        for failure in failures:
            print(f"  {failure}")
        return 1

    print("inherited corpus: PASS")
    print(
        f"  TeX {tex_record['lines']} lines, SHA-256 {tex_record['sha256']}"
    )
    pdf_record = FROZEN["pdf"]
    print(
        f"  PDF {pdf_record['pages']} pages, SHA-256 {pdf_record['sha256']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
