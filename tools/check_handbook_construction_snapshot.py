#!/usr/bin/env python3
"""Verify a pinned manifest against the current non-transient handbook tree.

The check is structural and byte-exact.  It makes no claim about source
fidelity, semantic correctness, completeness, visual quality, or release.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from handbook_tree_manifest import (
    anchored_rows,
    digest,
    live_rows,
    render,
    require_live_equality,
    resolve_candidate_path,
    self_test_file_universe,
    write_new_candidate,
)


ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
MANIFEST = ROOT / "spec/handbook-construction-snapshot.csv"
HISTORICAL_MANIFEST = ROOT / "spec/handbook-audit-snapshot.csv"
CONSTRUCTION_INVENTORY_CSV = ROOT / "spec/handbook-construction-source-inventory.csv"
CONSTRUCTION_INVENTORY_MD = ROOT / "spec/handbook-construction-source-inventory.md"
MANIFEST_SHA256 = "7d736a50cc53eab54cb0cb1eae97ac774e1ffb173b7fa5c1cca572e4f023b48c"
FORBIDDEN_CANDIDATE_PATHS = frozenset(
    {
        MANIFEST,
        HISTORICAL_MANIFEST,
        CONSTRUCTION_INVENTORY_CSV,
        CONSTRUCTION_INVENTORY_MD,
        ROOT / "spec/handbook-source-inventory.csv",
        ROOT / "spec/handbook-source-inventory.md",
    }
)


def verify_current(
    manifest: Path = MANIFEST,
    expected_sha256: str = MANIFEST_SHA256,
    handbook: Path = HANDBOOK,
    root: Path = ROOT,
) -> list[dict[str, str]]:
    """Validate the pinned manifest and require equality with the live tree."""

    self_test_file_universe()
    rows = anchored_rows(manifest, expected_sha256)
    return require_live_equality(rows, handbook, root)


def write_candidate(value: str) -> tuple[Path, bytes]:
    """Write a new, explicitly named candidate under spec without overwrite."""

    self_test_file_universe()
    path = resolve_candidate_path(value, ROOT)
    if path.suffix.lower() != ".csv":
        raise ValueError("construction snapshot candidate must have a .csv suffix")
    raw = render(live_rows(HANDBOOK, ROOT))
    write_new_candidate(
        path,
        raw,
        allowed_root=ROOT / "spec",
        forbidden_paths=FORBIDDEN_CANDIDATE_PATHS,
    )
    return path, raw


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write-candidate",
        metavar="PATH",
        help=(
            "write the live manifest to an explicit, non-existing candidate "
            "path under spec; canonical governed files are forbidden"
        ),
    )
    args = parser.parse_args(argv)
    try:
        if args.write_candidate:
            path, raw = write_candidate(args.write_candidate)
            print(
                f"wrote construction snapshot candidate {path.relative_to(ROOT)}: "
                f"{len(raw):,} bytes, SHA-256 {digest(raw)}"
            )
            print("The candidate is not pinned evidence and makes no content claim.")
            return 0
        rows = verify_current()
    except ValueError as exc:
        print(f"handbook construction snapshot: FAIL ({exc})")
        return 1
    print(f"handbook construction snapshot: VERIFIED ({len(rows)} current files)")
    print("This establishes current non-transient tree equality only.")
    print("It does not establish content correctness or completeness.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
