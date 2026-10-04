#!/usr/bin/env python3
"""Verify the immutable record of the handbook tree used by prior audits.

The historical record is deliberately not compared with the current tree.
Current-tree equality is a separate construction-snapshot control.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from handbook_tree_manifest import anchored_rows


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "spec/handbook-audit-snapshot.csv"
MANIFEST_SHA256 = "63b405b2b9d1384ee32ae963e053d5c971b90dfe34d186fde0d1b2a0b3cec2ba"


def verify_record(
    manifest: Path = MANIFEST, expected_sha256: str = MANIFEST_SHA256
) -> list[dict[str, str]]:
    """Validate the anchored historical bytes and canonical manifest schema."""

    return anchored_rows(manifest, expected_sha256)


def main(argv: list[str] | None = None) -> int:
    # Parsing an option-free command line intentionally makes former write
    # switches hard errors.  Historical evidence has no update mode.
    parser = argparse.ArgumentParser(
        description="verify the pinned historical handbook audit record"
    )
    parser.parse_args(argv)
    try:
        rows = verify_record()
    except ValueError as exc:
        print(f"handbook historical audit snapshot: FAIL ({exc})")
        return 1
    print(f"handbook historical audit snapshot: VERIFIED ({len(rows)} recorded files)")
    print("This verifies an anchored historical record, not the current tree.")
    print("It does not establish content correctness or completeness.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
