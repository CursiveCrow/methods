#!/usr/bin/env python3
"""Shared byte-manifest primitives for the handbook source tree.

This module records files, byte counts, and SHA-256 digests.  It does not
infer source fidelity, semantic correctness, completeness, or release status.
"""

from __future__ import annotations

import csv
import hashlib
import io
import re
from pathlib import Path, PurePosixPath


FIELDS = ("path", "bytes", "sha256")
SHA256_RE = re.compile(r"[0-9a-f]{64}")

# These paths are exact build outputs observed or emitted by the handbook
# build.  Exclusion is by full repository-relative path, never by suffix, so
# an otherwise unknown .aux, .pdf, image, class, data, or other input remains
# inside the manifest universe.
EXCLUDED_TRANSIENT_PATHS = frozenset(
    {
        "handbook/main.aux",
        "handbook/main.bbl",
        "handbook/main.bcf",
        "handbook/main.blg",
        "handbook/main.fdb_latexmk",
        "handbook/main.fls",
        "handbook/main.hbentry",
        "handbook/main.hbstatus",
        "handbook/main.idx",
        "handbook/main.ilg",
        "handbook/main.ind",
        "handbook/main.lof",
        "handbook/main.log",
        "handbook/main.lot",
        "handbook/main.out",
        "handbook/main.pdf",
        "handbook/main.run.xml",
        "handbook/main.synctex.gz",
        "handbook/main.toc",
        "handbook/tmp-p08-kozen-build.log",
    }
)


def digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def live_rows(
    handbook: Path,
    root: Path,
    excluded_paths: frozenset[str] = EXCLUDED_TRANSIENT_PATHS,
) -> list[dict[str, str]]:
    """Return canonical rows for every non-transient regular handbook file."""

    handbook = handbook.resolve()
    root = root.resolve()
    try:
        handbook.relative_to(root)
    except ValueError as exc:
        raise ValueError("handbook directory is outside the repository root") from exc
    if not handbook.is_dir():
        raise ValueError(f"handbook directory missing: {handbook}")

    paths: list[Path] = []
    for path in handbook.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"handbook tree contains a symbolic link: {path}")
        if not path.is_file():
            continue
        relative = path.relative_to(root).as_posix()
        if relative not in excluded_paths:
            paths.append(path)
    paths.sort(key=lambda path: path.relative_to(root).as_posix())
    rows: list[dict[str, str]] = []
    for path in paths:
        raw = path.read_bytes()
        rows.append(
            {
                "path": path.relative_to(root).as_posix(),
                "bytes": str(len(raw)),
                "sha256": digest(raw),
            }
        )
    return rows


def render(rows: list[dict[str, str]]) -> bytes:
    """Render rows as canonical UTF-8 CSV with LF line endings."""

    buffer = io.StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return buffer.getvalue().encode("utf-8")


def parse(raw: bytes, *, require_nonempty: bool = True) -> list[dict[str, str]]:
    """Parse and validate a canonical handbook-tree manifest."""

    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("manifest is not UTF-8") from exc
    with io.StringIO(text, newline="") as handle:
        reader = csv.DictReader(handle)
        if tuple(reader.fieldnames or ()) != FIELDS:
            raise ValueError("manifest has an unexpected schema")
        rows = list(reader)
    if require_nonempty and not rows:
        raise ValueError("manifest is empty")

    previous = ""
    seen: set[str] = set()
    for index, row in enumerate(rows, start=2):
        path = row["path"]
        pure = PurePosixPath(path)
        if (
            not path.startswith("handbook/")
            or pure.is_absolute()
            or "\\" in path
            or pure.as_posix() != path
            or any(part in {"", ".", ".."} for part in pure.parts)
        ):
            raise ValueError(f"manifest row {index} has an unsafe path: {path!r}")
        if path in seen:
            raise ValueError(f"manifest contains duplicate path: {path}")
        if previous and path <= previous:
            raise ValueError("manifest paths are not in strict lexical order")
        seen.add(path)
        previous = path
        byte_count = row["bytes"]
        if not byte_count.isascii() or not byte_count.isdecimal():
            raise ValueError(f"manifest row {index} has a non-decimal byte count")
        if str(int(byte_count)) != byte_count:
            raise ValueError(f"manifest row {index} has a non-canonical byte count")
        if not SHA256_RE.fullmatch(row["sha256"]):
            raise ValueError(f"manifest row {index} has an invalid SHA-256 digest")

    if render(rows) != raw:
        raise ValueError("manifest is not in canonical CSV form")
    return rows


def anchored_rows(path: Path, expected_sha256: str) -> list[dict[str, str]]:
    """Validate a pinned manifest as a record, without consulting a live tree."""

    if not path.is_file():
        raise ValueError(f"manifest missing: {path}")
    raw = path.read_bytes()
    actual = digest(raw)
    if expected_sha256 == "PENDING":
        raise ValueError("checker authority is not frozen")
    if actual != expected_sha256:
        raise ValueError(f"manifest drifted: {actual}, expected {expected_sha256}")
    return parse(raw)


def require_live_equality(
    manifest_rows: list[dict[str, str]], handbook: Path, root: Path
) -> list[dict[str, str]]:
    """Require a parsed manifest to equal the current non-transient tree."""

    current = live_rows(handbook, root)
    if manifest_rows != current:
        manifest_by_path = {row["path"]: row for row in manifest_rows}
        current_by_path = {row["path"]: row for row in current}
        missing = sorted(manifest_by_path.keys() - current_by_path.keys())
        added = sorted(current_by_path.keys() - manifest_by_path.keys())
        changed = sorted(
            path
            for path in manifest_by_path.keys() & current_by_path.keys()
            if manifest_by_path[path] != current_by_path[path]
        )
        details: list[str] = []
        if missing:
            details.append(f"missing={len(missing)}")
        if added:
            details.append(f"added={len(added)}")
        if changed:
            details.append(f"changed={len(changed)}")
        suffix = ", ".join(details) if details else "row mismatch"
        raise ValueError(f"handbook source tree drifted ({suffix})")
    return current


def resolve_candidate_path(value: str, root: Path) -> Path:
    """Resolve an explicit candidate path relative to the repository root."""

    path = Path(value)
    if not path.is_absolute():
        path = root / path
    return path.resolve()


def validate_new_candidate_path(
    path: Path,
    *,
    allowed_root: Path,
    forbidden_paths: set[Path] | frozenset[Path] = frozenset(),
) -> Path:
    """Validate and return an explicit, non-existing candidate path."""

    path = path.resolve()
    allowed_root = allowed_root.resolve()
    try:
        path.relative_to(allowed_root)
    except ValueError as exc:
        raise ValueError(f"candidate path is outside {allowed_root}") from exc
    if path in {forbidden.resolve() for forbidden in forbidden_paths}:
        raise ValueError("candidate path is a governed canonical artifact")
    if not path.parent.is_dir() or path.parent.is_symlink():
        raise ValueError("candidate parent must be an existing ordinary directory")
    if path.exists() or path.is_symlink():
        raise ValueError(f"candidate path already exists: {path}")
    return path


def write_new_candidate(
    path: Path,
    raw: bytes,
    *,
    allowed_root: Path,
    forbidden_paths: set[Path] | frozenset[Path] = frozenset(),
) -> None:
    """Create one explicitly named candidate without overwriting any file."""

    path = validate_new_candidate_path(
        path, allowed_root=allowed_root, forbidden_paths=forbidden_paths
    )
    try:
        with path.open("xb") as handle:
            handle.write(raw)
    except FileExistsError as exc:
        raise ValueError(f"candidate path already exists: {path}") from exc


def self_test_file_universe() -> None:
    """Prove suffix-independent inclusion and exact-path transient exclusion."""

    import tempfile

    with tempfile.TemporaryDirectory(prefix="handbook-tree-manifest-") as temp:
        root = Path(temp)
        handbook = root / "handbook"
        handbook.mkdir()
        (handbook / "new-input.cls").write_text("class input\n", encoding="utf-8")
        (handbook / "diagram.png").write_bytes(b"not-a-real-png\x00input")
        (handbook / "other.aux").write_text("not an exact transient\n", encoding="utf-8")
        (handbook / "main.aux").write_text("exact transient\n", encoding="utf-8")
        paths = {row["path"] for row in live_rows(handbook, root)}
        expected = {
            "handbook/diagram.png",
            "handbook/new-input.cls",
            "handbook/other.aux",
        }
        if paths != expected:
            raise ValueError(
                "file-universe self-test failed: "
                f"expected {sorted(expected)}, got {sorted(paths)}"
            )
